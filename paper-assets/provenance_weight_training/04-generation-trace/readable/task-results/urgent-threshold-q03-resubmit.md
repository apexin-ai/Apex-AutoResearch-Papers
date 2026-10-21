# urgent threshold q03 resubmit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_threshold-q03-resubmit_20260516T053759_result.json`
- **Structured JSON:** [`cdc6d5a907d44a76362b.json`](../../sessions/cd/cdc6d5a907d44a76362b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成，训练正常运行。

**失败原因**：wandb API key 未配置，`--use_wandb` 导致 `wandb.init()` 报错退出。

**修复内容**：在脚本中加 `export WANDB_MODE=offline`，wandb 日志保存到本地，不需要 API key。

**当前状态**：
- PID: **299248**（存活）
- 训练已开始：1/6103 steps，预估约 4h40m
- cuda:3 已占用（46523 MiB）
- 日志正常写入，Training Config 正确（116935 examples, max_steps=6103）

---
