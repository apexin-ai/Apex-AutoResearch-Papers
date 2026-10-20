# OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

Project: `schema_semantic_constrained_ie`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=schema_semantic_constrained_ie)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 85 source files; 51 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 447 conversations; 1973 worker logs/results; 2527 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 451 code/configuration files; 0 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 1384 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 23 internal review records; 17 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 285 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/schema_semantic_constrained_ie/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `33ac83b91c8dccebf2f804b4e630383934114fb5896936f95fac1d576ae12465`.

451 code/configuration files; 1,384 data/result files; 2,527 trace sources. The selected manuscript has 39 pages; 51 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [artifacts/_project/paper/main.tex](01-manuscript/source/artifacts/_project/paper/main.tex) · [artifacts/_project/paper/main.pdf](01-manuscript/source/artifacts/_project/paper/main.pdf) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [scripts/analyze_cf_cascade.py](03-code/source/scripts/analyze_cf_cascade.py) · [scripts/diagnose_entity_type_tokens.py](03-code/source/scripts/diagnose_entity_type_tokens.py) · [compiler/__init__.py](03-code/source/compiler/__init__.py) |
| Experiment and supporting data | [artifacts/runtime_benchmark.json](04-experiments/source/artifacts/runtime_benchmark.json) · [artifacts/figures/kappa_dr_data.json](04-experiments/source/artifacts/figures/kappa_dr_data.json) · [data/wikievents/event_role_KAIROS.json](04-experiments/source/data/wikievents/event_role_KAIROS.json) |
| Internal validation records | [_last_visual_review.json](06-validation/source/_last_visual_review.json) · [_paper_audit_result.json](06-validation/source/_paper_audit_result.json) · [artifacts/bib_audit_report.md](06-validation/source/artifacts/bib_audit_report.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [artifacts/lora_backups/westd-16980/70b_lora_docred/README.md](07-maintenance/source/artifacts/lora_backups/westd-16980/70b_lora_docred/README.md) · [artifacts/lora_backups/westd-16980/70b_lora_scierc/README.md](07-maintenance/source/artifacts/lora_backups/westd-16980/70b_lora_scierc/README.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 338 runtime bookkeeping files and 2 automated scan reports. These record the system workflow alongside the experiment assets.
