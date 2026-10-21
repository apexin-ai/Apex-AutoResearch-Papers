# code exp 003 mixing fix

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-003-mixing-fix_20260520T221750_result.json`
- **Structured JSON:** [`9ed6fc9d06e9693543ff.json`](../../sessions/9e/9ed6fc9d06e9693543ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass:

**Summary of changes:**

1. **`exp003_tweeteval.py`** — Fixed `build_mixing_matrix` to use Bayes' rule with empirical `P(Z)` and `P(Z_hat)` instead of assuming 0.5. Replaced `invert_mixing` with `invert_mixing_safe` (condition number guard). Updated output filenames to `_v2`.

2. **`exp001_hb_synthetic.py`** — Added docstring note that its `build_mixing_matrix` is correct only because the DGP uses `P(Z)=0.5`.

**Verification results (marginal, n_expert=500):**
- Oracle bias unchanged (Δ = 0) — correct, not affected by mixing matrix
- Global/Stratified `bias_z0` reduced by ~0.013–0.015 (closer to 0)
- Global/Stratified `bias_z1` shifted from ~−0.02 to ~+0.01–0.02 (magnitude reduced)
- Homogeneous regime: Global ≈ Stratified as expected

Output files: `results/exp003_phase_a_v2.csv` and `results/exp003_phase_a_v2_raw.csv`. Old files preserved.

---
