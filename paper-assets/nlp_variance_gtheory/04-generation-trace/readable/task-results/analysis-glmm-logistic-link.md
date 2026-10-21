# analysis glmm logistic link

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_glmm_logistic_link_20260521T085643_result.json`
- **Structured JSON:** [`bc178602259a0d94153d.json`](../../sessions/bc/bc178602259a0d94153d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Results in `results/analysis/glmm_logistic_link.json`.

**Key findings:**

| Method | Ranking |
|--------|---------|
| Henderson I (linear) | item_id > model:item_id > model > prompt > temp > seed > ordering |
| Marginal logit ANOVA | item_id > model:item_id > model > prompt > temp > seed > ordering |

- **Spearman ρ = 1.0** across all 7 major components (3 item-related + 5 non-item main effects, deduplicating model)
- Top 3 components (item_id 42%, model:item_id 34%, model 0.7%) = 76.4% of total variance — identical order under logistic transform
- MQL-1 analytical result: for p̄ = 0.70, logistic transform applies constant scaling 1/[p̄(1−p̄)]² = 22.8, preserving all rankings exactly
- BinomialBayesMixedGLM (VB) converged on 25-item subsample but produced inflated estimates due to underspecification — noted as supplementary evidence, not primary

---
