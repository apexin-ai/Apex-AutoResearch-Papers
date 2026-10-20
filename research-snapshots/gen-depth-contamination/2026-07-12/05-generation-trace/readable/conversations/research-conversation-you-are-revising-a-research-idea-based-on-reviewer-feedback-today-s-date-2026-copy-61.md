# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/d0aef627-83d9-4adc-aaf2-81b51c36b38c.jsonl`
- **Structured JSON:** [`f636c936e2f1ab15fa4c.json`](../../sessions/f6/f636c936e2f1ab15fa4c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:24:34.918Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:24:34.918Z",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Frozen-WAM Best-of-N: Plug-in Inference-Time Candidate Selection for Pretrained World Action Models via Action-Latent Value Learning\",\n  \"core_problem\": \"Pretrained WAMs generate a single action trajectory at inference and cannot explicitly compare candidate futures. Adding planning capability currently requires one of three costly interventions: (1) full fine-tuning of the video model on robot demos (Cosmos Policy, ICLR 2026: 384–3,072 H100-hours for full WAM retraining); (2) training a separate action-conditioned world model alongside the frozen policy (GPC, RAL 2025); or (3) architectural co-design or RL loops (H-WM, GigaBrain RAMP). Fast-WAM (arXiv 2603.16666) demonstrates that test-time video generation adds only 0.5–1.9 percentage points over action-only inference — achieving 97.6% on LIBERO and 91.8% on RoboTwin at 190ms latency — motivating efficient action-latent candidate generation rather than expensive full video trajectory generation. However, Fast-WAM still generates a single trajectory and provides no mechanism to compare or select among candidates. The key open problem is: given that WAM action-only inference is already fast and high-quality (per Fast-WAM), can we add Best-of-N candidate selection using only the WAM's own action latent space, without retraining WAM weights or training a separate world model, and at total additional training cost ≤40 H100-hours? No existing work provides this.\",\n  \"opportunity\": \"UWM's independent per-modality diffusion timestep architecture (RSS 2025) natively supports action-only inference (policy mode: video timestep = T, action timestep = 0 for full denoising of action tokens only), inheriting Fast-WAM's efficiency with no video generation overhead. Sampling B=4–8 action-only trajectories from the frozen WAM using independent Gaussian noise seeds produces diverse manipulation strategies — different approach angles, grasp orientations, sub-task orderings — that differ in quality in proportion to task difficulty. A 3-layer value MLP trained on WAM action latent encodings of success AND failure demonstrations scores each candidate. Hard argmax selection (Best-of-N: a_{i*} = argmax_i V(z_{a,i})) is the primary result, explicitly chosen to avoid the multi-modal action-averaging artifact: when B sampled trajectories approach a grasp from different sides, averaging produces a geometrically infeasible middle path, while hard selection picks the best strategy. This artifact is well-documented in the Diffusion Policy paper (Chi et al., 2023) and confirmed as a known failure mode for weighted averaging over multi-modal manipulation distributions. Soft MPPI weighting (w_i ∝ exp(β·V(z_{a,i}))) is retained as an ablation to empirically characterize when soft averaging might outperform hard selection (e.g., low-variance, near-unimodal trajectory distributions). A critical prerequisite not present in prior versions of this proposal: LIBERO-90 contains only successful demonstrations — negative examples must be explicitly generated via online rollout failures of the frozen UWM policy in simulation (~15–20 H100-hours) supplemented by Gaussian-perturbed synthetic failures. Total additional training cost: ≤40 H100-hours (20 failure collection + 15 demo encoding + 5 MLP training). The primary evaluation is RoboCasa (67.1% for fully fine-tuned Cosmos Policy at 1,536 H100-hours), where frozen WAM single-trajectory baselines are expected around 40–55%, providing meaningful headroom. The research question: does plug-in Best-of-N with a value MLP trained in ≤40 H100-hours close the gap to fine-tuned WAM performance on hard benchmarks, without modifying any WAM weight?\",\n  \"landscape\": \"Cosmos Policy (arXiv 2601.16163, ICLR 2026) is the closest prior work and primary comparison point. It fully fine-tunes Cosmos-Predict2-2B (all weights) on robot demos — 384 H100-hours for ALOHA, 1,536 for RoboCasa, 3,072 for LIBERO — then uses the fine-tuned model as a planning model with best-of-N over 15 ensemble value predictions per action. Achieves 98.5% LIBERO and 67.1% RoboCasa. Architecture-specific to Cosmos-Predict2; not plug-in compatible with other WAMs; requires full retraining per domain. Our method keeps all WAM weights frozen and costs ≤40 H100-hours.\\n\\nFast-WAM (arXiv 2603.16666, May 2026) is the most critical new work for positioning. It demonstrates that test-time video generation contributes only 0.5–1.9 percentage points: Fast-WAM achieves 97.6% LIBERO-avg (Spatial: 98.2%, Object: 100%, Goal: 97%, Long: 95.2%) and 91.8% RoboTwin WITHOUT generating any video at inference, at 190ms latency (4× faster than imagine-then-execute WAMs). Ablation shows removing video co-training causes much larger drops (4.1 pts LIBERO, 8 pts RoboTwin) than removing test-time video generation (0.5–1.9 pts). CRITICAL DISTINCTION: Fast-WAM generates a single action trajectory and provides no candidate comparison mechanism. Our method builds on Fast-WAM's insight — we also use action-only inference (no video generation at test time) for candidate generation — and adds Best-of-N candidate selection with a learned value MLP. Fast-WAM targets latency-critical deployment (single trajectory, fastest possible); Frozen-WAM BoN targets success-critical tasks (B trajectories, select best). Complementary operating points on the latency–success Pareto frontier. Fast-WAM's 95.2% on LIBERO-Long without embodied pretraining confirms LIBERO-Long is near saturation for strong WAMs; RoboCasa (67.1% for fine-tuned Cosmos) is therefore the more informative primary benchmark with meaningful headroom.\\n\\nGPC (arXiv 2502.00622, IEEE RAL 2025) augments a frozen diffusion policy with a separately trained action-conditioned world model; GPC-RANK generates multiple action proposals, unrolls through the world model, and selects via hard argmax — requiring training both a policy and a separate world model plus random exploration rollouts for WM training. Our method uses the WAM's own action latent space as the evaluation substrate (no separate world model) and requires only demonstration-derived training data (not exploration rollouts).\\n\\n'When to Trust Imagination: Adaptive Action Execution for World Action Models' (arXiv 2605.06222, May 2026) is concurrent work in the same WAM inference space. FFDC (Future Forward Dynamics Causal Attention) adaptively determines action chunk sizes during execution of a single trajectory, deciding when predictions remain trustworthy versus when to replan earlier. Achieves 69% reduction in forward passes, 34% faster execution, 2.54% SR improvement on RoboTwin, and 35% real-world improvement. CRITICAL DISTINCTION: FFDC operates within execution of a single trajectory (in-execution adaptation); our method selects among B candidate trajectories before execution begins (pre-execution selection). Orthogonal and combinable: use our value MLP to select the best of B candidates at planning time, then use FFDC to adaptively replan during execution.\\n\\nOA-WAM (arXiv 2605.06481, May 2026): object-addressable manipulation via addressable object slots. Different problem (object binding in multi-object scenes); achieves 97.8% LIBERO, 79.3% SimplerEnv. Not related to inference-time planning.\\n\\nCKT-WAM (arXiv 2605.06247, May 2026): parameter-efficient knowledge transfer between WAMs via text-embedding-space distillation using <2% trainable parameters. Achieves 86.1% LIBERO-Plus, 83.3% real-world. Different problem (cross-WAM adaptation), not related to inference-time planning.\\n\\nChEaP (arXiv 2603.30043) demonstrates early plan commitment in video diffusion for 2D maze navigation; not validated for manipulation. Our method does not rely on partial denoising or early commitment.\\n\\nDreamZero (arXiv 2602.15922): single joint video+action trajectories via 14B DiT, ~3s/chunk optimized. Secondary backbone in our cross-WAM evaluation.\\n\\nGigaBrain-0.5M* (arXiv 2602.12099) uses RAMP RL loops requiring 30%+ more training. H-WM (arXiv 2602.11291) requires hierarchical architectural co-design. Compositional Planning with Jumpy World Models (arXiv 2602.19634) requires WM training from scratch. PiJEPA (arXiv 2603.25981) applies MPPI over deterministic JEPA latents for navigation. Latent Diffusion Planning (arXiv 2504.16925) trains a diffusion planner from scratch.\\n\\nNo prior work applies Best-of-N hard argmax selection over B=4–8 action-only trajectories from a completely frozen pretrained video-diffusion WAM, using a value MLP trained on WAM action latents from explicitly collected success/failure demonstrations, without retraining the WAM or training a separate world model, demonstrated on RoboCasa and LIBERO-Long manipulation benchmarks.\",\n  \"approach\": \"Primary backbone: UWM (github.com/WEIRDLabUW/unified-world-model, RSS 2025), whose independent per-modality diffusion timestep architecture natively supports action-only inference (policy mode: video timestep = T, action timestep = 0). Secondary backbone: DreamZero-14B (GEAR-Dreams/DreamZero-DROID), for cross-WAM plug-in validation using full video+action denoising. All WAM weights frozen throughout.\\n\\nStep 0 — Failure Demonstration Collection (NEW — required for value MLP training): LIBERO-90 contains only successful human teleoperation demonstrations; binary success/failure classification requires explicit negative examples. Two approaches: (a) Primary negatives — run frozen UWM policy (action-only mode, B=1) on LIBERO-Long and RoboCasa tasks in MuJoCo/RoboCasa simulation. Frozen UWM (not fine-tuned on LIBERO/RoboCasa) is expected to fail on ~30–50% of RoboCasa tasks and ~5–15% of LIBERO-Long tasks, yielding 500–2,000 failure trajectories from ~2,000–4,000 total rollouts. Estimated cost: 15–20 H100-hours for rollout collection. (b) Synthetic supplement — apply Gaussian action perturbation (σ ∈ {0.05, 0.1}) to 20% of successful LIBERO-90 demos, simulate perturbed episodes in MuJoCo, flag truncated episodes as failures. Cost: <1 H100-hour (simulation-only). Combine both sources for balanced 2,000–4,000 positive / 2,000–4,000 negative training set.\\n\\nDiversity Pilot Experiment (NEW — mandatory pre-ablation diagnostic): Before the main ablation, validate the discriminability premise: sample B=16 action-only trajectories from frozen UWM on 3 RoboCasa tasks using different Gaussian noise seeds, execute each in simulation, record ground-truth success/failure, then measure: (1) pairwise cosine distance of action latents {z_{a,i}} — if mean < 0.05, increase noise temperature T_noise to {1.5, 2.0} or add diverse language paraphrases; (2) Spearman correlation of V(z_{a,i}) with ground-truth success after MLP training — target ρ > 0.3 for meaningful Best-of-N gains over random; (3) variance of V(z_{a,i}) across B=16 samples — std(V) < 0.05 indicates near-uniform weights degenerate to random selection. Presented as a required diagnostic figure in the paper.\\n\\nStep 1 — Demo Encoding: Encode all LIBERO-90 success demonstrations (4,500 demos) plus collected failures through frozen UWM in action-only mode (video timestep = T, action timestep = 0), obtaining clean WAM action latents z_a. Label with success/failure. Cost: ~10–15 H100-hours.\\n\\nStep 2 — Value MLP Training: Train a 3-layer MLP (input: flattened action latent z_a; output: scalar V ∈ [0,1]) via binary cross-entropy on balanced success/failure latents. Cost: ~3–5 H100-hours. Total additional training cost: ≤40 H100-hours.\\n\\nStep 3 — Inference-Time Best-of-N Planning: At each planning step, sample B=4–8 action-only trajectories from frozen UWM using independent Gaussian noise seeds. Score each with V(z_{a,i}). PRIMARY result: hard argmax Best-of-N: a_{i*} = argmax_i V(z_{a,i}). ABLATION only: soft MPPI w_i ∝ exp(β·V(z_{a,i})), output Σ_i w_i·a_i — retained specifically to document that soft averaging underperforms hard argmax on multi-modal manipulation tasks (action-averaging artifact). Inference regimes: (a) open-loop — B trajectories at episode start, execute selected; (b) periodic replanning — replan every K=5 action chunks (~8–10s intervals).\\n\\nAblation Grid: B ∈ {1, 2, 4, 8, 16} (B=1 is frozen WAM single-trajectory baseline, equivalent to Fast-WAM-style inference); selection method: hard argmax (primary) vs. soft MPPI β ∈ {0.5, 1, 2, 5} vs. random selection; noise temperature T_noise ∈ {1.0, 1.5, 2.0} (informed by diversity pilot); action-only latent scoring vs. full video+action latent scoring (ablation of whether video component adds scoring value); value MLP: 2-layer vs. 3-layer vs. 4-layer.\\n\\nPrimary hypothesis: Hard argmax Best-of-N over B=4–8 UWM action-latent candidates improves RoboCasa success rate by ≥10 percentage points over single-trajectory baseline, approaching Cosmos Policy fine-tuned performance (67.1%) at 40× lower training cost. Soft MPPI underperforms hard argmax on RoboCasa's multi-modal manipulation tasks.\\n\\nEvaluation Benchmarks: (a) Primary — RoboCasa: Cosmos Policy fine-tuned at 1,536 H100-hours achieves 67.1%; expected frozen WAM single-trajectory baseline ~40–55%. Best-of-N target: ≥60%. Core comparison: ≤40 H100-hours training vs. 1,536 H100-hours fine-tuning. (b) Secondary — LIBERO-Long: acknowledged near saturation (Fast-WAM 95.2% without embodied pretraining); included to characterize Best-of-N gains as a function of baseline task difficulty and to show method works across difficulty regimes. Baselines: single-trajectory WAM (B=1), random selection (B=4–8), GPC-RANK-style argmax over random scoring, Cosmos Policy published results (cited, not reproduced).\\n\\nCross-WAM Generalization (DreamZero-14B, secondary): full video+action denoising (action-only mode not directly available in DreamZero), B=4, open-loop planning only. Score using joint video+action latent. Validates plug-in claim across two distinct WAM architectures.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180h H100\",\n      \"gpu_utilization\": \"HIGH idle (~40–60%): GPU waits while researcher implements action-only inference wrapper, debugs failure collection pipeline, designs ablations, and interprets results between runs\",\n      \"timeline\": \"2–4 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$450 (180h × $2.50/h blended Lambda/RunPod/Vast.ai H100 rate)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~220h H100\",\n      \"gpu_utilization\": \"MODERATE idle (~20–30%): agent handles code scaffolding, failure collection, demo encoding, and experiment submission continuously; human approves diversity pilot results and ablation scope at daily check-ins\",\n      \"timeline\": \"4–6 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$150–250 (~1,500–2,500 turns at mixed Sonnet/Opus rates)\",\n      \"estimated_gpu_cost\": \"~$550 (220h × $2.50/h)\",\n      \"risk_note\": \"Step 0 (failure collection, ~15–20 H100-hours) creates a hard sequential dependency before value MLP training can begin. Diversity pilot may reveal low action-latent variance requiring noise temperature tuning before main ablation runs. RoboCasa simulation environment setup may require significant engineering effort separate from LIBERO. DreamZero-14B cross-WAM evaluation (~50 H100-hours) is secondary and can be dropped if CoRL timeline is tight — the plug-in claim can rest on UWM alone for the initial submission.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~550h H100 (both UWM and DreamZero-14B backbones; full B/β/T_noise ablation grid; RoboCasa + LIBERO-Long evaluations; multiple seeds)\",\n      \"gpu_utilization\": \"MINIMAL idle (~5–10%): agent pipelines failure collection, demo encoding, MLP training, evaluation, and logging continuously\",\n      \"timeline\": \"10–14 days with 4–8 H100 GPUs simultaneously\",\n      \"team\": \"0 (only initial repo setup and credential configuration)\",\n      \"claude_api_cost\": \"$250–450 (~3,000–5,000 turns at Opus rates)\",\n      \"estimated_gpu_cost\": \"~$1,375 (550h × $2.50/h)\",\n      \"speed_bottleneck\": \"Step 0 failure collection and diversity pilot create hard sequential dependencies that prevent full pipeline parallelization. RoboCasa evaluation rollouts: each ablation variant requires sequential per-task evaluation (3–5h per variant); with 4 GPUs running 4 variants concurrently, the full grid needs ~8–10 days minimum.\",\n      \"risk_note\": \"UWM action-only inference mode is architecturally supported (video timestep = T) but the exact code-level API may require implementation not present in the public UWM repository. DreamZero-14B's multi-GPU NCCL setup requires specific configuration. RoboCasa and LIBERO simulation environments do not share a rollout API — agent may spend significant effort unifying the data collection pipeline across environments.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (Abstract deadline: May 26, 2026; Full paper: May 29, 2026; Conference: Nov 9–12, Austin TX) — EXTREMELY TIGHT: 19 days from 2026-05-10. Step 0 failure collection must begin immediately. Minimum viable submission: RoboCasa Best-of-N results (primary) + LIBERO-Long secondary + diversity pilot figure + B/hard-vs-soft ablation. DreamZero cross-WAM can be deferred to camera-ready or ICLR.\",\n    \"ICLR 2027 (deadline ~September–October 2026; not yet officially announced as of 2026-05-10) — More feasible timeline for complete ablation grid, both WAM backbones, and potential real-world experiments.\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning (arXiv 2601.16163, ICLR 2026) — CRITICAL PRIOR WORK: full fine-tune of Cosmos-Predict2-2B (1,536 H100-hours for RoboCasa), 98.5% LIBERO, 67.1% RoboCasa; not plug-in compatible with other WAMs; our method targets ≥60% RoboCasa at ≤40 H100-hours\",\n    \"Fast-WAM: World Action Models without Test-Time Video (arXiv 2603.16666, May 2026) — CRITICAL NEW WORK: test-time video generation adds only 0.5–1.9 pts (97.6% LIBERO, 91.8% RoboTwin without video at inference, 190ms latency); single trajectory only, no candidate comparison; our method builds on this by using action-only inference for fast B-candidate generation and adding Best-of-N selection; also confirms LIBERO-Long near-saturation (95.2%), motivating RoboCasa as primary benchmark\",\n    \"When to Trust Imagination: Adaptive Action Execution for World Action Models (arXiv 2605.06222, May 2026) — SIGNIFICANT CONCURRENT WORK: FFDC adaptively decides when to replan during single-trajectory execution (in-execution adaptation); 69% fewer forward passes, 2.54% SR improvement on RoboTwin; orthogonal to our pre-execution Best-of-N; the two can be combined\",\n    \"Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling / GPC (arXiv 2502.00622, IEEE RAL 2025) — CRITICAL PRIOR WORK: frozen policy + separately trained world model + hard argmax (GPC-RANK); our method replaces separate WM with WAM's own action latent scoring\",\n    \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (arXiv 2303.04137, RSS 2023 / IJRR 2024) — documents multi-modal action distribution handling; confirms averaging over manipulation action modes produces infeasible blended actions; justifies hard argmax as primary result over soft MPPI weighting\",\n    \"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets / UWM (arXiv 2504.02792, RSS 2025) — primary backbone; independent per-modality timesteps natively support action-only inference (video timestep = T, confirmed in paper); publicly available weights and code\",\n    \"World Action Models are Zero-shot Policies / DreamZero (arXiv 2602.15922) — 14B joint video+action DiT, ~3s/chunk optimized; secondary backbone for cross-WAM plug-in validation\",\n    \"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv 2605.06481, May 2026) — concurrent work; different problem (object binding consistency); 97.8% LIBERO, 79.3% SimplerEnv\",\n    \"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models (arXiv 2605.06247, May 2026) — concurrent work; different problem (cross-WAM knowledge transfer with <2% trainable parameters)\",\n    \"Video Models Reason Early: Exploiting Plan Commitment for Maze Solving / ChEaP (arXiv 2603.30043) — early commitment in 2D mazes only; our method does not rely on partial denoising\",\n    \"GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning (arXiv 2602.12099) — RAMP RL loop requires 30%+ more training\",\n    \"H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model (arXiv 2602.11291) — requires architectural co-design\",\n    \"Compositional Planning with Jumpy World Models (arXiv 2602.19634) — requires WM training from scratch\",\n    \"Policy-Guided World Model Planning for Language-Conditioned Visual Navigation / PiJEPA (arXiv 2603.25981) — MPPI over deterministic JEPA latents for navigation, not manipulation\",\n    \"Latent Diffusion Planning for Imitation Learning (arXiv 2504.16925) — trains diffusion planner from scratch\"\n  ],\n  \"description\": \"Frozen-WAM Best-of-N (FW-BoN) converts any pretrained video-diffusion World Action Model into an inference-time multi-candidate planner without modifying a single WAM weight, building on Fast-WAM's finding that action-only inference (no test-time video generation) matches full video generation in quality. At each planning step, B=4–8 diverse action trajectories are sampled from the frozen WAM in action-only mode (UWM: video timestep = T, action timestep = 0), producing clean action latents at Fast-WAM-comparable speed with no video denoising overhead. A 3-layer value MLP — trained in ≤40 H100-hours on WAM action latent encodings of LIBERO-90 success demonstrations AND explicitly collected failure trajectories (online rollout failures from frozen UWM in simulation: ~15–20 H100-hours, plus Gaussian-perturbed synthetic failures) — scores each candidate. Hard argmax Best-of-N (a_{i*} = argmax_i V(z_{a,i})) is the primary result, explicitly chosen to avoid the multi-modal action-averaging artifact documented in the Diffusion Policy paper: soft MPPI weighting (w_i ∝ exp(β·V(z_{a,i}))) is retained as an ablation to empirically confirm that averaging over multi-modal manipulation trajectories produces infeasible blended actions in exactly the settings where Best-of-N gains are largest. A mandatory diversity pilot (B=16 on 3 RoboCasa tasks: pairwise cosine distance + V-score–success Spearman correlation) validates the discriminability premise before the main ablation. Primary evaluation: RoboCasa, where fine-tuned Cosmos Policy achieves 67.1% at 1,536 H100-hours; target is ≥60% at ≤40 H100-hours — approaching fine-tuned performance at 40× lower cost. Secondary: LIBERO-Long (near saturation for strong frozen WAMs per Fast-WAM's 95.2%, included to characterize gains vs. baseline difficulty). Cross-WAM validation: DreamZero-14B (full video+action denoising, B=4, open-loop). Key differentiators: (1) zero WAM retraining vs. 1,536 H100-hours for Cosmos Policy; (2) no separate world model vs. GPC-RANK; (3) builds on rather than competes with Fast-WAM — same action-only inference efficiency, adds candidate selection; (4) hard argmax Best-of-N over action latents with explicit action-averaging artifact ablation; (5) plug-in compatibility across two WAM architectures.\",\n  \"project_name\": \"frozen_wam_mppi\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 3)\nIssues: [\"SIGNIFICANT — Three important related papers are completely absent from the landscape: (1) RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Models (arXiv 2510.10975): generates B candidate actions from a frozen VLA, scores with a trained Process Reward Model (PRM), and selects via argmax — evaluated on CALVIN + real robot (GR-1, Dita, MoDE backbones). Different policy class (VLA not WAM) and benchmark (CALVIN not LIBERO/RoboCasa), but the paradigm is essentially identical. Must be cited and differentiated. (2) Verifier-free Test-Time Sampling for Vision Language Action Models (arXiv 2510.05681, ICLR 2026): Best-of-N for frozen VLAs using KL-divergence from a masked reference distribution as a confidence signal — no additional training required; achieves 168% relative improvement on pick-and-place. Differentiator: no trained value model; applicable to VLAs not WAMs. Must be cited. (3) Compose Your Policies! (arXiv 2510.01068): test-time policy composition for diffusion/flow-based robot policies without retraining, using score composition. Must be cited.\", \"CRITICAL — Frozen UWM baseline on RoboCasa is an unvalidated assumption that may be dramatically wrong. The UWM paper (RSS 2025, arXiv 2504.02792) evaluates primarily on LIBERO and OXE-distribution tasks; no published RoboCasa-without-fine-tuning results exist. Cosmos Policy achieves 67.1% on RoboCasa only after 1,536 H100-hours of domain-specific fine-tuning. A frozen UWM — not fine-tuned on RoboCasa's kitchen tasks — achieving 40-55% baseline success seems optimistic; 15-30% is more plausible. If the actual baseline is 15-30%, the ≥60% target requires +30-45pp from a 3-layer MLP scoring action latents, which is almost certainly too large. The Generator should: (a) run a quick 50-episode RoboCasa baseline with frozen UWM before committing to ≥60% target; (b) recalibrate the target to 'improve baseline by ≥10pp' rather than 'approach Cosmos Policy 67.1%' if baseline is lower than expected.\", \"SIGNIFICANT — The World-Value-Action (WAV) model (arXiv 2604.14732, April 2026) proposes a trajectory value function that 'evaluates long-horizon utility' and generates actions via 'inference in latent space where the model progressively concentrates probability mass on high-value trajectories.' This is substantially overlapping in motivation (value scoring over latent trajectory representations) though architecturally different (implicit latent inference vs. discrete Best-of-N selection). Should be cited and explicitly differentiated: WAV modifies the VLA architecture; this proposal keeps all weights frozen.\", \"MODERATE — Novelty argument is insufficiently grounded for CoRL acceptance. The technical differentiation from RoVer reduces to: (a) WAM action latents vs. VLA action space, (b) UWM action-only mode vs. standard policy, (c) LIBERO/RoboCasa vs. CALVIN. These are valid engineering differences but unlikely to meet CoRL's bar for conceptual novelty. The proposal needs a sharper 'why WAM action latents?' argument — specifically, that the WAM's joint video-action pretraining instills physical grounding into the action latent z_a that pure action-space policies lack, making the latent richer for value estimation. This would differentiate from RoVer on principled grounds, not just implementation.\", \"MODERATE — The DreamZero-14B cross-WAM evaluation is described as secondary but is essential for the 'plug-in across WAM architectures' claim. DreamZero-14B requires full video+action denoising (no native action-only mode), making B-trajectory sampling substantially more expensive than for UWM. If this experiment cannot be completed within the 20-day window (likely, given 50 H100-hours estimate), the 'plug-in' contribution collapses to a single-architecture result, significantly weakening the generalization claim. The Generator should either (a) commit to completing DreamZero validation within the timeline or (b) reframe the contribution as UWM-specific and drop the plug-in generalization claim.\", \"MODERATE — The feasibility of training a discriminative value MLP from action latents depends on a premise not yet verified: that frozen UWM action latents from successful and failed demonstrations are separable in the latent space. If UWM's action latent z_a primarily encodes task semantics (what to do) rather than execution quality (how well to do it), success/failure labels may be uncorrelated with latent structure and the MLP will learn a degenerate classifier. The diversity pilot (Spearman ρ > 0.3 target) partially addresses this, but binary classification accuracy on held-out demos should also be reported as a sanity check before the main ablation.\"]\nFeedback: The Round 3 revision has correctly addressed all three Round 2 critical issues: (1) hard argmax is now the primary result with solid justification, (2) Step 0 failure collection is explicitly specified at 15-20 H100-hours, and (3) Fast-WAM is now integrated as a complementary framing. The diversity pilot is a strong addition. However, three concrete fixes are needed before CoRL submission:\n\n**1. Add and differentiate three missing related papers (1-2 days).** You must cite RoVer (arXiv 2510.10975), Verifier-free Test-Time Sampling (ICLR 2026, arXiv 2510.05681), and Compose Your Policies! (arXiv 2510.01068) in your related work section. The differentiation argument for RoVer specifically should be: 'RoVer applies to VLA architectures in token-action space using an explicitly trained PRM; our method targets WAMs whose joint video-action pretraining produces physically grounded action latents z_a that are richer substrates for value estimation than action tokens from VLAs — we exploit this WAM-specific property to eliminate the need for a separate process reward model training stage.' Also cite WAV (arXiv 2604.14732) as addressing value-guided action selection within VLAs via implicit latent inference, and differentiate: 'WAV modifies the architecture; Frozen-WAM BoN leaves all weights frozen.'\n\n**2. Validate the frozen UWM baseline on RoboCasa before committing to ≥60% target (3-5 days, highest priority).** Run 50 episodes of B=1 frozen UWM action-only inference on a representative subset of RoboCasa tasks. If the baseline is 40-55%, the ≥60% target is appropriate. If it is 15-35% (which is equally plausible given no published UWM/RoboCasa results), you must: (a) adjust the target to 'improve baseline success rate by ≥10pp absolute,' and (b) reframe the comparison away from 'approaching fine-tuned Cosmos Policy (67.1%)' toward 'meaningful improvement over frozen WAM without any fine-tuning, at ≤40 H100-hours training.' The latter is still a publishable result; the former collapses if the baseline is too low.\n\n**3. Sharpen the theoretical motivation for WAM latents over action space (0.5 days).** Add one paragraph explaining why z_a from a jointly-trained video-action WAM contains more quality-discriminative information than the output action tokens of a VLA. The key insight: UWM's video diffusion process regularizes z_a to be consistent with physically plausible visual futures, instilling motion-physics grounding that raw VLA action tokens lack. This is why a 3-layer MLP over z_a can succeed where the same MLP over VLA output tokens would fail — and this is your fundamental novelty claim that differentiates Frozen-WAM BoN from RoVer at the conceptual level.\n\nMinimum viable CoRL submission: frozen UWM + RoboCasa Best-of-N (primary) + LIBERO-Long (secondary) + diversity pilot figure + B/hard-argmax ablation. Drop DreamZero cross-WAM to camera-ready — it adds a 50 H100-hour sequential dependency that cannot be completed before the diversity pilot results inform whether the premise holds.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 3 轮修订，近 3 轮的平均分从 3.0 到 3.2，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:24:34.922Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:24:34.922Z",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-10T08:24:34.945Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Frozen-WAM Best-of-N: Plug-in Inference-Time Candidate Selection for Pretrained World Action Models via Action-Latent Value Learning",
  "core_problem": "Pretrained WAMs generate a single action trajectory at inference and cannot explicitly compare candidate futures. Adding planning capability currently requires one of three costly interventions: (1) full fine-tuning of the video model on robot demos (Cosmos Policy, ICLR 2026: 384–3,072 H100-hours for full WAM retraining); (2) training a separate action-conditioned world model alongside the frozen policy (GPC, RAL 2025); or (3) architectural co-design or RL loops (H-WM, GigaBrain RAMP). Fast-WAM (arXiv 2603.16666) demonstrates that test-time video generation adds only 0.5–1.9 percentage points over action-only inference — achieving 97.6% on LIBERO and 91.8% on RoboTwin at 190ms latency — motivating efficient action-latent candidate generation rather than expensive full video trajectory generation. However, Fast-WAM still generates a single trajectory and provides no mechanism to compare or select among candidates. The key open problem is: given that WAM action-only inference is already fast and high-quality (per Fast-WAM), can we add Best-of-N candidate selection using only the WAM's own action latent space, without retraining WAM weights or training a separate world model, and at total additional training cost ≤40 H100-hours? No existing work provides this.",
  "opportunity": "UWM's independent per-modality diffusion timestep architecture (RSS 2025) natively supports action-only inference (policy mode: video timestep = T, action timestep = 0 for full denoising of action tokens only), inheriting Fast-WAM's efficiency with no video generation overhead. Sampling B=4–8 action-only trajectories from the frozen WAM using independent Gaussian noise seeds produces diverse manipulation strategies — different approach angles, grasp orientations, sub-task orderings — that differ in quality in proportion to task difficulty. A 3-layer value MLP trained on WAM action latent encodings of success AND failure demonstrations scores each candidate. Hard argmax selection (Best-of-N: a_{i*} = argmax_i V(z_{a,i})) is the primary result, explicitly chosen to avoid the multi-modal action-averaging artifact: when B sampled trajectories approach a grasp from different sides, averaging produces a geometrically infeasible middle path, while hard selection picks the best strategy. This artifact is well-documented in the Diffusion Policy paper (Chi et al., 2023) and confirmed as a known failure mode for weighted averaging over multi-modal manipulation distributions. Soft MPPI weighting (w_i ∝ exp(β·V(z_{a,i}))) is retained as an ablation to empirically characterize when soft averaging might outperform hard selection (e.g., low-variance, near-unimodal trajectory distributions). A critical prerequisite not present in prior versions of this proposal: LIBERO-90 contains only successful demonstrations — negative examples must be explicitly generated via online rollout failures of the frozen UWM policy in simulation (~15–20 H100-hours) supplemented by Gaussian-perturbed synthetic failures. Total additional training cost: ≤40 H100-hours (20 failure collection + 15 demo encoding + 5 MLP training). The primary evaluation is RoboCasa (67.1% for fully fine-tuned Cosmos Policy at 1,536 H100-hours), where frozen WAM single-trajectory baselines are expected around 40–55%, providing meaningful headroom. The research question: does plug-in Best-of-N with a value MLP trained in ≤40 H100-hours close the gap to fine-tuned WAM performance on hard benchmarks, without modifying any WAM weight?",
  "landscape": "Cosmos Policy (arXiv 2601.16163, ICLR 2026) is the closest prior work and primary comparison point. It fully fine-tunes Cosmos-Predict2-2B (all weights) on robot demos — 384 H100-hours for ALOHA, 1,536 for RoboCasa, 3,072 for LIBERO — then uses the fine-tuned model as a planning model with best-of-N over 15 ensemble value predictions per action. Achieves 98.5% LIBERO and 67.1% RoboCasa. Architecture-specific to Cosmos-Predict2; not plug-in compatible with other WAMs; requires full retraining per domain. Our method keeps all WAM weights frozen and costs ≤40 H100-hours.\n\nFast-WAM (arXiv 2603.16666, May 2026) is the most critical new work for positioning. It demonstrates that test-time video generation contributes only 0.5–1.9 percentage points: Fast-WAM achieves 97.6% LIBERO-avg (Spatial: 98.2%, Object: 100%, Goal: 97%, Long: 95.2%) and 91.8% RoboTwin WITHOUT generating any video at inference, at 190ms latency (4× faster than imagine-then-execute WAMs). Ablation shows removing video co-training causes much larger drops (4.1 pts LIBERO, 8 pts RoboTwin) than removing test-time video generation (0.5–1.9 pts). CRITICAL DISTINCTION: Fast-WAM generates a single action trajectory and provides no candidate comparison mechanism. Our method builds on Fast-WAM's insight — we also use action-only inference (no video generation at test time) for candidate generation — and adds Best-of-N candidate selection with a learned value MLP. Fast-WAM targets latency-critical deployment (single trajectory, fastest possible); Frozen-WAM BoN targets success-critical tasks (B trajectories, select best). Complementary operating points on the latency–success Pareto frontier. Fast-WAM's 95.2% on LIBERO-Long without embodied pretraining confirms LIBERO-Long is near saturation for strong WAMs; RoboCasa (67.1% for fine-tuned Cosmos) is therefore the more informative primary benchmark with meaningful headroom.\n\nGPC (arXiv 2502.00622, IEEE RAL 2025) augments a frozen diffusion policy with a separately trained action-conditioned world model; GPC-RANK generates multiple action proposals, unrolls through the world model, and selects via hard argmax — requiring training both a policy and a separate world model plus random exploration rollouts for WM training. Our method uses the WAM's own action latent space as the evaluation substrate (no separate world model) and requires only demonstration-derived training data (not exploration rollouts).\n\n'When to Trust Imagination: Adaptive Action Execution for World Action Models' (arXiv 2605.06222, May 2026) is concurrent work in the same WAM inference space. FFDC (Future Forward Dynamics Causal Attention) adaptively determines action chunk sizes during execution of a single trajectory, deciding when predictions remain trustworthy versus when to replan earlier. Achieves 69% reduction in forward passes, 34% faster execution, 2.54% SR improvement on RoboTwin, and 35% real-world improvement. CRITICAL DISTINCTION: FFDC operates within execution of a single trajectory (in-execution adaptation); our method selects among B candidate trajectories before execution begins (pre-execution selection). Orthogonal and combinable: use our value MLP to select the best of B candidates at planning time, then use FFDC to adaptively replan during execution.\n\nOA-WAM (arXiv 2605.06481, May 2026): object-addressable manipulation via addressable object slots. Different problem (object binding in multi-object scenes); achieves 97.8% LIBERO, 79.3% SimplerEnv. Not related to inference-time planning.\n\nCKT-WAM (arXiv 2605.06247, May 2026): parameter-efficient knowledge transfer between WAMs via text-embedding-space distillation using <2% trainable parameters. Achieves 86.1% LIBERO-Plus, 83.3% real-world. Different problem (cross-WAM adaptation), not related to inference-time planning.\n\nChEaP (arXiv 2603.30043) demonstrates early plan commitment in video diffusion for 2D maze navigation; not validated for manipulation. Our method does not rely on partial denoising or early commitment.\n\nDreamZero (arXiv 2602.15922): single joint video+action trajectories via 14B DiT, ~3s/chunk optimized. Secondary backbone in our cross-WAM evaluation.\n\nGigaBrain-0.5M* (arXiv 2602.12099) uses RAMP RL loops requiring 30%+ more training. H-WM (arXiv 2602.11291) requires hierarchical architectural co-design. Compositional Planning with Jumpy World Models (arXiv 2602.19634) requires WM training from scratch. PiJEPA (arXiv 2603.25981) applies MPPI over deterministic JEPA latents for navigation. Latent Diffusion Planning (arXiv 2504.16925) trains a diffusion planner from scratch.\n\nNo prior work applies Best-of-N hard argmax selection over B=4–8 action-only trajectories from a completely frozen pretrained video-diffusion WAM, using a value MLP trained on WAM action latents from explicitly collected success/failure demonstrations, without retraining the WAM or training a separate world model, demonstrated on RoboCasa and LIBERO-Long manipulation benchmarks.",
  "approach": "Primary backbone: UWM (github.com/WEIRDLabUW/unified-world-model, RSS 2025), whose independent per-modality diffusion timestep architecture natively supports action-only inference (policy mode: video timestep = T, action timestep = 0). Secondary backbone: DreamZero-14B (GEAR-Dreams/DreamZero-DROID), for cross-WAM plug-in validation using full video+action denoising. All WAM weights frozen throughout.\n\nStep 0 — Failure Demonstration Collection (NEW — required for value MLP training): LIBERO-90 contains only successful human teleoperation demonstrations; binary success/failure classification requires explicit negative examples. Two approaches: (a) Primary negatives — run frozen UWM policy (action-only mode, B=1) on LIBERO-Long and RoboCasa tasks in MuJoCo/RoboCasa simulation. Frozen UWM (not fine-tuned on LIBERO/RoboCasa) is expected to fail on ~30–50% of RoboCasa tasks and ~5–15% of LIBERO-Long tasks, yielding 500–2,000 failure trajectories from ~2,000–4,000 total rollouts. Estimated cost: 15–20 H100-hours for rollout collection. (b) Synthetic supplement — apply Gaussian action perturbation (σ ∈ {0.05, 0.1}) to 20% of successful LIBERO-90 demos, simulate perturbed episodes in MuJoCo, flag truncated episodes as failures. Cost: <1 H100-hour (simulation-only). Combine both sources for balanced 2,000–4,000 positive / 2,000–4,000 negative training set.\n\nDiversity Pilot Experiment (NEW — mandatory pre-ablation diagnostic): Before the main ablation, validate the discriminability premise: sample B=16 action-only trajectories from frozen UWM on 3 RoboCasa tasks using different Gaussian noise seeds, execute each in simulation, record ground-truth success/failure, then measure: (1) pairwise cosine distance of action latents {z_{a,i}} — if mean < 0.05, increase noise temperature T_noise to {1.5, 2.0} or add diverse language paraphrases; (2) Spearman correlation of V(z_{a,i}) with ground-truth success after MLP training — target ρ > 0.3 for meaningful Best-of-N gains over random; (3) variance of V(z_{a,i}) across B=16 samples — std(V) < 0.05 indicates near-uniform weights degenerate to random selection. Presented as a required diagnostic figure in the paper.\n\nStep 1 — Demo Encoding: Encode all LIBERO-90 success demonstrations (4,500 demos) plus collected failures through frozen UWM in action-only mode (video timestep = T, action timestep = 0), obtaining clean WAM action latents z_a. Label with success/failure. Cost: ~10–15 H100-hours.\n\nStep 2 — Value MLP Training: Train a 3-layer MLP (input: flattened action latent z_a; output: scalar V ∈ [0,1]) via binary cross-entropy on balanced success/failure latents. Cost: ~3–5 H100-hours. Total additional training cost: ≤40 H100-hours.\n\nStep 3 — Inference-Time Best-of-N Planning: At each planning step, sample B=4–8 action-only trajectories from frozen UWM using independent Gaussian noise seeds. Score each with V(z_{a,i}). PRIMARY result: hard argmax Best-of-N: a_{i*} = argmax_i V(z_{a,i}). ABLATION only: soft MPPI w_i ∝ exp(β·V(z_{a,i})), output Σ_i w_i·a_i — retained specifically to document that soft averaging underperforms hard argmax on multi-modal manipulation tasks (action-averaging artifact). Inference regimes: (a) open-loop — B trajectories at episode start, execute selected; (b) periodic replanning — replan every K=5 action chunks (~8–10s intervals).\n\nAblation Grid: B ∈ {1, 2, 4, 8, 16} (B=1 is frozen WAM single-trajectory baseline, equivalent to Fast-WAM-style inference); selection method: hard argmax (primary) vs. soft MPPI β ∈ {0.5, 1, 2, 5} vs. random selection; noise temperature T_noise ∈ {1.0, 1.5, 2.0} (informed by diversity pilot); action-only latent scoring vs. full video+action latent scoring (ablation of whether video component adds scoring value); value MLP: 2-layer vs. 3-layer vs. 4-layer.\n\nPrimary hypothesis: Hard argmax Best-of-N over B=4–8 UWM action-latent candidates improves RoboCasa success rate by ≥10 percentage points over single-trajectory baseline, approaching Cosmos Policy fine-tuned performance (67.1%) at 40× lower training cost. Soft MPPI underperforms hard argmax on RoboCasa's multi-modal manipulation tasks.\n\nEvaluation Benchmarks: (a) Primary — RoboCasa: Cosmos Policy fine-tuned at 1,536 H100-hours achieves 67.1%; expected frozen WAM single-trajectory baseline ~40–55%. Best-of-N target: ≥60%. Core comparison: ≤40 H100-hours training vs. 1,536 H100-hours fine-tuning. (b) Secondary — LIBERO-Long: acknowledged near saturation (Fast-WAM 95.2% without embodied pretraining); included to characterize Best-of-N gains as a function of baseline task difficulty and to show method works across difficulty regimes. Baselines: single-trajectory WAM (B=1), random selection (B=4–8), GPC-RANK-style argmax over random scoring, Cosmos Policy published results (cited, not reproduced).\n\nCross-WAM Generalization (DreamZero-14B, secondary): full video+action denoising (action-only mode not directly available in DreamZero), B=4, open-loop planning only. Score using joint video+action latent. Validates plug-in claim across two distinct WAM architectures.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180h H100",
      "gpu_utilization": "HIGH idle (~40–60%): GPU waits while researcher implements action-only inference wrapper, debugs failure collection pipeline, designs ablations, and interprets results between runs",
      "timeline": "2–4 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$450 (180h × $2.50/h blended Lambda/RunPod/Vast.ai H100 rate)"
    },
    "human_in_loop": {
      "gpu_hours": "~220h H100",
      "gpu_utilization": "MODERATE idle (~20–30%): agent handles code scaffolding, failure collection, demo encoding, and experiment submission continuously; human approves diversity pilot results and ablation scope at daily check-ins",
      "timeline": "4–6 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$150–250 (~1,500–2,500 turns at mixed Sonnet/Opus rates)",
      "estimated_gpu_cost": "~$550 (220h × $2.50/h)",
      "risk_note": "Step 0 (failure collection, ~15–20 H100-hours) creates a hard sequential dependency before value MLP training can begin. Diversity pilot may reveal low action-latent variance requiring noise temperature tuning before main ablation runs. RoboCasa simulation environment setup may require significant engineering effort separate from LIBERO. DreamZero-14B cross-WAM evaluation (~50 H100-hours) is secondary and can be dropped if CoRL timeline is tight — the plug-in claim can rest on UWM alone for the initial submission."
    },
    "auto_research": {
      "gpu_hours": "~550h H100 (both UWM and DreamZero-14B backbones; full B/β/T_noise ablation grid; RoboCasa + LIBERO-Long evaluations; multiple seeds)",
      "gpu_utilization": "MINIMAL idle (~5–10%): agent pipelines failure collection, demo encoding, MLP training, evaluation, and logging continuously",
      "timeline": "10–14 days with 4–8 H100 GPUs simultaneously",
      "team": "0 (only initial repo setup and credential configuration)",
      "claude_api_cost": "$250–450 (~3,000–5,000 turns at Opus rates)",
      "estimated_gpu_cost": "~$1,375 (550h × $2.50/h)",
      "speed_bottleneck": "Step 0 failure collection and diversity pilot create hard sequential dependencies that prevent full pipeline parallelization. RoboCasa evaluation rollouts: each ablation variant requires sequential per-task evaluation (3–5h per variant); with 4 GPUs running 4 variants concurrently, the full grid needs ~8–10 days minimum.",
      "risk_note": "UWM action-only inference mode is architecturally supported (video timestep = T) but the exact code-level API may require implementation not present in the public UWM repository. DreamZero-14B's multi-GPU NCCL setup requires specific configuration. RoboCasa and LIBERO simulation environments do not share a rollout API — agent may spend significant effort unifying the data collection pipeline across environments."
    }
  },
  "target_venues": [
    "CoRL 2026 (Abstract deadline: May 26, 2026; Full paper: May 29, 2026; Conference: Nov 9–12, Austin TX) — EXTREMELY TIGHT: 19 days from 2026-05-10. Step 0 failure collection must begin immediately. Minimum viable submission: RoboCasa Best-of-N results (primary) + LIBERO-Long secondary + diversity pilot figure + B/hard-vs-soft ablation. DreamZero cross-WAM can be deferred to camera-ready or ICLR.",
    "ICLR 2027 (deadline ~September–October 2026; not yet officially announced as of 2026-05-10) — More feasible timeline for complete ablation grid, both WAM backbones, and potential real-world experiments."
  ],
  "level": "solid",
  "key_references": [
    "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning (arXiv 2601.16163, ICLR 2026) — CRITICAL PRIOR WORK: full fine-tune of Cosmos-Predict2-2B (1,536 H100-hours for RoboCasa), 98.5% LIBERO, 67.1% RoboCasa; not plug-in compatible with other WAMs; our method targets ≥60% RoboCasa at ≤40 H100-hours",
    "Fast-WAM: World Action Models without Test-Time Video (arXiv 2603.16666, May 2026) — CRITICAL NEW WORK: test-time video generation adds only 0.5–1.9 pts (97.6% LIBERO, 91.8% RoboTwin without video at inference, 190ms latency); single trajectory only, no candidate comparison; our method builds on this by using action-only inference for fast B-candidate generation and adding Best-of-N selection; also confirms LIBERO-Long near-saturation (95.2%), motivating RoboCasa as primary benchmark",
    "When to Trust Imagination: Adaptive Action Execution for World Action Models (arXiv 2605.06222, May 2026) — SIGNIFICANT CONCURRENT WORK: FFDC adaptively decides when to replan during single-trajectory execution (in-execution adaptation); 69% fewer forward passes, 2.54% SR improvement on RoboTwin; orthogonal to our pre-execution Best-of-N; the two can be combined",
    "Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling / GPC (arXiv 2502.00622, IEEE RAL 2025) — CRITICAL PRIOR WORK: frozen policy + separately trained world model + hard argmax (GPC-RANK); our method replaces separate WM with WAM's own action latent scoring",
    "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (arXiv 2303.04137, RSS 2023 / IJRR 2024) — documents multi-modal action distribution handling; confirms averaging over manipulation action modes produces infeasible blended actions; justifies hard argmax as primary result over soft MPPI weighting",
    "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets / UWM (arXiv 2504.02792, RSS 2025) — primary backbone; independent per-modality timesteps natively support action-only inference (video timestep = T, confirmed in paper); publicly available weights and code",
    "World Action Models are Zero-shot Policies / DreamZero (arXiv 2602.15922) — 14B joint video+action DiT, ~3s/chunk optimized; secondary backbone for cross-WAM plug-in validation",
    "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv 2605.06481, May 2026) — concurrent work; different problem (object binding consistency); 97.8% LIBERO, 79.3% SimplerEnv",
    "CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models (arXiv 2605.06247, May 2026) — concurrent work; different problem (cross-WAM knowledge transfer with <2% trainable parameters)",
    "Video Models Reason Early: Exploiting Plan Commitment for Maze Solving / ChEaP (arXiv 2603.30043) — early commitment in 2D mazes only; our method does not rely on partial denoising",
    "GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning (arXiv 2602.12099) — RAMP RL loop requires 30%+ more training",
    "H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model (arXiv 2602.11291) — requires architectural co-design",
    "Compositional Planning with Jumpy World Models (arXiv 2602.19634) — requires WM training from scratch",
    "Policy-Guided World Model Planning for Language-Conditioned Visual Navigation / PiJEPA (arXiv 2603.25981) — MPPI over deterministic JEPA latents for navigation, not manipulation",
    "Latent Diffusion Planning for Imitation Learning (arXiv 2504.16925) — trains diffusion planner from scratch"
  ],
  "description": "Frozen-WAM Best-of-N (FW-BoN) converts any pretrained video-diffusion World Action Model into an inference-time multi-candidate planner without modifying a single WAM weight, building on Fast-WAM's finding that action-only inference (no test-time video generation) matches full video generation in quality. At each planning step, B=4–8 diverse action trajectories are sampled from the frozen WAM in action-only mode (UWM: video timestep = T, action timestep = 0), producing clean action latents at Fast-WAM-comparable speed with no video denoising overhead. A 3-layer value MLP — trained in ≤40 H100-hours on WAM action latent encodings of LIBERO-90 success demonstrations AND explicitly collected failure trajectories (online rollout failures from frozen UWM in simulation: ~15–20 H100-hours, plus Gaussian-perturbed synthetic failures) — scores each candidate. Hard argmax Best-of-N (a_{i*} = argmax_i V(z_{a,i})) is the primary result, explicitly chosen to avoid the multi-modal action-averaging artifact documented in the Diffusion Policy paper: soft MPPI weighting (w_i ∝ exp(β·V(z_{a,i}))) is retained as an ablation to empirically confirm that averaging over multi-modal manipulation trajectories produces infeasible blended actions in exactly the settings where Best-of-N gains are largest. A mandatory diversity pilot (B=16 on 3 RoboCasa tasks: pairwise cosine distance + V-score–success Spearman correlation) validates the discriminability premise before the main ablation. Primary evaluation: RoboCasa, where fine-tuned Cosmos Policy achieves 67.1% at 1,536 H100-hours; target is ≥60% at ≤40 H100-hours — approaching fine-tuned performance at 40× lower cost. Secondary: LIBERO-Long (near saturation for strong frozen WAMs per Fast-WAM's 95.2%, included to characterize gains vs. baseline difficulty). Cross-WAM validation: DreamZero-14B (full video+action denoising, B=4, open-loop). Key differentiators: (1) zero WAM retraining vs. 1,536 H100-hours for Cosmos Policy; (2) no separate world model vs. GPC-RANK; (3) builds on rather than competes with Fast-WAM — same action-only inference efficiency, adds candidate selection; (4) hard argmax Best-of-N over action latents with explicit action-averaging artifact ablation; (5) plug-in compatibility across two WAM architectures.",
  "project_name": "frozen_wam_mppi",
  "source": "web_research"
}

