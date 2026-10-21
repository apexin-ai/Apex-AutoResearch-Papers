# Supplementary Experiment Results

All results from experiments with status=DONE, conclusion=success.

## A. Threshold (τ) Sensitivity Analysis

**Total experiments: 55** (with valid SR values)

### pi05 / goal

| τ | seed | SR (%) | trigger_rate | source_exp_id |
|---|------|--------|-------------|---------------|
| 0.15 | 42 | 92.0 | 0.174 | pi05-adaptive-goal-s42-tau015-bjb2 |
| 0.15 | 43 | 87.5 | — | pi05-goal-tau015-s43-r3 |
| 0.25 | 43 | 88.5 | — | pi05-goal-tau025-s43-r3 |
| 0.35 | 42 | 87.5 | 0.057 | pi05-adaptive-goal-s42-tau035-bjb2 |
| 0.35 | 43 | 89.5 | — | pi05-goal-tau035-s43-r3 |
| 0.5 | 42 | 87.0 | 0.0206 | pi05-tau-sweep-goal-tau050-s42-r3 |
| 0.7 | 42 | 87.0 | 0.0104 | tau_sweep_goal_tau070_s42_cqa1 |
| 0.9 | 42 | 89.0 | 0.0035 | tau_sweep_goal_tau090_s42_cqa1 |

### pi05 / long

| τ | seed | SR (%) | trigger_rate | source_exp_id |
|---|------|--------|-------------|---------------|
| 0.15 | 42 | 84.0 | 0.114 | pi05-adaptive-long-s42-tau015-bjb2 |
| 0.15 | 43 | 82.0 | — | pi05-long-tau015-s43-r3 |

### pi05 / spatial

| τ | seed | SR (%) | trigger_rate | source_exp_id |
|---|------|--------|-------------|---------------|
| 0.15 | 42 | 97.0 | 0.112 | pi05-adaptive-spatial-s42-tau015-bjb2 |
| 0.15 | 43 | 96.5 | 0.117 | pi05-spatial-tau015-s43 |
| 0.25 | 43 | 98.5 | 0.028 | pi05-spatial-tau025-s43 |
| 0.35 | 42 | 96.5 | 0.0255 | pi05-adaptive-spatial-s42-tau035-bjb2 |
| 0.35 | 43 | 97.5 | 0.022 | pi05-spatial-tau035-s43 |

### smolvla / goal

| τ | seed | SR (%) | trigger_rate | source_exp_id |
|---|------|--------|-------------|---------------|
| 0.15 | 42 | 85.5 | 0.333 | smolvla-tau015-goal-s42 |
| 0.15 | 42 | 85.0 | 0.339 | eval-ablation-tau015-goal-s42 |
| 0.15 | 43 | 83.5 | 0.354 | smolvla-tau015-goal-s43 |
| 0.25 | 42 | 84.0 | 0.083 | smolvla-tau025-goal-s42 |
| 0.25 | 43 | 81.0 | 0.0925 | smolvla-tau025-goal-s43 |
| 0.35 | 42 | 82.5 | 0.024 | smolvla-tau035-goal-s42 |
| 0.35 | 43 | 85.5 | 0.0211 | smolvla-tau035-goal-s43 |

### smolvla / long

| τ | seed | SR (%) | trigger_rate | source_exp_id |
|---|------|--------|-------------|---------------|
| 0.1 | 42 | 53.5 | 0.613 | smolvla-tau010-long-s42 |
| 0.15 | 42 | 61.0 | 0.239 | smolvla-tau015-long-s42 |
| 0.15 | 43 | 61.0 | 0.236 | smolvla-tau015-long-s43 |
| 0.2 | 42 | 58.5 | 0.089 | smolvla-tau020-long-s42 |
| 0.2 | 43 | 54.5 | — | smolvla-tau020-long-s43-r2 |
| 0.25 | 42 | 56.0 | 0.042 | smolvla-tau025-long-s42 |
| 0.25 | 43 | 53.0 | 0.046 | smolvla-tau025-long-s43 |
| 0.3 | 42 | 54.5 | — | smolvla-tau030-long-s42-r2 |
| 0.3 | 43 | 55.5 | — | smolvla-tau030-long-s43-r2 |
| 0.35 | 42 | 57.5 | 0.013 | smolvla-tau035-long-s42 |
| 0.35 | 43 | 60.0 | 0.01 | smolvla-tau035-long-s43 |
| 0.4 | 42 | 60.0 | 0.004 | smolvla-tau040-long-s42 |
| 0.45 | 42 | 59.5 | 0.003 | smolvla-tau045-long-s42 |

