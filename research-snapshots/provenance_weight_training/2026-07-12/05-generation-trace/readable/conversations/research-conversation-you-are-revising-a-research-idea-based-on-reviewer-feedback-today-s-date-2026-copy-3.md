# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 88
- **Recorded user turns:** 1
- **Tool calls:** 25
- **Original source:** `logs/chats/exported-trajectories/account-3/2be61ec6-9efe-434d-aca6-59a9c3e9409c.jsonl`
- **Structured JSON:** [`a25a070dd8272870886b.json`](../../sessions/a2/a25a070dd8272870886b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T19:25:58.221Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T19:25:58.221Z",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Compositional Humanoid Loco-Manipulation Task Generation\",\n  \"core_problem\": \"Scaling humanoid loco-manipulation to diverse real-world tasks requires diverse training environments, but every loco-manipulation task in NVIDIA's AGILE/GR00T-WBC ecosystem must be manually specified as a self-contained Isaac Lab configuration file. VIRAL (CVPR 2026) demonstrates composite tasks work but identifies reward engineering as a scaling bottleneck. Eurekaverse (CoRL 2024) pioneered LLM-driven environment curriculum generation but only for single-skill training (quadruped parkour), generating environment variations rather than compositionally coupled multi-stage tasks. LLM-based reward methods (STRIDE, FORGE/EUREKA) automate reward optimization for single predefined tasks but cannot generate compositionally coupled tasks where inter-primitive dynamics (balance during walk-to-pick transitions, gait adaptation for carry, CoM shifts at primitive boundaries) create emergent failure modes absent from any individual primitive. The fundamental challenge is twofold: (1) composing novel multi-stage loco-manipulation tasks from a primitive grammar, and (2) efficiently predicting which compositions are dynamically feasible without exhaustive simulation—requiring a learned transition feasibility model that generalizes across primitive types and parameters. How can we combine a physics-informed skill grammar with a learned Transition Feasibility Network to automatically generate diverse, dynamically feasible loco-manipulation task configurations for Isaac Lab?\",\n  \"opportunity\": \"VIRAL (CVPR 2026) achieves 54 consecutive real-world loco-manipulation cycles on G1 but relies entirely on hand-designed stage-weighted rewards—the authors state that 'scaling to the open-ended diversity of daily life remains intractable' via manual reward engineering. Eurekaverse (CoRL 2024) automates environment curriculum generation via LLM code generation with agent-environment co-evolution, achieving superhuman parkour curricula—but operates on single-skill locomotion over terrain, with no manipulation, no inter-primitive coupling, and no compositional task structure. STRIDE (arXiv:2502.04692) and FORGE (OpenReview 2025) automate reward design for single tasks. DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single demonstration via object-centric replay—producing spatial variations of one task template but not compositionally novel tasks. LHM-Humanoid (arXiv:2508.16943) achieves impressive long-horizon loco-manipulation across 350 scenes but relies on manually designed configurations. Genie Sim 3.0 (arXiv:2601.02078) uses LLM-powered scene generation with 200+ tasks and 5140 assets but lacks formal compositional task specification and degrades on multi-step tasks (~52% vs ~80% for atomic tasks). In the learned composition space, Generative Skill Chaining (arXiv:2401.03360) uses diffusion models for skill precondition/effect chaining, and GSC (Robotics & Autonomous Systems, 2024) models skill sets as GNN graphs—but both target fixed-base manipulation without dynamics-aware feasibility for whole-body locomotion+manipulation coupling. SuperDyno (ICLR 2025 Workshop) learns neural dynamics for humanoid control but not for composition feasibility prediction. The gap is precise: no system combines (1) a grammar for compositional loco-manipulation task generation with (2) a learned transition feasibility predictor that efficiently determines which compositions are dynamically viable, enabling (3) active generation of training data for the AGILE/GR00T-WBC ecosystem.\",\n  \"landscape\": \"**LLM-based environment/curriculum generation**: Eurekaverse (arXiv:2411.01775, CoRL 2024) uses LLM code generation to produce increasingly challenging terrain environments for quadruped parkour, with agent-environment co-evolution over 5 generations. Key paradigm: LLM generates Python terrain functions → train policy → evaluate → feedback to LLM. However, it generates monolithic terrain programs for single-skill locomotion—no manipulation, no inter-primitive dynamics, no compositional task structure. CompLocoGen extends this paradigm to compositional multi-stage loco-manipulation: instead of varying a single environment, we compose multi-primitive task sequences and learn which compositions are dynamically feasible. Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) uses LLM-powered scene generation with RAG-based asset retrieval and DSL code generation to create thousands of diverse environments for humanoid manipulation across 200+ tasks—but lacks formal compositional grammar and shows performance degradation on multi-step tasks. **LLM-based reward design (per-task optimization)**: STRIDE (arXiv:2502.04692, Feb 2025) automates humanoid locomotion reward design via LLMs, 250% over EUREKA—single-task locomotion only. FORGE (OpenReview 2025) uses multi-agent LLMs for evolutionary reward refinement, 38.5% over EUREKA—single-task. EUREKA (ICLR 2024) established the LLM-to-reward-code paradigm. These solve per-task reward engineering; CompLocoGen solves the orthogonal problem of generating novel task compositions with learned feasibility prediction. **Demonstration-based data generation**: DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single teleoperated demonstration by converting to object-centric representations and replaying under varied initial conditions with a 3-stage pipeline (locomotion → pre-manipulation → manipulation) on Unitree G1. It produces spatial diversity within a fixed task template—not compositional novelty across task structures. CompLocoGen generates qualitatively different training data: novel task compositions (e.g., walk-pick-carry-climb_stairs-place) that no single demonstration could cover. **Learned skill composition approaches**: Generative Skill Chaining (arXiv:2401.03360, CoRL 2024) trains skill-level diffusion models capturing (precondition, parameters, effect) distributions for chaining—fixed-base manipulation only. SCaR (NeurIPS 2024) refines skill chaining with learned success predictors for sub-task transitions. GSC (Robotics & Autonomous Systems, 2024) models skill sets as GNN graphs with transformer-style architecture for skill embeddings. SuperDyno (ICLR 2025 Workshop) learns differentiable neural dynamics for humanoid whole-body control. None of these address composition feasibility for coupled loco-manipulation where locomotion dynamics (balance, gait) interact with manipulation state (load, grasp). CompLocoGen's Transition Feasibility Network operates specifically on the boundary states between loco-manipulation primitives, learning to predict whether locomotion-manipulation coupling will cause failure at transitions. **Sim-to-real composite tasks**: VIRAL/GR00T-VisualSim2Real (CVPR 2026, NVlabs) demonstrates composite loco-manipulation with 54 consecutive real-world cycles—hand-designed tasks. LHM-Humanoid (arXiv:2508.16943, March 2026) learns unified policies across 350 manually designed scenes via RL teacher distillation. FALCON (arXiv:2505.06776, L4DC 2026) demonstrates force-adaptive dual-agent RL for loco-manipulation on real humanoids—hand-designed tasks. WholeBodyVLA (ICLR 2026, arXiv:2512.11047) learns unified latent VLA—policy architecture orthogonal to task generation. **Scene graph and compositional approaches**: Scene Graph Atomic Skills (ICRA 2026) uses GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition—tabletop manipulation focus. GenManip (CVPR 2025) provides LLM-to-simulation-to-filter for tabletop manipulation. Humanoid Hanoi (arXiv:2602.13850, Feb 2026) demonstrates distribution shift during skill composition requiring data aggregation—directly informs our transition modeling. **The specific gap**: No system combines grammar-structured compositional task generation with a learned transition feasibility predictor for humanoid loco-manipulation. Eurekaverse generates single-skill environments; DemoHLM augments single demonstrations; Generative Skill Chaining/GSC learn feasibility for fixed-base manipulation; VIRAL/LHM-Humanoid use manually designed compositions. CompLocoGen uniquely combines: (a) a 7-primitive grammar generating exponentially many task compositions, (b) a GNN-based Transition Feasibility Network that learns loco-manipulation coupling dynamics from few-shot simulation rollouts, and (c) active generation targeting the uncertainty frontier of the feasibility predictor.\",\n  \"approach\": \"We build CompLocoGen as a grammar-structured system that learns transition feasibility for compositional loco-manipulation task generation, producing Isaac Lab-compatible configurations within 200 H100-hours.\\n\\n**Expanded Physics-Informed Skill Grammar (7 Primitives)**: We define a context-free grammar over seven coupled loco-manipulation primitives: walk(target_pos, speed, gait_style), pick(object_id, grasp_type, approach_vector), place(target_pos, placement_constraint), carry(object_id, carry_pose, stability_mode), push(object_id, direction, force_profile), open_door(door_id, handle_type, opening_angle), and squat(target_height, duration, stability_mode). Each primitive has typed spatial parameters, structural preconditions/postconditions, and a boundary state specification (the distribution of robot states—CoM position/velocity, joint configurations, contact states, grasp forces—at primitive entry/exit). The 7-primitive grammar produces 7^L valid structural sequences of length L (before feasibility filtering). For L=3-5 (typical loco-manipulation tasks), this yields 343-16,807 structural compositions. With parameter variation (3-5 settings per typed parameter), the effective task space is 10^4-10^6 unique configurations. Structural filtering (precondition/postcondition satisfaction) reduces this by ~60%; dynamic feasibility filtering further reduces by an experimentally measured factor—quantifying this reduction IS the key experimental result.\\n\\n**Transition Feasibility Network (TFN) — Core Algorithmic Contribution**: Instead of relying solely on analytical physics predicates (ZMP, centroidal dynamics), we introduce a GNN-based Transition Feasibility Network that learns to predict composition success probability from primitive boundary states. Architecture: Each primitive instance is a node with features encoding (primitive type, spatial parameters, expected boundary state statistics). Edges connect consecutive primitives in the composition. A message-passing GNN (3 layers, 128-dim) processes the composition graph and outputs per-edge transition feasibility scores ∈ [0,1] plus an overall composition feasibility score. Training proceeds in three phases: (1) Bootstrap: Seed the TFN with ~200 simulation rollouts (50 per transition type for the 4 most common transitions: walk→pick, pick→carry, carry→walk, walk→place) using analytical predicates to stratify sampling across feasible/infeasible boundary. (2) Active Learning: Use TFN uncertainty (MC-dropout variance) to identify which transition types and parameter regions have highest prediction uncertainty. Allocate simulation budget preferentially to these uncertain regions. After each batch of 50 rollouts, retrain TFN. (3) Generalization: Evaluate TFN's ability to predict feasibility for novel primitive types (push, open_door, squat) from only 20-30 rollouts per new transition type—testing whether the learned dynamics representations transfer across primitive types that share physical structure (e.g., all primitives involving load shifts share centroidal coupling features). The TFN's advantage over analytical predicates: (a) it captures non-obvious interaction effects that simplified analytical models miss (e.g., arm momentum during open_door affecting walking balance), (b) it improves with data rather than requiring manual engineering of new physics equations for each primitive type, (c) it provides calibrated uncertainty estimates enabling active generation. The TFN's advantage over monolithic learned feasibility models (e.g., training a classifier on full-task rollouts): the grammar structure means it only needs to learn local transition dynamics (O(P^2) transition types for P primitives = 49 for 7 primitives), not global task success from all possible sequences (exponential in length).\\n\\n**LLM-Guided Task Program Generation with Grammar Constraints**: The LLM (Qwen 3.6-35B-A3B) generates task programs as grammar-valid primitive sequences with spatial parameter bindings. The LLM reasons about task semantics (delivery routes, obstacle navigation, sequential manipulation schedules) while the grammar enforces structural validity and the TFN provides differentiable feasibility scores for soft-constraining the LLM's parameter choices. Generated programs are compiled into Isaac Lab Python @configclass environment configurations using AGILE's configuration-driven architecture: each becomes a self-contained file specifying scene setup, observation space, action space, staged reward functions (auto-generated from primitive sequence structure following VIRAL's stage-weighted approach), termination conditions, and curriculum parameters.\\n\\n**Active Composition Generation Loop**: Inspired by Eurekaverse's co-evolution but targeting compositional diversity rather than single-skill difficulty: (1) Generate batch of grammar-valid compositions via LLM. (2) TFN scores each composition; compositions above threshold proceed to simulation, compositions below threshold are rejected, compositions in the uncertain band are prioritized for simulation (active learning). (3) Simulate accepted compositions in Isaac Lab (4096 parallel environments). (4) Update TFN with new rollout data. (5) LLM receives feedback on which compositions succeeded/failed and why (structured failure mode analysis: balance failure, grasp loss, collision, timeout). This loop iterates for ~10 generations, progressively expanding the frontier of achievable compositions.\\n\\n**Pre-trained GR00T-WBC Execution**: Pre-trained SONIC locomotion checkpoint + PinkKinematics IK for upper-body manipulation. State-machine coordinator sequences SONIC commands and IK targets based on primitive transitions. For primitives requiring novel coordination (push, open_door), fine-tune with <5 H100-hours per primitive type using AGILE's training pipeline.\\n\\n**Downstream Evaluation with Compositional Generalization**: Train diffusion policy (ACT architecture) on generated datasets. Evaluate: (a) held-out compositions (novel primitive sequences), (b) held-out spatial configurations, (c) held-out dynamic parameters, (d) novel primitive types added post-training. Baselines: (1) Eurekaverse-style single-skill environment co-evolution (adapted to loco-manipulation: generate environment variations for individual primitives, then manually compose), (2) DemoHLM-style demo augmentation (single demo per task → spatial variations), (3) STRIDE-style per-task reward optimization for composed tasks, (4) Grammar-only composition with analytical predicates (no TFN), (5) Grammar + TFN without active learning (random composition sampling), (6) LLM-only generation without grammar constraints, (7) LHM-Humanoid-style manually designed task set (5-8 hand-designed compositions). Key ablations: TFN vs. analytical predicates (measures value of learning), active vs. random sampling (measures value of uncertainty-guided generation), grammar structure vs. unstructured composition (measures value of grammatical scaffold for learning).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180-200h H100\",\n      \"gpu_utilization\": \"25-35% effective; researcher idles GPU while designing grammar, implementing TFN architecture, debugging SONIC+IK integration, and iterating active learning loop\",\n      \"timeline\": \"7-8 weeks (1.5 weeks grammar design + TFN architecture + SONIC integration, 2 weeks TFN training + active generation loop, 2 weeks downstream training + evaluation, 1.5 weeks ablations + paper)\",\n      \"team\": \"1 researcher (requires familiarity with Isaac Lab, GNN training, and AGILE/GR00T-WBC)\",\n      \"estimated_gpu_cost\": \"$450-500 at ~$2.50/hr H100 spot pricing\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~170-200h H100\",\n      \"gpu_utilization\": \"55-70%; agent automates configclass generation, TFN training loops, experiment scheduling; idles during human review of TFN architecture decisions and generated task quality\",\n      \"timeline\": \"6-7 weeks (targeting Humanoids 2026 June 30 deadline, 51 days)\",\n      \"team\": \"1 researcher, ~25-35min/day reviewing TFN training curves, generated compositions, and demonstration quality\",\n      \"claude_api_cost\": \"$200-400 (2000-4000 agentic turns for Isaac Lab compilation, TFN training orchestration, and experiment analysis)\",\n      \"estimated_gpu_cost\": \"$425-500 at ~$2.50/hr H100 spot pricing\",\n      \"budget_breakdown\": \"~10h TFN bootstrap data collection (200 rollouts × 4096 envs), ~5h TFN training (GNN, fast on single GPU), ~5h SONIC fine-tuning for push/open_door/squat, ~60h active generation loop (10 generations × ~6h per generation: LLM generation + simulation verification + TFN update), ~60h downstream diffusion policy training, ~40h ablations (7 baselines + 3 key ablations), ~20h buffer/iteration\",\n      \"risk_note\": \"Primary risk: TFN may overfit to bootstrap distribution and fail to generalize to novel transition types with only 20-30 rollouts. Mitigation: architecture uses primitive-type-agnostic physical features (CoM velocity, contact forces, joint torques at boundaries) rather than type-specific embeddings. Secondary risk: SONIC checkpoint may need more than 5h fine-tuning for push/open_door primitives.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~190-200h H100 (budget-constrained)\",\n      \"gpu_utilization\": \"80-90%; agent operates continuously, prioritizing TFN active learning loop\",\n      \"timeline\": \"3-4 weeks with 4 H100 GPUs concurrently\",\n      \"team\": \"0 (initial 3-hour setup: configure AGILE, verify SONIC checkpoint, set LLM API keys, define TFN architecture)\",\n      \"claude_api_cost\": \"$350-750 (3500-7500 turns for autonomous pipeline development, TFN training, active generation, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$475-500 at ~$2.50/hr H100 spot pricing\",\n      \"speed_bottleneck\": \"Active learning loop requires sequential TFN updates between generation batches; physics verification throughput (4096 envs per H100, ~15 wall-clock hours for 1000 valid demonstrations)\",\n      \"risk_note\": \"Agent may over-explore TFN architecture variants vs. downstream evaluation; strict budget requires early stopping\"\n    }\n  },\n  \"target_venues\": [\n    \"Humanoids 2026 (paper deadline June 30, 2026 — 51 days, primary target. Ideal venue: humanoid-specific systems+algorithmic contribution, values both the grammar engineering and TFN learning contribution; conference Dec 6-9, Santa Clara CA)\",\n    \"ICRA 2027 (expected deadline ~September 2026 — allows extended ablations, potential real-robot transfer via AGILE's sim-to-real pipeline, and TFN generalization to more primitive types)\",\n    \"CoRL 2027 (expected deadline ~June 2027 — full learning-theoretic analysis of grammar-structured active feasibility learning, formal sample complexity bounds)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Eurekaverse: Environment Curriculum Generation via Large Language Models (CoRL 2024, arXiv:2411.01775, NVIDIA Research) — LLM-driven environment co-evolution for single-skill locomotion training; generates terrain programs for quadruped parkour. Key paradigm ancestor. Differentiation: single-skill environment variation vs. our compositional multi-stage task generation with learned transition dynamics\",\n    \"VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (CVPR 2026, arXiv:2511.15200, NVlabs) — hand-designed composite tasks on G1 with 54 consecutive real-world cycles; identifies reward engineering as scaling bottleneck. Primary comparison\",\n    \"DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (arXiv:2510.11258) — generates diverse trajectories from single demo via object-centric representation replay on Unitree G1. Produces spatial variations within fixed task template. Key data-generation baseline: demonstrates demo-augmentation cannot produce compositional novelty\",\n    \"AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning (arXiv:2603.20147, March 2026, github.com/nvidia-isaac/WBC-AGILE, Apache 2.0) — target substrate; configuration-driven Isaac Lab workflow. CompLocoGen generates upstream training task configurations\",\n    \"Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models (arXiv:2401.03360, CoRL 2024) — trains skill-level diffusion models for precondition/effect-based chaining in fixed-base manipulation. Informs our TFN's per-edge feasibility prediction but does not address loco-manipulation coupling\",\n    \"GSC: A Graph-based Skill Composition Framework for Robot Learning (Robotics & Autonomous Systems, 2024) — GNN over skill graphs with transformer-style architecture. Architectural inspiration for our Transition Feasibility Network\",\n    \"SCaR: Refining Skill Chaining for Long-Horizon Robotic Manipulation (NeurIPS 2024) — learned success predictors for sub-task transitions; validates that transition feasibility can be learned from few-shot rollouts\",\n    \"SuperDyno: Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics (ICLR 2025 Workshop) — learns neural dynamics for humanoid control replacing analytical simulators. Validates that humanoid dynamics can be captured by neural networks\",\n    \"Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) — LLM-powered scene generation with 200+ tasks, 5140 assets. Large-scale generation without compositional grammar; performance degrades on multi-step tasks\",\n    \"STRIDE: Automating Reward Design for Humanoid Robotics Locomotion (arXiv:2502.04692, Feb 2025) — automates single-task locomotion reward design via LLMs, 250% over EUREKA. Cannot compose multi-stage tasks\",\n    \"FORGE: Forging Better Rewards via Multi-Agent LLM Framework (OpenReview 2025) — multi-agent LLM reward evolution, 38.5% over EUREKA. Single-task; does not address task composition\",\n    \"EUREKA: Human-Level Reward Design via Coding LLMs (ICLR 2024, arXiv:2310.12931) — established LLM reward optimization paradigm\",\n    \"LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation (arXiv:2508.16943, March 2026) — 350 diverse scenes, RL teacher + DAgger. Manually designed scenes; CompLocoGen could serve as automated task generator\",\n    \"WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026, arXiv:2512.11047) — policy architecture orthogonal to task generation\",\n    \"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation (arXiv:2505.06776, L4DC 2026) — force-adaptive dual-agent RL on real humanoids; validates deployability, hand-designed tasks\",\n    \"Scene Graph Atomic Skills (ICRA 2026, Harvard) — GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition; tabletop focus\",\n    \"Humanoid Hanoi (arXiv:2602.13850, Feb 2026) — distribution shift during skill composition; directly informs our transition feasibility learning\",\n    \"GR00T-WholeBodyControl/SONIC (NVlabs, open-source Apache 2.0) — pre-trained G1 locomotion checkpoints (142K+ motions), decoupled WBC\",\n    \"GenManip: LLM-driven Simulation for Generalizable Manipulation (CVPR 2025) — LLM-to-simulation-to-filter paradigm for tabletop manipulation\",\n    \"GR00T-Gen (NVIDIA, 2025) — generates 100+ individual tasks, not compositionally coupled\",\n    \"Isaac Lab (arXiv:2511.04831) — Python @configclass manager-based workflow for environment specification\",\n    \"SkillBlender (arXiv:2506.09366) — compositional skill blending on G1, manual specification\"\n  ],\n  \"description\": \"We propose CompLocoGen, a system that combines a physics-informed skill grammar with a learned Transition Feasibility Network (TFN) to automatically generate diverse humanoid loco-manipulation training environments for NVIDIA's AGILE/Isaac Lab ecosystem—within 200 H100-hours. The core algorithmic contribution is the TFN: a GNN-based model that learns to predict whether primitive transitions in a composed task sequence will succeed, trained via active learning from targeted simulation rollouts at primitive boundaries. This addresses a limitation of both analytical approaches (which require manual engineering per primitive type and miss non-obvious coupling effects) and monolithic learned models (which face exponential sample complexity in composition length). The grammar provides structure that makes transition feasibility learnable from O(100) rollouts per transition type: instead of learning global task success (exponential), the TFN learns local boundary dynamics (quadratic in primitive count). We define a 7-primitive grammar (walk, pick, place, carry, push, open_door, squat) producing 10^4-10^6 parametrized compositions, and quantify how structural filtering, analytical predicates, and learned TFN filtering progressively reduce this space to dynamically feasible tasks. An active generation loop (inspired by Eurekaverse's co-evolution but targeting compositional diversity) iteratively expands the frontier of achievable compositions by allocating simulation budget to high-uncertainty transition regions. Generated task programs compile to Isaac Lab @configclass configurations. Execution leverages GR00T-WBC's pre-trained SONIC locomotion and PinkKinematics IK. Evaluation compares against 7 baselines including Eurekaverse-style single-skill co-evolution, DemoHLM-style demo augmentation, STRIDE-style per-task reward optimization, and grammar-only analytical filtering—with key ablations isolating the value of learned feasibility, active sampling, and grammar structure. Primary target: Humanoids 2026 (June 30, 51 days).\",\n  \"project_name\": \"llm_locomanip_factory\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 5)\nIssues: [\"CRITICAL: VENUE/TIMELINE MISMATCH WITH USER REQUIREMENTS. The user explicitly targets CoRL 2026 (abstract May 26, paper May 29, ≤20 days). The proposal abandons CoRL entirely, targeting Humanoids 2026 (July 24, 75 days) as primary with ICRA 2027 and CoRL 2027 as secondary. The manual timeline (7-8 weeks) and even auto-research timeline (3-4 weeks) exceed the user's 20-day hard constraint. The proposal must either present a CoRL-feasible minimal scope or explicitly justify why CoRL 2026 cannot be met while proposing a concrete alternative the user can accept.\", \"MISSING COMPETING WORK: RoboGene (arXiv:2602.16444, Feb 2026) generates diverse robot tasks with three LLM-based feasibility evaluators (physical, novelty, constraint adherence), diversity-driven LFU sampling, and self-reflection refinement. It produces 18K trajectories across 900 tasks. While its mechanism differs (LLM-based evaluation vs. learned GNN prediction), it directly addresses the same problem of automated diverse feasibility-aware task generation. The proposal must cite and differentiate: RoboGene uses post-hoc LLM feasibility fixing; CompLocoGen uses learned upfront prediction with compositional structure. RoboGene targets general manipulation; CompLocoGen targets humanoid loco-manipulation with coupled dynamics.\", \"MISSING COMPETING WORK: FATE (arXiv:2603.01505, March 2026) proposes closed-loop feasibility-aware task generation with active repair using VLM auditors (static + dynamic phases). While FATE targets individual tasks on mobile manipulators (not compositional humanoid tasks), it directly occupies the 'feasibility-aware task generation' space. The TFN's advantage over FATE—learned boundary dynamics vs. VLM-based auditing, compositional structure vs. single tasks—should be articulated.\", \"MISSING REFERENCE: Ψ₀ (arXiv:2603.12263, March 2026) is a foundation model for universal humanoid loco-manipulation using staged VLM pre-training on human video + robot data fine-tuning. While it's a policy model (not task generation), it represents a key potential downstream consumer of CompLocoGen's generated tasks and should be mentioned to strengthen the impact argument.\", \"TFN GENERALIZATION CLAIM UNSUBSTANTIATED: The proposal claims the TFN can generalize to novel primitive types (push, open_door, squat) from only 20-30 rollouts per new transition type, arguing that 'primitive-type-agnostic physical features (CoM velocity, contact forces, joint torques)' enable transfer. This is a strong empirical claim with no supporting evidence. While architecturally plausible, it should be framed as a key experimental hypothesis, not a design assumption. If generalization fails, the active learning budget for 7 primitives grows substantially.\", \"HUMANOIDS 2026 DEADLINE ERROR: The proposal claims 'paper deadline June 30, 2026 — 51 days' but the official Humanoids 2026 website (2026.ieee-humanoids.org) indicates the paper submission deadline is July 24, 2026 (75 days from today). This is favorable (more time) but suggests the deadline wasn't verified against the official source.\", \"MINOR: Generative Skill Chaining is cited as 'CoRL 2024' but appears to be CoRL 2023 (arXiv:2401.03360 submitted Jan 2024 but the paper was at CoRL 2023). Verify and correct.\"]\nFeedback: The proposal has improved substantially over 5 rounds — the TFN is a genuine novelty contribution and the compute/infrastructure are now realistic. Three targeted changes would bring this to pass quality:\n\n1. **ADDRESS CoRL 2026 OR JUSTIFY ALTERNATIVE**: The user's requirement is CoRL 2026 (20 days). You must either: (a) Present a CoRL-minimal scope: 3 primitives (walk/pick/place), pre-trained SONIC+IK, TFN with bootstrap-only training (no full active learning loop), 3 compositions, single downstream eval, no ablations — essentially demonstrating TFN feasibility prediction works. Use the Humanoids deadline for the full 7-primitive + active learning + ablation paper. OR (b) Make a compelling case that the TFN contribution requires the full evaluation to be convincing and that a stripped-down CoRL submission would be rejected anyway — then commit to Humanoids 2026 (actual deadline July 24 = 75 days, plenty of time).\n\n2. **ADD RoboGene AND FATE TO LANDSCAPE**: Both are 2026 works in automated feasibility-aware task generation. Your differentiation is clear and strong: (a) vs. RoboGene: learned GNN prediction vs. LLM-based evaluation; compositional grammar structure vs. free-form LLM generation; humanoid-specific coupled dynamics vs. general manipulation. (b) vs. FATE: upfront composition-level prediction vs. per-task post-hoc VLM auditing; compositional multi-stage tasks vs. single tasks; humanoid loco-manipulation vs. mobile manipulation. Frame RoboGene as a baseline comparison if possible.\n\n3. **REFRAME TFN GENERALIZATION AS HYPOTHESIS**: Change the 20-30 rollout generalization claim from a design assumption to a key experimental question. State: 'We hypothesize that primitive-type-agnostic physical features enable few-shot transfer; quantifying the number of rollouts needed per novel primitive type IS a key experimental result.' Budget contingency compute (10-20h) in case generalization requires more rollouts than expected.\n\nMinor: Fix Humanoids 2026 deadline to July 24 (more favorable). Verify Generative Skill Chaining venue (CoRL 2023 vs 2024). Add Ψ₀ as a downstream consumer in the impact discussion.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 3.2 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T19:25:58.226Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T19:25:58.226Z",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

## Round 1

86 recorded events

### User

_source line 3 · 2026-05-10T19:25:58.372Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "CompLocoGen: Grammar-Structured Transition Feasibility Learning for Compositional Humanoid Loco-Manipulation Task Generation",
  "core_problem": "Scaling humanoid loco-manipulation to diverse real-world tasks requires diverse training environments, but every loco-manipulation task in NVIDIA's AGILE/GR00T-WBC ecosystem must be manually specified as a self-contained Isaac Lab configuration file. VIRAL (CVPR 2026) demonstrates composite tasks work but identifies reward engineering as a scaling bottleneck. Eurekaverse (CoRL 2024) pioneered LLM-driven environment curriculum generation but only for single-skill training (quadruped parkour), generating environment variations rather than compositionally coupled multi-stage tasks. LLM-based reward methods (STRIDE, FORGE/EUREKA) automate reward optimization for single predefined tasks but cannot generate compositionally coupled tasks where inter-primitive dynamics (balance during walk-to-pick transitions, gait adaptation for carry, CoM shifts at primitive boundaries) create emergent failure modes absent from any individual primitive. The fundamental challenge is twofold: (1) composing novel multi-stage loco-manipulation tasks from a primitive grammar, and (2) efficiently predicting which compositions are dynamically feasible without exhaustive simulation—requiring a learned transition feasibility model that generalizes across primitive types and parameters. How can we combine a physics-informed skill grammar with a learned Transition Feasibility Network to automatically generate diverse, dynamically feasible loco-manipulation task configurations for Isaac Lab?",
  "opportunity": "VIRAL (CVPR 2026) achieves 54 consecutive real-world loco-manipulation cycles on G1 but relies entirely on hand-designed stage-weighted rewards—the authors state that 'scaling to the open-ended diversity of daily life remains intractable' via manual reward engineering. Eurekaverse (CoRL 2024) automates environment curriculum generation via LLM code generation with agent-environment co-evolution, achieving superhuman parkour curricula—but operates on single-skill locomotion over terrain, with no manipulation, no inter-primitive coupling, and no compositional task structure. STRIDE (arXiv:2502.04692) and FORGE (OpenReview 2025) automate reward design for single tasks. DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single demonstration via object-centric replay—producing spatial variations of one task template but not compositionally novel tasks. LHM-Humanoid (arXiv:2508.16943) achieves impressive long-horizon loco-manipulation across 350 scenes but relies on manually designed configurations. Genie Sim 3.0 (arXiv:2601.02078) uses LLM-powered scene generation with 200+ tasks and 5140 assets but lacks formal compositional task specification and degrades on multi-step tasks (~52% vs ~80% for atomic tasks). In the learned composition space, Generative Skill Chaining (arXiv:2401.03360) uses diffusion models for skill precondition/effect chaining, and GSC (Robotics & Autonomous Systems, 2024) models skill sets as GNN graphs—but both target fixed-base manipulation without dynamics-aware feasibility for whole-body locomotion+manipulation coupling. SuperDyno (ICLR 2025 Workshop) learns neural dynamics for humanoid control but not for composition feasibility prediction. The gap is precise: no system combines (1) a grammar for compositional loco-manipulation task generation with (2) a learned transition feasibility predictor that efficiently determines which compositions are dynamically viable, enabling (3) active generation of training data for the AGILE/GR00T-WBC ecosystem.",
  "landscape": "**LLM-based environment/curriculum generation**: Eurekaverse (arXiv:2411.01775, CoRL 2024) uses LLM code generation to produce increasingly challenging terrain environments for quadruped parkour, with agent-environment co-evolution over 5 generations. Key paradigm: LLM generates Python terrain functions → train policy → evaluate → feedback to LLM. However, it generates monolithic terrain programs for single-skill locomotion—no manipulation, no inter-primitive dynamics, no compositional task structure. CompLocoGen extends this paradigm to compositional multi-stage loco-manipulation: instead of varying a single environment, we compose multi-primitive task sequences and learn which compositions are dynamically feasible. Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) uses LLM-powered scene generation with RAG-based asset retrieval and DSL code generation to create thousands of diverse environments for humanoid manipulation across 200+ tasks—but lacks formal compositional grammar and shows performance degradation on multi-step tasks. **LLM-based reward design (per-task optimization)**: STRIDE (arXiv:2502.04692, Feb 2025) automates humanoid locomotion reward design via LLMs, 250% over EUREKA—single-task locomotion only. FORGE (OpenReview 2025) uses multi-agent LLMs for evolutionary reward refinement, 38.5% over EUREKA—single-task. EUREKA (ICLR 2024) established the LLM-to-reward-code paradigm. These solve per-task reward engineering; CompLocoGen solves the orthogonal problem of generating novel task compositions with learned feasibility prediction. **Demonstration-based data generation**: DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single teleoperated demonstration by converting to object-centric representations and replaying under varied initial conditions with a 3-stage pipeline (locomotion → pre-manipulation → manipulation) on Unitree G1. It produces spatial diversity within a fixed task template—not compositional novelty across task structures. CompLocoGen generates qualitatively different training data: novel task compositions (e.g., walk-pick-carry-climb_stairs-place) that no single demonstration could cover. **Learned skill composition approaches**: Generative Skill Chaining (arXiv:2401.03360, CoRL 2024) trains skill-level diffusion models capturing (precondition, parameters, effect) distributions for chaining—fixed-base manipulation only. SCaR (NeurIPS 2024) refines skill chaining with learned success predictors for sub-task transitions. GSC (Robotics & Autonomous Systems, 2024) models skill sets as GNN graphs with transformer-style architecture for skill embeddings. SuperDyno (ICLR 2025 Workshop) learns differentiable neural dynamics for humanoid whole-body control. None of these address composition feasibility for coupled loco-manipulation where locomotion dynamics (balance, gait) interact with manipulation state (load, grasp). CompLocoGen's Transition Feasibility Network operates specifically on the boundary states between loco-manipulation primitives, learning to predict whether locomotion-manipulation coupling will cause failure at transitions. **Sim-to-real composite tasks**: VIRAL/GR00T-VisualSim2Real (CVPR 2026, NVlabs) demonstrates composite loco-manipulation with 54 consecutive real-world cycles—hand-designed tasks. LHM-Humanoid (arXiv:2508.16943, March 2026) learns unified policies across 350 manually designed scenes via RL teacher distillation. FALCON (arXiv:2505.06776, L4DC 2026) demonstrates force-adaptive dual-agent RL for loco-manipulation on real humanoids—hand-designed tasks. WholeBodyVLA (ICLR 2026, arXiv:2512.11047) learns unified latent VLA—policy architecture orthogonal to task generation. **Scene graph and compositional approaches**: Scene Graph Atomic Skills (ICRA 2026) uses GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition—tabletop manipulation focus. GenManip (CVPR 2025) provides LLM-to-simulation-to-filter for tabletop manipulation. Humanoid Hanoi (arXiv:2602.13850, Feb 2026) demonstrates distribution shift during skill composition requiring data aggregation—directly informs our transition modeling. **The specific gap**: No system combines grammar-structured compositional task generation with a learned transition feasibility predictor for humanoid loco-manipulation. Eurekaverse generates single-skill environments; DemoHLM augments single demonstrations; Generative Skill Chaining/GSC learn feasibility for fixed-base manipulation; VIRAL/LHM-Humanoid use manually designed compositions. CompLocoGen uniquely combines: (a) a 7-primitive grammar generating exponentially many task compositions, (b) a GNN-based Transition Feasibility Network that learns loco-manipulation coupling dynamics from few-shot simulation rollouts, and (c) active generation targeting the uncertainty frontier of the feasibility predictor.",
  "approach": "We build CompLocoGen as a grammar-structured system that learns transition feasibility for compositional loco-manipulation task generation, producing Isaac Lab-compatible configurations within 200 H100-hours.\n\n**Expanded Physics-Informed Skill Grammar (7 Primitives)**: We define a context-free grammar over seven coupled loco-manipulation primitives: walk(target_pos, speed, gait_style), pick(object_id, grasp_type, approach_vector), place(target_pos, placement_constraint), carry(object_id, carry_pose, stability_mode), push(object_id, direction, force_profile), open_door(door_id, handle_type, opening_angle), and squat(target_height, duration, stability_mode). Each primitive has typed spatial parameters, structural preconditions/postconditions, and a boundary state specification (the distribution of robot states—CoM position/velocity, joint configurations, contact states, grasp forces—at primitive entry/exit). The 7-primitive grammar produces 7^L valid structural sequences of length L (before feasibility filtering). For L=3-5 (typical loco-manipulation tasks), this yields 343-16,807 structural compositions. With parameter variation (3-5 settings per typed parameter), the effective task space is 10^4-10^6 unique configurations. Structural filtering (precondition/postcondition satisfaction) reduces this by ~60%; dynamic feasibility filtering further reduces by an experimentally measured factor—quantifying this reduction IS the key experimental result.\n\n**Transition Feasibility Network (TFN) — Core Algorithmic Contribution**: Instead of relying solely on analytical physics predicates (ZMP, centroidal dynamics), we introduce a GNN-based Transition Feasibility Network that learns to predict composition success probability from primitive boundary states. Architecture: Each primitive instance is a node with features encoding (primitive type, spatial parameters, expected boundary state statistics). Edges connect consecutive primitives in the composition. A message-passing GNN (3 layers, 128-dim) processes the composition graph and outputs per-edge transition feasibility scores ∈ [0,1] plus an overall composition feasibility score. Training proceeds in three phases: (1) Bootstrap: Seed the TFN with ~200 simulation rollouts (50 per transition type for the 4 most common transitions: walk→pick, pick→carry, carry→walk, walk→place) using analytical predicates to stratify sampling across feasible/infeasible boundary. (2) Active Learning: Use TFN uncertainty (MC-dropout variance) to identify which transition types and parameter regions have highest prediction uncertainty. Allocate simulation budget preferentially to these uncertain regions. After each batch of 50 rollouts, retrain TFN. (3) Generalization: Evaluate TFN's ability to predict feasibility for novel primitive types (push, open_door, squat) from only 20-30 rollouts per new transition type—testing whether the learned dynamics representations transfer across primitive types that share physical structure (e.g., all primitives involving load shifts share centroidal coupling features). The TFN's advantage over analytical predicates: (a) it captures non-obvious interaction effects that simplified analytical models miss (e.g., arm momentum during open_door affecting walking balance), (b) it improves with data rather than requiring manual engineering of new physics equations for each primitive type, (c) it provides calibrated uncertainty estimates enabling active generation. The TFN's advantage over monolithic learned feasibility models (e.g., training a classifier on full-task rollouts): the grammar structure means it only needs to learn local transition dynamics (O(P^2) transition types for P primitives = 49 for 7 primitives), not global task success from all possible sequences (exponential in length).\n\n**LLM-Guided Task Program Generation with Grammar Constraints**: The LLM (Qwen 3.6-35B-A3B) generates task programs as grammar-valid primitive sequences with spatial parameter bindings. The LLM reasons about task semantics (delivery routes, obstacle navigation, sequential manipulation schedules) while the grammar enforces structural validity and the TFN provides differentiable feasibility scores for soft-constraining the LLM's parameter choices. Generated programs are compiled into Isaac Lab Python @configclass environment configurations using AGILE's configuration-driven architecture: each becomes a self-contained file specifying scene setup, observation space, action space, staged reward functions (auto-generated from primitive sequence structure following VIRAL's stage-weighted approach), termination conditions, and curriculum parameters.\n\n**Active Composition Generation Loop**: Inspired by Eurekaverse's co-evolution but targeting compositional diversity rather than single-skill difficulty: (1) Generate batch of grammar-valid compositions via LLM. (2) TFN scores each composition; compositions above threshold proceed to simulation, compositions below threshold are rejected, compositions in the uncertain band are prioritized for simulation (active learning). (3) Simulate accepted compositions in Isaac Lab (4096 parallel environments). (4) Update TFN with new rollout data. (5) LLM receives feedback on which compositions succeeded/failed and why (structured failure mode analysis: balance failure, grasp loss, collision, timeout). This loop iterates for ~10 generations, progressively expanding the frontier of achievable compositions.\n\n**Pre-trained GR00T-WBC Execution**: Pre-trained SONIC locomotion checkpoint + PinkKinematics IK for upper-body manipulation. State-machine coordinator sequences SONIC commands and IK targets based on primitive transitions. For primitives requiring novel coordination (push, open_door), fine-tune with <5 H100-hours per primitive type using AGILE's training pipeline.\n\n**Downstream Evaluation with Compositional Generalization**: Train diffusion policy (ACT architecture) on generated datasets. Evaluate: (a) held-out compositions (novel primitive sequences), (b) held-out spatial configurations, (c) held-out dynamic parameters, (d) novel primitive types added post-training. Baselines: (1) Eurekaverse-style single-skill environment co-evolution (adapted to loco-manipulation: generate environment variations for individual primitives, then manually compose), (2) DemoHLM-style demo augmentation (single demo per task → spatial variations), (3) STRIDE-style per-task reward optimization for composed tasks, (4) Grammar-only composition with analytical predicates (no TFN), (5) Grammar + TFN without active learning (random composition sampling), (6) LLM-only generation without grammar constraints, (7) LHM-Humanoid-style manually designed task set (5-8 hand-designed compositions). Key ablations: TFN vs. analytical predicates (measures value of learning), active vs. random sampling (measures value of uncertainty-guided generation), grammar structure vs. unstructured composition (measures value of grammatical scaffold for learning).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180-200h H100",
      "gpu_utilization": "25-35% effective; researcher idles GPU while designing grammar, implementing TFN architecture, debugging SONIC+IK integration, and iterating active learning loop",
      "timeline": "7-8 weeks (1.5 weeks grammar design + TFN architecture + SONIC integration, 2 weeks TFN training + active generation loop, 2 weeks downstream training + evaluation, 1.5 weeks ablations + paper)",
      "team": "1 researcher (requires familiarity with Isaac Lab, GNN training, and AGILE/GR00T-WBC)",
      "estimated_gpu_cost": "$450-500 at ~$2.50/hr H100 spot pricing"
    },
    "human_in_loop": {
      "gpu_hours": "~170-200h H100",
      "gpu_utilization": "55-70%; agent automates configclass generation, TFN training loops, experiment scheduling; idles during human review of TFN architecture decisions and generated task quality",
      "timeline": "6-7 weeks (targeting Humanoids 2026 June 30 deadline, 51 days)",
      "team": "1 researcher, ~25-35min/day reviewing TFN training curves, generated compositions, and demonstration quality",
      "claude_api_cost": "$200-400 (2000-4000 agentic turns for Isaac Lab compilation, TFN training orchestration, and experiment analysis)",
      "estimated_gpu_cost": "$425-500 at ~$2.50/hr H100 spot pricing",
      "budget_breakdown": "~10h TFN bootstrap data collection (200 rollouts × 4096 envs), ~5h TFN training (GNN, fast on single GPU), ~5h SONIC fine-tuning for push/open_door/squat, ~60h active generation loop (10 generations × ~6h per generation: LLM generation + simulation verification + TFN update), ~60h downstream diffusion policy training, ~40h ablations (7 baselines + 3 key ablations), ~20h buffer/iteration",
      "risk_note": "Primary risk: TFN may overfit to bootstrap distribution and fail to generalize to novel transition types with only 20-30 rollouts. Mitigation: architecture uses primitive-type-agnostic physical features (CoM velocity, contact forces, joint torques at boundaries) rather than type-specific embeddings. Secondary risk: SONIC checkpoint may need more than 5h fine-tuning for push/open_door primitives."
    },
    "auto_research": {
      "gpu_hours": "~190-200h H100 (budget-constrained)",
      "gpu_utilization": "80-90%; agent operates continuously, prioritizing TFN active learning loop",
      "timeline": "3-4 weeks with 4 H100 GPUs concurrently",
      "team": "0 (initial 3-hour setup: configure AGILE, verify SONIC checkpoint, set LLM API keys, define TFN architecture)",
      "claude_api_cost": "$350-750 (3500-7500 turns for autonomous pipeline development, TFN training, active generation, and paper drafting)",
      "estimated_gpu_cost": "$475-500 at ~$2.50/hr H100 spot pricing",
      "speed_bottleneck": "Active learning loop requires sequential TFN updates between generation batches; physics verification throughput (4096 envs per H100, ~15 wall-clock hours for 1000 valid demonstrations)",
      "risk_note": "Agent may over-explore TFN architecture variants vs. downstream evaluation; strict budget requires early stopping"
    }
  },
  "target_venues": [
    "Humanoids 2026 (paper deadline June 30, 2026 — 51 days, primary target. Ideal venue: humanoid-specific systems+algorithmic contribution, values both the grammar engineering and TFN learning contribution; conference Dec 6-9, Santa Clara CA)",
    "ICRA 2027 (expected deadline ~September 2026 — allows extended ablations, potential real-robot transfer via AGILE's sim-to-real pipeline, and TFN generalization to more primitive types)",
    "CoRL 2027 (expected deadline ~June 2027 — full learning-theoretic analysis of grammar-structured active feasibility learning, formal sample complexity bounds)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Eurekaverse: Environment Curriculum Generation via Large Language Models (CoRL 2024, arXiv:2411.01775, NVIDIA Research) — LLM-driven environment co-evolution for single-skill locomotion training; generates terrain programs for quadruped parkour. Key paradigm ancestor. Differentiation: single-skill environment variation vs. our compositional multi-stage task generation with learned transition dynamics",
    "VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (CVPR 2026, arXiv:2511.15200, NVlabs) — hand-designed composite tasks on G1 with 54 consecutive real-world cycles; identifies reward engineering as scaling bottleneck. Primary comparison",
    "DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (arXiv:2510.11258) — generates diverse trajectories from single demo via object-centric representation replay on Unitree G1. Produces spatial variations within fixed task template. Key data-generation baseline: demonstrates demo-augmentation cannot produce compositional novelty",
    "AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning (arXiv:2603.20147, March 2026, github.com/nvidia-isaac/WBC-AGILE, Apache 2.0) — target substrate; configuration-driven Isaac Lab workflow. CompLocoGen generates upstream training task configurations",
    "Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models (arXiv:2401.03360, CoRL 2024) — trains skill-level diffusion models for precondition/effect-based chaining in fixed-base manipulation. Informs our TFN's per-edge feasibility prediction but does not address loco-manipulation coupling",
    "GSC: A Graph-based Skill Composition Framework for Robot Learning (Robotics & Autonomous Systems, 2024) — GNN over skill graphs with transformer-style architecture. Architectural inspiration for our Transition Feasibility Network",
    "SCaR: Refining Skill Chaining for Long-Horizon Robotic Manipulation (NeurIPS 2024) — learned success predictors for sub-task transitions; validates that transition feasibility can be learned from few-shot rollouts",
    "SuperDyno: Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics (ICLR 2025 Workshop) — learns neural dynamics for humanoid control replacing analytical simulators. Validates that humanoid dynamics can be captured by neural networks",
    "Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) — LLM-powered scene generation with 200+ tasks, 5140 assets. Large-scale generation without compositional grammar; performance degrades on multi-step tasks",
    "STRIDE: Automating Reward Design for Humanoid Robotics Locomotion (arXiv:2502.04692, Feb 2025) — automates single-task locomotion reward design via LLMs, 250% over EUREKA. Cannot compose multi-stage tasks",
    "FORGE: Forging Better Rewards via Multi-Agent LLM Framework (OpenReview 2025) — multi-agent LLM reward evolution, 38.5% over EUREKA. Single-task; does not address task composition",
    "EUREKA: Human-Level Reward Design via Coding LLMs (ICLR 2024, arXiv:2310.12931) — established LLM reward optimization paradigm",
    "LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation (arXiv:2508.16943, March 2026) — 350 diverse scenes, RL teacher + DAgger. Manually designed scenes; CompLocoGen could serve as automated task generator",
    "WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026, arXiv:2512.11047) — policy architecture orthogonal to task generation",
    "FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation (arXiv:2505.06776, L4DC 2026) — force-adaptive dual-agent RL on real humanoids; validates deployability, hand-designed tasks",
    "Scene Graph Atomic Skills (ICRA 2026, Harvard) — GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition; tabletop focus",
    "Humanoid Hanoi (arXiv:2602.13850, Feb 2026) — distribution shift during skill composition; directly informs our transition feasibility learning",
    "GR00T-WholeBodyControl/SONIC (NVlabs, open-source Apache 2.0) — pre-trained G1 locomotion checkpoints (142K+ motions), decoupled WBC",
    "GenManip: LLM-driven Simulation for Generalizable Manipulation (CVPR 2025) — LLM-to-simulation-to-filter paradigm for tabletop manipulation",
    "GR00T-Gen (NVIDIA, 2025) — generates 100+ individual tasks, not compositionally coupled",
    "Isaac Lab (arXiv:2511.04831) — Python @configclass manager-based workflow for environment specification",
    "SkillBlender (arXiv:2506.09366) — compositional skill blending on G1, manual specification"
  ],
  "description": "We propose CompLocoGen, a system that combines a physics-informed skill grammar with a learned Transition Feasibility Network (TFN) to automatically generate diverse humanoid loco-manipulation training environments for NVIDIA's AGILE/Isaac Lab ecosystem—within 200 H100-hours. The core algorithmic contribution is the TFN: a GNN-based model that learns to predict whether primitive transitions in a composed task sequence will succeed, trained via active learning from targeted simulation rollouts at primitive boundaries. This addresses a limitation of both analytical approaches (which require manual engineering per primitive type and miss non-obvious coupling effects) and monolithic learned models (which face exponential sample complexity in composition length). The grammar provides structure that makes transition feasibility learnable from O(100) rollouts per transition type: instead of learning global task success (exponential), the TFN learns local boundary dynamics (quadratic in primitive count). We define a 7-primitive grammar (walk, pick, place, carry, push, open_door, squat) producing 10^4-10^6 parametrized compositions, and quantify how structural filtering, analytical predicates, and learned TFN filtering progressively reduce this space to dynamically feasible tasks. An active generation loop (inspired by Eurekaverse's co-evolution but targeting compositional diversity) iteratively expands the frontier of achievable compositions by allocating simulation budget to high-uncertainty transition regions. Generated task programs compile to Isaac Lab @configclass configurations. Execution leverages GR00T-WBC's pre-trained SONIC locomotion and PinkKinematics IK. Evaluation compares against 7 baselines including Eurekaverse-style single-skill co-evolution, DemoHLM-style demo augmentation, STRIDE-style per-task reward optimization, and grammar-only analytical filtering—with key ablations isolating the value of learned feasibility, active sampling, and grammar structure. Primary target: Humanoids 2026 (June 30, 51 days).",
  "project_name": "llm_locomanip_factory",
  "source": "web_research"
}

