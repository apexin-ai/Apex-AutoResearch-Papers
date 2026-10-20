#!/usr/bin/env python3
"""Exercise the final publication gate with real manifests and a fake Git remote."""
import contextlib, csv, gzip, hashlib, io, json, os, shutil, subprocess, tarfile, tempfile, unittest
from pathlib import Path
from unittest.mock import patch
import build_trace_browser as browser
import finalize_research_release as finalizer
import release_assets as rules


class FinalizationTests(unittest.TestCase):
    def test_metadata_publication_and_unmatched_source_gate(self):
        source = Path(__file__).resolve().parents[1]
        for unmatched in [False, True]:
            with self.subTest(unmatched=unmatched), tempfile.TemporaryDirectory() as temporary:
                root=Path(temporary);remote=root/'remote';remote.mkdir();(remote/'paper-assets').mkdir();(remote/'traces').mkdir()
                for name in ['index.html','viewer.css','viewer.js','FORMAT.md']:shutil.copyfile(source/'traces'/name,remote/'traces'/name)
                for name in ['README.md','RELEASE_NOTES.md']:(remote/name).write_text('The repository currently contains 0 projects.\n')
                (remote/'traces/projects.json').write_text('{"projects":[]}')
                archive=root/'workspace.tar.gz';code=b'print(1)\n'
                with tarfile.open(archive,'w:gz') as handle:
                    records={'scripts/analyze.py':code,'scripts/.hf_cache/known.bin':b'present','logs/chats/task.jsonl':b'{"role":"user","text":"Inspect results"}\n{"role":"assistant","text":"Recorded results inspected."}\n'}
                    for name,data in records.items():
                        member=tarfile.TarInfo('workspace/projects/known/'+name);member.size=len(data);handle.addfile(member,io.BytesIO(data))
                key='known/workspace.tar.gz';result=rules.collect(archive,remote,key)
                with patch.object(browser,'ROOT',remote),contextlib.redirect_stdout(io.StringIO()):entry,_=browser.build_project(remote/'paper-assets/known')
                (remote/'traces/projects.json').write_text(json.dumps({'projects':[entry]}))
                expected={'workspace_archives':[{'key':key,'bytes':archive.stat().st_size}],'streamed_exports':[],'document_bundles':[],'supplementary_collections':[],'decompressed_mirror_audit':{'excluded_cache_candidate_objects':1,'excluded_cache_candidate_bytes':5}}
                (remote/'release-sources.json').write_text(json.dumps(expected))
                (remote/'release-source-mirror-supplements.json').write_text('{"objects":[]}')
                (remote/'batch-release-status.json').write_text(json.dumps({'archives':{key:{'status':'uploaded','source':{'bytes':archive.stat().st_size},'archive_sha256':result['archive_sha256'],'projects':['known']}}}))
                (remote/'export-release-status.json').write_text('{"exports":{}}')
                documents=remote/'supplementary/paper-exports-20260712';documents.mkdir(parents=True)
                (documents/'manifest.json').write_text('{"archives":{},"pdfs":[],"included_files":0}')
                with gzip.open(remote/'release-source-mirrors.csv.gz','wt',newline='') as handle:
                    writer=csv.DictWriter(handle,fieldnames=['archive_key','project','relative_path','source_bytes','s3_key']);writer.writeheader()
                    writer.writerow({'archive_key':key,'project':'known','relative_path':'scripts/missing.py' if unmatched else 'scripts/analyze.py','source_bytes':len(code),'s3_key':'unpacked/known/workspace/scripts/analyze.py'})
                    writer.writerow({'archive_key':key,'project':'known','relative_path':'scripts/.hf_cache/known.bin','source_bytes':7,'s3_key':'unpacked/known/workspace/scripts/.hf_cache/known.bin'})
                    writer.writerow({'archive_key':key,'project':'known','relative_path':'scripts/.hf_cache/missing.bin','source_bytes':5,'s3_key':'unpacked/known/workspace/scripts/.hf_cache/missing.bin'})
                tracked=[p.relative_to(remote).as_posix() for p in remote.rglob('*') if p.is_file()]
                runner=root/'runner';runner.mkdir();commits=[]
                def checkout(path):shutil.copytree(remote,path);(path/'.git/info').mkdir(parents=True)
                def git(args,repo=None,**kwargs):
                    if args[:2]==['git','show']:return (remote/args[2].split(':',1)[1]).read_text()
                    return ''
                def push(repo,title):commits.append(title);shutil.copytree(repo,remote,dirs_exist_ok=True);return 'a'*40
                def process(args,**kwargs):
                    self.assertEqual(args[:2],['git','ls-tree'])
                    return subprocess.CompletedProcess(args,0,stdout=('\0'.join(tracked)+'\0').encode())
                def request(req,timeout):
                    self.assertIn('/commits?',req.full_url)
                    return io.BytesIO(json.dumps([{'sha':'b'*40,'commit':{'message':'Release research assets and readable traces for known'}}]).encode())
                environment={'GITHUB_ACTIONS':'true','RUNNER_TEMP':str(runner),'GITHUB_TOKEN':'synthetic-token','GITHUB_STEP_SUMMARY':str(root/'summary')}
                with patch.dict(os.environ,environment),patch.object(finalizer.batch,'checkout',checkout),patch.object(finalizer.batch,'run',git),patch.object(finalizer.batch,'commit_and_push',push),patch('subprocess.run',process),patch('urllib.request.urlopen',request),patch.object(browser,'ROOT',browser.ROOT),patch.object(finalizer.catalogue,'ROOT',finalizer.catalogue.ROOT),patch.object(finalizer.guides,'ROOT',finalizer.guides.ROOT),contextlib.redirect_stdout(io.StringIO()):
                    if unmatched:
                        with self.assertRaisesRegex(RuntimeError,'unindexed objects'):finalizer.main()
                    else:finalizer.main()
                if unmatched:
                    self.assertEqual(commits,[])
                    self.assertTrue((runner/'release-finalization/repo/unmatched-mirror-objects.json').exists())
                else:
                    self.assertFalse((runner/'release-finalization').exists())
                    self.assertEqual(len(commits),1)
                    summary=json.loads((remote/'release-summary.json').read_text())
                    self.assertEqual(summary['workspace_archives'],1)
                    self.assertEqual(summary['mirror_objects_matched_by_original_path_and_size'],2)
                    self.assertEqual(summary['mirror_cache_objects_excluded'],1)
                    self.assertEqual(summary['recorded_events'],2)
                    guide=(remote/'paper-assets/known/README.md').read_text()
                    self.assertIn('scripts/analyze.py',guide)
                    self.assertTrue((remote/'SOURCE_SNAPSHOTS.md').exists())


if __name__=='__main__':unittest.main()