### smolvla / object

| τ | seed | SR (%) | trigger_rate | source_exp_id |
|---|------|--------|-------------|---------------|
| 0.05 | 42 | 75.0 | — | smolvla-tau005-object-s42 |
| 0.1 | 42 | 78.0 | — | smolvla-tau010-object-s42 |
| 0.15 | 42 | 78.0 | 0.167 | smolvla-tau015-object-s42 |
| 0.2 | 42 | 78.5 | — | smolvla-tau020-object-s42 |
| 0.25 | 42 | 78.0 | 0.034 | smolvla-tau025-object-s42-r2 |
| 0.25 | 43 | 77.5 | 0.037 | smolvla-tau025-object-s43-r3 |
| 0.3 | 42 | 79.0 | 0.0231 | smolvla-tau030-object-s42 |
| 0.35 | 42 | 75.0 | 0.016 | smolvla-tau035-object-s42-r2 |
| 0.35 | 43 | 77.0 | 0.013 | smolvla-tau035-object-s43-r3 |
| 0.4 | 42 | 73.5 | 0.0091 | smolvla-tau040-object-s42 |
| 0.45 | 42 | 71.5 | 0.0075 | smolvla-tau045-object-s42 |

### smolvla / spatial

| τ | seed | SR (%) | trigger_rate | source_exp_id |
|---|------|--------|-------------|---------------|
| 0.1 | 42 | 78.0 | 0.744 | eval-k2-tau010-spatial-s42-r3 |
| 0.15 | 42 | 80.0 | 0.412 | eval-k2-tau015-spatial-s42-r2 |
| 0.15 | 43 | 80.5 | 0.386 | smolvla-tau015-spatial-s43 |
| 0.2 | 42 | 81.0 | 0.267 | eval-k2-tau020-spatial-s42 |
| 0.25 | 43 | 79.5 | 0.193 | smolvla-tau025-spatial-s43 |
| 0.3 | 42 | 79.5 | 0.168 | eval-k2-tau030-spatial-s42 |
| 0.35 | 42 | 80.5 | 0.118 | eval-k2-tau035-spatial-s42-v2 |
| 0.35 | 43 | 79.5 | 0.127 | smolvla-tau035-spatial-s43 |
| 0.45 | 42 | 80.0 | 0.073 | smolvla-tau045-spatial-s42 |

## B. Supplementary Seeds (Mean ± Std)

**Total experiments: 65** (with valid SR values)

| benchmark | method | n_seeds | SR (mean ± std) |
|-----------|--------|---------|----------------|
| goal | adaptive_conformal_crm | 6 | 83.6 ± 1.9 |
| goal | crm_obs_only | 5 | 82.8 ± 1.8 |
| goal | reconvla | 2 | 81.2 ± 3.2 |
| goal | vla_only | 7 | 83.2 ± 1.4 |
| long | crm_obs_only | 1 | 54.0 |
| long | reconvla | 2 | 57.5 ± 2.1 |
| long | vla_only | 3 | 56.8 ± 2.4 |
| object | adaptive_conformal_crm | 1 | 81.0 |
| object | crm_obs_only | 1 | 79.5 |
| object | reconvla | 6 | 77.8 ± 1.5 |
| object | vla_only | 4 | 77.2 ± 2.3 |
| spatial | adaptive_conformal_crm | 8 | 80.4 ± 0.7 |
| spatial | crm_obs_only | 6 | 79.8 ± 1.2 |
| spatial | reconvla | 4 | 79.4 ± 0.9 |
| spatial | vla_only | 9 | 79.8 ± 0.9 |

