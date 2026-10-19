# eval kl sparsity70 v2 ppl

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_kl_sparsity70_v2_ppl_20260515T221311_result.json`
- **Structured JSON:** [`c03f00ff44a7a659ad83.json`](../../sessions/c0/c03f00ff44a7a659ad83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

## kl_sparsity70_s42_v2 PPL 评估结果

| Metric | Value |
|--------|-------|
| true_dense_ppl | 6.12 |
| **predictor_hard_mask_ppl** | **13.84** |
| teal_sparse_ppl | 136,069.61 (broken) |
| model_level_sparsity | 0.699 |

## 70% vs 50% Sparsity 对比

| | 50% KL (4-seed mean) | 70% KL (seed 42) |
|--|--|--|
| PPL | 12.00 ± 0.07 | 13.84 |
| PPL degradation vs dense | +5.88 (+96%) | +7.72 (+126%) |

**关键发现：**
- 70% sparsity 的 predictor hard mask PPL (13.84) 仅比 50% (12.00) 高 15%，说明 KL predictor 在高稀疏度下仍能有效分配 neuron budget
- Static global topk (teal_sparse) 在 70% sparsity 下完全失效——per-layer sparsity 分布极不均匀 (0.508–0.876)，late layers (L25-28) 被过度剪枝至 85%+ 导致 PPL 爆炸。这表明 70% sparsity 下 **必须用 per-token adaptive masking**，static allocation 不可行

---
