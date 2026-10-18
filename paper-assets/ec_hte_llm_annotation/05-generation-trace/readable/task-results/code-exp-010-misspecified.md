# code exp 010 misspecified

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-010-misspecified_20260521T095812_result.json`
- **Structured JSON:** [`febc09600cbdd5c5b914.json`](../../sessions/fe/febc09600cbdd5c5b914.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs are complete and well-structured. Here's the summary:

**exp-010 completed: 800 MC runs in 15 seconds.**

**Output files:**
- `results/exp010_misspecified_results.csv` — 19,200 detail rows
- `results/exp010_misspecified_summary.csv` — 32 summary rows
- `results/exp010_misspecified_analysis.md` — full report

**Key findings:**

1. **Bias elimination is robust**: Corrected methods maintain near-zero systematic bias (mean bias < 0.01) across all noise levels, vs naive's ±0.04-0.05 systematic bias.

2. **RMSE shows bias-variance tradeoff**: Corrected methods have slightly higher RMSE than naive because matrix inversion amplifies CM estimation noise. The difference is small and stable.

3. **Coverage is the decisive metric**: Naive achieves only 87-92% coverage (below nominal 95%). MLE/HB achieve 95-96% at all noise levels — this is the core argument for EC-HTE.

4. **HB consistently beats MLE**: +0.1% to +0.9% RMSE improvement from partial pooling, larger for K=4.

5. **Graceful degradation**: At p_flip=0.50, HB/MLE converge to global correction — no catastrophic failure. The EB shrinkage mechanism works as expected.

---
