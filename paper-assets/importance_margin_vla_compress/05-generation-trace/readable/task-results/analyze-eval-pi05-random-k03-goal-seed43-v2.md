# analyze eval pi05 random k03 goal seed43 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k03_goal_seed43_v2_20260523T213113_result.json`
- **Structured JSON:** [`725b773eb66c1f71ce78.json`](../../sessions/72/725b773eb66c1f71ce78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已完整获取。汇总结果：

```
RESULT:
- overall_sr: 53.6%
- per_task:
    T0 [open the middle drawer of the cabinet]: 80.0% (40/50)
    T1 [put the bowl on the stove]: 12.0% (6/50)
    T2 [put the wine bottle on top of the cabinet]: 76.0% (38/50)
    T3 [open the top drawer and put the bowl inside]: 52.0% (26/50)
    T4 [put the bowl on top of the cabinet]: 60.0% (30/50)
    T5 [push the plate to the front of the stove]: 32.0% (16/50)
    T6 [put the cream cheese in the bowl]: 26.0% (13/50)
    T7 [turn on the stove]: 100.0% (50/50)
    T8 [put the bowl on the plate]: 70.0% (35/50)
    T9 [put the wine bottle on the rack]: 28.0% (14/50)
- total_episodes: 500
- elapsed: 127.4 min
- anomalies: 无异常，所有 task 正常完成 50 episodes
- W&B: 未找到对应 run（eval-only 实验未上传 W&B）
- comparison:
    seed42 = 50.6%
    seed43 = 53.6%
    delta  = +3.0pp
    mean   = 52.1%
    std    = ±2.1pp
```

两个 seed 的 CV 结果一致性较好（std ±2.1pp），Random k=0.3 在 Goal suite 上的稳定表现约 52%。

---
