# analysis kl sparsity70 s42 v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl_sparsity70_s42_v2_20260515T211314_result.json`
- **Structured JSON:** [`d418598aecce7e5b837a.json`](../../sessions/d4/d418598aecce7e5b837a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE/success. Analysis summary:

**kl_sparsity70_s42_v2 — SUCCESS (training converged)**

| Metric | Value |
|--------|-------|
| final_sparsity | 0.688 (target 0.70) |
| sparsity_range (last 200 steps) | 0.674–0.707 |
| final_kl_loss | 0.609 |
| final_constraint_loss | 0 |
| lambda_max | 1000 (hit cap at step 10) |
| tau_final | 0.100 |
| training_steps | 1000/1000 |
| wall_clock | ~41 min (0.68 GPU-hours) |
| checkpoint | `/root/distill_sparse_swiglu/checkpoints/kl_sparsity70_s42/predictor_kl_normalized.pt` |

**Key findings:**
- Sparsity converged quickly (~step 40) to ~0.68 and stayed stable throughout — well within the 0.65–0.75 success range
- lambda_max=1000 was sufficient (v1 was killed before reaching this; v2 with gradient_checkpointing ran to completion)
- Training was stable with no divergence or OOM

**Action needed:**
- **PPL evaluation not yet run.** The training script only logs KL/sparsity metrics. Need to run `evaluate.py` on the checkpoint to get `true_dense_ppl`, `predictor_hard_mask_ppl`, `teal_sparse_ppl` — these are critical for the plan_008 sparsity sweep comparison (30% vs 50% vs 70%).
- W&B run was offline — not synced to cloud.

---
