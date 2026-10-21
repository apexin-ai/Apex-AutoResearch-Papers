# Registry Audit: CRM Checkpoints, K Values, and Key Parameters

Generated: 2026-05-29

---

## 1. Pi0.5 (pi05) Experiments - CRM Checkpoint Paths

### 1.1 Primary CRM Checkpoint for pi05

Almost all pi05 experiments use a single unified CRM checkpoint:

```
/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt
```

This was trained by `train-crm-pi05-unified-3suite` (obs_only, 3-suite: Spatial+Goal+Object, obs_dim=2048, ~194K samples).

**Alternative checkpoints used in some early/failed experiments:**
- `/root/autodl-tmp/checkpoints/crm_pi05_full/spatial/crm_best.pt` (spatial-only, used in failed `eval-pi05-crm-spatial-seed42/43/44`)
- `/root/autodl-tmp/checkpoints/crm_pi05_full/object/crm_best.pt` (object-only, from `crm-train-pi05-object-full`)
- `/root/autodl-tmp/models/pi05_libero_finetuned` (listed as CRM source in `pi05-crm-k2-object-*-bjb1-r2` spec `checkpoint_source`, but actual CRM is the unified 3-suite)

### 1.2 Pi05 Goal Adaptive / Tau-Gated (DONE/success)

All use: `crm_pi05_unified_3suite/crm_best.pt`, K=2, norm=0.2

| exp_id | tau | SR | server |
|--------|-----|-----|--------|
| pi05-adaptive-goal-s42-cqa1 | 0.25 | 89.5% | cqa1 |
| pi05-adaptive-goal-s43-bjb1-18228 | 0.25 | 89.5% | bjb1 |
| pi05-adaptive-goal-s44-backfill | 0.25 | 86.5% | - |
| westd-pi05-adaptive-goal-s42 | 0.25 | 88.0% | westd |
| westd-pi05-adaptive-goal-s43 | 0.25 | 87.5% | westd |
| pi05-adaptive-goal-s42-tau015-bjb2 | 0.15 | 92.0% | bjb2 |
| pi05-adaptive-goal-s42-tau035-bjb2 | 0.35 | 87.5% | bjb2 |
| pi05-tau-sweep-goal-tau050-s42-r3 | 0.50 | 87.0% | - |
| pi05-tau-sweep-goal-tau070-s42-r2 | 0.70 | 87.0% | - |
| pi05-goal-tau015-s43-r3 | 0.15 | 87.5% | - |
| pi05-goal-tau025-s43-r3 | 0.25 | 88.5% | - |
| pi05-goal-tau035-s43-r3 | 0.35 | 89.5% | - |

### 1.3 Pi05 Long CRM Always-On (DONE)

CRM: `crm_pi05_unified_3suite/crm_best.pt` (confirmed from s43 spec `checkpoint_source`; s42 command omitted the flag but used same code default). K=2, tau=0.001, norm=0.2.

| exp_id | status | conclusion | SR |
|--------|--------|------------|-----|
| pi05-crm-always-on-long-s42 | DONE | success | 77.0% |
| pi05-crm-always-on-long-s43 | DONE | success | 79.5% |
| pi05-crm-always-on-long-s44 | DONE | killed | - |

Note: `s44` was killed, so only 2 seeds available. Baseline VLA-only SR for pi05 Long: ~94%.

### 1.4 Pi05 Long Adaptive (DONE/success)

CRM: `crm_pi05_unified_3suite/crm_best.pt`. K=2, norm=0.2.

| exp_id | tau | SR |
|--------|-----|-----|
| pi05-adaptive-long-s42-r2 | 0.25 | 80.5% |
| pi05-adaptive-long-s42-tau015-bjb2 | 0.15 | 84.0% |
| pi05-adaptive-long-s43-bjb1 | 0.25 | 79.0% |
| pi05-adaptive-long-s43-cqa1-r3 | 0.25 | 80.5% |
| pi05-adaptive-long-s44-bjb1 | 0.25 | 82.0% |
| pi05-adaptive-long-s44-cqa1-r3 | 0.25 | 83.0% |

### 1.5 Pi05 Spatial CRM (crm_obs_only mode, DONE/success)

CRM: `crm_pi05_unified_3suite/crm_best.pt`. K=2, norm=0.05.

| exp_id | SR |
|--------|-----|
| pi05-crm-k2-spatial-s42-bjb2-r2 | 96.5% |
| pi05-crm-k2-spatial-s43-bjb2-r2 | 97.0% |
| pi05-crm-k2-spatial-s44-bjb2-r2 | 97.0% |

### 1.6 Pi05 Object CRM (crm_obs_only mode, DONE/success)

