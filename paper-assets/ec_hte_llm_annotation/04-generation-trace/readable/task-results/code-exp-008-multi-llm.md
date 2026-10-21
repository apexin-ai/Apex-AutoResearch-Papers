# code exp 008 multi llm

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-008-multi-llm_20260521T081233_result.json`
- **Structured JSON:** [`d3ed82cb1f797962dd89.json`](../../sessions/d3/d3ed82cb1f797962dd89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline complete. Here's the summary:

**5 models analyzed** (500 tweets each, 100% valid annotations):

| Model | Δπ | Worst Subgroup |
|-------|-----|----------------|
| gpt-3.5-turbo | **0.3478** | True_short |
| gpt-4-turbo | **0.2240** | True_medium |
| gpt-4o-mini | **0.2160** | True_medium |
| gpt-4.1 | **0.2000** | True_medium |
| gpt-4o | **0.1760** | True_medium |

**Key findings:**
- **All 5 models show Δπ > 0.05** — misclassification heterogeneity is not model-specific
- **4/5 models agree** `True_medium` (hashtag-present, medium-length) is the hardest subgroup
- **Spearman rank correlations ρ = 0.82–1.00** (all p < 0.05) — the same subgroups are consistently harder across all models
- gpt-3.5-turbo has the largest Δπ (0.35), suggesting smaller models amplify the bias
- Interesting FPR/FNR split: gpt-3.5-turbo dominates FPR errors; gpt-4o dominates FNR errors — different models make different *types* of mistakes but the *subgroup heterogeneity pattern* is consistent

**Output files:**
- `results/exp008_available_models.txt` — 118 models on proxy
- `results/exp008_multi_llm_annotations.csv` — all annotations
- `results/exp008_multi_llm_comparison.csv` — per-model per-subgroup metrics
- `results/exp008_multi_llm_analysis.md` — full analysis report

---
