# Registry Data Mining Report
**Generated**: 2026-05-30 | **Total registry experiments**: 1423 | **Valid records (after filtering & dedup)**: 113

## Filtering Criteria

- **Conclusion**: `success` or `negative` (both are valid data)
- **Metrics**: Must have non-zero SR
- **VLA-only**: `mode=vla_only`, no K/tau requirements
- **CRM always-on**: `mode=adaptive_conformal_crm` with `tau≤0.01, K=2` OR `mode=crm_obs_only` with `K=2`
- **Adaptive**: `mode=adaptive_conformal_crm` with `tau=0.25, K=2`
- **Excluded**: ablations (K≠2 for CRM modes, tau≠0.25 for adaptive), k2mean, dry runs, old eval pipeline (SR<0.5 for SmolVLA Object/Spatial/Goal), OpenVLA, LTO-split
- **Deduplication**: When multiple runs exist for same (model, suite, condition, seed), kept latest run with trigger_rate data preferred

## 1. Raw Data Table

| # | Experiment ID | Model | Suite | Condition | Seed | SR | Trigger Rate | Conclusion |
|---|---|---|---|---|---|---|---|---|
| 1 | `pi05-adaptive-goal-s42-cqa1` | pi05 | goal | adaptive | 42 | 0.8950 | 0.0810 | success |
| 2 | `pi05-goal-tau025-s43-r3` | pi05 | goal | adaptive | 43 | 0.8850 | 0.0910 | success |
| 3 | `pi05-adaptive-goal-s44-backfill` | pi05 | goal | adaptive | 44 | 0.8650 | 0.1000 | success |
| 4 | `pi05-crm-always-on-goal-s42` | pi05 | goal | crm-always-on | 42 | 0.8150 | — | success |
| 5 | `pi05-crm-always-on-goal-s43` | pi05 | goal | crm-always-on | 43 | 0.8250 | — | success |
| 6 | `pi05-crm-always-on-goal-s44` | pi05 | goal | crm-always-on | 44 | 0.8350 | — | success |
| 7 | `eval-pi05-vla-only-goal-seed42-r4` | pi05 | goal | vla-only | 42 | 0.9800 | — | success |
| 8 | `eval-pi05-vla-only-goal-seed43-r4` | pi05 | goal | vla-only | 43 | 0.9800 | — | success |
| 9 | `eval-pi05-vla-only-goal-seed44-r4` | pi05 | goal | vla-only | 44 | 0.9750 | — | success |
| 10 | `pi05-adaptive-long-s42-r2` | pi05 | long | adaptive | 42 | 0.8050 | 0.0390 | success |
| 11 | `pi05-adaptive-long-s43-cqa1-r3` | pi05 | long | adaptive | 43 | 0.8050 | 0.0530 | success |
| 12 | `pi05-adaptive-long-s44-bjb1` | pi05 | long | adaptive | 44 | 0.8200 | 0.0440 | success |
| 13 | `pi05-crm-always-on-long-s42` | pi05 | long | crm-always-on | 42 | 0.7700 | 1.0000 | success |
| 14 | `pi05-crm-k2-long-s43-r2` | pi05 | long | crm-always-on | 43 | 0.7600 | — | negative |
| 15 | `pi05-crm-k2-long-s44-cqa1` | pi05 | long | crm-always-on | 44 | 0.7600 | — | success |
| 16 | `eval-pi05-vla-only-long-seed42-r4-rerun` | pi05 | long | vla-only | 42 | 0.9400 | — | success |
| 17 | `eval-pi05-vla-only-long-seed43-r4` | pi05 | long | vla-only | 43 | 0.9550 | — | success |
| 18 | `eval-pi05-vla-only-long-seed44-r4` | pi05 | long | vla-only | 44 | 0.9550 | — | success |
| 19 | `westd-pi05-adaptive-object-s42-paired` | pi05 | object | adaptive | 42 | 0.8350 | 0.0346 | negative |
| 20 | `westd-pi05-adaptive-object-s43-paired` | pi05 | object | adaptive | 43 | 0.8700 | 0.0383 | negative |
| 21 | `pi05-adaptive-object-s44-cqa1-r3` | pi05 | object | adaptive | 44 | 0.8800 | 0.0348 | success |
| 22 | `pi05-crm-always-on-object-s42` | pi05 | object | crm-always-on | 42 | 0.9050 | 1.0000 | success |
| 23 | `pi05-crm-always-on-object-s43` | pi05 | object | crm-always-on | 43 | 0.9200 | 1.0000 | success |
| 24 | `pi05-crm-always-on-object-s44` | pi05 | object | crm-always-on | 44 | 0.8950 | — | success |
| 25 | `eval-pi05-vla-only-object-seed42-r4` | pi05 | object | vla-only | 42 | 1.0000 | — | success |
| 26 | `eval-pi05-vla-only-object-s43-r5` | pi05 | object | vla-only | 43 | 0.9850 | — | success |
| 27 | `eval-pi05-vla-only-object-seed44-r4` | pi05 | object | vla-only | 44 | 0.9950 | — | success |
| 28 | `pi05-adaptive-spatial-s42-bjb2-r2` | pi05 | spatial | adaptive | 42 | 0.9650 | 0.0480 | success |
| 29 | `pi05-spatial-tau025-s43` | pi05 | spatial | adaptive | 43 | 0.9850 | 0.0280 | success |
| 30 | `pi05-adaptive-spatial-s44-bjb2-r2` | pi05 | spatial | adaptive | 44 | 0.9700 | 0.0390 | success |
| 31 | `pi05-crm-always-on-spatial-s42` | pi05 | spatial | crm-always-on | 42 | 0.9600 | 1.0000 | success |
| 32 | `pi05-crm-k2-spatial-s43-bjb2-r2` | pi05 | spatial | crm-always-on | 43 | 0.9700 | — | success |
| 33 | `pi05-crm-k2-spatial-s44-bjb2-r2` | pi05 | spatial | crm-always-on | 44 | 0.9700 | — | success |
| 34 | `eval-pi05-vla-only-spatial-s42-v2` | pi05 | spatial | vla-only | 42 | 0.9800 | — | success |
| 35 | `eval-pi05-vla-only-spatial-s43-r2` | pi05 | spatial | vla-only | 43 | 0.9750 | — | success |
| 36 | `westd-pi05-vla-only-spatial-s44-paired` | pi05 | spatial | vla-only | 44 | 0.9850 | — | success |
| 37 | `eval-pi05-vla-only-spatial-s45` | pi05 | spatial | vla-only | 45 | 0.8500 | — | success |
| 38 | `smolvla-tau025-goal-s42` | smolvla | goal | adaptive | 42 | 0.8400 | 0.0830 | success |
| 39 | `eval-adaptive-goal-s43-d149` | smolvla | goal | adaptive | 43 | 0.8450 | 0.0880 | success |
| 40 | `eval-adaptive-goal-s44-d149` | smolvla | goal | adaptive | 44 | 0.8650 | 0.0680 | success |
| 41 | `eval-k2-goal-adapt-s45-paired` | smolvla | goal | adaptive | 45 | 0.8200 | 0.0940 | success |
| 42 | `eval-k2-goal-adapt-s46-paired` | smolvla | goal | adaptive | 46 | 0.8400 | 0.0880 | success |
| 43 | `eval-k2-goal-adapt-s47-paired` | smolvla | goal | adaptive | 47 | 0.8250 | 0.0980 | success |
| 44 | `goal_adapt_s48` | smolvla | goal | adaptive | 48 | 0.8500 | — | success |
| 45 | `eval-goal-adapt-tau025-s49-paired` | smolvla | goal | adaptive | 49 | 0.8050 | — | negative |
| 46 | `crm-always-on-goal-s42` | smolvla | goal | crm-always-on | 42 | 0.8000 | 1.0000 | success |
| 47 | `crm-always-on-goal-s43` | smolvla | goal | crm-always-on | 43 | 0.7950 | 1.0000 | success |
| 48 | `crm-always-on-goal-s44` | smolvla | goal | crm-always-on | 44 | 0.8050 | 1.0000 | success |
| 49 | `crm-always-on-goal-s45` | smolvla | goal | crm-always-on | 45 | 0.8200 | 1.0000 | success |
| 50 | `crm-always-on-goal-s46` | smolvla | goal | crm-always-on | 46 | 0.8000 | 1.0000 | success |
| 51 | `eval-goal-vla-only-wrapper-s42` | smolvla | goal | vla-only | 42 | 0.8350 | — | success |
| 52 | `eval-supp-goal-vla-only-wrapper-s43` | smolvla | goal | vla-only | 43 | 0.8250 | — | success |
| 53 | `eval-supp-goal-vla-only-wrapper-s44-r2` | smolvla | goal | vla-only | 44 | 0.8500 | — | success |
| 54 | `eval-k2-goal-vla-only-s45-paired` | smolvla | goal | vla-only | 45 | 0.8350 | — | success |
| 55 | `eval-k2-goal-vla-only-s46-paired` | smolvla | goal | vla-only | 46 | 0.8200 | — | success |
| 56 | `eval-supp-goal-vla-only-s47-r3` | smolvla | goal | vla-only | 47 | 0.8250 | — | success |
| 57 | `goal_vla_only_s48` | smolvla | goal | vla-only | 48 | 0.7950 | — | success |
| 58 | `eval-goal-vla-only-s49-paired` | smolvla | goal | vla-only | 49 | 0.8350 | — | success |
| 59 | `eval-supp-long-adapt-tau025-s42` | smolvla | long | adaptive | 42 | 0.5900 | 0.0390 | success |
| 60 | `eval-supp-long-adapt-tau025-s43` | smolvla | long | adaptive | 43 | 0.5800 | 0.0450 | negative |
| 61 | `eval-supp-long-adapt-tau025-s44` | smolvla | long | adaptive | 44 | 0.5600 | 0.0490 | negative |
| 62 | `eval-supp-long-adapt-tau025-s45` | smolvla | long | adaptive | 45 | 0.6000 | — | success |
| 63 | `eval-supp-long-adapt-tau025-s46` | smolvla | long | adaptive | 46 | 0.5850 | — | success |
| 64 | `eval-supp-long-adapt-tau025-s47-r2` | smolvla | long | adaptive | 47 | 0.5500 | 0.0370 | negative |
| 65 | `crm-always-on-long-s42` | smolvla | long | crm-always-on | 42 | 0.4100 | 1.0000 | success |
| 66 | `crm-always-on-long-s43` | smolvla | long | crm-always-on | 43 | 0.4550 | 1.0000 | success |
| 67 | `crm-always-on-long-s44` | smolvla | long | crm-always-on | 44 | 0.4300 | 1.0000 | success |
| 68 | `crm-always-on-long-s45` | smolvla | long | crm-always-on | 45 | 0.4350 | 1.0000 | success |
| 69 | `eval-supp-long-vla-only-s42` | smolvla | long | vla-only | 42 | 0.5950 | — | success |
| 70 | `smolvla-vla-only-long-n20-s43` | smolvla | long | vla-only | 43 | 0.5750 | — | success |
| 71 | `eval-supp-long-vla-only-s44` | smolvla | long | vla-only | 44 | 0.6050 | — | success |
| 72 | `eval-supp-long-vla-only-s45` | smolvla | long | vla-only | 45 | 0.5750 | — | success |
| 73 | `eval-supp-long-vla-only-s47-r4` | smolvla | long | vla-only | 47 | 0.5950 | — | success |
| 74 | `smolvla-tau025-object-s42-r3` | smolvla | object | adaptive | 42 | 0.8100 | 0.0350 | success |
| 75 | `smolvla-tau025-object-s43-r3` | smolvla | object | adaptive | 43 | 0.7750 | 0.0370 | success |
| 76 | `eval-adaptive-object-s44-d149` | smolvla | object | adaptive | 44 | 0.7500 | 0.0360 | success |
| 77 | `eval-supp-adapt-tau025-obj-s45` | smolvla | object | adaptive | 45 | 0.7800 | — | success |
| 78 | `eval-supp-adapt-tau025-obj-s46` | smolvla | object | adaptive | 46 | 0.7750 | — | success |
| 79 | `eval-supp-obj-adapt-tau025-s47-r2` | smolvla | object | adaptive | 47 | 0.7700 | 0.0403 | success |
| 80 | `crm-always-on-object-s42` | smolvla | object | crm-always-on | 42 | 0.7100 | 1.0000 | success |
| 81 | `crm-always-on-object-s43` | smolvla | object | crm-always-on | 43 | 0.7350 | 1.0000 | success |
| 82 | `crm-always-on-object-s44` | smolvla | object | crm-always-on | 44 | 0.7450 | 1.0000 | success |
| 83 | `crm-always-on-object-s45` | smolvla | object | crm-always-on | 45 | 0.7450 | 1.0000 | success |
| 84 | `crm-always-on-object-s46` | smolvla | object | crm-always-on | 46 | 0.6750 | 1.0000 | success |
| 85 | `eval-object-vla-only-wrapper-s42-r2` | smolvla | object | vla-only | 42 | 0.7900 | — | success |
| 86 | `eval-object-vla-only-wrapper-s43-r2` | smolvla | object | vla-only | 43 | 0.7700 | — | success |
| 87 | `eval-object-vla-only-wrapper-s44-r2` | smolvla | object | vla-only | 44 | 0.7750 | — | success |
| 88 | `eval-supp-obj-vla-only-s45` | smolvla | object | vla-only | 45 | 0.7600 | — | success |
| 89 | `eval-supp-obj-vla-only-s46` | smolvla | object | vla-only | 46 | 0.7900 | — | success |
| 90 | `eval-supp-obj-vla-only-s47-r2` | smolvla | object | vla-only | 47 | 0.7550 | — | success |
| 91 | `eval-supp-vla-only-obj-s48` | smolvla | object | vla-only | 48 | 0.7900 | — | success |
| 92 | `eval-supp-vla-only-obj-s49` | smolvla | object | vla-only | 49 | 0.7550 | — | success |
| 93 | `eval-supp-obj-vla-only-s50` | smolvla | object | vla-only | 50 | 0.7400 | — | success |
| 94 | `eval-k2-spatial-adapt-s42-paired-r2` | smolvla | spatial | adaptive | 42 | 0.7950 | 0.1980 | success |
| 95 | `eval-k2-spatial-adapt-s43-paired-r2` | smolvla | spatial | adaptive | 43 | 0.7950 | 0.2030 | success |
| 96 | `eval-k2-spatial-adapt-s44-paired-r2` | smolvla | spatial | adaptive | 44 | 0.8050 | 0.1950 | success |
| 97 | `eval-supp-spatial-adapt-tau025-s45-r3` | smolvla | spatial | adaptive | 45 | 0.8000 | 0.2000 | success |
| 98 | `eval-supp-spatial-adapt-tau025-s46` | smolvla | spatial | adaptive | 46 | 0.8000 | 0.1990 | success |
| 99 | `eval-supp-spatial-adapt-tau025-s47` | smolvla | spatial | adaptive | 47 | 0.7950 | 0.2100 | success |
| 100 | `eval-spatial-adapt-tau025-s48-paired` | smolvla | spatial | adaptive | 48 | 0.8100 | — | success |
| 101 | `crm-always-on-spatial-s42` | smolvla | spatial | crm-always-on | 42 | 0.7900 | 1.0000 | success |
| 102 | `crm-always-on-spatial-s43` | smolvla | spatial | crm-always-on | 43 | 0.7600 | 1.0000 | success |
| 103 | `crm-always-on-spatial-s44` | smolvla | spatial | crm-always-on | 44 | 0.7900 | 1.0000 | success |
| 104 | `crm-always-on-spatial-s45` | smolvla | spatial | crm-always-on | 45 | 0.7700 | 1.0000 | success |
| 105 | `crm-always-on-spatial-s46` | smolvla | spatial | crm-always-on | 46 | 0.7850 | 1.0000 | success |
| 106 | `eval-k2-spatial-vla-only-s42-paired-r2` | smolvla | spatial | vla-only | 42 | 0.7850 | — | success |
| 107 | `eval-k2-spatial-vla-only-s43-paired-r2` | smolvla | spatial | vla-only | 43 | 0.7950 | — | success |
| 108 | `eval-k2-spatial-vla-only-s44-paired-r2` | smolvla | spatial | vla-only | 44 | 0.8000 | — | success |
| 109 | `eval-supp-vla-only-spatial-s45` | smolvla | spatial | vla-only | 45 | 0.8000 | — | success |
| 110 | `eval-spatial-vla-only-s46-paired` | smolvla | spatial | vla-only | 46 | 0.8000 | — | success |
| 111 | `eval-supp-spatial-vla-only-s47` | smolvla | spatial | vla-only | 47 | 0.8100 | — | success |
| 112 | `eval-spatial-vla-only-s48-paired` | smolvla | spatial | vla-only | 48 | 0.7750 | — | success |
| 113 | `eval-vla-only-spatial-bjb1-s49` | smolvla | spatial | vla-only | 49 | 0.7950 | — | success |

