# Related Work Survey: Pi0.5 + SDF Auxiliary Loss for Collision Avoidance

**Date:** 2026-05-23

---

## 1. VLA Safety / Collision Avoidance

#### SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning (NeurIPS 2025 Spotlight)
- **Authors:** Borong Zhang et al. (PKU-Alignment)
- **Core method:** Models VLA safety as a Constrained MDP (CMDP). Uses min-max optimization to align VLA policies against elicited safety risks via safe RL. Systematically elicits diverse unsafe behaviors, then constrains the policy to avoid them.
- **Key results:** Reduces cumulative cost of safety violations by 83.58% vs. SOTA while maintaining task success rate (+3.85%).
- **Relation to our work:** Competitor / complementary. SafeVLA uses RL-based constrained optimization at the policy level; we embed geometric safety (SDF) as an auxiliary loss during training. SafeVLA requires online RL fine-tuning, our SDF auxiliary loss is a simpler supervised signal. The two approaches could be combined.
- **URL:** https://arxiv.org/abs/2503.03480

#### VLSA (AEGIS): Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer (arXiv 2025)
- **Authors:** Songqiao Hu, Zeyi Liu, Shuang Liu, Jun Cen, Zihan Meng, Xiao He (Tsinghua)
- **Core method:** Adds a plug-and-play safety constraint (SC) layer based on Control Barrier Functions (CBF) on top of existing VLA models. Uses VLM-based safety assessment + open-set detection + depth, then a CBF-based QP solver minimally adjusts VLA actions to guarantee collision-free execution.
- **Key results:** 59.16% improvement in obstacle avoidance rate and 17.25% increase in task success rate on SafeLIBERO benchmark. Outperforms Pi0.5 (68.13% vs 50.88%).
- **Relation to our work:** **Most direct competitor.** Both add safety to VLA models, but AEGIS does it at **inference time** (post-hoc CBF-QP correction), while we integrate safety at **training time** via SDF auxiliary loss. Our approach learns inherently safer policies rather than relying on runtime corrections. AEGIS's SafeLIBERO benchmark is useful for evaluation.
- **URL:** https://arxiv.org/abs/2512.11891

#### CoFreeVLA: Collision-Free Dual-Arm Manipulation via VLA Model and Risk Estimation (arXiv 2026)
- **Authors:** Xuanran Zhai, Binkai Ou, Qiaojun Yu, Ce Hao, Yaohua Liu et al.
- **Core method:** Augments VLA with a short-horizon self-collision risk estimator from proprioception, visual embeddings, and planned actions. Gates risky commands and recovers to safe states. Risk estimator pre-trained with model-based collision labels.
- **Key results:** Reduces self-collisions and improves success rates vs. RDT and APEX on five bimanual tasks.
- **Relation to our work:** Technique to borrow. CoFreeVLA's collision risk estimator is conceptually similar to our SDF auxiliary head -- both predict a geometric safety signal alongside the action. Key difference: CoFreeVLA uses binary collision labels while we use continuous SDF values providing richer gradient information.
- **URL:** https://arxiv.org/abs/2601.21712

#### SAFE: Multitask Failure Detection for Vision-Language-Action Models (NeurIPS 2025)
- **Authors:** Gu, Ju, Sun, Gilitschenski, Nishimura, Itkina, Shkurti
- **Core method:** Learns a failure detector from VLA internal features that predicts task failure likelihood. Discovers that VLA feature spaces already encode success/failure information, enabling zero-shot failure detection on unseen tasks.
- **Key results:** SOTA failure detection on OpenVLA, Pi0, and Pi0-FAST in sim and real.
- **Relation to our work:** Complementary. SAFE detects failures post-hoc from VLA features rather than preventing them. Their finding that VLA features encode safety-relevant information supports our hypothesis that an SDF auxiliary head can effectively leverage VLA internal representations.
- **URL:** https://arxiv.org/abs/2506.09937

#### CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation (arXiv 2026)
- **Authors:** (arXiv 2601.15541)
- **Core method:** Augments VLA models with a VLM-informed context-aware variable impedance controller. VLM interprets task context to adapt stiffness/damping parameters, regulated by real-time force/torque feedback.
- **Key results:** Improves safety and effectiveness in contact-rich tasks vs. standard position-only VLA outputs.
- **Relation to our work:** Complementary -- addresses force/compliance safety rather than collision geometry. Could be combined: SDF prevents collisions in free space, impedance control handles intentional contact phases.
- **URL:** https://arxiv.org/abs/2601.15541

**Novelty gap:** No existing work integrates SDF-based geometric supervision as an auxiliary training loss within a VLA model. The landscape:

| Approach | When | Safety signal | Paper |
|---|---|---|---|
| RL constrained optimization | Training (RL) | Cost from unsafe rollouts | SafeVLA |
| CBF/QP post-hoc correction | Inference | Control barrier function | VLSA/AEGIS |
| Collision risk estimator | Inference (gating) | Binary collision prediction | CoFreeVLA |
| Failure detection | Post-hoc | VLA feature analysis | SAFE |
| Impedance control | Inference | Force/torque feedback | CompliantVLA-adaptor |
| **SDF auxiliary loss (ours)** | **Training (supervised)** | **Continuous signed distance** | **None** |

---

## 2. Fake Safety / Action Collapse in Robotics

**Overall assessment: Significant novelty gap.** No paper directly addresses the concept of a "frozen_rate" metric -- detecting and penalizing robots that achieve low collision rates merely by ceasing to move. The closest work falls into: (1) overly conservative safe RL policies, (2) action mode collapse in imitation/offline RL, (3) diffusion approaches handling multimodal actions.

#### FISOR: Safe Offline RL with Feasibility-Guided Diffusion Model (ICLR 2024)
- **Authors:** Yinan Zheng, Jianxiong Li, Dongjie Yu, Yujie Yang, Shengbo Eben Li, Xianyuan Zhan, Jingjing Liu
- **Core method:** Decouples safety constraint adherence, reward maximization, and offline policy learning. Uses Hamilton-Jacobi reachability to identify feasible region, then extracts policy via energy-guided diffusion model.
- **Key results:** Zero constraint violation in all tested tasks while achieving top returns. Explicitly addresses the tension where hard safety constraints can yield "overly conservative (near zero-reward) policies."
- **Relation to our work:** Acknowledges that naive safe offline RL can produce degenerate policies but doesn't define a metric to detect this. A frozen_rate metric would complement FISOR by quantifying when safety is achieved through inaction vs. genuine collision avoidance.
- **URL:** https://arxiv.org/abs/2401.10700

#### POLICEd RL: Learning Closed-Loop Robot Control with Provable Hard Constraints (RSS 2024)
- **Authors:** Jean-Baptiste Bouvier, Kartik Nagpal, Negar Mehr
- **Core method:** Makes the learned policy affine near unsafe state boundaries, using this affine region as a repulsive buffer that provably prevents constraint violations.
- **Key results:** Formal guarantees of hard constraint satisfaction in closed-loop execution.
- **Relation to our work:** Repulsive buffers near unsafe regions can cause robots to slow down or stop near obstacles -- exactly what frozen_rate detects. The paper does not measure or discuss this failure mode.
- **URL:** https://arxiv.org/abs/2403.13297

#### Learning on One Mode (LOM): Addressing Multi-modality in Offline RL (ICLR 2025)
- **Authors:** Mianchu Wang, Yue Jin, Giovanni Montana
- **Core method:** Uses GMM to decompose offline dataset's action distribution into modes, then applies weighted IL on only the highest-return mode. Avoids "mode averaging" where learning from multimodal data collapses to the mean (often near-zero) action.
- **Key results:** Outperforms standard offline RL methods on D4RL benchmarks, particularly in multi-modal scenarios.
- **Relation to our work:** Mode averaging is a direct mechanism producing frozen/near-zero actions: opposing motion directions average to zero velocity. frozen_rate is a diagnostic to detect when mode collapse produces inaction.
- **URL:** https://arxiv.org/abs/2412.03258

