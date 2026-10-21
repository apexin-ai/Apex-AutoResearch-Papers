# analyze pi05 baseline r3 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_pi05-baseline-r3-batch_20260521T121613_result.json`
- **Structured JSON:** [`fbc0f074302e418b5704.json`](../../sessions/fb/fbc0f074302e418b5704.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正常完成，无错误。日志中无 W&B run ID。

## 结果汇总

| exp_id | benchmark | seed | overall_sr | per_task_sr | wandb_run_id | errors |
|--------|-----------|------|-----------|-------------|--------------|--------|
| eval-pi05-vla-only-object-seed42-r3 | object | 42 | **82.0%** (164/200) | [85,100,60,80,80,55,100,80,100,80] | N/A | 无 |
| eval-pi05-vla-only-object-seed43-r3 | object | 43 | **81.5%** (163/200) | [80,95,70,85,80,60,95,80,100,70] | N/A | 无 |
| eval-pi05-vla-only-object-seed44-r3 | object | 44 | **81.0%** (162/200) | [85,95,65,80,85,55,90,85,100,70] | N/A | 无 |
| eval-pi05-vla-only-spatial-seed42-r3 | spatial | 42 | **84.5%** (169/200) | [95,90,100,90,75,25,100,90,90,90] | N/A | 无 |

**Object benchmark 跨 seed 均值: 81.5% ± 0.5%**

## 每个实验的详细 per-task 结果

### Object benchmark (seed 42 / 43 / 44)

| Task | seed42 | seed43 | seed44 | Mean |
|------|--------|--------|--------|------|
| alphabet_soup | 85% (17/20) | 80% (16/20) | 85% (17/20) | 83.3% |
| cream_cheese | 100% (20/20) | 95% (19/20) | 95% (19/20) | 96.7% |
| salad_dressing | 60% (12/20) | 70% (14/20) | 65% (13/20) | 65.0% |
| bbq_sauce | 80% (16/20) | 85% (17/20) | 80% (16/20) | 81.7% |
| ketchup | 80% (16/20) | 80% (16/20) | 85% (17/20) | 81.7% |
| tomato_sauce | 55% (11/20) | 60% (12/20) | 55% (11/20) | 56.7% |
| butter | 100% (20/20) | 95% (19/20) | 90% (18/20) | 95.0% |
| milk | 80% (16/20) | 80% (16/20) | 85% (17/20) | 81.7% |
| chocolate_pudding | 100% (20/20) | 100% (20/20) | 100% (20/20) | 100.0% |
| orange_juice | 80% (16/20) | 70% (14/20) | 70% (14/20) | 73.3% |

### Spatial benchmark (seed 42)

| Task | SR |
|------|-----|
| between_plate_and_ramekin | 95% (19/20) |
| next_to_ramekin | 90% (18/20) |
| from_table_center | 100% (20/20) |
| on_cookie_box | 90% (18/20) |
| in_top_drawer | 75% (15/20) |
| on_ramekin | **25%** (5/20) |
| next_to_cookie_box | 100% (20/20) |
| on_stove | 90% (18/20) |
| next_to_plate | 90% (18/20) |
| on_wooden_cabinet | 90% (18/20) |

**Notable**: Object benchmark 中 `tomato_sauce` (56.7%) 和 `salad_dressing` (65.0%) 是最弱 task；Spatial benchmark 中 `on_ramekin` (25%) 显著低于其他 task。

---
