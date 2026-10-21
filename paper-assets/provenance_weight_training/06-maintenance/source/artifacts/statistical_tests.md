# Statistical Significance Tests — Provenance Weight Training

## Methodology

**Test**: Paired bootstrap resampling (10,000 iterations)
**Samples**: 3 random seeds (42, 123, 456) per method
**Metric**: eval_ppl_holdout (lower is better)
**Dataset contamination rate**: ρ=0.4

### Limitation Statement

With only N=3 seeds, bootstrap resampling has very limited statistical power.
The test can only distinguish effects that are consistent across all 3 seeds.
A non-significant p-value means **insufficient evidence to reject H0** given the
small sample size — it does NOT mean the methods are equivalent. These results
should be interpreted as directional evidence, not definitive conclusions.

## ρ=0.4 Results (3-seed Bootstrap)

### Raw Data (eval_ppl_holdout)

| Method | seed=42 | seed=123 | seed=456 | Mean |
|--------|---------|----------|----------|------|
| Uniform | 17.6939 | 17.6861 | 17.7015 | 17.6938 |
| Adaptive (n_min=3, τ=0.8) | 17.6440 | 17.6308 | 17.6419 | 17.6389 |
| Adaptive_fix (n_min=2) | 17.6527 | 17.6432 | 17.6566 | 17.6508 |
| Grid-best (b=0.3/0.5) | 17.6400 | 17.6380 | 17.6500 | 17.6427 |
| ESS-only | 17.7300 | 17.7200 | 17.7190 | 17.7230 |

*Note: Grid-best uses b=0.3 for seed42, b=0.5 for seeds 123/456 (best grid value per seed).*

### Pairwise Comparisons

| Comparison | Mean Δ | 95% CI | p-value | Cohen's d | Sig. |
|-----------|--------|--------|---------|-----------|------|
| Adaptive (n_min=3) vs Uniform | -0.0549 | [-0.0596, -0.0499] | 0.0000 | -11.30 | *** |
| Adaptive_fix (n_min=2) vs Uniform | -0.0430 | [-0.0449, -0.0412] | 0.0000 | -23.22 | *** |
| Grid-best vs Uniform | -0.0512 | [-0.0539, -0.0481] | 0.0000 | -17.56 | *** |
| Adaptive (n_min=3) vs Grid-best | -0.0038 | [-0.0081, 0.0040] | 0.3002 | -0.56 | ns |
| Adaptive (n_min=3) vs ESS-only | -0.0841 | [-0.0892, -0.0771] | 0.0000 | -13.41 | *** |
| Adaptive_fix (n_min=2) vs ESS-only | -0.0722 | [-0.0773, -0.0624] | 0.0000 | -8.53 | *** |
| ESS-only vs Uniform | +0.0292 | [0.0175, 0.0361] | 0.0000 | 2.87 | *** |

*Significance: *** p<0.001, ** p<0.01, * p<0.05, ns = not significant*
*Negative Δ means the first method has lower (better) PPL.*

### Interpretation

- **Adaptive (n_min=3) vs Uniform**: Significant (p=0.0000). Adaptive (n_min=3) has lower PPL by 0.0549.
- **Adaptive_fix (n_min=2) vs Uniform**: Significant (p=0.0000). Adaptive_fix (n_min=2) has lower PPL by 0.0430.
- **Grid-best vs Uniform**: Significant (p=0.0000). Grid-best has lower PPL by 0.0512.
- **Adaptive (n_min=3) vs Grid-best**: Not significant (p=0.3002). Cannot distinguish with 3 seeds.
- **Adaptive (n_min=3) vs ESS-only**: Significant (p=0.0000). Adaptive (n_min=3) has lower PPL by 0.0841.
- **Adaptive_fix (n_min=2) vs ESS-only**: Significant (p=0.0000). Adaptive_fix (n_min=2) has lower PPL by 0.0722.
- **ESS-only vs Uniform**: Significant (p=0.0000). ESS-only has higher PPL by 0.0292.

## ρ=0.6 Results (Single Seed, No Statistical Test)

| Method | PPL | Δ vs Uniform |
|--------|-----|-------------|
| Uniform | 17.7660 | — |
| Adaptive τ=0.7 | 17.7300 | -0.0360 |
| Adaptive τ=0.8 | 17.7400 | -0.0260 |
| Adaptive τ=0.6 | 17.7359 | -0.0301 |
| ESS-only | 17.7700 | +0.0040 |

*Single-seed results. No statistical test is possible. Differences are point estimates only.*

## Summary

1. **Adaptive methods consistently outperform Uniform** across all 3 seeds (ρ=0.4), with the best variant (n_min=3, τ=0.8) achieving ~0.055 PPL reduction.
2. **ESS-only performs worse than Uniform**, indicating that ESS-based weighting without the adaptive component hurts performance.
3. **Grid-best is competitive with Adaptive**, suggesting the adaptive mechanism successfully finds near-optimal weighting without grid search.
4. **Statistical power is limited** with N=3. The consistency of direction across seeds provides confidence in the ranking, but precise effect sizes require more seeds.
5. **ρ=0.6 (single seed)**: Same directional pattern — adaptive methods improve over uniform, ESS-only is worst.
