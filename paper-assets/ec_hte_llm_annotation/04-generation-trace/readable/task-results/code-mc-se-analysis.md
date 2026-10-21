# code mc se analysis

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mc-se-analysis_20260521T115138_result.json`
- **Structured JSON:** [`adc71445056ff89c4b29.json`](../../sessions/ad/adc71445056ff89c4b29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs saved. Here's the summary:

**Output files** in `artifacts/mc_se_analysis/`:
- `mc_se_table.csv` — 5040 rows of SE data across both experiments
- `paired_tests.csv` — 1020 paired comparisons
- `mc_se_summary.md` — full analysis with tables

**Key findings:**

**exp-001 (HB synthetic):** Conservative z-tests (no per-seed data). In extreme regime, bias differences between hb and naive are highly significant (p<0.0001). hb vs global_corrected bias is significant with n=500 (p<0.001) but not always with n=100.

**exp-003 (TweetEval):** Proper paired t-tests across 100 seeds. 73% of all comparisons are significant at α=0.05. hb_ec_hte vs naive: 190/240 significant. hb_ec_hte vs global_corrected: 174/240 significant.

**Director's question — moderate regime small differences:**
- At **n=50, 100**: Differences ARE significant (p<0.001 for most comparisons). Even small absolute differences are resolvable with 100 MC runs.
- At **n=250, 500 (z0)**: CIs **DO overlap** — differences between hb_ec_hte, global_corrected, and naive are NOT significant (p=0.06–0.99). The methods converge when heterogeneity is moderate and sample size is adequate.
- At **n=250, 500 (z1)**: hb_ec_hte vs global_corrected remains significant (p=0.002–0.04) but hb_ec_hte vs naive loses significance.
- **exp-001 K=4, moderate, n=250**: hb vs global_corrected NOT significant (p=0.29/0.37). hb vs naive borderline (p=0.038/0.07).

**Bottom line**: The small differences in the moderate regime (e.g., 0.009 vs 0.005) often have overlapping MC CIs at n≥250, confirming that methods converge when heterogeneity is mild. The main findings in extreme regimes are robust and statistically significant.

---
