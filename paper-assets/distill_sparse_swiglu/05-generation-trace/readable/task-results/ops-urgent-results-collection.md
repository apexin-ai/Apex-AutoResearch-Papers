# ops urgent results collection

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-results-collection_20260519T050232_result.json`
- **Structured JSON:** [`c17ceab57f8ce77ac5f7.json`](../../sessions/c1/c17ceab57f8ce77ac5f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕。Checkpoint 验证通过。汇总如下：

```
=== mistral_teal30_downstream ===
wikitext2_ppl: 8.3807
arc_challenge_acc_norm: 0.4113
winogrande_acc: 0.6354
mmlu_acc: 0.4348
gsm8k_exact_match: 0.1592
hellaswag_acc_norm: 0.6011
piqa_acc_norm: 0.7214

=== mistral_teal50_downstream ===
wikitext2_ppl: 18.3061
arc_challenge_acc_norm: 0.2457
winogrande_acc: 0.5091
mmlu_acc: 0.2635
gsm8k_exact_match: 0.0341
hellaswag_acc_norm: 0.3603
piqa_acc_norm: 0.6045

=== eval_c1_retrain_30pct_s123 ===
wikitext2_ppl: 7.54
arc_challenge_acc_norm: 0.4471
winogrande_acc: 0.6977
mmlu_acc: 0.3992
gsm8k_exact_match: 0.0682

=== eval_c1_retrain_30pct_s456 ===
wikitext2_ppl: 7.38
arc_challenge_acc_norm: 0.4471
winogrande_acc: 0.6993
mmlu_acc: 0.4104
gsm8k_exact_match: 0.0660

=== c1_retrain training agreement ===
s123 final: agreement=0.977, sparsity=0.310
s456 final: agreement=0.977, sparsity=0.312

=== c1_retrain training PPL (WikiText-2, inline eval) ===
s123: PPL=7.54, actual_sparsity=0.332
s456: PPL=7.38, actual_sparsity=0.346
(reference: KL predictor PPL=11.79, BCE predictor PPL=22.51)
```

**Checkpoints 验证通过：**
- `c1_retrain_30pct_s123/predictor_bce_kl_targets.pt` — 145MB
- `c1_retrain_30pct_s456/predictor_bce_kl_targets.pt` — 145MB

**要点：**
- C1 retrain 两个 seed 结果高度一致（agreement 0.977，PPL ~7.4-7.5，downstream 差异 <1.1pp），复现性强
- C1 retrain eval 没有跑 hellaswag 和 piqa（只有 arc/winogrande/mmlu/gsm8k 4 项）
- TEAL 50% 性能显著退化（PPL 18.3 vs 30% 的 8.4），downstream 全面崩塌

---
