#!/usr/bin/env python3
"""Restore indexed files that nested source .gitignore rules omitted from Git."""
import csv
import hashlib
import json
import os
import shutil
import sys
import tarfile
from collections import defaultdict
from pathlib import Path

import release_assets as rules
import release_s3_batch as batch


def main():
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        raise RuntimeError('This repair must use temporary GitHub Actions storage.')
    event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
    items = json.loads(event['inputs']['repair_manifest'])
    for item in items:
        print('::add-mask::' + item['url'], flush=True)
    temporary = Path(os.environ['RUNNER_TEMP']) / 'indexed-asset-repair'
    temporary.mkdir()
    askpass = temporary / 'git-askpass.py'
    askpass.write_text('#!/usr/bin/env python3\nimport os,sys\nprint("x-access-token" if "username" in sys.argv[1].lower() else os.environ["GITHUB_TOKEN"])\n')
    askpass.chmod(0o700)
    os.environ.update(GIT_ASKPASS=str(askpass), GIT_TERMINAL_PROMPT='0', GIT_LFS_SKIP_SMUDGE='1')
    repo = temporary / 'repo'
    batch.checkout(repo)
    repair_list = repo / 'repair-indexed-assets.json'
    missing = json.loads(repair_list.read_text())
    source_state = json.loads((repo / 'batch-release-status.json').read_text())['archives']
    grouped = defaultdict(dict)
    expected_paths = set()
    projects = set()
    for missing_row in missing:
        project = Path(missing_row['release_path']).parts[1]
        manifest_path = repo / missing_row['manifest']
        manifest = json.loads(manifest_path.read_text())
        key = manifest['source_s3']['key']
        if key not in source_state or source_state[key]['status'] != 'uploaded':
            raise RuntimeError('Source archive was not verified: ' + key)
        output_path = missing_row['output_path']
        with (manifest_path.parent / 'asset-manifest.csv').open(encoding='utf-8-sig') as handle:
            matches = [row for row in csv.DictReader(handle) if row['output_path'] == output_path]
        if len(matches) != 1 or matches[0]['archive_path'] != missing_row['archive_path']:
            raise RuntimeError('Indexed source mapping is ambiguous: ' + missing_row['release_path'])
        row = matches[0]
        if int(row['source_bytes']) != int(missing_row['source_bytes']) or row['storage'] != 'file':
            raise RuntimeError('Unexpected indexed source size or storage: ' + missing_row['release_path'])
        name = row['member_path']
        if name in grouped[key]:
            raise RuntimeError('Duplicate source archive member: ' + name)
        grouped[key][name] = (missing_row['release_path'], row)
        expected_paths.add(missing_row['release_path'])
        projects.add(project)
    if len(expected_paths) != len(missing):
        raise RuntimeError('Duplicate repair destination')
    if set(grouped) != {item['key'] for item in items}:
        raise RuntimeError('Repair source archive list differs from indexed metadata')

    rules.EXTRA_SECRETS = [os.environ['GITHUB_TOKEN']]
    repaired = []
    archive = temporary / 'workspace.tar.gz'
    for item in items:
        key = item['key']
        source = source_state[key]
        if item['metadata']['etag'] != source['source']['etag'] or item['metadata']['bytes'] != source['source']['bytes']:
            raise RuntimeError('Live S3 source changed: ' + key)
        batch.download(item, archive)
        needed = grouped[key]
        found = set()
        with tarfile.open(archive, 'r|gz') as handle:
            for member in handle:
                if member.name not in needed:
                    continue
                if not member.isfile() or member.name in found:
                    raise RuntimeError('Invalid or repeated source member: ' + member.name)
                release_path, row = needed[member.name]
                target = repo / release_path
                if target.exists():
                    raise RuntimeError('Repair target unexpectedly exists: ' + release_path)
                output_size, result = rules.sanitize_member(handle, member, target)
                if output_size != int(row['output_bytes']) or result['sha256'] != row['sha256'] or result['split']:
                    raise RuntimeError('Restored bytes do not match the published index: ' + release_path)
                repaired.append(release_path)
                found.add(member.name)
        if found != set(needed):
            raise RuntimeError('Source archive lacked indexed members: ' + key)
        archive.unlink()
        batch.log(stage='source-repair-extracted-and-cleaned', key=key, files=len(found))

    batch.verify_files(repo, sorted(projects))
    (repo / '.git/repair-paths').write_bytes(b''.join((':(literal)' + path).encode() + b'\0' for path in repaired))
    batch.run(['git', 'add', '-f', '--sparse', '--pathspec-from-file=.git/repair-paths', '--pathspec-file-nul'], repo)
    repair_list.unlink()
    batch.run(['git', 'diff', '--cached', '--check'], repo)
    head = batch.commit_and_push(repo, 'Restore source-indexed files omitted by nested Git ignore rules')
    shutil.rmtree(repo)
    askpass.unlink()
    temporary.rmdir()
    batch.log(stage='indexed-assets-restored-and-cleaned', files=len(repaired), projects=sorted(projects), commit=head)
    with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as out:
        out.write(f'# Indexed asset repair\n\nRestored {len(repaired)} files from {len(items)} ETag-verified workspace archives and checked every restored SHA-256 against its published index. Temporary archives were removed after extraction.\n')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print('::error::' + type(error).__name__ + ': ' + str(error).split('https://')[0], flush=True)
        sys.exit(1)
