# Component Count Analysis: plan001 vs plan013 vs plan002

**Date**: 2026-05-14
**Purpose**: Verify D017 hypothesis — does plan013 random reward achieve ISR≈0.5 via shorter formalizations?

## Verdict

**Yes. plan013 ISR≈0.5 is entirely an artifact of degenerate formalization length.**

The random reward model collapsed to generating exactly 2 components (1 premise + 1 conclusion) for every sample. With 2 components and 1 necessary, ISR = 1/2 = 0.5 mechanically. This is not meaningful structural quality — it is reward hacking via output minimization.

---

## Table 1: Component Count Statistics

| Experiment | Scope | N | mean_comp | median_comp | std_comp | mean_nec | mean_ISR |
|---|---|---|---|---|---|---|---|
| plan001-exec-only-s42 | all_samples | 100 | 6.580 | 7.0 | 3.153 | 0.720 | 0.1232 |
| plan001-exec-only-s42 | proved_only | 93 | 7.075 | 7.0 | 2.681 | 0.774 | 0.1324 |
| plan013-random-reward-s42-r4 | all_samples | 100 | **2.040** | **2.0** | **0.196** | 1.110 | 0.5350 |
| plan013-random-reward-s42-r4 | proved_only | 100 | **2.040** | **2.0** | **0.196** | 1.110 | 0.5350 |
| plan002-additive-b03 | all_samples | 100 | 1.920 | 0.0 | 4.496 | 0.250 | 0.0257 |
| plan002-additive-b03 | proved_only | 18 | 10.667 | 9.0 | 4.359 | 1.389 | 0.1427 |

### Key observations

- **plan013**: mean_comp=2.04 with std=0.196 → virtually every sample has exactly 2 components. 100% of samples fall in the 1-3 bucket. This is a degenerate collapse.
- **plan001**: mean_comp=6.58, healthy spread across 4-12 components. This represents meaningful multi-premise formalizations.
- **plan002**: Bimodal — 82/100 samples have 0 components (failed formalization), 18 proved samples have mean 10.7 components.
- **plan013 proves 100/100** (vs plan001 93/100) — trivial 2-component formalizations are easy for the solver to verify.

## Table 2: Pairwise Comparisons (Mann-Whitney U)

### plan001 vs plan013
| Metric | plan001 | plan013 | Δ | p-value |
|---|---|---|---|---|
| n_components | 6.580 | 2.040 | +4.540 | <0.0001 |
| n_necessary | 0.720 | 1.110 | -0.390 | <0.0001 |
| ISR | 0.123 | 0.535 | -0.412 | <0.0001 |

### plan001 vs plan002
| Metric | plan001 | plan002 | Δ | p-value |
|---|---|---|---|---|
| n_components | 6.580 | 1.920 | +4.660 | <0.0001 |
| n_necessary | 0.720 | 0.250 | +0.470 | <0.0001 |
| ISR | 0.123 | 0.026 | +0.097 | <0.0001 |

## Table 3: Spearman ρ(n_components, ISR)

| Experiment | Scope | ρ | p-value |
|---|---|---|---|
| plan001-exec-only-s42 | all | -0.071 | 0.485 |
| plan001-exec-only-s42 | proved | **-0.219** | **0.035** |
| plan013-random-reward-s42-r4 | all | +0.744 | <0.0001 |
| plan002-additive-b03 | all | +0.828 | <0.0001 |
| plan002-additive-b03 | proved | -0.176 | 0.485 |

- plan001 proved: weak negative ρ=-0.219 (p=0.035) — slight tendency for longer formalizations to have lower ISR, consistent with more redundant premises.
- plan013: strong positive ρ=+0.744, but this is meaningless — range is 2-3 components, no real variation.

## Table 4: Per-Sample Paired Comparison (plan001 vs plan013)

- **100 common samples**
- Δn_components (plan013 − plan001): mean=**-4.54**, median=-5.0
  - plan013 FEWER: **93 samples** | EQUAL: 0 | MORE: 7
- Δn_necessary: mean=+0.39, median=+1.0
- ΔISR: mean=+0.41, median=+0.50
- Wilcoxon signed-rank (n_components): W=144, **p<0.0001**
- Wilcoxon signed-rank (ISR): W=88, **p<0.0001**

**93/100 samples** have fewer components in plan013 than plan001. The ISR improvement is entirely driven by denominator shrinkage, not numerator growth.

## Table 5: Component Count Distribution

| Bucket | plan001 | plan013 | plan002 |
|---|---|---|---|
| 1-3 | 11 | **100** | 0 |
| 4-6 | 30 | 0 | 2 |
| 7-9 | 39 | 0 | 8 |
| 10-12 | 11 | 0 | 2 |
| 13-15 | 1 | 0 | 5 |
| 16-20 | 1 | 0 | 0 |
| 21+ | 0 | 0 | 1 |

## Mechanism Explanation

Random reward provides no gradient signal for formalization quality — the model receives the same expected reward regardless of output content. Under GRPO, the model converges to the simplest output that satisfies the format constraint:
- 1 premise + 1 conclusion = 2 components
- Solver can trivially prove most such formalizations → prove_rate=100%
- ISR = n_necessary / n_components = 1/2 = 0.5

This is a textbook case of **reward hacking via output length minimization**. The model found that shorter outputs reduce variance in the reward signal (fewer components → fewer ways to fail the format check), leading to systematic collapse to minimal length.

## Implications for Paper

1. **plan013 ISR≈0.5 cannot be cited as evidence of structural quality** — it reflects degenerate 2-component formalizations
2. **plan001 ISR=0.132 is the more meaningful baseline** — it operates on real multi-premise formalizations (mean 7 components)
3. **Component count should be reported alongside ISR** in all comparisons to prevent this confound
4. **Normalized ISR** (controlling for component count) may be needed for fair cross-experiment comparison
