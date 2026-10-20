# ops find random reweight pid

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_find-random-reweight-pid_20260516T072342_result.json`
- **Structured JSON:** [`31bfe7110b03b8eda4e3.json`](../../sessions/31/31bfe7110b03b8eda4e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**PID: 310180** — `python training/pretrain_weighted.py`（实际训练进程），运行在 **GPU 2**（`CUDA_VISIBLE_DEVICES=2`）。

进程树：
- PID 310172: 外层 bash（启动 wrapper）
- PID 310177: `bash scripts/run_random_reweight_seed42.sh`
- PID 310180: `python training/pretrain_weighted.py ...`（训练主进程）

当前进度：**58/6103 steps (1%)**，速度 ~2.12s/step，预计剩余 ~3h33m。注意 `WANDB_MODE=offline`，wandb 离线记录。

---
