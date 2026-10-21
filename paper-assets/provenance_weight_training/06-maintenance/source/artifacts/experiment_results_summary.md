# Experiment Results Summary

Total DONE experiments: **63**
Generated: 2026-05-16

## Claim 1: Dual (adaptive) > ESS-only > Uniform

Compares adaptive weighting (dual b* optimization) vs ESS-only vs uniform baseline across 3 seeds.

| exp_id | method | seed | PPL_holdout | loss_holdout | tau | n_min | rho | GPU_hrs | conclusion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| uniform_seed123 | uniform | 123 | 17.6861 | 2.8728 | N/A | N/A | N/A | 3.4300 | success |
| uniform_seed42 | uniform | 42 | 17.6939 | 2.8732 | N/A | N/A | N/A | 3.4300 | success |
| uniform_seed456 | uniform | 456 | 17.7015 | 2.8737 | N/A | N/A | N/A | 3.4300 | success |
| ess_only_seed123 | ess_only | 123 | 17.7200 | 2.8746 | N/A | 2 | 0.4 | N/A | success |
| ess_only_seed42 | ess_only | 42 | N/A | 2.8750 | 0.8 | 2 | 0.4 | N/A | success |
| ess_only_seed456 | ess_only | 456 | N/A | 2.8746 | N/A | 2 | 0.4 | N/A | success |
| adaptive_fix_seed123 | adaptive | 123 | 17.6432 | 2.8704 | 0.8000 | N/A | 0.4000 | N/A | success |
| adaptive_seed123 | adaptive | 123 | 17.6308 | 2.8696 | 0.8000 | 3 | 0.4000 | 4.2100 | success |
| adaptive_v2_seed123 | adaptive | 123 | N/A | N/A | N/A | N/A | N/A | N/A | killed |
| adaptive_fix_seed42 | adaptive | 42 | 17.6527 | 2.8709 | 0.8000 | 2 | N/A | N/A | success |
| adaptive_seed42 | adaptive | 42 | 17.6440 | 2.8704 | 0.8000 | 3 | 0.4000 | 4.2100 | success |
| adaptive_v2_seed42 | adaptive | 42 | N/A | N/A | N/A | N/A | N/A | N/A | killed |
| adaptive_fix_seed456 | adaptive | 456 | 17.6566 | 2.8711 | 0.8000 | 2 | 0.4 | N/A | success |
| adaptive_seed456 | adaptive | 456 | 17.6419 | 2.8703 | 0.8000 | 3 | 0.4000 | 4.2100 | success |
| adaptive_v2_seed456 | adaptive | 456 | N/A | N/A | N/A | N/A | N/A | N/A | killed |

- **uniform** mean PPL: 17.6938 (n=3, seeds: 123, 42, 456)
- **ess_only** mean PPL: 17.7200 (n=1, seeds: 123)
- **adaptive** mean PPL: 17.6449 (n=6, seeds: 123, 123, 42, 42, 456, 456)
  - *adaptive_fix* mean PPL: 17.6508 (n=3)

## Claim 2: Adaptive ~ Grid-optimal

Grid sweep with fixed b values across seeds. Adaptive should match best grid point without manual tuning.

