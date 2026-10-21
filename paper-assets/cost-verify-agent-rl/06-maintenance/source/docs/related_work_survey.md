# B-IAVR Related Work Survey

> Survey date: 2026-05-15. Covers 2024-2026 publications across four directions.

---

## Direction 1: Self-Verification / Self-Correction in LLM Agents

### [When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs] (Huang et al., 2024)
- **Venue**: arXiv 2406.01297 (highly cited survey)
- **Core contribution**: First comprehensive critical survey of LLM self-correction, establishing taxonomy of intrinsic/external/fine-tuned correction.
- **Method**: Categorizes self-correction into three paradigms: (1) intrinsic correction via prompted self-feedback, (2) external correction via tool/verifier feedback, (3) fine-tuned correction via training. Systematically evaluates when each works.
- **Results**: No prior work demonstrates successful intrinsic self-correction from prompted LLMs alone, except for tasks exceptionally suited to self-correction. External feedback and large-scale fine-tuning enable reliable correction.
- **Relation to B-IAVR**: Foundational framing. B-IAVR's verification is closer to "external correction" (environment re-observation), not pure intrinsic self-correction. This survey validates that verification with grounded feedback is the viable path.
- **Key insight**: Pure self-correction is unreliable; grounded verification signals (like B-IAVR's action-change detection) are necessary.

### [CorrectBench: Can LLMs Correct Themselves?] (He et al., 2025)
- **Venue**: NeurIPS 2025 Datasets & Benchmarks
- **Core contribution**: Systematic benchmark for evaluating self-correction strategies across commonsense reasoning, math, and code.
- **Method**: Curates 3,825 QA pairs across 7 subdatasets. Evaluates intrinsic, external, and fine-tuned correction methods. Tests mixing strategies.
- **Results**: Self-correction improves accuracy for complex reasoning; mixing strategies helps but reduces efficiency. Reasoning LLMs (DeepSeek-R1) show limited gain from additional correction and high cost. Simple CoT is competitive.
- **Relation to B-IAVR**: Complementary benchmark. Validates that self-correction has diminishing returns when applied uniformly — supports B-IAVR's selective verification design.
- **Key insight**: Cost-accuracy tradeoff of self-correction is real; selective application (as in B-IAVR) is more efficient than blanket correction.

### [Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning] (2026)
- **Venue**: arXiv 2602.03485
- **Core contribution**: Identifies that LLM reasoning models massively overuse self-verification — most rechecks are confirmatory (>90%), not corrective (~2%).
- **Method**: Analyzes verification behavior across models/benchmarks. Proposes experience-driven test-time framework: detects recheck activation, consults offline experience pool of past verification outcomes, estimates whether recheck is unnecessary.
- **Results**: Vast majority of self-verification steps are wasted computation. Framework reduces unnecessary verification while preserving accuracy.
- **Relation to B-IAVR**: Directly supports B-IAVR's core thesis — verification should be selective, not universal. Their "experience pool" approach is complementary to B-IAVR's action-change signal.
- **Key insight**: The verification-overuse problem is empirically validated here. B-IAVR's signal-based triggering addresses the same inefficiency from a different angle.

### [Incentivizing LLMs to Self-Verify Their Answers] (Zhang et al., 2025)
- **Venue**: arXiv 2506.01369
- **Core contribution**: Unifies answer generation and verification in a single RL training process, eliminating external verifiers.
- **Method**: Trains LLMs with RL to jointly generate answers and verify them. The model learns to assess correctness of its own solutions during training. At inference, scales performance by self-verifying without external reward models.
- **Results**: Overcomes distribution mismatch between generator and external reward model. Achieves test-time scaling via self-verification.
- **Relation to B-IAVR**: Complementary approach. They train verification into the generation process; B-IAVR trains when to trigger a separate verification step. Could potentially be combined.
- **Key insight**: RL can train internal verification capability, paralleling B-IAVR's RL-trained verification policy.

### [MAR: Multi-Agent Reflexion] (2025)
- **Venue**: arXiv 2512.20845
- **Core contribution**: Extends Reflexion to multi-agent setting with diverse critic personas for more robust self-correction.
- **Method**: Uses Society-of-Mind framework: intentionally diverse critic personas provide structured disagreement. Reduces shared blind spots of single-agent reflection.
- **Results**: More stable and transferable improvements across tasks compared to single-agent Reflexion.
- **Relation to B-IAVR**: Complementary. MAR improves correction quality when verification is triggered; B-IAVR decides when to trigger it.
- **Key insight**: Multi-perspective verification is more effective than single-pass checking.

### [SSR: Socratic Self-Refine] (2025)
- **Venue**: arXiv 2511.10621
- **Core contribution**: Guides self-refinement through Socratic questioning rather than direct correction prompts.
- **Method**: Decomposes self-refinement into structured questioning steps. The model evaluates its own output by answering diagnostic questions about potential errors, then revises based on answers.
- **Results**: Improves over standard Self-Refine on reasoning tasks by making the critique step more structured.
- **Relation to B-IAVR**: Complementary. Improves the quality of the correction step itself; B-IAVR focuses on when to invoke correction.
- **Key insight**: Structured verification prompts yield better corrections than "is this correct?" style prompts.

---

## Direction 2: Agent RL Training

### [GiGPO: Group-in-Group Policy Optimization for LLM Agent Training] (Feng et al., 2025)
- **Venue**: NeurIPS 2025
- **Core contribution**: Fine-grained credit assignment for multi-step agent tasks while staying critic-free and memory-efficient.
- **Method**: Extends GRPO with nested group structure: outer group samples trajectories per task, inner group compares actions within each step. This decomposes trajectory-level reward into step-level advantages without a learned critic.
- **Results**: >12% improvement on ALFWorld, >9% on WebShop over GRPO. Preserves GRPO's low-memory properties.
- **Relation to B-IAVR**: Building block. B-IAVR uses GRPO/GiGPO for policy optimization. GiGPO's step-level credit assignment is especially relevant for training the verification trigger policy.
- **Key insight**: Step-level credit in agent RL is critical; GiGPO's approach directly benefits B-IAVR's reward attribution for verification decisions.

### [Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)] (2026)
- **Venue**: arXiv 2604.03098
- **Core contribution**: Self-generated internal reward (Self-Guide) that co-evolves with the agent policy for both inference-time guidance and training-time supervision.
- **Method**: Agent generates a short self-guidance signal to steer next action at inference; same signal is converted to step-level internal reward for GRPO training. Creates a co-evolving loop: better policy → better guidance → better reward.
- **Results**: 8% improvement over environment-reward-only baselines across ALFWorld, ScienceWorld, WebShop. Tested on Qwen3-1.7B/4B and Qwen2.5-7B.
- **Relation to B-IAVR**: Direct predecessor. B-IAVR builds on Self-Guide — the self-guidance signal is the foundation for the action-change detection that triggers verification.
- **Key insight**: Internal reward enables dense supervision for sparse-reward agent tasks; B-IAVR extends this by using the signal to decide when verification is needed.

### [SPEAR: Self-Imitation with Progressive Exploration for Agentic RL] (Tencent, 2025)
- **Venue**: ICLR 2026
- **Core contribution**: Curriculum-based self-imitation learning for long-horizon, sparse-reward agent tasks.
- **Method**: Two-phase curriculum: (1) early stage uses auxiliary tool-use rewards for broad exploration, (2) later stage strengthens self-imitation from successful trajectory replay. Uses advantage recalibration and regularization.
- **Results**: Increases success rates of GRPO/GiGPO/Dr.BoT by up to 16.1%/5.1%/8.6% on ALFWorld, 20.7%/11.8%/13.9% on WebShop.
- **Relation to B-IAVR**: Complementary training recipe. SPEAR's curriculum could be applied to B-IAVR's verification policy training to improve exploration of when-to-verify decisions.
- **Key insight**: Self-imitation from successful trajectories is powerful for sparse-reward agent RL; applicable to B-IAVR's training pipeline.

### [WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL] (Pei et al., 2025)
- **Venue**: EMNLP 2025
- **Core contribution**: Extends GRPO to multi-turn agent settings (M-GRPO) with dynamic context compression.
- **Method**: Asynchronous trajectory generation guided by binary success rewards. M-GRPO handles multi-turn credit assignment. Dynamic context compression reduces memory. Behavior cloning warm-up before RL.
- **Results**: Qwen-2.5-3B: 6.1% → 33.9% on WebArena-Lite. LLaMA-3.1-8B: 8.5% → 44.8%. Outperforms OpenAI o3.
- **Relation to B-IAVR**: Parallel work on agent RL. M-GRPO's multi-turn extension is directly relevant to B-IAVR's sequential decision process.
- **Key insight**: Multi-turn GRPO with warm-up is effective for agent training; B-IAVR could adopt similar context compression techniques.

### [DAPO: Decoupled Clip and Dynamic Sampling Policy Optimization] (ByteDance/Tsinghua, 2025)
- **Venue**: arXiv 2503.14476 (open-source system)
- **Core contribution**: Open-source large-scale RL system solving key instabilities in reasoning model training.
- **Method**: Four techniques: Clip-Higher (prevents entropy collapse), Dynamic Sampling (filters batches for consistent gradients), Token-level Policy Gradient Loss (for long CoT), Overlong Reward Shaping (reduces length-limit reward noise).
- **Results**: 50 points on AIME 2024 with Qwen2.5-32B, outperforming DeepSeek-R1-Zero with 50% training steps.
- **Relation to B-IAVR**: Infrastructure. DAPO's stabilization techniques (especially Clip-Higher and Dynamic Sampling) are applicable to B-IAVR's RL training to prevent collapse.
- **Key insight**: RL training stability techniques from reasoning domain transfer to agent RL.

### [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL] (2024)
- **Venue**: NeurIPS 2024
- **Core contribution**: Online RL for device control agents interacting with real GUI environments.
- **Method**: Two-stage: offline RL from demonstrations, then offline-to-online RL with autonomous performance evaluation. Agent learns from real interactions with graphical interfaces.
- **Results**: 49.5% absolute improvement (17.7% → 67.2%) over SFT on device control tasks.
- **Relation to B-IAVR**: Parallel approach. DigiRL demonstrates online RL viability for interactive agents; B-IAVR applies similar principles to text-based environments with selective verification.
- **Key insight**: Online RL with real environment interaction dramatically outperforms imitation learning for agents.

### [SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training] (Li et al., 2025)
- **Venue**: arXiv 2511.20718
- **Core contribution**: Addresses instability in off-policy PPO/GRPO for multi-turn agent tasks.
- **Method**: Turn-level importance sampling (aligns optimization granularity with turn-structured interactions) + clipping-triggered normalization (suppresses unreliable off-policy updates).
- **Results**: Prevents training collapse observed in standard PPO/GRPO. Maintains lower clipping ratios and stable optimization.
- **Relation to B-IAVR**: Infrastructure. B-IAVR's RL training on multi-turn ALFWorld episodes faces the same off-policy stability challenges. SORL's techniques are directly applicable.
- **Key insight**: Turn-level (not token-level) optimization is key for stable multi-turn agent RL.

### [The Landscape of Agentic RL for LLMs: A Survey] (2025)
- **Venue**: TMLR 2026 (arXiv 2509.02547)
- **Core contribution**: Comprehensive survey formalizing the shift from single-step LLM-RL to temporally extended agentic RL.
- **Method**: Distinguishes degenerate single-step MDPs (standard LLM-RL) from POMDPs (agentic RL). Proposes taxonomy around capabilities (planning, tool use, memory, reasoning, self-improvement) and task domains.
- **Results**: N/A (survey). Identifies RL as the critical mechanism for transforming static capabilities into adaptive agentic behavior.
- **Relation to B-IAVR**: Contextualizes B-IAVR within the broader agentic RL landscape. B-IAVR's selective verification is a form of adaptive self-improvement trained via RL.
- **Key insight**: The survey frames B-IAVR's contribution as part of the agentic RL paradigm — training agents to make meta-decisions (like when to verify) via RL.

---

## Direction 3: Selective Verification / Adaptive Computation in Agents

### [Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning] (Wan et al., 2025)
- **Venue**: ACL 2025 Findings
- **Core contribution**: Lightweight mechanism to detect reasoning instability and selectively trigger deep verification only when needed.
- **Method**: Derailer assesses reasoning stability via a lightweight check. Only when instability is detected does the expensive Rerailer verification process engage. Binary gate: cheap check → selective deep verification.
- **Results**: 8-11% accuracy improvements across reasoning tasks. 2-3x efficiency over uniform verification methods. Strong on math and symbolic reasoning.
- **Relation to B-IAVR**: Most directly related competitor. Both do selective verification with a binary trigger. Key difference: Derailer-Rerailer operates on reasoning chains (single-turn); B-IAVR operates on agent action trajectories (multi-turn). Derailer uses reasoning instability signal; B-IAVR uses action-change signal.
- **Key insight**: Binary selective verification is validated as effective. B-IAVR extends this paradigm from reasoning to interactive agent settings.

### [Sherlock: Reliable and Efficient Agentic Workflow Execution] (Microsoft, 2025)
- **Venue**: arXiv 2511.00330
- **Core contribution**: Framework for cost-efficient selective verification in agentic workflows via counterfactual analysis + speculative execution.
- **Method**: Counterfactual analysis identifies error-prone nodes in workflows. Cost-optimal verifiers attached only where necessary. Runtime: speculative execution of downstream tasks while verification runs in background; rollback on failure.
- **Results**: 18.3% accuracy gain over non-verifying baseline. 26% cost reduction over Monte Carlo verification. 48.7% latency reduction via speculative execution.
- **Relation to B-IAVR**: Complementary but different scope. Sherlock selects verification points via offline counterfactual analysis of workflow DAGs; B-IAVR learns verification points via online RL in interactive environments. Sherlock is workflow-level; B-IAVR is step-level.
- **Key insight**: Selective verification is also studied in structured workflow settings. B-IAVR's contribution is applying this idea to interactive, sequential agent decisions via learned policy.

### [When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning] (Singhi et al., 2025)
- **Venue**: arXiv 2504.01005
- **Core contribution**: Derives inference scaling laws for the tradeoff between generating more solutions vs. verifying existing ones under fixed compute budget.
- **Method**: Compares Self-Consistency (majority voting over solutions) vs. Generative Reward Models (GenRM: generate verification chains to score solutions). Analyzes compute-optimal allocation.
- **Results**: Compute-optimal inference favors scaling solution generation more aggressively than scaling verification. Over-verifying is wasteful under budget constraints.
- **Relation to B-IAVR**: Strong conceptual alignment. Both address "when to verify" as a resource allocation problem. Their finding that over-verification is suboptimal directly supports B-IAVR's selective approach.
- **Key insight**: The optimal compute allocation between solving and verifying is non-trivial — B-IAVR learns this allocation via RL rather than deriving it analytically.

### [ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents] (Yang et al., 2026)
- **Venue**: arXiv 2603.07915
- **Core contribution**: Per-step dynamic reasoning effort selection for multi-step agent tasks via lightweight router.
- **Method**: Trains a router to predict minimum sufficient reasoning effort (low/medium/high) per step. Pipeline: trajectory collection → effort annotation via sampling → rationale generation → SFT on router. Router receives same context as agent.
- **Results**: Reduces reasoning token usage by up to 52.7% with minimal accuracy degradation on agent tasks.
- **Relation to B-IAVR**: Closest competitor in the agent domain. Both train a learned policy for per-step compute allocation. Key difference: ARES selects reasoning effort level (continuous); B-IAVR selects binary verify/not-verify. ARES uses SFT-trained router; B-IAVR uses RL-trained policy.
- **Key insight**: Per-step adaptive computation for agents is a validated direction. B-IAVR's RL training and binary signal provide a simpler, more interpretable mechanism than ARES's multi-level effort.

### [AutoThink: Learning When to Think via Multi-Stage RL] (Tu et al., 2025)
- **Venue**: NeurIPS 2025
- **Core contribution**: RL framework teaching reasoning models to invoke explicit reasoning only when necessary.
- **Method**: Multi-stage RL with stage-wise reward shaping. Exploits discovery that R1-style models have latent controllability of thinking mode. Progressively optimizes reasoning policy.
- **Results**: +6.4% relative accuracy, -52% token usage on DeepSeek-R1-Distill-Qwen-1.5B across 5 math benchmarks.
- **Relation to B-IAVR**: Analogous idea in reasoning domain. AutoThink: "when to think deeply"; B-IAVR: "when to verify actions." Both use RL to learn the adaptive trigger. AutoThink operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.
- **Key insight**: RL-trained adaptive computation is proven effective for reasoning; B-IAVR extends this principle to agent verification.

### [Efficient Agents: Building Effective Agents While Reducing Cost] (Wang et al., 2025)
- **Venue**: arXiv 2508.02694
- **Core contribution**: First systematic study of efficiency-effectiveness tradeoff in modern agent systems.
- **Method**: Empirical analysis on GAIA benchmark evaluating LLM backbone selection, framework design, and test-time scaling. Uses cost-of-pass metric for efficiency-performance tradeoff.
- **Results**: Retains 96.7% performance of OWL framework while reducing cost from $0.398 to $0.228 (28.4% improvement in cost-of-pass).
- **Relation to B-IAVR**: Complementary. Provides framework-level efficiency; B-IAVR provides step-level verification efficiency. Both address agent cost reduction.
- **Key insight**: Agent cost is a first-class research concern. B-IAVR addresses it at the algorithmic (verification policy) level rather than the systems level.

### [Trust but Verify! A Survey on Verification Design for Test-time Scaling] (Venktesh et al., 2025)
- **Venue**: arXiv 2508.16665
- **Core contribution**: Survey of verification approaches for test-time compute scaling in LLMs.
- **Method**: Categorizes verification methods (outcome reward models, process reward models, generative verifiers). Analyzes when and how to verify during test-time inference.
- **Results**: N/A (survey). Maps the verification design space including when to verify, what to verify, and how to verify.
- **Relation to B-IAVR**: Provides theoretical context. B-IAVR's "when to verify" question is a central theme in this survey, but applied to agent trajectories rather than reasoning chains.
- **Key insight**: Verification timing is identified as a key open problem across the field — B-IAVR provides a concrete solution for the agent setting.

---

## Direction 4: ALFWorld / Interactive Environment Benchmarks

### [ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection] (Kim et al., 2025)
- **Venue**: EMNLP 2025
- **Core contribution**: New reasoning backbone that grounds agent decisions in continuous state-goal reflection rather than next-action planning.
- **Method**: Replaces ReAct's "think about next action" with "reflect on current state relative to goal." Enforces ongoing goal alignment, preventing the compounding errors from ungrounded reasoning.
- **Results**: **93.3% success rate on ALFWorld** (+27.7% over ReAct). Outperforms ReAct + Reflexion, ReAct + WKM, and other enhancement modules.
- **Relation to B-IAVR**: Strong baseline / complementary. ReflAct achieves near-ceiling performance via prompting alone. B-IAVR addresses a different axis: cost-efficiency of verification, not peak accuracy. ReflAct always reflects; B-IAVR selectively verifies.
- **Key insight**: ALFWorld performance is approaching saturation via prompting methods. B-IAVR's value proposition is efficiency, not raw success rate.

### [AgentPRM: Process Reward Models for LLM Agents] (Chatterjee et al., 2025)
- **Venue**: ACM Web Conference 2026 (arXiv 2502.10325)
- **Core contribution**: Lightweight actor-critic framework using Monte Carlo rollouts for step-level reward in agent training.
- **Method**: Trains process reward model via Monte Carlo rollouts to provide dense step-level supervision. InversePRM extension learns process rewards from demonstrations without outcome supervision.
- **Results**: 3B models with AgentPRM/InversePRM achieve **88-91% success on ALFWorld**, exceeding GPT-4o prompting baselines.
- **Relation to B-IAVR**: Complementary. AgentPRM provides dense reward shaping for training; B-IAVR's Self-Guide provides internal reward. AgentPRM could potentially serve as the reward model for B-IAVR's verification policy.
- **Key insight**: Process reward models enable small models to match large prompted models on agent tasks — validates the RL training approach B-IAVR uses.

### [Retrospex: Language Agent Meets Offline RL Critic] (Xiang et al., 2024)
- **Venue**: EMNLP 2024
- **Core contribution**: Combines LLM action likelihood with offline RL critic trained on past experiences.
- **Method**: Instead of injecting experiences into LLM context, trains a separate RL Critic offline on past trajectories. Dynamic rescoring mechanism adjusts importance of experience-based values based on task interaction requirements.
- **Results**: Demonstrates advantages over baselines on ScienceWorld, ALFWorld, and WebShop. Dynamic rescoring adapts to task difficulty.
- **Relation to B-IAVR**: Complementary approach to experience utilization. Retrospex uses past experience for action selection; B-IAVR uses action-change signal for verification triggering. Both leverage learned value functions.
- **Key insight**: Offline RL Critic can effectively augment LLM agents; similar architecture could inform B-IAVR's verification value estimation.

### [CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning] (2026)
- **Venue**: arXiv (February 2026)
- **Core contribution**: Memory-augmented agent planning with episodic and environmental knowledge grounding.
- **Method**: Coarse-to-fine retrieval of grounded memories. Fine-tunes a compact knowledge-embedding model to bridge retrieved experience and current context.
- **Results**: ALFWorld SR +10.40%, WebShop SR +20%, ScienceWorld SR +31% over ReAct baseline.
- **Relation to B-IAVR**: Complementary memory approach. CFGM improves action quality via memory; B-IAVR improves efficiency via selective verification. Could be combined.
- **Key insight**: Grounded memory significantly helps agent planning in interactive environments.

### [Self-Guide on ALFWorld/ScienceWorld/WebShop] (2026)
- **Venue**: arXiv 2604.03098 (see Direction 2)
- **Core contribution**: Internal reward co-evolving with policy. Directly evaluated on ALFWorld.
- **Results**: 8% improvement over environment-reward-only baselines on ALFWorld with Qwen3-1.7B/4B. B-IAVR builds directly on this.
- **Relation to B-IAVR**: Direct predecessor. B-IAVR's codebase extends Self-Guide.
- **Key insight**: Self-guidance signal is effective for ALFWorld; B-IAVR extends it to trigger selective verification.

### [GiGPO on ALFWorld/WebShop] (Feng et al., 2025)
- **Venue**: NeurIPS 2025 (see Direction 2)
- **Results**: >12% over GRPO on ALFWorld, >9% on WebShop.
- **Relation to B-IAVR**: Core training algorithm. B-IAVR uses GiGPO as the policy optimizer.

### [SPEAR on ALFWorld/WebShop] (2025)
- **Venue**: ICLR 2026 (see Direction 2)
- **Results**: Up to +16.1% on ALFWorld, +20.7% on WebShop over GRPO baseline.
- **Relation to B-IAVR**: Complementary training recipe. SPEAR's self-imitation curriculum could augment B-IAVR's training.

### [ReSpAct: Harmonizing Reasoning, Speaking, and Acting] (2024)
- **Venue**: arXiv 2411.00927
- **Core contribution**: Integrates dialogue/reasoning/acting for conversational agent tasks.
- **Method**: Agent uses active dialogue to interpret instructions, clarify goals, resolve failures. Reduces invalid actions from 13% to 3%.
- **Results**: +6% over ReAct on ALFWorld. With ideal user input, approaches human expert (85.3% vs 88.8%).
- **Relation to B-IAVR**: Different axis (dialogue vs. verification). But invalid action reduction is relevant — B-IAVR's verification also prevents error propagation from bad actions.
- **Key insight**: Reducing invalid actions is a key lever for ALFWorld performance; B-IAVR's verification achieves this differently.

---

## ALFWorld SOTA Summary Table (2024-2026)

| Method | Model | Success Rate | Year | Note |
|--------|-------|-------------|------|------|
| ReAct (baseline) | GPT-4 | ~65% | 2023 | Prompting baseline |
| Reflexion | GPT-4 | ~75% | 2023 | +trial-level reflection |
| ReSpAct | GPT-4 | ~71% | 2024 | +dialogue integration |
| AgentPRM/InversePRM | 3B trained | 88-91% | 2025 | Process reward RL |
| GiGPO | 7B trained | ~77%+ | 2025 | +12% over GRPO |
| SPEAR + GiGPO | 7B trained | ~82%+ | 2025 | +5.1% over GiGPO |
| Self-Guide (co-evolve) | Qwen3-4B | ~83%+ | 2026 | +8% over env-reward |
| ReflAct | GPT-4 | **93.3%** | 2025 | Prompting SOTA |
| ReAct-Finetune | Trained | **96%** | 2025 | Finetuned upper bound |

---

## Gap Analysis

### Shared Limitations of Existing Work

1. **Verification is all-or-nothing**: Most self-correction methods (Reflexion, Self-Refine, MAR) apply verification uniformly to every step or every trial. None learn *when* verification adds value vs. wastes compute.

2. **Adaptive computation focuses on reasoning, not agents**: AutoThink, ARES, and "When to Solve, When to Verify" all address adaptive computation in single-turn reasoning settings. Multi-turn interactive agent settings are underexplored.

3. **Selective verification studied at workflow level, not step level**: Sherlock operates on DAG workflows with offline counterfactual analysis. No prior work learns step-level verification decisions *online* via RL in interactive environments.

4. **Self-verification overuse is identified but not solved in agents**: The Self-Verification Dilemma paper documents the problem in reasoning models. The equivalent problem in agents (unnecessary re-planning/re-observing) has not been formally studied.

5. **Agent RL training ignores verification cost**: GiGPO, SPEAR, WebAgent-R1, and SORL all optimize for task success. None account for the additional cost of verification steps in their reward design.

### B-IAVR's Differentiated Position

B-IAVR uniquely combines:

1. **Action-change signal as verification trigger**: Uses the discrepancy between self-guided expected action and actual observation as a learned signal for when verification is needed. No prior work uses this specific signal.

2. **RL-trained binary verification policy**: Unlike Derailer-Rerailer (heuristic stability check) or Sherlock (offline counterfactual analysis), B-IAVR trains the verification trigger end-to-end via RL, allowing it to adapt to environment dynamics.

3. **Multi-turn interactive agent setting**: Extends the adaptive computation paradigm from single-turn reasoning (AutoThink, ARES) to multi-turn agent trajectories with environment interaction.

4. **Cost-aware reward design**: Explicitly penalizes unnecessary verification in the RL reward, unlike prior agent RL work that only rewards task success.

5. **Builds on Self-Guide internal reward**: Leverages the co-evolving policy-reward framework, extending it with a principled mechanism for selective verification rather than universal self-guidance.

### Novelty Claim Assessment

**The claim is strong.** The intersection of "selective verification" + "RL-trained trigger" + "interactive agent setting" + "action-change signal" is novel. The closest competitors are:

- **Derailer-Rerailer** (ACL 2025): Selective verification but for reasoning chains, not agents. Uses heuristic trigger, not RL-trained.
- **ARES** (2026): Adaptive computation for agents but adjusts reasoning effort level, not verification decisions. Uses SFT, not RL.
- **Sherlock** (2025): Selective verification for workflows but offline/static, not learned online.
- **Self-Verification Dilemma** (2026): Identifies the overuse problem but proposes experience-pool solution for reasoning, not RL-trained policy for agents.

No existing work trains an RL policy to decide when to verify in interactive agent environments using action-change signals. B-IAVR occupies a clear gap.
