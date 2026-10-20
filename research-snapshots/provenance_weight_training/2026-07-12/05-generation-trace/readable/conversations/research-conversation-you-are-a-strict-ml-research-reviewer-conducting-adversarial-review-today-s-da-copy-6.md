# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/55c7714a-4eab-4906-93b8-ec7a5460641c.jsonl`
- **Structured JSON:** [`acd577457229a29d0c96.json`](../../sessions/ac/acd577457229a29d0c96.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T11:51:09.777Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T11:51:09.777Z",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: Generative models specifically targeting HUMANOID robot training data — addressing the high-DoF, whole-body, loco-manipulation data scarcity that bottlenecks humanoid VLA / WM training. SCOPE LIMITED TO TWO CONTRIBUTION TYPES:\n  (a) Generation ALGORITHMS — e.g., video diffusion conditioned on humanoid action streams, action-conditioned generative models, latent humanoid trajectory generators, physics-aware whole-body video generation.\n  (b) Procedural data-generation PIPELINES — e.g., MimicGen-style automated demo multiplication for humanoids, procedural whole-body task/scene generation, automated quality filtering pipelines for synthetic humanoid trajectories.\n\nOUT OF SCOPE: action retargeting innovations (human-video → humanoid-action retargeting). Treat existing retargeters (HumanPlus, OmniH2O) as black-box upstream tools if needed; do NOT propose new retargeting methods.\n\nRecent landscape (do not duplicate): NVIDIA GR00T-Dreams, DexMimicGen, MimicGen extensions for humanoid, Helix self-supervised humanoid pipelines, Cosmos for synthetic humanoid video. Humanoid data scarcity is the #1 bottleneck cited in 2026 humanoid papers — high impact area.\n\nContribution type: METHOD ONLY. New generation algorithm OR new procedural pipeline. Not a new released humanoid dataset alone.\n\nSIM-ONLY MITIGATION: Validate generated data by training a downstream humanoid policy/VLA in sim and comparing against models trained on baseline data. Frame contribution as method, not dataset.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Strategies: (a) fine-tune existing video diffusion (CogVideoX, OpenSora, Cosmos) with humanoid-action conditioning, (b) procedural pipeline that requires negligible training compute, (c) small efficient humanoid-specific generator that beats general baselines.\n2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos, Isaac Lab humanoid suite (G1, H1), MimicGen, RoboCasa with humanoid embodiments if available.\n3. Eval: train humanoid policy/VLA on generated vs baseline data. Test on Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench. Report success rate + data efficiency curves.\n\nLook for: physics-aware whole-body video generation with kinematic consistency, action-conditioned generators that exploit humanoid kinematic structure, procedural pipelines that produce diverse loco-manipulation (not just static manipulation) data, automatic quality filtering for synthetic humanoid trajectories. Avoid: any retargeting-based contribution, arm-only generation rebadged as humanoid, naive fine-tuning of video diffusion on humanoid clips without method.\n\nTag: direction=humanoid_data_gen, contribution_type=method. target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 2/10)\n{\n  \"title\": \"URDF-DiT: ControlNet-Style Full-Body Kinematic Conditioning for Humanoid Video Diffusion and Sim-Bootstrap IDM Policy Extraction\",\n  \"core_problem\": \"How can a video diffusion model be conditioned in-loop on a full-body humanoid robot's URDF kinematic structure — enforcing 29+ DoF whole-body consistency during generation rather than correcting artifacts post-hoc — to produce kinematically coherent whole-body contact interaction videos from which a sim-trained inverse dynamics model can extract directly usable joint velocity commands for policy training, specifically for the embodiment scope (full-body humanoid) and task category (whole-body contact interaction) that the concurrent arm-only EA-WM system (arXiv:2605.06192) leaves unaddressed?\",\n  \"opportunity\": \"GR00T-Dreams/DreamGen (2025) validated the video-diffusion → IDM pipeline for tabletop manipulation. Dream2Act (March 2026) extended to whole-body contact interaction on the G1 (ball kicking, sofa sitting, bag punching, box hugging) using Seedance 2.0 with post-hoc URDF-IK recovery — achieving only 37.5% overall success, with failures attributed to kinematic artifacts from post-hoc correction. EA-WM (arXiv:2605.06192, May 7 2026) validates that in-loop KVAF injection into Wan 2.2 attention effectively enforces kinematic consistency — but is scoped exclusively to bimanual arm manipulation (~14 DoF), uses bidirectional dual-stream fusion requiring joint fine-tuning of both the video and kinematic branches, evaluates on WorldArena/RoboTwin 2.0 tabletop tasks, and produces no policy training pipeline (action recovery detection rate ~0.45). The specific gap URDF-DiT fills is precisely defined: in-loop URDF kinematic conditioning for full-body humanoid whole-body contact interaction (29+ DoF G1), using a ControlNet-style frozen-backbone design that is more compute-efficient than EA-WM's joint fine-tuning, and an explicit sim-IDM pipeline converting generated videos into policy training trajectories — all three dimensions EA-WM leaves unaddressed. Training a ControlNet-style conditioning module on top of Wan 2.2 (backbone frozen) is feasible within ~35 H100-hours; a sim-bootstrapped IDM for the G1 in Isaac Lab adds ~25 H100-hours, keeping the full pipeline within a ≤200 H100-hour budget.\",\n  \"landscape\": \"GR00T-Dreams/DreamGen (arXiv 2025): fine-tunes Cosmos-Predict2 with language conditioning; extracts pseudo-actions via IDM or latent action model. No URDF kinematic constraint. Tabletop manipulation only. Dream2Act (arXiv:2603.19709, March 2026): generates morphology-consistent G1 robot videos using Seedance 2.0, constrains kinematics post-hoc via URDF-IK — achieves 37.5% overall task success across four whole-body contact interaction benchmarks (ball kick, sofa sit, bag punch, box hug). EA-WM (arXiv:2605.06192, May 2026): the most direct concurrent work — injects Kinematic-Visual Action Fields (KVAF: Gaussian heatmaps at projected end-effector locations) via event-aware bidirectional dual-stream fusion into Wan 2.2; targets bimanual arm manipulation (~14 DoF) only; requires joint fine-tuning of both video and kinematic streams; evaluates on WorldArena/RoboTwin 2.0 tabletop manipulation tasks; provides no policy training output (action recovery detection rate ~0.45, explicitly described as heuristic recovery rather than an IDM). Kinema4D (arXiv March 2026, NTU): URDF-driven FK produces 4D pointmap conditioning for environmental simulation synthesis — targets scene realism, not policy-data generation or video diffusion attention-layer kinematic injection. Controllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026): cascaded text-to-2D-skeleton → skeleton-to-video pipeline validates per-frame 2D pose-sequence conditioning in video diffusion; targets human motion synthesis, not robot URDF kinematics or policy extraction — the closest analogue to URDF-DiT's conditioning mechanism in the video generation literature. X-Humanoid (arXiv Dec 2025): replaces human with humanoid in video via Wan 2.2, no URDF constraint injection. MITTY (arXiv 2025): human-to-robot video diffusion without kinematic enforcement. G-DReaM (arXiv 2025): graph-conditioned diffusion for cross-embodiment motion retargeting; operates on motion sequences, not RGB video. No published system combines in-loop URDF kinematic conditioning for full-body humanoid whole-body contact interaction (29+ DoF) with an explicit sim-IDM → policy training trajectory pipeline.\",\n  \"approach\": \"URDF-DiT uses a ControlNet-style conditioning module — Wan 2.2 backbone weights fully frozen; only the FK-heatmap encoder and zero-conv injection layers are trained — that encodes per-frame G1 URDF forward-kinematics outputs (all 29 DoF, projected to the camera plane via differentiable FK) as structured Gaussian joint-position heatmaps and injects them into the cross-attention layers of the Wan 2.2 DiT. Unlike EA-WM's bidirectional dual-stream fusion (which requires joint fine-tuning of both video and kinematic branches, roughly doubling trainable parameters and training compute versus a frozen-backbone approach), URDF-DiT's ControlNet-style design concentrates all learning in the conditioning module, reducing GPU hours by ~40% at matched video quality — directly enabling the full pipeline within ≤200 H100-hours. Full-body G1 scope (29 DoF: pelvis, legs, torso, arms, hands) is the critical embodiment extension over EA-WM's arm-only target: coordinating kinematic heatmaps across all limbs simultaneously is the conditioning challenge for whole-body contact interaction that EA-WM's end-effector-only KVAF representation does not address. Joint-angle sequences are sampled from an Isaac Lab G1 motion library covering locomotion primitives and upper-body reach plans, projected onto the camera plane, and encoded as per-frame kinematic tokens concatenated with temporal attention keys inside each DiT block. The sim→video IDM domain gap — the central technical risk — is mitigated via two mechanisms: (a) domain-randomized Isaac Lab rendering during IDM training, sampling lighting, camera noise, and surface material variation to statistically overlap with Wan 2.2's visual output distribution; and (b) a per-frame FK residual consistency loss added to URDF-DiT's generation objective, penalizing deviations between generated joint positions and URDF FK predictions, pulling generated frames toward sim-renderable kinematics before IDM application. The sim-bootstrapped IDM is trained on (frame_t, frame_{t+k}, joint-velocity) tuples from G1 Isaac Lab rollouts under domain-randomized conditions, then applied zero-shot to URDF-DiT-generated videos to extract joint velocity commands for policy training without any real-robot labeling. The pipeline is evaluated on three of Dream2Act's four whole-body contact interaction benchmarks — multi-position ball kicking, bag punching, box hugging (sofa sitting excluded as the least kinematically rich of the four) — using Dream2Act's 37.5% overall success as the primary baseline. Two core ablations: (1) in-loop URDF-DiT conditioning vs. post-hoc URDF-IK at matched video budgets, isolating kinematic artifact reduction as the performance driver; (2) ControlNet-style frozen-backbone vs. bidirectional fusion at matched compute budgets, verifying the efficiency–performance tradeoff relative to EA-WM's architecture.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~130h H100\",\n      \"gpu_utilization\": \"HIGH idle rate (~40-50% effective utilization) — sequential experiment launches and human debugging keep GPUs idle between runs; ControlNet module training and IDM training are the two dense compute bursts\",\n      \"timeline\": \"4-6 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$416 (130h × $3.20/hr)\",\n      \"breakdown\": \"ControlNet module training (frozen Wan 2.2 backbone): ~35h; IDM training (Isaac Lab G1 rollouts + domain-randomized rendering): ~25h; Video generation + evaluation on 3 benchmarks: ~35h; Ablations (in-loop vs. post-hoc, ControlNet-style vs. bidirectional fusion): ~25h; Data prep and miscellaneous: ~10h\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~160h H100\",\n      \"gpu_utilization\": \"Moderate (~60-65% effective utilization) — agent queues ablation variants back-to-back without waiting for human; approval gates add short pauses only at key architectural decisions (FK residual loss weight, injection layer depth, IDM backbone choice)\",\n      \"timeline\": \"5-8 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in for experiment approval and direction adjustment\",\n      \"claude_api_cost\": \"~$150-300 (Opus, ~1,500-2,000 conversation turns covering experiment design, code review, and result analysis)\",\n      \"estimated_gpu_cost\": \"~$512 (160h × $3.20/hr)\",\n      \"risk_note\": \"Key risk: if domain-randomized rendering and FK residual loss are insufficient for IDM sim→video transfer, human oversight can detect this at the 2-week checkpoint and redirect toward a lightweight IDM adapter fine-tuned on a small set of URDF-DiT-generated frames matched to sim rollouts via kinematic alignment, before the remaining GPU budget is spent\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~200h H100 (covers ControlNet injection depth sweeps, FK heatmap resolution variants, IDM backbone comparisons, FK residual loss weight ablation, and extended evaluation on all 4 Dream2Act benchmarks including sofa sitting)\",\n      \"gpu_utilization\": \"Near-zero idle (~88-92% effective utilization) — agent immediately queues the next experiment upon completion and runs non-dependent trials (IDM training vs. video generation) in parallel across GPUs\",\n      \"timeline\": \"1-2 weeks with 8+ H100s; 3-4 weeks on 4 GPUs\",\n      \"team\": \"0 (initial setup ~4h: configure Isaac Lab motion library, domain-randomized rendering pipeline, URDF-DiT scaffold, and automated evaluation harness)\",\n      \"claude_api_cost\": \"~$400-700 (Opus, ~4,000-7,000 turns for experiment proposal, code generation, failure diagnosis, and iterative result interpretation)\",\n      \"estimated_gpu_cost\": \"~$640 (200h × $3.20/hr)\",\n      \"speed_bottleneck\": \"GPU cluster size is the primary bottleneck — with 8 H100s running in parallel, wall-clock time compresses to ~1 week; API quota becomes secondary if the agent spawns many concurrent evaluation sub-agents\",\n      \"risk_note\": \"Automated evaluation harness must include per-frame kinematic consistency checks (FK residual, joint-limit violation rate, temporal flicker score) alongside task success to prevent silent metric gaming; qualitative failure modes in generated joint sequences are not captured by task-success metrics alone\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (expected submission deadline ~October 2026; official announcement pending at iclr.cc)\",\n    \"CoRL 2027 (fallback)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"DreamGen: Unlocking Generalization in Robot Learning through Video World Models (arXiv 2025)\",\n    \"Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis / Dream2Act (arXiv:2603.19709, March 2026)\",\n    \"EA-WM: Embodiment-Aware World Model via Kinematic-Visual Action Fields for Bimanual Manipulation (arXiv:2605.06192, May 2026) — primary concurrent work; differentiators: arm-only vs. full-body, bidirectional fusion vs. ControlNet-style, no policy training vs. explicit IDM pipeline\",\n    \"Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation (arXiv March 2026)\",\n    \"Controllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026) — validates per-frame 2D skeleton-sequence conditioning in video diffusion; closest video-generation analogue to URDF-DiT's conditioning mechanism\",\n    \"X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (arXiv Dec 2025)\",\n    \"Mitty: Diffusion-based Human-to-Robot Video Generation (arXiv 2025)\",\n    \"Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models (arXiv 2025)\",\n    \"G-DReaM: Graph-conditioned Diffusion Retargeting across Multiple Embodiments (arXiv 2025)\"\n  ],\n  \"description\": \"URDF-DiT addresses the kinematic artifact problem in video-diffusion robot data generation for full-body humanoid whole-body contact interaction — the embodiment scope and task category the concurrent EA-WM system (arXiv:2605.06192, May 2026) validates in principle but does not cover. EA-WM injects KVAF kinematic heatmaps into Wan 2.2 for bimanual arm manipulation (~14 DoF) via bidirectional dual-stream fusion requiring joint fine-tuning; URDF-DiT extends to full-body G1 humanoid (29+ DoF) using a ControlNet-style frozen-backbone design (only the FK-heatmap encoder and zero-conv layers trained), reducing trainable parameters and GPU compute versus EA-WM's joint fine-tuning by ~40% and enabling the full pipeline within ≤200 H100-hours across all resource modes. Unlike Dream2Act (which corrects kinematics post-hoc via URDF-IK, achieving 37.5% success on four G1 whole-body contact interaction benchmarks), URDF-DiT enforces G1 kinematic consistency in-loop through per-frame FK heatmap conditioning across all 29 DoF. The sim→video IDM domain gap is technically mitigated via (a) domain-randomized Isaac Lab rendering during IDM training and (b) a per-frame FK residual consistency loss during video generation. A companion sim-bootstrapped IDM converts URDF-DiT-generated video frame pairs into joint velocity commands for policy training — a capability EA-WM explicitly does not provide (action recovery detection rate ~0.45). Evaluation targets three Dream2Act whole-body contact interaction benchmarks (ball kicking, bag punching, box hugging), directly challenging the 37.5% baseline, with ablations isolating in-loop vs. post-hoc conditioning and ControlNet-style vs. bidirectional fusion. Estimated at ~130–200 H100-hours (~$416–$640 at $3.20/hr). Target venue: ICLR 2027 (expected deadline ~October 2026).\",\n  \"project_name\": \"urdf_dit_loco_policy\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"HARD CONSTRAINT VIOLATION: Manual resource estimate is ~250 H100-hours, which exceeds the user-specified hard limit of ≤200 H100-hours total. The entire resource plan must be revised downward.\", \"CRITICAL MISSED CONCURRENT WORK: EA-WM (arXiv:2605.06192, submitted May 7, 2026) renders forward-kinematics joint heatmaps and injects them as dual token streams into a Wan 2.2 backbone — the same core mechanism as URDF-DiT. This work is not acknowledged in the landscape or key references. The claim that 'no published system injects URDF joint-angle sequences directly into video diffusion attention layers' is false.\", \"VENUE MISLABELING: 'ICLR 2026 (paper deadline September 24 2026)' is incorrect. ICLR 2026 submissions closed ~October 2025. A September 24, 2026 deadline corresponds to ICLR 2027.\", \"TIMELINE IMPLAUSIBILITY FOR CoRL: 20 days (by May 29) to implement ControlNet-style conditioning on Wan 2.2 14B, train a sim IDM in Isaac Lab, run 4 benchmark evaluations, and write the paper is not realistic for a 1-2 person team. No timeline breakdown is provided to justify this.\", \"KIMODO MISCHARACTERIZATION: The proposal cites Kimodo as 'validating the in-loop kinematic conditioning principle' for video diffusion, but Kimodo is a 3D kinematic motion diffusion model (trained on mocap), not an RGB video diffusion model. It does not validate that kinematic conditioning works inside video diffusion attention layers.\", \"SIM→VIDEO IDM DOMAIN GAP UNADDRESSED: The IDM trained exclusively on Isaac Lab G1 frame pairs (photorealistic sim) applied zero-shot to Wan 2.2-generated videos (which have diffusion-model-specific textures and artifacts) faces a well-documented distribution gap. The proposal acknowledges this risk only in Human-in-Loop mode and offers no technical mitigation strategy.\", \"EVALUATION SCOPE VS. LOCO-MANIPULATION CLAIM: Dream2Act's four benchmarks (ball kicking, sofa sitting, bag punching, box hugging) are whole-body contact/interaction tasks, not loco-manipulation in the sense of locomotion simultaneously with object manipulation. Framing these as 'loco-manipulation' benchmarks overstates the scope relative to what the contribution promises.\"]\nFeedback: The core direction (in-loop URDF kinematic conditioning for humanoid video diffusion + sim IDM for policy extraction) remains viable but requires substantial revision before CoRL 2026 submission:\n\n1. **Differentiate from EA-WM**: Read arXiv:2605.06192 carefully. URDF-DiT must clearly differentiate from EA-WM's KVAF approach. The clearest differentiation axes are: (a) full-body humanoid (29+ DoF whole-body) vs. bimanual arm-only; (b) ControlNet as a separate trainable module (weights frozen in backbone) vs. EA-WM's bidirectional fusion requiring joint fine-tuning; (c) explicit action extraction pipeline (sim IDM → policy training trajectories) vs. EA-WM's world-model framing without policy training evaluation. The introduction must directly address EA-WM.\n\n2. **Fix the resource plan**: Reduce total to ≤200 H100-hours. Concretely: (a) use LoRA fine-tuning of Wan 2.2 rather than full fine-tuning (documented to run in 6–24 hours on a single GPU); (b) limit IDM training to ~20–30 H100-hours; (c) restrict evaluation to 2–3 benchmarks rather than all 4. A realistic breakdown: ControlNet module training ~60h, IDM ~30h, evaluation ~50h, ablations ~40h = 180h total.\n\n3. **Address IDM domain gap technically**: The sim→video transfer for IDM is the highest technical risk. Add one of: (a) domain-randomized sim rendering to match video diffusion output statistics; (b) a lightweight IDM adapter fine-tuned on a small set of URDF-DiT-generated frame pairs labeled via sim rollout matching; (c) a kinematic consistency loss during URDF-DiT generation that makes generated frames closer to sim-rendered frames. Without this, the zero-shot claim is likely to fail.\n\n4. **Fix venue labeling**: Change 'ICLR 2026' to 'ICLR 2027 (submission deadline ~October 2026)' as a fallback.\n\n5. **Reframe Kimodo citation**: Kimodo validates kinematic constraints in motion diffusion (3D joint sequences), not in RGB video diffusion. Replace with a more precise citation, e.g., citing 2D skeleton-conditioned video generation work (Controllable Complex Human Motion Video Generation, arXiv:2603.08028) as the closer analogue.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T11:51:09.780Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T11:51:09.780Z",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-10T11:51:09.801Z_

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

## Idea under review (round 2/10)
{
  "title": "URDF-DiT: ControlNet-Style Full-Body Kinematic Conditioning for Humanoid Video Diffusion and Sim-Bootstrap IDM Policy Extraction",
  "core_problem": "How can a video diffusion model be conditioned in-loop on a full-body humanoid robot's URDF kinematic structure — enforcing 29+ DoF whole-body consistency during generation rather than correcting artifacts post-hoc — to produce kinematically coherent whole-body contact interaction videos from which a sim-trained inverse dynamics model can extract directly usable joint velocity commands for policy training, specifically for the embodiment scope (full-body humanoid) and task category (whole-body contact interaction) that the concurrent arm-only EA-WM system (arXiv:2605.06192) leaves unaddressed?",
  "opportunity": "GR00T-Dreams/DreamGen (2025) validated the video-diffusion → IDM pipeline for tabletop manipulation. Dream2Act (March 2026) extended to whole-body contact interaction on the G1 (ball kicking, sofa sitting, bag punching, box hugging) using Seedance 2.0 with post-hoc URDF-IK recovery — achieving only 37.5% overall success, with failures attributed to kinematic artifacts from post-hoc correction. EA-WM (arXiv:2605.06192, May 7 2026) validates that in-loop KVAF injection into Wan 2.2 attention effectively enforces kinematic consistency — but is scoped exclusively to bimanual arm manipulation (~14 DoF), uses bidirectional dual-stream fusion requiring joint fine-tuning of both the video and kinematic branches, evaluates on WorldArena/RoboTwin 2.0 tabletop tasks, and produces no policy training pipeline (action recovery detection rate ~0.45). The specific gap URDF-DiT fills is precisely defined: in-loop URDF kinematic conditioning for full-body humanoid whole-body contact interaction (29+ DoF G1), using a ControlNet-style frozen-backbone design that is more compute-efficient than EA-WM's joint fine-tuning, and an explicit sim-IDM pipeline converting generated videos into policy training trajectories — all three dimensions EA-WM leaves unaddressed. Training a ControlNet-style conditioning module on top of Wan 2.2 (backbone frozen) is feasible within ~35 H100-hours; a sim-bootstrapped IDM for the G1 in Isaac Lab adds ~25 H100-hours, keeping the full pipeline within a ≤200 H100-hour budget.",
  "landscape": "GR00T-Dreams/DreamGen (arXiv 2025): fine-tunes Cosmos-Predict2 with language conditioning; extracts pseudo-actions via IDM or latent action model. No URDF kinematic constraint. Tabletop manipulation only. Dream2Act (arXiv:2603.19709, March 2026): generates morphology-consistent G1 robot videos using Seedance 2.0, constrains kinematics post-hoc via URDF-IK — achieves 37.5% overall task success across four whole-body contact interaction benchmarks (ball kick, sofa sit, bag punch, box hug). EA-WM (arXiv:2605.06192, May 2026): the most direct concurrent work — injects Kinematic-Visual Action Fields (KVAF: Gaussian heatmaps at projected end-effector locations) via event-aware bidirectional dual-stream fusion into Wan 2.2; targets bimanual arm manipulation (~14 DoF) only; requires joint fine-tuning of both video and kinematic streams; evaluates on WorldArena/RoboTwin 2.0 tabletop manipulation tasks; provides no policy training output (action recovery detection rate ~0.45, explicitly described as heuristic recovery rather than an IDM). Kinema4D (arXiv March 2026, NTU): URDF-driven FK produces 4D pointmap conditioning for environmental simulation synthesis — targets scene realism, not policy-data generation or video diffusion attention-layer kinematic injection. Controllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026): cascaded text-to-2D-skeleton → skeleton-to-video pipeline validates per-frame 2D pose-sequence conditioning in video diffusion; targets human motion synthesis, not robot URDF kinematics or policy extraction — the closest analogue to URDF-DiT's conditioning mechanism in the video generation literature. X-Humanoid (arXiv Dec 2025): replaces human with humanoid in video via Wan 2.2, no URDF constraint injection. MITTY (arXiv 2025): human-to-robot video diffusion without kinematic enforcement. G-DReaM (arXiv 2025): graph-conditioned diffusion for cross-embodiment motion retargeting; operates on motion sequences, not RGB video. No published system combines in-loop URDF kinematic conditioning for full-body humanoid whole-body contact interaction (29+ DoF) with an explicit sim-IDM → policy training trajectory pipeline.",
  "approach": "URDF-DiT uses a ControlNet-style conditioning module — Wan 2.2 backbone weights fully frozen; only the FK-heatmap encoder and zero-conv injection layers are trained — that encodes per-frame G1 URDF forward-kinematics outputs (all 29 DoF, projected to the camera plane via differentiable FK) as structured Gaussian joint-position heatmaps and injects them into the cross-attention layers of the Wan 2.2 DiT. Unlike EA-WM's bidirectional dual-stream fusion (which requires joint fine-tuning of both video and kinematic branches, roughly doubling trainable parameters and training compute versus a frozen-backbone approach), URDF-DiT's ControlNet-style design concentrates all learning in the conditioning module, reducing GPU hours by ~40% at matched video quality — directly enabling the full pipeline within ≤200 H100-hours. Full-body G1 scope (29 DoF: pelvis, legs, torso, arms, hands) is the critical embodiment extension over EA-WM's arm-only target: coordinating kinematic heatmaps across all limbs simultaneously is the conditioning challenge for whole-body contact interaction that EA-WM's end-effector-only KVAF representation does not address. Joint-angle sequences are sampled from an Isaac Lab G1 motion library covering locomotion primitives and upper-body reach plans, projected onto the camera plane, and encoded as per-frame kinematic tokens concatenated with temporal attention keys inside each DiT block. The sim→video IDM domain gap — the central technical risk — is mitigated via two mechanisms: (a) domain-randomized Isaac Lab rendering during IDM training, sampling lighting, camera noise, and surface material variation to statistically overlap with Wan 2.2's visual output distribution; and (b) a per-frame FK residual consistency loss added to URDF-DiT's generation objective, penalizing deviations between generated joint positions and URDF FK predictions, pulling generated frames toward sim-renderable kinematics before IDM application. The sim-bootstrapped IDM is trained on (frame_t, frame_{t+k}, joint-velocity) tuples from G1 Isaac Lab rollouts under domain-randomized conditions, then applied zero-shot to URDF-DiT-generated videos to extract joint velocity commands for policy training without any real-robot labeling. The pipeline is evaluated on three of Dream2Act's four whole-body contact interaction benchmarks — multi-position ball kicking, bag punching, box hugging (sofa sitting excluded as the least kinematically rich of the four) — using Dream2Act's 37.5% overall success as the primary baseline. Two core ablations: (1) in-loop URDF-DiT conditioning vs. post-hoc URDF-IK at matched video budgets, isolating kinematic artifact reduction as the performance driver; (2) ControlNet-style frozen-backbone vs. bidirectional fusion at matched compute budgets, verifying the efficiency–performance tradeoff relative to EA-WM's architecture.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~130h H100",
      "gpu_utilization": "HIGH idle rate (~40-50% effective utilization) — sequential experiment launches and human debugging keep GPUs idle between runs; ControlNet module training and IDM training are the two dense compute bursts",
      "timeline": "4-6 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$416 (130h × $3.20/hr)",
      "breakdown": "ControlNet module training (frozen Wan 2.2 backbone): ~35h; IDM training (Isaac Lab G1 rollouts + domain-randomized rendering): ~25h; Video generation + evaluation on 3 benchmarks: ~35h; Ablations (in-loop vs. post-hoc, ControlNet-style vs. bidirectional fusion): ~25h; Data prep and miscellaneous: ~10h"
    },
    "human_in_loop": {
      "gpu_hours": "~160h H100",
      "gpu_utilization": "Moderate (~60-65% effective utilization) — agent queues ablation variants back-to-back without waiting for human; approval gates add short pauses only at key architectural decisions (FK residual loss weight, injection layer depth, IDM backbone choice)",
      "timeline": "5-8 weeks",
      "team": "1 researcher, ~30 min/day check-in for experiment approval and direction adjustment",
      "claude_api_cost": "~$150-300 (Opus, ~1,500-2,000 conversation turns covering experiment design, code review, and result analysis)",
      "estimated_gpu_cost": "~$512 (160h × $3.20/hr)",
      "risk_note": "Key risk: if domain-randomized rendering and FK residual loss are insufficient for IDM sim→video transfer, human oversight can detect this at the 2-week checkpoint and redirect toward a lightweight IDM adapter fine-tuned on a small set of URDF-DiT-generated frames matched to sim rollouts via kinematic alignment, before the remaining GPU budget is spent"
    },
    "auto_research": {
      "gpu_hours": "~200h H100 (covers ControlNet injection depth sweeps, FK heatmap resolution variants, IDM backbone comparisons, FK residual loss weight ablation, and extended evaluation on all 4 Dream2Act benchmarks including sofa sitting)",
      "gpu_utilization": "Near-zero idle (~88-92% effective utilization) — agent immediately queues the next experiment upon completion and runs non-dependent trials (IDM training vs. video generation) in parallel across GPUs",
      "timeline": "1-2 weeks with 8+ H100s; 3-4 weeks on 4 GPUs",
      "team": "0 (initial setup ~4h: configure Isaac Lab motion library, domain-randomized rendering pipeline, URDF-DiT scaffold, and automated evaluation harness)",
      "claude_api_cost": "~$400-700 (Opus, ~4,000-7,000 turns for experiment proposal, code generation, failure diagnosis, and iterative result interpretation)",
      "estimated_gpu_cost": "~$640 (200h × $3.20/hr)",
      "speed_bottleneck": "GPU cluster size is the primary bottleneck — with 8 H100s running in parallel, wall-clock time compresses to ~1 week; API quota becomes secondary if the agent spawns many concurrent evaluation sub-agents",
      "risk_note": "Automated evaluation harness must include per-frame kinematic consistency checks (FK residual, joint-limit violation rate, temporal flicker score) alongside task success to prevent silent metric gaming; qualitative failure modes in generated joint sequences are not captured by task-success metrics alone"
    }
  },
  "target_venues": [
    "ICLR 2027 (expected submission deadline ~October 2026; official announcement pending at iclr.cc)",
    "CoRL 2027 (fallback)"
  ],
  "level": "solid",
  "key_references": [
    "DreamGen: Unlocking Generalization in Robot Learning through Video World Models (arXiv 2025)",
    "Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis / Dream2Act (arXiv:2603.19709, March 2026)",
    "EA-WM: Embodiment-Aware World Model via Kinematic-Visual Action Fields for Bimanual Manipulation (arXiv:2605.06192, May 2026) — primary concurrent work; differentiators: arm-only vs. full-body, bidirectional fusion vs. ControlNet-style, no policy training vs. explicit IDM pipeline",
    "Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation (arXiv March 2026)",
    "Controllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026) — validates per-frame 2D skeleton-sequence conditioning in video diffusion; closest video-generation analogue to URDF-DiT's conditioning mechanism",
    "X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (arXiv Dec 2025)",
    "Mitty: Diffusion-based Human-to-Robot Video Generation (arXiv 2025)",
    "Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models (arXiv 2025)",
    "G-DReaM: Graph-conditioned Diffusion Retargeting across Multiple Embodiments (arXiv 2025)"
  ],
  "description": "URDF-DiT addresses the kinematic artifact problem in video-diffusion robot data generation for full-body humanoid whole-body contact interaction — the embodiment scope and task category the concurrent EA-WM system (arXiv:2605.06192, May 2026) validates in principle but does not cover. EA-WM injects KVAF kinematic heatmaps into Wan 2.2 for bimanual arm manipulation (~14 DoF) via bidirectional dual-stream fusion requiring joint fine-tuning; URDF-DiT extends to full-body G1 humanoid (29+ DoF) using a ControlNet-style frozen-backbone design (only the FK-heatmap encoder and zero-conv layers trained), reducing trainable parameters and GPU compute versus EA-WM's joint fine-tuning by ~40% and enabling the full pipeline within ≤200 H100-hours across all resource modes. Unlike Dream2Act (which corrects kinematics post-hoc via URDF-IK, achieving 37.5% success on four G1 whole-body contact interaction benchmarks), URDF-DiT enforces G1 kinematic consistency in-loop through per-frame FK heatmap conditioning across all 29 DoF. The sim→video IDM domain gap is technically mitigated via (a) domain-randomized Isaac Lab rendering during IDM training and (b) a per-frame FK residual consistency loss during video generation. A companion sim-bootstrapped IDM converts URDF-DiT-generated video frame pairs into joint velocity commands for policy training — a capability EA-WM explicitly does not provide (action recovery detection rate ~0.45). Evaluation targets three Dream2Act whole-body contact interaction benchmarks (ball kicking, bag punching, box hugging), directly challenging the 37.5% baseline, with ablations isolating in-loop vs. post-hoc conditioning and ControlNet-style vs. bidirectional fusion. Estimated at ~130–200 H100-hours (~$416–$640 at $3.20/hr). Target venue: ICLR 2027 (expected deadline ~October 2026).",
  "project_name": "urdf_dit_loco_policy",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["HARD CONSTRAINT VIOLATION: Manual resource estimate is ~250 H100-hours, which exceeds the user-specified hard limit of ≤200 H100-hours total. The entire resource plan must be revised downward.", "CRITICAL MISSED CONCURRENT WORK: EA-WM (arXiv:2605.06192, submitted May 7, 2026) renders forward-kinematics joint heatmaps and injects them as dual token streams into a Wan 2.2 backbone — the same core mechanism as URDF-DiT. This work is not acknowledged in the landscape or key references. The claim that 'no published system injects URDF joint-angle sequences directly into video diffusion attention layers' is false.", "VENUE MISLABELING: 'ICLR 2026 (paper deadline September 24 2026)' is incorrect. ICLR 2026 submissions closed ~October 2025. A September 24, 2026 deadline corresponds to ICLR 2027.", "TIMELINE IMPLAUSIBILITY FOR CoRL: 20 days (by May 29) to implement ControlNet-style conditioning on Wan 2.2 14B, train a sim IDM in Isaac Lab, run 4 benchmark evaluations, and write the paper is not realistic for a 1-2 person team. No timeline breakdown is provided to justify this.", "KIMODO MISCHARACTERIZATION: The proposal cites Kimodo as 'validating the in-loop kinematic conditioning principle' for video diffusion, but Kimodo is a 3D kinematic motion diffusion model (trained on mocap), not an RGB video diffusion model. It does not validate that kinematic conditioning works inside video diffusion attention layers.", "SIM→VIDEO IDM DOMAIN GAP UNADDRESSED: The IDM trained exclusively on Isaac Lab G1 frame pairs (photorealistic sim) applied zero-shot to Wan 2.2-generated videos (which have diffusion-model-specific textures and artifacts) faces a well-documented distribution gap. The proposal acknowledges this risk only in Human-in-Loop mode and offers no technical mitigation strategy.", "EVALUATION SCOPE VS. LOCO-MANIPULATION CLAIM: Dream2Act's four benchmarks (ball kicking, sofa sitting, bag punching, box hugging) are whole-body contact/interaction tasks, not loco-manipulation in the sense of locomotion simultaneously with object manipulation. Framing these as 'loco-manipulation' benchmarks overstates the scope relative to what the contribution promises."]
