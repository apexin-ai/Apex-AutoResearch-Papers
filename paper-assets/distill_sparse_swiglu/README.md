# Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

Project: `distill_sparse_swiglu`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=distill_sparse_swiglu)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 29 source files; 31 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 5 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 582 conversations; 1939 worker logs/results; 2646 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 1783 code/configuration files; 6 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 2536 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 27 internal review records; 10 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 123 project documentation files; 5 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/distill_sparse_swiglu/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `f7eac3c6a537353e5fe458403f004301cd51028817ebce7e8c122f113a9aa61a`.

1,783 code/configuration files; 2,536 data/result files; 2,646 trace sources. The selected manuscript has 18 pages; 31 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [paper/main.tex](01-manuscript/source/paper/main.tex) · [paper/main.pdf](01-manuscript/source/paper/main.pdf) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [src/compute_jaccard.py](03-code/source/src/compute_jaccard.py) · [src/train_perlayer_kl.py](03-code/source/src/train_perlayer_kl.py) · [src/train_bce_kl_targets.py](03-code/source/src/train_bce_kl_targets.py) |
| Experiment and supporting data | [results/wallclock_profile.json](04-experiments/source/results/wallclock_profile.json) · [artifacts/50pct_3seed_summary.csv](04-experiments/source/artifacts/50pct_3seed_summary.csv) · [artifacts/snr_extended_results.json](04-experiments/source/artifacts/snr_extended_results.json) |
| Internal validation records | [_last_visual_review.json](06-validation/source/_last_visual_review.json) · [_paper_audit_result.json](06-validation/source/_paper_audit_result.json) · [artifacts/data_audit_report.md](06-validation/source/artifacts/data_audit_report.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [flashinfer/LICENSE](07-maintenance/source/flashinfer/LICENSE) · [R-Sparse/README.md](07-maintenance/source/R-Sparse/README.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 454 runtime bookkeeping files and 2 automated scan reports. These record the system workflow alongside the experiment assets.
