# code exp 001 mcmc fix

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-001-mcmc-fix_20260520T220148_result.json`
- **Structured JSON:** [`c4b92399c64bb3436274.json`](../../sessions/c4/c4b92399c64bb3436274.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Results verified: `exp001_hb_results_v2.csv` has 588 data rows (540 original + 48 new), original file unchanged at 565 lines.

---

## Results Summary

### MCMC Diagnostic Comparison (2-chain → 4-chain)

| Config | R̂\_max (2ch) | R̂\_max (4ch) | ESS\_min (2ch) | ESS\_min (4ch) |
|---|---|---|---|---|
| K=4/extreme/n=50 | 1.0053 | 1.0023 | 381 | 1695 |
| K=4/extreme/n=100 | 1.0036 | 1.0019 | 396 | 1888 |
| K=4/moderate/n=50 | 1.0053 | 1.0023 | 381 | 1695 |
| K=4/moderate/n=100 | 1.0014 | 1.0028 | 422 | 1618 |
| K=4/homogeneous/n=50 | 1.0011 | 1.0034 | 480 | 1730 |
| K=4/homogeneous/n=100 | 1.0031 | 1.0012 | 483 | 2119 |

ESS improved ~4x across all configs. R̂ consistently below 1.01.

### Singularity Guard Triggers

Only `extreme/n=50` triggered guards (2 HB, 3 MLE out of 100 runs) and `extreme/n=100` (1 each). All other configs: zero triggers.

### RMSE: Key Findings

The regularization dramatically fixed the HB blowups in extreme regime:
- **K=4/extreme/n=50/B**: HB RMSE\_z0 dropped from **509.93 → 0.27** (guard + better MCMC)
- **K=4/extreme/n=50/A**: HB RMSE\_z0 dropped from **3.14 → 0.99**
- **K=4/extreme/n=100/A**: HB RMSE\_z0 dropped from **11.57 → 0.29**

For moderate/homogeneous cells, RMSE was already stable — regularized values essentially match originals (no regressions).

Output files:
- `results/exp001_hb_results_v2.csv` — 540 original + 48 new rows
- `results/exp001_reg_v2_run.log` — full run log

---
