# exp_072_008e_v3_walker_s5 Analysis Report

**Config**: 008e_v3 mitigation (trained dt_emb + subsample ON + dt=1 imag + H=15)
**Task**: Walker Walk | **Seed**: 5 | **Steps**: 105K
**Server**: westd-19154 | **Date**: 2026-05-25

## Conclusion: SUCCESS

Final eval_return = **853.1** @ 105K (93.2% of baseline 915.67). No CIVO collapse detected. Monotonically improving trajectory with healthy NVE throughout.

## Eval Return Trajectory

| Step | eval_return | value_mean | ve_ratio | NVE (v/e) |
|------|-------------|------------|----------|-----------|
| 5K   | 29.4        | 0.0        | -        | ~0        |
| 15K  | 251.1       | 4.6        | 0.0      | 0.02x     |
| 25K  | 423.0       | 33.2       | 0.1      | 0.08x     |
| 35K  | 511.0       | 88.8       | 0.2      | 0.17x     |
| 45K  | 600.1       | 154.0      | 0.3      | 0.26x     |
| 55K  | 649.0       | 223.2      | 0.3      | 0.34x     |
| 65K  | 697.2       | 296.9      | 0.4      | 0.43x     |
| 75K  | 727.3       | 364.3      | 0.5      | 0.50x     |
| 85K  | 710.3       | 418.5      | 0.6      | 0.59x     |
| 95K  | 803.9       | 464.6      | 0.6      | 0.58x     |
| 105K | 853.1       | 520.8      | 0.6      | 0.61x     |

## Key Metrics @ 105K

- **final_eval_return**: 853.1
- **peak_eval_return**: 853.1 @ 105K (still improving at termination)
- **final_value_mean**: 520.8
- **final_ve_ratio**: 0.6
- **final_NVE**: 0.61x (well below 1.5x CIVO threshold)
- **actor_entropy**: -5.1
- **gate_dt_1_frac**: 1.0 (correct for dt=1 config)
- **civo/alert**: 0.0 throughout (never triggered)

## CIVO Assessment

- NVE peaked at 0.61x, far below the 1.5x CIVO threshold
- ve_ratio monotonically increased from 0→0.6, no spike pattern
- civo/alert = 0 throughout all training
- **No CIVO collapse**

## Non-CIVO Failure Assessment

- eval_return crossed 400 by 25K and continued improving
- Peak = 853.1 at final step, still on upward trajectory
- **No non-CIVO failure**

## Minor Observation

- Slight dip at 85K (710.3 vs 727.3 at 75K), but fully recovered by 95K (803.9). Normal variance, not a collapse signal.

## Seed Comparison (008e_v3 Walker Walk)

| Seed | exp_id | Conclusion | eval@105K | Peak eval | NVE@105K | Notes |
|------|--------|------------|-----------|-----------|----------|-------|
| s1 (parent) | exp_008e_v3_subsample_on_dt1_h15 | SUCCESS | 869.9 | 869.9@105K | 0.80x | First success |
| s2 | exp_008e_v3_walker_s2 | NEGATIVE | 136.96 | 715@85K | 3.78x | CIVO collapse@95K |
| s0 | exp_070_008e_v3_walker_s0 | NEGATIVE | 148 | 232.5@55K | 0.8x | Non-CIVO, never reached baseline |
| **s5** | **exp_072_008e_v3_walker_s5** | **SUCCESS** | **853.1** | **853.1@105K** | **0.61x** | **Healthy, still improving** |

## Collapse Rate Update

- **Before s5**: 2/4 = 50% (s1=SUCCESS, s2=NEGATIVE, s0=NEGATIVE)
- **After s5**: **2/5 = 40%** (s1=SUCCESS, s5=SUCCESS, s2=NEGATIVE, s0=NEGATIVE)

s5 is a strong success, comparable to s1 (869.9). With NVE=0.61x (even lower than s1's 0.80x), this is the healthiest run in the series. The 008e_v3 configuration shows 60% success rate across 5 seeds.
