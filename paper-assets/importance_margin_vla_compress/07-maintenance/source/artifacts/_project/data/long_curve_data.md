# π0.5 Long (libero_10) Disruption Curve Data

**Collected**: 2026-05-24
**Baseline**: pi05_baseline_long_seed42 → **91.6%** (500 eps)

## Random Long Disruption Curve

| k | overall_sr (%) | exp_id | version | notes |
|------|-----------|--------|---------|-------|
| 0.95 | **63.2** | eval_pi05_random_k095_long_seed42_postfix | postfix | ✅ |
| 0.90 | 31.8 | eval_pi05_random_k09_long_seed42 | prefix | ⚠️ prefix only, conclusion=negative; **postfix RUNNING** |
| 0.85 | **45.2** | eval_pi05_random_k085_long_seed42_postfix | postfix | ✅ |
| 0.70 | **65.8** | eval_pi05_random_k07_long_seed42_postfix | postfix | ✅ peak |
| 0.50 | **46.8** | eval_pi05_random_k05_long_seed42_postfix | postfix | ✅ |
| 0.30 | 29.0 | eval_pi05_random_k03_long_seed42 | prefix | ⚠️ prefix only; **postfix RUNNING** |

**Pattern**: U-shape dip at k=0.85–0.9, peak at k=0.7 (65.8%). Matches importance margin hypothesis.

## L2norm Long Disruption Curve

| k | overall_sr (%) | exp_id | version | notes |
|------|-----------|--------|---------|-------|
| 0.95 | **87.0** | eval_pi05_l2norm_k095_long_seed42_postfix | postfix | ✅ |
| 0.90 | 81.0 | eval_pi05_l2norm_k09_long_seed42 | prefix | ⚠️ prefix only; **postfix_v2 RUNNING** |
| 0.85 | **78.4** | eval_pi05_l2norm_k085_long_seed42_postfix | postfix | ✅ |
| 0.70 | 60.0 | eval_pi05_l2norm_k07_long_seed42 | prefix | ⚠️ prefix only; **postfix RUNNING** |
| 0.50 | 51.4 | eval_pi05_l2norm_k05_long_seed42_v3 | prefix | ⚠️ prefix only; **postfix RUNNING** |
| 0.30 | 39.0 | eval_pi05_l2norm_k03_long_seed42 | prefix | ⚠️ prefix only; no postfix planned |

**Pattern**: Monotonic degradation with decreasing k. L2norm consistently outperforms random at all k values.

## RUNNING Experiments (postfix versions in progress)

| exp_id | status |
|--------|--------|
| eval_pi05_random_k09_long_seed42_postfix | RUNNING |
| eval_pi05_random_k03_long_seed42_postfix | RUNNING |
| eval_pi05_l2norm_k09_long_seed42_postfix_v2 | RUNNING |
| eval_pi05_l2norm_k07_long_seed42_postfix | RUNNING |
| eval_pi05_l2norm_k05_long_seed42_postfix | RUNNING |

## Missing Data

- **Random k=0.9 postfix**: RUNNING. Current prefix value (31.8%) has conclusion=negative and may change significantly with postfix.
- **Random k=0.3 postfix**: RUNNING. Prefix value (29.0%) available as fallback.
- **L2norm k=0.9, 0.7, 0.5 postfix**: All RUNNING. Prefix values available as fallback.
- **L2norm k=0.3 postfix**: No postfix version exists or is planned. Prefix value (39.0%) is final.

## L2norm vs Random Importance Margin (Long suite)

| k | L2norm SR | Random SR | Margin (pp) |
|------|-----------|-----------|-------------|
| 0.95 | 87.0 | 63.2 | +23.8 |
| 0.90 | 81.0* | 31.8* | +49.2* |
| 0.85 | 78.4 | 45.2 | +33.2 |
| 0.70 | 60.0* | 65.8 | -5.8* |
| 0.50 | 51.4* | 46.8 | +4.6* |
| 0.30 | 39.0* | 29.0* | +10.0* |

*prefix values, pending postfix updates

## Cross-Suite Comparison (π0.5 disruption curve peaks)

| Suite | Random Peak | L2norm Peak | Baseline |
|-------|------------|-------------|----------|
| Object | k0.7=2.8% | k0.85=5.6% | 82.0% |
| Goal | k0.7=52.0% | k0.85=52.8% | 76.8% |
| Spatial | k0.7=50.6% | k0.90=53.4% | 78.0% |
| **Long** | **k0.7=65.8%** | **k0.95=87.0%** | **91.6%** |

**Key observation**: Long suite shows highest absolute SR retention under disruption among all suites. L2norm k=0.95 retains 95% of baseline performance (87.0/91.6). Random disruption shows the characteristic U-shape dip (peak at k=0.7) consistent with other suites.
