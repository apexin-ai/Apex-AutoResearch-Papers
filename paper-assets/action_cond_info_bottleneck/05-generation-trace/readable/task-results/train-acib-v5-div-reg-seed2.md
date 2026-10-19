# train acib v5 div reg seed2

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_acib_v5_div_reg_seed2_20260516T024952_result.json`
- **Structured JSON:** [`d6cf78c1550fc6e22a65.json`](../../sessions/d6/d6cf78c1550fc6e22a65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 上已有 3 个进程：

| PID | 运行时间 | 显存 | 内容 |
|-----|---------|------|------|
| 708166 | 35 min | ~6.6GB | `lerobot-eval` baseline 评估 (libero_10) |
| 726977 | 6 min | ~16GB | `acib_v5_div_reg_seed2` 训练 (**无 wandb**) |
| 728887 | 3 min | ~16GB | `acib_v5_div_reg_seed2` 训练 (**有 wandb**) |

**问题：seed 2 训练已被启动了两次**，且都写同一个 output_dir `/root/acib/outputs/acib_v5_div_reg_seed2`，会互相覆盖 checkpoint。

建议：
1. Kill 其中一个重复的训练（保留哪个？PID 726977 无 wandb 更早启动，PID 728887 有 wandb 但更晚）
2. baseline eval (PID 708166) 看起来是独立任务，可以让它继续

需要你确认怎么处理这两个重复进程。

---
