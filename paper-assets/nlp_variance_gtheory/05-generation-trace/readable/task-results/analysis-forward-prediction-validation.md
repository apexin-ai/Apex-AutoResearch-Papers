# analysis forward prediction validation

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_forward_prediction_validation_20260522T135327_result.json`
- **Structured JSON:** [`d32dd366066d93ad7cd2.json`](../../sessions/d3/d32dd366066d93ad7cd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 8-model actual G values match the bootstrap CI results exactly. Results saved to `artifacts/exp004/forward_prediction/forward_prediction_results.json`.

**Summary:**

| Benchmark | G(4m) | G_predicted | G_actual | ΔG | Error |
|-----------|-------|-------------|----------|--------|-------|
| MMLU | 0.816 | 0.888 | 0.896 | -0.009 | 0.96% |
| ARC | 0.831 | 0.904 | 0.892 | +0.012 | 1.38% |
| HellaSwag | 0.832 | 0.901 | 0.872 | +0.029 | 3.33% |
| GSM8K | 0.729 | 0.803 | 0.863 | -0.059 | 6.88% |
| MATH | 0.747 | 0.823 | 0.888 | -0.065 | 7.30% |

**Mean |ΔG| = 0.035, Mean relative error = 3.97%**

MC benchmarks (MMLU, ARC, HellaSwag) predict well — |ΔG| < 0.03. Free-form generation benchmarks (GSM8K, MATH) underpredict G by ~0.06, because the 4 source models' variance structure overestimates model×item interaction relative to the broader 8-model pool. This is a sensible pattern: the 4 original models share more similar generation capabilities, inflating model:item variance estimates. Adding 4 diverse new models dilutes model-specific item effects more than the D-study formula assumes.

---
