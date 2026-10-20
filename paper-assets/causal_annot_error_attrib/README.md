# Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction

Project: `causal_annot_error_attrib`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=causal_annot_error_attrib)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 51 source files; 46 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 2 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 78 conversations; 388 worker logs/results; 475 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 212 code/configuration files; 0 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 303 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 23 internal review records; 5 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 27 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/causal_annot_error_attrib/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `79c194cf0f980db206fbabd462b3d915ccd684d9d8b1fda6dd5ab87126e021be`.

212 code/configuration files; 303 data/result files; 475 trace sources. The selected manuscript has 33 pages; 46 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [paper/main.tex](01-manuscript/source/paper/main.tex) · [paper/main.pdf](01-manuscript/source/paper/main.pdf) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [patch_metrics.py](03-code/source/patch_metrics.py) · [artifacts/annotate.py](03-code/source/artifacts/annotate.py) · [artifacts/e2e_demo.py](03-code/source/artifacts/e2e_demo.py) |
| Experiment and supporting data | [artifacts/plan011_new_cms.json](04-experiments/source/artifacts/plan011_new_cms.json) · [artifacts/e2e_demo_results.json](04-experiments/source/artifacts/e2e_demo_results.json) · [artifacts/delta_max_results.json](04-experiments/source/artifacts/delta_max_results.json) |
| Internal validation records | [_last_visual_review.json](06-validation/source/_last_visual_review.json) · [_paper_audit_result.json](06-validation/source/_paper_audit_result.json) · [docs/_last_visual_review.json](06-validation/source/docs/_last_visual_review.json) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [memory.md](07-maintenance/source/memory.md) · [report.md](07-maintenance/source/report.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 68 runtime bookkeeping files and 2 automated scan reports. These record the system workflow alongside the experiment assets.
