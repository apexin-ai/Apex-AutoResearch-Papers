# eval mistral kl s42 analysis

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mistral_kl_s42_analysis_20260515T225044_result.json`
- **Structured JSON:** [`a4d2396331fe57e4d9c6.json`](../../sessions/a4/a4d2396331fe57e4d9c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## mistral_kl_s42 结果摘要

| 指标 | Mistral-7B-v0.3 | Llama-3.1-8B (4-seed mean) |
|------|-----------------|---------------------------|
| dense_ppl | **5.52** | 6.12 |
| predictor_hard_mask_ppl | **7.30** (1.32x) | — |
| teal_sparse_ppl | **8.98** (1.63x) | 12.00±0.07 (1.96x) |
| model_level_sparsity | 0.500 | 0.500 |

**跨架构泛化结论：成立。** Mistral-7B 在 50% sparsity 下 PPL 降级比例 (1.63x) 优于 Llama (1.96x)，KL distillation 方法对非 Llama 架构同样有效。Per-layer sparsity 分布合理——早期/晚期层稀疏度高 (~0.6)，中间层低 (~0.36-0.47)。

---
