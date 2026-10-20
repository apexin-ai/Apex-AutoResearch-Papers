# paper language polish and submission

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_language-polish-and-submission_20260516T012707_result.json`
- **Structured JSON:** [`8919702f6f3eb423a021.json`](../../sessions/89/8919702f6f3eb423a021.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both tasks complete. Summary:

---

## Task 1: Language Polishing — Changes per file

**abstract.tex**: No changes needed (clean).

**introduction.tex** (3 edits):
- Added missing article: "a non-trivial residual"
- Added comma before "respectively"
- (Already had "A separate line of work" fix from prior edit)

**method.tex** (1 edit):
- "while semantically unrelated" → "while remaining semantically unrelated" (dangling participle fix)
- (Comma after "In interpreting ISR results" already present)

**experiments.tex** (7 edits):
- Added comma: "by 1000 steps, the embedding rate"
- Added complementizer: "shows that aggregate metrics obscure"
- Unified terminology: "genuine rate" → "non-hacking rate" (2 occurrences in temporal collapse paragraph)
- "genuine proofs" → "non-hacking proofs"
- Removed redundant "as both fact and query" in Prolog seed~44 parenthetical
- "reported 100% genuine" → "reported 100% non-hacking"
- "the genuine residual" → "the non-hacking residual"

**related_work.tex**: No changes needed.

**conclusion.tex** (1 edit):
- "the strict classifier labeled genuine" → "labeled non-hacking"

**limitations.tex**: No changes needed.

**appendix.tex** (8 edits):
- Added article: "rather than an absence of reasoning"
- Unified "genuine rate" → "non-hacking rate" in table caption, table cell heading, paragraph heading, and running text (6 occurrences)
- "classified as genuine" → "classified as non-hacking"
- "$n_{\text{genuine}}$" → "$n_{\text{N-H}}$" (2 table cells)

## Task 2: Submission Package

- **Compilation**: 0 errors, 19 pages
- **Anonymization**: `\author{Anonymous ACL submission}`, no identifying info in .tex files
- **submission.zip**: 733 KB, 20 files (9 .tex, 5 figure PDFs, main.pdf, main.bbl, references.bib, acl.sty, acl_natbib.bst)
- **Location**: `artifacts/submission.zip`

## No anomalies found.

---
