# code gemma hetero tau

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma-hetero-tau_20260522T001443_result.json`
- **Structured JSON:** [`c0228a4b4926bbac14a4.json`](../../sessions/c0/c0228a4b4926bbac14a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Results:

- **CSV**: `gemma_hetero_tau_results.csv` — 4801 lines (4800 data + 1 header), matches expected count
- **Analysis**: `gemma_hetero_tau_analysis.md` — full report with all sections

**Key findings for Gemma-2-9B**:

| n_expert | |Bias| Global | |Bias| EC-HTE | Winner |
|----------|-------------|-------------|--------|
| 200 | 0.0261 | 0.0269 | Global |
| 500 | 0.0153 | 0.0117 | **EC-HTE** |
| 1000 | 0.0155 | 0.0157 | Global |

EC-HTE wins bias in only **1/3** budgets (n=500), vs 3/3 for both Llama and Qwen. Gemma's CM profile is quite different — small FPR heterogeneity (Δ_FPR=0.10) but large FNR heterogeneity (Δ_FNR=0.23), with strong FNR>FPR asymmetry. This means Global correction is already relatively accurate for Gemma, leaving less room for EC-HTE's subgroup-specific correction to improve on. Average Δ|Bias| improvement ranking: Llama (+0.016) > Qwen (+0.013) > Gemma (+0.001).

---
