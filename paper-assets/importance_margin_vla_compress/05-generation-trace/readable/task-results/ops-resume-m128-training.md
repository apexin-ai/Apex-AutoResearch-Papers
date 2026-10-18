# ops resume m128 training

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_resume_m128_training_20260518T052558_result.json`
- **Structured JSON:** [`1f6491467d4eed4b778e.json`](../../sessions/1f/1f6491467d4eed4b778e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the summary:

**Findings:**

- **GPU**: All 4x RTX 4090D are idle (0 MiB used). GPU 0 is free.
- **Checkpoint**: `checkpoints/smart_compress_m128/checkpoint.pt` (1.5 GB), confirmed at **step 32,000**. Contains keys: `step`, `model_state_dict`, `optimizer_state_dict`, `scheduler_state_dict`, `config`, `info`.
- **Resume mechanism**: The script has `--resume` flag. It accepts a directory path (auto-appends `/checkpoint.pt`) or a direct file path. It restores model, optimizer, scheduler, and sets `start_step = ckpt["step"] + 1` (= 32,001).

**Resume command:**

```bash
cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/bin/activate && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline python train_smart_compress.py --config configs/smart_compress_m128.yaml --resume checkpoints/smart_compress_m128 --wandb_run smart_compress_m128
```

The only addition vs. the original command is `--resume checkpoints/smart_compress_m128`. Training will resume from step 32,001 and run to 100,000.

---
