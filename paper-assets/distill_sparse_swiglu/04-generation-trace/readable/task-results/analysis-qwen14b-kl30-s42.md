# analysis qwen14b kl30 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b_kl30_s42_20260517T144541_result.json`
- **Structured JSON:** [`bf0d895449aa1fd40cdf.json`](../../sessions/bf/bf0d895449aa1fd40cdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## qwen14b_kl30_s42 分析完成 — **conclusion: success**

### 评估结果

| 指标 | 值 |
|---|---|
| Dense PPL (WikiText-2) | 5.18 |
| Predictor Hard Mask PPL | 6.80 (1.31x) |
| TEAL Global PPL | 7.62 (1.47x) |
| 训练 Sparsity | 0.281 |
| TEAL Global Sparsity | 0.300（精确命中） |
| Final Loss | 0.3398 |
| Lambda | 5000 (cap) |
| 训练步数 | 1000/1000 |

### 关键结论

Predictor hard mask 的 PPL ratio 1.31x **优于** LLaMA-8B 的 1.47x，说明 Qwen-2.5-14B 在 30% sparsity 下对 neuron pruning 更鲁棒（可能因模型更大、冗余更多）。TEAL global 模式恰好 1.47x，与 LLaMA-8B 持平。跨架构（LLaMA→Qwen）和跨规模（8B→14B）迁移验证通过。

### 注意事项
- 层级 sparsity 分布不均匀：中间层（Layer 10-44）约 0.12-0.20，首尾层更高（Layer 0: 0.50, Layer 47: 0.73），符合预期
- 评估日志：`~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_eval.log`
- Checkpoint：`checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt`（223MB）

---
