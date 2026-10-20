# analysis plan 001 flat nli seed43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_001_flat_nli_seed43_20260515T202143_result.json`
- **Structured JSON:** [`a84fe4399a9de1b35bde.json`](../../sessions/a8/a84fe4399a9de1b35bde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```json
{
  "conclusion": "success",
  "metrics": {
    "train_loss_avg": 0.6248,
    "train_loss_min_observed": 0.5895,
    "train_loss_min_step": 400,
    "train_runtime_seconds": 6880,
    "train_samples_per_second": 1.173,
    "total_steps": 507,
    "epochs": 3,
    "num_train_samples": 2691,
    "train_mean_token_accuracy_final": 0.8473,
    "train_mean_token_accuracy_max_observed": 0.8553,
    "eval_loss_epoch1": 0.7529,
    "eval_loss_epoch2": 0.7535,
    "eval_loss_epoch3": 0.7567,
    "eval_mean_token_accuracy_epoch1": 0.8297,
    "eval_mean_token_accuracy_epoch2": 0.8300,
    "eval_mean_token_accuracy_epoch3": 0.8298
  },
  "checkpoint_path": "/root/autodl-tmp/rsft_output_flat_nli_s43",
  "checkpoints": ["checkpoint-350", "checkpoint-400", "checkpoint-450", "checkpoint-500", "checkpoint-507"],
  "adapter_model_size_mb": 504,
  "comparison_with_seed42": {
    "train_loss_avg": "0.6248 vs 0.6238 (delta +0.001, 几乎一致)",
    "train_loss_min": "0.5895 vs 0.5803 (seed43 略高)",
    "train_accuracy": "~0.855 vs 0.8528 (范围一致)",
    "total_steps": "507 vs 507 (相同)",
    "num_samples": "2691 vs 2691 (相同)",
    "runtime": "6880s vs 2946s (seed43 含 per-epoch eval，seed42 可能未含)",
    "verdict": "两个 seed 训练指标高度一致，loss 和 accuracy 均在正常波动范围内"
  },
  "notes": "训练正常完成(EXIT_CODE=0)。eval_loss 三个 epoch 基本持平(0.753-0.757)，无明显过拟合。最终模型已保存至输出目录，含 adapter_model.safetensors(504MB)。"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "conclusion": "success",
    "metrics": {
      "train_loss_avg": 0.6248,
      "train_loss_min_observed": 0.5895,
      "train_loss_min_step": 400,
      "train_runtime_seconds": 6880,
      "train_samples_per_second": 1.173,
      "total_steps": 507,
      "epochs": 3,
      "num_train_samples": 2691,
      "train_mean_token_accuracy_final": 0.8473,
      "train_mean_token_accuracy_max_observed": 0.8553,
      "eval_loss_epoch1": 0.7529,
      "eval_loss_epoch2": 0.7535,
      "eval_loss_epoch3": 0.7567,
      "eval_mean_token_accuracy_epoch1": 0.8297,
      "eval_mean_token_accuracy_epoch2": 0.83,
      "eval_mean_token_accuracy_epoch3": 0.8298
    },
    "checkpoint_path": "/root/autodl-tmp/rsft_output_flat_nli_s43",
    "checkpoints": [
      "checkpoint-350",
      "checkpoint-400",
      "checkpoint-450",
      "checkpoint-500",
      "checkpoint-507"
    ],
    "adapter_model_size_mb": 504,
    "comparison_with_seed42": {
      "train_loss_avg": "0.6248 vs 0.6238 (delta +0.001, 几乎一致)",
      "train_loss_min": "0.5895 vs 0.5803 (seed43 略高)",
      "train_accuracy": "~0.855 vs 0.8528 (范围一致)",
      "total_steps": "507 vs 507 (相同)",
      "num_samples": "2691 vs 2691 (相同)",
      "runtime": "6880s vs 2946s (seed43 含 per-epoch eval，seed42 可能未含)",
      "verdict": "两个 seed 训练指标高度一致，loss 和 accuracy 均在正常波动范围内"
    },
    "notes": "训练正常完成(EXIT_CODE=0)。eval_loss 三个 epoch 基本持平(0.753-0.757)，无明显过拟合。最终模型已保存至输出目录，含 adapter_model.safetensors(504MB)。"
  }
}
```

</details>

---
