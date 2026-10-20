# paper fix overfull hbox

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_overfull_hbox_20260522T094334_result.json`
- **Structured JSON:** [`07c628eb143005dddfee.json`](../../sessions/07/07c628eb143005dddfee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Main text ends on page 8 (conclusion on page 7, page 8 has Limitations/Ethics). Bibliography starts on page 9. Page count is preserved.

Summary of results:

**Fixed (6 overfull hbox warnings >20pt):**

| # | File | Severity | Fix |
|---|------|----------|-----|
| 1 | `appendix.tex` (per-depth recall table) | 58.6pt | `\resizebox{\columnwidth}{!}{...}` |
| 2 | `appendix.tex` (dataset stats table) | 23.9pt | `\resizebox{\columnwidth}{!}{...}` |
| 3 | `appendix.tex` (feature desc table) | 23.9pt* | Shortened "Shannon entropy of word frequencies" to "Word frequency entropy"; widened `p{0.45\textwidth}` to `p{0.50\textwidth}`; added `\resizebox` |
| 4 | `appendix_extended.tex` (dose-response paragraph) | 32.2pt | `{\sloppy ...\par}` around dense math paragraph |
| 5 | `experiments_c1.tex` (cross-domain table) | 21.9pt | `\resizebox{\columnwidth}{!}{...}` |
| 6 | `method.tex` (config table) | 20.1pt | `\resizebox{\columnwidth}{!}{...}` |
| 7 | `tables/tab_filtering_main.tex` | 20.0pt | `\resizebox{\columnwidth}{!}{...}` |

**Before:** 11 overfull warnings (6 above 20pt, max 58.6pt)
**After:** 5 overfull warnings (all below 16pt, max 15.1pt)
**Pages:** 8 main text pages (unchanged), 23 total
**Undefined references:** 0

---
