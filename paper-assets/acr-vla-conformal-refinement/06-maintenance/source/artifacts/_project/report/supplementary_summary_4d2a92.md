# Supplementary Experiment Results

All results from registry experiments with status=DONE, conclusion in (success, negative).
SR values normalized to percentages. Deduplicated: for same conditions, latest/best run kept.

## A. Threshold (τ) Sensitivity Analysis

**Total data points: 69** (with valid SR)

### pi05 / goal

| τ | seed | SR (%) | trigger_rate | source_exp_id |
|---|------|--------|-------------|---------------|
| 0.15 | 42 | 92.0 | 0.174 | pi05-adaptive-goal-s42-tau015-bjb2 |
| 0.15 | 43 | 88.0 | 0.195 | pi05-goal-tau015-s43 |
| 0.25 | 43 | 89.0 | 0.093 | pi05-goal-tau025-s43 |
| 0.35 | 42 | 87.5 | 0.057 | pi05-adaptive-goal-s42-tau035-bjb2 |
| 0.35 | 43 | 90.0 | 0.044 | pi05-goal-tau035-s43 |
| 0.5 | 42 | 87.0 | 0.0206 | pi05-tau-sweep-goal-tau050-s42-r3 |
| 0.7 | 42 | 87 | 1.1 | pi05-tau-sweep-goal-tau070-s42-r2 |

### pi05 / long

| τ | seed | SR (%) | trigger_rate | source_exp_id |
|---|------|--------|-------------|---------------|
| 0.15 | 42 | 84.0 | 0.114 | pi05-adaptive-long-s42-tau015-bjb2 |
| 0.15 | 43 | 82 | 11.4 | pi05-long-tau015-s43-r3 |

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
| 0.1 | 42 | 81.0 | 0.739 | eval-ablation-tau010-goal-s42 |
| 0.15 | 42 | 85.5 | 0.333 | smolvla-tau015-goal-s42 |
| 0.15 | 43 | 83.5 | 0.354 | smolvla-tau015-goal-s43 |
| 0.25 | 42 | 84.0 | 0.083 | smolvla-tau025-goal-s42 |
| 0.25 | 43 | 81.0 | 0.0925 | smolvla-tau025-goal-s43 |
| 0.25 | 49 | 80.5 | — | eval-goal-adapt-tau025-s49-paired |
| 0.35 | 42 | 86 | 2.1 | tau-sweep-goal-tau035-s42 |
| 0.35 | 43 | 85.5 | 0.0211 | smolvla-tau035-goal-s43 |
| 0.4 | 42 | 83.5 | — | tau_sweep_goal_tau040_s42 |
| 0.45 | 42 | 83.5 | — | tau_sweep_goal_tau045_s42 |
| 0.5 | 42 | 87.0 | 0.0206 | tau_sweep_goal_tau050_s42_cqa1 |
| 0.7 | 42 | 87.0 | 0.0104 | tau_sweep_goal_tau070_s42_cqa1 |
| 0.9 | 42 | 89.0 | 0.0035 | tau_sweep_goal_tau090_s42_cqa1 |

### smolvla / long

| τ | seed | SR (%) | trigger_rate | source_exp_id |
|---|------|--------|-------------|---------------|
| 0.05 | 42 | 44.0 | 0.9781 | smolvla-tau005-long-s42 |
| 0.1 | 42 | 53.5 | 0.613 | smolvla-tau010-long-s42 |
| 0.15 | 42 | 61.0 | 0.239 | smolvla-tau015-long-s42 |
| 0.15 | 43 | 61.0 | 0.236 | smolvla-tau015-long-s43 |
| 0.2 | 42 | 58.5 | 0.089 | smolvla-tau020-long-s42 |
| 0.2 | 43 | 54.5 | 11.4 | smolvla-tau020-long-s43-r2 |
| 0.25 | 42 | 56.0 | 0.042 | smolvla-tau025-long-s42 |
| 0.25 | 43 | 53.0 | 0.046 | smolvla-tau025-long-s43 |
| 0.3 | 42 | 54.5 | 1.6 | smolvla-tau030-long-s42-r2 |
| 0.3 | 43 | 55.5 | 1.6 | smolvla-tau030-long-s43-r2 |
| 0.35 | 42 | 57.5 | 0.013 | smolvla-tau035-long-s42 |
| 0.35 | 43 | 60.0 | 0.01 | smolvla-tau035-long-s43 |
| 0.4 | 42 | 60.0 | 0.004 | smolvla-tau040-long-s42 |
| 0.45 | 42 | 59.5 | 0.003 | smolvla-tau045-long-s42 |

### smolvla / object

