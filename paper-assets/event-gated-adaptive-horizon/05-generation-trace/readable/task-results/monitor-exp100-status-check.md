# monitor exp100 status check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp100-status-check_20260526T074527_result.json`
- **Structured JSON:** [`923903fcf1a5760160ad.json`](../../sessions/92/923903fcf1a5760160ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
状态: completed (EXIT_CODE=0)
step: 105K/105K (训练继续到 112K 收集数据后退出)
eval_return_final: 750.6
ve_ratio_final: 0.3
eval_trajectory: [31.0, 168.8, 158.0, 202.9, 306.0, 457.3, 628.8, 687.0, 656.6, 717.7, 750.6]  (5K→105K, 每10K)
ve_ratio_trajectory: [0.0, 0.2, 0.3, 0.3, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3]  (15K→105K, 每10K)
civo_onset: no (max ve_ratio = 0.3, 远低于 1.5 阈值)
```

gate 全程锁定 dt=2（gate_dt_2_frac=1.0），无自适应 horizon 变化。

---