CRM: `crm_pi05_unified_3suite/crm_best.pt` (actual, despite some specs listing `/root/autodl-tmp/models/pi05_libero_finetuned` as `checkpoint_source` -- that's the VLA model path, not CRM). K=2, norm=0.05.

| exp_id | SR |
|--------|-----|
| pi05-crm-k2-object-s42-bjb1-r2 | 89.0% |
| pi05-crm-k2-object-s43-bjb1-r2 | 87.0% |
| pi05-crm-k2-object-s44-bjb1-r2 | 88.0% |

### 1.7 Pi05 Spatial/Object/Goal Always-On (DONE/success)

CRM: `crm_pi05_unified_3suite/crm_best.pt`. K=2, tau=0.001, norm=0.2.

| exp_id | benchmark | SR |
|--------|-----------|-----|
| pi05-crm-always-on-spatial-s42 | spatial | 96.0% |
| pi05-crm-always-on-object-s42 | object | 90.5% |
| pi05-crm-always-on-object-s43 | object | 92.0% |
| pi05-crm-always-on-object-s44 | object | 89.5% |
| pi05-crm-always-on-goal-s42 | goal | - |
| pi05-crm-always-on-goal-s43 | goal | - |
| pi05-crm-always-on-goal-s44 | goal | - |

### 1.8 Pi05 Goal CRM (crm_obs_only mode, DONE/success)

CRM (bjb1 runs): `/root/autodl-tmp/models/pi05_libero_finetuned` (as `checkpoint_source` in spec -- may be VLA model, actual CRM likely `crm_pi05_unified_3suite/crm_best.pt`).
CRM (westd run): `crm_pi05_unified_3suite/crm_best.pt`. K=2, norm=0.05.

| exp_id | SR |
|--------|-----|
| pi05-crm-k2-goal-s42-bjb1-r2 | 82.5% |
| pi05-crm-k2-goal-s43-bjb1-r2 | 83.0% |
| pi05-crm-k2-goal-s44-bjb1-r2 | 85.0% |
| westd-pi05-crm-k2-goal-s42 | 85.5% |

### 1.9 Pi05 Adaptive Spatial/Object (DONE/success)

CRM: `crm_pi05_unified_3suite/crm_best.pt`. K=2, norm=0.2.

**Spatial Adaptive:**
| exp_id | tau | SR |
|--------|-----|-----|
| pi05-adaptive-spatial-s42-bjb2-r2 | 0.25 | 96.5% |
| pi05-adaptive-spatial-s42-tau015-bjb2 | 0.15 | 97.0% |
| pi05-adaptive-spatial-s42-tau035-bjb2 | 0.35 | 96.5% |
| pi05-adaptive-spatial-s43-bjb2-r2 | 0.25 | 98.0% |
| pi05-adaptive-spatial-s44-bjb2-r2 | 0.25 | 97.0% |

**Object Adaptive:**
| exp_id | tau | SR |
|--------|-----|-----|
| pi05-adaptive-object-s42-cqa1 | 0.25 | 85.5% |
| pi05-adaptive-object-s43-bjb2-24035 | 0.25 | 83.0% |
| pi05-adaptive-object-s43-cqa1-r3 | 0.25 | 85.0% |
| pi05-adaptive-object-s44-cqa1-r3 | 0.25 | 88.0% |

---

## 2. SmolVLA Table 1 Experiments - K Values

### Summary of K values by experiment type

| Experiment Type | K Value(s) | tau | norm | Notes |
|----------------|------------|-----|------|-------|
| crm-always-on-object/spatial/goal/long | **K=2** | 0.001 | 0.2 | All seeds consistent |
| eval-adaptive-* (d149 series) | **K=2** | 0.25 | 0.2 | Main adaptive results |
| eval-crm-goal (d149) | **K=10** | - | 0.05 | CRM obs_only mode |
| eval-crm-long (d149) | **K=10** | - | 0.05 | CRM obs_only mode |
| eval-crm-spatial (k10) | **K=10** | - | 0.2 | CRM obs_only mode |
| eval-crm-object (k20) | **K=20** | - | 0.2 | CRM obs_only mode |
| eval-obs-only-object (default) | **K=10** | - | varies | Dominant config |
| eval-obs-only-object (norm003/005/01) | **K=10** or **K=20** | - | 0.03/0.05/0.1 | Norm sweeps |
| eval-obs-only-spatial (norm02-k5) | **K=5** | - | 0.2 | Spatial ablation |
| eval-obs-only-spatial (k10) | **K=10** | - | 0.2 | Spatial default |
| eval-obs-only-goal (norm02) | **K=10** | - | 0.2 | Goal obs_only |
| eval-random-selection-object | **K=5** or **K=10** | - | varies | Random baseline |
| eval-vla-only-goal/spatial/object | **K=1** | - | - | No CRM, baseline |
| eval-vla-only-long | K not set (N/A) | - | - | Pure baseline |

### SmolVLA CRM Checkpoint Paths

Primary checkpoint for most SmolVLA experiments:
```
/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt
```
Used by 213 experiments (majority of Table 1 evals).

Secondary checkpoints:
```
/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt
```
Used by 235+ experiments (supplementary evals, tau sweeps, adaptive experiments).

```
/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt
```
Used by 67 experiments (per-DOF ablation evals).

```
/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt
```
Used by 14 experiments (supplementary s47 series, long CRM s42-s47).

Other checkpoints (less common):
- `/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt` (10 exps, scalar uncertainty ablation)
- `/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt` (12 exps, K=1 CRM)
- `/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt` (2 exps, K=1 multiscale)
- `/root/autodl-tmp/checkpoints/crm_k1_accg_full/crm_best.pt` (ACCG variant)
- `/root/autodl-tmp/checkpoints/crm_openvla_k1_multiscale/object/crm_k1_best.pt` (2 exps, OpenVLA)
- `/root/autodl-tmp/checkpoints/crm_openvla_obs_only/crm_best.pt` (1 exp, OpenVLA)
- `/root/autodl-tmp/checkpoints/crm_lto_splitA_fixed/` (leave-task-out)

---

## 3. SmolVLA Long Supplementary Experiments (s45, s46)

### eval-supp-long-adapt-tau025-s45

**Status: DONE / success**

| Parameter | Value |
|-----------|-------|
| SR | 0.60 (120/200) |
| K | 2 |
| tau | 0.25 |
| max_correction_norm | 0.2 |
| CRM checkpoint | `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` |
| server | bjb1-18228 |
| seed | 45 |
| model | smolvla |
| mode | adaptive_conformal_crm |
| benchmark | long |
| n_rollouts | 20 |
| created_at | 2026-05-23T20:12:41.239Z |
| completed_at | 2026-05-24T00:53:11.757Z |

**Command:**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --K 2
```

### eval-supp-long-adapt-tau025-s46

**Status: DONE / success**

| Parameter | Value |
|-----------|-------|
| SR | 0.585 (117/200) |
| K | 2 |
| tau | 0.25 |
| max_correction_norm | 0.2 |
| CRM checkpoint | `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` |
| server | bjb1-18228 |
| seed | 46 |
| model | smolvla |
| mode | adaptive_conformal_crm |
| benchmark | long |
| n_rollouts | 20 |
| created_at | 2026-05-24T00:55:46.960Z |
| completed_at | 2026-05-24T08:05:01.126Z |
| log_path | `/root/acr-vla-conformal-refinement/logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed46.json` |
| checkpoint_path (registry) | `/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt` (likely stale/incorrect -- command clearly uses 3suite_v1) |

**Command:**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && python -u src/evaluate.py --model smolvla --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold 0.25 --benchmark long --seed 46 --n_rollouts 20 --max_correction_norm 0.2 --K 2
```

### All eval-supp-long-adapt-tau025 experiments

| exp_id | status | conclusion | SR | trigger_rate |
|--------|--------|------------|-----|-------------|
| eval-supp-long-adapt-tau025-s42 | DEPLOYED | success | 0.59 | 0.039 |
| eval-supp-long-adapt-tau025-s43 | DEPLOYED | negative | 0.58 | 0.045 |
| eval-supp-long-adapt-tau025-s44 | DONE | negative | 0.56 | 0.049 |
| eval-supp-long-adapt-tau025-s45 | DONE | success | 0.60 | - |
| eval-supp-long-adapt-tau025-s46 | DONE | success | 0.585 | - |
| eval-supp-long-adapt-tau025-s46-r2 | DONE | killed | - | - |
| eval-supp-long-adapt-tau025-s47 | DONE | failed | - | - |
| eval-supp-long-adapt-tau025-s47-r2 | DONE | negative | 0.55 | 0.037 |

---

## 4. SmolVLA Supplementary Goal Adaptive Experiments

CRM: `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` (s45-s46) or `crm_unified_4suite_r4/crm_best.pt` (s47). K=2, tau=0.25, norm=0.2.

| exp_id | SR | trigger_rate | CRM |
|--------|-----|-------------|-----|
| eval-supp-goal-adapt-tau025-s42 | 84.0% | 8.3% | (not in command) |
| eval-supp-goal-adapt-tau025-s45 | 81.0% | 9.4% | crm_smolvla_3suite_v1 |
| eval-supp-goal-adapt-tau025-s46 | 83.5% | 9.09% | crm_smolvla_3suite_v1 |
| eval-supp-goal-adapt-tau025-s47 | 82.0% | - | crm_unified_4suite_r4 |

---

## 5. SmolVLA Supplementary Long CRM Always-On Experiments

CRM: `/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt`. K=10 (where specified), norm=0.05.

| exp_id | conclusion | SR |
|--------|------------|-----|
| eval-supp-long-crm-norm005-s42 | negative | 56.5% |
| eval-supp-long-crm-norm005-s43 | negative | 54.5% |
| eval-supp-long-crm-norm005-s44 | success | 56.5% |
| eval-supp-long-crm-norm005-s45 | success | 60.5% |
| eval-supp-long-crm-norm005-s46 | success | 54.0% |
| eval-supp-long-crm-norm005-s47 | success | 56.5% |

---

## 6. CRM Training Provenance Summary

### Pi05 CRM Models

| Checkpoint Path | Training Exp | Status | Data |
|-----------------|-------------|--------|------|
| `crm_pi05_unified_3suite/crm_best.pt` | train-crm-pi05-unified-3suite-r2 | failed(!) | Spatial+Goal+Object, obs_dim=2048, ~194K samples |
| `crm_pi05_full/object/crm_best.pt` | crm-train-pi05-object-full | success | 69303 object samples, K=10 |
| `crm_pi05_full/spatial/crm_best.pt` | crm-train-pi05-spatial-v2 | success | 60250 spatial samples, K=10 |
| `crm_pi05_k1_multiscale/goal/` | train-crm-pi05-goal-k1 | success | K=1, obs_dim=2048 |
| `crm_pi05_k1_multiscale/spatial/` | train-crm-pi05-spatial-k1 | success | K=1, obs_dim=2048 |

Note: The unified 3-suite training had `r1` killed and `r2` failed, but the checkpoint file still exists and is used by all pi05 eval experiments. It may have been produced by an earlier successful run or partial training.

### SmolVLA CRM Models

| Checkpoint Path | Training Exp | Status | Data |
|-----------------|-------------|--------|------|
| `crm_v3_norm/obs_only/crm_best.pt` | crm-train-v3-norm-obs-only | success | Obs-only with normalization |
| `crm_v3_norm/perdof/crm_best.pt` | crm-train-v3-norm | success | Per-DOF with normalization |
| `crm_v3_norm/scalar_unc/crm_best.pt` | crm-train-v3-norm-scalar-unc | success | Scalar uncertainty with normalization |
| `crm_smolvla_3suite_v1/crm_best.pt` | train-crm-smolvla-3suite-v1 | success | Object+Spatial+Goal, 77835 samples, K=10 |
| `crm_unified_4suite_r4/crm_best.pt` | train-crm-unified-4suite-r6 | success | Object+Spatial+Goal+Long |
| `crm_k1/crm_best.pt` | plan_701-crm-k1-train | success | K=1 single-sample CRM |
| `crm_k1_accg_full/crm_best.pt` | train-crm-k1-accg-object-seed42-full | success | K=1 ACCG architecture |
| `crm_lto_splitA_fixed/` | crm-lto-splitA-train-fixed | success | Leave-task-out Split A |
| `crm_openvla_obs_only/crm_best.pt` | train-crm-openvla-obs-only | success | OpenVLA features, obs_dim=4096 |
| `crm_openvla_k1_multiscale/object/crm_k1_best.pt` | crm-train-openvla-k1-multiscale-object | success | OpenVLA K=1 multiscale |

---

## 7. Key Parameter Defaults for Reproduction

### SmolVLA Experiments
- **VLA-only baseline**: K=1, no CRM
- **CRM obs_only (Table 1)**: K=10, norm=0.05, CRM=`crm_v3_norm/obs_only/crm_best.pt`
- **CRM always-on**: K=2, tau=0.001, norm=0.2, CRM=`crm_smolvla_3suite_v1/crm_best.pt`
- **Adaptive (tau-gated)**: K=2, tau=0.25, norm=0.2, CRM=`crm_smolvla_3suite_v1/crm_best.pt`
- **Obs-only object (norm sweep)**: K=10 or K=20, norm=0.03/0.05/0.1/0.2

### Pi05 Experiments
- **VLA-only baseline**: K varies (1 or 10 or unset), no CRM
- **CRM obs_only**: K=2, norm=0.05, CRM=`crm_pi05_unified_3suite/crm_best.pt`
- **CRM always-on**: K=2, tau=0.001, norm=0.2, CRM=`crm_pi05_unified_3suite/crm_best.pt`
- **Adaptive (tau-gated)**: K=2, tau=0.25, norm=0.2, CRM=`crm_pi05_unified_3suite/crm_best.pt`
