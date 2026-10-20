# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-18 (UTC).** ## Original idea { "tit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 68
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/exported-trajectories/account-2/3df479bc-9246-4cd8-86a4-5261455de34a.jsonl`
- **Structured JSON:** [`aba903f7d9767f168b2e.json`](../../sessions/ab/aba903f7d9767f168b2e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T20:32:20.578Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T20:32:20.578Z",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-18 (UTC).**\n\n## Original idea\n{\n  \"title\": \"LACVLA: Enforcing Language-Affordance Grounding via Consistency Objectives for Zero-Shot Cross-Category VLA Manipulation\",\n  \"core_problem\": \"How can end-to-end VLA models achieve zero-shot affordance transfer to unseen object categories, given the empirical finding that current VLAs largely ignore language instructions (LIBERO-Plus, CVPR 2026; LangGap, Mar 2026) — a failure mode that is catastrophic for cross-category transfer where novel objects lack visual priors and language is the only available guide for spatial grounding?\",\n  \"opportunity\": \"Recent diagnostic work has exposed a fundamental flaw in VLAs: LIBERO-Plus (CVPR 2026, arXiv 2510.13626) shows VLAs are largely insensitive to language variations and tend to ignore language instructions entirely, exhibiting positional bias rather than genuine semantic understanding. LangGap (arXiv 2603.00592, Mar 2026) quantifies this: VLAs with 95%+ standard success largely ignore language; targeted data augmentation partially closes the gap (0%→90% single-task, 0%→28% multi-task) but proves fundamentally insufficient as semantic diversity increases. This language-ignoring failure is survivable in-distribution — visual priors and layout memorization compensate — but becomes catastrophic for cross-category zero-shot transfer, where the model encounters objects with no visual precedent and must rely on language to determine WHERE to interact. Spatial grounding approaches (ST4VLA, ICLR 2026; InternVLA-M1; SpatialVLA, RSS 2025) improve performance broadly but do not structurally guarantee language conditioning — a model can learn spatial shortcuts that generalize within training categories but fail on novel objects. LIBERO-Para (Mar 2026) quantifies this fragility: VLAs suffer 22–52pp success rate drops under paraphrased instructions, with 80–96% of failures from planning-level trajectory divergence. Shin (Mar 2026) attempts LLM-generated paraphrase augmentation but achieves only +1.71pp improvement, consistent with LangGap's finding that augmentation alone hits a ceiling. PPCL (EACL 2024) showed consistency regularization beats augmentation with 10× fewer samples in NLP. The opportunity: an affordance-gated architectural bottleneck with self-supervised consistency objectives that structurally force language to condition spatial grounding — making language a mandatory pathway for action generation rather than an ignorable input — enabling genuine cross-category zero-shot transfer without 3D sensors, expensive cross-category annotations, or modular decomposition.\",\n  \"landscape\": \"The VLA-affordance landscape has five relevant lineages, none of which structurally enforces language conditioning of spatial affordance representations for cross-category transfer. (1) Spatially-guided VLAs: ST4VLA (ICLR 2026, arXiv 2602.10109) introduces dual-system spatial grounding (Qwen2.5-VL planner + DiT/DINOv2 action expert), achieving 95.9% LIBERO average (98.0% Spatial, 99.0% Object, 93.8% Goal, 92.6% Long), 72%/61% attribute/spatial paraphrase robustness (vs π₀: 32%/31%), and 62% on new object instances (vs π₀: 32%, GR00T N1: 46%). This is LACVLA's strongest baseline — the null hypothesis is 'does explicit affordance consistency add value beyond spatial grounding alone?' InternVLA-M1 (arXiv 2510.13778) extends this with affordance recognition and chain-of-thought reasoning in pre-training. SpatialVLA (RSS 2025, arXiv 2501.15830) introduces Ego3D Position Encoding and Adaptive Action Grids. Spatial Forcing (ICLR 2026, arXiv 2510.12276) aligns VLM features with 3D foundation models without 3D input at inference. All improve spatial understanding but none guarantees language conditions the spatial representation — LIBERO-Plus (CVPR 2026) shows even top VLAs still ignore language. (2) Language grounding diagnostics: LIBERO-Plus (CVPR 2026, arXiv 2510.13626) reveals VLAs are insensitive to language and exhibit positional bias, with performance dropping from 95% to below 30% under camera/robot state perturbations. LangGap (arXiv 2603.00592, Mar 2026) confirms VLAs ignore language and shows data augmentation's ceiling (28% multi-task). LIBERO-Para (arXiv 2603.28301, Mar 2026) quantifies paraphrase fragility (22–52pp drops). Shin (arXiv 2603.16044, Mar 2026) achieves only +1.71pp via augmentation. Stable Language Guidance / RSS (ACL 2026, arXiv 2601.04052) addresses modality collapse at inference via residual steering — complementary to LACVLA's training-time approach. (3) Modular affordance-then-action pipelines: RT-Affordance (arXiv 2411.02704), UAD (ICRA 2025), RAM (CoRL 2024), RAAP (arXiv 2603.29419, Mar 2026), AffordDP (CVPR 2025), RoboMAP (arXiv 2510.10912), A0 (ICCV 2025, arXiv 2504.12636), and GLOVER++ (CoRL 2025, arXiv 2505.11865) all produce affordance representations but feed them to separate downstream planners/policies, sacrificing end-to-end optimization. A0 achieves zero-shot cross-category transfer via 1M contact points but without language conditioning of the affordance representation. (4) Affordance-aware VLA reasoning and pre-training: CoA-VLA (ICCV 2025) and Sim2Real VLA (ICLR 2026) incorporate affordances via text chains. PokéVLA (arXiv 2604.20834, Apr 2026) pre-trains a VLM on HOVA-500K for affordance understanding, validating ego-centric→VLA transfer, but uses affordance only for backbone pre-training rather than as an explicit consistency objective. (5) Architectural bottleneck enforcement: DIAL (arXiv 2603.29844, Mar 2026) enforces a latent intent bottleneck via inverse dynamics — the action head MUST use predicted latent intent because it resolves the discrepancy between current and predicted states. This inspires LACVLA's affordance-gated bottleneck (stop-gradient on VLM features before action head, affordance map as spatial attention gate). (6) Cross-category zero-shot benchmarks: AGNOSTOS/X-ICM (arXiv 2505.15660) provides 23 unseen manipulation tasks for cross-task evaluation; VLA² (arXiv 2510.14902) uses agentic retrieval for unseen concepts. Gap: No existing work combines (a) architectural enforcement that language must condition spatial features, (b) self-supervised consistency objectives on affordance maps (not raw actions), and (c) cross-category zero-shot transfer as the primary evaluation target.\",\n  \"approach\": \"We propose LACVLA, an end-to-end VLA that structurally forces language to condition spatial affordance grounding through an affordance-gated bottleneck and self-supervised consistency objectives, enabling zero-shot cross-category manipulation.\\n\\nArchitecture — Affordance-Gated Bottleneck (inspired by DIAL's latent intent bottleneck): Built on a 4B–7B VLM backbone (Qwen2-VL-4B via StarVLA or PaliGemma2) with LoRA fine-tuning. The architecture has three components:\\n(a) Affordance Readout: A cross-attention layer where language instruction tokens attend over intermediate VLM visual features (layer ~16 of 32 for Qwen2-VL), producing a dense affordance heatmap over the image. This encodes WHERE to interact, conditioned on the instruction. Architecture: single cross-attention + LayerNorm + linear projection to H×W heatmap, <5M parameters.\\n(b) Stop-Gradient Bottleneck: VLM intermediate visual features are passed through a stop-gradient before reaching the action head. The action head receives: affordance_heatmap ⊙ sg(VLM_visual_features) + proprioceptive_state. The affordance map acts as a spatial attention gate — if the model produces a uniform (language-ignoring) affordance map, the action head receives unselective visual features with no spatial focus, degrading performance. If the map collapses to a degenerate peak, the action head loses context. This structurally forces task-relevant WHERE information through the language-conditioned affordance bottleneck, preventing the bypass problem identified by reviewers. Unlike a soft bottleneck, the stop-gradient ensures no task-semantic gradient flows through the non-affordance pathway — the action head CANNOT learn to extract task information from raw VLM features.\\n(c) Flow-Matching Action Head: A lightweight DiT (Diffusion Transformer) that generates trajectory chunks conditioned on the affordance-gated visual features + proprioceptive state, following the flow-matching formulation.\\n\\nTraining Objectives — Three jointly optimized losses with phased schedule:\\n(1) Instruction-Paraphrase Affordance Consistency (IPAC): Given the same visual scene and K LLM-generated paraphrases of the same task instruction (e.g., 'grab the mug handle' vs. 'grasp the cup by its handle'), the affordance maps must be consistent (KL divergence penalty on spatial heatmaps). This transfers the consistency regularization principle from PPCL (EACL 2024) — which showed consistency > augmentation with 10× less data in NLP — to spatial affordance heatmaps. Unlike Shin (2026), who uses paraphrases purely as data augmentation (achieving marginal +1.71pp), IPAC uses them as a regularization signal constraining affordance geometry. Paraphrases generated offline by LLM — free, unlimited supervision.\\n(2) Instruction-Discriminative Affordance (IDA): Given the same visual scene and two semantically different instructions (e.g., 'pick up the mug by its handle' vs. 'pour from the mug'), the affordance maps must diverge (margin-based divergence loss). This prevents degenerate consistency collapse where the model produces instruction-invariant heatmaps to trivially satisfy IPAC. Different-instruction pairs come naturally from multi-task robot datasets.\\n(3) Action-Grounded Affordance (AGA): Standard flow-matching loss for trajectory prediction through the affordance-gated bottleneck. This grounds the affordance map in manipulation-relevant contact regions via end-to-end backpropagation through the gating mechanism.\\n\\nPhased Training Schedule:\\nPhase 1 — Affordance Readout Pre-training on HOVA-500K: Train the cross-attention readout to predict contact-point Gaussian heatmaps (σ proportional to object scale) conditioned on action-label text prompts from HOVA-500K's 675 action categories. Viewpoint augmentation (random crop, perspective warp, ego→third-person style augmentation) addresses the ego-centric domain gap. Diagnostic checkpoint: evaluate pre-trained affordance readout on robot observation images; if domain gap degrades affordance quality below threshold, bridge with (a) a small set of robot data with pseudo-affordance labels from action-contact heuristics and (b) cross-domain contrastive loss between HOVA-500K and robot VLM features for same-action categories. This addresses the reviewer concern that PokéVLA's backbone pre-training transfer is fundamentally different from affordance readout pre-training — we validate empirically before proceeding.\\nPhase 2 — End-to-end VLA training (steps 0–N): Fine-tune full model (VLM via LoRA + pre-trained affordance readout + flow-matching action head) on robot data. Sub-phases: (2a) AGA only for 10% of training — establish action grounding baseline. (2b) Add IPAC at 10% — enforce consistency while action loss stabilizes gradients. (2c) Ramp IDA from 0 to full weight over 15% of training via linear warmup, monitored by: (i) affordance entropy H(A) — if H(A) < 0.3 × H_max, increase IDA weight by 50%; (ii) instruction-discriminability D = mean pairwise KL between different-instruction maps on validation set — if D < 0.5, halt IPAC and boost IDA. GradNorm-style gradient normalization across the three losses balances training rates automatically.\\n\\nWhy Affordance Maps (Not Raw Actions) for Consistency: Affordance maps capture WHERE to interact — the geometric invariant across paraphrases and across categories sharing functional parts. Action distributions conflate WHERE + HOW + WHEN (trajectory shape, timing, force), making consistency regularization noisier. For cross-category transfer, WHERE is what transfers (handle locations generalize across mugs/cups/pitchers), while HOW adapts to object-specific geometry. This argument is validated empirically by ablation #6.\\n\\nCross-Object Functional Consistency via HOVA-500K: Group HOVA-500K images by shared action labels (675 categories) and apply soft KL penalty between affordance maps of same-action images from different object categories. This provides weak supervision for cross-category affordance consistency without requiring part-level functional equivalence annotations.\\n\\nData Pipeline: Open X-Embodiment and DROID for robot trajectories, HOVA-500K for affordance pre-training and cross-object grouping, LLM-generated instruction paraphrases (Qwen3 or GPT-4) for IPAC pairs.\\n\\nAblation Design (8 variants, addressing all reviewer concerns):\\n(1) Full LACVLA — affordance-gated bottleneck + IPAC + IDA + AGA\\n(2) No affordance bottleneck — direct VLA, no affordance readout (tests whether bottleneck is necessary)\\n(3) Modular composition — frozen GLOVER++ affordance → separate policy (tests end-to-end vs. modular)\\n(4) No consistency losses — only AGA through affordance bottleneck (tests whether architectural bottleneck alone suffices without consistency enforcement)\\n(5) Shin-style augmentation — paraphrases added as training data, no consistency loss (tests data augmentation ceiling, paralleling PPCL's NLP finding)\\n(6) IPAC on raw actions — KL divergence between action distributions under paraphrased instructions, no affordance readout (CRITICAL: tests whether isolating WHERE via affordance maps outperforms consistency on conflated action distributions — if affordance maps win, that's the paper's key finding; if raw actions work comparably, the affordance readout is unnecessary overhead)\\n(7) ST4VLA-style spatial grounding + IPAC on features — spatial grounding pre-training + consistency on intermediate VLM features without affordance readout (tests whether explicit affordance structure adds value beyond strong spatial pre-training + consistency, addressing the 'why not just do spatial grounding?' question)\\n(8) No phased training — all losses from step 0 (tests curriculum importance)\\n\\nEvaluation Protocol — Primary (Cross-Category Zero-Shot Transfer):\\n(a) Held-out object category experiments: partition LIBERO/DROID object categories into train/test sets, test on entirely unseen categories with both standard and paraphrased instructions\\n(b) HOVA-500K cross-category transfer tests: train on K action categories with one set of objects (e.g., 'pour from pitcher'), test on same actions with different object categories (e.g., 'pour from kettle') — constructed from HOVA-500K's 675 shared action labels\\n(c) AGNOSTOS benchmark (arXiv 2505.15660) for cross-task zero-shot evaluation (23 unseen tasks)\\n(d) Real-world evaluation on 5+ unseen object categories across at least 3 manipulation primitives (grasp, pour, push)\\n\\nEvaluation Protocol — Secondary:\\n(e) LIBERO-Para benchmark with PRIDE metric for paraphrase robustness (direct comparison with ST4VLA's 72%/61%)\\n(f) LangGap protocol for language grounding quality (targeting improvement over the 28% multi-task ceiling)\\n(g) Affogato for affordance quality assessment\\n(h) Standard LIBERO (Spatial, Object, Goal, Long) for in-distribution comparison with ST4VLA (95.9% avg)\\n\\nCoRL 2026 Infeasibility Statement: The user's original objective was CoRL 2026 submission (abstract May 26, 2026 — 8 days from today, May 18). This is clearly infeasible given the implementation scope: three-loss system with phased training, affordance-gated bottleneck, HOVA-500K pre-training pipeline, 8 ablation variants, and multi-benchmark evaluation. We target AAAI 2027 (abstract Jul 21 — 64 days) as primary, WACV 2027 Round 2 (paper Aug 27 — 101 days) as backup.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~250-350h A100 80GB, equivalent to ~170-235h H100 (HOVA-500K affordance readout pre-training ~25h, 3-4 full VLA training runs at ~35-50h each with LoRA on 4B backbone, 8 ablation experiments at ~15-20h each, cross-category evaluation sweeps ~30h, AGNOSTOS benchmark runs ~15h)\",\n      \"gpu_utilization\": \"~15-25% effective utilization — idle during result analysis, loss weight iteration, domain gap diagnostics between phases\",\n      \"timeline\": \"8-12 weeks (2-3 weeks data pipeline + HOVA-500K pre-training with viewpoint augmentation + domain gap diagnostics; 4-6 weeks iterative experimentation including all 8 ablations; 2-3 weeks cross-category evaluation + paper writing)\",\n      \"team\": \"2 researchers (1 lead on affordance-gated architecture + consistency objectives + bottleneck enforcement, 1 on data pipeline/HOVA-500K integration/cross-category evaluation/AGNOSTOS setup)\",\n      \"estimated_gpu_cost\": \"$375-525 (at ~$1.50/h A100 80GB on RunPod/Jarvislabs)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~320-450h A100 80GB, equivalent to ~215-300h H100 (agent runs 10-14 training configurations systematically, all 8 ablations + 2-4 additional hyperparameter variants, HOVA-500K pre-training, with wasted runs caught early by human)\",\n      \"gpu_utilization\": \"~40-55% — agent queues experiments but pauses at key gates: (1) HOVA-500K domain gap diagnostic before Stage 2, (2) affordance map quality inspection after bottleneck warmup, (3) cross-category held-out split design approval\",\n      \"timeline\": \"6-9 weeks (agent handles paraphrase generation, HOVA-500K preprocessing with viewpoint augmentation, hyperparameter sweeps, AGNOSTOS/LIBERO-Para/LangGap evaluation scripts; human approves domain gap bridging strategy, inspects affordance maps, validates cross-category split design)\",\n      \"team\": \"1 researcher, ~1.5h/day review\",\n      \"claude_api_cost\": \"$200-500 (estimated 2,000-5,000 agent turns)\",\n      \"estimated_gpu_cost\": \"$480-675 (at ~$1.50/h A100 80GB)\",\n      \"risk_note\": \"Primary risk: HOVA-500K affordance readout pre-training domain gap — mitigated by viewpoint augmentation and diagnostic checkpoint before Stage 2. Secondary risk: affordance-gated bottleneck may be too restrictive, causing performance collapse — mitigated by ablation #4 (bottleneck without consistency) to isolate the effect. ST4VLA comparison (ablation #7) will determine if the approach adds value beyond spatial grounding.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~650-1000h A100 80GB, equivalent to ~435-670h H100 (agent explores 18-28 training configurations for phased schedule tuning, all 8 ablation variants × 2-3 seeds, HOVA-500K pre-training with multiple viewpoint augmentation strategies, full benchmark sweeps)\",\n      \"gpu_utilization\": \"~85-95% — agent immediately queues next experiment upon completion; parallel ablation runs on multi-GPU setup\",\n      \"timeline\": \"3-4 weeks with 4+ A100 GPUs available concurrently (bottleneck: HOVA-500K pre-training → domain gap diagnostic → phased training search → cross-category evaluation)\",\n      \"team\": \"0 researchers after initial setup (~6-8 hours: dataset access, paraphrase generation config, HOVA-500K preprocessing, AGNOSTOS/LIBERO-Para/LangGap environment setup, cross-category held-out split definition)\",\n      \"claude_api_cost\": \"$500-1,200 (estimated 5,000-12,000 agent turns)\",\n      \"estimated_gpu_cost\": \"$975-1,500 (at ~$1.50/h A100 80GB)\",\n      \"speed_bottleneck\": \"Each LoRA training run on 4B backbone takes ~8-12h on 4 A100s. HOVA-500K preprocessing and viewpoint-augmented Gaussian heatmap generation ~30h one-time. Cross-category evaluation setup ~6h one-time.\",\n      \"risk_note\": \"Automated phased training managed by entropy/discriminability monitoring. If affordance-gated bottleneck causes consistent performance collapse across configurations, agent escalates to soft-gating variants (gradually opening the bottleneck). GradNorm balancing reduces sensitivity to manual loss weight tuning.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target, 64 days to abstract; strong fit for self-supervised consistency + architectural bottleneck contribution with robotics application)\",\n    \"WACV 2027 Round 2 (registration Aug 20, paper Aug 27, 2026 — realistic backup, 101 days; vision+robotics focus)\",\n    \"ICLR 2027 (abstract ~Sep 2026, full paper ~Sep 2026 — dates TBD, estimated from ICLR 2026 cycle; top-tier target if cross-category zero-shot results are strong)\",\n    \"CVPR 2027 (registration ~Nov 2026, paper ~Nov 2026 — dates TBD; if affordance visualization and cross-category transfer results are visually compelling)\",\n    \"NOTE: CoRL 2026 (abstract May 26, paper May 29) was the user's original target but is infeasible — 8 days is insufficient for implementation of affordance-gated bottleneck, 8 ablations, HOVA-500K pipeline, and multi-benchmark evaluation\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"ST4VLA: Spatially Guided Training for Vision-Language-Action Models (ICLR 2026, arXiv 2602.10109) — strongest baseline: 95.9% LIBERO avg, 72%/61% paraphrase robustness, 62% unseen objects via spatial grounding alone\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626) — diagnostic revealing VLAs ignore language instructions, exhibit positional bias\",\n    \"LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models (arXiv 2603.00592, Mar 2026) — quantifies language gap: augmentation reaches 90% single-task but only 28% multi-task\",\n    \"DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA (arXiv 2603.29844, Mar 2026) — latent intent bottleneck via inverse dynamics, inspiration for affordance-gated architecture\",\n    \"InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy (arXiv 2510.13778) — spatially guided VLA with affordance recognition in pre-training\",\n    \"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models (RSS 2025, arXiv 2501.15830) — spatial-aware action tokenization\",\n    \"Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model (ICLR 2026, arXiv 2510.12276) — implicit spatial alignment without 3D input, single-branch inspiration\",\n    \"AGNOSTOS / X-ICM: Exploring the Limits of Vision-Language-Action Manipulations in Cross-task Generalization (arXiv 2505.15660) — cross-task zero-shot benchmark with 23 unseen tasks\",\n    \"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models (arXiv 2603.28301, Mar 2026) — paraphrase robustness evaluation with PRIDE metric\",\n    \"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation (Shin, arXiv 2603.16044, Mar 2026) — direct augmentation baseline, +1.71pp only\",\n    \"Stable Language Guidance / Residual Semantic Steering for VLAs (ACL 2026, arXiv 2601.04052) — inference-time modality collapse mitigation, complementary to LACVLA's training-time approach\",\n    \"Prompt Perturbation Consistency Learning for Robust Language Models (PPCL, EACL 2024, arXiv 2402.15833) — consistency regularization > augmentation with 10× fewer samples in NLP\",\n    \"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs (arXiv 2510.14242, Oct 2025) — extends PPCL to LLMs\",\n    \"OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024) — base VLA architecture\",\n    \"StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing (arXiv 2604.05014, Apr 2026) — implementation framework\",\n    \"GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation (CoRL 2025, arXiv 2505.11865) — provides HOVA-500K dataset, modular baseline\",\n    \"PokéVLA: Empowering Pocket-Sized VLA Model with Comprehensive World Knowledge Guidance (arXiv 2604.20834, Apr 2026) — validates HOVA-500K ego→VLA transfer for backbone pre-training\",\n    \"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (arXiv 2411.02704, 2024) — modular affordance baseline\",\n    \"A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation (ICCV 2025, arXiv 2504.12636) — hierarchical affordance with zero-shot transfer but no language conditioning\",\n    \"RoboMAP: Adaptive Affordance Heatmaps via PaliGemma (arXiv 2510.10912, 2025) — modular language-conditioned heatmap architecture reference\",\n    \"AffordDP: Generalizable Diffusion Policy with Transferable Affordance (CVPR 2025) — cross-category transfer via 3D contact points\",\n    \"RAM: Retrieval-Based Affordance Transfer for Generalizable Zero-Shot Robotic Manipulation (CoRL 2024, arXiv 2407.04689) — retrieval-based affordance baseline\",\n    \"RAAP: Retrieval-Augmented Affordance Prediction with Cross-Image Action Alignment (arXiv 2603.29419, Mar 2026) — cross-image affordance alignment\",\n    \"Affogato: Learning Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale (arXiv 2506.12009, 2025) — affordance quality benchmark\",\n    \"AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation (arXiv 2604.11674, 2026) — simulation evaluation resource\",\n    \"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks (ICML 2018) — multi-task loss balancing\",\n    \"GeoVLA: Empowering 3D Representations in Vision-Language-Action Models (arXiv 2508.09071, Aug 2025) — 3D VLA baseline requiring depth sensor\",\n    \"RS-CL: Contrastive Representation Regularization for VLAs (arXiv 2510.01711, 2025) — contrastive VLA regularization on proprioceptive states only\"\n  ],\n  \"description\": \"LACVLA addresses the critical finding that VLAs largely ignore language instructions (LIBERO-Plus, CVPR 2026; LangGap, Mar 2026) — a failure mode survivable in-distribution but catastrophic for cross-category zero-shot transfer where novel objects lack visual priors. We propose an affordance-gated architectural bottleneck, inspired by DIAL's latent intent bottleneck, that structurally forces all task-relevant spatial information through a language-conditioned affordance map: VLM intermediate features pass through stop-gradient before the action head, which receives affordance_heatmap ⊙ sg(visual_features) + proprioceptive_state. The affordance map (produced via cross-attention between VLM features and language tokens) acts as a spatial attention gate — a uniform (language-ignoring) map yields unselective features and degraded performance, preventing the bypass problem. Self-supervised consistency objectives enforce language-affordance grounding: IPAC ensures semantically equivalent instructions produce identical affordance maps (transferring PPCL's consistency > augmentation principle from NLP to spatial heatmaps), while IDA ensures semantically different instructions produce divergent maps (preventing consistency collapse). A comprehensive 8-variant ablation suite addresses all key questions: (1) Does the architectural bottleneck help? (ablation #2: no bottleneck), (2) Does consistency outperform augmentation? (ablation #5: Shin-style augmentation), (3) Are affordance maps the right target? (ablation #6: IPAC on raw action distributions — the paper's critical test: if affordance maps outperform action-level consistency, it validates that isolating WHERE-to-interact from HOW-to-interact is essential), (4) Does affordance consistency add value beyond spatial grounding? (ablation #7: ST4VLA-style + IPAC on features). Evaluation is rebalanced toward the user's original objective: PRIMARY metrics target cross-category zero-shot transfer (held-out object categories, HOVA-500K cross-category splits across 675 action labels, AGNOSTOS benchmark, real-world evaluation on 5+ unseen categories), with SECONDARY metrics on paraphrase robustness (LIBERO-Para, LangGap) and affordance quality (Affogato). HOVA-500K domain gap is addressed via viewpoint augmentation and a diagnostic checkpoint before end-to-end training, with cross-domain contrastive bridging if needed. CoRL 2026 (abstract May 26 — 8 days away) is acknowledged as infeasible; the primary target is AAAI 2027 (abstract Jul 21, 64 days) with WACV 2027 Round 2 (Aug 27) as backup.\",\n  \"project_name\": \"lac_vla_zero_shot\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 5)\nIssues: [\"MISSING COMPETING WORK — GuidedVLA (RSS 2026, arXiv 2605.12369, May 12, 2026): Supervises individual action decoder attention heads with auxiliary signals for object grounding, spatial geometry, and temporal skill logic. Achieves improved in-domain and out-of-domain success rates. Conceptually adjacent to LACVLA's affordance readout supervision — both use explicit auxiliary supervision on intermediate representations to improve VLA grounding. Differentiation needed: GuidedVLA uses 3 predefined factor types (not open-vocabulary), doesn't use consistency objectives on heatmaps, doesn't target cross-category transfer. But the architectural parallel (supervised intermediate representations) must be discussed.\", \"MISSING BENCHMARK — BusyBox (arXiv 2602.05441, Feb 2026, Microsoft): Physical benchmark for VLA affordance generalization showing even strong VLAs (π₀.₅, GR00T-N1.6) struggle with affordance generalization across object variants. Directly relevant to LACVLA's cross-category transfer claims and could serve as additional evaluation.\", \"COMPUTE BUDGET BORDERLINE: Manual estimate of 250-350h A100 converts to 170-235h H100, but the user's hard constraint is ≤200 H100-hours. The upper range (235h H100) exceeds the constraint by 17.5%. The A100→H100 ratio of 1.5x is optimistic for mixed-precision transformer fine-tuning (1.3x is more conservative for some workloads, which would push 350h A100 to 269h H100). The 8 ablation variants are the main cost driver — consider which can be dropped or combined.\", \"ENTIRE PAPER'S VALUE DEPENDS ON ABLATION #6: The core claim — affordance maps are the right target for consistency regularization because they isolate WHERE-to-interact — is theoretically motivated but empirically unvalidated. If IPAC on raw action distributions (ablation #6) performs comparably to IPAC on affordance maps, the entire affordance readout + HOVA-500K pipeline becomes unnecessary overhead. This is acknowledged as a 'critical test' but represents significant experimental risk for a paper whose contribution rests on this finding.\", \"HOVA-500K DOMAIN GAP RISK REMAINS: PokéVLA validates HOVA-500K for backbone pre-training (learning general visual representations), but LACVLA uses it for affordance readout pre-training (producing pixel-level contact-point Gaussian heatmaps). The proposal includes viewpoint augmentation + diagnostic checkpoint + cross-domain contrastive bridging, but these add complexity and compute. If domain gap degrades affordance quality, Phase 2 training may learn to bypass the degraded affordance readout despite the stop-gradient bottleneck — producing low-entropy, uninformative heatmaps that satisfy IPAC trivially.\"]\nFeedback: The proposal has improved dramatically across five rounds and is now technically comprehensive with strong related work coverage. The gap is narrower than before. Specific revisions to push toward passing:\n\n1. **Add GuidedVLA (RSS 2026) to landscape.** arXiv 2605.12369, accepted to RSS 2026, supervises attention heads for object grounding + spatial geometry + temporal skill logic. Differentiate: GuidedVLA uses 3 predefined factor types, no consistency objectives, no affordance heatmaps, no cross-category transfer focus. LACVLA's affordance readout with stop-gradient bottleneck + open-vocabulary consistency is distinct but the architectural parallel must be acknowledged.\n\n2. **Trim ablation suite to fit compute budget.** 8 ablations at 15-20h each = 120-160h A100, which is 48-64% of total compute. Consider: (a) merge ablations #2 and #4 (no bottleneck vs. bottleneck without consistency — #2 subsumes #4 if you track affordance map quality for both), (b) drop ablation #8 (phased vs. non-phased training) — this is nice-to-have but not essential for the core argument. Target 6 ablations to bring compute to 180-280h A100 ≈ 120-190h H100, safely within ≤200h H100.\n\n3. **Add BusyBox as supplementary benchmark.** arXiv 2602.05441 is a physical benchmark specifically designed for VLA affordance generalization, showing even strong VLAs fail. If LACVLA performs better on BusyBox variants, that's powerful evidence for cross-category affordance transfer.\n\n4. **Strengthen the HOVA-500K fallback plan.** If domain gap diagnostic shows degraded affordance quality on robot observations: (a) fall back to self-supervised affordance readout initialization using robot data alone (action-contact heuristic labels from gripper position at grasp/contact time), (b) ablate HOVA-500K pre-training vs. self-supervised initialization to determine if HOVA-500K is actually necessary. This de-risks the paper from the HOVA-500K dependency.\n\n5. **Frame the narrative more aggressively around cross-category transfer.** The abstract/description still opens with 'VLAs ignore language' — a crowded framing shared by 8+ concurrent papers. Instead, open with: 'We address cross-category zero-shot manipulation transfer, where VLAs must generalize to objects with no visual precedent. We show that the well-documented language-ignoring failure (LIBERO-Plus, LangGap) is particularly catastrophic in this setting because language is the only available guide for spatial grounding on novel objects. Our approach: structurally force language to condition spatial affordance features via an architectural bottleneck, then enforce consistency to ensure the grounding is robust.' This positions LACVLA in a less crowded space (cross-category transfer) rather than the crowded one (fixing language bypass).\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 3.5 到 3.8，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T20:32:20.584Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T20:32:20.584Z",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

## Round 1

66 recorded events

### User

_source line 3 · 2026-05-18T20:32:20.623Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-18 (UTC).**

## Original idea
{
  "title": "LACVLA: Enforcing Language-Affordance Grounding via Consistency Objectives for Zero-Shot Cross-Category VLA Manipulation",
  "core_problem": "How can end-to-end VLA models achieve zero-shot affordance transfer to unseen object categories, given the empirical finding that current VLAs largely ignore language instructions (LIBERO-Plus, CVPR 2026; LangGap, Mar 2026) — a failure mode that is catastrophic for cross-category transfer where novel objects lack visual priors and language is the only available guide for spatial grounding?",
  "opportunity": "Recent diagnostic work has exposed a fundamental flaw in VLAs: LIBERO-Plus (CVPR 2026, arXiv 2510.13626) shows VLAs are largely insensitive to language variations and tend to ignore language instructions entirely, exhibiting positional bias rather than genuine semantic understanding. LangGap (arXiv 2603.00592, Mar 2026) quantifies this: VLAs with 95%+ standard success largely ignore language; targeted data augmentation partially closes the gap (0%→90% single-task, 0%→28% multi-task) but proves fundamentally insufficient as semantic diversity increases. This language-ignoring failure is survivable in-distribution — visual priors and layout memorization compensate — but becomes catastrophic for cross-category zero-shot transfer, where the model encounters objects with no visual precedent and must rely on language to determine WHERE to interact. Spatial grounding approaches (ST4VLA, ICLR 2026; InternVLA-M1; SpatialVLA, RSS 2025) improve performance broadly but do not structurally guarantee language conditioning — a model can learn spatial shortcuts that generalize within training categories but fail on novel objects. LIBERO-Para (Mar 2026) quantifies this fragility: VLAs suffer 22–52pp success rate drops under paraphrased instructions, with 80–96% of failures from planning-level trajectory divergence. Shin (Mar 2026) attempts LLM-generated paraphrase augmentation but achieves only +1.71pp improvement, consistent with LangGap's finding that augmentation alone hits a ceiling. PPCL (EACL 2024) showed consistency regularization beats augmentation with 10× fewer samples in NLP. The opportunity: an affordance-gated architectural bottleneck with self-supervised consistency objectives that structurally force language to condition spatial grounding — making language a mandatory pathway for action generation rather than an ignorable input — enabling genuine cross-category zero-shot transfer without 3D sensors, expensive cross-category annotations, or modular decomposition.",
  "landscape": "The VLA-affordance landscape has five relevant lineages, none of which structurally enforces language conditioning of spatial affordance representations for cross-category transfer. (1) Spatially-guided VLAs: ST4VLA (ICLR 2026, arXiv 2602.10109) introduces dual-system spatial grounding (Qwen2.5-VL planner + DiT/DINOv2 action expert), achieving 95.9% LIBERO average (98.0% Spatial, 99.0% Object, 93.8% Goal, 92.6% Long), 72%/61% attribute/spatial paraphrase robustness (vs π₀: 32%/31%), and 62% on new object instances (vs π₀: 32%, GR00T N1: 46%). This is LACVLA's strongest baseline — the null hypothesis is 'does explicit affordance consistency add value beyond spatial grounding alone?' InternVLA-M1 (arXiv 2510.13778) extends this with affordance recognition and chain-of-thought reasoning in pre-training. SpatialVLA (RSS 2025, arXiv 2501.15830) introduces Ego3D Position Encoding and Adaptive Action Grids. Spatial Forcing (ICLR 2026, arXiv 2510.12276) aligns VLM features with 3D foundation models without 3D input at inference. All improve spatial understanding but none guarantees language conditions the spatial representation — LIBERO-Plus (CVPR 2026) shows even top VLAs still ignore language. (2) Language grounding diagnostics: LIBERO-Plus (CVPR 2026, arXiv 2510.13626) reveals VLAs are insensitive to language and exhibit positional bias, with performance dropping from 95% to below 30% under camera/robot state perturbations. LangGap (arXiv 2603.00592, Mar 2026) confirms VLAs ignore language and shows data augmentation's ceiling (28% multi-task). LIBERO-Para (arXiv 2603.28301, Mar 2026) quantifies paraphrase fragility (22–52pp drops). Shin (arXiv 2603.16044, Mar 2026) achieves only +1.71pp via augmentation. Stable Language Guidance / RSS (ACL 2026, arXiv 2601.04052) addresses modality collapse at inference via residual steering — complementary to LACVLA's training-time approach. (3) Modular affordance-then-action pipelines: RT-Affordance (arXiv 2411.02704), UAD (ICRA 2025), RAM (CoRL 2024), RAAP (arXiv 2603.29419, Mar 2026), AffordDP (CVPR 2025), RoboMAP (arXiv 2510.10912), A0 (ICCV 2025, arXiv 2504.12636), and GLOVER++ (CoRL 2025, arXiv 2505.11865) all produce affordance representations but feed them to separate downstream planners/policies, sacrificing end-to-end optimization. A0 achieves zero-shot cross-category transfer via 1M contact points but without language conditioning of the affordance representation. (4) Affordance-aware VLA reasoning and pre-training: CoA-VLA (ICCV 2025) and Sim2Real VLA (ICLR 2026) incorporate affordances via text chains. PokéVLA (arXiv 2604.20834, Apr 2026) pre-trains a VLM on HOVA-500K for affordance understanding, validating ego-centric→VLA transfer, but uses affordance only for backbone pre-training rather than as an explicit consistency objective. (5) Architectural bottleneck enforcement: DIAL (arXiv 2603.29844, Mar 2026) enforces a latent intent bottleneck via inverse dynamics — the action head MUST use predicted latent intent because it resolves the discrepancy between current and predicted states. This inspires LACVLA's affordance-gated bottleneck (stop-gradient on VLM features before action head, affordance map as spatial attention gate). (6) Cross-category zero-shot benchmarks: AGNOSTOS/X-ICM (arXiv 2505.15660) provides 23 unseen manipulation tasks for cross-task evaluation; VLA² (arXiv 2510.14902) uses agentic retrieval for unseen concepts. Gap: No existing work combines (a) architectural enforcement that language must condition spatial features, (b) self-supervised consistency objectives on affordance maps (not raw actions), and (c) cross-category zero-shot transfer as the primary evaluation target.",
  "approach": "We propose LACVLA, an end-to-end VLA that structurally forces language to condition spatial affordance grounding through an affordance-gated bottleneck and self-supervised consistency objectives, enabling zero-shot cross-category manipulation.\n\nArchitecture — Affordance-Gated Bottleneck (inspired by DIAL's latent intent bottleneck): Built on a 4B–7B VLM backbone (Qwen2-VL-4B via StarVLA or PaliGemma2) with LoRA fine-tuning. The architecture has three components:\n(a) Affordance Readout: A cross-attention layer where language instruction tokens attend over intermediate VLM visual features (layer ~16 of 32 for Qwen2-VL), producing a dense affordance heatmap over the image. This encodes WHERE to interact, conditioned on the instruction. Architecture: single cross-attention + LayerNorm + linear projection to H×W heatmap, <5M parameters.\n(b) Stop-Gradient Bottleneck: VLM intermediate visual features are passed through a stop-gradient before reaching the action head. The action head receives: affordance_heatmap ⊙ sg(VLM_visual_features) + proprioceptive_state. The affordance map acts as a spatial attention gate — if the model produces a uniform (language-ignoring) affordance map, the action head receives unselective visual features with no spatial focus, degrading performance. If the map collapses to a degenerate peak, the action head loses context. This structurally forces task-relevant WHERE information through the language-conditioned affordance bottleneck, preventing the bypass problem identified by reviewers. Unlike a soft bottleneck, the stop-gradient ensures no task-semantic gradient flows through the non-affordance pathway — the action head CANNOT learn to extract task information from raw VLM features.\n(c) Flow-Matching Action Head: A lightweight DiT (Diffusion Transformer) that generates trajectory chunks conditioned on the affordance-gated visual features + proprioceptive state, following the flow-matching formulation.\n\nTraining Objectives — Three jointly optimized losses with phased schedule:\n(1) Instruction-Paraphrase Affordance Consistency (IPAC): Given the same visual scene and K LLM-generated paraphrases of the same task instruction (e.g., 'grab the mug handle' vs. 'grasp the cup by its handle'), the affordance maps must be consistent (KL divergence penalty on spatial heatmaps). This transfers the consistency regularization principle from PPCL (EACL 2024) — which showed consistency > augmentation with 10× less data in NLP — to spatial affordance heatmaps. Unlike Shin (2026), who uses paraphrases purely as data augmentation (achieving marginal +1.71pp), IPAC uses them as a regularization signal constraining affordance geometry. Paraphrases generated offline by LLM — free, unlimited supervision.\n(2) Instruction-Discriminative Affordance (IDA): Given the same visual scene and two semantically different instructions (e.g., 'pick up the mug by its handle' vs. 'pour from the mug'), the affordance maps must diverge (margin-based divergence loss). This prevents degenerate consistency collapse where the model produces instruction-invariant heatmaps to trivially satisfy IPAC. Different-instruction pairs come naturally from multi-task robot datasets.\n(3) Action-Grounded Affordance (AGA): Standard flow-matching loss for trajectory prediction through the affordance-gated bottleneck. This grounds the affordance map in manipulation-relevant contact regions via end-to-end backpropagation through the gating mechanism.\n\nPhased Training Schedule:\nPhase 1 — Affordance Readout Pre-training on HOVA-500K: Train the cross-attention readout to predict contact-point Gaussian heatmaps (σ proportional to object scale) conditioned on action-label text prompts from HOVA-500K's 675 action categories. Viewpoint augmentation (random crop, perspective warp, ego→third-person style augmentation) addresses the ego-centric domain gap. Diagnostic checkpoint: evaluate pre-trained affordance readout on robot observation images; if domain gap degrades affordance quality below threshold, bridge with (a) a small set of robot data with pseudo-affordance labels from action-contact heuristics and (b) cross-domain contrastive loss between HOVA-500K and robot VLM features for same-action categories. This addresses the reviewer concern that PokéVLA's backbone pre-training transfer is fundamentally different from affordance readout pre-training — we validate empirically before proceeding.\nPhase 2 — End-to-end VLA training (steps 0–N): Fine-tune full model (VLM via LoRA + pre-trained affordance readout + flow-matching action head) on robot data. Sub-phases: (2a) AGA only for 10% of training — establish action grounding baseline. (2b) Add IPAC at 10% — enforce consistency while action loss stabilizes gradients. (2c) Ramp IDA from 0 to full weight over 15% of training via linear warmup, monitored by: (i) affordance entropy H(A) — if H(A) < 0.3 × H_max, increase IDA weight by 50%; (ii) instruction-discriminability D = mean pairwise KL between different-instruction maps on validation set — if D < 0.5, halt IPAC and boost IDA. GradNorm-style gradient normalization across the three losses balances training rates automatically.\n\nWhy Affordance Maps (Not Raw Actions) for Consistency: Affordance maps capture WHERE to interact — the geometric invariant across paraphrases and across categories sharing functional parts. Action distributions conflate WHERE + HOW + WHEN (trajectory shape, timing, force), making consistency regularization noisier. For cross-category transfer, WHERE is what transfers (handle locations generalize across mugs/cups/pitchers), while HOW adapts to object-specific geometry. This argument is validated empirically by ablation #6.\n\nCross-Object Functional Consistency via HOVA-500K: Group HOVA-500K images by shared action labels (675 categories) and apply soft KL penalty between affordance maps of same-action images from different object categories. This provides weak supervision for cross-category affordance consistency without requiring part-level functional equivalence annotations.\n\nData Pipeline: Open X-Embodiment and DROID for robot trajectories, HOVA-500K for affordance pre-training and cross-object grouping, LLM-generated instruction paraphrases (Qwen3 or GPT-4) for IPAC pairs.\n\nAblation Design (8 variants, addressing all reviewer concerns):\n(1) Full LACVLA — affordance-gated bottleneck + IPAC + IDA + AGA\n(2) No affordance bottleneck — direct VLA, no affordance readout (tests whether bottleneck is necessary)\n(3) Modular composition — frozen GLOVER++ affordance → separate policy (tests end-to-end vs. modular)\n(4) No consistency losses — only AGA through affordance bottleneck (tests whether architectural bottleneck alone suffices without consistency enforcement)\n(5) Shin-style augmentation — paraphrases added as training data, no consistency loss (tests data augmentation ceiling, paralleling PPCL's NLP finding)\n(6) IPAC on raw actions — KL divergence between action distributions under paraphrased instructions, no affordance readout (CRITICAL: tests whether isolating WHERE via affordance maps outperforms consistency on conflated action distributions — if affordance maps win, that's the paper's key finding; if raw actions work comparably, the affordance readout is unnecessary overhead)\n(7) ST4VLA-style spatial grounding + IPAC on features — spatial grounding pre-training + consistency on intermediate VLM features without affordance readout (tests whether explicit affordance structure adds value beyond strong spatial pre-training + consistency, addressing the 'why not just do spatial grounding?' question)\n(8) No phased training — all losses from step 0 (tests curriculum importance)\n\nEvaluation Protocol — Primary (Cross-Category Zero-Shot Transfer):\n(a) Held-out object category experiments: partition LIBERO/DROID object categories into train/test sets, test on entirely unseen categories with both standard and paraphrased instructions\n(b) HOVA-500K cross-category transfer tests: train on K action categories with one set of objects (e.g., 'pour from pitcher'), test on same actions with different object categories (e.g., 'pour from kettle') — constructed from HOVA-500K's 675 shared action labels\n(c) AGNOSTOS benchmark (arXiv 2505.15660) for cross-task zero-shot evaluation (23 unseen tasks)\n(d) Real-world evaluation on 5+ unseen object categories across at least 3 manipulation primitives (grasp, pour, push)\n\nEvaluation Protocol — Secondary:\n(e) LIBERO-Para benchmark with PRIDE metric for paraphrase robustness (direct comparison with ST4VLA's 72%/61%)\n(f) LangGap protocol for language grounding quality (targeting improvement over the 28% multi-task ceiling)\n(g) Affogato for affordance quality assessment\n(h) Standard LIBERO (Spatial, Object, Goal, Long) for in-distribution comparison with ST4VLA (95.9% avg)\n\nCoRL 2026 Infeasibility Statement: The user's original objective was CoRL 2026 submission (abstract May 26, 2026 — 8 days from today, May 18). This is clearly infeasible given the implementation scope: three-loss system with phased training, affordance-gated bottleneck, HOVA-500K pre-training pipeline, 8 ablation variants, and multi-benchmark evaluation. We target AAAI 2027 (abstract Jul 21 — 64 days) as primary, WACV 2027 Round 2 (paper Aug 27 — 101 days) as backup.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~250-350h A100 80GB, equivalent to ~170-235h H100 (HOVA-500K affordance readout pre-training ~25h, 3-4 full VLA training runs at ~35-50h each with LoRA on 4B backbone, 8 ablation experiments at ~15-20h each, cross-category evaluation sweeps ~30h, AGNOSTOS benchmark runs ~15h)",
      "gpu_utilization": "~15-25% effective utilization — idle during result analysis, loss weight iteration, domain gap diagnostics between phases",
      "timeline": "8-12 weeks (2-3 weeks data pipeline + HOVA-500K pre-training with viewpoint augmentation + domain gap diagnostics; 4-6 weeks iterative experimentation including all 8 ablations; 2-3 weeks cross-category evaluation + paper writing)",
      "team": "2 researchers (1 lead on affordance-gated architecture + consistency objectives + bottleneck enforcement, 1 on data pipeline/HOVA-500K integration/cross-category evaluation/AGNOSTOS setup)",
      "estimated_gpu_cost": "$375-525 (at ~$1.50/h A100 80GB on RunPod/Jarvislabs)"
    },
    "human_in_loop": {
      "gpu_hours": "~320-450h A100 80GB, equivalent to ~215-300h H100 (agent runs 10-14 training configurations systematically, all 8 ablations + 2-4 additional hyperparameter variants, HOVA-500K pre-training, with wasted runs caught early by human)",
      "gpu_utilization": "~40-55% — agent queues experiments but pauses at key gates: (1) HOVA-500K domain gap diagnostic before Stage 2, (2) affordance map quality inspection after bottleneck warmup, (3) cross-category held-out split design approval",
      "timeline": "6-9 weeks (agent handles paraphrase generation, HOVA-500K preprocessing with viewpoint augmentation, hyperparameter sweeps, AGNOSTOS/LIBERO-Para/LangGap evaluation scripts; human approves domain gap bridging strategy, inspects affordance maps, validates cross-category split design)",
      "team": "1 researcher, ~1.5h/day review",
      "claude_api_cost": "$200-500 (estimated 2,000-5,000 agent turns)",
      "estimated_gpu_cost": "$480-675 (at ~$1.50/h A100 80GB)",
      "risk_note": "Primary risk: HOVA-500K affordance readout pre-training domain gap — mitigated by viewpoint augmentation and diagnostic checkpoint before Stage 2. Secondary risk: affordance-gated bottleneck may be too restrictive, causing performance collapse — mitigated by ablation #4 (bottleneck without consistency) to isolate the effect. ST4VLA comparison (ablation #7) will determine if the approach adds value beyond spatial grounding."
    },
    "auto_research": {
      "gpu_hours": "~650-1000h A100 80GB, equivalent to ~435-670h H100 (agent explores 18-28 training configurations for phased schedule tuning, all 8 ablation variants × 2-3 seeds, HOVA-500K pre-training with multiple viewpoint augmentation strategies, full benchmark sweeps)",
      "gpu_utilization": "~85-95% — agent immediately queues next experiment upon completion; parallel ablation runs on multi-GPU setup",
      "timeline": "3-4 weeks with 4+ A100 GPUs available concurrently (bottleneck: HOVA-500K pre-training → domain gap diagnostic → phased training search → cross-category evaluation)",
      "team": "0 researchers after initial setup (~6-8 hours: dataset access, paraphrase generation config, HOVA-500K preprocessing, AGNOSTOS/LIBERO-Para/LangGap environment setup, cross-category held-out split definition)",
      "claude_api_cost": "$500-1,200 (estimated 5,000-12,000 agent turns)",
      "estimated_gpu_cost": "$975-1,500 (at ~$1.50/h A100 80GB)",
      "speed_bottleneck": "Each LoRA training run on 4B backbone takes ~8-12h on 4 A100s. HOVA-500K preprocessing and viewpoint-augmented Gaussian heatmap generation ~30h one-time. Cross-category evaluation setup ~6h one-time.",
      "risk_note": "Automated phased training managed by entropy/discriminability monitoring. If affordance-gated bottleneck causes consistent performance collapse across configurations, agent escalates to soft-gating variants (gradually opening the bottleneck). GradNorm balancing reduces sensitivity to manual loss weight tuning."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target, 64 days to abstract; strong fit for self-supervised consistency + architectural bottleneck contribution with robotics application)",
    "WACV 2027 Round 2 (registration Aug 20, paper Aug 27, 2026 — realistic backup, 101 days; vision+robotics focus)",
    "ICLR 2027 (abstract ~Sep 2026, full paper ~Sep 2026 — dates TBD, estimated from ICLR 2026 cycle; top-tier target if cross-category zero-shot results are strong)",
    "CVPR 2027 (registration ~Nov 2026, paper ~Nov 2026 — dates TBD; if affordance visualization and cross-category transfer results are visually compelling)",
    "NOTE: CoRL 2026 (abstract May 26, paper May 29) was the user's original target but is infeasible — 8 days is insufficient for implementation of affordance-gated bottleneck, 8 ablations, HOVA-500K pipeline, and multi-benchmark evaluation"
  ],
  "level": "solid",
  "key_references": [
    "ST4VLA: Spatially Guided Training for Vision-Language-Action Models (ICLR 2026, arXiv 2602.10109) — strongest baseline: 95.9% LIBERO avg, 72%/61% paraphrase robustness, 62% unseen objects via spatial grounding alone",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626) — diagnostic revealing VLAs ignore language instructions, exhibit positional bias",
    "LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models (arXiv 2603.00592, Mar 2026) — quantifies language gap: augmentation reaches 90% single-task but only 28% multi-task",
    "DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA (arXiv 2603.29844, Mar 2026) — latent intent bottleneck via inverse dynamics, inspiration for affordance-gated architecture",
    "InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy (arXiv 2510.13778) — spatially guided VLA with affordance recognition in pre-training",
    "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models (RSS 2025, arXiv 2501.15830) — spatial-aware action tokenization",
    "Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model (ICLR 2026, arXiv 2510.12276) — implicit spatial alignment without 3D input, single-branch inspiration",
    "AGNOSTOS / X-ICM: Exploring the Limits of Vision-Language-Action Manipulations in Cross-task Generalization (arXiv 2505.15660) — cross-task zero-shot benchmark with 23 unseen tasks",
    "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models (arXiv 2603.28301, Mar 2026) — paraphrase robustness evaluation with PRIDE metric",
    "Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation (Shin, arXiv 2603.16044, Mar 2026) — direct augmentation baseline, +1.71pp only",
    "Stable Language Guidance / Residual Semantic Steering for VLAs (ACL 2026, arXiv 2601.04052) — inference-time modality collapse mitigation, complementary to LACVLA's training-time approach",
    "Prompt Perturbation Consistency Learning for Robust Language Models (PPCL, EACL 2024, arXiv 2402.15833) — consistency regularization > augmentation with 10× fewer samples in NLP",
    "Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs (arXiv 2510.14242, Oct 2025) — extends PPCL to LLMs",
    "OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024) — base VLA architecture",
    "StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing (arXiv 2604.05014, Apr 2026) — implementation framework",
    "GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation (CoRL 2025, arXiv 2505.11865) — provides HOVA-500K dataset, modular baseline",
    "PokéVLA: Empowering Pocket-Sized VLA Model with Comprehensive World Knowledge Guidance (arXiv 2604.20834, Apr 2026) — validates HOVA-500K ego→VLA transfer for backbone pre-training",
    "RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (arXiv 2411.02704, 2024) — modular affordance baseline",
    "A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation (ICCV 2025, arXiv 2504.12636) — hierarchical affordance with zero-shot transfer but no language conditioning",
    "RoboMAP: Adaptive Affordance Heatmaps via PaliGemma (arXiv 2510.10912, 2025) — modular language-conditioned heatmap architecture reference",
    "AffordDP: Generalizable Diffusion Policy with Transferable Affordance (CVPR 2025) — cross-category transfer via 3D contact points",
    "RAM: Retrieval-Based Affordance Transfer for Generalizable Zero-Shot Robotic Manipulation (CoRL 2024, arXiv 2407.04689) — retrieval-based affordance baseline",
    "RAAP: Retrieval-Augmented Affordance Prediction with Cross-Image Action Alignment (arXiv 2603.29419, Mar 2026) — cross-image affordance alignment",
    "Affogato: Learning Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale (arXiv 2506.12009, 2025) — affordance quality benchmark",
    "AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation (arXiv 2604.11674, 2026) — simulation evaluation resource",
    "GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks (ICML 2018) — multi-task loss balancing",
    "GeoVLA: Empowering 3D Representations in Vision-Language-Action Models (arXiv 2508.09071, Aug 2025) — 3D VLA baseline requiring depth sensor",
    "RS-CL: Contrastive Representation Regularization for VLAs (arXiv 2510.01711, 2025) — contrastive VLA regularization on proprioceptive states only"
  ],
  "description": "LACVLA addresses the critical finding that VLAs largely ignore language instructions (LIBERO-Plus, CVPR 2026; LangGap, Mar 2026) — a failure mode survivable in-distribution but catastrophic for cross-category zero-shot transfer where novel objects lack visual priors. We propose an affordance-gated architectural bottleneck, inspired by DIAL's latent intent bottleneck, that structurally forces all task-relevant spatial information through a language-conditioned affordance map: VLM intermediate features pass through stop-gradient before the action head, which receives affordance_heatmap ⊙ sg(visual_features) + proprioceptive_state. The affordance map (produced via cross-attention between VLM features and language tokens) acts as a spatial attention gate — a uniform (language-ignoring) map yields unselective features and degraded performance, preventing the bypass problem. Self-supervised consistency objectives enforce language-affordance grounding: IPAC ensures semantically equivalent instructions produce identical affordance maps (transferring PPCL's consistency > augmentation principle from NLP to spatial heatmaps), while IDA ensures semantically different instructions produce divergent maps (preventing consistency collapse). A comprehensive 8-variant ablation suite addresses all key questions: (1) Does the architectural bottleneck help? (ablation #2: no bottleneck), (2) Does consistency outperform augmentation? (ablation #5: Shin-style augmentation), (3) Are affordance maps the right target? (ablation #6: IPAC on raw action distributions — the paper's critical test: if affordance maps outperform action-level consistency, it validates that isolating WHERE-to-interact from HOW-to-interact is essential), (4) Does affordance consistency add value beyond spatial grounding? (ablation #7: ST4VLA-style + IPAC on features). Evaluation is rebalanced toward the user's original objective: PRIMARY metrics target cross-category zero-shot transfer (held-out object categories, HOVA-500K cross-category splits across 675 action labels, AGNOSTOS benchmark, real-world evaluation on 5+ unseen categories), with SECONDARY metrics on paraphrase robustness (LIBERO-Para, LangGap) and affordance quality (Affogato). HOVA-500K domain gap is addressed via viewpoint augmentation and a diagnostic checkpoint before end-to-end training, with cross-domain contrastive bridging if needed. CoRL 2026 (abstract May 26 — 8 days away) is acknowledged as infeasible; the primary target is AAAI 2027 (abstract Jul 21, 64 days) with WACV 2027 Round 2 (Aug 27) as backup.",
  "project_name": "lac_vla_zero_shot",
  "source": "web_research"
}

## Reviewer feedback (round 5)
Issues: ["MISSING COMPETING WORK — GuidedVLA (RSS 2026, arXiv 2605.12369, May 12, 2026): Supervises individual action decoder attention heads with auxiliary signals for object grounding, spatial geometry, and temporal skill logic. Achieves improved in-domain and out-of-domain success rates. Conceptually adjacent to LACVLA's affordance readout supervision — both use explicit auxiliary supervision on intermediate representations to improve VLA grounding. Differentiation needed: GuidedVLA uses 3 predefined factor types (not open-vocabulary), doesn't use consistency objectives on heatmaps, doesn't target cross-category transfer. But the architectural parallel (supervised intermediate representations) must be discussed.", "MISSING BENCHMARK — BusyBox (arXiv 2602.05441, Feb 2026, Microsoft): Physical benchmark for VLA affordance generalization showing even strong VLAs (π₀.₅, GR00T-N1.6) struggle with affordance generalization across object variants. Directly relevant to LACVLA's cross-category transfer claims and could serve as additional evaluation.", "COMPUTE BUDGET BORDERLINE: Manual estimate of 250-350h A100 converts to 170-235h H100, but the user's hard constraint is ≤200 H100-hours. The upper range (235h H100) exceeds the constraint by 17.5%. The A100→H100 ratio of 1.5x is optimistic for mixed-precision transformer fine-tuning (1.3x is more conservative for some workloads, which would push 350h A100 to 269h H100). The 8 ablation variants are the main cost driver — consider which can be dropped or combined.", "ENTIRE PAPER'S VALUE DEPENDS ON ABLATION #6: The core claim — affordance maps are the right target for consistency regularization because they isolate WHERE-to-interact — is theoretically motivated but empirically unvalidated. If IPAC on raw action distributions (ablation #6) performs comparably to IPAC on affordance maps, the entire affordance readout + HOVA-500K pipeline becomes unnecessary overhead. This is acknowledged as a 'critical test' but represents significant experimental risk for a paper whose contribution rests on this finding.", "HOVA-500K DOMAIN GAP RISK REMAINS: PokéVLA validates HOVA-500K for backbone pre-training (learning general visual representations), but LACVLA uses it for affordance readout pre-training (producing pixel-level contact-point Gaussian heatmaps). The proposal includes viewpoint augmentation + diagnostic checkpoint + cross-domain contrastive bridging, but these add complexity and compute. If domain gap degrades affordance quality, Phase 2 training may learn to bypass the degraded affordance readout despite the stop-gradient bottleneck — producing low-entropy, uninformative heatmaps that satisfy IPAC trivially."]
Feedback: The proposal has improved dramatically across five rounds and is now technically comprehensive with strong related work coverage. The gap is narrower than before. Specific revisions to push toward passing:

1. **Add GuidedVLA (RSS 2026) to landscape.** arXiv 2605.12369, accepted to RSS 2026, supervises attention heads for object grounding + spatial geometry + temporal skill logic. Differentiate: GuidedVLA uses 3 predefined factor types, no consistency objectives, no affordance heatmaps, no cross-category transfer focus. LACVLA's affordance readout with stop-gradient bottleneck + open-vocabulary consistency is distinct but the architectural parallel must be acknowledged.

2. **Trim ablation suite to fit compute budget.** 8 ablations at 15-20h each = 120-160h A100, which is 48-64% of total compute. Consider: (a) merge ablations #2 and #4 (no bottleneck vs. bottleneck without consistency — #2 subsumes #4 if you track affordance map quality for both), (b) drop ablation #8 (phased vs. non-phased training) — this is nice-to-have but not essential for the core argument. Target 6 ablations to bring compute to 180-280h A100 ≈ 120-190h H100, safely within ≤200h H100.

3. **Add BusyBox as supplementary benchmark.** arXiv 2602.05441 is a physical benchmark specifically designed for VLA affordance generalization, showing even strong VLAs fail. If LACVLA performs better on BusyBox variants, that's powerful evidence for cross-category affordance transfer.

4. **Strengthen the HOVA-500K fallback plan.** If domain gap diagnostic shows degraded affordance quality on robot observations: (a) fall back to self-supervised affordance readout initialization using robot data alone (action-contact heuristic labels from gripper position at grasp/contact time), (b) ablate HOVA-500K pre-training vs. self-supervised initialization to determine if HOVA-500K is actually necessary. This de-risks the paper from the HOVA-500K dependency.

5. **Frame the narrative more aggressively around cross-category transfer.** The abstract/description still opens with 'VLAs ignore language' — a crowded framing shared by 8+ concurrent papers. Instead, open with: 'We address cross-category zero-shot manipulation transfer, where VLAs must generalize to objects with no visual precedent. We show that the well-documented language-ignoring failure (LIBERO-Plus, LangGap) is particularly catastrophic in this setting because language is the only available guide for spatial grounding on novel objects. Our approach: structurally force language to condition spatial affordance features via an architectural bottleneck, then enforce consistency to ensure the grounding is robust.' This positions LACVLA in a less crowded space (cross-category transfer) rather than the crowded one (fixing language bypass).

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
这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 3.5 到 3.8，没有明显改善。

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
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "449da185-c88c-4ca7-a34e-971e14362455",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T20:32:20.620Z_

```json
{
  "parentUuid": "449da185-c88c-4ca7-a34e-971e14362455",
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
  "uuid": "a36142f7-1278-42e8-98be-2114a7a2a7c6",
  "timestamp": "2026-05-18T20:32:20.620Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T20:32:20.620Z_

```json
{
  "parentUuid": "a36142f7-1278-42e8-98be-2114a7a2a7c6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "75195a10-6574-49ae-a5ac-cf209f427353",
  "timestamp": "2026-05-18T20:32:20.620Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-18 (UTC).**  ## Original idea {   \"title\": \"LACVLA: Enforcing Language-Affordance Grounding via Consistency Object…",
  "leafUuid": "75195a10-6574-49ae-a5ac-cf209f427353",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise LACVLA affordance consistency for cross-category transfer",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Assistant

_source line 8 · 2026-05-18T20:32:36.424Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the reviewer feedback and think deeply about whether this idea needs minor fixes, major revision, or a pivot.

The reviewer feedback in round 5 has 5 specific issues:
1. Missing GuidedVLA (RSS 2026) - need to add to landscape
2. Missing BusyBox benchmark - need to add as evaluation
3. Compute budget exceeds ≤200 H100-hours constraint
4. Core paper value depends on ablation #6 (risky)
5. HOVA-500K domain gap risk remains

The reviewer also gives 5 specific revision suggestions:


1. Add GuidedVLA to landscape
2. Trim ablation suite (merge #2/#4, drop #8) to 6 ablations
3. Add BusyBox as supplementary benchmark
4. Strengthen HOVA-500K fallback plan
5. Reframe narrative around cross-category transfer (not "VLAs ignore language")

The stagnation warning notes scores from 3.5 to 3.8 over 3 rounds, so I need to assess whether these targeted fixes will move the needle or if the core idea needs rethinking. The fundamental contribution—forcing VLAs to use language through an affordance-gated bottleneck with consistency objectives—is sound, but the execution and framing need tightening to address the reviewer's concerns about risky dependencies and missing baselines.

Looking at the feedback more carefully, the reviewer isn't questioning the approach itself but flagging specific gaps: GuidedVLA and BusyBox aren't in the related work, the compute budget is tight without a solid HOVA-500K backup, the framing feels crowded, and ablation #6 is a critical dependency. The reviewer also notes we've improved substantially across rounds and are now "technically comprehensive with strong related work coverage"—that's a signal we're close. I think executing these five concrete changes cleanly could push this through without needing a fundamental pivot.

Before I commit to the revision strategy, I need to do the groundwork: read GuidedVLA and BusyBox to understand how they fit into the landscape, figure out where the compute savings can come from, design a fallback strategy for HOVA-500K, and think through how to reframe the opening around cross-category transfer without losing clarity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75195a10-6574-49ae-a5ac-cf209f427353",
  "isSidechain": false,
  "requestId": "req_011CbAfr64fmtmpBfdN73rXe",
  "type": "assistant",
  "uuid": "fa40802d-7683-40c7-a87c-0cbdb194e33c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVvm4wVxfCS62WYwYAUHeR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15847,
      "cache_read_input_tokens": 11841,
      "output_tokens": 765,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 765,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15847
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-18T20:32:36.427Z_

I'll research the papers and issues flagged by the reviewer before making any revisions. Let me start by looking up the two missing works and verifying the current landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa40802d-7683-40c7-a87c-0cbdb194e33c",
  "isSidechain": false,
  "requestId": "req_011CbAfr64fmtmpBfdN73rXe",
  "type": "assistant",
  "uuid": "f3d9b387-d4cf-4243-9b11-e3cbad636018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVvm4wVxfCS62WYwYAUHeR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15847,
      "cache_read_input_tokens": 11841,
      "output_tokens": 765,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 765,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15847
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T20:32:36.583Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FwVrHoetC6MtfSRm3NSA72`</summary>

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
  "parentUuid": "f3d9b387-d4cf-4243-9b11-e3cbad636018",
  "isSidechain": false,
  "requestId": "req_011CbAfr64fmtmpBfdN73rXe",
  "type": "assistant",
  "uuid": "baa5ac9c-e533-4f60-b544-ec5b740ca588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVvm4wVxfCS62WYwYAUHeR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15847,
      "cache_read_input_tokens": 11841,
      "output_tokens": 765,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 765,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15847
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T20:32:36.589Z_

<details><summary>↩ Tool result · `toolu_01FwVrHoetC6MtfSRm3NSA72`</summary>

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
  "parentUuid": "baa5ac9c-e533-4f60-b544-ec5b740ca588",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "355061c2-c798-45fe-ab3d-86e27cae61a0",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "baa5ac9c-e533-4f60-b544-ec5b740ca588",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-18T20:32:39.308Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now search for the two missing papers and do broader research on the landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "355061c2-c798-45fe-ab3d-86e27cae61a0",
  "isSidechain": false,
  "requestId": "req_011CbAfsGJbexKJqqFs4AGh3",
  "type": "assistant",
  "uuid": "37674282-d7aa-4fa6-bb99-f372ba78f848",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPAzrenNcwjiRX3MgRChKf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1784,
      "cache_read_input_tokens": 27688,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 27688,
          "cache_creation_input_tokens": 1784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1784
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-18T20:32:39.949Z_

Let me research the flagged papers and broader landscape in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37674282-d7aa-4fa6-bb99-f372ba78f848",
  "isSidechain": false,
  "requestId": "req_011CbAfsGJbexKJqqFs4AGh3",
  "type": "assistant",
  "uuid": "9802fe28-4494-466c-9ccc-4b88e9485fb6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPAzrenNcwjiRX3MgRChKf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1784,
      "cache_read_input_tokens": 27688,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 27688,
          "cache_creation_input_tokens": 1784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1784
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T20:32:40.397Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KVspUbfj9usuj5k6Fyew4G`</summary>

```json
{
  "query": "GuidedVLA arXiv 2605.12369 RSS 2026 attention head supervision VLA grounding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9802fe28-4494-466c-9ccc-4b88e9485fb6",
  "isSidechain": false,
  "requestId": "req_011CbAfsGJbexKJqqFs4AGh3",
  "type": "assistant",
  "uuid": "662fbe8d-f72d-40ab-a17b-d7e06cf23994",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPAzrenNcwjiRX3MgRChKf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1784,
      "cache_read_input_tokens": 27688,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1784,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 125,
          "cache_read_input_tokens": 27688,
          "cache_creation_input_tokens": 1784,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1784
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T20:32:45.906Z_

<details><summary>↩ Tool result · `toolu_01KVspUbfj9usuj5k6Fyew4G`</summary>

```text
Web search results for query: "GuidedVLA arXiv 2605.12369 RSS 2026 attention head supervision VLA grounding"

Links: [{"title":"[2605.12369v1] GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization","url":"https://arxiv.org/abs/2605.12369v1"},{"title":"GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization","url":"https://arxiv.org/html/2605.12369v1"},{"title":"Guiding Attention for Self-Supervised Learning with Transformers","url":"https://arxiv.org/pdf/2010.02399"},{"title":"Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models","url":"https://arxiv.org/pdf/2511.21663"},{"title":"Fine-Grained Perturbation Guidance via Attention Head Selection","url":"https://arxiv.org/html/2506.10978v3"}]

Based on the search results, I found the paper you're looking for:

**GuidedVLA** is a framework designed to manually guide the action generation to focus on task-relevant factors. Individual attention heads are supervised by manually defined auxiliary signals to capture distinct factors, instantiated with three specialized heads: object grounding, spatial geometry, and temporal skill logic.

Vision-Language-Action (VLA) models aim for general robot learning by aligning action as a modality within powerful Vision-Language Models. Existing VLAs rely on end-to-end supervision to implicitly enable the action decoding process to learn task-relevant features, but without explicit guidance, these models often overfit to spurious correlations, such as visual shortcuts or environmental noise, limiting their generalization.

The paper (arXiv:2605.12369v1) was submitted on May 12, 2026 and includes contributions from researchers at institutions including Fudan University, Shanghai Jiao Tong University, and the University of Hong Kong.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "662fbe8d-f72d-40ab-a17b-d7e06cf23994",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "ed6c00a0-8ecb-4151-a5a9-33da5e6292db",
  "toolUseResult": {
    "query": "GuidedVLA arXiv 2605.12369 RSS 2026 attention head supervision VLA grounding",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y9o6vx5X7pWRTqccSus29r",
        "content": [
          {
            "title": "[2605.12369v1] GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization",
            "url": "https://arxiv.org/abs/2605.12369v1"
          },
          {
            "title": "GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization",
            "url": "https://arxiv.org/html/2605.12369v1"
          },
          {
            "title": "Guiding Attention for Self-Supervised Learning with Transformers",
            "url": "https://arxiv.org/pdf/2010.02399"
          },
          {
            "title": "Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2511.21663"
          },
          {
            "title": "Fine-Grained Perturbation Guidance via Attention Head Selection",
            "url": "https://arxiv.org/html/2506.10978v3"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**GuidedVLA** is a framework designed to manually guide the action generation to focus on task-relevant factors. Individual attention heads are supervised by manually defined auxiliary signals to capture distinct factors, instantiated with three specialized heads: object grounding, spatial geometry, and temporal skill logic.\n\nVision-Language-Action (VLA) models aim for general robot learning by aligning action as a modality within powerful Vision-Language Models. Existing VLAs rely on end-to-end supervision to implicitly enable the action decoding process to learn task-relevant features, but without explicit guidance, these models often overfit to spurious correlations, such as visual shortcuts or environmental noise, limiting their generalization.\n\nThe paper (arXiv:2605.12369v1) was submitted on May 12, 2026 and includes contributions from researchers at institutions including Fudan University, Shanghai Jiao Tong University, and the University of Hong Kong."
    ],
    "durationSeconds": 5.503566051999998
  },
  "sourceToolAssistantUUID": "662fbe8d-f72d-40ab-a17b-d7e06cf23994",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T20:32:49.072Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FYdmGsur67AVwmAycDxDok`</summary>

```json
{
  "query": "BusyBox arXiv 2602.05441 VLA affordance generalization benchmark physical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed6c00a0-8ecb-4151-a5a9-33da5e6292db",
  "isSidechain": false,
  "requestId": "req_011CbAfsxSLRzk5HeAvr1ShR",
  "type": "assistant",
  "uuid": "622e708f-3076-41da-8428-e77c6c837faa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CsnXUHW1yNnnZEsRdKMFFR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 29472,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 29472,
          "cache_creation_input_tokens": 652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 652
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T20:32:57.032Z_

<details><summary>↩ Tool result · `toolu_01FYdmGsur67AVwmAycDxDok`</summary>

```text
Web search results for query: "BusyBox arXiv 2602.05441 VLA affordance generalization benchmark physical"

Links: [{"title":"[2602.05441] Benchmarking Affordance Generalization with BusyBox","url":"https://arxiv.org/abs/2602.05441"},{"title":"Benchmarking Affordance Generalization with BusyBox","url":"https://arxiv.org/pdf/2602.05441"},{"title":"Benchmarking Affordance Generalization with BusyBox","url":"https://arxiv.org/html/2602.05441"},{"title":"Benchmarking Affordance Generalization with BusyBox","url":"https://microsoft.github.io/BusyBox/"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=2693&show=1000"},{"title":"Benchmarking Affordance Generalization with BusyBox - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/benchmarking-affordance-generalization-with-busybox/"}]

Based on the search results, here's what I found about BusyBox (arXiv 2602.05441):

## Overview

BusyBox is a physical benchmark for systematic semi-automatic evaluation of VLAs' affordance generalization, consisting of 6 modules with switches, sliders, wires, buttons, a display, and a dial.

## Key Features

The modules can be swapped and rotated to create a multitude of BusyBox variations with different visual appearances but the same set of affordances. Affordance generalization is defined as the ability to manipulate new objects with familiar physical features.

## Research Findings

Empirical results demonstrate that generalization across BusyBox variants is highly challenging even for strong open-weights VLAs such as π₀.₅ and GR00T-N1.6.

## Open-Source Release

The benchmark was designed to be easy to build in most robotics labs, with full CAD files for 3D-printing parts and a bill of materials released. A dataset of language-annotated demonstrations collected using a Mobile Aloha robot was also published.

The paper was submitted to arXiv on February 5, 2026, and represents a contribution to evaluating how well Vision-Language-Action (VLA) models can generalize across different physical configurations of the same affordances.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "622e708f-3076-41da-8428-e77c6c837faa",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "659bc4cd-f7a7-49b7-b9a9-2f70079b9230",
  "toolUseResult": {
    "query": "BusyBox arXiv 2602.05441 VLA affordance generalization benchmark physical",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WofqqF2G6KLWNo42BN2oHr",
        "content": [
          {
            "title": "[2602.05441] Benchmarking Affordance Generalization with BusyBox",
            "url": "https://arxiv.org/abs/2602.05441"
          },
          {
            "title": "Benchmarking Affordance Generalization with BusyBox",
            "url": "https://arxiv.org/pdf/2602.05441"
          },
          {
            "title": "Benchmarking Affordance Generalization with BusyBox",
            "url": "https://arxiv.org/html/2602.05441"
          },
          {
            "title": "Benchmarking Affordance Generalization with BusyBox",
            "url": "https://microsoft.github.io/BusyBox/"
          },
          {
            "title": "Computer Science",
            "url": "https://www.arxiv.org/list/cs/recent?skip=2693&show=1000"
          },
          {
            "title": "Benchmarking Affordance Generalization with BusyBox - Microsoft Research",
            "url": "https://www.microsoft.com/en-us/research/publication/benchmarking-affordance-generalization-with-busybox/"
          }
        ]
      },
      "Based on the search results, here's what I found about BusyBox (arXiv 2602.05441):\n\n## Overview\n\nBusyBox is a physical benchmark for systematic semi-automatic evaluation of VLAs' affordance generalization, consisting of 6 modules with switches, sliders, wires, buttons, a display, and a dial.\n\n## Key Features\n\nThe modules can be swapped and rotated to create a multitude of BusyBox variations with different visual appearances but the same set of affordances. Affordance generalization is defined as the ability to manipulate new objects with familiar physical features.\n\n## Research Findings\n\nEmpirical results demonstrate that generalization across BusyBox variants is highly challenging even for strong open-weights VLAs such as π₀.₅ and GR00T-N1.6.\n\n## Open-Source Release\n\nThe benchmark was designed to be easy to build in most robotics labs, with full CAD files for 3D-printing parts and a bill of materials released. A dataset of language-annotated demonstrations collected using a Mobile Aloha robot was also published.\n\nThe paper was submitted to arXiv on February 5, 2026, and represents a contribution to evaluating how well Vision-Language-Action (VLA) models can generalize across different physical configurations of the same affordances."
    ],
    "durationSeconds": 7.955349860000002
  },
  "sourceToolAssistantUUID": "622e708f-3076-41da-8428-e77c6c837faa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T20:33:01.163Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DL8mkQ5S765phNYaEj46Jo`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.12369v1",
  "prompt": "Extract the full abstract, key method details, main results/numbers, and what benchmarks they evaluate on. Also note which VLA backbone they build on, and whether they do any cross-category or zero-shot transfer evaluation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "659bc4cd-f7a7-49b7-b9a9-2f70079b9230",
  "isSidechain": false,
  "requestId": "req_011CbAftmUoUVXGS9Jc81bcc",
  "type": "assistant",
  "uuid": "24845f7f-8dad-4e8f-b61b-4be4ded92089",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrfCMDBhzmLxyeffqWndGc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 30124,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 682,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 30124,
          "cache_creation_input_tokens": 682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 682
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T20:33:06.214Z_

<details><summary>↩ Tool result · `toolu_01DL8mkQ5S765phNYaEj46Jo`</summary>

```text
# GuidedVLA Paper Summary

## Abstract
The authors introduce a framework that explicitly guides Vision-Language-Action models to focus on task-relevant factors. Rather than relying solely on end-to-end supervision, they decompose the action decoder into specialized attention heads supervised by auxiliary signals for distinct factors: object grounding, spatial geometry, and temporal skill logic.

## Key Method Details
The core approach treats "the action decoder not as a monolithic learner, but as an assembly of functional components." Individual attention heads receive manual supervision to capture specific task-relevant aspects, enabling the model to avoid spurious correlations and environmental noise.

## Main Results
GuidedVLA "improves success rates in both in-domain and out-of-domain settings" compared to strong VLA baselines across simulation and real-robot experiments. The authors demonstrate that specialized factor quality correlates positively with task performance and produces decoupled, high-quality features.

## Limitations in Provided Content
The document does not specify:
- The specific VLA backbone architecture used
- Quantitative success rate numbers or benchmark scores
- Whether cross-category or zero-shot transfer evaluations were conducted
- Names of specific benchmarks tested

The paper is accepted to RSS 2026 with a project page available, but detailed numerical results and baseline comparisons aren't included in this excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24845f7f-8dad-4e8f-b61b-4be4ded92089",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "ab2c1e79-9fd2-47f7-94e6-a303475dc323",
  "toolUseResult": {
    "bytes": 49451,
    "code": 200,
    "codeText": "OK",
    "result": "# GuidedVLA Paper Summary\n\n## Abstract\nThe authors introduce a framework that explicitly guides Vision-Language-Action models to focus on task-relevant factors. Rather than relying solely on end-to-end supervision, they decompose the action decoder into specialized attention heads supervised by auxiliary signals for distinct factors: object grounding, spatial geometry, and temporal skill logic.\n\n## Key Method Details\nThe core approach treats \"the action decoder not as a monolithic learner, but as an assembly of functional components.\" Individual attention heads receive manual supervision to capture specific task-relevant aspects, enabling the model to avoid spurious correlations and environmental noise.\n\n## Main Results\nGuidedVLA \"improves success rates in both in-domain and out-of-domain settings\" compared to strong VLA baselines across simulation and real-robot experiments. The authors demonstrate that specialized factor quality correlates positively with task performance and produces decoupled, high-quality features.\n\n## Limitations in Provided Content\nThe document does not specify:\n- The specific VLA backbone architecture used\n- Quantitative success rate numbers or benchmark scores\n- Whether cross-category or zero-shot transfer evaluations were conducted\n- Names of specific benchmarks tested\n\nThe paper is accepted to RSS 2026 with a project page available, but detailed numerical results and baseline comparisons aren't included in this excerpt.",
    "durationMs": 5046,
    "url": "https://arxiv.org/abs/2605.12369v1"
  },
  "sourceToolAssistantUUID": "24845f7f-8dad-4e8f-b61b-4be4ded92089",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T20:33:11.092Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0151WTfusoq8g7dVq3BRwySE`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.12369v1",
  "prompt": "Extract: 1) The full abstract, 2) What VLA backbone they build on, 3) The three factor types and how they supervise each attention head, 4) Key quantitative results (success rates, benchmarks used), 5) Whether they evaluate cross-category or zero-shot transfer, 6) Whether they use consistency objectives or contrastive losses, 7) How they handle novel/unseen objects. Be as specific as possible with numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab2c1e79-9fd2-47f7-94e6-a303475dc323",
  "isSidechain": false,
  "requestId": "req_011CbAfuSixyP3bAY4UtMFt7",
  "type": "assistant",
  "uuid": "deacab98-37b4-4c16-a500-cdd8201c1748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018DYAJXeWtHp78cMA1TeNhY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 432,
      "cache_read_input_tokens": 30806,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 432,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 30806,
          "cache_creation_input_tokens": 432,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 432
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T20:33:25.741Z_

<details><summary>↩ Tool result · `toolu_0151WTfusoq8g7dVq3BRwySE`</summary>

```text
# GuidedVLA: Key Information Extract

## 1) Full Abstract
"Vision-Language-Action (VLA) models aim for general robot learning by aligning action as a modality within powerful Vision-Language Models (VLMs). Existing VLAs rely on end-to-end supervision to implicitly enable the action decoding process to learn task-relevant features. However, without explicit guidance, these models often overfit to spurious correlations, such as visual shortcuts or environmental noise, limiting their generalization. In this paper, we introduce GuidedVLA, a framework designed to manually guide the action generation to focus on task-relevant factors. Our core insight is to treat the action decoder not as a monolithic learner, but as an assembly of functional components. Individual attention heads are supervised by manually defined auxiliary signals to capture distinct factors. As an initial study, we instantiate this paradigm with three specialized heads: object grounding, spatial geometry, and temporal skill logic. Across simulation and real-robot experiments, GuidedVLA improves success rates in both in-domain and out-of-domain settings compared to strong VLA baselines."

## 2) VLA Backbone
The authors build on **π₀** (pi-zero), described as a "vision-language-action flow model for general robot control." They also report comparisons with OpenVLA but primarily enhance π₀'s architecture.

## 3) Three Factor Types & Supervision

**Object Head (Visual Grounding):** Supervise attention via object masks using negative log loss. "The object mass for action query t is minimized using ℒ_object = −log(max(m_b,t,ε))" where m represents attention mass over task-relevant regions identified by foundation models.

**Skill Head (Temporal Logic Intent):** Pool features across guided layers and heads, project to skill distribution, apply KL-divergence loss against ground-truth soft labels representing temporal skill phases over future horizon.

**Depth Head (3D Structure):** Constraint-based approach—"specific heads to specialize in 3D geometry processing" by restricting attention to frozen depth encoder features (DA3). No explicit loss; architectural constraint forces geometric awareness.

## 4) Key Quantitative Results

**LIBERO-Plus:** Full model achieves **75.4%** average success vs. π₀ baseline at **68.2%** (+7.2 percentage points). Single heads: object head 73.4%, skill head 72.5%, depth head 71.7%.

**RoboTwin 2.0:** Full model reaches **90.63%** average across 8 tasks vs. baseline **77.38%** (+13.25 points).

**Real-World (6 tasks across 2 platforms):** In-domain: 75.8% (ours) vs. 55.8% baseline; Scene: 67.5% vs. 44.2%; Lighting: 79.2% vs. 57.5%.

## 5) Cross-Category/Zero-Shot Transfer
The paper does **not** explicitly evaluate zero-shot transfer to novel object categories. Instead, they assess generalization via perturbations (camera, robot, language, lighting, background, noise, layout) within existing benchmarks and real-world positional/scene/lighting variations. No evidence of cross-category or unseen object evaluation.

## 6) Consistency or Contrastive Losses
**Neither.** The method uses:
- Negative log object mass (supervised attention)
- KL-divergence for skill classification
- Architectural constraints for depth (no loss term)
- Standard flow-matching loss for action generation

No contrastive or consistency objectives mentioned.

## 7) Novel/Unseen Object Handling
The paper does not address novel/unseen objects. Object supervision relies on "foundation models like grounding SAM" to annotate task-relevant regions in training data, followed by human verification. There is no mechanism for generalizing to object categories absent from training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "deacab98-37b4-4c16-a500-cdd8201c1748",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "b7119b83-85bf-437b-af6f-87241ff63b14",
  "toolUseResult": {
    "bytes": 958197,
    "code": 200,
    "codeText": "OK",
    "result": "# GuidedVLA: Key Information Extract\n\n## 1) Full Abstract\n\"Vision-Language-Action (VLA) models aim for general robot learning by aligning action as a modality within powerful Vision-Language Models (VLMs). Existing VLAs rely on end-to-end supervision to implicitly enable the action decoding process to learn task-relevant features. However, without explicit guidance, these models often overfit to spurious correlations, such as visual shortcuts or environmental noise, limiting their generalization. In this paper, we introduce GuidedVLA, a framework designed to manually guide the action generation to focus on task-relevant factors. Our core insight is to treat the action decoder not as a monolithic learner, but as an assembly of functional components. Individual attention heads are supervised by manually defined auxiliary signals to capture distinct factors. As an initial study, we instantiate this paradigm with three specialized heads: object grounding, spatial geometry, and temporal skill logic. Across simulation and real-robot experiments, GuidedVLA improves success rates in both in-domain and out-of-domain settings compared to strong VLA baselines.\"\n\n## 2) VLA Backbone\nThe authors build on **π₀** (pi-zero), described as a \"vision-language-action flow model for general robot control.\" They also report comparisons with OpenVLA but primarily enhance π₀'s architecture.\n\n## 3) Three Factor Types & Supervision\n\n**Object Head (Visual Grounding):** Supervise attention via object masks using negative log loss. \"The object mass for action query t is minimized using ℒ_object = −log(max(m_b,t,ε))\" where m represents attention mass over task-relevant regions identified by foundation models.\n\n**Skill Head (Temporal Logic Intent):** Pool features across guided layers and heads, project to skill distribution, apply KL-divergence loss against ground-truth soft labels representing temporal skill phases over future horizon.\n\n**Depth Head (3D Structure):** Constraint-based approach—\"specific heads to specialize in 3D geometry processing\" by restricting attention to frozen depth encoder features (DA3). No explicit loss; architectural constraint forces geometric awareness.\n\n## 4) Key Quantitative Results\n\n**LIBERO-Plus:** Full model achieves **75.4%** average success vs. π₀ baseline at **68.2%** (+7.2 percentage points). Single heads: object head 73.4%, skill head 72.5%, depth head 71.7%.\n\n**RoboTwin 2.0:** Full model reaches **90.63%** average across 8 tasks vs. baseline **77.38%** (+13.25 points).\n\n**Real-World (6 tasks across 2 platforms):** In-domain: 75.8% (ours) vs. 55.8% baseline; Scene: 67.5% vs. 44.2%; Lighting: 79.2% vs. 57.5%.\n\n## 5) Cross-Category/Zero-Shot Transfer\nThe paper does **not** explicitly evaluate zero-shot transfer to novel object categories. Instead, they assess generalization via perturbations (camera, robot, language, lighting, background, noise, layout) within existing benchmarks and real-world positional/scene/lighting variations. No evidence of cross-category or unseen object evaluation.\n\n## 6) Consistency or Contrastive Losses\n**Neither.** The method uses:\n- Negative log object mass (supervised attention)\n- KL-divergence for skill classification\n- Architectural constraints for depth (no loss term)\n- Standard flow-matching loss for action generation\n\nNo contrastive or consistency objectives mentioned.\n\n## 7) Novel/Unseen Object Handling\nThe paper does not address novel/unseen objects. Object supervision relies on \"foundation models like grounding SAM\" to annotate task-relevant regions in training data, followed by human verification. There is no mechanism for generalizing to object categories absent from training.",
    "durationMs": 14645,
    "url": "https://arxiv.org/html/2605.12369v1"
  },
  "sourceToolAssistantUUID": "deacab98-37b4-4c16-a500-cdd8201c1748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-18 (UTC).**  ## Original idea {   \"title\": \"LACVLA: Enforcing Language-Affordance Grounding via Consistency Object…",
  "leafUuid": "b7119b83-85bf-437b-af6f-87241ff63b14",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise LACVLA affordance consistency for cross-category transfer",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Tool call

_source line 24 · 2026-05-18T20:33:30.961Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016eBmFqpEcUTS7gHdadago1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.05441",
  "prompt": "Extract: 1) Full abstract, 2) What VLAs they benchmark (specific model names and versions), 3) Key quantitative results showing VLA failures on affordance generalization, 4) How many tasks/modules/variants the benchmark has, 5) Whether they test cross-category transfer specifically, 6) Whether they provide a simulation version or only physical, 7) How easy it is for other researchers to reproduce/use the benchmark."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7119b83-85bf-437b-af6f-87241ff63b14",
  "isSidechain": false,
  "requestId": "req_011CbAfvtCBCv7uRERMwk5MA",
  "type": "assistant",
  "uuid": "5e62f6ca-6ae3-4492-af20-c30cea14dcd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B6Yb5m58yH6iPJk7Vtd1UA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 31238,
      "output_tokens": 178,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1095,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 178,
          "cache_read_input_tokens": 31238,
          "cache_creation_input_tokens": 1095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1095
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-18T20:33:38.625Z_

<details><summary>↩ Tool result · `toolu_016eBmFqpEcUTS7gHdadago1`</summary>

```text
# BusyBox Benchmark Analysis

**1) Full Abstract:**
"Vision-Language-Action (VLA) models have been attracting the attention of researchers and practitioners thanks to their promise of generalization. Although single-task policies still offer competitive performance, VLAs are increasingly able to handle commands and environments unseen in their training set. While generalization in vision and language space is undoubtedly important for robust versatile behaviors, a key meta-skill VLAs need to possess is affordance generalization -- the ability to manipulate new objects with familiar physical features. In this work, we present BusyBox, a physical benchmark for systematic semi-automatic evaluation of VLAs' affordance generalization."

**2) VLAs Benchmarked:**
The document specifically identifies π₀.₅ and GR00T-N1.6 as "strong open-weights VLAs" tested on the benchmark.