## 2. Summary Table (Mean ± Std)

| Model | Suite | Condition | N | Mean SR | Std SR | Min SR | Max SR | Mean TR | Std TR |
|---|---|---|---|---|---|---|---|---|---|
| pi05 | goal | adaptive | 3 | 0.8817 | 0.0153 | 0.8650 | 0.8950 | 0.0907 | 0.0095 |
| pi05 | goal | crm-always-on | 3 | 0.8250 | 0.0100 | 0.8150 | 0.8350 | — | — |
| pi05 | goal | vla-only | 3 | 0.9783 | 0.0029 | 0.9750 | 0.9800 | — | — |
| pi05 | long | adaptive | 3 | 0.8100 | 0.0087 | 0.8050 | 0.8200 | 0.0453 | 0.0071 |
| pi05 | long | crm-always-on | 3 | 0.7633 | 0.0058 | 0.7600 | 0.7700 | 1.0000 | — |
| pi05 | long | vla-only | 3 | 0.9500 | 0.0087 | 0.9400 | 0.9550 | — | — |
| pi05 | object | adaptive | 3 | 0.8617 | 0.0236 | 0.8350 | 0.8800 | 0.0359 | 0.0021 |
| pi05 | object | crm-always-on | 3 | 0.9067 | 0.0126 | 0.8950 | 0.9200 | 1.0000 | 0.0000 |
| pi05 | object | vla-only | 3 | 0.9933 | 0.0076 | 0.9850 | 1.0000 | — | — |
| pi05 | spatial | adaptive | 3 | 0.9733 | 0.0104 | 0.9650 | 0.9850 | 0.0383 | 0.0100 |
| pi05 | spatial | crm-always-on | 3 | 0.9667 | 0.0058 | 0.9600 | 0.9700 | 1.0000 | — |
| pi05 | spatial | vla-only | 4 | 0.9475 | 0.0651 | 0.8500 | 0.9850 | — | — |
| smolvla | goal | adaptive | 8 | 0.8363 | 0.0189 | 0.8050 | 0.8650 | 0.0865 | 0.0105 |
| smolvla | goal | crm-always-on | 5 | 0.8040 | 0.0096 | 0.7950 | 0.8200 | 1.0000 | 0.0000 |
| smolvla | goal | vla-only | 8 | 0.8275 | 0.0160 | 0.7950 | 0.8500 | — | — |
| smolvla | long | adaptive | 6 | 0.5775 | 0.0189 | 0.5500 | 0.6000 | 0.0425 | 0.0055 |
| smolvla | long | crm-always-on | 4 | 0.4325 | 0.0185 | 0.4100 | 0.4550 | 1.0000 | 0.0000 |
| smolvla | long | vla-only | 5 | 0.5890 | 0.0134 | 0.5750 | 0.6050 | — | — |
| smolvla | object | adaptive | 6 | 0.7767 | 0.0194 | 0.7500 | 0.8100 | 0.0371 | 0.0023 |
| smolvla | object | crm-always-on | 5 | 0.7220 | 0.0299 | 0.6750 | 0.7450 | 1.0000 | 0.0000 |
| smolvla | object | vla-only | 9 | 0.7694 | 0.0183 | 0.7400 | 0.7900 | — | — |
| smolvla | spatial | adaptive | 7 | 0.8000 | 0.0058 | 0.7950 | 0.8100 | 0.2008 | 0.0052 |
| smolvla | spatial | crm-always-on | 5 | 0.7790 | 0.0134 | 0.7600 | 0.7900 | 1.0000 | 0.0000 |
| smolvla | spatial | vla-only | 8 | 0.7950 | 0.0107 | 0.7750 | 0.8100 | — | — |

