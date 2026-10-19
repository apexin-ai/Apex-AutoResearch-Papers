#!/usr/bin/env python3
"""Collect one S3 supplementary collection via the local in-memory credential broker.

No project code is executed. Files are sanitized before entering the release tree.
"""
import concurrent.futures
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace

EXTRA_SECRETS=[]

def collect(archive, repo, key, metadata):
    broker=sys.modules['__main__']
    s3=broker.s3
    prefix=key.rstrip('/')+'/'
    directory=repo/'supplementary'/key.strip('/');directory.mkdir(parents=True,exist_ok=True)
    spec=importlib.util.spec_from_file_location('rules',repo/'scripts/release_assets.py');rules=importlib.util.module_from_spec(spec);spec.loader.exec_module(rules)
    rules.ROOT=repo;rules.EXTRA_SECRETS=EXTRA_SECRETS
    rows=[];included=[];objects=metadata['objects']
    def process(item):
        rel=item['key'].removeprefix(prefix)
        reason=''
        if not rel or rel.endswith('/'):reason='Directory marker'
        elif rules.excluded(rel) or Path(rel).suffix.lower() in {'.pyc','.pyo'}:reason='Dependency, cache, or Git internals'
        elif Path(rel).name.lower() in rules.EXCLUDE_NAMES:reason='Credential/account file'
        elif rel.endswith(('.jsonl.lock','.json.lock','.log.lock')):reason='Runtime file lock'
        row=dict(s3_key=item['key'],source_bytes=item['bytes'],etag=item['etag'],source_modified=item.get('modified',''),output_path='',output_bytes=0,sha256='',status=reason)
        if reason:return row
        destination=directory/'source'/rules.safe_rel(rel)
        with tempfile.NamedTemporaryFile() as tmp:
            s3.download_file(rules.BUCKET if hasattr(rules,'BUCKET') else 'agent-ml-research-project-backups-20260531',item['key'],tmp.name)
            class Reader:
                def extractfile(self,member):return open(tmp.name,'rb')
            member=SimpleNamespace(name=rel,size=item['bytes'],mtime=0)
            size,details=rules.sanitize_member(Reader(),member,destination)
        output=str(destination.relative_to(directory))
        if details.get('storage')=='sanitized-archive-contents':output+='.contents'
        row.update(output_path=output,output_bytes=size,sha256=details['sha256'],status=details.get('storage') or ('Split parts' if details.get('split') else 'Sanitized copy'))
        return row
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        for i,row in enumerate(executor.map(process,objects),1):
            rows.append(row)
            if row['output_path']:included.append(row)
            if i%250==0:print(json.dumps({'supplementary':key,'processed_objects':i,'total_objects':len(objects)}),flush=True)
    rules.write_csv(directory/'source-manifest.csv',['s3_key','source_bytes','etag','source_modified','output_path','output_bytes','sha256','status'],rows)
    manifest={'collection':key,'s3_prefix':prefix,'source_objects':len(objects),'included_files':len(included),'excluded_files':len(objects)-len(included),'sanitized_bytes':sum(r['output_bytes'] for r in included)}
    (directory/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    title=metadata.get('title',key.replace('-',' ').title())
    (directory/'README.md').write_text(f'# {title}\n\n'+metadata.get('description','Supplementary research files from the project backup.')+f'\n\nIncluded: **{len(included):,} source objects**. [Browse files](source/) · [Source and exclusion manifest](source-manifest.csv).\n\nThese are archived code, experiment records, or revision materials. They are not automatically counted as separate generated papers. English guides accompany original-language evidence. Credential fields are redacted; dependency caches, Git internals, and account files are excluded. Nested archives are exposed as sanitized extracted files rather than unchecked binary bundles.\n')
    return manifest