## Reviewer feedback (round 5)
Issues: ["CRITICAL: VENUE/TIMELINE MISMATCH WITH USER REQUIREMENTS. The user explicitly targets CoRL 2026 (abstract May 26, paper May 29, ≤20 days). The proposal abandons CoRL entirely, targeting Humanoids 2026 (July 24, 75 days) as primary with ICRA 2027 and CoRL 2027 as secondary. The manual timeline (7-8 weeks) and even auto-research timeline (3-4 weeks) exceed the user's 20-day hard constraint. The proposal must either present a CoRL-feasible minimal scope or explicitly justify why CoRL 2026 cannot be met while proposing a concrete alternative the user can accept.", "MISSING COMPETING WORK: RoboGene (arXiv:2602.16444, Feb 2026) generates diverse robot tasks with three LLM-based feasibility evaluators (physical, novelty, constraint adherence), diversity-driven LFU sampling, and self-reflection refinement. It produces 18K trajectories across 900 tasks. While its mechanism differs (LLM-based evaluation vs. learned GNN prediction), it directly addresses the same problem of automated diverse feasibility-aware task generation. The proposal must cite and differentiate: RoboGene uses post-hoc LLM feasibility fixing; CompLocoGen uses learned upfront prediction with compositional structure. RoboGene targets general manipulation; CompLocoGen targets humanoid loco-manipulation with coupled dynamics.", "MISSING COMPETING WORK: FATE (arXiv:2603.01505, March 2026) proposes closed-loop feasibility-aware task generation with active repair using VLM auditors (static + dynamic phases). While FATE targets individual tasks on mobile manipulators (not compositional humanoid tasks), it directly occupies the 'feasibility-aware task generation' space. The TFN's advantage over FATE—learned boundary dynamics vs. VLM-based auditing, compositional structure vs. single tasks—should be articulated.", "MISSING REFERENCE: Ψ₀ (arXiv:2603.12263, March 2026) is a foundation model for universal humanoid loco-manipulation using staged VLM pre-training on human video + robot data fine-tuning. While it's a policy model (not task generation), it represents a key potential downstream consumer of CompLocoGen's generated tasks and should be mentioned to strengthen the impact argument.", "TFN GENERALIZATION CLAIM UNSUBSTANTIATED: The proposal claims the TFN can generalize to novel primitive types (push, open_door, squat) from only 20-30 rollouts per new transition type, arguing that 'primitive-type-agnostic physical features (CoM velocity, contact forces, joint torques)' enable transfer. This is a strong empirical claim with no supporting evidence. While architecturally plausible, it should be framed as a key experimental hypothesis, not a design assumption. If generalization fails, the active learning budget for 7 primitives grows substantially.", "HUMANOIDS 2026 DEADLINE ERROR: The proposal claims 'paper deadline June 30, 2026 — 51 days' but the official Humanoids 2026 website (2026.ieee-humanoids.org) indicates the paper submission deadline is July 24, 2026 (75 days from today). This is favorable (more time) but suggests the deadline wasn't verified against the official source.", "MINOR: Generative Skill Chaining is cited as 'CoRL 2024' but appears to be CoRL 2023 (arXiv:2401.03360 submitted Jan 2024 but the paper was at CoRL 2023). Verify and correct."]
Feedback: The proposal has improved substantially over 5 rounds — the TFN is a genuine novelty contribution and the compute/infrastructure are now realistic. Three targeted changes would bring this to pass quality:

1. **ADDRESS CoRL 2026 OR JUSTIFY ALTERNATIVE**: The user's requirement is CoRL 2026 (20 days). You must either: (a) Present a CoRL-minimal scope: 3 primitives (walk/pick/place), pre-trained SONIC+IK, TFN with bootstrap-only training (no full active learning loop), 3 compositions, single downstream eval, no ablations — essentially demonstrating TFN feasibility prediction works. Use the Humanoids deadline for the full 7-primitive + active learning + ablation paper. OR (b) Make a compelling case that the TFN contribution requires the full evaluation to be convincing and that a stripped-down CoRL submission would be rejected anyway — then commit to Humanoids 2026 (actual deadline July 24 = 75 days, plenty of time).

2. **ADD RoboGene AND FATE TO LANDSCAPE**: Both are 2026 works in automated feasibility-aware task generation. Your differentiation is clear and strong: (a) vs. RoboGene: learned GNN prediction vs. LLM-based evaluation; compositional grammar structure vs. free-form LLM generation; humanoid-specific coupled dynamics vs. general manipulation. (b) vs. FATE: upfront composition-level prediction vs. per-task post-hoc VLM auditing; compositional multi-stage tasks vs. single tasks; humanoid loco-manipulation vs. mobile manipulation. Frame RoboGene as a baseline comparison if possible.

3. **REFRAME TFN GENERALIZATION AS HYPOTHESIS**: Change the 20-30 rollout generalization claim from a design assumption to a key experimental question. State: 'We hypothesize that primitive-type-agnostic physical features enable few-shot transfer; quantifying the number of rollouts needed per novel primitive type IS a key experimental result.' Budget contingency compute (10-20h) in case generalization requires more rollouts than expected.

Minor: Fix Humanoids 2026 deadline to July 24 (more favorable). Verify Generative Skill Chaining venue (CoRL 2023 vs 2024). Add Ψ₀ as a downstream consumer in the impact discussion.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

## 停滞提醒
这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 3.2 到 3.5，没有明显改善。

请认真思考：
- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？
- 如果你认为问题出在 approach 而非 framing，可以做 major revision。
- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。
- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。

最终由你判断——做你认为最能提升 idea 质量的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "db4567a2-a6f4-4fc2-b412-1676cc6316ed",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T19:25:58.370Z_

```json
{
  "parentUuid": "db4567a2-a6f4-4fc2-b412-1676cc6316ed",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "5d647748-4406-4344-80f5-baf5526a874d",
  "timestamp": "2026-05-10T19:25:58.370Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T19:25:58.371Z_

```json
{
  "parentUuid": "5d647748-4406-4344-80f5-baf5526a874d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1fdaf5aa-708a-40b5-bbf5-aa903c35c513",
  "timestamp": "2026-05-10T19:25:58.371Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Co…",
  "leafUuid": "1fdaf5aa-708a-40b5-bbf5-aa903c35c513",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise CoRL 2026 scope or justify Humanoids 2026 timeline",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Assistant

_source line 8 · 2026-05-10T19:26:16.540Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before doing any research. The key issues are:

1. **CRITICAL: Venue/timeline mismatch** - User wants CoRL 2026 (20 days), but proposal targets Humanoids 2026 (75 days). Need to either scope down for CoRL or justify Humanoids.

2. **Missing competing work**: RoboGene (arXiv:2602.16444) and FATE (arXiv:2603.01505) - both in feasibility-aware task generation space.

3. **Missing reference**: Ψ₀ (arXiv:2603.12263) - foundation model for humanoid loco-manipulation.


4. **TFN generalization claim unsubstantiated** - The 20-30 rollouts claim needs to be reframed as a hypothesis rather than established fact.

5. **Humanoids 2026 deadline error** - It's July 24, not June 30.

6. **Minor**: Need to verify the venue for Generative Skill Chaining.

The stagnation pattern across five rounds (scores stuck at 3.2→3.5) is concerning, but the core idea—combining grammar with learned TFN for compositional task generation—is genuinely novel. The question is whether targeted fixes to address the venue mismatch and missing references can break through, or if this needs a more fundamental restructuring.

I'm going to research the missing papers and verify the deadlines to determine whether these are fixable presentation issues or if there's something deeper holding back the score.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fdaf5aa-708a-40b5-bbf5-aa903c35c513",
  "isSidechain": false,
  "requestId": "req_011CauSKDRFXzFjWy2GLTyRj",
  "type": "assistant",
  "uuid": "a6884eeb-176a-41d8-8260-e94c480de62b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163k4Ap6DEbMdvt5GHYWbsi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14536,
      "cache_read_input_tokens": 11664,
      "output_tokens": 523,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14536,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 523,
          "cache_read_input_tokens": 11664,
          "cache_creation_input_tokens": 14536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14536
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T19:26:16.645Z_

I'll research the missing papers and verify deadlines before revising. Let me search for all the flagged items in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6884eeb-176a-41d8-8260-e94c480de62b",
  "isSidechain": false,
  "requestId": "req_011CauSKDRFXzFjWy2GLTyRj",
  "type": "assistant",
  "uuid": "bcfeab33-4991-438a-8d56-89b836461023",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163k4Ap6DEbMdvt5GHYWbsi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14536,
      "cache_read_input_tokens": 11664,
      "output_tokens": 523,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14536,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 523,
          "cache_read_input_tokens": 11664,
          "cache_creation_input_tokens": 14536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14536
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T19:26:16.759Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013a9C9S4HJNZf8ZTpr3ZsUX`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcfeab33-4991-438a-8d56-89b836461023",
  "isSidechain": false,
  "requestId": "req_011CauSKDRFXzFjWy2GLTyRj",
  "type": "assistant",
  "uuid": "24fbb142-262e-441c-b822-e446e0319a2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163k4Ap6DEbMdvt5GHYWbsi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14536,
      "cache_read_input_tokens": 11664,
      "output_tokens": 523,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14536,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 523,
          "cache_read_input_tokens": 11664,
          "cache_creation_input_tokens": 14536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14536
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T19:26:16.765Z_

<details><summary>↩ Tool result · `toolu_013a9C9S4HJNZf8ZTpr3ZsUX`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24fbb142-262e-441c-b822-e446e0319a2a",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "e1396627-c4c3-4943-a886-9ae6d1f74449",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "24fbb142-262e-441c-b822-e446e0319a2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T19:26:20.287Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now search for all the missing papers and verify deadlines in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1396627-c4c3-4943-a886-9ae6d1f74449",
  "isSidechain": false,
  "requestId": "req_011CauSLafDPTDDuRTs8scrK",
  "type": "assistant",
  "uuid": "acdbde11-471d-4053-bba8-94f2891fece4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnzE9JzipkmmCSYXmVUsSE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1543,
      "cache_read_input_tokens": 26200,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 26200,
          "cache_creation_input_tokens": 1543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1543
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T19:26:20.955Z_

Let me research all the flagged items in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acdbde11-471d-4053-bba8-94f2891fece4",
  "isSidechain": false,
  "requestId": "req_011CauSLafDPTDDuRTs8scrK",
  "type": "assistant",
  "uuid": "b470e113-4e79-47ef-8898-5fe3d2034759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnzE9JzipkmmCSYXmVUsSE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1543,
      "cache_read_input_tokens": 26200,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 26200,
          "cache_creation_input_tokens": 1543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1543
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-10T19:26:21.582Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013sW6pmY9n4yLKh9AM5Fjgx`</summary>

```json
{
  "query": "RoboGene arXiv 2602.16444 robot task generation LLM feasibility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b470e113-4e79-47ef-8898-5fe3d2034759",
  "isSidechain": false,
  "requestId": "req_011CauSLafDPTDDuRTs8scrK",
  "type": "assistant",
  "uuid": "0580f3e2-0444-425b-aed4-741db26ad5ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LnzE9JzipkmmCSYXmVUsSE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1543,
      "cache_read_input_tokens": 26200,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 26200,
          "cache_creation_input_tokens": 1543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1543
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T19:26:32.679Z_

<details><summary>↩ Tool result · `toolu_013sW6pmY9n4yLKh9AM5Fjgx`</summary>

```text
Web search results for query: "RoboGene arXiv 2602.16444 robot task generation LLM feasibility"

Links: [{"title":"RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation","url":"https://arxiv.org/html/2602.16444"},{"title":"[2602.16444] RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation","url":"https://arxiv.org/abs/2602.16444"},{"title":"[2602.16444v2] RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation","url":"https://arxiv.org/abs/2602.16444v2"},{"title":"Ro-SLM: Onboard Small Language Models for Robot Task Planning and Operation Code Generation","url":"https://arxiv.org/html/2604.10929"},{"title":"LLM-GROP: Visually Grounded Robot Task and Motion Planning with Large Language Models","url":"https://arxiv.org/html/2511.07727"},{"title":"RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation","url":"https://arxiv.org/html/2311.01455v3"},{"title":"LLM-as-BT-Planner: Leveraging LLMs for Behavior Tree Generation in Robot Task Planning","url":"https://arxiv.org/html/2409.10444"},{"title":"[2409.10444v1] LLM as BT-Planner: Leveraging LLMs for Behavior Tree Generation in Robot Task Planning","url":"https://arxiv.org/abs/2409.10444v1"},{"title":"GitHub - GT-RIPL/Awesome-LLM-Robotics: A comprehensive list of papers using large language/multi-modal models for Robotics/RL, including papers, codes, and related websites · GitHub","url":"https://github.com/GT-RIPL/Awesome-LLM-Robotics"},{"title":"BTGenBot-2: Efficient Behavior Tree Generation with Small Language Models","url":"https://arxiv.org/html/2602.01870"}]

Based on the search results, I found detailed information about RoboGene (arXiv 2602.16444):

## Overview

RoboGene is a novel agentic framework designed for the automated, large-scale generation of diverse, physically grounded, and high-quality robotic manipulation tasks. It is designed to automate the generation of diverse, physically plausible manipulation tasks across single-arm, dual-arm, and mobile robots.

## Problem Addressed

The pursuit of general-purpose robotic manipulation is hindered by the scarcity of diverse, real-world interaction data. Unlike data collection from web in vision or language, robotic data collection is an active process incurring prohibitive physical costs. Consequently, automated task curation to maximize data value remains a critical yet under-explored challenge.

## LLM Feasibility Challenges

The framework specifically addresses critical limitations with using LLMs for robot task generation:

- Current LLMs lack physical grounding and are susceptible to hallucination, frequently yielding tasks that diverge from user constraints or reference non-existent objects. They cannot inherently assess whether a specific robot embodiment possesses the kinematic feasibility to execute a generated instruction.

- The naive application of LLMs to robotics often suffers from grounding failures, where the generator produces tasks that violate physical laws, reference hallucinated assets, or exceed the kinematic constraints of the robot embodiment.

## RoboGene's Solution

RoboGene introduces a closed-loop agentic framework that integrates a diversity-driven sampling mechanism with a self-reflective evaluation loop. This ensures that generated tasks are not only semantically novel but also physically executable and valid, providing a robust and balanced data foundation for pre-training generalist agents.

RoboGene integrates three core components: diversity-driven sampling for broad task coverage, self-reflection mechanisms to enforce physical constraints, and human-in-the-loop refinement for continuous improvement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0580f3e2-0444-425b-aed4-741db26ad5ad",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "f587df4d-7f63-4e88-bdce-fd96d15ccb31",
  "toolUseResult": {
    "query": "RoboGene arXiv 2602.16444 robot task generation LLM feasibility",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DwSY6NftrpVwLyWEzENFcn",
        "content": [
          {
            "title": "RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation",
            "url": "https://arxiv.org/html/2602.16444"
          },
          {
            "title": "[2602.16444] RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation",
            "url": "https://arxiv.org/abs/2602.16444"
          },
          {
            "title": "[2602.16444v2] RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation",
            "url": "https://arxiv.org/abs/2602.16444v2"
          },
          {
            "title": "Ro-SLM: Onboard Small Language Models for Robot Task Planning and Operation Code Generation",
            "url": "https://arxiv.org/html/2604.10929"
          },
          {
            "title": "LLM-GROP: Visually Grounded Robot Task and Motion Planning with Large Language Models",
            "url": "https://arxiv.org/html/2511.07727"
          },
          {
            "title": "RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation",
            "url": "https://arxiv.org/html/2311.01455v3"
          },
          {
            "title": "LLM-as-BT-Planner: Leveraging LLMs for Behavior Tree Generation in Robot Task Planning",
            "url": "https://arxiv.org/html/2409.10444"
          },
          {
            "title": "[2409.10444v1] LLM as BT-Planner: Leveraging LLMs for Behavior Tree Generation in Robot Task Planning",
            "url": "https://arxiv.org/abs/2409.10444v1"
          },
          {
            "title": "GitHub - GT-RIPL/Awesome-LLM-Robotics: A comprehensive list of papers using large language/multi-modal models for Robotics/RL, including papers, codes, and related websites · GitHub",
            "url": "https://github.com/GT-RIPL/Awesome-LLM-Robotics"
          },
          {
            "title": "BTGenBot-2: Efficient Behavior Tree Generation with Small Language Models",
            "url": "https://arxiv.org/html/2602.01870"
          }
        ]
      },
      "Based on the search results, I found detailed information about RoboGene (arXiv 2602.16444):\n\n## Overview\n\nRoboGene is a novel agentic framework designed for the automated, large-scale generation of diverse, physically grounded, and high-quality robotic manipulation tasks. It is designed to automate the generation of diverse, physically plausible manipulation tasks across single-arm, dual-arm, and mobile robots.\n\n## Problem Addressed\n\nThe pursuit of general-purpose robotic manipulation is hindered by the scarcity of diverse, real-world interaction data. Unlike data collection from web in vision or language, robotic data collection is an active process incurring prohibitive physical costs. Consequently, automated task curation to maximize data value remains a critical yet under-explored challenge.\n\n## LLM Feasibility Challenges\n\nThe framework specifically addresses critical limitations with using LLMs for robot task generation:\n\n- Current LLMs lack physical grounding and are susceptible to hallucination, frequently yielding tasks that diverge from user constraints or reference non-existent objects. They cannot inherently assess whether a specific robot embodiment possesses the kinematic feasibility to execute a generated instruction.\n\n- The naive application of LLMs to robotics often suffers from grounding failures, where the generator produces tasks that violate physical laws, reference hallucinated assets, or exceed the kinematic constraints of the robot embodiment.\n\n## RoboGene's Solution\n\nRoboGene introduces a closed-loop agentic framework that integrates a diversity-driven sampling mechanism with a self-reflective evaluation loop. This ensures that generated tasks are not only semantically novel but also physically executable and valid, providing a robust and balanced data foundation for pre-training generalist agents.\n\nRoboGene integrates three core components: diversity-driven sampling for broad task coverage, self-reflection mechanisms to enforce physical constraints, and human-in-the-loop refinement for continuous improvement."
    ],
    "durationSeconds": 11.092868952
  },
  "sourceToolAssistantUUID": "0580f3e2-0444-425b-aed4-741db26ad5ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-10T19:26:35.380Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018bzZ2n22mVPz8jCFkBeRxU`</summary>

```json
{
  "query": "FATE arXiv 2603.01505 feasibility-aware task generation VLM active repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f587df4d-7f63-4e88-bdce-fd96d15ccb31",
  "isSidechain": false,
  "requestId": "req_011CauSMjixEQNage4NRhwp4",
  "type": "assistant",
  "uuid": "71c3e8da-379d-4f5c-861e-aae058110342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTzwDNZpSgEiEdo2Lr8tVa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1151,
      "cache_read_input_tokens": 27743,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 27743,
          "cache_creation_input_tokens": 1151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1151
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T19:26:50.059Z_

<details><summary>↩ Tool result · `toolu_018bzZ2n22mVPz8jCFkBeRxU`</summary>

```text
Web search results for query: "FATE arXiv 2603.01505 feasibility-aware task generation VLM active repair"

Links: [{"title":"FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula","url":"https://arxiv.org/html/2603.01505"},{"title":"[2603.01505] FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula","url":"https://arxiv.org/abs/2603.01505"},{"title":"Multimodal Behavior Tree Generation: A Small Vision-Language Model for Robot Task Planning","url":"https://arxiv.org/html/2603.06084"},{"title":"Spatially Grounded Long-Horizon Task Planning in the Wild","url":"https://arxiv.org/html/2603.13433"},{"title":"VLM-driven Behavior Tree for Context-aware Task Planning","url":"https://arxiv.org/html/2501.03968v1"},{"title":"A Semantic Observer Layer for Autonomous Vehicles: Pre-Deployment Feasibility Study of VLMs for Low-Latency Anomaly Detection","url":"https://arxiv.org/html/2603.28888"},{"title":"ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation","url":"https://arxiv.org/html/2603.15169v1"},{"title":"ThermoAct: Thermal-Aware Vision-Language-Action Models for Robotic Perception and Decision-Making","url":"https://arxiv.org/html/2603.25044v1"},{"title":"AntiGrounding: Lifting Robotic Actions into VLM Representation Space for Decision Making","url":"https://arxiv.org/html/2506.12374v1"},{"title":"REMAC: Self-Reflective and Self-Evolving Multi-Agent Collaboration for Long-Horizon Robot Manipulation","url":"https://arxiv.org/html/2503.22122"}]

Based on the search results, I found the paper you're looking for:

**FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair** is a framework that reimagines task generation as an iterative validation-and-refinement process.

## Overview

Recent breakthroughs in generative simulation have harnessed Large Language Models (LLMs) to generate diverse robotic task curricula, yet these open-loop paradigms frequently produce linguistically coherent but physically infeasible goals—stemming from ungrounded task specifications or misaligned objective formulations.

## Key Innovation

Unlike conventional methods that decouple generation and verification into discrete stages, FATE embeds a generalist embodied agent directly into the generation loop to proactively guarantee the physical groundedness of the resulting curriculum.

## Training Approach

The framework leverages a curated hybrid dataset of approximately 145,000 samples, with the data distribution explicitly engineered to address the action gap often observed in generalist VLMs, balancing three critical cognitive axes: Embodied Action, Spatial Perception, and Reasoning.

## Paper Details

