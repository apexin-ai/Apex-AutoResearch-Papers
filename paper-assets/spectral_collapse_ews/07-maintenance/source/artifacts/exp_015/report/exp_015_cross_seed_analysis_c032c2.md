# exp_015 Cross-Seed Analysis: r=0.25 (Seeds 42/43/44)

## 1. Experiment Overview

| Property | Value |
|----------|-------|
| Config | phase1_fixed_mix, r=0.25 |
| Seeds | 42 (exp_009), 43 (exp_014/014b), 44 (exp_015) |
| Generations | 0–10 |
| Checkpoint (seed44) | `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/fixed_mix_r025_seed44/` |
| Log (seed44) | `~/runs/spectral_collapse_ews/exp_015.log` |

## 2. Per-Generation Metrics

### Seed 42 (exp_009)

| Gen | eff_rank | log_det (SLV) | ppl | distinct4 | sigma1 | train_loss |
|-----|----------|---------------|-------|-----------|---------|------------|
| 0 | 417.55 | 2366.68 | 9.554 | 0.7414 | 1942.82 | — |
| 1 | 476.66 | 2362.13 | 10.239 | 0.6499 | 946.35 | 1.801 |
| 2 | 482.84 | 2363.10 | 10.653 | 0.4973 | 868.76 | 1.698 |
| 3 | 489.47 | 2380.88 | 11.019 | 0.4419 | 807.37 | 1.413 |
| 4 | 491.21 | 2393.37 | 11.343 | 0.4298 | 780.54 | 1.343 |
| 5 | 495.84 | 2421.22 | 11.669 | 0.4192 | 759.85 | 1.308 |
| 6 | 498.59 | 2436.38 | 11.974 | 0.3969 | 747.85 | 1.317 |
| 7 | 500.66 | 2447.08 | 12.295 | 0.3889 | 741.85 | 1.303 |
| 8 | 505.82 | 2463.81 | 12.631 | 0.3657 | 716.07 | 1.304 |
| 9 | 509.59 | 2476.58 | 12.978 | 0.3674 | 709.26 | 1.289 |
| 10 | 512.46 | 2485.01 | 13.285 | 0.3572 | 702.94 | 1.319 |

### Seed 43 (exp_014/014b)

| Gen | eff_rank | log_det (SLV) | ppl | distinct4 | sigma1 | train_loss |
|-----|----------|---------------|-------|-----------|---------|------------|
| 0 | 417.55 | 2366.68 | 9.554 | 0.7415 | 1942.82 | — |
| 1 | 475.66 | 2365.35 | 10.226 | 0.6584 | 963.01 | 1.802 |
| 2 | 483.00 | 2362.54 | 10.649 | 0.5574 | 864.90 | 1.722 |
| 3 | 488.96 | 2380.55 | 11.003 | 0.4772 | 827.00 | 1.521 |
| 4 | 491.74 | 2395.05 | 11.346 | 0.3735 | 795.62 | 1.363 |
| 5 | 495.60 | 2414.84 | 11.668 | 0.3378 | 767.08 | 1.200 |
| 6 | 497.83 | 2426.55 | 12.005 | 0.3374 | 782.76 | 1.053 |
| 7 | 502.04 | 2448.42 | 12.406 | 0.3700 | 777.69 | 1.060 |
| 8 | 506.76 | 2465.02 | 12.767 | 0.3586 | 780.81 | 1.093 |
| 9 | 510.49 | 2477.84 | 13.184 | 0.3848 | 775.38 | 1.073 |
| 10 | 515.56 | 2488.58 | 13.611 | 0.3380 | 758.92 | 1.061 |

### Seed 44 (exp_015)

| Gen | eff_rank | log_det (SLV) | ppl | distinct4 | sigma1 | train_loss |
|-----|----------|---------------|-------|-----------|---------|------------|
| 0 | 417.55 | 2366.68 | 9.554 | 0.7305 | 1942.82 | — |
| 1 | 475.92 | 2366.13 | 10.221 | 0.6379 | 962.97 | 1.800 |
| 2 | 484.39 | 2364.59 | 10.641 | 0.5156 | 853.62 | 1.689 |
| 3 | 488.62 | 2378.05 | 11.002 | 0.4518 | 803.67 | 1.473 |
| 4 | 493.01 | 2402.71 | 11.333 | 0.4156 | 770.46 | 1.388 |
| 5 | 494.32 | 2415.91 | 11.641 | 0.4008 | 753.50 | 1.319 |
| 6 | 498.74 | 2437.92 | 11.973 | 0.3994 | 738.96 | 1.294 |
| 7 | 502.71 | 2456.77 | 12.300 | 0.3865 | 728.24 | 1.265 |
| 8 | 504.20 | 2463.28 | 12.614 | 0.3703 | 731.77 | 1.239 |
| 9 | 510.29 | 2482.46 | 13.005 | 0.3621 | 698.85 | 1.212 |
| 10 | 513.44 | 2490.74 | 13.330 | 0.3315 | 690.91 | 1.172 |

## 3. Cross-Seed Comparison (3-Seed Mean ± Std)

