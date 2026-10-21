# Experiment Metrics Summary

Generated: 2026-05-16 | Total: 60 experiments | With PPL: 37


## baseline

| exp_id | conclusion | eval_ppl | spec_summary | artifact_flag |
|--------|-----------|----------|-------------|---------------|
| baseline_qwen3_0.6b | success | 22.970 | Qwen3-0.6B |  |
| uniform_seed123 | success | 17.686 | method=uniform; bs=4; seed=123 |  |
| uniform_seed42 | success | 17.694 | method=uniform; bs=4; seed=42 |  |
| uniform_seed456 | success | 17.701 | method=uniform; bs=4; seed=456 |  |

## adaptive (n_min=2)

| exp_id | conclusion | eval_ppl | spec_summary | artifact_flag |
|--------|-----------|----------|-------------|---------------|
| adaptive_fix_seed123 | success | 17.643 | batch_size=4; contamination_ratio=0.4; tau=0.8 |  |
| adaptive_fix_seed42 | success | 17.653 | n_min=2; tau=0.8 |  |
| adaptive_fix_seed456 | success | 17.657 | n_min=2; tau=0.8 |  |

## adaptive (n_min=3)

| exp_id | conclusion | eval_ppl | spec_summary | artifact_flag |
|--------|-----------|----------|-------------|---------------|
| adaptive_seed123 | success | 17.631 | method=adaptive; contam=0.4; bs=4; seed=123 |  |
| adaptive_seed42 | success | 17.644 | method=adaptive; contam=0.4; bs=4; seed=42 |  |
| adaptive_seed456 | success | 17.642 | method=adaptive; contam=0.4; bs=4; seed=456 |  |

## ESS-only

| exp_id | conclusion | eval_ppl | spec_summary | artifact_flag |
|--------|-----------|----------|-------------|---------------|
| ess_only_seed123 | success | 17.720 | n_min=2; weighting_method=ess_only |  |
| ess_only_seed42 | success | 17.730 | n_min=2; weighting_method=ess_only |  |
| ess_only_seed456 | success | 17.719 | n_min=2; weighting_method=ess_only |  |

## grid-sweep

| exp_id | conclusion | eval_ppl | spec_summary | artifact_flag |
|--------|-----------|----------|-------------|---------------|
| grid_b0_5_seed123 | success | 17.638 | method=grid; b=0.5; contam=0.4; bs=4; seed=123; gpu_h=3.8 |  |
| grid_b0_5_seed456 | success | 17.650 | method=grid; b=0.5; contam=0.4; bs=4; seed=456; gpu_h=3.6 |  |
| grid_b1_0_seed123 | success | 17.674 | method=grid; b=1.0; contam=0.4; bs=4; seed=123; gpu_h=3.88 |  |
| grid_b1_0_seed456 | success | 17.680 | gpu_h=3.67 |  |
| grid_b1_5_seed123 | success | 17.701 | gpu_h=4.18 |  |
| grid_b1_5_seed456 | success | 17.710 | gpu_h=3.67 |  |
| grid_b2_0_seed123 | success | 17.725 | method=grid; b=2.0; contam=0.4; seed=123; gpu_h=3.63 |  |
| grid_b2_0_seed456 | success | 17.989 | method=grid; b=2.0; contam=0.4; bs=4; seed=456; gpu_h=3.6 | checkpoint_artifact |
| grid_b3_0_seed123 | success | 17.760 | gpu_h=3.6 |  |
| grid_b3_0_seed456 | success | 17.921 | method=grid; b=3.0; contam=0.4; bs=4; seed=456; gpu_h=1.83 | checkpoint_artifact |
| grid_b5_0_seed123 | success | 17.804 | method=grid; b=5.0; contam=0.4; bs=4; seed=123; gpu_h=4.01 |  |
| grid_b5_0_seed456 | success | 17.993 | method=grid; b=5.0; contam=0.4; bs=4; seed=456; gpu_h=1.83 | checkpoint_artifact |

## tau-sweep

