# Predictive Early-Stopping Rule: Gen-1 Metrics → Detection Outcome

## Objective

Determine whether gen-1 metric drifts can predict the final detection outcome (PermG ≥ 3/8 vs < 3/8), enabling early termination of the 11-generation iterative distillation loop.

## Data

- **19 experiments** from the alpha sweep (fp32 precision)
- Alpha range: 0.05–0.75; seeds: 42, 43, 44
- Datasets: WikiText (16 exps) + C4 (3 exps)
- Class split: 8 detected, 11 not detected

### Deduplication

For alpha/seed combinations with multiple runs (e.g., α=0.05 v2/v3/d080, α=0.60 v2/v3_d080/v4), the latest canonical version was kept. The `postd093` variant was excluded.

## Features

Relative drift from gen 0 → gen 1 for four metrics:

| Feature | Formula |
|---------|---------|
| `drift_token_entropy` | (gen1 − gen0) / |gen0| |
| `drift_distinct_1` | (gen1 − gen0) / |gen0| |
| `drift_ece` | (gen1 − gen0) / |gen0| |
| `drift_perplexity` | (gen1 − gen0) / |gen0| |

## Results

### Model Comparison (LOOCV AUROC)

| Model | AUROC | Accuracy |
|-------|-------|----------|
| Logistic Regression | 0.523 | 0.632 |
| Decision Tree (d=2) | 0.477 | 0.579 |
| Decision Tree (d=3) | 0.483 | 0.474 |
| **Random Forest** | **0.682** | **0.684** |

### Single-Feature AUROC

| Feature | AUROC |
|---------|-------|
| drift_token_entropy | 0.534 |
| drift_distinct_1 | 0.000 |
| drift_ece | 0.591 |
| drift_perplexity | 0.296 |
| **α alone (baseline)** | **0.773** |

### Decision Tree Structure (depth=2)

```
|--- drift_perplexity <= -0.1559
|   |--- class: Not detected
|--- drift_perplexity >  -0.1559
|   |--- drift_distinct_1 <= -0.0155
|   |   |--- class: Not detected
|   |--- drift_distinct_1 >  -0.0155
|   |   |--- class: Detected
```

### Error Analysis (6/19 misclassified)

| Experiment | α | True | P(det) | Error Type |
|-----------|---|------|--------|------------|
| c4_a025_s42 | 0.25 | 0 | 0.938 | FP — C4 drift pattern mimics collapse |
| c4_a075_s42 | 0.75 | 1 | 0.430 | FN — high α but low confidence |
| a010_s43 | 0.10 | 1 | 0.040 | FN — anomalous detection at very low α |
| a050_s44 | 0.50 | 1 | 0.333 | FN — seed 44 underconfident |
| a060_s43 | 0.60 | 0 | 0.960 | FP — high α but no detection |
| a075_s42 | 0.75 | 1 | 0.413 | FN — high α but low confidence |

## Key Findings

1. **Gen-1 drift features are not predictive** of final detection outcome. Best AUROC = 0.682 (Random Forest), well below the 0.70 threshold for appendix inclusion.

2. **α alone (AUROC = 0.773) outperforms all drift-based models.** This is trivially expected — higher contamination → more detectable — and provides no practical early-stopping value since α is known a priori.

3. **The signal-to-noise ratio at gen 1 is too low.** The lead-lag relationships that drive PermG detection emerge over multiple generations. Gen-1 drift captures initial training dynamics (perplexity recovery, entropy adjustment) that are shared across detected and undetected experiments.

4. **Dataset confound**: C4 experiments show dramatically different drift patterns (ECE drift 12–17x vs 0–5x for WikiText, perplexity drift +1.2–2.2x vs −0.3–0.2x). The model cannot distinguish C4's inherent drift from collapse signal.

5. **Boundary cases are inherently unpredictable**: a010_s43 (detected at α=0.10) and a060_s43 (not detected at α=0.60) have nearly identical gen-1 drift profiles to their non-anomalous seed counterparts, confirming that gen-1 information is insufficient.

## Conclusion

**Recommendation: NOT REPORTED** (AUROC < 0.70)

Gen-1 metrics do not carry enough information to predict which experiments will show detectable distributional collapse over the full 11-generation trajectory. Early stopping based on gen-1 drift would produce unacceptable false-negative and false-positive rates.

A useful early-stopping rule would likely require ≥3–5 generations of trajectory data, at which point the time savings become marginal.

## Artifacts

- `rule.json` — full model parameters, data, and predictions
- `fig_early_stop_auroc.pdf/png` — ROC curve
- `fig_gen1_scatter.pdf/png` — entropy drift vs α
- `fig_all_features_scatter.pdf/png` — 4-feature drift vs α
- `fig_predicted_prob.pdf/png` — LOOCV predicted probabilities
- `fig_feature_importance.pdf/png` — feature importance comparison
