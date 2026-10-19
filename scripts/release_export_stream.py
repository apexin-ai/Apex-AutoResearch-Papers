#!/usr/bin/env python3
"""Stream a multi-project S3 tar archive; release and remove each project in turn.

Invoked by the local credential broker. Compressed input stays in a bounded
memory buffer. Only the current project's derived archive and Git checkout are
written locally. Existing projects receive a separately labelled dated snapshot.
"""
import csv, hashlib, importlib.util, io, json, re, shutil, sys, tarfile
from pathlib import Path

EXTRA_SECRETS=[]
DATE='2026-07-12'


def collect(archive, repo, key, metadata):
    import run_batch as batch
    s3=sys.modules['__main__'].s3
    size=metadata['bytes'];project_reports=[];members=[];current_project=None;output=None;raw=None
    state=json.loads(batch.STATE.read_text());state.setdefault('exports',{})
    completed=state['exports'].setdefault(key,{}).setdefault('projects',{})
    temporary=batch.BASE/'current-export'
    if temporary.exists():shutil.rmtree(temporary)
    temporary.mkdir()
    class Reader(io.RawIOBase):
        def __init__(self):self.offset=0;self.buffer=b'';self.hash=hashlib.sha256();self.part_hashes=[]
        def readable(self):return True
        def read(self,n=-1):
            if n<0:n=16384
            while len(self.buffer)<n and self.offset<size:
                end=min(size-1,self.offset+8*1024**2-1)
                for attempt in range(5):
                    try:
                        body=s3.get_object(Bucket='agent-ml-research-project-backups-20260531',Key=key,Range=f'bytes={self.offset}-{end}')['Body']
                        data=body.read();body.close()
                        if len(data)!=end-self.offset+1:raise IOError('Short S3 range read')
                        break
                    except Exception:
                        if attempt==4:raise
                self.offset+=len(data);self.hash.update(data);self.part_hashes.append(hashlib.md5(data).digest());self.buffer+=data
            result=self.buffer[:n];self.buffer=self.buffer[n:];return result
    reader=Reader()
    def release(project):
        nonlocal output,raw,members
        if output is None:return
        output.close();output=None
        checkout=temporary/'repo';batch.checkout(checkout)
        for source in (batch.LOCAL/'Release_examples/scripts').glob('*.py'):shutil.copyfile(source,checkout/'scripts'/source.name)
        existing=(checkout/'paper-assets'/project/'08-index/asset-manifest.json').exists()
        collection=project+'--export-20260712' if existing else project
        # The stream uses an internal staging slug so later exports cannot replace
        # the previously released project snapshot.
        spec=importlib.util.spec_from_file_location('release_rules',checkout/'scripts/release_assets.py');rules=importlib.util.module_from_spec(spec);spec.loader.exec_module(rules)
        rules.EXTRA_SECRETS=EXTRA_SECRETS
        result=rules.collect(raw,checkout,key,metadata)
        folder=checkout/'paper-assets'/(project+'--export-20260712')
        manifest_path=folder/'08-index/asset-manifest.json';manifest=json.loads(manifest_path.read_text())
        manifest['derived_archive_sha256']=manifest['source_s3'].pop('sha256');manifest['source_s3'].update(member_prefix=project+'/',sha256=None,derivation='A single-project tar stream derived from the S3 export; see original-members.csv')
        manifest.update(snapshot_date=DATE,original_project=project)
        if not existing:
            new=checkout/'paper-assets'/project;folder.rename(new);folder=new;manifest['project']=project
        else:manifest['title']=manifest['title']+' (July export snapshot)'
        manifest_path=folder/'08-index/asset-manifest.json';manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        rules.write_csv(folder/'08-index/original-members.csv',['s3_archive','original_member','derived_member','source_bytes','processing'],members)
        rules.write_project_readme(folder,manifest)
        guide=folder/'README.md';guide.write_text(guide.read_text()+f'\nThis is a dated project export from `{key}`, collected without downloading the complete export archive. The SHA-256 of the derived single-project archive is `{manifest["derived_archive_sha256"]}`. Original tar paths are mapped in [original-members.csv](08-index/original-members.csv).\n')
        batch.run([batch.PYTHON,'scripts/build_trace_browser.py','--project',collection],checkout,timeout=3600)
        if existing:
            target=checkout/'research-snapshots'/project/DATE;target.parent.mkdir(parents=True,exist_ok=True);folder.rename(target)
            guide=target/'README.md';guide.write_text(guide.read_text().replace('../../traces/','../../../traces/'))
            for name in ['README.md','index.html']:
                path=target/'05-generation-trace'/name;path.write_text(path.read_text().replace('../../../traces/','../../../../traces/'))
            index=checkout/'traces/projects.json';content=json.loads(index.read_text())
            for entry in content['projects']:
                if entry['project']==collection:entry['catalog']=f'../research-snapshots/{project}/{DATE}/05-generation-trace/catalog.json'
            index.write_text(json.dumps(content,ensure_ascii=False,indent=2)+'\n')
        head=batch.publish(checkout,[collection],f'Release dated export and readable conversations for {project}')
        report={'status':'uploaded','project':project,'collection':collection,'commit':head,'snapshot':existing,'derived_archive_sha256':manifest['derived_archive_sha256'],'files':len(members)}
        completed[project]=report;batch.save(state);project_reports.append(report)
        shutil.rmtree(checkout);raw.unlink();members=[]
        batch.log(stage='export-project-cleaned',project=project,commit=head,completed_export_projects=len(completed))
    with tarfile.open(fileobj=reader,mode='r|gz') as handle:
        for member in handle:
            parts=Path(member.name).parts
            if len(parts)<2 or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*',parts[0]):continue
            project=parts[0];rel='/'.join(parts[1:])
            if current_project!=project:
                if current_project:release(current_project)
                current_project=project
                if completed.get(project,{}).get('status')=='uploaded':continue
                raw=temporary/'project.tar.gz';output=tarfile.open(raw,'w|gz',compresslevel=1)
                batch.log(stage='stream-export-project',project=project,compressed_bytes_read=reader.offset,total_bytes=size)
            if completed.get(project,{}).get('status')=='uploaded':continue
            row={'s3_archive':key,'original_member':member.name,'derived_member':'','source_bytes':member.size,'processing':''}
            if not member.isfile():
                if not member.isdir():row['processing']='Non-regular entry omitted';members.append(row)
                continue
            if any(part in {'.git','.venv','venv','node_modules','__pycache__','.cache','.ssh','.aws','.claude','.codex'} for part in parts) or Path(rel).name.lower() in {'.env','credentials','credentials.json','auth.json','accounts.json'}:
                row['processing']='Dependency, cache, runtime account file, or Git internals omitted';members.append(row);continue
            if rel.startswith('trajectories/'):
                rel='logs/chats/exported-trajectories/'+rel.removeprefix('trajectories/')
            else:
                for prefix in ('project/','workspace/','source/'):
                    if rel.startswith(prefix):rel=rel.removeprefix(prefix)
                split=Path(rel).parts
                if 'projects' in split and project in split:
                    offset=split.index(project);rel='/'.join(split[offset+1:])
            canonical=f'workspace/projects/{project}--export-20260712/{rel}'
            info=tarfile.TarInfo(canonical);info.size=member.size;info.mtime=member.mtime
            with handle.extractfile(member) as src:output.addfile(info,src)
            row.update(derived_member=canonical,processing='Preserved in derived per-project archive; sanitized for release');members.append(row)
    if current_project:release(current_project)
    # Finish reading the bounded compressed buffer to compute the complete source hash.
    while reader.offset<size:reader.read(8*1024**2)
    source_sha=reader.hash.hexdigest();etag=hashlib.md5(b''.join(reader.part_hashes)).hexdigest()+'-'+str(len(reader.part_hashes))
    expected=metadata['etag'].strip('"')
    if '-' in expected:assert etag==expected,'Export multipart ETag mismatch'
    state['exports'][key].update(status='uploaded',source_sha256=source_sha,source_etag=expected,projects=completed);batch.save(state)
    shutil.rmtree(temporary)
    return {'source_sha256':source_sha,'projects':project_reports,'all_completed_projects':len(completed)}
