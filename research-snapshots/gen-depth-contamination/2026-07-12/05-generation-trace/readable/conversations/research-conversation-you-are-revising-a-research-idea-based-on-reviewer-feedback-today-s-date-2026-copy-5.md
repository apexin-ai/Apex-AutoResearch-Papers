# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/359778ed-6dc4-481c-8b47-e9a2990ee60c.jsonl`
- **Structured JSON:** [`909fee94a9647448f798.json`](../../sessions/90/909fee94a9647448f798.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T09:21:05.173Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T09:21:05.173Z",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Commitment Depth Routing: Selective Video Activation in Video-Action Models\",\n  \"core_problem\": \"Video-Action Models (VAMs) like mimic-video train their action decoder robust to any τ_v ∈ [0,1] via logit-normal sampling, making τ_v a flexible test-time parameter. A foundational finding from mimic-video (arXiv:2512.15692): mimic-video's main text explicitly states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5),' and τ_v=1 achieves 46.9% task success on SIMPLER-Bridge described as 'a good default value that balances policy performance and inference speed' — the compute-efficient recommended starting point. At the same time, mimic-video Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies.' These findings are reconcilable, not contradictory: the main text identifies τ_v=1 as the best FIXED-GLOBAL τ_v (if you must pick one value for all tasks uniformly), while the Figure 5 caption describes the oracle per-task view — when optimal τ_v is selected independently per task, the distribution of per-task optima peaks at intermediate noise levels. CDR exploits precisely this gap: τ_v=1 is the best fixed-global τ_v baseline, but per-task (and per-observation) oracle routing to intermediate τ_v recovers gains that the fixed-global τ_v=1 default leaves on the table.\\n\\nτ_v=0 (fully denoised video) gives WORSE autonomous policy performance than intermediate τ_v values — confirmed by mimic-video — so the action-quality-optimal range excludes both extremes. The per-task τ_v sweep yields +9.4pp on SIMPLER-Bridge (46.9%→56.3%), proving SOME tasks genuinely benefit from actual video denoising (τ_v < 1) relative to the τ_v=1 fixed-global default. Fast-WAM (arXiv:2603.16666) achieves 97.6% LIBERO by skipping test-time future video generation entirely, confirming the high-τ_v regime is strong on average. The core gap is a selective video activation problem: which observations within which tasks need video denoising below τ_v=1 (i.e., below the confirmed best fixed-global), and can this be predicted zero-shot without expensive per-task offline rollouts?\\n\\nExisting approaches are non-adaptive: (1) LingBot-VA (RSS 2026) fixes τ_v≈0.6 uniformly — since mimic-video's main text establishes τ_v=1 as best fixed-global, this uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge; (2) Fast-WAM skips video entirely via architectural retraining — effective on average but permanently loses gains for tasks where video is genuinely critical; (3) mimic-video's per-task sweeping requires ~10 rollouts per new task at deployment time. CDR addresses this: default to τ_v=1 (confirmed best fixed-global by mimic-video main text), activate video denoising (route to τ_v < 1) only when the per-task or per-observation oracle justifies it, and Pareto-dominate the τ_v=1 fixed-global baseline on the task-success vs. mean-τ_v-consumed frontier on SIMPLER-Bridge.\\n\\nNote on concurrent work and absolute performance context: OA-WAM (arXiv:2605.06481, May 2026) achieves 79.3% on the same four WidowX Bridge tasks (Spoon Towel, Carrot Plate, Stack Cube, Eggplant Basket, Visual Matching protocol) — the identical evaluation setup as SIMPLER-Bridge. The 32pp gap between OA-WAM (79.3%) and mimic-video/CDR base (46.9%) reflects base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; mimic-video: 2B Cosmos-Predict2), not routing methodology. CDR is post-hoc on a frozen mimic-video checkpoint without retraining. The related work section explicitly states this distinction to pre-empt reviewer confusion about absolute performance comparisons.\",\n  \"opportunity\": \"The key enabling property is mimic-video's variable-τ_v training (logit-normal over [0,1]), which makes the action decoder capable of exploiting richer video features at lower τ_v while remaining functional at τ_v=1. CDR exploits this asymmetry: a lightweight router that defaults to τ_v=1 — the confirmed best fixed-global τ_v per mimic-video main text — and activates actual video denoising (routes to τ_v < 1) only for observations where the action decoder's output demonstrably benefits from real video structure.\\n\\nThe key reconciliation between mimic-video's two findings: (a) mimic-video's main text concludes τ_v=1 is the best fixed-global autonomous policy performance on SIMPLER-Bridge; (b) mimic-video's Figure 5 caption reports that performance peaks at an intermediate noise level when τ_v is optimized per-task (the oracle view). These are compatible: τ_v=1 wins when you must pick one global value, but the per-task oracle τ_v lives at intermediate levels — creating a +9.4pp gap (46.9%→56.3%) between the fixed-global default and the per-task sweep. CDR's primary claim is closing this gap: a lightweight router approximates the per-task or per-observation oracle, recovering gains that the fixed-global τ_v=1 leaves on the table, without the 10-rollout per-task sweep cost. This positions CDR's Pareto frontier claim squarely against the τ_v=1 fixed-global baseline.\\n\\nBecause mimic-video's main text establishes τ_v=1 as best fixed-global, CDR also pre-registers the prediction that LingBot-VA-style uniform partial denoising (fixed τ_v < 1 applied uniformly) will UNDERPERFORM τ_v=1 on SIMPLER-Bridge. If confirmed, this simplifies CDR's competitive landscape: LingBot-VA-style approaches are not valid Pareto competitors on this benchmark. CDR's Pareto win is cleanly against τ_v=1 alone — 'we beat the best fixed-global τ_v by selectively routing only the frames that need it.'\\n\\nTwo publishable outcomes with asymmetric CoRL value: (1) If per-observation τ_v* < 1 frames concentrate in precision phases with >2pp per-phase improvement: CDR demonstrates selective video activation as a Pareto-superior alternative to the τ_v=1 fixed-global default — the router outperforms the best fixed-threshold baseline on the task-success vs. mean-τ_v-consumed Pareto frontier on SIMPLER-Bridge. (2) If within-task per-phase variation is small (<2pp): task-level CDR router recovers ≥80% of per-task sweep gain (+7.5pp of +9.4pp) zero-shot on SIMPLER-Bridge — a concrete deployment contribution automating mimic-video's expensive per-task offline sweep via a frozen MLP trained on LIBERO-100 task embeddings. Outcome 2 must be framed with specific numerical targets (≥80% recovery) to meet CoRL bar; 'validation study alone' is insufficient.\\n\\nCDR's contribution is explicitly about extracting maximum performance from mimic-video's variable-τ_v training regime post-hoc; it does not claim to compete with architecturally distinct models (OA-WAM, Fast-WAM) that require retraining. The selective activation principle demonstrated on mimic-video is portable to any WAM supporting variable-τ_v inference.\",\n  \"landscape\": \"LingBot-VA (arXiv:2601.21998, RSS 2026, Ant Group) is CDR's primary comparison. Noisy History Augmentation (saug ∈ [0.5,1.0] during training) enables fixed 3-step inference to s=0.6. Key distinction from CDR: LingBot-VA imposes a LOWER τ_v (more denoising) than τ_v=1 uniformly across all frames. Because mimic-video's main text establishes τ_v=1 as the best fixed-global autonomous policy performance on SIMPLER-Bridge, LingBot-VA-style uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge — making LingBot-VA NOT a Pareto competitor on this benchmark. CDR's Pareto claim is therefore primarily against the τ_v=1 fixed-global baseline: if CDR matches or exceeds LingBot-VA's performance with lower mean τ_v consumed, AND exceeds τ_v=1 on precision tasks while keeping mean τ_v close to 1, CDR demonstrates Pareto-superior routing. 98.5% LIBERO (Spatial 98.5, Object 99.6, Goal 97.2, Long 98.5), 92.2% RoboTwin. No per-phase analysis; fixed threshold assumed without verification. NOTE: Due to mimic-video's noise-as-augmentation effect and main-text confirmation that τ_v=1 is best fixed-global on SIMPLER-Bridge, there is a formal pre-registered prediction that LingBot-VA-style fixed τ_v<1 baselines will underperform τ_v=1 on SIMPLER-Bridge — see Phase 3 pre-registration.\\n\\nmimic-video (arXiv:2512.15692, Dec 2025) is CDR's base model. Key findings: (a) Main text explicitly states: 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task; (c) RECONCILIATION: τ_v=1 wins as the best single fixed value (main text), but the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption) — CDR's contribution is approximating the per-task oracle via zero-shot routing; (d) per-task sweep yields +9.4pp (46.9%→56.3%), confirming the gap between fixed-global τ_v=1 and per-task oracle; (e) τ_v=0 gives WORSE performance than intermediate τ_v — the sweep range excludes τ_v=0. Note: mimic-video Table I does NOT enumerate fixed-global-τ_v comparisons (τ_v=0.5 vs 0.7 vs 0.9 vs 1.0) — CDR's Phase 3 baselines will be the first such systematic comparison on SIMPLER-Bridge. 93.9% LIBERO, 46.9%/56.3% SIMPLER-Bridge.\\n\\nFast-WAM (arXiv:2603.16666, Mar 2026) removes test-time future video prediction by processing only the first clean observation frame — architecturally different from τ_v=1 (which passes noisy future frames through the full backbone). 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. Important: Fast-WAM does NOT evaluate on SIMPLER-Bridge (results reported only on LIBERO and RoboTwin) — there is no Fast-WAM SIMPLER-Bridge number to compare against. CDR is post-hoc (no backbone retraining) and occupies the selective middle: defer to Fast-WAM-style efficiency (τ_v=1) by default, activate actual video generation for precision-critical frames. On SIMPLER-Bridge, CDR's baseline (a) τ_v=1 serves as the closest achievable proxy for Fast-WAM's test-time behavior on the mimic-video backbone.\\n\\nOA-WAM (arXiv:2605.06481, May 2026, Ding et al., IMPORTANT — MUST CITE) evaluates on LIBERO (97.8%) and SimplerEnv WidowX Bridge Visual Matching (79.3% average across Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%). CRITICAL: OA-WAM's 'SimplerEnv 79.3%' and CDR's 'SIMPLER-Bridge 46.9%' are the SAME four-task evaluation setup (identical task set and Visual Matching protocol). The 32pp performance gap reflects base model architecture and scale, not routing methodology: OA-WAM uses a 7B Chameleon-style trunk with slot-based object addressing and per-episode address vectors; CDR is post-hoc on mimic-video's 2B Cosmos-Predict2 backbone without retraining. DIFFERENTIATION from CDR: OA-WAM addresses object identity robustness in WAMs via scene decomposition into object slots — orthogonal to CDR's τ_v routing. OA-WAM requires full architectural retraining; CDR introduces no new training. Paper framing must state explicitly in related work and experimental sections: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks (Visual Matching); the performance gap is attributable to base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not the routing method CDR introduces. CDR's Pareto claims are within the mimic-video architecture family.'\\n\\nVADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) adapts ACTION diffusion denoising steps per task stage via a Hierarchical Vision Task Segmenter — orthogonal to CDR. VADF modifies the action diffusion process (fewer steps for simple actions, more for complex); CDR modifies the VIDEO backbone denoising depth (τ_v). These address different computational bottlenecks and can be combined. VADF is evaluated on simpler manipulation setups (Push-T, Adroit, ARX5); CDR targets WAM-class models on SIMPLER-Bridge and LIBERO-100.\\n\\nA₁ (arXiv:2604.05672, April 2026, MUST CITE as concurrent work) introduces per-observation inter-layer early exit via Inter-Layer Truncated Flow Matching for VLAs — achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION from CDR: A₁ targets how many transformer layers to compute in the VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth). These are orthogonal efficiency axes on different model families (VLAs vs WAMs). One-sentence cite in CDR related work: 'Concurrent work A₁ (arXiv:2604.05672) applies per-observation inter-layer early exit to VLA backbone computation; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal efficiency axes targeting different model families.'\\n\\nDiT4DiT (arXiv:2603.10448) ablation: single-step (high τ_v) is best on average — independently confirms the high-τ_v regime is a strong global default, corroborating mimic-video's main-text finding that τ_v=1 is best fixed-global on SIMPLER-Bridge, and supporting CDR's corrected framing. 98.6% LIBERO, 50.8% RoboCasa. DreamZero (arXiv:2602.15922, Feb 2026, 14B WAM) caches velocity within a denoising trajectory; complementary to CDR (reduces cost within given τ_v level vs. CDR choosing the τ_v level). ChEaP (arXiv:2603.30043) establishes early plan commitment in 2D mazes (first few denoising steps commit high-level motion; further steps add visual detail only); CDR empirically validates and extends this to 3D manipulation video backbones.\\n\\nDenoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) introduces the Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions complete denoising earlier while harder regions receive more denoising steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory timesteps — which frames in a manipulation episode need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined (spatial patch routing within each CDR-selected frame). Note: this paper is about image generation, not robot action models, and is cited as feasibility motivation only.\\n\\nMotuBrain (arXiv:2604.27792) is a unified VAM with Mixture-of-Transformers (MoT) architecture under a UniDiffuser formulation, supporting policy learning, world modeling, video generation, and inverse dynamics. Achieves 95.8%+ on RoboTwin 2.0 under clean and randomized settings with 50× speedup via step reduction, compilation, and FP8 quantization. DIFFERENTIATION from CDR: MotuBrain is a training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on a frozen mimic-video checkpoint requiring no backbone retraining. These are complementary — MotuBrain could serve as a future CDR base model if it supports variable-τ_v inference. Reviewers may mention MotuBrain as related work; distinguish on training-time architecture vs. test-time routing.\\n\\nD3P (arXiv:2508.06804) adapts ACTION denoising steps via RL — complementary efficiency axis (same as VADF, different mechanism). X-WAM (arXiv:2604.26694) uses Asynchronous Noise Sampling from a fixed joint distribution — not per-observation adaptive. UWM (arXiv:2504.02792) uses independent modality timesteps from fixed schedule. Being-H0.7 (arXiv:2605.00078) avoids pixel decoding via distillation. S-VAM (arXiv:2603.16195) distills multi-step to one-step; requires retraining. 'When to Trust Imagination' (arXiv:2605.06222) reduces replanning frequency; orthogonal to per-call CDR.\\n\\nNo existing VAM paper: (a) uses GT-action-referenced τ_v labeling; (b) provides the first empirical characterization of which 3D manipulation phases need τ_v < 1 below the confirmed best fixed-global τ_v=1; or (c) trains a zero-shot per-task/per-observation τ_v predictor that generalizes across tasks without offline rollouts.\",\n  \"approach\": \"CDR has four sequenced phases relative to a deployed mimic-video checkpoint (no backbone retraining required):\\n\\n**Phase 0 — Sanity Check + Preliminary Zero-Shot Validation (1–3 H100-hours, PREREQUISITE, run immediately):**\\nTake 5 LIBERO tasks spanning types (2 precision grasp/insert, 2 pick-and-place, 1 long-horizon). Run 3 demonstration trajectories each (~1,500 frames total). Sweep τ_v ∈ {1.0, 0.9, ..., 0.1} using the frozen mimic-video action decoder. Compute τ_v*(f) = argmin_{τ_v ∈ {1.0,...,0.1}} ||a_{τ_v}(f) − a_GT(f)||₂ for each frame f (GT action from demo teleop). Annotate frames by manipulation phase using end-effector distance to target + gripper state.\\n\\n[NEW] Preliminary zero-shot validation (run within Phase 0, ~1 additional H100-hour): Using CLIP image and frozen mimic-video language embeddings for the 5 tasks, train a task-level τ_v MLP on task-mean τ_v* from tasks 1–4. Evaluate zero-shot prediction on task 5. This 4→1 leave-one-out check validates whether task embedding space contains τ_v-predictive signal before committing the zero-shot LIBERO→SIMPLER-Bridge claim as a primary CoRL contribution. If prediction error on the held-out task is <20% of task 5's τ_v* value: preliminary evidence supports zero-shot generalization — proceed with zero-shot claim. If >20%: plan to include few-shot SIMPLER-Bridge adaptation (3 tasks) as fallback framing for Phase 3. Full 80/20 LIBERO held-out validation runs in Phase 2.\\n\\nDecision gate (by May 12):\\n- If <10% of frames have τ_v* < 0.9 (nearly all frames prefer τ_v=1 for action quality): per-observation variation is minimal. Pivot paper framing to 'τ_v=1 universality study + automated zero-shot per-task routing' — do NOT commit to full Phase 1 scope. Reframe contribution as empirical validation + deployment automation.\\n- If ≥20% of frames have τ_v* < 0.9 AND these cluster in grasp/insert phases: full CDR selective activation story is empirically supported. Proceed to Phase 1.\\n- Intermediate (10–20%): assess within-episode vs. across-task variance before proceeding.\\n\\n**Phase 1 — 3D Video Necessity Study (~40–60 H100-hours): The Primary Empirical Contribution**\\nFor each frame f in LIBERO-100 (100 tasks × 50 demos × ~100 steps ≈ 500K frames), compute:\\n\\n  τ_v*(f) = argmin_{τ_v ∈ {1.0, 0.9, ..., 0.1}} ||a_{τ_v}(f) − a_GT(f)||₂\\n\\nwhere a_GT(f) is the ground-truth demonstration action at frame f (available from LIBERO-100 teleop data) and a_{τ_v}(f) is the mimic-video action decoder output with τ_v-noised video input. The sweep range {1.0,...,0.1} excludes τ_v=0 entirely (confirmed worse than intermediate τ_v in mimic-video). NOTE: τ_v=1 is the expected modal value for τ_v*(f) given mimic-video's main-text finding; Phase 1 asks how many frames deviate from τ_v*=1.0, and whether deviations cluster in specific manipulation phases.\\n\\nAnnotate frames with manipulation phases: approach (end-effector distance > 5cm to target), pre-grasp (distance 1–5cm, gripper open), grasp (gripper closing event), transport (gripper closed, object moving), place (object near target, gripper opening). Derive from proprioceptive state; no additional network required.\\n\\nReport: (a) Distribution of τ_v* — specifically fraction of frames where τ_v*=1.0 (consistent with mimic-video main text) vs. τ_v* < 0.9 (deviations from fixed-global optimal); (b) Mean τ_v* by manipulation phase — do grasp/insert phases show significantly lower τ_v* than approach/transport, characterizing for the FIRST TIME which 3D manipulation phases need video denoising below the τ_v=1 fixed-global default?; (c) Within-episode τ_v* variance vs. across-task τ_v* variance — which dominates?; (d) Whether LingBot-VA's fixed s≈0.6 corresponds to over-denoising for approach frames.\\n\\n[Distribution shift mitigation]: Include suboptimal rollout states to reduce demo-vs-rollout gap. Specifically: run the mimic-video policy (τ_v=1) 3× per task on LIBERO-100, collect frames from failed/recovery trajectories (partial grasps, dropped objects, recovery approaches). Add these to the labeling dataset (~50% of total labeled frames from non-expert trajectories). This gives the router diverse training states including recovery behaviors seen during closed-loop evaluation.\\n\\nCompute: ~750K frames × 10 τ_v levels = ~7.5M backbone forward passes. With batch=64 on Cosmos-Predict2 (2B DiT), ~40–60 H100-hours.\\n\\n**Phase 2 — Router Training + Zero-Shot Hold-Out Validation (~6 H100-hours):**\\n4-class router: {τ_v=1.0 (no activation), τ_v∈[0.7,0.9] (light activation), τ_v∈[0.4,0.6] (medium activation), τ_v∈[0.1,0.3] (heavy activation)}. Labels from Phase 1 mapped to nearest class bin. Architecture: two-layer MLP (512-dim CLIP image embedding + 512-dim frozen mimic-video language embedding → 256-dim hidden ReLU → 4-class softmax). Loss: CE(τ̂, τ_v*_class) + λ·E[τ̂_consumed].\\n\\nConservative routing (addressing distribution shift): if max softmax probability < θ, predict τ_v=1.0 regardless of argmax — since τ_v=1 is the confirmed best fixed-global default, falling back to it on uncertain (OOD) states avoids unnecessary compute overhead while maintaining the quality floor. Sweep λ ∈ {0.01, 0.1, 0.5} and θ ∈ {0.5, 0.7, 0.9} to trace the accuracy-efficiency frontier.\\n\\nTask-level CDR variant: also train on task-mean τ_v* (average τ_v* across all frames in a task) to enable the per-task routing baseline (d) and test zero-shot generalization on SIMPLER-Bridge.\\n\\n[NEW] 80/20 LIBERO held-out validation (REQUIRED before finalizing zero-shot CoRL claim): Split LIBERO-100 into 80 training / 20 held-out tasks (stratified by task type). Train task-level τ_v MLP on 80 tasks' task-mean τ_v*. Test zero-shot on 20 held-out tasks: measure τ_v* recovery = (gain from predicted τ_v vs. τ_v=1) / (oracle gain from true τ_v* vs. τ_v=1).\\n\\nZero-shot claim gate:\\n- If ≥80% τ_v* recovery on 20 held-out LIBERO tasks → zero-shot LIBERO→SIMPLER-Bridge claim is empirically credible. Keep as primary CoRL claim: 'per-task CDR recovers ≥80% of +9.4pp zero-shot on SIMPLER-Bridge.'\\n- If <80% recovery on held-out LIBERO tasks → reframe to 'per-task routing with few-shot adaptation on 3 SIMPLER-Bridge tasks': train task-level MLP on the 3 SIMPLER-Bridge tasks with most available rollouts, test on remaining SIMPLER-Bridge tasks. This is still a deployment contribution (reduces 10-rollout per-task sweep to 3-task fine-tuning) but scoped more conservatively.\\n\\n**Phase 3 — Evaluation (~50 H100-hours, primary benchmark: SIMPLER-Bridge):**\\n\\n[ELEVATED ANCHOR CLAIM] Formal Pre-Registered Prediction: CDR's primary competitive framing is CDR vs. τ_v=1 fixed-global baseline. We formally pre-register two predictions before running Phase 3 experiments:\\n  (P1) Fixed intermediate τ_v baselines (b: τ_v=0.5; c: τ_v=0.7 and τ_v=0.9) will UNDERPERFORM baseline (a) τ_v=1 on SIMPLER-Bridge. This prediction is strongly supported by mimic-video's main text ('the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1') and independently corroborated by DiT4DiT's ablation that single-step (high τ_v) is best on average. The pre-registration converts a potential 'cherry-picked baselines' concern into a published empirical confirmation of mimic-video's finding.\\n  (P2) Per-task CDR zero-shot router outperforms τ_v=1 on SIMPLER-Bridge (recovers ≥80% of per-task sweep gain = ≥7.5pp) — the central routing contribution.\\n\\nImplications of P1 confirmation: LingBot-VA-style uniform τ_v<1 is not a valid Pareto competitor on SIMPLER-Bridge. CDR's Pareto claim simplifies to a clean head-to-head: CDR vs. τ_v=1 fixed-global. The paper headline becomes: 'τ_v=1 is the best fixed-global baseline; CDR Pareto-dominates it by selectively routing per-observation/per-task to the intermediate τ_v values that the per-task oracle requires.'\\n\\nImplications of P1 disconfirmation (some fixed τ_v < 1 outperforms τ_v=1 on SIMPLER-Bridge — less likely given mimic-video main text): CDR must Pareto-dominate the best fixed intermediate value. This is a harder but higher-impact claim. Either outcome is publishable; the pre-registration removes selective reporting concerns regardless.\\n\\nBaselines:\\n(a) mimic-video τ_v=1 global (confirmed best fixed-global per mimic-video main text; compute-efficient recommended default; 46.9% SIMPLER, 93.9% LIBERO). NOTE: this baseline also serves as CDR's closest achievable proxy for Fast-WAM's test-time video-skipping behavior on the mimic-video backbone — Fast-WAM (arXiv:2603.16666) does not evaluate on SIMPLER-Bridge and requires architectural retraining, so direct comparison is impossible; the paper notes this distinction explicitly.\\n(b) LingBot-VA-style fixed τ_v=0.5 on mimic-video base (formally predicted to underperform τ_v=1 per P1; included to empirically confirm pre-registration)\\n(c) LingBot-VA-style fixed τ_v=0.7 and τ_v=0.9 (systematic fixed-threshold sweep; NOTE: this is ALSO the first published fixed-global-τ_v comparison on SIMPLER-Bridge — mimic-video Table I does not include this sweep; confirms whether any fixed intermediate τ_v beats τ_v=1 globally)\\n(d) Per-task CDR router (predict task-mean τ_v* zero-shot on SIMPLER-Bridge — primary routing result; claim: recovers ≥80% of +9.4pp sweep gain = ≥7.5pp without offline rollouts; gated on Phase 2 held-out LIBERO validation)\\n(e) Per-observation CDR (full system)\\n(f) Per-task sweep oracle (56.3% SIMPLER — upper bound)\\n\\nPrimary results: Pareto curves (task success vs. mean τ_v consumed) on SIMPLER-Bridge, anchored at the τ_v=1 fixed-global point. LIBERO-100 results reported secondarily for comparability. Key empirical claims:\\n1. LingBot-VA-style uniform τ_v<1 is not a Pareto competitor on SIMPLER-Bridge — confirmed by pre-registered P1 (fixed τ_v < 1 underperforms τ_v=1)\\n2. Per-task CDR Pareto-dominates τ_v=1 fixed-global: matches or exceeds τ_v=1 task success at lower mean τ_v consumed, recovering ≥80% of the per-task sweep gap zero-shot\\n3. Per-observation CDR Pareto-dominates τ_v=1 on SIMPLER-Bridge — matching or exceeding the best fixed intermediate τ_v at strictly lower mean compute if P1 is disconfirmed, or beating τ_v=1 with near-1.0 mean τ_v if P1 confirmed\\n4. CDR allocates lower τ_v (more video activation) to grasp-phase frames than approach frames — interpretability via per-phase τ_v heatmaps, constituting the first empirical characterization of manipulation-phase video necessity in 3D WAMs\\n\\nBaseline note on OA-WAM: OA-WAM (arXiv:2605.06481) evaluates on the same four WidowX Bridge tasks (SimplerEnv Visual Matching) as SIMPLER-Bridge in CDR, achieving 79.3% vs. CDR base 46.9%. CDR does not include OA-WAM as a direct baseline because OA-WAM uses a fundamentally different base architecture (7B Chameleon-style trunk requiring full retraining) vs. CDR's post-hoc routing on frozen mimic-video (2B Cosmos-Predict2). The paper explicitly states: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks; the 79.3% vs. 46.9% performance gap reflects base model architecture and scale differences, not the routing contribution CDR introduces. CDR's Pareto claims are within the mimic-video architecture family and do not target models that require full retraining.'\\n\\nAblations: per-phase τ_v allocation analysis (grasp vs. approach); precision task subset (peg insertion, mug hanging) vs. coarse tasks; conservative routing ablation (θ sweep); zero-shot generalization from LIBERO-100 router to SIMPLER-Bridge tasks (no retraining — key deployment story).\\n\\nNote on absolute LIBERO numbers: CDR built on mimic-video (93.9%) will fall below LingBot-VA (98.5%) and DiT4DiT (98.6%) due to base model gap. Paper leads with SIMPLER-Bridge Pareto curves in abstract/intro, framed as: 'SIMPLER-Bridge is a real-to-sim transfer benchmark evaluated on four WidowX Bridge tasks under Visual Matching; mimic-video's 46.9% is the state-of-the-art for this backbone, and CDR's gain is measured against this competitive baseline.' LIBERO results in supplementary for comparability. Framing is explicit in introduction: 'Our contribution is the first empirical characterization of manipulation-phase video necessity in 3D WAMs (Phase 1 study) and the selective activation principle enabling zero-shot deployment, not absolute SOTA on LIBERO or SIMPLER-Bridge.'\\n\\n**Minimum Viable Submission (MVS) Track — Explicitly Defined:**\\nIf Phase 1 takes 8 days (upper bound: May 12–20) and Phase 3 cannot fully complete by May 26, the MVS constitutes a submittable CoRL 2026 paper:\\n- Phase 0 positive gate result (τ_v* distribution over 5 tasks with phase annotations)\\n- Phase 1 τ_v* distribution histograms across LIBERO-100 (primary contribution: first empirical characterization of which manipulation phases need τ_v < 1 below the τ_v=1 fixed-global default)\\n- Phase 2 router training + 80/20 held-out validation result\\n- Phase 3 PARTIAL: Pareto curve with minimum 3 points — {(a) τ_v=1 baseline, (c) best fixed intermediate τ_v, (d) per-task CDR zero-shot} on SIMPLER-Bridge\\n- Pre-registered prediction result for fixed τ_v < 1 baselines (P1 confirmation)\\nMVS drops: full per-observation CDR (Phase 3 baseline e), RoboCasa results, per-phase heatmap ablation, conservative routing θ sweep. If MVS is the submission path, the paper's primary contribution becomes: (1) first empirical study of τ_v* distribution in LIBERO-100 with manipulation-phase breakdown (Phase 1 histograms) — answering 'which phases need video denoising below the τ_v=1 fixed-global default for the first time'; (2) zero-shot per-task CDR on SIMPLER-Bridge; (3) pre-registered confirmation that uniform partial denoising underperforms τ_v=1. This is submittable as a focused empirical contribution even without full per-observation routing results.\\n\\n**Timeline for CoRL 2026 (May 29 deadline):**\\n- Phase 0: run May 10–11 (1–3 H100-hours including preliminary zero-shot check, 1–2 days)\\n- Phase 0 gate decision: May 12\\n- Phase 1 (if positive): May 12–18 (40–60h, with 8 H100s = 5–8 days)\\n- Phase 2: May 18–19 (~1–2 days, includes 80/20 held-out validation)\\n- Zero-shot claim gate decision: May 19\\n- Phase 3: May 19–25 (50h / 8 H100s = ~6 days; RoboCasa and per-phase heatmap ablations are explicitly drop-able if Phase 1 runs long — MVS requires only SIMPLER-Bridge primary Pareto curve {τ_v=1, best fixed τ_v, per-task CDR} plus pre-registered prediction confirmation)\\n- Write-up: May 25–28 (4 days; if Phase 1 takes 8 days, writing compresses to 2 days — acceptable for a focused Pareto-curve paper)\\n- Buffer: May 29 submission\\nFeasible but requires immediate Phase 0 execution. If Phase 0 is negative (< 10% activation frames), target ICLR 2027 with reframed 'zero-shot task routing' contribution.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~115–135 H100-hours (Phase 0: ~3h including preliminary zero-shot check; Phase 1: ~50h corrected sweep including rollout states; Phase 2: ~6h including 80/20 held-out validation; Phase 3: ~50h SIMPLER+LIBERO+baselines; ~20h buffer for reruns)\",\n      \"gpu_utilization\": \"45–55% effective — GPUs idle during Phase 0 gate decision, phase annotation, zero-shot gate decision, and result inspection\",\n      \"timeline\": \"2–3 weeks to CoRL submission (if Phase 0 positive by May 12); 2–3 months to ICLR 2027 otherwise\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$305 (122h × $2.49/hr spot H100)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~93 H100-hours\",\n      \"gpu_utilization\": \"65–75% — agent runs Phase 1 while human reviews Phase 0 gate; Phase 2 queued immediately after Phase 1 labels available; 80/20 validation runs in parallel with router training\",\n      \"timeline\": \"12–15 days to CoRL submission (Phase 0 gate on day 2, Phase 1 complete day 9, Phase 2 zero-shot gate day 10, Phase 3 complete day 15)\",\n      \"team\": \"1 researcher, ~20 min/day check-in\",\n      \"claude_api_cost\": \"~$100–200 (~1,000–2,000 turns at $0.10/turn Opus 4.7)\",\n      \"estimated_gpu_cost\": \"~$232 (93h × $2.49/hr spot H100)\",\n      \"risk_note\": \"Two critical decision points: (1) Phase 0 gate by May 12 — if <10% activation frames, reframe to zero-shot per-task routing, target ICLR 2027. (2) Phase 2 zero-shot gate by May 19 — if 80/20 LIBERO held-out validation fails (<80% τ_v* recovery), reframe primary zero-shot claim to few-shot SIMPLER-Bridge adaptation before committing it in the paper. Human judgment at both gates is essential. If Phase 1 takes 8 days (upper bound), MVS track is the fallback — dropping per-observation CDR and full ablations to submit the Phase 1 histograms + per-task CDR + pre-registered prediction result. Critical path has no slack beyond MVS; prioritize per-task CDR zero-shot result over per-observation CDR in Phase 3.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~410 H100-hours (Phase 0: 3h including zero-shot check; Phase 1 with rollout states: 70h; Phase 2 full λ×θ grid plus 80/20 validation: 17h; Phase 3 across SIMPLER+LIBERO+RoboCasa+all baselines: 200h; buffer: 120h)\",\n      \"gpu_utilization\": \"Near-zero idle — phases pipelined\",\n      \"timeline\": \"2–4 days with 8 H100s\",\n      \"team\": \"0 (only initial sweep grid and eval harness setup required)\",\n      \"claude_api_cost\": \"~$200–400 (~2,000–4,000 turns)\",\n      \"estimated_gpu_cost\": \"~$1021 (410h × $2.49/hr spot H100)\",\n      \"risk_note\": \"Auto mode must halt at Phase 0 gate and Phase 2 zero-shot gate before proceeding. Must not treat per-observation Pareto improvement as the only valid outcome — if Phase 1 shows task-level variation dominates or zero-shot gate fails, auto mode must automatically pivot to MVS track (per-task CDR zero-shot or few-shot adaptation). Auto mode should run 80/20 LIBERO held-out validation in Phase 2 before writing any claim about zero-shot SIMPLER-Bridge generalization into draft sections.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract deadline May 26, full paper May 29, 2026 — feasible only if Phase 0 positive by May 12 and MVS-track results complete by May 25)\",\n    \"ICLR 2027 (deadline expected September–October 2026 — fallback if Phase 0 negative or timeline slips)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (arXiv:2512.15692, Dec 2025) — CDR's base model. KEY VERIFIED FINDINGS — two distinct claims that must be cited separately: (a) MAIN TEXT (Section V-C): 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) FIGURE 5 CAPTION: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task. RECONCILIATION: τ_v=1 wins as the best single fixed global value (main text); the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption); CDR exploits this gap by approximating the per-task oracle via zero-shot routing; (c) Table I does NOT include a fixed-global-τ_v sweep — CDR's Phase 3 baselines provide the first such comparison on SIMPLER-Bridge; (d) per-task sweep +9.4pp (46.9%→56.3%), quantifying the gap between fixed-global τ_v=1 and per-task oracle; (e) τ_v=0 gives worse performance than intermediate τ_v — sweep excludes τ_v=0; (f) variable-τ_v training (logit-normal over [0,1]) makes action decoder robust at any τ_v — enabling CDR's selective activation without retraining\",\n    \"LingBot-VA: Causal World Modeling for Robot Control (arXiv:2601.21998, RSS 2026) — PRIMARY COMPARISON (predicted to underperform τ_v=1 on SIMPLER-Bridge per pre-registered P1, supported by mimic-video main text); Noisy History Augmentation (saug∈[0.5,1.0]) enables fixed 3-step inference to s≈0.6; 98.5% LIBERO, 92.2% RoboTwin; included in Phase 3 baselines to empirically confirm that uniform partial denoising (τ_v < 1 applied uniformly) is NOT a valid Pareto competitor against τ_v=1 on SIMPLER-Bridge\",\n    \"Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv:2603.16666, Mar 2026) — skips future video generation by processing only first clean observation; 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. IMPORTANT: Fast-WAM does NOT evaluate on SIMPLER-Bridge — no direct comparison number exists. CDR's baseline (a) τ_v=1 serves as closest achievable proxy for Fast-WAM's test-time video-skipping behavior on mimic-video backbone; paper states this distinction explicitly\",\n    \"OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv:2605.06481, May 2026) — MUST CITE; evaluates on LIBERO (97.8%) and SimplerEnv WidowX Bridge Visual Matching (79.3% average: Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%). CRITICAL: OA-WAM's SimplerEnv evaluation uses THE SAME four WidowX Bridge tasks and Visual Matching protocol as CDR's SIMPLER-Bridge — directly comparable evaluation setup. The 79.3% vs 46.9% gap is due to base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; CDR/mimic-video: 2B Cosmos-Predict2), not the routing method. DIFFERENTIATION: OA-WAM addresses object identity robustness via slot decomposition; CDR addresses adaptive video denoising depth via τ_v routing — orthogonal contributions. OA-WAM requires full architectural retraining; CDR is post-hoc on frozen checkpoint.\",\n    \"A₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model (arXiv:2604.05672, April 2026) — MUST CITE as concurrent work; applies per-observation Inter-Layer Truncated Flow Matching with early exit for VLA backbone computation, achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION: A₁ targets how many transformer layers to execute in a VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth routing) — orthogonal efficiency axes on different model families (VLAs vs WAMs).\",\n    \"VADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) — adapts ACTION diffusion denoising steps per task stage (shorter for simple, longer for complex); evaluated on Push-T, Adroit, ARX5; DIFFERENTIATION: VADF targets action denoising steps, CDR targets video backbone denoising depth (τ_v) — orthogonal efficiency axes, combinable\",\n    \"Video Models Reason Early: Exploiting Plan Commitment for Maze Solving (arXiv:2603.30043) — 2D commitment motivation: video diffusion commits high-level plan in first few denoising steps; CDR extends and empirically validates for 3D manipulation video backbones\",\n    \"DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control (arXiv:2603.10448) — fixed-step baseline; ablation confirms single-step (high τ_v) is best on average — independently corroborates mimic-video's main-text finding that τ_v=1 is best fixed-global on SIMPLER-Bridge, providing a second source supporting CDR's pre-registered P1 prediction; 98.6% LIBERO, 50.8% RoboCasa\",\n    \"DreamZero: World Action Models are Zero-shot Policies (arXiv:2602.15922, Feb 2026) — velocity caching within denoising trajectory; complementary to CDR (reduces cost within a fixed τ_v level vs. CDR selecting τ_v level before denoising begins)\",\n    \"Denoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) — introduces Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions advance denoising earlier, harder regions receive more steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory frames — which frames need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined. Cited as feasibility motivation only; evaluates image generation, not robot action models.\",\n    \"MotuBrain (arXiv:2604.27792) — unified VAM with Mixture-of-Transformers (MoT) architecture under UniDiffuser formulation; supports policy learning, world modeling, video generation, inverse dynamics; 95.8%+ on RoboTwin 2.0; 50× speedup via step reduction, FP8 quantization. DIFFERENTIATION: training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on frozen mimic-video checkpoint requiring no retraining. Orthogonal — MotuBrain could serve as future CDR base model.\",\n    \"D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning (arXiv:2508.06804) — adapts ACTION (not video) denoising steps via RL; orthogonal efficiency axis to CDR\",\n    \"S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight (arXiv:2603.16195, Mar 2026) — distillation-based efficiency; requires retraining\",\n    \"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (arXiv:2604.26694) — X-WAM; fixed-distribution ANS baseline; not per-observation adaptive\",\n    \"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (arXiv:2504.02792) — UWM; fixed schedule baseline\",\n    \"Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv:2605.00078) — distillation-based; different efficiency axis; 99.2% LIBERO, 62.1% RoboCasa\",\n    \"When to Trust Imagination: Adaptive Action Execution for World Action Models (arXiv:2605.06222) — episode-level replanning reduction; orthogonal to per-call CDR\"\n  ],\n  \"description\": \"Commitment Depth Routing (CDR) addresses selective video activation in Video-Action Models — providing the first empirical characterization of which 3D manipulation phases require video denoising below the confirmed best fixed-global τ_v=1, and learning a zero-shot router to approximate the per-task oracle τ_v without expensive offline sweeps.\\n\\nThe paper's theoretical foundation rests on a precise reconciliation of two mimic-video findings that prior versions of this idea conflated: (1) mimic-video's main text (Section V-C) states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1' — establishing τ_v=1 as the best fixed-global τ_v, which CDR adopts as its default; (2) mimic-video's Figure 5 caption states 'Performance peaks at an intermediate noise level' — referring to the oracle per-task view where τ_v is selected independently per task. These are compatible: τ_v=1 wins when one fixed value is applied globally (main text), but the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption). The +9.4pp per-task sweep gain (46.9%→56.3% on SIMPLER-Bridge) quantifies the gap. CDR's router closes this gap without the 10-rollout per-task sweep cost.\\n\\nCDR pre-registers two predictions before Phase 3 experiments: (P1) LingBot-VA-style fixed τ_v<1 baselines underperform τ_v=1 on SIMPLER-Bridge — strongly supported by mimic-video's main text and corroborated by DiT4DiT's ablation (single-step/high-τ_v is best on average). If P1 is confirmed, the competitive landscape simplifies: CDR's Pareto claim is cleanly against τ_v=1 alone — 'τ_v=1 is the best fixed-global; CDR beats it by routing per-task/per-observation to the intermediate τ_v that the oracle requires.' (P2) Per-task CDR zero-shot router recovers ≥80% of the +9.4pp sweep gap on SIMPLER-Bridge.\\n\\nThe paper's primary empirical contribution is Phase 1: the first systematic study of τ_v* (per-observation optimal denoising depth) across LIBERO-100 with manipulation-phase breakdown. The router (Phase 2, two-layer MLP on CLIP+language embeddings) is the deployment mechanism enabling zero-shot generalization, not the central novelty. Phase 3 reports Pareto curves on SIMPLER-Bridge anchored at the τ_v=1 fixed-global point, with LIBERO-100 results secondarily.\\n\\nThe paper explicitly frames: OA-WAM (arXiv:2605.06481) evaluates on the same four WidowX Bridge tasks (79.3% vs CDR base 46.9%); the gap reflects base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not CDR's routing contribution. CDR's Pareto claims are within the mimic-video architecture family. Target: CoRL 2026 (May 29); ICLR 2027 fallback.\",\n  \"project_name\": \"commit_depth_router\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 7)\nIssues: [\"MODERATE — DiT4DiT ablation is factually mischaracterized: Independent verification of arXiv:2603.10448 confirms that DiT4DiT's 'single-step is best' ablation (Figure 8b) concerns ACTION DENOISING STEPS (fewer action diffusion steps yield higher success), not τ_v (video noise level). CDR's landscape states: 'DiT4DiT ablation: single-step (high τ_v) is best on average — independently confirms the high-τ_v regime is a strong global default, corroborating mimic-video's main-text finding.' This conflates two different efficiency axes (action denoising steps vs. video noise level). Reviewers familiar with DiT4DiT will flag this. Fix: either remove DiT4DiT as corroborating evidence for τ_v=1 optimality, or rewrite as 'DiT4DiT finds that fewer action denoising steps improve performance — a parallel finding that the high-noise, low-denoising regime is preferable, supporting CDR's premise that less denoising is often better.' Do NOT use DiT4DiT to directly corroborate mimic-video's τ_v=1 result.\", \"MODERATE — Pareto efficiency claim is potentially misleading if P1 is confirmed: If P1 is confirmed (fixed intermediate τ_v < 1 uniformly underperforms τ_v=1 on SIMPLER-Bridge), then CDR's router will route the vast majority of frames to τ_v=1 (since τ_v=1 is the best single fixed value). The resulting 'compute savings' from CDR — measured as reduction in mean τ_v consumed below 1 — will be small (perhaps 5–10% of full video generation cost). The Pareto win is primarily in task SUCCESS (+≥7.5pp from zero-shot per-task routing), not in compute efficiency. The paper's abstract and intro must be honest about this: 'CDR's Pareto dominance is primarily measured in task success recovery, not compute savings, if the pre-registered P1 prediction is confirmed. The mean τ_v consumed by CDR remains close to 1 when P1 holds.' Misrepresenting the Pareto win as efficiency-driven when most frames route to τ_v=1 will trigger reviewer pushback.\", \"MODERATE — Auto-mode resource estimate (410 H100-hours) exceeds the ≤200 H100-hour budget constraint stated in user requirements. The manual estimate (115–135H) is within budget, but auto mode at 410H is 2-3× over the stated limit. Either: (a) cap the auto-mode scope to fit within 200H by dropping full RoboCasa, per-phase heatmap ablations, and the full λ×θ grid search; or (b) explicitly acknowledge in the proposal that auto-mode exceeds the 200H constraint and requires expanded budget authorization.\", \"MINOR — 'When to Trust Imagination' (arXiv:2605.06222) is misdescribed as 'reduces replanning frequency'; verified content shows it uses a per-action-chunk adaptive horizon mechanism with a fixed threshold τ=0.5 to decide when to replan after partial action execution — not episode-level replanning reduction. The orthogonality claim holds, but the description should be corrected to 'per-chunk adaptive replanning trigger' to avoid misleading reviewers.\", \"MINOR — Method contribution is architecturally thin for CoRL 2026's WAM track: The 2-layer MLP router (512-dim CLIP + 512-dim language → 256-dim hidden → 4-class softmax) is not a novel architecture. CoRL 2026's WAM submissions include DiT4DiT, MotuBrain, OA-WAM with substantial architectural innovation. CDR must foreground Phase 1 (first empirical characterization of manipulation-phase τ_v requirements) as the primary scientific contribution — the router is the deployment mechanism, not the contribution. The paper title 'Commitment Depth Routing' implies a routing method is the contribution; consider retitling to reflect the empirical study: e.g., 'When Do World Action Models Need Video? A Manipulation-Phase Study with Selective Denoising Activation.'\"]\nFeedback: CDR has fixed all prior critical issues through Round 6. The Round 7 proposal is now scientifically well-structured with explicit gates, correct mimic-video Figure 5 reconciliation, pre-registered predictions, and MVS fallback. Three focused fixes are required before CoRL submission:\n\n**Fix 1 (required, 30 minutes): Correct DiT4DiT characterization.** DiT4DiT's ablation (Figure 8b in arXiv:2603.10448) is about action denoising steps — not τ_v (video noise level). CDR incorrectly uses it to corroborate 'high τ_v is best on SIMPLER-Bridge.' Rewrite as: 'DiT4DiT finds that a single action denoising step outperforms multi-step action diffusion — a parallel finding that less denoising in the action domain also improves performance; we observe the same pattern in the video domain with mimic-video's τ_v=1 result.' Remove any language claiming DiT4DiT 'independently confirms' that high video noise τ_v is optimal.\n\n**Fix 2 (required, 20 minutes): Honestly bound the Pareto efficiency claim.** If P1 is confirmed (the expected outcome based on mimic-video main text), CDR routes most frames to τ_v=1, making compute savings modest. Add explicit language in the abstract and intro: 'CDR's primary Pareto benefit is task success recovery (≥7.5pp zero-shot on SIMPLER-Bridge), not compute efficiency — most frames continue to use τ_v=1, with video activation selectively applied only to frames where the Phase 1 study identifies τ_v* < 1.' This prevents reviewers from expecting large speedups and finding only 5-10% compute savings.\n\n**Fix 3 (budget reconciliation, 10 minutes): Cap auto-mode estimate.** The auto mode at 410 H100-hours violates the ≤200H project constraint. Either (a) reduce auto-mode scope to 150-180H (drop RoboCasa, full hyperparameter grid) while keeping the key SIMPLER-Bridge experiments, or (b) add a note that auto-mode exceeds the budget constraint and requires pre-authorization. The manual mode (115-135H) is within budget and should be the reference for the 200H limit.\n\n**Optional (strengthens paper): Retitle to foreground empirical contribution.** 'Commitment Depth Routing' implies a novel routing mechanism as the primary contribution. The actual primary contribution is Phase 1 — the first empirical study of which manipulation phases need τ_v < 1 in 3D WAMs. A title like 'When Does Robot Policy Need Video? Manipulation-Phase Analysis and Selective Activation for World Action Models' better positions the paper as an empirical methods contribution and reduces reviewer expectations of architectural novelty.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 7 轮修订，近 3 轮的平均分从 3.5 到 3.2，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T09:21:05.179Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T09:21:05.179Z",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c"
}
```

---

## Round 1

21 recorded events

### User

_source line 3 · 2026-05-10T09:21:05.223Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Commitment Depth Routing: Selective Video Activation in Video-Action Models",
  "core_problem": "Video-Action Models (VAMs) like mimic-video train their action decoder robust to any τ_v ∈ [0,1] via logit-normal sampling, making τ_v a flexible test-time parameter. A foundational finding from mimic-video (arXiv:2512.15692): mimic-video's main text explicitly states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5),' and τ_v=1 achieves 46.9% task success on SIMPLER-Bridge described as 'a good default value that balances policy performance and inference speed' — the compute-efficient recommended starting point. At the same time, mimic-video Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies.' These findings are reconcilable, not contradictory: the main text identifies τ_v=1 as the best FIXED-GLOBAL τ_v (if you must pick one value for all tasks uniformly), while the Figure 5 caption describes the oracle per-task view — when optimal τ_v is selected independently per task, the distribution of per-task optima peaks at intermediate noise levels. CDR exploits precisely this gap: τ_v=1 is the best fixed-global τ_v baseline, but per-task (and per-observation) oracle routing to intermediate τ_v recovers gains that the fixed-global τ_v=1 default leaves on the table.\n\nτ_v=0 (fully denoised video) gives WORSE autonomous policy performance than intermediate τ_v values — confirmed by mimic-video — so the action-quality-optimal range excludes both extremes. The per-task τ_v sweep yields +9.4pp on SIMPLER-Bridge (46.9%→56.3%), proving SOME tasks genuinely benefit from actual video denoising (τ_v < 1) relative to the τ_v=1 fixed-global default. Fast-WAM (arXiv:2603.16666) achieves 97.6% LIBERO by skipping test-time future video generation entirely, confirming the high-τ_v regime is strong on average. The core gap is a selective video activation problem: which observations within which tasks need video denoising below τ_v=1 (i.e., below the confirmed best fixed-global), and can this be predicted zero-shot without expensive per-task offline rollouts?\n\nExisting approaches are non-adaptive: (1) LingBot-VA (RSS 2026) fixes τ_v≈0.6 uniformly — since mimic-video's main text establishes τ_v=1 as best fixed-global, this uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge; (2) Fast-WAM skips video entirely via architectural retraining — effective on average but permanently loses gains for tasks where video is genuinely critical; (3) mimic-video's per-task sweeping requires ~10 rollouts per new task at deployment time. CDR addresses this: default to τ_v=1 (confirmed best fixed-global by mimic-video main text), activate video denoising (route to τ_v < 1) only when the per-task or per-observation oracle justifies it, and Pareto-dominate the τ_v=1 fixed-global baseline on the task-success vs. mean-τ_v-consumed frontier on SIMPLER-Bridge.\n\nNote on concurrent work and absolute performance context: OA-WAM (arXiv:2605.06481, May 2026) achieves 79.3% on the same four WidowX Bridge tasks (Spoon Towel, Carrot Plate, Stack Cube, Eggplant Basket, Visual Matching protocol) — the identical evaluation setup as SIMPLER-Bridge. The 32pp gap between OA-WAM (79.3%) and mimic-video/CDR base (46.9%) reflects base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; mimic-video: 2B Cosmos-Predict2), not routing methodology. CDR is post-hoc on a frozen mimic-video checkpoint without retraining. The related work section explicitly states this distinction to pre-empt reviewer confusion about absolute performance comparisons.",
  "opportunity": "The key enabling property is mimic-video's variable-τ_v training (logit-normal over [0,1]), which makes the action decoder capable of exploiting richer video features at lower τ_v while remaining functional at τ_v=1. CDR exploits this asymmetry: a lightweight router that defaults to τ_v=1 — the confirmed best fixed-global τ_v per mimic-video main text — and activates actual video denoising (routes to τ_v < 1) only for observations where the action decoder's output demonstrably benefits from real video structure.\n\nThe key reconciliation between mimic-video's two findings: (a) mimic-video's main text concludes τ_v=1 is the best fixed-global autonomous policy performance on SIMPLER-Bridge; (b) mimic-video's Figure 5 caption reports that performance peaks at an intermediate noise level when τ_v is optimized per-task (the oracle view). These are compatible: τ_v=1 wins when you must pick one global value, but the per-task oracle τ_v lives at intermediate levels — creating a +9.4pp gap (46.9%→56.3%) between the fixed-global default and the per-task sweep. CDR's primary claim is closing this gap: a lightweight router approximates the per-task or per-observation oracle, recovering gains that the fixed-global τ_v=1 leaves on the table, without the 10-rollout per-task sweep cost. This positions CDR's Pareto frontier claim squarely against the τ_v=1 fixed-global baseline.\n\nBecause mimic-video's main text establishes τ_v=1 as best fixed-global, CDR also pre-registers the prediction that LingBot-VA-style uniform partial denoising (fixed τ_v < 1 applied uniformly) will UNDERPERFORM τ_v=1 on SIMPLER-Bridge. If confirmed, this simplifies CDR's competitive landscape: LingBot-VA-style approaches are not valid Pareto competitors on this benchmark. CDR's Pareto win is cleanly against τ_v=1 alone — 'we beat the best fixed-global τ_v by selectively routing only the frames that need it.'\n\nTwo publishable outcomes with asymmetric CoRL value: (1) If per-observation τ_v* < 1 frames concentrate in precision phases with >2pp per-phase improvement: CDR demonstrates selective video activation as a Pareto-superior alternative to the τ_v=1 fixed-global default — the router outperforms the best fixed-threshold baseline on the task-success vs. mean-τ_v-consumed Pareto frontier on SIMPLER-Bridge. (2) If within-task per-phase variation is small (<2pp): task-level CDR router recovers ≥80% of per-task sweep gain (+7.5pp of +9.4pp) zero-shot on SIMPLER-Bridge — a concrete deployment contribution automating mimic-video's expensive per-task offline sweep via a frozen MLP trained on LIBERO-100 task embeddings. Outcome 2 must be framed with specific numerical targets (≥80% recovery) to meet CoRL bar; 'validation study alone' is insufficient.\n\nCDR's contribution is explicitly about extracting maximum performance from mimic-video's variable-τ_v training regime post-hoc; it does not claim to compete with architecturally distinct models (OA-WAM, Fast-WAM) that require retraining. The selective activation principle demonstrated on mimic-video is portable to any WAM supporting variable-τ_v inference.",
  "landscape": "LingBot-VA (arXiv:2601.21998, RSS 2026, Ant Group) is CDR's primary comparison. Noisy History Augmentation (saug ∈ [0.5,1.0] during training) enables fixed 3-step inference to s=0.6. Key distinction from CDR: LingBot-VA imposes a LOWER τ_v (more denoising) than τ_v=1 uniformly across all frames. Because mimic-video's main text establishes τ_v=1 as the best fixed-global autonomous policy performance on SIMPLER-Bridge, LingBot-VA-style uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge — making LingBot-VA NOT a Pareto competitor on this benchmark. CDR's Pareto claim is therefore primarily against the τ_v=1 fixed-global baseline: if CDR matches or exceeds LingBot-VA's performance with lower mean τ_v consumed, AND exceeds τ_v=1 on precision tasks while keeping mean τ_v close to 1, CDR demonstrates Pareto-superior routing. 98.5% LIBERO (Spatial 98.5, Object 99.6, Goal 97.2, Long 98.5), 92.2% RoboTwin. No per-phase analysis; fixed threshold assumed without verification. NOTE: Due to mimic-video's noise-as-augmentation effect and main-text confirmation that τ_v=1 is best fixed-global on SIMPLER-Bridge, there is a formal pre-registered prediction that LingBot-VA-style fixed τ_v<1 baselines will underperform τ_v=1 on SIMPLER-Bridge — see Phase 3 pre-registration.\n\nmimic-video (arXiv:2512.15692, Dec 2025) is CDR's base model. Key findings: (a) Main text explicitly states: 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task; (c) RECONCILIATION: τ_v=1 wins as the best single fixed value (main text), but the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption) — CDR's contribution is approximating the per-task oracle via zero-shot routing; (d) per-task sweep yields +9.4pp (46.9%→56.3%), confirming the gap between fixed-global τ_v=1 and per-task oracle; (e) τ_v=0 gives WORSE performance than intermediate τ_v — the sweep range excludes τ_v=0. Note: mimic-video Table I does NOT enumerate fixed-global-τ_v comparisons (τ_v=0.5 vs 0.7 vs 0.9 vs 1.0) — CDR's Phase 3 baselines will be the first such systematic comparison on SIMPLER-Bridge. 93.9% LIBERO, 46.9%/56.3% SIMPLER-Bridge.\n\nFast-WAM (arXiv:2603.16666, Mar 2026) removes test-time future video prediction by processing only the first clean observation frame — architecturally different from τ_v=1 (which passes noisy future frames through the full backbone). 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. Important: Fast-WAM does NOT evaluate on SIMPLER-Bridge (results reported only on LIBERO and RoboTwin) — there is no Fast-WAM SIMPLER-Bridge number to compare against. CDR is post-hoc (no backbone retraining) and occupies the selective middle: defer to Fast-WAM-style efficiency (τ_v=1) by default, activate actual video generation for precision-critical frames. On SIMPLER-Bridge, CDR's baseline (a) τ_v=1 serves as the closest achievable proxy for Fast-WAM's test-time behavior on the mimic-video backbone.\n\nOA-WAM (arXiv:2605.06481, May 2026, Ding et al., IMPORTANT — MUST CITE) evaluates on LIBERO (97.8%) and SimplerEnv WidowX Bridge Visual Matching (79.3% average across Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%). CRITICAL: OA-WAM's 'SimplerEnv 79.3%' and CDR's 'SIMPLER-Bridge 46.9%' are the SAME four-task evaluation setup (identical task set and Visual Matching protocol). The 32pp performance gap reflects base model architecture and scale, not routing methodology: OA-WAM uses a 7B Chameleon-style trunk with slot-based object addressing and per-episode address vectors; CDR is post-hoc on mimic-video's 2B Cosmos-Predict2 backbone without retraining. DIFFERENTIATION from CDR: OA-WAM addresses object identity robustness in WAMs via scene decomposition into object slots — orthogonal to CDR's τ_v routing. OA-WAM requires full architectural retraining; CDR introduces no new training. Paper framing must state explicitly in related work and experimental sections: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks (Visual Matching); the performance gap is attributable to base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not the routing method CDR introduces. CDR's Pareto claims are within the mimic-video architecture family.'\n\nVADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) adapts ACTION diffusion denoising steps per task stage via a Hierarchical Vision Task Segmenter — orthogonal to CDR. VADF modifies the action diffusion process (fewer steps for simple actions, more for complex); CDR modifies the VIDEO backbone denoising depth (τ_v). These address different computational bottlenecks and can be combined. VADF is evaluated on simpler manipulation setups (Push-T, Adroit, ARX5); CDR targets WAM-class models on SIMPLER-Bridge and LIBERO-100.\n\nA₁ (arXiv:2604.05672, April 2026, MUST CITE as concurrent work) introduces per-observation inter-layer early exit via Inter-Layer Truncated Flow Matching for VLAs — achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION from CDR: A₁ targets how many transformer layers to compute in the VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth). These are orthogonal efficiency axes on different model families (VLAs vs WAMs). One-sentence cite in CDR related work: 'Concurrent work A₁ (arXiv:2604.05672) applies per-observation inter-layer early exit to VLA backbone computation; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal efficiency axes targeting different model families.'\n\nDiT4DiT (arXiv:2603.10448) ablation: single-step (high τ_v) is best on average — independently confirms the high-τ_v regime is a strong global default, corroborating mimic-video's main-text finding that τ_v=1 is best fixed-global on SIMPLER-Bridge, and supporting CDR's corrected framing. 98.6% LIBERO, 50.8% RoboCasa. DreamZero (arXiv:2602.15922, Feb 2026, 14B WAM) caches velocity within a denoising trajectory; complementary to CDR (reduces cost within given τ_v level vs. CDR choosing the τ_v level). ChEaP (arXiv:2603.30043) establishes early plan commitment in 2D mazes (first few denoising steps commit high-level motion; further steps add visual detail only); CDR empirically validates and extends this to 3D manipulation video backbones.\n\nDenoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) introduces the Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions complete denoising earlier while harder regions receive more denoising steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory timesteps — which frames in a manipulation episode need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined (spatial patch routing within each CDR-selected frame). Note: this paper is about image generation, not robot action models, and is cited as feasibility motivation only.\n\nMotuBrain (arXiv:2604.27792) is a unified VAM with Mixture-of-Transformers (MoT) architecture under a UniDiffuser formulation, supporting policy learning, world modeling, video generation, and inverse dynamics. Achieves 95.8%+ on RoboTwin 2.0 under clean and randomized settings with 50× speedup via step reduction, compilation, and FP8 quantization. DIFFERENTIATION from CDR: MotuBrain is a training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on a frozen mimic-video checkpoint requiring no backbone retraining. These are complementary — MotuBrain could serve as a future CDR base model if it supports variable-τ_v inference. Reviewers may mention MotuBrain as related work; distinguish on training-time architecture vs. test-time routing.\n\nD3P (arXiv:2508.06804) adapts ACTION denoising steps via RL — complementary efficiency axis (same as VADF, different mechanism). X-WAM (arXiv:2604.26694) uses Asynchronous Noise Sampling from a fixed joint distribution — not per-observation adaptive. UWM (arXiv:2504.02792) uses independent modality timesteps from fixed schedule. Being-H0.7 (arXiv:2605.00078) avoids pixel decoding via distillation. S-VAM (arXiv:2603.16195) distills multi-step to one-step; requires retraining. 'When to Trust Imagination' (arXiv:2605.06222) reduces replanning frequency; orthogonal to per-call CDR.\n\nNo existing VAM paper: (a) uses GT-action-referenced τ_v labeling; (b) provides the first empirical characterization of which 3D manipulation phases need τ_v < 1 below the confirmed best fixed-global τ_v=1; or (c) trains a zero-shot per-task/per-observation τ_v predictor that generalizes across tasks without offline rollouts.",
  "approach": "CDR has four sequenced phases relative to a deployed mimic-video checkpoint (no backbone retraining required):\n\n**Phase 0 — Sanity Check + Preliminary Zero-Shot Validation (1–3 H100-hours, PREREQUISITE, run immediately):**\nTake 5 LIBERO tasks spanning types (2 precision grasp/insert, 2 pick-and-place, 1 long-horizon). Run 3 demonstration trajectories each (~1,500 frames total). Sweep τ_v ∈ {1.0, 0.9, ..., 0.1} using the frozen mimic-video action decoder. Compute τ_v*(f) = argmin_{τ_v ∈ {1.0,...,0.1}} ||a_{τ_v}(f) − a_GT(f)||₂ for each frame f (GT action from demo teleop). Annotate frames by manipulation phase using end-effector distance to target + gripper state.\n\n[NEW] Preliminary zero-shot validation (run within Phase 0, ~1 additional H100-hour): Using CLIP image and frozen mimic-video language embeddings for the 5 tasks, train a task-level τ_v MLP on task-mean τ_v* from tasks 1–4. Evaluate zero-shot prediction on task 5. This 4→1 leave-one-out check validates whether task embedding space contains τ_v-predictive signal before committing the zero-shot LIBERO→SIMPLER-Bridge claim as a primary CoRL contribution. If prediction error on the held-out task is <20% of task 5's τ_v* value: preliminary evidence supports zero-shot generalization — proceed with zero-shot claim. If >20%: plan to include few-shot SIMPLER-Bridge adaptation (3 tasks) as fallback framing for Phase 3. Full 80/20 LIBERO held-out validation runs in Phase 2.\n\nDecision gate (by May 12):\n- If <10% of frames have τ_v* < 0.9 (nearly all frames prefer τ_v=1 for action quality): per-observation variation is minimal. Pivot paper framing to 'τ_v=1 universality study + automated zero-shot per-task routing' — do NOT commit to full Phase 1 scope. Reframe contribution as empirical validation + deployment automation.\n- If ≥20% of frames have τ_v* < 0.9 AND these cluster in grasp/insert phases: full CDR selective activation story is empirically supported. Proceed to Phase 1.\n- Intermediate (10–20%): assess within-episode vs. across-task variance before proceeding.\n\n**Phase 1 — 3D Video Necessity Study (~40–60 H100-hours): The Primary Empirical Contribution**\nFor each frame f in LIBERO-100 (100 tasks × 50 demos × ~100 steps ≈ 500K frames), compute:\n\n  τ_v*(f) = argmin_{τ_v ∈ {1.0, 0.9, ..., 0.1}} ||a_{τ_v}(f) − a_GT(f)||₂\n\nwhere a_GT(f) is the ground-truth demonstration action at frame f (available from LIBERO-100 teleop data) and a_{τ_v}(f) is the mimic-video action decoder output with τ_v-noised video input. The sweep range {1.0,...,0.1} excludes τ_v=0 entirely (confirmed worse than intermediate τ_v in mimic-video). NOTE: τ_v=1 is the expected modal value for τ_v*(f) given mimic-video's main-text finding; Phase 1 asks how many frames deviate from τ_v*=1.0, and whether deviations cluster in specific manipulation phases.\n\nAnnotate frames with manipulation phases: approach (end-effector distance > 5cm to target), pre-grasp (distance 1–5cm, gripper open), grasp (gripper closing event), transport (gripper closed, object moving), place (object near target, gripper opening). Derive from proprioceptive state; no additional network required.\n\nReport: (a) Distribution of τ_v* — specifically fraction of frames where τ_v*=1.0 (consistent with mimic-video main text) vs. τ_v* < 0.9 (deviations from fixed-global optimal); (b) Mean τ_v* by manipulation phase — do grasp/insert phases show significantly lower τ_v* than approach/transport, characterizing for the FIRST TIME which 3D manipulation phases need video denoising below the τ_v=1 fixed-global default?; (c) Within-episode τ_v* variance vs. across-task τ_v* variance — which dominates?; (d) Whether LingBot-VA's fixed s≈0.6 corresponds to over-denoising for approach frames.\n\n[Distribution shift mitigation]: Include suboptimal rollout states to reduce demo-vs-rollout gap. Specifically: run the mimic-video policy (τ_v=1) 3× per task on LIBERO-100, collect frames from failed/recovery trajectories (partial grasps, dropped objects, recovery approaches). Add these to the labeling dataset (~50% of total labeled frames from non-expert trajectories). This gives the router diverse training states including recovery behaviors seen during closed-loop evaluation.\n\nCompute: ~750K frames × 10 τ_v levels = ~7.5M backbone forward passes. With batch=64 on Cosmos-Predict2 (2B DiT), ~40–60 H100-hours.\n\n**Phase 2 — Router Training + Zero-Shot Hold-Out Validation (~6 H100-hours):**\n4-class router: {τ_v=1.0 (no activation), τ_v∈[0.7,0.9] (light activation), τ_v∈[0.4,0.6] (medium activation), τ_v∈[0.1,0.3] (heavy activation)}. Labels from Phase 1 mapped to nearest class bin. Architecture: two-layer MLP (512-dim CLIP image embedding + 512-dim frozen mimic-video language embedding → 256-dim hidden ReLU → 4-class softmax). Loss: CE(τ̂, τ_v*_class) + λ·E[τ̂_consumed].\n\nConservative routing (addressing distribution shift): if max softmax probability < θ, predict τ_v=1.0 regardless of argmax — since τ_v=1 is the confirmed best fixed-global default, falling back to it on uncertain (OOD) states avoids unnecessary compute overhead while maintaining the quality floor. Sweep λ ∈ {0.01, 0.1, 0.5} and θ ∈ {0.5, 0.7, 0.9} to trace the accuracy-efficiency frontier.\n\nTask-level CDR variant: also train on task-mean τ_v* (average τ_v* across all frames in a task) to enable the per-task routing baseline (d) and test zero-shot generalization on SIMPLER-Bridge.\n\n[NEW] 80/20 LIBERO held-out validation (REQUIRED before finalizing zero-shot CoRL claim): Split LIBERO-100 into 80 training / 20 held-out tasks (stratified by task type). Train task-level τ_v MLP on 80 tasks' task-mean τ_v*. Test zero-shot on 20 held-out tasks: measure τ_v* recovery = (gain from predicted τ_v vs. τ_v=1) / (oracle gain from true τ_v* vs. τ_v=1).\n\nZero-shot claim gate:\n- If ≥80% τ_v* recovery on 20 held-out LIBERO tasks → zero-shot LIBERO→SIMPLER-Bridge claim is empirically credible. Keep as primary CoRL claim: 'per-task CDR recovers ≥80% of +9.4pp zero-shot on SIMPLER-Bridge.'\n- If <80% recovery on held-out LIBERO tasks → reframe to 'per-task routing with few-shot adaptation on 3 SIMPLER-Bridge tasks': train task-level MLP on the 3 SIMPLER-Bridge tasks with most available rollouts, test on remaining SIMPLER-Bridge tasks. This is still a deployment contribution (reduces 10-rollout per-task sweep to 3-task fine-tuning) but scoped more conservatively.\n\n**Phase 3 — Evaluation (~50 H100-hours, primary benchmark: SIMPLER-Bridge):**\n\n[ELEVATED ANCHOR CLAIM] Formal Pre-Registered Prediction: CDR's primary competitive framing is CDR vs. τ_v=1 fixed-global baseline. We formally pre-register two predictions before running Phase 3 experiments:\n  (P1) Fixed intermediate τ_v baselines (b: τ_v=0.5; c: τ_v=0.7 and τ_v=0.9) will UNDERPERFORM baseline (a) τ_v=1 on SIMPLER-Bridge. This prediction is strongly supported by mimic-video's main text ('the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1') and independently corroborated by DiT4DiT's ablation that single-step (high τ_v) is best on average. The pre-registration converts a potential 'cherry-picked baselines' concern into a published empirical confirmation of mimic-video's finding.\n  (P2) Per-task CDR zero-shot router outperforms τ_v=1 on SIMPLER-Bridge (recovers ≥80% of per-task sweep gain = ≥7.5pp) — the central routing contribution.\n\nImplications of P1 confirmation: LingBot-VA-style uniform τ_v<1 is not a valid Pareto competitor on SIMPLER-Bridge. CDR's Pareto claim simplifies to a clean head-to-head: CDR vs. τ_v=1 fixed-global. The paper headline becomes: 'τ_v=1 is the best fixed-global baseline; CDR Pareto-dominates it by selectively routing per-observation/per-task to the intermediate τ_v values that the per-task oracle requires.'\n\nImplications of P1 disconfirmation (some fixed τ_v < 1 outperforms τ_v=1 on SIMPLER-Bridge — less likely given mimic-video main text): CDR must Pareto-dominate the best fixed intermediate value. This is a harder but higher-impact claim. Either outcome is publishable; the pre-registration removes selective reporting concerns regardless.\n\nBaselines:\n(a) mimic-video τ_v=1 global (confirmed best fixed-global per mimic-video main text; compute-efficient recommended default; 46.9% SIMPLER, 93.9% LIBERO). NOTE: this baseline also serves as CDR's closest achievable proxy for Fast-WAM's test-time video-skipping behavior on the mimic-video backbone — Fast-WAM (arXiv:2603.16666) does not evaluate on SIMPLER-Bridge and requires architectural retraining, so direct comparison is impossible; the paper notes this distinction explicitly.\n(b) LingBot-VA-style fixed τ_v=0.5 on mimic-video base (formally predicted to underperform τ_v=1 per P1; included to empirically confirm pre-registration)\n(c) LingBot-VA-style fixed τ_v=0.7 and τ_v=0.9 (systematic fixed-threshold sweep; NOTE: this is ALSO the first published fixed-global-τ_v comparison on SIMPLER-Bridge — mimic-video Table I does not include this sweep; confirms whether any fixed intermediate τ_v beats τ_v=1 globally)\n(d) Per-task CDR router (predict task-mean τ_v* zero-shot on SIMPLER-Bridge — primary routing result; claim: recovers ≥80% of +9.4pp sweep gain = ≥7.5pp without offline rollouts; gated on Phase 2 held-out LIBERO validation)\n(e) Per-observation CDR (full system)\n(f) Per-task sweep oracle (56.3% SIMPLER — upper bound)\n\nPrimary results: Pareto curves (task success vs. mean τ_v consumed) on SIMPLER-Bridge, anchored at the τ_v=1 fixed-global point. LIBERO-100 results reported secondarily for comparability. Key empirical claims:\n1. LingBot-VA-style uniform τ_v<1 is not a Pareto competitor on SIMPLER-Bridge — confirmed by pre-registered P1 (fixed τ_v < 1 underperforms τ_v=1)\n2. Per-task CDR Pareto-dominates τ_v=1 fixed-global: matches or exceeds τ_v=1 task success at lower mean τ_v consumed, recovering ≥80% of the per-task sweep gap zero-shot\n3. Per-observation CDR Pareto-dominates τ_v=1 on SIMPLER-Bridge — matching or exceeding the best fixed intermediate τ_v at strictly lower mean compute if P1 is disconfirmed, or beating τ_v=1 with near-1.0 mean τ_v if P1 confirmed\n4. CDR allocates lower τ_v (more video activation) to grasp-phase frames than approach frames — interpretability via per-phase τ_v heatmaps, constituting the first empirical characterization of manipulation-phase video necessity in 3D WAMs\n\nBaseline note on OA-WAM: OA-WAM (arXiv:2605.06481) evaluates on the same four WidowX Bridge tasks (SimplerEnv Visual Matching) as SIMPLER-Bridge in CDR, achieving 79.3% vs. CDR base 46.9%. CDR does not include OA-WAM as a direct baseline because OA-WAM uses a fundamentally different base architecture (7B Chameleon-style trunk requiring full retraining) vs. CDR's post-hoc routing on frozen mimic-video (2B Cosmos-Predict2). The paper explicitly states: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks; the 79.3% vs. 46.9% performance gap reflects base model architecture and scale differences, not the routing contribution CDR introduces. CDR's Pareto claims are within the mimic-video architecture family and do not target models that require full retraining.'\n\nAblations: per-phase τ_v allocation analysis (grasp vs. approach); precision task subset (peg insertion, mug hanging) vs. coarse tasks; conservative routing ablation (θ sweep); zero-shot generalization from LIBERO-100 router to SIMPLER-Bridge tasks (no retraining — key deployment story).\n\nNote on absolute LIBERO numbers: CDR built on mimic-video (93.9%) will fall below LingBot-VA (98.5%) and DiT4DiT (98.6%) due to base model gap. Paper leads with SIMPLER-Bridge Pareto curves in abstract/intro, framed as: 'SIMPLER-Bridge is a real-to-sim transfer benchmark evaluated on four WidowX Bridge tasks under Visual Matching; mimic-video's 46.9% is the state-of-the-art for this backbone, and CDR's gain is measured against this competitive baseline.' LIBERO results in supplementary for comparability. Framing is explicit in introduction: 'Our contribution is the first empirical characterization of manipulation-phase video necessity in 3D WAMs (Phase 1 study) and the selective activation principle enabling zero-shot deployment, not absolute SOTA on LIBERO or SIMPLER-Bridge.'\n\n**Minimum Viable Submission (MVS) Track — Explicitly Defined:**\nIf Phase 1 takes 8 days (upper bound: May 12–20) and Phase 3 cannot fully complete by May 26, the MVS constitutes a submittable CoRL 2026 paper:\n- Phase 0 positive gate result (τ_v* distribution over 5 tasks with phase annotations)\n- Phase 1 τ_v* distribution histograms across LIBERO-100 (primary contribution: first empirical characterization of which manipulation phases need τ_v < 1 below the τ_v=1 fixed-global default)\n- Phase 2 router training + 80/20 held-out validation result\n- Phase 3 PARTIAL: Pareto curve with minimum 3 points — {(a) τ_v=1 baseline, (c) best fixed intermediate τ_v, (d) per-task CDR zero-shot} on SIMPLER-Bridge\n- Pre-registered prediction result for fixed τ_v < 1 baselines (P1 confirmation)\nMVS drops: full per-observation CDR (Phase 3 baseline e), RoboCasa results, per-phase heatmap ablation, conservative routing θ sweep. If MVS is the submission path, the paper's primary contribution becomes: (1) first empirical study of τ_v* distribution in LIBERO-100 with manipulation-phase breakdown (Phase 1 histograms) — answering 'which phases need video denoising below the τ_v=1 fixed-global default for the first time'; (2) zero-shot per-task CDR on SIMPLER-Bridge; (3) pre-registered confirmation that uniform partial denoising underperforms τ_v=1. This is submittable as a focused empirical contribution even without full per-observation routing results.\n\n**Timeline for CoRL 2026 (May 29 deadline):**\n- Phase 0: run May 10–11 (1–3 H100-hours including preliminary zero-shot check, 1–2 days)\n- Phase 0 gate decision: May 12\n- Phase 1 (if positive): May 12–18 (40–60h, with 8 H100s = 5–8 days)\n- Phase 2: May 18–19 (~1–2 days, includes 80/20 held-out validation)\n- Zero-shot claim gate decision: May 19\n- Phase 3: May 19–25 (50h / 8 H100s = ~6 days; RoboCasa and per-phase heatmap ablations are explicitly drop-able if Phase 1 runs long — MVS requires only SIMPLER-Bridge primary Pareto curve {τ_v=1, best fixed τ_v, per-task CDR} plus pre-registered prediction confirmation)\n- Write-up: May 25–28 (4 days; if Phase 1 takes 8 days, writing compresses to 2 days — acceptable for a focused Pareto-curve paper)\n- Buffer: May 29 submission\nFeasible but requires immediate Phase 0 execution. If Phase 0 is negative (< 10% activation frames), target ICLR 2027 with reframed 'zero-shot task routing' contribution.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~115–135 H100-hours (Phase 0: ~3h including preliminary zero-shot check; Phase 1: ~50h corrected sweep including rollout states; Phase 2: ~6h including 80/20 held-out validation; Phase 3: ~50h SIMPLER+LIBERO+baselines; ~20h buffer for reruns)",
      "gpu_utilization": "45–55% effective — GPUs idle during Phase 0 gate decision, phase annotation, zero-shot gate decision, and result inspection",
      "timeline": "2–3 weeks to CoRL submission (if Phase 0 positive by May 12); 2–3 months to ICLR 2027 otherwise",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$305 (122h × $2.49/hr spot H100)"
    },
    "human_in_loop": {
      "gpu_hours": "~93 H100-hours",
      "gpu_utilization": "65–75% — agent runs Phase 1 while human reviews Phase 0 gate; Phase 2 queued immediately after Phase 1 labels available; 80/20 validation runs in parallel with router training",
      "timeline": "12–15 days to CoRL submission (Phase 0 gate on day 2, Phase 1 complete day 9, Phase 2 zero-shot gate day 10, Phase 3 complete day 15)",
      "team": "1 researcher, ~20 min/day check-in",
      "claude_api_cost": "~$100–200 (~1,000–2,000 turns at $0.10/turn Opus 4.7)",
      "estimated_gpu_cost": "~$232 (93h × $2.49/hr spot H100)",
      "risk_note": "Two critical decision points: (1) Phase 0 gate by May 12 — if <10% activation frames, reframe to zero-shot per-task routing, target ICLR 2027. (2) Phase 2 zero-shot gate by May 19 — if 80/20 LIBERO held-out validation fails (<80% τ_v* recovery), reframe primary zero-shot claim to few-shot SIMPLER-Bridge adaptation before committing it in the paper. Human judgment at both gates is essential. If Phase 1 takes 8 days (upper bound), MVS track is the fallback — dropping per-observation CDR and full ablations to submit the Phase 1 histograms + per-task CDR + pre-registered prediction result. Critical path has no slack beyond MVS; prioritize per-task CDR zero-shot result over per-observation CDR in Phase 3."
    },
    "auto_research": {
      "gpu_hours": "~410 H100-hours (Phase 0: 3h including zero-shot check; Phase 1 with rollout states: 70h; Phase 2 full λ×θ grid plus 80/20 validation: 17h; Phase 3 across SIMPLER+LIBERO+RoboCasa+all baselines: 200h; buffer: 120h)",
      "gpu_utilization": "Near-zero idle — phases pipelined",
      "timeline": "2–4 days with 8 H100s",
      "team": "0 (only initial sweep grid and eval harness setup required)",
      "claude_api_cost": "~$200–400 (~2,000–4,000 turns)",
      "estimated_gpu_cost": "~$1021 (410h × $2.49/hr spot H100)",
      "risk_note": "Auto mode must halt at Phase 0 gate and Phase 2 zero-shot gate before proceeding. Must not treat per-observation Pareto improvement as the only valid outcome — if Phase 1 shows task-level variation dominates or zero-shot gate fails, auto mode must automatically pivot to MVS track (per-task CDR zero-shot or few-shot adaptation). Auto mode should run 80/20 LIBERO held-out validation in Phase 2 before writing any claim about zero-shot SIMPLER-Bridge generalization into draft sections."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract deadline May 26, full paper May 29, 2026 — feasible only if Phase 0 positive by May 12 and MVS-track results complete by May 25)",
    "ICLR 2027 (deadline expected September–October 2026 — fallback if Phase 0 negative or timeline slips)"
  ],
  "level": "solid",
  "key_references": [
    "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (arXiv:2512.15692, Dec 2025) — CDR's base model. KEY VERIFIED FINDINGS — two distinct claims that must be cited separately: (a) MAIN TEXT (Section V-C): 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) FIGURE 5 CAPTION: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task. RECONCILIATION: τ_v=1 wins as the best single fixed global value (main text); the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption); CDR exploits this gap by approximating the per-task oracle via zero-shot routing; (c) Table I does NOT include a fixed-global-τ_v sweep — CDR's Phase 3 baselines provide the first such comparison on SIMPLER-Bridge; (d) per-task sweep +9.4pp (46.9%→56.3%), quantifying the gap between fixed-global τ_v=1 and per-task oracle; (e) τ_v=0 gives worse performance than intermediate τ_v — sweep excludes τ_v=0; (f) variable-τ_v training (logit-normal over [0,1]) makes action decoder robust at any τ_v — enabling CDR's selective activation without retraining",
    "LingBot-VA: Causal World Modeling for Robot Control (arXiv:2601.21998, RSS 2026) — PRIMARY COMPARISON (predicted to underperform τ_v=1 on SIMPLER-Bridge per pre-registered P1, supported by mimic-video main text); Noisy History Augmentation (saug∈[0.5,1.0]) enables fixed 3-step inference to s≈0.6; 98.5% LIBERO, 92.2% RoboTwin; included in Phase 3 baselines to empirically confirm that uniform partial denoising (τ_v < 1 applied uniformly) is NOT a valid Pareto competitor against τ_v=1 on SIMPLER-Bridge",
    "Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv:2603.16666, Mar 2026) — skips future video generation by processing only first clean observation; 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. IMPORTANT: Fast-WAM does NOT evaluate on SIMPLER-Bridge — no direct comparison number exists. CDR's baseline (a) τ_v=1 serves as closest achievable proxy for Fast-WAM's test-time video-skipping behavior on mimic-video backbone; paper states this distinction explicitly",
    "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv:2605.06481, May 2026) — MUST CITE; evaluates on LIBERO (97.8%) and SimplerEnv WidowX Bridge Visual Matching (79.3% average: Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%). CRITICAL: OA-WAM's SimplerEnv evaluation uses THE SAME four WidowX Bridge tasks and Visual Matching protocol as CDR's SIMPLER-Bridge — directly comparable evaluation setup. The 79.3% vs 46.9% gap is due to base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; CDR/mimic-video: 2B Cosmos-Predict2), not the routing method. DIFFERENTIATION: OA-WAM addresses object identity robustness via slot decomposition; CDR addresses adaptive video denoising depth via τ_v routing — orthogonal contributions. OA-WAM requires full architectural retraining; CDR is post-hoc on frozen checkpoint.",
    "A₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model (arXiv:2604.05672, April 2026) — MUST CITE as concurrent work; applies per-observation Inter-Layer Truncated Flow Matching with early exit for VLA backbone computation, achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION: A₁ targets how many transformer layers to execute in a VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth routing) — orthogonal efficiency axes on different model families (VLAs vs WAMs).",
    "VADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) — adapts ACTION diffusion denoising steps per task stage (shorter for simple, longer for complex); evaluated on Push-T, Adroit, ARX5; DIFFERENTIATION: VADF targets action denoising steps, CDR targets video backbone denoising depth (τ_v) — orthogonal efficiency axes, combinable",
    "Video Models Reason Early: Exploiting Plan Commitment for Maze Solving (arXiv:2603.30043) — 2D commitment motivation: video diffusion commits high-level plan in first few denoising steps; CDR extends and empirically validates for 3D manipulation video backbones",
    "DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control (arXiv:2603.10448) — fixed-step baseline; ablation confirms single-step (high τ_v) is best on average — independently corroborates mimic-video's main-text finding that τ_v=1 is best fixed-global on SIMPLER-Bridge, providing a second source supporting CDR's pre-registered P1 prediction; 98.6% LIBERO, 50.8% RoboCasa",
    "DreamZero: World Action Models are Zero-shot Policies (arXiv:2602.15922, Feb 2026) — velocity caching within denoising trajectory; complementary to CDR (reduces cost within a fixed τ_v level vs. CDR selecting τ_v level before denoising begins)",
    "Denoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) — introduces Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions advance denoising earlier, harder regions receive more steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory frames — which frames need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined. Cited as feasibility motivation only; evaluates image generation, not robot action models.",
    "MotuBrain (arXiv:2604.27792) — unified VAM with Mixture-of-Transformers (MoT) architecture under UniDiffuser formulation; supports policy learning, world modeling, video generation, inverse dynamics; 95.8%+ on RoboTwin 2.0; 50× speedup via step reduction, FP8 quantization. DIFFERENTIATION: training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on frozen mimic-video checkpoint requiring no retraining. Orthogonal — MotuBrain could serve as future CDR base model.",
    "D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning (arXiv:2508.06804) — adapts ACTION (not video) denoising steps via RL; orthogonal efficiency axis to CDR",
    "S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight (arXiv:2603.16195, Mar 2026) — distillation-based efficiency; requires retraining",
    "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (arXiv:2604.26694) — X-WAM; fixed-distribution ANS baseline; not per-observation adaptive",
    "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (arXiv:2504.02792) — UWM; fixed schedule baseline",
    "Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv:2605.00078) — distillation-based; different efficiency axis; 99.2% LIBERO, 62.1% RoboCasa",
    "When to Trust Imagination: Adaptive Action Execution for World Action Models (arXiv:2605.06222) — episode-level replanning reduction; orthogonal to per-call CDR"
  ],
  "description": "Commitment Depth Routing (CDR) addresses selective video activation in Video-Action Models — providing the first empirical characterization of which 3D manipulation phases require video denoising below the confirmed best fixed-global τ_v=1, and learning a zero-shot router to approximate the per-task oracle τ_v without expensive offline sweeps.\n\nThe paper's theoretical foundation rests on a precise reconciliation of two mimic-video findings that prior versions of this idea conflated: (1) mimic-video's main text (Section V-C) states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1' — establishing τ_v=1 as the best fixed-global τ_v, which CDR adopts as its default; (2) mimic-video's Figure 5 caption states 'Performance peaks at an intermediate noise level' — referring to the oracle per-task view where τ_v is selected independently per task. These are compatible: τ_v=1 wins when one fixed value is applied globally (main text), but the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption). The +9.4pp per-task sweep gain (46.9%→56.3% on SIMPLER-Bridge) quantifies the gap. CDR's router closes this gap without the 10-rollout per-task sweep cost.\n\nCDR pre-registers two predictions before Phase 3 experiments: (P1) LingBot-VA-style fixed τ_v<1 baselines underperform τ_v=1 on SIMPLER-Bridge — strongly supported by mimic-video's main text and corroborated by DiT4DiT's ablation (single-step/high-τ_v is best on average). If P1 is confirmed, the competitive landscape simplifies: CDR's Pareto claim is cleanly against τ_v=1 alone — 'τ_v=1 is the best fixed-global; CDR beats it by routing per-task/per-observation to the intermediate τ_v that the oracle requires.' (P2) Per-task CDR zero-shot router recovers ≥80% of the +9.4pp sweep gap on SIMPLER-Bridge.\n\nThe paper's primary empirical contribution is Phase 1: the first systematic study of τ_v* (per-observation optimal denoising depth) across LIBERO-100 with manipulation-phase breakdown. The router (Phase 2, two-layer MLP on CLIP+language embeddings) is the deployment mechanism enabling zero-shot generalization, not the central novelty. Phase 3 reports Pareto curves on SIMPLER-Bridge anchored at the τ_v=1 fixed-global point, with LIBERO-100 results secondarily.\n\nThe paper explicitly frames: OA-WAM (arXiv:2605.06481) evaluates on the same four WidowX Bridge tasks (79.3% vs CDR base 46.9%); the gap reflects base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not CDR's routing contribution. CDR's Pareto claims are within the mimic-video architecture family. Target: CoRL 2026 (May 29); ICLR 2027 fallback.",
  "project_name": "commit_depth_router",
  "source": "web_research"
}

## Reviewer feedback (round 7)
Issues: ["MODERATE — DiT4DiT ablation is factually mischaracterized: Independent verification of arXiv:2603.10448 confirms that DiT4DiT's 'single-step is best' ablation (Figure 8b) concerns ACTION DENOISING STEPS (fewer action diffusion steps yield higher success), not τ_v (video noise level). CDR's landscape states: 'DiT4DiT ablation: single-step (high τ_v) is best on average — independently confirms the high-τ_v regime is a strong global default, corroborating mimic-video's main-text finding.' This conflates two different efficiency axes (action denoising steps vs. video noise level). Reviewers familiar with DiT4DiT will flag this. Fix: either remove DiT4DiT as corroborating evidence for τ_v=1 optimality, or rewrite as 'DiT4DiT finds that fewer action denoising steps improve performance — a parallel finding that the high-noise, low-denoising regime is preferable, supporting CDR's premise that less denoising is often better.' Do NOT use DiT4DiT to directly corroborate mimic-video's τ_v=1 result.", "MODERATE — Pareto efficiency claim is potentially misleading if P1 is confirmed: If P1 is confirmed (fixed intermediate τ_v < 1 uniformly underperforms τ_v=1 on SIMPLER-Bridge), then CDR's router will route the vast majority of frames to τ_v=1 (since τ_v=1 is the best single fixed value). The resulting 'compute savings' from CDR — measured as reduction in mean τ_v consumed below 1 — will be small (perhaps 5–10% of full video generation cost). The Pareto win is primarily in task SUCCESS (+≥7.5pp from zero-shot per-task routing), not in compute efficiency. The paper's abstract and intro must be honest about this: 'CDR's Pareto dominance is primarily measured in task success recovery, not compute savings, if the pre-registered P1 prediction is confirmed. The mean τ_v consumed by CDR remains close to 1 when P1 holds.' Misrepresenting the Pareto win as efficiency-driven when most frames route to τ_v=1 will trigger reviewer pushback.", "MODERATE — Auto-mode resource estimate (410 H100-hours) exceeds the ≤200 H100-hour budget constraint stated in user requirements. The manual estimate (115–135H) is within budget, but auto mode at 410H is 2-3× over the stated limit. Either: (a) cap the auto-mode scope to fit within 200H by dropping full RoboCasa, per-phase heatmap ablations, and the full λ×θ grid search; or (b) explicitly acknowledge in the proposal that auto-mode exceeds the 200H constraint and requires expanded budget authorization.", "MINOR — 'When to Trust Imagination' (arXiv:2605.06222) is misdescribed as 'reduces replanning frequency'; verified content shows it uses a per-action-chunk adaptive horizon mechanism with a fixed threshold τ=0.5 to decide when to replan after partial action execution — not episode-level replanning reduction. The orthogonality claim holds, but the description should be corrected to 'per-chunk adaptive replanning trigger' to avoid misleading reviewers.", "MINOR — Method contribution is architecturally thin for CoRL 2026's WAM track: The 2-layer MLP router (512-dim CLIP + 512-dim language → 256-dim hidden → 4-class softmax) is not a novel architecture. CoRL 2026's WAM submissions include DiT4DiT, MotuBrain, OA-WAM with substantial architectural innovation. CDR must foreground Phase 1 (first empirical characterization of manipulation-phase τ_v requirements) as the primary scientific contribution — the router is the deployment mechanism, not the contribution. The paper title 'Commitment Depth Routing' implies a routing method is the contribution; consider retitling to reflect the empirical study: e.g., 'When Do World Action Models Need Video? A Manipulation-Phase Study with Selective Denoising Activation.'"]
Feedback: CDR has fixed all prior critical issues through Round 6. The Round 7 proposal is now scientifically well-structured with explicit gates, correct mimic-video Figure 5 reconciliation, pre-registered predictions, and MVS fallback. Three focused fixes are required before CoRL submission:

**Fix 1 (required, 30 minutes): Correct DiT4DiT characterization.** DiT4DiT's ablation (Figure 8b in arXiv:2603.10448) is about action denoising steps — not τ_v (video noise level). CDR incorrectly uses it to corroborate 'high τ_v is best on SIMPLER-Bridge.' Rewrite as: 'DiT4DiT finds that a single action denoising step outperforms multi-step action diffusion — a parallel finding that less denoising in the action domain also improves performance; we observe the same pattern in the video domain with mimic-video's τ_v=1 result.' Remove any language claiming DiT4DiT 'independently confirms' that high video noise τ_v is optimal.

**Fix 2 (required, 20 minutes): Honestly bound the Pareto efficiency claim.** If P1 is confirmed (the expected outcome based on mimic-video main text), CDR routes most frames to τ_v=1, making compute savings modest. Add explicit language in the abstract and intro: 'CDR's primary Pareto benefit is task success recovery (≥7.5pp zero-shot on SIMPLER-Bridge), not compute efficiency — most frames continue to use τ_v=1, with video activation selectively applied only to frames where the Phase 1 study identifies τ_v* < 1.' This prevents reviewers from expecting large speedups and finding only 5-10% compute savings.

**Fix 3 (budget reconciliation, 10 minutes): Cap auto-mode estimate.** The auto mode at 410 H100-hours violates the ≤200H project constraint. Either (a) reduce auto-mode scope to 150-180H (drop RoboCasa, full hyperparameter grid) while keeping the key SIMPLER-Bridge experiments, or (b) add a note that auto-mode exceeds the budget constraint and requires pre-authorization. The manual mode (115-135H) is within budget and should be the reference for the 200H limit.

**Optional (strengthens paper): Retitle to foreground empirical contribution.** 'Commitment Depth Routing' implies a novel routing mechanism as the primary contribution. The actual primary contribution is Phase 1 — the first empirical study of which manipulation phases need τ_v < 1 in 3D WAMs. A title like 'When Does Robot Policy Need Video? Manipulation-Phase Analysis and Selective Activation for World Action Models' better positions the paper as an empirical methods contribution and reduces reviewer expectations of architectural novelty.

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
这个 idea 已经经过 7 轮修订，近 3 轮的平均分从 3.5 到 3.2，没有明显改善。

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
  "promptId": "96f00f33-f18a-4d33-9c85-730581b03df2",
  "type": "user",
  "uuid": "75dafa07-fed6-46b1-ab84-342daf61aad2",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T09:21:05.219Z_

```json
{
  "parentUuid": "75dafa07-fed6-46b1-ab84-342daf61aad2",
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
  "uuid": "7283ec9d-2940-4de8-afc5-2d667205464f",
  "timestamp": "2026-05-10T09:21:05.219Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T09:21:05.219Z_

```json
{
  "parentUuid": "7283ec9d-2940-4de8-afc5-2d667205464f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c9da39f5-d407-44fe-862f-0f423311010f",
  "timestamp": "2026-05-10T09:21:05.219Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Commitment Depth Routing: Selective Video Activation in Video-Action M…",
  "leafUuid": "c9da39f5-d407-44fe-862f-0f423311010f",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze video activation in robot policy learning",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c"
}
```

---

### Assistant

_source line 8 · 2026-05-10T09:23:18.079Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this research idea and the reviewer feedback to decide on the best course of action.

**Current Situation:**
- Round 7 of revisions
- 3 recent rounds averaging 3.5 to 3.2 (declining)
- The reviewer has flagged 3 moderate issues and 2 minor issues

**Reviewer Issues:**
1. **MODERATE** - DiT4DiT ablation mischaracterized: The "single-step is best" finding is about ACTION denoising steps, not τ_v (video noise level). Fix: rewrite or remove this as corroborating evidence.


2. **MODERATE** - The Pareto efficiency claim needs recalibration. If fixed τ_v < 1 underperforms τ_v=1, then CDR routes most frames there anyway, which means the compute savings are marginal at best (5-10%). The real win here is the task performance improvement of 7.5 percentage points, not efficiency gains—I need to be upfront about that distinction.
3. **MODERATE** - The auto-mode resource estimate at 410H blows past the ≤200H budget constraint, so I either need to cap it at 150-180H or explicitly flag that it requires pre-authorization.
4. **MINOR** - The "When to Trust Imagination" description is inaccurate and needs fixing.
5. **MINOR** - (incomplete)

The router itself is just a shallow 2-layer MLP, which is architecturally thin for a competitive venue like CoRL's WAM track. The empirical study in Phase 1 is really where the substance lies, but I'm concerned the core contribution—recovering 7.5pp of the 9.4pp gap zero-shot—is modest, especially if the routing mechanism ends up defaulting to τ_v=1 most of the time, making the routing contribution conceptually lightweight.

The Pareto framing feels misleading too. If Phase 1 confirms what mimic-video already suggests (that τ_v=1 is optimal fixed-globally), then CDR's "dominance" is just automated per-task τ_v selection with minimal compute savings, since 90%+ of frames still use full activation. The real novelty might actually be the zero-shot prediction capability—using CLIP embeddings to infer the best per-task τ_v without offline sweeps.

But that's a thin contribution for a top venue. I'm wondering if I should pivot entirely. One direction is reframing this as a pure empirical study on when world action models need video, skipping the router altogether. Or I could push toward something with genuine efficiency gains—maybe adaptive early stopping within video denoising trajectories rather than just binary τ_v selection.

Another angle is uncertainty-based video activation: only generate video when the policy is uncertain enough, which could save compute by skipping frames entirely instead of just adjusting τ_v. The last option is accepting the router's simplicity and positioning the paper around the empirical characterization itself—the surprising findings about τ_v* across tasks—with the router as a practical demonstration rather than the main contribution.

Looking at what's actually addressable right now, three moderate issues are fixable without major restructuring: removing the DiT4DiT claim, being honest about task success dominating the Pareto frontier, and capping auto-mode to a reasonable compute budget. But the deeper problem—that the method feels thin and the Pareto framing is misleading once Phase 1 is confirmed—suggests I should do a more substantial revision instead of patching. The real insight I want to build around is what happens to the framing if Phase 1 actually works.

If Phase 1 holds up, CDR's actual contribution is the zero-shot per-task τ_v selector plus the first empirical map of phase-level requirements in these manipulation tasks. If it doesn't, there's still some compute savings, but that's secondary. The paper should stop pretending to be about GPU efficiency and own what it actually is: a systematic empirical study of per-observation τ_v* needs in 3D manipulation, paired with a practical tool that automates the expensive per-task sweep. This is more honest about what we're delivering, makes the contribution sharper, directly addresses the misleading Pareto critique, and still reads well for CoRL.

A major revision makes more sense than a pivot here—the core finding about per-task τ_v* variation is real and grounded in the data, so the issue is really about how we frame it rather than the substance itself. I'll focus on fixing the DiT4DiT characterization, reframing the Pareto claim around task success rather than compute, repositioning the paper as empirical characterization plus deployment automation, capping the auto-mode estimate at 200H, correcting the "When to Trust Imagination" reference, and possibly strengthening the title.

Before I start writing, I should search for relevant recent work to make sure I'm not overlooking anything—particularly around DiT4DiT's actual ablations, compute efficiency approaches in world models, and zero-shot τ_v prediction methods. Once I've verified those details, I can rewrite the DiT4DiT section properly instead of claiming it independently confirms high-τ_v optimality for video denoising.

For the Pareto efficiency framing, the real story is that CDR's main wins are deployment efficiency—eliminating the 10 offline rollouts per task and replacing that sweep cost with zero-shot prediction—plus the +7.5pp task success boost on SIMPLER-Bridge. The per-inference compute savings aren't the primary benefit if mean τ_v stays near 1.0, so I need to reframe CDR around those actual contributions rather than overstating the computational gains.

I'm capping the auto-mode experiments at 150-180 hours by cutting RoboCasa, the full hyperparameter grid, and the extensive per-phase heatmap ablations. For the title, I'm considering "When Do World Action Models Need Video? Empirical Analysis and Zero-Shot Deployment of Selective Denoising Activation" to better capture what we're actually investigating.

Now I need to verify some key claims through searches—checking DiT4DiT's actual ablation findings, looking for any recent WAM papers I might have missed, and confirming what the "When to Trust Imagination" paper actually says.

For the revision, I'm planning to remove DiT4DiT as evidence for τ_v=1 optimality since I need to verify that claim, and instead add an honest statement about Pareto being task-success dominated rather than compute-efficiency dominated if P1 holds. I also need to reframe CDR's deployment value more precisely—it's really about eliminating 10 offline rollouts per new task, not GPU compute per inference. And I should clarify that even if P1 is confirmed, CDR's mean τ_v stays near 1.0 but task success improves. Finally, I need to fix the DiT4DiT description in the landscape section once I verify what it actually shows. I'm realizing the core issue: CDR's efficiency gains happen at deployment time—eliminating the need for 10 rollouts per task during calibration—rather than saving GPU cycles during inference itself. The Pareto analysis should either shift the X-axis to show deployment overhead (rollouts needed: 0 vs 10) with task success on the Y-axis, or stick with inference-time metrics but acknowledge the Y-axis improvements are modest (5-10% reduction in mean τ_v) while the real practical win is the task success boost. I think the cleanest framing focuses on the deployment-time savings and task performance gains rather than trying to claim inference-time compute benefits. The core problem stays the same—selecting τ_v per task in video mimic learning—but the framing shifts from compute efficiency to task success, and the deployment value moves from inference-time savings to calibration cost. This counts as a major revision since the Pareto characterization and method details change, though it's not a fundamental pivot. Before I write the full JSON, I should verify a couple of details: whether DiT4DiT Figure 8b is really about action denoising steps rather than τ_v, and what "When to Trust Imagination" actually says about per-chunk adaptive replacement.

The reviewer's already confirmed both, so I'll trust that and move forward with the fixes. For the landscape section, I'm reframing DiT4DiT from a τ_v ablation to a finding about action denoising steps—fewer steps outperform multi-step diffusion on task success, which is a different phenomenon than what mimic-video is studying. I'm scanning through the document structure to locate all DiT4DiT references and verify they're consistent with the corrected framing about τ_v=1 being a fixed-global baseline rather than a direct validation of video noise optimality. The entry appears in the landscape section with performance metrics, and I should check whether the core_problem, opportunity, and approach sections need updates to align with this distinction. I need to remove the DiT4DiT corroboration claim and rely solely on mimic-video's main text as evidence for P1. For the Pareto framing, I'm clarifying that CDR's primary benefit when P1 holds is task success recovery rather than compute savings, since most frames route to τ_v=1 anyway, keeping mean τ_v close to 1.0.

The real deployment efficiency gain comes from eliminating the 10-rollout calibration sweep per task at deployment time, not reducing per-inference GPU compute—this distinction needs to be explicit in the abstract and introduction. Now I'm revising the auto-mode budget estimate downward to 150–175 H100-hours, breaking down the phases more precisely. Updating the JSON with the revised title to better reflect that Phase 1 analysis is the main contribution and positioning this as an empirical methods paper rather than an architecture paper. The core finding holds—fixed global τ_v=1 works best in the baseline, but per-task sweeps show gains—so the work is worth pursuing with these structural changes to set clearer expectations. Generating the paper metadata... I'm going through the document systematically now—updating the title to emphasize the empirical study, removing the false DiT4DiT τ_v claim, and reframing the Pareto analysis to honestly distinguish between task success recovery and per-inference compute savings. I'm also fixing the resource estimate to cap GPU hours at 200 and correcting the landscape descriptions for both DiT4DiT and the adaptive replanning work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9da39f5-d407-44fe-862f-0f423311010f",
  "isSidechain": false,
  "requestId": "req_011CateBtjYXPSxfuZDzvafW",
  "type": "assistant",
  "uuid": "10096866-ee07-408f-ad58-b411cf882f42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AYBszTegBcd3qCgTDSwagy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21923,
      "cache_read_input_tokens": 11631,
      "output_tokens": 6380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6380,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 21923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21923
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

_source line 9 · 2026-05-10T09:23:18.082Z_

I'll research the specific papers flagged by reviewers before revising, then apply targeted fixes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10096866-ee07-408f-ad58-b411cf882f42",
  "isSidechain": false,
  "requestId": "req_011CateBtjYXPSxfuZDzvafW",
  "type": "assistant",
  "uuid": "3697e617-6ee7-4663-a245-27e33216aa1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AYBszTegBcd3qCgTDSwagy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21923,
      "cache_read_input_tokens": 11631,
      "output_tokens": 6380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6380,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 21923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21923
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

_source line 10 · 2026-05-10T09:23:22.727Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BXLRobcYLSBSLnnti8n3H5`</summary>

```json
{
  "description": "Verify DiT4DiT and \"When to Trust Imagination\" paper content",
  "subagent_type": "Explore",
  "prompt": "Fetch the following two arXiv abstracts and return the key relevant content:\n\n1. arXiv:2603.10448 (DiT4DiT) — I need to understand what Figure 8b / the ablation study actually tests. Specifically: does the \"single-step is best\" result refer to (a) action denoising steps, (b) video noise level τ_v, or (c) something else? Fetch https://arxiv.org/abs/2603.10448 and read the abstract and any available method/experiment description.\n\n2. arXiv:2605.06222 (\"When to Trust Imagination\") — I need to understand the mechanism. The reviewer says it uses \"per-action-chunk adaptive horizon mechanism with a fixed threshold τ=0.5 to decide when to replan after partial action execution.\" Fetch https://arxiv.org/abs/2605.06222 and confirm the mechanism description.\n\nReturn the relevant excerpts for each paper, focusing on the ablation/mechanism descriptions. Keep response under 400 words total."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3697e617-6ee7-4663-a245-27e33216aa1e",
  "isSidechain": false,
  "requestId": "req_011CateBtjYXPSxfuZDzvafW",
  "type": "assistant",
  "uuid": "6b431482-1ec1-4639-84c0-9d5f73f2d205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AYBszTegBcd3qCgTDSwagy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21923,
      "cache_read_input_tokens": 11631,
      "output_tokens": 6380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6380,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 21923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21923
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Commitment Depth Routing: Selective Video Activation in Video-Action M…",
  "leafUuid": "6b431482-1ec1-4639-84c0-9d5f73f2d205",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze video activation in robot policy learning",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c"
}
```

---

### Tool result

_source line 13 · 2026-05-10T09:23:40.946Z_

<details><summary>↩ Tool result · `toolu_01BXLRobcYLSBSLnnti8n3H5`</summary>

```text
**Summary of Findings:**

Unfortunately, the WebFetch tool cannot extract the detailed technical content from these PDFs with sufficient clarity. Here's what I was able to determine:

**arXiv:2603.10448 (DiT4DiT):**
- The paper is titled "DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control"
- Figure 8b and its ablation study details are not accessible through the PDF extraction
- You'll need to access the full PDF directly to see whether the ablation tests action denoising steps, video noise level τ_v, or another parameter

**arXiv:2605.06222 (When to Trust Imagination):**
- The paper implements an adaptive mechanism for deciding when to replan
- Uses a "Future Forward Dynamics Causal Attention (FFDC)" verifier that evaluates prediction reliability
- The mechanism appears threshold-based (deciding when to trust imagined vs. real observations)
- The specific τ=0.5 threshold value and "per-action-chunk adaptive horizon" details are not confirmed in the extracted content

**Recommendation:** Download the PDFs directly from arXiv. The abstracts and searchable text don't contain the specific ablation/mechanism details you need. The full papers will have the necessary figures, method sections, and experimental details to answer your questions definitively.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b431482-1ec1-4639-84c0-9d5f73f2d205",
  "isSidechain": false,
  "promptId": "96f00f33-f18a-4d33-9c85-730581b03df2",
  "type": "user",
  "uuid": "7d8746cd-d23b-4c67-ba86-e97c7b38312b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Fetch the following two arXiv abstracts and return the key relevant content:\n\n1. arXiv:2603.10448 (DiT4DiT) — I need to understand what Figure 8b / the ablation study actually tests. Specifically: does the \"single-step is best\" result refer to (a) action denoising steps, (b) video noise level τ_v, or (c) something else? Fetch https://arxiv.org/abs/2603.10448 and read the abstract and any available method/experiment description.\n\n2. arXiv:2605.06222 (\"When to Trust Imagination\") — I need to understand the mechanism. The reviewer says it uses \"per-action-chunk adaptive horizon mechanism with a fixed threshold τ=0.5 to decide when to replan after partial action execution.\" Fetch https://arxiv.org/abs/2605.06222 and confirm the mechanism description.\n\nReturn the relevant excerpts for each paper, focusing on the ablation/mechanism descriptions. Keep response under 400 words total.",
    "agentId": "acdadcf07a0cbe458",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "**Summary of Findings:**\n\nUnfortunately, the WebFetch tool cannot extract the detailed technical content from these PDFs with sufficient clarity. Here's what I was able to determine:\n\n**arXiv:2603.10448 (DiT4DiT):**\n- The paper is titled \"DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control\"\n- Figure 8b and its ablation study details are not accessible through the PDF extraction\n- You'll need to access the full PDF directly to see whether the ablation tests action denoising steps, video noise level τ_v, or another parameter\n\n**arXiv:2605.06222 (When to Trust Imagination):**\n- The paper implements an adaptive mechanism for deciding when to replan\n- Uses a \"Future Forward Dynamics Causal Attention (FFDC)\" verifier that evaluates prediction reliability\n- The mechanism appears threshold-based (deciding when to trust imagined vs. real observations)\n- The specific τ=0.5 threshold value and \"per-action-chunk adaptive horizon\" details are not confirmed in the extracted content\n\n**Recommendation:** Download the PDFs directly from arXiv. The abstracts and searchable text don't contain the specific ablation/mechanism details you need. The full papers will have the necessary figures, method sections, and experimental details to answer your questions definitively."
      }
    ],
    "totalDurationMs": 18212,
    "totalTokens": 17000,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 868,
      "cache_read_input_tokens": 15814,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 868
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 311,
          "cache_read_input_tokens": 15814,
          "cache_creation_input_tokens": 868,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 868,
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
      "otherToolCount": 4
    }
  },
  "sourceToolAssistantUUID": "6b431482-1ec1-4639-84c0-9d5f73f2d205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T09:23:49.964Z_

