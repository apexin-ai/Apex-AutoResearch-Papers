# How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints

Project directory: `recursive_gen_depth_est`

## Browse generation traces

[Visual browser](../../traces/index.html?project=recursive_gen_depth_est) · [Offline preview](../../traces/demo.html?project=recursive_gen_depth_est) · [GitHub trace guide](05-generation-trace/README.md) · [JSON catalogue](05-generation-trace/catalog.json)

Includes 1,779 source files and 166,550 recorded messages/events. Use the trace guide for session JSON and the browser for per-round inspection and downloads. Counts include overlapping source snapshots.

## Asset review matrix

| Requirement | Status | Organized contents and evidence | Still to verify |
|---|---|---|---|
| Manuscript and versions | Available | paper.pdf; 15 TeX/Bib source files; 12 archive version candidates | The author must confirm which files are the submitted and public revision versions; candidates were not automatically designated as official versions. |
| Academic status | Unverified | As of 2026-05-20, the project record states that the paper is finalized and awaits the user’s decision to submit to ARR, submit directly, or archive it; an internal review request also awaits user confirmation. Manuscript cover marker: Anonymous ACL submission. | This status reflects only the project files available on that date; official submission receipts, review/acceptance decisions, and publication records were not verified in the archive. |
| AI / human contribution | Partial | 3 role/task descriptions; the conversations record user/assistant/tool roles | Role labels cannot verify real-person identity, human decisions, edit ownership, or author contribution statements. |
| Generation trace | Organized | 347 conversation JSONL files; 1328 worker logs/results; text traces were packaged | Obvious credentials were redacted and binary payloads such as images were omitted; consult the source archive for the complete original. |
| Reproduction code | Available | 86 project code/command files; 0 dependency/environment manifests | Reproduction is needed to verify that the environment remains installable and that the code matches the manuscript version. |
| Experiments and environment | Partial | 80 data/result files; datasets, configurations, and dependency manifests were collected | Data permissions, hardware budget, completeness of failed runs, and cross-environment reproduction require item-by-item verification. |
| Validation evidence | Partial | 17 internal review reports; 19 audit/validation files; source identity not verified | These files do not establish that human verification, independent reproduction, or public external review has been completed. |
| Maintenance | Partial | 1 provenance files; 1 submission forms/checklists/metadata files; 0 license files; Project plans, roadmaps, and issue records are archived. See 01-manuscript/ for reference files. | The maintainer still needs to confirm license scope, closure of known issues, and the complete revision history. |

## Organized directories

- `01-manuscript/`: Current paper PDF, LaTeX source, references, and typesetting assets.
- `02-contributions/`: Agent role descriptions and human/AI contribution review notes.
- `03-code/`: Project code, figure-generation code, and environment manifests.
- `04-experiments/`: Data, result tables, analysis artifacts, and related notes.
- `05-generation-trace/`: Redacted conversation, tool-call, worker-log, and loop-note archive; binary attachment payloads omitted.
- `06-validation/`: Internal review reports and audit status files.
- `07-maintenance/`: Plans, provenance, roadmaps, references, and license files.
- `08-index/`: Source archive paths, version candidates, and per-category asset manifests.

## Important interpretation

- Manuscript marker: `Anonymous ACL submission`. This is cover text only and does not by itself establish submission, acceptance, or publication.
- Academic status snapshot (2026-05-20): The ROADMAP records that the paper is finalized and awaits the user’s decision to submit to ARR, submit directly, or archive it; an internal review request also awaits user confirmation. Official submission receipts, review decisions, or publication records were not verified in this archive. Source: `07-maintenance/source/ROADMAP.md`.
- Source archive: `recursive_gen_depth_est/workspace.tar.gz`. The generation-trace copy redacts obvious credential fields and omits binary attachment payloads; the source archive itself was not modified.
- Archive read status: `Archive scan completed`.

## Directory counts

86 source files; 80 experiment data/result files; 17 internal review reports; 19 audit/validation files; 347 conversation records; 1328 worker logs/results; main PDF (26 pages).

Manifests are organized by filename and archive path. The presence of evidence files does not establish independent reproduction or completion of external peer review.
