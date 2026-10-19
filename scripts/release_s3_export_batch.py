#!/usr/bin/env python3
"""Release dated snapshots from a multi-project tar via bounded S3 range reads.

The compressed export is never saved in full. A job can stop between projects
and resume from the committed export manifest in a later invocation.
"""
import hashlib, importlib.util, io, json, os, re, shutil, sys, tarfile, time
from pathlib import Path
import urllib.request
import release_s3_batch as batch

DATE='2026-07-12'


class RangedReader(io.RawIOBase):
    def __init__(self,item):
        self.url=item['url'];self.size=item['metadata']['bytes'];self.etag=item['metadata']['etag'];self.offset=0;self.buffer=b'';self.cursor=0;self.hash=hashlib.sha256();self.parts=[]
    def readable(self):return True
    def read(self,n=-1):
        if n<0:n=16384
        while len(self.buffer)-self.cursor<n and self.offset<self.size:
            end=min(self.size-1,self.offset+8*1024**2-1)
            for attempt in range(5):
                try:
                    request=urllib.request.Request(self.url,headers={'Range':f'bytes={self.offset}-{end}','If-Match':self.etag})
                    with urllib.request.urlopen(request,timeout=120) as response:
                        if response.status!=206:raise IOError('S3 did not honor byte range')
                        data=response.read()
                    if len(data)!=end-self.offset+1:raise IOError('Short S3 range')
                    break
                except Exception:
                    if attempt==4:raise
                    time.sleep(2)
            self.offset+=len(data);self.hash.update(data);self.parts.append(hashlib.md5(data).digest());self.buffer=self.buffer[self.cursor:]+data;self.cursor=0
        result=self.buffer[self.cursor:self.cursor+n];self.cursor+=len(result);return result


