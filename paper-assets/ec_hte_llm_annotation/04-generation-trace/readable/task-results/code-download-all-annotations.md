# code download all annotations

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_download-all-annotations_20260521T214803_result.json`
- **Structured JSON:** [`8b66d117b43eaab7369e.json`](../../sessions/8b/8b66d117b43eaab7369e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the summary:

**4-Model Misclassification Analysis (binary Z, K=4 subgroups, 'long' excluded)**

| Model | N | Accuracy | Δπ | max κ | Prop2 triggered |
|-------|---|----------|----|-------|-----------------|
| Llama-3.1-8B | 490 | 0.755 | 0.141 | 2.30 | 1/4 |
| Qwen-2.5-7B | 490 | 0.798 | 0.165 | 1.91 | 1/4 |
| Gemma-2-9B | 490 | 0.763 | 0.125 | 2.49 | 4/4 |
| Mistral-7B | 490 | 0.802 | 0.134 | 1.96 | 0/4 |

**Key findings:**
- All 4 models show Δπ > 0.05, confirming heterogeneous misclassification across subgroups
- `True_short` (has hashtag, short text) consistently has the lowest π_s across all models
- **Gemma-2-9B** triggers Prop2 in all 4 subgroups — strong FNR > FPR asymmetry (it under-predicts Z=1)
- **Mistral-7B** has the best accuracy (0.802) and triggers Prop2 in 0 subgroups — most balanced error profile
- **Qwen-2.5-7B** has the largest Δπ (0.165) with FPR=0.000 in `True_short`, creating extreme heterogeneity

**Output files:**
- `all_models_analysis.md` — full report with MLE + HB EB tables per model
- `all_models_metrics.csv` — 16 rows (4 models × 4 subgroups)
- `all_models_summary.csv` — 4-row model-level summary

---
