# Qwen2.5-7B Budget Sweep Analysis

## Design

- N=5000, P(Z=1)=0.652
- tau(z=0)=0.35, tau(z=1)=0.65, Δτ=0.30
- n_expert sweep: [100, 200, 500, 1000, 2000]
- 50 MC seeds per budget
- HB method: MAP-EB (Gamma(3,1) prior)
- |Bias| = avg across cells of |mean(bias) across seeds|
- RMSE = avg across cells of sqrt(mean(bias²) across seeds)
- Coverage = avg across cells of fraction(95% CI contains true CATE)
- CI Width = avg across cells of mean(CI width across seeds)

## K=4 Summary

| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_naive | Cov_echte | CI_W_echte | HB>Naive_bias? | HB>Naive_rmse? |
|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|-----------|------------|----------------|----------------|
| 100 | 0.0737 | 0.0218 | 0.0692 | 0.0697 | 0.1138 | 0.1611 | 0.3810 | 0.3775 | 0.833 | 0.685 | 0.6570 | YES | no |
| 200 | 0.0737 | 0.0208 | 0.0354 | 0.0343 | 0.1138 | 0.1471 | 0.2371 | 0.2371 | 0.833 | 0.797 | 0.5458 | YES | no |
| 500 | 0.0737 | 0.0200 | 0.0250 | 0.0226 | 0.1138 | 0.1315 | 0.1668 | 0.1658 | 0.833 | 0.873 | 0.4954 | YES | no |
| 1000 | 0.0737 | 0.0204 | 0.0189 | 0.0177 | 0.1138 | 0.1274 | 0.1416 | 0.1408 | 0.833 | 0.902 | 0.4797 | YES | no |
| 2000 | 0.0737 | 0.0206 | 0.0213 | 0.0206 | 0.1138 | 0.1238 | 0.1262 | 0.1258 | 0.833 | 0.943 | 0.4744 | YES | no |

### K=4 Crossover Analysis

- **|Bias| crossover**: EC-HTE beats Naive at n_expert=100
- **RMSE crossover**: EC-HTE never beats Naive in tested range

### K=4 Bias-Variance Decomposition

| n_expert | Method | Bias² | Variance | MSE |
|----------|--------|-------|----------|-----|
| 100 | naive | 0.0068 | 0.0072 | 0.0140 |
| 100 | hb_ec_hte | 0.0065 | 0.1586 | 0.1651 |
| 200 | naive | 0.0068 | 0.0072 | 0.0140 |
| 200 | hb_ec_hte | 0.0022 | 0.0629 | 0.0651 |
| 500 | naive | 0.0068 | 0.0072 | 0.0140 |
| 500 | hb_ec_hte | 0.0009 | 0.0296 | 0.0305 |
| 1000 | naive | 0.0068 | 0.0072 | 0.0140 |
| 1000 | hb_ec_hte | 0.0007 | 0.0210 | 0.0217 |
| 2000 | naive | 0.0068 | 0.0072 | 0.0140 |
| 2000 | hb_ec_hte | 0.0008 | 0.0164 | 0.0172 |

## K=2 Summary

| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_naive | Cov_echte | CI_W_echte | HB>Naive_bias? | HB>Naive_rmse? |
|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|-----------|------------|----------------|----------------|
| 100 | 0.0716 | 0.0051 | 0.0132 | 0.0137 | 0.0929 | 0.1294 | 0.1663 | 0.1693 | 0.715 | 0.760 | 0.3743 | YES | no |
| 200 | 0.0716 | 0.0101 | 0.0122 | 0.0119 | 0.0929 | 0.1198 | 0.1376 | 0.1389 | 0.715 | 0.750 | 0.3452 | YES | no |
| 500 | 0.0716 | 0.0102 | 0.0105 | 0.0101 | 0.0929 | 0.0991 | 0.1099 | 0.1101 | 0.715 | 0.905 | 0.3350 | YES | no |
| 1000 | 0.0716 | 0.0061 | 0.0075 | 0.0073 | 0.0929 | 0.0886 | 0.0916 | 0.0916 | 0.715 | 0.925 | 0.3322 | YES | YES |
| 2000 | 0.0716 | 0.0077 | 0.0139 | 0.0139 | 0.0929 | 0.0882 | 0.0889 | 0.0889 | 0.715 | 0.950 | 0.3301 | YES | YES |

### K=2 Crossover Analysis

- **|Bias| crossover**: EC-HTE beats Naive at n_expert=100
- **RMSE crossover**: EC-HTE beats Naive at n_expert=1000

### K=2 Bias-Variance Decomposition

| n_expert | Method | Bias² | Variance | MSE |
|----------|--------|-------|----------|-----|
| 100 | naive | 0.0064 | 0.0032 | 0.0095 |
| 100 | hb_ec_hte | 0.0002 | 0.0317 | 0.0319 |
| 200 | naive | 0.0064 | 0.0032 | 0.0095 |
| 200 | hb_ec_hte | 0.0002 | 0.0211 | 0.0213 |
| 500 | naive | 0.0064 | 0.0032 | 0.0095 |
| 500 | hb_ec_hte | 0.0002 | 0.0131 | 0.0133 |
| 1000 | naive | 0.0064 | 0.0032 | 0.0095 |
| 1000 | hb_ec_hte | 0.0002 | 0.0089 | 0.0090 |
| 2000 | naive | 0.0064 | 0.0032 | 0.0095 |
| 2000 | hb_ec_hte | 0.0004 | 0.0081 | 0.0085 |

## K=4 vs K=2 Comparison

### K=4 HB EC-HTE |Bias| by budget

- n_expert=100: |Bias|=0.0697
- n_expert=200: |Bias|=0.0343
- n_expert=500: |Bias|=0.0226
- n_expert=1000: |Bias|=0.0177
- n_expert=2000: |Bias|=0.0206

### K=2 HB EC-HTE |Bias| by budget

- n_expert=100: |Bias|=0.0137
- n_expert=200: |Bias|=0.0119
- n_expert=500: |Bias|=0.0101
- n_expert=1000: |Bias|=0.0073
- n_expert=2000: |Bias|=0.0139
