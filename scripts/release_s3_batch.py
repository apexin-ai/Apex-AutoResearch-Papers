#!/usr/bin/env python3
"""Sequential asset release in a temporary GitHub Actions runner.

Only object-scoped expiring URLs are accepted. No AWS credentials are needed.
Every project's temporary archive and checkout are deleted after its final push.
"""
import concurrent.futures
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
REPOSITORY='Zxy-MLlab/Release_examples'
REMOTE=f'https://github.com/{REPOSITORY}.git'
PATTERNS='/*\n!/paper-assets/\n/paper-assets/index.html\n/paper-assets/asset-matrix.csv\n/paper-assets/*/README.md\n/paper-assets/*/08-index/\n/paper-assets/*/05-generation-trace/example-session.json\n!/research-snapshots/\n/research-snapshots/*/*/08-index/\n/research-snapshots/*/*/05-generation-trace/example-session.json\n'


def log(**value):print(json.dumps(value,ensure_ascii=False),flush=True)

def run(args,repo=None,timeout=3600,quiet=False):
    result=subprocess.run(args,cwd=repo,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=timeout)
    if result.returncode:raise RuntimeError(f'{args[0]} failed ({result.returncode}): '+result.stdout[-5000:])
    if result.stdout and not quiet:print(result.stdout[-8000:],flush=True)
    return result.stdout.rstrip('\n')

def checkout(path):
    run(['git','clone','--filter=blob:none','--depth=1','--no-checkout',REMOTE,str(path)])
    run(['git','sparse-checkout','init','--no-cone'],path)
    (path/'.git/info/sparse-checkout').write_text(PATTERNS)
    run(['git','checkout','main'],path)
    for name,value in [('user.name','github-actions[bot]'),('user.email','41898282+github-actions[bot]@users.noreply.github.com'),('gc.auto','0'),('maintenance.auto','false'),('core.compression','3')]:run(['git','config',name,value],path)


def download(item,target):
    url=item['url'];size=item['metadata']['bytes'];etag=item['metadata']['etag']
    chunk=32*1024**2
    fd=os.open(target,os.O_CREAT|os.O_RDWR,0o600);os.ftruncate(fd,size)
    def part(start):
        end=min(size-1,start+chunk-1)
        for attempt in range(5):
            try:
                request=urllib.request.Request(url,headers={'Range':f'bytes={start}-{end}','If-Match':etag})
                with urllib.request.urlopen(request,timeout=120) as response:
                    if response.status!=206:raise IOError('S3 did not honor byte range')
                    position=start
                    while True:
                        data=response.read(1024**2)
                        if not data:break
                        os.pwrite(fd,data,position);position+=len(data)
                    if position!=end+1:raise IOError('Incomplete S3 range')
                return
            except Exception:
                if attempt==4:raise
                time.sleep(2)
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:list(executor.map(part,range(0,size,chunk)))
    finally:os.close(fd)
    expected=etag.strip('"')
    with target.open('rb') as handle:
        hashes=[hashlib.md5(data).digest() for data in iter(lambda:handle.read(8*1024**2),b'')]
    if '-' in expected:
        actual=hashlib.md5(b''.join(hashes)).hexdigest()+'-'+str(len(hashes))
    else:
        checksum=hashlib.md5()
        with target.open('rb') as handle:
            for data in iter(lambda:handle.read(8*1024**2),b''):checksum.update(data)
        actual=checksum.hexdigest()
    if actual!=expected:raise IOError('Source ETag checksum mismatch')
    log(stage='download-verified',key=item['key'],bytes=size)


def verify_files(repo,projects):
    sys.path.insert(0,str(repo/'scripts'))
    import validate_trace_release as validator
    credential=re.compile('|'.join('(?:'+p.pattern+')' for p in validator.SECRET_PATTERNS.values()))
    index={p['project']:p for p in json.loads((repo/'traces/projects.json').read_text())['projects']}
    total=0
    for project in projects:
        folder=(repo/'traces'/index[project]['catalog']).resolve().parent.parent
        for path in folder.rglob('*'):
            if not path.is_file():continue
            total+=path.stat().st_size
            if path.stat().st_size>=100_000_000:raise RuntimeError('File exceeds GitHub limit: '+str(path.relative_to(repo)))
            if path.suffix.lower() in {'.md','.json','.csv','.py','.sh','.yaml','.yml','.tex','.bib','.txt','.html','.log','.jsonl','.toml','.ini','.cfg','.js','.ts','.rst'}:
                if credential.search(path.read_text(encoding='utf-8',errors='replace')):raise RuntimeError('Credential pattern in '+str(path.relative_to(repo)))
    log(stage='release-file-checks-passed',projects=projects,bytes=total)


def push(repo):
    for attempt in range(4):
        try:
            run(['git','-c','pack.threads=2','-c','pack.compression=3','push','origin','main'],repo,timeout=1800)
            head=run(['git','rev-parse','HEAD'],repo,quiet=True)
            remote=run(['git','ls-remote','origin','refs/heads/main'],repo,quiet=True).split()[0]
            if head!=remote:raise RuntimeError('Remote commit does not match local commit')
            return head
        except Exception:
            if attempt==3:raise
            time.sleep(5)