### Detailed per-seed results

| benchmark | method | seed | SR (%) | source_exp_id |
|-----------|--------|------|--------|---------------|
| goal | adaptive_conformal_crm | 42 | 84.0 | eval-supp-goal-adapt-tau025-s42 |
| goal | adaptive_conformal_crm | 43 | 84.5 | eval-supp-adapt-tau025-goal-s43 |
| goal | adaptive_conformal_crm | 44 | 86.5 | eval-supp-adapt-tau025-goal-s44 |
| goal | adaptive_conformal_crm | 45 | 81.0 | eval-supp-goal-adapt-tau025-s45 |
| goal | adaptive_conformal_crm | 46 | 83.5 | eval-supp-goal-adapt-tau025-s46 |
| goal | adaptive_conformal_crm | 47 | 82.0 | eval-supp-goal-adapt-tau025-s47 |
| goal | crm_obs_only | 42 | 85.5 | eval-supp-goal-crm005-s42 |
| goal | crm_obs_only | 44 | 83.5 | eval-supp-crm-norm005-goal-s44 |
| goal | crm_obs_only | 45 | 81.0 | eval-supp-goal-crm-norm005-s45 |
| goal | crm_obs_only | 46 | 82.0 | eval-supp-goal-crm-norm005-s46 |
| goal | crm_obs_only | 47 | 82.0 | eval-supp-goal-crm-norm005-s47 |
| goal | reconvla | 46 | 79.0 | eval-supp-goal-reconvla-s46 |
| goal | reconvla | 47 | 83.5 | eval-supp-goal-reconvla-s47 |
| goal | vla_only | 42 | 85.5 | eval-supp-k2mean-goal-s42-r2 |
| goal | vla_only | 43 | 82.5 | eval-supp-goal-vla-only-wrapper-s43 |
| goal | vla_only | 44 | 82.0 | eval-supp-goal-vla-only-wrapper-s44 |
| goal | vla_only | 46 | 83.0 | eval-supp-goal-vla-only-s46 |
| goal | vla_only | 46 | 82.5 | eval-supp-goal-k2mean-s46 |
| goal | vla_only | 48 | 85.0 | eval-supp-vla-only-goal-s48 |
| goal | vla_only | 49 | 82.0 | eval-supp-vla-only-goal-s49 |
| long | crm_obs_only | 46 | 54.0 | eval-supp-long-crm-norm005-s46 |
| long | reconvla | 45 | 59.0 | eval-supp-long-reconvla-s45 |
| long | reconvla | 46 | 56.0 | eval-supp-long-reconvla-s46 |
| long | vla_only | 45 | 56.0 | eval-supp-long-k2mean-s45 |
| long | vla_only | 46 | 55.0 | eval-supp-long-k2mean-s46 |
| long | vla_only | 47 | 59.5 | eval-supp-long-vla-only-s47-r4 |
| object | adaptive_conformal_crm | 42 | 81.0 | eval-supp-obj-adapt-tau025-s42 |
| object | crm_obs_only | 46 | 79.5 | eval-supp-crm-obj-s46 |
| object | reconvla | 42 | 79.0 | eval-supp-obj-reconvla-s42 |
| object | reconvla | 43 | 77.0 | eval-supp-obj-reconvla-s43 |
| object | reconvla | 44 | 76.0 | eval-supp-obj-reconvla-s44 |
| object | reconvla | 45 | 78.0 | eval-supp-reconvla-obj-s45 |
| object | reconvla | 46 | 80.0 | eval-supp-reconvla-obj-s46 |
| object | reconvla | 47 | 76.5 | eval-supp-obj-reconvla-s47 |
| object | vla_only | 42 | 79.5 | eval-supp-k2mean-object-s42 |
| object | vla_only | 44 | 75.0 | eval-supp-k2mean-object-s44 |
| object | vla_only | 48 | 79.0 | eval-supp-vla-only-obj-s48 |
| object | vla_only | 49 | 75.5 | eval-supp-vla-only-obj-s49 |
| spatial | adaptive_conformal_crm | 42 | 80.5 | eval-supp-adapt-tau015-spatial-s42-r2 |
| spatial | adaptive_conformal_crm | 42 | 82.0 | eval-supp-adapt-tau025-spatial-s42-r2 |
| spatial | adaptive_conformal_crm | 42 | 80.0 | eval-supp-adapt-tau035-spatial-s42-r2 |
| spatial | adaptive_conformal_crm | 43 | 80.0 | eval-supp-adapt-tau025-spatial-s43 |
| spatial | adaptive_conformal_crm | 44 | 80.5 | eval-supp-adapt-tau025-spatial-s44 |
| spatial | adaptive_conformal_crm | 45 | 80.0 | eval-supp-spatial-adapt-tau025-s45-r3 |
| spatial | adaptive_conformal_crm | 45 | 80.0 | eval-supp-adapt-tau025-spatial-s45 |
| spatial | adaptive_conformal_crm | 46 | 80.0 | eval-supp-spatial-adapt-tau025-s46 |
| spatial | crm_obs_only | 42 | 79.0 | eval-supp-crm-norm02-spatial-s42-r2 |
| spatial | crm_obs_only | 43 | 81.0 | eval-supp-crm-norm005-spatial-s43 |
| spatial | crm_obs_only | 44 | 78.5 | eval-supp-crm-norm005-spatial-s44 |
| spatial | crm_obs_only | 45 | 80.5 | eval-supp-crm-norm005-spatial-s45 |
| spatial | crm_obs_only | 46 | 78.5 | eval-supp-crm-norm005-spatial-s46 |
| spatial | crm_obs_only | 46 | 81.0 | eval-supp-spatial-crm-norm005-s46 |
| spatial | reconvla | 42 | 80.0 | eval-supp-reconvla-k2-spatial-s42 |
| spatial | reconvla | 45 | 79.5 | eval-supp-spatial-reconvla-s45 |
| spatial | reconvla | 46 | 80.0 | eval-supp-spatial-reconvla-s46 |
| spatial | reconvla | 47 | 78.0 | eval-supp-spatial-reconvla-s47 |
| spatial | vla_only | 44 | 78.5 | eval-supp-spatial-vla-only-s44 |
| spatial | vla_only | 45 | 80.0 | eval-supp-vla-only-spatial-s45 |
| spatial | vla_only | 45 | 80.0 | eval-supp-spatial-k2mean-s45 |
| spatial | vla_only | 46 | 80.0 | eval-supp-spatial-k2mean-s46 |
| spatial | vla_only | 46 | 80.5 | eval-supp-vla-only-spatial-s46 |
| spatial | vla_only | 46 | 80.5 | eval-supp-spatial-vla-only-s46 |
| spatial | vla_only | 47 | 81.0 | eval-supp-spatial-vla-only-s47 |
| spatial | vla_only | 48 | 79.5 | eval-supp-vla-only-spatial-s48 |
| spatial | vla_only | 49 | 78.5 | eval-supp-vla-only-spatial-s49 |

