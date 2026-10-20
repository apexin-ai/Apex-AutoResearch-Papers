# Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation

Project: `demo_calibrated_sim`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=demo_calibrated_sim)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 6 source files; 6 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 37 conversations; 160 worker logs/results; 203 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 161 code/configuration files; 0 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 167 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 0 internal review records; 2 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 36 project documentation files; 1 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/entrainment_gated_ft/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `6c9d78da9ac8f06b5b71dd682841aa662127685bd00477d310d927c818bf9418`.

161 code/configuration files; 167 data/result files; 203 trace sources. The selected manuscript has 9 pages; 6 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [artifacts/dream_reports/dream_20260513T163256/best/paper.tex](01-manuscript/source/artifacts/dream_reports/dream_20260513T163256/best/paper.tex) · [artifacts/dream_reports/dream_20260513T163256/best/paper.pdf](01-manuscript/source/artifacts/dream_reports/dream_20260513T163256/best/paper.pdf) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [artifacts/tau-bench/run.py](03-code/source/artifacts/tau-bench/run.py) · [artifacts/code/train_dpo.py](03-code/source/artifacts/code/train_dpo.py) · [artifacts/tau-bench/setup.py](03-code/source/artifacts/tau-bench/setup.py) |
| Experiment and supporting data | [artifacts/tau-bench/tau_bench/envs/retail/data/users.json](04-experiments/source/artifacts/tau-bench/tau_bench/envs/retail/data/users.json) · [artifacts/tau-bench/tau_bench/envs/retail/data/orders.json](04-experiments/source/artifacts/tau-bench/tau_bench/envs/retail/data/orders.json) · [artifacts/tau-bench/tau_bench/envs/airline/data/users.json](04-experiments/source/artifacts/tau-bench/tau_bench/envs/airline/data/users.json) |
| Internal validation records | [artifacts/reference_audit_report.md](06-validation/source/artifacts/reference_audit_report.md) · [artifacts/_project/report/reference_audit_report.md](06-validation/source/artifacts/_project/report/reference_audit_report.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [artifacts/tau-bench/LICENSE](07-maintenance/source/artifacts/tau-bench/LICENSE) · [artifacts/tau-bench/README.md](07-maintenance/source/artifacts/tau-bench/README.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 29 runtime bookkeeping files and 0 automated scan reports. These record the system workflow alongside the experiment assets.
