# D127 Multispatial CCM Results

## Method
- Clark et al. (2015) Multispatial CCM with 8 canary-downstream pairs as spatial replicates
- Per-pair CCM with Fisher-z aggregation (more reliable due to non-independent replicates)
- Both raw z-scored and first-differenced analyses
- E=2, tau=1, 200 surrogates per test

## Key Results: Per-Pair Analysis (Raw)

### alpha=0.50 (onset boundary) -- CLEANEST SIGNAL
| Canary | Downstream | Fwd rho | Fwd p | Rev rho | Rev p |
|--------|-----------|---------|-------|---------|-------|
| token_entropy | distinct_1 | +0.973 | 0.000** | -0.131 | 0.370 |
| token_entropy | distinct_2 | +0.954 | 0.000** | +0.031 | 0.280 |
| token_entropy | distinct_3 | +0.939 | 0.005** | +0.294 | 0.110 |
| token_entropy | mauve | +0.442 | 0.080 | -0.486 | 0.715 |
| ece | distinct_1 | +0.393 | 0.030* | +0.864 | 0.005** |
| ece | distinct_2 | +0.406 | 0.010* | +0.827 | 0.000** |
| ece | distinct_3 | +0.411 | 0.025* | +0.729 | 0.010* |
| ece | mauve | +0.197 | 0.100 | -0.143 | 0.345 |

**Finding**: token_entropy -> distinct_* shows strong unidirectional forward causality (rho>0.93, p<0.005) with non-significant reverse. This is clean CCM evidence of canary -> downstream.

### alpha=1.0 (full distillation)
- Both directions significant for most pairs (bidirectional coupling)
- Forward: 6/8 sig, Fisher-z agg rho=0.618
- Reverse: 8/8 sig, Fisher-z agg rho=0.963
- Interpretation: system too strongly coupled for directional discrimination

### alpha=0.0 (null baseline)
- Forward: 2/8 sig, Fisher-z agg rho=0.264
- Reverse: 1/8 sig, Fisher-z agg rho=-0.110
- Mostly non-significant as expected for null

## Caveats
1. Multispatial aggregation inflates reverse rho due to non-independent replicates (shared canary/downstream time series across pairs)
2. Per-pair analysis with T=11, E=2 gives only M=10 embedded points per pair -- marginal for CCM
3. First-differenced results less reliable (T=10 after diff, M=9 embedded points)
4. alpha=0.0 shows 2 significant forward pairs (token_entropy -> distinct_1/2), may be residual mild coupling or FDR issue

## Files
- Script: `/root/autodl-tmp/distrib_canary_collapse/scripts/d127_multispatial_ccm.py`
- Results JSON: `/root/autodl-tmp/distrib_canary_collapse/artifacts/d127_ccm/d127_multispatial_ccm.json`
- Convergence plots: `d127_convergence_curves.png`
- Summary plots: `d127_summary.png`
