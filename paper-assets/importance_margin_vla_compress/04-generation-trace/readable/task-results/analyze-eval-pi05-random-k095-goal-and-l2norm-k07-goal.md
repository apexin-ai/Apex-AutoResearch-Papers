# analyze eval pi05 random k095 goal and l2norm k07 goal

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k095_goal_and_l2norm_k07_goal_20260524T105715_result.json`
- **Structured JSON:** [`3ab55ffe9fad3a9bacbc.json`](../../sessions/3a/3ab55ffe9fad3a9bacbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个日志均无 W&B URL。结果如下：

## 实验 1: eval_pi05_random_k095_goal_seed42_postfix
- **overall_sr: 82.6%**
- total_episodes: 500 (10 tasks × 50 episodes)
- per_task:

| Task | Name | SR |
|------|------|-----|
| T0 | (task 0) | 86.0% |
| T1 | (task 1) | 94.0% |
| T2 | put the wine bottle on top of the cabinet | 84.0% |
| T3 | open the top drawer and put the bowl in | 78.0% |
| T4 | put the bowl on top of the cabinet | 98.0% |
| T5 | push the plate to the front of the stove | 92.0% |
| T6 | put the cream cheese in the bowl | 88.0% |
| T7 | turn on the stove | 100.0% |
| T8 | put the bowl on the plate | 96.0% |
| T9 | put the wine bottle on the rack | 10.0% |

## 实验 2: eval_pi05_l2norm_k07_goal_seed42_postfix
- **overall_sr: 70.2%**
- total_episodes: 500 (10 tasks × 50 episodes)
- per_task:

| Task | Name | SR |
|------|------|-----|
| T0 | (task 0) | 74.0% |
| T1 | (task 1) | 82.0% |
| T2 | (task 2) | 70.0% |
| T3 | open the top drawer and put the bowl in | 48.0% |
| T4 | put the bowl on top of the cabinet | 92.0% |
| T5 | push the plate to the front of the stove | 70.0% |
| T6 | put the cream cheese in the bowl | 62.0% |
| T7 | turn on the stove | 100.0% |
| T8 | put the bowl on the plate | 60.0% |
| T9 | put the wine bottle on the rack | 44.0% |

## 关键发现

**Random k=0.95 Goal = 82.6%**：相比 baseline 88.4% 下降 5.8pp。不算 near-baseline，降幅比预期大，主要被 T9 (10%) 拖累。

**L2norm k=0.7 Goal = 70.2%**：与 Random k=0.7 Goal=78% 相比，L2norm 反而低 7.8pp。L2norm 在 Goal suite 上 k=0.7 时表现不如 random pruning，与 Object/Spatial suite 上 L2norm 优于 random 的趋势相反。

---
