# code perturbation eval wrapper

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_perturbation-eval-wrapper_20260516T050304_result.json`
- **Structured JSON:** [`6553aa073503ad3abffd.json`](../../sessions/65/6553aa073503ad3abffd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run completed successfully. Results:

- **libero_spatial with gaussian_noise (σ=0.05): 80% success rate** (8/10 tasks succeeded)
- No errors, all output files written correctly

Summary of deliverables:

| # | Deliverable | Status |
|---|------------|--------|
| 1 | `/root/acib/scripts/perturbation_wrapper.py` — 4 perturbation types + VectorEnv wrapper | Done |
| 2 | `/root/acib/scripts/eval_acib_perturbed.py` — eval script with perturbation support | Done |
| 3 | Dry-run validation — 1 episode × 10 tasks on libero_spatial, gaussian_noise=0.05 | Done (80% success) |
| 4 | `artifacts/perturbation_eval_guide.md` — usage documentation | Done |

Bonus fix: resolved the scorer dtype mismatch bug (bfloat16 vs float32) that also affects `eval_acib.py` — the perturbed eval script now explicitly casts `policy.scorer` to match the VLM's dtype.

---