<details><summary>Logged reasoning block</summary>

```text
The reviewer has already independently verified the content of both papers:
1. DiT4DiT Figure 8b: "action denoising steps (fewer action diffusion steps yield higher success), not τ_v (video noise level)"
2. "When to Trust Imagination": "per-action-chunk adaptive horizon mechanism with a fixed threshold τ=0.5 to decide when to replan after partial action execution"

I'll trust the reviewer's verification since they explicitly stated "Independent verification of arXiv:2603.10448 confirms" for DiT4DiT.

Now let me proceed with writing the full revised JSON. The changes I'll make:


1. **Title**: Change to foreground empirical study
2. **DiT4DiT**: Fix across landscape, approach, key_references - remove false τ_v corroboration
3. **Pareto framing**: Add honest language about task-success vs. compute-efficiency distinction when P1 confirmed
4. **Auto-mode budget**: Cap to ≤200H
5. **"When to Trust Imagination"**: Fix description
6. **Deployment value**: Reframe from "inference-time compute savings" to "deployment-time calibration savings"

Writing the complete JSON now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d8746cd-d23b-4c67-ba86-e97c7b38312b",
  "isSidechain": false,
  "requestId": "req_011CatePNHZ93Fgy4ELxcnX8",
  "type": "assistant",
  "uuid": "6a1be3dd-9617-49bc-bb65-16fad69ab30a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PXUFc8BK29zSvgYz49fyp7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6687,
      "cache_read_input_tokens": 33554,
      "output_tokens": 662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 662,
          "cache_read_input_tokens": 33554,
          "cache_creation_input_tokens": 6687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6687
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

_source line 15 · 2026-05-10T09:23:50.221Z_

The reviewer's verification is authoritative. Now I'll write the full revised JSON with all targeted fixes plus the reframing needed to break the stagnation pattern.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a1be3dd-9617-49bc-bb65-16fad69ab30a",
  "isSidechain": false,
  "requestId": "req_011CatePNHZ93Fgy4ELxcnX8",
  "type": "assistant",
  "uuid": "3de693c7-0575-4d20-af34-854762376997",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PXUFc8BK29zSvgYz49fyp7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6687,
      "cache_read_input_tokens": 33554,
      "output_tokens": 662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 662,
          "cache_read_input_tokens": 33554,
          "cache_creation_input_tokens": 6687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6687
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

_source line 16 · 2026-05-10T09:24:00.135Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01QyByXXpSg4LNn5ai3cP5DQ`</summary>

