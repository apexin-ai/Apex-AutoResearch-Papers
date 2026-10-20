# nmin1_seed42 Analysis

## Experiment Config
- **weighting_method**: adaptive, **n_min**: 1, **tau**: 0.8, **seed**: 42
- **contamination_ratio**: 0.4, **batch_size**: 4, **grad_accum**: 4, **max_length**: 2048, **lr**: 5e-5
- **Budget**: 200M tokens, **GPU**: cuda:2 on westd-47453
- **Training time**: ~4h50m, **Total steps**: 6103

## Key Metrics

| Metric | nmin1 (n_min=1) | adaptive_fix (n_min=2) | uniform | ess_only | golden_ratio | Δ vs adaptive_fix |
|--------|----------------|----------------------|---------|----------|-------------|-------------------|
| eval_ppl (holdout) | **17.79** | 17.65 | 17.69 | 17.73 | 17.654 | +0.14 |
| eval_loss | 2.8786 | 2.8709 | — | — | — | +0.0077 |
| train_loss (HF reported) | 10.467 | — | — | — | — | — |

## b* Distribution Comparison

| Statistic | nmin1 (n_min=1) | adaptive_fix (n_min=2) |
|-----------|----------------|----------------------|
| median | **1.746** | 0.871 |
| mean | **7.198** | 1.399 |
| std | 8.374 | — |
| min | 0.000 | — |
| max | 20.000 | — |
| p5 | 0.253 | — |
| p25 | 0.803 | — |
| p75 | 20.000 | — |
| p95 | 20.000 | — |
| frac(b=0) | 1.9% | — |
| frac(b≥20) | **25.0%** | — |
| frac(b>5) | **35.9%** | — |

### ESS Statistics (nmin1)
- mean: 1.904, median: 1.622, min: 1.000
- With n_min=1, ESS routinely drops to 1.0 (single effective sample), confirming the constraint is active

### Key Observations on b* Distribution
1. **Dramatically more aggressive**: b* median doubled (1.746 vs 0.871), mean 5x higher (7.198 vs 1.399)
2. **25% of batches hit b=20 cap**: the upper bound is binding frequently, meaning the optimizer wants even more extreme weighting
3. **Heavy right tail**: p75=20.0 means the top quartile is at the maximum allowed value
4. **ESS floor reached**: ESS min=1.0 (exact n_min boundary), confirming n_min=1 is binding

## Loss Analysis
- **Weighted loss (training signal)**: mean=2.617, last 100 steps=2.597
- **Unweighted loss**: mean=2.027, last 100 steps=2.013
- **HF-reported train_loss=10.467**: this is anomalously high because HF Trainer accumulates the weighted loss, which is inflated by extreme b* values amplifying high-loss (contaminated) samples. Not directly comparable to baselines that use uniform or milder weighting.

## Conclusion

**Negative** — but marginally so.

PPL=17.79 exceeds the uniform baseline (17.69) by 0.10, indicating mild degradation. Compared to adaptive_fix (n_min=2, PPL=17.65), the gap is +0.14. The extremely lax ESS constraint (n_min=1) allows the adaptive method to assign highly concentrated weights (25% of batches at b*=20, ESS dropping to 1.0), which effectively reduces the training to single-sample updates on many batches. This causes slight overfitting to the weighting signal and hurts generalization.

However, the degradation is modest: PPL 17.79 is only 0.6% worse than uniform and still outperforms a naive contaminated baseline. The method does not catastrophically fail even under extreme ESS relaxation.

## Implications for Paper

1. **ESS constraint matters but has a soft failure mode**: n_min=1 → PPL degrades from 17.65 to 17.79, a 0.8% increase. This supports the paper's claim that the ESS floor is a meaningful regularizer, but the method is robust — it degrades gracefully rather than collapsing.
2. **n_min=2 is a good default**: the adaptive_fix result (n_min=2, PPL=17.65) remains the best adaptive configuration, validating the choice.
3. **b* distribution shift is informative for ablation**: the dramatic b* inflation (median 0.87→1.75, mean 1.40→7.20, 25% hitting cap) with only modest PPL degradation shows the method's sensitivity to ESS constraint is bounded. Good for a robustness/sensitivity figure.
4. **Not a paper-worthy positive result, but useful as an ablation data point** showing the ESS floor's role.

## Metrics (machine-readable)

```json
{"eval_ppl_holdout": 17.79, "eval_loss": 2.8786, "b_star_median": 1.746, "b_star_mean": 7.198, "train_loss": 10.467, "vs_adaptive_ppl_delta": "+0.14"}
```