**3) Key Quantitative Results:**
The paper states that "generalization across BusyBox variants is highly challenging even for strong open-weights VLAs." However, specific failure metrics or percentages are not provided in this abstract.

**4) Benchmark Structure:**
"BusyBox consists of 6 modules with switches, sliders, wires, buttons, a display, and a dial. The modules can be swapped and rotated to create a multitude of BusyBox variations with different visual appearances but the same set of affordances."

**5) Cross-Category Transfer:**
Not explicitly discussed in the provided content.

**6) Simulation vs. Physical:**
The benchmark is physical only. The authors release "CAD files for 3D-printing its parts" and "electronics" materials for assembly.

**7) Reproducibility:**
Highly accessible—authors publish "CAD files," bill of materials, and "a dataset of language-annotated demonstrations" with Mobile Aloha robot recordings at their project website.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e62f6ca-6ae3-4492-af20-c30cea14dcd0",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "29a1cb8d-6552-41b6-ab34-d035c17496e5",
  "toolUseResult": {
    "bytes": 48061,
    "code": 200,
    "codeText": "OK",
    "result": "# BusyBox Benchmark Analysis\n\n**1) Full Abstract:**\n\"Vision-Language-Action (VLA) models have been attracting the attention of researchers and practitioners thanks to their promise of generalization. Although single-task policies still offer competitive performance, VLAs are increasingly able to handle commands and environments unseen in their training set. While generalization in vision and language space is undoubtedly important for robust versatile behaviors, a key meta-skill VLAs need to possess is affordance generalization -- the ability to manipulate new objects with familiar physical features. In this work, we present BusyBox, a physical benchmark for systematic semi-automatic evaluation of VLAs' affordance generalization.\"\n\n**2) VLAs Benchmarked:**\nThe document specifically identifies π₀.₅ and GR00T-N1.6 as \"strong open-weights VLAs\" tested on the benchmark.\n\n**3) Key Quantitative Results:**\nThe paper states that \"generalization across BusyBox variants is highly challenging even for strong open-weights VLAs.\" However, specific failure metrics or percentages are not provided in this abstract.\n\n**4) Benchmark Structure:**\n\"BusyBox consists of 6 modules with switches, sliders, wires, buttons, a display, and a dial. The modules can be swapped and rotated to create a multitude of BusyBox variations with different visual appearances but the same set of affordances.\"\n\n**5) Cross-Category Transfer:**\nNot explicitly discussed in the provided content.\n\n**6) Simulation vs. Physical:**\nThe benchmark is physical only. The authors release \"CAD files for 3D-printing its parts\" and \"electronics\" materials for assembly.\n\n**7) Reproducibility:**\nHighly accessible—authors publish \"CAD files,\" bill of materials, and \"a dataset of language-annotated demonstrations\" with Mobile Aloha robot recordings at their project website.",
    "durationMs": 7660,
    "url": "https://arxiv.org/abs/2602.05441"
  },
  "sourceToolAssistantUUID": "5e62f6ca-6ae3-4492-af20-c30cea14dcd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-18T20:33:41.726Z_

