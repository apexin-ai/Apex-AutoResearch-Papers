# Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models

Project: `phase-gated-compound-sparse`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=phase-gated-compound-sparse)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 37 source files; 31 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 591 conversations; 1411 worker logs/results; 2272 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 413 code/configuration files; 0 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 1167 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 8 internal review records; 36 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 195 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

413 code/configuration files; 1,167 data/result files; 2,272 trace sources. The selected manuscript has 28 pages; 31 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [artifacts/_project/paper/main.tex](01-manuscript/source/artifacts/_project/paper/main.tex) · [artifacts/_project/paper/main.pdf](01-manuscript/source/artifacts/_project/paper/main.pdf) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [run_accuracy_eval.py](03-code/source/run_accuracy_eval.py) · [run_profiling_gsm8k.py](03-code/source/run_profiling_gsm8k.py) · [artifacts/plot_figure1.py](03-code/source/artifacts/plot_figure1.py) |
| Experiment and supporting data | [artifacts/crossover_n500.csv](04-experiments/source/artifacts/crossover_n500.csv) · [artifacts/c3_llama_results.json](04-experiments/source/artifacts/c3_llama_results.json) · [artifacts/c2_progress_snapshot.json](04-experiments/source/artifacts/c2_progress_snapshot.json) |
| Internal validation records | [artifacts/reference_audit.md](06-validation/source/artifacts/reference_audit.md) · [artifacts/w1w5_audit_report.md](06-validation/source/artifacts/w1w5_audit_report.md) · [artifacts/reference_audit_report.md](06-validation/source/artifacts/reference_audit_report.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [memory.md](07-maintenance/source/memory.md) · [report.md](07-maintenance/source/report.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 319 runtime bookkeeping files and 0 automated scan reports. These record the system workflow alongside the experiment assets.
