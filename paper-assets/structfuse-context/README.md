# StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval

Project: `structfuse-context`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=structfuse-context)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 27 source files; 12 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 183 conversations; 1006 worker logs/results; 1232 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 212 code/configuration files; 2 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 354 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 0 internal review records; 2 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 113 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/contrastive_trace_safety/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `88c6d1a02d1e80773bcb185855f164326f017b04337a2bc48310182a4a6804e8`.

212 code/configuration files; 354 data/result files; 1,232 trace sources. The selected manuscript has 8 pages; 12 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [artifacts/paper_drafts/references.bib](01-manuscript/source/artifacts/paper_drafts/references.bib) · [artifacts/_project/paper/discussion.tex](01-manuscript/source/artifacts/_project/paper/discussion.tex) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [eval_repobench.py](03-code/source/eval_repobench.py) · [artifacts/patch_train.py](03-code/source/artifacts/patch_train.py) · [artifacts/patch_build_m1.py](03-code/source/artifacts/patch_build_m1.py) |
| Experiment and supporting data | [artifacts/plan006_error_patterns.json](04-experiments/source/artifacts/plan006_error_patterns.json) · [artifacts/bm25_overlap_stratified.json](04-experiments/source/artifacts/bm25_overlap_stratified.json) · [artifacts/plan_006/scalability_data.json](04-experiments/source/artifacts/plan_006/scalability_data.json) |
| Internal validation records | [artifacts/_project/report/citation_verification.md](06-validation/source/artifacts/_project/report/citation_verification.md) · [artifacts/paper_drafts/v2/citation_verification.md](06-validation/source/artifacts/paper_drafts/v2/citation_verification.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [memory.md](07-maintenance/source/memory.md) · [report.md](07-maintenance/source/report.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 138 runtime bookkeeping files and 0 automated scan reports. These record the system workflow alongside the experiment assets.
