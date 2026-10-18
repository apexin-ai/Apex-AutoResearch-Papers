# code llama echte analysis

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-echte-analysis_20260521T203818_result.json`
- **Structured JSON:** [`c50f9b5127e293d855dc.json`](../../sessions/c5/c50f9b5127e293d855dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the summary:

**Key Results — Llama-3.1-8B EC-HTE Analysis:**

| Metric | Llama-3.1-8B | Gemini (pilot) |
|--------|-------------|----------------|
| N | 500 | 500 |
| Overall accuracy | 0.754 | 0.780 |
| **Δπ** | **0.137** | **0.132** |
| max κ | 2.26 | 2.40 |
| Prop2 triggered | 1/4 subgroups | 3/4 subgroups |

**Δπ = 0.137 > 0.05** — confirms C1: Llama-3.1-8B exhibits subgroup-heterogeneous misclassification across hashtag × text-length subgroups. The `True_short` subgroup has the lowest error (π=0.140) while `False_medium` has the highest (π=0.277). Prop 2 diagnostic triggers for `True_short` (ratio=1.300), indicating asymmetric misclassification that would bias CATE.

**Output files:**
- `artifacts/c1_multi_llm/llama_analysis.md` — full report
- `artifacts/c1_multi_llm/llama_metrics.csv` — summary metrics (both Llama + Gemini pilot)
- `artifacts/c1_multi_llm/analyze_llama.py` — analysis script

---