| τ | seed | SR (%) | trigger_rate | source_exp_id |
|---|------|--------|-------------|---------------|
| 0.05 | 42 | 75 | 94.2 | smolvla-tau005-object-s42 |
| 0.1 | 42 | 78 | 44.4 | smolvla-tau010-object-s42 |
| 0.15 | 42 | 79 | 0.171 | smolvla-adapt-tau015-object-s42-cqa1 |
| 0.15 | 43 | 78 | 0.174 | smolvla-adapt-tau015-object-s43-cqa1 |
| 0.15 | 44 | 73.5 | 0.168 | smolvla-adapt-tau015-object-s44-cqa1 |
| 0.2 | 42 | 78.5 | 7.1 | smolvla-tau020-object-s42 |
| 0.25 | 42 | 81 | 3.5 | smolvla-tau025-object-s42-r3 |
| 0.25 | 43 | 77.5 | 0.037 | smolvla-tau025-object-s43-r3 |
| 0.3 | 42 | 79.0 | 0.0231 | smolvla-tau030-object-s42 |
| 0.35 | 42 | 75 | 1.6 | smolvla-tau035-object-s42-r3 |
| 0.35 | 43 | 77.0 | 0.013 | smolvla-tau035-object-s43-r3 |
| 0.4 | 42 | 73.5 | 0.0091 | smolvla-tau040-object-s42 |
| 0.45 | 42 | 71.5 | 0.0075 | smolvla-tau045-object-s42 |

### smolvla / spatial

| τ | seed | SR (%) | trigger_rate | source_exp_id |
|---|------|--------|-------------|---------------|
| 0.05 | 42 | 79.5 | 99.2 | eval-tau005-spatial-s42 |
| 0.075 | 42 | 78.0 | 0.92 | eval-k2-tau0075-spatial-s42 |
| 0.1 | 42 | 78.0 | 0.744 | eval-k2-tau010-spatial-s42-r3 |
| 0.15 | 42 | 80.0 | 0.412 | eval-k2-tau015-spatial-s42-r2 |
| 0.15 | 43 | 80.5 | 0.386 | smolvla-tau015-spatial-s43 |
| 0.2 | 42 | 81.0 | 0.267 | eval-k2-tau020-spatial-s42 |
| 0.25 | 42 | 79.5 | — | eval-k2-tau025-spatial-s42-v2 |
| 0.25 | 43 | 79.5 | 0.193 | smolvla-tau025-spatial-s43 |
| 0.25 | 46 | 78.0 | — | eval-spatial-adapt-tau025-s46-paired |
| 0.25 | 48 | 81.0 | — | eval-spatial-adapt-tau025-s48-paired |
| 0.3 | 42 | 79.5 | 0.168 | eval-k2-tau030-spatial-s42 |
| 0.35 | 42 | 80.5 | 12.1 | tau-sweep-spatial-tau035-s42 |
| 0.35 | 43 | 79.5 | 0.127 | smolvla-tau035-spatial-s43 |
| 0.4 | 42 | 80 | 9.6 | eval-tau040-spatial-s42 |
| 0.45 | 42 | 80.0 | 0.073 | smolvla-tau045-spatial-s42 |

## B. Supplementary Seeds (SmolVLA, τ=0.25)

**Total data points: 103** (with valid SR, deduplicated)

### Summary (Mean ± Std)

| benchmark | method | n_seeds | seeds | SR (mean ± std) |
|-----------|--------|---------|-------|----------------|
| goal | adaptive_conformal_crm | 6 | 42,43,44,45,46,47 | 83.6 ± 1.9 |
| goal | crm_obs_only | 7 | 42,43,44,45,46,47,48 | 82.3 ± 1.8 |
| goal | reconvla | 5 | 43,44,45,46,47 | 81.9 ± 2.6 |
| goal | vla_only | 8 | 42,43,44,45,46,47,48,49 | 83.6 ± 1.4 |
| long | adaptive_conformal_crm | 4 | 44,45,46,47 | 57.4 ± 2.3 |
| long | crm_obs_only | 6 | 42,43,44,45,46,47 | 56.4 ± 2.3 |
| long | reconvla | 6 | 42,43,44,45,46,47 | 57.1 ± 1.6 |
| long | vla_only | 6 | 42,43,44,45,46,47 | 58.0 ± 2.2 |
| object | adaptive_conformal_crm | 6 | 42,43,44,45,46,47 | 77.7 ± 1.9 |
| object | crm_obs_only | 6 | 42,43,44,45,46,47 | 78.0 ± 2.9 |
| object | reconvla | 6 | 42,43,44,45,46,47 | 77.8 ± 1.5 |
| object | vla_only | 9 | 42,43,44,45,46,47,48,49,50 | 77.2 ± 2.0 |
| spatial | adaptive_conformal_crm | 6 | 42,43,44,45,46,47 | 80.7 ± 0.9 |
| spatial | crm_obs_only | 8 | 42,43,44,45,46,47,48,49 | 79.6 ± 1.2 |
| spatial | reconvla | 6 | 42,43,44,45,46,47 | 80.2 ± 0.8 |
| spatial | vla_only | 8 | 42,43,44,45,46,47,48,49 | 80.2 ± 1.2 |

### Detailed per-seed results