| exp_id | grid_b | seed | PPL_holdout | loss_holdout | GPU_hrs | conclusion |
| --- | --- | --- | --- | --- | --- | --- |
| grid_b0_3_seed42 | 0.3000 | 42 | 17.6400 | 2.8702 | 3.8400 | success |
| grid_b0_5_seed123 | 0.5000 | 123 | 17.6380 | 2.8700 | 3.8000 | success |
| grid_b0_5_seed456 | 0.5000 | 456 | 17.6500 | 2.8705 | 3.6000 | success |
| grid_b1_0_seed123 | 1.0000 | 123 | 17.6740 | 2.8721 | 3.8800 | success |
| grid_b1_0_seed456 | 1.0000 | 456 | 17.6800 | 2.8734 | 3.6700 | success |
| grid_b1_5_seed123 | 1.5000 | 123 | 17.7010 | 2.8736 | 4.1800 | success |
| grid_b1_5_seed456 | 1.5000 | 456 | 17.7100 | 2.8750 | 3.6700 | success |
| grid_b2_0_seed123 | 2.0000 | 123 | 17.7250 | 2.8750 | 3.6300 | success |
| grid_b2_0_seed456 | 2.0000 | 456 | 17.9890 | 2.8898 | 3.6000 | success |
| grid_b3_0_seed123 | 3.0000 | 123 | 17.7600 | 2.8770 | 3.6000 | success |
| grid_b3_0_seed456 | 3.0000 | 456 | 17.9210 | 2.8860 | 1.8300 | success |
| grid_b5_0_seed123 | 5.0000 | 123 | 17.8039 | 2.8794 | 4.0100 | success |
| grid_b5_0_seed456 | 5.0000 | 456 | 17.9930 | 2.8900 | 1.8300 | success |
| grid_b_low_seed42 | batch | 42 | N/A | N/A | 0.2200 | failed |
| grid_b_low_seed42_r2 | batch | 42 | N/A | N/A | 0.0100 | failed |
| grid_b_low_seed42_r3 | batch | 42 | N/A | N/A | N/A | failed |
| grid_b_low_serial_seed42 | batch | 42 | N/A | N/A | 0.1000 | killed |
| grid_b_seed42_batch | batch | 42 | N/A | N/A | 22.5300 | success |

- Seed 42: best grid PPL = 17.64 at b=0.3
- Seed 123: best grid PPL = 17.638 at b=0.5
- Seed 456: best grid PPL = 17.65 at b=0.5

**grid_b_seed42_batch detailed results** (6 b values in one run):

| b | PPL_holdout | train_loss |
| --- | --- | --- |
| 0.5 | 17.651 | 9.598 |
| 1.0 | 17.692 | 10.223 |
| 1.5 | 17.718 | 10.485 |
| 2.0 | 17.741 | 10.621 |
| 3.0 | 17.774 | 10.754 |
| 5.0 | 17.818 | 10.858 |

Best: b=0.5, PPL=17.651

## Claim 3: Proportion-free (robust across rho)

Experiments with contamination_ratio=0.6 (vs default 0.4). Tests robustness.

| exp_id | method | seed | PPL_holdout | loss_holdout | tau | n_min | rho | GPU_hrs | conclusion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| contamination_60_seed42 | adaptive | 42 | N/A | N/A | 0.8000 | 2 | 0.6000 | N/A | failed |
| contamination_60_seed42_r2 | adaptive | 42 | 17.7400 | 2.8759 | 0.8 | 2 | 0.6 | 4.0500 | success |
| contamination_60_ess_only_seed42 | ess_only | 42 | 17.7700 | 2.8775 | 0.8 | 2 | 0.6 | 3.9400 | success |
| contamination_60_grid_b0_5_seed42 | grid | 42 | N/A | 2.8738 | N/A | N/A | 0.6 | 3.6500 | success |
| contamination_60_uniform_seed42 | uniform | 42 | 17.7660 | 2.8773 | N/A | N/A | 0.6 | 3.6100 | success |
| diagnostic_contamination100 | uniform | 42 | N/A | N/A | N/A | N/A | 1.0000 | N/A | killed |

## Baselines

| exp_id | method | seed | PPL_holdout | loss_holdout | tau | n_min | rho | GPU_hrs | conclusion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| detect_remove_baseline_seed42 | detect_remove | 42 | 17.2900 | 2.8499 | N/A | N/A | N/A | N/A | success |
| golden_ratio_seed42 | golden_ratio | 42 | 17.6540 | 2.8710 | 0.8 | N/A | 0.4 | 3.7300 | success |

## Ablations

Tau sweep, n_min sweep, and batch_size variations on adaptive method.

