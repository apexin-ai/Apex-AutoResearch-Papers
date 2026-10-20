# Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models

Project: `nlp_variance_gtheory`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=nlp_variance_gtheory)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 56 source files; 62 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 128 conversations; 678 worker logs/results; 815 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 396 code/configuration files; 4 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 519 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 11 internal review records; 13 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 77 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/nlp_variance_gtheory/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `fe75a74ae7b52053f7e5dd63ed07e07aad0f922691aa4cca0c2e8787bca06b81`.

396 code/configuration files; 519 data/result files; 815 trace sources. The selected manuscript has 15 pages; 62 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [docs/paper/main.tex](01-manuscript/source/docs/paper/main.tex) · [docs/paper/main.pdf](01-manuscript/source/docs/paper/main.pdf) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [scripts/lomo_8x5.py](03-code/source/scripts/lomo_8x5.py) · [scripts/gstudy_full.py](03-code/source/scripts/gstudy_full.py) · [scripts/sample_benchmarks.py](03-code/source/scripts/sample_benchmarks.py) |
| Experiment and supporting data | [artifacts/bootstrap_c2_ci.json](04-experiments/source/artifacts/bootstrap_c2_ci.json) · [artifacts/exp004/data/dstudy_arc.json](04-experiments/source/artifacts/exp004/data/dstudy_arc.json) · [artifacts/exp004/data/dstudy_math.json](04-experiments/source/artifacts/exp004/data/dstudy_math.json) |
| Internal validation records | [_last_visual_review.json](06-validation/source/_last_visual_review.json) · [_paper_audit_result.json](06-validation/source/_paper_audit_result.json) · [artifacts/verification_report.md](06-validation/source/artifacts/verification_report.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [artifacts/code/README.md](07-maintenance/source/artifacts/code/README.md) · [artifacts/_project/intermediate/README.md](07-maintenance/source/artifacts/_project/intermediate/README.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 117 runtime bookkeeping files and 2 automated scan reports. These record the system workflow alongside the experiment assets.
