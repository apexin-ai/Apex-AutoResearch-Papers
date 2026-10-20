exp001b Resampling Stability G-Study

| Metric | exp-001 (6f) | Sample 1 | Sample 2 | Sample 3 | Mean±Std | CV% |
|--------|-------------|----------|----------|----------|----------|-----|
| item_id% | 61.08 | 75.88 | 75.38 | 72.18 | 74.48±2.01 | 2.7% |
| prompt×item% | 4.58 | 4.42 | 4.35 | 5.38 | 4.71±0.58 | 12.2% |
| seed×item% | 4.72 | 5.41 | 4.87 | 5.32 | 5.20±0.29 | 5.5% |
| temp×item% | 1.83 | 1.43 | 1.44 | 1.66 | 1.51±0.13 | 8.7% |
| G_item | 0.611 | 0.759 | 0.754 | 0.722 | 0.745±0.020 | 2.7% |

Conclusion: item_id dominance stable (CV=2.7%), hypothesis confirmed.
Note: exp-001b is 5-facet (bf16 only) vs exp-001 6-facet (3 precisions), so absolute % not directly comparable.
File: results/analysis/exp001b_resampling_gstudy.json