def main():
    if os.environ.get('GITHUB_ACTIONS')!='true':raise RuntimeError('This script runs only in a temporary GitHub Actions runner.')
    event=json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text());item=json.loads(event['inputs']['export_manifest']);key=item['key'];meta=item['metadata'];limit=int(item.get('max_projects',10))
    print('::add-mask::'+item['url'],flush=True)
    temporary=Path(os.environ['RUNNER_TEMP'])/'research-export';temporary.mkdir()
    askpass=temporary/'git-askpass.py';askpass.write_text('#!/usr/bin/env python3\nimport os,sys\nprint("x-access-token" if "username" in sys.argv[1].lower() else os.environ["GITHUB_TOKEN"])\n');askpass.chmod(0o700)
    os.environ.update(GIT_ASKPASS=str(askpass),GIT_TERMINAL_PROMPT='0',GIT_LFS_SKIP_SMUDGE='1')
    initial=temporary/'initial';batch.checkout(initial)
    state_path=initial/'export-release-status.json';state=json.loads(state_path.read_text()) if state_path.exists() else {'exports':{}}
    state.setdefault('exports',{});export=state['exports'].setdefault(key,{'projects':{},'status':'in_progress','source':meta});completed=export['projects'];shutil.rmtree(initial)
    reader=RangedReader(item);observed=set();current_project=None;output=None;raw=temporary/'project.tar.gz';members=[];uploaded=0;end_reached=True
    def release(project):
        nonlocal output,members,uploaded
        if output is None:return
        output.close();output=None
        repo=temporary/'repo';batch.checkout(repo)
        primary=repo/'paper-assets'/project/'08-index/asset-manifest.json'
        existing=primary.exists();collection=project+'--export-20260712' if existing else project
        primary_manifest=json.loads(primary.read_text()) if existing else None
        spec=importlib.util.spec_from_file_location('snapshot_rules',repo/'scripts/release_assets.py');rules=importlib.util.module_from_spec(spec);spec.loader.exec_module(rules)
        rules.EXTRA_SECRETS=[os.environ['GITHUB_TOKEN']]
        result=rules.collect(raw,repo,key,meta)
        folder=repo/'paper-assets'/(project+'--export-20260712');manifest=json.loads((folder/'08-index/asset-manifest.json').read_text())
        manifest['derived_archive_sha256']=manifest['source_s3'].pop('sha256');manifest['source_s3'].update(member_prefix=project+'/',sha256=None,derivation='Single-project archive derived while streaming the source export')
        manifest.update(snapshot_date=DATE,original_project=project)
        if not existing:
            target=repo/'paper-assets'/project;folder.rename(target);folder=target;manifest['project']=project
        else:manifest['title']=primary_manifest['title']+' (July export snapshot)'
        (folder/'08-index/asset-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        rules.write_csv(folder/'08-index/original-members.csv',['s3_archive','original_member','derived_member','source_bytes','processing'],members)
        rules.write_project_readme(folder,manifest)
        guide=folder/'README.md';guide.write_text(guide.read_text()+f'\nThis dated snapshot came from `{key}`. Only one project was retained temporarily. [Original archive members](08-index/original-members.csv) map each source path to its derived copy. The derived archive SHA-256 is `{manifest["derived_archive_sha256"]}`; the source archive ETag is `{meta["etag"]}`.\n')
        batch.run([sys.executable,'scripts/build_trace_browser.py','--project',collection],repo)
        if existing:
            destination=repo/'research-snapshots'/project/DATE;destination.parent.mkdir(parents=True,exist_ok=True);folder.rename(destination);folder=destination
            path=folder/'README.md';path.write_text(path.read_text().replace('../../traces/','../../../traces/'))
            for name in ['README.md','index.html']:
                path=folder/'05-generation-trace'/name;path.write_text(path.read_text().replace('../../../traces/','../../../../traces/'))
            path=repo/'traces/projects.json';index=json.loads(path.read_text())
            for entry in index['projects']:
                if entry['project']==collection:entry['catalog']=f'../research-snapshots/{project}/{DATE}/05-generation-trace/catalog.json'
            path.write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
        for selected in [collection]:batch.run([sys.executable,'scripts/validate_trace_release.py','--project',selected],repo)
        batch.verify_files(repo,[collection]);batch.run([sys.executable,'scripts/update_release_catalogue.py'],repo)
        record={'status':'uploaded','project':project,'collection':collection,'snapshot':existing,'derived_archive_sha256':manifest['derived_archive_sha256'],'indexed_members':len(members),'paper_pdf':manifest['paper_pdf'],'code_count':manifest['code_count'],'trace_count':manifest['trace_count']}
        completed[project]=record
        (repo/'export-release-status.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
        batch.run(['git','diff','--check','--','scripts','README.md','CONTENTS.md','RELEASE_NOTES.md','paper-assets/index.html','paper-assets/asset-matrix.csv','traces'],repo)
        head=batch.commit_and_push(repo,'Release dated export and readable conversations for '+project)
        shutil.rmtree(repo);raw.unlink();members=[];uploaded+=1
        batch.log(stage='export-project-uploaded-and-cleaned',project=project,commit=head,uploaded_in_job=uploaded,completed_projects=len(completed))
    with tarfile.open(fileobj=reader,mode='r|gz') as handle:
        for member in handle:
            parts=Path(member.name).parts
            if len(parts)<2 or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*',parts[0]):continue
            project=parts[0];rel='/'.join(parts[1:])
            if current_project!=project:
                if current_project:release(current_project)
                if uploaded>=limit:end_reached=False;break
                if project in observed:raise ValueError('Non-contiguous project members in source export: '+project)
                observed.add(project);current_project=project
                if completed.get(project,{}).get('status')=='uploaded':continue
                output=tarfile.open(str(raw),'w|gz',compresslevel=1)
                batch.log(stage='stream-export-project',project=project,compressed_bytes_read=reader.offset,source_bytes=reader.size)
            if completed.get(project,{}).get('status')=='uploaded':continue
            row=dict(s3_archive=key,original_member=member.name,derived_member='',source_bytes=member.size,processing='')
            if not member.isfile():
                if not member.isdir():row['processing']='Non-regular entry omitted';members.append(row)
                continue
            if any(p in {'.git','.venv','venv','node_modules','__pycache__','.cache','.ssh','.aws','.claude','.codex'} for p in parts) or Path(rel).name.lower() in {'.env','credentials','credentials.json','auth.json','accounts.json'}:
                row['processing']='Dependency, cache, account file, or Git internals omitted';members.append(row);continue
            if rel.startswith('trajectories/'):rel='logs/chats/exported-trajectories/'+rel.removeprefix('trajectories/')
            else:
                for prefix in ('project/','workspace/','source/'):
                    if rel.startswith(prefix):rel=rel.removeprefix(prefix)
                components=Path(rel).parts
                if 'projects' in components and project in components:
                    i=components.index(project);rel='/'.join(components[i+1:])
            if not rel:continue
            canonical=f'workspace/projects/{project}--export-20260712/{rel}'
            info=tarfile.TarInfo(canonical);info.size=member.size;info.mtime=member.mtime
            with handle.extractfile(member) as source:output.addfile(info,source)
            row.update(derived_member=canonical,processing='Preserved in per-project archive; sanitized before release');members.append(row)
    if end_reached and current_project:release(current_project)
    if end_reached:
        while reader.offset<reader.size:reader.read(8*1024**2)
        actual=hashlib.md5(b''.join(reader.parts)).hexdigest()+'-'+str(len(reader.parts))
        if '-' in meta['etag']:assert actual==meta['etag'].strip('"'),'Source multipart ETag mismatch'
        export.update(status='uploaded',source_sha256=reader.hash.hexdigest())
        repo=temporary/'final-index';batch.checkout(repo)
        (repo/'export-release-status.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
        batch.commit_and_push(repo,'Record complete streamed export checksum');shutil.rmtree(repo)
    askpass.unlink();temporary.rmdir()
    with open(os.environ['GITHUB_STEP_SUMMARY'],'a') as out:out.write(f'# Streamed project export\n\n{uploaded} projects uploaded in this job; {len(completed)} total. Source archive complete: {end_reached}. Temporary project files were removed after upload.\n')
    batch.log(stage='export-job-complete',uploaded=uploaded,total_completed=len(completed),source_complete=end_reached)


if __name__=='__main__':
    try:main()
    except Exception as error:
        print('::error::'+type(error).__name__+': '+re.sub(r'https?://\S+','[URL]',str(error)),flush=True);sys.exit(1)
