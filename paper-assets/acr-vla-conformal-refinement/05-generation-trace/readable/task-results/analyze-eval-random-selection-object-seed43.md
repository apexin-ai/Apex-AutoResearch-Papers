# analyze eval random selection object seed43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-random-selection-object-seed43_20260518T154919_result.json`
- **Structured JSON:** [`432ad32b1c3a62ce9bac.json`](../../sessions/43/432ad32b1c3a62ce9bac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

## 结果摘要

**eval-random-selection-object-seed43** — LIBERO-Object, K=10 random selection

| 指标 | 值 |
|---|---|
| **overall success_rate** | **9%** (9/100) |
| n_tasks | 10 |
| n_rollouts | 10/task |
| total_rollouts | 100 |

**per_task_sr:**

| Task | seed43 | seed42 |
|---|---|---|
| alphabet_soup | 0.0 | 0.0 |
| cream_cheese | 0.0 | 0.0 |
| salad_dressing | 0.1 | 0.1 |
| bbq_sauce | 0.1 | 0.1 |
| ketchup | 0.0 | 0.4 |
| tomato_sauce | 0.1 | 0.0 |
| butter | 0.0 | 0.2 |
| milk | 0.1 | 0.0 |
| chocolate_pudding | 0.2 | 0.1 |
| orange_juice | 0.3 | 0.2 |

seed43 overall 9% vs seed42 13%，两个 seed 都很低，符合 random baseline 预期。Task 间方差较大（ketchup seed42=0.4 vs seed43=0.0），说明随机选择结果不稳定。

---
