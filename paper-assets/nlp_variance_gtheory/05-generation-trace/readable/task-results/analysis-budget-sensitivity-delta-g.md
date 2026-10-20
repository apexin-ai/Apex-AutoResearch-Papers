# analysis budget sensitivity delta g

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_budget_sensitivity_delta_g_20260522T145118_result.json`
- **Structured JSON:** [`5187669a4ef4692e56b1.json`](../../sessions/51/5187669a4ef4692e56b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。

**Summary Table — Budget Sensitivity to |ΔG|=0.035**

| Benchmark | σ²(item) | σ²(δ)₃ₓ₃ | n@0.800 | n@0.765 | n@0.835 | Δn (pessimistic) | %increase |
|-----------|----------|-----------|---------|---------|---------|-------------------|-----------|
| MMLU | 0.1271 | 0.0282 | 178 | 145 | 225 | +41 | 23.0% |
| ARC | 0.0671 | 0.0044 | 53 | 43 | 66 | +13 | 24.5% |
| HellaSwag | 0.0705 | 0.0071 | 81 | 66 | 103 | +19 | 23.5% |
| GSM8K | 0.0421 | 0.0153 | 291 | 237 | 368 | +67 | 23.0% |
| MATH | 0.0497 | 0.0136 | 220 | 179 | 278 | +51 | 23.2% |

**Δn interpretation**: If the actual G at planned n items is 0.035 lower than predicted (pessimistic), achieving G=0.800 requires ~23% more items. This percentage is constant across benchmarks because the ratio `(G/(1-G)) × ((1-G')/(G'))` depends only on the G values, not the variance components. Absolute Δn ranges from 13 (ARC) to 67 (GSM8K).

---
