# ops check default seed46 bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-default-seed46-bjb1-32546_20260518T002841_result.json`
- **Structured JSON:** [`2ec7603b577751160fde.json`](../../sessions/2e/2ec7603b577751160fde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron already cleaned up. Registry updated.

**Summary:**

| Field | Value |
|---|---|
| **Experiment** | eval-obs-only-object-default-seed46 |
| **Status** | DONE |
| **Conclusion** | **negative** |
| **Overall SR** | **0.15** (15%) |
| **Method** | crm_obs_only (uncapped correction, default config) |
| **Seed** | 46 |
| **Benchmark** | LIBERO-Object (10 tasks × 10 rollouts) |

**Per-task breakdown:**
- bbq_sauce: 0.4, orange_juice: 0.3, salad_dressing: 0.2, chocolate_pudding: 0.2
- ketchup: 0.1, tomato_sauce: 0.1, butter: 0.1, milk: 0.1
- alphabet_soup: 0.0, cream_cheese: 0.0

**Freed GPU:** `cuda:3` on bjb1-32546 (confirmed from spec).

The obs_only CRM with uncapped correction magnitude performs poorly at 15% overall SR, confirming that without norm constraint the correction magnitudes likely become unstable.

---
