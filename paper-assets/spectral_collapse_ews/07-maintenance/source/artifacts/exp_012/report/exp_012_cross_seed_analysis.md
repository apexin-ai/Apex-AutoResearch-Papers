# exp_012 Cross-Seed Analysis: r=0.3 (seed42 vs seed43)

## 1. exp_012 (seed43) Per-Generation Metrics

| Gen | eff_rank | SLV (log_det) | ppl | d4 | train_loss |
|-----|----------|---------------|-------|--------|------------|
| 0 | 417.55 | 2366.68 | 9.554 | 0.7415 | — |
| 1 | 476.75 | 2363.89 | 10.192 | 0.6676 | 1.837 |
| 2 | 483.02 | 2363.64 | 10.578 | 0.5348 | 1.765 |
| 3 | 489.31 | 2389.87 | 10.915 | 0.5225 | 1.544 |
| 4 | 494.15 | 2408.14 | 11.246 | 0.5097 | 1.461 |
| 5 | 498.80 | 2431.29 | 11.548 | 0.5046 | 1.441 |
| 6 | 502.00 | 2445.24 | 11.876 | 0.4527 | 1.435 |
| 7 | 505.90 | 2462.25 | 12.184 | 0.3219 | 1.328 |
| 8 | 510.97 | 2474.35 | 12.567 | 0.2315 | 1.169 |
| 9 | 516.45 | 2493.43 | 12.959 | 0.1833 | 1.087 |
| 10 | 521.19 | 2508.33 | 13.306 | 0.1217 | 1.032 |

**SLV monotonicity**: Not strictly monotonic — dips at gen1 (−2.79) and gen2 (−0.25), then monotonically increases gen2→gen10. Same qualitative pattern as seed42 (which dipped at gen1 only).

**SLV total change**: +5.98% ((2508.33 − 2366.68) / 2366.68)

## 2. Cross-Seed Comparison (seed42 vs seed43, mean ± std)

Sample std for n=2: |x₁ − x₂| / √2

### SLV (log_det)

| Gen | seed42 | seed43 | Mean | Std | Diff % |
|-----|--------|--------|------|-----|--------|
| 0 | 2366.68 | 2366.68 | 2366.68 | 0.00 | 0.000 |
| 1 | 2366.13 | 2363.89 | 2365.01 | 1.58 | 0.095 |
| 2 | 2372.45 | 2363.64 | 2368.05 | 6.23 | 0.372 |
| 3 | 2386.72 | 2389.87 | 2388.30 | 2.23 | 0.132 |
| 4 | 2404.02 | 2408.14 | 2406.08 | 2.92 | 0.171 |
| 5 | 2431.17 | 2431.29 | 2431.23 | 0.09 | 0.005 |
| 6 | 2452.00 | 2445.24 | 2448.62 | 4.78 | 0.276 |
| 7 | 2467.05 | 2462.25 | 2464.65 | 3.40 | 0.195 |
| 8 | 2485.91 | 2474.35 | 2480.13 | 8.17 | 0.466 |
| 9 | 2497.30 | 2493.43 | 2495.36 | 2.74 | 0.155 |
| 10 | 2511.13 | 2508.33 | 2509.73 | 1.98 | 0.112 |

**Max SLV divergence**: 0.47% at gen8. SLV trajectories are highly consistent across seeds.

### eff_rank

| Gen | seed42 | seed43 | Mean | Std |
|-----|--------|--------|------|-----|
| 0 | 417.55 | 417.55 | 417.55 | 0.00 |
| 1 | 476.91 | 476.75 | 476.83 | 0.12 |
| 2 | 484.17 | 483.02 | 483.60 | 0.81 |
| 3 | 489.48 | 489.31 | 489.39 | 0.12 |
| 4 | 492.59 | 494.15 | 493.37 | 1.10 |
| 5 | 497.86 | 498.80 | 498.33 | 0.67 |
| 6 | 501.63 | 502.00 | 501.82 | 0.26 |
| 7 | 506.30 | 505.90 | 506.10 | 0.28 |
| 8 | 511.71 | 510.97 | 511.34 | 0.53 |
| 9 | 515.92 | 516.45 | 516.18 | 0.37 |
| 10 | 521.26 | 521.19 | 521.23 | 0.05 |

### ppl (perplexity)

