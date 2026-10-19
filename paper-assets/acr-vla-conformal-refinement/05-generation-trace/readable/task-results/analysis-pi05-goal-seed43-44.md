# analysis pi05 goal seed43 44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi05-goal-seed43-44_20260522T155340_result.json`
- **Structured JSON:** [`70a527b2ce330aaf7a9f.json`](../../sessions/70/70a527b2ce330aaf7a9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both evals are still in progress — 4/10 tasks completed each. Note: actual `n_rollouts` is 20 (not 10 as stated in task), based on the logged args.

Here's what's available so far:

```
eval-pi05-vla-only-goal-seed43-r4:  [RUNNING - 4/10 tasks done, n_rollouts=20]
  per_task:
    open_the_middle_drawer_of_the_cabinet: 100.0% (20/20)
    put_the_bowl_on_the_stove: 100.0% (20/20)
    put_the_wine_bottle_on_top_of_the_cabinet: 95.0% (19/20)
    open_the_top_drawer_and_put_the_bowl_inside: 90.0% (18/20)
    put_the_bowl_on_top_of_the_cabinet: in progress (5/5 so far)
  overall_sr: N/A (still running)
  wandb_run_id: none found
  errors: none

eval-pi05-vla-only-goal-seed44-r4:  [RUNNING - 4/10 tasks done, n_rollouts=20]
  per_task:
    open_the_middle_drawer_of_the_cabinet: 90.0% (18/20)
    put_the_bowl_on_the_stove: 100.0% (20/20)
    put_the_wine_bottle_on_top_of_the_cabinet: 100.0% (20/20)
    open_the_top_drawer_and_put_the_bowl_inside: 85.0% (17/20)
  overall_sr: N/A (still running)
  wandb_run_id: none found
  errors: none
```

Key observations:
- Both evals are **still running** (4/10 tasks completed each)
- Actual `n_rollouts=20`, not 10
- No W&B integration found in logs
- No JSON results files yet (eval not complete)
- No errors or anomalies
- Partial average so far: seed43 = 96.25%, seed44 = 93.75% (across completed tasks only)

---
