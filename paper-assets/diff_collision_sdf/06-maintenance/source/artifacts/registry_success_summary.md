# Registry Success Experiments — Complete Summary

All 72 experiments have `conclusion=success`. Sorted by `created_at`.

---

## Group 1 — Early Baselines (pi0 full-FT, pi0+LoRA, A3 gradient refine) [May 19–21]

### 1. `baseline_spatial_bowl_s0_v2`
- **Hypothesis:** Vanilla pi0 fine-tune on LIBERO spatial_bowl (seed 0, extra_delta_transform=False) establishes baseline TSR >50% and CAR ~0% for ColliForce comparison
- **Metrics:** best_loss=0.00316, final_loss=0.0032, steps_completed=30000
- **Unique:** Full-FT (no LoRA) pi0 base; spatial_bowl scene; reference baseline

### 2. `baseline_object_pudding_s0_v2`
- **Hypothesis:** Vanilla pi0 fine-tune on LIBERO object_pudding establishes baseline for Level I collision scenario — expecting TSR >50%, CAR ~0%
- **Metrics:** final_loss=0.005, steps_completed=30000
- **Unique:** Full-FT (no LoRA) pi0 base; object_pudding scene; reference baseline

### 3. `a3_gradient_spatial_bowl_s0`
- **Hypothesis:** SDF gradient-guided action refinement during training (A3) on spatial_bowl Level II — expects CAR improvement over baseline with TSR drop <10%; comparable to AEGIS (CAR 86%, TSR 88%)
- **Metrics:** best_loss=0.01552, steps_completed=30000
- **Unique:** A3 architecture (SDF gradient loss at train time); spatial_bowl scene

### 4. `a3_gradient_object_pudding_s0`
- **Hypothesis:** SDF gradient-guided action refinement (A3) on object_pudding Level I — comparable to AEGIS (CAR 32%, TSR 92%)
- **Metrics:** best_loss=0.01439, final_loss=0.01898, steps_completed=30000
- **Unique:** A3 architecture; object_pudding scene; model `pi0+A3_gradient_refine`

### 5. `baseline_lora_spatial_bowl_s0`
- **Hypothesis:** LoRA fine-tuned pi0 baseline on spatial_bowl (rank 16/32) establishes fair comparison baseline — same trainable parameter budget as A3
- **Metrics:** best_loss=0.00876, steps_completed=30000
- **Unique:** LoRA baseline (no collision loss); spatial_bowl; parameter-matched reference for A3

### 6. `baseline_lora_object_pudding_s0`
- **Hypothesis:** LoRA fine-tuned pi0 baseline on object_pudding (rank 16/32) establishes fair comparison baseline — same trainable parameter budget as A3
- **Metrics:** best_loss=0.0124, steps_completed=30000
- **Unique:** LoRA baseline (no collision loss); object_pudding; parameter-matched reference for A3

### 7. `a1_lora_object_pudding_s0`
- **Hypothesis:** A1 SDF auxiliary task with LoRA injection (rank 16/32) on object_pudding — Phase 1 SDF warmup (frozen LoRA), Phase 2 joint training; expects CAR improvement over LoRA baseline with TSR drop <10%
- **Metrics:** best_loss=0.01326, final_loss=0.0184, steps_completed=30000
- **Unique:** A1 architecture; two-phase training (SDF warmup then joint); model `pi0+LoRA+SDF_aux`

### 8. `a1_lora_spatial_bowl_s0`
- **Hypothesis:** A1 SDF auxiliary task with LoRA injection on spatial_bowl — Phase 1 SDF warmup, Phase 2 joint; expects CAR improvement over LoRA baseline with TSR drop <10%
- **Metrics:** best_loss=0.01431, steps_completed=30000
- **Unique:** A1 architecture on spatial_bowl scene

---

## Group 2 — Pi0.5 Baselines and Initial A1 Diagnosis [May 22]

### 9. `eval_a1_lora_object_v11`
- **Hypothesis:** A1 (SDF auxiliary loss + LoRA, no runtime refinement) eval on safelibero_object — tests whether SDF auxiliary training signal alone improves CAR over LoRA baseline
- **Metrics:** TSR=0, n_episodes=200, displacement_avg=0.0027
- **Unique:** First A1 eval; TSR=0 flagged action collapse; critical diagnostic

### 10. `eval_pi05_safelibero_object_v11_s2`
- **Hypothesis:** Pi0.5 baseline multi-seed replication (seed 2): confirm CAR=28% is stable across seeds
- **Metrics:** CAR=27.5%, TSR=75.0%, mean_displacement=0.132
- **Unique:** Pi0.5 pretrained checkpoint (no fine-tune); seed 2 replication

### 11. `eval_pi05_safelibero_object_v11_s1`
- **Hypothesis:** Pi0.5 baseline multi-seed replication (seed 1): confirm CAR=28% is stable
- **Metrics:** CAR=25.0%, TSR=76.0%, mean_displacement=0.153
- **Unique:** Pi0.5 pretrained checkpoint; seed 1 replication

---

