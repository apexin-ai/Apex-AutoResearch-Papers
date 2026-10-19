#!/usr/bin/env python3
"""Safety and completeness checks for the streaming archive collector."""
import io, json, tempfile, tarfile, unittest
from pathlib import Path
import release_assets as a
from pypdf import PdfWriter

class ReleaseAssetTests(unittest.TestCase):
    def test_paths(self):
        for path in ['/absolute/file','project/../../escape']:
            with self.assertRaises(ValueError):a.safe_rel(path)
        self.assertEqual(a.safe_rel('scripts/run.py'),Path('scripts/run.py'))
    def test_archive_order_and_redaction(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);archive=root/'workspace.tar.gz';repo=root/'repo';repo.mkdir()
            pdf=io.BytesIO();w=PdfWriter();w.add_blank_page(300,300);w.add_metadata({'/Title':'A synthetic asset-release test'});w.write(pdf)
            files={
              'workspace/projects/example/scripts/run.py':b'print("not executed")\n',
              'workspace/projects/example/.venv/ignored.py':b'ignored',
              'workspace/projects/example/.env':b'PRIVATE_DATA=secret',
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
            for marker in ['.venv','.env','Non-regular']:self.assertIn(marker,exclusions)
            self.assertFalse((project/'03-code/source/scripts/escape').exists())

if __name__=='__main__':unittest.main()
