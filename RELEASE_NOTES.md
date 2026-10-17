# Release notes

## Scope

This release contains eight projects collected from the local `workspace.tar.gz` archives. The release includes the generated manuscript PDFs and source, experiment data and outputs, project code, contribution notes, internal review and audit materials, dated roadmaps, and sanitized text traces. The original workspace archives remain outside this repository and were not modified.

## Status evidence

Each paper README and the dashboard separates a project's dated internal roadmap record from official external evidence. A manuscript cover such as “Anonymous ACL submission”, a generated review, or a submission checklist is not treated as proof of an official submission or acceptance. Dates in the catalogue are snapshot dates from the project files.

## Trace and credential handling

The trace archives are derived copies. The collector redacts credential fields, token patterns, private keys, and large binary attachment payloads. A second scan of ordinary files and all members of the eight trace archives found no AWS, GitHub, Hugging Face, Anthropic, Google token, or private-key pattern.

The only archive above GitHub's 100 MB per-file limit was split into 80 MiB parts at `paper-assets/importance_margin_vla_compress/05-generation-trace/trace-files.tar.gz.parts/`. Use [`scripts/reconstruct_trace.py`](scripts/reconstruct_trace.py) and the included manifest to reconstruct and verify it.

## Verification limits

The release preserves the evidence available in the local project archives. It does not claim that every experiment can be rerun on a fresh machine, that all data licenses permit redistribution, or that internal review is equivalent to external peer review.
