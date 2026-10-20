# Multi-seed Inverse Scaling Recompute Report

## Setup

- **Dataset**: Few-NERD (32,565 gold-nonempty instances)
- **Models**: Qwen3-8B-FT, LLaMA-3.1-8B-FT
- **Seeds**: 42, 123, 456, 789 (Qwen N=8); 42, 456 (Qwen N=16); 42, 123, 456 (LLaMA N=8)
- **N values**: 2, 4, 6, 8 (N=8 configs); 2, 4, 6, 8, 16 (N=16 configs)
- **Methods**: majority_vote, lp_best, lp_weighted, vc_weighted, sj_weighted, theta2n, uniform
- **Significance**: Paired bootstrap, B=5000, 95% CI; sig inverse = entire CI below 0
- **Sub-sampling**: Uses first n samples from N_max data for fair comparison

## 1. Per-seed Transition Counts

| Config | Seed | N_max | Transitions | Inverse | Sig Inverse | Sig Positive |
|--------|------|-------|-------------|---------|-------------|--------------|
| Qwen_FewNERD_s42_n8 | 42 | 8 | 21 | 4 | 4 | 15 |
| Qwen_FewNERD_s123_n8 | 123 | 8 | 21 | 6 | 6 | 13 |
| Qwen_FewNERD_s456_n8 | 456 | 8 | 21 | 6 | 6 | 13 |
| Qwen_FewNERD_s789_n8 | 789 | 8 | 21 | 5 | 5 | 14 |
| Qwen_FewNERD_s42_n16 | 42 | 16 | 28 | 8 | 8 | 18 |
| Qwen_FewNERD_s456_n16 | 456 | 16 | 28 | 10 | 10 | 15 |
| LLaMA_FewNERD_s42_n8 | 42 | 8 | 21 | 8 | 8 | 13 |
| LLaMA_FewNERD_s123_n8 | 123 | 8 | 21 | 6 | 6 | 14 |
| LLaMA_FewNERD_s456_n8 | 456 | 8 | 21 | 6 | 6 | 14 |

**Key observation**: Every observed F1 drop is statistically significant (Inverse = Sig Inverse in all configs). Across Qwen N=8 seeds, sig inverse count ranges 4–6 out of 21 transitions (19–29%).

## 2. Direction Consistency

### Qwen N=8 (4 seeds: 42, 123, 456, 789)

- **All seeds agree inverse**: 4/21 transitions
- **All seeds same direction**: 15/21 transitions (71%)
- **Disagreements**: 6/21 — mostly borderline cases in vc_weighted, sj_weighted, theta2n

Transitions where **all 4 seeds** show sig inverse (p<0.05):

| Method | Transition | s42 | s123 | s456 | s789 |
|--------|-----------|-----|------|------|------|
| lp_weighted | N=6→8 | -0.51pp | -0.41pp | -0.63pp | -0.33pp |
| theta2n | N=6→8 | -0.97pp | -0.97pp | -1.24pp | -0.78pp |
| uniform | N=2→4 | -1.69pp | -2.96pp | -2.21pp | -3.11pp |
| uniform | N=6→8 | -0.97pp | -0.97pp | -1.24pp | -0.78pp |

### Qwen N=16 (2 seeds: 42, 456)

- **All seeds agree inverse**: 8/28 transitions
- **All seeds same direction**: 23/28 transitions (82%)
- N=8→16 amplifies inverse scaling: lp_weighted (-2.90pp/−2.99pp), theta2n (−3.63pp/−4.53pp), vc_weighted (−1.98pp/−2.09pp), sj_weighted (−1.00pp/−1.72pp) all sig inverse at N=8→16

### LLaMA N=8 (3 seeds: 42, 123, 456)

- **All seeds agree inverse**: 6/21 transitions
- **All seeds same direction**: 19/21 transitions (90%)
- Only 2 disagreements (lp_weighted N=4→6, sj_weighted N=6→8)

Transitions where **all 3 LLaMA seeds** show sig inverse:

| Method | Transition | s42 | s123 | s456 |
|--------|-----------|-----|------|------|
| lp_weighted | N=6→8 | -0.59pp | -0.56pp | -0.65pp |
| vc_weighted | N=6→8 | -0.19pp | -0.11pp | -0.13pp |
| theta2n | N=4→6 | -0.77pp | -0.52pp | -0.47pp |
| theta2n | N=6→8 | -1.10pp | -1.15pp | -1.13pp |
| uniform | N=2→4 | -3.09pp | -2.63pp | -2.48pp |
| uniform | N=6→8 | -1.10pp | -1.15pp | -1.13pp |

## 3. Per-method Breakdown

### Qwen N=8: Sig inverse transition count (out of 3 transitions per method)

| Method | s42 | s123 | s456 | s789 | Consistent? |
|--------|-----|------|------|------|-------------|
| majority_vote | 0 | 0 | 0 | 0 | YES (never inverse) |
| lp_best | 0 | 0 | 0 | 0 | YES (never inverse) |
| lp_weighted | 1 | 1 | 1 | 1 | YES |
| vc_weighted | 0 | 1 | 1 | 0 | NO |
| sj_weighted | 0 | 0 | 1 | 0 | NO |
| theta2n | 1 | 2 | 1 | 2 | NO |
| uniform | 2 | 2 | 2 | 2 | YES |

### LLaMA N=8: Sig inverse transition count (out of 3 transitions per method)

| Method | s42 | s123 | s456 |
|--------|-----|------|------|
| majority_vote | 0 | 0 | 0 |
| lp_best | 0 | 0 | 0 |
| lp_weighted | 2 | 1 | 1 |
| vc_weighted | 1 | 1 | 1 |
| sj_weighted | 1 | 0 | 0 |
| theta2n | 2 | 2 | 2 |
| uniform | 2 | 2 | 2 |

### Cross-model consistency summary

Methods that **never** show inverse scaling on any seed/model: **majority_vote**, **lp_best**

Methods that **always** show inverse scaling at N=6→8 across all 7 N=8 configs (both models, all seeds): **lp_weighted**, **theta2n**, **uniform**

## 4. Conclusions

1. **Inverse scaling is reproducible across seeds.** The 4 core inverse transitions (lp_weighted N=6→8, theta2n N=6→8, uniform N=2→4, uniform N=6→8) are significant in all 4 Qwen seeds — not a sampling artifact.

2. **Cross-model consistency.** The same pattern holds on LLaMA-3.1-8B-FT with even stronger agreement (19/21 same direction vs 15/21 for Qwen).

3. **Method stratification is clear.** majority_vote and lp_best are immune to inverse scaling; lp_weighted, theta2n, and uniform are consistently vulnerable; vc_weighted and sj_weighted are borderline.

4. **Larger N amplifies the effect.** N=16 configs show more inverse transitions (8–10/28) and larger drops (theta2n N=8→16: −3.63pp to −4.53pp).

5. **All F1 drops are significant.** Every observed inverse transition passes the bootstrap test — no cases of non-significant F1 decreases.
