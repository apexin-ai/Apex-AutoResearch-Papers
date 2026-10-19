# ops deploy bjb1 32546 3gpu magnitude

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-bjb1-32546-3gpu-magnitude_20260517T235243_result.json`
- **Structured JSON:** [`c44819b07f0d48289db7.json`](../../sessions/c4/c44819b07f0d48289db7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 experiments confirmed running on bjb1-32546:

| GPU | exp_id | PID | VRAM | Status |
|-----|--------|-----|------|--------|
| cuda:1 | eval-obs-only-object-norm005-seed44 | 549432 | 5645 MiB | Running (since 07:10) |
| cuda:2 | eval-perdof-object-norm005-seed44 | 553052 | 5645 MiB | Running (since 07:31) |
| cuda:4 | eval-obs-only-object-norm02-seed43 | 557072 | 5462 MiB | Running (since 07:55) |

Note: Experiments 1 and 2 were already deployed by a previous session with identical parameters. Experiment 3 was freshly launched. GPU 4 also has a pre-existing perdof norm02 seed43 experiment (PID 535595, 5182 MiB) — both coexist with sufficient VRAM.

---