The paper was submitted to arXiv on March 2, 2026 (arXiv:2603.01505) and is authored by Bingchuan Wei, Bingqi Huang, Jingheng Ma, Zeyu Zhang, and Sen Cui.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71c3e8da-379d-4f5c-861e-aae058110342",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "11a5f909-95b5-4855-8bc8-14afbb0d0b58",
  "toolUseResult": {
    "query": "FATE arXiv 2603.01505 feasibility-aware task generation VLM active repair",
    "results": [
      {
        "tool_use_id": "srvtoolu_012aVbT4QajNQ2Q6q8kgwSNA",
        "content": [
          {
            "title": "FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula",
            "url": "https://arxiv.org/html/2603.01505"
          },
          {
            "title": "[2603.01505] FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula",
            "url": "https://arxiv.org/abs/2603.01505"
          },
          {
            "title": "Multimodal Behavior Tree Generation: A Small Vision-Language Model for Robot Task Planning",
            "url": "https://arxiv.org/html/2603.06084"
          },
          {
            "title": "Spatially Grounded Long-Horizon Task Planning in the Wild",
            "url": "https://arxiv.org/html/2603.13433"
          },
          {
            "title": "VLM-driven Behavior Tree for Context-aware Task Planning",
            "url": "https://arxiv.org/html/2501.03968v1"
          },
          {
            "title": "A Semantic Observer Layer for Autonomous Vehicles: Pre-Deployment Feasibility Study of VLMs for Low-Latency Anomaly Detection",
            "url": "https://arxiv.org/html/2603.28888"
          },
          {
            "title": "ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation",
            "url": "https://arxiv.org/html/2603.15169v1"
          },
          {
            "title": "ThermoAct: Thermal-Aware Vision-Language-Action Models for Robotic Perception and Decision-Making",
            "url": "https://arxiv.org/html/2603.25044v1"
          },
          {
            "title": "AntiGrounding: Lifting Robotic Actions into VLM Representation Space for Decision Making",
            "url": "https://arxiv.org/html/2506.12374v1"
          },
          {
            "title": "REMAC: Self-Reflective and Self-Evolving Multi-Agent Collaboration for Long-Horizon Robot Manipulation",
            "url": "https://arxiv.org/html/2503.22122"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair** is a framework that reimagines task generation as an iterative validation-and-refinement process.\n\n## Overview\n\nRecent breakthroughs in generative simulation have harnessed Large Language Models (LLMs) to generate diverse robotic task curricula, yet these open-loop paradigms frequently produce linguistically coherent but physically infeasible goals—stemming from ungrounded task specifications or misaligned objective formulations.\n\n## Key Innovation\n\nUnlike conventional methods that decouple generation and verification into discrete stages, FATE embeds a generalist embodied agent directly into the generation loop to proactively guarantee the physical groundedness of the resulting curriculum.\n\n## Training Approach\n\nThe framework leverages a curated hybrid dataset of approximately 145,000 samples, with the data distribution explicitly engineered to address the action gap often observed in generalist VLMs, balancing three critical cognitive axes: Embodied Action, Spatial Perception, and Reasoning.\n\n## Paper Details\n\nThe paper was submitted to arXiv on March 2, 2026 (arXiv:2603.01505) and is authored by Bingchuan Wei, Bingqi Huang, Jingheng Ma, Zeyu Zhang, and Sen Cui."
    ],
    "durationSeconds": 14.675224725
  },
  "sourceToolAssistantUUID": "71c3e8da-379d-4f5c-861e-aae058110342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T19:26:53.039Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ALeqAbueP19g5ZMKjQfM5V`</summary>

```json
{
  "query": "Psi0 arXiv 2603.12263 foundation model humanoid loco-manipulation VLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11a5f909-95b5-4855-8bc8-14afbb0d0b58",
  "isSidechain": false,
  "requestId": "req_011CauSP21WuaPaqK4gfgSrD",
  "type": "assistant",
  "uuid": "49a060ba-8d4b-4dc6-a88d-39f71f2ef4a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ff5vXyuQp3bot2TPD6QqhM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 922,
      "cache_read_input_tokens": 28894,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 922,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 28894,
          "cache_creation_input_tokens": 922,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 922
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T19:26:59.620Z_

<details><summary>↩ Tool result · `toolu_01ALeqAbueP19g5ZMKjQfM5V`</summary>

```text
Web search results for query: "Psi0 arXiv 2603.12263 foundation model humanoid loco-manipulation VLM"

Links: [{"title":"[2603.12263] $Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2603.12263"},{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2603.12263v1"},{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://psi-lab.ai/Psi0/"},{"title":"$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.12263"},{"title":"GitHub - physical-superintelligence-lab/Psi0: [RSS26'] Welcome to Psi-Zero, a Humanoid VLA towards Universal Humanoid Intelligence. · GitHub","url":"https://github.com/physical-superintelligence-lab/Psi0"},{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation - Hongyi Jing","url":"https://hongyijing.me/publications/psi-0/"},{"title":"最新开源！全身运动操作的VLA基础模型，wholebody任务今年的风向标～_机器人_数据_动作","url":"https://www.sohu.com/a/997275103_115479"},{"title":"Ψ0: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (Mar 2026) - YouTube","url":"https://www.youtube.com/watch?v=sf31pDnScf8"},{"title":"$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://www.wispaper.ai/en/blog/psi-zero-open-foundation-model-universal-humanoid-loco-manipulation-20260314/eng"},{"title":"MetaWorld-X: Hierarchical World Modeling via VLM-Orchestrated Experts for Humanoid Loco-Manipulation","url":"https://arxiv.org/html/2603.08572"}]

Based on the search results, I found comprehensive information about this paper. Here's what I found:

Ψ₀ (Psi-Zero) is an open foundation model to address challenging humanoid loco-manipulation tasks. Existing approaches attempt to address this fundamental problem by co-training on large and diverse human and humanoid data, but this strategy is suboptimal due to the fundamental kinematic and motion disparities between humans and humanoid robots.

**Key Approach:**

The model proposes a staged training paradigm where it first autoregressively pre-trains a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations, then post-trains a flow-based action expert on high-quality humanoid robot data to learn precise robot joint control.

**Architecture:**

Ψ₀ adopts a triple-system architecture with two end-to-end-trained components: a vision-language backbone (system-2) and a multi-modal diffusion transformer (MM-DiT) action expert (system-1). The vision-language foundation model used is Qwen3-VL-2B-Instruct as system-2, and the action expert is implemented as a flow-based MM-DiT containing approximately 500M parameters.

**Performance:**

The model achieves an average overall success rate that is at least 40% higher than that of the second-best baseline, GR00T-N1.6, which is the most recently released humanoid foundation model.

The paper was published on arXiv on March 12, 2026, with code available on GitHub through the Physical Superintelligence Lab.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49a060ba-8d4b-4dc6-a88d-39f71f2ef4a2",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "3a498c69-15de-4be1-9fd7-478de4ca869a",
  "toolUseResult": {
    "query": "Psi0 arXiv 2603.12263 foundation model humanoid loco-manipulation VLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_019iRDdGJyd1XmXusFz1o9m4",
        "content": [
          {
            "title": "[2603.12263] $Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation",
            "url": "https://arxiv.org/abs/2603.12263"
          },
          {
            "title": "Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation",
            "url": "https://arxiv.org/html/2603.12263v1"
          },
          {
            "title": "Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation",
            "url": "https://psi-lab.ai/Psi0/"
          },
          {
            "title": "$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2603.12263"
          },
          {
            "title": "GitHub - physical-superintelligence-lab/Psi0: [RSS26'] Welcome to Psi-Zero, a Humanoid VLA towards Universal Humanoid Intelligence. · GitHub",
            "url": "https://github.com/physical-superintelligence-lab/Psi0"
          },
          {
            "title": "Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation - Hongyi Jing",
            "url": "https://hongyijing.me/publications/psi-0/"
          },
          {
            "title": "最新开源！全身运动操作的VLA基础模型，wholebody任务今年的风向标～_机器人_数据_动作",
            "url": "https://www.sohu.com/a/997275103_115479"
          },
          {
            "title": "Ψ0: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (Mar 2026) - YouTube",
            "url": "https://www.youtube.com/watch?v=sf31pDnScf8"
          },
          {
            "title": "$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation",
            "url": "https://www.wispaper.ai/en/blog/psi-zero-open-foundation-model-universal-humanoid-loco-manipulation-20260314/eng"
          },
          {
            "title": "MetaWorld-X: Hierarchical World Modeling via VLM-Orchestrated Experts for Humanoid Loco-Manipulation",
            "url": "https://arxiv.org/html/2603.08572"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about this paper. Here's what I found:\n\nΨ₀ (Psi-Zero) is an open foundation model to address challenging humanoid loco-manipulation tasks. Existing approaches attempt to address this fundamental problem by co-training on large and diverse human and humanoid data, but this strategy is suboptimal due to the fundamental kinematic and motion disparities between humans and humanoid robots.\n\n**Key Approach:**\n\nThe model proposes a staged training paradigm where it first autoregressively pre-trains a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations, then post-trains a flow-based action expert on high-quality humanoid robot data to learn precise robot joint control.\n\n**Architecture:**\n\nΨ₀ adopts a triple-system architecture with two end-to-end-trained components: a vision-language backbone (system-2) and a multi-modal diffusion transformer (MM-DiT) action expert (system-1). The vision-language foundation model used is Qwen3-VL-2B-Instruct as system-2, and the action expert is implemented as a flow-based MM-DiT containing approximately 500M parameters.\n\n**Performance:**\n\nThe model achieves an average overall success rate that is at least 40% higher than that of the second-best baseline, GR00T-N1.6, which is the most recently released humanoid foundation model.\n\nThe paper was published on arXiv on March 12, 2026, with code available on GitHub through the Physical Superintelligence Lab."
    ],
    "durationSeconds": 6.577008936999999
  },
  "sourceToolAssistantUUID": "49a060ba-8d4b-4dc6-a88d-39f71f2ef4a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Co…",
  "leafUuid": "3a498c69-15de-4be1-9fd7-478de4ca869a",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise CoRL 2026 scope or justify Humanoids 2026 timeline",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Tool call

_source line 22 · 2026-05-10T19:27:02.158Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Mxq59i7gP3ykj9nSRJewU`</summary>

```json
{
  "query": "CoRL 2026 submission deadline conference dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a498c69-15de-4be1-9fd7-478de4ca869a",
  "isSidechain": false,
  "requestId": "req_011CauSPiwNxjNXQkVSP7sa9",
  "type": "assistant",
  "uuid": "c685da48-c490-4813-a273-4b56445583ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fgcQqAn9Br7fAuKTUrHTj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 29816,
      "output_tokens": 61,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1082,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 61,
          "cache_read_input_tokens": 29816,
          "cache_creation_input_tokens": 1082,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1082
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T19:27:07.627Z_

<details><summary>↩ Tool result · `toolu_018Mxq59i7gP3ykj9nSRJewU`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline conference dates"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz","url":"https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"},{"title":"Vincent Vanhoucke's Post","url":"https://www.linkedin.com/posts/vanhoucke_corl-2026-website-is-officially-live-at-http-activity-7432112475480817664-gBos"}]

Based on the search results, here is the information for CoRL 2026:

**Submission Deadlines:**
- Abstract submission deadline: May 26, 2026 11:59 UTC
- Paper submission deadline: May 29, 2026 11:59 UTC

**Conference Dates:**
- November 9-12, 2026

**Location:**
- JW Marriott Austin, 110 E 2nd St, Austin, TX 78701

**Additional Details:**
- Workshops on Nov 9, main conference Nov 10-12


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c685da48-c490-4813-a273-4b56445583ed",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "550ce8d0-8a39-4794-8633-e0e233ca578c",
  "toolUseResult": {
    "query": "CoRL 2026 submission deadline conference dates",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BvN2gP7sah6vzcn6WXhiGX",
        "content": [
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf?lang=en"
          },
          {
            "title": "CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz",
            "url": "https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"
          },
          {
            "title": "Vincent Vanhoucke's Post",
            "url": "https://www.linkedin.com/posts/vanhoucke_corl-2026-website-is-officially-live-at-http-activity-7432112475480817664-gBos"
          }
        ]
      },
      "Based on the search results, here is the information for CoRL 2026:\n\n**Submission Deadlines:**\n- Abstract submission deadline: May 26, 2026 11:59 UTC\n- Paper submission deadline: May 29, 2026 11:59 UTC\n\n**Conference Dates:**\n- November 9-12, 2026\n\n**Location:**\n- JW Marriott Austin, 110 E 2nd St, Austin, TX 78701\n\n**Additional Details:**\n- Workshops on Nov 9, main conference Nov 10-12"
    ],
    "durationSeconds": 5.464899083000004
  },
  "sourceToolAssistantUUID": "c685da48-c490-4813-a273-4b56445583ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-10T19:27:10.509Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X5BDxXWsn9MJpPoHn3X2Bh`</summary>

```json
{
  "query": "Humanoids 2026 IEEE paper submission deadline July 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "550ce8d0-8a39-4794-8633-e0e233ca578c",
  "isSidechain": false,
  "requestId": "req_011CauSQKARFv5epDQ5q6n2U",
  "type": "assistant",
  "uuid": "0f67ba27-562d-46a3-b48d-4c2629224046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ST2DKjmP6XzWXg95dYgeFY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 30898,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 30898,
          "cache_creation_input_tokens": 671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 671
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T19:27:13.734Z_

<details><summary>↩ Tool result · `toolu_01X5BDxXWsn9MJpPoHn3X2Bh`</summary>

```text
Web search results for query: "Humanoids 2026 IEEE paper submission deadline July 2026"

Links: [{"title":"Humanoids 2026 - 2026 IEEE-RAS 25th International Conference on Humanoid Robots (Humanoids)","url":"https://2026.ieee-humanoids.org/"},{"title":"Humanoids: IEEE-RAS International Conference on Humanoid Robots 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1239"},{"title":"Humanoids 2026","url":"http://www.humanoids.global/"},{"title":"RA-L - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/publications/ra-l/"},{"title":"Humanoids 2025","url":"https://2025humanoids.org/"},{"title":"Catalog","url":"https://www.ieee.org/membership-catalog/productdetail/showProductDetailPage.html?product=CMYRAS027"},{"title":"25th IEEE-RAS International Conference on Humanoid Robotics — StartupEvents.org","url":"https://startupevents.org/startup-events-calendar/25th-ieee-ras-international-conference-on-humanoid-robotics"},{"title":"IEEE-RAS Humanoids 2026 (San Jose CA) - IEEE-RAS 25th International Conference on Humanoid Robots (Humanoids) -- showsbee.com","url":"https://www.showsbee.com/fairs/IEEE-Humanoids.html"},{"title":"Humanoids 2026 - 2026 IEEE-RAS 25th International Conference on Humanoid Robots (Humanoids) - Workshops - Humanoid Hub","url":"https://www.humanoidhub.ai/workshops/humanoids-2026-2026-ieee-ras-25th-international-conference-on-humanoid-robots-humanoids-000000"},{"title":"IEEE-RAS International Conference on Humanoid Robots (Humanoids 2026), 01 Sep - 31 Dec, 2026 | Conference Locate (Clocate)","url":"https://www.clocate.com/ieee-ras-international-conference-on-humanoid-robots-humanoids/15664/"}]

Based on the search results, I found information about Humanoids 2026:

The 25th IEEE-RAS International Conference on Humanoid Robots will take place December 6–9, 2026, in Santa Clara, CA, USA. 

Regarding the paper submission deadline, the submission period for Humanoids 2026 runs from October 1, 2025 to June 30, 2026. This means the deadline is June 30, 2026, not July 2026 as mentioned in your query.

The official Humanoids 2026 website is at 2026.ieee-humanoids.org where you can submit papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f67ba27-562d-46a3-b48d-4c2629224046",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "fb3ee818-2440-451e-897e-337c21d0064d",
  "toolUseResult": {
    "query": "Humanoids 2026 IEEE paper submission deadline July 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U4RdaHHSr25RyXQADckge8",
        "content": [
          {
            "title": "Humanoids 2026 - 2026 IEEE-RAS 25th International Conference on Humanoid Robots (Humanoids)",
            "url": "https://2026.ieee-humanoids.org/"
          },
          {
            "title": "Humanoids: IEEE-RAS International Conference on Humanoid Robots 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=1239"
          },
          {
            "title": "Humanoids 2026",
            "url": "http://www.humanoids.global/"
          },
          {
            "title": "RA-L - IEEE Robotics and Automation Society Website",
            "url": "https://www.ieee-ras.org/publications/ra-l/"
          },
          {
            "title": "Humanoids 2025",
            "url": "https://2025humanoids.org/"
          },
          {
            "title": "Catalog",
            "url": "https://www.ieee.org/membership-catalog/productdetail/showProductDetailPage.html?product=CMYRAS027"
          },
          {
            "title": "25th IEEE-RAS International Conference on Humanoid Robotics — StartupEvents.org",
            "url": "https://startupevents.org/startup-events-calendar/25th-ieee-ras-international-conference-on-humanoid-robotics"
          },
          {
            "title": "IEEE-RAS Humanoids 2026 (San Jose CA) - IEEE-RAS 25th International Conference on Humanoid Robots (Humanoids) -- showsbee.com",
            "url": "https://www.showsbee.com/fairs/IEEE-Humanoids.html"
          },
          {
            "title": "Humanoids 2026 - 2026 IEEE-RAS 25th International Conference on Humanoid Robots (Humanoids) - Workshops - Humanoid Hub",
            "url": "https://www.humanoidhub.ai/workshops/humanoids-2026-2026-ieee-ras-25th-international-conference-on-humanoid-robots-humanoids-000000"
          },
          {
            "title": "IEEE-RAS International Conference on Humanoid Robots (Humanoids 2026), 01 Sep - 31 Dec, 2026 | Conference Locate (Clocate)",
            "url": "https://www.clocate.com/ieee-ras-international-conference-on-humanoid-robots-humanoids/15664/"
          }
        ]
      },
      "Based on the search results, I found information about Humanoids 2026:\n\nThe 25th IEEE-RAS International Conference on Humanoid Robots will take place December 6–9, 2026, in Santa Clara, CA, USA. \n\nRegarding the paper submission deadline, the submission period for Humanoids 2026 runs from October 1, 2025 to June 30, 2026. This means the deadline is June 30, 2026, not July 2026 as mentioned in your query.\n\nThe official Humanoids 2026 website is at 2026.ieee-humanoids.org where you can submit papers."
    ],
    "durationSeconds": 3.222174291999996
  },
  "sourceToolAssistantUUID": "0f67ba27-562d-46a3-b48d-4c2629224046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-10T19:27:20.372Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D3A8n3gJzSBqmKjq9hnVAz`</summary>

```json
{
  "url": "https://2026.ieee-humanoids.org/",
  "prompt": "What are the exact paper submission deadlines? Include any dates for abstract deadline, paper deadline, notification, camera-ready. Look for any mention of July 24 or June 30 or other specific dates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb3ee818-2440-451e-897e-337c21d0064d",
  "isSidechain": false,
  "requestId": "req_011CauSQmH3xT4W1tm4vhnYB",
  "type": "assistant",
  "uuid": "d25762a5-5faf-4d7f-baa5-ba4086447fb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdQmkVA7w9v8SHvoXegSo4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 31569,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 123,
          "cache_read_input_tokens": 31569,
          "cache_creation_input_tokens": 810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 810
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T19:27:23.820Z_

<details><summary>↩ Tool result · `toolu_01D3A8n3gJzSBqmKjq9hnVAz`</summary>

```text
# Humanoids 2026 Paper Submission Timeline

Based on the conference website, here are the key deadlines:

**Paper Submission:** "July 24, 2026" is the primary deadline for submitting manuscripts.

**Supporting Materials:** Authors may also submit "Supplementary video deadline (optional)" by July 27, 2026.

**Acceptance Notification:** The conference will communicate decisions on October 6, 2026.

**Final Version:** Accepted authors must submit their "Camera-ready paper deadline" by October 26, 2026.

The page does not mention an abstract-only deadline or a June 30 date. The July 24 deadline appears to be for complete papers, not preliminary abstracts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d25762a5-5faf-4d7f-baa5-ba4086447fb3",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "90353164-7729-488a-a40d-9d2b6a85fb2f",
  "toolUseResult": {
    "bytes": 196259,
    "code": 200,
    "codeText": "OK",
    "result": "# Humanoids 2026 Paper Submission Timeline\n\nBased on the conference website, here are the key deadlines:\n\n**Paper Submission:** \"July 24, 2026\" is the primary deadline for submitting manuscripts.\n\n**Supporting Materials:** Authors may also submit \"Supplementary video deadline (optional)\" by July 27, 2026.\n\n**Acceptance Notification:** The conference will communicate decisions on October 6, 2026.\n\n**Final Version:** Accepted authors must submit their \"Camera-ready paper deadline\" by October 26, 2026.\n\nThe page does not mention an abstract-only deadline or a June 30 date. The July 24 deadline appears to be for complete papers, not preliminary abstracts.",
    "durationMs": 3444,
    "url": "https://2026.ieee-humanoids.org/"
  },
  "sourceToolAssistantUUID": "d25762a5-5faf-4d7f-baa5-ba4086447fb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-10T19:27:28.777Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JxPjAoapYpcyV3jM4qo3si`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.16444",
  "prompt": "Extract the full abstract, list of authors, submission date, and any venue information for RoboGene. What are the key methods: how many tasks generated, what feasibility evaluators are used, what robots are supported, what is the LFU sampling mechanism?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90353164-7729-488a-a40d-9d2b6a85fb2f",
  "isSidechain": false,
  "requestId": "req_011CauSRWQsL5YYyYZxiujr1",
  "type": "assistant",
  "uuid": "94c4022b-12ac-4938-9f32-6eddd85e03e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122gJma8ZSDWrCKJvMA2kb6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 32379,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 295,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 138,
          "cache_read_input_tokens": 32379,
          "cache_creation_input_tokens": 295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 295
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T19:27:34.734Z_

<details><summary>↩ Tool result · `toolu_01JxPjAoapYpcyV3jM4qo3si`</summary>

