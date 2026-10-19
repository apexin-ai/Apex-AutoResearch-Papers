#!/usr/bin/env python3
"""Collect paper-facing assets from each examples/*/workspace.tar.gz."""

from __future__ import annotations

import csv
import hashlib
import html
import io
import json
import os
import re
import shutil
import tarfile
import zipfile
from collections import Counter
from contextlib import ExitStack
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "papers"
OUT = ROOT / "paper-assets"
TRACE_LOGS = ("logs/chats/", "logs/workers/", "task_context/history/")
SKIP_PARTS = {
    ".venv", ".pb_venv", "venv", "site-packages", "dist-packages",
    ".git", "__pycache__", "node_modules", "_pdf_images",
    "_figure_backups", "dist-info",
}
SOURCE_EXT = {".tex", ".bib", ".bst", ".sty", ".cls", ".bbx", ".cbx", ".lbx", ".png", ".jpg", ".jpeg", ".eps", ".svg", ".pdf"}
CODE_EXT = {".py", ".sh", ".r", ".jl", ".ipynb", ".js", ".ts", ".m"}
DATA_EXT = {".csv", ".tsv", ".json", ".jsonl", ".parquet", ".xlsx", ".npy", ".npz", ".pt", ".pth", ".txt", ".md"}
TEXT_EXT = {
    ".bib", ".bbx", ".cbx", ".cff", ".cfg", ".cls", ".conf", ".csv", ".html",
    ".ini", ".ipynb", ".jl", ".json", ".jsonl", ".js", ".md", ".m", ".py",
    ".r", ".sh", ".sty", ".tex", ".toml", ".ts", ".tsv", ".txt", ".xml",
    ".yaml", ".yml",
}
ENV_NAMES = {"requirements.txt", "requirements.lock", "pyproject.toml", "uv.lock", "environment.yml", "environment.yaml", "conda.yml", "dockerfile", "makefile"}
MAINT_NAMES = {
    "license", "citation.cff", "changelog.md", "changes.md", "readme.md",
    "contributing.md", "roadmap.md", "registry.yaml", "decisions.yaml",
    "experiment_plan.yaml", "paper_provenance.yaml", "literature_map.yaml",
    "writing_plan.yaml", "mistakes.yaml", "constraints.yaml", "report.md",
    "study_status.md", "arr_checklist_reference.md", "arr_submission_metadata.md",
}
MAINT_SUFFIXES = {".cff", ".csv", ".json", ".md", ".txt", ".yaml", ".yml"}

