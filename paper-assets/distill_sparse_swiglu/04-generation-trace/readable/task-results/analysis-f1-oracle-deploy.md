# analysis f1 oracle deploy

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_f1_oracle_deploy_20260517T073603_result.json`
- **Structured JSON:** [`8b47765840c61406509c.json`](../../sessions/8b/8b47765840c61406509c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果确认了预期的 structural mismatch：

**F1 vs Oracle Magnitude Mask (top-50%)**

| Predictor | F1 | Precision | Recall |
|-----------|------|-----------|--------|
| **BCE** | **0.6128** | 0.6132 | 0.6124 |
| KL | 0.5397 | 0.5112 | 0.5715 |
| Random | 0.5000 | 0.5000 | 0.5000 |

关键发现：
- **BCE F1 (0.613) > KL F1 (0.540)**：BCE 在逐 neuron 预测 oracle mask 上确实更准确（+7.3 pp）
- **KL precision 极低（0.511）**：KL 几乎退化为"保留所有 neuron"策略（recall 0.572 > precision 0.511），说明 KL loss 不鼓励精确匹配 oracle mask，而是通过 output distribution 间接学习
- Per-layer 模式：BCE 在中间层(3-13) F1 最高(~0.65)，后期层逐渐下降；KL 在 layer 4-9 表现最差（F1 < 0.46）

这验证了论文的核心论点：**BCE 以更高的 per-neuron mask accuracy 达到了更差的 PPL（22.51 vs 11.79）**，因为 oracle magnitude mask 本身不是 output-distribution-optimal 的选择。

输出已保存至 `/root/distill_sparse_swiglu/artifacts/kl_bce_f1_oracle.json`。

---