Feedback: The core direction (in-loop URDF kinematic conditioning for humanoid video diffusion + sim IDM for policy extraction) remains viable but requires substantial revision before CoRL 2026 submission:

1. **Differentiate from EA-WM**: Read arXiv:2605.06192 carefully. URDF-DiT must clearly differentiate from EA-WM's KVAF approach. The clearest differentiation axes are: (a) full-body humanoid (29+ DoF whole-body) vs. bimanual arm-only; (b) ControlNet as a separate trainable module (weights frozen in backbone) vs. EA-WM's bidirectional fusion requiring joint fine-tuning; (c) explicit action extraction pipeline (sim IDM → policy training trajectories) vs. EA-WM's world-model framing without policy training evaluation. The introduction must directly address EA-WM.

2. **Fix the resource plan**: Reduce total to ≤200 H100-hours. Concretely: (a) use LoRA fine-tuning of Wan 2.2 rather than full fine-tuning (documented to run in 6–24 hours on a single GPU); (b) limit IDM training to ~20–30 H100-hours; (c) restrict evaluation to 2–3 benchmarks rather than all 4. A realistic breakdown: ControlNet module training ~60h, IDM ~30h, evaluation ~50h, ablations ~40h = 180h total.

3. **Address IDM domain gap technically**: The sim→video transfer for IDM is the highest technical risk. Add one of: (a) domain-randomized sim rendering to match video diffusion output statistics; (b) a lightweight IDM adapter fine-tuned on a small set of URDF-DiT-generated frame pairs labeled via sim rollout matching; (c) a kinematic consistency loss during URDF-DiT generation that makes generated frames closer to sim-rendered frames. Without this, the zero-shot claim is likely to fail.

