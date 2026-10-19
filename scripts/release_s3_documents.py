#!/usr/bin/env python3
"""Release the small manuscript-only export archives in a temporary runner."""
import importlib.util,json,os,re,shutil,sys
from pathlib import Path
import release_s3_batch as batch


def main():
    if os.environ.get('GITHUB_ACTIONS')!='true':raise RuntimeError('Run in GitHub Actions temporary storage.')
    event=json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text());items=json.loads(event['inputs']['document_manifest'])
    for item in items:print('::add-mask::'+item['url'],flush=True)
    temporary=Path(os.environ['RUNNER_TEMP'])/'paper-export-release';temporary.mkdir()
    askpass=temporary/'git-askpass.py';askpass.write_text('#!/usr/bin/env python3\nimport os,sys\nprint("x-access-token" if "username" in sys.argv[1].lower() else os.environ["GITHUB_TOKEN"])\n');askpass.chmod(0o700)
    os.environ.update(GIT_ASKPASS=str(askpass),GIT_TERMINAL_PROMPT='0',GIT_LFS_SKIP_SMUDGE='1')
    for item in items:
        current=temporary/'current';current.mkdir();repo=current/'repo';batch.checkout(repo)
        folder=repo/'supplementary/paper-exports-20260712';folder.mkdir(parents=True,exist_ok=True)
        state=folder/'manifest.json';manifest=json.loads(state.read_text()) if state.exists() else {'collection':'paper-exports-20260712','archives':{},'pdfs':[]}
        key=item['key']
        if manifest['archives'].get(key,{}).get('etag')==item['metadata']['etag']:shutil.rmtree(current);continue
        raw=current/'source.archive';batch.download(item,raw)
        spec=importlib.util.spec_from_file_location('doc_rules',repo/'scripts/release_assets.py');rules=importlib.util.module_from_spec(spec);spec.loader.exec_module(rules);rules.ROOT=repo;rules.EXTRA_SECRETS=[os.environ['GITHUB_TOKEN']]
        target=folder/'source'/Path(key).name;size,details=rules.sanitize_nested(raw,target);extracted=target.with_name(target.name+'.contents')
        from pypdf import PdfReader
        for path in sorted(extracted.rglob('*.pdf')):
            sha=rules.digest(path);title,pages,marker=rules.paper_metadata(path,path.stem)
            same=next((p for p in manifest['pdfs'] if p['sha256']==sha),None)
            manifest['pdfs'].append({'archive':key,'path':str(path.relative_to(folder)),'title':title,'pages':pages,'sha256':sha,'bytes':path.stat().st_size,'duplicate_of':same['path'] if same else None})
        manifest['archives'][key]={'status':'uploaded',**item['metadata'],'sha256':rules.digest(raw)}
        manifest.update(source_objects=len(manifest['archives']),included_files=len(manifest['pdfs']),excluded_files=0,sanitized_bytes=sum(p['bytes'] for p in manifest['pdfs']))
        state.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        rules.write_csv(folder/'source-manifest.csv',['archive','path','title','pages','sha256','bytes','duplicate_of'],manifest['pdfs'])
        lines=['# Manuscript export collections','','Generated manuscript PDFs from the July export bundles. Archive labels and filenames are preserved, and identical PDFs are identified by SHA-256. These PDF records are not automatically counted as distinct papers.','','| Manuscript | Source file | Pages | SHA-256 |','|---|---|---:|---|']
        from urllib.parse import quote
        for pdf in manifest['pdfs']:
            lines.append(f'| {pdf["title"].replace("|","/")} | [{Path(pdf["path"]).name}]({quote(pdf["path"],safe="/")}) | {pdf["pages"]} | `{pdf["sha256"][:16]}…` |')
        lines+=['','[Full source index](source-manifest.csv) includes source archives, complete hashes, and duplicate references. [Source archive metadata](manifest.json) records byte counts, ETags, and checksums.','']
        (folder/'README.md').write_text('\n'.join(lines))
        batch.run([sys.executable,'scripts/update_release_catalogue.py'],repo)
        for path in folder.rglob('*'):
            if path.is_file() and path.stat().st_size>=100_000_000:raise RuntimeError('GitHub file limit: '+path.name)
        head=batch.commit_and_push(repo,'Archive July manuscript export bundle '+Path(key).name)
        shutil.rmtree(current);batch.log(stage='document-archive-uploaded-and-cleaned',key=key,commit=head)
    askpass.unlink();temporary.rmdir()


if __name__=='__main__':
    try:main()
    except Exception as error:print('::error::'+type(error).__name__+': '+re.sub(r'https?://\S+','[URL]',str(error)),flush=True);sys.exit(1)
