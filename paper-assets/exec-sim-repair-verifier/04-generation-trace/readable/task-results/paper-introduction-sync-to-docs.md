# paper introduction sync to docs

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_introduction-sync-to-docs_20260515T144315_result.json`
- **Structured JSON:** [`94cf9845692e3dacb1d4.json`](../../sessions/94/94cf9845692e3dacb1d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both citation keys exist in `references.bib`.

**Summary of all changes made:**

**artifacts/_project/paper/introduction.tex** (3 edits):
- `zhang2025swerm` → `shum2025swerm`
- `ding2025selfexecution` → `maimon2026selfexecution`
- `p = 0.008` → `p = 0.0066`

**docs/paper/introduction.tex** (2 edits):
- Para 2: `53.7--67.2\% of \cwm{} predictions are unparseable across seeds` → `the majority of \cwm{} predictions become unparseable` (qualitative, numbers kept in C1)
- C1 end: added zero-shot baseline sentence `(32B NF4: 71.69\% vs.\ fine-tuned 4B: 88.43\%)`

**Verified:**
- No residual `zhang2025swerm`, `ding2025selfexecution`, or `p = 0.008` in either introduction file
- Both `shum2025swerm` and `maimon2026selfexecution` exist in `references.bib`
- LaTeX compiles without errors (citation undefined warnings are normal pre-bibtex)

**Flagged — same old citation keys remain in other files:**
- `related_work.tex` (lines 7, 15)
- `method.tex` (line 55)
- `introduction_304198.tex` (lines 8, 14)
- `dream_reports/.../paper.tex` (3 occurrences)

Want me to fix those too?

---