4. **Fix venue labeling**: Change 'ICLR 2026' to 'ICLR 2027 (submission deadline ~October 2026)' as a fallback.

5. **Reframe Kimodo citation**: Kimodo validates kinematic constraints in motion diffusion (3D joint sequences), not in RGB video diffusion. Replace with a more precise citation, e.g., citing 2D skeleton-conditioned video generation work (Controllable Complex Human Motion Video Generation, arXiv:2603.08028) as the closer analogue.


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
  "promptId": "2788fdb5-76a8-4a46-a99a-4abad3df867d",
  "type": "user",
  "uuid": "3a9f8208-da1c-4412-9a57-d6feeb1ffba8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T11:51:09.799Z_

```json
{
  "parentUuid": "3a9f8208-da1c-4412-9a57-d6feeb1ffba8",
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
  "uuid": "ac4eaac9-20bd-4f93-a7b1-7fdf7b3db3fd",
  "timestamp": "2026-05-10T11:51:09.799Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T11:51:09.800Z_

```json
{
  "parentUuid": "ac4eaac9-20bd-4f93-a7b1-7fdf7b3db3fd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "be476dcb-0d2c-4e17-ac18-7616fa6bfc4b",
  "timestamp": "2026-05-10T11:51:09.800Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
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
  "leafUuid": "be476dcb-0d2c-4e17-ac18-7616fa6bfc4b",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review URDF-DiT humanoid kinematic conditioning for CoRL",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c"
}
```

---

### Assistant

_source line 8 · 2026-05-10T11:51:17.552Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this Round 2 revision of the URDF-DiT idea. I need to independently verify the claims, check for concurrent work, assess feasibility, and evaluate whether the previous round's issues have been addressed.

Let me start by doing independent research on the key claims and papers mentioned.

Key things to verify:
1. EA-WM (arXiv:2605.06192) - the primary concurrent work - what does it actually do?
2. Dream2Act (arXiv:2603.19709) - 37.5% success rate claim
3. Whether the ControlNet-style approach for video diffusion is novel


4. The resource estimates - whether the reduction from ~250h to ~130h is justified
5. Kinema4D's actual capabilities
6. If the ICLR 2027 venue label is accurate
7. Whether the sim-to-video domain gap issue was properly addressed

Let me search for these papers and concurrent work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be476dcb-0d2c-4e17-ac18-7616fa6bfc4b",
  "isSidechain": false,
  "requestId": "req_011Catqdeu6zAipbvzRbuLz2",
  "type": "assistant",
  "uuid": "afc34ba5-60aa-49c7-b8a5-60cb52c5d021",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GNHdH9Adv6pusn1NhtSMrw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14562,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1303,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 14562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14562
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

_source line 9 · 2026-05-10T11:51:17.555Z_

I'll conduct independent research to verify the claims in this Round 2 revision. Let me search across multiple dimensions simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afc34ba5-60aa-49c7-b8a5-60cb52c5d021",
  "isSidechain": false,
  "requestId": "req_011Catqdeu6zAipbvzRbuLz2",
  "type": "assistant",
  "uuid": "7a67054a-5c43-4b4a-ac3f-e24d07a2fc58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GNHdH9Adv6pusn1NhtSMrw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14562,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1303,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 14562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14562
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

_source line 10 · 2026-05-10T11:51:22.997Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BdwQyWM9Ha11RgSQd5QheL`</summary>

```json
{
  "description": "Search for EA-WM paper and concurrent humanoid video diffusion work",
  "subagent_type": "Explore",
  "prompt": "Search for the following papers and report back their actual content/abstracts. I need to verify specific claims about them.\n\n1. Search for \"EA-WM arXiv 2605.06192 kinematic visual action fields bimanual manipulation\" - what does this paper actually do? Does it use ControlNet-style conditioning or bidirectional fusion? Is it arm-only or full-body?\n\n2. Search for \"Dream2Act morphology consistent humanoid interaction robot-centric video synthesis arXiv 2603.19709\" - what is the actual success rate? Does it use post-hoc URDF-IK?\n\n3. Search for \"ControlNet style conditioning video diffusion robot manipulation 2025 2026\" - any papers doing ControlNet-style kinematic conditioning for robot video generation?\n\n4. Search for \"humanoid video generation policy training data 2026 arXiv\" - find any recent concurrent work we might be missing.\n\nUse web search for each query. Report actual paper content/abstracts, not just titles."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a67054a-5c43-4b4a-ac3f-e24d07a2fc58",
  "isSidechain": false,
  "requestId": "req_011Catqdeu6zAipbvzRbuLz2",
  "type": "assistant",
  "uuid": "0a46d38d-39a0-43a8-b69b-e55ded30834b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GNHdH9Adv6pusn1NhtSMrw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14562,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1303,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 14562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14562
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

_source line 11 · 2026-05-10T11:51:29.178Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Qj3SRLaVrUGM5JuSd8q8e8`</summary>

```json
{
  "description": "Search for GR00T-Dreams and humanoid data generation landscape",
  "subagent_type": "Explore",
  "prompt": "Search for the following and report actual paper content:\n\n1. \"GR00T Dreams DreamGen NVIDIA humanoid video world model policy training 2025 2026\" - what exactly does this do? What backbone? What conditioning?\n\n2. \"whole body humanoid loco-manipulation video generation diffusion 2026\" - any papers specifically on whole-body humanoid (not just arm) video generation for policy training?\n\n3. \"ControlNet video diffusion conditioning 2024 2025\" - how widely has ControlNet-style conditioning been applied to video diffusion models? Is it a well-established technique?\n\n4. \"Isaac Lab G1 humanoid manipulation benchmark evaluation 2025 2026\" - what tasks exist on Isaac Lab for G1 humanoid evaluation?\n\n5. \"inverse dynamics model IDM sim to real transfer domain gap robot video\" - any papers on the IDM domain gap problem for sim-generated vs. diffusion-generated videos?\n\nUse web search. Report actual content found, not just paper names."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a46d38d-39a0-43a8-b69b-e55ded30834b",
  "isSidechain": false,
  "requestId": "req_011Catqdeu6zAipbvzRbuLz2",
  "type": "assistant",
  "uuid": "17c2bd9d-81bb-4132-88c2-b357d86d2fb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GNHdH9Adv6pusn1NhtSMrw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14562,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1303,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 14562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14562
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

_source line 12 · 2026-05-10T11:51:35.361Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0121kxu9pnsJbe6Ag5zFPfiC`</summary>

```json
{
  "description": "Search for ControlNet video diffusion novelty and competing work",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing an ML paper idea called \"URDF-DiT\" that proposes using ControlNet-style conditioning on a frozen Wan 2.2 video diffusion backbone to inject URDF forward-kinematics heatmaps for humanoid robot video generation. Help me verify its novelty by searching for:\n\n1. \"Wan 2.2 video diffusion ControlNet conditioning robotics 2025 2026\" - has ControlNet been applied to Wan 2.2 for robotics?\n\n2. \"URDF kinematic conditioning video generation robot 2025 2026\" - any direct URDF-conditioned video generation papers?\n\n3. \"whole body humanoid forward kinematics video diffusion conditioning\" - papers combining FK with video diffusion\n\n4. \"Kinema4D URDF 4D world modeling embodied simulation arXiv March 2026\" - what does Kinema4D actually do? Is it related to video diffusion or just 3D simulation?\n\n5. \"X-Humanoid humanoid video Wan 2.2 arXiv 2025\" - what does X-Humanoid do exactly?\n\n6. site:arxiv.org \"humanoid\" \"video diffusion\" \"kinematic\" 2026 - find any papers combining these three elements\n\nReport actual paper content/abstracts found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17c2bd9d-81bb-4132-88c2-b357d86d2fb8",
  "isSidechain": false,
  "requestId": "req_011Catqdeu6zAipbvzRbuLz2",
  "type": "assistant",
  "uuid": "e1b7435c-990e-4ce2-8c68-6bb77ca9030f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GNHdH9Adv6pusn1NhtSMrw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14562,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1303,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 14562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14562
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

_source line 13 · 2026-05-10T11:52:04.118Z_

<details><summary>↩ Tool result · `toolu_0121kxu9pnsJbe6Ag5zFPfiC`</summary>

```text
Excellent! I've completed a comprehensive search for related work. Here's a detailed report on the novelty landscape for your URDF-DiT proposal:

## Summary of Findings

### 1. **ControlNet on Wan 2.2 for Robotics**
**Status: Partially Explored but Not Robotics-Specific**

While Wan 2.1 and Wan 2.2 support ControlNet-style conditioning (depth, Canny, OpenPose), the search found no papers specifically applying this to robot control tasks. The ControlNet implementations focus on visual guidance (pose, depth) rather than URDF-based kinematic conditioning. This is a gap your approach could fill.

### 2. **URDF-Conditioned Video Generation**
**Status: NOT FOUND - Your Idea Appears Novel**

No direct URDF-conditioned video generation papers were found. However, there is relevant related work:
- **URDF-Anything+** (2603.14010): Generates URDF files from images, but focuses on 3D asset generation and physics simulation rather than video synthesis
- **URDFormer** (2405.11656): Maps images to simulation environments with kinematic structure, but again focuses on simulation not video generation
- **Dream2Act** (2603.19709): Uses URDF-constrained inverse kinematics to translate **from** video to joint trajectories (inverse direction), not conditioning video generation with URDF heatmaps

### 3. **Whole-Body Humanoid FK + Video Diffusion**
**Status: Partially Related but Different Approaches**

Several papers combine these elements but with different architectures:
- **Kimodo** (2603.15546): Kinematic motion diffusion model (motion-space diffusion, not video), supports full-body constraints including sparse joint positions/rotations and 2D waypoints
- **PEVA** (Whole-Body Conditioned Egocentric Video Prediction, 2506.21552): Conditions on kinematic pose trajectories but uses auto-regressive conditional diffusion, not ControlNet-style frozen backbone
- **DreamControl** (2509.14353): Uses diffusion + RL but for humanoid control, not for video generation with kinematic conditioning

**Key Distinction**: These all condition video/motion generation on poses or constraints differently than injecting URDF forward-kinematics heatmaps.

### 4. **Kinema4D - THE MOST RELEVANT PAPER**
**Status: HIGHLY RELEVANT BUT FUNDAMENTALLY DIFFERENT APPROACH**

From March 2026 (arXiv:2603.16669):

Kinema4D is an action-conditioned 4D generative robotic simulator that:
- **Drives a URDF-based 3D robot via kinematics** to produce 4D control trajectories
- **Projects the 4D robot trajectory into a pointmap** as spatiotemporal visual signal
- Uses this to control a generative model synthesizing environment dynamics
- Includes a Robo4D-200k dataset (200k+ robot interaction episodes)

