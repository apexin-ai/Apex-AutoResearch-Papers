# analysis bootstrap ci all benchmarks

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_ci_all_benchmarks_20260522T024307_result.json`
- **Structured JSON:** [`f32cd54719435b8e65b7.json`](../../sessions/f3/f32cd54719435b8e65b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results summary — all 5 benchmarks × 8 models × 460,800 records × 1000 bootstrap resamples completed in 316s total:

| Benchmark | G_item | 95% CI | Top 3 components (%) |
|-----------|--------|--------|---------------------|
| **MMLU** | 0.896 | [0.874, 0.914] | item_id 37.9%, model:item_id 30.2%, residual 25.0% |
| **ARC** | 0.892 | [0.852, 0.919] | item_id 37.9%, model:item_id 33.7%, residual 15.4% |
| **HellaSwag** | 0.872 | [0.842, 0.896] | model:item_id 36.0%, item_id 34.3%, residual 21.4% |
| **GSM8K** | 0.863 | [0.832, 0.887] | residual 39.9%, item_id 16.9%, model:item_id 14.6% |
| **MATH** | 0.888 | [0.868, 0.903] | residual 43.9%, item_id 24.0%, model:item_id 17.3% |

Files saved to:
- Server: `results/exp004_8model_analysis/bootstrap_ci_{benchmark}.json`
- Local: `artifacts/exp004/data/bootstrap_ci_{benchmark}.json`

---