## 3. Effect Size Analysis Per Suite

### SMOLVLA

#### Object

| Comparison | Δ (mean diff) | Cohen's d | 95% CI | t-stat | p-value | n₁ | n₂ |
|---|---|---|---|---|---|---|---|
| CRM-always-on vs VLA-only | -0.0474 | -2.079 | [-0.0752, -0.0197] | -3.227 | 0.0193 | 5 | 9 |
| Adaptive vs VLA-only | +0.0072 | 0.386 | [-0.0141, 0.0285] | 0.723 | 0.4859 | 6 | 9 |
| Adaptive vs CRM-always-on | +0.0547 | 2.219 | [0.0209, 0.0884] | 3.516 | 0.0107 | 6 | 5 |

#### Spatial

| Comparison | Δ (mean diff) | Cohen's d | 95% CI | t-stat | p-value | n₁ | n₂ |
|---|---|---|---|---|---|---|---|
| CRM-always-on vs VLA-only | -0.0160 | -1.361 | [-0.0307, -0.0013] | -2.256 | 0.0578 | 5 | 8 |
| Adaptive vs VLA-only | +0.0050 | 0.570 | [-0.0048, 0.0148] | 1.146 | 0.2762 | 7 | 8 |
| Adaptive vs CRM-always-on | +0.0210 | 2.189 | [0.0085, 0.0335] | 3.289 | 0.0213 | 7 | 5 |

