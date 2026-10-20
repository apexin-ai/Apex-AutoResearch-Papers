# bugfix cascade empirical 20 20 fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_cascade_empirical_20_20_fix_20260520T194026_result.json`
- **Structured JSON:** [`e7fd9414bbe7ce74a8c8.json`](../../sessions/e7/e7fd9414bbe7ce74a8c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Two remaining matches — both are legitimate uses ("across 20 experiments" describing the total dataset size, and "all 20 experiments" in the metric asymmetry argument). Neither is a "20/20 success" claim. These are correct and should stay.

All edits complete:

1. **`cascade_ordering_derivation.md`**: Replaced the 4-experiment comparison with 15/15 (α ≥ 0.30) claim, added low-α theoretical consistency, threshold sensitivity, and C4 MAUVE caveat. Also updated the MAUVE remark in Part 3 to note corpus-dependence.

2. **`cascade_empirical_validation.md`**: Summary point 1 now states 15/15 for α ≥ 0.30, explicitly notes 5 sub-threshold experiments as "neither confirmed nor refuted," and includes threshold sensitivity and C4 MAUVE caveats.

3. **`cascade_empirical_data.json`**: Updated `cascade_ordering_universal` (15/15 with qualification) and `t_D_invariant` (17 WikiText + C4 domain confound note).

---
