# Bootstrap 95% Confidence Intervals — Event-Gated Adaptive Horizon

N_BOOTSTRAP = 10,000 resamples. Date: 2026-05-16.

## Per-Condition Metrics

| Condition | Metric | n | Mean | 95% CI Lower | 95% CI Upper | Adequate? |
|-----------|--------|---|------|--------------|--------------|-----------|
| trained_dt_emb | nve_peak | 3 | 3.430 | 2.050 | 4.120 | ✓ |
| trained_dt_emb | nve_sustained_avg | 3 | 1.775 | 1.030 | 2.425 | ✓ |
| trained_dt_emb | eval_return_peak | 3 | 231.920 | 167.220 | 278.540 | ✓ |
| trained_dt_emb | eval_return_final | 3 | 160.587 | 82.750 | 267.930 | ✓ |
| trained_dt_emb | collapse_rate | 3 | 0.667 | 0.000 | 1.000 | ✓ |
| no_dt_emb | nve_peak | 2 | 1.140 | 1.020 | 1.260 | ⚠️ n<3 |
| no_dt_emb | nve_sustained_avg | 2 | 0.710 | 0.650 | 0.770 | ⚠️ n<3 |
| no_dt_emb | eval_return_peak | 2 | 431.070 | 359.140 | 503.000 | ⚠️ n<3 |
| no_dt_emb | eval_return_final | 2 | 325.670 | 148.340 | 503.000 | ⚠️ n<3 |
| no_dt_emb | collapse_rate | 2 | 0.000 | 0.000 | 0.000 | ⚠️ n<3 |
| SGS_partial | nve_peak | 1 | 10.420 | 10.420 | 10.420 | ⚠️ n<3 |
| SGS_partial | nve_sustained_avg | 1 | 2.460 | 2.460 | 2.460 | ⚠️ n<3 |
| SGS_partial | eval_return_peak | 1 | 326.670 | 326.670 | 326.670 | ⚠️ n<3 |
| SGS_partial | eval_return_final | 1 | 31.730 | 31.730 | 31.730 | ⚠️ n<3 |
| SGS_partial | collapse_rate | 1 | 1.000 | 0.000 | 1.000 | ⚠️ n<3 |
| SGS_full | nve_peak (35K+ window) | 1 | 1.660 | 1.660 | 1.660 | ⚠️ n<3 |
| SGS_full | nve_sustained_avg | 1 | 1.340 | 1.340 | 1.340 | ⚠️ n<3 |
| SGS_full | eval_return_peak | 1 | 499.600 | 499.600 | 499.600 | ⚠️ n<3 |
| SGS_full | eval_return_final | 1 | 448.340 | 448.340 | 448.340 | ⚠️ n<3 |
| SGS_full | collapse_rate | 1 | 0.000 | 0.000 | 1.000 | ⚠️ n<3 |
| frozen_dt_emb | nve_peak | 1 | 0.467 | 0.467 | 0.467 | ⚠️ n<3 |
| frozen_dt_emb | nve_sustained_avg | 1 | 0.427 | 0.427 | 0.427 | ⚠️ n<3 |
| frozen_dt_emb | eval_return_peak | 1 | 238.400 | 238.400 | 238.400 | ⚠️ n<3 |
| frozen_dt_emb | eval_return_final | 1 | 204.200 | 204.200 | 204.200 | ⚠️ n<3 |
| frozen_dt_emb | collapse_rate | 1 | 0.000 | 0.000 | 1.000 | ⚠️ n<3 |
| no_subsample | nve_peak | 1 | 0.930 | 0.930 | 0.930 | ⚠️ n<3 |
| no_subsample | nve_sustained_avg | 1 | 0.730 | 0.730 | 0.730 | ⚠️ n<3 |
| no_subsample | eval_return_peak | 1 | 777.660 | 777.660 | 777.660 | ⚠️ n<3 |
| no_subsample | eval_return_final | 1 | 777.660 | 777.660 | 777.660 | ⚠️ n<3 |
| no_subsample | collapse_rate | 1 | 0.000 | 0.000 | 1.000 | ⚠️ n<3 |
| dt1_imag | nve_peak | 1 | 3.780 | 3.780 | 3.780 | ⚠️ n<3 |
| dt1_imag | nve_sustained_avg | 1 | 1.350 | 1.350 | 1.350 | ⚠️ n<3 |
| dt1_imag | eval_return_peak | 2 | 792.555 | 715.210 | 869.900 | ⚠️ n<3 |
| dt1_imag | eval_return_final | 2 | 503.430 | 136.960 | 869.900 | ⚠️ n<3 |
| dt1_imag | collapse_rate | 2 | 0.500 | 0.000 | 1.000 | ⚠️ n<3 |
| baseline_walker | eval_return_peak | 3 | 962.770 | 950.960 | 970.410 | ✓ |
| baseline_walker | eval_return_final | 2 | 942.735 | 927.600 | 957.870 | ⚠️ n<3 |

