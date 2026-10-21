# analysis perlayer kl k2 s123 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k2_s123_eval_20260523T111250_result.json`
- **Structured JSON:** [`f9abec8adc5919c46b7a.json`](../../sessions/f9/f9abec8adc5919c46b7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成，`EXIT_CODE=0`，无异常。

```json
{
  "wikitext2_ppl": 10.8835,
  "arc_challenge_acc": 0.3584,
  "arc_challenge_acc_norm": 0.4078,
  "winogrande_acc": 0.6140,
  "mmlu_acc": 0.3789,
  "gsm8k_exact_match": 0.0326,
  "hellaswag_acc": 0.4716,
  "hellaswag_acc_norm": 0.6605,
  "piqa_acc": 0.7323,
  "piqa_acc_norm": 0.7410
}
```

状态：评估成功完成（耗时 4026.2s），结果已保存到 `/root/distill_sparse_swiglu/results/benchmark/perlayer_kl_k2_s123_eval/results.json`。唯一的非致命警告是 `fatal: not a git repository`（不影响结果）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "wikitext2_ppl": 10.8835,
    "arc_challenge_acc": 0.3584,
    "arc_challenge_acc_norm": 0.4078,
    "winogrande_acc": 0.614,
    "mmlu_acc": 0.3789,
    "gsm8k_exact_match": 0.0326,
    "hellaswag_acc": 0.4716,
    "hellaswag_acc_norm": 0.6605,
    "piqa_acc": 0.7323,
    "piqa_acc_norm": 0.741
  }
}
```

</details>

---