Now let me search for additional recent work that might be relevant to the cross-category transfer framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29a1cb8d-6552-41b6-ab34-d035c17496e5",
  "isSidechain": false,
  "requestId": "req_011CbAfwqJaPPgqEcfb9JVuT",
  "type": "assistant",
  "uuid": "9cd02c71-1c71-45ff-8ac9-31914523d60e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQp2szAYFtm721yGoHYZHC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 32333,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 90,
          "cache_read_input_tokens": 32333,
          "cache_creation_input_tokens": 619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 619
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T20:33:42.176Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VGcJkhKka2ezvwSn53vkQ1`</summary>

```json
{
  "query": "VLA cross-category zero-shot transfer manipulation 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cd02c71-1c71-45ff-8ac9-31914523d60e",
  "isSidechain": false,
  "requestId": "req_011CbAfwqJaPPgqEcfb9JVuT",
  "type": "assistant",
  "uuid": "0cdcf58d-7f0c-49f6-8420-bb8638235dc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BQp2szAYFtm721yGoHYZHC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 32333,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 90,
          "cache_read_input_tokens": 32333,
          "cache_creation_input_tokens": 619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 619
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T20:33:57.999Z_

<details><summary>↩ Tool result · `toolu_01VGcJkhKka2ezvwSn53vkQ1`</summary>

```text
Web search results for query: "VLA cross-category zero-shot transfer manipulation 2026 arXiv"

Links: [{"title":"[2602.10556] LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer","url":"https://arxiv.org/abs/2602.10556"},{"title":"[Paper Note] LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer, Lihan Zha+, arXiv'26, 2026.02 · Issue #4737 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4737"},{"title":"GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub","url":"https://github.com/OpenDriveLab/WholebodyVLA"},{"title":"XL-VLA: Cross-Hand Latent Representation for Vision-Language-Action Models","url":"https://xl-vla.github.io/"},{"title":"Paper page - World Action Models are Zero-shot Policies","url":"https://huggingface.co/papers/2602.15922"},{"title":"Exploring the Limits of Vision-Language-Action Manipulations in Cross-task Generalization","url":"https://arxiv.org/html/2505.15660v1"},{"title":"LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer","url":"https://arxiv.org/html/2602.10556v1"},{"title":"LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer","url":"https://arxiv.org/pdf/2602.10556"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Exploring the Limits of Vision-Language-Action Manipulations in Cross-task Generalization","url":"https://arxiv.org/pdf/2505.15660"}]

Based on the search results, I found several relevant papers from 2026 on arXiv related to Vision-Language-Action (VLA) models and zero-shot transfer in robot manipulation:

## Key Papers Found:

**1. LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer**

LAP introduces Language-Action Pre-training, which represents low-level robot actions directly in natural language, aligning action supervision with the pre-trained vision-language model's input-output distribution. LAP-3B is the first VLA to achieve substantial zero-shot transfer to previously unseen robot embodiments without any embodiment-specific fine-tuning. LAP-3B attains over 50% average zero-shot success, delivering roughly a 2x improvement over the strongest prior VLAs. This paper was published in February 2026 (arXiv:2602.10556).

**2. XL-VLA: Cross-Hand Latent Representation for Vision-Language-Action Models**

XL-VLA is a vision-language-action framework for dexterous manipulation that learns an embodiment-invariant latent action space shared across diverse dexterous hands. This enables training a single policy on pooled multi-hand demonstrations and transferring to new hand–task configurations with minimal friction.

**3. Cross-Task Generalization Studies**

AGNOSTOS is a novel simulation benchmark designed to rigorously evaluate cross-task zero-shot generalization in manipulation, comprising 23 unseen manipulation tasks for test.

These papers represent recent advances in zero-shot transfer and cross-category generalization for VLA models in robotic manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cdcf58d-7f0c-49f6-8420-bb8638235dc2",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "a737edb8-740d-4606-9874-60e6d905c9c8",
  "toolUseResult": {
    "query": "VLA cross-category zero-shot transfer manipulation 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VoVLKTbefPbUh59x9HMLHG",
        "content": [
          {
            "title": "[2602.10556] LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer",
            "url": "https://arxiv.org/abs/2602.10556"
          },
          {
            "title": "[Paper Note] LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer, Lihan Zha+, arXiv'26, 2026.02 · Issue #4737 · AkihikoWatanabe/paper_notes",
            "url": "https://github.com/AkihikoWatanabe/paper_notes/issues/4737"
          },
          {
            "title": "GitHub - OpenDriveLab/WholebodyVLA: [ICLR 2026] Towards Unified Latent VLA for Whole-body Loco-manipulation Control · GitHub",
            "url": "https://github.com/OpenDriveLab/WholebodyVLA"
          },
          {
            "title": "XL-VLA: Cross-Hand Latent Representation for Vision-Language-Action Models",
            "url": "https://xl-vla.github.io/"
          },
          {
            "title": "Paper page - World Action Models are Zero-shot Policies",
            "url": "https://huggingface.co/papers/2602.15922"
          },
          {
            "title": "Exploring the Limits of Vision-Language-Action Manipulations in Cross-task Generalization",
            "url": "https://arxiv.org/html/2505.15660v1"
          },
          {
            "title": "LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer",
            "url": "https://arxiv.org/html/2602.10556v1"
          },
          {
            "title": "LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer",
            "url": "https://arxiv.org/pdf/2602.10556"
          },
          {
            "title": "Vision Language Action Models in Robotic Manipulation: A Systematic Review",
            "url": "https://arxiv.org/html/2507.10672v1"
          },
          {
            "title": "Exploring the Limits of Vision-Language-Action Manipulations in Cross-task Generalization",
            "url": "https://arxiv.org/pdf/2505.15660"
          }
        ]
      },
      "Based on the search results, I found several relevant papers from 2026 on arXiv related to Vision-Language-Action (VLA) models and zero-shot transfer in robot manipulation:\n\n## Key Papers Found:\n\n**1. LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer**\n\nLAP introduces Language-Action Pre-training, which represents low-level robot actions directly in natural language, aligning action supervision with the pre-trained vision-language model's input-output distribution. LAP-3B is the first VLA to achieve substantial zero-shot transfer to previously unseen robot embodiments without any embodiment-specific fine-tuning. LAP-3B attains over 50% average zero-shot success, delivering roughly a 2x improvement over the strongest prior VLAs. This paper was published in February 2026 (arXiv:2602.10556).\n\n**2. XL-VLA: Cross-Hand Latent Representation for Vision-Language-Action Models**\n\nXL-VLA is a vision-language-action framework for dexterous manipulation that learns an embodiment-invariant latent action space shared across diverse dexterous hands. This enables training a single policy on pooled multi-hand demonstrations and transferring to new hand–task configurations with minimal friction.\n\n**3. Cross-Task Generalization Studies**\n\nAGNOSTOS is a novel simulation benchmark designed to rigorously evaluate cross-task zero-shot generalization in manipulation, comprising 23 unseen manipulation tasks for test.\n\nThese papers represent recent advances in zero-shot transfer and cross-category generalization for VLA models in robotic manipulation."
    ],
    "durationSeconds": 15.818594026000007
  },
  "sourceToolAssistantUUID": "0cdcf58d-7f0c-49f6-8420-bb8638235dc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-18T20:33:58.007Z_

```json
{
  "parentUuid": "a737edb8-740d-4606-9874-60e6d905c9c8",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7cd2e39c-9a3e-4ac8-af34-6924aa2d5cbb",
  "timestamp": "2026-05-18T20:33:58.007Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-18T20:34:00.509Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019XCTYnvdGRMYcGRes8sv6p`</summary>

```json
{
  "query": "affordance consistency regularization robotics manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cd2e39c-9a3e-4ac8-af34-6924aa2d5cbb",
  "isSidechain": false,
  "requestId": "req_011CbAfyGA5mLiyVBe9e7VHA",
  "type": "assistant",
  "uuid": "a9c70201-6752-4ff9-b3c8-a25d2a10f752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017GSP7jVPwP87Ydvor1wHKf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1124,
      "cache_read_input_tokens": 32952,
      "output_tokens": 65,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1124,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 65,
          "cache_read_input_tokens": 32952,
          "cache_creation_input_tokens": 1124,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1124
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T20:34:14.574Z_

<details><summary>↩ Tool result · `toolu_019XCTYnvdGRMYcGRes8sv6p`</summary>

```text
Web search results for query: "affordance consistency regularization robotics manipulation 2025 2026"

Links: [{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"[2411.02704] RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/abs/2411.02704"},{"title":"GitHub - HCPLab-SYSU/Embodied_AI_Paper_List: [Embodied-AI-Survey-2025] Paper List and Resource Repository for Embodied AI · GitHub","url":"https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List"},{"title":"A Survey of Embodied Learning for Object-centric Robotic Manipulation | Machine Intelligence Research | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11633-025-1542-8"},{"title":"Affordance-based Robot Manipulation with Flow Matching","url":"https://arxiv.org/pdf/2409.01083"},{"title":"Robo-ABC: Affordance Generalization Beyond Categories via Semantic   Correspondence for Robot Manipulation","url":"https://arxiv.org/pdf/2401.07487"}]

Based on the search results, here are the key findings related to affordance consistency regularization in robotics manipulation for 2025-2026:

## Recent Research in Affordance-Based Robot Manipulation

Recent 2025 work includes UAD (Unsupervised Affordance Distillation) for generalization in robotic manipulation at ICRA 2025, GEAL (Generalizable 3D Affordance Learning with Cross-Modal Consistency) at CVPR 2025, and SeqAfford (Sequential 3D affordance reasoning via Multimodal Large Language Model) at CVPR 2025.

## Affordance as Policy Representations

Recent approaches propose conditioning policies on affordances, which capture the pose of the robot at key stages of the task. Affordances offer expressive yet lightweight abstractions, are easy for users to specify, and facilitate efficient learning by transferring knowledge from large internet datasets.

## Affordance Generalization Methods

Robo-ABC represents an approach to affordance generalization beyond categories via semantic correspondence for robot manipulation. The affordance prediction success rate of Robo-ABC significantly increases by 31.6% compared to end-to-end methods, demonstrating strong generalization capability to novel objects and categories.

## Flow-Based Approaches

Recent work employs parameter-efficient prompt tuning methods for affordance prediction and proposes learning robot trajectories guided by affordances using Flow Matching methods.

The search results indicate significant progress in affordance-based approaches for robot manipulation, with emphasis on generalization, consistency across modalities, and efficient learning methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9c70201-6752-4ff9-b3c8-a25d2a10f752",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "d7ff8a6c-a5d5-4fdd-86a2-f5f031f6c1bc",
  "toolUseResult": {
    "query": "affordance consistency regularization robotics manipulation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CXUEyHvUHkeiZkz4dgeycr",
        "content": [
          {
            "title": "RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation",
            "url": "https://arxiv.org/pdf/2411.02704"
          },
          {
            "title": "[2411.02704] RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation",
            "url": "https://arxiv.org/abs/2411.02704"
          },
          {
            "title": "GitHub - HCPLab-SYSU/Embodied_AI_Paper_List: [Embodied-AI-Survey-2025] Paper List and Resource Repository for Embodied AI · GitHub",
            "url": "https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List"
          },
          {
            "title": "A Survey of Embodied Learning for Object-centric Robotic Manipulation | Machine Intelligence Research | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11633-025-1542-8"
          },
          {
            "title": "Affordance-based Robot Manipulation with Flow Matching",
            "url": "https://arxiv.org/pdf/2409.01083"
          },
          {
            "title": "Robo-ABC: Affordance Generalization Beyond Categories via Semantic   Correspondence for Robot Manipulation",
            "url": "https://arxiv.org/pdf/2401.07487"
          }
        ]
      },
      "Based on the search results, here are the key findings related to affordance consistency regularization in robotics manipulation for 2025-2026:\n\n## Recent Research in Affordance-Based Robot Manipulation\n\nRecent 2025 work includes UAD (Unsupervised Affordance Distillation) for generalization in robotic manipulation at ICRA 2025, GEAL (Generalizable 3D Affordance Learning with Cross-Modal Consistency) at CVPR 2025, and SeqAfford (Sequential 3D affordance reasoning via Multimodal Large Language Model) at CVPR 2025.\n\n## Affordance as Policy Representations\n\nRecent approaches propose conditioning policies on affordances, which capture the pose of the robot at key stages of the task. Affordances offer expressive yet lightweight abstractions, are easy for users to specify, and facilitate efficient learning by transferring knowledge from large internet datasets.\n\n## Affordance Generalization Methods\n\nRobo-ABC represents an approach to affordance generalization beyond categories via semantic correspondence for robot manipulation. The affordance prediction success rate of Robo-ABC significantly increases by 31.6% compared to end-to-end methods, demonstrating strong generalization capability to novel objects and categories.\n\n## Flow-Based Approaches\n\nRecent work employs parameter-efficient prompt tuning methods for affordance prediction and proposes learning robot trajectories guided by affordances using Flow Matching methods.\n\nThe search results indicate significant progress in affordance-based approaches for robot manipulation, with emphasis on generalization, consistency across modalities, and efficient learning methods."
    ],
    "durationSeconds": 14.059932398999997
  },
  "sourceToolAssistantUUID": "a9c70201-6752-4ff9-b3c8-a25d2a10f752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-18T20:34:17.142Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LuQ3PaZ3f4cvYeNGaDTCdB`</summary>

