# analyze qwen14b uniform eval 4task

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen14b_uniform_eval_4task_20260518T012312_result.json`
- **Structured JSON:** [`75e126d7d3dd350caad1.json`](../../sessions/75/75e126d7d3dd350caad1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments completed successfully (EXIT_CODE=0), no errors or warnings.

```
=== qwen14b_teal30_uniform_eval_4task ===
wikitext2_ppl: 8.0054
arc_challenge_acc: 0.5128
arc_challenge_acc_norm: 0.5529
winogrande_acc: 0.6985
mmlu_acc: 0.6634
errors/warnings: 无

=== qwen14b_kl30_uniform_eval_4task ===
wikitext2_ppl: 7.6318
arc_challenge_acc: 0.4949
arc_challenge_acc_norm: 0.5444
winogrande_acc: 0.7245
mmlu_acc: 0.6449
errors/warnings: 无
```

关键发现：KL uniform MMLU 从 global_topk 的 63.72% 涨到 64.49%，仅 +0.77pp，远未恢复到 >70%。TEAL uniform MMLU 66.34% 也低于其 global_topk 的 71.8%。uniform allocation 对两者都没有带来预期的 MMLU 恢复，反而 TEAL 的 MMLU 还从 71.8% 跌到 66.3%（-5.5pp）。PPL 方面 KL uniform 7.63 与 global_topk 7.62 持平，TEAL uniform 8.01 略优于 global_topk 8.73。

---
