# analyze ablation s0 eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_ablation-s0-eval_20260522T013218_result.json`
- **Structured JSON:** [`c994f2f79712cb482142.json`](../../sessions/c9/c994f2f79712cb482142.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Status summary:**

Both ablation trainings completed successfully (50005 steps, EXIT_CODE=0). Checkpoints are complete at 50000_chkpt with all expected components (4 model shards, action_head, occ_head, proprio_projector, lora_adapter).

**Currently running evals (6 total):**

| Experiment | Rollouts | GPU | PID | Status |
|---|---|---|---|---|
| ablation_occ_detach_s0 | 20r | GPU 0 | 614640 | running |
| ablation_random_occ_s0 | 20r | GPU 1 | 614641 | running |
| ablation_occ_detach_s1 | 20r | GPU 2 | 614642 | running |
| ablation_random_occ_s1 | 20r | GPU 3 | 614643 | running |
| ablation_random_occ_s0 | **50r** | GPU 1 | 615702 | T0: 72% |
| ablation_occ_detach_s0 | **50r** | GPU 0 | 632704 | T0: 4% (just launched) |

Estimated completion: ~25-30 min from now (both 50r evals). The 20r evals should finish in ~10-12 min.

Output paths:
- 50r detach: `/root/autodl-tmp/checkpoints/ablation_occ_detach_s0/eval_results.json`
- 50r random: `/root/autodl-tmp/checkpoints/ablation_random_occ_s0/eval_results.json`
- 20r all: `/root/occsafe_vla/eval_results/ablation_*_20r_50000.json`

I'll check back for results. Want me to poll periodically, or should I wait and check in ~30 minutes?

---
