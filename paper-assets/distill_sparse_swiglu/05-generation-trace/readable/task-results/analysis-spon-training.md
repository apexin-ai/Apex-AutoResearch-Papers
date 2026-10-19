# analysis spon training

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_spon_training_20260515T181242_result.json`
- **Structured JSON:** [`5e6e6ebd94ca864f207f.json`](../../sessions/5e/5e6e6ebd94ca864f207f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## SPON Training 实验结果

### 训练指标
- 1000 步训练，loss 在 0.38~0.48 间波动，无明显下降趋势
- Bias norm 在 ~step 700 饱和于 0.0406，后续步骤无变化
- SPON 参数量极小：458,752 / 8B（0.0057%）

### WikiText-2 评估结果（50% sparsity）

| Metric | No SPON | With SPON | Delta |
|---|---|---|---|
| true_dense_ppl | 6.12 | 6.19 | +0.08 |
| predictor_hard_mask_ppl | 9.21 | 9.09 | **-0.12** |
| teal_sparse_ppl | 12.15 | 11.93 | **-0.22** |
| ppl_increase (pred/dense) | 50.6% | 46.8% | -3.8pp |
| ppl_increase (teal/dense) | 98.6% | 92.5% | -6.1pp |

### 结论：**SUCCESS (marginal)**

SPON bias vectors 在稀疏推理上提供小幅但一致的 PPL 改善：
- Predictor hard mask: -0.12 PPL（1.3% 相对改善）
- TEAL sparse: -0.22 PPL（1.8% 相对改善）
- Dense 惩罚: +0.08 PPL（可接受）

改善幅度较小，可能因为 bias-only 参数化表达力有限，且 bias norm 在训练中较早饱和。效果方向正确，可推进 plan_005 composition experiment，但 SPON 在最终 pipeline 中的贡献可能偏 marginal。

---