| Gen | seed42 | seed43 | Mean | Std |
|-----|--------|--------|------|-----|
| 0 | 9.554 | 9.554 | 9.554 | 0.000 |
| 1 | 10.193 | 10.192 | 10.193 | 0.001 |
| 2 | 10.589 | 10.578 | 10.584 | 0.008 |
| 3 | 10.901 | 10.915 | 10.908 | 0.010 |
| 4 | 11.226 | 11.246 | 11.236 | 0.014 |
| 5 | 11.544 | 11.548 | 11.546 | 0.003 |
| 6 | 11.875 | 11.876 | 11.876 | 0.001 |
| 7 | 12.215 | 12.184 | 12.200 | 0.022 |
| 8 | 12.610 | 12.567 | 12.589 | 0.030 |
| 9 | 12.955 | 12.959 | 12.957 | 0.003 |
| 10 | 13.377 | 13.306 | 13.342 | 0.050 |

### d4 (distinct-4)

| Gen | seed42 | seed43 | Mean | Std |
|-----|--------|--------|------|-----|
| 0 | 0.7414 | 0.7415 | 0.7415 | 0.0001 |
| 1 | 0.6894 | 0.6676 | 0.6785 | 0.0154 |
| 2 | 0.4892 | 0.5348 | 0.5120 | 0.0322 |
| 3 | 0.4646 | 0.5225 | 0.4936 | 0.0409 |
| 4 | 0.4682 | 0.5097 | 0.4890 | 0.0293 |
| 5 | 0.4508 | 0.5046 | 0.4777 | 0.0380 |
| 6 | 0.4176 | 0.4527 | 0.4352 | 0.0248 |
| 7 | 0.3964 | 0.3219 | 0.3592 | 0.0527 |
| 8 | 0.4058 | 0.2315 | 0.3187 | 0.1232 |
| 9 | 0.3732 | 0.1833 | 0.2783 | 0.1343 |
| 10 | 0.3422 | 0.1217 | 0.2320 | 0.1559 |

**Note**: d4 shows substantial cross-seed divergence in late generations (gen8–10 std > 0.12). Seed43 collapses to 0.12 while seed42 remains at 0.34. Both decrease monotonically but at different rates.

## 3. Trajectory Consistency

| Metric | seed42 trajectory | seed43 trajectory | Consistent? |
|--------|------------------|------------------|-------------|
| SLV | Dip at gen1, then monotonic ↑ | Dip at gen1–2, then monotonic ↑ | Yes (qualitatively) |
| eff_rank | Monotonic ↑ | Monotonic ↑ | Yes |
| ppl | Monotonic ↑ | Monotonic ↑ | Yes |
| d4 | Monotonic ↓ | Monotonic ↓ | Direction yes, magnitude diverges |

**SLV total change**: seed42 = +6.10%, seed43 = +5.98%. Mean = **+6.04% ± 0.08%**.

## 4. Conclusions

### Type III verification
**Confirmed.** seed43 reproduces the Type III pattern (progressive SLV increase under fixed r=0.3 mix). Both seeds show:
- SLV rising ~6% over 10 generations
- eff_rank monotonically increasing (417→521)
- ppl monotonically increasing (9.55→13.3)
- Initial SLV dip in gen1 (transient) before sustained increase

### Cross-seed robustness
- **SLV, eff_rank, ppl**: Extremely reproducible. Max cross-seed SLV divergence < 0.5%. eff_rank and ppl nearly identical across seeds.
- **d4**: High variance in late generations. seed43 diversity collapses faster (0.12 at gen10 vs 0.34 for seed42). This metric is more stochastic and sensitive to generation sampling.

### Impact on Table 3
The r=0.3 row can be upgraded to 2-seed mean ± std:

| Metric | Current (seed42 only) | Upgraded (2-seed) |
|--------|----------------------|-------------------|
| SLV (gen10) | 2511.1 | 2509.7 ± 2.0 |
| SLV Δ% | +6.1% | +6.0% ± 0.1% |
| eff_rank (gen10) | 521.3 | 521.2 ± 0.0 |
| ppl (gen10) | 13.38 | 13.34 ± 0.05 |
| d4 (gen10) | 0.342 | 0.232 ± 0.156 |

**Recommendation for d4 in Table 3**: The large d4 std (0.156) warrants a footnote or reporting individual seed values. SLV/eff_rank/ppl are safe to report as mean ± std with tight confidence.
