# d064 DocRED Full Dev Set (998 docs) — Status Report

**Report time**: 2026-05-19 20:50 CST
**Server**: westd-21461 (2× NVIDIA RTX PRO 6000 Blackwell, 98GB each)

## Summary

All tasks are **still running**. No files have completed yet. Both GPUs at 90% utilization.

## Pipeline Status

### GPU 0 — Llama Cascade

| Step | Status | Progress | Notes |
|------|--------|----------|-------|
| 1. Llama LoRA training | ✅ Complete | 3/3 epochs | train_loss=0.0571, eval_loss=0.0624, token_acc=0.9807 |
| 2. Llama LoRA merge | ✅ Complete | — | Saved to merged checkpoint |
| 3. Llama greedy unconstrained | 🔄 Running | 546/998 (54.7%) | Started 18:41, ~17s/doc, ETA ~23:00 |
| 4. Llama greedy constrained S1 | ⏳ Queued | — | After step 3 |
| 5. Llama beam-4 unconstrained | ⏳ Queued | — | After step 4 |
| 6. Llama beam-4 constrained S1 | ⏳ Queued | — | After step 5 |

### GPU 1 — Qwen Cascade

| Step | Status | Progress | Notes |
|------|--------|----------|-------|
| 1. Qwen beam-4 unconstrained | 🔄 Running | 614/998 (61.5%) | Started ~17:22, ~20s/doc, ETA ~23:00 |
| 2. Qwen beam-4 constrained S1 | ⏳ Queued | — | Waiting on PID 98185 |

## Estimated Completion Timeline

| Task | ETA |
|------|-----|
| Llama greedy unc (546→998) | ~23:00 May 19 |
| Qwen beam-4 unc (614→998) | ~23:00 May 19 |
| Llama greedy con (998 docs) | ~03:40 May 20 |
| Qwen beam-4 con (998 docs) | ~04:30 May 20 |
| Llama beam-4 unc (998 docs) | ~10:10 May 20 |
| Llama beam-4 con (998 docs) | ~16:40 May 20 |

## Notes

- Qwen beam-4 unc parse failures: 16/490 ≈ 3.3%
- Cascade scripts use `set -e`; chain stops on failure
- Server NOT restarted — original PIDs still running
- No evaluation metrics yet — need complete files first