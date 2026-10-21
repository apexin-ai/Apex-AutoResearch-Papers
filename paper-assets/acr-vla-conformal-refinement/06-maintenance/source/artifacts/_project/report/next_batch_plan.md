# Next-Batch Experiment Plan (Post Current Batch)

## Current Batch Status (Running)

| Experiment | Server/GPU | Plan ID | What it covers |
|-----------|-----------|---------|----------------|
| eval-spatial-v6-full | bjb1 cuda:0 | plan_001 (eval) | VLA-only baseline on spatial |
| eval-acr-spatial-v2 | bjb1 cuda:1 | plan_001 (eval) | ACR-VLA on spatial |
| eval-reconvla-spatial-v3 | bjb1 cuda:2 | plan_014 | ReconVLA baseline on spatial |
| crm-train-a3-obs-only | bjb1 cuda:3 | plan_002 (train) | A3 ablation CRM training |
| eval-object-v5-full | bjb2 cuda:0 | plan_001 (eval) | VLA-only on object |

## Plan Coverage After Current Batch

| Plan | Status | Gap |
|------|--------|-----|
| plan_000 MVP | ✅ DONE | — |
| plan_001 Full pipeline | CRM ✅, spatial eval ✅, **object ACR-VLA eval MISSING** | Need eval-acr-object, eval-reconvla-object |
| plan_002 A3 obs_only | Training ✅, **eval MISSING** | Need eval-a3-obs-only-spatial |
| plan_003 A4 scalar | ❌ NOT STARTED | Need `--input_mode scalar` code + train + eval |
| plan_004 SRPO stacking | ❌ NOT STARTED | Needs SRPO checkpoint (external dep) |
| plan_005 COC validation | ❌ NOT STARTED | Needs COC logging in eval pipeline |
| plan_014 ReconVLA | spatial ✅, **object MISSING** | Need eval-reconvla-object |
| plan_015 K sensitivity | K=5 cache ✅, **train+eval MISSING** | Need CRM train K=5, then eval |
| plan_006-013, 016 | ❌ NOT STARTED | Lower priority |

---

## Scenario A: Spatial Results POSITIVE (ACR-VLA > VLA-only ≥ 5%)

### Wave 1 — Immediate (all can run in parallel, 4 GPU on bjb1)

#### 1. eval-a3-obs-only-spatial ⭐ MAKE-OR-BREAK
- **Plan ID**: plan_002 (eval phase)
- **Hypothesis**: CRM without conformal features (obs_only) performs significantly worse than full ACR-VLA, proving per-DOF conformal features are necessary
- **Kill criterion**: If obs_only ≥ full ACR-VLA - 2% → Claim 1 fails
- **Command sketch**:
  ```bash
  python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 \
    --crm_checkpoint /root/autodl-tmp/checkpoints/crm/obs_only/crm_best.pt
  ```
- **GPU**: bjb1 cuda:0, ~2-3h
- **Blocker**: crm-train-a3-obs-only must finish first

#### 2. eval-acr-object-v1
- **Plan ID**: plan_001 (eval, object benchmark)
- **Hypothesis**: ACR-VLA improvement generalizes from spatial to object benchmark
- **Command sketch**:
  ```bash
  python -u src/evaluate.py --mode acr_vla --benchmark object --n_rollouts 10 --seed 42 --K 10 \
    --crm_checkpoint /root/autodl-tmp/checkpoints/crm/crm_best.pt
  ```
- **GPU**: bjb1 cuda:1 OR bjb2 cuda:0, ~2-3h
- **Dep**: None (crm_best.pt already exists, object precompute cache exists)

#### 3. eval-reconvla-object-v1
- **Plan ID**: plan_014 (object extension)
- **Hypothesis**: ReconVLA scalar selection also improves on object, but less than ACR-VLA
- **Command sketch**:
  ```bash
  python -u src/evaluate.py --mode reconvla --benchmark object --n_rollouts 10 --seed 42 --K 10
  ```
- **GPU**: bjb1 cuda:2 OR bjb2 cuda:0, ~2-3h
- **Dep**: None

#### 4. crm-train-k5 + eval (plan_015 partial)
- **Plan ID**: plan_015 (K sensitivity, first data point K=5)
- **Hypothesis**: K=5 degrades per-DOF feature quality due to worse covariance estimation → lower ACR-VLA success
- **Command sketch**:
  ```bash
  # Train
  python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 512 --lr 0.016 \
    --K 5 --seed 42 --cache_dir /root/autodl-tmp/crm_cache_k5/ \
    --output_dir /root/autodl-tmp/checkpoints/crm/k5/
  # Eval (after training)
  python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 5 \
    --crm_checkpoint /root/autodl-tmp/checkpoints/crm/k5/crm_best.pt
  ```
