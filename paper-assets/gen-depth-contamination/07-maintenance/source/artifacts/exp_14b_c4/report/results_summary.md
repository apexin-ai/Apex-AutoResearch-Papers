# exp_14b_c4 Bootstrap CI Results

## Config
- Bootstrap: 10,000 doc-level resamples, percentile 95% CI
- Permutation test: 1,000 label permutations (doc-level)
- Threshold: θ = 0.60
- Seed: 42

## Pairwise AUC with 95% CI

| Pair | AUC | 95% CI | CI Width | Perm p-value |
|------|-----|--------|----------|-------------|
| 0v1 | 0.9598 | [0.9564, 0.9630] | 0.0066 | < 0.001 |
| 1v2 | 0.6210 | [0.6119, 0.6304] | 0.0185 | < 0.001 |
| 2v3 | 0.5494 | [0.5392, 0.5594] | 0.0202 | < 0.001 |
| 3v4 | 0.5243 | [0.5140, 0.5346] | 0.0206 | < 0.001 |
| 4v5 | 0.5154 | [0.5045, 0.5265] | 0.0220 | < 0.001 |

## K* Threshold Tests

- **1v2 CI lower (0.6119) > θ (0.60)**: SIGNIFICANT — K* >= 2 confirmed
- **2v3 CI upper (0.5594) < θ (0.60)**: SIGNIFICANT — K* <= 2 confirmed
- **Conclusion: K* = 2 is statistically confirmed** (both bounds hold)

## Interpretation

All pairs are significantly above chance (p < 0.001), confirming that LightGBM can detect distributional differences at every depth transition. The critical 1v2 pair has CI lower bound 0.6119, which clears the θ = 0.60 threshold by ~0.012. The 2v3 pair's CI upper bound (0.5594) falls well below θ, confirming that depth 3+ generations are no longer distinguishable at the θ = 0.60 criterion. K* = 2 is robust.

## Files
- Full results: `westd-42896:/root/autodl-tmp/gen-depth-contamination/results/exp_14b_c4/bootstrap_ci_results.json`
- Script: `westd-42896:/root/autodl-tmp/gen-depth-contamination/scripts/bootstrap_ci.py`
