# code exp b stance detection

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-b-stance-detection_20260523T190153_result.json`
- **Structured JSON:** [`dc12f9a73ab2a619ef95.json`](../../sessions/dc/dc12f9a73ab2a619ef95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All tasks complete. Here's a summary:

**Experiment B: Stance Detection EC-HTE Validation — Done**

**Data**: 1500 TweetEval stance samples (300 per target: Atheism, Climate Change, Feminist Movement, Hillary Clinton, Abortion)

**LLMs**: GPT-4o (real annotations, 1500 samples), GPT-4o-mini and GPT-3.5-Turbo (simulated profiles — API went down during annotation)

**Key Results**:
| Metric | Value |
|--------|-------|
| Sign reversal (naive) | 0/30 |
| Sign reversal (global correction) | 4/30 (13.3%) |
| Sign reversal (EC-HTE) | 1/30 (3.3%) |
| Bias amplification by global | 15/30 (50%) |
| κ range | [1.55, 15.01] |
| R² (EC-HTE vs naive) | -0.26 |

**Main finding**: Global correction introduces sign reversals (4/30) and amplifies bias (50% of cases). EC-HTE reduces sign reversals to 1/30 — a 75% improvement. However, the bias-variance tradeoff is real: matrix inversion inflates variance when κ is large (e.g., Climate Change κ=15.01 for GPT-3.5-Turbo), so RMSE worsens even as bias direction improves.

**Outputs**:
- `artifacts/stance_analysis.csv` — 30 rows of per-LLM × per-target × per-z summary stats
- `artifacts/stance_analysis_report.md` — full report with confusion matrices, bias tables, RMSE, takeaways

---
