# Provenance Weight Training — Experiment Metrics Summary

**Generated**: 2026-05-16
**Total experiments**: 59

## Experiment Counts by Group

| Group | Count |
|-------|-------|
| baseline | 4 |
| adaptive (n_min=2) | 3 |
| adaptive (n_min=3) | 3 |
| ESS-only | 3 |
| grid-sweep | 17 |
| tau-sweep | 11 |
| contamination_60 | 4 |
| batch_size | 3 |
| other | 11 |

## baseline

| exp_id | PPL | conclusion | method | ρ | τ | n_min | bs | seed |
|--------|-----|-----------|--------|---|---|-------|----|----|
| uniform_seed123 | 17.686 | success | uniform | N/A | N/A | N/A | 4 | 123 |
| uniform_seed42 | 17.694 | success | uniform | N/A | N/A | N/A | 4 | 42 |
| uniform_seed456 | 17.701 | success | uniform | N/A | N/A | N/A | 4 | 456 |
| baseline_qwen3_0.6b | 22.970 | success | N/A | N/A | N/A | N/A | N/A | 0 |

## adaptive (n_min=2)

| exp_id | PPL | conclusion | method | ρ | τ | n_min | bs | seed |
|--------|-----|-----------|--------|---|---|-------|----|----|
| adaptive_fix_seed123 | 17.643 | success | adaptive | N/A | N/A | 2 | N/A | 123 |
| adaptive_fix_seed42 | 17.653 | success | adaptive | 0.4 | N/A | N/A | 4 | 42 |
| adaptive_fix_seed456 | 17.657 | success | adaptive | 0.4 | N/A | N/A | 4 | 456 |

## adaptive (n_min=3)

| exp_id | PPL | conclusion | method | ρ | τ | n_min | bs | seed |
|--------|-----|-----------|--------|---|---|-------|----|----|
| adaptive_seed123 | 17.631 | success | adaptive | 0.4 | 0.8 | 3 | 4 | 123 |
| adaptive_seed456 | 17.642 | success | adaptive | 0.4 | 0.8 | 3 | 4 | 456 |
| adaptive_seed42 | 17.644 | success | adaptive | 0.4 | 0.8 | 3 | 4 | 42 |

## ESS-only

| exp_id | PPL | conclusion | method | ρ | τ | n_min | bs | seed |
|--------|-----|-----------|--------|---|---|-------|----|----|
| ess_only_seed456 | 17.719 | success | ess_only | 0.4 | N/A | 2 | 4 | 456 |
| ess_only_seed123 | 17.720 | success | ess_only | 0.4 | N/A | 2 | 4 | 123 |
| ess_only_seed42 | 17.730 | success | ess_only | 0.4 | 0.8 | N/A | 4 | 42 |

## grid-sweep

| exp_id | PPL | conclusion | method | ρ | τ | n_min | bs | seed |
|--------|-----|-----------|--------|---|---|-------|----|----|
| grid_b0_5_seed123 | 17.638 | success | grid | 0.4 | N/A | N/A | 4 | 123 |
| grid_b0_5_seed456 | 17.650 | success | grid | 0.4 | N/A | N/A | 4 | 456 |
| grid_b_seed42_batch | 17.651 | success | grid | N/A | N/A | N/A | N/A | 42 |
| grid_b1_0_seed123 | 17.674 | success | grid | 0.4 | N/A | N/A | 4 | 123 |
| grid_b1_0_seed456 | 17.680 | success | grid | N/A | N/A | N/A | N/A | 456 |
| grid_b1_5_seed123 | 17.701 | success | grid | N/A | N/A | N/A | N/A | 123 |
| grid_b1_5_seed456 | 17.710 | success | grid | N/A | N/A | N/A | N/A | 456 |
| grid_b2_0_seed123 | 17.725 | success | grid | 0.4 | N/A | N/A | N/A | 123 |
| grid_b3_0_seed123 | 17.760 | success | grid | N/A | N/A | N/A | N/A | 123 |
| grid_b5_0_seed123 | 17.804 | success | grid | 0.4 | N/A | N/A | 4 | 123 |
| grid_b3_0_seed456 | 17.921 | success | grid | 0.4 | N/A | N/A | 4 | 456 |
| grid_b2_0_seed456 | 17.989 | success | grid | 0.4 | N/A | N/A | 4 | 456 |
| grid_b5_0_seed456 | 17.993 | success | grid | 0.4 | N/A | N/A | 4 | 456 |
| grid_b_low_seed42 | N/A | failed | grid | N/A | N/A | N/A | N/A | 42 |
| grid_b_low_seed42_r2 | N/A | failed | grid | 0.4 | N/A | N/A | 4 | 42 |
| grid_b_low_seed42_r3 | N/A | failed | grid | N/A | N/A | N/A | N/A | 42 |
| grid_b_low_serial_seed42 | N/A | killed | grid | N/A | N/A | N/A | N/A | 42 |

