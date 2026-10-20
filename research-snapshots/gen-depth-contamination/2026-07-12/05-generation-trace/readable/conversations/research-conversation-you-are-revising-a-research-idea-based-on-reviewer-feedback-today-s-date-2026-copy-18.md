# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/4efdeba3-01a8-4084-b912-0729c5e53d52.jsonl`
- **Structured JSON:** [`8c8781e7161068cfcc47.json`](../../sessions/8c/8c8781e7161068cfcc47.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T20:17:29.699Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T20:17:29.699Z",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Geometric Sensitivity Filtering: Training-Free Score Subspace Projection for Robust Diffusion-Based Robot Policies Under Geometric Perturbation\",\n  \"core_problem\": \"Diffusion-based robot policies (World-Action Models, VLAs with diffusion/flow heads) achieve near-saturated standard benchmark performance (Fast-WAM 97.6%, OA-WAM 97.8% on LIBERO) but degrade catastrophically under geometric perturbations — camera viewpoint and robot initial state changes cause drops to 30–80% on LIBERO-Plus. All existing solutions require either architectural modification (OA-WAM: object-addressable slots, SDP: SE(3)-equivariant spherical Fourier architecture) or additional training (CKT-WAM: context knowledge transfer fine-tuning, equivariant architectures: training from scratch in equivariant representations). No training-free, architecture-agnostic inference-time method exists for geometric robustness of pre-trained diffusion policies. The fundamental question: can we improve geometric robustness of ANY pre-trained diffusion policy at test time, without modifying the architecture or retraining? We hypothesize YES, based on a key observation: under geometric perturbation, certain components of the action score function become unreliable (they encode viewpoint-specific spatial features that don't generalize) while other components remain reliable (they encode semantic/task-progress information that is viewpoint-invariant). By identifying and suppressing the unreliable components via local geometric sensitivity analysis, we can improve robustness at the cost of modest precision loss — a favorable trade-off for manipulation tasks where semantic understanding matters more than pixel-precise spatial mapping.\",\n  \"opportunity\": \"Four converging developments create a precise research opportunity: (1) LIBERO-Plus (2025) and the WAM robustness study (March 2026) establish that geometric perturbation is the dominant failure mode, with performance drops from 95% to below 30% under modest camera/robot perturbations. The geometric perturbation SOTA stands at OA-WAM Camera 80.5% (requires 7B architecture redesign) and CKT-WAM total 86.1% (requires fine-tuning). (2) SE(3)-equivariant diffusion policies (SDP/ICML 2025, EquiBot, ReSeFlow) demonstrate that geometric equivariance dramatically improves robustness — but all require training the entire model from scratch in equivariant representations. No test-time alternative exists. (3) Inference-time scaling for diffusion models is a rapidly validated paradigm (ICLR 2025-2026): noise trajectory search, FK steering with reward functions, and test-time policy composition (GPC/ICLR 2026) all show that spending additional compute at inference can substitute for training-time improvements. But none target geometric robustness specifically. (4) DiffStateGrad (ICLR 2025) establishes SVD-based subspace projection as effective for filtering guidance signals in diffusion models, while CPC theory (NeurIPS 2025) provides theoretical grounding for when selective amplification/suppression of score components helps. Both operate in image domains; neither has been applied to robot policy scores under distribution shift. The gap is clear: a principled method to spend inference-time compute on geometric robustness filtering, applicable to any pre-trained diffusion/flow policy without modification.\",\n  \"landscape\": \"**Geometric robustness methods (all require training/architecture changes):** OA-WAM (May 2026): object-addressable architecture with per-slot decomposition and address-only key projection, 7B params, Camera 80.5%, Robot 89.6% — requires complete architectural redesign. CKT-WAM (May 2026): parameter-efficient context knowledge transfer, total 86.1% — requires fine-tuning. SE(3)-Equivariant Diffusion Policy [SDP] (ICML 2025): spherical Fourier space embedding with equivariant FiLM layers, strong generalization to SE(3) transforms — requires training from scratch with equivariant architecture. EquiBot (2024): SIM(3)-equivariant networks + diffusion — architecture-specific. ReSeFlow (ICRA 2026): SE(3)-equivariant flow-matching — architecture-specific. Being-H0.7 (May 2026): 82.1% zero-shot / 84.8% fine-tuned on LIBERO-Plus. AnyCamVLA (March 2026): zero-shot camera adaptation via feed-forward novel view synthesis — training-free but VLA-specific, camera-only, requires known camera parameters. **Training-free inference-time methods for diffusion policies (none target geometric robustness):** GPC/Compose Your Policies (ICLR 2026): convex score composition from multiple heterogeneous policies — requires multiple trained policies, doesn't target geometry. ADPro (2025): test-time manifold-constrained denoising with FGR registration — requires point cloud observations, evaluated only on RLBench/CALVIN. GPC/Predictive World Model (RA-L 2025): inference-time look-ahead with separately trained world model. Inference-time scaling (ICLR 2025): noise trajectory search for better samples — general quality, not robustness-specific. FK steering (ICLR 2026): reward-guided inference-time steering — requires defining an appropriate reward. TTPL (April 2026): test-time perturbation learning with delayed feedback for VLAs — requires online learning from environment feedback during deployment, +7.4% on LIBERO. **SVD/spectral methods in diffusion models:** DiffStateGrad (ICLR 2025): SVD projection for image inverse problems. Mechanistic cross-attention subspace analysis (AAAI 2025): concept-encoding subspaces. Score Augmentation [ScoreAug] (2025): equivariant training augmentation in score space. CPC theory (NeurIPS 2025): CFG implicit decomposition into selective amplification. All single-modal image settings. **Training-free geometric augmentation for robot policies:** Data augmentation at training time is standard; test-time augmentation for classification is standard; but TEST-TIME SCORE-SPACE FILTERING using geometric sensitivity analysis has NOT been proposed for diffusion-based robot policies. **Gap:** No existing work (1) provides a purely inference-time, architecture-agnostic method for geometric robustness of pre-trained diffusion/flow policies, (2) uses geometric sensitivity analysis of the score function to identify and suppress unreliable components, or (3) evaluates such a method on LIBERO-Plus geometric perturbations. GSF fills all three gaps simultaneously.\",\n  \"approach\": \"We propose Geometric Sensitivity Filtering (GSF), a training-free inference-time method that improves geometric robustness of ANY pre-trained diffusion/flow-based robot policy by projecting action scores onto geometrically-stable subspaces identified through local sensitivity analysis.\\n\\n**Core Mechanism.** At each denoising/integration step t during inference:\\n1. Given current observation o and noisy action a_t, compute the nominal score: s_0 = s_θ(a_t, t | o)\\n2. Generate K=4 small geometric augmentations of the observation: {T_k(o)} where T_k are random camera jitter (±3° rotation, ±5% translation) or spatial crops\\n3. Compute augmented scores: s_k = s_θ(a_t, t | T_k(o)) for k=1,...,K\\n4. Compute score covariance across augmentations: C_t = (1/K) Σ_k (s_k - s̄)(s_k - s̄)^T where s̄ is the mean\\n5. SVD of C_t = U_t Λ_t U_t^T. The TOP eigenvectors (high eigenvalues) correspond to score directions with HIGH geometric sensitivity — these are the unreliable components under geometric perturbation\\n6. Construct projection: Π_t = I - Σ_{i: λ_i > τ·λ_max} u_i u_i^T (suppress top-sensitivity directions)\\n7. Apply filtered score: s_filtered = Π_t · s_0\\n8. Use s_filtered for the denoising/integration step\\n\\n**Theoretical Motivation.** Under the training distribution, ALL score components are reliable — the policy has seen similar observations. Under geometric perturbation (OOD camera/robot-init), the observation shifts from the training manifold. Score components encoding viewpoint-specific spatial features (e.g., pixel-coordinate-dependent reaching directions) become unreliable because they were learned for a specific viewpoint. Score components encoding viewpoint-invariant semantics (e.g., object identity, grasp type, task phase) remain reliable because they generalize across viewpoints. GSF identifies the unreliable components through their HIGH SENSITIVITY to small geometric perturbations (if a small camera jitter changes the score dramatically in direction u_i, that direction encodes viewpoint-specific information). This is analogous to how DiffStateGrad projects gradients onto low-rank state subspaces, but our filtering criterion is GEOMETRIC SENSITIVITY rather than state-space rank, and our domain is cross-modal robot control rather than image restoration.\\n\\n**Adaptive Filtering Schedule.** Not all denoising steps are equally sensitive to geometry. Early steps (high noise) determine coarse trajectory structure and are most geometry-dependent; later steps refine timing and precision. We apply GSF with adaptive strength: strong filtering (lower τ, suppress more) at early steps, weak filtering (higher τ, suppress less) at later steps. This follows the β-CFG principle of timestep-adaptive guidance.\\n\\n**Computational Overhead.** GSF requires K+1 forward passes per denoising step (1 nominal + K augmented). For K=4 and T=10 denoising steps, this is 50 vs. 10 forward passes — 5x overhead. Three optimizations reduce this: (i) Apply GSF only at the first M=3-4 denoising steps where geometry matters most (reducing to 10 + 12-16 = 22-26 passes, ~2.5x overhead). (ii) Cache visual backbone features for augmented views across denoising steps (augmentations are applied to the observation, which doesn't change across steps). (iii) For flow-matching policies with few integration steps (OA-WAM uses 4 steps), the overhead is minimal.\\n\\n**Backbone Strategy.** Primary: Fast-WAM (97.6% standard LIBERO, released code + checkpoints on HuggingFace, diffusion action head, real-time inference). Fast-WAM's architecture (MoT with video DiT backbone + action expert DiT) is representative of modern WAMs. Secondary: Standard Diffusion Policy (original Chi et al., widely used baseline, released code). Extension: OA-WAM checkpoint if available — demonstrating that GSF provides ADDITIONAL improvement on top of an already-robust architecture would be the strongest possible result, showing complementarity with training-time approaches.\\n\\n**Evaluation Strategy.** Primary benchmark: LIBERO-Plus geometric perturbations — Camera (L1, L3 difficulty) and Robot-Init (L1, L3), plus Light as control condition (non-geometric, expect no benefit). Standard LIBERO as sanity check (expect slight degradation from information loss, confirming the semantic/spatial decomposition). Baselines: (i) Fast-WAM standard inference, (ii) Fast-WAM + uniform test-time augmentation (TTA — average action PREDICTIONS from augmented views, the naive approach), (iii) Fast-WAM + score-space mean (average scores then denoise — GPC-style composition), (iv) Fast-WAM + GSF (ours). Ablations: (a) filtering threshold τ sensitivity, (b) number of augmentations K ∈ {2, 4, 8}, (c) augmentation type (camera jitter vs. spatial crop vs. both), (d) adaptive vs. uniform filtering schedule, (e) which denoising steps to apply GSF (early-only vs. all), (f) cross-task consistency of sensitive subspaces (do the same directions show high sensitivity across different tasks?). Framing vs. competitors: GSF is training-free and architecture-agnostic, complementary to OA-WAM/CKT-WAM/SDP. We explicitly frame it as the test-time counterpart of training-time equivariant methods: SDP builds geometric invariance into the architecture; GSF enforces approximate geometric stability at inference via score filtering.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~80-110h H100\",\n      \"gpu_utilization\": \"Moderate (35-45%). Human sets up Fast-WAM + LIBERO-Plus integration, implements GSF pipeline (SVD of score covariance, augmentation generation, projection), runs evaluation sweeps.\",\n      \"timeline\": \"2-2.5 weeks (feasible for CoRL abstract May 26, paper May 29)\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"$200-330 (at ~$2.50-3.00/H100-hr spot pricing)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~90-130h H100\",\n      \"gpu_utilization\": \"Moderate-high (55-70%). Agent implements GSF on Fast-WAM, integrates LIBERO-Plus evaluation, runs systematic sweeps. Human reviews intermediate results (~30min/day).\",\n      \"timeline\": \"12-16 days (targets CoRL 2026 abstract May 26, paper May 29)\",\n      \"team\": \"1 researcher, ~30min/day\",\n      \"claude_api_cost\": \"$80-200 (estimated ~800-2000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$225-390\",\n      \"risk_note\": \"Primary risk is GSF's filtering being too aggressive (removing task-relevant spatial info) or too weak (not suppressing enough noise). The threshold τ sweep mitigates this — even if the best τ varies per task, demonstrating the principle on any subset of tasks is sufficient.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~110-170h H100\",\n      \"gpu_utilization\": \"High (>80%). Agent runs continuous augmentation-type sweep → threshold sweep → evaluation loop.\",\n      \"timeline\": \"9-13 days with 2-4 GPUs concurrently\",\n      \"team\": \"0 (initial setup only, ~1.5 hours)\",\n      \"claude_api_cost\": \"$150-350 (estimated ~1500-3500 Opus turns)\",\n      \"estimated_gpu_cost\": \"$275-510\",\n      \"speed_bottleneck\": \"The main computational cost is K+1 forward passes per denoising step during evaluation. With 10 LIBERO-Plus tasks × 20 episodes × 150 steps × 5 threshold values = 150K policy calls per condition. At ~200ms per call on H100, each condition takes ~8h. 4 conditions (Camera L1/L3, Robot L1/L3) + standard LIBERO = ~40-50h for the full sweep.\",\n      \"risk_note\": \"Unlike the original Phase 1 contingency, GSF either helps or doesn't — no fundamental architectural blocker. If filtering threshold is optimized per-task, the practical value still holds since calibration requires only 5-10 episodes.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract May 26, paper May 29 — PRIMARY TARGET; 16-19 days; no Phase 1 gate means direct method development and evaluation; Fast-WAM checkpoint availability eliminates setup risk)\",\n    \"AAAI 2027 (deadline Aug 2, 2026 — secondary target; allows extension to OA-WAM backbone, multi-policy composition, deeper analysis of which score components encode what)\",\n    \"ICLR 2027 (deadline Sep 24, 2026 — fallback; allows comprehensive multi-backbone study across Fast-WAM, Diffusion Policy, OA-WAM, and VLAs, plus theoretical analysis connecting GSF to equivariance theory)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv March 2026) — PRIMARY BACKBONE; 97.6% standard LIBERO, released code + checkpoints, MoT architecture with video DiT backbone + action expert DiT; provides strong standard performance baseline for measuring GSF's robustness improvement\",\n    \"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv May 2026) — LIBERO-Plus Camera SOTA at 80.5%, Robot 89.6%; flow-matching action head with 4-step Euler; requires 7B architectural redesign; GSF is complementary (training-free, can potentially be applied on top)\",\n    \"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models (arXiv May 2026) — LIBERO-Plus total SOTA at 86.1%; requires additional fine-tuning; GSF is complementary\",\n    \"SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space [SDP] (ICML 2025) — training-time equivariant architecture for geometric generalization; GSF is the TEST-TIME counterpart — achieves approximate geometric stability without requiring equivariant architecture or retraining\",\n    \"Diffusion State-Guided Projected Gradient for Inverse Problems [DiffStateGrad] (ICLR 2025) — SVD-based subspace projection in diffusion models; key methodological predecessor; our contribution: replace state-defined projection with GEOMETRIC SENSITIVITY-defined projection, extend from image restoration to robot policy robustness\",\n    \"Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition [GPC] (ICLR 2026) — test-time score composition from multiple policies; proves convex score combination yields superior objectives; our distinction: same policy with geometric augmentations (not multiple policies), targeting robustness (not general quality)\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (arXiv 2025) — 7-dimension perturbation benchmark establishing geometric perturbation as dominant failure mode (drops from 95% to <30%)\",\n    \"Do World Action Models Generalize Better than VLAs? A Robustness Study (arXiv March 2026) — WAMs weak on geometric perturbations; motivates the robustness focus\",\n    \"Towards Understanding the Mechanisms of Classifier-Free Guidance [CPC Theory] (NeurIPS 2025) — theoretical grounding for when selective amplification/suppression of score components improves generation quality; applies to our sensitivity-based suppression\",\n    \"ADPro: Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising (2025) — related training-free inference-time approach; requires point cloud observations and task-geometric knowledge; evaluated on RLBench/CALVIN only; GSF is observation-modality-agnostic and requires no geometric knowledge\",\n    \"Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps (ICLR 2025) — establishes paradigm of spending additional inference compute for better diffusion samples; GSF is an instance of this paradigm applied specifically to geometric robustness\",\n    \"A General Framework for Inference-time Scaling and Steering of Diffusion Models [FK Steering] (ICLR 2026) — Feynman-Kac guided inference with arbitrary rewards; related but requires explicit reward function; GSF uses implicit geometric sensitivity as the signal\",\n    \"Test-Time Perturbation Learning with Delayed Feedback for VLA Models [TTPL] (arXiv April 2026) — test-time adaptation with online feedback; requires environment interaction during deployment; GSF requires no online learning or feedback\",\n    \"Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv May 2026) — LIBERO-Plus 82.1% zero-shot / 84.8% fine-tuned\",\n    \"AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust VLA Models (arXiv March 2026) — training-free camera adaptation via novel view synthesis; requires known camera parameters; VLA-specific, camera-perturbation-only\",\n    \"Score Augmentation for Diffusion Models [ScoreAug] (arXiv 2025) — equivariant training augmentation in score space; demonstrates that geometric transformations of noisy data establish equivariant learning objectives; training-time complement to our test-time approach\",\n    \"EquiBot: SIM(3)-Equivariant Diffusion Policy for Generalizable Learning (2024) — training-time equivariant architecture; related goal (geometric generalization) but fundamentally different mechanism (architectural vs. inference-time)\",\n    \"Classifier-free Guidance with Adaptive Scaling [β-CFG] (arXiv Feb 2025) — timestep-adaptive guidance scheduling; informs our adaptive filtering schedule\",\n    \"Classifier-Free Diffusion Guidance (NeurIPS 2021 Workshop) — foundational technique; GSF's augmentation-based filtering is related to guidance (both modify the score) but uses sensitivity analysis rather than conditional/unconditional decomposition\",\n    \"X-WAM: Unified 4D World Action Modeling with Asynchronous Denoising (arXiv April 2026) — alternative WAM architecture with coupled timestep sampling; critiques independent timestep mechanisms; GSF avoids timestep-mechanism dependency entirely\",\n    \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (RSS 2023) — foundational diffusion policy; secondary backbone candidate for demonstrating architecture-agnosticism\",\n    \"Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling [GPC-WM] (RA-L 2025) — inference-time enhancement via separately trained world model; requires additional model; GSF uses only the policy itself\",\n    \"When to Trust Imagination: Adaptive Action Execution for World Action Models [FFDC] (arXiv May 2026) — confidence-based replanning; orthogonal to GSF (decides WHEN to act; GSF improves HOW the score is computed)\"\n  ],\n  \"description\": \"We propose Geometric Sensitivity Filtering (GSF), a training-free inference-time method that improves geometric robustness of ANY pre-trained diffusion/flow-based robot policy by projecting action scores onto geometrically-stable subspaces. The key insight: under geometric perturbation (camera viewpoint change, robot initial state change), certain components of the policy's score function become unreliable because they encode viewpoint-specific spatial features, while components encoding task semantics remain reliable. GSF identifies unreliable components through their HIGH SENSITIVITY to small geometric augmentations at test time: at each denoising step, we compute scores from K=4 small geometric perturbations of the observation, perform SVD on the score covariance to find high-sensitivity directions, and project the nominal score onto the complementary (low-sensitivity) subspace before continuing denoising. This is the test-time counterpart of SE(3)-equivariant architectures (SDP/ICML 2025, EquiBot): where they build geometric invariance into training, GSF enforces approximate geometric stability at inference via score subspace projection. Unlike all existing geometric robustness methods — OA-WAM (Camera 80.5%, requires 7B architectural redesign), CKT-WAM (total 86.1%, requires fine-tuning), SDP (requires equivariant architecture) — GSF is training-free, architecture-agnostic, and can be applied to any pre-trained diffusion/flow policy including potentially on TOP of these methods for additional improvement. The method extends DiffStateGrad's SVD-based projection from single-modal image restoration to robot policy robustness, with the key innovation being geometric sensitivity as the projection criterion (rather than state-space rank). Evaluated on LIBERO-Plus geometric perturbations (Camera, Robot-Init at L1/L3 difficulty) using Fast-WAM (97.6% standard LIBERO) as primary backbone. Computational overhead is ~2.5x (applying GSF at early denoising steps only with cached visual features), comparable to standard classifier-free guidance. Ablations include filtering threshold, augmentation type/count, adaptive scheduling, and cross-task consistency of sensitive subspaces. The method is positioned as complementary to training-time approaches: spending modest additional inference compute to achieve geometric robustness that would otherwise require architectural redesign or retraining.\",\n  \"project_name\": \"geometric_sensitivity_filtering_diffusion_policy\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 7)\nIssues: [\"FAST-WAM HAS NO LIBERO-PLUS BASELINE (CRITICAL): After exhaustive search — the Fast-WAM paper, OA-WAM's Table 2 (which compares 16 baselines), the WAM robustness study (arXiv 2603.22078, which evaluates Cosmos-Policy/GE-Act/VLA-JEPA but NOT Fast-WAM) — Fast-WAM has never been evaluated on LIBERO-Plus. The proposal assumes Fast-WAM's LIBERO-Plus performance will show meaningful degradation under geometric perturbation, but this is unverified. If Fast-WAM somehow maintains >85% on camera perturbation (unlikely but possible given its strong 97.6% standard performance), the room for GSF improvement is small. Conversely, if it drops to <40% (possible given LIBERO-Plus findings of 95%→<30% drops), GSF would need enormous improvement to reach competitive absolute numbers. This baseline MUST be established in the first 2-3 days before committing to the full plan.\", \"CORE ASSUMPTION IS UNTESTED AND MAY BE WRONG: GSF assumes that SVD of the score covariance under small geometric augmentations (±3° rotation, ±5% translation) cleanly separates 'viewpoint-specific spatial features' (high eigenvalues) from 'viewpoint-invariant semantics' (low eigenvalues). This decomposition is a hypothesis, not a fact. In robot manipulation, spatial precision IS the task — reaching, grasping, and placing all depend on precise spatial features. Suppressing the 'high sensitivity' directions may suppress exactly the task-relevant spatial information needed for successful manipulation. The proposal acknowledges 'modest precision loss' but provides no evidence this trade-off is favorable. Furthermore, the augmentation magnitude (±3°) is much smaller than LIBERO-Plus camera perturbations — the first-order sensitivity at the nominal observation may not predict which score directions fail under large perturbations.\", \"TERMINOLOGY ERROR: FAST-WAM USES FLOW-MATCHING, NOT DIFFUSION: Fast-WAM explicitly uses flow matching ('trained to predict the corresponding velocity field with a standard flow matching objective') with 10 integration steps. The proposal consistently refers to 'action scores' and 'score function' but the correct term is 'velocity field.' While the SVD filtering mechanism applies identically to velocity vectors, the terminology throughout the proposal is technically incorrect and will raise reviewer concerns about the authors' understanding of the backbone model. Replace all 'score' references with 'velocity field' when discussing Fast-WAM.\", \"OA-WAM GEO-AVG DISCREPANCY: The proposal claims OA-WAM's 'Geo-Avg 84.3%' but the OA-WAM paper's own summary states 'Geo-Avg 76.0' which is defined as mean of Camera/Robot/Layout geometric axes. The 84.3% appears to be (Camera 80.5 + Robot 89.6) / 2 without Layout. This discrepancy must be corrected — using the wrong number inflates the apparent target and misrepresents the competitive landscape.\", \"MISSING RELATED WORK — DREAMING THE UNSEEN (DDP, March 2026): 'Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness' (arXiv 2603.21017) addresses OOD robustness of diffusion policies by coupling with a predictive world model. Achieves 73.8% OOD success on MetaWorld and 83.3% under severe real-world spatial shifts. While DDP is a training-time method, it directly addresses geometric robustness of diffusion policies and must be cited. Also missing: Visual-Geometry Diffusion Policy (VGDP, Nov 2025) which achieves 15.2% improvement in spatial perturbation settings via complementarity-aware multimodal fusion.\", \"GSF VS. SIMPLE TTA — THE MAKE-OR-BREAK COMPARISON: The proposal includes 'Fast-WAM + uniform TTA (average action predictions from augmented views)' as a baseline. This is the critical comparison. If simple prediction averaging from augmented views (which requires the same K+1 forward passes) achieves similar improvement to GSF's SVD-based filtering, then the entire SVD/covariance/projection mechanism adds complexity without benefit. The theoretical argument for why SVD-based filtering should outperform simple averaging is missing. In the image domain, test-time augmentation ensembles are strong baselines — GSF must clearly beat this.\", \"COMPARISON AGAINST TTPL (April 2026) IS COMPLICATED: TTPL achieves +7.4% on LIBERO via test-time perturbation learning with delayed feedback. TTPL is also training-free at inference (no fine-tuning needed) and uses augmentation-based uncertainty estimation + action voting — conceptually related to GSF's augmentation-based sensitivity analysis. TTPL's augmentation + voting mechanism is simpler than GSF's SVD filtering. If TTPL's simpler approach achieves larger gains, GSF's complexity is hard to justify. The proposal should compare against TTPL or explicitly differentiate (TTPL requires environment feedback during deployment; GSF does not).\"]\nFeedback: The pivot from SCG to GSF is a substantial improvement — the mechanism is cleaner, the backbone dependency is resolved, and the architecture-agnostic claim is better justified. But three critical issues must be addressed before this is CoRL-ready:\n\n**1. ESTABLISH FAST-WAM LIBERO-PLUS BASELINE IMMEDIATELY (Days 1-3):** This is the single most important unknown. Set up LIBERO-Plus perturbation pipeline with Fast-WAM's released checkpoint. Run Camera L1/L3 and Robot-Init L1/L3 with 20 episodes each — ~10-15h H100, 2-3 days. This tells you: (a) how much Fast-WAM degrades under geometric perturbation (the ceiling for GSF improvement), (b) whether the degradation pattern is consistent with the viewpoint-specific-spatial-feature hypothesis, and (c) whether the absolute numbers are competitive enough to be meaningful alongside OA-WAM's results.\n\n**2. ADD A SIMPLE TTA BASELINE AND THEORETICAL ARGUMENT FOR WHY SVD FILTERING IS BETTER:** The key question is not 'does augmentation help?' but 'does SVD-based filtering help MORE than simple averaging?' Include this baseline: compute K augmented velocity fields and average them directly (no SVD), then denoise with the averaged field. If this achieves similar improvement to GSF, the SVD mechanism is unnecessary. Provide a clear argument for when/why SVD filtering outperforms averaging — hypothesis: averaging retains all directions equally, including high-sensitivity directions where the augmented predictions disagree (noise), while GSF suppresses these noisy directions. This is testable and, if confirmed, is the core technical insight.\n\n**3. FIX TERMINOLOGY AND NUMBERS:** (a) Replace 'score' with 'velocity field' throughout when discussing Fast-WAM/flow-matching policies. GSF works on both diffusion scores and flow-matching velocity fields — make this explicit. (b) Correct OA-WAM Geo-Avg to 76.0 (mean of Camera/Robot/Layout) rather than 84.3 (appears to be Camera+Robot only). (c) Cite DDP (arXiv 2603.21017) and VGDP (arXiv 2511.22445) as related work.\n\n**4. CONSIDER A PHASE-0 DIAGNOSTIC:** Before implementing full GSF, run a quick diagnostic: for a few LIBERO-Plus camera-perturbed episodes, compute velocity fields from 4-8 small augmentations and visualize the eigenvalue spectrum of the covariance matrix. If the spectrum is flat (all eigenvalues similar), there's no low-rank structure to exploit and GSF will fail. If there's a clear spectral gap (top 2-3 eigenvalues dominate), GSF has a chance. This takes ~2h of compute and 1 day of analysis, and prevents committing 2 weeks to an approach that has no structural basis.\n\n**5. FRAME CONTRIBUTION CAREFULLY:** Don't claim GSF is 'the test-time counterpart of SE(3)-equivariant methods.' SE(3)-equivariant methods achieve exact mathematical equivariance by architectural design. GSF achieves approximate geometric stability via heuristic sensitivity-based filtering. The gap is enormous. Instead, frame GSF as: 'a lightweight inference-time method for improving geometric robustness of pre-trained policies, complementary to training-time equivariant approaches, requiring only K+1 forward passes and no architectural modification.'\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 7 轮修订，近 3 轮的平均分从 3.2 到 3.4，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T20:17:29.704Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T20:17:29.704Z",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-10T20:17:29.732Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Geometric Sensitivity Filtering: Training-Free Score Subspace Projection for Robust Diffusion-Based Robot Policies Under Geometric Perturbation",
  "core_problem": "Diffusion-based robot policies (World-Action Models, VLAs with diffusion/flow heads) achieve near-saturated standard benchmark performance (Fast-WAM 97.6%, OA-WAM 97.8% on LIBERO) but degrade catastrophically under geometric perturbations — camera viewpoint and robot initial state changes cause drops to 30–80% on LIBERO-Plus. All existing solutions require either architectural modification (OA-WAM: object-addressable slots, SDP: SE(3)-equivariant spherical Fourier architecture) or additional training (CKT-WAM: context knowledge transfer fine-tuning, equivariant architectures: training from scratch in equivariant representations). No training-free, architecture-agnostic inference-time method exists for geometric robustness of pre-trained diffusion policies. The fundamental question: can we improve geometric robustness of ANY pre-trained diffusion policy at test time, without modifying the architecture or retraining? We hypothesize YES, based on a key observation: under geometric perturbation, certain components of the action score function become unreliable (they encode viewpoint-specific spatial features that don't generalize) while other components remain reliable (they encode semantic/task-progress information that is viewpoint-invariant). By identifying and suppressing the unreliable components via local geometric sensitivity analysis, we can improve robustness at the cost of modest precision loss — a favorable trade-off for manipulation tasks where semantic understanding matters more than pixel-precise spatial mapping.",
  "opportunity": "Four converging developments create a precise research opportunity: (1) LIBERO-Plus (2025) and the WAM robustness study (March 2026) establish that geometric perturbation is the dominant failure mode, with performance drops from 95% to below 30% under modest camera/robot perturbations. The geometric perturbation SOTA stands at OA-WAM Camera 80.5% (requires 7B architecture redesign) and CKT-WAM total 86.1% (requires fine-tuning). (2) SE(3)-equivariant diffusion policies (SDP/ICML 2025, EquiBot, ReSeFlow) demonstrate that geometric equivariance dramatically improves robustness — but all require training the entire model from scratch in equivariant representations. No test-time alternative exists. (3) Inference-time scaling for diffusion models is a rapidly validated paradigm (ICLR 2025-2026): noise trajectory search, FK steering with reward functions, and test-time policy composition (GPC/ICLR 2026) all show that spending additional compute at inference can substitute for training-time improvements. But none target geometric robustness specifically. (4) DiffStateGrad (ICLR 2025) establishes SVD-based subspace projection as effective for filtering guidance signals in diffusion models, while CPC theory (NeurIPS 2025) provides theoretical grounding for when selective amplification/suppression of score components helps. Both operate in image domains; neither has been applied to robot policy scores under distribution shift. The gap is clear: a principled method to spend inference-time compute on geometric robustness filtering, applicable to any pre-trained diffusion/flow policy without modification.",
  "landscape": "**Geometric robustness methods (all require training/architecture changes):** OA-WAM (May 2026): object-addressable architecture with per-slot decomposition and address-only key projection, 7B params, Camera 80.5%, Robot 89.6% — requires complete architectural redesign. CKT-WAM (May 2026): parameter-efficient context knowledge transfer, total 86.1% — requires fine-tuning. SE(3)-Equivariant Diffusion Policy [SDP] (ICML 2025): spherical Fourier space embedding with equivariant FiLM layers, strong generalization to SE(3) transforms — requires training from scratch with equivariant architecture. EquiBot (2024): SIM(3)-equivariant networks + diffusion — architecture-specific. ReSeFlow (ICRA 2026): SE(3)-equivariant flow-matching — architecture-specific. Being-H0.7 (May 2026): 82.1% zero-shot / 84.8% fine-tuned on LIBERO-Plus. AnyCamVLA (March 2026): zero-shot camera adaptation via feed-forward novel view synthesis — training-free but VLA-specific, camera-only, requires known camera parameters. **Training-free inference-time methods for diffusion policies (none target geometric robustness):** GPC/Compose Your Policies (ICLR 2026): convex score composition from multiple heterogeneous policies — requires multiple trained policies, doesn't target geometry. ADPro (2025): test-time manifold-constrained denoising with FGR registration — requires point cloud observations, evaluated only on RLBench/CALVIN. GPC/Predictive World Model (RA-L 2025): inference-time look-ahead with separately trained world model. Inference-time scaling (ICLR 2025): noise trajectory search for better samples — general quality, not robustness-specific. FK steering (ICLR 2026): reward-guided inference-time steering — requires defining an appropriate reward. TTPL (April 2026): test-time perturbation learning with delayed feedback for VLAs — requires online learning from environment feedback during deployment, +7.4% on LIBERO. **SVD/spectral methods in diffusion models:** DiffStateGrad (ICLR 2025): SVD projection for image inverse problems. Mechanistic cross-attention subspace analysis (AAAI 2025): concept-encoding subspaces. Score Augmentation [ScoreAug] (2025): equivariant training augmentation in score space. CPC theory (NeurIPS 2025): CFG implicit decomposition into selective amplification. All single-modal image settings. **Training-free geometric augmentation for robot policies:** Data augmentation at training time is standard; test-time augmentation for classification is standard; but TEST-TIME SCORE-SPACE FILTERING using geometric sensitivity analysis has NOT been proposed for diffusion-based robot policies. **Gap:** No existing work (1) provides a purely inference-time, architecture-agnostic method for geometric robustness of pre-trained diffusion/flow policies, (2) uses geometric sensitivity analysis of the score function to identify and suppress unreliable components, or (3) evaluates such a method on LIBERO-Plus geometric perturbations. GSF fills all three gaps simultaneously.",
  "approach": "We propose Geometric Sensitivity Filtering (GSF), a training-free inference-time method that improves geometric robustness of ANY pre-trained diffusion/flow-based robot policy by projecting action scores onto geometrically-stable subspaces identified through local sensitivity analysis.\n\n**Core Mechanism.** At each denoising/integration step t during inference:\n1. Given current observation o and noisy action a_t, compute the nominal score: s_0 = s_θ(a_t, t | o)\n2. Generate K=4 small geometric augmentations of the observation: {T_k(o)} where T_k are random camera jitter (±3° rotation, ±5% translation) or spatial crops\n3. Compute augmented scores: s_k = s_θ(a_t, t | T_k(o)) for k=1,...,K\n4. Compute score covariance across augmentations: C_t = (1/K) Σ_k (s_k - s̄)(s_k - s̄)^T where s̄ is the mean\n5. SVD of C_t = U_t Λ_t U_t^T. The TOP eigenvectors (high eigenvalues) correspond to score directions with HIGH geometric sensitivity — these are the unreliable components under geometric perturbation\n6. Construct projection: Π_t = I - Σ_{i: λ_i > τ·λ_max} u_i u_i^T (suppress top-sensitivity directions)\n7. Apply filtered score: s_filtered = Π_t · s_0\n8. Use s_filtered for the denoising/integration step\n\n**Theoretical Motivation.** Under the training distribution, ALL score components are reliable — the policy has seen similar observations. Under geometric perturbation (OOD camera/robot-init), the observation shifts from the training manifold. Score components encoding viewpoint-specific spatial features (e.g., pixel-coordinate-dependent reaching directions) become unreliable because they were learned for a specific viewpoint. Score components encoding viewpoint-invariant semantics (e.g., object identity, grasp type, task phase) remain reliable because they generalize across viewpoints. GSF identifies the unreliable components through their HIGH SENSITIVITY to small geometric perturbations (if a small camera jitter changes the score dramatically in direction u_i, that direction encodes viewpoint-specific information). This is analogous to how DiffStateGrad projects gradients onto low-rank state subspaces, but our filtering criterion is GEOMETRIC SENSITIVITY rather than state-space rank, and our domain is cross-modal robot control rather than image restoration.\n\n**Adaptive Filtering Schedule.** Not all denoising steps are equally sensitive to geometry. Early steps (high noise) determine coarse trajectory structure and are most geometry-dependent; later steps refine timing and precision. We apply GSF with adaptive strength: strong filtering (lower τ, suppress more) at early steps, weak filtering (higher τ, suppress less) at later steps. This follows the β-CFG principle of timestep-adaptive guidance.\n\n**Computational Overhead.** GSF requires K+1 forward passes per denoising step (1 nominal + K augmented). For K=4 and T=10 denoising steps, this is 50 vs. 10 forward passes — 5x overhead. Three optimizations reduce this: (i) Apply GSF only at the first M=3-4 denoising steps where geometry matters most (reducing to 10 + 12-16 = 22-26 passes, ~2.5x overhead). (ii) Cache visual backbone features for augmented views across denoising steps (augmentations are applied to the observation, which doesn't change across steps). (iii) For flow-matching policies with few integration steps (OA-WAM uses 4 steps), the overhead is minimal.\n\n**Backbone Strategy.** Primary: Fast-WAM (97.6% standard LIBERO, released code + checkpoints on HuggingFace, diffusion action head, real-time inference). Fast-WAM's architecture (MoT with video DiT backbone + action expert DiT) is representative of modern WAMs. Secondary: Standard Diffusion Policy (original Chi et al., widely used baseline, released code). Extension: OA-WAM checkpoint if available — demonstrating that GSF provides ADDITIONAL improvement on top of an already-robust architecture would be the strongest possible result, showing complementarity with training-time approaches.\n\n**Evaluation Strategy.** Primary benchmark: LIBERO-Plus geometric perturbations — Camera (L1, L3 difficulty) and Robot-Init (L1, L3), plus Light as control condition (non-geometric, expect no benefit). Standard LIBERO as sanity check (expect slight degradation from information loss, confirming the semantic/spatial decomposition). Baselines: (i) Fast-WAM standard inference, (ii) Fast-WAM + uniform test-time augmentation (TTA — average action PREDICTIONS from augmented views, the naive approach), (iii) Fast-WAM + score-space mean (average scores then denoise — GPC-style composition), (iv) Fast-WAM + GSF (ours). Ablations: (a) filtering threshold τ sensitivity, (b) number of augmentations K ∈ {2, 4, 8}, (c) augmentation type (camera jitter vs. spatial crop vs. both), (d) adaptive vs. uniform filtering schedule, (e) which denoising steps to apply GSF (early-only vs. all), (f) cross-task consistency of sensitive subspaces (do the same directions show high sensitivity across different tasks?). Framing vs. competitors: GSF is training-free and architecture-agnostic, complementary to OA-WAM/CKT-WAM/SDP. We explicitly frame it as the test-time counterpart of training-time equivariant methods: SDP builds geometric invariance into the architecture; GSF enforces approximate geometric stability at inference via score filtering.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~80-110h H100",
      "gpu_utilization": "Moderate (35-45%). Human sets up Fast-WAM + LIBERO-Plus integration, implements GSF pipeline (SVD of score covariance, augmentation generation, projection), runs evaluation sweeps.",
      "timeline": "2-2.5 weeks (feasible for CoRL abstract May 26, paper May 29)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$200-330 (at ~$2.50-3.00/H100-hr spot pricing)"
    },
    "human_in_loop": {
      "gpu_hours": "~90-130h H100",
      "gpu_utilization": "Moderate-high (55-70%). Agent implements GSF on Fast-WAM, integrates LIBERO-Plus evaluation, runs systematic sweeps. Human reviews intermediate results (~30min/day).",
      "timeline": "12-16 days (targets CoRL 2026 abstract May 26, paper May 29)",
      "team": "1 researcher, ~30min/day",
      "claude_api_cost": "$80-200 (estimated ~800-2000 Opus turns)",
      "estimated_gpu_cost": "$225-390",
      "risk_note": "Primary risk is GSF's filtering being too aggressive (removing task-relevant spatial info) or too weak (not suppressing enough noise). The threshold τ sweep mitigates this — even if the best τ varies per task, demonstrating the principle on any subset of tasks is sufficient."
    },
    "auto_research": {
      "gpu_hours": "~110-170h H100",
      "gpu_utilization": "High (>80%). Agent runs continuous augmentation-type sweep → threshold sweep → evaluation loop.",
      "timeline": "9-13 days with 2-4 GPUs concurrently",
      "team": "0 (initial setup only, ~1.5 hours)",
      "claude_api_cost": "$150-350 (estimated ~1500-3500 Opus turns)",
      "estimated_gpu_cost": "$275-510",
      "speed_bottleneck": "The main computational cost is K+1 forward passes per denoising step during evaluation. With 10 LIBERO-Plus tasks × 20 episodes × 150 steps × 5 threshold values = 150K policy calls per condition. At ~200ms per call on H100, each condition takes ~8h. 4 conditions (Camera L1/L3, Robot L1/L3) + standard LIBERO = ~40-50h for the full sweep.",
      "risk_note": "Unlike the original Phase 1 contingency, GSF either helps or doesn't — no fundamental architectural blocker. If filtering threshold is optimized per-task, the practical value still holds since calibration requires only 5-10 episodes."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract May 26, paper May 29 — PRIMARY TARGET; 16-19 days; no Phase 1 gate means direct method development and evaluation; Fast-WAM checkpoint availability eliminates setup risk)",
    "AAAI 2027 (deadline Aug 2, 2026 — secondary target; allows extension to OA-WAM backbone, multi-policy composition, deeper analysis of which score components encode what)",
    "ICLR 2027 (deadline Sep 24, 2026 — fallback; allows comprehensive multi-backbone study across Fast-WAM, Diffusion Policy, OA-WAM, and VLAs, plus theoretical analysis connecting GSF to equivariance theory)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv March 2026) — PRIMARY BACKBONE; 97.6% standard LIBERO, released code + checkpoints, MoT architecture with video DiT backbone + action expert DiT; provides strong standard performance baseline for measuring GSF's robustness improvement",
    "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv May 2026) — LIBERO-Plus Camera SOTA at 80.5%, Robot 89.6%; flow-matching action head with 4-step Euler; requires 7B architectural redesign; GSF is complementary (training-free, can potentially be applied on top)",
    "CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models (arXiv May 2026) — LIBERO-Plus total SOTA at 86.1%; requires additional fine-tuning; GSF is complementary",
    "SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space [SDP] (ICML 2025) — training-time equivariant architecture for geometric generalization; GSF is the TEST-TIME counterpart — achieves approximate geometric stability without requiring equivariant architecture or retraining",
    "Diffusion State-Guided Projected Gradient for Inverse Problems [DiffStateGrad] (ICLR 2025) — SVD-based subspace projection in diffusion models; key methodological predecessor; our contribution: replace state-defined projection with GEOMETRIC SENSITIVITY-defined projection, extend from image restoration to robot policy robustness",
    "Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition [GPC] (ICLR 2026) — test-time score composition from multiple policies; proves convex score combination yields superior objectives; our distinction: same policy with geometric augmentations (not multiple policies), targeting robustness (not general quality)",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (arXiv 2025) — 7-dimension perturbation benchmark establishing geometric perturbation as dominant failure mode (drops from 95% to <30%)",
    "Do World Action Models Generalize Better than VLAs? A Robustness Study (arXiv March 2026) — WAMs weak on geometric perturbations; motivates the robustness focus",
    "Towards Understanding the Mechanisms of Classifier-Free Guidance [CPC Theory] (NeurIPS 2025) — theoretical grounding for when selective amplification/suppression of score components improves generation quality; applies to our sensitivity-based suppression",
    "ADPro: Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising (2025) — related training-free inference-time approach; requires point cloud observations and task-geometric knowledge; evaluated on RLBench/CALVIN only; GSF is observation-modality-agnostic and requires no geometric knowledge",
    "Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps (ICLR 2025) — establishes paradigm of spending additional inference compute for better diffusion samples; GSF is an instance of this paradigm applied specifically to geometric robustness",
    "A General Framework for Inference-time Scaling and Steering of Diffusion Models [FK Steering] (ICLR 2026) — Feynman-Kac guided inference with arbitrary rewards; related but requires explicit reward function; GSF uses implicit geometric sensitivity as the signal",
    "Test-Time Perturbation Learning with Delayed Feedback for VLA Models [TTPL] (arXiv April 2026) — test-time adaptation with online feedback; requires environment interaction during deployment; GSF requires no online learning or feedback",
    "Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv May 2026) — LIBERO-Plus 82.1% zero-shot / 84.8% fine-tuned",
    "AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust VLA Models (arXiv March 2026) — training-free camera adaptation via novel view synthesis; requires known camera parameters; VLA-specific, camera-perturbation-only",
    "Score Augmentation for Diffusion Models [ScoreAug] (arXiv 2025) — equivariant training augmentation in score space; demonstrates that geometric transformations of noisy data establish equivariant learning objectives; training-time complement to our test-time approach",
    "EquiBot: SIM(3)-Equivariant Diffusion Policy for Generalizable Learning (2024) — training-time equivariant architecture; related goal (geometric generalization) but fundamentally different mechanism (architectural vs. inference-time)",
    "Classifier-free Guidance with Adaptive Scaling [β-CFG] (arXiv Feb 2025) — timestep-adaptive guidance scheduling; informs our adaptive filtering schedule",
    "Classifier-Free Diffusion Guidance (NeurIPS 2021 Workshop) — foundational technique; GSF's augmentation-based filtering is related to guidance (both modify the score) but uses sensitivity analysis rather than conditional/unconditional decomposition",
    "X-WAM: Unified 4D World Action Modeling with Asynchronous Denoising (arXiv April 2026) — alternative WAM architecture with coupled timestep sampling; critiques independent timestep mechanisms; GSF avoids timestep-mechanism dependency entirely",
    "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (RSS 2023) — foundational diffusion policy; secondary backbone candidate for demonstrating architecture-agnosticism",
    "Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling [GPC-WM] (RA-L 2025) — inference-time enhancement via separately trained world model; requires additional model; GSF uses only the policy itself",
    "When to Trust Imagination: Adaptive Action Execution for World Action Models [FFDC] (arXiv May 2026) — confidence-based replanning; orthogonal to GSF (decides WHEN to act; GSF improves HOW the score is computed)"
  ],
  "description": "We propose Geometric Sensitivity Filtering (GSF), a training-free inference-time method that improves geometric robustness of ANY pre-trained diffusion/flow-based robot policy by projecting action scores onto geometrically-stable subspaces. The key insight: under geometric perturbation (camera viewpoint change, robot initial state change), certain components of the policy's score function become unreliable because they encode viewpoint-specific spatial features, while components encoding task semantics remain reliable. GSF identifies unreliable components through their HIGH SENSITIVITY to small geometric augmentations at test time: at each denoising step, we compute scores from K=4 small geometric perturbations of the observation, perform SVD on the score covariance to find high-sensitivity directions, and project the nominal score onto the complementary (low-sensitivity) subspace before continuing denoising. This is the test-time counterpart of SE(3)-equivariant architectures (SDP/ICML 2025, EquiBot): where they build geometric invariance into training, GSF enforces approximate geometric stability at inference via score subspace projection. Unlike all existing geometric robustness methods — OA-WAM (Camera 80.5%, requires 7B architectural redesign), CKT-WAM (total 86.1%, requires fine-tuning), SDP (requires equivariant architecture) — GSF is training-free, architecture-agnostic, and can be applied to any pre-trained diffusion/flow policy including potentially on TOP of these methods for additional improvement. The method extends DiffStateGrad's SVD-based projection from single-modal image restoration to robot policy robustness, with the key innovation being geometric sensitivity as the projection criterion (rather than state-space rank). Evaluated on LIBERO-Plus geometric perturbations (Camera, Robot-Init at L1/L3 difficulty) using Fast-WAM (97.6% standard LIBERO) as primary backbone. Computational overhead is ~2.5x (applying GSF at early denoising steps only with cached visual features), comparable to standard classifier-free guidance. Ablations include filtering threshold, augmentation type/count, adaptive scheduling, and cross-task consistency of sensitive subspaces. The method is positioned as complementary to training-time approaches: spending modest additional inference compute to achieve geometric robustness that would otherwise require architectural redesign or retraining.",
  "project_name": "geometric_sensitivity_filtering_diffusion_policy",
  "source": "web_research"
}

