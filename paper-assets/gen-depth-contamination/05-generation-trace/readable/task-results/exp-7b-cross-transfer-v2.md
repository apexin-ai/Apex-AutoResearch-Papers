# exp 7b cross transfer v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_7b-cross-transfer-v2_20260519T135346_result.json`
- **Structured JSON:** [`9a3801f5bd7590b50138.json`](../../sessions/9a/9a3801f5bd7590b50138.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## C4 域 7B Cross-Model Transfer Matrix 结果

数据：3 个 7B 模型 × C4 domain，每模型 30000 行（5000 docs × 6 depths），15 个共同特征。

### 3×3 Transfer Matrix (mean_pairwise_auc)

| Train \ Test | Qwen2.5-7B | LLaMA-3.1-8B | Mistral-7B |
|---|---|---|---|
| **Qwen2.5-7B** | **0.6438** | 0.6117 | 0.6272 |
| **LLaMA-3.1-8B** | 0.6299 | **0.6217** | 0.6169 |
| **Mistral-7B** | 0.6341 | 0.6067 | **0.6321** |

### Retention Rate

| Model | Diagonal | Off-diag Mean | Retention |
|---|---|---|---|
| Qwen2.5-7B | 0.6438 | 0.6195 | **96.2%** |
| LLaMA-3.1-8B | 0.6217 | 0.6234 | **100.3%** |
| Mistral-7B | 0.6321 | 0.6204 | **98.2%** |

### 1v2 AUC Transfer (early-depth, signal 最强的 pair)

| Train \ Test | Qwen2.5-7B | LLaMA-3.1-8B | Mistral-7B |
|---|---|---|---|
| Qwen2.5-7B | 0.6283 | 0.5959 | 0.5907 |
| LLaMA-3.1-8B | 0.6034 | 0.6091 | 0.5859 |
| Mistral-7B | 0.6054 | 0.5955 | 0.5919 |

### 0v1 AUC Transfer (depth 0 vs 1，区分度最高)

| Train \ Test | Qwen2.5-7B | LLaMA-3.1-8B | Mistral-7B |
|---|---|---|---|
| Qwen2.5-7B | 0.9875 | 0.9225 | 0.9757 |
| LLaMA-3.1-8B | 0.9917 | 0.9232 | 0.9492 |
| Mistral-7B | 0.9834 | 0.8961 | 0.9846 |

### vs 1.5B (80-92% retention) 对比

7B cross-model retention 为 **96.2%–100.3%**，显著高于 1.5B 的 80–92%。这表明：
- 更大模型的 contamination signature 更加 universal / model-agnostic
- OBD 特征在 7B scale 下具备极强的跨模型迁移能力，甚至 off-diagonal 有时超过 diagonal（LLaMA-3.1-8B retention 100.3%）
- 深层 depth pair（3v4, 4v5）AUC 接近 0.50（随机），transfer 退化可忽略，因为 signal 本身已消失

结果已保存至 `results/exp_7b_cross_transfer/cross_transfer_7b_c4.json`。

---