```json
{
  "description": "Search for recent WAM efficiency papers May 2026",
  "subagent_type": "Explore",
  "prompt": "Search for any new Video-Action Model (WAM) or World Action Model efficiency papers from April-May 2026 that I might be missing. Specifically:\n\n1. Search arXiv for \"video action model denoising efficiency 2026\" \n2. Search for \"world action model τ noise level routing\"\n3. Search for \"manipulation phase video generation robot policy\"\n\nI'm working on a paper about selective video denoising depth routing in VAMs (Video-Action Models like mimic-video). My key gap: mimic-video shows τ_v=1 (no video denoising) is best as a global default, but per-task optimal τ_v averages at intermediate levels (+9.4pp gain). I want to know if any new paper has already proposed zero-shot per-task τ_v selection or adaptive video denoising depth in WAMs.\n\nUse WebSearch to check. Return paper titles, arXiv IDs, and a one-sentence summary of each relevant paper. Under 300 words total."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3de693c7-0575-4d20-af34-854762376997",
  "isSidechain": false,
  "requestId": "req_011CatePNHZ93Fgy4ELxcnX8",
  "type": "assistant",
  "uuid": "51d9bf37-9bb4-4e12-99df-4d229019fddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PXUFc8BK29zSvgYz49fyp7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6687,
      "cache_read_input_tokens": 33554,
      "output_tokens": 662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 662,
          "cache_read_input_tokens": 33554,
          "cache_creation_input_tokens": 6687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6687
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

_source line 17 · 2026-05-10T09:24:15.573Z_

<details><summary>↩ Tool result · `toolu_01QyByXXpSg4LNn5ai3cP5DQ`</summary>

```text
Based on my search, here are the most relevant recent papers for your VAM denoising routing work:

**Highly Relevant:**

1. **"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising"** (arXiv:2604.26694) — Proposes Asynchronous Noise Sampling (ANS) to jointly optimize generation quality and action decoding efficiency, showing incomplete video denoising before action inference is viable.

2. **"MotuBrain: An Advanced World Action Model for Robot Control"** (arXiv:2604.27792) — Recent WAM advancing noise-level routing and action efficiency in world models.

3. **"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets"** (arXiv:2504.02792) — Explores decoupled noise schedules for video vs. action, with video biased toward high-noise states (routing mechanism).

**Moderately Relevant:**

4. **"Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control"** (arXiv:2506.01943) — Addresses manipulation phase video generation with policy learning.

5. **"Video Generators are Robot Policies"** (arXiv:2508.00795) — Demonstrates video generation as a fundamental policy learning approach.

**Gap Summary:** The 2604.26694 paper on asynchronous denoising is your closest match, but it focuses on hardware-level efficiency rather than *per-task adaptive τ_v selection*. The 2504.02792 paper explores video/action noise decoupling but doesn't propose zero-shot per-task τ_v routing. Your selective denoising depth routing contribution appears novel—no papers yet propose learnable per-task optimal τ_v selection in VAMs.

Sources:
- [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/html/2604.26694v2)
- [MotuBrain: An Advanced World Action Model for Robot Control](https://arxiv.org/html/2604.27792v2)
- [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](https://arxiv.org/html/2504.02792v1)
- [Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control](https://arxiv.org/html/2506.01943v3)
- [Video Generators are Robot Policies](https://arxiv.org/html/2508.00795v1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51d9bf37-9bb4-4e12-99df-4d229019fddb",
  "isSidechain": false,
  "promptId": "96f00f33-f18a-4d33-9c85-730581b03df2",
  "type": "user",
  "uuid": "22b9e16b-e1f8-4a43-9051-c8d656dcc2ce",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for any new Video-Action Model (WAM) or World Action Model efficiency papers from April-May 2026 that I might be missing. Specifically:\n\n1. Search arXiv for \"video action model denoising efficiency 2026\" \n2. Search for \"world action model τ noise level routing\"\n3. Search for \"manipulation phase video generation robot policy\"\n\nI'm working on a paper about selective video denoising depth routing in VAMs (Video-Action Models like mimic-video). My key gap: mimic-video shows τ_v=1 (no video denoising) is best as a global default, but per-task optimal τ_v averages at intermediate levels (+9.4pp gain). I want to know if any new paper has already proposed zero-shot per-task τ_v selection or adaptive video denoising depth in WAMs.\n\nUse WebSearch to check. Return paper titles, arXiv IDs, and a one-sentence summary of each relevant paper. Under 300 words total.",
    "agentId": "aba15aa0d1fce64ee",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my search, here are the most relevant recent papers for your VAM denoising routing work:\n\n**Highly Relevant:**\n\n1. **\"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising\"** (arXiv:2604.26694) — Proposes Asynchronous Noise Sampling (ANS) to jointly optimize generation quality and action decoding efficiency, showing incomplete video denoising before action inference is viable.\n\n2. **\"MotuBrain: An Advanced World Action Model for Robot Control\"** (arXiv:2604.27792) — Recent WAM advancing noise-level routing and action efficiency in world models.\n\n3. **\"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets\"** (arXiv:2504.02792) — Explores decoupled noise schedules for video vs. action, with video biased toward high-noise states (routing mechanism).\n\n**Moderately Relevant:**\n\n4. **\"Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control\"** (arXiv:2506.01943) — Addresses manipulation phase video generation with policy learning.\n\n5. **\"Video Generators are Robot Policies\"** (arXiv:2508.00795) — Demonstrates video generation as a fundamental policy learning approach.\n\n**Gap Summary:** The 2604.26694 paper on asynchronous denoising is your closest match, but it focuses on hardware-level efficiency rather than *per-task adaptive τ_v selection*. The 2504.02792 paper explores video/action noise decoupling but doesn't propose zero-shot per-task τ_v routing. Your selective denoising depth routing contribution appears novel—no papers yet propose learnable per-task optimal τ_v selection in VAMs.\n\nSources:\n- [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/html/2604.26694v2)\n- [MotuBrain: An Advanced World Action Model for Robot Control](https://arxiv.org/html/2604.27792v2)\n- [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](https://arxiv.org/html/2504.02792v1)\n- [Learning Video Generation for Robotic Manipulation with Collaborative Trajectory Control](https://arxiv.org/html/2506.01943v3)\n- [Video Generators are Robot Policies](https://arxiv.org/html/2508.00795v1)"
      }
    ],
    "totalDurationMs": 15411,
    "totalTokens": 18640,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 1678,
      "cache_creation_input_tokens": 1889,
      "cache_read_input_tokens": 14450,
      "output_tokens": 623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1889
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1678,
          "output_tokens": 623,
          "cache_read_input_tokens": 14450,
          "cache_creation_input_tokens": 1889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1889,
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
      "otherToolCount": 3
    }
  },
  "sourceToolAssistantUUID": "51d9bf37-9bb4-4e12-99df-4d229019fddb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T09:24:36.484Z_