## Reviewer feedback (round 3)
Issues: ["SIGNIFICANT — Three important related papers are completely absent from the landscape: (1) RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Models (arXiv 2510.10975): generates B candidate actions from a frozen VLA, scores with a trained Process Reward Model (PRM), and selects via argmax — evaluated on CALVIN + real robot (GR-1, Dita, MoDE backbones). Different policy class (VLA not WAM) and benchmark (CALVIN not LIBERO/RoboCasa), but the paradigm is essentially identical. Must be cited and differentiated. (2) Verifier-free Test-Time Sampling for Vision Language Action Models (arXiv 2510.05681, ICLR 2026): Best-of-N for frozen VLAs using KL-divergence from a masked reference distribution as a confidence signal — no additional training required; achieves 168% relative improvement on pick-and-place. Differentiator: no trained value model; applicable to VLAs not WAMs. Must be cited. (3) Compose Your Policies! (arXiv 2510.01068): test-time policy composition for diffusion/flow-based robot policies without retraining, using score composition. Must be cited.", "CRITICAL — Frozen UWM baseline on RoboCasa is an unvalidated assumption that may be dramatically wrong. The UWM paper (RSS 2025, arXiv 2504.02792) evaluates primarily on LIBERO and OXE-distribution tasks; no published RoboCasa-without-fine-tuning results exist. Cosmos Policy achieves 67.1% on RoboCasa only after 1,536 H100-hours of domain-specific fine-tuning. A frozen UWM — not fine-tuned on RoboCasa's kitchen tasks — achieving 40-55% baseline success seems optimistic; 15-30% is more plausible. If the actual baseline is 15-30%, the ≥60% target requires +30-45pp from a 3-layer MLP scoring action latents, which is almost certainly too large. The Generator should: (a) run a quick 50-episode RoboCasa baseline with frozen UWM before committing to ≥60% target; (b) recalibrate the target to 'improve baseline by ≥10pp' rather than 'approach Cosmos Policy 67.1%' if baseline is lower than expected.", "SIGNIFICANT — The World-Value-Action (WAV) model (arXiv 2604.14732, April 2026) proposes a trajectory value function that 'evaluates long-horizon utility' and generates actions via 'inference in latent space where the model progressively concentrates probability mass on high-value trajectories.' This is substantially overlapping in motivation (value scoring over latent trajectory representations) though architecturally different (implicit latent inference vs. discrete Best-of-N selection). Should be cited and explicitly differentiated: WAV modifies the VLA architecture; this proposal keeps all weights frozen.", "MODERATE — Novelty argument is insufficiently grounded for CoRL acceptance. The technical differentiation from RoVer reduces to: (a) WAM action latents vs. VLA action space, (b) UWM action-only mode vs. standard policy, (c) LIBERO/RoboCasa vs. CALVIN. These are valid engineering differences but unlikely to meet CoRL's bar for conceptual novelty. The proposal needs a sharper 'why WAM action latents?' argument — specifically, that the WAM's joint video-action pretraining instills physical grounding into the action latent z_a that pure action-space policies lack, making the latent richer for value estimation. This would differentiate from RoVer on principled grounds, not just implementation.", "MODERATE — The DreamZero-14B cross-WAM evaluation is described as secondary but is essential for the 'plug-in across WAM architectures' claim. DreamZero-14B requires full video+action denoising (no native action-only mode), making B-trajectory sampling substantially more expensive than for UWM. If this experiment cannot be completed within the 20-day window (likely, given 50 H100-hours estimate), the 'plug-in' contribution collapses to a single-architecture result, significantly weakening the generalization claim. The Generator should either (a) commit to completing DreamZero validation within the timeline or (b) reframe the contribution as UWM-specific and drop the plug-in generalization claim.", "MODERATE — The feasibility of training a discriminative value MLP from action latents depends on a premise not yet verified: that frozen UWM action latents from successful and failed demonstrations are separable in the latent space. If UWM's action latent z_a primarily encodes task semantics (what to do) rather than execution quality (how well to do it), success/failure labels may be uncorrelated with latent structure and the MLP will learn a degenerate classifier. The diversity pilot (Spearman ρ > 0.3 target) partially addresses this, but binary classification accuracy on held-out demos should also be reported as a sanity check before the main ablation."]
Feedback: The Round 3 revision has correctly addressed all three Round 2 critical issues: (1) hard argmax is now the primary result with solid justification, (2) Step 0 failure collection is explicitly specified at 15-20 H100-hours, and (3) Fast-WAM is now integrated as a complementary framing. The diversity pilot is a strong addition. However, three concrete fixes are needed before CoRL submission:

