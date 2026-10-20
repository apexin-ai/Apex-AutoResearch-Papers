# exp_cheetah_008a_s0 Analysis

## Experiment Config
- **Task**: Cheetah Run (C3 cross-env value growth suppression)
- **Parent**: exp_008a_no_subsample_dt2 (Walker Walk, NVE=0.59)
- **Key params**: gate_fixed_dt=2, gate_subsample_max_dt=1 (subsample OFF), imag_horizon=15, seed=0
- **Hypothesis**: Untrained dt=2 embedding → no CIVO, value suppression

## Metrics at 105K

| Metric | Value |
|--------|-------|
| eval_return | 366.19 |
| value_mean | 164.58 |
| **NVE** | **0.449** |
| civo_alert | 0 (all steps) |
| gate_dt_mean | 2.0 |
| gate_dt_2_frac | 1.0 |
| EMA_005 | 132.95 |
| EMA_095 | 174.91 |
| model_loss | 1.83 |
| kl | 1.72 |

## Eval Return Trajectory

| Step | eval_return |
|------|------------|
| 5K | 8.3 |
| 15K | 24.3 |
| 25K | 343.9 |
| 35K | 306.9 |
| 45K | 391.8 |
| 55K | 325.1 |
| 65K | 344.3 |
| 75K | 433.5 |
| **85K** | **483.0** (peak) |
| 95K | 415.4 |
| 105K | 366.2 |

## Cross-Seed Comparison (s0 vs s1)

| Metric | s0 | s1 | Delta |
|--------|-----|------|-------|
| eval_return_105K | 366.2 | 281.2 | +85.0 |
| value_mean_105K | 164.6 | 164.3 | +0.3 |
| NVE_105K | 0.449 | 0.584 | -0.135 |
| eval_return_peak | 483.0 (85K) | 519.6 (75K) | -36.6 |
| civo_alert | 0 | 0 | same |
| gate_dt_2_frac | 1.0 | 1.0 | same |

Seed variance is within normal range. value_mean nearly identical across seeds (~164). eval_return differs by ~85 at 105K but both show healthy learning curves. NVE values both well below tau=2.0.

## Conclusion: **SUCCESS**

- NVE=0.449 << tau=2.0 → no CIVO detected
- civo_alert=0 throughout training
- Value suppression pattern confirmed: untrained dt=2 embedding prevents value overestimation in Cheetah Run, matching Walker 008a behavior
- Cross-env generalization of the C3 mechanism validated across 2 seeds and 2 environments (Walker Walk + Cheetah Run)
