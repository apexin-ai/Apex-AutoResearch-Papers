# eval check 8b multiseed status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check_8b_multiseed_status_20260518T002629_result.json`
- **Structured JSON:** [`cc8030c0bfcd48d8502b.json`](../../sessions/cc/cc8030c0bfcd48d8502b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功启动并正在训练：

| 实验 | PID | GPU | 显存 | 状态 |
|------|-----|-----|------|------|
| s123 | 34700 | cuda:0 | 18284 MiB | 训练中 (model loaded) |
| s456 | 35045 | cuda:1 | 18284 MiB | 训练中 (model loaded) |

**失败原因**：原始提交时 `source /root/miniconda3/bin/activate base` 未生效，系统默认 python 没有 wandb。本次通过 `export PATH=/root/miniconda3/bin:$PATH` 前置修复。

**预计时间线**：
- 训练 ~45 min → 完成约 09:15 UTC
- Eval ~2-3h → 全部完成约 11:30-12:30 UTC

---
