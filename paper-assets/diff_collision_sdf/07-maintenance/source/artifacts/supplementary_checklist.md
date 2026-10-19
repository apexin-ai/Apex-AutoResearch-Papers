# Supplementary Material Checklist

> Generated: 2026-05-28
> Source: 131 experiments in registry (72 success, 25 negative, 18 failed, 16 killed)
> Authoritative eval pipeline: `reeval_*` series (rotation-fixed, eval_seed=7, n=200 episodes)

---

## S1. Multi-Seed Complete Results (Table)

### S1a. Main Results: CAR across conditions (reeval, rotation-fixed)

| Condition | Seed 0 | Seed 1 | Seed 2 | Mean±Std |
|-----------|--------|--------|--------|----------|
| LoRA-only | 57.0 | 52.5 | 55.0* | 54.8±2.3 |
| SDF λ=0.005 | 57.0 | 54.0 | 52.5 | 54.5±2.3 |
| SDF λ=0.01 | 57.0 | 57.5 | 54.5 | 56.3±1.6 |
| SDF λ=0.1 | 58.0 | 58.5 | 54.5 | 57.0±2.2 |

*LoRA s2 from `eval_lora_s2_30k_v2` (55% CAR, eval_seed=7)

**Data sources:**
- `reeval_lora_s0_30k_v2`: CAR=57, TSR=46
- `reeval_lora_s1_30k`: CAR=52.5, TSR=51.5
- `eval_lora_s2_30k_v2`: CAR=55, TSR=51.5
- `reeval_sdf_s0_l005_30k`: CAR=57, TSR=55.5
- `reeval_sdf_s1_l005_30k`: CAR=54, TSR=50.5
- `reeval_sdf_s2_l005_30k`: CAR=52.5, TSR=56
- `reeval_sdf_s0_l01_30k`: CAR=57, TSR=52.5
- `reeval_sdf_s1_l01_30k`: CAR=57.5, TSR=55.5
- `reeval_sdf_s2_l01_30k`: CAR=54.5, TSR=53.5
- `eval_pi05_a1_30k_s0_l01_high`: CAR=58, TSR=47
- `eval_pi05_a1_30k_s1_l01_high`: CAR=58.5, TSR=49
- `eval_pi05_a1_30k_s2_l01_high`: CAR=54.5, TSR=54.5

### S1b. TSR across conditions (reeval)

| Condition | Seed 0 | Seed 1 | Seed 2 | Mean±Std |
|-----------|--------|--------|--------|----------|
| LoRA-only | 46.0 | 51.5 | 51.5 | 49.7±3.2 |
| SDF λ=0.005 | 55.5 | 50.5 | 56.0 | 54.0±3.0 |
| SDF λ=0.01 | 52.5 | 55.5 | 53.5 | 53.8±1.5 |
| SDF λ=0.1 | 47.0 | 49.0 | 54.5 | 50.2±3.9 |

### S1c. EE Displacement (reeval, m)

| Condition | Seed 0 | Seed 1 | Seed 2 |
|-----------|--------|--------|--------|
| LoRA-only | — | 0.3882 | — |
| SDF λ=0.005 | — | 0.3883 | 0.3858 |
| SDF λ=0.01 | 0.3946 | 0.3852 | 0.3877 |
| SDF λ=0.1 | 0.400 | 0.3884 | — |

All frozen_rate_ee = 0%, fake_safe_rate_ee = 0%.

### S1d. Per-Task CAR Breakdown (reeval, all seeds)

**LoRA-only:**
| Seed | OrangeJuice | ChocoPudding | Milk | BBQSauce |
|------|-------------|--------------|------|----------|
| s0 | 68 | 74 | 66 | 20 |
| s1 | 54 | 68 | 72 | 16 |
| s2 | 56 | 76 | 62 | 26 |

**SDF λ=0.005:**
| Seed | OrangeJuice | ChocoPudding | Milk | BBQSauce |
|------|-------------|--------------|------|----------|
| s0 | 52 | 74 | 74 | 28 |
| s1 | 64 | 70 | 68 | 14 |
| s2 | 46 | 74 | 72 | 18 |

**SDF λ=0.01:**
| Seed | OrangeJuice | ChocoPudding | Milk | BBQSauce |
|------|-------------|--------------|------|----------|
| s0 | 48 | 74 | 72 | 34 |
| s1 | 60 | 76 | 72 | 22 |
| s2 | 64 | 68 | 72 | 14 |

