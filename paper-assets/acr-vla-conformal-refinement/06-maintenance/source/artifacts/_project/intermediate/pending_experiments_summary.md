# Pending Experiments Summary

> Updated: 2026-05-29 | Post-audit revision (C1-C3 fixed, duplicates removed, adaptive ε added)

## Audit Fixes Applied

| Issue | Description | Resolution |
|-------|-------------|------------|
| C1 | π₀.₅ obs_dim=960 | **Deleted** — all 3 pi05 configs removed (already completed in registry) |
| C2 | π₀.₅ CRM checkpoint wrong | **Deleted** — same reason; correct path is `crm_pi05_unified_3suite/crm_best.pt` |
| C3 | K=10 vs paper K=2 | **Fixed** — remaining CRM configs corrected to K=2. K=10 was for CRM training data, not eval |
| W1 | SmolVLA adaptive Long s45/s46 | **Deleted** — already completed (SR=60.0%, 58.5%) |

### Removed Configs (5 duplicates of completed experiments)

| Config | Registry Match | Status | SR |
|--------|---------------|--------|-----|
| pi05_goal_adaptive_s44 | pi05-adaptive-goal-s44-backfill | DONE | 86.5% |
| pi05_crm_long_s42 | pi05-crm-always-on-long-s42 | DONE | 77.0% |
| pi05_crm_long_s43 | pi05-crm-always-on-long-s43 | DONE | 79.5% |
| smolvla_adaptive_long_s45 | eval-supp-long-adapt-tau025-s45 | DONE | 60.0% |
| smolvla_adaptive_long_s46 | eval-supp-long-adapt-tau025-s46 | DONE | 58.5% |

### K Value Clarification

| Context | K value | Purpose |
|---------|---------|---------|
| CRM training data generation | K=10 | Generate diverse samples for training CRM |
| Table 1 eval: CRM always-on | **K=2** | Two VLA forward passes, argmin + CRM correction |
| Table 1 eval: τ-gated adaptive | **K=2** | Two VLA forward passes, d₂ gating + CRM correction |
| Table 1 eval: VLA-only | **K=1** | Single forward pass, no CRM |

---

## Group 1: SmolVLA Long n=5 Extension (4 experiments)

Extends Table 1 Long from n=3 (s42/s43/s44) to n=5. Adaptive Long s45/s46 already completed (see above), so only VLA-only and CRM always-on remain.

| Experiment ID | Mode | Seed | K | Est. GPU-hrs |
|---|---|---|---|---|
| smolvla-vla-only-long-s45 | vla_only | 45 | 1 | 1.0 |
| smolvla-vla-only-long-s46 | vla_only | 46 | 1 | 1.0 |
| smolvla-crm-long-s45 | crm_obs_only (always-on) | 45 | 2 | 1.5 |
| smolvla-crm-long-s46 | crm_obs_only (always-on) | 46 | 2 | 1.5 |

**Subtotal: 5.0 GPU-hours**

### What this enables
- Long n=5 for all three methods (VLA-only, CRM always-on, τ-gated adaptive)
- Narrows CI on the highest-variance suite (std=2.3 for adaptive)
- Addresses reviewer Q4 statistical power concern

---

## Group 2: Adaptive Epsilon Validation (2 experiments)

Tests the adaptive ε mechanism: `ε_adaptive = ε_max × min(d₂/τ, 1.0)`.

**Prerequisite:** Apply `artifacts/patch_adaptive_epsilon.py` (or manual changes per `artifacts/patch_adaptive_epsilon_manual.md`).

| Experiment ID | Suite | Seed | Est. GPU-hrs | Baseline |
|---|---|---|---|---|
| smolvla-adaptive-eps-spatial-s42 | Spatial | 42 | 1.0 | τ-gated: 80.8%, VLA-only: 79.3% |
| smolvla-adaptive-eps-object-s42 | Object | 42 | 1.0 | τ-gated: 77.8%, VLA-only: 77.7% |

**Subtotal: 2.0 GPU-hours**

### What this tests
- **Spatial** (trigger ~20%): Many near-threshold steps that could benefit from proportional vs binary correction
- **Object** (trigger ~4%): Tests whether soft gating preserves baseline even better than binary gating

### Expected outcomes
- Spatial: SR ≥ 80% (at least matches τ-gated; could improve if near-threshold steps benefit from partial correction)
- Object: SR ≈ 77.7% (baseline preservation; soft gating should be at least as conservative as binary)

---

## Total Resource Estimate

| Group | Experiments | GPU-hours | Can Parallelize |
|---|---|---|---|
| Long n=5 extension | 4 | 5.0 | Yes (independent seeds) |
| Adaptive ε validation | 2 | 2.0 | Yes (independent suites) |
| **Total** | **6** | **7.0** | |

With 2 GPUs: ~3.5 hours wall time. With 4 GPUs: ~2 hours wall time.

## Key Parameters (all experiments)

| Parameter | Value |
|---|---|
| Model | SmolVLA (0.4B) |
| CRM checkpoint | crm_smolvla_3suite_v1/crm_best.pt |
| obs_dim | 960 |
| K (CRM modes) | 2 |
| max_correction_norm (ε) | 0.2 |
| conformal_threshold (τ) | 0.25 (adaptive), 0.001 (always-on) |
| n_rollouts | 20 |

## Deployment Checklist

- [ ] Server accessible
- [ ] GPU allocated by Director
- [ ] Conda env verified: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- [ ] CRM checkpoint present: `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`
- [ ] Project code synced: `cd /root/acr-vla-conformal-refinement && git pull`
- [ ] (adaptive-eps only) Patch applied: `python artifacts/patch_adaptive_epsilon.py`
- [ ] Run: `bash artifacts/pending_experiments/run_pending_experiments.sh [long-n5|adaptive-eps|all] [experiment_id]`
