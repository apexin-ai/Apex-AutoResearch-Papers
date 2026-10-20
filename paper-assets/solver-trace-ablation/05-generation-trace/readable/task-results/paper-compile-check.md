# paper compile check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile-check_20260522T065759_result.json`
- **Structured JSON:** [`f60ca8113c1a290370c3.json`](../../sessions/f6/f60ca8113c1a290370c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Summary:

| Check | Result |
|---|---|
| **Sync** | All .tex/.bib files synced, MD5 verified identical |
| **Compilation** | Success (latexmk, no errors) |
| **Total pages** | 24 |
| **Main text** | 8 pages (References starts page 9) — within limit |
| **Undefined references** | 0 |
| **Missing citations** | 0 |
| **Multiply-defined labels** | 0 |
| **Appendix new sections** | All rendered — `app:seed-convergence` (E.5, p20), `app:8b-results` (E.6, p20), `app:llama-coldstart` (E.4, p19), `app:beta03` (E.1, p18), tables 7-12 on pp22-24 |
| **Warnings** | 10× hyperref "Token not allowed" — math (`$\beta$`) in section titles on lines 627/676 of `appendix.tex`. Cosmetic only, affects PDF bookmarks not rendered content. Harmless for submission. |

Paper is clean and ready for submission.

---
