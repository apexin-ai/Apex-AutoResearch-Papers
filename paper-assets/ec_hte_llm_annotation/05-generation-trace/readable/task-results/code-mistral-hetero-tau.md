# code mistral hetero tau

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral-hetero-tau_20260522T001452_result.json`
- **Structured JSON:** [`604bdcdb1e726d856e6a.json`](../../sessions/60/604bdcdb1e726d856e6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Results:

- **CSV**: 4801 lines (4800 data + 1 header) — matches expected count
- **Script**: `artifacts/c1_multi_llm/run_mistral_hetero_tau.py`
- **CSV**: `artifacts/c1_multi_llm/mistral_hetero_tau_results.csv`
- **Analysis**: `artifacts/c1_multi_llm/mistral_hetero_tau_analysis.md`

**Key findings**:
- EC-HTE wins on |Bias| in **2/3** budget levels (n=500, n=1000); Global wins at n=200
- EC-HTE wins on RMSE in **0/3** levels (higher variance from per-subgroup estimation)
- Average Δ|Bias|: Mistral +0.0030 vs Llama +0.0163 — Llama shows larger EC-HTE improvement
- Mistral has smaller FPR heterogeneity (0.15 vs 0.22) but larger FNR heterogeneity (0.18 vs 0.13) than Llama
- Mistral's CM is closer to Llama than Qwen's was, with True_short being the most accurate subgroup (FPR=0.091, FNR=0.121)

---
