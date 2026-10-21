# Table 1: Perplexity Results Across Weighting Methods

**Aggregation**: ratio of means (mean PPL across seeds, then compute Δ relative to uniform mean)
**Baseline**: Uniform weighting, mean PPL = 17.694
**Data source**: Post-hoc eval (unified pipeline), all values from project registry

## Per-Seed PPL

| Method | Seed 42 | Seed 123 | Seed 456 | # Seeds | Mean ± Std | ΔPPL | Δ% |
|--------|---------|----------|----------|---------|------------|------|-----|
| Uniform | 17.694 | 17.686 | 17.702 | 3 | 17.694 ± 0.008 | — | — |
| Grid *b*=0.5 | 17.651 | 17.638 | 17.650 | 3 | 17.646 ± 0.007 | −0.048 | −0.3% |
| Grid *b*=1.0 | 17.692 | 17.674 | 17.680 | 3 | 17.682 ± 0.009 | −0.012 | −0.1% |
| Grid *b*=1.5 | 17.718 | 17.701 | 17.710 | 3 | 17.710 ± 0.009 | +0.016 | +0.1% |
| Grid *b*=2.0 | 17.741 | 17.725 | †       | 2 | 17.733 ± 0.011 | +0.039 | +0.2% |
| Grid *b*=3.0 | 17.774 | 17.760 | †       | 2 | 17.767 ± 0.010 | +0.073 | +0.4% |
| Grid *b*=5.0 | 17.818 | 17.804 | †       | 2 | 17.811 ± 0.010 | +0.117 | +0.7% |
| ESS-only | 17.730 | 17.720 | 17.719 | 3 | 17.723 ± 0.006 | +0.029 | +0.2% |
| Golden Ratio | 17.654 | — | — | 1 | 17.654 | −0.040 | −0.2% |
| Adaptive (ours, τ=0.8, n_min=2) | 17.653 | 17.643 | 17.657 | 3 | 17.651 ± 0.007 | −0.043 | −0.2% |

**ΔPPL**: negative = lower perplexity = better than uniform. Computed as method_mean − uniform_mean.
**Δ%**: (method_mean − uniform_mean) / uniform_mean × 100.

† Seed 456 results for *b*≥2.0 invalidated due to checkpoint resume artifact (+0.16–0.25 PPL bias); decision D026. Mean computed from 2 seeds (42+123) only.

## Key Findings

1. **Best fixed-*b***: *b*=0.5 achieves 17.646 (−0.048 PPL, −0.3%), consistent across all 3 seeds.
2. **Monotonic degradation with *b***: PPL increases monotonically from *b*=0.5 to *b*=5.0; higher *b* upweights synthetic data more aggressively, hurting performance.
3. **Adaptive**: 17.651 (−0.043 PPL, −0.2%), competitive with best grid but without requiring *b* tuning. Median b* ≈ 0.88 across seeds.
4. **ESS-only**: 17.723 (+0.029), worse than uniform — removing α_eff leads to over-downweighting.

## Std Computation

Sample standard deviation (Bessel-corrected, n−1 denominator). For 2-seed rows, std = |x₁−x₂| / √2.

## Data Source

All PPL values from post-hoc eval (unified pipeline), confirmed via project registry. Updated 2026-05-15.
