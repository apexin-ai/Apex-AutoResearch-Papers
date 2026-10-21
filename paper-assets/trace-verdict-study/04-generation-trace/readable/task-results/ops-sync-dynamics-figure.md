# ops sync dynamics figure

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync_dynamics_figure_20260522T074207_result.json`
- **Structured JSON:** [`761326573ea47f59627e.json`](../../sessions/76/761326573ea47f59627e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**1. 复制成功。** 目标文件时间戳已更新为 May 22 15:42：
- `training_dynamics.pdf` — 35,761 bytes
- `training_dynamics.png` — 264,761 bytes

**2. oscillation_metrics.json 完整内容：**

```json
{
  "exception_only": {
    "condition": "exception_only",
    "loss_rolling_variance_mean": 0.001165439880952381,
    "loss_rolling_variance_max": 0.028815062500000016,
    "accuracy_cv_full": 0.0023848458050136426,
    "accuracy_cv_last100steps": 0.0,
    "convergence_std_last3ckpt": 0.0,
    "max_drop_pp": 0.0,
    "max_drop_from": 0.0,
    "max_drop_to": 0.0,
    "max_drop_from_step": 0,
    "max_drop_to_step": 0,
    "recovery_steps": null,
    "recovery_at_step": null,
    "best_accuracy": 0.9983,
    "best_accuracy_step": 200,
    "final_accuracy": 0.9983,
    "final_loss": 0.0329
  },
  "full_trace": {
    "condition": "full_trace",
    "loss_rolling_variance_mean": 0.1822864163690476,
    "loss_rolling_variance_max": 7.377470822499999,
    "accuracy_cv_full": 0.023394130513892983,
    "accuracy_cv_last100steps": 0.003135728519674257,
    "convergence_std_last3ckpt": 0.002772967769359,
    "max_drop_pp": 5.29,
    "max_drop_from": 0.8739,
    "max_drop_to": 0.821,
    "max_drop_from_step": 50,
    "max_drop_to_step": 100,
    "recovery_steps": 100,
    "recovery_at_step": 200,
    "best_accuracy": 0.8882,
    "best_accuracy_step": 350,
    "final_accuracy": 0.8824,
    "final_loss": 0.0085
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "exception_only": {
      "condition": "exception_only",
      "loss_rolling_variance_mean": 0.001165439880952381,
      "loss_rolling_variance_max": 0.028815062500000016,
      "accuracy_cv_full": 0.0023848458050136426,
      "accuracy_cv_last100steps": 0.0,
      "convergence_std_last3ckpt": 0.0,
      "max_drop_pp": 0.0,
      "max_drop_from": 0.0,
      "max_drop_to": 0.0,
      "max_drop_from_step": 0,
      "max_drop_to_step": 0,
      "recovery_steps": null,
      "recovery_at_step": null,
      "best_accuracy": 0.9983,
      "best_accuracy_step": 200,
      "final_accuracy": 0.9983,
      "final_loss": 0.0329
    },
    "full_trace": {
      "condition": "full_trace",
      "loss_rolling_variance_mean": 0.1822864163690476,
      "loss_rolling_variance_max": 7.377470822499999,
      "accuracy_cv_full": 0.023394130513892983,
      "accuracy_cv_last100steps": 0.003135728519674257,
      "convergence_std_last3ckpt": 0.002772967769359,
      "max_drop_pp": 5.29,
      "max_drop_from": 0.8739,
      "max_drop_to": 0.821,
      "max_drop_from_step": 50,
      "max_drop_to_step": 100,
      "recovery_steps": 100,
      "recovery_at_step": 200,
      "best_accuracy": 0.8882,
      "best_accuracy_step": 350,
      "final_accuracy": 0.8824,
      "final_loss": 0.0085
    }
  }
}
```

</details>

---
