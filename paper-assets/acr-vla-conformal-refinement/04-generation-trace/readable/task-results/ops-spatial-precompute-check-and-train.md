# ops spatial precompute check and train

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_spatial-precompute-check-and-train_20260521T183332_result.json`
- **Structured JSON:** [`33711524fe9fd9d2b9da.json`](../../sessions/33/33711524fe9fd9d2b9da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

tmux session alive, process running. Normalization on 60K×2048 takes a few minutes — GPU is engaged (14.5GB VRAM, 24% util).

**Summary:**

- **Spatial precompute**: All 7 shards (s0-s6) completed on bjb2-28827, auto-merge produced 60,250 samples (100%)
- **Data transfer**: Merged files (547MB total) transferred bjb2-28827 → management host → bjb1-18228
- **Spatial CRM training**: Submitted via `submit_training_job` on bjb1-18228 cuda:1, exp_id=`crm-train-pi05-spatial-full`, 50 epochs, batch_size=32, lr=1e-3
- **Registry**: Updated to RUNNING with full spec metadata
- **Object CRM training**: Continues on cuda:0 (epoch 4/50)

Both CRM training jobs now running in parallel on bjb1-18228.

---
