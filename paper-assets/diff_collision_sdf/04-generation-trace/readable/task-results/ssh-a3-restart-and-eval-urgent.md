# ssh a3 restart and eval urgent

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_a3_restart_and_eval_urgent_20260521T171124_result.json`
- **Structured JSON:** [`b902e94e318cc38df82d.json`](../../sessions/b9/b902e94e318cc38df82d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个训练都正常运行。

---

## 报告

### 1. A3 spatial_bowl (cuda:0)
- **Checkpoint 可 resume**: 是，从 step 6000 resume（之前 best loss = 0.0827）
- **旧进程**: PID 164430 已杀掉（之前占着 GPU 0 但没有 --exp_name 参数的旧版进程）
- **新 PID**: 191747，tmux session `a3_spatial`
- **从 step 6001 开始**，目标 30000，~4s/step，预计 ~27 小时
- GPU 0 占用 23924 MiB，利用率 100%

### 2. A3 object_pudding (cuda:1)
- **未完成**，当前 step 29198/30000（97%）
- ~4s/step，剩余 ~802 steps ≈ 54 分钟完成
- **eval 未启动**（等训练完成后再启动）

### 3. GPU 状态
| GPU | 利用率 | 显存 | 任务 |
|-----|--------|------|------|
| 0 | 100% | 23933/24576 MiB | spatial_bowl (PID 191747) |
| 1 | 100% | 23935/24576 MiB | object_pudding (PID 165990) |

---
