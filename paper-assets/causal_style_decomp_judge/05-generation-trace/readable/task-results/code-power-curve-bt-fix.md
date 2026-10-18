# code power curve bt fix

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_power_curve_bt_fix_20260521T030205_result.json`
- **Structured JSON:** [`86d93aace373d8f6ae6d.json`](../../sessions/86/86d93aace373d8f6ae6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both scripts ran successfully. Results:

### Task A: Power Curve (fixed)

80% power crossings:
| Method | n for 80% power |
|--------|-----------------|
| Pairwise BT (p=0.609) | **163** |
| Pairwise Sign Test (p=0.691, filtered) | **93** |
| Binarized Likert (p=0.606, tie-adj.) | **462** |
| Likert ATE (d=0.073) | **1,473** (off-chart) |

Binarized Likert now correctly requires n≈462 (vs old 172), confirming the Likert Blindspot argument. PDF saved to `artifacts/figures/paper/power_curve.pdf`.

### Task B: BT Bootstrap (pair-level fix)

**All Data (100 pairs, 197 comparisons):**
- BT P(formal wins): 0.6091
- Pair-level CI: [0.5381, 0.6784], p = 0.001
- Comparison-level CI: [0.5381, 0.6751] (reference)
- CI width ratio pair/comp: 1.024 (pair CI ~2.4% wider)

**NLI-filtered (88 pairs, 173 comparisons):**
- BT P(formal wins): 0.6300
- Pair-level CI: [0.5575, 0.7028], p = 0.0004
- Comparison-level CI: [0.5607, 0.6994] (reference)
- CI width ratio pair/comp: 1.048 (pair CI ~4.8% wider)

As expected, pair-level CIs are slightly wider than comparison-level, but conclusions hold — both subsets remain significant with the corrected bootstrap.

---
