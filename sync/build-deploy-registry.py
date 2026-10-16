#!/usr/bin/env python3
"""Build/refresh the SiteGround deploy registry.

- Reads and updates sync/sites.json (the central registry; deploy.sh/setup-repos.sh keep working).
- Refreshes each site's plugin list from the local VVV copy (www/<local_dir>/public_html/wp-content/plugins).
- Writes sync/deploy-registry.json: the trimmed copy that GitHub Actions read. Copy it to
  pegasus-child master at deploy/sites.json (see DEPLOY-SITEGROUND.md).
Usage: python3 sync/build-deploy-registry.py [--child-branches "b1 b2 ..."] [--offline] [--refresh-fingerprints]
  --refresh-fingerprints: re-scan every enabled ssh_host:port (ssh-keyscan in Go client order ecdsa > rsa > ed25519), cross-check
  ~/.ssh/known_hosts, store SHA256 as ssh_fingerprint. Without it, stored fingerprints are kept as-is.
  --known-hosts-only (with --refresh-fingerprints): no network; take fingerprints from ~/.ssh/known_hosts (same key order).
"""
import json, os, re, sys, subprocess, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
SITES = os.path.join(HERE, 'sites.json'); OUT = os.path.join(HERE, 'deploy-registry.json')
DEFAULT_PORT = 18765
# Component repo -> folder name(s) used under wp-content
COMPONENTS = {
  'pegasus': {'type': 'theme', 'folders': ['pegasus'], 'branch': 'master'},
  'pegasus-child': {'type': 'theme', 'folders': ['pegasus-child'], 'branch': 'per-site'},
}
PLUGIN_REPOS = {'pegasus-accordion':'main','pegasus-blog':'master','pegasus-botify':'main','pegasus-callout':'master',
 'pegasus-carousel':'master','pegasus-circle-progress':'master','pegasus-countup':'master','pegasus-masonry':'master',
 'pegasus-navmenu':'master','pegasus-onepage':'master','pegasus-packery':'master','pegasus-popup':'master',
 'pegasus-postgrid':'master','pegasus-posts-filter':'master','pegasus-slider':'master','pegasus-tabs':'master',
 'pegasus-toggleslide':'master','pegasus-wow':'master'}
FOLDER_ALIASES = {'pegasus-postgrid': ['pegasus-postgrid', 'pegasus-post-grid']}
for r, b in PLUGIN_REPOS.items():
    COMPONENTS[r] = {'type': 'plugin', 'folders': FOLDER_ALIASES.get(r, [r]), 'branch': b}
FOLDER_TO_REPO = {f: r for r, c in COMPONENTS.items() for f in c['folders']}

# The 37 SiteGround domains Jim listed on 2026-10-12, plus events.uptownlifegroup.com (already auto-deployed).
# domain -> (registry key, local VVV dir or None)
DOMAINS = {
 'visionquestdevelopment.com': ('vqdevelopment', 'visionquest'), 'visionquestdev.com': ('vqdev', None),
 'avenafamilyphotos.com': ('avena', None), 'meowweretalkin.com': ('meowweretalkin', None),
 'pegasustheme.com': ('pegasustheme', 'pegasustheme'), 'visionquestgoods.com': ('vqgoods', 'visionquestgoods'),
 'vqdev.com': ('vqdevcom', None), 'sagescnc.com': ('sagescnc', 'sagecnc'), 'chrishixson.com': ('chrishixson', None),
 'qbiqcamp.com': ('qbiqcamp', 'qbiqcamp'), 'qbiqsystem.com': ('qbiqsystem', 'qbiqsystem'),
 'qbroundtable.com': ('qbroundtable', None), 'quarterbackuniverse.com': ('quarterbackuniverse', None),
 'theadvcompany.com': ('advcompany', None), 'theshootout.camp': ('theshootout', None),
 'vineandvisionconsulting.com': ('vineandvision', 'vineandvision'), 'qb-tv.com': ('qbtv', None),
 '34oakcontracting.com': ('34oak', '34oak'), 'top100proday.com': ('top100proday', None),
 'uptownlifegroup.com': ('ulg', 'uptownlifegroup'), 'events.uptownlifegroup.com': ('ulg-events', 'ulgevents'),
 'theloft.com': ('theloft', 'theloftnew'), 'mabellas.com': ('mabellas', 'mabellas'), 'saltcellar.com': ('saltcellar', 'saltcellar'),
 'themixmarket.com': ('mixmarket', 'mixmarket'), 'tommygs.com': ('tommygs', 'tommygs'),
 'russellcontracting.org': ('russelcontracting', 'russelcontracting'), 'righthandrenovations.com': ('righthandrenovations', None),
 'organizepluscleaning.com': ('organizepluscleaning', 'organizepluscleaning'), 'ricecapitalfund.com': ('ricecapital', 'ricecapital'),
 'sugarpeddler.com': ('sugarpeddler', 'sugarpeddler'), 'mamakayscheesecakes.com': ('mamakay', 'mamakay'),
 'gen2automation.com': ('gentwo', 'gentwo'), 'osps26.com': ('osps26', 'osps26'),
 'renecatherinedesigns.com': ('renecatherinedesign', 'renecatherinedesign'), 'networkingnorth.com': ('networkingnorth', None),
 'valorcarega.com': ('valorcare', 'valorcare'), 'cadence-group.com': ('cadence-group', 'cadence-group'),
}

