# paper n16 auroc footnote update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_n16-auroc-footnote-update_20260518T121537_result.json`
- **Structured JSON:** [`a85e25c7a7e041ca0a3c.json`](../../sessions/a8/a85e25c7a7e041ca0a3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All old patterns cleared (grep returns empty). Here's the summary:

### Task 1: 5 locations updated
- **introduction.tex L6**: 13/14 → 15/16, n=14 → n=16
- **methodology.tex L87**: 14 → 16, 13/14 → 15/16, AUROC 0.933 → 0.950
- **results.tex L67**: 13 of 14 → 15 of 16, AUROC 0.933 → 0.950
- **conclusion.tex L8**: 13/14 → 15/16, n=14 → n=16, 92.9% → 93.8%
- **conclusion.tex L18** (Limitations): 13/14 → 15/16

### Task 2: Footnote — removed (stale)

Investigation findings:
- The footnote ("Excluding 3 baseline configurations, the 10-experiment subset yields accuracy=9/10 and AUROC=0.880") is from the **n=13 era** (13−3=10). It doesn't match n=14 (14−3=11≠10).
- The appendix B2 table (`tab:nve_raw`) has a **different** 10-experiment set: the factorial subset including 001 (a baseline) and all four 008e_v3 seeds. B2's AUROC=0.958, accuracy=9/10 at 1.5× threshold.
- AUROC=0.880 requires exactly 22/25 concordant pairs (5 pos, 5 neg), which doesn't match any reconstructable current subset. The underlying data has changed.
- Removed the footnote since it's unreproducible and the appendix B2 already provides a more rigorous sensitivity analysis on the factorial subset.

### Task 3: analysis.tex — confirmed clean

analysis.tex L23 ("thirteen runs") and conclusion.tex L18 ("thirteen runs across three environments") both refer to the **online detector's calibration set** (Table 5, n=13), not the NVE classification set. No AUROC is mentioned in that context. No confusion or updates needed.

---
