# analyze eval pi05 l2norm k095 long seed46 strict w27

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k095_long_seed46_strict_w27_20260528T110044_result.json`
- **Structured JSON:** [`a12e94c574b22aa35f74.json`](../../sessions/a1/a12e94c574b22aa35f74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_id: eval_pi05_l2norm_k095_long_seed46_strict_w27
conclusion: success
success_rate: 87.2%
per_task: {T0: 96%, T1: 98%, T2: 94%, T3: 100%, T4: 98%, T5: 96%, T6: 48%, T7: 96%, T8: 50%, T9: 96%}
episodes_completed: 500/500
```

5-seed 汇总：s42=85.8%, s43=86.2%, s44=86.8%, s45=87.8%, **s46=87.2%** → **5-seed mean=86.76%±0.80pp**。s46 排第二高，进一步确认 L2norm k=0.95 Long 稳定在 86-88% 区间。

---
