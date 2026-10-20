# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 111
- **Recorded user turns:** 1
- **Tool calls:** 32
- **Original source:** `logs/chats/exported-trajectories/account-2/e88c533b-e76f-4333-88cd-e263b24f285e.jsonl`
- **Structured JSON:** [`8b56708bf46d26e7dc91.json`](../../sessions/8b/8b56708bf46d26e7dc91.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T19:54:21.636Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T19:54:21.636Z",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification of World Knowledge for Robust Action Generation\",\n  \"core_problem\": \"World-Action Models (WAMs) achieve near-saturated performance on standard manipulation benchmarks (Being-H0.7: 99.2%, Fast-WAM: 97.6% on LIBERO) but remain brittle under geometric perturbations — camera viewpoint and robot initial state changes cause drops to 60–90% on LIBERO-Plus. Concurrently, Fast-WAM, GigaWorld-Policy, and MotuBrain demonstrate that video features are dispensable at inference under standard conditions. These facts appear contradictory: if video-encoded spatial knowledge is dispensable, why do WAMs fail precisely under geometric perturbations where spatial reasoning should matter most? We hypothesize the resolution lies in HOW video information is used, not WHETHER it is used. Under standard conditions, the action branch encodes sufficient visual-motor mappings from the training distribution, making video features redundant. Under geometric perturbation, these mappings break — and the video branch's spatial reasoning could compensate, but only if the video→action guidance signal is properly amplified and filtered. Standard classifier-free guidance (CFG) in diffusion models amplifies all conditional contributions equally, mixing action-relevant spatial information with irrelevant appearance features. CPC theory (NeurIPS 2025) proves CFG implicitly performs selective amplification via contrastive principal components, but only in class-conditional settings with well-separated covariance structures — not in heterogeneous cross-modal settings like video→action guidance. The core question: can explicit spectral filtering of the cross-modal guidance signal selectively amplify geometric/spatial components that improve robustness while suppressing components that add noise? Before answering this, a prior diagnostic question must be settled: does cross-modal guidance in WAMs carry any action-relevant signal at all under geometric perturbation? No existing work has tested this.\",\n  \"opportunity\": \"Three converging developments create a precise research opportunity, and a critical correction from the prior proposal version enables a more principled approach: (1) UWM (RSS 2025) uses UniDiffuser-style independent diffusion timesteps for video and action modalities — setting the video timestep t_o'=T marginalizes video information, yielding the unconditional action score, while t_o'&lt;T yields the video-conditioned action score. This natively enables cross-modal CFG through two forward passes without any dropout training, architectural modification, or fine-tuning. UWM releases a pretrained LIBERO-90 checkpoint. (2) LIBERO-Plus and the WAM robustness study (March 2026) reveal that geometric perturbations remain the dominant failure mode: OA-WAM Geo-Avg 84.3% (Camera 80.5%, Robot 89.6%), CKT-WAM (Camera 77.4%, Robot 71.4%), with the overall LIBERO-Plus SOTA at 86.1% (CKT-WAM). Crucially, all geometric robustness improvements to date (OA-WAM, CKT-WAM) require architectural modification or additional training — no training-free inference-time method has been attempted. (3) Independent Condition Guidance (ICG, ICLR 2025) demonstrates that CFG-quality guidance can be obtained from any pretrained conditional model without dropout training, by substituting the unconditional score with a prediction conditioned on a random/independent input. This enables cross-modal guidance on WAMs like Fast-WAM that were not trained with video dropout. (4) DiffStateGrad (ICLR 2025) establishes SVD-based subspace projection for filtering diffusion guidance signals, but only in single-modal image restoration. CRITICAL CORRECTION: The prior version incorrectly claimed Fast-WAM was trained with unconditional video feature dropout enabling native CFG. After verification — reading the full paper, project page, and GitHub — this claim is unsupported. Fast-WAM uses CFG scale 1.0 (no guidance amplification), and 'uncond' in checkpoint names refers to its unconditional inference mode (no future video denoising), not CFG-enabling dropout training. UWM's independent timestep mechanism provides the principled alternative, with ICG as a backbone-agnostic complement.\",\n  \"landscape\": \"**Video-at-inference in WAMs:** Fast-WAM (March 2026) removes video denoising at inference, retaining only backbone features. GigaWorld-Policy (March 2026) uses causal masking to block video→action flow. MotuBrain (April 2026) freezes video branch and caches KV pairs. All use binary approaches (all or no video features) and evaluate only on standard benchmarks — none test under geometric perturbation. **Cross-modal CFG support in WAMs:** UWM (RSS 2025) uses independent diffusion timesteps for video and action, enabling native cross-modal conditioning control by setting t_o'=T to marginalize video. Motus (Dec 2025) uses a similar UniDiffuser-style architecture. X-WAM (April 2026) uses asynchronous noise sampling across modalities. Vid2World (ICLR 2026) applies CFG in the action→video direction for video quality. DreamZero (Feb 2026) uses parallelized CFG for real-time inference. No work systematically applies or evaluates cross-modal CFG in the video→action direction for action quality or robustness improvement under perturbation. **Training-free guidance methods:** ICG (ICLR 2025) provides CFG-quality guidance on any pretrained conditional model using independent/random conditions, without dropout training — validated on image generation but not cross-modal robot control. **CFG Theory:** CPC decomposition (NeurIPS 2025) proves CFG implicitly decomposes into mean-shift + positive CPC + negative CPC; explicitly notes limitations when conditional covariances lack discriminative structure — the expected case for heterogeneous video→action conditioning. **SVD-based guidance filtering:** DiffStateGrad (ICLR 2025) projects measurement gradients onto SVD subspaces for image restoration. Related SVD approaches exist for controllable editing (Feb 2025) and concept removal (March 2025). All operate in single-modal image settings; none address cross-modal guidance for robot control. **Geometric robustness methods (competitors):** OA-WAM (May 2026): object-addressable architecture, Geo-Avg 84.3% (Camera 80.5%, Robot 89.6%) — requires architectural modification. CKT-WAM (May 2026): parameter-efficient context transfer, total 86.1% (Camera 77.4%, Robot 71.4%) — requires additional training. Being-H0.7 (May 2026): latent world-action queries with posterior alignment, 82.1% zero-shot / 84.8% fine-tuned — uses implicit world modeling without explicit video branch. π0.5: 85.7% total. AnyCamVLA (March 2026): zero-shot camera adaptation via feed-forward novel view synthesis, training-free but VLA-specific and camera-only. ADPro (2025): test-time adaptive diffusion policy via manifold-constrained denoising, evaluated on RLBench/CALVIN but not LIBERO-Plus. GPC (Feb 2025): inference-time enhancement via predictive world model look-ahead, requires a separately trained world model. **Selective world-model usage:** WoG (Feb 2026) compresses world predictions via learned Q-Former — requires retraining. FFDC (May 2026) decides WHEN to replan, not HOW MUCH or WHICH influence to apply within denoising. **Gap:** No existing work (1) applies cross-modal CFG in the video→action direction of WAMs with systematic evaluation under geometric perturbation, (2) uses spectral filtering to selectively amplify action-relevant components of the cross-modal guidance signal, or (3) provides a training-free, architecture-agnostic method targeting WAM geometric robustness specifically.\",\n  \"approach\": \"We propose Spectral Cross-Modal Guidance (SCG), a training-free inference-time method for selectively amplifying action-relevant world knowledge in WAMs, targeting geometric robustness. The approach is structured in two phases: a diagnostic phase establishing whether cross-modal guidance carries useful signal under perturbation, and a method phase applying spectral filtering if signal exists.\\n\\n**Phase 1 — Cross-Modal Guidance Diagnostics (primary empirical contribution).** Before spectral filtering, we answer the foundational question: does amplifying video→action guidance improve WAM robustness under geometric perturbation? Using UWM's independent timestep mechanism, we compute the guidance vector g_t = ε(a; t_a, t_o'=t_a) − ε(a; t_a, t_o'=T) at each action denoising step t. The first term uses joint denoising (video and action at matched noise levels, exchanging information through shared attention); the second marginalizes video by setting t_o'=T (pure noise). The guided prediction: ε_guided = ε_marginal + w·g_t. We sweep w ∈ {1.0, 1.5, 2.0, 3.0, 5.0} on both standard LIBERO (sanity check — expect no benefit, confirming video dispensability under standard conditions) and LIBERO-Plus geometric perturbations (camera, robot-init at L1/L3 difficulty). This takes ~25-30h H100 and definitively answers whether guidance carries signal. If uniform CFG shows zero improvement under geometric perturbation at all scales, the paper pivots to a diagnostic/negative-result contribution analyzing what video branches encode vs. what geometric robustness requires.\\n\\n**Phase 2 — Spectral Filtering with Action Quality Correlation (method contribution, contingent on Phase 1).** If Phase 1 reveals that uniform CFG helps (or helps inconsistently — improving some perturbation types but hurting others), we apply spectral filtering to selectively amplify beneficial components. Collect guidance vectors {g_t} across a calibration set (~100 trajectories from LIBERO training data) at each of K=10 denoising steps. For each step t, compute the SVD of the guidance covariance C_t = (1/N)Σ g_t g_t^T = U_t Λ_t U_t^T. For automatic component selection, compute Action Quality Correlation (AQC) for each principal direction u_i: the Spearman rank correlation between |u_i^T g_t| and action quality improvement (loss reduction) when the component is included. Retain components with AQC exceeding a permutation-null threshold (p<0.05), yielding projection Π_t. Filtered guidance: ε_guided = ε_marginal + w(t)·Π_t(g_t), where w(t) follows β-CFG timestep-adaptive scheduling. This extends DiffStateGrad's subspace projection from single-modal image restoration to cross-modal robot control, with the key difference being AQC-calibrated selection rather than state-defined projection.\\n\\n**Backbone Strategy.** Primary: UWM with released LIBERO-90 checkpoint, fine-tuned on LIBERO tasks. UWM's independent timesteps provide mathematically clean cross-modal CFG: t_o'=T gives the unconditional (video-marginalized) action score natively, with no dropout training or architectural modification needed. Secondary (extension for backbone-agnosticism): ICG applied to Fast-WAM. ICG approximates the unconditional score by conditioning on a random/independent input — for video features, this means substituting real video tokens with random embeddings sampled from a matched distribution. ICG has been validated on image diffusion models (ICLR 2025) but not cross-modal robot control; testing it here is itself a novel contribution. If ICG on Fast-WAM produces consistent results with UWM's native CFG, this demonstrates SCG's architecture-agnosticism.\\n\\n**Evaluation strategy.** Primary benchmark: LIBERO-Plus with 3 perturbation types — camera and robot-init (geometric, where video knowledge should help most), plus light as control (where WAMs already excel, expect no benefit from guidance). 2 difficulty levels (L1, L3), 2 seeds. Standard LIBERO as sanity check. Baselines: (i) UWM standard policy (t_o'=T, no guidance), (ii) UWM joint denoising (t_o'=t_a, no guidance amplification — equivalent to CFG w=1.0), (iii) Uniform cross-modal CFG (w>1), (iv) SCG with AQC spectral filtering (ours). Ablations: (a) AQC threshold sensitivity, (b) per-step vs. global SVD, (c) cross-task transfer of calibrated subspace (calibrate on LIBERO tasks A, evaluate on tasks B), (d) AQC-selected directions vs. top-variance directions (testing whether action-relevant ≠ high-variance), (e) ICG on Fast-WAM vs. UWM native CFG (backbone comparison). Framing vs. OA-WAM: SCG is training-free and architecture-agnostic, complementary to OA-WAM's architectural approach. We explicitly frame SCG as applicable to any WAM with video/action branches, including potentially OA-WAM itself if its checkpoint becomes available.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~100-140h H100\",\n      \"gpu_utilization\": \"Low-moderate (25-35%). Human sets up UWM + LIBERO-Plus integration, fine-tunes UWM, implements cross-modal CFG and SVD pipeline, runs evaluation sweeps.\",\n      \"timeline\": \"2.5-3 weeks (feasible for CoRL abstract May 26, paper May 29)\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"$250-420 (at ~$2.50-3.00/H100-hr spot pricing, May 2026)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~110-160h H100\",\n      \"gpu_utilization\": \"Moderate-high (55-70%). Agent implements cross-modal CFG on UWM, integrates LIBERO-Plus, queues Phase 1 diagnostic sweeps. Human reviews Phase 1 results to decide Phase 2 (~1hr at decision point, then ~30min/day).\",\n      \"timeline\": \"14-18 days (targets CoRL 2026 abstract May 26, paper May 29)\",\n      \"team\": \"1 researcher, ~30-45min/day\",\n      \"claude_api_cost\": \"$100-250 (estimated ~1000-2500 Opus turns)\",\n      \"estimated_gpu_cost\": \"$275-480\",\n      \"risk_note\": \"Primary risk is UWM fine-tuning achieving competitive LIBERO performance. UWM's released LIBERO-90 checkpoint and fine-tuning code reduce this risk. Phase 1 diagnostic is quick (~25-30h) and provides go/no-go signal for Phase 2.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~130-200h H100\",\n      \"gpu_utilization\": \"High (>85%). Agent runs continuous Phase 1 diagnostic → Phase 2 calibration → evaluation loop.\",\n      \"timeline\": \"10-14 days with 2-4 GPUs concurrently\",\n      \"team\": \"0 (initial setup only, ~2 hours)\",\n      \"claude_api_cost\": \"$180-400 (estimated ~1800-4000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$325-600\",\n      \"speed_bottleneck\": \"Phase 1 must complete before Phase 2 begins. Phase 1: ~25-30h across 3 perturbation types × 5 CFG scales × 2 difficulties × 2 seeds = 60 configs. Phase 2: ~40-60h for SVD calibration + SCG evaluation.\",\n      \"risk_note\": \"Agent must correctly interpret Phase 1 results (is there signal?) before proceeding. Human review of Phase 1 results recommended even in auto mode. UWM fine-tuning failure would require fallback to ICG-on-Fast-WAM.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract May 26, paper May 29 — PRIMARY TARGET; 16-19 days; Phase 1 diagnostic is achievable within first week, Phase 2 within second; tight but feasible with UWM checkpoint and focused scope)\",\n    \"AAAI 2027 (deadline Aug 2, 2026 — secondary target if CoRL revision needed; allows ICG-on-Fast-WAM extension, additional WAM backbones, full LIBERO-Plus sweep across all 7 perturbation types)\",\n    \"ICLR 2027 (deadline Sep 24, 2026 — fallback; allows comprehensive multi-backbone study, deeper mechanistic analysis, and potential integration with OA-WAM)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets [UWM] (RSS 2025) — PRIMARY BACKBONE; independent diffusion timesteps for video/action natively enable cross-modal CFG by setting t_o'=T to marginalize video; released LIBERO-90 checkpoint with fine-tuning code\",\n    \"No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models [ICG] (ICLR 2025) — Independent Condition Guidance enables CFG on any pretrained conditional model without dropout training; backbone-agnostic complement to UWM; uses random/independent conditions to approximate unconditional score\",\n    \"Towards Understanding the Mechanisms of Classifier-Free Guidance [CPC Theory] (NeurIPS 2025) — proves CFG implicitly decomposes into selective amplification (positive CPC) and suppression (negative CPC); limited to class-conditional settings with well-separated covariance structures\",\n    \"Diffusion State-Guided Projected Gradient for Inverse Problems [DiffStateGrad] (ICLR 2025) — SVD-based subspace projection in diffusion models for image inverse problems; key methodological predecessor; single-modal, external gradient projection\",\n    \"Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv March 2026) — demonstrates video dispensable at inference under STANDARD conditions; secondary backbone candidate via ICG; NOTE: does NOT support native CFG via dropout training (corrected from prior version)\",\n    \"Do World Action Models Generalize Better than VLAs? A Robustness Study (arXiv March 2026) — WAMs weak on geometric perturbations; camera 60-80%, robot-init 63-90%; motivates the robustness focus\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (arXiv 2025) — 7-dimension perturbation benchmark with L1-L5 difficulty levels\",\n    \"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv May 2026) — LIBERO-Plus Geo-Avg SOTA at 84.3% (Camera 80.5%, Robot 89.6%); requires architectural modification; SCG is complementary (training-free, architecture-agnostic)\",\n    \"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models (arXiv May 2026) — LIBERO-Plus total SOTA at 86.1% (Camera 77.4%, Robot 71.4%); requires additional training\",\n    \"Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv May 2026) — LIBERO standard SOTA at 99.2%; LIBERO-Plus 82.1% zero-shot / 84.8% fine-tuned; uses latent world-action queries without explicit video branch\",\n    \"AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models (arXiv March 2026) — training-free camera adaptation via novel view synthesis; VLA-specific, camera-perturbation-only; complementary approach\",\n    \"ADPro: Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising (2025) — test-time adaptation via geometric manifold constraints; evaluated on RLBench/CALVIN, not LIBERO-Plus; related inference-time approach\",\n    \"Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling [GPC] (RA-L 2025) — augments frozen diffusion policy with separately trained world model for inference-time look-ahead; requires additional world model training; SCG uses built-in video branch instead\",\n    \"Classifier-Free Diffusion Guidance (NeurIPS 2021 Workshop) — foundational CFG technique\",\n    \"Classifier-free Guidance with Adaptive Scaling [β-CFG] (arXiv Feb 2025) — timestep-adaptive guidance scheduling\",\n    \"Vid2World: Crafting Video Diffusion Models to Interactive World Models (ICLR 2026) — CFG in action→video direction\",\n    \"GigaWorld-Policy: An Efficient Action-Centered World-Action Model (arXiv March 2026) — causal masking prevents video→action flow\",\n    \"MotuBrain: An Advanced World Action Model for Robot Control (arXiv April 2026) — KV cache for video features\",\n    \"When to Trust Imagination: Adaptive Action Execution for World Action Models [FFDC] (arXiv May 2026) — confidence-based replanning at execution level; orthogonal\",\n    \"World Guidance: World Modeling in Condition Space for Action Generation [WoG] (arXiv Feb 2026) — learned world-model compression; requires retraining\",\n    \"X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (arXiv April 2026) — asynchronous noise sampling across modalities; depth prediction for 3D awareness; potential alternative backbone with independent timestep control\",\n    \"DreamZero: World Action Models are Zero-shot Policies (arXiv Feb 2026) — parallelized CFG in WAM inference\",\n    \"Motus: A Unified Latent Action World Model (arXiv Dec 2025) — UniDiffuser-style WAM; potential alternative backbone\",\n    \"One Transformer Fits All Distributions in Multi-Modal Diffusion [UniDiffuser] (ICML 2023) — foundational independent timestep mechanism\",\n    \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control (arXiv Jan 2026) — LIBERO-Plus 82.2%\",\n    \"Mechanistic Dissection of Cross-Attention Subspaces in Text-to-Image Diffusion Models (AAAI 2025) — SVD-based spectral analysis of concept-encoding subspaces\",\n    \"Test-Time Perturbation Learning with Delayed Feedback for VLA Models [TTPL] (arXiv April 2026) — verifier-free test-time adaptation; complementary approach\"\n  ],\n  \"description\": \"We propose Spectral Cross-Modal Guidance (SCG), a training-free inference-time method that selectively amplifies action-relevant world knowledge from the video branch of World-Action Models (WAMs), targeting robustness under geometric perturbations (camera viewpoint, robot initial state). The work is structured as a two-phase investigation. Phase 1 (diagnostic): WAMs achieve near-perfect standard benchmark performance (Fast-WAM 97.6%, Being-H0.7 99.2%) but remain brittle under geometric perturbation (OA-WAM Camera 80.5%, CKT-WAM Camera 77.4%). Multiple works show video features are dispensable at inference under standard conditions — but none test whether amplifying video→action guidance helps under geometric perturbation, where the action branch's learned visual-motor mappings break and the video branch's spatial reasoning could compensate. We use UWM's (RSS 2025) independent timestep mechanism — setting video timestep t_o'=T marginalizes video, giving the unconditional action score; t_o'&lt;T gives the video-conditioned score — to natively enable cross-modal CFG without dropout training or architectural modification. A systematic CFG scale sweep across LIBERO-Plus geometric perturbations answers whether guidance carries action-relevant signal. CRITICAL CORRECTION from prior version: Fast-WAM was previously claimed to support native CFG via video feature dropout, but this is unverified — the paper never mentions dropout training, uses CFG scale 1.0 (no amplification), and 'uncond' in checkpoint names refers to unconditional inference mode. UWM's independent timesteps provide the principled alternative. Phase 2 (method): If Phase 1 reveals signal, SCG applies SVD-based spectral filtering to the guidance vector g_t = ε_cond − ε_uncond, retaining only directions whose Action Quality Correlation (AQC) — Spearman correlation between projection magnitude and action quality improvement — exceeds a permutation-null threshold. This makes component selection automatic and parameter-free, extending DiffStateGrad's subspace projection from single-modal image restoration to cross-modal robot control with action-quality calibration. For backbone-agnosticism, we additionally test Independent Condition Guidance (ICG, ICLR 2025), which approximates unconditional scores via random conditions on any pretrained model, applied to Fast-WAM. SCG is complementary to OA-WAM (requires architectural modification) and CKT-WAM (requires additional training) — it is training-free, architecture-agnostic, and could be applied on top of these methods. Both phases contribute: Phase 1 provides the first empirical evidence on whether/when world knowledge helps under geometric perturbation (resolving the video-dispensability paradox); Phase 2 provides a practical method for selective guidance when signal exists. If Phase 1 shows no signal, the diagnostic finding itself — that video branches encode information irrelevant to geometric robustness despite encoding spatial features — is a significant negative result that redirects the field away from guidance-based approaches.\",\n  \"project_name\": \"spectral_cross_modal_guidance_wam\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"UWM BASELINE IS 79% AFTER FINE-TUNING — NOT PRETRAINING (CRITICAL): The proposal treats UWM's released LIBERO-90 checkpoint as needing task-specific fine-tuning to reach competitive performance. However, UWM's Table II (arXiv 2504.02792) shows 79% average IS the fine-tuned result (10K gradient steps), with individual tasks ranging 65-93%. This is 20 points below SOTA (Fast-WAM 97.6%, Being-H0.7 99.2%). Even if SCG improves UWM by 10% under geometric perturbation, the absolute numbers will likely remain below OA-WAM's 84.3% geo-avg — and OA-WAM starts from a much stronger standard-LIBERO baseline. CoRL reviewers will immediately question why the backbone is 20 points below contemporary WAMs.\", \"NO LIBERO-PLUS EVALUATION OF UWM EXISTS — BASELINE PERFORMANCE COMPLETELY UNKNOWN: UWM has never been evaluated on LIBERO-Plus. Given its 79% on standard LIBERO, it could plausibly score 40-60% under geometric perturbation. Even a large SCG improvement (e.g., +15%) would leave absolute performance at 55-75%, far below OA-WAM (Camera 80.5%, Robot 89.6%). The proposal must establish UWM's LIBERO-Plus baseline before any SCG work — this takes 5-10h but the results are completely unpredictable and could invalidate the entire experimental plan.\", \"ICG-ON-FAST-WAM AS SECONDARY BACKBONE DOESN'T SOLVE THE PROBLEM: Fast-WAM achieves 97.6% on standard LIBERO, making it a strong baseline candidate. But ICG has never been validated on cross-modal robot control — only on image generation. If ICG produces noisy unconditional estimates on Fast-WAM (likely, since Fast-WAM was not designed for any form of unconditional prediction), the guidance vectors will be unreliable. The proposal correctly notes this as 'itself a novel contribution' but underestimates the risk of it simply not working.\", \"PHASE 1 NULL RESULT DOES NOT SATISFY USER'S METHOD ONLY REQUIREMENT: If Phase 1 shows video→action guidance carries no useful signal under perturbation (40-60% probability given existing evidence), the paper becomes a diagnostic/negative-result contribution. The user explicitly requires 'METHOD ONLY — new inference algorithm.' A negative diagnostic finding, while scientifically valuable, does not meet this constraint and would not satisfy a method-focused CoRL submission.\", \"X-WAM (April 2026) CRITIQUES UWM'S INDEPENDENT TIMESTEP MECHANISM: X-WAM (arXiv 2604.26694) argues that independent timestep sampling creates train/test distribution mismatch, introducing training configurations (t_O < t_a) that never occur at inference. While X-WAM's own ablation shows action quality is barely affected (67.2 vs 67.8 success rate), this architectural concern should be acknowledged. More importantly, X-WAM's Asynchronous Noise Sampling is an alternative mechanism for cross-modal timestep control that should be discussed as a potential alternative backbone.\", \"CALIBRATION TRANSFERABILITY REMAINS UNADDRESSED AFTER TWO ROUNDS OF FEEDBACK: AQC requires ~100 trajectory calibration per task. The proposal mentions cross-task transfer as an ablation but never addresses whether it's realistic. LIBERO has 90+ tasks — if per-task recalibration is needed, the practical overhead is substantial. Previous rounds 4 and 5 both flagged this; the proposal should present a concrete hypothesis about transferability or acknowledge the limitation.\"]\nFeedback: The proposal has reached a well-structured, intellectually honest state — the Fast-WAM correction, CPC theory engagement, and two-phase design are commendable. But the UWM baseline problem is now the critical blocker. Here's how to fix it:\n\n**1. RESOLVE THE BACKBONE CRISIS (BLOCKER):** UWM's 79% fine-tuned LIBERO performance is not competitive. Three options:\n\n(a) **Reframe as a proof-of-concept:** Explicitly acknowledge UWM's weaker standard performance and argue that the METHOD is the contribution, not the absolute numbers. Frame as: 'SCG provides X% relative improvement over UWM's own baseline under geometric perturbation, demonstrating the principle of spectral cross-modal guidance. The method is architecture-agnostic and can be applied to stronger WAMs as they release checkpoints.' This is the fastest path but weakest framing.\n\n(b) **Fine-tune UWM more aggressively:** UWM's paper uses 10K steps. Try 50K-100K steps with learning rate sweep — the 180M parameter model is small enough that extended fine-tuning costs only ~10-20h H100 total. If this pushes standard LIBERO to >90%, the baseline becomes acceptable. Check if the UWM repo has any community fine-tuning recipes that achieve better performance.\n\n(c) **Switch to Motus/MotuBrain as backbone:** Motus uses the same UniDiffuser-style independent timesteps as UWM and achieves much stronger performance. MotuBrain (April 2026) reports strong LIBERO results. Check if Motus/MotuBrain checkpoints and LIBERO evaluation code are available — if so, SCG can be applied identically since both use independent timestep marginalization. This is the strongest option if checkpoints exist.\n\n**2. ADD A PHASE-1-INDEPENDENT METHOD GUARANTEE:** To satisfy the METHOD ONLY requirement regardless of Phase 1 outcome, frame SCG as a general 'Spectral Guidance Filtering' framework: even if uniform CFG shows zero benefit, the spectral analysis reveals which guidance dimensions are noise vs. signal, enabling 'sparse guidance' that runs faster (fewer effective dimensions → cheaper guidance computation). This gives a practical speedup contribution independent of robustness improvement.\n\n**3. ADDRESS CALIBRATION TRANSFERABILITY CONCRETELY:** Add a specific experiment: calibrate AQC on 3 LIBERO tasks, evaluate on 3 held-out tasks. If the top-k spectral components are consistent (cosine similarity of selected subspaces >0.8), claim transferability. If not, acknowledge per-task calibration as a limitation but note it requires only ~100 trajectories (~10 minutes of data collection) vs. OA-WAM/CKT-WAM's hours of retraining.\n\n**4. CITE AND DISCUSS X-WAM'S CRITIQUE:** Acknowledge X-WAM's concern about independent timestep sampling but cite their own ablation showing action quality is barely affected. This strengthens the argument for using UWM's marginalization mechanism.\n\n**5. CONSIDER NARROWING TO CAMERA PERTURBATION ONLY:** Camera viewpoint is the perturbation type where video spatial features are most obviously relevant (the camera change directly affects the visual-spatial mapping). Robot initial state is more ambiguous. Focusing Phase 1 on camera perturbation reduces evaluation cost and gives the strongest prior for finding a positive signal.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.0 到 3.2，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T19:54:21.641Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T19:54:21.641Z",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

## Round 1

109 recorded events

### User

_source line 3 · 2026-05-10T19:54:21.680Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Spectral Cross-Modal Guidance: Training-Free Selective Amplification of World Knowledge for Robust Action Generation",
  "core_problem": "World-Action Models (WAMs) achieve near-saturated performance on standard manipulation benchmarks (Being-H0.7: 99.2%, Fast-WAM: 97.6% on LIBERO) but remain brittle under geometric perturbations — camera viewpoint and robot initial state changes cause drops to 60–90% on LIBERO-Plus. Concurrently, Fast-WAM, GigaWorld-Policy, and MotuBrain demonstrate that video features are dispensable at inference under standard conditions. These facts appear contradictory: if video-encoded spatial knowledge is dispensable, why do WAMs fail precisely under geometric perturbations where spatial reasoning should matter most? We hypothesize the resolution lies in HOW video information is used, not WHETHER it is used. Under standard conditions, the action branch encodes sufficient visual-motor mappings from the training distribution, making video features redundant. Under geometric perturbation, these mappings break — and the video branch's spatial reasoning could compensate, but only if the video→action guidance signal is properly amplified and filtered. Standard classifier-free guidance (CFG) in diffusion models amplifies all conditional contributions equally, mixing action-relevant spatial information with irrelevant appearance features. CPC theory (NeurIPS 2025) proves CFG implicitly performs selective amplification via contrastive principal components, but only in class-conditional settings with well-separated covariance structures — not in heterogeneous cross-modal settings like video→action guidance. The core question: can explicit spectral filtering of the cross-modal guidance signal selectively amplify geometric/spatial components that improve robustness while suppressing components that add noise? Before answering this, a prior diagnostic question must be settled: does cross-modal guidance in WAMs carry any action-relevant signal at all under geometric perturbation? No existing work has tested this.",
  "opportunity": "Three converging developments create a precise research opportunity, and a critical correction from the prior proposal version enables a more principled approach: (1) UWM (RSS 2025) uses UniDiffuser-style independent diffusion timesteps for video and action modalities — setting the video timestep t_o'=T marginalizes video information, yielding the unconditional action score, while t_o'&lt;T yields the video-conditioned action score. This natively enables cross-modal CFG through two forward passes without any dropout training, architectural modification, or fine-tuning. UWM releases a pretrained LIBERO-90 checkpoint. (2) LIBERO-Plus and the WAM robustness study (March 2026) reveal that geometric perturbations remain the dominant failure mode: OA-WAM Geo-Avg 84.3% (Camera 80.5%, Robot 89.6%), CKT-WAM (Camera 77.4%, Robot 71.4%), with the overall LIBERO-Plus SOTA at 86.1% (CKT-WAM). Crucially, all geometric robustness improvements to date (OA-WAM, CKT-WAM) require architectural modification or additional training — no training-free inference-time method has been attempted. (3) Independent Condition Guidance (ICG, ICLR 2025) demonstrates that CFG-quality guidance can be obtained from any pretrained conditional model without dropout training, by substituting the unconditional score with a prediction conditioned on a random/independent input. This enables cross-modal guidance on WAMs like Fast-WAM that were not trained with video dropout. (4) DiffStateGrad (ICLR 2025) establishes SVD-based subspace projection for filtering diffusion guidance signals, but only in single-modal image restoration. CRITICAL CORRECTION: The prior version incorrectly claimed Fast-WAM was trained with unconditional video feature dropout enabling native CFG. After verification — reading the full paper, project page, and GitHub — this claim is unsupported. Fast-WAM uses CFG scale 1.0 (no guidance amplification), and 'uncond' in checkpoint names refers to its unconditional inference mode (no future video denoising), not CFG-enabling dropout training. UWM's independent timestep mechanism provides the principled alternative, with ICG as a backbone-agnostic complement.",
  "landscape": "**Video-at-inference in WAMs:** Fast-WAM (March 2026) removes video denoising at inference, retaining only backbone features. GigaWorld-Policy (March 2026) uses causal masking to block video→action flow. MotuBrain (April 2026) freezes video branch and caches KV pairs. All use binary approaches (all or no video features) and evaluate only on standard benchmarks — none test under geometric perturbation. **Cross-modal CFG support in WAMs:** UWM (RSS 2025) uses independent diffusion timesteps for video and action, enabling native cross-modal conditioning control by setting t_o'=T to marginalize video. Motus (Dec 2025) uses a similar UniDiffuser-style architecture. X-WAM (April 2026) uses asynchronous noise sampling across modalities. Vid2World (ICLR 2026) applies CFG in the action→video direction for video quality. DreamZero (Feb 2026) uses parallelized CFG for real-time inference. No work systematically applies or evaluates cross-modal CFG in the video→action direction for action quality or robustness improvement under perturbation. **Training-free guidance methods:** ICG (ICLR 2025) provides CFG-quality guidance on any pretrained conditional model using independent/random conditions, without dropout training — validated on image generation but not cross-modal robot control. **CFG Theory:** CPC decomposition (NeurIPS 2025) proves CFG implicitly decomposes into mean-shift + positive CPC + negative CPC; explicitly notes limitations when conditional covariances lack discriminative structure — the expected case for heterogeneous video→action conditioning. **SVD-based guidance filtering:** DiffStateGrad (ICLR 2025) projects measurement gradients onto SVD subspaces for image restoration. Related SVD approaches exist for controllable editing (Feb 2025) and concept removal (March 2025). All operate in single-modal image settings; none address cross-modal guidance for robot control. **Geometric robustness methods (competitors):** OA-WAM (May 2026): object-addressable architecture, Geo-Avg 84.3% (Camera 80.5%, Robot 89.6%) — requires architectural modification. CKT-WAM (May 2026): parameter-efficient context transfer, total 86.1% (Camera 77.4%, Robot 71.4%) — requires additional training. Being-H0.7 (May 2026): latent world-action queries with posterior alignment, 82.1% zero-shot / 84.8% fine-tuned — uses implicit world modeling without explicit video branch. π0.5: 85.7% total. AnyCamVLA (March 2026): zero-shot camera adaptation via feed-forward novel view synthesis, training-free but VLA-specific and camera-only. ADPro (2025): test-time adaptive diffusion policy via manifold-constrained denoising, evaluated on RLBench/CALVIN but not LIBERO-Plus. GPC (Feb 2025): inference-time enhancement via predictive world model look-ahead, requires a separately trained world model. **Selective world-model usage:** WoG (Feb 2026) compresses world predictions via learned Q-Former — requires retraining. FFDC (May 2026) decides WHEN to replan, not HOW MUCH or WHICH influence to apply within denoising. **Gap:** No existing work (1) applies cross-modal CFG in the video→action direction of WAMs with systematic evaluation under geometric perturbation, (2) uses spectral filtering to selectively amplify action-relevant components of the cross-modal guidance signal, or (3) provides a training-free, architecture-agnostic method targeting WAM geometric robustness specifically.",
  "approach": "We propose Spectral Cross-Modal Guidance (SCG), a training-free inference-time method for selectively amplifying action-relevant world knowledge in WAMs, targeting geometric robustness. The approach is structured in two phases: a diagnostic phase establishing whether cross-modal guidance carries useful signal under perturbation, and a method phase applying spectral filtering if signal exists.\n\n**Phase 1 — Cross-Modal Guidance Diagnostics (primary empirical contribution).** Before spectral filtering, we answer the foundational question: does amplifying video→action guidance improve WAM robustness under geometric perturbation? Using UWM's independent timestep mechanism, we compute the guidance vector g_t = ε(a; t_a, t_o'=t_a) − ε(a; t_a, t_o'=T) at each action denoising step t. The first term uses joint denoising (video and action at matched noise levels, exchanging information through shared attention); the second marginalizes video by setting t_o'=T (pure noise). The guided prediction: ε_guided = ε_marginal + w·g_t. We sweep w ∈ {1.0, 1.5, 2.0, 3.0, 5.0} on both standard LIBERO (sanity check — expect no benefit, confirming video dispensability under standard conditions) and LIBERO-Plus geometric perturbations (camera, robot-init at L1/L3 difficulty). This takes ~25-30h H100 and definitively answers whether guidance carries signal. If uniform CFG shows zero improvement under geometric perturbation at all scales, the paper pivots to a diagnostic/negative-result contribution analyzing what video branches encode vs. what geometric robustness requires.\n\n**Phase 2 — Spectral Filtering with Action Quality Correlation (method contribution, contingent on Phase 1).** If Phase 1 reveals that uniform CFG helps (or helps inconsistently — improving some perturbation types but hurting others), we apply spectral filtering to selectively amplify beneficial components. Collect guidance vectors {g_t} across a calibration set (~100 trajectories from LIBERO training data) at each of K=10 denoising steps. For each step t, compute the SVD of the guidance covariance C_t = (1/N)Σ g_t g_t^T = U_t Λ_t U_t^T. For automatic component selection, compute Action Quality Correlation (AQC) for each principal direction u_i: the Spearman rank correlation between |u_i^T g_t| and action quality improvement (loss reduction) when the component is included. Retain components with AQC exceeding a permutation-null threshold (p<0.05), yielding projection Π_t. Filtered guidance: ε_guided = ε_marginal + w(t)·Π_t(g_t), where w(t) follows β-CFG timestep-adaptive scheduling. This extends DiffStateGrad's subspace projection from single-modal image restoration to cross-modal robot control, with the key difference being AQC-calibrated selection rather than state-defined projection.\n\n**Backbone Strategy.** Primary: UWM with released LIBERO-90 checkpoint, fine-tuned on LIBERO tasks. UWM's independent timesteps provide mathematically clean cross-modal CFG: t_o'=T gives the unconditional (video-marginalized) action score natively, with no dropout training or architectural modification needed. Secondary (extension for backbone-agnosticism): ICG applied to Fast-WAM. ICG approximates the unconditional score by conditioning on a random/independent input — for video features, this means substituting real video tokens with random embeddings sampled from a matched distribution. ICG has been validated on image diffusion models (ICLR 2025) but not cross-modal robot control; testing it here is itself a novel contribution. If ICG on Fast-WAM produces consistent results with UWM's native CFG, this demonstrates SCG's architecture-agnosticism.\n\n**Evaluation strategy.** Primary benchmark: LIBERO-Plus with 3 perturbation types — camera and robot-init (geometric, where video knowledge should help most), plus light as control (where WAMs already excel, expect no benefit from guidance). 2 difficulty levels (L1, L3), 2 seeds. Standard LIBERO as sanity check. Baselines: (i) UWM standard policy (t_o'=T, no guidance), (ii) UWM joint denoising (t_o'=t_a, no guidance amplification — equivalent to CFG w=1.0), (iii) Uniform cross-modal CFG (w>1), (iv) SCG with AQC spectral filtering (ours). Ablations: (a) AQC threshold sensitivity, (b) per-step vs. global SVD, (c) cross-task transfer of calibrated subspace (calibrate on LIBERO tasks A, evaluate on tasks B), (d) AQC-selected directions vs. top-variance directions (testing whether action-relevant ≠ high-variance), (e) ICG on Fast-WAM vs. UWM native CFG (backbone comparison). Framing vs. OA-WAM: SCG is training-free and architecture-agnostic, complementary to OA-WAM's architectural approach. We explicitly frame SCG as applicable to any WAM with video/action branches, including potentially OA-WAM itself if its checkpoint becomes available.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~100-140h H100",
      "gpu_utilization": "Low-moderate (25-35%). Human sets up UWM + LIBERO-Plus integration, fine-tunes UWM, implements cross-modal CFG and SVD pipeline, runs evaluation sweeps.",
      "timeline": "2.5-3 weeks (feasible for CoRL abstract May 26, paper May 29)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$250-420 (at ~$2.50-3.00/H100-hr spot pricing, May 2026)"
    },
    "human_in_loop": {
      "gpu_hours": "~110-160h H100",
      "gpu_utilization": "Moderate-high (55-70%). Agent implements cross-modal CFG on UWM, integrates LIBERO-Plus, queues Phase 1 diagnostic sweeps. Human reviews Phase 1 results to decide Phase 2 (~1hr at decision point, then ~30min/day).",
      "timeline": "14-18 days (targets CoRL 2026 abstract May 26, paper May 29)",
      "team": "1 researcher, ~30-45min/day",
      "claude_api_cost": "$100-250 (estimated ~1000-2500 Opus turns)",
      "estimated_gpu_cost": "$275-480",
      "risk_note": "Primary risk is UWM fine-tuning achieving competitive LIBERO performance. UWM's released LIBERO-90 checkpoint and fine-tuning code reduce this risk. Phase 1 diagnostic is quick (~25-30h) and provides go/no-go signal for Phase 2."
    },
    "auto_research": {
      "gpu_hours": "~130-200h H100",
      "gpu_utilization": "High (>85%). Agent runs continuous Phase 1 diagnostic → Phase 2 calibration → evaluation loop.",
      "timeline": "10-14 days with 2-4 GPUs concurrently",
      "team": "0 (initial setup only, ~2 hours)",
      "claude_api_cost": "$180-400 (estimated ~1800-4000 Opus turns)",
      "estimated_gpu_cost": "$325-600",
      "speed_bottleneck": "Phase 1 must complete before Phase 2 begins. Phase 1: ~25-30h across 3 perturbation types × 5 CFG scales × 2 difficulties × 2 seeds = 60 configs. Phase 2: ~40-60h for SVD calibration + SCG evaluation.",
      "risk_note": "Agent must correctly interpret Phase 1 results (is there signal?) before proceeding. Human review of Phase 1 results recommended even in auto mode. UWM fine-tuning failure would require fallback to ICG-on-Fast-WAM."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract May 26, paper May 29 — PRIMARY TARGET; 16-19 days; Phase 1 diagnostic is achievable within first week, Phase 2 within second; tight but feasible with UWM checkpoint and focused scope)",
    "AAAI 2027 (deadline Aug 2, 2026 — secondary target if CoRL revision needed; allows ICG-on-Fast-WAM extension, additional WAM backbones, full LIBERO-Plus sweep across all 7 perturbation types)",
    "ICLR 2027 (deadline Sep 24, 2026 — fallback; allows comprehensive multi-backbone study, deeper mechanistic analysis, and potential integration with OA-WAM)"
  ],
  "level": "solid",
  "key_references": [
    "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets [UWM] (RSS 2025) — PRIMARY BACKBONE; independent diffusion timesteps for video/action natively enable cross-modal CFG by setting t_o'=T to marginalize video; released LIBERO-90 checkpoint with fine-tuning code",
    "No Training, No Problem: Rethinking Classifier-Free Guidance for Diffusion Models [ICG] (ICLR 2025) — Independent Condition Guidance enables CFG on any pretrained conditional model without dropout training; backbone-agnostic complement to UWM; uses random/independent conditions to approximate unconditional score",
    "Towards Understanding the Mechanisms of Classifier-Free Guidance [CPC Theory] (NeurIPS 2025) — proves CFG implicitly decomposes into selective amplification (positive CPC) and suppression (negative CPC); limited to class-conditional settings with well-separated covariance structures",
    "Diffusion State-Guided Projected Gradient for Inverse Problems [DiffStateGrad] (ICLR 2025) — SVD-based subspace projection in diffusion models for image inverse problems; key methodological predecessor; single-modal, external gradient projection",
    "Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv March 2026) — demonstrates video dispensable at inference under STANDARD conditions; secondary backbone candidate via ICG; NOTE: does NOT support native CFG via dropout training (corrected from prior version)",
    "Do World Action Models Generalize Better than VLAs? A Robustness Study (arXiv March 2026) — WAMs weak on geometric perturbations; camera 60-80%, robot-init 63-90%; motivates the robustness focus",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (arXiv 2025) — 7-dimension perturbation benchmark with L1-L5 difficulty levels",
    "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv May 2026) — LIBERO-Plus Geo-Avg SOTA at 84.3% (Camera 80.5%, Robot 89.6%); requires architectural modification; SCG is complementary (training-free, architecture-agnostic)",
    "CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models (arXiv May 2026) — LIBERO-Plus total SOTA at 86.1% (Camera 77.4%, Robot 71.4%); requires additional training",
    "Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv May 2026) — LIBERO standard SOTA at 99.2%; LIBERO-Plus 82.1% zero-shot / 84.8% fine-tuned; uses latent world-action queries without explicit video branch",
    "AnyCamVLA: Zero-Shot Camera Adaptation for Viewpoint Robust Vision-Language-Action Models (arXiv March 2026) — training-free camera adaptation via novel view synthesis; VLA-specific, camera-perturbation-only; complementary approach",
    "ADPro: Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising (2025) — test-time adaptation via geometric manifold constraints; evaluated on RLBench/CALVIN, not LIBERO-Plus; related inference-time approach",
    "Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling [GPC] (RA-L 2025) — augments frozen diffusion policy with separately trained world model for inference-time look-ahead; requires additional world model training; SCG uses built-in video branch instead",
    "Classifier-Free Diffusion Guidance (NeurIPS 2021 Workshop) — foundational CFG technique",
    "Classifier-free Guidance with Adaptive Scaling [β-CFG] (arXiv Feb 2025) — timestep-adaptive guidance scheduling",
    "Vid2World: Crafting Video Diffusion Models to Interactive World Models (ICLR 2026) — CFG in action→video direction",
    "GigaWorld-Policy: An Efficient Action-Centered World-Action Model (arXiv March 2026) — causal masking prevents video→action flow",
    "MotuBrain: An Advanced World Action Model for Robot Control (arXiv April 2026) — KV cache for video features",
    "When to Trust Imagination: Adaptive Action Execution for World Action Models [FFDC] (arXiv May 2026) — confidence-based replanning at execution level; orthogonal",
    "World Guidance: World Modeling in Condition Space for Action Generation [WoG] (arXiv Feb 2026) — learned world-model compression; requires retraining",
    "X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (arXiv April 2026) — asynchronous noise sampling across modalities; depth prediction for 3D awareness; potential alternative backbone with independent timestep control",
    "DreamZero: World Action Models are Zero-shot Policies (arXiv Feb 2026) — parallelized CFG in WAM inference",
    "Motus: A Unified Latent Action World Model (arXiv Dec 2025) — UniDiffuser-style WAM; potential alternative backbone",
    "One Transformer Fits All Distributions in Multi-Modal Diffusion [UniDiffuser] (ICML 2023) — foundational independent timestep mechanism",
    "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control (arXiv Jan 2026) — LIBERO-Plus 82.2%",
    "Mechanistic Dissection of Cross-Attention Subspaces in Text-to-Image Diffusion Models (AAAI 2025) — SVD-based spectral analysis of concept-encoding subspaces",
    "Test-Time Perturbation Learning with Delayed Feedback for VLA Models [TTPL] (arXiv April 2026) — verifier-free test-time adaptation; complementary approach"
  ],
  "description": "We propose Spectral Cross-Modal Guidance (SCG), a training-free inference-time method that selectively amplifies action-relevant world knowledge from the video branch of World-Action Models (WAMs), targeting robustness under geometric perturbations (camera viewpoint, robot initial state). The work is structured as a two-phase investigation. Phase 1 (diagnostic): WAMs achieve near-perfect standard benchmark performance (Fast-WAM 97.6%, Being-H0.7 99.2%) but remain brittle under geometric perturbation (OA-WAM Camera 80.5%, CKT-WAM Camera 77.4%). Multiple works show video features are dispensable at inference under standard conditions — but none test whether amplifying video→action guidance helps under geometric perturbation, where the action branch's learned visual-motor mappings break and the video branch's spatial reasoning could compensate. We use UWM's (RSS 2025) independent timestep mechanism — setting video timestep t_o'=T marginalizes video, giving the unconditional action score; t_o'&lt;T gives the video-conditioned score — to natively enable cross-modal CFG without dropout training or architectural modification. A systematic CFG scale sweep across LIBERO-Plus geometric perturbations answers whether guidance carries action-relevant signal. CRITICAL CORRECTION from prior version: Fast-WAM was previously claimed to support native CFG via video feature dropout, but this is unverified — the paper never mentions dropout training, uses CFG scale 1.0 (no amplification), and 'uncond' in checkpoint names refers to unconditional inference mode. UWM's independent timesteps provide the principled alternative. Phase 2 (method): If Phase 1 reveals signal, SCG applies SVD-based spectral filtering to the guidance vector g_t = ε_cond − ε_uncond, retaining only directions whose Action Quality Correlation (AQC) — Spearman correlation between projection magnitude and action quality improvement — exceeds a permutation-null threshold. This makes component selection automatic and parameter-free, extending DiffStateGrad's subspace projection from single-modal image restoration to cross-modal robot control with action-quality calibration. For backbone-agnosticism, we additionally test Independent Condition Guidance (ICG, ICLR 2025), which approximates unconditional scores via random conditions on any pretrained model, applied to Fast-WAM. SCG is complementary to OA-WAM (requires architectural modification) and CKT-WAM (requires additional training) — it is training-free, architecture-agnostic, and could be applied on top of these methods. Both phases contribute: Phase 1 provides the first empirical evidence on whether/when world knowledge helps under geometric perturbation (resolving the video-dispensability paradox); Phase 2 provides a practical method for selective guidance when signal exists. If Phase 1 shows no signal, the diagnostic finding itself — that video branches encode information irrelevant to geometric robustness despite encoding spatial features — is a significant negative result that redirects the field away from guidance-based approaches.",
  "project_name": "spectral_cross_modal_guidance_wam",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["UWM BASELINE IS 79% AFTER FINE-TUNING — NOT PRETRAINING (CRITICAL): The proposal treats UWM's released LIBERO-90 checkpoint as needing task-specific fine-tuning to reach competitive performance. However, UWM's Table II (arXiv 2504.02792) shows 79% average IS the fine-tuned result (10K gradient steps), with individual tasks ranging 65-93%. This is 20 points below SOTA (Fast-WAM 97.6%, Being-H0.7 99.2%). Even if SCG improves UWM by 10% under geometric perturbation, the absolute numbers will likely remain below OA-WAM's 84.3% geo-avg — and OA-WAM starts from a much stronger standard-LIBERO baseline. CoRL reviewers will immediately question why the backbone is 20 points below contemporary WAMs.", "NO LIBERO-PLUS EVALUATION OF UWM EXISTS — BASELINE PERFORMANCE COMPLETELY UNKNOWN: UWM has never been evaluated on LIBERO-Plus. Given its 79% on standard LIBERO, it could plausibly score 40-60% under geometric perturbation. Even a large SCG improvement (e.g., +15%) would leave absolute performance at 55-75%, far below OA-WAM (Camera 80.5%, Robot 89.6%). The proposal must establish UWM's LIBERO-Plus baseline before any SCG work — this takes 5-10h but the results are completely unpredictable and could invalidate the entire experimental plan.", "ICG-ON-FAST-WAM AS SECONDARY BACKBONE DOESN'T SOLVE THE PROBLEM: Fast-WAM achieves 97.6% on standard LIBERO, making it a strong baseline candidate. But ICG has never been validated on cross-modal robot control — only on image generation. If ICG produces noisy unconditional estimates on Fast-WAM (likely, since Fast-WAM was not designed for any form of unconditional prediction), the guidance vectors will be unreliable. The proposal correctly notes this as 'itself a novel contribution' but underestimates the risk of it simply not working.", "PHASE 1 NULL RESULT DOES NOT SATISFY USER'S METHOD ONLY REQUIREMENT: If Phase 1 shows video→action guidance carries no useful signal under perturbation (40-60% probability given existing evidence), the paper becomes a diagnostic/negative-result contribution. The user explicitly requires 'METHOD ONLY — new inference algorithm.' A negative diagnostic finding, while scientifically valuable, does not meet this constraint and would not satisfy a method-focused CoRL submission.", "X-WAM (April 2026) CRITIQUES UWM'S INDEPENDENT TIMESTEP MECHANISM: X-WAM (arXiv 2604.26694) argues that independent timestep sampling creates train/test distribution mismatch, introducing training configurations (t_O < t_a) that never occur at inference. While X-WAM's own ablation shows action quality is barely affected (67.2 vs 67.8 success rate), this architectural concern should be acknowledged. More importantly, X-WAM's Asynchronous Noise Sampling is an alternative mechanism for cross-modal timestep control that should be discussed as a potential alternative backbone.", "CALIBRATION TRANSFERABILITY REMAINS UNADDRESSED AFTER TWO ROUNDS OF FEEDBACK: AQC requires ~100 trajectory calibration per task. The proposal mentions cross-task transfer as an ablation but never addresses whether it's realistic. LIBERO has 90+ tasks — if per-task recalibration is needed, the practical overhead is substantial. Previous rounds 4 and 5 both flagged this; the proposal should present a concrete hypothesis about transferability or acknowledge the limitation."]
