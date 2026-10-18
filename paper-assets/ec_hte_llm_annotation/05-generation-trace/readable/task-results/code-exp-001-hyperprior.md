# code exp 001 hyperprior

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-001-hyperprior_20260520T220653_result.json`
- **Structured JSON:** [`761214a5330b08426397.json`](../../sessions/76/761214a5330b08426397.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Summary of changes:

1. **`exp001_hb_synthetic.py`** — Added `hp_a0=3.0, hp_b0=1.0` parameters to `_log_target_alpha` and `estimate_cm_hb_gibbs`. Defaults match the original Gamma(3,1) behavior, so no existing code is affected.

2. **`exp001_hyperprior_sensitivity.py`** — New script that sweeps `hyperprior_scale ∈ {0.5, 1.0, 2.0}` over K=2/moderate/n=250 with 100 MC runs. Scaling uses Gamma(a₀/s, b₀/s) to keep the prior mean fixed at 3 while varying variance (s=0.5 → tighter/more shrinkage, s=2.0 → wider/closer to MLE). Each run computes both HB and MLE baseline. Outputs `results/exp001_hyperprior_sensitivity.csv` and prints a condensed summary table.

Dry-run (2 MC) completed successfully in ~11s. Full 100 MC run is deferred per instructions.

---
