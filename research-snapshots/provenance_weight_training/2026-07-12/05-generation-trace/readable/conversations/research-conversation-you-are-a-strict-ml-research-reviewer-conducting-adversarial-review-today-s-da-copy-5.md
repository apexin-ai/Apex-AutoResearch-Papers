# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/35409173-1548-4aab-9fc6-05a4f1970257.jsonl`
- **Structured JSON:** [`e36b1ebc5ceb6fdf9c53.json`](../../sessions/e3/e36b1ebc5ceb6fdf9c53.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T20:21:53.965Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T20:21:53.965Z",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: Generative models specifically targeting HUMANOID robot training data — addressing the high-DoF, whole-body, loco-manipulation data scarcity that bottlenecks humanoid VLA / WM training. SCOPE LIMITED TO TWO CONTRIBUTION TYPES:\n  (a) Generation ALGORITHMS — e.g., video diffusion conditioned on humanoid action streams, action-conditioned generative models, latent humanoid trajectory generators, physics-aware whole-body video generation.\n  (b) Procedural data-generation PIPELINES — e.g., MimicGen-style automated demo multiplication for humanoids, procedural whole-body task/scene generation, automated quality filtering pipelines for synthetic humanoid trajectories.\n\nOUT OF SCOPE: action retargeting innovations (human-video → humanoid-action retargeting). Treat existing retargeters (HumanPlus, OmniH2O) as black-box upstream tools if needed; do NOT propose new retargeting methods.\n\nRecent landscape (do not duplicate): NVIDIA GR00T-Dreams, DexMimicGen, MimicGen extensions for humanoid, Helix self-supervised humanoid pipelines, Cosmos for synthetic humanoid video. Humanoid data scarcity is the #1 bottleneck cited in 2026 humanoid papers — high impact area.\n\nContribution type: METHOD ONLY. New generation algorithm OR new procedural pipeline. Not a new released humanoid dataset alone.\n\nSIM-ONLY MITIGATION: Validate generated data by training a downstream humanoid policy/VLA in sim and comparing against models trained on baseline data. Frame contribution as method, not dataset.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Strategies: (a) fine-tune existing video diffusion (CogVideoX, OpenSora, Cosmos) with humanoid-action conditioning, (b) procedural pipeline that requires negligible training compute, (c) small efficient humanoid-specific generator that beats general baselines.\n2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos, Isaac Lab humanoid suite (G1, H1), MimicGen, RoboCasa with humanoid embodiments if available.\n3. Eval: train humanoid policy/VLA on generated vs baseline data. Test on Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench. Report success rate + data efficiency curves.\n\nLook for: physics-aware whole-body video generation with kinematic consistency, action-conditioned generators that exploit humanoid kinematic structure, procedural pipelines that produce diverse loco-manipulation (not just static manipulation) data, automatic quality filtering for synthetic humanoid trajectories. Avoid: any retargeting-based contribution, arm-only generation rebadged as humanoid, naive fine-tuning of video diffusion on humanoid clips without method.\n\nTag: direction=humanoid_data_gen, contribution_type=method. target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 7/10)\n{\n  \"title\": \"Can Humanoid Motion Diffusion Models Compose? Body-Part Inpainting for Diverse Loco-Manipulation Trajectories\",\n  \"core_problem\": \"Generating diverse, physically plausible whole-body humanoid loco-manipulation demonstrations by compositionally mixing locomotion and manipulation behaviors remains unsolved in robot joint-space. DreamControl-v2 (arXiv 2604.00202, March 2026) validates that diffusion-generated reference trajectories can train robust RL policies for G1 humanoid skills (91-100% success across 8 tasks), but relies on monolithic text-conditioned generation — the diversity of downstream trajectories is bounded by the training data distribution, with no mechanism for combinatorial composition of locomotion and manipulation behaviors. Human-motion compositional methods (FrankenMotion, MixerMDM, Motion-Adapter) decompose by semantic body groups but operate in SMPL space without physics validation or downstream robot policy evaluation; FrankenMotion further documents that naive body-part composition produces 'unsmooth transitions.' MixerMDM (CVPR 2025) learns to compose frozen diffusion models at the body-joint level via spatial mixing weights, but operates in human motion space, uses simultaneous blending of frozen models (not conditioned generation), and does not evaluate downstream RL performance. MaskedMimic (SIGGRAPH Asia 2024) and MaskedManipulator (SIGGRAPH Asia 2025) pioneer random body-part masking for physics-based character control via RL + distillation, but use C-VAE/RL architectures (not diffusion), train from scratch (not fine-tuning pre-trained models), and produce real-time controllers rather than trajectory datasets for downstream RL. Robot-side generators like Kimodo (NVIDIA, March 2026) produce high-quality G1 motions from text and support kinematic constraint conditioning via imputation, but its constraint system was trained exclusively with end-effector and keyframe patterns — body-part-level masks are out-of-distribution. A critical and previously unaddressed complication is Kimodo's dual classifier-free guidance (w_text=2, w_constr=2): recent literature (CFG++, ICLR 2025; S-CFG, CVPR 2024) demonstrates that CFG extrapolation pushes samples off the data manifold, and dual guidance with OOD constraint patterns risks compounding this effect — the constraint guidance signal D_constr may itself be unreliable for OOD masks, and amplifying it via w_constr>0 could produce severe artifacts. Can we exploit Kimodo's imputation-based constraint mechanism — disentangling the contributions of imputation (mask replacement at each denoising step, following RePaint's mask-agnostic principle) versus guidance (CFG amplification of constraint adherence, which may be counterproductive for OOD patterns) — with URDF-guided body-part factorization and optional LoRA adaptation, to enable compositional loco-manipulation trajectory generation that achieves greater diversity and downstream RL policy quality than monolithic text-conditioned generation?\",\n  \"opportunity\": \"A key insight is that Kimodo's imputation-based constraint mechanism is mathematically equivalent to RePaint-style inpainting: at each denoising step, constrained joints are replaced with (noised) target values while unconstrained joints are generated freely. RePaint (CVPR 2022) demonstrated that this imputation mechanism generalizes to arbitrary mask patterns — including those never seen during training — because it operates at the level of individual denoising steps rather than requiring mask-pattern-specific learned representations. CondMDI (SIGGRAPH 2024) provides additional supporting evidence in the motion domain: it trains with randomly sampled joints and keyframes and achieves strong generalization to various spatial constraint patterns, demonstrating that motion diffusion models can handle diverse mask configurations. However, a critical caveat applies: Kimodo's Phase 2 training uses specific constraint patterns (full-body keyframes, random subsets of hands/feet positions/rotations, 2D root position/heading, foot contact configurations), and body-part-level masking (e.g., 'fix all lower-body joints while generating upper-body') was NEVER in its training distribution. Furthermore, Kimodo employs dual classifier-free guidance with formula x̂₀ = D∅ + w_text(D_text - D∅) + w_constr(D_constr - D∅), where D_constr is the model's output conditioned only on constraints. When constraints are OOD, D_constr may be unreliable, and amplifying it via w_constr=2 risks off-manifold artifacts — a failure mode documented by CFG++ (Chung et al., ICLR 2025), which shows standard CFG extrapolation pushes samples off the data manifold, and by S-CFG (Shen et al., CVPR 2024), which demonstrates spatial inconsistency from uniform guidance scaling across semantically distinct regions. A crucial experimental variable is therefore w_constr itself: setting w_constr=0 reduces constraint influence to pure imputation (RePaint-style, no guidance amplification), which may actually work BETTER for OOD body-part patterns than guided generation, since the imputation mechanism does not require in-distribution constraint patterns while the guidance signal does.\\n\\nBeyond the empirical OOD question, our methodological choice of iterative conditional generation — running sequential complete diffusion processes rather than composing scores within a single denoising loop — is itself a principled contribution motivated by the compositional diffusion failure literature. Score-composition approaches (MixerMDM, EnergyMoGen, CompDiffuser) assume approximate factorization of the joint distribution, but Bradley et al. (ICML 2025) prove this requires approximate independence between composed components — violated for kinematically coupled body parts. Naive score composition also suffers from mode-averaging when local distributions are multimodal (RCD, arXiv 2605.03075, May 2026) and produces 'unsmooth transitions' at body-part boundaries (FrankenMotion, Jan 2026). Iterative conditional generation avoids all three failure modes: each body-part generation is a complete diffusion process sampling from the true conditional p(upper|lower,text_manip) or p(lower|upper,text_loco), with no factorization assumption, no mode-averaging within the denoising loop, and full-trajectory coherence within each generated part.\\n\\nKimodo's G1-SEED-v1 checkpoint (282M parameters, trained on 288h BONES-SEED data) and its complete training hyperparameters are publicly documented: T=1000 diffusion steps, Adam-atan2 optimizer at lr=2e-5, Smooth L1 loss with per-component weights, EMA every 10 steps with decay 0.995, 6D rotation representation, and a two-stage transformer denoiser (16 layers, 8 heads, dim 1024). Kimodo's public repository provides ONLY inference code — no training scripts, data loaders, or fine-tuning infrastructure. The zero-shot iterative conditional generation pipeline requires only Kimodo's inference API with its imputation mechanism. For the LoRA secondary contribution, we implement fine-tuning from the inference codebase using documented hyperparameters. All infrastructure exists: (1) Kimodo G1-SEED-v1 provides the backbone; (2) BONES-SEED provides 288h of G1-retargeted motions with up to 6 NL descriptions per motion plus temporal segmentation; (3) OmniRetarget provides 4.0h of publicly available G1 loco-manipulation trajectories (3.0h robot-object + 0.5h robot-terrain + 0.5h robot-object-terrain); (4) ProtoMotions provides GPU-accelerated kinematic-to-dynamic conversion; (5) SkillBench provides 8 G1 loco-manipulation tasks with evaluation metrics.\",\n  \"landscape\": \"**Diffusion→trajectories→RL pipeline for G1 (direct paradigm validation):** DreamControl-v2 (arXiv 2604.00202, March 2026) is the most directly relevant prior work — it trains a guided diffusion model directly in G1's motion space using retargeted human motion data (AMASS, GRAB, Nymeria, OmniRetarget; 29.6K samples), generates reference trajectories conditioned on text and spatio-temporal controls, and trains downstream RL policies achieving 91-100% success across 8 tasks on real G1 hardware. Critically, DreamControl-v2 uses monolithic text-conditioned generation with no body-part compositional mechanism — trajectory diversity is bounded by training data. Our work extends this validated paradigm with compositional body-part generation: URDF-factored iterative conditioning enables N_loco × N_manip diverse trajectories from a single pre-trained model, targeting the diversity bottleneck that DreamControl-v2 does not address. DreamControl-v1 (arXiv 2509.14353) used an off-the-shelf human-space diffusion model with IK, requiring manual trajectory filtering; v2's robot-space training eliminates this, paralleling our use of Kimodo's robot-space model. Zhang et al. (arXiv 2604.17335, ETH Zurich, April 2026) concurrently validate the diffusion→tracking→RL pipeline for whole-body humanoid locomotion, training a diffusion model on retargeted human motions for terrain-aware reference generation with RL-based tracking, targeting terrain-adaptive locomotion rather than compositional loco-manipulation.\\n\\n**Body-part compositional motion diffusion (human motion space):** MixerMDM (CVPR 2025, arXiv 2504.01019) is the closest prior art for body-part composition — it learns spatial mixing weights (per-joint, per-timestep) to blend denoising outputs of two frozen pre-trained motion diffusion models. Key differences: MixerMDM composes *frozen* models via simultaneous weighted blending (score composition), operates in SMPL/HumanML3D space, and evaluates motion quality metrics (FID, alignment) rather than downstream RL policy performance. FrankenMotion (arXiv 2601.10909, Jan 2026) trains a diffusion model with part-level temporally-structured text prompts in SMPL space — critically, they found that naive body-part composition produces 'unsmooth transitions,' motivating purpose-built part-level training. Motion-Adapter (arXiv 2604.16135, April 2026) addresses compound action synthesis via attention-mask-guided denoising. CompDiffuser (NeurIPS 2025 Spotlight, arXiv 2503.05153) achieves compositional trajectory stitching through temporal overlap and bidirectional diffusion — a temporal analog to our spatial body-part approach. EnergyMoGen (CVPR 2025) and DeMoGen (arXiv 2512.22324, Dec 2025) compose motions via energy-based diffusion. All operate in human motion space without physics validation or robot RL evaluation, and all employ score-composition approaches that suffer from the documented failure modes (mode-averaging, factorization violations, boundary artifacts) that our iterative conditional generation avoids.\\n\\n**Physics-based masked motion controllers (NVIDIA):** MaskedMimic (SIGGRAPH Asia 2024, arXiv 2409.14393) formulates physics-based character control as motion inpainting via random body-part masking. MaskedManipulator (SIGGRAPH Asia 2025, arXiv 2505.19086) extends MaskedMimic to whole-body loco-manipulation. Both use C-VAE/RL architectures (not diffusion), train from scratch via RL+distillation, and produce real-time controllers rather than trajectory datasets. Our work brings MaskedMimic's masking insight into the diffusion paradigm on a pre-trained robot-specific model.\\n\\n**Diffusion-based humanoid control with inpainting:** BeyondMimic (arXiv 2508.08241, UC Berkeley) proposes a unified latent diffusion model for humanoid control that supports motion inpainting, skill composition, and dynamic behavior switching via classifier guidance, with zero-shot sim-to-real transfer. While it targets real-time control rather than trajectory dataset generation for downstream RL, its diffusion-based inpainting and composition approach validates that diffusion models can generalize to novel conditioning patterns at inference time.\\n\\n**Robot motion diffusion (G1-specific):** Kimodo (NVIDIA, arXiv 2603.15546, March 2026) is a 282M-parameter two-stage transformer denoiser trained on 288h BONES-SEED (SEED variant), generating G1 motions from text in 2-5s. Its constraint conditioning uses binary masking with imputation and dual classifier-free guidance (x̂₀ = D∅ + w_text(D_text - D∅) + w_constr(D_constr - D∅), default w_text=w_constr=2). Phase 2 training uses specific constraint patterns: full-body keyframes, random subsets of hands/feet positions/rotations, 2D root position/heading, foot contact configurations. Body-part-level masks are NOT in its training distribution — our use of body-part masking is OOD and constitutes an empirical hypothesis. MotionBricks (NVIDIA, arXiv 2604.24833, April 2026) provides real-time latent generative motion for G1 with training code, but uses VQVAE + latent backbone (not diffusion). REFINE-DP (arXiv 2603.13707, March 2026) demonstrates diffusion policy fine-tuning via RL for humanoid loco-manipulation but does not address compositional generation. Psi0 (arXiv 2603.12263, March 2026) is a VLA foundation model using flow-based action prediction. WholeBodyVLA (ICLR 2026) proposes a unified latent VLA for whole-body loco-manipulation control using vision-language-action learning from egocentric videos, but does not use diffusion-based trajectory generation.\\n\\n**Mask-agnostic diffusion inpainting:** RePaint (CVPR 2022, arXiv 2201.09865) demonstrated that pre-trained DDPMs can perform inpainting with arbitrary binary masks — including patterns never seen during training — by replacing masked regions with noised target values at each denoising step. Its resampling trick (re-noising and re-denoising at mask boundaries) improves coherence at the cost of additional denoising steps. CondMDI (SIGGRAPH 2024, arXiv 2405.11126) applies imputation-based conditioning to motion in-betweening, training with randomly sampled joints and keyframes, and demonstrating generalization to various spatial constraint patterns including single-joint trajectories — providing domain-specific evidence for mask-pattern generalization in motion diffusion. We adopt the imputation principle for body-part conditioning: Kimodo's imputation mechanism (x̃_t = m ⊙ x_gt + (1-m) ⊙ x_t) is structurally identical to RePaint's approach. Whether this generalizes from image DDPMs and human-motion diffusion to Kimodo's robot-specific transformer with dual CFG is our central empirical question.\\n\\n**Classifier-free guidance failure modes (motivating w_constr sweep):** CFG++ (Chung et al., ICLR 2025, arXiv 2406.08070) reveals that standard CFG's drawbacks — lack of invertibility and mode collapse at high guidance scales — stem from off-manifold extrapolation, and proposes manifold-constrained guidance via inverse-problem reformulation. S-CFG (Shen et al., CVPR 2024, arXiv 2404.05384) demonstrates that a global CFG scale creates spatial inconsistency across semantically distinct regions, proposing per-region adaptive guidance. Annealing Guidance (Yehezkel et al., SIGGRAPH Asia 2025, arXiv 2506.24108) proposes learning a dynamic schedule that adapts guidance scale throughout denoising. These works collectively motivate our experimental design: for OOD body-part masks, constraint guidance (w_constr>0) may amplify unreliable D_constr predictions, pushing trajectories off-manifold. Testing w_constr ∈ {0, 0.5, 1.0, 2.0} disentangles the contributions of imputation (mask-agnostic, theoretically robust to OOD) versus guidance (distribution-dependent, potentially harmful for OOD).\\n\\n**Compositional diffusion theory:** Reduce Reuse Recycle (Du et al., ICML 2023) identifies bias in naive score composition and proposes MCMC correction. Mechanisms of Projective Composition (Bradley et al., ICML 2025) proves score composition requires approximate factorization — violated for kinematically coupled body parts. Refining Compositional Diffusion (arXiv 2605.03075, May 2026) documents mode-averaging in compositional diffusion planning. These works provide the theoretical motivation for our iterative conditional generation approach (sequential complete processes) over score composition (simultaneous/alternating within one process).\\n\\n**LoRA fine-tuning for diffusion models:** LoRA (Hu et al., ICLR 2022) is standard for parameter-efficient fine-tuning of diffusion transformers. We apply LoRA to Kimodo's attention layers for the first time.\\n\\n**Data generation for humanoid RL:** OmniRetarget (arXiv 2509.26633) provides 4.0h of publicly available G1 loco-manipulation trajectories. ProtoMotions provides GPU-accelerated physics tracking for G1.\\n\\nNo existing work uses a pre-trained robot motion diffusion model's imputation mechanism for systematic body-part compositional trajectory generation — disentangling imputation from guidance for OOD constraints, with iterative conditional generation as a principled alternative to score composition — followed by physics projection and downstream RL evaluation. DreamControl-v2 validates the pipeline paradigm; we extend it with compositional generation. The iterative conditional generation methodology is differentiated from all prior compositional approaches, which use score composition.\",\n  \"approach\": \"We propose a framework testing whether Kimodo's imputation-based constraint conditioning generalizes to URDF-guided body-part masks for compositional loco-manipulation trajectory generation — an OOD application of RePaint-style inpainting principles to robot motion diffusion. The central methodological contribution is iterative conditional generation: unlike score-composition approaches (MixerMDM, EnergyMoGen, CompDiffuser) that compose body parts within a single denoising loop — suffering from mode-averaging (RCD, 2026), factorization violations (Bradley et al., ICML 2025), and boundary artifacts (FrankenMotion, 2026) — we run each body-part as a complete, independent diffusion process conditioned on the other's output, sampling from true conditionals rather than approximate factored distributions. The framework has two tiers: a zero-shot pipeline (primary contribution) that requires only Kimodo's inference API, and LoRA-enhanced generation (secondary contribution) that improves conditional quality via lightweight fine-tuning.\\n\\n**0. Preliminary Diversity and Guidance Analysis (Day 1-3).** Before the main pipeline, we establish (a) the empirical case for compositional generation over monolithic text prompting and (b) the interaction between constraint guidance and OOD body-part masks.\\n\\n  Diversity analysis: We generate N_text=50 compound text-prompted motions from Kimodo (e.g., 'walk toward the shelf while raising your right hand,' 'jog forward while waving both arms') and N_comp=50 compositionally generated motions (5 locomotion prompts × 10 manipulation prompts) using the zero-shot pipeline. Pre-registered success criterion: compositional generation is justified if mean pairwise joint-angle distance of compositional samples exceeds that of compound-text samples by >15% (or >1 standard deviation of the text-prompted distribution), measured via two-sided permutation test with 10,000 permutations at p<0.05. With N=50 per group and effect size d≥0.6, a permutation test achieves >80% power. If this criterion is not met, we pivot to analyzing when/why compositional generation fails — itself a valuable contribution that informs the field.\\n\\n  Guidance disentanglement: We test constraint guidance weight w_constr ∈ {0, 0.5, 1.0, 2.0} for body-part masks across all 50 compositional samples. This disentangles the contributions of imputation (mask replacement at each denoising step, theoretically robust to OOD per RePaint) versus guidance (CFG amplification of constraint adherence via D_constr, distribution-dependent and potentially counterproductive for OOD patterns). We hypothesize that w_constr=0 (pure imputation, no guidance) may outperform w_constr=2 (default) for OOD body-part masks, because: (a) with OOD constraints, D_constr (model output conditioned only on constraints) may be unreliable, and amplifying unreliable predictions via w_constr>0 pushes trajectories off-manifold (CFG++, ICLR 2025); (b) pure imputation does not require the constraint pattern to be in-distribution — it only requires the denoiser to produce locally coherent predictions at each step given the imputed values. We report: tracking success rate (ProtoMotions), joint-angle coherence at body-part boundaries, and generation FID for each w_constr setting. The best-performing w_constr is carried forward to full evaluation.\\n\\n**1. URDF-Guided Body-Part Factorization.** We parse the G1 URDF to define two kinematic subtrees: a lower-body group (root/pelvis, hips, knees, ankles, feet — locomotion, including boundary joints at the lower torso) and an upper-body group (torso, shoulders, elbows, wrists, hands — manipulation). This determines which of the 34 G1 joints are constrained vs. generated in each phase. The factorization is encoded as binary masks compatible with Kimodo's imputation format.\\n\\n**2. Iterative Conditional Generation with RePaint-Style Imputation (Primary Contribution).** We frame body-part composition as iterative conditional generation — a principled alternative to score composition for structured body-part composition, motivated by the compositional diffusion failure literature. Instead of composing scores within the denoising loop — which assumes approximate factorization (Bradley et al., ICML 2025), suffers from mode-averaging when local distributions are multimodal (RCD, 2026), and produces boundary artifacts (FrankenMotion, 2026) — we run sequential complete diffusion processes, each sampling from the true conditional distribution:\\n\\n  Phase 1 (Locomotion): Generate lower-body trajectory via Kimodo's full denoising (T=1000 steps) with locomotion text prompt and upper-body unconstrained.\\n\\n  Phase 2 (Manipulation): Generate upper-body trajectory via a second complete denoising with manipulation text prompt and lower-body joints fixed as constraints using Kimodo's imputation mechanism (x̃_t = m ⊙ x_lower + (1-m) ⊙ x_t). Constraint guidance weight w_constr is set to the value selected in the Day 1-3 analysis (we expect w_constr=0 for OOD masks based on the CFG off-manifold hypothesis). This generates from p(x_upper | x_lower, text_manip) — no factorization assumption needed.\\n\\n  Phase 2b (RePaint Resampling Variant): Following RePaint's resampling trick, we optionally add r=5-10 noise-denoise cycles at each denoising step near the body-part boundary (lower torso/pelvis joints), improving coherence between independently generated body parts. This costs r× more denoising steps at boundary joints but is trivial to implement with Kimodo's inference API.\\n\\n  Phase 3 (Optional Refinement): Re-generate lower-body conditioned on upper-body output, sampling from p(x_lower | x_upper, text_loco). 1-2 iterations suffice.\\n\\nDiversity is achieved by sampling different locomotion × manipulation combinations — the combinatorial product yields exponentially more compositions than exist in training data. The zero-shot pipeline requires NO modifications to Kimodo's code — only its public inference API with constraint inputs.\\n\\n**3. LoRA-Based Masked Fine-Tuning (Secondary Contribution).** While the zero-shot pipeline tests OOD generalization, LoRA fine-tuning can bring body-part conditioning into the training distribution, improving conditional quality. We implement a training loop from Kimodo's inference codebase — realistic scope is 500-800 lines of non-trivial PyTorch code covering:\\n\\n  (a) Data loading: BONES-SEED format parsing (motion representation with 6D rotations, smoothed root, temporal annotations) and OmniRetarget integration.\\n  (b) LoRA injection: Rank-16 adapters into query/key/value projections of 16 transformer layers (~8M trainable parameters, ~3% of 282M total).\\n  (c) Masked denoising objective: With probability p_mask=0.5, replace either upper-body or lower-body joint channels with Gaussian noise while preserving the other part's clean signal, computing loss only on masked joints. This directly trains the conditional distributions p(upper|lower,text_manip) and p(lower|upper,text_loco).\\n  (d) Body-part text annotations: BONES-SEED includes up to 6 NL descriptions per motion plus temporal segmentation with precise timestamps. We derive body-part-specific labels via: (i) parsing existing descriptions for body-part keywords ('walking' → lower, 'reaching' → upper); (ii) supplementing with per-body-part joint velocity statistics via LLM prompting for ambiguous cases; (iii) manually verifying 100 random annotations against motion visualizations.\\n  (e) Optimizer and training: Adam-atan2, lr=2e-5, Smooth L1 loss with published per-component weights, EMA decay 0.995. Training on BONES-SEED (288h, 142K motions) + OmniRetarget (4.0h).\\n\\n  No physics training losses: Physics consistency is handled entirely by post-generation projection.\\n\\n  Budget: 4-6 days for implementation, ~8-12h on 1×A100 for training.\\n\\n**4. Post-Composition Physics Projection.** After iterative conditional generation, a lightweight quadratic program (~0.1s per trajectory) optimizes for: (a) centroidal dynamics consistency between upper and lower body; (b) CoM within support polygon; (c) G1 joint torque limits from URDF. Trajectories failing projection (>5% of joints exceeding limits) are rejected and re-sampled.\\n\\n**5. Kinematic-to-Dynamic Pipeline.** Projected trajectories are converted to physics-validated RL demonstrations via ProtoMotions' GPU-accelerated tracking. Tracking success rate serves as a physics quality metric.\\n\\n**6. Evaluation on SkillBench (3 Tasks).** We evaluate on 3 SkillBench G1 tasks spanning difficulty levels: FarReach (Easy), BoxPush (Medium), PackageCarry (Hard). Baselines:\\n  (1) **DreamControl-v2** — the primary paradigm baseline: diffusion→trajectories→RL with monolithic text conditioning (no body-part composition). We use their published results or reproduce using their pipeline.\\n  (2) **Kimodo text-prompted** — compound text prompts (e.g., 'walk forward while reaching'). Tests whether Kimodo's LLM2Vec text encoding already handles compound prompts well enough.\\n  (3) **Zero-shot iterative conditioning (w_constr=0, no resampling)** — our pipeline with pure imputation (no constraint guidance); isolates the value of imputation-only body-part factorization.\\n  (4) **Zero-shot iterative conditioning (best w_constr from analysis)** — if w_constr>0 is selected, this tests whether guidance helps; if w_constr=0 wins, baselines 3 and 4 collapse.\\n  (5) **Zero-shot + RePaint resampling** — adds noise-denoise cycles at body-part boundaries; tests whether resampling improves coherence.\\n  (6) **LoRA-enhanced iterative generation** — our full pipeline; isolates the value of LoRA fine-tuning.\\n  (7) **OmniRetarget** — optimization-based G1 trajectories (4.0h available).\\n  (8) **Naive concatenation** — lower-body from one sample + upper-body from another, no conditioning (ablation).\\n\\n  Key metrics: downstream RL policy success rate (primary), trajectory diversity (mean pairwise distance in joint-angle space), physics violation rate (ProtoMotions tracking failure rate), and data efficiency curve.\\n\\n**Early Checkpoint (Day 8-10).** Before committing to full SkillBench evaluation, we evaluate: (a) zero-shot imputation quality across w_constr settings — does Kimodo produce coherent motions with body-part masks at any guidance level? If coherence is poor (<30% tracking success at all w_constr values), the OOD hypothesis is rejected and we focus the paper on the LoRA approach; (b) zero-shot vs. RePaint-resampled vs. LoRA-tuned conditional generation quality using FID and diversity metrics on held-out BONES-SEED motions. This checkpoint determines which variants to carry forward to full RL evaluation.\\n\\n**Possible Outcomes and Their Contributions:**\\n  (a) Zero-shot works well at w_constr=0 → demonstrates that pure imputation (without guidance) generalizes to OOD body-part masks in robot motion diffusion, and that guidance is counterproductive for OOD constraints. Novel finding with practical implications for constraint-based diffusion generation.\\n  (b) Zero-shot works at w_constr>0 → demonstrates that both imputation and guidance generalize to OOD, stronger than (a).\\n  (c) Zero-shot fails, LoRA succeeds → demonstrates that body-part conditioning requires explicit training but can be achieved efficiently via LoRA, with guidance disentanglement analysis informing the failure mode.\\n  (d) Both improve diversity but not RL performance → reveals that trajectory diversity alone is insufficient for downstream policy quality, an important negative result.\\n  (e) Compositional generation underperforms text-prompted → establishes empirical limits of factored generation, also valuable, with guidance analysis providing mechanistic explanation.\\n\\n**Key Differentiation.** From DreamControl-v2: compositional body-part generation enabling combinatorial diversity vs. monolithic text conditioning; uses pre-trained Kimodo (not custom-trained diffusion); tests OOD constraint generalization with guidance disentanglement. From MixerMDM: robot-specific model, LoRA fine-tuning, iterative conditional generation (not score composition), downstream RL evaluation. From MaskedMimic: diffusion not C-VAE/RL, LoRA fine-tune pre-trained model, trajectory datasets not real-time controllers. From BeyondMimic: trajectory dataset generation for downstream RL amplification vs. real-time latent diffusion control; URDF-structured body-part factorization vs. classifier-guided composition. Methodologically: iterative conditional generation (sequential complete processes) as a principled alternative to score composition, supported by the compositional diffusion failure literature and validated empirically.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~65-95h A100/H100\",\n      \"gpu_utilization\": \"High (65-75%): LoRA fine-tuning (~8-12h on 1 A100); iterative conditional generation with w_constr sweep uses Kimodo inference (4× conditions adds ~3h); ProtoMotions tracking established\",\n      \"timeline\": \"20-22 days\",\n      \"team\": \"1-2 researchers familiar with diffusion models and PyTorch LoRA\",\n      \"estimated_gpu_cost\": \"$195-285 (at ~$3.00/hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~75-105h A100/H100\",\n      \"gpu_utilization\": \"Moderate-high (55-65%): agent runs LoRA training, w_constr sweep, and evaluation; human reviews annotation quality and trajectory visualizations\",\n      \"timeline\": \"16-20 days — feasible for CoRL 2026 (16 days to abstract May 26, 19 to paper May 29)\",\n      \"team\": \"1 researcher, ~30min/day reviewing annotations and trajectory quality\",\n      \"claude_api_cost\": \"$30-80 (estimated 300-800 turns at ~$0.10/turn)\",\n      \"estimated_gpu_cost\": \"$225-315\",\n      \"risk_note\": \"Primary risk: zero-shot imputation may not generalize to body-part masks at ANY w_constr value (OOD failure across all guidance settings). Mitigation: (a) early checkpoint at Day 8-10 tests this directly with w_constr sweep; (b) pure imputation (w_constr=0) is the most theoretically grounded fallback; (c) RePaint resampling as boundary-coherence fallback; (d) LoRA fine-tuning as alternative that brings body-part masks into training distribution; (e) negative results (OOD failure analysis with guidance disentanglement) are themselves publishable. Secondary risk: LoRA training implementation takes 4-6 days (500-800 lines), consuming significant timeline. Mitigation: early checkpoint strategy determines whether LoRA is needed before full implementation.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~85-115h A100/H100\",\n      \"gpu_utilization\": \"Near-zero idle (<10%): w_constr sweep, LoRA fine-tuning, iterative generation, physics projection, ProtoMotions tracking, and SkillBench RL run back-to-back\",\n      \"timeline\": \"12-16 days with 2-4 concurrent A100 GPUs\",\n      \"team\": \"0 (initial setup: provide Kimodo G1-SEED-v1 checkpoint path, BONES-SEED data, SkillBench config)\",\n      \"claude_api_cost\": \"$80-180 (estimated 800-1800 turns)\",\n      \"estimated_gpu_cost\": \"$255-345\",\n      \"speed_bottleneck\": \"LoRA training implementation: 4-6 days (500-800 lines); LoRA fine-tuning: ~8-12h on 1×A100; SkillBench RL: ~15-25h per task on 1×A100, parallelized across 3 GPUs\",\n      \"risk_note\": \"Agent should run preliminary diversity+guidance analysis (Day 1-3) and early checkpoint evaluation (Day 8-10) comparing zero-shot across w_constr settings vs. resampled vs. LoRA conditional quality before committing to full SkillBench\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract deadline: May 26, 2026; paper deadline: May 29, 2026) — PRIMARY\",\n    \"Humanoids 2026 (paper deadline: July 24, 2026) — SECONDARY (extended version with full 8-task SkillBench, iterative refinement analysis, and additional ablations)\",\n    \"ICRA 2027 (paper deadline: September 16, 2026) — BACKUP\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Kimodo: Scaling Controllable Human Motion Generation (NVIDIA, arXiv 2603.15546, March 2026) — backbone model with imputation-based constraint conditioning and dual CFG (x̂₀ = D∅ + w_text(D_text - D∅) + w_constr(D_constr - D∅), default w_text=w_constr=2), G1-SEED-v1 checkpoint on HuggingFace. NOTE: public repo provides inference only, no training code. Body-part masks are OOD; w_constr interaction with OOD masks is a central experimental variable.\",\n    \"DreamControl-v2: Simpler and Scalable Autonomous Humanoid Skills via Trainable Guided Diffusion Priors (arXiv 2604.00202, March 2026) — validates diffusion→trajectories→RL pipeline for G1 with 91-100% success across 8 tasks; monolithic text conditioning without body-part composition; primary paradigm baseline\",\n    \"DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion (arXiv 2509.14353, 2025) — original version using human-space diffusion prior with manual filtering\",\n    \"RePaint: Inpainting using Denoising Diffusion Probabilistic Models (Lugmayr et al., CVPR 2022, arXiv 2201.09865) — demonstrates that pre-trained DDPMs generalize to arbitrary inpainting masks via step-by-step imputation without guidance; resampling trick improves boundary coherence; theoretical foundation for our pure-imputation (w_constr=0) approach to OOD body-part masking\",\n    \"CFG++: Manifold-Constrained Classifier Free Guidance for Diffusion Models (Chung et al., ICLR 2025, arXiv 2406.08070) — reveals that standard CFG extrapolation pushes samples off the data manifold, causing mode collapse and artifacts at high guidance scales; motivates our hypothesis that w_constr>0 may be counterproductive for OOD body-part constraints\",\n    \"Rethinking the Spatial Inconsistency in Classifier-Free Diffusion Guidance (Shen et al., CVPR 2024, arXiv 2404.05384) — demonstrates that uniform CFG scale creates spatial inconsistency across semantically distinct regions; proposes per-region adaptive guidance; motivates region-aware constraint guidance for body-part masks\",\n    \"Navigating with Annealing Guidance Scale in Diffusion Space (Yehezkel et al., SIGGRAPH Asia 2025, arXiv 2506.24108) — proposes learned dynamic guidance schedule adapting to denoising trajectory; alternative to fixed w_constr for future work\",\n    \"CondMDI: Flexible Motion In-betweening with Diffusion Models (Cohan et al., SIGGRAPH 2024, arXiv 2405.11126) — trains motion diffusion with randomly sampled joints and keyframes, demonstrating generalization to diverse spatial constraint patterns; domain-specific evidence for mask-pattern generalization in motion diffusion\",\n    \"MixerMDM: Learnable Composition of Human Motion Diffusion Models (CVPR 2025, arXiv 2504.01019) — closest prior art for body-part composition: learned spatial mixing weights via score composition in SMPL space; subject to mode-averaging and factorization violation failure modes\",\n    \"MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting (SIGGRAPH Asia 2024, arXiv 2409.14393) — body-part masking insight for conditional motion synthesis via C-VAE/RL\",\n    \"MaskedManipulator: Versatile Whole-Body Control for Loco-Manipulation (SIGGRAPH Asia 2025, arXiv 2505.19086) — extends MaskedMimic to loco-manipulation\",\n    \"BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion (arXiv 2508.08241, UC Berkeley) — unified latent diffusion for humanoid control with motion inpainting, skill composition, and classifier-guided generalization to unseen tasks; validates diffusion-based inference-time generalization\",\n    \"CompDiffuser: Generative Trajectory Stitching through Diffusion Composition (NeurIPS 2025 Spotlight, arXiv 2503.05153) — temporal compositional trajectory stitching via score composition; subject to documented failure modes\",\n    \"FrankenMotion: Part-level Human Motion Generation and Composition (arXiv 2601.10909, Jan 2026) — documents failure of naive body-part score composition ('unsmooth transitions') in SMPL space; motivates our iterative conditional generation approach\",\n    \"Motion-Adapter: A Diffusion Model Adapter for Text-to-Motion Generation of Compound Actions (arXiv 2604.16135, April 2026) — attention-mask-guided compound action synthesis\",\n    \"REFINE-DP: Diffusion Policy Fine-tuning for Humanoid Loco-manipulation via Reinforcement Learning (arXiv 2603.13707, March 2026) — RL fine-tuning of diffusion policies for humanoid control\",\n    \"MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model (NVIDIA, arXiv 2604.24833, April 2026) — sibling project to Kimodo with G1 training code, different architecture\",\n    \"Psi0: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (arXiv 2603.12263, March 2026) — VLA foundation model with flow-based action prediction\",\n    \"Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking (Zhang et al., arXiv 2604.17335, ETH Zurich, April 2026) — concurrent validation of diffusion→tracking→RL pipeline for terrain-aware G1 locomotion; targets locomotion not compositional loco-manipulation\",\n    \"WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026, arXiv 2512.11047) — unified VLA for humanoid loco-manipulation via egocentric video learning; different paradigm (VLA, not diffusion trajectory generation)\",\n    \"MDM: Human Motion Diffusion Model (Tevet et al., ICLR 2023, arXiv 2209.14916) — demonstrated spatial body-part inpainting in human motion diffusion via imputation; supports feasibility of body-part mask generalization\",\n    \"Reduce Reuse Recycle: Compositional Generation with Energy-Based Diffusion Models and MCMC (Du et al., ICML 2023) — identifies bias in naive score composition\",\n    \"Mechanisms of Projective Composition of Diffusion Models (Bradley et al., ICML 2025, arXiv 2502.04549) — proves score composition requires approximate factorization; violated for kinematically coupled body parts, motivating our iterative conditional generation\",\n    \"Refining Compositional Diffusion for Reliable Long-Horizon Planning (arXiv 2605.03075, May 2026) — documents mode-averaging in compositional diffusion planning; motivates sequential complete processes over within-loop composition\",\n    \"LoRA: Low-Rank Adaptation of Large Language Models (Hu et al., ICLR 2022) — parameter-efficient fine-tuning for transformers\",\n    \"BONES-SEED: Skeletal Everyday Embodiment Dataset (Bones Studio, March 2026) — 142K motions, 288h, up to 6 NL descriptions per motion, temporal segmentation, G1 retargeting on HuggingFace\",\n    \"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Loco-Manipulation (arXiv 2509.26633) — 4.0h publicly available G1 loco-manipulation data on HuggingFace\",\n    \"SkillBlender: Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending (arXiv 2506.09366, 2025) — SkillBench benchmark with 8 G1 tasks\",\n    \"ProtoMotions: GPU-Accelerated Simulation and Learning Framework (NVIDIA, open-source) — kinematic-to-dynamic tracking for G1\",\n    \"PhysDiff: Physics-Guided Human Motion Diffusion Model (NVIDIA, ICCV 2023) — physics-based motion projection during sampling\",\n    \"EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion (CVPR 2025)\",\n    \"DeMoGen: Decompositional Human Motion Generation with Energy-Based Diffusion (arXiv 2512.22324, Dec 2025)\",\n    \"Factorized Diffusion Policy: Flexible Multitask Learning (arXiv 2512.21898, RSS 2025 Workshop)\"\n  ],\n  \"description\": \"We address compositional generation of diverse, physically plausible humanoid loco-manipulation demonstrations by testing whether a pre-trained robot motion diffusion model's imputation-based constraint conditioning generalizes to URDF-guided body-part masks — an out-of-distribution application that we frame as RePaint-style inpainting in robot motion space. Our central methodological contribution is iterative conditional generation: unlike score-composition approaches (MixerMDM, EnergyMoGen, CompDiffuser) that compose body parts within a single denoising loop — suffering from mode-averaging (RCD, 2026), factorization violations (Bradley et al., ICML 2025), and boundary artifacts (FrankenMotion, 2026) — we run each body-part as a complete, independent diffusion process conditioned on the other's output, sampling from true conditionals p(upper|lower,text) and p(lower|upper,text) without factorization assumptions. Building on Kimodo's open-source G1-SEED-v1 model (282M parameters, trained on 288h BONES-SEED data), we observe that its constraint imputation mechanism (x̃_t = m ⊙ x_gt + (1-m) ⊙ x_t) is mathematically identical to RePaint's mask-agnostic inpainting — but Kimodo was trained with end-effector and keyframe constraint patterns, not body-part masks. A critical and previously unaddressed complication is Kimodo's dual classifier-free guidance (x̂₀ = D∅ + w_text(D_text - D∅) + w_constr(D_constr - D∅)): recent literature (CFG++, ICLR 2025; S-CFG, CVPR 2024) demonstrates that CFG extrapolation pushes samples off the data manifold, and with OOD body-part masks, the constraint-conditioned prediction D_constr may itself be unreliable — amplifying it via w_constr>0 could produce severe off-manifold artifacts. We therefore introduce constraint guidance weight w_constr as a key experimental variable, testing w_constr ∈ {0, 0.5, 1.0, 2.0} to disentangle the contributions of imputation (mask replacement at each step, theoretically robust to OOD per RePaint) versus guidance (CFG amplification of constraint adherence, distribution-dependent and potentially harmful for OOD). We hypothesize that w_constr=0 (pure imputation, no guidance) may outperform default w_constr=2 for OOD body-part masks. We introduce a two-tier framework: (1) a zero-shot iterative conditional generation pipeline (primary contribution) that uses URDF-guided body-part factorization to decompose G1's 34 joints into locomotion and manipulation subtrees, then runs sequential complete diffusion processes — first generating lower-body locomotion, then upper-body manipulation conditioned on fixed lower-body constraints via Kimodo's imputation — with an optional RePaint resampling variant (noise-denoise cycles at body-part boundaries for improved coherence), followed by post-composition physics projection via quadratic programming; (2) LoRA-based masked fine-tuning (secondary contribution, 500-800 lines of implementation, 4-6 days) that injects rank-16 adapters (~8M trainable parameters) into Kimodo's transformer attention layers with a masked denoising objective inspired by MaskedMimic, explicitly training the conditional distributions p(upper|lower,text) and p(lower|upper,text) to bring body-part conditioning into the training distribution. A preliminary diversity and guidance analysis (Day 1-3) establishes (a) whether compositional generation produces measurably more diverse trajectories than Kimodo's compound text prompts, with pre-registered success criterion: >15% improvement in mean pairwise joint-angle distance via permutation test at p<0.05, and (b) the optimal w_constr for OOD body-part masks. An early checkpoint (Day 8-10) tests zero-shot imputation quality across guidance settings, RePaint resampling, and LoRA-enhanced generation. DreamControl-v2 validates the diffusion→trajectories→RL pipeline paradigm for G1; we extend this paradigm with compositional body-part generation, guidance disentanglement for OOD constraints, and iterative conditional generation as a principled alternative to score composition. Generated trajectories are converted to physics-validated demonstrations via ProtoMotions. We evaluate on 3 SkillBench G1 tasks against eight baselines including DreamControl-v2, Kimodo text-prompted, and ablations across w_constr settings. The approach requires ~65-115h A100 and targets CoRL 2026 (16-20 day timeline).\",\n  \"project_name\": \"kintree_traj_diffusion\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Missing related work: FrankenMotion (arXiv 2601.10909, Jan 2026) does part-level body decomposition for compositional motion generation using diffusion; DeMoGen (arXiv 2512.22324, Dec 2025) does decompositional motion generation with energy-based diffusion; EnergyMoGen (CVPR 2025) composes motions via energy-based diffusion; KinMo (ICCV 2025) does kinematic-aware body-part-level generation. These directly undermine the claim that 'no existing work combines kinematic-tree factored diffusion with compositional trajectory generation.'\", \"CRITICAL — Kimodo (NVIDIA, arXiv 2603.15546) is not listed as a data generation baseline despite already generating G1 demonstrations from text, being open-source, and using a related root/body decomposition. It is a much stronger baseline than acknowledged and should be the primary comparison for data generation quality.\", \"CRITICAL — Compute budget likely exceeds the user's ≤200 H100-hour constraint. The proposal estimates 300-500 A100-hours for diffusion training alone (~150-250 H100-hours). Adding downstream RL evaluation on 8 SkillBench tasks (~20-50 H100-hours), physics validation rollouts (~10-20 H100-hours), and necessary ablations (~30-50 H100-hours) pushes total to ~210-370 H100-hours.\", \"HIGH — The 20-day timeline is unrealistic for: (a) implementing a novel GNN-based graph diffusion architecture with no reference implementation for the cross-attention torso-hub coordination, (b) training the model, (c) generating 500K trajectories with physics validation, (d) training downstream RL policies on 8+ tasks, (e) reproducing DreamControl-v2 and SkillBlender baselines, and (f) writing the paper.\", \"HIGH — Cross-attention at the torso hub is architecturally unproven for enforcing physics constraints (balance, momentum consistency, ground contact). Attention mechanisms learn soft correlations, not hard physical constraints. The proposal needs explicit physics loss terms or post-processing beyond cross-attention, which adds implementation complexity.\", \"MODERATE — DreamControl-v2 code has not been confirmed as open-source. If not available, reproducing it as a baseline within 20 days adds significant overhead. The proposal should confirm baseline reproducibility or choose baselines with available code.\", \"MODERATE — AMASS retargeted for G1 (~11K motions) and BONES-SEED (142K annotations) are primarily locomotion and everyday activities. The scarcity of manipulation demonstrations in this training data means the arm/hand subtree distributions may be poorly learned, undermining the compositional mixing claim for loco-manipulation.\", \"MODERATE — The resource estimates across modes are not internally consistent with the user's constraints. All three modes (manual, HIL, auto) specify A100-hours but the user's constraint is ≤200 H100-hours. Manual mode at 300-500 A100-hours and auto at 600-1000 A100-hours both need recalibration.\"]\nFeedback: The idea has a genuine kernel of novelty in applying kinematic-tree-structured GNN diffusion to robot trajectory data amplification, but it needs significant revision to be viable for CoRL 2026 under the stated constraints:\n\n1. **Address the body-part compositional generation literature**: FrankenMotion, DeMoGen, EnergyMoGen, and KinMo all decompose motion by body parts and compose novel combinations. You MUST differentiate clearly — the key differentiator is: (a) operating on robot joint-space trajectories rather than human motion, (b) using explicit kinematic-tree GNN structure rather than semantic body groups, and (c) physics-validated data amplification for downstream policy training. Frame these as the actual novel contributions.\n\n2. **Add Kimodo as the primary baseline**: Kimodo is open-source, generates G1 data from text, and uses root/body decomposition. The paper must show that kinematic-tree factoring produces higher-quality or more diverse training data than Kimodo. This is the main comparison reviewers will demand.\n\n3. **Reduce scope to fit ≤200 H100-hours**: Consider: (a) reducing to 3-4 SkillBench tasks instead of 8, (b) using Kimodo as a data source (fine-tune on Kimodo-generated data rather than training from scratch on AMASS), (c) simplifying the GNN architecture — start with a 2-level factorization (upper body / lower body) before claiming full kinematic-tree factoring.\n\n4. **Reduce timeline risk**: Use existing code maximally. KStar Diffuser code (CVPR 2025) provides the spatial-temporal graph diffusion backbone. ABD-Net provides URDF-to-graph parsing. Start from these codebases rather than implementing from scratch. Consider a simpler coordination mechanism than cross-attention — e.g., a shared latent variable at the torso that conditions both subtree denoisers.\n\n5. **Add physics loss terms**: Cross-attention alone won't enforce physical plausibility. Add explicit loss terms for center-of-mass balance, joint torque limits, and contact consistency during training, not just post-hoc physics filtering.\n\n6. **Clarify manipulation data sources**: If AMASS/BONES-SEED lack sufficient manipulation data, consider supplementing with DexMimicGen or RoboCasa demonstrations for the arm/hand subtrees.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Venue and timeline mismatch: User explicitly requested CoRL 2026 (abstract deadline May 26, paper deadline May 29, ≤20 days). The proposal targets Humanoids 2026 (July 24) as PRIMARY and does not list CoRL 2026 at all. The manual timeline of 8-10 weeks directly violates the user's 20-day hard constraint. Either (a) scope down drastically to fit CoRL 2026, or (b) explicitly justify abandoning CoRL with user agreement.\", \"HIGH — KStar Diffuser (CVPR 2025, Huawei Noah's Ark Lab) has NO publicly available code or GitHub repository. The proposal claims 'We build on three existing codebases: (1) KStar Diffuser provides the spatial-temporal graph diffusion backbone' — this is not possible without full reimplementation from the paper. This adds weeks of development time not accounted for in the timeline.\", \"HIGH — ABD-Net (arXiv 2603.19078) has NO publicly available code. The proposal claims ABD-Net 'provides URDF-to-graph parsing utilities for G1' — no such utilities are publicly available. URDF-to-graph parsing must be implemented from scratch (feasible but the effort is understated).\", \"HIGH — Missing closely related work: G-DReaM (arXiv 2505.20857, May 2025) uses graph-conditioned diffusion on robot morphological structure with joint-level attention for cross-embodiment motion generation. While it targets retargeting rather than compositional generation, it validates the core paradigm of graph-structured diffusion for robot motion and must be cited and differentiated against.\", \"MODERATE — Missing related work: UniMorphGrasp (arXiv 2602.00915, Jan 2026) uses URDF-derived kinematic graph features in diffusion with a hierarchical kinematic tree loss for cross-embodiment dexterous grasping. The kinematic tree loss concept is directly relevant to KinoTreeDiffuse's physics-informed training losses.\", \"MODERATE — DexMimicGen was built for bimanual Panda arms and the Fourier GR-1 humanoid, NOT the Unitree G1. Retargeting DexMimicGen trajectories to G1 arms/hands requires adding G1 URDF support, recalibrating subtask decomposition, and handling different hand configurations. This is non-trivial engineering work presented as straightforward.\", \"MODERATE — The proposal does not convincingly argue why compositional generation via factored diffusion outperforms prompting Kimodo with diverse text descriptions. Kimodo already generates G1 motions from text prompts ('walk while reaching for object') in 2-5 seconds. The key ablation missing: KinoTreeDiffuse compositional samples vs. Kimodo text-prompted loco-manipulation samples, evaluated on downstream RL policy diversity and success rate.\", \"LOW — Kimodo generates kinematic motions only. The pipeline doesn't address the kinematic-to-dynamic gap: generated trajectories need physics-based tracking (e.g., via ProtoMotions or sim-based tracking) before they can serve as RL demonstration data. This step's compute cost should be accounted for.\"]\nFeedback: The revision addressed Round 1 concerns well (simplified architecture, added baselines, reduced scope, added physics losses). The core idea — compositional humanoid trajectory generation via kinematic-tree-factored diffusion — remains genuinely novel and potentially impactful. However, several critical issues remain:\n\n1. **Fix the venue/timeline mismatch**: Either (a) drastically simplify to fit CoRL 2026's 20-day deadline — e.g., use Kimodo as the backbone and add only the 2-level factorization as a fine-tuning layer, skipping full reimplementation of KStar Diffuser; or (b) get explicit user agreement to target Humanoids 2026 instead. A 20-day version would need to use Kimodo's codebase directly (which IS open-source) rather than KStar Diffuser (which is not).\n\n2. **Rebuild implementation strategy around available code**: KStar Diffuser and ABD-Net have no public code. Feasible alternatives: (a) Build graph diffusion using PyTorch Geometric + standard DDPM/DDIM, which is ~2 weeks of work for an experienced researcher; (b) Use Kimodo's open-source G1 motion representation and diffusion architecture as the backbone, adding the 2-level factorization as a modification to Kimodo's existing root/body decomposition; (c) Implement URDF-to-graph parsing directly using PyBullet or urdfpy (simple — URDF is just a tree).\n\n3. **Cite and differentiate from G-DReaM and UniMorphGrasp**: G-DReaM uses graph-conditioned diffusion on robot morphology for retargeting — differentiate by emphasizing compositional generation (not retargeting) and the 2-level factorization architecture. UniMorphGrasp uses kinematic-tree-aware losses in diffusion for grasping — differentiate by emphasizing temporal trajectory generation vs. static pose generation.\n\n4. **Add a 'Kimodo text-prompted loco-manipulation' baseline**: This is the baseline reviewers will most demand. Generate loco-manipulation trajectories by prompting Kimodo with compound text descriptions and compare downstream RL performance against KinoTreeDiffuse's compositional samples. If you can't beat this baseline, the compositional approach isn't justified.\n\n5. **Simplify DexMimicGen dependency**: Either drop DexMimicGen from the multi-source training data (use Kimodo + OmniRetarget + AMASS-retargeted data instead), or explicitly budget 1-2 weeks for G1 adaptation of DexMimicGen.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"HIGH — Missing critical related work: MixerMDM (CVPR 2025, arXiv 2504.01019) performs learned body-joint-level composition of frozen pre-trained motion diffusion models with spatial mixing weights — this is the closest prior art for body-part compositional diffusion and is not cited. It uses simultaneous weighted blending rather than alternating denoising, but the core paradigm (compose diffusion models at the body-part level during denoising) is directly overlapping. Must be cited and clearly differentiated.\", \"HIGH — Missing critical related work: MaskedMimic (NVIDIA, SIGGRAPH Asia 2024, arXiv 2409.14393) trains with random body-part masking to learn a unified model that synthesizes full-body motion from partial (masked) joint constraints — conceptually identical to the proposed masked body-part fine-tuning objective. MaskedMimic is implemented in ProtoMotions (which the proposal already depends on) and comes from NVIDIA (same lab as Kimodo). Using their masking idea without citation would be a critical omission. MaskedMimic uses C-VAE rather than diffusion, which is a valid distinction, but the insight is the same.\", \"HIGH — Alternating body-part denoising faces documented theoretical problems that are not addressed: (1) Mode-averaging when component distributions are multimodal, producing samples that are 'neither locally feasible nor globally coherent' (documented in Refining Compositional Diffusion, 2025; CDGS, 2026); (2) Score composition via product-of-experts only holds when conditional distributions approximately factorize (Mechanisms of Projective Composition, 2025), which is violated by tight upper-lower body dynamic coupling (angular momentum compensation, centroidal dynamics, balance recovery all couple body parts); (3) FrankenMotion (Jan 2026) explicitly found that naive body-part composition with MDM produces 'unsmooth transitions' and required purpose-built part-level training data and architecture. The proposal needs either MCMC-corrected sampling (as in Reduce Reuse Recycle, ICML 2023), physics-based projection during denoising steps, or an honest discussion of these limitations.\", \"MODERATE — The 'torso coupling term' (weighted average of both denoisers' predictions based on predicted noise variance) is ad-hoc and underspecified. There is no theoretical justification for why noise-variance-weighted averaging at the body-part boundary produces physically consistent motions. Consider: (a) a physics-based projection step that enforces whole-body constraints (CoM, angular momentum) after each denoising step, or (b) a learned coupling module trained on full-body trajectories, or (c) framing this as classifier-free guidance with body-part conditions.\", \"MODERATE — Missing related work: Motion-Adapter (arXiv 2604.16135, April 2026) addresses compound action synthesis (multiple concurrent body-part actions) in text-to-motion diffusion via attention masks. Also missing: Factorized Diffusion Policy (arXiv 2512.21898, RSS 2025 Workshop) factorizes diffusion into compositional sub-models with score aggregation. Both should be cited for completeness.\", \"LOW — OmniRetarget HuggingFace dataset contains 4.0 hours of G1 trajectories (verified on huggingface.co/datasets/omniretarget), not '8+ hours' as claimed. Also, Kimodo model weights use NVIDIA Open Model License, not Apache 2.0 — only the code is Apache 2.0. These inaccuracies should be corrected.\"]\nFeedback: The proposal has improved substantially from Rounds 1-2: it correctly targets CoRL 2026, builds on available infrastructure (Kimodo, ProtoMotions, SkillBench), fits within compute constraints, and includes the right baselines. The core remaining problem is **theoretical grounding of the compositional sampling mechanism** and **two critical citation gaps**. Here is how to address each:\n\n1. **Cite and differentiate from MixerMDM and MaskedMimic.** MixerMDM (CVPR 2025) composes frozen diffusion models at the body-joint level via learned blending weights — differentiate by emphasizing that KinoTreeDiffuse uses URDF-structured factorization with masked fine-tuning (not frozen models), and alternating denoising (not simultaneous blending). MaskedMimic (SIGGRAPH Asia 2024, NVIDIA) trains with random body-part masking for motion completion — differentiate by noting it uses C-VAE (not diffusion), requires training from scratch via RL+distillation (not fine-tuning a pre-trained model), and targets character animation (not robot trajectory generation for downstream RL). Frame your contribution as: 'We bring MaskedMimic's masking insight into the diffusion fine-tuning paradigm on Kimodo's robot-specific representation, and extend MixerMDM's compositional diffusion from blending to structured alternating denoising with physics enforcement.'\n\n2. **Address the alternating denoising failure modes.** Three concrete options (implement at least one):\n   (a) **Physics-based projection after each denoising step** — after alternating upper/lower denoising, project the composed state to satisfy whole-body constraints (CoM within support polygon, angular momentum budget, joint torque limits). This is computationally cheap and directly addresses the coupling concern.\n   (b) **Langevin MCMC correction steps** — following Reduce Reuse Recycle (Du et al., ICML 2023), add a few MCMC steps after each reverse-diffusion step to correct for the bias introduced by naive composition. This is the theoretically principled approach.\n   (c) **Masked fine-tuning as the primary contribution, with inference-time composition as secondary.** Reframe: the masked fine-tuning teaches strong conditional distributions p(upper|lower,text) and p(lower|upper,text), which can be used for diverse data generation via iterative conditional generation (sample lower-body, then sample upper-body conditioned on it) rather than alternating denoising. This avoids the composition-during-denoising theoretical issues entirely and is closer to MaskedMimic's proven approach.\n\n3. **Strengthen the argument against the Kimodo text-prompted baseline.** This is the baseline reviewers will focus on. The argument 'factorized generation enables combinatorial diversity' is intuitive but needs empirical grounding. Consider: (a) a toy experiment showing that Kimodo's compound-text samples cluster in a smaller region of joint-angle space than compositionally generated samples; (b) explicit measurement of state-space coverage (mean pairwise distance) as a primary metric; (c) honest acknowledgment that if the Kimodo training distribution already covers loco-manipulation compositions well, the compositional approach may offer diminishing returns.\n\n4. **Frame novelty honestly.** The contribution is best described as: 'the first application of masked body-part diffusion fine-tuning (inspired by MaskedMimic) to a pre-trained robot motion diffusion model (Kimodo), with URDF-structured factorization and physics-enforced compositional sampling, evaluated on downstream RL policy quality.' This is a valid and publishable contribution at CoRL, but overselling it as 'no prior work combines kinematic-tree factored diffusion with compositional trajectory generation' is inaccurate given MixerMDM and MaskedMimic.\n\n5. **Minor corrections:** OmniRetarget HuggingFace data is 4.0h (not 8+). Kimodo weights are NVIDIA Open Model License (not Apache 2.0).\n\n### Round 4 review\nVerdict: revise\nIssues: [\"CRITICAL — Kimodo's public repository (github.com/nv-tlabs/kimodo) provides ONLY inference code. There are no training scripts, no trainer module, no data loading pipeline, and no fine-tuning infrastructure. The directory structure (kimodo/model/, kimodo/scripts/, etc.) contains model definition and generation code only. The proposal's claim 'Fine-tuning uses Kimodo's existing training infrastructure' is factually incorrect. Implementing a complete training loop from scratch — noise scheduling, masked denoising loss, constraint conditioning curriculum, data loading for OmniRetarget + Kimodo's motion representation format, LLM annotation pipeline — is feasible (Apache-2.0 code + NVIDIA Open Model License weights permit it) but adds an estimated 5-8 days of engineering effort that is not accounted for in the 15-19 day timeline.\", \"HIGH — The 15-19 day manual timeline is unrealistic given the training code gap. Realistic breakdown with training implementation: Days 1-6: implement training infrastructure and masked training objective; Days 5-7: generate body-part text annotations via LLM; Days 7-10: fine-tuning runs (~12-20h); Days 10-13: trajectory generation + physics projection + ProtoMotions tracking; Days 13-17: SkillBench RL training (4 tasks × 5 baselines = 20 runs, ~5h each, parallelized on 4 GPUs to ~25h); Days 16-20: paper writing. This requires zero slack for debugging, hyperparameter tuning, or failed experiments, making the CoRL abstract deadline (Day 16) extremely risky for having results.\", \"HIGH — The Kimodo G1-RP-v1 checkpoint was trained on the proprietary Bones Rigplay dataset (~560h), which is unavailable. Fine-tuning this checkpoint with only OmniRetarget's 4.0h of supplemental loco-manipulation data creates a massive data distribution shift (4h supplemental vs. 560h base training). The proposal does not discuss: (a) whether fine-tuning with such a small supplement will actually shift the conditional distributions meaningfully, (b) whether using the G1-SEED-v1 checkpoint (trained on open BONES-SEED, 288h) would be more appropriate since BONES-SEED data is available for continued pre-training alongside OmniRetarget data, or (c) catastrophic forgetting risks when fine-tuning with masked objectives on a small dataset.\", \"MODERATE — The LLM-generated body-part text annotations are an untested pipeline component with no validation plan. The proposal says annotations are generated by 'prompting an LLM with per-body-part joint velocity statistics (e.g., high leg velocity + low arm velocity → walking for lower, arms at sides for upper).' This heuristic could produce noisy, uninformative, or incorrect annotations (e.g., a motion with both legs stationary but high torso rotation could be mislabeled). No annotation quality evaluation or human verification step is described.\", \"MODERATE — Physics auxiliary losses (CoM balance, joint torque limits) computed on the predicted clean sample x̂₀ during diffusion training may be ineffective at early denoising steps where x̂₀ predictions are highly noisy. PhysDiff (ICCV 2023) applied physics corrections as a post-processing step during sampling, not as training losses. The effectiveness of physics losses during diffusion fine-tuning (as opposed to post-generation projection, which the proposal also includes) is not established in the literature and may add implementation complexity without meaningful quality improvement.\", \"LOW — The risk note honestly acknowledges that 'masked fine-tuning may not significantly improve conditional quality over Kimodo zero-shot constraint conditioning,' but frames a null result as publishable. At CoRL, a negative result paper would need substantially more analysis (why doesn't it help? what does this tell us about pre-trained model representations?) than what the current experimental design supports.\"]\nFeedback: The idea has improved substantially across rounds and addresses a genuine gap. The iterative conditional generation approach is theoretically well-motivated, the baselines are comprehensive, and the differentiation from prior work is clear. The remaining blockers are primarily execution feasibility, not conceptual soundness. Here is how to address each:\n\n1. **Acknowledge and plan for the training code gap.** This is the single most important fix. Kimodo has no training code — you must implement it. Three options:\n   (a) **Fastest**: Write a minimal fine-tuning script that loads Kimodo's model weights, implements a standard DDPM training loop with your masked denoising objective, and uses PyTorch's native optimizer. The model architecture is a standard transformer; the noise schedule and loss are standard DDPM. Budget 3-5 days for this. This is the recommended path.\n   (b) **Contact NVIDIA**: The Kimodo team (NVIDIA SIL) may share training scripts under collaboration. This could save 3-5 days but adds dependency risk.\n   (c) **Simplify to zero-shot only**: If time is critically short, drop the fine-tuning contribution entirely and evaluate only Kimodo's zero-shot constraint conditioning for iterative conditional generation. The URDF factorization + iterative conditional generation + physics projection + downstream RL evaluation would still be a contribution, though weaker.\n\n2. **Choose the G1-SEED-v1 checkpoint.** Since BONES-SEED data is publicly available and you can combine it with OmniRetarget for fine-tuning, this avoids the distribution shift problem of fine-tuning the RP checkpoint on 4h of data against 560h of unseen base training data. The SEED model is less capable but the fine-tuning dynamics are more predictable.\n\n3. **Add annotation quality validation.** Before committing to the full pipeline, manually verify a random sample of 50 LLM-generated body-part text annotations against ground-truth motion videos. Report inter-annotator agreement or at least spot-check accuracy. This takes <1 day and prevents a foundational pipeline flaw.\n\n4. **Drop physics training losses; keep post-generation projection.** The physics auxiliary losses during fine-tuning are theoretically shaky and add implementation complexity. The post-composition physics projection (QP) is sufficient and well-grounded. Simplifying the fine-tuning to pure masked denoising loss saves implementation time.\n\n5. **Timeline recovery strategy.** With training code implementation, the realistic timeline is 20-22 days, which misses the paper deadline by 1-3 days. Mitigation: (a) submit abstract by Day 16 with partial/expected results and complete experiments by Day 20; (b) reduce to 3 SkillBench tasks (FarReach-Easy, BoxPush-Medium, PackageCarry-Hard) to save RL compute time; (c) run Kimodo text-prompted baseline first (Day 1, no code needed) to establish the target to beat.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"CRITICAL — Zero-shot pipeline relies on out-of-distribution constraint masking. Independent verification of Kimodo's technical report (arXiv 2603.15546) confirms that Phase 2 training uses ONLY pre-defined constraint patterns: full-body keyframes, random subsets of hands/feet positions/rotations, 2D root position/heading, and foot contact configurations. Body-part-level masking (e.g., 'fix all lower-body joints while generating upper-body') was NEVER in the training distribution. The proposal claims Kimodo's 'native constraint conditioning system' supports body-part masking, but this is out-of-distribution. While RePaint (CVPR 2022) showed diffusion models can generalize to arbitrary inpainting masks via step-by-step imputation, Kimodo's motion-specific constraint conditioning (with dual CFG for text vs. constraints) may not generalize as cleanly. The proposal must: (a) explicitly acknowledge this OOD risk, (b) frame the zero-shot approach as RePaint-style imputation and cite RePaint, (c) present the zero-shot quality as an empirical question rather than an assumed capability.\", \"HIGH — Missing critical related work: DreamControl-v2 (arXiv 2604.00202, March 31 2026) trains a guided diffusion model directly in humanoid robot motion space (G1-specific), generates reference trajectories from text + spatio-temporal controls, and trains downstream RL policies — the exact same pipeline paradigm as KinoTreeDiffuse. DreamControl-v2 does not do compositional body-part generation, which is KinoTreeDiffuse's differentiator, but it must be cited and used as a baseline or at minimum discussed. It validates the core pipeline (diffusion → trajectories → RL) while highlighting that the compositional body-part factorization is the specific novel contribution.\", \"HIGH — OmniRetarget data size persists at '8+ hours' despite previous rounds flagging this. Independent verification on HuggingFace (huggingface.co/datasets/omniretarget/OmniRetarget_Dataset) confirms 4.0 hours total (3.0h robot-object + 0.5h robot-terrain + 0.5h robot-object-terrain). The arXiv paper may claim 8+ hours, but only 4.0h are publicly available. This discrepancy appears in the opportunity section, approach section, and key_references — all must be corrected to '4.0h publicly available.'\", \"MODERATE — The argument for compositional generation over Kimodo's text-prompted baseline is insufficiently developed. Kimodo uses LLM2Vec for text encoding, which provides strong compositional text understanding for compound prompts like 'walk toward the shelf while raising your right hand.' The proposal's claim that factorized generation enables 'combinatorial diversity' (N_loco × N_manip >> N_compound) is intuitive but may not hold empirically if Kimodo's text-prompted generations already cover the relevant distribution. The proposal should explicitly hypothesize WHERE compositional generation would outperform text prompting (e.g., rare combinations not in training data, out-of-distribution text compositions) and design targeted experiments for those cases.\", \"MODERATE — LoRA training loop complexity is understated at '~200 lines.' A proper implementation from Kimodo's inference-only codebase requires: data loading for BONES-SEED's specific format (motion representation, temporal annotations), motion preprocessing matching Kimodo's representation (6D rotations, smoothed root), masked denoising objective with body-part masks, LoRA injection into Kimodo's two-stage transformer architecture, optimizer setup matching documented hyperparameters (Adam-atan2, per-component loss weights), EMA tracking, and evaluation/checkpointing. Realistic estimate: 500-800 lines of non-trivial code. Budget 4-6 days, not 2-3.\", \"LOW — BeyondMimic (arXiv 2508.08241, UC Berkeley) uses a unified latent diffusion model for humanoid control including motion inpainting and skill composition. While it targets real-time control rather than trajectory dataset generation, its diffusion-based inpainting/composition approach is conceptually related and should be cited for completeness.\"]\nFeedback: The proposal has improved enormously across 5 rounds and is approaching publishable quality. The remaining issues are fixable. Here is how to address each:\n\n1. **Acknowledge the OOD constraint masking risk explicitly.** This is the single most important fix. Reframe the zero-shot pipeline honestly: 'Kimodo was trained with end-effector and keyframe constraint patterns, not body-part-level masks. We hypothesize that its imputation-based conditioning (x̃_t = m ⊙ x_gt + (1-m) ⊙ x_t) generalizes to body-part masks following the same principle as RePaint (CVPR 2022), where arbitrary inpainting masks work with pre-trained DDPMs. We test this empirically.' This transforms a hidden weakness into an explicit research question — which is actually more interesting for reviewers.\n\n2. **Cite DreamControl-v2 and position against it.** DreamControl-v2 validates the diffusion→trajectories→RL pipeline for G1 but uses monolithic text-conditioned generation without body-part factorization. Frame KinoTreeDiffuse as advancing this paradigm with compositional generation: 'DreamControl-v2 demonstrates the effectiveness of diffusion-generated reference trajectories for humanoid RL; we extend this paradigm with compositional body-part generation that enables combinatorial diversity beyond what monolithic text prompting achieves.'\n\n3. **Correct OmniRetarget to 4.0h everywhere.** This is a simple fix but its persistence across 3 review rounds suggests carelessness.\n\n4. **Strengthen the case against the text-prompted baseline.** Add a preliminary analysis (Day 1-2): generate 50 compound text-prompted motions from Kimodo (e.g., 'walk while reaching,' 'jog while waving') and measure their diversity in joint-angle space. Compare against 50 compositionally generated motions (5 locomotions × 10 manipulations). If compositional diversity is measurably higher, lead with this result.\n\n5. **Budget 4-6 days for LoRA training implementation, not 2-3.** Update timeline accordingly. The early checkpoint strategy (Day 7-8) becomes more important with this revised estimate.\n\n6. **Consider adding a 'Kimodo + RePaint resampling' baseline.** If you're going to frame the zero-shot approach as RePaint-style imputation, adding RePaint's resampling trick (noise-denoise cycles at the mask boundary) could improve zero-shot quality significantly and costs nothing in implementation complexity.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"HIGH — Dual CFG interaction with OOD body-part masks is an unaddressed failure mode. Recent work (CFG++, ICLR 2025; Rethinking Spatial Inconsistency in CFG, CVPR 2024; What Guidance Does in Masked Discrete Diffusion, 2025) documents that when dual guidance signals conflict — here, text guidance pulling toward in-distribution regions while constraint guidance (w_constr=2) pushes toward OOD body-part patterns — the result is off-manifold amplification with double-exponential dependency on guidance weight. The proposal uses Kimodo's default w_constr=2, but with OOD constraint patterns this may produce severe artifacts. Mitigation options not discussed: (a) set w_constr=0 for OOD masks (pure imputation without guidance), (b) use adaptive/annealed constraint guidance, (c) apply CFG++ manifold-constrained sampling.\", \"MODERATE — The novelty argument rests primarily on 'testing an empirical hypothesis on a specific model.' While honest, this positions the paper as an empirical study rather than a method paper. CoRL reviewers may question whether 'we applied RePaint-style inpainting to Kimodo and added LoRA' constitutes sufficient methodological contribution. Strengthening: the URDF-factored iterative conditional generation (sequential complete processes rather than score composition) should be emphasized as the methodological choice, with theoretical justification from the compositional diffusion failure literature (mode-averaging, factorization violations).\", \"MODERATE — The preliminary diversity analysis (Day 1-2) is the linchpin of the entire motivation. If compositional generation does NOT produce measurably higher diversity than Kimodo's compound text prompts (which use LLM2Vec for compositional text understanding), the paper's raison d'être evaporates. The proposal correctly identifies this but doesn't specify: (a) what diversity threshold would constitute a 'positive' result, (b) what statistical test would be used, (c) how many samples are needed for statistical significance. Without pre-registered success criteria, there's a risk of post-hoc rationalization.\", \"LOW — Missing recent paper: 'Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking' (arXiv 2604.17335, April 2026) uses diffusion-based G1 motion generation with RL tracking — validates the generation→tracking paradigm but targets terrain-aware locomotion rather than compositional loco-manipulation. Should be briefly cited for completeness as concurrent validation of diffusion→ProtoMotions→RL pipeline.\", \"LOW — The paper title 'KinoTreeDiffuse: Compositional Humanoid Trajectory Amplification via URDF-Factored Iterative Conditional Diffusion' is 13 subtitle words. CoRL papers benefit from concise, memorable titles. Consider: 'Can Humanoid Motion Diffusion Models Compose? Testing Body-Part Inpainting for Diverse Trajectory Generation' — which foregrounds the empirical question.\"]\nFeedback: The proposal is close to passable after 5 rounds of revision — the clarity is excellent, related work is comprehensive, baselines are strong, and the early checkpoint strategy is well-designed. Three changes would push it over the threshold:\n\n1. **Address the dual-CFG failure mode explicitly.** This is the single most important remaining gap. Kimodo's constraint conditioning uses dual CFG (w_text, w_constr), and literature shows dual guidance amplifies off-manifold artifacts when one signal is OOD. Add a specific experimental variable: test w_constr ∈ {0, 0.5, 1.0, 2.0} for body-part masks in the Day 1-2 preliminary analysis. Setting w_constr=0 reduces to pure imputation (RePaint-style, no guidance), which may actually work BETTER than guided generation for OOD patterns. This costs nothing extra and strengthens the empirical contribution. Frame it as: 'We disentangle the contributions of imputation (mask replacement at each step) versus guidance (CFG amplification of constraint adherence) for OOD body-part patterns.'\n\n2. **Pre-register diversity success criteria.** State explicitly: 'We consider compositional generation justified if mean pairwise joint-angle distance of N_comp=50 compositional samples exceeds that of N_text=50 compound-text samples by >15% (or 1 standard deviation), measured via permutation test at p<0.05.' This transforms the preliminary analysis from a subjective judgment to a rigorous hypothesis test and protects against post-hoc rationalization.\n\n3. **Strengthen the methodological contribution framing.** The choice of iterative conditional generation (sequential complete diffusion processes) over score composition (simultaneous/alternating denoising within one process) is itself a methodological contribution supported by the compositional diffusion failure literature. Emphasize: 'Unlike score-composition approaches (MixerMDM, EnergyMoGen, CompDiffuser) which suffer from mode-averaging and factorization violations within the denoising loop, iterative conditional generation runs each body-part as a complete, independent diffusion process conditioned on the other's output — avoiding the documented failure modes while enabling compositional diversity.' This elevates the paper from 'we tried inpainting on Kimodo' to 'we propose iterative conditional generation as a principled alternative to score composition for structured body-part composition, supported by theory and validated empirically.'\n\nMinor: cite arXiv 2604.17335 for pipeline validation, and consider a shorter title.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T20:21:53.970Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T20:21:53.970Z",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-10T20:21:54.000Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-10 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).