# Sites staged in a subfolder of another SiteGround account (environment=staging).
# key -> (domain label, parent account key in sites.json, subfolder under parent public_html, local dir, child branch)
STAGING = {
 'qbiqsystem-staging': ('qbiqsystem.com/test (staged at chrishixson.com/test)', 'chrishixson', 'test', 'qbiqsystem', 'qbiqsystem_theme'),
 'hfhs-staging': ('visionquestdev.com/hfhsga', 'vqdev', 'hfhsga', 'hfhsga', 'hfhsga_theme'),
}
# Known registry branch names that don't exist on GitHub -> the branch actually used (verified from local VVV copies)
BRANCH_FIX = {'sagescnc': 'sage_theme', 'russelcontracting': 'russell_theme', 'righthandrenovations': 'righthandrenovations'}

# Server folder names we could not confirm (path kept from Jim's original sync/sites.json, which is authoritative until checked).
PATH_UNVERIFIED = {}
# Server folders confirmed by Jim (2026-10-12): key -> remote_path
PATH_CONFIRMED = {'renecatherinedesign': '/home/u2742-urgzibllpjue/www/renecatherinedesigns.com/public_html'}

def detect_default_branches():
    # Ask GitHub for each repo's current default branch (HEAD symref); fall back to the hardcoded value offline.
    if '--offline' in sys.argv: return
    for repo, c in COMPONENTS.items():
        try:
            out = subprocess.run(['git', 'ls-remote', '--symref', f'git@github.com:Visionquest-Development/{repo}.git', 'HEAD'],
                                 capture_output=True, text=True, timeout=30).stdout
            for line in out.splitlines():
                if line.startswith('ref: refs/heads/'):
                    b = line.split()[1][len('refs/heads/'):]
                    if repo == 'pegasus-child': c['default_branch'] = b
                    else: c['branch'] = b
        except Exception as e:
            print(f'warning: could not read default branch of {repo}: {e}', file=sys.stderr)

FP_RE = re.compile(r'^SHA256:[A-Za-z0-9+/]{43}=?$')
_fp_cache = {}
# appleboy/ssh-action -> drone-ssh -> golang.org/x/crypto/ssh negotiates host key types in this order
# (defaultHostKeyAlgos): ECDSA, then RSA (rsa-sha2-256/512), then ed25519 LAST. The pin must be the fingerprint of the
# key type the server will actually present to that client, NOT ed25519 just because OpenSSH prefers it.
GO_KEY_ORDER = [('ecdsa', 'ECDSA'), ('rsa', 'RSA'), ('ed25519', 'ED25519')]

def _known_hosts_fps(name):
    out = subprocess.run(['ssh-keygen', '-F', name], capture_output=True, text=True).stdout
    kh = '\n'.join(l for l in out.splitlines() if l and not l.startswith('#'))
    if not kh: return {}
    res = {}
    for x in subprocess.run(['ssh-keygen', '-lf', '-'], input=kh + '\n', capture_output=True, text=True).stdout.splitlines():
        f = x.split()
        if len(f) > 2: res.setdefault(f[-1].strip('()').upper(), f[1])
    return res

def scan_fingerprint(host, port, known_hosts_only=False):
    """Return (fingerprint or '', status) for host:port, for the key type Go's ssh client will negotiate.
    status: pinned | pinned-known_hosts | missing | mismatch."""
    if (host, port) in _fp_cache: return _fp_cache[(host, port)]
    name = host if int(port) == 22 else f'[{host}]:{port}'
    known = _known_hosts_fps(name)
    fp = typ = ''
    if not known_hosts_only:
        time.sleep(float(os.environ.get('KEYSCAN_DELAY', '5')))  # be gentle: SiteGround firewalls rapid scanners
        for t, T in GO_KEY_ORDER:
            try:
                k = subprocess.run(['ssh-keyscan', '-T', '10', '-p', str(port), '-t', t, host], capture_output=True, text=True, timeout=30).stdout
            except Exception: k = ''
            k = '\n'.join(l for l in k.splitlines() if l and not l.startswith('#'))
            if k:
                o = subprocess.run(['ssh-keygen', '-lf', '-'], input=k + '\n', capture_output=True, text=True).stdout.split()
                if len(o) > 1 and FP_RE.match(o[1]): fp, typ = o[1], T; break
    if fp:
        res = (fp, 'pinned')
        if typ in known and known[typ] != fp:
            print(f'WARNING: {name} keyscan {typ} {fp} != known_hosts {known[typ]}; NOT pinned', file=sys.stderr); res = ('', 'mismatch')
    else:
        # No scan (or scan failed): fall back to the user's known_hosts, taking the key type Go would negotiate.
        # Only valid if known_hosts lists every key type the server offers (OpenSSH UpdateHostKeys records them all).
        res = ('', 'missing')
        for _, T in GO_KEY_ORDER:
            if T in known and FP_RE.match(known[T]): res = (known[T], 'pinned-known_hosts'); break
    _fp_cache[(host, port)] = res
    return res