| exp_id | conclusion | eval_ppl | spec_summary | artifact_flag |
|--------|-----------|----------|-------------|---------------|
| tau_0.6_seed42 | killed | — | N/A |  |
| tau_05_seed42 | success | 17.688 | method=adaptive; tau=0.5; contam=0.4; bs=4; seed=42 |  |
| tau_06_seed42 | success | 17.680 | tau=0.6; method=adaptive; contam=0.4; bs=4; seed=42 |  |
| tau_07_seed42 | success | 17.679 | method=adaptive; tau=0.7; contam=0.4; bs=4; seed=42 |  |
| tau_095_seed42 | negative | 17.723 | N/A |  |
| tau_09_seed42 | negative | 17.712 | N/A |  |

## nmin-ablation

| exp_id | conclusion | eval_ppl | spec_summary | artifact_flag |
|--------|-----------|----------|-------------|---------------|
| nmin1_seed42 | success | 17.789 | method=adaptive; tau=0.8; n_min=1; contam=0.4; bs=4; seed=42 |  |
| nmin4_seed42 | success | 17.695 | method=adaptive; tau=0.8; n_min=4; contam=0.4; bs=4; seed=42 |  |
| nmin5_seed42 | killed | — | N/A |  |

## contamination_60

| exp_id | conclusion | eval_ppl | spec_summary | artifact_flag |
|--------|-----------|----------|-------------|---------------|
| contamination_60_grid_b0_5_seed42 | success | 17.704 | method=grid; b=0.5; contam=0.6; bs=4; seed=42 |  |
| contamination_60_seed42 | failed | — | contamination_ratio=0.6 |  |
| contamination_60_seed42_r2 | success | 17.740 | method=adaptive; tau=0.8; n_min=2; contam=0.6; bs=4; seed=42 |  |
| contamination_60_uniform_seed42 | success | 17.766 | method=uniform; contam=0.6; bs=4; seed=42 |  |

## batch_size

| exp_id | conclusion | eval_ppl | spec_summary | artifact_flag |
|--------|-----------|----------|-------------|---------------|
| bs8_nmin2_seed42 | failed | — | method=adaptive; tau=0.8; n_min=2; contam=0.4; bs=8; seed=42 |  |
| bs8_nmin2_seed42_r2 | negative | 17.730 | method=adaptive; tau=0.8; n_min=2; contam=0.4; bs=8; seed=42 |  |
| bs8_seed42 | failed | — | method=adaptive; tau=0.8; n_min=4; contam=0.4; bs=8; seed=42 |  |

## other

| exp_id | conclusion | eval_ppl | spec_summary | artifact_flag |
|--------|-----------|----------|-------------|---------------|
| adaptive_v2_seed123 | killed | — | N/A |  |
| adaptive_v2_seed42 | killed | — | N/A |  |
| adaptive_v2_seed456 | killed | — | N/A |  |
| datagen_synthetic_4gpu | success | — | bs=128 |  |
| detector_modernbert | killed | — | N/A |  |
| detector_tfidf_lr | success | — | N/A |  |
| diagnostic_contamination100 | killed | — | method=uniform; seed=42 |  |
| golden_ratio_seed42 | success | 17.654 | method=golden_ratio; tau=0.8; contam=0.4; bs=4; seed=42; gpu... |  |
| grid_b_low_seed42 | failed | — | N/A |  |
| grid_b_low_seed42_r2 | failed | — | method=grid; b=$b; contam=0.4; bs=4; seed=42 |  |
| grid_b_low_seed42_r3 | failed | — | N/A |  |
| grid_b_low_serial_seed42 | killed | — | N/A |  |
| grid_b_seed42_batch | success | — | N/A |  |
| p0_contamination_60_datagen | success | — | N/A |  |
| tau_05_nmin2_seed42 | killed | — | method=adaptive; tau=0.5; n_min=2; contam=0.4; bs=4; seed=42 |  |
| tau_06_nmin2_seed42 | killed | — | N/A |  |
| tau_07_nmin2_seed42 | killed | — | N/A |  |
| tau_095_nmin2_seed42 | killed | — | N/A |  |
| tau_09_nmin2_seed42 | killed | — | N/A |  |