## C. Pi05 Cross-VLA Generalization (Table 2)

**Total experiments: 33** (canonical, deduplicated)

### Summary (Mean ± Std)

| benchmark | mode | n | SR (mean ± std) |
|-----------|------|---|----------------|
| goal | adaptive_conformal_crm | 2 | 89.5 ± 0.0 |
| goal | crm_obs_only | 3 | 84.5 ± 1.3 |
| goal | vla_only | 3 | 97.5 ± 0.5 |
| long | adaptive_conformal_crm | 3 | 81.3 ± 1.4 |
| long | crm_obs_only | 1 | 76.0 |
| long | vla_only | 3 | 95.0 ± 0.9 |
| object | adaptive_conformal_crm | 3 | 86.2 ± 1.6 |
| object | crm_obs_only | 3 | 88.0 ± 1.0 |
| object | vla_only | 3 | 99.3 ± 0.8 |
| spatial | adaptive_conformal_crm | 3 | 97.2 ± 0.8 |
| spatial | crm_obs_only | 3 | 96.8 ± 0.3 |
| spatial | vla_only | 3 | 98.0 ± 0.5 |

### Per-seed detail

| benchmark | mode | seed | SR (%) | source_exp_id |
|-----------|------|------|--------|---------------|
| goal | adaptive_conformal_crm | 42 | 89.5 | pi05-adaptive-goal-s42-cqa1 |
| goal | adaptive_conformal_crm | 43 | 89.5 | pi05-adaptive-goal-s43-bjb1-18228 |
| goal | crm_obs_only | 42 | 85.5 | westd-pi05-crm-k2-goal-s42 |
| goal | crm_obs_only | 43 | 83.0 | pi05-crm-k2-goal-s43-bjb1-r2 |
| goal | crm_obs_only | 44 | 85.0 | pi05-crm-k2-goal-s44-bjb1-r2 |
| goal | vla_only | 42 | 98.0 | eval-pi05-vla-only-goal-s42-paired |
| goal | vla_only | 43 | 97.0 | eval-pi05-vla-only-goal-s43-v2 |
| goal | vla_only | 44 | 97.5 | eval-pi05-vla-only-goal-s44 |
| long | adaptive_conformal_crm | 42 | 80.5 | pi05-adaptive-long-s42-r2 |
| long | adaptive_conformal_crm | 43 | 80.5 | pi05-adaptive-long-s43-cqa1-r3 |
| long | adaptive_conformal_crm | 44 | 83.0 | pi05-adaptive-long-s44-cqa1-r3 |
| long | crm_obs_only | 44 | 76.0 | pi05-crm-k2-long-s44-cqa1 |
| long | vla_only | 42 | 94.0 | eval-pi05-vla-only-long-seed42-r4-rerun |
| long | vla_only | 43 | 95.5 | eval-pi05-vla-only-long-seed43-r4 |
| long | vla_only | 44 | 95.5 | eval-pi05-vla-only-long-seed44-r4 |
| object | adaptive_conformal_crm | 42 | 85.5 | pi05-adaptive-object-s42-cqa1 |
| object | adaptive_conformal_crm | 43 | 85.0 | pi05-adaptive-object-s43-cqa1-r3 |
| object | adaptive_conformal_crm | 44 | 88.0 | pi05-adaptive-object-s44-cqa1-r3 |
| object | crm_obs_only | 42 | 89.0 | pi05-crm-k2-object-s42-bjb1-r2 |
| object | crm_obs_only | 43 | 87.0 | pi05-crm-k2-object-s43-bjb1-r2 |
| object | crm_obs_only | 44 | 88.0 | pi05-crm-k2-object-s44-bjb1-r2 |
| object | vla_only | 42 | 100.0 | eval-pi05-vla-only-object-seed42-r4 |
| object | vla_only | 43 | 98.5 | eval-pi05-vla-only-object-seed43-r4 |
| object | vla_only | 44 | 99.5 | eval-pi05-vla-only-object-seed44-r4 |
| spatial | adaptive_conformal_crm | 42 | 96.5 | pi05-adaptive-spatial-s42-bjb2-r2 |
| spatial | adaptive_conformal_crm | 43 | 98.0 | pi05-adaptive-spatial-s43-bjb2-r2 |
| spatial | adaptive_conformal_crm | 44 | 97.0 | pi05-adaptive-spatial-s44-bjb2-r2 |
| spatial | crm_obs_only | 42 | 96.5 | pi05-crm-k2-spatial-s42-bjb2-r2 |
| spatial | crm_obs_only | 43 | 97.0 | pi05-crm-k2-spatial-s43-bjb2-r2 |
| spatial | crm_obs_only | 44 | 97.0 | pi05-crm-k2-spatial-s44-bjb2-r2 |
| spatial | vla_only | 42 | 98.0 | eval-pi05-vla-only-spatial-s42-paired |
| spatial | vla_only | 43 | 97.5 | westd-pi05-vla-only-spatial-s43-paired |
| spatial | vla_only | 44 | 98.5 | westd-pi05-vla-only-spatial-s44-paired |