**SDF λ=0.1:**
| Seed | OrangeJuice | ChocoPudding | Milk | BBQSauce |
|------|-------------|--------------|------|----------|
| s0 | 60 | 74 | 68 | 30 |
| s1 | 66 | 72 | 70 | 26 |
| s2 | 56 | 76 | 70 | 16 |

**Existing figure:** `fig_pertask_car_fingerprint.png`

---

## S2. Multi-Eval-Seed Robustness (Table)

Tests CAR stability across different eval_seed values for LoRA s0 and SDF (lambda=0.1) s0 checkpoints.

### S2a. LoRA-only s0 30K across eval seeds

| eval_seed | avg_CAR | avg_TSR | n_episodes |
|-----------|---------|---------|------------|
| 0 | 53.0 | 55.5 | 50 |
| 7 (default) | 56.5 | 51.5 | 200 |
| 42 | 56.5 | 46.0 | 50 |
| 99 | 57.5 | 52.0 | 50 |
| 123 | 53.0 | 50.5 | 50 |

**Mean CAR = 55.3%, Std = 2.0%**

**Data sources:** `eval_multiseed_lora_s0_eseed{0,42,99,123}`, `eval_lora_baseline_30k_s0_reeval`

### S2b. SDF s0 30K across eval seeds

Note: eseed 0/99 use λ=0.01 model; eseed 42/123/256 use λ=0.1 model.

| eval_seed | Model (λ) | avg_CAR | avg_TSR | n_episodes |
|-----------|-----------|---------|---------|------------|
| 0 | 0.01 | 52.5 | 48.5 | 50 |
| 42 | 0.1 | 59.0 | 52.5 | 50 |
| 99 | 0.01 | 57.0 | 46.5 | 50 |
| 123 | 0.1 | 58.5 | 53.5 | 50 |
| 256 | 0.1 | 57.0 | 48.0 | 50 |

**SDF λ=0.1 (eseed 42/123/256): Mean CAR = 58.2%, Std = 1.1%**
**SDF λ=0.01 (eseed 0/99): Mean CAR = 54.8%, Std = 3.2%**

**Data sources:** `eval_multiseed_sdf_l01_s0_eseed{0,42,99,123,256}`

### S2c. Per-Task Detail (available for eseed 42/123/256)

| eval_seed | OJ CAR | CP CAR | Milk CAR | BBQ CAR |
|-----------|--------|--------|----------|---------|
| 42 (LoRA) | 60 | 70 | 68 | 28 |
| 42 (SDF λ=0.1) | 64 | 74 | 74 | 24 |
| 123 (LoRA) | 52 | 74 | 66 | 20 |
| 123 (SDF λ=0.1) | 62 | 76 | 74 | 22 |
| 256 (SDF λ=0.1) | 60 | 72 | 66 | 30 |

**Existing figure:** None specific to eval-seed. Needs new figure.

---

## S3. Lambda Ablation Detailed Data (Table + Figure)

### S3a. Summary: CAR vs Lambda (reeval, 3 seeds each)

| λ | s0 CAR | s1 CAR | s2 CAR | Mean | Std | p vs null |
|---|--------|--------|--------|------|-----|-----------|
| 0 (LoRA-only) | 57 | 52.5 | 55 | 54.8 | 2.3 | — |
| 0.005 | 57 | 54 | 52.5 | 54.5 | 2.3 | within null |
| 0.01 | 57 | 57.5 | 54.5 | 56.3 | 1.6 | +0.84σ, p>0.1 |
| 0.1 | 58 | 58.5 | 54.5 | 57.0 | 2.2 | see S3c |
| 0 (Phase 2) | — | — | 57.5 | — | — | +1.40σ, p~0.08 |

Null distribution: LoRA + λ=0.005 pooled, mean=54.7%, σ=2.15%.

### S3b. Stepwise Training Curve for λ=0.1 s0

| Step | CAR | TSR | frozen_rate | exp_id |
|------|-----|-----|-------------|--------|
| 16K | 55.5 | 49.5 | 0% | eval_stepwise_s0_l1_16k |
| 20K | 55.0 | 54.0 | 0% | eval_early_signal_s0_l1_20k |
| 22K | 60.5 | 45.5 | 0% | eval_stepwise_s0_l1_22k |
| 24K | 52.5 | 50.5 | 0% | eval_stepwise_s0_l1_24k_v2 |
| 26K | 53.5 | 53.0 | 0% | eval_stepwise_s0_l1_26k_v2 |
| 28K | 54.5 | 48.5 | 0% | eval_stepwise_s0_l1_28k |
| 30K | 58.0 | 47.0 | 0% | eval_pi05_a1_30k_s0_l01_high |

