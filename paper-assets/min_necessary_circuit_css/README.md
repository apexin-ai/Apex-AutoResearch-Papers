# Transformer Model EAP-IG

Project: `min_necessary_circuit_css`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=min_necessary_circuit_css)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 15 source files; 12 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 54 conversations; 255 worker logs/results; 313 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 130 code/configuration files; 0 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 186 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Not found | 0 internal review records; 0 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 44 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/solver-trace-ablation/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `92568f10d844a89b87c0d3497469e17f18de067ebd694a67943e119eae91c455`.

130 code/configuration files; 186 data/result files; 313 trace sources. The selected manuscript has 1 pages; 12 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [docs/paper/main.tex](01-manuscript/source/docs/paper/main.tex) · [docs/paper/references.bib](01-manuscript/source/docs/paper/references.bib) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [artifacts/css.py](03-code/source/artifacts/css.py) · [acdc_topk_sweep.py](03-code/source/acdc_topk_sweep.py) · [artifacts/test_css.py](03-code/source/artifacts/test_css.py) |
| Experiment and supporting data | [artifacts/mean_ablation_results.json](04-experiments/source/artifacts/mean_ablation_results.json) · [artifacts/analysis/analysis_results.json](04-experiments/source/artifacts/analysis/analysis_results.json) · [artifacts/mvp_sva_gpt2_k3/data/sva_results_summary.json](04-experiments/source/artifacts/mvp_sva_gpt2_k3/data/sva_results_summary.json) |
| Internal validation records | No matching files in this snapshot |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [memory.md](07-maintenance/source/memory.md) · [report.md](07-maintenance/source/report.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 48 runtime bookkeeping files and 0 automated scan reports. These record the system workflow alongside the experiment assets.
