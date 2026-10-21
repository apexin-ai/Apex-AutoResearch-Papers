# ssh a3 spa check and restart

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a3_spa_check_and_restart_20260521T091356_result.json`
- **Structured JSON:** [`5af2419d3df7fa5a3fc1.json`](../../sessions/5a/5af2419d3df7fa5a3fc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行，无需操作。

## 状态报告

### 1. spatial_bowl (GPU 0)
- **PID 164420**: DEAD（旧 bash wrapper）
- **PID 164430**: ALIVE，已从头重启（无 --resume），运行 ~10 分钟
- **当前 step**: **138/30000**，loss ~0.26-0.28，lr=3.45e-06
- 速度: ~3.5s/step，预计 ~29 小时完成

### 2. object_pudding (GPU 1)
- **PID 165984/165990**: ALIVE，从 step 22000 resume
- **当前 step**: **22119/30000**，loss ~0.027-0.035，lr=6.36e-06
- 速度: ~4.0s/step，预计 ~8.8 小时完成剩余 ~7880 steps

### 3. GPU 状态
| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| 0 | 100% | 16907 MiB | PID 164430 (spatial_bowl) |
| 1 | 100% | 23935 MiB | PID 165990 (object_pudding) |

### 结论
spatial_bowl 已被前一个 Worker 重启（从 step 0 开始，无 --resume），当前正常训练中。无需任何操作。

---
