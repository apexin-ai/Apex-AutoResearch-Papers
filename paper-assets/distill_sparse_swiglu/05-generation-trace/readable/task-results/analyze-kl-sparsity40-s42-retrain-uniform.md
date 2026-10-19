# analyze kl sparsity40 s42 retrain uniform

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_kl_sparsity40_s42_retrain_uniform_20260520T064809_result.json`
- **Structured JSON:** [`1d28073ae0b7c0f62e79.json`](../../sessions/1d/1d28073ae0b7c0f62e79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

- **训练**: 成功（1000/1000 steps, 最终 loss=0.2598, sparsity=0.387）
- **checkpoint_path**: `/root/distill_sparse_swiglu/checkpoints/kl_sparsity40_s42/predictor_kl_normalized.pt` (145MB, 2026-05-20 14:12)
- **allocation**: uniform, sparsity_target=0.4

| 指标 | 值 |
|------|-----|
| wikitext2_ppl | **10.76** |
| arc_challenge | 39.59% (acc_norm) |
| winogrande | 63.06% |
| mmlu | 35.50% |
| gsm8k | 3.56% |

**对比 global 40%**: global PPL=10.12, uniform PPL=10.76, 差距 Δ=+0.64。uniform 略差于 global，符合预期（global 分配可以按层重要性调整 sparsity，uniform 则均匀分配）。

结果已保存至 `/root/distill_sparse_swiglu/results/benchmark/kl_sparsity40_s42_retrain_uniform/results.json`，时间戳 2026-05-20 14:12:19。

---