#### The Pitfalls of Imitation Learning when Actions are Continuous (COLT 2025)
- **Authors:** Max Simchowitz, Daniel Pfrommer, Ali Jadbabaie
- **Core method:** Theoretical analysis proving that for stable dynamics with smooth deterministic experts, any smooth deterministic imitator suffers execution error exponentially larger than training error.
- **Key results:** Formalizes why BC fails due to closed-loop feedback between imperfect policy and dynamics. Shows "sufficiently spread" expert trajectory distributions can mitigate the problem.
- **Relation to our work:** Provides theoretical grounding for why IL policies can degenerate, including potential freezing when the policy becomes uncertain and regresses toward mean actions. frozen_rate operationalizes detection of one specific failure mode this theory predicts.
- **URL:** https://arxiv.org/abs/2503.09722

#### CAPE: Context-Aware Diffusion Policy via Proximal Mode Expansion for Collision Avoidance (arXiv 2025)
- **Authors:** (arXiv 2511.22773)
- **Core method:** Expands trajectory distribution modes of a diffusion policy using context-aware priors and guided denoising. Generates initial plans, executes short prefixes, then re-denoises with collision-aware guidance.
- **Key results:** Up to 26% (sim) and 80% (real) higher success rates in cluttered unseen environments.
- **Relation to our work:** Addresses limited mode coverage in diffusion policies for collision avoidance. When a policy lacks diverse trajectory modes, it may freeze. Mode expansion is a generation-side solution; frozen_rate is the evaluation-side diagnostic.
- **URL:** https://arxiv.org/abs/2511.22773

**Novelty of frozen_rate:** The problem is acknowledged (FISOR, safe RL surveys note "overly conservative policies"), but no existing metric explicitly measures the fraction of time a robot is stationary when it should be acting. Treating frozen behavior as safety metric gaming is an original contribution.

---

## 3. SDF in Robot Manipulation

#### Representing Robot Geometry as Distance Fields (RDF) (ICRA 2024)
- **Authors:** Yiming Li, Yan Zhang, Amirreza Razmjoo, Sylvain Calinon
- **Core method:** Represents robot geometry as Robot Distance Fields using Bernstein polynomials to encode signed distance for each link. Continuous and differentiable, enabling direct use as cost functions for optimization-based planning.
- **Key results:** Demonstrated on 7-axis Franka for collision avoidance and whole-body manipulation, including dual-arm settings.
- **Relation to our work:** Borrowable technique. The Bernstein polynomial SDF encoding for robot links could compute the robot-side SDF in our auxiliary loss, providing accurate differentiable distance queries.
- **URL:** https://arxiv.org/abs/2307.00533

#### Configuration Space Distance Fields for Manipulation Planning (RSS 2024)
- **Authors:** Yiming Li, Xuemin Chi, Amirreza Razmjoo, Sylvain Calinon
- **Core method:** Computes Signed Distance Fields in configuration space (CDF) rather than task space. Neural MLP representation for compact, continuous C-space distances. Zero-level-set matches SDF, but CDF level sets have unit-norm gradients enabling one-step IK.
- **Key results:** Fewer iterations than task-space SDF for contact planning on 7-axis Franka.
- **Relation to our work:** Borrowable technique. CDF provides collision avoidance directly in joint space -- the space VLA models output actions in. Could yield better gradients than task-space SDF for the auxiliary loss.
- **URL:** https://arxiv.org/abs/2406.01137

