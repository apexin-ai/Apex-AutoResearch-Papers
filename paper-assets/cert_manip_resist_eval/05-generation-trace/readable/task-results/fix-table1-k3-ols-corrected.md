# fix table1 k3 ols corrected

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_table1-k3-ols-corrected_20260523T175018_result.json`
- **Structured JSON:** [`38faf5a01ea45e560f27.json`](../../sessions/38/38faf5a01ea45e560f27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results summary:

**Error impact**: 1221/63000 scores invalid (1.94%), concentrated in Gemini models (gemini-3.5-flash: 742, gemini-3.1-pro-preview: 335). The bug `.get("winner", "tie")` treated these as ties, inflating η_max (high-error models = high-η models) and suppressing K_eff.

**5 of 12 conditions changed significance/dominance:**

| Condition | Old dom | New dom | Key change |
|---|---|---|---|
| MMLU × Score manip | η | **K** | η collapses 0.60→0.08, K rises 0.03→0.58 |
| MMLU × Position bias | η | **Co** | K gains sig, 0.10→0.38 |
| MMLU × Authority bias | η | **Co** | K gains sig, 0.01→0.50, R² doubles |
| ARC × Sycophancy | Co (K-) | **Co (K+)** | K sign flips −0.19→+0.26 |
| ARC × Verbosity | η | **Co** | K gains sig, 0.15→0.39 |

**Aggregate shift:**
- η sig: 11/12 → 10/12
- K sig: 8/12 → **12/12** (all conditions!)
- All K_eff betas now positive (was 1 negative)
- Dominance: {Co:7, η:4, K:1} → {**Co:10**, K:2, η:0}
- No pure η-dominant conditions remain

The corrected script is at `scripts/run_aggregation_loglog_corrected.py` on the server, corrected JSON saved to `artifacts/results/plan001/aggregation_regression_15model_loglog_corrected.json`, and the comparison at `docs/paper/data/table1_corrected.json` locally.

---