## Reviewer feedback (round 7)
Issues: ["FAST-WAM HAS NO LIBERO-PLUS BASELINE (CRITICAL): After exhaustive search — the Fast-WAM paper, OA-WAM's Table 2 (which compares 16 baselines), the WAM robustness study (arXiv 2603.22078, which evaluates Cosmos-Policy/GE-Act/VLA-JEPA but NOT Fast-WAM) — Fast-WAM has never been evaluated on LIBERO-Plus. The proposal assumes Fast-WAM's LIBERO-Plus performance will show meaningful degradation under geometric perturbation, but this is unverified. If Fast-WAM somehow maintains >85% on camera perturbation (unlikely but possible given its strong 97.6% standard performance), the room for GSF improvement is small. Conversely, if it drops to <40% (possible given LIBERO-Plus findings of 95%→<30% drops), GSF would need enormous improvement to reach competitive absolute numbers. This baseline MUST be established in the first 2-3 days before committing to the full plan.", "CORE ASSUMPTION IS UNTESTED AND MAY BE WRONG: GSF assumes that SVD of the score covariance under small geometric augmentations (±3° rotation, ±5% translation) cleanly separates 'viewpoint-specific spatial features' (high eigenvalues) from 'viewpoint-invariant semantics' (low eigenvalues). This decomposition is a hypothesis, not a fact. In robot manipulation, spatial precision IS the task — reaching, grasping, and placing all depend on precise spatial features. Suppressing the 'high sensitivity' directions may suppress exactly the task-relevant spatial information needed for successful manipulation. The proposal acknowledges 'modest precision loss' but provides no evidence this trade-off is favorable. Furthermore, the augmentation magnitude (±3°) is much smaller than LIBERO-Plus camera perturbations — the first-order sensitivity at the nominal observation may not predict which score directions fail under large perturbations.", "TERMINOLOGY ERROR: FAST-WAM USES FLOW-MATCHING, NOT DIFFUSION: Fast-WAM explicitly uses flow matching ('trained to predict the corresponding velocity field with a standard flow matching objective') with 10 integration steps. The proposal consistently refers to 'action scores' and 'score function' but the correct term is 'velocity field.' While the SVD filtering mechanism applies identically to velocity vectors, the terminology throughout the proposal is technically incorrect and will raise reviewer concerns about the authors' understanding of the backbone model. Replace all 'score' references with 'velocity field' when discussing Fast-WAM.", "OA-WAM GEO-AVG DISCREPANCY: The proposal claims OA-WAM's 'Geo-Avg 84.3%' but the OA-WAM paper's own summary states 'Geo-Avg 76.0' which is defined as mean of Camera/Robot/Layout geometric axes. The 84.3% appears to be (Camera 80.5 + Robot 89.6) / 2 without Layout. This discrepancy must be corrected — using the wrong number inflates the apparent target and misrepresents the competitive landscape.", "MISSING RELATED WORK — DREAMING THE UNSEEN (DDP, March 2026): 'Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness' (arXiv 2603.21017) addresses OOD robustness of diffusion policies by coupling with a predictive world model. Achieves 73.8% OOD success on MetaWorld and 83.3% under severe real-world spatial shifts. While DDP is a training-time method, it directly addresses geometric robustness of diffusion policies and must be cited. Also missing: Visual-Geometry Diffusion Policy (VGDP, Nov 2025) which achieves 15.2% improvement in spatial perturbation settings via complementarity-aware multimodal fusion.", "GSF VS. SIMPLE TTA — THE MAKE-OR-BREAK COMPARISON: The proposal includes 'Fast-WAM + uniform TTA (average action predictions from augmented views)' as a baseline. This is the critical comparison. If simple prediction averaging from augmented views (which requires the same K+1 forward passes) achieves similar improvement to GSF's SVD-based filtering, then the entire SVD/covariance/projection mechanism adds complexity without benefit. The theoretical argument for why SVD-based filtering should outperform simple averaging is missing. In the image domain, test-time augmentation ensembles are strong baselines — GSF must clearly beat this.", "COMPARISON AGAINST TTPL (April 2026) IS COMPLICATED: TTPL achieves +7.4% on LIBERO via test-time perturbation learning with delayed feedback. TTPL is also training-free at inference (no fine-tuning needed) and uses augmentation-based uncertainty estimation + action voting — conceptually related to GSF's augmentation-based sensitivity analysis. TTPL's augmentation + voting mechanism is simpler than GSF's SVD filtering. If TTPL's simpler approach achieves larger gains, GSF's complexity is hard to justify. The proposal should compare against TTPL or explicitly differentiate (TTPL requires environment feedback during deployment; GSF does not)."]
Feedback: The pivot from SCG to GSF is a substantial improvement — the mechanism is cleaner, the backbone dependency is resolved, and the architecture-agnostic claim is better justified. But three critical issues must be addressed before this is CoRL-ready:

