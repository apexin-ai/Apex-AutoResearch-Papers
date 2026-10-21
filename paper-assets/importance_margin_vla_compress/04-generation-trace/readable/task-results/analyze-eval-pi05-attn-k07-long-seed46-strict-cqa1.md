# analyze eval pi05 attn k07 long seed46 strict cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_attn_k07_long_seed46_strict_cqa1_20260528T110049_result.json`
- **Structured JSON:** [`95efefcffb151110380c.json`](../../sessions/95/95efefcffb151110380c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_id: eval_pi05_attn_k07_long_seed46_strict_cqa1
conclusion: success
success_rate: 51.4%
per_task: {T0: 70%, T1: 74%, T2: 70%, T3: 36%, T4: 40%, T5: 34%, T6: 64%, T7: 42%, T8: 4%, T9: 80%}
episodes_completed: 500/500
```

seed46 = 51.4%，低于前几个 seed（s42=53.6%, s43=53.8%, s44=53.8%）约 2.4pp。Attn k=0.7 plateau 存在但有一定波动，T8（moka pots）仅 4% 是主要拖累项。

---
