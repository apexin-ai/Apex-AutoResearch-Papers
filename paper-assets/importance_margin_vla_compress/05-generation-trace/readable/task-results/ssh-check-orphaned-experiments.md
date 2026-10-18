# ssh check orphaned experiments

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_orphaned_experiments_20260517T013104_result.json`
- **Structured JSON:** [`fb1ef93ce45ec4431a37.json`](../../sessions/fb/fb1ef93ce45ec4431a37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

| GPU | 实验 | 状态 | 详情 |
|-----|------|------|------|
| **0** | libero_fullft_seed1 | **运行中** | PID 45551, 启动 05:34, step 59200/100000, loss~0.08, sps=4.2. 剩余 40800 步 ≈ 2.7h 后完成 (~12:12) |
| **1** | fullft_batch64 | **运行中** | PID 124908 (已确认), 2727MiB |
| **2** | libero_imm_fullft_seed0 | **已死** | GPU 显存 0MiB, 无进程, 无 tmux session |
| **3** | libero_imm_fullft_k07 | **运行中** | PID 117885, 启动 07:17, stage2 step 17700/20000, loss~0.23, sps=3.1. 剩余 2300 步 ≈ 12min 后完成 (~09:43) |

关键发现：
- GPU 2 的 `libero_imm_fullft_seed0` 确实已死（无进程、无 tmux、无显存占用），reconciliation 标记正确
- GPU 0 和 GPU 3 的实验仍在正常运行，reconciliation 误判为 failed，需要恢复其跟踪状态

---