## D. K-sweep Results

**Total experiments: 23** (22 with valid SR)

| model | benchmark | mode | seed | K | SR (%) | source_exp_id |
|-------|-----------|------|------|---|--------|---------------|
| — | object | — | — | 5 | 18.0 | eval-obs-only-object-norm02-k5-seed48 |
| smolvla | object | crm_obs_only | 42 | 5 | 73.5 | eval-ksweep-k5-obs-object-s42 |
| — | object | crm_obs_only | 42 | 5 | — | eval-obs-only-object-norm02-k5-seed42 |
| — | object | random_selection | 42 | 5 | 14.0 | eval-random-selection-object-k5-seed42-r2 |
| smolvla | object | crm_obs_only | 43 | 5 | 73.0 | eval-ksweep-k5-obs-object-s43 |
| — | object | crm_obs_only | 43 | 5 | 19.0 | eval-obs-only-object-norm02-k5-seed43 |
| — | object | random_selection | 43 | 5 | 11.0 | eval-random-selection-object-k5-seed43-r2 |
| — | object | crm_obs_only | 44 | 5 | 14.0 | eval-k5-obs-only-object-seed44 |
| — | object | crm_obs_only | 44 | 5 | 17.0 | eval-obs-only-object-norm02-k5-seed44 |
| — | object | random_selection | 44 | 5 | 10.0 | eval-random-selection-object-k5-seed44-r2 |
| — | object | crm_obs_only | 45 | 5 | 15.0 | eval-obs-only-object-norm02-k5-seed45 |
| — | object | random_selection | 45 | 5 | 7.0 | eval-random-selection-object-k5-seed45-r2 |
| — | object | crm_obs_only | 46 | 5 | 16.0 | eval-obs-only-object-norm02-k5-seed46 |
| — | object | crm_obs_only | 47 | 5 | 13.0 | eval-obs-only-object-norm02-k5-seed47 |
| smolvla | object | crm_obs_only | 44 | 10 | 78.0 | smolvla-crm-norm005-k10-object-s44-cqa1 |
| smolvla | object | crm_obs_only | 42 | 20 | 75.5 | eval-ksweep-k20-obs-object-s42 |
| smolvla | object | crm_obs_only | 43 | 20 | 73.5 | eval-ksweep-k20-obs-object-s43 |
| — | spatial | — | — | 5 | 35.0 | eval-obs-only-spatial-norm02-k5-seed42 |
| — | spatial | — | — | 5 | 32.0 | eval-obs-only-spatial-norm02-k5-seed43 |
| — | spatial | adaptive_conformal_crm | 42 | 5 | 79.0 | eval-k5-spatial-s42-sweep |
| — | spatial | crm_obs_only | 44 | 5 | 37.0 | eval-obs-only-spatial-norm02-k5-seed44-r2 |
| — | spatial | crm_obs_only | 45 | 5 | 34.0 | eval-obs-only-spatial-norm02-k5-seed45-r2 |
| — | spatial | crm_obs_only | 51 | 10 | 36.0 | eval-crm-spatial-k10-seed51 |

