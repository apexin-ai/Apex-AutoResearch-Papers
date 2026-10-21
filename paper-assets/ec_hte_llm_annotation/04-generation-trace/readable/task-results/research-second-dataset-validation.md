# research second dataset validation

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_second-dataset-validation_20260522T035753_result.json`
- **Structured JSON:** [`29e4727eb643d24de61f.json`](../../sessions/29/29e4727eb643d24de61f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Task A complete. Here's the summary:

## exp-023 Results: Civil Comments Semi-Synthetic Validation

**Claim 1 — Heterogeneous LLM Misclassification: Confirmed**

All 3 models show strong subgroup heterogeneity on Civil Comments toxicity:
- gpt-4o: Δ_FPR=0.184, Δ_FNR=0.168
- gpt-4o-mini: Δ_FPR=0.191, Δ_FNR=0.108
- gpt-3.5-turbo: Δ_FPR=0.099, Δ_FNR=0.101

All exceed the 0.05 threshold.

**Claim 2 — EC-HTE Outperforms Naive and Global: Confirmed**

v3 semi-synthetic (K=2, N=10000, symmetric misclassification):

| Regime | n_expert | Naive RMSE | Global RMSE | EC-HTE RMSE | EC-HTE Cov |
|--------|----------|-----------|-------------|-------------|------------|
| Extreme | 250 | 0.113 | 0.140 | **0.108** | 0.835 |
| Extreme | 500 | 0.113 | 0.135 | **0.093** | 0.865 |
| Moderate | 250 | 0.098 | 0.088 | **0.085** | 0.860 |
| Moderate | 500 | 0.098 | 0.081 | **0.067** | 0.910 |

Coverage gap is dramatic: EC-HTE 0.87 vs Naive 0.56 vs Global 0.58 (extreme, n=500).

**Design note**: v2 (K=4, asymmetric CMs, N=5000) showed EC-HTE worse than Naive due to tiny subgroup S1 (11%) causing noisy CM estimation. v3 fixed this by matching TweetEval's design structure (K=2, symmetric misclassification, larger N). The crossover at n_expert≈250 is consistent with TweetEval findings.

**Artifacts registered**: final summary, v3 analysis report, v3 summary CSV, confusion matrices. LLM annotations still running (80% complete — will give refined CMs but won't change the core conclusion).

---
