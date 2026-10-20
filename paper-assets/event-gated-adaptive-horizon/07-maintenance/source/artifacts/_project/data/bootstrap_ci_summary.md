# Bootstrap 95% Confidence Intervals — Event-Gated Adaptive Horizon

N_BOOTSTRAP = 10,000 resamples. Date: 2026-05-16.

## Per-Condition Metrics

| Condition | Metric | n | Mean | 95% CI Lower | 95% CI Upper | Adequate? |
|-----------|--------|---|------|--------------|--------------|-----------|
| trained_dt_emb | nve_peak | 2 | 3.085 | 2.050 | 4.120 | ⚠️ n<3 |
| trained_dt_emb | nve_sustained_avg | 2 | 1.595 | 1.030 | 2.160 | ⚠️ n<3 |
| trained_dt_emb | eval_return_peak | 2 | 222.880 | 167.220 | 278.540 | ⚠️ n<3 |
| trained_dt_emb | eval_return_final | 2 | 175.340 | 82.750 | 267.930 | ⚠️ n<3 |
| trained_dt_emb | collapse_rate | 2 | 0.500 | 0.000 | 1.000 | ⚠️ n<3 |
| no_dt_emb | nve_peak | 3 | 1.050 | 0.870 | 1.260 | ✓ |
| no_dt_emb | nve_sustained_avg | 3 | 0.663 | 0.570 | 0.770 | ✓ |
| no_dt_emb | eval_return_peak | 3 | 485.440 | 359.140 | 594.180 | ✓ |
| no_dt_emb | eval_return_final | 3 | 357.350 | 148.340 | 503.000 | ✓ |
| no_dt_emb | collapse_rate | 3 | 0.000 | 0.000 | 0.000 | ✓ |
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

## Effect Sizes: trained_dt_emb − no_dt_emb (bootstrap, n=2 vs n=3)

| Metric | Δ Mean | 95% CI Lower | 95% CI Upper |
|--------|--------|--------------|--------------|
| nve_peak | +2.035 | +0.790 | +3.250 |
| nve_sustained_avg | +0.932 | +0.260 | +1.590 |
| eval_return_peak | -262.560 | -426.960 | -80.600 |
| collapse_rate | +0.500 | +0.000 | +1.000 |

## NVE > 1.5× Threshold Exceedance Rate

| Condition | Rate | 95% CI Lower | 95% CI Upper | n |
|-----------|------|--------------|--------------|---|
| trained_dt_emb | 1.000 | 0.342 | 1.000 | 2 |
| no_dt_emb | 0.000 | 0.000 | 0.000 | 3 |
| SGS_partial | 1.000 | 0.000 | 1.000 | 1 |
| SGS_full | 0.000 | 0.000 | 1.000 | 1 |
| frozen_dt_emb | 0.000 | 0.000 | 1.000 | 1 |
| no_subsample | 0.000 | 0.000 | 1.000 | 1 |
| dt1_imag | 1.000 | 0.000 | 1.000 | 1 |

## Cross-Environment Classification

**Cannot compute.** Only 1 Cheetah Run experiment exists (baseline 010a).
All treatment conditions are Walker Walk only.

**Recommendation:** Run 2-3 Cheetah seeds each for trained_dt_emb and no_dt_emb conditions.

## Sample Size Notes

| Condition | Seeds | Status |
|-----------|-------|--------|
| trained_dt_emb | 2 | **INSUFFICIENT** — need ≥3 seeds (008d_s1 ALLOCATED) |
| no_dt_emb | 3 | Adequate |
| SGS_partial | 1 | **INSUFFICIENT** — need ≥3 seeds |
| SGS_full | 1 | **INSUFFICIENT** — need ≥3 seeds |
| frozen_dt_emb | 1 | **INSUFFICIENT** — need ≥3 seeds |
| no_subsample | 1 | **INSUFFICIENT** — need ≥3 seeds |
| dt1_imag | 2 | **INSUFFICIENT** — need ≥3 seeds |
| baseline_walker | 3 | Adequate |

## Independence Notes

- **trained_dt_emb**: Walker-only condition, effective n=2.
  009e excluded (seed=0, identical to 008d — naming error). 010b excluded (Cheetah Run, cross-env).
  Independent seeds: 008d (seed 0) + 009b (seed 2). 008d_civo_trigger_s1 (seed 1) ALLOCATED.
- **no_dt_emb**: 3 fully independent seeds (008f s1, 009c s2, 008f s3). exp_020 excluded — vanilla DreamerV3 (different design).
- **SGS_full**: 018v2 (seed 1) only. Exp 018 excluded — invalid config (gate_enabled=false, D065).
- **All other conditions**: single seed only — CIs are degenerate (point estimates).
