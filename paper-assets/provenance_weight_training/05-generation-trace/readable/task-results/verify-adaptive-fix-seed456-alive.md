# verify adaptive fix seed456 alive

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_adaptive_fix_seed456_alive_20260514T151727_result.json`
- **Structured JSON:** [`0ec6ff47dfa63dc94d44.json`](../../sessions/0e/0ec6ff47dfa63dc94d44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行，验证结果：

| 检查项 | 状态 |
|--------|------|
| PID 115066 | 存活，状态 `Ss+`，已运行 33 秒 |
| GPU cuda:3 | PID 115071（子进程）占用 46514 MiB 显存 |
| 训练进度 | step 11/6103，速度 ~2.25s/it，预计 ~3h50m |
| WANDB | 无错误（已设 `WANDB_MODE=disabled`） |
| 日志 | adaptive weighting 指标正常输出，`alpha_eff` 在 0.04-0.8 范围波动，loss 在合理区间 |

训练已成功启动并稳定运行。

---
