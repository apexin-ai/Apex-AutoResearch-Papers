# ops mask divergence 30pct recovery

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mask-divergence-30pct-recovery_20260519T131552_result.json`
- **Structured JSON:** [`e46bf50d3befbf2397e2.json`](../../sessions/e4/e46bf50d3befbf2397e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态：已完成。** 进程 PID 107986 已运行结束，结果已保存。

### 结果摘要

| 指标 | 值 |
|------|-----|
| Mean Jaccard distance | **0.3902** |
| Std | 0.0336 |
| Max | 0.4810 (layer 0) |
| Min | 0.3516 (layer 14) |

### Per-layer pattern

- **前 8 层（0-7）Jaccard 最高**：均值 0.4402，mask 分歧最大，predictor 和 magnitude 选择的神经元重叠度最低
- **中间层（8-23）最稳定**：均值 ~0.371，mask 分歧最小
- **后 8 层（24-31）略回升**：均值 0.378

### 其他观察

- `per_layer_kl_retention` 所有层恒定为 0.7000（predictor 精确保留 70% 激活 = 30% sparsity）
- `per_layer_mag_retention` 在 0.700-0.720 之间轻微波动，说明 magnitude pruning 的实际保留率与 KL predictor 接近但不完全一致

整体 Jaccard ~0.39 意味着 predictor 和 magnitude-based mask 在 30% sparsity 下约有 **61% 的神经元选择一致**，前几层分歧最大（可能因为 embedding-adjacent 层的激活分布更复杂）。

---