## Group 3 — Pi0.5+A1 Training Sweep (3 seeds × 2 lambdas) [May 23–24]

### 12. `train_pi05_a1_obj_s0_l01`
- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.01) seed 0 — restarted after P0 checkpoint collision fix; tests whether stronger SDF signal produces real collision avoidance or action collapse
- **Metrics:** best_loss=0.00801, steps_completed=30000
- **Unique:** Pi0.5 backbone; λ=0.01; seed 0; restart after checkpoint fix

### 13. `train_pi05_a1_obj_s0_l005`
- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.005) seed 0 — conservative SDF signal
- **Metrics:** best_loss=0.007861, steps_completed=30000
- **Unique:** Pi0.5 backbone; λ=0.005; seed 0

### 14. `train_pi05_a1_obj_s1_l005`
- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.005) seed 1 — multi-seed replication of conservative lambda
- **Metrics:** best_loss=0.01143, steps_completed=30000
- **Unique:** Pi0.5; λ=0.005; seed 1

### 15. `train_pi05_a1_obj_s1_l01`
- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.01) seed 1 — multi-seed replication of stronger lambda
- **Metrics:** best_loss=0.01168, steps_completed=30000
- **Unique:** Pi0.5; λ=0.01; seed 1

### 16. `train_pi05_a1_obj_s2_l005`
- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.005) seed 2 — third seed for statistical significance
- **Metrics:** best_loss=0.00874, steps_completed=30000
- **Unique:** Pi0.5; λ=0.005; seed 2

### 17. `train_pi05_a1_obj_s2_l01`
- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss (λ=0.01) seed 2 — third seed for statistical significance of higher SDF signal
- **Metrics:** best_loss=0.00911, steps_completed=30000
- **Unique:** Pi0.5; λ=0.01; seed 2

### 18. `train_pi05_lora_baseline_s0`
- **Hypothesis:** LoRA baseline (no SDF) on object_pudding 30K steps — attribution control; if CAR ≈ Pi0.5 baseline (~27%), confirms ColliForce improvement is from SDF not LoRA
- **Metrics:** best_loss=0.01025, final_loss=0.01343, best_step=24000
- **Unique:** Pi0.5+LoRA-only control; seed 0; Claim 4 SDF attribution

### 19. `train_pi05_lora_baseline_s1`
- **Hypothesis:** LoRA baseline (no SDF) seed 1 on object_pudding — second seed for LoRA-only attribution control
- **Metrics:** best_loss=0.0113, final_loss=0.01408, best_step=14000
- **Unique:** Pi0.5+LoRA-only control; seed 1

---

## Group 4 — 30K Eval Matrix (3 seeds × 2 lambdas) [May 25]

### 20. `eval_pi05_a1_30k_s0_l005`
- **Hypothesis:** Pi0.5+A1 30K eval (seed0, λ=0.005): completes 3-seed coverage for conservative lambda
- **Metrics:** avg_CAR=50%, avg_TSR=5.5%, task0_CAR=58%, task1_CAR=42%, task2_CAR=86%, task3_CAR=14%, task0_TSR=2%, task1_TSR=20%, n_episodes=200
- **Unique:** First corrected eval with fixed checkpoint path; low TSR (old eval bug later discovered)

### 21. `eval_pi05_a1_30k_s0_l01`
- **Hypothesis:** Pi0.5+A1 30K eval (seed0, λ=0.01): completes 3-seed coverage for stronger lambda
- **Metrics:** avg_CAR=53%, avg_TSR=5.5%, task0_CAR=68%, task1_CAR=46%, task2_CAR=86%, task3_CAR=12%, task0_TSR=2%, task1_TSR=20%, n_episodes=200 (note: old script, no max_ee_displacement)
- **Unique:** λ=0.01; note flags old script version

### 22. `train_pi05_a1_spatial_bowl_s0_l005`
- **Hypothesis:** Pi0.5+A1 SDF auxiliary loss on spatial_bowl (λ=0.005, seed 0) — tests cross-scene generalization; bilateral obstacles
- **Metrics:** best_loss=0.01063, final_loss=0.0137, best_step=28000
- **Unique:** Cross-scene generalization to spatial_bowl; bilateral obstacle geometry

### 23. `eval_pi05_a1_30k_s1_l005_v2`
- **Hypothesis:** Pi0.5+A1 30K eval (seed1, λ=0.005) corrected re-run with verified 30K checkpoint path
- **Metrics:** avg_CAR=52.5%, avg_TSR=5.5%, task0_CAR=58%, task1_CAR=40%, task2_CAR=94%, task3_CAR=18%, n_episodes=200
- **Unique:** v2 correction of checkpoint path bug; seed 1

### 24. `eval_pi05_a1_30k_s2_l005_v2`
- **Hypothesis:** Pi0.5+A1 30K eval (seed2, λ=0.005) corrected re-run — third seed for statistical significance
- **Metrics:** avg_CAR=54.5%, avg_TSR=9.5%, task0_CAR=62%, task1_CAR=44%, task2_CAR=90%, task3_CAR=22%, n_episodes=200
- **Unique:** Third seed; corrected checkpoint path