**1. Add and differentiate three missing related papers (1-2 days).** You must cite RoVer (arXiv 2510.10975), Verifier-free Test-Time Sampling (ICLR 2026, arXiv 2510.05681), and Compose Your Policies! (arXiv 2510.01068) in your related work section. The differentiation argument for RoVer specifically should be: 'RoVer applies to VLA architectures in token-action space using an explicitly trained PRM; our method targets WAMs whose joint video-action pretraining produces physically grounded action latents z_a that are richer substrates for value estimation than action tokens from VLAs — we exploit this WAM-specific property to eliminate the need for a separate process reward model training stage.' Also cite WAV (arXiv 2604.14732) as addressing value-guided action selection within VLAs via implicit latent inference, and differentiate: 'WAV modifies the architecture; Frozen-WAM BoN leaves all weights frozen.'

**2. Validate the frozen UWM baseline on RoboCasa before committing to ≥60% target (3-5 days, highest priority).** Run 50 episodes of B=1 frozen UWM action-only inference on a representative subset of RoboCasa tasks. If the baseline is 40-55%, the ≥60% target is appropriate. If it is 15-35% (which is equally plausible given no published UWM/RoboCasa results), you must: (a) adjust the target to 'improve baseline success rate by ≥10pp absolute,' and (b) reframe the comparison away from 'approaching fine-tuned Cosmos Policy (67.1%)' toward 'meaningful improvement over frozen WAM without any fine-tuning, at ≤40 H100-hours training.' The latter is still a publishable result; the former collapses if the baseline is too low.

**3. Sharpen the theoretical motivation for WAM latents over action space (0.5 days).** Add one paragraph explaining why z_a from a jointly-trained video-action WAM contains more quality-discriminative information than the output action tokens of a VLA. The key insight: UWM's video diffusion process regularizes z_a to be consistent with physically plausible visual futures, instilling motion-physics grounding that raw VLA action tokens lack. This is why a 3-layer MLP over z_a can succeed where the same MLP over VLA output tokens would fail — and this is your fundamental novelty claim that differentiates Frozen-WAM BoN from RoVer at the conceptual level.

Minimum viable CoRL submission: frozen UWM + RoboCasa Best-of-N (primary) + LIBERO-Long (secondary) + diversity pilot figure + B/hard-argmax ablation. Drop DreamZero cross-WAM to camera-ready — it adds a 50 H100-hour sequential dependency that cannot be completed before the diversity pilot results inform whether the premise holds.

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
这个 idea 已经经过 3 轮修订，近 3 轮的平均分从 3.0 到 3.2，没有明显改善。

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
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "type": "user",
  "uuid": "c3807b4b-b774-40c2-8dc5-da4e8ee9b51f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:24:34.943Z_

```json
{
  "parentUuid": "c3807b4b-b774-40c2-8dc5-da4e8ee9b51f",
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
  "uuid": "e08a8f09-ac7d-4824-b30d-4272732fd9e3",
  "timestamp": "2026-05-10T08:24:34.943Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:24:34.943Z_

```json
{
  "parentUuid": "e08a8f09-ac7d-4824-b30d-4272732fd9e3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c3d26a82-f79f-4d8b-a191-8d50635e7981",
  "timestamp": "2026-05-10T08:24:34.943Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Frozen-WAM Best-of-N: Plug-in Inference-Time Candidate Selection for P…",
  "leafUuid": "c3d26a82-f79f-4d8b-a191-8d50635e7981",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate frozen UWM baseline before CoRL submission",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c"
}
```

---

### Assistant

_source line 8 · 2026-05-10T08:25:30.586Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this carefully. The idea has been through 3 rounds of revisions with minimal improvement (3.0 to 3.2 average score). The reviewer feedback is quite detailed and points to several issues:

1. **Missing related papers**: RoVer (arXiv 2510.10975), Verifier-free Test-Time Sampling (arXiv 2510.05681), Compose Your Policies! (arXiv 2510.01068), and WAV (arXiv 2604.14732)

2. **Critical**: Frozen UWM baseline on RoboCasa is an unvalidated assumption - the 40-55% baseline might actually be 15-30%


3. **Significant**: WAV model overlap in motivation
4. **Moderate**: Novelty argument is weak - the differentiation from RoVer reduces to engineering differences
5. **Moderate**: DreamZero cross-WAM evaluation essential for "plug-in" claim but likely infeasible
6. **Moderate**: Feasibility of discriminative value MLP from action latents not verified

Before I tackle these issues, I need to step back and assess whether the core concept even holds up. The approach relies on best-of-N selection over frozen WAM action latents using a trained value MLP, leveraging WAM's joint video-action representation as the key differentiator.

But there are some deeper structural problems here. First, if RoVer already achieves strong results with best-of-N over frozen VLAs, then my WAM-specific contribution is mostly just swapping in different latents—that's not compelling enough. Second, I'm uncertain whether a frozen UWM baseline can even reach 15-30% on RoboCasa, and if it can't, comparing against Cosmos Policy's 67.1% becomes meaningless. Third, my actual novel claim—that WAM action latents are richer because of joint video-action pretraining—is something I'm asserting rather than proving.

I should reconsider whether this framing is salvageable or if I need to pivot the whole approach.

The stagnation from 3.0 to 3.2 suggests something fundamental is off. What's actually worth keeping is the core insight: joint video-action pretraining in WAM creates physically grounded action representations, which is genuinely interesting. Maybe I should reframe around that directly instead of forcing it into a best-of-N plugin story.

I could go with a latent space analysis angle—showing that WAM action latents contain quality-discriminative information specifically because of the joint training, demonstrated through systematic comparison with VLA tokens. Or I could leverage the video side more cleverly by using frozen video latents as a value signal, since WAM can predict visual futures from actions.

But Option D is catching my attention: using WAM's video generation as a scorer rather than a policy. Generate an action trajectory, then generate the video conditioned on it, and use video coherence as a reward signal. That's genuinely WAM-specific—VLAs can't do this—and doesn't require training anything extra.

The approach would be sampling multiple action trajectories from the frozen WAM, running partial video denoising passes to assess consistency rather than full generation, and selecting based on video quality. This sidesteps training a value MLP, avoids latent separability assumptions, and doesn't depend on external demos. The main concern is test-time overhead, though partial denoising might keep it fast enough.

The reviewer's RoVer feedback is nagging at me though—if we're essentially doing the same paradigm, we need something genuinely different to justify the work.

Maybe the real insight is that joint video-action pretraining in WAMs creates action latents that are inherently more quality-discriminative than VLA action tokens, and we can exploit that property for better test-time selection. That's a cleaner research question that's actually WAM-specific. For a CoRL paper though, I need a concrete method with results, not just an empirical study.

The strongest angle: use the WAM's own video generation as the quality signal directly. Sample action trajectories and let the model's video predictions tell us which actions are most consistent. B action trajectories (fast, action-only mode)
2. For each action trajectory, run a short video denoising (partial, e.g., 10 steps) conditioned on that action
3. Score by video denoising loss (lower loss = action is more consistent with a plausible visual future)
4. Select argmax

This is:
- WAM-specific (VLAs can't do this)
- Training-free (no value MLP needed!)
- Theoretically principled (WAM's physics are embedded in video-action joint training)
- Differentiates from RoVer on principle, not implementation

The downside: adds video generation overhead back in. But partial denoising (10 steps) is much cheaper than full denoising (50+ steps). And it's conceptually clean.

This would be a **major revision** that addresses novelty, the latent separability concern, the DreamZero cross-WAM issue, and provides a physics-grounded quality signal through video denoising loss.

Now I'm wondering if this video denoising approach already exists in the literature—ChEaP uses early commitment in video diffusion, Fast-WAM argues video generation adds little at test time, and FFDC does adaptive replanning based on uncertainty. This could actually be an interesting counter-demonstration to Fast-WAM's claims about video generation overhead.

I need to search for existing work on video denoising as a quality or reward signal, and read through RoVer, Verifier-free, Compose Your Policies!, and WAV to make sure I'm not duplicating prior work. I'll need to do some parallel research to validate this direction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3d26a82-f79f-4d8b-a191-8d50635e7981",
  "isSidechain": false,
  "requestId": "req_011CatZsydkqZhV3iPZkcsma",
  "type": "assistant",
  "uuid": "0acc06b1-8207-49c2-b63a-d6881cd83abc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XPKCftDZi5U6DYerjoreAX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15306,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3156,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15306
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

_source line 9 · 2026-05-10T08:25:31.358Z_

I'll analyze this carefully before diving into fixes. Three rounds with minimal score improvement signals something deeper than surface patches. Let me research all the missing papers and concurrent work before deciding whether to refine or pivot.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0acc06b1-8207-49c2-b63a-d6881cd83abc",
  "isSidechain": false,
  "requestId": "req_011CatZsydkqZhV3iPZkcsma",
  "type": "assistant",
  "uuid": "cc9c044f-6e32-4dae-9e57-f5d24b817da9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XPKCftDZi5U6DYerjoreAX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15306,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3156,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15306
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

_source line 10 · 2026-05-10T08:25:36.157Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01P94tvKcGQk7uJPmu4Xncsf`</summary>

```json
{
  "description": "Read RoVer, Verifier-free, and WAV papers",
  "subagent_type": "Explore",
  "prompt": "Please fetch and summarize the following arXiv papers. For each, read the abstract, introduction, and method sections carefully. Report: (1) core method, (2) key results, (3) how it differentiates from \"Best-of-N over frozen WAM action latents with a trained value MLP.\"\n\n1. RoVer: Robot Reward Model as Test-Time Verifier - https://arxiv.org/abs/2510.10975\n2. Verifier-free Test-Time Sampling for Vision Language Action Models - https://arxiv.org/abs/2510.05681  \n3. World-Value-Action (WAV) model - https://arxiv.org/abs/2604.14732\n\nFor each paper, try both the abstract page (https://arxiv.org/abs/XXXX.XXXXX) and the HTML version (https://arxiv.org/html/XXXX.XXXXX). Report what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc9c044f-6e32-4dae-9e57-f5d24b817da9",
  "isSidechain": false,
  "requestId": "req_011CatZsydkqZhV3iPZkcsma",
  "type": "assistant",
  "uuid": "ca20648a-a5c8-4b0c-bd2d-d30b1db8161c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XPKCftDZi5U6DYerjoreAX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15306,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3156,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15306
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

_source line 11 · 2026-05-10T08:25:41.797Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014BbK3fDtesEndmkyXicvri`</summary>

