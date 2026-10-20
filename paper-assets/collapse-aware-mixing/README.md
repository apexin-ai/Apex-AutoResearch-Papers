# collapse aware mixing

Project: `collapse-aware-mixing`

[Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=collapse-aware-mixing)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Partial | 0 source files; 0 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 54 conversations; 158 worker logs/results; 232 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 84 code/configuration files; 1 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 58 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 0 internal review records; 6 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 19 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/schema-dag-extraction/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `bb19a28e6f8501fcbe2320aeef4aa932ec06eccfcf2917ebeef449b2ad144799`.

84 code/configuration files; 58 data/result files; 232 trace sources. The selected manuscript has 0 pages; 0 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

No manuscript PDF was found in this project snapshot.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | No matching files in this snapshot |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [analyze_seed0_vs_v7.py](03-code/source/analyze_seed0_vs_v7.py) · [artifacts/code/train.py](03-code/source/artifacts/code/train.py) · [artifacts/code/config.py](03-code/source/artifacts/code/config.py) |
| Experiment and supporting data | [checkpoints/mvp_pilot_DONE_20260512T112136.json](04-experiments/source/checkpoints/mvp_pilot_DONE_20260512T112136.json) · [checkpoints/mvp_pilot_QUEUED_20260512T103215.json](04-experiments/source/checkpoints/mvp_pilot_QUEUED_20260512T103215.json) · [checkpoints/mvp_pilot_RUNNING_20260512T105712.json](04-experiments/source/checkpoints/mvp_pilot_RUNNING_20260512T105712.json) |
| Internal validation records | [checkpoints/pivot_b_verification_DONE_20260513T202046.json](06-validation/source/checkpoints/pivot_b_verification_DONE_20260513T202046.json) · [checkpoints/pivot_b_verification_QUEUED_20260513T184849.json](06-validation/source/checkpoints/pivot_b_verification_QUEUED_20260513T184849.json) · [checkpoints/pivot_b_verification_RUNNING_20260513T201945.json](06-validation/source/checkpoints/pivot_b_verification_RUNNING_20260513T201945.json) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [ideas.md](07-maintenance/source/ideas.md) · [memory.md](07-maintenance/source/memory.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 32 runtime bookkeeping files and 0 automated scan reports. These record the system workflow alongside the experiment assets.
