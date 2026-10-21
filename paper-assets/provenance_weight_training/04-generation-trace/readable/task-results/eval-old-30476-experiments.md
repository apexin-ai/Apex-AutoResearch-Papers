# eval old 30476 experiments

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_old_30476_experiments_20260518T094911_result.json`
- **Structured JSON:** [`f87942cd970038c53659.json`](../../sessions/f8/f87942cd970038c53659.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the summary:

## Experiment Status

| Experiment | Status | Steps | PPL | Notes |
|---|---|---|---|---|
| **rho02_adaptive_tau08_seed42** | Completed + Eval'd | 6103/6103 | **17.382** | NEW result: ρ=0.2, adaptive, τ=0.8, n_min=2 |
| **grid_b0_1_seed42** | **Killed at step 1999** | 1999/6103 | — | Only ~33% done, no final checkpoint |
| **batchsize16_nmin8_r2** | Completed + Eval'd | 6103/6103 | 17.653 | Duplicate — matches prior bs=16 n_min=8 result exactly |

### Details

**rho02_adaptive_tau08_seed42** — This is the new result worth noting. Config: adaptive weighting, τ=0.8 (default), n_min=2, ρ=0.2, seed=42. PPL=17.382. Both training and eval were already completed (eval ran automatically after training finished). The eval file was at the actual output path `/root/autodl-tmp/output/models/rho02_adaptive_tau08_seed42/`.

**grid_b0_1_seed42** — Killed before completion when D&R experiments took the GPU. Last logged step was 1999. Only has checkpoints at 500/1000/1500. Since you already have b=0.1 seed42=17.657 from a prior run, this is a known duplicate — no need to resume.

**batchsize16_nmin8_r2** — Completed successfully, PPL=17.653 confirms the prior result exactly. No new information.

No eval runs needed — both completed experiments already have eval results on disk.

---
