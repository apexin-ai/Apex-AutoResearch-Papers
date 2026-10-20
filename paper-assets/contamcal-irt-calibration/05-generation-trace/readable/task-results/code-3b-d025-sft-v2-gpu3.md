# code 3B d025 sft v2 gpu3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_3B-d025-sft-v2-gpu3_20260514T235153_result.json`
- **Structured JSON:** [`13ee943183087b255f03.json`](../../sessions/13/13ee943183087b255f03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`exp_001_sft_d025_3B_v2` registered as RUNNING.

**Summary:**
- **Root cause of v1 failure**: `train_sft.py` parses `--gpu` but never sets `CUDA_VISIBLE_DEVICES` or `device_map` — process defaulted to GPU 0
- **v2 fix**: Prefixed command with `CUDA_VISIBLE_DEVICES=3`
- **Verified**: PID 466755 on GPU 3 (`GPU-c30258a6`), 17616 MiB allocated, training at step 5/3384 (~4.1s/step)
- **ETA**: ~3384 steps × 4.1s ≈ 3.9 hours
- **Log**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/train_v2.log`

---
