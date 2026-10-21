# check traj v2 status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_traj-v2-status_20260516T141512_result.json`
- **Structured JSON:** [`8d936886ccb18503d567.json`](../../sessions/8d/8d936886ccb18503d567.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DeepSeek TRAJ v2 训练状态报告

### 实验 1: `deepseek-traj-func-v2` (seed 42)

| 项目 | 值 |
|------|-----|
| **状态** | ✅ **Completed** |
| PID 511676 | 已退出 |
| best_eval_loss | **0.0891** |
| train_loss | 0.0857 |
| train_runtime | 3069.6s (~51 min) |
| best_step | 756/756 (epoch 3 结束时) |
| checkpoint 路径 | `/root/autodl-tmp/checkpoints_deepseek_traj_v2/best` |
| 所有 checkpoints | `checkpoint-504`, `checkpoint-756`, `best` |

### 实验 2: `deepseek-traj-func-v2-s123` (seed 123)

| 项目 | 值 |
|------|-----|
| **状态** | 🔄 **Running** (epoch 2→3 过渡中) |
| PID 513115 | 存活，已运行 37 min |
| 当前进度 | 555/756 steps (73%) |
| epoch 2 eval_loss | **0.0770** |
| 估计剩余时间 | ~13 min |
| checkpoint 路径 | `/root/autodl-tmp/checkpoints_deepseek_traj_v2_s123/` |
| 当前 checkpoints | `checkpoint-252`, `checkpoint-504` |

### GPU 利用率

| GPU | Util | VRAM |
|-----|------|------|
| 0 | 99% | 19.6 / 32.6 GB |
| 1 | 99% | 19.7 / 32.6 GB |
| 2 | 100% | 23.8 / 32.6 GB |
| 3 | 98% | 18.3 / 32.6 GB |

4 张卡全部满载。GPU 2 (VRAM 最高) 可能是 s123 实验所在的 cuda:3 对应物理卡，GPU 0/1 在跑其他任务。

### 备注
- s123 的 epoch 2 eval_loss (0.0770) 比 seed 42 的最终 eval_loss (0.0891) 更低，预计最终结果会更好
- s123 预计约 13 分钟后完成

---
