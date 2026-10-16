import json,subprocess as sp,os,glob,collections,datetime
from concurrent.futures import ThreadPoolExecutor
B='/home/jim/Projects/vagrant-local';F=B+'/repo-status-pegasus-2026-10-12.json'
old=json.load(open(F))
rows={(r['site'],r['path']):r for r in old['rows']}
for p in glob.glob(B+'/www/*/public_html/wp-content/*/*'):
    n=os.path.basename(p)
    if not os.path.isdir(p): continue
    if not (n.startswith('pegasus') or n in('wp-bootstrap-hooks','vqdev-toast')): continue
    site=p.split('/www/')[1].split('/')[0]; rel=p.split('/public_html/')[1]
    rows.setdefault((site,rel),{'site':site,'component':n,'path':rel,'remote':'','branch':'','default':'','on_default':'','ahead':'','behind':'','dirty':'','branch_gone':'','status':'','_new':1})
def g(p,*a):
    r=sp.run(['git','-C',p,*a],capture_output=True,text=True);return r.returncode,r.stdout.strip()
dcache={}
def scan(r):
    p=f"{B}/www/{r['site']}/public_html/{r['path']}"
    for k in('commit','commit_date','remote_head'): r[k]=''
    if not os.path.exists(p+'/.git'):
        r.update(status='Not a git repo',branch='',on_default='',ahead='',behind='',dirty='');return r
    g(p,'fetch','-q','--prune','origin')
    r['remote']=g(p,'remote','get-url','origin')[1]
    br=g(p,'rev-parse','--abbrev-ref','HEAD')[1]; r['branch']=br
    rc,dh=g(p,'ls-remote','--symref','origin','HEAD')
    if 'refs/heads/' in dh: r['default']=dh.split('refs/heads/')[1].split()[0]
    r['commit']=g(p,'rev-parse','--short','HEAD')[1]; r['commit_date']=g(p,'log','-1','--format=%ci')[1]
    # Upstream: use branch.<b>.merge config, not @{u}. Single-branch clones (fetch refspec
    # only maps master) make @{u} fail even though the branch exists on origin, so fetch the
    # tracked branch explicitly into refs/remotes/origin/<name> before comparing.
    rc,merge=g(p,'config',f'branch.{br}.merge')
    rbr=merge.replace('refs/heads/','') if rc==0 and merge else br
    rc,_=g(p,'fetch','-q','origin',f'+refs/heads/{rbr}:refs/remotes/origin/{rbr}')
    up='origin/'+rbr
    r['upstream']=up if rc==0 else ''
    rc2,ab=g(p,'rev-list','--left-right','--count',f'HEAD...{up}') if rc==0 else (1,'')
    gone = rc2!=0
    r['contained_in']=''
    if gone:
        _,cont=g(p,'branch','-r','--contains','HEAD')
        r['contained_in']=','.join(x.strip() for x in cont.splitlines() if '->' not in x)
    a,b=ab.split() if not gone else ('?','?')
    r['ahead'],r['behind']=a,b; r['branch_gone']='yes' if gone else ''
    r['remote_head']=g(p,'rev-parse','--short',up)[1] if not gone else ''
    r['dirty']=str(len(g(p,'status','--porcelain','--untracked-files=no')[1].splitlines()))
    r['on_default']='yes' if br==r['default'] else 'no'
    if br=='HEAD': s='Detached HEAD'
    elif r['on_default']=='no' and r['component']=='pegasus-child':
        if gone:
            ci=[x for x in r['contained_in'].split(',') if x]
            s='Site branch: not on origin'+(f" (HEAD is in {ci[0]})" if len(ci)==1 else f" (HEAD is a shared commit in {len(ci)} origin branches)" if ci else '')
        elif b!='0': s='Site branch: needs pull'
        elif a!='0': s='Site branch: unpushed commits'
        elif r['dirty']!='0': s='Site branch: uncommitted changes'
        else: s='Site branch: up to date'
    elif r['on_default']=='no': s='Off default branch'
    elif gone: s='Branch not on origin'
    elif b!='0': s=f'Needs pull'
    elif a!='0': s='Unpushed commits'
    elif r['dirty']!='0': s='Uncommitted changes'
    else: s='Up to date'
    r['status']=s; return r
with ThreadPoolExecutor(8) as ex: out=list(ex.map(scan,rows.values()))
out.sort(key=lambda r:(r['site'],r['path']))
new=[f"{r['site']}/{r['component']}" for r in out if r.pop('_new',0)]
d={'scan_date':datetime.datetime.now().astimezone().isoformat(timespec='seconds'),'counts':dict(collections.Counter(r['status'] for r in out)),'rows':out}
json.dump(d,open(F,'w'),indent=1)
import csv
cols=['site','component','path','remote','branch','upstream','default','on_default','commit','commit_date','remote_head','ahead','behind','dirty','branch_gone','status']
w=csv.DictWriter(open(B+'/REPO-STATUS-2026-10-12.csv','w',newline=''),fieldnames=cols,extrasaction='ignore');w.writeheader();w.writerows(out)
print(d['scan_date'],len(out),d['counts'],'new:',new)