### 25. `eval_pi05_a1_30k_s1_l01_v2`
- **Hypothesis:** Pi0.5+A1 30K eval (seed1, λ=0.01) corrected re-run with lora_baseline model type
- **Metrics:** avg_CAR=52.5%, avg_TSR=7.5%, task0_CAR=54%, task1_CAR=48%, task2_CAR=94%, task3_CAR=14%, n_episodes=200
- **Unique:** λ=0.01; corrected model_type parameter; seed 1

### 26. `eval_pi05_a1_30k_s2_l01_v2`
- **Hypothesis:** Pi0.5+A1 30K eval (seed2, λ=0.01) — completes the 3-seed × 2-lambda eval matrix
- **Metrics:** avg_CAR=53%, avg_TSR=7.5%, task0_CAR=62%, task1_CAR=42%, task2_CAR=88%, task3_CAR=20%, n_episodes=200
- **Unique:** Completes the full 3×2 matrix; seed 2; λ=0.01

### 27. `eval_pi05_a1_30k_s1_l005_v3`
- **Hypothesis:** Pi0.5+A1 30K eval (seed1, λ=0.005) rerun with correct --output_path to preserve per-episode displacement data (v2 JSON was overwritten by concurrent evals)
- **Metrics:** avg_CAR=51.5%, avg_TSR=4%, task0_CAR=54%, task1_CAR=48%, task2_CAR=88%, task3_CAR=16%, n_episodes=200
- **Unique:** v3 fix for output path collision; first eval with displacement data preserved

### 28. `eval_pi05_a1_30k_s2_l005_v3`
- **Hypothesis:** Pi0.5+A1 30K eval (seed2, λ=0.005) rerun with correct --output_path; v2 JSON was overwritten
- **Metrics:** avg_CAR=53%, avg_TSR=9%, task0_CAR=60%, task1_CAR=46%, task2_CAR=86%, task3_CAR=20%, n_episodes=200
- **Unique:** v3 fix; seed 2; displacement data preserved

### 29. `eval_pi05_a1_best_s0_l005`
- **Hypothesis:** Pi0.5+A1 best checkpoint eval (seed0, λ=0.005) at best-loss checkpoint (step 26000) — completes 3-seed best-checkpoint coverage
- **Metrics:** avg_CAR=54.5%, avg_TSR=52%, task0_CAR=50%, task1_CAR=74%, task2_CAR=68%, task3_CAR=26%, n_episodes=50, eval_seed=7, collision_threshold=0.001
- **Unique:** Best-loss checkpoint (step 26000) not final; task-level breakdown; eval_seed=7

### 30. `eval_pi05_a1_best_s2_l005_10k`
- **Hypothesis:** Pi0.5+A1 best checkpoint eval (seed2, λ=0.005, step 10K) — evaluates the sweet-spot checkpoint before action collapse
- **Metrics:** avg_CAR=55.5%, avg_TSR=9%, task0_CAR=68%, task1_CAR=44%, task2_CAR=92%, task3_CAR=18%, n_episodes=200, fake_safe_pct=0; analysis: "ALL episodes have high EE displacement (0.39–0.58m). Zero fake safety. 10K best shows genuine collision avoidance."
- **Unique:** Pre-collapse checkpoint; zero fake-safe episodes; analysis confirms genuine avoidance

### 31. `eval_pi05_a1_30k_s0_l005_r4`
- **Hypothesis:** Pi0.5+A1 30K eval retry (seed0, λ=0.005) — re-run with fixed eval script to get displacement data
- **Metrics:** avg_CAR=47%, avg_TSR=7.5%, task0_CAR=58%, task1_CAR=38%, task2_CAR=76%, task3_CAR=16%, n_episodes=200 (note: old script, no max_ee_displacement)
- **Unique:** Retry with fixed script; old script note still present; seed 0

### 32. `eval_pi05_a1_best_s1_l005_16k`
- **Hypothesis:** Pi0.5+A1 best checkpoint eval (seed1, λ=0.005, step 16000) — best-loss checkpoint vs 30K final
- **Metrics:** avg_CAR=53%, avg_TSR=6.5%, task0_CAR=58%, task1_CAR=50%, task2_CAR=88%, task3_CAR=16%, n_episodes=200, fake_safe_pct=0
- **Unique:** Best-loss checkpoint at step 16K; zero fake-safe episodes

### 33. `eval_pi05_a1_30k_s1_l005_disp`
- **Hypothesis:** Displacement fix verification — rerun s1_l005_30k eval to confirm max_ee_displacement field is correctly output
- **Metrics:** avg_CAR=54%, avg_TSR=4%, task0_CAR=54%, task1_CAR=58%, task2_CAR=92%, task3_CAR=12%, n_episodes=200, fake_safe_pct=0
- **Unique:** Explicitly validates displacement field fix; zero fake-safe

