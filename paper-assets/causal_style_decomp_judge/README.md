# The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation

Project: `causal_style_decomp_judge`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=causal_style_decomp_judge)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 34 source files; 38 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | The ROADMAP records that the OpenReview submission was completed manually by operations and the project is awaiting review. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 69 conversations; 432 worker logs/results; 506 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 171 code/configuration files; 1 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 488 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 18 internal review records; 28 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 57 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/causal_style_decomp_judge/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `a6cba92e3bc3effbf4567563f441561bbc64e34a2c984588a832d5d3c22dcc20`.

171 code/configuration files; 488 data/result files; 506 trace sources. The selected manuscript has 20 pages; 38 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [docs/paper/main.tex](01-manuscript/source/docs/paper/main.tex) · [docs/paper/main.pdf](01-manuscript/source/docs/paper/main.pdf) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [artifacts/run_mvp.sh](03-code/source/artifacts/run_mvp.sh) · [artifacts/gpt4o_analysis.py](03-code/source/artifacts/gpt4o_analysis.py) · [csd_pipeline/verbosity_gee.py](03-code/source/csd_pipeline/verbosity_gee.py) |
| Experiment and supporting data | [data/policy-1.csv](04-experiments/source/data/policy-1.csv) · [data/policy-2.csv](04-experiments/source/data/policy-2.csv) · [data/annotation_sheet_1.csv](04-experiments/source/data/annotation_sheet_1.csv) |
| Internal validation records | [_last_visual_review.json](06-validation/source/_last_visual_review.json) · [_paper_audit_result.json](06-validation/source/_paper_audit_result.json) · [artifacts/audit_anon_repo.md](06-validation/source/artifacts/audit_anon_repo.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [memory.md](07-maintenance/source/memory.md) · [report.md](07-maintenance/source/report.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 62 runtime bookkeeping files and 4 automated scan reports. These record the system workflow alongside the experiment assets.