### S3c. Permutation Test Results (Exact)

| Setting | Obs Mean | Perm p (1-tail) | Perm p (2-tail) | Welch p (1-tail) | Sig α=0.05? |
|---------|----------|-----------------|-----------------|------------------|-------------|
| λ=0.1, 2 seeds | 58.25 | 0.0357 | 0.0714 | 0.0035 | YES* |
| λ=0.1, 3 seeds (s2=54) | 56.83 | 0.1071 | 0.2143 | 0.1349 | NO |
| λ=0.1, 3 seeds (s2=55) | 57.17 | 0.0714 | 0.1548 | 0.0682 | NO |
| λ=0.1, 3 seeds (s2=56) | 57.50 | 0.0476 | 0.0833 | 0.0227 | YES |

*2-tail p=0.071, marginal

**Data source:** `permutation_test_results.txt`

**Existing figures:**
- `fig5_lambda_curve.pdf` / `fig5_lambda_curve.png` — CAR vs λ
- `fig5_lambda_car_v4.png` — updated version
- `fig_threshold_sensitivity.pdf` — threshold sensitivity analysis

---

## S4. Oracle Experiment Complete Results (Table)

All oracle experiments produced **negative** conclusions. Unified finding: even GT SDF cannot improve CAR; refinement causes action collapse.

### S4a. Oracle Lineage and Results

| Experiment | Oracle Type | CAR | TSR | Fake Safe % | Notes |
|-----------|------------|-----|-----|-------------|-------|
| Baseline (no refinement) | — | 79%† | — | — | Reference |
| oracle_a3_force_refine_object_v11 | Learned decoder, force_refine | 81.2 | 0 | — | M027: dead code, used learned decoder |
| oracle_a3_m024fix_object_v11 | M024 coord fix, learned decoder | 85.6 | 0 | — | 85.6% frozen = fake safety |
| oracle_true_gt_adaptive_alpha_v11 | GT SDF, adaptive alpha | 75.0 | 0 | 98.3% | 118/120 safe eps disp<0.1mm |
| oracle_true_gt_fixed_alpha_v11 | GT SDF, fixed alpha=0.005 | 73.1 | 0 | 98.3% | 115/117 safe eps disp<0.1mm |
| oracle_true_gt_feature_v11 | GT SDF, feature-space gradient | 76.9 | 0 | 96.7% | 119/123 safe eps disp<0.1mm |

†Baseline CAR from eval_baseline_v11_object

### S4b. Per-Task CAR Breakdown (Oracle)

| Task | Adaptive α | Fixed α | Feature-space |
|------|-----------|---------|---------------|
| OrangeJuice | 82.5 | 85.0 | 90.0 |
| ChocoPudding | 55.0 | 50.0 | 47.5 |
| Milk | 77.5 | 77.5 | 82.5 |
| BBQSauce | 85.0 | 80.0 | 87.5 |

### S4c. Refinement Statistics

| Metric | Adaptive α | Fixed α | Feature-space |
|--------|-----------|---------|---------------|
| Avg refined steps/ep | 14.2 | 14.8 | 241.7 |
| Total refined steps | 2270 | 2375 | 38679 |
| Grad magnitude (mean) | 0.18–0.49 | — | 0.004–0.006 |
| n_episodes | 160 | 160 | 160 |

### S4d. Per-Task Displacement (Oracle)

| Task | Adaptive α (m) | Fixed α (m) | Feature-space (m) |
|------|---------------|-------------|-------------------|
| OrangeJuice | 0.0076 | 0.0113 | 0.0023 |
| ChocoPudding | 0.0475 | 0.0365 | 0.0473 |
| Milk | 0.0107 | 0.0042 | 0.0086 |
| BBQSauce | 0.0077 | 0.0032 | 0.0097 |

**Data sources:** `oracle_true_gt_adaptive_alpha_v11`, `oracle_true_gt_fixed_alpha_v11`, `oracle_true_gt_feature_v11`

**Existing figure:** `fig_oracle_bar.pdf`

---

## S5. Training Curves

**Registry has NO wandb_run_id fields** — W&B tracking was not registered in the experiment registry.

### S5a. Available Training Loss Data (from registry metrics)