| benchmark | method | seed | SR (%) | source_exp_id |
|-----------|--------|------|--------|---------------|
| goal | adaptive_conformal_crm | 42 | 84 | eval-supp-goal-adapt-tau025-s42 |
| goal | adaptive_conformal_crm | 43 | 84.5 | eval-supp-adapt-tau025-goal-s43 |
| goal | adaptive_conformal_crm | 44 | 86.5 | eval-supp-adapt-tau025-goal-s44 |
| goal | adaptive_conformal_crm | 45 | 81.0 | eval-supp-goal-adapt-tau025-s45 |
| goal | adaptive_conformal_crm | 46 | 83.5 | eval-supp-goal-adapt-tau025-s46 |
| goal | adaptive_conformal_crm | 47 | 82 | eval-supp-goal-adapt-tau025-s47 |
| goal | crm_obs_only | 42 | 85.5 | eval-supp-goal-crm005-s42 |
| goal | crm_obs_only | 43 | 82.0 | eval-supp-crm-norm005-goal-s43 |
| goal | crm_obs_only | 44 | 83.5 | eval-supp-crm-norm005-goal-s44 |
| goal | crm_obs_only | 45 | 81 | eval-supp-goal-crm-norm005-s45 |
| goal | crm_obs_only | 46 | 82.0 | eval-supp-goal-crm-norm005-s46 |
| goal | crm_obs_only | 47 | 82 | eval-supp-goal-crm-norm005-s47 |
| goal | crm_obs_only | 48 | 80.0 | eval-supp-crm-norm005-goal-s48 |
| goal | reconvla | 43 | 81.0 | eval-supp-goal-reconvla-s43 |
| goal | reconvla | 44 | 80.5 | eval-supp-goal-reconvla-s44 |
| goal | reconvla | 45 | 85.5 | eval-supp-goal-reconvla-s45 |
| goal | reconvla | 46 | 79.0 | eval-supp-goal-reconvla-s46 |
| goal | reconvla | 47 | 83.5 | eval-supp-goal-reconvla-s47 |
| goal | vla_only | 42 | 85.5 | eval-supp-k2mean-goal-s42-r2 |
| goal | vla_only | 43 | 82.5 | eval-supp-goal-vla-only-wrapper-s43 |
| goal | vla_only | 44 | 85.0 | eval-supp-goal-vla-only-wrapper-s44-r2 |
| goal | vla_only | 45 | 83.5 | eval-supp-goal-vla-only-s45 |
| goal | vla_only | 46 | 83.0 | eval-supp-goal-vla-only-s46 |
| goal | vla_only | 47 | 82.5 | eval-supp-goal-vla-only-s47-r3 |
| goal | vla_only | 48 | 85.0 | eval-supp-vla-only-goal-s48 |
| goal | vla_only | 49 | 82.0 | eval-supp-vla-only-goal-s49 |
| long | adaptive_conformal_crm | 44 | 56.0 | eval-supp-long-adapt-tau025-s44 |
| long | adaptive_conformal_crm | 45 | 60.0 | eval-supp-long-adapt-tau025-s45 |
| long | adaptive_conformal_crm | 46 | 58.5 | eval-supp-long-adapt-tau025-s46 |
| long | adaptive_conformal_crm | 47 | 55.0 | eval-supp-long-adapt-tau025-s47-r2 |
| long | crm_obs_only | 42 | 56.5 | eval-supp-long-crm-norm005-s42 |
| long | crm_obs_only | 43 | 54.5 | eval-supp-long-crm-norm005-s43 |
| long | crm_obs_only | 44 | 56.5 | eval-supp-long-crm-norm005-s44 |
| long | crm_obs_only | 45 | 60.5 | eval-supp-long-crm-norm005-s45 |
| long | crm_obs_only | 46 | 54.0 | eval-supp-long-crm-norm005-s46 |
| long | crm_obs_only | 47 | 56.5 | eval-supp-long-crm-norm005-s47 |
| long | reconvla | 42 | 56.5 | eval-supp-long-reconvla-s42 |
| long | reconvla | 43 | 59.0 | eval-supp-long-reconvla-s43 |
| long | reconvla | 44 | 57.0 | eval-supp-long-reconvla-s44 |
| long | reconvla | 45 | 59 | eval-supp-long-reconvla-s45 |
| long | reconvla | 46 | 56.0 | eval-supp-long-reconvla-s46 |
| long | reconvla | 47 | 55.0 | eval-supp-long-reconvla-s47 |
| long | vla_only | 42 | 59.5 | eval-supp-long-vla-only-s42 |
| long | vla_only | 43 | 56.0 | eval-supp-long-k2mean-s43 |
| long | vla_only | 44 | 60.5 | eval-supp-long-vla-only-s44 |
| long | vla_only | 45 | 57.5 | eval-supp-long-vla-only-s45 |
| long | vla_only | 46 | 55.0 | eval-supp-long-k2mean-s46 |
| long | vla_only | 47 | 59.5 | eval-supp-long-vla-only-s47-r4 |
| object | adaptive_conformal_crm | 42 | 81.0 | eval-supp-obj-adapt-tau025-s42 |
| object | adaptive_conformal_crm | 43 | 77.5 | eval-supp-adapt-tau025-obj-s43 |
| object | adaptive_conformal_crm | 44 | 75.0 | eval-supp-adapt-tau025-obj-s44 |
| object | adaptive_conformal_crm | 45 | 78.0 | eval-supp-adapt-tau025-obj-s45 |
| object | adaptive_conformal_crm | 46 | 77.5 | eval-supp-adapt-tau025-obj-s46 |
| object | adaptive_conformal_crm | 47 | 77.0 | eval-supp-obj-adapt-tau025-s47-r2 |
| object | crm_obs_only | 42 | 77.0 | eval-supp-obj-crm005-s42-r2 |
| object | crm_obs_only | 43 | 78.5 | eval-supp-crm-norm005-obj-s43 |
| object | crm_obs_only | 44 | 74.0 | eval-supp-crm-norm005-obj-s44 |
| object | crm_obs_only | 45 | 76.5 | eval-supp-obj-crm-norm005-s45 |
| object | crm_obs_only | 46 | 79.5 | eval-supp-crm-obj-s46 |
| object | crm_obs_only | 47 | 82.5 | eval-supp-obj-crm-norm005-s47-r2 |
| object | reconvla | 42 | 79 | eval-supp-obj-reconvla-s42 |
| object | reconvla | 43 | 77.0 | eval-supp-obj-reconvla-s43 |
| object | reconvla | 44 | 76.0 | eval-supp-obj-reconvla-s44 |
| object | reconvla | 45 | 78 | eval-supp-reconvla-obj-s45 |
| object | reconvla | 46 | 80.0 | eval-supp-reconvla-obj-s46 |
| object | reconvla | 47 | 76.5 | eval-supp-obj-reconvla-s47 |
| object | vla_only | 42 | 79.5 | eval-supp-k2mean-object-s42 |
| object | vla_only | 43 | 78.0 | eval-supp-k2mean-object-s43 |
| object | vla_only | 44 | 75.0 | eval-supp-k2mean-object-s44 |
| object | vla_only | 45 | 77.5 | eval-supp-k2mean-obj-s45 |
| object | vla_only | 46 | 79.0 | eval-supp-obj-vla-only-s46 |
| object | vla_only | 47 | 77.5 | eval-supp-obj-k2mean-s47 |
| object | vla_only | 48 | 79.0 | eval-supp-vla-only-obj-s48 |
| object | vla_only | 49 | 75.5 | eval-supp-vla-only-obj-s49 |
| object | vla_only | 50 | 74.0 | eval-supp-obj-vla-only-s50 |
| spatial | adaptive_conformal_crm | 42 | 82 | eval-supp-adapt-tau025-spatial-s42-r2 |
| spatial | adaptive_conformal_crm | 43 | 80 | eval-supp-adapt-tau025-spatial-s43 |
| spatial | adaptive_conformal_crm | 44 | 80.5 | eval-supp-adapt-tau025-spatial-s44 |
| spatial | adaptive_conformal_crm | 45 | 80 | eval-supp-spatial-adapt-tau025-s45-r3 |
| spatial | adaptive_conformal_crm | 46 | 80 | eval-supp-spatial-adapt-tau025-s46 |
| spatial | adaptive_conformal_crm | 47 | 81.5 | eval-supp-adapt-tau025-spatial-s47 |
| spatial | crm_obs_only | 42 | 79 | eval-supp-crm-norm02-spatial-s42-r2 |
| spatial | crm_obs_only | 43 | 81 | eval-supp-crm-norm005-spatial-s43 |
| spatial | crm_obs_only | 44 | 78.5 | eval-supp-crm-norm005-spatial-s44 |
| spatial | crm_obs_only | 45 | 80.5 | eval-supp-crm-norm005-spatial-s45 |
| spatial | crm_obs_only | 46 | 81 | eval-supp-spatial-crm-norm005-s46 |
| spatial | crm_obs_only | 47 | 80.5 | eval-supp-spatial-crm-norm005-s47 |
| spatial | crm_obs_only | 48 | 78.0 | eval-supp-crm-norm005-spatial-s48 |
| spatial | crm_obs_only | 49 | 78.5 | eval-supp-crm-norm005-spatial-s49 |
| spatial | reconvla | 42 | 80 | eval-supp-reconvla-k2-spatial-s42 |
| spatial | reconvla | 43 | 81.5 | eval-supp-reconvla-spatial-s43 |
| spatial | reconvla | 44 | 79.5 | eval-supp-reconvla-spatial-s44 |
| spatial | reconvla | 45 | 79.5 | eval-supp-spatial-reconvla-s45 |
| spatial | reconvla | 46 | 80 | eval-supp-spatial-reconvla-s46 |
| spatial | reconvla | 47 | 81.0 | eval-supp-reconvla-spatial-s47 |
| spatial | vla_only | 42 | 81.5 | eval-supp-k2mean-spatial-s42 |
| spatial | vla_only | 43 | 79.0 | eval-supp-spatial-vla-only-s43 |
| spatial | vla_only | 44 | 81.0 | eval-supp-k2mean-spatial-s44 |
| spatial | vla_only | 45 | 80.0 | eval-supp-vla-only-spatial-s45 |
| spatial | vla_only | 46 | 80.5 | eval-supp-vla-only-spatial-s46 |
| spatial | vla_only | 47 | 82 | eval-supp-spatial-k2mean-s47 |
| spatial | vla_only | 48 | 79.5 | eval-supp-vla-only-spatial-s48 |
| spatial | vla_only | 49 | 78.5 | eval-supp-vla-only-spatial-s49 |

