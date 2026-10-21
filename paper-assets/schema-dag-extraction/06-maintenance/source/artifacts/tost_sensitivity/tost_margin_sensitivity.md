# TOST Margin Sensitivity Analysis

FewRel BCS-controlled experiments: count x confusability interaction term.


## A: d051 factorial (N=150)

2x2 factorial: Count(8 vs 16) x BCS(low/high, within-count median split). 3 seeds pooled (s42, s123, s456), 75 batches per count level.

- **Observed interaction (prob)**: -4.94 pp
- **90% CI (prob)**: [-8.97, -0.92] pp
- **Observed interaction (logit)**: -0.3424
- **90% CI (logit)**: [-0.6105, -0.0743]

| Margin (pp) | Scale | Observed Interaction | 90% CI | TOST p-value | Conclusion |
|---|---|---|---|---|---|
| +/-2 | Probability | -4.94 pp | [-8.97, -0.92] pp | 0.8860 | Inconclusive |
| +/-2 | Logit | -0.3424 | [-0.6105, -0.0743] | 0.9243 | Inconclusive |
| +/-2.5 | Probability | -4.94 pp | [-8.97, -0.92] pp | 0.8417 | Inconclusive |
| +/-2.5 | Logit | -0.3424 | [-0.6105, -0.0743] | 0.8978 | Inconclusive |
| +/-3 | Probability | -4.94 pp | [-8.97, -0.92] pp | 0.7873 | Inconclusive |
| +/-3 | Logit | -0.3424 | [-0.6105, -0.0743] | 0.8649 | Inconclusive |
| +/-3.5 | Probability | -4.94 pp | [-8.97, -0.92] pp | 0.7233 | Inconclusive |
| +/-3.5 | Logit | -0.3424 | [-0.6105, -0.0743] | 0.8254 | Inconclusive |
| +/-4 | Probability | -4.94 pp | [-8.97, -0.92] pp | 0.6509 | Inconclusive |
| +/-4 | Logit | -0.3424 | [-0.6105, -0.0743] | 0.7790 | Inconclusive |
| +/-5 | Probability | -4.94 pp | [-8.97, -0.92] pp | 0.4910 | Inconclusive |
| +/-5 | Logit | -0.3424 | [-0.6105, -0.0743] | 0.6676 | Inconclusive |

## B: d051 regression (N=375)

Multiple regression: accuracy ~ log2(count) + BCS + interaction, count levels 4-40 from 80-rel pool. 3 seeds pooled, 75 batches per count level x 5 count levels.

- **Observed interaction (prob)**: -0.37 pp
- **90% CI (prob)**: [-1.18, 0.44] pp
- **Observed interaction (logit)**: 0.0124
- **90% CI (logit)**: [-0.1262, 0.1509]

| Margin (pp) | Scale | Observed Interaction | 90% CI | TOST p-value | Conclusion |
|---|---|---|---|---|---|
| +/-2 | Probability | -0.37 pp | [-1.18, 0.44] pp | 0.0005 | Equivalent |
| +/-2 | Logit | 0.0124 | [-0.1262, 0.1509] | 0.1476 | Inconclusive |
| +/-2.5 | Probability | -0.37 pp | [-1.18, 0.44] pp | <0.0001 | Equivalent |
| +/-2.5 | Logit | 0.0124 | [-0.1262, 0.1509] | 0.0894 | Inconclusive |
| +/-3 | Probability | -0.37 pp | [-1.18, 0.44] pp | <0.0001 | Equivalent |
| +/-3 | Logit | 0.0124 | [-0.1262, 0.1509] | 0.0503 | Inconclusive |
| +/-3.5 | Probability | -0.37 pp | [-1.18, 0.44] pp | <0.0001 | Equivalent |
| +/-3.5 | Logit | 0.0124 | [-0.1262, 0.1509] | 0.0263 | Equivalent |
| +/-4 | Probability | -0.37 pp | [-1.18, 0.44] pp | <0.0001 | Equivalent |
| +/-4 | Logit | 0.0124 | [-0.1262, 0.1509] | 0.0127 | Equivalent |
| +/-5 | Probability | -0.37 pp | [-1.18, 0.44] pp | <0.0001 | Equivalent |
| +/-5 | Logit | 0.0124 | [-0.1262, 0.1509] | 0.0024 | Equivalent |

## C: 40rel factorial (N=54)

Original 2x2 factorial from fewrel_40rel_r4: Count(8 vs 16) x BCS(low/high, within-count median split). Single seed, ~27 batches per count level.

- **Observed interaction (prob)**: -3.77 pp
- **90% CI (prob)**: [-12.08, 4.55] pp
- **Observed interaction (logit)**: -0.2317
- **90% CI (logit)**: [-0.7122, 0.2488]

| Margin (pp) | Scale | Observed Interaction | 90% CI | TOST p-value | Conclusion |
|---|---|---|---|---|---|
| +/-2 | Probability | -3.77 pp | [-12.08, 4.55] pp | 0.6388 | Inconclusive |
| +/-2 | Logit | -0.2317 | [-0.7122, 0.2488] | 0.6668 | Inconclusive |
| +/-2.5 | Probability | -3.77 pp | [-12.08, 4.55] pp | 0.6005 | Inconclusive |
| +/-2.5 | Logit | -0.2317 | [-0.7122, 0.2488] | 0.6320 | Inconclusive |
| +/-3 | Probability | -3.77 pp | [-12.08, 4.55] pp | 0.5613 | Inconclusive |
| +/-3 | Logit | -0.2317 | [-0.7122, 0.2488] | 0.5960 | Inconclusive |
| +/-3.5 | Probability | -3.77 pp | [-12.08, 4.55] pp | 0.5214 | Inconclusive |
| +/-3.5 | Logit | -0.2317 | [-0.7122, 0.2488] | 0.5591 | Inconclusive |
| +/-4 | Probability | -3.77 pp | [-12.08, 4.55] pp | 0.4812 | Inconclusive |
| +/-4 | Logit | -0.2317 | [-0.7122, 0.2488] | 0.5217 | Inconclusive |
| +/-5 | Probability | -3.77 pp | [-12.08, 4.55] pp | 0.4019 | Inconclusive |
| +/-5 | Logit | -0.2317 | [-0.7122, 0.2488] | 0.4466 | Inconclusive |
