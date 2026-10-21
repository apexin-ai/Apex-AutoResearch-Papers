# analyze qwen14b kl30 s42 gsm8k uniform

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen14b_kl30_s42_gsm8k_uniform_20260522T103235_result.json`
- **Structured JSON:** [`f84557606cfaef89edba.json`](../../sessions/f8/f84557606cfaef89edba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "gsm8k_exact_match": 0.3548,
  "gsm8k_exact_match_stderr": 0.01318,
  "actual_sparsity": 0.296,
  "wandb_run_id": null,
  "success": true,
  "error_msg": null,
  "raw_metrics_line": "gsm8k: sample_len=1319, exact_match=0.3548"
}
```

关键发现：

- **KL s42 uniform GSM8K = 0.3548**，与 KL s42 global (0.3571) 几乎无差异（Δ = -0.0023，在 stderr 范围内）
- 两种 allocation 策略（uniform vs global）对 KL predictor 的 GSM8K 性能没有实质影响
- 相比 TEAL@30% uniform (0.5208) 仍有显著差距（-0.166）
- 每层 sparsity 均在 0.285–0.301 范围，均值约 0.296（接近目标 0.30）
- 无 W&B run ID，结果已保存至 `results/benchmark/qwen14b_kl30_s42_gsm8k_uniform/results.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "gsm8k_exact_match": 0.3548,
    "gsm8k_exact_match_stderr": 0.01318,
    "actual_sparsity": 0.296,
    "wandb_run_id": null,
    "success": true,
    "error_msg": null,
    "raw_metrics_line": "gsm8k: sample_len=1319, exact_match=0.3548"
  }
}
```

</details>

---
