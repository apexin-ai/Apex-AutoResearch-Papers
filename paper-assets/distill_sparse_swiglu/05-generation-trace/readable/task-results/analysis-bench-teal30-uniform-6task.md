# analysis bench teal30 uniform 6task

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bench_teal30_uniform_6task_20260519T232855_result.json`
- **Structured JSON:** [`bd153aea5f3831285be9.json`](../../sessions/bd/bd153aea5f3831285be9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，无错误（EXIT_CODE=0）。无 gsm8k 任务（未包含在 tasks 列表中）。

```json
{
  "exp_id": "bench_teal30_uniform_6task",
  "config": {
    "model": "llama-3.1-8b",
    "sparsity_mode": "per_token",
    "baseline_mode": "teal_vanilla",
    "sparsity_target": 0.3,
    "allocation": "uniform",
    "bottleneck_size": 128,
    "batch_size": 8,
    "seq_len": 2048
  },
  "metrics": {
    "wikitext2_ppl": 10.8173,
    "arc_challenge_acc": 0.3771,
    "arc_challenge_acc_norm": 0.3933,
    "winogrande_acc": 0.6504,
    "mmlu_acc": 0.4586,
    "hellaswag_acc": 0.4617,
    "hellaswag_acc_norm": 0.6331,
    "piqa_acc": 0.7198,
    "piqa_acc_norm": 0.7280
  },
  "timestamp": "2026-05-20 06:37:22"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exp_id": "bench_teal30_uniform_6task",
    "config": {
      "model": "llama-3.1-8b",
      "sparsity_mode": "per_token",
      "baseline_mode": "teal_vanilla",
      "sparsity_target": 0.3,
      "allocation": "uniform",
      "bottleneck_size": 128,
      "batch_size": 8,
      "seq_len": 2048
    },
    "metrics": {
      "wikitext2_ppl": 10.8173,
      "arc_challenge_acc": 0.3771,
      "arc_challenge_acc_norm": 0.3933,
      "winogrande_acc": 0.6504,
      "mmlu_acc": 0.4586,
      "hellaswag_acc": 0.4617,
      "hellaswag_acc_norm": 0.6331,
      "piqa_acc": 0.7198,
      "piqa_acc_norm": 0.728
    },
    "timestamp": "2026-05-20 06:37:22"
  }
}
```

</details>

---
