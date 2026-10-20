# tau_09_seed42 Post-hoc Eval

## Conclusion: NEGATIVE

PPL = 17.712 > uniform mean (17.694). Marginal difference (+0.018), but does not beat baseline.

## Eval Metrics

| Metric | Value |
|--------|-------|
| Perplexity | 17.712 |
| Loss | 2.8742 |
| Eval tokens | 4,077,068 |
| Eval data | data/human/eval_holdout.jsonl (5000 docs) |
| Model | output/models/tau_09_seed42/final (1.2GB) |

## b* Distribution (24,662 steps)

| Stat | Value |
|------|-------|
| Mean | 2.3561 |
| Median | 1.3200 |
| Std | 3.0416 |
| Min / Max | 0.0000 / 20.0000 |
| P25 / P75 | 0.7400 / 2.6400 |

### b* Range Breakdown

| Range | Percentage |
|-------|-----------|
| b*=0 | 0.3% |
| b*<0.5 | 10.0% |
| 0.5≤b*<1 | 27.7% |
| 1≤b*<2 | 28.6% |
| b*≥2 | 33.7% |

## Analysis

tau=0.9 produces a right-skewed b* distribution with median 1.32 and a long tail (33.7% ≥ 2). Despite aggressive provenance weighting, the model does not outperform uniform training. The high b* variance (std=3.04) suggests tau=0.9 amplifies noise in provenance scores without a consistent benefit.