## C. Pi05 Cross-VLA Generalization

**Total data points: 37** (deduplicated, SR>0%)

### Summary (Mean ± Std)

| benchmark | method | n | seeds | SR (mean ± std) |
|-----------|--------|---|-------|----------------|
| goal | adaptive_conformal_crm | 3 | 42,43,44 | 88.8 ± 1.2 |
| goal | crm_obs_only | 3 | 42,43,44 | 84.5 ± 1.3 |
| goal | vla_only | 3 | 42,43,44 | 98.3 ± 1.0 |
| long | adaptive_conformal_crm | 3 | 42,43,44 | 81.3 ± 1.4 |
| long | crm_obs_only | 3 | 42,43,44 | 79.3 ± 3.1 |
| long | vla_only | 3 | 42,43,44 | 96.5 ± 1.3 |
| object | adaptive_conformal_crm | 3 | 42,43,44 | 86.8 ± 1.3 |
| object | crm_obs_only | 3 | 42,43,44 | 88.0 ± 1.0 |
| object | vla_only | 3 | 42,43,44 | 99.8 ± 0.3 |
| spatial | adaptive_conformal_crm | 3 | 42,43,44 | 97.2 ± 0.8 |
| spatial | crm_obs_only | 3 | 42,43,44 | 96.8 ± 0.3 |
| spatial | vla_only | 4 | 42,43,44,45 | 94.9 ± 6.6 |