#### Goal

| Comparison | Δ (mean diff) | Cohen's d | 95% CI | t-stat | p-value | n₁ | n₂ |
|---|---|---|---|---|---|---|---|
| CRM-always-on vs VLA-only | -0.0235 | -1.673 | [-0.0411, -0.0059] | -3.302 | 0.0071 | 5 | 8 |
| Adaptive vs VLA-only | +0.0088 | 0.500 | [-0.0100, 0.0275] | 1.000 | 0.3347 | 8 | 8 |
| Adaptive vs CRM-always-on | +0.0323 | 2.001 | [0.0120, 0.0525] | 4.066 | 0.0019 | 8 | 5 |

#### Long

| Comparison | Δ (mean diff) | Cohen's d | 95% CI | t-stat | p-value | n₁ | n₂ |
|---|---|---|---|---|---|---|---|
| CRM-always-on vs VLA-only | -0.1565 | -9.912 | [-0.1815, -0.1315] | -14.203 | 1.88e-05 | 4 | 5 |
| Adaptive vs VLA-only | -0.0115 | -0.689 | [-0.0344, 0.0114] | -1.176 | 0.2702 | 6 | 5 |
| Adaptive vs CRM-always-on | +0.1450 | 7.733 | [0.1171, 0.1729] | 12.042 | 8.82e-06 | 6 | 4 |

