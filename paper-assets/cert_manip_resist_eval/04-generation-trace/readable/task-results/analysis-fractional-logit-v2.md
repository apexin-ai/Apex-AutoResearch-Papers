# analysis fractional logit v2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fractional-logit-v2_20260523T193141_result.json`
- **Structured JSON:** [`634fca5c15db09464a5a.json`](../../sessions/63/634fca5c15db09464a5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

V2 fractional logit rerun complete.

**Results:**
- **Direction concordance: 98.6%** (V1 was 93.1%) — improved after V2 bug fix
- Only **1 direction flip** remains: K7 `arc_challenge × score_manipulation` for `eta_max` (frac_logit negative, OLS positive)
- **K_eff direction: 36/36 perfect concordance** across all K values and conditions
- Basic fractional logit sig counts are lower than OLS (conservative z-scored predictors), but robust HC1 variant closely matches OLS significance

Saved to `docs/paper/data/fractional_logit_corrected.json`.

---