### K-sweep summary (SmolVLA, object, crm_obs_only)

| K | seeds | SR (mean ± std) |
|---|-------|----------------|
| 5 | 2 | 73.2 ± 0.4 |
| 10 | 1 | 78.0 |
| 20 | 2 | 74.5 ± 1.4 |

## E. CRM Always-On Ablation (τ=0.001)

**Total experiments: 23** (23 with valid SR)

### Summary (Mean ± Std)

| model | benchmark | n | SR (mean ± std) |
|-------|-----------|---|----------------|
| pi05 | goal | 1 | 81.5 |
| pi05 | long | 1 | 77.0 |
| pi05 | object | 2 | 91.2 ± 1.1 |
| pi05 | spatial | 1 | 96.0 |
| smolvla | goal | 5 | 80.4 ± 1.0 |
| smolvla | long | 3 | 43.2 ± 2.3 |
| smolvla | object | 5 | 72.2 ± 3.0 |
| smolvla | spatial | 5 | 77.9 ± 1.3 |

### Per-seed detail

| model | benchmark | seed | SR (%) | trigger_rate (%) | source_exp_id |
|-------|-----------|------|--------|-----------------|---------------|
| pi05 | goal | 42 | 81.5 | 100 | pi05-crm-always-on-goal-s42 |
| pi05 | long | 42 | 77.0 | 100 | pi05-crm-always-on-long-s42 |
| pi05 | object | 42 | 90.5 | 100 | pi05-crm-always-on-object-s42 |
| pi05 | object | 43 | 92.0 | 100 | pi05-crm-always-on-object-s43 |
| pi05 | spatial | 42 | 96.0 | 100 | pi05-crm-always-on-spatial-s42 |
| smolvla | goal | 42 | 80.0 | 100 | crm-always-on-goal-s42 |
| smolvla | goal | 43 | 79.5 | 100 | crm-always-on-goal-s43 |
| smolvla | goal | 44 | 80.5 | 100 | crm-always-on-goal-s44 |
| smolvla | goal | 45 | 82.0 | 100 | crm-always-on-goal-s45 |
| smolvla | goal | 46 | 80.0 | 100 | crm-always-on-goal-s46 |
| smolvla | long | 42 | 41.0 | 100 | crm-always-on-long-s42 |
| smolvla | long | 43 | 45.5 | 100 | crm-always-on-long-s43 |
| smolvla | long | 44 | 43.0 | 100 | crm-always-on-long-s44 |
| smolvla | object | 42 | 71.0 | 100 | crm-always-on-object-s42 |
| smolvla | object | 43 | 73.5 | 100 | crm-always-on-object-s43 |
| smolvla | object | 44 | 74.5 | 100 | crm-always-on-object-s44 |
| smolvla | object | 45 | 74.5 | 100 | crm-always-on-object-s45 |
| smolvla | object | 46 | 67.5 | 100 | crm-always-on-object-s46 |
| smolvla | spatial | 42 | 79.0 | 100 | crm-always-on-spatial-s42 |
| smolvla | spatial | 43 | 76.0 | 100 | crm-always-on-spatial-s43 |
| smolvla | spatial | 44 | 79.0 | 100 | crm-always-on-spatial-s44 |
| smolvla | spatial | 45 | 77.0 | 100 | crm-always-on-spatial-s45 |
| smolvla | spatial | 46 | 78.5 | 100 | crm-always-on-spatial-s46 |