**Degradation severity ranking (smolvla)**: 
long (-0.1565) > object (-0.0474) > goal (-0.0235) > spatial (-0.0160)

### PI05

#### Object

| Comparison | Δ (mean diff) | Cohen's d | 95% CI | t-stat | p-value | n₁ | n₂ |
|---|---|---|---|---|---|---|---|
| CRM-always-on vs VLA-only | -0.0867 | -8.327 | [-0.1103, -0.0631] | -10.198 | 0.0013 | 3 | 3 |
| Adaptive vs VLA-only | -0.1317 | -7.498 | [-0.1715, -0.0919] | -9.184 | 0.0062 | 3 | 3 |
| Adaptive vs CRM-always-on | -0.0450 | -2.377 | [-0.0879, -0.0021] | -2.911 | 0.0607 | 3 | 3 |

#### Spatial

| Comparison | Δ (mean diff) | Cohen's d | 95% CI | t-stat | p-value | n₁ | n₂ |
|---|---|---|---|---|---|---|---|
| CRM-always-on vs VLA-only | +0.0192 | 0.379 | [-0.0801, 0.1185] | 0.586 | 0.5986 | 3 | 4 |
| Adaptive vs VLA-only | +0.0258 | 0.508 | [-0.0741, 0.1257] | 0.780 | 0.4889 | 3 | 4 |
| Adaptive vs CRM-always-on | +0.0067 | 0.792 | [-0.0124, 0.0257] | 0.970 | 0.4009 | 3 | 3 |

