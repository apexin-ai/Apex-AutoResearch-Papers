# deploy cqa1 gpu3 next

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_gpu3_next_20260525T110242_result.json`
- **Structured JSON:** [`f5158ad92a1bc80ac1cd.json`](../../sessions/f5/f5158ad92a1bc80ac1cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 3 still at 4MiB — model loading to CPU first, will move to GPU shortly (normal for π0.5).

**Summary:**

**Step 1 — Collected ✓**
- `eval_pi05_l2norm_k085_long_seed42_postfix_v3`: **SR=78.0%** (390/500)
- Per-task: T0=98%, T1=94%, T2=82%, T3=100%, T4=72%, T5=96%, T6=8%, T7=80%, T8=56%, T9=94%
- Registry → DONE (success), metrics recorded

**Step 2 — Deployed ✓**
- `eval_pi05_random_k03_long_seed43_v4` on cqa1 GPU 3 (PID 313394)
- Random k=0.3, libero_10, seed 43, CUDA_VISIBLE_DEVICES=3 + --gpu 0
- Registry → RUNNING with full provenance

**Step 3 — Verified**
- Tmux session running, log shows model loading from `/root/autodl-tmp/pi05_libero_finetuned`
- GPU 3 not yet allocated (CPU loading phase) — expected, will show ~10GB once model loads to GPU

---
