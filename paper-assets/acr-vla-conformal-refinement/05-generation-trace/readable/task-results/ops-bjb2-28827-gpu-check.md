# ops bjb2 28827 gpu check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb2-28827-gpu-check_20260519T134318_result.json`
- **Structured JSON:** [`3ed733602682f35806ca.json`](../../sessions/3e/3ed733602682f35806ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb2-28827 GPU 状态

| GPU | 显存占用 | GPU利用率 | 状态 | 实验 |
|-----|---------|----------|------|------|
| **0** | 1 MiB / 24564 MiB | 0% | **空闲** | 无（train-crm-k1-v2 tmux 存在但进程未占 GPU） |
| **1** | 2839 MiB | 16% | 占用 | argmin object K=5 seed44 (PID 758237) |
| **2** | 2375 MiB | 19% | 占用 | random_selection object seed46 K=10 (PID 693631) |
| **3** | 2006 MiB | 19% | 占用 | crm_obs_only spatial seed44 K=10 norm0.2 (PID 697045) |
| **4** | 6206 MiB | 17% | 占用 | vla_only spatial seed44 (PID 835816, 刚启动 ~45min) |
| **5** | 1 MiB / 24564 MiB | 0% | **空闲** | 无 |

### 活跃 tmux sessions (4个)
- `eval-argmin-object-k5-seed44` → GPU 1
- `eval-random-seed46-t16` → GPU 2
- `eval-spatial-obs-only-norm02-seed44` → GPU 3
- `eval-vla-only-spatial-seed44` → GPU 4

### perdof norm005 seed45
**未在 bjb2-28827 上运行**，ps 和 tmux 中均无相关进程。

### 可用 GPU
**GPU 0 和 GPU 5 空闲**，可立即部署新实验。2 张卡可同时跑 2 个评估任务。

---
