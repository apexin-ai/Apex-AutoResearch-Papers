# analysis exp 001 sft 14b d050 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_14b_d050_s42_20260518T224139_result.json`
- **Structured JSON:** [`2d9c0f375b3f450084dc.json`](../../sessions/2d/2d9c0f375b3f450084dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the information needed. Here's the analysis:

```
conclusion: success
metrics:
  final_train_loss: 0.9165
  final_token_accuracy: 0.7760
  total_steps: 3642
  training_time: ~3h10m (estimated; log file missing, proportional to 14B d000's 2h43m/3125 steps)
  checkpoint_size_mb: 1100 (total), 263 (adapter_model.safetensors)
wandb_run_id: N/A (no W&B directory found on server; training ran without W&B)
notes:
  - Log file /root/autodl-tmp/exp001/logs/14b_d050_s42.log does not exist; metrics extracted from trainer_state.json in checkpoint
  - .done sentinel present (2026-05-19 06:38)
  - Checkpoint complete: adapter_model.safetensors (263M), adapter_config.json, tokenizer, training_args.bin, plus full checkpoint-3642 with optimizer state
  - lora_alpha=32 confirmed (compliant with C006)
  - Steps 3642 matches expectation: 58266 / 16 (grad_accum) = 3641.6 → 3642
  - Final metrics (step 3640, last logged) vs series:
      d000: loss=0.9089, acc=0.7761, steps=3125
      d005: loss=0.9141, acc=0.7969, steps=3177
      d025: loss=0.9260, acc=0.7740, steps=3384
      d050: loss=0.9165, acc=0.7760, steps=3642  ← this run
  - Loss and accuracy within normal range for the 14B series; no anomalies
  - No errors or warnings detected in trainer_state
```

---
