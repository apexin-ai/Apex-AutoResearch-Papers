# analysis mistral kl s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mistral_kl_s42_20260515T225403_result.json`
- **Structured JSON:** [`3600eac53686c9a7ebde.json`](../../sessions/36/3600eac53686c9a7ebde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry already has complete results (populated by the on_complete hook). All data verified against the logs and evaluation I ran independently.

## mistral_kl_s42 结果

### 训练指标
| Metric | Value |
|--------|-------|
| Final loss | 0.2188 |
| Final sparsity | 0.480 |
| Final lambda | 1000.00 |
| Final tau | 0.100 |
| Steps | 1000/1000 |
| EXIT_CODE | 0 |

### WikiText-2 PPL 评估 (50% sparsity)

| Metric | Mistral-7B | Llama-3.1-8B (4-seed mean) |
|--------|-----------|---------------------------|
| true_dense_ppl | **5.52** | 6.12 |
| predictor_hard_mask_ppl | **7.30** (1.32x) | — |
| teal_sparse_ppl | **8.98** (1.63x) | 12.00±0.07 (1.96x) |
| model_level_sparsity | 0.500 | 0.500 |

### 结论：**Claim 4 确认** (cross-architecture generalization)

- PPL 8.98 远低于 15 的阈值
- Mistral 绝对 PPL 更低（8.98 vs 12.00），降级比例也更小（1.63x vs 1.96x）
- Per-layer sparsity 分布合理：前后层高（~0.6），中间层低（~0.36-0.47）
- Registry 已更新：status=DONE, conclusion=success

---
