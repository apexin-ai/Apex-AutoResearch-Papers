# Idea Brief: VLA-SSD: Do VLAs Know Which Demonstrations Are Good? Self-Referential Quality Scoring from Pretrained Representations


- **Idea ID**: `idea_004`
- **Created**: 2026-05-15
- **Approved**: 2026-05-15
- **Source**: foreign:be-idea-gen-0509-14
- **Level**: top-tier
- **Target Venues**: CoRL 2026 (abstract deadline May 26, full paper May 29, 2026), ICRA 2027 (~September 2026 deadline, backup if additional real-world validation needed), ICLR 2027 (~October 2026)

## Seed Topic

按照以下方向，生成1-2个优质idea，保质不求量：Seed 2: Reinforcement-Informed Demonstration Distillation for Noise-Robust VLA Training
Target: CoRL 2026 (Austin, Nov 9–12, 2026). Abstract deadline 2026-05-26 (12 days from today 2026-05-14); paper deadline 2026-05-29 (15 days).
Direction: RL-inspired experience scoring and filtering for VLA training data — methods that leverage data-intrinsic signals to identify and down-weight noisy, redundant, or suboptimal actions in real-world demonstration datasets before or during VLA fine-tuning. Real-world teleoperation data inevitably contains noise: hesitation pauses, corrective motions, grip fumbles, suboptimal trajectories, and redundant repeated actions. Standard behavioral cloning treats all timesteps equally, forcing the VLA to memorize noise as if it were signal — this is a fundamental source of brittleness. By borrowing the experience replay and advantage estimation machinery from offline RL, we can score each (state, action) pair by its contribution to task completion and filter or re-weight the training distribution accordingly. Unlike full offline RL (which replaces BC entirely), this approach retains the simplicity and stability of VLA fine-tuning while using RL-derived scores as a data curation signal. The key theoretical insight is that demonstration noise creates multi-modal action distributions at identical states, inflating the entropy of the learned policy; scoring and filtering collapses these modes to the high-performing subset, yielding a sharper, more robust policy.
Recent landscape (do not duplicate): Behavior Cloning, OpenVLA: An Open-Source Vision-Language-Action Model, FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models, PLD: Probe, Learn, Distill – Self-Improving Vision-Language-Action Models with Data Generation via Residual RL, REDI: Refined Policy Distillation: From VLA Generalists to RL Experts, GOLD: Guided Offline Learning from Demonstrations, SHS: An Offline Reinforcement Learning Algorithm Based on Selection of High-Quality Samples, PER: Prioritized Experience Replay, PRGS: Peak Reward Guided Trajectory Segmentation, What Can RL Bring to VLA Generalization? An Empirical Study, πRL: πRL: Manifold Policy Reinforcement Learning for Vision-Language-Action Models
Contribution type: METHOD ONLY. A two-stage demonstration distillation pipeline: (1) Temporal Advantage Scoring — train a lightweight value function on the demonstration data itself (using hindsight relabeling: final task success as sparse reward, or dense reward from state-goal distance) to compute per-timestep advantage estimates; actions with negative advantage (worse than the trajectory's average) are flagged as noisy; (2) Curriculum-Weighted Fine-Tuning — use the advantage scores as per-sample weights during VLA fine-tuning, with a curriculum that starts permissive (all data) and progressively sharpens to high-advantage subsets; (3) Consistency Regularization — for state-action pairs with high variance across similar states, add a consistency loss that encourages the VLA to commit to the high-scoring mode. No real robot required — the scoring is derived entirely from the existing dataset's structure.
EVAL PROTOCOL — IMPORTANT:
TRAIN on standard LIBERO suites (Object/Spatial/Goal/Long/90), with synthetic noise injection to simulate real-world demonstration noise (action jitter, redundant sub-trajectories, random pauses).
EVALUATE on existing LIBERO-PLUS / LIBERO-PRO style perturbation benchmarks (and similar community-released robustness benchmark series). DO NOT spend time constructing your own robustness benchmark — use existing perturbation suites and route the budget into the method.
Report robustness gap (Δ between nominal LIBERO success and perturbed-suite success) AND nominal preservation (must not regress on base LIBERO).
Additionally report: performance under varying noise injection ratios (10%/30%/50% noisy demonstrations), ablation of scoring function choices (MC return, TD advantage, trajectory ranking), and data efficiency curves (how much noisy data can be tolerated).
Experiments can be extended to other benchmarks with noisy demonstration collection (e.g., RLBench with injected perturbations).
SIM-ONLY MITIGATION: Using sim demonstrations with controlled noise injection is methodologically clean and well-accepted at CoRL. The scoring method is agnostic to sim/real — it operates on (state, action) pairs.
HARD CONSTRAINTS:
Compute: ≤200 H100-hours total. Fine-tune from open VLA checkpoints (OpenVLA, SmolVLA, OpenPi, π0) — no pretraining. Value function is lightweight (small MLP head). Show the math.
Time: ≤20 days. Build on OpenVLA, OpenPi and other proper codebases, LeRobot, HF Transformers.
Eval datasets: LIBERO base (training/nominal eval) + LIBERO-PLUS / LIBERO-PRO and similar existing perturbation suites (perturbed eval). No custom benchmark construction.
Look for: temporal advantage estimation from demonstration data without environment interaction, hindsight relabeling strategies for sparse-reward scoring, curriculum learning schedules that progressively filter noisy samples, connections between action distribution entropy and robustness, offline RL value estimation adapted to VLA's representation space. Avoid: requiring environment interaction or online rollouts (must be purely offline), full offline RL replacing BC (too unstable for VLA scale), simple trajectory-level success filtering (too coarse — need timestep-level scoring), just-add-noise training without filtering mechanism.
Tag: direction=robust_vla, contribution_type=method, sub_direction=demonstration_distillation, target_venues=["CoRL 2026"].

## Generation Journey

1. **Start** — 开始生成，seed: 'Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\nDirection：Meta-Brain VLA（无真机）\n*让LLM在不同场景下进行角色切换，辅助VLA应对多个场景，本质上还是利用潜在能力对视觉部分表征进行优化。\nMotivation：希望利用大模型已具备知识辅助VLA决策，达到类似Agentic元大脑框架的效果\nidea创新性：\n（1）使用现有性能比较强的大模型辅助VLA决策，回传时选择更新Skill库或者尝试优化Prompt\n（2）根据不同的场景信息选择角色，能够有效解决泛化\n（3）尝试用一种统一的表征来表达不同的信息\n\n元大脑角色切换：\nLLM作为元大脑，根据当前任务场景动态路由切换以下三种模式：\n（1）感知增强模式 ：环境光照暗、物体遮挡严重或遇到罕见物体，LLM专注输出空间关系描述或视觉线索引导，辅助 VLA 重新对齐特征\n（2）逻辑拆解模式：用户指令模糊，LLM 此时退回 Long-term Planning 角色，将任务分解为一系列 Skill 序列。\n（3）异常干预模式：VLA 预测的 Action 概率分布不确定性高，或者物理碰撞检测报错，LLM 介入进行反思，对比当前状态与目标状态，指导VLA改出。\n\n动态 Skill 库的进化逻辑：\n         LLM 具备写Skill能力，无法解决时有自我更新能力，并将其持久化到库中。\n\n技术难点：\n（1）无论 LLM 扮演什么角色，它最终产出一组同类型但不同功能的优化形式\n1）混合语义 Token (Hybrid Semantic Tokens)\n输出固定维度的嵌入向量，根据不同角色重塑原始视觉token\n2）功能前缀 (Function Prefix)\n在 LLM 输出的表征最前面，加入 Role Embedding，标识当前LLM的指导意见，能够使得VLA接收后，注意力机制或某些层面上发生相应变化。\n3）注意力热力图 (Attention Masking)\n让 LLM 生成注意力引导，始终返回给VLA的是一个权重矩阵\n压缩功能=将无效区域的权重降为 0。\n3D 引入功能 = 给具备空间深度的特征点赋予更高的初始权重。\n技能调用功能 = 强化与该技能相关的物体特征。\n\n（2）哪些部分要训练，如何训练？\n1）如何让LLM切换角色，可以划分关键帧前后两阶段训练\n2）Adapter的训练范式，需要元学习，构造功能性数据集学习不同任务需要的输出。\n3）信息穿透性，训练出的表征需要能对VLA有明显影响'
2. **Problem Discovery** (675s) — 发现 5 个研究方向
   - Role-Conditioned Meta-Brain for Adaptive VLA Enhancement
   - Unified Functional Token Interface for LLM-to-VLA Communication
   - Uncertainty-Triggered LLM Intervention with Representation-Level Correction
   - Scene-Adaptive Skill Routing via Meta-Brain Role Switching
   - LLM-Guided Attention Reweighting for VLA Robustness Under Perturbation
3. **Method Synthesis** (788s) — 完成: "Role-Conditioned Meta-Brain for Adaptive VLA Enhancement" [top-tier] → CoRL 2026 (abstract: May 26, paper: May 29, 2026) — top-tier robotics-learning venue, most natural fit for VLA representation-level intervention, AAAI 2027 (abstract: Jul 25, paper: Aug 1, 2026) — broad top-tier AI venue accepting embodied AI and robotics, ICLR 2027 (abstract: Sep 19, paper: Sep 24, 2026) — top-tier ML venue, strong fit for architectural innovation in VLA representation learning
3. **Method Synthesis** (515s) — 完成: "Unified Functional Token Interface for LLM-to-VLA Communication" [top-tier] → CoRL 2026 (abstract May 26, paper May 29 — top-tier robotics venue, ideal fit for VLA interface design contribution), ICLR 2027 (expected deadline ~Sep-Oct 2026 — highest-tier ML venue for architectural contributions), AAAI 2027 (expected deadline ~Jul-Aug 2026 — strong AI venue, confirmed Feb 16-23 2027 in Montréal)
3. **Method Synthesis** (631s) — 完成: "Uncertainty-Triggered LLM Intervention with Representation-Level Correction" [top-tier] → CoRL 2026 (abstract: May 26, paper: May 29 — confirmed open, premier robot learning venue), ICLR 2027 (expected deadline: ~Sep-Oct 2026 — highest-tier ML venue, strong fit for representation-learning contribution), AAAI 2027 (expected deadline: ~Jul-Aug 2026 — top AI venue), ICRA 2027 (expected deadline: ~Sep 2026 — top robotics venue)
3. **Method Synthesis** (619s) — 完成: "Scene-Adaptive Skill Routing via Meta-Brain Role Switching" [solid] → CoRL 2026 (paper deadline May 28-29, 2026 — top-tier robot learning venue, ideal topical fit for skill evolution in robot manipulation), ICLR 2027 (expected deadline ~October 2026 — top-tier ML venue, meta-learning contribution fits core audience), AAAI 2027 (expected deadline ~August 2026 — top-tier AI venue, fallback if CoRL reviews suggest broader framing needed)
3. **Method Synthesis** (676s) — 完成: "LLM-Guided Attention Reweighting for VLA Robustness Under Perturbation" [solid] → CoRL 2026 (abstract: May 25, paper: May 28 — top venue for robot learning, directly relevant to VLA robustness), ICLR 2027 (projected abstract: Sep 19, paper: Sep 24 — highest-tier ML venue, contribution level supports it), AAAI 2027 (projected abstract: Jul 26, paper: Aug 2 — top-tier AI venue, broad audience for LLM+robotics), ICRA 2027 (projected deadline: Sep 2026 — flagship robotics venue, strong fit for manipulation robustness evaluation)

## Core Problem

Offline VLA fine-tuning on heterogeneous demonstration datasets is bottlenecked by the absence of reliable, annotation-free quality signals. Existing approaches each impose substantial external dependencies: GVL (ICLR 2025 Spotlight) achieves zero-shot value estimation across 300+ tasks but requires per-frame inference from Gemini-scale VLMs; TOPReward (Feb 2026) achieves 0.947 VOC zero-shot but requires a separate 4-8B VLM at scoring time; SCIZOR (ICRA 2026) uses external DINO-V2 features not adapted to the action domain and applies hard binary filtering that discards gradient signal; RINSE (ICML 2025) provides architecture-agnostic trajectory smoothness scoring via SAL/TED metrics without any learned features; influence-function methods (CUPID, CoRL 2025; QoQ, arXiv 2603.09056) require evaluation rollouts or curated validation datasets; PROGRESSOR (ICCV 2025) requires external pretraining on EPIC-KITCHENS video; and ProgressVLA (Microsoft, March 2026) trains a separate progress estimator on large-scale video-text datasets. Online methods (SRPO, VLAC) require environment interaction entirely. Notably, a survey of ICLR 2026 VLA submissions reveals that data curation remains a critically underrepresented problem despite being widely acknowledged as a bottleneck. A fundamental question remains: do VLA models, through large-scale pretraining on action-prediction tasks, already encode sufficient task-progress information in their own internal representations to score demonstration quality — enabling a fully self-referential pipeline with zero external models, zero additional inference cost, and zero annotation requirements?

## Opportunity / Why Now

Recent mechanistic interpretability work provides moderate but encouraging evidence that VLA representations encode task-relevant information. The Emergent World Representations study (arXiv 2509.24559) demonstrates that linear probes on OpenVLA hidden states achieve R²=0.667 for state transition vector prediction (K=30 setting), confirming meaningful task-dynamic information is accessible in VLA feature space — though this falls well short of perfect prediction and concerns continuous state transitions rather than discrete progress. Complementarily, Probing OpenVLA for Symbolic States (arXiv 2502.04558) shows >90% accuracy for discrete symbolic state classification (binary properties like is_grasped, is_on_table) on LIBERO-Spatial, demonstrating that VLA representations linearly encode task-relevant binary predicates. Most directly, the mechanistic study 'Not All Features Are Created Equal' (arXiv 2603.19233) reports that π0.5 expert pathway features achieve R²=0.45 for continuous state prediction and AUC=0.93 for success prediction, with expert pathways consistently outperforming VLM pathways for motor-relevant information — directly demonstrating discriminative capacity in VLA features for quality-related judgments. SAE analyses (arXiv 2603.19183) reveal that 97-99% of individual sparse dictionary features are memorized on LIBERO-tuned models, but DROID-pretrained models show only 89.19% memorization, and critically, aggregate hidden-state vectors remain discriminative for state-level properties despite individual-feature memorization. The OpenGVL benchmark (arXiv 2509.17321) further reveals that open-source VLMs achieve only ~70% of closed-source VLM performance on temporal progress estimation, suggesting that VLA-internal features — which are natively adapted to the action domain — may offer competitive or superior signal without requiring external VLM inference. This creates a testable opportunity: if VLA features can support temporal distance estimation (frame-pair relative progress) beyond what positional embeddings alone provide, and if this signal outperforms both generic visual features (DINO-V2) and simple trajectory geometry (RINSE), then the same model being fine-tuned can score its own training data at zero marginal cost.

## Landscape (SOTA & Limitations)

The demonstration curation space for VLA fine-tuning has rapidly expanded across seven complementary approaches: (1) **Zero-shot VLM value estimation**: GVL (ICLR 2025 Spotlight, arXiv 2411.04549) poses value estimation as temporal ordering of shuffled video frames using Gemini-1.5-Pro, achieving zero-shot value prediction across 300+ tasks with Value-Order Correlation (VOC) as the metric. Applied to dataset filtering and advantage-weighted regression (AWR) on real ALOHA tasks. Limitation: requires per-frame API calls to a Gemini-scale VLM, with no reported compute cost analysis. OpenGVL (arXiv 2509.17321) benchmarks open-source VLMs on this task, finding they achieve ~70% of closed-source performance. TOPReward (Feb 2026, arXiv 2602.19313) extracts zero-shot progress from VLM token probabilities (0.947 VOC on Qwen3-VL), applied to advantage-weighted fine-tuning of pi0. Both require a separate large VLM at scoring time. (2) **Self-supervised visual curation**: SCIZOR (ICRA 2026, arXiv 2505.22626) trains a temporal distance classifier on frozen DINO-V2 features to estimate progress, then hard-filters low-quality timesteps and removes redundant data via joint state-action deduplication. Achieves 5.4% improvement on RoboMimic, 8.1% on OXE-Magic-Soup, and 32.9% on Sirius-Fleet real-robot tasks. Limitations: external visual features without action-domain adaptation; hard binary filtering discards gradient signal; tested primarily on Octo, not modern VLAs. VLA-SSD directly extends SCIZOR's temporal distance classification framework to VLA-internal representations, testing whether action-domain adaptation through VLA pretraining provides superior progress signals, and replaces hard filtering with soft reward weighting grounded in iw-SFT theory. (3) **Trajectory geometry heuristics**: RINSE (ICML 2025, arXiv 2604.23000) uses Spectral Arc Length (SAL, frequency-domain smoothness) and Trajectory-Envelope Distance (TED, spatial contact-aware geometry) for architecture-agnostic demo scoring. Achieves 16% higher success with 1/6 data on RoboMimic, 20% improvement with 1/2 data in real-world tasks, and 5.6% mean success improvement on LIBERO-10 via STRAP integration. Requires zero model access or learned features. This is the critical lower bound: if learned features cannot beat pure trajectory geometry, feature-based scoring is unjustified. (4) **External progress estimators**: PROGRESSOR (ICCV 2025, arXiv 2411.17764) learns a task-agnostic reward function pretrained on EPIC-KITCHENS for goal-conditioned RL. ProgressVLA (Microsoft, March 2026, arXiv 2603.27670) pre-trains a dedicated progress estimator on large-scale unsupervised video-text robotic datasets (0.07 prediction residual, zero-shot real-world transfer), integrated into a diffusion VLA with inverse dynamics guidance. Both require external pretraining data/models. (5) **Influence-function curation**: CUPID (CoRL 2025) and QoQ (arXiv 2603.09056) use REINFORCE-style influence estimation for trajectory-level filtering. QoQ achieves 23.2%/30.0% improvements on GR00T N1 VLA. Both require evaluation rollouts or curated validation sets and provide only trajectory-level granularity. (6) **External reward models**: Robometer (RSS 2026, arXiv 2603.02115) trains Qwen3-VL-4B on 1M+ trajectories for dense per-frame progress with strong zero-shot transfer (Kendall tau=0.66 OOD). Requires a separate 4-8B VLM at scoring time. (7) **Online self-improvement**: SRPO (arXiv 2511.15605) uses the model's own successful rollouts for self-referential optimization (48.9→99.2% on LIBERO). PLD (ICLR 2026, arXiv 2511.00091) uses residual RL to probe VLA failure regions, collect recovery data, and distill back via SFT (99% on LIBERO, 50%+ gains on SimplerEnv). VLAC (arXiv 2509.15937) integrates a dense progress critic into an online RL loop. All require environment interaction. (8) **Weighted BC frameworks**: VACO (ICLR 2025) uses a meta-scoring network for bi-level weighted BC on D4RL. iw-SFT (arXiv 2507.12856) proves that SFT on curated data maximizes a lower bound on the RL objective, tightened by importance weighting — providing theoretical justification for quality-weighted BC as a principled approach. **Gap**: No work has investigated whether VLA-internal features — uniquely adapted to the action domain through pretraining and already computed during the forward pass — can serve as a self-referential progress estimator that (a) beats trajectory geometry heuristics (RINSE), justifying learned features, (b) matches or exceeds external VLM scoring (GVL/TOPReward) on task-specific data, and (c) does so at zero marginal cost since features are a byproduct of the fine-tuning forward pass.

## Proposed Approach

VLA-SSD is a three-stage offline pipeline that tests a mechanistic hypothesis — VLA pretrained representations encode task-progress information sufficient for self-referential demonstration scoring — and operationalizes positive findings into a theoretically-grounded curriculum-weighted fine-tuning method. The theoretical foundation comes from iw-SFT (arXiv 2507.12856), which proves that SFT on quality-scored data maximizes a lower bound on the RL objective, tightened by importance weighting; VLA-SSD's quality scores serve as the importance weights, making the pipeline provably principled rather than heuristic.

**Stage 1 — Temporal Distance Probing with Positional Embedding Controls**: Extract frozen hidden-state representations h_l(t) from every transformer layer l of the pretrained VLA (OpenVLA 7B as primary, π0.5 as validation) for each demonstration timestep. Train lightweight probes at each layer using TWO complementary targets designed to be robust against positional embedding shortcuts:

(a) **Temporal distance classification** (primary target): Given a pair of frames (t_i, t_j) from the same trajectory, predict relative progress Δp = |t_j - t_i|/T from feature differences h_l(t_j) - h_l(t_i). This forces the probe to compare semantic content between two frames rather than recovering absolute temporal position from a single frame, directly mitigating the positional embedding shortcut. This explicitly extends SCIZOR's temporal distance classification framework — which uses frozen DINO-V2 features — to the VLA's own internal representations, testing whether action-domain adaptation through VLA pretraining provides superior progress signals.

(b) **Sub-task predicate classification** (secondary target, LIBERO only): LIBERO provides BDDL goal predicates (e.g., is_grasped, is_on_table, is_in_drawer) checkable at every simulator timestep. Train binary classifiers on VLA features to predict sub-task completion milestones. These are discrete semantic properties that cannot be predicted from positional embeddings, providing the strongest evidence for genuine task understanding.

(c) **Positional embedding control experiment** (probe-level only, not full pipeline): Train identical probes on positional embeddings alone (extracted from the same transformer layers but with content features zeroed out / using only the position component). If VLA content features significantly outperform positional-embedding-only probes, this confirms the signal comes from task-semantic representations, not temporal position recovery.

Probe architecture: single linear layer + sigmoid for classification, ~50K params each. 80/20 train/validation split within the demonstration set. Rank layers by validation performance (Spearman ρ for temporal distance, AUC for sub-task predicates); select best layer l* automatically. Based on arXiv 2603.19233, expert pathway features (PG5, PG11 equivalent) are hypothesized most informative, but selection is fully data-driven.

**Critical controlled ablations** (run in parallel):
- **DINO-V2 (ViT-L/14) baseline**: Extract DINO-V2 features from the same observations, train identical probes — isolates the effect of action-domain adaptation.
- **RINSE baseline**: Compute SAL and TED scores on the same trajectories — tests whether learned features beat trajectory geometry heuristics. If RINSE matches or exceeds our probes, the 'VLA features encode progress' narrative is undermined.
- **DINO-V2 Fallback**: If no VLA layer achieves Spearman ρ > 0.3 on temporal distance AND no layer achieves AUC > 0.7 on sub-task predicates, switch to DINO-V2 features for subsequent stages and report this as a negative mechanistic finding.

**Stage 2 — Hierarchical Quality Scoring**: Use the temporal distance probe from l* to compute per-timestep progress estimates by anchoring relative to the first frame: q_t = probe_{l*}(h_{l*}(t) - h_{l*}(0)). Derive trajectory-level quality Q(τ) = α * q_T + β * mono(τ) + γ * mean(q_t), combining terminal progress (endpoint quality), progress monotonicity (fraction of consecutive timesteps with increasing estimated progress), and average progress. Default weights: α=0.5, β=0.3, γ=0.2. Compute timestep-level reward weights w_t = q_t * Q(τ). Apply temperature-controlled normalization for the trajectory component. On LIBERO, additionally compute sub-task milestone coverage as a trajectory quality signal.

**Stage 3 — Curriculum-Weighted LoRA Fine-Tuning**: Fine-tune the VLA with LoRA (rank 16-64) using weighted BC loss with a curriculum temperature schedule that starts permissive and progressively sharpens quality weighting over training. Specifically, define a temperature parameter τ(epoch) that decreases linearly from τ_max to τ_min over training: w_t^(epoch) = softmax(q_t / τ(epoch)), where τ_max = 2.0 (near-uniform early training, allowing the model to learn from all demonstrations) and τ_min = 0.5 (sharp quality weighting in later epochs, focusing gradient signal on high-quality timesteps). The curriculum rationale: early uniform training establishes broad behavioral coverage, while progressive sharpening concentrates fine-tuning on the most informative demonstrations — analogous to curriculum learning in knowledge distillation (Curriculum Temperature, arXiv 2211.16231) and grounded by iw-SFT's theoretical result that tighter importance weighting progressively tightens the RL objective lower bound. The loss at each epoch: L = Σ_t w_t^(epoch) * ||a_t - π_θ(o_t, l)||². Unlike SCIZOR's hard filtering, soft reward weighting preserves gradient signal from all timesteps proportional to quality. Unlike GVL+AWR, no external VLM is needed — features come from the model being fine-tuned. Probes are trained once on pretrained features and frozen; all quality scores are computed before fine-tuning begins, ensuring no circular dependency.

**Evaluation Protocol**:

*Primary benchmarks* (in main paper): (1) RoboMimic Multi-Human (300 naturally mixed-quality demos from 6 operators of varied skill, Can and Square tasks). Validates quality scoring on natural distribution. Verify scores correlate with operator skill levels — the RoboMimic MH dataset organizes 50 demos per operator across 3 skill tiers (worse/okay/better); operator group membership is verifiable via filter keys using `get_dataset_info.py` and the known sequential collection structure. (2) LIBERO-Long with controlled noise injection (action jitter σ ∈ {0.05, 0.1, 0.2}, trajectory truncation at {50%, 75%}). Probes trained exclusively on clean data, then evaluated on mixed clean+noisy demonstrations — tests whether scoring generalizes beyond the noise distribution seen during probe training.

*Robustness benchmarks* (in appendix): LIBERO-Plus (CVPR 2026, arXiv 2510.13626; 10,030 tasks across 7 perturbation dimensions) and LIBERO-PRO (arXiv 2510.03827). Report robustness gap Δ between nominal LIBERO success and perturbed-suite success.

*Scale validation* (in appendix): DROID subsets with natural variable-quality teleoperation, where SAE analysis shows more general features (10.81% vs 2.63% on LIBERO).

*π0.5 validation* (in appendix): Replicate core probing experiments (Stage 1) and one primary benchmark fine-tuning on π0.5 to validate generalization across VLA architectures.

**Baselines** (6 core + 2 appendix):

Core (main paper):
1. Vanilla BC (unweighted)
2. RINSE (SAL+TED trajectory geometry, no features) — critical lower bound
3. SCIZOR-style (DINO-V2 + temporal distance + hard filtering)
4. DINO-V2 + our curriculum-weighted pipeline (ablation isolating feature source)
5. GVL-style (open-source VLM scoring via OpenGVL protocol + AWR)
6. VLA-SSD without curriculum (static τ=1.0, ablating the curriculum contribution)

Appendix:
7. Oracle scoring (ground-truth operator labels/noise levels)
8. TOPReward (external VLM + AWR)

**Key metrics**: success rate on nominal and perturbed benchmarks, robustness gap Δ, probe Spearman ρ for temporal distance by layer (mechanistic), sub-task AUC by layer, quality score Kendall tau with ground-truth labels, VLA-feature vs. DINO-V2 vs. positional-embedding probe performance comparison (probe-level), VLA-feature vs. RINSE scoring comparison, curriculum ablation (with/without temperature schedule), compute overhead comparison (FLOPs, wall-clock, API cost).

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$200-400 (~2500-5000 turns)', 'estimated_gpu_cost': '$490-685', 'gpu_hours': '~195h H100 (feature extraction from OpenVLA on 2 primary benchmarks ~25h, π0.5 validation extraction ~12h, probe training sweep across layers with temporal distance + sub-task + positional embedding control ~15h, DINO-V2 baseline ~10h, RINSE computation ~2h, LoRA fine-tuning: 1 primary VLA × 2 primary benchmarks × 6 core conditions × ~3h each ~72h, curriculum schedule sweep ~12h, π0.5 validation fine-tuning ~20h, appendix benchmarks (LIBERO-Plus/PRO, DROID) ~20h, evaluation rollouts ~25h)', 'gpu_utilization': '~85-90% — agent runs 24/7, parallelizes feature extraction across benchmarks and probe training across layers', 'risk_note': 'Agent may need human intervention at two critical decision points (positional embedding control result, RINSE comparison). The fallback mechanisms handle clear-negative cases automatically, but marginal results require judgment about paper framing.', 'speed_bottleneck': 'Feature extraction from OpenVLA 7B dominates; with 4 H100s, extraction parallelizes across benchmarks. π0.5 validation adds ~12h due to larger model size.', 'team': '0 (setup + final review only)', 'timeline': '5-8 days with 4 H100 GPUs'}
- **human_in_loop**: {'claude_api_cost': '$100-200 (~1250-2500 turns at ~$0.08/turn)', 'estimated_gpu_cost': '$400-560', 'gpu_hours': '~160h H100', 'gpu_utilization': '~65-75% — agent queues feature extraction, probe sweeps, and LoRA runs; researcher reviews layer-wise probing results and quality score calibration at check-ins', 'risk_note': "Key decision points: (1) If no VLA layer significantly outperforms positional-embedding-only probes on temporal distance, the 'semantic progress encoding' claim is falsified — paper pivots to negative finding about VLA representation limits. (2) If RINSE matches or exceeds VLA-probe scoring, the learned-feature approach is unjustified — paper pivots to 'trajectory geometry suffices' finding. Human judgment critical at these decision points.", 'team': '1 researcher, ~30min/day reviewing probing accuracy curves, RINSE comparison, and curriculum schedule', 'timeline': '3.5-4.5 weeks'}
- **manual**: {'estimated_gpu_cost': '$450-630 (H100 spot at ~$2.50-3.50/hr)', 'gpu_hours': '~180h H100 (feature extraction from OpenVLA on 2 primary benchmarks ~20h, π0.5 validation extraction ~10h, linear probe training across all layers with temporal distance + sub-task targets ~10h, DINO-V2 and positional embedding baselines ~8h, RINSE computation ~2h, LoRA fine-tuning: 1 primary VLA × 2 primary benchmarks × 6 core conditions ~60h, π0.5 validation fine-tuning ~20h, appendix benchmarks ~25h, evaluation rollouts ~25h)', 'gpu_utilization': '~40-50% — researcher iterates on layer selection analysis, examines probe performance curves and quality score distributions between GPU runs', 'team': '1-2 researchers', 'timeline': '2-3 months'}

## Key References

- GVL: Vision Language Models are In-Context Value Learners (ICLR 2025 Spotlight, arXiv 2411.04549)
- RINSE: Learning from the Best — Smoothness-Driven Metrics for Data Quality in Imitation Learning (ICML 2025, arXiv 2604.23000)
- PROGRESSOR: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement (ICCV 2025, arXiv 2411.17764)
- ProgressVLA: Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation (Microsoft, March 2026, arXiv 2603.27670)
- OpenGVL: Benchmarking Visual Temporal Progress for Data Curation (arXiv 2509.17321)
- SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026, arXiv 2505.22626)
- CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025, arXiv 2506.19121)
- QoQ: Quality over Quantity — Demonstration Curation via Influence Functions (arXiv 2603.09056)
- Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons (RSS 2026, arXiv 2603.02115)
- TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics (Feb 2026, arXiv 2602.19313)
- SRPO: Self-Referential Policy Optimization for VLAs (arXiv 2511.15605)
- PLD: Self-Improving Vision-Language-Action Models with Data Generation via Residual RL (ICLR 2026, arXiv 2511.00091)
- VLAC: A Vision-Language-Action-Critic Model for Robotic Real-World RL (arXiv 2509.15937)
- Emergent World Representations in OpenVLA (arXiv 2509.24559) — R²=0.667 for state transition prediction
- Probing OpenVLA for Symbolic States (arXiv 2502.04558) — >90% accuracy for discrete symbolic state classification
- Not All Features Are Created Equal: A Mechanistic Study of VLA Models (arXiv 2603.19233) — R²=0.45 state prediction, AUC=0.93 success prediction from π0.5 expert pathway
- Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models (arXiv 2603.19183)
- iw-SFT: Supervised Fine Tuning on Curated Data is Reinforcement Learning (arXiv 2507.12856)
- VACO: Value-Aligned Behavior Cloning via Bi-Level Optimization (ICLR 2025)
- Curriculum Temperature for Knowledge Distillation (arXiv 2211.16231)
- LIBERO-Plus: In-depth Robustness Analysis of VLA Models (CVPR 2026, arXiv 2510.13626)
- LIBERO-PRO: Towards Robust and Fair Evaluation of VLA Models Beyond Memorization (arXiv 2510.03827)
- RoboMimic: What Matters in Learning from Offline Human Demonstrations (CoRL 2021)
- DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset (RSS 2024)
- OpenVLA: An Open-Source Vision-Language-Action Model (2024)
- VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models (ICLR 2026)

