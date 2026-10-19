# analyze v2 lora physical r16

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_v2_lora_physical_r16_20260516T153026_result.json`
- **Structured JSON:** [`7fc0fdce32140deb3b09.json`](../../sessions/7f/7fc0fdce32140deb3b09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总：

```json
{
  "final_train_loss": 0.6776,
  "initial_train_loss": 0.731,
  "initial_train_loss_note": "resume from step_6000",
  "loss_reduction_ratio": 1.079,
  "total_steps": 9999,
  "steps_this_run": 3999,
  "training_time_minutes": 68,
  "exit_code": 0,
  "checkpoint_path": "/root/autodl-tmp/checkpoints/v2_lora_physical_r16/v2lora_physical_r16/final",
  "checkpoints_saved": ["step_1000","step_2000","step_3000","step_4000","step_5000","step_6000","step_7000","step_8000","step_9000","final"],
  "lora_rank": 16,
  "lora_alpha": 32,
  "errors": 0,
  "tracebacks": 0,
  "adapter_size_mb": 14.1,
  "conclusion": "success",
  "status": "DONE"
}
```

Loss 从 0.731 (step 6000 resume) 稳步下降到 0.6776 (step 9999)，checkpoint 完整（14.1MB adapter），无报错。实验标记为 success/DONE。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "final_train_loss": 0.6776,
    "initial_train_loss": 0.731,
    "initial_train_loss_note": "resume from step_6000",
    "loss_reduction_ratio": 1.079,
    "total_steps": 9999,
    "steps_this_run": 3999,
    "training_time_minutes": 68,
    "exit_code": 0,
    "checkpoint_path": "/root/autodl-tmp/checkpoints/v2_lora_physical_r16/v2lora_physical_r16/final",
    "checkpoints_saved": [
      "step_1000",
      "step_2000",
      "step_3000",
      "step_4000",
      "step_5000",
      "step_6000",
      "step_7000",
      "step_8000",
      "step_9000",
      "final"
    ],
    "lora_rank": 16,
    "lora_alpha": 32,
    "errors": 0,
    "tracebacks": 0,
    "adapter_size_mb": 14.1,
    "conclusion": "success",
    "status": "DONE"
  }
}
```

</details>

---
