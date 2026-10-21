# ops cqa1 xvla k07 seed43 check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-xvla-k07-seed43-check_20260521T072121_result.json`
- **Structured JSON:** [`f8dcf21fd283e4d02deb.json`](../../sessions/f8/f8dcf21fd283e4d02deb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

**1. eval_xvla_random_k07_object_seed43** — Confirmed **failed**. The result file on disk (`xvla_prune_k0.7_libero_object_seed43.json`) is actually l2_norm_prune mode (SR=59.0%), not random. No random k=0.7 seed43 result exists. Registry updated with notes.

**2. eval_xvla_random_k05_spatial_seed42** (bonus find) — **Completed successfully**. SR=**71.4%** (357/500), CI [67.3%, 75.2%]. Notable: Spatial random k=0.5 (71.4%) ≈ Object random k=0.5 (70.6%), confirming linear projection immunity across suites. Registry updated to DONE/success.

**3. cqa1-33015 GPU status**:
- **GPU 0: FREE**
- **GPU 1: FREE**
- GPU 2: l2_norm k=0.70 seed42 (~47 min in)
- GPU 3: random k=0.50 seed43 (~47 min in)

---
