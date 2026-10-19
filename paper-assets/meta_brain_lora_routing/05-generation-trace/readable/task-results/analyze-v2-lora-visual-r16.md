# analyze v2 lora visual r16

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_v2_lora_visual_r16_20260516T153227_result.json`
- **Structured JSON:** [`d20bd688e3868266d347.json`](../../sessions/d2/d20bd688e3868266d347.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。结果汇总：

```json
{
  "experiment": "v2_lora_visual_r16",
  "status": "DONE",
  "conclusion": "success",
  "metrics": {
    "final_train_loss": 0.7035,
    "total_steps": 9999,
    "final_lr": 1e-05,
    "final_grad_norm": 4.82,
    "checkpoint_size_mb": 14.1
  },
  "checkpoints": "10 个 (step_1000~step_9000 + final)",
  "final_checkpoint": "/root/autodl-tmp/checkpoints/v2_lora_visual_r16/v2lora_visual_r16/final",
  "errors": 0
}
```

训练 9999 步正常完成，loss 从中后期稳定在 ~0.70，无异常。Final adapter 14MB 已保存。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "experiment": "v2_lora_visual_r16",
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "final_train_loss": 0.7035,
      "total_steps": 9999,
      "final_lr": 1e-05,
      "final_grad_norm": 4.82,
      "checkpoint_size_mb": 14.1
    },
    "checkpoints": "10 个 (step_1000~step_9000 + final)",
    "final_checkpoint": "/root/autodl-tmp/checkpoints/v2_lora_visual_r16/v2lora_visual_r16/final",
    "errors": 0
  }
}
```

</details>

---
