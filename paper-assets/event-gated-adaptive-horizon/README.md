# Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3

Project: `event-gated-adaptive-horizon`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=event-gated-adaptive-horizon)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 58 source files; 45 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 666 conversations; 2210 worker logs/results; 3085 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 649 code/configuration files; 1 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 1727 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 6 internal review records; 41 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 383 project documentation files; 1 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/event-gated-adaptive-horizon/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `58461bd0e80239ced93e13b727a697210b6b0dda0ab567897ffb040ae545b17e`.

649 code/configuration files; 1,727 data/result files; 3,085 trace sources. The selected manuscript has 46 pages; 45 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [docs/paper/main.tex](01-manuscript/source/docs/paper/main.tex) · [docs/paper/main.pdf](01-manuscript/source/docs/paper/main.pdf) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [scripts/plot_018_results.py](03-code/source/scripts/plot_018_results.py) · [scripts/eval_nve_maniskill.py](03-code/source/scripts/eval_nve_maniskill.py) · [scripts/analyze_018_full_sgs.py](03-code/source/scripts/analyze_018_full_sgs.py) |
| Experiment and supporting data | [artifacts/bootstrap_cis.json](04-experiments/source/artifacts/bootstrap_cis.json) · [artifacts/bootstrap_ci_n3.json](04-experiments/source/artifacts/bootstrap_ci_n3.json) · [artifacts/value_vs_returns.json](04-experiments/source/artifacts/value_vs_returns.json) |
| Internal validation records | [_last_visual_review.json](06-validation/source/_last_visual_review.json) · [_paper_audit_result.json](06-validation/source/_paper_audit_result.json) · [paper/framing_b_reaudit.md](06-validation/source/paper/framing_b_reaudit.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [artifacts/supplementary/LICENSE](07-maintenance/source/artifacts/supplementary/LICENSE) · [artifacts/figures/paper/README.md](07-maintenance/source/artifacts/figures/paper/README.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 455 runtime bookkeeping files and 2 automated scan reports. These record the system workflow alongside the experiment assets.