Direction: Generative models specifically targeting HUMANOID robot training data — addressing the high-DoF, whole-body, loco-manipulation data scarcity that bottlenecks humanoid VLA / WM training. SCOPE LIMITED TO TWO CONTRIBUTION TYPES:
  (a) Generation ALGORITHMS — e.g., video diffusion conditioned on humanoid action streams, action-conditioned generative models, latent humanoid trajectory generators, physics-aware whole-body video generation.
  (b) Procedural data-generation PIPELINES — e.g., MimicGen-style automated demo multiplication for humanoids, procedural whole-body task/scene generation, automated quality filtering pipelines for synthetic humanoid trajectories.

OUT OF SCOPE: action retargeting innovations (human-video → humanoid-action retargeting). Treat existing retargeters (HumanPlus, OmniH2O) as black-box upstream tools if needed; do NOT propose new retargeting methods.

Recent landscape (do not duplicate): NVIDIA GR00T-Dreams, DexMimicGen, MimicGen extensions for humanoid, Helix self-supervised humanoid pipelines, Cosmos for synthetic humanoid video. Humanoid data scarcity is the #1 bottleneck cited in 2026 humanoid papers — high impact area.

Contribution type: METHOD ONLY. New generation algorithm OR new procedural pipeline. Not a new released humanoid dataset alone.

