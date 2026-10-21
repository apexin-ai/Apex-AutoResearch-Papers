# analysis grid b3 0 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b3_0_seed123_20260514T142523_result.json`
- **Structured JSON:** [`fcfa1e0a74999710d3ea.json`](../../sessions/fc/fcfa1e0a74999710d3ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
METRICS:
- train_loss: 10.7422
- total_steps: 6103
- train_runtime_s: 12955.83
- gpu_hours: 3.60
- eval_ppl_holdout: NOT_EXECUTED
- eval_loss: NOT_EXECUTED
- eval_holdout_tokens: NOT_EXECUTED
- checkpoint_path: /root/provenance_weight_training/output/models/grid_b3_0_seed123/final/

Checkpoints present: checkpoint-6000, checkpoint-6103, final/ (model.safetensors 1.19GB + tokenizer + config)

NOTE: eval was NOT executed — grep for "eval" in the log returned zero matches. Same issue as grid_b2_0_seed123 (should_evaluate=false).

ADAPTIVE_FIX_SEED123_STATUS:
- PID 109357: RUNNING (state Ss+, elapsed 01:30)
- GPU: PID 109362 (child process) on GPU-f25ffc1a (cuda:2), 46514 MiB allocated
```

---
