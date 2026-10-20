# Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis

Project: `vla-ssd`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=vla-ssd)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 50 source files; 123 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 326 conversations; 1435 worker logs/results; 1850 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 348 code/configuration files; 0 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 1167 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 15 internal review records; 32 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 122 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/vla-ssd/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `7c757731851c40b826c3f916398e85264e0c9607e98c333d313548f9fb61a575`.

348 code/configuration files; 1,167 data/result files; 1,850 trace sources. The selected manuscript has 39 pages; 123 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [paper_main.pdf](01-manuscript/source/paper_main.pdf) · [paper/main.tex](01-manuscript/source/paper/main.tex) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [scripts/plot_teaser.py](03-code/source/scripts/plot_teaser.py) · [scripts/plot_overview.py](03-code/source/scripts/plot_overview.py) · [scripts/plot_r2_collapse.py](03-code/source/scripts/plot_r2_collapse.py) |
| Experiment and supporting data | [artifacts/kendall_w_cross_task.json](04-experiments/source/artifacts/kendall_w_cross_task.json) · [artifacts/bootstrap_task_ratio.json](04-experiments/source/artifacts/bootstrap_task_ratio.json) · [artifacts/trained_action_head_r2.json](04-experiments/source/artifacts/trained_action_head_r2.json) |
| Internal validation records | [_last_visual_review.json](06-validation/source/_last_visual_review.json) · [_paper_audit_result.json](06-validation/source/_paper_audit_result.json) · [artifacts/audit_figures.md](06-validation/source/artifacts/audit_figures.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [memory.md](07-maintenance/source/memory.md) · [report.md](07-maintenance/source/report.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 235 runtime bookkeeping files and 2 automated scan reports. These record the system workflow alongside the experiment assets.
