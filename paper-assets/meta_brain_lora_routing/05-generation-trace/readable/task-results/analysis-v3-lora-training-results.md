# analysis v3 lora training results

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v3_lora_training_results_20260516T200313_result.json`
- **Structured JSON:** [`9e20ec572598450d681c.json`](../../sessions/9e/9e20ec572598450d681c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here are the results:

```json
{
  "v3_lora_universal_r16": {
    "final_train_loss": 0.6030,
    "initial_train_loss": 1.9529,
    "loss_reduction_ratio": 3.239,
    "total_steps": 10000,
    "training_time_minutes": 170.4,
    "exit_code": 0,
    "checkpoint_path": "/root/autodl-tmp/checkpoints/v3_lora_universal_r16/v3lora_universal_r16/final",
    "checkpoints_saved": ["step_1000", "step_2000", "step_3000", "step_4000", "step_5000", "step_6000", "step_7000", "step_8000", "step_9000", "final"],
    "lora_rank": 16,
    "lora_alpha": 32,
    "errors": 0,
    "tracebacks": 0
  },
  "v3_lora_physical_r16": {
    "final_train_loss": 0.5876,
    "initial_train_loss": 2.3697,
    "loss_reduction_ratio": 4.033,
    "total_steps": 10000,
    "training_time_minutes": 170.1,
    "exit_code": 0,
    "checkpoint_path": "/root/autodl-tmp/checkpoints/v3_lora_physical_r16/v3lora_physical_r16/final",
    "checkpoints_saved": ["step_1000", "step_2000", "step_3000", "step_4000", "step_5000", "step_6000", "step_7000", "step_8000", "step_9000", "final"],
    "lora_rank": 16,
    "lora_alpha": 32,
    "errors": 0,
    "tracebacks": 0
  },
  "v3_lora_spatial_r16": {
    "final_train_loss": 0.6126,
    "initial_train_loss": 1.9529,
    "loss_reduction_ratio": 3.188,
    "total_steps": 10000,
    "training_time_minutes": 171.1,
    "exit_code": 0,
    "checkpoint_path": "/root/autodl-tmp/checkpoints/v3_lora_spatial_r16/v3lora_spatial_r16/final",
    "checkpoints_saved": ["step_1000", "step_2000", "step_3000", "step_4000", "step_5000", "step_6000", "step_7000", "step_8000", "step_9000", "final"],
    "lora_rank": 16,
    "lora_alpha": 32,
    "errors": 0,
    "tracebacks": 0
  }
}
```

**要点：**
- 3 个实验全部正常完成，EXIT_CODE=0，无 traceback
- physical expert 的 initial loss 最高（2.3697 vs ~1.95），说明 physical perturbation 对 base model 偏离最大，但最终 loss 也最低（0.5876），收敛最好
- 每个 checkpoint 目录包含 `adapter_config.json` + `adapter_model.safetensors`（~14MB），结构正确
- 每个实验约 170 分钟，每步 ~51s

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "v3_lora_universal_r16": {
      "final_train_loss": 0.603,
      "initial_train_loss": 1.9529,
      "loss_reduction_ratio": 3.239,
      "total_steps": 10000,
      "training_time_minutes": 170.4,
      "exit_code": 0,
      "checkpoint_path": "/root/autodl-tmp/checkpoints/v3_lora_universal_r16/v3lora_universal_r16/final",
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
      "tracebacks": 0
    },
    "v3_lora_physical_r16": {
      "final_train_loss": 0.5876,
      "initial_train_loss": 2.3697,
      "loss_reduction_ratio": 4.033,
      "total_steps": 10000,
      "training_time_minutes": 170.1,
      "exit_code": 0,
      "checkpoint_path": "/root/autodl-tmp/checkpoints/v3_lora_physical_r16/v3lora_physical_r16/final",
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
      "tracebacks": 0
    },
    "v3_lora_spatial_r16": {
      "final_train_loss": 0.6126,
      "initial_train_loss": 1.9529,
      "loss_reduction_ratio": 3.188,
      "total_steps": 10000,
      "training_time_minutes": 171.1,
      "exit_code": 0,
      "checkpoint_path": "/root/autodl-tmp/checkpoints/v3_lora_spatial_r16/v3lora_spatial_r16/final",
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
      "tracebacks": 0
    }
  }
}
```

</details>

---
