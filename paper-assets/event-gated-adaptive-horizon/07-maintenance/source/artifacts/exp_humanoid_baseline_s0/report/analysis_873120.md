# exp_humanoid_baseline_s0 — Analysis Report

## Experiment Summary
- **Task**: dmc_humanoid_walk (21-DoF)
- **Model**: DreamerV3-S (baseline, dt=1, no gate)
- **Steps**: 200K (ran to 212K)
- **Seed**: 0
- **Server**: westd-51268
- **Status**: Completed (EXIT_CODE=0)

## Hypothesis
> Humanoid Walk baseline (dt=1, no gate) establishes reference performance for 21-DoF environment CIVO verification. Expect stable training without value overestimation (NVE < 2.0×).

## Conclusion: **NEGATIVE** — Hypothesis Falsified

The baseline exhibits **severe, persistent value overestimation** throughout training. NVE never drops below 2.3× after 35K steps, peaks at 13.0× (105K), and reaches 12.2× at experiment end. Three CIVO alerts triggered. eval_return remains flat at ~1.2 — effectively no learning.

## Key Metrics

| Metric | Value |
|--------|-------|
| eval_return (final, 205K) | 1.24 |
| eval_return (last 5 mean±std) | 1.48 ± 0.36 |
| eval_return (overall mean) | 1.22 |
| eval_return (max) | 2.16 (at 165K) |
| NVE_105K | **13.0×** |
| NVE_peak | **13.0×** (at 105K) |
| NVE_final (205K) | **12.2×** |
| NVE_mean (≥35K) | **7.7×** |
| NVE_min (≥35K) | 2.3× (at 165K) |
| CIVO alerts | 3 (at 55K, 105K, 195K) |
| value_mean (final) | 15.2 |
| value_mean (35K) | 5.5 |

## eval_return Trajectory

| Step | eval_return |
|------|-------------|
| 5K | 1.2 |
| 15K | 0.6 |
| 25K | 1.2 |
| 35K | 1.4 |
| 45K | 1.2 |
| 55K | 1.1 |
| 65K | 1.8 |
| 75K | 0.9 |
| 85K | 1.5 |
| 95K | 1.4 |
| 105K | 1.0 |
| 115K | 0.9 |
| 125K | 1.0 |
| 135K | 1.6 |
| 145K | 0.6 |
| 155K | 1.2 |
| 165K | 2.2 |
| 175K | 1.4 |
| 185K | 1.4 |
| 195K | 1.2 |
| 205K | 1.2 |

## NVE (ve_ratio) Trajectory (step ≥ 35K)

| Step | ve_ratio | delta_ve | alert | value_mean |
|------|----------|----------|-------|------------|
| 35K | 3.9 | 1.2 | 0 | 5.5 |
| 45K | 5.5 | 1.6 | 0 | 6.7 |
| 55K | 9.7 | 4.2 | **1** | 10.8 |
| 65K | 6.7 | -2.9 | 0 | 12.0 |
| 75K | 10.4 | 3.6 | 0 | 9.4 |
| 85K | 6.6 | -3.8 | 0 | 10.1 |
| 95K | 7.5 | 0.9 | 0 | 10.7 |
| 105K | **13.0** | 5.5 | **1** | 12.7 |
| 115K | 11.0 | -2.0 | 0 | 10.4 |
| 125K | 7.3 | -3.7 | 0 | 7.2 |
| 135K | 3.4 | -3.9 | 0 | 5.4 |
| 145K | 11.8 | 8.4 | 0 | 7.5 |
| 155K | 4.9 | -6.9 | 0 | 5.9 |
| 165K | 2.3 | -2.6 | 0 | 5.1 |
| 175K | 5.3 | 2.9 | 0 | 7.5 |
| 185K | 6.4 | 1.1 | 0 | 8.9 |
| 195K | 9.9 | 3.5 | **1** | 11.4 |
| 205K | **12.2** | 2.3 | 0 | 15.2 |

## Analysis

### Value Overestimation Pattern
The value function inflates unboundedly while actual return stays flat:
- value_mean grows from 5.5 (35K) → 15.2 (205K), a ~3× increase
- eval_return stays flat at ~1.2 throughout
- This creates an ever-widening gap: NVE = value_mean / eval_return

### NVE Oscillation
NVE shows large oscillations (2.3× to 13.0×) driven by:
1. **value_mean fluctuations**: value function periodically contracts then re-inflates
2. **eval_return noise**: small denominator amplifies ratio volatility
3. The pattern shows two inflation cycles: 35K→105K (peak 13.0×), then partial reset and 165K→205K (peak 12.2× and rising)

### Comparison with Other Baselines
| Environment | eval_return | NVE_peak | NVE_105K | CIVO alerts |
|-------------|-------------|----------|----------|-------------|
| Walker Walk | ~950 | < 2.0× | < 2.0× | 0 |
| Cheetah Run | ~430 | < 2.0× | < 2.0× | 0 |
| **Humanoid Walk** | **~1.2** | **13.0×** | **13.0×** | **3** |

### Implications
1. **Humanoid Walk is intrinsically CIVO-prone** for DreamerV3-S even without any horizon extension — fundamentally different from Walker/Cheetah baselines
2. The 21-DoF action space appears to create a natural breeding ground for value overestimation in the world model
3. eval_return ~1.2 (vs Walker ~950) indicates DreamerV3-S struggles with Humanoid complexity at this model scale
4. This baseline establishes that **CIVO intervention is needed even at dt=1** for Humanoid, making it a strong stress-test for the gating mechanism