```text
# RoboGene Paper Summary

## Abstract
The paper addresses robotic data scarcity by introducing an automated framework. Key claim: "RoboGene significantly outperforms state-of-the-art foundation models (e.g., GPT-4o, Gemini 2.5 Pro)" in task generation for robot pre-training.

## Authors
Yixue Zhang, Kun Wu, Zhi Gao, Zhen Zhao, Pei Ren, Zhiyuan Xu, Fei Liao, Xinhua Wang, Shichao Fan, Di Wu, Qiuxuan Feng, Meng Li, Zhengping Che, Chang Liu, and Jian Tang (15 authors total).

## Submission Details
- **Submitted:** February 18, 2026 (v1)
- **Last revised:** February 19, 2026 (v2)
- **arXiv identifier:** 2602.16444
- **Subjects:** Robotics (cs.RO), Artificial Intelligence (cs.AI), Machine Learning (cs.LG)
- **Venue:** Not specified in content

## Key Methods & Specifications

**Dataset scale:** The framework collected "datasets of 18k trajectories" during evaluation.

**Supported robots:** The system operates across "single-arm, dual-arm, and mobile robots."

**Core components:** The framework integrates "diversity-driven sampling for broad task coverage, self-reflection mechanisms to enforce physical constraints, and human-in-the-loop refinement."

**Feasibility evaluation approach:** The document mentions self-reflection mechanisms but doesn't detail specific feasibility evaluators or the "LFU sampling mechanism" you referenced—these details appear absent from the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94c4022b-12ac-4938-9f32-6eddd85e03e4",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "82b073bb-53b8-4c85-bf81-19cf26a4085b",
  "toolUseResult": {
    "bytes": 49401,
    "code": 200,
    "codeText": "OK",
    "result": "# RoboGene Paper Summary\n\n## Abstract\nThe paper addresses robotic data scarcity by introducing an automated framework. Key claim: \"RoboGene significantly outperforms state-of-the-art foundation models (e.g., GPT-4o, Gemini 2.5 Pro)\" in task generation for robot pre-training.\n\n## Authors\nYixue Zhang, Kun Wu, Zhi Gao, Zhen Zhao, Pei Ren, Zhiyuan Xu, Fei Liao, Xinhua Wang, Shichao Fan, Di Wu, Qiuxuan Feng, Meng Li, Zhengping Che, Chang Liu, and Jian Tang (15 authors total).\n\n## Submission Details\n- **Submitted:** February 18, 2026 (v1)\n- **Last revised:** February 19, 2026 (v2)\n- **arXiv identifier:** 2602.16444\n- **Subjects:** Robotics (cs.RO), Artificial Intelligence (cs.AI), Machine Learning (cs.LG)\n- **Venue:** Not specified in content\n\n## Key Methods & Specifications\n\n**Dataset scale:** The framework collected \"datasets of 18k trajectories\" during evaluation.\n\n**Supported robots:** The system operates across \"single-arm, dual-arm, and mobile robots.\"\n\n**Core components:** The framework integrates \"diversity-driven sampling for broad task coverage, self-reflection mechanisms to enforce physical constraints, and human-in-the-loop refinement.\"\n\n**Feasibility evaluation approach:** The document mentions self-reflection mechanisms but doesn't detail specific feasibility evaluators or the \"LFU sampling mechanism\" you referenced—these details appear absent from the provided content.",
    "durationMs": 5953,
    "url": "https://arxiv.org/abs/2602.16444"
  },
  "sourceToolAssistantUUID": "94c4022b-12ac-4938-9f32-6eddd85e03e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-10T19:27:34.739Z_

```json
{
  "parentUuid": "82b073bb-53b8-4c85-bf81-19cf26a4085b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a6dcdd47-25f1-47c8-a982-4daf3cfae1df",
  "timestamp": "2026-05-10T19:27:34.739Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-10T19:27:38.037Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U4RZ9dWeRHJaHuKXRrvtQC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.01505",
  "prompt": "Extract the full abstract, authors, submission date, and venue for FATE. What are the key methods: static vs dynamic feasibility phases, how does VLM auditing work, what tasks/robots does it target, how many tasks generated, what are the main results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6dcdd47-25f1-47c8-a982-4daf3cfae1df",
  "isSidechain": false,
  "requestId": "req_011CauSSK32r4q4AMzo3f1AG",
  "type": "assistant",
  "uuid": "6d2984ed-17e8-4770-8141-e55b0a760b01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mt2WdGBMXSiU6HvMnmMVCe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 657,
      "cache_read_input_tokens": 32674,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 32674,
          "cache_creation_input_tokens": 657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 657
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T19:27:44.741Z_

<details><summary>↩ Tool result · `toolu_01U4RZ9dWeRHJaHuKXRrvtQC`</summary>

```text
# FATE Paper Summary

**Full Abstract:**
"Recent breakthroughs in generative simulation have harnessed Large Language Models (LLMs) to generate diverse robotic task curricula, yet these open-loop paradigms frequently produce linguistically coherent but physically infeasible goals, stemming from ungrounded task specifications or misaligned objective formulations. To address this critical limitation, we propose FATE (Feasibility-Aware Task gEneration), a closed-loop, self-correcting framework that reimagines task generation as an iterative validation-and-refinement process. Unlike conventional methods that decouple generation and verification into discrete stages, FATE embeds a generalist embodied agent directly into the generation loop to proactively guarantee the physical groundedness of the resulting curriculum. FATE instantiates a sequential auditing pipeline: it first validates static scene attributes (e.g., object affordances, layout compatibility) and subsequently verifies execution feasibility via simulated embodied interaction. Critical to its performance, upon detecting an infeasible task, FATE deploys an active repair module that autonomously adapts scene configurations or policy specifications, converting unworkable proposals into physically valid task instances. Extensive experiments validate that FATE generates semantically diverse, physically grounded task curricula while achieving a substantial reduction in execution failure rates relative to state-of-the-art generative baselines."

**Authors:** Bingchuan Wei, Bingqi Huang, Jingheng Ma, Zeyu Zhang, Sen Cui

**Submission Date:** March 2, 2026

**Venue:** arXiv Computer Science > Robotics (cs.RO)

**Key Methods:**
- **Two-phase validation:** Static scene attribute checking followed by dynamic execution feasibility verification through embodied interaction simulation
- **Active repair mechanism:** Autonomous adaptation of scene or policy configurations when infeasible tasks are detected
- **Embodied agent integration:** Direct embedding of a generalist agent within the generation loop rather than separate verification stages

**Tasks/Robots/Scale:** The abstract does not specify particular robot platforms, task domains, or the number of tasks generated.

**Main Results:** Substantial reduction in execution failure rates compared to baseline generative approaches while maintaining semantic diversity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d2984ed-17e8-4770-8141-e55b0a760b01",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "8608df80-c9b5-45d4-a9cc-ab64dd6e253a",
  "toolUseResult": {
    "bytes": 47404,
    "code": 200,
    "codeText": "OK",
    "result": "# FATE Paper Summary\n\n**Full Abstract:**\n\"Recent breakthroughs in generative simulation have harnessed Large Language Models (LLMs) to generate diverse robotic task curricula, yet these open-loop paradigms frequently produce linguistically coherent but physically infeasible goals, stemming from ungrounded task specifications or misaligned objective formulations. To address this critical limitation, we propose FATE (Feasibility-Aware Task gEneration), a closed-loop, self-correcting framework that reimagines task generation as an iterative validation-and-refinement process. Unlike conventional methods that decouple generation and verification into discrete stages, FATE embeds a generalist embodied agent directly into the generation loop to proactively guarantee the physical groundedness of the resulting curriculum. FATE instantiates a sequential auditing pipeline: it first validates static scene attributes (e.g., object affordances, layout compatibility) and subsequently verifies execution feasibility via simulated embodied interaction. Critical to its performance, upon detecting an infeasible task, FATE deploys an active repair module that autonomously adapts scene configurations or policy specifications, converting unworkable proposals into physically valid task instances. Extensive experiments validate that FATE generates semantically diverse, physically grounded task curricula while achieving a substantial reduction in execution failure rates relative to state-of-the-art generative baselines.\"\n\n**Authors:** Bingchuan Wei, Bingqi Huang, Jingheng Ma, Zeyu Zhang, Sen Cui\n\n**Submission Date:** March 2, 2026\n\n**Venue:** arXiv Computer Science > Robotics (cs.RO)\n\n**Key Methods:**\n- **Two-phase validation:** Static scene attribute checking followed by dynamic execution feasibility verification through embodied interaction simulation\n- **Active repair mechanism:** Autonomous adaptation of scene or policy configurations when infeasible tasks are detected\n- **Embodied agent integration:** Direct embedding of a generalist agent within the generation loop rather than separate verification stages\n\n**Tasks/Robots/Scale:** The abstract does not specify particular robot platforms, task domains, or the number of tasks generated.\n\n**Main Results:** Substantial reduction in execution failure rates compared to baseline generative approaches while maintaining semantic diversity.",
    "durationMs": 6702,
    "url": "https://arxiv.org/abs/2603.01505"
  },
  "sourceToolAssistantUUID": "6d2984ed-17e8-4770-8141-e55b0a760b01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T19:27:53.537Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017DVDF7kSqRQHa8AEPY7hQG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.12263",
  "prompt": "Extract the full abstract, authors, submission date, and venue for Ψ₀. What humanoid robot does it target? What is the staged VLM pre-training approach? What are the key results, especially on loco-manipulation tasks? Is there a benchmark or evaluation protocol?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8608df80-c9b5-45d4-a9cc-ab64dd6e253a",
  "isSidechain": false,
  "requestId": "req_011CauSTE79YkSuCULxS1pnr",
  "type": "assistant",
  "uuid": "c5293242-e79e-46b1-ad68-14441942fe5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XVLtYxgWdmQEzsMTHx8BSE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 33331,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 639,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 144,
          "cache_read_input_tokens": 33331,
          "cache_creation_input_tokens": 639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 639
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-10T19:27:59.077Z_

<details><summary>↩ Tool result · `toolu_017DVDF7kSqRQHa8AEPY7hQG`</summary>

```text
# Ψ₀: Foundation Model for Humanoid Loco-Manipulation

## Basic Information
**Authors:** Songlin Wei, Hongyi Jing, Boqian Li, Zhenyu Zhao, Jiageng Mao, Zhenhao Ni, Sicheng He, Jie Liu, Xiawei Liu, Kaidi Kang, Sheng Zang, Weiduo Yuan, Marco Pavone, Di Huang, Yue Wang

**Submission Date:** March 12, 2026

**Venue:** arXiv Computer Science - Robotics (cs.RO)

## Abstract
The researchers introduced Ψ₀ to tackle humanoid loco-manipulation by decoupling the learning process. The approach involves "autoregressively pre-train a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations" followed by post-training a flow-based action expert on humanoid robot data.

## Target Robot
The paper does not specify which particular humanoid robot model it targets—only referring generally to "humanoid robots."

## Staged VLM Pre-training
The two-stage approach consists of:
1. **Pre-training:** VLM backbone trained on egocentric human manipulation videos for visual-action understanding
2. **Post-training:** Flow-based action expert trained on domain-specific humanoid robot trajectories

## Key Results
Performance significantly exceeds baselines: the model "achieves the best performance using only about 800 hours of human video data and 30 hours of real-world robot data, outperforming baselines pre-trained on more than 10× as much data by over 40% in overall success rate."

## Evaluation & Benchmark
The abstract references "multiple tasks" but doesn't detail specific benchmarks or evaluation protocols in the provided excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5293242-e79e-46b1-ad68-14441942fe5d",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "17f0c0aa-3828-4646-aca0-dd9f43e28ca9",
  "toolUseResult": {
    "bytes": 48592,
    "code": 200,
    "codeText": "OK",
    "result": "# Ψ₀: Foundation Model for Humanoid Loco-Manipulation\n\n## Basic Information\n**Authors:** Songlin Wei, Hongyi Jing, Boqian Li, Zhenyu Zhao, Jiageng Mao, Zhenhao Ni, Sicheng He, Jie Liu, Xiawei Liu, Kaidi Kang, Sheng Zang, Weiduo Yuan, Marco Pavone, Di Huang, Yue Wang\n\n**Submission Date:** March 12, 2026\n\n**Venue:** arXiv Computer Science - Robotics (cs.RO)\n\n## Abstract\nThe researchers introduced Ψ₀ to tackle humanoid loco-manipulation by decoupling the learning process. The approach involves \"autoregressively pre-train a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations\" followed by post-training a flow-based action expert on humanoid robot data.\n\n## Target Robot\nThe paper does not specify which particular humanoid robot model it targets—only referring generally to \"humanoid robots.\"\n\n## Staged VLM Pre-training\nThe two-stage approach consists of:\n1. **Pre-training:** VLM backbone trained on egocentric human manipulation videos for visual-action understanding\n2. **Post-training:** Flow-based action expert trained on domain-specific humanoid robot trajectories\n\n## Key Results\nPerformance significantly exceeds baselines: the model \"achieves the best performance using only about 800 hours of human video data and 30 hours of real-world robot data, outperforming baselines pre-trained on more than 10× as much data by over 40% in overall success rate.\"\n\n## Evaluation & Benchmark\nThe abstract references \"multiple tasks\" but doesn't detail specific benchmarks or evaluation protocols in the provided excerpt.",
    "durationMs": 5537,
    "url": "https://arxiv.org/abs/2603.12263"
  },
  "sourceToolAssistantUUID": "c5293242-e79e-46b1-ad68-14441942fe5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Co…",
  "leafUuid": "17f0c0aa-3828-4646-aca0-dd9f43e28ca9",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise CoRL 2026 scope or justify Humanoids 2026 timeline",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Tool call

_source line 37 · 2026-05-10T19:28:01.829Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PwiC6MSRWceDXXiAYdqjuH`</summary>

```json
{
  "query": "Generative Skill Chaining diffusion models CoRL 2023 or 2024 arXiv 2401.03360"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17f0c0aa-3828-4646-aca0-dd9f43e28ca9",
  "isSidechain": false,
  "requestId": "req_011CauSU79imKNQswBa8KFFc",
  "type": "assistant",
  "uuid": "567849f8-c06c-4d0c-84f5-3cfcb3ec31db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GujiQ43Gwy3hqJZBg7gGb8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 581,
      "cache_read_input_tokens": 33970,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 581,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 33970,
          "cache_creation_input_tokens": 581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 581
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-10T19:28:08.915Z_

<details><summary>↩ Tool result · `toolu_01PwiC6MSRWceDXXiAYdqjuH`</summary>

```text
Web search results for query: "Generative Skill Chaining diffusion models CoRL 2023 or 2024 arXiv 2401.03360"

Links: [{"title":"[2401.03360] Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models","url":"https://arxiv.org/abs/2401.03360"},{"title":"Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models","url":"https://arxiv.org/pdf/2401.03360"},{"title":"Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models | Request PDF","url":"https://www.researchgate.net/publication/390175368_Generative_Skill_Chaining_Long-Horizon_Skill_Planning_with_Diffusion_Models"},{"title":"Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240103360M/abstract"},{"title":"Utkarsh A. Mishra","url":"https://umishra.me/"},{"title":"[PDF] Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Generative-Skill-Chaining:-Long-Horizon-Skill-with-Mishra-Xue/7090d35c316afe869440ede6ad61fdeec85b8bc8"},{"title":"Generative Skill Chaining","url":"https://generative-skill-chaining.github.io/"},{"title":"Generative Factor Chaining: Coordinated Manipulation with Diffusion-based Factor Graph | OpenReview","url":"https://openreview.net/forum?id=p6Wq6TjjHH"},{"title":"Generative Factor Chaining","url":"https://generative-fc.github.io/"},{"title":"GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub","url":"https://github.com/showlab/Awesome-Robotics-Diffusion"}]

Based on the search results, here's what I found:

## Generative Skill Chaining (arXiv 2401.03360)

The paper was submitted on October 13, 2023, and it was published in the Proceedings of The 7th Conference on Robot Learning (CoRL 2023).

**Paper Overview:**

Generative Skill Chaining (GSC) is a probabilistic framework that learns skill-centric diffusion models and composes their learned distributions to generate long-horizon plans during inference. 

GSC samples from all skill models in parallel to efficiently solve unseen tasks while enforcing geometric constraints.

**Authors:**
Utkarsh A. Mishra, Shangjie Xue, Yongxin Chen, and Danfei Xu

**Key Contributions:**

The method uses skill-level probabilistic generative models that capture the joint distribution of precondition-skill parameter-effect of each skill, and allows direct sampling of valid skill chains given a plan skeleton by conditionally generating skill parameters and post-condition states that satisfy the pre-condition of the next skill.

The paper evaluates the method on various long-horizon tasks and demonstrates its capability in reasoning about action dependencies, constraint handling, and generalization, along with its ability to replan in the face of perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "567849f8-c06c-4d0c-84f5-3cfcb3ec31db",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "d8e6e51e-9862-4aba-99f9-58efaea34a97",
  "toolUseResult": {
    "query": "Generative Skill Chaining diffusion models CoRL 2023 or 2024 arXiv 2401.03360",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BRbvCLsCrGdwV4cytdnuaB",
        "content": [
          {
            "title": "[2401.03360] Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models",
            "url": "https://arxiv.org/abs/2401.03360"
          },
          {
            "title": "Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models",
            "url": "https://arxiv.org/pdf/2401.03360"
          },
          {
            "title": "Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models | Request PDF",
            "url": "https://www.researchgate.net/publication/390175368_Generative_Skill_Chaining_Long-Horizon_Skill_Planning_with_Diffusion_Models"
          },
          {
            "title": "Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240103360M/abstract"
          },
          {
            "title": "Utkarsh A. Mishra",
            "url": "https://umishra.me/"
          },
          {
            "title": "[PDF] Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Generative-Skill-Chaining:-Long-Horizon-Skill-with-Mishra-Xue/7090d35c316afe869440ede6ad61fdeec85b8bc8"
          },
          {
            "title": "Generative Skill Chaining",
            "url": "https://generative-skill-chaining.github.io/"
          },
          {
            "title": "Generative Factor Chaining: Coordinated Manipulation with Diffusion-based Factor Graph | OpenReview",
            "url": "https://openreview.net/forum?id=p6Wq6TjjHH"
          },
          {
            "title": "Generative Factor Chaining",
            "url": "https://generative-fc.github.io/"
          },
          {
            "title": "GitHub - showlab/Awesome-Robotics-Diffusion: A curated list of recent robot learning papers incorporating diffusion models for robotics tasks. · GitHub",
            "url": "https://github.com/showlab/Awesome-Robotics-Diffusion"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\n## Generative Skill Chaining (arXiv 2401.03360)\n\nThe paper was submitted on October 13, 2023, and it was published in the Proceedings of The 7th Conference on Robot Learning (CoRL 2023).\n\n**Paper Overview:**\n\nGenerative Skill Chaining (GSC) is a probabilistic framework that learns skill-centric diffusion models and composes their learned distributions to generate long-horizon plans during inference. \n\nGSC samples from all skill models in parallel to efficiently solve unseen tasks while enforcing geometric constraints.\n\n**Authors:**\nUtkarsh A. Mishra, Shangjie Xue, Yongxin Chen, and Danfei Xu\n\n**Key Contributions:**\n\nThe method uses skill-level probabilistic generative models that capture the joint distribution of precondition-skill parameter-effect of each skill, and allows direct sampling of valid skill chains given a plan skeleton by conditionally generating skill parameters and post-condition states that satisfy the pre-condition of the next skill.\n\nThe paper evaluates the method on various long-horizon tasks and demonstrates its capability in reasoning about action dependencies, constraint handling, and generalization, along with its ability to replan in the face of perturbations."
    ],
    "durationSeconds": 7.082122596999994
  },
  "sourceToolAssistantUUID": "567849f8-c06c-4d0c-84f5-3cfcb3ec31db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-10T19:28:17.437Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011epretEhsdyxqdXnNNTs1n`</summary>

```json
{
  "url": "https://arxiv.org/abs/2401.03360",
  "prompt": "What venue was this paper published at? CoRL 2023 or CoRL 2024? What year was the conference? Extract any conference/venue info from the page."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8e6e51e-9862-4aba-99f9-58efaea34a97",
  "isSidechain": false,
  "requestId": "req_011CauSUqBoch9UaLGpaR8a9",
  "type": "assistant",
  "uuid": "fe93ed94-b3bf-4d82-b768-80418dfd1345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXMyJkkQQkgexrNiBpRN3t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 970,
      "cache_read_input_tokens": 34551,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 34551,
          "cache_creation_input_tokens": 970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 970
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T19:28:19.249Z_

<details><summary>↩ Tool result · `toolu_011epretEhsdyxqdXnNNTs1n`</summary>

```text
# Conference Publication Details

Based on the page content, this paper was published at **CoRL 2023**.

The relevant citation states: "Accepted at CoRL 2023: [this https URL](https://openreview.net/forum?id=HtJE9ly5dT)"

CoRL stands for Conference on Robot Learning. The paper was submitted on October 13, 2023, and accepted at the 2023 iteration of the conference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe93ed94-b3bf-4d82-b768-80418dfd1345",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "418fa652-3d65-4825-875a-7e567f82cfaa",
  "toolUseResult": {
    "bytes": 46083,
    "code": 200,
    "codeText": "OK",
    "result": "# Conference Publication Details\n\nBased on the page content, this paper was published at **CoRL 2023**.\n\nThe relevant citation states: \"Accepted at CoRL 2023: [this https URL](https://openreview.net/forum?id=HtJE9ly5dT)\"\n\nCoRL stands for Conference on Robot Learning. The paper was submitted on October 13, 2023, and accepted at the 2023 iteration of the conference.",
    "durationMs": 1808,
    "url": "https://arxiv.org/abs/2401.03360"
  },
  "sourceToolAssistantUUID": "fe93ed94-b3bf-4d82-b768-80418dfd1345",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-10T19:28:22.785Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017wBLXGHjS8Zq5UzAHpowxL`</summary>

```json
{
  "query": "RoboGene feasibility evaluators LFU sampling diversity-driven 2026 details method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "418fa652-3d65-4825-875a-7e567f82cfaa",
  "isSidechain": false,
  "requestId": "req_011CauSVbLeVgtiUMCH8HWqX",
  "type": "assistant",
  "uuid": "9d31d464-1c15-4546-b868-406cfe9379f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sj1EDb67YMawHJXJfuKj23",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 35521,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 230,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 35521,
          "cache_creation_input_tokens": 230,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 230
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-10T19:28:29.645Z_

<details><summary>↩ Tool result · `toolu_017wBLXGHjS8Zq5UzAHpowxL`</summary>

```text
Web search results for query: "RoboGene feasibility evaluators LFU sampling diversity-driven 2026 details method"

Links: [{"title":"RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation","url":"https://arxiv.org/html/2602.16444"},{"title":"[2602.16444v2] RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation","url":"https://arxiv.org/abs/2602.16444v2"},{"title":"[2602.16444] RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation","url":"https://arxiv.org/abs/2602.16444"},{"title":"[2602.15270] Enhancing Diversity and Feasibility: Joint Population Synthesis from Multi-source Data Using Generative Models","url":"https://arxiv.org/abs/2602.15270"},{"title":"","url":"http://192.99.15.201/pdf/23524129-respondent-driven-sampling-feasibility-validation-and-its-potential-use-for-estimating-health-indicators-for-large-general-populations/"},{"title":"RoboGen | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3694197"},{"title":"Clinical evaluation of the RoboGene Kit for HDV RNA quantification | Request PDF","url":"https://www.researchgate.net/publication/333999244_Clinical_evaluation_of_the_RoboGene_Kit_for_HDV_RNA_quantification"},{"title":"Accurate quantification using the new RoboGene HDV RNA Quantification Kit 3.0: A European multicenter study - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1386653225000708"},{"title":"Maintaining and Enhancing Diversity of Sampled Protein Conformations in Robotics-Inspired Methods - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC5756939/"},{"title":"Quantification of serum HDV RNA by Robogene 2.0 in HDV patients is significantly influenced by the extraction methods - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/38247385/"}]

Based on the search results, I found detailed information about RoboGene and its feasibility evaluators with LFU sampling:

## RoboGene Overview

RoboGene is an agentic framework designed to automate the generation of diverse, physically plausible manipulation tasks across single-arm, dual-arm, and mobile robots.

## Feasibility Evaluators and Method Details

The framework incorporates three specialized evaluators built on foundation models to independently assess constraint adherence, novelty, and physical feasibility. These evaluators work as part of a self-reflection mechanism to ensure robust physical grounding.

## Diversity-Driven LFU Sampling

To address the long-tail distribution problem, RoboGene employs a diversity-driven sampling mechanism based on a Least Frequently Used (LFU) strategy that actively guides the agent toward under-explored regions of the task space, prioritizing interactions with rare objects and skills.

## Key Components

RoboGene integrates three core components: diversity-driven sampling for broad task coverage, self-reflection mechanisms to enforce physical constraints, and human-in-the-loop refinement for continuous improvement.

## Evaluation Results

The framework introduces a novel suite of metrics to quantify both the quality of individual tasks, such as physical feasibility, and the global properties of the generated dataset, such as object and skill diversity. Extensive evaluations collected datasets of 18,000 trajectories with novel metrics assessing task quality, feasibility, and diversity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d31d464-1c15-4546-b868-406cfe9379f5",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "eb3044d7-227e-4e70-b0f7-100b6a5e5123",
  "toolUseResult": {
    "query": "RoboGene feasibility evaluators LFU sampling diversity-driven 2026 details method",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QSrjY1voV12uwUFXd4qAPF",
        "content": [
          {
            "title": "RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation",
            "url": "https://arxiv.org/html/2602.16444"
          },
          {
            "title": "[2602.16444v2] RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation",
            "url": "https://arxiv.org/abs/2602.16444v2"
          },
          {
            "title": "[2602.16444] RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation",
            "url": "https://arxiv.org/abs/2602.16444"
          },
          {
            "title": "[2602.15270] Enhancing Diversity and Feasibility: Joint Population Synthesis from Multi-source Data Using Generative Models",
            "url": "https://arxiv.org/abs/2602.15270"
          },
          {
            "title": "",
            "url": "http://192.99.15.201/pdf/23524129-respondent-driven-sampling-feasibility-validation-and-its-potential-use-for-estimating-health-indicators-for-large-general-populations/"
          },
          {
            "title": "RoboGen | Proceedings of the 41st International Conference on Machine Learning",
            "url": "https://dl.acm.org/doi/10.5555/3692070.3694197"
          },
          {
            "title": "Clinical evaluation of the RoboGene Kit for HDV RNA quantification | Request PDF",
            "url": "https://www.researchgate.net/publication/333999244_Clinical_evaluation_of_the_RoboGene_Kit_for_HDV_RNA_quantification"
          },
          {
            "title": "Accurate quantification using the new RoboGene HDV RNA Quantification Kit 3.0: A European multicenter study - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S1386653225000708"
          },
          {
            "title": "Maintaining and Enhancing Diversity of Sampled Protein Conformations in Robotics-Inspired Methods - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5756939/"
          },
          {
            "title": "Quantification of serum HDV RNA by Robogene 2.0 in HDV patients is significantly influenced by the extraction methods - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/38247385/"
          }
        ]
      },
      "Based on the search results, I found detailed information about RoboGene and its feasibility evaluators with LFU sampling:\n\n## RoboGene Overview\n\nRoboGene is an agentic framework designed to automate the generation of diverse, physically plausible manipulation tasks across single-arm, dual-arm, and mobile robots.\n\n## Feasibility Evaluators and Method Details\n\nThe framework incorporates three specialized evaluators built on foundation models to independently assess constraint adherence, novelty, and physical feasibility. These evaluators work as part of a self-reflection mechanism to ensure robust physical grounding.\n\n## Diversity-Driven LFU Sampling\n\nTo address the long-tail distribution problem, RoboGene employs a diversity-driven sampling mechanism based on a Least Frequently Used (LFU) strategy that actively guides the agent toward under-explored regions of the task space, prioritizing interactions with rare objects and skills.\n\n## Key Components\n\nRoboGene integrates three core components: diversity-driven sampling for broad task coverage, self-reflection mechanisms to enforce physical constraints, and human-in-the-loop refinement for continuous improvement.\n\n## Evaluation Results\n\nThe framework introduces a novel suite of metrics to quantify both the quality of individual tasks, such as physical feasibility, and the global properties of the generated dataset, such as object and skill diversity. Extensive evaluations collected datasets of 18,000 trajectories with novel metrics assessing task quality, feasibility, and diversity."
    ],
    "durationSeconds": 6.857280657999974
  },
  "sourceToolAssistantUUID": "9d31d464-1c15-4546-b868-406cfe9379f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-10T19:28:36.869Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AkxCMBDokHe3X1fTBYbrNg`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.16444",
  "prompt": "Extract the detailed method of RoboGene. Specifically: (1) What are the three feasibility evaluators and how do they work? (2) How does the LFU diversity sampling work? (3) What is the self-reflection/repair mechanism? (4) What robots and environments does it target? (5) What are the main results and comparisons? (6) Does it handle compositional or multi-stage tasks, or only single atomic tasks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb3044d7-227e-4e70-b0f7-100b6a5e5123",
  "isSidechain": false,
  "requestId": "req_011CauSWNP4bqGnWMq18ciHE",
  "type": "assistant",
  "uuid": "6f651c8c-fe5e-4814-88d1-7e8e617f099f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0166M39sSyWzLnHUYC4b2bTq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1061,
      "cache_read_input_tokens": 35751,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1061,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 182,
          "cache_read_input_tokens": 35751,
          "cache_creation_input_tokens": 1061,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1061
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T19:28:48.168Z_

<details><summary>↩ Tool result · `toolu_01AkxCMBDokHe3X1fTBYbrNg`</summary>

```text
# RoboGene: Detailed Method Extraction

## (1) Three Feasibility Evaluators

RoboGene employs specialized LLM-based evaluators:

**Physical Feasibility Evaluator (E_phy):** Assesses whether tasks are achievable given robot type and physics laws. It examines "kinematic feasibility (e.g., the overlap of dual-arm workspaces)" and validates task decomposition logic, synchronization control, and compliance with fundamental physical laws.

**Novelty Evaluator (E_nov):** Measures task complexity across four dimensions: object complexity (deformable objects, fluids), precision of contact/interaction (in-hand manipulation, tool use), temporal/logical depth (long-horizon tasks), and environmental unstructuredness (dynamic targets, disturbances).

**Constraint Adherence Evaluator (E_con):** Verifies the task aligns with assigned scene type and correctly uses objects/skills from sampled sets without hallucination, providing specific modification suggestions.

## (2) LFU Diversity Sampling

The Least Frequently Used strategy operates hierarchically:

- **Scenario selection:** Chooses the environment category with minimum usage count: "et = arg min u(e)"
- **Semantic filtering:** Filters contextually relevant objects/skills to prevent incoherence
- **Candidate sampling:** Selects objects and skills using LFU strategy, "favoring objects with lower usage frequencies"

This ensures balanced coverage across under-explored regions of the task space.

## (3) Self-Reflection/Repair Mechanism

The system implements a generator-evaluator-improvement loop:

1. A proposal generator produces initial task (T_raw)
2. Three evaluators independently produce critiques (f_phy, f_nov, f_con)
3. A self-reflection refiner integrates critiques to produce revised task (T_ref)
4. Memory-augmented refinement retrieves relevant heuristics via retrieval-augmented generation (RAG)

## (4) Robots and Environments Targeted

**Robots:** Single-arm (UR-5e), dual-arm (Franka), mobile manipulation (AgileX Cobot Magic V2.0)

**Environments:** Eight semantic scenarios—"Domestic, Office, Education, Laboratory, Kitchen, Industry, Retail, and Medical"

**Task Space:** 1,137 objects and 118 manipulation skills across these embodiments.

## (5) Main Results and Comparisons

RoboGene substantially outperforms baselines:

- **Object coverage:** 0.6323 vs. GPT-4o (0.3105) and Gemini (0.2172)
- **Skill coverage:** 0.9152 vs. baselines ~25%
- **Object diversity:** 719 unique objects vs. ~350 for GPT-4o
- **Real-world validation:** Policies pre-trained on RoboGene data achieved superior success rates and generalization across novel objects, backgrounds, illumination changes, and instruction variations

## (6) Task Complexity Handling

RoboGene handles **multi-stage compositional tasks**. Example Instance 1 shows cleaning requiring "throwing used tissue, then taking new tissue to wipe." Instance 3 demonstrates four-step sorting tasks (pick, identify, navigate, place). The framework explicitly values "long-horizon tasks with partial observability" and "temporal and logical depth."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f651c8c-fe5e-4814-88d1-7e8e617f099f",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "653f5c01-0a3a-4bd2-ab5b-77c8ec6fdc1e",
  "toolUseResult": {
    "bytes": 1218441,
    "code": 200,
    "codeText": "OK",
    "result": "# RoboGene: Detailed Method Extraction\n\n## (1) Three Feasibility Evaluators\n\nRoboGene employs specialized LLM-based evaluators:\n\n**Physical Feasibility Evaluator (E_phy):** Assesses whether tasks are achievable given robot type and physics laws. It examines \"kinematic feasibility (e.g., the overlap of dual-arm workspaces)\" and validates task decomposition logic, synchronization control, and compliance with fundamental physical laws.\n\n**Novelty Evaluator (E_nov):** Measures task complexity across four dimensions: object complexity (deformable objects, fluids), precision of contact/interaction (in-hand manipulation, tool use), temporal/logical depth (long-horizon tasks), and environmental unstructuredness (dynamic targets, disturbances).\n\n**Constraint Adherence Evaluator (E_con):** Verifies the task aligns with assigned scene type and correctly uses objects/skills from sampled sets without hallucination, providing specific modification suggestions.\n\n## (2) LFU Diversity Sampling\n\nThe Least Frequently Used strategy operates hierarchically:\n\n- **Scenario selection:** Chooses the environment category with minimum usage count: \"et = arg min u(e)\"\n- **Semantic filtering:** Filters contextually relevant objects/skills to prevent incoherence\n- **Candidate sampling:** Selects objects and skills using LFU strategy, \"favoring objects with lower usage frequencies\"\n\nThis ensures balanced coverage across under-explored regions of the task space.\n\n## (3) Self-Reflection/Repair Mechanism\n\nThe system implements a generator-evaluator-improvement loop:\n\n1. A proposal generator produces initial task (T_raw)\n2. Three evaluators independently produce critiques (f_phy, f_nov, f_con)\n3. A self-reflection refiner integrates critiques to produce revised task (T_ref)\n4. Memory-augmented refinement retrieves relevant heuristics via retrieval-augmented generation (RAG)\n\n## (4) Robots and Environments Targeted\n\n**Robots:** Single-arm (UR-5e), dual-arm (Franka), mobile manipulation (AgileX Cobot Magic V2.0)\n\n**Environments:** Eight semantic scenarios—\"Domestic, Office, Education, Laboratory, Kitchen, Industry, Retail, and Medical\"\n\n**Task Space:** 1,137 objects and 118 manipulation skills across these embodiments.\n\n## (5) Main Results and Comparisons\n\nRoboGene substantially outperforms baselines:\n\n- **Object coverage:** 0.6323 vs. GPT-4o (0.3105) and Gemini (0.2172)\n- **Skill coverage:** 0.9152 vs. baselines ~25%\n- **Object diversity:** 719 unique objects vs. ~350 for GPT-4o\n- **Real-world validation:** Policies pre-trained on RoboGene data achieved superior success rates and generalization across novel objects, backgrounds, illumination changes, and instruction variations\n\n## (6) Task Complexity Handling\n\nRoboGene handles **multi-stage compositional tasks**. Example Instance 1 shows cleaning requiring \"throwing used tissue, then taking new tissue to wipe.\" Instance 3 demonstrates four-step sorting tasks (pick, identify, navigate, place). The framework explicitly values \"long-horizon tasks with partial observability\" and \"temporal and logical depth.\"",
    "durationMs": 11294,
    "url": "https://arxiv.org/html/2602.16444"
  },
  "sourceToolAssistantUUID": "6f651c8c-fe5e-4814-88d1-7e8e617f099f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-10T19:28:52.152Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NmBj88KBCoNiFppHNVWtQR`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.01505",
  "prompt": "Extract the detailed method of FATE. Specifically: (1) How does the static feasibility phase work? (2) How does the dynamic feasibility phase work? (3) What is the active repair module? (4) What robots and simulators does it target? (5) Does it handle multi-stage compositional tasks or only single tasks? (6) What are the main quantitative results? (7) How many tasks does it generate?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "653f5c01-0a3a-4bd2-ab5b-77c8ec6fdc1e",
  "isSidechain": false,
  "requestId": "req_011CauSXj3JKjnbU4Jvjn6Gg",
  "type": "assistant",
  "uuid": "31224604-794d-4199-a735-e67aeaf9cde7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015yLMkLEgSgdPAHNXE5Pvbc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 981,
      "cache_read_input_tokens": 36812,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 981,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 36812,
          "cache_creation_input_tokens": 981,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 981
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-10T19:29:02.295Z_

<details><summary>↩ Tool result · `toolu_01NmBj88KBCoNiFppHNVWtQR`</summary>

```text
# FATE: Detailed Method Extraction

## (1) Static Feasibility Phase

The static alignment operator (𝒜perc) acts as a "perceptual gatekeeper" that validates scene-instruction alignment before simulation. The Ante-Auditor checks four consistency conditions: reachability, affordance matching, physical plausibility, and morphological compatibility. Upon detecting violations, the system applies discrete repairs like object swapping, rescaling, pose adjustment, or asset removal to project the task onto a geometrically valid manifold.

## (2) Dynamic Feasibility Phase

The dynamic alignment operator (𝒜exec) monitors task execution and detects runtime failures such as grasp instability, collision deadlocks, or sparse reward stagnation. When divergences occur, the In-Step Auditor triggers a "rollback-and-repair" mechanism that modifies either the physical scene configuration or solver parameters—effectively implementing a semantic policy gradient to pull divergent trajectories back into the feasible region.

## (3) Active Repair Module

The repair system comprises two hierarchical stages. Static repair uses discrete APIs (SWAP_ASSET, RESCALE, TRANSFORM_POSE, etc.) to fix perceptual hallucinations. Dynamic repair adjusts RL reward functions, MPC constraints, and controller impedance through APIs like INJECT_REWARD and REPLAN_PATH. The framework treats repairs as "constructive residual injection" rather than discarding infeasible proposals.

## (4) Robots and Simulators

The paper evaluates on a "RidgebackFranka" platform—a 7-DoF arm mounted on a holonomic base. It implements the system in "NVIDIA Isaac Sim" leveraging precise contact physics, using BIT* for collision-free navigation and Soft Actor-Critic (SAC) for contact-rich manipulation.

## (5) Task Composition

FATE handles multi-stage compositional tasks. The framework decomposes global instructions into "a sequence of atomic primitives" and employs hierarchical decomposition with state checkpointing to support iterative refinement across multiple execution stages.

## (6) Main Quantitative Results

- **Scene Validity Rate (SVR):** 97.5% (full pipeline)
- **Execution Validity Rate (EVR):** 94.5%
- **Feasible Task Rate (FTR):** 92.1% (versus 12.6% baseline)
- **Auditor F1-Score:** 0.88 overall (0.95 semantic, 0.86 geometric, 0.83 dynamic)
- **Repair Success Rate (RSR):** 89.5% aggregate across all stages

## (7) Task Generation Scale

The paper generates 352 tasks evaluated in experiments. Tasks are sampled from a diverse proposal distribution using assets from Objaverse and PartNet-Mobility, with semantic diversity metrics showing comparable performance to human-curated benchmarks (Self-BLEU-4: 0.276 versus 0.299–0.378 for baselines).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31224604-794d-4199-a735-e67aeaf9cde7",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "ca26cf14-bcf6-436d-a2cb-be7b5db2b840",
  "toolUseResult": {
    "bytes": 374696,
    "code": 200,
    "codeText": "OK",
    "result": "# FATE: Detailed Method Extraction\n\n## (1) Static Feasibility Phase\n\nThe static alignment operator (𝒜perc) acts as a \"perceptual gatekeeper\" that validates scene-instruction alignment before simulation. The Ante-Auditor checks four consistency conditions: reachability, affordance matching, physical plausibility, and morphological compatibility. Upon detecting violations, the system applies discrete repairs like object swapping, rescaling, pose adjustment, or asset removal to project the task onto a geometrically valid manifold.\n\n## (2) Dynamic Feasibility Phase\n\nThe dynamic alignment operator (𝒜exec) monitors task execution and detects runtime failures such as grasp instability, collision deadlocks, or sparse reward stagnation. When divergences occur, the In-Step Auditor triggers a \"rollback-and-repair\" mechanism that modifies either the physical scene configuration or solver parameters—effectively implementing a semantic policy gradient to pull divergent trajectories back into the feasible region.\n\n## (3) Active Repair Module\n\nThe repair system comprises two hierarchical stages. Static repair uses discrete APIs (SWAP_ASSET, RESCALE, TRANSFORM_POSE, etc.) to fix perceptual hallucinations. Dynamic repair adjusts RL reward functions, MPC constraints, and controller impedance through APIs like INJECT_REWARD and REPLAN_PATH. The framework treats repairs as \"constructive residual injection\" rather than discarding infeasible proposals.\n\n## (4) Robots and Simulators\n\nThe paper evaluates on a \"RidgebackFranka\" platform—a 7-DoF arm mounted on a holonomic base. It implements the system in \"NVIDIA Isaac Sim\" leveraging precise contact physics, using BIT* for collision-free navigation and Soft Actor-Critic (SAC) for contact-rich manipulation.\n\n## (5) Task Composition\n\nFATE handles multi-stage compositional tasks. The framework decomposes global instructions into \"a sequence of atomic primitives\" and employs hierarchical decomposition with state checkpointing to support iterative refinement across multiple execution stages.\n\n## (6) Main Quantitative Results\n\n- **Scene Validity Rate (SVR):** 97.5% (full pipeline)\n- **Execution Validity Rate (EVR):** 94.5%\n- **Feasible Task Rate (FTR):** 92.1% (versus 12.6% baseline)\n- **Auditor F1-Score:** 0.88 overall (0.95 semantic, 0.86 geometric, 0.83 dynamic)\n- **Repair Success Rate (RSR):** 89.5% aggregate across all stages\n\n## (7) Task Generation Scale\n\nThe paper generates 352 tasks evaluated in experiments. Tasks are sampled from a diverse proposal distribution using assets from Objaverse and PartNet-Mobility, with semantic diversity metrics showing comparable performance to human-curated benchmarks (Self-BLEU-4: 0.276 versus 0.299–0.378 for baselines).",
    "durationMs": 10139,
    "url": "https://arxiv.org/html/2603.01505"
  },
  "sourceToolAssistantUUID": "31224604-794d-4199-a735-e67aeaf9cde7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Co…",
  "leafUuid": "ca26cf14-bcf6-436d-a2cb-be7b5db2b840",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise CoRL 2026 scope or justify Humanoids 2026 timeline",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Tool call

_source line 49 · 2026-05-10T19:29:05.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HKFqSWeZwM7qwLcJhWL5rt`</summary>

```json
{
  "query": "Psi0 RSS 2026 humanoid loco-manipulation benchmark tasks evaluation Unitree"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca26cf14-bcf6-436d-a2cb-be7b5db2b840",
  "isSidechain": false,
  "requestId": "req_011CauSYmUBSxo9u9q3N6Qbh",
  "type": "assistant",
  "uuid": "cb07c51e-65a0-458e-bbce-2546155e917a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZsFoK8ScdmSQVY8psncyh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 882,
      "cache_read_input_tokens": 37793,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 882,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 37793,
          "cache_creation_input_tokens": 882,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 882
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-10T19:29:13.252Z_

<details><summary>↩ Tool result · `toolu_01HKFqSWeZwM7qwLcJhWL5rt`</summary>

```text
Web search results for query: "Psi0 RSS 2026 humanoid loco-manipulation benchmark tasks evaluation Unitree"

Links: [{"title":"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://psi-lab.ai/Psi0/"},{"title":"GitHub - physical-superintelligence-lab/Psi0: [RSS26'] Welcome to Psi-Zero, a Humanoid VLA towards Universal Humanoid Intelligence. · GitHub","url":"https://github.com/physical-superintelligence-lab/Psi0"},{"title":"[2603.12263] $Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation","url":"https://arxiv.org/abs/2603.12263"},{"title":"Towards robust Humanoid Loco-Manipulation using Deep Reinforcement Learning | by Niraj Pudasaini | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/towards-robust-humanoid-loco-manipulation-using-deep-reinforcement-learning-45c8a5a0fcbf"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning | OpenReview","url":"https://openreview.net/forum?id=hVoIz6xD9Q"},{"title":"HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation","url":"https://arxiv.org/html/2403.10506v1"},{"title":"HUMANOID-LLA: OPEN-VOCABULARY ...","url":"https://openreview.net/pdf/830d6b6b95ad212ad757bba8ac1fac08c6273041.pdf"},{"title":"HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation | Request PDF","url":"https://www.researchgate.net/publication/383889121_HumanoidBench_Simulated_Humanoid_Benchmark_for_Whole-Body_Locomotion_and_Manipulation"},{"title":"HumanoidBench","url":"https://humanoid-bench.github.io/"}]

Based on my search results, here's what I found about Psi0 and humanoid loco-manipulation benchmarks:

## Ψ₀: An Open Foundation Model for Humanoid Loco-Manipulation

Ψ₀ (Psi-Zero) is an open foundation model to address challenging humanoid loco-manipulation tasks. It is a vision-language-action (VLA) model for dexterous humanoid loco-manipulation.

### Training Approach

The model uses a staged training paradigm: it first autoregressively pre-trains a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations, then post-trains a flow-based action expert on high-quality humanoid robot data to learn precise robot joint control.

### Capabilities

The foundation model is capable of acquiring new long-horizontal dexterous loco-manipulation skill by fine-tuning using as few as 80 trajectories. Additionally, six pre-collected whole-body humanoid loco-manipulation tasks are available on Huggingface.

### RSS 2026 Publication

The paper was published on arXiv with the title "$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation" (arXiv:2603.12263) in 2026.

The Psi0 project also connects to the Unitree robotics platform, as indicated by references to real-world task collections in their open-source repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb07c51e-65a0-458e-bbce-2546155e917a",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "89f9b151-a70d-484a-859c-937d1f3dd35f",
  "toolUseResult": {
    "query": "Psi0 RSS 2026 humanoid loco-manipulation benchmark tasks evaluation Unitree",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M5fGDY33sj4mWV9wKiAcqs",
        "content": [
          {
            "title": "Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation",
            "url": "https://psi-lab.ai/Psi0/"
          },
          {
            "title": "GitHub - physical-superintelligence-lab/Psi0: [RSS26'] Welcome to Psi-Zero, a Humanoid VLA towards Universal Humanoid Intelligence. · GitHub",
            "url": "https://github.com/physical-superintelligence-lab/Psi0"
          },
          {
            "title": "[2603.12263] $Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation",
            "url": "https://arxiv.org/abs/2603.12263"
          },
          {
            "title": "Towards robust Humanoid Loco-Manipulation using Deep Reinforcement Learning | by Niraj Pudasaini | Toward Humanoids | Medium",
            "url": "https://medium.com/correll-lab/towards-robust-humanoid-loco-manipulation-using-deep-reinforcement-learning-45c8a5a0fcbf"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning | OpenReview",
            "url": "https://openreview.net/forum?id=hVoIz6xD9Q"
          },
          {
            "title": "HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation",
            "url": "https://arxiv.org/html/2403.10506v1"
          },
          {
            "title": "HUMANOID-LLA: OPEN-VOCABULARY ...",
            "url": "https://openreview.net/pdf/830d6b6b95ad212ad757bba8ac1fac08c6273041.pdf"
          },
          {
            "title": "HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation | Request PDF",
            "url": "https://www.researchgate.net/publication/383889121_HumanoidBench_Simulated_Humanoid_Benchmark_for_Whole-Body_Locomotion_and_Manipulation"
          },
          {
            "title": "HumanoidBench",
            "url": "https://humanoid-bench.github.io/"
          }
        ]
      },
      "Based on my search results, here's what I found about Psi0 and humanoid loco-manipulation benchmarks:\n\n## Ψ₀: An Open Foundation Model for Humanoid Loco-Manipulation\n\nΨ₀ (Psi-Zero) is an open foundation model to address challenging humanoid loco-manipulation tasks. It is a vision-language-action (VLA) model for dexterous humanoid loco-manipulation.\n\n### Training Approach\n\nThe model uses a staged training paradigm: it first autoregressively pre-trains a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations, then post-trains a flow-based action expert on high-quality humanoid robot data to learn precise robot joint control.\n\n### Capabilities\n\nThe foundation model is capable of acquiring new long-horizontal dexterous loco-manipulation skill by fine-tuning using as few as 80 trajectories. Additionally, six pre-collected whole-body humanoid loco-manipulation tasks are available on Huggingface.\n\n### RSS 2026 Publication\n\nThe paper was published on arXiv with the title \"$Ψ_0$: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation\" (arXiv:2603.12263) in 2026.\n\nThe Psi0 project also connects to the Unitree robotics platform, as indicated by references to real-world task collections in their open-source repository."
    ],
    "durationSeconds": 7.922131339999993
  },
  "sourceToolAssistantUUID": "cb07c51e-65a0-458e-bbce-2546155e917a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-10T19:29:16.556Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013v3kpiyUJatFEVLo7ifoSY`</summary>

```json
{
  "query": "compositional task generation humanoid robot grammar feasibility 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89f9b151-a70d-484a-859c-937d1f3dd35f",
  "isSidechain": false,
  "requestId": "req_011CauSZaFmZSEXyBV5eAHZN",
  "type": "assistant",
  "uuid": "4be3247d-5a53-4ac2-9095-ff1d0603b8bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWvQid3Ygzp3u9icbY1kaq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1052,
      "cache_read_input_tokens": 38675,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 38675,
          "cache_creation_input_tokens": 1052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1052
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-10T19:29:23.476Z_

<details><summary>↩ Tool result · `toolu_013v3kpiyUJatFEVLo7ifoSY`</summary>

```text
Web search results for query: "compositional task generation humanoid robot grammar feasibility 2025 2026 arXiv"

Links: [{"title":"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots","url":"https://arxiv.org/html/2503.14734"},{"title":"[2602.14551] Replanning Human-Robot Collaborative Tasks with Vision-Language Models via Semantic and Physical Dual-Correction","url":"https://arxiv.org/abs/2602.14551"},{"title":"Large Language Models for Robotics: A survey","url":"https://arxiv.org/html/2311.07226v2"},{"title":"Compositional Coordination for Multi‑Robot Teams with Large Language Models","url":"https://arxiv.org/html/2507.16068v3"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"ProgPrompt: program generation for situated robot task planning using large language models | Autonomous Robots | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10514-023-10135-3"},{"title":"ProgPrompt: program generation for situated robot task planning using large language models | Autonomous Robots","url":"https://dl.acm.org/doi/abs/10.1007/s10514-023-10135-3"},{"title":"Scaling up Memory for Robotic Control via Experience Retrieval | OpenReview","url":"https://openreview.net/forum?id=1dH4ARGdwD"},{"title":"PHUMA: PHYSICALLY-GROUNDED HUMANOID ...","url":"https://openreview.net/pdf/a36747cac87a488230dfe8cb6d5c0aa5a6db82d7.pdf"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2503.12466"}]

I found several relevant papers related to your search query. Here are the key findings from arXiv:

## Recent Papers on Humanoid Robots and Task Generation

GR00T N1 is an open foundation model for generalist humanoid robots that uses a compositional model integrating a Vision-Language Model (VLM)-based reasoning module and a Diffusion Transformer (DiT)-based action module in a unified learning framework. This paper was published in March 2025.

Human-Robot Collaboration (HRC) is important in assembly tasks by enabling robots to plan and adjust their motions based on interactive, real-time human instructions, though such instructions are often linguistically ambiguous and underspecified, making it difficult to generate physically feasible and cooperative robot behaviors. A related paper on this topic was published in February 2026.

A compositional approach for multi-robot coordination uses LLMs to compose robust execution code for action nodes, promoting reusability, flexibility, and scalability in multi-robot systems. This paper was published in October 2025.

## General Context on Language Models for Robotics

Large language models (LLMs) have garnered increasing attention in robotics, as they possess the ability to process and generate natural language, facilitating efficient interaction and collaboration with robots, and researchers have recognized their immense potential in enhancing robot intelligence, human-robot interaction, and autonomy.

These papers demonstrate active research into compositional task generation for humanoid robots using grammar-based and language-driven approaches in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4be3247d-5a53-4ac2-9095-ff1d0603b8bb",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "577f4cd0-0145-4454-9841-d63713e7887a",
  "toolUseResult": {
    "query": "compositional task generation humanoid robot grammar feasibility 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KWMSUf6QatXGgaMAcYawCc",
        "content": [
          {
            "title": "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots",
            "url": "https://arxiv.org/html/2503.14734"
          },
          {
            "title": "[2602.14551] Replanning Human-Robot Collaborative Tasks with Vision-Language Models via Semantic and Physical Dual-Correction",
            "url": "https://arxiv.org/abs/2602.14551"
          },
          {
            "title": "Large Language Models for Robotics: A survey",
            "url": "https://arxiv.org/html/2311.07226v2"
          },
          {
            "title": "Compositional Coordination for Multi‑Robot Teams with Large Language Models",
            "url": "https://arxiv.org/html/2507.16068v3"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "ProgPrompt: program generation for situated robot task planning using large language models | Autonomous Robots | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10514-023-10135-3"
          },
          {
            "title": "ProgPrompt: program generation for situated robot task planning using large language models | Autonomous Robots",
            "url": "https://dl.acm.org/doi/abs/10.1007/s10514-023-10135-3"
          },
          {
            "title": "Scaling up Memory for Robotic Control via Experience Retrieval | OpenReview",
            "url": "https://openreview.net/forum?id=1dH4ARGdwD"
          },
          {
            "title": "PHUMA: PHYSICALLY-GROUNDED HUMANOID ...",
            "url": "https://openreview.net/pdf/a36747cac87a488230dfe8cb6d5c0aa5a6db82d7.pdf"
          },
          {
            "title": "Arxiv",
            "url": "https://arxiv.org/pdf/2503.12466"
          }
        ]
      },
      "I found several relevant papers related to your search query. Here are the key findings from arXiv:\n\n## Recent Papers on Humanoid Robots and Task Generation\n\nGR00T N1 is an open foundation model for generalist humanoid robots that uses a compositional model integrating a Vision-Language Model (VLM)-based reasoning module and a Diffusion Transformer (DiT)-based action module in a unified learning framework. This paper was published in March 2025.\n\nHuman-Robot Collaboration (HRC) is important in assembly tasks by enabling robots to plan and adjust their motions based on interactive, real-time human instructions, though such instructions are often linguistically ambiguous and underspecified, making it difficult to generate physically feasible and cooperative robot behaviors. A related paper on this topic was published in February 2026.\n\nA compositional approach for multi-robot coordination uses LLMs to compose robust execution code for action nodes, promoting reusability, flexibility, and scalability in multi-robot systems. This paper was published in October 2025.\n\n## General Context on Language Models for Robotics\n\nLarge language models (LLMs) have garnered increasing attention in robotics, as they possess the ability to process and generate natural language, facilitating efficient interaction and collaboration with robots, and researchers have recognized their immense potential in enhancing robot intelligence, human-robot interaction, and autonomy.\n\nThese papers demonstrate active research into compositional task generation for humanoid robots using grammar-based and language-driven approaches in 2025-2026."
    ],
    "durationSeconds": 6.915874746999995
  },
  "sourceToolAssistantUUID": "4be3247d-5a53-4ac2-9095-ff1d0603b8bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-10T19:29:26.259Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W7Z2P8iNpmE9fkfD5U8uj9`</summary>

```json
{
  "query": "transition feasibility prediction skill composition learning GNN robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "577f4cd0-0145-4454-9841-d63713e7887a",
  "isSidechain": false,
  "requestId": "req_011CauSaL5kx1seh7ALUX3uB",
  "type": "assistant",
  "uuid": "9732ecca-2a89-4f42-a99f-f5442ecd26ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167rJPAfKFuZ5DLvgQ9cEHM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 935,
      "cache_read_input_tokens": 39727,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 935,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 39727,
          "cache_creation_input_tokens": 935,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 935
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-10T19:29:34.450Z_

<details><summary>↩ Tool result · `toolu_01W7Z2P8iNpmE9fkfD5U8uj9`</summary>

```text
Web search results for query: "transition feasibility prediction skill composition learning GNN robot 2025 2026"

Links: [{"title":"Ai et al., Sci. Robot. 10, eadt1497 (2025) 17 September 2025","url":"https://albertboai.com/assets/pdf/2025_scirobotics.adt1497.pdf"},{"title":"Proceedings of Machine Learning Research | Proceedings of The 8th Conference on Robot Learning Held in Munich, Germany on 06-09 November 2024 Published as Volume 270 by the Proceedings of Machine Learning Research on 12 January 2025. Volume Edited by: Pulkit Agrawal Oliver Kroemer Wolfram Burgard Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v270/"},{"title":"ICLR2025 Workshop Proposal on Generative Models for Robot Learning (GenBot) 1","url":"https://openreview.net/pdf?id=bYCIdcBpEm"},{"title":"GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub","url":"https://github.com/YanjieZe/awesome-humanoid-robot-learning"},{"title":"A review of learning-based dynamics models for robotic manipulation | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.adt1497"},{"title":"Robot learning in the era of foundation models: : a survey: Neurocomputing: Vol 638, No C","url":"https://dl.acm.org/doi/10.1016/j.neucom.2025.129963"},{"title":"Generative Models for Robot Learning","url":"https://iclr.cc/virtual/2025/workshop/23977"},{"title":"Towards zero-shot robot tool manipulation in industrial ...","url":"https://sites.gc.sjtu.edu.cn/youyibi/wp-content/uploads/sites/3/2025/10/RCIM-2026ToolManip.pdf"},{"title":"Deep reinforcement learning trajectory planning for robotic manipulator based on simulation-efficient training | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-93175-2"},{"title":"Cognitive Empowerment for Human-robot Collaboration: Research Progress and Challenges","url":"https://qikan.cmes.org/jxgcxb/EN/10.3901/JME.2025.03.001"}]

Based on the web search results, I found relevant information about robot learning with GNNs and related topics from 2025-2026:

## Key Findings

### GNNs for Robot Learning and Dynamics Modeling

GNNs are widely used for modeling particle interactions, where particles are represented as graph nodes with features that may include physical parameters or motion information, with hierarchical relation networks introducing hierarchical graph structures where leaf particles encode local interactions and root nodes provide object-level abstractions.

Dynamic particle interaction networks (DPI-Nets) update dynamic interaction graphs during simulation to effectively capture object deformations, with this flexibility enabling them to lay the foundation for modeling elastoplastic objects, granular material manipulation, food preparation, and object packing.

### Recent Robot Learning Research (2025-2026)

The search results also revealed active research in humanoid robot learning, including work on:
- Humanoid dexterous manipulation, motion generation with depth-fused distance fields, generative robot world models, vision-language-guided manipulation, and various specialized skills like parkour, gesture synthesis, and adaptive compliance control

### Human-Robot Collaboration and Skill Learning

Recent research reviews cognitive empowerment in human-machine collaboration, focusing on interactive perception, task planning and execution, and skill learning, while highlighting challenges in multimodal information integration, task reasoning, dynamic decision-making, and skill knowledge representation.

The search results show active development in robot learning using graph neural networks, particularly for dynamics modeling and skill composition tasks, though specific papers on "transition feasibility prediction" were not directly returned in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9732ecca-2a89-4f42-a99f-f5442ecd26ca",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "e66193fc-58da-4ff1-b35d-d6b4950582ca",
  "toolUseResult": {
    "query": "transition feasibility prediction skill composition learning GNN robot 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FdjeRLKUvWgXGJA997uNnb",
        "content": [
          {
            "title": "Ai et al., Sci. Robot. 10, eadt1497 (2025) 17 September 2025",
            "url": "https://albertboai.com/assets/pdf/2025_scirobotics.adt1497.pdf"
          },
          {
            "title": "Proceedings of Machine Learning Research | Proceedings of The 8th Conference on Robot Learning Held in Munich, Germany on 06-09 November 2024 Published as Volume 270 by the Proceedings of Machine Learning Research on 12 January 2025. Volume Edited by: Pulkit Agrawal Oliver Kroemer Wolfram Burgard Series Editors: Neil D. Lawrence",
            "url": "https://proceedings.mlr.press/v270/"
          },
          {
            "title": "ICLR2025 Workshop Proposal on Generative Models for Robot Learning (GenBot) 1",
            "url": "https://openreview.net/pdf?id=bYCIdcBpEm"
          },
          {
            "title": "GitHub - YanjieZe/awesome-humanoid-robot-learning: A Paper List for Humanoid Robot Learning. · GitHub",
            "url": "https://github.com/YanjieZe/awesome-humanoid-robot-learning"
          },
          {
            "title": "A review of learning-based dynamics models for robotic manipulation | Science Robotics",
            "url": "https://www.science.org/doi/10.1126/scirobotics.adt1497"
          },
          {
            "title": "Robot learning in the era of foundation models: : a survey: Neurocomputing: Vol 638, No C",
            "url": "https://dl.acm.org/doi/10.1016/j.neucom.2025.129963"
          },
          {
            "title": "Generative Models for Robot Learning",
            "url": "https://iclr.cc/virtual/2025/workshop/23977"
          },
          {
            "title": "Towards zero-shot robot tool manipulation in industrial ...",
            "url": "https://sites.gc.sjtu.edu.cn/youyibi/wp-content/uploads/sites/3/2025/10/RCIM-2026ToolManip.pdf"
          },
          {
            "title": "Deep reinforcement learning trajectory planning for robotic manipulator based on simulation-efficient training | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-93175-2"
          },
          {
            "title": "Cognitive Empowerment for Human-robot Collaboration: Research Progress and Challenges",
            "url": "https://qikan.cmes.org/jxgcxb/EN/10.3901/JME.2025.03.001"
          }
        ]
      },
      "Based on the web search results, I found relevant information about robot learning with GNNs and related topics from 2025-2026:\n\n## Key Findings\n\n### GNNs for Robot Learning and Dynamics Modeling\n\nGNNs are widely used for modeling particle interactions, where particles are represented as graph nodes with features that may include physical parameters or motion information, with hierarchical relation networks introducing hierarchical graph structures where leaf particles encode local interactions and root nodes provide object-level abstractions.\n\nDynamic particle interaction networks (DPI-Nets) update dynamic interaction graphs during simulation to effectively capture object deformations, with this flexibility enabling them to lay the foundation for modeling elastoplastic objects, granular material manipulation, food preparation, and object packing.\n\n### Recent Robot Learning Research (2025-2026)\n\nThe search results also revealed active research in humanoid robot learning, including work on:\n- Humanoid dexterous manipulation, motion generation with depth-fused distance fields, generative robot world models, vision-language-guided manipulation, and various specialized skills like parkour, gesture synthesis, and adaptive compliance control\n\n### Human-Robot Collaboration and Skill Learning\n\nRecent research reviews cognitive empowerment in human-machine collaboration, focusing on interactive perception, task planning and execution, and skill learning, while highlighting challenges in multimodal information integration, task reasoning, dynamic decision-making, and skill knowledge representation.\n\nThe search results show active development in robot learning using graph neural networks, particularly for dynamics modeling and skill composition tasks, though specific papers on \"transition feasibility prediction\" were not directly returned in these results."
    ],
    "durationSeconds": 8.185981999999989
  },
  "sourceToolAssistantUUID": "9732ecca-2a89-4f42-a99f-f5442ecd26ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 55 · 2026-05-10T19:29:34.453Z_

```json
{
  "parentUuid": "e66193fc-58da-4ff1-b35d-d6b4950582ca",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7cc6f823-c9c6-4028-83fe-94f07d19e2f1",
  "timestamp": "2026-05-10T19:29:34.453Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 56 · 2026-05-10T19:29:37.060Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FXUbeKzQER2LSxhSRVs1Sh`</summary>

```json
{
  "query": "CoRL 2026 call for papers page limit format requirements 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cc6f823-c9c6-4028-83fe-94f07d19e2f1",
  "isSidechain": false,
  "requestId": "req_011CauSb8v5UH42ctmRFAygx",
  "type": "assistant",
  "uuid": "e6aa53a1-1018-4d01-b4f4-bde4a8c52828",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAMmTGw7QZ6CWz4rBWhbVj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1161,
      "cache_read_input_tokens": 40662,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1161,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 40662,
          "cache_creation_input_tokens": 1161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1161
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-10T19:29:42.843Z_

<details><summary>↩ Tool result · `toolu_01FXUbeKzQER2LSxhSRVs1Sh`</summary>

```text
Web search results for query: "CoRL 2026 call for papers page limit format requirements 2026"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"Call for Papers · Robotics: Science and Systems","url":"https://roboticsconference.org/information/cfp/"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"}]

Based on the search results, here are the key page limit and format requirements for CoRL 2026:

## Page Limit

The page limit is 8 pages for the main paper. Acknowledgments, References, and Appendix (optional) will not count towards the page limit.

## Format Requirements

The camera-ready paper should follow the template: 8-page main text + acknowledgment + references + appendix (optional). The template uses "\usepackage[final]{corl_2026}".

## Additional Requirements

All submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future.

## Camera-Ready Updates

This year, an additional page is allowed to accommodate feedback from the review process.

For the most current and complete information, you can visit the official [CoRL 2026 Instruction for Authors page](https://www.corl.org/contributions/instruction-for-authors).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6aa53a1-1018-4d01-b4f4-bde4a8c52828",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "ff4bd80f-8732-45fb-b510-1479e123c7df",
  "toolUseResult": {
    "query": "CoRL 2026 call for papers page limit format requirements 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RVNK6HNuDGaF1sJkwXT6GD",
        "content": [
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL 2026 - Annoucements",
            "url": "https://www.corl.org/annoucements"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "CoRL 2026 - Instruction for Presentations",
            "url": "https://www.corl.org/contributions/instruction-for-presentations"
          },
          {
            "title": "Call for Papers · Robotics: Science and Systems",
            "url": "https://roboticsconference.org/information/cfp/"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          }
        ]
      },
      "Based on the search results, here are the key page limit and format requirements for CoRL 2026:\n\n## Page Limit\n\nThe page limit is 8 pages for the main paper. Acknowledgments, References, and Appendix (optional) will not count towards the page limit.\n\n## Format Requirements\n\nThe camera-ready paper should follow the template: 8-page main text + acknowledgment + references + appendix (optional). The template uses \"\\usepackage[final]{corl_2026}\".\n\n## Additional Requirements\n\nAll submissions should include a Limitations section (counted toward the 8-page limit), explicitly describing limiting assumptions, failure modes, and other limitations of the results and experiments, and how these might be addressed in the future.\n\n## Camera-Ready Updates\n\nThis year, an additional page is allowed to accommodate feedback from the review process.\n\nFor the most current and complete information, you can visit the official [CoRL 2026 Instruction for Authors page](https://www.corl.org/contributions/instruction-for-authors)."
    ],
    "durationSeconds": 5.780261407999991
  },
  "sourceToolAssistantUUID": "e6aa53a1-1018-4d01-b4f4-bde4a8c52828",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Co…",
  "leafUuid": "ff4bd80f-8732-45fb-b510-1479e123c7df",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise CoRL 2026 scope or justify Humanoids 2026 timeline",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Tool call