REDACT_PATTERNS = [
    (re.compile(r"(?i)(\b(?:api[_-]?key|access[_-]?key|secret|password|passwd|authorization|cookie|credential|client_secret)\b\s*[\"']?\s*[:=]\s*[\"']?)(?:(?:bearer|basic)\s+)?([^\s\"',;}]+)"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(\bbearer\s+)[A-Za-z0-9._~+/=-]{12,}"), r"\1[REDACTED]"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "[REDACTED_AWS_KEY]"),
    (re.compile(r"\bsk-ant-(?:api|oat)[A-Za-z0-9_-]{12,}\b"), "[REDACTED_API_TOKEN]"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"), "[REDACTED_GITHUB_TOKEN]"),
    (re.compile(r"\bhf_[A-Za-z0-9]{20,}\b"), "[REDACTED_HF_TOKEN]"),
    (re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"), "[REDACTED_GOOGLE_TOKEN]"),
    (re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"), "[REDACTED_SLACK_TOKEN]"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----", re.S), "[REDACTED_PRIVATE_KEY]"),
    # Some JSONL logs contain an escaped, truncated key preview without the END marker.
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?(?=\\\\\"|\"|$)", re.S), "[REDACTED_PRIVATE_KEY]"),
]
SECRET_KEY = re.compile(r"(?i)^(?:api[_-]?key|access[_-]?key|secret|password|passwd|authorization|cookie|credential|client_secret|refresh_token|access_token)$")
BASE64_ONLY = re.compile(r"[A-Za-z0-9+/=_-]+$")
BINARY_FIELD = re.compile(r"(?i)([\"']?(?:data|base64|image_bytes|audio_bytes)[\"']?\s*[:=]\s*[\"'])([A-Za-z0-9+/=_-]{512,})([\"'])")


def safe_rel(path: str) -> Path:
    parts = Path(path).parts
    if Path(path).is_absolute() or not parts or any(p in {"..", ""} for p in parts):
        raise ValueError(f"Unsafe archive path: {path}")
    return Path(*parts)


def excluded(path: str) -> bool:
    parts = set(Path(path).parts)
    return bool(parts & SKIP_PARTS) or any(p.startswith(".") and p.endswith(".lock") for p in parts)


EXTRA_SECRETS = []

def redact_text(text: str) -> str:
    for value in EXTRA_SECRETS:
        text = text.replace(value, "[REDACTED_CREDENTIAL]")
    for pattern, replacement in REDACT_PATTERNS:
        text = pattern.sub(replacement, text)
    return text


def redact_json(value):
    if isinstance(value, dict):
        return {k: ("[REDACTED]" if SECRET_KEY.fullmatch(str(k)) else redact_json(v)) for k, v in value.items()}
    if isinstance(value, list):
        return [redact_json(v) for v in value]
    if isinstance(value, str):
        if len(value) >= 512 and BASE64_ONLY.fullmatch(value):
            return "[ATTACHMENT_DATA_REDACTED]"
        return redact_text(value)
    return value


def source_target(project_dir: Path, category: str, rel: str) -> Path:
    return project_dir / category / "source" / safe_rel(rel)


def write_member(tf: tarfile.TarFile, member: tarfile.TarInfo, target: Path) -> None:
    if not member.isfile():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    with tf.extractfile(member) as src:
        raw = src.read()
    if target.suffix.lower() in TEXT_EXT or target.name.lower() in ENV_NAMES | MAINT_NAMES:
        text = redact_text(raw.decode("utf-8", "replace"))
        text = BINARY_FIELD.sub(r"\1[ATTACHMENT_DATA_REDACTED]\3", text)
        raw = text.encode("utf-8")
    target.write_bytes(raw)


def write_trace(tf: tarfile.TarFile, member: tarfile.TarInfo, trace_tar: tarfile.TarFile, rel: str) -> int:
    if not member.isfile():
        return 0
    with tf.extractfile(member) as src:
        raw = src.read()
    if rel.endswith(".jsonl") or rel.endswith(".log") or rel.endswith("_result.json"):
        lines = []
        for line in raw.splitlines():
            try:
                obj = json.loads(line)
                line = json.dumps(redact_json(obj), ensure_ascii=False, separators=(",", ":")).encode("utf-8")
            except (json.JSONDecodeError, UnicodeDecodeError):
                text_line = redact_text(line.decode("utf-8", "replace"))
                text_line = BINARY_FIELD.sub(r"\1[ATTACHMENT_DATA_REDACTED]\3", text_line)
                line = text_line.encode("utf-8")
            lines.append(line)
        raw = b"\n".join(lines) + (b"\n" if lines else b"")
    else:
        raw = redact_text(raw.decode("utf-8", "replace")).encode("utf-8")
    info = tarfile.TarInfo(name=rel)
    info.size = len(raw)
    info.mtime = member.mtime
    trace_tar.addfile(info, io.BytesIO(raw))
    return len(raw)


def is_paper_source(rel: str) -> bool:
    if not rel.startswith("docs/paper/") or excluded(rel):
        return False
    if "review_template" in Path(rel).parts:
        return False
    if rel.endswith("/main.pdf"):
        return False
    return Path(rel).suffix.lower() in SOURCE_EXT


def is_code(rel: str) -> bool:
    if excluded(rel):
        return False
    path = Path(rel)
    if path.suffix.lower() in CODE_EXT:
        return True
    return path.name.lower() in ENV_NAMES


def is_experiment_data(rel: str) -> bool:
    if excluded(rel) or Path(rel).suffix.lower() not in DATA_EXT:
        return False
    p = Path(rel)
    parts = p.parts
    if not parts:
        return False
    if parts[0] in {"data", "results"}:
        return True
    if rel.startswith(("docs/paper/data/", "artifacts/_project/data/", "artifacts/_project/paper/", "artifacts/paper_data/", "artifacts/results/")):
        return True
    if parts[0] == "artifacts" and any(x in {"data", "results"} for x in parts[1:-1]):
        return True
    if parts[0] == "artifacts" and len(parts) == 2 and re.search(r"(?:result|summary|metric|benchmark|seed|sweep|analysis|data)", p.name, re.I):
        return True
    return False


def is_maintenance(rel: str) -> bool:
    if excluded(rel):
        return False
    path = Path(rel)
    name = path.name.lower()
    if name in MAINT_NAMES:
        return True
    if name.startswith(("license.", "changelog.", "citation.")):
        return True
    if path.suffix.lower() not in MAINT_SUFFIXES:
        return False
    return bool(re.search(
        r"(?:^|[_-])(?:arr|openreview|submission|provenance|study_status|paper_status|version_history|checklist)(?:[_-]|$)",
        path.stem,
        re.I,
    ))


def is_review(rel: str) -> bool:
    if excluded(rel):
        return False
    return rel.startswith("artifacts/review_reports/") and Path(rel).suffix.lower() in {".md", ".txt", ".json"}


def is_validation(rel: str) -> bool:
    if excluded(rel):
        return False
    path = Path(rel)
    if path.suffix.lower() not in {".md", ".txt", ".json", ".yaml", ".yml", ".csv"}:
        return False
    return bool(re.search(r"(?:audit|validation|verification|visual_review|consistency_check)", path.name, re.I))


def is_contribution_note(rel: str) -> bool:
    return rel.startswith("task_context/") and "/history/" not in rel and Path(rel).suffix.lower() in {".md", ".txt"} and not excluded(rel)


def is_trace(rel: str, member: tarfile.TarInfo) -> bool:
    if excluded(rel) or not member.isfile():
        return False
    return ((rel.startswith("logs/chats/") and rel.endswith(".jsonl"))
            or (rel.startswith("logs/workers/") and (rel.endswith(".log") or rel.endswith("_result.json")))
            or (rel.startswith("task_context/history/") and Path(rel).suffix.lower() in {".md", ".txt"}))


# Release importer: preserve project files without extracting executables or links.
import argparse
import datetime
import tempfile
import gzip
import bz2
import lzma
from types import SimpleNamespace

PART_SIZE = 80 * 1024**2
EXCLUDE_NAMES = {'.env', '.env.local', '.env.production', 'credentials', 'credentials.json', 'accounts.json', 'auth.json', '.netrc', '.npmrc', '.pypirc'}
SKIP_PARTS.update({'.cache', '.npm', '.mypy_cache', '.pytest_cache', '.ruff_cache', '.tox', '.conda', '.ssh', '.aws', '.claude', '.codex', '.idea', '.vscode', '.ipynb_checkpoints', 'wandb'})
REDACT_PATTERNS.extend([
    (re.compile(r'\bASIA[A-Z0-9]{16}\b'), '[REDACTED_AWS_KEY]'),
    (re.compile(r'\bgithub_pat_[A-Za-z0-9_]{30,}\b'), '[REDACTED_GITHUB_TOKEN]'),
    (re.compile(r'\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{24,}\b'), '[REDACTED_API_TOKEN]'),
    (re.compile(r'(?i)((?:AWS_SECRET_ACCESS_KEY|AWS_ACCESS_KEY_ID|(?<![A-Z_])[A-Z_]*(?:API_KEY|ACCESS_TOKEN|SECRET_KEY|AUTH_TOKEN|PASSWORD))\s*[\"\x27]?\s*[:=]\s*[\"\x27]?)[^\s\"\x27,;}]+'), r'\1[REDACTED]'),
    (re.compile(r'(?i)(https?://)[^\s/@:]+:[^\s/@]+@'), r'\1[REDACTED]@'),
])
CATEGORIES = {
 '01-manuscript':'Manuscript PDF, source, references, figures, and version candidates.',
 '02-contributions':'Recorded agent roles and task instructions.',
 '03-code':'Research code, scripts, configurations, and dependency manifests.',
 '04-experiments':'Data, experiment outputs, metrics, and supporting artifacts.',
 '05-generation-trace':'Readable Markdown conversations, complete normalized JSON, and sanitized source logs.',
 '06-validation':'Internal reviews, audits, and verification records.',
 '07-maintenance':'Project documentation, roadmaps, provenance, and maintenance notes.',
 '08-index':'File manifests, original paths, exclusions, and source checksums.',
}


def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(8*1024**2),b''):h.update(block)
    return h.hexdigest()


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore',lineterminator='\n');w.writeheader();w.writerows(rows)


def split_file(path):
    if path.stat().st_size < 95_000_000: return None
    directory=path.with_name(path.name+'.parts');directory.mkdir()
    rows=[]; whole=hashlib.sha256()
    with path.open('rb') as f:
        for i,data in enumerate(iter(lambda:f.read(PART_SIZE),b''),1):
            name=f'part-{i:04d}';(directory/name).write_bytes(data);whole.update(data)
            rows.append({'part':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    write_csv(directory/'manifest.csv',['part','bytes','sha256'],rows)
    (directory/'README.md').write_text(f'# Split file: {path.name}\n\nReconstruct from the repository root:\n\n```bash\npython3 scripts/reconstruct_trace.py {directory.relative_to(ROOT) if directory.is_relative_to(ROOT) else directory.name} {path.name}\n```\n\nOriginal bytes: {path.stat().st_size:,}; SHA-256: `{whole.hexdigest()}`. Parts retain the exact file bytes.\n')
    path.unlink();return directory


def project_path(name, fallback):
    path=Path(name)
    if path.is_absolute() or '..' in path.parts: raise ValueError('Unsafe archive member path')
    parts=path.parts
    if 'projects' in parts:
        i=parts.index('projects')
        if i+2<len(parts):return parts[i+1],'/'.join(parts[i+2:])
    # Some exports store a single project directly under a workspace root.
    for anchor in ('docs','logs','task_context','artifacts','scripts','results','data','src'):
        if anchor in parts:
            i=parts.index(anchor)
            if i==0 or (i==1 and parts[0] in {'workspace',fallback}):return fallback,'/'.join(parts[i:])
    return None,None


def classify_asset(rel):
    p=Path(rel)
    if rel.startswith(('logs/chats/','logs/workers/','task_context/history/')) and p.suffix.lower() in {'.jsonl','.json','.log','.md','.txt'}:
        return '05-generation-trace'
    if rel.startswith('docs/paper/') or (p.suffix.lower() in {'.tex','.bib','.bst','.sty','.cls'}):return '01-manuscript'
    if p.suffix.lower()=='.pdf' and ('paper' in p.name.lower() or 'submitted' in p.name.lower() or any(x in p.parts for x in {'paper','papers','review_reports'})):return '01-manuscript'
    if rel.startswith('task_context/'):return '02-contributions'
    if is_review(rel) or is_validation(rel) or rel.startswith(('docs/reviews/','artifacts/review_reports/')):return '06-validation'
    if is_code(rel) or p.suffix.lower() in {'.yaml','.yml','.toml','.cfg','.ini','.lock','.cu','.cpp','.c','.h','.hpp','.rs','.go','.ipynb','.ipynb_checkpoints'} or p.name.lower() in {'dockerfile','.gitignore'}:return '03-code'
    if is_maintenance(rel) or rel.startswith('docs/') or p.suffix.lower() in {'.md','.rst'}:return '07-maintenance'
    return '04-experiments'


def sanitize_member(tf, member, target, trace=None, rel=None):
    # JSONL is handled line by line so a large conversation does not require a
    # second full in-memory copy. The temporary spool is deleted after each member.
    if target is not None and Path(member.name).suffix.lower() in {'.tar','.zip','.gz','.tgz','.bz2','.xz'}:
        with tempfile.NamedTemporaryFile(suffix=Path(member.name).suffix) as nested:
            with tf.extractfile(member) as source:shutil.copyfileobj(source,nested,4*1024**2)
            nested.flush()
            return sanitize_nested(Path(nested.name),target)
    with tf.extractfile(member) as source:
        if trace is not None:
            with tempfile.TemporaryFile() as spool:
                for line in source:
                    try:
                        obj=json.loads(line)
                        out=json.dumps(redact_json(obj),ensure_ascii=False,separators=(',',':')).encode()+b'\n'
                    except (ValueError,UnicodeDecodeError):
                        text=redact_text(line.decode('utf-8','replace'))
                        out=BINARY_FIELD.sub(r'\1[ATTACHMENT_DATA_REDACTED]\3',text).encode()
                    spool.write(out)
                size=spool.tell();spool.seek(0)
                info=tarfile.TarInfo(rel);info.size=size;info.mtime=member.mtime
                trace.addfile(info,spool);return size,None
        target.parent.mkdir(parents=True,exist_ok=True)
        is_text=target.suffix.lower() in TEXT_EXT or target.name.lower() in ENV_NAMES|MAINT_NAMES or target.suffix.lower() in {'.log','.err','.out','.rst','.cu','.cpp','.c','.h','.hpp','.rs','.go','.lock','.cff'}
        if is_text:
            with target.open('wb') as dst:
                for line in source:
                    text=redact_text(line.decode('utf-8','replace'))
                    dst.write(BINARY_FIELD.sub(r'\1[ATTACHMENT_DATA_REDACTED]\3',text).encode())
        else:
            with target.open('wb') as dst:shutil.copyfileobj(source,dst,length=4*1024**2)
    size=target.stat().st_size;sha=digest(target)
    parts=split_file(target)
    return size, {'sha256':sha,'split':str(parts.name) if parts else None}


def sanitize_nested(archive, target):
    directory=target.with_name(target.name+'.contents');directory.mkdir(parents=True,exist_ok=True)
    if sum(p.endswith('.contents') for p in directory.parts)>8:raise ValueError('Nested archive depth exceeds eight')
    rows=[];total=0
    def member(reader, info):
        nonlocal total
        rel=str(safe_rel(info.name))
        if rel in {'.',''}:return
        reason=''
        if not info.isfile():reason='Non-regular archive entry'
        elif excluded(rel):reason='Dependency, cache, runtime account directory, or Git internals'
        elif rel.endswith(('.jsonl.lock','.json.lock','.log.lock')):reason='Runtime file lock'
        elif Path(rel).name.lower() in EXCLUDE_NAMES:reason='Credential/account file'
        if reason:
            rows.append(dict(member_path=rel,source_bytes=info.size,output_bytes=0,status=reason,sha256=''));return
        destination=directory/safe_rel(rel)
        size,details=sanitize_member(reader,info,destination);total+=size
        rows.append(dict(member_path=rel,source_bytes=info.size,output_bytes=size,status='Sanitized extracted copy',sha256=details['sha256']))
    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as z:
            class Reader:
                def extractfile(self,info):return z.open(info.name)
            for info in z.infolist():
                # ZIP symlinks are recorded but never followed.
                mode=(info.external_attr>>16)&0o170000
                m=SimpleNamespace(name=info.filename,size=info.file_size,isfile=lambda i=info,m=mode:not i.is_dir() and m!=0o120000)
                member(Reader(),m)
    elif tarfile.is_tarfile(archive):
        with tarfile.open(archive,'r|*') as t:
            for info in t:
                if not info.isdir():member(t,info)
    else:
        suffix=target.suffix.lower();opener={'.gz':gzip.open,'.bz2':bz2.open,'.xz':lzma.open}.get(suffix)
        if opener is None:raise ValueError('Unsupported or invalid nested archive: '+target.name)
        class Reader:
            def extractfile(self,info):return opener(archive,'rb')
        m=SimpleNamespace(name=target.stem,size=archive.stat().st_size,isfile=lambda:True)
        member(Reader(),m)
    write_csv(directory/'extraction-manifest.csv',['member_path','source_bytes','output_bytes','status','sha256'],rows)
    (directory/'README.md').write_text('# Sanitized archive contents\n\nThese files were extracted without executing code. Original archive members and exclusions are listed in [the manifest](extraction-manifest.csv). Source archive SHA-256: `'+digest(archive)+'`.\n')
    return total,{'sha256':digest(archive),'split':None,'storage':'sanitized-archive-contents'}


def paper_metadata(path, fallback):
    from pypdf import PdfReader
    try:
        reader=PdfReader(path);first=reader.pages[0].extract_text() or ''
        metadata_title=str((reader.metadata or {}).get('/Title','')).strip()
        if len(metadata_title)>10 and not metadata_title.lower().startswith(('untitled','main','template')): title=metadata_title
        else:
            lines=[re.sub(r'\s+',' ',x).strip() for x in first.splitlines() if x.strip()]
            lines=[re.sub(r'\s+\d{3}$','',x) for x in lines if not re.fullmatch(r'\d+',x) and not re.search(r'Anonymous (ACL submission|Author\(s\))',x)]
            selected=[]
            for line in lines:
                if re.search(r'^(Anonymous|Abstract|Under review|Submitted|Preprint|Published|[A-Z][a-z]+ [A-Z][a-z]+,)',line):break
                selected.append(line)
                if len(selected)>=3:break
            title=' '.join(selected)[:240] or fallback
        marker='Anonymous ACL submission' if 'Anonymous ACL submission' in first else 'Anonymous Author(s)' if 'Anonymous Author(s)' in first else ''
        return title,len(reader.pages),marker
    except Exception:return fallback,0,''


def criteria(info):
    def row(name,status,evidence,gap,path):return dict(name=name,status=status,evidence=evidence,gap=gap,path=path)
    n=info
    return [
     row('Manuscript and versions','Available' if n['paper_pdf'] else 'Partial',f"{n['tex_count']} source files; {n['version_count']} PDF candidates",'Candidate filenames do not establish official submission or publication.','01-manuscript/'),
     row('Academic status','Unverified',n['academic_record']['record'],'Official submission, acceptance, and publication were not independently checked.','07-maintenance/'),
     row('AI / human contribution','Partial',f"{n['contribution_count']} task/role records",'User and assistant roles do not identify people or establish author contributions.','02-contributions/'),
     row('Generation trace','Organized' if n['trace_count'] else 'Not found',f"{n['chat_count']} conversations; {n['worker_count']} worker logs/results; {n['trace_count']} source files",'Overlapping snapshots are retained; credentials and binary attachments are redacted.','05-generation-trace/'),
     row('Reproduction code','Available' if n['code_count'] else 'Not found',f"{n['code_count']} code/configuration files; {n['env_count']} environment manifests",'The code is archived; experiments were not rerun for this release.','03-code/'),
     row('Experiments and environment','Partial' if n['data_count'] else 'Not found',f"{n['data_count']} data/result files",'Original data permissions and completeness require project-specific review.','04-experiments/'),
     row('Validation evidence','Partial' if n['review_count']+n['validation_count'] else 'Not found',f"{n['review_count']} internal review records; {n['validation_count']} other audit records",'Internal reviews are project evidence, not independently verified external reviews.','06-validation/'),
     row('Maintenance','Partial' if n['maintenance_count'] else 'Not found',f"{n['maintenance_count']} project documentation files; {n['license_count']} license files",'A project license file applies only within its stated scope.','07-maintenance/'),
    ]


def finish(profile, archive_key, meta, archive_sha, repo):
    pdir=profile.pop('_dir');previous=profile.pop('_previous',{});profile.pop('_trace').close();rows=profile.pop('_rows');exclusions=profile.pop('_exclusions')
    papers=[r for r in rows if r['category']=='01-manuscript' and r['archive_path'].lower().endswith('.pdf')]
    candidates=sorted(papers,key=lambda r:(r['archive_path']!='docs/paper/main.pdf', not r['archive_path'].endswith('main.pdf'),'archive' in r['archive_path'],len(r['archive_path'])))
    profile['paper_pdf']=None;profile['paper_sha256']='';profile['title']=profile['project'].replace('_',' ').replace('-',' ');profile['pages']=0;profile['status_marker']=''
    if candidates:
        chosen=candidates[0];src=pdir/chosen['output_path']
        if src.exists() and src.read_bytes()[:5]==b'%PDF-':
            shutil.copyfile(src,pdir/'01-manuscript/paper.pdf')
            profile['paper_pdf']='paper.pdf';profile['paper_sha256']=digest(src)
            profile['title'],profile['pages'],profile['status_marker']=paper_metadata(src,profile['title'])
    profile.update(version_count=len(papers),version_paths=[r['archive_path'] for r in papers],archive_rel=archive_key,archive_note='Archive scan completed',archive_error=None,source_s3={'bucket':'agent-ml-research-project-backups-20260531','key':archive_key,'sha256':archive_sha,**meta})
    profile['academic_record']={'date':meta.get('modified','2026-10-19')[:10],'record':'Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified.'}
    if previous.get('paper_sha256')==profile.get('paper_sha256') and profile.get('paper_sha256'):
        profile['title']=previous.get('title',profile['title'])
        profile['academic_record']=previous.get('academic_record',profile['academic_record'])
    profile['criteria']=criteria(profile)
    fields=['category','archive_path','member_path','source_bytes','output_path','output_bytes','sha256','storage']
    write_csv(pdir/'08-index/asset-manifest.csv',fields,rows)
    write_csv(pdir/'08-index/excluded-files.csv',['member_path','source_bytes','reason'],exclusions)
    write_csv(pdir/'08-index/version-index.csv',['archive_path','source_bytes','output_path'],papers)
    trace_rows=[dict(source_archive=archive_key,member_path=r['archive_path'],source_bytes=r['source_bytes'],sanitized_bytes=r['output_bytes'],processing='Credentials and binary attachments redacted') for r in rows if r['category']=='05-generation-trace']
    write_csv(pdir/'05-generation-trace/trace-index.csv',['source_archive','member_path','source_bytes','sanitized_bytes','processing'],trace_rows)
    split_file(pdir/'05-generation-trace/trace-files.tar.gz')
    (pdir/'08-index/asset-manifest.json').write_text(json.dumps(profile,ensure_ascii=False,indent=2)+'\n')
    write_project_readme(pdir,profile)
    return profile


def write_project_readme(pdir, info):
    project=info['project'];s=info
    lines=[f"# {s['title']}",'',f'Project: `{project}`','', '[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project='+project+')','', '## Asset review matrix','', '| Requirement | Status | Included evidence | Verification limit |','|---|---|---|---|']
    for r in info['criteria']:lines.append('| '+' | '.join(str(r[k]).replace('|','\\|') for k in ('name','status','evidence','gap'))+' |')
    lines+=['','## What each directory contains','']
    lines += [f'- `{k}/`: {v}' for k,v in CATEGORIES.items()]
    lines+=['','## Source and scope','',f"Source: `s3://agent-ml-research-project-backups-20260531/{s['archive_rel']}`. Archive SHA-256 (derived archive for export snapshots): `{s['source_s3'].get('sha256') or s.get('derived_archive_sha256', 'not recorded')}`.",'',f"{s['code_count']:,} code/configuration files; {s['data_count']:,} data/result files; {s['trace_count']:,} trace sources. The selected manuscript has {s['pages']} pages; {s['version_count']} PDF candidates are indexed.",'','Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).','', 'Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.','']
    if not info['paper_pdf']:lines[4]=lines[4].replace('[Manuscript](01-manuscript/paper.pdf) · ','');lines+=['No manuscript PDF was found in this project snapshot.','']
    (pdir/'README.md').write_text('\n'.join(lines))


def collect(archive, repo, archive_key, metadata=None):
    global ROOT
    ROOT=repo
    fallback=archive_key.split('/')[0];profiles={};counts=Counter();meta=metadata or {}
    streamed=hasattr(archive,'read')
    sha=None if streamed else digest(archive)
    source=tarfile.open(fileobj=archive,mode='r|gz') if streamed else tarfile.open(archive,'r|gz')
    with ExitStack() as traces, source as tf:
        for member_number,member in enumerate(tf,1):
            if os.environ.get('RELEASE_DIAGNOSTICS')=='true' and (member_number%10000==0 or member.size>=32*1024**2):
                print(json.dumps({'stage':'archive-member','number':member_number,'path':member.name,'bytes':member.size}),flush=True)
            project,rel=project_path(member.name,fallback)
            if not project or not rel:continue
            if project.startswith(('.','_','idea_gen_')):continue
            if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*',project):raise ValueError('Unsafe project name')
            if project not in profiles:
                pdir=repo/'paper-assets'/project
                previous = json.loads((pdir/'08-index/asset-manifest.json').read_text()) if (pdir/'08-index/asset-manifest.json').exists() else {}
                if pdir.exists():shutil.rmtree(pdir)
                for cat in CATEGORIES:(pdir/cat).mkdir(parents=True,exist_ok=True)
                profiles[project]=dict(project=project,_previous=previous,_dir=pdir,_trace=traces.enter_context(tarfile.open(pdir/'05-generation-trace/trace-files.tar.gz','w:gz',compresslevel=4)),_rows=[],_exclusions=[],**{k:0 for k in ['code_count','data_count','env_count','tex_count','bib_count','review_count','validation_count','contribution_count','chat_count','worker_count','trace_count','trace_bytes','maintenance_count','provenance_count','submission_count','license_count']})
            p=profiles[project]
            reason=''
            if not member.isfile():
                if not member.isdir():reason='Non-regular archive entry'
                else:continue
            elif excluded(rel):reason='Dependency, cache, runtime account directory, or Git internals'
            elif rel.endswith(('.jsonl.lock','.json.lock','.log.lock')):reason='Runtime file lock'
            elif Path(rel).suffix.lower()=='.7z':reason='Unsupported nested archive format; original retained in S3'
            elif Path(rel).name.lower() in EXCLUDE_NAMES or re.search(r'(?:^|/)(?:id_rsa|id_ed25519|.*credentials.*|.*accounts.*)(?:\.[^/]*)?$',rel,re.I):reason='Account or credential file'
            if reason:
                p['_exclusions'].append(dict(member_path=member.name,source_bytes=member.size,reason=reason));continue
            category=classify_asset(rel);path=Path(rel)
            if category=='05-generation-trace':
                size,_=sanitize_member(tf,member,None,trace=p['_trace'],rel=rel);out='05-generation-trace/trace-files.tar.gz';details=None
                p['trace_count']+=1;p['trace_bytes']+=size;p['chat_count']+=int(rel.startswith('logs/chats/'));p['worker_count']+=int(rel.startswith('logs/workers/'))
            else:
                target=p['_dir']/category/'source'/safe_rel(rel)
                if target.exists():
                    # Retain repeated tar paths rather than silently overwriting evidence.
                    n=2
                    while target.with_name(target.stem+f'-archive-copy-{n}'+target.suffix).exists():n+=1
                    target=target.with_name(target.stem+f'-archive-copy-{n}'+target.suffix)
                size,details=sanitize_member(tf,member,target);out=str(target.relative_to(p['_dir']))+(('.contents') if details and details.get('storage')=='sanitized-archive-contents' else '')
                if category=='03-code':p['code_count']+=1;p['env_count']+=int(path.name.lower() in ENV_NAMES)
                if category=='04-experiments':p['data_count']+=1
                if category=='01-manuscript':p['tex_count']+=int(path.suffix.lower() in {'.tex','.bib','.bst','.sty','.cls'});p['bib_count']+=int(path.suffix.lower()=='.bib')
                if category=='02-contributions':p['contribution_count']+=1
                if category=='06-validation':p['review_count']+=int(is_review(rel));p['validation_count']+=int(not is_review(rel))
                if category=='07-maintenance':p['maintenance_count']+=1;p['license_count']+=int(path.name.lower().startswith('license'));p['provenance_count']+=int('provenance' in path.name.lower())
            p['_rows'].append(dict(category=category,archive_path=rel,member_path=member.name,source_bytes=member.size,output_path=out,output_bytes=size,sha256=details['sha256'] if details else '',storage=details['storage'] if details and details.get('storage') else 'split-parts' if details and details['split'] else 'sanitized-trace-archive' if category=='05-generation-trace' else 'file'))
            counts[project]+=1
            if sum(counts.values())%1000==0:print(json.dumps({'archive':archive_key,'collected_files':sum(counts.values()),'projects':list(profiles),'free_GiB':round(shutil.disk_usage(repo).free/1024**3,1)}),flush=True)
    if streamed:
        sha=archive.finish()
    result=[]
    for p in profiles.values():result.append(finish(p,archive_key,meta,sha,repo))
    return {'archive_sha256':sha,'projects':result,'collected_files':dict(counts)}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('archive',type=Path);parser.add_argument('--repo',type=Path,default=ROOT);parser.add_argument('--source-key',required=True);parser.add_argument('--source-metadata-json',type=Path);parser.add_argument('--result-json',type=Path)
    args=parser.parse_args();metadata=json.loads(args.source_metadata_json.read_text()) if args.source_metadata_json else {}
    result=collect(args.archive,args.repo,args.source_key,metadata)
    if args.result_json:args.result_json.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    else:print(json.dumps(result,indent=2))