## Reviewer Evaluation

**Scores**:
  - clarity: **4**/5
  - feasibility: **3**/5
  - impact: **3**/5
  - novelty: **3**/5

**Recommendation**: borderline

**Summary**:

研究问题新颖但负结果风险高；方法论是 SCIZOR + iw-SFT 的自然延伸，突破性有限；CoRL 时间线极紧（12 天）


## MVP Validation Results

- **Date**: 2026-05-15
- **Hypothesis Supported**: No

### Key Metrics

SigLIP+Projector RSA=0.615 | Full VLA RSA≈0.488 (all 4 conditions) | DINO RSA=0.388 | Training effect Δ<0.01 | Instruction effect Δ<0.005 | 2×2 matrix Bootstrap CI [-0.058, 0.072] includes 0 | 6 probing methods × 2 benchmarks consistent

### Summary

原假设（VLA training 注入独特表征知识）被系统性否定，但发现了更强的 publishable finding：VLA 中 action-relevant 表征完全由 frozen SigLIP vision encoder 决定，LLM processing 反而降低 action-relevant 结构。

7 轮系统性 probing（temporal distance / subtask / action prediction / action-delta / goal classification / RSA / instruction ablation）× 2 benchmarks（LIBERO-10 + LIBERO-Goal）一致确认：trained ≈ untrained >> DINO，instruction 无影响。SigLIP+Projector RSA = 0.615 远高于 full VLA 0.488 和 DINO 0.388，直接证明 vision encoder 是 action-relevant 表征的来源，LLM 是 degrader。

Framing: "Vision Encoder Dominance" — 三个 core claims: (1) 表征源自 frozen SigLIP; (2) LLM degrades action alignment; (3) training 和 instruction 均不改变表征结构。

### Recommendation

GO — 进入 research/writing 阶段，目标 CoRL 2026（abstract May 26, paper May 29）。Evidence chain 完整，三个 claims 各有直接数据支持，LLM degradation 是 novel contribution。需要：(1) post-MVP kickoff 写 paper_framing.md + experiment_plan.yaml；(2) 启动 Paper Agent；(3) 考虑补充 SigLIP 不同变体对比实验加强 claim 1。