#### Goal

| Comparison | Δ (mean diff) | Cohen's d | 95% CI | t-stat | p-value | n₁ | n₂ |
|---|---|---|---|---|---|---|---|
| CRM-always-on vs VLA-only | -0.1533 | -20.834 | [-0.1700, -0.1366] | -25.516 | 6.61e-04 | 3 | 3 |
| Adaptive vs VLA-only | -0.0967 | -8.794 | [-0.1216, -0.0717] | -10.770 | 0.0067 | 3 | 3 |
| Adaptive vs CRM-always-on | +0.0567 | 4.389 | [0.0274, 0.0859] | 5.376 | 0.0087 | 3 | 3 |

#### Long

| Comparison | Δ (mean diff) | Cohen's d | 95% CI | t-stat | p-value | n₁ | n₂ |
|---|---|---|---|---|---|---|---|
| CRM-always-on vs VLA-only | -0.1867 | -25.363 | [-0.2034, -0.1700] | -31.063 | 2.20e-05 | 3 | 3 |
| Adaptive vs VLA-only | -0.1400 | -16.166 | [-0.1596, -0.1204] | -19.799 | 3.84e-05 | 3 | 3 |
| Adaptive vs CRM-always-on | +0.0467 | 6.341 | [0.0300, 0.0634] | 7.766 | 0.0026 | 3 | 3 |

**Degradation severity ranking (pi05)**: 
long (-0.1867) > goal (-0.1533) > object (-0.0867) > spatial (+0.0192)

## 4. Trigger Rate Analysis

### SMOLVLA Trigger Rate Distribution

| Suite | Condition | N (with TR) | Mean TR | Std TR | Min TR | Max TR |
|---|---|---|---|---|---|---|
| object | crm-always-on | 5 | 1.0000 | 0.0000 | 1.0000 | 1.0000 |
| object | adaptive | 4 | 0.0371 | 0.0023 | 0.0350 | 0.0403 |
| spatial | crm-always-on | 5 | 1.0000 | 0.0000 | 1.0000 | 1.0000 |
| spatial | adaptive | 6 | 0.2008 | 0.0052 | 0.1950 | 0.2100 |
| goal | crm-always-on | 5 | 1.0000 | 0.0000 | 1.0000 | 1.0000 |
| goal | adaptive | 6 | 0.0865 | 0.0105 | 0.0680 | 0.0980 |
| long | crm-always-on | 4 | 1.0000 | 0.0000 | 1.0000 | 1.0000 |
| long | adaptive | 4 | 0.0425 | 0.0055 | 0.0370 | 0.0490 |

