# exp d046 collect eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_d046_collect_eval_20260517T065549_result.json`
- **Structured JSON:** [`6ad90a94e3bf376d68f6.json`](../../sessions/6a/6ad90a94e3bf376d68f6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果汇总：

| Method | PPL (WikiText-2) | vs Forward KL | Sparsity |
|---|---|---|---|
| Forward KL | 11.79 | baseline | 0.50 |
| Reverse KL | 12.80 | +1.01 (+8.6%) | 0.50 |
| JSD | 12.54 | +0.75 (+6.4%) | 0.50 |

**关键发现**：
- **Forward KL 仍然是最优的**，PPL 11.79
- **JSD 次优**，PPL 12.54，比 Forward KL 高 0.75（+6.4%）
- **Reverse KL 最差**，PPL 12.80，比 Forward KL 高 1.01（+8.6%）

两个替代损失函数都未能超越 Forward KL baseline。JSD 比 Reverse KL 略好（12.54 vs 12.80），但两者都明显逊于 Forward KL。

层级 sparsity 分配上，两者都达到了目标的 model-level 0.500 sparsity，但层分配模式有差异（JSD 的中间层 sparsity 更低，例如 Layer 25 仅 0.344 vs Reverse KL 的 0.512）。

---
