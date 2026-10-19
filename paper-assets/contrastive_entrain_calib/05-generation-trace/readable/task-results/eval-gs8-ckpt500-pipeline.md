# eval gs8 ckpt500 pipeline

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gs8-ckpt500-pipeline_20260522T194054_result.json`
- **Structured JSON:** [`418645f9683cc069f772.json`](../../sessions/41/418645f9683cc069f772.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training is far behind expectations:

- **Current step**: 38/8000
- **Speed**: ~66s/step (not 24s/step as expected)
- **ETA to step 500**: ~462 steps × 66s ≈ **8.5 hours** (not 12 minutes)

This is a major discrepancy from the task description. The training appears to have restarted or is running much slower than anticipated. At this rate, checkpoint-500 won't be available until approximately **09:00 UTC on May 23**.

Should I:
1. Set up a periodic check and notify you when it's ready?
2. Investigate why the training is so slow (65s/step vs expected 24s/step)?
3. Something else?

---