### SMOLVLA Trigger Rate × SR Correlation (Adaptive only)

| Suite | N | Mean TR | Pearson r | Pearson p | Spearman ρ | Spearman p |
|---|---|---|---|---|---|---|
| goal | 6 | 0.0865 | -0.9321 | 0.0068 | -0.8088 | 0.0513 |
| long | 4 | 0.0425 | 0.0000 | 1.0000 | 0.2000 | 0.8000 |
| object | 4 | 0.0371 | -0.3593 | 0.6407 | -0.4000 | 0.6000 |
| spatial | 6 | 0.2008 | -0.6761 | 0.1404 | -0.6172 | 0.1917 |

### PI05 Trigger Rate Distribution

| Suite | Condition | N (with TR) | Mean TR | Std TR | Min TR | Max TR |
|---|---|---|---|---|---|---|
| object | crm-always-on | 2 | 1.0000 | 0.0000 | 1.0000 | 1.0000 |
| object | adaptive | 3 | 0.0359 | 0.0021 | 0.0346 | 0.0383 |
| spatial | crm-always-on | 1 | 1.0000 | 0.0000 | 1.0000 | 1.0000 |
| spatial | adaptive | 3 | 0.0383 | 0.0100 | 0.0280 | 0.0480 |
| goal | adaptive | 3 | 0.0907 | 0.0095 | 0.0810 | 0.1000 |
| long | crm-always-on | 1 | 1.0000 | 0.0000 | 1.0000 | 1.0000 |
| long | adaptive | 3 | 0.0453 | 0.0071 | 0.0390 | 0.0530 |

### PI05 Trigger Rate × SR Correlation (Adaptive only)

| Suite | N | Mean TR | Pearson r | Pearson p | Spearman ρ | Spearman p |
|---|---|---|---|---|---|---|
| goal | 3 | 0.0907 | -0.9758 | 0.1404 | -1.0000 | 0.0000 |
| long | 3 | 0.0453 | -0.1628 | 0.8959 | 0.0000 | 1.0000 |
| object | 3 | 0.0359 | 0.3508 | 0.7718 | 0.5000 | 0.6667 |
| spatial | 3 | 0.0383 | -0.9752 | 0.1422 | -1.0000 | 0.0000 |

## 5. Cross-Seed Variance Analysis

### SMOLVLA

#### Object

| Comparison | Var₁ | Var₂ | F-ratio | Levene stat | Levene p |
|---|---|---|---|---|---|
| vla-only vs crm-always-on | 0.000334 | 0.000895 | 0.373 | 0.484 | 0.4999 |
| vla-only vs adaptive | 0.000334 | 0.000377 | 0.887 | 0.300 | 0.5932 |
| crm-always-on vs adaptive | 0.000895 | 0.000377 | 2.376 | 0.647 | 0.4418 |

#### Spatial

| Comparison | Var₁ | Var₂ | F-ratio | Levene stat | Levene p |
|---|---|---|---|---|---|
| vla-only vs crm-always-on | 0.000114 | 0.000180 | 0.635 | 0.264 | 0.6173 |
| vla-only vs adaptive | 0.000114 | 0.000033 | 3.429 | 1.064 | 0.3212 |
| crm-always-on vs adaptive | 0.000180 | 0.000033 | 5.400 | 2.020 | 0.1856 |

#### Goal

| Comparison | Var₁ | Var₂ | F-ratio | Levene stat | Levene p |
|---|---|---|---|---|---|
| vla-only vs crm-always-on | 0.000257 | 0.000092 | 2.780 | 0.842 | 0.3784 |
| vla-only vs adaptive | 0.000257 | 0.000355 | 0.724 | 0.182 | 0.6763 |
| crm-always-on vs adaptive | 0.000092 | 0.000355 | 0.260 | 1.498 | 0.2466 |

#### Long

| Comparison | Var₁ | Var₂ | F-ratio | Levene stat | Levene p |
|---|---|---|---|---|---|
| vla-only vs crm-always-on | 0.000180 | 0.000342 | 0.527 | 0.122 | 0.7376 |
| vla-only vs adaptive | 0.000180 | 0.000357 | 0.503 | 0.376 | 0.5549 |
| crm-always-on vs adaptive | 0.000342 | 0.000357 | 0.956 | 0.047 | 0.8337 |

### PI05

#### Object

