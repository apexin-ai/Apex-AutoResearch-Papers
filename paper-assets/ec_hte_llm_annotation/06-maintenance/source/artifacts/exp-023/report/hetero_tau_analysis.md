# Heterogeneous-τ DGP: EC-HTE vs Global Correction

## Design

- N=5000, P(Z=1)=0.652, K=4 subgroups
- **Heterogeneous τ(z) across subgroups:**
  - False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1
  - False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1
  - True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
  - True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6
- n_expert sweep: [200, 500, 1000]
- 50 MC seeds per budget
- HB method: MAP-EB (Gamma(3,1) prior)
- |Bias| = avg across cells of |mean(bias) across seeds|
- RMSE = avg across cells of sqrt(mean(bias²) across seeds)

## Summary Table (averaged across all cells)

| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |
|----------|--------|-------|------|----------|----------|
| 200 | Naive | 0.0643 | 0.1141 | 0.858 | 0.335 |
| 200 | Global | 0.0365 | 0.1780 | 0.887 | 0.590 |
| 200 | Strat MLE | 0.0179 | 0.2561 | 0.800 | 0.646 |
| 200 | HB EC-HTE | 0.0248 | 0.2606 | 0.795 | 0.655 |
|----------|--------|-------|------|----------|----------|
| 500 | Naive | 0.0643 | 0.1141 | 0.858 | 0.335 |
| 500 | Global | 0.0314 | 0.1580 | 0.915 | 0.574 |
| 500 | Strat MLE | 0.0085 | 0.1750 | 0.900 | 0.576 |
| 500 | HB EC-HTE | 0.0099 | 0.1760 | 0.895 | 0.579 |
|----------|--------|-------|------|----------|----------|
| 1000 | Naive | 0.0643 | 0.1141 | 0.858 | 0.335 |
| 1000 | Global | 0.0286 | 0.1554 | 0.927 | 0.566 |
| 1000 | Strat MLE | 0.0131 | 0.1597 | 0.912 | 0.553 |
| 1000 | HB EC-HTE | 0.0130 | 0.1602 | 0.912 | 0.554 |
|----------|--------|-------|------|----------|----------|

## EC-HTE vs Global Comparison

| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |
|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|
| 200 | 0.0365 | 0.0248 | +0.0117 | 0.1780 | 0.2606 | -0.0826 | **YES** | no |
| 500 | 0.0314 | 0.0099 | +0.0215 | 0.1580 | 0.1760 | -0.0180 | **YES** | no |
| 1000 | 0.0286 | 0.0130 | +0.0156 | 0.1554 | 0.1602 | -0.0048 | **YES** | no |

## Per-Subgroup Breakdown

### n_expert = 200

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0135 | 0.0119 | +0.0016 | 0.1837 | 0.3011 |
| False_medium | 0.1 | 1 | 0.0083 | 0.0165 | -0.0082 | 0.0966 | 0.1544 |
| False_short | 0.1 | 0 | 0.0390 | 0.0090 | +0.0301 | 0.1996 | 0.3353 |
| False_short | 0.1 | 1 | 0.0104 | 0.0163 | -0.0059 | 0.1239 | 0.1937 |
| True_medium | 0.3 | 0 | 0.0044 | 0.0228 | -0.0185 | 0.2260 | 0.3332 |
| True_medium | 0.3 | 1 | 0.0218 | 0.0531 | -0.0313 | 0.1418 | 0.2161 |
| True_short | 0.6 | 0 | 0.1177 | 0.0351 | +0.0826 | 0.2691 | 0.3307 |
| True_short | 0.6 | 1 | 0.0771 | 0.0340 | +0.0431 | 0.1832 | 0.2204 |