| Gen | eff_rank | log_det (SLV) | ppl | distinct4 | sigma1 |
|-----|----------|---------------|-------|-----------|--------|
| 0 | 417.55 ± 0.00 | 2366.68 ± 0.00 | 9.554 ± 0.000 | 0.7378 ± 0.006 | 1942.82 ± 0.00 |
| 1 | 476.08 ± 0.51 | 2364.54 ± 2.12 | 10.229 ± 0.009 | 0.6487 ± 0.010 | 957.44 ± 9.56 |
| 2 | 483.41 ± 0.81 | 2363.41 ± 1.03 | 10.648 ± 0.006 | 0.5234 ± 0.030 | 862.43 ± 7.82 |
| 3 | 489.02 ± 0.43 | 2379.83 ± 1.55 | 11.008 ± 0.010 | 0.4570 ± 0.018 | 812.68 ± 12.56 |
| 4 | 491.99 ± 0.93 | 2397.04 ± 4.97 | 11.341 ± 0.007 | 0.4063 ± 0.029 | 782.21 ± 12.59 |
| 5 | 495.26 ± 0.80 | 2417.32 ± 3.47 | 11.659 ± 0.016 | 0.3859 ± 0.043 | 760.14 ± 6.81 |
| 6 | 498.39 ± 0.46 | 2433.62 ± 6.06 | 11.984 ± 0.018 | 0.3779 ± 0.035 | 756.52 ± 23.07 |
| 7 | 501.80 ± 0.34 | 2450.76 ± 5.17 | 12.334 ± 0.057 | 0.3818 ± 0.009 | 749.26 ± 25.64 |
| 8 | 505.59 ± 1.28 | 2464.04 ± 0.92 | 12.671 ± 0.080 | 0.3649 ± 0.006 | 742.88 ± 34.32 |
| 9 | 510.12 ± 0.47 | 2478.96 ± 3.08 | 13.056 ± 0.105 | 0.3714 ± 0.013 | 727.83 ± 40.63 |
| 10 | **513.82 ± 1.59** | **2488.11 ± 2.89** | **13.409 ± 0.18** | **0.3422 ± 0.013** | **717.59 ± 36.31** |

## 4. SLV (log_det) Trajectory Analysis

### 4a. Type II Trajectory: Dip-then-Recovery

All three seeds exhibit the **Type II trajectory** — an initial SLV dip in Gen 1–2 followed by monotonic recovery:

| Seed | Dip Location | Dip Depth (from Gen0) | Recovery Gen |
|------|-------------|----------------------|-------------|
| 42 | Gen 1 | −4.55 (2366.68 → 2362.13) | Gen 3 (2380.88) |
| 43 | Gen 2 | −4.14 (2366.68 → 2362.54) | Gen 3 (2380.55) |
| 44 | Gen 2 | −2.09 (2366.68 → 2364.59) | Gen 3 (2378.05) |

**Mean dip depth: −3.59 ± 1.30**

The dip is shallow (< 0.2% of baseline SLV) and recovery is swift (always by Gen 3).

### 4b. SLV Total Change (Gen 0 → Gen 10)

| Seed | Gen0 SLV | Gen10 SLV | Δ | Δ% |
|------|----------|-----------|--------|------|
| 42 | 2366.68 | 2485.01 | +118.33 | +5.00% |
| 43 | 2366.68 | 2488.58 | +121.90 | +5.15% |
| 44 | 2366.68 | 2490.74 | +124.06 | +5.24% |
| **Mean** | 2366.68 | **2488.11** | **+121.43** | **+5.13%** |

### 4c. Non-Decreasing Condition

SLV is monotonically non-decreasing from:
- **Seed 42**: Gen 1 onwards (only Gen0→Gen1 decreases)
- **Seed 43**: Gen 2 onwards (Gen0→Gen1 and Gen1→Gen2 decrease)
- **Seed 44**: Gen 2 onwards (Gen0→Gen1 and Gen1→Gen2 decrease)

All seeds achieve monotonic non-decreasing SLV by **Gen 2 at latest**, confirming robust recovery after the initial dip.

## 5. Gen 10 Final Summary (3-Seed)

| Metric | Seed 42 | Seed 43 | Seed 44 | Mean ± Std |
|--------|---------|---------|---------|------------|
| eff_rank | 512.46 | 515.56 | 513.44 | **513.82 ± 1.59** |
| log_det (SLV) | 2485.01 | 2488.58 | 2490.74 | **2488.11 ± 2.89** |
| ppl | 13.285 | 13.611 | 13.330 | **13.409 ± 0.18** |
| distinct4 | 0.3572 | 0.3380 | 0.3315 | **0.3422 ± 0.013** |
| sigma1 | 702.94 | 758.92 | 690.91 | **717.59 ± 36.31** |

## 6. Conclusions

1. **Type II trajectory robustly reproduced** across all 3 seeds. The characteristic SLV dip (Gen 1–2) followed by monotonic recovery (Gen 3+) is consistent.

2. **Low cross-seed variance**: Gen10 SLV CV = 0.12%, Gen10 PPL CV = 1.3%, Gen10 eff_rank CV = 0.31%. The r=0.25 fixed-mix setting yields highly reproducible collapse dynamics.

3. **sigma1 shows higher variance** (CV = 5.1% at Gen10), driven by seed43 retaining a higher leading singular value (758.92 vs 690–703 for seeds 42/44). This does not affect SLV or eff_rank convergence.

4. **Distinct-4 decline is consistent**: all seeds converge to ~0.33–0.36 by Gen10, confirming diversity loss accompanies spectral broadening.

5. **Data complete**: all 3 seeds have full Gen 0–10 metrics, enabling robust 3-seed statistics for the paper.
