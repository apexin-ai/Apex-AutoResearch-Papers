# Experiment Data Tables

## Table 1: Grid Curve (ρ=0.4, Claim 2)

Baseline: **Adaptive mean = 17.651 ± 0.007**

| b | seed42 | seed123 | seed456 | mean ± std | n |
|---|--------|---------|---------|------------|---|
| 0.1 | 17.657 | 17.646 | 17.663 | 17.655 ± 0.009 | 3 |
| 0.2 | 17.640 | *pending* | *pending* | 17.640 (1 seed) | 1 |
| 0.3 | 17.640 | 17.579 | 17.640 | 17.620 ± 0.035 | 3 |
| 0.5 | *missing* | 17.638 | 17.650 | 17.644 ± 0.008 | 2 |
| 1.0 | *missing* | 17.674 | 17.680 | 17.677 ± 0.004 | 2 |
| 1.5 | *missing* | 17.701 | 17.710 | 17.706 ± 0.006 | 2 |
| 2.0 | *missing* | 17.725 | 17.989 | 17.857 ± 0.187 | 2 |
| 3.0 | *missing* | 17.760 | 17.921 | 17.841 ± 0.114 | 2 |
| 5.0 | *missing* | 17.804 | 17.993 | 17.899 ± 0.134 | 2 |

**Notes:**
- b=0.2 seed123/seed456: RUNNING (resume in progress)
- b=0.3: seed123 uses grid_b0_3_seed123_r2 (17.579), seed456 uses grid_b0_3_seed456_r2 (17.640). Original runs had no metrics.
- b ≥ 0.5 seed42: Not in registry. Only seed123/seed456 registered (named grid_b1_0_*, grid_b1_5_*, grid_b2_0_*, grid_b3_0_*, grid_b5_0_*). Batch experiment grid_b_seed42_batch (DONE) has no individual metrics.

---

## Table 2: ρ=0.6 Ablation (Claim 1, cross-ρ validation)

| Method | seed42 | seed123 | seed456 | mean ± std | n |
|--------|--------|---------|---------|------------|---|
| Adaptive | 17.740 | 17.732 | *pending* | 17.736 ± 0.006 | 2 |
| Uniform | 17.766 | 17.754 | 17.769 | 17.763 ± 0.008 | 3 |
| ESS-only | 17.770 | — | — | 17.770 (1 seed) | 1 |
| Random | *pending* | — | — | — | 0 |
| Grid b=0.3 | *pending* | — | — | — | 0 |
| Grid b=0.5 | no metrics | — | — | — | 0 |

**Additional tau-sweep experiments (single seed42):**

| Experiment | eval_ppl_holdout |
|------------|-----------------|
| contamination_60_tau06_seed42 | 17.736 |
| contamination_60_tau07_seed42 | 17.730 |

**Notes:**
- Adaptive seed456 (contamination_60_adaptive_seed456): RUNNING
- Random seed42 (contamination_60_random_seed42): RUNNING (resume)
- Grid b=0.3 seed42 (contamination_60_grid_b0_3_seed42): RUNNING (resume)
- Grid b=0.5 seed42 (contamination_60_grid_b0_5_seed42): DONE but no metrics recorded
- Adaptive seed42 uses contamination_60_seed42_r2 (retry version)

---

## Key Observations

### Table 1: Grid U-curve (ρ=0.4)

1. **U-shaped curve confirmed**: Best grid PPL at b=0.3 (17.620), degrading toward both extremes (b=0.1: 17.655, b=5.0: 17.899).
2. **Grid-best vs Adaptive gap**: b=0.3 mean (17.620) beats adaptive (17.651) by 0.031, but driven by one outlier seed (17.579). Two of three seeds at b=0.3 are 17.640, close to adaptive.
3. **High variance at large b**: b ≥ 2.0 shows std > 0.1 (even with only 2 seeds), indicating grid becomes unstable when over-penalizing high-provenance data.
4. **Data gaps**: seed42 missing for all b ≥ 0.5 is the biggest hole. b=0.2 has only 1 seed.

### Table 2: ρ=0.6 Method Hierarchy

1. **Hierarchy holds across ρ**: Adaptive (17.736) < Uniform (17.763) < ESS-only (17.770), consistent with ρ=0.4 ordering. Supports Claim 1.
2. **Adaptive-Uniform gap at ρ=0.6**: 0.027 PPL, comparable to the gap at ρ=0.4.
3. **Tau-sweep alignment**: tau=0.6 (17.736) and tau=0.7 (17.730) match adaptive, suggesting low sensitivity to tau in this range.
4. **Pending data**: Random and Grid b=0.3 baselines at ρ=0.6 still running, needed for complete cross-ρ comparison.

### Pending Items Summary

| Experiment | Status | Impact |
|------------|--------|--------|
| grid_b0_2_seed123, grid_b0_2_seed456 | RUNNING | Completes b=0.2 row |
| grid_b*_seed42 (b ≥ 0.5) | Missing from registry | 3-seed stats for high-b values |
| contamination_60_adaptive_seed456 | RUNNING | 3-seed adaptive at ρ=0.6 |
| contamination_60_random_seed42 | RUNNING | Random baseline at ρ=0.6 |
| contamination_60_grid_b0_3_seed42 | RUNNING | Grid comparison at ρ=0.6 |
| contamination_60_grid_b0_5_seed42 | No metrics | Needs re-check or re-run |