### n_expert = 500

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0089 | 0.0058 | +0.0031 | 0.1407 | 0.2082 |
| False_medium | 0.1 | 1 | 0.0043 | 0.0103 | -0.0060 | 0.0807 | 0.1062 |
| False_short | 0.1 | 0 | 0.0417 | 0.0138 | +0.0279 | 0.1978 | 0.2307 |
| False_short | 0.1 | 1 | 0.0062 | 0.0031 | +0.0030 | 0.1137 | 0.1359 |
| True_medium | 0.3 | 0 | 0.0006 | 0.0131 | -0.0124 | 0.1893 | 0.2035 |
| True_medium | 0.3 | 1 | 0.0144 | 0.0245 | -0.0101 | 0.1131 | 0.1235 |
| True_short | 0.6 | 0 | 0.1117 | 0.0022 | +0.1095 | 0.2567 | 0.2253 |
| True_short | 0.6 | 1 | 0.0636 | 0.0063 | +0.0574 | 0.1717 | 0.1745 |

### n_expert = 1000

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0138 | 0.0054 | +0.0084 | 0.1278 | 0.1601 |
| False_medium | 0.1 | 1 | 0.0002 | 0.0017 | -0.0015 | 0.0750 | 0.0827 |
| False_short | 0.1 | 0 | 0.0358 | 0.0260 | +0.0098 | 0.1974 | 0.2054 |
| False_short | 0.1 | 1 | 0.0028 | 0.0049 | -0.0021 | 0.1101 | 0.1262 |
| True_medium | 0.3 | 0 | 0.0094 | 0.0059 | +0.0035 | 0.1902 | 0.2032 |
| True_medium | 0.3 | 1 | 0.0093 | 0.0224 | -0.0132 | 0.1154 | 0.1281 |
| True_short | 0.6 | 0 | 0.1020 | 0.0274 | +0.0745 | 0.2577 | 0.2117 |
| True_short | 0.6 | 1 | 0.0554 | 0.0103 | +0.0452 | 0.1693 | 0.1637 |

## Bias-Variance Decomposition

| n_expert | Method | Bias² | Variance | MSE |
|----------|--------|-------|----------|-----|
| 200 | Naive | 0.0077 | 0.0081 | 0.0158 |
| 200 | Global | 0.0028 | 0.0323 | 0.0351 |
| 200 | Strat MLE | 0.0005 | 0.0709 | 0.0714 |
| 200 | HB EC-HTE | 0.0008 | 0.0732 | 0.0740 |
| 500 | Naive | 0.0077 | 0.0081 | 0.0158 |
| 500 | Global | 0.0023 | 0.0260 | 0.0283 |
| 500 | Strat MLE | 0.0001 | 0.0332 | 0.0333 |
| 500 | HB EC-HTE | 0.0001 | 0.0336 | 0.0337 |
| 1000 | Naive | 0.0077 | 0.0081 | 0.0158 |
| 1000 | Global | 0.0019 | 0.0258 | 0.0277 |
| 1000 | Strat MLE | 0.0003 | 0.0276 | 0.0279 |
| 1000 | HB EC-HTE | 0.0003 | 0.0278 | 0.0280 |

## Comparison with Constant-τ DGP

Under **constant τ** (τ(z=0)=0.35, τ(z=1)=0.65 for all subgroups),
Global correction uses a pooled CM that is correct *on average*.
Since all subgroups share the same Δτ, Global's pooled correction is unbiased.

Under **heterogeneous τ**, Global's pooled CM applies a single correction
factor to all subgroups, but the true Δτ varies from 0.1 (False_medium/short)
to 0.6 (True_short). The correction's bias = δ_s × Δτ_s / (1−2π̄),
and since Global uses pooled δ instead of subgroup-specific δ_s,
it over-corrects subgroups with small Δτ and under-corrects those with large Δτ.

## Conclusion

EC-HTE wins on |Bias| in 3/3 budget levels.
EC-HTE wins on RMSE in 0/3 budget levels.

**Result: Under heterogeneous-τ DGP, EC-HTE consistently outperforms Global correction in bias.**
