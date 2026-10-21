# eval kl only s0 fix

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_kl_only_s0_fix_20260515T181049_result.json`
- **Structured JSON:** [`e35b98e58127f3454fa9.json`](../../sessions/e3/e35b98e58127f3454fa9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（status/conclusion/checkpoint_path/log_path 已正确设置，无需重复更新）。

## kl_only_s0 评估结果 (seq_len=2048, WikiText-2)

| 指标 | 值 |
|------|-----|
| true_dense_ppl | 6.12 |
| predictor_hard_mask_ppl | 9.19 |
| teal_sparse_ppl | 12.03 |
| model_level_sparsity | 0.499 |
| ppl_increase_vs_true_dense_pct | 96.6% |

## 5-seed 对比表 (KL normalized v3, seq_len=2048)

| Metric | s0 | s1 | s42 | s123 | s456 | Mean ± Std |
|--------|-----|-----|------|------|------|------------|
| true_dense_ppl | 6.12 | 6.12 | 6.12 | 6.12 | 6.12 | 6.12 ± 0.00 |
| hard_mask_ppl | 9.19 | 9.15 | 9.21 | 9.25 | 9.14 | 9.19 ± 0.04 |
| teal_sparse_ppl | 12.03 | 11.99 | 12.08 | 11.91 | **13.58** | 12.32 ± 0.71 |
| sparsity | 0.499 | 0.498 | 0.498 | 0.498 | 0.498 | 0.498 |
| ppl_inc_vs_dense | 96.6% | 95.9% | 97.4% | 94.7% | **121.9%** | 101.3% |

4-seed (排除 s456 异常值): teal_sparse_ppl = **12.00 ± 0.07**，s0 在正常聚类内。

---
