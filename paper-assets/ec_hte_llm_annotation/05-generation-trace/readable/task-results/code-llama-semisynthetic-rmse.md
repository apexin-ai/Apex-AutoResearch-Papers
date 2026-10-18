# code llama semisynthetic rmse

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-semisynthetic-rmse_20260521T204338_result.json`
- **Structured JSON:** [`34b4daf726f24c0a3c6e.json`](../../sessions/34/34b4daf726f24c0a3c6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The analysis is complete and the bias-variance decomposition confirms the story clearly:

- **Naive**: Bias^2=0.0079, Var=0.0087, MSE=0.0165
- **HB EC-HTE**: Bias^2=0.0039, Var=0.0824, MSE=0.0863

EC-HTE halves the systematic bias (0.0039 vs 0.0079) but inflates variance by ~10x (0.0824 vs 0.0087), so total MSE is 5x worse.

All outputs produced:
- `artifacts/c1_multi_llm/llama_semisynthetic_results.csv` — 800 rows (20 seeds x 4 subgroups x 2 z-levels x 5 methods)
- `artifacts/c1_multi_llm/llama_semisynthetic_analysis.md` — full analysis with summary tables, per-subgroup breakdown, bias reduction ratios, bias-variance decomposition, and interpretation

**Key finding**: Under Llama's real CMs (Δπ=0.137, moderate heterogeneity) with n_expert=200, EC-HTE correction does NOT improve over Naive. The per-subgroup CM estimates (~28-77 expert labels per subgroup) are too noisy — the variance cost from inverting estimated mixing matrices exceeds the bias reduction benefit. EC-HTE would need larger expert budgets or greater CM heterogeneity to be beneficial.

---