**1. ESTABLISH FAST-WAM LIBERO-PLUS BASELINE IMMEDIATELY (Days 1-3):** This is the single most important unknown. Set up LIBERO-Plus perturbation pipeline with Fast-WAM's released checkpoint. Run Camera L1/L3 and Robot-Init L1/L3 with 20 episodes each — ~10-15h H100, 2-3 days. This tells you: (a) how much Fast-WAM degrades under geometric perturbation (the ceiling for GSF improvement), (b) whether the degradation pattern is consistent with the viewpoint-specific-spatial-feature hypothesis, and (c) whether the absolute numbers are competitive enough to be meaningful alongside OA-WAM's results.

**2. ADD A SIMPLE TTA BASELINE AND THEORETICAL ARGUMENT FOR WHY SVD FILTERING IS BETTER:** The key question is not 'does augmentation help?' but 'does SVD-based filtering help MORE than simple averaging?' Include this baseline: compute K augmented velocity fields and average them directly (no SVD), then denoise with the averaged field. If this achieves similar improvement to GSF, the SVD mechanism is unnecessary. Provide a clear argument for when/why SVD filtering outperforms averaging — hypothesis: averaging retains all directions equally, including high-sensitivity directions where the augmented predictions disagree (noise), while GSF suppresses these noisy directions. This is testable and, if confirmed, is the core technical insight.

**3. FIX TERMINOLOGY AND NUMBERS:** (a) Replace 'score' with 'velocity field' throughout when discussing Fast-WAM/flow-matching policies. GSF works on both diffusion scores and flow-matching velocity fields — make this explicit. (b) Correct OA-WAM Geo-Avg to 76.0 (mean of Camera/Robot/Layout) rather than 84.3 (appears to be Camera+Robot only). (c) Cite DDP (arXiv 2603.21017) and VGDP (arXiv 2511.22445) as related work.

**4. CONSIDER A PHASE-0 DIAGNOSTIC:** Before implementing full GSF, run a quick diagnostic: for a few LIBERO-Plus camera-perturbed episodes, compute velocity fields from 4-8 small augmentations and visualize the eigenvalue spectrum of the covariance matrix. If the spectrum is flat (all eigenvalues similar), there's no low-rank structure to exploit and GSF will fail. If there's a clear spectral gap (top 2-3 eigenvalues dominate), GSF has a chance. This takes ~2h of compute and 1 day of analysis, and prevents committing 2 weeks to an approach that has no structural basis.

**5. FRAME CONTRIBUTION CAREFULLY:** Don't claim GSF is 'the test-time counterpart of SE(3)-equivariant methods.' SE(3)-equivariant methods achieve exact mathematical equivariance by architectural design. GSF achieves approximate geometric stability via heuristic sensitivity-based filtering. The gap is enormous. Instead, frame GSF as: 'a lightweight inference-time method for improving geometric robustness of pre-trained policies, complementary to training-time equivariant approaches, requiring only K+1 forward passes and no architectural modification.'

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
这个 idea 已经经过 7 轮修订，近 3 轮的平均分从 3.2 到 3.4，没有明显改善。

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
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "type": "user",
  "uuid": "96f71436-9bf5-4f37-be5a-8ec5ee1a0e33",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T20:17:29.730Z_

```json
{
  "parentUuid": "96f71436-9bf5-4f37-be5a-8ec5ee1a0e33",
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
  "uuid": "294de369-18fa-4d62-a8ee-e219b8f66b92",
  "timestamp": "2026-05-10T20:17:29.730Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T20:17:29.730Z_

```json
{
  "parentUuid": "294de369-18fa-4d62-a8ee-e219b8f66b92",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "03277415-1fd9-4784-bbc8-ac2f38c1bcbb",
  "timestamp": "2026-05-10T20:17:29.730Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Geometric Sensitivity Filtering: Training-Free Score Subspace Projecti…",
  "leafUuid": "03277415-1fd9-4784-bbc8-ac2f38c1bcbb",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate Fast-WAM LIBERO-Plus baseline before committing to GSF",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52"
}
```

---

### Assistant

_source line 8 · 2026-05-10T20:18:52.745Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the reviewer feedback and the current state of this research idea. The idea has gone through 7 rounds of revision with stagnating scores (3.2 to 3.4). Let me think deeply about whether this needs a minor fix, major revision, or pivot.

**Core Issues from Reviewer:**

1. **Fast-WAM has no LIBERO-Plus baseline** - This is critical. The entire proposal assumes Fast-WAM degrades under geometric perturbation, but this hasn't been verified.

2. **Core assumption untested** - SVD decomposition may not cleanly separate viewpoint-specific from viewpoint-invariant features. 

3. **Terminology error** - Fast-WAM uses flow-matching, not diffusion. Should use "velocity field" not "score."

4. **OA-WAM number discrepancy** - 84.3% vs 76.0% Geo-Avg.

5. **Missing related work** - DDP and VGDP.

6. **GSF vs simple TTA** - The make-or-break comparison. If simple averaging works as well, SVD is unnecessary complexity.

7. **TTPL comparison** - Simpler approach may achieve more.

**Deep Thinking About Stagnation:**

The real problem is that GSF is fundamentally an inference-time technique, and I'm not adequately demonstrating why the SVD-based decomposition provides value over straightforward test-time augmentation approaches.

The reviewer's core critique cuts deep: in manipulation tasks, spatial precision is everything, so filtering out high-sensitivity directions could eliminate the exact capabilities we need. Combined with the fact that simple averaging of augmented predictions might perform equally well, the entire SVD mechanism starts looking like unnecessary overhead without a compelling theoretical justification.

I'm facing a choice between committing to a major revision that addresses all these issues or reconsidering the approach entirely. Seven iterations without meaningful progress, the questionable assumption that SVD cleanly separates spatial from semantic information in manipulation, and the possibility that basic test-time averaging is just as effective all point toward fundamental problems with the current direction.

But the underlying problem—making pre-trained diffusion and flow policies geometrically robust at test time in a training-free, architecture-agnostic way—remains genuinely important and underexplored. The real question is whether I can redesign this to avoid the SVD decomposition trap, or if I should pivot to something that doesn't rely on that flawed assumption.

Let me consider some alternative directions: instead of filtering velocity fields through SVD, I could use test-time geometric adaptation where a small correction is learned from the augmented views themselves. Or I could shift to a consensus-based approach where I measure agreement across augmented velocity fields and use that as a confidence signal—regions where all augmentations align are trustworthy, while disagreement flags areas that need different handling. A third option is adaptive test-time augmentation with geometric consistency scoring, where each augmented view is weighted by how well it aligns with the consensus, creating a softer version of TTA that naturally downweights outliers.

But stepping back, the reviewer's real question is why SVD filtering beats simple averaging. The answer is that averaging treats all dimensions equally, but augmented views agree in some dimensions (geometrically stable) and disagree in others (geometrically sensitive)—SVD identifies which is which. The problem is what to do with that information. GSF suppresses disagreement dimensions entirely, but zeroing out a velocity component might be worse than keeping a noisy one. A better strategy would be to trust the consensus where augmentations agree and use conservative actions where they disagree, rather than just eliminating those directions.

This leads me to a different approach: instead of suppression, use consensus across augmented views as the target in high-sensitivity directions while relying on the nominal prediction in stable directions. I'd compute the nominal velocity, generate augmented versions under different transformations, find the mean velocity, measure component-wise variance across dimensions, and then blend between the consensus and nominal predictions based on sensitivity levels.

But I'm realizing this is essentially a softer version of test-time augmentation with dimension-wise confidence weighting—which raises the question of whether it's novel enough. After multiple rounds of iteration, I'm starting to wonder if the core "inference-time geometric robustness" angle for diffusion policies is simply too incremental when simpler TTA approaches might work just as well, the improvement margins are unclear, and more principled training-time methods already exist. Maybe I need to step back and think about what would actually constitute a strong contribution here.

The real strength would be establishing that velocity field decomposition explains geometric robustness, empirically demonstrating that these fields have low-rank structure under perturbation, building a method around that structure, and showing it outperforms basic TTA. But the critical missing piece is whether that low-rank structure actually exists—the reviewer's suggestion to do a diagnostic phase first makes sense. Without that foundation, I'm just speculating.

I think the right move is a major revision that first establishes the Fast-WAM baseline properly, directly addresses the SVD filtering versus simple TTA tradeoff, and redesigns the mechanism to be more principled.

The core idea I want to keep is that geometric perturbations affect velocity field components differently, and we can leverage that asymmetry at test time. Instead of just suppressing high-sensitivity directions, I'm thinking about a Variance-Weighted Consensus approach where we adaptively weight each dimension based on whether augmentations agree or disagree—treating dimensions with consistent signal differently from those where augmentations introduce conflicting noise.

But I'm realizing this might actually invert GSF's logic: if augmentations disagree in a dimension, that suggests it's sensitive to the exact geometric transform, so the nominal observation might be most reliable there. Conversely, when augmentations agree, the consensus reinforces the signal. Now I need to think through what happens under actual geometric perturbation at test time—the observation is already shifted from the training distribution, so the nominal velocity computed from it could be systematically wrong in certain directions.

When I look at high variance under small augmentations, it tells me the velocity field changes rapidly with small geometric shifts in that direction, which means both the nominal prediction and any consensus are unreliable there. Simply suppressing these directions like GSF does feels too crude—I should instead consider using a prior based on the consensus magnitude with direction from majority voting, or some other approach to reduce rather than eliminate the signal.

The key insight is that low-variance directions have a stable velocity field I can trust, while high-variance directions are unstable and need a more conservative estimate. Simple TTA averages everything uniformly, which dilutes the precision in stable dimensions where the nominal prediction is actually best. A smarter approach would preserve the nominal estimate's precision in stable directions while falling back to consensus in unstable ones.

I can formalize this as a variance-weighted interpolation that blends the nominal and consensus predictions based on per-dimension variance—when variance is low, I use the nominal; when it's high, I shift toward consensus. This beats both approaches: it's more robust than nominal-only since it uses consensus where needed, and more precise than simple TTA since it doesn't dilute the signal in reliable dimensions.

Now I'm wondering if this is actually novel or if it's just a reframing of something that already exists...

it's related to Bayesian model averaging and ensemble methods with confidence weighting, but the specific angle here is applying it to velocity fields in flow-matching policies and using local geometric sensitivity as the weighting criterion. The real contribution might not be the method itself, but rather the empirical insight that pre-trained flow policies have non-uniform geometric sensitivity across action dimensions—that's the diagnostic finding that makes everything else make sense.

If I can demonstrate that this sensitivity structure is real, that it corresponds to meaningful decompositions in the action space, and that exploiting it improves robustness, then the paper becomes about understanding why geometric perturbations break these policies and how to fix it at test time. That's a stronger story than just proposing a filtering technique.

Now I need to track down those specific papers the reviewer mentioned and verify the claims before diving into the revision.

The reframing should shift focus from the SVD filtering itself toward understanding the geometric sensitivity structure of velocity fields, then use that insight to motivate a simpler, more empirically grounded method. I'll restructure to lead with the diagnostic finding, redesign the mechanism around variance-weighted consensus instead of SVD projection, and make sure to include the Phase-0 gate and Fast-WAM baseline as explicit starting points. There's also a lot of terminology and reference cleanup needed throughout.

Now I'm searching for relevant work on test-time augmentation, robot policy robustness, and related methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03277415-1fd9-4784-bbc8-ac2f38c1bcbb",
  "isSidechain": false,
  "requestId": "req_011CauWF69JSEGMg2ujs8zYZ",
  "type": "assistant",
  "uuid": "f2088c93-21f9-4bc9-baa9-f7f56d7ba8e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRMBYSgRhYhNvbhEpwuefV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14575,
      "cache_read_input_tokens": 11804,
      "output_tokens": 4692,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14575,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4692,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 14575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14575
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

_source line 9 · 2026-05-10T20:18:52.748Z_

I'll research the reviewer's specific concerns before revising. Let me search for the missing related work, verify claims, and investigate the core feasibility questions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2088c93-21f9-4bc9-baa9-f7f56d7ba8e9",
  "isSidechain": false,
  "requestId": "req_011CauWF69JSEGMg2ujs8zYZ",
  "type": "assistant",
  "uuid": "69abb104-48e8-47d9-b849-f40c9dceff58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRMBYSgRhYhNvbhEpwuefV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14575,
      "cache_read_input_tokens": 11804,
      "output_tokens": 4692,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14575,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4692,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 14575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14575
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

_source line 10 · 2026-05-10T20:18:59.209Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GUjPZZeKCRbTS1FUkFtLRG`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search DDP and VGDP papers",
  "prompt": "I need to find and read two specific papers that a reviewer flagged as missing related work:\n\n1. \"Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness\" (DDP) - arXiv 2603.21017 (March 2026). Claims to achieve 73.8% OOD success on MetaWorld and 83.3% under severe real-world spatial shifts.\n\n2. \"Visual-Geometry Diffusion Policy\" (VGDP) - arXiv 2511.22445 (November 2025). Claims 15.2% improvement in spatial perturbation settings via complementarity-aware multimodal fusion.\n\nFor each paper, please:\n- Use WebSearch to find it\n- Use WebFetch to read the abstract and method description\n- Report: what problem they solve, their approach, key results, and how they relate to \"test-time inference methods for geometric robustness of diffusion policies\"\n\nAlso search for: \"test-time augmentation diffusion policy robot\" and \"velocity field flow matching robot manipulation robustness\" to find any other recent related work I might be missing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69abb104-48e8-47d9-b849-f40c9dceff58",
  "isSidechain": false,
  "requestId": "req_011CauWF69JSEGMg2ujs8zYZ",
  "type": "assistant",
  "uuid": "1cb6a58d-2aac-4907-bbcd-63899323b8c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRMBYSgRhYhNvbhEpwuefV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14575,
      "cache_read_input_tokens": 11804,
      "output_tokens": 4692,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14575,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4692,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 14575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14575
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

