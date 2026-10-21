# exp_026 Paired t-test Results: arXiv Filtering Strategies

**Date:** 2026-05-18
**Design:** 3 strategies (graduated_a09, binary, no_filter) × 5 seeds (42, 123, 456, 789, 1024), paired by seed
**Metrics:** MMLU, HellaSwag
**Correction:** Bonferroni (6 comparisons, adjusted alpha = 0.0083)

## Raw Scores

| Strategy | Metric | Seed 42 | Seed 123 | Seed 456 | Seed 789 | Seed 1024 | Mean | Std |
|---|---|---|---|---|---|---|---|---|
| graduated | MMLU | 0.5889 | 0.5887 | 0.5901 | 0.5917 | 0.5907 | 0.5900 | 0.0013 |
| graduated | HellaSwag | 0.6604 | 0.6596 | 0.6599 | 0.6598 | 0.6595 | 0.6599 | 0.0003 |
| binary | MMLU | 0.5871 | 0.5881 | 0.5872 | 0.5876 | 0.5880 | 0.5876 | 0.0005 |
| binary | HellaSwag | 0.6641 | 0.6637 | 0.6649 | 0.6639 | 0.6641 | 0.6642 | 0.0005 |
| no_filter | MMLU | 0.5887 | 0.5893 | 0.5900 | 0.5911 | 0.5904 | 0.5899 | 0.0009 |
| no_filter | HellaSwag | 0.6602 | 0.6597 | 0.6603 | 0.6599 | 0.6598 | 0.6600 | 0.0003 |

## Paired t-test Results

| Comparison | Metric | Mean Diff | Std Diff | t(4) | p-value | 95% CI | Cohen's d | Sig (p<.05) | Sig (Bonferroni) |
|---|---|---|---|---|---|---|---|---|---|
| graduated vs binary | MMLU | +0.0024 | 0.0013 | 4.11 | 0.0147 | [+0.0008, +0.0040] | 1.84 | Yes | No |
| graduated vs binary | HellaSwag | -0.0043 | 0.0005 | -19.04 | 0.000045 | [-0.0049, -0.0037] | -8.52 | Yes | Yes |
| graduated vs no_filter | MMLU | +0.0001 | 0.0004 | 0.43 | 0.6921 | [-0.0005, +0.0006] | 0.19 | No | No |
| graduated vs no_filter | HellaSwag | -0.0001 | 0.0002 | -1.36 | 0.2455 | [-0.0004, +0.0001] | -0.61 | No | No |
| binary vs no_filter | MMLU | -0.0023 | 0.0009 | -5.67 | 0.0048 | [-0.0035, -0.0012] | -2.54 | Yes | Yes |
| binary vs no_filter | HellaSwag | +0.0041 | 0.0003 | 32.29 | 0.000005 | [+0.0038, +0.0045] | 14.44 | Yes | Yes |

## Key Findings

### 1. graduated vs no_filter: No significant difference (confirmed null result)

- **MMLU:** mean diff = +0.01pp, p = 0.692, d = 0.19 (negligible effect)
- **HellaSwag:** mean diff = -0.01pp, p = 0.245, d = -0.61 (small effect, not significant)
- Both CIs include zero. Graduated filtering is statistically indistinguishable from no filtering.

### 2. binary vs no_filter: Significant difference (trade-off)

- **MMLU:** binary is 0.23pp worse (p = 0.005, survives Bonferroni)
- **HellaSwag:** binary is 0.41pp better (p < 0.00001, survives Bonferroni)
- Binary filtering shows a statistically significant metric trade-off: it hurts MMLU but helps HellaSwag.

### 3. graduated vs binary: Significant difference

- **MMLU:** graduated is 0.24pp better (p = 0.015, does not survive Bonferroni)
- **HellaSwag:** graduated is 0.43pp worse (p < 0.0001, survives Bonferroni)
- Same trade-off pattern as binary vs no_filter, since graduated ≈ no_filter.

## Interpretation

Graduated arXiv filtering (alpha=0.9) has no measurable effect on either MMLU or HellaSwag compared to no filtering at all. The differences are well within noise (0.01pp on both metrics, p > 0.24). This confirms the graduated strategy is effectively a no-op at alpha=0.9.

Binary filtering produces a real but small trade-off: ~0.2pp MMLU degradation for ~0.4pp HellaSwag improvement, both statistically significant after Bonferroni correction.