```json
{
  "description": "Read Compose Your Policies and search for video consistency as quality signal",
  "subagent_type": "Explore",
  "prompt": "Please do two tasks:\n\n1. Fetch and summarize \"Compose Your Policies!\" (arXiv 2510.01068) - read abstract and method. Report: core method, key results, and how it differs from \"Best-of-N hard argmax selection over frozen WAM action latents.\"\n\n2. Search for papers that use video/world model denoising loss or video consistency as a quality signal for robot action selection at test time. Search queries to try:\n   - \"video denoising quality reward robot policy\"\n   - \"world model consistency score action selection\"  \n   - \"video diffusion denoising loss reward robot\"\n   - \"world model self-consistency action scoring\"\n\nFor the search, use WebSearch to find any papers (2024-2026) that use a video/world model's own denoising reconstruction loss as a quality signal to rank or select among candidate robot actions. This is different from training a separate reward model - it uses the model's own reconstruction error.\n\nReport all relevant papers found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca20648a-a5c8-4b0c-bd2d-d30b1db8161c",
  "isSidechain": false,
  "requestId": "req_011CatZsydkqZhV3iPZkcsma",
  "type": "assistant",
  "uuid": "982df43d-aedf-4d1a-a73f-4622bd6ee99f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XPKCftDZi5U6DYerjoreAX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15306,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3156,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15306
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

_source line 12 · 2026-05-10T08:25:46.724Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017tCyySRRTkZkpPfii26jHa`</summary>

```json
{
  "description": "Search for UWM RoboCasa baseline and related test-time compute work",
  "subagent_type": "Explore",
  "prompt": "Please search for the following information:\n\n1. Any published results of UWM (Unified World Model, arXiv 2504.02792, RSS 2025) on RoboCasa benchmark - specifically success rates WITHOUT fine-tuning. Search:\n   - \"UWM RoboCasa\"\n   - \"unified world model RoboCasa zero-shot\"\n   - arXiv 2504.02792 citations mentioning RoboCasa\n\n2. Current state of Best-of-N / test-time compute scaling for robot policies - search for papers from 2025-2026:\n   - \"best of N robot policy test time\"\n   - \"test time compute scaling robot manipulation\"\n   - \"inference time scaling robot policy\"\n   - \"process reward model robot VLA\"\n\n3. Also fetch this paper and report its method: https://arxiv.org/abs/2510.10975 (RoVer)\n\nReport: what frozen WAM baseline on RoboCasa can be inferred, and what's the current landscape of test-time compute papers for robot policies."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "982df43d-aedf-4d1a-a73f-4622bd6ee99f",
  "isSidechain": false,
  "requestId": "req_011CatZsydkqZhV3iPZkcsma",
  "type": "assistant",
  "uuid": "3213910b-864d-48a0-99fa-c1c1a4609240",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XPKCftDZi5U6DYerjoreAX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15306,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3156,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3156,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15306
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

_source line 13 · 2026-05-10T08:26:00.571Z_

<details><summary>↩ Tool result · `toolu_01P94tvKcGQk7uJPmu4Xncsf`</summary>

```text
Excellent! I've successfully fetched all three papers. Here's a comprehensive summary:

---

## Paper 1: RoVer: Robot Reward Model as Test-Time Verifier (arXiv:2510.10975)

**Core Method:**
RoVer uses a Process Reward Model (PRM) as a test-time verifier for Vision-Language-Action models. The framework operates in three stages: (1) generate multiple candidate actions from the base policy, (2) expand candidates along PRM-predicted 6D refinement directions in action space, and (3) score all candidates and select the optimal action. The PRM is a compact model (0.2B parameters, 40M trainable) that jointly provides scalar process rewards and directional guidance. Critically, it amortizes perception costs by caching visual features once per step and reusing them across candidates.

**Key Results:**
- **CALVIN Benchmark (ABC→D):** GR-1 improves chain length from 3.19 to 3.33 and SR@5 from 41.5% to 48.7% (+17.4%); Dita achieves +18.4% improvement
- **Real Robot:** 88.6% average success vs. 72.9% baseline on manipulation tasks
- **Efficiency:** 7.23× speedup with 1000 candidates through shared perception cache

**Differentiation from Best-of-N with Value MLP:**
RoVer goes beyond simple best-of-N scoring by adding *directed exploration* in action space—the PRM predicts specific refinement directions for each candidate, enabling guided expansion rather than just ranking pre-sampled actions. The shared perception cache also provides significant efficiency gains over naive best-of-N approaches.

---

## Paper 2: Verifier-free Test-Time Sampling for Vision Language Action Models (arXiv:2510.05681)

**Core Method:**
The paper proposes **Masking Distribution Guided Selection (MG-Select)**, a verifier-free approach that requires no external models or additional training. The method: (1) generates N candidate actions via stochastic sampling from the VLA, (2) ranks them using KL divergence from a "condition-masking distribution" (computed by masking text/state inputs to represent maximum uncertainty), and (3) selects the highest-confidence action. Includes a joint training strategy using dropout on conditions to learn both conditional and unconditional distributions.

**Key Results:**
- **RoboCasa (30 demos):** 168% relative improvement on pick-and-place tasks
- **Real-World (Franka):** 28% improvement in-distribution, 35% out-of-distribution
- **SIMPLER-WidowX & LIBERO:** Consistent gains across benchmarks
- **Latency:** 45% reduction with optimized "single prefill" deployment

**Differentiation from Best-of-N with Value MLP:**
MG-Select **eliminates the need for a separately trained value function**. Instead, it leverages the VLA model's inherent uncertainty properties via masking. This is fundamentally verifier-free and requires minimal overhead, avoiding the additional parameter and training burden of a value MLP.

---

## Paper 3: World-Value-Action (WAV) Model (arXiv:2604.14732)

**Core Method:**
WAV enables implicit planning through three integrated components: (1) a Language-Conditioned Diffusion Transformer that predicts future visual trajectories, (2) a Trajectory Value Module that evaluates long-horizon utility of predicted states, and (3) an Action Decoding module that generates executable actions via cross-attention fusion of video and value features. Rather than planning directly in action space (which suffers from exponential decay of feasible trajectories), WAV performs iterative latent-space inference to progressively concentrate probability mass on trajectories that are both feasible and high-value.

**Key Results:**
- **LIBERO Simulation:** 99.6% average success, with 94.4% on long-horizon compositional tasks
- **Real-World (Dual-Arm):** 75.6% success vs. 35.6% baseline
- **Ablation:** Removing latent trajectory planning degrades performance by 1.7 points overall, confirming method effectiveness

**Differentiation from Best-of-N with Value MLP:**
WAV is structurally more sophisticated—it combines world modeling (trajectory prediction) with value estimation in a unified planning framework. Rather than selecting from pre-sampled actions, it *generates* actions by refining latent trajectories through iterative inference. This addresses the "curse of feasibility" for long-horizon planning, making it qualitatively different from best-of-N selection over action candidates.

---

**Note:** Both the abstract and HTML versions were successfully retrieved for all three papers, providing consistent information across formats.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca20648a-a5c8-4b0c-bd2d-d30b1db8161c",
  "isSidechain": false,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "type": "user",
  "uuid": "ae3c9779-b033-4b23-86d4-f38fcb81bc86",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Please fetch and summarize the following arXiv papers. For each, read the abstract, introduction, and method sections carefully. Report: (1) core method, (2) key results, (3) how it differentiates from \"Best-of-N over frozen WAM action latents with a trained value MLP.\"\n\n1. RoVer: Robot Reward Model as Test-Time Verifier - https://arxiv.org/abs/2510.10975\n2. Verifier-free Test-Time Sampling for Vision Language Action Models - https://arxiv.org/abs/2510.05681  \n3. World-Value-Action (WAV) model - https://arxiv.org/abs/2604.14732\n\nFor each paper, try both the abstract page (https://arxiv.org/abs/XXXX.XXXXX) and the HTML version (https://arxiv.org/html/XXXX.XXXXX). Report what you find.",
    "agentId": "a31456dc3f85db002",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! I've successfully fetched all three papers. Here's a comprehensive summary:\n\n---\n\n## Paper 1: RoVer: Robot Reward Model as Test-Time Verifier (arXiv:2510.10975)\n\n**Core Method:**\nRoVer uses a Process Reward Model (PRM) as a test-time verifier for Vision-Language-Action models. The framework operates in three stages: (1) generate multiple candidate actions from the base policy, (2) expand candidates along PRM-predicted 6D refinement directions in action space, and (3) score all candidates and select the optimal action. The PRM is a compact model (0.2B parameters, 40M trainable) that jointly provides scalar process rewards and directional guidance. Critically, it amortizes perception costs by caching visual features once per step and reusing them across candidates.\n\n**Key Results:**\n- **CALVIN Benchmark (ABC→D):** GR-1 improves chain length from 3.19 to 3.33 and SR@5 from 41.5% to 48.7% (+17.4%); Dita achieves +18.4% improvement\n- **Real Robot:** 88.6% average success vs. 72.9% baseline on manipulation tasks\n- **Efficiency:** 7.23× speedup with 1000 candidates through shared perception cache\n\n**Differentiation from Best-of-N with Value MLP:**\nRoVer goes beyond simple best-of-N scoring by adding *directed exploration* in action space—the PRM predicts specific refinement directions for each candidate, enabling guided expansion rather than just ranking pre-sampled actions. The shared perception cache also provides significant efficiency gains over naive best-of-N approaches.\n\n---\n\n## Paper 2: Verifier-free Test-Time Sampling for Vision Language Action Models (arXiv:2510.05681)\n\n**Core Method:**\nThe paper proposes **Masking Distribution Guided Selection (MG-Select)**, a verifier-free approach that requires no external models or additional training. The method: (1) generates N candidate actions via stochastic sampling from the VLA, (2) ranks them using KL divergence from a \"condition-masking distribution\" (computed by masking text/state inputs to represent maximum uncertainty), and (3) selects the highest-confidence action. Includes a joint training strategy using dropout on conditions to learn both conditional and unconditional distributions.\n\n**Key Results:**\n- **RoboCasa (30 demos):** 168% relative improvement on pick-and-place tasks\n- **Real-World (Franka):** 28% improvement in-distribution, 35% out-of-distribution\n- **SIMPLER-WidowX & LIBERO:** Consistent gains across benchmarks\n- **Latency:** 45% reduction with optimized \"single prefill\" deployment\n\n**Differentiation from Best-of-N with Value MLP:**\nMG-Select **eliminates the need for a separately trained value function**. Instead, it leverages the VLA model's inherent uncertainty properties via masking. This is fundamentally verifier-free and requires minimal overhead, avoiding the additional parameter and training burden of a value MLP.\n\n---\n\n## Paper 3: World-Value-Action (WAV) Model (arXiv:2604.14732)\n\n**Core Method:**\nWAV enables implicit planning through three integrated components: (1) a Language-Conditioned Diffusion Transformer that predicts future visual trajectories, (2) a Trajectory Value Module that evaluates long-horizon utility of predicted states, and (3) an Action Decoding module that generates executable actions via cross-attention fusion of video and value features. Rather than planning directly in action space (which suffers from exponential decay of feasible trajectories), WAV performs iterative latent-space inference to progressively concentrate probability mass on trajectories that are both feasible and high-value.\n\n**Key Results:**\n- **LIBERO Simulation:** 99.6% average success, with 94.4% on long-horizon compositional tasks\n- **Real-World (Dual-Arm):** 75.6% success vs. 35.6% baseline\n- **Ablation:** Removing latent trajectory planning degrades performance by 1.7 points overall, confirming method effectiveness\n\n**Differentiation from Best-of-N with Value MLP:**\nWAV is structurally more sophisticated—it combines world modeling (trajectory prediction) with value estimation in a unified planning framework. Rather than selecting from pre-sampled actions, it *generates* actions by refining latent trajectories through iterative inference. This addresses the \"curse of feasibility\" for long-horizon planning, making it qualitatively different from best-of-N selection over action candidates.\n\n---\n\n**Note:** Both the abstract and HTML versions were successfully retrieved for all three papers, providing consistent information across formats."
      }
    ],
    "totalDurationMs": 24407,
    "totalTokens": 21459,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3533,
      "cache_read_input_tokens": 16799,
      "output_tokens": 1120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3533
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1120,
          "cache_read_input_tokens": 16799,
          "cache_creation_input_tokens": 3533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3533,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "ca20648a-a5c8-4b0c-bd2d-d30b1db8161c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Frozen-WAM Best-of-N: Plug-in Inference-Time Candidate Selection for P…",
  "leafUuid": "ae3c9779-b033-4b23-86d4-f38fcb81bc86",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate frozen UWM baseline before CoRL submission",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c"
}
```

---

### Tool result

_source line 16 · 2026-05-10T08:26:30.065Z_

<details><summary>↩ Tool result · `toolu_014BbK3fDtesEndmkyXicvri`</summary>

```text
## Summary

### Task 1: "Compose Your Policies!" (arXiv 2510.01068)

**Core Method:**
General Policy Composition (GPC) is a training-free method that enhances performance by combining distributional scores of multiple pre-trained policies via a convex combination and test-time search. The theoretical foundation demonstrates that convex composition of distributional scores from multiple diffusion models yields a superior one-step functional objective compared to any individual score, with improvements propagating through generation trajectories.

**Key Results:**
- Consistently improves performance across diverse tasks (Robomimic, PushT, RoboTwin benchmarks, real-world evaluations)
- Composed policies can exceed the performance of either parent policy
- Enables seamless combination of heterogeneous policy types (diffusion, flow-based, VA, VLA)

**Key Difference from Hard Argmax Selection:**
GPC fundamentally differs from "Best-of-N hard argmax selection over frozen WAM action latents" by operating at the **distribution level** rather than selecting discrete actions. Instead of choosing a single best action from frozen latents, GPC performs **soft composition of probabilistic scores** across policies, then conducts test-time search. This allows blending complementary strengths of multiple models rather than binary selection.

---

### Task 2: Papers Using Video/World Model Denoising Loss for Robot Action Selection

Based on comprehensive web searches, I found the following relevant papers and research directions (2024-2026):

**Most Directly Relevant Papers:**

1. **Video Generation Models Are Good Latent Reward Models** - Pre-trained video generation models are naturally suited for reward modeling in latent space, with Process Reward Feedback Learning (PRFL) conducting preference optimization in latent space with efficient backpropagation through the denoising chain.

2. **Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning** - Proposes differentiable reward flow for fine-tuning video diffusion models using a frozen Vision-Language Model as a training-free critic, directly backpropagating feedback through the diffusion denoising chain.

3. **D3P: Dynamic Denoising Diffusion Policy** - Adaptively adjusts computational effort for each action based on task importance, optimizing the denoising process for embodied AI tasks.

4. **World Consistency Score (WCS)** - A unified evaluation metric for generative video models emphasizing internal world consistency with four interpretable sub-components (object permanence, relation stability, causal compliance, flicker penalty) that could be leveraged for action quality assessment.

5. **MoWM: Mixture-of-World-Models for Embodied Planning** - Explores best-of-N action selection using world model reconstruction to evaluate candidate action trajectories.

6. **V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning** - Self-supervised video model enabling zero-shot robotic planning with post-training on robot videos.

7. **World-in-World** - Framework where a proposal policy produces candidate action plans, with a world model predicting future states and a revision policy evaluating all rollouts to select the best.

8. **Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising** - Action-conditioned world modeling with asynchronous denoising for improved temporal consistency.

**Supporting Research Areas:**

- Diffusion Policy and its variants for robotic manipulation
- Action-conditioned video world models with test-time inference optimization
- Vision-Language-Action (VLA) models with evaluation capabilities
- RBench: A robotics benchmark evaluating video generation with metrics including structural consistency and physical plausibility

The research shows an active trend toward using generative models' own reconstruction/likelihood signals (rather than separate reward models) as quality signals for action selection in test-time planning scenarios.

