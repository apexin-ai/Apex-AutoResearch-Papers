# ops fix bjb2 28827 failed but running

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-bjb2-28827-failed-but-running_20260518T023024_result.json`
- **Structured JSON:** [`eb17cfb26205644f7342.json`](../../sessions/eb/eb17cfb26205644f7342.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both re-registered as RUNNING. Summary:

**Both processes are running normally on bjb2-28827:**

| Experiment | Registry ID | PID | GPU | Uptime | Progress |
|---|---|---|---|---|---|
| obs_only norm0.1 seed42 | `eval-obs-only-object-norm01-seed42-r2` | 497445 | cuda:1 (5182 MiB) | ~2h38m | Task 2/10, rollout 6/10 |
| perdof norm0.1 seed42 | `eval-perdof-object-norm01-seed42-r2` | 497642 | cuda:3 (5182 MiB) | ~2h38m | Task 2/10, rollout 6/10 |

**What happened:** The original entries (`eval-*-object-norm01-seed42`) were marked failed at 02:11 UTC by startup recovery ("RUNNING with no cron and no server/pid info"). The processes were then restarted at 07:52 UTC and are progressing through LIBERO-Object evaluations (10 tasks x 10 rollouts each). At ~15min/task, they should finish in roughly another 2 hours.

**Registry state:** Original entries stuck at DEPLOYED (dead state from my recovery attempt). New `-r2` entries are now correctly tracking the running processes.

---