```json
{
  "query": "VLA language grounding bottleneck architecture stop-gradient 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7ff8a6c-a5d5-4fdd-86a2-f5f031f6c1bc",
  "isSidechain": false,
  "requestId": "req_011CbAfzV1moMwXTwDau1mat",
  "type": "assistant",
  "uuid": "56558df2-a4f8-4fe3-9ebe-b65160558850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2cWk3ed9a8EvqYgSyXjju",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 783,
      "cache_read_input_tokens": 34076,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 783,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 34076,
          "cache_creation_input_tokens": 783,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 783
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-18T20:34:24.594Z_

<details><summary>↩ Tool result · `toolu_01LuQ3PaZ3f4cvYeNGaDTCdB`</summary>

```text
Web search results for query: "VLA language grounding bottleneck architecture stop-gradient 2025 2026"

Links: [{"title":"[2604.09824] ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.09824"},{"title":"Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration","url":"https://arxiv.org/html/2603.06001v1"},{"title":"ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/html/2604.09824"},{"title":"Characterizing VLA Models: Identifying the Action Generation Bottleneck for Edge AI Architectures","url":"https://arxiv.org/pdf/2603.02271"},{"title":"2025-9-22 A Vision-Language-Action-Critic Model","url":"https://arxiv.org/pdf/2509.15937"},{"title":"LangForce: Bayesian Decomposition of Vision Language ...","url":"https://arxiv.org/pdf/2601.15197"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"}]

Based on the search results, I found several relevant papers addressing language grounding bottlenecks and architectural approaches in Vision-Language-Action (VLA) models:

## Key Findings:

### Verified Grounding Bottleneck Approach
ProGAL-VLA imposes a verified grounding bottleneck where every symbolic sub-goal must correspond to a physically reachable entity before the policy can act, which suppresses language-ignorance failure modes, avoids visually driven shortcuts, and stabilizes behavior under ambiguity. The verification bottleneck increases mutual information of language-actions, the GAC loss imposes an entity-level InfoNCE bound, and attention entropy yields calibrated selective prediction.

### Linguistic Grounding via Attention Recalibration
In modern VLA architectures, action-query tokens disproportionately attend to visually salient tokens, forming vision-dominant attention sinks that suppress instruction tokens, with linguistic blindness attributed to a structural cross-modal competition imbalance induced by attention sink dynamics.

### Bottleneck Interface Design
Recent approaches use queries as a dedicated bottleneck interface between the VLM and the continuous action head, with exclusive use of their corresponding hidden states to condition the action head, unlike architectures that feed hidden states of all input tokens to the action expert.

### Architectural Paradigms
Recent VLA models have converged toward three major architectural paradigms—early fusion models, dual-system architectures, and self-correcting frameworks—each addressing specific challenges in grounding, generalization, and action reliability in real-world robotic systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56558df2-a4f8-4fe3-9ebe-b65160558850",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "374ec422-ac90-4ce8-8dc6-f26f51619836",
  "toolUseResult": {
    "query": "VLA language grounding bottleneck architecture stop-gradient 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FTX35UF4BbsBSGKqS6ovw9",
        "content": [
          {
            "title": "[2604.09824] ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2604.09824"
          },
          {
            "title": "Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration",
            "url": "https://arxiv.org/html/2603.06001v1"
          },
          {
            "title": "ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2604.09824"
          },
          {
            "title": "Characterizing VLA Models: Identifying the Action Generation Bottleneck for Edge AI Architectures",
            "url": "https://arxiv.org/pdf/2603.02271"
          },
          {
            "title": "2025-9-22 A Vision-Language-Action-Critic Model",
            "url": "https://arxiv.org/pdf/2509.15937"
          },
          {
            "title": "LangForce: Bayesian Decomposition of Vision Language ...",
            "url": "https://arxiv.org/pdf/2601.15197"
          },
          {
            "title": "Vision-Language-Action Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v1"
          },
          {
            "title": "Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v2"
          }
        ]
      },
      "Based on the search results, I found several relevant papers addressing language grounding bottlenecks and architectural approaches in Vision-Language-Action (VLA) models:\n\n## Key Findings:\n\n### Verified Grounding Bottleneck Approach\nProGAL-VLA imposes a verified grounding bottleneck where every symbolic sub-goal must correspond to a physically reachable entity before the policy can act, which suppresses language-ignorance failure modes, avoids visually driven shortcuts, and stabilizes behavior under ambiguity. The verification bottleneck increases mutual information of language-actions, the GAC loss imposes an entity-level InfoNCE bound, and attention entropy yields calibrated selective prediction.\n\n### Linguistic Grounding via Attention Recalibration\nIn modern VLA architectures, action-query tokens disproportionately attend to visually salient tokens, forming vision-dominant attention sinks that suppress instruction tokens, with linguistic blindness attributed to a structural cross-modal competition imbalance induced by attention sink dynamics.\n\n### Bottleneck Interface Design\nRecent approaches use queries as a dedicated bottleneck interface between the VLM and the continuous action head, with exclusive use of their corresponding hidden states to condition the action head, unlike architectures that feed hidden states of all input tokens to the action expert.\n\n### Architectural Paradigms\nRecent VLA models have converged toward three major architectural paradigms—early fusion models, dual-system architectures, and self-correcting frameworks—each addressing specific challenges in grounding, generalization, and action reliability in real-world robotic systems."
    ],
    "durationSeconds": 7.4484438009999865
  },
  "sourceToolAssistantUUID": "56558df2-a4f8-4fe3-9ebe-b65160558850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-18T20:34:28.529Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0143mqwzMUQt7VuPTUQ8Fw4W`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.09824",
  "prompt": "Extract: 1) Full abstract, 2) What is the \"verified grounding bottleneck\" mechanism exactly, 3) How does it force language conditioning, 4) Key results and benchmarks, 5) Does it use consistency objectives, 6) Does it address cross-category transfer. Be specific."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "374ec422-ac90-4ce8-8dc6-f26f51619836",
  "isSidechain": false,
  "requestId": "req_011CbAg1Dpk6GwgqTCnG3JnD",
  "type": "assistant",
  "uuid": "0090210a-8b2d-488b-99e6-144e6c4ec49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016kCtCcf3hK8mKyWPq2RYhL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 34859,
      "output_tokens": 148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 148,
          "cache_read_input_tokens": 34859,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-18 (UTC).**  ## Original idea {   \"title\": \"LACVLA: Enforcing Language-Affordance Grounding via Consistency Object…",
  "leafUuid": "0090210a-8b2d-488b-99e6-144e6c4ec49f",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise LACVLA affordance consistency for cross-category transfer",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Tool result

