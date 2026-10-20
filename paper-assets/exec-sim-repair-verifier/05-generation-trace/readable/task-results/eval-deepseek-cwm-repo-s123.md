# eval deepseek cwm repo s123

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_deepseek-cwm-repo-s123_20260517T161324_result.json`
- **Structured JSON:** [`089a6d032714e5327c48.json`](../../sessions/08/089a6d032714e5327c48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练仍在运行，未退出。当前状态：

- **训练进度**: step 9496/13266 (71.5%), epoch ~2.15
- **eval_loss at step 8844 (epoch 2.0)**: **nan** — 这可能有问题
- **GPU 3**: 99% utilization, 18052 MiB — 被训练占用
- **GPU 1, 2**: 空闲 (0%, 0 MiB)

checkpoint-8844 存在且完整（有 adapter_model.safetensors）。

**问题**: GPU 3 被训练进程占用，无法在上面跑 eval。选项：

1. **杀训练，在 GPU 3 上 eval checkpoint-8844** — 训练 eval_loss=nan 可能意味着后续 checkpoint 也没用
2. **在 GPU 1 或 2 上 eval checkpoint-8844** — 不影响训练继续
3. **等训练跑完再 eval** — 还剩 ~8.4 小时

建议选 2，在空闲 GPU 上 eval，同时不干扰训练。怎么处理？

---
