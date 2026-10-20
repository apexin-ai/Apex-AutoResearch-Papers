# distill kv rag cache

Project: `distill_kv_rag_cache`

[Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=distill_kv_rag_cache)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Partial | 0 source files; 0 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 1 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 9 conversations; 56 worker logs/results; 65 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 48 code/configuration files; 1 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 13 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Not found | 0 internal review records; 0 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 13 project documentation files; 0 license files | A project license file applies only within its stated scope. |

## What each directory contains

- `01-manuscript/`: Manuscript PDF, source, references, figures, and version candidates.
- `02-contributions/`: Recorded agent roles and task instructions.
- `03-code/`: Research code, scripts, configurations, and dependency manifests.
- `04-experiments/`: Data, experiment outputs, metrics, and supporting artifacts.
- `05-generation-trace/`: Readable Markdown conversations, complete normalized JSON, and sanitized source logs.
- `06-validation/`: Internal reviews, audits, and verification records.
- `07-maintenance/`: Project documentation, roadmaps, provenance, and maintenance notes.
- `08-index/`: File manifests, original paths, exclusions, and source checksums.

## Source and scope

Source: `s3://agent-ml-research-project-backups-20260531/recursive_gen_depth_est/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `46ff9255389bd71b05a36880fa4485856313b10a42d3f491c5d4bef75902d99e`.

48 code/configuration files; 13 data/result files; 65 trace sources. The selected manuscript has 0 pages; 0 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

No manuscript PDF was found in this project snapshot.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | No matching files in this snapshot |
| Contribution records | [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [artifacts/_project/data/__init__.py](03-code/source/artifacts/_project/data/__init__.py) · [artifacts/_project/intermediate/metrics.py](03-code/source/artifacts/_project/intermediate/metrics.py) · [artifacts/compresslink_code/tests/__init__.py](03-code/source/artifacts/compresslink_code/tests/__init__.py) |
| Experiment and supporting data | [checkpoints/mvp_hotpot_gpu0_DONE_20260514T074718.json](04-experiments/source/checkpoints/mvp_hotpot_gpu0_DONE_20260514T074718.json) · [checkpoints/mvp_hotpot_gpu1_DONE_20260514T074718.json](04-experiments/source/checkpoints/mvp_hotpot_gpu1_DONE_20260514T074718.json) · [checkpoints/mvp_hotpot_gpu0_QUEUED_20260514T074509.json](04-experiments/source/checkpoints/mvp_hotpot_gpu0_QUEUED_20260514T074509.json) |
| Internal validation records | No matching files in this snapshot |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [artifacts/compresslink_code/README.md](07-maintenance/source/artifacts/compresslink_code/README.md) · [memory.md](07-maintenance/source/memory.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 9 runtime bookkeeping files and 0 automated scan reports. These record the system workflow alongside the experiment assets.
