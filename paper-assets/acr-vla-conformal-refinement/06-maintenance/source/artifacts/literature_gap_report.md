# Literature Gap Report: ACR-VLA Conformal Refinement

Generated: 2026-05-15 | Target: CoRL 2026

---

## Gap 1: Supervised (Non-RL) Residual Correction for Robot Control

**Why needed**: CRM uses supervised L2 loss to expert actions, not RL/policy gradient. Existing residual policy references (Silver 2018, PLD, DRC) are RL-based. Need supervised correction precedents to position CRM correctly.

### Papers

| # | Key | Title | Authors | Year | Venue | Summary | Relation |
|---|-----|-------|---------|------|-------|---------|----------|
| 1 | `cai2025cr_dagger` | Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections | Cai et al. | 2025 | NeurIPS 2025 | Learns supervised residual corrections from human delta corrections via compliance control interface; no RL. +64% on contact-rich tasks. | **support** — closest supervised residual paradigm to CRM; both learn corrections from demonstration data |
| 2 | `rac2025` | RaC: Robot Learning for Long-Horizon Tasks by Scaling Recovery and Correction | — | 2025 | arXiv:2509.07953 | Supervised fine-tuning on human intervention trajectories (recovery + correction segments). DAgger-style supervised correction scaling. 10x fewer data than prior SOTA. | **support** — demonstrates supervised correction data suffices without RL reward signal |
| 3 | `xue2025reactive_diffusion` | Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation | Xue et al. | 2025 | RSS 2025 | Two-level architecture: slow diffusion policy (1-2 Hz) + fast supervised correction module (20-30 Hz) using real-time tactile/force feedback. | **support** — structural precedent for slow-generate + fast-correct pipeline; fast module is supervised, not RL |
| 4 | `ross2011dagger` | A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning | Ross, Gordon & Bagnell | 2011 | AISTATS 2011 | Classic DAgger algorithm: iterative supervised correction from expert queries. Reduces compounding error from O(T^2) to O(T). | **background** — foundational supervised correction framework; CRM can be viewed as single-round offline DAgger |

### Summary for paper
CRM's supervised residual correction has precedent in CR-DAgger (learns delta corrections from human demonstrations), RaC (supervised fine-tuning on correction data), and Reactive Diffusion Policy (fast supervised correction module). Unlike RL-based residual methods (Silver 2018, PLD), these approaches learn corrections directly from demonstration data, matching CRM's offline supervised training paradigm.

---

## Gap 2: Uncertainty-Conditioned Negative Results Precedent

**Why needed**: Our core negative result — per-DOF conformal features (40D) add no value over observation features for correction conditioning — needs precedent. We need papers showing that richer uncertainty representations can fail to improve downstream tasks.

### Papers

| # | Key | Title | Authors | Year | Venue | Summary | Relation |
|---|-----|-------|---------|------|-------|---------|----------|
| 1 | `ovadia2019trust_uncertainty` | Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift | Ovadia, Fertig, Ren, Nado, Sculley, Nowozin, Dillon, Lakshminarayanan & Snoek | 2019 | NeurIPS 2019 | Systematic evaluation showing uncertainty methods degrade under distribution shift. Post-hoc calibration (temperature scaling) can make things *worse* under shift. Deep ensembles (simplest method) outperform sophisticated Bayesian approaches. | **support** — precedent that UQ methods fail under shift; CP features computed from shifted distributions may carry corrupted signal |
| 2 | `lakshminarayanan2017ensembles` | Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles | Lakshminarayanan et al. | 2017 | NeurIPS 2017 | Simple ensemble approach outperforms more complex Bayesian methods. The simplest UQ representation consistently works best. | **support** — already in map; establishes "simpler is often better" principle for uncertainty representations |
| 3 | `tang2026shifting_uncertainty` | Shifting Uncertainty to Critical Moments: Towards Reliable UQ for VLA Models | Tang et al. | 2026 | arXiv:2603.18342 | Identifies "Averaging Trap" where mean aggregation dilutes critical uncertainty spikes. Standard uncertainty representations lose task-critical information. | **support** — already in map; shows how UQ representations can lose information relevant to downstream tasks |

### Summary for paper
Our negative result is consistent with (a) Ovadia et al.'s finding that UQ degrades under distribution shift (our evaluation is explicitly OOD), (b) the "simpler is better" principle from deep ensembles, and (c) Tang et al.'s "Averaging Trap" showing UQ representations lose critical information. **However, a direct precedent for uncertainty features being redundant when used as policy conditioning is notably absent in the literature, making our negative result a genuinely novel empirical finding.** This strengthens the contribution.

---

## Gap 3: Object Manipulation vs Spatial Robustness Taxonomy

**Why needed**: CRM improves object perturbation tasks (+8pp) but not spatial perturbation tasks (approx 0pp). Need references establishing why these perturbation types differ in difficulty and what mechanisms handle each.

### Papers

| # | Key | Title | Authors | Year | Venue | Summary | Relation |
|---|-----|-------|---------|------|-------|---------|----------|
| 1 | `xu2025libero_pro` | LIBERO-PRO: Towards Robust and Fair Evaluation of VLAs Beyond Memorization | Xu et al. | 2025 | arXiv:2510.03827 | Systematic robustness evaluation across 4 perturbation dimensions. Reveals VLAs collapse to 0% under spatial perturbation. Models exploit spatial memorization. | **support** — establishes that spatial perturbations require re-planning (not correctable by residual), explaining our spatial null result |
| 2 | `wang2024gendp` | GenDP: 3D Semantic Fields for Category-Level Generalizable Diffusion Policy | Wang et al. | 2024 | CoRL 2024 | Uses 3D semantic fields for category-level object generalization. Separates geometric/semantic representation from spatial layout. 20% -> 93% on unseen instances. | **support** — shows object-level generalization is achievable via semantic features; supports why CRM's observation features help with object but not spatial |
| 3 | `s2_diffusion_2025` | S^2-Diffusion: Generalizing from Instance-level to Category-level Skills in Robot Manipulation | — | 2025 | arXiv:2502.09389 | Spatial-Semantic Diffusion policy enabling instance-to-category transfer via foundation model features. Invariant to task-irrelevant visual factors. | **support** — shows object category generalization relies on semantic abstraction (correctable), while spatial generalization requires explicit spatial prediction (requires re-planning) |

