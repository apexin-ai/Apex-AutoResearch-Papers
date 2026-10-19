# Experiment Utilization Audit: diff_collision_sdf

**Date:** 2026-05-28
**Scope:** 72 registry experiments (all conclusion=success) vs. paper tex files

---

## 1. Paper-Referenced Experiments

### 1.1 Claim 1 — Action-Collapse Diagnosis (claim1.tex)

| Registry exp_id | Paper reference | Value used |
|----------------|----------------|------------|
| `eval_a1_lora_object_v11` | tab:fake_safety, Pi0+A1 row | CAR=91.5%, TSR=0%, collapsed=99.6% (800 ep aggregate) |
| `eval_pi05_safelibero_object_v11_s1` | tab:fake_safety, Pi0.5 row | CAR=25% (one of multi-seed) |
| `eval_pi05_safelibero_object_v11_s2` | tab:fake_safety, Pi0.5 row | CAR=27.5% (one of multi-seed) |

**Note:** Pi0 Full-FT (83%), Pi0 LoRA (82%), and Pi0.5 seed 0 (to get 28.5% mean) results appear in the paper but have **no matching registry experiments** — see §5 Provenance Gaps.

### 1.2 Claim 2 — Oracle SDF Refinement (claim2.tex)

| Registry exp_id | Paper reference | Value used |
|----------------|----------------|------------|
| *(none)* | tab:oracle | Oracle-adaptive 75%, Oracle-fixed 73.1%, Oracle-feature 76.9%, A3 77.1% |

**Note:** All oracle and A3 eval results in claim2 have **no matching registry experiments** — see §5.

### 1.3 Claim 3 — Avoidance Source Attribution (claim3.tex)

| Registry exp_id | Paper reference | Value used |
|----------------|----------------|------------|
| `eval_lora_baseline_30k_s0_reeval` | tab:avoidance_source, LoRA s0 | CAR=56.5% |
| `reeval_lora_s1_30k` | tab:avoidance_source, LoRA s1 | CAR=52.5% |
| `eval_lora_s2_30k_v2` | tab:avoidance_source, LoRA s2 | CAR=55.0% |
| `reeval_sdf_s0_l005_30k` | tab:avoidance_source, λ=0.005 s0 | CAR=57.0% |
| `reeval_sdf_s1_l005_30k` | tab:avoidance_source, λ=0.005 s1 | CAR=54.0% |
| `reeval_sdf_s2_l005_30k` | tab:avoidance_source, λ=0.005 s2 | CAR=52.5% |
| `reeval_sdf_s0_l01_30k` | tab:avoidance_source, λ=0.01 s0 | CAR=57.0% |
| `reeval_sdf_s1_l01_30k` | tab:avoidance_source, λ=0.01 s1 | CAR=57.5% |
| `reeval_sdf_s2_l01_30k` | tab:avoidance_source, λ=0.01 s2 | CAR=54.5% |
| `eval_pi05_a1_30k_s0_l01_high` | tab:avoidance_source, λ=0.1 s0 | CAR=58.0% |
| `eval_pi05_a1_30k_s1_l01_high` | tab:avoidance_source, λ=0.1 s1 | CAR=58.5% |
| `eval_pi05_a1_30k_s2_l01_high` | tab:avoidance_source, λ=0.1 s2 | CAR=54.5% |

Phase 2 ablation (claim3 body):
| `train_pi05_phase2_lambda0_s2` | claim3 body text | Phase 2 λ=0 training |
| `eval_phase2_lambda0_s2` | claim3 body text | CAR=57.5% at 18K (single seed s2) |

### 1.4 Appendix

| Registry exp_id | Paper reference | Value used |
|----------------|----------------|------------|
| `analysis_threshold_sensitivity` | tab:dfcar_threshold | dfCAR invariant across τ_d ∈ [2, 200] mm |
| `eval_stepwise_s0_l1_22k` | tab:stepwise_lambda01 | 22K: CAR=60.5% |
| `eval_stepwise_s0_l1_26k_v2` | tab:stepwise_lambda01 | 26K: CAR=53.5% |
| `eval_multiseed_lora_s0_eseed0` | tab:eval_seed_robustness | LoRA s0 eseed=0: CAR=53.0% |
| `eval_multiseed_lora_s0_eseed42` | tab:eval_seed_robustness | LoRA s0 eseed=42: CAR=56.5% |
| `eval_multiseed_lora_s0_eseed99` | tab:eval_seed_robustness | LoRA s0 eseed=99: CAR=57.5% |
| `eval_multiseed_lora_s0_eseed123` | tab:eval_seed_robustness | LoRA s0 eseed=123: CAR=53.0% |
| `eval_multiseed_sdf_l01_s0_eseed0` | tab:eval_seed_robustness | SDF λ=0.01 eseed=0: CAR=52.5% |
| `eval_multiseed_sdf_l01_s0_eseed99` | tab:eval_seed_robustness | SDF λ=0.01 eseed=99: CAR=57.0% |
| `eval_multiseed_sdf_l01_s0_eseed42` | tab:eval_seed_robustness | SDF λ=0.1 eseed=42: CAR=59.0% |
| `eval_multiseed_sdf_l01_s0_eseed123` | tab:eval_seed_robustness | SDF λ=0.1 eseed=123: CAR=58.5% |
| `eval_spatial_bowl_lora_ctrl_s0_v2` | tab:spatial_bowl | LoRA-only spatial: CAR=12.0% |

