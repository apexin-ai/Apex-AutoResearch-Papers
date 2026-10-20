# fix adaptive fix seed42 resubmit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_adaptive_fix_seed42_resubmit_20260514T142038_result.json`
- **Structured JSON:** [`06a1a56ffe6eb4eb7f21.json`](../../sessions/06/06a1a56ffe6eb4eb7f21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验 adaptive_fix_seed42 正在正常运行，不需要重新提交。**

实际状态：
- PID 108208 仍然存活（bash wrapper 进程）
- PID 108213 是实际的 python 训练进程，运行在 GPU 1 上，占用 46514 MiB 显存
- GPU 1 利用率 99%
- 训练进度：step 150/6103 (2%)，速度 ~2.22s/it，预计剩余约 3 小时 40 分钟
- 日志中无 wandb 报错，训练指标正常输出（loss、weighting 参数等）

wandb 错误可能只是一个非致命警告，训练本身并未中断。无需执行任何清理或重新提交操作。

---
