# svs formal verification

Project: `svs_formal_verification`

[Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=svs_formal_verification)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Partial | 0 source files; 0 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 32 conversations; 172 worker logs/results; 205 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 68 code/configuration files; 0 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 28 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 0 internal review records; 1 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 15 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/gen-depth-fingerprint/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `1273cf80a9751a0250aeea77fa12eaa84da288bf6d80fb04d6fa73f3da32ef2d`.

68 code/configuration files; 28 data/result files; 205 trace sources. The selected manuscript has 0 pages; 0 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

No manuscript PDF was found in this project snapshot.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | No matching files in this snapshot |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [artifacts/mvp_diagnostic.py](03-code/source/artifacts/mvp_diagnostic.py) · [artifacts/svs_pipeline/types.py](03-code/source/artifacts/svs_pipeline/types.py) · [artifacts/svs_pipeline/config.py](03-code/source/artifacts/svs_pipeline/config.py) |
| Experiment and supporting data | [artifacts/cross_model_dry_run.json](04-experiments/source/artifacts/cross_model_dry_run.json) · [artifacts/_project/data/cross_model_dry_run.json](04-experiments/source/artifacts/_project/data/cross_model_dry_run.json) · [checkpoints/mvp_001_DONE_20260514T084933.json](04-experiments/source/checkpoints/mvp_001_DONE_20260514T084933.json) |
| Internal validation records | [artifacts/literature_survey_formal_verification.md](06-validation/source/artifacts/literature_survey_formal_verification.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [memory.md](07-maintenance/source/memory.md) · [report.md](07-maintenance/source/report.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 29 runtime bookkeeping files and 0 automated scan reports. These record the system workflow alongside the experiment assets.
