# How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?

Project directory: `schema-dag-extraction`

## Browse generation traces

[Visual browser](../../traces/index.html?project=schema-dag-extraction) · [Offline preview](../../traces/demo.html?project=schema-dag-extraction) · [GitHub trace guide](05-generation-trace/README.md) · [JSON catalogue](05-generation-trace/catalog.json)

Includes 1,242 source files and 131,771 recorded messages/events. Use the trace guide's Readable Markdown pages for human review; the adjacent JSON links and browser provide structured and per-round inspection. Counts include overlapping source snapshots.

## Asset review matrix

| Requirement | Status | Organized contents and evidence | Still to verify |
|---|---|---|---|
| Manuscript and versions | Available | paper.pdf; 15 TeX/Bib source files; 24 archive version candidates | The author must confirm which files are the submitted and public revision versions; candidates were not automatically designated as official versions. |
| Academic status | Unverified | As of 2026-05-22, the project record states that v35 is submission-ready and awaits user approval for ARR submission. Manuscript cover marker: Anonymous ACL submission. | This status reflects only the project files available on that date; official submission receipts, review/acceptance decisions, and publication records were not verified in the archive. |
| AI / human contribution | Partial | 3 role/task descriptions; the conversations record user/assistant/tool roles | Role labels cannot verify real-person identity, human decisions, edit ownership, or author contribution statements. |
| Generation trace | Organized | 217 conversation JSONL files; 980 worker logs/results; text traces were packaged | Obvious credentials were redacted and binary payloads such as images were omitted; consult the source archive for the complete original. |
| Reproduction code | Available | 135 project code/command files; 1 dependency/environment manifests | Reproduction is needed to verify that the environment remains installable and that the code matches the manuscript version. |
| Experiments and environment | Partial | 68 data/result files; datasets, configurations, and dependency manifests were collected | Data permissions, hardware budget, completeness of failed runs, and cross-environment reproduction require item-by-item verification. |
| Validation evidence | Partial | 28 internal review reports; 15 audit/validation files; source identity not verified | These files do not establish that human verification, independent reproduction, or public external review has been completed. |
| Maintenance | Partial | 2 provenance files; 7 submission forms/checklists/metadata files; 1 license files; Project plans, roadmaps, and issue records are archived. See 01-manuscript/ for reference files. | The maintainer still needs to confirm license scope, closure of known issues, and the complete revision history. |

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
- Academic status snapshot (2026-05-22): The ROADMAP records that v35 is submission-ready and awaits user approval for ARR submission. Official submission receipts, review decisions, or publication records were not verified in this archive. Source: `07-maintenance/source/ROADMAP.md`.
- Source archive: `schema-dag-extraction/workspace.tar.gz`. The generation-trace copy redacts obvious credential fields and omits binary attachment payloads; the source archive itself was not modified.
- Archive read status: `Archive scan completed`.

## Directory counts

135 source files; 68 experiment data/result files; 28 internal review reports; 15 audit/validation files; 217 conversation records; 980 worker logs/results; main PDF (26 pages).

Manifests are organized by filename and archive path. The presence of evidence files does not establish independent reproduction or completion of external peer review.
