# Release_examples

This repository is a release-ready collection of manuscripts and supporting artifacts produced by an automated research system. It is organized for external review of what the system generated: papers, source files, code, experiment outputs, generation traces, validation notes, and maintenance records. The layout is inspired by the catalogue-and-manuscript organization of [openai/math](https://github.com/openai/math).

The repository currently contains 30 projects with manuscript PDFs and 18 additional project records with supporting assets. Start with:

- [`traces/README.md`](traces/README.md) — browse the research process through conversations, tool calls, and per-round JSON.
- [`traces/demo.html`](traces/demo.html) — an offline preview containing one recorded conversation round per paper; download the repository and open the file.
- [`CONTENTS.md`](CONTENTS.md) — manuscript map and project-level counts.
- [`paper-assets/index.html`](paper-assets/index.html) — interactive project asset matrix.
- [`paper-assets/asset-matrix.csv`](paper-assets/asset-matrix.csv) — one row per project and requirement.
- [`RELEASE_NOTES.md`](RELEASE_NOTES.md) — scope, verification limits, and privacy handling.

Each paper directory has the same structure:

- `01-manuscript/`: PDF, LaTeX source, references, figures, and version candidates.
- `02-contributions/`: agent roles and contribution records.
- `03-code/`: project code, scripts, and environment files.
- `04-experiments/`: datasets, configurations, result tables, and analysis artifacts.
- `05-generation-trace/`: visual trace entry, GitHub-friendly Markdown transcripts, readable session JSON, per-round messages, and the sanitized source archives.
- `06-validation/`: internal reviews and audit/verification artifacts.
- `07-maintenance/`: roadmap, provenance, submission checklists, plans, and licenses.
- `08-index/`: manifests and version indexes.

The collection is intended to make the system's research process inspectable. The files themselves are evidence of generation and project workflow; they do not by themselves establish independent reproduction, human authorship, external peer review, acceptance, or publication.

To use the complete interactive trace browser, clone the repository and run:

```bash
python3 scripts/serve_traces.py --open
```

The viewer runs locally without additional packages or API keys. On GitHub, each paper's `05-generation-trace/README.md` starts with human-readable Markdown transcripts; the JSON links beside them provide the complete structured records. See the [format guide](traces/FORMAT.md) for source provenance, round boundaries, chunked records, and reference projects.
