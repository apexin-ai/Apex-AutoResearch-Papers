# ops gpu status check cqa1 urgent

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_cqa1_urgent_20260518T025320_result.json`
- **Structured JSON:** [`fd883ade9092e347eb9b.json`](../../sessions/fd/fd883ade9092e347eb9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both evals completed. Both trainings still running. Here's the full status:

```
=== GPU STATUS ===
GPU 0: idle — M=32 eval DONE
GPU 1: idle — M=64 eval DONE
GPU 2: busy (2787 MiB) — M=96 train running (step 87700/100000, ~87.7%)
GPU 3: busy (2815 MiB) — M=16 train running (step 84750/100000, ~84.8%)

=== M=32 EVAL RESULTS ===
SUITE: libero_object | M=32
Overall SR: 308/500 (61.6%) [95% Wilson CI: 57.3%–65.8%]
  Task 0: 68% (34/50) — alphabet soup
  Task 1: 64% (32/50) — cream cheese
  Task 2: 60% (30/50) — salad dressing
  Task 3: 46% (23/50) — bbq sauce
  Task 4: 66% (33/50) — ketchup
  Task 5: 36% (18/50) — tomato sauce
  Task 6: 82% (41/50) — butter
  Task 7: 76% (38/50) — milk
  Task 8: 90% (45/50) — chocolate pudding
  Task 9: 28% (14/50) — orange juice

=== M=64 EVAL RESULTS ===
SUITE: libero_object | M=64
Overall SR: 308/500 (61.6%) [95% Wilson CI: 57.3%–65.8%]
  Task 0: 74% (37/50) — alphabet soup
  Task 1: 38% (19/50) — cream cheese
  Task 2: 64% (32/50) — salad dressing
  Task 3: 56% (28/50) — bbq sauce
  Task 4: 64% (32/50) — ketchup
  Task 5: 54% (27/50) — tomato sauce
  Task 6: 84% (42/50) — butter
  Task 7: 62% (31/50) — milk
  Task 8: 74% (37/50) — chocolate pudding
  Task 9: 46% (23/50) — orange juice

=== TRAINING PROGRESS ===
M=96: step 87700/100000 (87.7%), ~4.0 sps → ETA ~51 min
M=16: step 84750/100000 (84.8%), ~4.1 sps → ETA ~62 min

=== NEW EVALS ===
Not launched — both trainings still in progress. Will need to wait ~1 hour.
```

Notable: M=32 and M=64 both hit exactly 61.6% overall SR, but with very different per-task distributions. M=64 is more balanced (fewer extreme highs/lows), while M=32 has higher variance (90% on chocolate pudding vs 28% on orange juice).

Training should finish in ~1 hour. Want me to check back then and launch the M=96/M=16 evals?

---
