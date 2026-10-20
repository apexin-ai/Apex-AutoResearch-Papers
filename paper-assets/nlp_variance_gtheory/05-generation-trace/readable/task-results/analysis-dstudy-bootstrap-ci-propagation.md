# analysis dstudy bootstrap ci propagation

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dstudy_bootstrap_ci_propagation_20260522T031753_result.json`
- **Structured JSON:** [`7fc4bcd2790534d76a69.json`](../../sessions/7f/7fc4bcd2790534d76a69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Results summary:

| Benchmark | Multi n(G≥0.80) | 95% CI | Single n(G≥0.80) | 95% CI | Ratio | 95% CI |
|-----------|-----------------|--------|-------------------|--------|-------|--------|
| MMLU | 93 | [76, 116] | 1216 | [1004, 1491] | 13.1× | [12.5, 13.7] |
| ARC | 98 | [71, 139] | 1078 | [793, 1512] | 11.0× | [10.7, 11.4] |
| HellaSwag | 118 | [93, 151] | 1403 | [1120, 1790] | 11.9× | [11.5, 12.3] |
| GSM8K | 128 | [103, 162] | 2768 | [2230, 3531] | 21.6× | [20.7, 23.0] |
| MATH | 101 | [86, 122] | 2160 | [1853, 2631] | 21.4× | [20.2, 22.5] |

**Verification**: ARC/HellaSwag/GSM8K/MATH point estimates match expected values exactly. Aggregates: MC ratio mean = 12.0× [11.6, 12.5], FF ratio mean = 21.5× [20.4, 22.8].

**MMLU note**: The expected MMLU values (multi=55, single=552) are from the original single-model 6-facet study (precision×temp×prompt×seed×ordering = 3×3×6×6×4). The 8-model G-study uses a different facet structure (model=8, temp=2, prompt=6, seed=6, ordering=4 → 2304 conditions), giving multi=93 and single=1216.

**Key takeaway for the paper**: The ratio CIs are tight — even the lowest CI bound across all benchmarks (ARC: 10.7×) far exceeds 1×, strongly supporting the "order-of-magnitude fewer items" claim. The reviewer's concern is addressed.

Output saved to:
- Server: `results/exp004_8model_analysis/dstudy_bootstrap_ci.json`
- Local: `artifacts/exp004/data/dstudy_bootstrap_ci.json`

---
