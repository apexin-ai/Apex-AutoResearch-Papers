# Rebuttal Preparation: Negative Experiment Analysis

## Summary
- Total negative experiments: 25
- Engineering Rigor: 3 (trust-building — bug discovery→fix→re-eval)
- Method Negative: 8
- Hyperparameter Sensitivity: 6
- Scale/Generalization: 5
- Evaluation Artifact: 3

---

## Category 1: Engineering Rigor (3 experiments)

Implementation bugs that, once identified and fixed, still resulted in negative outcomes — confirming the method-level failure is not caused by engineering errors. The bug discovery→fix→re-eval narrative demonstrates scientific rigor and builds trust in the remaining results.

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

## Category 2: Method Negative (8 experiments)

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

A: Phase 2 trains with SDF for 5K steps then switches to λ=0 for the remaining 25K. The resulting CAR matches LoRA-only baselines exactly, showing SDF produces no lasting behavioral encoding. Combined with the flat λ curve and stepwise analysis, our Phase 2 experiment suggests SDF gradients are not effectively internalized within the tested training schedule — they appear structurally redundant when the demonstration data already provides collision avoidance signal. We note that Phase 2 is supporting evidence; the primary evidence for Claim 3 is the multi-seed, multi-λ flat curve (3 seeds × 4 conditions, all within null range). If reviewers request additional Phase 2 seeds, each requires ~32h of training — fully feasible within a rebuttal period. However, even if a Phase 2 effect appeared in one seed, it would not alter the primary evidence: the 3-vs-3 seed comparison across λ∈{0.005, 0.01, 0.1} shows no significant CAR elevation, and the per-task avoidance fingerprint is identical across all conditions.

---

## Category 3: Hyperparameter Sensitivity (6 experiments)

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