### 1.5 Training Experiments (indirectly used for hyperparameters/training protocol)

22 training experiments provide training loss data and underpin the appendix training details section:
`baseline_spatial_bowl_s0_v2`, `baseline_object_pudding_s0_v2`, `a3_gradient_spatial_bowl_s0`, `a3_gradient_object_pudding_s0`, `baseline_lora_spatial_bowl_s0`, `baseline_lora_object_pudding_s0`, `a1_lora_object_pudding_s0`, `a1_lora_spatial_bowl_s0`, `train_pi05_a1_obj_s0_l01`, `train_pi05_a1_obj_s0_l005`, `train_pi05_a1_obj_s1_l005`, `train_pi05_a1_obj_s1_l01`, `train_pi05_a1_obj_s2_l005`, `train_pi05_a1_obj_s2_l01`, `train_pi05_lora_baseline_s0`, `train_pi05_lora_baseline_s1`, `train_pi05_a1_spatial_bowl_s0_l005`, `train_pi05_a1_obj_s0_l01_high`, `train_pi05_a1_obj_s1_l01_high`, `train_pi05_a1_obj_s2_l01_high`, `train_spatial_bowl_lora_control_s0`, `train_pi05_lora_baseline_s2_resume`

**Summary: 51 of 72 experiments are directly or indirectly referenced in the paper.**

---

## 2. Unused Experiments with Potential Value

### 2.1 `eval_multiseed_sdf_l01_s0_eseed256` — 4th eval seed for λ=0.1

- **Data:** CAR=57.0%, TSR=48.0%, 50 episodes, eval_seed=256
- **Current paper gap:** tab:eval_seed_robustness shows 5 eval seeds for LoRA but only 3 for SDF λ=0.1 (seeds 7, 42, 123). This asymmetry is noticeable.
- **Recommendation:** **Add to appendix table.** Including eseed=256 would give 4 eval seeds for λ=0.1 (mean CAR = 58.1→57.9%), reducing the asymmetry. Alternatively, add both eseed=0 and eseed=256 for full 5-way symmetry (but eseed=0 eval for λ=0.1 was never run — only for λ=0.01).
- **Priority: HIGH** — easy win, data already exists.

### 2.2 `reeval_lora_s0_30k_v2` — Run-to-run stochastic variance

- **Data:** LoRA s0, eval_seed=7, CAR=57.0%, TSR=46.0%
- **Current paper uses:** `eval_lora_baseline_30k_s0_reeval` for the same model/seed giving CAR=56.5%, TSR=51.5%
- **Significance:** Two runs of the identical model/seed/eval_seed produce 0.5 pp CAR difference and 5.5 pp TSR difference. This quantifies **run-to-run evaluation noise**, which is directly relevant to the MDE discussion (current MDE ≈ 5 pp at n=3).
- **Recommendation:** Mention in limitations or appendix as evidence that evaluation itself contributes ~0.5–5.5 pp noise, further justifying why 2.3 pp effects are undetectable.
- **Priority: MEDIUM** — strengthens the statistical argument but requires careful framing.

### 2.3 `train_phase2_lambda0_extra_seed` — 2nd seed for Phase 2 ablation

- **Data:** Phase 2 Stage 1 training (seed 0, λ=0.005, 10K steps)
- **Current paper gap:** Phase 2 ablation is single-seed (s2 only, CAR=57.5%). This is explicitly flagged as a limitation.
- **Status:** Training completed, but **no eval experiment registered.** If evaluation was conducted, the data should be added.
- **Recommendation:** If eval data exists somewhere, add it to claim3 to upgrade Phase 2 ablation from n=1 to n=2.
- **Priority: HIGH** if eval exists, LOW if eval was never run.

### 2.4 Pre-fix vs post-fix comparison for methodological documentation

