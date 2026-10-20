# SciERC 5-Seed Holm-Bonferroni Statistical Test

**Date**: 2026-05-22
**Purpose**: Resolve R39 W4 concern (3-seed Holm-Bonferroni adjusted p=0.055)

## Data Source

All from `scierc_mf4v2_seed{SEED}/report.json` on autodl-5090. Unified MF4v2 pipeline, n=529 instances (551 total − 22 gold-empty).

## Per-Seed Metrics

| Seed | greedy_f1 | ρ_SJ | ρ_FK | ρ_LP | ρ_advantage (SJ−LP) |
|------|-----------|------|------|------|---------------------|
| 42   | 0.6651 | 0.3524 | 0.2507 | 0.2098 | 0.1426 |
| 123  | 0.6633 | 0.3681 | 0.2457 | 0.2209 | 0.1472 |
| 456  | 0.6631 | 0.3756 | 0.2832 | 0.2184 | 0.1572 |
| 2024 | 0.6641 | 0.3370 | 0.2356 | 0.1831 | 0.1539 |
| 3141 | 0.6609 | 0.3477 | 0.2074 | 0.1926 | 0.1552 |

## 5-Seed Summary

| Metric | Mean ± Std |
|--------|-----------|
| ρ_SJ   | 0.3562 ± 0.0140 |
| ρ_FK   | 0.2445 ± 0.0245 |
| ρ_LP   | 0.2050 ± 0.0148 |
| ρ_advantage (SJ−LP) | 0.1512 ± 0.0055 |
| greedy_f1 | 0.6633 ± 0.0014 |

## Test 1: SJ vs LP (Primary — Structural vs Surface)

**H₀**: ρ_SJ ≤ ρ_LP (structural consistency does not predict quality better than log-probability)

Method: Fisher z-transformation, one-sided, per-seed, then Holm-Bonferroni correction across 5 seeds.

| Seed | z | p_raw | p_adj (Holm-Bonf) |
|------|---|-------|-------------------|
| 42   | 2.517 | 0.00592 | 0.01295 |
| 123  | 2.622 | 0.00437 | 0.01295 |
| 456  | 2.804 | 0.00252 | 0.01261 |
| 2024 | 2.683 | 0.00364 | 0.01295 |
| 3141 | 2.723 | 0.00324 | 0.01295 |

**Max adjusted p = 0.0130 < 0.05 ✓**

All 5 seeds reject H₀ after Holm-Bonferroni correction. The structural consistency metric (Soft Jaccard) significantly outperforms the surface baseline (log-probability) as a quality predictor.

### Comparison with 3-seed result

- **3-seed** (R39 W4): Holm-Bonferroni adjusted p = 0.055 (borderline, not significant)
- **5-seed**: Holm-Bonferroni adjusted p = 0.013 (**significant at α=0.05**)

The additional seeds (2024, 3141) both show strong SJ > LP advantages (0.154, 0.155), consistent with the original 3 seeds.

## Test 2: SJ vs FK (Sensitivity — Between Structural Metrics)

| Seed | z | p_raw | p_adj (Holm-Bonf) |
|------|---|-------|-------------------|
| 42   | 1.816 | 0.0347 | 0.1041 |
| 123  | 2.196 | 0.0140 | 0.0562 |
| 456  | 1.682 | 0.0463 | 0.1041 |
| 2024 | 1.793 | 0.0365 | 0.1041 |
| 3141 | 2.473 | 0.0067 | 0.0335 |

Max adjusted p = 0.104. SJ vs FK does NOT reach family-wise significance — expected, as both are structural metrics.

## Alternative Analysis: Paired t-test

Treating ρ values as paired observations across seeds:

| Comparison | t | p (one-sided) |
|-----------|---|---------------|
| SJ vs LP | 55.44 | < 0.0001 |
| SJ vs FK | 12.81 | 0.0001 |

## Conclusion

**R39 W4 is resolved.** With 5 seeds, Holm-Bonferroni adjusted p = 0.013 (previously 0.055 with 3 seeds). The structural consistency advantage is statistically significant.

## Paper Update Locations

The following sections need updated numbers:
1. **Statistical significance claim**: Update "p = 0.055" → "Holm-Bonferroni adjusted p = 0.013" 
2. **Seed count**: Update "3 seeds" → "5 seeds" wherever SciERC seed count is mentioned
3. **Summary statistics**: Update ρ_SJ mean/std to 0.356 ± 0.014, ρ_advantage to 0.151 ± 0.006
4. **Results table**: Add seed 2024 and 3141 rows if individual seed results are shown

## Note on Method

The Fisher z-test treats the two correlations as independent, which overestimates the standard error (since SJ and LP are computed on the same instances). This makes the test conservative — the true p-values are even smaller. The paired t-test (p < 0.0001) confirms this.
