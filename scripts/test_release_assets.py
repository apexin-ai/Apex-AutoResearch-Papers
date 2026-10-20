#!/usr/bin/env python3
"""Safety and completeness checks for the streaming archive collector."""
import io, json, tempfile, tarfile, unittest, zipfile, gzip, re, subprocess, sys
from pathlib import Path
import release_assets as a
from pypdf import PdfWriter

class ReleaseAssetTests(unittest.TestCase):
    def test_redaction_long_text_and_assignment_equivalence(self):
        pattern,replacement=a.REDACT_PATTERNS[-2]
        previous=re.compile(pattern.pattern.replace('(?<![A-Z_])',''))
        for prefix in ['', 'project_', 'ABC', '9abc', 'wordAWS_', 'lower_']:
            for key in ['API_KEY','ACCESS_TOKEN','SECRET_KEY','AUTH_TOKEN','PASSWORD','AWS_SECRET_ACCESS_KEY','AWS_ACCESS_KEY_ID']:
                text=f'before {prefix}{key} = "synthetic-sensitive-value" after'
                self.assertEqual(pattern.sub(replacement,text),previous.sub(replacement,text))
                self.assertNotIn('synthetic-sensitive-value',a.redact_text(text))
        # A long token must not cause the assignment matcher to retry every
        # suffix. Use a subprocess so a regression cannot hang the test suite.
        program='import release_assets as a; text="a"*1000000; assert a.redact_text(text)==text'
        subprocess.run([sys.executable,'-c',program],cwd=Path(a.__file__).parent,check=True,timeout=5)
    def test_paths(self):
        for path in ['/absolute/file','project/../../escape']:
            with self.assertRaises(ValueError):a.safe_rel(path)
        self.assertEqual(a.safe_rel('scripts/run.py'),Path('scripts/run.py'))
        self.assertTrue(a.excluded('artifacts/v1_irt_refit_pilot/.hf_cache/dataset.arrow'))
        self.assertFalse(a.excluded('artifacts/v1_irt_refit_pilot/results/dataset.arrow'))
    def test_nested_archives_are_sanitized(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);path=root/'bundle.zip'
            with zipfile.ZipFile(path,'w') as f:
                f.writestr('code/run.py','print("retained")')
                f.writestr('.env','PRIVATE_DATA=secret')
                f.writestr('config.json','{"api_key":"synthetic-sensitive-value"}')
                f.writestr('invalid.zip','<!doctype html><title>Validating...</title>')
            _,info=a.sanitize_nested(path,root/'release.zip')
            self.assertEqual(info['storage'],'sanitized-archive-contents')
            out=root/'release.zip.contents'
            self.assertTrue((out/'code/run.py').exists());self.assertFalse((out/'.env').exists())
            self.assertNotIn('synthetic-sensitive-value',(out/'config.json').read_text())
            self.assertFalse((out/'invalid.zip.contents').exists())
            self.assertIn('Invalid nested archive',(out/'extraction-manifest.csv').read_text())
            with zipfile.ZipFile(root/'traversal.zip','w') as f:f.writestr('../../escape','bad')
            with self.assertRaises(ValueError):a.sanitize_nested(root/'traversal.zip',root/'out.zip')
            with gzip.open(root/'metrics.csv.gz','wb') as f:f.write(b'seed,score\n1,0.7\n')
            a.sanitize_nested(root/'metrics.csv.gz',root/'output.csv.gz')
            self.assertEqual((root/'output.csv.gz.contents/output.csv').read_text(),'seed,score\n1,0.7\n')
    def test_archive_order_and_redaction(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);archive=root/'workspace.tar.gz';repo=root/'repo';repo.mkdir()
            pdf=io.BytesIO();w=PdfWriter();w.add_blank_page(300,300);w.add_metadata({'/Title':'A synthetic asset-release test'});w.write(pdf)
            files={
              'workspace/projects/example/scripts/run.py':b'print("not executed")\n',
              'workspace/projects/example/.venv/ignored.py':b'ignored',
              'workspace/projects/example/.env':b'PRIVATE_DATA=secret',
              'workspace/projects/example/artifacts/data/dataset.zip':b'<!doctype html><title>Validating...</title>',
              'workspace/projects/example/logs/chats/task.jsonl':json.dumps({'role':'assistant','content':{'api_key':'synthetic-sensitive-value','text':'retained evidence'}}).encode()+b'\n',
              'workspace/projects/example/docs/paper/main.pdf':pdf.getvalue(),
              'workspace/projects/second/results/metrics.csv':b'seed,score\n1,0.7\n',
            }
            with tarfile.open(archive,'w:gz') as f:
                for path,data in files.items():
                    m=tarfile.TarInfo(path);m.size=len(data);f.addfile(m,io.BytesIO(data))
                link=tarfile.TarInfo('workspace/projects/example/scripts/escape');link.type=tarfile.SYMTYPE;link.linkname='/etc/passwd';f.addfile(link)
            result=a.collect(archive,repo,'example/workspace.tar.gz')
            self.assertEqual(len(result['projects']),2)
            project=repo/'paper-assets/example'
            self.assertTrue((project/'03-code/source/scripts/run.py').exists())
            self.assertEqual((project/'01-manuscript/paper.pdf').read_bytes(),pdf.getvalue())
            with tarfile.open(project/'05-generation-trace/trace-files.tar.gz') as f:
                text=f.extractfile(f.getmembers()[0]).read().decode()
                self.assertNotIn('synthetic-sensitive-value',text);self.assertIn('retained evidence',text)
            exclusions=(project/'08-index/excluded-files.csv').read_text()
            for marker in ['.venv','.env','Non-regular','dataset.zip','Invalid nested archive']:self.assertIn(marker,exclusions)
            self.assertFalse((project/'04-experiments/source/artifacts/data/dataset.zip.contents').exists())
            self.assertFalse((project/'03-code/source/scripts/escape').exists())

if __name__=='__main__':unittest.main()
