# Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR

Project: `xling_calib_direction`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=xling_calib_direction)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 31 source files; 15 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 2 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 48 conversations; 242 worker logs/results; 290 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 121 code/configuration files; 0 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 201 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 1 internal review records; 1 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 48 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/cert_manip_resist_eval/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `3741f54c54a9849bc40ea9499ea2849bfd86df5f744a3e76a2601ea970a830c4`.

121 code/configuration files; 201 data/result files; 290 trace sources. The selected manuscript has 11 pages; 15 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [artifacts/dream_reports/dream_20260520T201854/best/references.bib](01-manuscript/source/artifacts/dream_reports/dream_20260520T201854/best/references.bib) · [artifacts/dream_reports/dream_20260521T122458/best/references.bib](01-manuscript/source/artifacts/dream_reports/dream_20260521T122458/best/references.bib) |
| Contribution records | [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [code/train_caclr.py](03-code/source/code/train_caclr.py) · [code/train_probe.py](03-code/source/code/train_probe.py) · [code/compute_cka.py](03-code/source/code/compute_cka.py) |
| Experiment and supporting data | [artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json](04-experiments/source/artifacts/dream_reports/dream_20260520T185641/best/experiment_data.json) · [artifacts/dream_reports/dream_20260520T201854/best/experiment_data.json](04-experiments/source/artifacts/dream_reports/dream_20260520T201854/best/experiment_data.json) · [artifacts/dream_reports/dream_20260521T122458/best/experiment_data.json](04-experiments/source/artifacts/dream_reports/dream_20260521T122458/best/experiment_data.json) |
| Internal validation records | [_last_visual_review.json](06-validation/source/_last_visual_review.json) · [artifacts/review_reports/round_0.md](06-validation/source/artifacts/review_reports/round_0.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [memory.md](07-maintenance/source/memory.md) · [report.md](07-maintenance/source/report.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 47 runtime bookkeeping files and 0 automated scan reports. These record the system workflow alongside the experiment assets.