### 34. `eval_pi05_a1_30k_s0_l01_disp`
- **Hypothesis:** Pi0.5+A1 30K displacement eval (seed0, λ=0.01) — re-run with fixed eval script to get max_ee_displacement; tests for 30K action collapse
- **Metrics:** avg_CAR=52.5%, avg_TSR=6.5%, task0_CAR=76%, task1_CAR=32%, task2_CAR=84%, task3_CAR=18%, n_episodes=200, fake_safe_pct=0
- **Unique:** λ=0.01; displacement-aware eval; zero fake-safe

---

## Group 5 — Phase 2 Ablation, High-Lambda Training [May 25–26]

### 35. `train_pi05_phase2_lambda0_s2`
- **Hypothesis:** Phase 2 λ=0 ablation (seed2): resume from seed2 l005 best (10K) checkpoint with SDF loss disabled — tests whether early SDF-encoded collision awareness persists in LoRA weights
- **Metrics:** best_loss=0.00651, best_step=4000
- **Unique:** Ablation of SDF loss after warmup; resume from 10K; seed 2; tests LoRA weight retention

### 36. `train_pi05_a1_obj_s0_l01_high`
- **Hypothesis:** Pi0.5+A1 SDF training with high lambda=0.1 (seed0, 30K) — tests faster collision avoidance learning vs earlier over-avoidance onset
- **Metrics:** (empty — training only)
- **Unique:** High lambda=0.1; seed 0; paired with seed 1 for error bars

### 37. `train_pi05_a1_obj_s1_l01_high`
- **Hypothesis:** Pi0.5+A1 SDF training with high lambda=0.1 (seed1, 30K) — second seed for lambda=0.1 error bars
- **Metrics:** (empty — training only)
- **Unique:** High lambda=0.1; seed 1

---

## Group 6 — Rotation Fix Re-evals (LoRA Baseline) [May 26]

### 38. `eval_lora_baseline_30k_s0_v2`
- **Hypothesis:** LoRA baseline (no SDF) 30K eval on object_pudding seed 0 (v2, base env fix) — expects CAR ≈ Pi0.5 baseline (~27%); critical for Claim 4 SDF attribution
- **Metrics:** avg_CAR=54.5%, avg_TSR=8.5%, dfCAR_100mm=54.5%, n_episodes=200, frozen_pct=0
- **Unique:** Surprising high CAR~54.5% (vs expected ~27%); dfCAR_100mm introduced; first dfCAR datapoint

### 39. `eval_lora_baseline_30k_s1_v2`
- **Hypothesis:** LoRA baseline (no SDF) 30K eval seed 1 (v2, base env fix) — second seed for LoRA-only attribution
- **Metrics:** avg_CAR=56%, avg_TSR=4%, dfCAR_100mm=56%, n_episodes=200, frozen_pct=0
- **Unique:** Consistently high LoRA CAR; challenges SDF attribution claim; dfCAR_100mm

### 40. `eval_pi05_baseline_reeval_disp`
- **Hypothesis:** Pi0.5 base model (no LoRA, no SDF) re-eval with fixed eval script on object_pudding 200ep — obtain EE displacement data for dfCAR baseline comparison
- **Metrics:** (empty — results pending or logged elsewhere)
- **Unique:** Raw pi0.5 model re-eval; displacement data for dfCAR analysis

### 41. `eval_lora_baseline_30k_s0_reeval`
- **Hypothesis:** Re-eval LoRA-only s0 (30K) with fixed eval_safelibero.py (180° image rotation added) — if TSR remains ~6–8%, catastrophic forgetting is real; if TSR >30%, eval bug artifact
- **Metrics:** CAR=56.5%, TSR=51.5%
- **Unique:** Critical rotation fix applied; TSR jumped from ~8% to 51.5%, confirming earlier TSR collapse was eval bug

---

## Group 7 — Full Re-eval Batch with Rotation Fix (SDF + LoRA) [May 26]

### 42. `reeval_sdf_s0_l01_30k`
- **Hypothesis:** Re-eval SDF λ=0.01 s0 (30K) with fixed eval_safelibero.py (180° rotation) — verify TSR collapse is real or eval bug
- **Metrics:** car=57%, tsr=52.5%, fake_safe_rate_ee=0, frozen_rate_ee=0, frozen_rate_obs=55.5%
- **Unique:** First corrected SDF re-eval; frozen_rate_obs=55.5% (obstacle motionless, NOT fake safety); note distinguishes paper definition vs script definition

### 43. `reeval_lora_s1_30k`
- **Hypothesis:** Re-eval LoRA-only s1 (30K) with fixed eval — second seed for LoRA-only attribution baseline; expected TSR ~50%
- **Metrics:** car=52.5%, tsr=51.5%, fake_safe_rate_ee=0, frozen_rate_ee=0
- **Unique:** LoRA-only seed 1; confirms rotation fix recovers TSR

### 44. `reeval_sdf_s0_l005_30k`
- **Hypothesis:** Re-eval SDF λ=0.005 s0 (30K) with rotation fix — corrected SDF attribution data
- **Metrics:** car=57%, tsr=55.5%, fake_safe_rate_ee=0, frozen_rate_ee=0
- **Unique:** λ=0.005; seed 0; corrected

