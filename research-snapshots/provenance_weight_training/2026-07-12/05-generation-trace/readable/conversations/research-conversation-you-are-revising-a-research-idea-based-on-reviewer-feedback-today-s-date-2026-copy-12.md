# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/3eca5a12-2fc4-436c-9188-e19cda922486.jsonl`
- **Structured JSON:** [`4f4851b4503766d65345.json`](../../sessions/4f/4f4851b4503766d65345.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T12:57:50.577Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T12:57:50.577Z",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"URDF-DiT: Does Full-Body Kinematic Conditioning Throughout Denoising Improve IDM Training Data for Humanoid Whole-Body Contact Tasks?\",\n  \"core_problem\": \"The central empirical question: does conditioning a video diffusion model on all 29 DoF of a humanoid robot's URDF forward kinematics throughout the entire denoising process — enforcing joint-limit compliance in every generated frame via structured Gaussian heatmaps injected into DiT cross-attention — yield measurably better IDM training trajectories for whole-body contact interaction tasks than (A) post-hoc kinematic recovery applied after unconstrained video generation, or (B) end-effector-only conditioning (~5 DoF wrist/hand positions)? This question is directly testable via two ablations — (A) URDF-DiT vs. vanilla Wan 2.2 + post-hoc URDF-IK (same IDM, same downstream policy training) and (B) 29 DoF full-body FK heatmaps vs. end-effector-only heatmaps — with downstream Isaac Lab G1 pick-and-place policy success rate as the primary evaluation metric.\\n\\n⚠️ USER REQUIREMENT TRADEOFF — EXPLICIT FLAG: The user specified three required evaluation platforms: Isaac Lab G1 locomanipulation, HumanoidBench whole-body tasks, and RoboCasa365 humanoid kitchen. The CoRL 2026 scoped submission covers ONLY Isaac Lab G1 locomanipulation (1 of 3 required benchmarks). HumanoidBench and RoboCasa365 are deferred entirely to ICLR 2027. The user should make an explicit decision: (option A) target CoRL 2026 with 1-of-3 benchmark coverage and full results on all three platforms at ICLR 2027; (option B) skip CoRL 2026 entirely and target ICLR 2027 from the start with full user-required benchmark coverage. This tradeoff is presented explicitly, not embedded quietly in venue notes.\\n\\nThree coupled sub-problems require simultaneous solution: (1) EA-WM (arXiv:2605.06192) validates that KVAF kinematic heatmap injection into Wan 2.2 cross-attention enforces kinematic consistency for arm manipulation — but evaluates arm tasks only (WorldArena benchmark), requires joint fine-tuning of both branches, and produces no policy training output; (2) Dream2Act (arXiv:2603.19709) generates in robot-native visual space (hallucinating the G1 body, not retargeting from human video) and achieves 37.5% on G1 whole-body contact tasks — but applies kinematic recovery POST-generation via constrained URDF-IK (converting pixel-space poses to joint angles after all video frames are produced), and targets zero-shot real-robot execution rather than synthetic training data generation; (3) VAG (arXiv:2604.09330) jointly denoises video and action via flow matching but explicitly acknowledges 'the video branch has not been influenced by the action branch' and provides no kinematic constraints. URDF-DiT directly tests whether the in-loop conditioning approach (vs. Dream2Act's post-hoc IK) and the full-body scope (vs. EA-WM's arm-only conditioning and VAG's unconstrained generation) are necessary for high-quality IDM training data on whole-body contact tasks — an empirical question with a clear experimental design.\",\n  \"opportunity\": \"GR00T-Dreams/DreamGen (2025) validated the video-diffusion → IDM pipeline for tabletop manipulation. Dream2Act (arXiv:2603.19709, March 2026) extended to full-body G1 whole-body contact interaction by generating video in robot-native visual space — hallucinating the G1 robot body to achieve morphological consistency — then applying post-generation kinematic recovery: (a) native 2D pose estimation, (b) 2D-to-3D lifting, (c) URDF-constrained IK to convert pixel-space poses to joint trajectories. Dream2Act achieves 37.5% overall success across four whole-body contact tasks (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%) vs. 0% for conventional retargeting baselines; inference latency is its primary stated limitation. Dream2Act's two distinct components — (A) robot-native video generation modality and (B) post-generation URDF-constrained IK for kinematic extraction — are the baseline against which URDF-DiT's in-loop conditioning is tested. The hypothesis: conditioning on FK heatmaps throughout denoising prevents kinematically infeasible frame transitions during generation rather than correcting them afterward, producing cleaner IDM training trajectories.\\n\\nEA-WM (arXiv:2605.06192, May 7 2026) validates that in-loop kinematic heatmap injection into Wan 2.2 cross-attention enforces kinematic consistency — using KVAFs (Gaussian heatmaps at projected joint/end-effector positions) via event-aware bidirectional dual-stream fusion. But EA-WM evaluates arm manipulation only (WorldArena benchmark), requires joint fine-tuning of both video and kinematic branches, and produces no policy training output. URDF-DiT extends this approach to the full-body 29 DoF case with a ControlNet-style frozen backbone (more compute-efficient, ~40% fewer trainable parameters) and adds the IDM→policy pipeline — but critically, the full-body extension is not assumed: it is empirically tested via the 29 DoF vs. end-effector-only ablation, which is the paper's primary scientific finding.\\n\\nVAG (arXiv:2604.09330, April 2026) introduces dual-stream flow matching jointly denoising video and action for arm manipulation (7–16 DoF, 45% on AgiBot G1 dual-arm grasping vs. 8% IDM baseline) but explicitly acknowledges the video-action coupling gap. EVA (arXiv:2603.17808, March 2026) enforces executability via learned IDM reward signals (RL post-training, soft constraint) on bimanual tabletop tasks — distinct from URDF-DiT's hard geometric constraint at every diffusion step.\\n\\n⚠️ USER REQUIREMENT TRADEOFF: The user required evaluation on Isaac Lab G1 locomanipulation, HumanoidBench, and RoboCasa365. CoRL 2026 covers only Isaac Lab G1 locomanipulation. Full benchmark coverage requires ICLR 2027. The user must decide between CoRL 2026 (fast, partial coverage) and ICLR 2027 (full coverage). This is not a minor footnote — it is a deliberate scope decision with direct implications for whether the work meets the user's original requirements at submission time.\\n\\nVENUE/TIMELINE NOTE: Today is May 10, 2026. CoRL 2026 deadline is May 29 — 19 days away. CoRL 2026 is feasible ONLY in auto-research mode with 8+ H100s available from Day 1, scoped to Isaac Lab G1 locomanipulation + Dream2Act ball kicking contextual comparison, with 2 ablations and a concrete Day 14 decision gate (see resource_estimate). Manual mode (4–6 months) and HIL mode (5–8 weeks) are incompatible with CoRL 2026.\",\n  \"landscape\": \"GR00T-Dreams/DreamGen (arXiv 2025): fine-tunes Cosmos-Predict2 with language conditioning; extracts pseudo-actions via IDM or latent action model. No URDF kinematic constraint. Tabletop manipulation only.\\n\\nDream2Act (arXiv:2603.19709, March 2026): Two distinct components must be distinguished — (A) VIDEO GENERATION MODALITY: generates in robot-native visual space by hallucinating the G1 robot body (not retargeting from human video) using Seedance 2.0, achieving morphological consistency; (B) KINEMATIC EXTRACTION: post-generation pipeline applying native 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK to convert pixel-space poses to joint trajectories. Achieves 37.5% overall success across four whole-body contact interaction benchmarks (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%) vs. 0% for conventional retargeting. Primary stated limitation is inference latency as an offline planner. Dream2Act targets zero-shot real-robot execution; URDF-DiT targets synthetic IDM training data generation — complementary goals. URDF-DiT tests whether conditioning the video branch on FK heatmaps throughout denoising (in-loop) improves IDM training data quality relative to Dream2Act's approach (B), post-generation URDF-IK.\\n\\nEA-WM (arXiv:2605.06192, May 2026): 'EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields' — injects Kinematic-to-Visual Action Fields (KVAF: Gaussian heatmaps at projected end-effector/joint locations) via event-aware bidirectional dual-stream fusion into Wan 2.2; evaluates on WorldArena benchmark for arm manipulation tasks; requires joint fine-tuning of both video and kinematic streams; no policy training output (action recovery detection rate ~0.45). Note: 'EA' = Event-Aware, not Embodiment-Aware. URDF-DiT differentiates on three empirically testable axes: (a) full-body 29+ DoF vs. arm manipulation — tested by full-body vs. end-effector ablation; (b) ControlNet-style frozen backbone vs. joint fine-tuning — ~40% fewer trainable parameters; (c) explicit IDM→policy pipeline vs. no policy output.\\n\\nVAG (arXiv:2604.09330, April 2026): dual-stream video-action generation using flow matching for tabletop arm manipulation (7–16 DoF); 45% on AgiBot G1 dual-arm grasping vs. 8% ResNet+IDM baseline; no URDF kinematic constraints; authors explicitly acknowledge 'video branch not influenced by action branch'; no full-body humanoid evaluation. URDF-DiT's in-loop FK heatmap injection directly addresses VAG's stated limitation while extending to 29+ DoF whole-body tasks.\\n\\nEVA (arXiv:2603.17808, March 2026): closes executability gap via RL post-training using IDM-derived reward signals penalizing embodiment violations (joint-limit violations, velocity/acceleration/jerk penalties); evaluates on RoboTwin 2.0 bimanual manipulation. Key distinction: EVA = learned IDM reward (soft executability constraint via RL post-training); URDF-DiT = explicit geometric URDF FK heatmaps (hard geometric constraint injected at every diffusion step). EVA evaluates bimanual tabletop; URDF-DiT targets full-body 29+ DoF contact interaction.\\n\\nFlowAct-R1 (arXiv:2601.10103, January 2026): 'FlowAct-R1: Towards Interactive Humanoid Video Generation' — real-time interactive digital human character animation via MMDiT chunkwise diffusion with audio/text-based full-body control at 25fps; targets NPC-style animated digital humans for real-time interaction (lip-sync, facial expressions, body gestures), not physical robot embodiment; no URDF kinematic structure, no physical robot joint constraints, no IDM policy extraction pipeline. Differentiation: interactive character animation use case vs. offline robot training data generation; audio/text conditioning vs. geometric URDF FK heatmaps.\\n\\nKStar Diffuser (arXiv:2503.10743, CVPR 2025): URDF-parsed spatial-temporal graph with differentiable FK for bimanual arm action diffusion (68.2% ± 2.1 success with 100 demos vs. 33.9% for PerAct2); operates at the policy/action layer not video synthesis — complementary to URDF-DiT rather than competing.\\n\\nKinema4D (arXiv March 2026, NTU): URDF-driven FK for 4D pointmap conditioning for scene realism; not policy-data generation or video diffusion attention-layer injection.\\n\\nControllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026): cascaded text-to-2D-skeleton → skeleton-to-video pipeline validates per-frame 2D pose-sequence conditioning in video diffusion for human motion synthesis — closest video-generation analogue to URDF-DiT's conditioning mechanism, but targets human motion not robot URDF kinematics or policy extraction.\\n\\nX-Humanoid (arXiv Dec 2025): replaces human with humanoid in video via Wan 2.2; no URDF constraint injection. MITTY (arXiv 2025): human-to-robot video diffusion without kinematic enforcement. G-DReaM (arXiv 2025): graph-conditioned diffusion for cross-embodiment motion retargeting on motion sequences, not RGB video.\\n\\nHumanoidBench (arXiv:2403.10506, 2024): 27 whole-body tasks (H1/Digit robots, MuJoCo); deferred to ICLR 2027 full paper. RoboCasa365 (arXiv:2603.04356, ICLR 2026): 365 kitchen tasks with humanoid support; deferred to ICLR 2027 full paper.\",\n  \"approach\": \"PRIMARY SCIENTIFIC CLAIM (reframed to lead the paper): The paper's central empirical question — presented as a hypothesis test, not merely a system description — is whether full-body kinematic conditioning throughout denoising is NECESSARY for whole-body contact task IDM training data generation, not merely sufficient. Two ablations directly test this:\\n\\nABLATION A (primary, vs. Dream2Act approach B): Does in-loop FK conditioning produce better IDM training trajectories than post-hoc URDF-IK applied to unconstrained video? Setup: same IDM, same downstream Isaac Lab G1 policy training procedure, same evaluation benchmark — only the video source differs. URDF-DiT-generated videos vs. vanilla Wan 2.2 videos post-processed with URDF-IK (the same IK pipeline used in Dream2Act's kinematic extraction stage). This directly measures whether conditioning throughout denoising outperforms correcting afterward.\\n\\nABLATION B (central scientific claim, vs. EA-WM conditioning scope): Does full-body 29 DoF conditioning (pelvis, legs, torso, arms, hands) improve IDM training data quality over end-effector-only conditioning (~5 DoF wrist/hand positions)? Setup: same IDM, same downstream policy evaluation — only the conditioning scope differs. For whole-body CONTACT tasks (ball kicking, pick-and-place with locomotion), the hypothesis is that leg and torso kinematics during approach and weight-shifting phases affect interaction quality in ways that end-effector-only conditioning cannot capture. Ablation B is the paper's STRONGEST SCIENTIFIC CLAIM and the primary differentiator from EA-WM — if full-body conditioning yields ≥5 pp improvement over end-effector-only on the downstream policy success rate, this empirically validates that the 29 DoF extension is necessary, not incremental. If the improvement is < 3 pp, the paper should be reframed as 'end-effector conditioning is sufficient for whole-body tasks, simplifying the conditioning design' — still a valid and publishable empirical finding.\\n\\nARCHITECTURE: URDF-DiT uses a ControlNet-style conditioning module — Wan 2.2 backbone weights fully frozen; only the FK-heatmap encoder and zero-conv injection layers are trained — that encodes per-frame G1 URDF forward-kinematics outputs (all 29 DoF, projected to the camera plane via differentiable FK) as structured Gaussian joint-position heatmaps and injects them into the cross-attention layers of the Wan 2.2 DiT. Unlike EA-WM's event-aware bidirectional dual-stream fusion (requiring joint fine-tuning of both video and kinematic branches), URDF-DiT's ControlNet-style design concentrates all learning in the conditioning module, reducing trainable parameters ~40% versus EA-WM's architecture — enabling the full pipeline within ≤200 H100-hours. Full-body G1 scope (29 DoF: pelvis, legs, torso, arms, hands) is the embodiment extension under test in Ablation B.\\n\\nDIFFERENTIATING DREAM2ACT PRECISELY: Dream2Act operates as follows: (A) video generation modality = robot-native visual space (Seedance 2.0 hallucinating the G1 body for morphological consistency — not retargeting from human video); (B) kinematic extraction = post-generation pipeline applying 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK (applied AFTER all video frames are generated). URDF-DiT vs. Dream2Act is not a comparison of visual generation approach — both generate in robot-native-compatible space — but specifically a test of whether kinematic constraints applied IN-LOOP during denoising (URDF-DiT) produce better training data than constraints applied POST-GENERATION (Dream2Act's approach B), for the synthetic data use case.\\n\\nJoint-angle sequences are sampled from an Isaac Lab G1 motion library covering locomotion primitives and upper-body reach plans, projected onto the camera plane, and encoded as per-frame kinematic tokens injected into DiT cross-attention.\\n\\nFK RESIDUAL LOSS: A per-frame FK residual consistency loss penalizes deviations between joint positions in generated video frames and URDF FK predictions from the conditioning signal. This is a kinematic consistency mechanism operating on geometric structure — reducing temporal joint jitter, preventing joint-limit violations during denoising. It is NOT a visual domain gap bridge. The visual appearance domain gap between Wan 2.2 outputs and Isaac Lab rendering is separately addressed via domain-randomized Isaac Lab rendering during IDM training (sampling lighting, camera noise, surface material variation to statistically overlap with Wan 2.2's output distribution). Two distinct mechanisms for two distinct problems.\\n\\nThe sim-bootstrapped IDM is trained on (frame_t, frame_{t+k}, joint-velocity) tuples from G1 Isaac Lab rollouts under domain-randomized conditions, then applied zero-shot to URDF-DiT-generated videos. If domain gap remains too large (joint-limit violation rate >15% in generated videos at the 3-day checkpoint), a contingency IDM adapter fine-tuned on ~200 URDF-DiT frame pairs matched to Isaac Lab rollouts via kinematic alignment (~8h additional compute) activates.\\n\\nEVALUATION STRATEGY:\\n\\n(1) CoRL 2026 scoped (2 benchmarks, 2 ablations): Isaac Lab G1 locomanipulation pick-and-place (primary); Dream2Act ball kicking (contextual comparison — 40% success, distinct use case: zero-shot real-robot execution vs. synthetic training data); Ablation A (in-loop URDF-DiT vs. post-hoc vanilla Wan 2.2 + URDF-IK); Ablation B (29 DoF full-body vs. end-effector-only). NOTE: covers 1 of 3 user-required benchmarks.\\n\\n(2) ICLR 2027 full paper (all user-required platforms): Isaac Lab G1 locomanipulation (multi-task: pick-and-place, reaching, pick-navigate-place); HumanoidBench H1 whole-body (carry + cabinet); RoboCasa365 humanoid kitchen (pick-and-place in kitchen); Dream2Act ball kicking + bag punching; Ablations A and B plus: ControlNet-style frozen backbone vs. EA-WM-style event-aware bidirectional fusion; URDF-DiT geometric FK conditioning vs. EVA-style learned IDM reward.\",\n  \"resource_estimate\": {\n    \"corl2026_scoped_auto\": {\n      \"gpu_hours\": \"~130h H100 total compute (compressed to ~12–18h wall clock on 8 H100s)\",\n      \"gpu_utilization\": \"Near-zero idle (~88–92% effective utilization) — agent queues IDM training immediately after ControlNet training checkpoint and runs evaluation generation in parallel\",\n      \"timeline\": \"19 days (May 10 → May 29, 2026 CoRL deadline) with 8+ H100s available from Day 1\",\n      \"team\": \"0 (4h Day 1 setup: Isaac Lab G1 motion library, domain-randomized rendering, URDF-DiT scaffold, evaluation harness)\",\n      \"estimated_gpu_cost\": \"~$416 (130h × $3.20/hr) spread across 8 GPUs\",\n      \"day_by_day_plan\": \"Day 1: env setup (Isaac Lab G1, Wan 2.2 base, eval harness). Days 2–3: implement FK heatmap encoder + zero-conv injection layers for Wan 2.2 cross-attention; simultaneously implement vanilla Wan 2.2 + post-hoc URDF-IK baseline for Ablation A. Days 3–5: ControlNet module training 35–50h GPU compute (~5–7h wall clock on 8 H100s). Days 4–5: IDM training in parallel (~25h GPU, ~3h wall clock). Days 5–8: generate 200 evaluation videos from URDF-DiT and 200 from vanilla Wan 2.2 baseline (~35h GPU, ~5h wall clock). Days 7–11: Isaac Lab G1 policy evaluation on trajectories from both sources (simulation rollouts — wall-clock bottleneck: parallel episode execution). Days 8–12: Ablation B (29 DoF vs. end-effector-only, same IDM, same downstream policy evaluation) + Dream2Act ball kicking contextual comparison. Days 12–14: results analysis and Day 14 DECISION GATE (see pivot_criteria below). Days 14–19: agent-assisted LaTeX drafting of all paper sections (introduction, related work, method, experiments) — auto mode includes full concurrent section generation starting Day 14.\",\n      \"pivot_criteria\": {\n        \"description\": \"Day 14 decision gate with concrete metric thresholds. Calibration anchor: Isaac Lab G1 pick-and-place with Robomimic from clean teleoperation demos achieves 92% success; IDM extraction from generated video will yield substantially lower rates due to visual noise and trajectory imprecision. Thresholds are set relative to the vanilla Wan 2.2 + post-hoc URDF-IK baseline, not absolute performance.\",\n        \"submit_to_corl\": {\n          \"condition\": \"ALL of the following: (1) URDF-DiT trained policy success rate ≥ 20% on Isaac Lab G1 pick-and-place (establishes non-trivial absolute performance from generated data); (2) URDF-DiT > vanilla Wan 2.2 + post-hoc URDF-IK baseline by ≥ 5 percentage points (establishes in-loop conditioning advantage — Ablation A is positive); (3) joint-limit violation rate in URDF-DiT generated videos ≤ 10% (validates FK conditioning is working geometrically)\",\n          \"strong_submission_additionally\": \"Full-body 29 DoF conditioning ≥ end-effector-only conditioning by ≥ 5 pp on downstream policy success (Ablation B strongly positive — validates the 29 DoF scope claim empirically)\"\n        },\n        \"submit_with_reframing\": {\n          \"condition\": \"Ablation A positive (URDF-DiT ≥ baseline + 5 pp) BUT Ablation B shows < 3 pp improvement from full-body vs. end-effector-only conditioning — reframe as 'end-effector conditioning suffices; full 29 DoF conditioning adds marginal benefit for pick-and-place.' Still a valid CoRL contribution if absolute performance (condition 1) and FK violation rate (condition 3) are met.\",\n          \"note\": \"Negative ablation B result is publishable as an empirical finding, not a failure — it simplifies the design recommendation for the community.\"\n        },\n        \"pivot_to_iclr_2027\": {\n          \"condition\": \"ANY of the following: (1) URDF-DiT fails to exceed baseline by ≥ 5 pp (Ablation A inconclusive — primary claim unsupported); (2) joint-limit violation rate > 15% in URDF-DiT generated videos (FK conditioning not working — triggers IDM adapter contingency, but if adapter also fails, implementation issue requires debugging time incompatible with May 29 deadline); (3) absolute policy success < 15% (both URDF-DiT and baseline yield near-zero performance — IDM domain gap too large for 19-day timeline, requires more investigation); (4) contingency IDM adapter required AND results still negative after adapter training\",\n          \"note\": \"ICLR 2027 pivot preserves all GPU investment — same implementation, full benchmark coverage (all 3 user-required platforms), full ablation suite. Pivot to ICLR 2027 is not a failure; it is the correct decision if CoRL results do not meet the above thresholds.\"\n        }\n      },\n      \"scope\": \"2 benchmarks (Isaac Lab G1 locomanipulation + Dream2Act ball kicking contextual comparison), 2 ablations (A: in-loop URDF-DiT vs. post-hoc vanilla Wan 2.2 + URDF-IK; B: full-body 29 DoF vs. end-effector-only conditioning). HumanoidBench and RoboCasa365 deferred to ICLR 2027. NOTE: covers 1 of 3 user-required benchmarks.\",\n      \"feasibility_risk\": \"HIGH. Estimated 60–70% probability of obtaining submittable results by May 29 in auto mode. Key risks: (1) ControlNet training non-convergence adds 1–2 days; (2) IDM domain gap exceeds FK residual loss + domain randomization, triggering 8h contingency adapter; (3) Isaac Lab simulation evaluation wall-clock bottleneck if environment resets are slow. Day 14 decision gate with concrete thresholds (above) provides an unambiguous pivot trigger.\",\n      \"requirement\": \"8+ H100s available from Day 1 (May 10). If fewer than 8 GPUs are available, wall-clock time increases proportionally and May 29 deadline becomes infeasible — target ICLR 2027.\"\n    },\n    \"manual\": {\n      \"note\": \"ICLR 2027 full paper mode (full coverage of all 3 user-required benchmarks). Incompatible with CoRL 2026 deadline.\",\n      \"gpu_hours\": \"~130–150h H100 (sensitivity-adjusted: ControlNet training 35–70h + IDM 25h + video generation/eval 35h + ablations 25h + data prep 10h)\",\n      \"gpu_utilization\": \"HIGH idle rate (~40–50% effective utilization) — sequential experiment launches and human debugging\",\n      \"timeline\": \"4–6 months (ICLR 2027 submission ~October 2026)\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$416–$480 (130–150h × $3.20/hr)\",\n      \"breakdown\": \"ControlNet module training: 35–70h; IDM training (Isaac Lab G1 rollouts + domain-randomized rendering): ~25h; Video generation + evaluation (Isaac Lab + HumanoidBench + RoboCasa365 + Dream2Act contextual): ~35h; Ablations A, B, ControlNet-vs.-bidirectional-fusion, geometric-FK-vs.-EVA-RL: ~25h; Data prep: ~10h. At 70h worst case for ControlNet: total ~165h, within 200h cap.\",\n      \"benchmark_coverage\": \"FULL — Isaac Lab G1 locomanipulation, HumanoidBench H1 whole-body, RoboCasa365 humanoid kitchen. Meets all 3 user-required benchmarks.\"\n    },\n    \"human_in_loop\": {\n      \"note\": \"ICLR 2027 full paper mode. Incompatible with CoRL 2026 deadline.\",\n      \"gpu_hours\": \"~160h H100\",\n      \"gpu_utilization\": \"Moderate (~60–65% effective utilization)\",\n      \"timeline\": \"5–8 weeks (ICLR 2027 submission ~October 2026)\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"~$150–300 (Opus, ~1,500–2,000 conversation turns)\",\n      \"estimated_gpu_cost\": \"~$512 (160h × $3.20/hr)\",\n      \"risk_note\": \"Human oversight detects IDM domain-gap failure at 2-week checkpoint, activates contingency IDM adapter (~8h additional compute) before remaining budget is spent.\",\n      \"benchmark_coverage\": \"FULL — all 3 user-required benchmarks.\"\n    },\n    \"auto_research\": {\n      \"note\": \"ICLR 2027 full paper mode (all user-required evaluation platforms). For CoRL 2026 scoped version, see corl2026_scoped_auto above.\",\n      \"gpu_hours\": \"~200h H100 (covers full ablation suite: Ablation A, Ablation B, ControlNet-style vs. EA-WM bidirectional fusion, geometric FK vs. EVA-style RL reward, IDM backbone comparisons, FK heatmap resolution variants)\",\n      \"gpu_utilization\": \"Near-zero idle (~88–92% effective utilization)\",\n      \"timeline\": \"1–2 weeks with 8+ H100s; 3–4 weeks on 4 GPUs\",\n      \"team\": \"0 (initial setup ~4h)\",\n      \"claude_api_cost\": \"~$400–700 (Opus, ~4,000–7,000 turns)\",\n      \"estimated_gpu_cost\": \"~$640 (200h × $3.20/hr)\",\n      \"benchmark_coverage\": \"FULL — all 3 user-required benchmarks (Isaac Lab G1 locomanipulation multi-task, HumanoidBench H1 whole-body, RoboCasa365 humanoid kitchen).\",\n      \"risk_note\": \"Automated evaluation harness must include per-frame kinematic consistency checks (FK residual, joint-limit violation rate, temporal flicker score) alongside task success. If FK residual loss is insufficient for IDM domain transfer (joint-limit violation rate >15%), agent triggers IDM adapter contingency (~8h) automatically.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (paper deadline May 29, 2026 — 19 days from today): FEASIBLE only in auto-research mode with 8+ H100s available starting May 10. ⚠️ COVERS ONLY 1 OF 3 USER-REQUIRED BENCHMARKS (Isaac Lab G1 locomanipulation only; HumanoidBench and RoboCasa365 deferred to ICLR 2027). Scoped to 2 ablations: (A) in-loop URDF-DiT vs. post-hoc vanilla Wan 2.2 + URDF-IK extraction; (B) full-body 29 DoF vs. end-effector-only conditioning — the paper's primary scientific claim. Day 14 decision gate: submit if URDF-DiT ≥ 20% success AND ≥ 5 pp improvement over baseline AND joint-limit violation rate ≤ 10%; pivot to ICLR 2027 otherwise. Estimated 60–70% probability of submittable results by deadline. If Day 14 shows negative results, same implementation pivots to ICLR 2027 with no wasted GPU investment.\",\n    \"ICLR 2027 (expected submission deadline ~October 2026; official announcement pending at iclr.cc): RECOMMENDED if full user-required benchmark coverage is the priority. Covers all 3 required platforms (Isaac Lab G1 locomanipulation, HumanoidBench H1 whole-body, RoboCasa365 humanoid kitchen) and full ablation suite (A, B, ControlNet-vs.-bidirectional-fusion, geometric-FK-vs.-EVA-RL). All operation modes (manual 4–6 months, HIL 5–8 weeks, auto 1–2 weeks on 8 H100s) are compatible.\",\n    \"CoRL 2027 (fallback if ICLR 2027 results are negative)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories (arXiv 2025)\",\n    \"Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis / Dream2Act (arXiv:2603.19709, March 2026) — TWO DISTINCT COMPONENTS: (A) video generation modality: robot-native visual space by hallucinating G1 robot body via Seedance 2.0 (not retargeting from human video); (B) kinematic extraction: post-generation pipeline via 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK. Achieves 37.5% success (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%); inference latency is primary stated limitation; targets zero-shot real-robot execution. URDF-DiT tests whether in-loop FK conditioning outperforms Dream2Act's approach (B) for synthetic training data quality.\",\n    \"EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields (arXiv:2605.06192, May 2026) — primary concurrent work; injects KVAF kinematic heatmaps into Wan 2.2 via event-aware bidirectional dual-stream fusion; WorldArena benchmark for arm manipulation; requires joint fine-tuning of both branches; no policy training pipeline. Note: 'EA' = Event-Aware, not Embodiment-Aware. URDF-DiT differentiators are empirically testable: full-body 29 DoF vs. arm manipulation (Ablation B), ControlNet frozen backbone vs. joint fine-tuning (~40% fewer trainable parameters), explicit IDM→policy pipeline.\",\n    \"VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis (arXiv:2604.09330, April 2026) — jointly denoises video+action via flow matching for tabletop arm manipulation (7–16 DoF); 45% on AgiBot G1 dual-arm grasping vs. 8% IDM baseline; no URDF kinematic constraints; acknowledged limitation: 'video branch not influenced by action branch.' URDF-DiT's FK heatmap injection directly addresses this limitation while extending to 29+ DoF.\",\n    \"EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards (arXiv:2603.17808, March 2026) — executability via RL post-training using IDM-derived reward signals; evaluates bimanual tabletop. Key distinction: EVA = soft learned reward constraint; URDF-DiT = hard geometric FK constraint at every diffusion step. ICLR 2027 ablation directly compares these two executability enforcement approaches.\",\n    \"FlowAct-R1: Towards Interactive Humanoid Video Generation (arXiv:2601.10103, January 2026) — real-time interactive digital human character animation via MMDiT chunkwise diffusion with audio/text-based full-body control at 25fps; targets NPC-style animated digital humans (lip-sync, expressions, body gestures), not physical robot embodiment; no URDF kinematic constraints, no robot joint angles, no IDM policy extraction pipeline. Differentiation: character animation interactive use case vs. offline robot training data generation.\",\n    \"KStar Diffuser (arXiv:2503.10743, CVPR 2025) — URDF-parsed spatial-temporal graph with differentiable FK for bimanual action diffusion (68.2% vs. 33.9% for PerAct2); policy layer not video synthesis; complementary.\",\n    \"Kinema4D (arXiv March 2026, NTU) — URDF-driven FK for 4D pointmap scene realism; not policy-data generation or DiT attention injection.\",\n    \"Controllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026) — validates per-frame 2D skeleton-sequence conditioning in video diffusion for human motion synthesis; closest video-generation analogue to URDF-DiT's conditioning mechanism; targets human motion not robot URDF kinematics or policy extraction.\",\n    \"HumanoidBench (arXiv:2403.10506, 2024) — 27 tasks (H1/Digit, MuJoCo); ICLR 2027 cross-embodiment evaluation target.\",\n    \"RoboCasa365 (arXiv:2603.04356, ICLR 2026) — 365 kitchen tasks with humanoid support; ICLR 2027 household generalization evaluation.\",\n    \"X-Humanoid (arXiv Dec 2025); MITTY (arXiv 2025); G-DReaM (arXiv 2025)\"\n  ],\n  \"description\": \"⚠️ USER REQUIREMENT TRADEOFF: The user required evaluation on three platforms — Isaac Lab G1 locomanipulation, HumanoidBench whole-body tasks, and RoboCasa365 humanoid kitchen. The CoRL 2026 submission covers ONLY Isaac Lab G1 locomanipulation (1 of 3). The user must decide: (A) target CoRL 2026 with partial benchmark coverage now + ICLR 2027 for full coverage; or (B) skip CoRL 2026 and target ICLR 2027 directly with full coverage from the start. This is not a footnote — it is a deliberate scope decision.\\n\\nURDF-DiT addresses a specific, empirically testable question: is full-body kinematic conditioning throughout the denoising process necessary for high-quality IDM training data generation on whole-body contact tasks? The paper tests this via two ablations that together constitute its primary scientific contribution: (A) downstream Isaac Lab G1 policy success rate from URDF-DiT-generated trajectories vs. vanilla Wan 2.2 + post-hoc URDF-IK trajectories (same IDM, same policy training — tests in-loop vs. post-hoc kinematic enforcement); (B) full-body 29 DoF conditioning vs. end-effector-only conditioning (tests whether the full kinematic chain matters for whole-body contact task video generation). The second ablation directly and empirically differentiates URDF-DiT from EA-WM's arm-only kinematic heatmap approach.\\n\\nKey technical points: (1) Dream2Act (arXiv:2603.19709) generates in robot-native VISUAL space (hallucinating G1 body via Seedance 2.0) then applies post-generation URDF-IK for kinematic extraction — URDF-DiT tests whether in-loop FK conditioning outperforms this extraction approach for synthetic training data; (2) EA-WM (arXiv:2605.06192, Event-Aware, not Embodiment-Aware) validates in-loop KVAF heatmap injection for arm manipulation — URDF-DiT extends to 29 DoF full-body with ControlNet-style frozen backbone (no joint fine-tuning, ~40% fewer trainable parameters) and adds the IDM→policy pipeline; (3) FlowAct-R1 (arXiv:2601.10103) is audio/text-driven digital human character animation (NPCs), not physical robot URDF kinematics or policy extraction.\\n\\nDay 14 CoRL/ICLR 2027 pivot criteria (concrete): Submit to CoRL if URDF-DiT policy success ≥ 20% AND ≥ 5 pp improvement over vanilla baseline AND joint-limit violation rate ≤ 10%. Pivot to ICLR 2027 if URDF-DiT fails to exceed baseline by ≥ 5 pp, or absolute success < 15%, or violation rate > 15% (all GPU investment preserved for ICLR 2027). FK residual consistency loss enforces kinematic geometry in generated outputs; visual domain gap addressed separately via domain-randomized Isaac Lab rendering during IDM training — two distinct mechanisms for two distinct problems.\",\n  \"project_name\": \"urdf_dit_loco_policy\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"CRITICAL NEW ISSUE — BRIDGEV2W (arXiv:2602.03793, February 2026) NOT CITED: Independent verification confirms BridgeV2W explicitly 'converts coordinate-space actions into pixel-aligned embodiment masks rendered from the URDF and camera parameters. These masks are then injected into a pretrained video generation model via a ControlNet-style pathway.' This paper — applied to single-arm (DROID) and dual-arm (AgiBot-G1) robots — is architecturally nearly identical to URDF-DiT's core contribution (ControlNet + URDF conditioning for robot video DiT). A CoRL reviewer familiar with the embodied world model literature will immediately flag this omission. URDF-DiT must cite BridgeV2W and differentiate explicitly on: (a) full-body humanoid 29 DoF vs. arm/dual-arm scope; (b) Gaussian joint-position heatmaps from FK (continuous per-joint scalar fields encoding kinematic structure) vs. BridgeV2W's pixel-aligned binary embodiment masks (which encode link occupancy but not individual joint angles); (c) IDM training data generation as the downstream objective vs. BridgeV2W's policy evaluation and goal-conditioned planning. With BridgeV2W now in the landscape alongside EA-WM, the claim that URDF-DiT introduces ControlNet + URDF injection into video DiT is no longer defensible — the paper's novelty must be repositioned as 'full-body humanoid kinematic conditioning with Gaussian heatmaps for IDM training data generation,' not as a novel conditioning architecture.\", \"VAG 'EXPLICITLY ACKNOWLEDGES' CHARACTERIZATION REQUIRES PRECISION: The proposal states VAG 'explicitly acknowledges the video branch has not been influenced by the action branch.' Independent review of the VAG abstract finds it describes 'synchronized denoising in both branches' with 'adaptive 3D pooling to transfer compact global video context to the action branch' — suggesting the design routes video features to actions but not necessarily the reverse. If this quote comes from an ablation or analysis section in the full paper, it must be cited with section/page reference. If it is the proposal author's inference, it must be rewritten: 'VAG's architecture routes video context to the action branch via 3D pooling but does not inject action signals back into the video denoising process, leaving a video-action coupling gap that explicit FK heatmap injection in URDF-DiT addresses.' Misquoting a competitor's paper is a fast track to rejection at CoRL.\", \"NOVELTY BAR AT CORL IS NOW CRITICALLY THIN: With EA-WM (in-loop kinematic heatmap injection into Wan 2.2 cross-attention, May 2026) and BridgeV2W (ControlNet + URDF embodiment mask injection into pretrained video DiT, February 2026) both uncited-until-now, the paper's architectural contribution is no longer novel. The remaining novelty is exclusively in (a) full-body humanoid scope (29 DoF vs. arm-only) and (b) IDM-to-policy pipeline. Point (b) is primarily an engineering contribution. Point (a) is an empirical claim that depends on Ablation B showing meaningful improvement (≥5pp). If Ablation B shows marginal benefit from full-body vs. end-effector conditioning, the paper has no defensible novel claim over the combined EA-WM + BridgeV2W prior work. The proposal's 'submit with reframing' contingency (Ablation B < 3pp → 'end-effector conditioning suffices') would produce a paper saying 'our novel extension doesn't help' — which is not a CoRL-level contribution. This risk must be assessed before committing to the CoRL trajectory.\", \"CORL EVALUATION STILL 1 OF 3 USER-REQUIRED BENCHMARKS: This is flagged explicitly in the proposal (which is correct), but it remains a hard constraint — the CoRL submission does not satisfy the user's stated requirement of evaluating on Isaac Lab G1 locomanipulation, HumanoidBench, AND RoboCasa365. The proposal correctly identifies this as an explicit user decision, but the review record should note it is unresolved from the user's perspective until they make the opt-in/out decision. Without user confirmation, the CoRL path should be treated as provisional.\"]\nFeedback: Round 6 correctly resolved all four Round 5 issues: user tradeoff is explicitly and prominently flagged, FlowAct-R1 is in the landscape with a one-line differentiation, Ablation B is the primary scientific claim, and Day 14 pivot criteria have concrete numeric thresholds. The proposal is structurally sound. Two targeted fixes are required:\n\n1. **URGENT: Add BridgeV2W to the landscape and reposition the novelty claim.** BridgeV2W (arXiv:2602.03793, February 2026) uses 'coordinate-space actions → pixel-aligned embodiment masks rendered from URDF → ControlNet-style injection into pretrained video DiT.' This is the same architecture as URDF-DiT. Add a landscape entry: 'BridgeV2W (arXiv:2602.03793, Feb 2026) uses URDF-rendered pixel-aligned embodiment masks injected via ControlNet pathway into a pretrained video DiT for arm/dual-arm manipulation video generation and policy evaluation. URDF-DiT differentiates on three axes: (a) full-body humanoid 29 DoF (vs. arm/dual-arm) with Gaussian joint-position heatmaps encoding per-joint kinematic structure rather than binary link occupancy masks; (b) whole-body contact interaction tasks (pick-and-place with locomotion, ball-kicking) vs. arm manipulation; (c) IDM training data generation pipeline vs. policy evaluation and goal-conditioned planning.' Then revise the introduction to acknowledge that ControlNet + URDF conditioning for robot video DiTs is now an established approach (citing EA-WM and BridgeV2W) and position URDF-DiT as the first application of this approach to full-body humanoid whole-body contact tasks with an explicit IDM training data generation objective.\n\n2. **Fix the VAG 'explicitly acknowledges' characterization.** Change to: 'VAG's architecture routes compact global video context to the action branch via adaptive 3D pooling, but does not inject action signals back into the video denoising process — a design gap URDF-DiT addresses via bidirectional FK heatmap conditioning.' Do not use a direct quote unless you can cite the specific section where VAG uses those exact words.\n\n3. **Assess the Ablation B risk explicitly.** Given EA-WM + BridgeV2W now both in the landscape, the paper needs Ablation B to be strongly positive (≥5pp) to have a defensible novel claim at CoRL. Add to the pivot criteria: if Ablation B < 5pp AND BridgeV2W is the closest prior, the paper's CoRL-level novelty is insufficient — pivot to ICLR 2027 with full benchmark coverage and a deeper ablation suite (also including a direct comparison against BridgeV2W's embodiment mask approach).\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.0 到 3.2，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T12:57:50.580Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T12:57:50.580Z",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-10T12:57:50.599Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "URDF-DiT: Does Full-Body Kinematic Conditioning Throughout Denoising Improve IDM Training Data for Humanoid Whole-Body Contact Tasks?",
  "core_problem": "The central empirical question: does conditioning a video diffusion model on all 29 DoF of a humanoid robot's URDF forward kinematics throughout the entire denoising process — enforcing joint-limit compliance in every generated frame via structured Gaussian heatmaps injected into DiT cross-attention — yield measurably better IDM training trajectories for whole-body contact interaction tasks than (A) post-hoc kinematic recovery applied after unconstrained video generation, or (B) end-effector-only conditioning (~5 DoF wrist/hand positions)? This question is directly testable via two ablations — (A) URDF-DiT vs. vanilla Wan 2.2 + post-hoc URDF-IK (same IDM, same downstream policy training) and (B) 29 DoF full-body FK heatmaps vs. end-effector-only heatmaps — with downstream Isaac Lab G1 pick-and-place policy success rate as the primary evaluation metric.\n\n⚠️ USER REQUIREMENT TRADEOFF — EXPLICIT FLAG: The user specified three required evaluation platforms: Isaac Lab G1 locomanipulation, HumanoidBench whole-body tasks, and RoboCasa365 humanoid kitchen. The CoRL 2026 scoped submission covers ONLY Isaac Lab G1 locomanipulation (1 of 3 required benchmarks). HumanoidBench and RoboCasa365 are deferred entirely to ICLR 2027. The user should make an explicit decision: (option A) target CoRL 2026 with 1-of-3 benchmark coverage and full results on all three platforms at ICLR 2027; (option B) skip CoRL 2026 entirely and target ICLR 2027 from the start with full user-required benchmark coverage. This tradeoff is presented explicitly, not embedded quietly in venue notes.\n\nThree coupled sub-problems require simultaneous solution: (1) EA-WM (arXiv:2605.06192) validates that KVAF kinematic heatmap injection into Wan 2.2 cross-attention enforces kinematic consistency for arm manipulation — but evaluates arm tasks only (WorldArena benchmark), requires joint fine-tuning of both branches, and produces no policy training output; (2) Dream2Act (arXiv:2603.19709) generates in robot-native visual space (hallucinating the G1 body, not retargeting from human video) and achieves 37.5% on G1 whole-body contact tasks — but applies kinematic recovery POST-generation via constrained URDF-IK (converting pixel-space poses to joint angles after all video frames are produced), and targets zero-shot real-robot execution rather than synthetic training data generation; (3) VAG (arXiv:2604.09330) jointly denoises video and action via flow matching but explicitly acknowledges 'the video branch has not been influenced by the action branch' and provides no kinematic constraints. URDF-DiT directly tests whether the in-loop conditioning approach (vs. Dream2Act's post-hoc IK) and the full-body scope (vs. EA-WM's arm-only conditioning and VAG's unconstrained generation) are necessary for high-quality IDM training data on whole-body contact tasks — an empirical question with a clear experimental design.",
  "opportunity": "GR00T-Dreams/DreamGen (2025) validated the video-diffusion → IDM pipeline for tabletop manipulation. Dream2Act (arXiv:2603.19709, March 2026) extended to full-body G1 whole-body contact interaction by generating video in robot-native visual space — hallucinating the G1 robot body to achieve morphological consistency — then applying post-generation kinematic recovery: (a) native 2D pose estimation, (b) 2D-to-3D lifting, (c) URDF-constrained IK to convert pixel-space poses to joint trajectories. Dream2Act achieves 37.5% overall success across four whole-body contact tasks (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%) vs. 0% for conventional retargeting baselines; inference latency is its primary stated limitation. Dream2Act's two distinct components — (A) robot-native video generation modality and (B) post-generation URDF-constrained IK for kinematic extraction — are the baseline against which URDF-DiT's in-loop conditioning is tested. The hypothesis: conditioning on FK heatmaps throughout denoising prevents kinematically infeasible frame transitions during generation rather than correcting them afterward, producing cleaner IDM training trajectories.\n\nEA-WM (arXiv:2605.06192, May 7 2026) validates that in-loop kinematic heatmap injection into Wan 2.2 cross-attention enforces kinematic consistency — using KVAFs (Gaussian heatmaps at projected joint/end-effector positions) via event-aware bidirectional dual-stream fusion. But EA-WM evaluates arm manipulation only (WorldArena benchmark), requires joint fine-tuning of both video and kinematic branches, and produces no policy training output. URDF-DiT extends this approach to the full-body 29 DoF case with a ControlNet-style frozen backbone (more compute-efficient, ~40% fewer trainable parameters) and adds the IDM→policy pipeline — but critically, the full-body extension is not assumed: it is empirically tested via the 29 DoF vs. end-effector-only ablation, which is the paper's primary scientific finding.\n\nVAG (arXiv:2604.09330, April 2026) introduces dual-stream flow matching jointly denoising video and action for arm manipulation (7–16 DoF, 45% on AgiBot G1 dual-arm grasping vs. 8% IDM baseline) but explicitly acknowledges the video-action coupling gap. EVA (arXiv:2603.17808, March 2026) enforces executability via learned IDM reward signals (RL post-training, soft constraint) on bimanual tabletop tasks — distinct from URDF-DiT's hard geometric constraint at every diffusion step.\n\n⚠️ USER REQUIREMENT TRADEOFF: The user required evaluation on Isaac Lab G1 locomanipulation, HumanoidBench, and RoboCasa365. CoRL 2026 covers only Isaac Lab G1 locomanipulation. Full benchmark coverage requires ICLR 2027. The user must decide between CoRL 2026 (fast, partial coverage) and ICLR 2027 (full coverage). This is not a minor footnote — it is a deliberate scope decision with direct implications for whether the work meets the user's original requirements at submission time.\n\nVENUE/TIMELINE NOTE: Today is May 10, 2026. CoRL 2026 deadline is May 29 — 19 days away. CoRL 2026 is feasible ONLY in auto-research mode with 8+ H100s available from Day 1, scoped to Isaac Lab G1 locomanipulation + Dream2Act ball kicking contextual comparison, with 2 ablations and a concrete Day 14 decision gate (see resource_estimate). Manual mode (4–6 months) and HIL mode (5–8 weeks) are incompatible with CoRL 2026.",
  "landscape": "GR00T-Dreams/DreamGen (arXiv 2025): fine-tunes Cosmos-Predict2 with language conditioning; extracts pseudo-actions via IDM or latent action model. No URDF kinematic constraint. Tabletop manipulation only.\n\nDream2Act (arXiv:2603.19709, March 2026): Two distinct components must be distinguished — (A) VIDEO GENERATION MODALITY: generates in robot-native visual space by hallucinating the G1 robot body (not retargeting from human video) using Seedance 2.0, achieving morphological consistency; (B) KINEMATIC EXTRACTION: post-generation pipeline applying native 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK to convert pixel-space poses to joint trajectories. Achieves 37.5% overall success across four whole-body contact interaction benchmarks (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%) vs. 0% for conventional retargeting. Primary stated limitation is inference latency as an offline planner. Dream2Act targets zero-shot real-robot execution; URDF-DiT targets synthetic IDM training data generation — complementary goals. URDF-DiT tests whether conditioning the video branch on FK heatmaps throughout denoising (in-loop) improves IDM training data quality relative to Dream2Act's approach (B), post-generation URDF-IK.\n\nEA-WM (arXiv:2605.06192, May 2026): 'EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields' — injects Kinematic-to-Visual Action Fields (KVAF: Gaussian heatmaps at projected end-effector/joint locations) via event-aware bidirectional dual-stream fusion into Wan 2.2; evaluates on WorldArena benchmark for arm manipulation tasks; requires joint fine-tuning of both video and kinematic streams; no policy training output (action recovery detection rate ~0.45). Note: 'EA' = Event-Aware, not Embodiment-Aware. URDF-DiT differentiates on three empirically testable axes: (a) full-body 29+ DoF vs. arm manipulation — tested by full-body vs. end-effector ablation; (b) ControlNet-style frozen backbone vs. joint fine-tuning — ~40% fewer trainable parameters; (c) explicit IDM→policy pipeline vs. no policy output.\n\nVAG (arXiv:2604.09330, April 2026): dual-stream video-action generation using flow matching for tabletop arm manipulation (7–16 DoF); 45% on AgiBot G1 dual-arm grasping vs. 8% ResNet+IDM baseline; no URDF kinematic constraints; authors explicitly acknowledge 'video branch not influenced by action branch'; no full-body humanoid evaluation. URDF-DiT's in-loop FK heatmap injection directly addresses VAG's stated limitation while extending to 29+ DoF whole-body tasks.\n\nEVA (arXiv:2603.17808, March 2026): closes executability gap via RL post-training using IDM-derived reward signals penalizing embodiment violations (joint-limit violations, velocity/acceleration/jerk penalties); evaluates on RoboTwin 2.0 bimanual manipulation. Key distinction: EVA = learned IDM reward (soft executability constraint via RL post-training); URDF-DiT = explicit geometric URDF FK heatmaps (hard geometric constraint injected at every diffusion step). EVA evaluates bimanual tabletop; URDF-DiT targets full-body 29+ DoF contact interaction.\n\nFlowAct-R1 (arXiv:2601.10103, January 2026): 'FlowAct-R1: Towards Interactive Humanoid Video Generation' — real-time interactive digital human character animation via MMDiT chunkwise diffusion with audio/text-based full-body control at 25fps; targets NPC-style animated digital humans for real-time interaction (lip-sync, facial expressions, body gestures), not physical robot embodiment; no URDF kinematic structure, no physical robot joint constraints, no IDM policy extraction pipeline. Differentiation: interactive character animation use case vs. offline robot training data generation; audio/text conditioning vs. geometric URDF FK heatmaps.\n\nKStar Diffuser (arXiv:2503.10743, CVPR 2025): URDF-parsed spatial-temporal graph with differentiable FK for bimanual arm action diffusion (68.2% ± 2.1 success with 100 demos vs. 33.9% for PerAct2); operates at the policy/action layer not video synthesis — complementary to URDF-DiT rather than competing.\n\nKinema4D (arXiv March 2026, NTU): URDF-driven FK for 4D pointmap conditioning for scene realism; not policy-data generation or video diffusion attention-layer injection.\n\nControllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026): cascaded text-to-2D-skeleton → skeleton-to-video pipeline validates per-frame 2D pose-sequence conditioning in video diffusion for human motion synthesis — closest video-generation analogue to URDF-DiT's conditioning mechanism, but targets human motion not robot URDF kinematics or policy extraction.\n\nX-Humanoid (arXiv Dec 2025): replaces human with humanoid in video via Wan 2.2; no URDF constraint injection. MITTY (arXiv 2025): human-to-robot video diffusion without kinematic enforcement. G-DReaM (arXiv 2025): graph-conditioned diffusion for cross-embodiment motion retargeting on motion sequences, not RGB video.\n\nHumanoidBench (arXiv:2403.10506, 2024): 27 whole-body tasks (H1/Digit robots, MuJoCo); deferred to ICLR 2027 full paper. RoboCasa365 (arXiv:2603.04356, ICLR 2026): 365 kitchen tasks with humanoid support; deferred to ICLR 2027 full paper.",
  "approach": "PRIMARY SCIENTIFIC CLAIM (reframed to lead the paper): The paper's central empirical question — presented as a hypothesis test, not merely a system description — is whether full-body kinematic conditioning throughout denoising is NECESSARY for whole-body contact task IDM training data generation, not merely sufficient. Two ablations directly test this:\n\nABLATION A (primary, vs. Dream2Act approach B): Does in-loop FK conditioning produce better IDM training trajectories than post-hoc URDF-IK applied to unconstrained video? Setup: same IDM, same downstream Isaac Lab G1 policy training procedure, same evaluation benchmark — only the video source differs. URDF-DiT-generated videos vs. vanilla Wan 2.2 videos post-processed with URDF-IK (the same IK pipeline used in Dream2Act's kinematic extraction stage). This directly measures whether conditioning throughout denoising outperforms correcting afterward.\n\nABLATION B (central scientific claim, vs. EA-WM conditioning scope): Does full-body 29 DoF conditioning (pelvis, legs, torso, arms, hands) improve IDM training data quality over end-effector-only conditioning (~5 DoF wrist/hand positions)? Setup: same IDM, same downstream policy evaluation — only the conditioning scope differs. For whole-body CONTACT tasks (ball kicking, pick-and-place with locomotion), the hypothesis is that leg and torso kinematics during approach and weight-shifting phases affect interaction quality in ways that end-effector-only conditioning cannot capture. Ablation B is the paper's STRONGEST SCIENTIFIC CLAIM and the primary differentiator from EA-WM — if full-body conditioning yields ≥5 pp improvement over end-effector-only on the downstream policy success rate, this empirically validates that the 29 DoF extension is necessary, not incremental. If the improvement is < 3 pp, the paper should be reframed as 'end-effector conditioning is sufficient for whole-body tasks, simplifying the conditioning design' — still a valid and publishable empirical finding.\n\nARCHITECTURE: URDF-DiT uses a ControlNet-style conditioning module — Wan 2.2 backbone weights fully frozen; only the FK-heatmap encoder and zero-conv injection layers are trained — that encodes per-frame G1 URDF forward-kinematics outputs (all 29 DoF, projected to the camera plane via differentiable FK) as structured Gaussian joint-position heatmaps and injects them into the cross-attention layers of the Wan 2.2 DiT. Unlike EA-WM's event-aware bidirectional dual-stream fusion (requiring joint fine-tuning of both video and kinematic branches), URDF-DiT's ControlNet-style design concentrates all learning in the conditioning module, reducing trainable parameters ~40% versus EA-WM's architecture — enabling the full pipeline within ≤200 H100-hours. Full-body G1 scope (29 DoF: pelvis, legs, torso, arms, hands) is the embodiment extension under test in Ablation B.\n\nDIFFERENTIATING DREAM2ACT PRECISELY: Dream2Act operates as follows: (A) video generation modality = robot-native visual space (Seedance 2.0 hallucinating the G1 body for morphological consistency — not retargeting from human video); (B) kinematic extraction = post-generation pipeline applying 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK (applied AFTER all video frames are generated). URDF-DiT vs. Dream2Act is not a comparison of visual generation approach — both generate in robot-native-compatible space — but specifically a test of whether kinematic constraints applied IN-LOOP during denoising (URDF-DiT) produce better training data than constraints applied POST-GENERATION (Dream2Act's approach B), for the synthetic data use case.\n\nJoint-angle sequences are sampled from an Isaac Lab G1 motion library covering locomotion primitives and upper-body reach plans, projected onto the camera plane, and encoded as per-frame kinematic tokens injected into DiT cross-attention.\n\nFK RESIDUAL LOSS: A per-frame FK residual consistency loss penalizes deviations between joint positions in generated video frames and URDF FK predictions from the conditioning signal. This is a kinematic consistency mechanism operating on geometric structure — reducing temporal joint jitter, preventing joint-limit violations during denoising. It is NOT a visual domain gap bridge. The visual appearance domain gap between Wan 2.2 outputs and Isaac Lab rendering is separately addressed via domain-randomized Isaac Lab rendering during IDM training (sampling lighting, camera noise, surface material variation to statistically overlap with Wan 2.2's output distribution). Two distinct mechanisms for two distinct problems.\n\nThe sim-bootstrapped IDM is trained on (frame_t, frame_{t+k}, joint-velocity) tuples from G1 Isaac Lab rollouts under domain-randomized conditions, then applied zero-shot to URDF-DiT-generated videos. If domain gap remains too large (joint-limit violation rate >15% in generated videos at the 3-day checkpoint), a contingency IDM adapter fine-tuned on ~200 URDF-DiT frame pairs matched to Isaac Lab rollouts via kinematic alignment (~8h additional compute) activates.\n\nEVALUATION STRATEGY:\n\n(1) CoRL 2026 scoped (2 benchmarks, 2 ablations): Isaac Lab G1 locomanipulation pick-and-place (primary); Dream2Act ball kicking (contextual comparison — 40% success, distinct use case: zero-shot real-robot execution vs. synthetic training data); Ablation A (in-loop URDF-DiT vs. post-hoc vanilla Wan 2.2 + URDF-IK); Ablation B (29 DoF full-body vs. end-effector-only). NOTE: covers 1 of 3 user-required benchmarks.\n\n(2) ICLR 2027 full paper (all user-required platforms): Isaac Lab G1 locomanipulation (multi-task: pick-and-place, reaching, pick-navigate-place); HumanoidBench H1 whole-body (carry + cabinet); RoboCasa365 humanoid kitchen (pick-and-place in kitchen); Dream2Act ball kicking + bag punching; Ablations A and B plus: ControlNet-style frozen backbone vs. EA-WM-style event-aware bidirectional fusion; URDF-DiT geometric FK conditioning vs. EVA-style learned IDM reward.",
  "resource_estimate": {
    "corl2026_scoped_auto": {
      "gpu_hours": "~130h H100 total compute (compressed to ~12–18h wall clock on 8 H100s)",
      "gpu_utilization": "Near-zero idle (~88–92% effective utilization) — agent queues IDM training immediately after ControlNet training checkpoint and runs evaluation generation in parallel",
      "timeline": "19 days (May 10 → May 29, 2026 CoRL deadline) with 8+ H100s available from Day 1",
      "team": "0 (4h Day 1 setup: Isaac Lab G1 motion library, domain-randomized rendering, URDF-DiT scaffold, evaluation harness)",
      "estimated_gpu_cost": "~$416 (130h × $3.20/hr) spread across 8 GPUs",
      "day_by_day_plan": "Day 1: env setup (Isaac Lab G1, Wan 2.2 base, eval harness). Days 2–3: implement FK heatmap encoder + zero-conv injection layers for Wan 2.2 cross-attention; simultaneously implement vanilla Wan 2.2 + post-hoc URDF-IK baseline for Ablation A. Days 3–5: ControlNet module training 35–50h GPU compute (~5–7h wall clock on 8 H100s). Days 4–5: IDM training in parallel (~25h GPU, ~3h wall clock). Days 5–8: generate 200 evaluation videos from URDF-DiT and 200 from vanilla Wan 2.2 baseline (~35h GPU, ~5h wall clock). Days 7–11: Isaac Lab G1 policy evaluation on trajectories from both sources (simulation rollouts — wall-clock bottleneck: parallel episode execution). Days 8–12: Ablation B (29 DoF vs. end-effector-only, same IDM, same downstream policy evaluation) + Dream2Act ball kicking contextual comparison. Days 12–14: results analysis and Day 14 DECISION GATE (see pivot_criteria below). Days 14–19: agent-assisted LaTeX drafting of all paper sections (introduction, related work, method, experiments) — auto mode includes full concurrent section generation starting Day 14.",
      "pivot_criteria": {
        "description": "Day 14 decision gate with concrete metric thresholds. Calibration anchor: Isaac Lab G1 pick-and-place with Robomimic from clean teleoperation demos achieves 92% success; IDM extraction from generated video will yield substantially lower rates due to visual noise and trajectory imprecision. Thresholds are set relative to the vanilla Wan 2.2 + post-hoc URDF-IK baseline, not absolute performance.",
        "submit_to_corl": {
          "condition": "ALL of the following: (1) URDF-DiT trained policy success rate ≥ 20% on Isaac Lab G1 pick-and-place (establishes non-trivial absolute performance from generated data); (2) URDF-DiT > vanilla Wan 2.2 + post-hoc URDF-IK baseline by ≥ 5 percentage points (establishes in-loop conditioning advantage — Ablation A is positive); (3) joint-limit violation rate in URDF-DiT generated videos ≤ 10% (validates FK conditioning is working geometrically)",
          "strong_submission_additionally": "Full-body 29 DoF conditioning ≥ end-effector-only conditioning by ≥ 5 pp on downstream policy success (Ablation B strongly positive — validates the 29 DoF scope claim empirically)"
        },
        "submit_with_reframing": {
          "condition": "Ablation A positive (URDF-DiT ≥ baseline + 5 pp) BUT Ablation B shows < 3 pp improvement from full-body vs. end-effector-only conditioning — reframe as 'end-effector conditioning suffices; full 29 DoF conditioning adds marginal benefit for pick-and-place.' Still a valid CoRL contribution if absolute performance (condition 1) and FK violation rate (condition 3) are met.",
          "note": "Negative ablation B result is publishable as an empirical finding, not a failure — it simplifies the design recommendation for the community."
        },
        "pivot_to_iclr_2027": {
          "condition": "ANY of the following: (1) URDF-DiT fails to exceed baseline by ≥ 5 pp (Ablation A inconclusive — primary claim unsupported); (2) joint-limit violation rate > 15% in URDF-DiT generated videos (FK conditioning not working — triggers IDM adapter contingency, but if adapter also fails, implementation issue requires debugging time incompatible with May 29 deadline); (3) absolute policy success < 15% (both URDF-DiT and baseline yield near-zero performance — IDM domain gap too large for 19-day timeline, requires more investigation); (4) contingency IDM adapter required AND results still negative after adapter training",
          "note": "ICLR 2027 pivot preserves all GPU investment — same implementation, full benchmark coverage (all 3 user-required platforms), full ablation suite. Pivot to ICLR 2027 is not a failure; it is the correct decision if CoRL results do not meet the above thresholds."
        }
      },
      "scope": "2 benchmarks (Isaac Lab G1 locomanipulation + Dream2Act ball kicking contextual comparison), 2 ablations (A: in-loop URDF-DiT vs. post-hoc vanilla Wan 2.2 + URDF-IK; B: full-body 29 DoF vs. end-effector-only conditioning). HumanoidBench and RoboCasa365 deferred to ICLR 2027. NOTE: covers 1 of 3 user-required benchmarks.",
      "feasibility_risk": "HIGH. Estimated 60–70% probability of obtaining submittable results by May 29 in auto mode. Key risks: (1) ControlNet training non-convergence adds 1–2 days; (2) IDM domain gap exceeds FK residual loss + domain randomization, triggering 8h contingency adapter; (3) Isaac Lab simulation evaluation wall-clock bottleneck if environment resets are slow. Day 14 decision gate with concrete thresholds (above) provides an unambiguous pivot trigger.",
      "requirement": "8+ H100s available from Day 1 (May 10). If fewer than 8 GPUs are available, wall-clock time increases proportionally and May 29 deadline becomes infeasible — target ICLR 2027."
    },
    "manual": {
      "note": "ICLR 2027 full paper mode (full coverage of all 3 user-required benchmarks). Incompatible with CoRL 2026 deadline.",
      "gpu_hours": "~130–150h H100 (sensitivity-adjusted: ControlNet training 35–70h + IDM 25h + video generation/eval 35h + ablations 25h + data prep 10h)",
      "gpu_utilization": "HIGH idle rate (~40–50% effective utilization) — sequential experiment launches and human debugging",
      "timeline": "4–6 months (ICLR 2027 submission ~October 2026)",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$416–$480 (130–150h × $3.20/hr)",
      "breakdown": "ControlNet module training: 35–70h; IDM training (Isaac Lab G1 rollouts + domain-randomized rendering): ~25h; Video generation + evaluation (Isaac Lab + HumanoidBench + RoboCasa365 + Dream2Act contextual): ~35h; Ablations A, B, ControlNet-vs.-bidirectional-fusion, geometric-FK-vs.-EVA-RL: ~25h; Data prep: ~10h. At 70h worst case for ControlNet: total ~165h, within 200h cap.",
      "benchmark_coverage": "FULL — Isaac Lab G1 locomanipulation, HumanoidBench H1 whole-body, RoboCasa365 humanoid kitchen. Meets all 3 user-required benchmarks."
    },
    "human_in_loop": {
      "note": "ICLR 2027 full paper mode. Incompatible with CoRL 2026 deadline.",
      "gpu_hours": "~160h H100",
      "gpu_utilization": "Moderate (~60–65% effective utilization)",
      "timeline": "5–8 weeks (ICLR 2027 submission ~October 2026)",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "~$150–300 (Opus, ~1,500–2,000 conversation turns)",
      "estimated_gpu_cost": "~$512 (160h × $3.20/hr)",
      "risk_note": "Human oversight detects IDM domain-gap failure at 2-week checkpoint, activates contingency IDM adapter (~8h additional compute) before remaining budget is spent.",
      "benchmark_coverage": "FULL — all 3 user-required benchmarks."
    },
    "auto_research": {
      "note": "ICLR 2027 full paper mode (all user-required evaluation platforms). For CoRL 2026 scoped version, see corl2026_scoped_auto above.",
      "gpu_hours": "~200h H100 (covers full ablation suite: Ablation A, Ablation B, ControlNet-style vs. EA-WM bidirectional fusion, geometric FK vs. EVA-style RL reward, IDM backbone comparisons, FK heatmap resolution variants)",
      "gpu_utilization": "Near-zero idle (~88–92% effective utilization)",
      "timeline": "1–2 weeks with 8+ H100s; 3–4 weeks on 4 GPUs",
      "team": "0 (initial setup ~4h)",
      "claude_api_cost": "~$400–700 (Opus, ~4,000–7,000 turns)",
      "estimated_gpu_cost": "~$640 (200h × $3.20/hr)",
      "benchmark_coverage": "FULL — all 3 user-required benchmarks (Isaac Lab G1 locomanipulation multi-task, HumanoidBench H1 whole-body, RoboCasa365 humanoid kitchen).",
      "risk_note": "Automated evaluation harness must include per-frame kinematic consistency checks (FK residual, joint-limit violation rate, temporal flicker score) alongside task success. If FK residual loss is insufficient for IDM domain transfer (joint-limit violation rate >15%), agent triggers IDM adapter contingency (~8h) automatically."
    }
  },
  "target_venues": [
    "CoRL 2026 (paper deadline May 29, 2026 — 19 days from today): FEASIBLE only in auto-research mode with 8+ H100s available starting May 10. ⚠️ COVERS ONLY 1 OF 3 USER-REQUIRED BENCHMARKS (Isaac Lab G1 locomanipulation only; HumanoidBench and RoboCasa365 deferred to ICLR 2027). Scoped to 2 ablations: (A) in-loop URDF-DiT vs. post-hoc vanilla Wan 2.2 + URDF-IK extraction; (B) full-body 29 DoF vs. end-effector-only conditioning — the paper's primary scientific claim. Day 14 decision gate: submit if URDF-DiT ≥ 20% success AND ≥ 5 pp improvement over baseline AND joint-limit violation rate ≤ 10%; pivot to ICLR 2027 otherwise. Estimated 60–70% probability of submittable results by deadline. If Day 14 shows negative results, same implementation pivots to ICLR 2027 with no wasted GPU investment.",
    "ICLR 2027 (expected submission deadline ~October 2026; official announcement pending at iclr.cc): RECOMMENDED if full user-required benchmark coverage is the priority. Covers all 3 required platforms (Isaac Lab G1 locomanipulation, HumanoidBench H1 whole-body, RoboCasa365 humanoid kitchen) and full ablation suite (A, B, ControlNet-vs.-bidirectional-fusion, geometric-FK-vs.-EVA-RL). All operation modes (manual 4–6 months, HIL 5–8 weeks, auto 1–2 weeks on 8 H100s) are compatible.",
    "CoRL 2027 (fallback if ICLR 2027 results are negative)"
  ],
  "level": "solid",
  "key_references": [
    "DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories (arXiv 2025)",
    "Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis / Dream2Act (arXiv:2603.19709, March 2026) — TWO DISTINCT COMPONENTS: (A) video generation modality: robot-native visual space by hallucinating G1 robot body via Seedance 2.0 (not retargeting from human video); (B) kinematic extraction: post-generation pipeline via 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK. Achieves 37.5% success (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%); inference latency is primary stated limitation; targets zero-shot real-robot execution. URDF-DiT tests whether in-loop FK conditioning outperforms Dream2Act's approach (B) for synthetic training data quality.",
    "EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields (arXiv:2605.06192, May 2026) — primary concurrent work; injects KVAF kinematic heatmaps into Wan 2.2 via event-aware bidirectional dual-stream fusion; WorldArena benchmark for arm manipulation; requires joint fine-tuning of both branches; no policy training pipeline. Note: 'EA' = Event-Aware, not Embodiment-Aware. URDF-DiT differentiators are empirically testable: full-body 29 DoF vs. arm manipulation (Ablation B), ControlNet frozen backbone vs. joint fine-tuning (~40% fewer trainable parameters), explicit IDM→policy pipeline.",
    "VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis (arXiv:2604.09330, April 2026) — jointly denoises video+action via flow matching for tabletop arm manipulation (7–16 DoF); 45% on AgiBot G1 dual-arm grasping vs. 8% IDM baseline; no URDF kinematic constraints; acknowledged limitation: 'video branch not influenced by action branch.' URDF-DiT's FK heatmap injection directly addresses this limitation while extending to 29+ DoF.",
    "EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards (arXiv:2603.17808, March 2026) — executability via RL post-training using IDM-derived reward signals; evaluates bimanual tabletop. Key distinction: EVA = soft learned reward constraint; URDF-DiT = hard geometric FK constraint at every diffusion step. ICLR 2027 ablation directly compares these two executability enforcement approaches.",
    "FlowAct-R1: Towards Interactive Humanoid Video Generation (arXiv:2601.10103, January 2026) — real-time interactive digital human character animation via MMDiT chunkwise diffusion with audio/text-based full-body control at 25fps; targets NPC-style animated digital humans (lip-sync, expressions, body gestures), not physical robot embodiment; no URDF kinematic constraints, no robot joint angles, no IDM policy extraction pipeline. Differentiation: character animation interactive use case vs. offline robot training data generation.",
    "KStar Diffuser (arXiv:2503.10743, CVPR 2025) — URDF-parsed spatial-temporal graph with differentiable FK for bimanual action diffusion (68.2% vs. 33.9% for PerAct2); policy layer not video synthesis; complementary.",
    "Kinema4D (arXiv March 2026, NTU) — URDF-driven FK for 4D pointmap scene realism; not policy-data generation or DiT attention injection.",
    "Controllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026) — validates per-frame 2D skeleton-sequence conditioning in video diffusion for human motion synthesis; closest video-generation analogue to URDF-DiT's conditioning mechanism; targets human motion not robot URDF kinematics or policy extraction.",
    "HumanoidBench (arXiv:2403.10506, 2024) — 27 tasks (H1/Digit, MuJoCo); ICLR 2027 cross-embodiment evaluation target.",
    "RoboCasa365 (arXiv:2603.04356, ICLR 2026) — 365 kitchen tasks with humanoid support; ICLR 2027 household generalization evaluation.",
    "X-Humanoid (arXiv Dec 2025); MITTY (arXiv 2025); G-DReaM (arXiv 2025)"
  ],
  "description": "⚠️ USER REQUIREMENT TRADEOFF: The user required evaluation on three platforms — Isaac Lab G1 locomanipulation, HumanoidBench whole-body tasks, and RoboCasa365 humanoid kitchen. The CoRL 2026 submission covers ONLY Isaac Lab G1 locomanipulation (1 of 3). The user must decide: (A) target CoRL 2026 with partial benchmark coverage now + ICLR 2027 for full coverage; or (B) skip CoRL 2026 and target ICLR 2027 directly with full coverage from the start. This is not a footnote — it is a deliberate scope decision.\n\nURDF-DiT addresses a specific, empirically testable question: is full-body kinematic conditioning throughout the denoising process necessary for high-quality IDM training data generation on whole-body contact tasks? The paper tests this via two ablations that together constitute its primary scientific contribution: (A) downstream Isaac Lab G1 policy success rate from URDF-DiT-generated trajectories vs. vanilla Wan 2.2 + post-hoc URDF-IK trajectories (same IDM, same policy training — tests in-loop vs. post-hoc kinematic enforcement); (B) full-body 29 DoF conditioning vs. end-effector-only conditioning (tests whether the full kinematic chain matters for whole-body contact task video generation). The second ablation directly and empirically differentiates URDF-DiT from EA-WM's arm-only kinematic heatmap approach.\n\nKey technical points: (1) Dream2Act (arXiv:2603.19709) generates in robot-native VISUAL space (hallucinating G1 body via Seedance 2.0) then applies post-generation URDF-IK for kinematic extraction — URDF-DiT tests whether in-loop FK conditioning outperforms this extraction approach for synthetic training data; (2) EA-WM (arXiv:2605.06192, Event-Aware, not Embodiment-Aware) validates in-loop KVAF heatmap injection for arm manipulation — URDF-DiT extends to 29 DoF full-body with ControlNet-style frozen backbone (no joint fine-tuning, ~40% fewer trainable parameters) and adds the IDM→policy pipeline; (3) FlowAct-R1 (arXiv:2601.10103) is audio/text-driven digital human character animation (NPCs), not physical robot URDF kinematics or policy extraction.\n\nDay 14 CoRL/ICLR 2027 pivot criteria (concrete): Submit to CoRL if URDF-DiT policy success ≥ 20% AND ≥ 5 pp improvement over vanilla baseline AND joint-limit violation rate ≤ 10%. Pivot to ICLR 2027 if URDF-DiT fails to exceed baseline by ≥ 5 pp, or absolute success < 15%, or violation rate > 15% (all GPU investment preserved for ICLR 2027). FK residual consistency loss enforces kinematic geometry in generated outputs; visual domain gap addressed separately via domain-randomized Isaac Lab rendering during IDM training — two distinct mechanisms for two distinct problems.",
  "project_name": "urdf_dit_loco_policy",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["CRITICAL NEW ISSUE — BRIDGEV2W (arXiv:2602.03793, February 2026) NOT CITED: Independent verification confirms BridgeV2W explicitly 'converts coordinate-space actions into pixel-aligned embodiment masks rendered from the URDF and camera parameters. These masks are then injected into a pretrained video generation model via a ControlNet-style pathway.' This paper — applied to single-arm (DROID) and dual-arm (AgiBot-G1) robots — is architecturally nearly identical to URDF-DiT's core contribution (ControlNet + URDF conditioning for robot video DiT). A CoRL reviewer familiar with the embodied world model literature will immediately flag this omission. URDF-DiT must cite BridgeV2W and differentiate explicitly on: (a) full-body humanoid 29 DoF vs. arm/dual-arm scope; (b) Gaussian joint-position heatmaps from FK (continuous per-joint scalar fields encoding kinematic structure) vs. BridgeV2W's pixel-aligned binary embodiment masks (which encode link occupancy but not individual joint angles); (c) IDM training data generation as the downstream objective vs. BridgeV2W's policy evaluation and goal-conditioned planning. With BridgeV2W now in the landscape alongside EA-WM, the claim that URDF-DiT introduces ControlNet + URDF injection into video DiT is no longer defensible — the paper's novelty must be repositioned as 'full-body humanoid kinematic conditioning with Gaussian heatmaps for IDM training data generation,' not as a novel conditioning architecture.", "VAG 'EXPLICITLY ACKNOWLEDGES' CHARACTERIZATION REQUIRES PRECISION: The proposal states VAG 'explicitly acknowledges the video branch has not been influenced by the action branch.' Independent review of the VAG abstract finds it describes 'synchronized denoising in both branches' with 'adaptive 3D pooling to transfer compact global video context to the action branch' — suggesting the design routes video features to actions but not necessarily the reverse. If this quote comes from an ablation or analysis section in the full paper, it must be cited with section/page reference. If it is the proposal author's inference, it must be rewritten: 'VAG's architecture routes video context to the action branch via 3D pooling but does not inject action signals back into the video denoising process, leaving a video-action coupling gap that explicit FK heatmap injection in URDF-DiT addresses.' Misquoting a competitor's paper is a fast track to rejection at CoRL.", "NOVELTY BAR AT CORL IS NOW CRITICALLY THIN: With EA-WM (in-loop kinematic heatmap injection into Wan 2.2 cross-attention, May 2026) and BridgeV2W (ControlNet + URDF embodiment mask injection into pretrained video DiT, February 2026) both uncited-until-now, the paper's architectural contribution is no longer novel. The remaining novelty is exclusively in (a) full-body humanoid scope (29 DoF vs. arm-only) and (b) IDM-to-policy pipeline. Point (b) is primarily an engineering contribution. Point (a) is an empirical claim that depends on Ablation B showing meaningful improvement (≥5pp). If Ablation B shows marginal benefit from full-body vs. end-effector conditioning, the paper has no defensible novel claim over the combined EA-WM + BridgeV2W prior work. The proposal's 'submit with reframing' contingency (Ablation B < 3pp → 'end-effector conditioning suffices') would produce a paper saying 'our novel extension doesn't help' — which is not a CoRL-level contribution. This risk must be assessed before committing to the CoRL trajectory.", "CORL EVALUATION STILL 1 OF 3 USER-REQUIRED BENCHMARKS: This is flagged explicitly in the proposal (which is correct), but it remains a hard constraint — the CoRL submission does not satisfy the user's stated requirement of evaluating on Isaac Lab G1 locomanipulation, HumanoidBench, AND RoboCasa365. The proposal correctly identifies this as an explicit user decision, but the review record should note it is unresolved from the user's perspective until they make the opt-in/out decision. Without user confirmation, the CoRL path should be treated as provisional."]
Feedback: Round 6 correctly resolved all four Round 5 issues: user tradeoff is explicitly and prominently flagged, FlowAct-R1 is in the landscape with a one-line differentiation, Ablation B is the primary scientific claim, and Day 14 pivot criteria have concrete numeric thresholds. The proposal is structurally sound. Two targeted fixes are required:

1. **URGENT: Add BridgeV2W to the landscape and reposition the novelty claim.** BridgeV2W (arXiv:2602.03793, February 2026) uses 'coordinate-space actions → pixel-aligned embodiment masks rendered from URDF → ControlNet-style injection into pretrained video DiT.' This is the same architecture as URDF-DiT. Add a landscape entry: 'BridgeV2W (arXiv:2602.03793, Feb 2026) uses URDF-rendered pixel-aligned embodiment masks injected via ControlNet pathway into a pretrained video DiT for arm/dual-arm manipulation video generation and policy evaluation. URDF-DiT differentiates on three axes: (a) full-body humanoid 29 DoF (vs. arm/dual-arm) with Gaussian joint-position heatmaps encoding per-joint kinematic structure rather than binary link occupancy masks; (b) whole-body contact interaction tasks (pick-and-place with locomotion, ball-kicking) vs. arm manipulation; (c) IDM training data generation pipeline vs. policy evaluation and goal-conditioned planning.' Then revise the introduction to acknowledge that ControlNet + URDF conditioning for robot video DiTs is now an established approach (citing EA-WM and BridgeV2W) and position URDF-DiT as the first application of this approach to full-body humanoid whole-body contact tasks with an explicit IDM training data generation objective.

2. **Fix the VAG 'explicitly acknowledges' characterization.** Change to: 'VAG's architecture routes compact global video context to the action branch via adaptive 3D pooling, but does not inject action signals back into the video denoising process — a design gap URDF-DiT addresses via bidirectional FK heatmap conditioning.' Do not use a direct quote unless you can cite the specific section where VAG uses those exact words.

3. **Assess the Ablation B risk explicitly.** Given EA-WM + BridgeV2W now both in the landscape, the paper needs Ablation B to be strongly positive (≥5pp) to have a defensible novel claim at CoRL. Add to the pivot criteria: if Ablation B < 5pp AND BridgeV2W is the closest prior, the paper's CoRL-level novelty is insufficient — pivot to ICLR 2027 with full benchmark coverage and a deeper ablation suite (also including a direct comparison against BridgeV2W's embodiment mask approach).

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
  "promptId": "3abb6fbf-dc12-41d6-81de-bd436aa09aac",
  "type": "user",
  "uuid": "54c5bd99-4f18-4375-b026-8c5c3e9ab18d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T12:57:50.598Z_

