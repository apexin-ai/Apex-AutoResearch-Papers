# MATH 8-model + Clean Permutation Test

## MATH 8-model Henderson I (with real DeepSeek)
- N = 460,800 (8 models × 57,600)
- item_id% = 24.03% [20.73, 27.17]
- G_item = 0.888
- model:item_id% = 17.28%
- residual% = 43.88%
- 7→8 model change: 26.48% → 24.03% (-2.45pp, within CI)

## Clean Permutation Test (all fixes applied)

| Benchmark | Format | item_id% |
|-----------|--------|----------|
| MMLU | MC | 37.88% |
| ARC | MC | 37.88% |
| HellaSwag | MC | 34.27% |
| GSM8K | FF | 16.86% |
| MATH | FF | 24.03% |

- MC mean: 36.68%, FF mean: 20.45%
- Diff: 16.23pp
- p = 0.10 (exhaustive, 1/10)
- Cohen's d = 1.73 [1.72, 1.83]
- Diff 95% CI: [11.44, 21.02]pp