# fix d126 kill long redeploy baseline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d126-kill-long-redeploy-baseline_20260522T204728_result.json`
- **Structured JSON:** [`f9aec77ab845581a7e41.json`](../../sessions/f9/f9aec77ab845581a7e41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both evals are running successfully — models loaded and stepping through eval batches.

## Summary

### Part 1: Kill Long precompute (bjb1-18228)
- PID 114506 **killed** successfully
- All 4 GPUs show ~9884 MiB residual memory (from other processes)

### Part 2: object_seed43/44 results (bjb1-32546)
Both complete:
| Eval | pc_success | n_episodes |
|------|-----------|------------|
| object_seed43_v2 | **66.5%** | 200 |
| object_seed44_v2 | **65.0%** | 200 |

Registry updated → DONE with metrics.

### Part 3: spatial_seed43 + goal_seed43 redeployed (bjb1-32546)
- `eval_spatial_s43` on cuda:0 → running, SmolVLM2 loaded, stepping through batches
- `eval_goal_s43` on cuda:1 → running, SmolVLM2 loaded, stepping through batches
- Log: `/tmp/eval_smolvla_{spatial,goal}_seed43_v3.log`
- Note: correct module path is `lerobot.scripts.lerobot_eval` (v0.5.2)

### Part 4: goal_seed44
**Pending** — will serial-run on same GPU after goal_seed43 completes.

### Part 5: SmolVLA CRM v1 training (bjb2-28827)
- **Epoch 32/50**, batch 1600/2190, loss ~0.009
- PID 344463, log at `~/runs/acr-vla-conformal-refinement/train-crm-smolvla-3suite-v1.log`
- Estimated ~64% through total training

---