SIM-ONLY MITIGATION: Validate generated data by training a downstream humanoid policy/VLA in sim and comparing against models trained on baseline data. Frame contribution as method, not dataset.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Strategies: (a) fine-tune existing video diffusion (CogVideoX, OpenSora, Cosmos) with humanoid-action conditioning, (b) procedural pipeline that requires negligible training compute, (c) small efficient humanoid-specific generator that beats general baselines.
2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos, Isaac Lab humanoid suite (G1, H1), MimicGen, RoboCasa with humanoid embodiments if available.
3. Eval: train humanoid policy/VLA on generated vs baseline data. Test on Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench. Report success rate + data efficiency curves.

Look for: physics-aware whole-body video generation with kinematic consistency, action-conditioned generators that exploit humanoid kinematic structure, procedural pipelines that produce diverse loco-manipulation (not just static manipulation) data, automatic quality filtering for synthetic humanoid trajectories. Avoid: any retargeting-based contribution, arm-only generation rebadged as humanoid, naive fine-tuning of video diffusion on humanoid clips without method.

Tag: direction=humanoid_data_gen, contribution_type=method. target_venues=["CoRL 2026"].**
You MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be "revise" or "fail".

## 核心要求：非常仔细地调研，非常仔细地思考

你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。

### 调研要求

1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。
   每个验证维度建议用 2-3 种不同的搜索查询。

2. **可行性深度检查**：
   - 搜索类似实验的实际成本/周期
   - 检查 claimed baselines 是否可复现
   - 验证所需的 datasets/models 是否真的可以获取

3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：
   - 尝试不同的关键词组合
   - 同时检查 arXiv 和 conference proceedings
   - 寻找相邻领域的并行/concurrent 工作

4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。

### 思考要求

5. **独立判断**：
   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查
   - 思考这个 idea 在实际执行中会遇到什么困难
   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）

6. **评分诚实**：
   - 不要给"看起来还行"的 idea 高分——4 分意味着"确实很好"，5 分意味着"令人兴奋"
   - Agent 评分经常虚高，你的职责就是纠正这种偏差

充分利用你的工具——做真正的调研，不是走过场。


## 论文搜索策略

你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。

### 搜索源（推荐每个维度使用 2 个不同来源）

1. **arXiv 预印本**（最新工作）:
   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文
   - `site:arxiv.org {method_name}` — 按具体方法名搜索
   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作