### Summary for paper
LIBERO-PRO establishes that spatial perturbations are fundamentally harder because VLAs memorize spatial layouts. GenDP and S^2-Diffusion show object-level generalization can be achieved through semantic feature abstraction — the kind of information available in CRM's observation features. Spatial perturbations require re-planning rather than local action correction, explaining why CRM helps on object but not spatial benchmarks.

---

## Gap 4: Compounding Error in Action Prediction

**Why needed**: CRM's task-level variance (some tasks hurt by correction) and magnitude sensitivity (unbounded -> 0%) relate to compounding error. Need theoretical grounding.

### Papers

| # | Key | Title | Authors | Year | Venue | Summary | Relation |
|---|-----|-------|---------|------|-------|---------|----------|
| 1 | `ross2011dagger` | A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning | Ross, Gordon & Bagnell | 2011 | AISTATS 2011 | Proves compounding error grows as O(T^2) for behavior cloning. DAgger reduces to O(T) via iterative expert queries. | **background** — foundational theory; CRM's magnitude control directly addresses error compounding |
| 2 | `laskey2017dart` | DART: Noise Injection for Robust Imitation Learning | Laskey, Lee, Fox, Dragan & Goldberg | 2017 | CoRL 2017 | Injects optimized noise into demonstrations to train policies robust to distribution shift. 3x faster than DAgger with 62% improvement over vanilla BC. | **support** — demonstrates compounding error can be mitigated without online interaction; analogous to CRM's offline training |
| 3 | `somalwar2025imperfect_models` | Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error | Somalwar et al. | 2025 | arXiv:2504.01766 | Proves that under model misspecification, multi-step predictors reduce bias. Well-specified models favor single-step. | **extend** — theoretical framework for when correction helps vs hurts; explains CRM's differential performance across tasks |

### Summary for paper
CRM's magnitude sensitivity (unbounded correction -> 0% success) directly illustrates compounding error: residual errors accumulate over the action chunk horizon. Ross et al.'s O(T^2) bound explains the phase transition at high magnitude. DART shows offline robustness training can mitigate compounding without online interaction. Somalwar et al. provide a framework for understanding when correction helps (object tasks with correctable misspecification) vs. hurts (tasks where correction introduces new misspecification).

---

## Gap 5: Conformal Prediction as Feature Extractor Precedent

**Why needed**: ACR-VLA's core novelty — using CP nonconformity scores as input features to a downstream MLP rather than for calibration/coverage — needs positioning.

### Papers

| # | Key | Title | Authors | Year | Venue | Summary | Relation |
|---|-----|-------|---------|------|-------|---------|----------|
| 1 | `huang2023feature_cp` | Predictive Inference with Feature Conformal Prediction | Huang et al. | 2023 | ICLR 2023 | Deploys CP in learned feature space rather than output space. Uses surrogate features for nonconformity scores. Provably tighter intervals. | **contrast** — opposite direction (CP *in* feature space vs. our CP scores *as* features), but establishes the bridge between CP and representation learning |
| 2 | `lekeufack2024conformal_decision` | Conformal Decision Theory: Safe Autonomous Decisions from Imperfect Predictions | Lekeufack, Angelopoulos, Bajcsy, Jordan & Malik | 2024 | ICRA 2024 | Uses CP scores to calibrate decisions directly (not prediction sets). Applied to robot planning, manufacturing, trading. Distribution-free guarantees. | **support** — closest precedent for using CP beyond calibration; CP scores inform decision-making rather than just providing coverage |
| 3 | `jin2023selection_prediction` | Selection by Prediction with Conformal p-values | Jin & Candes | 2023 | JMLR 2023 | Uses conformal p-values for downstream screening/selection decisions with FDR control. CP scores inform candidate selection. | **support** — uses CP scores as informative signals for downstream task selection, paralleling CRM's use of CP features for correction conditioning |

### Summary for paper
The use of CP scores as input features to a learned downstream model is genuinely novel. Closest precedents: Feature CP (deploys CP within feature spaces — reverse direction), Conformal Decision Theory (uses CP scores to inform decisions, not as NN input), Selection by Prediction (conformal p-values for screening). **None use CP scores as literal input features to a learned model**, making ACR-VLA's approach a novel contribution — and the negative result all the more important, since it challenges what would be a natural extension of the emerging "CP-beyond-calibration" paradigm.

---

## Cross-Gap Synthesis

The five gaps connect through a coherent narrative:

1. **CRM is supervised, not RL** (Gap 1) — enables offline training without environment interaction
2. **Simpler observation features suffice** (Gap 2) — per-DOF CP features are redundant, a genuinely novel negative finding
3. **Object != Spatial** (Gap 3) — correction helps where semantic features are informative (objects), not where re-planning is needed (spatial)
4. **Magnitude control prevents compounding** (Gap 4) — unbounded corrections destroy trajectories due to error accumulation
5. **CP as features is novel but didn't work** (Gap 5) — using CP beyond calibration is an emerging paradigm, but our negative result provides a cautionary data point

Total new references to add: 12 papers (3 already referenced in existing map).