- **Available data pairs:**
  | Model | Pre-fix TSR | Post-fix TSR | Δ |
  |-------|------------|-------------|---|
  | SDF λ=0.005 s0 | 5.5% (#20) | 55.5% (#44) | +50 pp |
  | SDF λ=0.01 s0 | 5.5% (#21) | 52.5% (#42) | +47 pp |
  | LoRA s0 | 8.5% (#38) | 51.5% (#41) | +43 pp |

- **Recommendation:** Consider a brief appendix paragraph or footnote documenting the 180° image rotation bug and its ~45 pp impact on TSR. This is a valuable cautionary note for the community (VLA evaluation pitfalls).
- **Priority: LOW** — methodological interest only, not core contribution.

---

## 3. Correctly Excluded Experiments

### 3.1 Pre-rotation-fix evals (12 experiments) — SUPERSEDED

All performed before the 180° image rotation bug was discovered. TSR values are artifactually low (~4–10% instead of ~50%). CAR values are also unreliable because the policy received incorrectly oriented images.

| exp_id | Issue |
|--------|-------|
| `eval_pi05_a1_30k_s0_l005` | Pre-fix, TSR=5.5% |
| `eval_pi05_a1_30k_s0_l01` | Pre-fix, TSR=5.5% |
| `eval_pi05_a1_30k_s1_l005_v2` | Pre-fix, TSR=5.5% |
| `eval_pi05_a1_30k_s2_l005_v2` | Pre-fix, TSR=9.5% |
| `eval_pi05_a1_30k_s1_l01_v2` | Pre-fix, TSR=7.5% |
| `eval_pi05_a1_30k_s2_l01_v2` | Pre-fix, TSR=7.5% |
| `eval_pi05_a1_30k_s1_l005_v3` | Pre-fix, TSR=4% |
| `eval_pi05_a1_30k_s2_l005_v3` | Pre-fix, TSR=9% |
| `eval_pi05_a1_best_s0_l005` | Pre-fix (eval_seed=7 but old script) |
| `eval_pi05_a1_30k_s0_l005_r4` | Old script retry |
| `eval_lora_baseline_30k_s0_v2` | Pre-fix |
| `eval_lora_baseline_30k_s1_v2` | Pre-fix |

### 3.2 Displacement fix / debugging evals (4 experiments) — INTERMEDIATE

| exp_id | Issue |
|--------|-------|
| `eval_pi05_a1_best_s2_l005_10k` | Pre-fix, used old eval script. Zero-fake-safe finding is interesting but invalid due to rotation bug. |
| `eval_pi05_a1_best_s1_l005_16k` | Pre-fix, best-loss checkpoint eval |
| `eval_pi05_a1_30k_s1_l005_disp` | Displacement field fix verification run |
| `eval_pi05_a1_30k_s0_l01_disp` | Displacement field fix verification run |

### 3.3 Pipeline v1 / empty metrics (2 experiments) — SUPERSEDED

| exp_id | Issue |
|--------|-------|
| `eval_pi05_baseline_reeval_disp` | Metrics empty in registry |
| `eval_spatial_bowl_lora_ctrl_s0` | v1 pipeline, superseded by `_v2` (#68) |

---

## 4. Consistency Cross-Checks

### 4.1 Registry ↔ Paper Value Matches

All checked values match between registry metrics and paper tables:

| Paper value | Registry source | Match? |
|-------------|----------------|--------|
| LoRA s1 CAR=52.5% | reeval_lora_s1_30k: car=52.5% | ✓ |
| SDF λ=0.005 s0 CAR=57.0% | reeval_sdf_s0_l005_30k: car=57% | ✓ |
| SDF λ=0.1 s0 CAR=58.0% | eval_pi05_a1_30k_s0_l01_high: CAR=58% | ✓ |
| SDF λ=0.1 s2 CAR=54.5% | eval_pi05_a1_30k_s2_l01_high: car=54.5% | ✓ |
| LoRA eseed=42 CAR=56.5% | eval_multiseed_lora_s0_eseed42: avg_CAR=56.5% | ✓ |
| dfCAR threshold stable [2,200]mm | analysis_threshold_sensitivity | ✓ |

### 4.2 Potential Discrepancy: LoRA s0 value

- Paper tab:avoidance_source uses LoRA-only mean = 54.67% = (56.5 + 52.5 + 55.0) / 3
- This implies LoRA s0 = 56.5%, from `eval_lora_baseline_30k_s0_reeval`
- But `reeval_lora_s0_30k_v2` gives 57.0% for the same model/seed/eval_seed
- The 0.5 pp discrepancy is due to different eval runs (stochastic simulation). Paper consistently uses the earlier run (#41).

---

## 5. Provenance Gaps — Paper Numbers Without Registry Source

The following paper values have **no matching registry experiment**:

| Paper value | Location | Likely source |
|-------------|----------|---------------|
| Pi0 Full-FT: CAR=83.0%, TSR=0.5% | claim1 tab:fake_safety | Evaluated before registry established, or unregistered eval |
| Pi0 LoRA: CAR=82.0%, TSR=0.0% | claim1 tab:fake_safety | Same — unregistered eval |
| Pi0.5 baseline: CAR=28.5% (aggregate) | claim1, claim3 | Requires seed 0 eval (registered s1=25%, s2=27.5%; seed 0 not registered) |
| Oracle-adaptive: CAR=75.0% | claim2 tab:oracle | Oracle evals never registered |
| Oracle-fixed: CAR=73.1% | claim2 tab:oracle | Oracle evals never registered |
| Oracle-feature: CAR=76.9% | claim2 tab:oracle | Oracle evals never registered |
| A3 learned SDF: CAR=77.1% | claim2 tab:oracle | A3 eval never registered |
| Spatial bowl SDF λ=0.005: CAR=11.5% | appendix tab:spatial_bowl | Eval of trained model #22, eval not registered |
| Stepwise 16K s0: CAR=55.5% | appendix tab:stepwise | Unregistered eval |
| Stepwise 20K s0: CAR=55.0% | appendix tab:stepwise | Unregistered eval |
| Stepwise 24K s0: CAR=52.5% | appendix tab:stepwise | Unregistered eval |
| Stepwise 28K s0: CAR=54.5% | appendix tab:stepwise | Unregistered eval |
| Stepwise 16K s1: CAR=56.0% | appendix tab:stepwise | Unregistered eval |
| Stepwise 20K s1: CAR=56.0% | appendix tab:stepwise | Unregistered eval |
| Stepwise 22K s1: CAR=56.5% | appendix tab:stepwise | Unregistered eval |

**Total: ~17 data points in the paper without registry provenance.**

---

## 6. Recommendations (Prioritized)

### Priority 1: Add eseed=256 to eval-seed robustness table
- **Effort:** 5 min (add one row to tab:eval_seed_robustness)
- **Impact:** Fixes asymmetry (3 vs 5 eval seeds for SDF vs LoRA). New λ=0.1 mean: 58.5→58.1% (4 seeds), further supporting non-significance.

### Priority 2: Check if Phase 2 extra seed was evaluated
- **Effort:** Check server for eval results of `train_phase2_lambda0_extra_seed` model
- **Impact:** If available, upgrades Phase 2 ablation from n=1 to n=2, partially addressing a stated limitation.

### Priority 3: Report run-to-run variance in limitations
- **Effort:** 1 sentence + footnote
- **Impact:** `reeval_lora_s0_30k_v2` (CAR=57%) vs `eval_lora_baseline_30k_s0_reeval` (CAR=56.5%) demonstrates 0.5 pp CAR and 5.5 pp TSR run-to-run noise. Strengthens the argument that 2.3 pp effects are below noise floor.

### Priority 4: Register provenance gaps
- **Effort:** Retroactively register the 17 unregistered evals
- **Impact:** Complete audit trail. Especially important for Pi0/Oracle/A3 results (claim1 & claim2 are foundational).

### Priority 5: Document rotation bug as methodological note
- **Effort:** 2-3 sentences in appendix
- **Impact:** Cautionary contribution for VLA evaluation community. 12 pre-fix experiments provide clear evidence of ~45 pp TSR artifact.

### Not recommended:
- Adding pre-rotation-fix data to the paper (invalid due to eval bug)
- Adding displacement-fix verification runs (debugging artifacts)
- Adding v1 pipeline results (superseded)

---

## 7. Summary Statistics

| Category | Count | % of 72 |
|----------|-------|---------|
| Directly referenced in paper (eval) | 27 | 37.5% |
| Indirectly referenced (training) | 22 | 30.6% |
| Phase 2 ablation | 2 | 2.8% |
| **Total used** | **51** | **70.8%** |
| Unused — potentially valuable | 3 | 4.2% |
| Unused — superseded (pre-fix) | 12 | 16.7% |
| Unused — debugging/intermediate | 4 | 5.6% |
| Unused — pipeline v1/empty | 2 | 2.8% |
| **Total unused** | **21** | **29.2%** |

**Utilization rate: 70.8%.** The 29.2% unused experiments are predominantly pre-rotation-fix evals (57% of unused) that were correctly excluded due to the evaluation bug. Only 3 experiments (4.2% of total) have potential value not currently captured in the paper.
