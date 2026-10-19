# ops mass deploy bjb2 28827 6gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mass-deploy-bjb2-28827-6gpu_20260518T022736_result.json`
- **Structured JSON:** [`157fcb8bce8e2d04bb96.json`](../../sessions/15/157fcb8bce8e2d04bb96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**All 6 GPUs are currently occupied** with running Python processes:

| GPU | Memory Used | PID |
|-----|------------|-----|
| 0 | 5146 MiB | 492545 |
| 1 | 5182 MiB | 497445 |
| 2 | 1923 MiB | 404983 |
| 3 | 5182 MiB | 497642 |
| 4 | 5609 MiB | 514350 |
| 5 | 4717 MiB | 488665 |

**No GPUs are free.** All 6 GPUs have active Python processes with significant VRAM usage (1.9–5.6 GiB). Cannot deploy any of the 6 experiments.

Do you want me to:
1. Check what those processes are (tmux sessions / exp_ids)?
2. Kill specific jobs to free GPUs?
3. Wait and retry later?

---
