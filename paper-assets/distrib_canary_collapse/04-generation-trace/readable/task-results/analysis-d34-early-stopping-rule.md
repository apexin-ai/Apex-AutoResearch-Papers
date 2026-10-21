# analysis d34 early stopping rule

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d34_early_stopping_rule_20260520T184918_result.json`
- **Structured JSON:** [`08a1f37841aa1bef6175.json`](../../sessions/08/08a1f37841aa1bef6175.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figures look good. The scatter plot visually confirms the core finding — detected (green) and not-detected (red) points overlap heavily in drift space, especially at α=0.60 where s42 is detected but s43 is not despite near-identical gen-1 drift.

## Summary

**Negative result**: Gen-1 metric drifts cannot predict final detection outcome.

| Model | LOOCV AUROC |
|-------|-------------|
| Random Forest (best) | 0.682 |
| Logistic Regression | 0.523 |
| Decision Tree | 0.477 |
| **α alone (baseline)** | **0.773** |

The α-alone baseline outperforms all drift-based models, confirming that gen-1 drift adds no predictive signal beyond what's already known from the experimental design. Key confounds: (1) C4 vs WikiText produce very different drift patterns, (2) seed-level variability at α=0.10 and α=0.60 makes the detection boundary intrinsically noisy.

**Recommendation: NOT REPORTED** (AUROC < 0.70).

All artifacts saved to `artifacts/early_stopping/`:
- `rule.json` — data + model parameters
- `early_stopping_report.md` — full analysis
- 5 figure pairs (PDF + PNG): ROC, scatter, 4-feature, predicted prob, feature importance

---
