# diagnose ablation occ detach s0 retrain

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ablation_occ_detach_s0_retrain_20260525T022401_result.json`
- **Structured JSON:** [`69a83297ffb5fc5f93ed.json`](../../sessions/69/69a83297ffb5fc5f93ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已完成，日志显示 "Max step 50005 reached! Stopping training..."。最后记录的 AUX 指标是 step=30000（resume 日志中只有两条 AUX 记录）。

```json
{
  "checkpoint_50k_exists": true,
  "checkpoint_path": "/root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt",
  "checkpoint_size": "15G",
  "checkpoint_contents": ["action_head--50000_checkpoint.pt", "occ_head--50000_checkpoint.pt", "proprio_projector--50000_checkpoint.pt", "lora_adapter", "model-00001~00004-of-00004.safetensors", "config.json", "dataset_statistics.json", "tokenizer files..."],
  "last_aux_metrics": "step=30000, occ_loss=0.0179, depth_loss=0.0000, action_loss=0.0562",
  "training_status": "completed (Max step 50005 reached)",
  "other_checkpoints": ["20000_chkpt", "40000_chkpt"]
}
```

注意：没有 30K checkpoint 目录（日志中 30K 处只记录了 AUX 指标但未保存 checkpoint）。20K 和 40K checkpoint 都存在。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "checkpoint_50k_exists": true,
    "checkpoint_path": "/root/autodl-tmp/checkpoints/ablation_occ_detach_s0_retrain/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt",
    "checkpoint_size": "15G",
    "checkpoint_contents": [
      "action_head--50000_checkpoint.pt",
      "occ_head--50000_checkpoint.pt",
      "proprio_projector--50000_checkpoint.pt",
      "lora_adapter",
      "model-00001~00004-of-00004.safetensors",
      "config.json",
      "dataset_statistics.json",
      "tokenizer files..."
    ],
    "last_aux_metrics": "step=30000, occ_loss=0.0179, depth_loss=0.0000, action_loss=0.0562",
    "training_status": "completed (Max step 50005 reached)",
    "other_checkpoints": [
      "20000_chkpt",
      "40000_chkpt"
    ]
  }
}
```

</details>

---
