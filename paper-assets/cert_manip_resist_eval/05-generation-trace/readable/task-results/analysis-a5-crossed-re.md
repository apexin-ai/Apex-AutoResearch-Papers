# analysis a5 crossed re

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a5-crossed-re_20260524T114401_result.json`
- **Structured JSON:** [`c4330fdc0385a45890e3.json`](../../sessions/c4/c4330fdc0385a45890e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Results saved to `crossed_re_results.json`.

**Summary — Multi-Membership Clustered SE vs. Wild Cluster Bootstrap:**

| K | Bootstrap (K_eff FDR sig) | Crossed RE (K_eff FDR sig) | Crossed RE (raw sig) |
|---|---|---|---|
| 3 | 4/12 | **0/12** | 5/12 |
| 5 | 7/12 | **8/12** | 8/12 |
| 7 | 8/12 | **8/12** | 9/12 |

Key findings:

- **K=3**: The multi-membership CRVE is substantially more conservative — none of the 12 conditions survive FDR correction (vs 4/12 bootstrap). SE inflation from OLS is modest (1.75×–4.96×), reflecting the high overlap when 15 judges appear across only 455 panels of size 3.

- **K=5/K=7**: Results closely align with bootstrap. At K=5, CRVE finds 8/12 (vs 7/12 bootstrap); at K=7, both agree at 8/12. SE inflation is much larger (6×–19×), correctly accounting for the extreme overlap in C(15,5)=3003 and C(15,7)=6435 panels sharing the same 15 judges.

- **η_max** is mostly non-significant across all methods — the panel's maximum individual ASR is not a reliable predictor of panel-level attack success after accounting for crossed judge structure.

The core conclusion holds: **K_eff significantly predicts panel-level attack success for K≥5, robust to the crossed random effects structure.** The K=3 discrepancy with bootstrap is expected — with only 15 judges forming 455 3-judge panels, the effective degrees of freedom (df=14) severely limit power, making the CRVE approach appropriately conservative.

---
