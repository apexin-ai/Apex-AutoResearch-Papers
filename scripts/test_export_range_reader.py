#!/usr/bin/env python3
"""Verify exact, bounded range-stream reads without contacting S3."""
import contextlib,hashlib,io,json,os,shutil,tarfile,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
import release_s3_export_batch as stream

class RangeReaderTests(unittest.TestCase):
    def test_read_boundaries_and_checksum(self):
        data=bytes(range(251))*80000
        calls=[]
        def request(req,timeout):
            start,end=map(int,req.get_header('Range').removeprefix('bytes=').split('-'))
            calls.append((start,end));response=io.BytesIO(data[start:end+1]);response.status=206;return response
        item={'url':'https://example.invalid/object','metadata':{'bytes':len(data),'etag':'"synthetic"'}}
        reader=stream.RangedReader(item);parts=[]
        with patch('urllib.request.urlopen',request):
            for size in [1,10240,17,8*1024**2,3,12345]:parts.append(reader.read(size))
            while True:
                part=reader.read(17473)
                if not part:break
                parts.append(part)
        self.assertEqual(b''.join(parts),data)
        self.assertEqual(reader.hash.hexdigest(),hashlib.sha256(data).hexdigest())
        self.assertEqual(len(calls),3)
        self.assertTrue(all(end-start+1<=8*1024**2 for start,end in calls))

    def test_snapshot_release_resume_and_cleanup(self):
        """Exercise the real collector, transcript exporter, and validator."""
        import release_assets as rules
        import build_trace_browser as browser
        source=Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);remote=root/'remote';remote.mkdir();(remote/'scripts').mkdir();(remote/'traces').mkdir();(remote/'paper-assets').mkdir()
            for path in (source/'scripts').glob('*.py'):shutil.copyfile(path,remote/'scripts'/path.name)
            for name in ['index.html','viewer.css','viewer.js','FORMAT.md']:shutil.copyfile(source/'traces'/name,remote/'traces'/name)
            (remote/'traces/projects.json').write_text('{"projects":[]}')
            for name in ['README.md','RELEASE_NOTES.md']:(remote/name).write_text('The repository currently contains 0 projects.\n')
            original=root/'original.tar.gz'
            with tarfile.open(original,'w:gz') as handle:
                data=b'print("archived research")\n';info=tarfile.TarInfo('workspace/projects/known/scripts/train.py');info.size=len(data);handle.addfile(info,io.BytesIO(data))
            rules.collect(original,remote,'known/workspace.tar.gz')
            browser.ROOT=remote
            # The primary collection has no conversations; a later export adds them.
            primary,_=browser.build_project(remote/'paper-assets/known')
            (remote/'traces/projects.json').write_text(json.dumps({'projects':[primary]}))
            payload=io.BytesIO()
            with tarfile.open(fileobj=payload,mode='w:gz') as handle:
                for project in ['known','new-project']:
                    messages=[{'role':'user','text':'Analyze the recorded experiment results'},{'role':'assistant','text':'I will inspect the measurements.'}]
                    data=('\n'.join(json.dumps(m) for m in messages)+'\n').encode()
                    info=tarfile.TarInfo('./'+project+'/trajectories/account-2/opaque-id.jsonl');info.size=len(data);handle.addfile(info,io.BytesIO(data))
                    data=b'credential-directory-must-be-excluded'
                    info=tarfile.TarInfo('./'+project+'/.aws/credentials');info.size=len(data);handle.addfile(info,io.BytesIO(data))
            data=payload.getvalue()
            item={'key':'uploads/projects-export-20260712.tar.gz','url':'https://example.invalid/object','metadata':{'bytes':len(data),'etag':hashlib.md5(data).hexdigest()},'max_projects':1}
            event=root/'event.json';event.write_text(json.dumps({'inputs':{'export_manifest':json.dumps(item)}}))
            runner=root/'runner';runner.mkdir();commits=[]
            def checkout(path):shutil.copytree(remote,path)
            def push(repo,title):
                commits.append(title);shutil.copytree(repo,remote,dirs_exist_ok=True);return str(len(commits))*40
            def request(req,timeout):
                start,end=map(int,req.get_header('Range').removeprefix('bytes=').split('-'))
                response=io.BytesIO(data[start:end+1]);response.status=206;return response
            def command(args,repo=None,**kwargs):
                if args[0]=='git':return ''
                return real_run(args,repo,**kwargs)
            real_run=stream.batch.run
            environment={'GITHUB_ACTIONS':'true','GITHUB_EVENT_PATH':str(event),'RUNNER_TEMP':str(runner),'GITHUB_TOKEN':'synthetic-token','GITHUB_STEP_SUMMARY':str(root/'summary')}
            try:
                with patch.dict(os.environ,environment),patch.object(stream.batch,'checkout',checkout),patch.object(stream.batch,'commit_and_push',push),patch.object(stream.batch,'run',command),patch('urllib.request.urlopen',request),contextlib.redirect_stdout(io.StringIO()):
                    stream.main()
                    self.assertFalse((runner/'research-export').exists())
                    state=json.loads((remote/'export-release-status.json').read_text())['exports'][item['key']]
                    self.assertEqual(set(state['projects']),{'known'})
                    self.assertEqual(state['status'],'in_progress')
                    stream.main()
                self.assertFalse((runner/'research-export').exists())
                state=json.loads((remote/'export-release-status.json').read_text())['exports'][item['key']]
                self.assertEqual(state['status'],'uploaded')
                self.assertEqual(state['source_sha256'],hashlib.sha256(data).hexdigest())
                self.assertEqual(set(state['projects']),{'known','new-project'})
                snapshot=remote/'research-snapshots/known/2026-07-12'
                self.assertTrue((remote/'paper-assets/known/03-code/source/scripts/train.py').exists())
                catalog=json.loads((snapshot/'05-generation-trace/catalog.json').read_text())
                entry=catalog['sessions'][0]
                self.assertEqual(entry['messages'],2)
                self.assertIn('analyze-the-recorded-experiment-results',entry['readable_path'])
                self.assertNotIn('opaque-id',entry['readable_path'])
                self.assertTrue((snapshot/'05-generation-trace'/entry['readable_path']).exists())
                self.assertFalse(any(p.name=='credentials' for p in remote.rglob('*')))
                self.assertEqual(len(commits),3)
            finally:browser.ROOT=source

if __name__=='__main__':unittest.main()
