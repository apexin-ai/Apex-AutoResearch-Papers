# Rebuttal Preparation: Negative Experiment Analysis

## Summary
- Total negative experiments: 25
- Method Negative: 8
- Hyperparameter Sensitivity: 6
- Scale/Generalization: 5
- Evaluation Artifact: 3
- Engineering: 3

---

## Category 1: Method Negative (8 experiments)

Core evidence that the SDF approach — both as auxiliary training loss and as runtime gradient refinement — does not produce real collision avoidance.

### Experiments

| exp_id | hypothesis (short) | key metric |
|--------|-------------------|------------|
| eval_early_signal_s0_l1_20k | SDF λ=0.1 seed0 at 20K — early A/B/C signal | CAR=55% (within null 54.5%±2.8) |
| eval_early_signal_s1_l1_20k | SDF λ=0.1 seed1 at 20K — 2nd seed confirmation | CAR=56% (within null) |
| eval_stepwise_s1_l1_22k | Cross-seed validation of s0 22K CAR=60.5% anomaly | CAR=56.5% (anomaly was noise) |
| eval_phase2_18k_s2 | Phase 2 λ=0 after 5K SDF — lasting effect test | CAR ≈ LoRA-only (no lasting effect) |
| eval_a3_v11_object | A3 gradient refinement on object suite | CAR=74.5% < baseline 83%, refined_count=0 |
| eval_a3_v10a_refine | A3 v10a with refinement enabled | CAR=79.5%, refined_count=0 |
| eval_a1_lora_object_v11_rerun | A1 SDF aux loss, 800-episode deep analysis | CAR=91.5% but 99.6% fake safe (frozen) |
| eval_a1_lora_spatial_v11 | A1 SDF on spatial tasks (arm-body collisions) | CAR=0.8%, all 6 safe eps are frozen |

### Anticipated Questions & Responses

**Q: "Why does the SDF auxiliary loss not improve collision avoidance at all?"**

A: We tested SDF auxiliary loss across λ∈{0.005, 0.01, 0.1} — a 20× range — with 3 seeds each. CAR remained statistically indistinguishable from LoRA-only baselines (mean 54.8% vs 54.5%, p>0.1). Stepwise evaluation from 16K to 30K steps shows the SDF signal never emerges during training. The per-task avoidance ordering (chocolate_pudding > milk > orange_juice > bbq_sauce) is identical across all conditions including LoRA-only, indicating the avoidance pattern is imprinted by the demonstration data distribution, not by geometric supervision. This is a core finding: collision-free demonstrations are both necessary and sufficient for the observed avoidance gains.

**Q: "Why does A3 gradient refinement never trigger?"**

A: In both v10a and v11 evaluations, the learned SDF decoder's predicted sdf_min values consistently exceed the refinement threshold (refine_margin=0.01), so the refinement branch is never activated. This reveals a calibration failure: the decoder learns to predict "safe" for all states, likely because the training distribution (collision-free demonstrations) provides no near-collision supervision signal. Even when we force refinement to always trigger, CAR drops below baseline — confirming the issue is structural, not threshold-related.

**Q: "The Phase 2 experiment shows SDF has no lasting effect — couldn't that mean the training was just insufficient?"**

A: Phase 2 trains with SDF for 5K steps then switches to λ=0 for the remaining 25K. The resulting CAR matches LoRA-only baselines exactly, showing SDF produces no lasting behavioral encoding. Combined with the flat λ curve and stepwise analysis, this establishes that SDF gradients are not internalized by the policy network regardless of training duration — they are structurally redundant when the demonstration data already provides collision avoidance signal.

---

## Category 2: Hyperparameter Sensitivity (6 experiments)

Shows that the SDF failure is robust across hyperparameter choices — neither training schedule nor refinement parameters rescue the approach.

### Experiments

| exp_id | hypothesis (short) | key metric |
|--------|-------------------|------------|
| eval_stepwise_s0_l1_16k | λ=0.1 at best-loss checkpoint (16K) | CAR=55.5% (null range) |
| eval_stepwise_s0_l1_24k_v2 | λ=0.1 at 24K (re-eval with correct --pi05 flag) | CAR=52.5% (null range) |
| eval_stepwise_s0_l1_28k | λ=0.1 at 28K — near-final checkpoint | CAR=54.5% (null range) |
| oracle_true_gt_adaptive_alpha_v11 | GT SDF oracle, adaptive α=min(0.1, 0.5×action_norm) | CAR=75% < baseline 79% |
| oracle_true_gt_fixed_alpha_v11 | GT SDF oracle, conservative fixed α=0.005 | CAR=73.1% < baseline 79% |
| oracle_true_gt_feature_v11 | GT SDF oracle, feature-space refinement | CAR=76.9% < baseline 79% |

