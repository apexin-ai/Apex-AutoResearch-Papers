# analyze perlayer kl k8 s456 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_perlayer_kl_k8_s456_eval_20260523T123708_result.json`
- **Structured JSON:** [`c30dedcc29d4b2551037.json`](../../sessions/c3/c30dedcc29d4b2551037.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "wikitext2_ppl": 8.9515,
  "arc_challenge_acc_norm": 0.3951,
  "winogrande_acc": 0.6875,
  "mmlu_acc": 0.4105,
  "gsm8k_exact_match": 0.0811,
  "hellaswag_acc_norm": 0.6783,
  "piqa_acc_norm": 0.7399,
  "sparsity": 0.298
}
```

全部 7 个任务均成功完成，无错误。与同配置其他 seed 对比：

| 指标 | s42 | s123 | **s456** |
|------|-----|------|----------|
| PPL | 8.9704 | 9.0648 | **8.9515** |
| ARC | 0.4104 | 0.4155 | **0.3951** |
| WG | 0.674 | 0.6993 | **0.6875** |
| MMLU | 0.398 | 0.4042 | **0.4105** |
| GSM8K | 0.0561 | 0.0682 | **0.0811** |

s456 的 PPL 最低（最优），MMLU 和 GSM8K 也是三个 seed 中最高的。ARC 略低但在合理范围内。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "wikitext2_ppl": 8.9515,
    "arc_challenge_acc_norm": 0.3951,
    "winogrande_acc": 0.6875,
    "mmlu_acc": 0.4105,
    "gsm8k_exact_match": 0.0811,
    "hellaswag_acc_norm": 0.6783,
    "piqa_acc_norm": 0.7399,
    "sparsity": 0.298
  }
}
```

</details>

---
