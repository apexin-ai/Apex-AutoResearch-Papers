# Gamma Prior Sensitivity Analysis (RD2-M5)

## Setup
- DGP: K=2, pi_s=[0.05, 0.15], Delta_tau=0.3, n_expert=200, N=5000
- Gamma prior: shape in [1, 2, 3, 5, 10], scale in [0.5, 1, 2] (15 configurations)
  - Prior mean alpha_0 ranges from 0.5 to 20.0
- 20 MC seeds per configuration
- Method: MAP Empirical Bayes (penalized marginal likelihood with Gamma prior on alpha_0)

## HB RMSE by (shape, scale)

| shape | scale | prior mean | |bias| | RMSE | Coverage | pi MAE |
|------:|------:|-----------:|-------:|-----:|---------:|-------:|
|     1 |   0.5 |        0.5 | 0.0367 | 0.0825 | 0.938 | 0.0243 |
|     1 |   1.0 |        1.0 | 0.0367 | 0.0828 | 0.938 | 0.0244 |
|     1 |   2.0 |        2.0 | 0.0367 | 0.0831 | 0.938 | 0.0246 |
|     2 |   0.5 |        1.0 | 0.0367 | 0.0829 | 0.938 | 0.0244 |
|     2 |   1.0 |        2.0 | 0.0367 | 0.0834 | 0.938 | 0.0247 |
|     2 |   2.0 |        4.0 | 0.0367 | 0.0839 | 0.938 | 0.0255 |
|     3 |   0.5 |        1.5 | 0.0367 | 0.0834 | 0.938 | 0.0246 |
|     3 |   1.0 |        3.0 | 0.0367 | 0.0841 | 0.938 | 0.0256 | *
|     3 |   2.0 |        6.0 | 0.0367 | 0.0850 | 0.938 | 0.0269 |
|     5 |   0.5 |        2.5 | 0.0367 | 0.0843 | 0.938 | 0.0258 |
|     5 |   1.0 |        5.0 | 0.0366 | 0.0858 | 0.938 | 0.0282 |
|     5 |   2.0 |       10.0 | 0.0366 | 0.0875 | 0.925 | 0.0323 |
|    10 |   0.5 |        5.0 | 0.0366 | 0.0872 | 0.925 | 0.0318 |
|    10 |   1.0 |       10.0 | 0.0365 | 0.0910 | 0.938 | 0.0414 |
|    10 |   2.0 |       20.0 | 0.0365 | 0.0969 | 0.938 | 0.0553 |

\* = paper default Gamma(3, 1)

## Sensitivity Metrics

### Full range (all 15 configurations)
- RMSE range: 0.0825 to 0.0969 (delta = 0.0143)
- Best: shape=1, scale=0.5 (RMSE=0.0825)
- Worst: shape=10, scale=2.0 (RMSE=0.0969)
- Max RMSE difference: **17.3%**
- Coverage range: 0.925 to 0.938

### Reasonable prior range (shape <= 5, 12 of 15 configurations)
- RMSE range: 0.0825 to 0.0875
- Max RMSE difference: **6.0%**

### Paper default Gamma(3,1)
- RMSE = 0.0841
- Rank: 8 / 15 (1 = best)

## Comparison with Baselines

| Method | RMSE |
|--------|-----:|
| Stratified MLE (no prior) | 0.0848 |
| Global correction | 0.0797 |
| HB best (shape=1, scale=0.5) | 0.0825 |
| HB default Gamma(3,1) | 0.0841 |
| HB worst (shape=10, scale=2.0) | 0.0969 |

## Conclusion

1. **Prior sensitivity is low for reasonable priors.** Across shape in {1,2,3,5} and scale in {0.5,1,2} (12 configs), RMSE varies by only 6.0%. The full 15-config range (17.3%) is inflated by Gamma(10,2) (prior mean alpha_0=20), which over-regularizes the confusion matrix toward equal misclassification rates.

2. **The Gamma(3,1) default is not an outlier.** Its RMSE (0.0841) ranks 8/15 among all configs and is within 1.9% of the best.

3. **Coverage is stable.** Coverage ranges from 0.925 to 0.938 across all 15 configs, indicating the prior choice does not distort uncertainty quantification.

4. **Baselines context.** 9/15 HB configs outperform stratified MLE (RMSE=0.0848). The global correction (RMSE=0.0797) performs well in this K=2 moderate-heterogeneity setting where pooling across 2 subgroups is relatively safe; HB's advantage is more pronounced with larger K or more extreme heterogeneity (see exp-001 main results).
