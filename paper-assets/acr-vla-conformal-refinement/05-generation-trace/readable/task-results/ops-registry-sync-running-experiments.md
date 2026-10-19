# ops registry sync running experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-sync-running-experiments_20260517T235138_result.json`
- **Structured JSON:** [`1871c4e4a90fb634b1d2.json`](../../sessions/18/1871c4e4a90fb634b1d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All experiments are already properly registered. Here's the summary:

**8 target experiments — all already registered as RUNNING with complete specs:**

| Experiment | Server | Status |
|---|---|---|
| eval-perdof-object-norm02-seed46 | bjb2-28827 | RUNNING ✓ (PID 389051, cuda:4) |
| eval-perdof-object-norm02-seed47 | bjb2-28827 | RUNNING ✓ (PID 404983, cuda:2) |
| eval-obs-only-object-norm005-seed43-r2 | bjb1-32546 | RUNNING ✓ (PID 433500, cuda:0) |
| eval-obs-only-object-default-seed46 | bjb1-32546 | RUNNING ✓ (PID 422357, cuda:3) |
| eval-perdof-object-default-seed46 | bjb1-32546 | RUNNING ✓ (PID 423767, cuda:5) |
| eval-random-selection-object-seed42 | bjb2-40593 | RUNNING ✓ (PID 395256, cuda:0) |
| eval-obs-only-object-norm01-seed48 | bjb1-18228 | RUNNING ✓ (PID 774342, cuda:1) |
| eval-obs-only-object-norm03-seed48 | bjb1-18228 | RUNNING ✓ (PID 774543, cuda:2) |

All entries have command, server, hypothesis, seed, model_name, and data fields populated.

**eval-obs-only-object-norm005-seed43:** Already DONE (conclusion: "killed"). Superseded by r2 (bjb1-32546) and r3 (bjb1-18228). Process is dead on bjb2-28827, log file exists but no output JSON — it died after completing only 1 of 10 tasks. No action needed.

**Bonus finding — additional unregistered experiments running:**
- bjb2-28827: perdof norm02 seed48, random_selection seed43
- bjb1-32546: perdof norm02 seed43, obs_only norm005 seed44, perdof norm005 seed44
- bjb1-18228: k1_accg seed43, obs_only norm02 K=5 seed42, perdof norm02 seed45

These may need registration separately if they're part of the experimental plan.

---
