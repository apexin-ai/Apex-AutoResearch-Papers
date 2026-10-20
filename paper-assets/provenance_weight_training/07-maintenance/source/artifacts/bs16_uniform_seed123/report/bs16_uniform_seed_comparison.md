# bs16_uniform: seed42 vs seed123 Comparison

## Results

| Metric | seed42 | seed123 | Δ (s123−s42) | Δ% |
|--------|--------|---------|--------------|-----|
| holdout_loss | 2.8732 | 2.8728 | −0.0004 | −0.01% |
| holdout_ppl | 17.694 | 17.686 | −0.008 | −0.05% |
| owt_loss | 2.9104 | 2.9107 | +0.0003 | +0.01% |
| owt_ppl | 18.364 | 18.369 | +0.005 | +0.03% |
| wiki_loss | 2.7302 | 2.7332 | +0.003 | +0.11% |
| wiki_ppl | 15.337 | 15.381 | +0.044 | +0.29% |
| train_loss | 1.965 | 1.997 | +0.032 | +1.63% |

## Conclusion

Two seeds produce nearly identical results across all eval metrics. Maximum difference is wiki_ppl at 0.29%, well within random seed noise. The uniform baseline at bs=16 is highly stable — any Δ(adaptive−uniform) > 0.5% can be attributed to the weighting method rather than seed variance.

Train loss shows the largest difference (1.63%), which is expected as it reflects single-run stochasticity rather than converged eval performance.
