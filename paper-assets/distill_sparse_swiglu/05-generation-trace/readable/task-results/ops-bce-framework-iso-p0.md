# ops bce framework iso p0

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bce-framework-iso-p0_20260516T191340_result.json`
- **Structured JSON:** [`03d33392ad922a8bc226.json`](../../sessions/03/03d33392ad922a8bc226.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training is running on cuda:1. Run 1 (lr=1e-4) completed successfully in ~17 min. Run 2 (lr=1e-3) has started. Summary so far:

**Run 1 (lr=1e-4) training complete:**
- Final BCE loss: ~0.716
- Final sparsity: ~0.512 (target: 0.50)
- Checkpoint saved: `checkpoints/bce_framework_lr1e4/predictor_bce_gumbel.pt`
- Training time: ~1012s (1.01s/step)

All framework components working correctly:
- Gumbel-sigmoid mask with tau annealing (1.0 → 0.1)
- Lagrangian constraint: lambda stabilized at 4.0, sparsity converged to ~50%
- BCE loss computed against magnitude oracle

Runs 2 (lr=1e-3) and 3 (lr=3e-3) are queued serially. Total ETA for all 3 runs: ~50 min from now. I'll check back when run 2 is further along.

---