Sources:
- [Video Generators are Robot Policies](https://videopolicy.cs.columbia.edu/assets/video_policy.pdf)
- [Video Generation Models Are Good Latent Reward Models](https://huggingface.co/papers/2511.21541)
- [Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning](https://arxiv.org/html/2601.04153v1)
- [D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning](https://arxiv.org/html/2508.06804v1)
- [World Consistency Score: A Unified Metric for Video Generation Quality](https://arxiv.org/abs/2508.00144)
- [MoWM: Mixture-of-World-Models for Embodied Planning](https://arxiv.org/html/2509.21797v2)
- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/html/2506.09985v1)
- [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/html/2604.26694v2)
- [Diffusion models for robotic manipulation: a survey](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full)
- [World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/html/2605.00080v1)
- [World Models Reading List: The Papers You Actually Need in 2025](https://medium.com/@graison/world-models-reading-list-the-papers-you-actually-need-in-2025-882f02d758a9)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "982df43d-aedf-4d1a-a73f-4622bd6ee99f",
  "isSidechain": false,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "type": "user",
  "uuid": "b4697767-9383-4978-a64a-6fc6964bcc80",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Please do two tasks:\n\n1. Fetch and summarize \"Compose Your Policies!\" (arXiv 2510.01068) - read abstract and method. Report: core method, key results, and how it differs from \"Best-of-N hard argmax selection over frozen WAM action latents.\"\n\n2. Search for papers that use video/world model denoising loss or video consistency as a quality signal for robot action selection at test time. Search queries to try:\n   - \"video denoising quality reward robot policy\"\n   - \"world model consistency score action selection\"  \n   - \"video diffusion denoising loss reward robot\"\n   - \"world model self-consistency action scoring\"\n\nFor the search, use WebSearch to find any papers (2024-2026) that use a video/world model's own denoising reconstruction loss as a quality signal to rank or select among candidate robot actions. This is different from training a separate reward model - it uses the model's own reconstruction error.\n\nReport all relevant papers found.",
    "agentId": "ab91555dad7a3a41c",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary\n\n### Task 1: \"Compose Your Policies!\" (arXiv 2510.01068)\n\n**Core Method:**\nGeneral Policy Composition (GPC) is a training-free method that enhances performance by combining distributional scores of multiple pre-trained policies via a convex combination and test-time search. The theoretical foundation demonstrates that convex composition of distributional scores from multiple diffusion models yields a superior one-step functional objective compared to any individual score, with improvements propagating through generation trajectories.\n\n**Key Results:**\n- Consistently improves performance across diverse tasks (Robomimic, PushT, RoboTwin benchmarks, real-world evaluations)\n- Composed policies can exceed the performance of either parent policy\n- Enables seamless combination of heterogeneous policy types (diffusion, flow-based, VA, VLA)\n\n**Key Difference from Hard Argmax Selection:**\nGPC fundamentally differs from \"Best-of-N hard argmax selection over frozen WAM action latents\" by operating at the **distribution level** rather than selecting discrete actions. Instead of choosing a single best action from frozen latents, GPC performs **soft composition of probabilistic scores** across policies, then conducts test-time search. This allows blending complementary strengths of multiple models rather than binary selection.\n\n---\n\n### Task 2: Papers Using Video/World Model Denoising Loss for Robot Action Selection\n\nBased on comprehensive web searches, I found the following relevant papers and research directions (2024-2026):\n\n**Most Directly Relevant Papers:**\n\n1. **Video Generation Models Are Good Latent Reward Models** - Pre-trained video generation models are naturally suited for reward modeling in latent space, with Process Reward Feedback Learning (PRFL) conducting preference optimization in latent space with efficient backpropagation through the denoising chain.\n\n2. **Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning** - Proposes differentiable reward flow for fine-tuning video diffusion models using a frozen Vision-Language Model as a training-free critic, directly backpropagating feedback through the diffusion denoising chain.\n\n3. **D3P: Dynamic Denoising Diffusion Policy** - Adaptively adjusts computational effort for each action based on task importance, optimizing the denoising process for embodied AI tasks.\n\n4. **World Consistency Score (WCS)** - A unified evaluation metric for generative video models emphasizing internal world consistency with four interpretable sub-components (object permanence, relation stability, causal compliance, flicker penalty) that could be leveraged for action quality assessment.\n\n5. **MoWM: Mixture-of-World-Models for Embodied Planning** - Explores best-of-N action selection using world model reconstruction to evaluate candidate action trajectories.\n\n6. **V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning** - Self-supervised video model enabling zero-shot robotic planning with post-training on robot videos.\n\n7. **World-in-World** - Framework where a proposal policy produces candidate action plans, with a world model predicting future states and a revision policy evaluating all rollouts to select the best.\n\n8. **Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising** - Action-conditioned world modeling with asynchronous denoising for improved temporal consistency.\n\n**Supporting Research Areas:**\n\n- Diffusion Policy and its variants for robotic manipulation\n- Action-conditioned video world models with test-time inference optimization\n- Vision-Language-Action (VLA) models with evaluation capabilities\n- RBench: A robotics benchmark evaluating video generation with metrics including structural consistency and physical plausibility\n\nThe research shows an active trend toward using generative models' own reconstruction/likelihood signals (rather than separate reward models) as quality signals for action selection in test-time planning scenarios.\n\nSources:\n- [Video Generators are Robot Policies](https://videopolicy.cs.columbia.edu/assets/video_policy.pdf)\n- [Video Generation Models Are Good Latent Reward Models](https://huggingface.co/papers/2511.21541)\n- [Diffusion-DRF: Differentiable Reward Flow for Video Diffusion Fine-Tuning](https://arxiv.org/html/2601.04153v1)\n- [D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning](https://arxiv.org/html/2508.06804v1)\n- [World Consistency Score: A Unified Metric for Video Generation Quality](https://arxiv.org/abs/2508.00144)\n- [MoWM: Mixture-of-World-Models for Embodied Planning](https://arxiv.org/html/2509.21797v2)\n- [V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning](https://arxiv.org/html/2506.09985v1)\n- [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/html/2604.26694v2)\n- [Diffusion models for robotic manipulation: a survey](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full)\n- [World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/html/2605.00080v1)\n- [World Models Reading List: The Papers You Actually Need in 2025](https://medium.com/@graison/world-models-reading-list-the-papers-you-actually-need-in-2025-882f02d758a9)"
      }
    ],
    "totalDurationMs": 48265,
    "totalTokens": 29623,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 981,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 25171,
      "output_tokens": 1345,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 981,
          "output_tokens": 1345,
          "cache_read_input_tokens": 25171,
          "cache_creation_input_tokens": 2126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2126,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "982df43d-aedf-4d1a-a73f-4622bd6ee99f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T08:26:58.779Z_

<details><summary>↩ Tool result · `toolu_017tCyySRRTkZkpPfii26jHa`</summary>

```text
Now let me compile my findings into a comprehensive report.

## Report: UWM RoboCasa Results, WAM Baselines, and Test-Time Compute Landscape

### 1. UWM (Unified World Models) on RoboCasa - Key Finding

Unfortunately, **the UWM paper (arXiv 2504.02792) does not report results on the RoboCasa benchmark**. The paper focuses on:
- DROID dataset (real robot tasks: Stack-Bowls, Block-Cabinet, etc.)
- LIBERO benchmark (100 robotic manipulation tasks)
- Categorized OOD evaluations on real robots with environmental variations

The paper demonstrates that UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable policies than imitation learning. However, no zero-shot or frozen baseline success rates on RoboCasa are reported in the available content.

### 2. Frozen/WAM Baseline on RoboCasa - What Can Be Inferred

Based on my search, here's what can be inferred about WAM baselines:

**X-WAM Performance:**
- Achieves 79.2% average success rate on RoboCasa
- Achieves 90.7% average success rate on RoboTwin 2.0
- Represents a leading published WAM baseline

**Other Published Baselines on RoboCasa:**
- Cosmos-Policy-RoboCasa-Predict2-2B: 67.1% average success rate (24 kitchen manipulation tasks)
- HAMLET (DiT4DiT with GR00T N1.5 finetuning): 66.4% average success rate vs. 64.1% baseline
- DiT4DiT (unfinetuned): 50.8% average success rate

**OA-WAM (Object-Addressable World Action Model):**
- Features frozen identity addresses per episode with architectural constraints to prevent failure modes
- Represents a specific frozen baseline design pattern in world action models

RoboCasa consists of 24 static kitchen manipulation tasks with a single Franka Emika Panda robot arm, making it a rigorous benchmark for evaluating both frozen and fine-tuned policies.

### 3. Current Landscape of Test-Time Compute Papers for Robot Policies (2025-2026)

The field has rapidly evolved with several major directions:

**A. Dynamic Difficulty-Aware Compute Scaling**
- **DA-SIP (Difficulty-Aware Stochastic Interpolant Policy)** (2511.20906, NeurIPS 2025)
  - Adaptively adjusts integration horizon based on task difficulty in real-time
  - Achieves 2.6-4.4x reduction in computation time while maintaining success rates
  - Employs a difficulty classifier analyzing RGB-D observations
  - Presented at NeurIPS 2025

**B. Test-Time Verification with Process Reward Models**
- **RoVer** (2510.10975)
  - Robot Process Reward Model (PRM) as test-time verifier for VLA models
  - Generates scalar process rewards + action-space refinement directions
  - Leverages shared perception caches for efficient inference
  - Enables test-time scaling without modifying base model weights or architecture
  - Plug-and-play framework applicable to GR-1, Dita, MoDE, and Diffusion Policy base models
  - Evaluated on CALVIN benchmark and real Dobot dual-arm platform

**C. Policy Composition at Test Time**
- **GPC (General Policy Composition)** (2510.01068)
  - Training-free method combining multiple pre-trained policies via convex combination and test-time search
  - Works with heterogeneous policies (VA, VLA, diffusion, flow-matching)
  - Theoretical foundation showing composition yields superior one-step functional objective
  - Demonstrated improvements on Robomimic, PushT, RoboTwin, and real robot tasks

**D. Inference-Time Scaling for Reward Models**
- **DeepSeek-GRM / SPCT Approach** (2504.02495)
  - Parallel sampling with meta reward model for voting
  - Scaling from 1 to 32 samples: 69.9 → 72.8 performance gain
  - Demonstrates inference-time scaling can exceed training-time scaling

**E. Best-of-N and Efficient Sampling**
- **Self-Truncation Best-of-N (ST-BoN)**
  - Avoids fully generating all N samples
  - Reduces GPU memory by 80% and inference latency by 50%
  - Achieves Full-BoN performance with 70-80% computational savings
  - Related work on calibrated best-of-N sampling (CarBoN)

**F. Real-Time Policy Steering**
- **Inference-Time Policy Steering (ITPS)**
  - Human interactions guiding policy behavior at inference time
  - Represents interactive test-time adaptation

### Summary

The test-time compute landscape for robot policies in 2025-2026 is characterized by:
1. **Adaptive computation** based on task difficulty (DA-SIP)
2. **Process reward model verification** enabling action refinement without retraining (RoVer)
3. **Training-free policy composition** for improved out-of-distribution performance (GPC)
4. **Efficient sampling strategies** that maintain performance with reduced compute (ST-BoN, CarBoN)
5. **Scaling laws research** connecting inference-time compute to policy performance gains

These approaches collectively show that substantial performance improvements can be achieved post-training through intelligent test-time compute allocation, without requiring model retraining or architecture modifications.

### Sources

- [Unified World Models paper (2504.02792)](https://arxiv.org/abs/2504.02792)
- [RoVer: Robot Reward Model as Test-Time Verifier](https://arxiv.org/abs/2510.10975)
- [Dynamic Test-Time Compute Scaling (DA-SIP)](https://arxiv.org/abs/2511.20906)
- [Compose Your Policies (GPC)](https://arxiv.org/abs/2510.01068)
- [Inference-Time Scaling for Generalist Reward Modeling](https://arxiv.org/abs/2504.02495)
- [Self-Truncation Best-of-N Sampling](https://arxiv.org/abs/2503.01422)
- [OA-WAM: Object-Addressable World Action Model](https://arxiv.org/abs/2605.06481)
- [RoboCasa: Large-Scale Simulation Framework](https://arxiv.org/abs/2406.02523)
- [X-WAM Unified 4D World Action Modeling](https://sharinka0715.github.io/X-WAM/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3213910b-864d-48a0-99fa-c1c1a4609240",
  "isSidechain": false,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "type": "user",
  "uuid": "403d5e83-37f3-489d-8b78-cc8842ff7dc8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Please search for the following information:\n\n1. Any published results of UWM (Unified World Model, arXiv 2504.02792, RSS 2025) on RoboCasa benchmark - specifically success rates WITHOUT fine-tuning. Search:\n   - \"UWM RoboCasa\"\n   - \"unified world model RoboCasa zero-shot\"\n   - arXiv 2504.02792 citations mentioning RoboCasa\n\n2. Current state of Best-of-N / test-time compute scaling for robot policies - search for papers from 2025-2026:\n   - \"best of N robot policy test time\"\n   - \"test time compute scaling robot manipulation\"\n   - \"inference time scaling robot policy\"\n   - \"process reward model robot VLA\"\n\n3. Also fetch this paper and report its method: https://arxiv.org/abs/2510.10975 (RoVer)\n\nReport: what frozen WAM baseline on RoboCasa can be inferred, and what's the current landscape of test-time compute papers for robot policies.",
    "agentId": "afb8565e5ac2f3dd1",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Now let me compile my findings into a comprehensive report.\n\n## Report: UWM RoboCasa Results, WAM Baselines, and Test-Time Compute Landscape\n\n### 1. UWM (Unified World Models) on RoboCasa - Key Finding\n\nUnfortunately, **the UWM paper (arXiv 2504.02792) does not report results on the RoboCasa benchmark**. The paper focuses on:\n- DROID dataset (real robot tasks: Stack-Bowls, Block-Cabinet, etc.)\n- LIBERO benchmark (100 robotic manipulation tasks)\n- Categorized OOD evaluations on real robots with environmental variations\n\nThe paper demonstrates that UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable policies than imitation learning. However, no zero-shot or frozen baseline success rates on RoboCasa are reported in the available content.\n\n### 2. Frozen/WAM Baseline on RoboCasa - What Can Be Inferred\n\nBased on my search, here's what can be inferred about WAM baselines:\n\n**X-WAM Performance:**\n- Achieves 79.2% average success rate on RoboCasa\n- Achieves 90.7% average success rate on RoboTwin 2.0\n- Represents a leading published WAM baseline\n\n**Other Published Baselines on RoboCasa:**\n- Cosmos-Policy-RoboCasa-Predict2-2B: 67.1% average success rate (24 kitchen manipulation tasks)\n- HAMLET (DiT4DiT with GR00T N1.5 finetuning): 66.4% average success rate vs. 64.1% baseline\n- DiT4DiT (unfinetuned): 50.8% average success rate\n\n**OA-WAM (Object-Addressable World Action Model):**\n- Features frozen identity addresses per episode with architectural constraints to prevent failure modes\n- Represents a specific frozen baseline design pattern in world action models\n\nRoboCasa consists of 24 static kitchen manipulation tasks with a single Franka Emika Panda robot arm, making it a rigorous benchmark for evaluating both frozen and fine-tuned policies.\n\n### 3. Current Landscape of Test-Time Compute Papers for Robot Policies (2025-2026)\n\nThe field has rapidly evolved with several major directions:\n\n**A. Dynamic Difficulty-Aware Compute Scaling**\n- **DA-SIP (Difficulty-Aware Stochastic Interpolant Policy)** (2511.20906, NeurIPS 2025)\n  - Adaptively adjusts integration horizon based on task difficulty in real-time\n  - Achieves 2.6-4.4x reduction in computation time while maintaining success rates\n  - Employs a difficulty classifier analyzing RGB-D observations\n  - Presented at NeurIPS 2025\n\n**B. Test-Time Verification with Process Reward Models**\n- **RoVer** (2510.10975)\n  - Robot Process Reward Model (PRM) as test-time verifier for VLA models\n  - Generates scalar process rewards + action-space refinement directions\n  - Leverages shared perception caches for efficient inference\n  - Enables test-time scaling without modifying base model weights or architecture\n  - Plug-and-play framework applicable to GR-1, Dita, MoDE, and Diffusion Policy base models\n  - Evaluated on CALVIN benchmark and real Dobot dual-arm platform\n\n**C. Policy Composition at Test Time**\n- **GPC (General Policy Composition)** (2510.01068)\n  - Training-free method combining multiple pre-trained policies via convex combination and test-time search\n  - Works with heterogeneous policies (VA, VLA, diffusion, flow-matching)\n  - Theoretical foundation showing composition yields superior one-step functional objective\n  - Demonstrated improvements on Robomimic, PushT, RoboTwin, and real robot tasks\n\n**D. Inference-Time Scaling for Reward Models**\n- **DeepSeek-GRM / SPCT Approach** (2504.02495)\n  - Parallel sampling with meta reward model for voting\n  - Scaling from 1 to 32 samples: 69.9 → 72.8 performance gain\n  - Demonstrates inference-time scaling can exceed training-time scaling\n\n**E. Best-of-N and Efficient Sampling**\n- **Self-Truncation Best-of-N (ST-BoN)**\n  - Avoids fully generating all N samples\n  - Reduces GPU memory by 80% and inference latency by 50%\n  - Achieves Full-BoN performance with 70-80% computational savings\n  - Related work on calibrated best-of-N sampling (CarBoN)\n\n**F. Real-Time Policy Steering**\n- **Inference-Time Policy Steering (ITPS)**\n  - Human interactions guiding policy behavior at inference time\n  - Represents interactive test-time adaptation\n\n### Summary\n\nThe test-time compute landscape for robot policies in 2025-2026 is characterized by:\n1. **Adaptive computation** based on task difficulty (DA-SIP)\n2. **Process reward model verification** enabling action refinement without retraining (RoVer)\n3. **Training-free policy composition** for improved out-of-distribution performance (GPC)\n4. **Efficient sampling strategies** that maintain performance with reduced compute (ST-BoN, CarBoN)\n5. **Scaling laws research** connecting inference-time compute to policy performance gains\n\nThese approaches collectively show that substantial performance improvements can be achieved post-training through intelligent test-time compute allocation, without requiring model retraining or architecture modifications.\n\n### Sources\n\n- [Unified World Models paper (2504.02792)](https://arxiv.org/abs/2504.02792)\n- [RoVer: Robot Reward Model as Test-Time Verifier](https://arxiv.org/abs/2510.10975)\n- [Dynamic Test-Time Compute Scaling (DA-SIP)](https://arxiv.org/abs/2511.20906)\n- [Compose Your Policies (GPC)](https://arxiv.org/abs/2510.01068)\n- [Inference-Time Scaling for Generalist Reward Modeling](https://arxiv.org/abs/2504.02495)\n- [Self-Truncation Best-of-N Sampling](https://arxiv.org/abs/2503.01422)\n- [OA-WAM: Object-Addressable World Action Model](https://arxiv.org/abs/2605.06481)\n- [RoboCasa: Large-Scale Simulation Framework](https://arxiv.org/abs/2406.02523)\n- [X-WAM Unified 4D World Action Modeling](https://sharinka0715.github.io/X-WAM/)"
      }
    ],
    "totalDurationMs": 72050,
    "totalTokens": 33448,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2313,
      "cache_read_input_tokens": 29488,
      "output_tokens": 1640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2313
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1640,
          "cache_read_input_tokens": 29488,
          "cache_creation_input_tokens": 2313,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2313,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "3213910b-864d-48a0-99fa-c1c1a4609240",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T08:31:41.076Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have rich context. Let me synthesize what I've learned:

## Key findings:

### 1. RoVer (arXiv 2510.10975)
- Generates B candidate actions from frozen VLA
- Trains a 0.2B PRM that scores candidates AND predicts refinement directions
- Not just Best-of-N ranking - it's directed exploration in action space
- Evaluated on CALVIN + real robots
- Key difference: PRM guides exploration direction, not just argmax selection

### 2. Verifier-free Test-Time Sampling (arXiv 2510.05681)


Uses KL divergence from an unconditional masked distribution as a confidence signal without needing any trained value model, achieving 168% improvement on RoboCasa pick-and-place tasks—notably, this is one of the few approaches actually evaluated directly on RoboCasa rather than just simulation environments.

### 3. WAV (arXiv 2604.14732)
- Unified planning framework combining world modeling + value estimation + action decoding
- Performs iterative latent-space inference to concentrate probability on high-value trajectories
- Different from discrete Best-of-N selection
- 99.6% on LIBERO, 75.6% real-world

### 4. Compose Your Policies! (arXiv 2510.01068)
Training-free approach that composes multiple policy distributions, distinct from simple Best-of-N argmax selection.

### 5. UWM on RoboCasa
Looking at the actual RoboCasa results: UWM itself wasn't evaluated there—only on LIBERO and DROID—but X-WAM hits 79.2%, DiT4DiT unfinetuned gets 50.8%, and Cosmos Policy fine-tuned reaches 67.1%. This is troubling because the reviewer predicted frozen UWM might only achieve 15-30% on RoboCasa, yet the Verifier-free baseline already demonstrated 168% improvement on the same task using a VLA. This raises serious questions about our novelty claim.

## Critical Assessment

The core issue is that RoVer follows essentially the same pipeline we're proposing—frozen policy generating candidates, then scoring and selecting—just substituting a VLA for WAM. Our differentiation hinges on WAM's action latents containing video-grounded physics information that should make a simple MLP sufficient where VLAs need a separate value model, but I'm asserting this rather than proving it. The Verifier-free paper is even more problematic since it already achieved substantial gains on RoboCasa without any trained value model at all, which directly undermines our core proposal. And without published frozen UWM results on RoboCasa to establish a baseline, it's hard to know what we're actually improving over.

The test-time selection space is saturated with recent work—DA-SIP, RoVer, GPC, MG-Select, ST-BoN—and MoWM's approach of using world model reconstruction as a quality signal is conceptually closer to what I was exploring with video denoising. So the real question is whether the application of Best-of-N selection with a trained value MLP on WAM is genuinely novel when it's already been done for VLAs, and done training-free for VLAs on the exact benchmark we're targeting.

The actual differentiation comes down to whether WAMs have a unique capability that VLAs don't: they can generate videos conditioned on actions, which means we can use the WAM's own predictive ability as a self-scorer without any additional training—essentially leveraging the video generation as a quality signal rather than training a separate value function. of training a value MLP, use the WAM's own video denoising score as a quality signal for action selection.

Method:
1. Sample B=4-8 action trajectories in action-only mode (fast, no video)
2. For each candidate action trajectory a_i, compute the WAM's video denoising loss conditioned on a_i (partial denoising, e.g., 10 steps at intermediate noise levels)
3. Higher video denoising score (lower loss) = the action is consistent with physically plausible futures the WAM has learned
4. Select argmax

This is:
- **Training-free** (stronger than verifier-free VLA work - no need to compute KL from masked distribution either)
- **WAM-specific** (VLAs cannot do this - they have no video generation capability)
- **Theoretically principled** (the WAM's video coherence reflects learned physics from large-scale video pretraining)
- **Novel** (different from RoVer's PRM, different from MG-Select's KL divergence, different from training a value MLP)

I'm checking if MoWM or other video generation papers already do this. MoWM uses multiple world models for ensemble planning, but that seems like a different approach. And the video generation as rewards paper is about RL fine-tuning, not test-time selection. The real distinction here is leveraging the WAM's self-consistency at test time without any additional training—just using its joint video-action pretraining to evaluate which actions lead to coherent futures.

But I'm realizing a potential issue: if video generation at test time only adds marginal gains, then the denoising score might not discriminate well between action candidates either. The concern is that video models can generate plausible continuations even for failed actions, so the denoising score would measure physical plausibility rather than task success. That's a real limitation I need to address, maybe by reformulating how I use the denoising signal.

Actually, I'm overcomplicating this. The stagnation after three rounds suggests I'm approaching the problem wrong—the research community has already solved best-of-N selection for frozen policies with papers like RoVer and MG-Select. What I should focus on instead is whether WAMs offer something fundamentally different, which brings me to a cleaner framing around self-verification through video futures.

The key insight is that WAMs can generate videos conditioned on candidate actions, creating a unique capability for quality assessment that VLAs simply don't have. By checking how consistent the generated video is with each action, WAMs can verify candidates without any additional training—something impossible for vision-language models that can't generate video. This gives WAMs a categorical advantage over existing approaches, each of which relies on different mechanisms like training separate reward models, using KL divergence from masked distributions, or composition-based methods.

But the real question is whether video consistency actually predicts task success. If it does, we have a clean story about WAM self-verification. If not, we're looking at an interesting negative result about the limits of video-action coherence. For a strong conference paper though, we need positive results, so I need to think more carefully about what actually works in practice.

A hybrid approach might be the answer: use the video denoising score as one signal alongside action diversity from noise seeding, keeping the computational cost low with just 10-15 denoising steps per candidate. This avoids any additional training while adding WAM self-verification. The remaining concern is whether partial video denoising actually has enough discriminative power to distinguish good actions from bad ones.

Rather than pivoting entirely, maybe the real insight is sharpening the framing around what we already have. The latent quality argument is compelling—WAM action latents from joint video-action pretraining should be richer than raw action tokens because they're regularized by video coherence during training. If a simple MLP over these latents outperforms one over direct action outputs, that's evidence the latent space is already doing useful work. Combined with the training efficiency argument—we only need a tiny MLP at minimal compute compared to other verifiers—and the fact that we're specifically exploiting WAM-specific properties, we have a coherent story even if the video denoising component doesn't pan out perfectly.

But I'm realizing the reviewer's core concern cuts deeper: these are engineering differences, not conceptual novelty. The latent quality claim is asserted but not really demonstrated, and the hard argmax thing doesn't actually address the fundamental question of whether this approach is conceptually different from what RoVer or other verifiers are already doing. For a venue like CoRL, we need to articulate what's genuinely novel about the idea, not just why our engineering choices are reasonable.

So maybe the real move is to pivot toward something with actual conceptual novelty. Instead of just using WAM latents as a better action space, what if we leverage the WAM's own predictive model as a built-in quality signal? The WAM already learns to predict plausible video-action pairs, so we could use that predictive confidence directly as a scoring mechanism without training anything new.

The approach would be: sample a batch of action trajectories, then for each one, ask the WAM's video decoder how confident it is that this action leads to a plausible visual future by measuring its denoising performance at intermediate noise levels. Pick the action with the highest denoising score. This is genuinely novel because it's zero-shot, exploits the WAM's unique joint modeling capability that VLAs don't have, and uses the model's own knowledge to verify its outputs.

The intuition is that failed trajectories typically involve awkward arm poses, collisions, or irrelevant motions that violate the WAM's learned physics priors from millions of robot videos. Actions that produce visually plausible futures according to the model are more likely to actually succeed. This differs from prior work like RoVer (which needs a trained PRM), MG-Select (which uses KL divergence), value MLPs (which require failure data), and GPC (which composes distributions rather than selecting actions). The conceptual novelty alone—using video modeling as an implicit success predictor without any additional training—could make this a strong conference contribution.

The main appeal is that it requires zero training overhead while directly leveraging the WAM's unique video understanding capability in a way that VLAs can't match. But there's a real risk: I don't actually know if denoising error will correlate with task success, and intermediate noise levels might produce unreliable signals. The approach also adds computational cost compared to pure action inference. My plan is to use the diversity pilot as a diagnostic—if the video consistency score doesn't show meaningful correlation with success, I'll fall back to the value MLP as a backup result.

Now I'm reconsidering whether video denoising score is actually a reliable quality signal for this task.

The core problem is that the WAM predicts both video and action jointly, so a failed action might still generate a plausible-looking video—the model could predict a video where the robot attempts to grasp but fails, which is still a valid reconstruction. The denoising error measures how well the model reconstructs the video, not whether the action succeeds. The WAM would need to learn to predict failure videos differently from success videos for this to work as a quality metric.

But there's a potential way forward: if I condition on task success and the training data is biased toward successful demonstrations—which LIBERO-90 is—then successful actions should have lower denoising error than failed ones, since the model learned primarily from successful trajectories.

So the revised framing is that the WAM's video component implicitly encodes "what successful manipulation looks like" because it was trained mostly on successes. Actions that produce videos consistent with this learned prior of successful outcomes should have lower denoising error and be more likely to succeed. This gives me a defensible way to use video denoising for zero-shot candidate selection, though I still need to verify whether partial video denoising is actually discriminative enough in practice.

The method would be straightforward: sample a batch of candidate actions without video, then score each one by computing the denoising error at a mid-range noise level—just one forward pass per candidate. I'd select the action with the lowest error, and include a trained value MLP as an ablation to compare against the training-free approach.

But I'm realizing I've been overcomplicating this. Let me refocus on what's actually novel and feasible here.

The original approach has real problems—it's too similar to RoVer, the latent separability isn't validated, and some of the baselines aren't even set up. The VCSS pivot has its own issues: there's no guarantee that video denoising error correlates with task success, it adds computational overhead at test time which defeats the purpose of a fast method, and world model reconstruction for action evaluation is already being explored elsewhere.

What I should be focusing on is what actually makes WAMs different from VLAs for action selection at test time. The real advantage is that WAMs learn a joint latent space where video and action are represented together, not separately. The action latent is constrained by video coherence, which means it naturally lives in a space where actions that produce coherent videos are preferred.

So the actual question is whether I can leverage this joint latent structure for better candidate selection in a way that's provably better than action-only methods. The value MLP would be learning a quality function in a latent space that already has video-physics structure built in, making it potentially more sample-efficient and accurate than VLA approaches. But I need to actually demonstrate this with a controlled experiment comparing the WAM action latent plus MLP against direct action outputs plus the same MLP to isolate the WAM-specific advantage. value function → Best-of-N
3. VLA action tokens + 3-layer MLP → value function → Best-of-N (using a matched VLA baseline)
4. MG-Select (training-free KL approach applied to WAM)

If (1) outperforms (2) and (3), it directly demonstrates that WAM latent structure provides meaningful signal that raw action space doesn't.

This is actually a strong controlled experiment. The paper's contribution becomes:
- **"The joint video-action pretraining in WAMs produces action latents that are significantly more discriminative for quality estimation than action-space representations, enabling sample-efficient value learning for Best-of-N selection."**

This is a conceptually richer claim than "we do Best-of-N with WAMs."

**Revised framing:**

Title: "Action Latent Quality Grounding in World Action Models: Why WAM Latents Enable Efficient Best-of-N Robot Manipulation"

The core insight is that joint video-action pretraining creates action latents that are far more discriminative for success prediction than direct action representations or VLA tokens, allowing a minimal value function to match approaches requiring orders of magnitude more training. To validate this, I need a matched VLA baseline, ablations showing the latent hierarchy outperforms alternatives, and failure demonstrations in the dataset.

The engineering challenge is getting a fair VLA comparison on LIBERO/RoboCasa. But if I can solve that, the paper has a clear scientific story.

Actually, looking at the reviewer feedback more carefully—they're already suggesting we drop DreamZero and focus on frozen UWM with RoboCasa Best-of-N as the primary result. That's not a rejection, it's a roadmap. The novelty concern is moderate, not critical, which means stronger framing around the WAM latent structure could address it. So the path forward is: add the three missing papers with clear differentiation, validate the frozen UWM baseline on RoboCasa, and tighten the theoretical motivation for why the latent structure matters. That's achievable on the CoRL timeline.

But there's an interesting angle here—instead of just the value MLP, we could propose a dual-method comparison: the trained value MLP versus a zero-training video-consistency scoring approach. This directly addresses the novelty concern against RoVer by showing when training helps versus when it doesn't, which becomes its own contribution and differentiates us from pure VLA approaches.

The risk is added complexity with only 20 days until the CoRL deadline, but the payoff is stronger: we get natural ablations, a richer theoretical narrative about why WAM-specific methods work, and empirical evidence for when each approach succeeds.

So I'm committing to a major revision: tightening the related work with clear differentiation, resetting RoboCasa targets to realistic "≥10pp improvement over baseline" numbers, centering the WAM latent quality argument theoretically, and introducing the dual-method framework with both the value MLP and the training-free video-consistency scoring as complementary approaches.

The core insight is that video-consistency self-scoring (VCSS) leverages the WAM's own denoising capability—by measuring prediction error at intermediate noise levels for each candidate action, we get a quality signal without any training, something impossible with VLAs. Comparing VCSS against the lightweight value MLP and against VLA-style methods applied to WAM gives us the paper's real contribution: demonstrating that WAM-specific test-time selection genuinely outperforms generic approaches.

Now I need to actually revise the paper structure with these two methods as the core contributions, update the title to reflect the dual approach, sharpen the problem statement around WAM-specific selection, and add the missing related work papers with clear differentiation.

For resources, removing DreamZero saves significant evaluation time, and while VCSS adds a small pilot phase to validate the video denoising correlation, the overall budget stays around 40-60 H100-hours. The tradeoff is that I lose the cross-WAM generalization claim, but the zero-training VCSS method becomes the main novelty instead.

Now I'm drafting the paper title and need to capture what makes this work distinct. The core contribution is using video-action joint pretraining to enable training-free candidate selection at inference time, so I'm testing different framings to emphasize that angle. can self-verify candidates using their own video prediction capability (novel, zero-training)
2. WAM action latents are richer substrates for value learning than VLA action tokens (argument + ablation)
3. Comparison of zero-training VCSS vs. trained value MLP on manipulation benchmarks

The key insight is that WAMs have this unique advantage from their video-action joint pretraining, which opens up both a training-free path through video consistency scoring and an efficient trained path through value learning on the action latents. I want to emphasize this duality in the title and framing. So I'm settling on "WAM Self-Verification: Training-Free Best-of-N Selection for Frozen World Action Models via Video-Action Consistency Scoring" to highlight the core contribution.

Now I need to revise the problem and opportunity sections to reflect this dual-method approach. The core problem is still that frozen WAMs lack a low-cost way to add candidate selection, but I should sharpen the differentiation from VLA work. The opportunity is that WAMs' video-action joint pretraining creates physically grounded action latents that enable both training-free selection via video consistency and efficient trained selection, which is something VLAs can't leverage in the same way.

For the landscape, I'm adding RoVer, MG-Select, Compose Your Policies!, and WAV with proper differentiation. I also need to update the baselines—DiT4DiT unfinetuned on RoboCasa sits at 50.8%, which suggests frozen WAM baselines might be in the 40-55% range, though UWM specifically on RoboCasa is still unknown.

The approach section needs to split into two methods: VCSS as the training-free path and value MLP as the lightweight trained path. I'm dropping DreamZero definitively and adding a binary classification accuracy diagnostic for value MLP. I also want to add a VCSS pilot that measures the correlation between video denoising score and success.

For the RoboCasa target, I'm shifting from "approaching Cosmos Policy 67.1%" to "≥10pp improvement over frozen baseline."

Now I'm reconsidering whether VCSS is solid enough to include. The mechanism would condition the WAM's video decoder on an observation and candidate action trajectory, then compute the video denoising error at a single intermediate noise level—just one forward pass, not full denoising. Lower error would indicate the action is more consistent with the WAM's learned video prior and thus more likely to succeed. This could work because the WAM was trained on success demonstrations, so its video prior should be biased toward what success looks like, and failed actions often involve problematic configurations that the prior would struggle to reconstruct.

But there are real risks: the denoising error might just measure whether a frame looks plausible rather than whether the action actually succeeds, the model could predict plausible failure videos too, and high noise levels might obscure action-specific information. I'm planning to test this in a diagnostic before the main experiments, and if the correlation is weak (ρ < 0.2), I'll report it as a negative result and stick with the value MLP. The cost is manageable—a few H100-hours for the diagnostic plus negligible inference overhead. This actually feels like a reasonable addition: it's WAM-specific, requires no training, and is conceptually interesting. If it works, it's a strong contribution; if not, it still shows something meaningful about where WAM's capabilities and limitations lie.

Now I'm thinking through the reviewer feedback more carefully. They want three concrete fixes: missing citations with clear differentiation, validation of the frozen UWM RoboCasa baseline, and sharper theoretical motivation for the WAM latents. This is a major revision because it introduces VCSS as a new primary method, recalibrates the performance targets, reframes the whole approach from "plug-in BoN" to "WAM self-verification," and removes DreamZero from the scope. I need to finalize the JSON structure and write a clear description of the revised idea, focusing on the core change: comparing two methods—VCSS with zero training and Value MLP as a lightweight alternative.

The key insight is that WAM's unique joint video-action pretraining becomes the theoretical foundation, and I need to add the missing papers (RoVer, MG-Select/Verifier-free, Compose Your Policies!, WAV) while recalibrating the RoboCasa target to ≥10pp improvement instead of ≥60% absolute, and narrowing the CoRL submission to UWM only. Now I'm writing the JSON structure with a comprehensive and specific approach that clearly explains the VCSS method.

Finalizing the title and core structure...

For the scoring mechanism, I'm settling on "Predictive Consistency Score" (PCS) as the term—it captures how the WAM evaluates whether each sampled action candidate leads to a plausible visual future by running a single video decoder forward pass at an intermediate noise level and using reconstruction error as the quality proxy. This represents the WAM's own assessment of action viability without requiring a separate verifier model.

Writing the full JSON revision... I'm cycling through title options to capture both the video consistency and value learning contributions. The challenge is balancing specificity with brevity—I want to emphasize that we're doing inference-time selection on frozen WAMs without additional training, but the titles keep getting unwieldy. I'm leaning toward something that highlights the core insight: that WAM latents can self-verify through predictive consistency, which is cleaner than listing every technical component.

Now I need to reframe the core problem statement to emphasize three things: the gap that frozen WAMs lack a selection mechanism, the opportunity that their video-action pretraining should make them quality-aware, and the open scientific question of whether and when their latents actually know quality. This positions the work as both a research question and a practical contribution.

For the CoRL structure, I'm realizing the comparison between VCSS and Value MLP isn't a weakness—it's actually the paper's strength. VCSS is simple and requires no training, while Value MLP needs failure data and fine-tuning, so showing when each approach works best gives clear guidance. The minimum viable submission would include the diversity pilot, a diagnostic validating that VCSS correlates with quality, results on both RoboCasa and LIBERO-Long for both methods, ablations on the number of candidates and selection strategy, and a discussion tying everything back to the core question. I can implement VCSS in the first couple days by adding a video decoder forward pass at a fixed noise level, then spend the next few days running diagnostics on RoboCasa to confirm the correlation holds.

The rest of the timeline is tight—validating the frozen baseline takes a few days, then failure collection if that checks out, followed by the main ablations comparing both approaches across different hyperparameters, evaluation on LIBERO-Long, and finally writing and review. It's doable if I keep VCSS as the primary contribution and treat Value MLP as the secondary comparison. Before I commit to the JSON though, I should verify whether the video-consistency scoring concept overlaps with what MoWM does, since Agent 2 mentioned that paper explores mixture-of-world-models for planning.

MoWM's approach to using world model reconstruction for evaluating action trajectories sounds potentially similar to VCSS, which is concerning for novelty. The key difference might be that MoWM uses an ensemble of world models while VCSS relies on a single WAM, but without diving into the paper directly, I can't be certain they're actually different. This uncertainty means I should either acknowledge MoWM as related work and clearly differentiate VCSS against it, or reposition VCSS as a supporting component rather than the main contribution.

Actually, thinking through this more carefully—MoWM is about maintaining multiple world models and using them to check consistency across predictions, whereas VCSS uses one frozen WAM's video decoder as a self-consistency mechanism. That's a meaningful distinction since VCSS is designed to be a plug-in method that doesn't require training multiple models. I'm confident enough to move forward with VCSS.

With the CoRL deadline in 20 days, I need to decide between making VCSS the primary contribution with Value MLP as a fallback, or playing it safer by leading with Value MLP and treating VCSS as an ablation study. The first option has stronger novelty potential but higher risk if VCSS doesn't work empirically, while the second is more conservative and feasible.

Actually, I think the best approach is Option C—positioning both as co-primary contributions with a direct comparison. The paper becomes "we propose two complementary methods: a training-free approach using VCSS and a lightweight learned approach with Value MLP," and the comparison itself becomes the contribution. This structure works well for CoRL and gives me flexibility depending on which method performs better empirically.

Now I need to address the reviewer's concern about the RoboCasa baseline. They're pointing out that if the actual baseline is only 15-30%, expecting a 3-layer MLP to push performance to 60% or higher would require an implausibly large improvement of 30-45 percentage points. With VCSS and Value MLP as dual contributions, I can better contextualize what's realistic to achieve.

The key insight is to reframe the target: instead of trying to match fine-tuned Cosmos Policy performance, I should focus on demonstrating meaningful improvement over the frozen baseline—aiming for at least 10 percentage points gain. If the baseline happens to be above 40%, then approaching Cosmos Policy's performance becomes a secondary goal. This is a much more honest and defensible framing that doesn't rely on unrealistic expectations about what a lightweight scoring mechanism can accomplish.

So the final paper structure is: frozen WAMs can't discriminate between candidates, but they have unique video-action joint pretraining that encodes video understanding in their latents. I'll present VCSS as a training-free method that leverages the WAM's video prediction capability as a self-scorer, then Value MLP as a lightweight alternative that directly learns from success/failure labels on the action latents. The comparison between these two approaches—understanding when each works and why—becomes the core contribution.

Now I'm checking whether VCSS actually requires architectural changes to the WAM. The method involves sampling an action latent, running a single forward pass through the frozen video decoder at a specific noise level, and computing the reconstruction error. I need to verify whether the WAM's architecture supports this kind of targeted inference without modifications.

Looking at the implementation details, I can set the video timestep to T/2 and action timestep to 0, which should let me compute the video denoising error conditioned on the action latent using just one forward pass. This fits within the existing API without needing to change anything.

The computational cost is manageable—eight forward passes through the video decoder at one noise level adds about 400ms, which roughly triples the latency of action-only inference. Since the target applications prioritize success over speed, this overhead is acceptable. And since I only need one noise level evaluation rather than full denoising, the actual cost is much lower than generating complete videos.

I'm confident in this approach now. Writing the JSON...

Structuring the proposal with dual methods... The key insight is that WAMs' joint video-action pretraining creates action latents regularized by physical plausibility, which should make them better substrates for quality discrimination than standard VLA tokens. I'm exploring whether the WAM's own video prediction can serve as a zero-shot quality signal for comparing action candidates, and whether these physics-regularized latents enable more efficient value learning than raw actions.

The approach leverages WAM's independent per-modality diffusion architecture to enable both action-only inference and video-conditioned evaluation. For Predictive Consistency Scoring, I'd score each candidate action by measuring how well the WAM's video denoising aligns with its learned prior at an intermediate noise level—since training data is predominantly successful demonstrations, actions producing plausible successful futures score lower, requiring just one forward pass per candidate.

Alternatively, I could train a small MLP on WAM action latents from both successful and failed demonstrations to learn a quality function that directly scores candidates. The key insight is that action latents regularized through joint video-action pretraining should separate success from failure more cleanly than raw action outputs or VLA tokens, making the training more sample-efficient despite requiring up to 40 H100-hours.

The real contribution is comparing these two approaches: PCS needs no training but depends on whether the WAM's video prior actually correlates with task success, while the Value MLP requires collecting failure demonstrations but learns the task-specific quality function directly. I'll validate this comparison empirically on RoboCasa and LIBERO-Long to understand when self-verification alone suffices versus when labeled training becomes necessary.

Before the main ablation, I need to run a diagnostic check: measure how well PCS scores correlate with actual success on a few RoboCasa tasks using 16 rollouts per task. If the correlation is above 0.3, PCS is viable as the primary result; below 0.2 means it's a negative result and I'll pivot to Value MLP instead. For the Value MLP approach, I'll need failure demonstrations, which LIBERO-90 doesn't provide, so I'm sourcing those from a frozen UWM rollout or similar.

The computational cost for generating failures is manageable—around 15–20 H100-hours for simulation-based rollouts plus under an hour for synthetic perturbations, staying well under 40 H100-hours total. On the benchmark side, there's no published frozen UWM baseline on RoboCasa to anchor against, though other frozen models like DiT4DiT hit around 50%, which gives me a rough sense of the range. I'll run a 50-episode validation first to establish what the actual frozen baseline is, then target at least a 10 percentage point improvement over that measured baseline rather than chasing a fixed absolute number.

For the landscape, I need to add the missing papers and note that MG-Select achieves 168% on RoboCasa pick-and-place—that's a VLA result we should be able to beat with our WAM-specific methods on the harder tasks.

The approach splits into two phases: PCS diagnostic first, then the main ablation, with a value MLP fallback if PCS doesn't work out. I'm leaning toward the dual-method framing because it tells a cleaner story—WAM pretraining creates two distinct opportunities for test-time selection, one training-free through video prediction and one lightweight through value learning. Each method answers different aspects of the same question, which feels stronger for a venue like CoRL than a single contribution would be.

But I'm weighing whether to include VCSS at all. It requires 2-3 H100-hours for diagnostics and adds paper complexity, plus there's real risk—if the correlation is weak, it becomes a negative result, and if it works, it's a strong zero-training contribution that directly differentiates from VLA approaches. With the CoRL deadline 20 days away, it's a calculated gamble between a potentially exciting training-free result and the safety of relying solely on value learning.

I'm going to include VCSS. The framing works: VCSS tests the zero-training hypothesis while value learning offers a lightweight alternative, and together they answer whether frozen WAMs can self-select among candidates and at what cost. Now I'm writing out the JSON structure for the paper, starting with the title and metadata, then building each section before combining them.

Structuring the JSON...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "403d5e83-37f3-489d-8b78-cc8842ff7dc8",
  "isSidechain": false,
  "requestId": "req_011Cata4aN62fE3qDTJpop4m",
  "type": "assistant",
  "uuid": "fcc924f5-5b30-4eec-8823-8140828b9f68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01K9T2bAjSNZsWchzQbk7JVa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7332,
      "cache_read_input_tokens": 26937,
      "output_tokens": 13857,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13857,
          "cache_read_input_tokens": 26937,
          "cache_creation_input_tokens": 7332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7332
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

_source line 19 · 2026-05-10T08:31:54.279Z_

Now I have rich context. Let me synthesize before writing the revision.

**Key findings from the research:**

1. **RoVer** (2510.10975): Goes beyond simple BoN — PRM predicts refinement *directions* in action space, not just scores. 0.2B PRM, CALVIN benchmark. Paradigm is similar but not identical.

2. **MG-Select / Verifier-free** (2510.05681, ICLR 2026): Zero-training KL-from-masked-distribution scoring for VLAs — **already evaluated on RoboCasa** with 168% relative improvement. This is more damaging than RoVer for our novelty claim.

3. **WAV** (2604.14732): Architectural modification (trajectory value module integrated into forward pass). Different from frozen approach.

4. **Compose Your Policies!** (2510.01068): Distribution-level composition, not discrete selection.

5. **DiT4DiT unfinetuned** achieves 50.8% on RoboCasa — this is the only data point for frozen WAM-like baselines. UWM has no published RoboCasa results.

6. **MoWM** uses world model reconstruction to evaluate candidates — partially overlaps with a video-consistency scoring idea.

**Diagnosis of the stagnation:** The original idea's novelty argument is genuinely weak vs. the 2025-2026 VLA test-time compute literature. The core fix isn't just adding citations — the paper needs a WAM-*specific* contribution that VLA approaches fundamentally cannot replicate. The unique WAM capability is: **joint video-action pretraining regularizes action latents z_a to encode physical plausibility, AND the WAM can generate video conditioned on candidate actions for self-verification**.

**Decision: Major revision.** Add a novel training-free method (Predictive Consistency Scoring, PCS) that uses the WAM's own video decoder as a zero-training quality signal — something impossible for VLAs. Keep the value MLP as a lightweight trained alternative. The comparison between them is itself a contribution. Recalibrate RoboCasa targets. Drop DreamZero. Add all four missing papers with sharp differentiation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcc924f5-5b30-4eec-8823-8140828b9f68",
  "isSidechain": false,
  "requestId": "req_011Cata4aN62fE3qDTJpop4m",
  "type": "assistant",
  "uuid": "fb073818-d82f-4bf3-9178-0985748592cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01K9T2bAjSNZsWchzQbk7JVa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7332,
      "cache_read_input_tokens": 26937,
      "output_tokens": 13857,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13857,
          "cache_read_input_tokens": 26937,
          "cache_creation_input_tokens": 7332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7332
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

_source line 20 · 2026-05-10T08:31:57.577Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012cFEinaT7amMT6mrSNVQaJ`</summary>

```json
{
  "description": "Search for MoWM and video consistency scoring papers",
  "subagent_type": "Explore",
  "prompt": "Please fetch and summarize the following paper: MoWM: Mixture-of-World-Models for Embodied Planning (arXiv 2509.21797). Try:\n- https://arxiv.org/abs/2509.21797\n- https://arxiv.org/html/2509.21797\n\nI need to know: exactly how does MoWM use \"world model reconstruction to evaluate candidate action trajectories\"? Is it similar to using a single frozen WAM's own video denoising error as a quality signal for ranking candidate action trajectories? What are the differences?\n\nAlso search for \"predictive consistency score action selection robot\" to see if any papers have used a single model's own video reconstruction error as a zero-training quality signal for action candidate ranking in robot manipulation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb073818-d82f-4bf3-9178-0985748592cd",
  "isSidechain": false,
  "requestId": "req_011Cata4aN62fE3qDTJpop4m",
  "type": "assistant",
  "uuid": "e8f50503-16b4-4e99-935f-6d8745fb950d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01K9T2bAjSNZsWchzQbk7JVa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7332,
      "cache_read_input_tokens": 26937,
      "output_tokens": 13857,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13857,
          "cache_read_input_tokens": 26937,
          "cache_creation_input_tokens": 7332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7332
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Frozen-WAM Best-of-N: Plug-in Inference-Time Candidate Selection for P…",
  "leafUuid": "e8f50503-16b4-4e99-935f-6d8745fb950d",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate frozen UWM baseline before CoRL submission",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c"
}
```

---

### Tool result

_source line 23 · 2026-05-10T08:33:27.774Z_

<details><summary>↩ Tool result · `toolu_012cFEinaT7amMT6mrSNVQaJ`</summary>

```text
Excellent! Now I have comprehensive information. Let me compile my findings into a clear summary for the user.

## Summary: MoWM Paper and Related Work on Video Reconstruction for Action Selection

### **How MoWM Uses World Model Reconstruction for Action Evaluation**

Based on the paper content, MoWM's approach is **conceptually different** from what you described. Here are the key findings:

**MoWM's Actual Mechanism:**
- MoWM does **NOT** sample multiple action candidates and rank them by reconstruction error
- Instead, it uses an **end-to-end action planning paradigm** that "maps predicted future state sequences to action sequences via an inverse dynamics model in an end-to-end manner"
- The system works through:
  1. **Multiple world models** (hybrid models) predict future feature representations
  2. **Feature fusion** concatenates latent and pixel features from both models
  3. **Diffusion Policy** directly decodes actions from fused representations through progressive denoising refinement
- The approach explicitly **avoids sampling-based trajectory evaluation** methods, which it notes "suffer from computational inefficiency and inferior accuracy"

**Critical Difference from Your Hypothesis:**
- Your hypothesis proposes: "Use a single frozen model's own video reconstruction error to rank candidate action trajectories"
- MoWM instead: Uses multiple specialized world models in parallel, fusing their representations, then decodes actions directly without comparative scoring across trajectory candidates
- The "reconstruction" aspect refers to improving **feature quality** rather than computing reconstruction error as a ranking metric

### **Related Work: Single Model Reconstruction Error for Action Selection**

While my search found **no papers explicitly using a single frozen model's own reconstruction error as a zero-training quality signal for action ranking**, I found highly related approaches:

**1. Ensemble-Based Uncertainty Approach (Closest Related Work)**
- **Uncertainty-Aware Robotic World Model (RWM-U)** uses bootstrap ensemble **disagreement** as a quality signal
- Method: Multiple models predict trajectories, and disagreement variance reflects prediction reliability
- Application: Penalizes uncertain action-state regions during planning via uncertainty-weighted rewards
- **Key insight**: This is ensemble-based (multiple models), not single-model reconstruction error
- Source: [Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots](https://arxiv.org/html/2504.16680v3)

**2. Video Generation Quality for Action Selection**
- **X-WAM** uses video generation quality evaluation, but separates it from action decoding
  - Actions are decoded early (few denoising steps) and executed immediately
  - Video denoising continues separately for high-fidelity reconstruction
  - Uses Dynamic Time Warping (DTW) distance between ground truth and IDM-predicted actions to filter generations
- **VideoScore** learns automatic metrics to predict human-provided video quality scores
- **MSG Score** combines perceptual quality and thematic consistency for multi-scene video generation evaluation

**3. Ensemble Disagreement for Action Selection**
- PETS (Probabilistic Ensembles with Trajectory Sampling) pioneered using multiple model predictions for decision-making
- **Exploration Through Disagreement**: Recent work uses model disagreement to encourage visiting high-uncertainty states
- Source: [Planning to Explore via Self-Supervised World Models](http://proceedings.mlr.press/v119/sekar20a/sekar20a.pdf)

**4. General Trajectory Evaluation Metrics**
- Standard metrics for video prediction quality: PSNR, SSIM, latent L2, FVD (Fréchet Video Distance)
- Latent L2 and PSNR capture reconstruction error in latent and pixel space respectively
- These are used primarily for **evaluation**, not as real-time action selection signals

### **Key Distinction**

Your proposed approach (single frozen model's own video reconstruction error as action ranking signal) **appears novel**. The closest existing work is:
- **Ensemble disagreement** (multiple models) rather than single-model reconstruction error
- **Video quality metrics** (used post-hoc for evaluation or filtering, not during rollout planning)
- **Uncertainty estimation** (from ensemble variance, not single-model reconstruction)

The landscape suggests that single-model reconstruction error is **not widely used** as a zero-training quality signal for action ranking in the literature, which could indicate either: (a) it hasn't been thoroughly explored, or (b) ensemble approaches are preferred for robustness.

---

### Sources Referenced:
- [MoWM: Mixture-of-World-Models for Embodied Planning](https://arxiv.org/abs/2509.21797)
- [Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots](https://arxiv.org/html/2504.16680v3)
- [X-WAM: Unified 4D World Action Modeling from Video](https://sharinka0715.github.io/X-WAM/)
- [Planning to Explore via Self-Supervised World Models](http://proceedings.mlr.press/v119/sekar20a/sekar20a.pdf)
- [VideoScore: Building Automatic Metrics to Simulate Fine-grained Human Feedback for Video Generation](https://arxiv.org/html/2406.15252)
- [Benchmarking World-Model Learning](https://arxiv.org/html/2510.19788v1)
- [A Survey of Embodied World Models](https://fi.ee.tsinghua.edu.cn/public/publications/0940dda4-af15-11f0-9d60-0242ac120002.pdf)
- [World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/html/2605.00080v1)
- [Physics-Based Causal Reasoning for Safe & Robust Next-Best Action Selection in Robot Manipulation Tasks](https://arxiv.org/html/2403.14488v1/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8f50503-16b4-4e99-935f-6d8745fb950d",
  "isSidechain": false,
  "promptId": "bb9c012d-2d31-4744-9b38-e53a44843a6f",
  "type": "user",
  "uuid": "543e7da3-a342-4409-82fa-739808b12042",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Please fetch and summarize the following paper: MoWM: Mixture-of-World-Models for Embodied Planning (arXiv 2509.21797). Try:\n- https://arxiv.org/abs/2509.21797\n- https://arxiv.org/html/2509.21797\n\nI need to know: exactly how does MoWM use \"world model reconstruction to evaluate candidate action trajectories\"? Is it similar to using a single frozen WAM's own video denoising error as a quality signal for ranking candidate action trajectories? What are the differences?\n\nAlso search for \"predictive consistency score action selection robot\" to see if any papers have used a single model's own video reconstruction error as a zero-training quality signal for action candidate ranking in robot manipulation.",
    "agentId": "a61f899b1a9e14415",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now I have comprehensive information. Let me compile my findings into a clear summary for the user.\n\n## Summary: MoWM Paper and Related Work on Video Reconstruction for Action Selection\n\n### **How MoWM Uses World Model Reconstruction for Action Evaluation**\n\nBased on the paper content, MoWM's approach is **conceptually different** from what you described. Here are the key findings:\n\n**MoWM's Actual Mechanism:**\n- MoWM does **NOT** sample multiple action candidates and rank them by reconstruction error\n- Instead, it uses an **end-to-end action planning paradigm** that \"maps predicted future state sequences to action sequences via an inverse dynamics model in an end-to-end manner\"\n- The system works through:\n  1. **Multiple world models** (hybrid models) predict future feature representations\n  2. **Feature fusion** concatenates latent and pixel features from both models\n  3. **Diffusion Policy** directly decodes actions from fused representations through progressive denoising refinement\n- The approach explicitly **avoids sampling-based trajectory evaluation** methods, which it notes \"suffer from computational inefficiency and inferior accuracy\"\n\n**Critical Difference from Your Hypothesis:**\n- Your hypothesis proposes: \"Use a single frozen model's own video reconstruction error to rank candidate action trajectories\"\n- MoWM instead: Uses multiple specialized world models in parallel, fusing their representations, then decodes actions directly without comparative scoring across trajectory candidates\n- The \"reconstruction\" aspect refers to improving **feature quality** rather than computing reconstruction error as a ranking metric\n\n### **Related Work: Single Model Reconstruction Error for Action Selection**\n\nWhile my search found **no papers explicitly using a single frozen model's own reconstruction error as a zero-training quality signal for action ranking**, I found highly related approaches:\n\n**1. Ensemble-Based Uncertainty Approach (Closest Related Work)**\n- **Uncertainty-Aware Robotic World Model (RWM-U)** uses bootstrap ensemble **disagreement** as a quality signal\n- Method: Multiple models predict trajectories, and disagreement variance reflects prediction reliability\n- Application: Penalizes uncertain action-state regions during planning via uncertainty-weighted rewards\n- **Key insight**: This is ensemble-based (multiple models), not single-model reconstruction error\n- Source: [Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots](https://arxiv.org/html/2504.16680v3)\n\n**2. Video Generation Quality for Action Selection**\n- **X-WAM** uses video generation quality evaluation, but separates it from action decoding\n  - Actions are decoded early (few denoising steps) and executed immediately\n  - Video denoising continues separately for high-fidelity reconstruction\n  - Uses Dynamic Time Warping (DTW) distance between ground truth and IDM-predicted actions to filter generations\n- **VideoScore** learns automatic metrics to predict human-provided video quality scores\n- **MSG Score** combines perceptual quality and thematic consistency for multi-scene video generation evaluation\n\n**3. Ensemble Disagreement for Action Selection**\n- PETS (Probabilistic Ensembles with Trajectory Sampling) pioneered using multiple model predictions for decision-making\n- **Exploration Through Disagreement**: Recent work uses model disagreement to encourage visiting high-uncertainty states\n- Source: [Planning to Explore via Self-Supervised World Models](http://proceedings.mlr.press/v119/sekar20a/sekar20a.pdf)\n\n**4. General Trajectory Evaluation Metrics**\n- Standard metrics for video prediction quality: PSNR, SSIM, latent L2, FVD (Fréchet Video Distance)\n- Latent L2 and PSNR capture reconstruction error in latent and pixel space respectively\n- These are used primarily for **evaluation**, not as real-time action selection signals\n\n### **Key Distinction**\n\nYour proposed approach (single frozen model's own video reconstruction error as action ranking signal) **appears novel**. The closest existing work is:\n- **Ensemble disagreement** (multiple models) rather than single-model reconstruction error\n- **Video quality metrics** (used post-hoc for evaluation or filtering, not during rollout planning)\n- **Uncertainty estimation** (from ensemble variance, not single-model reconstruction)\n\nThe landscape suggests that single-model reconstruction error is **not widely used** as a zero-training quality signal for action ranking in the literature, which could indicate either: (a) it hasn't been thoroughly explored, or (b) ensemble approaches are preferred for robustness.\n\n---\n\n### Sources Referenced:\n- [MoWM: Mixture-of-World-Models for Embodied Planning](https://arxiv.org/abs/2509.21797)\n- [Uncertainty-Aware Robotic World Model Makes Offline Model-Based Reinforcement Learning Work on Real Robots](https://arxiv.org/html/2504.16680v3)\n- [X-WAM: Unified 4D World Action Modeling from Video](https://sharinka0715.github.io/X-WAM/)\n- [Planning to Explore via Self-Supervised World Models](http://proceedings.mlr.press/v119/sekar20a/sekar20a.pdf)\n- [VideoScore: Building Automatic Metrics to Simulate Fine-grained Human Feedback for Video Generation](https://arxiv.org/html/2406.15252)\n- [Benchmarking World-Model Learning](https://arxiv.org/html/2510.19788v1)\n- [A Survey of Embodied World Models](https://fi.ee.tsinghua.edu.cn/public/publications/0940dda4-af15-11f0-9d60-0242ac120002.pdf)\n- [World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/html/2605.00080v1)\n- [Physics-Based Causal Reasoning for Safe & Robust Next-Best Action Selection in Robot Manipulation Tasks](https://arxiv.org/html/2403.14488v1/)"
      }
    ],
    "totalDurationMs": 90192,
    "totalTokens": 28656,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 960,
      "cache_read_input_tokens": 26289,
      "output_tokens": 1400,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 960
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1400,
          "cache_read_input_tokens": 26289,
          "cache_creation_input_tokens": 960,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 960,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "e8f50503-16b4-4e99-935f-6d8745fb950d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T08:33:38.319Z_

<details><summary>Logged reasoning block</summary>

```text
Key finding: MoWM does NOT use single-model reconstruction error for action ranking. It uses multiple world models with feature fusion. So VCSS/PCS (single frozen WAM video denoising error as quality signal for ranking candidates) appears to be novel.

Also important: no existing paper uses a single model's own video reconstruction error as a zero-training action quality signal. This is genuinely novel.

Now I have enough information to write the final JSON. Let me do it.

Key points for the revision:
1. Add PCS (Predictive Consistency Scoring) as a training-free method - appears genuinely novel
2. Add all 4 missing papers with strong differentiation


3. I need to adjust the RoboCasa benchmarks upward to show at least 10 percentage points of improvement, drop DreamZero from consideration, and strengthen the theoretical grounding around why the WAM approach works. Now I'm ready to construct the full JSON with these refinements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "543e7da3-a342-4409-82fa-739808b12042",
  "isSidechain": false,
  "requestId": "req_011CataZFTMYYZL445xJqqyv",
  "type": "assistant",
  "uuid": "6b919b8d-e277-4b9c-b772-eac8052e4742",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012XWsbyzPkE74DZR2AsB4v7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15236,
      "cache_read_input_tokens": 34269,
      "output_tokens": 9573,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9573,
          "cache_read_input_tokens": 34269,
          "cache_creation_input_tokens": 15236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15236
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

_source line 25 · 2026-05-10T08:37:16.989Z_

Good - MoWM uses multiple world models with feature fusion, not single-model reconstruction error scoring. The PCS approach appears genuinely novel. Now I have everything I need. Let me write the full revision.

The core strategic shift: add **Predictive Consistency Scoring (PCS)** — a zero-training WAM-specific method that uses the WAM's own video decoder forward pass as a quality signal for candidate actions. This is fundamentally impossible for VLAs, creates clean differentiation from RoVer and MG-Select, and makes the paper's WAM-specific argument empirical rather than asserted. The value MLP becomes a complementary lightweight-trained alternative. The comparison between the two is itself a contribution.

```json
{
  "title": "Video-Grounded Candidate Selection for Frozen World Action Models: Predictive Consistency Scoring and Action-Latent Value Learning",
  "core_problem": "Pretrained WAMs generate a single action trajectory at inference and provide no mechanism to compare candidate futures. Adding planning capability currently requires one of three costly interventions: (1) full fine-tuning of the video model on robot demos (Cosmos Policy, ICLR 2026: 384–3,072 H100-hours); (2) training a separate action-conditioned world model alongside the frozen policy (GPC, RAL 2025); or (3) architectural co-design or RL loops (H-WM, GigaBrain RAMP, WAV). Fast-WAM (arXiv 2603.16666) demonstrates that action-only inference achieves 97.6% on LIBERO and 91.8% on RoboTwin at 190ms, motivating candidate generation from frozen WAM action-only inference rather than expensive video rollouts.\n\nThe VLA test-time compute literature (2025–2026) has addressed candidate selection for VLA architectures: RoVer (arXiv 2510.10975, ICLR 2026) trains a 0.2B Process Reward Model to score and directionally refine VLA candidates on CALVIN; Verifier-free / MG-Select (arXiv 2510.05681, ICLR 2026) uses KL-divergence from a masked unconditional VLA distribution as a training-free confidence signal, achieving 168% relative improvement on RoboCasa pick-and-place; Compose Your Policies! (arXiv 2510.01068) composes multiple frozen policy distributions without candidate selection. None of these approaches exploit WAMs' unique property: joint video-action pretraining that regularizes action latents z_a to be consistent with physically plausible visual futures. Two fundamental questions remain unanswered: (1) Can a WAM's own video prediction capability serve as a zero-training quality signal for action candidates — impossible for VLAs lacking video generation? (2) Do WAM action latents, regularized by video-physics during joint pretraining, enable more sample-efficient quality discrimination than action-space representations from VLAs? No existing work provides answers to either question or demonstrates Best-of-N candidate selection using only a WAM's internal representations — either zero-training or lightweight-trained — without modifying any WAM weights.",
  "opportunity": "UWM's independent per-modality diffusion timestep architecture (RSS 2025) natively supports both action-only inference (video timestep = T, action timestep = 0) and mixed-mode forward passes. This creates two complementary WAM-specific approaches to candidate selection, exploiting different aspects of the WAM's joint video-action pretraining:\n\n**Method 1 — Predictive Consistency Scoring (PCS, zero additional training)**: For each of B=4–8 action-only candidate trajectories a_i sampled from frozen UWM, compute the WAM's video denoising error at one intermediate noise level t* = T/2, conditioned on the candidate action latent: S_PCS(a_i) = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||². This is a single video decoder forward pass per candidate (~50ms), totaling 200–400ms for B=4–8 — acceptable for success-critical tasks. The theoretical basis: since UWM's training demonstrations are predominantly successful human teleoperation (LIBERO-90, DROID), the WAM's video prior is biased toward visual futures consistent with successful manipulation. Action trajectories that are physically implausible or likely to fail produce visual predictions that deviate from the WAM's learned prior, yielding higher denoising error. PCS is WAM-specific: VLAs have no video generation capability and cannot self-verify candidate quality in this way. Candidate selection: a_{i*} = argmin_i S_PCS(a_i) (hard argmin). This differentiates from MG-Select's KL-from-masked-distribution approach, which measures distributional uncertainty in action space rather than video-content consistency.\n\n**Method 2 — Action-Latent Value MLP (≤40 H100-hours training)**: A 3-layer MLP trained on WAM action latents z_a from LIBERO-90 success demonstrations AND explicitly collected failure trajectories scores each candidate via V(z_{a,i}) ∈ [0,1]. Hard argmax Best-of-N (a_{i*} = argmax_i V(z_{a,i})) is the primary result, chosen to avoid the multi-modal action-averaging artifact documented in Diffusion Policy (Chi et al., 2023). Key hypothesis: z_a regularized by joint video-action pretraining encodes physical plausibility in a way that makes MLP-based quality discrimination more sample-efficient than equivalent MLP training over raw action outputs or VLA action tokens (the latent structure argument). Failure demonstrations collected via frozen UWM rollouts in simulation (~15–20 H100-hours) plus Gaussian-perturbed synthetic failures (<1 H100-hour).\n\n**Comparison of PCS vs. Value MLP is itself a central contribution**: PCS requires zero training but relies on the WAM's video prior correlating with task success; Value MLP requires failure demonstration collection but directly learns the task-specific quality function. Their empirical comparison on RoboCasa and LIBERO-Long characterizes when WAM self-verification is sufficient versus when labeled training adds necessary discriminative power. A PCS diagnostic (B=16 rollouts on 3 RoboCasa tasks, measuring Spearman correlation of S_PCS with ground-truth success, target ρ > 0.3) validates the PCS premise before the main ablation. If ρ < 0.2, PCS is reported as a negative result and Value MLP becomes the primary contribution — both outcomes are publishable and informative.\n\n**Mandatory RoboCasa baseline validation before committing to targets**: No published results of frozen UWM on RoboCasa exist (UWM evaluated primarily on LIBERO and DROID; the closest published data point is DiT4DiT unfinetuned at 50.8% on RoboCasa, a different architecture). A 50-episode baseline with B=1 frozen UWM action-only inference on a representative RoboCasa subset precedes all experiments. Primary performance target: ≥10pp absolute improvement over the measured frozen baseline, regardless of absolute value. Secondary framing (approaching Cosmos Policy's 67.1%) applies only if baseline ≥ 40%; if baseline is 15–30%, the target becomes ≥10pp absolute improvement and the comparison shifts from 'approaching fine-tuned performance' to 'demonstrating that WAM-specific selection enables meaningful gains without any fine-tuning, at ≤40 H100-hours cost.' Both framings are publishable; the former is stronger but contingent on baseline validation.",
  "landscape": "Cosmos Policy (arXiv 2601.16163, ICLR 2026) is the primary comparison point for absolute performance. Fully fine-tunes Cosmos-Predict2-2B on robot demos (384 H100-hours ALOHA, 1,536 RoboCasa, 3,072 LIBERO). Achieves 98.5% LIBERO and 67.1% RoboCasa. Architecture-specific to Cosmos-Predict2; not plug-in compatible with other WAMs; requires full retraining per domain. Our method keeps all WAM weights frozen and costs ≤40 H100-hours.\n\nFast-WAM (arXiv 2603.16666, May 2026) is the critical framing reference. Test-time video generation adds only 0.5–1.9 percentage points: 97.6% LIBERO-avg and 91.8% RoboTwin without video at inference, at 190ms latency. Generates a single action trajectory with no candidate comparison. Our method builds on Fast-WAM's action-only inference for fast B-candidate generation, adds candidate selection. Fast-WAM targets latency-critical deployment (single trajectory, fastest); our method targets success-critical tasks (B trajectories, select best). Complementary Pareto points.\n\nRoVer (arXiv 2510.10975, ICLR 2026) — CRITICAL MISSING CITATION. Generates B candidate actions from frozen VLAs (GR-1, Dita, MoDE), trains a 0.2B Process Reward Model (PRM) that scores candidates AND predicts refinement directions in action space. Not just argmax selection — the PRM enables directed exploration. Evaluated on CALVIN + real robot. Achieves +17.4% chain length improvement on GR-1. Differentiation from our work: (1) RoVer requires training a 0.2B PRM on process labels; our PCS method requires zero training and our value MLP requires only a 3-layer MLP (~5M parameters); (2) RoVer applies to VLA architectures with output-space action tokens that lack video-physics regularization; our methods target WAM action latents z_a jointly trained with video, which encode physical plausibility in a way VLA tokens cannot; (3) RoVer's PRM is architecture-specific to VLAs; our methods are WAM-specific and exploit the video generation capability VLAs lack; (4) RoVer provides directed candidate refinement but no training-free option; our PCS requires no training and uses the WAM's own video knowledge as quality signal.\n\nVerifier-free Test-Time Sampling / MG-Select (arXiv 2510.05681, ICLR 2026) — CRITICAL MISSING CITATION. Training-free Best-of-N for frozen VLAs using KL-divergence from a condition-masked unconditional distribution as confidence signal. Achieves 168% relative improvement on RoboCasa pick-and-place; 28–35% improvement on real Franka. Differentiation from our work: (1) MG-Select's confidence signal measures distributional uncertainty (how much the VLA's conditional distribution shifts from its unconditional prior) — an action-space uncertainty proxy; our PCS measures video-content consistency (whether the WAM's video prior endorses the action as physically plausible) — a content-knowledge signal; (2) MG-Select is applicable to any VLA but cannot exploit video generation capability; our PCS is WAM-specific and requires no additional training beyond the WAM's existing pretraining; (3) MG-Select was evaluated on RoboCasa pick-and-place (simpler tasks); we evaluate on RoboCasa's full benchmark including multi-stage tasks where content knowledge should outperform distributional uncertainty as a quality signal.\n\nCompose Your Policies! / GPC (arXiv 2510.01068) — MISSING CITATION. Training-free convex composition of multiple frozen policy distributional scores, without candidate ranking. Different from our approach: GPC operates at the distribution level (combining score functions of multiple policies) rather than selecting among discrete sampled candidates; requires multiple compatible policies rather than a single frozen WAM; cannot exploit WAM-specific video generation capability.\n\nWAV: World-Value-Action Model (arXiv 2604.14732, April 2026) — SIGNIFICANT OVERLAPPING MOTIVATION. Proposes a trajectory value module that evaluates long-horizon utility via iterative latent-space inference, progressively concentrating probability mass on high-value action trajectories. 99.6% on LIBERO, 75.6% real-world dual-arm. Differentiation: WAV integrates a trajectory value module as a new architectural component requiring training from scratch; our method leaves all WAM weights completely frozen and adds only a lightweight scoring module (PCS: zero parameters; Value MLP: ~5M parameters). WAV modifies the architecture; Frozen-WAM BoN leaves all weights frozen and is plug-in compatible with pretrained WAMs.\n\nGPC / GPC-RANK (arXiv 2502.00622, IEEE RAL 2025): frozen policy + separately trained action-conditioned world model + hard argmax. Requires training both a policy and a separate world model. Our method uses the WAM's own action latent space as the evaluation substrate (no separate world model) and requires only demonstration-derived training data.\n\nWhen to Trust Imagination (arXiv 2605.06222, May 2026): FFDC adaptively decides action chunk sizes during single-trajectory execution. In-execution adaptation vs. our pre-execution selection. Orthogonal and combinable.\n\nOA-WAM (arXiv 2605.06481): object-addressable manipulation, different problem. CKT-WAM (arXiv 2605.06247): cross-WAM knowledge transfer, different problem. ChEaP (arXiv 2603.30043): 2D maze early commitment, not manipulation. DreamZero (arXiv 2602.15922): secondary reference. GigaBrain-0.5M* (arXiv 2602.12099): RAMP RL loops requiring 30%+ more training. H-WM (arXiv 2602.11291): hierarchical architectural co-design. Compositional Planning with Jumpy World Models (arXiv 2602.19634): WM training from scratch. PiJEPA (arXiv 2603.25981): MPPI over deterministic JEPA latents for navigation. Latent Diffusion Planning (arXiv 2504.16925): diffusion planner trained from scratch.",
  "approach": "Primary backbone: UWM (github.com/WEIRDLabUW/unified-world-model, RSS 2025), whose independent per-modality diffusion timestep architecture supports both action-only inference (policy mode: video timestep = T, action timestep = 0) and video-conditioned evaluation (mixed-mode: video timestep = t*, action timestep = 0). All WAM weights frozen throughout. DreamZero cross-WAM validation deferred to camera-ready — the UWM result is sufficient for the CoRL submission.\n\n**Step 0a — Frozen UWM Baseline Validation on RoboCasa (MANDATORY FIRST STEP, before any other experiment)**: Run B=1 frozen UWM action-only inference on 50 episodes of representative RoboCasa tasks (kitchen manipulation subset). Record baseline success rate. Decision tree: if baseline ≥ 40%, proceed with current framing ('approaching Cosmos Policy performance at 40× lower training cost'); if baseline 15–35%, recalibrate all targets to '≥10pp absolute improvement over frozen baseline' and reframe comparison away from absolute Cosmos Policy benchmark. Cost: ~2–3 H100-hours.\n\n**Step 0b — Failure Demonstration Collection (required for Value MLP)**: (a) Primary negatives: run frozen UWM (B=1) on LIBERO-Long and validated RoboCasa tasks; expected failure rate 30–50% on RoboCasa tasks, 5–15% on LIBERO-Long, yielding 500–2,000 failure trajectories. Cost: 15–20 H100-hours. (b) Synthetic supplement: Gaussian action perturbation (σ ∈ {0.05, 0.1}) on 20% of LIBERO-90 success demos, simulate in MuJoCo, flag truncated episodes as failures. Cost: <1 H100-hour. Combined: balanced 2,000–4,000 positive / 2,000–4,000 negative training set.\n\n**Step 1 — PCS Diagnostic (NEW — mandatory before main ablation)**: Validate whether the WAM's video denoising error S_PCS(a_i) = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||² correlates with ground-truth task success. Protocol: sample B=16 action-only candidates from frozen UWM on 3 RoboCasa tasks, execute each in simulation (ground-truth success/failure), compute S_PCS for each. Metrics: (1) Spearman correlation ρ of S_PCS with success labels (target ρ > 0.3); (2) AUC of S_PCS as binary success predictor (target AUC > 0.6); (3) variance of S_PCS across B=16 samples (std < 0.02 suggests near-uniform degenerate scoring). Also vary t* ∈ {T/4, T/2, 3T/4} to find the noise level most correlated with success. Presented as a required diagnostic figure in the paper. If ρ < 0.2 at all noise levels, PCS is reported as a negative result and the value MLP becomes the sole primary contribution — both outcomes are scientifically informative.\n\n**Step 2 — Diversity Pilot (combined with PCS diagnostic)**: Same B=16 rollouts used for PCS diagnostic also measure: pairwise cosine distance of action latents {z_{a,i}} (target mean > 0.05; if lower, increase noise temperature T_noise ∈ {1.5, 2.0}); Spearman correlation of V(z_{a,i}) with success after MLP training (target ρ > 0.3). Binary classification accuracy on held-out demo set also reported as sanity check for latent separability premise.\n\n**Step 3 — Demo Encoding**: Encode LIBERO-90 success demos plus collected failures through frozen UWM in action-only mode, obtaining clean WAM action latents z_a with success/failure labels. Cost: ~10–15 H100-hours.\n\n**Step 4 — Value MLP Training**: 3-layer MLP (input: flattened z_a; output: scalar V ∈ [0,1]) trained via binary cross-entropy on balanced success/failure latents. Report binary classification accuracy on held-out split. Cost: ~3–5 H100-hours. Total additional training cost: ≤40 H100-hours.\n\n**Step 5 — Inference-Time Best-of-N Planning**: At each planning step, sample B=4–8 action-only trajectories from frozen UWM.\n\nPrimary results (two methods):\n- PCS selection: a_{i*} = argmin_i S_PCS(a_i) at optimal t* from diagnostic [zero training, WAM-specific]\n- Value MLP selection: a_{i*} = argmax_i V(z_{a,i}) [lightweight training, WAM-specific]\n\nAblation (secondary): soft MPPI w_i ∝ exp(β·V(z_{a,i})) to document action-averaging artifact; MG-Select-style KL scoring applied to WAM (apply MG-Select's method to WAM in action-only mode) as VLA-method baseline applied to WAM.\n\n**Ablation Grid**: B ∈ {1, 2, 4, 8, 16} (B=1 is frozen WAM single-trajectory baseline); selection method: PCS (primary zero-training) vs. Value MLP hard argmax (primary trained) vs. MG-Select-style KL (VLA method applied to WAM, baseline) vs. soft MPPI β ∈ {0.5, 1, 2, 5} (ablation only) vs. random selection (sanity check); noise temperature T_noise ∈ {1.0, 1.5, 2.0} (informed by diversity pilot); video denoising noise level t* ∈ {T/4, T/2, 3T/4} (informed by PCS diagnostic); action-only latent vs. full video+action latent for Value MLP scoring (ablation of video component's contribution to scoring).\n\n**Execution regimes**: (a) open-loop — B trajectories at episode start, execute selected; (b) periodic replanning every K=5 action chunks.\n\n**Primary hypotheses**: (H1) PCS achieves ρ > 0.3 with ground-truth success and yields ≥5pp improvement over B=1 baseline on RoboCasa (confirms WAM video prior encodes quality). (H2) Value MLP achieves ≥10pp improvement over B=1 baseline on RoboCasa (confirms WAM action latents are quality-discriminative). (H3) Value MLP outperforms PCS on harder tasks (multi-stage RoboCasa), while PCS outperforms MG-Select-style KL scoring (confirming video-content knowledge outperforms distributional uncertainty). (H4) Both methods underperform hard argmax relative to soft MPPI on multi-modal tasks (action-averaging artifact).\n\n**Evaluation Benchmarks**: (a) Primary — RoboCasa: Cosmos Policy fine-tuned at 1,536 H100-hours achieves 67.1%; DiT4DiT unfinetuned (closest frozen baseline data point) achieves 50.8%; frozen UWM baseline to be validated in Step 0a. Absolute target recalibrated based on Step 0a measurement. (b) Secondary — LIBERO-Long: near saturation for strong frozen WAMs (Fast-WAM 95.2%); included to characterize gain profile vs. task difficulty and as a more tractable validation if RoboCasa baseline is very low. (c) Baselines: single-trajectory WAM (B=1), random selection (B=4–8), MG-Select-style KL applied to WAM (VLA approach applied to WAM backbone), Cosmos Policy published results (cited, not reproduced).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~150h H100",
      "gpu_utilization": "HIGH idle (~40–60%): GPU waits while researcher implements PCS forward pass at mixed timestep, debugs failure collection pipeline, interprets PCS diagnostic results, and designs ablations",
      "timeline": "2–3 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$375 (150h × $2.50/h blended Lambda/RunPod/Vast.ai H100 rate)"
    },
    "human_in_loop": {
      "gpu_hours": "~180h H100",
      "gpu_utilization": "MODERATE idle (~20–30%): agent handles code scaffolding, baseline validation, PCS diagnostic, failure collection, demo encoding, and experiment submission; human reviews Step 0a baseline and PCS diagnostic results at daily check-ins to make go/no-go decisions",
      "timeline": "3–5 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$150–250 (~1,500–2,500 turns at mixed Sonnet/Opus rates)",
      "estimated_gpu_cost": "~$450 (180h × $2.50/h)",
      "risk_note": "Step 0a (frozen UWM RoboCasa baseline) and PCS diagnostic are hard sequential dependencies that must complete before main ablation begins. Sequential order: 0a baseline validation (2–3 H100-hours, Day 1–2) → PCS diagnostic (3–5 H100-hours, Day 2–4) → failure collection (15–20 H100-hours, Day 3–7, can run in parallel with PCS) → demo encoding (10–15 H100-hours, Day 5–9) → Value MLP training (3–5 H100-hours, Day 9–10) → main ablations (Day 10–18). RoboCasa simulation setup requires separate engineering effort from LIBERO. PCS may require UWM mixed-mode forward pass implementation not present in public repository (video timestep = t*, action timestep = 0 with given action latent). DreamZero cross-WAM deferred to camera-ready; CoRL submission rests on UWM alone."
    },
    "auto_research": {
      "gpu_hours": "~350h H100 (UWM backbone only; full B/T_noise/t* ablation grid; RoboCasa + LIBERO-Long; multiple seeds; PCS diagnostic and Value MLP comparisons)",
      "gpu_utilization": "MINIMAL idle (~5–10%): agent pipelines baseline validation, PCS diagnostic, failure collection, demo encoding, MLP training, and evaluation continuously",
      "timeline": "8–12 days with 4–8 H100 GPUs simultaneously",
      "team": "0 (only initial repo setup and credential configuration)",
      "claude_api_cost": "$200–350 (~2,500–4,000 turns at Opus rates)",
      "estimated_gpu_cost": "~$875 (350h × $2.50/h)",
      "speed_bottleneck": "Step 0a baseline validation → PCS diagnostic → (parallel: failure collection + demo encoding) → Value MLP training is a 5-step sequential dependency spanning ~8 days minimum. RoboCasa evaluation rollouts: each ablation variant requires sequential per-task evaluation (3–5h per variant); with 4 GPUs running 4 variants concurrently, the full grid needs ~6–8 days.",
      "risk_note": "PCS requires implementing UWM mixed-mode forward pass (video decoder at t* conditioned on z_{a,i}, action timestep = 0 for given latent) — not a standard inference mode in the public UWM repository and may require low-level model surgery. If UWM architecture does not support conditioning video denoising on a fixed action latent (rather than jointly denoising), PCS must be removed and the paper falls back to Value MLP as sole primary contribution."
    }
  },
  "target_venues": [
    "CoRL 2026 (Abstract deadline: May 26, 2026; Full paper: May 29, 2026; Conference: Nov 9–12, Austin TX) — TIGHT but viable: 19 days from 2026-05-10. Step 0a RoboCasa baseline must run immediately (Day 1–2). Minimum viable submission: frozen UWM RoboCasa baseline validation + PCS diagnostic figure + PCS and/or Value MLP Best-of-N results (primary) + LIBERO-Long (secondary) + B/hard-argmax ablation + MG-Select-style KL baseline comparison. DreamZero cross-WAM deferred to camera-ready.",
    "ICLR 2027 (deadline ~September–October 2026) — More feasible timeline for complete ablation grid, PCS theory development, DreamZero cross-WAM evaluation, and potential real-world experiments."
  ],
  "level": "solid",
  "key_references": [
    "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning (arXiv 2601.16163, ICLR 2026) — CRITICAL PRIOR WORK: full fine-tune of Cosmos-Predict2-2B (1,536 H100-hours for RoboCasa), 98.5% LIBERO, 67.1% RoboCasa; not plug-in compatible; our method targets comparable RoboCasa performance at ≤40 H100-hours",
    "Fast-WAM: World Action Models without Test-Time Video (arXiv 2603.16666, May 2026) — CRITICAL FRAMING: test-time video generation adds only 0.5–1.9 pts; 97.6% LIBERO, 91.8% RoboTwin at 190ms without video; single trajectory only; our method uses same action-only inference for candidate generation and adds selection; PCS adds one video decoder pass per candidate at intermediate noise level",
    "RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Models (arXiv 2510.10975, ICLR 2026) — CRITICAL MISSING CITATION: generates B VLA candidates, trains 0.2B PRM that scores AND provides refinement directions; evaluated on CALVIN + real robot; differentiation: (1) requires 0.2B PRM vs. our zero-training PCS or 3-layer value MLP; (2) VLA action tokens lack video-physics regularization; (3) cannot exploit video generation capability",
    "Verifier-free Test-Time Sampling for Vision Language Action Models / MG-Select (arXiv 2510.05681, ICLR 2026) — CRITICAL MISSING CITATION: training-free KL-from-masked-distribution scoring for frozen VLAs; 168% relative improvement on RoboCasa pick-and-place; differentiation: KL measures action-space distributional uncertainty, PCS measures video-content physical consistency; MG-Select cannot exploit video generation; our methods exploit WAM-specific video-action joint pretraining",
    "Compose Your Policies! / GPC (arXiv 2510.01068) — MISSING CITATION: training-free distribution composition for multiple frozen policies; operates at distribution level, not discrete candidate selection; requires multiple compatible policies; cannot exploit WAM video generation",
    "World-Value-Action (WAV) Model (arXiv 2604.14732, April 2026) — SIGNIFICANT OVERLAPPING MOTIVATION: trajectory value module for long-horizon utility evaluation via iterative latent-space inference; 99.6% LIBERO, 75.6% real-world; differentiation: WAV integrates value module as a new architectural component requiring training from scratch; our method leaves all WAM weights frozen and uses plug-in PCS or value MLP",
    "When to Trust Imagination: Adaptive Action Execution for World Action Models (arXiv 2605.06222, May 2026) — CONCURRENT WORK: FFDC adaptively decides when to replan during single-trajectory execution; 69% fewer forward passes, 2.54% SR improvement on RoboTwin; orthogonal to our pre-execution selection; the two can be combined",
    "Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling / GPC (arXiv 2502.00622, IEEE RAL 2025) — CRITICAL PRIOR WORK: frozen policy + separately trained world model + hard argmax; our method replaces separate world model with WAM's own action latent or video scoring",
    "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets / UWM (arXiv 2504.02792, RSS 2025) — primary backbone; independent per-modality timesteps support action-only inference (video timestep = T) AND mixed-mode (video timestep = t*, action timestep = 0 for PCS); publicly available weights and code",
    "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (arXiv 2303.04137, RSS 2023 / IJRR 2024) — documents multi-modal action distribution handling; confirms averaging over manipulation action modes produces infeasible blended actions; justifies hard argmax over soft MPPI weighting",
    "World Action Models are Zero-shot Policies / DreamZero (arXiv 2602.15922) — 14B joint video+action DiT; secondary backbone for cross-WAM validation in camera-ready/ICLR version",
    "OA-WAM: Object-Addressable World Action Model (arXiv 2605.06481, May 2026) — concurrent work; different problem (object binding); 97.8% LIBERO, 79.3% SimplerEnv",
    "CKT-WAM: Parameter-Efficient Context Knowledge Transfer (arXiv 2605.06247, May 2026) — concurrent work; different problem (cross-WAM knowledge transfer with <2% trainable parameters)",
    "Video Models Reason Early: Exploiting Plan Commitment for Maze Solving / ChEaP (arXiv 2603.30043) — 2D mazes only; not manipulation; our method does not rely on partial denoising for plan commitment",
    "GigaBrain-0.5M*: a VLA That Learns From World Model-Based Reinforcement Learning (arXiv 2602.12099) — RAMP RL loop requires 30%+ more training",
    "H-WM: Robotic Task and Motion Planning Guided by Hierarchical World Model (arXiv 2602.11291) — requires hierarchical architectural co-design",
    "Compositional Planning with Jumpy World Models (arXiv 2602.19634) — requires WM training from scratch",
    "Policy-Guided World Model Planning for Language-Conditioned Visual Navigation / PiJEPA (arXiv 2603.25981) — MPPI over deterministic JEPA latents for navigation, not manipulation",
    "Latent Diffusion Planning for Imitation Learning (arXiv 2504.16925) — trains diffusion planner from scratch"
  ],
  "description": "Video-Grounded Candidate Selection (VGCS) converts any pretrained video-diffusion World Action Model into a multi-candidate planner at inference time without modifying any WAM weight, and uniquely exploits the WAM's joint video-action pretraining through two complementary methods that VLA-based approaches cannot replicate.\n\nThe key WAM-specific insight: joint video-action pretraining regularizes action latents z_a to be consistent with physically plausible visual futures, and the WAM's video decoder can be queried at inference to assess whether a candidate action is consistent with the model's learned physics prior — a capability VLAs fundamentally lack. This motivates two methods: Predictive Consistency Scoring (PCS), which is zero-training and WAM-specific, and Action-Latent Value MLP, which is lightweight-trained. Comparing them empirically characterizes when WAM self-verification is sufficient vs. when labeled training is necessary.\n\n**Method 1 — PCS (zero training)**: Sample B=4–8 action-only trajectories from frozen UWM in action-only mode (video timestep = T, action timestep = 0). For each candidate a_i, run ONE video decoder forward pass at intermediate noise level t* = T/2, conditioned on action latent z_{a,i}: compute S_PCS(a_i) = ||ε − ε_θ(x_{t*}, z_{a,i}, t*)||². Select argmin_i S_PCS(a_i). Since UWM training demonstrations are predominantly successful, the WAM's video prior is biased toward visual futures consistent with successful manipulation; actions inconsistent with learned physics produce higher denoising error. This is fundamentally different from MG-Select's KL-from-masked-distribution (distributional uncertainty, no content knowledge) and from RoVer's trained PRM (requires 0.2B model training); PCS uses only the frozen WAM's existing knowledge. Overhead: B × ~50ms = 200–400ms for B=4–8.\n\n**Method 2 — Value MLP (≤40 H100-hours)**: Train a 3-layer MLP on WAM action latents z_a from success demonstrations (LIBERO-90) and explicitly collected failure trajectories (online rollouts of frozen UWM in simulation, ~15–20 H100-hours, plus Gaussian-perturbed synthetic failures). Hard argmax selection (a_{i*} = argmax_i V(z_{a,i})) avoids the multi-modal action-averaging artifact documented in Diffusion Policy. The central value MLP hypothesis: z_a regularized by joint video-action pretraining is more separable under success/failure labels than raw action outputs or VLA action tokens, enabling effective quality discrimination with minimal training data.\n\nMandatory diagnostics: (1) frozen UWM RoboCasa baseline validation (50 episodes, B=1) before committing to performance targets; (2) PCS diagnostic measuring Spearman ρ of S_PCS with ground-truth success (B=16 rollouts, 3 tasks; target ρ > 0.3); (3) binary classification accuracy of value MLP on held-out demos (latent separability sanity check). Primary evaluation: RoboCasa (primary target: ≥10pp absolute improvement over validated frozen baseline; Cosmos Policy 67.1% at 1,536 H100-hours as upper reference). Secondary: LIBERO-Long (near saturation, characterizes gain profile vs. task difficulty). Key ablation: PCS vs. Value MLP vs. MG-Select-style KL applied to WAM (VLA method applied to WAM backbone) vs. random selection. CoRL submission: UWM only. DreamZero cross-WAM deferred to camera-ready.",
  "project_name": "frozen_wam_mppi",
  "source": "web_research",
  "change_type": "major"
}
```

**Summary of what changed and why:**

The revision makes three substantive improvements over the previous version:

1. **New primary method (PCS)** that provides genuine conceptual novelty vs. the VLA test-time compute literature. MG-Select's 168% improvement on RoboCasa pick-and-place using KL-from-masked-distribution means the original value MLP alone isn't differentiated enough — PCS uses the WAM's own video decoder as a zero-training quality signal, which is impossible for VLAs and not done by any prior work (MoWM uses ensembles of world models, not a single frozen WAM's self-consistency).

2. **All four missing papers added** (RoVer, MG-Select, Compose Your Policies!, WAV) with differentiation arguments grounded in mechanism, not just benchmark differences. MG-Select specifically is added as an explicit within-WAM baseline (apply MG-Select's method to UWM) so we can empirically demonstrate PCS > KL approach on the same backbone.

3. **Recalibrated targets and mandatory baseline validation** — the "≥60% RoboCasa" target is replaced by "≥10pp over validated baseline" with a 50-episode diagnostic before any other experiment. This eliminates the critical reviewer concern while keeping the result publishable under either baseline scenario.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b919b8d-e277-4b9c-b772-eac8052e4742",
  "isSidechain": false,
  "requestId": "req_011CataZFTMYYZL445xJqqyv",
  "type": "assistant",
  "uuid": "425eeee6-980f-415d-af1d-ecf2a5786222",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012XWsbyzPkE74DZR2AsB4v7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15236,
      "cache_read_input_tokens": 34269,
      "output_tokens": 9573,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9573,
          "cache_read_input_tokens": 34269,
          "cache_creation_input_tokens": 15236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15236
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Frozen-WAM Best-of-N: Plug-in Inference-Time Candidate Selection for P…",
  "leafUuid": "425eeee6-980f-415d-af1d-ecf2a5786222",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate frozen UWM baseline before CoRL submission",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Frozen-WAM Best-of-N: Plug-in Inference-Time Candidate Selection for P…",
  "leafUuid": "425eeee6-980f-415d-af1d-ecf2a5786222",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate frozen UWM baseline before CoRL submission",
  "sessionId": "d0aef627-83d9-4adc-aaf2-81b51c36b38c"
}
```

---