#### iSDF: Real-Time Neural Signed Distance Fields for Robot Perception (RSS 2022)
- **Authors:** Joseph Ortiz, Alexander Clegg, Jing Dong, Edgar Sucar, David Novotny, Michael Zollhoefer, Mustafa Mukadam
- **Core method:** Continual learning system training a neural network online to map 3D coordinates to signed distances from a stream of posed depth images. Self-supervised, room-scale, real-time.
- **Key results:** More accurate reconstructions and better collision cost/gradient approximations vs. voxel-grid baselines.
- **Relation to our work:** Borrowable technique. Demonstrates how to construct differentiable SDF representations from depth images in real time -- exactly what's needed to compute SDF auxiliary loss during training or inference.
- **URL:** https://arxiv.org/abs/2204.02296

#### Neural NMPC through SDF Encoding for Collision Avoidance (IJRR 2025)
- **Authors:** Martin Jacquet, Marvin Harms, Kostas Alexis
- **Core method:** Encodes range images into SDF via convolutional encoder (latent vector) + MLP decoder (spatial SDF). SDF parametrizes position constraints in a velocity-tracking NMPC for map-free collision avoidance.
- **Key results:** Real-world collision avoidance in forest environments for aerial robots with adversarial references.
- **Relation to our work:** Borrowable architecture. The encoder-decoder (visual observation -> latent -> SDF) is transferable to our vision-conditioned SDF module for the auxiliary loss.
- **URL:** https://arxiv.org/abs/2511.21312

#### Composite SDF Networks for Collision-Free Motion of Articulated Robots (RA-L 2023)
- **Authors:** Baolin Liu, Gedong Jiang, Fei Zhao, Xuesong Mei
- **Core method:** Learns composite SDF networks to represent signed distance of articulated robots per link, enabling fast batch minimum distance estimation. Integrates into stochastic trajectory planner.
- **Key results:** Collision-free, time-optimal motion generation with fast and accurate distance estimation.
- **Relation to our work:** Borrowable technique. Composite SDF network architecture for articulated robots provides more accurate collision distance gradients for the auxiliary loss than scene-level SDF.
- **URL:** https://arxiv.org/abs/2306.04130

---

## 4. Safety Metrics for Robot Learning

#### SafeVLA (NeurIPS 2025 Spotlight)
- *(See Section 1 for full details)*
- **Metrics relevance:** Defines cumulative cost and violation rate for VLA manipulation evaluation, analogous to our collision_rate and frozen_rate.
- **URL:** https://arxiv.org/abs/2503.03480

#### Safety-Gymnasium: A Unified Safe RL Benchmark (NeurIPS 2023 D&B)
- **Authors:** Jiaming Ji, Borong Zhang, Jiayi Zhou, Xuehai Pan et al.
- **Core method:** Unified environment suite for safe RL (single/multi-agent) + SafePO library of 16 SOTA safe RL algorithms. Standardizes task definitions, constraint specifications, evaluation protocols.
- **Key results:** Benchmarks 16 safe RL algorithms with standardized metrics: cost rate, cost return, reward-cost trade-off curves.
- **Relation to our work:** "Cost rate" (violations per timestep) is conceptually identical to collision_rate. Evaluation protocol -- measuring task performance and safety simultaneously -- provides methodological template.
- **URL:** https://arxiv.org/abs/2310.12567

#### Robot Learning as an Empirical Science: Best Practices for Policy Evaluation (arXiv 2024)
- **Authors:** Hadas Kress-Gazit, Kunimatsu Hashimoto, Naveen Kuppuswamy et al.
- **Core method:** Surveys evaluation practices in robot learning. Argues the field over-relies on success rate. Proposes reporting multiple complementary metrics including safety-related ones and statistical significance.
- **Key results:** Meta-analysis showing most papers report only success rate. Complementary metrics (collision rate, completion time, smoothness) reveal important behavioral differences invisible to success rate.
- **Relation to our work:** Directly supports using collision_rate and frozen_rate as complementary metrics beyond success rate. Provides methodological justification for multi-metric evaluation.
- **URL:** https://arxiv.org/abs/2409.09491

