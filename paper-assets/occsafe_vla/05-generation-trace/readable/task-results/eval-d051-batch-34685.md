# eval d051 batch 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d051_batch_34685_20260526T080507_result.json`
- **Structured JSON:** [`61a3df9773a455e3df7d.json`](../../sessions/61/61a3df9773a455e3df7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All registry entries updated. Here's the current status:

### Training Metrics (step 50000)

| Experiment | action_loss | occ_loss |
|---|---|---|
| detach_bn_v2_s0 (seed 42) | 0.0449 | 0.0095 |
| detach_bn_v2_s1 (seed 43) | 0.0513 | 0.0089 |
| detach_bn_v2_s2 (seed 44) | 0.0481 | 0.0094 |
| full_occ_bn_v2_s1 (seed 43) | 0.0583 | 0.0100 |

### Eval Status (westd-34685)

| Eval | GPU | Progress | ETA |
|---|---|---|---|
| detach_bn_v2_s0_eval | cuda:0 | T5 92% | ~30-40 min |
| detach_bn_v2_s1_eval | cuda:1 | T6 12% | ~30-40 min |
| detach_bn_v2_s2_eval | cuda:2 | T5 82% | ~35-45 min |
| full_occ_bn_v2_s1_eval | cuda:3 | T0 0% (just started) | ~90-120 min |

The first 3 evals should finish in ~30-45 min. full_occ_bn_v2_s1_eval just launched and will take ~1.5-2 hours. All logs at `~/runs/occsafe_vla/&lt;exp_id>.log`.

---
