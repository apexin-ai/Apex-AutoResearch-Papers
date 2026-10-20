# Release notes

## 2026-10-18: Browseable generation traces

The eight sanitized trace archives now also have a deterministic JSON export and a static browser. The export covers 12,444 source files and 1,127,056 recorded messages/events, including overlapping conversation snapshots and worker logs. These are source-record counts, not a count of independent research actions. The source archives are retained.

Each paper has a trace README, JSON catalogue, per-source session JSON, chunked large records, and direct GitHub indexes. The browser adds paper/session selection, round navigation, role and text filters, tool argument/result display, source-line provenance, and selected-round JSON downloads. `traces/demo.html` is an offline preview with one bounded recorded conversation round per paper.

New interface text and guides are English; recorded source content keeps its original language. Tool results wrapped in user envelopes are classified as tool results, missing user prompts remain unbounded sequences, and parallel logs remain separate. See [the format guide](traces/FORMAT.md) for references and verification procedures.

## Scope

This release contains 69 research projects collected from project backup snapshots. The release includes the generated manuscript PDFs and source, experiment data and outputs, project code, contribution notes, internal review and audit materials, dated roadmaps, and sanitized text traces. The original workspace archives remain outside this repository and were not modified.

## Status evidence

Each paper README and the dashboard separates a project's dated internal roadmap record from official external evidence. A manuscript cover such as “Anonymous ACL submission”, a generated review, or a submission checklist is not treated as proof of an official submission or acceptance. Dates in the catalogue are snapshot dates from the project files.

## Trace and credential handling

The trace archives are derived copies. The collector redacts credential fields, token patterns, private keys, and large binary attachment payloads. A second scan of ordinary files and all members of the released trace archives found no AWS, GitHub, Hugging Face, Anthropic, Google token, or private-key pattern.

Files above GitHub's size limit are split into 80 MiB parts with checksum manifests. Use [`scripts/reconstruct_trace.py`](scripts/reconstruct_trace.py) and the included manifest to reconstruct and verify it.

## Verification limits

The release preserves the evidence available in the local project archives. It does not claim that every experiment can be rerun on a fresh machine, that all data licenses permit redistribution, or that internal review is equivalent to external peer review.