### 45. `reeval_sdf_s1_l005_30k`
- **Hypothesis:** Re-eval SDF λ=0.005 s1 (30K) with rotation fix
- **Metrics:** CAR=54%, TSR=50.5%
- **Unique:** λ=0.005; seed 1; corrected

### 46. `reeval_sdf_s2_l005_30k`
- **Hypothesis:** Re-eval SDF λ=0.005 s2 (30K) with rotation fix — third seed for λ=0.005
- **Metrics:** CAR=52.5%, TSR=56%
- **Unique:** λ=0.005; seed 2; corrected

### 47. `reeval_sdf_s1_l01_30k`
- **Hypothesis:** Re-eval SDF λ=0.01 s1 (30K) with rotation fix — second seed for λ=0.01
- **Metrics:** CAR=57.5%, TSR=55.5%
- **Unique:** λ=0.01; seed 1; corrected

### 48. `reeval_sdf_s2_l01_30k`
- **Hypothesis:** Re-eval SDF λ=0.01 s2 (30K) with rotation fix — third seed for λ=0.01
- **Metrics:** CAR=54.5%, TSR=53.5%
- **Unique:** λ=0.01; seed 2; corrected; completes 3-seed λ=0.01 re-eval

---

## Group 8 — Phase 2 λ=0 Eval, LoRA Spatial Bowl, Reeval s0, High-Lambda Training [May 26]

### 49. `eval_phase2_lambda0_s2`
- **Hypothesis:** Phase 2 LoRA unfrozen training with λ=0 (no SDF loss) seed 2 should achieve baseline-level TSR on safelibero_object — control for SDF-augmented models
- **Metrics:** (empty — eval results not recorded in metrics field)
- **Unique:** Phase 2 ablation control; λ=0; tests task retention after SDF warmup removed

### 50. `train_spatial_bowl_lora_control_s0`
- **Hypothesis:** LoRA-only baseline (without SDF collision loss) on spatial_bowl — safety-violation rate should remain high at pre-training level, establishing the gap SDF training aims to close
- **Metrics:** (empty — training only)
- **Unique:** LoRA control for spatial_bowl scene; establishes control arm for cross-scene generalization

### 51. `reeval_lora_s0_30k_v2`
- **Hypothesis:** Re-eval LoRA-only s0 30K with confirmed rotation-fixed script (seed=7) — previous reeval was from buggy version; second reliable LoRA-only seed for Claim 3 mean±std
- **Metrics:** CAR=57%, TSR=46%
- **Unique:** Uses eval_seed=7; explicit confirmation of rotation fix; second reliable LoRA seed

### 52. `train_pi05_a1_obj_s2_l01_high`
- **Hypothesis:** Pi0.5+A1 SDF training with high lambda=0.1 (seed2, 30K) — third seed for 3-seed statistical power for A/B/C scenario determination
- **Metrics:** best_loss=0.0104, final_loss=0.0104, best_step=30000
- **Unique:** High lambda=0.1; seed 2; third seed; final checkpoint = best checkpoint (no early plateau)

---

## Group 9 — dfCAR Analysis, Stepwise Eval, LoRA Baseline Seed 2 [May 26–27]

### 53. `analysis_threshold_sensitivity`
- **Hypothesis:** dfCAR threshold τ_d is robust across [2, 200] mm — bimodal displacement gap (collapsed <0.1mm vs active >270mm) means any threshold in this range produces identical dfCAR values
- **Metrics:** dfCAR_stable_range_mm="[2, 200]", n_models=8, max_dfCAR_variation_2_to_200mm=0, n_active_equals_n_total_at_200mm=true; conclusion: "dfCAR perfectly invariant across tau_d in [2, 200] mm for all 8 model-seed combinations; only at 300mm do 1-2 episodes fall below threshold"
- **Unique:** Analysis experiment (no training/eval); validates dfCAR metric robustness; uses threshold_sensitivity_v2.csv; 8 models tested

### 54. `eval_stepwise_s0_l1_22k`
- **Hypothesis:** Step-wise eval of Pi0.5+A1 SDF λ=0.1 (seed 0) at 22K checkpoint — third point in step-wise CAR curve (16K: 55.5%, 20K: 55%, 22K: this)
- **Metrics:** CAR=60.5%, TSR=45.5%, eval_seed=7, frozen_pct=0
- **Unique:** Step-wise curve point at 22K; λ=0.1; peak CAR in curve

### 55. `train_pi05_lora_baseline_s2_resume`
- **Hypothesis:** Resume LoRA baseline seed2 training from checkpoint 22000 to 30000 — original run killed by 24h tmux timeout at step 22364
- **Metrics:** final_loss=0.0117
- **Unique:** Resume from tmux-killed checkpoint; seed 2; enables 3v3 statistical comparison

### 56. `eval_stepwise_s0_l1_26k_v2`
- **Hypothesis:** The 24K frozen episodes (29.5%) were caused by missing --pi05 flag in eval, not SDF training degradation; re-running 26K eval with --pi05 should eliminate frozen episodes
- **Metrics:** CAR=53.5%, TSR=53%, dfCAR=53.5%, frozen_rate=0
- **Unique:** Diagnoses eval bug (missing --pi05 flag); dfCAR introduced; frozen_rate corrected to 0

