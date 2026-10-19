# eval kl30 s123 uniform

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_kl30_s123_uniform_20260517T125234_result.json`
- **Structured JSON:** [`1c23bfbaffa26445b3de.json`](../../sessions/1c/1c23bfbaffa26445b3de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均已成功启动：

| 任务 | GPU | 显存占用 | PID | 日志 |
|------|-----|---------|-----|------|
| `kl30_s123_eval` (uniform eval) | cuda:0 | 15,879 MiB | 42019 | `~/runs/distill_sparse_swiglu/kl30_s123_eval.log` |
| `kl30_s456_train` (KL训练) | cuda:1 | 加载中 | 42092 | `~/runs/distill_sparse_swiglu/kl30_s456_train.log` |

cuda:0 eval 已在加载模型（~16GB），cuda:1 train 刚启动正在初始化。双卡并行运行中，无冲突。

---
