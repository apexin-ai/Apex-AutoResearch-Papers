# Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models

Project: `irt_equated_bench_regen`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=irt_equated_bench_regen)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 15 source files; 5 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 58 conversations; 318 worker logs/results; 380 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 92 code/configuration files; 0 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 348 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 0 internal review records; 8 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 10 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/irt_equated_bench_regen/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `3988eb03eba17e04ba3d402d47fb1bb7e59698e4000943f709bb43683a5a91fc`.

92 code/configuration files; 348 data/result files; 380 trace sources. The selected manuscript has 16 pages; 5 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [paper/main.tex](01-manuscript/source/paper/main.tex) · [paper/main.pdf](01-manuscript/source/paper/main.pdf) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [figures/paper/fig_2_dose_response.py](03-code/source/figures/paper/fig_2_dose_response.py) · [figures/paper/fig_A3_rho_degradation.py](03-code/source/figures/paper/fig_A3_rho_degradation.py) · [artifacts/plan_001b/data/plan_001b_analysis.py](03-code/source/artifacts/plan_001b/data/plan_001b_analysis.py) |
| Experiment and supporting data | [artifacts/response_matrix.npz](04-experiments/source/artifacts/response_matrix.npz) · [artifacts/_project/data/target.csv](04-experiments/source/artifacts/_project/data/target.csv) · [artifacts/response_matrix_index.npz](04-experiments/source/artifacts/response_matrix_index.npz) |
| Internal validation records | [_last_visual_review.json](06-validation/source/_last_visual_review.json) · [_paper_audit_result.json](06-validation/source/_paper_audit_result.json) · [checkpoints/plan_011_semi_synthetic_validation_DONE_20260520T215454.json](06-validation/source/checkpoints/plan_011_semi_synthetic_validation_DONE_20260520T215454.json) |
| Project documentation | [AGENTS.md](07-maintenance/source/AGENTS.md) · [paper_framing.md](07-maintenance/source/paper_framing.md) · [distilled-writing.skill.md](07-maintenance/source/distilled-writing.skill.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 52 runtime bookkeeping files and 3 automated scan reports. These record the system workflow alongside the experiment assets.