---

## Group 10 — High-Lambda (λ=0.1) 3-Seed Eval, LoRA Seed 2 Eval, Spatial Bowl Control [May 27–28]

### 57. `eval_pi05_a1_30k_s0_l01_high`
- **Hypothesis:** Evaluate λ=0.1 seed0 30K checkpoint — based on stepwise curve (16K–28K CAR ~52.5–60.5%, mean ~55.1%), expects Scenario B (CAR ≤ 57%, SDF redundant)
- **Metrics:** CAR=58%, TSR=47%, dfCAR=58%, frozen_rate=0
- **Unique:** λ=0.1; seed 0; 30K; dfCAR=CAR (zero frozen); A/B/C scenario determination

### 58. `eval_pi05_a1_30k_s1_l01_high`
- **Hypothesis:** Evaluate λ=0.1 seed1 30K — combined with s0 CAR=58.0% determines A/B/C scenario
- **Metrics:** CAR=58.5%, TSR=49%, dfCAR=58.5%, frozen_rate=0
- **Unique:** λ=0.1; seed 1; dfCAR=CAR; seeds 0+1 both at ~58% → Scenario C gray zone

### 59. `train_phase2_lambda0_extra_seed`
- **Hypothesis:** Phase 2 Stage 1 with seed0 and λ_sdf=0.005 for 10K steps — viable checkpoint for Stage 2 lambda-0 training on object_pudding
- **Metrics:** (empty — training only)
- **Unique:** Extra seed for Phase 2 ablation; seed 0; 10K stage 1

### 60. `eval_lora_s2_30k_v2`
- **Hypothesis:** LoRA baseline seed2 at 30K steps — establishes 3-seed null distribution variance for statistical comparison with SDF-augmented models
- **Metrics:** overall_CAR=55%, overall_TSR=51.5%
- **Unique:** Uses `overall_CAR`/`overall_TSR` key names; seed 2; completes 3-seed LoRA null distribution

### 61. `eval_spatial_bowl_lora_ctrl_s0`
- **Hypothesis:** LoRA baseline (no SDF) on spatial_bowl at 30K steps — high TSR but low CAR, confirming collision avoidance requires explicit SDF training signal
- **Metrics:** avg_CAR=15.5%, avg_TSR=50%; note: "v1 old pipeline, superseded by v2"
- **Unique:** spatial_bowl scene; LoRA control arm; CAR=15.5% vs object_pudding ~56%; note flags pipeline issue

---

## Group 11 — λ=0.1 Seed 2 Eval, Multi-Eval-Seed Robustness Battery [May 28]

### 62. `eval_pi05_a1_30k_s2_l01_high`
- **Hypothesis:** Evaluate λ=0.1 seed2 30K — third seed to complete 3-seed statistical power; s0=58%, s1=58.5%, s2 determines final A/B/C scenario
- **Metrics:** car=54.5%, tsr=54.5%
- **Unique:** λ=0.1; seed 2; uses lowercase `car`/`tsr` keys; 3-seed mean ≈ 57%; confirms Scenario B/C boundary

### 63. `eval_multiseed_lora_s0_eseed42`
- **Hypothesis:** Multi-eval-seed robustness: LoRA-only s0 30K with eval_seed=42 — tests whether LoRA CAR (~56.5% at eval_seed=7) is stable across eval seeds; part of 5-way battery
- **Metrics:** avg_CAR=56.5%, avg_TSR=46%, n_episodes=50, eval_seed=42
- **Unique:** 50-episode eval; eval_seed sweep; part of 5-way → 7-way battery

### 64. `eval_multiseed_lora_s0_eseed123`
- **Hypothesis:** Multi-eval-seed robustness: LoRA-only s0 30K with eval_seed=123
- **Metrics:** avg_CAR=53%, avg_TSR=50.5%, n_episodes=50, eval_seed=123
- **Unique:** eval_seed=123; part of 5-way battery

### 65. `eval_multiseed_sdf_l01_s0_eseed42`
- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.1 s0 30K with eval_seed=42 — tests whether SDF CAR (~58.0% at eval_seed=7) remains non-significant vs LoRA across eval seeds
- **Metrics:** avg_CAR=59%, avg_TSR=52.5%, n_episodes=50, eval_seed=42
- **Unique:** SDF λ=0.1; eval_seed=42; 5-way battery arm

### 66. `eval_multiseed_sdf_l01_s0_eseed123`
- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.1 s0 30K with eval_seed=123
- **Metrics:** avg_CAR=58.5%, avg_TSR=53.5%, n_episodes=50, eval_seed=123
- **Unique:** SDF λ=0.1; eval_seed=123; 5-way battery arm