## tau-sweep

| exp_id | PPL | conclusion | method | ρ | τ | n_min | bs | seed |
|--------|-----|-----------|--------|---|---|-------|----|----|
| tau_07_seed42 | 17.679 | success | adaptive | 0.4 | 0.7 | N/A | 4 | 42 |
| tau_06_seed42 | 17.680 | success | adaptive | 0.4 | 0.6 | N/A | 4 | 42 |
| tau_05_seed42 | 17.688 | success | adaptive | 0.4 | 0.5 | N/A | 4 | 42 |
| tau_09_seed42 | 17.712 | ⚠️ negative | adaptive | N/A | 0.9 | N/A | N/A | 42 |
| tau_095_seed42 | 17.723 | ⚠️ negative | adaptive | N/A | 0.95 | N/A | N/A | 42 |
| tau_0.6_seed42 | N/A | killed | adaptive | N/A | 0.6 | N/A | N/A | 42 |
| tau_05_nmin2_seed42 | N/A | killed | adaptive | 0.4 | 0.5 | 2 | 4 | 42 |
| tau_06_nmin2_seed42 | N/A | killed | adaptive | N/A | 0.6 | 2 | N/A | 42 |
| tau_07_nmin2_seed42 | N/A | killed | adaptive | N/A | 0.7 | 2 | N/A | 42 |
| tau_095_nmin2_seed42 | N/A | killed | adaptive | N/A | 0.95 | 2 | N/A | 42 |
| tau_09_nmin2_seed42 | N/A | killed | adaptive | N/A | 0.9 | 2 | N/A | 42 |

## contamination_60

| exp_id | PPL | conclusion | method | ρ | τ | n_min | bs | seed |
|--------|-----|-----------|--------|---|---|-------|----|----|
| contamination_60_uniform_seed42 | 17.766 | success | uniform | 0.6 | N/A | N/A | 4 | 42 |
| contamination_60_grid_b0_5_seed42 | 17.704 | success | grid | 0.6 | N/A | N/A | 4 | 42 |
| contamination_60_seed42_r2 | 17.740 | success | adaptive | 0.6 | 0.8 | 2 | 4 | 42 |
| contamination_60_seed42 | N/A | failed | adaptive | 0.6 | 0.8 | 2 | 4 | 42 |

## batch_size

| exp_id | PPL | conclusion | method | ρ | τ | n_min | bs | seed |
|--------|-----|-----------|--------|---|---|-------|----|----|
| bs8_nmin2_seed42_r2 | 17.730 | ⚠️ negative | adaptive | 0.4 | 0.8 | 2 | 8 | 42 |
| bs8_nmin2_seed42 | N/A | failed | adaptive | 0.4 | 0.8 | 2 | 8 | 42 |
| bs8_seed42 | N/A | failed | adaptive | 0.4 | 0.8 | 4 | 8 | 42 |

## other

| exp_id | PPL | conclusion | method | ρ | τ | n_min | bs | seed |
|--------|-----|-----------|--------|---|---|-------|----|----|
| golden_ratio_seed42 | 17.654 | success | golden_ratio | 0.4 | 0.8 | N/A | 4 | 42 |
| nmin4_seed42 | 17.695 | success | adaptive | 0.4 | 0.8 | 4 | 4 | 42 |
| nmin1_seed42 | 17.789 | success | adaptive | 0.4 | 0.8 | 1 | 4 | 42 |
| adaptive_v2_seed123 | N/A | killed | adaptive | N/A | N/A | N/A | N/A | 123 |
| adaptive_v2_seed42 | N/A | killed | adaptive | N/A | N/A | N/A | N/A | 42 |
| adaptive_v2_seed456 | N/A | killed | adaptive | N/A | N/A | N/A | N/A | 456 |
| datagen_synthetic_4gpu | N/A | success | N/A | N/A | N/A | N/A | 128 | 42/1042/2042/3042 |
| detector_modernbert | N/A | killed | N/A | N/A | N/A | N/A | N/A | N/A |
| detector_tfidf_lr | N/A | success | N/A | N/A | N/A | N/A | N/A | 42 |
| diagnostic_contamination100 | N/A | killed | uniform | 1.0 | N/A | N/A | N/A | 42 |
| p0_contamination_60_datagen | N/A | success | adaptive | 0.6 | N/A | N/A | N/A | 42 |