| exp_id | tau | n_min | batch_size | seed | PPL_holdout | loss_holdout | GPU_hrs | conclusion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bs8_nmin2_seed42 | 0.8 | 2 | 8 | 42 | N/A | N/A | 0.0100 | failed |
| bs8_nmin2_seed42_r2 | 0.8 | 2 | 8 | 42 | 17.7300 | 2.8752 | 4.1000 | negative |
| bs8_seed42 | 0.8 | 4 | 8 | 42 | N/A | N/A | 0.1900 | failed |
| nmin1_seed42 | 0.8 | 1 | 4 | 42 | 17.7890 | 2.8786 | 5.0100 | success |
| nmin4_seed42 | 0.8 | 4 | 4 | 42 | 17.6947 | 2.8733 | 4.6300 | success |
| nmin5_seed42 | N/A | 5 | N/A | 42 | N/A | N/A | N/A | killed |
| tau_0.6_seed42 | 0.6000 | N/A | N/A | 42 | N/A | N/A | N/A | killed |
| tau_05_nmin2_seed42 | 0.5 | 2 | 4 | 42 | N/A | N/A | 0.7800 | killed |
| tau_05_seed42 | 0.5 | N/A | 4 | 42 | 17.6880 | 2.8729 | N/A | success |
| tau_06_nmin2_seed42 | 0.6000 | 2 | N/A | 42 | N/A | N/A | N/A | killed |
| tau_06_seed42 | 0.6000 | N/A | 4 | 42 | 17.6805 | 2.8725 | 3.8800 | success |
| tau_07_nmin2_seed42 | 0.7000 | 2 | N/A | 42 | N/A | N/A | N/A | killed |
| tau_07_seed42 | 0.7 | N/A | 4 | 42 | 17.6793 | 2.8724 | 4.3600 | success |
| tau_095_nmin2_seed42 | 0.9500 | 2 | N/A | 42 | N/A | N/A | N/A | killed |
| tau_095_seed42 | 0.9500 | N/A | N/A | 42 | 17.7230 | 2.8749 | N/A | negative |
| tau_09_nmin2_seed42 | 0.9000 | 2 | N/A | 42 | N/A | N/A | N/A | killed |
| tau_09_seed42 | 0.9000 | N/A | N/A | 42 | 17.7120 | 2.8742 | N/A | negative |

## Infrastructure / Non-training

| exp_id | type | conclusion | hypothesis |
| --- | --- | --- | --- |
| baseline_qwen3_0.6b | none | success | Raw Qwen3-0.6B pretrained checkpoint baseline PPL (no continued pretraining). Reference point for quantifying absolute i |
| datagen_synthetic_4gpu | datagen | success | 4-GPU parallel generation produces 132M synthetic tokens in ~2.5h |
| detector_modernbert | detector | killed | ModernBERT-base can distinguish Qwen3-0.6B synthetic text from FineWeb human text with AUC>=0.95 and ECE<=0.05 |
| detector_tfidf_lr | detector | success | TF-IDF + LogisticRegression detector provides spread q-scores (AUC~0.94, not binarized) for provenance weighting, replac |
| p0_contamination_60_datagen | datagen | success | N/A |

## Failed / Killed / Negative Experiments

| exp_id | method | conclusion | PPL_holdout |
| --- | --- | --- | --- |
| adaptive_v2_seed123 | adaptive | killed | N/A |
| adaptive_v2_seed42 | adaptive | killed | N/A |
| adaptive_v2_seed456 | adaptive | killed | N/A |
| bs8_nmin2_seed42 | adaptive | failed | N/A |
| bs8_nmin2_seed42_r2 | adaptive | negative | 17.7300 |
| bs8_seed42 | adaptive | failed | N/A |
| contamination_60_seed42 | adaptive | failed | N/A |
| detector_modernbert | detector | killed | N/A |
| diagnostic_contamination100 | uniform | killed | N/A |
| grid_b_low_seed42 | grid | failed | N/A |
| grid_b_low_seed42_r2 | grid | failed | N/A |
| grid_b_low_seed42_r3 | grid | failed | N/A |
| grid_b_low_serial_seed42 | grid | killed | N/A |
| nmin5_seed42 | adaptive | killed | N/A |
| tau_0.6_seed42 | adaptive | killed | N/A |
| tau_05_nmin2_seed42 | adaptive | killed | N/A |
| tau_06_nmin2_seed42 | adaptive | killed | N/A |
| tau_07_nmin2_seed42 | adaptive | killed | N/A |
| tau_095_nmin2_seed42 | adaptive | killed | N/A |
| tau_095_seed42 | adaptive | negative | 17.7230 |
| tau_09_nmin2_seed42 | adaptive | killed | N/A |
| tau_09_seed42 | adaptive | negative | 17.7120 |
