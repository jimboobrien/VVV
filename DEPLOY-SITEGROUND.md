# SiteGround auto-deploy (GitHub Actions)

Last updated 2026-10-12. When code is pushed to GitHub, the affected live (or staging) SiteGround sites run `git pull --ff-only` in the matching theme or plugin folder.

## Architecture

```
vagrant-local/sync/sites.json            <- central registry (edit this)
        |  sync/pegasus.sh registry --child-branches auto
        v
vagrant-local/sync/deploy-registry.json  <- generated, trimmed copy
        |  copy to .github/deploy/sites.json in each repo (via PRs); also renders per-repo workflows
        v
.github/deploy/sites.json vendored in every repo (pegasus-child reads its master copy via actions/checkout)
        +  sync/pegasus.sh workflow render <repo> (sync/deploy-siteground.template.yml + sync/remote-deploy.sh; stdout only)
```

There is one identical workflow file, `.github/workflows/deploy-siteground.yml`, in each of these repos:
- `pegasus`
- `pegasus-child`
- all 18 `pegasus-*` plugin repos

Each run has two jobs:

1. **plan** downloads the registry and builds a matrix of target sites.
   - **pegasus-child:** the sites whose `child_branch` equals the pushed branch. A push to `master` or any unmapped branch deploys nothing.
   - **pegasus (parent theme):** every enabled site, on a push to the default branch only.
   - **plugin repos:** sites whose `plugins` list contains the repo, plus sites whose list is unknown (`null`). Default branch only. Folder aliases are in `components`, e.g. `pegasus-postgrid` is installed as `pegasus-post-grid` on some sites.
   - Sites with `enabled: false` (no SSH host/user/path) are skipped with a notice.
   - If secret `SITEGROUND_SSH_KEY` is missing, or the registry can't be downloaded, the run ends green with a notice. It does not fail.
2. **deploy** runs one job per site (`fail-fast: false`, so each site gets its own result) using `appleboy/ssh-action`, the same pattern the old pegasus-child workflow used. On the server it:
   - `cd <wp_content>/<themes|plugins>/<folder>`
   - skips if the folder is missing, isn't a git checkout, or is on an unexpected branch
   - **fails** if the server copy has modified tracked files
   - otherwise runs `git fetch --prune origin && git pull --ff-only origin <branch>`

Manual runs: Actions → "Deploy to SiteGround" → Run workflow. Set `only_site` to a registry key to deploy just that site.

**Behavior change vs. the old pegasus-child workflow:** the old one ran `git checkout <branch> && git pull` (merge pull) for 7–28 hard-coded sites. The new one uses `--ff-only` and never switches branches.

## Security hardening (2026-10-12, after Bugbot and Security Reviewer findings on pegasus-child#4)

- **Push allowlist:**
  - pegasus-child `on.push.branches` lists only the mapped site branches (31 today). `sync/lib/build_registry.py` regenerates the list into the rendered workflow (`sync/pegasus.sh workflow render pegasus-child`).
  - pegasus and the plugin repos allow only their default branch: `master`, or `main` for accordion and botify.
- **Permissions:** `permissions: contents: read`.
- **No GitHub Environments:** Jim decided against them. Secrets are organization secrets visible only to the 20 pegasus repos.
- **No templating into remote bash:** values reach the server script (`sync/remote-deploy.sh`) only as env vars via `appleboy/ssh-action` `envs:`.
- **Input validation:** the plan step drops, with a `::warning`, any entry failing these checks:
  - branch `^[A-Za-z0-9._/-]+$`
  - wp_content `^/home/<user>/www/<domain>/public_html(/sub)*/wp-content$`
  - kind theme|plugin
  - folders `^[A-Za-z0-9._-]+$`
  - host `^[A-Za-z0-9.-]+$`
  - user `^[A-Za-z0-9._-]+$`
  - port numeric