_source line 60 · 2026-05-10T19:29:46.431Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019F1RFNGsuc1HVMcgEtx3Lq`</summary>

```json
{
  "query": "AGILE humanoid loco-manipulation Isaac Lab SONIC GR00T WBC configuration 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff4bd80f-8732-45fb-b510-1479e123c7df",
  "isSidechain": false,
  "requestId": "req_011CauSbn2FUmAvQR9kqCmRM",
  "type": "assistant",
  "uuid": "7b67a7bd-5a45-4f2a-aa40-acaaff993d24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDCYh1qavYzYeAE1jmGxvh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 728,
      "cache_read_input_tokens": 41823,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 728,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 41823,
          "cache_creation_input_tokens": 728,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 728
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-10T19:29:55.130Z_

<details><summary>↩ Tool result · `toolu_019F1RFNGsuc1HVMcgEtx3Lq`</summary>

```text
Web search results for query: "AGILE humanoid loco-manipulation Isaac Lab SONIC GR00T WBC configuration 2026"

Links: [{"title":"GitHub - NVlabs/GR00T-WholeBodyControl: Welcome to GR00T Whole-Body Control (WBC)! This is a unified platform for developing and deploying advanced humanoid controllers. This includes: Decoupled WBC models used in NVIDIA Isaac-Gr00t, Gr00t N1.5 and N1.6 and GEAR-SONIC · GitHub","url":"https://github.com/NVlabs/GR00T-WholeBodyControl"},{"title":"GR00T-WholeBodyControl Documentation — GR00T-WholeBodyControl Documentation","url":"https://nvlabs.github.io/GR00T-WholeBodyControl/"},{"title":"Building Generalist Humanoid Capabilities with NVIDIA Isaac GR00T N1.6 Using a Sim-to-Real Workflow | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n1-6-using-a-sim-to-real-workflow/"},{"title":"GitHub - nvidia-isaac/WBC-AGILE: Whole Body Control for humanoids: AGILE","url":"https://github.com/nvidia-isaac/WBC-AGILE"},{"title":"NVlabs/GR00T-WholeBodyControl | DeepWiki","url":"https://deepwiki.com/NVlabs/GR00T-WholeBodyControl"},{"title":"GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub","url":"https://github.com/NVIDIA/Isaac-GR00T"},{"title":"Control Paradigms | NVlabs/GR00T-WholeBodyControl | DeepWiki","url":"https://deepwiki.com/NVlabs/GR00T-WholeBodyControl/1.2-key-features"},{"title":"GR00T-WholeBodyControl/README.md at main · NVlabs/GR00T-WholeBodyControl","url":"https://github.com/NVlabs/GR00T-WholeBodyControl/blob/main/README.md"},{"title":"Advancing Humanoid Robot Sight and Skill Development with NVIDIA Project GR00T | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/advancing-humanoid-robot-sight-and-skill-development-with-nvidia-project-gr00t/"},{"title":"Teleoperation and Imitation Learning with Isaac Lab Mimic — Isaac Lab Documentation","url":"https://isaac-sim.github.io/IsaacLab/main/source/overview/imitation-learning/teleop_imitation.html"}]

Based on the search results, here's information about the technologies and frameworks mentioned in your query:

## AGILE Framework

AGILE provides a comprehensive reinforcement learning framework for training whole-body control policies with validated sim-to-real transfer capabilities, built on NVIDIA Isaac Lab to enable researchers and practitioners to develop loco-manipulation behaviors for humanoid robots. This modular architecture represents a current implementation focus for loco-manipulation tasks, particularly enabling teleoperation where the upper body responds to external commands while maintaining stable locomotion.

## Isaac Lab Integration

The sim-to-real pipeline leverages whole-body reinforcement learning in NVIDIA Isaac Lab and synthetic-data-driven navigation with COMPASS to train robust, generalized policies for locomotion, manipulation, and navigation.

## SONIC Whole-Body Control

SONIC is a humanoid behavior foundation model that gives robots a core set of motor skills learned from large-scale human motion data, using motion tracking as a scalable training task to enable a single unified policy to produce natural, whole-body movement and support behaviors from walking and crawling to teleoperation and multi-modal control.

## WBC Configuration in 2026

GEAR-SONIC was released on February 19, 2026 with pretrained checkpoints, C++ inference, VR teleoperation, and documentation. An end-to-end VLA workflow on G1 was released on May 7, 2026, allowing collection of teleop data, fine-tuning of Isaac-GR00T N1.7, and deployment with SONIC whole-body control.

GR00T N1.7 supports whole-body humanoid control via the UNITREE_G1_SONIC embodiment tag and the GEAR-SONIC controller, where the VLA predicts compact latent action tokens that a learned whole-body controller decodes into full-body joint commands including legs, arms, and hands.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b67a7bd-5a45-4f2a-aa40-acaaff993d24",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "2d0b559d-62df-4a7b-a154-921a6b72c1e9",
  "toolUseResult": {
    "query": "AGILE humanoid loco-manipulation Isaac Lab SONIC GR00T WBC configuration 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GSpe3oUyviYefnYv4aMNv1",
        "content": [
          {
            "title": "GitHub - NVlabs/GR00T-WholeBodyControl: Welcome to GR00T Whole-Body Control (WBC)! This is a unified platform for developing and deploying advanced humanoid controllers. This includes: Decoupled WBC models used in NVIDIA Isaac-Gr00t, Gr00t N1.5 and N1.6 and GEAR-SONIC · GitHub",
            "url": "https://github.com/NVlabs/GR00T-WholeBodyControl"
          },
          {
            "title": "GR00T-WholeBodyControl Documentation — GR00T-WholeBodyControl Documentation",
            "url": "https://nvlabs.github.io/GR00T-WholeBodyControl/"
          },
          {
            "title": "Building Generalist Humanoid Capabilities with NVIDIA Isaac GR00T N1.6 Using a Sim-to-Real Workflow | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n1-6-using-a-sim-to-real-workflow/"
          },
          {
            "title": "GitHub - nvidia-isaac/WBC-AGILE: Whole Body Control for humanoids: AGILE",
            "url": "https://github.com/nvidia-isaac/WBC-AGILE"
          },
          {
            "title": "NVlabs/GR00T-WholeBodyControl | DeepWiki",
            "url": "https://deepwiki.com/NVlabs/GR00T-WholeBodyControl"
          },
          {
            "title": "GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub",
            "url": "https://github.com/NVIDIA/Isaac-GR00T"
          },
          {
            "title": "Control Paradigms | NVlabs/GR00T-WholeBodyControl | DeepWiki",
            "url": "https://deepwiki.com/NVlabs/GR00T-WholeBodyControl/1.2-key-features"
          },
          {
            "title": "GR00T-WholeBodyControl/README.md at main · NVlabs/GR00T-WholeBodyControl",
            "url": "https://github.com/NVlabs/GR00T-WholeBodyControl/blob/main/README.md"
          },
          {
            "title": "Advancing Humanoid Robot Sight and Skill Development with NVIDIA Project GR00T | NVIDIA Technical Blog",
            "url": "https://developer.nvidia.com/blog/advancing-humanoid-robot-sight-and-skill-development-with-nvidia-project-gr00t/"
          },
          {
            "title": "Teleoperation and Imitation Learning with Isaac Lab Mimic — Isaac Lab Documentation",
            "url": "https://isaac-sim.github.io/IsaacLab/main/source/overview/imitation-learning/teleop_imitation.html"
          }
        ]
      },
      "Based on the search results, here's information about the technologies and frameworks mentioned in your query:\n\n## AGILE Framework\n\nAGILE provides a comprehensive reinforcement learning framework for training whole-body control policies with validated sim-to-real transfer capabilities, built on NVIDIA Isaac Lab to enable researchers and practitioners to develop loco-manipulation behaviors for humanoid robots. This modular architecture represents a current implementation focus for loco-manipulation tasks, particularly enabling teleoperation where the upper body responds to external commands while maintaining stable locomotion.\n\n## Isaac Lab Integration\n\nThe sim-to-real pipeline leverages whole-body reinforcement learning in NVIDIA Isaac Lab and synthetic-data-driven navigation with COMPASS to train robust, generalized policies for locomotion, manipulation, and navigation.\n\n## SONIC Whole-Body Control\n\nSONIC is a humanoid behavior foundation model that gives robots a core set of motor skills learned from large-scale human motion data, using motion tracking as a scalable training task to enable a single unified policy to produce natural, whole-body movement and support behaviors from walking and crawling to teleoperation and multi-modal control.\n\n## WBC Configuration in 2026\n\nGEAR-SONIC was released on February 19, 2026 with pretrained checkpoints, C++ inference, VR teleoperation, and documentation. An end-to-end VLA workflow on G1 was released on May 7, 2026, allowing collection of teleop data, fine-tuning of Isaac-GR00T N1.7, and deployment with SONIC whole-body control.\n\nGR00T N1.7 supports whole-body humanoid control via the UNITREE_G1_SONIC embodiment tag and the GEAR-SONIC controller, where the VLA predicts compact latent action tokens that a learned whole-body controller decodes into full-body joint commands including legs, arms, and hands."
    ],
    "durationSeconds": 8.697144142999983
  },
  "sourceToolAssistantUUID": "7b67a7bd-5a45-4f2a-aa40-acaaff993d24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-10T19:31:31.972Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me synthesize my findings and think deeply about the revision.

**Key findings from research:**

1. **CoRL 2026 deadline**: Abstract May 26, Paper May 29 — that's 16 days for abstract, 19 days for paper. Very tight.

2. **Humanoids 2026 deadline**: July 24, 2026 — 75 days. This is correct per the reviewer. The original proposal said June 30, which appears to be incorrect.

3. **RoboGene** (arXiv:2602.16444, Feb 2026): Uses three LLM-based evaluators (physical feasibility, novelty, constraint adherence) + LFU diversity sampling + self-reflection. 

RoboGene generates 18K trajectories for VLA pre-training across single-arm, dual-arm, and mobile manipulation platforms, but differs from CompLocoGen in using LLM-based post-hoc evaluation rather than learned prediction, targeting general manipulation instead of humanoid locomotion-manipulation, and handling multi-stage tasks without formal grammar or transition dynamics.

4. **FATE** (arXiv:2603.01505, March 2026): Closed-loop feasibility-aware task generation with VLM auditor handling both static and dynamic phases plus active...

FATE generates 352 tasks with 92.1% feasibility for RidgebackFranka in Isaac Sim, using VLM-based auditing instead of learned prediction and checking feasibility per-task rather than compositionally, while targeting mobile manipulation instead of humanoid locomotion.

5. **Ψ₀** (arXiv:2603.12263, March 2026, RSS 2026): A foundation model for humanoid loco-manipulation trained through staged VLM pre-training on human video followed by robot data fine-tuning, achieving 40%+ improvement over GR00T-N1.6 and learning new skills from just 80 trajectories—this is the downstream consumer of the generated training data.

6. **Generative Skill Chaining**: Confirmed CoRL 2023 (not 2024).

7. **GR00T-WBC/SONIC**: GEAR-SONIC released in February 2026, GR00T N1.7 in May 2026, with the end-to-end VLA workflow released May 7, 2026.

Now I'm seeing the core tension: five rounds of revision with scores stuck between 3.2 and 3.5, and the real bottleneck is the scope-timeline mismatch. The reviewer keeps questioning whether the ambition fits the venue, forcing a choice between a minimal CoRL proof-of-concept with just three primitives and bootstrap TFN versus a full humanoids paper with seven primitives, active learning, and comprehensive ablations.

From a reviewer's lens, a stripped-down CoRL submission with only three primitives and no active learning would feel incomplete—it wouldn't actually demonstrate the TFN's core strength, which is scalability. The humanoids venue makes more sense: it's specifically designed for humanoid loco-manipulation work, values both systems and algorithmic contributions, and the July 24 deadline gives us 75 days, which is realistic. I'm leaning toward committing to Humanoids 2026 as the primary target with the full evaluation, since the TFN contribution genuinely requires that scope to be convincing.

The core idea itself is sound—grammar-based task generation with a learned transition function for compositional feasibility prediction is novel, and nothing in the existing work (RoboGene, FATE) does this with GNNs for humanoid manipulation. The stagnation we've been hitting comes down to venue indecision, missing related work surfacing repeatedly, and some overclaiming about generalization—all of which are fixable with a clear commitment and tighter framing.

I'm going to lock in Humanoids 2026 as the target, explicitly explain why CoRL 2026 is too tight and would result in a weaker paper, and add CoRL 2027 as a fallback for the extended version. I'll integrate the missing related work, reframe the TFN generalization as an experimental hypothesis rather than a guarantee, and clean up the minor errors like the deadline date and citation fixes. 5. **Tighten approach**: Clearer separation of what's novel vs. what's engineering.

Let me write the JSON now.

Actually, let me reconsider the venue question more carefully. The user "explicitly targets CoRL 2026." But with 16 days to abstract and 19 days to paper, can we make a meaningful CoRL submission? A CoRL paper needs 8 pages + experiments, and even with 3 primitives, the timeline is extremely tight—grammar definition, TFN architecture with bootstrap training, SONIC integration, composition generation and simulation, downstream evaluation, and writing would consume nearly all 16 days with zero buffer. This is technically possible only if the researcher already has Isaac Lab and SONIC set up and keeps scope minimal, but the core claim of "TFN predicts transition feasibility" with just 3 primitives and no active learning would likely be too thin for a competitive venue like CoRL.

I think the better strategy is to target Humanoids 2026 in July as the primary venue—that gives room for a full paper with 7 primitives, active learning, and proper ablations—while positioning CoRL 2026 as a workshop submission if a relevant one exists, and treating CoRL 2027 as a stretch goal once real-robot experiments are in place. I'll justify this choice to the reviewer by explaining why Humanoids is the stronger fit. I should consider whether RoboGene could work as a baseline—the reviewer suggested framing it that way. RoboGene uses LLM-based feasibility evaluators, so I could compare our TFN-based prediction approach against LLM evaluation on compositional humanoid tasks. The domain mismatch is real (RoboGene targets tabletop and mobile manipulation), but I could adapt their LLM evaluator approach as a baseline method within our humanoid setting, which would make for a solid experimental comparison.

Now I have a clearer direction: present Humanoids as the primary target with a full paper, offer CoRL 2026 workshop as an optional lightweight parallel track if the researcher wants to maintain CoRL visibility, and position CoRL 2027 for the more complete learning-theoretic version. But I'm realizing the reviewer's mention of CoRL 2026 might be based on a constraint I'm not seeing in the original proposal—the stated targets were Humanoids 2026, ICRA 2027, and CoRL 2027, with no explicit CoRL 2026 deadline mentioned.

The core idea itself is solid. The TFN genuinely offers something new for humanoid loco-manipulation—learned upfront feasibility prediction that's faster than simulation, compositional structure that captures transitions rather than full tasks, and active learning that targets the uncertainty frontier. These are real advantages over RoboGene and FATE's post-hoc evaluation approaches. The stagnation around 3.2-3.5 probably stems from the venue tension creating circular revisions rather than any fundamental flaw in the approach.

To break through this plateau, I need to make decisive moves: lock in the venue strategy, add the missing related work comprehensively, dial back the claims to testable hypotheses, simplify the approach to reduce noise, and include a RoboGene-adapted baseline for comparison. This is a major revision because the venue shift and expanded related work will reframe the entire paper.

For the timeline, I'm working toward Humanoids 2026 in July, which gives me 75 days from mid-May. The manual track needs 7-8 weeks, human-in-loop fits in 6-7 weeks, and the automated approach should take 3-4 weeks with proper setup.

If I pivot to a minimal CoRL 2026 version instead, I'd have only about 16 days to abstract and 19 to paper, which means stripping down to three core primitives, a bootstrapped TFN with 200 rollouts, three composition evaluations, and no ablations—roughly 40-50 H100-hours of compute. It's tight but feasible.

Now I'm structuring the JSON carefully: establishing that RoboGene and FATE already handle feasibility-aware generation, then showing how they don't address compositional humanoid locomotion-manipulation; expanding the opportunity gap to include these existing approaches; and adding detailed coverage of RoboGene, FATE, and Ψ₀ to the landscape section.

For the approach, I'm reframing TFN generalization as a core hypothesis and including a RoboGene-adapted baseline for comparison. The resource estimate needs to present both tracks—Humanoids 2026 as the primary 75-day path with a comfortable timeline, plus a justified discussion of why the CoRL 2026 minimal would produce weaker results, with contingency for TFN generalization challenges. I'm targeting Humanoids 2026 in July as primary and CoRL 2027 as secondary, and I need to add the missing references while fixing the Generative Skill Chaining venue.

Writing this out now...

Actually, I have what I need. The recent releases like GEAR-SONIC and GR00T N1.7 plus the May VLA workflow strengthen the infrastructure maturity for CompLocoGen, and UNITREE_G1_SONIC is directly applicable. I'm going with the official July 24 deadline for Humanoids 2026 since that's what the website confirms, not the June 30 date mentioned in the original feedback.

Now I'm drafting the full revision as a substantial JSON with change_type marked as "major" due to the venue strategy shift, expanded related work, and sharpened claims. I'm updating the core problem to acknowledge RoboGene and FATE while clarifying the gap around compositional humanoid loco-manipulation with learned transition dynamics. The opportunity section gets revised to highlight how RoboGene uses LLM-based evaluation on 18K tasks without humanoid-specific dynamics, FATE achieves 92.1% FTR but relies on VLM evaluation for single mobile manipulator tasks, and Ψ₀ needs diverse training data—none of which provide grammar-structured compositional generation with learned transitions for humanoid systems. The landscape section expands significantly with dedicated coverage of RoboGene, FATE, and Ψ₀.

For the approach, I'm reframing TFN generalization as a core hypothesis, adding a contingency budget, introducing RoboGene-adapted as an eighth baseline, keeping the 7 primitives and active learning pipeline intact, and updating references to GEAR-SONIC and the latest whole-body control methods. The resource estimate commits to Humanoids 2026 as the primary target with 75 days until July 24, justifies why CoRL 2026 alone would be insufficient, maintains the ~200 H100-hour budget, and adds 10-20 hours of contingency for TFN generalization validation. The target venues are Humanoids 2026 as primary, CoRL 2027 as secondary for an extended version, and ICRA 2027 as an alternative.

Now I'm adding the key references—RoboGene, FATE, and Ψ₀—while fixing the Generative Skill Chaining formulation and updating the SONIC citations to GEAR-SONIC throughout. I'll structure this as a comprehensive JSON document to capture all the details.

Writing the JSON structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d0b559d-62df-4a7b-a154-921a6b72c1e9",
  "isSidechain": false,
  "requestId": "req_011CauScfQfVKsGBJwqSXpjP",
  "type": "assistant",
  "uuid": "d257219b-e231-4dbf-853e-42e1e094fce1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zqUbHm82RxahyJAm6Cmsx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 42551,
      "output_tokens": 4240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4240,
          "cache_read_input_tokens": 42551,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1226
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-10T19:31:37.618Z_

Now I have all the research I need. Let me synthesize the findings before drafting the revision.

**Key findings:**
- **CoRL 2026**: Abstract May 26 (16 days), Paper May 29 (19 days). 8-page papers. Extremely tight.
- **Humanoids 2026**: Paper deadline July 24 (75 days), not June 30. Confirmed via official website.
- **RoboGene**: 3 LLM-based evaluators (physical feasibility, novelty, constraint adherence) + LFU diversity sampling. 18K trajectories, single/dual-arm/mobile manipulation. Handles multi-stage tasks but without formal grammar or learned transition dynamics.
- **FATE**: Static + dynamic VLM auditing with active repair. 352 tasks, 92.1% FTR. RidgebackFranka in Isaac Sim. Per-task feasibility, not compositional.
- **Ψ₀**: RSS 2026, staged VLM pre-training, 40%+ over GR00T-N1.6. Downstream consumer of training data.
- **Generative Skill Chaining**: Confirmed CoRL 2023 (not 2024).
- **GEAR-SONIC**: Released Feb 2026, GR00T N1.7 end-to-end VLA workflow released May 7, 2026.

The stagnation at 3.2-3.5 is from unresolved venue tension, missing related work each round, and overclaiming. The core idea (grammar + learned TFN) is genuinely novel — RoboGene/FATE validate the importance of feasibility-aware generation but use fundamentally different mechanisms. This calls for a decisive major revision: commit to Humanoids, add all missing work, reframe claims as hypotheses.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d257219b-e231-4dbf-853e-42e1e094fce1",
  "isSidechain": false,
  "requestId": "req_011CauScfQfVKsGBJwqSXpjP",
  "type": "assistant",
  "uuid": "ebec1885-6599-4989-844b-a77e9848fb75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zqUbHm82RxahyJAm6Cmsx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 42551,
      "output_tokens": 4240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4240,
          "cache_read_input_tokens": 42551,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1226
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-10T19:31:38.368Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LPjL8SvnLwBpf1H21UADEH`</summary>

```json
{
  "query": "SkillBlender arXiv 2506.09366 compositional skill humanoid G1 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebec1885-6599-4989-844b-a77e9848fb75",
  "isSidechain": false,
  "requestId": "req_011CauScfQfVKsGBJwqSXpjP",
  "type": "assistant",
  "uuid": "48bc5fa6-c67f-44cf-96ed-8e6776b6fdc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zqUbHm82RxahyJAm6Cmsx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 42551,
      "output_tokens": 4240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4240,
          "cache_read_input_tokens": 42551,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1226
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 65_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Co…",
  "leafUuid": "48bc5fa6-c67f-44cf-96ed-8e6776b6fdc1",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise CoRL 2026 scope or justify Humanoids 2026 timeline",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Tool result

_source line 67 · 2026-05-10T19:31:47.842Z_

<details><summary>↩ Tool result · `toolu_01LPjL8SvnLwBpf1H21UADEH`</summary>

```text
Web search results for query: "SkillBlender arXiv 2506.09366 compositional skill humanoid G1 2025"

Links: [{"title":"SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://arxiv.org/html/2506.09366v1"},{"title":"[2506.09366] SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://arxiv.org/abs/2506.09366"},{"title":"GitHub - Humanoid-SkillBlender/SkillBlender: Official implementation of SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://github.com/Humanoid-SkillBlender/SkillBlender"},{"title":"Paper page - SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://huggingface.co/papers/2506.09366"},{"title":"SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://psi-lab.ai/SkillBlender-web/"},{"title":"[Literature Review] SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending","url":"https://www.themoonlight.io/en/review/skillblender-towards-versatile-humanoid-whole-body-loco-manipulation-via-skill-blending"},{"title":"SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2506.09366"},{"title":"VisualMimic Visual Humanoid Loco-Manipulation via Motion Tracking and Generation","url":"https://arxiv.org/html/2509.20322v1"},{"title":"Robotics Jun 2025","url":"http://arxiv.org/list/cs.RO/2025-06?skip=225&show=1000"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=3150&show=500"}]

Based on the search results, here's what I found about SkillBlender (arXiv 2506.09366):

## Overview

SkillBlender is a novel hierarchical reinforcement learning framework for versatile humanoid loco-manipulation. It first pretrains goal-conditioned task-agnostic primitive skills, and then dynamically blends these skills to accomplish complex loco-manipulation tasks with minimal task-specific reward engineering.

## Key Components

**Primitive Skills:** SkillBench provides 4 primitive skills: Walking, Reaching, Squatting, and Stepping.

**Humanoid Embodiments:** The system supports the 19-DoF Unitree H1, 21-DoF Unitree G1, and 21-DoF Unitree H1-2. The Unitree G1 is a smaller humanoid model, standing around 1.2 meters tall, and features an additional roll DoF on each ankle, increasing the total DoF count to 21.

**Benchmark Tasks:** SkillBench includes eight challenging whole-body loco-manipulation tasks categorized by difficulty (Easy: FarReach, ButtonPress, CabinetClose; Medium: FootballShoot, BoxPush, PackageLift; Hard: BoxTransfer, PackageCarry).

## Performance

SkillBlender outperforms PPO by a large margin, producing more accurate and natural movements, demonstrating the framework's superiority across multiple humanoid embodiments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48bc5fa6-c67f-44cf-96ed-8e6776b6fdc1",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "bca8b603-376f-465a-bcb8-afccfb41b875",
  "toolUseResult": {
    "query": "SkillBlender arXiv 2506.09366 compositional skill humanoid G1 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FiQYCyUb1SrzYpm6ett7Pw",
        "content": [
          {
            "title": "SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://arxiv.org/html/2506.09366v1"
          },
          {
            "title": "[2506.09366] SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://arxiv.org/abs/2506.09366"
          },
          {
            "title": "GitHub - Humanoid-SkillBlender/SkillBlender: Official implementation of SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://github.com/Humanoid-SkillBlender/SkillBlender"
          },
          {
            "title": "Paper page - SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://huggingface.co/papers/2506.09366"
          },
          {
            "title": "SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://psi-lab.ai/SkillBlender-web/"
          },
          {
            "title": "[Literature Review] SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending",
            "url": "https://www.themoonlight.io/en/review/skillblender-towards-versatile-humanoid-whole-body-loco-manipulation-via-skill-blending"
          },
          {
            "title": "SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2506.09366"
          },
          {
            "title": "VisualMimic Visual Humanoid Loco-Manipulation via Motion Tracking and Generation",
            "url": "https://arxiv.org/html/2509.20322v1"
          },
          {
            "title": "Robotics Jun 2025",
            "url": "http://arxiv.org/list/cs.RO/2025-06?skip=225&show=1000"
          },
          {
            "title": "Machine Learning Jun 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-06?skip=3150&show=500"
          }
        ]
      },
      "Based on the search results, here's what I found about SkillBlender (arXiv 2506.09366):\n\n## Overview\n\nSkillBlender is a novel hierarchical reinforcement learning framework for versatile humanoid loco-manipulation. It first pretrains goal-conditioned task-agnostic primitive skills, and then dynamically blends these skills to accomplish complex loco-manipulation tasks with minimal task-specific reward engineering.\n\n## Key Components\n\n**Primitive Skills:** SkillBench provides 4 primitive skills: Walking, Reaching, Squatting, and Stepping.\n\n**Humanoid Embodiments:** The system supports the 19-DoF Unitree H1, 21-DoF Unitree G1, and 21-DoF Unitree H1-2. The Unitree G1 is a smaller humanoid model, standing around 1.2 meters tall, and features an additional roll DoF on each ankle, increasing the total DoF count to 21.\n\n**Benchmark Tasks:** SkillBench includes eight challenging whole-body loco-manipulation tasks categorized by difficulty (Easy: FarReach, ButtonPress, CabinetClose; Medium: FootballShoot, BoxPush, PackageLift; Hard: BoxTransfer, PackageCarry).\n\n## Performance\n\nSkillBlender outperforms PPO by a large margin, producing more accurate and natural movements, demonstrating the framework's superiority across multiple humanoid embodiments."
    ],
    "durationSeconds": 9.469483581000008
  },
  "sourceToolAssistantUUID": "48bc5fa6-c67f-44cf-96ed-8e6776b6fdc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-10T19:31:52.362Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Di6yfhzbbA4Lbqjwg4UJWc`</summary>

```json
{
  "query": "\"feasibility-aware\" OR \"feasibility prediction\" task generation robotics simulation 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bca8b603-376f-465a-bcb8-afccfb41b875",
  "isSidechain": false,
  "requestId": "req_011CauSkyJAVkLSQpK4uwmc8",
  "type": "assistant",
  "uuid": "c261f86c-71ba-4009-8807-557d574c38ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PKbYBmjegdiULHFC1dxEqh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5210,
      "cache_read_input_tokens": 43777,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5210,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 43777,
          "cache_creation_input_tokens": 5210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5210
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-10T19:31:59.800Z_

<details><summary>↩ Tool result · `toolu_01Di6yfhzbbA4Lbqjwg4UJWc`</summary>

```text
Web search results for query: ""feasibility-aware" OR "feasibility prediction" task generation robotics simulation 2026 arXiv"

Links: [{"title":"FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula","url":"https://arxiv.org/html/2603.01505"},{"title":"Generative Artificial Intelligence in Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2503.03464v1"},{"title":"KiGRAS: Kinematic-Driven Generative Model for Realistic Agent Simulation","url":"https://arxiv.org/html/2407.12940v1"},{"title":"Robotics Mar 2025","url":"https://arxiv.org/list/cs.RO/2025-03?skip=275&show=2000"},{"title":"A Step Toward World Models: A Survey on Robotic Manipulation","url":"https://arxiv.org/html/2511.02097v1"},{"title":"Uncertainty-aware Planning with Inaccurate Models for Robotized Liquid Handling","url":"https://arxiv.org/pdf/2507.20861"},{"title":"GitHub - GT-RIPL/Awesome-LLM-Robotics: A comprehensive list of papers using large language/multi-modal models for Robotics/RL, including papers, codes, and related websites · GitHub","url":"https://github.com/GT-RIPL/Awesome-LLM-Robotics"},{"title":"H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model","url":"https://arxiv.org/html/2602.11291v2"},{"title":"Safety Aware Task Planning via Large Language Models in Robotics","url":"https://arxiv.org/html/2503.15707"},{"title":"Machine Learning Jun 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-06?skip=1900&show=2000"}]

Based on the search results, I found a highly relevant paper for your query:

## FATE: Closed-Loop Feasibility-Aware Task Generation

FATE (Feasibility-Aware Task gEneration) is a closed-loop, self-correcting framework that reimagines task generation as an iterative validation-and-refinement process. Unlike conventional methods that decouple generation and verification into discrete stages, FATE embeds a generalist embodied agent directly into the generation loop to proactively guarantee the physical groundedness of the resulting curriculum.

This addresses a critical limitation where recent breakthroughs in generative simulation have used Large Language Models (LLMs) to generate diverse robotic task curricula, yet these open-loop paradigms frequently produce linguistically coherent but physically infeasible goals.

**Technical Approach:**

FATE instantiates a sequential auditing pipeline: it first validates static scene attributes (e.g., object affordances, layout compatibility) and subsequently verifies execution feasibility via simulated embodied interaction. It decomposes feasibility assessment into two sub-metrics: the Scene Validity Rate (SVR) measures perceptual alignment via BLIP-2 semantic coherence and geometric checks; the Execution Validity Rate (EVR) assesses dynamic feasibility using a Simulation Oracle to verify successful physical rollouts with MPC and RL solvers.

**Publication:**
This paper was published on arXiv on March 2, 2026 (arxiv.org/html/2603.01505) and directly addresses feasibility-aware task generation for robotics simulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c261f86c-71ba-4009-8807-557d574c38ae",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "27a21f83-ba7a-45a3-bb95-04da9cca5002",
  "toolUseResult": {
    "query": "\"feasibility-aware\" OR \"feasibility prediction\" task generation robotics simulation 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_016vysEWG56bSMZdFmV1fvWq",
        "content": [
          {
            "title": "FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula",
            "url": "https://arxiv.org/html/2603.01505"
          },
          {
            "title": "Generative Artificial Intelligence in Robotic Manipulation: A Survey",
            "url": "https://arxiv.org/html/2503.03464v1"
          },
          {
            "title": "KiGRAS: Kinematic-Driven Generative Model for Realistic Agent Simulation",
            "url": "https://arxiv.org/html/2407.12940v1"
          },
          {
            "title": "Robotics Mar 2025",
            "url": "https://arxiv.org/list/cs.RO/2025-03?skip=275&show=2000"
          },
          {
            "title": "A Step Toward World Models: A Survey on Robotic Manipulation",
            "url": "https://arxiv.org/html/2511.02097v1"
          },
          {
            "title": "Uncertainty-aware Planning with Inaccurate Models for Robotized Liquid Handling",
            "url": "https://arxiv.org/pdf/2507.20861"
          },
          {
            "title": "GitHub - GT-RIPL/Awesome-LLM-Robotics: A comprehensive list of papers using large language/multi-modal models for Robotics/RL, including papers, codes, and related websites · GitHub",
            "url": "https://github.com/GT-RIPL/Awesome-LLM-Robotics"
          },
          {
            "title": "H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model",
            "url": "https://arxiv.org/html/2602.11291v2"
          },
          {
            "title": "Safety Aware Task Planning via Large Language Models in Robotics",
            "url": "https://arxiv.org/html/2503.15707"
          },
          {
            "title": "Machine Learning Jun 2024",
            "url": "https://web3.arxiv.org/list/cs.LG/2024-06?skip=1900&show=2000"
          }
        ]
      },
      "Based on the search results, I found a highly relevant paper for your query:\n\n## FATE: Closed-Loop Feasibility-Aware Task Generation\n\nFATE (Feasibility-Aware Task gEneration) is a closed-loop, self-correcting framework that reimagines task generation as an iterative validation-and-refinement process. Unlike conventional methods that decouple generation and verification into discrete stages, FATE embeds a generalist embodied agent directly into the generation loop to proactively guarantee the physical groundedness of the resulting curriculum.\n\nThis addresses a critical limitation where recent breakthroughs in generative simulation have used Large Language Models (LLMs) to generate diverse robotic task curricula, yet these open-loop paradigms frequently produce linguistically coherent but physically infeasible goals.\n\n**Technical Approach:**\n\nFATE instantiates a sequential auditing pipeline: it first validates static scene attributes (e.g., object affordances, layout compatibility) and subsequently verifies execution feasibility via simulated embodied interaction. It decomposes feasibility assessment into two sub-metrics: the Scene Validity Rate (SVR) measures perceptual alignment via BLIP-2 semantic coherence and geometric checks; the Execution Validity Rate (EVR) assesses dynamic feasibility using a Simulation Oracle to verify successful physical rollouts with MPC and RL solvers.\n\n**Publication:**\nThis paper was published on arXiv on March 2, 2026 (arxiv.org/html/2603.01505) and directly addresses feasibility-aware task generation for robotics simulation."
    ],
    "durationSeconds": 7.434586443000008
  },
  "sourceToolAssistantUUID": "c261f86c-71ba-4009-8807-557d574c38ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-10T19:32:03.272Z_

