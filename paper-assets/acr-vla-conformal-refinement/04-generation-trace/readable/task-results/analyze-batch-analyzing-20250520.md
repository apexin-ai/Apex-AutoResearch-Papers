# analyze batch analyzing 20250520

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_batch-analyzing-20250520_20260520T125542_result.json`
- **Structured JSON:** [`e1f1227a86846bf152b5.json`](../../sessions/e1/e1f1227a86846bf152b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| # | exp_id | conclusion | SR | 关键 metrics |
|---|--------|------------|-----|-------------|
| 1 | eval-adaptive-k-spatial-p90-seed43 | success | **32%** | avg_K=3.6, fast_path=80.2%, mean_l2=0.0905 |
| 2 | eval-random-selection-spatial-seed43 | success | **26%** | baseline: random selection |
| 3 | eval-argmin-object-seed49 | success | **16%** | argmin baseline on Object |
| 4 | eval-obs-only-spatial-norm02-seed42 | **不存在** | — | registry 中无此 exp_id，未创建 |
| 5 | eval-obs-only-goal-norm02-seed52 | success | **68%** | turn_on_stove=100%, put_bowl_on_plate=100% |

4 个实验已完成 metrics 提取并更新 registry → DONE。`eval-obs-only-spatial-norm02-seed42` 在 registry 中不存在，需确认是否需要补建。

---