_source line 37 · 2026-05-18T20:34:37.812Z_

<details><summary>↩ Tool result · `toolu_0143mqwzMUQt7VuPTUQ8Fw4W`</summary>

```text
# ProGAL-VLA Paper Analysis

## 1) Full Abstract

Vision language action models often ignore language and rely on visual shortcuts. ProGAL-VLA addresses this by constructing a 3D entity-centric graph, using a slow planner for symbolic sub-goals, and aligning them via a Grounding Alignment Contrastive loss. All actions depend on a verified goal embedding whose attention entropy signals ambiguity. Results show substantial improvements in robustness, reduced language ignorance, and enhanced ambiguity awareness across benchmarks.

## 2) Verified Grounding Bottleneck Mechanism

The document states: "All actions are conditioned on a verified goal embedding $g\_t$, whose attention entropy provides an intrinsic ambiguity signal." The mechanism uses a verification bottleneck that increases mutual information between language and actions, serving as a gating mechanism for action selection based on grounded entity alignment.

## 3) Language Conditioning Mechanism

The approach forces language conditioning through the Grounding Alignment Contrastive (GAC) loss, which aligns symbolic sub-goals with grounded entities. This creates a dependency where actions cannot be executed without properly grounded language-entity alignment, preventing visual shortcut exploitation.

## 4) Key Results and Benchmarks

**LIBERO-Plus:**
- Robustness under perturbations: 30.3% → 71.5%
- Language ignorance: reduced 3-4x
- Entity retrieval: 0.41 → 0.71 Recall@1

**Custom Ambiguity Benchmark:**
- AUROC: 0.81 (vs. 0.52 baseline)
- AUPR: 0.79
- Clarification on ambiguous inputs: 0.09 → 0.81

## 5) Consistency Objectives

The document does not explicitly mention consistency objectives in the provided content.

## 6) Cross-Category Transfer

The document does not address cross-category transfer in the available excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0090210a-8b2d-488b-99e6-144e6c4ec49f",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "db8efaaf-f5a1-4873-a1a0-92570512c647",
  "toolUseResult": {
    "bytes": 46291,
    "code": 200,
    "codeText": "OK",
    "result": "# ProGAL-VLA Paper Analysis\n\n## 1) Full Abstract\n\nVision language action models often ignore language and rely on visual shortcuts. ProGAL-VLA addresses this by constructing a 3D entity-centric graph, using a slow planner for symbolic sub-goals, and aligning them via a Grounding Alignment Contrastive loss. All actions depend on a verified goal embedding whose attention entropy signals ambiguity. Results show substantial improvements in robustness, reduced language ignorance, and enhanced ambiguity awareness across benchmarks.\n\n## 2) Verified Grounding Bottleneck Mechanism\n\nThe document states: \"All actions are conditioned on a verified goal embedding $g\\_t$, whose attention entropy provides an intrinsic ambiguity signal.\" The mechanism uses a verification bottleneck that increases mutual information between language and actions, serving as a gating mechanism for action selection based on grounded entity alignment.\n\n## 3) Language Conditioning Mechanism\n\nThe approach forces language conditioning through the Grounding Alignment Contrastive (GAC) loss, which aligns symbolic sub-goals with grounded entities. This creates a dependency where actions cannot be executed without properly grounded language-entity alignment, preventing visual shortcut exploitation.\n\n## 4) Key Results and Benchmarks\n\n**LIBERO-Plus:**\n- Robustness under perturbations: 30.3% → 71.5%\n- Language ignorance: reduced 3-4x\n- Entity retrieval: 0.41 → 0.71 Recall@1\n\n**Custom Ambiguity Benchmark:**\n- AUROC: 0.81 (vs. 0.52 baseline)\n- AUPR: 0.79\n- Clarification on ambiguous inputs: 0.09 → 0.81\n\n## 5) Consistency Objectives\n\nThe document does not explicitly mention consistency objectives in the provided content.\n\n## 6) Cross-Category Transfer\n\nThe document does not address cross-category transfer in the available excerpt.",
    "durationMs": 9279,
    "url": "https://arxiv.org/abs/2604.09824"
  },
  "sourceToolAssistantUUID": "0090210a-8b2d-488b-99e6-144e6c4ec49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-18T20:34:40.432Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T4UboAFaJLx7j91bWrgSUs`</summary>

```json
{
  "query": "\"attention recalibration\" VLA linguistic grounding arXiv 2603.06001 train-free"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db8efaaf-f5a1-4873-a1a0-92570512c647",
  "isSidechain": false,
  "requestId": "req_011CbAg2CNxGxiVpEgrUUpSn",
  "type": "assistant",
  "uuid": "baa27c3e-6d92-4d2e-922d-647867a789cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FK9yCQQQ6DyNVSgeg6siCx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 614,
      "cache_read_input_tokens": 35688,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 614,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 35688,
          "cache_creation_input_tokens": 614,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 614
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-18T20:34:45.444Z_

<details><summary>↩ Tool result · `toolu_01T4UboAFaJLx7j91bWrgSUs`</summary>

```text
Web search results for query: ""attention recalibration" VLA linguistic grounding arXiv 2603.06001 train-free"

