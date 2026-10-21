# eval bce isocompute v2 teal

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_bce_isocompute_v2_teal_20260515T211005_result.json`
- **Structured JSON:** [`9a4f6a28871b51b1f8c9.json`](../../sessions/9a/9a4f6a28871b51b1f8c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 评估结果汇总

**bce_isocompute_v2_s42** (BCE loss, reg_weight=2.0, 1000 steps, sparsity≈0.50):

| 指标 | 值 |
|------|------|
| true_dense_ppl | 6.12 |
| predictor_hard_mask_ppl | **26.76** |
| teal_sparse_ppl | **54.84** |
| model_level_sparsity | 0.493 |

**Iso-compute 对比 (seed=42, 1000 steps)**:

| 方案 | hard_mask_ppl | teal_sparse_ppl |
|------|-------------|----------------|
| KL-only | **9.19** | **11.91** |
| BCE iso-compute v2 | 26.76 | 54.84 |

BCE 方案在 iso-compute 条件下 PPL 显著劣于 KL，差距约 3x (hard_mask) 和 4.6x (teal_sparse)。

---
