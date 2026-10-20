# Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families

Project: `contamcal-irt-calibration`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=contamcal-irt-calibration)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 62 source files; 55 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 1010 conversations; 3731 worker logs/results; 5003 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 958 code/configuration files; 2 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 2747 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 12 internal review records; 27 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 225 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/contamcal-irt-calibration/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `01d1ed51e11849cb695cf653cb78f6d45d375aa06fb1b2957b6be616d1ea3f65`.

958 code/configuration files; 2,747 data/result files; 5,003 trace sources. The selected manuscript has 21 pages; 55 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [docs/paper/main.tex](01-manuscript/source/docs/paper/main.tex) · [docs/paper/main.pdf](01-manuscript/source/docs/paper/main.pdf) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [scripts/run_gsm8k_eval_s42.sh](03-code/source/scripts/run_gsm8k_eval_s42.sh) · [exp002/utils.py](03-code/source/exp002/utils.py) · [fit_irt_2pl_gamma.py](03-code/source/fit_irt_2pl_gamma.py) |
| Experiment and supporting data | [artifacts/eval_summary_matrix.csv](04-experiments/source/artifacts/eval_summary_matrix.csv) · [artifacts/exp008_auc_heatmap.json](04-experiments/source/artifacts/exp008_auc_heatmap.json) · [artifacts/irt_calibration_data.json](04-experiments/source/artifacts/irt_calibration_data.json) |
| Internal validation records | [_last_visual_review.json](06-validation/source/_last_visual_review.json) · [_paper_audit_result.json](06-validation/source/_paper_audit_result.json) · [docs/_last_visual_review.json](06-validation/source/docs/_last_visual_review.json) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [exp002/README.md](07-maintenance/source/exp002/README.md) · [ideas.md](07-maintenance/source/ideas.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 746 runtime bookkeeping files and 2 automated scan reports. These record the system workflow alongside the experiment assets.
