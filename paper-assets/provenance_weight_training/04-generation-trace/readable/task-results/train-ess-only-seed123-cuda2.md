# train ess only seed123 cuda2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_ess_only_seed123_cuda2_20260517T152741_result.json`
- **Structured JSON:** [`cff15d658cbb86196c4d.json`](../../sessions/cf/cff15d658cbb86196c4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动在 cuda:2 上。

**结果汇总：**
- cuda:1: 0MiB，无残留进程
- cuda:2: 46539MiB，PID **115021**，GPU-Util 100%
- tmux session: `ess_only_seed123` 运行中
- 训练速度: **~2.16s/it**，预计总时长 ~3h40m (6103 steps)
- 脚本修复：删除了GPU等待逻辑、修复 save_steps 200→500（需与 eval_steps=500 对齐）、添加 `WANDB_MODE=disabled`（该服务器无 wandb 凭证）

---
