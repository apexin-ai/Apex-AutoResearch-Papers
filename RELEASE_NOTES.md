# Research asset release

This release organizes 40 original workspace archives into 53 project records with manuscript PDFs and 36 additional project records. The [contents](CONTENTS.md) links to the available papers, code, experiment files, and generation traces. Counts describe source records; they are not a count of independently verified scientific discoveries.

The July project export adds 34 dated snapshots alongside the workspace releases. The [supplementary collections](supplementary/README.md) retain benchmark implementations, results, manuscript exports, revisions, and rebuttals. [Original workspace snapshots](SOURCE_SNAPSHOTS.md) provide fixed links when the same project appears in several source archives.

## Reading the evidence

- Project and category READMEs show concrete source-file examples.
- Readable Markdown transcripts label user instructions, assistant responses, tool calls, and tool results in recorded order. Adjacent JSON files preserve normalized structure and source provenance.
- [The offline trace preview](traces/demo.html) embeds 114 actual bounded recorded rounds. The complete interactive browser is available through `python3 scripts/serve_traces.py --open` after downloading the repository.
- Per-project manifests map original archive members to released files. Archive checksums, exclusions, and PDF versions remain available in each project index.

## Collection and verification

Archives were handled sequentially in temporary storage. Each changed trace collection was compared with its sanitized source for content and order; file sizes and credential patterns were checked before upload. Pushes were checked against the remote commit before temporary project files were removed. This final pass verified 252,723 indexed asset paths against the committed Git tree.

Generated documentation is English. Original documents, code, and conversations retain their recorded language. Credential/account snapshots, dependency installations, caches, and Git internals are excluded; inline attachment payloads and credentials are redacted. Large files use checksum-indexed parts. The source coverage and intentional exclusions are recorded in [release-sources.json](release-sources.json).

Research code was archived without rerunning the scientific experiments. Internal reviews, manuscript filenames, and status notes do not establish independent reproduction or external acceptance. User-role records can originate from agents or the runtime system and do not identify human authorship.
