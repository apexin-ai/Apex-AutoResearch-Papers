# LLaMA 3.1-8B Cross-Model Statistical Tests

## Data Source (from registry, 3 training seeds: s123, s42, s0)

### Clean Eval (Success Rate)
| Variant | s123 | s42 | s0 | Mean | Std |
|---------|------|-----|-----|------|-----|
| TaxEI | 0.617 | 0.766 | 0.766 | 0.716 | 0.086 |
| Random | 0.766 | 0.766 | 0.745 | 0.759 | 0.012 |
| Vanilla | 0.723 | 0.723 | 0.723 | 0.723 | 0.000 |

### Recovery Eval (Recovery Rate under Error Injection)
| Variant | s123 | s0 |
|---------|------|----|
| TaxEI | 0.596 | 0.745 |
| Random | 0.787 | 0.745 |
| Vanilla | 0.702 | — |

### Injected Eval (s123 only)
| Variant | Success | Recovery | Detection |
|---------|---------|----------|-----------|
| TaxEI | 0.638 | 0.614 | 0.750 |
| Random | 0.702 | 0.689 | 0.533 |

---

## Test Results

### 1. Variance Tests (TaxEI vs Random, Clean Eval)

| Test | Statistic | p-value | Significant (α=0.05) |
|------|-----------|---------|---------------------|
| Levene's test (TaxEI vs Random) | 11.578 | 0.0272 | Yes |
| Levene's test (TaxEI vs Vanilla) | 16.000 | 0.0161 | Yes |
| F-test (variance ratio) | 50.342 | 0.0195 | Yes |
| Permutation test (variance ratio, 10k) | ratio=50.34 | 0.5074 | No |

**Interpretation**: TaxEI exhibits significantly higher cross-seed variance (std=0.086) compared to Random (0.012) and Vanilla (0.000). Levene's and F-test reach significance, but the permutation test does not — likely due to the small sample (n=3) making the permutation distribution highly discrete.

### 2. Mean Difference Tests

| Test | Statistic | p-value | Significant |
|------|-----------|---------|-------------|
| One-way ANOVA (3 groups) | F=0.628 | 0.5653 | No |
| Bootstrap 95% CI (TaxEI−Random) | diff=−0.043 | CI:[−0.142, 0.014] | No (CI crosses 0) |
| Bootstrap 95% CI (TaxEI−Vanilla) | diff=−0.007 | CI:[−0.106, 0.043] | No |

**Effect size**: Cohen's d (TaxEI vs Random) = −0.695 (medium-large), but not statistically significant with n=3.

### 3. Detection Rate (Injected Eval, Fisher Exact)

| Comparison | Odds Ratio | p-value | Significant |
|------------|-----------|---------|-------------|
| TaxEI (33/44) vs Random (23/45) | 2.625 | 0.0467 | Yes |

---

## Conclusions

1. **Variance instability**: TaxEI training produces significantly more variable models across seeds (Levene p=0.027). One seed (s123) underperforms badly (0.617) while s42/s0 match Random. This suggests the TaxEI curriculum's effectiveness is seed-sensitive.

2. **No mean difference**: Despite variance differences, average task performance is statistically indistinguishable across all 3 variants (ANOVA p=0.565). TaxEI training does not degrade clean task capability on average.

3. **Detection capability**: TaxEI-trained models detect injected errors significantly better (75% vs 53%, Fisher p=0.047, OR=2.6). This is the primary benefit of the TaxEI curriculum.

4. **Limitation**: n=3 seeds provides very low statistical power. The permutation test's non-significance (p=0.507) vs the parametric F-test's significance (p=0.020) highlights this — results should be interpreted with caution and ideally replicated with more seeds.