Good — I've confirmed there's nothing else major missing. Now let me compose the full revised idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27a21f83-ba7a-45a3-bb95-04da9cca5002",
  "isSidechain": false,
  "requestId": "req_011CauSmrMj3titqX3ee1QtM",
  "type": "assistant",
  "uuid": "2f3fcb5c-c428-43e4-958d-c3b1aedef070",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167zwUN8QB7sAJEPR7gjqdT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 48987,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 48987,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 951
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-10T19:32:03.443Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019vHbDdXzjvtaugAVJaub3S`</summary>

```json
{
  "query": "CoRL 2026 workshops call for workshop papers deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f3fcb5c-c428-43e4-958d-c3b1aedef070",
  "isSidechain": false,
  "requestId": "req_011CauSmrMj3titqX3ee1QtM",
  "type": "assistant",
  "uuid": "2c733b56-0477-4089-a64d-931e7480e0b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167zwUN8QB7sAJEPR7gjqdT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 48987,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 48987,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 951
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-10T19:32:07.349Z_

<details><summary>↩ Tool result · `toolu_019vHbDdXzjvtaugAVJaub3S`</summary>

```text
Web search results for query: "CoRL 2026 workshops call for workshop papers deadline"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026 - Call for Workshops | Danfei Xu","url":"https://www.linkedin.com/posts/danfei-xu-94522133_corl-2026-call-for-workshops-activity-7458261431461965824-yH7b"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"}]

Based on the search results, I found information about CoRL 2026. The call for workshops is now available as of April 29. However, the search results don't contain specific information about the workshop papers deadline. 

The main conference paper submission deadline is May 28, 2026 (AoE), but for specific details about the workshop papers deadline, you would need to visit the official CoRL 2026 workshops page directly. CoRL 2026 will be held in Austin, Texas, US.

Would you like me to search for more specific information about the workshop papers deadline?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c733b56-0477-4089-a64d-931e7480e0b8",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "ed860872-e293-4ed2-85b2-cc023f6cd968",
  "toolUseResult": {
    "query": "CoRL 2026 workshops call for workshop papers deadline",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HSrSGYM8mJs9N49dhP3zQk",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL 2026 - Contributions",
            "url": "https://www.corl.org/contributions"
          },
          {
            "title": "CoRL 2026 - Annoucements",
            "url": "https://www.corl.org/annoucements"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "CoRL 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"
          },
          {
            "title": "CoRL 2026 - Call for Workshops | Danfei Xu",
            "url": "https://www.linkedin.com/posts/danfei-xu-94522133_corl-2026-call-for-workshops-activity-7458261431461965824-yH7b"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf?lang=en"
          }
        ]
      },
      "Based on the search results, I found information about CoRL 2026. The call for workshops is now available as of April 29. However, the search results don't contain specific information about the workshop papers deadline. \n\nThe main conference paper submission deadline is May 28, 2026 (AoE), but for specific details about the workshop papers deadline, you would need to visit the official CoRL 2026 workshops page directly. CoRL 2026 will be held in Austin, Texas, US.\n\nWould you like me to search for more specific information about the workshop papers deadline?"
    ],
    "durationSeconds": 3.900537942999974
  },
  "sourceToolAssistantUUID": "2c733b56-0477-4089-a64d-931e7480e0b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-10T19:32:57.620Z_

<details><summary>Logged reasoning block</summary>

```text
The CoRL 2026 workshops call was just posted (April 29), so workshop paper deadlines are likely in August-September 2026, well after Humanoids. That's not useful for a parallel track.

Now let me compose the complete revised JSON. I have all the information I need.

Let me think carefully about the venue strategy one more time:

Option A: CoRL 2026 minimal (19 days)
- 3 primitives (walk/pick/place)
- Bootstrap TFN only (200 rollouts)
- 3 composition evaluations
- No ablations
- Risk: too thin for competitive venue, likely rejected


- 8-page paper in 19 days with experiments is extremely aggressive

Option B: Humanoids 2026 full (75 days)
- 7 primitives, active learning, full evaluation
- 8 baselines, 3+ ablations
- Proper venue fit (humanoid-specific)
- Comfortable timeline

I'm going to recommend Humanoids 2026 as the primary target since the CoRL minimal scope would be too rushed and underdeveloped for a competitive venue, while Humanoids gives us the time and thematic alignment to do this properly. I'll frame the CoRL option as a contingency if needed.

Now I'm cataloging what's actually changed here: the venue strategy is the biggest shift, but I've also substantially expanded the related work with RoboGene, FATE, and Ψ₀, reframed TFN generalization from an assumption into a testable hypothesis with a fallback plan, and added a new RoboGene-adapted baseline that leverages LLM-based feasibility checking for the humanoid domain. The minor updates are just deadline clarifications and recent model releases. This is definitely a major revision across multiple dimensions.

I'm keeping Qwen 3.6-35B-A3B since it was in the original proposal and the reviewer didn't flag it as outdated. Now I need to sharpen the gap statement to account for these new systems—RoboGene and FATE do handle feasibility-aware generation, but they're missing the compositional grammar structure that makes feasibility learnable from local transition dynamics, the GNN-based prediction approach instead of post-hoc LLM evaluation, and the specific handling of coupled loco-manipulation dynamics at primitive boundaries in humanoids.

For the reviewer's suggestion about RoboGene as a baseline, I can't directly port it to humanoid loco-manipulation since it's designed for tabletop and mobile systems, but I can adapt its core idea—using LLM-based feasibility evaluation instead of our learned GNN predictor. This becomes a clean baseline that isolates the value of learned prediction versus post-hoc LLM filtering while keeping the grammar and primitives constant.

Now I'm structuring the full revision with a clearer problem statement, adding RoboGene and FATE as key comparisons, and laying out a dual-venue strategy with Humanoids 2026 as the primary target and CoRL 2026 as a contingency. I'm also tightening the description and updating the resource estimates to account for the generalization hypothesis testing. Now I'm refining the opportunity section to highlight RoboGene and FATE as key competitive references, and I should also incorporate GR00T N1.7 / GEAR-SONIC since it just released three days ago—that's the most current baseline to position against. The "solid-to-strong" framing still holds, but with clearer differentiation through these references and a more measured hypothesis around TFN generalization, the actual positioning becomes sharper. Let me draft the complete JSON structure now, working through each section methodically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed860872-e293-4ed2-85b2-cc023f6cd968",
  "isSidechain": false,
  "requestId": "req_011CauSnQiQEyaJJ5PxVC6qE",
  "type": "assistant",
  "uuid": "ee867918-a146-435f-82cd-cba1b80543d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwuYNR7EN9tarewPNKNfsf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 49938,
      "output_tokens": 10997,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10997,
          "cache_read_input_tokens": 49938,
          "cache_creation_input_tokens": 670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 670
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 74 · 2026-05-10T19:32:57.622Z_

Now I have all the information needed. Let me compose the full revised idea, addressing every reviewer point.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee867918-a146-435f-82cd-cba1b80543d5",
  "isSidechain": false,
  "requestId": "req_011CauSnQiQEyaJJ5PxVC6qE",
  "type": "assistant",
  "uuid": "54682e57-47a9-4f2d-8ea6-a0ed311f372d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwuYNR7EN9tarewPNKNfsf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 49938,
      "output_tokens": 10997,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10997,
          "cache_read_input_tokens": 49938,
          "cache_creation_input_tokens": 670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 670
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-10T19:37:02.706Z_

<details open><summary>🔧 Tool call — Write · `toolu_01CRd1yruUUAqNKDtt4Mo76N`</summary>

```json
{
  "file_path": "/tmp/revised_idea.json",
  "content": "{\n  \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Compositional Humanoid Loco-Manipulation Task Generation\",\n  \"change_type\": \"major\",\n  \"core_problem\": \"Scaling humanoid loco-manipulation to diverse real-world tasks requires diverse training environments, but every loco-manipulation task in NVIDIA's AGILE/GR00T-WBC ecosystem must be manually specified as a self-contained Isaac Lab configuration file. VIRAL (CVPR 2026) demonstrates composite tasks work but identifies reward engineering as a scaling bottleneck. Eurekaverse (CoRL 2024) pioneered LLM-driven environment curriculum generation but only for single-skill training (quadruped parkour). Recent feasibility-aware task generation systems—RoboGene (arXiv:2602.16444, Feb 2026) and FATE (arXiv:2603.01505, March 2026)—automate diverse task creation with LLM/VLM-based feasibility evaluation, achieving impressive scale (18K trajectories and 92.1% feasible task rate respectively). However, both use post-hoc evaluation (LLM-based evaluators in RoboGene; VLM static+dynamic auditing in FATE) rather than learned predictive models, and neither targets humanoid loco-manipulation where locomotion-manipulation coupling creates emergent failure modes at primitive boundaries. The fundamental challenge is twofold: (1) composing novel multi-stage loco-manipulation tasks from a primitive grammar where inter-primitive dynamics (balance during walk-to-pick transitions, gait adaptation for carry, CoM shifts at primitive boundaries) create failure modes absent from any individual primitive, and (2) efficiently predicting which compositions are dynamically feasible without exhaustive simulation—requiring a learned transition feasibility model that generalizes across primitive types and parameters. How can we combine a physics-informed skill grammar with a learned Transition Feasibility Network to automatically generate diverse, dynamically feasible loco-manipulation task configurations for Isaac Lab?\",\n  \"opportunity\": \"VIRAL (CVPR 2026) achieves 54 consecutive real-world loco-manipulation cycles on G1 but relies entirely on hand-designed stage-weighted rewards—the authors state that 'scaling to the open-ended diversity of daily life remains intractable' via manual reward engineering. Eurekaverse (CoRL 2024) automates environment curriculum generation via LLM code generation with agent-environment co-evolution, achieving superhuman parkour curricula—but operates on single-skill locomotion over terrain, with no manipulation, no inter-primitive coupling, and no compositional task structure. RoboGene (arXiv:2602.16444, Feb 2026) generates 18K trajectories across 900 tasks with LLM-based feasibility evaluators (physical, novelty, constraint adherence) and LFU diversity sampling—but targets tabletop and mobile manipulation (UR-5e, Franka, AgileX) without humanoid-specific dynamics, and its LLM-based evaluation cannot capture the physical coupling between locomotion and manipulation at transition boundaries. FATE (arXiv:2603.01505, March 2026) achieves 92.1% feasible task rate via closed-loop VLM auditing with active repair on a RidgebackFranka mobile manipulator—but evaluates individual tasks post-hoc rather than predicting compositional feasibility upfront, and does not address humanoid whole-body dynamics. DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single demonstration via object-centric replay—producing spatial variations of one task template but not compositionally novel tasks. LHM-Humanoid (arXiv:2508.16943) achieves impressive long-horizon loco-manipulation across 350 scenes but relies on manually designed configurations. Ψ₀ (arXiv:2603.12263, RSS 2026) demonstrates a foundation model for universal humanoid loco-manipulation that outperforms GR00T-N1.6 by 40%+ and can acquire new skills from only 80 trajectories—representing a key downstream consumer that would directly benefit from CompLocoGen's automatically generated diverse training tasks. In the learned composition space, Generative Skill Chaining (CoRL 2023) uses diffusion models for skill precondition/effect chaining, and SCaR (NeurIPS 2024) learns success predictors for sub-task transitions—but both target fixed-base manipulation without dynamics-aware feasibility for whole-body locomotion+manipulation coupling. The gap is precise: no system combines (1) a grammar for compositional loco-manipulation task generation with (2) a learned transition feasibility predictor that captures humanoid-specific coupled dynamics at primitive boundaries—as opposed to post-hoc LLM/VLM evaluation (RoboGene, FATE) or exhaustive simulation—enabling (3) active generation of training data for the AGILE/GR00T-WBC ecosystem and downstream foundation models like Ψ₀.\",\n  \"landscape\": \"**LLM-based environment/curriculum generation**: Eurekaverse (arXiv:2411.01775, CoRL 2024) uses LLM code generation to produce increasingly challenging terrain environments for quadruped parkour, with agent-environment co-evolution over 5 generations. Key paradigm: LLM generates Python terrain functions → train policy → evaluate → feedback to LLM. However, it generates monolithic terrain programs for single-skill locomotion—no manipulation, no inter-primitive dynamics, no compositional task structure. CompLocoGen extends this paradigm to compositional multi-stage loco-manipulation: instead of varying a single environment, we compose multi-primitive task sequences and learn which compositions are dynamically feasible. Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) uses LLM-powered scene generation with RAG-based asset retrieval and DSL code generation to create thousands of diverse environments for humanoid manipulation across 200+ tasks—but lacks formal compositional grammar and shows performance degradation on multi-step tasks (~52% vs ~80% for atomic tasks). **Feasibility-aware task generation (key concurrent work)**: RoboGene (arXiv:2602.16444, Feb 2026) introduces a diversity-driven agentic framework with three specialized LLM-based evaluators: a Physical Feasibility Evaluator (kinematic reachability, physics law compliance), a Novelty Evaluator (object complexity, temporal depth), and a Constraint Adherence Evaluator (scene-task consistency). Its LFU (Least Frequently Used) sampling ensures balanced coverage across under-explored task regions. RoboGene achieves 63.2% object coverage and 91.5% skill coverage across 18K trajectories on UR-5e, Franka, and AgileX platforms. Critical differentiation: RoboGene's feasibility evaluation is LLM-based and post-hoc (generate → evaluate → self-reflect → refine); CompLocoGen's TFN is a learned GNN that predicts feasibility upfront from boundary state features, capturing physical dynamics that LLMs cannot assess (centroidal momentum coupling, contact force propagation at transitions). RoboGene targets general manipulation without humanoid-specific whole-body coupling. We include a RoboGene-adapted baseline (LLM-based feasibility evaluation applied to grammar-generated humanoid compositions) to directly compare learned vs. LLM-based feasibility assessment. FATE (arXiv:2603.01505, March 2026) proposes closed-loop feasibility-aware generation with a sequential VLM auditing pipeline: static alignment (reachability, affordance, physical plausibility) followed by dynamic alignment (execution monitoring with rollback-and-repair). FATE achieves 92.1% feasible task rate on a RidgebackFranka in Isaac Sim. Critical differentiation: FATE evaluates individual task instances post-hoc via VLM perception; CompLocoGen predicts compositional feasibility upfront from learned transition dynamics—the TFN scores an entire primitive sequence in milliseconds without simulation, enabling efficient search over the exponential composition space. FATE's per-task VLM auditing scales linearly with proposals; TFN-based filtering is amortized after training. FATE targets mobile manipulation (7-DoF arm + holonomic base); CompLocoGen targets humanoid whole-body control where locomotion-manipulation coupling is qualitatively different. **LLM-based reward design (per-task optimization)**: STRIDE (arXiv:2502.04692, Feb 2025) automates humanoid locomotion reward design via LLMs, 250% over EUREKA—single-task locomotion only. FORGE (OpenReview 2025) uses multi-agent LLMs for evolutionary reward refinement, 38.5% over EUREKA—single-task. EUREKA (ICLR 2024) established the LLM-to-reward-code paradigm. These solve per-task reward engineering; CompLocoGen solves the orthogonal problem of generating novel task compositions with learned feasibility prediction. **Demonstration-based data generation**: DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single teleoperated demonstration by converting to object-centric representations and replaying under varied initial conditions with a 3-stage pipeline (locomotion → pre-manipulation → manipulation) on Unitree G1. It produces spatial diversity within a fixed task template—not compositional novelty across task structures. CompLocoGen generates qualitatively different training data: novel task compositions (e.g., walk-pick-carry-climb_stairs-place) that no single demonstration could cover. **Learned skill composition approaches**: Generative Skill Chaining (arXiv:2401.03360, CoRL 2023) trains skill-level diffusion models capturing (precondition, parameters, effect) distributions for chaining—fixed-base manipulation only. SCaR (NeurIPS 2024) refines skill chaining with learned success predictors for sub-task transitions. GSC (Robotics & Autonomous Systems, 2024) models skill sets as GNN graphs with transformer-style architecture for skill embeddings. SuperDyno (ICLR 2025 Workshop) learns differentiable neural dynamics for humanoid whole-body control. None of these address composition feasibility for coupled loco-manipulation where locomotion dynamics (balance, gait) interact with manipulation state (load, grasp). CompLocoGen's Transition Feasibility Network operates specifically on the boundary states between loco-manipulation primitives, learning to predict whether locomotion-manipulation coupling will cause failure at transitions. **Sim-to-real composite tasks**: VIRAL/GR00T-VisualSim2Real (CVPR 2026, NVlabs) demonstrates composite loco-manipulation with 54 consecutive real-world cycles—hand-designed tasks. LHM-Humanoid (arXiv:2508.16943, March 2026) learns unified policies across 350 manually designed scenes via RL teacher distillation. FALCON (arXiv:2505.06776, L4DC 2026) demonstrates force-adaptive dual-agent RL for loco-manipulation on real humanoids—hand-designed tasks. **Foundation models as downstream consumers**: Ψ₀ (arXiv:2603.12263, RSS 2026) is an open foundation model for universal humanoid loco-manipulation using staged VLM pre-training on egocentric human video followed by flow-based action expert fine-tuning on robot data. Ψ₀ achieves 40%+ over GR00T-N1.6 and can acquire new loco-manipulation skills from only 80 trajectories. CompLocoGen could serve as an automated training data generator for Ψ₀-class models—the compositionally diverse tasks it produces are precisely the data these foundation models need to achieve broader generalization. WholeBodyVLA (ICLR 2026, arXiv:2512.11047) learns unified latent VLA for whole-body control—another downstream consumer. SkillBlender (arXiv:2506.09366) demonstrates compositional skill blending on G1 with 4 primitive skills (walking, reaching, squatting, stepping) across 8 benchmark tasks—manually specified. CompLocoGen's grammar could automate task generation for SkillBlender-style systems. **Scene graph and compositional approaches**: Scene Graph Atomic Skills (ICRA 2026, Harvard) uses GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition—tabletop manipulation focus. GenManip (CVPR 2025) provides LLM-to-simulation-to-filter for tabletop manipulation. Humanoid Hanoi (arXiv:2602.13850, Feb 2026) demonstrates distribution shift during skill composition requiring data aggregation—directly informs our transition modeling. **The specific gap**: No system combines grammar-structured compositional task generation with a learned transition feasibility predictor for humanoid loco-manipulation. RoboGene and FATE achieve feasibility-aware generation via LLM/VLM post-hoc evaluation for tabletop/mobile manipulation; CompLocoGen introduces learned upfront prediction via GNN that captures humanoid-specific coupled dynamics. Eurekaverse generates single-skill environments; DemoHLM augments single demonstrations; Generative Skill Chaining/GSC learn feasibility for fixed-base manipulation; VIRAL/LHM-Humanoid use manually designed compositions. CompLocoGen uniquely combines: (a) a 7-primitive grammar generating exponentially many task compositions, (b) a GNN-based Transition Feasibility Network that learns loco-manipulation coupling dynamics from few-shot simulation rollouts, and (c) active generation targeting the uncertainty frontier of the feasibility predictor.\",\n  \"approach\": \"We build CompLocoGen as a grammar-structured system that learns transition feasibility for compositional loco-manipulation task generation, producing Isaac Lab-compatible configurations within 220 H100-hours.\\n\\n**Expanded Physics-Informed Skill Grammar (7 Primitives)**: We define a context-free grammar over seven coupled loco-manipulation primitives: walk(target_pos, speed, gait_style), pick(object_id, grasp_type, approach_vector), place(target_pos, placement_constraint), carry(object_id, carry_pose, stability_mode), push(object_id, direction, force_profile), open_door(door_id, handle_type, opening_angle), and squat(target_height, duration, stability_mode). Each primitive has typed spatial parameters, structural preconditions/postconditions, and a boundary state specification (the distribution of robot states—CoM position/velocity, joint configurations, contact states, grasp forces—at primitive entry/exit). The 7-primitive grammar produces 7^L valid structural sequences of length L (before feasibility filtering). For L=3-5 (typical loco-manipulation tasks), this yields 343-16,807 structural compositions. With parameter variation (3-5 settings per typed parameter), the effective task space is 10^4-10^6 unique configurations. Structural filtering (precondition/postcondition satisfaction) reduces this by ~60%; dynamic feasibility filtering further reduces by an experimentally measured factor—quantifying this reduction IS the key experimental result.\\n\\n**Transition Feasibility Network (TFN) — Core Algorithmic Contribution**: Instead of relying on analytical physics predicates (ZMP, centroidal dynamics) or post-hoc LLM/VLM evaluation (as in RoboGene and FATE), we introduce a GNN-based Transition Feasibility Network that learns to predict composition success probability from primitive boundary states. Architecture: Each primitive instance is a node with features encoding (primitive type, spatial parameters, expected boundary state statistics). Edges connect consecutive primitives in the composition. A message-passing GNN (3 layers, 128-dim) processes the composition graph and outputs per-edge transition feasibility scores ∈ [0,1] plus an overall composition feasibility score. The TFN's advantages over alternative feasibility approaches: (a) vs. analytical predicates: captures non-obvious interaction effects that simplified models miss (e.g., arm momentum during open_door affecting walking balance), improves with data rather than requiring manual engineering per primitive type; (b) vs. LLM-based evaluation (RoboGene-style): provides calibrated continuous scores rather than binary judgments, runs in milliseconds rather than requiring LLM API calls per composition, captures physical dynamics (centroidal momentum, contact forces) that language models cannot assess; (c) vs. VLM-based auditing (FATE-style): predicts upfront rather than evaluating post-hoc, handles compositional structure (scores full sequences via message-passing) rather than per-task evaluation; (d) vs. monolithic learned models: the grammar structure means it only needs to learn local transition dynamics (O(P^2) transition types for P primitives = 49 for 7 primitives), not global task success from all possible sequences (exponential in length).\\n\\n**TFN Training — Three-Phase Protocol**: (1) Bootstrap: Seed the TFN with ~200 simulation rollouts (50 per transition type for the 4 most common transitions: walk→pick, pick→carry, carry→walk, walk→place) using analytical predicates to stratify sampling across feasible/infeasible boundary. (2) Active Learning: Use TFN uncertainty (MC-dropout variance) to identify which transition types and parameter regions have highest prediction uncertainty. Allocate simulation budget preferentially to these uncertain regions. After each batch of 50 rollouts, retrain TFN. (3) Generalization Testing: We hypothesize that primitive-type-agnostic physical features (CoM velocity, contact forces, joint torques at boundaries) enable few-shot transfer to novel primitive types (push, open_door, squat). Quantifying the number of rollouts needed per novel primitive type to achieve reliable prediction (target: >85% AUROC) IS a key experimental result, not a design assumption. We budget 20-30 rollouts per new transition type as an optimistic starting point, with 10-20 additional H100-hours of contingency compute if generalization requires more data. If few-shot transfer fails entirely, we fall back to full active learning for all 7 primitives (~49 transition types), which remains feasible within the 220 H100-hour budget.\\n\\n**LLM-Guided Task Program Generation with Grammar Constraints**: The LLM (Qwen 3.6-35B-A3B) generates task programs as grammar-valid primitive sequences with spatial parameter bindings. The LLM reasons about task semantics (delivery routes, obstacle navigation, sequential manipulation schedules) while the grammar enforces structural validity and the TFN provides differentiable feasibility scores for soft-constraining the LLM's parameter choices. Generated programs are compiled into Isaac Lab Python @configclass environment configurations using AGILE's configuration-driven architecture: each becomes a self-contained file specifying scene setup, observation space, action space, staged reward functions (auto-generated from primitive sequence structure following VIRAL's stage-weighted approach), termination conditions, and curriculum parameters.\\n\\n**Active Composition Generation Loop**: Inspired by Eurekaverse's co-evolution but targeting compositional diversity rather than single-skill difficulty: (1) Generate batch of grammar-valid compositions via LLM. (2) TFN scores each composition; compositions above threshold proceed to simulation, compositions below threshold are rejected, compositions in the uncertain band are prioritized for simulation (active learning). (3) Simulate accepted compositions in Isaac Lab (4096 parallel environments). (4) Update TFN with new rollout data. (5) LLM receives feedback on which compositions succeeded/failed and why (structured failure mode analysis: balance failure, grasp loss, collision, timeout). This loop iterates for ~10 generations, progressively expanding the frontier of achievable compositions.\\n\\n**Pre-trained GR00T-WBC Execution**: Leverages the latest GEAR-SONIC (Feb 2026) pre-trained locomotion checkpoint and GR00T-WBC's PinkKinematics IK for upper-body manipulation, compatible with the GR00T N1.7 end-to-end VLA workflow (released May 2026). State-machine coordinator sequences SONIC commands and IK targets based on primitive transitions. For primitives requiring novel coordination (push, open_door), fine-tune with <5 H100-hours per primitive type using AGILE's training pipeline.\\n\\n**Downstream Evaluation with Compositional Generalization**: Train diffusion policy (ACT architecture) on generated datasets. Evaluate: (a) held-out compositions (novel primitive sequences), (b) held-out spatial configurations, (c) held-out dynamic parameters, (d) novel primitive types added post-training. Baselines: (1) Eurekaverse-style single-skill environment co-evolution (adapted to loco-manipulation), (2) DemoHLM-style demo augmentation (single demo per task → spatial variations), (3) STRIDE-style per-task reward optimization for composed tasks, (4) Grammar-only composition with analytical predicates (no TFN), (5) Grammar + TFN without active learning (random composition sampling), (6) LLM-only generation without grammar constraints, (7) LHM-Humanoid-style manually designed task set (5-8 hand-designed compositions), (8) RoboGene-adapted: replace TFN with three LLM-based feasibility evaluators (physical, novelty, constraint adherence) applied to grammar-generated humanoid compositions—directly isolating the value of learned GNN prediction vs. LLM-based evaluation within the same compositional framework. Key ablations: TFN vs. analytical predicates (measures value of learning), active vs. random sampling (measures value of uncertainty-guided generation), grammar structure vs. unstructured composition (measures value of grammatical scaffold for learning), TFN generalization curve (measures rollouts needed per novel primitive type).\",\n  \"resource_estimate\": {\n    \"venue_strategy\": \"We target Humanoids 2026 (paper deadline July 24, 2026 — 75 days from today, per 2026.ieee-humanoids.org) as the primary venue. This is the ideal venue for this work: Humanoids specifically values humanoid-focused systems contributions with algorithmic novelty, and the 75-day timeline comfortably accommodates the full evaluation (7 primitives, active learning loop, 8 baselines, 4 ablations). CoRL 2026 (abstract May 26, paper May 29 — 16-19 days) was considered but rejected for two reasons: (1) A CoRL-minimal submission (3 primitives, bootstrap TFN only, no active learning, no ablations) would demonstrate TFN feasibility prediction in principle but lack the evaluation depth to be competitive at CoRL's acceptance rate (~25%). The TFN's core value proposition is that grammar structure makes transition feasibility learnable and that active learning efficiently explores the composition space—neither can be demonstrated with only 3 primitives and bootstrap training. (2) The 19-day timeline is incompatible with rigorous experimentation: grammar implementation + TFN architecture + SONIC integration + bootstrap data collection + composition evaluation + 8-page paper, with zero margin for debugging the inevitable SONIC integration issues. A rushed submission risks a desk rejection on evaluation grounds. CoRL 2027 is targeted for an extended version with real-robot transfer experiments and formal sample complexity analysis.\",\n    \"manual\": {\n      \"gpu_hours\": \"~200-220h H100 (includes 10-20h contingency for TFN generalization)\",\n      \"gpu_utilization\": \"25-35% effective; researcher idles GPU while designing grammar, implementing TFN architecture, debugging GEAR-SONIC integration, and iterating active learning loop\",\n      \"timeline\": \"7-8 weeks (1.5 weeks grammar design + TFN architecture + GEAR-SONIC integration, 2 weeks TFN training + active generation loop, 2 weeks downstream training + evaluation, 1.5 weeks ablations + paper). Fits comfortably within 75-day Humanoids deadline with ~2 weeks buffer.\",\n      \"team\": \"1 researcher (requires familiarity with Isaac Lab, GNN training, and AGILE/GR00T-WBC)\",\n      \"estimated_gpu_cost\": \"$500-550 at ~$2.50/hr H100 spot pricing\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~190-220h H100 (includes 10-20h contingency for TFN generalization)\",\n      \"gpu_utilization\": \"55-70%; agent automates configclass generation, TFN training loops, experiment scheduling; idles during human review of TFN architecture decisions and generated task quality\",\n      \"timeline\": \"6-7 weeks (targeting Humanoids 2026 July 24 deadline, 75 days, with ~3 weeks buffer)\",\n      \"team\": \"1 researcher, ~25-35min/day reviewing TFN training curves, generated compositions, and demonstration quality\",\n      \"claude_api_cost\": \"$200-400 (2000-4000 agentic turns for Isaac Lab compilation, TFN training orchestration, and experiment analysis)\",\n      \"estimated_gpu_cost\": \"$475-550 at ~$2.50/hr H100 spot pricing\",\n      \"budget_breakdown\": \"~10h TFN bootstrap data collection (200 rollouts × 4096 envs), ~5h TFN training (GNN, fast on single GPU), ~5h GEAR-SONIC fine-tuning for push/open_door/squat, ~60h active generation loop (10 generations × ~6h per generation: LLM generation + simulation verification + TFN update), ~60h downstream diffusion policy training, ~40h ablations (8 baselines + 4 key ablations), ~10-20h contingency for TFN generalization testing, ~10h buffer/iteration\",\n      \"risk_note\": \"Primary risk: TFN may not generalize to novel primitive types from 20-30 rollouts. This is framed as a key experimental hypothesis, not an assumption. Mitigation: architecture uses primitive-type-agnostic physical features; contingency budget of 10-20h for additional rollouts if generalization requires more data. Worst case (no transfer): full active learning for all 49 transition types remains within budget. Secondary risk: GEAR-SONIC checkpoint may need more than 5h fine-tuning for push/open_door primitives.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~210-220h H100 (budget-constrained, includes contingency)\",\n      \"gpu_utilization\": \"80-90%; agent operates continuously, prioritizing TFN active learning loop\",\n      \"timeline\": \"3-4 weeks with 4 H100 GPUs concurrently (well within 75-day Humanoids deadline)\",\n      \"team\": \"0 (initial 3-hour setup: configure AGILE, verify GEAR-SONIC checkpoint, set LLM API keys, define TFN architecture)\",\n      \"claude_api_cost\": \"$350-750 (3500-7500 turns for autonomous pipeline development, TFN training, active generation, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$525-550 at ~$2.50/hr H100 spot pricing\",\n      \"speed_bottleneck\": \"Active learning loop requires sequential TFN updates between generation batches; physics verification throughput (4096 envs per H100, ~15 wall-clock hours for 1000 valid demonstrations)\",\n      \"risk_note\": \"Agent may over-explore TFN architecture variants vs. downstream evaluation; strict budget requires early stopping. TFN generalization testing requires careful allocation of contingency compute.\"\n    }\n  },\n  \"target_venues\": [\n    \"Humanoids 2026 (paper deadline July 24, 2026 — 75 days, primary target. Ideal venue: humanoid-specific systems+algorithmic contribution, values both the grammar engineering and TFN learning contribution; conference Dec 6-9, Santa Clara CA. Full 7-primitive evaluation with active learning and all ablations.)\",\n    \"CoRL 2027 (expected deadline ~May 2027 — extended version with real-robot transfer via AGILE's sim-to-real pipeline, formal sample complexity bounds for grammar-structured feasibility learning, TFN generalization analysis across additional primitive types, and comparison with Ψ₀ as downstream consumer)\",\n    \"ICRA 2027 (expected deadline ~September 2026 — alternative venue if Humanoids review feedback suggests major revisions; allows additional baselines and potential RoboGene direct comparison)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Eurekaverse: Environment Curriculum Generation via Large Language Models (CoRL 2024, arXiv:2411.01775, NVIDIA Research) — LLM-driven environment co-evolution for single-skill locomotion training; generates terrain programs for quadruped parkour. Key paradigm ancestor. Differentiation: single-skill environment variation vs. our compositional multi-stage task generation with learned transition dynamics\",\n    \"VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (CVPR 2026, arXiv:2511.15200, NVlabs) — hand-designed composite tasks on G1 with 54 consecutive real-world cycles; identifies reward engineering as scaling bottleneck. Primary comparison\",\n    \"RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation (arXiv:2602.16444, Feb 2026) — diversity-driven agentic framework with three LLM-based feasibility evaluators (physical, novelty, constraint adherence) and LFU sampling; generates 18K trajectories across 900 tasks on UR-5e/Franka/AgileX. Key concurrent work in feasibility-aware task generation. Differentiation: LLM-based post-hoc evaluation vs. learned GNN upfront prediction; general manipulation vs. humanoid-specific coupled dynamics; free-form generation vs. compositional grammar structure. Adapted as baseline 8\",\n    \"FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula (arXiv:2603.01505, March 2026) — closed-loop VLM auditing (static scene validation + dynamic execution monitoring) with active repair on RidgebackFranka in Isaac Sim; achieves 92.1% feasible task rate. Key concurrent work. Differentiation: per-task post-hoc VLM auditing vs. compositional upfront GNN prediction; individual tasks vs. multi-stage sequences; mobile manipulation vs. humanoid whole-body control\",\n    \"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (arXiv:2603.12263, RSS 2026) — staged VLM pre-training on egocentric human video + flow-based action expert fine-tuning; 40%+ over GR00T-N1.6, acquires new skills from 80 trajectories. Key downstream consumer: CompLocoGen's generated compositional tasks could serve as training data for Ψ₀-class foundation models\",\n    \"DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (arXiv:2510.11258) — generates diverse trajectories from single demo via object-centric representation replay on Unitree G1. Produces spatial variations within fixed task template. Key data-generation baseline: demonstrates demo-augmentation cannot produce compositional novelty\",\n    \"AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning (arXiv:2603.20147, March 2026, github.com/nvidia-isaac/WBC-AGILE, Apache 2.0) — target substrate; configuration-driven Isaac Lab workflow. CompLocoGen generates upstream training task configurations\",\n    \"GR00T-WholeBodyControl/GEAR-SONIC (NVlabs, open-source Apache 2.0, GEAR-SONIC released Feb 2026, GR00T N1.7 VLA workflow May 2026) — pre-trained G1 locomotion checkpoints (142K+ motions), decoupled WBC with UNITREE_G1_SONIC embodiment\",\n    \"Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models (arXiv:2401.03360, CoRL 2023) — trains skill-level diffusion models for precondition/effect-based chaining in fixed-base manipulation. Informs our TFN's per-edge feasibility prediction but does not address loco-manipulation coupling\",\n    \"GSC: A Graph-based Skill Composition Framework for Robot Learning (Robotics & Autonomous Systems, 2024) — GNN over skill graphs with transformer-style architecture. Architectural inspiration for our Transition Feasibility Network\",\n    \"SCaR: Refining Skill Chaining for Long-Horizon Robotic Manipulation (NeurIPS 2024) — learned success predictors for sub-task transitions; validates that transition feasibility can be learned from few-shot rollouts\",\n    \"SuperDyno: Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics (ICLR 2025 Workshop) — learns neural dynamics for humanoid control replacing analytical simulators. Validates that humanoid dynamics can be captured by neural networks\",\n    \"Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) — LLM-powered scene generation with 200+ tasks, 5140 assets. Large-scale generation without compositional grammar; performance degrades on multi-step tasks\",\n    \"STRIDE: Automating Reward Design for Humanoid Robotics Locomotion (arXiv:2502.04692, Feb 2025) — automates single-task locomotion reward design via LLMs, 250% over EUREKA. Cannot compose multi-stage tasks\",\n    \"FORGE: Forging Better Rewards via Multi-Agent LLM Framework (OpenReview 2025) — multi-agent LLM reward evolution, 38.5% over EUREKA. Single-task; does not address task composition\",\n    \"EUREKA: Human-Level Reward Design via Coding LLMs (ICLR 2024, arXiv:2310.12931) — established LLM reward optimization paradigm\",\n    \"LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation (arXiv:2508.16943, March 2026) — 350 diverse scenes, RL teacher + DAgger. Manually designed scenes; CompLocoGen could serve as automated task generator\",\n    \"WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026, arXiv:2512.11047) — policy architecture orthogonal to task generation; downstream consumer\",\n    \"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation (arXiv:2505.06776, L4DC 2026) — force-adaptive dual-agent RL on real humanoids; validates deployability, hand-designed tasks\",\n    \"SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending (arXiv:2506.09366) — hierarchical RL with 4 primitive skills on G1/H1, 8 benchmark tasks; manually specified. CompLocoGen's grammar could automate task generation for SkillBlender-style systems\",\n    \"Scene Graph Atomic Skills (ICRA 2026, Harvard) — GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition; tabletop focus\",\n    \"Humanoid Hanoi (arXiv:2602.13850, Feb 2026) — distribution shift during skill composition; directly informs our transition feasibility learning\",\n    \"GenManip: LLM-driven Simulation for Generalizable Manipulation (CVPR 2025) — LLM-to-simulation-to-filter paradigm for tabletop manipulation\",\n    \"GR00T-Gen (NVIDIA, 2025) — generates 100+ individual tasks, not compositionally coupled\",\n    \"Isaac Lab (arXiv:2511.04831) — Python @configclass manager-based workflow for environment specification\"\n  ],\n  \"description\": \"We propose CompLocoGen, a system that combines a physics-informed skill grammar with a learned Transition Feasibility Network (TFN) to automatically generate diverse humanoid loco-manipulation training environments for NVIDIA's AGILE/Isaac Lab ecosystem—within 220 H100-hours. The core algorithmic contribution is the TFN: a GNN-based model that learns to predict whether primitive transitions in a composed task sequence will succeed, trained via active learning from targeted simulation rollouts at primitive boundaries. This positions CompLocoGen distinctly from concurrent feasibility-aware generation systems: RoboGene (Feb 2026) uses LLM-based post-hoc evaluation for general manipulation; FATE (March 2026) uses VLM-based auditing with active repair for mobile manipulation. CompLocoGen instead provides learned upfront prediction via GNN that captures humanoid-specific coupled dynamics (centroidal momentum, contact forces at transition boundaries)—operating in milliseconds per composition and improving with data rather than requiring LLM/VLM inference per proposal. The grammar provides structure that makes transition feasibility learnable from O(100) rollouts per transition type: instead of learning global task success (exponential), the TFN learns local boundary dynamics (quadratic in primitive count). We define a 7-primitive grammar (walk, pick, place, carry, push, open_door, squat) producing 10^4-10^6 parametrized compositions, and quantify how structural filtering, analytical predicates, and learned TFN filtering progressively reduce this space to dynamically feasible tasks. We hypothesize that primitive-type-agnostic physical features enable few-shot TFN transfer to novel primitive types; quantifying the generalization curve IS a key experimental result, with contingency compute budgeted if transfer requires more data than anticipated. An active generation loop (inspired by Eurekaverse's co-evolution but targeting compositional diversity) iteratively expands the frontier of achievable compositions. Generated task programs compile to Isaac Lab @configclass configurations. Execution leverages GEAR-SONIC (Feb 2026) pre-trained locomotion and GR00T-WBC's PinkKinematics IK. Evaluation compares against 8 baselines including a RoboGene-adapted baseline (LLM-based feasibility evaluation applied to grammar-generated compositions) that directly isolates the value of learned vs. LLM-based feasibility assessment—with key ablations isolating the value of learned feasibility, active sampling, grammar structure, and TFN generalization. Generated tasks could serve as training data for downstream foundation models like Ψ₀ (RSS 2026). Primary target: Humanoids 2026 (July 24, 75 days).\",\n  \"project_name\": \"llm_locomanip_factory\",\n  \"source\": \"web_research\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54682e57-47a9-4f2d-8ea6-a0ed311f372d",
  "isSidechain": false,
  "requestId": "req_011CauSnQiQEyaJJ5PxVC6qE",
  "type": "assistant",
  "uuid": "92b1d86f-ffed-46fe-aef6-2dda2b14b1ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LwuYNR7EN9tarewPNKNfsf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 49938,
      "output_tokens": 10997,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10997,
          "cache_read_input_tokens": 49938,
          "cache_creation_input_tokens": 670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 670
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-10T19:37:02.719Z_

<details><summary>↩ Tool result · reported error · `toolu_01CRd1yruUUAqNKDtt4Mo76N`</summary>

```text
Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92b1d86f-ffed-46fe-aef6-2dda2b14b1ee",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "b8c4ca06-4599-4ff5-9635-5cfb6450e1b3",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "92b1d86f-ffed-46fe-aef6-2dda2b14b1ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 77_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Co…",
  "leafUuid": "b8c4ca06-4599-4ff5-9635-5cfb6450e1b3",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Runtime record

_source line 78_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise CoRL 2026 scope or justify Humanoids 2026 timeline",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Tool call

_source line 79 · 2026-05-10T19:41:20.411Z_

<details open><summary>🔧 Tool call — Write · `toolu_01HjzbRkEmrvCCDHjaBAEK63`</summary>

```json
{
  "file_path": "/tmp/revised_idea.json",
  "content": "{\n  \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Compositional Humanoid Loco-Manipulation Task Generation\",\n  \"change_type\": \"major\",\n  \"core_problem\": \"Scaling humanoid loco-manipulation to diverse real-world tasks requires diverse training environments, but every loco-manipulation task in NVIDIA's AGILE/GR00T-WBC ecosystem must be manually specified as a self-contained Isaac Lab configuration file. VIRAL (CVPR 2026) demonstrates composite tasks work but identifies reward engineering as a scaling bottleneck. Eurekaverse (CoRL 2024) pioneered LLM-driven environment curriculum generation but only for single-skill training (quadruped parkour). Recent feasibility-aware task generation systems—RoboGene (arXiv:2602.16444, Feb 2026) and FATE (arXiv:2603.01505, March 2026)—automate diverse task creation with LLM/VLM-based feasibility evaluation, achieving impressive scale (18K trajectories and 92.1% feasible task rate respectively). However, both use post-hoc evaluation (LLM-based evaluators in RoboGene; VLM static+dynamic auditing in FATE) rather than learned predictive models, and neither targets humanoid loco-manipulation where locomotion-manipulation coupling creates emergent failure modes at primitive boundaries. The fundamental challenge is twofold: (1) composing novel multi-stage loco-manipulation tasks from a primitive grammar where inter-primitive dynamics (balance during walk-to-pick transitions, gait adaptation for carry, CoM shifts at primitive boundaries) create failure modes absent from any individual primitive, and (2) efficiently predicting which compositions are dynamically feasible without exhaustive simulation—requiring a learned transition feasibility model that generalizes across primitive types and parameters. How can we combine a physics-informed skill grammar with a learned Transition Feasibility Network to automatically generate diverse, dynamically feasible loco-manipulation task configurations for Isaac Lab?\",\n  \"opportunity\": \"VIRAL (CVPR 2026) achieves 54 consecutive real-world loco-manipulation cycles on G1 but relies entirely on hand-designed stage-weighted rewards—the authors state that 'scaling to the open-ended diversity of daily life remains intractable' via manual reward engineering. Eurekaverse (CoRL 2024) automates environment curriculum generation via LLM code generation with agent-environment co-evolution, achieving superhuman parkour curricula—but operates on single-skill locomotion over terrain, with no manipulation, no inter-primitive coupling, and no compositional task structure. RoboGene (arXiv:2602.16444, Feb 2026) generates 18K trajectories across 900 tasks with LLM-based feasibility evaluators (physical, novelty, constraint adherence) and LFU diversity sampling—but targets tabletop and mobile manipulation (UR-5e, Franka, AgileX) without humanoid-specific dynamics, and its LLM-based evaluation cannot capture the physical coupling between locomotion and manipulation at transition boundaries. FATE (arXiv:2603.01505, March 2026) achieves 92.1% feasible task rate via closed-loop VLM auditing with active repair on a RidgebackFranka mobile manipulator—but evaluates individual tasks post-hoc rather than predicting compositional feasibility upfront, and does not address humanoid whole-body dynamics. DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single demonstration via object-centric replay—producing spatial variations of one task template but not compositionally novel tasks. LHM-Humanoid (arXiv:2508.16943) achieves impressive long-horizon loco-manipulation across 350 scenes but relies on manually designed configurations. Ψ₀ (arXiv:2603.12263, RSS 2026) demonstrates a foundation model for universal humanoid loco-manipulation that outperforms GR00T-N1.6 by 40%+ and can acquire new skills from only 80 trajectories—representing a key downstream consumer that would directly benefit from CompLocoGen's automatically generated diverse training tasks. In the learned composition space, Generative Skill Chaining (CoRL 2023) uses diffusion models for skill precondition/effect chaining, and SCaR (NeurIPS 2024) learns success predictors for sub-task transitions—but both target fixed-base manipulation without dynamics-aware feasibility for whole-body locomotion+manipulation coupling. The gap is precise: no system combines (1) a grammar for compositional loco-manipulation task generation with (2) a learned transition feasibility predictor that captures humanoid-specific coupled dynamics at primitive boundaries—as opposed to post-hoc LLM/VLM evaluation (RoboGene, FATE) or exhaustive simulation—enabling (3) active generation of training data for the AGILE/GR00T-WBC ecosystem and downstream foundation models like Ψ₀.\",\n  \"landscape\": \"**LLM-based environment/curriculum generation**: Eurekaverse (arXiv:2411.01775, CoRL 2024) uses LLM code generation to produce increasingly challenging terrain environments for quadruped parkour, with agent-environment co-evolution over 5 generations. Key paradigm: LLM generates Python terrain functions → train policy → evaluate → feedback to LLM. However, it generates monolithic terrain programs for single-skill locomotion—no manipulation, no inter-primitive dynamics, no compositional task structure. CompLocoGen extends this paradigm to compositional multi-stage loco-manipulation: instead of varying a single environment, we compose multi-primitive task sequences and learn which compositions are dynamically feasible. Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) uses LLM-powered scene generation with RAG-based asset retrieval and DSL code generation to create thousands of diverse environments for humanoid manipulation across 200+ tasks—but lacks formal compositional grammar and shows performance degradation on multi-step tasks (~52% vs ~80% for atomic tasks). **Feasibility-aware task generation (key concurrent work)**: RoboGene (arXiv:2602.16444, Feb 2026) introduces a diversity-driven agentic framework with three specialized LLM-based evaluators: a Physical Feasibility Evaluator (kinematic reachability, physics law compliance), a Novelty Evaluator (object complexity, temporal depth), and a Constraint Adherence Evaluator (scene-task consistency). Its LFU (Least Frequently Used) sampling ensures balanced coverage across under-explored task regions. RoboGene achieves 63.2% object coverage and 91.5% skill coverage across 18K trajectories on UR-5e, Franka, and AgileX platforms. Critical differentiation: RoboGene's feasibility evaluation is LLM-based and post-hoc (generate → evaluate → self-reflect → refine); CompLocoGen's TFN is a learned GNN that predicts feasibility upfront from boundary state features, capturing physical dynamics that LLMs cannot assess (centroidal momentum coupling, contact force propagation at transitions). RoboGene targets general manipulation without humanoid-specific whole-body coupling. We include a RoboGene-adapted baseline (LLM-based feasibility evaluation applied to grammar-generated humanoid compositions) to directly compare learned vs. LLM-based feasibility assessment. FATE (arXiv:2603.01505, March 2026) proposes closed-loop feasibility-aware generation with a sequential VLM auditing pipeline: static alignment (reachability, affordance, physical plausibility) followed by dynamic alignment (execution monitoring with rollback-and-repair). FATE achieves 92.1% feasible task rate on a RidgebackFranka in Isaac Sim. Critical differentiation: FATE evaluates individual task instances post-hoc via VLM perception; CompLocoGen predicts compositional feasibility upfront from learned transition dynamics—the TFN scores an entire primitive sequence in milliseconds without simulation, enabling efficient search over the exponential composition space. FATE's per-task VLM auditing scales linearly with proposals; TFN-based filtering is amortized after training. FATE targets mobile manipulation (7-DoF arm + holonomic base); CompLocoGen targets humanoid whole-body control where locomotion-manipulation coupling is qualitatively different. **LLM-based reward design (per-task optimization)**: STRIDE (arXiv:2502.04692, Feb 2025) automates humanoid locomotion reward design via LLMs, 250% over EUREKA—single-task locomotion only. FORGE (OpenReview 2025) uses multi-agent LLMs for evolutionary reward refinement, 38.5% over EUREKA—single-task. EUREKA (ICLR 2024) established the LLM-to-reward-code paradigm. These solve per-task reward engineering; CompLocoGen solves the orthogonal problem of generating novel task compositions with learned feasibility prediction. **Demonstration-based data generation**: DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single teleoperated demonstration by converting to object-centric representations and replaying under varied initial conditions with a 3-stage pipeline (locomotion → pre-manipulation → manipulation) on Unitree G1. It produces spatial diversity within a fixed task template—not compositional novelty across task structures. CompLocoGen generates qualitatively different training data: novel task compositions (e.g., walk-pick-carry-climb_stairs-place) that no single demonstration could cover. **Learned skill composition approaches**: Generative Skill Chaining (arXiv:2401.03360, CoRL 2023) trains skill-level diffusion models capturing (precondition, parameters, effect) distributions for chaining—fixed-base manipulation only. SCaR (NeurIPS 2024) refines skill chaining with learned success predictors for sub-task transitions. GSC (Robotics & Autonomous Systems, 2024) models skill sets as GNN graphs with transformer-style architecture for skill embeddings. SuperDyno (ICLR 2025 Workshop) learns differentiable neural dynamics for humanoid whole-body control. None of these address composition feasibility for coupled loco-manipulation where locomotion dynamics (balance, gait) interact with manipulation state (load, grasp). CompLocoGen's Transition Feasibility Network operates specifically on the boundary states between loco-manipulation primitives, learning to predict whether locomotion-manipulation coupling will cause failure at transitions. **Sim-to-real composite tasks**: VIRAL/GR00T-VisualSim2Real (CVPR 2026, NVlabs) demonstrates composite loco-manipulation with 54 consecutive real-world cycles—hand-designed tasks. LHM-Humanoid (arXiv:2508.16943, March 2026) learns unified policies across 350 manually designed scenes via RL teacher distillation. FALCON (arXiv:2505.06776, L4DC 2026) demonstrates force-adaptive dual-agent RL for loco-manipulation on real humanoids—hand-designed tasks. **Foundation models as downstream consumers**: Ψ₀ (arXiv:2603.12263, RSS 2026) is an open foundation model for universal humanoid loco-manipulation using staged VLM pre-training on egocentric human video followed by flow-based action expert fine-tuning on robot data. Ψ₀ achieves 40%+ over GR00T-N1.6 and can acquire new loco-manipulation skills from only 80 trajectories. CompLocoGen could serve as an automated training data generator for Ψ₀-class models—the compositionally diverse tasks it produces are precisely the data these foundation models need to achieve broader generalization. WholeBodyVLA (ICLR 2026, arXiv:2512.11047) learns unified latent VLA for whole-body control—another downstream consumer. SkillBlender (arXiv:2506.09366) demonstrates compositional skill blending on G1 with 4 primitive skills (walking, reaching, squatting, stepping) across 8 benchmark tasks—manually specified. CompLocoGen's grammar could automate task generation for SkillBlender-style systems. **Scene graph and compositional approaches**: Scene Graph Atomic Skills (ICRA 2026, Harvard) uses GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition—tabletop manipulation focus. GenManip (CVPR 2025) provides LLM-to-simulation-to-filter for tabletop manipulation. Humanoid Hanoi (arXiv:2602.13850, Feb 2026) demonstrates distribution shift during skill composition requiring data aggregation—directly informs our transition modeling. **The specific gap**: No system combines grammar-structured compositional task generation with a learned transition feasibility predictor for humanoid loco-manipulation. RoboGene and FATE achieve feasibility-aware generation via LLM/VLM post-hoc evaluation for tabletop/mobile manipulation; CompLocoGen introduces learned upfront prediction via GNN that captures humanoid-specific coupled dynamics. Eurekaverse generates single-skill environments; DemoHLM augments single demonstrations; Generative Skill Chaining/GSC learn feasibility for fixed-base manipulation; VIRAL/LHM-Humanoid use manually designed compositions. CompLocoGen uniquely combines: (a) a 7-primitive grammar generating exponentially many task compositions, (b) a GNN-based Transition Feasibility Network that learns loco-manipulation coupling dynamics from few-shot simulation rollouts, and (c) active generation targeting the uncertainty frontier of the feasibility predictor.\",\n  \"approach\": \"We build CompLocoGen as a grammar-structured system that learns transition feasibility for compositional loco-manipulation task generation, producing Isaac Lab-compatible configurations within 220 H100-hours.\\n\\n**Expanded Physics-Informed Skill Grammar (7 Primitives)**: We define a context-free grammar over seven coupled loco-manipulation primitives: walk(target_pos, speed, gait_style), pick(object_id, grasp_type, approach_vector), place(target_pos, placement_constraint), carry(object_id, carry_pose, stability_mode), push(object_id, direction, force_profile), open_door(door_id, handle_type, opening_angle), and squat(target_height, duration, stability_mode). Each primitive has typed spatial parameters, structural preconditions/postconditions, and a boundary state specification (the distribution of robot states—CoM position/velocity, joint configurations, contact states, grasp forces—at primitive entry/exit). The 7-primitive grammar produces 7^L valid structural sequences of length L (before feasibility filtering). For L=3-5 (typical loco-manipulation tasks), this yields 343-16,807 structural compositions. With parameter variation (3-5 settings per typed parameter), the effective task space is 10^4-10^6 unique configurations. Structural filtering (precondition/postcondition satisfaction) reduces this by ~60%; dynamic feasibility filtering further reduces by an experimentally measured factor—quantifying this reduction IS the key experimental result.\\n\\n**Transition Feasibility Network (TFN) — Core Algorithmic Contribution**: Instead of relying on analytical physics predicates (ZMP, centroidal dynamics) or post-hoc LLM/VLM evaluation (as in RoboGene and FATE), we introduce a GNN-based Transition Feasibility Network that learns to predict composition success probability from primitive boundary states. Architecture: Each primitive instance is a node with features encoding (primitive type, spatial parameters, expected boundary state statistics). Edges connect consecutive primitives in the composition. A message-passing GNN (3 layers, 128-dim) processes the composition graph and outputs per-edge transition feasibility scores in [0,1] plus an overall composition feasibility score. The TFN's advantages over alternative feasibility approaches: (a) vs. analytical predicates: captures non-obvious interaction effects that simplified models miss (e.g., arm momentum during open_door affecting walking balance), improves with data rather than requiring manual engineering per primitive type; (b) vs. LLM-based evaluation (RoboGene-style): provides calibrated continuous scores rather than binary judgments, runs in milliseconds rather than requiring LLM API calls per composition, captures physical dynamics (centroidal momentum, contact forces) that language models cannot assess; (c) vs. VLM-based auditing (FATE-style): predicts upfront rather than evaluating post-hoc, handles compositional structure (scores full sequences via message-passing) rather than per-task evaluation; (d) vs. monolithic learned models: the grammar structure means it only needs to learn local transition dynamics (O(P^2) transition types for P primitives = 49 for 7 primitives), not global task success from all possible sequences (exponential in length).\\n\\n**TFN Training — Three-Phase Protocol**: (1) Bootstrap: Seed the TFN with ~200 simulation rollouts (50 per transition type for the 4 most common transitions: walk→pick, pick→carry, carry→walk, walk→place) using analytical predicates to stratify sampling across feasible/infeasible boundary. (2) Active Learning: Use TFN uncertainty (MC-dropout variance) to identify which transition types and parameter regions have highest prediction uncertainty. Allocate simulation budget preferentially to these uncertain regions. After each batch of 50 rollouts, retrain TFN. (3) Generalization Testing: We hypothesize that primitive-type-agnostic physical features (CoM velocity, contact forces, joint torques at boundaries) enable few-shot transfer to novel primitive types (push, open_door, squat). Quantifying the number of rollouts needed per novel primitive type to achieve reliable prediction (target: >85% AUROC) IS a key experimental result, not a design assumption. We budget 20-30 rollouts per new transition type as an optimistic starting point, with 10-20 additional H100-hours of contingency compute if generalization requires more data. If few-shot transfer fails entirely, we fall back to full active learning for all 7 primitives (~49 transition types), which remains feasible within the 220 H100-hour budget.\\n\\n**LLM-Guided Task Program Generation with Grammar Constraints**: The LLM (Qwen 3.6-35B-A3B) generates task programs as grammar-valid primitive sequences with spatial parameter bindings. The LLM reasons about task semantics (delivery routes, obstacle navigation, sequential manipulation schedules) while the grammar enforces structural validity and the TFN provides differentiable feasibility scores for soft-constraining the LLM's parameter choices. Generated programs are compiled into Isaac Lab Python @configclass environment configurations using AGILE's configuration-driven architecture: each becomes a self-contained file specifying scene setup, observation space, action space, staged reward functions (auto-generated from primitive sequence structure following VIRAL's stage-weighted approach), termination conditions, and curriculum parameters.\\n\\n**Active Composition Generation Loop**: Inspired by Eurekaverse's co-evolution but targeting compositional diversity rather than single-skill difficulty: (1) Generate batch of grammar-valid compositions via LLM. (2) TFN scores each composition; compositions above threshold proceed to simulation, compositions below threshold are rejected, compositions in the uncertain band are prioritized for simulation (active learning). (3) Simulate accepted compositions in Isaac Lab (4096 parallel environments). (4) Update TFN with new rollout data. (5) LLM receives feedback on which compositions succeeded/failed and why (structured failure mode analysis: balance failure, grasp loss, collision, timeout). This loop iterates for ~10 generations, progressively expanding the frontier of achievable compositions.\\n\\n**Pre-trained GR00T-WBC Execution**: Leverages the latest GEAR-SONIC (Feb 2026) pre-trained locomotion checkpoint and GR00T-WBC's PinkKinematics IK for upper-body manipulation, compatible with the GR00T N1.7 end-to-end VLA workflow (released May 2026). State-machine coordinator sequences SONIC commands and IK targets based on primitive transitions. For primitives requiring novel coordination (push, open_door), fine-tune with <5 H100-hours per primitive type using AGILE's training pipeline.\\n\\n**Downstream Evaluation with Compositional Generalization**: Train diffusion policy (ACT architecture) on generated datasets. Evaluate: (a) held-out compositions (novel primitive sequences), (b) held-out spatial configurations, (c) held-out dynamic parameters, (d) novel primitive types added post-training. Baselines: (1) Eurekaverse-style single-skill environment co-evolution (adapted to loco-manipulation), (2) DemoHLM-style demo augmentation (single demo per task → spatial variations), (3) STRIDE-style per-task reward optimization for composed tasks, (4) Grammar-only composition with analytical predicates (no TFN), (5) Grammar + TFN without active learning (random composition sampling), (6) LLM-only generation without grammar constraints, (7) LHM-Humanoid-style manually designed task set (5-8 hand-designed compositions), (8) RoboGene-adapted: replace TFN with three LLM-based feasibility evaluators (physical, novelty, constraint adherence) applied to grammar-generated humanoid compositions—directly isolating the value of learned GNN prediction vs. LLM-based evaluation within the same compositional framework. Key ablations: TFN vs. analytical predicates (measures value of learning), active vs. random sampling (measures value of uncertainty-guided generation), grammar structure vs. unstructured composition (measures value of grammatical scaffold for learning), TFN generalization curve (measures rollouts needed per novel primitive type).\",\n  \"resource_estimate\": {\n    \"venue_strategy\": \"We target Humanoids 2026 (paper deadline July 24, 2026 — 75 days from today, per 2026.ieee-humanoids.org) as the primary venue. This is the ideal venue for this work: Humanoids specifically values humanoid-focused systems contributions with algorithmic novelty, and the 75-day timeline comfortably accommodates the full evaluation (7 primitives, active learning loop, 8 baselines, 4 ablations). CoRL 2026 (abstract May 26, paper May 29 — 16-19 days) was considered but rejected for two reasons: (1) A CoRL-minimal submission (3 primitives, bootstrap TFN only, no active learning, no ablations) would demonstrate TFN feasibility prediction in principle but lack the evaluation depth to be competitive at CoRL's acceptance rate (~25%). The TFN's core value proposition is that grammar structure makes transition feasibility learnable and that active learning efficiently explores the composition space—neither can be demonstrated with only 3 primitives and bootstrap training. (2) The 19-day timeline is incompatible with rigorous experimentation: grammar implementation + TFN architecture + SONIC integration + bootstrap data collection + composition evaluation + 8-page paper, with zero margin for debugging the inevitable GEAR-SONIC integration issues. A rushed submission risks a desk rejection on evaluation grounds. CoRL 2027 is targeted for an extended version with real-robot transfer experiments and formal sample complexity analysis.\",\n    \"manual\": {\n      \"gpu_hours\": \"~200-220h H100 (includes 10-20h contingency for TFN generalization)\",\n      \"gpu_utilization\": \"25-35% effective; researcher idles GPU while designing grammar, implementing TFN architecture, debugging GEAR-SONIC integration, and iterating active learning loop\",\n      \"timeline\": \"7-8 weeks (1.5 weeks grammar design + TFN architecture + GEAR-SONIC integration, 2 weeks TFN training + active generation loop, 2 weeks downstream training + evaluation, 1.5 weeks ablations + paper). Fits comfortably within 75-day Humanoids deadline with ~2 weeks buffer.\",\n      \"team\": \"1 researcher (requires familiarity with Isaac Lab, GNN training, and AGILE/GR00T-WBC)\",\n      \"estimated_gpu_cost\": \"$500-550 at ~$2.50/hr H100 spot pricing\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~190-220h H100 (includes 10-20h contingency for TFN generalization)\",\n      \"gpu_utilization\": \"55-70%; agent automates configclass generation, TFN training loops, experiment scheduling; idles during human review of TFN architecture decisions and generated task quality\",\n      \"timeline\": \"6-7 weeks (targeting Humanoids 2026 July 24 deadline, 75 days, with ~3 weeks buffer)\",\n      \"team\": \"1 researcher, ~25-35min/day reviewing TFN training curves, generated compositions, and demonstration quality\",\n      \"claude_api_cost\": \"$200-400 (2000-4000 agentic turns for Isaac Lab compilation, TFN training orchestration, and experiment analysis)\",\n      \"estimated_gpu_cost\": \"$475-550 at ~$2.50/hr H100 spot pricing\",\n      \"budget_breakdown\": \"~10h TFN bootstrap data collection (200 rollouts x 4096 envs), ~5h TFN training (GNN, fast on single GPU), ~5h GEAR-SONIC fine-tuning for push/open_door/squat, ~60h active generation loop (10 generations x ~6h per generation: LLM generation + simulation verification + TFN update), ~60h downstream diffusion policy training, ~40h ablations (8 baselines + 4 key ablations), ~10-20h contingency for TFN generalization testing, ~10h buffer/iteration\",\n      \"risk_note\": \"Primary risk: TFN may not generalize to novel primitive types from 20-30 rollouts. This is framed as a key experimental hypothesis, not an assumption. Mitigation: architecture uses primitive-type-agnostic physical features; contingency budget of 10-20h for additional rollouts if generalization requires more data. Worst case (no transfer): full active learning for all 49 transition types remains within budget. Secondary risk: GEAR-SONIC checkpoint may need more than 5h fine-tuning for push/open_door primitives.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~210-220h H100 (budget-constrained, includes contingency)\",\n      \"gpu_utilization\": \"80-90%; agent operates continuously, prioritizing TFN active learning loop\",\n      \"timeline\": \"3-4 weeks with 4 H100 GPUs concurrently (well within 75-day Humanoids deadline)\",\n      \"team\": \"0 (initial 3-hour setup: configure AGILE, verify GEAR-SONIC checkpoint, set LLM API keys, define TFN architecture)\",\n      \"claude_api_cost\": \"$350-750 (3500-7500 turns for autonomous pipeline development, TFN training, active generation, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$525-550 at ~$2.50/hr H100 spot pricing\",\n      \"speed_bottleneck\": \"Active learning loop requires sequential TFN updates between generation batches; physics verification throughput (4096 envs per H100, ~15 wall-clock hours for 1000 valid demonstrations)\",\n      \"risk_note\": \"Agent may over-explore TFN architecture variants vs. downstream evaluation; strict budget requires early stopping. TFN generalization testing requires careful allocation of contingency compute.\"\n    }\n  },\n  \"target_venues\": [\n    \"Humanoids 2026 (paper deadline July 24, 2026 — 75 days, primary target. Ideal venue: humanoid-specific systems+algorithmic contribution, values both the grammar engineering and TFN learning contribution; conference Dec 6-9, Santa Clara CA. Full 7-primitive evaluation with active learning and all ablations.)\",\n    \"CoRL 2027 (expected deadline ~May 2027 — extended version with real-robot transfer via AGILE's sim-to-real pipeline, formal sample complexity bounds for grammar-structured feasibility learning, TFN generalization analysis across additional primitive types, and comparison with Ψ₀ as downstream consumer)\",\n    \"ICRA 2027 (expected deadline ~September 2026 — alternative venue if Humanoids review feedback suggests major revisions; allows additional baselines and potential RoboGene direct comparison)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Eurekaverse: Environment Curriculum Generation via Large Language Models (CoRL 2024, arXiv:2411.01775, NVIDIA Research) — LLM-driven environment co-evolution for single-skill locomotion training; generates terrain programs for quadruped parkour. Key paradigm ancestor. Differentiation: single-skill environment variation vs. our compositional multi-stage task generation with learned transition dynamics\",\n    \"VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (CVPR 2026, arXiv:2511.15200, NVlabs) — hand-designed composite tasks on G1 with 54 consecutive real-world cycles; identifies reward engineering as scaling bottleneck. Primary comparison\",\n    \"RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation (arXiv:2602.16444, Feb 2026) — diversity-driven agentic framework with three LLM-based feasibility evaluators (physical, novelty, constraint adherence) and LFU sampling; generates 18K trajectories across 900 tasks on UR-5e/Franka/AgileX. Key concurrent work in feasibility-aware task generation. Differentiation: LLM-based post-hoc evaluation vs. learned GNN upfront prediction; general manipulation vs. humanoid-specific coupled dynamics; free-form generation vs. compositional grammar structure. Adapted as baseline 8\",\n    \"FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula (arXiv:2603.01505, March 2026) — closed-loop VLM auditing (static scene validation + dynamic execution monitoring) with active repair on RidgebackFranka in Isaac Sim; achieves 92.1% feasible task rate. Key concurrent work. Differentiation: per-task post-hoc VLM auditing vs. compositional upfront GNN prediction; individual tasks vs. multi-stage sequences; mobile manipulation vs. humanoid whole-body control\",\n    \"Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (arXiv:2603.12263, RSS 2026) — staged VLM pre-training on egocentric human video + flow-based action expert fine-tuning; 40%+ over GR00T-N1.6, acquires new skills from 80 trajectories. Key downstream consumer: CompLocoGen's generated compositional tasks could serve as training data for Ψ₀-class foundation models\",\n    \"DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (arXiv:2510.11258) — generates diverse trajectories from single demo via object-centric representation replay on Unitree G1. Produces spatial variations within fixed task template. Key data-generation baseline: demonstrates demo-augmentation cannot produce compositional novelty\",\n    \"AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning (arXiv:2603.20147, March 2026, github.com/nvidia-isaac/WBC-AGILE, Apache 2.0) — target substrate; configuration-driven Isaac Lab workflow. CompLocoGen generates upstream training task configurations\",\n    \"GR00T-WholeBodyControl/GEAR-SONIC (NVlabs, open-source Apache 2.0, GEAR-SONIC released Feb 2026, GR00T N1.7 VLA workflow May 2026) — pre-trained G1 locomotion checkpoints (142K+ motions), decoupled WBC with UNITREE_G1_SONIC embodiment\",\n    \"Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models (arXiv:2401.03360, CoRL 2023) — trains skill-level diffusion models for precondition/effect-based chaining in fixed-base manipulation. Informs our TFN's per-edge feasibility prediction but does not address loco-manipulation coupling\",\n    \"GSC: A Graph-based Skill Composition Framework for Robot Learning (Robotics & Autonomous Systems, 2024) — GNN over skill graphs with transformer-style architecture. Architectural inspiration for our Transition Feasibility Network\",\n    \"SCaR: Refining Skill Chaining for Long-Horizon Robotic Manipulation (NeurIPS 2024) — learned success predictors for sub-task transitions; validates that transition feasibility can be learned from few-shot rollouts\",\n    \"SuperDyno: Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics (ICLR 2025 Workshop) — learns neural dynamics for humanoid control replacing analytical simulators. Validates that humanoid dynamics can be captured by neural networks\",\n    \"Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) — LLM-powered scene generation with 200+ tasks, 5140 assets. Large-scale generation without compositional grammar; performance degrades on multi-step tasks\",\n    \"STRIDE: Automating Reward Design for Humanoid Robotics Locomotion (arXiv:2502.04692, Feb 2025) — automates single-task locomotion reward design via LLMs, 250% over EUREKA. Cannot compose multi-stage tasks\",\n    \"FORGE: Forging Better Rewards via Multi-Agent LLM Framework (OpenReview 2025) — multi-agent LLM reward evolution, 38.5% over EUREKA. Single-task; does not address task composition\",\n    \"EUREKA: Human-Level Reward Design via Coding LLMs (ICLR 2024, arXiv:2310.12931) — established LLM reward optimization paradigm\",\n    \"LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation (arXiv:2508.16943, March 2026) — 350 diverse scenes, RL teacher + DAgger. Manually designed scenes; CompLocoGen could serve as automated task generator\",\n    \"WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026, arXiv:2512.11047) — policy architecture orthogonal to task generation; downstream consumer\",\n    \"FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation (arXiv:2505.06776, L4DC 2026) — force-adaptive dual-agent RL on real humanoids; validates deployability, hand-designed tasks\",\n    \"SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending (arXiv:2506.09366) — hierarchical RL with 4 primitive skills on G1/H1, 8 benchmark tasks; manually specified. CompLocoGen's grammar could automate task generation for SkillBlender-style systems\",\n    \"Scene Graph Atomic Skills (ICRA 2026, Harvard) — GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition; tabletop focus\",\n    \"Humanoid Hanoi (arXiv:2602.13850, Feb 2026) — distribution shift during skill composition; directly informs our transition feasibility learning\",\n    \"GenManip: LLM-driven Simulation for Generalizable Manipulation (CVPR 2025) — LLM-to-simulation-to-filter paradigm for tabletop manipulation\",\n    \"GR00T-Gen (NVIDIA, 2025) — generates 100+ individual tasks, not compositionally coupled\",\n    \"Isaac Lab (arXiv:2511.04831) — Python @configclass manager-based workflow for environment specification\"\n  ],\n  \"description\": \"We propose CompLocoGen, a system that combines a physics-informed skill grammar with a learned Transition Feasibility Network (TFN) to automatically generate diverse humanoid loco-manipulation training environments for NVIDIA's AGILE/Isaac Lab ecosystem—within 220 H100-hours. The core algorithmic contribution is the TFN: a GNN-based model that learns to predict whether primitive transitions in a composed task sequence will succeed, trained via active learning from targeted simulation rollouts at primitive boundaries. This positions CompLocoGen distinctly from concurrent feasibility-aware generation systems: RoboGene (Feb 2026) uses LLM-based post-hoc evaluation for general manipulation; FATE (March 2026) uses VLM-based auditing with active repair for mobile manipulation. CompLocoGen instead provides learned upfront prediction via GNN that captures humanoid-specific coupled dynamics (centroidal momentum, contact forces at transition boundaries)—operating in milliseconds per composition and improving with data rather than requiring LLM/VLM inference per proposal. The grammar provides structure that makes transition feasibility learnable from O(100) rollouts per transition type: instead of learning global task success (exponential), the TFN learns local boundary dynamics (quadratic in primitive count). We define a 7-primitive grammar (walk, pick, place, carry, push, open_door, squat) producing 10^4-10^6 parametrized compositions, and quantify how structural filtering, analytical predicates, and learned TFN filtering progressively reduce this space to dynamically feasible tasks. We hypothesize that primitive-type-agnostic physical features enable few-shot TFN transfer to novel primitive types; quantifying the generalization curve IS a key experimental result, with contingency compute budgeted if transfer requires more data than anticipated. An active generation loop (inspired by Eurekaverse's co-evolution but targeting compositional diversity) iteratively expands the frontier of achievable compositions. Generated task programs compile to Isaac Lab @configclass configurations. Execution leverages GEAR-SONIC (Feb 2026) pre-trained locomotion and GR00T-WBC's PinkKinematics IK. Evaluation compares against 8 baselines including a RoboGene-adapted baseline (LLM-based feasibility evaluation applied to grammar-generated compositions) that directly isolates the value of learned vs. LLM-based feasibility assessment—with key ablations isolating the value of learned feasibility, active sampling, grammar structure, and TFN generalization. Generated tasks could serve as training data for downstream foundation models like Ψ₀ (RSS 2026). Primary target: Humanoids 2026 (July 24, 75 days).\",\n  \"project_name\": \"llm_locomanip_factory\",\n  \"source\": \"web_research\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8c4ca06-4599-4ff5-9635-5cfb6450e1b3",
  "isSidechain": false,
  "requestId": "req_011CauTABXGCHxAZAgYfANPi",
  "type": "assistant",
  "uuid": "026ec46b-d66d-48e8-ae50-8f4f6a5f873f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWMfvzAsxzVzWpxWmpv7BW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11032,
      "cache_read_input_tokens": 50608,
      "output_tokens": 9382,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11032,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9382,
          "cache_read_input_tokens": 50608,
          "cache_creation_input_tokens": 11032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11032
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-10T19:41:20.417Z_

<details><summary>↩ Tool result · reported error · `toolu_01HjzbRkEmrvCCDHjaBAEK63`</summary>

```text
Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "026ec46b-d66d-48e8-ae50-8f4f6a5f873f",
  "isSidechain": false,
  "promptId": "6a6d27ca-d99b-47ba-806b-b8312d7e1e48",
  "type": "user",
  "uuid": "b193539f-e09e-4431-b2b9-3335207a76f7",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "026ec46b-d66d-48e8-ae50-8f4f6a5f873f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 81 · 2026-05-10T19:41:20.434Z_

```json
{
  "parentUuid": "b193539f-e09e-4431-b2b9-3335207a76f7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1f2ebccc-d97e-4104-959d-14a03847a123",
  "timestamp": "2026-05-10T19:41:20.434Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 82_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Co…",
  "leafUuid": "1f2ebccc-d97e-4104-959d-14a03847a123",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Runtime record

_source line 83_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise CoRL 2026 scope or justify Humanoids 2026 timeline",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Assistant

_source line 84 · 2026-05-10T19:45:41.971Z_

Here is the complete revised idea as JSON, addressing every reviewer point:

```json
{
  "title": "CompLocoGen: Grammar-Structured Transition Feasibility Learning for Compositional Humanoid Loco-Manipulation Task Generation",
  "change_type": "major",
  "core_problem": "Scaling humanoid loco-manipulation to diverse real-world tasks requires diverse training environments, but every loco-manipulation task in NVIDIA's AGILE/GR00T-WBC ecosystem must be manually specified as a self-contained Isaac Lab configuration file. VIRAL (CVPR 2026) demonstrates composite tasks work but identifies reward engineering as a scaling bottleneck. Eurekaverse (CoRL 2024) pioneered LLM-driven environment curriculum generation but only for single-skill training (quadruped parkour). Recent feasibility-aware task generation systems—RoboGene (arXiv:2602.16444, Feb 2026) and FATE (arXiv:2603.01505, March 2026)—automate diverse task creation with LLM/VLM-based feasibility evaluation, achieving impressive scale (18K trajectories and 92.1% feasible task rate respectively). However, both use post-hoc evaluation (LLM-based evaluators in RoboGene; VLM static+dynamic auditing in FATE) rather than learned predictive models, and neither targets humanoid loco-manipulation where locomotion-manipulation coupling creates emergent failure modes at primitive boundaries. The fundamental challenge is twofold: (1) composing novel multi-stage loco-manipulation tasks from a primitive grammar where inter-primitive dynamics (balance during walk-to-pick transitions, gait adaptation for carry, CoM shifts at primitive boundaries) create failure modes absent from any individual primitive, and (2) efficiently predicting which compositions are dynamically feasible without exhaustive simulation—requiring a learned transition feasibility model that generalizes across primitive types and parameters. How can we combine a physics-informed skill grammar with a learned Transition Feasibility Network to automatically generate diverse, dynamically feasible loco-manipulation task configurations for Isaac Lab?",
  "opportunity": "VIRAL (CVPR 2026) achieves 54 consecutive real-world loco-manipulation cycles on G1 but relies entirely on hand-designed stage-weighted rewards—the authors state that 'scaling to the open-ended diversity of daily life remains intractable' via manual reward engineering. Eurekaverse (CoRL 2024) automates environment curriculum generation via LLM code generation with agent-environment co-evolution, achieving superhuman parkour curricula—but operates on single-skill locomotion over terrain, with no manipulation, no inter-primitive coupling, and no compositional task structure. RoboGene (arXiv:2602.16444, Feb 2026) generates 18K trajectories across 900 tasks with LLM-based feasibility evaluators (physical, novelty, constraint adherence) and LFU diversity sampling—but targets tabletop and mobile manipulation (UR-5e, Franka, AgileX) without humanoid-specific dynamics, and its LLM-based evaluation cannot capture the physical coupling between locomotion and manipulation at transition boundaries. FATE (arXiv:2603.01505, March 2026) achieves 92.1% feasible task rate via closed-loop VLM auditing with active repair on a RidgebackFranka mobile manipulator—but evaluates individual tasks post-hoc rather than predicting compositional feasibility upfront, and does not address humanoid whole-body dynamics. DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single demonstration via object-centric replay—producing spatial variations of one task template but not compositionally novel tasks. LHM-Humanoid (arXiv:2508.16943) achieves impressive long-horizon loco-manipulation across 350 scenes but relies on manually designed configurations. Ψ₀ (arXiv:2603.12263, RSS 2026) demonstrates a foundation model for universal humanoid loco-manipulation that outperforms GR00T-N1.6 by 40%+ and can acquire new skills from only 80 trajectories—representing a key downstream consumer that would directly benefit from CompLocoGen's automatically generated diverse training tasks. In the learned composition space, Generative Skill Chaining (CoRL 2023) uses diffusion models for skill precondition/effect chaining, and SCaR (NeurIPS 2024) learns success predictors for sub-task transitions—but both target fixed-base manipulation without dynamics-aware feasibility for whole-body locomotion+manipulation coupling. The gap is precise: no system combines (1) a grammar for compositional loco-manipulation task generation with (2) a learned transition feasibility predictor that captures humanoid-specific coupled dynamics at primitive boundaries—as opposed to post-hoc LLM/VLM evaluation (RoboGene, FATE) or exhaustive simulation—enabling (3) active generation of training data for the AGILE/GR00T-WBC ecosystem and downstream foundation models like Ψ₀.",
  "landscape": "**LLM-based environment/curriculum generation**: Eurekaverse (arXiv:2411.01775, CoRL 2024) uses LLM code generation to produce increasingly challenging terrain environments for quadruped parkour, with agent-environment co-evolution over 5 generations. Key paradigm: LLM generates Python terrain functions → train policy → evaluate → feedback to LLM. However, it generates monolithic terrain programs for single-skill locomotion—no manipulation, no inter-primitive dynamics, no compositional task structure. CompLocoGen extends this paradigm to compositional multi-stage loco-manipulation: instead of varying a single environment, we compose multi-primitive task sequences and learn which compositions are dynamically feasible. Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) uses LLM-powered scene generation with RAG-based asset retrieval and DSL code generation to create thousands of diverse environments for humanoid manipulation across 200+ tasks—but lacks formal compositional grammar and shows performance degradation on multi-step tasks (~52% vs ~80% for atomic tasks). **Feasibility-aware task generation (key concurrent work)**: RoboGene (arXiv:2602.16444, Feb 2026) introduces a diversity-driven agentic framework with three specialized LLM-based evaluators: a Physical Feasibility Evaluator (kinematic reachability, physics law compliance), a Novelty Evaluator (object complexity, temporal depth), and a Constraint Adherence Evaluator (scene-task consistency). Its LFU (Least Frequently Used) sampling ensures balanced coverage across under-explored task regions. RoboGene achieves 63.2% object coverage and 91.5% skill coverage across 18K trajectories on UR-5e, Franka, and AgileX platforms. Critical differentiation: RoboGene's feasibility evaluation is LLM-based and post-hoc (generate → evaluate → self-reflect → refine); CompLocoGen's TFN is a learned GNN that predicts feasibility upfront from boundary state features, capturing physical dynamics that LLMs cannot assess (centroidal momentum coupling, contact force propagation at transitions). RoboGene targets general manipulation without humanoid-specific whole-body coupling. We include a RoboGene-adapted baseline (LLM-based feasibility evaluation applied to grammar-generated humanoid compositions) to directly compare learned vs. LLM-based feasibility assessment. FATE (arXiv:2603.01505, March 2026) proposes closed-loop feasibility-aware generation with a sequential VLM auditing pipeline: static alignment (reachability, affordance, physical plausibility) followed by dynamic alignment (execution monitoring with rollback-and-repair). FATE achieves 92.1% feasible task rate on a RidgebackFranka in Isaac Sim. Critical differentiation: FATE evaluates individual task instances post-hoc via VLM perception; CompLocoGen predicts compositional feasibility upfront from learned transition dynamics—the TFN scores an entire primitive sequence in milliseconds without simulation, enabling efficient search over the exponential composition space. FATE's per-task VLM auditing scales linearly with proposals; TFN-based filtering is amortized after training. FATE targets mobile manipulation (7-DoF arm + holonomic base); CompLocoGen targets humanoid whole-body control where locomotion-manipulation coupling is qualitatively different. **LLM-based reward design (per-task optimization)**: STRIDE (arXiv:2502.04692, Feb 2025) automates humanoid locomotion reward design via LLMs, 250% over EUREKA—single-task locomotion only. FORGE (OpenReview 2025) uses multi-agent LLMs for evolutionary reward refinement, 38.5% over EUREKA—single-task. EUREKA (ICLR 2024) established the LLM-to-reward-code paradigm. These solve per-task reward engineering; CompLocoGen solves the orthogonal problem of generating novel task compositions with learned feasibility prediction. **Demonstration-based data generation**: DemoHLM (arXiv:2510.11258) generates diverse humanoid loco-manipulation trajectories from a single teleoperated demonstration by converting to object-centric representations and replaying under varied initial conditions with a 3-stage pipeline (locomotion → pre-manipulation → manipulation) on Unitree G1. It produces spatial diversity within a fixed task template—not compositional novelty across task structures. CompLocoGen generates qualitatively different training data: novel task compositions (e.g., walk-pick-carry-climb_stairs-place) that no single demonstration could cover. **Learned skill composition approaches**: Generative Skill Chaining (arXiv:2401.03360, CoRL 2023) trains skill-level diffusion models capturing (precondition, parameters, effect) distributions for chaining—fixed-base manipulation only. SCaR (NeurIPS 2024) refines skill chaining with learned success predictors for sub-task transitions. GSC (Robotics & Autonomous Systems, 2024) models skill sets as GNN graphs with transformer-style architecture for skill embeddings. SuperDyno (ICLR 2025 Workshop) learns differentiable neural dynamics for humanoid whole-body control. None of these address composition feasibility for coupled loco-manipulation where locomotion dynamics (balance, gait) interact with manipulation state (load, grasp). CompLocoGen's Transition Feasibility Network operates specifically on the boundary states between loco-manipulation primitives, learning to predict whether locomotion-manipulation coupling will cause failure at transitions. **Sim-to-real composite tasks**: VIRAL/GR00T-VisualSim2Real (CVPR 2026, NVlabs) demonstrates composite loco-manipulation with 54 consecutive real-world cycles—hand-designed tasks. LHM-Humanoid (arXiv:2508.16943, March 2026) learns unified policies across 350 manually designed scenes via RL teacher distillation. FALCON (arXiv:2505.06776, L4DC 2026) demonstrates force-adaptive dual-agent RL for loco-manipulation on real humanoids—hand-designed tasks. **Foundation models as downstream consumers**: Ψ₀ (arXiv:2603.12263, RSS 2026) is an open foundation model for universal humanoid loco-manipulation using staged VLM pre-training on egocentric human video followed by flow-based action expert fine-tuning on robot data. Ψ₀ achieves 40%+ over GR00T-N1.6 and can acquire new loco-manipulation skills from only 80 trajectories. CompLocoGen could serve as an automated training data generator for Ψ₀-class models—the compositionally diverse tasks it produces are precisely the data these foundation models need to achieve broader generalization. WholeBodyVLA (ICLR 2026, arXiv:2512.11047) learns unified latent VLA for whole-body control—another downstream consumer. SkillBlender (arXiv:2506.09366) demonstrates compositional skill blending on G1 with 4 primitive skills (walking, reaching, squatting, stepping) across 8 benchmark tasks—manually specified. CompLocoGen's grammar could automate task generation for SkillBlender-style systems. **Scene graph and compositional approaches**: Scene Graph Atomic Skills (ICRA 2026, Harvard) uses GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition—tabletop manipulation focus. GenManip (CVPR 2025) provides LLM-to-simulation-to-filter for tabletop manipulation. Humanoid Hanoi (arXiv:2602.13850, Feb 2026) demonstrates distribution shift during skill composition requiring data aggregation—directly informs our transition modeling. **The specific gap**: No system combines grammar-structured compositional task generation with a learned transition feasibility predictor for humanoid loco-manipulation. RoboGene and FATE achieve feasibility-aware generation via LLM/VLM post-hoc evaluation for tabletop/mobile manipulation; CompLocoGen introduces learned upfront prediction via GNN that captures humanoid-specific coupled dynamics. Eurekaverse generates single-skill environments; DemoHLM augments single demonstrations; Generative Skill Chaining/GSC learn feasibility for fixed-base manipulation; VIRAL/LHM-Humanoid use manually designed compositions. CompLocoGen uniquely combines: (a) a 7-primitive grammar generating exponentially many task compositions, (b) a GNN-based Transition Feasibility Network that learns loco-manipulation coupling dynamics from few-shot simulation rollouts, and (c) active generation targeting the uncertainty frontier of the feasibility predictor.",
  "approach": "We build CompLocoGen as a grammar-structured system that learns transition feasibility for compositional loco-manipulation task generation, producing Isaac Lab-compatible configurations within 220 H100-hours.\n\n**Expanded Physics-Informed Skill Grammar (7 Primitives)**: We define a context-free grammar over seven coupled loco-manipulation primitives: walk(target_pos, speed, gait_style), pick(object_id, grasp_type, approach_vector), place(target_pos, placement_constraint), carry(object_id, carry_pose, stability_mode), push(object_id, direction, force_profile), open_door(door_id, handle_type, opening_angle), and squat(target_height, duration, stability_mode). Each primitive has typed spatial parameters, structural preconditions/postconditions, and a boundary state specification (the distribution of robot states—CoM position/velocity, joint configurations, contact states, grasp forces—at primitive entry/exit). The 7-primitive grammar produces 7^L valid structural sequences of length L (before feasibility filtering). For L=3-5 (typical loco-manipulation tasks), this yields 343-16,807 structural compositions. With parameter variation (3-5 settings per typed parameter), the effective task space is 10^4-10^6 unique configurations. Structural filtering (precondition/postcondition satisfaction) reduces this by ~60%; dynamic feasibility filtering further reduces by an experimentally measured factor—quantifying this reduction IS the key experimental result.\n\n**Transition Feasibility Network (TFN) — Core Algorithmic Contribution**: Instead of relying on analytical physics predicates (ZMP, centroidal dynamics) or post-hoc LLM/VLM evaluation (as in RoboGene and FATE), we introduce a GNN-based Transition Feasibility Network that learns to predict composition success probability from primitive boundary states. Architecture: Each primitive instance is a node with features encoding (primitive type, spatial parameters, expected boundary state statistics). Edges connect consecutive primitives in the composition. A message-passing GNN (3 layers, 128-dim) processes the composition graph and outputs per-edge transition feasibility scores in [0,1] plus an overall composition feasibility score. The TFN's advantages over alternative feasibility approaches: (a) vs. analytical predicates: captures non-obvious interaction effects that simplified models miss (e.g., arm momentum during open_door affecting walking balance), improves with data rather than requiring manual engineering per primitive type; (b) vs. LLM-based evaluation (RoboGene-style): provides calibrated continuous scores rather than binary judgments, runs in milliseconds rather than requiring LLM API calls per composition, captures physical dynamics (centroidal momentum, contact forces) that language models cannot assess; (c) vs. VLM-based auditing (FATE-style): predicts upfront rather than evaluating post-hoc, handles compositional structure (scores full sequences via message-passing) rather than per-task evaluation; (d) vs. monolithic learned models: the grammar structure means it only needs to learn local transition dynamics (O(P^2) transition types for P primitives = 49 for 7 primitives), not global task success from all possible sequences (exponential in length).\n\n**TFN Training — Three-Phase Protocol**: (1) Bootstrap: Seed the TFN with ~200 simulation rollouts (50 per transition type for the 4 most common transitions: walk→pick, pick→carry, carry→walk, walk→place) using analytical predicates to stratify sampling across feasible/infeasible boundary. (2) Active Learning: Use TFN uncertainty (MC-dropout variance) to identify which transition types and parameter regions have highest prediction uncertainty. Allocate simulation budget preferentially to these uncertain regions. After each batch of 50 rollouts, retrain TFN. (3) Generalization Testing: We hypothesize that primitive-type-agnostic physical features (CoM velocity, contact forces, joint torques at boundaries) enable few-shot transfer to novel primitive types (push, open_door, squat). Quantifying the number of rollouts needed per novel primitive type to achieve reliable prediction (target: >85% AUROC) IS a key experimental result, not a design assumption. We budget 20-30 rollouts per new transition type as an optimistic starting point, with 10-20 additional H100-hours of contingency compute if generalization requires more data. If few-shot transfer fails entirely, we fall back to full active learning for all 7 primitives (~49 transition types), which remains feasible within the 220 H100-hour budget.\n\n**LLM-Guided Task Program Generation with Grammar Constraints**: The LLM (Qwen 3.6-35B-A3B) generates task programs as grammar-valid primitive sequences with spatial parameter bindings. The LLM reasons about task semantics (delivery routes, obstacle navigation, sequential manipulation schedules) while the grammar enforces structural validity and the TFN provides differentiable feasibility scores for soft-constraining the LLM's parameter choices. Generated programs are compiled into Isaac Lab Python @configclass environment configurations using AGILE's configuration-driven architecture: each becomes a self-contained file specifying scene setup, observation space, action space, staged reward functions (auto-generated from primitive sequence structure following VIRAL's stage-weighted approach), termination conditions, and curriculum parameters.\n\n**Active Composition Generation Loop**: Inspired by Eurekaverse's co-evolution but targeting compositional diversity rather than single-skill difficulty: (1) Generate batch of grammar-valid compositions via LLM. (2) TFN scores each composition; compositions above threshold proceed to simulation, compositions below threshold are rejected, compositions in the uncertain band are prioritized for simulation (active learning). (3) Simulate accepted compositions in Isaac Lab (4096 parallel environments). (4) Update TFN with new rollout data. (5) LLM receives feedback on which compositions succeeded/failed and why (structured failure mode analysis: balance failure, grasp loss, collision, timeout). This loop iterates for ~10 generations, progressively expanding the frontier of achievable compositions.\n\n**Pre-trained GR00T-WBC Execution**: Leverages the latest GEAR-SONIC (Feb 2026) pre-trained locomotion checkpoint and GR00T-WBC's PinkKinematics IK for upper-body manipulation, compatible with the GR00T N1.7 end-to-end VLA workflow (released May 2026). State-machine coordinator sequences SONIC commands and IK targets based on primitive transitions. For primitives requiring novel coordination (push, open_door), fine-tune with <5 H100-hours per primitive type using AGILE's training pipeline.\n\n**Downstream Evaluation with Compositional Generalization**: Train diffusion policy (ACT architecture) on generated datasets. Evaluate: (a) held-out compositions (novel primitive sequences), (b) held-out spatial configurations, (c) held-out dynamic parameters, (d) novel primitive types added post-training. Baselines: (1) Eurekaverse-style single-skill environment co-evolution (adapted to loco-manipulation), (2) DemoHLM-style demo augmentation (single demo per task → spatial variations), (3) STRIDE-style per-task reward optimization for composed tasks, (4) Grammar-only composition with analytical predicates (no TFN), (5) Grammar + TFN without active learning (random composition sampling), (6) LLM-only generation without grammar constraints, (7) LHM-Humanoid-style manually designed task set (5-8 hand-designed compositions), (8) RoboGene-adapted: replace TFN with three LLM-based feasibility evaluators (physical, novelty, constraint adherence) applied to grammar-generated humanoid compositions—directly isolating the value of learned GNN prediction vs. LLM-based evaluation within the same compositional framework. Key ablations: TFN vs. analytical predicates (measures value of learning), active vs. random sampling (measures value of uncertainty-guided generation), grammar structure vs. unstructured composition (measures value of grammatical scaffold for learning), TFN generalization curve (measures rollouts needed per novel primitive type).",
  "resource_estimate": {
    "venue_strategy": "We target Humanoids 2026 (paper deadline July 24, 2026 — 75 days from today, per 2026.ieee-humanoids.org) as the primary venue. This is the ideal venue for this work: Humanoids specifically values humanoid-focused systems contributions with algorithmic novelty, and the 75-day timeline comfortably accommodates the full evaluation (7 primitives, active learning loop, 8 baselines, 4 ablations). CoRL 2026 (abstract May 26, paper May 29 — 16-19 days) was considered but rejected for two reasons: (1) A CoRL-minimal submission (3 primitives, bootstrap TFN only, no active learning, no ablations) would demonstrate TFN feasibility prediction in principle but lack the evaluation depth to be competitive at CoRL's acceptance rate (~25%). The TFN's core value proposition is that grammar structure makes transition feasibility learnable and that active learning efficiently explores the composition space—neither can be demonstrated with only 3 primitives and bootstrap training. (2) The 19-day timeline is incompatible with rigorous experimentation: grammar implementation + TFN architecture + SONIC integration + bootstrap data collection + composition evaluation + 8-page paper, with zero margin for debugging the inevitable GEAR-SONIC integration issues. A rushed submission risks a desk rejection on evaluation grounds. CoRL 2027 is targeted for an extended version with real-robot transfer experiments and formal sample complexity analysis.",
    "manual": {
      "gpu_hours": "~200-220h H100 (includes 10-20h contingency for TFN generalization)",
      "gpu_utilization": "25-35% effective; researcher idles GPU while designing grammar, implementing TFN architecture, debugging GEAR-SONIC integration, and iterating active learning loop",
      "timeline": "7-8 weeks (1.5 weeks grammar design + TFN architecture + GEAR-SONIC integration, 2 weeks TFN training + active generation loop, 2 weeks downstream training + evaluation, 1.5 weeks ablations + paper). Fits comfortably within 75-day Humanoids deadline with ~2 weeks buffer.",
      "team": "1 researcher (requires familiarity with Isaac Lab, GNN training, and AGILE/GR00T-WBC)",
      "estimated_gpu_cost": "$500-550 at ~$2.50/hr H100 spot pricing"
    },
    "human_in_loop": {
      "gpu_hours": "~190-220h H100 (includes 10-20h contingency for TFN generalization)",
      "gpu_utilization": "55-70%; agent automates configclass generation, TFN training loops, experiment scheduling; idles during human review of TFN architecture decisions and generated task quality",
      "timeline": "6-7 weeks (targeting Humanoids 2026 July 24 deadline, 75 days, with ~3 weeks buffer)",
      "team": "1 researcher, ~25-35min/day reviewing TFN training curves, generated compositions, and demonstration quality",
      "claude_api_cost": "$200-400 (2000-4000 agentic turns for Isaac Lab compilation, TFN training orchestration, and experiment analysis)",
      "estimated_gpu_cost": "$475-550 at ~$2.50/hr H100 spot pricing",
      "budget_breakdown": "~10h TFN bootstrap data collection (200 rollouts x 4096 envs), ~5h TFN training (GNN, fast on single GPU), ~5h GEAR-SONIC fine-tuning for push/open_door/squat, ~60h active generation loop (10 generations x ~6h per generation: LLM generation + simulation verification + TFN update), ~60h downstream diffusion policy training, ~40h ablations (8 baselines + 4 key ablations), ~10-20h contingency for TFN generalization testing, ~10h buffer/iteration",
      "risk_note": "Primary risk: TFN may not generalize to novel primitive types from 20-30 rollouts. This is framed as a key experimental hypothesis, not an assumption. Mitigation: architecture uses primitive-type-agnostic physical features; contingency budget of 10-20h for additional rollouts if generalization requires more data. Worst case (no transfer): full active learning for all 49 transition types remains within budget. Secondary risk: GEAR-SONIC checkpoint may need more than 5h fine-tuning for push/open_door primitives."
    },
    "auto_research": {
      "gpu_hours": "~210-220h H100 (budget-constrained, includes contingency)",
      "gpu_utilization": "80-90%; agent operates continuously, prioritizing TFN active learning loop",
      "timeline": "3-4 weeks with 4 H100 GPUs concurrently (well within 75-day Humanoids deadline)",
      "team": "0 (initial 3-hour setup: configure AGILE, verify GEAR-SONIC checkpoint, set LLM API keys, define TFN architecture)",
      "claude_api_cost": "$350-750 (3500-7500 turns for autonomous pipeline development, TFN training, active generation, and paper drafting)",
      "estimated_gpu_cost": "$525-550 at ~$2.50/hr H100 spot pricing",
      "speed_bottleneck": "Active learning loop requires sequential TFN updates between generation batches; physics verification throughput (4096 envs per H100, ~15 wall-clock hours for 1000 valid demonstrations)",
      "risk_note": "Agent may over-explore TFN architecture variants vs. downstream evaluation; strict budget requires early stopping. TFN generalization testing requires careful allocation of contingency compute."
    }
  },
  "target_venues": [
    "Humanoids 2026 (paper deadline July 24, 2026 — 75 days, primary target. Ideal venue: humanoid-specific systems+algorithmic contribution, values both the grammar engineering and TFN learning contribution; conference Dec 6-9, Santa Clara CA. Full 7-primitive evaluation with active learning and all ablations.)",
    "CoRL 2027 (expected deadline ~May 2027 — extended version with real-robot transfer via AGILE's sim-to-real pipeline, formal sample complexity bounds for grammar-structured feasibility learning, TFN generalization analysis across additional primitive types, and comparison with Ψ₀ as downstream consumer)",
    "ICRA 2027 (expected deadline ~September 2026 — alternative venue if Humanoids review feedback suggests major revisions; allows additional baselines and potential RoboGene direct comparison)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Eurekaverse: Environment Curriculum Generation via Large Language Models (CoRL 2024, arXiv:2411.01775, NVIDIA Research) — LLM-driven environment co-evolution for single-skill locomotion training; generates terrain programs for quadruped parkour. Key paradigm ancestor. Differentiation: single-skill environment variation vs. our compositional multi-stage task generation with learned transition dynamics",
    "VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation (CVPR 2026, arXiv:2511.15200, NVlabs) — hand-designed composite tasks on G1 with 54 consecutive real-world cycles; identifies reward engineering as scaling bottleneck. Primary comparison",
    "RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation (arXiv:2602.16444, Feb 2026) — diversity-driven agentic framework with three LLM-based feasibility evaluators (physical, novelty, constraint adherence) and LFU sampling; generates 18K trajectories across 900 tasks on UR-5e/Franka/AgileX. Key concurrent work in feasibility-aware task generation. Differentiation: LLM-based post-hoc evaluation vs. learned GNN upfront prediction; general manipulation vs. humanoid-specific coupled dynamics; free-form generation vs. compositional grammar structure. Adapted as baseline 8",
    "FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula (arXiv:2603.01505, March 2026) — closed-loop VLM auditing (static scene validation + dynamic execution monitoring) with active repair on RidgebackFranka in Isaac Sim; achieves 92.1% feasible task rate. Key concurrent work. Differentiation: per-task post-hoc VLM auditing vs. compositional upfront GNN prediction; individual tasks vs. multi-stage sequences; mobile manipulation vs. humanoid whole-body control",
    "Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (arXiv:2603.12263, RSS 2026) — staged VLM pre-training on egocentric human video + flow-based action expert fine-tuning; 40%+ over GR00T-N1.6, acquires new skills from 80 trajectories. Key downstream consumer: CompLocoGen's generated compositional tasks could serve as training data for Ψ₀-class foundation models",
    "DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (arXiv:2510.11258) — generates diverse trajectories from single demo via object-centric representation replay on Unitree G1. Produces spatial variations within fixed task template. Key data-generation baseline: demonstrates demo-augmentation cannot produce compositional novelty",
    "AGILE: A Comprehensive Workflow for Humanoid Loco-Manipulation Learning (arXiv:2603.20147, March 2026, github.com/nvidia-isaac/WBC-AGILE, Apache 2.0) — target substrate; configuration-driven Isaac Lab workflow. CompLocoGen generates upstream training task configurations",
    "GR00T-WholeBodyControl/GEAR-SONIC (NVlabs, open-source Apache 2.0, GEAR-SONIC released Feb 2026, GR00T N1.7 VLA workflow May 2026) — pre-trained G1 locomotion checkpoints (142K+ motions), decoupled WBC with UNITREE_G1_SONIC embodiment",
    "Generative Skill Chaining: Long-Horizon Skill Planning with Diffusion Models (arXiv:2401.03360, CoRL 2023) — trains skill-level diffusion models for precondition/effect-based chaining in fixed-base manipulation. Informs our TFN's per-edge feasibility prediction but does not address loco-manipulation coupling",
    "GSC: A Graph-based Skill Composition Framework for Robot Learning (Robotics & Autonomous Systems, 2024) — GNN over skill graphs with transformer-style architecture. Architectural inspiration for our Transition Feasibility Network",
    "SCaR: Refining Skill Chaining for Long-Horizon Robotic Manipulation (NeurIPS 2024) — learned success predictors for sub-task transitions; validates that transition feasibility can be learned from few-shot rollouts",
    "SuperDyno: Scalable Humanoid Whole-Body Control via Differentiable Neural Network Dynamics (ICLR 2025 Workshop) — learns neural dynamics for humanoid control replacing analytical simulators. Validates that humanoid dynamics can be captured by neural networks",
    "Genie Sim 3.0 (arXiv:2601.02078, AgiBot, Jan 2026) — LLM-powered scene generation with 200+ tasks, 5140 assets. Large-scale generation without compositional grammar; performance degrades on multi-step tasks",
    "STRIDE: Automating Reward Design for Humanoid Robotics Locomotion (arXiv:2502.04692, Feb 2025) — automates single-task locomotion reward design via LLMs, 250% over EUREKA. Cannot compose multi-stage tasks",
    "FORGE: Forging Better Rewards via Multi-Agent LLM Framework (OpenReview 2025) — multi-agent LLM reward evolution, 38.5% over EUREKA. Single-task; does not address task composition",
    "EUREKA: Human-Level Reward Design via Coding LLMs (ICLR 2024, arXiv:2310.12931) — established LLM reward optimization paradigm",
    "LHM-Humanoid: Learning a Unified Policy for Long-Horizon Humanoid Whole-Body Loco-Manipulation (arXiv:2508.16943, March 2026) — 350 diverse scenes, RL teacher + DAgger. Manually designed scenes; CompLocoGen could serve as automated task generator",
    "WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026, arXiv:2512.11047) — policy architecture orthogonal to task generation; downstream consumer",
    "FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation (arXiv:2505.06776, L4DC 2026) — force-adaptive dual-agent RL on real humanoids; validates deployability, hand-designed tasks",
    "SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending (arXiv:2506.09366) — hierarchical RL with 4 primitive skills on G1/H1, 8 benchmark tasks; manually specified. CompLocoGen's grammar could automate task generation for SkillBlender-style systems",
    "Scene Graph Atomic Skills (ICRA 2026, Harvard) — GNN + diffusion for compositional skill execution addressing distribution shifts from scene composition; tabletop focus",
    "Humanoid Hanoi (arXiv:2602.13850, Feb 2026) — distribution shift during skill composition; directly informs our transition feasibility learning",
    "GenManip: LLM-driven Simulation for Generalizable Manipulation (CVPR 2025) — LLM-to-simulation-to-filter paradigm for tabletop manipulation",
    "GR00T-Gen (NVIDIA, 2025) — generates 100+ individual tasks, not compositionally coupled",
    "Isaac Lab (arXiv:2511.04831) — Python @configclass manager-based workflow for environment specification"
  ],
  "description": "We propose CompLocoGen, a system that combines a physics-informed skill grammar with a learned Transition Feasibility Network (TFN) to automatically generate diverse humanoid loco-manipulation training environments for NVIDIA's AGILE/Isaac Lab ecosystem—within 220 H100-hours. The core algorithmic contribution is the TFN: a GNN-based model that learns to predict whether primitive transitions in a composed task sequence will succeed, trained via active learning from targeted simulation rollouts at primitive boundaries. This positions CompLocoGen distinctly from concurrent feasibility-aware generation systems: RoboGene (Feb 2026) uses LLM-based post-hoc evaluation for general manipulation; FATE (March 2026) uses VLM-based auditing with active repair for mobile manipulation. CompLocoGen instead provides learned upfront prediction via GNN that captures humanoid-specific coupled dynamics (centroidal momentum, contact forces at transition boundaries)—operating in milliseconds per composition and improving with data rather than requiring LLM/VLM inference per proposal. The grammar provides structure that makes transition feasibility learnable from O(100) rollouts per transition type: instead of learning global task success (exponential), the TFN learns local boundary dynamics (quadratic in primitive count). We define a 7-primitive grammar (walk, pick, place, carry, push, open_door, squat) producing 10^4-10^6 parametrized compositions, and quantify how structural filtering, analytical predicates, and learned TFN filtering progressively reduce this space to dynamically feasible tasks. We hypothesize that primitive-type-agnostic physical features enable few-shot TFN transfer to novel primitive types; quantifying the generalization curve IS a key experimental result, with contingency compute budgeted if transfer requires more data than anticipated. An active generation loop (inspired by Eurekaverse's co-evolution but targeting compositional diversity) iteratively expands the frontier of achievable compositions. Generated task programs compile to Isaac Lab @configclass configurations. Execution leverages GEAR-SONIC (Feb 2026) pre-trained locomotion and GR00T-WBC's PinkKinematics IK. Evaluation compares against 8 baselines including a RoboGene-adapted baseline (LLM-based feasibility evaluation applied to grammar-generated compositions) that directly isolates the value of learned vs. LLM-based feasibility assessment—with key ablations isolating the value of learned feasibility, active sampling, grammar structure, and TFN generalization. Generated tasks could serve as training data for downstream foundation models like Ψ₀ (RSS 2026). Primary target: Humanoids 2026 (July 24, 75 days).",
  "project_name": "llm_locomanip_factory",
  "source": "web_research"
}
```

---

## Summary of changes (major revision)

**Issue-by-issue resolution:**

1. **CRITICAL: Venue/timeline** — Decisively committed to **Humanoids 2026 (July 24, 75 days)** as primary. Added explicit `venue_strategy` field justifying why CoRL 2026 (19 days) would produce a suboptimal submission: a 3-primitive bootstrap-only paper lacks the evaluation depth to demonstrate the TFN's core value (compositional scaling + active learning). CoRL 2027 becomes the extended version target.

2. **RoboGene** — Added throughout: core_problem, opportunity, landscape (detailed differentiation: LLM-based post-hoc vs. learned GNN upfront; general manipulation vs. humanoid-specific dynamics), and as **baseline 8** (RoboGene-adapted: LLM evaluators applied to grammar-generated humanoid compositions, directly isolating learned vs. LLM-based feasibility).

3. **FATE** — Added throughout with detailed differentiation: per-task VLM auditing vs. compositional upfront GNN prediction; linear scaling vs. amortized inference; mobile manipulation vs. humanoid whole-body control.

4. **Ψ₀** — Added as downstream consumer in opportunity and landscape. CompLocoGen's generated tasks are precisely the diverse training data Ψ₀-class foundation models need.

5. **TFN generalization reframed** — Changed from design assumption to **key experimental hypothesis**: "Quantifying the number of rollouts needed per novel primitive type IS a key experimental result, not a design assumption." Added 10-20h contingency compute and explicit fallback (full active learning for all 49 transition types if few-shot transfer fails).

6. **Humanoids 2026 deadline corrected** — Fixed to **July 24, 2026** (75 days), verified against official website.

7. **Generative Skill Chaining venue corrected** — Fixed to **CoRL 2023** (confirmed via arXiv page: "Accepted at CoRL 2023").

**Additional improvements**: Updated SONIC references to GEAR-SONIC (Feb 2026) and GR00T N1.7 (May 2026); added SkillBlender context; expanded baselines from 7 to 8; added TFN generalization curve as a 4th ablation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f2ebccc-d97e-4104-959d-14a03847a123",
  "isSidechain": false,
  "requestId": "req_011CauTVBHA53nG9AgGgqQ7s",
  "type": "assistant",
  "uuid": "a5169abc-ff17-4605-9622-8783adc7db01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyNHSM4ZYEK1dBwvdxH1ZQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9528,
      "cache_read_input_tokens": 61640,
      "output_tokens": 9888,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9888,
          "cache_read_input_tokens": 61640,
          "cache_creation_input_tokens": 9528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9528
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 85_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Co…",
  "leafUuid": "a5169abc-ff17-4605-9622-8783adc7db01",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Runtime record

_source line 86_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise CoRL 2026 scope or justify Humanoids 2026 timeline",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Runtime record

_source line 87_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"CompLocoGen: Grammar-Structured Transition Feasibility Learning for Co…",
  "leafUuid": "a5169abc-ff17-4605-9622-8783adc7db01",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---

### Runtime record

_source line 88_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise CoRL 2026 scope or justify Humanoids 2026 timeline",
  "sessionId": "2be61ec6-9efe-434d-aca6-59a9c3e9409c"
}
```

---