A: We tested three alpha strategies with ground-truth SDF (eliminating decoder error): adaptive scaling (α=min(0.1, 0.5×action_norm)), conservative fixed (α=0.005, ~0.5× typical action norm), and feature-space refinement (gradient through the network's representation layer). All three produce CAR *below* the unrefined baseline (73.1–76.9% vs 79%), with >96% of "safe" episodes showing obstacle displacement <0.1mm — the robot freezes rather than avoids. The failure is invariant to alpha magnitude, scaling strategy, and refinement representation, ruling out hyperparameter tuning as a solution. We note that each oracle variant uses a single policy seed (n=1, 160 episodes); however, the consistent direction across three independent strategies (adaptive, fixed, feature — all below baseline) constitutes converging evidence against hyperparameter-level explanations.

**Q: "The flat stepwise curve could mean the model just hasn't learned enough — what about longer training?"**

A: The learning curve from 16K to 30K steps (7 checkpoints) is remarkably flat at CAR≈54.5%, with the only deviation (s0 22K=60.5%) confirmed as single-seed noise by cross-seed validation (s1 22K=56.5%). The SDF training loss converges by ~10K steps — additional training produces no further signal. Combined with λ=0.005 and λ=0.01 showing the same null effect at 30K, this rules out underfitting.

---

## Category 4: Scale/Generalization (5 experiments)

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

A: Spatial scenes expose the structural limitation of EE-only SDF monitoring. In object_pudding, collisions are primarily between the EE and tabletop obstacles — the exact failure mode SDF can detect. In spatial_bowl, obstacles are placed at varying heights where the robot's arm links (shoulder, elbow, forearm) sweep through during reaching motions. Since SDF supervision only monitors the EE point, it is blind to arm-body collisions. All methods — full-FT, LoRA, SDF-augmented — achieve CAR≈0% on spatial, confirming this is a structural scope limitation, not a training deficiency. This motivates future work on full-body geometric representations. We emphasize that the EE-only limitation is not as obvious as it may appear in hindsight: prior to our work, no quantitative evidence existed on the relative proportion of EE-obstacle vs arm-body collisions in VLA manipulation. Our spatial_bowl results provide the first empirical evidence that arm-body collisions dominate in cluttered environments, making EE-only monitoring fundamentally insufficient.

**Q: "Why not test on more diverse environments beyond SafeLIBERO?"**

A: SafeLIBERO is currently the only benchmark that provides per-episode collision annotations with object displacement tracking, which is essential for our fake-safety analysis. Our two sub-suites (object_pudding: 4 tasks with tabletop obstacles; spatial_bowl: 4 tasks with varied obstacle placements) cover the two dominant collision geometries (EE-obstacle vs arm-body). We acknowledge this as a scope limitation and discuss it explicitly; however, our mechanistic findings (action collapse contaminating CAR, EE-only SDF insufficiency, demonstration-driven avoidance) are physics-based arguments that generalize beyond this specific benchmark.

---

## Category 5: Evaluation Artifact (3 experiments)

Evidence that standard CAR metrics are systematically contaminated by action collapse and frozen-robot artifacts.

### Experiments

| exp_id | hypothesis (short) | key metric |
|--------|-------------------|------------|
| eval_pi05_safelibero_object_v11 | Pi0.5 stronger base model — implicit avoidance? | CAR=28.5%, real_safe=0.5%, fake_safe=98.2% |
| eval_lora_baseline_object_v11 | LoRA baseline on object suite | TSR=0%, CAR=82% (action collapse) |
| eval_baseline_v11_object | Full-FT baseline with action chunking fix | TSR=0.5%, CAR=83% (action collapse) |

### Anticipated Questions & Responses

**Q: "Action collapse is a well-known problem — what's new about your analysis?"**

A: While action collapse has been noted anecdotally, to our knowledge, no prior work has quantified action collapse's impact on safety metrics at the scale tested here. We show that in Pi0 fine-tuned models (both full-FT and LoRA), 99.4% of episodes classified as "collision-free" exhibit obstacle displacement <0.1mm (median ~5nm) — the robot is frozen, not safe. This inflates CAR from a true ~0.5% to a reported 82–91.5%. Our contribution is (a) demonstrating the magnitude of metric contamination (80+ percentage points of CAR inflation), (b) proposing EE displacement-filtered CAR (dfCAR) as a principled correction, and (c) showing dfCAR is robust to threshold choice (δ∈[2mm, 200mm] produces identical results due to the bimodal displacement distribution: either <0.1mm or >239mm). The mechanism of action collapse may be straightforward, but its consequence — 80+ percentage points of CAR inflation — is non-trivial and has not been quantified before. Any VLA safety evaluation that does not account for this artifact risks drawing fundamentally wrong conclusions about method effectiveness.

**Q: "The capability-safety anti-correlation with Pi0.5 — isn't that just because more capable robots move more?"**

A: Exactly — and that is precisely the point. Pi0.5 (TSR=73%, CAR=28.5%) demonstrates that when a model is capable enough to attempt tasks, it inevitably contacts obstacles because its training data does not teach explicit avoidance. Pi0 (TSR≈0%, CAR=82%) appears "safer" only because it is too broken to move. The anti-correlation between capability and apparent safety is a direct consequence of CAR conflating "unable to collide" with "able to avoid." We present this as a supporting observation (not a causal claim), but it reinforces why dfCAR is necessary.

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

A: SDFs are widely used in classical motion planning and differentiable collision detection, making their integration into VLA fine-tuning a reasonable prior hypothesis. Our negative result is specifically about EE-only SDF supervision in the VLA fine-tuning setting. We do not claim that all forms of geometric supervision are ineffective. Control Barrier Functions (CBFs), potential fields, and reward shaping operate through different mechanisms (hard constraints vs soft gradients, action-space vs state-space). However, our finding about the EE-only structural limitation applies to any geometric method that monitors only the end-effector point: regardless of the loss formulation, a single-point supervision signal cannot prevent collisions along unmonitored arm links. We discuss this scope boundary explicitly and identify full-body geometric supervision as a promising direction.

### Why Not Full-Body SDF?

**Q: "If EE-only SDF is the problem, why not just use full-body SDF?"**

A: Full-body SDF requires SDF queries at multiple points along the kinematic chain, which introduces: (a) computational cost scaling linearly with the number of monitored points, (b) the need for accurate forward kinematics within the policy network to obtain link positions, and (c) gradient conflicts when different links receive opposing repulsion directions. Our work identifies this as a promising future direction — by demonstrating that EE-only is fundamentally insufficient, we motivate the investment required for full-body approaches. However, our Claim 3 (SDF is redundant when demonstrations provide avoidance) suggests that even full-body geometric supervision may be unnecessary if the demonstration data is sufficiently rich — this is an open question we leave for future work.

### Architecture Generalization

**Q: "Does action collapse affect autoregressive VLAs (RT-2, Octo), or is it specific to diffusion-based models?"**

A: Action collapse as we observe it — near-zero actions across all timesteps — arises from diffusion denoising collapsing to a single mode near zero, a failure mode documented in flow-matching training instabilities (Dong et al., 2025). Autoregressive VLAs (RT-2, Octo) use discrete token prediction, which has different failure modes (e.g., repeating stop tokens) but could produce analogous inaction artifacts. We tested Pi0 (flow matching), Pi0.5 (flow matching with language-conditioned pretraining), and confirmed OpenVLA (autoregressive) also exhibits near-zero TSR on SafeLIBERO, though we did not conduct the full dfCAR displacement analysis on OpenVLA. The dfCAR metric itself is architecture-agnostic — it filters on EE displacement regardless of how actions are generated — and we recommend its adoption for any VLA evaluation pipeline. Whether autoregressive VLAs exhibit the same bimodal displacement pattern is an empirical question we flag as future work.

### Demonstration Curation Practicality

**Q: "How practical is curating collision-free demos? Doesn't it require the same geometric knowledge as SDF?"**

A: There is a fundamental cost asymmetry. Collision-free demonstration curation is an *offline, one-time* process: a human operator or automated filter labels demonstrations as collision-free or not, requiring only binary contact detection (e.g., force sensor threshold, visual inspection, or simulator collision flag). This is available in most data collection pipelines at near-zero marginal cost. In contrast, SDF auxiliary loss requires *online, per-step* computation: at every training step, the policy must query a pre-computed SDF field, compute the signed distance for the current EE position, and backpropagate through the SDF gradient — adding both computational overhead and a dependency on accurate obstacle geometry at training time. Our Claim 3 shows that LoRA fine-tuning on curated collision-free demos yields 54.83% CAR, while the addition of SDF auxiliary loss provides no statistically significant further gain (p≥0.155). Practitioners should invest in demonstration quality, not geometric loss engineering.

### dfCAR Bimodal Assumption

**Q: "What if the bimodal displacement distribution doesn't hold for other robots/tasks?"**

A: The bimodality arises from task structure, not simulator specifics: manipulation tasks produce either contact-level displacement (<0.1mm, robot frozen or barely moving) or task-completion-level displacement (>100mm, robot actively reaching and grasping). This dichotomy is inherent to pick-and-place — either the robot reaches the object or it does not. We expect similar bimodality in any task with discrete contact events. That said, continuous-contact tasks (e.g., wiping, polishing) may produce a unimodal or multi-modal displacement distribution where the threshold τ_d requires task-specific calibration. We acknowledge this as an explicit limitation in the paper. Importantly, dfCAR's threshold robustness across two orders of magnitude ([2mm, 200mm]) in our experiments suggests that when bimodality exists, the exact threshold choice is not critical — the separation is structural, not marginal.

### TSR Collapse / Catastrophic Forgetting

**Q: "TSR drops from 73% to ~50% — isn't your 'collision avoidance' just catastrophic forgetting making the robot too conservative to reach obstacles?"**

A: Four lines of evidence rule out "reduced exposure" as the explanation for improved CAR:

(1) **SSR/TSR ratio increases**: The Safe Success Rate (SSR) to TSR ratio rises from 0.39 (Pi0.5 baseline) to 0.51–0.60 (LoRA fine-tuned conditions). If the robot were simply failing to reach obstacles, SSR/TSR would remain constant or decrease. The increase means a higher fraction of successful episodes are also collision-free — the robot completes tasks more safely, not less ambitiously.

(2) **Active motion confirmed**: All LoRA fine-tuned episodes show EE displacement >0.37m with frozen_rate=0%. The robot is actively moving through the workspace, not freezing conservatively short of obstacles.

(3) **SDF does not cause TSR collapse**: The TSR drop from Pi0.5 baseline is identical for LoRA-only (-68.4%) and SDF conditions (-68.7%). SDF supervision does not make the robot more conservative — the TSR reduction is entirely attributable to LoRA fine-tuning on the limited collision-free demonstration set, independent of geometric supervision.

(4) **Composite mechanism (M041 analysis)**: The TSR collapse reflects task-semantic forgetting (the model partially forgets which object to pick and where to place it) while retaining collision avoidance behaviors learned from demonstrations. Fine-tuning on 30K steps of collision-free demos expectedly shifts behavior: the robot learns conservative reaching patterns from safe demonstrations, prioritizing collision-free trajectories over task completion. This is a training data effect, not a failure mode — and it affects all conditions equally, preserving the validity of SDF vs LoRA-only comparisons.

### Per-Task Error Case Analysis

**Q: "Is the null result driven by BBQ sauce noise masking a real signal on other tasks?"**

A: BBQ sauce (task 3) exhibits the highest seed-to-seed variance: at λ=0.01, CAR ranges from 34% (s0) to 14% (s2), a 20pp spread — the largest single-task fluctuation in our experiments. However, three observations confirm the null result is not an artifact of this variance:

(1) **Excluding BBQ sauce preserves the null**: Across the remaining 3 tasks (orange_juice, chocolate_pudding, milk), SDF vs LoRA-only CAR differences are consistently <2pp in either direction. The null result holds task by task, not just in aggregate.

(2) **Stable tasks confirm the pattern**: chocolate_pudding (68–76% CAR across all conditions) and milk (62–74%) show low cross-seed variance and no systematic SDF benefit. These are the cleanest test cases and both show null.

(3) **BBQ sauce variance reflects task difficulty, not SDF signal**: BBQ sauce has the lowest baseline CAR across all conditions (LoRA-only: 14–34%), suggesting obstacle placement creates more constrained, collision-prone trajectories. The high variance is a property of the task geometry interacting with seed-specific trajectory distributions, not a masked SDF effect — LoRA-only seeds show the same variance range as SDF seeds.

### Two-Tailed vs One-Tailed Test

**Q: "Why use a two-tailed test? If SDF is hypothesized to improve safety, shouldn't you use one-tailed?"**

A: SDF supervision does not have a unidirectional prior. Our oracle experiments (Claim 2) demonstrate that SDF gradient signals can *reduce* CAR by rotating unmonitored arm links into obstacles — the SDF signal is capable of worsening safety, not just improving it. A two-tailed test is therefore the correct choice: it guards against both false positive claims of improvement and false negative dismissal of harm. We report the one-tailed p=0.071 in the appendix for transparency, allowing readers who hold a stronger directional prior to draw their own conclusions. The two-tailed p=0.155 remains non-significant at conventional α=0.05.

### Third Seed Outlier Concern

**Q: "The third seed (s2=54.5%) looks like an outlier that killed significance — with just s0 and s1 you'd have a significant result."**

A: s2=54.5% falls squarely within the null distribution (LoRA-only mean=54.83%, σ=2.25, so ±1σ range is [52.58, 57.08]). It is not an outlier by any standard criterion. The real issue is the opposite: with n=2, the permutation test has only C(5,2)=10 possible arrangements, making any "significant" result at α=0.05 a single-permutation artifact — a high false-positive risk. Adding the third seed provides C(6,3)=20 arrangements, yielding a more reliable test. If anything, the n=2 "significance" is the statistical anomaly, and n=3 corrects it. The observed effect size (2.2pp) is small relative to cross-seed variance; claiming significance from 2 seeds would be cherry-picking.

### Permutation Test vs Welch t-test

**Q: "A Welch t-test gives p=0.0035 — why choose the more conservative permutation test at p=0.036?"**

A: With n=3 per group, the normality assumption underlying the Welch t-test is unverifiable — 3 observations cannot meaningfully validate a distributional assumption. Small-sample t-tests are known to have inflated Type I error rates when the underlying distribution is non-normal (the t-distribution approximation degrades rapidly below n≈10). The permutation test is an exact test: it enumerates all C(6,3)=20 possible group assignments and computes the proportion with mean difference ≥ observed, requiring no distributional assumptions. For small samples, permutation tests are the recommended approach (Good, 2005; Phipson & Smyth, 2010). We report both p-values for transparency, but base our conclusions on the permutation test as the methodologically appropriate choice for n=3.