- **Pinned registry:** I chose to vendor it rather than pin a SHA. Each plugin/theme repo reads `.github/deploy/sites.json` from the commit being deployed, so a registry change has to go through that repo's own review. pegasus-child reads its registry from its own `master` (same repo, protect it).
  - To update: run `sync/lib/build_registry.py`, then PR the new `sites.json` (and the rendered workflow if branches changed) into each repo.
- **Pinned actions:**
  - `appleboy/ssh-action@0ff4204d59e8e51228ff73bce53f80d53301dee2` (v1.2.5; upgraded from v1.0.3, which always echoed the script to the log. v1.2.5 echoes it only with `debug: true`, and we set `debug: false`)
  - `actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683` (v4.2.2)
- **No `script_stop`:** the server script never fails on "not installed"; it SKIPs. Real errors exit 1 explicitly.

**Accepted risk:** a user with write access could read the org secrets through an edited workflow. Jim is the sole developer of the org and trusts anyone he adds, so this risk is accepted.

Branch protection or rulesets on `master` and the site branches (no force-push or deletion) are **optional** extra hardening, not required.

## PRs (open, not merged)

- pegasus-child: https://github.com/Visionquest-Development/pegasus-child/pull/4 (workflow + `.github/deploy/sites.json`). Merge it before running the site-branch rollout script.
- pegasus: https://github.com/Visionquest-Development/pegasus/pull/18
- Plugins, all on branch `chore/siteground-auto-deploy`:
  - accordion #1, blog #2, botify #2, callout #1, carousel #3, circle-progress #2, countup #2, masonry #2
  - navmenu #2, onepage #3, packery #2, popup #3, postgrid #2, posts-filter #1, slider #2, tabs #1, toggleslide #1, wow #2

After merging pegasus-child#4, push the workflow to every site branch. GitHub runs the workflow file from the pushed branch, so each site branch needs its own copy:

```bash
sync/pegasus.sh rollout-child                 # dry run
sync/pegasus.sh rollout-child --push          # all mapped branches (each push deploys that site)
sync/pegasus.sh rollout-child --push mabellas_theme   # one branch
```

## Secrets Jim must add (organization secrets, restricted to the 20 pegasus repos)

1. Open GitHub → **Visionquest-Development** → Settings → Secrets and variables → Actions → **New organization secret**.
2. For each secret below, set **Repository access** to **Selected repositories**. Pick `pegasus`, `pegasus-child` and the 18 `pegasus-*` plugin repos:
   - accordion, blog, botify, callout, carousel, circle-progress, countup, masonry, navmenu
   - onepage, packery, popup, postgrid, posts-filter, slider, tabs, toggleslide, wow
3. Delete pegasus-child's old **repository** secrets with the same names, or leave them identical. A repository secret overrides an org secret of the same name.

| Secret | Value | Notes |
|---|---|---|
| `SITEGROUND_SSH_KEY` | private key of the ULG SiteGround key (`~/.ssh/ulg_siteground`, the "ulg_key") | Whole file including the BEGIN/END lines. |
| `SITEGROUND_SSH_PASSPHRASE` | that key's passphrase | `sync/.env` shows the key has one. |
| `SITEGROUND_SSH_PORT` | `18765` | Optional; it falls back to `ssh_port` in the registry. |

Without `SITEGROUND_SSH_KEY`, each workflow logs a notice and exits successfully.

## Per-server setup checklist

For each site, the workflow needs:

