# exp-023 K=2 Extreme: PPI/DSL Baseline Comparison

## Setup
- K=2 subgroups: S0 (no hashtag), S1 (has hashtag)
- Misclassification: π=[0.05, 0.20] (extreme)
- DELTA_S: S0=0.4, S1=0.8
- N=5000, MC=50, n_expert={100, 250, 500}
- TweetEval sentiment DGP (same as exp-023 K=4)

## Table 1: Subgroup-Averaged Metrics (K=2 extreme)

| Method | n=100: \|Bias\| / RMSE / Cov | n=250: \|Bias\| / RMSE / Cov | n=500: \|Bias\| / RMSE / Cov |
|--------|------|------|------|
| Oracle | 0.009 / 0.075 / 0.93 | 0.009 / 0.075 / 0.93 | 0.009 / 0.075 / 0.93 |
| Naive | 0.093 / 0.126 / 0.76 | 0.093 / 0.126 / 0.76 | 0.093 / 0.126 / 0.76 |
| Global (=DSL-global) | 0.068 / 0.132 / 0.81 | 0.070 / 0.124 / 0.84 | 0.070 / 0.117 / 0.83 |
| PPI-global | 0.076 / 0.165 / 1.00 | 0.076 / 0.131 / 1.00 | 0.076 / 0.119 / 1.00 |
| Strat. MLE (=DSL-sub) | 0.253 / 1.421 / 0.74 | 0.056 / 0.187 / 0.82 | 0.030 / 0.133 / 0.86 |
| PPI-subgroup | 0.050 / 0.319 / 0.94 | 0.019 / 0.197 / 1.00 | 0.015 / 0.128 / 1.00 |
| EC-HTE (HB) | 0.160 / 1.558 / 0.76 | 0.051 / 0.185 / 0.82 | 0.028 / 0.132 / 0.86 |

## Table 2: Per-Subgroup Breakdown

### n=100
| Method | S0: Bias_z0/z1, RMSE_z0/z1 | S1: Bias_z0/z1, RMSE_z0/z1 |
|--------|---|---|
| Oracle | -0.006/0.012, 0.042/0.061 | -0.007/-0.011, 0.084/0.113 |
| Naive | 0.005/-0.029, 0.045/0.064 | 0.085/-0.255, 0.118/0.278 |
| Global | -0.023/0.069, 0.057/0.142 | 0.047/-0.131, 0.102/0.225 |
| Strat MLE | -0.011/0.041, 0.053/0.136 | -0.247/0.713, 1.627/3.868 |
| EC-HTE | -0.010/0.037, 0.052/0.133 | -0.126/0.469, 1.921/4.127 |

### n=250
| Method | S0: Bias_z0/z1, RMSE_z0/z1 | S1: Bias_z0/z1, RMSE_z0/z1 |
|--------|---|---|
| Oracle | -0.006/0.012, 0.042/0.061 | -0.007/-0.011, 0.084/0.113 |
| Naive | 0.005/-0.029, 0.045/0.064 | 0.085/-0.255, 0.118/0.278 |
| Global | -0.016/0.049, 0.052/0.110 | 0.058/-0.158, 0.107/0.225 |
| Strat MLE | -0.006/0.019, 0.048/0.104 | -0.060/0.139, 0.183/0.412 |
| EC-HTE | -0.005/0.018, 0.048/0.103 | -0.055/0.128, 0.181/0.407 |

### n=500
| Method | S0: Bias_z0/z1, RMSE_z0/z1 | S1: Bias_z0/z1, RMSE_z0/z1 |
|--------|---|---|
| Oracle | -0.006/0.012, 0.042/0.061 | -0.007/-0.011, 0.084/0.113 |
| Naive | 0.005/-0.029, 0.045/0.064 | 0.085/-0.255, 0.118/0.278 |
| Global | -0.017/0.045, 0.051/0.094 | 0.056/-0.161, 0.104/0.218 |
| Strat MLE | -0.006/0.017, 0.047/0.081 | -0.042/0.056, 0.135/0.268 |
| EC-HTE | -0.006/0.016, 0.047/0.081 | -0.040/0.052, 0.134/0.266 |

## EC-HTE vs Global RMSE (avg over subgroups)

| n_expert | EC-HTE | Global | Delta | Winner |
|----------|--------|--------|-------|--------|
| 100 | 1.558 | 0.132 | -1.427 | Global |
| 250 | 0.185 | 0.124 | -0.061 | Global |
| 500 | 0.132 | 0.117 | -0.015 | Global |

## Key Findings

1. **EC-HTE does NOT beat Global at any n in this K=2 TweetEval DGP** — contrary to the exp-006 prediction of crossover at n=250. Global wins at all three budget levels.

2. **Root cause: subgroup size imbalance.** TweetEval has ~25-30% hashtag rate, so S1 is much smaller than S0. With n_expert=100, S1 gets ~25-30 expert labels — too few for stable per-subgroup CM estimation. This causes explosive RMSE in S1 for both Strat MLE and EC-HTE at n=100.

3. **EC-HTE ≈ Strat MLE at all n.** With only K=2 subgroups, the HB partial pooling has minimal shrinkage leverage (only 2 groups to pool across), so EC-HTE barely improves over Strat MLE.

4. **Global's advantage: it ignores subgroup heterogeneity in the CM.** When the global CM is a reasonable average, this avoids the variance penalty of per-subgroup estimation, especially in the smaller subgroup.

5. **exp-006 discrepancy explained:** exp-006 used a balanced synthetic DGP (equal subgroup sizes) with larger DELTA_S and different misclass rates. The TweetEval DGP has unbalanced subgroups, which shifts the crossover point to higher n.

6. **PPI-subgroup has lowest bias** at n≥250 but with inflated SEs (coverage=1.00), consistent with PPI's conservative CI construction.