```json
{
  "parentUuid": "54c5bd99-4f18-4375-b026-8c5c3e9ab18d",
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
  "uuid": "b22fac31-bb7e-4e72-a1f9-d348c6298be3",
  "timestamp": "2026-05-10T12:57:50.598Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T12:57:50.598Z_

```json
{
  "parentUuid": "b22fac31-bb7e-4e72-a1f9-d348c6298be3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fd901d1d-5349-4709-93a0-61a672105436",
  "timestamp": "2026-05-10T12:57:50.598Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"URDF-DiT: Does Full-Body Kinematic Conditioning Throughout Denoising I…",
  "leafUuid": "fd901d1d-5349-4709-93a0-61a672105436",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Full-body kinematic conditioning for humanoid whole-body contact video generation",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---

### Assistant

_source line 8 · 2026-05-10T12:59:04.809Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before deciding on the approach.

**Current State After 6 Rounds:**
- The idea has been through 6 rounds of review with stagnating scores (3.0-3.2 range)
- Round 6 feedback identified critical issues:
  1. BridgeV2W (arXiv:2602.03793) - architecturally nearly identical to URDF-DiT's core contribution, not cited
  2. VAG "explicitly acknowledges" characterization needs precision
  3. Novelty bar is now critically thin with EA-WM + BridgeV2W both doing ControlNet + URDF conditioning
  4. CoRL evaluation still only covers 1 of 3 user-required benchmarks

**The Core Problem:**
The stagnation points to something more fundamental. BridgeV2W and EA-WM together essentially eliminate the architectural novelty—both apply ControlNet-style URDF conditioning to video DiTs. What's left is just extending from arm-only to full-body 29 DoF, the engineering work of generating IDM training data, and swapping binary masks for Gaussian heatmaps. These feel like incremental improvements rather than genuine contributions, and the incomplete CoRL evaluation makes it harder to demonstrate real impact.

**The contingency plan falls apart**: If Ablation B shows minimal gains, the paper admits the full-body extension doesn't meaningfully help—leaving no novelty over the existing methods. Even if it does show strong improvements, I'm essentially just saying "we extended BridgeV2W to humanoids," which is engineering, not algorithmic innovation.

**Time to seriously consider pivoting.** The real research question should be about video diffusion models for robot training data with kinematic constraints—what genuinely hasn't been explored yet? Looking at the landscape, BridgeV2W handles the core video generation, but there's still untapped potential in how we could approach this differently.

Now I'm examining what the existing methods actually achieve: Dream2Act gets 37.5% on whole-body tasks without any in-loop kinematic conditioning, which challenges the assumption that kinematic constraints during generation are even necessary. That's the real insight worth investigating.

Rather than debating where to apply kinematic conditioning, the deeper gap is that none of these approaches handle contact physics—the forces and deformations that matter when a robot interacts with soft objects or applies force. That's where the actual limitation lies for contact-rich manipulation tasks.

I'm considering two concrete pivots: either tackle the visual domain gap between generated videos and real robot footage that breaks inverse dynamics model training, or flip the approach entirely and generate actions directly from the task rather than synthesizing intermediate video representations.

Looking at the Dream2Act results more closely, the contact-heavy tasks like box-hugging are failing hardest at 10% success, which suggests conditioning video generation on predicted contact points rather than just kinematics could be a more targeted contribution—something that hasn't been explored yet in this space.

But stepping back, maybe the real issue is that I'm trying to dress up an ablation as a novel finding. The core question should be whether robot-native video generation is actually necessary for training IDMs, or if we could condition a general video model on latent robot representations instead. the whole-body domain. Since the architectural novelty is limited, I should pivot toward answering a genuine scientific question rather than proposing new methods. The strongest angle is studying what kinematic information is actually necessary for training video-based policies on humanoid whole-body tasks—testing a range from minimal conditioning up to full joint information across increasingly complex behaviors.

This positions the work as a systematic empirical study building on established conditioning techniques from prior work, which is inherently valuable regardless of the results. The key differentiator is that no prior work has systematically compared conditioning granularity across both task complexity and kinematic detail levels, making this a useful contribution even for CoRL if the findings are clean and interpretable.

Before committing to this framing, I should verify what BridgeV2W actually does and check if there are other papers I'm missing that might already cover this ground. The reviewer's feedback suggests the novelty is salvageable through repositioning rather than impossible—they're pointing toward an engineering contribution focused on the first application of ControlNet with URDF conditioning for full-body humanoid tasks in an IDM pipeline. Given that the architectural novelty is limited, I'm leaning toward a major revision that addresses their specific suggestions: add BridgeV2W context, fix the VAG characterization, and properly assess the risks around Ablation B. The scores have plateaued around 3.0-3.2 after six rounds, with the core issues being thin novelty and incomplete benchmark coverage—both structural problems that minor fixes won't resolve. I'm convinced a major revision is the right move since the infrastructure is solid and the research question about full-body kinematic conditioning for IDM training is genuinely worth pursuing, especially with comparisons against Dream2Act and EA-WM. The revision needs to foreground the empirical question more clearly and accept the architectural contributions as established rather than novel.

I should add BridgeV2W as an ablation baseline, reframe the novelty as the first systematic study of kinematic conditioning for humanoid whole-body tasks, and strengthen the risk assessment with concrete contingencies. But beyond these structural improvements, I'm wondering what would actually make this exciting—maybe the most compelling finding would be showing that end-effector conditioning alone isn't sufficient, but full-body kinematic conditioning only marginally outperforms contact-joint-only approaches, which would be a more nuanced and interesting result than I initially expected. I need to look up BridgeV2W to understand what it actually does and how it compares to my approach, then tighten up the novelty criteria and decision gates accordingly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd901d1d-5349-4709-93a0-61a672105436",
  "isSidechain": false,
  "requestId": "req_011Catviak3U2QGHe7gYzY7B",
  "type": "assistant",
  "uuid": "684b0487-e19f-448c-9d6d-47b7f46e4ae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VXgfvaRnigMYSnqWeNB5cQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18279,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18279,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4619,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18279
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

_source line 9 · 2026-05-10T12:59:04.842Z_

I need to do deep research before revising — especially on BridgeV2W and the current landscape — before deciding whether this needs a major revision or pivot.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "684b0487-e19f-448c-9d6d-47b7f46e4ae5",
  "isSidechain": false,
  "requestId": "req_011Catviak3U2QGHe7gYzY7B",
  "type": "assistant",
  "uuid": "944dc5a1-2d60-4518-aa0e-9e9e51011362",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VXgfvaRnigMYSnqWeNB5cQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18279,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18279,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4619,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18279
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

_source line 10 · 2026-05-10T12:59:20.447Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011WNgE4bbrqjzm6JZH8AMea`</summary>

```json
{
  "description": "Research BridgeV2W and related papers for URDF-DiT revision",
  "subagent_type": "Explore",
  "prompt": "I need you to fetch and analyze several arxiv papers for a research idea revision. Please use WebSearch and WebFetch to read the abstracts and method sections of the following papers:\n\n1. BridgeV2W (arXiv:2602.03793, February 2026) - described as using \"coordinate-space actions → pixel-aligned embodiment masks rendered from URDF → ControlNet-style injection into pretrained video DiT\" for robot video generation. I need to understand: (a) exactly what conditioning signal they use (binary masks? continuous? other?), (b) what tasks/embodiments they evaluate on, (c) what their downstream objective is (policy training? video generation quality? planning?), (d) what video backbone they use, (e) what their results show.\n\n2. EA-WM (arXiv:2605.06192, May 2026) - \"Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields\" - I need to confirm: (a) do they use Gaussian heatmaps or something else for kinematic conditioning?, (b) is it really arm manipulation only?, (c) do they fine-tune the entire video backbone jointly or use a ControlNet-style approach?, (d) what's the exact nature of their \"event-aware bidirectional dual-stream fusion\"?\n\n3. Also search for any papers from early 2026 that combine URDF + video diffusion + ControlNet for robotics. Search terms to try: \"URDF ControlNet video diffusion robot\", \"embodiment mask video generation robot\", \"kinematic conditioning humanoid video synthesis\". I want to know if there are other BridgeV2W-type papers we're missing.\n\n4. Also check: does Dream2Act (arXiv:2603.19709) really use Seedance 2.0 as the video backbone? And is their post-hoc IK approach really distinct from in-loop conditioning?\n\nPlease actually fetch and read (using WebFetch) the arxiv abstract pages for papers 1 and 2 at minimum. For paper 3, use WebSearch. Report what you find in detail, especially the technical specifics of the conditioning mechanisms."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "944dc5a1-2d60-4518-aa0e-9e9e51011362",
  "isSidechain": false,
  "requestId": "req_011Catviak3U2QGHe7gYzY7B",
  "type": "assistant",
  "uuid": "3a65003d-2184-4170-abde-9c9e6dfa579a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VXgfvaRnigMYSnqWeNB5cQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18279,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18279,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4619,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18279
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

_source line 11 · 2026-05-10T12:59:26.116Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BxtD2xaYxufXWipgU5JpZD`</summary>

```json
{
  "description": "Research novelty positioning for humanoid video diffusion IDM papers",
  "subagent_type": "Explore",
  "prompt": "I'm revising a research paper proposal called \"URDF-DiT\" that conditions a video diffusion model on full-body humanoid kinematics (29 DoF URDF forward kinematics encoded as Gaussian heatmaps, injected via ControlNet into Wan 2.2 DiT) to generate IDM training data for whole-body contact tasks.\n\nTwo papers are now known to do similar things architecturally:\n- BridgeV2W (arXiv:2602.03793): ControlNet + URDF embodiment masks → video DiT, arm/dual-arm robots\n- EA-WM (arXiv:2605.06192): kinematic heatmap injection into Wan 2.2 cross-attention, arm manipulation\n\nGiven this, the paper needs to either (a) find stronger differentiation, or (b) pivot to a genuinely novel question.\n\nPlease search for:\n1. Recent papers (2025-2026) on \"IDM inverse dynamics model humanoid video synthesis\" or \"humanoid whole-body contact video generation policy training\"\n2. Papers comparing kinematic conditioning granularity (end-effector only vs. full-body) in video generation or robot learning\n3. Papers on \"contact-aware video generation robot\" or \"contact point conditioning video diffusion\"\n4. Any papers specifically about video diffusion for locomotion-coupled manipulation (loco-manipulation) policy training\n5. Check if there's work on the question \"does video kinematic conditioning help IDM training quality?\" as an empirical study\n\nAlso think about: is the SCIENTIFIC QUESTION (does full-body kinematic conditioning improve IDM training data vs. post-hoc IK or end-effector-only?) genuinely novel as an empirical study, even if the architecture is established? What would make this a strong empirical paper for CoRL/ICLR?\n\nReport your findings and give me your honest assessment of whether this can be a strong paper at CoRL 2026 or needs to be repositioned for ICLR 2027 with broader scope."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a65003d-2184-4170-abde-9c9e6dfa579a",
  "isSidechain": false,
  "requestId": "req_011Catviak3U2QGHe7gYzY7B",
  "type": "assistant",
  "uuid": "5e3a50d9-cd81-478f-ae7b-fb8b2f1f72f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VXgfvaRnigMYSnqWeNB5cQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18279,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18279,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4619,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18279
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

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"URDF-DiT: Does Full-Body Kinematic Conditioning Throughout Denoising I…",
  "leafUuid": "5e3a50d9-cd81-478f-ae7b-fb8b2f1f72f7",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Full-body kinematic conditioning for humanoid whole-body contact video generation",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---

### Tool result

_source line 14 · 2026-05-10T13:00:27.006Z_

<details><summary>↩ Tool result · `toolu_01BxtD2xaYxufXWipgU5JpZD`</summary>

```text
Excellent. Now I have comprehensive information. Let me compile my assessment.

---

## Assessment: URDF-DiT Paper Positioning for CoRL 2026 vs. ICLR 2027

Based on my comprehensive search of recent literature (2025-2026), here is my honest assessment:

### **The Competitive Landscape**

You're correct that the architectural space is now occupied:

1. **BridgeV2W (arXiv:2602.03793)** - Published Feb 2026
   - ControlNet + URDF embodiment masks → video DiT
   - Scope: Dual-arm and single-arm manipulation (arm robots)
   - Uses flow-based motion loss for dynamics-focused learning
   - Unified architecture across embodiments via view-specific conditioning

2. **EA-WM (arXiv:2605.06192)** - Published May 2026
   - Kinematic heatmap injection into Wan 2.2 cross-attention
   - Scope: Arm manipulation with event-aware world modeling
   - Emphasizes kinematic-to-visual action field translation
   - Focus on preserving fine-grained robot-object interaction

3. **Morphology-Consistent Humanoid Interaction (arXiv:2603.19709)** - Published Mar 2026
   - Robot-centric video synthesis with URDF-constrained IK
   - Scope: Humanoid full-body interaction (kicking, sitting, punching)
   - Direct hallucination in robot coordinate system (eliminates morphology gap)
   - Validates on Unitree G1

### **The Critical Gap: What's Actually Missing**

After reviewing the literature, **the core scientific question is genuinely underexplored:**

**"Does full-body kinematic conditioning improve IDM training quality compared to end-effector-only or post-hoc IK approaches?"**

The literature reveals:

1. **No direct empirical comparison studies** - While BridgeV2W and EA-WM both use kinematic conditioning, neither conducts a systematic ablation comparing:
   - Full-body URDF kinematics vs. end-effector-only heatmaps
   - Synthetic video-generated IDM vs. real robot data IDM
   - Control-aware data synthesis vs. arbitrary video generation

2. **IDM quality as a training metric is underspecified** - Most papers focus on:
   - World model accuracy (L2 pixel loss, LPIPS)
   - Task success rates on downstream policies
   - NOT systematically on "does this synthesis approach produce better training data for IDMs?"

3. **Full-body humanoid + contact tasks is sparse** - Papers exist on:
   - Arm manipulation with kinematics
   - Humanoid locomotion (DiffuseLoco, LeVERB)
   - Humanoid manipulation (HDMI, X-Humanoid, RHINO)
   - BUT: Very little on **loco-manipulation with contact modeling** as a training data generation problem

4. **Contact-aware conditioning is underdeveloped** - Recent work on:
   - Contact diffusion (implicit contact reasoning)
   - Hierarchical diffusion with contact guidance
   - But NOT systematically integrated with kinematic heatmaps for humanoids

---

### **Verdict: Can This Be Strong at CoRL 2026?**

**Short answer: Unlikely as currently framed. Here's why:**

**Against CoRL 2026:**
- The architectural novelty (ControlNet + URDF heatmaps into Wan 2.2) is **already established** by BridgeV2W, EA-WM, and Morphology-Consistent
- CoRL 2026 submissions are likely already accepted/reviewed; you're months late
- CoRL values robotics contributions; yours is primarily a systems/data-generation paper without new embodied AI insights
- Incremental architecture papers rarely win unless paired with surprising empirical findings

**For CoRL 2026 to work, you'd need:**
1. **Genuinely novel embodiment** (e.g., quadrupeds doing loco-manipulation with precise foot contact)
2. **Surprising empirical finding** (e.g., "full-body conditioning degrades IDM quality under X conditions")
3. **Real robot validation** at scale (not just simulation)
4. Already substantial results to demonstrate

---

### **Verdict: ICLR 2027 is the Right Target**

**Reposition as a strong empirical paper with these angles:**

**Option A: "Kinematic Conditioning Granularity for Video-Based IDM Training" (Ablation Study)**
- **Research question:** "What level of kinematic detail (end-effector vs. full-body vs. contact points) maximizes IDM training data quality?"
- **Experiments:**
  - Generate 100K videos each with: (a) end-effector heatmaps only, (b) full-body 29-DoF URDF, (c) full-body + contact point conditioning
  - Train IDMs on each dataset
  - Test on downstream whole-body loco-manipulation tasks (pushing, lifting while walking, etc.)
  - Measure: task success, data efficiency, generalization to unseen contact scenarios
- **Why it's novel:** No paper directly compares these. BridgeV2W doesn't study this. EA-WM doesn't compare granularities.
- **Publication fit:** Strong empirical methodology, actionable insights for practitioners

**Option B: "Contact-Aware Kinematic Video Diffusion for Humanoid Loco-Manipulation"**
- **Research question:** "Can contact point conditioning improve video-generated IDM training for tasks requiring precise contact (footsteps, hand-object interactions during locomotion)?"
- **Technical contribution:** 
  - Extend your URDF heatmaps to include **contact state channels** (binary masks for foot-ground, hand-object contact predicted from physics simulation)
  - Modify cross-attention injection to weight contact regions
  - Compare to baseline (full-body kinematics without contact)
- **Validation:** 
  - Synthetic task suite: stepping over obstacles, pushing heavy objects while walking, etc.
  - Real robot (if possible): G1, H1, or similar
- **Why it's novel:** Contact conditioning in kinematic heatmaps is not systematically studied. Contact-aware world models exist, but not specifically for kinematic injection into video diffusion for humanoids.

**Option C: "Video Diffusion as Synthetic Data for Humanoid Loco-Manipulation: An Empirical Study of Data Quality vs. Quantity Trade-offs"**
- **Research question:** "For loco-manipulation policies, is 1M synthetic videos from a well-conditioned diffusion model better than 100K real videos? What conditioning choices matter?"
- **Why it's novel:** This is a pragmatic question that practitioners care about. No paper systematically answers it for humanoids doing contact-heavy tasks.

---

### **Honest Assessment Summary**

| Aspect | CoRL 2026 | ICLR 2027 |
|--------|-----------|----------|
| **Architecture Novelty** | Established (BridgeV2W, EA-WM, Morphology-Consistent) | Not the focus |
| **Empirical Question Novelty** | ❌ Unclear | ✅ High (kinematic conditioning ablation) |
| **Scope Advantage** | Humanoid + full-body 29-DoF | ✅ Strong differentiator |
| **Contact Modeling** | Underdeveloped in literature | ✅ Opportunity |
| **Real Robot Data** | Hard to match quickly | Can be simulation + 1-2 embodiments |
| **Timeline** | Unrealistic | Realistic (12 months) |
| **Likely Acceptance** | 20-30% (if empirical is strong) | 50-60% (if well-designed ablation) |

---

### **My Recommendation**

**Pivot to ICLR 2027 with Option A or B:**

1. **Don't lead with architecture.** Lead with: *"We systematically study whether full-body kinematic conditioning improves video-generated training data for whole-body contact tasks, compared to end-effector-only baselines."*

2. **Make the comparison tables your core contribution:**
   - Ablation: different conditioning granularities
   - Task performance under different data generation strategies
   - Data efficiency curves

3. **Use the established architecture (ControlNet + heatmaps)** as the *implementation detail*, not the story. The story is: **"What works best for humanoid loco-manipulation training data?"**

4. **Include contact modeling as a secondary contribution** (Option B strengthens this). Even if it's a small delta, it's defensible because contact is underexplored in this space.

5. **Get real robot validation if humanly possible.** Even 1-2 tasks on a real G1 or H1 would shift this from "interesting simulation study" to "actionable robotics contribution."

---

### **Sources**

- [BridgeV2W: Bridging Video Generation Models to Embodied World Models](https://arxiv.org/abs/2602.03793)
- [EA-WM: Event-Aware Generative World Model](https://arxiv.org/html/2605.06192v1)
- [Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis](https://arxiv.org/html/2603.19709v1)
- [DiffuseLoco: Real-Time Legged Locomotion Control](https://arxiv.org/abs/2404.19264)
- [HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos](https://arxiv.org/html/2509.16757v1)
- [X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale](https://arxiv.org/html/2512.04537v1)
- [Diffusion models for robotic manipulation: a survey](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full)
- [LeVERB: Humanoid Whole-Body Control](https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf)
- [X-Diffusion: Training Diffusion Policies on Cross-Embodiment Human Demonstrations](https://arxiv.org/html/2511.04671)
- [Morphological Self-Modeling in Robotics](https://www.science.org/doi/10.1126/scirobotics.abn1944)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e3a50d9-cd81-478f-ae7b-fb8b2f1f72f7",
  "isSidechain": false,
  "promptId": "3abb6fbf-dc12-41d6-81de-bd436aa09aac",
  "type": "user",
  "uuid": "e6441e6e-fcda-49fe-8407-db4376fc6889",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm revising a research paper proposal called \"URDF-DiT\" that conditions a video diffusion model on full-body humanoid kinematics (29 DoF URDF forward kinematics encoded as Gaussian heatmaps, injected via ControlNet into Wan 2.2 DiT) to generate IDM training data for whole-body contact tasks.\n\nTwo papers are now known to do similar things architecturally:\n- BridgeV2W (arXiv:2602.03793): ControlNet + URDF embodiment masks → video DiT, arm/dual-arm robots\n- EA-WM (arXiv:2605.06192): kinematic heatmap injection into Wan 2.2 cross-attention, arm manipulation\n\nGiven this, the paper needs to either (a) find stronger differentiation, or (b) pivot to a genuinely novel question.\n\nPlease search for:\n1. Recent papers (2025-2026) on \"IDM inverse dynamics model humanoid video synthesis\" or \"humanoid whole-body contact video generation policy training\"\n2. Papers comparing kinematic conditioning granularity (end-effector only vs. full-body) in video generation or robot learning\n3. Papers on \"contact-aware video generation robot\" or \"contact point conditioning video diffusion\"\n4. Any papers specifically about video diffusion for locomotion-coupled manipulation (loco-manipulation) policy training\n5. Check if there's work on the question \"does video kinematic conditioning help IDM training quality?\" as an empirical study\n\nAlso think about: is the SCIENTIFIC QUESTION (does full-body kinematic conditioning improve IDM training data vs. post-hoc IK or end-effector-only?) genuinely novel as an empirical study, even if the architecture is established? What would make this a strong empirical paper for CoRL/ICLR?\n\nReport your findings and give me your honest assessment of whether this can be a strong paper at CoRL 2026 or needs to be repositioned for ICLR 2027 with broader scope.",
    "agentId": "ad534df661cd8a8a7",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent. Now I have comprehensive information. Let me compile my assessment.\n\n---\n\n## Assessment: URDF-DiT Paper Positioning for CoRL 2026 vs. ICLR 2027\n\nBased on my comprehensive search of recent literature (2025-2026), here is my honest assessment:\n\n### **The Competitive Landscape**\n\nYou're correct that the architectural space is now occupied:\n\n1. **BridgeV2W (arXiv:2602.03793)** - Published Feb 2026\n   - ControlNet + URDF embodiment masks → video DiT\n   - Scope: Dual-arm and single-arm manipulation (arm robots)\n   - Uses flow-based motion loss for dynamics-focused learning\n   - Unified architecture across embodiments via view-specific conditioning\n\n2. **EA-WM (arXiv:2605.06192)** - Published May 2026\n   - Kinematic heatmap injection into Wan 2.2 cross-attention\n   - Scope: Arm manipulation with event-aware world modeling\n   - Emphasizes kinematic-to-visual action field translation\n   - Focus on preserving fine-grained robot-object interaction\n\n3. **Morphology-Consistent Humanoid Interaction (arXiv:2603.19709)** - Published Mar 2026\n   - Robot-centric video synthesis with URDF-constrained IK\n   - Scope: Humanoid full-body interaction (kicking, sitting, punching)\n   - Direct hallucination in robot coordinate system (eliminates morphology gap)\n   - Validates on Unitree G1\n\n### **The Critical Gap: What's Actually Missing**\n\nAfter reviewing the literature, **the core scientific question is genuinely underexplored:**\n\n**\"Does full-body kinematic conditioning improve IDM training quality compared to end-effector-only or post-hoc IK approaches?\"**\n\nThe literature reveals:\n\n1. **No direct empirical comparison studies** - While BridgeV2W and EA-WM both use kinematic conditioning, neither conducts a systematic ablation comparing:\n   - Full-body URDF kinematics vs. end-effector-only heatmaps\n   - Synthetic video-generated IDM vs. real robot data IDM\n   - Control-aware data synthesis vs. arbitrary video generation\n\n2. **IDM quality as a training metric is underspecified** - Most papers focus on:\n   - World model accuracy (L2 pixel loss, LPIPS)\n   - Task success rates on downstream policies\n   - NOT systematically on \"does this synthesis approach produce better training data for IDMs?\"\n\n3. **Full-body humanoid + contact tasks is sparse** - Papers exist on:\n   - Arm manipulation with kinematics\n   - Humanoid locomotion (DiffuseLoco, LeVERB)\n   - Humanoid manipulation (HDMI, X-Humanoid, RHINO)\n   - BUT: Very little on **loco-manipulation with contact modeling** as a training data generation problem\n\n4. **Contact-aware conditioning is underdeveloped** - Recent work on:\n   - Contact diffusion (implicit contact reasoning)\n   - Hierarchical diffusion with contact guidance\n   - But NOT systematically integrated with kinematic heatmaps for humanoids\n\n---\n\n### **Verdict: Can This Be Strong at CoRL 2026?**\n\n**Short answer: Unlikely as currently framed. Here's why:**\n\n**Against CoRL 2026:**\n- The architectural novelty (ControlNet + URDF heatmaps into Wan 2.2) is **already established** by BridgeV2W, EA-WM, and Morphology-Consistent\n- CoRL 2026 submissions are likely already accepted/reviewed; you're months late\n- CoRL values robotics contributions; yours is primarily a systems/data-generation paper without new embodied AI insights\n- Incremental architecture papers rarely win unless paired with surprising empirical findings\n\n**For CoRL 2026 to work, you'd need:**\n1. **Genuinely novel embodiment** (e.g., quadrupeds doing loco-manipulation with precise foot contact)\n2. **Surprising empirical finding** (e.g., \"full-body conditioning degrades IDM quality under X conditions\")\n3. **Real robot validation** at scale (not just simulation)\n4. Already substantial results to demonstrate\n\n---\n\n### **Verdict: ICLR 2027 is the Right Target**\n\n**Reposition as a strong empirical paper with these angles:**\n\n**Option A: \"Kinematic Conditioning Granularity for Video-Based IDM Training\" (Ablation Study)**\n- **Research question:** \"What level of kinematic detail (end-effector vs. full-body vs. contact points) maximizes IDM training data quality?\"\n- **Experiments:**\n  - Generate 100K videos each with: (a) end-effector heatmaps only, (b) full-body 29-DoF URDF, (c) full-body + contact point conditioning\n  - Train IDMs on each dataset\n  - Test on downstream whole-body loco-manipulation tasks (pushing, lifting while walking, etc.)\n  - Measure: task success, data efficiency, generalization to unseen contact scenarios\n- **Why it's novel:** No paper directly compares these. BridgeV2W doesn't study this. EA-WM doesn't compare granularities.\n- **Publication fit:** Strong empirical methodology, actionable insights for practitioners\n\n**Option B: \"Contact-Aware Kinematic Video Diffusion for Humanoid Loco-Manipulation\"**\n- **Research question:** \"Can contact point conditioning improve video-generated IDM training for tasks requiring precise contact (footsteps, hand-object interactions during locomotion)?\"\n- **Technical contribution:** \n  - Extend your URDF heatmaps to include **contact state channels** (binary masks for foot-ground, hand-object contact predicted from physics simulation)\n  - Modify cross-attention injection to weight contact regions\n  - Compare to baseline (full-body kinematics without contact)\n- **Validation:** \n  - Synthetic task suite: stepping over obstacles, pushing heavy objects while walking, etc.\n  - Real robot (if possible): G1, H1, or similar\n- **Why it's novel:** Contact conditioning in kinematic heatmaps is not systematically studied. Contact-aware world models exist, but not specifically for kinematic injection into video diffusion for humanoids.\n\n**Option C: \"Video Diffusion as Synthetic Data for Humanoid Loco-Manipulation: An Empirical Study of Data Quality vs. Quantity Trade-offs\"**\n- **Research question:** \"For loco-manipulation policies, is 1M synthetic videos from a well-conditioned diffusion model better than 100K real videos? What conditioning choices matter?\"\n- **Why it's novel:** This is a pragmatic question that practitioners care about. No paper systematically answers it for humanoids doing contact-heavy tasks.\n\n---\n\n### **Honest Assessment Summary**\n\n| Aspect | CoRL 2026 | ICLR 2027 |\n|--------|-----------|----------|\n| **Architecture Novelty** | Established (BridgeV2W, EA-WM, Morphology-Consistent) | Not the focus |\n| **Empirical Question Novelty** | ❌ Unclear | ✅ High (kinematic conditioning ablation) |\n| **Scope Advantage** | Humanoid + full-body 29-DoF | ✅ Strong differentiator |\n| **Contact Modeling** | Underdeveloped in literature | ✅ Opportunity |\n| **Real Robot Data** | Hard to match quickly | Can be simulation + 1-2 embodiments |\n| **Timeline** | Unrealistic | Realistic (12 months) |\n| **Likely Acceptance** | 20-30% (if empirical is strong) | 50-60% (if well-designed ablation) |\n\n---\n\n### **My Recommendation**\n\n**Pivot to ICLR 2027 with Option A or B:**\n\n1. **Don't lead with architecture.** Lead with: *\"We systematically study whether full-body kinematic conditioning improves video-generated training data for whole-body contact tasks, compared to end-effector-only baselines.\"*\n\n2. **Make the comparison tables your core contribution:**\n   - Ablation: different conditioning granularities\n   - Task performance under different data generation strategies\n   - Data efficiency curves\n\n3. **Use the established architecture (ControlNet + heatmaps)** as the *implementation detail*, not the story. The story is: **\"What works best for humanoid loco-manipulation training data?\"**\n\n4. **Include contact modeling as a secondary contribution** (Option B strengthens this). Even if it's a small delta, it's defensible because contact is underexplored in this space.\n\n5. **Get real robot validation if humanly possible.** Even 1-2 tasks on a real G1 or H1 would shift this from \"interesting simulation study\" to \"actionable robotics contribution.\"\n\n---\n\n### **Sources**\n\n- [BridgeV2W: Bridging Video Generation Models to Embodied World Models](https://arxiv.org/abs/2602.03793)\n- [EA-WM: Event-Aware Generative World Model](https://arxiv.org/html/2605.06192v1)\n- [Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis](https://arxiv.org/html/2603.19709v1)\n- [DiffuseLoco: Real-Time Legged Locomotion Control](https://arxiv.org/abs/2404.19264)\n- [HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos](https://arxiv.org/html/2509.16757v1)\n- [X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale](https://arxiv.org/html/2512.04537v1)\n- [Diffusion models for robotic manipulation: a survey](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full)\n- [LeVERB: Humanoid Whole-Body Control](https://people.eecs.berkeley.edu/~sastry/pubs/Pdfs%20of%202025/XueLeVERB2025.pdf)\n- [X-Diffusion: Training Diffusion Policies on Cross-Embodiment Human Demonstrations](https://arxiv.org/html/2511.04671)\n- [Morphological Self-Modeling in Robotics](https://www.science.org/doi/10.1126/scirobotics.abn1944)"
      }
    ],
    "totalDurationMs": 60882,
    "totalTokens": 33449,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 854,
      "cache_creation_input_tokens": 3028,
      "cache_read_input_tokens": 27022,
      "output_tokens": 2545,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3028
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 854,
          "output_tokens": 2545,
          "cache_read_input_tokens": 27022,
          "cache_creation_input_tokens": 3028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3028,
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
  "sourceToolAssistantUUID": "5e3a50d9-cd81-478f-ae7b-fb8b2f1f72f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T13:00:33.325Z_

<details><summary>↩ Tool result · `toolu_011WNgE4bbrqjzm6JZH8AMea`</summary>

```text
Perfect. Now let me compile my detailed findings with all the technical specifics you requested.

## Comprehensive Research Paper Analysis

I've successfully fetched and analyzed the papers you requested. Here are my detailed findings:

---

### **1. BridgeV2W (arXiv:2602.03793, February 2026)**

**Conditioning Signal:**
- Converts coordinate-space actions into **pixel-aligned embodiment masks** rendered from URDF and camera parameters
- Masks are injected via a **ControlNet-style pathway** into the pretrained video generation model
- The approach is binary mask-based (pixel-space segmentation of robot embodiment)
- View-specific conditioning accommodates different camera viewpoints

**Tasks & Embodiments Evaluated:**
- Single-arm robotics: DROID dataset
- Dual-arm robotics: AgiBot-G1 dataset
- Tested on "diverse and challenging conditions with unseen viewpoints and scenes"
- Downstream objectives include policy evaluation and goal-conditioned planning in real-world tasks

**Downstream Objective:**
- **Policy evaluation and goal-conditioned planning** for real-world robotic tasks
- Video generation quality as intermediate metric

**Video Backbone:**
- The paper leverages "a pretrained video generation model" but the specific backbone name is not disclosed in the abstracts/publicly available content. The ControlNet-style integration suggests a diffusion-based architecture (likely DiT-based given the trend in the field)

**Results:**
- Improved video generation quality compared to prior state-of-the-art
- Addresses action-video misalignment, viewpoint sensitivity, and architectural inconsistency across embodiments
- **Flow-based motion loss** focuses learning on dynamic, task-relevant regions rather than static backgrounds

---

### **2. EA-WM (arXiv:2605.06192, May 2026)**

**Kinematic Conditioning Method:**
- Uses **Structured Kinematic-to-Visual Action Fields (KVAFs)** converting low-dimensional robot states into camera-aligned visual fields
- **Yes, Gaussian heatmaps are used** - specifically "truncated Gaussian heatmaps centered at the projected end-effector location" for explicit manipulation focus
- KVAF rendering includes: depth-aware arm structures, joint landmarks, gripper geometry, end-effector heatmaps, and pose cues as temporally aligned visual fields

**Embodiments & Tasks:**
- Evaluated on **WorldArena benchmark** using **RoboTwin dataset**
- Appears to focus on bimanual manipulation setups
- Not limited to arm manipulation only (though primary focus)

**Video Backbone & Fine-tuning:**
- Backbone: **Wan2.2-TI2V** (a 5B parameter text-to-image-to-video DiT model from Alibaba)
- **NOT ControlNet-style** - uses **LoRA (Low-Rank Adaptation)** with rank 32 applied to:
  - Main DiT
  - KVAF-branch components
  - KVAF head
- Preserves original text-conditioned video denoising path while adding specialized action integration
- This is **joint fine-tuning via LoRA**, not a frozen backbone with adapter networks

**Event-Aware Bidirectional Dual-Stream Fusion:**
- Inserts **event-aware bidirectional fusion blocks** at sparse layers
- Computes **shared event representations** that generate:
  - Per-token event gates
  - Predicted event latents
- Modulates **cross-stream attention** between video and KVAF branches through residual connections
- Captures object state changes and interaction dynamics

---

### **3. Dream2Act (arXiv:2603.19709)**

**Video Backbone:**
- **Yes, uses Seedance 2.0** as confirmed
- Seedance 2.0 is ByteDance's multimodal video generation model (released February 2026)

**Post-Hoc IK Approach - Distinct from In-Loop Conditioning:**
The approach is fundamentally different:

**Post-Hoc IK Pipeline (3-stage):**
1. **Internal Joint Kinematics:** Constrained inverse kinematics optimization minimizes difference between forward kinematics predictions and extracted 3D keypoints, subject to URDF joint limits
2. **Scale Recovery:** Uses Perspective-n-Point (PnP) algorithm to align local 3D points with 2D detections, recovering metric scale and global pose
3. **Execution:** Formats trajectories into GMR (General Motion Retargeting) format for Sonic whole-body controller

**Key Distinction:**
- **Dream2Act generates videos OF the physical robot directly**, then extracts native trajectories post-hoc
- **In-loop conditioning** would condition generation on robot kinematics during synthesis
- Dream2Act avoids intermediate human representations entirely, **eliminating retargeting-induced morphological mismatches**
- Human-centric approaches failed completely (0% success vs. Dream2Act's 37.5%)

**Evaluation Results:**
- Overall success rate: **37.5%** across four task categories
- Baseline (human-centric retargeting): **0%** success
- Spatial alignment error: **0.14m** (vs. 0.75m for baselines)
- Ball kicking (multi-location): **40%** average success (vs. 0% baseline)

---

### **4. Additional Related Papers & Context**

**Other URDF + Video Diffusion + ControlNet Papers Found:**

1. **Kinema4D** (arXiv:2603.16669) - Drives URDF-based 3D robot via kinematics, producing 4D robot control trajectories with robot-centric pointmaps as conditioning
2. **Mask2IV** (arXiv:2510.03135) - Interaction-centric video generation via mask trajectories; predicts mask-based interaction trajectory then generates video
3. **MagicMotion** (arXiv:2503.16421) - Trajectory-controlled I2V using ControlNet-like architecture for trajectory integration
4. **Unified World Models (UWM)** (arXiv:2504.02792) - Couples video and action diffusion for pretraining on large robotic datasets; to be presented at RSS 2026

**Video Backbone Context:**
- **Wan2.2-TI2V-5B:** 5B parameter DiT with 4×32×32 compression ratio, trained on +65.6% more images and +83.2% more videos than Wan2.1
- **Seedance 2.0:** Multi-modal video generation supporting text, images, videos, audio inputs; outputs 4-15 second videos at 480p-720p
- **Kimodo** (arXiv:2603.15546) - NVIDIA's kinematic motion diffusion model trained on 700 hours of mocap data; supports text, keyframes, sparse joint positions, 2D paths, foot contacts

---

### **Key Technical Distinctions Summary**

| Aspect | BridgeV2W | EA-WM | Dream2Act |
|--------|-----------|-------|-----------|
| **Conditioning** | Binary embodiment masks (URDF-rendered) | Gaussian heatmaps + KVAF visual fields | Post-hoc IK from video keypoints |
| **Backbone** | Pretrained video DiT (not named) | Wan2.2-TI2V | Seedance 2.0 |
| **Integration** | ControlNet-style injection | LoRA fine-tuning | None (post-hoc) |
| **Flow Loss** | Yes (motion-focused) | Implicit (event gates) | No |
| **Success Rate** | Qualitative (video quality) | Qualitative (WorldArena) | 37.5% (real-world tasks) |

---

Sources:
- [BridgeV2W arXiv abstract](https://arxiv.org/abs/2602.03793)
- [EA-WM arXiv HTML](https://arxiv.org/html/2605.06192)
- [Dream2Act arXiv abstract](https://arxiv.org/abs/2603.19709)
- [Seedance 2.0 official](https://seed.bytedance.com/en/seedance2_0)
- [Wan2.2 GitHub](https://github.com/Wan-Video/Wan2.2)
- [Kinema4D arXiv](https://arxiv.org/html/2603.16669)
- [Mask2IV arXiv](https://arxiv.org/pdf/2510.03135)
- [MagicMotion arXiv](https://arxiv.org/html/2503.16421v3)
- [Unified World Models arXiv](https://arxiv.org/html/2504.02792v1)
- [Kimodo arXiv](https://arxiv.org/abs/2603.15546)
- [ControlNet methodology](https://huggingface.co/docs/diffusers/en/using-diffusers/controlnet)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a65003d-2184-4170-abde-9c9e6dfa579a",
  "isSidechain": false,
  "promptId": "3abb6fbf-dc12-41d6-81de-bd436aa09aac",
  "type": "user",
  "uuid": "c40bafe4-6da5-4eff-a56f-40c3fd637cfa",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to fetch and analyze several arxiv papers for a research idea revision. Please use WebSearch and WebFetch to read the abstracts and method sections of the following papers:\n\n1. BridgeV2W (arXiv:2602.03793, February 2026) - described as using \"coordinate-space actions → pixel-aligned embodiment masks rendered from URDF → ControlNet-style injection into pretrained video DiT\" for robot video generation. I need to understand: (a) exactly what conditioning signal they use (binary masks? continuous? other?), (b) what tasks/embodiments they evaluate on, (c) what their downstream objective is (policy training? video generation quality? planning?), (d) what video backbone they use, (e) what their results show.\n\n2. EA-WM (arXiv:2605.06192, May 2026) - \"Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields\" - I need to confirm: (a) do they use Gaussian heatmaps or something else for kinematic conditioning?, (b) is it really arm manipulation only?, (c) do they fine-tune the entire video backbone jointly or use a ControlNet-style approach?, (d) what's the exact nature of their \"event-aware bidirectional dual-stream fusion\"?\n\n3. Also search for any papers from early 2026 that combine URDF + video diffusion + ControlNet for robotics. Search terms to try: \"URDF ControlNet video diffusion robot\", \"embodiment mask video generation robot\", \"kinematic conditioning humanoid video synthesis\". I want to know if there are other BridgeV2W-type papers we're missing.\n\n4. Also check: does Dream2Act (arXiv:2603.19709) really use Seedance 2.0 as the video backbone? And is their post-hoc IK approach really distinct from in-loop conditioning?\n\nPlease actually fetch and read (using WebFetch) the arxiv abstract pages for papers 1 and 2 at minimum. For paper 3, use WebSearch. Report what you find in detail, especially the technical specifics of the conditioning mechanisms.",
    "agentId": "a90e86dad728436c7",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now let me compile my detailed findings with all the technical specifics you requested.\n\n## Comprehensive Research Paper Analysis\n\nI've successfully fetched and analyzed the papers you requested. Here are my detailed findings:\n\n---\n\n### **1. BridgeV2W (arXiv:2602.03793, February 2026)**\n\n**Conditioning Signal:**\n- Converts coordinate-space actions into **pixel-aligned embodiment masks** rendered from URDF and camera parameters\n- Masks are injected via a **ControlNet-style pathway** into the pretrained video generation model\n- The approach is binary mask-based (pixel-space segmentation of robot embodiment)\n- View-specific conditioning accommodates different camera viewpoints\n\n**Tasks & Embodiments Evaluated:**\n- Single-arm robotics: DROID dataset\n- Dual-arm robotics: AgiBot-G1 dataset\n- Tested on \"diverse and challenging conditions with unseen viewpoints and scenes\"\n- Downstream objectives include policy evaluation and goal-conditioned planning in real-world tasks\n\n**Downstream Objective:**\n- **Policy evaluation and goal-conditioned planning** for real-world robotic tasks\n- Video generation quality as intermediate metric\n\n**Video Backbone:**\n- The paper leverages \"a pretrained video generation model\" but the specific backbone name is not disclosed in the abstracts/publicly available content. The ControlNet-style integration suggests a diffusion-based architecture (likely DiT-based given the trend in the field)\n\n**Results:**\n- Improved video generation quality compared to prior state-of-the-art\n- Addresses action-video misalignment, viewpoint sensitivity, and architectural inconsistency across embodiments\n- **Flow-based motion loss** focuses learning on dynamic, task-relevant regions rather than static backgrounds\n\n---\n\n### **2. EA-WM (arXiv:2605.06192, May 2026)**\n\n**Kinematic Conditioning Method:**\n- Uses **Structured Kinematic-to-Visual Action Fields (KVAFs)** converting low-dimensional robot states into camera-aligned visual fields\n- **Yes, Gaussian heatmaps are used** - specifically \"truncated Gaussian heatmaps centered at the projected end-effector location\" for explicit manipulation focus\n- KVAF rendering includes: depth-aware arm structures, joint landmarks, gripper geometry, end-effector heatmaps, and pose cues as temporally aligned visual fields\n\n**Embodiments & Tasks:**\n- Evaluated on **WorldArena benchmark** using **RoboTwin dataset**\n- Appears to focus on bimanual manipulation setups\n- Not limited to arm manipulation only (though primary focus)\n\n**Video Backbone & Fine-tuning:**\n- Backbone: **Wan2.2-TI2V** (a 5B parameter text-to-image-to-video DiT model from Alibaba)\n- **NOT ControlNet-style** - uses **LoRA (Low-Rank Adaptation)** with rank 32 applied to:\n  - Main DiT\n  - KVAF-branch components\n  - KVAF head\n- Preserves original text-conditioned video denoising path while adding specialized action integration\n- This is **joint fine-tuning via LoRA**, not a frozen backbone with adapter networks\n\n**Event-Aware Bidirectional Dual-Stream Fusion:**\n- Inserts **event-aware bidirectional fusion blocks** at sparse layers\n- Computes **shared event representations** that generate:\n  - Per-token event gates\n  - Predicted event latents\n- Modulates **cross-stream attention** between video and KVAF branches through residual connections\n- Captures object state changes and interaction dynamics\n\n---\n\n### **3. Dream2Act (arXiv:2603.19709)**\n\n**Video Backbone:**\n- **Yes, uses Seedance 2.0** as confirmed\n- Seedance 2.0 is ByteDance's multimodal video generation model (released February 2026)\n\n**Post-Hoc IK Approach - Distinct from In-Loop Conditioning:**\nThe approach is fundamentally different:\n\n**Post-Hoc IK Pipeline (3-stage):**\n1. **Internal Joint Kinematics:** Constrained inverse kinematics optimization minimizes difference between forward kinematics predictions and extracted 3D keypoints, subject to URDF joint limits\n2. **Scale Recovery:** Uses Perspective-n-Point (PnP) algorithm to align local 3D points with 2D detections, recovering metric scale and global pose\n3. **Execution:** Formats trajectories into GMR (General Motion Retargeting) format for Sonic whole-body controller\n\n**Key Distinction:**\n- **Dream2Act generates videos OF the physical robot directly**, then extracts native trajectories post-hoc\n- **In-loop conditioning** would condition generation on robot kinematics during synthesis\n- Dream2Act avoids intermediate human representations entirely, **eliminating retargeting-induced morphological mismatches**\n- Human-centric approaches failed completely (0% success vs. Dream2Act's 37.5%)\n\n**Evaluation Results:**\n- Overall success rate: **37.5%** across four task categories\n- Baseline (human-centric retargeting): **0%** success\n- Spatial alignment error: **0.14m** (vs. 0.75m for baselines)\n- Ball kicking (multi-location): **40%** average success (vs. 0% baseline)\n\n---\n\n### **4. Additional Related Papers & Context**\n\n**Other URDF + Video Diffusion + ControlNet Papers Found:**\n\n1. **Kinema4D** (arXiv:2603.16669) - Drives URDF-based 3D robot via kinematics, producing 4D robot control trajectories with robot-centric pointmaps as conditioning\n2. **Mask2IV** (arXiv:2510.03135) - Interaction-centric video generation via mask trajectories; predicts mask-based interaction trajectory then generates video\n3. **MagicMotion** (arXiv:2503.16421) - Trajectory-controlled I2V using ControlNet-like architecture for trajectory integration\n4. **Unified World Models (UWM)** (arXiv:2504.02792) - Couples video and action diffusion for pretraining on large robotic datasets; to be presented at RSS 2026\n\n**Video Backbone Context:**\n- **Wan2.2-TI2V-5B:** 5B parameter DiT with 4×32×32 compression ratio, trained on +65.6% more images and +83.2% more videos than Wan2.1\n- **Seedance 2.0:** Multi-modal video generation supporting text, images, videos, audio inputs; outputs 4-15 second videos at 480p-720p\n- **Kimodo** (arXiv:2603.15546) - NVIDIA's kinematic motion diffusion model trained on 700 hours of mocap data; supports text, keyframes, sparse joint positions, 2D paths, foot contacts\n\n---\n\n### **Key Technical Distinctions Summary**\n\n| Aspect | BridgeV2W | EA-WM | Dream2Act |\n|--------|-----------|-------|-----------|\n| **Conditioning** | Binary embodiment masks (URDF-rendered) | Gaussian heatmaps + KVAF visual fields | Post-hoc IK from video keypoints |\n| **Backbone** | Pretrained video DiT (not named) | Wan2.2-TI2V | Seedance 2.0 |\n| **Integration** | ControlNet-style injection | LoRA fine-tuning | None (post-hoc) |\n| **Flow Loss** | Yes (motion-focused) | Implicit (event gates) | No |\n| **Success Rate** | Qualitative (video quality) | Qualitative (WorldArena) | 37.5% (real-world tasks) |\n\n---\n\nSources:\n- [BridgeV2W arXiv abstract](https://arxiv.org/abs/2602.03793)\n- [EA-WM arXiv HTML](https://arxiv.org/html/2605.06192)\n- [Dream2Act arXiv abstract](https://arxiv.org/abs/2603.19709)\n- [Seedance 2.0 official](https://seed.bytedance.com/en/seedance2_0)\n- [Wan2.2 GitHub](https://github.com/Wan-Video/Wan2.2)\n- [Kinema4D arXiv](https://arxiv.org/html/2603.16669)\n- [Mask2IV arXiv](https://arxiv.org/pdf/2510.03135)\n- [MagicMotion arXiv](https://arxiv.org/html/2503.16421v3)\n- [Unified World Models arXiv](https://arxiv.org/html/2504.02792v1)\n- [Kimodo arXiv](https://arxiv.org/abs/2603.15546)\n- [ControlNet methodology](https://huggingface.co/docs/diffusers/en/using-diffusers/controlnet)"
      }
    ],
    "totalDurationMs": 72871,
    "totalTokens": 30182,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2899,
      "cache_read_input_tokens": 25102,
      "output_tokens": 2174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2899
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2174,
          "cache_read_input_tokens": 25102,
          "cache_creation_input_tokens": 2899,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2899,
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
      "otherToolCount": 15
    }
  },
  "sourceToolAssistantUUID": "3a65003d-2184-4170-abde-9c9e6dfa579a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"URDF-DiT: Does Full-Body Kinematic Conditioning Throughout Denoising I…",
  "leafUuid": "c40bafe4-6da5-4eff-a56f-40c3fd637cfa",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Full-body kinematic conditioning for humanoid whole-body contact video generation",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---

### Assistant

_source line 18 · 2026-05-10T13:02:07.727Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have rich research findings. Let me synthesize what I've learned:

**Key findings:**

1. **EA-WM uses LoRA, NOT ControlNet**: This is a significant correction. EA-WM uses LoRA (rank 32) for joint fine-tuning of both branches, NOT a frozen backbone with adapter networks. The original idea claimed "ControlNet-style frozen backbone vs. EA-WM's joint fine-tuning" as a differentiator, but the previous idea incorrectly described EA-WM's integration method. 

The correct distinction is that EA-WM applies LoRA for fine-tuning combined with event-aware bidirectional dual-stream fusion, while URDF-DiT relies on a frozen backbone with ControlNet-style adaptation.

2. **BridgeV2W uses binary pixel-aligned embodiment masks, NOT Gaussian heatmaps**: The masks are rendered from URDF + camera parameters and injected via ControlNet pathway. So URDF-DiT's Gaussian heatmaps ARE distinct from BridgeV2W's binary masks — this is a meaningful technical difference.

3. **BridgeV2W evaluates on arm/dual-arm tasks**: Looking at the evaluation datasets, BridgeV2W focuses on arm and dual-arm configurations from DROID and other sources.

4. **Dream2Act confirmed using Seedance 2.0**: Generates videos of the physical robot directly (hallucinating G1 body), then extracts trajectories post-hoc via constrained IK.

5. **The empirical question about conditioning granularity is genuinely underexplored**: No paper directly compares end-effector-only vs. full-body kinematic conditioning for IDM training quality.

6. **ICLR 2027 seems like the right target**: Framing this as a systematic empirical study of how different kinematic conditioning strategies affect diffusion model performance.

So the positioning strategy is clearer now—I can acknowledge that URDF conditioning into video diffusion models isn't entirely novel, but the specific application to full-body humanoid whole-body contact tasks with systematic granularity comparisons is genuinely unexplored. The technical differentiation from BridgeV2W comes down to using continuous Gaussian heatmaps encoding individual joint angles rather than binary masks, and compared to EA-WM, the distinction is in how the kinematic structure gets integrated into the conditioning pipeline.

Wait, I need to correct something important about EA-WM—it actually does use KVAF Gaussian heatmaps like we're proposing, not just generic kinematic heatmaps, and the joint fine-tuning mechanism is more nuanced than I initially described. The real architectural difference is that EA-WM uses bidirectional dual-stream fusion with LoRA fine-tuning on both branches, whereas URDF-DiT keeps the backbone frozen and applies ControlNet-style conditioning, which is more compute-efficient and scales better to the full 29 DoF humanoid rather than just arm manipulation.

Given the stagnation and these corrections, I'm going with a major revision rather than a pivot—the core problem and scientific question are solid, but I need to reframe this as the first systematic study of full-body humanoid manipulation with event-aware fusion, not just a novel architecture claim. I'll add BridgeV2W as a precise technical comparison point and fix the EA-WM description to accurately reflect the LoRA approach and Gaussian heatmap components.

On CoRL 2026, I'm keeping it as an option despite the thin novelty bar, since the resource plan already accounts for it and the user should decide. I'll make the novelty risk explicit in the decision gate—if the ablations show binary masks work as well as Gaussian heatmaps and the embodiment-specific gains are under 5 percentage points, that triggers a pivot to ICLR 2027 instead.

The reframing contingency needs fixing: if Ablation B underperforms, I can't claim novelty for CoRL. But if I position URDF-DiT as a systematic comparison of conditioning approaches—binary masks, Gaussian heatmaps, end-effector heatmaps, and post-hoc IK—then even negative results become publishable as useful empirical findings.

Now I'm drafting the major revision. I need to reposition the core problem to acknowledge that ControlNet plus URDF conditioning is already established work (EA-WM and BridgeV2W), then frame this as a systematic study combined with the first full-body humanoid application. For the opportunity section, I'm correcting the technical details: EA-WM uses LoRA with KVAF and Gaussian heatmaps at end-effectors, not general kinematic heatmaps, and I need to properly integrate BridgeV2W and fix how I'm characterizing VAG. In the landscape and approach sections, I'm adding BridgeV2W, correcting the EA-WM entry, and repositioning the novelty claim around the systematic study scope and full-body application. I'm clarifying the technical distinctions between these approaches: EA-WM uses end-effector-focused Gaussian heatmaps with additional visual fields and LoRA fine-tuning, while BridgeV2W employs binary embodiment masks with ControlNet injection, and URDF-DiT scales to full-body 29 DoF joint heatmaps with a frozen ControlNet backbone—the key differentiator being URDF-DiT's comprehensive joint coverage versus EA-WM's end-effector specificity and different parameter optimization strategies.

Now I'm digging into the parameter efficiency claim: with LoRA rank 32 on a 5B DiT model, the additional parameters land somewhere between 50-200M, which is comparable to what a ControlNet-style adapter would add depending on implementation details, so the "40% fewer trainable parameters" assertion needs closer scrutiny against actual LoRA parameter counts rather than full fine-tuning baselines.

For the submission strategy, I'm mapping out decision thresholds: if Ablation B shows more than 5 percentage points improvement, that's a strong CoRL paper; if it's in the 3-5pp range and Ablation C demonstrates that Gaussian heatmaps outperform binary masks, I can reframe this as a representation design problem rather than a scope problem; but if Ablation B dips below 3pp or binary masks perform comparably, the novelty argument weakens and I should target ICLR 2027 instead.

Adding Ablation C to the timeline means training a ControlNet variant with binary embodiment masks, which adds roughly 15 hours to the resource estimate.

Now I'm writing out the full revised JSON with all the fixes applied — tightening the novelty claims, being honest about where the bar sits, and correcting the VAG characterization to accurately reflect that video context flows to the action branch but action signals don't feed back into video generation.

Actually, the key insight here is reframing the contribution around the systematic study itself. Even if the full-body conditioning doesn't outperform end-effector alone, showing which conditioning strategy works best for humanoid whole-body IDM training becomes the primary contribution — and that's defensible at CoRL if the experimental design is rigorous enough.

The real solution is spreading the novelty across three independent ablations: in-loop versus post-hoc training, full-body versus end-effector conditioning, and Gaussian heatmaps versus binary masks. This way the paper has multiple paths to a positive finding rather than betting everything on one ablation, and the systematic comparison across all three becomes its own contribution.

But I'm worried this could read as purely an ablation study without a clear positive result...

Actually, I need to identify what the expected strong positive finding should be for CoRL. Looking at the landscape: in-loop training should outperform Dream2Act's post-hoc approach, but the comparison is messy because they use different video backbones and evaluation setups. For full-body versus end-effector conditioning, the advantage depends heavily on the task—pick-and-place is arm-dominated while ball-kicking uses the legs, so if Isaac Lab only evaluates pick-and-place, this ablation might not show much difference.

The Gaussian versus binary masks comparison is more promising: Gaussian heatmaps encode continuous joint positions while binary masks only show link occupancy, so Gaussian should win for precise manipulation. But the real issue is that pick-and-place is fundamentally an arm task, so the full-body conditioning advantage might be negligible. To get a strong positive result, I'd need to either evaluate on whole-body contact tasks like ball-kicking or sofa-sitting, or include both arm-dominant and whole-body tasks in the evaluation.

This reframes the research question nicely: does the full-body conditioning advantage scale with how much whole-body coordination the task requires? I could add ball-kicking alongside pick-and-place to create a spectrum, predicting larger Ablation B gains for ball-kicking. That makes the paper more scientifically interesting and robust—if pick-and-place shows no advantage, ball-kicking would demonstrate the effect. Ball-kicking also aligns with Dream2Act's evaluation, which strengthens the comparison, though I'm now wondering about the implications of using the same task.

The key distinction is that Dream2Act targets zero-shot real-robot execution while URDF-DiT focuses on simulation-based policy training with synthetic data. These are fundamentally different use cases, so I shouldn't frame them as direct performance comparisons—they're complementary approaches. This clarifies how to position the work relative to Dream2Act.

Now I'm thinking through the major revision scope: the core empirical question holds, but I need to correct the architecture details around LoRA in EA-WM, integrate BridgeV2W properly, and reconsider how novelty should be framed given these changes.

The scientific contribution strengthens with task diversification across ball-kicking and pick-and-place, and adding Ablation C gives me a more rigorous comparison. This is definitely a major revision rather than a pivot—the fundamental problem stays intact while the framing, experiments, and related work all improve significantly.

I'm now ready to structure the full JSON response, focusing on updating the core problem to reflect the systematic study plus full-body extension angle, fixing the opportunity section with correct architecture details and BridgeV2W, repositioning novelty in the approach, and adjusting resource estimates for the additional ablation. me write this now.

One more consideration: the stagnation reminder says "近 3 轮的平均分从 3.0 到 3.2". The average score hasn't improved much. What would actually move the needle?

1. Fixing the missing BridgeV2W citation (was flagged as "CRITICAL NEW ISSUE" — this is an obvious rejection criterion, fixing it is necessary)
2. Genuinely improving the novelty claim (not just repositioning, but making it stronger)
3. Better experimental design (task diversification to stress-test Ablation B)

The task diversification (adding ball-kicking alongside pick-and-place) is the most substantive improvement to the scientific design. It makes:
- Ablation B more interpretable (different results for different task types = interesting finding)
- The paper more robust to a negative result on any single task
- The contribution more clearly

Expanding the evaluation to include whole-body contact tasks beyond just pick-and-place could be the breakthrough that finally breaks through this plateau. Let me generate the JSON now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c40bafe4-6da5-4eff-a56f-40c3fd637cfa",
  "isSidechain": false,
  "requestId": "req_011CatvvZZSKSx3Wq4ncBRPk",
  "type": "assistant",
  "uuid": "a04e9524-f719-4331-ab92-c73fb9d63e0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0168fKBp75wBkPqEVeBQ74xq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2571,
      "cache_creation_input_tokens": 6814,
      "cache_read_input_tokens": 29910,
      "output_tokens": 4940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2571,
          "output_tokens": 4940,
          "cache_read_input_tokens": 29910,
          "cache_creation_input_tokens": 6814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6814
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

_source line 19 · 2026-05-10T13:02:12.049Z_

Now I have the research I need. Key findings that change my analysis:

1. **EA-WM uses LoRA (not full fine-tuning)** — KVAF includes Gaussian heatmaps at end-effectors plus additional visual fields; the "ControlNet-style frozen backbone vs. joint fine-tuning" differentiator needs correction to "vs. LoRA fine-tuning"
2. **BridgeV2W confirmed**: binary pixel-aligned embodiment masks (not Gaussian heatmaps) via ControlNet into video DiT; arm/dual-arm only; downstream = policy eval and goal-conditioned planning (not IDM training)
3. **Task design flaw identified**: Using pick-and-place as the ONLY evaluation for "full-body 29 DoF conditioning" is self-defeating — pick-and-place is primarily an arm task, so Ablation B (full-body vs. end-effector) is likely to show minimal difference. This is why the paper is stagnating: the evaluation doesn't stress-test the core claim.

This warrants a **major revision**: same core problem, but (a) fix all three reviewer issues precisely, (b) diversify evaluation to tasks that actually demand full-body coordination, (c) add Ablation C comparing BridgeV2W-style binary masks vs. Gaussian heatmaps, making three independent bets instead of one.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a04e9524-f719-4331-ab92-c73fb9d63e0f",
  "isSidechain": false,
  "requestId": "req_011CatvvZZSKSx3Wq4ncBRPk",
  "type": "assistant",
  "uuid": "0188023d-a317-41c0-a6ed-5bf3bfb45921",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0168fKBp75wBkPqEVeBQ74xq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2571,
      "cache_creation_input_tokens": 6814,
      "cache_read_input_tokens": 29910,
      "output_tokens": 4940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2571,
          "output_tokens": 4940,
          "cache_read_input_tokens": 29910,
          "cache_creation_input_tokens": 6814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6814
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

_source line 20 · 2026-05-10T13:02:12.580Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CaQjxcq5PYNyuTNaJex6kW`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0188023d-a317-41c0-a6ed-5bf3bfb45921",
  "isSidechain": false,
  "requestId": "req_011CatvvZZSKSx3Wq4ncBRPk",
  "type": "assistant",
  "uuid": "89b4478c-683a-4ba1-9750-02821b44a750",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0168fKBp75wBkPqEVeBQ74xq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2571,
      "cache_creation_input_tokens": 6814,
      "cache_read_input_tokens": 29910,
      "output_tokens": 4940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2571,
          "output_tokens": 4940,
          "cache_read_input_tokens": 29910,
          "cache_creation_input_tokens": 6814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6814
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

_source line 21 · 2026-05-10T13:02:12.588Z_

<details><summary>↩ Tool result · `toolu_01CaQjxcq5PYNyuTNaJex6kW`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89b4478c-683a-4ba1-9750-02821b44a750",
  "isSidechain": false,
  "promptId": "3abb6fbf-dc12-41d6-81de-bd436aa09aac",
  "type": "user",
  "uuid": "45096e8e-3867-48a9-aea5-762bd706b112",
  "toolUseResult": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "89b4478c-683a-4ba1-9750-02821b44a750",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"URDF-DiT: Does Full-Body Kinematic Conditioning Throughout Denoising I…",
  "leafUuid": "45096e8e-3867-48a9-aea5-762bd706b112",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Full-body kinematic conditioning for humanoid whole-body contact video generation",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---

### Assistant

_source line 24 · 2026-05-10T13:02:51.504Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the research I need. Let me write the complete major revision JSON. Here's my plan for the key changes:

1. **core_problem**: Reframe to acknowledge established ControlNet+URDF architecture, position as systematic study + first full-body humanoid application, fix task design to include ball-kicking (whole-body) alongside pick-and-place (arm-dominant)

2. **opportunity**: Fix EA-WM description (LoRA, KVAF = Gaussian heatmaps at end-effectors + additional visual fields); add BridgeV2W precisely; fix VAG characterization

3. **landscape**: Add BridgeV2W entry; correct EA-WM entry; fix VAG quote  
   
4. **approach**: I'm repositioning the novelty around systematically comparing conditioning strategies and applying them to full-body humanoid control for the first time, with three core ablations testing in-loop versus post-hoc conditioning, full-body versus end-effector focus, and Gaussian heatmaps against BridgeV2W masks—using both pick-and-place and ball-kicking tasks to stress-test the full-body approach differently.

5. **resource_estimate**: Adding compute time for the third ablation and recalibrating the overall timeline.

6. **key_references**: Finalizing the reference list.

7. **change_type**: This is a major revision.

Now I'm reconsidering the CoRL versus ICLR decision more carefully. The reviewer's point is stark—if BridgeV2W and EA-WM are standard components, then CoRL only works if the ablations show real gains, and my current fallback plan of reframing without strong results doesn't hold up. I need clearer submission criteria: CoRL makes sense only if URDF-DiT hits at least 20% on one task, Ablation A shows 5+ percentage points over baseline, violation rates stay under 10%, and at least one of the other ablations proves meaningful.

If those conditions don't pan out, ICLR 2027 becomes the right move—and interestingly, even a negative result across all ablations could be valuable, showing that the kinematic conditioning approach matters less than the visual domain gap itself for this task.

Now I'm refining the technical details. Let me correct the specifics on EA-WM: it uses LoRA rank 32 across the DiT and KVAF components, with Gaussian heatmaps encoding end-effector positions alongside depth-aware arm structures and joint landmarks, all fused through event-aware bidirectional gating on the WorldArena benchmark. For BridgeV2W, the key difference is binary pixel-aligned masks rendered from URDF rather than Gaussian heatmaps, which changes how embodiment information gets encoded into the model.

BridgeV2W also applies flow-based motion loss to focus on task-relevant dynamics, evaluating on both single-arm DROID and dual-arm AgiBot-G1 setups. VAG's architecture is fundamentally different—it routes global video context to the action branch through adaptive 3D pooling but crucially doesn't feed action signals back into video generation, which leaves the video denoising process unconstrained by action feasibility. That's the architectural gap I'm highlighting in the comparison.

On the parameter efficiency claim, I need to reconsider the "40% fewer parameters" framing. EA-WM uses LoRA fine-tuning with rank 32, which adds roughly 50-100M parameters to a 5B model, whereas a ControlNet-style module could add 100-300M depending on architecture depth. So the parameter count might actually be comparable or even higher for ControlNet, not necessarily lower. The real distinction isn't parameter efficiency but rather how the learning is distributed—ControlNet freezes the backbone and concentrates all updates in the conditioning pathway to preserve the pre-trained prior, while LoRA spreads parameter updates across both branches. I should reframe this around the architectural trade-off rather than claiming fewer parameters.

For the ablation study, I'm seeing a pattern: full-body conditioning should provide the most benefit in tasks requiring whole-body coordination. Pick-and-place is arm-dominant so the advantage would be marginal, but ball-kicking involves locomotion and contact dynamics where the legs are critical actors, so the full-body advantage should be substantial. This gives me a testable hypothesis within the paper itself—that the benefit of full-body over end-effector conditioning scales with task complexity and coordination demands.

Generating the JSON structure now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45096e8e-3867-48a9-aea5-762bd706b112",
  "isSidechain": false,
  "requestId": "req_011Catw3tC4eV4g7UVc9DS8g",
  "type": "assistant",
  "uuid": "a1b9e0b3-aa77-4b51-9c6b-5fa7fef07f9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019ExTu5KjkabjG7DBbYr3MR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9895,
      "cache_read_input_tokens": 36724,
      "output_tokens": 1624,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1624,
          "cache_read_input_tokens": 36724,
          "cache_creation_input_tokens": 9895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9895
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

_source line 25 · 2026-05-10T13:02:51.505Z_

Now I have everything I need. Let me write the complete major revision.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1b9e0b3-aa77-4b51-9c6b-5fa7fef07f9e",
  "isSidechain": false,
  "requestId": "req_011Catw3tC4eV4g7UVc9DS8g",
  "type": "assistant",
  "uuid": "1e69c32b-e54d-4c6c-92a1-fff161c20e7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019ExTu5KjkabjG7DBbYr3MR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9895,
      "cache_read_input_tokens": 36724,
      "output_tokens": 1624,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1624,
          "cache_read_input_tokens": 36724,
          "cache_creation_input_tokens": 9895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9895
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

_source line 26 · 2026-05-10T13:02:51.514Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01KBQiA9uPBcxKFwQFdN45d1`</summary>

```json
{
  "todos": [
    {
      "content": "Write complete major-revision JSON for URDF-DiT round 7",
      "status": "in_progress",
      "activeForm": "Writing revised JSON"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e69c32b-e54d-4c6c-92a1-fff161c20e7d",
  "isSidechain": false,
  "requestId": "req_011Catw3tC4eV4g7UVc9DS8g",
  "type": "assistant",
  "uuid": "134a703e-c5be-440e-9241-c9d50a05f5d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019ExTu5KjkabjG7DBbYr3MR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9895,
      "cache_read_input_tokens": 36724,
      "output_tokens": 1624,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1624,
          "cache_read_input_tokens": 36724,
          "cache_creation_input_tokens": 9895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9895
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

_source line 27 · 2026-05-10T13:02:51.521Z_

<details><summary>↩ Tool result · `toolu_01KBQiA9uPBcxKFwQFdN45d1`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "134a703e-c5be-440e-9241-c9d50a05f5d6",
  "isSidechain": false,
  "promptId": "3abb6fbf-dc12-41d6-81de-bd436aa09aac",
  "type": "user",
  "uuid": "bf1d6931-6cd0-4b22-adbe-8aebbf2a9634",
  "toolUseResult": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Write complete major-revision JSON for URDF-DiT round 7",
        "status": "in_progress",
        "activeForm": "Writing revised JSON"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "134a703e-c5be-440e-9241-c9d50a05f5d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T13:06:28.279Z_

Based on my research, here is the complete major revision:

```json
{
  "change_type": "major",
  "title": "URDF-DiT: A Systematic Study of Kinematic Conditioning Approaches for Humanoid Whole-Body Contact Task IDM Training Data",
  "project_name": "urdf_dit_loco_policy",
  "source": "web_research",
  "level": "solid",

  "core_problem": "ControlNet-style URDF conditioning for robot video generation is now an established approach — BridgeV2W (arXiv:2602.03793, Feb 2026) applies it with binary embodiment masks for arm/dual-arm manipulation; EA-WM (arXiv:2605.06192, May 2026) applies it with Gaussian end-effector heatmaps for arm manipulation via LoRA fine-tuning. Neither work has been applied to full-body humanoid whole-body contact tasks, and neither studies the conditioning mechanism itself as an empirical variable affecting downstream IDM training quality.\n\nURDF-DiT's empirical question is therefore: across three independently testable conditioning design choices — (A) in-loop FK conditioning during denoising vs. post-hoc URDF-IK after unconstrained generation; (B) full-body 29 DoF Gaussian heatmaps vs. end-effector-only heatmaps; (C) continuous Gaussian joint-position heatmaps (encoding kinematic structure and individual joint angles) vs. BridgeV2W-style binary pixel-aligned embodiment masks (encoding link occupancy) — which choices measurably improve IDM training data quality for humanoid whole-body contact interaction tasks, as measured by downstream Isaac Lab G1 policy success rate?\n\nThe three ablations are independent bets: the paper's scientific contribution holds if any one of them is positive. Crucially, task diversification is necessary to stress-test Ablation B: pick-and-place (arm-dominant; full-body conditioning advantage expected small) and ball-kicking (whole-body locomotion + foot contact; full-body conditioning advantage expected large) are both evaluated, enabling the within-paper hypothesis — the advantage of full-body over end-effector-only conditioning scales with the degree of whole-body coordination required — to be tested directly. This makes Ablation B informative regardless of the direction of the finding.\n\n⚠️ USER REQUIREMENT TRADEOFF — EXPLICIT FLAG: The user required evaluation on three platforms: Isaac Lab G1 locomanipulation, HumanoidBench whole-body tasks, and RoboCasa365 humanoid kitchen. The CoRL 2026 scoped submission covers ONLY Isaac Lab G1 locomanipulation + Isaac Lab G1 ball-kicking (2 tasks, 1 simulation environment). HumanoidBench and RoboCasa365 are deferred to ICLR 2027. The user must decide: (A) target CoRL 2026 with partial coverage now + ICLR 2027 for full coverage; or (B) skip CoRL 2026 and target ICLR 2027 from the start with all three user-required platforms. This is not a footnote — it is a deliberate scope decision that remains unresolved until the user confirms.",

  "opportunity": "GR00T-Dreams/DreamGen (2025) validated the video-diffusion → IDM pipeline for tabletop manipulation. Dream2Act (arXiv:2603.19709, March 2026) extended to full-body G1 whole-body contact interaction via two distinct components: (A) robot-native visual space generation using Seedance 2.0 (hallucinating the G1 body for morphological consistency — not retargeting from human video); (B) post-generation kinematic extraction via 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK applied AFTER all video frames are produced. Dream2Act achieves 37.5% overall success across four whole-body contact tasks (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%) vs. 0% for conventional retargeting; inference latency is its primary stated limitation. Dream2Act targets zero-shot real-robot execution; URDF-DiT targets synthetic IDM training data generation — complementary objectives. Ablation A directly tests whether in-loop FK conditioning (URDF-DiT) produces better IDM training trajectories than Dream2Act's post-generation URDF-IK extraction (approach B) for the synthetic data use case.\n\nBridgeV2W (arXiv:2602.03793, February 2026) — the most architecturally proximate prior work — converts coordinate-space actions into pixel-aligned binary embodiment masks rendered from URDF and camera parameters, then injects them via ControlNet-style pathway into a pretrained video DiT. BridgeV2W also applies a flow-based motion loss focusing learning on dynamic, task-relevant regions. Evaluates on DROID (single-arm) and AgiBot-G1 (dual-arm); downstream objective is policy evaluation and goal-conditioned planning, not IDM training data generation. URDF-DiT differentiates along three empirically testable axes: (a) continuous Gaussian joint-position heatmaps (encoding per-joint kinematic structure and individual joint angles from all 29 DoF) vs. binary pixel-aligned link-occupancy masks (which encode embodiment geometry but not individual joint-angle state); (b) full-body humanoid whole-body contact tasks vs. arm/dual-arm manipulation; (c) IDM training data generation pipeline vs. policy evaluation and goal-conditioned planning. Ablation C directly tests axis (a): do Gaussian heatmaps produce better IDM training data than BridgeV2W-style binary masks when both are applied under identical ControlNet injection?\n\nEA-WM (arXiv:2605.06192, May 2026) injects Kinematic-to-Visual Action Fields (KVAFs — truncated Gaussian heatmaps at projected end-effector positions plus depth-aware arm structures, joint landmarks, gripper geometry, and pose cues) into Wan 2.2 via event-aware bidirectional dual-stream fusion, implemented with LoRA fine-tuning (rank 32) applied to the main DiT, KVAF branch, and KVAF head. Evaluates on WorldArena benchmark (RoboTwin dataset, arm/bimanual manipulation); no policy training output. URDF-DiT differentiates: (a) full-body 29 DoF (pelvis, legs, torso, arms, hands) vs. EA-WM's end-effector-focused KVAF; (b) ControlNet frozen backbone (conditioning pathway only trained, pre-trained video prior preserved) vs. EA-WM's LoRA fine-tuning distributed across both branches; (c) explicit IDM→policy pipeline vs. no policy output. Ablation B directly tests axis (a) for IDM training data quality.\n\nVAG (arXiv:2604.09330, April 2026) introduces dual-stream flow matching jointly denoising video and action for arm manipulation (7–16 DoF), achieving 45% on AgiBot G1 dual-arm grasping vs. 8% IDM baseline. VAG's architecture routes compact global video context to the action branch via adaptive 3D pooling but does not inject action signals back into the video denoising process, leaving video generation unconstrained by action-space feasibility — a design gap URDF-DiT addresses by conditioning video denoising on FK heatmaps throughout.\n\nEVA (arXiv:2603.17808, March 2026) closes executability gaps via RL post-training using IDM-derived reward signals. Key distinction: EVA = soft learned reward constraint via RL; URDF-DiT = hard geometric FK constraint injected at every diffusion step. EVA evaluates bimanual tabletop; URDF-DiT targets full-body 29+ DoF whole-body contact.\n\n⚠️ USER REQUIREMENT TRADEOFF: Explicitly flagged in core_problem above. CoRL 2026 = 1 of 3 user-required platforms. Full coverage requires ICLR 2027. Decision is unresolved pending user confirmation.",

  "landscape": "GR00T-Dreams/DreamGen (arXiv 2025): fine-tunes Cosmos-Predict2 with language conditioning; extracts pseudo-actions via IDM or latent action model. No URDF kinematic constraint. Tabletop manipulation only.\n\nDream2Act (arXiv:2603.19709, March 2026): TWO DISTINCT COMPONENTS — (A) VIDEO GENERATION MODALITY: robot-native visual space via Seedance 2.0 (ByteDance), hallucinating G1 body for morphological consistency; (B) KINEMATIC EXTRACTION: post-generation pipeline applying 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK. Achieves 37.5% overall (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%) vs. 0% for human-centric retargeting; spatial alignment error 0.14m vs. 0.75m for baselines. Targets zero-shot real-robot execution; inference latency is primary stated limitation. URDF-DiT Ablation A tests whether in-loop FK conditioning outperforms Dream2Act's approach B for synthetic IDM training data quality.\n\nBridgeV2W (arXiv:2602.03793, February 2026): converts coordinate-space actions into PIXEL-ALIGNED BINARY EMBODIMENT MASKS rendered from URDF + camera parameters; injects via ControlNet-style pathway into pretrained video DiT; applies flow-based motion loss to focus learning on dynamic, task-relevant regions. Evaluates on DROID (single-arm) and AgiBot-G1 (dual-arm); downstream = policy evaluation and goal-conditioned planning. Key distinction from URDF-DiT: (a) binary link-occupancy masks vs. continuous Gaussian joint-position heatmaps (masks encode embodiment geometry but not individual joint-angle state; heatmaps encode per-joint kinematic structure and angle); (b) arm/dual-arm scope vs. full-body humanoid 29 DoF whole-body contact; (c) policy evaluation/planning vs. IDM training data generation. URDF-DiT Ablation C directly compares these conditioning representations under identical ControlNet injection.\n\nEA-WM (arXiv:2605.06192, May 2026): 'EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields.' KVAF = truncated Gaussian heatmaps at projected end-effector locations + depth-aware arm structures + joint landmarks + gripper geometry + pose cues. Implements event-aware bidirectional dual-stream fusion via shared event representations generating per-token event gates modulating cross-stream attention. Uses LoRA fine-tuning (rank 32) applied to main Wan 2.2 DiT, KVAF branch, and KVAF head — NOT a frozen backbone; distributes parameter updates across both branches. Evaluates on WorldArena benchmark (RoboTwin dataset, arm/bimanual tasks); no policy training pipeline. Note: 'EA' = Event-Aware, not Embodiment-Aware. URDF-DiT differentiates: (a) full-body 29 DoF (all joints, including legs and pelvis critical for whole-body contact) vs. EA-WM's end-effector-focused KVAF; (b) ControlNet frozen backbone (trains conditioning pathway only, preserves pre-trained video prior) vs. EA-WM's LoRA fine-tuning distributed across branches; (c) IDM→policy pipeline vs. no policy output.\n\nVAG (arXiv:2604.09330, April 2026): dual-stream video-action generation via flow matching for tabletop arm manipulation (7–16 DoF); 45% on AgiBot G1 dual-arm grasping vs. 8% ResNet+IDM baseline; no URDF kinematic constraints. Architecture routes compact global video context to the action branch via adaptive 3D pooling but does not inject action signals back into the video denoising process, leaving video generation unconstrained by action-space feasibility. No full-body humanoid evaluation.\n\nEVA (arXiv:2603.17808, March 2026): RL post-training using IDM-derived reward signals penalizing joint-limit violations, velocity/acceleration/jerk; evaluates bimanual tabletop (RoboTwin 2.0). Distinct from URDF-DiT: soft learned reward (post-training) vs. hard geometric FK constraint (every diffusion step).\n\nFlowAct-R1 (arXiv:2601.10103, January 2026): real-time interactive digital human character animation via MMDiT with audio/text-based full-body control at 25fps; targets NPC-style animated digital humans (lip-sync, expressions, gestures), not physical robot URDF kinematics or IDM extraction.\n\nKStar Diffuser (arXiv:2503.10743, CVPR 2025): URDF-parsed spatial-temporal graph with differentiable FK for bimanual action diffusion (68.2% vs. 33.9% for PerAct2); operates at the policy/action layer, not video synthesis. Complementary.\n\nKinema4D (arXiv March 2026, NTU): URDF-driven FK for 4D pointmap scene realism conditioning; not policy-data generation or video DiT attention injection.\n\nControllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026): cascaded text-to-2D-skeleton → skeleton-to-video pipeline validates per-frame 2D pose-sequence conditioning in video diffusion; targets human motion synthesis, not robot URDF kinematics or policy extraction.\n\nX-Humanoid (arXiv Dec 2025): replaces human with humanoid in video via Wan 2.2; no URDF constraint injection. MITTY (arXiv 2025): human-to-robot video diffusion without kinematic enforcement. G-DReaM (arXiv 2025): graph-conditioned diffusion for motion retargeting on motion sequences, not RGB video.\n\nHumanoidBench (arXiv:2403.10506, 2024): 27 whole-body tasks (H1/Digit, MuJoCo); deferred to ICLR 2027. RoboCasa365 (arXiv:2603.04356, ICLR 2026): 365 kitchen tasks with humanoid support; deferred to ICLR 2027.",

  "approach": "NOVELTY REPOSITIONING (required given EA-WM + BridgeV2W): ControlNet + URDF conditioning for robot video DiTs is now an established approach. URDF-DiT's contribution is NOT a novel conditioning architecture. The paper's contribution is: (1) first application of this conditioning paradigm to full-body humanoid 29 DoF whole-body contact interaction tasks (pelvis, legs, torso, arms, hands) — neither BridgeV2W nor EA-WM evaluate full-body humanoid contact tasks; (2) first systematic study comparing three conditioning design choices (in-loop vs. post-hoc, full-body vs. end-effector, Gaussian heatmaps vs. binary masks) on IDM training data quality, with downstream policy success as the evaluation metric; (3) task-dependent conditioning hypothesis: the advantage of full-body over end-effector-only conditioning scales with the degree of whole-body coordination required, tested via two evaluation tasks that span the arm-dominant/whole-body spectrum. This repositioning makes the paper robust to any single ablation being negative — a systematic study with three independent testable claims has a defensible contribution even if one claim is not supported.\n\nARCHITECTURE: URDF-DiT uses a ControlNet-style conditioning module — Wan 2.2 backbone weights fully frozen; only the FK-heatmap encoder and zero-conv injection layers are trained. Per-frame G1 URDF forward-kinematics outputs (all 29 DoF: pelvis, legs, torso, arms, hands) are projected to the camera plane via differentiable FK and encoded as structured Gaussian joint-position heatmaps, injected into the cross-attention layers of the Wan 2.2 DiT. Unlike EA-WM's LoRA fine-tuning distributed across both video and KVAF branches, URDF-DiT's ControlNet design concentrates all learning in the conditioning pathway (preserving the pre-trained video prior) — a different compute allocation suited to the training-data synthesis objective where video fidelity matters more than end-to-end action prediction.\n\nTASK SUITE (critical for Ablation B): Two Isaac Lab G1 tasks are evaluated, chosen to differentially stress the full-body conditioning hypothesis:\n- Task 1: Pick-and-place with locomotion (arm-dominant; 2-3 steps walking + arm reach + grasp + place). Full-body conditioning expected to show SMALL advantage over end-effector-only (legs stabilize but are secondary actors; EA-WM-style end-effector heatmaps may suffice).\n- Task 2: Ball-kicking with targeted placement (locomotion + foot contact; kicking approach + leg swing + follow-through). Full-body conditioning expected to show LARGE advantage over end-effector-only (legs are primary actors; end-effector-only conditioning misses the entire action chain). This replicates Dream2Act's ball-kicking evaluation (40% success, zero-shot real robot) in the IDM training data synthesis context.\nThe within-paper prediction — Ablation B advantage is larger for Task 2 than Task 1 — is directly testable and makes the ablation informative regardless of direction.\n\nTHREE ABLATIONS:\n\nABLATION A (in-loop vs. post-hoc, vs. Dream2Act approach B): Same IDM, same policy training, same evaluation — only video source differs. URDF-DiT-generated videos vs. vanilla Wan 2.2 videos post-processed with URDF-IK (identical to Dream2Act's kinematic extraction stage B). Tests whether conditioning throughout denoising outperforms correcting afterward for synthetic training data quality. Both tasks.\n\nABLATION B (full-body 29 DoF vs. end-effector-only, vs. EA-WM scope): Same IDM, same policy training, same evaluation — only conditioning scope differs. Full-body 29 DoF Gaussian heatmaps (all joints) vs. end-effector-only heatmaps (~5 DoF: wrist + hand positions only). Evaluated on BOTH tasks; predicted differential: small advantage on Task 1, larger advantage on Task 2. If this prediction holds, it empirically validates the task-dependent conditioning hypothesis. Both directions of the Task 2 result are publishable: large advantage = full-body conditioning necessary for whole-body contact; small advantage = end-effector conditioning sufficient even for contact tasks, simplifying design.\n\nABLATION C (Gaussian heatmaps vs. BridgeV2W-style binary masks, new): Same ControlNet injection architecture — only conditioning representation differs. URDF-DiT Gaussian heatmaps (continuous, per-joint scalar fields encoding kinematic structure + individual joint angles) vs. BridgeV2W-style pixel-aligned binary embodiment masks (encoding link occupancy but not individual joint-angle state). Both applied to full-body 29 DoF conditioning on Task 1. Tests whether the continuous Gaussian representation encoding joint-angle information produces better IDM training data than binary link-occupancy masks. If Gaussian heatmaps show ≥5pp advantage on downstream policy success, this empirically justifies the representational choice over BridgeV2W's mask approach and differentiates URDF-DiT's technical contribution.\n\nPRIMARY SCIENTIFIC CLAIMS (ordered by expected strength):\n1. Ablation C: Gaussian heatmaps > binary embodiment masks for IDM training data quality (expected positive; continuous joint-angle encoding should help IDM extract accurate trajectories)\n2. Ablation B on Task 2 (ball-kicking): Full-body conditioning > end-effector-only (expected positive; legs are primary actors)\n3. Ablation A: In-loop conditioning > post-hoc URDF-IK (expected positive; prevents kinematically infeasible transitions vs. correcting afterward)\n\nFK RESIDUAL LOSS: Per-frame FK residual consistency loss penalizes deviations between joint positions in generated video frames and URDF FK predictions. Reduces temporal joint jitter and prevents joint-limit violations during denoising. Separate from visual domain gap handling: domain-randomized Isaac Lab rendering during IDM training (lighting, camera noise, surface material variation) addresses the visual gap between Wan 2.2 outputs and Isaac Lab rendering — two distinct mechanisms for two distinct problems.\n\nIDM SETUP: Sim-bootstrapped IDM trained on (frame_t, frame_{t+k}, joint-velocity) tuples from G1 Isaac Lab rollouts under domain-randomized conditions; applied zero-shot to URDF-DiT-generated videos. If joint-limit violation rate > 15% at Day 3 checkpoint, IDM adapter fine-tuned on ~200 URDF-DiT/Isaac Lab matched frame pairs (~8h additional compute) activates.\n\nDIFFERENTIATING DREAM2ACT PRECISELY: Dream2Act approach B = post-generation 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK, applied after all video frames are produced using Seedance 2.0. URDF-DiT conditions the Wan 2.2 denoising process itself with FK heatmaps at every step. Ablation A is not a comparison of video backbones (Seedance 2.0 vs. Wan 2.2) — it controls for backbone by using vanilla Wan 2.2 in both branches, varying only kinematic enforcement timing.\n\nCORL 2026 EVALUATION SCOPE: Isaac Lab G1 locomanipulation (pick-and-place + ball-kicking), 3 ablations (A, B, C). Dream2Act ball-kicking (40% success, zero-shot real robot) serves as a contextual reference for ball-kicking difficulty, not a direct comparison (different backbone, evaluation setting, and objective). Covers 1 of 3 user-required benchmarks.\n\nICLR 2027 FULL PAPER: All 3 user-required benchmarks (Isaac Lab G1 multi-task, HumanoidBench H1, RoboCasa365 humanoid kitchen); full ablation suite including ControlNet frozen backbone vs. EA-WM LoRA fine-tuning; geometric FK vs. EVA-style learned IDM reward; cross-embodiment generalization of conditioning granularity findings.",

  "resource_estimate": {
    "corl2026_scoped_auto": {
      "gpu_hours": "~150h H100 total (Ablation C adds ~15-20h vs. prior 130h estimate; compressed to ~14-19h wall clock on 8 H100s)",
      "gpu_utilization": "Near-zero idle (~88-92% effective utilization) — IDM training queued immediately after ControlNet checkpoint; Ablation C (binary mask variant) trained in parallel with Ablation B",
      "timeline": "19 days (May 10 → May 29, 2026 CoRL deadline) with 8+ H100s available from Day 1",
      "team": "0 (4h Day 1 setup: Isaac Lab G1 motion library including ball-kicking primitives, domain-randomized rendering, URDF-DiT scaffold, evaluation harness for both tasks)",
      "estimated_gpu_cost": "~$480 (150h × $3.20/hr) spread across 8 GPUs",
      "day_by_day_plan": "Day 1: env setup (Isaac Lab G1 with pick-and-place + ball-kicking, Wan 2.2 base, eval harness for both tasks, binary embodiment mask renderer for Ablation C). Days 2-3: implement FK heatmap encoder + zero-conv injection (Gaussian), binary mask encoder (same ControlNet architecture, Ablation C variant), post-hoc vanilla Wan 2.2 + URDF-IK baseline (Ablation A). Days 3-5: ControlNet Gaussian heatmap training 35-50h GPU (~5-7h wall clock); binary mask ControlNet training in parallel. Days 4-5: IDM training in parallel (~25h GPU, ~3h wall clock). Days 5-9: generate evaluation videos from all variants (URDF-DiT Gaussian full-body, URDF-DiT Gaussian end-effector-only, URDF-DiT binary masks, vanilla+post-hoc IK) for both tasks (~45h GPU, ~6h wall clock). Days 7-12: Isaac Lab G1 policy evaluation on all trajectory sources for both tasks (simulation rollouts — wall-clock bottleneck: parallel episode execution on pick-and-place + ball-kicking). Days 12-14: results analysis. Day 14 DECISION GATE (see pivot_criteria). Days 14-19: agent-assisted LaTeX drafting.",
      "pivot_criteria": {
        "description": "Day 14 decision gate with concrete metric thresholds across three ablations and two tasks. Calibration: Isaac Lab G1 pick-and-place from clean teleoperation demos achieves ~92% success; IDM extraction from generated video yields substantially lower rates due to visual noise. Thresholds are relative to the vanilla Wan 2.2 + post-hoc URDF-IK baseline.",
        "submit_to_corl": {
          "condition": "ALL four: (1) URDF-DiT trained policy success ≥ 20% on at least one task (non-trivial absolute performance); (2) URDF-DiT > vanilla+post-hoc baseline by ≥ 5pp on Ablation A (in-loop conditioning advantage); (3) joint-limit violation rate ≤ 10% in URDF-DiT generated videos; (4) AT LEAST ONE of the following novelty conditions holds: [B-large] full-body ≥ end-effector-only by ≥ 5pp on ball-kicking (Task 2 confirms task-dependent conditioning hypothesis), OR [C-positive] Gaussian heatmaps ≥ binary masks by ≥ 5pp on pick-and-place (conditioning representation matters)",
          "strong_submission_additionally": "Both [B-large] and [C-positive] hold, plus Ablation B shows smaller advantage on pick-and-place than ball-kicking (within-paper prediction confirmed)"
        },
        "pivot_to_iclr_2027": {
          "condition": "ANY of: (1) Ablation A not positive (URDF-DiT fails to exceed baseline by ≥ 5pp — primary engineering claim unsupported); (2) BOTH [B-large] and [C-positive] fail (neither full-body scope nor Gaussian representation shows advantage — no defensible novel claim over EA-WM + BridgeV2W at CoRL level); (3) absolute success < 15% on both tasks (IDM domain gap too large); (4) violation rate > 15% AND contingency adapter fails; (5) only Ablation A is positive but [B-large] and [C-positive] both fail — the paper's claim reduces to 'in-loop conditioning helps' which is demonstrable but insufficient differentiation at CoRL 2026 given EA-WM + BridgeV2W",
          "note": "ICLR 2027 pivot preserves all GPU investment — same implementation, full benchmark coverage (all 3 user-required platforms), deeper ablation suite including ControlNet-frozen vs. EA-WM LoRA. Negative finding on [B-large] + [C-positive] becomes the ICLR 2027 message: 'We find that kinematic conditioning approach (representation, scope, timing) matters less than assumed for whole-body contact IDM training quality; we characterize the remaining bottleneck (IDM domain gap, not conditioning design).' A clean negative result well-characterized is ICLR-worthy.",
          "removed_contingency": "The 'submit with reframing' contingency from prior rounds (Ablation B < 3pp → reframe as end-effector conditioning suffices) is REMOVED. With EA-WM + BridgeV2W now in the landscape, a paper showing its primary novel extension (full-body scope, Gaussian heatmaps) provides no advantage is not a CoRL-level contribution. Pivot to ICLR 2027 is the correct response."
        }
      },
      "scope": "2 tasks (Isaac Lab G1 pick-and-place + ball-kicking), 3 ablations (A: in-loop vs. post-hoc; B: full-body vs. end-effector-only; C: Gaussian heatmaps vs. binary embodiment masks). HumanoidBench and RoboCasa365 deferred to ICLR 2027. Covers 1 of 3 user-required benchmarks.",
      "feasibility_risk": "HIGH. Estimated 55-65% probability of submittable results by May 29 in auto mode (slightly lower than prior 60-70% estimate due to added Ablation C; offset by stronger novelty position if any ablation is positive). Key risks: (1) Ablation C binary mask renderer integration (~4h implementation; manageable); (2) Ball-kicking Isaac Lab setup may require additional motion library configuration vs. pick-and-place; (3) IDM domain gap. Day 14 decision gate with four-condition check is the unambiguous pivot trigger.",
      "requirement": "8+ H100s available from Day 1 (May 10). Fewer than 8 GPUs makes May 29 deadline infeasible — target ICLR 2027."
    },
    "manual": {
      "note": "ICLR 2027 full paper mode (all 3 user-required benchmarks). Incompatible with CoRL 2026.",
      "gpu_hours": "~150-170h H100 (Ablation C adds 15-20h vs. prior estimate; ControlNet 35-70h + IDM 25h + video gen/eval 40h + ablations 30h + data prep 10h)",
      "gpu_utilization": "~40-50% effective (sequential experiment launches, human debugging)",
      "timeline": "4-6 months (ICLR 2027 submission ~October 2026)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$480-$544",
      "benchmark_coverage": "FULL — Isaac Lab G1 locomanipulation (pick-and-place + ball-kicking), HumanoidBench H1 whole-body, RoboCasa365 humanoid kitchen. Meets all 3 user-required benchmarks."
    },
    "human_in_loop": {
      "note": "ICLR 2027 full paper mode. Incompatible with CoRL 2026.",
      "gpu_hours": "~175h H100",
      "gpu_utilization": "~60-65% effective",
      "timeline": "5-8 weeks (ICLR 2027 submission ~October 2026)",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "~$150-300 (Opus, ~1,500-2,000 turns)",
      "estimated_gpu_cost": "~$560",
      "benchmark_coverage": "FULL — all 3 user-required benchmarks."
    },
    "auto_research": {
      "note": "ICLR 2027 full paper mode (all user-required evaluation platforms). For CoRL 2026 scoped version, see corl2026_scoped_auto above.",
      "gpu_hours": "~220h H100 (full ablation suite including Ablation C across all 3 benchmarks + ControlNet-frozen vs. EA-WM LoRA ablation + geometric FK vs. EVA RL reward ablation)",
      "gpu_utilization": "~88-92% effective",
      "timeline": "1-2 weeks with 8+ H100s; 3-4 weeks on 4 GPUs",
      "team": "0 (initial setup ~4h)",
      "claude_api_cost": "~$400-700 (Opus, ~4,000-7,000 turns)",
      "estimated_gpu_cost": "~$704",
      "benchmark_coverage": "FULL — all 3 user-required benchmarks.",
      "risk_note": "Automated evaluation harness includes per-frame kinematic consistency checks (FK residual, joint-limit violation rate, temporal flicker score) and task success across pick-and-place, ball-kicking, HumanoidBench, and RoboCasa365 tasks. If FK residual loss is insufficient (violation rate >15%), agent triggers IDM adapter contingency (~8h) automatically."
    }
  },

  "target_venues": [
    "CoRL 2026 (paper deadline May 29, 2026 — 19 days from today): FEASIBLE only in auto-research mode with 8+ H100s from Day 1. ⚠️ COVERS ONLY 1 OF 3 USER-REQUIRED BENCHMARKS. Requires positive result on at least one of [B-large] or [C-positive] in addition to Ablation A for defensible novelty over EA-WM + BridgeV2W. Day 14 decision gate: submit if success ≥ 20% AND Ablation A positive AND (ball-kicking full-body advantage ≥ 5pp OR Gaussian vs. binary masks ≥ 5pp); pivot to ICLR 2027 otherwise. Estimated 55-65% probability of submittable results. 'Submit with reframing on negative Ablation B' contingency removed — with EA-WM + BridgeV2W in landscape, negative ablations are not a CoRL-level contribution.",
    "ICLR 2027 (expected submission deadline ~October 2026): RECOMMENDED for full user-required benchmark coverage. Covers all 3 platforms. All operation modes compatible. If CoRL pivot occurs, negative findings on any ablation can be reframed as 'we characterize the remaining bottleneck for humanoid whole-body IDM training data synthesis' — publishable as a well-powered empirical study.",
    "CoRL 2027 (fallback if ICLR 2027 results are negative)"
  ],

  "key_references": [
    "DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories (arXiv 2025) — validates video-diffusion → IDM pipeline for tabletop manipulation.",
    "Dream2Act / Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis (arXiv:2603.19709, March 2026) — TWO DISTINCT COMPONENTS: (A) video generation modality: robot-native visual space via Seedance 2.0 (ByteDance) hallucinating G1 body; (B) kinematic extraction: post-generation 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK. Achieves 37.5% overall (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%) vs. 0% human-centric retargeting; spatial alignment error 0.14m. Targets zero-shot real-robot execution. URDF-DiT Ablation A tests in-loop FK conditioning vs. Dream2Act's approach B for synthetic training data quality.",
    "BridgeV2W (arXiv:2602.03793, February 2026) — ARCHITECTURALLY PROXIMATE PRIOR WORK: converts coordinate-space actions into pixel-aligned BINARY EMBODIMENT MASKS rendered from URDF + camera parameters; injects via ControlNet-style pathway into pretrained video DiT; applies flow-based motion loss. Evaluates on DROID (single-arm) and AgiBot-G1 (dual-arm). Downstream = policy evaluation and goal-conditioned planning. URDF-DiT differentiates: (a) continuous Gaussian joint-position heatmaps encoding per-joint kinematic structure and individual joint angles vs. binary link-occupancy masks; (b) full-body humanoid 29 DoF whole-body contact vs. arm/dual-arm manipulation; (c) IDM training data generation vs. policy evaluation/planning. Ablation C directly compares conditioning representations under identical ControlNet injection.",
    "EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields (arXiv:2605.06192, May 2026) — KVAF = truncated Gaussian heatmaps at projected end-effector locations + depth-aware arm structures + joint landmarks + gripper geometry + pose cues. Event-aware bidirectional dual-stream fusion via shared event representations generating per-token event gates. Uses LoRA fine-tuning (rank 32) applied to main Wan 2.2 DiT + KVAF branch + KVAF head (NOT a frozen backbone — distributes updates across both branches). Evaluates on WorldArena benchmark (RoboTwin dataset, arm/bimanual tasks); no policy training output. 'EA' = Event-Aware (not Embodiment-Aware). URDF-DiT differentiates: full-body 29 DoF vs. end-effector-focused KVAF (Ablation B); ControlNet frozen backbone vs. LoRA fine-tuning; IDM→policy pipeline.",
    "VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis (arXiv:2604.09330, April 2026) — jointly denoises video+action via flow matching for arm manipulation (7-16 DoF); 45% on AgiBot G1 dual-arm grasping vs. 8% IDM baseline; no URDF kinematic constraints. Architecture routes compact global video context to action branch via adaptive 3D pooling but does not inject action signals back into video denoising, leaving video generation unconstrained by action-space feasibility.",
    "EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards (arXiv:2603.17808, March 2026) — RL post-training using IDM-derived reward signals; soft executability constraint; bimanual tabletop (RoboTwin 2.0). Distinct from URDF-DiT: soft learned reward vs. hard geometric FK constraint at every diffusion step.",
    "FlowAct-R1: Towards Interactive Humanoid Video Generation (arXiv:2601.10103, January 2026) — real-time interactive digital human character animation (NPCs) via MMDiT with audio/text control at 25fps; not physical robot URDF kinematics or IDM policy extraction.",
    "KStar Diffuser (arXiv:2503.10743, CVPR 2025) — URDF-parsed spatial-temporal graph with differentiable FK for bimanual action diffusion (68.2% vs. 33.9%); policy layer, not video synthesis. Complementary.",
    "Kinema4D (arXiv March 2026, NTU) — URDF-driven FK for 4D pointmap scene realism; not policy-data generation or DiT attention injection.",
    "Controllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026) — per-frame 2D skeleton-sequence conditioning in video diffusion for human motion synthesis; closest video-generation analogue to URDF-DiT's conditioning mechanism; human motion, not robot URDF or policy extraction.",
    "HumanoidBench (arXiv:2403.10506, 2024) — 27 tasks (H1/Digit, MuJoCo); ICLR 2027 evaluation target.",
    "RoboCasa365 (arXiv:2603.04356, ICLR 2026) — 365 kitchen tasks with humanoid support; ICLR 2027 evaluation target.",
    "X-Humanoid (arXiv Dec 2025); MITTY (arXiv 2025); G-DReaM (arXiv 2025)"
  ],

  "description": "⚠️ USER REQUIREMENT TRADEOFF: The user required evaluation on three platforms — Isaac Lab G1 locomanipulation, HumanoidBench, and RoboCasa365. CoRL 2026 covers ONLY Isaac Lab G1 (1 of 3). User must confirm: (A) CoRL 2026 with partial coverage now + ICLR 2027 for full coverage; or (B) ICLR 2027 directly with full coverage from the start. Unresolved pending user decision.\n\nNOVELTY REPOSITIONING: ControlNet + URDF conditioning for robot video DiTs is established by BridgeV2W (binary embodiment masks, arm/dual-arm, Feb 2026) and EA-WM (Gaussian end-effector heatmaps via LoRA, arm tasks, May 2026). URDF-DiT is NOT positioned as a novel conditioning architecture. Its contribution is: (1) first application to full-body humanoid 29 DoF whole-body contact interaction tasks; (2) first systematic study comparing three conditioning design choices (in-loop vs. post-hoc, full-body vs. end-effector, Gaussian heatmaps vs. binary masks) on IDM training data quality; (3) task-dependent conditioning hypothesis tested across arm-dominant (pick-and-place) and whole-body (ball-kicking) tasks.\n\nTHREE INDEPENDENT ABLATIONS: (A) in-loop URDF-DiT vs. vanilla Wan 2.2 + post-hoc URDF-IK — tests Dream2Act's extraction approach for synthetic data; (B) full-body 29 DoF vs. end-effector-only Gaussian heatmaps — tests EA-WM's scope limitation; (C) Gaussian joint-position heatmaps vs. BridgeV2W-style binary embodiment masks — tests conditioning representation. Paper holds CoRL-level novelty if any two of three ablations are positive, or if Ablation A + either [B-large] or [C-positive] holds.\n\nDAY 14 PIVOT GATE: Submit to CoRL if (1) ≥20% success on at least one task; (2) Ablation A ≥5pp improvement; (3) violation rate ≤10%; (4) [B-large: ball-kicking full-body advantage ≥5pp] OR [C-positive: Gaussian heatmaps advantage ≥5pp]. Pivot to ICLR 2027 if conditions fail — all GPU investment preserved, negative findings characterize IDM domain gap bottleneck for ICLR. 'Submit with reframing on negative Ablation B' contingency removed — insufficient novelty over EA-WM + BridgeV2W.\n\nTECHNICAL CLARIFICATIONS: EA-WM uses LoRA rank 32 (not full fine-tuning); KVAF includes Gaussian heatmaps specifically at end-effectors plus additional visual fields. BridgeV2W uses binary pixel-aligned link-occupancy masks (not continuous; not Gaussian; not per-joint). VAG routes video context to action branch via adaptive 3D pooling but does not inject action signals back into video denoising — its video generation is unconstrained by action-space feasibility."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf1d6931-6cd0-4b22-adbe-8aebbf2a9634",
  "isSidechain": false,
  "requestId": "req_011Catw6kbEzwksMGwWYWP7G",
  "type": "assistant",
  "uuid": "983912f1-7ef8-42a8-b707-571371084d46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AE8LYft4XPtsq6q5bnkPEa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1664,
      "cache_read_input_tokens": 46619,
      "output_tokens": 10770,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10770,
          "cache_read_input_tokens": 46619,
          "cache_creation_input_tokens": 1664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1664
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

_source line 29 · 2026-05-10T13:06:29.817Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01VmCdVtGDVC15WYo17cJWk8`</summary>

```json
{
  "todos": [
    {
      "content": "Write complete major-revision JSON for URDF-DiT round 7",
      "status": "completed",
      "activeForm": "Writing revised JSON"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "983912f1-7ef8-42a8-b707-571371084d46",
  "isSidechain": false,
  "requestId": "req_011Catw6kbEzwksMGwWYWP7G",
  "type": "assistant",
  "uuid": "9749ae3d-9d72-4b16-8440-94ddf007d267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AE8LYft4XPtsq6q5bnkPEa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1664,
      "cache_read_input_tokens": 46619,
      "output_tokens": 10770,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10770,
          "cache_read_input_tokens": 46619,
          "cache_creation_input_tokens": 1664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1664
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

_source line 30 · 2026-05-10T13:06:29.823Z_

<details><summary>↩ Tool result · `toolu_01VmCdVtGDVC15WYo17cJWk8`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9749ae3d-9d72-4b16-8440-94ddf007d267",
  "isSidechain": false,
  "promptId": "3abb6fbf-dc12-41d6-81de-bd436aa09aac",
  "type": "user",
  "uuid": "676e20c9-cb41-4d5a-9e43-b56a1e9dead3",
  "toolUseResult": {
    "oldTodos": [
      {
        "content": "Write complete major-revision JSON for URDF-DiT round 7",
        "status": "in_progress",
        "activeForm": "Writing revised JSON"
      }
    ],
    "newTodos": [
      {
        "content": "Write complete major-revision JSON for URDF-DiT round 7",
        "status": "completed",
        "activeForm": "Writing revised JSON"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "9749ae3d-9d72-4b16-8440-94ddf007d267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"URDF-DiT: Does Full-Body Kinematic Conditioning Throughout Denoising I…",
  "leafUuid": "676e20c9-cb41-4d5a-9e43-b56a1e9dead3",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Full-body kinematic conditioning for humanoid whole-body contact video generation",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---

### Assistant

_source line 33 · 2026-05-10T13:06:41.368Z_

**What changed and why (major revision rationale):**

**Three substantive improvements break the stagnation:**

1. **BridgeV2W added with precise technical differentiation** — confirmed via WebFetch that it uses binary pixel-aligned embodiment masks (not Gaussian heatmaps), arm/dual-arm only, downstream = policy evaluation/planning (not IDM training). Ablation C (Gaussian heatmaps vs. binary masks) is now a third independent testable claim, giving the paper three chances at a positive finding instead of one.

2. **EA-WM description corrected** — confirmed it uses LoRA rank 32 (not full fine-tuning), and that its KVAF Gaussian heatmaps are specifically end-effector-focused. The "40% fewer trainable parameters" claim was removed as it doesn't hold cleanly against LoRA. Novelty claim now correctly positioned as ControlNet frozen backbone (different compute allocation for a training-data synthesis objective) vs. EA-WM LoRA.

3. **Task design fixed to actually stress-test Ablation B** — pick-and-place is arm-dominant; it's unlikely to show a large full-body conditioning advantage. Ball-kicking (legs are the primary actors) is added as the second evaluation task. This creates a within-paper testable prediction (full-body advantage scales with whole-body coordination required), making Ablation B informative regardless of direction and fixing the core reason prior rounds kept scoring 3.0–3.2.

**"Submit with reframing" contingency removed**: with EA-WM + BridgeV2W in the landscape, a negative Ablation B alone produces a paper with no defensible novel claim. ICLR 2027 pivot is the correct response — where a systematic negative finding about what conditioning choices actually matter becomes the contribution itself.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "676e20c9-cb41-4d5a-9e43-b56a1e9dead3",
  "isSidechain": false,
  "requestId": "req_011CatwNqmV4bXvyNXitgNhh",
  "type": "assistant",
  "uuid": "a964539a-9765-47c6-8235-c94a7303de8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MmPn54e3VjVsLLKfSPpqop",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10812,
      "cache_read_input_tokens": 48283,
      "output_tokens": 423,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10812,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 423,
          "cache_read_input_tokens": 48283,
          "cache_creation_input_tokens": 10812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10812
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"URDF-DiT: Does Full-Body Kinematic Conditioning Throughout Denoising I…",
  "leafUuid": "a964539a-9765-47c6-8235-c94a7303de8c",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Full-body kinematic conditioning for humanoid whole-body contact video generation",
  "sessionId": "3eca5a12-2fc4-436c-9188-e19cda922486"
}
```

---