- **GPU**: bjb1 cuda:3, ~1h train + ~2-3h eval
- **Dep**: precompute-k5 ✅ already done

**Wave 1 总结**: 4 experiments, 4 GPU parallel, ~3h wall time

### Wave 2 — After Wave 1 (need code changes or external deps)

#### 5. A4 scalar ablation (plan_003) ⚠️ NEEDS CODE
- **Plan ID**: plan_003
- **Hypothesis**: CRM with scalar uncertainty (single Euclidean distance) performs worse than per-DOF (40D features), validating structured > scalar
- **What's needed**:
  1. Implement `--input_mode scalar` in train_crm.py (replace 40D per-DOF features with 1D Euclidean distance per chunk, ~30D total input reduction)
  2. Modify precompute to also save scalar nonconformity scores (or derive from existing cache)
  3. Train CRM with scalar input
  4. Eval on spatial + object
- **Command sketch**:
  ```bash
  # Train
  python -u src/train_crm.py --benchmark spatial object --epochs 50 --batch_size 512 --lr 0.016 \
    --K 10 --seed 42 --input_mode scalar \
    --output_dir /root/autodl-tmp/checkpoints/crm/scalar/
  # Eval
  python -u src/evaluate.py --mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10 \
    --crm_checkpoint /root/autodl-tmp/checkpoints/crm/scalar/crm_best.pt --crm_input_mode scalar
  ```
- **GPU**: 1 GPU, ~1h code + ~1h train + ~3h eval
- **Dep**: Code changes required

#### 6. K=15, K=20 precompute + train + eval (plan_015 completion)
- **Plan ID**: plan_015
- **Hypothesis**: K=15/20 improves covariance estimation → better per-DOF features, but diminishing returns + inference cost
- **Command sketch**:
  ```bash
  # Precompute K=15
  python -u src/train_crm.py --precompute --benchmark spatial object --K 15 \
    --cache_dir /root/autodl-tmp/crm_cache_k15/
  # Precompute K=20
  python -u src/train_crm.py --precompute --benchmark spatial object --K 20 \
    --cache_dir /root/autodl-tmp/crm_cache_k20/
  ```
- **GPU**: 2-3 GPU for precompute (~2h each), then 1 GPU each for train + eval
- **Dep**: None, but heavy GPU time (~15h total for K=15+20 precompute+train+eval)

#### 7. COC signal validation (plan_005)
- **Plan ID**: plan_005
- **Hypothesis**: COC coverage fraction correlates with task success (Spearman ρ > 0.3), ACI converges, ellipsoid volume shrinks vs static
- **What's needed**: Eval logging needs to dump per-step COC scores + per-episode success. May need eval code changes.
- **GPU**: Reuses eval runs with extra logging, ~3h per benchmark
- **Dep**: Code changes for COC logging

#### 8. SRPO stacking (plan_004) ⚠️ EXTERNAL DEP
- **Plan ID**: plan_004
- **Hypothesis**: ACR-VLA + SRPO > SRPO alone on LIBERO-Plus (≥2% gain)
- **Blockers**:
  1. Need SRPO checkpoint (public release or reproduce training)
  2. Need LIBERO-Plus benchmark setup
  3. Need new precompute with SRPO base model
  4. Need new CRM training on SRPO features
- **GPU**: ~18h total (precompute + train CRM + eval LIBERO-Plus)
- **Status**: Deferred until SRPO checkpoint sourced

### Wave 3 — Paper-strengthening (P1-P2)

| # | Exp ID suggestion | Plan | Hypothesis | GPU | Can parallel? |
|---|------------------|------|-----------|-----|--------------|
| 9 | eval-held-out-perturbation | plan_016 | CRM trained without camera augmentation still improves on camera perturbation (conformal features, not memorization) | 1 GPU, ~8h | Yes |
| 10 | eval-no-aci-spatial | plan_006 | Static CGS without ACI degrades under distribution shift | 1 GPU, ~3h | Yes |
| 11 | eval-aci-no-crm-spatial | plan_007 | ACI+COC+sample-selection (no CRM) improves over ReconVLA but less than full ACR-VLA | 1 GPU, ~3h | Yes with #10 |
| 12 | feature-importance-analysis | plan_012 | CRM gradient analysis shows dimension-selective attention to high-uncertainty DOFs | 0.5h, CPU ok | After plan_008 |
| 13 | eval-diu-features | plan_011 | DiU aleatoric features perform worse than CGS epistemic; combined 52D may improve | 1 GPU, ~10h | Yes |

---

## Scenario B: Spatial Results NEGATIVE (ACR-VLA ≤ VLA-only or < 3% gain)

