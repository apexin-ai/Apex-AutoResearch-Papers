# eval uniform 1 7b seed456 full

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_uniform_1_7b_seed456_full_20260520T205739_result.json`
- **Structured JSON:** [`7a01af0b9c85e2885c3d.json`](../../sessions/7a/7a01af0b9c85e2885c3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 evals complete. Here are the full results:

```
uniform_1_7b_seed456:
  holdout PPL:      13.2800
  OWT PPL:          13.3070
  Wiki PPL:         10.9525
  arc_easy:         0.7361  (acc_norm: 0.7113)
  arc_challenge:    0.3899  (acc_norm: 0.4224)
  hellaswag:        0.4588  (acc_norm: 0.6132)
  piqa:             0.7361  (acc_norm: 0.7448)
  winogrande:       0.6251
  downstream_mean:  0.5892  (acc)
  downstream_mean:  0.6234  (acc_norm, excl. winogrande)
```

Notes:
- **Wiki PPL 10.95** — the most critical indicator per your instructions
- acc_norm is reported where available (winogrande only has acc, no acc_norm)
- downstream_mean(acc) = mean of all 5 tasks' `acc,none`: (0.7361 + 0.3899 + 0.4588 + 0.7361 + 0.6251) / 5 = 0.5892
- downstream_mean(acc_norm) = mean of 4 tasks with acc_norm: (0.7113 + 0.4224 + 0.6132 + 0.7448) / 4 = 0.6229

Total evaluation time: ~447s for downstream, plus ~1693s for all 3 PPL evals.

---
