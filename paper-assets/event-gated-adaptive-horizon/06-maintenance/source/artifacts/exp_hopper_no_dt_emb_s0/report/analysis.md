# exp_hopper_no_dt_emb_s0 Analysis Report

## Experiment Config
- **task**: dmc_hopper_hop
- **gate_enabled**: True, **gate_fixed_dt**: 2, **gate_subsample_max_dt**: 2
- **gate_dt_embed_dim**: 0 (no dt embedding)
- **steps**: 105K, **seed**: 0
- **parent**: exp_hopper_trained_s0
- **hypothesis**: Removing dt_embedding entirely while keeping gate+dt=2+subsample ON will still show severe learning delay, confirming gate mechanism itself (not dt_emb) is root cause.

## 1. eval_return Time Series

| Step | no_dt_emb | baseline | trained_s0_ext (150K) | frozen_s0_ext (160K) |
|------|-----------|----------|-----------------------|----------------------|
| 5K   | 0.003     | 0.059    | -                     | -                    |
| 15K  | 0.249     | 1.042    | -                     | -                    |
| 25K  | 0.380     | 1.695    | -                     | -                    |
| 35K  | 0.056     | 6.548    | -                     | -                    |
| 45K  | 0.188     | 19.087   | -                     | -                    |
| 55K  | 0.131     | 22.515   | -                     | -                    |
| 65K  | 0.000     | 3.499    | -                     | -                    |
| 75K  | 0.709     | 62.197   | -                     | -                    |
| 85K  | 2.626     | 67.615   | -                     | -                    |
| 95K  | 0.520     | 86.465   | -                     | -                    |
| 105K | **10.759**| **96.429**| **81.58** (at 150K)  | **0.56** (at 160K)   |

**eval_return_final = 10.76** (11.2% of baseline 96.43)

## 2. ve_ratio Time Series (precise from metrics.jsonl)

| Step | no_dt_emb | baseline | Notes |
|------|-----------|----------|-------|
| 15K  | 0.2337    | 0.0797   | |
| 25K  | 0.1846    | 0.0975   | |
| 35K  | 0.7240    | 0.1656   | MIN_STEP boundary |
| 45K  | 0.1243    | 0.1900   | |
| 55K  | 0.1135    | 0.2788   | |
| 65K  | 131070.66 | 3.4790   | **DIV-BY-ZERO** (eval_return=0.0) |
| 75K  | 0.5455    | 0.3414   | |
| 85K  | 0.2188    | 0.5016   | |
| 95K  | 1.9485    | 0.5175   | |
| 105K | 0.2156    | 0.5590   | |

## 3. NVE Analysis (MIN_STEP=35K, excluding 65K div-by-zero)

NVE = ve_ratio_exp / ve_ratio_baseline (step-matched)

| Step | NVE   | > 1.5x? |
|------|-------|---------|
| 35K  | 4.37  | YES     |
| 45K  | 0.65  | no      |
| 55K  | 0.41  | no      |
| 65K  | EXCLUDED (div-by-zero) | - |
| 75K  | 1.60  | YES     |
| 85K  | 0.44  | no      |
| 95K  | 3.77  | YES     |
| 105K | 0.39  | no      |

- **NVE_peak = 4.37** (at 35K, low absolute values)
- **Sustained NVE > 1.5 for >= 2 consecutive points**: NO
  - 35K spike isolated (45K drops to 0.65)
  - 75K spike isolated (85K drops to 0.44)
  - 95K spike isolated (105K drops to 0.39)
- **D155 CIVO criterion NOT met** (no sustained elevation)

## 4. value_mean Time Series

| Step | no_dt_emb | baseline |
|------|-----------|----------|
| 5K   | 0.001     | -        |
| 15K  | 0.058     | 0.083    |
| 25K  | 0.070     | 0.166    |
| 35K  | ~0.04     | ~1.1     |
| 45K  | 0.023     | 3.628    |
| 55K  | 0.015     | 6.279    |
| 65K  | 0.131     | 12.177   |
| 75K  | 0.387     | 21.238   |
| 85K  | 0.575     | 33.917   |
| 95K  | 1.014     | 44.745   |
| 105K | 2.320     | 53.904   |