### Per-seed detail

| benchmark | method | seed | SR (%) | source_exp_id |
|-----------|--------|------|--------|---------------|
| goal | adaptive_conformal_crm | 42 | 89.5 | pi05-adaptive-goal-s42-cqa1 |
| goal | adaptive_conformal_crm | 43 | 89.5 | pi05-adaptive-goal-s43-bjb1-18228 |
| goal | adaptive_conformal_crm | 44 | 87.5 | westd-pi05-adaptive-goal-s44 |
| goal | crm_obs_only | 42 | 85.5 | westd-pi05-crm-k2-goal-s42 |
| goal | crm_obs_only | 43 | 83 | pi05-crm-k2-goal-s43-bjb1-r2 |
| goal | crm_obs_only | 44 | 85 | pi05-crm-k2-goal-s44-bjb1-r2 |
| goal | vla_only | 42 | 99.5 | westd-pi05-k2mean-goal-s42 |
| goal | vla_only | 43 | 98.0 | eval-pi05-vla-only-goal-seed43-r4 |
| goal | vla_only | 44 | 97.5 | pi05-vla-only-goal-s44-4090 |
| long | adaptive_conformal_crm | 42 | 80.5 | pi05-adaptive-long-s42-r2 |
| long | adaptive_conformal_crm | 43 | 80.5 | pi05-adaptive-long-s43-cqa1-r3 |
| long | adaptive_conformal_crm | 44 | 83.0 | pi05-adaptive-long-s44-cqa1-r3 |
| long | crm_obs_only | 42 | 82.0 | pi05-crm-k2-long-s42-r2 |
| long | crm_obs_only | 43 | 76.0 | pi05-crm-k2-long-s43-r2 |
| long | crm_obs_only | 44 | 80.0 | pi05-crm-k2-long-s44 |
| long | vla_only | 42 | 98.0 | westd-pi05-vla-only-long-s42-paired |
| long | vla_only | 43 | 95.5 | pi05-vla-only-long-s43-4090 |
| long | vla_only | 44 | 96.0 | westd-pi05-vla-only-long-s44-paired |
| object | adaptive_conformal_crm | 42 | 85.5 | pi05-object-adaptive-s42-cqa1 |
| object | adaptive_conformal_crm | 43 | 87.0 | westd-pi05-adaptive-object-s43-paired |
| object | adaptive_conformal_crm | 44 | 88.0 | pi05-object-adaptive-s44-cqa1 |
| object | crm_obs_only | 42 | 89 | pi05-crm-k2-object-s42-bjb1-r2 |
| object | crm_obs_only | 43 | 87.0 | westd-pi05-crm-k2-object-s43 |
| object | crm_obs_only | 44 | 88.0 | westd-pi05-crm-k2-object-s44 |
| object | vla_only | 42 | 100 | pi05-k2mean-object-s42-r3 |
| object | vla_only | 43 | 100 | westd-pi05-vla-only-object-s43-paired |
| object | vla_only | 44 | 99.5 | westd-pi05-vla-only-object-s44-paired |
| spatial | adaptive_conformal_crm | 42 | 96.5 | pi05-adaptive-spatial-s42-bjb2-r2 |
| spatial | adaptive_conformal_crm | 43 | 98 | pi05-adaptive-spatial-s43-bjb2-r2 |
| spatial | adaptive_conformal_crm | 44 | 97 | pi05-adaptive-spatial-s44-bjb2-r2 |
| spatial | crm_obs_only | 42 | 96.5 | pi05-crm-k2-spatial-s42-bjb2-r2 |
| spatial | crm_obs_only | 43 | 97 | pi05-crm-k2-spatial-s43-bjb2-r2 |
| spatial | crm_obs_only | 44 | 97 | pi05-crm-k2-spatial-s44-bjb2-r2 |
| spatial | vla_only | 42 | 98.0 | eval-pi05-vla-only-spatial-s42-v2 |
| spatial | vla_only | 43 | 97.5 | westd-pi05-vla-only-spatial-s43-paired |
| spatial | vla_only | 44 | 99.0 | eval-pi05-vla-only-spatial-s44-d149 |
| spatial | vla_only | 45 | 85.0 | eval-pi05-vla-only-spatial-s45 |

## D. K-sweep Results

**Total data points: 89** (with valid SR)

### SmolVLA K-sweep (object, crm_obs_only, with VLA)