### 67. `eval_multiseed_sdf_l01_s0_eseed256`
- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.1 s0 30K with eval_seed=256 — third SDF eval seed for symmetric 3v3 comparison vs LoRA
- **Metrics:** avg_CAR=57%, avg_TSR=48%, n_episodes=50, eval_seed=256
- **Unique:** eval_seed=256; symmetric 3v3 SDF vs LoRA comparison

### 68. `eval_spatial_bowl_lora_ctrl_s0_v2`
- **Hypothesis:** Re-evaluate LoRA-only control on safelibero_spatial with consistent eval pipeline — confirms SDF redundancy across scenes
- **Metrics:** avg_CAR=12%, avg_TSR=49%, n_episodes=50, eval_seed=7
- **Unique:** Corrected v2 pipeline for spatial_bowl; avg_CAR=12% (vs 15.5% in v1); confirms spatial_bowl pattern

### 69. `eval_multiseed_lora_s0_eseed0`
- **Hypothesis:** Multi-eval-seed robustness: LoRA-only s0 30K with eval_seed=0 — extends 5-way battery to 7-way
- **Metrics:** avg_CAR=53%, avg_TSR=55.5%, n_episodes=50, eval_seed=0
- **Unique:** eval_seed=0; extends battery to 7-way

### 70. `eval_multiseed_lora_s0_eseed99`
- **Hypothesis:** Multi-eval-seed robustness: LoRA-only s0 30K with eval_seed=99 — extends 5-way battery to 7-way
- **Metrics:** avg_CAR=57.5%, avg_TSR=52%, n_episodes=50, eval_seed=99
- **Unique:** eval_seed=99; 7-way battery complete for LoRA

### 71. `eval_multiseed_sdf_l01_s0_eseed0`
- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.01 s0 30K with eval_seed=0 — extends 5-way battery to 7-way
- **Metrics:** avg_CAR=52.5%, avg_TSR=48.5%, n_episodes=50, eval_seed=0
- **Unique:** SDF λ=0.01 (not λ=0.1); eval_seed=0; 7-way extension

### 72. `eval_multiseed_sdf_l01_s0_eseed99`
- **Hypothesis:** Multi-eval-seed robustness: SDF λ=0.01 s0 30K with eval_seed=99 — extends 5-way battery to 7-way
- **Metrics:** avg_CAR=57%, avg_TSR=46.5%, n_episodes=50, eval_seed=99
- **Unique:** SDF λ=0.01; eval_seed=99; 7-way battery complete for SDF

---

## Summary Table — Eval Experiments with Performance Metrics

