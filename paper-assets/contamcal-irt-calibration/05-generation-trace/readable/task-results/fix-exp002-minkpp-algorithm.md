# fix exp002 minkpp algorithm

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp002_minkpp_algorithm_20260514T035901_result.json`
- **Structured JSON:** [`9d12204a38d26c8134cc.json`](../../sessions/9d/9d12204a38d26c8134cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Integration test passed. Scores are 0.0 because target and reference are the same model (delta = 0 for every token), which is the correct behavior — identical models should produce zero per-token difference.

**Summary of changes to `signal_minkpp.py`:**

1. **New `minkpp_score()` (line 80)**: correct per-token difference implementation — `delta_t = target[t] - ref[t]`, then mean of bottom K% deltas
2. **Old implementation renamed to `minkpp_zscore_score()` (line 98)**: preserved as ablation variant with updated docstring
3. **`compute_minkpp_signal()` unchanged**: still calls `minkpp_score()`, which now uses the correct algorithm. Output column remains `s2_minkpp`
4. **No changes needed** in `compute_signals.py` or `aggregate_rrf.py`

---