## F. Data Gaps & Notes

### Incomplete categories
- **Bonus seeds / long / adaptive**: Only experiments with None SR (s42/s45/s46) — **incomplete**
- **Bonus seeds / object / adaptive**: Only 1 valid experiment (s42) — **incomplete**
- **Bonus seeds / object / crm_obs_only**: Only 1 valid experiment (s46) — **incomplete**
- **Bonus seeds / long / crm_obs_only**: Only 1 valid experiment (s46) — **incomplete**
- **Bonus seeds / goal / reconvla**: Only 2 valid experiments (s46, s47) — **incomplete**
- **Bonus seeds / long / reconvla**: Only 2 valid experiments (s45, s46) — **incomplete**
- **Pi05 / long / crm_obs_only**: Only 1 seed (s44) — **incomplete**
- **K-sweep**: Many experiments have None SR (especially K=20 and reconvla/argmin variants)
- **CRM always-on / smolvla / long**: s45 has None SR — **incomplete**

### Deduplication notes
- Multiple runs exist for same conditions (e.g., different servers, -r2/-r3 reruns). This summary uses the latest successful run with valid metrics.
- Pi05 vla_only experiments with SR=0% (e.g., seed42-r4 long, seed43/44 object) are excluded as known OOM artifacts.
- Trigger rates stored inconsistently: some as fractions (0.0–1.0), some as percentages (0–100). Values >1.0 in the tau-sweep are likely percentages.