#### GUARD: A Safe RL Benchmark (arXiv 2023)
- **Authors:** Weiye Zhao, Ruixuan Liu, Rui Chen, Tianhao Wei, Yifan Sun, Changliu Liu (CMU)
- **Core method:** Generalized Unified SAfe RL Development benchmark with configurable agents, tasks, and safety constraints. Supports state, action, and joint constraints.
- **Key results:** Comprehensive comparison of safe RL algorithms (CPO, PPO-Lagrangian, TRPO-Lagrangian) with constraint violation rate, episodic cost, reward-cost Pareto frontiers.
- **Relation to our work:** Flexible constraint specification framework is relevant for defining collision avoidance as a state constraint. Systematic comparison methodology parallels our evaluation approach.
- **URL:** https://arxiv.org/abs/2305.13681

#### Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms (arXiv 2026)
- **Authors:** Qi Li et al.
- **Core method:** Comprehensive survey of VLA safety covering five risk dimensions: irreversible physical consequences, multimodal attack surfaces, real-time latency constraints, error propagation over long horizons, data supply chain vulnerabilities.
- **Key results:** VLA safety evaluation requires metrics beyond traditional RL safety, including physical damage assessment, constraint violation severity, and temporal propagation of unsafe states.
- **Relation to our work:** Most directly relevant survey -- specifically addresses safety evaluation for VLA models. Contextualizes our collision_rate and frozen_rate metrics within the broader VLA safety landscape.
- **URL:** https://arxiv.org/abs/2604.23775

---

## 5. Auxiliary Loss for Safety

#### RAIL: Reachability-Aided Imitation Learning for Safe Policy Execution (ICRA 2025)
- **Authors:** Wonsuhk Jung, Dennis Anthony, Utkarsh A. Mishra et al.
- **Core method:** Builds a reachability-based safety filter on top of IL policies. Uses polynomial zonotopes to overapproximate the robot's continuous-time swept volume for fast collision checking, then intervenes when IL policy's action would collide.
- **Key results:** 0% collision rate vs. 5-35% for baseline IL policies, while maintaining task success.
- **Relation to our work:** Competitor / complementary. RAIL adds safety as a post-hoc filter over IL policies; we bake safety into the policy during training via SDF auxiliary loss. These strategies could be combined.
- **URL:** https://arxiv.org/abs/2409.19190

#### Learning to Recover for Safe RL (arXiv 2023)
- **Authors:** Haoyu Wang et al.
- **Core method:** Three-stage architecture (TU-Recovery) where safety critic and recovery policy are learned before task training. An auxiliary reward mitigates the "adversarial phenomenon" between task and recovery policies.
- **Key results:** Outperforms unconstrained baselines in both reward and constraint violations. Auxiliary reward significantly reduces constraint violations.
- **Relation to our work:** Borrowable technique. The idea of using an auxiliary reward/loss to shape task policy toward safety-aware behavior is directly analogous to our SDF auxiliary loss. Key difference: RL with learned recovery vs. our geometric loss in IL.
- **URL:** https://arxiv.org/abs/2309.11907

#### Reward Training Wheels: Adaptive Auxiliary Rewards for Robotics RL (IROS 2025)
- **Authors:** Linji Wang, Tong Xu, Yuanjie Lu, Xuesu Xiao
- **Core method:** Teacher-student framework (RTW) where a teacher monitors training signals and dynamically adjusts auxiliary reward weights during RL training.
- **Key results:** Outperforms expert-designed rewards by 2.35% success rate, 122.62% in off-road mobility. 35% and 3x faster training.
- **Relation to our work:** Borrowable technique. Adaptive weighting of auxiliary rewards is directly relevant -- a fixed SDF loss weight may be suboptimal across training stages. RTW's dynamic scheduling could improve SDF loss integration.
- **URL:** https://arxiv.org/abs/2503.15724

