# analyze eval xvla l2norm k05 goal seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_xvla_l2norm_k05_goal_seed42_v3_20260523T194946_result.json`
- **Structured JSON:** [`70f9f1af9f821c2ac766.json`](../../sessions/70/70f9f1af9f821c2ac766.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无 W&B 记录。结果汇总：

```
Overall success rate: 59.0% (295/500)
95% Wilson CI: [54.6%, 63.2%]
Total episodes: 500
Elapsed: 65.8 min

Per-task breakdown:
  Task 0: 80.0% (40/50) -- open the middle drawer of the cabinet
  Task 1: 92.0% (46/50) -- put the bowl on the stove
  Task 2: 98.0% (49/50) -- put the wine bottle on top of the cabinet
  Task 3: 34.0% (17/50) -- open the top drawer and put the bowl inside
  Task 4: 100.0% (50/50) -- put the bowl on top of the cabinet
  Task 5:  0.0%  (0/50) -- push the plate to the front of the stove
  Task 6: 24.0% (12/50) -- put the cream cheese in the bowl
  Task 7: 72.0% (36/50) -- turn on the stove
  Task 8: 90.0% (45/50) -- put the bowl on the plate
  Task 9:  0.0%  (0/50) -- put the wine bottle on the rack

W&B run ID: 无
```

对比假设中的基准：
- **L2norm k=0.5 Goal: 59.0%** vs attention k=0.5 Goal (98.2%) vs random k=0.5 Goal (67.2%)
- L2norm 显著弱于 attention（差 39.2pp），也低于 random（差 8.2pp）
- Task 5 和 Task 9 完全失败（0%），是主要拖累项

无错误或异常，EXIT_CODE=0，全部 500 episodes 正常完成。

---
