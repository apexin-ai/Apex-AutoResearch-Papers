# FewNERD 3-epoch Entity Construction Results (2-seed)

## Setup
- Model: 3-epoch finetuned (mf4v2)
- Seeds: 42, 456
- N_samples/instance: 8, θ=2/N=0.25
- Instances per seed: 32,565 (gold entities non-empty)

## Per-seed Results

| Seed | Greedy F1 | MV Constr F1 | MV Δ (pp) | MV p | LP Constr F1 | LP Δ (pp) | LP p |
|------|-----------|-------------|-----------|------|-------------|-----------|------|
| 42   | 74.79     | 74.12       | -0.66     | 1.00 | 74.75       | -0.04     | 0.64 |
| 456  | 74.86     | 75.46       | +0.60     | 0.00 | 76.38       | +1.52     | 0.00 |

## Aggregate (2-seed mean±σ)

| Method | Δ mean | Δ σ |
|--------|--------|-----|
| MV     | -0.03  | 0.63 |
| LP     | +0.74  | 0.78 |

## Pooled Bootstrap (B=10,000)

| Method | Δ (pp) | 95% CI | p-value | Sig? |
|--------|--------|--------|---------|------|
| MV     | -0.03  | [-0.19, +0.13] | 0.6386 | NO |
| LP     | +0.74  | [+0.60, +0.89] | 0.0000 | YES |

## vs Paper Claim
- Paper reports: **+1.40pp** (4-seed, p<0.001) for LP construction on FewNERD
- 2-seed result: **+0.74pp** (pooled p<0.001)
- Direction consistent, magnitude lower (2 seeds vs 4, high seed variance: seed42 shows -0.04pp while seed456 shows +1.52pp)
- MV construction ineffective on FewNERD (not significant)
- LP weighting is critical for FewNERD entity construction

## Rebuttal-ready Summary Line
FewNERD (3-epoch, 2-seed): LP construction **+0.74pp** (p<0.001), MV construction -0.03pp (n.s.)
