# Eval Report: tau_095_seed42

## Experiment
- **exp_id**: tau_095_seed42
- **τ (tau)**: 0.95
- **seed**: 42
- **contamination_ratio**: 0.4
- **hypothesis**: τ=0.95 is the most restrictive α_eff threshold; expected to over-constrain b* toward extreme values.

## Training Summary
- **train_loss**: 10.198
- **total_steps**: 6103
- **train_runtime**: 13698.6s (~3h48m)
- **train_samples_per_second**: 7.128
- **epoch**: 0.26

## Eval Results
- **eval_ppl_holdout**: 17.723
- **eval_loss**: 2.8749
- **eval_holdout_tokens**: 4,077,068
- **eval_method**: eval_perplexity.py (sliding window, stride=1024, max_docs=5000, autocast fp16)

## b* Statistics
| Metric | τ=0.95 (this) | τ=0.9 | τ=0.8 (baseline) | τ=0.7 | τ=0.6 | τ=0.5 |
|--------|---------------|-------|-------------------|-------|-------|-------|
| mean   | **3.078**     | 2.360 | 1.399             | 0.894 | 0.590 | 0.392 |
| median | **1.520**     | 1.320 | 0.871             | 0.580 | 0.375 | 0.171 |
| stdev  | **3.992**     | 3.040 | 1.933             | 1.401 | 1.069 | 0.882 |
| p25    | 0.800         | -     | 0.540             | 0.331 | 0.120 | 0.000 |
| p75    | 3.460         | -     | 1.512             | 0.971 | 0.660 | 0.437 |
| %>=2   | **40.3%**     | 33.7% | 16.1%             | 7.7%  | -     | 2.9%  |
| %<0.5  | 8.5%          | -     | 20.9%             | 36.0% | -     | 78.4% |

## Comparison with τ Sweep
| τ   | eval_ppl | Δ vs baseline | b* mean | conclusion |
|-----|----------|---------------|---------|------------|
| 0.5 | 17.688   | +0.035        | 0.392   | success    |
| 0.6 | 17.681   | +0.028        | 0.590   | success    |
| 0.7 | 17.679   | +0.027        | 0.894   | success    |
| **0.8** | **17.653** | **baseline** | **1.399** | **baseline** |
| 0.9 | 17.712   | +0.059        | 2.360   | negative   |
| **0.95** | **17.723** | **+0.070** | **3.078** | **negative** |

## Conclusion: NEGATIVE

τ=0.95 produces the worst PPL in the sweep (17.723, +0.070 vs baseline), confirming the hypothesis that very high τ over-constrains b*.

Key observations:
1. **b* inflation**: mean b*=3.08, with 40.3% of batches having b*≥2 (vs 16.1% at baseline). The optimizer is forced to push b* to extreme values to satisfy the strict α_eff≥0.95 constraint.
2. **Monotonic degradation above τ=0.8**: PPL degrades monotonically as τ increases beyond 0.8 (17.653 → 17.712 → 17.723).
3. **Asymmetric sensitivity**: τ is robust in [0.5, 0.8] (max PPL delta = 0.035) but degrades sharply above 0.8 (delta = 0.059–0.070).

**Implication for Claim 3**: τ is a robust hyperparameter within [0.5, 0.8], not across the full range. The paper should frame this as "robust in the practical range [0.5, 0.8]" with a clear upper boundary.
