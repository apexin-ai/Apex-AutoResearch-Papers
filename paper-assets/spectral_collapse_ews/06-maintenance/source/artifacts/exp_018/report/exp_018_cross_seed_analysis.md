# Exp_018 Cross-Seed Analysis: r=0.5 Type III Trajectory Reproduction

## Experiment Setup

| Parameter | exp_004 (seed42) | exp_018 (seed43) |
|-----------|------------------|------------------|
| Model | EleutherAI/pythia-410m-deduped | EleutherAI/pythia-410m-deduped |
| Condition | fixed_mix | fixed_mix |
| real_ratio | 0.5 | 0.5 |
| Generations | 10 | 10 |
| Seed | 42 | 43 |

**Hypothesis**: r=0.5 with seed 43 reproduces Type III trajectory (monotonic expansion) observed in the r=0.5 seed42 run (exp_004).

## Per-Generation Metrics Comparison

### Effective Rank

| Gen | seed42 | seed43 | Mean | Std |
|-----|--------|--------|------|-----|
| 0 | 417.55 | 417.55 | 417.55 | 0.00 |
| 1 | 477.89 | 475.91 | 476.90 | 1.40 |
| 2 | 487.92 | 488.01 | 487.97 | 0.06 |
| 3 | 496.57 | 493.94 | 495.25 | 1.86 |
| 4 | 502.05 | 503.05 | 502.55 | 0.71 |
| 5 | 512.78 | 510.11 | 511.45 | 1.89 |
| 6 | 519.78 | 519.21 | 519.50 | 0.40 |
| 7 | 527.47 | 526.83 | 527.15 | 0.46 |
| 8 | 536.39 | 536.98 | 536.69 | 0.42 |
| 9 | 545.73 | 545.35 | 545.54 | 0.27 |
| 10 | 554.51 | 552.40 | 553.46 | 1.49 |

### Log-Determinant (SLV)

| Gen | seed42 | seed43 | Mean | Std |
|-----|--------|--------|------|-----|
| 0 | 2366.68 | 2366.68 | 2366.68 | 0.00 |
| 1 | 2366.58 | 2361.66 | 2364.12 | 3.48 |
| 2 | 2395.36 | 2393.57 | 2394.46 | 1.26 |
| 3 | 2425.64 | 2419.34 | 2422.49 | 4.45 |
| 4 | 2451.72 | 2454.90 | 2453.31 | 2.25 |
| 5 | 2486.34 | 2479.81 | 2483.08 | 4.62 |
| 6 | 2507.62 | 2507.73 | 2507.68 | 0.08 |
| 7 | 2525.55 | 2528.07 | 2526.81 | 1.78 |
| 8 | 2544.03 | 2548.02 | 2546.02 | 2.82 |
| 9 | 2562.13 | 2560.14 | 2561.13 | 1.40 |
| 10 | 2573.20 | 2570.09 | 2571.65 | 2.20 |

Note: Both seeds show a minor SLV dip at gen1 (seed42: -0.11, seed43: -5.02), then monotonic increase from gen2 onward. This is a first-generation transient effect, not a structural dip.

### Perplexity

| Gen | seed42 | seed43 | Mean | Std |
|-----|--------|--------|------|-----|
| 0 | 9.55 | 9.55 | 9.55 | 0.00 |
| 1 | 10.08 | 10.08 | 10.08 | 0.01 |
| 2 | 10.41 | 10.41 | 10.41 | 0.00 |
| 3 | 10.76 | 10.73 | 10.74 | 0.02 |
| 4 | 11.14 | 11.12 | 11.13 | 0.01 |
| 5 | 11.65 | 11.60 | 11.63 | 0.04 |
| 6 | 12.16 | 12.12 | 12.14 | 0.03 |
| 7 | 12.77 | 12.69 | 12.73 | 0.06 |
| 8 | 13.46 | 13.46 | 13.46 | 0.00 |
| 9 | 14.23 | 14.21 | 14.22 | 0.01 |
| 10 | 15.20 | 15.03 | 15.11 | 0.12 |

### Distinct-4

| Gen | seed42 | seed43 | Mean | Std |
|-----|--------|--------|------|-----|
| 0 | 0.7414 | 0.7415 | 0.7415 | 0.0001 |
| 1 | 0.6693 | 0.6705 | 0.6699 | 0.0009 |
| 2 | 0.5817 | 0.5708 | 0.5763 | 0.0077 |
| 3 | 0.4563 | 0.5438 | 0.5000 | 0.0619 |
| 4 | 0.3280 | 0.4632 | 0.3956 | 0.0956 |
| 5 | 0.2354 | 0.4189 | 0.3271 | 0.1298 |
| 6 | 0.2203 | 0.4110 | 0.3156 | 0.1349 |
| 7 | 0.1932 | 0.3614 | 0.2773 | 0.1189 |
| 8 | 0.1681 | 0.2987 | 0.2334 | 0.0924 |
| 9 | 0.1019 | 0.2309 | 0.1664 | 0.0912 |
| 10 | 0.0954 | 0.2088 | 0.1521 | 0.0802 |

## Trend Summary (gen0 → gen10)

| Metric | seed42 | seed43 | 2-seed Mean |
|--------|--------|--------|-------------|
| Eff. Rank | 417.55 → 554.51 (+32.8%) | 417.55 → 552.40 (+32.3%) | 417.55 → 553.46 (+32.5%) |
| SLV | 2366.68 → 2573.20 (+8.7%) | 2366.68 → 2570.09 (+8.6%) | 2366.68 → 2571.65 (+8.7%) |
| PPL | 9.55 → 15.20 (+59.1%) | 9.55 → 15.03 (+57.4%) | 9.55 → 15.11 (+58.2%) |
| D-4 | 0.7414 → 0.0954 (-87.1%) | 0.7415 → 0.2088 (-71.8%) | 0.7415 → 0.1521 (-79.5%) |

## Cross-Seed Reproducibility

| Metric | Reproducibility | Notes |
|--------|----------------|-------|
| Eff. Rank | Excellent | Max gen-wise std = 1.89; <0.4% relative |
| SLV (log_det) | Excellent | Max gen-wise std = 4.62; <0.2% relative |
| PPL | Excellent | Max gen-wise std = 0.12; <0.8% relative |
| D-4 | Moderate | Max gen-wise std = 0.1349; seed43 retains 2× higher D-4 than seed42 at gen10 |

D-4 is the least reproducible metric: seed43 maintains substantially higher lexical diversity throughout. This suggests generation-level sampling stochasticity has a larger impact on surface-level diversity than on spectral structure.

## Trajectory Classification

Both seeds exhibit **Type III trajectory (monotonic expansion)**:
- Eff. Rank: monotonic increase across all 11 generations in both seeds
- SLV: minor transient dip at gen1 (first fine-tuning), then monotonic increase from gen2–gen10
- No spectral collapse observed at r=0.5

## Conclusion

**SUCCESS** — exp_018 (seed43) reproduces the Type III trajectory observed in exp_004 (seed42).

The r=0.5 fixed-mix condition robustly prevents spectral collapse across seeds:
- Spectral metrics (eff_rank, SLV) are highly reproducible (relative std <0.4%)
- Quality degradation (PPL +58%) is consistent but does not trigger spectral narrowing
- D-4 decline rate is seed-dependent (71.8% vs 87.1%), suggesting surface diversity is more stochastic than spectral structure

The 2-seed mean±std values are ready for Table 3 update.
