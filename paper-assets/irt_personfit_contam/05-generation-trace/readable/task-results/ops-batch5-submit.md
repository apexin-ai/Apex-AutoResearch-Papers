# ops batch5 submit

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_batch5-submit_20260523T123755_result.json`
- **Structured JSON:** [`1462e5acb01ea58d568e.json`](../../sessions/14/1462e5acb01ea58d568e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 jobs are loading successfully:

| GPU | exp_id | Model | Condition | Seed | Status |
|-----|--------|-------|-----------|------|--------|
| 1 | exp-llama-5pct-s3 | llama | contam_5_s3 | 456 | Loading weights ✓ |
| 2 | exp-llama-25pct-s3 | llama | contam_25_s3 | 456 | Loading weights ✓ |
| 3 | exp-mistral-25pct-s2 | mistral | contam_25_s2 | 123 | Loading weights ✓ |

**Deferred:** exp-mistral-25pct-s3 (cuda:0 busy with Batch 4)

**Prep work done:**
- Generated `contam_5_s3` data (5702 items: 5000 alpaca + 702 MMLU, shuffle seed=456)
- Added `contam_5_s3: 456` to SEED_MAP in train.py

---
