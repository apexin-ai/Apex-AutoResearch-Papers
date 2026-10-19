# train m2 full qwen

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_m2_full_qwen_20260513T162011_result.json`
- **Structured JSON:** [`9b8a1324551805ffd82c.json`](../../sessions/9b/9b8a1324551805ffd82c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Process at 13:43 elapsed, still only step 50 logged. Based on timing:

- Training loop started ~3 min after process launch
- 50 steps completed in ~10 min of training → **~9-10 s/step**
- 4242 steps/run × ~9.5s/step ≈ **11.2 hours/run**
- **9 runs total ≈ 101 hours ≈ 4.2 days**

**Status summary:**

| Item | Value |
|------|-------|
| Wrapper script | `/root/structfuse/run_m2_full_qwen.sh` (registered as artifact) |
| Log directory | `/root/runs/m2_full_qwen/{strategy}_s{seed}.log` |
| Checkpoint dir | `/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/{strategy}_s{seed}/` |
| Current run | 1/9: `random_s42` |
| Step 50 loss | 0.6716 (lr=2.36e-06, warmup phase) |
| GPU util | 100%, 49.4 GB / 95.6 GB VRAM |
| Registry | `m2_full_qwen` → RUNNING |
| Estimated completion | ~4.2 days from now (≈May 17) |

Training is healthy — loss is reasonable for early warmup, GPU fully utilized, dual checkpoint logic patched and verified, logs flushing correctly with `_print_flush()`. Next log line (step 100) should appear in ~5 minutes.

---
