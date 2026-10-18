# analyze eval pi05 random k09 long seed44 strict w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k09_long_seed44_strict_w41_20260527T221228_result.json`
- **Structured JSON:** [`3c9c936e9a753918d1e5.json`](../../sessions/3c/3c9c936e9a753918d1e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_id: eval_pi05_random_k09_long_seed44_strict_w41
conclusion: success
overall_success_rate: 31.8%
per_task: {T0: 8%, T1: 48%, T2: 36%, T3: 54%, T4: 18%, T5: 32%, T6: 14%, T7: 34%, T8: 4%, T9: 70%}
three_seed_stats: mean=32.8%, ±1.4pp (seed42=34.2%, seed43=32.4%, seed44=31.8%)
```

三种子方差很小（±1.4pp），Random k=0.9 Long 稳定在 ~32.8%，确认了 Random valley。

---