| Comparison | Var₁ | Var₂ | F-ratio | Levene stat | Levene p |
|---|---|---|---|---|---|
| vla-only vs crm-always-on | 0.000058 | 0.000158 | 0.368 | 0.400 | 0.5614 |
| vla-only vs adaptive | 0.000058 | 0.000558 | 0.104 | 0.857 | 0.4069 |
| crm-always-on vs adaptive | 0.000158 | 0.000558 | 0.284 | 0.348 | 0.5870 |

#### Spatial

| Comparison | Var₁ | Var₂ | F-ratio | Levene stat | Levene p |
|---|---|---|---|---|---|
| vla-only vs crm-always-on | 0.004242 | 0.000033 | 127.250 | 0.748 | 0.4267 |
| vla-only vs adaptive | 0.004242 | 0.000108 | 39.154 | 0.596 | 0.4749 |
| crm-always-on vs adaptive | 0.000033 | 0.000108 | 0.308 | 0.364 | 0.5790 |

#### Goal

| Comparison | Var₁ | Var₂ | F-ratio | Levene stat | Levene p |
|---|---|---|---|---|---|
| vla-only vs crm-always-on | 0.000008 | 0.000100 | 0.083 | 1.800 | 0.2508 |
| vla-only vs adaptive | 0.000008 | 0.000233 | 0.036 | 1.923 | 0.2378 |
| crm-always-on vs adaptive | 0.000100 | 0.000233 | 0.429 | 0.250 | 0.6433 |

#### Long

| Comparison | Var₁ | Var₂ | F-ratio | Levene stat | Levene p |
|---|---|---|---|---|---|
| vla-only vs crm-always-on | 0.000075 | 0.000033 | 2.250 | 0.077 | 0.7953 |
| vla-only vs adaptive | 0.000075 | 0.000075 | 1.000 | 0.000 | 1.0000 |
| crm-always-on vs adaptive | 0.000033 | 0.000075 | 0.444 | 0.077 | 0.7953 |

## 6. Key Findings Summary

1. **SMOLVLA CRM always-on degradation**: Average Δ = -0.0609. Worst: long (-0.1565). Best: spatial (-0.0160).
2. **PI05 CRM always-on degradation**: Average Δ = -0.1019. Worst: long (-0.1867). Best: spatial (+0.0192).
3. **SMOLVLA Adaptive vs VLA-only**: Average Δ = +0.0024. Positive in: object, spatial, goal. Negative in: long.
4. **PI05 Adaptive vs VLA-only**: Average Δ = -0.0856. Positive in: spatial. Negative in: object, goal, long.
5. **SMOLVLA Trigger rates (adaptive)**: spatial: 0.201, goal: 0.086, long: 0.043, object: 0.037
6. **PI05 Trigger rates (adaptive)**: goal: 0.091, long: 0.045, spatial: 0.038, object: 0.036
7. **SMOLVLA Variance**: Highest std: object/crm-always-on (σ=0.0299). Lowest std: spatial/adaptive (σ=0.0058).
8. **PI05 Variance**: Highest std: spatial/vla-only (σ=0.0651). Lowest std: goal/vla-only (σ=0.0029).

## 7. Condition Summary Pivot Table

### SR by Model × Suite × Condition

| Model | Suite | VLA-only (N, μ±σ) | CRM-always-on (N, μ±σ) | Adaptive (N, μ±σ) | Δ(CRM-VLA) | Δ(Adp-VLA) | Δ(Adp-CRM) |
|---|---|---|---|---|---|---|---|
| smolvla | object | 9, 0.769±0.018 | 5, 0.722±0.030 | 6, 0.777±0.019 | -0.047 | +0.007 | +0.055 |
| smolvla | spatial | 8, 0.795±0.011 | 5, 0.779±0.013 | 7, 0.800±0.006 | -0.016 | +0.005 | +0.021 |
| smolvla | goal | 8, 0.827±0.016 | 5, 0.804±0.010 | 8, 0.836±0.019 | -0.023 | +0.009 | +0.032 |
| smolvla | long | 5, 0.589±0.013 | 4, 0.432±0.018 | 6, 0.578±0.019 | -0.156 | -0.011 | +0.145 |
| pi05 | object | 3, 0.993±0.008 | 3, 0.907±0.013 | 3, 0.862±0.024 | -0.087 | -0.132 | -0.045 |
| pi05 | spatial | 4, 0.948±0.065 | 3, 0.967±0.006 | 3, 0.973±0.010 | +0.019 | +0.026 | +0.007 |
| pi05 | goal | 3, 0.978±0.003 | 3, 0.825±0.010 | 3, 0.882±0.015 | -0.153 | -0.097 | +0.057 |
| pi05 | long | 3, 0.950±0.009 | 3, 0.763±0.006 | 3, 0.810±0.009 | -0.187 | -0.140 | +0.047 |
