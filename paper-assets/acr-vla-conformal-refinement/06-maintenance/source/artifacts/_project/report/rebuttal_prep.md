# Rebuttal Preparation — ACR-VLA Conformal Refinement

> Generated: 2026-05-29 | Pre-submission anticipated reviewer questions

---

## Q1: Why no head-to-head comparison with A2C2?

A2C2 and our method address fundamentally different failure modes of frozen VLA deployment. A2C2 targets **temporal staleness**: within an action chunk, later steps become outdated as the environment evolves, so A2C2 learns a correction head that updates stale chunk actions using new observations at each timestep. This requires modifying the VLA's chunk execution mechanism and training with online RL (PPO). Our method targets **initial action quality**: the first action sample from the VLA may already be suboptimal, and we learn a residual correction on the selected action *before* execution. Our CRM is trained offline with supervised L2 loss on demonstration data, requires no RL, and never modifies VLA weights or the chunk execution loop.

The experimental settings are also incompatible: A2C2 trains SmolVLA from scratch on LIBERO (reaching 67–72% baselines), whereas we evaluate on the publicly released pretrained SmolVLA checkpoint (79–84% baselines on short suites). A direct SR comparison would conflate the correction mechanism with the base policy quality. We cite A2C2 as the closest concurrent work and note that the two approaches are orthogonal and potentially combinable: A2C2 could correct temporal staleness within a chunk whose initial action was already refined by our gating pipeline.

---

## Q2: Why only a 3-layer MLP? Could a stronger CRM resolve overcorrection?

The lightweight architecture (~327K parameters) is a deliberate design choice, not a limitation of compute budget. A more expressive CRM increases correction capacity but simultaneously amplifies the overcorrection risk that is the paper's central finding: unconditional correction degrades all four suites precisely because the CRM injects noise on confident steps.

Our negative results provide direct evidence that "richer ≠ better." Per-DOF uncertainty conditioning gives the CRM strictly more input information than observation-only conditioning, yet causes progressive collapse: SR drops to 0% with uncapped magnitude and recovers only to 4–6% even at ε=0.3 (17 experiments; Appendix, §Negative Results). Similarly, alternative multi-loss training objectives (conformal-guided, combined, per-DOF weighted) all perform 2.5–43× worse than simple L2 loss. These results show that increasing correction expressiveness without gating amplifies failure modes rather than resolving them.

The paper's thesis is that the bottleneck is *when* to correct, not *how strongly*. The τ-gating mechanism recovers up to +13.5pp over unconditional correction using the same lightweight CRM—demonstrating that gating matters more than architecture capacity.

---

## Q3: Why no ablation on CRM training data quantity?

The 10 demonstrations per task used for CRM training is the standard LIBERO configuration: the LIBERO benchmark provides exactly 50 demonstrations per task, and 10 demos/task is the canonical few-shot setting used by SmolVLA, A2C2, ReconVLA, and other LIBERO evaluations. We follow this convention to ensure comparability with prior work.

The CRM training data is derived from these demonstrations: at each demonstration timestep, we cache K=10 VLA forward passes and train the CRM to predict the residual from the argmin-selected action to the expert action. The total training set (~88K samples across 30 tasks) is thus determined by the number of demonstration steps, not a tunable hyperparameter. Varying the number of demonstrations would conflate CRM data quantity with task coverage (fewer demos = fewer tasks or fewer trajectories per task), making the ablation difficult to interpret cleanly.

We note that the leave-task-out experiment (Appendix, §Negative Results) provides an indirect data coverage ablation: removing 5/10 tasks from CRM training drops SR from ~78% to ~2%, showing that CRM performance is highly sensitive to task coverage rather than sample count per task.

---

## Q4: Statistical power is insufficient (n=3 seeds, π₀.₅ n=1)

We address statistical power through multiple complementary strategies:

**Extended analysis.** On Spatial, an 8-seed paired analysis yields Δ=+1.4pp with p=0.017 (paired t-test, α=0.05), reaching conventional significance (Appendix, Table 6). Six of eight seeds show positive improvement.

**Effect size.** The CRM always-on degradation on Long (−14.8pp, from 58.0% to 43.2%) has an extremely large effect size. With n=3 seeds and std~2pp, Cohen's d exceeds 5—even n=2 would yield p<0.05. The paper's primary claim is the *degradation pattern* (unconditional correction hurts), not a small positive improvement, and the degradation effects are unambiguous.

**Cross-suite consistency.** The claim does not rest on any single suite's significance. CRM always-on degrades all 4/4 suites on SmolVLA and all 4/4 suites on π₀.₅—a pattern probability of (1/2)⁸ = 0.4% under the null hypothesis of random direction. This cross-suite consistency is the primary evidence.

**π₀.₅ hedging.** All π₀.₅ results are explicitly labeled "preliminary" with "suggest" language throughout (Abstract, Experiments, Conclusion). The paper does not claim statistical significance for π₀.₅; it claims pattern consistency across model scale.

---

## Q5: Why no real-robot experiments?

LIBERO is the standard simulation benchmark for VLA evaluation in the manipulation community. Among the most closely related concurrent works: A2C2 evaluates on LIBERO simulation only, ReconVLA uses LIBERO simulation, SC-VLA uses MetaWorld and LIBERO simulation, and VLA-Pilot uses simulation environments. Our evaluation setting is consistent with current community practice.

The paper's contribution is analytical: systematically characterizing when learned correction helps vs. hurts, and proposing calibrated gating as the solution. This analysis requires controlled, reproducible experiments with sufficient seeds and ablations—requirements that are prohibitively expensive on real hardware (each suite evaluation = 200 rollouts × 300 max steps). The 1,200+ experiments reported in this paper (including 97 negative results documented in the appendix) would be infeasible on physical robots.

Sim-to-real transfer is an orthogonal challenge that affects the base VLA policy, the CRM, and the gating threshold independently. We list real-robot transfer as future work in the Limitations section. We note that the gating mechanism's trigger rate provides a built-in deployment diagnostic: practitioners can inspect it on a new domain to assess whether the CRM is firing appropriately before committing to physical deployment.
