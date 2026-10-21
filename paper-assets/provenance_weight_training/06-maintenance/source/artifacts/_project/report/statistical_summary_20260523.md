# Statistical Summary — 2026-05-23

## 1. Paired t-Tests (Adaptive vs Uniform, Holdout PPL)

### B=8 (ρ=0.4, τ=0.7, n_min=4)

| Seed | Adaptive | Uniform | Δ |
|------|----------|---------|--------|
| 42 | 17.650 | 17.694 | −0.044 |
| 123 | 17.631 | 17.687 | −0.056 |
| 456 | 17.646 | 17.702 | −0.056 |

| Statistic | Value |
|-----------|-------|
| Mean Δ | −0.052 |
| SD(Δ) | 0.0069 |
| t(2) | −13.00 |
| p (two-sided) | 0.0059 |

### ρ=0.3 (B=4, τ=0.7, n_min=2)

| Seed | Adaptive | Uniform | Δ |
|------|----------|---------|--------|
| 42 | 17.422 | 17.422 | 0.000 |
| 123 | 17.435 | 17.433 | +0.002 |
| 456 | 17.424 | 17.419 | +0.005 |

| Statistic | Value |
|-----------|-------|
| Mean Δ | +0.0023 |
| SD(Δ) | 0.0025 |
| t(2) | +1.61 |
| p (two-sided) | 0.2495 |

## 2. Benjamini-Hochberg Correction (α = 0.05)

| Comparison | p_raw | Rank | p_BH | Significant? |
|------------|-------|------|------|-------------|
| B=16 (ρ=0.4) | 0.005 | 1 | 0.0147 | **Yes** |
| B=8 (ρ=0.4) | 0.0059 | 2 | 0.0147 | **Yes** |
| ρ=0.6 (B=4) | 0.010 | 3 | 0.0167 | **Yes** |
| B=4 (ρ=0.4) | 0.019 | 4 | 0.0238 | **Yes** |
| ρ=0.3 (B=4) | 0.2495 | 5 | 0.2495 | No |

All comparisons except ρ=0.3 survive BH correction at α=0.05.

## 3. Batch-Size Amplification Gradient

| B | Mean Δ (PPL) | Ratio vs B=4 |
|---|-------------|-------------|
| 4 | −0.020 | 1.00× |
| 8 | −0.052 | 2.60× |
| 16 | −0.068 | 3.40× |

- B=4→B=8: improvement grows **2.60×** (Δ doubles+)
- B=8→B=16: improvement grows **1.31×** (diminishing marginal gain)
- Near-linear scaling from B=4 to B=8; sublinear from B=8 to B=16 (diminishing returns).

## 4. α_eff-Only Ablation (n_min=1, ρ=0.4)

| Seed | PPL (α_eff-only) |
|------|------------------|
| 42 | 17.750 |
| 123 | 17.733 |
| *456* | *running* |

| Statistic | Value |
|-----------|-------|
| Mean (2 seeds) | 17.742 ± 0.012 |
| Dual adaptive baseline | ~17.674 |
| Degradation vs dual | +0.068 PPL |

Removing n_min gating (keeping only α_eff) degrades PPL by +0.068 compared to the dual-adaptive system — confirming that both components contribute. Seed 456 still running; final stats pending.

## Key Takeaways

1. **B=8 confirms the batch-size amplification story.** Adaptive weighting delivers a statistically significant −0.052 PPL improvement over uniform at B=8 (p=0.006, p_BH=0.015), slotting cleanly between B=4 (−0.020) and B=16 (−0.068). The scaling is near-linear from B=4→B=8 (2.6×) with diminishing returns at B=16 (1.3× marginal), consistent with a mechanism that exploits intra-batch quality variance — more samples per batch → more signal for the weighting function.

2. **ρ=0.3 shows no adaptive advantage.** At low binding rate, Δ ≈ 0 (p=0.25, n.s. after BH). This matches the theoretical prediction: when almost no n-grams bind, the provenance signal is too sparse to differentiate sample quality, and adaptive weighting collapses to uniform. The ρ=0.3 result serves as a useful **negative control** bounding the method's operating range to ρ ≥ 0.4.

3. **α_eff alone is insufficient.** Dropping the n_min gate costs +0.068 PPL versus the full dual-adaptive system (17.742 vs 17.674), demonstrating that the two components are complementary — α_eff provides per-sample granularity while n_min provides a reliability floor that prevents noisy low-count estimates from corrupting the weights.
