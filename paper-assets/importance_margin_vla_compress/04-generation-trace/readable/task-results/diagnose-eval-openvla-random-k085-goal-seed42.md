# diagnose eval openvla random k085 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_random_k085_goal_seed42_20260526T135742_result.json`
- **Structured JSON:** [`a459c16e5cec8f5838c0.json`](../../sessions/a4/a459c16e5cec8f5838c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
RESULT: success
SR: 78.6% (393/500)
DETAILS: 10 tasks 全部完成，耗时 193.7 min。
  Per-task SR: cabinet_drawer=70, bowl_stove=92, wine_cabinet=84, drawer_bowl=30,
  bowl_cabinet=98, plate_stove=88, cream_bowl=70, stove_on=98, bowl_plate=86, wine_rack=70
  vs Random k=0.9 Goal=79.6% → k=0.85 仅降 1%，pruning 从 10% 增到 15% 几乎无性能损失。
```

---