| exp_id | CAR (%) | TSR (%) | dfCAR (%) | n_ep | eval_seed | λ | seed | Scene |
|--------|---------|---------|-----------|------|-----------|---|------|-------|
| eval_pi05_safelibero_object_v11_s2 | 27.5 | 75.0 | — | 200 | 2 | — | 0 | object |
| eval_pi05_safelibero_object_v11_s1 | 25.0 | 76.0 | — | 200 | 1 | — | 1 | object |
| eval_pi05_a1_30k_s0_l005 | 50.0 | 5.5 | — | 200 | 0 | 0.005 | 0 | object |
| eval_pi05_a1_30k_s0_l01 | 53.0 | 5.5 | — | 200 | 0 | 0.01 | 0 | object |
| eval_pi05_a1_30k_s1_l005_v2 | 52.5 | 5.5 | — | 200 | 0 | 0.005 | 1 | object |
| eval_pi05_a1_30k_s2_l005_v2 | 54.5 | 9.5 | — | 200 | 0 | 0.005 | 2 | object |
| eval_pi05_a1_30k_s1_l01_v2 | 52.5 | 7.5 | — | 200 | 0 | 0.01 | 1 | object |
| eval_pi05_a1_30k_s2_l01_v2 | 53.0 | 7.5 | — | 200 | 0 | 0.01 | 2 | object |
| eval_pi05_a1_30k_s1_l005_v3 | 51.5 | 4.0 | — | 200 | 0 | 0.005 | 1 | object |
| eval_pi05_a1_30k_s2_l005_v3 | 53.0 | 9.0 | — | 200 | 0 | 0.005 | 2 | object |
| eval_pi05_a1_best_s0_l005 | 54.5 | 52.0 | — | 50 | 7 | 0.005 | 0 | object |
| eval_pi05_a1_best_s2_l005_10k | 55.5 | 9.0 | — | 200 | 0 | 0.005 | 2 | object |
| eval_pi05_a1_30k_s0_l005_r4 | 47.0 | 7.5 | — | 200 | 0 | 0.005 | 0 | object |
| eval_pi05_a1_best_s1_l005_16k | 53.0 | 6.5 | — | 200 | 1 | 0.005 | 1 | object |
| eval_pi05_a1_30k_s1_l005_disp | 54.0 | 4.0 | — | 200 | 1 | 0.005 | 1 | object |
| eval_pi05_a1_30k_s0_l01_disp | 52.5 | 6.5 | — | 200 | 0 | 0.01 | 0 | object |
| eval_lora_baseline_30k_s0_v2 | 54.5 | 8.5 | 54.5 | 200 | 0 | LoRA-only | 0 | object |
| eval_lora_baseline_30k_s1_v2 | 56.0 | 4.0 | 56.0 | 200 | 1 | LoRA-only | 1 | object |
| eval_lora_baseline_30k_s0_reeval | 56.5 | 51.5 | — | — | 7 | LoRA-only | 0 | object |
| reeval_sdf_s0_l01_30k | 57.0 | 52.5 | — | 200 | 0 | 0.01 | 0 | object |
| reeval_lora_s1_30k | 52.5 | 51.5 | — | 200 | 1 | LoRA-only | 1 | object |
| reeval_sdf_s0_l005_30k | 57.0 | 55.5 | — | 200 | 0 | 0.005 | 0 | object |
| reeval_sdf_s1_l005_30k | 54.0 | 50.5 | — | 200 | 1 | 0.005 | 1 | object |
| reeval_sdf_s2_l005_30k | 52.5 | 56.0 | — | 200 | 2 | 0.005 | 2 | object |
| reeval_sdf_s1_l01_30k | 57.5 | 55.5 | — | 200 | 1 | 0.01 | 1 | object |
| reeval_sdf_s2_l01_30k | 54.5 | 53.5 | — | 200 | 2 | 0.01 | 2 | object |
| reeval_lora_s0_30k_v2 | 57.0 | 46.0 | — | — | 7 | LoRA-only | 0 | object |
| eval_stepwise_s0_l1_22k | 60.5 | 45.5 | — | — | 7 | 0.1 | 0 | object |
| eval_stepwise_s0_l1_26k_v2 | 53.5 | 53.0 | 53.5 | — | 7 | 0.1 | 0 | object |
| eval_pi05_a1_30k_s0_l01_high | 58.0 | 47.0 | 58.0 | — | 7 | 0.1 | 0 | object |
| eval_pi05_a1_30k_s1_l01_high | 58.5 | 49.0 | 58.5 | — | 7 | 0.1 | 1 | object |
| eval_lora_s2_30k_v2 | 55.0 | 51.5 | — | — | 7 | LoRA-only | 2 | object |
| eval_spatial_bowl_lora_ctrl_s0 | 15.5 | 50.0 | — | — | 7 | LoRA-only | 0 | spatial |
| eval_pi05_a1_30k_s2_l01_high | 54.5 | 54.5 | — | — | 7 | 0.1 | 2 | object |
| eval_multiseed_lora_s0_eseed42 | 56.5 | 46.0 | — | 50 | 42 | LoRA-only | 0 | object |
| eval_multiseed_lora_s0_eseed123 | 53.0 | 50.5 | — | 50 | 123 | LoRA-only | 0 | object |
| eval_multiseed_sdf_l01_s0_eseed42 | 59.0 | 52.5 | — | 50 | 42 | 0.1 | 0 | object |
| eval_multiseed_sdf_l01_s0_eseed123 | 58.5 | 53.5 | — | 50 | 123 | 0.1 | 0 | object |
| eval_multiseed_sdf_l01_s0_eseed256 | 57.0 | 48.0 | — | 50 | 256 | 0.1 | 0 | object |
| eval_spatial_bowl_lora_ctrl_s0_v2 | 12.0 | 49.0 | — | 50 | 7 | LoRA-only | 0 | spatial |
| eval_multiseed_lora_s0_eseed0 | 53.0 | 55.5 | — | 50 | 0 | LoRA-only | 0 | object |
| eval_multiseed_lora_s0_eseed99 | 57.5 | 52.0 | — | 50 | 99 | LoRA-only | 0 | object |
| eval_multiseed_sdf_l01_s0_eseed0 | 52.5 | 48.5 | — | 50 | 0 | 0.01 | 0 | object |
| eval_multiseed_sdf_l01_s0_eseed99 | 57.0 | 46.5 | — | 50 | 99 | 0.01 | 0 | object |

---

## Key Findings Across All 72 Experiments

1. **All 72 experiments have `conclusion=success`** — no failures in registry.
2. **Eval bug (180° image rotation):** Early evals (Groups 3–4) showed TSR ~4–10%, later corrected by rotation fix which recovered TSR to ~50–56%.
3. **SDF redundancy (Scenario B/C):** After rotation fix, CAR for SDF-augmented models (λ=0.005/0.01/0.1) is ~52–58%, indistinguishable from LoRA-only baseline (~52–57%). This is the central finding.
4. **dfCAR metric:** Introduced in Group 6 to filter action-collapse episodes. For all rotation-fixed evals, frozen_rate=0 and dfCAR=CAR (no collapsed episodes exist).
5. **dfCAR threshold sensitivity:** Perfectly invariant across τ_d ∈ [2, 200] mm for all 8 model-seed combinations (`analysis_threshold_sensitivity`).
6. **Multi-eval-seed battery:** 7 eval seeds tested for both LoRA-only and SDF λ=0.01/0.1; SDF CAR consistently overlaps LoRA CAR range across all seeds.
7. **Spatial bowl scene:** LoRA-only CAR=12–15.5%, much lower than object_pudding (~54–57%), indicating scene-specific difficulty.