1. **SSH access with the ULG key.** In SiteGround Site Tools → Devs → SSH Keys Manager, import the **public** key for `ulg_siteground`, or confirm it is already there. Test with `ssh -i ~/.ssh/ulg_siteground -p 18765 user@host echo ok`.
2. **The server must be able to `git fetch` from GitHub.** All 20 repos are public.
   - **HTTPS remotes** (`https://github.com/Visionquest-Development/<repo>.git`) need no key. This is the simplest option.
   - **`git@github.com:` remotes** need an SSH key on the server that GitHub accepts:
     - Run `ssh-keygen -t ed25519` on the server (or reuse the server's existing key).
     - Add its public key to GitHub, either as a deploy key per repo (one key can only be a deploy key for **one** repo) or on a machine user / Jim's account.
     - `sync/pegasus.sh setup` already has a "show/generate SSH key" helper.
   - Check with `cd wp-content/plugins/<repo> && git remote -v && git fetch` on the server.
3. **Each theme/plugin folder on the server is a git clone** on the expected branch: `master`/`main`, or the site's pegasus-child branch. Use `sync/pegasus.sh setup` to clone any that are missing.
4. **No uncommitted edits on the server** (otherwise that site's job fails on purpose).

Set `deploy_key_status` in `sync/sites.json` to `ok` once a site passes all four checks. Every site is `unknown` today: deploy-key status was not verified on any server.

## Site registry (generated 2026-10-12)

Columns:
- **Plugins**: which `pegasus-*` / `wp-bootstrap-hooks` / `vqdev-toast` plugins the workflows deploy to that site.
  - `local-vvv` means it was read from the local VVV copy.
  - `sites.json (unverified)` comes from the older sync config.
  - `unknown` means plugin workflows target the site anyway and skip it if the folder isn't there.
- **Deploy key**: status of the GitHub deploy key on the server (step 2 of the checklist).

| Key | Domain | Env | Enabled | SSH | pegasus-child branch | Plugins | Deploy key |
|---|---|---|---|---|---|---|---|
| `vqdevelopment` | visionquestdevelopment.com | live | yes | u795-gsjmrktis7i1@ssh.visionquestdevelopment.com | vqdev_theme | local-vvv: pegasus-botify, pegasus-carousel, pegasus-slider, wp-bootstrap-hooks | unknown |
| `vqdev` | visionquestdev.com | live | yes | u137-u0edzwblljc1@ssh.visionquestdev.com | visionquestdev_theme ⚠ not on GitHub | sites.json (unverified): pegasus-carousel, pegasus-slider, wp-bootstrap-hooks | unknown |
| `avena` | avenafamilyphotos.com | live | yes | u2668-1czijvloaqmy@ssh.avenafamilyphotos.com | avena_theme ⚠ not on GitHub | sites.json (unverified): pegasus-carousel, pegasus-slider, wp-bootstrap-hooks | unknown |
| `meowweretalkin` | meowweretalkin.com | live | yes | u2373-whpzjvnzbcyl@ssh.meowweretalkin.com | meowweretalkin_theme ⚠ not on GitHub | sites.json (unverified): pegasus-carousel, wp-bootstrap-hooks | unknown |
| `pegasustheme` | pegasustheme.com | live | yes | u2375-bnxmykzebbol@ssh.pegasustheme.com | pegasustheme_child | local-vvv: pegasus-blog, pegasus-callout, pegasus-carousel, pegasus-circle-progress, pegasus-countup, pegasus-masonry, pegasus-navmenu, pegasus-onepage, pegasus-packery, pegasus-popup, pegasus-postgrid, pegasus-posts-filter, pegasus-slider, pegasus-tabs, pegasus-toggleslide, pegasus-wow, wp-bootstrap-hooks | unknown |
| `vqgoods` | visionquestgoods.com | live | yes | u1448-xyecwpzvlm05@gvam1224.siteground.biz | vqgoods_theme ⚠ not on GitHub | local-vvv: none | unknown |
| `vqdevcom` | vqdev.com | live | **no – needs SSH host/user/path** | ?@? | — | unknown | unknown |
| `sagescnc` | sagescnc.com | live | yes | u1896-o95aamxni69r@ssh.sagescnc.com | sage_theme | local-vvv: pegasus-accordion, pegasus-carousel, pegasus-tabs, wp-bootstrap-hooks | unknown |
| `chrishixson` | chrishixson.com | live | yes | u869-geq9wwrhqrna@gvam1007.siteground.biz | chrishixson_theme ⚠ not on GitHub | sites.json (unverified): pegasus-carousel, pegasus-slider, wp-bootstrap-hooks | unknown |
| `qbiqcamp` | qbiqcamp.com | live | yes | u3018-28ezo8zzg2yz@ssh.qbiqcamp.com | qbiqcamp_theme | local-vvv: pegasus-carousel, pegasus-onepage, pegasus-packery, wp-bootstrap-hooks | unknown |
| `qbiqsystem` | qbiqsystem.com | live | yes | u436-ep3uiws3fvge@gvam1008.siteground.biz | qbiqsystem_theme | local-vvv: pegasus-carousel, pegasus-slider, pegasus-wow, wp-bootstrap-hooks | unknown |
| `qbroundtable` | qbroundtable.com | live | yes | u1153-di2xlglhg6jr@ssh.qbroundtable.com | qbroundtable_theme ⚠ not on GitHub | sites.json (unverified): pegasus-carousel, wp-bootstrap-hooks | unknown |
| `quarterbackuniverse` | quarterbackuniverse.com | live | **no – needs SSH host/user/path** | ?@? | — | unknown | unknown |
| `advcompany` | theadvcompany.com | live | yes | u592-x2l2hh9agfst@gvam1008.siteground.biz | advcompany_theme ⚠ not on GitHub | sites.json (unverified): pegasus-carousel, pegasus-slider, wp-bootstrap-hooks | unknown |
| `theshootout` | theshootout.camp | live | yes | u1059-lbxrgueukvoh@ssh.theshootout.camp | theshootout_theme ⚠ not on GitHub | sites.json (unverified): pegasus-carousel, pegasus-slider, wp-bootstrap-hooks | unknown |
| `vineandvision` | vineandvisionconsulting.com | live | yes | u2017-qcevdn2ytb46@ssh.vineandvisionconsulting.com | vineandvision_theme | local-vvv: pegasus-callout, pegasus-wow, wp-bootstrap-hooks | unknown |
| `qbtv` | qb-tv.com | live | **no – needs SSH host/user/path** | ?@? | — | unknown | unknown |
| `34oak` | 34oakcontracting.com | live | yes | u3139-as2zskfuqrlw@gvam1082.siteground.biz | 34oak_theme | local-vvv: pegasus-carousel, pegasus-masonry, pegasus-packery, pegasus-slider, pegasus-wow, wp-bootstrap-hooks | unknown |
| `top100proday` | top100proday.com | live | yes | u2547-1s1cfrj9bp8f@ssh.top100proday.com | top100proday_theme ⚠ not on GitHub | sites.json (unverified): pegasus-carousel, pegasus-slider, wp-bootstrap-hooks | unknown |
| `ulg` | uptownlifegroup.com | live | yes | u2337-sdvymoa8u5vg@gvam1201.siteground.biz | ulg_theme | local-vvv: pegasus-accordion, pegasus-carousel, pegasus-slider, pegasus-toggleslide, pegasus-wow, wp-bootstrap-hooks | unknown |
| `ulg-events` | events.uptownlifegroup.com | live | yes | u2337-sdvymoa8u5vg@gvam1201.siteground.biz | ulg_events_theme | local-vvv: pegasus-carousel, pegasus-slider, pegasus-wow, wp-bootstrap-hooks | unknown |
| `theloft` | theloft.com | live | yes | u2322-twgfllmscyih@gvam1201.siteground.biz | theloft2025_theme | local-vvv: pegasus-carousel, pegasus-packery, pegasus-slider, pegasus-wow, vqdev-toast, wp-bootstrap-hooks | unknown |
| `mabellas` | mabellas.com | live | yes | u2334-rmtgm55yo6gg@gvam1201.siteground.biz | mabellas_theme | local-vvv: pegasus-carousel, pegasus-slider, pegasus-wow, vqdev-toast, wp-bootstrap-hooks | unknown |
| `saltcellar` | saltcellar.com | live | yes | u1922-ox3nr6uplk2h@gvam1248.siteground.biz | saltcellar_theme | local-vvv: pegasus-carousel, pegasus-slider, pegasus-tabs, pegasus-wow, vqdev-toast, wp-bootstrap-hooks | unknown |
| `mixmarket` | themixmarket.com | live | yes | u1926-nm5r7lzdccbc@gvam1248.siteground.biz | mixmarket_theme | local-vvv: pegasus-carousel, pegasus-slider, pegasus-wow, vqdev-toast, wp-bootstrap-hooks | unknown |
| `tommygs` | tommygs.com | live | yes | u1929-p96clzjdofva@gvam1248.siteground.biz | tommygs_theme | local-vvv: pegasus-carousel, pegasus-slider, pegasus-wow, vqdev-toast, wp-bootstrap-hooks | unknown |
| `russelcontracting` | russellcontracting.org | live | yes | u2186-ihxeklzicf7p@ssh.russellcontracting.org | russell_theme | local-vvv: pegasus-carousel, pegasus-masonry, pegasus-slider, pegasus-wow, wp-bootstrap-hooks | unknown |
| `righthandrenovations` | righthandrenovations.com | live | **no – needs SSH host/user/path** | ?@? | righthandrenovations | unknown | unknown |
| `organizepluscleaning` | organizepluscleaning.com | live | **no – needs SSH host/user/path** | ?@? | organizepluscleaning | local-vvv: pegasus-carousel, wp-bootstrap-hooks | unknown |
| `ricecapital` | ricecapitalfund.com | live | yes | u3053-bxgyinhxxknr@gvam1137.siteground.biz | ricecapital_theme | local-vvv: wp-bootstrap-hooks | unknown |
| `sugarpeddler` | sugarpeddler.com | live | yes | u2821-kszudcgjgqwe@gvam1168.siteground.biz | sugarpeddler_theme | local-vvv: pegasus-carousel, pegasus-slider, pegasus-wow, vqdev-toast, wp-bootstrap-hooks | unknown |
| `mamakay` | mamakayscheesecakes.com | live | **no – needs SSH host/user/path** | ?@? | — | local-vvv: pegasus-carousel, pegasus-slider, pegasus-wow, wp-bootstrap-hooks | unknown |
| `gentwo` | gen2automation.com | live | yes | u2607-33glsnvdafav@gtxm1263.siteground.biz | gentwo_theme | local-vvv: pegasus-carousel, pegasus-slider, pegasus-wow, wp-bootstrap-hooks | unknown |
| `osps26` | osps26.com | live | yes | u899-mruelycumg2h@gtxm1338.siteground.biz | osps26_theme | local-vvv: wp-bootstrap-hooks | unknown |
| `renecatherinedesign` | renecatherinedesigns.com | live | yes | u2742-urgzibllpjue@gvam1254.siteground.biz | renecdesign_theme | local-vvv: pegasus-carousel, pegasus-slider, pegasus-wow, wp-bootstrap-hooks | unknown |
| `networkingnorth` | networkingnorth.com | live | **no – needs SSH host/user/path** | ?@? | — | unknown | unknown |
| `valorcare` | valorcarega.com | live | yes | u3161-8gdgsgcscocg@ssh.valorcarega.com | valorcare_theme | local-vvv: pegasus-carousel, pegasus-slider, pegasus-wow, wp-bootstrap-hooks | unknown |
| `cadence-group` | cadence-group.com | live | **no – needs SSH host/user/path** | ?@? | cadence_group_theme | local-vvv: pegasus-accordion, pegasus-carousel, pegasus-postgrid, pegasus-slider, pegasus-tabs, wp-bootstrap-hooks | unknown |
| `qbiqsystem-staging` | qbiqsystem.com/test (staged at chrishixson.com/test) | staging | yes | u869-geq9wwrhqrna@gvam1007.siteground.biz | qbiqsystem_theme | local-vvv: pegasus-carousel, pegasus-slider, pegasus-wow, wp-bootstrap-hooks | unknown |
| `hfhs-staging` | visionquestdev.com/hfhs | staging | yes | u137-u0edzwblljc1@ssh.visionquestdev.com | hfhsga_theme | local-vvv: pegasus-accordion, pegasus-carousel, pegasus-slider, pegasus-wow, wp-bootstrap-hooks | unknown |

### Gaps to resolve

- **Unpinned host keys (deploys SKIP, 5 sites; status 2026-10-13 1:45 PM EDT):** gentwo (gtxm1263), qbroundtable, theshootout, top100proday, vineandvision. Keyscan got no answer from these hosts, even after Jim's IP was whitelisted (SiteGround began timing out again partway through the gentle scan), and Jim's known_hosts has no entry for them. Fix: `ssh -p 18765 user@host` once from Jim's machine, then `--refresh-fingerprints --known-hosts-only`.
- **pegasus-child site branches without the new workflow:** these branches don't exist on GitHub, so the 2026-10-13 rollout skipped them: advcompany_theme, avena_theme, chrishixson_theme, meowweretalkin_theme, qbroundtable_theme, theshootout_theme, top100proday_theme, visionquestdev_theme, vqgoods_theme.
- **Rollout 2026-10-13:** the workflow was pushed to 25 pegasus-child site branches.
  - cadence_group_theme, organizepluscleaning and righthandrenovations got the file but trigger nothing: those sites are disabled and not in the push allowlist.
  - Of 22 runs, hfhsga_theme succeeded because it skipped as unpinned. The other 21 FAILED with `host key fingerprint mismatch` (ed25519 pinned, RSA presented), so no server was touched.
  - Re-run after the RSA registry lands on pegasus-child master (pegasus-child#6). Fixes: pegasus#19, plus the 18 plugin PR branches.
- **No SSH details** (`enabled: false`): vqdev.com, quarterbackuniverse.com, qb-tv.com, righthandrenovations.com, organizepluscleaning.com, mamakayscheesecakes.com, networkingnorth.com, cadence-group.com. Fill in `ssh_user`, `ssh_host` and `remote_path` in `sync/sites.json` and regenerate.
- **pegasus-child branch named in the registry but not on GitHub:** these branches don't exist yet, so pushes have nothing to deploy. Create each branch from the live site's theme (as was done for `vineandvision_theme`) or correct the name.
  - visionquestdev_theme, avena_theme, meowweretalkin_theme, vqgoods_theme, chrishixson_theme
  - qbroundtable_theme, advcompany_theme, theshootout_theme, top100proday_theme
- **No pegasus-child branch at all:** vqdev.com, quarterbackuniverse.com, qb-tv.com, mamakayscheesecakes.com, networkingnorth.com.
- **Two sites on one branch:** `qbiqsystem_theme` maps to both `qbiqsystem` (live, own account) and `qbiqsystem-staging`, so a push deploys both. Disable or remove the live entry if qbiqsystem.com is not running this theme yet.
- **sagescnc / russellcontracting:** the old workflow listed `sagescnc_theme` and `russellcontracting_theme`, which don't exist on GitHub, so it never ran for these sites. The registry uses `sage_theme` and `russell_theme` (both confirmed by Jim).
- **renecatherinedesign:** Jim confirmed the domain and server folder are both `renecatherinedesigns.com` (`path_verified: true`).
- **Corrected mappings** (verified from the local VVV branch):
  - sagescnc → `sage_theme` (was `sagescnc_theme`)
  - russellcontracting → `russell_theme` (was `russellcontracting_theme`)
  - righthandrenovations → `righthandrenovations`
- **Unconfirmed root path:** ricecapital's registry path is `…/www/ricecapitalfund.com/public_html`.

## Staging sites

Sites staged in a subfolder of another SiteGround account have `environment: "staging"` and `parent_site`. They use the parent account's SSH user and host. `remote_path` is `<parent public_html>/<subfolder>` (not yet verified on the server: `path_verified: false`).

| Key | URL | Parent account | Path | Child branch |
|---|---|---|---|---|
| `qbiqsystem-staging` | qbiqsystem.com/test (lives at chrishixson.com/test) | `chrishixson` (u869-geq9wwrhqrna@gvam1007) | /home/u869-geq9wwrhqrna/www/chrishixson.com/public_html/test | qbiqsystem_theme |
| `hfhs-staging` | visionquestdev.com/hfhs | `vqdev` (u137-u0edzwblljc1@ssh.visionquestdev.com) | /home/u137-u0edzwblljc1/www/visionquestdev.com/public_html/hfhs | hfhsga_theme |

Staging sites are defined in `STAGING` in `sync/lib/build_registry.py`.

To **promote a staging site to live**:
1. Once the live SiteGround site exists, set the live entry's `ssh_user`, `ssh_host` and `remote_path` in `sync/sites.json`. Give it `environment: "live"` and the same `pegasus-child` branch.
2. Remove the staging key from `STAGING` in `sync/lib/build_registry.py`, or keep it if both should deploy.
3. Regenerate the registry, then PR `.github/deploy/sites.json` (and the regenerated workflows) into the repos.
4. On the live server, clone the theme and plugins (`sync/pegasus.sh setup`) and run checklist steps 1–4.

## SSH host key pinning (`ssh_fingerprint`)

Every enabled site in the registry carries `ssh_fingerprint`, the SHA256 fingerprint of the server's host key. It must match `^SHA256:[A-Za-z0-9+/]{43}=?$` and is passed to `appleboy/ssh-action` `fingerprint:`.
- drone-ssh 1.8.2 compares it to `ssh.FingerprintSHA256(hostkey)` and refuses to connect on a mismatch.
- A site with no valid fingerprint is **not connected to**: the plan job drops it with a `Skipped <site>: no pinned SSH host key fingerprint` notice.

**Pin the key type the Go client negotiates, not the one OpenSSH uses.** drone-ssh uses golang.org/x/crypto/ssh (v0.45), whose host-key preference is ECDSA, then RSA, then ed25519 last. SiteGround servers offer ed25519 and RSA, so the action sees the **RSA** key.
- The first rollout pinned ed25519, and every deploy on 2026-10-13 failed with `ssh: handshake failed: ssh: host key fingerprint mismatch`. Nothing connected, so nothing was deployed.
- The builder now scans and picks in Go order (ecdsa > rsa > ed25519).

Many sites share one SiteGround server (`gvamXXXX`/`gtxmXXXX.siteground.biz`) and so share a fingerprint.

Fingerprints live in `sync/sites.json` (`ssh_fingerprint` and `ssh_fingerprint_status`) and are copied into `deploy-registry.json`. `ssh_fingerprint_status` is one of:
- `pinned`: from ssh-keyscan, cross-checked against known_hosts.
- `pinned-known_hosts`: taken from Jim's `~/.ssh/known_hosts`.
- `missing`
- `mismatch`

The builder keeps the stored values unless you ask it to refresh.

**Refresh** (after SiteGround rotates host keys or moves a site; the symptom is a deploy FAIL with `host key fingerprint mismatch`):
1. Check the new key is genuine first: Site Tools, or SiteGround support. Then update known_hosts: `ssh-keygen -R '[host]:18765'`, then reconnect with `ssh -p 18765 user@host`. OpenSSH's UpdateHostKeys then records all of the server's keys, RSA included.
2. Run `sync/pegasus.sh registry --child-branches auto --refresh-fingerprints`.
   - This runs `ssh-keyscan -p <port> -t ecdsa|rsa|ed25519` (first type that answers, in Go order), computes SHA256 with `ssh-keygen -lf -`, and cross-checks `ssh-keygen -F '[host]:port'`. A **mismatch** is not pinned and is printed as a WARNING.
   - If keyscan fails, it falls back to known_hosts (same order).
   - Add `--known-hosts-only` to skip the network entirely. Use this when SiteGround's firewall is blocking you.
3. Vendor the new registry to pegasus-child's default branch (the registry the child workflow reads) and to pegasus and the plugin repos.

Don't hammer keyscan. On 2026-10-12, repeated scans got Jim's IP firewalled by SiteGround (connections timed out, even on 443), and it was still blocked on 2026-10-13 at 12:45 PM EDT.

## Public logs

Actions logs on these repos may be public, so the workflow prints as little as possible:
- The plan summary lists only `site (environment)`.
- The deploy job masks the site's host, user and path (`::add-mask::`) before the SSH step, so they show as `***` in the step header.
- The server script prints one line per site: `<site>: DEPLOYED <short sha>`, `<site>: SKIP <reason>` (not installed / not a git checkout / detached HEAD / wrong branch / master-main mismatch) or `<site>: FAIL <category>` (dirty working tree (N files) / git fetch error / git pull --ff-only error / git status error).
- Git's own output, file names, commit subjects and paths are never printed. Investigate failures over SSH.
- Connection-level errors from drone-ssh itself (e.g. a timeout) can still include the masked host.

## Moving to main (master → main rename)

Deploys work whether a repo's default branch is `master` or `main`, before, during and after a rename.

- **Workflows (pegasus + plugins):** trigger on `push` to `[master, main]` but deploy only when the pushed branch equals the repo's current default branch (`github.event.repository.default_branch`). A stale push to the old name deploys nothing.
- **pegasus-child:** reads `.github/deploy/sites.json` from its default branch (whatever it's called). Site branches (`*_theme`) are never renamed. `sync/pegasus.sh rollout-child` copies the workflow from the default branch.
- **Registry builder:** `sync/lib/build_registry.py` reads each repo's default branch from GitHub (`git ls-remote --symref`) and writes it into the registry, `sync/sites.json` and `repos.json`. Use `--offline` to keep the stored values. `setup-repos.sh` and `git-status.sh` follow `origin/HEAD` instead of assuming master.
- **Server copies:** the deploy never switches branches on a server. If a server copy is on `master` while the repo's default is `main` (or the other way round), the deploy SKIPs with `server on <cur>, default is <new>: run sync/migrate-default-branch-to-main.sh --servers or switch manually`. Other branch mismatches also SKIP.
- **Doing the rename:** `sync/migrate-default-branch-to-main.sh` (dry run by default; add `--apply` to change anything).
  1. `./migrate-default-branch-to-main.sh --apply`: renames on GitHub (`gh api -X POST repos/OWNER/REPO/branches/master/rename -f new_name=main`; GitHub retargets open PRs and redirects the old name), then switches local VVV copies.
  2. `./migrate-default-branch-to-main.sh --servers` (review), then `--servers --apply`: SSHes to every enabled site in `deploy-registry.json` that uses the repo and switches the server copy.
  3. Push to `main` (or run the workflow manually) to deploy.

  Local and server switches use the same safe steps and never `checkout -B` or `branch -D`: refuse if the copy is dirty; `git fetch origin main:refs/remotes/origin/main`; refuse if `git rev-list origin/main..master` is non-empty; `git checkout -b main --track origin/main` (refuse if a local `main` exists and differs); `git branch -d master` (a refusal is reported, the branch is left). Results: SWITCHED / OK / DIRTY / SKIP / PENDING / FAIL. Pass repo names to limit; `--local-only` skips the GitHub step. pegasus-child is skipped unless named.

## Adding a new site

1. Add an entry to `sync/sites.json`:
   - `name`, `domain`, `ssh_user`, `ssh_host`, `ssh_port` (18765), `remote_path` (…/public_html)
   - `themes.pegasus-child.branch`, `plugins`, and `environment`
   - Also add the domain to `DOMAINS` in `sync/lib/build_registry.py`.
2. Create the site's pegasus-child branch on GitHub, from master or from the site's existing theme.
3. Run `sync/pegasus.sh registry --child-branches auto` (see above). Then PR `sync/deploy-registry.json` as `.github/deploy/sites.json` into each repo (and pegasus-child's rendered workflow, `sync/deploy-workflow/out/pegasus-child.yml`, which now includes the new branch in its allowlist).
4. Push the workflow to the new branch: `sync/pegasus.sh rollout-child --push <branch>`.
5. Complete the server checklist.