Links: [{"title":"Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration","url":"https://arxiv.org/html/2603.06001v1"},{"title":"GitHub - BaiShuanghao/my_arXiv_daily · GitHub","url":"https://github.com/BaiShuanghao/my_arXiv_daily"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/pdf/2508.10333"},{"title":"Conscious Gaze: Adaptive Attention Mechanisms for Hallucination Mitigation in Vision-Language Models","url":"https://arxiv.org/pdf/2512.05546"},{"title":"Your Large Vision-Language Model Only Needs A Few Attention Heads For   Visual Grounding","url":"https://arxiv.org/pdf/2503.06287"},{"title":"Grounding Hierarchical Vision-Language-Action Models Through Explicit Language-Action Alignment","url":"https://arxiv.org/pdf/2604.05614"}]

Based on the search results, I found the paper you're looking for:

The paper is titled "Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration" and was published on arXiv as 2603.06001 on March 6, 2026, by researchers from Tsinghua University, Singapore Management University, and Fudan University.

The paper addresses a critical failure mode where Vision-Language-Action (VLA) policies continue executing visually plausible actions even when the language instruction contradicts the scene—a phenomenon the researchers call "linguistic blindness," where VLA policies prioritize visual priors over instruction semantics during action generation.

To systematically analyze this issue, the authors introduce ICBench, a diagnostic benchmark constructed from the LIBERO dataset that probes language–action coupling by injecting controlled out-of-distribution instructions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "baa27c3e-6d92-4d2e-922d-647867a789cc",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "66d389b3-c3f1-46c3-be63-4cb93b32448a",
  "toolUseResult": {
    "query": "\"attention recalibration\" VLA linguistic grounding arXiv 2603.06001 train-free",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N3mSqHbFuDJuD2FSFJPaKm",
        "content": [
          {
            "title": "Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration",
            "url": "https://arxiv.org/html/2603.06001v1"
          },
          {
            "title": "GitHub - BaiShuanghao/my_arXiv_daily · GitHub",
            "url": "https://github.com/BaiShuanghao/my_arXiv_daily"
          },
          {
            "title": "ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/pdf/2508.10333"
          },
          {
            "title": "Conscious Gaze: Adaptive Attention Mechanisms for Hallucination Mitigation in Vision-Language Models",
            "url": "https://arxiv.org/pdf/2512.05546"
          },
          {
            "title": "Your Large Vision-Language Model Only Needs A Few Attention Heads For   Visual Grounding",
            "url": "https://arxiv.org/pdf/2503.06287"
          },
          {
            "title": "Grounding Hierarchical Vision-Language-Action Models Through Explicit Language-Action Alignment",
            "url": "https://arxiv.org/pdf/2604.05614"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper is titled \"Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration\" and was published on arXiv as 2603.06001 on March 6, 2026, by researchers from Tsinghua University, Singapore Management University, and Fudan University.\n\nThe paper addresses a critical failure mode where Vision-Language-Action (VLA) policies continue executing visually plausible actions even when the language instruction contradicts the scene—a phenomenon the researchers call \"linguistic blindness,\" where VLA policies prioritize visual priors over instruction semantics during action generation.\n\nTo systematically analyze this issue, the authors introduce ICBench, a diagnostic benchmark constructed from the LIBERO dataset that probes language–action coupling by injecting controlled out-of-distribution instructions."
    ],
    "durationSeconds": 5.006836202000006
  },
  "sourceToolAssistantUUID": "baa27c3e-6d92-4d2e-922d-647867a789cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-18T20:34:48.500Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014wGGRGoFK9b5MfCF153uhv`</summary>

```json
{
  "query": "GuidedVLA RSS 2026 results LIBERO success rate pi0 baseline numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66d389b3-c3f1-46c3-be63-4cb93b32448a",
  "isSidechain": false,
  "requestId": "req_011CbAg2m1kPobnAa9RxwaL8",
  "type": "assistant",
  "uuid": "f1d53055-a244-4b2d-a084-aabf8deb7928",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BFbHaW8VdLEzoH7pR26s5A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 606,
      "cache_read_input_tokens": 36302,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 606,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 36302,
          "cache_creation_input_tokens": 606,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 606
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-18T20:35:09.179Z_

<details><summary>↩ Tool result · `toolu_014wGGRGoFK9b5MfCF153uhv`</summary>

```text
Web search results for query: "GuidedVLA RSS 2026 results LIBERO success rate pi0 baseline numbers"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"PI0 Evaluation results on LIBERO is very low · Issue #952 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/952"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/734"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Success rates of OpenVLA, pi0, pi0.5, and univla under object position... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rates-of-OpenVLA-pi0-pi05-and-univla-under-object-position-perturbations_fig1_396249917"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"pi0.5 on LIBERO simulation reproduce, zero success rate on pi05_libero_base · Issue #2533 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2533"},{"title":"Value Vision-Language-Action Planning & Search","url":"https://arxiv.org/pdf/2601.00969"}]

I found some relevant results about VLA models and LIBERO benchmarks. However, I didn't find specific information about "GuidedVLA RSS 2026 results." Let me search more specifically for that:

Links: [{"title":"RSS 2026","url":"https://roboticsconference.org/"},{"title":"2026 RSS Scientific Meeting","url":"https://rss2026.eventscribe.net/"},{"title":"RSS 2026 Conference | OpenReview","url":"https://openreview.net/group?id=roboticsfoundation.org%2FRSS%2F2026%2FConference"},{"title":"Accepted Papers · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/"},{"title":"SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/11/"},{"title":"Lihan Zha on X: \"Excited to share LAP got accepted to RSS 2026!! See you in Sydney 🦘\" / X","url":"https://x.com/LihanZha/status/2048773362197884978"},{"title":"Formula RSS 3 2026 V6 released - Race Sim Studio","url":"https://racesimstudio.com/formula-rss-3-2026-v6-released"},{"title":"Call for Papers · Robotics: Science and Systems","url":"https://roboticsconference.org/information/cfp/"},{"title":"RSS: Robotics: Science and Systems 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=2506&f=Robotics"}]

The search results show that RSS 2026 is an upcoming conference (July 13-17, 2026 in Sydney), but I haven't found specific papers about "GuidedVLA" yet. Let me search more directly for that term:

Links: [{"title":"SignVLA: A Gloss-Free Vision-Language-Action Framework for Real-Time Sign Language-Guided Robotic Manipulation","url":"https://arxiv.org/pdf/2602.22514"},{"title":"OmniGuide: Universal Guidance Fields for Enhancing Generalist Robot Policies","url":"https://arxiv.org/pdf/2603.10052"},{"title":"ACG: Action Coherence Guidance for Flow-based Vision-Language-Action models","url":"https://arxiv.org/pdf/2510.22201"},{"title":"dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought","url":"https://arxiv.org/pdf/2509.25681"},{"title":"DAM-VLA: A Dynamic Action Model-Based Vision-Language-Action Framework for Robot Manipulation","url":"https://arxiv.org/pdf/2603.00926"}]

I found OmniGuide which mentions "guidance" for VLA models, but not the specific "GuidedVLA" paper. Let me try another search:

Links: [{"title":"Value Vision-Language-Action Planning & Search","url":"https://arxiv.org/pdf/2601.00969"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/pdf/2510.03827"},{"title":"When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs","url":"https://arxiv.org/pdf/2602.17659"},{"title":"TAG: Target-Agnostic Guidance for Stable Object-Centric Inference in Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.24584"},{"title":"Libero: A Definite Guide - Volleyball and Me","url":"https://www.volleyballandme.com/volleyball-libero/"}]

I found TAG and CAG papers that discuss guidance mechanisms for VLAs, but still not the specific "GuidedVLA" paper. Let me try one more search with a different approach:

Links: [{"title":"[2605.12369v1] GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization","url":"https://arxiv.org/abs/2605.12369v1"},{"title":"GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization","url":"https://arxiv.org/html/2605.12369v1"},{"title":"GitHub - Ed1sonChen/DailyArxiv · GitHub","url":"https://github.com/Ed1sonChen/DailyArxiv"},{"title":"Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models","url":"https://arxiv.org/pdf/2511.21663"},{"title":"$\\pi$, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation","url":"https://arxiv.org/pdf/2603.25038"}]

Great! I found the GuidedVLA paper. Now let me search for the specific results mentioned in your query (RSS 2026, LIBERO success rates, π0 baseline numbers):

Links: [{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in","url":"https://www.arxiv.org/pdf/2512.07472"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"PI0 Evaluation results on LIBERO is very low · Issue #952 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/952"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"Success rates of OpenVLA, pi0, pi0.5, and univla under object position... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rates-of-OpenVLA-pi0-pi05-and-univla-under-object-position-perturbations_fig1_396249917"},{"title":"Poor training performance (3.3% success rate) with pi0 model on locally downloaded official LIBERO dataset · Issue #804 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/804"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Value Vision-Language-Action Planning & Search","url":"https://arxiv.org/pdf/2601.00969"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"}]

Based on my search results, I have found information about the GuidedVLA paper and various LIBERO benchmark results. Here's what I found:

## GuidedVLA Overview

GuidedVLA is a framework designed to manually guide the action generation to focus on task-relevant factors. The core insight is to treat the action decoder not as a monolithic learner, but as an assembly of functional components. Individual attention heads are supervised by manually defined auxiliary signals to capture distinct factors, including three specialized heads: object grounding, spatial geometry, and temporal skill logic.

## Performance Results

Across simulation and real-robot experiments, GuidedVLA improves success rates in both in-domain and out-of-domain settings compared to strong VLA baselines.

## Related π0 Baseline Numbers on LIBERO

While I found the GuidedVLA paper, the specific detailed results tables comparing GuidedVLA with π0 baselines on LIBERO were not fully accessible in the search results. However, I can note that in related work:

- OpenVLA-OFT achieves 97.1% average success rate across 4 LIBERO task suites, outperforming π0 and other models
- Pi0.5 achieves a 0.38 success rate in the libero-goal task under position changes, compared to 0 for OpenVLA and Pi0 under robustness perturbations

The GuidedVLA paper (arxiv 2605.12369) was posted about a week ago and may be related to upcoming robotics conference submissions, though it doesn't appear to be explicitly confirmed for RSS 2026 yet in the available search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1d53055-a244-4b2d-a084-aabf8deb7928",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "bcfa6ee2-d10f-4096-9093-e695f8fa9912",
  "toolUseResult": {
    "query": "GuidedVLA RSS 2026 results LIBERO success rate pi0 baseline numbers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F66UN9ZnVXbZzkdGJhHbUw",
        "content": [
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "PI0 Evaluation results on LIBERO is very low · Issue #952 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/952"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/734"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "Success rates of OpenVLA, pi0, pi0.5, and univla under object position... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Success-rates-of-OpenVLA-pi0-pi05-and-univla-under-object-position-perturbations_fig1_396249917"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "pi0.5 on LIBERO simulation reproduce, zero success rate on pi05_libero_base · Issue #2533 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2533"
          },
          {
            "title": "Value Vision-Language-Action Planning & Search",
            "url": "https://arxiv.org/pdf/2601.00969"
          }
        ]
      },
      "I found some relevant results about VLA models and LIBERO benchmarks. However, I didn't find specific information about \"GuidedVLA RSS 2026 results.\" Let me search more specifically for that:",
      {
        "tool_use_id": "srvtoolu_01MYrQyUyRxmgp7L4jLwizt6",
        "content": [
          {
            "title": "RSS 2026",
            "url": "https://roboticsconference.org/"
          },
          {
            "title": "2026 RSS Scientific Meeting",
            "url": "https://rss2026.eventscribe.net/"
          },
          {
            "title": "RSS 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=roboticsfoundation.org%2FRSS%2F2026%2FConference"
          },
          {
            "title": "Accepted Papers · Robotics: Science and Systems",
            "url": "https://roboticsconference.org/program/papers/"
          },
          {
            "title": "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models · Robotics: Science and Systems",
            "url": "https://roboticsconference.org/program/papers/11/"
          },
          {
            "title": "Lihan Zha on X: \"Excited to share LAP got accepted to RSS 2026!! See you in Sydney 🦘\" / X",
            "url": "https://x.com/LihanZha/status/2048773362197884978"
          },
          {
            "title": "Formula RSS 3 2026 V6 released - Race Sim Studio",
            "url": "https://racesimstudio.com/formula-rss-3-2026-v6-released"
          },
          {
            "title": "Call for Papers · Robotics: Science and Systems",
            "url": "https://roboticsconference.org/information/cfp/"
          },
          {
            "title": "RSS: Robotics: Science and Systems 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=2506&f=Robotics"
          }
        ]
      },
      "The search results show that RSS 2026 is an upcoming conference (July 13-17, 2026 in Sydney), but I haven't found specific papers about \"GuidedVLA\" yet. Let me search more directly for that term:",
      {
        "tool_use_id": "srvtoolu_01F3b9cHyV47dDzQpAoARawg",
        "content": [
          {
            "title": "SignVLA: A Gloss-Free Vision-Language-Action Framework for Real-Time Sign Language-Guided Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2602.22514"
          },
          {
            "title": "OmniGuide: Universal Guidance Fields for Enhancing Generalist Robot Policies",
            "url": "https://arxiv.org/pdf/2603.10052"
          },
          {
            "title": "ACG: Action Coherence Guidance for Flow-based Vision-Language-Action models",
            "url": "https://arxiv.org/pdf/2510.22201"
          },
          {
            "title": "dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought",
            "url": "https://arxiv.org/pdf/2509.25681"
          },
          {
            "title": "DAM-VLA: A Dynamic Action Model-Based Vision-Language-Action Framework for Robot Manipulation",
            "url": "https://arxiv.org/pdf/2603.00926"
          }
        ]
      },
      "I found OmniGuide which mentions \"guidance\" for VLA models, but not the specific \"GuidedVLA\" paper. Let me try another search:",
      {
        "tool_use_id": "srvtoolu_012rwDCDd4wP3tU4iZnuwBhR",
        "content": [
          {
            "title": "Value Vision-Language-Action Planning & Search",
            "url": "https://arxiv.org/pdf/2601.00969"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/pdf/2509.12594"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs",
            "url": "https://arxiv.org/pdf/2602.17659"
          },
          {
            "title": "TAG: Target-Agnostic Guidance for Stable Object-Centric Inference in Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.24584"
          },
          {
            "title": "Libero: A Definite Guide - Volleyball and Me",
            "url": "https://www.volleyballandme.com/volleyball-libero/"
          }
        ]
      },
      "I found TAG and CAG papers that discuss guidance mechanisms for VLAs, but still not the specific \"GuidedVLA\" paper. Let me try one more search with a different approach:",
      {
        "tool_use_id": "srvtoolu_0161BNvMa8A7BbwS9y7Bzf1C",
        "content": [
          {
            "title": "[2605.12369v1] GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization",
            "url": "https://arxiv.org/abs/2605.12369v1"
          },
          {
            "title": "GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization",
            "url": "https://arxiv.org/html/2605.12369v1"
          },
          {
            "title": "GitHub - Ed1sonChen/DailyArxiv · GitHub",
            "url": "https://github.com/Ed1sonChen/DailyArxiv"
          },
          {
            "title": "Attention-Guided Patch-Wise Sparse Adversarial Attacks on Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2511.21663"
          },
          {
            "title": "$\\pi$, But Make It Fly: Physics-Guided Transfer of VLA Models to Aerial Manipulation",
            "url": "https://arxiv.org/pdf/2603.25038"
          }
        ]
      },
      "Great! I found the GuidedVLA paper. Now let me search for the specific results mentioned in your query (RSS 2026, LIBERO success rates, π0 baseline numbers):",
      {
        "tool_use_id": "srvtoolu_01Jcom6w3g2u4QHRKV1Z2yx3",
        "content": [
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in",
            "url": "https://www.arxiv.org/pdf/2512.07472"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "PI0 Evaluation results on LIBERO is very low · Issue #952 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/952"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "Success rates of OpenVLA, pi0, pi0.5, and univla under object position... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Success-rates-of-OpenVLA-pi0-pi05-and-univla-under-object-position-perturbations_fig1_396249917"
          },
          {
            "title": "Poor training performance (3.3% success rate) with pi0 model on locally downloaded official LIBERO dataset · Issue #804 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/804"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "Value Vision-Language-Action Planning & Search",
            "url": "https://arxiv.org/pdf/2601.00969"
          },
          {
            "title": "(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"
          }
        ]
      },
      "Based on my search results, I have found information about the GuidedVLA paper and various LIBERO benchmark results. Here's what I found:\n\n## GuidedVLA Overview\n\nGuidedVLA is a framework designed to manually guide the action generation to focus on task-relevant factors. The core insight is to treat the action decoder not as a monolithic learner, but as an assembly of functional components. Individual attention heads are supervised by manually defined auxiliary signals to capture distinct factors, including three specialized heads: object grounding, spatial geometry, and temporal skill logic.\n\n## Performance Results\n\nAcross simulation and real-robot experiments, GuidedVLA improves success rates in both in-domain and out-of-domain settings compared to strong VLA baselines.\n\n## Related π0 Baseline Numbers on LIBERO\n\nWhile I found the GuidedVLA paper, the specific detailed results tables comparing GuidedVLA with π0 baselines on LIBERO were not fully accessible in the search results. However, I can note that in related work:\n\n- OpenVLA-OFT achieves 97.1% average success rate across 4 LIBERO task suites, outperforming π0 and other models\n- Pi0.5 achieves a 0.38 success rate in the libero-goal task under position changes, compared to 0 for OpenVLA and Pi0 under robustness perturbations\n\nThe GuidedVLA paper (arxiv 2605.12369) was posted about a week ago and may be related to upcoming robotics conference submissions, though it doesn't appear to be explicitly confirmed for RSS 2026 yet in the available search results."
    ],
    "durationSeconds": 20.67443034199998
  },
  "sourceToolAssistantUUID": "f1d53055-a244-4b2d-a084-aabf8deb7928",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-18T20:35:12.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0152CZhaeNgTmn72f4FQypEx`</summary>

```json
{
  "query": "ProGAL-VLA verified grounding bottleneck arXiv 2604.09824 cross-category novel objects"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcfa6ee2-d10f-4096-9093-e695f8fa9912",
  "isSidechain": false,
  "requestId": "req_011CbAg4WUgnBrHpKAdRokGa",
  "type": "assistant",
  "uuid": "02861c5f-c956-4af6-ad58-b09c6b9006c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016RAFCX4HSy1Ev4dbH4w98z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2943,
      "cache_read_input_tokens": 36908,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2943,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 36908,
          "cache_creation_input_tokens": 2943,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2943
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-18 (UTC).**  ## Original idea {   \"title\": \"LACVLA: Enforcing Language-Affordance Grounding via Consistency Object…",
  "leafUuid": "02861c5f-c956-4af6-ad58-b09c6b9006c5",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise LACVLA affordance consistency for cross-category transfer",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Tool result

_source line 45 · 2026-05-18T20:35:18.405Z_

<details><summary>↩ Tool result · `toolu_0152CZhaeNgTmn72f4FQypEx`</summary>

```text
Web search results for query: "ProGAL-VLA verified grounding bottleneck arXiv 2604.09824 cross-category novel objects"

Links: [{"title":"ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/html/2604.09824"},{"title":"[2604.09824] ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.09824"},{"title":"Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding","url":"https://arxiv.org/pdf/2512.22519"},{"title":"[2604.01893] ProVG: Progressive Visual Grounding via Language Decoupling for Remote Sensing Imagery","url":"https://arxiv.org/abs/2604.01893"},{"title":"[2604.24036] Robust Grounding with MLLMs against Occlusion and Small Objects via Language-guided Semantic Cues","url":"https://arxiv.org/abs/2604.24036"},{"title":"Zero-Shot Grounding of Objects from Natural Language Queries","url":"https://arxiv.org/pdf/1908.07129"}]

I found the paper you're looking for. ProGAL-VLA (Prospective Grounding and Alignment VLA) addresses the issue that vision language action models often exhibit language ignorance by relying on visual shortcuts. The model constructs a 3D entity-centric graph (GSM), uses a slow planner to produce symbolic sub-goals, and aligns them with grounded entities via a Grounding Alignment Contrastive (GAC) loss.

The system uses a verification bottleneck that separates slow symbolic planning from fast control. All actions are conditioned on a verified goal embedding whose attention entropy provides an intrinsic ambiguity signal.

On LIBERO-Plus, ProGAL-VLA increases robustness under robot perturbations from 30.3 to 71.5 percent, reduces language ignorance by 3x-4x, and improves entity retrieval from 0.41 to 0.71 Recall@1. The paper (arXiv 2604.09824) was published on April 10, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02861c5f-c956-4af6-ad58-b09c6b9006c5",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "e79db049-277f-44de-afce-d94c89489d8c",
  "toolUseResult": {
    "query": "ProGAL-VLA verified grounding bottleneck arXiv 2604.09824 cross-category novel objects",
    "results": [
      {
        "tool_use_id": "srvtoolu_01W44eX7RSygZvM1YUpSYtcy",
        "content": [
          {
            "title": "ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2604.09824"
          },
          {
            "title": "[2604.09824] ProGAL-VLA: Grounded Alignment through Prospective Reasoning in Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2604.09824"
          },
          {
            "title": "Clutter-Resistant Vision-Language-Action Models through Object-Centric and Geometry Grounding",
            "url": "https://arxiv.org/pdf/2512.22519"
          },
          {
            "title": "[2604.01893] ProVG: Progressive Visual Grounding via Language Decoupling for Remote Sensing Imagery",
            "url": "https://arxiv.org/abs/2604.01893"
          },
          {
            "title": "[2604.24036] Robust Grounding with MLLMs against Occlusion and Small Objects via Language-guided Semantic Cues",
            "url": "https://arxiv.org/abs/2604.24036"
          },
          {
            "title": "Zero-Shot Grounding of Objects from Natural Language Queries",
            "url": "https://arxiv.org/pdf/1908.07129"
          }
        ]
      },
      "I found the paper you're looking for. ProGAL-VLA (Prospective Grounding and Alignment VLA) addresses the issue that vision language action models often exhibit language ignorance by relying on visual shortcuts. The model constructs a 3D entity-centric graph (GSM), uses a slow planner to produce symbolic sub-goals, and aligns them with grounded entities via a Grounding Alignment Contrastive (GAC) loss.\n\nThe system uses a verification bottleneck that separates slow symbolic planning from fast control. All actions are conditioned on a verified goal embedding whose attention entropy provides an intrinsic ambiguity signal.\n\nOn LIBERO-Plus, ProGAL-VLA increases robustness under robot perturbations from 30.3 to 71.5 percent, reduces language ignorance by 3x-4x, and improves entity retrieval from 0.41 to 0.71 Recall@1. The paper (arXiv 2604.09824) was published on April 10, 2026."
    ],
    "durationSeconds": 6.057474657999992
  },
  "sourceToolAssistantUUID": "02861c5f-c956-4af6-ad58-b09c6b9006c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-18T20:35:22.767Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KoABtUbEPeixpbNVMTCjRT`</summary>

```json
{
  "query": "self-supervised affordance learning robot data gripper contact heuristic pseudo labels 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e79db049-277f-44de-afce-d94c89489d8c",
  "isSidechain": false,
  "requestId": "req_011CbAg5Bv1PzUnPSW6wNQyR",
  "type": "assistant",
  "uuid": "8fb4c1be-b90d-40d6-b9eb-4594c8a5a68f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CM7RwKHTVaSDh6s51bPZMV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 39851,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 39851,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-18T20:35:29.473Z_

<details><summary>↩ Tool result · `toolu_01KoABtUbEPeixpbNVMTCjRT`</summary>

```text
Web search results for query: "self-supervised affordance learning robot data gripper contact heuristic pseudo labels 2025 2026"

Links: [{"title":"Learning Labeled Robot Affordance Models by using Simulations and Crowdsourcing","url":"https://sim.ece.utexas.edu/static/papers/allevato_rss2020.pdf"},{"title":"GIFT: Generalizable Interaction-aware Functional Tool Affordances   without Labels","url":"https://arxiv.org/pdf/2106.14973"},{"title":"Learning Precise Affordances from Egocentric Videos for Robotic Manipulation","url":"https://arxiv.org/pdf/2408.10123"},{"title":"HRP: Human Affordances for Robotic Pre-Training","url":"https://arxiv.org/pdf/2407.18911"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://www.researchgate.net/publication/385560182_RT-Affordance_Affordances_are_Versatile_Intermediate_Representations_for_Robot_Manipulation"},{"title":"A Survey of Embodied Learning for Object-Centric Robotic Manipulation","url":"https://arxiv.org/html/2408.11537v1"},{"title":"Self-Assessment of Grasp Affordance Transfer","url":"https://arxiv.org/pdf/2007.02132"},{"title":"Accelerating Grasp Learning via Pretraining with Coarse Affordance Maps   of Objects","url":"https://arxiv.org/pdf/2205.05508"}]

Based on the search results, I found several relevant research papers on self-supervised affordance learning for robotics:

## Key Research Areas

**Self-Supervised Affordance Learning without Manual Labels:**

One approach achieves representation learning without human supervision by efficiently generating trajectories with a sampling-based method and recovering affordances from contact data.

**Contact-Based Affordance Learning:**

HRP (Human Affordances for Robotic Pre-Training) mines affordances including contact, hand pose, and object labels from human videos to improve self-supervised visual encoders. This addresses the challenge of learning from gripper interactions with objects.

**Interaction-Based Affordance Learning:**

Rather than relying on supervised learning from static data, affordance learning from interaction seeks to gather training data through simulations, allowing systems to learn from interactions and gain essential prior knowledge for real-world deployment.

**Grasp Affordance with Heuristics:**

Relations between grasp candidates and task outcomes are ranked by performance success with a heuristic confidence function to build a library of affordance task experiences.

**Self-Supervised Grasp Learning:**

Self-supervised grasp learning is one of the most promising approaches to human-like robotic grasp, though most existing methods are coarse-grained due to inadequate feedback on grasp quality.

The research shows active development in using pseudo-labels, contact feedback, and heuristic-based confidence metrics to enable robots to learn manipulation affordances with minimal manual annotation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fb4c1be-b90d-40d6-b9eb-4594c8a5a68f",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "c6590ea6-b360-48bc-a649-82bde09a749e",
  "toolUseResult": {
    "query": "self-supervised affordance learning robot data gripper contact heuristic pseudo labels 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014Cw43G6ftEvR93RFUJsV5W",
        "content": [
          {
            "title": "Learning Labeled Robot Affordance Models by using Simulations and Crowdsourcing",
            "url": "https://sim.ece.utexas.edu/static/papers/allevato_rss2020.pdf"
          },
          {
            "title": "GIFT: Generalizable Interaction-aware Functional Tool Affordances   without Labels",
            "url": "https://arxiv.org/pdf/2106.14973"
          },
          {
            "title": "Learning Precise Affordances from Egocentric Videos for Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2408.10123"
          },
          {
            "title": "HRP: Human Affordances for Robotic Pre-Training",
            "url": "https://arxiv.org/pdf/2407.18911"
          },
          {
            "title": "RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation",
            "url": "https://www.researchgate.net/publication/385560182_RT-Affordance_Affordances_are_Versatile_Intermediate_Representations_for_Robot_Manipulation"
          },
          {
            "title": "A Survey of Embodied Learning for Object-Centric Robotic Manipulation",
            "url": "https://arxiv.org/html/2408.11537v1"
          },
          {
            "title": "Self-Assessment of Grasp Affordance Transfer",
            "url": "https://arxiv.org/pdf/2007.02132"
          },
          {
            "title": "Accelerating Grasp Learning via Pretraining with Coarse Affordance Maps   of Objects",
            "url": "https://arxiv.org/pdf/2205.05508"
          }
        ]
      },
      "Based on the search results, I found several relevant research papers on self-supervised affordance learning for robotics:\n\n## Key Research Areas\n\n**Self-Supervised Affordance Learning without Manual Labels:**\n\nOne approach achieves representation learning without human supervision by efficiently generating trajectories with a sampling-based method and recovering affordances from contact data.\n\n**Contact-Based Affordance Learning:**\n\nHRP (Human Affordances for Robotic Pre-Training) mines affordances including contact, hand pose, and object labels from human videos to improve self-supervised visual encoders. This addresses the challenge of learning from gripper interactions with objects.\n\n**Interaction-Based Affordance Learning:**\n\nRather than relying on supervised learning from static data, affordance learning from interaction seeks to gather training data through simulations, allowing systems to learn from interactions and gain essential prior knowledge for real-world deployment.\n\n**Grasp Affordance with Heuristics:**\n\nRelations between grasp candidates and task outcomes are ranked by performance success with a heuristic confidence function to build a library of affordance task experiences.\n\n**Self-Supervised Grasp Learning:**\n\nSelf-supervised grasp learning is one of the most promising approaches to human-like robotic grasp, though most existing methods are coarse-grained due to inadequate feedback on grasp quality.\n\nThe research shows active development in using pseudo-labels, contact feedback, and heuristic-based confidence metrics to enable robots to learn manipulation affordances with minimal manual annotation."
    ],
    "durationSeconds": 6.700497177000012
  },
  "sourceToolAssistantUUID": "8fb4c1be-b90d-40d6-b9eb-4594c8a5a68f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-18T20:35:32.605Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Rd3cgs8pKrSNkdXrU21sa`</summary>

```json
{
  "query": "A100 H100 conversion ratio transformer fine-tuning mixed precision actual benchmark comparison 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6590ea6-b360-48bc-a649-82bde09a749e",
  "isSidechain": false,
  "requestId": "req_011CbAg61L3jUFow5UtdEcpE",
  "type": "assistant",
  "uuid": "fcc5f459-4555-4f94-aaa1-b77cadccf99f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144mqjty2zs4XUuSRWtxEys",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 40530,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 821,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 40530,
          "cache_creation_input_tokens": 821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 821
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-18T20:35:41.327Z_

<details><summary>↩ Tool result · `toolu_018Rd3cgs8pKrSNkdXrU21sa`</summary>

```text
Web search results for query: "A100 H100 conversion ratio transformer fine-tuning mixed precision actual benchmark comparison 2025"

Links: [{"title":"Comparing NVIDIA H100 vs A100 GPUs for AI Workloads | OpenMetal IaaS","url":"https://openmetal.io/resources/blog/nvidia-h100-vs-a100-gpu-comparison/"},{"title":"NVIDIA A100 vs H100 vs H200: GPU Comparison for AI | E2E Networks","url":"https://www.e2enetworks.com/blog/nvidia-a100-vs-h100-vs-h200-gpu-comparison"},{"title":"NVIDIA GPU benchmark: H100 vs A100 vs L40S","url":"https://www.cudocompute.com/blog/real-world-gpu-benchmarks"},{"title":"NVIDIA GPUs: H100 vs. A100 | a detailed comparison | Gcore","url":"https://gcore.com/blog/nvidia-h100-a100"},{"title":"Nvidia H100 GPU: Specs, VRAM, Price, and AI Performance","url":"https://www.runpod.io/articles/guides/nvidia-h100"},{"title":"NVIDIA A100 vs H100: AI Training, HPC, and Next-Gen Performance","url":"https://www.databasemart.com/blog/a100-vs-h100"},{"title":"H100 80GB vs A100 80GB Fine-Tuning: Performance Guide | Lyceum Technology","url":"https://lyceum.technology/magazine/h100-80gb-vs-a100-80gb-fine-tuning/"},{"title":"NVIDIA A100 vs H100: INT4, FP8, BF16 & AI Performance Comparison (2026)","url":"https://www.bestgpusforai.com/gpu-comparison/a100-vs-h100"}]

Based on the search results, here are the key benchmarks comparing A100 and H100 GPUs for transformer fine-tuning with mixed precision:

## Training Speed Improvements

The H100 provides up to 2.4 times faster training throughput compared to the A100 when using mixed precision. However, other benchmarks report higher performance gains—NVIDIA reports up to 4x faster training for GPT-3 class models compared to A100, while the H100 delivers up to 6x faster training of models like GPT-style transformers compared to the A100 using dynamic precision adjustment.

## Mixed Precision Performance

H100 delivers ~1,000 TFLOPS for mixed-precision AI training (FP16/BF16) vs. A100's 312 TFLOPS, enabling 3×+ faster deep learning workloads, especially in large-scale model training. For fine-tuning specifically, using FP8 on an H100 can lead to a 2x to 4x speedup over BF16 on an A100.

## Actual Benchmark Results

A practical benchmark shows that H100's 4th-gen tensor cores, plus 3.36 TB/s memory bandwidth, deliver a 2.15× throughput edge over the A100 and a 23% lower cost-per-token, despite the higher hourly rate. This was measured using an end-to-end BERT-base fine-tuning workload.

## Key Technical Advantage

The Hopper architecture introduces the Transformer Engine, which is designed to accelerate deep learning operations using mixed precision formats, especially FP8, and plays a key role in accelerating both training and inference workloads.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcc5f459-4555-4f94-aaa1-b77cadccf99f",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "d0860294-0baa-48e0-bd6c-59ef90a936f2",
  "toolUseResult": {
    "query": "A100 H100 conversion ratio transformer fine-tuning mixed precision actual benchmark comparison 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KCCTHT4W4AKnDXxCnb3zCd",
        "content": [
          {
            "title": "Comparing NVIDIA H100 vs A100 GPUs for AI Workloads | OpenMetal IaaS",
            "url": "https://openmetal.io/resources/blog/nvidia-h100-vs-a100-gpu-comparison/"
          },
          {
            "title": "NVIDIA A100 vs H100 vs H200: GPU Comparison for AI | E2E Networks",
            "url": "https://www.e2enetworks.com/blog/nvidia-a100-vs-h100-vs-h200-gpu-comparison"
          },
          {
            "title": "NVIDIA GPU benchmark: H100 vs A100 vs L40S",
            "url": "https://www.cudocompute.com/blog/real-world-gpu-benchmarks"
          },
          {
            "title": "NVIDIA GPUs: H100 vs. A100 | a detailed comparison | Gcore",
            "url": "https://gcore.com/blog/nvidia-h100-a100"
          },
          {
            "title": "Nvidia H100 GPU: Specs, VRAM, Price, and AI Performance",
            "url": "https://www.runpod.io/articles/guides/nvidia-h100"
          },
          {
            "title": "NVIDIA A100 vs H100: AI Training, HPC, and Next-Gen Performance",
            "url": "https://www.databasemart.com/blog/a100-vs-h100"
          },
          {
            "title": "H100 80GB vs A100 80GB Fine-Tuning: Performance Guide | Lyceum Technology",
            "url": "https://lyceum.technology/magazine/h100-80gb-vs-a100-80gb-fine-tuning/"
          },
          {
            "title": "NVIDIA A100 vs H100: INT4, FP8, BF16 & AI Performance Comparison (2026)",
            "url": "https://www.bestgpusforai.com/gpu-comparison/a100-vs-h100"
          }
        ]
      },
      "Based on the search results, here are the key benchmarks comparing A100 and H100 GPUs for transformer fine-tuning with mixed precision:\n\n## Training Speed Improvements\n\nThe H100 provides up to 2.4 times faster training throughput compared to the A100 when using mixed precision. However, other benchmarks report higher performance gains—NVIDIA reports up to 4x faster training for GPT-3 class models compared to A100, while the H100 delivers up to 6x faster training of models like GPT-style transformers compared to the A100 using dynamic precision adjustment.\n\n## Mixed Precision Performance\n\nH100 delivers ~1,000 TFLOPS for mixed-precision AI training (FP16/BF16) vs. A100's 312 TFLOPS, enabling 3×+ faster deep learning workloads, especially in large-scale model training. For fine-tuning specifically, using FP8 on an H100 can lead to a 2x to 4x speedup over BF16 on an A100.\n\n## Actual Benchmark Results\n\nA practical benchmark shows that H100's 4th-gen tensor cores, plus 3.36 TB/s memory bandwidth, deliver a 2.15× throughput edge over the A100 and a 23% lower cost-per-token, despite the higher hourly rate. This was measured using an end-to-end BERT-base fine-tuning workload.\n\n## Key Technical Advantage\n\nThe Hopper architecture introduces the Transformer Engine, which is designed to accelerate deep learning operations using mixed precision formats, especially FP8, and plays a key role in accelerating both training and inference workloads."
    ],
    "durationSeconds": 8.718015475000023
  },
  "sourceToolAssistantUUID": "fcc5f459-4555-4f94-aaa1-b77cadccf99f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-18T20:37:11.198Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now gather my research findings and think deeply about the revisions needed.

Key findings from research:

1. **GuidedVLA (arXiv 2605.12369)**: Builds on π₀, supervises individual attention heads for 3 factors (object grounding, spatial geometry, temporal skill logic). Results: 75.4% on LIBERO-Plus (vs 68.2% π₀ baseline), 90.63% on RoboTwin 2.0. Does NOT do consistency objectives, does NOT do cross-category transfer, does NOT use affordance heatmaps. Uses predefined factor types, not open-vocabulary. 

2. **BusyBox (arXiv 2602.05441)**: Physical benchmark with 6 modules testing affordance generalization across variants—even π₀.₅ and GR00T-N1.6 struggle with it. Since it requires actual hardware, it's more of a supplementary reference than a primary comparison point.

3. **ProGAL-VLA (arXiv 2604.09824)**: Another language grounding approach using 3D entity-centric graphs and symbolic sub-goals with verification, achieving 71.5% on LIBERO—

relevant concurrent work that addresses robustness and should be in the landscape.

For the A100→H100 performance ratio, real benchmarks show 1.5-2.4x depending on the workload, and for transformer fine-tuning with mixed precision around 2.15x is reasonable, though 1.5x is more conservative. I'll use 1.5x as the baseline but note the range.

The core idea still holds up despite the crowded landscape—GuidedVLA and ProGAL-VLA both tackle language grounding, but LACVLA's specific combination of affordance-gated bottleneck with stop-gradient, consistency objectives on spatial heatmaps, and cross-category zero-shot transfer focus remains distinct.

I shouldn't pivot since the reviewer says the proposal has improved dramatically and the gap is narrower than before, and pivoting would waste the refinement work. The revision scope is manageable: adding GuidedVLA and ProGAL-VLA to the landscape, incorporating BusyBox into evaluation, trimming ablations, strengthening the HOVA-500K fallback with a self-supervised alternative, reframing the narrative opening, and fixing the compute budget to stay within 200 H100-hours. These are solid improvements that don't require a major overhaul.

For the narrative reframing, I should lead with cross-category zero-shot transfer as the core contribution, then explain why the language-ignoring problem makes this particularly challenging—this positions LACVLA in a less crowded space. When differentiating from GuidedVLA, the key distinctions are that GuidedVLA uses predefined factor types with supervised attention heads and no cross-category transfer, while LACVLA generates open-vocabulary affordance heatmaps through cross-attention, applies a stop-gradient bottleneck, uses self-supervised consistency objectives, and explicitly targets cross-category zero-shot transfer. I need to add ProGAL-VLA to the landscape comparison as well.

For the ablations, the reviewer's suggestion makes sense—I can merge the bottleneck-related ablations by tracking affordance map quality across conditions: one without the bottleneck entirely, and one with the bottleneck but no consistency objectives. This gives me the comparison I need without redundancy. I'll also drop the phased versus non-phased training detail since that's just an implementation choice.

So my revised ablation suite becomes six variants: the full LACVLA system, a version without the affordance bottleneck, modular composition with frozen GLOVER++, Shin-style augmentation using paraphrases without consistency loss, IPAC applied directly to raw actions, and ST4VLA-style spatial grounding with IPAC on features. Let me make sure the bottleneck ablation is structured correctly—I need one experiment that tests both the no-bottleneck condition and the bottleneck-without-consistency condition so I can isolate what the consistency objectives actually contribute.

With this streamlined setup of six ablations at 15-20 hours each on A100, I'm looking at roughly 90-120 hours total compute.

Let me recalculate the full budget more carefully. The HOVA pre-training takes about 25 hours, the main LACVLA training run is 35-50 hours, and then I have five additional ablation variants at 15-20 hours each for another 75-100 hours. But I realize the ablations and full training runs aren't separate — the ablations are actually variants of the training runs themselves, so many of them can skip certain expensive steps. I should restructure this to avoid double-counting the overlapping work.

So the real breakdown is: HOVA pre-training around 25 hours, the main result around 35-50 hours, five ablation variants at 15-20 hours each since they skip pre-training, cross-category evaluation sweeps around 25 hours, and AGNOSTOS plus BusyBox setup around 15 hours. That puts me at roughly 175-215 hours on A100, which translates to about 117-143 hours on H100 at a 1.5x ratio, or 135-165 hours at a more conservative 1.3x ratio.

The reviewer mentioned that 1.5x is optimistic for mixed-precision transformer fine-tuning and suggested 1.3x is more conservative, but I'm seeing real benchmarks showing 2.15x for BERT fine-tuning, so 1.5x is actually quite conservative. Still, since the reviewer raised this concern, I should acknowledge it and use a conservative range. I'll go with 1.4x as my central estimate with a 1.3-1.5x range to be safe.

That gives me 125-154 hours on H100 at the central estimate and 135-165 hours at the conservative end, both comfortably under the 200-hour limit. The key to staying within budget is the ablation reduction strategy.

For the fallback plan, I'm adding self-supervised affordance readout initialization using gripper position data from robot trajectories to generate pseudo-affordance Gaussian heatmaps. If the HOVA-500K domain gap diagnostic fails, I can fall back to this approach, and I'll ablate both strategies to determine whether HOVA-500K pre-training is actually necessary.

I'll also add BusyBox as a supplementary evaluation.

Now, thinking about the stagnation concern — the scores have plateaued around 3.5-3.8, and I need to figure out what pushes this to 4.0 or higher. The reviewer's feedback is actually quite positive: "improved dramatically," "technically comprehensive," "gap is narrower." All five issues are solvable, and I think executing them cleanly, especially the narrative reframing, could get me over the threshold.

The narrative reframing is strategically important because the current framing about VLAs ignoring language is already being used by LIBERO-Plus, LangGap, LIBERO-Para, and other recent work. I need to differentiate the story.

The cross-category zero-shot transfer angle is much less saturated — A0, AffordDP, RAM, AGNOSTOS, and VLA² are the main players, and none of them combine language-conditioned affordance consistency with architectural bottlenecks the way I'm proposing.

I should probably add ProGAL-VLA to the related work since it uses a verified grounding bottleneck, which is conceptually adjacent to my stop-gradient bottleneck, even though the underlying approaches are quite different.

This is a minor revision — everything stays within the existing framework, no fundamental restructuring needed. But let me think through this once more before committing.

The reviewer feedback is actually pretty encouraging — scores are creeping up from 3.5 to 3.8 over the last three rounds, and they note the gap is narrowing. A clean, well-executed minor revision that addresses all five points should be the right move rather than risking a major overhaul that could destabilize what's already working.

Now I'll put together the full revised JSON with these specific changes: reframing the core problem and opportunity around cross-category transfer, adding GuidedVLA and ProGAL-VLA to the landscape, including BusyBox in the evaluation, cutting ablations from eight down to six, recalculating compute to stay under 200 hours on H100, adding a self-supervised affordance fallback for HOVA-500K, and refreshing the key references.

For the narrative, I'm leading with cross-category zero-shot transfer as the central problem, then explaining why ignoring language signals becomes particularly damaging in that context. The affordance-gating mechanism shifts from being primarily a language grounding solution to a bottleneck fix for cross-category generalization. I'm also merging a couple of ablation experiments and dropping the phased training one to get down to six total, which should fit within 90-120 hours on A100.

Now I'm recalculating the compute budget more carefully. The pre-training phase comes in around 20 hours, the main LACVLA training with LoRA takes 35-45 hours, and the five ablation variants run 12-18 hours each for 60-90 hours total. Adding cross-category evaluation and BusyBox setup brings me to roughly 145 hours on A100, which translates to about 120-190 hours on H100 using a conservative conversion ratio.

Converting to H100 at different efficiency ratios gives me 104-142 hours depending on assumptions, comfortably under the 200-hour budget. I'll apply the same scaling to the other experiment estimates and then structure everything in the JSON format. For BusyBox specifically, since it's a physical benchmark and the paper provides CAD files for 3D printing, I should frame it as supplementary physical evaluation if the lab has access to the hardware or can build it, otherwise focusing on simulation-based cross-category benchmarks.