Feedback: The proposal has reached a well-structured, intellectually honest state — the Fast-WAM correction, CPC theory engagement, and two-phase design are commendable. But the UWM baseline problem is now the critical blocker. Here's how to fix it:

**1. RESOLVE THE BACKBONE CRISIS (BLOCKER):** UWM's 79% fine-tuned LIBERO performance is not competitive. Three options:

(a) **Reframe as a proof-of-concept:** Explicitly acknowledge UWM's weaker standard performance and argue that the METHOD is the contribution, not the absolute numbers. Frame as: 'SCG provides X% relative improvement over UWM's own baseline under geometric perturbation, demonstrating the principle of spectral cross-modal guidance. The method is architecture-agnostic and can be applied to stronger WAMs as they release checkpoints.' This is the fastest path but weakest framing.

(b) **Fine-tune UWM more aggressively:** UWM's paper uses 10K steps. Try 50K-100K steps with learning rate sweep — the 180M parameter model is small enough that extended fine-tuning costs only ~10-20h H100 total. If this pushes standard LIBERO to >90%, the baseline becomes acceptable. Check if the UWM repo has any community fine-tuning recipes that achieve better performance.

(c) **Switch to Motus/MotuBrain as backbone:** Motus uses the same UniDiffuser-style independent timesteps as UWM and achieves much stronger performance. MotuBrain (April 2026) reports strong LIBERO results. Check if Motus/MotuBrain checkpoints and LIBERO evaluation code are available — if so, SCG can be applied identically since both use independent timestep marginalization. This is the strongest option if checkpoints exist.

**2. ADD A PHASE-1-INDEPENDENT METHOD GUARANTEE:** To satisfy the METHOD ONLY requirement regardless of Phase 1 outcome, frame SCG as a general 'Spectral Guidance Filtering' framework: even if uniform CFG shows zero benefit, the spectral analysis reveals which guidance dimensions are noise vs. signal, enabling 'sparse guidance' that runs faster (fewer effective dimensions → cheaper guidance computation). This gives a practical speedup contribution independent of robustness improvement.

**3. ADDRESS CALIBRATION TRANSFERABILITY CONCRETELY:** Add a specific experiment: calibrate AQC on 3 LIBERO tasks, evaluate on 3 held-out tasks. If the top-k spectral components are consistent (cosine similarity of selected subspaces >0.8), claim transferability. If not, acknowledge per-task calibration as a limitation but note it requires only ~100 trajectories (~10 minutes of data collection) vs. OA-WAM/CKT-WAM's hours of retraining.

**4. CITE AND DISCUSS X-WAM'S CRITIQUE:** Acknowledge X-WAM's concern about independent timestep sampling but cite their own ablation showing action quality is barely affected. This strengthens the argument for using UWM's marginalization mechanism.

**5. CONSIDER NARROWING TO CAMERA PERTURBATION ONLY:** Camera viewpoint is the perturbation type where video spatial features are most obviously relevant (the camera change directly affects the visual-spatial mapping). Robot initial state is more ambiguous. Focusing Phase 1 on camera perturbation reduces evaluation cost and gives the strongest prior for finding a positive signal.

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
这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.0 到 3.2，没有明显改善。

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
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "b2d13bee-0fa9-4b12-b116-7d6041973243",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T19:54:21.677Z_

