# paper fix threshold tables

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix_threshold_tables_20260517T173019_result.json`
- **Structured JSON:** [`80a3af4b5f2d168d695e.json`](../../sessions/80/80a3af4b5f2d168d695e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All corrections verified. Let me also confirm the `tab:single-method-errors` Threshold row is consistent with the new `tab:method_comparison` data:

- α=0.00: subscripts 3,1,1 → (3+1+1)/24 = 5/24 = 20.8% ✓
- α=0.50: subscripts 0,0,0 → 0/24 = 0% ✓  
- α=0.75: subscripts 4,0,4 → 8/24 = 33.3% ✓

Summary of changes made to `experiments.tex`:

| Location | Old | New |
|----------|-----|-----|
| Line 114 (`tab:method_comparison` Threshold row) | 62.5 / 37.5 / 100 / 50 / 100 / 62.5 | 20.8 / 0 / 0 / 33.3 / 100 / 20.8 |
| Line 319 (`tab:fpr_fnr` Threshold FPR) | 29.2% (12.5--62.5) | 20.8% (12.5--37.5) |
| Line 232 (prose FPR ordering) | "through 62.5% (threshold) and 37.5% (differenced)" | "through 37.5% (differenced) and 20.8% (threshold)" |
| Line 88 (α=0.50 description) | "correlation-based methods (naive, differenced, threshold) unanimously find significance" | corrected to note threshold finds 0% |
| Line 92 (α=0.25 threshold value) | "threshold onset to 37.5%" | "threshold onset to 0%" |
| Line 175 (onset boundary paragraph) | "Correlation-based methods unanimously find significance" | corrected to specify only naive and differenced |

Compilation passes with 0 errors. The `tab:single-method-errors` per-seed subscripts (3,1,1 / 0,0,0 / 4,0,4) are consistent with the corrected aggregates.

---
