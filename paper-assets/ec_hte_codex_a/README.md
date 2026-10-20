# ec hte codex a

Project: `ec_hte_codex_a`

[Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=ec_hte_codex_a)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Partial | 0 source files; 0 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 0 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 4 conversations; 26 worker logs/results; 30 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 25 code/configuration files; 0 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 40 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 0 internal review records; 2 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 22 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/turn_residual_gating/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `6ff497f2a6f9a171f3ace9ef6a18ee9af5ed3ea68e042dc484c7f76cb82d95f5`.

25 code/configuration files; 40 data/result files; 30 trace sources. The selected manuscript has 0 pages; 0 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

No manuscript PDF was found in this project snapshot.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | No matching files in this snapshot |
| Contribution records | No matching files in this snapshot |
| Research code and configurations | [repro/exp_001_bias_bound_mvp/__init__.py](03-code/source/repro/exp_001_bias_bound_mvp/__init__.py) · [repro/exp_002_gpu_dgp_grid/run_gpu_dgp_grid.py](03-code/source/repro/exp_002_gpu_dgp_grid/run_gpu_dgp_grid.py) · [repro/exp_001_bias_bound_mvp/run_experiment.py](03-code/source/repro/exp_001_bias_bound_mvp/run_experiment.py) |
| Experiment and supporting data | [artifacts/exp_002_gpu_dgp_grid/formal/summary.json](04-experiments/source/artifacts/exp_002_gpu_dgp_grid/formal/summary.json) · [artifacts/exp_001_bias_bound_mvp/quick/metrics.csv](04-experiments/source/artifacts/exp_001_bias_bound_mvp/quick/metrics.csv) · [artifacts/exp_001_bias_bound_mvp/data/summary.json](04-experiments/source/artifacts/exp_001_bias_bound_mvp/data/summary.json) |
| Internal validation records | [artifacts/analysis/exp002_negative_mechanism_audit_20260531.md](06-validation/source/artifacts/analysis/exp002_negative_mechanism_audit_20260531.md) · [artifacts/_project/report/exp002_negative_mechanism_audit_20260531.md](06-validation/source/artifacts/_project/report/exp002_negative_mechanism_audit_20260531.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [repro/exp_002_gpu_dgp_grid/README.md](07-maintenance/source/repro/exp_002_gpu_dgp_grid/README.md) · [ideas.md](07-maintenance/source/ideas.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 5 runtime bookkeeping files and 0 automated scan reports. These record the system workflow alongside the experiment assets.