### Diagnostic Wave — Before proceeding with any more experiments

#### D1. Per-task breakdown analysis
- **Exp ID**: diag-per-task-spatial
- **Purpose**: Identify if ACR-VLA hurts specific tasks or fails uniformly
- **Method**: Parse eval JSON, compute per-task success rates, compare ACR-VLA vs VLA-only per task
- **GPU**: 0 (analysis only)
- **Immediate action**: Check if CRM corrections are too aggressive on easy tasks

#### D2. CRM residual magnitude analysis
- **Exp ID**: diag-crm-residual
- **Purpose**: Check if CRM is applying corrections that are too large, overshoot ground truth
- **Method**: Run eval with residual logging, plot |CRM correction| vs |needed correction| per DOF
- **GPU**: 1 GPU, ~1h (modified eval with logging)
- **Code needed**: Add residual magnitude logging to evaluate.py

#### D3. A3 obs_only eval (STILL CRITICAL)
- Same as Scenario A #1 — if obs_only ≈ full ACR-VLA, the conformal features aren't helping
- If obs_only < full ACR-VLA < VLA-only → CRM itself is harmful, conformal features just less harmful

#### D4. CRM temperature/scaling sweep
- **Exp ID**: diag-crm-scaling
- **Purpose**: Test if CRM corrections need to be scaled down (α * CRM_output, α ∈ {0.1, 0.3, 0.5, 0.7})
- **Method**: Modify eval to scale CRM residual by α
- **GPU**: 1 GPU, ~1h per α value
- **Rationale**: CRM trained on offline data may produce corrections too large for closed-loop execution

#### D5. Retrain CRM with L2 regularization / lower lr
- **Exp ID**: crm-train-v2-regularized
- **Purpose**: Reduce CRM overfitting to training distribution
- **Command sketch**:
  ```bash
  python -u src/train_crm.py --benchmark spatial object --epochs 100 --batch_size 512 \
    --lr 0.004 --K 10 --seed 42 --weight_decay 0.01 \
    --output_dir /root/autodl-tmp/checkpoints/crm/v2_reg/
  ```
- **GPU**: 1 GPU, ~1h

#### D6. Verify precompute-eval consistency
- **Purpose**: Ensure eval-time CGS computation matches training-time precompute (same K, same sampling, same normalization)
- **Method**: Run eval with `--debug_conformal` flag, compare features against cached training features for same demo
- **GPU**: 0.5h

### Decision tree after diagnostics:

```
If D1 shows task-specific failure:
  → Investigate failing tasks, check if CRM training data covers those tasks
  → Consider task-conditional CRM or per-task evaluation

If D2 shows oversized corrections:
  → D4 scaling sweep → find optimal α → re-evaluate
  → If α < 0.3 works → CRM is poorly calibrated, need better training signal

If D3 shows obs_only ≈ full:
  → Conformal features not informative in LIBERO context
  → Pivot: try different feature engineering (raw covariance entries, per-DOF ranking)

If D6 shows mismatch:
  → Fix consistency bug → re-evaluate before any other conclusion
```

---

## Resource Summary

### Scenario A (positive) total GPU budget:
| Wave | GPU-hours | Wall time (4 GPU parallel) |
|------|-----------|---------------------------|
| Wave 1 | ~12h | ~3h |
| Wave 2 (#5-7) | ~20h | ~6h |
| Wave 2 (#8 SRPO) | ~18h | blocked on checkpoint |
| Wave 3 | ~25h | ~8h |
| **Total** | **~75h** | **~17h + SRPO** |

### Scenario B (negative) diagnostic budget:
| Diagnostic | GPU-hours | Wall time |
|-----------|-----------|-----------|
| D1-D2 analysis | ~1h | ~1h |
| D3 obs_only eval | ~3h | ~3h |
| D4 scaling sweep (4 values) | ~4h | ~1h (parallel) |
| D5 retrain | ~1h | ~1h |
| D6 consistency check | ~0.5h | ~0.5h |
| **Total** | **~9.5h** | **~6.5h** |

---

## Recommended Execution Order

**Regardless of spatial result**, the FIRST thing to do when GPUs free up:

1. ⭐ **eval-a3-obs-only-spatial** — make-or-break, determines if the entire per-DOF story holds
2. **eval-acr-object-v1** + **eval-reconvla-object-v1** — complete the 3-way comparison on second benchmark
3. **crm-train-k5** — cheap, K=5 cache already exists

Then branch based on spatial results.

**Object benchmark ACR-VLA eval does NOT need new precompute** — existing precompute-v4 already includes object (14570 samples). The eval-time CGS is computed online from K flow-matching samples, not from the training cache.
