# analysis binary reward results v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_binary_reward_results_v2_20260523T114334_result.json`
- **Structured JSON:** [`198cb116682379b10dfc.json`](../../sessions/19/198cb116682379b10dfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results written to `artifacts/binary_reward_final_results.md`.

## Summary

**Training status**: 1/3 iterations complete (iteration 0 done, ~2h remaining). PID 14928 still running.

**Core result from iteration 0 (400 records)**:

| Metric | Value |
|--------|-------|
| **Credit agreement** | **157/157 = 100%** |
| Zero advantage (all-fail groups, no gradient) | 243/400 = 60.75% |
| Episode success rate | 12/72 = 16.67% |
| Groups with ≥1 success | 4/10 |

- 100% credit agreement confirms the theoretical prediction: binary reward + GRPO makes advantage sign perfectly track episode outcome.
- The cost: **60.75% of windows produce zero advantage** (all-fail groups) — no learning signal from these.
- Advantage asymmetry: positive magnitudes ~5× larger than negative (expected at low success rates).

This establishes the baseline for the paper: binary reward gives perfect agreement but wastes 60%+ compute on zero-gradient windows. Step-level reward (format_penalty ≠ 0) should trade a small amount of agreement for gradient signal from all windows.

---
