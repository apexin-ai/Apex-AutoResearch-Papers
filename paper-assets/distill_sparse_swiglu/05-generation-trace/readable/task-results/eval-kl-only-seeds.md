# eval kl only seeds

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_kl_only_seeds_20260515T180042_result.json`
- **Structured JSON:** [`f81692e184313fe91e16.json`](../../sessions/f8/f81692e184313fe91e16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s1 评估完成！

**kl_only_s1:**
- true_dense: 6.12
- predictor (hard mask): 9.15
- teal_predictor (sparse): 11.99
- model sparsity: 0.498

现在汇总 5-seed 统计：

| Metric | s0 | s1 | s42 | s123 | s456 | Mean | Std |
|--------|----|----|-----|------|------|------|-----|
| true_dense_ppl | 6.12 | 6.12 | - | - | - | 6.12 | 0.00 |
| predictor_hard_mask_ppl | 9.19 | 9.15 | 9.21 | 9.25 | 9.14 | 9.19 | 0.04 |
| teal_sparse_ppl | 12.03 | 11.99 | 12.08 | 11.91 | 13.58 | 12.32 | 0.69 |
| model_level_sparsity | 0.499 | 0.498 | 0.498 | 0.498 | 0.498 | 0.498 | 0.000 |

PPL increase vs true dense:
- predictor_hard_mask: (9.19/6.12 - 1) × 100 = **50.2%** mean
- teal_sparse: (12.32/6.12 - 1) × 100 = **101.3%** mean

注意：s456 的 teal_sparse_ppl (13.58) 是明显的 outlier，拉高了 mean 和 std。去掉它后 4-seed mean = 12.00 ± 0.09。

需要确认 3-seed 的 true_dense_ppl 是否也是 6.12——它是同一个基模型，应该相同（评估时基模型不变，只是 predictor 不同）。

---
