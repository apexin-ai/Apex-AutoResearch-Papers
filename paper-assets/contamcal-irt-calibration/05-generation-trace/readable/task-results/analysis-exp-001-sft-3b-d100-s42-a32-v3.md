# analysis exp 001 sft 3B d100 s42 a32 v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_3B_d100_s42_a32_v3_20260516T011149_result.json`
- **Structured JSON:** [`e2c9fddbf909816ef6b8.json`](../../sessions/e2/e2c9fddbf909816ef6b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常完成，checkpoint 完整。

```
STATUS: success
CHECKPOINT_PATH: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter
LOG_PATH: ~/runs/contamcal-irt-calibration/exp_001_sft_3B_d100_s42_a32_v3.log
FINAL_LOSS: 1.1795 (train_loss avg)
TOTAL_STEPS: 4159
TRAINING_TIME: 294 min (4h 54m)
WANDB_RUN_ID: N/A (no W&B logging detected)
NOTES:
- EXIT_CODE=0, epoch=1.0, cosine LR schedule fully decayed
- adapter_model.safetensors = 114.2 MB ✓
- lora_alpha=32, r=16 confirmed ✓
- mean_token_accuracy: 0.7186
- 3.771 samples/sec, 0.236 steps/sec
- Last-step loss ~1.19-1.21, consistent with avg — no divergence
```

---