2. **Google Scholar**（引用关系 + 综合覆盖）:
   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果
   - `"{exact paper title}"` — 验证论文是否真实存在
   - `"{author name}" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）

3. **Papers With Code**（SOTA 排行 + 代码可用性）:
   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜
   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现
   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局

4. **OpenReview**（会议审稿 + 同行评价）:
   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文
   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价

5. **Semantic Scholar**（语义搜索 + 引用图谱）:
   - `semantic scholar {topic} survey {year}` — 找综述论文
   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）

6. **GitHub**（实现验证）:
   - `site:github.com {method_name} {task}` — 验证开源实现是否存在
   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取

### 搜索维度（多角度交叉，不要只按 topic 搜）

对每个 idea/方向，尽量覆盖以下维度：

1. **正向搜索**：直接搜索主题相关论文
   - `{topic} {subtopic} {year}`
   - `{method_name} for {task_name}`

2. **竞争论文搜索**（最关键！）：
   - `{core_problem} {year}` — 有没有人在解决同样的问题？
   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？
   - `{gap_description} solution` — 你发现的 gap 是否已被解决？
   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文

3. **相邻领域搜索**：
   - `{method_from_other_field} applied to {your_task}`
   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题

4. **反面搜索**（找到反对你 idea 的证据）：
   - `{your_approach} limitations` / `{your_approach} failure`
   - `why {assumed_gap} is not a problem`
   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好

5. **引用链追踪**（发现遗漏工作的最有效方法）：
   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分
   - 在 Semantic Scholar 上查看它的 "cited by" — 最近引用它的论文很可能是 concurrent work
   - 对 3 个以上核心相关论文重复此步骤

### 搜索数量建议（理想目标，上下文充裕时尽量达到）

| 角色 | 建议搜索次数 | 说明 |
|------|-------------|------|
| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |
| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |
| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |
| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |

### 上下文管理

你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。

- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。
- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。
- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。
- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。


As a reviewer, your search focus should be:
1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实
2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作
3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通
4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work

## 竞争论文专项搜索（Reviewer 独有）

这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：

1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题
   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）
   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）
   - 方法名 + 任务名的不同组合

2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，
   搜索他们最近的论文（`"team_name" OR "author_name" {topic} {year}`）

3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers
   - `site:openreview.net {topic} 2026`
   - `{conference_name} 2026 accepted papers {topic}`

4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文
   这是发现 concurrent work 最有效的窗口

如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，
并在 feedback 中说明这些工作如何影响 idea 的 novelty。

## Review checklist
1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?
   If outdated, specify what the current SOTA is and cite your source.
2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)
3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?
5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?
6. **Novelty**: Is this sufficiently different from existing work?
   When scoring novelty < 4:
   - You MUST identify the closest existing work(s) via WebSearch
   - In your feedback, write: "This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion]."
   - This gives the generator targeted guidance to boost novelty, not just "be more novel".
7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?
   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero
   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks
   - Human-in-Loop should fall between manual and auto on most dimensions
   - Manual and HIL must NOT include salary/wages — only GPU and API costs
   - Auto Research must NOT include agent operational overhead
   - If any mode estimate is clearly unrealistic, flag it

## Idea under review (round 7/10)
{
  "title": "Can Humanoid Motion Diffusion Models Compose? Body-Part Inpainting for Diverse Loco-Manipulation Trajectories",
  "core_problem": "Generating diverse, physically plausible whole-body humanoid loco-manipulation demonstrations by compositionally mixing locomotion and manipulation behaviors remains unsolved in robot joint-space. DreamControl-v2 (arXiv 2604.00202, March 2026) validates that diffusion-generated reference trajectories can train robust RL policies for G1 humanoid skills (91-100% success across 8 tasks), but relies on monolithic text-conditioned generation — the diversity of downstream trajectories is bounded by the training data distribution, with no mechanism for combinatorial composition of locomotion and manipulation behaviors. Human-motion compositional methods (FrankenMotion, MixerMDM, Motion-Adapter) decompose by semantic body groups but operate in SMPL space without physics validation or downstream robot policy evaluation; FrankenMotion further documents that naive body-part composition produces 'unsmooth transitions.' MixerMDM (CVPR 2025) learns to compose frozen diffusion models at the body-joint level via spatial mixing weights, but operates in human motion space, uses simultaneous blending of frozen models (not conditioned generation), and does not evaluate downstream RL performance. MaskedMimic (SIGGRAPH Asia 2024) and MaskedManipulator (SIGGRAPH Asia 2025) pioneer random body-part masking for physics-based character control via RL + distillation, but use C-VAE/RL architectures (not diffusion), train from scratch (not fine-tuning pre-trained models), and produce real-time controllers rather than trajectory datasets for downstream RL. Robot-side generators like Kimodo (NVIDIA, March 2026) produce high-quality G1 motions from text and support kinematic constraint conditioning via imputation, but its constraint system was trained exclusively with end-effector and keyframe patterns — body-part-level masks are out-of-distribution. A critical and previously unaddressed complication is Kimodo's dual classifier-free guidance (w_text=2, w_constr=2): recent literature (CFG++, ICLR 2025; S-CFG, CVPR 2024) demonstrates that CFG extrapolation pushes samples off the data manifold, and dual guidance with OOD constraint patterns risks compounding this effect — the constraint guidance signal D_constr may itself be unreliable for OOD masks, and amplifying it via w_constr>0 could produce severe artifacts. Can we exploit Kimodo's imputation-based constraint mechanism — disentangling the contributions of imputation (mask replacement at each denoising step, following RePaint's mask-agnostic principle) versus guidance (CFG amplification of constraint adherence, which may be counterproductive for OOD patterns) — with URDF-guided body-part factorization and optional LoRA adaptation, to enable compositional loco-manipulation trajectory generation that achieves greater diversity and downstream RL policy quality than monolithic text-conditioned generation?",
  "opportunity": "A key insight is that Kimodo's imputation-based constraint mechanism is mathematically equivalent to RePaint-style inpainting: at each denoising step, constrained joints are replaced with (noised) target values while unconstrained joints are generated freely. RePaint (CVPR 2022) demonstrated that this imputation mechanism generalizes to arbitrary mask patterns — including those never seen during training — because it operates at the level of individual denoising steps rather than requiring mask-pattern-specific learned representations. CondMDI (SIGGRAPH 2024) provides additional supporting evidence in the motion domain: it trains with randomly sampled joints and keyframes and achieves strong generalization to various spatial constraint patterns, demonstrating that motion diffusion models can handle diverse mask configurations. However, a critical caveat applies: Kimodo's Phase 2 training uses specific constraint patterns (full-body keyframes, random subsets of hands/feet positions/rotations, 2D root position/heading, foot contact configurations), and body-part-level masking (e.g., 'fix all lower-body joints while generating upper-body') was NEVER in its training distribution. Furthermore, Kimodo employs dual classifier-free guidance with formula x̂₀ = D∅ + w_text(D_text - D∅) + w_constr(D_constr - D∅), where D_constr is the model's output conditioned only on constraints. When constraints are OOD, D_constr may be unreliable, and amplifying it via w_constr=2 risks off-manifold artifacts — a failure mode documented by CFG++ (Chung et al., ICLR 2025), which shows standard CFG extrapolation pushes samples off the data manifold, and by S-CFG (Shen et al., CVPR 2024), which demonstrates spatial inconsistency from uniform guidance scaling across semantically distinct regions. A crucial experimental variable is therefore w_constr itself: setting w_constr=0 reduces constraint influence to pure imputation (RePaint-style, no guidance amplification), which may actually work BETTER for OOD body-part patterns than guided generation, since the imputation mechanism does not require in-distribution constraint patterns while the guidance signal does.\n\nBeyond the empirical OOD question, our methodological choice of iterative conditional generation — running sequential complete diffusion processes rather than composing scores within a single denoising loop — is itself a principled contribution motivated by the compositional diffusion failure literature. Score-composition approaches (MixerMDM, EnergyMoGen, CompDiffuser) assume approximate factorization of the joint distribution, but Bradley et al. (ICML 2025) prove this requires approximate independence between composed components — violated for kinematically coupled body parts. Naive score composition also suffers from mode-averaging when local distributions are multimodal (RCD, arXiv 2605.03075, May 2026) and produces 'unsmooth transitions' at body-part boundaries (FrankenMotion, Jan 2026). Iterative conditional generation avoids all three failure modes: each body-part generation is a complete diffusion process sampling from the true conditional p(upper|lower,text_manip) or p(lower|upper,text_loco), with no factorization assumption, no mode-averaging within the denoising loop, and full-trajectory coherence within each generated part.\n\nKimodo's G1-SEED-v1 checkpoint (282M parameters, trained on 288h BONES-SEED data) and its complete training hyperparameters are publicly documented: T=1000 diffusion steps, Adam-atan2 optimizer at lr=2e-5, Smooth L1 loss with per-component weights, EMA every 10 steps with decay 0.995, 6D rotation representation, and a two-stage transformer denoiser (16 layers, 8 heads, dim 1024). Kimodo's public repository provides ONLY inference code — no training scripts, data loaders, or fine-tuning infrastructure. The zero-shot iterative conditional generation pipeline requires only Kimodo's inference API with its imputation mechanism. For the LoRA secondary contribution, we implement fine-tuning from the inference codebase using documented hyperparameters. All infrastructure exists: (1) Kimodo G1-SEED-v1 provides the backbone; (2) BONES-SEED provides 288h of G1-retargeted motions with up to 6 NL descriptions per motion plus temporal segmentation; (3) OmniRetarget provides 4.0h of publicly available G1 loco-manipulation trajectories (3.0h robot-object + 0.5h robot-terrain + 0.5h robot-object-terrain); (4) ProtoMotions provides GPU-accelerated kinematic-to-dynamic conversion; (5) SkillBench provides 8 G1 loco-manipulation tasks with evaluation metrics.",
  "landscape": "**Diffusion→trajectories→RL pipeline for G1 (direct paradigm validation):** DreamControl-v2 (arXiv 2604.00202, March 2026) is the most directly relevant prior work — it trains a guided diffusion model directly in G1's motion space using retargeted human motion data (AMASS, GRAB, Nymeria, OmniRetarget; 29.6K samples), generates reference trajectories conditioned on text and spatio-temporal controls, and trains downstream RL policies achieving 91-100% success across 8 tasks on real G1 hardware. Critically, DreamControl-v2 uses monolithic text-conditioned generation with no body-part compositional mechanism — trajectory diversity is bounded by training data. Our work extends this validated paradigm with compositional body-part generation: URDF-factored iterative conditioning enables N_loco × N_manip diverse trajectories from a single pre-trained model, targeting the diversity bottleneck that DreamControl-v2 does not address. DreamControl-v1 (arXiv 2509.14353) used an off-the-shelf human-space diffusion model with IK, requiring manual trajectory filtering; v2's robot-space training eliminates this, paralleling our use of Kimodo's robot-space model. Zhang et al. (arXiv 2604.17335, ETH Zurich, April 2026) concurrently validate the diffusion→tracking→RL pipeline for whole-body humanoid locomotion, training a diffusion model on retargeted human motions for terrain-aware reference generation with RL-based tracking, targeting terrain-adaptive locomotion rather than compositional loco-manipulation.\n\n**Body-part compositional motion diffusion (human motion space):** MixerMDM (CVPR 2025, arXiv 2504.01019) is the closest prior art for body-part composition — it learns spatial mixing weights (per-joint, per-timestep) to blend denoising outputs of two frozen pre-trained motion diffusion models. Key differences: MixerMDM composes *frozen* models via simultaneous weighted blending (score composition), operates in SMPL/HumanML3D space, and evaluates motion quality metrics (FID, alignment) rather than downstream RL policy performance. FrankenMotion (arXiv 2601.10909, Jan 2026) trains a diffusion model with part-level temporally-structured text prompts in SMPL space — critically, they found that naive body-part composition produces 'unsmooth transitions,' motivating purpose-built part-level training. Motion-Adapter (arXiv 2604.16135, April 2026) addresses compound action synthesis via attention-mask-guided denoising. CompDiffuser (NeurIPS 2025 Spotlight, arXiv 2503.05153) achieves compositional trajectory stitching through temporal overlap and bidirectional diffusion — a temporal analog to our spatial body-part approach. EnergyMoGen (CVPR 2025) and DeMoGen (arXiv 2512.22324, Dec 2025) compose motions via energy-based diffusion. All operate in human motion space without physics validation or robot RL evaluation, and all employ score-composition approaches that suffer from the documented failure modes (mode-averaging, factorization violations, boundary artifacts) that our iterative conditional generation avoids.\n\n**Physics-based masked motion controllers (NVIDIA):** MaskedMimic (SIGGRAPH Asia 2024, arXiv 2409.14393) formulates physics-based character control as motion inpainting via random body-part masking. MaskedManipulator (SIGGRAPH Asia 2025, arXiv 2505.19086) extends MaskedMimic to whole-body loco-manipulation. Both use C-VAE/RL architectures (not diffusion), train from scratch via RL+distillation, and produce real-time controllers rather than trajectory datasets. Our work brings MaskedMimic's masking insight into the diffusion paradigm on a pre-trained robot-specific model.\n\n**Diffusion-based humanoid control with inpainting:** BeyondMimic (arXiv 2508.08241, UC Berkeley) proposes a unified latent diffusion model for humanoid control that supports motion inpainting, skill composition, and dynamic behavior switching via classifier guidance, with zero-shot sim-to-real transfer. While it targets real-time control rather than trajectory dataset generation for downstream RL, its diffusion-based inpainting and composition approach validates that diffusion models can generalize to novel conditioning patterns at inference time.\n\n**Robot motion diffusion (G1-specific):** Kimodo (NVIDIA, arXiv 2603.15546, March 2026) is a 282M-parameter two-stage transformer denoiser trained on 288h BONES-SEED (SEED variant), generating G1 motions from text in 2-5s. Its constraint conditioning uses binary masking with imputation and dual classifier-free guidance (x̂₀ = D∅ + w_text(D_text - D∅) + w_constr(D_constr - D∅), default w_text=w_constr=2). Phase 2 training uses specific constraint patterns: full-body keyframes, random subsets of hands/feet positions/rotations, 2D root position/heading, foot contact configurations. Body-part-level masks are NOT in its training distribution — our use of body-part masking is OOD and constitutes an empirical hypothesis. MotionBricks (NVIDIA, arXiv 2604.24833, April 2026) provides real-time latent generative motion for G1 with training code, but uses VQVAE + latent backbone (not diffusion). REFINE-DP (arXiv 2603.13707, March 2026) demonstrates diffusion policy fine-tuning via RL for humanoid loco-manipulation but does not address compositional generation. Psi0 (arXiv 2603.12263, March 2026) is a VLA foundation model using flow-based action prediction. WholeBodyVLA (ICLR 2026) proposes a unified latent VLA for whole-body loco-manipulation control using vision-language-action learning from egocentric videos, but does not use diffusion-based trajectory generation.\n\n**Mask-agnostic diffusion inpainting:** RePaint (CVPR 2022, arXiv 2201.09865) demonstrated that pre-trained DDPMs can perform inpainting with arbitrary binary masks — including patterns never seen during training — by replacing masked regions with noised target values at each denoising step. Its resampling trick (re-noising and re-denoising at mask boundaries) improves coherence at the cost of additional denoising steps. CondMDI (SIGGRAPH 2024, arXiv 2405.11126) applies imputation-based conditioning to motion in-betweening, training with randomly sampled joints and keyframes, and demonstrating generalization to various spatial constraint patterns including single-joint trajectories — providing domain-specific evidence for mask-pattern generalization in motion diffusion. We adopt the imputation principle for body-part conditioning: Kimodo's imputation mechanism (x̃_t = m ⊙ x_gt + (1-m) ⊙ x_t) is structurally identical to RePaint's approach. Whether this generalizes from image DDPMs and human-motion diffusion to Kimodo's robot-specific transformer with dual CFG is our central empirical question.\n\n**Classifier-free guidance failure modes (motivating w_constr sweep):** CFG++ (Chung et al., ICLR 2025, arXiv 2406.08070) reveals that standard CFG's drawbacks — lack of invertibility and mode collapse at high guidance scales — stem from off-manifold extrapolation, and proposes manifold-constrained guidance via inverse-problem reformulation. S-CFG (Shen et al., CVPR 2024, arXiv 2404.05384) demonstrates that a global CFG scale creates spatial inconsistency across semantically distinct regions, proposing per-region adaptive guidance. Annealing Guidance (Yehezkel et al., SIGGRAPH Asia 2025, arXiv 2506.24108) proposes learning a dynamic schedule that adapts guidance scale throughout denoising. These works collectively motivate our experimental design: for OOD body-part masks, constraint guidance (w_constr>0) may amplify unreliable D_constr predictions, pushing trajectories off-manifold. Testing w_constr ∈ {0, 0.5, 1.0, 2.0} disentangles the contributions of imputation (mask-agnostic, theoretically robust to OOD) versus guidance (distribution-dependent, potentially harmful for OOD).\n\n**Compositional diffusion theory:** Reduce Reuse Recycle (Du et al., ICML 2023) identifies bias in naive score composition and proposes MCMC correction. Mechanisms of Projective Composition (Bradley et al., ICML 2025) proves score composition requires approximate factorization — violated for kinematically coupled body parts. Refining Compositional Diffusion (arXiv 2605.03075, May 2026) documents mode-averaging in compositional diffusion planning. These works provide the theoretical motivation for our iterative conditional generation approach (sequential complete processes) over score composition (simultaneous/alternating within one process).\n\n**LoRA fine-tuning for diffusion models:** LoRA (Hu et al., ICLR 2022) is standard for parameter-efficient fine-tuning of diffusion transformers. We apply LoRA to Kimodo's attention layers for the first time.\n\n**Data generation for humanoid RL:** OmniRetarget (arXiv 2509.26633) provides 4.0h of publicly available G1 loco-manipulation trajectories. ProtoMotions provides GPU-accelerated physics tracking for G1.\n\nNo existing work uses a pre-trained robot motion diffusion model's imputation mechanism for systematic body-part compositional trajectory generation — disentangling imputation from guidance for OOD constraints, with iterative conditional generation as a principled alternative to score composition — followed by physics projection and downstream RL evaluation. DreamControl-v2 validates the pipeline paradigm; we extend it with compositional generation. The iterative conditional generation methodology is differentiated from all prior compositional approaches, which use score composition.",
  "approach": "We propose a framework testing whether Kimodo's imputation-based constraint conditioning generalizes to URDF-guided body-part masks for compositional loco-manipulation trajectory generation — an OOD application of RePaint-style inpainting principles to robot motion diffusion. The central methodological contribution is iterative conditional generation: unlike score-composition approaches (MixerMDM, EnergyMoGen, CompDiffuser) that compose body parts within a single denoising loop — suffering from mode-averaging (RCD, 2026), factorization violations (Bradley et al., ICML 2025), and boundary artifacts (FrankenMotion, 2026) — we run each body-part as a complete, independent diffusion process conditioned on the other's output, sampling from true conditionals rather than approximate factored distributions. The framework has two tiers: a zero-shot pipeline (primary contribution) that requires only Kimodo's inference API, and LoRA-enhanced generation (secondary contribution) that improves conditional quality via lightweight fine-tuning.\n\n**0. Preliminary Diversity and Guidance Analysis (Day 1-3).** Before the main pipeline, we establish (a) the empirical case for compositional generation over monolithic text prompting and (b) the interaction between constraint guidance and OOD body-part masks.\n\n  Diversity analysis: We generate N_text=50 compound text-prompted motions from Kimodo (e.g., 'walk toward the shelf while raising your right hand,' 'jog forward while waving both arms') and N_comp=50 compositionally generated motions (5 locomotion prompts × 10 manipulation prompts) using the zero-shot pipeline. Pre-registered success criterion: compositional generation is justified if mean pairwise joint-angle distance of compositional samples exceeds that of compound-text samples by >15% (or >1 standard deviation of the text-prompted distribution), measured via two-sided permutation test with 10,000 permutations at p<0.05. With N=50 per group and effect size d≥0.6, a permutation test achieves >80% power. If this criterion is not met, we pivot to analyzing when/why compositional generation fails — itself a valuable contribution that informs the field.\n\n  Guidance disentanglement: We test constraint guidance weight w_constr ∈ {0, 0.5, 1.0, 2.0} for body-part masks across all 50 compositional samples. This disentangles the contributions of imputation (mask replacement at each denoising step, theoretically robust to OOD per RePaint) versus guidance (CFG amplification of constraint adherence via D_constr, distribution-dependent and potentially counterproductive for OOD patterns). We hypothesize that w_constr=0 (pure imputation, no guidance) may outperform w_constr=2 (default) for OOD body-part masks, because: (a) with OOD constraints, D_constr (model output conditioned only on constraints) may be unreliable, and amplifying unreliable predictions via w_constr>0 pushes trajectories off-manifold (CFG++, ICLR 2025); (b) pure imputation does not require the constraint pattern to be in-distribution — it only requires the denoiser to produce locally coherent predictions at each step given the imputed values. We report: tracking success rate (ProtoMotions), joint-angle coherence at body-part boundaries, and generation FID for each w_constr setting. The best-performing w_constr is carried forward to full evaluation.\n\n**1. URDF-Guided Body-Part Factorization.** We parse the G1 URDF to define two kinematic subtrees: a lower-body group (root/pelvis, hips, knees, ankles, feet — locomotion, including boundary joints at the lower torso) and an upper-body group (torso, shoulders, elbows, wrists, hands — manipulation). This determines which of the 34 G1 joints are constrained vs. generated in each phase. The factorization is encoded as binary masks compatible with Kimodo's imputation format.\n\n**2. Iterative Conditional Generation with RePaint-Style Imputation (Primary Contribution).** We frame body-part composition as iterative conditional generation — a principled alternative to score composition for structured body-part composition, motivated by the compositional diffusion failure literature. Instead of composing scores within the denoising loop — which assumes approximate factorization (Bradley et al., ICML 2025), suffers from mode-averaging when local distributions are multimodal (RCD, 2026), and produces boundary artifacts (FrankenMotion, 2026) — we run sequential complete diffusion processes, each sampling from the true conditional distribution:\n\n  Phase 1 (Locomotion): Generate lower-body trajectory via Kimodo's full denoising (T=1000 steps) with locomotion text prompt and upper-body unconstrained.\n\n  Phase 2 (Manipulation): Generate upper-body trajectory via a second complete denoising with manipulation text prompt and lower-body joints fixed as constraints using Kimodo's imputation mechanism (x̃_t = m ⊙ x_lower + (1-m) ⊙ x_t). Constraint guidance weight w_constr is set to the value selected in the Day 1-3 analysis (we expect w_constr=0 for OOD masks based on the CFG off-manifold hypothesis). This generates from p(x_upper | x_lower, text_manip) — no factorization assumption needed.\n\n  Phase 2b (RePaint Resampling Variant): Following RePaint's resampling trick, we optionally add r=5-10 noise-denoise cycles at each denoising step near the body-part boundary (lower torso/pelvis joints), improving coherence between independently generated body parts. This costs r× more denoising steps at boundary joints but is trivial to implement with Kimodo's inference API.\n\n  Phase 3 (Optional Refinement): Re-generate lower-body conditioned on upper-body output, sampling from p(x_lower | x_upper, text_loco). 1-2 iterations suffice.\n\nDiversity is achieved by sampling different locomotion × manipulation combinations — the combinatorial product yields exponentially more compositions than exist in training data. The zero-shot pipeline requires NO modifications to Kimodo's code — only its public inference API with constraint inputs.\n\n**3. LoRA-Based Masked Fine-Tuning (Secondary Contribution).** While the zero-shot pipeline tests OOD generalization, LoRA fine-tuning can bring body-part conditioning into the training distribution, improving conditional quality. We implement a training loop from Kimodo's inference codebase — realistic scope is 500-800 lines of non-trivial PyTorch code covering:\n\n  (a) Data loading: BONES-SEED format parsing (motion representation with 6D rotations, smoothed root, temporal annotations) and OmniRetarget integration.\n  (b) LoRA injection: Rank-16 adapters into query/key/value projections of 16 transformer layers (~8M trainable parameters, ~3% of 282M total).\n  (c) Masked denoising objective: With probability p_mask=0.5, replace either upper-body or lower-body joint channels with Gaussian noise while preserving the other part's clean signal, computing loss only on masked joints. This directly trains the conditional distributions p(upper|lower,text_manip) and p(lower|upper,text_loco).\n  (d) Body-part text annotations: BONES-SEED includes up to 6 NL descriptions per motion plus temporal segmentation with precise timestamps. We derive body-part-specific labels via: (i) parsing existing descriptions for body-part keywords ('walking' → lower, 'reaching' → upper); (ii) supplementing with per-body-part joint velocity statistics via LLM prompting for ambiguous cases; (iii) manually verifying 100 random annotations against motion visualizations.\n  (e) Optimizer and training: Adam-atan2, lr=2e-5, Smooth L1 loss with published per-component weights, EMA decay 0.995. Training on BONES-SEED (288h, 142K motions) + OmniRetarget (4.0h).\n\n  No physics training losses: Physics consistency is handled entirely by post-generation projection.\n\n  Budget: 4-6 days for implementation, ~8-12h on 1×A100 for training.\n\n**4. Post-Composition Physics Projection.** After iterative conditional generation, a lightweight quadratic program (~0.1s per trajectory) optimizes for: (a) centroidal dynamics consistency between upper and lower body; (b) CoM within support polygon; (c) G1 joint torque limits from URDF. Trajectories failing projection (>5% of joints exceeding limits) are rejected and re-sampled.\n\n**5. Kinematic-to-Dynamic Pipeline.** Projected trajectories are converted to physics-validated RL demonstrations via ProtoMotions' GPU-accelerated tracking. Tracking success rate serves as a physics quality metric.\n\n**6. Evaluation on SkillBench (3 Tasks).** We evaluate on 3 SkillBench G1 tasks spanning difficulty levels: FarReach (Easy), BoxPush (Medium), PackageCarry (Hard). Baselines:\n  (1) **DreamControl-v2** — the primary paradigm baseline: diffusion→trajectories→RL with monolithic text conditioning (no body-part composition). We use their published results or reproduce using their pipeline.\n  (2) **Kimodo text-prompted** — compound text prompts (e.g., 'walk forward while reaching'). Tests whether Kimodo's LLM2Vec text encoding already handles compound prompts well enough.\n  (3) **Zero-shot iterative conditioning (w_constr=0, no resampling)** — our pipeline with pure imputation (no constraint guidance); isolates the value of imputation-only body-part factorization.\n  (4) **Zero-shot iterative conditioning (best w_constr from analysis)** — if w_constr>0 is selected, this tests whether guidance helps; if w_constr=0 wins, baselines 3 and 4 collapse.\n  (5) **Zero-shot + RePaint resampling** — adds noise-denoise cycles at body-part boundaries; tests whether resampling improves coherence.\n  (6) **LoRA-enhanced iterative generation** — our full pipeline; isolates the value of LoRA fine-tuning.\n  (7) **OmniRetarget** — optimization-based G1 trajectories (4.0h available).\n  (8) **Naive concatenation** — lower-body from one sample + upper-body from another, no conditioning (ablation).\n\n  Key metrics: downstream RL policy success rate (primary), trajectory diversity (mean pairwise distance in joint-angle space), physics violation rate (ProtoMotions tracking failure rate), and data efficiency curve.\n\n**Early Checkpoint (Day 8-10).** Before committing to full SkillBench evaluation, we evaluate: (a) zero-shot imputation quality across w_constr settings — does Kimodo produce coherent motions with body-part masks at any guidance level? If coherence is poor (<30% tracking success at all w_constr values), the OOD hypothesis is rejected and we focus the paper on the LoRA approach; (b) zero-shot vs. RePaint-resampled vs. LoRA-tuned conditional generation quality using FID and diversity metrics on held-out BONES-SEED motions. This checkpoint determines which variants to carry forward to full RL evaluation.\n\n**Possible Outcomes and Their Contributions:**\n  (a) Zero-shot works well at w_constr=0 → demonstrates that pure imputation (without guidance) generalizes to OOD body-part masks in robot motion diffusion, and that guidance is counterproductive for OOD constraints. Novel finding with practical implications for constraint-based diffusion generation.\n  (b) Zero-shot works at w_constr>0 → demonstrates that both imputation and guidance generalize to OOD, stronger than (a).\n  (c) Zero-shot fails, LoRA succeeds → demonstrates that body-part conditioning requires explicit training but can be achieved efficiently via LoRA, with guidance disentanglement analysis informing the failure mode.\n  (d) Both improve diversity but not RL performance → reveals that trajectory diversity alone is insufficient for downstream policy quality, an important negative result.\n  (e) Compositional generation underperforms text-prompted → establishes empirical limits of factored generation, also valuable, with guidance analysis providing mechanistic explanation.\n\n**Key Differentiation.** From DreamControl-v2: compositional body-part generation enabling combinatorial diversity vs. monolithic text conditioning; uses pre-trained Kimodo (not custom-trained diffusion); tests OOD constraint generalization with guidance disentanglement. From MixerMDM: robot-specific model, LoRA fine-tuning, iterative conditional generation (not score composition), downstream RL evaluation. From MaskedMimic: diffusion not C-VAE/RL, LoRA fine-tune pre-trained model, trajectory datasets not real-time controllers. From BeyondMimic: trajectory dataset generation for downstream RL amplification vs. real-time latent diffusion control; URDF-structured body-part factorization vs. classifier-guided composition. Methodologically: iterative conditional generation (sequential complete processes) as a principled alternative to score composition, supported by the compositional diffusion failure literature and validated empirically.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~65-95h A100/H100",
      "gpu_utilization": "High (65-75%): LoRA fine-tuning (~8-12h on 1 A100); iterative conditional generation with w_constr sweep uses Kimodo inference (4× conditions adds ~3h); ProtoMotions tracking established",
      "timeline": "20-22 days",
      "team": "1-2 researchers familiar with diffusion models and PyTorch LoRA",
      "estimated_gpu_cost": "$195-285 (at ~$3.00/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "~75-105h A100/H100",
      "gpu_utilization": "Moderate-high (55-65%): agent runs LoRA training, w_constr sweep, and evaluation; human reviews annotation quality and trajectory visualizations",
      "timeline": "16-20 days — feasible for CoRL 2026 (16 days to abstract May 26, 19 to paper May 29)",
      "team": "1 researcher, ~30min/day reviewing annotations and trajectory quality",
      "claude_api_cost": "$30-80 (estimated 300-800 turns at ~$0.10/turn)",
      "estimated_gpu_cost": "$225-315",
      "risk_note": "Primary risk: zero-shot imputation may not generalize to body-part masks at ANY w_constr value (OOD failure across all guidance settings). Mitigation: (a) early checkpoint at Day 8-10 tests this directly with w_constr sweep; (b) pure imputation (w_constr=0) is the most theoretically grounded fallback; (c) RePaint resampling as boundary-coherence fallback; (d) LoRA fine-tuning as alternative that brings body-part masks into training distribution; (e) negative results (OOD failure analysis with guidance disentanglement) are themselves publishable. Secondary risk: LoRA training implementation takes 4-6 days (500-800 lines), consuming significant timeline. Mitigation: early checkpoint strategy determines whether LoRA is needed before full implementation."
    },
    "auto_research": {
      "gpu_hours": "~85-115h A100/H100",
      "gpu_utilization": "Near-zero idle (<10%): w_constr sweep, LoRA fine-tuning, iterative generation, physics projection, ProtoMotions tracking, and SkillBench RL run back-to-back",
      "timeline": "12-16 days with 2-4 concurrent A100 GPUs",
      "team": "0 (initial setup: provide Kimodo G1-SEED-v1 checkpoint path, BONES-SEED data, SkillBench config)",
      "claude_api_cost": "$80-180 (estimated 800-1800 turns)",
      "estimated_gpu_cost": "$255-345",
      "speed_bottleneck": "LoRA training implementation: 4-6 days (500-800 lines); LoRA fine-tuning: ~8-12h on 1×A100; SkillBench RL: ~15-25h per task on 1×A100, parallelized across 3 GPUs",
      "risk_note": "Agent should run preliminary diversity+guidance analysis (Day 1-3) and early checkpoint evaluation (Day 8-10) comparing zero-shot across w_constr settings vs. resampled vs. LoRA conditional quality before committing to full SkillBench"
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract deadline: May 26, 2026; paper deadline: May 29, 2026) — PRIMARY",
    "Humanoids 2026 (paper deadline: July 24, 2026) — SECONDARY (extended version with full 8-task SkillBench, iterative refinement analysis, and additional ablations)",
    "ICRA 2027 (paper deadline: September 16, 2026) — BACKUP"
  ],
  "level": "top-tier",
  "key_references": [
    "Kimodo: Scaling Controllable Human Motion Generation (NVIDIA, arXiv 2603.15546, March 2026) — backbone model with imputation-based constraint conditioning and dual CFG (x̂₀ = D∅ + w_text(D_text - D∅) + w_constr(D_constr - D∅), default w_text=w_constr=2), G1-SEED-v1 checkpoint on HuggingFace. NOTE: public repo provides inference only, no training code. Body-part masks are OOD; w_constr interaction with OOD masks is a central experimental variable.",
    "DreamControl-v2: Simpler and Scalable Autonomous Humanoid Skills via Trainable Guided Diffusion Priors (arXiv 2604.00202, March 2026) — validates diffusion→trajectories→RL pipeline for G1 with 91-100% success across 8 tasks; monolithic text conditioning without body-part composition; primary paradigm baseline",
    "DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion (arXiv 2509.14353, 2025) — original version using human-space diffusion prior with manual filtering",
    "RePaint: Inpainting using Denoising Diffusion Probabilistic Models (Lugmayr et al., CVPR 2022, arXiv 2201.09865) — demonstrates that pre-trained DDPMs generalize to arbitrary inpainting masks via step-by-step imputation without guidance; resampling trick improves boundary coherence; theoretical foundation for our pure-imputation (w_constr=0) approach to OOD body-part masking",
    "CFG++: Manifold-Constrained Classifier Free Guidance for Diffusion Models (Chung et al., ICLR 2025, arXiv 2406.08070) — reveals that standard CFG extrapolation pushes samples off the data manifold, causing mode collapse and artifacts at high guidance scales; motivates our hypothesis that w_constr>0 may be counterproductive for OOD body-part constraints",
    "Rethinking the Spatial Inconsistency in Classifier-Free Diffusion Guidance (Shen et al., CVPR 2024, arXiv 2404.05384) — demonstrates that uniform CFG scale creates spatial inconsistency across semantically distinct regions; proposes per-region adaptive guidance; motivates region-aware constraint guidance for body-part masks",
    "Navigating with Annealing Guidance Scale in Diffusion Space (Yehezkel et al., SIGGRAPH Asia 2025, arXiv 2506.24108) — proposes learned dynamic guidance schedule adapting to denoising trajectory; alternative to fixed w_constr for future work",
    "CondMDI: Flexible Motion In-betweening with Diffusion Models (Cohan et al., SIGGRAPH 2024, arXiv 2405.11126) — trains motion diffusion with randomly sampled joints and keyframes, demonstrating generalization to diverse spatial constraint patterns; domain-specific evidence for mask-pattern generalization in motion diffusion",
    "MixerMDM: Learnable Composition of Human Motion Diffusion Models (CVPR 2025, arXiv 2504.01019) — closest prior art for body-part composition: learned spatial mixing weights via score composition in SMPL space; subject to mode-averaging and factorization violation failure modes",
    "MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting (SIGGRAPH Asia 2024, arXiv 2409.14393) — body-part masking insight for conditional motion synthesis via C-VAE/RL",
    "MaskedManipulator: Versatile Whole-Body Control for Loco-Manipulation (SIGGRAPH Asia 2025, arXiv 2505.19086) — extends MaskedMimic to loco-manipulation",
    "BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion (arXiv 2508.08241, UC Berkeley) — unified latent diffusion for humanoid control with motion inpainting, skill composition, and classifier-guided generalization to unseen tasks; validates diffusion-based inference-time generalization",
    "CompDiffuser: Generative Trajectory Stitching through Diffusion Composition (NeurIPS 2025 Spotlight, arXiv 2503.05153) — temporal compositional trajectory stitching via score composition; subject to documented failure modes",
    "FrankenMotion: Part-level Human Motion Generation and Composition (arXiv 2601.10909, Jan 2026) — documents failure of naive body-part score composition ('unsmooth transitions') in SMPL space; motivates our iterative conditional generation approach",
    "Motion-Adapter: A Diffusion Model Adapter for Text-to-Motion Generation of Compound Actions (arXiv 2604.16135, April 2026) — attention-mask-guided compound action synthesis",
    "REFINE-DP: Diffusion Policy Fine-tuning for Humanoid Loco-manipulation via Reinforcement Learning (arXiv 2603.13707, March 2026) — RL fine-tuning of diffusion policies for humanoid control",
    "MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model (NVIDIA, arXiv 2604.24833, April 2026) — sibling project to Kimodo with G1 training code, different architecture",
    "Psi0: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (arXiv 2603.12263, March 2026) — VLA foundation model with flow-based action prediction",
    "Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking (Zhang et al., arXiv 2604.17335, ETH Zurich, April 2026) — concurrent validation of diffusion→tracking→RL pipeline for terrain-aware G1 locomotion; targets locomotion not compositional loco-manipulation",
    "WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026, arXiv 2512.11047) — unified VLA for humanoid loco-manipulation via egocentric video learning; different paradigm (VLA, not diffusion trajectory generation)",
    "MDM: Human Motion Diffusion Model (Tevet et al., ICLR 2023, arXiv 2209.14916) — demonstrated spatial body-part inpainting in human motion diffusion via imputation; supports feasibility of body-part mask generalization",
    "Reduce Reuse Recycle: Compositional Generation with Energy-Based Diffusion Models and MCMC (Du et al., ICML 2023) — identifies bias in naive score composition",
    "Mechanisms of Projective Composition of Diffusion Models (Bradley et al., ICML 2025, arXiv 2502.04549) — proves score composition requires approximate factorization; violated for kinematically coupled body parts, motivating our iterative conditional generation",
    "Refining Compositional Diffusion for Reliable Long-Horizon Planning (arXiv 2605.03075, May 2026) — documents mode-averaging in compositional diffusion planning; motivates sequential complete processes over within-loop composition",
    "LoRA: Low-Rank Adaptation of Large Language Models (Hu et al., ICLR 2022) — parameter-efficient fine-tuning for transformers",
    "BONES-SEED: Skeletal Everyday Embodiment Dataset (Bones Studio, March 2026) — 142K motions, 288h, up to 6 NL descriptions per motion, temporal segmentation, G1 retargeting on HuggingFace",
    "OmniRetarget: Interaction-Preserving Data Generation for Humanoid Loco-Manipulation (arXiv 2509.26633) — 4.0h publicly available G1 loco-manipulation data on HuggingFace",
    "SkillBlender: Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending (arXiv 2506.09366, 2025) — SkillBench benchmark with 8 G1 tasks",
    "ProtoMotions: GPU-Accelerated Simulation and Learning Framework (NVIDIA, open-source) — kinematic-to-dynamic tracking for G1",
    "PhysDiff: Physics-Guided Human Motion Diffusion Model (NVIDIA, ICCV 2023) — physics-based motion projection during sampling",
    "EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion (CVPR 2025)",
    "DeMoGen: Decompositional Human Motion Generation with Energy-Based Diffusion (arXiv 2512.22324, Dec 2025)",
    "Factorized Diffusion Policy: Flexible Multitask Learning (arXiv 2512.21898, RSS 2025 Workshop)"
  ],
  "description": "We address compositional generation of diverse, physically plausible humanoid loco-manipulation demonstrations by testing whether a pre-trained robot motion diffusion model's imputation-based constraint conditioning generalizes to URDF-guided body-part masks — an out-of-distribution application that we frame as RePaint-style inpainting in robot motion space. Our central methodological contribution is iterative conditional generation: unlike score-composition approaches (MixerMDM, EnergyMoGen, CompDiffuser) that compose body parts within a single denoising loop — suffering from mode-averaging (RCD, 2026), factorization violations (Bradley et al., ICML 2025), and boundary artifacts (FrankenMotion, 2026) — we run each body-part as a complete, independent diffusion process conditioned on the other's output, sampling from true conditionals p(upper|lower,text) and p(lower|upper,text) without factorization assumptions. Building on Kimodo's open-source G1-SEED-v1 model (282M parameters, trained on 288h BONES-SEED data), we observe that its constraint imputation mechanism (x̃_t = m ⊙ x_gt + (1-m) ⊙ x_t) is mathematically identical to RePaint's mask-agnostic inpainting — but Kimodo was trained with end-effector and keyframe constraint patterns, not body-part masks. A critical and previously unaddressed complication is Kimodo's dual classifier-free guidance (x̂₀ = D∅ + w_text(D_text - D∅) + w_constr(D_constr - D∅)): recent literature (CFG++, ICLR 2025; S-CFG, CVPR 2024) demonstrates that CFG extrapolation pushes samples off the data manifold, and with OOD body-part masks, the constraint-conditioned prediction D_constr may itself be unreliable — amplifying it via w_constr>0 could produce severe off-manifold artifacts. We therefore introduce constraint guidance weight w_constr as a key experimental variable, testing w_constr ∈ {0, 0.5, 1.0, 2.0} to disentangle the contributions of imputation (mask replacement at each step, theoretically robust to OOD per RePaint) versus guidance (CFG amplification of constraint adherence, distribution-dependent and potentially harmful for OOD). We hypothesize that w_constr=0 (pure imputation, no guidance) may outperform default w_constr=2 for OOD body-part masks. We introduce a two-tier framework: (1) a zero-shot iterative conditional generation pipeline (primary contribution) that uses URDF-guided body-part factorization to decompose G1's 34 joints into locomotion and manipulation subtrees, then runs sequential complete diffusion processes — first generating lower-body locomotion, then upper-body manipulation conditioned on fixed lower-body constraints via Kimodo's imputation — with an optional RePaint resampling variant (noise-denoise cycles at body-part boundaries for improved coherence), followed by post-composition physics projection via quadratic programming; (2) LoRA-based masked fine-tuning (secondary contribution, 500-800 lines of implementation, 4-6 days) that injects rank-16 adapters (~8M trainable parameters) into Kimodo's transformer attention layers with a masked denoising objective inspired by MaskedMimic, explicitly training the conditional distributions p(upper|lower,text) and p(lower|upper,text) to bring body-part conditioning into the training distribution. A preliminary diversity and guidance analysis (Day 1-3) establishes (a) whether compositional generation produces measurably more diverse trajectories than Kimodo's compound text prompts, with pre-registered success criterion: >15% improvement in mean pairwise joint-angle distance via permutation test at p<0.05, and (b) the optimal w_constr for OOD body-part masks. An early checkpoint (Day 8-10) tests zero-shot imputation quality across guidance settings, RePaint resampling, and LoRA-enhanced generation. DreamControl-v2 validates the diffusion→trajectories→RL pipeline paradigm for G1; we extend this paradigm with compositional body-part generation, guidance disentanglement for OOD constraints, and iterative conditional generation as a principled alternative to score composition. Generated trajectories are converted to physics-validated demonstrations via ProtoMotions. We evaluate on 3 SkillBench G1 tasks against eight baselines including DreamControl-v2, Kimodo text-prompted, and ablations across w_constr settings. The approach requires ~65-115h A100 and targets CoRL 2026 (16-20 day timeline).",
  "project_name": "kintree_traj_diffusion",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL — Missing related work: FrankenMotion (arXiv 2601.10909, Jan 2026) does part-level body decomposition for compositional motion generation using diffusion; DeMoGen (arXiv 2512.22324, Dec 2025) does decompositional motion generation with energy-based diffusion; EnergyMoGen (CVPR 2025) composes motions via energy-based diffusion; KinMo (ICCV 2025) does kinematic-aware body-part-level generation. These directly undermine the claim that 'no existing work combines kinematic-tree factored diffusion with compositional trajectory generation.'", "CRITICAL — Kimodo (NVIDIA, arXiv 2603.15546) is not listed as a data generation baseline despite already generating G1 demonstrations from text, being open-source, and using a related root/body decomposition. It is a much stronger baseline than acknowledged and should be the primary comparison for data generation quality.", "CRITICAL — Compute budget likely exceeds the user's ≤200 H100-hour constraint. The proposal estimates 300-500 A100-hours for diffusion training alone (~150-250 H100-hours). Adding downstream RL evaluation on 8 SkillBench tasks (~20-50 H100-hours), physics validation rollouts (~10-20 H100-hours), and necessary ablations (~30-50 H100-hours) pushes total to ~210-370 H100-hours.", "HIGH — The 20-day timeline is unrealistic for: (a) implementing a novel GNN-based graph diffusion architecture with no reference implementation for the cross-attention torso-hub coordination, (b) training the model, (c) generating 500K trajectories with physics validation, (d) training downstream RL policies on 8+ tasks, (e) reproducing DreamControl-v2 and SkillBlender baselines, and (f) writing the paper.", "HIGH — Cross-attention at the torso hub is architecturally unproven for enforcing physics constraints (balance, momentum consistency, ground contact). Attention mechanisms learn soft correlations, not hard physical constraints. The proposal needs explicit physics loss terms or post-processing beyond cross-attention, which adds implementation complexity.", "MODERATE — DreamControl-v2 code has not been confirmed as open-source. If not available, reproducing it as a baseline within 20 days adds significant overhead. The proposal should confirm baseline reproducibility or choose baselines with available code.", "MODERATE — AMASS retargeted for G1 (~11K motions) and BONES-SEED (142K annotations) are primarily locomotion and everyday activities. The scarcity of manipulation demonstrations in this training data means the arm/hand subtree distributions may be poorly learned, undermining the compositional mixing claim for loco-manipulation.", "MODERATE — The resource estimates across modes are not internally consistent with the user's constraints. All three modes (manual, HIL, auto) specify A100-hours but the user's constraint is ≤200 H100-hours. Manual mode at 300-500 A100-hours and auto at 600-1000 A100-hours both need recalibration."]
Feedback: The idea has a genuine kernel of novelty in applying kinematic-tree-structured GNN diffusion to robot trajectory data amplification, but it needs significant revision to be viable for CoRL 2026 under the stated constraints:

1. **Address the body-part compositional generation literature**: FrankenMotion, DeMoGen, EnergyMoGen, and KinMo all decompose motion by body parts and compose novel combinations. You MUST differentiate clearly — the key differentiator is: (a) operating on robot joint-space trajectories rather than human motion, (b) using explicit kinematic-tree GNN structure rather than semantic body groups, and (c) physics-validated data amplification for downstream policy training. Frame these as the actual novel contributions.

2. **Add Kimodo as the primary baseline**: Kimodo is open-source, generates G1 data from text, and uses root/body decomposition. The paper must show that kinematic-tree factoring produces higher-quality or more diverse training data than Kimodo. This is the main comparison reviewers will demand.

3. **Reduce scope to fit ≤200 H100-hours**: Consider: (a) reducing to 3-4 SkillBench tasks instead of 8, (b) using Kimodo as a data source (fine-tune on Kimodo-generated data rather than training from scratch on AMASS), (c) simplifying the GNN architecture — start with a 2-level factorization (upper body / lower body) before claiming full kinematic-tree factoring.

4. **Reduce timeline risk**: Use existing code maximally. KStar Diffuser code (CVPR 2025) provides the spatial-temporal graph diffusion backbone. ABD-Net provides URDF-to-graph parsing. Start from these codebases rather than implementing from scratch. Consider a simpler coordination mechanism than cross-attention — e.g., a shared latent variable at the torso that conditions both subtree denoisers.

5. **Add physics loss terms**: Cross-attention alone won't enforce physical plausibility. Add explicit loss terms for center-of-mass balance, joint torque limits, and contact consistency during training, not just post-hoc physics filtering.

6. **Clarify manipulation data sources**: If AMASS/BONES-SEED lack sufficient manipulation data, consider supplementing with DexMimicGen or RoboCasa demonstrations for the arm/hand subtrees.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL — Venue and timeline mismatch: User explicitly requested CoRL 2026 (abstract deadline May 26, paper deadline May 29, ≤20 days). The proposal targets Humanoids 2026 (July 24) as PRIMARY and does not list CoRL 2026 at all. The manual timeline of 8-10 weeks directly violates the user's 20-day hard constraint. Either (a) scope down drastically to fit CoRL 2026, or (b) explicitly justify abandoning CoRL with user agreement.", "HIGH — KStar Diffuser (CVPR 2025, Huawei Noah's Ark Lab) has NO publicly available code or GitHub repository. The proposal claims 'We build on three existing codebases: (1) KStar Diffuser provides the spatial-temporal graph diffusion backbone' — this is not possible without full reimplementation from the paper. This adds weeks of development time not accounted for in the timeline.", "HIGH — ABD-Net (arXiv 2603.19078) has NO publicly available code. The proposal claims ABD-Net 'provides URDF-to-graph parsing utilities for G1' — no such utilities are publicly available. URDF-to-graph parsing must be implemented from scratch (feasible but the effort is understated).", "HIGH — Missing closely related work: G-DReaM (arXiv 2505.20857, May 2025) uses graph-conditioned diffusion on robot morphological structure with joint-level attention for cross-embodiment motion generation. While it targets retargeting rather than compositional generation, it validates the core paradigm of graph-structured diffusion for robot motion and must be cited and differentiated against.", "MODERATE — Missing related work: UniMorphGrasp (arXiv 2602.00915, Jan 2026) uses URDF-derived kinematic graph features in diffusion with a hierarchical kinematic tree loss for cross-embodiment dexterous grasping. The kinematic tree loss concept is directly relevant to KinoTreeDiffuse's physics-informed training losses.", "MODERATE — DexMimicGen was built for bimanual Panda arms and the Fourier GR-1 humanoid, NOT the Unitree G1. Retargeting DexMimicGen trajectories to G1 arms/hands requires adding G1 URDF support, recalibrating subtask decomposition, and handling different hand configurations. This is non-trivial engineering work presented as straightforward.", "MODERATE — The proposal does not convincingly argue why compositional generation via factored diffusion outperforms prompting Kimodo with diverse text descriptions. Kimodo already generates G1 motions from text prompts ('walk while reaching for object') in 2-5 seconds. The key ablation missing: KinoTreeDiffuse compositional samples vs. Kimodo text-prompted loco-manipulation samples, evaluated on downstream RL policy diversity and success rate.", "LOW — Kimodo generates kinematic motions only. The pipeline doesn't address the kinematic-to-dynamic gap: generated trajectories need physics-based tracking (e.g., via ProtoMotions or sim-based tracking) before they can serve as RL demonstration data. This step's compute cost should be accounted for."]
Feedback: The revision addressed Round 1 concerns well (simplified architecture, added baselines, reduced scope, added physics losses). The core idea — compositional humanoid trajectory generation via kinematic-tree-factored diffusion — remains genuinely novel and potentially impactful. However, several critical issues remain:

1. **Fix the venue/timeline mismatch**: Either (a) drastically simplify to fit CoRL 2026's 20-day deadline — e.g., use Kimodo as the backbone and add only the 2-level factorization as a fine-tuning layer, skipping full reimplementation of KStar Diffuser; or (b) get explicit user agreement to target Humanoids 2026 instead. A 20-day version would need to use Kimodo's codebase directly (which IS open-source) rather than KStar Diffuser (which is not).

2. **Rebuild implementation strategy around available code**: KStar Diffuser and ABD-Net have no public code. Feasible alternatives: (a) Build graph diffusion using PyTorch Geometric + standard DDPM/DDIM, which is ~2 weeks of work for an experienced researcher; (b) Use Kimodo's open-source G1 motion representation and diffusion architecture as the backbone, adding the 2-level factorization as a modification to Kimodo's existing root/body decomposition; (c) Implement URDF-to-graph parsing directly using PyBullet or urdfpy (simple — URDF is just a tree).

3. **Cite and differentiate from G-DReaM and UniMorphGrasp**: G-DReaM uses graph-conditioned diffusion on robot morphology for retargeting — differentiate by emphasizing compositional generation (not retargeting) and the 2-level factorization architecture. UniMorphGrasp uses kinematic-tree-aware losses in diffusion for grasping — differentiate by emphasizing temporal trajectory generation vs. static pose generation.

4. **Add a 'Kimodo text-prompted loco-manipulation' baseline**: This is the baseline reviewers will most demand. Generate loco-manipulation trajectories by prompting Kimodo with compound text descriptions and compare downstream RL performance against KinoTreeDiffuse's compositional samples. If you can't beat this baseline, the compositional approach isn't justified.

5. **Simplify DexMimicGen dependency**: Either drop DexMimicGen from the multi-source training data (use Kimodo + OmniRetarget + AMASS-retargeted data instead), or explicitly budget 1-2 weeks for G1 adaptation of DexMimicGen.

### Round 3 review
Verdict: revise
Issues: ["HIGH — Missing critical related work: MixerMDM (CVPR 2025, arXiv 2504.01019) performs learned body-joint-level composition of frozen pre-trained motion diffusion models with spatial mixing weights — this is the closest prior art for body-part compositional diffusion and is not cited. It uses simultaneous weighted blending rather than alternating denoising, but the core paradigm (compose diffusion models at the body-part level during denoising) is directly overlapping. Must be cited and clearly differentiated.", "HIGH — Missing critical related work: MaskedMimic (NVIDIA, SIGGRAPH Asia 2024, arXiv 2409.14393) trains with random body-part masking to learn a unified model that synthesizes full-body motion from partial (masked) joint constraints — conceptually identical to the proposed masked body-part fine-tuning objective. MaskedMimic is implemented in ProtoMotions (which the proposal already depends on) and comes from NVIDIA (same lab as Kimodo). Using their masking idea without citation would be a critical omission. MaskedMimic uses C-VAE rather than diffusion, which is a valid distinction, but the insight is the same.", "HIGH — Alternating body-part denoising faces documented theoretical problems that are not addressed: (1) Mode-averaging when component distributions are multimodal, producing samples that are 'neither locally feasible nor globally coherent' (documented in Refining Compositional Diffusion, 2025; CDGS, 2026); (2) Score composition via product-of-experts only holds when conditional distributions approximately factorize (Mechanisms of Projective Composition, 2025), which is violated by tight upper-lower body dynamic coupling (angular momentum compensation, centroidal dynamics, balance recovery all couple body parts); (3) FrankenMotion (Jan 2026) explicitly found that naive body-part composition with MDM produces 'unsmooth transitions' and required purpose-built part-level training data and architecture. The proposal needs either MCMC-corrected sampling (as in Reduce Reuse Recycle, ICML 2023), physics-based projection during denoising steps, or an honest discussion of these limitations.", "MODERATE — The 'torso coupling term' (weighted average of both denoisers' predictions based on predicted noise variance) is ad-hoc and underspecified. There is no theoretical justification for why noise-variance-weighted averaging at the body-part boundary produces physically consistent motions. Consider: (a) a physics-based projection step that enforces whole-body constraints (CoM, angular momentum) after each denoising step, or (b) a learned coupling module trained on full-body trajectories, or (c) framing this as classifier-free guidance with body-part conditions.", "MODERATE — Missing related work: Motion-Adapter (arXiv 2604.16135, April 2026) addresses compound action synthesis (multiple concurrent body-part actions) in text-to-motion diffusion via attention masks. Also missing: Factorized Diffusion Policy (arXiv 2512.21898, RSS 2025 Workshop) factorizes diffusion into compositional sub-models with score aggregation. Both should be cited for completeness.", "LOW — OmniRetarget HuggingFace dataset contains 4.0 hours of G1 trajectories (verified on huggingface.co/datasets/omniretarget), not '8+ hours' as claimed. Also, Kimodo model weights use NVIDIA Open Model License, not Apache 2.0 — only the code is Apache 2.0. These inaccuracies should be corrected."]
Feedback: The proposal has improved substantially from Rounds 1-2: it correctly targets CoRL 2026, builds on available infrastructure (Kimodo, ProtoMotions, SkillBench), fits within compute constraints, and includes the right baselines. The core remaining problem is **theoretical grounding of the compositional sampling mechanism** and **two critical citation gaps**. Here is how to address each:

1. **Cite and differentiate from MixerMDM and MaskedMimic.** MixerMDM (CVPR 2025) composes frozen diffusion models at the body-joint level via learned blending weights — differentiate by emphasizing that KinoTreeDiffuse uses URDF-structured factorization with masked fine-tuning (not frozen models), and alternating denoising (not simultaneous blending). MaskedMimic (SIGGRAPH Asia 2024, NVIDIA) trains with random body-part masking for motion completion — differentiate by noting it uses C-VAE (not diffusion), requires training from scratch via RL+distillation (not fine-tuning a pre-trained model), and targets character animation (not robot trajectory generation for downstream RL). Frame your contribution as: 'We bring MaskedMimic's masking insight into the diffusion fine-tuning paradigm on Kimodo's robot-specific representation, and extend MixerMDM's compositional diffusion from blending to structured alternating denoising with physics enforcement.'

2. **Address the alternating denoising failure modes.** Three concrete options (implement at least one):
   (a) **Physics-based projection after each denoising step** — after alternating upper/lower denoising, project the composed state to satisfy whole-body constraints (CoM within support polygon, angular momentum budget, joint torque limits). This is computationally cheap and directly addresses the coupling concern.
   (b) **Langevin MCMC correction steps** — following Reduce Reuse Recycle (Du et al., ICML 2023), add a few MCMC steps after each reverse-diffusion step to correct for the bias introduced by naive composition. This is the theoretically principled approach.
   (c) **Masked fine-tuning as the primary contribution, with inference-time composition as secondary.** Reframe: the masked fine-tuning teaches strong conditional distributions p(upper|lower,text) and p(lower|upper,text), which can be used for diverse data generation via iterative conditional generation (sample lower-body, then sample upper-body conditioned on it) rather than alternating denoising. This avoids the composition-during-denoising theoretical issues entirely and is closer to MaskedMimic's proven approach.

3. **Strengthen the argument against the Kimodo text-prompted baseline.** This is the baseline reviewers will focus on. The argument 'factorized generation enables combinatorial diversity' is intuitive but needs empirical grounding. Consider: (a) a toy experiment showing that Kimodo's compound-text samples cluster in a smaller region of joint-angle space than compositionally generated samples; (b) explicit measurement of state-space coverage (mean pairwise distance) as a primary metric; (c) honest acknowledgment that if the Kimodo training distribution already covers loco-manipulation compositions well, the compositional approach may offer diminishing returns.

4. **Frame novelty honestly.** The contribution is best described as: 'the first application of masked body-part diffusion fine-tuning (inspired by MaskedMimic) to a pre-trained robot motion diffusion model (Kimodo), with URDF-structured factorization and physics-enforced compositional sampling, evaluated on downstream RL policy quality.' This is a valid and publishable contribution at CoRL, but overselling it as 'no prior work combines kinematic-tree factored diffusion with compositional trajectory generation' is inaccurate given MixerMDM and MaskedMimic.

5. **Minor corrections:** OmniRetarget HuggingFace data is 4.0h (not 8+). Kimodo weights are NVIDIA Open Model License (not Apache 2.0).

### Round 4 review
Verdict: revise
Issues: ["CRITICAL — Kimodo's public repository (github.com/nv-tlabs/kimodo) provides ONLY inference code. There are no training scripts, no trainer module, no data loading pipeline, and no fine-tuning infrastructure. The directory structure (kimodo/model/, kimodo/scripts/, etc.) contains model definition and generation code only. The proposal's claim 'Fine-tuning uses Kimodo's existing training infrastructure' is factually incorrect. Implementing a complete training loop from scratch — noise scheduling, masked denoising loss, constraint conditioning curriculum, data loading for OmniRetarget + Kimodo's motion representation format, LLM annotation pipeline — is feasible (Apache-2.0 code + NVIDIA Open Model License weights permit it) but adds an estimated 5-8 days of engineering effort that is not accounted for in the 15-19 day timeline.", "HIGH — The 15-19 day manual timeline is unrealistic given the training code gap. Realistic breakdown with training implementation: Days 1-6: implement training infrastructure and masked training objective; Days 5-7: generate body-part text annotations via LLM; Days 7-10: fine-tuning runs (~12-20h); Days 10-13: trajectory generation + physics projection + ProtoMotions tracking; Days 13-17: SkillBench RL training (4 tasks × 5 baselines = 20 runs, ~5h each, parallelized on 4 GPUs to ~25h); Days 16-20: paper writing. This requires zero slack for debugging, hyperparameter tuning, or failed experiments, making the CoRL abstract deadline (Day 16) extremely risky for having results.", "HIGH — The Kimodo G1-RP-v1 checkpoint was trained on the proprietary Bones Rigplay dataset (~560h), which is unavailable. Fine-tuning this checkpoint with only OmniRetarget's 4.0h of supplemental loco-manipulation data creates a massive data distribution shift (4h supplemental vs. 560h base training). The proposal does not discuss: (a) whether fine-tuning with such a small supplement will actually shift the conditional distributions meaningfully, (b) whether using the G1-SEED-v1 checkpoint (trained on open BONES-SEED, 288h) would be more appropriate since BONES-SEED data is available for continued pre-training alongside OmniRetarget data, or (c) catastrophic forgetting risks when fine-tuning with masked objectives on a small dataset.", "MODERATE — The LLM-generated body-part text annotations are an untested pipeline component with no validation plan. The proposal says annotations are generated by 'prompting an LLM with per-body-part joint velocity statistics (e.g., high leg velocity + low arm velocity → walking for lower, arms at sides for upper).' This heuristic could produce noisy, uninformative, or incorrect annotations (e.g., a motion with both legs stationary but high torso rotation could be mislabeled). No annotation quality evaluation or human verification step is described.", "MODERATE — Physics auxiliary losses (CoM balance, joint torque limits) computed on the predicted clean sample x̂₀ during diffusion training may be ineffective at early denoising steps where x̂₀ predictions are highly noisy. PhysDiff (ICCV 2023) applied physics corrections as a post-processing step during sampling, not as training losses. The effectiveness of physics losses during diffusion fine-tuning (as opposed to post-generation projection, which the proposal also includes) is not established in the literature and may add implementation complexity without meaningful quality improvement.", "LOW — The risk note honestly acknowledges that 'masked fine-tuning may not significantly improve conditional quality over Kimodo zero-shot constraint conditioning,' but frames a null result as publishable. At CoRL, a negative result paper would need substantially more analysis (why doesn't it help? what does this tell us about pre-trained model representations?) than what the current experimental design supports."]
Feedback: The idea has improved substantially across rounds and addresses a genuine gap. The iterative conditional generation approach is theoretically well-motivated, the baselines are comprehensive, and the differentiation from prior work is clear. The remaining blockers are primarily execution feasibility, not conceptual soundness. Here is how to address each:

1. **Acknowledge and plan for the training code gap.** This is the single most important fix. Kimodo has no training code — you must implement it. Three options:
   (a) **Fastest**: Write a minimal fine-tuning script that loads Kimodo's model weights, implements a standard DDPM training loop with your masked denoising objective, and uses PyTorch's native optimizer. The model architecture is a standard transformer; the noise schedule and loss are standard DDPM. Budget 3-5 days for this. This is the recommended path.
   (b) **Contact NVIDIA**: The Kimodo team (NVIDIA SIL) may share training scripts under collaboration. This could save 3-5 days but adds dependency risk.
   (c) **Simplify to zero-shot only**: If time is critically short, drop the fine-tuning contribution entirely and evaluate only Kimodo's zero-shot constraint conditioning for iterative conditional generation. The URDF factorization + iterative conditional generation + physics projection + downstream RL evaluation would still be a contribution, though weaker.

2. **Choose the G1-SEED-v1 checkpoint.** Since BONES-SEED data is publicly available and you can combine it with OmniRetarget for fine-tuning, this avoids the distribution shift problem of fine-tuning the RP checkpoint on 4h of data against 560h of unseen base training data. The SEED model is less capable but the fine-tuning dynamics are more predictable.

3. **Add annotation quality validation.** Before committing to the full pipeline, manually verify a random sample of 50 LLM-generated body-part text annotations against ground-truth motion videos. Report inter-annotator agreement or at least spot-check accuracy. This takes <1 day and prevents a foundational pipeline flaw.

4. **Drop physics training losses; keep post-generation projection.** The physics auxiliary losses during fine-tuning are theoretically shaky and add implementation complexity. The post-composition physics projection (QP) is sufficient and well-grounded. Simplifying the fine-tuning to pure masked denoising loss saves implementation time.

5. **Timeline recovery strategy.** With training code implementation, the realistic timeline is 20-22 days, which misses the paper deadline by 1-3 days. Mitigation: (a) submit abstract by Day 16 with partial/expected results and complete experiments by Day 20; (b) reduce to 3 SkillBench tasks (FarReach-Easy, BoxPush-Medium, PackageCarry-Hard) to save RL compute time; (c) run Kimodo text-prompted baseline first (Day 1, no code needed) to establish the target to beat.

### Round 5 review
Verdict: revise
Issues: ["CRITICAL — Zero-shot pipeline relies on out-of-distribution constraint masking. Independent verification of Kimodo's technical report (arXiv 2603.15546) confirms that Phase 2 training uses ONLY pre-defined constraint patterns: full-body keyframes, random subsets of hands/feet positions/rotations, 2D root position/heading, and foot contact configurations. Body-part-level masking (e.g., 'fix all lower-body joints while generating upper-body') was NEVER in the training distribution. The proposal claims Kimodo's 'native constraint conditioning system' supports body-part masking, but this is out-of-distribution. While RePaint (CVPR 2022) showed diffusion models can generalize to arbitrary inpainting masks via step-by-step imputation, Kimodo's motion-specific constraint conditioning (with dual CFG for text vs. constraints) may not generalize as cleanly. The proposal must: (a) explicitly acknowledge this OOD risk, (b) frame the zero-shot approach as RePaint-style imputation and cite RePaint, (c) present the zero-shot quality as an empirical question rather than an assumed capability.", "HIGH — Missing critical related work: DreamControl-v2 (arXiv 2604.00202, March 31 2026) trains a guided diffusion model directly in humanoid robot motion space (G1-specific), generates reference trajectories from text + spatio-temporal controls, and trains downstream RL policies — the exact same pipeline paradigm as KinoTreeDiffuse. DreamControl-v2 does not do compositional body-part generation, which is KinoTreeDiffuse's differentiator, but it must be cited and used as a baseline or at minimum discussed. It validates the core pipeline (diffusion → trajectories → RL) while highlighting that the compositional body-part factorization is the specific novel contribution.", "HIGH — OmniRetarget data size persists at '8+ hours' despite previous rounds flagging this. Independent verification on HuggingFace (huggingface.co/datasets/omniretarget/OmniRetarget_Dataset) confirms 4.0 hours total (3.0h robot-object + 0.5h robot-terrain + 0.5h robot-object-terrain). The arXiv paper may claim 8+ hours, but only 4.0h are publicly available. This discrepancy appears in the opportunity section, approach section, and key_references — all must be corrected to '4.0h publicly available.'", "MODERATE — The argument for compositional generation over Kimodo's text-prompted baseline is insufficiently developed. Kimodo uses LLM2Vec for text encoding, which provides strong compositional text understanding for compound prompts like 'walk toward the shelf while raising your right hand.' The proposal's claim that factorized generation enables 'combinatorial diversity' (N_loco × N_manip >> N_compound) is intuitive but may not hold empirically if Kimodo's text-prompted generations already cover the relevant distribution. The proposal should explicitly hypothesize WHERE compositional generation would outperform text prompting (e.g., rare combinations not in training data, out-of-distribution text compositions) and design targeted experiments for those cases.", "MODERATE — LoRA training loop complexity is understated at '~200 lines.' A proper implementation from Kimodo's inference-only codebase requires: data loading for BONES-SEED's specific format (motion representation, temporal annotations), motion preprocessing matching Kimodo's representation (6D rotations, smoothed root), masked denoising objective with body-part masks, LoRA injection into Kimodo's two-stage transformer architecture, optimizer setup matching documented hyperparameters (Adam-atan2, per-component loss weights), EMA tracking, and evaluation/checkpointing. Realistic estimate: 500-800 lines of non-trivial code. Budget 4-6 days, not 2-3.", "LOW — BeyondMimic (arXiv 2508.08241, UC Berkeley) uses a unified latent diffusion model for humanoid control including motion inpainting and skill composition. While it targets real-time control rather than trajectory dataset generation, its diffusion-based inpainting/composition approach is conceptually related and should be cited for completeness."]
Feedback: The proposal has improved enormously across 5 rounds and is approaching publishable quality. The remaining issues are fixable. Here is how to address each:

1. **Acknowledge the OOD constraint masking risk explicitly.** This is the single most important fix. Reframe the zero-shot pipeline honestly: 'Kimodo was trained with end-effector and keyframe constraint patterns, not body-part-level masks. We hypothesize that its imputation-based conditioning (x̃_t = m ⊙ x_gt + (1-m) ⊙ x_t) generalizes to body-part masks following the same principle as RePaint (CVPR 2022), where arbitrary inpainting masks work with pre-trained DDPMs. We test this empirically.' This transforms a hidden weakness into an explicit research question — which is actually more interesting for reviewers.

2. **Cite DreamControl-v2 and position against it.** DreamControl-v2 validates the diffusion→trajectories→RL pipeline for G1 but uses monolithic text-conditioned generation without body-part factorization. Frame KinoTreeDiffuse as advancing this paradigm with compositional generation: 'DreamControl-v2 demonstrates the effectiveness of diffusion-generated reference trajectories for humanoid RL; we extend this paradigm with compositional body-part generation that enables combinatorial diversity beyond what monolithic text prompting achieves.'

3. **Correct OmniRetarget to 4.0h everywhere.** This is a simple fix but its persistence across 3 review rounds suggests carelessness.

4. **Strengthen the case against the text-prompted baseline.** Add a preliminary analysis (Day 1-2): generate 50 compound text-prompted motions from Kimodo (e.g., 'walk while reaching,' 'jog while waving') and measure their diversity in joint-angle space. Compare against 50 compositionally generated motions (5 locomotions × 10 manipulations). If compositional diversity is measurably higher, lead with this result.

5. **Budget 4-6 days for LoRA training implementation, not 2-3.** Update timeline accordingly. The early checkpoint strategy (Day 7-8) becomes more important with this revised estimate.

6. **Consider adding a 'Kimodo + RePaint resampling' baseline.** If you're going to frame the zero-shot approach as RePaint-style imputation, adding RePaint's resampling trick (noise-denoise cycles at the mask boundary) could improve zero-shot quality significantly and costs nothing in implementation complexity.

### Round 6 review
Verdict: revise
Issues: ["HIGH — Dual CFG interaction with OOD body-part masks is an unaddressed failure mode. Recent work (CFG++, ICLR 2025; Rethinking Spatial Inconsistency in CFG, CVPR 2024; What Guidance Does in Masked Discrete Diffusion, 2025) documents that when dual guidance signals conflict — here, text guidance pulling toward in-distribution regions while constraint guidance (w_constr=2) pushes toward OOD body-part patterns — the result is off-manifold amplification with double-exponential dependency on guidance weight. The proposal uses Kimodo's default w_constr=2, but with OOD constraint patterns this may produce severe artifacts. Mitigation options not discussed: (a) set w_constr=0 for OOD masks (pure imputation without guidance), (b) use adaptive/annealed constraint guidance, (c) apply CFG++ manifold-constrained sampling.", "MODERATE — The novelty argument rests primarily on 'testing an empirical hypothesis on a specific model.' While honest, this positions the paper as an empirical study rather than a method paper. CoRL reviewers may question whether 'we applied RePaint-style inpainting to Kimodo and added LoRA' constitutes sufficient methodological contribution. Strengthening: the URDF-factored iterative conditional generation (sequential complete processes rather than score composition) should be emphasized as the methodological choice, with theoretical justification from the compositional diffusion failure literature (mode-averaging, factorization violations).", "MODERATE — The preliminary diversity analysis (Day 1-2) is the linchpin of the entire motivation. If compositional generation does NOT produce measurably higher diversity than Kimodo's compound text prompts (which use LLM2Vec for compositional text understanding), the paper's raison d'être evaporates. The proposal correctly identifies this but doesn't specify: (a) what diversity threshold would constitute a 'positive' result, (b) what statistical test would be used, (c) how many samples are needed for statistical significance. Without pre-registered success criteria, there's a risk of post-hoc rationalization.", "LOW — Missing recent paper: 'Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking' (arXiv 2604.17335, April 2026) uses diffusion-based G1 motion generation with RL tracking — validates the generation→tracking paradigm but targets terrain-aware locomotion rather than compositional loco-manipulation. Should be briefly cited for completeness as concurrent validation of diffusion→ProtoMotions→RL pipeline.", "LOW — The paper title 'KinoTreeDiffuse: Compositional Humanoid Trajectory Amplification via URDF-Factored Iterative Conditional Diffusion' is 13 subtitle words. CoRL papers benefit from concise, memorable titles. Consider: 'Can Humanoid Motion Diffusion Models Compose? Testing Body-Part Inpainting for Diverse Trajectory Generation' — which foregrounds the empirical question."]
Feedback: The proposal is close to passable after 5 rounds of revision — the clarity is excellent, related work is comprehensive, baselines are strong, and the early checkpoint strategy is well-designed. Three changes would push it over the threshold:

1. **Address the dual-CFG failure mode explicitly.** This is the single most important remaining gap. Kimodo's constraint conditioning uses dual CFG (w_text, w_constr), and literature shows dual guidance amplifies off-manifold artifacts when one signal is OOD. Add a specific experimental variable: test w_constr ∈ {0, 0.5, 1.0, 2.0} for body-part masks in the Day 1-2 preliminary analysis. Setting w_constr=0 reduces to pure imputation (RePaint-style, no guidance), which may actually work BETTER than guided generation for OOD patterns. This costs nothing extra and strengthens the empirical contribution. Frame it as: 'We disentangle the contributions of imputation (mask replacement at each step) versus guidance (CFG amplification of constraint adherence) for OOD body-part patterns.'

2. **Pre-register diversity success criteria.** State explicitly: 'We consider compositional generation justified if mean pairwise joint-angle distance of N_comp=50 compositional samples exceeds that of N_text=50 compound-text samples by >15% (or 1 standard deviation), measured via permutation test at p<0.05.' This transforms the preliminary analysis from a subjective judgment to a rigorous hypothesis test and protects against post-hoc rationalization.

3. **Strengthen the methodological contribution framing.** The choice of iterative conditional generation (sequential complete diffusion processes) over score composition (simultaneous/alternating denoising within one process) is itself a methodological contribution supported by the compositional diffusion failure literature. Emphasize: 'Unlike score-composition approaches (MixerMDM, EnergyMoGen, CompDiffuser) which suffer from mode-averaging and factorization violations within the denoising loop, iterative conditional generation runs each body-part as a complete, independent diffusion process conditioned on the other's output — avoiding the documented failure modes while enabling compositional diversity.' This elevates the paper from 'we tried inpainting on Kimodo' to 'we propose iterative conditional generation as a principled alternative to score composition for structured body-part composition, supported by theory and validated empirically.'

Minor: cite arXiv 2604.17335 for pipeline validation, and consider a shorter title.


## Output format
Output ONLY a JSON object:
{
  "verdict": "pass | revise | fail",
  "scores": {
    "novelty": {"score": 0-5, "rationale": "1-2 sentence justification"},
    "feasibility": {"score": 0-5, "rationale": "1-2 sentence justification"},
    "clarity": {"score": 0-5, "rationale": "1-2 sentence justification"},
    "impact": {"score": 0-5, "rationale": "1-2 sentence justification"}
  },
  "issues": ["specific issue 1", "specific issue 2", ...],
  "feedback": "Actionable feedback for the generator (if verdict=revise)",
  "reason": "One-line summary of verdict rationale"
}

Rules:
- "pass": idea is sound AND high quality — avg score >= 4.0, no critical issues
- "revise": fixable issues OR scores below threshold — provide specific feedback
- "fail": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)
- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.
- Round 10 only: if still "revise", you MUST choose "pass" or "fail".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "type": "user",
  "uuid": "590d15f0-fc08-4055-b781-98b3fc79f62f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T20:21:53.996Z_

```json
{
  "parentUuid": "590d15f0-fc08-4055-b781-98b3fc79f62f",
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
  "uuid": "2b42c87f-895e-451f-a4d4-c0a74e4c0b17",
  "timestamp": "2026-05-10T20:21:53.996Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T20:21:53.996Z_

```json
{
  "parentUuid": "2b42c87f-895e-451f-a4d4-c0a74e4c0b17",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "56ee8af6-4743-41a5-b469-eaf270ef650b",
  "timestamp": "2026-05-10T20:21:53.996Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "56ee8af6-4743-41a5-b469-eaf270ef650b",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Humanoid body-part compositional diffusion with out-of-distribution constraint testing",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257"
}
```

---

### Assistant

_source line 8 · 2026-05-10T20:22:16.739Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed ML research proposal review for Round 7 of 10. I need to independently verify the claims made in this proposal through web searches, then issue a verdict. Let me carefully analyze the proposal and conduct thorough research.

The proposal is about compositional humanoid trajectory generation using body-part inpainting on Kimodo's pre-trained diffusion model, with iterative conditional generation as the key methodological contribution.

Let me identify the key claims to verify:

1. **Kimodo's existence and capabilities** - arXiv 2603.15546, inference-only code, G1-SEED-v1 checkpoint


2. **DreamControl-v2** - arXiv 2604.00202, validates diffusion→trajectories→RL pipeline
3. **MixerMDM** - CVPR 2025, arXiv 2504.01019
4. **MaskedMimic** - SIGGRAPH Asia 2024
5. **RePaint** - CVPR 2022, mask-agnostic inpainting
6. **CFG++ and S-CFG** - guidance failure modes
7. **Bradley et al. ICML 2025** - compositional diffusion theory
8. **CondMDM** - conditional motion diffusion model

Now I'm compiling the references to verify... I need to dig into a few key uncertainties: whether iterative conditional generation has already been explored in the literature, if the out-of-distribution masking concern actually holds up, and whether the proposed timeline and computational resources are realistic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "56ee8af6-4743-41a5-b469-eaf270ef650b",
  "isSidechain": false,
  "requestId": "req_011CauWaZyeWRUA8tRdFNjwK",
  "type": "assistant",
  "uuid": "7396ef49-c266-44f4-9dc0-d28bd31e1e2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGHRTqGCB3E7B9QBEk3tkm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30620,
      "cache_read_input_tokens": 11664,
      "output_tokens": 1054,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1054,
          "cache_read_input_tokens": 11664,
          "cache_creation_input_tokens": 30620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30620
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

_source line 9 · 2026-05-10T20:22:17.032Z_

I'll conduct an independent verification of this proposal's claims, searching for competing work, validating references, and checking feasibility. Let me launch parallel searches across multiple dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7396ef49-c266-44f4-9dc0-d28bd31e1e2d",
  "isSidechain": false,
  "requestId": "req_011CauWaZyeWRUA8tRdFNjwK",
  "type": "assistant",
  "uuid": "02ddc33a-f858-412f-ba3c-d7a62fcd7c26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGHRTqGCB3E7B9QBEk3tkm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30620,
      "cache_read_input_tokens": 11664,
      "output_tokens": 1054,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1054,
          "cache_read_input_tokens": 11664,
          "cache_creation_input_tokens": 30620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30620
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

_source line 10 · 2026-05-10T20:22:26.948Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01EHFFZ2Tk7EvgbM58F5U7em`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Kimodo and DreamControl-v2",
  "prompt": "You are helping me verify claims in an ML research proposal. Search for and verify the following:\n\n1. **Kimodo** (NVIDIA, arXiv 2603.15546, March 2026): Verify it exists, check whether the public repo (github.com/nv-tlabs/kimodo) provides ONLY inference code (no training scripts), verify the G1-SEED-v1 checkpoint details (282M params, 288h BONES-SEED data), and confirm the dual CFG formula (x̂₀ = D∅ + w_text(D_text - D∅) + w_constr(D_constr - D∅)). Also check what constraint patterns were used in Phase 2 training.\n\n2. **DreamControl-v2** (arXiv 2604.00202, March 2026): Verify it exists, check if it achieves 91-100% success across 8 tasks on G1, confirm it uses monolithic text conditioning without body-part composition.\n\n3. **BONES-SEED dataset**: Verify it exists on HuggingFace, check if it really has 142K motions and 288h of data, and whether it includes NL descriptions and temporal segmentation.\n\n4. **OmniRetarget dataset**: Verify the data size — the proposal claims 4.0h (3.0h robot-object + 0.5h robot-terrain + 0.5h robot-object-terrain). Check HuggingFace.\n\nUse WebSearch and WebFetch to verify. Report what you find with specific details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02ddc33a-f858-412f-ba3c-d7a62fcd7c26",
  "isSidechain": false,
  "requestId": "req_011CauWaZyeWRUA8tRdFNjwK",
  "type": "assistant",
  "uuid": "161df6b4-a1f8-42e6-b266-f1a11c7e1abc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KGHRTqGCB3E7B9QBEk3tkm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30620,
      "cache_read_input_tokens": 11664,
      "output_tokens": 1054,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30620,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1054,
          "cache_read_input_tokens": 11664,
          "cache_creation_input_tokens": 30620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30620
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

_source line 11 · 2026-05-10T20:24:33.923Z_

<details><summary>↩ Tool result · `toolu_01EHFFZ2Tk7EvgbM58F5U7em`</summary>

```text
I now have all the information needed. Here is the complete verification report.

---

## Verification Report

### 1. Kimodo (NVIDIA, arXiv 2603.15546)

**Existence:** CONFIRMED. The paper "Kimodo: Scaling Controllable Human Motion Generation" exists at [arXiv 2603.15546](https://arxiv.org/abs/2603.15546), published March 16, 2026.

**Public repo (github.com/nv-tlabs/kimodo):** CONFIRMED. The repo exists and provides **inference code only** -- no training scripts. It explicitly lists: "Inference: code and CLI to generate motions on both human and robot skeletons," along with an interactive demo, benchmark evaluation tools, and a low-level Python API. No training code or training documentation is included.

**G1-SEED-v1 checkpoint details:**
- **282M parameters:** CONFIRMED. The [HuggingFace model card](https://huggingface.co/nvidia/Kimodo-G1-SEED-v1) explicitly states 282M parameters.
- **288h BONES-SEED data:** CONFIRMED. The model card states "288 hours of human motion capture" from the "Public Bones-SEED Dataset."
- **Skeleton:** 34-joint Unitree G1 robot skeleton.

**Dual CFG formula:** CONFIRMED. The paper contains exactly the formula claimed:
> x-hat_0 = D_empty + w_text(D_text - D_empty) + w_constr(D_constr - D_empty)

where D_empty is the baseline denoiser with no conditioning, D_text uses only text guidance, and D_constr uses only constraint conditioning. Default weights are w_text = 2 and w_constr = 2.

**Phase 2 constraint patterns:** CONFIRMED. Phase 2 training (500k steps) used these constraint patterns:
- Full-body joint positions at sparse keyframes
- Hand/foot position and rotation subsets at sparse keyframes
- 2D root position/heading at sparse keyframes
- Dense 2D root position/heading paths
- Foot contact configurations at sparse keyframes
- Two constraint patterns mixed together 25% of the time; 10% of the time no constraints used.

---

### 2. DreamControl-v2 (arXiv 2604.00202)

**Existence:** CONFIRMED. The paper "DreamControl-v2: Simpler and Scalable Autonomous Humanoid Skills via Trainable Guided Diffusion Priors" exists at [arXiv 2604.00202](https://arxiv.org/abs/2604.00202), published March 31, 2026.

**91-100% success across 8 tasks on G1:** CONFIRMED. Per Table III in the paper, the success rates across all 8 tasks are:
| Task | Success Rate |
|------|-------------|
| Pick | 99% |
| Punch | 99% |
| Deep Squat & Pick | 94% |
| Drawer Open | 96% |
| Pour | 92% |
| Vertical Wipe | 100% |
| Deep Squat | 99% |
| Step & Punch | 91% |

All 8 tasks fall within the 91-100% range. The claim is accurate.

**Monolithic text conditioning (no body-part composition):** CONFIRMED. The system uses monolithic text conditioning -- text prompts are task-level instructions (e.g., "a person picks an object with their right hand") applied uniformly to the whole body, not decomposed into body-part components. Spatial guidance operates through joint-level constraints in robot space, but the text conditioning itself remains holistic.

---

### 3. BONES-SEED Dataset

**Existence on HuggingFace:** CONFIRMED. Available at [bones-studio/seed](https://huggingface.co/datasets/bones-studio/seed).

**142K motions:** CONFIRMED. Exactly 142,220 motions (71,132 original + 71,088 mirrored).

**288h of data:** CONFIRMED. Approximately 288 hours at 120 fps.

**NL descriptions:** CONFIRMED. Up to 6 natural language descriptions per motion (4 natural fluent, 1 technical/biomechanical, 2 short).

**Temporal segmentation:** CONFIRMED. Temporal segmentation labels with precise timestamps and phase descriptions are included, stored in `metadata/seed_metadata_v002_temporal_labels.jsonl`.

Additional notable details: 522 performers (253F/269M), ages 17-71, 8 top-level motion categories, 114 GB total size, available in SOMA and Unitree G1 MuJoCo-compatible formats.

---

### 4. OmniRetarget Dataset

**Existence on HuggingFace:** CONFIRMED. Available at [omniretarget/OmniRetarget_Dataset](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset).

**Data size breakdown:** CONFIRMED exactly as claimed:
| Subset | Duration |
|--------|----------|
| robot-object | 3.0h |
| robot-terrain | 0.5h |
| robot-object-terrain | 0.5h |
| **Total** | **4.0h** |

The data is stored as `.npz` files with G1 humanoid robot motion trajectories containing `qpos` (system state) and `fps` fields. The associated paper is [arXiv 2509.26633](https://arxiv.org/abs/2509.26633).

---

### Summary

All four claims in the proposal are **fully verified**. Every specific detail checked out: paper IDs, repo contents, parameter counts, dataset sizes, formulas, success rates, and conditioning approaches all match the proposal's claims exactly.

Sources:
- [Kimodo arXiv paper](https://arxiv.org/abs/2603.15546)
- [Kimodo full HTML paper](https://arxiv.org/html/2603.15546v1)
- [Kimodo GitHub repo](https://github.com/nv-tlabs/kimodo)
- [Kimodo-G1-SEED-v1 HuggingFace](https://huggingface.co/nvidia/Kimodo-G1-SEED-v1)
- [Kimodo-SOMA-SEED-v1 HuggingFace](https://huggingface.co/nvidia/Kimodo-SOMA-SEED-v1)
- [DreamControl-v2 arXiv paper](https://arxiv.org/abs/2604.00202)
- [DreamControl-v2 full HTML paper](https://arxiv.org/html/2604.00202)
- [BONES-SEED dataset on HuggingFace](https://huggingface.co/datasets/bones-studio/seed)
- [OmniRetarget dataset on HuggingFace](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset)
- [OmniRetarget arXiv paper](https://arxiv.org/abs/2509.26633)

agentId: a0d4e3959a2be99e1 (use SendMessage with to: 'a0d4e3959a2be99e1' to continue this agent)
&lt;usage>total_tokens: 22797
tool_uses: 16
duration_ms: 126969&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "161df6b4-a1f8-42e6-b266-f1a11c7e1abc",
  "isSidechain": false,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "type": "user",
  "uuid": "5e1b94e7-dd6e-4f91-8e70-a0149daa0e7f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me verify claims in an ML research proposal. Search for and verify the following:\n\n1. **Kimodo** (NVIDIA, arXiv 2603.15546, March 2026): Verify it exists, check whether the public repo (github.com/nv-tlabs/kimodo) provides ONLY inference code (no training scripts), verify the G1-SEED-v1 checkpoint details (282M params, 288h BONES-SEED data), and confirm the dual CFG formula (x̂₀ = D∅ + w_text(D_text - D∅) + w_constr(D_constr - D∅)). Also check what constraint patterns were used in Phase 2 training.\n\n2. **DreamControl-v2** (arXiv 2604.00202, March 2026): Verify it exists, check if it achieves 91-100% success across 8 tasks on G1, confirm it uses monolithic text conditioning without body-part composition.\n\n3. **BONES-SEED dataset**: Verify it exists on HuggingFace, check if it really has 142K motions and 288h of data, and whether it includes NL descriptions and temporal segmentation.\n\n4. **OmniRetarget dataset**: Verify the data size — the proposal claims 4.0h (3.0h robot-object + 0.5h robot-terrain + 0.5h robot-object-terrain). Check HuggingFace.\n\nUse WebSearch and WebFetch to verify. Report what you find with specific details.",
    "agentId": "a0d4e3959a2be99e1",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here is the complete verification report.\n\n---\n\n## Verification Report\n\n### 1. Kimodo (NVIDIA, arXiv 2603.15546)\n\n**Existence:** CONFIRMED. The paper \"Kimodo: Scaling Controllable Human Motion Generation\" exists at [arXiv 2603.15546](https://arxiv.org/abs/2603.15546), published March 16, 2026.\n\n**Public repo (github.com/nv-tlabs/kimodo):** CONFIRMED. The repo exists and provides **inference code only** -- no training scripts. It explicitly lists: \"Inference: code and CLI to generate motions on both human and robot skeletons,\" along with an interactive demo, benchmark evaluation tools, and a low-level Python API. No training code or training documentation is included.\n\n**G1-SEED-v1 checkpoint details:**\n- **282M parameters:** CONFIRMED. The [HuggingFace model card](https://huggingface.co/nvidia/Kimodo-G1-SEED-v1) explicitly states 282M parameters.\n- **288h BONES-SEED data:** CONFIRMED. The model card states \"288 hours of human motion capture\" from the \"Public Bones-SEED Dataset.\"\n- **Skeleton:** 34-joint Unitree G1 robot skeleton.\n\n**Dual CFG formula:** CONFIRMED. The paper contains exactly the formula claimed:\n> x-hat_0 = D_empty + w_text(D_text - D_empty) + w_constr(D_constr - D_empty)\n\nwhere D_empty is the baseline denoiser with no conditioning, D_text uses only text guidance, and D_constr uses only constraint conditioning. Default weights are w_text = 2 and w_constr = 2.\n\n**Phase 2 constraint patterns:** CONFIRMED. Phase 2 training (500k steps) used these constraint patterns:\n- Full-body joint positions at sparse keyframes\n- Hand/foot position and rotation subsets at sparse keyframes\n- 2D root position/heading at sparse keyframes\n- Dense 2D root position/heading paths\n- Foot contact configurations at sparse keyframes\n- Two constraint patterns mixed together 25% of the time; 10% of the time no constraints used.\n\n---\n\n### 2. DreamControl-v2 (arXiv 2604.00202)\n\n**Existence:** CONFIRMED. The paper \"DreamControl-v2: Simpler and Scalable Autonomous Humanoid Skills via Trainable Guided Diffusion Priors\" exists at [arXiv 2604.00202](https://arxiv.org/abs/2604.00202), published March 31, 2026.\n\n**91-100% success across 8 tasks on G1:** CONFIRMED. Per Table III in the paper, the success rates across all 8 tasks are:\n| Task | Success Rate |\n|------|-------------|\n| Pick | 99% |\n| Punch | 99% |\n| Deep Squat & Pick | 94% |\n| Drawer Open | 96% |\n| Pour | 92% |\n| Vertical Wipe | 100% |\n| Deep Squat | 99% |\n| Step & Punch | 91% |\n\nAll 8 tasks fall within the 91-100% range. The claim is accurate.\n\n**Monolithic text conditioning (no body-part composition):** CONFIRMED. The system uses monolithic text conditioning -- text prompts are task-level instructions (e.g., \"a person picks an object with their right hand\") applied uniformly to the whole body, not decomposed into body-part components. Spatial guidance operates through joint-level constraints in robot space, but the text conditioning itself remains holistic.\n\n---\n\n### 3. BONES-SEED Dataset\n\n**Existence on HuggingFace:** CONFIRMED. Available at [bones-studio/seed](https://huggingface.co/datasets/bones-studio/seed).\n\n**142K motions:** CONFIRMED. Exactly 142,220 motions (71,132 original + 71,088 mirrored).\n\n**288h of data:** CONFIRMED. Approximately 288 hours at 120 fps.\n\n**NL descriptions:** CONFIRMED. Up to 6 natural language descriptions per motion (4 natural fluent, 1 technical/biomechanical, 2 short).\n\n**Temporal segmentation:** CONFIRMED. Temporal segmentation labels with precise timestamps and phase descriptions are included, stored in `metadata/seed_metadata_v002_temporal_labels.jsonl`.\n\nAdditional notable details: 522 performers (253F/269M), ages 17-71, 8 top-level motion categories, 114 GB total size, available in SOMA and Unitree G1 MuJoCo-compatible formats.\n\n---\n\n### 4. OmniRetarget Dataset\n\n**Existence on HuggingFace:** CONFIRMED. Available at [omniretarget/OmniRetarget_Dataset](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset).\n\n**Data size breakdown:** CONFIRMED exactly as claimed:\n| Subset | Duration |\n|--------|----------|\n| robot-object | 3.0h |\n| robot-terrain | 0.5h |\n| robot-object-terrain | 0.5h |\n| **Total** | **4.0h** |\n\nThe data is stored as `.npz` files with G1 humanoid robot motion trajectories containing `qpos` (system state) and `fps` fields. The associated paper is [arXiv 2509.26633](https://arxiv.org/abs/2509.26633).\n\n---\n\n### Summary\n\nAll four claims in the proposal are **fully verified**. Every specific detail checked out: paper IDs, repo contents, parameter counts, dataset sizes, formulas, success rates, and conditioning approaches all match the proposal's claims exactly.\n\nSources:\n- [Kimodo arXiv paper](https://arxiv.org/abs/2603.15546)\n- [Kimodo full HTML paper](https://arxiv.org/html/2603.15546v1)\n- [Kimodo GitHub repo](https://github.com/nv-tlabs/kimodo)\n- [Kimodo-G1-SEED-v1 HuggingFace](https://huggingface.co/nvidia/Kimodo-G1-SEED-v1)\n- [Kimodo-SOMA-SEED-v1 HuggingFace](https://huggingface.co/nvidia/Kimodo-SOMA-SEED-v1)\n- [DreamControl-v2 arXiv paper](https://arxiv.org/abs/2604.00202)\n- [DreamControl-v2 full HTML paper](https://arxiv.org/html/2604.00202)\n- [BONES-SEED dataset on HuggingFace](https://huggingface.co/datasets/bones-studio/seed)\n- [OmniRetarget dataset on HuggingFace](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset)\n- [OmniRetarget arXiv paper](https://arxiv.org/abs/2509.26633)"
      }
    ],
    "totalDurationMs": 126969,
    "totalTokens": 22797,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 20325,
      "output_tokens": 1751,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1751,
          "cache_read_input_tokens": 20325,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 720,
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
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "161df6b4-a1f8-42e6-b266-f1a11c7e1abc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T20:24:47.098Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012G9wTB5y6HXzb6nFwfCu89`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search competing compositional work",
  "prompt": "You are helping me verify an ML research proposal about compositional humanoid trajectory generation using body-part inpainting on diffusion models. I need to find ANY competing or closely related work the proposal may have missed. Search thoroughly for:\n\n1. **Compositional body-part motion generation 2025-2026**: Search for recent papers that decompose motion generation by body parts using diffusion models. Try multiple queries:\n   - \"body part compositional motion diffusion 2026\"\n   - \"spatial composition motion generation diffusion\"\n   - \"body part inpainting motion diffusion\"\n   - \"humanoid compositional trajectory generation\"\n\n2. **Iterative conditional generation in diffusion**: Search for papers that use sequential conditional diffusion processes (generate one part, then condition the next generation on it), as opposed to score composition. Try:\n   - \"iterative conditional diffusion generation\"\n   - \"sequential conditional diffusion composition\"\n   - \"autoregressive diffusion spatial composition\"\n\n3. **Robot motion diffusion with inpainting/masking 2025-2026**: Search for papers that apply inpainting or masking to robot-specific (not human) motion diffusion models:\n   - \"robot motion diffusion inpainting\"\n   - \"masked robot trajectory diffusion\"\n   - \"constraint conditioning diffusion robot\"\n\n4. **Kimodo extensions or follow-up work**: Search for any papers building on Kimodo (NVIDIA, March 2026):\n   - \"Kimodo motion generation\"\n   - \"BONES-SEED diffusion\"\n   - \"G1 humanoid diffusion\"\n\n5. **Any concurrent work on humanoid data generation via diffusion**: \n   - \"humanoid data generation diffusion 2026\"\n   - \"synthetic humanoid training data diffusion\"\n\nUse WebSearch for each query. Report ALL papers found with titles, venues, dates, and brief descriptions. I need to know if there's anything the proposal missed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e1b94e7-dd6e-4f91-8e70-a0149daa0e7f",
  "isSidechain": false,
  "requestId": "req_011CauWnMinSKj5BN88iBguM",
  "type": "assistant",
  "uuid": "4543c899-3e79-4843-bc6f-a0d4629090ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LxipUUVPfW62kRcozeASRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2888,
      "cache_read_input_tokens": 42284,
      "output_tokens": 530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 530,
          "cache_read_input_tokens": 42284,
          "cache_creation_input_tokens": 2888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2888
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

_source line 13 · 2026-05-10T20:28:53.097Z_

<details><summary>↩ Tool result · `toolu_012G9wTB5y6HXzb6nFwfCu89`</summary>

```text
I now have comprehensive results. Here is my full report of all relevant and competing work found:

---

## Comprehensive Literature Search Results

### Category 1: Compositional Body-Part Motion Generation (2024-2026)

**FrankenMotion: Part-level Human Motion Generation and Composition** (arXiv, January 2026)
- A transformer-based diffusion model that accepts sequence-level, action-level, AND part-level text prompts. It constructs a dataset with atomic, temporally-aware part-level annotations using LLMs. This is the MOST DIRECTLY competing work -- it explicitly decomposes motion by body parts and generates part-conditioned motion using diffusion. First to provide atomic, temporally-aware part-level motion annotations.
- [Paper](https://arxiv.org/abs/2601.10909) | [Project](https://coral79.github.io/frankenmotion/)

**EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space** (CVPR 2025)
- Uses energy-based composition of multiple diffusion models in latent space for compositional motion. Introduces "Synergistic Energy Fusion" to combine multiple energy terms corresponding to text descriptions. Achieves concept conjunction, negation, and multi-concept composition.
- [Paper](https://arxiv.org/abs/2412.14706) | [Project](https://jiro-zhang.github.io/EnergyMoGen/)

**DeMoGen: Towards Decompositional Human Motion Generation with Energy-Based Diffusion Models** (arXiv, December 2025)
- Inverse of composition: decomposes holistic motion into semantically meaningful sub-components using an energy-based diffusion model. Three training variants (explicit decomposition, orthogonal self-supervised, semantic consistency). Enables disentangling reusable motion primitives from complex sequences.
- [Paper](https://arxiv.org/abs/2512.22324) | [Project](https://jiro-zhang.github.io/DeMoGen/)

**SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation** (ICCV 2023)
- Uses GPT-3 to map actions to body parts, then combines body parts from two motions. Creates synthetic compositional training data. Earlier foundational work on spatial composition of body parts.
- [Paper](https://arxiv.org/abs/2304.10417)

**Motion Composition Diffusion (MCD): Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models** (arXiv, September 2024)
- Decomposes complex actions into sub-movements via GPT, processes each individually during denoising, then combines. Handles both temporal and spatial composition. Agnostic to spatial overlap, no need for body-part specification.
- [Paper](https://arxiv.org/abs/2409.11920)

**STMC: Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation** (CVPR Workshop 2024)
- Multi-track timeline with overlapping text prompts. At each denoising step, processes each timeline interval individually, then aggregates predictions with consideration for specific body parts engaged. Test-time method compatible with any pre-trained motion diffusion model.
- [Paper](https://arxiv.org/abs/2401.08559) | [GitHub](https://github.com/nv-tlabs/stmc)

**BA-IDM: Body-Aware Diffusion for 3D Human Motion Generation** (MMAsia 2025)
- Divides body into five parts (head, left arm, right arm, spine, legs). Maps complex text instructions to specific body parts. Includes RL and conditional guidance for stable generation in complex scenes.
- [Paper](https://dl.acm.org/doi/10.1145/3743093.3770934)

**Motion-Adapter: A Diffusion Model Adapter for Text-to-Motion Generation of Compound Actions** (arXiv, April 2026)
- Plug-and-play adapter that computes decoupled cross-attention maps serving as structural masks during denoising. Trained on single-action motions only. Addresses catastrophic neglect and attention collapse. Very recent.
- [Paper](https://arxiv.org/html/2604.16135v1)

**FineMoGen: Fine-Grained Spatio-Temporal Motion Generation and Editing** (NeurIPS area)
- Builds a Spatio-Temporal Mixture Attention (SAMI) architecture for explicit spatial-temporal composition constraints.
- [Paper](https://arxiv.org/abs/2312.15004)

---

### Category 2: Iterative/Sequential Conditional Generation in Diffusion

**CompDiffuser: Generative Trajectory Stitching through Diffusion Composition** (arXiv, March 2025)
- Autoregressive sampling of multiple short-horizon diffusion models, stitching them into longer trajectories. Uses noise-conditioned score function formulation. Models overlapping chunks with conditional relationships via a single bidirectional diffusion model. Tested on 50D humanoid (HumanoidMaze).
- [Paper](https://arxiv.org/abs/2503.05153) | [Project](https://comp-diffuser.github.io/)

**DartControl (DART): A Diffusion-Based Autoregressive Motion Model for Real-Time Text-Driven Motion Control** (2024)
- Autoregressive latent diffusion for motion primitive generation, jointly conditioned on text prompts and motion history. Supports spatial constraints, waypoint goal reaching, and in-betweening.
- [Paper](https://zkf1997.github.io/DART/)

**MotionStreamer: Streaming Motion Generation via Diffusion-based Autoregressive Model in Causal Latent Space** (ICCV 2025)
- Continuous causal latent space with probabilistic autoregressive model. Supports multi-round generation, long-term generation, and dynamic motion composition.
- [Paper](https://arxiv.org/abs/2503.15451)

---

### Category 3: Inpainting/Masking in Motion Diffusion

**MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting** (NVIDIA, ACM TOG 2024)
- HIGHLY RELEVANT. Formulates physics-based character control as motion inpainting. Single unified model synthesizes motions from partial (masked) motion descriptions -- masked keyframes, objects, text, or combinations. Supports partial joint targets, joystick control, text commands, and multi-modal composition.
- [Paper](https://arxiv.org/abs/2409.14393) | [Project](https://research.nvidia.com/labs/par/maskedmimic/)

**CondMDI: Flexible Motion In-betweening with Diffusion Models** (SIGGRAPH 2024)
- Trains on randomly sampled keyframes with randomly sampled joints and a mask indicating observations. Supports partial keyframe constraints (subset of joints). Replaces noisy input with given keyframes and concatenates observation mask.
- [Paper](https://arxiv.org/abs/2405.11126)

**COIN: Control-Inpainting Diffusion Prior for Human and Camera Motion Estimation** (ECCV 2024)
- Soft inpainting strategy that identifies high-confidence regions and uses them as soft constraints while re-sampling low-confidence regions from scratch.
- [Paper](https://arxiv.org/html/2408.16426)

**MDM: Human Motion Diffusion Model** (ICLR 2023)
- Original work demonstrating inpainting in joint space for semantic editing of specific body parts.
- [Paper](https://guytevet.github.io/mdm-page/)

**Towards Natural Prosthetic Hand Gestures: A Common-Rig and Diffusion Inpainting Pipeline** (IEEE, 2024)
- Directly relevant: generates hand motion from body motion via diffusion-based inpainting on a common kinematic rig. Conditions hand generation on body-only motion. Validated on a real robotic system.
- [Paper](https://kaseungyup.github.io/natural-prosthetic-hand-gestures/)

---

### Category 4: Robot-Specific Motion Diffusion

**RobotMDM: Robot Motion Diffusion Model** (SIGGRAPH Asia 2024, Disney Research)
- Integrates kinematic generative motion models with physics-based character control. Generalizes across human, non-human, and synthetic morphologies. Tested on a bipedal robot (20 DoF).
- [Paper](https://dl.acm.org/doi/10.1145/3680528.3687626)

**DiffusionSeeder: Seeding Motion Optimization with Diffusion for Rapid Motion Planning** (CoRL 2025)
- Uses diffusion to generate trajectory seeds for motion optimization. 12x speed-up on average. Sim2real on Franka robot.
- [Paper](https://arxiv.org/abs/2410.16727)

**CoDiG: Constraint-Aware Diffusion Guidance for Robotics** (arXiv, May 2025)
- Integrates barrier functions into denoising to guide toward constraint-satisfying outputs. Real-world racing experiments.
- [Paper](https://arxiv.org/abs/2505.13131)

**Diffusion Predictive Control with Constraints** (arXiv, December 2024)
- Model-based projections in trajectory denoising for constraint-satisfying, dynamically feasible trajectories.
- [Paper](https://arxiv.org/html/2412.09342)

---

### Category 5: Kimodo Ecosystem and Extensions

**Kimodo: Scaling Controllable Human Motion Generation** (NVIDIA, March 16, 2026)
- Kinematic motion diffusion model trained on 700 hours of mocap (BONES-RigPlay). Five model variants (SOMA, G1, SMPL-X). Supports text + full-body keyframes, sparse joint positions/rotations, 2D waypoints, dense 2D paths. Two-stage denoiser separating root and body prediction. Open-source code, closed data.
- Updates: v1.1 models + benchmark (April 10, 2026); multi-prompt improvements (April 24, 2026).
- Integrated into GEAR-SONIC interactive demo.
- [Project](https://research.nvidia.com/labs/sil/projects/kimodo/) | [GitHub](https://github.com/nv-tlabs/kimodo)

**BONES-SEED (Skeletal Everyday Embodiment Dataset)** (Bones Studio, March 2026)
- 142,220 annotated motion animations for humanoid robotics. SOMA and Unitree G1 formats. 288 hours publicly available.
- [Dataset](https://huggingface.co/datasets/bones-studio/seed)

**GR00T Whole-Body Control** (NVIDIA, 2025-2026)
- Unified platform for humanoid controllers, connected to Kimodo for motion generation.
- [GitHub](https://github.com/NVlabs/GR00T-WholeBodyControl)

---

### Category 6: Concurrent Humanoid Data Generation via Diffusion (2025-2026)

**NVIDIA Synthetic Motion Generation Pipeline** (2026)
- 780K synthetic trajectories in 11 hours from recorded demonstrations. Improved GR00T N1 performance by 40%. Combines real + synthetic data.
- [Blog](https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/)

**HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning** (OpenReview, 2026)
- Automated task creation and demonstration collection using atomic dexterous skills + LLM reasoning. Shows scaling of 2D/3D diffusion policies with generated data.
- [Paper](https://openreview.net/forum?id=Mk9ykil8eP)

**Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions** (CoRL 2025)
- Multi-stage pipeline: PhysDiff (diffusion-based) generates human motion from text, then retargets to humanoid robot (Fourier GR1), then VLM edits finger/head motions. 86.7% human preference rate.
- [Paper](https://arxiv.org/abs/2410.12773) | [Project](https://ut-austin-rpl.github.io/Harmon/)

**BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion** (arXiv, August 2025)
- Unified diffusion policy for humanoid control. Uses classifier guidance for zero-shot task-specific control. Supports motion inpainting, joystick teleoperation, obstacle avoidance. Deployed on real hardware.
- [Paper](https://arxiv.org/abs/2508.08241)

**Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking** (arXiv, April 2026)
- Trains diffusion model on retargeted human motions for real-time terrain-aware reference motion prediction. Concurrent RL-based whole-body tracker. Deployed on Unitree G1.
- [Paper](https://arxiv.org/abs/2604.17335)

**PHUMA: Physically-Grounded Humanoid Locomotion Dataset** (ICLR 2026)
- Physics-constrained retargeting (PhySINK) from human video. Outperforms Humanoid-X and AMASS datasets.
- [Paper](https://arxiv.org/abs/2510.26236)

**Dexterous World Models (DWM)** (arXiv, December 2025)
- Video diffusion framework using inpainting to model how dexterous hand actions change 3D scenes. Initialized from pretrained video inpainting model. Converts human-scene interaction videos to robot-scene interaction.
- [Paper](https://arxiv.org/abs/2512.17907)

---

### Key Papers the Proposal Likely Needs to Address

The papers most likely to be missed and most directly relevant to a "compositional humanoid trajectory generation using body-part inpainting on diffusion models" proposal are:

1. **FrankenMotion** (Jan 2026) -- Part-level motion generation with diffusion, extremely close in concept
2. **MaskedMimic** (NVIDIA, 2024) -- Motion inpainting with partial/masked body joint specifications in a physics-based diffusion setting
3. **CondMDI** (SIGGRAPH 2024) -- Masked joint diffusion conditioning
4. **STMC** (CVPR Workshop 2024) -- Body-part-aware denoising aggregation at test time
5. **EnergyMoGen / DeMoGen** (CVPR 2025 / Dec 2025) -- Energy-based compositional/decompositional alternatives
6. **Motion-Adapter** (April 2026) -- Very recent structural masking approach for compound actions
7. **BeyondMimic** (Aug 2025) -- Diffusion-based humanoid control with motion inpainting capability
8. **Harmon** (CoRL 2025) -- Diffusion-based whole-body humanoid motion generation from language
9. **Prosthetic Hand Gestures pipeline** (2024) -- Body-part inpainting on kinematic rig for robot hands
10. **Kimodo v1.1** (April 2026) -- Benchmarks and multi-prompt support may overlap with compositional approach

Sources:
- [FrankenMotion](https://arxiv.org/abs/2601.10909)
- [EnergyMoGen](https://arxiv.org/abs/2412.14706)
- [DeMoGen](https://arxiv.org/abs/2512.22324)
- [SINC](https://arxiv.org/abs/2304.10417)
- [MCD](https://arxiv.org/abs/2409.11920)
- [STMC](https://arxiv.org/abs/2401.08559)
- [BA-IDM](https://dl.acm.org/doi/10.1145/3743093.3770934)
- [Motion-Adapter](https://arxiv.org/html/2604.16135v1)
- [FineMoGen](https://arxiv.org/abs/2312.15004)
- [CompDiffuser](https://arxiv.org/abs/2503.05153)
- [DartControl](https://zkf1997.github.io/DART/)
- [MotionStreamer](https://arxiv.org/abs/2503.15451)
- [MaskedMimic](https://arxiv.org/abs/2409.14393)
- [CondMDI](https://arxiv.org/abs/2405.11126)
- [COIN](https://arxiv.org/html/2408.16426)
- [MDM](https://guytevet.github.io/mdm-page/)
- [Prosthetic Hand Gestures](https://kaseungyup.github.io/natural-prosthetic-hand-gestures/)
- [RobotMDM](https://dl.acm.org/doi/10.1145/3680528.3687626)
- [DiffusionSeeder](https://arxiv.org/abs/2410.16727)
- [CoDiG](https://arxiv.org/abs/2505.13131)
- [Diffusion Predictive Control](https://arxiv.org/html/2412.09342)
- [Kimodo](https://research.nvidia.com/labs/sil/projects/kimodo/)
- [BONES-SEED](https://huggingface.co/datasets/bones-studio/seed)
- [GR00T WBC](https://github.com/NVlabs/GR00T-WholeBodyControl)
- [NVIDIA Synthetic Pipeline](https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/)
- [HumanoidGen](https://openreview.net/forum?id=Mk9ykil8eP)
- [Harmon](https://arxiv.org/abs/2410.12773)
- [BeyondMimic](https://arxiv.org/abs/2508.08241)
- [Whole-Body Humanoid Locomotion](https://arxiv.org/abs/2604.17335)
- [PHUMA](https://arxiv.org/abs/2510.26236)
- [Dexterous World Models](https://arxiv.org/abs/2512.17907)

agentId: a7ec97cca13734ab9 (use SendMessage with to: 'a7ec97cca13734ab9' to continue this agent)
&lt;usage>total_tokens: 53344
tool_uses: 40
duration_ms: 245995&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4543c899-3e79-4843-bc6f-a0d4629090ef",
  "isSidechain": false,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "type": "user",
  "uuid": "1a019945-eef5-4a61-89f5-bdcd32de8d1b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me verify an ML research proposal about compositional humanoid trajectory generation using body-part inpainting on diffusion models. I need to find ANY competing or closely related work the proposal may have missed. Search thoroughly for:\n\n1. **Compositional body-part motion generation 2025-2026**: Search for recent papers that decompose motion generation by body parts using diffusion models. Try multiple queries:\n   - \"body part compositional motion diffusion 2026\"\n   - \"spatial composition motion generation diffusion\"\n   - \"body part inpainting motion diffusion\"\n   - \"humanoid compositional trajectory generation\"\n\n2. **Iterative conditional generation in diffusion**: Search for papers that use sequential conditional diffusion processes (generate one part, then condition the next generation on it), as opposed to score composition. Try:\n   - \"iterative conditional diffusion generation\"\n   - \"sequential conditional diffusion composition\"\n   - \"autoregressive diffusion spatial composition\"\n\n3. **Robot motion diffusion with inpainting/masking 2025-2026**: Search for papers that apply inpainting or masking to robot-specific (not human) motion diffusion models:\n   - \"robot motion diffusion inpainting\"\n   - \"masked robot trajectory diffusion\"\n   - \"constraint conditioning diffusion robot\"\n\n4. **Kimodo extensions or follow-up work**: Search for any papers building on Kimodo (NVIDIA, March 2026):\n   - \"Kimodo motion generation\"\n   - \"BONES-SEED diffusion\"\n   - \"G1 humanoid diffusion\"\n\n5. **Any concurrent work on humanoid data generation via diffusion**: \n   - \"humanoid data generation diffusion 2026\"\n   - \"synthetic humanoid training data diffusion\"\n\nUse WebSearch for each query. Report ALL papers found with titles, venues, dates, and brief descriptions. I need to know if there's anything the proposal missed.",
    "agentId": "a7ec97cca13734ab9",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive results. Here is my full report of all relevant and competing work found:\n\n---\n\n## Comprehensive Literature Search Results\n\n### Category 1: Compositional Body-Part Motion Generation (2024-2026)\n\n**FrankenMotion: Part-level Human Motion Generation and Composition** (arXiv, January 2026)\n- A transformer-based diffusion model that accepts sequence-level, action-level, AND part-level text prompts. It constructs a dataset with atomic, temporally-aware part-level annotations using LLMs. This is the MOST DIRECTLY competing work -- it explicitly decomposes motion by body parts and generates part-conditioned motion using diffusion. First to provide atomic, temporally-aware part-level motion annotations.\n- [Paper](https://arxiv.org/abs/2601.10909) | [Project](https://coral79.github.io/frankenmotion/)\n\n**EnergyMoGen: Compositional Human Motion Generation with Energy-Based Diffusion Model in Latent Space** (CVPR 2025)\n- Uses energy-based composition of multiple diffusion models in latent space for compositional motion. Introduces \"Synergistic Energy Fusion\" to combine multiple energy terms corresponding to text descriptions. Achieves concept conjunction, negation, and multi-concept composition.\n- [Paper](https://arxiv.org/abs/2412.14706) | [Project](https://jiro-zhang.github.io/EnergyMoGen/)\n\n**DeMoGen: Towards Decompositional Human Motion Generation with Energy-Based Diffusion Models** (arXiv, December 2025)\n- Inverse of composition: decomposes holistic motion into semantically meaningful sub-components using an energy-based diffusion model. Three training variants (explicit decomposition, orthogonal self-supervised, semantic consistency). Enables disentangling reusable motion primitives from complex sequences.\n- [Paper](https://arxiv.org/abs/2512.22324) | [Project](https://jiro-zhang.github.io/DeMoGen/)\n\n**SINC: Spatial Composition of 3D Human Motions for Simultaneous Action Generation** (ICCV 2023)\n- Uses GPT-3 to map actions to body parts, then combines body parts from two motions. Creates synthetic compositional training data. Earlier foundational work on spatial composition of body parts.\n- [Paper](https://arxiv.org/abs/2304.10417)\n\n**Motion Composition Diffusion (MCD): Generation of Complex 3D Human Motion by Temporal and Spatial Composition of Diffusion Models** (arXiv, September 2024)\n- Decomposes complex actions into sub-movements via GPT, processes each individually during denoising, then combines. Handles both temporal and spatial composition. Agnostic to spatial overlap, no need for body-part specification.\n- [Paper](https://arxiv.org/abs/2409.11920)\n\n**STMC: Multi-Track Timeline Control for Text-Driven 3D Human Motion Generation** (CVPR Workshop 2024)\n- Multi-track timeline with overlapping text prompts. At each denoising step, processes each timeline interval individually, then aggregates predictions with consideration for specific body parts engaged. Test-time method compatible with any pre-trained motion diffusion model.\n- [Paper](https://arxiv.org/abs/2401.08559) | [GitHub](https://github.com/nv-tlabs/stmc)\n\n**BA-IDM: Body-Aware Diffusion for 3D Human Motion Generation** (MMAsia 2025)\n- Divides body into five parts (head, left arm, right arm, spine, legs). Maps complex text instructions to specific body parts. Includes RL and conditional guidance for stable generation in complex scenes.\n- [Paper](https://dl.acm.org/doi/10.1145/3743093.3770934)\n\n**Motion-Adapter: A Diffusion Model Adapter for Text-to-Motion Generation of Compound Actions** (arXiv, April 2026)\n- Plug-and-play adapter that computes decoupled cross-attention maps serving as structural masks during denoising. Trained on single-action motions only. Addresses catastrophic neglect and attention collapse. Very recent.\n- [Paper](https://arxiv.org/html/2604.16135v1)\n\n**FineMoGen: Fine-Grained Spatio-Temporal Motion Generation and Editing** (NeurIPS area)\n- Builds a Spatio-Temporal Mixture Attention (SAMI) architecture for explicit spatial-temporal composition constraints.\n- [Paper](https://arxiv.org/abs/2312.15004)\n\n---\n\n### Category 2: Iterative/Sequential Conditional Generation in Diffusion\n\n**CompDiffuser: Generative Trajectory Stitching through Diffusion Composition** (arXiv, March 2025)\n- Autoregressive sampling of multiple short-horizon diffusion models, stitching them into longer trajectories. Uses noise-conditioned score function formulation. Models overlapping chunks with conditional relationships via a single bidirectional diffusion model. Tested on 50D humanoid (HumanoidMaze).\n- [Paper](https://arxiv.org/abs/2503.05153) | [Project](https://comp-diffuser.github.io/)\n\n**DartControl (DART): A Diffusion-Based Autoregressive Motion Model for Real-Time Text-Driven Motion Control** (2024)\n- Autoregressive latent diffusion for motion primitive generation, jointly conditioned on text prompts and motion history. Supports spatial constraints, waypoint goal reaching, and in-betweening.\n- [Paper](https://zkf1997.github.io/DART/)\n\n**MotionStreamer: Streaming Motion Generation via Diffusion-based Autoregressive Model in Causal Latent Space** (ICCV 2025)\n- Continuous causal latent space with probabilistic autoregressive model. Supports multi-round generation, long-term generation, and dynamic motion composition.\n- [Paper](https://arxiv.org/abs/2503.15451)\n\n---\n\n### Category 3: Inpainting/Masking in Motion Diffusion\n\n**MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting** (NVIDIA, ACM TOG 2024)\n- HIGHLY RELEVANT. Formulates physics-based character control as motion inpainting. Single unified model synthesizes motions from partial (masked) motion descriptions -- masked keyframes, objects, text, or combinations. Supports partial joint targets, joystick control, text commands, and multi-modal composition.\n- [Paper](https://arxiv.org/abs/2409.14393) | [Project](https://research.nvidia.com/labs/par/maskedmimic/)\n\n**CondMDI: Flexible Motion In-betweening with Diffusion Models** (SIGGRAPH 2024)\n- Trains on randomly sampled keyframes with randomly sampled joints and a mask indicating observations. Supports partial keyframe constraints (subset of joints). Replaces noisy input with given keyframes and concatenates observation mask.\n- [Paper](https://arxiv.org/abs/2405.11126)\n\n**COIN: Control-Inpainting Diffusion Prior for Human and Camera Motion Estimation** (ECCV 2024)\n- Soft inpainting strategy that identifies high-confidence regions and uses them as soft constraints while re-sampling low-confidence regions from scratch.\n- [Paper](https://arxiv.org/html/2408.16426)\n\n**MDM: Human Motion Diffusion Model** (ICLR 2023)\n- Original work demonstrating inpainting in joint space for semantic editing of specific body parts.\n- [Paper](https://guytevet.github.io/mdm-page/)\n\n**Towards Natural Prosthetic Hand Gestures: A Common-Rig and Diffusion Inpainting Pipeline** (IEEE, 2024)\n- Directly relevant: generates hand motion from body motion via diffusion-based inpainting on a common kinematic rig. Conditions hand generation on body-only motion. Validated on a real robotic system.\n- [Paper](https://kaseungyup.github.io/natural-prosthetic-hand-gestures/)\n\n---\n\n### Category 4: Robot-Specific Motion Diffusion\n\n**RobotMDM: Robot Motion Diffusion Model** (SIGGRAPH Asia 2024, Disney Research)\n- Integrates kinematic generative motion models with physics-based character control. Generalizes across human, non-human, and synthetic morphologies. Tested on a bipedal robot (20 DoF).\n- [Paper](https://dl.acm.org/doi/10.1145/3680528.3687626)\n\n**DiffusionSeeder: Seeding Motion Optimization with Diffusion for Rapid Motion Planning** (CoRL 2025)\n- Uses diffusion to generate trajectory seeds for motion optimization. 12x speed-up on average. Sim2real on Franka robot.\n- [Paper](https://arxiv.org/abs/2410.16727)\n\n**CoDiG: Constraint-Aware Diffusion Guidance for Robotics** (arXiv, May 2025)\n- Integrates barrier functions into denoising to guide toward constraint-satisfying outputs. Real-world racing experiments.\n- [Paper](https://arxiv.org/abs/2505.13131)\n\n**Diffusion Predictive Control with Constraints** (arXiv, December 2024)\n- Model-based projections in trajectory denoising for constraint-satisfying, dynamically feasible trajectories.\n- [Paper](https://arxiv.org/html/2412.09342)\n\n---\n\n### Category 5: Kimodo Ecosystem and Extensions\n\n**Kimodo: Scaling Controllable Human Motion Generation** (NVIDIA, March 16, 2026)\n- Kinematic motion diffusion model trained on 700 hours of mocap (BONES-RigPlay). Five model variants (SOMA, G1, SMPL-X). Supports text + full-body keyframes, sparse joint positions/rotations, 2D waypoints, dense 2D paths. Two-stage denoiser separating root and body prediction. Open-source code, closed data.\n- Updates: v1.1 models + benchmark (April 10, 2026); multi-prompt improvements (April 24, 2026).\n- Integrated into GEAR-SONIC interactive demo.\n- [Project](https://research.nvidia.com/labs/sil/projects/kimodo/) | [GitHub](https://github.com/nv-tlabs/kimodo)\n\n**BONES-SEED (Skeletal Everyday Embodiment Dataset)** (Bones Studio, March 2026)\n- 142,220 annotated motion animations for humanoid robotics. SOMA and Unitree G1 formats. 288 hours publicly available.\n- [Dataset](https://huggingface.co/datasets/bones-studio/seed)\n\n**GR00T Whole-Body Control** (NVIDIA, 2025-2026)\n- Unified platform for humanoid controllers, connected to Kimodo for motion generation.\n- [GitHub](https://github.com/NVlabs/GR00T-WholeBodyControl)\n\n---\n\n### Category 6: Concurrent Humanoid Data Generation via Diffusion (2025-2026)\n\n**NVIDIA Synthetic Motion Generation Pipeline** (2026)\n- 780K synthetic trajectories in 11 hours from recorded demonstrations. Improved GR00T N1 performance by 40%. Combines real + synthetic data.\n- [Blog](https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/)\n\n**HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning** (OpenReview, 2026)\n- Automated task creation and demonstration collection using atomic dexterous skills + LLM reasoning. Shows scaling of 2D/3D diffusion policies with generated data.\n- [Paper](https://openreview.net/forum?id=Mk9ykil8eP)\n\n**Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions** (CoRL 2025)\n- Multi-stage pipeline: PhysDiff (diffusion-based) generates human motion from text, then retargets to humanoid robot (Fourier GR1), then VLM edits finger/head motions. 86.7% human preference rate.\n- [Paper](https://arxiv.org/abs/2410.12773) | [Project](https://ut-austin-rpl.github.io/Harmon/)\n\n**BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion** (arXiv, August 2025)\n- Unified diffusion policy for humanoid control. Uses classifier guidance for zero-shot task-specific control. Supports motion inpainting, joystick teleoperation, obstacle avoidance. Deployed on real hardware.\n- [Paper](https://arxiv.org/abs/2508.08241)\n\n**Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking** (arXiv, April 2026)\n- Trains diffusion model on retargeted human motions for real-time terrain-aware reference motion prediction. Concurrent RL-based whole-body tracker. Deployed on Unitree G1.\n- [Paper](https://arxiv.org/abs/2604.17335)\n\n**PHUMA: Physically-Grounded Humanoid Locomotion Dataset** (ICLR 2026)\n- Physics-constrained retargeting (PhySINK) from human video. Outperforms Humanoid-X and AMASS datasets.\n- [Paper](https://arxiv.org/abs/2510.26236)\n\n**Dexterous World Models (DWM)** (arXiv, December 2025)\n- Video diffusion framework using inpainting to model how dexterous hand actions change 3D scenes. Initialized from pretrained video inpainting model. Converts human-scene interaction videos to robot-scene interaction.\n- [Paper](https://arxiv.org/abs/2512.17907)\n\n---\n\n### Key Papers the Proposal Likely Needs to Address\n\nThe papers most likely to be missed and most directly relevant to a \"compositional humanoid trajectory generation using body-part inpainting on diffusion models\" proposal are:\n\n1. **FrankenMotion** (Jan 2026) -- Part-level motion generation with diffusion, extremely close in concept\n2. **MaskedMimic** (NVIDIA, 2024) -- Motion inpainting with partial/masked body joint specifications in a physics-based diffusion setting\n3. **CondMDI** (SIGGRAPH 2024) -- Masked joint diffusion conditioning\n4. **STMC** (CVPR Workshop 2024) -- Body-part-aware denoising aggregation at test time\n5. **EnergyMoGen / DeMoGen** (CVPR 2025 / Dec 2025) -- Energy-based compositional/decompositional alternatives\n6. **Motion-Adapter** (April 2026) -- Very recent structural masking approach for compound actions\n7. **BeyondMimic** (Aug 2025) -- Diffusion-based humanoid control with motion inpainting capability\n8. **Harmon** (CoRL 2025) -- Diffusion-based whole-body humanoid motion generation from language\n9. **Prosthetic Hand Gestures pipeline** (2024) -- Body-part inpainting on kinematic rig for robot hands\n10. **Kimodo v1.1** (April 2026) -- Benchmarks and multi-prompt support may overlap with compositional approach\n\nSources:\n- [FrankenMotion](https://arxiv.org/abs/2601.10909)\n- [EnergyMoGen](https://arxiv.org/abs/2412.14706)\n- [DeMoGen](https://arxiv.org/abs/2512.22324)\n- [SINC](https://arxiv.org/abs/2304.10417)\n- [MCD](https://arxiv.org/abs/2409.11920)\n- [STMC](https://arxiv.org/abs/2401.08559)\n- [BA-IDM](https://dl.acm.org/doi/10.1145/3743093.3770934)\n- [Motion-Adapter](https://arxiv.org/html/2604.16135v1)\n- [FineMoGen](https://arxiv.org/abs/2312.15004)\n- [CompDiffuser](https://arxiv.org/abs/2503.05153)\n- [DartControl](https://zkf1997.github.io/DART/)\n- [MotionStreamer](https://arxiv.org/abs/2503.15451)\n- [MaskedMimic](https://arxiv.org/abs/2409.14393)\n- [CondMDI](https://arxiv.org/abs/2405.11126)\n- [COIN](https://arxiv.org/html/2408.16426)\n- [MDM](https://guytevet.github.io/mdm-page/)\n- [Prosthetic Hand Gestures](https://kaseungyup.github.io/natural-prosthetic-hand-gestures/)\n- [RobotMDM](https://dl.acm.org/doi/10.1145/3680528.3687626)\n- [DiffusionSeeder](https://arxiv.org/abs/2410.16727)\n- [CoDiG](https://arxiv.org/abs/2505.13131)\n- [Diffusion Predictive Control](https://arxiv.org/html/2412.09342)\n- [Kimodo](https://research.nvidia.com/labs/sil/projects/kimodo/)\n- [BONES-SEED](https://huggingface.co/datasets/bones-studio/seed)\n- [GR00T WBC](https://github.com/NVlabs/GR00T-WholeBodyControl)\n- [NVIDIA Synthetic Pipeline](https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/)\n- [HumanoidGen](https://openreview.net/forum?id=Mk9ykil8eP)\n- [Harmon](https://arxiv.org/abs/2410.12773)\n- [BeyondMimic](https://arxiv.org/abs/2508.08241)\n- [Whole-Body Humanoid Locomotion](https://arxiv.org/abs/2604.17335)\n- [PHUMA](https://arxiv.org/abs/2510.26236)\n- [Dexterous World Models](https://arxiv.org/abs/2512.17907)"
      }
    ],
    "totalDurationMs": 245995,
    "totalTokens": 53344,
    "totalToolUseCount": 40,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2908,
      "cache_read_input_tokens": 45828,
      "output_tokens": 4607,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2908
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4607,
          "cache_read_input_tokens": 45828,
          "cache_creation_input_tokens": 2908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2908,
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
      "otherToolCount": 40
    }
  },
  "sourceToolAssistantUUID": "4543c899-3e79-4843-bc6f-a0d4629090ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "1a019945-eef5-4a61-89f5-bdcd32de8d1b",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Humanoid body-part compositional diffusion with out-of-distribution constraint testing",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257"
}
```

---

### Tool call

_source line 16 · 2026-05-10T20:29:08.554Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015MTDcb9GXMcTVwwkUHT5k7`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify theory refs and CFG claims",
  "prompt": "You are helping me verify claims in an ML research proposal. Search for and verify the following theoretical references:\n\n1. **CFG++ (Chung et al., ICLR 2025, arXiv 2406.08070)**: Verify it exists, check if it really reveals that standard CFG pushes samples off the data manifold, and confirm it was accepted at ICLR 2025.\n\n2. **S-CFG / Rethinking Spatial Inconsistency in CFG (Shen et al., CVPR 2024, arXiv 2404.05384)**: Verify it exists and the claim about spatial inconsistency from uniform guidance scaling.\n\n3. **Mechanisms of Projective Composition (Bradley et al., ICML 2025, arXiv 2502.04549)**: Verify it exists and the claim that score composition requires approximate independence/factorization between composed components.\n\n4. **Refining Compositional Diffusion (RCD, arXiv 2605.03075, May 2026)**: Verify this paper exists. The arXiv ID 2605.xxxxx would be from May 2026 — check if this is real or fabricated.\n\n5. **MixerMDM (CVPR 2025, arXiv 2504.01019)**: Verify it exists, was accepted at CVPR 2025, and does body-joint-level composition of frozen diffusion models via spatial mixing weights.\n\n6. **MaskedManipulator (SIGGRAPH Asia 2025, arXiv 2505.19086)**: Verify it exists and extends MaskedMimic to loco-manipulation.\n\n7. **SkillBlender / SkillBench (arXiv 2506.09366)**: Verify this exists and provides 8 G1 loco-manipulation tasks.\n\n8. **Annealing Guidance (Yehezkel et al., SIGGRAPH Asia 2025, arXiv 2506.24108)**: Verify existence.\n\nUse WebSearch to check each paper. Report which ones you can confirm and which may be fabricated."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a019945-eef5-4a61-89f5-bdcd32de8d1b",
  "isSidechain": false,
  "requestId": "req_011CauX7Te1W65J9y3uk6Vve",
  "type": "assistant",
  "uuid": "975e16b6-772f-44d0-b0eb-217994bcdca5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BeAR4xsXx2NK7L7YJwQ78L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5214,
      "cache_read_input_tokens": 45172,
      "output_tokens": 596,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5214,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 596,
          "cache_read_input_tokens": 45172,
          "cache_creation_input_tokens": 5214,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5214
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

_source line 17 · 2026-05-10T20:31:05.039Z_

<details><summary>↩ Tool result · `toolu_015MTDcb9GXMcTVwwkUHT5k7`</summary>

```text
I now have comprehensive information on all eight papers. Here is my full verification report:

---

## Verification Report: ML Research Proposal References

### 1. CFG++ (Chung et al., ICLR 2025, arXiv 2406.08070) -- CONFIRMED

- **Exists:** Yes. "CFG++: Manifold-constrained Classifier Free Guidance for Diffusion Models" by Hyungjin Chung, Jeongsol Kim, Geon Yeong Park, Hyelin Nam, and Jong Chul Ye.
- **ICLR 2025 acceptance:** Confirmed. It appears in the ICLR 2025 proceedings and has a poster page on `iclr.cc/virtual/2025/poster/30421`. The official GitHub repo also states "[ICLR2025]".
- **Claim about off-manifold:** Confirmed. The paper reveals that standard CFG's problems (lack of invertibility, mode collapse at high guidance scales) stem from an "off-manifold phenomenon" -- i.e., CFG pushes samples off the data manifold. CFG++ reformulates text-guidance as an inverse problem to stay on-manifold.

### 2. S-CFG / Rethinking Spatial Inconsistency (Shen et al., CVPR 2024, arXiv 2404.05384) -- CONFIRMED

- **Exists:** Yes. "Rethinking the Spatial Inconsistency in Classifier-Free Diffusion Guidance" by Dazhong Shen et al.
- **CVPR 2024 acceptance:** Confirmed. The paper appears in CVPR 2024 proceedings on `openaccess.thecvf.com` and has a CVPR 2024 poster page.
- **Claim about spatial inconsistency from uniform guidance scaling:** Confirmed. The paper argues that a global/uniform CFG scale results in spatial inconsistency across regions with varying semantic strengths, leading to suboptimal image quality. S-CFG addresses this by adaptively adjusting CFG scales across different semantic regions.

### 3. Mechanisms of Projective Composition (Bradley et al., ICML 2025, arXiv 2502.04549) -- CONFIRMED

- **Exists:** Yes. "Mechanisms of Projective Composition of Diffusion Models" by Arwen Bradley, Preetum Nakkiran, David Berthelot, James Thornton, and Joshua M. Susskind (Apple).
- **ICML 2025 acceptance:** Confirmed. Has an ICML 2025 poster page (`icml.cc/virtual/2025/poster/45339`) and is listed in Apple's ICML 2025 publications.
- **Claim about approximate independence/factorization:** Confirmed, with nuance. The paper introduces formal "Factorized Conditionals" criteria (Definition 5.2), which is a form of independence condition along both distributions and coordinates. When this condition holds, projective composition can be achieved by linearly combining scores. In practice, "cluttered" settings approximately satisfy this condition. So the claim is essentially correct -- successful score composition requires an approximate factorization/independence between composed components.

### 4. Refining Compositional Diffusion (RCD, arXiv 2605.03075, May 2026) -- CONFIRMED (exists on arXiv)

- **Exists:** Yes. "Refining Compositional Diffusion for Reliable Long-Horizon Planning" by Kyowoon Lee, Yunhao Luo, Anh Tong, and Jaesik Choi (KAIST, U. Michigan, Korea University, INEEJI). Submitted to arXiv on May 4, 2026.
- **Suspicion of fabrication:** Not fabricated. The arXiv ID 2605.xxxxx is consistent with a May 2026 submission, and the paper does appear on arXiv. It is a training-free guidance method for compositional diffusion planning that addresses mode-averaging in multimodal local plan distributions. The paper is a preprint with no confirmed venue acceptance yet.
- **Note:** Since today's date is May 10, 2026, this is a very recent preprint (6 days old). Its existence is confirmed but it is fresh and not yet peer-reviewed.

### 5. MixerMDM (CVPR 2025, arXiv 2504.01019) -- CONFIRMED

- **Exists:** Yes. "MixerMDM: Learnable Composition of Human Motion Diffusion Models" by Pablo Ruiz-Ponce et al.
- **CVPR 2025 acceptance:** Confirmed. Has a CVPR 2025 poster page (`cvpr.thecvf.com/virtual/2025/poster/33404`), the official GitHub says "[CVPR 2025]", and it appears in the CVPR 2025 Open Access Repository.
- **Claim about body-joint-level composition of frozen diffusion models via spatial mixing weights:** Partially confirmed. MixerMDM does perform composition of pre-trained (frozen) motion diffusion models and offers mixing at multiple granularities including "body joint" level as well as global, motion-duration, and spatio-temporal levels. The mixing strategy is learned via adversarial training. It is described as "learnable composition" rather than just "spatial mixing weights," so the proposal's characterization is a reasonable simplification but not an exact quote.

### 6. MaskedManipulator (SIGGRAPH Asia 2025, arXiv 2505.19086) -- CONFIRMED

- **Exists:** Yes. "MaskedManipulator: Versatile Whole-Body Manipulation" (also titled "Versatile Whole-Body Control for Loco-Manipulation").
- **SIGGRAPH Asia 2025 acceptance:** Confirmed. Published in the Proceedings of SIGGRAPH Asia 2025 Conference Papers (December 15-18, 2025, Hong Kong), with a DOI on `dl.acm.org`.
- **Claim about extending MaskedMimic to loco-manipulation:** Confirmed. The paper explicitly extends the MaskedMimic framework to enable full-body loco-manipulation, providing spatio-temporal goal-conditioning on both humanoid body parts and manipulated objects.

### 7. SkillBlender / SkillBench (arXiv 2506.09366) -- CONFIRMED, with a caveat on the specific claim

- **Exists:** Yes. "SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending." Has an official GitHub repository and project page.
- **Claim about "8 G1 loco-manipulation tasks":** Partially accurate / misleadingly stated. SkillBench contains 8 loco-manipulation tasks total, but these tasks are cross-embodiment -- they span three Unitree humanoid embodiments (H1, G1, and H1-2), not exclusively G1. The 8 tasks are: FarReach, ButtonPress, CabinetClose, FootballShoot, BoxPush, PackageLift, BoxTransfer, PackageCarry. Saying "8 G1 loco-manipulation tasks" could imply the tasks are G1-specific, when in fact SkillBench is a cross-embodiment benchmark. The tasks can be run on G1, but they are not "G1 tasks" exclusively.

### 8. Annealing Guidance (Yehezkel et al., SIGGRAPH Asia 2025, arXiv 2506.24108) -- CONFIRMED

- **Exists:** Yes. "Navigating with Annealing Guidance Scale in Diffusion Space" by Shai Yehezkel, Omer Dahary, Andrey Voynov, and Daniel Cohen-Or.
- **SIGGRAPH Asia 2025 acceptance:** Confirmed. Published in the Proceedings of SIGGRAPH Asia 2025 Conference Papers, with a DOI on `dl.acm.org` (`10.1145/3757377.3763830`).
- **Content:** Proposes an annealing guidance scheduler that dynamically adjusts the CFG guidance scale during sampling based on the conditional noisy signal, learned via a scheduling policy.

---

## Summary Table

| # | Paper | Exists | Venue Confirmed | Key Claims Accurate |
|---|-------|--------|----------------|---------------------|
| 1 | CFG++ | Yes | ICLR 2025 -- Yes | Yes (off-manifold) |
| 2 | S-CFG | Yes | CVPR 2024 -- Yes | Yes (spatial inconsistency) |
| 3 | Projective Composition | Yes | ICML 2025 -- Yes | Yes (factorization condition) |
| 4 | RCD (2605.03075) | Yes | Preprint only (no venue) | N/A (very recent preprint) |
| 5 | MixerMDM | Yes | CVPR 2025 -- Yes | Mostly yes (minor simplification) |
| 6 | MaskedManipulator | Yes | SIGGRAPH Asia 2025 -- Yes | Yes (extends MaskedMimic) |
| 7 | SkillBlender/SkillBench | Yes | Preprint (no venue listed) | Partially -- 8 tasks are cross-embodiment, not G1-specific |
| 8 | Annealing Guidance | Yes | SIGGRAPH Asia 2025 -- Yes | Yes |

**Bottom line:** All 8 papers are real and verifiable on arXiv. None appear to be fabricated. The venue claims are accurate for all papers where a venue was claimed (6 of 8). The two preprints (RCD and SkillBlender) have no venue claims to verify beyond arXiv. The only notable inaccuracy in the proposal's citations is the characterization of SkillBench as providing "8 G1 loco-manipulation tasks" -- the 8 tasks exist but are cross-embodiment (H1, G1, H1-2), not G1-exclusive.

Sources:
- [CFG++ on arXiv](https://arxiv.org/abs/2406.08070)
- [CFG++ ICLR 2025 Poster](https://iclr.cc/virtual/2025/poster/30421)
- [CFG++ GitHub](https://github.com/CFGpp-diffusion/CFGpp)
- [S-CFG on arXiv](https://arxiv.org/abs/2404.05384)
- [S-CFG CVPR 2024 Poster](https://cvpr.thecvf.com/virtual/2024/poster/30715)
- [S-CFG CVPR 2024 Proceedings](https://openaccess.thecvf.com/content/CVPR2024/papers/Shen_Rethinking_the_Spatial_Inconsistency_in_Classifier-Free_Diffusion_Guidance_CVPR_2024_paper.pdf)
- [Projective Composition on arXiv](https://arxiv.org/abs/2502.04549)
- [Projective Composition ICML 2025 Poster](https://icml.cc/virtual/2025/poster/45339)
- [Projective Composition - Apple ML Research](https://machinelearning.apple.com/research/mechanisms-of-projective-composition)
- [RCD on arXiv](https://arxiv.org/abs/2605.03075)
- [MixerMDM on arXiv](https://arxiv.org/abs/2504.01019)
- [MixerMDM CVPR 2025 Poster](https://cvpr.thecvf.com/virtual/2025/poster/33404)
- [MixerMDM CVPR 2025 Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Ruiz-Ponce_MixerMDM_Learnable_Composition_of_Human_Motion_Diffusion_Models_CVPR_2025_paper.html)
- [MixerMDM GitHub](https://github.com/pabloruizponce/MixerMDM)
- [MaskedManipulator on arXiv](https://arxiv.org/abs/2505.19086)
- [MaskedManipulator SIGGRAPH Asia 2025](https://doi.org/10.1145/3757377.3763934)
- [SkillBlender on arXiv](https://arxiv.org/abs/2506.09366)
- [SkillBlender GitHub](https://github.com/Humanoid-SkillBlender/SkillBlender)
- [Annealing Guidance on arXiv](https://arxiv.org/abs/2506.24108)
- [Annealing Guidance SIGGRAPH Asia 2025](https://doi.org/10.1145/3757377.3763830)

agentId: a15b7d4854ee07d9d (use SendMessage with to: 'a15b7d4854ee07d9d' to continue this agent)
&lt;usage>total_tokens: 26028
tool_uses: 14
duration_ms: 116480&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "975e16b6-772f-44d0-b0eb-217994bcdca5",
  "isSidechain": false,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "type": "user",
  "uuid": "3705b88d-1ca9-4b66-9b35-1a843c2e780b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me verify claims in an ML research proposal. Search for and verify the following theoretical references:\n\n1. **CFG++ (Chung et al., ICLR 2025, arXiv 2406.08070)**: Verify it exists, check if it really reveals that standard CFG pushes samples off the data manifold, and confirm it was accepted at ICLR 2025.\n\n2. **S-CFG / Rethinking Spatial Inconsistency in CFG (Shen et al., CVPR 2024, arXiv 2404.05384)**: Verify it exists and the claim about spatial inconsistency from uniform guidance scaling.\n\n3. **Mechanisms of Projective Composition (Bradley et al., ICML 2025, arXiv 2502.04549)**: Verify it exists and the claim that score composition requires approximate independence/factorization between composed components.\n\n4. **Refining Compositional Diffusion (RCD, arXiv 2605.03075, May 2026)**: Verify this paper exists. The arXiv ID 2605.xxxxx would be from May 2026 — check if this is real or fabricated.\n\n5. **MixerMDM (CVPR 2025, arXiv 2504.01019)**: Verify it exists, was accepted at CVPR 2025, and does body-joint-level composition of frozen diffusion models via spatial mixing weights.\n\n6. **MaskedManipulator (SIGGRAPH Asia 2025, arXiv 2505.19086)**: Verify it exists and extends MaskedMimic to loco-manipulation.\n\n7. **SkillBlender / SkillBench (arXiv 2506.09366)**: Verify this exists and provides 8 G1 loco-manipulation tasks.\n\n8. **Annealing Guidance (Yehezkel et al., SIGGRAPH Asia 2025, arXiv 2506.24108)**: Verify existence.\n\nUse WebSearch to check each paper. Report which ones you can confirm and which may be fabricated.",
    "agentId": "a15b7d4854ee07d9d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on all eight papers. Here is my full verification report:\n\n---\n\n## Verification Report: ML Research Proposal References\n\n### 1. CFG++ (Chung et al., ICLR 2025, arXiv 2406.08070) -- CONFIRMED\n\n- **Exists:** Yes. \"CFG++: Manifold-constrained Classifier Free Guidance for Diffusion Models\" by Hyungjin Chung, Jeongsol Kim, Geon Yeong Park, Hyelin Nam, and Jong Chul Ye.\n- **ICLR 2025 acceptance:** Confirmed. It appears in the ICLR 2025 proceedings and has a poster page on `iclr.cc/virtual/2025/poster/30421`. The official GitHub repo also states \"[ICLR2025]\".\n- **Claim about off-manifold:** Confirmed. The paper reveals that standard CFG's problems (lack of invertibility, mode collapse at high guidance scales) stem from an \"off-manifold phenomenon\" -- i.e., CFG pushes samples off the data manifold. CFG++ reformulates text-guidance as an inverse problem to stay on-manifold.\n\n### 2. S-CFG / Rethinking Spatial Inconsistency (Shen et al., CVPR 2024, arXiv 2404.05384) -- CONFIRMED\n\n- **Exists:** Yes. \"Rethinking the Spatial Inconsistency in Classifier-Free Diffusion Guidance\" by Dazhong Shen et al.\n- **CVPR 2024 acceptance:** Confirmed. The paper appears in CVPR 2024 proceedings on `openaccess.thecvf.com` and has a CVPR 2024 poster page.\n- **Claim about spatial inconsistency from uniform guidance scaling:** Confirmed. The paper argues that a global/uniform CFG scale results in spatial inconsistency across regions with varying semantic strengths, leading to suboptimal image quality. S-CFG addresses this by adaptively adjusting CFG scales across different semantic regions.\n\n### 3. Mechanisms of Projective Composition (Bradley et al., ICML 2025, arXiv 2502.04549) -- CONFIRMED\n\n- **Exists:** Yes. \"Mechanisms of Projective Composition of Diffusion Models\" by Arwen Bradley, Preetum Nakkiran, David Berthelot, James Thornton, and Joshua M. Susskind (Apple).\n- **ICML 2025 acceptance:** Confirmed. Has an ICML 2025 poster page (`icml.cc/virtual/2025/poster/45339`) and is listed in Apple's ICML 2025 publications.\n- **Claim about approximate independence/factorization:** Confirmed, with nuance. The paper introduces formal \"Factorized Conditionals\" criteria (Definition 5.2), which is a form of independence condition along both distributions and coordinates. When this condition holds, projective composition can be achieved by linearly combining scores. In practice, \"cluttered\" settings approximately satisfy this condition. So the claim is essentially correct -- successful score composition requires an approximate factorization/independence between composed components.\n\n### 4. Refining Compositional Diffusion (RCD, arXiv 2605.03075, May 2026) -- CONFIRMED (exists on arXiv)\n\n- **Exists:** Yes. \"Refining Compositional Diffusion for Reliable Long-Horizon Planning\" by Kyowoon Lee, Yunhao Luo, Anh Tong, and Jaesik Choi (KAIST, U. Michigan, Korea University, INEEJI). Submitted to arXiv on May 4, 2026.\n- **Suspicion of fabrication:** Not fabricated. The arXiv ID 2605.xxxxx is consistent with a May 2026 submission, and the paper does appear on arXiv. It is a training-free guidance method for compositional diffusion planning that addresses mode-averaging in multimodal local plan distributions. The paper is a preprint with no confirmed venue acceptance yet.\n- **Note:** Since today's date is May 10, 2026, this is a very recent preprint (6 days old). Its existence is confirmed but it is fresh and not yet peer-reviewed.\n\n### 5. MixerMDM (CVPR 2025, arXiv 2504.01019) -- CONFIRMED\n\n- **Exists:** Yes. \"MixerMDM: Learnable Composition of Human Motion Diffusion Models\" by Pablo Ruiz-Ponce et al.\n- **CVPR 2025 acceptance:** Confirmed. Has a CVPR 2025 poster page (`cvpr.thecvf.com/virtual/2025/poster/33404`), the official GitHub says \"[CVPR 2025]\", and it appears in the CVPR 2025 Open Access Repository.\n- **Claim about body-joint-level composition of frozen diffusion models via spatial mixing weights:** Partially confirmed. MixerMDM does perform composition of pre-trained (frozen) motion diffusion models and offers mixing at multiple granularities including \"body joint\" level as well as global, motion-duration, and spatio-temporal levels. The mixing strategy is learned via adversarial training. It is described as \"learnable composition\" rather than just \"spatial mixing weights,\" so the proposal's characterization is a reasonable simplification but not an exact quote.\n\n### 6. MaskedManipulator (SIGGRAPH Asia 2025, arXiv 2505.19086) -- CONFIRMED\n\n- **Exists:** Yes. \"MaskedManipulator: Versatile Whole-Body Manipulation\" (also titled \"Versatile Whole-Body Control for Loco-Manipulation\").\n- **SIGGRAPH Asia 2025 acceptance:** Confirmed. Published in the Proceedings of SIGGRAPH Asia 2025 Conference Papers (December 15-18, 2025, Hong Kong), with a DOI on `dl.acm.org`.\n- **Claim about extending MaskedMimic to loco-manipulation:** Confirmed. The paper explicitly extends the MaskedMimic framework to enable full-body loco-manipulation, providing spatio-temporal goal-conditioning on both humanoid body parts and manipulated objects.\n\n### 7. SkillBlender / SkillBench (arXiv 2506.09366) -- CONFIRMED, with a caveat on the specific claim\n\n- **Exists:** Yes. \"SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending.\" Has an official GitHub repository and project page.\n- **Claim about \"8 G1 loco-manipulation tasks\":** Partially accurate / misleadingly stated. SkillBench contains 8 loco-manipulation tasks total, but these tasks are cross-embodiment -- they span three Unitree humanoid embodiments (H1, G1, and H1-2), not exclusively G1. The 8 tasks are: FarReach, ButtonPress, CabinetClose, FootballShoot, BoxPush, PackageLift, BoxTransfer, PackageCarry. Saying \"8 G1 loco-manipulation tasks\" could imply the tasks are G1-specific, when in fact SkillBench is a cross-embodiment benchmark. The tasks can be run on G1, but they are not \"G1 tasks\" exclusively.\n\n### 8. Annealing Guidance (Yehezkel et al., SIGGRAPH Asia 2025, arXiv 2506.24108) -- CONFIRMED\n\n- **Exists:** Yes. \"Navigating with Annealing Guidance Scale in Diffusion Space\" by Shai Yehezkel, Omer Dahary, Andrey Voynov, and Daniel Cohen-Or.\n- **SIGGRAPH Asia 2025 acceptance:** Confirmed. Published in the Proceedings of SIGGRAPH Asia 2025 Conference Papers, with a DOI on `dl.acm.org` (`10.1145/3757377.3763830`).\n- **Content:** Proposes an annealing guidance scheduler that dynamically adjusts the CFG guidance scale during sampling based on the conditional noisy signal, learned via a scheduling policy.\n\n---\n\n## Summary Table\n\n| # | Paper | Exists | Venue Confirmed | Key Claims Accurate |\n|---|-------|--------|----------------|---------------------|\n| 1 | CFG++ | Yes | ICLR 2025 -- Yes | Yes (off-manifold) |\n| 2 | S-CFG | Yes | CVPR 2024 -- Yes | Yes (spatial inconsistency) |\n| 3 | Projective Composition | Yes | ICML 2025 -- Yes | Yes (factorization condition) |\n| 4 | RCD (2605.03075) | Yes | Preprint only (no venue) | N/A (very recent preprint) |\n| 5 | MixerMDM | Yes | CVPR 2025 -- Yes | Mostly yes (minor simplification) |\n| 6 | MaskedManipulator | Yes | SIGGRAPH Asia 2025 -- Yes | Yes (extends MaskedMimic) |\n| 7 | SkillBlender/SkillBench | Yes | Preprint (no venue listed) | Partially -- 8 tasks are cross-embodiment, not G1-specific |\n| 8 | Annealing Guidance | Yes | SIGGRAPH Asia 2025 -- Yes | Yes |\n\n**Bottom line:** All 8 papers are real and verifiable on arXiv. None appear to be fabricated. The venue claims are accurate for all papers where a venue was claimed (6 of 8). The two preprints (RCD and SkillBlender) have no venue claims to verify beyond arXiv. The only notable inaccuracy in the proposal's citations is the characterization of SkillBench as providing \"8 G1 loco-manipulation tasks\" -- the 8 tasks exist but are cross-embodiment (H1, G1, H1-2), not G1-exclusive.\n\nSources:\n- [CFG++ on arXiv](https://arxiv.org/abs/2406.08070)\n- [CFG++ ICLR 2025 Poster](https://iclr.cc/virtual/2025/poster/30421)\n- [CFG++ GitHub](https://github.com/CFGpp-diffusion/CFGpp)\n- [S-CFG on arXiv](https://arxiv.org/abs/2404.05384)\n- [S-CFG CVPR 2024 Poster](https://cvpr.thecvf.com/virtual/2024/poster/30715)\n- [S-CFG CVPR 2024 Proceedings](https://openaccess.thecvf.com/content/CVPR2024/papers/Shen_Rethinking_the_Spatial_Inconsistency_in_Classifier-Free_Diffusion_Guidance_CVPR_2024_paper.pdf)\n- [Projective Composition on arXiv](https://arxiv.org/abs/2502.04549)\n- [Projective Composition ICML 2025 Poster](https://icml.cc/virtual/2025/poster/45339)\n- [Projective Composition - Apple ML Research](https://machinelearning.apple.com/research/mechanisms-of-projective-composition)\n- [RCD on arXiv](https://arxiv.org/abs/2605.03075)\n- [MixerMDM on arXiv](https://arxiv.org/abs/2504.01019)\n- [MixerMDM CVPR 2025 Poster](https://cvpr.thecvf.com/virtual/2025/poster/33404)\n- [MixerMDM CVPR 2025 Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Ruiz-Ponce_MixerMDM_Learnable_Composition_of_Human_Motion_Diffusion_Models_CVPR_2025_paper.html)\n- [MixerMDM GitHub](https://github.com/pabloruizponce/MixerMDM)\n- [MaskedManipulator on arXiv](https://arxiv.org/abs/2505.19086)\n- [MaskedManipulator SIGGRAPH Asia 2025](https://doi.org/10.1145/3757377.3763934)\n- [SkillBlender on arXiv](https://arxiv.org/abs/2506.09366)\n- [SkillBlender GitHub](https://github.com/Humanoid-SkillBlender/SkillBlender)\n- [Annealing Guidance on arXiv](https://arxiv.org/abs/2506.24108)\n- [Annealing Guidance SIGGRAPH Asia 2025](https://doi.org/10.1145/3757377.3763830)"
      }
    ],
    "totalDurationMs": 116480,
    "totalTokens": 26028,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1055,
      "cache_creation_input_tokens": 1311,
      "cache_read_input_tokens": 20489,
      "output_tokens": 3173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1311
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1055,
          "output_tokens": 3173,
          "cache_read_input_tokens": 20489,
          "cache_creation_input_tokens": 1311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1311,
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
  "sourceToolAssistantUUID": "975e16b6-772f-44d0-b0eb-217994bcdca5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T20:31:16.814Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DxBggVkskF99QuQXKQgbs6`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check CoRL 2026 deadlines and feasibility",
  "prompt": "You are helping me verify claims about venue deadlines and feasibility for an ML research proposal. Search for:\n\n1. **CoRL 2026 deadlines**: Verify the claimed abstract deadline of May 26, 2026 and paper deadline of May 29, 2026. Search for \"CoRL 2026 deadline\" or \"Conference on Robot Learning 2026\". The conference is claimed to be in Austin, Nov 9-12, 2026.\n\n2. **Humanoids 2026 deadline**: Verify the claimed paper deadline of July 24, 2026. Search \"Humanoids 2026 deadline\" or \"IEEE Humanoids 2026\".\n\n3. **NVIDIA Kimodo v1.1 updates**: Search for any updates to Kimodo after the initial March 2026 release. The competing search found mentions of \"v1.1 models + benchmark (April 10, 2026)\" and \"multi-prompt improvements (April 24, 2026)\". Check if Kimodo's multi-prompt support overlaps with the proposal's compositional generation approach.\n\n4. **HumanoidGen (OpenReview, 2026)**: Search for \"HumanoidGen data generation bimanual dexterous manipulation LLM\" — this was found in competing work search and may be directly relevant. Get more details.\n\n5. **NVIDIA synthetic motion generation pipeline for GR00T**: The competing search found \"780K synthetic trajectories in 11 hours\" — search for details about this pipeline and whether it uses compositional generation.\n\nUse WebSearch and WebFetch to verify. Report detailed findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3705b88d-1ca9-4b66-9b35-1a843c2e780b",
  "isSidechain": false,
  "requestId": "req_011CauXHBm4HJeqrDswozW4u",
  "type": "assistant",
  "uuid": "c421a553-e45c-4a48-be61-03cf842ffdd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PYrinEDeuVSedT34viCnEG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3849,
      "cache_read_input_tokens": 50386,
      "output_tokens": 466,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 466,
          "cache_read_input_tokens": 50386,
          "cache_creation_input_tokens": 3849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3849
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

_source line 19 · 2026-05-10T20:33:12.336Z_

<details><summary>↩ Tool result · `toolu_01DxBggVkskF99QuQXKQgbs6`</summary>

```text
Now I have comprehensive information for all five items. Here is the detailed report:

---

## Verification Report

### 1. CoRL 2026 Deadlines -- CONFIRMED

All claimed deadlines and venue details are **verified and accurate**:

- **Abstract deadline**: May 26, 2026, 11:59 UTC -- **confirmed**
- **Paper deadline**: May 29, 2026, 11:59 UTC -- **confirmed**
- **Conference dates**: November 9-12, 2026 (workshops Nov 9, main conference Nov 10-12) -- **confirmed**
- **Location**: JW Marriott Austin, 110 E 2nd St, Austin, TX 78701 -- **confirmed**

Sources:
- [CoRL 2026 Official Site](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [HuggingFace AI Deadlines Commit](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)

---

### 2. Humanoids 2026 Deadline -- CONFIRMED

The claimed paper deadline is **verified**:

- **Paper submission deadline**: July 24, 2026 -- **confirmed**
- **Supplementary video deadline**: July 27, 2026 (optional)
- **Acceptance notification**: October 6, 2026
- **Camera-ready deadline**: October 26, 2026
- **Conference dates**: December 6-9, 2026, Santa Clara, CA, USA
- **Full name**: 25th IEEE-RAS International Conference on Humanoid Robots

Sources:
- [Humanoids 2026 Official Site](https://2026.ieee-humanoids.org/)

---

### 3. NVIDIA Kimodo v1.1 Updates -- CONFIRMED with Important Nuance

The claimed update timeline is **verified**:

- **v1.1 models + Kimodo Motion Generation Benchmark release**: April 10, 2026 -- **confirmed**
- **Multi-prompt improvements**: April 24, 2026 -- **confirmed** (changelog mentions "improved multi-prompt generation and better support for small VRAM GPUs via `TEXT_ENCODER_DEVICE=cpu` env var")

**Critical finding on overlap with compositional generation proposals**: Kimodo's "multi-prompt" capability is **sequential generation with transition constraints**, NOT true compositional generation. Specifically:
- Kimodo is "trained to take a single prompt as input" -- multi-prompt sequencing is a **post-hoc capability**, not an inherent design feature.
- It works by generating motion for the first prompt, then generating the next segment with overlapping frames where full-body keyframe constraints enforce positional and acceleration consistency.
- The overlapping frames are then blended together.
- This is fundamentally **different from compositional generation** where distinct motion primitives or components are combined. A proposal focused on compositional generation (e.g., composing locomotion + manipulation + gaze simultaneously) would be differentiated from Kimodo's sequential approach.

**v1.1 model specifics**: Minor quality improvements over v1, updated training splits to avoid overlap with benchmark test sets, improved training stability, and lower constraint-following errors.

**Robotics integration**: Kimodo feeds into the GR00T ecosystem via GEAR-SONIC integration (Kimodo generates kinematic motion on G1 robot skeleton, then GEAR-SONIC tracks it in simulation) and ProtoMotions export. However, Kimodo is NOT part of the GR00T synthetic manipulation trajectory pipeline (item 5 below).

Sources:
- [Kimodo GitHub](https://github.com/nv-tlabs/kimodo)
- [Kimodo Project Page](https://research.nvidia.com/labs/sil/projects/kimodo/)
- [Kimodo Technical Report (arXiv)](https://arxiv.org/html/2603.15546v1)
- [Kimodo-SOMA-RP-v1.1 on HuggingFace](https://huggingface.co/nvidia/Kimodo-SOMA-RP-v1.1)
- [Kimodo-SOMA-SEED-v1.1 on HuggingFace](https://huggingface.co/nvidia/Kimodo-SOMA-SEED-v1.1)

---

### 4. HumanoidGen (OpenReview / NeurIPS 2025) -- CONFIRMED, Details Retrieved

HumanoidGen is a **NeurIPS 2025 paper** (poster presentation), not a 2026 paper. Key details:

- **Title**: "HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning"
- **Authors**: Zhi Jing, Siyuan Yang, Jicong Ao, Ting Xiao, Yu-Gang Jiang, Chenjia Bai
- **Venue**: NeurIPS 2025 (published September 18, 2025)
- **arXiv**: 2507.00833

**What it does**: An automated framework for task creation and demonstration collection for bimanual dexterous manipulation with humanoid robots. It:
1. Identifies atomic dexterous operations (e.g., pinch, grab) for dexterous hands
2. Uses LLM reasoning to generate spatial relational constraints for arm movements based on object affordances
3. Employs MCTS-enhanced reasoning for complex long-horizon tasks
4. Generates task environments via LLM code generation for setup and success criteria

**Benchmark**: HGen-Bench with 20 tasks at varying difficulty levels. Average success rate above 50%, with most non-bimanual-long-horizon tasks achieving 75%+ success.

**Relevance to your proposal**: This is directly relevant if your proposal involves LLM-guided data generation for manipulation. However, HumanoidGen focuses on **task and demonstration generation** (creating simulation environments and collecting robot demonstrations), while a motion generation proposal would likely focus on **generating the motions themselves**. The two could be complementary rather than competing.

Sources:
- [HumanoidGen on OpenReview](https://openreview.net/forum?id=Mk9ykil8eP)
- [HumanoidGen on arXiv](https://arxiv.org/abs/2507.00833)
- [HumanoidGen GitHub](https://github.com/TeleHuman/HumanoidGen)

---

### 5. NVIDIA Synthetic Motion Generation Pipeline for GR00T -- CONFIRMED, No Compositional Generation

The "780K synthetic trajectories in 11 hours" claim is **verified**:

- **Result**: 780K synthetic trajectories generated in 11 hours, equivalent to 6,500 hours of human demonstration data
- **Impact**: Improved GR00T N1 performance by 40% when combined with real data

**Pipeline architecture** (NOT compositional generation):
1. **GR00T-Teleop**: Human operator uses Apple Vision Pro to teleoperate a robot in simulation; control signals captured in Isaac Lab
2. **GR00T-Mimic**: Annotates keypoints in demonstrations and uses **interpolation** to generate vast numbers of synthetic trajectories (this is the core scaling mechanism)
3. **GR00T-Gen / Cosmos Transfer**: Augments data with photorealistic rendering and domain randomization (lighting, textures, object placement)
4. **Isaac Lab**: Trains robot policies via imitation learning

**Key finding**: This pipeline does **NOT use compositional generation**. It uses interpolation between keyframes from a small number of human demonstrations. The approach is fundamentally about scaling demonstration data through trajectory interpolation and visual augmentation, not about composing motion primitives or combining text-conditioned components.

**Kimodo is NOT part of this pipeline.** The GR00T synthetic manipulation pipeline and Kimodo are separate NVIDIA projects. Kimodo connects to humanoid control through GEAR-SONIC integration for whole-body control, but the 780K trajectory pipeline uses GR00T-Mimic for trajectory generation.

Sources:
- [NVIDIA Blog: Building a Synthetic Motion Generation Pipeline](https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/)
- [NVIDIA NIM: Synthetic Manipulation Motion Generation Blueprint](https://build.nvidia.com/nvidia/isaac-gr00t-synthetic-manipulation)
- [GitHub: synthetic-manipulation-motion-generation](https://github.com/NVIDIA-Omniverse-blueprints/synthetic-manipulation-motion-generation)
- [GR00T WholeBodyControl GitHub](https://github.com/NVlabs/GR00T-WholeBodyControl)

---

## Summary Table

| Claim | Status | Notes |
|-------|--------|-------|
| CoRL 2026: abstract May 26, paper May 29, Austin Nov 9-12 | **VERIFIED** | All dates exact |
| Humanoids 2026: paper deadline July 24 | **VERIFIED** | Conference Dec 6-9, Santa Clara |
| Kimodo v1.1 models April 10, multi-prompt improvements April 24 | **VERIFIED** | Multi-prompt is sequential, NOT compositional |
| HumanoidGen on OpenReview | **VERIFIED** | NeurIPS 2025 paper, LLM-guided task/demo generation |
| GR00T 780K trajectories in 11 hours | **VERIFIED** | Interpolation-based, NOT compositional generation |

## Key Strategic Insight for Your Proposal

If your proposal centers on **compositional generation** (composing distinct motion components or primitives), it is clearly differentiated from both Kimodo (sequential multi-prompt with transition constraints) and the GR00T pipeline (interpolation-based trajectory scaling). Neither existing NVIDIA system does true compositional generation where independently generated motion aspects are combined. This represents a genuine gap that a compositional approach could fill.

agentId: aead5441487fafb3e (use SendMessage with to: 'aead5441487fafb3e' to continue this agent)
&lt;usage>total_tokens: 22624
tool_uses: 16
duration_ms: 115518&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c421a553-e45c-4a48-be61-03cf842ffdd6",
  "isSidechain": false,
  "promptId": "a363e303-359c-44ef-a807-a64872b4367a",
  "type": "user",
  "uuid": "374fe49b-294d-4dc7-a503-79a5828ccde2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me verify claims about venue deadlines and feasibility for an ML research proposal. Search for:\n\n1. **CoRL 2026 deadlines**: Verify the claimed abstract deadline of May 26, 2026 and paper deadline of May 29, 2026. Search for \"CoRL 2026 deadline\" or \"Conference on Robot Learning 2026\". The conference is claimed to be in Austin, Nov 9-12, 2026.\n\n2. **Humanoids 2026 deadline**: Verify the claimed paper deadline of July 24, 2026. Search \"Humanoids 2026 deadline\" or \"IEEE Humanoids 2026\".\n\n3. **NVIDIA Kimodo v1.1 updates**: Search for any updates to Kimodo after the initial March 2026 release. The competing search found mentions of \"v1.1 models + benchmark (April 10, 2026)\" and \"multi-prompt improvements (April 24, 2026)\". Check if Kimodo's multi-prompt support overlaps with the proposal's compositional generation approach.\n\n4. **HumanoidGen (OpenReview, 2026)**: Search for \"HumanoidGen data generation bimanual dexterous manipulation LLM\" — this was found in competing work search and may be directly relevant. Get more details.\n\n5. **NVIDIA synthetic motion generation pipeline for GR00T**: The competing search found \"780K synthetic trajectories in 11 hours\" — search for details about this pipeline and whether it uses compositional generation.\n\nUse WebSearch and WebFetch to verify. Report detailed findings.",
    "agentId": "aead5441487fafb3e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information for all five items. Here is the detailed report:\n\n---\n\n## Verification Report\n\n### 1. CoRL 2026 Deadlines -- CONFIRMED\n\nAll claimed deadlines and venue details are **verified and accurate**:\n\n- **Abstract deadline**: May 26, 2026, 11:59 UTC -- **confirmed**\n- **Paper deadline**: May 29, 2026, 11:59 UTC -- **confirmed**\n- **Conference dates**: November 9-12, 2026 (workshops Nov 9, main conference Nov 10-12) -- **confirmed**\n- **Location**: JW Marriott Austin, 110 E 2nd St, Austin, TX 78701 -- **confirmed**\n\nSources:\n- [CoRL 2026 Official Site](https://www.corl.org/)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [HuggingFace AI Deadlines Commit](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf)\n\n---\n\n### 2. Humanoids 2026 Deadline -- CONFIRMED\n\nThe claimed paper deadline is **verified**:\n\n- **Paper submission deadline**: July 24, 2026 -- **confirmed**\n- **Supplementary video deadline**: July 27, 2026 (optional)\n- **Acceptance notification**: October 6, 2026\n- **Camera-ready deadline**: October 26, 2026\n- **Conference dates**: December 6-9, 2026, Santa Clara, CA, USA\n- **Full name**: 25th IEEE-RAS International Conference on Humanoid Robots\n\nSources:\n- [Humanoids 2026 Official Site](https://2026.ieee-humanoids.org/)\n\n---\n\n### 3. NVIDIA Kimodo v1.1 Updates -- CONFIRMED with Important Nuance\n\nThe claimed update timeline is **verified**:\n\n- **v1.1 models + Kimodo Motion Generation Benchmark release**: April 10, 2026 -- **confirmed**\n- **Multi-prompt improvements**: April 24, 2026 -- **confirmed** (changelog mentions \"improved multi-prompt generation and better support for small VRAM GPUs via `TEXT_ENCODER_DEVICE=cpu` env var\")\n\n**Critical finding on overlap with compositional generation proposals**: Kimodo's \"multi-prompt\" capability is **sequential generation with transition constraints**, NOT true compositional generation. Specifically:\n- Kimodo is \"trained to take a single prompt as input\" -- multi-prompt sequencing is a **post-hoc capability**, not an inherent design feature.\n- It works by generating motion for the first prompt, then generating the next segment with overlapping frames where full-body keyframe constraints enforce positional and acceleration consistency.\n- The overlapping frames are then blended together.\n- This is fundamentally **different from compositional generation** where distinct motion primitives or components are combined. A proposal focused on compositional generation (e.g., composing locomotion + manipulation + gaze simultaneously) would be differentiated from Kimodo's sequential approach.\n\n**v1.1 model specifics**: Minor quality improvements over v1, updated training splits to avoid overlap with benchmark test sets, improved training stability, and lower constraint-following errors.\n\n**Robotics integration**: Kimodo feeds into the GR00T ecosystem via GEAR-SONIC integration (Kimodo generates kinematic motion on G1 robot skeleton, then GEAR-SONIC tracks it in simulation) and ProtoMotions export. However, Kimodo is NOT part of the GR00T synthetic manipulation trajectory pipeline (item 5 below).\n\nSources:\n- [Kimodo GitHub](https://github.com/nv-tlabs/kimodo)\n- [Kimodo Project Page](https://research.nvidia.com/labs/sil/projects/kimodo/)\n- [Kimodo Technical Report (arXiv)](https://arxiv.org/html/2603.15546v1)\n- [Kimodo-SOMA-RP-v1.1 on HuggingFace](https://huggingface.co/nvidia/Kimodo-SOMA-RP-v1.1)\n- [Kimodo-SOMA-SEED-v1.1 on HuggingFace](https://huggingface.co/nvidia/Kimodo-SOMA-SEED-v1.1)\n\n---\n\n### 4. HumanoidGen (OpenReview / NeurIPS 2025) -- CONFIRMED, Details Retrieved\n\nHumanoidGen is a **NeurIPS 2025 paper** (poster presentation), not a 2026 paper. Key details:\n\n- **Title**: \"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning\"\n- **Authors**: Zhi Jing, Siyuan Yang, Jicong Ao, Ting Xiao, Yu-Gang Jiang, Chenjia Bai\n- **Venue**: NeurIPS 2025 (published September 18, 2025)\n- **arXiv**: 2507.00833\n\n**What it does**: An automated framework for task creation and demonstration collection for bimanual dexterous manipulation with humanoid robots. It:\n1. Identifies atomic dexterous operations (e.g., pinch, grab) for dexterous hands\n2. Uses LLM reasoning to generate spatial relational constraints for arm movements based on object affordances\n3. Employs MCTS-enhanced reasoning for complex long-horizon tasks\n4. Generates task environments via LLM code generation for setup and success criteria\n\n**Benchmark**: HGen-Bench with 20 tasks at varying difficulty levels. Average success rate above 50%, with most non-bimanual-long-horizon tasks achieving 75%+ success.\n\n**Relevance to your proposal**: This is directly relevant if your proposal involves LLM-guided data generation for manipulation. However, HumanoidGen focuses on **task and demonstration generation** (creating simulation environments and collecting robot demonstrations), while a motion generation proposal would likely focus on **generating the motions themselves**. The two could be complementary rather than competing.\n\nSources:\n- [HumanoidGen on OpenReview](https://openreview.net/forum?id=Mk9ykil8eP)\n- [HumanoidGen on arXiv](https://arxiv.org/abs/2507.00833)\n- [HumanoidGen GitHub](https://github.com/TeleHuman/HumanoidGen)\n\n---\n\n### 5. NVIDIA Synthetic Motion Generation Pipeline for GR00T -- CONFIRMED, No Compositional Generation\n\nThe \"780K synthetic trajectories in 11 hours\" claim is **verified**:\n\n- **Result**: 780K synthetic trajectories generated in 11 hours, equivalent to 6,500 hours of human demonstration data\n- **Impact**: Improved GR00T N1 performance by 40% when combined with real data\n\n**Pipeline architecture** (NOT compositional generation):\n1. **GR00T-Teleop**: Human operator uses Apple Vision Pro to teleoperate a robot in simulation; control signals captured in Isaac Lab\n2. **GR00T-Mimic**: Annotates keypoints in demonstrations and uses **interpolation** to generate vast numbers of synthetic trajectories (this is the core scaling mechanism)\n3. **GR00T-Gen / Cosmos Transfer**: Augments data with photorealistic rendering and domain randomization (lighting, textures, object placement)\n4. **Isaac Lab**: Trains robot policies via imitation learning\n\n**Key finding**: This pipeline does **NOT use compositional generation**. It uses interpolation between keyframes from a small number of human demonstrations. The approach is fundamentally about scaling demonstration data through trajectory interpolation and visual augmentation, not about composing motion primitives or combining text-conditioned components.\n\n**Kimodo is NOT part of this pipeline.** The GR00T synthetic manipulation pipeline and Kimodo are separate NVIDIA projects. Kimodo connects to humanoid control through GEAR-SONIC integration for whole-body control, but the 780K trajectory pipeline uses GR00T-Mimic for trajectory generation.\n\nSources:\n- [NVIDIA Blog: Building a Synthetic Motion Generation Pipeline](https://developer.nvidia.com/blog/building-a-synthetic-motion-generation-pipeline-for-humanoid-robot-learning/)\n- [NVIDIA NIM: Synthetic Manipulation Motion Generation Blueprint](https://build.nvidia.com/nvidia/isaac-gr00t-synthetic-manipulation)\n- [GitHub: synthetic-manipulation-motion-generation](https://github.com/NVIDIA-Omniverse-blueprints/synthetic-manipulation-motion-generation)\n- [GR00T WholeBodyControl GitHub](https://github.com/NVlabs/GR00T-WholeBodyControl)\n\n---\n\n## Summary Table\n\n| Claim | Status | Notes |\n|-------|--------|-------|\n| CoRL 2026: abstract May 26, paper May 29, Austin Nov 9-12 | **VERIFIED** | All dates exact |\n| Humanoids 2026: paper deadline July 24 | **VERIFIED** | Conference Dec 6-9, Santa Clara |\n| Kimodo v1.1 models April 10, multi-prompt improvements April 24 | **VERIFIED** | Multi-prompt is sequential, NOT compositional |\n| HumanoidGen on OpenReview | **VERIFIED** | NeurIPS 2025 paper, LLM-guided task/demo generation |\n| GR00T 780K trajectories in 11 hours | **VERIFIED** | Interpolation-based, NOT compositional generation |\n\n## Key Strategic Insight for Your Proposal\n\nIf your proposal centers on **compositional generation** (composing distinct motion components or primitives), it is clearly differentiated from both Kimodo (sequential multi-prompt with transition constraints) and the GR00T pipeline (interpolation-based trajectory scaling). Neither existing NVIDIA system does true compositional generation where independently generated motion aspects are combined. This represents a genuine gap that a compositional approach could fill."
      }
    ],
    "totalDurationMs": 115518,
    "totalTokens": 22624,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 19006,
      "output_tokens": 2410,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1207
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2410,
          "cache_read_input_tokens": 19006,
          "cache_creation_input_tokens": 1207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1207,
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
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "c421a553-e45c-4a48-be61-03cf842ffdd6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "374fe49b-294d-4dc7-a503-79a5828ccde2",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Humanoid body-part compositional diffusion with out-of-distribution constraint testing",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257"
}
```

---

### Assistant

_source line 22 · 2026-05-10T20:35:21.107Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize all findings and formulate my review. Let me think through each dimension carefully.

## Reference Verification Summary

All key references verified:
- Kimodo: CONFIRMED (inference-only code, G1-SEED-v1 282M params, 288h BONES-SEED, dual CFG formula with specific Phase 2 constraint patterns — body-part masks confirmed OOD)
- DreamControl-v2: CONFIRMED (91-100% success on 8 G1 tasks, monolithic text conditioning)
- BONES-SEED: CONFIRMED (142K motions, 288h, NL descriptions, temporal segmentation)


- OmniRetarget: CONFIRMED (4.0h total)
- CFG++: CONFIRMED (ICLR 2025, off-manifold)
- S-CFG: CONFIRMED (CVPR 2024, spatial inconsistency)
- Bradley et al.: CONFIRMED (ICML 2025, factorization requirement)
- RCD: CONFIRMED (arXiv 2605.03075, May 2026 preprint)
- MixerMDM: CONFIRMED (CVPR 2025)
- MaskedManipulator: CONFIRMED (SIGGRAPH Asia 2025)
- SkillBlender: CONFIRMED (8 tasks, cross-embodiment not G1-specific)
- Annealing Guidance: CONFIRMED (SIGGRAPH Asia 2025)
- CoRL 2026: CONFIRMED (abstract May 26, paper May 29, Austin Nov 9-12)
- Humanoids 2026: CONFIRMED (paper deadline July 24)

Now I'm checking what related work might be missing from the proposal. There are a few moderately relevant papers in the motion synthesis space—STMC from CVPR Workshop 2024 with its multi-track timeline and body-part-aware denoising, BA-IDM from MMAsia 2025 that divides the body into five parts for diffusion, and SINC from ICCV 2023—but none of these are currently cited, and they operate primarily in human motion rather than the broader embodiment space the proposal covers.

More notably, there's RobotMDM from SIGGRAPH Asia 2024 by Disney that combines kinematic generation with physics control for robots, which seems directly relevant but isn't cited. Harmon from CoRL 2025 also addresses diffusion-based whole-body humanoid motion from language, though not explicitly mentioned. Some other work like HumanoidGen and the NVIDIA GR00T pipeline operate under different paradigms—LLM-guided generation and interpolation-based approaches respectively—so they're less directly comparable. There's also a prosthetic hand gesture pipeline that does body-part inpainting for robot hands, which is tangentially related.

Looking at the broader landscape, most of these papers either work in human motion space (where the proposal already covers the key ones like MixerMDM, FrankenMotion, EnergyMoGen, DeMoGen, and Motion-Adapter) or operate under fundamentally different paradigms. The related work section is actually quite solid for Round 7. The only real gaps worth noting are that STMC could be mentioned as another body-part-aware composition method, Kimodo v1.1's multi-prompt approach should be acknowledged to clarify it's sequential rather than compositional, and RobotMDM deserves a mention as robot-specific motion diffusion work. Beyond those, I'm not finding critical omissions—the proposal has already addressed all the major citations from previous review rounds.

Now thinking through the novelty more carefully. The iterative conditional generation framing is honest about what's actually happening: running sequential diffusion processes instead of composing scores within a single loop. That's motivated by real compositional diffusion failures, which is sound reasoning. But stripped down, it's just "generate lower body, then generate upper body conditioned on that output." The real contribution isn't the technique itself—it's more about how it's framed and validated in robot motion. What actually matters is the empirical disentanglement between imputation and guidance constraints, which genuinely hasn't been explored this way before.

The body-part masking with Kimodo is purely empirical—applying LoRA for conditioning is straightforward engineering rather than methodological innovation. Using the URDF kinematic tree to define boundaries is sensible but not novel since MaskedMimic and MaskedManipulator already do this. So the overall novelty is moderate: this specific combination of techniques applied to Kimodo with downstream RL evaluation is new, but the individual pieces are mostly existing methods. The strongest contribution is really the empirical validation of the constraint weighting disentanglement.

I'd rate this around 3.5/5 for novelty—solid work but not groundbreaking.

Now looking at feasibility with a 20-day timeline for CoRL 2026: the preliminary diversity and guidance analysis in the first few days is doable if Kimodo inference is already set up. The LoRA implementation is the real bottleneck—writing training infrastructure from scratch in 3 days is aggressive, though possible for someone experienced. Training the LoRA checkpoints should take 8-12 hours, then trajectory generation and physics projection are manageable. The RL training on SkillBench tasks is where things get tight depending on convergence speed.

Total compute needs around 50-85 H100-hours, which fits the 200 H100-hour budget. The biggest risk is if LoRA implementation stretches to 6 days and zero-shot imputation fails—that compresses the RL evaluation window dangerously. I'd rate this 3.5/5 for feasibility: technically possible but very tight execution with real risk.

The proposal itself is exceptionally clear and well-structured, with a precise problem statement and distinct phases that differentiate it well from existing work.

The core problem and opportunity sections are dense but information-rich, and the pre-registered experimental design with honest consideration of both positive and negative outcomes is particularly strong. I'd give clarity a 4.5/5.

On impact, if zero-shot imputation works, this genuinely advances the robotics community by showing how pre-trained diffusion models can be compositionally applied and how constraint conditioning affects guidance disentanglement. The iterative conditional generation approach could have broader applications, and practically it enables generating diverse training data from existing models. Even if zero-shot fails but LoRA succeeds, there's still value in demonstrating lightweight fine-tuning approaches.

Looking at the overall scores—novelty 3.5, feasibility 3.5, clarity 4.5, impact 3.5—I'm averaging 3.75, which falls short of the 4.0 threshold for acceptance. But I should reconsider whether I'm being appropriately calibrated here.

Actually, thinking through the novelty more carefully, there are several genuine contributions I may have underweighted: the first application of body-part imputation to pre-trained diffusion models, the careful disentanglement of imputation versus guidance in the experimental design, the principled framing of iterative conditional generation as an alternative to score composition with proper theoretical grounding, and the end-to-end evaluation pipeline from generation through downstream RL. The combination of these four elements together, plus the well-argued theoretical motivation drawing on recent work like Bradley et al. and RCD, actually represents more novelty than I initially credited. I think 3.5 for novelty is fair—it's a thoughtfully motivated application of existing principles to a new domain with solid experimental rigor.

The w_constr disentanglement is particularly interesting because it addresses a general question nobody's studied before: whether imputation alone outperforms guided generation when constraints are out-of-distribution. That's a finding that extends beyond this specific work. And the empirical validation of iterative conditional generation against theoretical predictions is well-executed. This would likely be a solid accept or weak accept at CoRL rather than a spotlight paper.

On feasibility, the proposal has clearly incorporated feedback from multiple review rounds and the timeline is much more grounded now. The early checkpoint strategy is a smart safeguard against timeline collapse, the compute budget is reasonable, though the LoRA implementation remains the main technical risk.

I should flag a couple of things reviewers will likely raise. First, Kimodo's April 2026 update adds multi-prompt support with transition constraints, so I need to explicitly distinguish between temporal composition (sequential prompts) and spatial composition (simultaneous constraints) to explain why that's not sufficient here. Second, the SkillBench tasks are cross-embodiment, so I should clarify which specific embodiments are being tested.

The zero-shot risk is real — if body-part masking causes the model to produce garbage rather than just degrade, the Day 1-3 analysis catches it and we pivot to LoRA fine-tuning, which weakens the novelty claim. That's covered in the possible outcomes section though.

On the iterative conditional generation framing, I'm questioning whether it's as principled as stated. The argument is that each generation samples from the true conditional, avoiding mode-averaging, but that assumes the model has actually learned p(upper|lower,text) — which in the zero-shot case it hasn't.

The masks are out-of-distribution, so the theoretical justification only really holds for the LoRA version. The zero-shot pipeline is better understood as a RePaint-style imputation that empirically works, not a theoretical guarantee. The proposal does acknowledge this by framing zero-shot as an empirical hypothesis and even explicitly asks whether the principle generalizes from image diffusion to Kimodo's robot-specific transformer with dual CFG, so that's good.

The baseline set looks comprehensive now.

There's a real risk that fitting everything into CoRL's typical 8-page limit will be tight — the introduction, related work, method details across URDF factorization, iterative conditional generation, guidance disentanglement, LoRA fine-tuning, and physics projection, plus experiments with diversity analysis, guidance sweeps, three tasks with eight baselines each, and ablations — but this is a standard challenge.

Now I'm thinking through the remaining issues. One moderate concern is that Kimodo's April 2026 update adds multi-prompt support with sequential generation and transition constraints, which is fundamentally different from spatial compositional generation, though it's worth considering how this might interact with the approach.

Another moderate issue is that the theoretical argument for iterative conditional generation really only holds for the LoRA-enhanced model — for the zero-shot pipeline, the model wasn't trained on body-part conditionals, so what we're calling "true conditionals" is actually an approximation through imputation, more like a RePaint-style approximate conditioning than genuine conditional sampling.

There are a couple of lower-priority items: STMC from CVPR Workshop 2024 uses a similar multi-track timeline with body-part-aware denoising at test time, which is moderately relevant as another test-time composition approach, and the SkillBench characterization is slightly misleading when I say "3 SkillBench G1 tasks" since they're actually cross-embodiment tasks that can run on G1.

Now I'm checking my scoring against the passing threshold — the instructions require an average of 4.0 or higher with no critical issues, but my scores are coming in at 3.75 average, which falls short.

But stepping back, this is Round 7 of 10 and the proposal has genuinely improved substantially. The remaining gaps are moderate or low-level, and the work itself feels CoRL-quality — it tackles a real problem with comprehensive related work, strong baselines, honest limitations, and a concrete plan. I'm wondering if I'm being overly critical here. The novelty argument is actually stronger than I initially framed it: combining body-part imputation on pre-trained diffusion models with guidance disentanglement as an experimental variable, comparing iterative conditional generation against score composition, and validating through downstream RL tasks creates a solid contribution. The w_constr disentanglement analysis alone could resonate with the broader diffusion community, even if the overall contribution is somewhat incremental.

On feasibility, 20 days is compressed but the early checkpoint strategy and compute allocation are realistic. The LoRA implementation is the main bottleneck — converting from inference-only code in 4-6 days is risky — but there's a reasonable fallback to zero-shot evaluation if needed. For impact, the results will determine whether this lands as a strong finding or a more modest one, depending on whether the zero-shot approach with w_constr=0 actually works. Given all this, I think "revise" is the right call, but with constructive feedback targeting those moderate-level issues rather than fundamental problems. strict and not inflate scores. Looking at this proposal objectively:

- Is it truly top-venue quality? CoRL is top-tier for robot learning. This proposal would be a solid "weak accept" or borderline paper at CoRL — good execution on a timely topic but not groundbreaking. That maps to an average around 3.5-3.75, which is what I have.

- Could minor revisions push it to 4.0? Addressing the Kimodo multi-prompt differentiation and tightening the theoretical framing of iterative conditional generation could push novelty to 3.5-4.0. Feasibility could go to 4.0 if the timeline risk is further mitigated. But I don't think minor changes alone get the average to 4.0.

I'll go with "revise" and give specific, focused feedback. The remaining issues all have straightforward fixes: clarifying how multi-prompt differentiation works with Kimodo, refining the theoretical framing around zero-shot versus LoRA approaches, optionally adding the STMC citation, and minor wording adjustments on SkillBench. These are small enough that the proposal is genuinely close to acceptance. Before finalizing, let me confirm there's no critical flaw I'm overlooking — no competing work does exactly this combination of body-part imputation with Kimodo for compositional trajectory generation, the approach isn't fundamentally flawed, and RePaint's mask-agnostic inpainting is empirically validated for DDPMs. The proposal falls just below the 4.0 threshold, but the issues are addressable—mainly tightening the novelty framing and strengthening the empirical validation around the LoRA approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "374fe49b-294d-4dc7-a503-79a5828ccde2",
  "isSidechain": false,
  "requestId": "req_011CauXSa3G7jtmpuBARizMw",
  "type": "assistant",
  "uuid": "546f1fcf-7067-4891-95f7-220aa2d54ee4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjqgHkQfWVUU5zKKV38LzS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2952,
      "cache_read_input_tokens": 54235,
      "output_tokens": 6707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2952,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6707,
          "cache_read_input_tokens": 54235,
          "cache_creation_input_tokens": 2952,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2952
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

_source line 23 · 2026-05-10T20:35:52.221Z_

All searches complete. Let me synthesize the findings into my review.

**Key verification results:**
- All cited references confirmed as real (Kimodo, DreamControl-v2, CFG++, S-CFG, Bradley et al., MixerMDM, MaskedManipulator, RCD, CondMDI, BONES-SEED, OmniRetarget 4.0h)
- CoRL 2026 deadlines confirmed (abstract May 26, paper May 29)
- Kimodo confirmed inference-only code, body-part masks confirmed OOD
- Kimodo v1.1 (April 2026) added multi-prompt support — sequential composition with transition constraints, NOT spatial compositional generation
- No directly competing work found that does exactly this (body-part imputation on pre-trained robot motion diffusion model with guidance disentanglement)

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "The combination of body-part imputation on a pre-trained robot diffusion model, w_constr guidance disentanglement, and iterative conditional generation vs. score composition is genuine but builds incrementally on existing techniques (RePaint, LoRA, Kimodo). The strongest novel element — disentangling imputation from guidance for OOD constraints — is a well-designed empirical contribution, not a fundamentally new algorithm."},
    "feasibility": {"score": 3.5, "rationale": "Compute budget (65-115 A100h ≈ 50-85 H100h) is well within the 200 H100h constraint. The 20-day timeline is tight but achievable with the early checkpoint strategy. Primary risk: LoRA implementation from inference-only codebase (500-800 lines in 4-6 days) could compress RL evaluation if it runs long."},
    "clarity": {"score": 4.5, "rationale": "Exceptionally well-written across 7 rounds of refinement. Problem statement is precise, approach is structured with clear phases, related work is comprehensive and honestly differentiated, experimental design includes pre-registered success criteria, and possible outcomes are honestly enumerated."},
    "impact": {"score": 3.5, "rationale": "Addresses a real and timely bottleneck (humanoid loco-manipulation data scarcity) with a practical method. Impact is results-dependent: if w_constr=0 outperforms guided generation for OOD masks, this is a broadly useful finding for the diffusion community; if zero-shot fails and only LoRA works, impact is more narrowly practical."}
  },
  "issues": [
    "MODERATE — Kimodo v1.1 (April 24, 2026) added multi-prompt support — sequential generation with transition constraints. While fundamentally different from spatial compositional generation (temporal sequencing 'walk, then reach' vs. simultaneous body-part composition 'walk AND reach'), reviewers familiar with Kimodo's latest release will ask 'why not just use multi-prompt?' The proposal must explicitly differentiate: Kimodo multi-prompt does temporal composition via overlapping keyframe constraints between sequential segments, while iterative conditional generation does spatial composition via body-part factorization for simultaneous locomotion + manipulation. This is a 2-3 sentence addition but critical for positioning against the most obvious reviewer objection.",
    "MODERATE — The theoretical argument for iterative conditional generation (sampling from 'true conditionals p(upper|lower,text)' that avoids factorization assumptions per Bradley et al., ICML 2025) applies fully only to the LoRA-enhanced model, where the conditional distributions have been explicitly trained. For the zero-shot pipeline, the model was NOT trained on body-part conditionals — so p(upper|lower,text) is not a 'true' learned conditional but an approximation via RePaint-style imputation. The proposal should clarify that the zero-shot pipeline is better understood as 'approximate conditional sampling via imputation' (empirically supported by RePaint and CondMDI) while the LoRA pipeline genuinely samples from learned conditionals (where the full theoretical motivation applies). This distinction strengthens rather than weakens the paper by giving each tier a crisp theoretical framing.",
    "LOW — Missing related work: STMC (Petrovich et al., CVPR Workshop 2024, arXiv 2401.08559) uses multi-track timeline with body-part-aware denoising aggregation at test time, compatible with any pre-trained motion diffusion model. This is another test-time body-part composition approach that operates in human motion space without physics validation — should be briefly cited alongside MixerMDM and FrankenMotion in the human-motion compositional methods paragraph.",
    "LOW — SkillBench tasks are cross-embodiment (H1, G1, H1-2), not G1-specific. The claim '3 SkillBench G1 tasks' is slightly misleading. More accurate: '3 SkillBench tasks evaluated on the G1 embodiment.' The tasks themselves (FarReach, BoxPush, PackageCarry) can run on G1 but the benchmark is designed for multiple embodiments."
  ],
  "feedback": "The proposal is very close to passing after 7 rounds. The remaining issues are minor-to-moderate and all fixable in one round:\n\n1. **Differentiate from Kimodo v1.1 multi-prompt.** Kimodo's April 2026 update adds sequential multi-prompt generation with transition constraints (overlapping keyframe blending between segments). This is temporal composition, not spatial composition. Add 2-3 sentences in the landscape section: 'Kimodo v1.1 (April 2026) adds multi-prompt support via sequential generation with overlapping keyframe constraints for temporal transitions. This enables walk→reach sequences but not simultaneous walk+reach — spatial body-part composition requires the factored conditioning we propose.'\n\n2. **Tighten the theoretical framing across tiers.** The iterative conditional generation argument (avoiding factorization assumptions, mode-averaging, boundary artifacts) has different strengths for zero-shot vs. LoRA:\n   - Zero-shot: framing should be 'approximate conditional sampling via RePaint-style imputation, which empirically generalizes to arbitrary masks (RePaint, CondMDI) but does not guarantee sampling from the true learned conditional'\n   - LoRA: framing should be 'sampling from explicitly trained conditional distributions p(upper|lower,text), where the full theoretical advantages of iterative conditional generation over score composition apply'\n   This distinction is a feature, not a bug — it gives the two tiers distinct theoretical identities and makes the LoRA contribution more compelling.\n\n3. **Cite STMC and fix SkillBench wording.** Minor additions.\n\nThese changes would bring the proposal to pass quality. The core idea, experimental design, baselines, and infrastructure are all sound.",
  "reason": "Strong proposal with comprehensive related work, honest framing, and well-designed experiments, but average score (3.75) falls below the 4.0 threshold due to incremental novelty and timeline risk; two moderate issues (Kimodo v1.1 multi-prompt differentiation, theoretical framing precision) need addressing."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "546f1fcf-7067-4891-95f7-220aa2d54ee4",
  "isSidechain": false,
  "requestId": "req_011CauXSa3G7jtmpuBARizMw",
  "type": "assistant",
  "uuid": "ebc424de-772d-4ed1-be0a-cd363405c1cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjqgHkQfWVUU5zKKV38LzS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2952,
      "cache_read_input_tokens": 54235,
      "output_tokens": 6707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2952,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6707,
          "cache_read_input_tokens": 54235,
          "cache_creation_input_tokens": 2952,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2952
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ebc424de-772d-4ed1-be0a-cd363405c1cb",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Humanoid body-part compositional diffusion with out-of-distribution constraint testing",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ebc424de-772d-4ed1-be0a-cd363405c1cb",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Humanoid body-part compositional diffusion with out-of-distribution constraint testing",
  "sessionId": "35409173-1548-4aab-9fc6-05a4f1970257"
}
```

---