<details><summary>Logged reasoning block</summary>

```text
Good. The search confirms no existing paper proposes learnable per-task optimal τ_v selection in WAMs. The gap is still novel.

Now let me write the full revised JSON. The key changes:

1. **Title**: "When Do World Action Models Need Video? Manipulation-Phase Analysis and Zero-Shot Selective Denoising Activation" — foregrounds empirical study

2. **DiT4DiT fix** everywhere:
   - In landscape: Remove "independently confirms the high-τ_v regime is a strong global default, corroborating mimic-video's main-text finding"
   - Replace with: "DiT4DiT's ablation shows that fewer action denoising steps improve task success — this is about action diffusion efficiency, not video noise level. CDR treats this as a structural parallel: both action and video domains benefit from reduced denoising as a global default, but they're independent efficiency levers."
   - In approach Phase 3 P1: Remove DiT4DiT as corroborating source for P1
   - In key_references: Correct the DiT4DiT citation details

Now I need to clarify the Pareto framing — CDR's main win is task success recovery of at least 7.5 percentage points in zero-shot mode, not computational savings per inference. The efficiency actually comes from eliminating the calibration sweep entirely, going from 10 rollouts down to zero through zero-shot prediction. I should make sure the abstract and introduction emphasize this deployment-time benefit clearly to set proper expectations.

For the auto-mode budget, I'm capping the compute at around 150-175 hours instead of 410, which means dropping RoboCasa and scaling back the hyperparameter grid to just a few key combinations rather than the full λ×θ sweep.

On the "When to Trust Imagination" framing, I need to shift from talking about reduced replanning frequency to describing an adaptive per-chunk mechanism where a learned threshold decides after each partial action whether to continue or replan — this is separate from CDR's per-observation routing decision.

The deployment value should be reframed to make clear that the 10 offline rollout savings happen at deployment time for each new task, not as a per-inference GPU cost reduction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22b9e16b-e1f8-4a43-9051-c8d656dcc2ce",
  "isSidechain": false,
  "requestId": "req_011CateRv7XztmfhCHeHhAF7",
  "type": "assistant",
  "uuid": "f8c39219-0d3a-42eb-933f-98f1cd130d8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019XWVUaeRGkoqekFcC8y6he",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 40241,
      "output_tokens": 16486,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16486,
          "cache_read_input_tokens": 40241,
          "cache_creation_input_tokens": 1292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1292
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

_source line 19 · 2026-05-10T09:30:41.420Z_

Good — no new papers occupy the zero-shot per-task τ_v selection gap. Now I'll write the full revised JSON with all fixes applied.

The core strategic decision here: after 7 rounds of stagnation, the right move is a **major revision** that fundamentally reframes the Pareto story (from "compute efficiency" to "deployment calibration savings + task success recovery") rather than a pivot. The empirical gap is real; the framing was dishonest about what CDR actually saves. Fixing that dishonesty sharpens the paper's identity.

```json
{
  "title": "When Do World Action Models Need Video? Manipulation-Phase Analysis and Zero-Shot Selective Denoising Activation",
  "change_type": "major",
  "core_problem": "Video-Action Models (VAMs) like mimic-video train their action decoder robust to any τ_v ∈ [0,1] via logit-normal sampling, making τ_v a flexible test-time parameter. A foundational finding from mimic-video (arXiv:2512.15692): mimic-video's main text explicitly states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5),' and τ_v=1 achieves 46.9% task success on SIMPLER-Bridge described as 'a good default value that balances policy performance and inference speed' — the compute-efficient recommended starting point. At the same time, mimic-video Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies.' These findings are reconcilable, not contradictory: the main text identifies τ_v=1 as the best FIXED-GLOBAL τ_v (if you must pick one value for all tasks uniformly), while the Figure 5 caption describes the oracle per-task view — when optimal τ_v is selected independently per task, the distribution of per-task optima peaks at intermediate noise levels. This paper exploits precisely this gap: τ_v=1 is the best fixed-global τ_v baseline, but per-task oracle routing to intermediate τ_v recovers gains that the fixed-global τ_v=1 default leaves on the table.\n\nτ_v=0 (fully denoised video) gives WORSE autonomous policy performance than intermediate τ_v values — confirmed by mimic-video — so the action-quality-optimal range excludes both extremes. The per-task τ_v sweep yields +9.4pp on SIMPLER-Bridge (46.9%→56.3%), proving SOME tasks genuinely benefit from actual video denoising (τ_v < 1) relative to the τ_v=1 fixed-global default. Fast-WAM (arXiv:2603.16666) achieves 97.6% LIBERO by skipping test-time future video generation entirely, confirming the high-τ_v regime is strong on average. The core gap is a selective video activation problem: which observations within which tasks need video denoising below τ_v=1 (i.e., below the confirmed best fixed-global), and can this be predicted zero-shot without expensive per-task offline rollouts?\n\nExisting approaches are non-adaptive: (1) LingBot-VA (RSS 2026) fixes τ_v≈0.6 uniformly — since mimic-video's main text establishes τ_v=1 as best fixed-global, this uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge; (2) Fast-WAM skips video entirely via architectural retraining — effective on average but permanently loses gains for tasks where video is genuinely critical; (3) mimic-video's per-task sweeping requires ~10 rollouts per new task at deployment time. This paper addresses the third cost: default to τ_v=1 (confirmed best fixed-global by mimic-video main text), activate video denoising (route to τ_v < 1) only when the per-task oracle justifies it, and eliminate the 10-rollout-per-task deployment calibration cost via a zero-shot router trained on LIBERO-100.\n\nCRITICAL PARETO FRAMING CLARIFICATION (required for reviewer accuracy): If the pre-registered prediction P1 is confirmed (fixed intermediate τ_v < 1 underperforms τ_v=1 on SIMPLER-Bridge — the expected outcome per mimic-video main text), then the zero-shot router routes the MAJORITY of frames to τ_v=1. This means: (a) mean τ_v consumed by CDR stays CLOSE TO 1.0; (b) per-inference GPU compute savings are SMALL (5–10% at most); (c) the primary benefit is TASK SUCCESS RECOVERY (+≥7.5pp zero-shot on SIMPLER-Bridge) and DEPLOYMENT CALIBRATION SAVINGS (10 offline rollouts per new task → 0). The abstract and introduction MUST state this explicitly. CDR's Pareto dominance vs. τ_v=1 is: same or slightly lower mean τ_v consumed, significantly higher task success — not a large speedup per inference call.\n\nNote on concurrent work and absolute performance context: OA-WAM (arXiv:2605.06481, May 2026) achieves 79.3% on the same four WidowX Bridge tasks (Spoon Towel, Carrot Plate, Stack Cube, Eggplant Basket, Visual Matching protocol) — the identical evaluation setup as SIMPLER-Bridge. The 32pp gap between OA-WAM (79.3%) and mimic-video/CDR base (46.9%) reflects base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; mimic-video: 2B Cosmos-Predict2), not routing methodology. CDR is post-hoc on a frozen mimic-video checkpoint without retraining. The related work section explicitly states this distinction to pre-empt reviewer confusion about absolute performance comparisons.",

  "opportunity": "The key enabling property is mimic-video's variable-τ_v training (logit-normal over [0,1]), which makes the action decoder capable of exploiting richer video features at lower τ_v while remaining functional at τ_v=1. This paper exploits this asymmetry: a lightweight router that defaults to τ_v=1 — the confirmed best fixed-global τ_v per mimic-video main text — and activates actual video denoising (routes to τ_v < 1) only for observations where the action decoder's output demonstrably benefits from real video structure.\n\nThe key reconciliation between mimic-video's two findings: (a) mimic-video's main text concludes τ_v=1 is the best fixed-global autonomous policy performance on SIMPLER-Bridge; (b) mimic-video's Figure 5 caption reports that performance peaks at an intermediate noise level when τ_v is optimized per-task (the oracle view). These are compatible: τ_v=1 wins when you must pick one global value, but the per-task oracle τ_v lives at intermediate levels — creating a +9.4pp gap (46.9%→56.3%) between the fixed-global default and the per-task sweep. The primary claim is closing this gap: a lightweight router approximates the per-task or per-observation oracle, recovering gains that the fixed-global τ_v=1 leaves on the table, without the 10-rollout per-task sweep cost.\n\nCRITICAL: THE DEPLOYMENT EFFICIENCY GAIN IS CALIBRATION COST, NOT PER-INFERENCE COMPUTE. When P1 is confirmed (the expected outcome), CDR routes most frames to τ_v=1, keeping mean τ_v close to 1.0. The efficiency improvement CDR delivers is: eliminating the 10-offline-rollout per-task sweep required to find the optimal fixed τ_v for a new task. A new task can be deployed with ZERO rollouts using the zero-shot router, rather than requiring 10 rollouts to calibrate the best fixed τ_v. This is a real and practically important contribution — robotics deployments accumulate many new tasks, and even at 10 rollouts each, calibration cost is significant — but it is DIFFERENT from 'faster inference per call.' The paper's framing must be explicit: 'CDR saves deployment calibration cost (10 rollouts → 0 per new task) and recovers task success (+≥7.5pp zero-shot), not primarily per-inference GPU compute.'\n\nBecause mimic-video's main text establishes τ_v=1 as best fixed-global, this paper also pre-registers the prediction that LingBot-VA-style uniform partial denoising (fixed τ_v < 1 applied uniformly) will UNDERPERFORM τ_v=1 on SIMPLER-Bridge. If confirmed, this simplifies the competitive landscape: LingBot-VA-style approaches are not valid Pareto competitors on this benchmark. The Pareto win is cleanly against τ_v=1 alone — 'we beat the best fixed-global τ_v by selectively routing only the tasks/frames that need it, without any offline rollout cost.'\n\nTwo publishable outcomes with asymmetric CoRL value: (1) If per-observation τ_v* < 1 frames concentrate in precision phases with >2pp per-phase improvement: CDR demonstrates selective video activation as a Pareto-superior alternative to the τ_v=1 fixed-global default — the router outperforms the best fixed-threshold baseline on the task-success vs. deployment-calibration-rollouts Pareto frontier on SIMPLER-Bridge. (2) If within-task per-phase variation is small (<2pp): task-level CDR router recovers ≥80% of per-task sweep gain (+7.5pp of +9.4pp) zero-shot on SIMPLER-Bridge — a concrete deployment contribution automating mimic-video's expensive per-task offline sweep via a frozen MLP trained on LIBERO-100 task embeddings. Outcome 2 must be framed with specific numerical targets (≥80% recovery) to meet CoRL bar; 'validation study alone' is insufficient.\n\nThe primary scientific contribution is Phase 1: the FIRST empirical characterization of which 3D manipulation phases require video denoising below the τ_v=1 fixed-global default, using GT-action-referenced τ_v labeling across LIBERO-100. The zero-shot router is the deployment mechanism enabling practical use of Phase 1's findings without offline sweeps — not the architectural novelty. The paper should be read as an empirical methods contribution, not an architectural one.",

  "landscape": "LingBot-VA (arXiv:2601.21998, RSS 2026, Ant Group) is the primary comparison. Noisy History Augmentation (saug ∈ [0.5,1.0] during training) enables fixed 3-step inference to s=0.6. Key distinction: LingBot-VA imposes a LOWER τ_v (more denoising) than τ_v=1 uniformly across all frames. Because mimic-video's main text establishes τ_v=1 as the best fixed-global autonomous policy performance on SIMPLER-Bridge, LingBot-VA-style uniform partial denoising is formally predicted to underperform τ_v=1 on SIMPLER-Bridge — making LingBot-VA NOT a Pareto competitor on this benchmark. CDR's Pareto claim is therefore primarily against the τ_v=1 fixed-global baseline. 98.5% LIBERO (Spatial 98.5, Object 99.6, Goal 97.2, Long 98.5), 92.2% RoboTwin. No per-phase analysis; fixed threshold assumed without verification. NOTE: Due to mimic-video's noise-as-augmentation effect and main-text confirmation that τ_v=1 is best fixed-global on SIMPLER-Bridge, there is a formal pre-registered prediction that LingBot-VA-style fixed τ_v<1 baselines will underperform τ_v=1 on SIMPLER-Bridge — see Phase 3 pre-registration.\n\nmimic-video (arXiv:2512.15692, Dec 2025) is the base model. Key findings: (a) Main text explicitly states: 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) Figure 5 caption separately states: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task; (c) RECONCILIATION: τ_v=1 wins as the best single fixed value (main text), but the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption) — this paper's contribution is approximating the per-task oracle via zero-shot routing; (d) per-task sweep yields +9.4pp (46.9%→56.3%), confirming the gap between fixed-global τ_v=1 and per-task oracle; (e) τ_v=0 gives WORSE performance than intermediate τ_v — the sweep range excludes τ_v=0. Note: mimic-video Table I does NOT enumerate fixed-global-τ_v comparisons (τ_v=0.5 vs 0.7 vs 0.9 vs 1.0) — Phase 3 baselines will be the first such systematic comparison on SIMPLER-Bridge. 93.9% LIBERO, 46.9%/56.3% SIMPLER-Bridge.\n\nFast-WAM (arXiv:2603.16666, Mar 2026) removes test-time future video prediction by processing only the first clean observation frame — architecturally different from τ_v=1 (which passes noisy future frames through the full backbone). 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. Important: Fast-WAM does NOT evaluate on SIMPLER-Bridge (results reported only on LIBERO and RoboTwin) — there is no Fast-WAM SIMPLER-Bridge number to compare against. CDR is post-hoc (no backbone retraining) and occupies the selective middle: defer to Fast-WAM-style efficiency (τ_v=1) by default, activate actual video generation for precision-critical frames. On SIMPLER-Bridge, CDR's baseline (a) τ_v=1 serves as the closest achievable proxy for Fast-WAM's test-time behavior on the mimic-video backbone.\n\nOA-WAM (arXiv:2605.06481, May 2026, Ding et al., IMPORTANT — MUST CITE) evaluates on LIBERO (97.8%) and SimplerEnv WidowX Bridge Visual Matching (79.3% average across Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%). CRITICAL: OA-WAM's 'SimplerEnv 79.3%' and CDR's 'SIMPLER-Bridge 46.9%' are the SAME four-task evaluation setup (identical task set and Visual Matching protocol). The 32pp performance gap reflects base model architecture and scale, not routing methodology: OA-WAM uses a 7B Chameleon-style trunk with slot-based object addressing and per-episode address vectors; CDR is post-hoc on mimic-video's 2B Cosmos-Predict2 backbone without retraining. DIFFERENTIATION from CDR: OA-WAM addresses object identity robustness in WAMs via scene decomposition into object slots — orthogonal to CDR's τ_v routing. OA-WAM requires full architectural retraining; CDR introduces no new training. Paper framing must state explicitly in related work and experimental sections: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks (Visual Matching); the performance gap is attributable to base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not the routing method CDR introduces. CDR's Pareto claims are within the mimic-video architecture family.'\n\nVADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) adapts ACTION diffusion denoising steps per task stage via a Hierarchical Vision Task Segmenter — orthogonal to CDR. VADF modifies the action diffusion process (fewer steps for simple actions, more for complex); CDR modifies the VIDEO backbone denoising depth (τ_v). These address different computational bottlenecks and can be combined. VADF is evaluated on simpler manipulation setups (Push-T, Adroit, ARX5); CDR targets WAM-class models on SIMPLER-Bridge and LIBERO-100.\n\nA₁ (arXiv:2604.05672, April 2026, MUST CITE as concurrent work) introduces per-observation inter-layer early exit via Inter-Layer Truncated Flow Matching for VLAs — achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION from CDR: A₁ targets how many transformer layers to compute in the VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth). These are orthogonal efficiency axes on different model families (VLAs vs WAMs). One-sentence cite in CDR related work: 'Concurrent work A₁ (arXiv:2604.05672) applies per-observation inter-layer early exit to VLA backbone computation; CDR applies per-observation τ_v routing to the video backbone in WAMs — orthogonal efficiency axes targeting different model families.'\n\nDiT4DiT (arXiv:2603.10448) ablation (Figure 8b): fewer ACTION denoising steps yield higher task success — this finding concerns the action diffusion process, NOT τ_v (video noise level). These are orthogonal efficiency axes. CDR cites DiT4DiT only as a structural analogy: in both the action domain (DiT4DiT) and the video domain (mimic-video τ_v=1 main-text finding), less denoising tends to be preferable as a global default. CDR does NOT use DiT4DiT to corroborate τ_v=1 video noise optimality; these are different axes and conflating them would be factually incorrect. 98.6% LIBERO, 50.8% RoboCasa. DreamZero (arXiv:2602.15922, Feb 2026, 14B WAM) caches velocity within a denoising trajectory; complementary to CDR (reduces cost within given τ_v level vs. CDR choosing the τ_v level). ChEaP (arXiv:2603.30043) establishes early plan commitment in 2D mazes (first few denoising steps commit high-level motion; further steps add visual detail only); CDR empirically validates and extends this to 3D manipulation video backbones.\n\nDenoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) introduces the Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions complete denoising earlier while harder regions receive more denoising steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory timesteps — which frames in a manipulation episode need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined (spatial patch routing within each CDR-selected frame). Note: this paper is about image generation, not robot action models, and is cited as feasibility motivation only.\n\nMotuBrain (arXiv:2604.27792) is a unified VAM with Mixture-of-Transformers (MoT) architecture under a UniDiffuser formulation, supporting policy learning, world modeling, video generation, and inverse dynamics. Achieves 95.8%+ on RoboTwin 2.0 under clean and randomized settings with 50× speedup via step reduction, compilation, and FP8 quantization. DIFFERENTIATION from CDR: MotuBrain is a training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on a frozen mimic-video checkpoint requiring no backbone retraining. These are complementary — MotuBrain could serve as a future CDR base model if it supports variable-τ_v inference. Reviewers may mention MotuBrain as related work; distinguish on training-time architecture vs. test-time routing.\n\nD3P (arXiv:2508.06804) adapts ACTION denoising steps via RL — complementary efficiency axis (same as VADF, different mechanism). X-WAM (arXiv:2604.26694) uses Asynchronous Noise Sampling from a fixed joint distribution — not per-observation adaptive. UWM (arXiv:2504.02792) uses independent modality timesteps from fixed schedule. Being-H0.7 (arXiv:2605.00078) avoids pixel decoding via distillation. S-VAM (arXiv:2603.16195) distills multi-step to one-step; requires retraining. 'When to Trust Imagination' (arXiv:2605.06222) introduces a per-action-chunk adaptive replanning trigger: after each partial action execution, a learned threshold (τ=0.5) decides whether to continue executing the current plan or replan based on prediction reliability — orthogonal to CDR's per-observation τ_v routing.\n\nNo existing VAM paper: (a) uses GT-action-referenced τ_v labeling; (b) provides the first empirical characterization of which 3D manipulation phases need τ_v < 1 below the confirmed best fixed-global τ_v=1; or (c) trains a zero-shot per-task/per-observation τ_v predictor that generalizes across tasks without offline rollouts.",

  "approach": "CDR has four sequenced phases relative to a deployed mimic-video checkpoint (no backbone retraining required):\n\n**Phase 0 — Sanity Check + Preliminary Zero-Shot Validation (1–3 H100-hours, PREREQUISITE, run immediately):**\nTake 5 LIBERO tasks spanning types (2 precision grasp/insert, 2 pick-and-place, 1 long-horizon). Run 3 demonstration trajectories each (~1,500 frames total). Sweep τ_v ∈ {1.0, 0.9, ..., 0.1} using the frozen mimic-video action decoder. Compute τ_v*(f) = argmin_{τ_v ∈ {1.0,...,0.1}} ||a_{τ_v}(f) − a_GT(f)||₂ for each frame f (GT action from demo teleop). Annotate frames by manipulation phase using end-effector distance to target + gripper state.\n\n[NEW] Preliminary zero-shot validation (run within Phase 0, ~1 additional H100-hour): Using CLIP image and frozen mimic-video language embeddings for the 5 tasks, train a task-level τ_v MLP on task-mean τ_v* from tasks 1–4. Evaluate zero-shot prediction on task 5. This 4→1 leave-one-out check validates whether task embedding space contains τ_v-predictive signal before committing the zero-shot LIBERO→SIMPLER-Bridge claim as a primary CoRL contribution. If prediction error on the held-out task is <20% of task 5's τ_v* value: preliminary evidence supports zero-shot generalization — proceed with zero-shot claim. If >20%: plan to include few-shot SIMPLER-Bridge adaptation (3 tasks) as fallback framing for Phase 3. Full 80/20 LIBERO held-out validation runs in Phase 2.\n\nDecision gate (by May 12):\n- If <10% of frames have τ_v* < 0.9 (nearly all frames prefer τ_v=1 for action quality): per-observation variation is minimal. Pivot paper framing to 'τ_v=1 universality study + automated zero-shot per-task routing' — do NOT commit to full Phase 1 scope. Reframe contribution as empirical validation + deployment automation.\n- If ≥20% of frames have τ_v* < 0.9 AND these cluster in grasp/insert phases: full selective activation story is empirically supported. Proceed to Phase 1.\n- Intermediate (10–20%): assess within-episode vs. across-task variance before proceeding.\n\n**Phase 1 — 3D Video Necessity Study (~40–60 H100-hours): The Primary Empirical Contribution**\nFor each frame f in LIBERO-100 (100 tasks × 50 demos × ~100 steps ≈ 500K frames), compute:\n\n  τ_v*(f) = argmin_{τ_v ∈ {1.0, 0.9, ..., 0.1}} ||a_{τ_v}(f) − a_GT(f)||₂\n\nwhere a_GT(f) is the ground-truth demonstration action at frame f (available from LIBERO-100 teleop data) and a_{τ_v}(f) is the mimic-video action decoder output with τ_v-noised video input. The sweep range {1.0,...,0.1} excludes τ_v=0 entirely (confirmed worse than intermediate τ_v in mimic-video). NOTE: τ_v=1 is the expected modal value for τ_v*(f) given mimic-video's main-text finding; Phase 1 asks how many frames deviate from τ_v*=1.0, and whether deviations cluster in specific manipulation phases.\n\nAnnotate frames with manipulation phases: approach (end-effector distance > 5cm to target), pre-grasp (distance 1–5cm, gripper open), grasp (gripper closing event), transport (gripper closed, object moving), place (object near target, gripper opening). Derive from proprioceptive state; no additional network required.\n\nReport: (a) Distribution of τ_v* — specifically fraction of frames where τ_v*=1.0 (consistent with mimic-video main text) vs. τ_v* < 0.9 (deviations from fixed-global optimal); (b) Mean τ_v* by manipulation phase — do grasp/insert phases show significantly lower τ_v* than approach/transport, characterizing for the FIRST TIME which 3D manipulation phases need video denoising below the τ_v=1 fixed-global default?; (c) Within-episode τ_v* variance vs. across-task τ_v* variance — which dominates?; (d) Whether LingBot-VA's fixed s≈0.6 corresponds to over-denoising for approach frames.\n\n[Distribution shift mitigation]: Include suboptimal rollout states to reduce demo-vs-rollout gap. Specifically: run the mimic-video policy (τ_v=1) 3× per task on LIBERO-100, collect frames from failed/recovery trajectories (partial grasps, dropped objects, recovery approaches). Add these to the labeling dataset (~50% of total labeled frames from non-expert trajectories). This gives the router diverse training states including recovery behaviors seen during closed-loop evaluation.\n\nCompute: ~750K frames × 10 τ_v levels = ~7.5M backbone forward passes. With batch=64 on Cosmos-Predict2 (2B DiT), ~40–60 H100-hours.\n\n**Phase 2 — Router Training + Zero-Shot Hold-Out Validation (~6 H100-hours):**\n4-class router: {τ_v=1.0 (no activation), τ_v∈[0.7,0.9] (light activation), τ_v∈[0.4,0.6] (medium activation), τ_v∈[0.1,0.3] (heavy activation)}. Labels from Phase 1 mapped to nearest class bin. Architecture: two-layer MLP (512-dim CLIP image embedding + 512-dim frozen mimic-video language embedding → 256-dim hidden ReLU → 4-class softmax). Loss: CE(τ̂, τ_v*_class) + λ·E[τ̂_consumed].\n\nConservative routing (addressing distribution shift): if max softmax probability < θ, predict τ_v=1.0 regardless of argmax — since τ_v=1 is the confirmed best fixed-global default, falling back to it on uncertain (OOD) states avoids unnecessary compute overhead while maintaining the quality floor. Sweep λ ∈ {0.01, 0.1} and θ ∈ {0.5, 0.7} to trace the accuracy-efficiency frontier (reduced from full grid to fit within compute budget).\n\nTask-level CDR variant: also train on task-mean τ_v* (average τ_v* across all frames in a task) to enable the per-task routing baseline (d) and test zero-shot generalization on SIMPLER-Bridge.\n\n[NEW] 80/20 LIBERO held-out validation (REQUIRED before finalizing zero-shot CoRL claim): Split LIBERO-100 into 80 training / 20 held-out tasks (stratified by task type). Train task-level τ_v MLP on 80 tasks' task-mean τ_v*. Test zero-shot on 20 held-out tasks: measure τ_v* recovery = (gain from predicted τ_v vs. τ_v=1) / (oracle gain from true τ_v* vs. τ_v=1).\n\nZero-shot claim gate:\n- If ≥80% τ_v* recovery on 20 held-out LIBERO tasks → zero-shot LIBERO→SIMPLER-Bridge claim is empirically credible. Keep as primary CoRL claim: 'per-task CDR recovers ≥80% of +9.4pp zero-shot on SIMPLER-Bridge.'\n- If <80% recovery on held-out LIBERO tasks → reframe to 'per-task routing with few-shot adaptation on 3 SIMPLER-Bridge tasks': train task-level MLP on the 3 SIMPLER-Bridge tasks with most available rollouts, test on remaining SIMPLER-Bridge tasks. This is still a deployment contribution (reduces 10-rollout per-task sweep to 3-task fine-tuning) but scoped more conservatively.\n\n**Phase 3 — Evaluation (~50 H100-hours, primary benchmark: SIMPLER-Bridge):**\n\n[ELEVATED ANCHOR CLAIM] Formal Pre-Registered Prediction: The primary competitive framing is CDR vs. τ_v=1 fixed-global baseline. We formally pre-register two predictions before running Phase 3 experiments:\n  (P1) Fixed intermediate τ_v baselines (b: τ_v=0.5; c: τ_v=0.7 and τ_v=0.9) will UNDERPERFORM baseline (a) τ_v=1 on SIMPLER-Bridge. This prediction is strongly supported by mimic-video's main text ('the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1'). The pre-registration converts a potential 'cherry-picked baselines' concern into a published empirical confirmation of mimic-video's finding. NOTE: DiT4DiT's ablation (Figure 8b, about action denoising steps — not τ_v) is NOT cited as corroborating evidence for P1; mimic-video's main text alone anchors this prediction.\n  (P2) Per-task CDR zero-shot router outperforms τ_v=1 on SIMPLER-Bridge (recovers ≥80% of per-task sweep gain = ≥7.5pp) — the central routing contribution.\n\n[CRITICAL PARETO HONESTY REQUIREMENT] If P1 is confirmed (the expected outcome): CDR routes the majority of frames to τ_v=1. Mean τ_v consumed by CDR stays close to 1.0. Per-inference GPU compute savings are SMALL (approximately 5–10%). The primary benefit CDR provides is: (1) TASK SUCCESS RECOVERY: +≥7.5pp zero-shot on SIMPLER-Bridge vs. τ_v=1; (2) DEPLOYMENT CALIBRATION SAVINGS: eliminates 10 offline rollouts per new task required to identify optimal fixed τ_v. The abstract, introduction, and Phase 3 results section MUST state this explicitly. The Pareto curve axis framing should reflect this: if P1 confirmed, the x-axis showing 'mean τ_v consumed' will show CDR close to τ_v=1 with small compute savings; the y-axis showing task success will show the +≥7.5pp gain. This is still a Pareto win (same compute, better performance) but is NOT primarily an efficiency contribution — it is a zero-shot deployment automation contribution that recovers task success without offline rollout cost.\n\nImplications of P1 confirmation: LingBot-VA-style uniform τ_v<1 is not a valid Pareto competitor on SIMPLER-Bridge. CDR's Pareto claim simplifies to a clean head-to-head: CDR vs. τ_v=1 fixed-global. The paper headline becomes: 'τ_v=1 is the best fixed-global baseline; CDR recovers per-task oracle gains zero-shot — same inference compute, +≥7.5pp task success, zero offline calibration rollouts.'\n\nImplications of P1 disconfirmation (some fixed τ_v < 1 outperforms τ_v=1 on SIMPLER-Bridge — less likely given mimic-video main text): CDR must Pareto-dominate the best fixed intermediate value. This is a harder but higher-impact claim — if confirmed, CDR also delivers genuine per-inference compute savings. Either outcome is publishable; the pre-registration removes selective reporting concerns regardless.\n\nBaselines:\n(a) mimic-video τ_v=1 global (confirmed best fixed-global per mimic-video main text; compute-efficient recommended default; 46.9% SIMPLER, 93.9% LIBERO). NOTE: this baseline also serves as CDR's closest achievable proxy for Fast-WAM's test-time video-skipping behavior on the mimic-video backbone — Fast-WAM (arXiv:2603.16666) does not evaluate on SIMPLER-Bridge and requires architectural retraining, so direct comparison is impossible; the paper notes this distinction explicitly.\n(b) LingBot-VA-style fixed τ_v=0.5 on mimic-video base (formally predicted to underperform τ_v=1 per P1; included to empirically confirm pre-registration)\n(c) LingBot-VA-style fixed τ_v=0.7 and τ_v=0.9 (systematic fixed-threshold sweep; NOTE: this is ALSO the first published fixed-global-τ_v comparison on SIMPLER-Bridge — mimic-video Table I does not include this sweep; confirms whether any fixed intermediate τ_v beats τ_v=1 globally)\n(d) Per-task CDR router (predict task-mean τ_v* zero-shot on SIMPLER-Bridge — primary routing result; claim: recovers ≥80% of +9.4pp sweep gain = ≥7.5pp without offline rollouts; gated on Phase 2 held-out LIBERO validation)\n(e) Per-observation CDR (full system)\n(f) Per-task sweep oracle (56.3% SIMPLER — upper bound)\n\nPrimary results: Pareto curves (task success vs. mean τ_v consumed) on SIMPLER-Bridge, anchored at the τ_v=1 fixed-global point. LIBERO-100 results reported secondarily for comparability. Key empirical claims:\n1. LingBot-VA-style uniform τ_v<1 is not a Pareto competitor on SIMPLER-Bridge — confirmed by pre-registered P1 (fixed τ_v < 1 underperforms τ_v=1)\n2. Per-task CDR Pareto-dominates τ_v=1 fixed-global: same inference compute as τ_v=1, +≥7.5pp task success, zero offline calibration rollouts — when P1 confirmed, the compute savings (mean τ_v consumed below 1.0) are modest but the task success gain is the primary result\n3. Per-observation CDR Pareto-dominates τ_v=1 on SIMPLER-Bridge — matching or exceeding the best fixed intermediate τ_v at strictly lower mean compute if P1 is disconfirmed, or beating τ_v=1 with near-1.0 mean τ_v if P1 confirmed\n4. CDR allocates lower τ_v (more video activation) to grasp-phase frames than approach frames — interpretability via per-phase τ_v heatmaps, constituting the first empirical characterization of manipulation-phase video necessity in 3D WAMs\n\nBaseline note on OA-WAM: OA-WAM (arXiv:2605.06481) evaluates on the same four WidowX Bridge tasks (SimplerEnv Visual Matching) as SIMPLER-Bridge in CDR, achieving 79.3% vs. CDR base 46.9%. CDR does not include OA-WAM as a direct baseline because OA-WAM uses a fundamentally different base architecture (7B Chameleon-style trunk requiring full retraining) vs. CDR's post-hoc routing on frozen mimic-video (2B Cosmos-Predict2). The paper explicitly states: 'OA-WAM and CDR evaluate on the same SimplerEnv WidowX Bridge tasks; the 79.3% vs. 46.9% performance gap reflects base model architecture and scale differences, not the routing contribution CDR introduces. CDR's Pareto claims are within the mimic-video architecture family and do not target models that require full retraining.'\n\nAblations: per-phase τ_v allocation analysis (grasp vs. approach); precision task subset (peg insertion, mug hanging) vs. coarse tasks; conservative routing ablation (θ sweep); zero-shot generalization from LIBERO-100 router to SIMPLER-Bridge tasks (no retraining — key deployment story). [RoboCasa results and full per-phase heatmap ablations are explicitly dropped from CoRL submission to stay within compute budget — these move to ICLR 2027 extended version if applicable.]\n\nNote on absolute LIBERO numbers: CDR built on mimic-video (93.9%) will fall below LingBot-VA (98.5%) and DiT4DiT (98.6%) due to base model gap. Paper leads with SIMPLER-Bridge Pareto curves in abstract/intro, framed as: 'SIMPLER-Bridge is a real-to-sim transfer benchmark evaluated on four WidowX Bridge tasks under Visual Matching; mimic-video's 46.9% is the state-of-the-art for this backbone, and CDR's gain is measured against this competitive baseline.' LIBERO results in supplementary for comparability. Framing is explicit in introduction: 'Our contribution is the first empirical characterization of manipulation-phase video necessity in 3D WAMs (Phase 1 study) and the zero-shot deployment automation that eliminates offline calibration rollouts, not absolute SOTA on LIBERO or SIMPLER-Bridge.'\n\n**Minimum Viable Submission (MVS) Track — Explicitly Defined:**\nIf Phase 1 takes 8 days (upper bound: May 12–20) and Phase 3 cannot fully complete by May 26, the MVS constitutes a submittable CoRL 2026 paper:\n- Phase 0 positive gate result (τ_v* distribution over 5 tasks with phase annotations)\n- Phase 1 τ_v* distribution histograms across LIBERO-100 (primary contribution: first empirical characterization of which manipulation phases need τ_v < 1 below the τ_v=1 fixed-global default)\n- Phase 2 router training + 80/20 held-out validation result\n- Phase 3 PARTIAL: Pareto curve with minimum 3 points — {(a) τ_v=1 baseline, (c) best fixed intermediate τ_v, (d) per-task CDR zero-shot} on SIMPLER-Bridge\n- Pre-registered prediction result for fixed τ_v < 1 baselines (P1 confirmation)\nMVS drops: full per-observation CDR (Phase 3 baseline e), RoboCasa results, per-phase heatmap ablation, conservative routing θ sweep. If MVS is the submission path, the paper's primary contribution becomes: (1) first empirical study of τ_v* distribution in LIBERO-100 with manipulation-phase breakdown (Phase 1 histograms) — answering 'which phases need video denoising below the τ_v=1 fixed-global default for the first time'; (2) zero-shot per-task CDR on SIMPLER-Bridge eliminating 10 offline calibration rollouts; (3) pre-registered confirmation that uniform partial denoising underperforms τ_v=1. This is submittable as a focused empirical contribution even without full per-observation routing results.\n\n**Timeline for CoRL 2026 (May 29 deadline):**\n- Phase 0: run May 10–11 (1–3 H100-hours including preliminary zero-shot check, 1–2 days)\n- Phase 0 gate decision: May 12\n- Phase 1 (if positive): May 12–18 (40–60h, with 8 H100s = 5–8 days)\n- Phase 2: May 18–19 (~1–2 days, includes 80/20 held-out validation)\n- Zero-shot claim gate decision: May 19\n- Phase 3: May 19–25 (50h / 8 H100s = ~6 days; RoboCasa and per-phase heatmap ablations are explicitly drop-able — MVS requires only SIMPLER-Bridge primary Pareto curve {τ_v=1, best fixed τ_v, per-task CDR} plus pre-registered prediction confirmation)\n- Write-up: May 25–28 (4 days; if Phase 1 takes 8 days, writing compresses to 2 days — acceptable for a focused Pareto-curve paper)\n- Buffer: May 29 submission\nFeasible but requires immediate Phase 0 execution. If Phase 0 is negative (< 10% activation frames), target ICLR 2027 with reframed 'zero-shot task routing' contribution.",

  "resource_estimate": {
    "manual": {
      "gpu_hours": "~115–135 H100-hours (Phase 0: ~3h including preliminary zero-shot check; Phase 1: ~50h corrected sweep including rollout states; Phase 2: ~6h including 80/20 held-out validation; Phase 3: ~50h SIMPLER+LIBERO+baselines, NO RoboCasa; ~20h buffer for reruns)",
      "gpu_utilization": "45–55% effective — GPUs idle during Phase 0 gate decision, phase annotation, zero-shot gate decision, and result inspection",
      "timeline": "2–3 weeks to CoRL submission (if Phase 0 positive by May 12); 2–3 months to ICLR 2027 otherwise",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$305 (122h × $2.49/hr spot H100)"
    },
    "human_in_loop": {
      "gpu_hours": "~93 H100-hours",
      "gpu_utilization": "65–75% — agent runs Phase 1 while human reviews Phase 0 gate; Phase 2 queued immediately after Phase 1 labels available; 80/20 validation runs in parallel with router training",
      "timeline": "12–15 days to CoRL submission (Phase 0 gate on day 2, Phase 1 complete day 9, Phase 2 zero-shot gate day 10, Phase 3 complete day 15)",
      "team": "1 researcher, ~20 min/day check-in",
      "claude_api_cost": "~$100–200 (~1,000–2,000 turns at $0.10/turn Opus 4.7)",
      "estimated_gpu_cost": "~$232 (93h × $2.49/hr spot H100)",
      "risk_note": "Two critical decision points: (1) Phase 0 gate by May 12 — if <10% activation frames, reframe to zero-shot per-task routing, target ICLR 2027. (2) Phase 2 zero-shot gate by May 19 — if 80/20 LIBERO held-out validation fails (<80% τ_v* recovery), reframe primary zero-shot claim to few-shot SIMPLER-Bridge adaptation before committing it in the paper. Human judgment at both gates is essential. If Phase 1 takes 8 days (upper bound), MVS track is the fallback — dropping per-observation CDR and full ablations to submit the Phase 1 histograms + per-task CDR + pre-registered prediction result. Critical path has no slack beyond MVS; prioritize per-task CDR zero-shot result over per-observation CDR in Phase 3."
    },
    "auto_research": {
      "gpu_hours": "~150–175 H100-hours (Phase 0: 3h including zero-shot check; Phase 1 with rollout states: 55h; Phase 2 with reduced λ×θ grid (λ∈{0.01,0.1} × θ∈{0.5,0.7}) plus 80/20 validation: 8h; Phase 3 SIMPLER-Bridge + LIBERO primary results only — NO RoboCasa, NO full per-phase heatmap ablations: 70h; buffer: 15h). SCOPE REDUCTION vs. prior 410H estimate: RoboCasa evaluation dropped, full 3×3 λ×θ hyperparameter grid dropped (reduced to 2×2), extensive per-phase heatmap ablations moved to ICLR 2027 extended version. This fits within the ≤200H project constraint.",
      "gpu_utilization": "Near-zero idle — phases pipelined",
      "timeline": "3–5 days with 8 H100s",
      "team": "0 (only initial sweep grid and eval harness setup required)",
      "claude_api_cost": "~$200–400 (~2,000–4,000 turns)",
      "estimated_gpu_cost": "~$410 (165h × $2.49/hr spot H100)",
      "risk_note": "Auto mode must halt at Phase 0 gate and Phase 2 zero-shot gate before proceeding. Must not treat per-observation Pareto improvement as the only valid outcome — if Phase 1 shows task-level variation dominates or zero-shot gate fails, auto mode must automatically pivot to MVS track (per-task CDR zero-shot or few-shot adaptation). Auto mode should run 80/20 LIBERO held-out validation in Phase 2 before writing any claim about zero-shot SIMPLER-Bridge generalization into draft sections. Auto mode must NOT interpret CDR's benefit as 'inference-time compute savings' if P1 is confirmed — the honest framing is 'deployment calibration cost savings (10 rollouts → 0) and task success recovery (+≥7.5pp), with mean τ_v consumed remaining close to 1.0.'"
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract deadline May 26, full paper May 29, 2026 — feasible only if Phase 0 positive by May 12 and MVS-track results complete by May 25)",
    "ICLR 2027 (deadline expected September–October 2026 — fallback if Phase 0 negative or timeline slips)"
  ],
  "level": "solid",
  "key_references": [
    "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (arXiv:2512.15692, Dec 2025) — CDR's base model. KEY VERIFIED FINDINGS — two distinct claims that must be cited separately: (a) MAIN TEXT (Section V-C): 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1 (Fig. 5)' — τ_v=1 is the confirmed best fixed-global τ_v, achieving 46.9% scratch SIMPLER-Bridge; (b) FIGURE 5 CAPTION: 'Performance peaks at an intermediate noise level, confirming that high-fidelity video reconstruction is not required for performant robot policies' — this refers to the oracle per-task view where τ_v is optimized independently per task. RECONCILIATION: τ_v=1 wins as the best single fixed global value (main text); the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption); CDR exploits this gap by approximating the per-task oracle via zero-shot routing; (c) Table I does NOT include a fixed-global-τ_v sweep — CDR's Phase 3 baselines provide the first such comparison on SIMPLER-Bridge; (d) per-task sweep +9.4pp (46.9%→56.3%), quantifying the gap between fixed-global τ_v=1 and per-task oracle; (e) τ_v=0 gives worse performance than intermediate τ_v — sweep excludes τ_v=0; (f) variable-τ_v training (logit-normal over [0,1]) makes action decoder robust at any τ_v — enabling CDR's selective activation without retraining",
    "LingBot-VA: Causal World Modeling for Robot Control (arXiv:2601.21998, RSS 2026) — PRIMARY COMPARISON (predicted to underperform τ_v=1 on SIMPLER-Bridge per pre-registered P1, supported by mimic-video main text); Noisy History Augmentation (saug∈[0.5,1.0]) enables fixed 3-step inference to s≈0.6; 98.5% LIBERO, 92.2% RoboTwin; included in Phase 3 baselines to empirically confirm that uniform partial denoising (τ_v < 1 applied uniformly) is NOT a valid Pareto competitor against τ_v=1 on SIMPLER-Bridge",
    "Fast-WAM: Do World Action Models Need Test-time Future Imagination? (arXiv:2603.16666, Mar 2026) — skips future video generation by processing only first clean observation; 97.6% LIBERO, 91.8% RoboTwin, 4× speedup; requires retraining. IMPORTANT: Fast-WAM does NOT evaluate on SIMPLER-Bridge — no direct comparison number exists. CDR's baseline (a) τ_v=1 serves as closest achievable proxy for Fast-WAM's test-time video-skipping behavior on mimic-video backbone; paper states this distinction explicitly",
    "OA-WAM: Object-Addressable World Action Model for Robust Robot Manipulation (arXiv:2605.06481, May 2026) — MUST CITE; evaluates on LIBERO (97.8%) and SimplerEnv WidowX Bridge Visual Matching (79.3% average: Spoon Towel 83%, Carrot Plate 71.1%, Stack Cube 65%, Eggplant Basket 98.2%). CRITICAL: OA-WAM's SimplerEnv evaluation uses THE SAME four WidowX Bridge tasks and Visual Matching protocol as CDR's SIMPLER-Bridge — directly comparable evaluation setup. The 79.3% vs 46.9% gap is due to base model architecture and scale (OA-WAM: 7B Chameleon-style trunk; CDR/mimic-video: 2B Cosmos-Predict2), not the routing method. DIFFERENTIATION: OA-WAM addresses object identity robustness via slot decomposition; CDR addresses adaptive video denoising depth via τ_v routing — orthogonal contributions. OA-WAM requires full architectural retraining; CDR is post-hoc on frozen checkpoint.",
    "A₁: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model (arXiv:2604.05672, April 2026) — MUST CITE as concurrent work; applies per-observation Inter-Layer Truncated Flow Matching with early exit for VLA backbone computation, achieving 72% latency reduction and 76.6% backbone computation savings on LIBERO and VLABench. DIFFERENTIATION: A₁ targets how many transformer layers to execute in a VLA backbone (inter-layer early exit); CDR targets how many denoising steps to apply to the video backbone in WAMs (τ_v depth routing) — orthogonal efficiency axes on different model families (VLAs vs WAMs).",
    "VADF: Vision-Adaptive Diffusion Policy Framework (arXiv:2604.15938, Apr 2026) — adapts ACTION diffusion denoising steps per task stage (shorter for simple, longer for complex); evaluated on Push-T, Adroit, ARX5; DIFFERENTIATION: VADF targets action denoising steps, CDR targets video backbone denoising depth (τ_v) — orthogonal efficiency axes, combinable",
    "Video Models Reason Early: Exploiting Plan Commitment for Maze Solving (arXiv:2603.30043) — 2D commitment motivation: video diffusion commits high-level plan in first few denoising steps; CDR extends and empirically validates for 3D manipulation video backbones",
    "DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control (arXiv:2603.10448) — CDR cites as structural analogy only; DiT4DiT's ablation (Figure 8b) shows that fewer ACTION denoising steps yield higher task success — this is about action diffusion steps, NOT τ_v (video noise level). IMPORTANT: DiT4DiT does NOT corroborate τ_v=1 video noise optimality — these are orthogonal efficiency axes. CDR's related work may note: 'DiT4DiT finds fewer action denoising steps improve task success in the action domain; we investigate the analogous question in the video backbone domain.' Any language claiming DiT4DiT 'independently confirms' high-τ_v video optimality is FACTUALLY INCORRECT and must not appear in the paper. 98.6% LIBERO, 50.8% RoboCasa.",
    "DreamZero: World Action Models are Zero-shot Policies (arXiv:2602.15922, Feb 2026) — velocity caching within denoising trajectory; complementary to CDR (reduces cost within a fixed τ_v level vs. CDR selecting τ_v level before denoising begins)",
    "Denoising, Fast and Slow (CVPR 2026, arXiv:2604.19141) — introduces Patch Forcing (PF) Framework for per-PATCH spatial difficulty routing within images: easier image regions advance denoising earlier, harder regions receive more steps — computation varies spatially WITHIN a single generated image. DIFFERENTIATION from CDR: CDR operates in the temporal domain (routing across trajectory frames — which frames need video backbone denoising), while Denoising Fast and Slow operates in the spatial domain (which patches within a single frame need more steps). These are orthogonal axes that could in principle be combined. Cited as feasibility motivation only; evaluates image generation, not robot action models.",
    "MotuBrain (arXiv:2604.27792) — unified VAM with Mixture-of-Transformers (MoT) architecture under UniDiffuser formulation; supports policy learning, world modeling, video generation, inverse dynamics; 95.8%+ on RoboTwin 2.0; 50× speedup via step reduction, FP8 quantization. DIFFERENTIATION: training-time architectural approach for unified multimodal modeling; CDR is post-hoc test-time routing on frozen mimic-video checkpoint requiring no retraining. Orthogonal — MotuBrain could serve as future CDR base model.",
    "D3P: Dynamic Denoising Diffusion Policy via Reinforcement Learning (arXiv:2508.06804) — adapts ACTION (not video) denoising steps via RL; orthogonal efficiency axis to CDR",
    "S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight (arXiv:2603.16195, Mar 2026) — distillation-based efficiency; requires retraining",
    "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising (arXiv:2604.26694) — X-WAM; fixed-distribution ANS baseline; not per-observation adaptive",
    "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets (arXiv:2504.02792) — UWM; fixed schedule baseline",
    "Being-H0.7: A Latent World-Action Model from Egocentric Videos (arXiv:2605.00078) — distillation-based; different efficiency axis; 99.2% LIBERO, 62.1% RoboCasa",
    "When to Trust Imagination: Adaptive Action Execution for World Action Models (arXiv:2605.06222) — introduces per-action-chunk adaptive replanning trigger: after each partial action execution, a learned threshold (τ=0.5) decides whether to continue executing the current plan or replan based on prediction reliability — orthogonal to CDR's per-observation τ_v routing"
  ],
  "description": "This paper investigates when World Action Models (WAMs) need video: the first systematic empirical study of per-observation optimal denoising depth (τ_v*) across LIBERO-100, with manipulation-phase breakdown, followed by a zero-shot router that automates per-task τ_v selection without offline calibration rollouts.\n\nThe paper's theoretical foundation rests on a precise reconciliation of two mimic-video findings: (1) mimic-video's main text (Section V-C) states 'the best autonomous policy performance in our SIMPLER experiments is achieved at the highest noise level τ_v=1' — establishing τ_v=1 as the best fixed-global τ_v, which CDR adopts as its default; (2) mimic-video's Figure 5 caption states 'Performance peaks at an intermediate noise level' — referring to the oracle per-task view where τ_v is selected independently per task. These are compatible: τ_v=1 wins when one fixed value is applied globally (main text), but the per-task oracle τ_v distribution peaks at intermediate levels (Figure 5 caption). The +9.4pp per-task sweep gain (46.9%→56.3% on SIMPLER-Bridge) quantifies the gap. The zero-shot router closes this gap without the 10-rollout per-task sweep cost.\n\nCRITICAL PARETO FRAMING (enforced throughout): When pre-registered prediction P1 is confirmed (the expected outcome per mimic-video main text), CDR routes most frames to τ_v=1, keeping mean τ_v consumed close to 1.0. Per-inference compute savings are small (5–10%). CDR's primary benefits are: (1) TASK SUCCESS RECOVERY — +≥7.5pp zero-shot on SIMPLER-Bridge; (2) DEPLOYMENT CALIBRATION SAVINGS — eliminating 10 offline rollouts per new task. The paper DOES NOT claim large per-inference speedups when P1 is confirmed. This distinction is stated explicitly in the abstract and introduction to prevent reviewer disappointment.\n\nTwo pre-registered predictions before Phase 3: (P1) LingBot-VA-style fixed τ_v<1 baselines underperform τ_v=1 on SIMPLER-Bridge — strongly supported by mimic-video's main text. If P1 confirmed, CDR's Pareto claim is: same inference compute, +≥7.5pp task success, zero offline calibration rollouts. (P2) Per-task CDR zero-shot router recovers ≥80% of the +9.4pp sweep gap on SIMPLER-Bridge.\n\nThe primary empirical contribution is Phase 1: first systematic study of τ_v* (per-observation optimal denoising depth) across LIBERO-100 with manipulation-phase breakdown — answering for the first time which 3D manipulation phases need video denoising below τ_v=1. The router (Phase 2, two-layer MLP on CLIP+language embeddings) is the deployment mechanism enabling zero-shot per-task generalization, not the central architectural novelty. Phase 3 reports Pareto curves on SIMPLER-Bridge anchored at the τ_v=1 fixed-global point.\n\nDiT4DiT (arXiv:2603.10448) is cited as structural analogy only: its ablation (Figure 8b) shows fewer action denoising steps improve task success in the action domain — a parallel finding that less denoising can be globally preferable. DiT4DiT does NOT corroborate τ_v=1 video noise optimality directly; these are orthogonal efficiency axes and must not be conflated.\n\nThe paper explicitly frames: OA-WAM (arXiv:2605.06481) evaluates on the same four WidowX Bridge tasks (79.3% vs CDR base 46.9%); the gap reflects base model architecture (7B Chameleon vs 2B Cosmos-Predict2), not the routing contribution. CDR's Pareto claims are within the mimic-video architecture family. Target: CoRL 2026 (May 29); ICLR 2027 fallback.",
  "project_name": "commit_depth_router",
  "source": "web_research"
}
```

---

**Summary of changes (major revision):**

**Fix 1 — DiT4DiT (required, all instances corrected):** Removed every claim that DiT4DiT "independently corroborates" τ_v=1 video optimality. The ablation concerns action denoising steps, not τ_v. Rewritten across landscape, approach/Phase 3/P1, key_references, and description as a "structural analogy only" — same direction (less denoising better), different axis (action vs. video). P1 now anchors solely on mimic-video's main text.

**Fix 2 — Pareto honesty (required, now load-bearing):** Added a "CRITICAL PARETO FRAMING" block in core_problem, approach/Phase 3, and description. When P1 is confirmed: mean τ_v stays near 1.0, per-inference compute savings are 5–10%, and CDR's actual benefits are (a) +≥7.5pp task success zero-shot and (b) 10 offline calibration rollouts → 0. The paper's Pareto story now positions CDR as a *deployment automation* contribution first, *efficiency* contribution second (and only if P1 is disconfirmed).

**Fix 3 — Auto-mode budget cap (required):** Reduced from 410H to 150–175H by dropping RoboCasa, cutting the λ×θ grid from 3×3 to 2×2, and removing extensive per-phase heatmap ablations (moved to ICLR 2027). Fits within ≤200H constraint.

**Fix 4 — "When to Trust Imagination" (minor, corrected):** Rewritten as "per-action-chunk adaptive replanning trigger with threshold τ=0.5" per reviewer's verified description.

**Fix 5 — Title (optional but adopted):** Changed to "When Do World Action Models Need Video? Manipulation-Phase Analysis and Zero-Shot Selective Denoising Activation" — foregrounds Phase 1 empirical study as primary contribution, reduces reviewer expectations of architectural novelty, and positions the paper honestly as an empirical methods paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8c39219-0d3a-42eb-933f-98f1cd130d8c",
  "isSidechain": false,
  "requestId": "req_011CateRv7XztmfhCHeHhAF7",
  "type": "assistant",
  "uuid": "7ae0fac2-6bf6-4aec-a458-605be61dbdf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019XWVUaeRGkoqekFcC8y6he",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 40241,
      "output_tokens": 16486,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16486,
          "cache_read_input_tokens": 40241,
          "cache_creation_input_tokens": 1292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1292
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Commitment Depth Routing: Selective Video Activation in Video-Action M…",
  "leafUuid": "7ae0fac2-6bf6-4aec-a458-605be61dbdf5",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze video activation in robot policy learning",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Commitment Depth Routing: Selective Video Activation in Video-Action M…",
  "leafUuid": "7ae0fac2-6bf6-4aec-a458-605be61dbdf5",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze video activation in robot policy learning",
  "sessionId": "359778ed-6dc4-481c-8b47-e9a2990ee60c"
}
```

---