**Critical Difference from URDF-DiT**: Kinema4D uses kinematics to generate the world model input (pointmap as conditioning signal), whereas URDF-DiT would use URDF forward-kinematics **heatmaps** to condition the frozen video diffusion backbone. Kinema4D is generating the 4D simulation; URDF-DiT would be generating video directly.

### 5. **X-Humanoid - Wan 2.2 Humanoid Videos**
**Status: Different Conditioning Mechanism**

From December 2025 (arXiv:2512.04537):

X-Humanoid adapts Wan 2.2 by:
- Taking **human video as input condition** (not kinematic heatmaps)
- Encoding input human video into condition tokens
- Concatenating with generation tokens during self-attention
- Outputting edited video with humanoid embodiment

**How This Differs from URDF-DiT**: X-Humanoid conditions on pixel-space human video; URDF-DiT would condition on abstract kinematic heatmaps (FK visualization).

### 6. **Arxiv Search Results**
**Status: Confirmed No Direct Precedent**

The broader 2026 papers on humanoid + video diffusion + kinematics (Kimodo, Dream2Act, PEVA, DreamControl, Kinema4D) all approach the combination differently - none use URDF forward-kinematics heatmaps as ControlNet-style conditioning to a frozen Wan 2.2 backbone.

## Novelty Assessment

**URDF-DiT appears genuinely novel** because:

1. **No URDF FK heatmap conditioning on video diffusion** - Kinema4D uses URDF to generate the conditioning signal, not as visual heatmap conditioning
2. **No Wan 2.2 + URDF combination** - X-Humanoid uses Wan 2.2 but conditions on human video, not kinematics
3. **Different from motion diffusion approaches** - Kimodo, PEVA, DreamControl work in motion/pose space or with different conditioning architectures
4. **Inverse of Dream2Act** - While Dream2Act extracts kinematics from video, URDF-DiT injects kinematics into video generation
5. **ControlNet on Wan 2.2 for robotics untested** - No robotics papers found using ControlNet conditioning on Wan 2.2

The key novelty lies in the **specific combination**: using URDF forward-kinematics visualization as a frozen backbone conditioning signal in a Wan 2.2 ControlNet-style architecture for humanoid video generation.