Now I'm finalizing the approach and writing out the revised idea with key framing changes: leading with cross-category zero-shot transfer in the core problem, repositioning the opportunity in a less crowded space, and opening the description with that same transfer focus. I'm also adding the recent landscape works like GuidedVLA and ProGAL-VLA from 2026, plus the BusyBox benchmark, then structuring the full JSON output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0860294-0baa-48e0-bd6c-59ef90a936f2",
  "isSidechain": false,
  "requestId": "req_011CbAg6sv69dZYwH77HJuQv",
  "type": "assistant",
  "uuid": "02fb1a0d-c15c-4224-bf8b-3ef4eb1bd12b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gq9T1JB9hEr8Unp8zQuXNE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 41351,
      "output_tokens": 3937,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 943,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3937,
          "cache_read_input_tokens": 41351,
          "cache_creation_input_tokens": 943,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 943
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-18T20:37:11.461Z_

Now let me search for one more area to be thorough — any very recent work on the self-supervised affordance initialization strategy that the reviewer suggests as a fallback.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02fb1a0d-c15c-4224-bf8b-3ef4eb1bd12b",
  "isSidechain": false,
  "requestId": "req_011CbAg6sv69dZYwH77HJuQv",
  "type": "assistant",
  "uuid": "c167888b-dd8d-418d-8d03-2b6db8dfd4be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gq9T1JB9hEr8Unp8zQuXNE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 41351,
      "output_tokens": 3937,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 943,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3937,
          "cache_read_input_tokens": 41351,
          "cache_creation_input_tokens": 943,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 943
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-18T20:37:12.003Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T8NPnNbM8ULWtTkFjDcDBx`</summary>

```json
{
  "query": "robot trajectory gripper contact point affordance pseudo label self-supervised heatmap generation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c167888b-dd8d-418d-8d03-2b6db8dfd4be",
  "isSidechain": false,
  "requestId": "req_011CbAg6sv69dZYwH77HJuQv",
  "type": "assistant",
  "uuid": "6e4bbe3b-8f0e-4508-9d87-0dc31ad8ebfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gq9T1JB9hEr8Unp8zQuXNE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 943,
      "cache_read_input_tokens": 41351,
      "output_tokens": 3937,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 943,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3937,
          "cache_read_input_tokens": 41351,
          "cache_creation_input_tokens": 943,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 943
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-18 (UTC).**  ## Original idea {   \"title\": \"LACVLA: Enforcing Language-Affordance Grounding via Consistency Object…",
  "leafUuid": "6e4bbe3b-8f0e-4508-9d87-0dc31ad8ebfc",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise LACVLA affordance consistency for cross-category transfer",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Tool result

_source line 55 · 2026-05-18T20:37:24.916Z_

<details><summary>↩ Tool result · `toolu_01T8NPnNbM8ULWtTkFjDcDBx`</summary>

```text
Web search results for query: "robot trajectory gripper contact point affordance pseudo label self-supervised heatmap generation 2025 2026"

Links: [{"title":"Learning Precise Affordances from Egocentric Videos for Robotic Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Learning_Precise_Affordances_from_Egocentric_Videos_for_Robotic_Manipulation_ICCV_2025_paper.pdf"},{"title":"Text-driven Affordance Learning from Egocentric Vision","url":"https://arxiv.org/pdf/2404.02523"},{"title":"GIFT: Generalizable Interaction-aware Functional Tool Affordances   without Labels","url":"https://arxiv.org/pdf/2106.14973"},{"title":"Enhancing task-oriented robotic grasping via 3D affordance grounding from vision-language models | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02169-0"},{"title":"Learning Precise Affordances from Egocentric Videos for Robotic Manipulation","url":"https://arxiv.org/pdf/2408.10123"},{"title":"Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024","url":"https://www.roboticsproceedings.org/rss20/p046.pdf"},{"title":"Accelerating Grasp Learning via Pretraining with Coarse Affordance Maps   of Objects","url":"https://arxiv.org/pdf/2205.05508"}]

I found several highly relevant papers on robot affordance learning, gripper contact points, and related techniques from 2025-2026 and recent years:

## Key Research Findings

**Precise Affordance Learning from Egocentric Videos (ICCV 2025)**

Recent work has introduced improved affordance data collection pipelines that localize both graspable and functional points, utilizing SAM to produce high-quality annotations. These methods cover both graspable affordances (e.g., object handles) and functional affordances (e.g., knife blades, hammer heads) and extract data with precise segmentation masks, addressing the limitation that affordances predicted as coarse heatmaps are less accurate when applied in the real world.

**Text-Driven Affordance Learning with Pseudo Labels**

Research has proposed pseudo dataset creation pipelines to build large pseudo-training datasets consisting of contact points, trajectories, images, and text tuples. Contact points are represented as heatmaps in weakly-supervised learning approaches.

**Self-Supervised Trajectory-Based Affordance Learning**

Methods can generate trajectories efficiently using sampling-based approaches and recover affordances from contact data, achieving representation learning without human supervision. Some approaches ground affordance representation on the contacts between objects.

**3D Affordance Heatmaps for Robotic Grasping**

Recent systems can infer 3D affordance heatmaps based on language instructions to identify semantically relevant interaction regions for task-oriented grasping with grippers.

These papers represent the latest developments in self-supervised and weakly-supervised affordance learning for robotic manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e4bbe3b-8f0e-4508-9d87-0dc31ad8ebfc",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "29e01c03-808b-4392-b74c-22b2d839020d",
  "toolUseResult": {
    "query": "robot trajectory gripper contact point affordance pseudo label self-supervised heatmap generation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CRKVww1UjjLhNpVe4sDwkf",
        "content": [
          {
            "title": "Learning Precise Affordances from Egocentric Videos for Robotic Manipulation",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Li_Learning_Precise_Affordances_from_Egocentric_Videos_for_Robotic_Manipulation_ICCV_2025_paper.pdf"
          },
          {
            "title": "Text-driven Affordance Learning from Egocentric Vision",
            "url": "https://arxiv.org/pdf/2404.02523"
          },
          {
            "title": "GIFT: Generalizable Interaction-aware Functional Tool Affordances   without Labels",
            "url": "https://arxiv.org/pdf/2106.14973"
          },
          {
            "title": "Enhancing task-oriented robotic grasping via 3D affordance grounding from vision-language models | Complex & Intelligent Systems | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s40747-025-02169-0"
          },
          {
            "title": "Learning Precise Affordances from Egocentric Videos for Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2408.10123"
          },
          {
            "title": "Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024",
            "url": "https://www.roboticsproceedings.org/rss20/p046.pdf"
          },
          {
            "title": "Accelerating Grasp Learning via Pretraining with Coarse Affordance Maps   of Objects",
            "url": "https://arxiv.org/pdf/2205.05508"
          }
        ]
      },
      "I found several highly relevant papers on robot affordance learning, gripper contact points, and related techniques from 2025-2026 and recent years:\n\n## Key Research Findings\n\n**Precise Affordance Learning from Egocentric Videos (ICCV 2025)**\n\nRecent work has introduced improved affordance data collection pipelines that localize both graspable and functional points, utilizing SAM to produce high-quality annotations. These methods cover both graspable affordances (e.g., object handles) and functional affordances (e.g., knife blades, hammer heads) and extract data with precise segmentation masks, addressing the limitation that affordances predicted as coarse heatmaps are less accurate when applied in the real world.\n\n**Text-Driven Affordance Learning with Pseudo Labels**\n\nResearch has proposed pseudo dataset creation pipelines to build large pseudo-training datasets consisting of contact points, trajectories, images, and text tuples. Contact points are represented as heatmaps in weakly-supervised learning approaches.\n\n**Self-Supervised Trajectory-Based Affordance Learning**\n\nMethods can generate trajectories efficiently using sampling-based approaches and recover affordances from contact data, achieving representation learning without human supervision. Some approaches ground affordance representation on the contacts between objects.\n\n**3D Affordance Heatmaps for Robotic Grasping**\n\nRecent systems can infer 3D affordance heatmaps based on language instructions to identify semantically relevant interaction regions for task-oriented grasping with grippers.\n\nThese papers represent the latest developments in self-supervised and weakly-supervised affordance learning for robotic manipulation."
    ],
    "durationSeconds": 12.906402906000032
  },
  "sourceToolAssistantUUID": "6e4bbe3b-8f0e-4508-9d87-0dc31ad8ebfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56 · 2026-05-18T20:37:24.923Z_

```json
{
  "parentUuid": "29e01c03-808b-4392-b74c-22b2d839020d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fff344a5-299a-4308-b2c9-465b25d7dbe5",
  "timestamp": "2026-05-18T20:37:24.923Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 57 · 2026-05-18T20:37:28.081Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0156nKAX9ZKuTzWsoxDgtx7c`</summary>

```json
{
  "query": "BusyBox benchmark VLA pi0.5 GR00T success rate quantitative results affordance generalization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fff344a5-299a-4308-b2c9-465b25d7dbe5",
  "isSidechain": false,
  "requestId": "req_011CbAgEWoZkg3JNmnihRPJZ",
  "type": "assistant",
  "uuid": "38fd37a7-2fde-4427-b09d-98adcdf681d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RFWC968Hs2s8PXnfxerphC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4830,
      "cache_read_input_tokens": 42294,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4830,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 42294,
          "cache_creation_input_tokens": 4830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4830
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-18T20:37:34.553Z_

<details><summary>↩ Tool result · `toolu_0156nKAX9ZKuTzWsoxDgtx7c`</summary>

```text
Web search results for query: "BusyBox benchmark VLA pi0.5 GR00T success rate quantitative results affordance generalization 2026"

Links: [{"title":"[2602.05441] Benchmarking Affordance Generalization with BusyBox","url":"https://arxiv.org/abs/2602.05441"},{"title":"Benchmarking Affordance Generalization with BusyBox","url":"https://arxiv.org/pdf/2602.05441"},{"title":"Benchmarking Affordance Generalization with BusyBox","url":"https://arxiv.org/html/2602.05441"},{"title":"Benchmarking Affordance Generalization with BusyBox","url":"https://microsoft.github.io/BusyBox/"},{"title":"2026-01-28 Work in progress.","url":"https://arxiv.org/pdf/2601.15197"},{"title":"REALM: A Real-to-Sim Validated Benchmark for Generalization in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.19562"}]

Based on the search results, I found relevant information about the BusyBox benchmark with VLA models π0.5 and GR00T.

BusyBox is a physical benchmark for systematic semi-automatic evaluation of VLAs' affordance generalization, consisting of 6 modules with switches, sliders, wires, buttons, a display, and a dial that can be swapped and rotated to create multiple variations with different visual appearances but the same set of affordances.

Generalization across BusyBox variants is highly challenging even for strong open-weights VLAs such as π₀.₅ and GR00T-N1.6. More specifically, π₀.₅'s and GR00T-N1.6's performance degraded even more severely in semi- and fully shuffled BusyBox configurations, despite both having the same set of affordances as the canonical one.

Basic affordance generalization is a major area for improvement even for the strongest existing VLAs, and BusyBox as a benchmark is far from saturation. The research demonstrates that affordance generalization is a challenge even for some of the strongest existing VLAs and even in in-distribution settings, because it can require out-of distribution generalization in the visual space.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38fd37a7-2fde-4427-b09d-98adcdf681d0",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "42d94c35-6ae9-4618-86e7-2be0049a160d",
  "toolUseResult": {
    "query": "BusyBox benchmark VLA pi0.5 GR00T success rate quantitative results affordance generalization 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D91QFghvAXybnZn6hYmqbA",
        "content": [
          {
            "title": "[2602.05441] Benchmarking Affordance Generalization with BusyBox",
            "url": "https://arxiv.org/abs/2602.05441"
          },
          {
            "title": "Benchmarking Affordance Generalization with BusyBox",
            "url": "https://arxiv.org/pdf/2602.05441"
          },
          {
            "title": "Benchmarking Affordance Generalization with BusyBox",
            "url": "https://arxiv.org/html/2602.05441"
          },
          {
            "title": "Benchmarking Affordance Generalization with BusyBox",
            "url": "https://microsoft.github.io/BusyBox/"
          },
          {
            "title": "2026-01-28 Work in progress.",
            "url": "https://arxiv.org/pdf/2601.15197"
          },
          {
            "title": "REALM: A Real-to-Sim Validated Benchmark for Generalization in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.19562"
          }
        ]
      },
      "Based on the search results, I found relevant information about the BusyBox benchmark with VLA models π0.5 and GR00T.\n\nBusyBox is a physical benchmark for systematic semi-automatic evaluation of VLAs' affordance generalization, consisting of 6 modules with switches, sliders, wires, buttons, a display, and a dial that can be swapped and rotated to create multiple variations with different visual appearances but the same set of affordances.\n\nGeneralization across BusyBox variants is highly challenging even for strong open-weights VLAs such as π₀.₅ and GR00T-N1.6. More specifically, π₀.₅'s and GR00T-N1.6's performance degraded even more severely in semi- and fully shuffled BusyBox configurations, despite both having the same set of affordances as the canonical one.\n\nBasic affordance generalization is a major area for improvement even for the strongest existing VLAs, and BusyBox as a benchmark is far from saturation. The research demonstrates that affordance generalization is a challenge even for some of the strongest existing VLAs and even in in-distribution settings, because it can require out-of distribution generalization in the visual space."
    ],
    "durationSeconds": 6.465646189999999
  },
  "sourceToolAssistantUUID": "38fd37a7-2fde-4427-b09d-98adcdf681d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-18T20:37:38.982Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ChYeTzipoiiFdpys45aow9`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.05441",
  "prompt": "Extract the specific quantitative results: What are the exact success rates for π₀.₅ and GR00T-N1.6 on different BusyBox configurations (canonical, semi-shuffled, fully shuffled)? What specific tasks do they test? How many trials per condition? What is the performance drop from canonical to shuffled? Be as specific with numbers as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42d94c35-6ae9-4618-86e7-2be0049a160d",
  "isSidechain": false,
  "requestId": "req_011CbAgFDxZoKjavwCDx8mgE",
  "type": "assistant",
  "uuid": "cab0d366-0c91-4849-a852-b6ce64a67c4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KH3nTTNzL1k2uasDvjHkN4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 661,
      "cache_read_input_tokens": 47124,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 661,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 47124,
          "cache_creation_input_tokens": 661,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 661
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T20:37:44.666Z_

<details><summary>↩ Tool result · `toolu_01ChYeTzipoiiFdpys45aow9`</summary>

```text
# BusyBox Affordance Generalization Results

The paper presents experimental results but **does not provide exact numerical success rates** in the text. Instead, the findings are visualized in Figure 5, which shows bar charts for three configurations.

## Key Quantitative Details:

**Test Protocol:**
- "60 task instructions" evaluated across three BusyBox configurations
- "10 task instructions from moving BusyBox, moving sliders, pulling wires, pushing buttons, turning the knob, and flipping switches" affordance categories
- 30-second time limit per episode
- No explicit trial count per condition stated in the text

**Task Categories Tested:**
The paper evaluated 6 affordance categories: pushing buttons, moving sliders, turning the knob, flipping switches, pulling wires, and moving BusyBox itself.

**Key Findings:**
The researchers report that "both π₀.₅ and GR00T-N1.6 finetuned on the data from the canonical BusyBox have difficulties on the visually out-of-distribution BusyBox tasks" and that "on the fully shuffled configuration, π₀.₅'s and GR00T-N1.6's performance degraded even more severely."

However, the specific numerical performance drops are only visible in Figure 5's bar charts, not provided as exact percentages in the paper's text. The authors conclude that "affordance generalization is a challenge even for some of the strongest existing VLAs."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cab0d366-0c91-4849-a852-b6ce64a67c4b",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "ac6aa58d-2697-4d0b-8bf8-ff74593215fd",
  "toolUseResult": {
    "bytes": 130286,
    "code": 200,
    "codeText": "OK",
    "result": "# BusyBox Affordance Generalization Results\n\nThe paper presents experimental results but **does not provide exact numerical success rates** in the text. Instead, the findings are visualized in Figure 5, which shows bar charts for three configurations.\n\n## Key Quantitative Details:\n\n**Test Protocol:**\n- \"60 task instructions\" evaluated across three BusyBox configurations\n- \"10 task instructions from moving BusyBox, moving sliders, pulling wires, pushing buttons, turning the knob, and flipping switches\" affordance categories\n- 30-second time limit per episode\n- No explicit trial count per condition stated in the text\n\n**Task Categories Tested:**\nThe paper evaluated 6 affordance categories: pushing buttons, moving sliders, turning the knob, flipping switches, pulling wires, and moving BusyBox itself.\n\n**Key Findings:**\nThe researchers report that \"both π₀.₅ and GR00T-N1.6 finetuned on the data from the canonical BusyBox have difficulties on the visually out-of-distribution BusyBox tasks\" and that \"on the fully shuffled configuration, π₀.₅'s and GR00T-N1.6's performance degraded even more severely.\"\n\nHowever, the specific numerical performance drops are only visible in Figure 5's bar charts, not provided as exact percentages in the paper's text. The authors conclude that \"affordance generalization is a challenge even for some of the strongest existing VLAs.\"",
    "durationMs": 5678,
    "url": "https://arxiv.org/html/2602.05441"
  },
  "sourceToolAssistantUUID": "cab0d366-0c91-4849-a852-b6ce64a67c4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-18T20:37:47.750Z_

Good, I have enough research now. Let me synthesize everything and write the revised idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac6aa58d-2697-4d0b-8bf8-ff74593215fd",
  "isSidechain": false,
  "requestId": "req_011CbAgFyDadYnW69wfW14Ba",
  "type": "assistant",
  "uuid": "b2e5ed13-6c8d-40ad-a4fc-b7b8bbe5bf0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hi3HHpdi9D8gheQK1nhxT7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 47785,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 47785,
          "cache_creation_input_tokens": 515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 515
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-18T20:37:47.877Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VuhnCDM1Hueuw83QUJK2fD`</summary>

```json
{
  "query": "AAAI 2027 submission deadline abstract paper July 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2e5ed13-6c8d-40ad-a4fc-b7b8bbe5bf0b",
  "isSidechain": false,
  "requestId": "req_011CbAgFyDadYnW69wfW14Ba",
  "type": "assistant",
  "uuid": "99d5694a-a020-476e-89bf-d42bb1b5be0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hi3HHpdi9D8gheQK1nhxT7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 47785,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 515,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 47785,
          "cache_creation_input_tokens": 515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 515
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-18T20:37:57.051Z_

<details><summary>↩ Tool result · `toolu_01VuhnCDM1Hueuw83QUJK2fD`</summary>

```text
Web search results for query: "AAAI 2027 submission deadline abstract paper July 2026"

Links: [{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI-27 - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/"},{"title":"AAAI-26 Submission Instructions - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/submission-instructions/"},{"title":"The 40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"AI/ML Conference Timeline | NIU AI","url":"https://www.niuai.org/resources/conference-timeline/"},{"title":"AAAI-27 Main Technical Track - AAAI","url":"https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"AI Deadlines – AI Conference Call For Paper Deadlines","url":"http://aideadlines.org/"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"}]

Based on the search results, here are the submission deadlines for AAAI 2027:

The abstract submission deadline for AAAI 2027 is July 21, 2026 at 11:59 PM UTC-12, and the full paper submission deadline is July 28, 2026 at 11:59 PM UTC-12. Supplementary material and code are due by July 31, 2026 at 11:59 PM UTC-12.

The Forty-First AAAI Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Canada, from February 16 to February 23, 2027.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99d5694a-a020-476e-89bf-d42bb1b5be0a",
  "isSidechain": false,
  "promptId": "b3441386-2847-4d9e-8e6b-f7c0469bd008",
  "type": "user",
  "uuid": "b218d5a8-7bd6-413f-925b-54cd56119e49",
  "toolUseResult": {
    "query": "AAAI 2027 submission deadline abstract paper July 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FGZFSXq479F9iptFss5AsA",
        "content": [
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "AAAI-27 - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-27/"
          },
          {
            "title": "AAAI-26 Submission Instructions - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/submission-instructions/"
          },
          {
            "title": "The 40th Annual AAAI Conference on Artificial Intelligence",
            "url": "https://aaai.org/conference/aaai/aaai-26/"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "AI/ML Conference Timeline | NIU AI",
            "url": "https://www.niuai.org/resources/conference-timeline/"
          },
          {
            "title": "AAAI-27 Main Technical Track - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-27/call/main-technical-track/"
          },
          {
            "title": "AAAI 2027 Conference Deadline | Live Countdown Tracker",
            "url": "https://www.getpaperpilot.com/deadlines/aaai-2027.html"
          },
          {
            "title": "AI Deadlines – AI Conference Call For Paper Deadlines",
            "url": "http://aideadlines.org/"
          },
          {
            "title": "Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"
          }
        ]
      },
      "Based on the search results, here are the submission deadlines for AAAI 2027:\n\nThe abstract submission deadline for AAAI 2027 is July 21, 2026 at 11:59 PM UTC-12, and the full paper submission deadline is July 28, 2026 at 11:59 PM UTC-12. Supplementary material and code are due by July 31, 2026 at 11:59 PM UTC-12.\n\nThe Forty-First AAAI Conference on Artificial Intelligence (AAAI-27) will be held in Montréal, Canada, from February 16 to February 23, 2027."
    ],
    "durationSeconds": 9.171103295000037
  },
  "sourceToolAssistantUUID": "99d5694a-a020-476e-89bf-d42bb1b5be0a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-18T20:41:58.791Z_

I've now completed deep research on all reviewer-flagged issues. Let me synthesize my findings and produce the revision.

**Key research takeaways:**
- **GuidedVLA**: Builds on π₀, supervises 3 predefined attention head types (object/spatial/temporal), achieves 75.4% on LIBERO-Plus (vs 68.2% π₀). No consistency objectives, no cross-category transfer, no affordance heatmaps — clear differentiation from LACVLA.
- **BusyBox**: Physical benchmark, 6 modules, even π₀.₅ and GR00T-N1.6 struggle badly on shuffled configurations. Directly tests affordance generalization.
- **ProGAL-VLA**: Another concurrent grounding approach (3D entity graph + symbolic sub-goals + GAC loss). Gets 71.5% LIBERO-Plus robustness. Different mechanism from LACVLA but should be acknowledged.
- **A100→H100 ratio**: Real benchmarks show 1.5-2.15x for transformer fine-tuning. 1.5x is reasonable, not optimistic. Using 1.4x conservatively.
- **Self-supervised affordance from robot data**: Well-established — gripper contact points as pseudo-labels, trajectory-based heatmaps. Clean fallback for HOVA-500K.

Now writing the complete revised idea with all changes.

