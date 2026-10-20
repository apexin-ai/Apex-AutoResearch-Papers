# Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001

Project: `agent_progress_probe`

[Manuscript](01-manuscript/paper.pdf) · [Research code](03-code/source/) · [Experiment assets](04-experiments/source/) · [Readable conversations](05-generation-trace/readable/README.md) · [Trace browser](../../traces/index.html?project=agent_progress_probe)

## Asset review matrix

| Requirement | Status | Included evidence | Verification limit |
|---|---|---|---|
| Manuscript and versions | Available | 55 source files; 25 PDF candidates | Candidate filenames do not establish official submission or publication. |
| Academic status | Unverified | Project status documents are included as source evidence; formal submission, acceptance, or publication status is unverified. | Official submission, acceptance, and publication were not independently checked. |
| AI / human contribution | Partial | 3 task/role records | User and assistant roles do not identify people or establish author contributions. |
| Generation trace | Organized | 156 conversations; 577 worker logs/results; 767 source files | Overlapping snapshots are retained; credentials and binary attachments are redacted. |
| Reproduction code | Available | 245 code/configuration files; 0 environment manifests | The code is archived; experiments were not rerun for this release. |
| Experiments and environment | Partial | 748 data/result files | Original data permissions and completeness require project-specific review. |
| Validation evidence | Partial | 5 internal review records; 7 other audit records | Internal reviews are project evidence, not independently verified external reviews. |
| Maintenance | Partial | 121 project documentation files; 0 license files | A project license file applies only within its stated scope. |

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

Source: `s3://agent-ml-research-project-backups-20260531/occsafe_vla/workspace.tar.gz`. Archive SHA-256 (derived archive for export snapshots): `541499ff9e8f9937e13ca55d5892301ea41ff1bed125e955affeed7e40580d87`.

245 code/configuration files; 748 data/result files; 767 trace sources. The selected manuscript has 19 pages; 25 PDF candidates are indexed.

Original project paths and release paths are mapped in [the file manifest](08-index/asset-manifest.csv). Selected PDFs are copied to `01-manuscript/paper.pdf`; other versions remain under manuscript source. Files exceeding the GitHub size limit are split into checksum-verified parts. Dependency installations, caches, Git internals, credential/account files, and non-regular archive entries are excluded and recorded in [the exclusion manifest](08-index/excluded-files.csv).

Generated documentation is English. Source files and conversations retain their original language. Credentials and inline attachment payloads are redacted. No project code was executed as part of asset collection; archived code and internal reviews do not establish independent reproduction or external acceptance.

## Concrete file examples

| Content | Examples from this snapshot |
|---|---|
| Manuscript assets | [Selected paper PDF](01-manuscript/paper.pdf) · [docs/paper/main.tex](01-manuscript/source/docs/paper/main.tex) · [docs/paper/main.pdf](01-manuscript/source/docs/paper/main.pdf) |
| Contribution records | [task_context/agent.md](02-contributions/source/task_context/agent.md) · [task_context/director.md](02-contributions/source/task_context/director.md) · [task_context/reviewer.md](02-contributions/source/task_context/reviewer.md) |
| Research code and configurations | [src/evaluation/gold_set_eval.py](03-code/source/src/evaluation/gold_set_eval.py) · [src/analysis/llm_structured_input.py](03-code/source/src/analysis/llm_structured_input.py) · [src/analysis/error_overlap_canonical.py](03-code/source/src/analysis/error_overlap_canonical.py) |
| Experiment and supporting data | [artifacts/e9_e10_results.json](04-experiments/source/artifacts/e9_e10_results.json) · [artifacts/e5_e6_e8_results.json](04-experiments/source/artifacts/e5_e6_e8_results.json) · [artifacts/d073/coverage_2lf.json](04-experiments/source/artifacts/d073/coverage_2lf.json) |
| Internal validation records | [artifacts/review_reports/round_2.md](06-validation/source/artifacts/review_reports/round_2.md) · [artifacts/review_reports/round_1.md](06-validation/source/artifacts/review_reports/round_1.md) · [artifacts/review_reports/round_4.md](06-validation/source/artifacts/review_reports/round_4.md) |
| Project documentation | [ROADMAP.md](07-maintenance/source/ROADMAP.md) · [memory.md](07-maintenance/source/memory.md) · [report.md](07-maintenance/source/report.md) |
| Provenance and file indexes | [Source/file manifest](08-index/asset-manifest.csv) · [Snapshot metadata](08-index/asset-manifest.json) |
| Recorded conversations and tools | [Readable Markdown](05-generation-trace/readable/README.md) · [Structured JSON catalogue](05-generation-trace/catalog.json) |

Supporting files include 120 runtime bookkeeping files and 0 automated scan reports. These record the system workflow alongside the experiment assets.
