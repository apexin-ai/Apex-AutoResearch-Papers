# analysis retrain chain v2 bootstrap

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_retrain_chain_v2_bootstrap_20260518T045534_result.json`
- **Structured JSON:** [`de287a433cafa8b4e1ec.json`](../../sessions/de/de287a433cafa8b4e1ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written. Results summary:

| Pair | AUC (OOF) | 95% CI | p-value |
|------|-----------|--------|---------|
| 0v1 | 0.9842 | [0.9823, 0.9860] | < 0.001 |
| 1v2 | 0.9471 | [0.9432, 0.9509] | < 0.001 |
| 2v3 | 0.8888 | [0.8832, 0.8943] | < 0.001 |
| 3v4 | 0.7994 | [0.7920, 0.8067] | < 0.001 |

**K\* = 4** (all pairs pass CI lower > 0.60). All permutation tests reject H0: AUC=0.5 at p < 0.001. CIs are tight (widths 0.004-0.015) with monotonic AUC decay across depths.

JSON results also saved on server at `results/exp_008_retrain_chain/bootstrap_ci_v2.json`.

---
