# LLaMA CoNLL-2003 NER N=16: 3-Seed 5-Signal Robustness Summary

Protocol: seeds 42/123/456 | Model: llama3.1-8b-conll2003-merged | Dataset: CoNLL-2003
N=16 samples, T=1.0 | 3453 instances, 2756 valid (gold_empty=697 filtered), 2642 conditional

## Full rho (Spearman correlation with greedy F1)

| Signal      | seed42 | seed123 | seed456 | Mean   | SD     | CV%  |
|-------------|--------|---------|---------|--------|--------|------|
| SJ          | 0.4642 | 0.4698  | 0.4552  | 0.4631 | 0.0074 | 1.6% |
| FK          | 0.4566 | 0.4594  | 0.4478  | 0.4546 | 0.0061 | 1.3% |
| EM          | 0.4613 | 0.4676  | 0.4520  | 0.4603 | 0.0078 | 1.7% |
| voting_conf | 0.4554 | 0.4612  | 0.4571  | 0.4579 | 0.0030 | 0.7% |
| logprob     | 0.3058 | 0.3161  | 0.3078  | 0.3099 | 0.0055 | 1.8% |

## Full AUROC

| Signal      | seed42 | seed123 | seed456 | Mean   | SD     |
|-------------|--------|---------|---------|--------|--------|
| SJ          | 0.7391 | 0.7402  | 0.7288  | 0.7360 | 0.0064 |
| FK          | 0.7360 | 0.7351  | 0.7248  | 0.7320 | 0.0063 |
| EM          | 0.7391 | 0.7399  | 0.7275  | 0.7355 | 0.0069 |
| voting_conf | 0.7406 | 0.7429  | 0.7348  | 0.7394 | 0.0041 |
| logprob     | 0.7594 | 0.7680  | 0.7612  | 0.7629 | 0.0044 |

## Conditional rho (greedy F1 > 0)

| Signal      | seed42 | seed123 | seed456 | Mean   | SD     | CV%  |
|-------------|--------|---------|---------|--------|--------|------|
| SJ          | 0.4597 | 0.4712  | 0.4505  | 0.4605 | 0.0104 | 2.3% |
| FK          | 0.4515 | 0.4595  | 0.4422  | 0.4511 | 0.0087 | 1.9% |
| EM          | 0.4618 | 0.4732  | 0.4510  | 0.4620 | 0.0112 | 2.4% |
| voting_conf | 0.3978 | 0.4086  | 0.3962  | 0.4009 | 0.0067 | 1.7% |
| logprob     | 0.3193 | 0.3314  | 0.3242  | 0.3250 | 0.0061 | 1.9% |

## Structural > Surface verdict: 3/3 seeds (full AND conditional)

## N=8 to N=16 scaling (mean delta across 3 seeds, full rho)
- SJ: +0.032 | FK: +0.027 | EM: +0.030 | voting_conf: +0.032 | logprob: +0.003
- Structural signals scale with N; logprob does not.

## Cross-protocol comparison with Qwen SciERC 3-seed
| Metric    | Qwen SciERC       | LLaMA CoNLL       |
|-----------|-------------------|-------------------|
| SJ mean   | 0.412             | 0.463             |
| SJ SD     | 0.025             | 0.007             |
| SJ CV%    | 6.0%              | 1.6%              |
| n_valid   | 529               | 2756              |
Higher magnitude, tighter variance. Both confirm structural > surface across all seeds.

## rho-AUROC dissociation
logprob has highest mean AUROC (0.763) but lowest mean rho (0.310).
Structural signals: mean AUROC ~0.735 but mean rho ~0.458.
Interpretation: logprob captures binary correct/incorrect well but misses fine-grained quality ranking.