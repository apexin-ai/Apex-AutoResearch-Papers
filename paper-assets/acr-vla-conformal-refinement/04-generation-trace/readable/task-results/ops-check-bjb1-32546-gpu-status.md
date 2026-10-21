# ops check bjb1 32546 gpu status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-bjb1-32546-gpu-status_20260518T164850_result.json`
- **Structured JSON:** [`0c43425bef07ada59ced.json`](../../sessions/0c/0c43425bef07ada59ced.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 张 GPU 均双跑满载（98-99% util）。每张 GPU 上 2 个 eval 进程：

### GPU 0 — 10862 MiB / 24564 MiB

| PID | tmux session | 实验 | 显存 |
|---|---|---|---|
| 651466 | eval-obs-only-object-norm003-seed44 | crm_obs_only, norm=0.03, seed44 | 5182 MiB |
| 662825 | eval-perdof-object-norm005-seed46 | crm_perdof, norm=0.05, seed46 | 5645 MiB |

### GPU 1 — 10397 MiB / 24564 MiB

| PID | tmux session | 实验 | 显存 |
|---|---|---|---|
| 642305 | eval-perdof-object-norm005-seed43 | crm_perdof, norm=0.05, seed43 | 4717 MiB |
| 663022 | eval-obs-only-object-default-seed47 | crm_obs_only, default norm, seed47 | 5645 MiB |

### GPU 2 — 10397 MiB / 24564 MiB

| PID | tmux session | 实验 | 显存 |
|---|---|---|---|
| 640624 | eval-perdof-object-norm003-seed43 | crm_perdof, norm=0.03, seed43 | 4717 MiB |
| 663285 | eval-perdof-object-norm03-seed46 | crm_perdof, norm=0.3, seed46 | 5645 MiB |

### GPU 3 — 10381 MiB / 24564 MiB

| PID | tmux session | 实验 | 显存 |
|---|---|---|---|
| 651806 | eval-obs-only-object-norm003-seed45 | crm_obs_only, norm=0.03, seed45 | 4711 MiB |
| 663550 | eval-obs-only-object-norm03-seed46 | crm_obs_only, norm=0.3, seed46 | 5645 MiB |

### GPU 4 — 9465 MiB / 24564 MiB

| PID | tmux session | 实验 | 显存 |
|---|---|---|---|
| 626277 | eval_perdof_default_seed45 | crm_perdof, default norm, seed45 | 3785 MiB |
| 663877 | eval-scalar-object-seed46 | crm_scalar, norm=0.1, seed46 | 5645 MiB |

### GPU 5 — 10862 MiB / 24564 MiB

| PID | tmux session | 实验 | 显存 |
|---|---|---|---|
| 652415 | eval-perdof-object-norm003-seed45 | crm_perdof, norm=0.03, seed45 | 5182 MiB |
| 664271 | eval-obs-only-object-norm01-seed47 | crm_obs_only, norm=0.1, seed47 | 5645 MiB |

---

**关于你关注的两张卡：**
- **cuda:0**: 确认 eval-obs-only-object-norm003-seed44 (PID 651466) 仍在跑，双跑 Worker 加上了 eval-perdof-object-norm005-seed46 (PID 662825)
- **cuda:3**: 确认 eval-obs-only-object-norm003-seed45 (PID 651806) 仍在跑，双跑 Worker 加上了 eval-obs-only-object-norm03-seed46 (PID 663550)（不是 norm03-seed46 perdof，而是 obs_only）

另有 1 个无 GPU 进程的 tmux session: `eval-dc-r2`（创建于 5/17，可能已完成）。

---
