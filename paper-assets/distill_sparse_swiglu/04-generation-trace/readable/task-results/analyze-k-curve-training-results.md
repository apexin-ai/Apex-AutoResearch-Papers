# analyze k curve training results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_k_curve_training_results_20260523T090401_result.json`
- **Structured JSON:** [`8ae120a817178fb74363.json`](../../sessions/8a/8ae120a817178fb74363.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验均已完成。

```json
{
  "exp_id": "perlayer_kl_k8_s456",
  "training_complete": true,
  "final_avg_kl": 0.0982,
  "final_avg_sparsity": 0.285,
  "wall_time_s": 1894.5,
  "training_steps": 1000,
  "checkpoint_path": "/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k8_s456/predictor_perlayer_kl_k4.pt",
  "log_path": "/root/runs/distill_sparse_swiglu/perlayer_kl_k8_s456.log"
}
```

```json
{
  "exp_id": "perlayer_kl_k8_s123",
  "training_complete": true,
  "final_avg_kl": 0.0997,
  "final_avg_sparsity": 0.286,
  "wall_time_s": 1900.2,
  "training_steps": 1000,
  "checkpoint_path": "/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k8_s123/predictor_perlayer_kl_k4.pt",
  "log_path": "/root/runs/distill_sparse_swiglu/perlayer_kl_k8_s123.log"
}
```

```json
{
  "exp_id": "perlayer_kl_k2_s42_train",
  "training_complete": true,
  "final_avg_kl": 0.0358,
  "final_avg_sparsity": 0.268,
  "wall_time_s": 3843.1,
  "training_steps": 1000,
  "checkpoint_path": "/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k2_s42/predictor_perlayer_kl_k4.pt",
  "log_path": "/root/runs/distill_sparse_swiglu/perlayer_kl_k2_s42_train.log"
}
```

每个 checkpoint 目录下均有 3 个文件：`predictor_perlayer_kl_k4.pt`（final）、`_step_500.pt`、`_step_1000.pt`。

K=2 的 KL 显著低于 K=8（0.036 vs ~0.099），但 sparsity 也略低（0.268 vs ~0.286），训练时间约为 K=8 的 2 倍（3843s vs ~1900s），符合 K=2 每步只更新 2 层导致收敛更慢的预期。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exp_id": "perlayer_kl_k2_s42_train",
    "training_complete": true,
    "final_avg_kl": 0.0358,
    "final_avg_sparsity": 0.268,
    "wall_time_s": 3843.1,
    "training_steps": 1000,
    "checkpoint_path": "/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k2_s42/predictor_perlayer_kl_k4.pt",
    "log_path": "/root/runs/distill_sparse_swiglu/perlayer_kl_k2_s42_train.log"
  }
}
```

</details>

---
