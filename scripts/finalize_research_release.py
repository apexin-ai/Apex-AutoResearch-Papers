#!/usr/bin/env python3
"""Finish the reading guides using metadata and Git trees, without asset downloads."""
import csv, datetime, gzip, io, json, os, re, shutil, subprocess, urllib.request
from pathlib import Path
from urllib.parse import quote
import build_trace_browser as browser
import release_s3_batch as batch
import update_release_catalogue as catalogue
import write_asset_guides as guides


def main():
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        raise RuntimeError('Run this final metadata pass in temporary Actions storage.')
    temporary = Path(os.environ['RUNNER_TEMP']).resolve() / 'release-finalization'
    temporary.mkdir()
    askpass = temporary / 'git-askpass.py'
    askpass.write_text('#!/usr/bin/env python3\nimport os,sys\nprint("x-access-token" if "username" in sys.argv[1].lower() else os.environ["GITHUB_TOKEN"])\n')
    askpass.chmod(0o700)
    os.environ.update(GIT_ASKPASS=str(askpass), GIT_TERMINAL_PROMPT='0', GIT_LFS_SKIP_SMUDGE='1')
    repo = temporary / 'repo'
    batch.checkout(repo)
    # Category guides are already tracked; include them so rewriting a guide
    # updates its current file rather than operating on a skipped worktree path.
    patterns = batch.PATTERNS + '/paper-assets/*/*/README.md\n/research-snapshots/*/*/README.md\n/research-snapshots/*/*/*/README.md\n/supplementary/*/pdf-index.json\n'
    (repo / '.git/info/sparse-checkout').write_text(patterns)
    batch.run(['git', 'sparse-checkout', 'reapply'], repo)
    browser.ROOT = catalogue.ROOT = guides.ROOT = repo
    expected = json.loads((repo / 'release-sources.json').read_text())
    state = json.loads((repo / 'batch-release-status.json').read_text())['archives']
    for source in expected['workspace_archives']:
        record = state.get(source['key'], {})
        assert record.get('status') == 'uploaded', 'Incomplete workspace: ' + source['key']
        assert record['source']['bytes'] == source['bytes'], source['key']
        assert record.get('archive_sha256'), source['key']
    export_state = json.loads((repo / 'export-release-status.json').read_text())['exports']
    for key in expected['streamed_exports']:
        assert export_state.get(key, {}).get('status') == 'uploaded', 'Incomplete streamed export: ' + key
        assert export_state[key].get('source_sha256'), key
    documents = json.loads((repo / 'supplementary/paper-exports-20260712/manifest.json').read_text())
    for key in expected['document_bundles']:
        assert documents['archives'].get(key, {}).get('status') == 'uploaded', key
    for name in expected['supplementary_collections']:
        assert (repo / 'supplementary' / name / 'manifest.json').exists(), name

    catalogue.main()
    guides.main()
    index = json.loads((repo / 'traces/projects.json').read_text())['projects']
    examples = []
    for entry in index:
        path = (repo / 'traces' / entry['catalog']).resolve().parent / 'example-session.json'
        if path.exists(): examples.append(json.loads(path.read_text()))
    browser.write_preview(repo / 'traces', examples)

    result = subprocess.run(['git', 'ls-tree', '-r', '-z', '--name-only', 'HEAD'], cwd=repo, stdout=subprocess.PIPE, check=True)
    tracked = set(result.stdout.decode().split('\0'))
    directories = set()
    for name in tracked:
        parent = Path(name).parent
        while parent != Path('.'):
            directories.add(parent.as_posix()); parent = parent.parent
    manifests = list((repo / 'paper-assets').glob('*/08-index/asset-manifest.json'))
    snapshots = list((repo / 'research-snapshots').glob('*/*/08-index/asset-manifest.json'))
    primary = [json.loads(path.read_text()) for path in manifests]
    pdf_records = []
    for pdf in documents['pdfs']:
        pdf_records.append({**pdf, 'release_path':'supplementary/paper-exports-20260712/'+pdf['path']})
    additional = repo / 'supplementary/exports/pdf-index.json'
    if additional.exists():
        for pdf in json.loads(additional.read_text())['pdfs']:
            pdf_records.append({**pdf, 'release_path':'supplementary/exports/source/'+pdf['file']})
    for pdf in pdf_records:
        assert pdf['release_path'] in tracked, 'Missing manuscript export: ' + pdf['release_path']
    by_hash = {}
    for pdf in pdf_records: by_hash.setdefault(pdf['sha256'], []).append(pdf)
    normalized_title = lambda value: re.sub(r'[^\w]+', '', value.casefold())
    lines = ['# Manuscript exports and revisions', '', 'These records preserve manuscript versions from the July export and revision bundles. Identical PDF bytes are grouped by SHA-256. A PDF record or a matching title does not establish a distinct paper, official submission, or acceptance.', '', '| Recorded manuscript title | Pages | PDF source copies | Related primary assets |', '|---|---:|---|---|']
    for sha, versions in sorted(by_hash.items(), key=lambda item:item[1][0]['title'].casefold()):
        pdf = versions[0]
        exact = [m for m in primary if m.get('paper_sha256')==sha]
        matching = exact or [m for m in primary if m.get('paper_pdf') and normalized_title(m['title'])==normalized_title(pdf['title'])]
        files = ' · '.join(f'[PDF {i}]({quote(v["release_path"],safe="/")})' for i,v in enumerate(versions,1))
        related = ' · '.join(f'[{m["project"]}](paper-assets/{m["project"]}/README.md)' for m in matching)
        if related: related += ' (identical PDF)' if exact else ' (matching title)'
        else: related = 'No identical PDF or exact title match in primary snapshots'
        lines.append(f'| {pdf["title"].replace("|","/")} | {pdf["pages"]} | {files} | {related} |')
    lines += ['', f'{len(pdf_records)} source PDF records; {len(by_hash)} unique PDF hashes. This is a file/version count.', '', '[Revision and rebuttal files](supplementary/exports/README.md) · [Reviewer response records](supplementary/rebuttal-share/README.md) · [Source snapshot history](SOURCE_SNAPSHOTS.md)', '']
    (repo / 'MANUSCRIPT_EXPORTS.md').write_text('\n'.join(lines))
    with (repo / 'CONTENTS.md').open('a') as out: out.write('\n[Manuscript exports and revisions](MANUSCRIPT_EXPORTS.md) groups duplicate PDF files and links matching primary project assets.\n')
    rows_checked = 0
    missing_indexed = []
    for path in manifests + snapshots:
        folder = path.parents[1]
        metadata = json.loads(path.read_text())
        if metadata.get('paper_pdf'):
            assert str((folder / '01-manuscript/paper.pdf').relative_to(repo)) in tracked, path
        with (folder / '08-index/asset-manifest.csv').open(encoding='utf-8-sig') as handle:
            for row in csv.DictReader(handle):
                name = str((folder / row['output_path']).relative_to(repo))
                if name not in tracked and name not in directories and name + '.parts' not in directories:
                    missing_indexed.append({'manifest': str(path.relative_to(repo)), 'output_path': row['output_path'], 'release_path': name, 'archive_path': row['archive_path'], 'source_bytes': row['source_bytes']})
                rows_checked += 1
    if missing_indexed:
        from collections import Counter
        (repo / 'unmatched-indexed-assets.json').write_text(json.dumps(missing_indexed, indent=2) + '\n')
        print(json.dumps({'missing_indexed_assets': len(missing_indexed), 'names': Counter(Path(r['release_path']).name for r in missing_indexed).most_common(20), 'first_paths': [r['release_path'] for r in missing_indexed[:20]]}), flush=True)
        raise RuntimeError('Indexed asset paths are absent from the committed Git tree.')
    for entry in index:
        name = str((repo / 'traces' / entry['catalog']).resolve().relative_to(repo))
        assert name in tracked, 'Missing trace catalogue: ' + entry['project']

    # Keep links to complete historical releases: the same project can appear
    # inside several workspaces, and each original snapshot remains in Git.
    commits = {}
    for page in range(1, 31):
        url = f'https://api.github.com/repos/{batch.REPOSITORY}/commits?sha=main&per_page=100&page={page}'
        request = urllib.request.Request(url, headers={'Authorization': 'Bearer ' + os.environ['GITHUB_TOKEN'], 'Accept': 'application/vnd.github+json'})
        with urllib.request.urlopen(request, timeout=60) as response: history = json.load(response)
        for commit in history:
            match = re.fullmatch(r'Release research assets and readable traces for ([A-Za-z0-9_.-]+)', commit['commit']['message'])
            if match: commits.setdefault(match.group(1), commit['sha'])
        if len(commits) >= len(expected['workspace_archives']) or not history: break
    lines = ['# Workspace source snapshots', '', 'Each row links to the complete release commit for an original S3 workspace archive. A workspace can contain several project directories. If a later archive updates the same project, earlier files and conversations remain accessible through these fixed commit links.', '', '| Source archive | SHA-256 | Released project snapshots |', '|---|---|---|']
    for source in expected['workspace_archives']:
        key = source['key']; record = state[key]; slug = key.split('/')[0]
        assert slug in commits, 'Missing complete release commit: ' + slug
        links = ' · '.join(f'[{project}](https://github.com/{batch.REPOSITORY}/tree/{commits[slug]}/paper-assets/{project})' for project in record['projects'])
        lines.append(f'| `{key}` | `{record["archive_sha256"]}` | {links} |')
    (repo / 'SOURCE_SNAPSHOTS.md').write_text('\n'.join(lines) + '\n')
    with (repo / 'CONTENTS.md').open('a') as out: out.write('\n[Original workspace snapshots](SOURCE_SNAPSHOTS.md) retain fixed links to every archive release.\n')
    mirror_checked = 0
    mirrors = {}
    with gzip.open(repo / 'release-source-mirrors.csv.gz', 'rt') as handle:
        for row in csv.DictReader(handle): mirrors.setdefault(row['archive_key'], []).append(row)
    mirror_mismatches = []
    import release_assets as rules
    for key, objects in mirrors.items():
        commit = commits[key.split('/')[0]]
        batch.run(['git', 'fetch', '--filter=blob:none', '--depth=1', 'origin', commit], repo, quiet=True)
        source_files = set(); excluded_files = set()
        for project in state[key]['projects']:
            name = f'paper-assets/{project}/08-index/asset-manifest.csv'
            content = batch.run(['git', 'show', commit + ':' + name], repo, quiet=True)
            for row in csv.DictReader(io.StringIO(content)):
                source_files.add((project, row['archive_path'], int(row['source_bytes'])))
            name = f'paper-assets/{project}/08-index/excluded-files.csv'
            content = batch.run(['git', 'show', commit + ':' + name], repo, quiet=True)
            for row in csv.DictReader(io.StringIO(content)):
                p, relative = rules.project_path(row['member_path'], key.split('/')[0])
                excluded_files.add((p, relative, int(row['source_bytes'])))
        for row in objects:
            identifier = (row['project'], row['relative_path'], int(row['source_bytes']))
            if identifier in source_files or identifier in excluded_files: mirror_checked += 1
            else: mirror_mismatches.append(row)
    if mirror_mismatches:
        # Listing metadata is not treated as proof that distinct file bytes are
        # equal. Fail here if a mirror contains an unindexed path or byte size.
        (repo / 'unmatched-mirror-objects.json').write_text(json.dumps(mirror_mismatches, indent=2))
        print(json.dumps({'unmatched_mirror_objects':len(mirror_mismatches),'first_paths':[r['s3_key'] for r in mirror_mismatches[:20]]}), flush=True)
        raise RuntimeError('Decompressed S3 mirrors contain unindexed objects; release those before finalization.')
    expected['decompressed_mirror_audit'].update(status='Candidate objects matched to original archive source or exclusion records by project, path, and byte size', matched_objects=mirror_checked)
    (repo / 'release-sources.json').write_text(json.dumps(expected, indent=2) + '\n')
    papers = sum(bool(json.loads(p.read_text()).get('paper_pdf')) for p in manifests)
    summary = {'generated_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'workspace_archives': len(state), 'primary_project_records': len(manifests), 'primary_projects_with_manuscript_pdf': papers, 'additional_project_records_without_pdf': len(manifests)-papers, 'dated_project_snapshots': len(snapshots), 'supplementary_collections': len(list((repo/'supplementary').glob('*/manifest.json'))), 'document_pdf_records': len(documents['pdfs']), 'trace_collections': len(index), 'trace_source_records': sum(e['statistics'].get('files', 0) for e in index), 'recorded_events': sum(e['statistics'].get('messages', 0) for e in index), 'indexed_asset_rows_verified': rows_checked, 'mirror_objects_matched_by_original_path_and_size': mirror_checked, 'offline_preview_rounds': len(examples), 'source_archives_verified': True}
    (repo / 'release-summary.json').write_text(json.dumps(summary, indent=2) + '\n')
    (repo / 'RELEASE_NOTES.md').write_text(f'''# Research asset release

This release organizes {len(state)} original workspace archives into {papers} project records with manuscript PDFs and {len(manifests)-papers} additional project records. The [contents](CONTENTS.md) links to the available papers, code, experiment files, and generation traces. Counts describe source records; they are not a count of independently verified scientific discoveries.

The July project export adds {len(snapshots)} dated snapshots alongside the workspace releases. The [supplementary collections](supplementary/README.md) retain benchmark implementations, results, manuscript exports, revisions, and rebuttals. [Original workspace snapshots](SOURCE_SNAPSHOTS.md) provide fixed links when the same project appears in several source archives.

## Reading the evidence

- Project and category READMEs show concrete source-file examples.
- Readable Markdown transcripts label user instructions, assistant responses, tool calls, and tool results in recorded order. Adjacent JSON files preserve normalized structure and source provenance.
- [The offline trace preview](traces/demo.html) embeds {len(examples)} actual bounded recorded rounds. The complete interactive browser is available through `python3 scripts/serve_traces.py --open` after downloading the repository.
- Per-project manifests map original archive members to released files. Archive checksums, exclusions, and PDF versions remain available in each project index.

## Collection and verification

Archives were handled sequentially in temporary storage. Each changed trace collection was compared with its sanitized source for content and order; file sizes and credential patterns were checked before upload. Pushes were checked against the remote commit before temporary project files were removed. This final pass verified {rows_checked:,} indexed asset paths against the committed Git tree.

Generated documentation is English. Original documents, code, and conversations retain their recorded language. Credential/account snapshots, dependency installations, caches, and Git internals are excluded; inline attachment payloads and credentials are redacted. Large files use checksum-indexed parts. The source coverage and intentional exclusions are recorded in [release-sources.json](release-sources.json).

Research code was archived without rerunning the scientific experiments. Internal reviews, manuscript filenames, and status notes do not establish independent reproduction or external acceptance. User-role records can originate from agents or the runtime system and do not identify human authorship.
''')
    batch.run(['git', 'diff', '--check'], repo)
    head = batch.commit_and_push(repo, 'Finalize English research catalogue, concrete examples, and source snapshot links')
    shutil.rmtree(repo); askpass.unlink(); temporary.rmdir()
    batch.log(stage='release-finalized-and-cleaned', commit=head, **summary)
    with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as out: out.write('# Completed research asset release\n\n```json\n' + json.dumps(summary, indent=2) + '\n```\n')


if __name__ == '__main__': main()