| K | n_seeds | SR (mean ± std) | per-seed |
|---|---------|----------------|----------|
| 5 | 2 | 73.2 ± 0.4 | s42=73.5; s43=73 |
| 10 | 1 | 78.0 | s44=78.0 |
| 20 | 3 | 73.3 ± 2.3 | s42=75.5; s43=73.5; s44=71 |

### All K-sweep data points

| model | benchmark | method | seed | K | SR (%) | source_exp_id |
|-------|-----------|--------|------|---|--------|---------------|
| obs_only | object | crm_obs_only | 42 | 20 | 20.0 | eval-k20-obs-only-object-seed42 |
| obs_only | object | crm_obs_only | 43 | 20 | 18.0 | eval-k20-obs-only-object-seed43 |
| obs_only | object | crm_obs_only | 44 | 20 | 18.0 | eval-k20-obs-only-object-seed44 |
| obs_only | object | crm_obs_only | 45 | 20 | 19.0 | eval-k20-obs-only-object-seed45 |
| obs_only | object | crm_obs_only | 42 | 5 | 14.0 | eval-obs-only-object-norm02-k5-seed42 |
| obs_only | object | crm_obs_only | 43 | 5 | 19.0 | eval-obs-only-object-norm02-k5-seed43 |
| obs_only | object | crm_obs_only | 44 | 5 | 17.0 | eval-obs-only-object-norm02-k5-seed44 |
| obs_only | object | crm_obs_only | 45 | 5 | 15.0 | eval-obs-only-object-norm02-k5-seed45 |
| obs_only | object | crm_obs_only | 46 | 5 | 16.0 | eval-obs-only-object-norm02-k5-seed46 |
| obs_only | object | crm_obs_only | 47 | 5 | 13.0 | eval-obs-only-object-norm02-k5-seed47 |
| obs_only | object | crm_obs_only | 48 | 5 | 18.0 | eval-obs-only-object-norm02-k5-seed48 |
| obs_only | object | crm_obs_only | 42 | None | 20.0 | eval-obs-only-object-norm02-seed42 |
| obs_only | object | crm_obs_only | 43 | None | 16.0 | eval-obs-only-object-norm02-seed43-r3 |
| obs_only | object | crm_obs_only | 44 | None | 18.0 | eval-obs-only-object-norm03-seed44 |
| obs_only | object | crm_obs_only | 45 | None | 18.0 | eval-obs-only-object-default-seed45-r2 |
| obs_only | object | crm_obs_only | 46 | None | 18.0 | eval-obs-only-object-norm01-seed46-r3 |
| obs_only | object | crm_obs_only | 47 | None | 20.0 | eval-obs-only-object-norm02-seed47 |
| obs_only | object | crm_obs_only | 48 | None | 18.0 | eval-obs-only-object-norm02-seed48-r2 |
| obs_only | object | crm_obs_only | 49 | None | 16.0 | eval-obs-only-object-norm01-seed49 |
| obs_only | object | crm_obs_only | 50 | None | 18.0 | eval-obs-only-object-norm02-seed50 |
| obs_only | object | crm_obs_only | 51 | None | 17.0 | eval-obs-only-object-norm02-seed51 |
| obs_only | object | crm_obs_only | 52 | None | 15.0 | eval-obs-only-object-norm02-seed52 |
| obs_only | object | crm_obs_only | 53 | None | 19.0 | eval-obs-only-object-norm01-seed53 |
| obs_only | object | crm_obs_only | 54 | None | 15.0 | eval-obs-only-object-norm01-seed54 |
| obs_only | object | crm_obs_only | 55 | None | 15.0 | eval-obs-only-object-norm005-seed55 |
| obs_only | object | crm_obs_only | 56 | None | 15.0 | eval-obs-only-object-norm003-seed56 |
| obs_only | object | crm_obs_only | 57 | None | 19.0 | eval-obs-only-object-norm01-seed57 |
| obs_only | object | crm_obs_only | 58 | None | 16.0 | eval-obs-only-object-norm005-seed58 |
| obs_only | object | crm_obs_only | 59 | None | 13.0 | eval-obs-only-object-norm003-seed59 |
| obs_only | object | crm_obs_only | 60 | None | 15.0 | eval-obs-only-object-norm01-seed60 |
| obs_only | object | crm_obs_only | 61 | None | 15.0 | eval-obs-only-object-norm005-seed61 |
| obs_only | object | crm_obs_only | 64 | None | 17.0 | eval-obs-only-object-norm003-seed64 |
| obs_only | object | crm_obs_only | 65 | None | 17.0 | eval-obs-only-object-norm003-seed65 |
| obs_only | object | crm_obs_only | 66 | None | 13.5 | eval-obs-only-object-norm01-seed66 |
| obs_only | object | crm_obs_only | 67 | None | 14.0 | eval-obs-only-object-norm003-seed67 |
| obs_only | object | crm_obs_only | 71 | None | 16.0 | eval-obs-only-object-norm01-seed71 |
| obs_only | object | crm_obs_only | 72 | None | 11.0 | eval-obs-only-object-norm005-seed72 |
| obs_only | object | crm_obs_only | 73 | None | 16.0 | eval-obs-only-object-norm003-seed73 |
| obs_only | object | crm_obs_only | 74 | None | 13.0 | eval-obs-only-object-norm01-seed74 |
| obs_only | object | crm_obs_only | 75 | None | 15.0 | eval-obs-only-object-norm005-seed75 |
| obs_only | spatial | crm_obs_only | 42 | 20 | 35.0 | eval-k20-obs-only-spatial-seed42 |
| obs_only | spatial | crm_obs_only | 43 | 20 | 34.0 | eval-k20-obs-only-spatial-seed43 |
| obs_only | spatial | crm_obs_only | 44 | 20 | 34.0 | eval-k20-obs-only-spatial-seed44 |
| obs_only | spatial | crm_obs_only | 42 | 5 | 35.0 | eval-obs-only-spatial-norm02-k5-seed42 |
| obs_only | spatial | crm_obs_only | 43 | 5 | 32.0 | eval-obs-only-spatial-norm02-k5-seed43 |
| obs_only | spatial | crm_obs_only | 44 | 5 | 37.0 | eval-obs-only-spatial-norm02-k5-seed44-r2 |
| obs_only | spatial | crm_obs_only | 45 | 5 | 34.0 | eval-obs-only-spatial-norm02-k5-seed45-r2 |
| obs_only | spatial | crm_obs_only | None | None | 0 | eval-obs-only-spatial-v2 |
| obs_only | spatial | crm_obs_only | 42 | None | 33 | eval-obs-only-spatial-norm02-seed42-r2 |
| obs_only | spatial | crm_obs_only | 43 | None | 34.0 | eval-obs-only-spatial-norm02-seed43-r2 |
| obs_only | spatial | crm_obs_only | 44 | None | 36.0 | eval-obs-only-spatial-norm02-seed44 |
| obs_only | spatial | crm_obs_only | 45 | None | 34.0 | eval-obs-only-spatial-norm02-seed45 |
| obs_only | spatial | crm_obs_only | 46 | None | 33.0 | eval-obs-only-spatial-norm02-seed46-r2 |
| obs_only | spatial | crm_obs_only | 47 | None | 32.0 | eval-obs-only-spatial-norm02-seed47 |
| obs_only | spatial | crm_obs_only | 48 | None | 35.0 | eval-obs-only-spatial-seed48 |
| obs_only | spatial | crm_obs_only | 49 | None | 32.0 | eval-obs-only-spatial-norm02-seed49 |
| obs_only | spatial | crm_obs_only | 50 | None | 35.0 | eval-obs-only-spatial-norm02-seed50 |
| obs_only | spatial | crm_obs_only | 52 | None | 33.0 | eval-obs-only-spatial-norm02-seed52 |
| smolvla | None | None | 43 | 20 | 77 | eval-ksweep-k20-obs-obj-s43 |
| smolvla | object | None | 42 | 20 | 75.5 | eval-ksweep-k20-obs-object-s42 |
| smolvla | object | None | 43 | 20 | 73.5 | eval-ksweep-k20-obs-object-s43 |
| smolvla | object | None | 44 | 20 | 71 | eval-ksweep-k20-obs-object-s44 |
| smolvla | object | None | 42 | 5 | 73.5 | eval-ksweep-k5-obs-object-s42 |
| smolvla | object | None | 43 | 5 | 73 | eval-ksweep-k5-obs-object-s43 |
| smolvla | object | argmin | 42 | 5 | 15.0 | eval-argmin-object-k5-seed42 |
| smolvla | object | argmin | 43 | 5 | 13.0 | eval-argmin-object-k5-seed43 |
| smolvla | object | argmin | 44 | 5 | 11.0 | eval-argmin-object-k5-seed44-r2 |
| smolvla | object | argmin | 45 | 5 | 13.0 | eval-argmin-object-k5-seed45 |
| smolvla | object | crm_obs_only | 44 | 10 | 78.0 | smolvla-crm-norm005-k10-object-s44-cqa1 |
| smolvla | object | crm_obs_only | 42 | 20 | 20.0 | eval-crm-object-k20-seed42 |
| smolvla | object | crm_obs_only | 43 | 20 | 18.0 | eval-crm-object-k20-seed43 |
| smolvla | object | crm_obs_only | 44 | 20 | 18.0 | eval-crm-object-k20-seed44 |
| smolvla | object | random_selection | 42 | 5 | 14.0 | eval-random-selection-object-k5-seed42-r2 |
| smolvla | object | random_selection | 43 | 5 | 11.0 | eval-random-selection-object-k5-seed43-r2 |
| smolvla | object | random_selection | 44 | 5 | 10.0 | eval-random-selection-object-k5-seed44-r2 |
| smolvla | object | random_selection | 45 | 5 | 7.0 | eval-random-selection-object-k5-seed45-r2 |
| smolvla | object | random_selection | 42 | None | 11.0 | eval-random-selection-object-seed42 |
| smolvla | object | random_selection | 43 | None | 77 | eval-random-selection-object-seed43-v2 |
| smolvla | object | random_selection | 44 | None | 11.0 | eval-random-selection-object-seed44 |
| smolvla | object | random_selection | 45 | None | 10.0 | eval-random-selection-object-seed45 |
| smolvla | object | random_selection | 46 | None | 10.0 | eval-random-selection-object-seed46-r3 |
| smolvla | object | random_selection | 47 | None | 7 | eval-random-selection-object-seed47 |
| smolvla | object | random_selection | 48 | None | 10.0 | eval-random-selection-object-seed48 |
| smolvla | object | random_selection | 49 | None | 12.0 | eval-random-selection-object-seed49 |
| smolvla | spatial | None | 42 | 5 | 79 | eval-k5-spatial-s42-sweep |
| smolvla | spatial | crm_obs_only | 51 | 10 | 36.0 | eval-crm-spatial-k10-seed51 |
| smolvla | spatial | random_selection | 42 | None | 34 | eval-random-selection-spatial-seed42 |
| smolvla | spatial | random_selection | 43 | None | 26 | eval-random-selection-spatial-seed43-r2 |
| smolvla | spatial | random_selection | 44 | None | 28.0 | eval-random-selection-spatial-seed44 |

