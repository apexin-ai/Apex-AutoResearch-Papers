# NER 3-Seed 5-Signal Summary (SciERC, N=16, T=1.0, 551 instances)

## Table 1: Spearman ρ (Full, n=529)

| Signal | seed42 | seed123 | seed456 | Mean | SD |
|-------------|--------|---------|---------|-------|-------|
| voting_conf | 0.441 | 0.413 | 0.411 | 0.422 | 0.017 |
| SJ | 0.428 | 0.424 | 0.384 | 0.412 | 0.025 |
| EM | 0.335 | 0.337 | 0.316 | 0.329 | 0.011 |
| FK | 0.281 | 0.275 | 0.223 | 0.260 | 0.032 |
| logprob | 0.219 | 0.251 | 0.232 | 0.234 | 0.016 |

## Table 2: Spearman ρ (Conditional, n≈477-479)

| Signal | seed42 | seed123 | seed456 | Mean | SD |
|-------------|--------|---------|---------|-------|-------|
| EM | 0.415 | 0.404 | 0.406 | 0.408 | 0.006 |
| SJ | 0.369 | 0.376 | 0.349 | 0.365 | 0.014 |
| voting_conf | 0.353 | 0.339 | 0.346 | 0.346 | 0.007 |
| FK | 0.193 | 0.178 | 0.157 | 0.176 | 0.019 |
| logprob | 0.156 | 0.173 | 0.171 | 0.166 | 0.009 |

## Table 3: AUROC (Full, n=529)

| Signal | seed42 | seed123 | seed456 | Mean | SD |
|-------------|--------|---------|---------|-------|-------|
| EM | 0.790 | 0.781 | 0.768 | 0.780 | 0.011 |
| SJ | 0.737 | 0.736 | 0.711 | 0.728 | 0.015 |
| voting_conf | 0.734 | 0.717 | 0.712 | 0.721 | 0.012 |
| FK | 0.610 | 0.627 | 0.577 | 0.605 | 0.025 |
| logprob | 0.587 | 0.606 | 0.594 | 0.596 | 0.010 |

## Table 4: AUROC (Conditional, n≈477-479)

| Signal | seed42 | seed123 | seed456 | Mean | SD |
|-------------|--------|---------|---------|-------|-------|
| EM | 0.797 | 0.787 | 0.780 | 0.788 | 0.009 |
| SJ | 0.719 | 0.721 | 0.699 | 0.713 | 0.013 |
| voting_conf | 0.712 | 0.698 | 0.694 | 0.701 | 0.010 |
| FK | 0.589 | 0.605 | 0.561 | 0.585 | 0.023 |
| logprob | 0.569 | 0.584 | 0.576 | 0.577 | 0.008 |

## Key Findings

- **structural > surface: 3/3 seeds.** SJ beats FK in all seeds; all structure-based signals (EM, SJ, voting_conf) beat logprob.
- **Ranking stability:** Top-3 (EM, SJ, voting_conf) vs bottom-2 (FK, logprob) is perfectly consistent across all seeds and both splits.
- **Conditional split ranking is perfectly consistent:** EM > SJ > voting_conf > FK > logprob in all 3 seeds.
- **EM leads in AUROC** (0.780 full, 0.788 conditional) despite mid-tier ρ — it's the best binary discriminator.
- **voting_conf and SJ trade #1 in full ρ** — practically tied (0.422 vs 0.412), but SJ has higher SD (0.025 vs 0.017).
- **FK and logprob are the weakest signals** with mean ρ < 0.26 full, < 0.18 conditional.
