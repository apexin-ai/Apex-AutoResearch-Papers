# code exp 001 regularize

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-001-regularize_20260520T213804_result.json`
- **Structured JSON:** [`e962f2ea82f0a9d1c855.json`](../../sessions/e9/e962f2ea82f0a9d1c855.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

564 data rows (540 original + 24 new). CSV appended correctly, original data untouched.

**Summary of changes:**
1. **`exp001_hb_synthetic.py`**: Added `safe_invert_correction` (condition number guard, threshold=100) and `invert_mixing_safe` (full wrapper with SE propagation)
2. **`exp001_regularize.py`**: Standalone script that reruns 3 affected cells (300 MC runs) with `hb_dirichlet_reg` and `mle_laplace_reg` methods, appends 24 aggregated rows to the CSV
3. The `cond_threshold=100` is appropriate — it catches the near-singular matrices in K=4/extreme while leaving well-conditioned cells unchanged

---
