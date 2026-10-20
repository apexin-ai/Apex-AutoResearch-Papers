# When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic

Project: `ratekv`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=ratekv)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 25 source files; 18 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | The ROADMAP records that the project is in an additional-experiment sprint targeting EMNLP 2026 Main via ARR; no formal paper submission is recorded. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 260 conversations; 932 worker logs/results; 1250 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 308 code/configuration files; 0 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 874 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 2 internal review records; 6 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 33 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

308 code/configuration files; 874 data/result files; 1,250 trace sources. The selected manuscript has 15 pages; 18 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [docs/paper/main.tex](01-manuscript/source/docs/paper/main.tex) · [docs/paper/main.pdf](01-manuscript/source/docs/paper/main.pdf) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [run_k_ablation.py](03-code/source/run_k_ablation.py) · [run_kv_separation.py](03-code/source/run_kv_separation.py) · [run_kivi_baseline.py](03-code/source/run_kivi_baseline.py) |
| Experiment and supporting data | [artifacts/shape_metrics.json](04-experiments/source/artifacts/shape_metrics.json) · [artifacts/compounding_curves_data.json](04-experiments/source/artifacts/compounding_curves_data.json) · [artifacts/w3_downstream_yi_results.json](04-experiments/source/artifacts/w3_downstream_yi_results.json) |
| Internal validation records | [artifacts/paper_data_audit.md](06-validation/source/artifacts/paper_data_audit.md) · [artifacts/paper_patch_audit.md](06-validation/source/artifacts/paper_patch_audit.md) · [artifacts/reference_audit_report.md](06-validation/source/artifacts/reference_audit_report.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [memory.md](07-maintenance/source/memory.md) · [report.md](07-maintenance/source/report.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 200 runtime bookkeeping files and 0 automated scan reports. These record the system workflow alongside the experiment assets.