```json
{
  "parentUuid": "b2d13bee-0fa9-4b12-b116-7d6041973243",
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
  "uuid": "f45b4f21-124f-4bb2-b6f3-7beb0e522dfd",
  "timestamp": "2026-05-10T19:54:21.677Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T19:54:21.677Z_

```json
{
  "parentUuid": "f45b4f21-124f-4bb2-b6f3-7beb0e522dfd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "391b8add-8ba3-48a7-addc-07b3b0c849f3",
  "timestamp": "2026-05-10T19:54:21.677Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification o…",
  "leafUuid": "391b8add-8ba3-48a7-addc-07b3b0c849f3",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revisit WAM geometric robustness via video-action alignment",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Assistant

_source line 8 · 2026-05-10T19:54:34.244Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the reviewer feedback and the current state of this research idea. The key issues are:

1. UWM baseline is only 79% after fine-tuning - not competitive
2. No LIBERO-Plus evaluation of UWM exists
3. ICG on Fast-WAM is risky
4. Phase 1 null result doesn't satisfy "METHOD ONLY" requirement
5. X-WAM critiques UWM's independent timestep mechanism
6. Calibration transferability unaddressed

The idea has been through 6 rounds with no significant improvement. Let me think deeply about whether the core approach is fundamentally viable or needs a pivot.


The core problem is real—WAMs do struggle with geometric perturbations—and the spectral filtering approach is theoretically sound, but the backbone bottleneck is crippling. UWM's 79% performance is too weak to build on, and there's no clear path to finding a stronger backbone that supports the required mechanism. With a 40-60% chance Phase 1 fails entirely, these structural issues keep resurfacing because they can't be solved through iteration alone. I need to investigate whether alternative backbones like Motus or MotuBrain are available and whether X-WAM offers a viable direction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "391b8add-8ba3-48a7-addc-07b3b0c849f3",
  "isSidechain": false,
  "requestId": "req_011CauUUnWotvxFBS6xR5vEX",
  "type": "assistant",
  "uuid": "08fe883f-5447-4b01-a5c3-c5e1b7053306",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198S7nVMJtHq3K4k2yJ7yLK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14581,
      "cache_read_input_tokens": 11804,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14581,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 512,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 14581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14581
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

_source line 9 · 2026-05-10T19:54:35.531Z_

I'll do deep research on the critical issues before deciding whether to revise or pivot. The backbone crisis (UWM at 79%) and the structural risk of Phase 1 null results suggest this idea may have fundamental viability problems after 6 rounds.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08fe883f-5447-4b01-a5c3-c5e1b7053306",
  "isSidechain": false,
  "requestId": "req_011CauUUnWotvxFBS6xR5vEX",
  "type": "assistant",
  "uuid": "f558d7c4-a94b-404a-879e-06fb84c98c35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198S7nVMJtHq3K4k2yJ7yLK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14581,
      "cache_read_input_tokens": 11804,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14581,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 512,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 14581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14581
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

_source line 10 · 2026-05-10T19:54:35.952Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VjmPhK3HJyAMRMNbRUsF3N`</summary>

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
  "parentUuid": "f558d7c4-a94b-404a-879e-06fb84c98c35",
  "isSidechain": false,
  "requestId": "req_011CauUUnWotvxFBS6xR5vEX",
  "type": "assistant",
  "uuid": "e9c61b5d-c6e9-44b9-bc4f-660e4c7102fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198S7nVMJtHq3K4k2yJ7yLK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14581,
      "cache_read_input_tokens": 11804,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14581,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 512,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 14581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14581
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

_source line 11 · 2026-05-10T19:54:35.958Z_

<details><summary>↩ Tool result · `toolu_01VjmPhK3HJyAMRMNbRUsF3N`</summary>

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
  "parentUuid": "e9c61b5d-c6e9-44b9-bc4f-660e4c7102fc",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "8a461a2a-7e32-4c7c-9691-8830b3119395",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "e9c61b5d-c6e9-44b9-bc4f-660e4c7102fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T19:54:41.405Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now do the deep research. I need to investigate:

1. Motus/MotuBrain checkpoints and LIBERO performance
2. X-WAM's architecture and whether it could be a backbone
3. Whether there are any stronger WAMs with independent timestep control that could serve as backbone
4. Alternative training-free approaches for geometric robustness in robot manipulation
5. Whether the core idea of spectral guidance filtering is viable at all given the backbone constraints

Let me search for these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a461a2a-7e32-4c7c-9691-8830b3119395",
  "isSidechain": false,
  "requestId": "req_011CauUVq6roJXjtUBoLuzY4",
  "type": "assistant",
  "uuid": "97e7035c-9cbc-49e1-aa71-c5909e61eca4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDpjPAwdEKBxYNfoYyAPSP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 26385,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 354,
          "cache_read_input_tokens": 26385,
          "cache_creation_input_tokens": 1529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1529
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

_source line 13 · 2026-05-10T19:54:41.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G6UEvbh57KhK1kn9qGH4Hc`</summary>

```json
{
  "query": "MotuBrain world action model LIBERO performance checkpoint release 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97e7035c-9cbc-49e1-aa71-c5909e61eca4",
  "isSidechain": false,
  "requestId": "req_011CauUVq6roJXjtUBoLuzY4",
  "type": "assistant",
  "uuid": "6e7ee857-a0dc-42c9-adf8-d5409e60444b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDpjPAwdEKBxYNfoYyAPSP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 26385,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 354,
          "cache_read_input_tokens": 26385,
          "cache_creation_input_tokens": 1529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1529
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

_source line 14 · 2026-05-10T19:54:42.436Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ep9LpK7AAp9TXeAtQxDWaq`</summary>

```json
{
  "query": "X-WAM asynchronous noise sampling independent timestep WAM arXiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e7ee857-a0dc-42c9-adf8-d5409e60444b",
  "isSidechain": false,
  "requestId": "req_011CauUVq6roJXjtUBoLuzY4",
  "type": "assistant",
  "uuid": "82e131f7-1802-4a33-96fc-2d317b2957b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDpjPAwdEKBxYNfoYyAPSP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 26385,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 354,
          "cache_read_input_tokens": 26385,
          "cache_creation_input_tokens": 1529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1529
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

_source line 15 · 2026-05-10T19:54:43.362Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J4Y8caSkUokuKRPk4Gwgwq`</summary>

```json
{
  "query": "Motus unified latent action world model LIBERO checkpoint github 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82e131f7-1802-4a33-96fc-2d317b2957b6",
  "isSidechain": false,
  "requestId": "req_011CauUVq6roJXjtUBoLuzY4",
  "type": "assistant",
  "uuid": "4d32ffd7-cdb3-404f-9fb7-4c946ce0ce12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDpjPAwdEKBxYNfoYyAPSP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 26385,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 354,
          "cache_read_input_tokens": 26385,
          "cache_creation_input_tokens": 1529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1529
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

_source line 16 · 2026-05-10T19:54:43.823Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GCQu6z7G6sBLZhV9QSnyLc`</summary>

```json
{
  "query": "training-free inference-time robustness improvement robot manipulation diffusion policy 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d32ffd7-cdb3-404f-9fb7-4c946ce0ce12",
  "isSidechain": false,
  "requestId": "req_011CauUVq6roJXjtUBoLuzY4",
  "type": "assistant",
  "uuid": "6f389385-4e78-4d7a-90e9-d126cc7c2e73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDpjPAwdEKBxYNfoYyAPSP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1529,
      "cache_read_input_tokens": 26385,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 354,
          "cache_read_input_tokens": 26385,
          "cache_creation_input_tokens": 1529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1529
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

_source line 17 · 2026-05-10T19:54:48.352Z_

<details><summary>↩ Tool result · `toolu_01G6UEvbh57KhK1kn9qGH4Hc`</summary>

```text
Web search results for query: "MotuBrain world action model LIBERO performance checkpoint release 2026"

Links: [{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence","url":"https://www.prnewswire.com/news-releases/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence-302757280.html"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence | RoboticsTomorrow","url":"https://www.roboticstomorrow.com/news/2026/04/29/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/26497/"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence | The Manila Times","url":"https://www.manilatimes.net/2026/04/29/tmt-newswire/pr-newswire/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/2331652"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"ShengShu Technology Unveils Motubrain: A Unified \"World Action Model\" to Solve the Robotics Scaling Problem | Humanoids Daily","url":"https://www.humanoidsdaily.com/news/shengshu-technology-unveils-motubrain-a-unified-world-action-model-to-solve-the-robotics-scaling-problem"},{"title":"ShengShu Technology Unveils World Action Model “Motubrain”: One Brain, Infinite Possibilities for Robotic Intelligence – Digital Media Net","url":"https://digitalmedianet.com/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/"},{"title":"ChinaPulse.com - ShengShu Technology Unveils World Action Model “Motubrain”: One Brain, Infinite Possibilities for Robotic Intelligence","url":"https://www.chinapulse.com/data-news/2026/04/29/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"}]

Based on the search results, here's what I found about MotuBrain and its performance on benchmarks:

## MotuBrain Overview

ShengShu Technology announced MotuBrain on April 29, 2026, a World Action Model that replaces multiple task-specific systems with a single, unified model that functions as a robotic brain for the physical world.

## Performance on Benchmarks

MotuBrain achieved a 63.77 EWM Score on WorldArena. It scored an average of 96.0 on RoboTwin 2.0 across 50 predetermined tasks, and remains the only model to exceed 95.0 in randomized environments.

## Architecture and Capabilities

MotuBrain is built on a Unified Multimodal Model that treats video and action as two continuous modalities to be learned together. A single training run gives it five capabilities at once: vision-language-action control (VLA), world modelling, video generation, inverse dynamics modelling (IDM), and joint video-action prediction.

## About LIBERO

While the search results mention LIBERO benchmarks in relation to VLA (Vision-Language-Action) model evaluation, I did not find specific information about MotuBrain's performance on LIBERO benchmarks in the results. The LIBERO benchmarks appear to be primarily used for evaluating other VLA models rather than being a focal point for MotuBrain's announced performance metrics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e7ee857-a0dc-42c9-adf8-d5409e60444b",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "43ace8bb-ff4e-45ab-9b07-ea9c803e3703",
  "toolUseResult": {
    "query": "MotuBrain world action model LIBERO performance checkpoint release 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AicAwKyJEXCGNNbWGtGgU8",
        "content": [
          {
            "title": "MotuBrain: An Advanced World Action Model for Robot Control",
            "url": "https://arxiv.org/html/2604.27792v2"
          },
          {
            "title": "ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence",
            "url": "https://www.prnewswire.com/news-releases/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence-302757280.html"
          },
          {
            "title": "ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence | RoboticsTomorrow",
            "url": "https://www.roboticstomorrow.com/news/2026/04/29/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/26497/"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          },
          {
            "title": "ShengShu Technology Unveils World Action Model \"Motubrain\": One Brain, Infinite Possibilities for Robotic Intelligence | The Manila Times",
            "url": "https://www.manilatimes.net/2026/04/29/tmt-newswire/pr-newswire/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/2331652"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "ShengShu Technology Unveils Motubrain: A Unified \"World Action Model\" to Solve the Robotics Scaling Problem | Humanoids Daily",
            "url": "https://www.humanoidsdaily.com/news/shengshu-technology-unveils-motubrain-a-unified-world-action-model-to-solve-the-robotics-scaling-problem"
          },
          {
            "title": "ShengShu Technology Unveils World Action Model “Motubrain”: One Brain, Infinite Possibilities for Robotic Intelligence – Digital Media Net",
            "url": "https://digitalmedianet.com/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/"
          },
          {
            "title": "ChinaPulse.com - ShengShu Technology Unveils World Action Model “Motubrain”: One Brain, Infinite Possibilities for Robotic Intelligence",
            "url": "https://www.chinapulse.com/data-news/2026/04/29/shengshu-technology-unveils-world-action-model-motubrain-one-brain-infinite-possibilities-for-robotic-intelligence/"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          }
        ]
      },
      "Based on the search results, here's what I found about MotuBrain and its performance on benchmarks:\n\n## MotuBrain Overview\n\nShengShu Technology announced MotuBrain on April 29, 2026, a World Action Model that replaces multiple task-specific systems with a single, unified model that functions as a robotic brain for the physical world.\n\n## Performance on Benchmarks\n\nMotuBrain achieved a 63.77 EWM Score on WorldArena. It scored an average of 96.0 on RoboTwin 2.0 across 50 predetermined tasks, and remains the only model to exceed 95.0 in randomized environments.\n\n## Architecture and Capabilities\n\nMotuBrain is built on a Unified Multimodal Model that treats video and action as two continuous modalities to be learned together. A single training run gives it five capabilities at once: vision-language-action control (VLA), world modelling, video generation, inverse dynamics modelling (IDM), and joint video-action prediction.\n\n## About LIBERO\n\nWhile the search results mention LIBERO benchmarks in relation to VLA (Vision-Language-Action) model evaluation, I did not find specific information about MotuBrain's performance on LIBERO benchmarks in the results. The LIBERO benchmarks appear to be primarily used for evaluating other VLA models rather than being a focal point for MotuBrain's announced performance metrics."
    ],
    "durationSeconds": 6.400449739
  },
  "sourceToolAssistantUUID": "6e7ee857-a0dc-42c9-adf8-d5409e60444b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T19:54:48.672Z_

<details><summary>↩ Tool result · `toolu_01Ep9LpK7AAp9TXeAtQxDWaq`</summary>

```text
Web search results for query: "X-WAM asynchronous noise sampling independent timestep WAM arXiv 2604"

Links: [{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"X-WAM: Bridging Action and 4D Synthesis | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/ai-research/2026/x-wam-bridging-action-and-4d-synthesis"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"Adaptive Non-uniform Timestep Sampling for Accelerating Diffusion Model Training","url":"https://arxiv.org/html/2411.09998v1"},{"title":"[2604.19141] Denoising, Fast and Slow: Difficulty-Aware Adaptive Sampling for Image Generation","url":"https://arxiv.org/abs/2604.19141"},{"title":"Denoising, Fast and Slow: Difficulty-Aware Adaptive Sampling for Image Generation","url":"https://arxiv.org/html/2604.19141"},{"title":"GitHub - DravenALG/awesome-vla-wam: A Curated List of Vision-Language-Action (VLA) and World Action Models (WAM) Research and Beyond · GitHub","url":"https://github.com/DravenALG/awesome-vla-wam"},{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"Exploring Time Conditioning in Diffusion Generative Models from Disjoint Noisy Data Manifolds","url":"https://arxiv.org/html/2604.25289"}]

Based on the search results, here's what I found about X-WAM and Asynchronous Noise Sampling:

## X-WAM Overview

X-WAM is a unified 4D World Action Model that simultaneously targets four objectives within a single architecture: high-fidelity video generation, 3D spatial reconstruction, high policy success rate, and efficient action execution.

## Asynchronous Noise Sampling (ANS)

ANS is proposed to jointly optimize generation quality and action decoding efficiency, applying a specialized asynchronous denoising schedule during inference, which rapidly decodes actions with fewer steps to enable efficient real-time execution, while dedicating the full sequence of steps to generate high-fidelity video.

### Training Strategy for Independent Timesteps

The key aspect of ANS related to your query about independent timesteps is this: Rather than entirely decoupling the timesteps during training, ANS samples from their joint distribution to align with the inference distribution, and instead of completely decoupling the noise timesteps of these modalities via independent random sampling, ANS systematically samples from a joint distribution of video and actions that strictly matches the test-time distribution.

The paper is published on arXiv as arXiv:2604.26694.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82e131f7-1802-4a33-96fc-2d317b2957b6",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "dc69c0b4-b102-4b9b-8e72-728b9fd0ec5f",
  "toolUseResult": {
    "query": "X-WAM asynchronous noise sampling independent timestep WAM arXiv 2604",
    "results": [
      {
        "tool_use_id": "srvtoolu_013NdaY2PeqywcGRcX2Gouos",
        "content": [
          {
            "title": "X-WAM: Unified 4D World Action Modeling from Video ...",
            "url": "https://sharinka0715.github.io/X-WAM/"
          },
          {
            "title": "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising",
            "url": "https://arxiv.org/html/2604.26694v2"
          },
          {
            "title": "X-WAM: Bridging Action and 4D Synthesis | StartupHub.ai",
            "url": "https://www.startuphub.ai/ai-news/ai-research/2026/x-wam-bridging-action-and-4d-synthesis"
          },
          {
            "title": "Fast-WAM: Do World Action Models Need Test-time Future Imagination?",
            "url": "https://arxiv.org/html/2603.16666v1"
          },
          {
            "title": "Adaptive Non-uniform Timestep Sampling for Accelerating Diffusion Model Training",
            "url": "https://arxiv.org/html/2411.09998v1"
          },
          {
            "title": "[2604.19141] Denoising, Fast and Slow: Difficulty-Aware Adaptive Sampling for Image Generation",
            "url": "https://arxiv.org/abs/2604.19141"
          },
          {
            "title": "Denoising, Fast and Slow: Difficulty-Aware Adaptive Sampling for Image Generation",
            "url": "https://arxiv.org/html/2604.19141"
          },
          {
            "title": "GitHub - DravenALG/awesome-vla-wam: A Curated List of Vision-Language-Action (VLA) and World Action Models (WAM) Research and Beyond · GitHub",
            "url": "https://github.com/DravenALG/awesome-vla-wam"
          },
          {
            "title": "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation",
            "url": "https://arxiv.org/html/2605.06481v1"
          },
          {
            "title": "Exploring Time Conditioning in Diffusion Generative Models from Disjoint Noisy Data Manifolds",
            "url": "https://arxiv.org/html/2604.25289"
          }
        ]
      },
      "Based on the search results, here's what I found about X-WAM and Asynchronous Noise Sampling:\n\n## X-WAM Overview\n\nX-WAM is a unified 4D World Action Model that simultaneously targets four objectives within a single architecture: high-fidelity video generation, 3D spatial reconstruction, high policy success rate, and efficient action execution.\n\n## Asynchronous Noise Sampling (ANS)\n\nANS is proposed to jointly optimize generation quality and action decoding efficiency, applying a specialized asynchronous denoising schedule during inference, which rapidly decodes actions with fewer steps to enable efficient real-time execution, while dedicating the full sequence of steps to generate high-fidelity video.\n\n### Training Strategy for Independent Timesteps\n\nThe key aspect of ANS related to your query about independent timesteps is this: Rather than entirely decoupling the timesteps during training, ANS samples from their joint distribution to align with the inference distribution, and instead of completely decoupling the noise timesteps of these modalities via independent random sampling, ANS systematically samples from a joint distribution of video and actions that strictly matches the test-time distribution.\n\nThe paper is published on arXiv as arXiv:2604.26694."
    ],
    "durationSeconds": 6.234240046999999
  },
  "sourceToolAssistantUUID": "82e131f7-1802-4a33-96fc-2d317b2957b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T19:54:50.438Z_

<details><summary>↩ Tool result · `toolu_01GCQu6z7G6sBLZhV9QSnyLc`</summary>

```text
Web search results for query: "training-free inference-time robustness improvement robot manipulation diffusion policy 2026"

Links: [{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"MoE-DP: An MoE-Enhanced Diffusion Policy for Robust Long-Horizon Robotic Manipulation with Skill Decomposition and Failure Recovery","url":"https://arxiv.org/html/2511.05007"},{"title":"Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising | OpenReview","url":"https://openreview.net/forum?id=YY1MPKBHp7"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .","url":"https://arxiv.org/pdf/2303.04137"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"},{"title":"[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137"},{"title":"[2510.01068] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/abs/2510.01068"},{"title":"Uncertainty Comes for Free: Human-in-the-Loop Policies with Diffusion Models","url":"https://arxiv.org/html/2503.01876v1"}]

Based on the search results, I found several relevant papers and resources related to training-free inference-time robustness improvement for robot manipulation with diffusion policies in 2026:

## Key Findings:

**Training-Free Inference-Time Methods:**

1. **Two-Steps Diffusion Policy via Genetic Denoising** - This recent work (September 2025) shows that diffusion policy can be made faster and more accurate without retraining, introducing a genetic algorithm to reduce to two denoising steps while solving challenging tasks with only 2 neural function evaluations while improving or matching performance.

2. **Policy Composition at Test-Time** - An alternative paradigm for enhancing policy performance without additional model training demonstrates that composed policies can exceed the performance of either parent policy.

3. **Human-in-the-Loop with Uncertainty Estimation** - A method leverages the generative process of diffusion policies to compute an uncertainty-based metric based on which the autonomous agent can decide to request operator assistance at deployment time, without requiring any operator interaction during training.

**Robustness-Focused Approaches:**

MoE-DP (Mixture of Experts-Enhanced Diffusion Policy) integrates an MoE layer between the visual encoder and the diffusion model, decomposing long-horizon tasks into a set of specialized skills in an end-to-end manner and enhancing robustness when facing disturbance.

These approaches represent the current state-of-the-art in improving diffusion policy robustness and efficiency at inference time without requiring model retraining.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f389385-4e78-4d7a-90e9-d126cc7c2e73",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "e517abb8-0602-44b1-b4d1-a05f546bc24f",
  "toolUseResult": {
    "query": "training-free inference-time robustness improvement robot manipulation diffusion policy 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QbRJ6E9Zgz1gu5sM9E71pv",
        "content": [
          {
            "title": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
            "url": "https://diffusion-policy.cs.columbia.edu/"
          },
          {
            "title": "Diffusion models for robotic manipulation: a survey - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"
          },
          {
            "title": "Frontiers | Diffusion models for robotic manipulation: a survey",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"
          },
          {
            "title": "MoE-DP: An MoE-Enhanced Diffusion Policy for Robust Long-Horizon Robotic Manipulation with Skill Decomposition and Failure Recovery",
            "url": "https://arxiv.org/html/2511.05007"
          },
          {
            "title": "Two-Steps Diffusion Policy for Robotic Manipulation via Genetic Denoising | OpenReview",
            "url": "https://openreview.net/forum?id=YY1MPKBHp7"
          },
          {
            "title": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .",
            "url": "https://arxiv.org/pdf/2303.04137"
          },
          {
            "title": "Diffusion Policy:",
            "url": "https://www.roboticsproceedings.org/rss19/p026.pdf"
          },
          {
            "title": "[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
            "url": "https://arxiv.org/abs/2303.04137"
          },
          {
            "title": "[2510.01068] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition",
            "url": "https://arxiv.org/abs/2510.01068"
          },
          {
            "title": "Uncertainty Comes for Free: Human-in-the-Loop Policies with Diffusion Models",
            "url": "https://arxiv.org/html/2503.01876v1"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and resources related to training-free inference-time robustness improvement for robot manipulation with diffusion policies in 2026:\n\n## Key Findings:\n\n**Training-Free Inference-Time Methods:**\n\n1. **Two-Steps Diffusion Policy via Genetic Denoising** - This recent work (September 2025) shows that diffusion policy can be made faster and more accurate without retraining, introducing a genetic algorithm to reduce to two denoising steps while solving challenging tasks with only 2 neural function evaluations while improving or matching performance.\n\n2. **Policy Composition at Test-Time** - An alternative paradigm for enhancing policy performance without additional model training demonstrates that composed policies can exceed the performance of either parent policy.\n\n3. **Human-in-the-Loop with Uncertainty Estimation** - A method leverages the generative process of diffusion policies to compute an uncertainty-based metric based on which the autonomous agent can decide to request operator assistance at deployment time, without requiring any operator interaction during training.\n\n**Robustness-Focused Approaches:**\n\nMoE-DP (Mixture of Experts-Enhanced Diffusion Policy) integrates an MoE layer between the visual encoder and the diffusion model, decomposing long-horizon tasks into a set of specialized skills in an end-to-end manner and enhancing robustness when facing disturbance.\n\nThese approaches represent the current state-of-the-art in improving diffusion policy robustness and efficiency at inference time without requiring model retraining."
    ],
    "durationSeconds": 6.612120172999999
  },
  "sourceToolAssistantUUID": "6f389385-4e78-4d7a-90e9-d126cc7c2e73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification o…",
  "leafUuid": "e517abb8-0602-44b1-b4d1-a05f546bc24f",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Revisit WAM geometric robustness via video-action alignment",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Tool result

_source line 22 · 2026-05-10T19:54:51.633Z_

<details><summary>↩ Tool result · `toolu_01J4Y8caSkUokuKRPk4Gwgwq`</summary>

```text
Web search results for query: "Motus unified latent action world model LIBERO checkpoint github 2025"

Links: [{"title":"GitHub - thu-ml/Motus: Official code of Motus: A Unified Latent Action World Model · GitHub","url":"https://github.com/thu-ml/Motus"},{"title":"Motus: A Unified Latent Action World Model","url":"https://motus-robotics.github.io/motus"},{"title":"Motus: A Unified Latent Action World Model","url":"https://arxiv.org/html/2512.13030v1"},{"title":"Motus/README.md at main · thu-ml/Motus","url":"https://github.com/thu-ml/Motus/blob/main/README.md"},{"title":"[2512.13030] Motus: A Unified Latent Action World Model","url":"https://arxiv.org/abs/2512.13030"},{"title":"Motus: A Unified Latent Action World Model | alphaXiv","url":"https://www.alphaxiv.org/resources/2512.13030v1"},{"title":"motus-robotics/Motus · Hugging Face","url":"https://huggingface.co/motus-robotics/Motus"},{"title":"Motus: A Unified Latent Action World Model | Request PDF","url":"https://www.researchgate.net/publication/398721535_Motus_A_Unified_Latent_Action_World_Model"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning","url":"https://arxiv.org/html/2602.11236v1"}]

Based on the web search results, here's information about Motus and its LIBERO performance:

## Overview

Motus is the official code of a unified latent action world model, available on GitHub at [thu-ml/Motus](https://github.com/thu-ml/Motus).

## Architecture and Approach

Motus introduces a Mixture-of-Transformers (MoT) architecture to integrate three experts (understanding, action, and video generation) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (World Models, Vision-Language-Action Models, Inverse Dynamics Models, Video Generation Models, and Video-Action Joint Prediction Models).

Motus further leverages optical flow to learn latent actions and adopts a three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level "delta action" and enabling large-scale action pretraining.

## LIBERO Benchmark Results

LIBERO-Long is the long-horizon subset of the LIBERO benchmark, comprising 10 language-conditioned manipulation tasks from LIBERO-100 that require multi-stage decision making, diverse manipulation skills, and robust knowledge transfer across objects and scenes. Under the standard LIBERO-Long evaluation protocol, Motus achieves an average success score of 97.6, matching the best reported performance of X-VLA and thereby reaching state-of-the-art results on this benchmark.

## Checkpoints and Code

[2025-12-16] Initial release of Motus with pretrained checkpoints and training code. Checkpoints can be downloaded using huggingface-cli for models like Motus_Wan2_2_5B_pretrain, Motus, and Motus_robotwin2.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d32ffd7-cdb3-404f-9fb7-4c946ce0ce12",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "12805f33-f63d-452e-a6de-80fb081248fe",
  "toolUseResult": {
    "query": "Motus unified latent action world model LIBERO checkpoint github 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_014r2igoN9WZqFzZJxmeUTyg",
        "content": [
          {
            "title": "GitHub - thu-ml/Motus: Official code of Motus: A Unified Latent Action World Model · GitHub",
            "url": "https://github.com/thu-ml/Motus"
          },
          {
            "title": "Motus: A Unified Latent Action World Model",
            "url": "https://motus-robotics.github.io/motus"
          },
          {
            "title": "Motus: A Unified Latent Action World Model",
            "url": "https://arxiv.org/html/2512.13030v1"
          },
          {
            "title": "Motus/README.md at main · thu-ml/Motus",
            "url": "https://github.com/thu-ml/Motus/blob/main/README.md"
          },
          {
            "title": "[2512.13030] Motus: A Unified Latent Action World Model",
            "url": "https://arxiv.org/abs/2512.13030"
          },
          {
            "title": "Motus: A Unified Latent Action World Model | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2512.13030v1"
          },
          {
            "title": "motus-robotics/Motus · Hugging Face",
            "url": "https://huggingface.co/motus-robotics/Motus"
          },
          {
            "title": "Motus: A Unified Latent Action World Model | Request PDF",
            "url": "https://www.researchgate.net/publication/398721535_Motus_A_Unified_Latent_Action_World_Model"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning",
            "url": "https://arxiv.org/html/2602.11236v1"
          }
        ]
      },
      "Based on the web search results, here's information about Motus and its LIBERO performance:\n\n## Overview\n\nMotus is the official code of a unified latent action world model, available on GitHub at [thu-ml/Motus](https://github.com/thu-ml/Motus).\n\n## Architecture and Approach\n\nMotus introduces a Mixture-of-Transformers (MoT) architecture to integrate three experts (understanding, action, and video generation) and adopts a UniDiffuser-style scheduler to enable flexible switching between different modeling modes (World Models, Vision-Language-Action Models, Inverse Dynamics Models, Video Generation Models, and Video-Action Joint Prediction Models).\n\nMotus further leverages optical flow to learn latent actions and adopts a three-phase training pipeline and six-layer data pyramid, thereby extracting pixel-level \"delta action\" and enabling large-scale action pretraining.\n\n## LIBERO Benchmark Results\n\nLIBERO-Long is the long-horizon subset of the LIBERO benchmark, comprising 10 language-conditioned manipulation tasks from LIBERO-100 that require multi-stage decision making, diverse manipulation skills, and robust knowledge transfer across objects and scenes. Under the standard LIBERO-Long evaluation protocol, Motus achieves an average success score of 97.6, matching the best reported performance of X-VLA and thereby reaching state-of-the-art results on this benchmark.\n\n## Checkpoints and Code\n\n[2025-12-16] Initial release of Motus with pretrained checkpoints and training code. Checkpoints can be downloaded using huggingface-cli for models like Motus_Wan2_2_5B_pretrain, Motus, and Motus_robotwin2."
    ],
    "durationSeconds": 8.268543248000002
  },
  "sourceToolAssistantUUID": "4d32ffd7-cdb3-404f-9fb7-4c946ce0ce12",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-10T19:55:00.994Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DufabshPM9Yes2jzGf6qr4`</summary>

```json
{
  "url": "https://github.com/thu-ml/Motus",
  "prompt": "What is the exact LIBERO performance reported? Does Motus use independent timesteps like UniDiffuser? Is there a LIBERO checkpoint available for download? What are the training details and architecture specifics for robot control?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12805f33-f63d-452e-a6de-80fb081248fe",
  "isSidechain": false,
  "requestId": "req_011CauUWyVfLm2TfiPnKbVCV",
  "type": "assistant",
  "uuid": "688841e6-01d1-4560-aeab-6f488a0bfd63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtSQdr98zvpNeTpCp2j4kv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 3329,
      "cache_read_input_tokens": 27914,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 900,
          "output_tokens": 411,
          "cache_read_input_tokens": 27914,
          "cache_creation_input_tokens": 3329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3329
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

_source line 24 · 2026-05-10T19:55:03.981Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017rZ5v1mQ5LJXUPYKAyGryA`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.26694v2",
  "prompt": "Extract the following information about X-WAM: 1) What is its LIBERO performance? 2) How does Asynchronous Noise Sampling work exactly - does it allow marginalizing video information like UWM? 3) What are the specific ablation results comparing independent timestep sampling vs their method? 4) Is there code/checkpoint released? 5) What is their critique of UWM's independent timestep mechanism?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "688841e6-01d1-4560-aeab-6f488a0bfd63",
  "isSidechain": false,
  "requestId": "req_011CauUWyVfLm2TfiPnKbVCV",
  "type": "assistant",
  "uuid": "d428899e-466f-4aa1-9f97-b738dd00b8b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtSQdr98zvpNeTpCp2j4kv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 3329,
      "cache_read_input_tokens": 27914,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 900,
          "output_tokens": 411,
          "cache_read_input_tokens": 27914,
          "cache_creation_input_tokens": 3329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3329
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

_source line 25 · 2026-05-10T19:55:04.510Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QywYHKjeKgqiqzcTjLjT6T`</summary>

```json
{
  "query": "Motus LIBERO-Long LIBERO-90 benchmark results UniDiffuser timestep mechanism robot control"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d428899e-466f-4aa1-9f97-b738dd00b8b1",
  "isSidechain": false,
  "requestId": "req_011CauUWyVfLm2TfiPnKbVCV",
  "type": "assistant",
  "uuid": "50071af9-dfb4-4a9b-bd04-75abc4c95692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtSQdr98zvpNeTpCp2j4kv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 3329,
      "cache_read_input_tokens": 27914,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 900,
          "output_tokens": 411,
          "cache_read_input_tokens": 27914,
          "cache_creation_input_tokens": 3329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3329
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

_source line 26 · 2026-05-10T19:55:05.390Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RqckQPhJnZ6YkXjimkfVj3`</summary>

```json
{
  "query": "\"test-time adaptation\" \"diffusion policy\" geometric perturbation viewpoint robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50071af9-dfb4-4a9b-bd04-75abc4c95692",
  "isSidechain": false,
  "requestId": "req_011CauUWyVfLm2TfiPnKbVCV",
  "type": "assistant",
  "uuid": "c0de02b5-2bd1-4321-a6b2-bf0f814ade8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtSQdr98zvpNeTpCp2j4kv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 3329,
      "cache_read_input_tokens": 27914,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 900,
          "output_tokens": 411,
          "cache_read_input_tokens": 27914,
          "cache_creation_input_tokens": 3329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3329
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

_source line 27 · 2026-05-10T19:55:06.088Z_

<details><summary>↩ Tool result · `toolu_01DufabshPM9Yes2jzGf6qr4`</summary>

```text
# Motus Repository Information

Based on the GitHub repository content provided, I cannot find answers to your specific questions:

**LIBERO Performance:** No LIBERO benchmark results are mentioned in the documentation.

**UniDiffuser Independence:** The page describes Motus as adopting a "UniDiffuser-style scheduler" but does not specify whether it uses independent timesteps like the original UniDiffuser architecture.

**LIBERO Checkpoint:** No LIBERO-specific checkpoint is listed among the available models. The documented checkpoints are:
- Motus_Wan2_2_5B_pretrain
- Motus (general pretrain)
- Motus_robotwin2 (RoboTwin 2.0 fine-tuned)

**Robot Control Architecture:** The repository provides limited architectural detail. It mentions a "Mixture-of-Transformers (MoT)" with three experts (understanding, action, and video generation) totaling approximately 8B parameters, but specific robot control training details are referenced as available in the TRAINING.md guide, which is not included in this excerpt.

For comprehensive architecture and training specifications, you would need to consult the full documentation files or the arXiv paper (2512.13030).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "688841e6-01d1-4560-aeab-6f488a0bfd63",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "100e946d-b0ef-43f8-9f48-55faa8b63b4c",
  "toolUseResult": {
    "bytes": 349113,
    "code": 200,
    "codeText": "OK",
    "result": "# Motus Repository Information\n\nBased on the GitHub repository content provided, I cannot find answers to your specific questions:\n\n**LIBERO Performance:** No LIBERO benchmark results are mentioned in the documentation.\n\n**UniDiffuser Independence:** The page describes Motus as adopting a \"UniDiffuser-style scheduler\" but does not specify whether it uses independent timesteps like the original UniDiffuser architecture.\n\n**LIBERO Checkpoint:** No LIBERO-specific checkpoint is listed among the available models. The documented checkpoints are:\n- Motus_Wan2_2_5B_pretrain\n- Motus (general pretrain)\n- Motus_robotwin2 (RoboTwin 2.0 fine-tuned)\n\n**Robot Control Architecture:** The repository provides limited architectural detail. It mentions a \"Mixture-of-Transformers (MoT)\" with three experts (understanding, action, and video generation) totaling approximately 8B parameters, but specific robot control training details are referenced as available in the TRAINING.md guide, which is not included in this excerpt.\n\nFor comprehensive architecture and training specifications, you would need to consult the full documentation files or the arXiv paper (2512.13030).",
    "durationMs": 5090,
    "url": "https://github.com/thu-ml/Motus"
  },
  "sourceToolAssistantUUID": "688841e6-01d1-4560-aeab-6f488a0bfd63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T19:55:10.722Z_

<details><summary>↩ Tool result · `toolu_01QywYHKjeKgqiqzcTjLjT6T`</summary>

```text
Web search results for query: "Motus LIBERO-Long LIBERO-90 benchmark results UniDiffuser timestep mechanism robot control"

Links: [{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"Libero - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/simulation/libero"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"Motus: A Unified Latent Action World Model","url":"https://arxiv.org/pdf/2512.13030"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"LIBERO Benchmark: Lifelong Robot Learning","url":"https://www.emergentmind.com/topics/libero-benchmark"},{"title":"LIBERO – LIBERO","url":"https://libero-project.github.io/main.html"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/en/libero"}]

Based on the search results, I found relevant information about your query:

## Motus and UniDiffuser Timestep Mechanism

Motus incorporates a UniDiffuser-like scheduler, allocating distinct timesteps and noise scales to each modality (e.g., videos and actions). This mechanism is part of the model's approach to coordinate multimodal generation.

## LIBERO Benchmarks

The search results confirm the LIBERO benchmarks you mentioned:

- LIBERO-90 consists of 90 short-horizon tasks from the LIBERO-100 collection
- LIBERO-Long consists of 10 long-horizon tasks from the LIBERO-100 collection

## Motus Performance Results

Motus achieves state-of-the-art performance on the RoboTwin 2.0 randomized multi-task setting, delivering over a 45% absolute improvement compared with the π0.5 model.

The search results also indicate that Motus incorporates a UniDiffuser-like scheduler for multimodal generation, which helps coordinate video and action generation with appropriately allocated timesteps for each modality. However, the search results don't contain specific benchmark results on LIBERO-90 or LIBERO-Long for the Motus model—the detailed results appear to be on the RoboTwin 2.0 simulation benchmark instead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50071af9-dfb4-4a9b-bd04-75abc4c95692",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "75357108-698b-4e8f-ac11-1347b0ff139a",
  "toolUseResult": {
    "query": "Motus LIBERO-Long LIBERO-90 benchmark results UniDiffuser timestep mechanism robot control",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SxDp1PGCDUV2YUwYHF1s2X",
        "content": [
          {
            "title": "GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub",
            "url": "https://github.com/Lifelong-Robot-Learning/LIBERO"
          },
          {
            "title": "Libero - LeRobot",
            "url": "https://www.mintlify.com/huggingface/lerobot/simulation/libero"
          },
          {
            "title": "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium",
            "url": "https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"
          },
          {
            "title": "Motus: A Unified Latent Action World Model",
            "url": "https://arxiv.org/pdf/2512.13030"
          },
          {
            "title": "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview",
            "url": "https://openreview.net/forum?id=xzEtNSuDJk"
          },
          {
            "title": "LIBERO Benchmark: Lifelong Robot Learning",
            "url": "https://www.emergentmind.com/topics/libero-benchmark"
          },
          {
            "title": "LIBERO – LIBERO",
            "url": "https://libero-project.github.io/main.html"
          },
          {
            "title": "LIBERO",
            "url": "https://huggingface.co/docs/lerobot/en/libero"
          }
        ]
      },
      "Based on the search results, I found relevant information about your query:\n\n## Motus and UniDiffuser Timestep Mechanism\n\nMotus incorporates a UniDiffuser-like scheduler, allocating distinct timesteps and noise scales to each modality (e.g., videos and actions). This mechanism is part of the model's approach to coordinate multimodal generation.\n\n## LIBERO Benchmarks\n\nThe search results confirm the LIBERO benchmarks you mentioned:\n\n- LIBERO-90 consists of 90 short-horizon tasks from the LIBERO-100 collection\n- LIBERO-Long consists of 10 long-horizon tasks from the LIBERO-100 collection\n\n## Motus Performance Results\n\nMotus achieves state-of-the-art performance on the RoboTwin 2.0 randomized multi-task setting, delivering over a 45% absolute improvement compared with the π0.5 model.\n\nThe search results also indicate that Motus incorporates a UniDiffuser-like scheduler for multimodal generation, which helps coordinate video and action generation with appropriately allocated timesteps for each modality. However, the search results don't contain specific benchmark results on LIBERO-90 or LIBERO-Long for the Motus model—the detailed results appear to be on the RoboTwin 2.0 simulation benchmark instead."
    ],
    "durationSeconds": 6.20778542
  },
  "sourceToolAssistantUUID": "50071af9-dfb4-4a9b-bd04-75abc4c95692",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T19:55:12.845Z_

<details><summary>↩ Tool result · `toolu_01RqckQPhJnZ6YkXjimkfVj3`</summary>

```text
Web search results for query: ""test-time adaptation" "diffusion policy" geometric perturbation viewpoint robustness 2025 2026"

Links: [{"title":"Smoothing the Shift: Towards Stable Test-Time Adaptation under Complex Multimodal Noises | OpenReview","url":"https://openreview.net/forum?id=rObkvzJxTG"},{"title":"AGSM–CPA: Reliability-Aware Robustness for Rotation-Invariant Point Cloud Learning","url":"https://www.mdpi.com/2227-7390/14/2/278"},{"title":"awesome-test-time-adaptation/TTA-TTBA.md at main · tim-learn/awesome-test-time-adaptation","url":"https://github.com/tim-learn/awesome-test-time-adaptation/blob/main/TTA-TTBA.md"},{"title":"Robust Test-time Video-Text Retrieval: Benchmarking and Adapting for Query Shifts | OpenReview","url":"https://openreview.net/forum?id=FRkJ3ehpNN"},{"title":"Test time Adaptation through Perturbation Robustness | OpenReview","url":"https://openreview.net/forum?id=GbBeI5z86uD"},{"title":"[2110.10232] Test time Adaptation through Perturbation Robustness","url":"https://arxiv.org/abs/2110.10232"},{"title":"Frontiers | Research on the robustness of the open-world test-time training model","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1621025/full"},{"title":"Test-time Alignment of Diffusion Models without Reward Over-optimization | OpenReview","url":"https://openreview.net/forum?id=vi3DjUhFVm"},{"title":"Towards Robustness Prompt Tuning with Fully Test-Time Adaptation for CLIP's Zero-Shot Generalization | Proceedings of the 32nd ACM International Conference on Multimedia","url":"https://dl.acm.org/doi/10.1145/3664647.3681213"},{"title":"GitHub - 52CV/WACV-2025-Papers · GitHub","url":"https://github.com/52CV/WACV-2025-Papers"}]

Based on the web search results, I found several relevant papers and resources related to test-time adaptation with diffusion models and robustness concerns:

## Key Findings:

**Test-Time Adaptation with Diffusion Models:**

CloudFixer is a test-time adaptation method for 3D point clouds via diffusion-guided geometric transformation (ECCV 2024). Additionally, there is a work on diffusion-driven test-time adaptation via synthetic-domain alignment (SDA) presented at CVPR 2025.

**Geometric Perturbation and Viewpoint Robustness:**

Rotation-invariant point cloud models aim to reduce sensitivity to viewpoint changes, but their performance still drops noticeably in real-world settings when local geometry is degraded by noise, occlusion, and uneven sampling. The AGSM-CPA framework was proposed to enhance the robustness of rotation-invariant models, treating real-world distortions as geometric perturbations including Gaussian noise, background clutter, point dropout, and spatial block erasing.

**Test-Time Adaptation Frameworks:**

More broadly, test-time adaptation aims to tackle distribution shifts using unlabeled test data without access to the source data, and one approach to combat domain shift at test time involves enforcing robustness to augmented inputs.

The search results indicate active research in 2025-2026 on combining diffusion models with test-time adaptation, geometric robustness, and viewpoint invariance, though I didn't find a specific paper that directly combines all four concepts (test-time adaptation, diffusion policy, geometric perturbation, and viewpoint robustness) in a single work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0de02b5-2bd1-4321-a6b2-bf0f814ade8c",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "ab723950-5b39-454b-94d3-e609bc220b33",
  "toolUseResult": {
    "query": "\"test-time adaptation\" \"diffusion policy\" geometric perturbation viewpoint robustness 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013tKFqMwUeUG1ZsynMiTWwW",
        "content": [
          {
            "title": "Smoothing the Shift: Towards Stable Test-Time Adaptation under Complex Multimodal Noises | OpenReview",
            "url": "https://openreview.net/forum?id=rObkvzJxTG"
          },
          {
            "title": "AGSM–CPA: Reliability-Aware Robustness for Rotation-Invariant Point Cloud Learning",
            "url": "https://www.mdpi.com/2227-7390/14/2/278"
          },
          {
            "title": "awesome-test-time-adaptation/TTA-TTBA.md at main · tim-learn/awesome-test-time-adaptation",
            "url": "https://github.com/tim-learn/awesome-test-time-adaptation/blob/main/TTA-TTBA.md"
          },
          {
            "title": "Robust Test-time Video-Text Retrieval: Benchmarking and Adapting for Query Shifts | OpenReview",
            "url": "https://openreview.net/forum?id=FRkJ3ehpNN"
          },
          {
            "title": "Test time Adaptation through Perturbation Robustness | OpenReview",
            "url": "https://openreview.net/forum?id=GbBeI5z86uD"
          },
          {
            "title": "[2110.10232] Test time Adaptation through Perturbation Robustness",
            "url": "https://arxiv.org/abs/2110.10232"
          },
          {
            "title": "Frontiers | Research on the robustness of the open-world test-time training model",
            "url": "https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1621025/full"
          },
          {
            "title": "Test-time Alignment of Diffusion Models without Reward Over-optimization | OpenReview",
            "url": "https://openreview.net/forum?id=vi3DjUhFVm"
          },
          {
            "title": "Towards Robustness Prompt Tuning with Fully Test-Time Adaptation for CLIP's Zero-Shot Generalization | Proceedings of the 32nd ACM International Conference on Multimedia",
            "url": "https://dl.acm.org/doi/10.1145/3664647.3681213"
          },
          {
            "title": "GitHub - 52CV/WACV-2025-Papers · GitHub",
            "url": "https://github.com/52CV/WACV-2025-Papers"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers and resources related to test-time adaptation with diffusion models and robustness concerns:\n\n## Key Findings:\n\n**Test-Time Adaptation with Diffusion Models:**\n\nCloudFixer is a test-time adaptation method for 3D point clouds via diffusion-guided geometric transformation (ECCV 2024). Additionally, there is a work on diffusion-driven test-time adaptation via synthetic-domain alignment (SDA) presented at CVPR 2025.\n\n**Geometric Perturbation and Viewpoint Robustness:**\n\nRotation-invariant point cloud models aim to reduce sensitivity to viewpoint changes, but their performance still drops noticeably in real-world settings when local geometry is degraded by noise, occlusion, and uneven sampling. The AGSM-CPA framework was proposed to enhance the robustness of rotation-invariant models, treating real-world distortions as geometric perturbations including Gaussian noise, background clutter, point dropout, and spatial block erasing.\n\n**Test-Time Adaptation Frameworks:**\n\nMore broadly, test-time adaptation aims to tackle distribution shifts using unlabeled test data without access to the source data, and one approach to combat domain shift at test time involves enforcing robustness to augmented inputs.\n\nThe search results indicate active research in 2025-2026 on combining diffusion models with test-time adaptation, geometric robustness, and viewpoint invariance, though I didn't find a specific paper that directly combines all four concepts (test-time adaptation, diffusion policy, geometric perturbation, and viewpoint robustness) in a single work."
    ],
    "durationSeconds": 7.4517199949999995
  },
  "sourceToolAssistantUUID": "c0de02b5-2bd1-4321-a6b2-bf0f814ade8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T19:55:13.963Z_

<details><summary>↩ Tool result · `toolu_017rZ5v1mQ5LJXUPYKAyGryA`</summary>

```text
# X-WAM Analysis Based on Available Content

## 1) LIBERO Performance
The document does not contain LIBERO benchmark results. Evaluations are limited to RoboCasa (79.2% success rate) and RoboTwin 2.0 (89.8-90.7% success rates).

## 2) Asynchronous Noise Sampling Mechanism
ANS does **not** marginalize video information like UWM. Instead, it employs coupled sampling where video and action noise levels are dependent rather than independent. During inference, actions decode in Ta steps while videos continue for To steps (Ta < To). The training sampling formula uses a mixture distribution where: "ta ∼ U(0,1), tO = ta + (1−ta)⋅b, b ∼ Beta(1.5,1)" ensuring tO ≥ ta, matching the inference regime.

## 3) Ablation Results: Coupled vs. Independent Sampling
The ablation study (Table 4b) directly compares strategies:
- **Decoupled train + Async infer**: 67.2% success, PSNR 22.60
- **ANS train + Async infer**: 67.8% success, PSNR 23.46

The authors note that decoupled sampling creates "training configurations that never arise at test time (e.g., tO<ta)" degrading reconstruction quality. ANS resolves this by "sampling from their joint distribution" to match inference conditions.

## 4) Code/Checkpoint Release
The document provides no information about code or checkpoint availability, though a project website is referenced: "https://sharinka0715.github.io/X-WAM/"

## 5) Critique of UWM's Independent Timestep Mechanism
The paper criticizes that "independent noise sampling for each modality during training...introduces a mismatch between the training and inference distributions and thus limits the effectiveness of asynchronous denoising."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d428899e-466f-4aa1-9f97-b738dd00b8b1",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "ebbbd508-d9af-44b9-ab60-874328df6a82",
  "toolUseResult": {
    "bytes": 414267,
    "code": 200,
    "codeText": "OK",
    "result": "# X-WAM Analysis Based on Available Content\n\n## 1) LIBERO Performance\nThe document does not contain LIBERO benchmark results. Evaluations are limited to RoboCasa (79.2% success rate) and RoboTwin 2.0 (89.8-90.7% success rates).\n\n## 2) Asynchronous Noise Sampling Mechanism\nANS does **not** marginalize video information like UWM. Instead, it employs coupled sampling where video and action noise levels are dependent rather than independent. During inference, actions decode in Ta steps while videos continue for To steps (Ta < To). The training sampling formula uses a mixture distribution where: \"ta ∼ U(0,1), tO = ta + (1−ta)⋅b, b ∼ Beta(1.5,1)\" ensuring tO ≥ ta, matching the inference regime.\n\n## 3) Ablation Results: Coupled vs. Independent Sampling\nThe ablation study (Table 4b) directly compares strategies:\n- **Decoupled train + Async infer**: 67.2% success, PSNR 22.60\n- **ANS train + Async infer**: 67.8% success, PSNR 23.46\n\nThe authors note that decoupled sampling creates \"training configurations that never arise at test time (e.g., tO<ta)\" degrading reconstruction quality. ANS resolves this by \"sampling from their joint distribution\" to match inference conditions.\n\n## 4) Code/Checkpoint Release\nThe document provides no information about code or checkpoint availability, though a project website is referenced: \"https://sharinka0715.github.io/X-WAM/\"\n\n## 5) Critique of UWM's Independent Timestep Mechanism\nThe paper criticizes that \"independent noise sampling for each modality during training...introduces a mismatch between the training and inference distributions and thus limits the effectiveness of asynchronous denoising.\"",
    "durationMs": 9980,
    "url": "https://arxiv.org/html/2604.26694v2"
  },
  "sourceToolAssistantUUID": "d428899e-466f-4aa1-9f97-b738dd00b8b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-10T19:55:13.966Z_

```json
{
  "parentUuid": "ebbbd508-d9af-44b9-ab60-874328df6a82",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c1ef5bb4-28b3-41b7-85e6-f20797702a76",
  "timestamp": "2026-05-10T19:55:13.966Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification o…",
  "leafUuid": "c1ef5bb4-28b3-41b7-85e6-f20797702a76",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Revisit WAM geometric robustness via video-action alignment",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Assistant

_source line 34 · 2026-05-10T19:55:18.773Z_

<details><summary>Logged reasoning block</summary>

```text
Let me get more information about Motus's exact architecture and LIBERO performance, and also check if there are any alternatives to the whole approach. Let me also look at ADPro and TTPL more carefully, as well as investigate the "compose your policies" paper which could be relevant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1ef5bb4-28b3-41b7-85e6-f20797702a76",
  "isSidechain": false,
  "requestId": "req_011CauUYcxwk2HFK1rFxSce4",
  "type": "assistant",
  "uuid": "4ebcec76-7213-4c99-9b53-ba6bc7da61b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCF4QXKuQFjzjtXrSXJTLU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1845,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 31243,
      "output_tokens": 434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2196,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1845,
          "output_tokens": 434,
          "cache_read_input_tokens": 31243,
          "cache_creation_input_tokens": 2196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2196
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

_source line 35 · 2026-05-10T19:55:21.626Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CeZiREguGNEhu5B2FS4oQr`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.13030v1",
  "prompt": "Extract: 1) Exact LIBERO-Long and LIBERO-90 performance numbers. 2) Does Motus use independent timesteps for video and action (like UniDiffuser's t_x and t_y can be set independently)? Can you set t_video = T to marginalize video? 3) What is the architecture size? 4) What is the training pipeline for robot control? 5) Any mention of classifier-free guidance or conditional dropout?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ebcec76-7213-4c99-9b53-ba6bc7da61b4",
  "isSidechain": false,
  "requestId": "req_011CauUYcxwk2HFK1rFxSce4",
  "type": "assistant",
  "uuid": "f6f314a4-5e68-440f-b030-622f64d2e7be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCF4QXKuQFjzjtXrSXJTLU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1845,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 31243,
      "output_tokens": 434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2196,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1845,
          "output_tokens": 434,
          "cache_read_input_tokens": 31243,
          "cache_creation_input_tokens": 2196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2196
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

_source line 36 · 2026-05-10T19:55:22.563Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Mnc8rNwpBdEHVYxzyq2rY`</summary>

```json
{
  "query": "ADPro test-time adaptive diffusion policy manifold denoising ICLR 2025 geometric robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6f314a4-5e68-440f-b030-622f64d2e7be",
  "isSidechain": false,
  "requestId": "req_011CauUYcxwk2HFK1rFxSce4",
  "type": "assistant",
  "uuid": "957a2f9c-dc51-4b8c-8b1e-fb7293887034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCF4QXKuQFjzjtXrSXJTLU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1845,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 31243,
      "output_tokens": 434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2196,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1845,
          "output_tokens": 434,
          "cache_read_input_tokens": 31243,
          "cache_creation_input_tokens": 2196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2196
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

_source line 37 · 2026-05-10T19:55:23.115Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PuSoqDFPjuZptrkfmmpQrW`</summary>

```json
{
  "query": "\"compose your policies\" diffusion test-time composition robot manipulation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "957a2f9c-dc51-4b8c-8b1e-fb7293887034",
  "isSidechain": false,
  "requestId": "req_011CauUYcxwk2HFK1rFxSce4",
  "type": "assistant",
  "uuid": "b1ea91ba-d87e-4d0d-bcf4-2c3ad2a7947b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCF4QXKuQFjzjtXrSXJTLU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1845,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 31243,
      "output_tokens": 434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2196,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1845,
          "output_tokens": 434,
          "cache_read_input_tokens": 31243,
          "cache_creation_input_tokens": 2196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2196
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

_source line 38 · 2026-05-10T19:55:23.680Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KA1JH6CNtJAEeZh3sSiymo`</summary>

```json
{
  "query": "TTPL \"test-time perturbation learning\" VLA delayed feedback 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1ea91ba-d87e-4d0d-bcf4-2c3ad2a7947b",
  "isSidechain": false,
  "requestId": "req_011CauUYcxwk2HFK1rFxSce4",
  "type": "assistant",
  "uuid": "5c199a2b-ef19-4149-b89d-0d2ceb6c78ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCF4QXKuQFjzjtXrSXJTLU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1845,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 31243,
      "output_tokens": 434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2196,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1845,
          "output_tokens": 434,
          "cache_read_input_tokens": 31243,
          "cache_creation_input_tokens": 2196,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2196
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

_source line 39 · 2026-05-10T19:55:27.306Z_

<details><summary>↩ Tool result · `toolu_01CeZiREguGNEhu5B2FS4oQr`</summary>

```text
# Motus Research Questions - Response

## 1) LIBERO-Long and LIBERO-90 Performance

**LIBERO-Long:** Motus achieves 97.6, matching X-VLA's best reported performance.

**LIBERO-90:** Not mentioned in the provided content. Only LIBERO-Long results are included.

## 2) Independent Timesteps for Video and Action

Yes, Motus employs independent timesteps. The paper states: "By allocating different timesteps and noise scales to videos and actions, respectively, Motus establishes a UniDiffuser-like scheduler."

However, the document does **not explicitly confirm** whether video can be marginalized by setting τ_video to maximum while sampling actions. The algorithms show both modalities use separate timestep variables (τ_o and τ_a), but complete marginalization capability isn't detailed.

## 3) Architecture Size

**Total model scale: 8B parameters**
- VGM: 5.0B
- VLM: 2.13B  
- Action Expert: 641.5M
- Understanding Expert: 253.5M

## 4) Training Pipeline for Robot Control

**Three-stage process:**
- **Stage 1:** Video generation model adaptation using multi-robot and human video data
- **Stage 2:** Unified training (VLM frozen) incorporating latent actions across diverse datasets
- **Stage 3:** Fine-tuning on target-robot demonstrations

## 5) Classifier-Free Guidance or Conditional Dropout

**Not mentioned** in the provided document. No discussion of these techniques appears in the methodology or implementation sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6f314a4-5e68-440f-b030-622f64d2e7be",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "8d27f8d5-6f7b-4994-9a0a-d16bbb75054a",
  "toolUseResult": {
    "bytes": 606019,
    "code": 200,
    "codeText": "OK",
    "result": "# Motus Research Questions - Response\n\n## 1) LIBERO-Long and LIBERO-90 Performance\n\n**LIBERO-Long:** Motus achieves 97.6, matching X-VLA's best reported performance.\n\n**LIBERO-90:** Not mentioned in the provided content. Only LIBERO-Long results are included.\n\n## 2) Independent Timesteps for Video and Action\n\nYes, Motus employs independent timesteps. The paper states: \"By allocating different timesteps and noise scales to videos and actions, respectively, Motus establishes a UniDiffuser-like scheduler.\"\n\nHowever, the document does **not explicitly confirm** whether video can be marginalized by setting τ_video to maximum while sampling actions. The algorithms show both modalities use separate timestep variables (τ_o and τ_a), but complete marginalization capability isn't detailed.\n\n## 3) Architecture Size\n\n**Total model scale: 8B parameters**\n- VGM: 5.0B\n- VLM: 2.13B  \n- Action Expert: 641.5M\n- Understanding Expert: 253.5M\n\n## 4) Training Pipeline for Robot Control\n\n**Three-stage process:**\n- **Stage 1:** Video generation model adaptation using multi-robot and human video data\n- **Stage 2:** Unified training (VLM frozen) incorporating latent actions across diverse datasets\n- **Stage 3:** Fine-tuning on target-robot demonstrations\n\n## 5) Classifier-Free Guidance or Conditional Dropout\n\n**Not mentioned** in the provided document. No discussion of these techniques appears in the methodology or implementation sections.",
    "durationMs": 5673,
    "url": "https://arxiv.org/html/2512.13030v1"
  },
  "sourceToolAssistantUUID": "f6f314a4-5e68-440f-b030-622f64d2e7be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T19:55:29.865Z_

<details><summary>↩ Tool result · `toolu_019Mnc8rNwpBdEHVYxzyq2rY`</summary>

```text
Web search results for query: "ADPro test-time adaptive diffusion policy manifold denoising ICLR 2025 geometric robustness"

Links: [{"title":"ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/html/2508.06266"},{"title":"[2508.06266] ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation","url":"https://arxiv.org/abs/2508.06266"},{"title":"ADPro: a Test-time Adaptive Diffusion Policy for Robot Manipulation via Manifold and Initial Noise Constraints","url":"https://arxiv.org/html/2508.06266v1"},{"title":"Published as a conference paper at ICLR 2025 TEST-TIME ALIGNMENT OF DIFFUSION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d9042abf40782fbce28901c1c9c0e8d8-Paper-Conference.pdf"},{"title":"ADPro: a Test-time Adaptive Diffusion Policy for Robot ...","url":"https://www.alphaxiv.org/overview/2508.06266v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Track: Oral Session 1A","url":"https://iclr.cc/virtual/2025/session/31935"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"ICLR 2025 Schedule","url":"https://iclr.cc/virtual/2025/calendar"}]

Based on the web search results, I found detailed information about ADPro:

## ADPro: Test-Time Adaptive Diffusion Policy

ADPro is a novel adaptive diffusion policy that leverages observation guidance from observed data and constrains the diffusion process to improve generalizability in robotic manipulation.

### Key Technical Components:

**Manifold-Constrained Denoising**: ADPro embeds a geometric manifold constraint that aligns denoising updates with task-relevant subspaces, leveraging the fact that the relative pose between the end-effector and target scene provides a natural gradient direction, and guiding denoising along the geodesic path of the manipulation manifold.

**Task-Aware Initialization**: To reduce unnecessary exploration and accelerate convergence, ADPro proposes an analytically guided initialization: rather than sampling from an uninformative prior, it computes a rough registration between the gripper and target scenes to propose a structured initial noisy action.

### Training-Free and Plug-and-Play:

ADPro is compatible with pre-trained diffusion policies and requires no retraining, enabling test-time adaptation that tailors the policy to specific tasks, thereby enhancing generalization across novel tasks and environments.

### Performance Results:

Experiments on RLBench, CALVIN, and real-world datasets show that ADPro improves success rates, generalization, and sampling efficiency, achieving up to 25% fewer inference steps and 9% points improvement in success rates on long-horizon tasks.

The paper appears to be available on arXiv (2508.06266) and represents recent work in adaptive diffusion-based robotic manipulation policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "957a2f9c-dc51-4b8c-8b1e-fb7293887034",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "2fddbaf7-7ae4-44a6-8f11-5c0cc58bbdc4",
  "toolUseResult": {
    "query": "ADPro test-time adaptive diffusion policy manifold denoising ICLR 2025 geometric robustness",
    "results": [
      {
        "tool_use_id": "srvtoolu_014KRRGiKpb4PWX42K9Dzq4c",
        "content": [
          {
            "title": "ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation",
            "url": "https://arxiv.org/html/2508.06266"
          },
          {
            "title": "[2508.06266] ADPro: a Test-time Adaptive Diffusion Policy via Manifold-constrained Denoising and Task-aware Initialization for Robotic Manipulation",
            "url": "https://arxiv.org/abs/2508.06266"
          },
          {
            "title": "ADPro: a Test-time Adaptive Diffusion Policy for Robot Manipulation via Manifold and Initial Noise Constraints",
            "url": "https://arxiv.org/html/2508.06266v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 TEST-TIME ALIGNMENT OF DIFFUSION",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/d9042abf40782fbce28901c1c9c0e8d8-Paper-Conference.pdf"
          },
          {
            "title": "ADPro: a Test-time Adaptive Diffusion Policy for Robot ...",
            "url": "https://www.alphaxiv.org/overview/2508.06266v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/c0749c39aaff9e9e4c91f7118bf21b1e-Paper-Conference.pdf"
          },
          {
            "title": "ICLR 2025 Papers",
            "url": "https://iclr.cc/virtual/2025/papers.html"
          },
          {
            "title": "Track: Oral Session 1A",
            "url": "https://iclr.cc/virtual/2025/session/31935"
          },
          {
            "title": "ICLR 2026 Schedule",
            "url": "https://iclr.cc/virtual/2026/calendar"
          },
          {
            "title": "ICLR 2025 Schedule",
            "url": "https://iclr.cc/virtual/2025/calendar"
          }
        ]
      },
      "Based on the web search results, I found detailed information about ADPro:\n\n## ADPro: Test-Time Adaptive Diffusion Policy\n\nADPro is a novel adaptive diffusion policy that leverages observation guidance from observed data and constrains the diffusion process to improve generalizability in robotic manipulation.\n\n### Key Technical Components:\n\n**Manifold-Constrained Denoising**: ADPro embeds a geometric manifold constraint that aligns denoising updates with task-relevant subspaces, leveraging the fact that the relative pose between the end-effector and target scene provides a natural gradient direction, and guiding denoising along the geodesic path of the manipulation manifold.\n\n**Task-Aware Initialization**: To reduce unnecessary exploration and accelerate convergence, ADPro proposes an analytically guided initialization: rather than sampling from an uninformative prior, it computes a rough registration between the gripper and target scenes to propose a structured initial noisy action.\n\n### Training-Free and Plug-and-Play:\n\nADPro is compatible with pre-trained diffusion policies and requires no retraining, enabling test-time adaptation that tailors the policy to specific tasks, thereby enhancing generalization across novel tasks and environments.\n\n### Performance Results:\n\nExperiments on RLBench, CALVIN, and real-world datasets show that ADPro improves success rates, generalization, and sampling efficiency, achieving up to 25% fewer inference steps and 9% points improvement in success rates on long-horizon tasks.\n\nThe paper appears to be available on arXiv (2508.06266) and represents recent work in adaptive diffusion-based robotic manipulation policies."
    ],
    "durationSeconds": 7.298995967999995
  },
  "sourceToolAssistantUUID": "957a2f9c-dc51-4b8c-8b1e-fb7293887034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T19:55:29.875Z_

<details><summary>↩ Tool result · `toolu_01KA1JH6CNtJAEeZh3sSiymo`</summary>

```text
Web search results for query: "TTPL "test-time perturbation learning" VLA delayed feedback 2026 arXiv"

Links: [{"title":"Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2604.18107"},{"title":"Test-Time Perturbation Learning with Delayed Feedback for","url":"https://arxiv.org/pdf/2604.18107"},{"title":"[2604.18107] Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.18107"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"Test-Time Learning for Large Language Models","url":"https://arxiv.org/html/2505.20633v1"},{"title":"AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.14148v1"},{"title":"[2504.16084] TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2504.16084"},{"title":"Test-Time Adaptation for Tactile-Vision-Language Models","url":"https://arxiv.org/html/2602.15873v1"},{"title":"Paper page - TTRL: Test-Time Reinforcement Learning","url":"https://huggingface.co/papers/2504.16084"},{"title":"Improving Generalization of Neural Combinatorial Optimization for Vehicle Routing Problems via Test-Time Projection Learning","url":"https://arxiv.org/html/2506.02392"}]

I found the paper you were looking for! The paper proposes Perturbation learning with Delayed Feedback (PDF), a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model.

Here are the key details:

**Paper Title:** Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models

**ArXiv ID:** 2604.18107

**Publication Date:** April 20, 2026

**Main Contribution:** PDF mitigates spurious correlation through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency. To further improve stability, PDF learns a lightweight perturbation module that retrospectively adjusts action logits guided by delayed feedback, correcting overconfidence issue.

**Results:** Experiments on LIBERO (+7.4% success rate) and Atari (+10.3 human normalized score) demonstrate consistent gains of PDF in task success over vanilla VLA and VLA with test-time adaptation.

The paper addresses the problem of trajectory overfitting in Vision-Language-Action models and proposes using delayed feedback during test-time to improve robustness without requiring a separate verifier model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c199a2b-ef19-4149-b89d-0d2ceb6c78ea",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "0a697866-f69d-47bc-b141-7aaa8f0e57b9",
  "toolUseResult": {
    "query": "TTPL \"test-time perturbation learning\" VLA delayed feedback 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KwAQ9wxpmUSeQ7BfqEQikM",
        "content": [
          {
            "title": "Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2604.18107"
          },
          {
            "title": "Test-Time Perturbation Learning with Delayed Feedback for",
            "url": "https://arxiv.org/pdf/2604.18107"
          },
          {
            "title": "[2604.18107] Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2604.18107"
          },
          {
            "title": "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2601.06748v1"
          },
          {
            "title": "Test-Time Learning for Large Language Models",
            "url": "https://arxiv.org/html/2505.20633v1"
          },
          {
            "title": "AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.14148v1"
          },
          {
            "title": "[2504.16084] TTRL: Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/abs/2504.16084"
          },
          {
            "title": "Test-Time Adaptation for Tactile-Vision-Language Models",
            "url": "https://arxiv.org/html/2602.15873v1"
          },
          {
            "title": "Paper page - TTRL: Test-Time Reinforcement Learning",
            "url": "https://huggingface.co/papers/2504.16084"
          },
          {
            "title": "Improving Generalization of Neural Combinatorial Optimization for Vehicle Routing Problems via Test-Time Projection Learning",
            "url": "https://arxiv.org/html/2506.02392"
          }
        ]
      },
      "I found the paper you were looking for! The paper proposes Perturbation learning with Delayed Feedback (PDF), a verifier-free test-time adaptation framework that improves decision performance without fine-tuning the base model.\n\nHere are the key details:\n\n**Paper Title:** Test-Time Perturbation Learning with Delayed Feedback for Vision-Language-Action Models\n\n**ArXiv ID:** 2604.18107\n\n**Publication Date:** April 20, 2026\n\n**Main Contribution:** PDF mitigates spurious correlation through uncertainty-based data augmentation and action voting, while an adaptive scheduler allocates augmentation budgets to balance performance and efficiency. To further improve stability, PDF learns a lightweight perturbation module that retrospectively adjusts action logits guided by delayed feedback, correcting overconfidence issue.\n\n**Results:** Experiments on LIBERO (+7.4% success rate) and Atari (+10.3 human normalized score) demonstrate consistent gains of PDF in task success over vanilla VLA and VLA with test-time adaptation.\n\nThe paper addresses the problem of trajectory overfitting in Vision-Language-Action models and proposes using delayed feedback during test-time to improve robustness without requiring a separate verifier model."
    ],
    "durationSeconds": 6.193078156999996
  },
  "sourceToolAssistantUUID": "5c199a2b-ef19-4149-b89d-0d2ceb6c78ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-10T19:55:41.037Z_

<details><summary>↩ Tool result · `toolu_01PuSoqDFPjuZptrkfmmpQrW`</summary>

```text
Web search results for query: ""compose your policies" diffusion test-time composition robot manipulation 2025"

Links: [{"title":"[2510.01068] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/abs/2510.01068"},{"title":"[2510.01068v1] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/abs/2510.01068v1"},{"title":"Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/html/2510.01068v1"},{"title":"Paper page - Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://huggingface.co/papers/2510.01068"},{"title":"Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition | OpenReview","url":"https://openreview.net/forum?id=TnLFRhLuZ6"},{"title":"COMPOSE YOUR POLICIES! IMPROVING DIFFUSION","url":"https://openreview.net/pdf/19038717c38630da036dbe146de9bbf66ddd1afc.pdf"},{"title":"Test-Time Composition for Robot Diffusion Policies - YouTube","url":"https://www.youtube.com/watch?v=Avm8rN34Hak"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

Based on the web search results, here's what I found about "Compose Your Policies":

## Overview

"Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition" is a research paper published in October 2025.

## Key Contribution

This work introduces an alternative paradigm for enhancing policy performance without additional model training. The composed policies can exceed the performance of either parent policy.

## Technical Approach

The work establishes a theoretical foundation showing that the convex composition of distributional scores from multiple diffusion models can yield a superior one-step functional objective compared to any individual score, with a Grönwall-type bound used to show that this single-step improvement propagates through entire generation trajectories, leading to systemic performance gains.

## Implementation Details

Combining distributional scores from pre-trained diffusion-based or flow-based policies on different conditions (e.g., visual modalities and network backbones), the General Policy Composition (GPC) can generate expressive and adaptable action trajectories through convex score combination without additional training.

## Evaluation

The paper evaluates on Robomimic (which includes three manipulation tasks: Can, Lift, Square), PushT, and RoboTwin (a suite of dual-arm collaborative tasks), and further performs four real-world experiments: Place Bottles, Hang Mug, Close Table, and Punch Holes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1ea91ba-d87e-4d0d-bcf4-2c3ad2a7947b",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "d625c765-43e4-4df9-b5e2-eeaf9fd22e0c",
  "toolUseResult": {
    "query": "\"compose your policies\" diffusion test-time composition robot manipulation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NgCjgKUXH23Yu1AiwcgfQW",
        "content": [
          {
            "title": "[2510.01068] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition",
            "url": "https://arxiv.org/abs/2510.01068"
          },
          {
            "title": "[2510.01068v1] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition",
            "url": "https://arxiv.org/abs/2510.01068v1"
          },
          {
            "title": "Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition",
            "url": "https://arxiv.org/html/2510.01068v1"
          },
          {
            "title": "Paper page - Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition",
            "url": "https://huggingface.co/papers/2510.01068"
          },
          {
            "title": "Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition | OpenReview",
            "url": "https://openreview.net/forum?id=TnLFRhLuZ6"
          },
          {
            "title": "COMPOSE YOUR POLICIES! IMPROVING DIFFUSION",
            "url": "https://openreview.net/pdf/19038717c38630da036dbe146de9bbf66ddd1afc.pdf"
          },
          {
            "title": "Test-Time Composition for Robot Diffusion Policies - YouTube",
            "url": "https://www.youtube.com/watch?v=Avm8rN34Hak"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          }
        ]
      },
      "Based on the web search results, here's what I found about \"Compose Your Policies\":\n\n## Overview\n\n\"Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition\" is a research paper published in October 2025.\n\n## Key Contribution\n\nThis work introduces an alternative paradigm for enhancing policy performance without additional model training. The composed policies can exceed the performance of either parent policy.\n\n## Technical Approach\n\nThe work establishes a theoretical foundation showing that the convex composition of distributional scores from multiple diffusion models can yield a superior one-step functional objective compared to any individual score, with a Grönwall-type bound used to show that this single-step improvement propagates through entire generation trajectories, leading to systemic performance gains.\n\n## Implementation Details\n\nCombining distributional scores from pre-trained diffusion-based or flow-based policies on different conditions (e.g., visual modalities and network backbones), the General Policy Composition (GPC) can generate expressive and adaptable action trajectories through convex score combination without additional training.\n\n## Evaluation\n\nThe paper evaluates on Robomimic (which includes three manipulation tasks: Can, Lift, Square), PushT, and RoboTwin (a suite of dual-arm collaborative tasks), and further performs four real-world experiments: Place Bottles, Hang Mug, Close Table, and Punch Holes."
    ],
    "durationSeconds": 17.919447753999993
  },
  "sourceToolAssistantUUID": "b1ea91ba-d87e-4d0d-bcf4-2c3ad2a7947b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-10T19:56:46.471Z_

<details><summary>Logged reasoning block</summary>

```text
Let me gather more info. Key findings so far:

1. **Motus**: 8B params, UniDiffuser-style independent timesteps (τ_o and τ_a), LIBERO-Long 97.6%. But only releases RoboTwin2 checkpoint, no LIBERO checkpoint. Very large (8B) model.

2. **X-WAM**: ANS is different from independent timesteps - it's coupled sampling. Not easily usable for marginalization. Only evaluated on RoboCasa and RoboTwin, not LIBERO. 67.2-67.8% success rate.


3. **MotuBrain** and **ADPro** don't have LIBERO results either - the former focuses on WorldArena and RoboTwin 2.0, while the latter is a test-time adaptation approach for diffusion policies showing up to 9% improvement on RLBench/CALVIN. **GPC** and **TTPL/PDF** offer training-free test-time composition and perturbation learning respectively, with TTPL/PDF achieving +7.4% on LIBERO. So the real question is whether Motus can actually serve as a backbone given these constraints.

Motus looks promising on paper with its UniDiffuser-style scheduler and 97.6% LIBERO-Long performance, but it's an 8B parameter model with expensive inference, and there's no released LIBERO checkpoint - only RoboTwin 2.0. There's also no mention of CFG or dropout support. I need to figure out if we can get a LIBERO fine-tuned version or if we'd have to fine-tune it ourselves, and whether the "Compose Your Policies" approach might actually be more aligned with what we're trying to do here.

Stepping back, the fundamental issue after exploring all these options is that we have a backbone problem: UWM is too weak at 79%, but Motus is strong at 97.6% on LIBERO-Long yet comes with significant practical constraints.

Beyond that, there's a deeper question about whether the core hypothesis even holds up. If video features are truly unnecessary under standard conditions - as Fast-WAM, GigaWorld, and MotuBrain have shown - then maybe they're not encoding geometric information at all, just appearance and texture that the action branch can learn on its own. When geometric perturbations happen, both branches fail not because you need more video guidance, but because neither has encountered that distribution shift. Meanwhile, competitors like OA-WAM and CKT-WAM are already hitting 84-86% with modest modifications, so a training-free method that underperforms them won't be competitive at CoRL.

After six rounds with no improvement, I'm convinced a major pivot is needed. The structural problem is real - there's no good WAM backbone that combines high performance with native cross-modal CFG support - and the Phase 1 contingency means I'm looking at a 40-60% chance of having no method at all. Even if Phase 1 works, the absolute numbers will likely fall short of SOTA. So I should keep the core insight about inference-time robustness but completely rethink the technical approach. One promising direction is test-time score composition from different viewpoints instead of spectral filtering, since prior work shows you can effectively combine policy scores across different conditions.

But wait - the reviewer's feedback is actually pointing me toward concrete options. They're suggesting I switch to Motus or MotuBrain as the backbone if checkpoints are available, and add something in Phase 2. Let me focus on what they're actually recommending rather than generating more alternatives.

The real constraint is the checkpoint situation: UWM has a released LIBERO checkpoint at 79% with 180M parameters, while Motus shows 97.6% on LIBERO-Long but that's only 10 tasks and no checkpoint is publicly available. Fast-WAM also hits 97.6% on LIBERO. So I need to figure out which backbone is actually feasible to work with given what's been released.

Now I'm considering a completely different angle—instead of trying to amplify guidance through the model architecture, what if I compose action predictions from multiple geometric perspectives at test time? The idea is to apply various camera perturbations and spatial augmentations to the observation, compute action scores from each variant, then combine them through weighted averaging or product-of-experts in score space. This way the composed prediction becomes more robust to geometric variations without needing specific architectural support, drawing from test-time augmentation and score composition principles.

But I'm realizing this is essentially standard test-time augmentation applied to diffusion policies—straightforward but potentially lacking novelty. Let me step back and think about what's actually achievable here. The core issue is whether I can work around the backbone constraints by using Motus, which has strong LIBERO performance and released code. Maybe the right path forward is to commit to Motus as the primary backbone and plan to fine-tune it on the target dataset rather than trying to force architectural modifications that won't work without native support.

That said, Motus is 8B parameters, so running inference multiple times for classifier-free guidance becomes computationally expensive compared to something like UWM at 180M. There's a real practical cost tradeoff here. Let me refocus on what's actually novel and feasible—the core problem of geometric brittleness in world models is still valid, and a training-free solution would genuinely be useful. Rather than pursuing spectral filtering of video-to-action guidance, which ties me to specific backbone architectures, I should explore test-time approaches that work model-agnostically.

The key idea is leveraging recent work showing that composing policies through distributional score averaging improves robustness—I can apply this specifically to geometric perturbations by generating multiple augmented views of the same observation at test time, computing action scores from each, and then averaging them to get a more robust composed policy. This works for any diffusion-based policy without requiring architectural changes or retraining.

But I'm realizing this might just be standard test-time augmentation applied to diffusion policies, which isn't particularly novel. For WAM specifically though, there's an interesting angle: instead of augmenting the observation itself, I could leverage the video branch to generate predicted future states from different geometric perspectives and compose scores across those predicted trajectories. Let me think through whether this is actually different from what's already been done with diffusion policies and whether "Compose Your Policies" even addresses geometric robustness in the way I'm imagining.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d625c765-43e4-4df9-b5e2-eeaf9fd22e0c",
  "isSidechain": false,
  "requestId": "req_011CauUacjc3JioSKhmMGesS",
  "type": "assistant",
  "uuid": "bd633da8-af28-4133-a0d0-ea2f7249d996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwRfRUctxssNVNroueUe99",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 757,
      "cache_creation_input_tokens": 4506,
      "cache_read_input_tokens": 33439,
      "output_tokens": 2662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 757,
          "output_tokens": 2662,
          "cache_read_input_tokens": 33439,
          "cache_creation_input_tokens": 4506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4506
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

_source line 44 · 2026-05-10T19:56:47.236Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019BZFbT82jj4NgwTiJPEbYk`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.01068v1",
  "prompt": "Extract: 1) What exactly is being composed - same policy with different inputs, or different policies? 2) What is the mathematical formulation of the composition? 3) Does it address viewpoint/geometric robustness? 4) What are the main results and what benchmarks? 5) What are its limitations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd633da8-af28-4133-a0d0-ea2f7249d996",
  "isSidechain": false,
  "requestId": "req_011CauUacjc3JioSKhmMGesS",
  "type": "assistant",
  "uuid": "10c6b4ba-a3d5-40af-ad9d-d55e5ebe4335",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwRfRUctxssNVNroueUe99",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 757,
      "cache_creation_input_tokens": 4506,
      "cache_read_input_tokens": 33439,
      "output_tokens": 2662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 757,
          "output_tokens": 2662,
          "cache_read_input_tokens": 33439,
          "cache_creation_input_tokens": 4506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4506
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

_source line 45 · 2026-05-10T19:56:47.843Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DJvZoR98Jhmnst2PhK2N82`</summary>

```json
{
  "query": "test-time augmentation diffusion policy robot action prediction geometric invariance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10c6b4ba-a3d5-40af-ad9d-d55e5ebe4335",
  "isSidechain": false,
  "requestId": "req_011CauUacjc3JioSKhmMGesS",
  "type": "assistant",
  "uuid": "d2f78f74-f035-4099-9156-2d587ba4d7c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwRfRUctxssNVNroueUe99",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 757,
      "cache_creation_input_tokens": 4506,
      "cache_read_input_tokens": 33439,
      "output_tokens": 2662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 757,
          "output_tokens": 2662,
          "cache_read_input_tokens": 33439,
          "cache_creation_input_tokens": 4506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4506
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

_source line 46 · 2026-05-10T19:56:48.504Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QUupkw9hJXQmYHgfmojfRn`</summary>

```json
{
  "query": "Fast-WAM LIBERO-Plus geometric perturbation evaluation camera viewpoint 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2f78f74-f035-4099-9156-2d587ba4d7c7",
  "isSidechain": false,
  "requestId": "req_011CauUacjc3JioSKhmMGesS",
  "type": "assistant",
  "uuid": "ec67a2bc-84fb-4ae8-aff3-96108d8e8787",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwRfRUctxssNVNroueUe99",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 757,
      "cache_creation_input_tokens": 4506,
      "cache_read_input_tokens": 33439,
      "output_tokens": 2662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 757,
          "output_tokens": 2662,
          "cache_read_input_tokens": 33439,
          "cache_creation_input_tokens": 4506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4506
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification o…",
  "leafUuid": "ec67a2bc-84fb-4ae8-aff3-96108d8e8787",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Revisit WAM geometric robustness via video-action alignment",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Tool result

_source line 49 · 2026-05-10T19:56:54.749Z_

<details><summary>↩ Tool result · `toolu_019BZFbT82jj4NgwTiJPEbYk`</summary>

```text
# General Policy Composition (GPC) Analysis

## 1) What is Being Composed?

GPC composes **different pre-trained policies** rather than the same policy with different inputs. The framework combines heterogeneous models across multiple dimensions:

- Different architectures (Diffusion Policy vs. Mamba Policy)
- Different modalities (RGB vs. point cloud inputs)
- Different model types (Vision-Action vs. Vision-Language-Action)
- Different generative approaches (diffusion vs. flow-matching)

As stated: "GPC is versatile, allowing for the plug-and-play composition of heterogeneous policies."

## 2) Mathematical Formulation

The core composition uses **convex score combination**:

$$\hat{s}_{\text{comp}}(\tau_t, t, \mathbf{c}) = \sum_{i=1}^{n} w_i s_\theta(\tau_t, t, \mathbf{c}_i), \quad \sum_{i=1}^{n} w_i = 1$$

This combines score functions from multiple policies through weighted averaging, where weights sum to one and remain non-negative.

## 3) Viewpoint/Geometric Robustness

The paper does **not directly address** viewpoint or geometric robustness. However, combining RGB and point cloud modalities indirectly improves robustness by leveraging complementary sensory representations.

## 4) Main Results and Benchmarks

**Performance gains across benchmarks:**
- Robomimic & PushT: up to +7.55% improvement
- RoboTwin (bimanual tasks): up to +7% improvement  
- Real-world tasks: approximately +10% improvement

**Key finding:** "the composed policies can exceed the performance of either parent policy," demonstrated across diverse manipulation and navigation tasks.

## 5) Main Limitations

The authors acknowledge:

- **Fixed discretization**: "test-time weight search is restricted by a fixed discretization"
- **Scalability**: Study focuses on dual-policy composition; extending to multiple policies increases computational cost
- **Optimal weights**: Finding analytically optimal weights is intractable, requiring test-time search
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "10c6b4ba-a3d5-40af-ad9d-d55e5ebe4335",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "822fe510-9e90-403d-aba0-d4c039c54378",
  "toolUseResult": {
    "bytes": 787135,
    "code": 200,
    "codeText": "OK",
    "result": "# General Policy Composition (GPC) Analysis\n\n## 1) What is Being Composed?\n\nGPC composes **different pre-trained policies** rather than the same policy with different inputs. The framework combines heterogeneous models across multiple dimensions:\n\n- Different architectures (Diffusion Policy vs. Mamba Policy)\n- Different modalities (RGB vs. point cloud inputs)\n- Different model types (Vision-Action vs. Vision-Language-Action)\n- Different generative approaches (diffusion vs. flow-matching)\n\nAs stated: \"GPC is versatile, allowing for the plug-and-play composition of heterogeneous policies.\"\n\n## 2) Mathematical Formulation\n\nThe core composition uses **convex score combination**:\n\n$$\\hat{s}_{\\text{comp}}(\\tau_t, t, \\mathbf{c}) = \\sum_{i=1}^{n} w_i s_\\theta(\\tau_t, t, \\mathbf{c}_i), \\quad \\sum_{i=1}^{n} w_i = 1$$\n\nThis combines score functions from multiple policies through weighted averaging, where weights sum to one and remain non-negative.\n\n## 3) Viewpoint/Geometric Robustness\n\nThe paper does **not directly address** viewpoint or geometric robustness. However, combining RGB and point cloud modalities indirectly improves robustness by leveraging complementary sensory representations.\n\n## 4) Main Results and Benchmarks\n\n**Performance gains across benchmarks:**\n- Robomimic & PushT: up to +7.55% improvement\n- RoboTwin (bimanual tasks): up to +7% improvement  \n- Real-world tasks: approximately +10% improvement\n\n**Key finding:** \"the composed policies can exceed the performance of either parent policy,\" demonstrated across diverse manipulation and navigation tasks.\n\n## 5) Main Limitations\n\nThe authors acknowledge:\n\n- **Fixed discretization**: \"test-time weight search is restricted by a fixed discretization\"\n- **Scalability**: Study focuses on dual-policy composition; extending to multiple policies increases computational cost\n- **Optimal weights**: Finding analytically optimal weights is intractable, requiring test-time search",
    "durationMs": 7509,
    "url": "https://arxiv.org/html/2510.01068v1"
  },
  "sourceToolAssistantUUID": "10c6b4ba-a3d5-40af-ad9d-d55e5ebe4335",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-10T19:56:55.156Z_

<details><summary>↩ Tool result · `toolu_01DJvZoR98Jhmnst2PhK2N82`</summary>

```text
Web search results for query: "test-time augmentation diffusion policy robot action prediction geometric invariance 2025 2026"

Links: [{"title":"RoboTransfer: Geometry-Consistent Video Diffusion for Robotic Visual Policy Transfer","url":"https://arxiv.org/html/2505.23171v1"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Diffusion policy: : Visuomotor policy learning via action diffusion: International Journal of Robotics Research: Vol 44, No 10-11","url":"https://dl.acm.org/doi/10.1177/02783649241273668"},{"title":"Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/html/2510.01068v1"},{"title":"Time-Unified Diffusion Policy with Action Discrimination for Robotic Manipulation","url":"https://arxiv.org/html/2506.09422"},{"title":"Time-Unified Diffusion Policy with Action Discrimination for ...","url":"https://arxiv.org/pdf/2506.09422"},{"title":"[2510.01068v1] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/abs/2510.01068v1"},{"title":"[2510.01068] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/abs/2510.01068"},{"title":"Diffusion models for robotic manipulation: a survey - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"}]

I found several relevant research papers and resources on diffusion policies for robot action prediction. Here are the key findings:

## Main Results:

**Test-Time Augmentation and Diffusion Policies:**
Diffusion-based models for robotic control, including vision-language-action (VLA) and vision-action (VA) policies, have demonstrated significant capabilities, yet their advancement is constrained by the high cost of acquiring large-scale interaction datasets. Recent work introduces alternative paradigms for enhancing policy performance without additional model training.

Specifically, one theoretical approach shows that the convex composition of distributional scores from multiple diffusion models can yield a superior one-step functional objective compared to any individual score.

**Geometric Invariance and Robot Policies:**
Data augmentation is widely used to train robust machine learning models, and prior work has applied augmentation directly to real-world robot captures to improve the resilience of visual policies against environmental variations. Neural view synthesis techniques generate novel viewpoints from existing robot data, promoting view-invariant feature learning.

A 2025 paper on geometric-consistent video diffusion addresses this directly: evaluation includes multi-view consistency, geometric consistency, and semantic consistency.

**Foundational Work:**
Diffusion Policy introduces a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process, with key technical contributions including the incorporation of receding horizon control, visual conditioning, and the time-series diffusion transformer.

The search returned recent papers from 2025-2026 addressing test-time composition of diffusion policies, geometric consistency in video diffusion for robotics, and time-unified diffusion policies for robot action prediction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2f78f74-f035-4099-9156-2d587ba4d7c7",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "393a3171-aeba-4e83-98c4-966792c4fc21",
  "toolUseResult": {
    "query": "test-time augmentation diffusion policy robot action prediction geometric invariance 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012Ea2CgSK3Cfbqqj66W7uUm",
        "content": [
          {
            "title": "RoboTransfer: Geometry-Consistent Video Diffusion for Robotic Visual Policy Transfer",
            "url": "https://arxiv.org/html/2505.23171v1"
          },
          {
            "title": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
            "url": "https://diffusion-policy.cs.columbia.edu/"
          },
          {
            "title": "Diffusion policy: : Visuomotor policy learning via action diffusion: International Journal of Robotics Research: Vol 44, No 10-11",
            "url": "https://dl.acm.org/doi/10.1177/02783649241273668"
          },
          {
            "title": "Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition",
            "url": "https://arxiv.org/html/2510.01068v1"
          },
          {
            "title": "Time-Unified Diffusion Policy with Action Discrimination for Robotic Manipulation",
            "url": "https://arxiv.org/html/2506.09422"
          },
          {
            "title": "Time-Unified Diffusion Policy with Action Discrimination for ...",
            "url": "https://arxiv.org/pdf/2506.09422"
          },
          {
            "title": "[2510.01068v1] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition",
            "url": "https://arxiv.org/abs/2510.01068v1"
          },
          {
            "title": "[2510.01068] Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition",
            "url": "https://arxiv.org/abs/2510.01068"
          },
          {
            "title": "Diffusion models for robotic manipulation: a survey - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12454101/"
          },
          {
            "title": "Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025",
            "url": "https://journals.sagepub.com/doi/full/10.1177/02783649241273668"
          }
        ]
      },
      "I found several relevant research papers and resources on diffusion policies for robot action prediction. Here are the key findings:\n\n## Main Results:\n\n**Test-Time Augmentation and Diffusion Policies:**\nDiffusion-based models for robotic control, including vision-language-action (VLA) and vision-action (VA) policies, have demonstrated significant capabilities, yet their advancement is constrained by the high cost of acquiring large-scale interaction datasets. Recent work introduces alternative paradigms for enhancing policy performance without additional model training.\n\nSpecifically, one theoretical approach shows that the convex composition of distributional scores from multiple diffusion models can yield a superior one-step functional objective compared to any individual score.\n\n**Geometric Invariance and Robot Policies:**\nData augmentation is widely used to train robust machine learning models, and prior work has applied augmentation directly to real-world robot captures to improve the resilience of visual policies against environmental variations. Neural view synthesis techniques generate novel viewpoints from existing robot data, promoting view-invariant feature learning.\n\nA 2025 paper on geometric-consistent video diffusion addresses this directly: evaluation includes multi-view consistency, geometric consistency, and semantic consistency.\n\n**Foundational Work:**\nDiffusion Policy introduces a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process, with key technical contributions including the incorporation of receding horizon control, visual conditioning, and the time-series diffusion transformer.\n\nThe search returned recent papers from 2025-2026 addressing test-time composition of diffusion policies, geometric consistency in video diffusion for robotics, and time-unified diffusion policies for robot action prediction."
    ],
    "durationSeconds": 7.309904145000008
  },
  "sourceToolAssistantUUID": "d2f78f74-f035-4099-9156-2d587ba4d7c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-10T19:56:56.162Z_

<details><summary>↩ Tool result · `toolu_01QUupkw9hJXQmYHgfmojfRn`</summary>

```text
Web search results for query: "Fast-WAM LIBERO-Plus geometric perturbation evaluation camera viewpoint 2026"

Links: [{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"[Quick Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action\\n Models","url":"https://liner.com/review/liberoplus-indepth-robustness-analysis-visionlanguageaction-models"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"Efficient Spatial Adaptation in VLA Models","url":"https://www.emergentmind.com/papers/2512.02902"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/html/2512.02902v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"}]

Based on the web search results, I found relevant information about your query. Here are the key findings:

## LIBERO-Plus: Robustness Analysis with Camera Viewpoint Evaluation

LIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities across key vulnerability dimensions. The research specifically focuses on geometric perturbations and camera viewpoint evaluation.

### Camera Viewpoint Perturbation Evaluation

The research evaluates changes to the viewpoint/pose and field-of-view of the third-person camera as part of a systematic robustness analysis. The camera viewpoint dimension tests the model's view-free representation and generalization ability by changing camera viewpoints, including: camera distance (moving the camera along its optical axis), spherical position (perturbing camera position on a sphere centered at the scene), and camera orientation (fixing camera position but perturbing its orientation).

### Critical Findings

Models are most vulnerable to changes in camera viewpoint and robot initial state, which require a high-level understanding of spatial geometry and proprioception. Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

The benchmark construction follows a systematic two-stage process: expanding the original LIBERO benchmark through seven distinct perturbation factors, followed by task filtering and category balancing based on empirical findings; and evaluating the resulting tasks using four representative models and stratifying them into five difficulty levels (Level-1 to Level-5).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec67a2bc-84fb-4ae8-aff3-96108d8e8787",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "4432a3c2-d0c2-4643-8d05-a6d51045a483",
  "toolUseResult": {
    "query": "Fast-WAM LIBERO-Plus geometric perturbation evaluation camera viewpoint 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015vbYq5HWNGVMxiYqEFCxRR",
        "content": [
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "[Quick Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action\\n Models",
            "url": "https://liner.com/review/liberoplus-indepth-robustness-analysis-visionlanguageaction-models"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "Efficient Spatial Adaptation in VLA Models",
            "url": "https://www.emergentmind.com/papers/2512.02902"
          },
          {
            "title": "[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626v1"
          },
          {
            "title": "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling",
            "url": "https://arxiv.org/html/2512.02902v1"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          }
        ]
      },
      "Based on the web search results, I found relevant information about your query. Here are the key findings:\n\n## LIBERO-Plus: Robustness Analysis with Camera Viewpoint Evaluation\n\nLIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities across key vulnerability dimensions. The research specifically focuses on geometric perturbations and camera viewpoint evaluation.\n\n### Camera Viewpoint Perturbation Evaluation\n\nThe research evaluates changes to the viewpoint/pose and field-of-view of the third-person camera as part of a systematic robustness analysis. The camera viewpoint dimension tests the model's view-free representation and generalization ability by changing camera viewpoints, including: camera distance (moving the camera along its optical axis), spherical position (perturbing camera position on a sphere centered at the scene), and camera orientation (fixing camera position but perturbing its orientation).\n\n### Critical Findings\n\nModels are most vulnerable to changes in camera viewpoint and robot initial state, which require a high-level understanding of spatial geometry and proprioception. Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.\n\nThe benchmark construction follows a systematic two-stage process: expanding the original LIBERO benchmark through seven distinct perturbation factors, followed by task filtering and category balancing based on empirical findings; and evaluating the resulting tasks using four representative models and stratifying them into five difficulty levels (Level-1 to Level-5)."
    ],
    "durationSeconds": 7.655175431999989
  },
  "sourceToolAssistantUUID": "ec67a2bc-84fb-4ae8-aff3-96108d8e8787",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-10T19:59:04.763Z_

<details><summary>Logged reasoning block</summary>

```text
Now I'm finding a very interesting paper: "RoboTransfer: Geometry-Consistent Video Diffusion for Robotic Visual Policy Transfer" (arXiv 2505.23171). Let me check this out - it uses geometric video synthesis for robustness. Also, the "Compose Your Policies" approach is specifically about composing DIFFERENT policies, not the same policy with augmented inputs.

Let me also check the LIBERO-Plus results more carefully to understand the current SOTA landscape, and look at this RoboTransfer paper.

Let me also think more carefully about what direction to go.


Looking at the key tradeoffs: Motus has strong LIBERO-Long performance at 97.6% with independent timesteps, but it's 8B parameters which makes CFG prohibitively expensive, and there's no released LIBERO-90 checkpoint. The original approach has a fundamental structural issue, and GPC composes different policies rather than augmenting a single one. I need to figure out what a realistic pivot would look like - using Motus as a backbone is tempting given its performance, but the computational cost and missing checkpoints are real blockers.

Instead of trying to force Motus to work, I should step back and think about the core problem differently. The geometric robustness challenge for diffusion-based robot policies is still unsolved and worth tackling. What if I approached it as a test-time method that's truly training-free, works with any diffusion policy architecture, and directly targets geometric perturbations? I'm considering something like Test-Time Geometric Score Alignment - the idea being that when the observation gets perturbed geometrically, the diffusion policy's score function becomes biased because it's outside the training distribution. I could align that score back toward the training manifold by estimating the geometric offset, projecting onto a geometrically-aware subspace, and using self-consistency or similar techniques to refine the alignment.

But I'm realizing this approach is getting complicated, and I need to be clearer about what actually differentiates it from existing work. Looking at what's already out there - ADPro uses manifold constraints based on relative poses, AnyCamVLA handles camera adaptation through novel view synthesis, GPC composes scores from different policies, and TTPL does test-time learning with delayed feedback - I'm noticing the gap is really about having a method that directly operates on the score function itself, stays completely training-free without online learning, specifically handles geometric distribution shift, and has solid theoretical grounding. Maybe the right angle is Equivariant Score Rectification, where I leverage the SE(3) or SE(2) structure of geometric perturbations to directly correct the action predictions.

The core insight is that if the observation transforms under some geometric perturbation T, the score should transform equivariantly with it - so I can estimate the perturbation from the observations, compute how actions should transform under it, and use that to rectify the score during denoising. It's principled, training-free, and architecture-agnostic, though it does require estimating the perturbation itself, which could be tricky.

But actually, let me reconsider the whole approach. The original problem with relying on specific architectural features is limiting - what if I reframe this as a test-time correction method instead? The real issue is that diffusion policies learn a score function tuned to the training distribution of observations, so when the camera or robot configuration shifts, the policy computes scores for out-of-distribution observations and gets biased results. I should focus on correcting for that geometric shift directly at test time.

The core method would involve generating multiple geometric augmentations of the perturbed observation and using the variance in predicted scores across these augmentations as a signal for how uncertain the policy is about the geometry. Then I can adaptively adjust the denoising process - slowing down when variance is high and proceeding normally when it's low. I could also try projecting the score onto directions that remain consistent across augmentations to filter out geometry-sensitive components. Though I'm realizing this is getting complicated and might need simplification.

Let me step back and reconsider the reviewer's concrete suggestions instead. They mentioned switching to Motus as the backbone since it has a UniDiffuser-style scheduler and reportedly achieves 97.6% on LIBERO-Long. The tradeoffs are significant though - there's no LIBERO-90 checkpoint available, it requires 8B parameters which makes two forward passes expensive, and there's no evaluation on LIBERO-Plus. I should verify what that 97.6% result actually represents, since LIBERO-Long is only 10 tasks while the standard benchmark most people use is LIBERO-90 with 90 tasks.

The compute cost is the real killer here. With 8B parameters, each forward pass costs roughly 16x more than UWM's 180M, and running CFG with two passes across 90 tasks with 20 seeds and multiple conditions would be prohibitively expensive given the CoRL timeline. Fine-tuning an 8B model on LIBERO-90 from scratch would require substantial compute resources I likely don't have available.

So Motus isn't actually viable for this work. Let me think about what the field actually needs - training-free geometric robustness that works across diverse benchmarks. ADPro handles test-time manifold constraints but only on RLBench and CALVIN, not LIBERO-Plus. AnyCamVLA does view synthesis but is limited to camera variations.  TTPL requires online feedback, and GPC needs a separately trained world model. None of these are purely inference-time, architecture-agnostic, or evaluated on the geometric perturbations I care about.

Instead of sticking with spectral CFG filtering, what if I reframe the approach entirely? The key insight is that a well-trained diffusion policy should have action scores that are approximately equivariant under SE(2) transformations. I could enforce geometric consistency directly in the score space during denoising rather than trying to amplify video-to-action guidance.

The method would compute scores from several small geometric augmentations of the observation at each denoising step, extract the consensus component that aligns across these augmentations, and use that instead of the original score. This is training-free, works with any diffusion-based policy regardless of architecture, directly targets geometric robustness, and doesn't require any backbone-specific modifications or contingency planning.

The main concern is computational cost—K forward passes per step across multiple denoising steps adds significant overhead, though applying this selectively at early denoising steps where geometric information matters most could reduce it to 2-3x. What distinguishes this from standard test-time augmentation is that we're averaging scores in the latent space during the denoising trajectory rather than averaging final predictions, which fundamentally changes how the model generates robust samples. It's conceptually similar to score composition methods like "Compose Your Policies," but instead of combining different policies, we're composing the same policy under different geometric views.

The real novelty lies in using geometric augmentations at test-time to improve robustness without requiring multiple trained policies. But here's the critical realization: if the policy hasn't seen certain viewpoints during training, augmenting to out-of-distribution views won't help. The augmentations need to be small perturbations around the actual observation to probe local geometric sensitivity rather than venture into unseen regions.

This actually connects back to the spectral filtering intuition—instead of filtering guidance signals, I'm filtering the action scores themselves based on which directions are geometrically unstable. The approach would compute augmented scores from small random perturbations at each denoising step, analyze their covariance structure, and suppress the high-variance directions that indicate geometric sensitivity. The approach has several key advantages: it's training-free, works with any diffusion policy architecture, specifically targets geometric perturbations, and adds only modest computational overhead comparable to classifier-free guidance. The core difference from the original spectral filtering idea is that this filters the action score itself based on geometric sensitivity rather than filtering the video-to-action guidance signal, which means it doesn't require a specific architecture like WAM and can work with any backbone including Fast-WAM or other VLAs. I can still evaluate on LIBERO-Plus with this method, but I'm wondering whether the filtering will actually preserve enough task-relevant information.

The key insight is that under camera perturbations, some action components are inherently geometric—like XY position predictions that depend directly on camera pose—while others like gripper timing aren't. The geometric components will show high variance under small perturbations, and suppressing them means predicting less in those dimensions. But here's the subtlety: when the policy encounters a large camera shift at test time, it's already making wrong predictions. Small additional perturbations around that already-wrong state tell me about local sensitivity, but that doesn't necessarily reveal which directions are actually correct versus incorrect.

What I really want is to isolate the augmentation-consistent components—the low-variance subspace that's reliable. If a score component changes dramatically under small camera shifts, it's being driven by fine-grained spatial features that don't generalize across viewpoints. But components that stay stable across perturbations are likely driven by semantic understanding—object identity, task progress—rather than exact pixel positions. Under geometric perturbation, the semantic signal remains correct since the task and objects are unchanged, while the spatial signal breaks. So by keeping only the geometrically-stable components, I preserve the semantic signal while discarding the corrupted spatial one.

The decomposition is clean: the policy score splits into semantic and spatial components, where semantic is stable under small geometric perturbations but spatial is viewpoint-dependent. During training both are correct, giving full performance. Under perturbation, semantic stays right while spatial becomes wrong—GSF suppresses the spatial component, keeping semantic, which makes the policy more robust but potentially less precise. This hurts on pure geometric tasks like reaching exact coordinates, but most manipulation tasks only need the semantic signal once the object is localized. I can verify this empirically: if GSF helps under camera perturbation but hurts on standard conditions, that confirms the decomposition hypothesis.

This feels like a strong direction. Now I'm thinking about how to frame the full idea and what to call it.

The core problem remains the same—diffusion policies are brittle under geometric perturbation. The method is to estimate geometric sensitivity of the action score at test time through small augmentations, then project onto a geometrically-stable subspace. I'm planning to use Fast-WAM as the primary backbone since it achieves 97.6% on standard LIBERO, with Diffusion Policy as a secondary baseline. The evaluation would focus on LIBERO-Plus with camera perturbation.

One thing I need to clarify: Fast-WAM removes video features at inference, so the score I'm filtering comes purely from the action branch. That's actually fine—GSF doesn't require the video branch and works directly on the action prediction score. But I should verify whether Fast-WAM's diffusion model produces action scores I can actually manipulate in this way.

Looking at how action denoising works in Fast-WAM, the diffusion head predicts noise at each denoising step conditioned on visual features, and that prediction IS the score function I can apply GSF to. The computational cost is significant though—with K=4 augmentations and 10 denoising steps, I'd need 40 forward passes instead of 10, giving 4x overhead. That's comparable to standard classifier-free guidance which needs 2x. The visual encoder is the expensive part, and while I could cache intermediate features and only recompute from spatial processing layers, geometric augmentations fundamentally change the visual features, so that optimization won't work. I'm wondering if I should apply GSF selectively at only the most critical denoising steps to reduce overhead.

The literature on diffusion guidance suggests early steps determine coarse structure while later steps refine details, and geometric information matters most early on. So if I apply GSF only to the first 3-4 denoising steps, that's 12-16 extra forward passes total—roughly 2x overhead, which is much more reasonable.

Now I'm positioning this against related work: ADPro uses manifold constraints based on known task geometry like relative pose, whereas GSF discovers sensitivity empirically without requiring that prior knowledge, and ADPro hasn't been evaluated on LIBERO-Plus anyway. GPC composes different policies while GSF perturbs a single policy geometrically for sensitivity analysis. AnyCamVLA synthesizes new views to match the training distribution, but GSF doesn't need to do that.

There are some real concerns to address though. The 2-4x compute overhead is substantial for real-time control at 100Hz, though it's acceptable for offline LIBERO evaluation and comparable to CFG anyway. The core assumption—that small geometric augmentations at test time reveal sensitivity directions relevant to large geometric perturbations—is empirical and needs validation. And suppressing geometrically-sensitive components risks removing task-relevant information, so I need to carefully calibrate the filtering strength using a validation set, similar to how the original spectral guidance approach used AQC.

I could use a parameter-free median-based approach where I keep components with below-median variance across augmentations, or go with a softer weighting scheme that down-weights score components proportional to their variance rather than hard-filtering them. The weighting approach has just one hyperparameter and avoids SVD computation, but the SVD method is more principled and connects better to the original spectral filtering idea, so I'll explore both variants.

Now I need to search for related work to make sure this direction hasn't already been explored.

Looking at the core differences between this approach and the original method—the new approach is truly architecture-agnostic, doesn't require cross-modal CFG or the diagnostic phase, and has clearer theoretical grounding in geometric sensitivity. This feels like a major revision rather than a pivot since the problem and venue stay the same but the methodology is fundamentally different.

Now I should verify that filtering action scores based on augmentation sensitivity is actually novel and hasn't been explored elsewhere.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4432a3c2-d0c2-4643-8d05-a6d51045a483",
  "isSidechain": false,
  "requestId": "req_011CauUgA3QyYDUH9f74AET1",
  "type": "assistant",
  "uuid": "587159ea-0ad0-4a68-896e-9c09e8dd3d9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013chBEYfuX2uoZvw5g5jF8e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5817,
      "cache_read_input_tokens": 37945,
      "output_tokens": 5645,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5645,
          "cache_read_input_tokens": 37945,
          "cache_creation_input_tokens": 5817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5817
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

_source line 53 · 2026-05-10T19:59:04.853Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DbDhdTpDyeW7roUh4izx4Q`</summary>

```json
{
  "query": "\"score filtering\" OR \"score projection\" diffusion denoising augmentation sensitivity robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "587159ea-0ad0-4a68-896e-9c09e8dd3d9c",
  "isSidechain": false,
  "requestId": "req_011CauUgA3QyYDUH9f74AET1",
  "type": "assistant",
  "uuid": "2ccb33d3-4736-49bf-a61e-863e497889bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013chBEYfuX2uoZvw5g5jF8e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5817,
      "cache_read_input_tokens": 37945,
      "output_tokens": 5645,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5645,
          "cache_read_input_tokens": 37945,
          "cache_creation_input_tokens": 5817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5817
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

_source line 54 · 2026-05-10T19:59:05.383Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0154GoEWo4xM1ftqZYabnN2k`</summary>

```json
{
  "query": "geometric augmentation score variance diffusion model robustness subspace projection 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ccb33d3-4736-49bf-a61e-863e497889bb",
  "isSidechain": false,
  "requestId": "req_011CauUgA3QyYDUH9f74AET1",
  "type": "assistant",
  "uuid": "372e688a-4e17-441b-89a8-98a6f4c04ed2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013chBEYfuX2uoZvw5g5jF8e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5817,
      "cache_read_input_tokens": 37945,
      "output_tokens": 5645,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5645,
          "cache_read_input_tokens": 37945,
          "cache_creation_input_tokens": 5817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5817
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

_source line 55 · 2026-05-10T19:59:08.085Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FyjvzXpGXKweXE818nZs23`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.06266",
  "prompt": "Extract the key technical details of ADPro: 1) Exactly how does the manifold constraint work? 2) What geometric information does it use? 3) How much inference overhead? 4) What are the LIBERO results if any? 5) Does it require any task-specific information or geometric knowledge? 6) What are the main limitations?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "372e688a-4e17-441b-89a8-98a6f4c04ed2",
  "isSidechain": false,
  "requestId": "req_011CauUgA3QyYDUH9f74AET1",
  "type": "assistant",
  "uuid": "359fb277-14c8-4452-aba5-59634a58b23d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013chBEYfuX2uoZvw5g5jF8e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5817,
      "cache_read_input_tokens": 37945,
      "output_tokens": 5645,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5645,
          "cache_read_input_tokens": 37945,
          "cache_creation_input_tokens": 5817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5817
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

_source line 56_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification o…",
  "leafUuid": "359fb277-14c8-4452-aba5-59634a58b23d",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Revisit WAM geometric robustness via video-action alignment",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Tool result

_source line 58 · 2026-05-10T19:59:11.189Z_

<details><summary>↩ Tool result · `toolu_01DbDhdTpDyeW7roUh4izx4Q`</summary>

```text
Web search results for query: ""score filtering" OR "score projection" diffusion denoising augmentation sensitivity robustness 2025 2026"

Links: [{"title":"[2401.15604] Neural Network-Based Score Estimation in Diffusion Models: Optimization and Generalization","url":"https://arxiv.org/abs/2401.15604"},{"title":"Denoising Score Matching","url":"https://www.emergentmind.com/topics/denoising-score-matching"},{"title":"Neural Network-Based Score Estimation in Diffusion Models: Optimization and Generalization | OpenReview","url":"https://openreview.net/forum?id=h8GeqOxtd4"},{"title":"Denoising Score Matching with Random Features: Insights on Diffusion Models from Precise Learning Curves","url":"https://arxiv.org/html/2502.00336v1"},{"title":"To smooth a cloud or to pin it down: Expressiveness guarantees and insights on score matching in denoising diffusion models | OpenReview","url":"https://openreview.net/forum?id=BV2STKHKE6"},{"title":"[2502.00336] Denoising Score Matching with Random Features: Insights on Diffusion Models from Precise Learning Curves","url":"https://arxiv.org/abs/2502.00336"},{"title":"Optimizing Input of Denoising Score Matching is Biased Towards Higher Score Norm","url":"https://arxiv.org/html/2511.11727"},{"title":"What’s the score? Automated Denoising Score Matching for Nonlinear Diffusions","url":"https://arxiv.org/html/2407.07998v1"},{"title":"Score-based Self-supervised MRI Denoising | OpenReview","url":"https://openreview.net/forum?id=uNd289HjLi"},{"title":"Efficient Denoising using Score Embedding in Score-based Diffusion Models","url":"https://arxiv.org/html/2404.06661"}]

The search results provide relevant information about denoising score matching and diffusion models, though they don't contain specific papers on "score filtering" or "score projection" with the exact combination of terms you mentioned. Here's what I found:

## Recent Research on Denoising Score Matching and Robustness (2025-2026)

Recent work derives asymptotically precise expressions for test and train errors of denoising score matching (DSM) in generative diffusion models, with theoretical investigation of generalization and memorization phenomena in diffusion models, influenced by model complexity and training dataset size.

Theoretical and empirical advances have enhanced DSM's flexibility, robustness, and accuracy, driving its adoption in state-of-the-art generative modeling, inverse problems, uncertainty quantification, and structured data generation.

## Recent Work on Score Optimization and Sensitivity (2025)

Many recent works utilize denoising score matching to optimize the conditional input of diffusion models, though such optimization breaks the equivalence between denoising score matching and exact score matching. This bias leads to higher score norm, which has implications for model sensitivity.

The search results focus primarily on denoising score matching theory and applications rather than specific techniques called "score filtering" or "score projection." If you're looking for papers on these specific techniques, you may want to search with more specialized terminology or check recent conference proceedings from ICLR, NeurIPS, or arXiv directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ccb33d3-4736-49bf-a61e-863e497889bb",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "af2457e5-e836-4b33-800a-f6b73989a1ed",
  "toolUseResult": {
    "query": "\"score filtering\" OR \"score projection\" diffusion denoising augmentation sensitivity robustness 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014s3Zm9WomM9whCBTb2VRvm",
        "content": [
          {
            "title": "[2401.15604] Neural Network-Based Score Estimation in Diffusion Models: Optimization and Generalization",
            "url": "https://arxiv.org/abs/2401.15604"
          },
          {
            "title": "Denoising Score Matching",
            "url": "https://www.emergentmind.com/topics/denoising-score-matching"
          },
          {
            "title": "Neural Network-Based Score Estimation in Diffusion Models: Optimization and Generalization | OpenReview",
            "url": "https://openreview.net/forum?id=h8GeqOxtd4"
          },
          {
            "title": "Denoising Score Matching with Random Features: Insights on Diffusion Models from Precise Learning Curves",
            "url": "https://arxiv.org/html/2502.00336v1"
          },
          {
            "title": "To smooth a cloud or to pin it down: Expressiveness guarantees and insights on score matching in denoising diffusion models | OpenReview",
            "url": "https://openreview.net/forum?id=BV2STKHKE6"
          },
          {
            "title": "[2502.00336] Denoising Score Matching with Random Features: Insights on Diffusion Models from Precise Learning Curves",
            "url": "https://arxiv.org/abs/2502.00336"
          },
          {
            "title": "Optimizing Input of Denoising Score Matching is Biased Towards Higher Score Norm",
            "url": "https://arxiv.org/html/2511.11727"
          },
          {
            "title": "What’s the score? Automated Denoising Score Matching for Nonlinear Diffusions",
            "url": "https://arxiv.org/html/2407.07998v1"
          },
          {
            "title": "Score-based Self-supervised MRI Denoising | OpenReview",
            "url": "https://openreview.net/forum?id=uNd289HjLi"
          },
          {
            "title": "Efficient Denoising using Score Embedding in Score-based Diffusion Models",
            "url": "https://arxiv.org/html/2404.06661"
          }
        ]
      },
      "The search results provide relevant information about denoising score matching and diffusion models, though they don't contain specific papers on \"score filtering\" or \"score projection\" with the exact combination of terms you mentioned. Here's what I found:\n\n## Recent Research on Denoising Score Matching and Robustness (2025-2026)\n\nRecent work derives asymptotically precise expressions for test and train errors of denoising score matching (DSM) in generative diffusion models, with theoretical investigation of generalization and memorization phenomena in diffusion models, influenced by model complexity and training dataset size.\n\nTheoretical and empirical advances have enhanced DSM's flexibility, robustness, and accuracy, driving its adoption in state-of-the-art generative modeling, inverse problems, uncertainty quantification, and structured data generation.\n\n## Recent Work on Score Optimization and Sensitivity (2025)\n\nMany recent works utilize denoising score matching to optimize the conditional input of diffusion models, though such optimization breaks the equivalence between denoising score matching and exact score matching. This bias leads to higher score norm, which has implications for model sensitivity.\n\nThe search results focus primarily on denoising score matching theory and applications rather than specific techniques called \"score filtering\" or \"score projection.\" If you're looking for papers on these specific techniques, you may want to search with more specialized terminology or check recent conference proceedings from ICLR, NeurIPS, or arXiv directly."
    ],
    "durationSeconds": 6.32792768600001
  },
  "sourceToolAssistantUUID": "2ccb33d3-4736-49bf-a61e-863e497889bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-10T19:59:13.610Z_

<details><summary>↩ Tool result · `toolu_0154GoEWo4xM1ftqZYabnN2k`</summary>

```text
Web search results for query: "geometric augmentation score variance diffusion model robustness subspace projection 2025"

Links: [{"title":"[2508.07926] Score Augmentation for Diffusion Models","url":"https://arxiv.org/abs/2508.07926"},{"title":"Score Augmentation for Diffusion Models","url":"https://arxiv.org/html/2508.07926v1"},{"title":"Generalization in diffusion models arises from geometry-adaptive harmonic representations","url":"https://arxiv.org/html/2310.02557v3"},{"title":"Enhancing DNN Adversarial Robustness via Dual Stochasticity and Geometric Normalization - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12694524/"},{"title":"[1901.04420] Data Augmentation with Manifold Exploring Geometric Transformations for Increased Performance and Robustness","url":"https://ar5iv.labs.arxiv.org/html/1901.04420"},{"title":"Diffusion State-Guided Projected Gradient for Inverse Problems","url":"https://arxiv.org/html/2410.03463v2"},{"title":"Effective Data Augmentation With Diffusion Models","url":"https://arxiv.org/html/2302.07944v3"},{"title":"The Unreasonable Effectiveness of Gaussian Score Approximation for Diffusion Models and its Applications","url":"https://arxiv.org/html/2412.09726v1"},{"title":"A Review on Score-based Generative Models for Audio Applications","url":"https://arxiv.org/html/2506.08457v1"},{"title":"generalization in diffusion models arises from","url":"https://www.cns.nyu.edu/pub/eero/kadkhodaie24a.pdf"}]

Based on the web search results, I found several relevant papers on diffusion models, augmentation, score functions, and robustness. Here are the key findings:

## Main Results

**Score Augmentation for Diffusion Models (2025)**

The most directly relevant work is "Score Augmentation (ScoreAug)," a novel data augmentation framework specifically designed for diffusion models that applies transformations to noisy data rather than clean data, aligning with the inherent denoising mechanism of diffusion. This design establishes an equivariant learning objective, enabling the denoiser to learn scores across varied denoising spaces.

Experiments on benchmark image generation datasets (CIFAR-10, FFHQ, AFHQv2, and ImageNet) demonstrate that ScoreAug achieves significant improvements over the baseline and exhibits robust resistance to overfitting under varied settings, including reduced training data and increased model complexity.

## Related Work on Geometric and Subspace Methods

Recent work on "Diffusion State-Guided Projected Gradient (DiffStateGrad)" enhances the performance and robustness of diffusion models in solving inverse problems by projecting the measurement gradient onto a subspace that is a low-rank approximation of an intermediate state of the diffusion process.

**Variance and Score Geometry**

Research on Gaussian score approximation reveals a geometric picture of sample generation where the endpoint estimate begins at the center of the distribution and travels along the data manifold, moving first along the high variance axes and then along the lower variance axes.

These findings directly address the intersection of geometric augmentation, score functions, variance, robustness, and subspace projection in diffusion models that your query encompasses.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "372e688a-4e17-441b-89a8-98a6f4c04ed2",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "c666c89c-e9fe-4332-baad-563e274763af",
  "toolUseResult": {
    "query": "geometric augmentation score variance diffusion model robustness subspace projection 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_013qFk3e1ZW5TiryrjocsjLH",
        "content": [
          {
            "title": "[2508.07926] Score Augmentation for Diffusion Models",
            "url": "https://arxiv.org/abs/2508.07926"
          },
          {
            "title": "Score Augmentation for Diffusion Models",
            "url": "https://arxiv.org/html/2508.07926v1"
          },
          {
            "title": "Generalization in diffusion models arises from geometry-adaptive harmonic representations",
            "url": "https://arxiv.org/html/2310.02557v3"
          },
          {
            "title": "Enhancing DNN Adversarial Robustness via Dual Stochasticity and Geometric Normalization - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12694524/"
          },
          {
            "title": "[1901.04420] Data Augmentation with Manifold Exploring Geometric Transformations for Increased Performance and Robustness",
            "url": "https://ar5iv.labs.arxiv.org/html/1901.04420"
          },
          {
            "title": "Diffusion State-Guided Projected Gradient for Inverse Problems",
            "url": "https://arxiv.org/html/2410.03463v2"
          },
          {
            "title": "Effective Data Augmentation With Diffusion Models",
            "url": "https://arxiv.org/html/2302.07944v3"
          },
          {
            "title": "The Unreasonable Effectiveness of Gaussian Score Approximation for Diffusion Models and its Applications",
            "url": "https://arxiv.org/html/2412.09726v1"
          },
          {
            "title": "A Review on Score-based Generative Models for Audio Applications",
            "url": "https://arxiv.org/html/2506.08457v1"
          },
          {
            "title": "generalization in diffusion models arises from",
            "url": "https://www.cns.nyu.edu/pub/eero/kadkhodaie24a.pdf"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers on diffusion models, augmentation, score functions, and robustness. Here are the key findings:\n\n## Main Results\n\n**Score Augmentation for Diffusion Models (2025)**\n\nThe most directly relevant work is \"Score Augmentation (ScoreAug),\" a novel data augmentation framework specifically designed for diffusion models that applies transformations to noisy data rather than clean data, aligning with the inherent denoising mechanism of diffusion. This design establishes an equivariant learning objective, enabling the denoiser to learn scores across varied denoising spaces.\n\nExperiments on benchmark image generation datasets (CIFAR-10, FFHQ, AFHQv2, and ImageNet) demonstrate that ScoreAug achieves significant improvements over the baseline and exhibits robust resistance to overfitting under varied settings, including reduced training data and increased model complexity.\n\n## Related Work on Geometric and Subspace Methods\n\nRecent work on \"Diffusion State-Guided Projected Gradient (DiffStateGrad)\" enhances the performance and robustness of diffusion models in solving inverse problems by projecting the measurement gradient onto a subspace that is a low-rank approximation of an intermediate state of the diffusion process.\n\n**Variance and Score Geometry**\n\nResearch on Gaussian score approximation reveals a geometric picture of sample generation where the endpoint estimate begins at the center of the distribution and travels along the data manifold, moving first along the high variance axes and then along the lower variance axes.\n\nThese findings directly address the intersection of geometric augmentation, score functions, variance, robustness, and subspace projection in diffusion models that your query encompasses."
    ],
    "durationSeconds": 8.224362781999982
  },
  "sourceToolAssistantUUID": "372e688a-4e17-441b-89a8-98a6f4c04ed2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-10T19:59:17.064Z_

<details><summary>↩ Tool result · `toolu_01FyjvzXpGXKweXE818nZs23`</summary>

```text
# ADPro Technical Analysis

## 1) Manifold Constraint Mechanism

ADPro employs two complementary constraints. First, it applies task manifold guidance using Chamfer distance between transformed gripper and scene point clouds. The method extracts a noise-free action prediction via Tweedie's formula, then applies observation guidance: the update becomes `𝐚t−1k = 𝐚~t−1k − η∇𝐚L(𝐀^0k𝐎k,0, 𝐎k,1)`. Second, it uses spherical Gaussian constraints that normalize gradient magnitudes to prevent instability, constraining updates "to lie on a hypersphere that captures high-confidence regions."

## 2) Geometric Information Used

The approach leverages "the relative pose between the end-effector and target object" as gradient direction. It processes "two posed RGB-D images or point clouds" and uses Fast Global Registration to align gripper and scene point clouds, computing rotation and translation parameters for initialization.

## 3) Inference Overhead

ADPro shows "25% faster execution" and achieves comparable success rates with "only 20 steps, whereas the baseline requires at least 50 steps." On CALVIN, it reduces "computational time by approximately 25%." The FGR registration requires "6–10 iterations...as only a coarse estimate is required."

## 4) LIBERO Results

The paper contains no LIBERO benchmark results. Evaluation focuses on RLBench, CALVIN, and Real-world play (RealWP) datasets.

## 5) Task-Specific Requirements

ADPro is "training-free and plug-and-play" but requires point cloud observations of both gripper and target scene at test time. The authors note this "may constrain its applicable scenarios," though such data is "readily available in some datasets."

## 6) Main Limitations

The stated limitation is "reliance on both the end-effector and the scene point clouds as input." The method depends on FGR initialization quality and the pre-trained diffusion model's robustness, with error bounds influenced by registration accuracy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "359fb277-14c8-4452-aba5-59634a58b23d",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "ac6a144b-690e-4a63-ad36-34cde35d84af",
  "toolUseResult": {
    "bytes": 261844,
    "code": 200,
    "codeText": "OK",
    "result": "# ADPro Technical Analysis\n\n## 1) Manifold Constraint Mechanism\n\nADPro employs two complementary constraints. First, it applies task manifold guidance using Chamfer distance between transformed gripper and scene point clouds. The method extracts a noise-free action prediction via Tweedie's formula, then applies observation guidance: the update becomes `𝐚t−1k = 𝐚~t−1k − η∇𝐚L(𝐀^0k𝐎k,0, 𝐎k,1)`. Second, it uses spherical Gaussian constraints that normalize gradient magnitudes to prevent instability, constraining updates \"to lie on a hypersphere that captures high-confidence regions.\"\n\n## 2) Geometric Information Used\n\nThe approach leverages \"the relative pose between the end-effector and target object\" as gradient direction. It processes \"two posed RGB-D images or point clouds\" and uses Fast Global Registration to align gripper and scene point clouds, computing rotation and translation parameters for initialization.\n\n## 3) Inference Overhead\n\nADPro shows \"25% faster execution\" and achieves comparable success rates with \"only 20 steps, whereas the baseline requires at least 50 steps.\" On CALVIN, it reduces \"computational time by approximately 25%.\" The FGR registration requires \"6–10 iterations...as only a coarse estimate is required.\"\n\n## 4) LIBERO Results\n\nThe paper contains no LIBERO benchmark results. Evaluation focuses on RLBench, CALVIN, and Real-world play (RealWP) datasets.\n\n## 5) Task-Specific Requirements\n\nADPro is \"training-free and plug-and-play\" but requires point cloud observations of both gripper and target scene at test time. The authors note this \"may constrain its applicable scenarios,\" though such data is \"readily available in some datasets.\"\n\n## 6) Main Limitations\n\nThe stated limitation is \"reliance on both the end-effector and the scene point clouds as input.\" The method depends on FGR initialization quality and the pre-trained diffusion model's robustness, with error bounds influenced by registration accuracy.",
    "durationMs": 8976,
    "url": "https://arxiv.org/html/2508.06266"
  },
  "sourceToolAssistantUUID": "359fb277-14c8-4452-aba5-59634a58b23d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 61 · 2026-05-10T19:59:17.067Z_

```json
{
  "parentUuid": "ac6a144b-690e-4a63-ad36-34cde35d84af",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3ef7cd62-38ec-45eb-891b-26422a6a39e8",
  "timestamp": "2026-05-10T19:59:17.067Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 62 · 2026-05-10T19:59:29.424Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent findings! Let me analyze:

1. **Score Augmentation (ScoreAug)** - applies transformations to NOISY data for training augmentation, establishing equivariant learning. This is a TRAINING-time method, not test-time. Different from what I'm proposing.

2. **ADPro** - requires POINT CLOUD observations of both gripper and scene. This is task-specific (needs depth cameras and point cloud processing). Not evaluated on LIBERO. Has specific geometric knowledge requirements.

3. **DiffStateGrad** - projects onto low-rank subspace of intermediate diffusion state. This is for image inverse problems.


4. **Gaussian Score Approximation** - reveals geometric structure of score functions, moving along high-variance axes first.

So I'm looking at something genuinely novel here—using geometric augmentation variance at test time to identify and filter sensitivity directions in diffusion policy scores. No one's combined these ideas this way. I should verify whether Score Augmentation is truly training-only, then check if Fast-WAM or other strong WAMs have been tested on LIBERO-Plus and what their actual geometric perturbation results look like. I also need to pull the current LIBERO-Plus leaderboard to make sure I'm working with accurate baseline numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ef7cd62-38ec-45eb-891b-26422a6a39e8",
  "isSidechain": false,
  "requestId": "req_011CauUrYKtP8Fkfc3UrzWYh",
  "type": "assistant",
  "uuid": "a2f7a19d-bff0-4386-b8e1-7bff079fd631",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhW3CFgvxXEYmXFibvGkoj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7995,
      "cache_read_input_tokens": 43762,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7995,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 512,
          "cache_read_input_tokens": 43762,
          "cache_creation_input_tokens": 7995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7995
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

_source line 63 · 2026-05-10T19:59:29.434Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012oYwDDLj3Yk79QbMoY6ort`</summary>

```json
{
  "query": "LIBERO-Plus leaderboard SOTA 2026 camera robot geometric perturbation results all models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2f7a19d-bff0-4386-b8e1-7bff079fd631",
  "isSidechain": false,
  "requestId": "req_011CauUrYKtP8Fkfc3UrzWYh",
  "type": "assistant",
  "uuid": "18280efb-85b1-4693-a558-be3519bd928f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhW3CFgvxXEYmXFibvGkoj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7995,
      "cache_read_input_tokens": 43762,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7995,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 512,
          "cache_read_input_tokens": 43762,
          "cache_creation_input_tokens": 7995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7995
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

_source line 64 · 2026-05-10T19:59:29.574Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P2ozkYPz3y4CKkte1KQD7M`</summary>

```json
{
  "query": "\"score augmentation\" ScoreAug diffusion equivariant test-time OR training arXiv 2508.07926"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18280efb-85b1-4693-a558-be3519bd928f",
  "isSidechain": false,
  "requestId": "req_011CauUrYKtP8Fkfc3UrzWYh",
  "type": "assistant",
  "uuid": "661b2de6-de60-4769-ad81-069c7634f737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhW3CFgvxXEYmXFibvGkoj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7995,
      "cache_read_input_tokens": 43762,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7995,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 512,
          "cache_read_input_tokens": 43762,
          "cache_creation_input_tokens": 7995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7995
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

_source line 65 · 2026-05-10T19:59:29.997Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019tuLExfCY36VrHnnYTuQHu`</summary>

```json
{
  "query": "diffusion policy equivariance SE3 SE2 geometric transformation action space robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "661b2de6-de60-4769-ad81-069c7634f737",
  "isSidechain": false,
  "requestId": "req_011CauUrYKtP8Fkfc3UrzWYh",
  "type": "assistant",
  "uuid": "74711d63-3c92-44be-aa14-dfe7de11908d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhW3CFgvxXEYmXFibvGkoj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7995,
      "cache_read_input_tokens": 43762,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7995,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 512,
          "cache_read_input_tokens": 43762,
          "cache_creation_input_tokens": 7995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7995
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

_source line 66 · 2026-05-10T19:59:35.926Z_

<details><summary>↩ Tool result · `toolu_01P2ozkYPz3y4CKkte1KQD7M`</summary>

```text
Web search results for query: ""score augmentation" ScoreAug diffusion equivariant test-time OR training arXiv 2508.07926"

Links: [{"title":"[2508.07926] Score Augmentation for Diffusion Models","url":"https://arxiv.org/abs/2508.07926"},{"title":"Score Augmentation for Diffusion Models","url":"https://arxiv.org/html/2508.07926"},{"title":"[2508.07926v1] Score Augmentation for Diffusion Models","url":"https://arxiv.org/abs/2508.07926v1"},{"title":"Equivariant score-based generative models provably learn distributions with symmetries efficiently","url":"https://arxiv.org/html/2410.01244v1"},{"title":"Score Matching on Large Geometric Graphs for Cosmology Generation","url":"https://arxiv.org/html/2508.16990"},{"title":"[2410.06262] SymDiff: Equivariant Diffusion via Stochastic Symmetrisation","url":"https://arxiv.org/abs/2410.06262"},{"title":"The Unreasonable Effectiveness of Gaussian Score Approximation for Diffusion Models and its Applications","url":"https://arxiv.org/html/2412.09726v1"},{"title":"Guiding Diffusion Models with Reinforcement Learning for Stable Molecule Generation","url":"https://arxiv.org/html/2508.16521"},{"title":"[2410.01244] Equivariant score-based generative models provably learn distributions with symmetries efficiently","url":"https://arxiv.org/abs/2410.01244"},{"title":"Equivariant score-based generative diffusion framework for 3D molecules | BMC Bioinformatics","url":"https://link.springer.com/article/10.1186/s12859-024-05810-w"}]

Based on the search results, I found the paper you're looking for:

## Score Augmentation for Diffusion Models (arXiv 2508.07926)

Score Augmentation (ScoreAug) is a novel data augmentation framework specifically designed for diffusion models. 

**Key Concept:**
Unlike conventional data augmentation methods that exclusively target clean data, ScoreAug applies transformations to noisy data and reformulates the denoising objective to predict augmented targets, thereby establishing an equivariant learning signal.

**Technical Details:**
ScoreAug requires the denoiser to predict the augmentation of the original target, which establishes an equivariant learning objective, enabling the denoiser to learn scores across varied denoising spaces. The paper also theoretically analyzes the relationship between scores in different spaces under general transformations.

**Motivation and Results:**
The study confirms the existence of overfitting in diffusion model training, particularly in data-limited regimes. Experiments on benchmark image generation datasets (CIFAR-10, FFHQ, AFHQv2, and ImageNet) demonstrate that ScoreAug achieves significant improvements over the baseline.

You can access the full paper on arXiv at: https://arxiv.org/abs/2508.07926


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "661b2de6-de60-4769-ad81-069c7634f737",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "49d7b38d-6ede-4f9a-be68-9cd6047737f9",
  "toolUseResult": {
    "query": "\"score augmentation\" ScoreAug diffusion equivariant test-time OR training arXiv 2508.07926",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Bb6zEdWX4dSGqWQLGRtRqg",
        "content": [
          {
            "title": "[2508.07926] Score Augmentation for Diffusion Models",
            "url": "https://arxiv.org/abs/2508.07926"
          },
          {
            "title": "Score Augmentation for Diffusion Models",
            "url": "https://arxiv.org/html/2508.07926"
          },
          {
            "title": "[2508.07926v1] Score Augmentation for Diffusion Models",
            "url": "https://arxiv.org/abs/2508.07926v1"
          },
          {
            "title": "Equivariant score-based generative models provably learn distributions with symmetries efficiently",
            "url": "https://arxiv.org/html/2410.01244v1"
          },
          {
            "title": "Score Matching on Large Geometric Graphs for Cosmology Generation",
            "url": "https://arxiv.org/html/2508.16990"
          },
          {
            "title": "[2410.06262] SymDiff: Equivariant Diffusion via Stochastic Symmetrisation",
            "url": "https://arxiv.org/abs/2410.06262"
          },
          {
            "title": "The Unreasonable Effectiveness of Gaussian Score Approximation for Diffusion Models and its Applications",
            "url": "https://arxiv.org/html/2412.09726v1"
          },
          {
            "title": "Guiding Diffusion Models with Reinforcement Learning for Stable Molecule Generation",
            "url": "https://arxiv.org/html/2508.16521"
          },
          {
            "title": "[2410.01244] Equivariant score-based generative models provably learn distributions with symmetries efficiently",
            "url": "https://arxiv.org/abs/2410.01244"
          },
          {
            "title": "Equivariant score-based generative diffusion framework for 3D molecules | BMC Bioinformatics",
            "url": "https://link.springer.com/article/10.1186/s12859-024-05810-w"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n## Score Augmentation for Diffusion Models (arXiv 2508.07926)\n\nScore Augmentation (ScoreAug) is a novel data augmentation framework specifically designed for diffusion models. \n\n**Key Concept:**\nUnlike conventional data augmentation methods that exclusively target clean data, ScoreAug applies transformations to noisy data and reformulates the denoising objective to predict augmented targets, thereby establishing an equivariant learning signal.\n\n**Technical Details:**\nScoreAug requires the denoiser to predict the augmentation of the original target, which establishes an equivariant learning objective, enabling the denoiser to learn scores across varied denoising spaces. The paper also theoretically analyzes the relationship between scores in different spaces under general transformations.\n\n**Motivation and Results:**\nThe study confirms the existence of overfitting in diffusion model training, particularly in data-limited regimes. Experiments on benchmark image generation datasets (CIFAR-10, FFHQ, AFHQv2, and ImageNet) demonstrate that ScoreAug achieves significant improvements over the baseline.\n\nYou can access the full paper on arXiv at: https://arxiv.org/abs/2508.07926"
    ],
    "durationSeconds": 6.348797657999967
  },
  "sourceToolAssistantUUID": "661b2de6-de60-4769-ad81-069c7634f737",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 67_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification o…",
  "leafUuid": "49d7b38d-6ede-4f9a-be68-9cd6047737f9",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Revisit WAM geometric robustness via video-action alignment",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Tool result

_source line 69 · 2026-05-10T19:59:37.888Z_

<details><summary>↩ Tool result · `toolu_019tuLExfCY36VrHnnYTuQHu`</summary>

```text
Web search results for query: "diffusion policy equivariance SE3 SE2 geometric transformation action space robot 2025 2026"

Links: [{"title":"SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space | OpenReview","url":"https://openreview.net/forum?id=U5nRMOs8Ed"},{"title":"SE⁢(3)-Equivariant Diffusion Policy in Spherical Fourier Space","url":"https://arxiv.org/html/2507.01723"},{"title":"[2507.01723] SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space","url":"https://arxiv.org/abs/2507.01723"},{"title":"[2503.09829] SE(3)-Equivariant Robot Learning and Control: A Tutorial Survey","url":"https://arxiv.org/abs/2503.09829"},{"title":"SE(3) - Equivariant diffusion policy in spherical Fourier space - Amazon Science","url":"https://www.amazon.science/publications/se3-equivariant-diffusion-policy-in-spherical-fourier-space"},{"title":"EquiBot: SIM(3)-Equivariant Diffusion Policy for Generalizable and Data Efficient Learning","url":"https://arxiv.org/html/2407.01479v2"},{"title":"ReSeFlow: Rectifying SE(3)-Equivariant Policy Learning Flows","url":"https://arxiv.org/html/2509.22695"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Original article The International Journal of Robotics Research","url":"https://journals.sagepub.com/doi/pdf/10.1177/02783649261424445"},{"title":"EquAct: An SE(3)-Equivariant Multi-Task Transformer for Open-Loop Robotic Manipulation","url":"https://arxiv.org/html/2505.21351v1"}]

I've performed the web search for your query. Here are the key findings on diffusion policy with SE(3) equivariance and geometric transformations for robot action spaces from recent 2025-2026 research:

## Key Recent Work

**Spherical Diffusion Policy (SDP)**: SDP is an SE(3) equivariant diffusion policy that adapts trajectories according to 3D transformations of the scene, achieved by embedding the states, actions, and the denoising process in spherical Fourier space. SDP demonstrates a large performance improvement over strong baselines in 20 simulation tasks and 5 physical robot tasks including single-arm and bi-manual embodiments.

**EquiBot**: This approach combines SIM(3)-equivariant neural network architectures with diffusion models, ensuring that learned policies are invariant to changes in scale, rotation, and translation, enhancing their applicability to unseen environments.

**ReSeFlow**: This work was submitted to the 2026 IEEE International Conference on Robotics & Automation and develops SE(3)-equivariant diffusion models that are data-efficient, setting a new technical benchmark for data-efficient and inference-efficient robotic policy learning.

**EquAct**: This is a novel SE(3)-equivariant multi-task transformer that leverages SE(3) equivariance as a key structural property shared by both policy and language.

**Tutorial Survey**: Recent work discusses applications of SE(3)-equivariant neural networks in robotics in terms of imitation learning and reinforcement learning, with SE(3)-equivariant control design reviewed from the perspective of geometric control.

These methods address the challenge of generalizing robot policies to novel 3D object arrangements and transformations through geometric equivariance constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74711d63-3c92-44be-aa14-dfe7de11908d",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "b7c5813e-b9bf-4680-9c54-41cc154a73be",
  "toolUseResult": {
    "query": "diffusion policy equivariance SE3 SE2 geometric transformation action space robot 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LMaiJzvT1obEnf2ZyqTiFc",
        "content": [
          {
            "title": "SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space | OpenReview",
            "url": "https://openreview.net/forum?id=U5nRMOs8Ed"
          },
          {
            "title": "SE⁢(3)-Equivariant Diffusion Policy in Spherical Fourier Space",
            "url": "https://arxiv.org/html/2507.01723"
          },
          {
            "title": "[2507.01723] SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space",
            "url": "https://arxiv.org/abs/2507.01723"
          },
          {
            "title": "[2503.09829] SE(3)-Equivariant Robot Learning and Control: A Tutorial Survey",
            "url": "https://arxiv.org/abs/2503.09829"
          },
          {
            "title": "SE(3) - Equivariant diffusion policy in spherical Fourier space - Amazon Science",
            "url": "https://www.amazon.science/publications/se3-equivariant-diffusion-policy-in-spherical-fourier-space"
          },
          {
            "title": "EquiBot: SIM(3)-Equivariant Diffusion Policy for Generalizable and Data Efficient Learning",
            "url": "https://arxiv.org/html/2407.01479v2"
          },
          {
            "title": "ReSeFlow: Rectifying SE(3)-Equivariant Policy Learning Flows",
            "url": "https://arxiv.org/html/2509.22695"
          },
          {
            "title": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
            "url": "https://diffusion-policy.cs.columbia.edu/"
          },
          {
            "title": "Original article The International Journal of Robotics Research",
            "url": "https://journals.sagepub.com/doi/pdf/10.1177/02783649261424445"
          },
          {
            "title": "EquAct: An SE(3)-Equivariant Multi-Task Transformer for Open-Loop Robotic Manipulation",
            "url": "https://arxiv.org/html/2505.21351v1"
          }
        ]
      },
      "I've performed the web search for your query. Here are the key findings on diffusion policy with SE(3) equivariance and geometric transformations for robot action spaces from recent 2025-2026 research:\n\n## Key Recent Work\n\n**Spherical Diffusion Policy (SDP)**: SDP is an SE(3) equivariant diffusion policy that adapts trajectories according to 3D transformations of the scene, achieved by embedding the states, actions, and the denoising process in spherical Fourier space. SDP demonstrates a large performance improvement over strong baselines in 20 simulation tasks and 5 physical robot tasks including single-arm and bi-manual embodiments.\n\n**EquiBot**: This approach combines SIM(3)-equivariant neural network architectures with diffusion models, ensuring that learned policies are invariant to changes in scale, rotation, and translation, enhancing their applicability to unseen environments.\n\n**ReSeFlow**: This work was submitted to the 2026 IEEE International Conference on Robotics & Automation and develops SE(3)-equivariant diffusion models that are data-efficient, setting a new technical benchmark for data-efficient and inference-efficient robotic policy learning.\n\n**EquAct**: This is a novel SE(3)-equivariant multi-task transformer that leverages SE(3) equivariance as a key structural property shared by both policy and language.\n\n**Tutorial Survey**: Recent work discusses applications of SE(3)-equivariant neural networks in robotics in terms of imitation learning and reinforcement learning, with SE(3)-equivariant control design reviewed from the perspective of geometric control.\n\nThese methods address the challenge of generalizing robot policies to novel 3D object arrangements and transformations through geometric equivariance constraints."
    ],
    "durationSeconds": 7.889287114999956
  },
  "sourceToolAssistantUUID": "74711d63-3c92-44be-aa14-dfe7de11908d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-10T19:59:38.097Z_

<details><summary>↩ Tool result · `toolu_012oYwDDLj3Yk79QbMoY6ort`</summary>

```text
Web search results for query: "LIBERO-Plus leaderboard SOTA 2026 camera robot geometric perturbation results all models"

Links: [{"title":"VLA SOTA Leaderboard","url":"https://sota.evomind-tech.com/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Would you like to set up an online leaderboard for SOTA methods on libero? · Issue #25 · Lifelong-Robot-Learning/LIBERO","url":"https://github.com/Lifelong-Robot-Learning/LIBERO/issues/25"},{"title":"LIDEA: Human-to-Robot Imitation Learning via Implicit Feature Distillation and Explicit Geometry Alignment","url":"https://yifuxu1127.github.io/LIDEA/"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"VLA & Dexterous Manipulation SOTA Leaderboard","url":"https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"}]

Based on the search results, I found information about the LIBERO-Plus leaderboard and camera robot geometric perturbation results. Here's what I found:

## LIBERO-Plus Benchmark Overview

LIBERO Plus is an extended benchmark testing robustness across 7 perturbation dimensions: Camera, Robot, Language, Light, Background, Noise, and Layout. The benchmark consists of 10,030 tasks spanning seven perturbation dimensions, with a diverse training dataset of over 20,000 successful trajectories.

## Camera and Robot (Geometric) Perturbation Results

The research revealed critical vulnerabilities in current VLA models under geometric perturbations:

**Camera Viewpoint Perturbations:** Models are most vulnerable to changes in camera viewpoint and robot initial state, which require a high-level understanding of spatial geometry and proprioception. More specifically, models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

## Model Performance on LIBERO-Plus

LaMP achieves 98.3% SOTA on LIBERO benchmark and 96.7% on challenging long-horizon tasks, and on LIBERO-Plus OOD perturbations, it outperforms the strongest baseline by +9.7%.

The leaderboard is available at multiple locations, including a comprehensive leaderboard tracking the state-of-the-art (SOTA) performance of Vision-Language-Action (VLA) models across multiple robotics benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18280efb-85b1-4693-a558-be3519bd928f",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "83437cbd-95db-4411-88ac-05623e2be04f",
  "toolUseResult": {
    "query": "LIBERO-Plus leaderboard SOTA 2026 camera robot geometric perturbation results all models",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NjHzTXFbeBv5FbQnrGYvRg",
        "content": [
          {
            "title": "VLA SOTA Leaderboard",
            "url": "https://sota.evomind-tech.com/"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "Would you like to set up an online leaderboard for SOTA methods on libero? · Issue #25 · Lifelong-Robot-Learning/LIBERO",
            "url": "https://github.com/Lifelong-Robot-Learning/LIBERO/issues/25"
          },
          {
            "title": "LIDEA: Human-to-Robot Imitation Learning via Implicit Feature Distillation and Explicit Geometry Alignment",
            "url": "https://yifuxu1127.github.io/LIDEA/"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "VLA & Dexterous Manipulation SOTA Leaderboard",
            "url": "https://github.com/MINT-SJTU/Evo-SOTA.io/blob/main/README.md"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          }
        ]
      },
      "Based on the search results, I found information about the LIBERO-Plus leaderboard and camera robot geometric perturbation results. Here's what I found:\n\n## LIBERO-Plus Benchmark Overview\n\nLIBERO Plus is an extended benchmark testing robustness across 7 perturbation dimensions: Camera, Robot, Language, Light, Background, Noise, and Layout. The benchmark consists of 10,030 tasks spanning seven perturbation dimensions, with a diverse training dataset of over 20,000 successful trajectories.\n\n## Camera and Robot (Geometric) Perturbation Results\n\nThe research revealed critical vulnerabilities in current VLA models under geometric perturbations:\n\n**Camera Viewpoint Perturbations:** Models are most vulnerable to changes in camera viewpoint and robot initial state, which require a high-level understanding of spatial geometry and proprioception. More specifically, models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.\n\n## Model Performance on LIBERO-Plus\n\nLaMP achieves 98.3% SOTA on LIBERO benchmark and 96.7% on challenging long-horizon tasks, and on LIBERO-Plus OOD perturbations, it outperforms the strongest baseline by +9.7%.\n\nThe leaderboard is available at multiple locations, including a comprehensive leaderboard tracking the state-of-the-art (SOTA) performance of Vision-Language-Action (VLA) models across multiple robotics benchmarks."
    ],
    "durationSeconds": 8.659564260999963
  },
  "sourceToolAssistantUUID": "18280efb-85b1-4693-a558-be3519bd928f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-10T19:59:49.626Z_

<details><summary>Logged reasoning block</summary>

```text
This is very important! Let me analyze:

1. **LaMP** achieves 98.3% on standard LIBERO and outperforms the strongest baseline by +9.7% on LIBERO-Plus. This is a NEW SOTA I wasn't aware of. Let me search more about LaMP.

2. **SE(3)-Equivariant Diffusion Policy (SDP)** - This is VERY relevant! It enforces equivariance by construction through spherical Fourier space. This is a TRAINING-time approach (requires training with equivariant architecture). My proposed test-time method would be complementary.


3. **ScoreAug**, **EquiBot**, **ReSeFlow**, and **EquAct** are all training-time methods too—either augmenting data during training or building equivariance into the architecture itself. The critical realization here is that every existing approach to geometric robustness requires modifications at training time. There's a genuine gap for test-time enforcement of equivariance on pre-trained, non-equivariant diffusion policies, which is exactly what I'm proposing.

Now I need to check LaMP to see what the current state-of-the-art looks like before I lock in my final direction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83437cbd-95db-4411-88ac-05623e2be04f",
  "isSidechain": false,
  "requestId": "req_011CauUt6H38NijdRb8FRLnT",
  "type": "assistant",
  "uuid": "c2de2c7c-8849-4f5e-8898-ab26efa596e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EQet44tqtw5QM5bcra1fG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1765,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 51757,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1765,
          "output_tokens": 522,
          "cache_read_input_tokens": 51757,
          "cache_creation_input_tokens": 1421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1421
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

_source line 72 · 2026-05-10T19:59:49.638Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GEtLTKjkmdnyHs8Bk1gj9M`</summary>

```json
{
  "query": "LaMP LIBERO-Plus SOTA 98.3% 2026 VLA robustness perturbation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2de2c7c-8849-4f5e-8898-ab26efa596e8",
  "isSidechain": false,
  "requestId": "req_011CauUt6H38NijdRb8FRLnT",
  "type": "assistant",
  "uuid": "4f26f38d-df96-446f-b6b7-d09bd96f48f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EQet44tqtw5QM5bcra1fG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1765,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 51757,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1765,
          "output_tokens": 522,
          "cache_read_input_tokens": 51757,
          "cache_creation_input_tokens": 1421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1421
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

_source line 73 · 2026-05-10T19:59:49.686Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A4a2kEYjQtmvxUCGjGn2Ho`</summary>

```json
{
  "query": "SE3 equivariant diffusion policy spherical Fourier SDP LIBERO generalization viewpoint 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f26f38d-df96-446f-b6b7-d09bd96f48f8",
  "isSidechain": false,
  "requestId": "req_011CauUt6H38NijdRb8FRLnT",
  "type": "assistant",
  "uuid": "193e8d7a-38cf-498b-bbd0-5ff06f1e189b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EQet44tqtw5QM5bcra1fG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1765,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 51757,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1765,
          "output_tokens": 522,
          "cache_read_input_tokens": 51757,
          "cache_creation_input_tokens": 1421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1421
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

_source line 74 · 2026-05-10T19:59:50.222Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011v8M6F7XRkQcXQxNdSs3b3`</summary>

```json
{
  "query": "Fast-WAM diffusion action head architecture inference denoising steps LIBERO 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "193e8d7a-38cf-498b-bbd0-5ff06f1e189b",
  "isSidechain": false,
  "requestId": "req_011CauUt6H38NijdRb8FRLnT",
  "type": "assistant",
  "uuid": "f44dd2cc-f0f5-491f-8106-84232b9791a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EQet44tqtw5QM5bcra1fG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1765,
      "cache_creation_input_tokens": 1421,
      "cache_read_input_tokens": 51757,
      "output_tokens": 522,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1421,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1765,
          "output_tokens": 522,
          "cache_read_input_tokens": 51757,
          "cache_creation_input_tokens": 1421,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1421
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

_source line 75 · 2026-05-10T19:59:57.530Z_

<details><summary>↩ Tool result · `toolu_011v8M6F7XRkQcXQxNdSs3b3`</summary>

```text
Web search results for query: "Fast-WAM diffusion action head architecture inference denoising steps LIBERO 2026"

Links: [{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666v1"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://yuantianyuan01.github.io/FastWAM/"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/html/2508.20072v1"},{"title":"WAM-Diff: A Masked Diffusion VLA Framework with MoE and Online Reinforcement Learning for Autonomous Driving","url":"https://arxiv.org/html/2512.11872v1"},{"title":"Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance","url":"https://arxiv.org/html/2603.25661"},{"title":"X-WAM: Bridging Action and 4D Synthesis | StartupHub.ai","url":"https://www.startuphub.ai/ai-news/ai-research/2026/x-wam-bridging-action-and-4d-synthesis"},{"title":"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation","url":"https://arxiv.org/html/2604.05656v1"},{"title":"Dream-VL & Dream-VLA: Open Vision-Language and ...","url":"https://arxiv.org/pdf/2512.22615"},{"title":"MMaDA-VLA: LARGE DIFFUSION VISION-LANGUAGE-ACTION MODEL WITH","url":"https://arxiv.org/pdf/2603.25406"},{"title":"Preprint. Under Review dVLA: DIFFUSION VISION-LANGUAGE-ACTION","url":"https://arxiv.org/pdf/2509.25681"}]

Based on the search results, here's information about Fast-WAM and related diffusion-based action generation architectures:

## Fast-WAM Overview

Fast-WAM is a WAM architecture that retains video co-training during training but skips future prediction at test time. Fast-WAM retains video co-training during training but removes explicit future generation at inference time, directly predicting actions from latent world representations in a single forward pass.

## Inference and Denoising

At inference time, Fast-WAM keeps only the clean latent tokens of the current observation, processes them with the video backbone once, and directly generates actions without explicit future video denoising. This design eliminates the iterative denoising steps required by traditional world action models.

## Key Architectural Difference

Existing WAMs can be broadly grouped into two representative paradigms: (A) future videos and actions are jointly denoised with shared attention; and (B) actions are predicted after, and conditioned on, generated future videos. Fast-WAM represents a third paradigm that sidesteps future video generation entirely at inference time.

## Performance on LIBERO Benchmark

Experiments on simulation benchmarks (LIBERO and RoboTwin) show that Fast-WAM achieves strong results without any embodied pretraining, demonstrating strong data efficiency. Additionally, Fast-WAM achieves competitive results on LIBERO, RoboTwin, and real-world towel folding without embodied pretraining, and runs in real time with 190 ms latency, more than 4x faster than existing imagine-then-execute WAM designs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f44dd2cc-f0f5-491f-8106-84232b9791a4",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "c4f30f5e-41a5-47b4-8858-6ce20690342f",
  "toolUseResult": {
    "query": "Fast-WAM diffusion action head architecture inference denoising steps LIBERO 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Kww4QqL9Ae5936GfJb6Cnf",
        "content": [
          {
            "title": "Fast-WAM: Do World Action Models Need Test-time Future Imagination?",
            "url": "https://arxiv.org/html/2603.16666v1"
          },
          {
            "title": "Fast-WAM: Do World Action Models Need Test-time Future Imagination?",
            "url": "https://yuantianyuan01.github.io/FastWAM/"
          },
          {
            "title": "Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies",
            "url": "https://arxiv.org/html/2508.20072v1"
          },
          {
            "title": "WAM-Diff: A Masked Diffusion VLA Framework with MoE and Online Reinforcement Learning for Autonomous Driving",
            "url": "https://arxiv.org/html/2512.11872v1"
          },
          {
            "title": "Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance",
            "url": "https://arxiv.org/html/2603.25661"
          },
          {
            "title": "X-WAM: Bridging Action and 4D Synthesis | StartupHub.ai",
            "url": "https://www.startuphub.ai/ai-news/ai-research/2026/x-wam-bridging-action-and-4d-synthesis"
          },
          {
            "title": "SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation",
            "url": "https://arxiv.org/html/2604.05656v1"
          },
          {
            "title": "Dream-VL & Dream-VLA: Open Vision-Language and ...",
            "url": "https://arxiv.org/pdf/2512.22615"
          },
          {
            "title": "MMaDA-VLA: LARGE DIFFUSION VISION-LANGUAGE-ACTION MODEL WITH",
            "url": "https://arxiv.org/pdf/2603.25406"
          },
          {
            "title": "Preprint. Under Review dVLA: DIFFUSION VISION-LANGUAGE-ACTION",
            "url": "https://arxiv.org/pdf/2509.25681"
          }
        ]
      },
      "Based on the search results, here's information about Fast-WAM and related diffusion-based action generation architectures:\n\n## Fast-WAM Overview\n\nFast-WAM is a WAM architecture that retains video co-training during training but skips future prediction at test time. Fast-WAM retains video co-training during training but removes explicit future generation at inference time, directly predicting actions from latent world representations in a single forward pass.\n\n## Inference and Denoising\n\nAt inference time, Fast-WAM keeps only the clean latent tokens of the current observation, processes them with the video backbone once, and directly generates actions without explicit future video denoising. This design eliminates the iterative denoising steps required by traditional world action models.\n\n## Key Architectural Difference\n\nExisting WAMs can be broadly grouped into two representative paradigms: (A) future videos and actions are jointly denoised with shared attention; and (B) actions are predicted after, and conditioned on, generated future videos. Fast-WAM represents a third paradigm that sidesteps future video generation entirely at inference time.\n\n## Performance on LIBERO Benchmark\n\nExperiments on simulation benchmarks (LIBERO and RoboTwin) show that Fast-WAM achieves strong results without any embodied pretraining, demonstrating strong data efficiency. Additionally, Fast-WAM achieves competitive results on LIBERO, RoboTwin, and real-world towel folding without embodied pretraining, and runs in real time with 190 ms latency, more than 4x faster than existing imagine-then-execute WAM designs."
    ],
    "durationSeconds": 7.305164370999963
  },
  "sourceToolAssistantUUID": "f44dd2cc-f0f5-491f-8106-84232b9791a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-10T19:59:58.113Z_

<details><summary>↩ Tool result · `toolu_01GEtLTKjkmdnyHs8Bk1gj9M`</summary>

```text
Web search results for query: "LaMP LIBERO-Plus SOTA 98.3% 2026 VLA robustness perturbation"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"VLA SOTA Leaderboard","url":"https://sota.evomind-tech.com/"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301"},{"title":"Published as a conference paper at ICLR 2026 ON ROBUSTNESS","url":"https://arxiv.org/pdf/2510.00037v4"}]

I found comprehensive information about LIBERO-Plus and its findings related to VLA robustness. Here's what the search results reveal:

## LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models

LIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities across key vulnerability dimensions in Vision-Language-Action (VLA) models.

### Key Findings on Robustness

Reported LIBERO SOTA models degrade from approximately 98% to 0–40% in perturbed regimes. More specifically, models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

### Perturbation Dimensions

The analysis introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

### Critical Weaknesses Identified

The research reveals several fundamental issues:

- Models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely
- Models demonstrate an ability to ignore distracting objects, but fail to generalize when target objects are displaced, indicating they rely on memorized positional cues rather than learning invariant object semantics
- Current VLA models lack compositional generalization capabilities, with their learned representations entangled and unable to handle complex, multi-dimensional perturbations that characterize real-world environments


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f26f38d-df96-446f-b6b7-d09bd96f48f8",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "0c158dac-cc51-46bb-8a2e-e22cbeedcd2d",
  "toolUseResult": {
    "query": "LaMP LIBERO-Plus SOTA 98.3% 2026 VLA robustness perturbation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EsTg7VJNGjTX4sxnAUJAnJ",
        "content": [
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "VLA SOTA Leaderboard",
            "url": "https://sota.evomind-tech.com/"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 ON ROBUSTNESS",
            "url": "https://arxiv.org/pdf/2510.00037v4"
          }
        ]
      },
      "I found comprehensive information about LIBERO-Plus and its findings related to VLA robustness. Here's what the search results reveal:\n\n## LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\n\nLIBERO-Plus is a comprehensive benchmark designed to establish a rigorous leaderboard for evaluating generalization capabilities across key vulnerability dimensions in Vision-Language-Action (VLA) models.\n\n### Key Findings on Robustness\n\nReported LIBERO SOTA models degrade from approximately 98% to 0–40% in perturbed regimes. More specifically, models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.\n\n### Perturbation Dimensions\n\nThe analysis introduces controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.\n\n### Critical Weaknesses Identified\n\nThe research reveals several fundamental issues:\n\n- Models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely\n- Models demonstrate an ability to ignore distracting objects, but fail to generalize when target objects are displaced, indicating they rely on memorized positional cues rather than learning invariant object semantics\n- Current VLA models lack compositional generalization capabilities, with their learned representations entangled and unable to handle complex, multi-dimensional perturbations that characterize real-world environments"
    ],
    "durationSeconds": 8.470442055000051
  },
  "sourceToolAssistantUUID": "4f26f38d-df96-446f-b6b7-d09bd96f48f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification o…",
  "leafUuid": "0c158dac-cc51-46bb-8a2e-e22cbeedcd2d",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 78_

```json
{
  "type": "ai-title",
  "aiTitle": "Revisit WAM geometric robustness via video-action alignment",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Tool result

_source line 79 · 2026-05-10T19:59:58.680Z_

<details><summary>↩ Tool result · `toolu_01A4a2kEYjQtmvxUCGjGn2Ho`</summary>

```text
Web search results for query: "SE3 equivariant diffusion policy spherical Fourier SDP LIBERO generalization viewpoint 2025 2026"

Links: [{"title":"SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space | OpenReview","url":"https://openreview.net/forum?id=U5nRMOs8Ed"},{"title":"[2507.01723] SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space","url":"https://arxiv.org/abs/2507.01723"},{"title":"SE(3) - Equivariant diffusion policy in spherical Fourier space - Amazon Science","url":"https://www.amazon.science/publications/se3-equivariant-diffusion-policy-in-spherical-fourier-space"},{"title":"SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250701723Z/abstract"},{"title":"ICML Poster SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space","url":"https://icml.cc/virtual/2025/poster/45141"},{"title":"GitHub - amazon-science/Spherical_Diffusion_Policy: [ICML 2025] Official implementation of Spherical Diffusion Policy: A SE(3) Equivariant Visuomotor Policy with Spherical Fourier Representation","url":"https://github.com/amazon-science/Spherical_Diffusion_Policy"},{"title":"[Literature Review] SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space","url":"https://www.themoonlight.io/en/review/se3-equivariant-diffusion-policy-in-spherical-fourier-space"},{"title":"SE⁢(3)-Equivariant Diffusion Policy in Spherical Fourier Space","url":"https://arxiv.org/html/2507.01723v1"},{"title":"3D Equivariant Visuomotor Policy Learning via Spherical Projection | OpenReview","url":"https://openreview.net/forum?id=kXJd4JxF34"},{"title":"3D Equivariant Visuomotor Policy Learning via Spherical Projection","url":"https://isp-3d.github.io/"}]

Based on the search results, I found information about the SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space (SDP) research:

## SE(3) Equivariant Diffusion Policy with Spherical Fourier Space

Spherical Diffusion Policy (SDP) is an SE(3) equivariant diffusion policy that adapts trajectories according to 3D transformations of the scene. Such equivariance is achieved by embedding the states, actions, and the denoising process in spherical Fourier space.

### Key Technical Innovations

The method embeds states, actions, and the denoising process in spherical Fourier space, employs novel spherical FiLM layers to condition the action denoising process equivariantly on scene embeddings, and proposes a spherical denoising temporal U-net that achieves spatiotemporal equivariance with computational efficiency.

### Performance and Generalization

SDP is end-to-end SE(3) equivariant, allowing robust generalization across transformed 3D scenes, and demonstrates a large performance improvement over strong baselines in 20 simulation tasks and 5 physical robot tasks including single-arm and bi-manual embodiments. Experiments demonstrated significant performance improvements over strong baselines like DiffPo, EquiDiff, and EquiBot, especially in tasks with large SE(3) variations.

### Publication

The work was published at ICML 2025 with official implementation available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "193e8d7a-38cf-498b-bbd0-5ff06f1e189b",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "8f864c71-8fca-4d61-b558-52b62f2ed68a",
  "toolUseResult": {
    "query": "SE3 equivariant diffusion policy spherical Fourier SDP LIBERO generalization viewpoint 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VcfZ993VhounXT7yEgteeT",
        "content": [
          {
            "title": "SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space | OpenReview",
            "url": "https://openreview.net/forum?id=U5nRMOs8Ed"
          },
          {
            "title": "[2507.01723] SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space",
            "url": "https://arxiv.org/abs/2507.01723"
          },
          {
            "title": "SE(3) - Equivariant diffusion policy in spherical Fourier space - Amazon Science",
            "url": "https://www.amazon.science/publications/se3-equivariant-diffusion-policy-in-spherical-fourier-space"
          },
          {
            "title": "SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250701723Z/abstract"
          },
          {
            "title": "ICML Poster SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space",
            "url": "https://icml.cc/virtual/2025/poster/45141"
          },
          {
            "title": "GitHub - amazon-science/Spherical_Diffusion_Policy: [ICML 2025] Official implementation of Spherical Diffusion Policy: A SE(3) Equivariant Visuomotor Policy with Spherical Fourier Representation",
            "url": "https://github.com/amazon-science/Spherical_Diffusion_Policy"
          },
          {
            "title": "[Literature Review] SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space",
            "url": "https://www.themoonlight.io/en/review/se3-equivariant-diffusion-policy-in-spherical-fourier-space"
          },
          {
            "title": "SE⁢(3)-Equivariant Diffusion Policy in Spherical Fourier Space",
            "url": "https://arxiv.org/html/2507.01723v1"
          },
          {
            "title": "3D Equivariant Visuomotor Policy Learning via Spherical Projection | OpenReview",
            "url": "https://openreview.net/forum?id=kXJd4JxF34"
          },
          {
            "title": "3D Equivariant Visuomotor Policy Learning via Spherical Projection",
            "url": "https://isp-3d.github.io/"
          }
        ]
      },
      "Based on the search results, I found information about the SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space (SDP) research:\n\n## SE(3) Equivariant Diffusion Policy with Spherical Fourier Space\n\nSpherical Diffusion Policy (SDP) is an SE(3) equivariant diffusion policy that adapts trajectories according to 3D transformations of the scene. Such equivariance is achieved by embedding the states, actions, and the denoising process in spherical Fourier space.\n\n### Key Technical Innovations\n\nThe method embeds states, actions, and the denoising process in spherical Fourier space, employs novel spherical FiLM layers to condition the action denoising process equivariantly on scene embeddings, and proposes a spherical denoising temporal U-net that achieves spatiotemporal equivariance with computational efficiency.\n\n### Performance and Generalization\n\nSDP is end-to-end SE(3) equivariant, allowing robust generalization across transformed 3D scenes, and demonstrates a large performance improvement over strong baselines in 20 simulation tasks and 5 physical robot tasks including single-arm and bi-manual embodiments. Experiments demonstrated significant performance improvements over strong baselines like DiffPo, EquiDiff, and EquiBot, especially in tasks with large SE(3) variations.\n\n### Publication\n\nThe work was published at ICML 2025 with official implementation available on GitHub."
    ],
    "durationSeconds": 8.991884870999959
  },
  "sourceToolAssistantUUID": "193e8d7a-38cf-498b-bbd0-5ff06f1e189b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 80 · 2026-05-10T20:00:42.721Z_

<details><summary>Logged reasoning block</summary>

```text
OK, now I have a much clearer picture. Let me check one more thing - LaMP doesn't seem to be a real paper from my searches. Let me check the SOTA leaderboard more carefully. Actually, the search result mentioned "LaMP achieves 98.3% SOTA on LIBERO benchmark" - let me verify this.

Actually wait, looking at the search results more carefully, the 98.3% claim about LaMP came from the EvoMind SOTA Leaderboard page. Let me check that. But for now, I'll note that the original idea's numbers (Being-H0.7: 99.2%, Fast-WAM: 97.6%) are still roughly in the right ballpark for standard LIBERO SOTA.
 
Now I'm looking at the specific performance metrics across different approaches. The key insight is that LIBERO-Plus shows dramatic drops under geometric perturbation, while OA-WAM and CKT-WAM maintain more reasonable performance. What's striking is that all the equivariant methods—SDP, EquiBot, ReSeFlow—require equivariant architectures at training time, meaning there's currently no test-time geometric robustness solution for diffusion policies on LIBERO-Plus. Fast-WAM stands out because it achieves this with just a single forward pass rather than iterative denoising.

I need to clarify whether Fast-WAM actually uses diffusion for action generation or if it's doing something fundamentally different—the description about "directly predicting actions from latent world representations in a single forward pass" is ambiguous, but the mention of CFG scale suggests it still leverages diffusion somehow, just with a different inference strategy.

Now I'm thinking through what I actually need to know: whether the backbone uses iterative diffusion denoising for actions (which it does for most WAMs), and whether I can modify that denoising process at test time (which I can). So I need to decide which backbone to evaluate against.

Fast-WAM looks promising at 97.6% on standard LIBERO with diffusion-based actions and cached backbone features, though its 190ms inference suggests the diffusion head is relatively lightweight. Being-H0.7 achieves 99.2% but uses latent world-action queries that might not follow a standard diffusion process. The real constraint is that if I apply geometric augmentations for score filtering, I'd need to rerun the expensive backbone for each augmented view, even though the diffusion iterations themselves are cheap. I'm starting to think about whether I should only augment the visual inputs at a specific stage rather than recomputing everything from scratch. For evaluation purposes, the 4x overhead is acceptable since this is a research paper where inference speed matters less than proving the concept works. I'm going to do a major revision: keeping the core problem of geometric robustness in diffusion-based policies and the LIBERO-Plus evaluation setup, but replacing the cross-modal video CFG approach with Geometric Sensitivity Filtering that analyzes action score sensitivity to augmentations. This is better because it's backbone-agnostic and works with any diffusion policy architecture.

Now I'm checking whether any existing work applies test-time augmentation specifically to diffusion model scores rather than just predictions, to confirm this mechanism is actually novel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f864c71-8fca-4d61-b558-52b62f2ed68a",
  "isSidechain": false,
  "requestId": "req_011CauUucGMhMNVu8id5onwB",
  "type": "assistant",
  "uuid": "3d1ea105-76ab-40af-b573-fe752b038778",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DE1HqtHdzrg1xBx6VTVmUD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 4157,
      "cache_read_input_tokens": 53178,
      "output_tokens": 1846,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 906,
          "output_tokens": 1846,
          "cache_read_input_tokens": 53178,
          "cache_creation_input_tokens": 4157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4157
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

_source line 81 · 2026-05-10T20:00:42.736Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AffUvqpvxF5EzBLAk529uQ`</summary>

```json
{
  "query": "\"test-time\" score function variance augmentation diffusion model filtering denoising inference 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d1ea105-76ab-40af-b573-fe752b038778",
  "isSidechain": false,
  "requestId": "req_011CauUucGMhMNVu8id5onwB",
  "type": "assistant",
  "uuid": "921b05b9-31b7-45ce-92d2-cddfb74978ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DE1HqtHdzrg1xBx6VTVmUD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 4157,
      "cache_read_input_tokens": 53178,
      "output_tokens": 1846,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 906,
          "output_tokens": 1846,
          "cache_read_input_tokens": 53178,
          "cache_creation_input_tokens": 4157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4157
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

_source line 82 · 2026-05-10T20:00:44.519Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PV1ofha3N5yLRYdPLnUY8h`</summary>

```json
{
  "url": "https://sota.evomind-tech.com/",
  "prompt": "What are the current SOTA results on LIBERO and LIBERO-Plus? Specifically: 1) Top models on standard LIBERO (LIBERO-90, LIBERO-Long) 2) Top models on LIBERO-Plus geometric perturbation (camera, robot-init) 3) Which models use diffusion-based action generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "921b05b9-31b7-45ce-92d2-cddfb74978ab",
  "isSidechain": false,
  "requestId": "req_011CauUucGMhMNVu8id5onwB",
  "type": "assistant",
  "uuid": "e3137763-a2e9-42ff-9b31-8ccf9da3c4d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DE1HqtHdzrg1xBx6VTVmUD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 4157,
      "cache_read_input_tokens": 53178,
      "output_tokens": 1846,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 906,
          "output_tokens": 1846,
          "cache_read_input_tokens": 53178,
          "cache_creation_input_tokens": 4157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4157
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

_source line 83 · 2026-05-10T20:00:44.907Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017DzigJNrkyDxTHJTg3yTPt`</summary>

```json
{
  "query": "OA-WAM CKT-WAM Being-H LIBERO-Plus camera robot perturbation specific numbers May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3137763-a2e9-42ff-9b31-8ccf9da3c4d4",
  "isSidechain": false,
  "requestId": "req_011CauUucGMhMNVu8id5onwB",
  "type": "assistant",
  "uuid": "ac1eb9d0-111f-4b57-a632-f4b7309b3cb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DE1HqtHdzrg1xBx6VTVmUD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 4157,
      "cache_read_input_tokens": 53178,
      "output_tokens": 1846,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4157,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 906,
          "output_tokens": 1846,
          "cache_read_input_tokens": 53178,
          "cache_creation_input_tokens": 4157,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4157
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

_source line 84 · 2026-05-10T20:00:47.272Z_

<details><summary>↩ Tool result · `toolu_01PV1ofha3N5yLRYdPLnUY8h`</summary>

```text
I cannot provide the specific SOTA results you're requesting based on the content available. The webpage shows that the VLA SOTA Leaderboard exists and mentions LIBERO and LIBERO Plus as benchmarks, but it displays "0 Models" for each benchmark section.

The page states: "LIBERO is a benchmark for lifelong robot learning with 130 language-conditioned manipulation tasks" and "LIBERO Plus is an extended benchmark testing robustness across 7 perturbation dimensions," but no actual leaderboard data, top-performing models, or details about action generation methods are provided in the document.

To access the current rankings and model details you're seeking, you would need to visit the individual leaderboard pages linked on the site, such as `/benchmarks/libero/` and `/benchmarks/liberoplus/`.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3137763-a2e9-42ff-9b31-8ccf9da3c4d4",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "27ed30ce-7086-416b-9bab-90c97579f6a9",
  "toolUseResult": {
    "bytes": 26531,
    "code": 200,
    "codeText": "OK",
    "result": "I cannot provide the specific SOTA results you're requesting based on the content available. The webpage shows that the VLA SOTA Leaderboard exists and mentions LIBERO and LIBERO Plus as benchmarks, but it displays \"0 Models\" for each benchmark section.\n\nThe page states: \"LIBERO is a benchmark for lifelong robot learning with 130 language-conditioned manipulation tasks\" and \"LIBERO Plus is an extended benchmark testing robustness across 7 perturbation dimensions,\" but no actual leaderboard data, top-performing models, or details about action generation methods are provided in the document.\n\nTo access the current rankings and model details you're seeking, you would need to visit the individual leaderboard pages linked on the site, such as `/benchmarks/libero/` and `/benchmarks/liberoplus/`.",
    "durationMs": 2750,
    "url": "https://sota.evomind-tech.com/"
  },
  "sourceToolAssistantUUID": "e3137763-a2e9-42ff-9b31-8ccf9da3c4d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-10T20:00:51.069Z_

<details><summary>↩ Tool result · `toolu_01AffUvqpvxF5EzBLAk529uQ`</summary>

```text
Web search results for query: ""test-time" score function variance augmentation diffusion model filtering denoising inference 2025 2026"

Links: [{"title":"Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps","url":"https://arxiv.org/html/2501.09732v1"},{"title":"Test-Time Scaling of Diffusion Models via Noise Trajectory Search","url":"https://arxiv.org/html/2506.03164v1"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"Effective Test-Time Scaling of Discrete Diffusion through ...","url":"https://arxiv.org/pdf/2511.05562"},{"title":"Beyond denoising: rethinking inference-time scaling in diffusion models | by Ula La Paris | Data Science Collective | Medium","url":"https://medium.com/data-science-collective/beyond-denoising-rethinking-inference-time-scaling-in-diffusion-models-55603337e44a"},{"title":"Inference-Time Scaling for Diffusion Models beyond Scaling ...","url":"https://inference-scale-diffusion.github.io/"},{"title":"Published as a conference paper at ICLR 2025 TEST-TIME ALIGNMENT OF DIFFUSION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/d9042abf40782fbce28901c1c9c0e8d8-Paper-Conference.pdf"},{"title":"Test-Time Scaling of Diffusion Models via Noise Trajectory Search | OpenReview","url":"https://openreview.net/forum?id=fnkkY7UGRl"},{"title":"Effective Test-Time Scaling of Discrete Diffusion through Iterative Refinement","url":"https://arxiv.org/html/2511.05562v1"},{"title":"Advances in diffusion models for image data augmentation: a review of methods, models, evaluation metrics and future research directions | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11116-x"}]

I've performed a web search on your query about test-time scaling, score functions, variance, and diffusion model techniques. Here are the key findings from recent research in 2025-2026:

## Main Research Areas

**Test-Time Scaling of Diffusion Models:**

Recent work explores inference-time scaling behavior of diffusion models beyond increasing denoising steps, specifically considering a search problem aimed at identifying better noises for the diffusion sampling process.

**Noise Trajectory Optimization:**

Current research fixes the denoising steps and explores scaling along an orthogonal axis: compute devoted to searching for more favorable noise candidates during the sampling process, extending to the SDE formulation and considering noise candidates at every denoising step.

**Key Technical Approaches:**

Researchers address this by casting diffusion as a Markov Decision Process (MDP) with a terminal reward, and then resorting to a relaxation of MDP where denoising is viewed as a sequence of independent contextual bandits, introducing an epsilon-greedy search algorithm that globally explores at extreme timesteps and locally exploits during intermediate steps.

**Discrete Diffusion Models:**

For discrete diffusion, methods design transitions as noising-denoising processes where adding noise promotes exploration and denoising restores consistency, adopting the Multiple-Try Metropolis framework and providing theoretical guarantees that iterative refinement sampling converges to the target distribution.

**Variance and Diversity Issues:**

A key challenge is that classifiers operating point-wise lead to significant reduction in sample variance and mode collapse as compute increases.

These approaches represent significant advances in efficient inference-time scaling for generative models in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "921b05b9-31b7-45ce-92d2-cddfb74978ab",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "50aac313-44a5-4236-aaab-7e1974c1dca2",
  "toolUseResult": {
    "query": "\"test-time\" score function variance augmentation diffusion model filtering denoising inference 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018jXoUpjMLmQTVHfq88n9Ed",
        "content": [
          {
            "title": "Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps",
            "url": "https://arxiv.org/html/2501.09732v1"
          },
          {
            "title": "Test-Time Scaling of Diffusion Models via Noise Trajectory Search",
            "url": "https://arxiv.org/html/2506.03164v1"
          },
          {
            "title": "GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub",
            "url": "https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"
          },
          {
            "title": "Effective Test-Time Scaling of Discrete Diffusion through ...",
            "url": "https://arxiv.org/pdf/2511.05562"
          },
          {
            "title": "Beyond denoising: rethinking inference-time scaling in diffusion models | by Ula La Paris | Data Science Collective | Medium",
            "url": "https://medium.com/data-science-collective/beyond-denoising-rethinking-inference-time-scaling-in-diffusion-models-55603337e44a"
          },
          {
            "title": "Inference-Time Scaling for Diffusion Models beyond Scaling ...",
            "url": "https://inference-scale-diffusion.github.io/"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 TEST-TIME ALIGNMENT OF DIFFUSION",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/d9042abf40782fbce28901c1c9c0e8d8-Paper-Conference.pdf"
          },
          {
            "title": "Test-Time Scaling of Diffusion Models via Noise Trajectory Search | OpenReview",
            "url": "https://openreview.net/forum?id=fnkkY7UGRl"
          },
          {
            "title": "Effective Test-Time Scaling of Discrete Diffusion through Iterative Refinement",
            "url": "https://arxiv.org/html/2511.05562v1"
          },
          {
            "title": "Advances in diffusion models for image data augmentation: a review of methods, models, evaluation metrics and future research directions | Artificial Intelligence Review | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10462-025-11116-x"
          }
        ]
      },
      "I've performed a web search on your query about test-time scaling, score functions, variance, and diffusion model techniques. Here are the key findings from recent research in 2025-2026:\n\n## Main Research Areas\n\n**Test-Time Scaling of Diffusion Models:**\n\nRecent work explores inference-time scaling behavior of diffusion models beyond increasing denoising steps, specifically considering a search problem aimed at identifying better noises for the diffusion sampling process.\n\n**Noise Trajectory Optimization:**\n\nCurrent research fixes the denoising steps and explores scaling along an orthogonal axis: compute devoted to searching for more favorable noise candidates during the sampling process, extending to the SDE formulation and considering noise candidates at every denoising step.\n\n**Key Technical Approaches:**\n\nResearchers address this by casting diffusion as a Markov Decision Process (MDP) with a terminal reward, and then resorting to a relaxation of MDP where denoising is viewed as a sequence of independent contextual bandits, introducing an epsilon-greedy search algorithm that globally explores at extreme timesteps and locally exploits during intermediate steps.\n\n**Discrete Diffusion Models:**\n\nFor discrete diffusion, methods design transitions as noising-denoising processes where adding noise promotes exploration and denoising restores consistency, adopting the Multiple-Try Metropolis framework and providing theoretical guarantees that iterative refinement sampling converges to the target distribution.\n\n**Variance and Diversity Issues:**\n\nA key challenge is that classifiers operating point-wise lead to significant reduction in sample variance and mode collapse as compute increases.\n\nThese approaches represent significant advances in efficient inference-time scaling for generative models in 2025-2026."
    ],
    "durationSeconds": 8.328886511000048
  },
  "sourceToolAssistantUUID": "921b05b9-31b7-45ce-92d2-cddfb74978ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 86_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification o…",
  "leafUuid": "50aac313-44a5-4236-aaab-7e1974c1dca2",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 87_

```json
{
  "type": "ai-title",
  "aiTitle": "Revisit WAM geometric robustness via video-action alignment",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Tool result

_source line 88 · 2026-05-10T20:00:57.252Z_

<details><summary>↩ Tool result · `toolu_017DzigJNrkyDxTHJTg3yTPt`</summary>

```text
Web search results for query: "OA-WAM CKT-WAM Being-H LIBERO-Plus camera robot perturbation specific numbers May 2026"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"How brittle are the VLA models in robotics | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub","url":"https://github.com/yuantianyuan01/FastWAM"}]

Based on the search results, I found information about **LIBERO-Plus** and camera/robot perturbations, but I need to search more specifically for the other terms you mentioned (OA-WAM, CKT-WAM, Being-H) to get complete information.

Links: [{"title":"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation","url":"https://arxiv.org/html/2605.06481v1"},{"title":"CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models","url":"https://arxiv.org/html/2605.06247v1"},{"title":"CES 2026 Robotics Announcements Recap","url":"https://counterpointresearch.com/en/insights/ces-2026-robotics-announcements-recap"},{"title":"Which Humanoid Robots Launch in 2026? - Qviro Blog","url":"https://qviro.com/blog/humanoid-robots-launch-2026/"},{"title":"9 humanoid robots at CES 2026 that showed the future is already here","url":"https://interestingengineering.com/ai-robotics/9-humanoid-robots-at-ces-2026"},{"title":"Top 10 robotics developments of March 2026 - The Robot Report","url":"https://www.therobotreport.com/top-10-robotics-developments-march-2026/"},{"title":"Humanoid robots in 2026: Types, prices, and what’s next - Standard Bots","url":"https://standardbots.com/blog/humanoid-robot"},{"title":"2026 Robotics Advancements: The Complete Industry Guide | RoboCloud Hub","url":"https://robocloud-dashboard.vercel.app/learn/blog/robotics-advancements-2026"},{"title":"Top 10 Physical AI Models Powering Real-World Robots in 2026 - MarkTechPost","url":"https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/"},{"title":"Top 12 Humanoid Robots of 2026 - Humanoid Robotics Technology","url":"https://humanoidroboticstechnology.com/articles/top-12-humanoid-robots-of-2026/"}]

Now let me search more specifically for "Being-H" robot model:

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium","url":"https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"LIBERO Tasks: Lifelong Robotic Learning","url":"https://www.emergentmind.com/topics/libero-tasks"}]

Based on my search results, I have found detailed information about several of the models and benchmarks you mentioned. Here's what I found:

## Summary of Search Results

### **OA-WAM (Object-Addressable World Action Model)**

OA-WAM is an Object-Addressable World Action Model for robust robot manipulation. OA-WAM matches the SOTA VLA and WAM baselines on LIBERO (79.3%) and on LIBERO-Plus, OA-WAM sets a new SOTA on the geometric axes most aligned with the hypothesis. On the LIBERO-Plus robustness benchmark, it sets a new SOTA on the geometric axes—camera at 85.7%.

### **CKT-WAM (Context Knowledge Transfer)**

CKT-WAM consistently improves zero-shot generalization and achieves the best overall performance on LIBERO-Plus, reaching 86.1% total success rate with only 1.17% trainable parameters. Beyond simulation, CKT-WAM also demonstrates strong real-world long-horizon manipulation ability, achieving the best average success rate of 83.3% across four multi-step tasks.

### **LIBERO-Plus Camera and Robot Perturbation**

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

### **Regarding "Being-H"**

I was unable to find specific information about a robot model called "Being-H" in the search results. The searches returned information about various humanoid robots like Boston Dynamics' Atlas, Unitree robots, and others, but no model specifically identified as "Being-H."

If you're looking for more specific information about Being-H or other particular numerical results from May 2026, could you provide additional context or clarification about these terms?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac1eb9d0-111f-4b57-a632-f4b7309b3cb5",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "9387a1fa-48f4-419d-90b2-85593e033a9a",
  "toolUseResult": {
    "query": "OA-WAM CKT-WAM Being-H LIBERO-Plus camera robot perturbation specific numbers May 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Di8T61mvcYm7JQcgwtx6g9",
        "content": [
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "How brittle are the VLA models in robotics | by Yanan Chen | Medium",
            "url": "https://medium.com/@yananchen1116/how-brittle-are-the-vla-models-in-robotics-66ab85286ecf"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR",
            "url": "https://tldr.takara.ai/p/2510.13626"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626v1"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub",
            "url": "https://github.com/yuantianyuan01/FastWAM"
          }
        ]
      },
      "Based on the search results, I found information about **LIBERO-Plus** and camera/robot perturbations, but I need to search more specifically for the other terms you mentioned (OA-WAM, CKT-WAM, Being-H) to get complete information.",
      {
        "tool_use_id": "srvtoolu_01MVcYQMx2o4w7DURNvmU5ZR",
        "content": [
          {
            "title": "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation",
            "url": "https://arxiv.org/html/2605.06481v1"
          },
          {
            "title": "CKT-WAM: Parameter-Efficient Context Knowledge Transfer Between World Action Models",
            "url": "https://arxiv.org/html/2605.06247v1"
          },
          {
            "title": "CES 2026 Robotics Announcements Recap",
            "url": "https://counterpointresearch.com/en/insights/ces-2026-robotics-announcements-recap"
          },
          {
            "title": "Which Humanoid Robots Launch in 2026? - Qviro Blog",
            "url": "https://qviro.com/blog/humanoid-robots-launch-2026/"
          },
          {
            "title": "9 humanoid robots at CES 2026 that showed the future is already here",
            "url": "https://interestingengineering.com/ai-robotics/9-humanoid-robots-at-ces-2026"
          },
          {
            "title": "Top 10 robotics developments of March 2026 - The Robot Report",
            "url": "https://www.therobotreport.com/top-10-robotics-developments-march-2026/"
          },
          {
            "title": "Humanoid robots in 2026: Types, prices, and what’s next - Standard Bots",
            "url": "https://standardbots.com/blog/humanoid-robot"
          },
          {
            "title": "2026 Robotics Advancements: The Complete Industry Guide | RoboCloud Hub",
            "url": "https://robocloud-dashboard.vercel.app/learn/blog/robotics-advancements-2026"
          },
          {
            "title": "Top 10 Physical AI Models Powering Real-World Robots in 2026 - MarkTechPost",
            "url": "https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/"
          },
          {
            "title": "Top 12 Humanoid Robots of 2026 - Humanoid Robotics Technology",
            "url": "https://humanoidroboticstechnology.com/articles/top-12-humanoid-robots-of-2026/"
          }
        ]
      },
      "Now let me search more specifically for \"Being-H\" robot model:",
      {
        "tool_use_id": "srvtoolu_018uPu6N7yvGnLQVVtySqwE7",
        "content": [
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub",
            "url": "https://github.com/Lifelong-Robot-Learning/LIBERO"
          },
          {
            "title": "GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark",
            "url": "https://github.com/Zxy-MLlab/LIBERO-PRO"
          },
          {
            "title": "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
            "url": "https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/liu_zhu_NeurIPS2023.pdf"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "LIBERO: simulation benchmark for the study of lifelong robot learning | by Deepthi Karkada | Medium",
            "url": "https://medium.com/@deepkarkada/libero-simulation-benchmark-for-the-study-of-lifelong-robot-learning-583b786a96f6"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
            "url": "https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"
          },
          {
            "title": "LIBERO Tasks: Lifelong Robotic Learning",
            "url": "https://www.emergentmind.com/topics/libero-tasks"
          }
        ]
      },
      "Based on my search results, I have found detailed information about several of the models and benchmarks you mentioned. Here's what I found:\n\n## Summary of Search Results\n\n### **OA-WAM (Object-Addressable World Action Model)**\n\nOA-WAM is an Object-Addressable World Action Model for robust robot manipulation. OA-WAM matches the SOTA VLA and WAM baselines on LIBERO (79.3%) and on LIBERO-Plus, OA-WAM sets a new SOTA on the geometric axes most aligned with the hypothesis. On the LIBERO-Plus robustness benchmark, it sets a new SOTA on the geometric axes—camera at 85.7%.\n\n### **CKT-WAM (Context Knowledge Transfer)**\n\nCKT-WAM consistently improves zero-shot generalization and achieves the best overall performance on LIBERO-Plus, reaching 86.1% total success rate with only 1.17% trainable parameters. Beyond simulation, CKT-WAM also demonstrates strong real-world long-horizon manipulation ability, achieving the best average success rate of 83.3% across four multi-step tasks.\n\n### **LIBERO-Plus Camera and Robot Perturbation**\n\nModels exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.\n\n### **Regarding \"Being-H\"**\n\nI was unable to find specific information about a robot model called \"Being-H\" in the search results. The searches returned information about various humanoid robots like Boston Dynamics' Atlas, Unitree robots, and others, but no model specifically identified as \"Being-H.\"\n\nIf you're looking for more specific information about Being-H or other particular numerical results from May 2026, could you provide additional context or clarification about these terms?"
    ],
    "durationSeconds": 12.342769189000013
  },
  "sourceToolAssistantUUID": "ac1eb9d0-111f-4b57-a632-f4b7309b3cb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 89 · 2026-05-10T20:01:25.274Z_

<details><summary>Logged reasoning block</summary>

```text
Interesting - the search results give me some updated numbers:
- OA-WAM: LIBERO 79.3%, LIBERO-Plus Camera 85.7% (updated from 80.5% in the original idea)
- CKT-WAM: LIBERO-Plus total 86.1%

Wait, OA-WAM's standard LIBERO is only 79.3%? That's the same as UWM! Interesting. Let me re-read...

Actually it says "OA-WAM matches the SOTA VLA and WAM baselines on LIBERO (79.3%)". 

That seems surprisingly low for state-of-the-art unless they're testing on a different LIBERO variant - maybe LIBERO-Long or LIBERO-90 rather than the standard benchmark. Different papers use different subsets, so I shouldn't get too hung up on the exact numbers. The real takeaway is that under geometric perturbation, all these models show dramatic performance drops across the board.

Looking at the current best results on LIBERO-Plus with geometric robustness, OA-WAM and CKT-WAM are hitting around 85-86%, but every single approach requires either architectural changes or retraining - there's no training-free solution yet. I'm also noticing some related work on inference-time scaling for diffusion models that searches for better noise trajectories, but that's different from what I'm proposing. My approach focuses on filtering the score function based on geometric sensitivity rather than searching for optimal initial noise. There's also the recent test-time alignment work from ICLR 2025 that could be relevant. I think I have enough pieces now to put together the revised idea.

The real opportunity here is that all the equivariant methods require training-time modifications, and there's nothing addressing geometric robustness at test time for diffusion policies on LIBERO-Plus. Inference-time scaling is getting attention but it's all about noise search, not robustness. My approach - filtering based on geometric sensitivity at inference time without any training - fills that gap perfectly. I'm calling it Geometric Sensitivity Filtering, and it's specifically designed as a training-free, test-time method for making pre-trained diffusion policies geometrically robust.

The mechanism is straightforward: during denoising, I compute action scores from multiple small geometric variations of the observation, use SVD on the score covariance to identify which directions are sensitive to geometry, then project the original score away from those sensitive directions. This works with any diffusion-based policy - Fast-WAM, DP, VLAs with diffusion heads - and I have a strong baseline to compare against. The positioning is clear too: this is the training-free alternative to SE(3)-equivariant architectures, and I can reference the recent equivariant diffusion work and score composition methods to show where this fits in the landscape.

Now I'm identifying the related work to position this properly - there's the training-time equivariant scoring approaches, inference-time scaling paradigms for diffusion, and test-time adaptation methods like ADPro that work with point clouds but have different requirements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9387a1fa-48f4-419d-90b2-85593e033a9a",
  "isSidechain": false,
  "requestId": "req_011CauUyvhEgpseaP2Jn6xnd",
  "type": "assistant",
  "uuid": "be19c18a-4856-4706-9ad1-06a7b05ca8af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFxjqdF2bFXSsAfkyAfxGi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6081,
      "cache_read_input_tokens": 57335,
      "output_tokens": 1280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6081,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1280,
          "cache_read_input_tokens": 57335,
          "cache_creation_input_tokens": 6081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6081
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

_source line 90 · 2026-05-10T20:01:25.275Z_

Now I have a comprehensive picture of the landscape. Let me do one final search to confirm that no one has proposed test-time geometric sensitivity analysis for diffusion policy scores.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be19c18a-4856-4706-9ad1-06a7b05ca8af",
  "isSidechain": false,
  "requestId": "req_011CauUyvhEgpseaP2Jn6xnd",
  "type": "assistant",
  "uuid": "75aa74f7-a8e6-4f87-bbba-a92f39b6c830",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFxjqdF2bFXSsAfkyAfxGi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6081,
      "cache_read_input_tokens": 57335,
      "output_tokens": 1280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6081,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1280,
          "cache_read_input_tokens": 57335,
          "cache_creation_input_tokens": 6081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6081
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

_source line 91 · 2026-05-10T20:01:25.741Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019jNVPi2mhp66KefjV7eEmF`</summary>

```json
{
  "query": "inference-time geometric robustness pre-trained diffusion policy without retraining architecture-agnostic 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75aa74f7-a8e6-4f87-bbba-a92f39b6c830",
  "isSidechain": false,
  "requestId": "req_011CauUyvhEgpseaP2Jn6xnd",
  "type": "assistant",
  "uuid": "3ac8964c-fce9-4130-9f46-b8287b35cc46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFxjqdF2bFXSsAfkyAfxGi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6081,
      "cache_read_input_tokens": 57335,
      "output_tokens": 1280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6081,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1280,
          "cache_read_input_tokens": 57335,
          "cache_creation_input_tokens": 6081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6081
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

_source line 92 · 2026-05-10T20:01:28.581Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Nj6Xv6aCfTQfQRpCAoo8Tq`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.06481v1",
  "prompt": "Extract: 1) OA-WAM's exact LIBERO standard performance and LIBERO-Plus camera/robot results. 2) What baseline WAM does OA-WAM build on? 3) What specific architectural modifications are required? 4) Is OA-WAM's action generation diffusion-based? 5) Could a test-time filtering method be applied on top of OA-WAM?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ac8964c-fce9-4130-9f46-b8287b35cc46",
  "isSidechain": false,
  "requestId": "req_011CauUyvhEgpseaP2Jn6xnd",
  "type": "assistant",
  "uuid": "91723e87-2f2c-4a5b-9a77-a412e134d530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UFxjqdF2bFXSsAfkyAfxGi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6081,
      "cache_read_input_tokens": 57335,
      "output_tokens": 1280,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6081,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1280,
          "cache_read_input_tokens": 57335,
          "cache_creation_input_tokens": 6081,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6081
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

_source line 93 · 2026-05-10T20:01:31.490Z_

<details><summary>↩ Tool result · `toolu_019jNVPi2mhp66KefjV7eEmF`</summary>

```text
Web search results for query: "inference-time geometric robustness pre-trained diffusion policy without retraining architecture-agnostic 2026"

Links: [{"title":"Inference-Time Scaling for Diffusion Models beyond Scaling ...","url":"https://inference-scale-diffusion.github.io/"},{"title":"Beyond denoising: rethinking inference-time scaling in diffusion models | by Ula La Paris | Data Science Collective | Medium","url":"https://medium.com/data-science-collective/beyond-denoising-rethinking-inference-time-scaling-in-diffusion-models-55603337e44a"},{"title":"A General Framework for Inference-time Scaling and Steering of Diffusion Models | OpenReview","url":"https://openreview.net/forum?id=Jp988ELppQ&noteId=FSERsnO0Ez"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps","url":"https://arxiv.org/html/2501.09732v1"},{"title":"GitHub - bansky-cl/diffusion-nlp-paper-arxiv: Auto get diffusion nlp papers in Axriv. More papers Information can be found in another repository \"Diffusion-LM-Papers\". · GitHub","url":"https://github.com/bansky-cl/diffusion-nlp-paper-arxiv"},{"title":"[2501.06848] A General Framework for Inference-time Scaling and Steering of Diffusion Models","url":"https://arxiv.org/abs/2501.06848"},{"title":"DiffusionNet: Discretization Agnostic Learning on Surfaces | ACM Transactions on Graphics","url":"https://dl.acm.org/doi/full/10.1145/3507905"},{"title":"[2501.09732] Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps","url":"https://arxiv.org/abs/2501.09732"},{"title":"Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior (arXiv:2312.06655v1) - ScienceStack","url":"https://www.sciencestack.ai/paper/2312.06655"}]

Based on the search results, the query appears to match research on inference-time scaling for diffusion models. The most relevant findings are:

Recent work explores inference-time scaling behavior of diffusion models beyond increasing denoising steps by investigating how generation performance can improve with increased computation, specifically considering a search problem aimed at identifying better noises for the diffusion sampling process.

A framework called FK steering has been proposed for inference-time steering of diffusion models with reward functions, which applies Feynman-Kac interacting particle systems to this task. This method doesn't require any additional training and works by generating multiple candidates in parallel and favoring the ones more likely to meet the desired goal.

The research also addresses robustness without retraining. This shift from passive denoising to active search echoes trends in LLMs, where inference-time optimizations have led to significant performance boosts without retraining.

However, the search results did not return a specific paper that exactly matches all the terms in your query (particularly "geometric robustness" and "pre-trained diffusion policy"). The results focus more on general inference-time scaling and steering of diffusion models rather than a specific work on robustness for pre-trained diffusion policies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ac8964c-fce9-4130-9f46-b8287b35cc46",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "de410821-213a-4ab8-990c-f93f658c795d",
  "toolUseResult": {
    "query": "inference-time geometric robustness pre-trained diffusion policy without retraining architecture-agnostic 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VtiuQJpamCVywDtMKu5Ddi",
        "content": [
          {
            "title": "Inference-Time Scaling for Diffusion Models beyond Scaling ...",
            "url": "https://inference-scale-diffusion.github.io/"
          },
          {
            "title": "Beyond denoising: rethinking inference-time scaling in diffusion models | by Ula La Paris | Data Science Collective | Medium",
            "url": "https://medium.com/data-science-collective/beyond-denoising-rethinking-inference-time-scaling-in-diffusion-models-55603337e44a"
          },
          {
            "title": "A General Framework for Inference-time Scaling and Steering of Diffusion Models | OpenReview",
            "url": "https://openreview.net/forum?id=Jp988ELppQ&noteId=FSERsnO0Ez"
          },
          {
            "title": "GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub",
            "url": "https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"
          },
          {
            "title": "Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps",
            "url": "https://arxiv.org/html/2501.09732v1"
          },
          {
            "title": "GitHub - bansky-cl/diffusion-nlp-paper-arxiv: Auto get diffusion nlp papers in Axriv. More papers Information can be found in another repository \"Diffusion-LM-Papers\". · GitHub",
            "url": "https://github.com/bansky-cl/diffusion-nlp-paper-arxiv"
          },
          {
            "title": "[2501.06848] A General Framework for Inference-time Scaling and Steering of Diffusion Models",
            "url": "https://arxiv.org/abs/2501.06848"
          },
          {
            "title": "DiffusionNet: Discretization Agnostic Learning on Surfaces | ACM Transactions on Graphics",
            "url": "https://dl.acm.org/doi/full/10.1145/3507905"
          },
          {
            "title": "[2501.09732] Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps",
            "url": "https://arxiv.org/abs/2501.09732"
          },
          {
            "title": "Sherpa3D: Boosting High-Fidelity Text-to-3D Generation via Coarse 3D Prior (arXiv:2312.06655v1) - ScienceStack",
            "url": "https://www.sciencestack.ai/paper/2312.06655"
          }
        ]
      },
      "Based on the search results, the query appears to match research on inference-time scaling for diffusion models. The most relevant findings are:\n\nRecent work explores inference-time scaling behavior of diffusion models beyond increasing denoising steps by investigating how generation performance can improve with increased computation, specifically considering a search problem aimed at identifying better noises for the diffusion sampling process.\n\nA framework called FK steering has been proposed for inference-time steering of diffusion models with reward functions, which applies Feynman-Kac interacting particle systems to this task. This method doesn't require any additional training and works by generating multiple candidates in parallel and favoring the ones more likely to meet the desired goal.\n\nThe research also addresses robustness without retraining. This shift from passive denoising to active search echoes trends in LLMs, where inference-time optimizations have led to significant performance boosts without retraining.\n\nHowever, the search results did not return a specific paper that exactly matches all the terms in your query (particularly \"geometric robustness\" and \"pre-trained diffusion policy\"). The results focus more on general inference-time scaling and steering of diffusion models rather than a specific work on robustness for pre-trained diffusion policies."
    ],
    "durationSeconds": 5.743830906999996
  },
  "sourceToolAssistantUUID": "3ac8964c-fce9-4130-9f46-b8287b35cc46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 94_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification o…",
  "leafUuid": "de410821-213a-4ab8-990c-f93f658c795d",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 95_

```json
{
  "type": "ai-title",
  "aiTitle": "Revisit WAM geometric robustness via video-action alignment",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Tool result

_source line 96 · 2026-05-10T20:01:36.430Z_

<details><summary>↩ Tool result · `toolu_01Nj6Xv6aCfTQfQRpCAoo8Tq`</summary>

```text
# OA-WAM: Key Technical Details

## 1. Performance Metrics

**LIBERO Standard:** OA-WAM achieves "97.8%" average success across all four task suites (Spatial/Object/Goal/Long).

**LIBERO-Plus Results:**
- Camera axis: 80.5% (compared to π₀.₅'s 75.4%)
- Robot initial state: 89.6% (versus π₀.₅'s 77.5%)

## 2. Baseline Foundation

OA-WAM does not build directly on an existing WAM. Instead, it constructs its approach from first principles using a "7B Chameleon-style trunk" as the core transformer backbone, combined with novel object-slot tokenization and per-layer attention constraints.

## 3. Architectural Modifications

The key modifications are:

- **Per-slot decomposition:** Each frame splits into N+1 slots with frozen identity addresses and time-varying content vectors
- **Address-only key projection:** "the cross-slot key projection reads only addr_k (first 32 dims)"
- **Per-layer reset hook:** After each transformer block, "a forward hook overwrites x_k^(ℓ+1)[1:32] ← addr_k at slot positions"

These two components together enforce that "slot-routing keys at every transformer layer are architecturally constrained to depend only on the frozen identity address."

## 4. Action Generation Mechanism

Yes, OA-WAM uses flow-matching for action decoding. The "action head h_ξ...is a flow-matching MLP" that "decodes a 16-step continuous action chunk." At inference, "the chunk is decoded by 4-step forward Euler integration in a single forward pass."

## 5. Test-Time Filtering Compatibility

The paper does not discuss or address whether filtering methods could augment OA-WAM. The architecture is presented as complete; no evaluation of post-hoc filtering strategies appears in the work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91723e87-2f2c-4a5b-9a77-a412e134d530",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "f25aa6c8-30d1-4d14-9b55-382bc905ab39",
  "toolUseResult": {
    "bytes": 793456,
    "code": 200,
    "codeText": "OK",
    "result": "# OA-WAM: Key Technical Details\n\n## 1. Performance Metrics\n\n**LIBERO Standard:** OA-WAM achieves \"97.8%\" average success across all four task suites (Spatial/Object/Goal/Long).\n\n**LIBERO-Plus Results:**\n- Camera axis: 80.5% (compared to π₀.₅'s 75.4%)\n- Robot initial state: 89.6% (versus π₀.₅'s 77.5%)\n\n## 2. Baseline Foundation\n\nOA-WAM does not build directly on an existing WAM. Instead, it constructs its approach from first principles using a \"7B Chameleon-style trunk\" as the core transformer backbone, combined with novel object-slot tokenization and per-layer attention constraints.\n\n## 3. Architectural Modifications\n\nThe key modifications are:\n\n- **Per-slot decomposition:** Each frame splits into N+1 slots with frozen identity addresses and time-varying content vectors\n- **Address-only key projection:** \"the cross-slot key projection reads only addr_k (first 32 dims)\"\n- **Per-layer reset hook:** After each transformer block, \"a forward hook overwrites x_k^(ℓ+1)[1:32] ← addr_k at slot positions\"\n\nThese two components together enforce that \"slot-routing keys at every transformer layer are architecturally constrained to depend only on the frozen identity address.\"\n\n## 4. Action Generation Mechanism\n\nYes, OA-WAM uses flow-matching for action decoding. The \"action head h_ξ...is a flow-matching MLP\" that \"decodes a 16-step continuous action chunk.\" At inference, \"the chunk is decoded by 4-step forward Euler integration in a single forward pass.\"\n\n## 5. Test-Time Filtering Compatibility\n\nThe paper does not discuss or address whether filtering methods could augment OA-WAM. The architecture is presented as complete; no evaluation of post-hoc filtering strategies appears in the work.",
    "durationMs": 7846,
    "url": "https://arxiv.org/html/2605.06481v1"
  },
  "sourceToolAssistantUUID": "91723e87-2f2c-4a5b-9a77-a412e134d530",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 97 · 2026-05-10T20:01:36.434Z_

```json
{
  "parentUuid": "f25aa6c8-30d1-4d14-9b55-382bc905ab39",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2a4c9915-b4e4-4cb4-bcfd-495b09271c9a",
  "timestamp": "2026-05-10T20:01:36.434Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 98 · 2026-05-10T20:02:08.102Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have crucial updated information:

**OA-WAM:** 
- Standard LIBERO: 97.8% (NOT 79.3% as the earlier search suggested - that was probably a different evaluation)
- LIBERO-Plus Camera: 80.5%
- LIBERO-Plus Robot: 89.6%
- Uses flow-matching MLP for actions (4-step forward Euler)
- 7B Chameleon-style trunk
- Requires architectural modifications (per-slot decomposition, address-only key projection, per-layer reset hooks)

This is very helpful. Now I know:


Flow-matching with just 4 integration steps actually strengthens my GSF approach—since the velocity field is fundamentally similar to score-based models, I can apply the same augmentation strategy there, and the lightweight inference cost means the K augmentations per step remain computationally feasible.

Now I need to check if OA-WAM has a released checkpoint, because if it does, I could layer GSF on top of their architecture and demonstrate additional improvements beyond what they achieved. The competitive positioning is clear: OA-WAM requires a 7B model with architectural changes, CKT-WAM needs retraining, but GSF is training-free and can enhance any existing policy. For the baseline, I'm leaning toward Fast-WAM since it has an official GitHub release and solid diffusion-based action generation, though I should verify OA-WAM's checkpoint availability too given its stronger camera-view performance.

But I'm hitting a critical issue—I need to confirm whether Fast-WAM actually uses iterative diffusion denoising or if it generates actions in a single forward pass. The description mentions "directly generating actions without explicit future video denoising," which suggests it might not have the iterative refinement process that GSF would need to improve upon.

Looking more carefully at the details though, Fast-WAM still uses a CFG scale parameter, which strongly indicates it's using a diffusion or flow-matching process for the action generation itself, even if it skips the video denoising step. So GSF should be applicable.

Now I'm thinking about which evaluation metric to prioritize—OA-WAM achieves 80.5% on camera perturbation while CKT-WAM hits 86.1% overall, but the latter requires retraining. If I can demonstrate that GSF improves Fast-WAM's performance on camera perturbations specifically, that would be a compelling result.

Even better would be showing that GSF works as a complementary technique on top of OA-WAM itself, pushing camera performance from 80.5% toward 85% or higher—that would prove the method's value even for architectures already designed for robustness.

So I'm settling on the final approach: same problem and evaluation setup, same venue target, but with a completely redesigned method that shifts from spectral CFG filtering to geometric sensitivity filtering of action scores. This resolves the backbone compatibility issue, works with any diffusion or flow policy, and has clear theoretical grounding. Time to write this up.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a4c9915-b4e4-4cb4-bcfd-495b09271c9a",
  "isSidechain": false,
  "requestId": "req_011CauV2pDtXGBvBy2sYnKfH",
  "type": "assistant",
  "uuid": "6e2a9cb9-d974-494e-bbb3-69f9c68a260c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDhT5WZbewitqjA5Wdq3bo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2803,
      "cache_read_input_tokens": 63416,
      "output_tokens": 1503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1503,
          "cache_read_input_tokens": 63416,
          "cache_creation_input_tokens": 2803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2803
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

_source line 99 · 2026-05-10T20:02:11.897Z_

Now I have a comprehensive understanding. The key findings confirm my analysis:

1. **No training-free method exists for LIBERO-Plus geometric robustness** - clear gap
2. **ALL equivariant approaches (SDP/ICML 2025, EquiBot) are training-time** - my proposed test-time method fills the gap
3. **OA-WAM uses flow-matching (4-step Euler)** - GSF can work on velocity fields too
4. **OA-WAM standard LIBERO: 97.8%, Camera: 80.5%** - updated numbers
5. **Fast-WAM has released code/checkpoints** - viable backbone

I'm now going to produce a **major revision** that fundamentally redesigns the method while keeping the same core problem. The key insight: instead of filtering video→action CFG (which has backbone dependency), I'll propose filtering the action score directly based on geometric sensitivity analysis via augmentations - making it truly architecture-agnostic.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e2a9cb9-d974-494e-bbb3-69f9c68a260c",
  "isSidechain": false,
  "requestId": "req_011CauV2pDtXGBvBy2sYnKfH",
  "type": "assistant",
  "uuid": "b85a7feb-837c-43e0-819b-07844d51e8c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDhT5WZbewitqjA5Wdq3bo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2803,
      "cache_read_input_tokens": 63416,
      "output_tokens": 1503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1503,
          "cache_read_input_tokens": 63416,
          "cache_creation_input_tokens": 2803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2803
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

_source line 100 · 2026-05-10T20:02:12.760Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ce2PKKNnYZVE69uhBPG5Xa`</summary>

```json
{
  "query": "Fast-WAM github checkpoint LIBERO action diffusion denoising steps inference architecture"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b85a7feb-837c-43e0-819b-07844d51e8c2",
  "isSidechain": false,
  "requestId": "req_011CauV2pDtXGBvBy2sYnKfH",
  "type": "assistant",
  "uuid": "1c00a256-99b0-47e7-ae97-ee913b10f3d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDhT5WZbewitqjA5Wdq3bo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2803,
      "cache_read_input_tokens": 63416,
      "output_tokens": 1503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1503,
          "cache_read_input_tokens": 63416,
          "cache_creation_input_tokens": 2803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2803
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

_source line 101 · 2026-05-10T20:02:13.276Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EUdpwZipbJkemLnCngZ6eN`</summary>

```json
{
  "query": "\"inference time scaling\" \"diffusion policy\" robot action verifier reward function 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c00a256-99b0-47e7-ae97-ee913b10f3d6",
  "isSidechain": false,
  "requestId": "req_011CauV2pDtXGBvBy2sYnKfH",
  "type": "assistant",
  "uuid": "e112dbb3-e79e-4d47-ae38-9897fcffeb39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDhT5WZbewitqjA5Wdq3bo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2803,
      "cache_read_input_tokens": 63416,
      "output_tokens": 1503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1503,
          "cache_read_input_tokens": 63416,
          "cache_creation_input_tokens": 2803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2803
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

_source line 102 · 2026-05-10T20:02:21.799Z_

<details><summary>↩ Tool result · `toolu_01Ce2PKKNnYZVE69uhBPG5Xa`</summary>

```text
Web search results for query: "Fast-WAM github checkpoint LIBERO action diffusion denoising steps inference architecture"

Links: [{"title":"GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub","url":"https://github.com/yuantianyuan01/FastWAM"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://yuantianyuan01.github.io/FastWAM/"},{"title":"Fast-WAM: Do World Action Models Need Test-time Future Imagination?","url":"https://arxiv.org/html/2603.16666"},{"title":"WAM-Diff: A Masked Diffusion VLA Framework with MoE and Online Reinforcement Learning for Autonomous Driving","url":"https://arxiv.org/html/2512.11872v1"},{"title":"X-WAM: Unified 4D World Action Modeling from Video ...","url":"https://sharinka0715.github.io/X-WAM/"},{"title":"Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation","url":"https://consistency-policy.github.io/"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/html/2508.20072v1"},{"title":"Diving into Diffusion Policy with LeRobot","url":"https://radekosmulski.com/diving-into-diffusion-policy-with-lerobot/"},{"title":"GitHub - lucidrains/denoising-diffusion-pytorch: Implementation of Denoising Diffusion Probabilistic Model in Pytorch · GitHub","url":"https://github.com/lucidrains/denoising-diffusion-pytorch"},{"title":"GitHub - real-stanford/diffusion_policy: [RSS 2023] Diffusion Policy Visuomotor Policy Learning via Action Diffusion · GitHub","url":"https://github.com/real-stanford/diffusion_policy"}]

I found relevant information about Fast-WAM! Here's a summary based on the search results:

## Fast-WAM: Key Information

**Project Overview:**
Fast-WAM is an official codebase for "Do World Action Models Need Test-time Future Imagination?" and contains training and evaluation code for FastWAM on LIBERO / RoboTwin.

**Architecture:**
Fast-WAM repurposes a pretrained video Diffusion Transformer (DiT) as a single-pass world encoder for action generation. It builds Fast-WAM with a Mixture-of-Transformer (MoT) architecture with shared attention, consisting of a video DiT and an action expert DiT. Fast-WAM is built on top of the video Diffusion Transformer (DiT) from Wan2.2-5B, which serves as the world modeling backbone.

**Key Innovation - Inference Approach:**
At inference time, Fast-WAM keeps only the clean latent tokens of the current observation, processes them with the video backbone once, and directly generates actions without explicit future video denoising. During inference, Fast-WAM does not explicitly generate future observations. Instead, it keeps only the clean latent tokens of the first observation frame, processes them with the video model in a single forward pass, and uses the resulting latent world representation for direct action generation.

**Performance:**
Fast-WAM achieves competitive results on LIBERO, RoboTwin, and real-world towel folding without embodied pretraining and runs in real time with 190 ms latency, more than 4x faster than existing imagine-then-execute WAM designs.

**GitHub Repository:**
The official repository is available at https://github.com/yuantianyuan01/FastWAM with model checkpoints available through Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c00a256-99b0-47e7-ae97-ee913b10f3d6",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "c7e67cfb-ab69-4180-ace4-1321acebf5f2",
  "toolUseResult": {
    "query": "Fast-WAM github checkpoint LIBERO action diffusion denoising steps inference architecture",
    "results": [
      {
        "tool_use_id": "srvtoolu_0127LvXx6bAyHwNdEamiByoy",
        "content": [
          {
            "title": "GitHub - yuantianyuan01/FastWAM: Official codebase for Fast-WAM: Do World Action Models Need Test-time Future Imagination? · GitHub",
            "url": "https://github.com/yuantianyuan01/FastWAM"
          },
          {
            "title": "Fast-WAM: Do World Action Models Need Test-time Future Imagination?",
            "url": "https://yuantianyuan01.github.io/FastWAM/"
          },
          {
            "title": "Fast-WAM: Do World Action Models Need Test-time Future Imagination?",
            "url": "https://arxiv.org/html/2603.16666"
          },
          {
            "title": "WAM-Diff: A Masked Diffusion VLA Framework with MoE and Online Reinforcement Learning for Autonomous Driving",
            "url": "https://arxiv.org/html/2512.11872v1"
          },
          {
            "title": "X-WAM: Unified 4D World Action Modeling from Video ...",
            "url": "https://sharinka0715.github.io/X-WAM/"
          },
          {
            "title": "Consistency Policy: Accelerated Visuomotor Policies via Consistency Distillation",
            "url": "https://consistency-policy.github.io/"
          },
          {
            "title": "Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies",
            "url": "https://arxiv.org/html/2508.20072v1"
          },
          {
            "title": "Diving into Diffusion Policy with LeRobot",
            "url": "https://radekosmulski.com/diving-into-diffusion-policy-with-lerobot/"
          },
          {
            "title": "GitHub - lucidrains/denoising-diffusion-pytorch: Implementation of Denoising Diffusion Probabilistic Model in Pytorch · GitHub",
            "url": "https://github.com/lucidrains/denoising-diffusion-pytorch"
          },
          {
            "title": "GitHub - real-stanford/diffusion_policy: [RSS 2023] Diffusion Policy Visuomotor Policy Learning via Action Diffusion · GitHub",
            "url": "https://github.com/real-stanford/diffusion_policy"
          }
        ]
      },
      "I found relevant information about Fast-WAM! Here's a summary based on the search results:\n\n## Fast-WAM: Key Information\n\n**Project Overview:**\nFast-WAM is an official codebase for \"Do World Action Models Need Test-time Future Imagination?\" and contains training and evaluation code for FastWAM on LIBERO / RoboTwin.\n\n**Architecture:**\nFast-WAM repurposes a pretrained video Diffusion Transformer (DiT) as a single-pass world encoder for action generation. It builds Fast-WAM with a Mixture-of-Transformer (MoT) architecture with shared attention, consisting of a video DiT and an action expert DiT. Fast-WAM is built on top of the video Diffusion Transformer (DiT) from Wan2.2-5B, which serves as the world modeling backbone.\n\n**Key Innovation - Inference Approach:**\nAt inference time, Fast-WAM keeps only the clean latent tokens of the current observation, processes them with the video backbone once, and directly generates actions without explicit future video denoising. During inference, Fast-WAM does not explicitly generate future observations. Instead, it keeps only the clean latent tokens of the first observation frame, processes them with the video model in a single forward pass, and uses the resulting latent world representation for direct action generation.\n\n**Performance:**\nFast-WAM achieves competitive results on LIBERO, RoboTwin, and real-world towel folding without embodied pretraining and runs in real time with 190 ms latency, more than 4x faster than existing imagine-then-execute WAM designs.\n\n**GitHub Repository:**\nThe official repository is available at https://github.com/yuantianyuan01/FastWAM with model checkpoints available through Hugging Face."
    ],
    "durationSeconds": 9.029990625000035
  },
  "sourceToolAssistantUUID": "1c00a256-99b0-47e7-ae97-ee913b10f3d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-10T20:02:23.665Z_

<details><summary>↩ Tool result · `toolu_01EUdpwZipbJkemLnCngZ6eN`</summary>

```text
Web search results for query: ""inference time scaling" "diffusion policy" robot action verifier reward function 2025 2026"

Links: [{"title":"[2504.02495] Inference-Time Scaling for Generalist Reward Modeling","url":"https://arxiv.org/abs/2504.02495"},{"title":"Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition","url":"https://arxiv.org/html/2510.01068"},{"title":"Diffusion Policy for Robot Learning: What It Is and How to Use It | SVRC","url":"https://www.roboticscenter.ai/blog/diffusion-policy-robots"},{"title":"A General Framework for Inference-time Scaling and Steering of Diffusion Models","url":"https://arxiv.org/html/2501.06848v3"},{"title":"Lookahead Sample Reward Guidance for Test-Time Scaling of Diffusion Models","url":"https://arxiv.org/html/2602.03211"},{"title":"Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps","url":"https://arxiv.org/html/2501.09732v1"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives","url":"https://arxiv.org/html/2505.05787"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .","url":"https://arxiv.org/pdf/2303.04137"},{"title":"Diffusion Policy:","url":"https://www.roboticsproceedings.org/rss19/p026.pdf"}]

I've completed the web search for your query about inference time scaling, diffusion policy, robot action verifier, and reward function in 2025-2026. Here are the relevant results:

## Key Findings:

**Inference-Time Scaling with Reward Functions:**

Inference-time scaling and steering of diffusion models – even with off-the-shelf rewards – can provide significant sample quality gains and controllability benefits. Feynman-Kac steering is an inference-time steering framework for sampling tilted distributions with diffusion models that enables guidance with arbitrary reward functions, differentiable or otherwise, for both discrete and continuous-state space models.

**Diffusion Policies for Robotics:**

Diffusion-based models for robotic control, including vision-language-action (VLA) and vision-action (VA) policies, have demonstrated significant capabilities, yet their advancement is constrained by the high cost of acquiring large-scale interaction datasets.

**Test-Time Scaling with Verifiers:**

Recent studies in test-time scaling of LLMs focus on better search/planning algorithms, better verifiers, and scaling law of test-time compute. The community has been orienting towards building agents with the ability to reason and self-correct, with diffusion models now studying inference-time scaling through a general search framework over injected noises during sampling.

**Lookahead Sample Reward Guidance:**

The Lookahead Sample Reward Guidance (LiDAR) sampler framework matches the GenEval performance of the latest gradient guidance method on SDXL while achieving a 9.5× reduction in inference time.

The search results show active research combining inference-time scaling, diffusion models, and reward-based guidance for both language models and robotics applications in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e112dbb3-e79e-4d47-ae38-9897fcffeb39",
  "isSidechain": false,
  "promptId": "965947ba-0f43-45e8-888d-1e4f472ba711",
  "type": "user",
  "uuid": "709ba4c2-e12e-4db1-aa4c-cc197df9ff4d",
  "toolUseResult": {
    "query": "\"inference time scaling\" \"diffusion policy\" robot action verifier reward function 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018eLttFmB1gXS6rQjvhPTSw",
        "content": [
          {
            "title": "[2504.02495] Inference-Time Scaling for Generalist Reward Modeling",
            "url": "https://arxiv.org/abs/2504.02495"
          },
          {
            "title": "Compose Your Policies! Improving Diffusion-based or Flow-based Robot Policies via Test-time Distribution-level Composition",
            "url": "https://arxiv.org/html/2510.01068"
          },
          {
            "title": "Diffusion Policy for Robot Learning: What It Is and How to Use It | SVRC",
            "url": "https://www.roboticscenter.ai/blog/diffusion-policy-robots"
          },
          {
            "title": "A General Framework for Inference-time Scaling and Steering of Diffusion Models",
            "url": "https://arxiv.org/html/2501.06848v3"
          },
          {
            "title": "Lookahead Sample Reward Guidance for Test-Time Scaling of Diffusion Models",
            "url": "https://arxiv.org/html/2602.03211"
          },
          {
            "title": "Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps",
            "url": "https://arxiv.org/html/2501.09732v1"
          },
          {
            "title": "GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub",
            "url": "https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"
          },
          {
            "title": "Demystifying Diffusion Policies: Action Memorization and Simple Lookup Table Alternatives",
            "url": "https://arxiv.org/html/2505.05787"
          },
          {
            "title": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion .",
            "url": "https://arxiv.org/pdf/2303.04137"
          },
          {
            "title": "Diffusion Policy:",
            "url": "https://www.roboticsproceedings.org/rss19/p026.pdf"
          }
        ]
      },
      "I've completed the web search for your query about inference time scaling, diffusion policy, robot action verifier, and reward function in 2025-2026. Here are the relevant results:\n\n## Key Findings:\n\n**Inference-Time Scaling with Reward Functions:**\n\nInference-time scaling and steering of diffusion models – even with off-the-shelf rewards – can provide significant sample quality gains and controllability benefits. Feynman-Kac steering is an inference-time steering framework for sampling tilted distributions with diffusion models that enables guidance with arbitrary reward functions, differentiable or otherwise, for both discrete and continuous-state space models.\n\n**Diffusion Policies for Robotics:**\n\nDiffusion-based models for robotic control, including vision-language-action (VLA) and vision-action (VA) policies, have demonstrated significant capabilities, yet their advancement is constrained by the high cost of acquiring large-scale interaction datasets.\n\n**Test-Time Scaling with Verifiers:**\n\nRecent studies in test-time scaling of LLMs focus on better search/planning algorithms, better verifiers, and scaling law of test-time compute. The community has been orienting towards building agents with the ability to reason and self-correct, with diffusion models now studying inference-time scaling through a general search framework over injected noises during sampling.\n\n**Lookahead Sample Reward Guidance:**\n\nThe Lookahead Sample Reward Guidance (LiDAR) sampler framework matches the GenEval performance of the latest gradient guidance method on SDXL while achieving a 9.5× reduction in inference time.\n\nThe search results show active research combining inference-time scaling, diffusion models, and reward-based guidance for both language models and robotics applications in 2025-2026."
    ],
    "durationSeconds": 10.386049065000028
  },
  "sourceToolAssistantUUID": "e112dbb3-e79e-4d47-ae38-9897fcffeb39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 104_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification o…",
  "leafUuid": "709ba4c2-e12e-4db1-aa4c-cc197df9ff4d",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 105_

```json
{
  "type": "ai-title",
  "aiTitle": "Revisit WAM geometric robustness via video-action alignment",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Assistant

_source line 106 · 2026-05-10T20:02:42.764Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me confirm my understanding of Fast-WAM:

1. Fast-WAM uses a Mixture-of-Transformers (MoT) with a video DiT (Wan2.2-5B) + action expert DiT
2. At inference: video backbone processes observation ONCE (single pass), then action expert generates actions
3. The action generation likely uses iterative denoising (since it has CFG scale parameter)
4. GitHub available with checkpoints on HuggingFace

The action expert DiT should use iterative denoising to generate action chunks. This is where GSF can be applied.


There's also relevant work on steering diffusion models at inference time using reward functions, which validates the principle of manipulating the denoising process. I could frame geometric consistency as a reward signal and apply Feynman-Kac steering, but my SVD approach is more direct—it doesn't require evaluating a reward function at each step, just applying the geometric constraint through the singular value decomposition.

Now I'm ready to finalize the idea. The key shift is moving from "Spectral Cross-Modal Guidance" (which depends on specific backbone architectures and has contingency risks) to "Geometric Sensitivity Filtering"—a backbone-agnostic method that works with any diffusion or flow policy, eliminates the contingency problem, and can leverage stronger baselines like Fast-WAM or OA-WAM while preserving the core SVD-based mathematics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "709ba4c2-e12e-4db1-aa4c-cc197df9ff4d",
  "isSidechain": false,
  "requestId": "req_011CauV6JAV5MEhwr7jAErxq",
  "type": "assistant",
  "uuid": "b956b98e-c12e-491f-bb9c-d75d182e2357",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UooLGAeK4M9mAE1vLnTtb5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3395,
      "cache_read_input_tokens": 66219,
      "output_tokens": 7117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7117,
          "cache_read_input_tokens": 66219,
          "cache_creation_input_tokens": 3395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3395
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

_source line 107 · 2026-05-10T20:05:15.514Z_

I now have all the information needed. After deep research, I'm performing a **major revision**. The original spectral cross-modal guidance approach has structural issues that 6 rounds of minor fixes can't resolve (backbone dependency on weak UWM, Phase 1 contingency). I'm redesigning the method from scratch while keeping the same core problem (training-free geometric robustness).

The key insight from my research: ALL existing geometric robustness methods (SE(3)-equivariant architectures, OA-WAM, CKT-WAM) require training-time changes. No test-time method exists. My revised approach filters action scores based on geometric sensitivity analysis, making it truly backbone-agnostic.

Here's the complete revised idea:

```json
{
  "change_type": "major",
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
```

**Key changes from the original and why:**

1. **Method pivot** (solves backbone crisis): GSF works on ANY diffusion/flow policy's action score — no need for UWM's independent timesteps or specific CFG-enabling architecture. Fast-WAM (97.6%) is now a viable, strong backbone.

2. **Eliminated Phase 1 contingency** (satisfies METHOD ONLY requirement): GSF is a direct method — either filtering helps or the threshold is set too aggressively. No diagnostic phase needed. No risk of ending up with only a negative result.

3. **Resolved calibration transferability**: The filtering threshold τ is determined by a simple ratio (suppress directions above τ·λ_max variance). Cross-task consistency of high-sensitivity subspaces is an ablation, not a requirement — even per-task τ requires only 5-10 episodes to tune.

4. **Clear positioning against equivariant methods**: SDP/EquiBot build equivariance into training; GSF achieves approximate stability at test time. This is the training-free counterpart narrative.

5. **Acknowledged X-WAM**: GSF avoids the timestep-mechanism debate entirely since it doesn't depend on independent timesteps.

6. **Narrowed to geometric perturbation**: Camera + Robot-Init are the focus; Light as negative control.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b956b98e-c12e-491f-bb9c-d75d182e2357",
  "isSidechain": false,
  "requestId": "req_011CauV6JAV5MEhwr7jAErxq",
  "type": "assistant",
  "uuid": "8216a780-a6a5-451e-a556-4ce55532d8a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UooLGAeK4M9mAE1vLnTtb5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3395,
      "cache_read_input_tokens": 66219,
      "output_tokens": 7117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7117,
          "cache_read_input_tokens": 66219,
          "cache_creation_input_tokens": 3395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3395
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

_source line 108_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification o…",
  "leafUuid": "8216a780-a6a5-451e-a556-4ce55532d8a9",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 109_

```json
{
  "type": "ai-title",
  "aiTitle": "Revisit WAM geometric robustness via video-action alignment",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 110_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Spectral Cross-Modal Guidance: Training-Free Selective Amplification o…",
  "leafUuid": "8216a780-a6a5-451e-a556-4ce55532d8a9",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---

### Runtime record

_source line 111_

```json
{
  "type": "ai-title",
  "aiTitle": "Revisit WAM geometric robustness via video-action alignment",
  "sessionId": "e88c533b-e76f-4333-88cd-e263b24f285e"
}
```

---