## Effect Sizes: trained_dt_emb − no_dt_emb (bootstrap)

| Metric | Δ Mean | 95% CI Lower | 95% CI Upper |
|--------|--------|--------------|--------------|
| nve_peak | +2.290 | +0.910 | +3.100 |
| nve_sustained_avg | +1.065 | +0.320 | +1.715 |
| eval_return_peak | -199.150 | -308.187 | -90.113 |
| collapse_rate | +0.667 | +0.000 | +1.000 |

## NVE > 1.5× Threshold Exceedance Rate

| Condition | Rate | 95% CI Lower | 95% CI Upper | n |
|-----------|------|--------------|--------------|---|
| trained_dt_emb | 1.000 | 1.000 | 1.000 | 3 |
| no_dt_emb | 0.000 | 0.000 | 0.000 | 2 |
| SGS_partial | 1.000 | 0.000 | 1.000 | 1 |
| SGS_full | 0.250 | — | — | 8 steps (35K+ window) |
| frozen_dt_emb | 0.000 | 0.000 | 1.000 | 1 |
| no_subsample | 0.000 | 0.000 | 1.000 | 1 |
| dt1_imag | 1.000 | 0.000 | 1.000 | 1 |

## Effect Sizes: SGS_full − trained_dt_emb (point estimates, n=1 vs n=3)

| Metric | SGS_full | trained_dt_emb (mean) | Δ | Note |
|--------|----------|----------------------|---|------|
| nve_peak (35K+) | 1.660 | 3.430 | −1.770 | SGS_full peak at 95K; raw 4.01× at 25K excluded (pre-threshold noise) |
| nve_sustained_avg | 1.340 | 1.775 | −0.435 | SGS_full sustains less |
| eval_return_peak | 499.600 | 231.920 | +267.680 | SGS_full much higher return (peak@75K) |
| eval_return_final | 448.340 | 160.587 | +287.753 | No collapse in SGS_full |
| collapse_rate | 0.000 | 0.667 | −0.667 | SGS_full avoids collapse |

> **Caveat:** SGS_full has n=1 (018v2 only). No CI can be computed. Need seed 2 to confirm.
>
> **NVE peak correction (2026-05-16):** SGS_full raw NVE peak is 4.01× at 25K, but this is pre-threshold noise outside the 35K+ diagnostic window. The reliable peak within the 35K+ window is 1.66× at 95K. NVE timeline (35K+): [1.61, 1.38, 1.27, 1.04, 0.83, 1.08, 1.66, 1.34]. Exceedance rate (>1.5×) = 2/8 = 25% (steps 35K and 95K).

## Cross-Environment Classification

**Cannot compute.** Only 1 Cheetah Run experiment exists (baseline 010a).
All treatment conditions are Walker Walk only.

**Recommendation:** Run 2-3 Cheetah seeds each for trained_dt_emb and no_dt_emb conditions.

## Sample Size Notes

| Condition | Seeds | Status |
|-----------|-------|--------|
| trained_dt_emb | 3 | Adequate |
| no_dt_emb | 2 | **INSUFFICIENT** — need ≥3 seeds |
| SGS_partial | 1 | **INSUFFICIENT** — need ≥3 seeds |
| SGS_full | 1 | **INSUFFICIENT** — need ≥3 seeds |
| frozen_dt_emb | 1 | **INSUFFICIENT** — need ≥3 seeds |
| no_subsample | 1 | **INSUFFICIENT** — need ≥3 seeds |
| dt1_imag | 2 | **INSUFFICIENT** — need ≥3 seeds |
| baseline_walker | 3 | Adequate |

## Independence Notes

- **trained_dt_emb**: 008d (seed 0, 55K) and 009e (seed 1, 105K) share first 55K steps.
  For NVE peak at 55K they are effectively the same observation.
  Conservative effective n=2 for this condition.
- **no_dt_emb**: 2 fully independent seeds (008f s1, 009c s2).
- **SGS_full**: 018v2 (seed 1) only. Exp 018 excluded — invalid config (gate_enabled=false, not actually SGS). Need seed 2.
- **All other conditions**: single seed only — CIs are degenerate (point estimates).
