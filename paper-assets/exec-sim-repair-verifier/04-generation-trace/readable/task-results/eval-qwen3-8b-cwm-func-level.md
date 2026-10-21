# eval qwen3 8b cwm func level

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen3-8b-cwm-func-level_20260516T101005_result.json`
- **Structured JSON:** [`22cf279d3cbe76efb768.json`](../../sessions/22/22cf279d3cbe76efb768.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：Qwen3-8B CWM func-level checkpoint 不存在。**

服务器上所有 CWM checkpoint 情况：

| 路径 | 模型 | 级别 |
|------|------|------|
| `checkpoints_repo_cwm_8b_conda` | Qwen3-8B | repo-level |
| `checkpoints_backup_cwm_8b` | Qwen3-8B | repo-level |
| `checkpoints_deepseek_cwm_func` | DeepSeek | func-level |
| `checkpoints_deepseek_cwm_func_seed123` | DeepSeek | func-level |

唯一的 func-level CWM 都是 DeepSeek 的。Qwen3-8B 只有 repo-level CWM（已跑过 eval，accuracy=65.17%）。

**从未训练过 Qwen3-8B func-level CWM。** 如果论文对比表需要这个数据点，需要用 func-level CWM 训练数据重新训练一个 Qwen3-8B LoRA adapter。训练数据应该已有（DeepSeek 用的同一份），只是没在 8B 上跑过。

---