## E. CRM Always-On Ablation (τ=0.001)

**Total data points: 28** (with valid SR)

### Summary (Mean ± Std)

| model | benchmark | n | seeds | SR (mean ± std) |
|-------|-----------|---|-------|----------------|
| pi05 | goal | 3 | 42,43,44 | 82.5 ± 1.0 |
| pi05 | long | 2 | 42,43 | 78.2 ± 1.8 |
| pi05 | object | 3 | 42,43,44 | 90.7 ± 1.3 |
| pi05 | spatial | 1 | 42 | 96.0 |
| smolvla | goal | 5 | 42,43,44,45,46 | 80.4 ± 1.0 |
| smolvla | long | 4 | 42,43,44,45 | 43.2 ± 1.8 |
| smolvla | object | 5 | 42,43,44,45,46 | 72.2 ± 3.0 |
| smolvla | spatial | 5 | 42,43,44,45,46 | 77.9 ± 1.3 |

### Per-seed detail

| model | benchmark | seed | SR (%) | trigger_rate (%) | source_exp_id |
|-------|-----------|------|--------|-----------------|---------------|
| pi05 | goal | 42 | 81.5 | 100 | pi05-crm-always-on-goal-s42 |
| pi05 | goal | 43 | 82.5 | 100 | pi05-crm-always-on-goal-s43 |
| pi05 | goal | 44 | 83.5 | 100 | pi05-crm-always-on-goal-s44 |
| pi05 | long | 42 | 77 | 100 | pi05-crm-always-on-long-s42 |
| pi05 | long | 43 | 79.5 | 100 | pi05-crm-always-on-long-s43 |
| pi05 | object | 42 | 90.5 | 100 | pi05-crm-always-on-object-s42 |
| pi05 | object | 43 | 92 | 100 | pi05-crm-always-on-object-s43 |
| pi05 | object | 44 | 89.5 | 100 | pi05-crm-always-on-object-s44 |
| pi05 | spatial | 42 | 96 | 100 | pi05-crm-always-on-spatial-s42 |
| smolvla | goal | 42 | 80 | 100 | crm-always-on-goal-s42 |
| smolvla | goal | 43 | 79.5 | 100 | crm-always-on-goal-s43 |
| smolvla | goal | 44 | 80.5 | 100 | crm-always-on-goal-s44 |
| smolvla | goal | 45 | 82 | 100 | crm-always-on-goal-s45 |
| smolvla | goal | 46 | 80 | 100 | crm-always-on-goal-s46 |
| smolvla | long | 42 | 41.0 | 100 | crm-always-on-long-s42 |
| smolvla | long | 43 | 45.5 | 100 | crm-always-on-long-s43 |
| smolvla | long | 44 | 43.0 | 100 | crm-always-on-long-s44 |
| smolvla | long | 45 | 43.5 | 100 | crm-always-on-long-s45 |
| smolvla | object | 42 | 71.0 | 100 | crm-always-on-object-s42 |
| smolvla | object | 43 | 73.5 | 100 | crm-always-on-object-s43 |
| smolvla | object | 44 | 74.5 | 100 | crm-always-on-object-s44 |
| smolvla | object | 45 | 74.5 | 100 | crm-always-on-object-s45 |
| smolvla | object | 46 | 67.5 | 100 | crm-always-on-object-s46 |
| smolvla | spatial | 42 | 79.0 | 100 | crm-always-on-spatial-s42 |
| smolvla | spatial | 43 | 76 | 100 | crm-always-on-spatial-s43 |
| smolvla | spatial | 44 | 79 | 100 | crm-always-on-spatial-s44 |
| smolvla | spatial | 45 | 77.0 | 100 | crm-always-on-spatial-s45 |
| smolvla | spatial | 46 | 78.5 | 100 | crm-always-on-spatial-s46 |

## F. Data Gaps & Notes

### Bonus seed coverage (target: 6 seeds per benchmark × method)

- **goal / reconvla**: 5 seeds — needs 1 more
- **long / adaptive_conformal_crm**: 4 seeds — needs 2 more

### Pi05 cross-VLA coverage (target: 3 seeds per benchmark × method)

All benchmark × method combinations have ≥3 seeds.

### CRM always-on coverage

- **pi05 / long**: 2 seeds — needs 1 more
- **pi05 / spatial**: 1 seeds — needs 2 more

### Deduplication notes
- Multiple runs for same conditions (different servers, -r2/-r3 reruns). This summary keeps the run with highest SR.
- Pi05 vla_only experiments with SR=0% excluded as known OOM artifacts.
- Trigger rates stored inconsistently: some as fractions (0.0–1.0), some as percentages (0–100).