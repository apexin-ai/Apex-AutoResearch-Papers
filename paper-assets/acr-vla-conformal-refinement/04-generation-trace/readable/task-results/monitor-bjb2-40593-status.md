# monitor bjb2 40593 status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_bjb2-40593-status_20260515T044929_result.json`
- **Structured JSON:** [`1bd1f04cad7639be4137.json`](../../sessions/1b/1bd1f04cad7639be4137.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-40593 Status

| Experiment | Mode | Progress | Current SR | Status |
|---|---|---|---|---|
| eval-acr-spatial-v4-default-r3 | acr_vla, spatial | Task 1, rollout 5/10 | 0/5 (0%) | **killed** (EXIT_CODE=143, 2026-05-15T03:10:02Z) |
| eval-reconvla-object | reconvla, object, K=10, n=20 | Task 1, rollout 10/20 | 0/10 (0%) | **running** (since 09:48, ~3h) |

### 详细信息

**eval-acr-spatial-v4-default-r3**: 已被 kill（SIGTERM），停在第1个task `pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate` 的 rollout 5/10。无结果输出。

**eval-reconvla-object**: 正在运行，当前在第1个task `pick_up_the_alphabet_soup_and_place_it_in_the_basket`，完成 10/20 rollouts，成功率 0/10。GPU 占用 5573MiB / 24564MiB，GPU-Util 11%。进度较慢——3小时仅完成1个task的一半（共10个tasks × 20 rollouts = 200 rollouts）。

### 已有结果文件

- `eval-vla-mean-spatial-t10.json`: vla_only + mean baseline, spatial benchmark, n=10, **overall SR = 10%**（仅1个task有结果：`pick_up_the_black_bowl_on_the_wooden_cabinet` 1/10）

---