```json
{
  "title": "LACVLA: Enforcing Language-Affordance Grounding via Consistency Objectives for Zero-Shot Cross-Category VLA Manipulation",
  "core_problem": "How can end-to-end VLA models achieve zero-shot manipulation transfer to entirely unseen object categories — objects with no visual precedent in training — given that (1) cross-category transfer fundamentally requires spatial grounding from language (the only cue that specifies WHERE to interact on a novel object), yet (2) current VLAs largely ignore language instructions (LIBERO-Plus, CVPR 2026; LangGap, Mar 2026), a failure mode that is survivable in-distribution but catastrophic when visual priors are absent?",
  "opportunity": "Cross-category zero-shot manipulation — generalizing to objects never seen during training — remains an open challenge: even strong VLAs like π₀.₅ and GR00T-N1.6 fail on affordance generalization across object variants (BusyBox, Feb 2026), and A0 (ICCV 2025) achieves cross-category transfer via 1M contact points but without language conditioning. The fundamental bottleneck is that novel objects lack visual priors, so language must serve as the primary guide for spatial grounding — yet diagnostic work shows VLAs systematically ignore language. LIBERO-Plus (CVPR 2026, arXiv 2510.13626) reveals VLAs exhibit positional bias rather than semantic understanding; LangGap (arXiv 2603.00592, Mar 2026) quantifies this: VLAs with 95%+ standard success largely ignore language, and targeted data augmentation hits a ceiling (0%→28% multi-task). LIBERO-Para (Mar 2026) shows 22–52pp drops under paraphrased instructions, with 80–96% of failures from planning-level trajectory divergence. Shin (Mar 2026) achieves only +1.71pp via LLM-generated paraphrase augmentation, consistent with LangGap's ceiling finding. Recent approaches address aspects of this problem but not the full combination: spatial grounding methods (ST4VLA, ICLR 2026; SpatialVLA, RSS 2025) improve performance broadly but do not structurally guarantee language conditioning — a model can learn spatial shortcuts within training categories. GuidedVLA (RSS 2026) supervises individual attention heads with auxiliary signals but uses 3 predefined factor types without cross-category transfer focus. ProGAL-VLA (Apr 2026) imposes a verified grounding bottleneck via 3D entity-centric graphs and symbolic sub-goals, improving robustness (30.3%→71.5% on LIBERO-Plus perturbations) but requires explicit entity recognition rather than open-vocabulary affordance transfer. PPCL (EACL 2024) showed consistency regularization beats augmentation with 10× fewer samples in NLP. The opportunity: an affordance-gated architectural bottleneck with self-supervised consistency objectives that structurally forces language to condition spatial grounding — making language a mandatory pathway for action generation — enabling genuine cross-category zero-shot transfer without 3D sensors, expensive cross-category annotations, or modular decomposition.",
  "landscape": "The VLA-affordance landscape has six relevant lineages, none of which combines architectural enforcement of language conditioning, self-supervised consistency on spatial affordance representations, and cross-category zero-shot transfer as the primary target. (1) Spatially-guided VLAs: ST4VLA (ICLR 2026, arXiv 2602.10109) introduces dual-system spatial grounding (Qwen2.5-VL planner + DiT/DINOv2 action expert), achieving 95.9% LIBERO average (98.0% Spatial, 99.0% Object, 93.8% Goal, 92.6% Long), 72%/61% attribute/spatial paraphrase robustness (vs π₀: 32%/31%), and 62% on new object instances (vs π₀: 32%, GR00T N1: 46%). This is LACVLA's strongest baseline — the null hypothesis is 'does explicit affordance consistency add value beyond spatial grounding alone?' InternVLA-M1 (arXiv 2510.13778) extends this with affordance recognition and chain-of-thought reasoning. SpatialVLA (RSS 2025, arXiv 2501.15830) introduces Ego3D Position Encoding and Adaptive Action Grids. Spatial Forcing (ICLR 2026, arXiv 2510.12276) aligns VLM features with 3D foundation models without 3D input at inference. All improve spatial understanding but none guarantees language conditions the spatial representation. (2) Supervised intermediate representation guidance: GuidedVLA (RSS 2026, arXiv 2605.12369) treats the action decoder as an assembly of functional components, supervising individual attention heads with auxiliary signals for three predefined factor types: object grounding (attention mass loss over detected object masks), spatial geometry (depth encoder feature constraint), and temporal skill logic (KL-divergence skill classification). Built on π₀, achieves 75.4% on LIBERO-Plus (vs 68.2% baseline), 90.63% on RoboTwin 2.0. Architectural parallel to LACVLA: both use explicit supervision on intermediate representations to improve VLA grounding. Key differences: GuidedVLA uses 3 predefined factor types (not open-vocabulary), does not use consistency objectives on heatmaps, does not produce affordance heatmaps, and does not target cross-category zero-shot transfer. LACVLA's affordance readout with stop-gradient bottleneck produces open-vocabulary spatial heatmaps enforced via self-supervised consistency — a fundamentally different supervision signal (consistency between paraphrases vs. factor-specific auxiliary losses). (3) Language grounding diagnostics and solutions: LIBERO-Plus (CVPR 2026, arXiv 2510.13626) reveals VLAs are insensitive to language and exhibit positional bias. LangGap (arXiv 2603.00592, Mar 2026) confirms VLAs ignore language and shows augmentation's ceiling (28% multi-task). LIBERO-Para (arXiv 2603.28301, Mar 2026) quantifies paraphrase fragility (22–52pp drops). Shin (arXiv 2603.16044, Mar 2026) achieves only +1.71pp via augmentation. ProGAL-VLA (arXiv 2604.09824, Apr 2026) constructs a 3D entity-centric graph with symbolic sub-goals and Grounding Alignment Contrastive loss, imposing a verified grounding bottleneck — achieves 71.5% robustness on LIBERO-Plus (up from 30.3%), but requires explicit entity recognition and 3D scene graphs, not applicable to open-vocabulary affordance transfer across unseen categories. Stable Language Guidance (ACL 2026, arXiv 2601.04052) addresses modality collapse at inference via residual steering — complementary to LACVLA's training-time approach. Attention recalibration (arXiv 2603.06001) provides train-free inference-time fix for attention sink dynamics but does not change learned representations. (4) Modular affordance-then-action pipelines: RT-Affordance (arXiv 2411.02704), UAD (ICRA 2025), RAM (CoRL 2024), RAAP (arXiv 2603.29419, Mar 2026), AffordDP (CVPR 2025), RoboMAP (arXiv 2510.10912), A0 (ICCV 2025, arXiv 2504.12636), and GLOVER++ (CoRL 2025, arXiv 2505.11865) all produce affordance representations but feed them to separate downstream planners/policies, sacrificing end-to-end optimization. A0 achieves zero-shot cross-category transfer via 1M contact points but without language conditioning. (5) Architectural bottleneck enforcement: DIAL (arXiv 2603.29844, Mar 2026) enforces a latent intent bottleneck via inverse dynamics — the action head MUST use predicted latent intent. This inspires LACVLA's affordance-gated bottleneck (stop-gradient on VLM features, affordance map as spatial attention gate). (6) Cross-category zero-shot benchmarks: AGNOSTOS/X-ICM (arXiv 2505.15660) provides 23 unseen manipulation tasks. VLA² (arXiv 2510.14902) uses agentic retrieval for unseen concepts. BusyBox (arXiv 2602.05441, Feb 2026) is a physical benchmark where 6 reconfigurable modules test affordance generalization — even π₀.₅ and GR00T-N1.6 fail on shuffled configurations despite identical affordances, demonstrating that affordance generalization remains unsolved. Gap: No existing work combines (a) architectural enforcement that language must condition spatial features via stop-gradient bottleneck, (b) self-supervised consistency objectives on affordance heatmaps (not raw actions, not predefined factor types), and (c) cross-category zero-shot transfer as the primary evaluation target.",
  "approach": "We propose LACVLA, an end-to-end VLA that structurally forces language to condition spatial affordance grounding through an affordance-gated bottleneck and self-supervised consistency objectives, enabling zero-shot cross-category manipulation transfer.\n\nArchitecture — Affordance-Gated Bottleneck (inspired by DIAL's latent intent bottleneck): Built on a 4B–7B VLM backbone (Qwen2-VL-4B via StarVLA or PaliGemma2) with LoRA fine-tuning. The architecture has three components:\n(a) Affordance Readout: A cross-attention layer where language instruction tokens attend over intermediate VLM visual features (layer ~16 of 32 for Qwen2-VL), producing a dense affordance heatmap over the image. This encodes WHERE to interact, conditioned on the instruction. Architecture: single cross-attention + LayerNorm + linear projection to H×W heatmap, <5M parameters.\n(b) Stop-Gradient Bottleneck: VLM intermediate visual features are passed through a stop-gradient before reaching the action head. The action head receives: affordance_heatmap ⊙ sg(VLM_visual_features) + proprioceptive_state. The affordance map acts as a spatial attention gate — if the model produces a uniform (language-ignoring) affordance map, the action head receives unselective visual features with no spatial focus, degrading performance. Unlike GuidedVLA's factor-specific head supervision (predefined types, direct auxiliary losses), LACVLA's stop-gradient ensures no task-semantic gradient flows through the non-affordance pathway — the action head CANNOT learn to extract task information from raw VLM features, and the affordance readout is open-vocabulary rather than restricted to predefined factor categories.\n(c) Flow-Matching Action Head: A lightweight DiT (Diffusion Transformer) that generates trajectory chunks conditioned on the affordance-gated visual features + proprioceptive state, following the flow-matching formulation.\n\nTraining Objectives — Three jointly optimized losses with phased schedule:\n(1) Instruction-Paraphrase Affordance Consistency (IPAC): Given the same visual scene and K LLM-generated paraphrases of the same task instruction (e.g., 'grab the mug handle' vs. 'grasp the cup by its handle'), the affordance maps must be consistent (KL divergence penalty on spatial heatmaps). This transfers the consistency regularization principle from PPCL (EACL 2024) — which showed consistency > augmentation with 10× less data in NLP — to spatial affordance heatmaps. Unlike Shin (2026), who uses paraphrases purely as data augmentation (+1.71pp), IPAC uses them as a regularization signal constraining affordance geometry. Paraphrases generated offline by LLM — free, unlimited supervision.\n(2) Instruction-Discriminative Affordance (IDA): Given the same visual scene and two semantically different instructions (e.g., 'pick up the mug by its handle' vs. 'pour from the mug'), the affordance maps must diverge (margin-based divergence loss). This prevents degenerate consistency collapse where the model produces instruction-invariant heatmaps to trivially satisfy IPAC. Different-instruction pairs come naturally from multi-task robot datasets.\n(3) Action-Grounded Affordance (AGA): Standard flow-matching loss for trajectory prediction through the affordance-gated bottleneck. This grounds the affordance map in manipulation-relevant contact regions via end-to-end backpropagation through the gating mechanism.\n\nPhased Training Schedule:\nPhase 1 — Affordance Readout Pre-training: PRIMARY path: pre-train on HOVA-500K with cross-attention readout predicting contact-point Gaussian heatmaps (σ proportional to object scale) conditioned on action-label text prompts from 675 action categories. Viewpoint augmentation (random crop, perspective warp, ego→third-person style augmentation) addresses the ego-centric domain gap. FALLBACK path (if domain gap diagnostic fails): self-supervised affordance readout initialization using robot data alone — extract pseudo-affordance Gaussian heatmaps from gripper position at grasp/contact time in robot trajectory data (well-established technique: text-driven affordance learning with pseudo-labels, trajectory-based contact recovery). This produces lower-coverage but higher-fidelity affordance supervision for the robot observation domain. Diagnostic checkpoint: evaluate pre-trained affordance readout on a held-out set of robot observation images; if domain gap degrades affordance quality below threshold (mean IoU < 0.3 between predicted heatmap peak and gripper contact region), switch to fallback path. Ablation of HOVA-500K vs. self-supervised initialization determines whether HOVA-500K is necessary, de-risking the paper from the HOVA-500K dependency.\nPhase 2 — End-to-end VLA training (steps 0–N): Fine-tune full model (VLM via LoRA + pre-trained affordance readout + flow-matching action head) on robot data. Sub-phases: (2a) AGA only for 10% of training — establish action grounding baseline. (2b) Add IPAC at 10% — enforce consistency while action loss stabilizes gradients. (2c) Ramp IDA from 0 to full weight over 15% of training via linear warmup, monitored by: (i) affordance entropy H(A) — if H(A) < 0.3 × H_max, increase IDA weight by 50%; (ii) instruction-discriminability D = mean pairwise KL between different-instruction maps on validation set — if D < 0.5, halt IPAC and boost IDA. GradNorm-style gradient normalization across the three losses balances training rates automatically.\n\nWhy Affordance Maps (Not Raw Actions) for Consistency: Affordance maps capture WHERE to interact — the geometric invariant across paraphrases and across categories sharing functional parts. Action distributions conflate WHERE + HOW + WHEN (trajectory shape, timing, force), making consistency regularization noisier. For cross-category transfer, WHERE is what transfers (handle locations generalize across mugs/cups/pitchers), while HOW adapts to object-specific geometry. This argument is validated empirically by ablation #5.\n\nCross-Object Functional Consistency via HOVA-500K: Group HOVA-500K images by shared action labels (675 categories) and apply soft KL penalty between affordance maps of same-action images from different object categories. This provides weak supervision for cross-category affordance consistency without requiring part-level functional equivalence annotations.\n\nData Pipeline: Open X-Embodiment and DROID for robot trajectories, HOVA-500K for affordance pre-training and cross-object grouping (with self-supervised robot-data fallback), LLM-generated instruction paraphrases (Qwen3 or GPT-4) for IPAC pairs.\n\nAblation Design (6 variants, streamlined to fit compute budget while retaining all core tests):\n(1) Full LACVLA — affordance-gated bottleneck + IPAC + IDA + AGA\n(2) Bottleneck analysis (merged): (a) No affordance bottleneck — direct VLA without affordance readout; (b) Bottleneck + AGA only, no consistency losses — tests whether architectural bottleneck alone suffices. Both sub-conditions use identical training data and hyperparameters; affordance map quality (entropy, instruction-discriminability) tracked for sub-condition (b) to diagnose whether the bottleneck induces meaningful affordance structure without consistency enforcement.\n(3) Modular composition — frozen GLOVER++ affordance → separate policy (tests end-to-end vs. modular)\n(4) Shin-style augmentation — paraphrases added as training data, no consistency loss (tests data augmentation ceiling, paralleling PPCL's NLP finding)\n(5) IPAC on raw actions — KL divergence between action distributions under paraphrased instructions, no affordance readout (CRITICAL: tests whether isolating WHERE via affordance maps outperforms consistency on conflated action distributions — if affordance maps win, that's the paper's key finding; if raw actions work comparably, the affordance readout is unnecessary overhead)\n(6) ST4VLA-style spatial grounding + IPAC on features — spatial grounding pre-training + consistency on intermediate VLM features without affordance readout (tests whether explicit affordance structure adds value beyond strong spatial pre-training + consistency)\n\nEvaluation Protocol — Primary (Cross-Category Zero-Shot Transfer):\n(a) Held-out object category experiments: partition LIBERO/DROID object categories into train/test sets, test on entirely unseen categories with both standard and paraphrased instructions\n(b) HOVA-500K cross-category transfer tests: train on K action categories with one set of objects (e.g., 'pour from pitcher'), test on same actions with different object categories (e.g., 'pour from kettle') — constructed from HOVA-500K's 675 shared action labels\n(c) AGNOSTOS benchmark (arXiv 2505.15660) for cross-task zero-shot evaluation (23 unseen tasks)\n(d) BusyBox (arXiv 2602.05441) supplementary evaluation: if physical hardware is available, test LACVLA on shuffled BusyBox configurations where even π₀.₅ and GR00T-N1.6 fail — directly measures affordance generalization across visual variants with identical functional affordances\n(e) Real-world evaluation on 5+ unseen object categories across at least 3 manipulation primitives (grasp, pour, push)\n\nEvaluation Protocol — Secondary:\n(f) LIBERO-Para benchmark with PRIDE metric for paraphrase robustness (direct comparison with ST4VLA's 72%/61%)\n(g) LangGap protocol for language grounding quality (targeting improvement over the 28% multi-task ceiling)\n(h) Affogato for affordance quality assessment\n(i) Standard LIBERO (Spatial, Object, Goal, Long) for in-distribution comparison with ST4VLA (95.9% avg)\n\nCoRL 2026 Infeasibility Statement: CoRL 2026 (abstract May 26 — 8 days from today, May 18) is infeasible given implementation scope. Primary target: AAAI 2027 (abstract Jul 21, full paper Jul 28 — 64 days to abstract). Backup: WACV 2027 Round 2 (paper Aug 27 — 101 days).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~175-245h A100 80GB, equivalent to ~125-175h H100 at conservative 1.4x ratio (HOVA-500K affordance readout pre-training ~20h or self-supervised fallback ~8h, 1 full LACVLA training run ~35-45h, 5 ablation experiments at ~12-18h each = 60-90h, cross-category evaluation sweeps ~25h, AGNOSTOS benchmark runs ~15h, BusyBox evaluation if available ~5h). 6 ablations (down from 8) are the key cost savings: merging bottleneck analysis into one experiment with sub-conditions and dropping phased-training ablation saves ~30-40h A100.",
      "gpu_utilization": "~15-25% effective utilization — idle during result analysis, loss weight iteration, domain gap diagnostics between phases",
      "timeline": "8-10 weeks (1-2 weeks data pipeline + affordance readout pre-training (HOVA-500K or self-supervised fallback) + domain gap diagnostics; 4-5 weeks iterative experimentation including all 6 ablations; 2-3 weeks cross-category evaluation + paper writing)",
      "team": "2 researchers (1 lead on affordance-gated architecture + consistency objectives + bottleneck enforcement, 1 on data pipeline/HOVA-500K integration/cross-category evaluation/AGNOSTOS setup)",
      "estimated_gpu_cost": "$265-370 (at ~$1.50/h A100 80GB)"
    },
    "human_in_loop": {
      "gpu_hours": "~225-310h A100 80GB, equivalent to ~160-220h H100 at conservative 1.4x ratio (agent runs 8-10 training configurations systematically: all 6 ablations + 2-4 additional hyperparameter variants, HOVA-500K pre-training or self-supervised fallback, with wasted runs caught early by human)",
      "gpu_utilization": "~40-55% — agent queues experiments but pauses at key gates: (1) affordance readout domain gap diagnostic (HOVA-500K vs. self-supervised), (2) affordance map quality inspection after bottleneck warmup, (3) cross-category held-out split design approval",
      "timeline": "6-8 weeks (agent handles paraphrase generation, HOVA-500K or self-supervised preprocessing, hyperparameter sweeps, AGNOSTOS/LIBERO-Para/LangGap evaluation scripts; human approves domain gap bridging strategy, inspects affordance maps, validates cross-category split design)",
      "team": "1 researcher, ~1.5h/day review",
      "claude_api_cost": "$200-500 (estimated 2,000-5,000 agent turns)",
      "estimated_gpu_cost": "$340-465 (at ~$1.50/h A100 80GB)",
      "risk_note": "Primary risk: HOVA-500K affordance readout domain gap — fully mitigated by self-supervised fallback using robot-data pseudo-affordance labels from gripper contact positions, with ablation comparing both paths. Secondary risk: affordance-gated bottleneck may be too restrictive — mitigated by ablation #2b (bottleneck without consistency) to isolate the effect. ST4VLA comparison (ablation #6) determines value beyond spatial grounding."
    },
    "auto_research": {
      "gpu_hours": "~450-650h A100 80GB, equivalent to ~320-465h H100 at conservative 1.4x ratio (agent explores 14-20 training configurations for phased schedule tuning, all 6 ablation variants × 2-3 seeds, both HOVA-500K and self-supervised affordance pre-training paths, full benchmark sweeps)",
      "gpu_utilization": "~85-95% — agent immediately queues next experiment upon completion; parallel ablation runs on multi-GPU setup",
      "timeline": "3-4 weeks with 4+ A100 GPUs available concurrently (bottleneck: affordance pre-training → domain gap diagnostic → phased training search → cross-category evaluation)",
      "team": "0 researchers after initial setup (~6-8 hours: dataset access, paraphrase generation config, HOVA-500K + self-supervised preprocessing, AGNOSTOS/LIBERO-Para/LangGap environment setup, cross-category held-out split definition)",
      "claude_api_cost": "$500-1,200 (estimated 5,000-12,000 agent turns)",
      "estimated_gpu_cost": "$675-975 (at ~$1.50/h A100 80GB)",
      "speed_bottleneck": "Each LoRA training run on 4B backbone takes ~8-12h on 4 A100s. HOVA-500K preprocessing and viewpoint-augmented Gaussian heatmap generation ~25h one-time. Cross-category evaluation setup ~6h one-time.",
      "risk_note": "Automated phased training managed by entropy/discriminability monitoring. If affordance-gated bottleneck causes consistent performance collapse across configurations, agent escalates to soft-gating variants. GradNorm balancing reduces sensitivity to manual loss weight tuning. Self-supervised fallback eliminates HOVA-500K as a single point of failure."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract Jul 21, full paper Jul 28, 2026 — primary target, 64 days to abstract; strong fit for self-supervised consistency + architectural bottleneck contribution with robotics application)",
    "WACV 2027 Round 2 (registration Aug 20, paper Aug 27, 2026 — realistic backup, 101 days; vision+robotics focus)",
    "ICLR 2027 (abstract ~Sep 2026, full paper ~Sep 2026 — dates TBD, estimated from ICLR 2026 cycle; top-tier target if cross-category zero-shot results are strong)",
    "CVPR 2027 (registration ~Nov 2026, paper ~Nov 2026 — dates TBD; if affordance visualization and cross-category transfer results are visually compelling)",
    "NOTE: CoRL 2026 (abstract May 26, paper May 29) was the user's original target but is infeasible — 8 days is insufficient for implementation of affordance-gated bottleneck, 6 ablations, HOVA-500K pipeline, and multi-benchmark evaluation"
  ],
  "level": "solid",
  "key_references": [
    "ST4VLA: Spatially Guided Training for Vision-Language-Action Models (ICLR 2026, arXiv 2602.10109) — strongest baseline: 95.9% LIBERO avg, 72%/61% paraphrase robustness, 62% unseen objects via spatial grounding alone",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (CVPR 2026, arXiv 2510.13626) — diagnostic revealing VLAs ignore language instructions, exhibit positional bias",
    "LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models (arXiv 2603.00592, Mar 2026) — quantifies language gap: augmentation reaches 90% single-task but only 28% multi-task",
    "GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization (RSS 2026, arXiv 2605.12369, May 2026) — supervises 3 predefined attention head types (object/spatial/temporal) on π₀; 75.4% LIBERO-Plus, 90.63% RoboTwin; architectural parallel (supervised intermediate representations) but no consistency objectives, no affordance heatmaps, no cross-category transfer",
    "BusyBox: Benchmarking Affordance Generalization (arXiv 2602.05441, Feb 2026, Microsoft) — physical benchmark with 6 reconfigurable modules; even π₀.₅ and GR00T-N1.6 fail on shuffled configurations; directly tests affordance generalization across visual variants",
    "ProGAL-VLA: Grounded Alignment through Prospective Reasoning in VLA Models (arXiv 2604.09824, Apr 2026) — verified grounding bottleneck via 3D entity-centric graph + GAC loss; 71.5% LIBERO-Plus robustness; requires explicit entity recognition, not applicable to open-vocabulary affordance transfer",
    "DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA (arXiv 2603.29844, Mar 2026) — latent intent bottleneck via inverse dynamics, inspiration for affordance-gated architecture",
    "InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy (arXiv 2510.13778) — spatially guided VLA with affordance recognition in pre-training",
    "SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Models (RSS 2025, arXiv 2501.15830) — spatial-aware action tokenization",
    "Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model (ICLR 2026, arXiv 2510.12276) — implicit spatial alignment without 3D input",
    "AGNOSTOS / X-ICM: Exploring the Limits of Vision-Language-Action Manipulations in Cross-task Generalization (arXiv 2505.15660) — cross-task zero-shot benchmark with 23 unseen tasks",
    "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models (arXiv 2603.28301, Mar 2026) — paraphrase robustness evaluation with PRIDE metric",
    "Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation (Shin, arXiv 2603.16044, Mar 2026) — direct augmentation baseline, +1.71pp only",
    "Stable Language Guidance / Residual Semantic Steering for VLAs (ACL 2026, arXiv 2601.04052) — inference-time modality collapse mitigation, complementary to LACVLA's training-time approach",
    "Restoring Linguistic Grounding in VLA Models via Train-Free Attention Recalibration (arXiv 2603.06001, Mar 2026) — diagnoses attention sink dynamics as cause of linguistic blindness; train-free inference fix complementary to LACVLA",
    "Prompt Perturbation Consistency Learning for Robust Language Models (PPCL, EACL 2024, arXiv 2402.15833) — consistency regularization > augmentation with 10× fewer samples in NLP",
    "Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs (arXiv 2510.14242, Oct 2025) — extends PPCL to LLMs",
    "OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024) — base VLA architecture",
    "StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing (arXiv 2604.05014, Apr 2026) — implementation framework",
    "GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation (CoRL 2025, arXiv 2505.11865) — provides HOVA-500K dataset, modular baseline",
    "PokéVLA: Empowering Pocket-Sized VLA Model with Comprehensive World Knowledge Guidance (arXiv 2604.20834, Apr 2026) — validates HOVA-500K ego→VLA transfer for backbone pre-training",
    "RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (arXiv 2411.02704, 2024) — modular affordance baseline",
    "A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation (ICCV 2025, arXiv 2504.12636) — hierarchical affordance with zero-shot transfer but no language conditioning",
    "RoboMAP: Adaptive Affordance Heatmaps via PaliGemma (arXiv 2510.10912, 2025) — modular language-conditioned heatmap architecture reference",
    "AffordDP: Generalizable Diffusion Policy with Transferable Affordance (CVPR 2025) — cross-category transfer via 3D contact points",
    "RAM: Retrieval-Based Affordance Transfer for Generalizable Zero-Shot Robotic Manipulation (CoRL 2024, arXiv 2407.04689) — retrieval-based affordance baseline",
    "RAAP: Retrieval-Augmented Affordance Prediction with Cross-Image Action Alignment (arXiv 2603.29419, Mar 2026) — cross-image affordance alignment",
    "Affogato: Learning Open-Vocabulary Affordance Grounding with Automated Data Generation at Scale (arXiv 2506.12009, 2025) — affordance quality benchmark",
    "AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation (arXiv 2604.11674, 2026) — simulation evaluation resource",
    "GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks (ICML 2018) — multi-task loss balancing",
    "LAP: Language-Action Pre-Training Enables Zero-shot Cross-Embodiment Transfer (RSS 2026, arXiv 2602.10556) — cross-embodiment (not cross-category) zero-shot via language-action alignment"
  ],
  "description": "We address cross-category zero-shot manipulation transfer — generalizing to objects with no visual precedent in training — where language is the only available guide for spatial grounding on novel objects. We show that the well-documented language-ignoring failure in VLAs (LIBERO-Plus, CVPR 2026; LangGap, Mar 2026) is particularly catastrophic in this setting: visual priors and layout memorization cannot compensate when the object itself is unseen. Existing approaches either improve spatial understanding without guaranteeing language conditions the representation (ST4VLA, SpatialVLA, Spatial Forcing), supervise predefined intermediate factor types without cross-category affordance transfer (GuidedVLA, RSS 2026), impose grounding bottlenecks requiring explicit entity recognition (ProGAL-VLA), or produce affordance representations in modular pipelines sacrificing end-to-end optimization (A0, GLOVER++, RT-Affordance). LACVLA proposes an affordance-gated architectural bottleneck, inspired by DIAL's latent intent bottleneck, that structurally forces all task-relevant spatial information through a language-conditioned affordance map: VLM intermediate features pass through stop-gradient before the action head, which receives affordance_heatmap ⊙ sg(visual_features) + proprioceptive_state. The affordance map (produced via cross-attention between VLM features and language tokens) acts as a spatial attention gate — a uniform (language-ignoring) map yields unselective features and degraded performance. Self-supervised consistency objectives enforce language-affordance grounding: IPAC ensures semantically equivalent instructions produce identical affordance maps (transferring PPCL's consistency > augmentation principle from NLP to spatial heatmaps), while IDA ensures semantically different instructions produce divergent maps (preventing collapse). Affordance readout is pre-trained via HOVA-500K with a fully specified self-supervised fallback using robot-data pseudo-affordance labels from gripper contact positions — eliminating HOVA-500K as a single point of failure and producing an ablation that determines whether HOVA-500K pre-training is necessary. A streamlined 6-variant ablation suite (reduced from 8 to fit ≤200 H100-hour budget) addresses all key questions: bottleneck necessity (#2, merged sub-conditions: no bottleneck vs. bottleneck-only), end-to-end vs. modular (#3), augmentation ceiling (#4), affordance maps vs. raw actions as consistency target (#5 — the paper's critical test: if affordance-level consistency outperforms action-level, it validates that isolating WHERE from HOW is essential), and value beyond spatial grounding (#6). Evaluation is anchored on cross-category zero-shot transfer as the PRIMARY metric: held-out object categories, HOVA-500K cross-category splits, AGNOSTOS benchmark, BusyBox affordance generalization (supplementary physical evaluation), and real-world tests on 5+ unseen categories. SECONDARY metrics cover paraphrase robustness (LIBERO-Para, LangGap), affordance quality (Affogato), and in-distribution performance (standard LIBERO). Primary target: AAAI 2027 (abstract Jul 21, 64 days).",
  "project_name": "lac_vla_zero_shot",
  "source": "web_research",
  "change_type": "minor"
}
```

**Summary of changes addressing all 5 reviewer issues:**

1. **GuidedVLA (RSS 2026) added** to landscape section (2) with detailed differentiation: predefined 3-factor supervision vs. LACVLA's open-vocabulary affordance heatmaps + consistency + stop-gradient bottleneck. Also added ProGAL-VLA as newly discovered concurrent work.

2. **Ablations trimmed from 8 → 6**: Merged #2/#4 into one experiment with sub-conditions (no bottleneck vs. bottleneck-only, tracking affordance map quality for both). Dropped #8 (phased training). Compute drops from 250-350h to 175-245h A100 = 125-175h H100 at conservative 1.4x ratio — safely within ≤200 H100-hour constraint.

3. **BusyBox added** as supplementary physical benchmark in evaluation protocol, with context on π₀.₅/GR00T-N1.6 failures.

4. **HOVA-500K fallback fully specified**: Self-supervised affordance readout initialization using gripper contact positions as pseudo-labels. Diagnostic checkpoint (mean IoU < 0.3 triggers fallback). Explicit ablation of HOVA-500K vs. self-supervised — de-risks the paper from HOVA-500K dependency entirely.

5. **Narrative reframed around cross-category transfer**: core_problem, opportunity, and description now open with "cross-category zero-shot manipulation transfer" rather than "VLAs ignore language," positioning LACVLA in a less crowded space.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b218d5a8-7bd6-413f-925b-54cd56119e49",
  "isSidechain": false,
  "requestId": "req_011CbAgGt9knytXmfv8q9fEN",
  "type": "assistant",
  "uuid": "0ca07714-a0ac-43d3-bf63-8cdb7fe70375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6cWAheqDMShsVHDDhgUSW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 48300,
      "output_tokens": 9763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 725,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9763,
          "cache_read_input_tokens": 48300,
          "cache_creation_input_tokens": 725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 725
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-18 (UTC).**  ## Original idea {   \"title\": \"LACVLA: Enforcing Language-Affordance Grounding via Consistency Object…",
  "leafUuid": "0ca07714-a0ac-43d3-bf63-8cdb7fe70375",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Runtime record

_source line 66_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise LACVLA affordance consistency for cross-category transfer",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-18 (UTC).**  ## Original idea {   \"title\": \"LACVLA: Enforcing Language-Affordance Grounding via Consistency Object…",
  "leafUuid": "0ca07714-a0ac-43d3-bf63-8cdb7fe70375",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise LACVLA affordance consistency for cross-category transfer",
  "sessionId": "3df479bc-9246-4cd8-86a4-5261455de34a"
}
```

---
