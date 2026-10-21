# code exp 028 asymmetric diagnostic auc

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-028-asymmetric-diagnostic-auc_20260522T160245_result.json`
- **Structured JSON:** [`1e1e69407193c84b97e3.json`](../../sessions/1e/1e1e69407193c84b97e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results produced. Key findings:

**Overall AUC:**
- Symmetric: 0.6259
- Asymmetric: 0.6109 (slightly worse, -0.015)

**Per-combo:** Asymmetric outperforms symmetric for some combos (gpt-3.5-turbo/TweetEval 0→1, gpt-4.1 0.67→1) but underperforms for others (gpt-3.5-turbo/CivilComments 0.67→0.33, gpt-4o/CivilComments 0.33→0).

**Key observation:** For binary outcomes, the asymmetric scores for z=0 and z=1 are identical (confirmed in dry run output: `asym_score z=0: 0.1114, z=1: 0.1114`) because M is column-stochastic, so B_s columns sum to 0 and |B_s[0,1]| = |B_s[1,1]|. Analytically, the full DIM CATE bias from global correction reduces to `-2δ_s·τ_s/(1-2π̄)`, which depends only on the symmetric deviation δ_s, not on asymmetry. This explains why the asymmetric score (which captures only the FNR deviation component) doesn't improve over the symmetric score.

Output files:
- `results/exp_asymmetric_diagnostic_auc.csv` — 112 rows (56 subgroups × 2 z-levels)
- `results/exp_asymmetric_diagnostic_auc_summary.csv` — 16 combos with per-combo AUC

---
