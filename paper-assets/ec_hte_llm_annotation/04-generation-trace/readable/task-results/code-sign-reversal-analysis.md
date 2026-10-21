# code sign reversal analysis

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sign-reversal-analysis_20260523T144810_result.json`
- **Structured JSON:** [`e589c0a3cd7ca9701987.json`](../../sessions/e5/e589c0a3cd7ca9701987.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs are generated. Here's the final report:

---

**Sign-Reversal Analysis Results**

**Synthetic data (K=2 grid, 546 configs):**
- **50%** of non-zero subgroup-rows (1000/2000) experience sign reversal
- **92%** of configs (500/546) have at least one affected subgroup
- Sign reversal occurs exclusively in subgroup B (π_B < π̄), where global correction overcorrects
- Top 5 most extreme cases all have high δ_misclass (0.23-0.25) and δ_cate (0.50), subgroup B with π_B = 0.025-0.035. Maximum flip magnitude = 0.1018.

**Real LLM data:**
- **215/435** subgroup-rows (49%) experience sign reversal across **all 8 LLMs**
- Affected across both datasets (CivilComments and TweetEval)
- All 8 LLMs (gpt-4o, gpt-4o-mini, gpt-3.5-turbo, gpt-4.1, gpt-4-turbo, Gemma-2-9B, Mistral-7B, Qwen2.5-7B) show sign reversal in at least some subgroups

**EC-HTE: 0% sign reversals** — per-subgroup correction is analytically unbiased, so it never introduces sign reversal.

**Outputs:**
- Figure: `artifacts/sign_reversal_figure.pdf` + `.png`
- CSV: `artifacts/sign_reversal_summary.csv` (1215 rows)

---