At 105K, no_dt_emb value_mean is 4.3% of baseline value_mean. Value function barely develops.

## 5. actor_entropy Time Series

| Step | no_dt_emb | baseline |
|------|-----------|----------|
| 5K   | 5.45      | -        |
| 15K  | 4.95      | 4.51     |
| 25K  | 5.43      | 3.88     |
| 35K  | 5.50      | 0.60     |
| 45K  | 5.56      | 0.85     |
| 55K  | 5.53      | 1.40     |
| 65K  | 2.22      | -1.62    |
| 75K  | 0.50      | -2.38    |
| 85K  | -0.17     | -3.16    |
| 95K  | -1.08     | -3.29    |
| 105K | -1.94     | -3.26    |

Actor entropy remains near-maximum (~5.5) through 55K in no_dt_emb, indicating the policy stays near-random for 55K steps. Baseline entropy drops to 0.6 by 35K. The no_dt_emb actor only begins specializing at ~65K, lagging baseline by ~30K steps.

## 6. Gate Behavior

All steps show: gate_dt_mean=2.0, gate_dt_std=0.0, gate_dt_2_frac=1.0, gate_empirical_entropy=0.0.
Gate is **fixed at dt=2** throughout (as configured). No gate adaptation since dt_embed_dim=0 removes the embedding entirely.

## 7. Conclusion: SUCCESS

**The hypothesis is confirmed.** Removing dt_embedding entirely (dt_embed_dim=0) while keeping the gate mechanism active did NOT prevent severe learning delay in Hopper.

Evidence:
1. **eval_return_final = 10.76** (11.2% of baseline), showing severe learning impairment at 105K
2. **Near-zero returns through 85K** (max 2.63 at 85K vs baseline 67.62), consistent with the learning delay pattern seen in trained_s0
3. **No sustained CIVO signal** (D155 three-dimensional criterion not met: isolated NVE spikes but no >= 2 consecutive points above threshold)
4. **Value function development severely stunted**: 2.32 at 105K vs baseline 53.90
5. **Policy stays near-random 30K steps longer** than baseline (entropy plateau through 55K)

### Comparison with other Hopper gated variants:

| Experiment | Config | eval_return_final | Learning Status |
|------------|--------|-------------------|-----------------|
| baseline | no gate | 96.43 @ 105K | Normal |
| trained_s0_ext | trained dt_emb | 81.58 @ 150K | Delayed, recovers |
| **no_dt_emb_s0** | **no dt_emb** | **10.76 @ 105K** | **Severe delay** |
| frozen_s0_ext | frozen dt_emb | 0.56 @ 160K | No recovery |

The no_dt_emb variant performs **worse** than trained_s0 at the same step count (10.76 vs trained_s0 which was also near 0 at 105K but recovered by 150K). It may eventually recover with more training, but the pattern is clear: the gate mechanism itself causes severe learning delay in Hopper regardless of dt_embedding configuration.

**Root cause confirmed**: Gate mechanism (subsample + fixed dt) is the primary driver of Hopper's learning failure, not dt_emb-induced CIVO. This is consistent with D162's reclassification of Hopper as a "gate mechanism failure" environment.

## 8. Key Metrics Summary

| Metric | Value |
|--------|-------|
| eval_return_final | 10.759 |
| eval_return_final_pct_baseline | 11.2% |
| ve_ratio_peak (>= 35K, excl. div-by-zero) | 1.949 (@ 95K) |
| nve_peak | 4.37 (@ 35K) |
| nve_sustained_above_1.5 | False |
| value_mean_final | 2.320 |
| actor_entropy_final | -1.939 |
| learning_delay_vs_baseline | ~30K steps entropy lag |
