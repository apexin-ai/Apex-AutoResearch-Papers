# ops gpu check bjb2 28827

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check-bjb2-28827_20260518T151327_result.json`
- **Structured JSON:** [`ffeb45d1e57402e43cd9.json`](../../sessions/ff/ffeb45d1e57402e43cd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态总览 (bjb2-28827)

| GPU | 显存占用 | 利用率 | 状态 | 进程 / tmux session |
|-----|---------|--------|------|---------------------|
| **0** | 1905 / 24564 MiB | 17% | 占用 | `evaluate.py --mode random_selection --seed 43` / `eval-random-selection-object-seed43` |
| **1** | 7138 / 24564 MiB | 99% | 占用(双进程) | PID 497445: `evaluate.py --mode crm_obs_only --seed 42 --norm 0.1` / `eval-obs-only-norm01-s42`; PID 578945: `evaluate.py --mode crm_obs_only --seed 45 --norm 0.1` / `eval-obs-only-object-norm01-seed45-r2` |
| **2** | 4736 / 24564 MiB | 19% | 占用 | `evaluate.py --mode crm_obs_only --seed 44 --K 5 --norm 0.2` / `eval-obs-only-object-norm02-k5-seed44` |
| **3** | 5201 / 24564 MiB | 19% | 占用 | `evaluate.py --mode crm_obs_only --seed 45 (default norm)` / `eval-obs-only-object-default-seed45-r2` |
| **4** | 1905 / 24564 MiB | 19% | 占用 | `evaluate.py --mode random_selection --seed 44` / `eval-random-selection-object-seed44` |
| **5** | 1 / 24564 MiB | 0% | **空闲** | 无进程 |

### 空闲 GPU 列表

**仅 GPU 5 空闲。** 其余 GPU 0-4 全部在跑 evaluation 任务（共 6 个 eval 进程分布在 5 张卡上，GPU 1 跑了两个）。

另外注意：ps 中还有一个 `train-crm-k1-v2` 的 tmux session（PID 447916），指定了 `CUDA_VISIBLE_DEVICES=0`，但该训练进程未出现在 nvidia-smi 的 GPU 进程列表中，可能已结束但 tmux session 未被 `tmux ls` 列出（或已退出）。

---