def apply_fingerprint(s, refresh):
    # s is a sites.json entry (source of truth). Keeps the stored value unless --refresh-fingerprints.
    if refresh and s.get('ssh_host'):
        fp, st = scan_fingerprint(s['ssh_host'], s.get('ssh_port', DEFAULT_PORT), '--known-hosts-only' in sys.argv)
        s['ssh_fingerprint'] = fp; s['ssh_fingerprint_status'] = st   # never keep an unverified old pin
    fp = s.get('ssh_fingerprint', '')
    if fp and not FP_RE.match(fp): print(f"WARNING: invalid ssh_fingerprint for {s.get('domain')}; ignored", file=sys.stderr); fp = ''
    return fp

def render_workflows(reg):
    # Render one workflow per repo from deploy-workflow/deploy-siteground.template.yml with an explicit push allowlist.
    wd = os.path.join(HERE, 'deploy-workflow'); tpl = open(os.path.join(wd, 'deploy-siteground.template.yml')).read()
    script = open(os.path.join(wd, 'remote-deploy.sh')).read().rstrip('\n').split('\n')
    tpl = tpl.replace('            #DEPLOY_SCRIPT#', '\n'.join(('            ' + l) if l else '' for l in script))
    out = os.path.join(wd, 'out'); os.makedirs(out, exist_ok=True)
    child = sorted({v['child_branch'] for v in reg['sites'].values() if v['child_branch'] and v['child_branch'] != 'master' and v.get('enabled')})
    for repo, c in reg['components'].items():
        # Theme/plugin repos: allow both names so a master->main rename keeps working; the plan job only deploys the current default.
        br = child if repo == 'pegasus-child' else ['master', 'main']
        txt = tpl.replace('#BRANCHES#', '\n'.join('      - ' + json.dumps(b) for b in br))
        open(os.path.join(out, repo + '.yml'), 'w').write(txt)
    return child

