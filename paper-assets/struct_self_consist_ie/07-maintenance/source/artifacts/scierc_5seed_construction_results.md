# SciERC 5-Seed Entity Construction Results

**Dataset**: SciERC, N=8 samples/instance, θ=2/N=0.25
**Date**: 2026-05-24
**Instances per seed**: 529 (filtered: gold entities non-empty)

## Per-Seed Results

| Seed | N | Greedy F1 | MV Constr F1 | MV Δpp | LP Constr F1 | LP Δpp | LP p |
|------|---|-----------|--------------|--------|--------------|--------|------|
| 42   | 529 | 65.02 | 65.28 | +0.26 | 64.44 | -0.58 | 0.8242 |
| 123  | 529 | 64.71 | 64.78 | +0.06 | 65.67 | +0.96 | 0.0853 |
| 456  | 529 | 64.56 | 65.38 | +0.81 | 66.47 | +1.91 | 0.0031* |
| 2024 | 529 | 64.78 | 65.96 | +1.18 | 66.25 | +1.48 | 0.0233* |
| 3141 | 529 | 64.27 | 66.14 | +1.87 | 66.05 | +1.78 | 0.0075* |

## Aggregate (5-seed mean±σ)

| Method | F1 (%) | Δ vs Greedy (pp) |
|--------|--------|------------------|
| Greedy | 64.67 ± 0.25 | — |
| MV Construction | 65.51 ± 0.49 | +0.84 ± 0.65 |
| LP Construction | 65.78 ± 0.72 | +1.11 ± 0.91 |

## Pooled Bootstrap Significance (B=10,000)

| Comparison | Δ (pp) | 95% CI | p-value | Significant |
|------------|--------|--------|---------|-------------|
| MV vs Greedy | +0.84 | [+0.17, +1.52] | 0.0074 | Yes |
| LP vs Greedy | +1.11 | [+0.48, +1.75] | 0.0003 | Yes |
| LP vs MV | +0.27 | [-0.04, +0.57] | 0.0431 | Yes (marginal) |

## Key Takeaways

1. **Both construction methods significantly outperform greedy** (pooled p < 0.01).
2. **LP construction provides the largest gain** (+1.11pp mean, p=0.0003), outperforming MV (+0.84pp).
3. **LP vs MV difference is marginally significant** (p=0.0431), suggesting LP weighting adds value beyond uniform voting.
4. **Stability**: MV improves in 5/5 seeds; LP improves in 4/5 seeds (seed 42 is the exception at -0.58pp).
5. **Per-seed significance**: LP reaches p<0.05 in 3/5 seeds individually; seed 42 is the only negative outlier.