_source line 11 · 2026-05-10T20:19:06.224Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016qE4Eqdn32SodwrqSqjN9u`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search TTPL and TTA baselines",
  "prompt": "I need to research two things for a paper revision:\n\n1. **TTPL (Test-Time Perturbation Learning with Delayed Feedback for VLA Models)** - arXiv April 2026. Claims +7.4% on LIBERO via test-time perturbation learning with delayed feedback. I need to understand:\n   - What is their exact mechanism? (augmentation + voting? uncertainty estimation?)\n   - Do they require environment feedback during deployment?\n   - How does their approach compare to simply averaging predictions from augmented views?\n   - Search for \"TTPL test-time perturbation learning VLA\" and fetch the paper.\n\n2. **Test-time augmentation (TTA) for robot manipulation policies** - I need to understand what simple TTA baselines exist:\n   - Search \"test-time augmentation robot policy manipulation\"\n   - Search \"ensemble augmentation inference robot learning diffusion\"\n   - What's the state of the art for simple prediction averaging from augmented views?\n   - Has anyone compared TTA to more sophisticated filtering methods for robot policies?\n\n3. **Fast-WAM architecture details** - Search for \"Fast-WAM world action model\" and verify:\n   - Does it use flow-matching (velocity field) or diffusion (score)?\n   - How many integration steps?\n   - Is the code/checkpoint actually released on HuggingFace?\n   - Has it been evaluated on LIBERO-Plus anywhere?\n\nReport findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cb6a58d-2aac-4907-bbcd-63899323b8c5",
  "isSidechain": false,
  "requestId": "req_011CauWF69JSEGMg2ujs8zYZ",
  "type": "assistant",
  "uuid": "0d1b0641-3257-4a15-b731-8346ec3ceff1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRMBYSgRhYhNvbhEpwuefV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14575,
      "cache_read_input_tokens": 11804,
      "output_tokens": 4692,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14575,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4692,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 14575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14575
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

_source line 12 · 2026-05-10T20:19:14.391Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HGXLtVhXyTTMZSkorx2ZHP`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search SVD velocity field structure",
  "prompt": "I'm investigating whether the core assumption of a research idea holds: that velocity fields of flow-matching robot policies have non-uniform geometric sensitivity that can be decomposed via SVD.\n\nPlease search for:\n\n1. \"spectral analysis velocity field diffusion model\" - any work analyzing the spectral/eigenvalue structure of score functions or velocity fields in diffusion/flow models\n\n2. \"low-rank structure diffusion model score\" - whether score functions/velocity fields have been shown to have low-rank structure\n\n3. \"DiffStateGrad SVD diffusion\" - the ICLR 2025 paper on SVD-based projection for diffusion models. Fetch its abstract and understand what structural assumptions it makes about scores.\n\n4. \"geometric robustness test-time inference diffusion\" - any recent work on test-time methods for geometric robustness\n\n5. \"variance weighted ensemble prediction robot\" - whether variance-weighted ensembling has been applied to robot policy predictions\n\n6. Also search for \"OA-WAM LIBERO-Plus\" and verify what the actual Geo-Avg number is (reviewer says 76.0, proposal says 84.3)\n\nReport all findings. I'm particularly interested in:\n- Whether velocity fields are known to have low-rank sensitivity structure\n- Whether simple variance-weighted ensembling has been proposed for robot policies\n- What the actual OA-WAM numbers are on LIBERO-Plus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d1b0641-3257-4a15-b731-8346ec3ceff1",
  "isSidechain": false,
  "requestId": "req_011CauWF69JSEGMg2ujs8zYZ",
  "type": "assistant",
  "uuid": "1faab6e0-32b1-48e4-9b9f-eb6da9f17b38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRMBYSgRhYhNvbhEpwuefV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14575,
      "cache_read_input_tokens": 11804,
      "output_tokens": 4692,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14575,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4692,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 14575,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14575
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Geometric Sensitivity Filtering: Training-Free Score Subspace Projecti…",
  "leafUuid": "1faab6e0-32b1-48e4-9b9f-eb6da9f17b38",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate Fast-WAM LIBERO-Plus baseline before committing to GSF",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52"
}
```

---

### Tool result

_source line 15 · 2026-05-10T20:21:02.812Z_

<details><summary>↩ Tool result · `toolu_01GUjPZZeKCRbTS1FUkFtLRG`</summary>

```text
I now have comprehensive information on both flagged papers and additional related work. Here is my full report:

---

## Paper 1: "Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness" (DDP)

**arXiv 2603.21017, March 2026**

**Problem:** Diffusion policies for visuomotor control fail catastrophically under severe OOD disturbances such as unexpected object displacements or visual corruptions during deployment.

**Approach:** DDP deeply integrates a diffusion world model into the policy via a shared 3D visual encoder, co-optimizing behavior cloning and world model objectives (L_total = L_BC + lambda * L_WM). At inference time, it implements a three-stage OOD response:
1. **Detection** - monitors "real-imagination discrepancy" (latent distance between actual observations and predicted states)
2. **Imagination** - when OOD is detected, abandons the corrupted visual stream and generates actions conditioned on autoregressively forecasted latent dynamics
3. **Recovery** - applies compensatory spatial corrections via pose estimation once the displaced object settles

**Key Results:**
- 73.8% OOD success on MetaWorld (vs. 23.9% baseline with tracking)
- 83.3% success under real-world spatial shifts (vs. 3.3% baseline)
- 76.7% real-world success in open-loop imagination (no visual feedback post-initialization)

**Relation to test-time geometric robustness of diffusion policies:** DDP is directly relevant as it uses a *test-time inference mechanism* (switching to imagined latent states) to handle geometric/spatial perturbations. However, it requires training a world model jointly with the policy -- it is not a pure test-time method. The spatial correction is computed as a static displacement offset rather than a continuous geometric transformation.

---

## Paper 2: "Visual-Geometry Diffusion Policy" (VGDP)

**arXiv 2511.22445, November 2025**

**Problem:** Visuomotor policies relying on single-modality inputs (RGB alone or point clouds alone) fail to generalize under visual and spatial perturbations.

**Approach:** VGDP introduces a Complementarity-Aware Fusion Module combining RGB (ResNet-18, 512-dim) and point cloud (DP3, 64-dim) features:
- Features project into a shared 256-dimensional space
- **Modality dropout** (p=0.2) randomly disables entire RGB or 3D branches during training, forcing modality-invariant representations
- Bidirectional cross-attention with residual connections enables lightweight modality interaction
- A diffusion policy head denoises actions conditioned on the fused representation

**Key Results:**
- 39.1% average improvement over 7 baselines (18 sim + 4 real tasks)
- 15.2% improvement under spatial perturbations
- 41.5% improvement under visual condition changes
- 11x stability improvement (variance 2.53% vs. 32.72% for competitors)
- 55.3% higher mean success under severe randomization

**Relation to test-time geometric robustness:** VGDP achieves spatial robustness through *training-time architectural design* (multimodal fusion + modality dropout) rather than test-time inference modifications. It demonstrates that point cloud geometry provides complementary spatial information that compensates for RGB failures under geometric shifts. This is a representational/training approach rather than a test-time inference method.

---

## Additional Related Work Discovered

### SE(3)-Equivariant Approaches (highly relevant to geometric robustness)

**EquiForm** (arXiv 2601.17486, January 2026): Noise-robust SE(3)-equivariant policy learning from 3D point clouds. Uses a geometric denoising module + equivariant contrastive learning to maintain SE(3) structure under realistic sensor noise. Achieves 17.2% improvement in sim, 28.1% in real-world. Directly addresses the breakdown of equivariance guarantees under noisy conditions.

**ReSeFlow** (arXiv 2509.22695, September 2025): Rectified SE(3)-equivariant flow matching. Replaces iterative diffusion denoising with straight geodesic-like paths in SE(3) space, enabling single-step inference. Up to 48.5% error reduction. Combines geometric invariance with flow-based efficiency.

**Spherical Diffusion Policy (SDP)** (arXiv 2507.01723): SE(3)-equivariant diffusion policy operating in spherical Fourier space, adapting trajectories according to 3D scene transformations.

### Flow Matching Approaches

**FlowPolicy** (AAAI 2025 Oral, arXiv 2412.04987): Consistency flow matching for single-step policy generation with 7x inference speedup. Uses 3D point clouds but does not explicitly address spatial robustness.

**Flow Matching Policy Gradients (FPO)** (ICLR 2026): Policy gradient algorithm for optimizing flow-based generative models via conditional flow matching objective reframing.

### Test-Time Composition

**General Policy Composition (GPC)** (arXiv 2510.01068): Training-free test-time composition of diffusion/flow policy scores via convex combination. Does NOT specifically address geometric robustness but provides a framework for test-time policy enhancement without retraining.

---

## Summary of Relevance to "Test-Time Inference Methods for Geometric Robustness of Diffusion Policies"

| Paper | Training-time? | Test-time? | Geometric Focus? |
|-------|---------------|-----------|-----------------|
| DDP | Yes (world model co-training) | Yes (imagination at inference) | Yes (spatial displacement recovery) |
| VGDP | Yes (modality dropout/fusion) | No | Yes (point cloud + RGB fusion) |
| EquiForm | Yes (denoising + contrastive) | No | Yes (SE(3) under noise) |
| ReSeFlow | Yes (rectified flow) | Partially (single-step) | Yes (SE(3) equivariance) |
| GPC | No | Yes (score composition) | No |

**DDP is the most directly relevant** as it is the only paper combining both a test-time inference mechanism (switching to imagined states) with explicit geometric/spatial perturbation handling. **VGDP** is relevant as a training-time baseline showing what multimodal fusion can achieve for spatial robustness. The **SE(3)-equivariant line of work** (EquiForm, ReSeFlow, SDP) provides an orthogonal approach to geometric robustness through architectural symmetry constraints rather than test-time adaptation.