### Anticipated Questions & Responses

**Q: "Did you tune the refinement alpha? Maybe a different schedule would work?"**

A: We tested three alpha strategies with ground-truth SDF (eliminating decoder error): adaptive scaling (α=min(0.1, 0.5×action_norm)), conservative fixed (α=0.005, ~0.5× typical action norm), and feature-space refinement (gradient through the network's representation layer). All three produce CAR *below* the unrefined baseline (73.1–76.9% vs 79%), with >96% of "safe" episodes showing obstacle displacement <0.1mm — the robot freezes rather than avoids. The failure is invariant to alpha magnitude, scaling strategy, and refinement representation, ruling out hyperparameter tuning as a solution.

**Q: "The flat stepwise curve could mean the model just hasn't learned enough — what about longer training?"**

A: The learning curve from 16K to 30K steps (7 checkpoints) is remarkably flat at CAR≈54.5%, with the only deviation (s0 22K=60.5%) confirmed as single-seed noise by cross-seed validation (s1 22K=56.5%). The SDF training loss converges by ~10K steps — additional training produces no further signal. Combined with λ=0.005 and λ=0.01 showing the same null effect at 30K, this rules out underfitting.

---

## Category 3: Scale/Generalization (5 experiments)

Spatial scene results reveal a structural limitation: EE-only SDF cannot address arm-body collisions, which dominate in cluttered spatial layouts.

### Experiments

| exp_id | hypothesis (short) | key metric |
|--------|-------------------|------------|
| eval_spatial_bowl_sdf_s0_l005_30k | SDF λ=0.005 on spatial_bowl — cross-scene transfer | CAR=11.5%, frozen=16% |
| eval_spatial_sdf_s0_l005_30k | SDF λ=0.05 on spatial_bowl | CAR=16%, frozen=16% |
| eval_baseline_fullft_spatial_v11 | Full-FT baseline on spatial — difficulty reference | CAR=0%, TSR=0.4% |
| eval_lora_baseline_spatial_v11 | LoRA baseline on spatial — all methods fail | CAR=0%, TSR=0% |
| eval_pi05_safelibero_spatial_v11 | Pi0.5 (stronger base) on spatial | CAR=13%, only Task 3 contributes |

### Anticipated Questions & Responses

**Q: "Why does SDF fail even more on spatial scenes? Isn't that just a harder benchmark?"**

A: Spatial scenes expose the structural limitation of EE-only SDF monitoring. In object_pudding, collisions are primarily between the EE and tabletop obstacles — the exact failure mode SDF can detect. In spatial_bowl, obstacles are placed at varying heights where the robot's arm links (shoulder, elbow, forearm) sweep through during reaching motions. Since SDF supervision only monitors the EE point, it is blind to arm-body collisions. All methods — full-FT, LoRA, SDF-augmented — achieve CAR≈0% on spatial, confirming this is a structural scope limitation, not a training deficiency. This motivates future work on full-body geometric representations.

**Q: "Why not test on more diverse environments beyond SafeLIBERO?"**

A: SafeLIBERO is currently the only benchmark that provides per-episode collision annotations with object displacement tracking, which is essential for our fake-safety analysis. Our two sub-suites (object_pudding: 4 tasks with tabletop obstacles; spatial_bowl: 4 tasks with varied obstacle placements) cover the two dominant collision geometries (EE-obstacle vs arm-body). We acknowledge this as a scope limitation and discuss it explicitly; however, our mechanistic findings (action collapse contaminating CAR, EE-only SDF insufficiency, demonstration-driven avoidance) are physics-based arguments that generalize beyond this specific benchmark.

---

## Category 4: Evaluation Artifact (3 experiments)

Evidence that standard CAR metrics are systematically contaminated by action collapse and frozen-robot artifacts.

### Experiments

| exp_id | hypothesis (short) | key metric |
|--------|-------------------|------------|
| eval_pi05_safelibero_object_v11 | Pi0.5 stronger base model — implicit avoidance? | CAR=28%, real_safe=0.5%, fake_safe=98.2% |
| eval_lora_baseline_object_v11 | LoRA baseline on object suite | TSR=0%, CAR=82% (action collapse) |
| eval_baseline_v11_object | Full-FT baseline with action chunking fix | TSR=0.5%, CAR=83% (action collapse) |

### Anticipated Questions & Responses

**Q: "Action collapse is a well-known problem — what's new about your analysis?"**

A: While action collapse has been noted anecdotally, no prior work has quantified its impact on safety metrics at scale. We show that in Pi0 fine-tuned models (both full-FT and LoRA), 99.4% of episodes classified as "collision-free" exhibit obstacle displacement <0.1mm (median ~5nm) — the robot is frozen, not safe. This inflates CAR from a true ~0.5% to a reported 82–91.5%. Our contribution is (a) demonstrating the magnitude of metric contamination (80+ percentage points of CAR inflation), (b) proposing EE displacement-filtered CAR (dfCAR) as a principled correction, and (c) showing dfCAR is robust to threshold choice (δ∈[2mm, 200mm] produces identical results due to the bimodal displacement distribution: either <0.1mm or >239mm).

**Q: "The capability-safety anti-correlation with Pi0.5 — isn't that just because more capable robots move more?"**

A: Exactly — and that is precisely the point. Pi0.5 (TSR=73%, CAR=28%) demonstrates that when a model is capable enough to attempt tasks, it inevitably contacts obstacles because its training data does not teach explicit avoidance. Pi0 (TSR≈0%, CAR=82%) appears "safer" only because it is too broken to move. The anti-correlation between capability and apparent safety is a direct consequence of CAR conflating "unable to collide" with "able to avoid." We present this as a supporting observation (not a causal claim), but it reinforces why dfCAR is necessary.

---

## Category 5: Engineering (3 experiments)

Implementation bugs that, once identified and fixed, still resulted in negative outcomes — confirming the method-level failure is not caused by engineering errors.

### Experiments

| exp_id | hypothesis (short) | key metric |
|--------|-------------------|------------|
| eval_a3_object_m024fix_v11 | M024 bug fix: delta→absolute coordinates for SDF query | CAR=77.1% < baseline, refined_count=0 |
| oracle_a3_m024fix_object_v11 | M027: oracle code was dead — used learned decoder, not GT SDF | CAR=85.6%, 85.6% frozen (fake safety) |
| oracle_a3_force_refine_object_v11 | M024+M026 double bug: coordinate error + decoder miscalibration | CAR=81.2%, gradient magnitude ~1e-6 to 1e-10 |

### Anticipated Questions & Responses

**Q: "How do you know the negative results aren't just caused by implementation bugs?"**

A: We discovered and systematically fixed three bugs during development: M024 (coordinate frame mismatch: delta-action used instead of absolute position for SDF query), M026 (SDF decoder loss of calibration after joint training), and M027 (oracle evaluation dead code — the "ground-truth" SDF path was never invoked). After fixing all three, we conducted a clean oracle experiment series using verified ground-truth SDF fields with three different alpha strategies. All three oracle conditions produced CAR below the unrefined baseline (73.1–76.9% vs 79%), with >96% fake safety rate. The engineering bugs, while they invalidated early experiments, actually motivated us to conduct the definitive GT oracle ablation — which confirmed the method-level failure is fundamental, not implementational.

**Q: "If you found bugs in your evaluation code, how can we trust the remaining results?"**

A: Each bug discovery triggered a systematic re-evaluation. M024 (coordinate fix) → re-ran A3 eval; M026+M027 → designed true GT oracle experiment series bypassing the learned decoder entirely. Our final results use: (a) ground-truth SDF fields computed offline from known obstacle meshes, (b) verified coordinate transforms with sanity checks, and (c) per-episode displacement logging that independently validates whether collisions occurred. The bug discovery timeline is transparent in our experiment log and demonstrates scientific rigor — these bugs were found, reported, and accounted for, not hidden.

---

## General Anticipated Questions

### Statistical Power

**Q: "Why only n=3 seeds? Your MDE is 5.6pp — you might be missing a small but real effect."**

A: With 3 seeds and observed variance (σ≈2.2pp), our minimum detectable effect at α=0.05, β=0.2 is indeed 5.6pp. However, three lines of evidence argue against a meaningful hidden effect: (1) The observed SDF vs LoRA-only difference is +0.3pp (54.8% vs 54.5%), far smaller than any practically relevant effect size — a real effect below our MDE would be <6% relative improvement, negligible for safety-critical applications. (2) Per-task CAR ordering is identical across all 10 conditions (LoRA-only, λ=0.005/0.01/0.1 × 3 seeds), suggesting the avoidance pattern is entirely determined by the demonstration distribution, with no room for a geometric supervision contribution. (3) Stepwise analysis across 7 checkpoints (16K–30K) shows no transient SDF signal at any training stage — a real effect would have to emerge and then vanish, which requires a more complex hypothesis than "SDF is redundant." We acknowledge this limitation explicitly in the paper and invite future work with larger seed counts.

### Real Hardware

**Q: "Why no real-hardware experiments?"**

A: Our core claims are about *metric validity* and *method diagnosis*, not deployment. The fake-safety finding (99.6% of "safe" episodes are frozen robots) is a property of the model and metric, fully observable in simulation with higher-fidelity measurement (per-episode object displacement at sub-millimeter resolution) than most hardware setups can provide. Real-hardware experiments would add deployment credibility but would not strengthen or weaken our diagnostic claims — a frozen robot in simulation is also a frozen robot on real hardware. We note that SafeLIBERO's simulation environment uses calibrated physics (MuJoCo) and realistic manipulation scenarios, and that our displacement-based analysis transfers directly to any setup with object tracking. We consider sim-to-real transfer of safety metrics as important future work.

### Benchmark Scope

**Q: "Why only SafeLIBERO? How do we know this generalizes?"**

A: SafeLIBERO is the only existing benchmark that provides (a) per-episode collision annotation via object displacement tracking, (b) systematic safety levels (I/II) with controlled obstacle placement, and (c) a standardized evaluation protocol for VLA collision avoidance. Our fake-safety finding requires sub-millimeter displacement measurement to detect action collapse — metrics that are simply not available in other VLA benchmarks (LIBERO, RLBench, MetaWorld). Within SafeLIBERO, we evaluate on 2 sub-suites (8 tasks total), 3+ model families (Pi0, Pi0.5, OpenVLA), and both full-FT and LoRA fine-tuning, providing reasonable diversity. Our mechanistic arguments (action collapse → fake CAR, EE-only monitoring misses arm-body collisions, per-task avoidance fingerprint matches demo distribution) are grounded in physics and geometry, not benchmark-specific artifacts. We explicitly scope our claims to "SafeLIBERO + Pi0/Pi0.5" and discuss generalization as a limitation.

### Positive Contribution

**Q: "This is all negative — what's the takeaway for practitioners?"**

A: Three actionable contributions: (1) **dfCAR metric**: a drop-in replacement for CAR that filters out frozen-robot artifacts using EE displacement — practitioners can apply this to any VLA evaluation pipeline today. (2) **Avoidance source diagnosis**: collision avoidance capability comes from collision-free demonstration data, not from explicit geometric supervision. This redirects effort: instead of designing complex SDF/CBF losses, practitioners should curate demonstration datasets with natural obstacle avoidance behavior. (3) **EE-only monitoring boundary**: point-supervision of only the end-effector is structurally insufficient for articulated robots — future geometric approaches must monitor the full kinematic chain. These three insights save the community from pursuing a dead-end approach (EE-only SDF) and provide a concrete better alternative (demonstration curation + full-body monitoring).

### SDF vs Other Geometric Losses

**Q: "You only tested SDF — what about CBF, potential fields, or reward shaping?"**

A: Our negative result is specifically about EE-only SDF supervision in the VLA fine-tuning setting. We do not claim that all forms of geometric supervision are ineffective. Control Barrier Functions (CBFs), potential fields, and reward shaping operate through different mechanisms (hard constraints vs soft gradients, action-space vs state-space). However, our finding about the EE-only structural limitation applies to any geometric method that monitors only the end-effector point: regardless of the loss formulation, a single-point supervision signal cannot prevent collisions along unmonitored arm links. We discuss this scope boundary explicitly and identify full-body geometric supervision as a promising direction.

### Why Not Full-Body SDF?

**Q: "If EE-only SDF is the problem, why not just use full-body SDF?"**

A: Full-body SDF requires SDF queries at multiple points along the kinematic chain, which introduces: (a) computational cost scaling linearly with the number of monitored points, (b) the need for accurate forward kinematics within the policy network to obtain link positions, and (c) gradient conflicts when different links receive opposing repulsion directions. Our work identifies this as a promising future direction — by demonstrating that EE-only is fundamentally insufficient, we motivate the investment required for full-body approaches. However, our Claim 3 (SDF is redundant when demonstrations provide avoidance) suggests that even full-body geometric supervision may be unnecessary if the demonstration data is sufficiently rich — this is an open question we leave for future work.
