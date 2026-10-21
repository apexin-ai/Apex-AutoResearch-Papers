# κ Threshold Sweep Analysis

## Setup

- K=2, N=5000, n_expert=200
- π_s = [0.05, 0.15] (symmetric CM)
- τ(Z=0)=0.5, τ(Z=1)=1.0
- T ~ Bernoulli(0.5)
- κ values: [10, 25, 50, 100, 200, 500, 1000]
- MC runs: 50 seeds (0–49)

## Summary Table

| κ | Guard Rate | RMSE HB | RMSE Global | RMSE Ratio | Instability % | Mean Max κ(M) | Median Max κ(M) |
|---:|----------:|--------:|------------:|-----------:|--------------:|--------------:|----------------:|
| 10 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
| 25 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
| 50 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
| 100 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
| 200 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
| 500 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |
| 1000 | 0.000 ± 0.000 | 0.0759 ± 0.0043 | 0.0765 ± 0.0042 | 1.0477 ± 0.0483 | 0.0 | 1.4 | 1.4 |

## Analysis

### Key Finding: Guard Never Triggers

Across all 350 runs (7 κ values × 50 seeds), the condition number guard **never triggered**. The maximum observed condition number is **1.89**, far below the smallest sweep value κ=10.

This means all κ values produce **identical** RMSE results. The per-subgroup HB correction is always applied without fallback.

**Interpretation**: With n_expert=200 and moderate misclassification (π_s = [0.05, 0.15]), the confusion matrix is well-estimated and the mixing matrix is well-conditioned. The κ guard is a safety net for edge cases, not an active component under these conditions.

### Condition Number Distribution

| Statistic | Value |
|-----------|------:|
| Mean | 1.446 |
| Median | 1.447 |
| P90 | 1.598 |
| P95 | 1.655 |
| P99 | 1.893 |
| Max | 1.893 |

### Numerical Stability

No numerical instability (NaN/Inf) observed at any κ value.

## Stress Test: When Does the Guard Matter?

To contextualize the sweep, we probe condition numbers under more challenging settings (20 seeds each):

| Configuration | Mean Max κ(M) | P95 Max κ(M) | Max κ(M) | Triggers κ=100? |
|---------------|-------------:|-----------:|--------:|:---------------|
| moderate/n200/K2 | 1.4 | 1.7 | 1.8 | No |
| moderate/n50/K2 | 1.7 | 2.7 | 2.7 | No |
| extreme/n200/K2 | 2.3 | 2.9 | 5.7 | No |
| extreme/n50/K2 | 2.6 | 4.4 | 4.4 | No |
| extreme/n50/K4 | 5.6 | 15.6 | 15.9 | No |
| near_random/n50/K2 | 181.7 | 1015.8 | 1125.3 | Yes |

The guard becomes relevant when n_expert is small (≤50) and/or misclassification rates approach 0.5. Under the specified moderate regime, κ never approaches the threshold.

## Is κ=100 Reasonable?

**Yes.** κ=100 is a safe default for this regime:
- The empirical max condition number (1.89) is ~53× below the threshold, providing a large safety margin.
- The guard activates only under adversarial conditions (near-random labeling, tiny expert budgets) where correction would amplify noise regardless.
- A threshold much lower than 100 (e.g., κ=10) would still never trigger here, so the exact value is not critical for well-conditioned problems.

## Adaptive Formula Suggestion

A data-driven approach: set κ = c · √(n_expert / K), where c is calibrated per regime.
- With n_expert=200, K=2: √(200/2) = 10.0
- Setting c=10 gives κ=100, which is close to 100
- However, the optimal κ depends on the misclassification severity, not just sample size
- A more robust adaptive rule: set κ to 2× the observed P99 of condition numbers from a pilot run. Here that would be κ = 2 × 1.9 = 3.8
- **Bottom line**: κ=100 provides ample headroom. The exact value matters only in edge cases where n_expert/K is very small.
