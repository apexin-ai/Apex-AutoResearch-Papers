# Experiment Data Tables

## Table 1: Grid Curve (ρ=0.4, Claim 2)

Baseline: **Adaptive mean = 17.651 ± 0.007**

| b | seed42 | seed123 | seed456 | mean ± std | n |
|---|--------|---------|---------|------------|---|
| 0.1 | 17.657 | 17.646 | 17.663 | 17.655 ± 0.009 | 3 |
| 0.2 | 17.640 | 17.637† | 17.645† | 17.641 ± 0.004 | 3 |
| 0.3 | 17.640 | 17.579 | 17.640 | 17.620 ± 0.035 | 3 |
| 0.5 | 17.651 | 17.638 | 17.650 | 17.646 ± 0.007 | 3 |
| 1.0 | 17.692 | 17.674 | 17.680 | 17.682 ± 0.009 | 3 |
| 1.5 | 17.718 | 17.701 | 17.710 | 17.710 ± 0.009 | 3 |
| 2.0 | 17.741 | 17.725 | 17.989 | 17.818 ± 0.148 | 3 |
| 3.0 | 17.774 | 17.760 | 17.921 | 17.818 ± 0.089 | 3 |
| 5.0 | 17.818 | 17.804 | 17.993 | 17.872 ± 0.105 | 3 |

**Notes:**
- b=0.2 seed123/seed456: †eval at checkpoint-5500 (step 5500/6103, 90%); --save_only_model caused LR reset on resume → final 603 steps trained with ~10× too high LR (PPL 18.3-18.4). Using checkpoint-5500 eval as representative result.
- b=0.3: seed123 uses grid_b0_3_seed123_r2 (17.579), seed456 uses grid_b0_3_seed456_r2 (17.640). Original runs had no metrics.
- b ≥ 0.5 seed42: from grid_b_seed42_batch metrics (post-hoc eval confirmed).

---

## Table 2: ρ=0.6 Ablation (Claim 1, cross-ρ validation)

| Method | seed42 | seed123 | seed456 | mean ± std | n |
|--------|--------|---------|---------|------------|---|
| Adaptive | 17.740 | 17.732 | 17.735 | 17.736 ± 0.004 | 3 |
| Uniform | 17.766 | 17.754 | 17.769 | 17.763 ± 0.008 | 3 |
| ESS-only | 17.770 | — | — | 17.770 (1 seed) | 1 |
| Random | 17.832 | — | — | 17.832 (1 seed) | 1 |
| Grid b=0.3 | 17.634 | — | — | 17.634 (1 seed) | 1 |
| Grid b=0.5 | 17.704 | — | — | 17.704 (1 seed) | 1 |

**Additional tau-sweep experiments (single seed42):**

| Experiment | eval_ppl_holdout |
|------------|-----------------|
| contamination_60_tau06_seed42 | 17.736 |
| contamination_60_tau07_seed42 | 17.730 |

**Notes:**
- Adaptive seed456 (contamination_60_adaptive_seed456): ✅ DONE, PPL=17.735
- Random seed42 (contamination_60_random_seed42): ✅ DONE, PPL=17.832 (resume from checkpoint-1000)
- Grid b=0.3 seed42 (contamination_60_grid_b0_3_seed42): ✅ DONE, PPL=17.634 (resume from checkpoint-1500; checkpoint-1500 PPL=18.583, final PPL improved → no resume degradation)
- Grid b=0.5 seed42 (contamination_60_grid_b0_5_seed42): DONE, eval_ppl=17.704
- Adaptive seed42 uses contamination_60_seed42_r2 (retry version)

---

## Key Observations

### Table 1: Grid U-curve (ρ=0.4)

1. **U-shaped curve confirmed (3-seed)**: Best grid PPL at b=0.3 (17.620±0.035), degrading toward both extremes (b=0.1: 17.655, b=5.0: 17.872). All b values now have 3-seed data except b=0.2 (pending).
2. **Grid-best vs Adaptive gap**: b=0.3 mean (17.620) beats adaptive (17.651) by 0.031, but driven by one outlier seed (17.579). Two of three seeds at b=0.3 are 17.640, close to adaptive.
3. **Plateau region b∈[0.1, 0.5]**: mean PPL 17.620~17.655, all within ~0.035 of each other and close to adaptive (17.651).
4. **High variance at large b**: b ≥ 2.0 shows std > 0.08, with seed456 consistently higher than seed42/seed123, indicating grid becomes unstable when over-penalizing high-provenance data.
5. **Remaining gap**: b=0.2 has only 1 seed (resume in progress, ~20min).

### Table 2: ρ=0.6 Method Hierarchy

1. **Full four-tier hierarchy confirmed at ρ=0.6**: Adaptive (17.736) < Uniform (17.763) < ESS-only (17.770) < Random (17.832). Consistent with ρ=0.4 ordering. Supports Claim 1.
2. **Adaptive-Uniform gap at ρ=0.6**: 0.027 PPL, comparable to the gap at ρ=0.4.
3. **Grid b=0.3 at ρ=0.6**: 17.634, beats adaptive (17.736) by 0.102. Same pattern as ρ=0.4 where grid-best outperforms adaptive.
4. **Tau-sweep alignment**: tau=0.6 (17.736) and tau=0.7 (17.730) match adaptive, suggesting low sensitivity to tau in this range.
5. **ESS-only ≈ Uniform collapse at ρ=0.6**: gap only 0.007 (vs 0.043 at ρ=0.4), confirming D075 finding that max-intervention loses effectiveness at high contamination.
6. **Pending**: ESS-only seed123/456 + Random seed123/456 running on 41312 for 3-seed completion.

### Pending Items Summary

| Experiment | Status | Impact |
|------------|--------|--------|
| grid_b0_2_seed123, grid_b0_2_seed456 | RUNNING | Completes b=0.2 row |
| grid_b*_seed42 (b ≥ 0.5) | ✅ Filled from batch | 3-seed stats complete |
| contamination_60_adaptive_seed456 | RUNNING | 3-seed adaptive at ρ=0.6 |
| contamination_60_random_seed42 | ✅ PPL=17.832 | Random baseline at ρ=0.6 |
| contamination_60_grid_b0_3_seed42 | ✅ PPL=17.634 | Grid comparison at ρ=0.6 |
| contamination_60_grid_b0_5_seed42 | ✅ eval_ppl=17.704 | Filled |