Sources:
- [Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669)
- [X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale](https://arxiv.org/abs/2512.04537)
- [Kimodo: Scaling Controllable Human Motion Generation](https://arxiv.org/abs/2603.15546)
- [Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis (Dream2Act)](https://arxiv.org/html/2603.19709v2)
- [Whole-Body Conditioned Egocentric Video Prediction (PEVA)](https://arxiv.org/html/2506.21552)
- [DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion](https://arxiv.org/abs/2509.14353)
- [URDF-Anything+: Autoregressive Articulated 3D Models Generation for Physical Simulation](https://arxiv.org/abs/2603.14010)
- [URDFormer: A Pipeline for Constructing Articulated Simulation Environments from Real-World Images](https://arxiv.org/abs/2405.11656)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1b7435c-990e-4ce2-8c68-6bb77ca9030f",
  "isSidechain": false,
  "promptId": "2788fdb5-76a8-4a46-a99a-4abad3df867d",
  "type": "user",
  "uuid": "09d38922-38d2-4b49-aa4b-bfed440ba01b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing an ML paper idea called \"URDF-DiT\" that proposes using ControlNet-style conditioning on a frozen Wan 2.2 video diffusion backbone to inject URDF forward-kinematics heatmaps for humanoid robot video generation. Help me verify its novelty by searching for:\n\n1. \"Wan 2.2 video diffusion ControlNet conditioning robotics 2025 2026\" - has ControlNet been applied to Wan 2.2 for robotics?\n\n2. \"URDF kinematic conditioning video generation robot 2025 2026\" - any direct URDF-conditioned video generation papers?\n\n3. \"whole body humanoid forward kinematics video diffusion conditioning\" - papers combining FK with video diffusion\n\n4. \"Kinema4D URDF 4D world modeling embodied simulation arXiv March 2026\" - what does Kinema4D actually do? Is it related to video diffusion or just 3D simulation?\n\n5. \"X-Humanoid humanoid video Wan 2.2 arXiv 2025\" - what does X-Humanoid do exactly?\n\n6. site:arxiv.org \"humanoid\" \"video diffusion\" \"kinematic\" 2026 - find any papers combining these three elements\n\nReport actual paper content/abstracts found.",
    "agentId": "a7446b7e790b8cadb",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! I've completed a comprehensive search for related work. Here's a detailed report on the novelty landscape for your URDF-DiT proposal:\n\n## Summary of Findings\n\n### 1. **ControlNet on Wan 2.2 for Robotics**\n**Status: Partially Explored but Not Robotics-Specific**\n\nWhile Wan 2.1 and Wan 2.2 support ControlNet-style conditioning (depth, Canny, OpenPose), the search found no papers specifically applying this to robot control tasks. The ControlNet implementations focus on visual guidance (pose, depth) rather than URDF-based kinematic conditioning. This is a gap your approach could fill.\n\n### 2. **URDF-Conditioned Video Generation**\n**Status: NOT FOUND - Your Idea Appears Novel**\n\nNo direct URDF-conditioned video generation papers were found. However, there is relevant related work:\n- **URDF-Anything+** (2603.14010): Generates URDF files from images, but focuses on 3D asset generation and physics simulation rather than video synthesis\n- **URDFormer** (2405.11656): Maps images to simulation environments with kinematic structure, but again focuses on simulation not video generation\n- **Dream2Act** (2603.19709): Uses URDF-constrained inverse kinematics to translate **from** video to joint trajectories (inverse direction), not conditioning video generation with URDF heatmaps\n\n### 3. **Whole-Body Humanoid FK + Video Diffusion**\n**Status: Partially Related but Different Approaches**\n\nSeveral papers combine these elements but with different architectures:\n- **Kimodo** (2603.15546): Kinematic motion diffusion model (motion-space diffusion, not video), supports full-body constraints including sparse joint positions/rotations and 2D waypoints\n- **PEVA** (Whole-Body Conditioned Egocentric Video Prediction, 2506.21552): Conditions on kinematic pose trajectories but uses auto-regressive conditional diffusion, not ControlNet-style frozen backbone\n- **DreamControl** (2509.14353): Uses diffusion + RL but for humanoid control, not for video generation with kinematic conditioning\n\n**Key Distinction**: These all condition video/motion generation on poses or constraints differently than injecting URDF forward-kinematics heatmaps.\n\n### 4. **Kinema4D - THE MOST RELEVANT PAPER**\n**Status: HIGHLY RELEVANT BUT FUNDAMENTALLY DIFFERENT APPROACH**\n\nFrom March 2026 (arXiv:2603.16669):\n\nKinema4D is an action-conditioned 4D generative robotic simulator that:\n- **Drives a URDF-based 3D robot via kinematics** to produce 4D control trajectories\n- **Projects the 4D robot trajectory into a pointmap** as spatiotemporal visual signal\n- Uses this to control a generative model synthesizing environment dynamics\n- Includes a Robo4D-200k dataset (200k+ robot interaction episodes)\n\n**Critical Difference from URDF-DiT**: Kinema4D uses kinematics to generate the world model input (pointmap as conditioning signal), whereas URDF-DiT would use URDF forward-kinematics **heatmaps** to condition the frozen video diffusion backbone. Kinema4D is generating the 4D simulation; URDF-DiT would be generating video directly.\n\n### 5. **X-Humanoid - Wan 2.2 Humanoid Videos**\n**Status: Different Conditioning Mechanism**\n\nFrom December 2025 (arXiv:2512.04537):\n\nX-Humanoid adapts Wan 2.2 by:\n- Taking **human video as input condition** (not kinematic heatmaps)\n- Encoding input human video into condition tokens\n- Concatenating with generation tokens during self-attention\n- Outputting edited video with humanoid embodiment\n\n**How This Differs from URDF-DiT**: X-Humanoid conditions on pixel-space human video; URDF-DiT would condition on abstract kinematic heatmaps (FK visualization).\n\n### 6. **Arxiv Search Results**\n**Status: Confirmed No Direct Precedent**\n\nThe broader 2026 papers on humanoid + video diffusion + kinematics (Kimodo, Dream2Act, PEVA, DreamControl, Kinema4D) all approach the combination differently - none use URDF forward-kinematics heatmaps as ControlNet-style conditioning to a frozen Wan 2.2 backbone.\n\n## Novelty Assessment\n\n**URDF-DiT appears genuinely novel** because:\n\n1. **No URDF FK heatmap conditioning on video diffusion** - Kinema4D uses URDF to generate the conditioning signal, not as visual heatmap conditioning\n2. **No Wan 2.2 + URDF combination** - X-Humanoid uses Wan 2.2 but conditions on human video, not kinematics\n3. **Different from motion diffusion approaches** - Kimodo, PEVA, DreamControl work in motion/pose space or with different conditioning architectures\n4. **Inverse of Dream2Act** - While Dream2Act extracts kinematics from video, URDF-DiT injects kinematics into video generation\n5. **ControlNet on Wan 2.2 for robotics untested** - No robotics papers found using ControlNet conditioning on Wan 2.2\n\nThe key novelty lies in the **specific combination**: using URDF forward-kinematics visualization as a frozen backbone conditioning signal in a Wan 2.2 ControlNet-style architecture for humanoid video generation.\n\nSources:\n- [Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669)\n- [X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale](https://arxiv.org/abs/2512.04537)\n- [Kimodo: Scaling Controllable Human Motion Generation](https://arxiv.org/abs/2603.15546)\n- [Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis (Dream2Act)](https://arxiv.org/html/2603.19709v2)\n- [Whole-Body Conditioned Egocentric Video Prediction (PEVA)](https://arxiv.org/html/2506.21552)\n- [DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion](https://arxiv.org/abs/2509.14353)\n- [URDF-Anything+: Autoregressive Articulated 3D Models Generation for Physical Simulation](https://arxiv.org/abs/2603.14010)\n- [URDFormer: A Pipeline for Constructing Articulated Simulation Environments from Real-World Images](https://arxiv.org/abs/2405.11656)"
      }
    ],
    "totalDurationMs": 28752,
    "totalTokens": 25428,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 3657,
      "cache_creation_input_tokens": 3199,
      "cache_read_input_tokens": 16889,
      "output_tokens": 1683,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3199
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3657,
          "output_tokens": 1683,
          "cache_read_input_tokens": 16889,
          "cache_creation_input_tokens": 3199,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3199,
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
  "sourceToolAssistantUUID": "e1b7435c-990e-4ce2-8c68-6bb77ca9030f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T11:52:06.836Z_

<details><summary>↩ Tool result · `toolu_01BdwQyWM9Ha11RgSQd5QheL`</summary>

```text
Excellent! I now have detailed information on all four queries. Here's my report on the actual content and claims:

## Paper Search Results and Findings

### 1. EA-WM (arXiv 2605.06192) - Kinematic Visual Action Fields

**Claim Verification:**
- **ControlNet-style conditioning**: FALSE. EA-WM uses **bidirectional fusion**, not ControlNet-style conditioning. It employs "a dedicated KVAF branch and event-aware bidirectional fusion blocks" built on the Wan2.2 video diffusion backbone with separate video and KVAF token streams.
- **Embodiment scope**: BIMANUAL - it explicitly handles bimanual manipulation with depth-aware arm structures, joint landmarks, gripper geometry, and end-effector heatmaps for both arms.

**Key technical innovation**: The architecture uses event gates that "modulate cross-stream attention" to capture object state changes, and Event-Difference Latent Supervision (EDLS) that "supervises event predictions with VAE-encoded temporal difference latents" rather than auxiliary losses.

**Source**: [EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields](https://arxiv.org/html/2605.06192v1)

---

### 2. Dream2Act (arXiv 2603.19709) - Morphology-Consistent Humanoid Interaction

**Claim Verification:**
- **Success rate**: 37.5% overall across four interaction categories on Unitree G1. Breakdown: ball kicking (40%), box hugging (10%), bag punching (30%), sofa sitting (70%).
- **Post-hoc URDF-IK**: TRUE. The method explicitly uses "constrained Inverse Kinematics (IK) optimization" that recovers "joint angles by minimizing endpoint distances while respecting joint limits."

**Trajectory extraction pipeline**:
1. Video-to-2D: ViTPose detects 30 native robotic joints as 2D keypoints from synthesized videos
2. 2D-to-3D lifting: Specialized network regresses 3D relative joint coordinates in camera space
3. Kinematic recovery: Constrained IK optimizes joint angles, then PnP alignment recovers global pose

**Source**: [Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis](https://arxiv.org/html/2603.19709v1)

---

### 3. ControlNet-Style Conditioning for Robot Video Generation (2025-2026)

**Findings:**
The search identified multiple papers using ControlNet-inspired architectures for robot manipulation:

- **Motion Prompting** (CVPR 2025): Controlling video generation with motion trajectories
- **Control-A-Video**: Text-to-video generation with diffusion models using controllable conditioning
- **Video-ControlNet**: Generates videos conditioned on sequences of control signals (edges, depth maps), with track-conditioned ControlNet adapters for motion control in videos
- Recent advances address feature "collisions" when blending multiple spatial control signals through MGDA-inspired residual combination

However, I found NO paper explicitly doing "ControlNet-style kinematic conditioning for robot video generation" as a primary contribution in the 2025-2026 timeframe. The closest work uses ControlNet-inspired mechanisms but not for kinematic conditioning specifically.

**Sources**: 
- [Motion Prompting: Controlling Video Generation with Motion Trajectories](https://openaccess.thecvf.com/content/CVPR2025/papers/Geng_Motion_Prompting_Controlling_Video_Generation_with_Motion_Trajectories_CVPR_2025_paper.pdf)
- [Control-A-Video: Controllable Text-to-Video Generation with Diffusion Models](https://controlavideo.github.io/)

---

### 4. Humanoid Video Generation & Policy Training (2026 arXiv)

**Recent concurrent work found:**

1. **X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale** (arXiv 2512.04537)
   - Adapts Wan 2.2 diffusion model for human-to-humanoid video translation
   - Created 17+ hours of synthetic paired human-humanoid videos via Unreal Engine
   - Created 60-hour "robotized" Ego-Exo4D dataset (3.6M frames) with Tesla Optimus
   - User studies showed 69% preference for motion consistency and 62.1% for embodiment accuracy

2. **FlowAct-R1: Towards Interactive Humanoid Video Generation** (arXiv 2601.10103)
   - Real-time interactive humanoid video generation using MMDiT architecture
   - Enables streaming synthesis with arbitrary durations and low-latency responsiveness

3. **From Generated Human Videos to Physically Plausible Robot Trajectories** (arXiv 2512.05094)
   - Two-stage pipeline: 4D reconstruction + GenMimic RL policy
   - Uses weighted keypoint tracking prioritizing end-effectors
   - Symmetry loss leverages bilateral symmetry to correct errors
   - Trained on AMASS data via PPO

4. **Rethinking Video Generation Model for the Embodied World** (arXiv 2601.15282)
   - Comprehensive framework for video generation in embodied AI contexts

**Sources**:
- [X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale](https://arxiv.org/html/2512.04537v1)
- [FlowAct-R1: Towards Interactive Humanoid Video Generation](https://arxiv.org/html/2601.10103v1)
- [From Generated Human Videos to Physically Plausible Robot Trajectories](https://arxiv.org/html/2512.05094)
- [Rethinking Video Generation Model for the Embodied World](https://arxiv.org/html/2601.15282v1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a46d38d-39a0-43a8-b69b-e55ded30834b",
  "isSidechain": false,
  "promptId": "2788fdb5-76a8-4a46-a99a-4abad3df867d",
  "type": "user",
  "uuid": "8cfb7cf3-50be-42af-a396-48d20d2e08fa",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the following papers and report back their actual content/abstracts. I need to verify specific claims about them.\n\n1. Search for \"EA-WM arXiv 2605.06192 kinematic visual action fields bimanual manipulation\" - what does this paper actually do? Does it use ControlNet-style conditioning or bidirectional fusion? Is it arm-only or full-body?\n\n2. Search for \"Dream2Act morphology consistent humanoid interaction robot-centric video synthesis arXiv 2603.19709\" - what is the actual success rate? Does it use post-hoc URDF-IK?\n\n3. Search for \"ControlNet style conditioning video diffusion robot manipulation 2025 2026\" - any papers doing ControlNet-style kinematic conditioning for robot video generation?\n\n4. Search for \"humanoid video generation policy training data 2026 arXiv\" - find any recent concurrent work we might be missing.\n\nUse web search for each query. Report actual paper content/abstracts, not just titles.",
    "agentId": "ad1f7a683f8fc17fb",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! I now have detailed information on all four queries. Here's my report on the actual content and claims:\n\n## Paper Search Results and Findings\n\n### 1. EA-WM (arXiv 2605.06192) - Kinematic Visual Action Fields\n\n**Claim Verification:**\n- **ControlNet-style conditioning**: FALSE. EA-WM uses **bidirectional fusion**, not ControlNet-style conditioning. It employs \"a dedicated KVAF branch and event-aware bidirectional fusion blocks\" built on the Wan2.2 video diffusion backbone with separate video and KVAF token streams.\n- **Embodiment scope**: BIMANUAL - it explicitly handles bimanual manipulation with depth-aware arm structures, joint landmarks, gripper geometry, and end-effector heatmaps for both arms.\n\n**Key technical innovation**: The architecture uses event gates that \"modulate cross-stream attention\" to capture object state changes, and Event-Difference Latent Supervision (EDLS) that \"supervises event predictions with VAE-encoded temporal difference latents\" rather than auxiliary losses.\n\n**Source**: [EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields](https://arxiv.org/html/2605.06192v1)\n\n---\n\n### 2. Dream2Act (arXiv 2603.19709) - Morphology-Consistent Humanoid Interaction\n\n**Claim Verification:**\n- **Success rate**: 37.5% overall across four interaction categories on Unitree G1. Breakdown: ball kicking (40%), box hugging (10%), bag punching (30%), sofa sitting (70%).\n- **Post-hoc URDF-IK**: TRUE. The method explicitly uses \"constrained Inverse Kinematics (IK) optimization\" that recovers \"joint angles by minimizing endpoint distances while respecting joint limits.\"\n\n**Trajectory extraction pipeline**:\n1. Video-to-2D: ViTPose detects 30 native robotic joints as 2D keypoints from synthesized videos\n2. 2D-to-3D lifting: Specialized network regresses 3D relative joint coordinates in camera space\n3. Kinematic recovery: Constrained IK optimizes joint angles, then PnP alignment recovers global pose\n\n**Source**: [Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis](https://arxiv.org/html/2603.19709v1)\n\n---\n\n### 3. ControlNet-Style Conditioning for Robot Video Generation (2025-2026)\n\n**Findings:**\nThe search identified multiple papers using ControlNet-inspired architectures for robot manipulation:\n\n- **Motion Prompting** (CVPR 2025): Controlling video generation with motion trajectories\n- **Control-A-Video**: Text-to-video generation with diffusion models using controllable conditioning\n- **Video-ControlNet**: Generates videos conditioned on sequences of control signals (edges, depth maps), with track-conditioned ControlNet adapters for motion control in videos\n- Recent advances address feature \"collisions\" when blending multiple spatial control signals through MGDA-inspired residual combination\n\nHowever, I found NO paper explicitly doing \"ControlNet-style kinematic conditioning for robot video generation\" as a primary contribution in the 2025-2026 timeframe. The closest work uses ControlNet-inspired mechanisms but not for kinematic conditioning specifically.\n\n**Sources**: \n- [Motion Prompting: Controlling Video Generation with Motion Trajectories](https://openaccess.thecvf.com/content/CVPR2025/papers/Geng_Motion_Prompting_Controlling_Video_Generation_with_Motion_Trajectories_CVPR_2025_paper.pdf)\n- [Control-A-Video: Controllable Text-to-Video Generation with Diffusion Models](https://controlavideo.github.io/)\n\n---\n\n### 4. Humanoid Video Generation & Policy Training (2026 arXiv)\n\n**Recent concurrent work found:**\n\n1. **X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale** (arXiv 2512.04537)\n   - Adapts Wan 2.2 diffusion model for human-to-humanoid video translation\n   - Created 17+ hours of synthetic paired human-humanoid videos via Unreal Engine\n   - Created 60-hour \"robotized\" Ego-Exo4D dataset (3.6M frames) with Tesla Optimus\n   - User studies showed 69% preference for motion consistency and 62.1% for embodiment accuracy\n\n2. **FlowAct-R1: Towards Interactive Humanoid Video Generation** (arXiv 2601.10103)\n   - Real-time interactive humanoid video generation using MMDiT architecture\n   - Enables streaming synthesis with arbitrary durations and low-latency responsiveness\n\n3. **From Generated Human Videos to Physically Plausible Robot Trajectories** (arXiv 2512.05094)\n   - Two-stage pipeline: 4D reconstruction + GenMimic RL policy\n   - Uses weighted keypoint tracking prioritizing end-effectors\n   - Symmetry loss leverages bilateral symmetry to correct errors\n   - Trained on AMASS data via PPO\n\n4. **Rethinking Video Generation Model for the Embodied World** (arXiv 2601.15282)\n   - Comprehensive framework for video generation in embodied AI contexts\n\n**Sources**:\n- [X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale](https://arxiv.org/html/2512.04537v1)\n- [FlowAct-R1: Towards Interactive Humanoid Video Generation](https://arxiv.org/html/2601.10103v1)\n- [From Generated Human Videos to Physically Plausible Robot Trajectories](https://arxiv.org/html/2512.05094)\n- [Rethinking Video Generation Model for the Embodied World](https://arxiv.org/html/2601.15282v1)"
      }
    ],
    "totalDurationMs": 43834,
    "totalTokens": 24749,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 19460,
      "output_tokens": 1435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3847
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1435,
          "cache_read_input_tokens": 19460,
          "cache_creation_input_tokens": 3847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3847,
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
      "otherToolCount": 8
    }
  },
  "sourceToolAssistantUUID": "0a46d38d-39a0-43a8-b69b-e55ded30834b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "8cfb7cf3-50be-42af-a396-48d20d2e08fa",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Review URDF-DiT humanoid kinematic conditioning for CoRL",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c"
}
```

---

### Tool result

_source line 17 · 2026-05-10T11:53:32.757Z_

<details><summary>↩ Tool result · `toolu_01Qj3SRLaVrUGM5JuSd8q8e8`</summary>

```text
Excellent. Now I have comprehensive information. Let me compile the findings.

## Comprehensive Report on Video Diffusion and Humanoid Robot Learning (2024-2026)

### 1. GR00T Dreams (DreamGen): NVIDIA Humanoid Video World Model Policy Training

**What it does:**
DreamGen is a 4-stage pipeline developed by NVIDIA GEAR Lab that addresses the robotics data scarcity problem using video world models to generate synthetic robot trajectories called "neural trajectories." A humanoid robot trained on only teleoperation data from a single pick-and-place task in one environment can then perform 22 new behaviors in both seen and unseen environments.

**Backbone Architecture:**
DreamGen evaluates four video generative models as backbones:
- Cosmos (NVIDIA's world foundation model)
- Wanx 2.1
- Hunyuan
- CogVideoX

These are all **image-to-video diffusion models** that are fine-tuned on target robot embodiments.

**Cosmos Backbone Details (DiT-based):**
Cosmos uses two architectural variants:
- **Diffusion-based WFM**: Built on latent diffusion with a transformer-based denoiser (adapted from DiT) in 7B and 14B parameter sizes
- **Autoregressive-based WFM**: GPT-style transformers (4B-13B parameters)

The diffusion backbone employs:
- 3D patchification of latent video representations
- Hybrid positional embedding with FPS-aware 3D RoPE
- Adaptive layer normalization (ALN) modulated by timesteps
- Query-key normalization to stabilize training
- Cross-attention layers for semantic information (T5-XXL text embeddings)

**Conditioning:**
- **Text conditioning**: Initial frames and language instructions guide the model
- **Image conditioning**: Via classifier-free guidance during inference

**Action Recovery:**
DreamGen recovers pseudo-action sequences using two methods:
1. **Latent Action Model (LAPA)**: Latent action pretraining approach
2. **Inverse Dynamics Model (IDM)**: Extracts actions from generated video frames (similar to OpenAI's VPT approach)

Both IDM and LAPA actions lead to performance boosts across all data regimes.

**Real-world impact:** GR00T N1.5 (built using DreamGen) was developed in 36 hours using the DreamGen blueprint—a task that would have taken nearly three months with manual data collection.

---

### 2. Whole-Body Humanoid Loco-Manipulation Video Generation (2026)

**WholeBodyVLA (ICLR 2026):**

A unified Vision-Language-Action framework enabling large-space humanoid control that learns from action-free egocentric videos.

**Key Technical Approach:**
- **Latent Action Model (LAM)**: Discovers unified latent actions directly from egocentric videos without manual action annotations
- **Architecture**: Encodes egocentric images and language into latent action tokens that decode into:
  - Dual-arm joint actions for manipulation
  - Locomotion commands for whole-body coordination
- **Reinforcement Learning**: Uses loco-manipulation-oriented (LMO) RL policy enabling precise, stable whole-body coordination under disturbances
- **Video-based learning**: Learns from egocentric manipulation and manipulation-aware locomotion videos without action supervision

---

### 3. Diffusion-Based Motion Generation for Humanoid Locomotion (2026)

**Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking:**

**Approach:**
Combines diffusion-based motion generation with RL-based motion tracking in real-time robot control.

**Key Components:**
1. **Motion Generation**: A diffusion model trained on retargeted human motions generates terrain-aware reference motions in real-time
2. **Motion Tracking**: RL-based tracker that outputs physically plausible actions instead of purely kinematic generation
3. **Closed-loop fine-tuning**: Tracker is further refined with frozen motion generator in closed-loop setting

**Real-world validation:** Successfully navigated complex terrain (boxes, hurdles, stairs) on Unitree G1 with onboard perception.

---

### 4. Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models (2025)

**Approach:**
Uses latent diffusion models to generate realistic RGB human-object interaction scenes as intermediate guidance for planning.

**Pipeline:**
1. **LDM-based scene generation**: Uses state-of-the-art LDM (references FLUX) with ordered text prompt sequences
2. **Contact extraction**: 
   - Vision-language models for object detection
   - Segmentation refinement
   - Sampling-based optimization combining semantic scores and object geometries
   - SVD and ICP for contact matching between generated and simulated scenes
3. **Configuration retargeting**: 3D human pose estimation → inverse kinematics → robot joint angles
4. **Trajectory optimization**: 
   - Centroidal dynamics coupled with whole-body kinematics
   - Semi-implicit Euler discretization
   - Contact constraints, friction cones, collision avoidance formulated as nonlinear optimization

**Key contribution**: First pipeline planning both contacts and robot configurations for humanoid loco-manipulation using latent diffusion models, validated on long-horizon scenarios in simulation.

---

### 5. ControlNet-Style Conditioning in Video Diffusion (2024-2025)

**Status: Well-established and widely deployed**

ControlNet-style conditioning has become a standard technique in video diffusion, with multiple frameworks extending it:

**Key Implementations (2024-2025):**

1. **ControlNeXt**: Powerful and efficient method for controllable image and video generation, addressing computational overhead challenges

2. **Video-ControlNet**: Controllable text-to-video diffusion model that:
   - Generates videos conditioned on sequences of control signals (edge, depth maps, etc.)
   - Built on pre-trained conditional text-to-image diffusion
   - Incorporates spatial-temporal self-attention and trainable temporal layers

3. **EasyControl**: Universal framework (2024) that:
   - Enables control with single condition map through condition adapters
   - Propagates and injects condition features
   - Works with Unet-based pre-trained video diffusion models at low computational cost
   - Achieves 152.0 FVD and 19.9 IS gains on UCF101 (sketch-to-video)

4. **EquiVDM + ControlNet**: Base EquiVDM outperforms models with dense frame-level conditioning; performance improves further when paired with ControlNet

**Conclusion:** ControlNet-style conditioning is deeply integrated into modern video diffusion pipelines and represents standard practice for controllable video generation.

---

### 6. Isaac Lab and G1 Humanoid Manipulation Benchmarks (2025-2026)

**Isaac Lab GPU-accelerated framework provides:**

**Task Categories:**
- Classic "Hello World" environments
- Locomotion tasks with terrain curricula and height-scanner perception
- Manipulation tasks: dexterous hand-arm operations and assembly benchmarks
- Navigation: goal-conditioned hierarchical control

**G1-Specific Support:**
- Rough terrain locomotion benchmarks (alongside Agility Robotics Digit humanoid)
- Teleoperation with dexterous retargeting for:
  - Unitree three-finger hand
  - Inspire five-finger hand (translates human hand configs to robot joints)
- New industrial manipulation tasks for policy evaluation

**Recent Developments:**
- **NVIDIA Agile**: Isaac Lab-based engine for humanoid loco-manipulation with sim-to-real-verified workflow for Unitree G1
  - Built-in task configurations
  - Training utilities
  - Deterministic evaluation tools

**Policy Evaluation Framework:**
- Isaac Lab-Arena benchmarks GR00T N family (vision-language-action models) at scale
- Provides comprehensive evaluation infrastructure for generalized humanoid reasoning and skills

---

### 7. Inverse Dynamics Model Domain Gap for Sim-Generated vs. Diffusion-Generated Videos

**Key Findings:**

**Domain Gap Issues Identified (2025-2026):**

1. **Embodiment Gap** (mimic-video, 2025):
   - Extraction from videos prone to significant noise and artifacts
   - Severe embodiment gap when retrofitting human videos for robot control
   - Distribution mismatch: fully denoised video predictions diverge from training data
   - Single-view limitations restrict policies to fixed workspace views

2. **Physics Realism Gaps** (Video Generators are Robot Policies, 2024):
   - Pretrained video models lack accurate physical predictions
   - Failures in tasks requiring object stability estimation
   - Perceptual distribution shifts (color, backgrounds)
   - Behavioral distribution shifts (new objects, unseen tasks)

3. **Cumulative Error Problem** (VAG, 2026):
   - Two-stage pipelines (video generation → action extraction) accumulate errors
   - Temporal misalignment between visual and motor signals
   - Inefficiency and degraded cross-modal consistency

**Solutions Emerging:**

1. **mimic-video approach** (2025):
   - Trains video backbone with Low-Rank Adapters on robotics datasets
   - Action decoder trains on frozen video features using flow matching
   - Samples independent flow times for video and action denoising
   - Addresses distribution mismatch through separate noise schedules

2. **VAG (Dual-Stream Video-Action Generation)** (2026):
   - Joint synchronous denoising of video and action branches
   - Adaptive 3D pooling to compress video latents into global embeddings
   - Rigorously aligned outputs without error accumulation

3. **Domain-Specific Fine-tuning**:
   - Minimizing domain gap via target distribution fine-tuning improves performance
   - Oracle latent conditioning yields near-perfect success even without target distribution finetuning

**Research Note:** While extensive literature exists on sim-to-real domain gaps with traditional IDMs (2018-2020), research specifically comparing IDM performance on diffusion-generated videos vs. simulator-generated videos remains an emerging area. The focus has shifted toward joint video-action generation frameworks that avoid separate IDM application altogether.

---

Sources:
- [DreamGen arXiv](https://arxiv.org/abs/2505.12705)
- [GitHub - NVIDIA/GR00T-Dreams](https://github.com/nvidia/gr00t-dreams)
- [NVIDIA DreamGen Research](https://research.nvidia.com/labs/gear/dreamgen/)
- [GitHub - OpenDriveLab/WholebodyVLA](https://github.com/OpenDriveLab/WholebodyVLA)
- [Isaac Lab Paper](https://arxiv.org/html/2511.04831v1)
- [Cosmos World Foundation Model](https://arxiv.org/html/2501.03575v1)
- [EasyControl - Video Diffusion Control](https://arxiv.org/abs/2408.13005)
- [Physically Consistent Humanoid Loco-Manipulation](https://arxiv.org/abs/2504.16843)
- [mimic-video](https://arxiv.org/abs/2512.15692)
- [Video Generators are Robot Policies](https://arxiv.org/html/2508.00795v1)
- [VAG: Dual-Stream Video-Action Generation](https://arxiv.org/html/2604.09330)
- [Whole-Body Humanoid Locomotion](https://arxiv.org/abs/2604.17335)
- [NVIDIA GR00T N1.5 Blog](https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n-1-6-using-a-sim-to-real-workflow/)
- [Isaac Lab Arena Blog](https://developer.nvidia.com/blog/simplify-generalist-robot-policy-evaluation-in-simulation-with-nvidia-isaac-lab-arena/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17c2bd9d-81bb-4132-88c2-b357d86d2fb8",
  "isSidechain": false,
  "promptId": "2788fdb5-76a8-4a46-a99a-4abad3df867d",
  "type": "user",
  "uuid": "ea981b6c-7036-4d1c-b333-2f865756e81a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the following and report actual paper content:\n\n1. \"GR00T Dreams DreamGen NVIDIA humanoid video world model policy training 2025 2026\" - what exactly does this do? What backbone? What conditioning?\n\n2. \"whole body humanoid loco-manipulation video generation diffusion 2026\" - any papers specifically on whole-body humanoid (not just arm) video generation for policy training?\n\n3. \"ControlNet video diffusion conditioning 2024 2025\" - how widely has ControlNet-style conditioning been applied to video diffusion models? Is it a well-established technique?\n\n4. \"Isaac Lab G1 humanoid manipulation benchmark evaluation 2025 2026\" - what tasks exist on Isaac Lab for G1 humanoid evaluation?\n\n5. \"inverse dynamics model IDM sim to real transfer domain gap robot video\" - any papers on the IDM domain gap problem for sim-generated vs. diffusion-generated videos?\n\nUse web search. Report actual content found, not just paper names.",
    "agentId": "a9517d5359c76a4f1",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent. Now I have comprehensive information. Let me compile the findings.\n\n## Comprehensive Report on Video Diffusion and Humanoid Robot Learning (2024-2026)\n\n### 1. GR00T Dreams (DreamGen): NVIDIA Humanoid Video World Model Policy Training\n\n**What it does:**\nDreamGen is a 4-stage pipeline developed by NVIDIA GEAR Lab that addresses the robotics data scarcity problem using video world models to generate synthetic robot trajectories called \"neural trajectories.\" A humanoid robot trained on only teleoperation data from a single pick-and-place task in one environment can then perform 22 new behaviors in both seen and unseen environments.\n\n**Backbone Architecture:**\nDreamGen evaluates four video generative models as backbones:\n- Cosmos (NVIDIA's world foundation model)\n- Wanx 2.1\n- Hunyuan\n- CogVideoX\n\nThese are all **image-to-video diffusion models** that are fine-tuned on target robot embodiments.\n\n**Cosmos Backbone Details (DiT-based):**\nCosmos uses two architectural variants:\n- **Diffusion-based WFM**: Built on latent diffusion with a transformer-based denoiser (adapted from DiT) in 7B and 14B parameter sizes\n- **Autoregressive-based WFM**: GPT-style transformers (4B-13B parameters)\n\nThe diffusion backbone employs:\n- 3D patchification of latent video representations\n- Hybrid positional embedding with FPS-aware 3D RoPE\n- Adaptive layer normalization (ALN) modulated by timesteps\n- Query-key normalization to stabilize training\n- Cross-attention layers for semantic information (T5-XXL text embeddings)\n\n**Conditioning:**\n- **Text conditioning**: Initial frames and language instructions guide the model\n- **Image conditioning**: Via classifier-free guidance during inference\n\n**Action Recovery:**\nDreamGen recovers pseudo-action sequences using two methods:\n1. **Latent Action Model (LAPA)**: Latent action pretraining approach\n2. **Inverse Dynamics Model (IDM)**: Extracts actions from generated video frames (similar to OpenAI's VPT approach)\n\nBoth IDM and LAPA actions lead to performance boosts across all data regimes.\n\n**Real-world impact:** GR00T N1.5 (built using DreamGen) was developed in 36 hours using the DreamGen blueprint—a task that would have taken nearly three months with manual data collection.\n\n---\n\n### 2. Whole-Body Humanoid Loco-Manipulation Video Generation (2026)\n\n**WholeBodyVLA (ICLR 2026):**\n\nA unified Vision-Language-Action framework enabling large-space humanoid control that learns from action-free egocentric videos.\n\n**Key Technical Approach:**\n- **Latent Action Model (LAM)**: Discovers unified latent actions directly from egocentric videos without manual action annotations\n- **Architecture**: Encodes egocentric images and language into latent action tokens that decode into:\n  - Dual-arm joint actions for manipulation\n  - Locomotion commands for whole-body coordination\n- **Reinforcement Learning**: Uses loco-manipulation-oriented (LMO) RL policy enabling precise, stable whole-body coordination under disturbances\n- **Video-based learning**: Learns from egocentric manipulation and manipulation-aware locomotion videos without action supervision\n\n---\n\n### 3. Diffusion-Based Motion Generation for Humanoid Locomotion (2026)\n\n**Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking:**\n\n**Approach:**\nCombines diffusion-based motion generation with RL-based motion tracking in real-time robot control.\n\n**Key Components:**\n1. **Motion Generation**: A diffusion model trained on retargeted human motions generates terrain-aware reference motions in real-time\n2. **Motion Tracking**: RL-based tracker that outputs physically plausible actions instead of purely kinematic generation\n3. **Closed-loop fine-tuning**: Tracker is further refined with frozen motion generator in closed-loop setting\n\n**Real-world validation:** Successfully navigated complex terrain (boxes, hurdles, stairs) on Unitree G1 with onboard perception.\n\n---\n\n### 4. Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models (2025)\n\n**Approach:**\nUses latent diffusion models to generate realistic RGB human-object interaction scenes as intermediate guidance for planning.\n\n**Pipeline:**\n1. **LDM-based scene generation**: Uses state-of-the-art LDM (references FLUX) with ordered text prompt sequences\n2. **Contact extraction**: \n   - Vision-language models for object detection\n   - Segmentation refinement\n   - Sampling-based optimization combining semantic scores and object geometries\n   - SVD and ICP for contact matching between generated and simulated scenes\n3. **Configuration retargeting**: 3D human pose estimation → inverse kinematics → robot joint angles\n4. **Trajectory optimization**: \n   - Centroidal dynamics coupled with whole-body kinematics\n   - Semi-implicit Euler discretization\n   - Contact constraints, friction cones, collision avoidance formulated as nonlinear optimization\n\n**Key contribution**: First pipeline planning both contacts and robot configurations for humanoid loco-manipulation using latent diffusion models, validated on long-horizon scenarios in simulation.\n\n---\n\n### 5. ControlNet-Style Conditioning in Video Diffusion (2024-2025)\n\n**Status: Well-established and widely deployed**\n\nControlNet-style conditioning has become a standard technique in video diffusion, with multiple frameworks extending it:\n\n**Key Implementations (2024-2025):**\n\n1. **ControlNeXt**: Powerful and efficient method for controllable image and video generation, addressing computational overhead challenges\n\n2. **Video-ControlNet**: Controllable text-to-video diffusion model that:\n   - Generates videos conditioned on sequences of control signals (edge, depth maps, etc.)\n   - Built on pre-trained conditional text-to-image diffusion\n   - Incorporates spatial-temporal self-attention and trainable temporal layers\n\n3. **EasyControl**: Universal framework (2024) that:\n   - Enables control with single condition map through condition adapters\n   - Propagates and injects condition features\n   - Works with Unet-based pre-trained video diffusion models at low computational cost\n   - Achieves 152.0 FVD and 19.9 IS gains on UCF101 (sketch-to-video)\n\n4. **EquiVDM + ControlNet**: Base EquiVDM outperforms models with dense frame-level conditioning; performance improves further when paired with ControlNet\n\n**Conclusion:** ControlNet-style conditioning is deeply integrated into modern video diffusion pipelines and represents standard practice for controllable video generation.\n\n---\n\n### 6. Isaac Lab and G1 Humanoid Manipulation Benchmarks (2025-2026)\n\n**Isaac Lab GPU-accelerated framework provides:**\n\n**Task Categories:**\n- Classic \"Hello World\" environments\n- Locomotion tasks with terrain curricula and height-scanner perception\n- Manipulation tasks: dexterous hand-arm operations and assembly benchmarks\n- Navigation: goal-conditioned hierarchical control\n\n**G1-Specific Support:**\n- Rough terrain locomotion benchmarks (alongside Agility Robotics Digit humanoid)\n- Teleoperation with dexterous retargeting for:\n  - Unitree three-finger hand\n  - Inspire five-finger hand (translates human hand configs to robot joints)\n- New industrial manipulation tasks for policy evaluation\n\n**Recent Developments:**\n- **NVIDIA Agile**: Isaac Lab-based engine for humanoid loco-manipulation with sim-to-real-verified workflow for Unitree G1\n  - Built-in task configurations\n  - Training utilities\n  - Deterministic evaluation tools\n\n**Policy Evaluation Framework:**\n- Isaac Lab-Arena benchmarks GR00T N family (vision-language-action models) at scale\n- Provides comprehensive evaluation infrastructure for generalized humanoid reasoning and skills\n\n---\n\n### 7. Inverse Dynamics Model Domain Gap for Sim-Generated vs. Diffusion-Generated Videos\n\n**Key Findings:**\n\n**Domain Gap Issues Identified (2025-2026):**\n\n1. **Embodiment Gap** (mimic-video, 2025):\n   - Extraction from videos prone to significant noise and artifacts\n   - Severe embodiment gap when retrofitting human videos for robot control\n   - Distribution mismatch: fully denoised video predictions diverge from training data\n   - Single-view limitations restrict policies to fixed workspace views\n\n2. **Physics Realism Gaps** (Video Generators are Robot Policies, 2024):\n   - Pretrained video models lack accurate physical predictions\n   - Failures in tasks requiring object stability estimation\n   - Perceptual distribution shifts (color, backgrounds)\n   - Behavioral distribution shifts (new objects, unseen tasks)\n\n3. **Cumulative Error Problem** (VAG, 2026):\n   - Two-stage pipelines (video generation → action extraction) accumulate errors\n   - Temporal misalignment between visual and motor signals\n   - Inefficiency and degraded cross-modal consistency\n\n**Solutions Emerging:**\n\n1. **mimic-video approach** (2025):\n   - Trains video backbone with Low-Rank Adapters on robotics datasets\n   - Action decoder trains on frozen video features using flow matching\n   - Samples independent flow times for video and action denoising\n   - Addresses distribution mismatch through separate noise schedules\n\n2. **VAG (Dual-Stream Video-Action Generation)** (2026):\n   - Joint synchronous denoising of video and action branches\n   - Adaptive 3D pooling to compress video latents into global embeddings\n   - Rigorously aligned outputs without error accumulation\n\n3. **Domain-Specific Fine-tuning**:\n   - Minimizing domain gap via target distribution fine-tuning improves performance\n   - Oracle latent conditioning yields near-perfect success even without target distribution finetuning\n\n**Research Note:** While extensive literature exists on sim-to-real domain gaps with traditional IDMs (2018-2020), research specifically comparing IDM performance on diffusion-generated videos vs. simulator-generated videos remains an emerging area. The focus has shifted toward joint video-action generation frameworks that avoid separate IDM application altogether.\n\n---\n\nSources:\n- [DreamGen arXiv](https://arxiv.org/abs/2505.12705)\n- [GitHub - NVIDIA/GR00T-Dreams](https://github.com/nvidia/gr00t-dreams)\n- [NVIDIA DreamGen Research](https://research.nvidia.com/labs/gear/dreamgen/)\n- [GitHub - OpenDriveLab/WholebodyVLA](https://github.com/OpenDriveLab/WholebodyVLA)\n- [Isaac Lab Paper](https://arxiv.org/html/2511.04831v1)\n- [Cosmos World Foundation Model](https://arxiv.org/html/2501.03575v1)\n- [EasyControl - Video Diffusion Control](https://arxiv.org/abs/2408.13005)\n- [Physically Consistent Humanoid Loco-Manipulation](https://arxiv.org/abs/2504.16843)\n- [mimic-video](https://arxiv.org/abs/2512.15692)\n- [Video Generators are Robot Policies](https://arxiv.org/html/2508.00795v1)\n- [VAG: Dual-Stream Video-Action Generation](https://arxiv.org/html/2604.09330)\n- [Whole-Body Humanoid Locomotion](https://arxiv.org/abs/2604.17335)\n- [NVIDIA GR00T N1.5 Blog](https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n-1-6-using-a-sim-to-real-workflow/)\n- [Isaac Lab Arena Blog](https://developer.nvidia.com/blog/simplify-generalist-robot-policy-evaluation-in-simulation-with-nvidia-isaac-lab-arena/)"
      }
    ],
    "totalDurationMs": 123575,
    "totalTokens": 37500,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 303,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 33618,
      "output_tokens": 2887,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 692
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 303,
          "output_tokens": 2887,
          "cache_read_input_tokens": 33618,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 692,
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
      "otherToolCount": 24
    }
  },
  "sourceToolAssistantUUID": "17c2bd9d-81bb-4132-88c2-b357d86d2fb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T11:55:03.232Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have extensive research results. Let me also search for a few more critical things:

1. PEVA - "Whole-Body Conditioned Egocentric Video Prediction" (arXiv:2506.21552) - this seems extremely relevant as it conditions on kinematic pose trajectories for video prediction. But the date 2506 would mean June 2026... let me check this.

2. VAG dual-stream video-action generation - this could be important

3. FlowAct-R1 interactive humanoid video generation

4. The resource estimate realism - 35h for ControlNet training, 25h for IDM


5. CoRL 2026 venue constraint vs. target venue being ICLR 2027

I'm noticing some critical overlaps in the literature. PEVA from June 2026 looks particularly relevant since it uses auto-regressive conditional diffusion to condition on kinematic pose trajectories for video prediction—this could be nearly identical to what URDF-DiT is doing. VAG's dual-stream approach for synchronized video-action generation from April 2026 also seems like it could be addressing similar problems.

There's a significant issue though: the venue mislabeling is corrected now with ICLR 2027 as the target, but the user's original constraint explicitly specifies CoRL 2026 with May deadlines. Targeting ICLR 2027 instead represents a major deviation from the stated requirements. On the resource side, the 130-hour manual estimate fits within the 200-hour budget, though I should verify if that's realistic. The domain gap mitigation through domain-randomized rendering and FK residual consistency loss seems reasonable, but I need to assess whether these solutions are actually sufficient.

The ControlNet application to video diffusion for robotics feels more like an engineering contribution than a fundamental algorithmic advance, which could be a weakness. I'm also noticing PEVA's June 2026 date might actually align with the paper deadline, so that's worth reconsidering. Let me break down the compute estimates more carefully to see if the 130-hour projection holds up across the different training phases. Video generation and evaluation at 35h is tight given the model size and inference speed, and ablations at 25h seems especially constrained for running multiple experiments. Looking at the resource breakdown, manual mode stays within the 130h budget while auto-research hits the hard 200h limit exactly. But there's a critical mismatch I'm noticing: the user's target is CoRL 2026 with a May deadline, yet the revised proposal is aiming for ICLR 2027 in October—that's a fundamental misalignment with what they actually need. The user's core requirement was CoRL 2026 with a May 29 deadline, but the revised proposal targets ICLR 2027 instead—that's a fundamental mismatch. I'm also noticing something odd with the PEVA paper dated 2506.21552, which would be June 2026, but today is May 10, 2026, so that shouldn't exist yet. There's likely an error in the search results I need to flag. On the technical side, I'm concerned about using FK heatmaps for a 29+ DoF system since projecting that many joints into 2D creates an extremely dense conditioning signal.

The occlusion problem is significant—many joints get hidden depending on the camera angle, and the proposal doesn't really tackle this. The bigger issue is whether in-loop conditioning is actually the key difference from Dream2Act's 37.5% success rate, or if other factors like training data quality are responsible. The ablation comparing in-loop versus post-hoc conditioning is sound but requires implementing both approaches. There's also the architectural challenge of adapting ControlNet, which was built for U-Net diffusion models, to work with DiT-based video models like Wan 2.2.

I need to verify whether Wan 2.2 is actually open-source and trainable. Looking at the overall assessment, the novelty feels limited—ControlNet-style conditioning is standard, the URDF FK heatmaps are incremental, and EA-WM is a very similar concurrent work. The differentiation around full-body versus arm-only and frozen versus finetuned backbones is valid but narrow. The feasibility score is concerning too; the 35-hour training estimate for ControlNet on Wan 2.2 seems optimistic, and while the sim-to-video domain gap gets some attention, it's still a major unresolved issue.

The real problem is the timeline—hitting all three benchmarks in 20 days for CoRL is completely unrealistic, and even ICLR 2027 is tight for a two-person team. I'm also noticing the proposal targets ICLR 2027 and CoRL 2027, but the user specifically asked for CoRL 2026, which is a direct requirement violation. I should double-check whether the resource estimates have actually been corrected or if this is still an issue.

Looking at the revised estimates, manual mode dropped from ~250h to ~130h across ControlNet training, IDM training, video generation, ablations, and data prep—which finally fits the ≤200h constraint. But I'm skeptical about whether 35 hours is realistic for ControlNet fine-tuning on a 14B video diffusion model, since typical LoRA training on models like Wan 2.1 usually requires 10-30 GPU hours just for images.

For video diffusion with temporal attention, that could easily be 2-4x longer. Similarly, generating 100 evaluation videos at 30 frames each on the Wan 2.2 14B model seems computationally heavy for just 35 hours.

The bigger problems are that the venue shifted from CoRL 2026 to ICLR 2027—directly contradicting the user's stated requirement—and I need to verify whether PEVA (the whole-body egocentric video prediction work) actually exists as concurrent work from May 2026. There's also a lingering novelty question around applying ControlNet to video.

The core issue is that while the URDF FK heatmap conditioning is novel, the technical contribution feels thin—it's essentially standard ControlNet applied to a new signal. The differentiation from EA-WM is narrow too (full-body versus arm-only, ControlNet versus bidirectional fusion), and the IDM domain gap, though better addressed than before, remains risky. The idea does have genuine merit with the full-body humanoid video generation pipeline and explicit IDM training approach, but it fundamentally fails the user's primary venue constraint.

The real problem is the timeline mismatch: the user explicitly targets CoRL 2026 with a May 29 deadline, but this proposal is aimed at ICLR 2027. That's a critical misalignment I need to flag directly. I should give a "revise" verdict with specific, actionable feedback: the proposal must either commit to the CoRL 2026 timeline and explain how that's feasible, or clearly articulate why it can't meet that deadline and what the fallback venue is. Beyond that, the novelty needs strengthening—"same as EA-WM but for whole body" isn't enough—and the proposal should acknowledge PEVA as concurrent work if relevant. I'm checking whether the timeline constraint actually refers to implementation time or days until the deadline—the proposal's manual and HIL modes (4-8 weeks) don't fit a 20-day implementation window, though the auto mode might work with sufficient compute resources, which isn't explicitly confirmed.

The bigger issue is that the proposal has shifted the target venue from CoRL 2026 (May 29 deadline) to ICLR 2027, effectively sidestepping the user's 20-day constraint entirely—this is a direct violation of the stated requirements and needs to be flagged.

On the evaluation side, the proposal does include Dream2Act benchmarks with relevant tasks like ball kicking and bag punching, which aligns with the user's SIM-ONLY MITIGATION requirements, though I should check what the comparison baseline is.

However, there's another mismatch: the user explicitly asked for evaluation on Isaac Lab humanoid manipulation tasks, RoboCasa kitchen with humanoid embodiment, and HumanoidBench, but the proposal only covers Dream2Act benchmarks—these are fundamentally different evaluation environments.

Now looking at the novelty score, the core contribution is using URDF FK heatmaps as conditioning signals for ControlNet on top of a frozen Wan 2.2 backbone to generate full-body humanoid videos. While ControlNet conditioning on video diffusion itself isn't novel, the specific application to 29+ DoF humanoid control through FK heatmaps is genuinely new and distinct from prior work like EA-WM.

For feasibility, the timeline is a critical issue—the proposal requires 4-6 months for manual data collection, 5-8 weeks for HIL, and 1-2 weeks for automated approaches, which far exceeds the stated 20-day constraint. The 35-hour estimate for ControlNet training on a 14B parameter video diffusion model seems optimistic, and the IDM domain gap mitigation strategy is incomplete. Combined with the evaluation scope not matching user requirements, this significantly impacts feasibility.

The proposal is well-structured and clearly articulates its differentiation from prior work with a specific ablation plan, which keeps clarity high. For impact, while addressing whole-body humanoid data scarcity is valuable, the actual contribution—a ControlNet adapter for video diffusion—may have limited scope beyond this specific application.

Averaging the scores gives 3.0, below the 4.0 threshold, so this needs revision. The core problems are the timeline violation against the 20-day hard constraint, the evaluation mismatch with user-specified benchmarks, and the novelty concern around conditioning video diffusion with URDF FK heatmaps when similar approaches like PEVA are emerging. Even the automated mode at 1-2 weeks barely fits within 20 days and requires substantial computational resources. The core issues are clear: the timeline doesn't fit the 20-day constraint even with automation, the resource estimates for ControlNet training seem optimistic, and there's still meaningful risk around the domain gap between IDM pretraining and robotic control. The ControlNet contribution itself is also fairly straightforward—applying an existing technique to a new conditioning signal rather than introducing novel methodology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea981b6c-7036-4d1c-b333-2f865756e81a",
  "isSidechain": false,
  "requestId": "req_011CatqpBwS5yZpaEyhoXNPw",
  "type": "assistant",
  "uuid": "91ad9611-8e84-4c44-b07f-32b00c1bd1f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LzakogKFnvFkFSaQ1DLjj9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1709,
      "cache_creation_input_tokens": 5673,
      "cache_read_input_tokens": 26193,
      "output_tokens": 5300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5673,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1709,
          "output_tokens": 5300,
          "cache_read_input_tokens": 26193,
          "cache_creation_input_tokens": 5673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5673
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

_source line 19 · 2026-05-10T11:55:08.097Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TqM8UQXvgRtVpqphVcrrA2`</summary>

```json
{
  "description": "Verify PEVA paper and check CoRL 2026 timeline feasibility",
  "subagent_type": "Explore",
  "prompt": "I need to verify two specific things for an ML paper review:\n\n1. **Check if PEVA paper exists**: Search for \"PEVA Whole-Body Conditioned Egocentric Video Prediction arXiv 2506.21552\". The arXiv ID 2506 would suggest June 2026, but today is May 10, 2026. Is this paper real? What does it actually do? Does it condition on kinematic pose trajectories for video prediction/generation?\n\n2. **Check if any CoRL 2026 papers deadline is May 29, 2026**: Search for \"CoRL 2026 submission deadline paper deadline\" and \"CoRL 2026 Austin November\". Confirm the actual deadlines for CoRL 2026.\n\n3. **Check Wan 2.2 ControlNet training feasibility**: Search for \"Wan 2.1 OR Wan 2.2 ControlNet training GPU hours time\" or \"Wan video diffusion ControlNet fine-tuning hours\" - what is the actual GPU compute needed to train a ControlNet adapter on Wan-family video diffusion models?\n\n4. **Check for VAG paper**: Search for \"VAG Dual-Stream Video-Action Generation arXiv 2604.09330 April 2026\" - what does this paper do? Does it jointly generate video and actions? Is it relevant to humanoid policy training?\n\nReport actual findings, not speculation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91ad9611-8e84-4c44-b07f-32b00c1bd1f6",
  "isSidechain": false,
  "requestId": "req_011CatqpBwS5yZpaEyhoXNPw",
  "type": "assistant",
  "uuid": "bf2f4194-c8b4-4b56-b83e-74ec755f9655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LzakogKFnvFkFSaQ1DLjj9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1709,
      "cache_creation_input_tokens": 5673,
      "cache_read_input_tokens": 26193,
      "output_tokens": 5300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5673,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1709,
          "output_tokens": 5300,
          "cache_read_input_tokens": 26193,
          "cache_creation_input_tokens": 5673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5673
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "bf2f4194-c8b4-4b56-b83e-74ec755f9655",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Review URDF-DiT humanoid kinematic conditioning for CoRL",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c"
}
```

---

### Tool result

_source line 22 · 2026-05-10T11:55:26.808Z_

<details><summary>↩ Tool result · `toolu_01TqM8UQXvgRtVpqphVcrrA2`</summary>

```text
Excellent! I found actual information on all four items. Here are the verified findings:

## 1. PEVA Paper - CONFIRMED REAL

**Status:** The paper is REAL and currently available.
- **Full Title:** "Whole-Body Conditioned Egocentric Video Prediction"
- **ArXiv ID:** 2506.21552 (timestamped for June 2026, which is in the future from your perspective of May 10, 2026, but this is normal for pre-scheduled arXiv submissions)
- **What it does:** Trains models to predict egocentric video from human actions, conditioning on kinematic pose trajectories structured by the body's joint hierarchy. It's an auto-regressive conditional diffusion transformer trained on the Nymeria dataset.
- **Key feature:** YES - it explicitly conditions on kinematic pose trajectories and learns how physical human actions shape the environment from a first-person point of view.
- **Authors:** Yutong Bai, Danny Tran, Amir Bar, Yann LeCun, Trevor Darrell, and Jitendra Malik
- **Project page:** https://dannytran123.github.io/PEVA/

## 2. CoRL 2026 Deadline - CONFIRMED

**Status:** May 29, 2026 is CORRECT for the paper submission deadline.
- **Abstract deadline:** May 26, 2026 at 11:59 UTC
- **Paper submission deadline:** May 29, 2026 at 11:59 UTC
- **Conference dates:** November 9-12, 2026
- **Location:** Austin, Texas (JW Marriott Austin)
- **Important note:** Deadlines are firm with no accommodations for missing them.

## 3. Wan ControlNet Training - PARTIAL DATA FOUND

**Status:** Specific GPU hour data exists but is limited.
- **Wan 2.1 ControlNet example:** One reported case showed 62k training steps taking ~3 days on a single RTX 3090 GPU (≈72 GPU hours)
- **Wan 2.1 Fun V1.1 14B ControlNet:** Required 8x 80GB H100 GPUs with 77GB peak memory usage
- **Another report:** 20 days to complete one epoch on their dataset setup (significant compute, dataset-dependent)
- **Note:** Actual compute varies substantially based on model size, dataset size, video frame count, and resolution. No standardized benchmark across the literature.

## 4. VAG Paper - CONFIRMED REAL

**Status:** The paper exists and is relevant to humanoid policy training.
- **Full Title:** "VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis"
- **ArXiv ID:** 2604.09330 (April 2026)
- **What it does:** A unified flow-matching-based framework that JOINTLY generates video AND action under visual and language conditioning
- **Problem it addresses:** Scaling robot learning by generating synthetic paired action trajectories (solving the limitation that existing World Models don't provide paired actions)
- **Relevance to humanoid policy:** YES - specifically designed for embodied AI and robot learning, addressing the challenge of collecting task-specific demonstrations for robot training
- **Authors:** From GigaAI, Zhejiang University, Peking University, and others

---

## Summary for Your Review

All four papers exist and are real. PEVA and VAG are particularly relevant to humanoid policy training since they both address embodied action prediction/generation. The CoRL 2026 deadline of May 29 is accurate. For Wan ControlNet training feasibility, expect GPU hours in the range of days to weeks depending on your specific setup, with the most resource-intensive options requiring multiple H100s.

Sources:
- [PEVA arXiv](https://arxiv.org/abs/2506.21552)
- [PEVA Project Page](https://dannytran123.github.io/PEVA/)
- [CoRL 2026](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers/)
- [Wan 2.1 ControlNet GitHub](https://github.com/TheDenk/wan2.1-dilated-controlnet)
- [VAG arXiv](https://arxiv.org/abs/2604.09330)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf2f4194-c8b4-4b56-b83e-74ec755f9655",
  "isSidechain": false,
  "promptId": "2788fdb5-76a8-4a46-a99a-4abad3df867d",
  "type": "user",
  "uuid": "25a83bd1-16b4-4cde-b8f1-122b2de89e82",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two specific things for an ML paper review:\n\n1. **Check if PEVA paper exists**: Search for \"PEVA Whole-Body Conditioned Egocentric Video Prediction arXiv 2506.21552\". The arXiv ID 2506 would suggest June 2026, but today is May 10, 2026. Is this paper real? What does it actually do? Does it condition on kinematic pose trajectories for video prediction/generation?\n\n2. **Check if any CoRL 2026 papers deadline is May 29, 2026**: Search for \"CoRL 2026 submission deadline paper deadline\" and \"CoRL 2026 Austin November\". Confirm the actual deadlines for CoRL 2026.\n\n3. **Check Wan 2.2 ControlNet training feasibility**: Search for \"Wan 2.1 OR Wan 2.2 ControlNet training GPU hours time\" or \"Wan video diffusion ControlNet fine-tuning hours\" - what is the actual GPU compute needed to train a ControlNet adapter on Wan-family video diffusion models?\n\n4. **Check for VAG paper**: Search for \"VAG Dual-Stream Video-Action Generation arXiv 2604.09330 April 2026\" - what does this paper do? Does it jointly generate video and actions? Is it relevant to humanoid policy training?\n\nReport actual findings, not speculation.",
    "agentId": "ab99650b232837b6a",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! I found actual information on all four items. Here are the verified findings:\n\n## 1. PEVA Paper - CONFIRMED REAL\n\n**Status:** The paper is REAL and currently available.\n- **Full Title:** \"Whole-Body Conditioned Egocentric Video Prediction\"\n- **ArXiv ID:** 2506.21552 (timestamped for June 2026, which is in the future from your perspective of May 10, 2026, but this is normal for pre-scheduled arXiv submissions)\n- **What it does:** Trains models to predict egocentric video from human actions, conditioning on kinematic pose trajectories structured by the body's joint hierarchy. It's an auto-regressive conditional diffusion transformer trained on the Nymeria dataset.\n- **Key feature:** YES - it explicitly conditions on kinematic pose trajectories and learns how physical human actions shape the environment from a first-person point of view.\n- **Authors:** Yutong Bai, Danny Tran, Amir Bar, Yann LeCun, Trevor Darrell, and Jitendra Malik\n- **Project page:** https://dannytran123.github.io/PEVA/\n\n## 2. CoRL 2026 Deadline - CONFIRMED\n\n**Status:** May 29, 2026 is CORRECT for the paper submission deadline.\n- **Abstract deadline:** May 26, 2026 at 11:59 UTC\n- **Paper submission deadline:** May 29, 2026 at 11:59 UTC\n- **Conference dates:** November 9-12, 2026\n- **Location:** Austin, Texas (JW Marriott Austin)\n- **Important note:** Deadlines are firm with no accommodations for missing them.\n\n## 3. Wan ControlNet Training - PARTIAL DATA FOUND\n\n**Status:** Specific GPU hour data exists but is limited.\n- **Wan 2.1 ControlNet example:** One reported case showed 62k training steps taking ~3 days on a single RTX 3090 GPU (≈72 GPU hours)\n- **Wan 2.1 Fun V1.1 14B ControlNet:** Required 8x 80GB H100 GPUs with 77GB peak memory usage\n- **Another report:** 20 days to complete one epoch on their dataset setup (significant compute, dataset-dependent)\n- **Note:** Actual compute varies substantially based on model size, dataset size, video frame count, and resolution. No standardized benchmark across the literature.\n\n## 4. VAG Paper - CONFIRMED REAL\n\n**Status:** The paper exists and is relevant to humanoid policy training.\n- **Full Title:** \"VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis\"\n- **ArXiv ID:** 2604.09330 (April 2026)\n- **What it does:** A unified flow-matching-based framework that JOINTLY generates video AND action under visual and language conditioning\n- **Problem it addresses:** Scaling robot learning by generating synthetic paired action trajectories (solving the limitation that existing World Models don't provide paired actions)\n- **Relevance to humanoid policy:** YES - specifically designed for embodied AI and robot learning, addressing the challenge of collecting task-specific demonstrations for robot training\n- **Authors:** From GigaAI, Zhejiang University, Peking University, and others\n\n---\n\n## Summary for Your Review\n\nAll four papers exist and are real. PEVA and VAG are particularly relevant to humanoid policy training since they both address embodied action prediction/generation. The CoRL 2026 deadline of May 29 is accurate. For Wan ControlNet training feasibility, expect GPU hours in the range of days to weeks depending on your specific setup, with the most resource-intensive options requiring multiple H100s.\n\nSources:\n- [PEVA arXiv](https://arxiv.org/abs/2506.21552)\n- [PEVA Project Page](https://dannytran123.github.io/PEVA/)\n- [CoRL 2026](https://www.corl.org/)\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers/)\n- [Wan 2.1 ControlNet GitHub](https://github.com/TheDenk/wan2.1-dilated-controlnet)\n- [VAG arXiv](https://arxiv.org/abs/2604.09330)"
      }
    ],
    "totalDurationMs": 18706,
    "totalTokens": 22327,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 2451,
      "cache_creation_input_tokens": 1931,
      "cache_read_input_tokens": 16906,
      "output_tokens": 1039,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1931
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2451,
          "output_tokens": 1039,
          "cache_read_input_tokens": 16906,
          "cache_creation_input_tokens": 1931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1931,
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
  "sourceToolAssistantUUID": "bf2f4194-c8b4-4b56-b83e-74ec755f9655",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T11:56:08.801Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me formulate my final review.

Key findings:

1. **PEVA (arXiv:2506.21552)**: This is REAL but from June 2026, which is FUTURE relative to today (May 10, 2026). It conditions on kinematic pose trajectories for egocentric video prediction using autoregressive conditional diffusion. This is conceptually related to URDF-DiT but: (a) it's for humans (egocentric first-person), not robot URDF conditioning, (b) it's for prediction not generation, (c) it uses autoregressive diffusion transformer not ControlNet-style. 

Since PEVA is technically from the future, it's not really concurrent work that would affect a May 29 submission timeline.

2. **VAG (arXiv:2604.09330)**: This DOES jointly generate video AND action - addressing a key problem that URDF-DiT's IDM approach tries to solve. VAG jointly denoises video and action sequences. This could be seen as a competitor to the URDF-DiT+IDM pipeline.

3. **CoRL 2026 deadline**: Confirmed May 29, 2026. The proposal targets ICLR 2027 - this is a clear user requirement violation.

4. **Wan ControlNet training**: One case showed ~72 GPU hours on a single RTX 3090. For H100s, that would be significantly less. But the proposed 35h might actually be achievable on H100s.

5. **VAG** is a significant concurrent work that also addresses the joint video+action generation problem - and it's from April 2026, so it's concurrent.

Now I'm noticing a major mismatch in the evaluation setup. The user specified testing on Isaac Lab humanoid manipulation and locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, and HumanoidBench, but the proposal actually evaluates on Dream2Act's ball kicking, bag punching, and box hugging benchmarks instead.

Looking at the scoring more carefully: the URDF FK heatmap conditioning for full-body humanoid video generation is genuinely novel compared to EA-WM's arm-only approach, and applying ControlNet to URDF FK for video diffusion is differentiated from VAG's flow matching approach. That puts novelty around 3/5 - incrementally novel but not groundbreaking. On feasibility though, there's a hard constraint violation with the CoRL 2026 deadline of May 29 versus targeting ICLR 2027, which is a significant problem.

The timeline estimates are concerning: manual and HIL approaches both exceed the constraint window, while the auto approach might barely squeeze in at 1-2 weeks. ControlNet training at 35 hours on H100s is tight but potentially doable, and the IDM domain gap is only partially addressed, bringing feasibility down to 2/5. Clarity is strong at 4/5 with well-articulated contributions and good ablation planning, while impact sits at 3/5 since the contribution may not be sufficient for a top venue despite addressing the important problem of humanoid data scarcity—VAG's joint video and action generation approach could be more elegant. That averages to 3.0 overall.

But there are critical issues: the proposal targets ICLR 2027 when the user explicitly requested CoRL 2026, the timeline doesn't meet the 20-day constraint except possibly in auto mode with 8+ H100s, the evaluation plan uses only Dream2Act benchmarks instead of the required Isaac Lab tasks and RoboCasa, and I'm missing that VAG from April 2026 does joint video-action generation via flow matching—potentially a better alternative to the two-stage URDF-DiT plus IDM pipeline. The IDM domain gap is better handled than before but still incomplete.

I need to decide whether to present a preliminary CoRL 2026 submission or acknowledge why it's infeasible, rather than just shifting to ICLR 2027 without addressing the user's original constraint.

There's also a significant mismatch between the evaluation benchmarks the user specified—Isaac Lab humanoid manipulation, RoboCasa kitchen, HumanoidBench—and what the proposal actually uses, which are Dream2Act whole-body contact tasks. While Dream2Act does provide downstream policy evaluation, it doesn't match the user's stated requirements, and I should flag this discrepancy.

Looking at my assessment, the core issues are the unexplained venue shift from CoRL 2026 to ICLR 2027, the 20-day timeline constraint that isn't met, and the evaluation mismatch. These need to be addressed before this can move forward, so my verdict is revise.

I'm also noticing some additional concerns: the proposal doesn't acknowledge VAG's concurrent work on joint video and action generation, and the ControlNet training estimate of 35 hours might be optimistic. But more critically, I need to clarify what the 20-day constraint actually means—it's explicitly stated as a hard constraint for implementation, and the proposal's 4-6 month manual timeline clearly violates this. Even the auto_research mode timeline seems to extend beyond what's feasible within those bounds.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25a83bd1-16b4-4cde-b8f1-122b2de89e82",
  "isSidechain": false,
  "requestId": "req_011CatqxbXEUfsHFYtVQfBmo",
  "type": "assistant",
  "uuid": "cc7665d4-c90e-4295-86af-1f1afe03d76e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017Js1Y73StTmFEzP4qLQmxK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8050,
      "cache_read_input_tokens": 31866,
      "output_tokens": 4484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8050,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4484,
          "cache_read_input_tokens": 31866,
          "cache_creation_input_tokens": 8050,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8050
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

_source line 24 · 2026-05-10T11:56:53.308Z_

Now I have sufficient research to formulate my verdict. Let me synthesize the findings.

**Critical findings from independent research:**

1. **EA-WM (arXiv:2605.06192)** verified: confirmed it uses bidirectional fusion (NOT ControlNet-style), is arm-only (~14 DoF bimanual). The proposal's differentiation is accurate.

2. **Dream2Act (arXiv:2603.19709)** verified: 37.5% success rate confirmed. Post-hoc URDF-IK confirmed.

3. **VAG (arXiv:2604.09330, April 2026)** - MISSED CONCURRENT WORK: Jointly generates video AND robot actions via dual-stream flow matching, directly addressing the two-stage IDM pipeline problem that URDF-DiT's approach relies on. This is a cleaner solution to the same problem.

4. **PEVA (arXiv:2506.21552, June 2026)**: Real paper that conditions egocentric video generation on kinematic pose trajectories — a related mechanism, though for human (not robot URDF) and using autoregressive diffusion, not ControlNet.

5. **Wan ControlNet training**: Community reports suggest ~72h on RTX 3090 for similar tasks; 35h on H100s is plausible but tight.

6. **CoRL 2026 deadline**: Confirmed May 29, 2026. The proposal now targets ICLR 2027 — a direct violation of the user's explicit requirement.

7. **Evaluation mismatch**: User specified Isaac Lab, RoboCasa, HumanoidBench. Proposal only uses Dream2Act benchmarks.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "URDF FK heatmap conditioning on a frozen Wan 2.2 backbone for full-body humanoid (29+ DoF) video generation is a genuinely novel combination not directly replicated by EA-WM (arm-only, bidirectional fusion) or Dream2Act (post-hoc IK). However, ControlNet-style adapter conditioning on video diffusion is fully standard practice (well-established since 2024), and the novelty reduces to the conditioning signal (URDF FK heatmaps) and embodiment scope — an incremental extension rather than a fundamental algorithmic contribution. VAG (arXiv:2604.09330, April 2026) jointly denoises video and action streams via flow matching, directly competing with the IDM extraction pipeline that is URDF-DiT's second major contribution."
    },
    "feasibility": {
      "score": 2,
      "rationale": "The proposal silently drops CoRL 2026 (user's required venue, deadline May 29) for ICLR 2027, violating both the venue requirement and the ≤20-day implementation constraint (manual: 4–6 months, HIL: 5–8 weeks). Community Wan ControlNet training reports (~72h on RTX 3090 for comparable tasks) suggest the 35h H100 estimate for the ControlNet module is plausible but tight; the evaluation scope (Dream2Act benchmarks only) contradicts the user's specified platforms (Isaac Lab, RoboCasa, HumanoidBench). The FK residual consistency loss as a sim→video domain bridge remains unproven in the literature."
    },
    "clarity": {
      "score": 4,
      "rationale": "The proposal is well-structured, directly addresses all Round 1 issues (EA-WM acknowledged, Kimodo citation replaced, resource plan revised, IDM domain gap technically addressed, venue corrected to ICLR 2027), and clearly articulates three differentiation axes from EA-WM. The ablation plan is specific and directly testable."
    },
    "impact": {
      "score": 3,
      "rationale": "Humanoid data scarcity is a high-impact bottleneck and the problem framing is compelling. However, if VAG's joint video+action generation supersedes the URDF-DiT + IDM two-stage pipeline, and if the FK residual consistency loss fails to bridge the sim→video IDM domain gap, the contribution reduces to a ControlNet adapter on Wan 2.2 for a specific embodiment — an engineering result unlikely to meet the bar for ICLR 2027."
    }
  },
  "issues": [
    "USER REQUIREMENT VIOLATION — TARGET VENUE: The proposal has silently replaced CoRL 2026 (user's explicit target, deadline May 29, 2026) with ICLR 2027 (October 2026 deadline). This violates the primary constraint. The generator must either (a) produce a concrete CoRL 2026 plan with preliminary results achievable in ≤20 days, or (b) explicitly present the infeasibility argument to the user and request venue scope change before proceeding.",
    "USER REQUIREMENT VIOLATION — TIMELINE: Manual mode (4–6 months) and HIL mode (5–8 weeks) both violate the user's ≤20-day hard constraint. Only auto mode with 8+ H100s (1–2 weeks) approaches feasibility. If targeting CoRL 2026, the auto mode timeline with specific GPU allocation must be the primary mode, not the fallback.",
    "USER REQUIREMENT VIOLATION — EVALUATION PLATFORMS: User specified 'Test on Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench.' The proposal evaluates exclusively on three Dream2Act benchmarks (ball kicking, bag punching, box hugging). None of the user's required evaluation platforms are included.",
    "MISSED CRITICAL CONCURRENT WORK — VAG (arXiv:2604.09330, April 2026): VAG (Dual-Stream Video-Action Generation) jointly denoises video and robot action streams via flow matching, directly solving the paired data synthesis problem without a two-stage IDM. This paper is from April 2026 and directly competes with URDF-DiT's IDM extraction pipeline. The proposal's landscape section must acknowledge VAG and explain why URDF-DiT's explicit URDF kinematic conditioning offers advantages over VAG's implicit action learning, otherwise the IDM contribution is largely subsumed.",
    "RESOURCE ESTIMATE CONCERN — ControlNet Training: Community reports indicate Wan-family ControlNet training requires ~72h on RTX 3090 for similar tasks (implied ~35–50h on H100 depending on dataset size). The proposed 35h may be achievable but is at the boundary — the estimate should reflect worst-case sensitivity (e.g., if longer context/temporal attention training increases compute 1.5–2x, the manual budget risks exceeding 200h total).",
    "IDM DOMAIN GAP — MITIGATION UNPROVEN: The FK residual consistency loss during video generation (pulling generated frames toward sim-renderable kinematics) is a reasonable hypothesis but has no empirical precedent specifically for bridging Wan 2.2 generation distribution → Isaac Lab sim rollout distribution for IDM application. The proposal should cite or test whether this loss actually reduces IDM error or whether domain-randomized rendering alone is sufficient."
  ],
  "feedback": "The Round 1 issues with EA-WM acknowledgment, Kimodo mischaracterization, venue labeling, and IDM domain gap are substantially addressed. The technical differentiation from EA-WM is now specific and compelling on three axes (full-body vs. arm-only, ControlNet frozen vs. joint fine-tuning, explicit IDM pipeline vs. no policy output). The remaining blockers are primarily user-requirement alignment issues:\n\n1. **Address the venue/timeline mismatch directly**: If CoRL 2026 (May 29) is genuinely infeasible, say so explicitly and quantify why — e.g., 'ControlNet training requires ≥35h GPU compute + 3 days of debugging + evaluation, totaling ≥20 days even in auto mode, so the earliest feasible venue is CoRL 2027 or ICLR 2027.' Present this to the user as a constraint, not a silent substitution.\n\n2. **Add user-required evaluation platforms**: At minimum, add one Isaac Lab humanoid manipulation task (e.g., G1 pick-and-place or table-top reaching from Isaac Lab humanoid suite) as a downstream policy training target. This directly satisfies user requirements and provides a more standardized comparison point than Dream2Act-only benchmarks.\n\n3. **Acknowledge VAG (arXiv:2604.09330, April 2026)** in the landscape. VAG jointly generates video and action, which avoids the IDM domain gap entirely. URDF-DiT's advantage over VAG is the explicit URDF kinematic constraint (enforcing joint-limit compliance and embodiment geometry) rather than implicit action learning — this distinction must be made explicit.\n\n4. **Tighten the ControlNet compute estimate**: Add a sensitivity analysis — if training takes 50h instead of 35h due to video temporal attention overhead, total manual budget becomes ~150h, still within constraint. This removes the ambiguity in the estimate.\n\n5. **Scope the contribution more precisely for a 20-day auto-mode execution**: If targeting CoRL 2026 is reinstated, the evaluation scope must be reduced to 2 benchmarks (not 3), and the ablation set must be compressed to one primary comparison (in-loop vs. post-hoc), with the ControlNet-vs-bidirectional-fusion ablation deferred to the ICLR 2027 extended submission.",
  "reason": "Three hard user-requirement violations (target venue CoRL 2026 silently dropped for ICLR 2027, 20-day timeline not met in manual/HIL modes, evaluation platforms not matching user spec) and one missed critical concurrent work (VAG April 2026) prevent pass despite strong technical clarity and correct EA-WM differentiation."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc7665d4-c90e-4295-86af-1f1afe03d76e",
  "isSidechain": false,
  "requestId": "req_011CatqxbXEUfsHFYtVQfBmo",
  "type": "assistant",
  "uuid": "d294c3d7-61d6-4cf2-9de1-bd62116005fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017Js1Y73StTmFEzP4qLQmxK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8050,
      "cache_read_input_tokens": 31866,
      "output_tokens": 4484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8050,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4484,
          "cache_read_input_tokens": 31866,
          "cache_creation_input_tokens": 8050,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8050
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d294c3d7-61d6-4cf2-9de1-bd62116005fc",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Review URDF-DiT humanoid kinematic conditioning for CoRL",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d294c3d7-61d6-4cf2-9de1-bd62116005fc",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Review URDF-DiT humanoid kinematic conditioning for CoRL",
  "sessionId": "55c7714a-4eab-4906-93b8-ec7a5460641c"
}
```

---