| Experiment | best_loss | final_loss | best_step | total_steps |
|-----------|-----------|------------|-----------|-------------|
| train_pi05_lora_baseline_s0 | 0.01025 | 0.01343 | 24K | 30K |
| train_pi05_lora_baseline_s1 | 0.01130 | 0.01408 | 14K | 30K |
| train_pi05_lora_baseline_s2_resume | — | 0.01170 | — | 30K |
| train_pi05_a1_obj_s0_l005 | 0.00786 | — | 26K | 30K |
| train_pi05_a1_obj_s1_l005 | 0.01143 | — | 16K | 30K |
| train_pi05_a1_obj_s2_l005 | 0.00874 | — | 10K | 30K |
| train_pi05_a1_obj_s0_l01 | 0.00801 | — | — | 30K |
| train_pi05_a1_obj_s1_l01 | 0.01168 | — | 16K | 30K |
| train_pi05_a1_obj_s2_l01 | 0.00911 | — | 10K | 30K |
| train_pi05_a1_obj_s2_l01_high | 0.01040 | 0.01040 | 30K | 30K |
| train_pi05_phase2_lambda0_s2 | 0.00651 | — | 4K | 10K |

### S5b. Action Items for Training Curves

- [ ] Check if W&B runs exist on server (not tracked in registry)
- [ ] If W&B available: export loss curves for LoRA-only vs SDF conditions
- [ ] If not: only scalar best/final loss available (table above), no time-series curves
- [ ] A3 training metrics available for `a3_gradient_object_pudding_s0`: action_loss=0.01546, total_loss=0.01898, eikonal=0, n_refine=2.64

---

## S6. Additional Supplementary Data

### S6a. SSR (Safe Success Rate) Analysis

| Condition | Avg TSR | Avg CAR | Avg SSR | SSR/TSR |
|-----------|---------|---------|---------|---------|
| Pi0.5 baseline | 71.5% | 28.5% | 28.0% | 0.392 |
| LoRA (2 seeds) | 51.5% | 54.5% | 28.3% | 0.549 |
| SDF λ=0.005 (3 seeds) | 54.0% | 54.5% | 27.8% | 0.515 |
| SDF λ=0.01 (3 seeds) | 53.8% | 56.3% | 30.2% | 0.561 |

**Data source:** `ssr_analysis.md`

### S6b. Threshold Sensitivity Analysis

- dfCAR stable across collision thresholds 2mm–200mm
- `analysis_threshold_sensitivity` experiment registered
- **Existing figures:** `fig_threshold_sensitivity.pdf`, `sensitivity_curves.png`
- **Data:** `threshold_sensitivity.csv`

### S6c. Fake Safety (A1 Full-FT Baseline)

- Fake safe rate = 99.6% (729/732 safe episodes with displacement < 0.1mm)
- **Data source:** `eval_a1_lora_object_v11_rerun` (800 episodes)
- **Existing figure:** `fig_displacement_hist.pdf`, `fig2_ee_displacement_distribution.pdf`

### S6d. Spatial Bowl Transfer Results

| Condition | avg_CAR | avg_TSR | exp_id |
|-----------|---------|---------|--------|
| LoRA-only s0 | 12.0 | 49.0 | eval_spatial_bowl_lora_ctrl_s0_v2 |
| SDF λ=0.005 s0 | 11.5 | 51.5 | eval_spatial_bowl_sdf_s0_l005_30k |

SDF provides no transfer benefit on spatial_bowl scene.

---

## Summary: Existing Figures Index

| Figure | File | In Paper? |
|--------|------|-----------|
| Teaser / overview | `fig1_teaser_v2.pdf`, `fig_overview_pb_v13.png` | Yes |
| EE displacement distribution | `fig2_ee_displacement_distribution.pdf` | Yes |
| TSR–CAR scatter | `fig3_tsr_car_scatter.pdf` | Yes |
| Lambda curve (CAR vs λ) | `fig5_lambda_curve.pdf`, `fig5_lambda_car_v4.png` | Yes |
| Threshold sensitivity | `fig_threshold_sensitivity.pdf` | Yes |
| Oracle bar chart | `fig_oracle_bar.pdf` | Yes |
| Per-task CAR fingerprint | `fig_pertask_car_fingerprint.png` | Yes |
| Plan A/B concept | `fig2_plan_a.png`, `fig2_plan_b.png` | Yes |

### Figures Needed for Supplementary

- [ ] Multi-eval-seed CAR bar chart (LoRA vs SDF across eval seeds)
- [ ] Per-task TSR breakdown table/heatmap
- [ ] Training loss curves (if W&B data available)
- [ ] Stepwise CAR curve for λ=0.1 (step 16K–30K)
