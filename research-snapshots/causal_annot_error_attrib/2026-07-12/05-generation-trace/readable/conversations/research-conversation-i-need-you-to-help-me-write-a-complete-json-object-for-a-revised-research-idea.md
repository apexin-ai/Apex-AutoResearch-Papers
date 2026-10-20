# Research conversation: I need you to help me write a complete JSON object for a revised research idea. I'll provide all the content — please fo

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 3
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aaba1fc60cb524cf3.jsonl`
- **Structured JSON:** [`162f9bdc07e7be5f0315.json`](../../sessions/16/162f9bdc07e7be5f0315.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

3 recorded events

### User

_source line 1 · 2026-05-18T20:49:28.611Z_

I need you to help me write a complete JSON object for a revised research idea. I'll provide all the content — please format it precisely as a JSON object. Output ONLY the JSON, nothing else.

Here's the complete revised idea content to format as JSON:

{
  "change_type": "major",
  "title": "AffordInvar: Annotation-Free Spatial Affordance Learning in VLAs via Instruction Invariance and Cross-Object Transfer",
  "core_problem": "Can we learn explicit spatial affordance representations within an end-to-end Vision-Language-Action model without any affordance annotations or external supervision signals, by jointly exploiting (1) instruction paraphrase invariance — semantically equivalent instructions must activate identical spatial affordance regions — and (2) cross-object affordance transfer — objects with similar functional parts must exhibit similar affordance patterns for the same interaction type — producing interpretable intermediate representations that improve manipulation success, paraphrase robustness, and zero-shot generalization to novel objects beyond what action-level invariance methods (RSS, LangForce), supervised spatial affordance approaches (PALM, CoA-VLA), spatial grounding with web-scale data (ST4VLA), 3D teacher-based alignment (Spatial Forcing), or standalone affordance modules (INTRA, AffordanceSAM) can achieve — all without the annotation pipelines, web-scale grounding data, simulator labels, or foundation model teachers that existing spatial methods require?",
  "opportunity": "Recent work has firmly established that spatial representations within VLAs improve manipulation — ST4VLA (ICLR 2026) uses point/box/trajectory spatial priors from web-scale grounding data achieving 95.9% on LIBERO, Spatial Forcing (ICLR 2026) aligns intermediate VLA embeddings with a 3D foundation model (VGGT) achieving 98.5% LIBERO average (current SOTA), PALM (CVPR 2026) integrates 4 supervised affordance types achieving 91.8% on LIBERO-Long, and SG-VLA (March 2026) co-trains affordance decoders with simulator-extracted labels. However, all these methods require external supervision: ST4VLA needs web-scale grounding data (RefCOCO, LLaVA-OneVision); PALM requires a semi-automated annotation pipeline (GroundingDINO + SAM + SpatialVLM + RoboPoint + CoTracker); SG-VLA depends on simulator ground-truth labels (grasp states, segmentation masks); and Spatial Forcing requires a pretrained 3D foundation model as teacher. This supervision dependence creates a critical scaling bottleneck — deploying to new environments, tasks, or real-world settings without simulators requires re-annotation or re-collection of grounding data. Meanwhile, LIBERO-Para (arXiv 2603.28301, March 2026) reveals that VLAs suffer 22-52 percentage point drops under simple paraphrasing with 80-96% of failures at the planning level — and none of the above spatial methods (ST4VLA, PALM, SG-VLA, Spatial Forcing) have been evaluated on LIBERO-Para, leaving paraphrase robustness as an untested dimension for spatial VLA methods. The context-dependent affordance study (arXiv 2603.04419) confirms that stable latent affordance factors persist despite >90% lexical drift across contexts, suggesting spatial affordance structure is exploitable as a free self-supervision signal from paraphrases alone. OpenVLA-OFT achieves 97.1% on LIBERO with LoRA fine-tuning in ~10-15 hours on a single A100, providing a compute-efficient backbone.",
  "landscape": "**Spatial representations in VLAs (supervised/teacher-based)**: ST4VLA (ICLR 2026, arXiv 2602.10109) uses spatial priors (point, box, trajectory) from web-scale grounding pre-training (RefCOCO, LLaVA-OneVision) followed by spatially guided action post-training, achieving 95.9% LIBERO average (92.6% Long) and emergent paraphrase robustness in real-world (52% on novel instructions by attribute) — the closest spatial VLA, but requires web-scale grounding data not available in new domains and does not explicitly learn affordance maps. Spatial Forcing (ICLR 2026, arXiv 2510.12276) aligns intermediate VLA visual embeddings with 3D representations from VGGT, achieving 98.5% LIBERO average (96.0% Long) with 3.8x training speedup — a plug-and-play approach demonstrating that intermediate spatial alignment improves VLAs, but requires a pretrained 3D foundation model as teacher with no learned affordance structure. PALM (CVPR 2026, arXiv 2601.07060) integrates 4 complementary affordance types (global object masks via GroundingDINO+SAM, local contact heatmaps, spatial placements via SpatialVLM+RoboPoint, motion dynamics via CoTracker) end-to-end with progress-aware policy learning, achieving 91.8% on LIBERO-Long — the most directly comparable affordance-in-VLA work, but requires a multi-model semi-automated annotation pipeline. SG-VLA (arXiv 2603.22760, March 2026) co-trains auxiliary decoders for grasp affordances, segmentation masks, robot pose, and joint configurations from shared VLA features, with ground truth extracted from ManiSkill-HAB simulator state — demonstrates that auxiliary affordance decoders improve VLA performance, but is limited to simulation environments with accessible ground-truth state. RoboMAP (arXiv 2510.10912, October 2025) generates adaptive affordance heatmaps as continuous spatial representations for language-guided manipulation achieving 82% real-world success — anticipates our heatmap-based approach but is a standalone grounding module, not integrated into end-to-end VLA training, and requires diverse annotation synthesis. **Action-level robustness methods**: RSS (arXiv 2601.04052, January 2026) uses Monte Carlo Syntactic Integration and Residual Affordance Steering at the action logit level, achieving 82.2% on pi0 (vs 52.4% baseline) and 90.0% on LIBERO-Plus — strong but explicitly operates at the action output level with no learned spatial affordance maps. LangForce/BayesianVLA (arXiv 2601.15197, January 2026) uses Bayesian decomposition into vision-only prior and language-conditioned posterior achieving 11.3% OOD improvement on SimplerEnv — complementary but similarly action-level. RobustVLA (ICLR 2026) enforces action-level consistency under 17 perturbation types. **Standalone affordance modules**: INTRA (ECCV 2024, arXiv 2409.06210) uses ChatGPT-4-generated synonyms with interaction-relationship-guided contrastive learning for text-conditioned affordance maps, SOTA on AGD20K/UMD — directly anticipates our paraphrase-invariance idea for affordance but is disconnected from VLA action prediction. AffordanceSAM (April 2025, arXiv 2504.15650) extends SAM for affordance grounding, current SOTA on AGD20K — supervised, standalone. WSAG-PLSP (ICLR 2025) uses part-level semantic priors for weakly supervised affordance grounding — standalone, requires pseudo-label generation. **Supervised affordance in VLAs**: CoA-VLA (ICCV 2025) integrates chain-of-affordance reasoning with supervised labels. GeneralVLA (arXiv 2602.04315) proposes a hierarchical VLA with externally supervised Affordance Segmentation Module. RT-Affordance (ICRA 2025) uses affordances as intermediate representations with supervised learning achieving 69% vs 15% baseline. **Diagnostic benchmarks**: LIBERO-Para (arXiv 2603.28301, March 2026) reveals 22-52pp VLA drops under paraphrasing — confirms the problem but proposes no solution and has not been used to evaluate any spatial VLA method (ST4VLA, PALM, SG-VLA, Spatial Forcing). **The critical gap**: No work learns spatial affordance maps within a VLA via pure self-supervision. ST4VLA uses web-scale grounding data; PALM uses multi-model annotation pipelines; SG-VLA uses simulator ground truth; Spatial Forcing uses 3D foundation model teachers. Our method requires only robot demonstrations + LLM-generated paraphrases.",
  "approach": "We propose AffordInvar, which augments OpenVLA-OFT with a lightweight spatial affordance decoder trained jointly with the VLA via LoRA using two complementary self-supervised signals — requiring no affordance annotations, web-scale grounding data, simulator labels, or foundation model teachers. **Architecture**: The affordance decoder takes intermediate features from the VLA's 18th transformer layer (out of 32), which retain spatial structure before the final action-prediction layers. The decoder consists of 3 transposed convolution blocks (each: ConvTranspose2d 4x4 stride 2, GroupNorm, GELU) upsampling from 16x16 to 128x128 resolution, with text conditioning via the instruction embedding projected through a linear layer and channel-wise multiplied at each block (~8M parameters total, <0.12% of VLA backbone). Output is a sigmoid-activated 128x128 affordance heatmap. **Self-supervised signal 1 — Paraphrase invariance (L_consist)**: For each training episode, Qwen 3 generates K=3 semantically equivalent instruction paraphrases offline. During training, each paraphrase-image pair is processed through the VLA, and a symmetric KL divergence loss enforces identical affordance heatmaps across all K+1 instruction variants: L_consist = (1/C(K+1,2)) sum_{i&lt;j} KL(h_i || h_j), extending SelfEQ's visual grounding consistency (CVPR 2024) from general VLM grounding to the VLA affordance domain. Unlike RSS which applies paraphrase averaging at the action logit level, we enforce consistency at the intermediate spatial representation level, providing richer structured learning signal. Unlike ST4VLA's emergent robustness from web-scale spatial pre-training, we explicitly optimize for instruction invariance. **Self-supervised signal 2 — Cross-object affordance transfer (L_transfer)**: Episodes with semantically similar instructions (cosine similarity > 0.85 on instruction embeddings) but different target objects are mined as positive pairs; episodes with the same object but different interaction types serve as negatives. A contrastive InfoNCE loss on spatially-normalized affordance features encourages interaction-specific (not object-specific) affordance representations, enabling zero-shot transfer to novel objects — inspired by INTRA's interaction-relationship contrastive learning but operating on VLA-internal features with free-form instructions rather than predefined interaction labels. **Affordance-action integration**: The affordance heatmap is bilinearly downsampled to the action feature resolution and applied as an element-wise gate: action_features = action_features * sigma(W_g * affordance_features + b_g), where W_g is a learned linear projection (~0.5M parameters). This is architecturally similar to SG-VLA's auxiliary decoder approach but with a key difference: our decoder is trained entirely self-supervised while SG-VLA requires simulator ground truth for each auxiliary task. **Entropy regularization**: H_entropy = -lambda_H sum h_i log(h_i), preventing degenerate uniform or collapsed heatmaps. **Total loss**: L = L_action + alpha*L_consist + beta*L_transfer + lambda_H*H_entropy, where L_action is OpenVLA-OFT's continuous L1 action regression loss. **Evaluation**: (1) Manipulation success on LIBERO-Long (10 tasks, standard) and LIBERO-Para (paraphrase robustness, measuring PRIDE score) — we will be the first to evaluate a spatial affordance VLA method on LIBERO-Para; (2) Zero-shot generalization to held-out object categories within LIBERO; (3) Held-out interaction type generalization: train without all 'opening' tasks and test on them, plus creative rephrasings via Qwen 3 using novel interaction vocabulary (e.g., 'unfasten the container' instead of 'open the drawer') to test whether affordance representations generalize to unseen interaction semantics; (4) Affordance transfer evaluation with fine-tuning protocol: (a) zero-shot application of the VLA-learned affordance decoder on AGD20K/UMD as an exploratory experiment assessing cross-domain affordance quality, and (b) fine-tuning only the affordance decoder on AGD20K while freezing the VLA backbone, testing whether VLA-learned representations provide useful initialization vs. training from scratch — this addresses the large sim-to-real domain gap; (5) Qualitative affordance map visualization and contact-point prediction accuracy on held-out LIBERO episodes. **Baselines**: (a) OpenVLA-OFT (vanilla, no affordance) — 97.1% LIBERO standard; (b) OpenVLA-OFT + RSS-style action-level paraphrase invariance (our reimplementation); (c) OpenVLA-OFT + Spatial Forcing (intermediate 3D alignment with VGGT teacher) — 98.5% LIBERO average; (d) PALM (semi-automated affordance annotation) — 91.8% LIBERO-Long; (e) ST4VLA (web-scale spatial grounding) — 95.9% LIBERO average; (f) INTRA affordance maps + OpenVLA-OFT policy (two-stage); (g) CoA-VLA (supervised affordance). Key comparison axis: standard LIBERO performance may be competitive but not necessarily SOTA (Spatial Forcing at 98.5% is hard to beat without 3D teachers); our primary advantage claims are on (i) LIBERO-Para paraphrase robustness where explicit invariance training should outperform emergent robustness, (ii) zero-shot novel object/interaction generalization where annotation-free affordance transfer should outperform annotation-dependent methods in out-of-distribution settings, and (iii) annotation efficiency — competitive performance without any affordance labels, web-scale data, or foundation model teachers. **Key hypotheses**: (a) Explicit paraphrase invariance at the spatial affordance level provides better PRIDE scores on LIBERO-Para than ST4VLA's emergent robustness from spatial grounding or RSS's action-level invariance; (b) Self-supervised cross-object affordance transfer enables superior zero-shot generalization to novel objects compared to methods that learn object-specific supervised affordance features (PALM, SG-VLA); (c) Despite requiring no external supervision, AffordInvar achieves within 2-3 percentage points of supervised spatial methods (PALM, ST4VLA) on standard LIBERO, demonstrating that self-supervision closes most of the gap; (d) VLA-learned affordance representations provide useful initialization for downstream affordance benchmarks, demonstrated by faster convergence when fine-tuning the decoder on AGD20K vs. training from scratch.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180-200h H100 80GB (8-9 training runs at ~20-22h each: 2 main method runs, 2 baseline reproductions including Spatial Forcing and RSS reimplementation, 4 ablation runs for L_consist-only/L_transfer-only/no-gating/decoder-depth, 1 hyperparameter tuning run)",
      "gpu_utilization": "~30-35% effective utilization — human iteration time between runs for debugging and analysis",
      "timeline": "8-10 weeks (2 weeks codebase setup + paraphrase generation + baseline reproduction, 4-5 weeks experimentation including LIBERO-Para evaluation and AGD20K fine-tuning, 2-3 weeks paper writing)",
      "team": "1-2 researchers with VLA fine-tuning experience",
      "estimated_gpu_cost": "~$600-$700 (200h x $3.50/hr on-demand H100, or ~$400-$500 with spot pricing)"
    },
    "human_in_loop": {
      "gpu_hours": "~190-200h H100 80GB (agent manages experiment scheduling with slightly more efficient ablation design)",
      "gpu_utilization": "~60-70% — agent queues next experiment after prior run, human approves loss hyperparameters and reviews affordance heatmap quality at checkpoints",
      "timeline": "5-7 weeks (agent handles implementation and experiment orchestration; human reviews loss weight schedules and affordance map quality daily ~1hr)",
      "team": "1 researcher, ~1hr/day check-in",
      "claude_api_cost": "$100-200 (1,000-2,000 Opus turns for code generation, experiment design, result analysis)",
      "estimated_gpu_cost": "~$600-$700 (200h x $3.50/hr)",
      "risk_note": "Affordance consistency loss hyperparameters (alpha, beta) are sensitive — human review of affordance heatmaps after first 2-3 runs is critical to detect degenerate solutions (uniform or collapsed maps) early and adjust entropy regularization strength"
    },
    "auto_research": {
      "gpu_hours": "~200h H100 80GB (hard budget cap; agent maximizes information per run via sequential Bayesian hyperparameter optimization over alpha, beta, lambda_H, LoRA rank, and decoder depth)",
      "gpu_utilization": "~90-95% — agent immediately launches next experiment upon completion, no human wait time",
      "timeline": "2-3 weeks with 4 H100 GPUs (parallel ablation pairs reduce wall-clock time; includes evaluation and paper draft)",
      "team": "0 researchers after initial ~2hr setup (repo clone, API keys, compute allocation)",
      "claude_api_cost": "$200-400 (2,000-4,000 Opus turns for autonomous code development, ~9 experiment configurations, analysis, and paper writing)",
      "estimated_gpu_cost": "~$600-$700 (200h x $3.50/hr)",
      "speed_bottleneck": "GPU count is primary bottleneck — with 4 H100s, parallel ablation pairs complete in 2-3 weeks; with only 2 H100s, extends to 4-5 weeks",
      "risk_note": "Without human oversight, agent may waste ~20-30% of compute budget exploring suboptimal loss weight configurations before discovering effective entropy regularization settings — Bayesian optimization mitigates but does not eliminate this risk"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstracts July 21, full paper July 28, 2026 — primary target, ~10 weeks from today, feasible in human-in-loop or auto-research modes)",
    "ICRA 2027 (estimated deadline ~September 15, 2026 — flagship robotics venue, comfortable timeline, natural fit for manipulation-focused contribution)",
    "ICLR 2027 (estimated deadline ~October 2026 — top-tier ML venue, strongest signal for self-supervised learning methodology contribution)",
    "CoRL 2027 (estimated deadline ~June 2027 — if additional real-robot experiments are needed for strongest submission)"
  ],
  "level": "top-tier",
  "key_references": [
    "ST4VLA: Spatially Guided Training for Vision-Language-Action Models — spatial priors (point, box, trajectory) from web-scale grounding data, 95.9% LIBERO average, emergent paraphrase robustness (ICLR 2026, arXiv 2602.10109)",
    "PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation — 4 supervised affordance types with semi-automated annotation (GroundingDINO+SAM+SpatialVLM+RoboPoint+CoTracker), 91.8% LIBERO-Long (CVPR 2026, arXiv 2601.07060)",
    "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation — auxiliary decoders for grasp affordances and segmentation from simulator ground truth (arXiv 2603.22760, March 2026)",
    "Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model — intermediate VLA alignment with 3D foundation model (VGGT), 98.5% LIBERO average, 3.8x training speedup (ICLR 2026, arXiv 2510.12276)",
    "RoboMAP: More than A Point — adaptive affordance heatmaps for spatial grounding, 82% real-world success (arXiv 2510.10912, October 2025)",
    "Stable Language Guidance for Vision-Language-Action Models — RSS with Monte Carlo Syntactic Integration and Residual Affordance Steering (arXiv 2601.04052, January 2026)",
    "INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding — text synonym augmentation with contrastive learning for affordance on AGD20K (ECCV 2024, arXiv 2409.06210)",
    "LangForce/BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries — Bayesian VLA instruction-following via PMI (arXiv 2601.15197, January 2026)",
    "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — 22-52pp drops under paraphrasing, PRIDE metric (arXiv 2603.28301, March 2026)",
    "OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success — OpenVLA-OFT (arXiv 2502.19645, February 2025)",
    "Improved Visual Grounding through Self-Consistent Explanations — SelfEQ paraphrase consistency for VLM grounding (CVPR 2024)",
    "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance (ICCV 2025, arXiv 2412.20451)",
    "GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning (arXiv 2602.04315, February 2026)",
    "RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (ICRA 2025, arXiv 2411.02704)",
    "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations — RobustVLA (ICLR 2026, arXiv 2510.00037)",
    "Context-Dependent Affordance Computation in Vision-Language Models — >90% lexical drift, stable latent factors (arXiv 2603.04419)",
    "VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (CoRL 2023, arXiv 2307.05973)",
    "OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding (arXiv 2404.11000, 2024)",
    "AffordanceSAM: Segment Anything Once More in Affordance Grounding — current SOTA on AGD20K (arXiv 2504.15650, April 2025)",
    "Weakly-Supervised Affordance Grounding Guided by Part-Level Semantic Priors — WSAG-PLSP (ICLR 2025, arXiv 2505.24103)",
    "Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation (arXiv 2603.16044, March 2026)",
    "Learning Affordance Grounding from Exocentric Images — AGD20K dataset (CVPR 2022)"
  ],
  "description": "AffordInvar introduces annotation-free spatial affordance learning within an end-to-end Vision-Language-Action model, addressing a critical gap in the rapidly maturing landscape of spatial VLA methods. Recent work has established that spatial representations within VLAs significantly improve manipulation: ST4VLA (ICLR 2026) achieves 95.9% LIBERO average via web-scale spatial grounding, Spatial Forcing (ICLR 2026) achieves 98.5% via 3D foundation model alignment, PALM (CVPR 2026) achieves 91.8% LIBERO-Long via 4 semi-automated affordance types, and SG-VLA (March 2026) co-trains affordance decoders with simulator ground truth. However, all these methods require external supervision — web-scale grounding data, multi-model annotation pipelines, simulator labels, or foundation model teachers — creating scaling bottlenecks for new environments and tasks. AffordInvar eliminates this supervision requirement entirely. Built on OpenVLA-OFT with LoRA, it adds a lightweight 8M-parameter transposed-convolution affordance decoder on intermediate VLA features (layer 18/32) producing 128x128 spatial heatmaps, trained via two complementary self-supervised signals requiring only robot demonstrations and LLM-generated paraphrases: (1) paraphrase invariance — symmetric KL divergence enforcing identical affordance maps across K=3 Qwen-3-generated instruction variants, extending SelfEQ (CVPR 2024) from general VLM grounding to VLA affordance and explicitly optimizing the instruction robustness that ST4VLA achieves only emergently, and (2) cross-object affordance transfer — InfoNCE contrastive loss on spatially-normalized affordance features across episodes with similar interactions but different objects, inspired by INTRA but operating on VLA-internal features. The affordance heatmap gates action prediction via learned element-wise modulation. Key advantages over existing spatial VLA methods: (a) no annotation pipeline (vs. PALM's GroundingDINO+SAM+SpatialVLM+RoboPoint+CoTracker), no web-scale data (vs. ST4VLA's RefCOCO), no simulator labels (vs. SG-VLA), no 3D teachers (vs. Spatial Forcing) — only robot demonstrations + LLM paraphrases; (b) explicit paraphrase invariance optimization at the spatial level, unlike any existing spatial VLA method; (c) interpretable affordance maps independently evaluable on standard benchmarks. Evaluated on LIBERO-Long, LIBERO-Para (first spatial VLA method evaluated on paraphrase robustness via PRIDE metric), held-out interaction types, and AGD20K via fine-tuning protocol. Primary claims: superior LIBERO-Para PRIDE scores over emergent robustness (ST4VLA) and action-level invariance (RSS); competitive standard LIBERO performance without any affordance annotations; superior zero-shot novel object generalization via annotation-free affordance transfer. Baselines include OpenVLA-OFT, Spatial Forcing, PALM, ST4VLA, RSS-style action invariance, and CoA-VLA. Designed for <=200 H100-hours via LoRA efficiency.",
  "project_name": "afford_invar_vla",
  "source": "web_research"
}

Please output this as a valid, properly escaped JSON object. Make sure all quotes within strings are properly handled, and the structure is valid JSON. Output ONLY the JSON.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "aae39bd4-b34f-48d6-b312-052f0425a13f",
  "agentId": "aaba1fc60cb524cf3",
  "type": "user",
  "uuid": "c1d02912-1e0f-468d-86f2-741bdae9807d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4f4c7ec-c601-4d53-8881-5c7ea4ffd775",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T20:49:28.617Z_

```json
{
  "parentUuid": "c1d02912-1e0f-468d-86f2-741bdae9807d",
  "isSidechain": true,
  "agentId": "aaba1fc60cb524cf3",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "00f3d1c8-395f-4059-a267-e1cd68e26f3b",
  "timestamp": "2026-05-18T20:49:28.617Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4f4c7ec-c601-4d53-8881-5c7ea4ffd775",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-18T20:51:04.959Z_



```json
{
  "change_type": "major",
  "title": "AffordInvar: Annotation-Free Spatial Affordance Learning in VLAs via Instruction Invariance and Cross-Object Transfer",
  "core_problem": "Can we learn explicit spatial affordance representations within an end-to-end Vision-Language-Action model without any affordance annotations or external supervision signals, by jointly exploiting (1) instruction paraphrase invariance — semantically equivalent instructions must activate identical spatial affordance regions — and (2) cross-object affordance transfer — objects with similar functional parts must exhibit similar affordance patterns for the same interaction type — producing interpretable intermediate representations that improve manipulation success, paraphrase robustness, and zero-shot generalization to novel objects beyond what action-level invariance methods (RSS, LangForce), supervised spatial affordance approaches (PALM, CoA-VLA), spatial grounding with web-scale data (ST4VLA), 3D teacher-based alignment (Spatial Forcing), or standalone affordance modules (INTRA, AffordanceSAM) can achieve — all without the annotation pipelines, web-scale grounding data, simulator labels, or foundation model teachers that existing spatial methods require?",
  "opportunity": "Recent work has firmly established that spatial representations within VLAs improve manipulation — ST4VLA (ICLR 2026) uses point/box/trajectory spatial priors from web-scale grounding data achieving 95.9% on LIBERO, Spatial Forcing (ICLR 2026) aligns intermediate VLA embeddings with a 3D foundation model (VGGT) achieving 98.5% LIBERO average (current SOTA), PALM (CVPR 2026) integrates 4 supervised affordance types achieving 91.8% on LIBERO-Long, and SG-VLA (March 2026) co-trains affordance decoders with simulator-extracted labels. However, all these methods require external supervision: ST4VLA needs web-scale grounding data (RefCOCO, LLaVA-OneVision); PALM requires a semi-automated annotation pipeline (GroundingDINO + SAM + SpatialVLM + RoboPoint + CoTracker); SG-VLA depends on simulator ground-truth labels (grasp states, segmentation masks); and Spatial Forcing requires a pretrained 3D foundation model as teacher. This supervision dependence creates a critical scaling bottleneck — deploying to new environments, tasks, or real-world settings without simulators requires re-annotation or re-collection of grounding data. Meanwhile, LIBERO-Para (arXiv 2603.28301, March 2026) reveals that VLAs suffer 22-52 percentage point drops under simple paraphrasing with 80-96% of failures at the planning level — and none of the above spatial methods (ST4VLA, PALM, SG-VLA, Spatial Forcing) have been evaluated on LIBERO-Para, leaving paraphrase robustness as an untested dimension for spatial VLA methods. The context-dependent affordance study (arXiv 2603.04419) confirms that stable latent affordance factors persist despite >90% lexical drift across contexts, suggesting spatial affordance structure is exploitable as a free self-supervision signal from paraphrases alone. OpenVLA-OFT achieves 97.1% on LIBERO with LoRA fine-tuning in ~10-15 hours on a single A100, providing a compute-efficient backbone.",
  "landscape": "**Spatial representations in VLAs (supervised/teacher-based)**: ST4VLA (ICLR 2026, arXiv 2602.10109) uses spatial priors (point, box, trajectory) from web-scale grounding pre-training (RefCOCO, LLaVA-OneVision) followed by spatially guided action post-training, achieving 95.9% LIBERO average (92.6% Long) and emergent paraphrase robustness in real-world (52% on novel instructions by attribute) — the closest spatial VLA, but requires web-scale grounding data not available in new domains and does not explicitly learn affordance maps. Spatial Forcing (ICLR 2026, arXiv 2510.12276) aligns intermediate VLA visual embeddings with 3D representations from VGGT, achieving 98.5% LIBERO average (96.0% Long) with 3.8x training speedup — a plug-and-play approach demonstrating that intermediate spatial alignment improves VLAs, but requires a pretrained 3D foundation model as teacher with no learned affordance structure. PALM (CVPR 2026, arXiv 2601.07060) integrates 4 complementary affordance types (global object masks via GroundingDINO+SAM, local contact heatmaps, spatial placements via SpatialVLM+RoboPoint, motion dynamics via CoTracker) end-to-end with progress-aware policy learning, achieving 91.8% on LIBERO-Long — the most directly comparable affordance-in-VLA work, but requires a multi-model semi-automated annotation pipeline. SG-VLA (arXiv 2603.22760, March 2026) co-trains auxiliary decoders for grasp affordances, segmentation masks, robot pose, and joint configurations from shared VLA features, with ground truth extracted from ManiSkill-HAB simulator state — demonstrates that auxiliary affordance decoders improve VLA performance, but is limited to simulation environments with accessible ground-truth state. RoboMAP (arXiv 2510.10912, October 2025) generates adaptive affordance heatmaps as continuous spatial representations for language-guided manipulation achieving 82% real-world success — anticipates our heatmap-based approach but is a standalone grounding module, not integrated into end-to-end VLA training, and requires diverse annotation synthesis. **Action-level robustness methods**: RSS (arXiv 2601.04052, January 2026) uses Monte Carlo Syntactic Integration and Residual Affordance Steering at the action logit level, achieving 82.2% on pi0 (vs 52.4% baseline) and 90.0% on LIBERO-Plus — strong but explicitly operates at the action output level with no learned spatial affordance maps. LangForce/BayesianVLA (arXiv 2601.15197, January 2026) uses Bayesian decomposition into vision-only prior and language-conditioned posterior achieving 11.3% OOD improvement on SimplerEnv — complementary but similarly action-level. RobustVLA (ICLR 2026) enforces action-level consistency under 17 perturbation types. **Standalone affordance modules**: INTRA (ECCV 2024, arXiv 2409.06210) uses ChatGPT-4-generated synonyms with interaction-relationship-guided contrastive learning for text-conditioned affordance maps, SOTA on AGD20K/UMD — directly anticipates our paraphrase-invariance idea for affordance but is disconnected from VLA action prediction. AffordanceSAM (April 2025, arXiv 2504.15650) extends SAM for affordance grounding, current SOTA on AGD20K — supervised, standalone. WSAG-PLSP (ICLR 2025) uses part-level semantic priors for weakly supervised affordance grounding — standalone, requires pseudo-label generation. **Supervised affordance in VLAs**: CoA-VLA (ICCV 2025) integrates chain-of-affordance reasoning with supervised labels. GeneralVLA (arXiv 2602.04315) proposes a hierarchical VLA with externally supervised Affordance Segmentation Module. RT-Affordance (ICRA 2025) uses affordances as intermediate representations with supervised learning achieving 69% vs 15% baseline. **Diagnostic benchmarks**: LIBERO-Para (arXiv 2603.28301, March 2026) reveals 22-52pp VLA drops under paraphrasing — confirms the problem but proposes no solution and has not been used to evaluate any spatial VLA method (ST4VLA, PALM, SG-VLA, Spatial Forcing). **The critical gap**: No work learns spatial affordance maps within a VLA via pure self-supervision. ST4VLA uses web-scale grounding data; PALM uses multi-model annotation pipelines; SG-VLA uses simulator ground truth; Spatial Forcing uses 3D foundation model teachers. Our method requires only robot demonstrations + LLM-generated paraphrases.",
  "approach": "We propose AffordInvar, which augments OpenVLA-OFT with a lightweight spatial affordance decoder trained jointly with the VLA via LoRA using two complementary self-supervised signals — requiring no affordance annotations, web-scale grounding data, simulator labels, or foundation model teachers. **Architecture**: The affordance decoder takes intermediate features from the VLA's 18th transformer layer (out of 32), which retain spatial structure before the final action-prediction layers. The decoder consists of 3 transposed convolution blocks (each: ConvTranspose2d 4x4 stride 2, GroupNorm, GELU) upsampling from 16x16 to 128x128 resolution, with text conditioning via the instruction embedding projected through a linear layer and channel-wise multiplied at each block (~8M parameters total, <0.12% of VLA backbone). Output is a sigmoid-activated 128x128 affordance heatmap. **Self-supervised signal 1 — Paraphrase invariance (L_consist)**: For each training episode, Qwen 3 generates K=3 semantically equivalent instruction paraphrases offline. During training, each paraphrase-image pair is processed through the VLA, and a symmetric KL divergence loss enforces identical affordance heatmaps across all K+1 instruction variants: L_consist = (1/C(K+1,2)) sum_{i&lt;j} KL(h_i || h_j), extending SelfEQ's visual grounding consistency (CVPR 2024) from general VLM grounding to the VLA affordance domain. Unlike RSS which applies paraphrase averaging at the action logit level, we enforce consistency at the intermediate spatial representation level, providing richer structured learning signal. Unlike ST4VLA's emergent robustness from web-scale spatial pre-training, we explicitly optimize for instruction invariance. **Self-supervised signal 2 — Cross-object affordance transfer (L_transfer)**: Episodes with semantically similar instructions (cosine similarity > 0.85 on instruction embeddings) but different target objects are mined as positive pairs; episodes with the same object but different interaction types serve as negatives. A contrastive InfoNCE loss on spatially-normalized affordance features encourages interaction-specific (not object-specific) affordance representations, enabling zero-shot transfer to novel objects — inspired by INTRA's interaction-relationship contrastive learning but operating on VLA-internal features with free-form instructions rather than predefined interaction labels. **Affordance-action integration**: The affordance heatmap is bilinearly downsampled to the action feature resolution and applied as an element-wise gate: action_features = action_features * sigma(W_g * affordance_features + b_g), where W_g is a learned linear projection (~0.5M parameters). This is architecturally similar to SG-VLA's auxiliary decoder approach but with a key difference: our decoder is trained entirely self-supervised while SG-VLA requires simulator ground truth for each auxiliary task. **Entropy regularization**: H_entropy = -lambda_H sum h_i log(h_i), preventing degenerate uniform or collapsed heatmaps. **Total loss**: L = L_action + alpha*L_consist + beta*L_transfer + lambda_H*H_entropy, where L_action is OpenVLA-OFT's continuous L1 action regression loss. **Evaluation**: (1) Manipulation success on LIBERO-Long (10 tasks, standard) and LIBERO-Para (paraphrase robustness, measuring PRIDE score) — we will be the first to evaluate a spatial affordance VLA method on LIBERO-Para; (2) Zero-shot generalization to held-out object categories within LIBERO; (3) Held-out interaction type generalization: train without all 'opening' tasks and test on them, plus creative rephrasings via Qwen 3 using novel interaction vocabulary (e.g., 'unfasten the container' instead of 'open the drawer') to test whether affordance representations generalize to unseen interaction semantics; (4) Affordance transfer evaluation with fine-tuning protocol: (a) zero-shot application of the VLA-learned affordance decoder on AGD20K/UMD as an exploratory experiment assessing cross-domain affordance quality, and (b) fine-tuning only the affordance decoder on AGD20K while freezing the VLA backbone, testing whether VLA-learned representations provide useful initialization vs. training from scratch — this addresses the large sim-to-real domain gap; (5) Qualitative affordance map visualization and contact-point prediction accuracy on held-out LIBERO episodes. **Baselines**: (a) OpenVLA-OFT (vanilla, no affordance) — 97.1% LIBERO standard; (b) OpenVLA-OFT + RSS-style action-level paraphrase invariance (our reimplementation); (c) OpenVLA-OFT + Spatial Forcing (intermediate 3D alignment with VGGT teacher) — 98.5% LIBERO average; (d) PALM (semi-automated affordance annotation) — 91.8% LIBERO-Long; (e) ST4VLA (web-scale spatial grounding) — 95.9% LIBERO average; (f) INTRA affordance maps + OpenVLA-OFT policy (two-stage); (g) CoA-VLA (supervised affordance). Key comparison axis: standard LIBERO performance may be competitive but not necessarily SOTA (Spatial Forcing at 98.5% is hard to beat without 3D teachers); our primary advantage claims are on (i) LIBERO-Para paraphrase robustness where explicit invariance training should outperform emergent robustness, (ii) zero-shot novel object/interaction generalization where annotation-free affordance transfer should outperform annotation-dependent methods in out-of-distribution settings, and (iii) annotation efficiency — competitive performance without any affordance labels, web-scale data, or foundation model teachers. **Key hypotheses**: (a) Explicit paraphrase invariance at the spatial affordance level provides better PRIDE scores on LIBERO-Para than ST4VLA's emergent robustness from spatial grounding or RSS's action-level invariance; (b) Self-supervised cross-object affordance transfer enables superior zero-shot generalization to novel objects compared to methods that learn object-specific supervised affordance features (PALM, SG-VLA); (c) Despite requiring no external supervision, AffordInvar achieves within 2-3 percentage points of supervised spatial methods (PALM, ST4VLA) on standard LIBERO, demonstrating that self-supervision closes most of the gap; (d) VLA-learned affordance representations provide useful initialization for downstream affordance benchmarks, demonstrated by faster convergence when fine-tuning the decoder on AGD20K vs. training from scratch.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180-200h H100 80GB (8-9 training runs at ~20-22h each: 2 main method runs, 2 baseline reproductions including Spatial Forcing and RSS reimplementation, 4 ablation runs for L_consist-only/L_transfer-only/no-gating/decoder-depth, 1 hyperparameter tuning run)",
      "gpu_utilization": "~30-35% effective utilization — human iteration time between runs for debugging and analysis",
      "timeline": "8-10 weeks (2 weeks codebase setup + paraphrase generation + baseline reproduction, 4-5 weeks experimentation including LIBERO-Para evaluation and AGD20K fine-tuning, 2-3 weeks paper writing)",
      "team": "1-2 researchers with VLA fine-tuning experience",
      "estimated_gpu_cost": "~$600-$700 (200h x $3.50/hr on-demand H100, or ~$400-$500 with spot pricing)"
    },
    "human_in_loop": {
      "gpu_hours": "~190-200h H100 80GB (agent manages experiment scheduling with slightly more efficient ablation design)",
      "gpu_utilization": "~60-70% — agent queues next experiment after prior run, human approves loss hyperparameters and reviews affordance heatmap quality at checkpoints",
      "timeline": "5-7 weeks (agent handles implementation and experiment orchestration; human reviews loss weight schedules and affordance map quality daily ~1hr)",
      "team": "1 researcher, ~1hr/day check-in",
      "claude_api_cost": "$100-200 (1,000-2,000 Opus turns for code generation, experiment design, result analysis)",
      "estimated_gpu_cost": "~$600-$700 (200h x $3.50/hr)",
      "risk_note": "Affordance consistency loss hyperparameters (alpha, beta) are sensitive — human review of affordance heatmaps after first 2-3 runs is critical to detect degenerate solutions (uniform or collapsed maps) early and adjust entropy regularization strength"
    },
    "auto_research": {
      "gpu_hours": "~200h H100 80GB (hard budget cap; agent maximizes information per run via sequential Bayesian hyperparameter optimization over alpha, beta, lambda_H, LoRA rank, and decoder depth)",
      "gpu_utilization": "~90-95% — agent immediately launches next experiment upon completion, no human wait time",
      "timeline": "2-3 weeks with 4 H100 GPUs (parallel ablation pairs reduce wall-clock time; includes evaluation and paper draft)",
      "team": "0 researchers after initial ~2hr setup (repo clone, API keys, compute allocation)",
      "claude_api_cost": "$200-400 (2,000-4,000 Opus turns for autonomous code development, ~9 experiment configurations, analysis, and paper writing)",
      "estimated_gpu_cost": "~$600-$700 (200h x $3.50/hr)",
      "speed_bottleneck": "GPU count is primary bottleneck — with 4 H100s, parallel ablation pairs complete in 2-3 weeks; with only 2 H100s, extends to 4-5 weeks",
      "risk_note": "Without human oversight, agent may waste ~20-30% of compute budget exploring suboptimal loss weight configurations before discovering effective entropy regularization settings — Bayesian optimization mitigates but does not eliminate this risk"
    }
  },
  "target_venues": [
    "AAAI 2027 (abstracts July 21, full paper July 28, 2026 — primary target, ~10 weeks from today, feasible in human-in-loop or auto-research modes)",
    "ICRA 2027 (estimated deadline ~September 15, 2026 — flagship robotics venue, comfortable timeline, natural fit for manipulation-focused contribution)",
    "ICLR 2027 (estimated deadline ~October 2026 — top-tier ML venue, strongest signal for self-supervised learning methodology contribution)",
    "CoRL 2027 (estimated deadline ~June 2027 — if additional real-robot experiments are needed for strongest submission)"
  ],
  "level": "top-tier",
  "key_references": [
    "ST4VLA: Spatially Guided Training for Vision-Language-Action Models — spatial priors (point, box, trajectory) from web-scale grounding data, 95.9% LIBERO average, emergent paraphrase robustness (ICLR 2026, arXiv 2602.10109)",
    "PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation — 4 supervised affordance types with semi-automated annotation (GroundingDINO+SAM+SpatialVLM+RoboPoint+CoTracker), 91.8% LIBERO-Long (CVPR 2026, arXiv 2601.07060)",
    "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation — auxiliary decoders for grasp affordances and segmentation from simulator ground truth (arXiv 2603.22760, March 2026)",
    "Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model — intermediate VLA alignment with 3D foundation model (VGGT), 98.5% LIBERO average, 3.8x training speedup (ICLR 2026, arXiv 2510.12276)",
    "RoboMAP: More than A Point — adaptive affordance heatmaps for spatial grounding, 82% real-world success (arXiv 2510.10912, October 2025)",
    "Stable Language Guidance for Vision-Language-Action Models — RSS with Monte Carlo Syntactic Integration and Residual Affordance Steering (arXiv 2601.04052, January 2026)",
    "INTRA: Interaction Relationship-aware Weakly Supervised Affordance Grounding — text synonym augmentation with contrastive learning for affordance on AGD20K (ECCV 2024, arXiv 2409.06210)",
    "LangForce/BayesianVLA: Bayesian Decomposition of Vision Language Action Models via Latent Action Queries — Bayesian VLA instruction-following via PMI (arXiv 2601.15197, January 2026)",
    "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — 22-52pp drops under paraphrasing, PRIDE metric (arXiv 2603.28301, March 2026)",
    "OpenVLA: An Open-Source Vision-Language-Action Model (CoRL 2024)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success — OpenVLA-OFT (arXiv 2502.19645, February 2025)",
    "Improved Visual Grounding through Self-Consistent Explanations — SelfEQ paraphrase consistency for VLM grounding (CVPR 2024)",
    "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance (ICCV 2025, arXiv 2412.20451)",
    "GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning (arXiv 2602.04315, February 2026)",
    "RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (ICRA 2025, arXiv 2411.02704)",
    "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations — RobustVLA (ICLR 2026, arXiv 2510.00037)",
    "Context-Dependent Affordance Computation in Vision-Language Models — >90% lexical drift, stable latent factors (arXiv 2603.04419)",
    "VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (CoRL 2023, arXiv 2307.05973)",
    "OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding (arXiv 2404.11000, 2024)",
    "AffordanceSAM: Segment Anything Once More in Affordance Grounding — current SOTA on AGD20K (arXiv 2504.15650, April 2025)",
    "Weakly-Supervised Affordance Grounding Guided by Part-Level Semantic Priors — WSAG-PLSP (ICLR 2025, arXiv 2505.24103)",
    "Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation (arXiv 2603.16044, March 2026)",
    "Learning Affordance Grounding from Exocentric Images — AGD20K dataset (CVPR 2022)"
  ],
  "description": "AffordInvar introduces annotation-free spatial affordance learning within an end-to-end Vision-Language-Action model, addressing a critical gap in the rapidly maturing landscape of spatial VLA methods. Recent work has established that spatial representations within VLAs significantly improve manipulation: ST4VLA (ICLR 2026) achieves 95.9% LIBERO average via web-scale spatial grounding, Spatial Forcing (ICLR 2026) achieves 98.5% via 3D foundation model alignment, PALM (CVPR 2026) achieves 91.8% LIBERO-Long via 4 semi-automated affordance types, and SG-VLA (March 2026) co-trains affordance decoders with simulator ground truth. However, all these methods require external supervision — web-scale grounding data, multi-model annotation pipelines, simulator labels, or foundation model teachers — creating scaling bottlenecks for new environments and tasks. AffordInvar eliminates this supervision requirement entirely. Built on OpenVLA-OFT with LoRA, it adds a lightweight 8M-parameter transposed-convolution affordance decoder on intermediate VLA features (layer 18/32) producing 128x128 spatial heatmaps, trained via two complementary self-supervised signals requiring only robot demonstrations and LLM-generated paraphrases: (1) paraphrase invariance — symmetric KL divergence enforcing identical affordance maps across K=3 Qwen-3-generated instruction variants, extending SelfEQ (CVPR 2024) from general VLM grounding to VLA affordance and explicitly optimizing the instruction robustness that ST4VLA achieves only emergently, and (2) cross-object affordance transfer — InfoNCE contrastive loss on spatially-normalized affordance features across episodes with similar interactions but different objects, inspired by INTRA but operating on VLA-internal features. The affordance heatmap gates action prediction via learned element-wise modulation. Key advantages over existing spatial VLA methods: (a) no annotation pipeline (vs. PALM's GroundingDINO+SAM+SpatialVLM+RoboPoint+CoTracker), no web-scale data (vs. ST4VLA's RefCOCO), no simulator labels (vs. SG-VLA), no 3D teachers (vs. Spatial Forcing) — only robot demonstrations + LLM paraphrases; (b) explicit paraphrase invariance optimization at the spatial level, unlike any existing spatial VLA method; (c) interpretable affordance maps independently evaluable on standard benchmarks. Evaluated on LIBERO-Long, LIBERO-Para (first spatial VLA method evaluated on paraphrase robustness via PRIDE metric), held-out interaction types, and AGD20K via fine-tuning protocol. Primary claims: superior LIBERO-Para PRIDE scores over emergent robustness (ST4VLA) and action-level invariance (RSS); competitive standard LIBERO performance without any affordance annotations; superior zero-shot novel object generalization via annotation-free affordance transfer. Baselines include OpenVLA-OFT, Spatial Forcing, PALM, ST4VLA, RSS-style action invariance, and CoA-VLA. Designed for <=200 H100-hours via LoRA efficiency.",
  "project_name": "afford_invar_vla",
  "source": "web_research"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00f3d1c8-395f-4059-a267-e1cd68e26f3b",
  "isSidechain": true,
  "agentId": "aaba1fc60cb524cf3",
  "requestId": "req_011CbAh9ryynT8yfwY42FNTt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b47febff-556a-4410-98b8-3e7b92b5c0db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "c4f4c7ec-c601-4d53-8881-5c7ea4ffd775",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTsZwQHBiBy2Hz32pUhz8Y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15526,
      "cache_read_input_tokens": 0,
      "output_tokens": 6673,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15526
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 6673,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15526,
            "ephemeral_1h_input_tokens": 0
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
