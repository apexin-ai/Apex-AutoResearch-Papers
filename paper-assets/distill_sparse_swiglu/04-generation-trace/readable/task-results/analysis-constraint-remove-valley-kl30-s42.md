# analysis constraint remove valley kl30 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_constraint_remove_valley_kl30_s42_20260522T144601_result.json`
- **Structured JSON:** [`a3165114b9749b33e6ba.json`](../../sessions/a3/a3165114b9749b33e6ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据已提取。

```
METRICS:
- wikitext2_ppl: 8.7592
- arc_challenge_acc: 0.3498 (±0.0139)
- arc_challenge_acc_norm: 0.3933 (±0.0143)
- mmlu_acc: 0.4397 (±0.0041)
- gsm8k_exact_match (strict): 0.0872 (±0.0078)
- gsm8k_exact_match (flexible): 0.0895 (±0.0079)
- actual_overall_sparsity: 0.2955

CONSTRAINT MECHANISM:
remove_valley: 强制将 L14–L18（predictor 发现的"保护谷"层，natural sparsity 仅 0.21–0.29）的 sparsity 拉高到 0.30（等于全局目标），多出的 pruning budget 均匀分摊给其余 27 层（使它们的 sparsity 各降低约 0.012），整体 sparsity 保持 ~0.30。目的是消融验证 predictor 自发保护这些层的因果效应。

LOG TAIL (最后有效行):
  PPL = 8.7592  (15.4s)
  Completed in 3121.0s
  arc_challenge: sample_len=1172, acc=0.3498, acc_norm=0.3933
  mmlu: sample_len=14042, acc=0.4397
  gsm8k: sample_len=1319, exact_match=0.0895
  Results saved to /root/distill_sparse_swiglu/results/benchmark/constraint_remove_valley_kl30_s42/results.json
  EXIT_CODE=0
```

---