#### Differentiable Constrained Imitation Learning for Robot Motion Planning (arXiv 2023)
- **Authors:** Christopher Diehl, Janis Adamek, Martin Krueger, Frank Hoffmann, Torsten Bertram
- **Core method:** Integrates hard spatio-temporal constraints (dynamics, safety/obstacle boundaries) into IL via differentiable optimization layers. Argues soft-constraint approaches (auxiliary losses) can fail catastrophically in OOD scenarios.
- **Key results:** Hard constraint integration prevents safety violations that soft auxiliary losses cannot guarantee. Demonstrated on mobile robot and automated driving.
- **Relation to our work:** **Counterpoint.** Explicitly argues against soft auxiliary loss approaches. Important for positioning our contribution: SDF auxiliary loss is practical for high-dimensional VLA policies where differentiable hard constraints are intractable, trading formal guarantees for scalability.
- **URL:** https://arxiv.org/abs/2210.11796

#### Composite SDF Networks for Collision-Free Motion of Articulated Robots (RA-L 2023)
- **Authors:** Baolin Liu, Gedong Jiang, Fei Zhao, Xuesong Mei
- *(See Section 3 for full details)*
- **Relation to auxiliary loss:** Composite SDF network could serve as the geometric backbone for computing the SDF auxiliary loss in our VLA training pipeline.
- **URL:** https://arxiv.org/abs/2306.04130

---

## Summary

### Our positioning in the literature

This project -- adding SDF-based auxiliary loss to Pi0.5 VLA for collision avoidance -- sits at a unique intersection:

1. **Training-time geometric safety for VLA:** No existing work trains VLA models with continuous geometric safety signals (SDF) as auxiliary supervision. AEGIS/VLSA uses inference-time CBF correction; SafeVLA uses RL-based constrained optimization; CoFreeVLA uses binary collision gating. Our approach is the only one that embeds rich, differentiable geometric supervision directly into IL training.

2. **frozen_rate as evaluation metric:** No existing metric explicitly detects "fake safety through inaction." The problem is acknowledged (FISOR, safe RL surveys), but no one has proposed a dedicated metric. This is a clear novelty.

3. **SDF in VLA context:** SDF is well-established in traditional motion planning (RDF, CDF, iSDF) but has never been used as an auxiliary training signal within a VLA model. We bridge the gap between geometric planning and end-to-end VLA learning.

### Key papers to cite

| Paper | Why cite |
|---|---|
| VLSA/AEGIS (Hu et al., 2025) | Most direct competitor -- inference-time safety vs. our training-time safety |
| SafeVLA (Zhang et al., NeurIPS 2025) | RL-based VLA safety alignment -- different paradigm to contrast |
| CoFreeVLA (Zhai et al., 2026) | Closest architecture -- collision risk estimator alongside action output |
| iSDF (Ortiz et al., RSS 2022) | Foundation for neural SDF representation |
| RDF (Li et al., ICRA 2024) | Differentiable robot distance fields for articulated bodies |
| FISOR (Zheng et al., ICLR 2024) | Acknowledges conservative policy collapse -- motivates frozen_rate |
| Safety-Gymnasium (Ji et al., NeurIPS 2023) | Standard safe RL benchmark methodology |
| Diehl et al. (2023) | Important counterpoint -- hard vs. soft safety constraints |

### Key differentiators vs. closest competitors

| | AEGIS/VLSA | SafeVLA | CoFreeVLA | **Ours** |
|---|---|---|---|---|
| Safety integration | Inference-time CBF-QP | RL fine-tuning (CMDP) | Inference-time gating | **Training-time auxiliary loss** |
| Safety signal | Depth + detection | Learned cost | Binary collision | **Continuous SDF** |
| Requires retraining? | No | Yes (RL) | No | **Yes (supervised)** |
| Gradient quality | N/A | Sparse RL reward | Binary | **Dense, differentiable** |
| Formal guarantee? | Yes (CBF) | Probabilistic | No | **No (soft constraint)** |
| Scalability to VLA | Plug-and-play | Needs RL infra | Plug-and-play | **Native to IL pipeline** |
