#!/usr/bin/env python3
"""Inspect one slow archive in temporary runner storage; do not publish assets."""
import faulthandler,json,os,shutil,signal,tempfile
from pathlib import Path
import release_assets as assets
import release_s3_batch as batch

def main():
    assert os.environ.get('GITHUB_ACTIONS')=='true'
    item=json.loads(json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())['inputs']['archive_manifest'])[0]
    print('::add-mask::'+item['url'],flush=True)
    os.environ['RELEASE_DIAGNOSTICS']='true'
    with tempfile.TemporaryDirectory(prefix='archive-diagnostics-',dir=os.environ['RUNNER_TEMP']) as temporary:
        root=Path(temporary);archive=root/'workspace.tar.gz';repo=root/'release';repo.mkdir()
        batch.download(item,archive)
        def expired(signum,frame):raise TimeoutError('Eight-minute collection diagnostic limit reached')
        signal.signal(signal.SIGALRM,expired);signal.alarm(480)
        faulthandler.dump_traceback_later(60,repeat=True)
        try:
            result=assets.collect(archive,repo,item['key'],item['metadata'])
            print(json.dumps({'diagnostic_complete':True,'projects':[p['project'] for p in result['projects']]}),flush=True)
        finally:
            signal.alarm(0);faulthandler.cancel_dump_traceback_later()
    print('Diagnostic temporary files removed.',flush=True)

if __name__=='__main__':main()