Sources:
- [DDP - Dreaming the Unseen](https://arxiv.org/html/2603.21017v1)
- [VGDP - Visual-Geometry Diffusion Policy](https://arxiv.org/abs/2511.22445)
- [GPC - Compose Your Policies](https://arxiv.org/abs/2510.01068)
- [FlowPolicy](https://arxiv.org/abs/2412.04987)
- [EquiForm](https://arxiv.org/html/2601.17486)
- [ReSeFlow](https://arxiv.org/html/2509.22695v1)
- [Spherical Diffusion Policy](https://arxiv.org/abs/2507.01723)
- [Flow Matching Policy Gradients (ICLR 2026)](https://openreview.net/pdf/376ea41422d8f63f58a4916b9a9783de90e8e461.pdf)

agentId: a2db14817da9e1d4a (use SendMessage with to: 'a2db14817da9e1d4a' to continue this agent)
&lt;usage>total_tokens: 23903
tool_uses: 14
duration_ms: 123596&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1cb6a58d-2aac-4907-bbcd-63899323b8c5",
  "isSidechain": false,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "type": "user",
  "uuid": "7f9163db-7b60-44c3-a6b8-82ea55de91a8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find and read two specific papers that a reviewer flagged as missing related work:\n\n1. \"Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness\" (DDP) - arXiv 2603.21017 (March 2026). Claims to achieve 73.8% OOD success on MetaWorld and 83.3% under severe real-world spatial shifts.\n\n2. \"Visual-Geometry Diffusion Policy\" (VGDP) - arXiv 2511.22445 (November 2025). Claims 15.2% improvement in spatial perturbation settings via complementarity-aware multimodal fusion.\n\nFor each paper, please:\n- Use WebSearch to find it\n- Use WebFetch to read the abstract and method description\n- Report: what problem they solve, their approach, key results, and how they relate to \"test-time inference methods for geometric robustness of diffusion policies\"\n\nAlso search for: \"test-time augmentation diffusion policy robot\" and \"velocity field flow matching robot manipulation robustness\" to find any other recent related work I might be missing.",
    "agentId": "a2db14817da9e1d4a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on both flagged papers and additional related work. Here is my full report:\n\n---\n\n## Paper 1: \"Dreaming the Unseen: World Model-regularized Diffusion Policy for Out-of-Distribution Robustness\" (DDP)\n\n**arXiv 2603.21017, March 2026**\n\n**Problem:** Diffusion policies for visuomotor control fail catastrophically under severe OOD disturbances such as unexpected object displacements or visual corruptions during deployment.\n\n**Approach:** DDP deeply integrates a diffusion world model into the policy via a shared 3D visual encoder, co-optimizing behavior cloning and world model objectives (L_total = L_BC + lambda * L_WM). At inference time, it implements a three-stage OOD response:\n1. **Detection** - monitors \"real-imagination discrepancy\" (latent distance between actual observations and predicted states)\n2. **Imagination** - when OOD is detected, abandons the corrupted visual stream and generates actions conditioned on autoregressively forecasted latent dynamics\n3. **Recovery** - applies compensatory spatial corrections via pose estimation once the displaced object settles\n\n**Key Results:**\n- 73.8% OOD success on MetaWorld (vs. 23.9% baseline with tracking)\n- 83.3% success under real-world spatial shifts (vs. 3.3% baseline)\n- 76.7% real-world success in open-loop imagination (no visual feedback post-initialization)\n\n**Relation to test-time geometric robustness of diffusion policies:** DDP is directly relevant as it uses a *test-time inference mechanism* (switching to imagined latent states) to handle geometric/spatial perturbations. However, it requires training a world model jointly with the policy -- it is not a pure test-time method. The spatial correction is computed as a static displacement offset rather than a continuous geometric transformation.\n\n---\n\n## Paper 2: \"Visual-Geometry Diffusion Policy\" (VGDP)\n\n**arXiv 2511.22445, November 2025**\n\n**Problem:** Visuomotor policies relying on single-modality inputs (RGB alone or point clouds alone) fail to generalize under visual and spatial perturbations.\n\n**Approach:** VGDP introduces a Complementarity-Aware Fusion Module combining RGB (ResNet-18, 512-dim) and point cloud (DP3, 64-dim) features:\n- Features project into a shared 256-dimensional space\n- **Modality dropout** (p=0.2) randomly disables entire RGB or 3D branches during training, forcing modality-invariant representations\n- Bidirectional cross-attention with residual connections enables lightweight modality interaction\n- A diffusion policy head denoises actions conditioned on the fused representation\n\n**Key Results:**\n- 39.1% average improvement over 7 baselines (18 sim + 4 real tasks)\n- 15.2% improvement under spatial perturbations\n- 41.5% improvement under visual condition changes\n- 11x stability improvement (variance 2.53% vs. 32.72% for competitors)\n- 55.3% higher mean success under severe randomization\n\n**Relation to test-time geometric robustness:** VGDP achieves spatial robustness through *training-time architectural design* (multimodal fusion + modality dropout) rather than test-time inference modifications. It demonstrates that point cloud geometry provides complementary spatial information that compensates for RGB failures under geometric shifts. This is a representational/training approach rather than a test-time inference method.\n\n---\n\n## Additional Related Work Discovered\n\n### SE(3)-Equivariant Approaches (highly relevant to geometric robustness)\n\n**EquiForm** (arXiv 2601.17486, January 2026): Noise-robust SE(3)-equivariant policy learning from 3D point clouds. Uses a geometric denoising module + equivariant contrastive learning to maintain SE(3) structure under realistic sensor noise. Achieves 17.2% improvement in sim, 28.1% in real-world. Directly addresses the breakdown of equivariance guarantees under noisy conditions.\n\n**ReSeFlow** (arXiv 2509.22695, September 2025): Rectified SE(3)-equivariant flow matching. Replaces iterative diffusion denoising with straight geodesic-like paths in SE(3) space, enabling single-step inference. Up to 48.5% error reduction. Combines geometric invariance with flow-based efficiency.\n\n**Spherical Diffusion Policy (SDP)** (arXiv 2507.01723): SE(3)-equivariant diffusion policy operating in spherical Fourier space, adapting trajectories according to 3D scene transformations.\n\n### Flow Matching Approaches\n\n**FlowPolicy** (AAAI 2025 Oral, arXiv 2412.04987): Consistency flow matching for single-step policy generation with 7x inference speedup. Uses 3D point clouds but does not explicitly address spatial robustness.\n\n**Flow Matching Policy Gradients (FPO)** (ICLR 2026): Policy gradient algorithm for optimizing flow-based generative models via conditional flow matching objective reframing.\n\n### Test-Time Composition\n\n**General Policy Composition (GPC)** (arXiv 2510.01068): Training-free test-time composition of diffusion/flow policy scores via convex combination. Does NOT specifically address geometric robustness but provides a framework for test-time policy enhancement without retraining.\n\n---\n\n## Summary of Relevance to \"Test-Time Inference Methods for Geometric Robustness of Diffusion Policies\"\n\n| Paper | Training-time? | Test-time? | Geometric Focus? |\n|-------|---------------|-----------|-----------------|\n| DDP | Yes (world model co-training) | Yes (imagination at inference) | Yes (spatial displacement recovery) |\n| VGDP | Yes (modality dropout/fusion) | No | Yes (point cloud + RGB fusion) |\n| EquiForm | Yes (denoising + contrastive) | No | Yes (SE(3) under noise) |\n| ReSeFlow | Yes (rectified flow) | Partially (single-step) | Yes (SE(3) equivariance) |\n| GPC | No | Yes (score composition) | No |\n\n**DDP is the most directly relevant** as it is the only paper combining both a test-time inference mechanism (switching to imagined states) with explicit geometric/spatial perturbation handling. **VGDP** is relevant as a training-time baseline showing what multimodal fusion can achieve for spatial robustness. The **SE(3)-equivariant line of work** (EquiForm, ReSeFlow, SDP) provides an orthogonal approach to geometric robustness through architectural symmetry constraints rather than test-time adaptation.\n\nSources:\n- [DDP - Dreaming the Unseen](https://arxiv.org/html/2603.21017v1)\n- [VGDP - Visual-Geometry Diffusion Policy](https://arxiv.org/abs/2511.22445)\n- [GPC - Compose Your Policies](https://arxiv.org/abs/2510.01068)\n- [FlowPolicy](https://arxiv.org/abs/2412.04987)\n- [EquiForm](https://arxiv.org/html/2601.17486)\n- [ReSeFlow](https://arxiv.org/html/2509.22695v1)\n- [Spherical Diffusion Policy](https://arxiv.org/abs/2507.01723)\n- [Flow Matching Policy Gradients (ICLR 2026)](https://openreview.net/pdf/376ea41422d8f63f58a4916b9a9783de90e8e461.pdf)"
      }
    ],
    "totalDurationMs": 123596,
    "totalTokens": 23903,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1113,
      "cache_read_input_tokens": 20917,
      "output_tokens": 1872,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1113
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1872,
          "cache_read_input_tokens": 20917,
          "cache_creation_input_tokens": 1113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1113,
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
      "otherToolCount": 14
    }
  },
  "sourceToolAssistantUUID": "1cb6a58d-2aac-4907-bbcd-63899323b8c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T20:22:11.131Z_

<details><summary>↩ Tool result · `toolu_016qE4Eqdn32SodwrqSqjN9u`</summary>

```text
I now have comprehensive information on all three topics. Here is my detailed research report:

---

## 1. TTPL / PDF (Test-Time Perturbation Learning with Delayed Feedback)

**Paper**: [arXiv:2604.18107](https://arxiv.org/abs/2604.18107), April 2026. The method is actually called **PDF** (Perturbation learning with Delayed Feedback), though the paper title uses "Test-Time Perturbation Learning."

### Exact Mechanism

PDF has three components working together:

1. **Uncertainty-based Data Augmentation + Action Voting**: At each timestep, the model computes normalized Shannon entropy of the predicted action distribution: `U_t = -1/log(K) * sum(p(a_k|s_k) * log(p(a_k|s_k)))`. This uncertainty score drives an adaptive augmentation budget: `N_t = N_max * U_t` (with N_max = 3). Multiple augmented observations are generated, passed through the frozen VLA, and the resulting candidate actions are selected via **majority voting** (not simple averaging).

2. **Adaptive Scheduler**: Allocates more augmented views when the model is uncertain, fewer when confident. This balances performance vs. computational cost.

3. **Lightweight Perturbation Module (P-head)**: A small 9M-parameter learned head `h_theta` that adjusts action logits: `z_tilde_t = h_phi(f_t) + lambda * h_theta(f_t)`. Only `h_theta` is updated; all VLA parameters remain frozen.

### Environment Feedback Requirement

**Yes, it requires delayed episodic feedback during deployment.** Upon task completion, the agent receives a delayed reward signal `r_i` indicating task success/failure. The perturbation head is trained via REINFORCE: `L = -(r-b) * log(pi_phi) + lambda_kl * I[r>b] * KL(pi_phi || pi_tilde)`. This is a critical limitation -- it needs end-of-episode reward signals.

### Comparison to Simple Averaging

The paper does NOT explicitly include a "simple averaging of augmented views" baseline. However, based on the ablation:
- **PDF w/o DF** = multi-view voting only (no delayed feedback learning) -- this is essentially augment + vote without the learned perturbation
- **PDF w/o DA** = perturbation learning with only original observations (no augmentation)
- Both underperform the full method. Notably, without delayed feedback, performance drops substantially (0.50 on Object suite vs much higher with full method).

The key difference from naive TTA averaging: (1) they use majority voting not mean averaging; (2) the augmentation budget adapts to uncertainty; (3) the perturbation head learns from episodic feedback to correct overconfidence.

### LIBERO Results: +7.4% average success rate improvement over vanilla OpenVLA.

---

## 2. Test-Time Augmentation (TTA) for Robot Manipulation Policies

### State of the Art for Prediction Averaging / Filtering

The literature reveals several distinct approaches, none of which are simple TTA averaging:

**a) MG-Select (ICLR 2026)** -- [Verifier-free Test-Time Sampling](https://arxiv.org/html/2510.05681v1)
- Samples N=4 action candidates in parallel (temperature-controlled stochastic sampling)
- Scores them using KL divergence between normal predictions and "condition-masked" predictions (model with randomly masked text/state inputs)
- Selects the candidate with highest KL divergence (most "confident" deviation from uncertain baseline)
- Does NOT use data augmentation at test time
- Results: +168% on RoboCasa, +28%/+35% in/out-of-distribution on real Franka

**b) VOTE (2025)** -- [Trajectory Ensemble Voting](https://arxiv.org/abs/2507.05116)
- Collects action predictions across timesteps and uses cosine similarity to identify consensus
- Actions split into two groups by threshold (tau=0.5); the larger group is averaged
- Explicitly compares Vote Ensemble (64.5%) vs. naive Average (61.6%) vs. no ensemble (47.1%)
- **This is the clearest direct comparison**: voting outperforms simple averaging by ~3 points

**c) GPC (Generative Predictive Control, 2025)** -- [arXiv:2502.00622](https://arxiv.org/abs/2502.00622)
- Samples K action proposals from frozen diffusion policy
- Rolls each forward through a learned world model
- Selects the one with highest predicted reward (GPC-RANK) or refines via gradient ascent (GPC-OPT)
- ~10-25% improvement over pure behavior cloning

**d) RoVer** -- Uses a learned Process Reward Model to score action chunks at test time

### Key Finding: Why Simple Averaging Fails

The literature consistently notes that **averaging multimodal action distributions produces invalid or suboptimal actions**. MSE-style averaging of diverse expert behaviors results in conservative or infeasible actions (the "averaging" problem). This is why voting/selection methods dominate over simple mean-based TTA in robotics.

### Has Anyone Compared TTA to Sophisticated Filtering?

**Yes -- the VOTE paper (Table 5) is the most direct comparison**:
- No ensemble: 47.1%
- Simple Average: 61.6%  
- Vote Ensemble (filtering): 64.5%

MG-Select compares against likelihood-based selection but not against augmentation-based averaging specifically.

---

## 3. Fast-WAM Architecture Details

**Paper**: [arXiv:2603.16666](https://arxiv.org/abs/2603.16666), March 2026.

### Flow-Matching vs. Diffusion

**Flow-matching (velocity field)**. The paper explicitly states it is "trained to predict the corresponding velocity field with a standard flow matching objective." This is NOT score-based diffusion.

### Integration Steps

**10 denoising steps** at inference with classifier-free guidance (CFG) scale of 1.0.

### Code and Checkpoint Release

Both are publicly available:
- **GitHub**: https://github.com/yuantianyuan01/FastWAM (official codebase)
- **HuggingFace checkpoints**: https://huggingface.co/yuanty/fastwam
  - `libero_uncond_2cam224.pt` + stats JSON
  - `robotwin_uncond_3cam_384.pt` + stats JSON
- **Preprocessed datasets**: `huggingface.co/datasets/yuanty/LIBERO-fastwam` and `huggingface.co/datasets/yuanty/robotwin2.0-fastwam`

### LIBERO-Plus Evaluation

**No.** Fast-WAM has NOT been evaluated on LIBERO-Plus. It only evaluates on standard LIBERO suites (Spatial, Object, Goal, Long) and RoboTwin.

### LIBERO Results

Average **97.6%** success rate:
- Spatial: 98.2%
- Object: 100.0%
- Goal: 97.0%
- Long: 95.2%

### Architecture

- Built on **Wan2.2-5B** video DiT backbone + 1B action expert DiT (6B total parameters)
- **Mixture-of-Transformer (MoT)** design with shared attention
- Action horizon: 32 steps; 9 video frames per chunk
- Training: joint flow-matching loss `L = L_act + lambda * L_vid`
- Inference latency: **190ms** on single GPU (4x faster than imagine-then-execute WAMs)
- Key insight: video co-training during training improves representations, but explicit future video generation at test time is unnecessary

---

## Summary Table for Your Paper Revision

| Method | Mechanism | Needs Env Feedback? | Simple Avg Baseline? |
|--------|-----------|--------------------|--------------------|
| PDF/TTPL | Augment + vote + learned perturbation | Yes (episodic reward) | Not directly compared |
| MG-Select | Multi-sample + KL selection | No | No (compares to likelihood) |
| VOTE | Temporal ensemble + cosine voting | No | Yes: Avg=61.6%, Vote=64.5% |
| GPC | World model ranking/optimization | No (needs world model) | Not directly |
| Fast-WAM | Flow-matching WAM (no test-time imagination) | No | N/A (not a TTA method) |

Sources:
- [TTPL/PDF - arXiv:2604.18107](https://arxiv.org/abs/2604.18107)
- [Fast-WAM - arXiv:2603.16666](https://arxiv.org/abs/2603.16666)
- [Fast-WAM GitHub](https://github.com/yuantianyuan01/FastWAM)
- [Fast-WAM HuggingFace](https://huggingface.co/yuanty/fastwam)
- [MG-Select - Verifier-free Test-Time Sampling](https://arxiv.org/html/2510.05681v1)
- [VOTE - Trajectory Ensemble Voting](https://arxiv.org/abs/2507.05116)
- [GPC - Generative Predictive Control](https://arxiv.org/abs/2502.00622)
- [RoVer - Robot Reward Model as Test-Time Verifier](https://arxiv.org/abs/2510.10975)
- [Diff-DAgger - Uncertainty Estimation with Diffusion Policy](https://arxiv.org/html/2410.14868v1)

agentId: aaadd70e821d54dca (use SendMessage with to: 'aaadd70e821d54dca' to continue this agent)
&lt;usage>total_tokens: 28788
tool_uses: 20
duration_ms: 184904&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d1b0641-3257-4a15-b731-8346ec3ceff1",
  "isSidechain": false,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "type": "user",
  "uuid": "ce5ce05c-2de1-4a41-9cbf-87f251de5647",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research two things for a paper revision:\n\n1. **TTPL (Test-Time Perturbation Learning with Delayed Feedback for VLA Models)** - arXiv April 2026. Claims +7.4% on LIBERO via test-time perturbation learning with delayed feedback. I need to understand:\n   - What is their exact mechanism? (augmentation + voting? uncertainty estimation?)\n   - Do they require environment feedback during deployment?\n   - How does their approach compare to simply averaging predictions from augmented views?\n   - Search for \"TTPL test-time perturbation learning VLA\" and fetch the paper.\n\n2. **Test-time augmentation (TTA) for robot manipulation policies** - I need to understand what simple TTA baselines exist:\n   - Search \"test-time augmentation robot policy manipulation\"\n   - Search \"ensemble augmentation inference robot learning diffusion\"\n   - What's the state of the art for simple prediction averaging from augmented views?\n   - Has anyone compared TTA to more sophisticated filtering methods for robot policies?\n\n3. **Fast-WAM architecture details** - Search for \"Fast-WAM world action model\" and verify:\n   - Does it use flow-matching (velocity field) or diffusion (score)?\n   - How many integration steps?\n   - Is the code/checkpoint actually released on HuggingFace?\n   - Has it been evaluated on LIBERO-Plus anywhere?\n\nReport findings in detail.",
    "agentId": "aaadd70e821d54dca",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on all three topics. Here is my detailed research report:\n\n---\n\n## 1. TTPL / PDF (Test-Time Perturbation Learning with Delayed Feedback)\n\n**Paper**: [arXiv:2604.18107](https://arxiv.org/abs/2604.18107), April 2026. The method is actually called **PDF** (Perturbation learning with Delayed Feedback), though the paper title uses \"Test-Time Perturbation Learning.\"\n\n### Exact Mechanism\n\nPDF has three components working together:\n\n1. **Uncertainty-based Data Augmentation + Action Voting**: At each timestep, the model computes normalized Shannon entropy of the predicted action distribution: `U_t = -1/log(K) * sum(p(a_k|s_k) * log(p(a_k|s_k)))`. This uncertainty score drives an adaptive augmentation budget: `N_t = N_max * U_t` (with N_max = 3). Multiple augmented observations are generated, passed through the frozen VLA, and the resulting candidate actions are selected via **majority voting** (not simple averaging).\n\n2. **Adaptive Scheduler**: Allocates more augmented views when the model is uncertain, fewer when confident. This balances performance vs. computational cost.\n\n3. **Lightweight Perturbation Module (P-head)**: A small 9M-parameter learned head `h_theta` that adjusts action logits: `z_tilde_t = h_phi(f_t) + lambda * h_theta(f_t)`. Only `h_theta` is updated; all VLA parameters remain frozen.\n\n### Environment Feedback Requirement\n\n**Yes, it requires delayed episodic feedback during deployment.** Upon task completion, the agent receives a delayed reward signal `r_i` indicating task success/failure. The perturbation head is trained via REINFORCE: `L = -(r-b) * log(pi_phi) + lambda_kl * I[r>b] * KL(pi_phi || pi_tilde)`. This is a critical limitation -- it needs end-of-episode reward signals.\n\n### Comparison to Simple Averaging\n\nThe paper does NOT explicitly include a \"simple averaging of augmented views\" baseline. However, based on the ablation:\n- **PDF w/o DF** = multi-view voting only (no delayed feedback learning) -- this is essentially augment + vote without the learned perturbation\n- **PDF w/o DA** = perturbation learning with only original observations (no augmentation)\n- Both underperform the full method. Notably, without delayed feedback, performance drops substantially (0.50 on Object suite vs much higher with full method).\n\nThe key difference from naive TTA averaging: (1) they use majority voting not mean averaging; (2) the augmentation budget adapts to uncertainty; (3) the perturbation head learns from episodic feedback to correct overconfidence.\n\n### LIBERO Results: +7.4% average success rate improvement over vanilla OpenVLA.\n\n---\n\n## 2. Test-Time Augmentation (TTA) for Robot Manipulation Policies\n\n### State of the Art for Prediction Averaging / Filtering\n\nThe literature reveals several distinct approaches, none of which are simple TTA averaging:\n\n**a) MG-Select (ICLR 2026)** -- [Verifier-free Test-Time Sampling](https://arxiv.org/html/2510.05681v1)\n- Samples N=4 action candidates in parallel (temperature-controlled stochastic sampling)\n- Scores them using KL divergence between normal predictions and \"condition-masked\" predictions (model with randomly masked text/state inputs)\n- Selects the candidate with highest KL divergence (most \"confident\" deviation from uncertain baseline)\n- Does NOT use data augmentation at test time\n- Results: +168% on RoboCasa, +28%/+35% in/out-of-distribution on real Franka\n\n**b) VOTE (2025)** -- [Trajectory Ensemble Voting](https://arxiv.org/abs/2507.05116)\n- Collects action predictions across timesteps and uses cosine similarity to identify consensus\n- Actions split into two groups by threshold (tau=0.5); the larger group is averaged\n- Explicitly compares Vote Ensemble (64.5%) vs. naive Average (61.6%) vs. no ensemble (47.1%)\n- **This is the clearest direct comparison**: voting outperforms simple averaging by ~3 points\n\n**c) GPC (Generative Predictive Control, 2025)** -- [arXiv:2502.00622](https://arxiv.org/abs/2502.00622)\n- Samples K action proposals from frozen diffusion policy\n- Rolls each forward through a learned world model\n- Selects the one with highest predicted reward (GPC-RANK) or refines via gradient ascent (GPC-OPT)\n- ~10-25% improvement over pure behavior cloning\n\n**d) RoVer** -- Uses a learned Process Reward Model to score action chunks at test time\n\n### Key Finding: Why Simple Averaging Fails\n\nThe literature consistently notes that **averaging multimodal action distributions produces invalid or suboptimal actions**. MSE-style averaging of diverse expert behaviors results in conservative or infeasible actions (the \"averaging\" problem). This is why voting/selection methods dominate over simple mean-based TTA in robotics.\n\n### Has Anyone Compared TTA to Sophisticated Filtering?\n\n**Yes -- the VOTE paper (Table 5) is the most direct comparison**:\n- No ensemble: 47.1%\n- Simple Average: 61.6%  \n- Vote Ensemble (filtering): 64.5%\n\nMG-Select compares against likelihood-based selection but not against augmentation-based averaging specifically.\n\n---\n\n## 3. Fast-WAM Architecture Details\n\n**Paper**: [arXiv:2603.16666](https://arxiv.org/abs/2603.16666), March 2026.\n\n### Flow-Matching vs. Diffusion\n\n**Flow-matching (velocity field)**. The paper explicitly states it is \"trained to predict the corresponding velocity field with a standard flow matching objective.\" This is NOT score-based diffusion.\n\n### Integration Steps\n\n**10 denoising steps** at inference with classifier-free guidance (CFG) scale of 1.0.\n\n### Code and Checkpoint Release\n\nBoth are publicly available:\n- **GitHub**: https://github.com/yuantianyuan01/FastWAM (official codebase)\n- **HuggingFace checkpoints**: https://huggingface.co/yuanty/fastwam\n  - `libero_uncond_2cam224.pt` + stats JSON\n  - `robotwin_uncond_3cam_384.pt` + stats JSON\n- **Preprocessed datasets**: `huggingface.co/datasets/yuanty/LIBERO-fastwam` and `huggingface.co/datasets/yuanty/robotwin2.0-fastwam`\n\n### LIBERO-Plus Evaluation\n\n**No.** Fast-WAM has NOT been evaluated on LIBERO-Plus. It only evaluates on standard LIBERO suites (Spatial, Object, Goal, Long) and RoboTwin.\n\n### LIBERO Results\n\nAverage **97.6%** success rate:\n- Spatial: 98.2%\n- Object: 100.0%\n- Goal: 97.0%\n- Long: 95.2%\n\n### Architecture\n\n- Built on **Wan2.2-5B** video DiT backbone + 1B action expert DiT (6B total parameters)\n- **Mixture-of-Transformer (MoT)** design with shared attention\n- Action horizon: 32 steps; 9 video frames per chunk\n- Training: joint flow-matching loss `L = L_act + lambda * L_vid`\n- Inference latency: **190ms** on single GPU (4x faster than imagine-then-execute WAMs)\n- Key insight: video co-training during training improves representations, but explicit future video generation at test time is unnecessary\n\n---\n\n## Summary Table for Your Paper Revision\n\n| Method | Mechanism | Needs Env Feedback? | Simple Avg Baseline? |\n|--------|-----------|--------------------|--------------------|\n| PDF/TTPL | Augment + vote + learned perturbation | Yes (episodic reward) | Not directly compared |\n| MG-Select | Multi-sample + KL selection | No | No (compares to likelihood) |\n| VOTE | Temporal ensemble + cosine voting | No | Yes: Avg=61.6%, Vote=64.5% |\n| GPC | World model ranking/optimization | No (needs world model) | Not directly |\n| Fast-WAM | Flow-matching WAM (no test-time imagination) | No | N/A (not a TTA method) |\n\nSources:\n- [TTPL/PDF - arXiv:2604.18107](https://arxiv.org/abs/2604.18107)\n- [Fast-WAM - arXiv:2603.16666](https://arxiv.org/abs/2603.16666)\n- [Fast-WAM GitHub](https://github.com/yuantianyuan01/FastWAM)\n- [Fast-WAM HuggingFace](https://huggingface.co/yuanty/fastwam)\n- [MG-Select - Verifier-free Test-Time Sampling](https://arxiv.org/html/2510.05681v1)\n- [VOTE - Trajectory Ensemble Voting](https://arxiv.org/abs/2507.05116)\n- [GPC - Generative Predictive Control](https://arxiv.org/abs/2502.00622)\n- [RoVer - Robot Reward Model as Test-Time Verifier](https://arxiv.org/abs/2510.10975)\n- [Diff-DAgger - Uncertainty Estimation with Diffusion Policy](https://arxiv.org/html/2410.14868v1)"
      }
    ],
    "totalDurationMs": 184904,
    "totalTokens": 28788,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1309,
      "cache_read_input_tokens": 25094,
      "output_tokens": 2384,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1309
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2384,
          "cache_read_input_tokens": 25094,
          "cache_creation_input_tokens": 1309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1309,
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
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "0d1b0641-3257-4a15-b731-8346ec3ceff1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Geometric Sensitivity Filtering: Training-Free Score Subspace Projecti…",
  "leafUuid": "ce5ce05c-2de1-4a41-9cbf-87f251de5647",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate Fast-WAM LIBERO-Plus baseline before committing to GSF",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52"
}
```

---

### Tool result

_source line 19 · 2026-05-10T20:22:54.928Z_

<details><summary>↩ Tool result · `toolu_01HGXLtVhXyTTMZSkorx2ZHP`</summary>

```text
Now I have comprehensive information. Let me compile the findings into a clear report.

---

## Summary of Findings

### 1. Spectral/Eigenvalue Structure of Score Functions and Velocity Fields

**Strong supporting evidence exists.** Several lines of work establish that diffusion model score functions and velocity fields have interpretable spectral structure:

- **"Spectral Analysis of Diffusion Models with Application to Schedule Design"** (NeurIPS 2025, [arXiv:2502.00180](https://arxiv.org/abs/2502.00180)): Shows that under Gaussianity, the diffusion inference process decomposes into independent scalar transfer functions along eigenvectors of the data covariance. Different eigenvalues correspond to different frequency components, and the diffusion process reconstructs low-frequency (large-eigenvalue) components first, high-frequency (small-eigenvalue) components later. This is the "coarse-to-fine" pattern.

- **Sander Dieleman's "Diffusion is Spectral Autoregression"** ([blog post, Sept 2024](https://sander.ai/2024/09/02/spectral-autoregression.html)): Argues that diffusion models perform approximate autoregression in frequency space -- low frequencies have higher SNR throughout the reverse process and are generated first.

- **"Generalization Guarantees for Neural Networks via Harnessing the Low-rank Structure of the Jacobian"** ([arXiv:1906.05392](https://arxiv.org/abs/1906.05392)): Shows that Jacobians of typical neural networks exhibit low-rank structure with a few large singular values and many small ones, creating a low-dimensional "information space."

### 2. Low-Rank Structure of Score Functions

**Yes, this has been demonstrated:**

- **"The Unreasonable Effectiveness of Gaussian Score Approximation for Diffusion Models"** (Dec 2024, [arXiv:2412.09726](https://arxiv.org/html/2412.09726v1)): Key finding -- at high noise levels, score functions are well-approximated by a low-rank Gaussian model. The required covariance rank increases as noise decreases toward zero. At moderate-to-high noise, "the score field of real diffusion models is dominated by its Gaussian/linear approximation." For lower noise, a Gaussian mixture with moderate modes is needed, with a trade-off between component count and local covariance rank.

- **DiffStateGrad** (ICLR 2025, [arXiv:2410.03463](https://arxiv.org/abs/2410.03463)): Empirically validates that intermediate diffusion states have exploitable low-rank structure. Their code uses `var_cutoff=0.99` for adaptive rank selection via SVD, meaning they retain singular vectors that explain 99% of variance -- implying rapid singular value decay.

### 3. DiffStateGrad: SVD-Based Projection for Diffusion Models

**Paper:** "Diffusion State-Guided Projected Gradient for Inverse Problems" by Rayhan Zirvi, Bahareh Tolooshams, and Anima Anandkumar (ICLR 2025).

**Structural assumptions:**
- Intermediate diffusion states live in a low-rank subspace
- SVD on the diffusion state reveals the relevant subspace via highest singular vectors
- Projecting guidance gradients onto this subspace keeps generation on the data manifold
- Adaptive rank is determined by a variance cutoff (99% of explained variance)
- The "crucial factor is the choice of the subspace, not just its low-rank nature"

**Key implication for your work:** DiffStateGrad demonstrates that SVD of intermediate diffusion states reveals geometrically meaningful directions. This is closely analogous to what you propose -- decomposing the velocity field's sensitivity via SVD to find geometrically important directions. However, DiffStateGrad operates on image states for inverse problems, not on robot action velocity fields for geometric robustness.

### 4. Geometric Robustness / Test-Time Inference for Diffusion Policies

Several relevant works:

- **"Compose Your Policies" (GPC)** ([arXiv:2510.01068](https://arxiv.org/abs/2510.01068)): A training-free test-time method that combines distributional scores from multiple diffusion/flow-matching robot policies via convex combination. Uses fixed weights found by test-time search, NOT variance/uncertainty weighting. Works for both diffusion and flow-matching policies.

- **"Dreaming the Unseen" (Dream Diffusion Policy)** ([arXiv:2603.21017](https://arxiv.org/html/2603.21017v1)): Uses a shared 3D encoder for geometric latent embeddings; detects OOD anomalies at inference and falls back on internal "imagination" from a world model.

- **"Mask World Model"** ([arXiv:2604.19683](https://arxiv.org/html/2604.19683)): Imposes a geometric information bottleneck via semantic mask prediction during training, runs on raw RGB at test time.

None of these explicitly perform SVD-based geometric sensitivity analysis on velocity fields at test time.

### 5. Variance-Weighted Ensembling for Robot Policies

**Yes, this concept has been explored, but with important caveats:**

- **Disagreement-Regularized Imitation Learning (DRIL)** ([OpenReview](https://openreview.net/forum?id=rkgbYyHtwB)): Trains an ensemble of behavior cloning policies and uses the variance of their predictions as a cost signal for RL. High variance indicates out-of-distribution states. This uses variance as a *penalty* rather than as *weights for ensembling predictions*.

- **Diff-DAgger** ([arXiv:2410.14868](https://arxiv.org/abs/2410.14868)): Explicitly argues AGAINST ensemble variance for diffusion policies. The key finding: ensemble disagreement fails for multi-modal policies because policies disagree at decision points where multiple valid actions exist, creating false uncertainty signals. They propose using diffusion loss instead. This is a direct challenge to variance-weighted ensembling for diffusion/flow policies.

- **GPC** uses convex score combination with fixed weights, not variance weighting.

**Bottom line:** Simple variance-weighted ensembling has been proposed conceptually (DRIL) but recent work (Diff-DAgger) specifically argues it fails for expressive multi-modal policies like diffusion/flow-matching models. This is a potential vulnerability in your proposal if it relies on ensemble variance.

### 6. OA-WAM Numbers on LIBERO-Plus

**From the OA-WAM paper** ([arXiv:2605.06481](https://arxiv.org/html/2605.06481v1)):

The paper **defines "Geo-Avg" as the mean across three geometric axes** (Camera, Robot Initial State, Layout):
- Camera: 80.5%
- Robot Init: 89.6%
- Layout: 82.8%
- **Geo-Avg: 84.3%** (arithmetic mean of those three)

The paper claims "+4.8% over pi_0.5" with the prior best being 79.5%.

**From the original LIBERO-Plus paper** ([arXiv:2510.13626](https://arxiv.org/html/2510.13626v1)), the main results table does NOT contain OA-WAM (it predates it). The best models in that table on Camera/Robot/Layout are:
- Best Camera: 92.8% (the fine-tuned method in LIBERO-Plus paper itself)
- Best Robot: 46.2% (UniVLA)
- Best Layout: 77.6%

**The 76.0 number the reviewer mentions** likely refers to a different model's Geo-Avg or a different computation. Looking at LIBERO-Plus Table 2 numbers: OpenVLA-OFT gets (56.4 + 31.9 + 74.2)/3 = 54.2; pi_0-Fast gets (65.1 + 21.6 + 68.8)/3 = 51.8. None of the original LIBERO-Plus baselines reach 76.0 on Geo-Avg. The OA-WAM paper's own claim of 84.3 appears internally consistent with their reported per-axis numbers. The reviewer's "76.0" may refer to a different baseline model or a different subset/definition.

---

## Key Takeaways for Your Research Idea

1. **The core assumption has partial support:** Score functions/velocity fields ARE known to have spectral structure and low-rank properties (especially at higher noise levels). DiffStateGrad shows SVD decomposition of diffusion states reveals meaningful geometric subspaces. However, nobody has yet applied this specifically to flow-matching velocity fields in robot policy space to decompose geometric sensitivity.

2. **Gap/novelty exists:** No existing work performs SVD on the Jacobian of a flow-matching robot policy's velocity field to identify geometrically sensitive directions. The closest is DiffStateGrad (image inverse problems) and DRIFT (low-rank weight matrices for efficiency, not sensitivity analysis).

3. **Variance-weighted ensembling is problematic:** Diff-DAgger specifically demonstrates that ensemble variance is unreliable for multi-modal diffusion/flow policies. If your method uses variance weighting, you need to address why it avoids the false-disagreement problem at multi-modal decision points.

4. **OA-WAM's 84.3 Geo-Avg appears to be their own reported number.** The reviewer's 76.0 may reference a different model or computation method that I could not pin down from public sources.

Sources:
- [Spectral Analysis of Diffusion Models with Application to Schedule Design](https://arxiv.org/abs/2502.00180)
- [Diffusion is Spectral Autoregression - Sander Dieleman](https://sander.ai/2024/09/02/spectral-autoregression.html)
- [The Unreasonable Effectiveness of Gaussian Score Approximation](https://arxiv.org/html/2412.09726v1)
- [DiffStateGrad - ICLR 2025](https://arxiv.org/abs/2410.03463)
- [DiffStateGrad Project Page](https://diffstategrad.github.io/)
- [DiffStateGrad GitHub](https://github.com/Anima-Lab/DiffStateGrad)
- [Dynamic Rank Adjustment in Diffusion Policies (DRIFT)](https://arxiv.org/abs/2502.03822)
- [Compose Your Policies (GPC)](https://arxiv.org/abs/2510.01068)
- [Diff-DAgger: Uncertainty Estimation with Diffusion Policy](https://arxiv.org/abs/2410.14868)
- [Disagreement-Regularized Imitation Learning (DRIL)](https://openreview.net/forum?id=rkgbYyHtwB)
- [OA-WAM Paper](https://arxiv.org/html/2605.06481v1)
- [LIBERO-Plus Benchmark](https://arxiv.org/html/2510.13626v1)
- [Low-Rank Jacobian Structure in Neural Networks](https://arxiv.org/abs/1906.05392)
- [Dreaming the Unseen (Dream Diffusion Policy)](https://arxiv.org/html/2603.21017v1)
- [Mask World Model](https://arxiv.org/html/2604.19683)

agentId: a1d899e8303092d51 (use SendMessage with to: 'a1d899e8303092d51' to continue this agent)
&lt;usage>total_tokens: 37258
tool_uses: 31
duration_ms: 220532&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1faab6e0-32b1-48e4-9b9f-eb6da9f17b38",
  "isSidechain": false,
  "promptId": "3558a6dc-24ed-4795-b161-f58d83861b74",
  "type": "user",
  "uuid": "cb01c567-df3f-465f-8926-9476e7b8cfd6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm investigating whether the core assumption of a research idea holds: that velocity fields of flow-matching robot policies have non-uniform geometric sensitivity that can be decomposed via SVD.\n\nPlease search for:\n\n1. \"spectral analysis velocity field diffusion model\" - any work analyzing the spectral/eigenvalue structure of score functions or velocity fields in diffusion/flow models\n\n2. \"low-rank structure diffusion model score\" - whether score functions/velocity fields have been shown to have low-rank structure\n\n3. \"DiffStateGrad SVD diffusion\" - the ICLR 2025 paper on SVD-based projection for diffusion models. Fetch its abstract and understand what structural assumptions it makes about scores.\n\n4. \"geometric robustness test-time inference diffusion\" - any recent work on test-time methods for geometric robustness\n\n5. \"variance weighted ensemble prediction robot\" - whether variance-weighted ensembling has been applied to robot policy predictions\n\n6. Also search for \"OA-WAM LIBERO-Plus\" and verify what the actual Geo-Avg number is (reviewer says 76.0, proposal says 84.3)\n\nReport all findings. I'm particularly interested in:\n- Whether velocity fields are known to have low-rank sensitivity structure\n- Whether simple variance-weighted ensembling has been proposed for robot policies\n- What the actual OA-WAM numbers are on LIBERO-Plus",
    "agentId": "a1d899e8303092d51",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the findings into a clear report.\n\n---\n\n## Summary of Findings\n\n### 1. Spectral/Eigenvalue Structure of Score Functions and Velocity Fields\n\n**Strong supporting evidence exists.** Several lines of work establish that diffusion model score functions and velocity fields have interpretable spectral structure:\n\n- **\"Spectral Analysis of Diffusion Models with Application to Schedule Design\"** (NeurIPS 2025, [arXiv:2502.00180](https://arxiv.org/abs/2502.00180)): Shows that under Gaussianity, the diffusion inference process decomposes into independent scalar transfer functions along eigenvectors of the data covariance. Different eigenvalues correspond to different frequency components, and the diffusion process reconstructs low-frequency (large-eigenvalue) components first, high-frequency (small-eigenvalue) components later. This is the \"coarse-to-fine\" pattern.\n\n- **Sander Dieleman's \"Diffusion is Spectral Autoregression\"** ([blog post, Sept 2024](https://sander.ai/2024/09/02/spectral-autoregression.html)): Argues that diffusion models perform approximate autoregression in frequency space -- low frequencies have higher SNR throughout the reverse process and are generated first.\n\n- **\"Generalization Guarantees for Neural Networks via Harnessing the Low-rank Structure of the Jacobian\"** ([arXiv:1906.05392](https://arxiv.org/abs/1906.05392)): Shows that Jacobians of typical neural networks exhibit low-rank structure with a few large singular values and many small ones, creating a low-dimensional \"information space.\"\n\n### 2. Low-Rank Structure of Score Functions\n\n**Yes, this has been demonstrated:**\n\n- **\"The Unreasonable Effectiveness of Gaussian Score Approximation for Diffusion Models\"** (Dec 2024, [arXiv:2412.09726](https://arxiv.org/html/2412.09726v1)): Key finding -- at high noise levels, score functions are well-approximated by a low-rank Gaussian model. The required covariance rank increases as noise decreases toward zero. At moderate-to-high noise, \"the score field of real diffusion models is dominated by its Gaussian/linear approximation.\" For lower noise, a Gaussian mixture with moderate modes is needed, with a trade-off between component count and local covariance rank.\n\n- **DiffStateGrad** (ICLR 2025, [arXiv:2410.03463](https://arxiv.org/abs/2410.03463)): Empirically validates that intermediate diffusion states have exploitable low-rank structure. Their code uses `var_cutoff=0.99` for adaptive rank selection via SVD, meaning they retain singular vectors that explain 99% of variance -- implying rapid singular value decay.\n\n### 3. DiffStateGrad: SVD-Based Projection for Diffusion Models\n\n**Paper:** \"Diffusion State-Guided Projected Gradient for Inverse Problems\" by Rayhan Zirvi, Bahareh Tolooshams, and Anima Anandkumar (ICLR 2025).\n\n**Structural assumptions:**\n- Intermediate diffusion states live in a low-rank subspace\n- SVD on the diffusion state reveals the relevant subspace via highest singular vectors\n- Projecting guidance gradients onto this subspace keeps generation on the data manifold\n- Adaptive rank is determined by a variance cutoff (99% of explained variance)\n- The \"crucial factor is the choice of the subspace, not just its low-rank nature\"\n\n**Key implication for your work:** DiffStateGrad demonstrates that SVD of intermediate diffusion states reveals geometrically meaningful directions. This is closely analogous to what you propose -- decomposing the velocity field's sensitivity via SVD to find geometrically important directions. However, DiffStateGrad operates on image states for inverse problems, not on robot action velocity fields for geometric robustness.\n\n### 4. Geometric Robustness / Test-Time Inference for Diffusion Policies\n\nSeveral relevant works:\n\n- **\"Compose Your Policies\" (GPC)** ([arXiv:2510.01068](https://arxiv.org/abs/2510.01068)): A training-free test-time method that combines distributional scores from multiple diffusion/flow-matching robot policies via convex combination. Uses fixed weights found by test-time search, NOT variance/uncertainty weighting. Works for both diffusion and flow-matching policies.\n\n- **\"Dreaming the Unseen\" (Dream Diffusion Policy)** ([arXiv:2603.21017](https://arxiv.org/html/2603.21017v1)): Uses a shared 3D encoder for geometric latent embeddings; detects OOD anomalies at inference and falls back on internal \"imagination\" from a world model.\n\n- **\"Mask World Model\"** ([arXiv:2604.19683](https://arxiv.org/html/2604.19683)): Imposes a geometric information bottleneck via semantic mask prediction during training, runs on raw RGB at test time.\n\nNone of these explicitly perform SVD-based geometric sensitivity analysis on velocity fields at test time.\n\n### 5. Variance-Weighted Ensembling for Robot Policies\n\n**Yes, this concept has been explored, but with important caveats:**\n\n- **Disagreement-Regularized Imitation Learning (DRIL)** ([OpenReview](https://openreview.net/forum?id=rkgbYyHtwB)): Trains an ensemble of behavior cloning policies and uses the variance of their predictions as a cost signal for RL. High variance indicates out-of-distribution states. This uses variance as a *penalty* rather than as *weights for ensembling predictions*.\n\n- **Diff-DAgger** ([arXiv:2410.14868](https://arxiv.org/abs/2410.14868)): Explicitly argues AGAINST ensemble variance for diffusion policies. The key finding: ensemble disagreement fails for multi-modal policies because policies disagree at decision points where multiple valid actions exist, creating false uncertainty signals. They propose using diffusion loss instead. This is a direct challenge to variance-weighted ensembling for diffusion/flow policies.\n\n- **GPC** uses convex score combination with fixed weights, not variance weighting.\n\n**Bottom line:** Simple variance-weighted ensembling has been proposed conceptually (DRIL) but recent work (Diff-DAgger) specifically argues it fails for expressive multi-modal policies like diffusion/flow-matching models. This is a potential vulnerability in your proposal if it relies on ensemble variance.\n\n### 6. OA-WAM Numbers on LIBERO-Plus\n\n**From the OA-WAM paper** ([arXiv:2605.06481](https://arxiv.org/html/2605.06481v1)):\n\nThe paper **defines \"Geo-Avg\" as the mean across three geometric axes** (Camera, Robot Initial State, Layout):\n- Camera: 80.5%\n- Robot Init: 89.6%\n- Layout: 82.8%\n- **Geo-Avg: 84.3%** (arithmetic mean of those three)\n\nThe paper claims \"+4.8% over pi_0.5\" with the prior best being 79.5%.\n\n**From the original LIBERO-Plus paper** ([arXiv:2510.13626](https://arxiv.org/html/2510.13626v1)), the main results table does NOT contain OA-WAM (it predates it). The best models in that table on Camera/Robot/Layout are:\n- Best Camera: 92.8% (the fine-tuned method in LIBERO-Plus paper itself)\n- Best Robot: 46.2% (UniVLA)\n- Best Layout: 77.6%\n\n**The 76.0 number the reviewer mentions** likely refers to a different model's Geo-Avg or a different computation. Looking at LIBERO-Plus Table 2 numbers: OpenVLA-OFT gets (56.4 + 31.9 + 74.2)/3 = 54.2; pi_0-Fast gets (65.1 + 21.6 + 68.8)/3 = 51.8. None of the original LIBERO-Plus baselines reach 76.0 on Geo-Avg. The OA-WAM paper's own claim of 84.3 appears internally consistent with their reported per-axis numbers. The reviewer's \"76.0\" may refer to a different baseline model or a different subset/definition.\n\n---\n\n## Key Takeaways for Your Research Idea\n\n1. **The core assumption has partial support:** Score functions/velocity fields ARE known to have spectral structure and low-rank properties (especially at higher noise levels). DiffStateGrad shows SVD decomposition of diffusion states reveals meaningful geometric subspaces. However, nobody has yet applied this specifically to flow-matching velocity fields in robot policy space to decompose geometric sensitivity.\n\n2. **Gap/novelty exists:** No existing work performs SVD on the Jacobian of a flow-matching robot policy's velocity field to identify geometrically sensitive directions. The closest is DiffStateGrad (image inverse problems) and DRIFT (low-rank weight matrices for efficiency, not sensitivity analysis).\n\n3. **Variance-weighted ensembling is problematic:** Diff-DAgger specifically demonstrates that ensemble variance is unreliable for multi-modal diffusion/flow policies. If your method uses variance weighting, you need to address why it avoids the false-disagreement problem at multi-modal decision points.\n\n4. **OA-WAM's 84.3 Geo-Avg appears to be their own reported number.** The reviewer's 76.0 may reference a different model or computation method that I could not pin down from public sources.\n\nSources:\n- [Spectral Analysis of Diffusion Models with Application to Schedule Design](https://arxiv.org/abs/2502.00180)\n- [Diffusion is Spectral Autoregression - Sander Dieleman](https://sander.ai/2024/09/02/spectral-autoregression.html)\n- [The Unreasonable Effectiveness of Gaussian Score Approximation](https://arxiv.org/html/2412.09726v1)\n- [DiffStateGrad - ICLR 2025](https://arxiv.org/abs/2410.03463)\n- [DiffStateGrad Project Page](https://diffstategrad.github.io/)\n- [DiffStateGrad GitHub](https://github.com/Anima-Lab/DiffStateGrad)\n- [Dynamic Rank Adjustment in Diffusion Policies (DRIFT)](https://arxiv.org/abs/2502.03822)\n- [Compose Your Policies (GPC)](https://arxiv.org/abs/2510.01068)\n- [Diff-DAgger: Uncertainty Estimation with Diffusion Policy](https://arxiv.org/abs/2410.14868)\n- [Disagreement-Regularized Imitation Learning (DRIL)](https://openreview.net/forum?id=rkgbYyHtwB)\n- [OA-WAM Paper](https://arxiv.org/html/2605.06481v1)\n- [LIBERO-Plus Benchmark](https://arxiv.org/html/2510.13626v1)\n- [Low-Rank Jacobian Structure in Neural Networks](https://arxiv.org/abs/1906.05392)\n- [Dreaming the Unseen (Dream Diffusion Policy)](https://arxiv.org/html/2603.21017v1)\n- [Mask World Model](https://arxiv.org/html/2604.19683)"
      }
    ],
    "totalDurationMs": 220532,
    "totalTokens": 37258,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1982,
      "cache_read_input_tokens": 32481,
      "output_tokens": 2794,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1982
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2794,
          "cache_read_input_tokens": 32481,
          "cache_creation_input_tokens": 1982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1982,
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
      "otherToolCount": 31
    }
  },
  "sourceToolAssistantUUID": "1faab6e0-32b1-48e4-9b9f-eb6da9f17b38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T20:24:28.169Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research results. Let me synthesize the key findings:

**Key Findings:**

1. **DDP (Dreaming the Unseen)**: Training-time method that co-trains a world model with diffusion policy. At inference, detects OOD and switches to imagined latent states. Achieves 73.8% on MetaWorld OOD, 83.3% real-world spatial shifts. Requires training - NOT purely test-time.

2. **VGDP**: Training-time multimodal fusion (RGB + point cloud) with modality dropout. 15.2% improvement on spatial perturbations. 

3. **TTPL/PDF**: Uses augmentation plus voting with a learned perturbation head that needs episodic environment feedback through REINFORCE. The simpler augmentation and voting approach without delayed feedback is less effective but doesn't require that feedback loop. Shows +7.4% gains on LIBERO.

4. **Fast-WAM**: Confirmed flow-matching approach with 10 integration steps and publicly available code and checkpoints. Hasn't been tested on LIBERO-Plus yet.

5. **Spectral structure of score functions/velocity fields**: At high noise levels, scores follow low-rank Gaussian approximations, and DiffStateGrad validates this exploitable low-rank structure in intermediate diffusion states.

6. **Variance-weighted ensembling**: Diff-DAgger explicitly warns against using ensemble variance for multi-modal diffusion policies since disagreement at decision points creates false uncertainty signals rather than useful information.

7. **OA-WAM Geo-Avg**: The paper reports Camera 80.5, Robot 89.6, Layout 82.8 with a stated Geo-Avg of 84.3. The reviewer's 76.0 figure might be incorrect or measuring something different, so I'll use the paper's reported number while noting it includes Layout.

8. **Simple TTA baselines**: The VOTE paper shows averaging gets 61.6%, voting improves to 64.5%, while no ensemble drops to 47.1%, demonstrating the value of ensemble approaches.

9. **The core tension**: If variance is unreliable for multi-modal policies, then GSF's SVD approach—which depends on variance and covariance structure—faces the same fundamental problem as variance-weighted methods: disagreement between augmented views could signal multi-modality rather than geometric sensitivity.

The stagnation after seven rounds points to a deeper issue: SVD decomposition assumes unimodal behavior, but diffusion and flow policies are inherently multi-modal, so variance from augmented views conflates geometric sensitivity with multi-modal disagreement.

Without a Fast-WAM LIBERO-Plus baseline, I can't determine if there's meaningful room for improvement, and given that simple averaging only gains ~3pp from filtering in the VOTE paper, GSF needs to convincingly outperform basic test-time augmentation or the approach loses credibility. The framing as a test-time counterpart to equivariant methods is also too ambitious—the gap between approximate heuristic filtering and exact mathematical equivariance is too large.

This calls for a major restructuring: starting with diagnostic experiments to understand the actual problem, establishing clean baselines, then redesigning the mechanism to handle multi-modality properly, with a clear path to demonstrating real improvement.

The key insight is distinguishing geometric sensitivity from multi-modality—multi-modal policies produce variance regardless of augmentation, while geometric sensitivity creates variance that correlates with specific perturbations. I'm designing a mechanism that computes velocity fields across geometric augmentations to capture this distinction.

But wait, I'm realizing that in flow-matching the velocity field is deterministic given fixed inputs, so the multi-modality concern from Diff-DAgger doesn't actually apply here the same way—multi-modality gets expressed differently in this framework.

The key insight is that for a fixed noisy action at a given timestep, the velocity field produces a deterministic output. So when I compute variance under geometric augmentation, that variance purely reflects geometric sensitivity without the confound of multi-modality from different policy rollouts. This actually validates GSF's covariance analysis—all the variance I'm seeing under geometric transformations genuinely captures geometric sensitivity rather than intrinsic stochasticity.

Now I'm seeing why SVD filtering outperforms simple averaging. When I average augmented velocities, I'm taking the centroid of velocities that differ because each augmentation perturbs the observation slightly. But this centroid is suboptimal because the augmentations themselves are arbitrary perturbations that don't match the actual geometric shift at test time. Averaging amplifies noise in high-sensitivity directions where augmentations cause large changes, since those changes don't correspond to real test-time shifts. GSF filtering instead projects the nominal velocity onto the low-sensitivity subspace, keeping only directions where the velocity field is robust to geometric variation.

But zeroing out high-sensitivity directions entirely is problematic if those directions carry important spatial information. So instead, I should use a hybrid approach: keep the nominal velocity in low-sensitivity directions where it's reliable and precise, and replace high-sensitivity components with the consensus across augmentations. The mean across augmentations smooths out the noise induced by geometric sensitivity, giving a more robust estimate in those unreliable directions even if it's less precise.

This variance-weighted interpolation approach outperforms both using the nominal velocity alone (which relies on unreliable high-sensitivity components from a shifted observation) and simple test-time averaging (which dilutes precision where the nominal is actually trustworthy). Since flow-matching velocity fields are deterministic given the state and time, the multi-modality concern from Diff-DAgger doesn't apply here.

Now I'm working through how to structure this as a major revision. The core mechanism is really about decomposing the velocity field and selectively replacing unreliable components with consensus estimates rather than just suppressing them. I'm considering whether to rename GSF to better capture this—something like Geometric Sensitivity Decomposition, or maybe keep GSF but redefine what "filtering" means in this context.

I need to lay out the key structural changes: adding explicit diagnostic and baseline phases, redesigning the mechanism around consensus replacement, standardizing terminology for flow-matching, clarifying the OA-WAM computation, and incorporating comparisons with other recent methods like DDP, VGDP, VOTE, and MG-Select.

Now I'm checking the OA-WAM numbers more carefully—the reviewer claims 76.0 is the correct geometric average, but my calculation from the reported values (Camera 80.5, Robot 89.6, Layout 82.8) gives 84.3, which matches what the paper states. I should verify whether the reviewer is using a different set of axes or a different definition of geometric average, since LIBERO-Plus apparently has more than three evaluation dimensions. I'm going to stick with reporting the individual per-axis numbers (Camera 80.5%, Robot 89.6%, Layout 82.8%) and acknowledge that the Geo-Avg definition seems inconsistent across the paper—the reviewer's 76.0% might reflect a different calculation that includes all difficulty levels, so I'll note that discrepancy rather than pick one number arbitrarily. I'll sidestep the Geo-Avg issue entirely and just report the per-axis numbers where I'm confident, flagging the discrepancy. The real competitive advantage lies in those specific per-axis results anyway—Camera, Robot, Layout performance—rather than trying to justify an aggregate metric.

For the revised framing, the core problem stays the same (geometric robustness without retraining), but I need to sharpen the angle: this is specifically about training-free, architecture-agnostic methods, and the deterministic velocity fields give us a clean way to do sensitivity analysis. I'll also be explicit about what we don't know yet—Fast-WAM's performance on LIBERO-Plus—and gate the plan accordingly.

The phased approach breaks down into an eigenvalue spectrum check to see if low-rank structure exists, then establishing the Fast-WAM baseline on LIBERO-Plus, followed by the main sensitivity analysis work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb01c567-df3f-465f-8926-9476e7b8cfd6",
  "isSidechain": false,
  "requestId": "req_011CauWf4Noo9TQyc6G7xcta",
  "type": "assistant",
  "uuid": "e55a144c-da51-4671-ae95-f8c616eb19f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qc6nhSjgW3ojg1E8uHpkEZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12030,
      "cache_read_input_tokens": 26379,
      "output_tokens": 12193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12193,
          "cache_read_input_tokens": 26379,
          "cache_creation_input_tokens": 12030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12030
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

_source line 21 · 2026-05-10T20:27:40.945Z_

Now I have comprehensive research findings. Let me synthesize the key insights before writing the revision:

**Critical findings:**
1. Fast-WAM confirmed uses flow-matching (velocity fields), 10 steps, code+checkpoints available, NOT evaluated on LIBERO-Plus
2. DDP requires co-training a world model — not purely test-time. VGDP is training-time multimodal fusion.
3. TTPL/PDF requires episodic environment feedback (REINFORCE) — not feedback-free
4. **Diff-DAgger explicitly argues AGAINST ensemble variance for multi-modal policies** — but this doesn't apply to GSF because flow-matching velocity fields are deterministic given (a_t, t, o), so all variance under augmentation IS geometric sensitivity
5. VOTE paper shows averaging gives +14.5pp, smart filtering adds only +2.9pp more — the increment is small
6. Score functions DO have established low-rank spectral structure (NeurIPS 2025, DiffStateGrad validates)
7. OA-WAM reports Camera 80.5, Robot 89.6, Layout 82.8 per-axis — the Geo-Avg definition is ambiguous

**Key theoretical insight I'll incorporate:** Flow-matching velocity fields are deterministic given fixed (a_t, t, o). This means variance under geometric augmentation is PURELY geometric sensitivity — no multi-modality confound. This is the argument that makes SVD-based analysis valid and distinguishes GSF from ensemble methods that suffer from the Diff-DAgger problem.

**Mechanism redesign:** Replace "suppress" with "selective consensus replacement" — in high-sensitivity directions, use the augmentation consensus (more robust) rather than zeroing out. This avoids removing task-relevant spatial information while still improving robustness.

Now I'll write the complete revised idea:

```json
{
  "title": "Geometric Sensitivity Filtering: Training-Free Velocity-Field Decomposition for Robust Flow-Based Robot Policies Under Geometric Perturbation",
  "change_type": "major",
  "core_problem": "Flow-matching and diffusion-based robot policies achieve near-saturated standard benchmark performance (Fast-WAM 97.6% on LIBERO) but are expected to degrade substantially under geometric perturbations based on established findings: LIBERO-Plus demonstrates 95%→<30% drops for strong baselines, and the WAM robustness study (March 2026) identifies geometric perturbation as the dominant failure mode. All existing solutions for geometric robustness require either architectural modification (OA-WAM: object-addressable slots requiring 7B parameter redesign; SDP: SE(3)-equivariant spherical Fourier architecture) or additional training/fine-tuning (CKT-WAM: context knowledge transfer; VGDP: multimodal fusion training; DDP: world model co-training). No training-free, architecture-agnostic inference-time method exists for geometric robustness of pre-trained flow/diffusion policies. The fundamental question: can we improve geometric robustness of ANY pre-trained flow/diffusion policy at test time, without modifying the architecture or retraining? We hypothesize YES, based on a key structural property: flow-matching velocity fields v_θ(a_t, t | o) are DETERMINISTIC functions of their inputs — given a fixed noisy action a_t at timestep t, the velocity is a fixed vector. This means that variance of the velocity field under small geometric augmentations of the observation is PURELY attributable to geometric sensitivity, with no multi-modality confound (unlike ensemble disagreement methods that conflate policy multi-modality with uncertainty). This deterministic property enables clean identification of geometrically-sensitive velocity components via covariance analysis, followed by selective correction using augmentation consensus.",
  "opportunity": "Five converging developments create a precise research opportunity: (1) LIBERO-Plus (2025) and the WAM robustness study (March 2026) establish geometric perturbation as the dominant failure mode, with dramatic performance drops under camera/robot perturbations. The geometric robustness SOTA stands at OA-WAM Camera 80.5%, Robot-Init 89.6% (requires 7B architectural redesign) and CKT-WAM (requires fine-tuning). (2) SE(3)-equivariant approaches (SDP/ICML 2025, EquiBot, ReSeFlow/ICRA 2026, EquiForm 2026) demonstrate geometric equivariance improves robustness — but all require training from scratch. No test-time alternative exists. (3) Inference-time scaling for diffusion/flow models is a validated paradigm (ICLR 2025-2026): noise trajectory search, FK steering, test-time policy composition (GPC/ICLR 2026), and verifier-free test-time sampling (MG-Select/ICLR 2026) all show additional inference compute substitutes for training-time improvements. But none target geometric robustness specifically. (4) DiffStateGrad (ICLR 2025) establishes SVD-based subspace projection as effective for filtering signals in diffusion models, while spectral analysis of diffusion models (NeurIPS 2025) and Gaussian score approximation theory (2024) confirm that score/velocity fields have exploitable low-rank spectral structure. (5) A critical gap in the TTA literature: VOTE (2025) shows prediction averaging improves success (+14.5pp) but smart filtering adds only modest additional improvement (+2.9pp) via trajectory-level cosine voting. However, NO work has exploited the DETERMINISTIC nature of flow-matching velocity fields to perform dimensionwise sensitivity decomposition — a fundamentally different and potentially more powerful approach than trajectory-level ensemble voting. The gap: a principled method leveraging the spectral structure of velocity fields for geometric robustness, applicable to any pre-trained flow/diffusion policy without modification.",
  "landscape": "**Geometric robustness methods (all require training/architecture changes):** OA-WAM (May 2026): object-addressable architecture with per-slot decomposition, Camera 80.5%, Robot 89.6%, Layout 82.8% — requires complete 7B architectural redesign. CKT-WAM (May 2026): parameter-efficient context knowledge transfer — requires fine-tuning. SE(3)-Equivariant Diffusion Policy [SDP] (ICML 2025): spherical Fourier space embedding with equivariant FiLM layers — requires training from scratch. EquiBot (2024): SIM(3)-equivariant diffusion — architecture-specific. ReSeFlow (ICRA 2026): SE(3)-equivariant flow-matching — architecture-specific. EquiForm (Jan 2026): noise-robust SE(3)-equivariant policy, +17.2% sim — requires training. Being-H0.7 (May 2026): 82.1% zero-shot on LIBERO-Plus. VGDP (Nov 2025): complementarity-aware RGB+pointcloud fusion, +15.2% under spatial perturbation — requires multimodal training with modality dropout. DDP/Dreaming the Unseen (March 2026): world-model-regularized diffusion policy, 83.3% under real-world spatial shifts — requires co-training world model with policy. **Training-free inference-time methods (none target geometric robustness with velocity-field decomposition):** GPC/Compose Your Policies (ICLR 2026): convex score composition from multiple policies — requires multiple trained policies, doesn't target geometry. MG-Select (ICLR 2026): verifier-free test-time sampling via KL-divergence scoring of multiple action candidates — uses sampling diversity not geometric augmentation, not geometric-robustness-specific. VOTE (2025): trajectory ensemble with cosine-similarity voting, Average 61.6% vs Vote 64.5% — trajectory-level voting, not velocity-field-level decomposition. ADPro (2025): manifold-constrained denoising with FGR registration — requires point cloud observations. AnyCamVLA (March 2026): zero-shot camera adaptation via novel view synthesis — VLA-specific, camera-only, requires known camera parameters. TTPL/PDF (April 2026): test-time perturbation learning with augmentation + voting + learned perturbation head, +7.4% on LIBERO — requires episodic environment feedback (delayed reward via REINFORCE); the augmentation+voting component alone is less effective. FK steering (ICLR 2026): Feynman-Kac guided inference — requires explicit reward function. **SVD/spectral methods in diffusion models:** DiffStateGrad (ICLR 2025): SVD projection for image inverse problems — validates low-rank subspace structure in intermediate diffusion states. Spectral Analysis of Diffusion Models (NeurIPS 2025): eigenvalue decomposition reveals coarse-to-fine frequency structure along principal components. Gaussian Score Approximation (2024): scores are well-approximated by low-rank Gaussian models at moderate-to-high noise levels. CPC theory (NeurIPS 2025): CFG implicit decomposition into selective component amplification. All single-modal image settings. **Critical distinction (multi-modality vs. geometric sensitivity):** Diff-DAgger (2024) demonstrates that ensemble disagreement is unreliable for multi-modal diffusion policies because policies disagree at valid multi-modal decision points. However, this concern does NOT apply to velocity-field sensitivity analysis: v_θ(a_t, t | o) is DETERMINISTIC given (a_t, t, o), so variance under geometric augmentation is purely geometric sensitivity, not multi-modal disagreement. This is a fundamental structural advantage of velocity-field-level analysis over trajectory-level ensemble methods. **Gap:** No existing work (1) exploits the deterministic structure of flow-matching velocity fields for clean geometric sensitivity decomposition, (2) proposes selective consensus replacement in high-sensitivity subspaces as an alternative to both suppression and naive averaging, or (3) evaluates such a method on LIBERO-Plus geometric perturbations.",
  "approach": "We propose Geometric Sensitivity Filtering (GSF), a training-free inference-time method that improves geometric robustness of pre-trained flow-matching/diffusion robot policies by decomposing velocity fields into geometrically-stable and geometrically-sensitive subspaces, then selectively applying augmentation consensus in the sensitive subspace while preserving nominal precision in the stable subspace.\n\n**Key Theoretical Insight: Why This Differs From Ensemble Methods.** Flow-matching velocity fields v_θ(a_t, t | o) are deterministic functions: given a fixed noisy action a_t at integration step t with observation o, the output is a single vector with no stochasticity. This means that when we compute velocity fields from geometrically-augmented observations {T_k(o)}, ALL variance across the K augmented velocity fields is attributable to geometric sensitivity — there is no multi-modality confound. This distinguishes GSF from ensemble/disagreement methods (e.g., Diff-DAgger shows ensemble variance conflates multi-modality with uncertainty at the trajectory level). At the velocity-field level with fixed (a_t, t), the analysis is clean.\n\n**Why GSF Beats Simple Averaging (The Core Technical Argument).** Consider three alternatives at each integration step:\n- Nominal only: v_0 = v_θ(a_t, t | o) — uses unreliable velocity components when o is geometrically shifted from training distribution\n- Simple TTA (full average): v̄ = (1/K)Σ v_k — treats ALL dimensions equally, diluting precision in stable dimensions (where nominal is reliable) while gaining robustness in sensitive dimensions\n- GSF (selective consensus): uses v_0 in low-sensitivity dimensions (preserving maximum precision where the velocity field is locally stable) and v̄ in high-sensitivity dimensions (improving robustness where the velocity field is unreliable)\n\nGSF dominates both alternatives: it preserves nominal precision where possible (unlike TTA averaging) while improving robustness where needed (unlike nominal-only). The SVD identifies the decomposition boundary — it's not arbitrary but determined by the actual sensitivity structure at each (a_t, t).\n\n**Phased Research Plan with Explicit Gates:**\n\n**Phase 0 — Spectral Diagnostic (1 day, ~2-3h H100).** Before committing to full development: take 5-10 LIBERO-Plus camera-perturbed episodes, compute velocity fields from 8 small geometric augmentations at several integration steps, compute the eigenvalue spectrum of the velocity covariance. GATE: If the spectrum is flat (ratio of top to bottom eigenvalue < 3), there is no exploitable structure and GSF cannot work — abort. If there is a clear spectral gap (top 2-3 eigenvalues dominate, >10x ratio), proceed. Expected outcome: based on DiffStateGrad's findings of clear low-rank structure in diffusion states and established spectral structure theory, we expect a gap — but this must be verified.\n\n**Phase 1 — Fast-WAM LIBERO-Plus Baseline (2-3 days, ~10-15h H100).** Evaluate Fast-WAM's released checkpoint on LIBERO-Plus Camera L1/L3 and Robot-Init L1/L3, 20 episodes each. GATE: If Fast-WAM maintains >85% (unlikely given LIBERO-Plus findings), the improvement ceiling is too small. If it drops to 40-70%, there is substantial room for GSF. If <40%, absolute numbers may be too low to be competitive regardless of relative improvement — consider switching backbone to OA-WAM if checkpoint becomes available.\n\n**Phase 2 — GSF Implementation and Evaluation (8-12 days).**\n\n**Core Mechanism.** At each integration step t during inference:\n1. Given current observation o and noisy action a_t, compute the nominal velocity: v_0 = v_θ(a_t, t | o)\n2. Generate K=4-6 small geometric augmentations of the observation: {T_k(o)} where T_k are random camera jitter (±2-4° rotation, ±3-5% translation) and/or spatial crops\n3. Compute augmented velocities: v_k = v_θ(a_t, t | T_k(o)) for k=1,...,K\n4. Compute velocity covariance across augmentations: C_t = (1/K) Σ_k (v_k - v̄)(v_k - v̄)^T where v̄ = (1/K)Σ v_k\n5. SVD of C_t = U_t Λ_t U_t^T. Top eigenvectors (high eigenvalues) = high geometric sensitivity directions\n6. Construct subspace decomposition: Π_high = Σ_{i: λ_i > τ·tr(Λ)} u_i u_i^T, Π_low = I - Π_high\n7. Apply selective consensus: v_filtered = Π_low · v_0 + Π_high · v̄\n8. Use v_filtered for the integration step\n\n**Interpretation:** In low-sensitivity directions (Π_low), we trust the nominal velocity v_0 computed from the actual (shifted) observation — it retains full precision for stable components. In high-sensitivity directions (Π_high), we replace the unreliable nominal with the augmentation consensus v̄ — which averages out the geometric-sensitivity-induced variability, providing a more robust (if less precise) estimate.\n\n**Adaptive Integration Schedule.** Early integration steps (high noise/far from data) determine coarse trajectory structure and are most geometry-dependent; later steps refine timing and precision. Apply GSF with adaptive strength: aggressive decomposition (lower τ, larger Π_high) at early steps, conservative (higher τ, smaller Π_high) at later steps. Based on the spectral analysis finding that low-rank approximation quality decreases with noise level, we apply full GSF at steps 1-4 (of 10) and nominal-only at steps 5-10, with linear interpolation for the threshold.\n\n**Computational Overhead.** GSF requires K+1 forward passes per filtered integration step. For K=4, applying GSF at M=4 of T=10 steps: 4×5 + 6×1 = 26 forward passes vs. 10 baseline — 2.6x overhead. Optimizations: (i) Cache visual backbone features across integration steps (the observation doesn't change; only recompute action-expert forward pass). (ii) For Fast-WAM's MoT architecture, the video DiT backbone (5B) is shared; only the 1B action expert needs K+1 passes. With feature caching, effective overhead is ~1.5-2x on wall-clock time.\n\n**Backbone Strategy.** Primary: Fast-WAM (97.6% standard LIBERO, released code + HuggingFace checkpoints, flow-matching action head with 10 integration steps, MoT architecture with video DiT + action expert DiT). Secondary: Diffusion Policy (Chi et al., diffusion-based, widely used). Extension: demonstrate on a non-WAM architecture (e.g., standard Diffusion Policy or a VLA with diffusion/flow head) to validate architecture-agnosticism.\n\n**Evaluation Strategy.** Primary benchmark: LIBERO-Plus geometric perturbations — Camera (L1, L3) and Robot-Init (L1, L3), plus Light as control (non-geometric, expect no benefit or slight degradation). Standard LIBERO as sanity check (expect 1-3% degradation from information loss in filtered components). \n\nBaselines: (i) Fast-WAM standard inference (nominal only), (ii) Fast-WAM + Simple TTA: average K+1 velocity fields uniformly then integrate (same compute budget as GSF — the critical apples-to-apples comparison), (iii) Fast-WAM + VOTE-style action voting: generate K+1 full trajectories and select by consensus, (iv) Fast-WAM + GSF (ours — selective consensus in sensitivity-decomposed subspace). \n\nAblations: (a) filtering threshold τ ∈ {0.1, 0.2, 0.3, 0.5} as fraction of trace, (b) number of augmentations K ∈ {2, 4, 6, 8}, (c) augmentation type and magnitude, (d) adaptive vs. uniform schedule across integration steps, (e) which integration steps to apply GSF, (f) eigenvalue spectrum visualization across tasks/perturbation types, (g) component analysis: what do high-sensitivity directions encode? (visualize by perturbing actions along top eigenvectors and rendering predicted trajectories).\n\n**Framing vs. Competitors:** GSF is positioned as a lightweight inference-time method for improving geometric robustness of pre-trained flow/diffusion policies, complementary to training-time approaches. It requires only K+1 forward passes at selected integration steps and no architectural modification. It is NOT equivalent to SE(3)-equivariant methods (which achieve exact mathematical equivariance); rather, it provides approximate geometric stability via empirical sensitivity analysis. The key advantages over alternatives: vs. OA-WAM/CKT-WAM — no retraining/redesign needed; vs. TTPL/PDF — no environment feedback required; vs. AnyCamVLA — no camera parameter knowledge needed, handles robot-init perturbation too; vs. simple TTA — exploits directional sensitivity structure rather than treating all dimensions equally.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~70-100h H100",
      "gpu_utilization": "Moderate (35-45%). Phase 0: 2-3h (spectral diagnostic). Phase 1: 10-15h (baseline evaluation). Phase 2: 55-80h (GSF implementation + evaluation sweeps).",
      "timeline": "2-2.5 weeks with explicit gates (Phase 0: day 1, Phase 1: days 2-4, Phase 2: days 5-16)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$175-300 (at ~$2.50-3.00/H100-hr spot pricing)"
    },
    "human_in_loop": {
      "gpu_hours": "~80-120h H100",
      "gpu_utilization": "Moderate-high (55-70%). Agent implements GSF pipeline, integrates LIBERO-Plus evaluation, runs systematic sweeps. Human reviews spectral diagnostic and Phase 1 baseline results before greenlighting Phase 2.",
      "timeline": "12-16 days (targets CoRL 2026 abstract May 26, paper May 29)",
      "team": "1 researcher, ~30-45min/day for gate decisions",
      "claude_api_cost": "$80-200 (estimated ~800-2000 Opus turns)",
      "estimated_gpu_cost": "$200-360",
      "risk_note": "Primary risk is Phase 0 failure (flat eigenvalue spectrum). Secondary risk is GSF not beating simple TTA significantly. Both are detected early (days 1-5) before major compute investment. The selective-consensus mechanism (vs. original suppression) reduces risk of removing task-relevant information."
    },
    "auto_research": {
      "gpu_hours": "~100-150h H100",
      "gpu_utilization": "High (>80%). Continuous Phase 0→1→2 pipeline with automated gates.",
      "timeline": "10-14 days with 2-4 GPUs concurrently",
      "team": "0 (initial setup only, ~2 hours)",
      "claude_api_cost": "$150-350 (estimated ~1500-3500 Opus turns)",
      "estimated_gpu_cost": "$250-450",
      "speed_bottleneck": "Phase 2 evaluation: 10 LIBERO-Plus tasks × 20 episodes × 150 steps × K+1 forward passes per GSF step. With selective application (M=4 steps), ~26 forward passes per episode step → ~10h per perturbation condition on single H100. 4 conditions + standard LIBERO = ~50h for full evaluation.",
      "risk_note": "Phased gates prevent wasted compute: Phase 0 (2-3h) catches structural infeasibility; Phase 1 (10-15h) catches insufficient baseline degradation. Maximum wasted compute if aborted early: ~15h."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract May 26, paper May 29 — PRIMARY TARGET; 16 days; phased plan with early gates ensures go/no-go decision by day 4; Fast-WAM checkpoint availability eliminates setup risk)",
    "AAAI 2027 (deadline Aug 2026 — secondary target; allows extension to multiple backbones, deeper spectral analysis, and theoretical connection to equivariance)",
    "ICLR 2027 (deadline Sep 2026 — fallback; comprehensive multi-backbone study with theoretical analysis)"
  ],
  "level": "solid",
  "key_references": [
    "Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv March 2026) — PRIMARY BACKBONE; 97.6% standard LIBERO, flow-matching with 10 integration steps, released code (github.com/yuantianyuan01/FastWAM) + HuggingFace checkpoints, MoT architecture with video DiT backbone + action expert DiT; NOT evaluated on LIBERO-Plus (baseline must be established)",
    "OA-WAM: Object-Addressable World Action Model (arXiv May 2026) — LIBERO-Plus Camera 80.5%, Robot 89.6%, Layout 82.8%; flow-matching with 4-step Euler; requires 7B architectural redesign; GSF is complementary (training-free, can potentially be applied on top)",
    "CKT-WAM: Parameter-Efficient Context Knowledge Transfer (arXiv May 2026) — requires fine-tuning; GSF is complementary",
    "SE(3)-Equivariant Diffusion Policy [SDP] (ICML 2025) — training-time equivariant architecture achieving exact SE(3) equivariance; GSF achieves approximate geometric stability via inference-time sensitivity analysis — complementary, not equivalent",
    "DiffStateGrad: Diffusion State-Guided Projected Gradient (ICLR 2025) — SVD-based subspace projection in diffusion models; validates that intermediate states have exploitable low-rank structure with adaptive rank via variance cutoff; key methodological predecessor; our contribution: geometric-sensitivity-defined decomposition with selective consensus (vs. state-rank-defined projection with gradient filtering), applied to robot velocity fields (vs. image restoration)",
    "Spectral Analysis of Diffusion Models with Application to Schedule Design (NeurIPS 2025) — establishes that diffusion inference decomposes into independent transfer functions along eigenvectors of data covariance; coarse-to-fine spectral structure supports our adaptive integration schedule",
    "The Unreasonable Effectiveness of Gaussian Score Approximation for Diffusion Models (2024) — at moderate-to-high noise, score fields are dominated by low-rank Gaussian approximation; supports Phase 0 hypothesis of exploitable spectral structure in velocity fields",
    "Compose Your Policies [GPC] (ICLR 2026) — test-time score composition from multiple policies via convex combination; proves convex score mixing yields superior objectives; our distinction: same policy with geometric augmentations (not multiple policies) and sensitivity-aware weighting (not uniform combination)",
    "MG-Select: Verifier-free Test-Time Sampling (ICLR 2026) — test-time action selection via KL-divergence scoring; +168% on RoboCasa; samples diversity from stochastic decoding rather than geometric augmentation; complementary to GSF",
    "VOTE: Trajectory Ensemble Voting (2025) — cosine-similarity-based trajectory voting; directly shows averaging (+14.5pp) vs. smart voting (+17.4pp) — our distinction: velocity-field-level decomposition rather than trajectory-level voting; dimensionwise sensitivity rather than holistic similarity",
    "Diff-DAgger: Uncertainty Estimation with Diffusion Policy (2024) — demonstrates ensemble disagreement is unreliable for multi-modal diffusion policies due to multi-modality confound; our key distinction: velocity field v_θ(a_t,t|o) is deterministic given fixed inputs, so augmentation variance is PURELY geometric sensitivity — no multi-modality confound",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (arXiv 2025) — 7-dimension perturbation benchmark establishing geometric perturbation as dominant failure mode",
    "Do World Action Models Generalize Better than VLAs? (arXiv March 2026) — WAMs weak on geometric perturbations",
    "Dreaming the Unseen [DDP]: World Model-regularized Diffusion Policy (arXiv March 2026, 2603.21017) — 83.3% real-world success under spatial shifts via world-model co-training + inference-time imagination; requires training a world model jointly with the policy; GSF requires no additional training or world model",
    "Visual-Geometry Diffusion Policy [VGDP] (arXiv Nov 2025, 2511.22445) — +15.2% under spatial perturbation via complementarity-aware RGB+pointcloud fusion with modality dropout; requires multimodal training; GSF works with any single-modality policy",
    "Test-Time Perturbation Learning with Delayed Feedback [TTPL/PDF] (arXiv April 2026) — +7.4% on LIBERO via augmentation + voting + learned perturbation head; requires episodic environment feedback (REINFORCE); GSF requires no environment interaction",
    "ADPro: Test-time Adaptive Diffusion Policy (2025) — manifold-constrained denoising requiring point cloud observations; GSF is observation-modality-agnostic",
    "Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps (ICLR 2025) — establishes paradigm of additional inference compute for better samples; GSF is an instance targeting geometric robustness specifically",
    "A General Framework for Inference-time Scaling and Steering [FK Steering] (ICLR 2026) — Feynman-Kac guided inference requiring explicit reward; GSF uses implicit geometric sensitivity as signal",
    "EquiBot: SIM(3)-Equivariant Diffusion Policy (2024) — training-time equivariant architecture",
    "ReSeFlow: SE(3)-Equivariant Flow Matching (ICRA 2026) — rectified geodesic flow in SE(3); training-time equivariant approach",
    "EquiForm: Noise-Robust SE(3)-Equivariant Policy (Jan 2026) — equivariant contrastive learning under sensor noise; +17.2% sim improvement",
    "AnyCamVLA: Zero-Shot Camera Adaptation (March 2026) — feed-forward novel view synthesis; VLA-specific, camera-only, requires known camera parameters",
    "Being-H0.7: Latent World-Action Model (May 2026) — LIBERO-Plus 82.1% zero-shot / 84.8% fine-tuned",
    "Score Augmentation [ScoreAug] (2025) — equivariant training augmentation in score space; training-time complement",
    "Classifier-free Guidance with Adaptive Scaling [β-CFG] (Feb 2025) — timestep-adaptive guidance scheduling; informs our adaptive filtering schedule",
    "Classifier-Free Diffusion Guidance (NeurIPS 2021 Workshop) — foundational guidance technique",
    "Towards Understanding the Mechanisms of Classifier-Free Guidance [CPC Theory] (NeurIPS 2025) — selective component amplification theory",
    "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (RSS 2023) — foundational; secondary backbone candidate",
    "When to Trust Imagination [FFDC] (May 2026) — confidence-based replanning; orthogonal to GSF"
  ],
  "description": "We propose Geometric Sensitivity Filtering (GSF), a training-free inference-time method that improves geometric robustness of pre-trained flow-matching/diffusion robot policies by decomposing velocity fields into geometrically-stable and geometrically-sensitive subspaces, then applying selective consensus replacement. The key structural insight: flow-matching velocity fields are DETERMINISTIC given fixed inputs (a_t, t, o), meaning variance under geometric augmentation reflects PURE geometric sensitivity with no multi-modality confound — a fundamental advantage over trajectory-level ensemble methods (which Diff-DAgger shows conflate multi-modality with uncertainty). At each integration step, GSF computes velocity fields from K=4-6 small geometric augmentations, performs SVD on the velocity covariance to identify high-sensitivity directions, then constructs a filtered velocity that uses the NOMINAL prediction in stable dimensions (preserving precision) and the AUGMENTATION CONSENSUS in sensitive dimensions (improving robustness). This selective consensus dominates both naive approaches: vs. nominal-only (which uses unreliable components in sensitive directions) and vs. simple TTA averaging (which dilutes precision in stable directions). The research follows an explicitly gated plan: Phase 0 (1 day) verifies exploitable spectral structure exists via eigenvalue analysis; Phase 1 (2-3 days) establishes Fast-WAM's LIBERO-Plus baseline (currently unknown — Fast-WAM has never been evaluated on LIBERO-Plus); Phase 2 (8-12 days) implements and evaluates GSF. Unlike all existing geometric robustness methods — OA-WAM (Camera 80.5%, requires 7B redesign), CKT-WAM (requires fine-tuning), SDP/EquiBot/ReSeFlow (require equivariant architecture), DDP (requires world model co-training), VGDP (requires multimodal training), TTPL (requires environment feedback) — GSF is training-free, architecture-agnostic, feedback-free, and modality-agnostic. It provides approximate geometric stability via empirical sensitivity analysis, complementary to (not equivalent to) training-time equivariant methods that achieve exact mathematical equivariance. Computational overhead is ~2-2.6x (applying GSF at early integration steps with cached visual features). Evaluated on LIBERO-Plus Camera and Robot-Init perturbations with critical baselines including simple TTA (same compute budget, the make-or-break comparison) and trajectory-level voting.",
  "project_name": "geometric_sensitivity_filtering_diffusion_policy",
  "source": "web_research"
}
```

**Summary of changes (major revision):**

1. **Redesigned mechanism**: Replaced velocity "suppression" (zeroing) with "selective consensus replacement" — high-sensitivity directions use augmentation consensus rather than being zeroed out, avoiding removal of task-relevant spatial information.

2. **Added critical theoretical argument**: Flow-matching velocity fields are deterministic given (a_t, t, o), so augmentation variance is purely geometric sensitivity — no multi-modality confound. This distinguishes GSF from ensemble methods that suffer from the Diff-DAgger problem and provides the theoretical basis for why SVD analysis is valid here.

3. **Clear argument for beating simple TTA**: GSF dominates both extremes (nominal-only and full averaging) by preserving precision in stable dimensions while improving robustness in sensitive ones. Included explicit framing of why dimensionwise selectivity matters.

4. **Phased plan with explicit gates**: Phase 0 (spectral diagnostic, 1 day), Phase 1 (Fast-WAM LIBERO-Plus baseline, 2-3 days), Phase 2 (full development, 8-12 days). Prevents committing 2 weeks to a structurally infeasible approach.

5. **Fixed terminology**: "Velocity field" throughout for flow-matching; noted applicability to both diffusion scores and flow velocity fields.

6. **Fixed OA-WAM numbers**: Reported per-axis (Camera 80.5%, Robot 89.6%, Layout 82.8%) rather than ambiguous aggregate.

7. **Added missing related work**: DDP, VGDP, VOTE, MG-Select, Diff-DAgger, EquiForm, spectral analysis papers.

8. **Honest framing**: "Approximate geometric stability via empirical sensitivity analysis, complementary to (not equivalent to) training-time equivariant methods." Dropped the over-claimed "test-time counterpart of SE(3)-equivariance."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e55a144c-da51-4671-ae95-f8c616eb19f8",
  "isSidechain": false,
  "requestId": "req_011CauWf4Noo9TQyc6G7xcta",
  "type": "assistant",
  "uuid": "9e1656de-bf14-4e47-9b05-b0a445a95a7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qc6nhSjgW3ojg1E8uHpkEZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12030,
      "cache_read_input_tokens": 26379,
      "output_tokens": 12193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12193,
          "cache_read_input_tokens": 26379,
          "cache_creation_input_tokens": 12030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12030
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Geometric Sensitivity Filtering: Training-Free Score Subspace Projecti…",
  "leafUuid": "9e1656de-bf14-4e47-9b05-b0a445a95a7e",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate Fast-WAM LIBERO-Plus baseline before committing to GSF",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Geometric Sensitivity Filtering: Training-Free Score Subspace Projecti…",
  "leafUuid": "9e1656de-bf14-4e47-9b05-b0a445a95a7e",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate Fast-WAM LIBERO-Plus baseline before committing to GSF",
  "sessionId": "4efdeba3-01a8-4084-b912-0729c5e53d52"
}
```

---
