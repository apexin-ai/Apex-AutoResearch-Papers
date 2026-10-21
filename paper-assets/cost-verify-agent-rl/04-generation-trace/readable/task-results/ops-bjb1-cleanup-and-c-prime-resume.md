# ops bjb1 cleanup and c prime resume

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_cleanup_and_c_prime_resume_20260522T011602_result.json`
- **Structured JSON:** [`f09d297623938da42cc5.json`](../../sessions/f0/f09d297623938da42cc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training started successfully.

**Report:**

| Item | Value |
|------|-------|
| **PID** | 362509 (tmux), TaskRunner 365754, Workers 365951/365952 |
| **GPU memory** | cuda:0 = 11,113 MiB, cuda:1 = 11,113 MiB |
| **W&B run ID** | `ij377ngn` |
| **W&B run name** | `exp029-c-prime-resume` |
| **Status** | Checkpoint loaded from `global_step_5` (model + optimizer + rng + lr_scheduler on both ranks). Validation data loaded (494 items). Training started. |

Checkpoint resume confirmed:
- `[Rank 0] Loaded model from .../global_step_5/actor/model_world_size_2_rank_0.pt`
- `[Rank 1] Loaded optimizer from .../global_step_5/actor/optim_world_size_2_rank_1.pt`
- `[Rank 1] Loaded rng + lr_scheduler from extra_state`

The run will execute 2 training steps (step 6 → 7) and save a checkpoint at step 7 (last step trigger).

---
