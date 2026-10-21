# ops check plan a spatial seed42 43

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-plan-a-spatial-seed42-43_20260520T235331_result.json`
- **Structured JSON:** [`36dd358252e766e0f0bd.json`](../../sessions/36/36dd358252e766e0f0bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，JSON 完整。结果如下：

## eval-plan-a-spatial-seed42
- **文件**: `/root/acr-vla-conformal-refinement/logs/eval_plan_a_spatial_seed42.json`
- **SR%**: **34.0%** (34/100)
- **trigger_rate**: 97.60%
- **mean_uncertainty**: 0.2679
- **tau**: 0.074855
- **n_rollouts**: 10 × 10 tasks = 100
- **完成状态**: **success** ✓

## eval-plan-a-spatial-seed43
- **文件**: `/root/acr-vla-conformal-refinement/logs/eval_plan_a_spatial_seed43.json`
- **SR%**: **35.0%** (35/100)
- **trigger_rate**: 97.96%
- **mean_uncertainty**: 0.2619
- **tau**: 0.074855
- **n_rollouts**: 10 × 10 tasks = 100
- **完成状态**: **success** ✓

## GPU 状态 (bjb1-32546)

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 2 MiB / 24564 MiB | 0% | **空闲** |
| 1 | 2 MiB / 24564 MiB | 0% | **空闲** |
| 2 | 5731 MiB / 24564 MiB | 37% | 占用 |
| 3 | 2008 MiB / 24564 MiB | 32% | 占用 |
| 4 | 2008 MiB / 24564 MiB | 28% | 占用 |
| 5 | 2008 MiB / 24564 MiB | 28% | 占用 |

GPU 0 和 GPU 1（之前跑 seed42/43 的卡）已完全释放，空闲可用。GPU 2-5 有其他任务在跑。

---
