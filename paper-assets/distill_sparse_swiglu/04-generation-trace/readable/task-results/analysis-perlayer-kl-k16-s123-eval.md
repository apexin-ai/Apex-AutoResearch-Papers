# analysis perlayer kl k16 s123 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k16_s123_eval_20260523T135310_result.json`
- **Structured JSON:** [`f90b60c3870765c20de6.json`](../../sessions/f9/f90b60c3870765c20de6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常完成（EXIT_CODE=0），耗时 4179.3s。

```json
{
  "wikitext2_ppl": 8.6939,
  "arc_challenge_acc_norm": 0.4317,
  "winogrande_acc": 0.6772,
  "mmlu_acc": 0.3996,
  "gsm8k_exact_match": 0.0986,
  "hellaswag_acc_norm": 0.7050,
  "piqa_acc_norm": 0.7481,
  "sparsity_per_layer": "0.293–0.301 (avg ≈ 0.298, 32 layers)"
}
```

**Checkpoint 目录注意**：`/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k16_s123/` 存在，但里面只有一个文件 `predictor_perlayer_kl_k4.pt`（145MB）——文件名是 k4 而非 k16，可能是命名不一致或复用了其他 checkpoint。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "wikitext2_ppl": 8.6939,
    "arc_challenge_acc_norm": 0.4317,
    "winogrande_acc": 0.6772,
    "mmlu_acc": 0.3996,
    "gsm8k_exact_match": 0.0986,
    "hellaswag_acc_norm": 0.705,
    "piqa_acc_norm": 0.7481,
    "sparsity_per_layer": "0.293–0.301 (avg ≈ 0.298, 32 layers)"
  }
}
```

</details>

---