def commit_and_push(repo,title):
    run(['git','add','--sparse','-A'],repo)
    names=[p for p in run(['git','diff','--cached','--name-only','-z'],repo,quiet=True).split('\0') if p]
    if not names:return run(['git','rev-parse','HEAD'],repo,quiet=True)
    body=[];reserved=[]
    for name in names:
        if name.startswith(('scripts/','traces/')) or '/' not in name or '/08-index/' in name or name.endswith(('/README.md','/catalog.json','/index.html')) or name in {'paper-assets/index.html','paper-assets/asset-matrix.csv'}:reserved.append(name)
        else:body.append(name)
    groups=[];group=[];size=0
    for name in body:
        file=repo/name;addition=file.stat().st_size if file.is_file() else 0
        if group and size+addition>600*1024**2:groups.append(group);group=[];size=0
        group.append(name);size+=addition
    if group:groups.append(group)
    if len(groups)>1:
        for i,paths in enumerate(groups,1):
            (repo/'.git/release-paths').write_bytes(b''.join((':(literal)'+p).encode()+b'\0' for p in paths))
            run(['git','commit','--only','--pathspec-from-file=.git/release-paths','--pathspec-file-nul','-qm',title+f' (assets {i}/{len(groups)})'],repo)
            head=push(repo);log(stage='asset-part-uploaded',part=i,total=len(groups),commit=head)
    if run(['git','diff','--cached','--name-only'],repo,quiet=True):
        run(['git','commit','-qm',title],repo);return push(repo)
    return run(['git','rev-parse','HEAD'],repo,quiet=True)


def main():
    if os.environ.get('GITHUB_ACTIONS')!='true':raise RuntimeError('Run this script in GitHub Actions; it uses the runner temporary directory.')
    manifest=json.loads(os.environ.pop('ARCHIVE_MANIFEST'))
    for item in manifest:print('::add-mask::'+item['url'],flush=True)
    token=os.environ['GITHUB_TOKEN']
    temporary=Path(os.environ['RUNNER_TEMP'])/'research-release';temporary.mkdir(exist_ok=True)
    askpass=temporary/'git-askpass.py';askpass.write_text('#!/usr/bin/env python3\nimport os,sys\nprint("x-access-token" if "username" in sys.argv[1].lower() else os.environ["GITHUB_TOKEN"])\n');askpass.chmod(0o700)
    os.environ.update(GIT_ASKPASS=str(askpass),GIT_TERMINAL_PROMPT='0',GIT_LFS_SKIP_SMUDGE='1')
    reports=[]
    for number,item in enumerate(manifest,1):
        key=item['key'];slug=key.split('/')[0];meta=item['metadata']
        log(stage='begin',index=number,total=len(manifest),key=key,free_GiB=round(shutil.disk_usage(temporary).free/1024**3,1))
        current=temporary/'current';current.mkdir();repo=current/'repo';checkout(repo)
        previous=repo/'paper-assets'/slug/'08-index/asset-manifest.json'
        if previous.exists():
            old=json.loads(previous.read_text());source=old.get('source_s3',{})
            if source.get('etag')==meta['etag'] and source.get('key')==key and source.get('sha256'):
                log(stage='skip-verified-release',key=key);shutil.rmtree(current);continue
        archive=current/'workspace.tar.gz';download(item,archive)
        (current/'metadata.json').write_text(json.dumps(meta))
        run([sys.executable,'scripts/release_assets.py',str(archive),'--repo',str(repo),'--source-key',key,'--source-metadata-json',str(current/'metadata.json'),'--result-json',str(current/'result.json')],repo)
        result=json.loads((current/'result.json').read_text());projects=[p['project'] for p in result['projects']]
        if not projects:raise RuntimeError('No project assets found in '+key)
        for project in projects:run(['git','rm','-qr','--cached','--sparse','--ignore-unmatch','paper-assets/'+project],repo)
        args=[sys.executable,'scripts/build_trace_browser.py']
        for project in projects:args+=['--project',project]
        run(args,repo)
        for project in projects:run([sys.executable,'scripts/validate_trace_release.py','--project',project],repo)
        verify_files(repo,projects)
        run([sys.executable,'scripts/update_release_catalogue.py'],repo)
        status_path=repo/'batch-release-status.json';status=json.loads(status_path.read_text()) if status_path.exists() else {'archives':{}}
        record={'status':'uploaded','source':meta,'archive_sha256':result['archive_sha256'],'projects':projects,'counts':[{k:p[k] for k in ['project','title','paper_pdf','code_count','data_count','trace_count']} for p in result['projects']],'workflow_run':f'https://github.com/{REPOSITORY}/actions/runs/'+os.environ['GITHUB_RUN_ID']}
        status['archives'][key]=record;status_path.write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
        run(['git','diff','--check','--','scripts','README.md','CONTENTS.md','RELEASE_NOTES.md','paper-assets/index.html','paper-assets/asset-matrix.csv','traces'],repo)
        head=commit_and_push(repo,'Release research assets and readable traces for '+slug)
        reports.append({**record,'commit':head});shutil.rmtree(current)
        log(stage='uploaded-and-cleaned',key=key,projects=projects,commit=head)
    askpass.unlink();temporary.rmdir()
    with open(os.environ['GITHUB_STEP_SUMMARY'],'a') as out:
        out.write('# Sequential research asset release\n\n'+str(len(reports))+' archives processed and uploaded. Temporary project archives and checkouts were removed after successful uploads.\n')
    log(stage='complete',uploaded_archives=len(reports))


if __name__=='__main__':
    try:main()
    except Exception as error:
        message=re.sub(r'https?://\S+','[URL]',str(error))
        print('::error::'+type(error).__name__+': '+message,flush=True)
        sys.exit(1)