def local_info(d):
    base = os.path.join(ROOT, 'www', d or '', 'public_html', 'wp-content')
    if not d or not os.path.isdir(base): return None, None
    pl = sorted(FOLDER_TO_REPO[f] for f in os.listdir(os.path.join(base, 'plugins')) if f in FOLDER_TO_REPO and COMPONENTS[FOLDER_TO_REPO[f]]['type']=='plugin')
    other = sorted(f for f in os.listdir(os.path.join(base, 'plugins')) if f in ('wp-bootstrap-hooks', 'vqdev-toast'))
    br = None; cp = os.path.join(base, 'themes', 'pegasus-child')
    if os.path.isdir(os.path.join(cp, '.git')):
        br = subprocess.run(['git', '-C', cp, 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True).stdout.strip()
    return pl + other, br

def main():
    detect_default_branches()
    data = json.load(open(SITES)); sites = data['sites']
    child_branches = None
    refresh = '--refresh-fingerprints' in sys.argv
    if '--child-branches' in sys.argv: child_branches = set(sys.argv[sys.argv.index('--child-branches') + 1].split())
    by_domain = {v.get('domain'): k for k, v in sites.items()}
    reg = {'_comment': 'Generated by vagrant-local/sync/build-deploy-registry.py from sync/sites.json. Do not edit by hand.',
           'version': 1, 'defaults': {'ssh_port': DEFAULT_PORT}, 'components': COMPONENTS, 'sites': {}}
    for dom, (key, ldir) in DOMAINS.items():
        k = by_domain.get(dom) or (key if key in sites else None)
        if dom == 'renecatherinedesigns.com': k = 'renecatherinedesign'
        if dom == 'cadence-group.com': k = 'cadence-group'
        if k is None:
            k = key; sites[k] = {'name': dom, 'domain': dom, 'ssh_user': '', 'ssh_host': '', 'ssh_command': '', 'remote_path': '',
                                 'themes': {'pegasus': {'branch': 'master'}, 'pegasus-child': {'branch': ''}}, 'plugins': []}
        s = sites[k]; s['domain'] = dom; s['siteground'] = True
        if ldir: s['local_dir'] = ldir
        pl, lbr = local_info(ldir)
        if pl is not None: s['plugins'] = pl; s['plugins_source'] = 'local-vvv'
        else: s['plugins_source'] = 'unknown' if not s.get('plugins') else 'sites.json (unverified)'
        if k in BRANCH_FIX: s['themes']['pegasus-child']['branch'] = BRANCH_FIX[k]
        s.setdefault('environment', 'live')
        s.setdefault('themes', {}).setdefault('pegasus', {})['branch'] = COMPONENTS['pegasus']['branch']
        cb = s.setdefault('themes', {}).setdefault('pegasus-child', {}).get('branch', '')
        if not cb and lbr and lbr not in ('master', 'HEAD'): cb = lbr; s['themes']['pegasus-child']['branch'] = cb
        s.setdefault('ssh_port', DEFAULT_PORT); s.setdefault('deploy_key_status', 'unknown')
        if k in PATH_CONFIRMED: s['remote_path'] = PATH_CONFIRMED[k]; s['path_verified'] = True; s.pop('path_note', None)
        if k in PATH_UNVERIFIED: s['path_verified'] = False; s['path_note'] = PATH_UNVERIFIED[k]
        if s.get('remote_path'): s['wp_content'] = s['remote_path'].rstrip('/') + '/wp-content'
        if child_branches is not None: s['themes']['pegasus-child']['branch_exists'] = cb in child_branches
        ok = bool(s.get('ssh_host') and s.get('ssh_user') and s.get('remote_path'))
        reg['sites'][k] = {'domain': dom, 'environment': s.get('environment', 'live'), 'enabled': ok, 'ssh_host': s.get('ssh_host', ''), 'ssh_user': s.get('ssh_user', ''),
            'ssh_port': s.get('ssh_port', DEFAULT_PORT), 'wp_content': s.get('wp_content', ''), 'child_branch': cb,
            'plugins': s.get('plugins') if s['plugins_source'] != 'unknown' else None,
            'ssh_fingerprint': apply_fingerprint(s, refresh and ok)}
    for k, (label, parent, sub, ldir, cb) in STAGING.items():
        par = sites[parent]
        s = sites.setdefault(k, {'name': label, 'themes': {'pegasus': {'branch': 'master'}, 'pegasus-child': {'branch': cb}}})
        s.update({'domain': label, 'environment': 'staging', 'parent_site': parent, 'siteground': True, 'local_dir': ldir,
                  'ssh_user': par['ssh_user'], 'ssh_host': par['ssh_host'], 'ssh_command': par.get('ssh_command', ''),
                  'remote_path': par['remote_path'].rstrip('/') + '/' + sub, 'ssh_port': par.get('ssh_port', DEFAULT_PORT),
                  'path_verified': False})
        s.setdefault('deploy_key_status', 'unknown')
        s['wp_content'] = s['remote_path'] + '/wp-content'
        pl, _ = local_info(ldir); s['plugins'] = pl or []; s['plugins_source'] = 'local-vvv'
        if child_branches is not None: s['themes']['pegasus-child']['branch_exists'] = cb in child_branches
        reg['sites'][k] = {'domain': label, 'environment': 'staging', 'enabled': True, 'ssh_host': s['ssh_host'], 'ssh_user': s['ssh_user'],
            'ssh_port': s['ssh_port'], 'wp_content': s['wp_content'], 'child_branch': cb, 'plugins': s['plugins'],
            'ssh_fingerprint': apply_fingerprint(s, refresh)}
    rp = os.path.join(HERE, 'repos.json')
    if os.path.exists(rp):  # git-status.sh reads repos.json; keep the parent-theme branch in sync too
        rj = json.load(open(rp))
        for v in rj.get('sites', {}).values():
            if 'pegasus' in v.get('themes', {}): v['themes']['pegasus']['branch'] = COMPONENTS['pegasus']['branch']
        json.dump(rj, open(rp, 'w'), indent=2); open(rp, 'a').write('\n')
    json.dump(data, open(SITES, 'w'), indent=2); open(SITES, 'a').write('\n')
    json.dump(reg, open(OUT, 'w'), indent=2); open(OUT, 'a').write('\n')
    child = render_workflows(reg)
    en = [k for k, v in reg['sites'].items() if v['enabled']]
    print(f"rendered workflows for {len(reg['components'])} repos; pegasus-child push allowlist: {len(child)} branches")
    pinned = [k for k in en if reg['sites'][k]['ssh_fingerprint']]
    print(f"host key fingerprints: {len(pinned)}/{len(en)} enabled sites pinned; unpinned (deploy SKIPs): {', '.join(sorted(set(en) - set(pinned))) or 'none'}")
    print(f"{len(reg['sites'])} SiteGround sites, {len(en)} enabled (host/user/path known); wrote {OUT}")
main()
