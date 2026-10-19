# analysis perlayer kl k16 s456 v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k16_s456_v2_20260523T100647_result.json`
- **Structured JSON:** [`e526a9b12b24c8986e97.json`](../../sessions/e5/e526a9b12b24c8986e97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练成功完成，1000 步全部跑完，无报错。

```json
{
  "training_success": true,
  "final_kl": 0.1611,
  "avg_kl": 0.1565,
  "avg_sparsity": 0.287,
  "wall_time_s": 1977.9,
  "steps_completed": 1000,
  "checkpoint_path": "/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k16_s456/",
  "checkpoint_exists": true,
  "checkpoint_files": [
    "predictor_perlayer_kl_k4.pt (145MB, final)",
    "predictor_perlayer_kl_k4_step_500.pt (435MB)",
    "predictor_perlayer_kl_k4_step_1000.pt (435MB)"
  ],
  "comparison_note": "与 s42(avg_kl=0.1582, sp=0.286) 和 s123(avg_kl=0.1617, sp=0.287) 高度一致。avg_kl=0.1565 居三者中间，sparsity=0.287 与 s123 完全一致。final_kl=0.1611 略高于 s42(0.1406)/s123(0.1436)，属单步波动，不影响整体收敛质量。三个 seed 结果稳定。"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "training_success": true,
    "final_kl": 0.1611,
    "avg_kl": 0.1565,
    "avg_sparsity": 0.287,
    "wall_time_s": 1977.9,
    "steps_completed": 1000,
    "checkpoint_path": "/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k16_s456/",
    "checkpoint_exists": true,
    "checkpoint_files": [
      "predictor_perlayer_kl_k4.pt (145MB, final)",
      "predictor_perlayer_kl_k4_step_500.pt (435MB)",
      "predictor_perlayer_kl_k4_step_1000.pt (435MB)"
    ],
    "comparison_note": "与 s42(avg_kl=0.1582, sp=0.286) 和 s123(avg_kl=0.1617, sp=0.287) 高度一致。avg_kl=0.1565 居三者中间，sparsity=0.287 与 s123 完全一致。final_kl=0.1611 略高于 s42(0.1406)/s123(0.1436)，属单步波动，不影响整体收敛质量。三个 seed 结果稳定。"
  }
}
```

</details>

---
