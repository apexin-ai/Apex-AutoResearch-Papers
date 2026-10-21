# fix westd41074 pi05 random k075 strict crash

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd41074_pi05_random_k075_strict_crash_20260527T053318_result.json`
- **Structured JSON:** [`aa7170f6e663617092de.json`](../../sessions/aa/aa7170f6e663617092de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Model loaded successfully and running on GPU1 (10.4GB VRAM). No tokenizer errors — preprocessor/postprocessor loaded fine. The eval is starting: `Suite: libero_10, 10 tasks, max_steps=520`.

Summary:
- Killed stale processes, freed GPU1
- Root cause of original crash: `google/paligemma-3b-pt-224` tokenizer not cached when first strict runs launched. It's now cached in HF cache.
- Resubmitted job with `TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1` for safety
- **PID 177597 on GPU1, 10.4GB VRAM, evaluating libero_10 (random k=0.75, 50 episodes, seed 42)**
- Note: the previous run we killed had already completed Task 0 (84%), so this restart will redo that work (~15 min per task, ~2.5h total for all 10 tasks)

---
