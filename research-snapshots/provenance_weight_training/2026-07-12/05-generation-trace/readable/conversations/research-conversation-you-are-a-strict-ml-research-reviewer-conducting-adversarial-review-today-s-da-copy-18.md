# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-3/db3aeea3-bff8-4e0d-8d26-b79997933bd9.jsonl`
- **Structured JSON:** [`b06fb1b210f8f1293b95.json`](../../sessions/b0/b06fb1b210f8f1293b95.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T13:55:15.760Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T13:55:15.760Z",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: Generative models specifically targeting HUMANOID robot training data — addressing the high-DoF, whole-body, loco-manipulation data scarcity that bottlenecks humanoid VLA / WM training. SCOPE LIMITED TO TWO CONTRIBUTION TYPES:\n  (a) Generation ALGORITHMS — e.g., video diffusion conditioned on humanoid action streams, action-conditioned generative models, latent humanoid trajectory generators, physics-aware whole-body video generation.\n  (b) Procedural data-generation PIPELINES — e.g., MimicGen-style automated demo multiplication for humanoids, procedural whole-body task/scene generation, automated quality filtering pipelines for synthetic humanoid trajectories.\n\nOUT OF SCOPE: action retargeting innovations (human-video → humanoid-action retargeting). Treat existing retargeters (HumanPlus, OmniH2O) as black-box upstream tools if needed; do NOT propose new retargeting methods.\n\nRecent landscape (do not duplicate): NVIDIA GR00T-Dreams, DexMimicGen, MimicGen extensions for humanoid, Helix self-supervised humanoid pipelines, Cosmos for synthetic humanoid video. Humanoid data scarcity is the #1 bottleneck cited in 2026 humanoid papers — high impact area.\n\nContribution type: METHOD ONLY. New generation algorithm OR new procedural pipeline. Not a new released humanoid dataset alone.\n\nSIM-ONLY MITIGATION: Validate generated data by training a downstream humanoid policy/VLA in sim and comparing against models trained on baseline data. Frame contribution as method, not dataset.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Strategies: (a) fine-tune existing video diffusion (CogVideoX, OpenSora, Cosmos) with humanoid-action conditioning, (b) procedural pipeline that requires negligible training compute, (c) small efficient humanoid-specific generator that beats general baselines.\n2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos, Isaac Lab humanoid suite (G1, H1), MimicGen, RoboCasa with humanoid embodiments if available.\n3. Eval: train humanoid policy/VLA on generated vs baseline data. Test on Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench. Report success rate + data efficiency curves.\n\nLook for: physics-aware whole-body video generation with kinematic consistency, action-conditioned generators that exploit humanoid kinematic structure, procedural pipelines that produce diverse loco-manipulation (not just static manipulation) data, automatic quality filtering for synthetic humanoid trajectories. Avoid: any retargeting-based contribution, arm-only generation rebadged as humanoid, naive fine-tuning of video diffusion on humanoid clips without method.\n\nTag: direction=humanoid_data_gen, contribution_type=method. target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 9/10)\n{\n  \"title\": \"URDF-DiT: Full-Body Kinematic Conditioning Throughout Video Denoising for Humanoid Whole-Body Contact Training Data\",\n  \"project_name\": \"urdf_dit_loco_policy\",\n  \"source\": \"web_research\",\n  \"level\": \"solid\",\n  \"core_problem\": \"URDF-DiT addresses the challenge of generating kinematically valid synthetic training videos for humanoid whole-body contact tasks at scale. Two design decisions define the system: (A) kinematic constraints are enforced IN-LOOP throughout video denoising — injecting URDF FK heatmaps into Wan 2.2 DiT cross-attention at every step — rather than post-hoc after generation (Dream2Act approach B: 2D pose estimation → 2D-to-3D lifting → URDF-IK applied after all frames are produced); (B) conditioning spans the full 29-DoF kinematic chain (pelvis, legs, torso, arms, hands) rather than end-effector-only (~5 DoF wrist/hand), as in established arm-manipulation approaches.\\n\\nThese design choices are validated by two ablations against the primary downstream metric — Isaac Lab G1 pick-and-place policy success rate — rather than against video quality metrics: (Ablation A) URDF-DiT vs. vanilla Wan 2.2 + post-hoc URDF-IK [same IDM, same downstream training — directly tests in-loop vs. post-hoc kinematic enforcement]; (Ablation B) 29-DoF full-body conditioning vs. end-effector-only conditioning [same IDM, same downstream evaluation — tests whether the full kinematic chain is necessary for whole-body contact task IDM data]. Neither BridgeV2W nor EA-WM tests either comparison — both evaluate video generation quality metrics, not downstream IDM training data quality.\\n\\nThe landscape context: BridgeV2W (arXiv:2602.03793, Feb 2026) and EA-WM (arXiv:2605.06192, May 2026) together establish the ControlNet+URDF+video-DiT paradigm for arm/dual-arm manipulation — validating in-loop URDF-derived conditioning for arm manipulation, but neither evaluates IDM training data quality or full-body humanoid DoF. Dream2Act (arXiv:2603.19709, March 2026) applies post-hoc URDF-IK for kinematic extraction after unconstrained video generation in robot-native visual space, achieving 37.5% on whole-body contact tasks. HumanX (arXiv:2602.02473, Feb 2026) demonstrates a parallel paradigm: XGen synthesizes humanoid loco-manipulation training data via motion retargeting (3D pose estimation → IK optimization to humanoid skeleton) + IsaacGym physics simulation — no video diffusion, no IDM. HumanX validates synthetic humanoid data generation without video diffusion; URDF-DiT's contribution is specific to the video-diffusion → IDM pathway. URDF-DiT is the first system in this pathway to extend full-body 29-DoF FK conditioning to whole-body contact tasks and validate the design choices via downstream policy success rate.\\n\\n⚠️ USER REQUIREMENT TRADEOFF — EXPLICIT FLAG: The user specified three required evaluation platforms: Isaac Lab G1 locomanipulation, HumanoidBench whole-body tasks, and RoboCasa365 humanoid kitchen. The CoRL 2026 scoped submission covers ONLY Isaac Lab G1 locomanipulation (1 of 3 required benchmarks). HumanoidBench and RoboCasa365 are deferred entirely to ICLR 2027. The user should make an explicit decision: (option A) target CoRL 2026 with 1-of-3 benchmark coverage and full results on all three platforms at ICLR 2027; (option B) skip CoRL 2026 entirely and target ICLR 2027 from the start with full user-required benchmark coverage.\",\n  \"opportunity\": \"GR00T-Dreams/DreamGen (2025) validated the video-diffusion → IDM pipeline for tabletop manipulation. Dream2Act (arXiv:2603.19709, March 2026) extended to full-body G1 whole-body contact interaction by generating video in robot-native visual space — hallucinating the G1 robot body via Seedance 2.0 — then applying post-generation kinematic recovery: (a) native 2D pose estimation, (b) 2D-to-3D lifting, (c) URDF-constrained IK. This post-hoc extraction approach achieves 37.5% overall success across four whole-body contact tasks but is inherently corrective: it recovers joint-angle-consistent trajectories from video frames generated without kinematic constraints, which can introduce temporal jitter and joint-limit violations that propagate into IDM training. URDF-DiT addresses this at the source — FK heatmaps injected throughout denoising prevent kinematically infeasible transitions during generation rather than correcting them afterward. Dream2Act's two distinct components — (A) robot-native video generation modality and (B) post-generation URDF-constrained IK — are the baseline against which URDF-DiT's in-loop conditioning is tested.\\n\\nBridgeV2W (arXiv:2602.03793, February 3, 2026) established the ControlNet+URDF+video-DiT paradigm for arm/dual-arm manipulation: it converts coordinate-space robot actions into pixel-aligned binary embodiment masks rendered from URDF and camera parameters, injects them via a ControlNet-style pathway into a pretrained video DiT, and introduces a flow-based motion loss to prevent overfitting to static backgrounds. Evaluated on DROID (single-arm) and AgiBot-G1 (dual-arm) for goal-conditioned planning and policy evaluation. BridgeV2W's conditioning signal is a binary occupancy mask encoding link presence and location — it does not encode individual joint angles, temporal joint-angle transitions, or joint-limit constraints. URDF-DiT applies continuous per-joint Gaussian FK heatmaps, extends to full-body humanoid 29 DoF, and targets IDM synthetic training data generation.\\n\\nEA-WM (arXiv:2605.06192, May 7 2026) validates that in-loop kinematic heatmap injection into Wan 2.2 cross-attention enforces kinematic consistency — using KVAFs (Gaussian heatmaps at projected joint/end-effector positions) via event-aware bidirectional dual-stream fusion. But EA-WM evaluates arm manipulation only (WorldArena benchmark), requires joint fine-tuning of both video and kinematic branches, and produces no policy training output. URDF-DiT extends to full-body 29 DoF with a ControlNet-style frozen backbone (~40% fewer trainable parameters) and adds the IDM→policy pipeline.\\n\\nA concurrent parallel paradigm is established by HumanX (arXiv:2602.02473, February 2026): XGen generates physically plausible humanoid interaction data from human videos via motion retargeting (3D human pose extraction via GVHMR → IK optimization to humanoid skeleton) + physics simulation (IsaacGym for non-contact phases, force-closure optimization for contact), without video diffusion. XMimic is a unified imitation learning framework with teacher-student distillation (no IDM). Evaluates on 10 skills across 5 domains (basketball, football, badminton, cargo pickup, reactive fighting) with zero-shot G1 transfer; achieves 8× higher generalization success than prior methods. HumanX validates synthetic humanoid training data via the simulation paradigm; URDF-DiT's opportunity is specifically the video-diffusion → IDM pathway — testing whether FK-conditioned video generation can produce training data of comparable quality through the video synthesis route.\\n\\nTogether, BridgeV2W (Feb 2026) and EA-WM (May 2026) establish ControlNet+URDF conditioning into video DiTs as a validated paradigm for arm/dual-arm manipulation. The introduction acknowledges both as prior work establishing the paradigm and positions URDF-DiT as the first application to full-body humanoid 29 DoF whole-body contact tasks with explicit IDM training data generation.\\n\\nVAG (arXiv:2604.09330, April 2026) introduces dual-stream flow matching jointly denoising video and action for arm manipulation (7–16 DoF, 45% on AgiBot G1 dual-arm grasping vs. 8% IDM baseline) but explicitly acknowledges in its Limitations and Future Work section that 'video generation has not been influenced by the action branch, wasting beneficial control signals.' EVA (arXiv:2603.17808, March 2026) enforces executability via learned IDM reward signals (RL post-training, soft constraint) on bimanual tabletop tasks — distinct from URDF-DiT's hard geometric constraint at every diffusion step.\\n\\n⚠️ USER REQUIREMENT TRADEOFF: The user required evaluation on Isaac Lab G1 locomanipulation, HumanoidBench, and RoboCasa365. CoRL 2026 covers only Isaac Lab G1 locomanipulation. Full benchmark coverage requires ICLR 2027. This is a deliberate scope decision with direct implications for whether the work meets the user's original requirements at submission time.\\n\\nVENUE/TIMELINE NOTE: Today is May 10, 2026. CoRL 2026 deadline is May 29 — 19 days away. CoRL 2026 is feasible ONLY in auto-research mode with 8+ H100s available from Day 1, scoped to Isaac Lab G1 locomanipulation + Dream2Act ball kicking contextual comparison, with 2 ablations and a concrete Day 14 decision gate (see resource_estimate). Manual mode (4–6 months) and HIL mode (5–8 weeks) are incompatible with CoRL 2026.\",\n  \"landscape\": \"GR00T-Dreams/DreamGen (arXiv 2025): fine-tunes Cosmos-Predict2 with language conditioning; extracts pseudo-actions via IDM or latent action model. No URDF kinematic constraint. Tabletop manipulation only.\\n\\nDream2Act (arXiv:2603.19709, March 2026): Two distinct components must be distinguished — (A) VIDEO GENERATION MODALITY: generates in robot-native visual space by hallucinating the G1 robot body (not retargeting from human video) using Seedance 2.0, achieving morphological consistency; (B) KINEMATIC EXTRACTION: post-generation pipeline applying native 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK to convert pixel-space poses to joint trajectories. Achieves 37.5% overall success across four whole-body contact interaction benchmarks (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%) vs. 0% for conventional retargeting. Primary stated limitation is inference latency as an offline planner. Dream2Act targets zero-shot real-robot execution; URDF-DiT targets synthetic IDM training data generation — complementary goals. Ablation A tests whether in-loop FK conditioning (URDF-DiT) outperforms Dream2Act's post-generation URDF-IK (approach B) for IDM training data quality.\\n\\nHumanX (arXiv:2602.02473, February 2026): 'HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos' — XGen synthesizes physically plausible humanoid training data from human videos via motion retargeting (3D human pose extraction via GVHMR → IK optimization to humanoid skeleton) + physics simulation (IsaacGym for non-contact phases, force-closure optimization for contact phases), without video diffusion. XMimic is a unified imitation learning framework with teacher-student distillation (no IDM). Evaluates on 10 skills across 5 domains (basketball, football, badminton, cargo pickup, reactive fighting) with zero-shot transfer to physical Unitree G1; achieves 8× higher generalization success than prior methods. Key distinction from URDF-DiT: HumanX generates humanoid training data via physics-based motion retargeting from human video — a simulation-space synthesis paradigm; URDF-DiT generates humanoid training data via kinematically constrained RGB video diffusion → IDM — a video-space synthesis paradigm. HumanX does not use video diffusion, has no IDM pipeline, and does not inject kinematic conditioning into a generative model's attention layers. The two approaches are paradigmatically complementary (simulation vs. video diffusion) and both validate synthetic humanoid training data generation. A CoRL reviewer expecting citation of concurrent synthetic humanoid data work should see HumanX cited with this differentiation.\\n\\nBridgeV2W (arXiv:2602.03793, February 3, 2026): 'BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks' — converts coordinate-space robot actions into pixel-aligned binary embodiment masks rendered from URDF and camera parameters, injected via ControlNet-style pathway into a pretrained video DiT; introduces a flow-based motion loss to focus learning on dynamic task-relevant regions and prevent background overfitting; evaluates on DROID (single-arm) and AgiBot-G1 (dual-arm) for goal-conditioned planning and policy evaluation. BridgeV2W establishes the ControlNet+URDF+video-DiT paradigm for arm/dual-arm manipulation. URDF-DiT differentiates on: (a) full-body humanoid 29 DoF (pelvis, legs, torso, arms, hands) vs. arm/dual-arm scope; (b) continuous per-joint Gaussian FK heatmaps encoding joint-angle-specific kinematic structure and joint-limit constraints at every denoising step vs. binary pixel-aligned occupancy masks (encoding link presence/location but not individual joint angles, temporal joint-angle transitions, or joint-limit compliance); (c) IDM synthetic training data generation pipeline targeting whole-body contact tasks vs. goal-conditioned planning and policy evaluation. The introduction acknowledges BridgeV2W alongside EA-WM as establishing the ControlNet+URDF paradigm and positions URDF-DiT as the first extension to full-body humanoid 29 DoF whole-body contact tasks.\\n\\nEA-WM (arXiv:2605.06192, May 2026): 'EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields' — injects Kinematic-to-Visual Action Fields (KVAF: Gaussian heatmaps at projected end-effector/joint locations) via event-aware bidirectional dual-stream fusion into Wan 2.2; evaluates on WorldArena benchmark for arm manipulation tasks; requires joint fine-tuning of both video and kinematic streams; no policy training pipeline (action recovery detection rate ~0.45). Note: 'EA' = Event-Aware, not Embodiment-Aware. Together with BridgeV2W, EA-WM establishes in-loop URDF-derived conditioning into video DiTs as validated for arm manipulation. URDF-DiT differentiates on three empirically testable axes: (a) full-body 29+ DoF vs. arm manipulation — tested by full-body vs. end-effector ablation; (b) ControlNet-style frozen backbone vs. joint fine-tuning — ~40% fewer trainable parameters; (c) explicit IDM→policy pipeline vs. no policy output.\\n\\nVAG (arXiv:2604.09330, April 2026): dual-stream video-action generation using flow matching for tabletop arm manipulation (7–16 DoF); 45% on AgiBot G1 dual-arm grasping vs. 8% ResNet+IDM baseline; no URDF kinematic constraints; authors explicitly acknowledge in the Limitations and Future Work section: 'video generation has not been influenced by the action branch, wasting beneficial control signals.' No full-body humanoid evaluation. URDF-DiT's in-loop FK heatmap injection directly addresses VAG's stated limitation while extending to 29+ DoF whole-body tasks.\\n\\nMotuBrain (arXiv:2604.27792, April 2026): 'MotuBrain: An Advanced World Action Model for Robot Control' — UniDiffuser formulation with three-stream Mixture-of-Transformers (video, action, language) jointly supporting five inference distributions: policy learning, world modeling, video generation, inverse dynamics, and joint video-action prediction; 95%+ average success on RoboTwin 2.0; tops WorldArena EWMScore; adapts to new humanoid embodiments with 50–100 trajectories. URDF-DiT differentiates: MotuBrain targets direct policy learning via joint video-action diffusion using robot-collected trajectory data; URDF-DiT generates FK-constrained synthetic training data in robot-native visual space without requiring robot-collected trajectory fine-tuning data, and validates whether in-loop geometric URDF FK conditioning improves IDM training data quality for whole-body contact tasks.\\n\\nEVA (arXiv:2603.17808, March 2026): closes executability gap via RL post-training using IDM-derived reward signals penalizing embodiment violations (joint-limit violations, velocity/acceleration/jerk penalties); evaluates on RoboTwin 2.0 bimanual manipulation. Key distinction: EVA = learned IDM reward (soft executability constraint via RL post-training); URDF-DiT = explicit geometric URDF FK heatmaps (hard geometric constraint injected at every diffusion step). EVA evaluates bimanual tabletop; URDF-DiT targets full-body 29+ DoF contact interaction.\\n\\nFlowAct-R1 (arXiv:2601.10103, January 2026): 'FlowAct-R1: Towards Interactive Humanoid Video Generation' — real-time interactive digital human character animation via MMDiT chunkwise diffusion with audio/text-based full-body control at 25fps; targets NPC-style animated digital humans for real-time interaction (lip-sync, facial expressions, body gestures), not physical robot embodiment; no URDF kinematic structure, no physical robot joint constraints, no IDM policy extraction pipeline. Differentiation: interactive character animation use case vs. offline robot training data generation; audio/text conditioning vs. geometric URDF FK heatmaps.\\n\\nKStar Diffuser (arXiv:2503.10743, CVPR 2025): URDF-parsed spatial-temporal graph with differentiable FK for bimanual arm action diffusion (68.2% ± 2.1 success with 100 demos vs. 33.9% for PerAct2); operates at the policy/action layer not video synthesis — complementary to URDF-DiT rather than competing.\\n\\nKinema4D (arXiv:2603.16669, March 2026, NTU): 'Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation' — action-conditioned 4D generative simulator that drives a URDF-based 3D robot via kinematics, projects the robot trajectory into a pointmap, then conditions a diffusion transformer to generate synchronized RGB+pointmap world sequences for spatiotemporal simulation (Robo4D-200k dataset, 201k episodes). Key distinction from URDF-DiT: (a) Kinema4D uses a decoupled architecture — URDF kinematics project into pointmap which conditions a separate generative model — rather than injecting FK heatmaps directly into RGB video DiT cross-attention in-loop during denoising; (b) Kinema4D targets 4D spatiotemporal world simulation (synchronized RGB+pointmap sequences for environment reaction dynamics and scene realism) rather than IDM training data generation; (c) Kinema4D provides no IDM extraction pipeline or downstream policy training evaluation. Kinema4D and URDF-DiT are complementary: the former handles 4D world simulation fidelity, the latter targets RGB video generation for IDM policy training data.\\n\\nControllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026): cascaded text-to-2D-skeleton → skeleton-to-video pipeline validates per-frame 2D pose-sequence conditioning in video diffusion for human motion synthesis — closest video-generation analogue to URDF-DiT's conditioning mechanism, but targets human motion not robot URDF kinematics or policy extraction.\\n\\nX-Humanoid (arXiv Dec 2025): replaces human with humanoid in video via Wan 2.2; no URDF constraint injection. MITTY (arXiv 2025): human-to-robot video diffusion without kinematic enforcement. G-DReaM (arXiv 2025): graph-conditioned diffusion for cross-embodiment motion retargeting on motion sequences, not RGB video.\\n\\nHumanoidBench (arXiv:2403.10506, 2024): 27 whole-body tasks (H1/Digit robots, MuJoCo); deferred to ICLR 2027 full paper. RoboCasa365 (arXiv:2603.04356, ICLR 2026): 365 kitchen tasks with humanoid support; deferred to ICLR 2027 full paper.\",\n  \"approach\": \"SYSTEM CONTRIBUTION: URDF-DiT is the first system to inject full-body URDF FK heatmaps into a video DiT throughout the denoising process for humanoid whole-body contact task training data generation, producing a complete IDM → policy training pipeline for 29-DoF whole-body contact tasks. The ControlNet+URDF+video-DiT paradigm is established for arm/dual-arm manipulation by BridgeV2W (arXiv:2602.03793, Feb 2026) and EA-WM (arXiv:2605.06192, May 2026). URDF-DiT extends this paradigm to full-body humanoid 29 DoF — requiring continuous per-joint Gaussian FK heatmaps (not binary occupancy masks) and motivating a ControlNet-style frozen backbone (rather than EA-WM's joint fine-tuning, ~40% fewer trainable parameters). Two key design choices are validated via ablation against downstream Isaac Lab G1 policy success rate:\\n\\nABLATION A (in-loop vs. post-hoc kinematic enforcement): URDF-DiT vs. vanilla Wan 2.2 + post-hoc URDF-IK — same IDM, same downstream Isaac Lab G1 policy training procedure, same evaluation benchmark, only the video source differs. URDF-DiT-generated videos vs. vanilla Wan 2.2 videos post-processed with URDF-IK (the same IK pipeline as Dream2Act's kinematic extraction stage). This measures whether conditioning throughout denoising — preventing kinematically infeasible frame transitions — outperforms correcting them afterward for IDM training data quality. Neither BridgeV2W nor EA-WM tests this comparison: both evaluate video generation quality metrics, not downstream IDM training data quality.\\n\\nABLATION B (full-body 29 DoF vs. end-effector-only scope): Same IDM, same downstream policy evaluation — only the conditioning scope differs. Full-body 29 DoF (pelvis, legs, torso, arms, hands) vs. end-effector-only (~5 DoF wrist/hand positions). End-effector-only conditioning approximates the scope of BridgeV2W (binary arm/hand masks) and EA-WM (arm end-effector heatmaps), both applied to arm manipulation. For whole-body CONTACT tasks (ball kicking, pick-and-place with locomotion), leg and torso kinematics during approach and weight-shifting phases are hypothesized to affect interaction quality in ways that arm-scope conditioning cannot capture. Ablation B tests whether the scope extension from arm manipulation to full-body humanoid is necessary for whole-body contact task IDM data quality — the paper's core experimental differentiation from the BridgeV2W + EA-WM arm-manipulation landscape.\\n\\nARCHITECTURE: URDF-DiT uses a ControlNet-style conditioning module — Wan 2.2 backbone weights fully frozen; only the FK-heatmap encoder and zero-conv injection layers are trained — that encodes per-frame G1 URDF forward-kinematics outputs (all 29 DoF, projected to the camera plane via differentiable FK) as structured Gaussian joint-position heatmaps and injects them into the cross-attention layers of the Wan 2.2 DiT. Unlike EA-WM's event-aware bidirectional dual-stream fusion (requiring joint fine-tuning of both video and kinematic branches) and BridgeV2W's binary occupancy masks (encoding link presence but not individual joint angles or joint-limit constraints), URDF-DiT's continuous per-joint Gaussian heatmaps encode joint-angle-specific kinematic structure and enable the FK residual consistency loss to penalize joint-limit violations at every denoising step. The ControlNet-style frozen backbone concentrates all learning in the conditioning module, reducing trainable parameters ~40% versus EA-WM's architecture — enabling the full pipeline within ≤200 H100-hours. Full-body G1 scope (29 DoF: pelvis, legs, torso, arms, hands) is the embodiment extension validated by Ablation B.\\n\\nDIFFERENTIATING DREAM2ACT PRECISELY: Dream2Act operates as follows: (A) video generation modality = robot-native visual space (Seedance 2.0 hallucinating the G1 body for morphological consistency — not retargeting from human video); (B) kinematic extraction = post-generation pipeline applying 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK (applied AFTER all video frames are generated). URDF-DiT vs. Dream2Act is not a comparison of visual generation approach — both generate in robot-native-compatible space — but specifically a test of whether kinematic constraints applied IN-LOOP during denoising (URDF-DiT) produce better IDM training data than constraints applied POST-GENERATION (Dream2Act's approach B).\\n\\nJoint-angle sequences are sampled from an Isaac Lab G1 motion library covering locomotion primitives and upper-body reach plans, projected onto the camera plane, and encoded as per-frame kinematic tokens injected into DiT cross-attention.\\n\\nFK RESIDUAL LOSS: A per-frame FK residual consistency loss penalizes deviations between joint positions in generated video frames and URDF FK predictions from the conditioning signal. This is a kinematic consistency mechanism operating on geometric structure — reducing temporal joint jitter, preventing joint-limit violations during denoising. It is NOT a visual domain gap bridge. The visual appearance domain gap between Wan 2.2 outputs and Isaac Lab rendering is separately addressed via domain-randomized Isaac Lab rendering during IDM training (sampling lighting, camera noise, surface material variation to statistically overlap with Wan 2.2's output distribution). Two distinct mechanisms for two distinct problems.\\n\\nThe sim-bootstrapped IDM is trained on (frame_t, frame_{t+k}, joint-velocity) tuples from G1 Isaac Lab rollouts under domain-randomized conditions, then applied zero-shot to URDF-DiT-generated videos. If domain gap remains too large (joint-limit violation rate >15% in generated videos at the 3-day checkpoint), a contingency IDM adapter fine-tuned on ~200 URDF-DiT frame pairs matched to Isaac Lab rollouts via kinematic alignment (~8h additional compute) activates.\\n\\nEVALUATION STRATEGY:\\n\\n(1) CoRL 2026 scoped (2 benchmarks, 2 ablations): Isaac Lab G1 locomanipulation pick-and-place (primary); Dream2Act ball kicking (contextual comparison — 40% success, distinct use case: zero-shot real-robot execution vs. synthetic training data); Ablation A (in-loop URDF-DiT vs. post-hoc vanilla Wan 2.2 + URDF-IK); Ablation B (29 DoF full-body vs. end-effector-only). NOTE: covers 1 of 3 user-required benchmarks.\\n\\n(2) ICLR 2027 full paper (all user-required platforms): Isaac Lab G1 locomanipulation (multi-task: pick-and-place, reaching, pick-navigate-place); HumanoidBench H1 whole-body (carry + cabinet); RoboCasa365 humanoid kitchen (pick-and-place in kitchen); Dream2Act ball kicking + bag punching; Ablations A and B plus: ControlNet-style frozen backbone vs. EA-WM-style event-aware bidirectional fusion; URDF-DiT geometric FK conditioning vs. EVA-style learned IDM reward.\",\n  \"resource_estimate\": {\n    \"corl2026_scoped_auto\": {\n      \"gpu_hours\": \"~130h H100 total compute (compressed to ~12–18h wall clock on 8 H100s)\",\n      \"gpu_utilization\": \"Near-zero idle (~88–92% effective utilization) — agent queues IDM training immediately after ControlNet training checkpoint and runs evaluation generation in parallel\",\n      \"timeline\": \"19 days (May 10 → May 29, 2026 CoRL deadline) with 8+ H100s available from Day 1\",\n      \"team\": \"0 (4h Day 1 setup: Isaac Lab G1 motion library, domain-randomized rendering, URDF-DiT scaffold, evaluation harness)\",\n      \"estimated_gpu_cost\": \"~$416 (130h × $3.20/hr) spread across 8 GPUs\",\n      \"day_by_day_plan\": \"Day 1: env setup (Isaac Lab G1, Wan 2.2 base, eval harness). Days 2–3: implement FK heatmap encoder + zero-conv injection layers for Wan 2.2 cross-attention; simultaneously implement vanilla Wan 2.2 + post-hoc URDF-IK baseline for Ablation A. Days 3–5: ControlNet module training 35–50h GPU compute (~5–7h wall clock on 8 H100s). Days 4–5: IDM training in parallel (~25h GPU, ~3h wall clock). Days 5–8: generate 200 evaluation videos from URDF-DiT and 200 from vanilla Wan 2.2 baseline (~35h GPU, ~5h wall clock). Days 7–11: Isaac Lab G1 policy evaluation on trajectories from both sources (simulation rollouts — wall-clock bottleneck: parallel episode execution). Days 8–12: Ablation B (29 DoF vs. end-effector-only, same IDM, same downstream policy evaluation) + Dream2Act ball kicking contextual comparison. Days 12–14: results analysis and Day 14 DECISION GATE (see pivot_criteria below). Days 14–19: agent-assisted LaTeX drafting of all paper sections (introduction, related work, method, experiments) — auto mode includes full concurrent section generation starting Day 14.\",\n      \"pivot_criteria\": {\n        \"description\": \"Day 14 decision gate with concrete metric thresholds. Calibration anchor: Isaac Lab G1 pick-and-place with Robomimic from clean teleoperation demos achieves 92% success; IDM extraction from generated video will yield substantially lower rates due to visual noise and trajectory imprecision. Thresholds are set relative to the vanilla Wan 2.2 + post-hoc URDF-IK baseline, not absolute performance.\",\n        \"submit_to_corl\": {\n          \"condition\": \"ALL of the following: (1) URDF-DiT trained policy success rate ≥ 20% on Isaac Lab G1 pick-and-place (establishes non-trivial absolute performance from generated data); (2) URDF-DiT > vanilla Wan 2.2 + post-hoc URDF-IK baseline by ≥ 5 percentage points (establishes in-loop conditioning advantage — Ablation A is positive); (3) joint-limit violation rate in URDF-DiT generated videos ≤ 10% (validates FK conditioning is working geometrically)\",\n          \"strong_submission_additionally\": \"Full-body 29 DoF conditioning ≥ end-effector-only conditioning by ≥ 5 pp on downstream policy success (Ablation B strongly positive — validates the 29 DoF scope claim empirically, differentiating from BridgeV2W and EA-WM arm-robot conditioning scope)\"\n        },\n        \"submit_with_reframing\": {\n          \"condition\": \"Ablation A positive (URDF-DiT ≥ baseline + 5 pp) AND absolute success ≥ 20% AND violation rate ≤ 10% — but Ablation B shows < 3 pp improvement from full-body vs. end-effector-only conditioning.\",\n          \"reframing\": \"If Ablation B < 3 pp, the paper cannot claim 'full-body 29 DoF conditioning is necessary' — this would effectively validate that arm-scope conditioning (as in BridgeV2W, EA-WM) suffices for humanoid whole-body contact tasks. However, if Ablation A remains strongly positive (≥ 5 pp), the paper can be reframed around Ablation A as its primary novel contribution: 'in-loop FK conditioning outperforms post-hoc URDF-IK for IDM training data quality on whole-body contact tasks.' Neither BridgeV2W nor EA-WM test this comparison, so Ablation A remains a genuinely novel empirical finding. The reframed paper leads with Ablation A and treats Ablation B as a negative result that simplifies the conditioning design recommendation.\",\n          \"critical_caveat\": \"⚠️ If Ablation B < 3 pp AND Ablation A is also weak (< 5 pp improvement over baseline), pivot directly to ICLR 2027 — no CoRL-level contribution remains. Do NOT attempt CoRL reframing if both ablations are inconclusive.\"\n        },\n        \"pivot_to_iclr_2027\": {\n          \"condition\": \"ANY of the following: (1) URDF-DiT fails to exceed baseline by ≥ 5 pp (Ablation A inconclusive); (2) joint-limit violation rate > 15% in URDF-DiT generated videos (FK conditioning not working — triggers IDM adapter contingency, but if adapter also fails, pivot); (3) absolute policy success < 15% (IDM domain gap too large for 19-day timeline); (4) contingency IDM adapter required AND results still negative after adapter training; (5) Ablation A < 5 pp AND Ablation B < 3 pp simultaneously (both ablations inconclusive — no CoRL-level claim survives)\",\n          \"note\": \"ICLR 2027 pivot preserves all GPU investment — same implementation, full benchmark coverage (all 3 user-required platforms), full ablation suite including ControlNet-vs.-EA-WM-fusion and geometric-FK-vs.-EVA-RL comparisons. Pivot to ICLR 2027 is not a failure; it is the correct decision if CoRL results do not meet the above thresholds.\"\n        }\n      },\n      \"scope\": \"2 benchmarks (Isaac Lab G1 locomanipulation + Dream2Act ball kicking contextual comparison), 2 ablations (A: in-loop URDF-DiT vs. post-hoc vanilla Wan 2.2 + URDF-IK; B: full-body 29 DoF vs. end-effector-only conditioning). HumanoidBench and RoboCasa365 deferred to ICLR 2027. NOTE: covers 1 of 3 user-required benchmarks.\",\n      \"feasibility_risk\": \"HIGH. Estimated 60–70% probability of obtaining submittable results by May 29 in auto mode. Key risks: (1) ControlNet training non-convergence adds 1–2 days; (2) IDM domain gap exceeds FK residual loss + domain randomization, triggering 8h contingency adapter; (3) Isaac Lab simulation evaluation wall-clock bottleneck if environment resets are slow. Day 14 decision gate with concrete thresholds provides an unambiguous pivot trigger.\",\n      \"requirement\": \"8+ H100s available from Day 1 (May 10). If fewer than 8 GPUs are available, wall-clock time increases proportionally and May 29 deadline becomes infeasible — target ICLR 2027.\"\n    },\n    \"manual\": {\n      \"note\": \"ICLR 2027 full paper mode (full coverage of all 3 user-required benchmarks). Incompatible with CoRL 2026 deadline.\",\n      \"gpu_hours\": \"~130–150h H100 (sensitivity-adjusted: ControlNet training 35–70h + IDM 25h + video generation/eval 35h + ablations 25h + data prep 10h)\",\n      \"gpu_utilization\": \"HIGH idle rate (~40–50% effective utilization) — sequential experiment launches and human debugging\",\n      \"timeline\": \"4–6 months (ICLR 2027 submission ~October 2026)\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$416–$480 (130–150h × $3.20/hr)\",\n      \"breakdown\": \"ControlNet module training: 35–70h; IDM training (Isaac Lab G1 rollouts + domain-randomized rendering): ~25h; Video generation + evaluation (Isaac Lab + HumanoidBench + RoboCasa365 + Dream2Act contextual): ~35h; Ablations A, B, ControlNet-vs.-bidirectional-fusion, geometric-FK-vs.-EVA-RL: ~25h; Data prep: ~10h. At 70h worst case for ControlNet: total ~165h, within 200h cap.\",\n      \"benchmark_coverage\": \"FULL — Isaac Lab G1 locomanipulation, HumanoidBench H1 whole-body, RoboCasa365 humanoid kitchen. Meets all 3 user-required benchmarks.\"\n    },\n    \"human_in_loop\": {\n      \"note\": \"ICLR 2027 full paper mode. Incompatible with CoRL 2026 deadline.\",\n      \"gpu_hours\": \"~160h H100\",\n      \"gpu_utilization\": \"Moderate (~60–65% effective utilization)\",\n      \"timeline\": \"5–8 weeks (ICLR 2027 submission ~October 2026)\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"~$150–300 (Opus, ~1,500–2,000 conversation turns)\",\n      \"estimated_gpu_cost\": \"~$512 (160h × $3.20/hr)\",\n      \"risk_note\": \"Human oversight detects IDM domain-gap failure at 2-week checkpoint, activates contingency IDM adapter (~8h additional compute) before remaining budget is spent.\",\n      \"benchmark_coverage\": \"FULL — all 3 user-required benchmarks.\"\n    },\n    \"auto_research\": {\n      \"note\": \"ICLR 2027 full paper mode (all user-required evaluation platforms). For CoRL 2026 scoped version, see corl2026_scoped_auto above.\",\n      \"gpu_hours\": \"~200h H100 (covers full ablation suite: Ablation A, Ablation B, ControlNet-style vs. EA-WM bidirectional fusion, geometric FK vs. EVA-style RL reward, IDM backbone comparisons, FK heatmap resolution variants)\",\n      \"gpu_utilization\": \"Near-zero idle (~88–92% effective utilization)\",\n      \"timeline\": \"1–2 weeks with 8+ H100s; 3–4 weeks on 4 GPUs\",\n      \"team\": \"0 (initial setup ~4h)\",\n      \"claude_api_cost\": \"~$400–700 (Opus, ~4,000–7,000 turns)\",\n      \"estimated_gpu_cost\": \"~$640 (200h × $3.20/hr)\",\n      \"benchmark_coverage\": \"FULL — all 3 user-required benchmarks (Isaac Lab G1 locomanipulation multi-task, HumanoidBench H1 whole-body, RoboCasa365 humanoid kitchen).\",\n      \"risk_note\": \"Automated evaluation harness must include per-frame kinematic consistency checks (FK residual, joint-limit violation rate, temporal flicker score) alongside task success. If FK residual loss is insufficient for IDM domain transfer (joint-limit violation rate >15%), agent triggers IDM adapter contingency (~8h) automatically.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (paper deadline May 29, 2026 — 19 days from today): FEASIBLE only in auto-research mode with 8+ H100s available starting May 10. ⚠️ COVERS ONLY 1 OF 3 USER-REQUIRED BENCHMARKS (Isaac Lab G1 locomanipulation only; HumanoidBench and RoboCasa365 deferred to ICLR 2027). Scoped to 2 ablations: (A) in-loop URDF-DiT vs. post-hoc vanilla Wan 2.2 + URDF-IK extraction; (B) full-body 29 DoF vs. end-effector-only conditioning. Introduction acknowledges BridgeV2W (Feb 2026) + EA-WM (May 2026) as establishing ControlNet+URDF for arm/dual-arm robots; positions URDF-DiT as first extension to full-body humanoid 29 DoF whole-body contact tasks. Day 14 decision gate: submit if URDF-DiT ≥ 20% success AND ≥ 5 pp improvement over baseline AND joint-limit violation rate ≤ 10%; pivot to ICLR 2027 otherwise. Reframing contingency: valid ONLY if Ablation A ≥ 5 pp regardless of Ablation B result; if both ablations inconclusive, pivot directly to ICLR 2027. Estimated 60–70% probability of submittable results by deadline. If Day 14 shows negative results, same implementation pivots to ICLR 2027 with no wasted GPU investment.\",\n    \"ICLR 2027 (expected submission deadline ~October 2026; official announcement pending at iclr.cc): RECOMMENDED if full user-required benchmark coverage is the priority. Covers all 3 required platforms (Isaac Lab G1 locomanipulation, HumanoidBench H1 whole-body, RoboCasa365 humanoid kitchen) and full ablation suite (A, B, ControlNet-vs.-bidirectional-fusion, geometric-FK-vs.-EVA-RL). All operation modes (manual 4–6 months, HIL 5–8 weeks, auto 1–2 weeks on 8 H100s) are compatible.\",\n    \"CoRL 2027 (fallback if ICLR 2027 results are negative)\"\n  ],\n  \"key_references\": [\n    \"DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories (arXiv 2025)\",\n    \"Dream2Act (arXiv:2603.19709, March 2026) — TWO DISTINCT COMPONENTS: (A) video generation modality: robot-native visual space by hallucinating G1 robot body via Seedance 2.0 (not retargeting from human video); (B) kinematic extraction: post-generation pipeline via 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK. Achieves 37.5% success (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%); inference latency is primary stated limitation; targets zero-shot real-robot execution. URDF-DiT Ablation A tests whether in-loop FK conditioning outperforms Dream2Act's approach (B) for synthetic IDM training data quality.\",\n    \"HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos (arXiv:2602.02473, February 2026) — XGen generates physically plausible humanoid training data from human videos via motion retargeting (3D human pose extraction via GVHMR → IK optimization to humanoid skeleton) + physics simulation (IsaacGym for non-contact phases, force-closure optimization for contact phases), without video diffusion; XMimic is a unified imitation learning framework with teacher-student distillation (no IDM). Evaluates on 10 skills across 5 domains (basketball, football, badminton, cargo pickup, reactive fighting) with zero-shot transfer to physical Unitree G1; achieves 8× higher generalization success than prior methods. Key distinction from URDF-DiT: HumanX = physics-based motion retargeting from human video (simulation-space synthesis paradigm, no IDM); URDF-DiT = kinematically constrained RGB video diffusion → IDM (video-space synthesis paradigm). Cited as concurrent work demonstrating synthetic humanoid training data viability via the simulation pathway — URDF-DiT's contribution is specific to the video-diffusion → IDM pathway.\",\n    \"BridgeV2W (arXiv:2602.03793, February 3, 2026) — establishes ControlNet+URDF+video-DiT paradigm for arm/dual-arm manipulation: converts coordinate-space actions to pixel-aligned binary embodiment masks rendered from URDF + camera parameters → ControlNet pathway → pretrained video DiT; flow-based motion loss prevents background overfitting; evaluates on DROID (single-arm) and AgiBot-G1 (dual-arm) for goal-conditioned planning and policy evaluation. URDF-DiT differentiates: (a) full-body humanoid 29 DoF vs. arm/dual-arm scope; (b) continuous per-joint Gaussian FK heatmaps encoding joint-angle-specific kinematic structure and joint-limit constraints vs. binary pixel-aligned occupancy masks encoding link presence/location only; (c) IDM synthetic training data generation pipeline vs. goal-conditioned planning and policy evaluation.\",\n    \"EA-WM (arXiv:2605.06192, May 2026) — primary concurrent work; injects KVAF kinematic heatmaps into Wan 2.2 via event-aware bidirectional dual-stream fusion; WorldArena benchmark for arm manipulation; requires joint fine-tuning of both branches; no policy training pipeline. Note: 'EA' = Event-Aware, not Embodiment-Aware. Together with BridgeV2W, establishes in-loop URDF-derived conditioning into video DiTs for arm manipulation. URDF-DiT differentiators are empirically testable: full-body 29 DoF vs. arm manipulation (Ablation B), ControlNet frozen backbone vs. joint fine-tuning (~40% fewer trainable parameters), explicit IDM→policy pipeline.\",\n    \"VAG (arXiv:2604.09330, April 2026) — jointly denoises video+action via flow matching for tabletop arm manipulation (7–16 DoF); 45% on AgiBot G1 dual-arm grasping vs. 8% IDM baseline; no URDF kinematic constraints; authors explicitly acknowledge in the Limitations and Future Work section: 'video generation has not been influenced by the action branch, wasting beneficial control signals.' URDF-DiT's FK heatmap injection directly addresses this limitation while extending to 29+ DoF.\",\n    \"MotuBrain (arXiv:2604.27792, April 2026) — UniDiffuser + three-stream Mixture-of-Transformers (video, action, language) supporting five inference distributions including inverse dynamics and joint video-action prediction; 95%+ on RoboTwin 2.0; tops WorldArena EWMScore; adapts to new humanoid embodiments with 50–100 trajectories. URDF-DiT differentiates: MotuBrain targets direct policy learning via joint video-action diffusion using robot-collected trajectory data; URDF-DiT generates FK-constrained synthetic training data in robot-native visual space without robot-trajectory fine-tuning.\",\n    \"EVA (arXiv:2603.17808, March 2026) — executability via RL post-training using IDM-derived reward signals; evaluates bimanual tabletop. Key distinction: EVA = soft learned reward constraint; URDF-DiT = hard geometric FK constraint at every diffusion step. ICLR 2027 ablation directly compares these two executability enforcement approaches.\",\n    \"FlowAct-R1 (arXiv:2601.10103, January 2026) — real-time interactive digital human character animation via MMDiT chunkwise diffusion with audio/text-based full-body control at 25fps; targets NPC-style animated digital humans (lip-sync, expressions, body gestures), not physical robot embodiment; no URDF kinematic constraints, no robot joint angles, no IDM policy extraction pipeline.\",\n    \"KStar Diffuser (arXiv:2503.10743, CVPR 2025) — URDF-parsed spatial-temporal graph with differentiable FK for bimanual action diffusion (68.2% vs. 33.9% for PerAct2); policy layer not video synthesis; complementary.\",\n    \"Kinema4D (arXiv:2603.16669, March 2026, NTU): 'Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation' — action-conditioned 4D generative simulator that drives a URDF-based 3D robot via kinematics, projects the robot trajectory into a pointmap, then conditions a diffusion transformer to generate synchronized RGB+pointmap world sequences for spatiotemporal simulation (Robo4D-200k dataset, 201k episodes). Key distinction from URDF-DiT: (a) decoupled architecture — URDF kinematics project into pointmap which conditions a separate generative model, rather than injecting FK heatmaps directly into RGB video DiT cross-attention in-loop during denoising; (b) targets 4D spatiotemporal world simulation (synchronized RGB+pointmap sequences for environment reaction dynamics) rather than IDM training data generation; (c) no IDM extraction pipeline or downstream policy training evaluation. Kinema4D and URDF-DiT are complementary: the former handles 4D world simulation fidelity, the latter targets RGB video generation for IDM policy training data.\",\n    \"Controllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026) — validates per-frame 2D skeleton-sequence conditioning in video diffusion for human motion synthesis; closest video-generation analogue to URDF-DiT's conditioning mechanism; targets human motion not robot URDF kinematics or policy extraction.\",\n    \"HumanoidBench (arXiv:2403.10506, 2024) — 27 tasks (H1/Digit, MuJoCo); ICLR 2027 cross-embodiment evaluation target.\",\n    \"RoboCasa365 (arXiv:2603.04356, ICLR 2026) — 365 kitchen tasks with humanoid support; ICLR 2027 household generalization evaluation.\",\n    \"X-Humanoid (arXiv Dec 2025); MITTY (arXiv 2025); G-DReaM (arXiv 2025)\"\n  ],\n  \"description\": \"URDF-DiT generates kinematically valid synthetic training videos for humanoid whole-body contact tasks by injecting 29-DoF URDF FK heatmaps into Wan 2.2 DiT cross-attention throughout the denoising process, then extracting joint-velocity actions via IDM for downstream policy training on Isaac Lab G1. Two design decisions are validated via ablation against downstream policy success rate: (A) in-loop FK conditioning throughout denoising vs. post-hoc URDF-IK applied to unconstrained video; (B) full-body 29-DoF conditioning vs. end-effector-only conditioning.\\n\\n⚠️ USER REQUIREMENT TRADEOFF: The user required evaluation on three platforms — Isaac Lab G1 locomanipulation, HumanoidBench whole-body tasks, and RoboCasa365 humanoid kitchen. The CoRL 2026 submission covers ONLY Isaac Lab G1 locomanipulation (1 of 3). The user must decide: (A) target CoRL 2026 with partial benchmark coverage now + ICLR 2027 for full coverage; or (B) skip CoRL 2026 and target ICLR 2027 directly with full coverage from the start. This is not a footnote — it is a deliberate scope decision.\\n\\nThe ControlNet+URDF+video-DiT paradigm for arm/dual-arm manipulation is established: BridgeV2W (arXiv:2602.03793, Feb 2026) injected URDF-rendered binary pixel-aligned embodiment masks via ControlNet into a pretrained video DiT for goal-conditioned planning on DROID and AgiBot-G1 dual-arm; EA-WM (arXiv:2605.06192, May 2026) injected per-joint Gaussian heatmaps (KVAFs) into Wan 2.2 via event-aware bidirectional fusion for arm manipulation on WorldArena. The introduction acknowledges both as prior work establishing the paradigm and positions URDF-DiT as the first extension to full-body humanoid 29-DoF whole-body contact tasks with explicit IDM training data generation.\\n\\nKey landscape context: Dream2Act (arXiv:2603.19709) generates in robot-native visual space then applies post-generation URDF-IK (approach B) — Ablation A tests whether in-loop FK conditioning outperforms this for IDM data quality, a comparison neither BridgeV2W nor EA-WM makes. HumanX (arXiv:2602.02473, Feb 2026) demonstrates a parallel synthesis paradigm: XGen (motion retargeting + IsaacGym physics simulation, no video diffusion) + XMimic (imitation learning, no IDM), achieving 8× generalization improvement on sports/cargo tasks with zero-shot G1 transfer — a physics-simulation paradigm complementary to URDF-DiT's video-diffusion paradigm, cited as concurrent work validating synthetic humanoid training data generation. Kinema4D (arXiv:2603.16669, March 2026, NTU) generates synchronized RGB+pointmap sequences via URDF-driven kinematics projected into pointmaps conditioning a diffusion transformer — a decoupled 4D world simulation architecture, distinct from URDF-DiT's in-loop FK injection into RGB video DiT cross-attention and IDM extraction pipeline.\\n\\nKey technical differentiators: (1) vs. Dream2Act: in-loop kinematic constraint enforcement (URDF-DiT) vs. post-generation kinematic extraction (Dream2Act approach B) — tested directly by Ablation A; (2) vs. BridgeV2W + EA-WM: continuous per-joint Gaussian FK heatmaps encoding joint angles and joint-limit constraints (not binary occupancy masks), ControlNet-style frozen backbone (~40% fewer trainable parameters than EA-WM), full-body 29-DoF scope, explicit IDM→policy pipeline; (3) vs. HumanX: video-diffusion paradigm (URDF-DiT) vs. physics-simulation paradigm (HumanX) — paradigmatically distinct, both validate synthetic humanoid training data generation; (4) FK residual consistency loss enforces kinematic geometry during denoising; visual domain gap addressed separately via domain-randomized Isaac Lab rendering during IDM training — two distinct mechanisms for two distinct problems.\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"HARD CONSTRAINT VIOLATION: Manual resource estimate is ~250 H100-hours, which exceeds the user-specified hard limit of ≤200 H100-hours total. The entire resource plan must be revised downward.\", \"CRITICAL MISSED CONCURRENT WORK: EA-WM (arXiv:2605.06192, submitted May 7, 2026) renders forward-kinematics joint heatmaps and injects them as dual token streams into a Wan 2.2 backbone — the same core mechanism as URDF-DiT. This work is not acknowledged in the landscape or key references. The claim that 'no published system injects URDF joint-angle sequences directly into video diffusion attention layers' is false.\", \"VENUE MISLABELING: 'ICLR 2026 (paper deadline September 24 2026)' is incorrect. ICLR 2026 submissions closed ~October 2025. A September 24, 2026 deadline corresponds to ICLR 2027.\", \"TIMELINE IMPLAUSIBILITY FOR CoRL: 20 days (by May 29) to implement ControlNet-style conditioning on Wan 2.2 14B, train a sim IDM in Isaac Lab, run 4 benchmark evaluations, and write the paper is not realistic for a 1-2 person team. No timeline breakdown is provided to justify this.\", \"KIMODO MISCHARACTERIZATION: The proposal cites Kimodo as 'validating the in-loop kinematic conditioning principle' for video diffusion, but Kimodo is a 3D kinematic motion diffusion model (trained on mocap), not an RGB video diffusion model. It does not validate that kinematic conditioning works inside video diffusion attention layers.\", \"SIM→VIDEO IDM DOMAIN GAP UNADDRESSED: The IDM trained exclusively on Isaac Lab G1 frame pairs (photorealistic sim) applied zero-shot to Wan 2.2-generated videos (which have diffusion-model-specific textures and artifacts) faces a well-documented distribution gap. The proposal acknowledges this risk only in Human-in-Loop mode and offers no technical mitigation strategy.\", \"EVALUATION SCOPE VS. LOCO-MANIPULATION CLAIM: Dream2Act's four benchmarks (ball kicking, sofa sitting, bag punching, box hugging) are whole-body contact/interaction tasks, not loco-manipulation in the sense of locomotion simultaneously with object manipulation. Framing these as 'loco-manipulation' benchmarks overstates the scope relative to what the contribution promises.\"]\nFeedback: The core direction (in-loop URDF kinematic conditioning for humanoid video diffusion + sim IDM for policy extraction) remains viable but requires substantial revision before CoRL 2026 submission:\n\n1. **Differentiate from EA-WM**: Read arXiv:2605.06192 carefully. URDF-DiT must clearly differentiate from EA-WM's KVAF approach. The clearest differentiation axes are: (a) full-body humanoid (29+ DoF whole-body) vs. bimanual arm-only; (b) ControlNet as a separate trainable module (weights frozen in backbone) vs. EA-WM's bidirectional fusion requiring joint fine-tuning; (c) explicit action extraction pipeline (sim IDM → policy training trajectories) vs. EA-WM's world-model framing without policy training evaluation. The introduction must directly address EA-WM.\n\n2. **Fix the resource plan**: Reduce total to ≤200 H100-hours. Concretely: (a) use LoRA fine-tuning of Wan 2.2 rather than full fine-tuning (documented to run in 6–24 hours on a single GPU); (b) limit IDM training to ~20–30 H100-hours; (c) restrict evaluation to 2–3 benchmarks rather than all 4. A realistic breakdown: ControlNet module training ~60h, IDM ~30h, evaluation ~50h, ablations ~40h = 180h total.\n\n3. **Address IDM domain gap technically**: The sim→video transfer for IDM is the highest technical risk. Add one of: (a) domain-randomized sim rendering to match video diffusion output statistics; (b) a lightweight IDM adapter fine-tuned on a small set of URDF-DiT-generated frame pairs labeled via sim rollout matching; (c) a kinematic consistency loss during URDF-DiT generation that makes generated frames closer to sim-rendered frames. Without this, the zero-shot claim is likely to fail.\n\n4. **Fix venue labeling**: Change 'ICLR 2026' to 'ICLR 2027 (submission deadline ~October 2026)' as a fallback.\n\n5. **Reframe Kimodo citation**: Kimodo validates kinematic constraints in motion diffusion (3D joint sequences), not in RGB video diffusion. Replace with a more precise citation, e.g., citing 2D skeleton-conditioned video generation work (Controllable Complex Human Motion Video Generation, arXiv:2603.08028) as the closer analogue.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"USER REQUIREMENT VIOLATION — TARGET VENUE: The proposal has silently replaced CoRL 2026 (user's explicit target, deadline May 29, 2026) with ICLR 2027 (October 2026 deadline). This violates the primary constraint. The generator must either (a) produce a concrete CoRL 2026 plan with preliminary results achievable in ≤20 days, or (b) explicitly present the infeasibility argument to the user and request venue scope change before proceeding.\", \"USER REQUIREMENT VIOLATION — TIMELINE: Manual mode (4–6 months) and HIL mode (5–8 weeks) both violate the user's ≤20-day hard constraint. Only auto mode with 8+ H100s (1–2 weeks) approaches feasibility. If targeting CoRL 2026, the auto mode timeline with specific GPU allocation must be the primary mode, not the fallback.\", \"USER REQUIREMENT VIOLATION — EVALUATION PLATFORMS: User specified 'Test on Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench.' The proposal evaluates exclusively on three Dream2Act benchmarks (ball kicking, bag punching, box hugging). None of the user's required evaluation platforms are included.\", \"MISSED CRITICAL CONCURRENT WORK — VAG (arXiv:2604.09330, April 2026): VAG (Dual-Stream Video-Action Generation) jointly denoises video and robot action streams via flow matching, directly solving the paired data synthesis problem without a two-stage IDM. This paper is from April 2026 and directly competes with URDF-DiT's IDM extraction pipeline. The proposal's landscape section must acknowledge VAG and explain why URDF-DiT's explicit URDF kinematic conditioning offers advantages over VAG's implicit action learning, otherwise the IDM contribution is largely subsumed.\", \"RESOURCE ESTIMATE CONCERN — ControlNet Training: Community reports indicate Wan-family ControlNet training requires ~72h on RTX 3090 for similar tasks (implied ~35–50h on H100 depending on dataset size). The proposed 35h may be achievable but is at the boundary — the estimate should reflect worst-case sensitivity (e.g., if longer context/temporal attention training increases compute 1.5–2x, the manual budget risks exceeding 200h total).\", \"IDM DOMAIN GAP — MITIGATION UNPROVEN: The FK residual consistency loss during video generation (pulling generated frames toward sim-renderable kinematics) is a reasonable hypothesis but has no empirical precedent specifically for bridging Wan 2.2 generation distribution → Isaac Lab sim rollout distribution for IDM application. The proposal should cite or test whether this loss actually reduces IDM error or whether domain-randomized rendering alone is sufficient.\"]\nFeedback: The Round 1 issues with EA-WM acknowledgment, Kimodo mischaracterization, venue labeling, and IDM domain gap are substantially addressed. The technical differentiation from EA-WM is now specific and compelling on three axes (full-body vs. arm-only, ControlNet frozen vs. joint fine-tuning, explicit IDM pipeline vs. no policy output). The remaining blockers are primarily user-requirement alignment issues:\n\n1. **Address the venue/timeline mismatch directly**: If CoRL 2026 (May 29) is genuinely infeasible, say so explicitly and quantify why — e.g., 'ControlNet training requires ≥35h GPU compute + 3 days of debugging + evaluation, totaling ≥20 days even in auto mode, so the earliest feasible venue is CoRL 2027 or ICLR 2027.' Present this to the user as a constraint, not a silent substitution.\n\n2. **Add user-required evaluation platforms**: At minimum, add one Isaac Lab humanoid manipulation task (e.g., G1 pick-and-place or table-top reaching from Isaac Lab humanoid suite) as a downstream policy training target. This directly satisfies user requirements and provides a more standardized comparison point than Dream2Act-only benchmarks.\n\n3. **Acknowledge VAG (arXiv:2604.09330, April 2026)** in the landscape. VAG jointly generates video and action, which avoids the IDM domain gap entirely. URDF-DiT's advantage over VAG is the explicit URDF kinematic constraint (enforcing joint-limit compliance and embodiment geometry) rather than implicit action learning — this distinction must be made explicit.\n\n4. **Tighten the ControlNet compute estimate**: Add a sensitivity analysis — if training takes 50h instead of 35h due to video temporal attention overhead, total manual budget becomes ~150h, still within constraint. This removes the ambiguity in the estimate.\n\n5. **Scope the contribution more precisely for a 20-day auto-mode execution**: If targeting CoRL 2026 is reinstated, the evaluation scope must be reduced to 2 benchmarks (not 3), and the ablation set must be compressed to one primary comparison (in-loop vs. post-hoc), with the ControlNet-vs-bidirectional-fusion ablation deferred to the ICLR 2027 extended submission.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"DREAM2ACT FAILURE MODE MISCHARACTERIZATION (PERSISTENT): The proposal states 'kinematic artifacts from post-hoc URDF-IK correction are cited as the primary failure mode' for Dream2Act's 37.5% success — this is inaccurate. The paper's failure analysis identifies the 'morphology gap' and 'severe spatial misalignments' as failures of the BASELINE (traditional retargeting, 0%), not as Dream2Act's own failure mode. Dream2Act's 37.5% performance is not attributed to post-hoc correction artifacts in the paper itself. The generator is presenting an inference as a citation, which will draw immediate reviewer fire. Correct to: 'We hypothesize that post-hoc URDF-IK correction in Dream2Act introduces kinematic artifacts (e.g., joint discontinuities from IK failure at contact poses); the 37.5% overall ceiling, including 10% on Box Hugging, is consistent with this hypothesis but may also reflect task difficulty.'\", \"COMPARISON VALIDITY — URDF-DiT vs. DREAM2ACT IS APPLES-TO-ORANGES: Dream2Act is a zero-shot real-robot execution system (video → URDF-IK → motor commands → physical robot); URDF-DiT generates synthetic training data for a sim-IDM policy (video → IDM → joint velocity commands → policy training in Isaac Lab). The proposed 'in-loop vs. post-hoc ablation at matched video budgets' is comparing architectures that solve different problems. This comparison needs to be redesigned: either (a) compare kinematic consistency metrics of generated videos (FK residual, joint-limit violation rate, temporal smoothness) between URDF-DiT and a post-hoc correction baseline, or (b) compare downstream policy success rate on Isaac Lab after training on URDF-DiT-generated data vs. data extracted via post-hoc URDF-IK from vanilla Wan 2.2 outputs — the latter is a fair ablation.\", \"NOVELTY ARGUMENT UNDERSPECIFIED FOR FULL-BODY VS. END-EFFECTOR CONDITIONING: EA-WM already injects end-effector heatmaps into Wan 2.2 cross-attention and achieves action recovery detection rate ~0.45. URDF-DiT's claim is that conditioning on all 29 DoF (pelvis, legs, torso, arms, hands) simultaneously is qualitatively different. But the technical argument for why whole-body joint conditioning outperforms end-effector-only conditioning for whole-body tasks (not just arm tasks) needs to be made explicitly — e.g., does the pelvis/leg conditioning actually improve foot contact realism in generated videos? Without a targeted ablation (all-joint FK heatmaps vs. end-effector-only heatmaps), reviewers will reasonably ask if end-effector conditioning would suffice for the manipulation component while leg conditioning is just noise.\", \"IDM DOMAIN GAP: FK RESIDUAL LOSS MECHANISM LACKS CLARITY: The proposal claims 'a per-frame FK residual consistency loss added to URDF-DiT's generation objective, penalizing deviations between generated joint positions and URDF FK predictions' bridges the Wan 2.2 → Isaac Lab appearance domain gap. But this loss operates on kinematics, not appearance. The domain gap for the IDM is primarily in the visual domain (Wan 2.2 texture/lighting vs. Isaac Lab domain-randomized rendering). The FK residual loss may enforce kinematic consistency in generated videos but does not directly reduce the appearance domain gap that causes IDM errors. Domain-randomized rendering during IDM training is the more direct mitigation; the FK residual loss role needs to be more precisely specified.\", \"COMPUTE ESTIMATE FOR CONTROLNET TRAINING REMAINS UNCERTAIN: The 35–70h range is wide (2x uncertainty). Community experience with Wan 2.2 LoRA fine-tuning (3-6h on A40) and the existence of TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1 on HuggingFace suggest ControlNet module training on Wan 2.2 is feasible, but for FK heatmap conditioning specifically (multi-channel, time-varying, full-body), temporal attention overhead could push toward the 70h end. Given the 8 H100 parallelization, this is manageable within budget, but the estimate should be anchored to the existing depth-ControlNet training reports rather than stated as a 2x range with no empirical basis.\", \"PAPER WRITING TIMELINE (DAYS 15–19) IS EXTREMELY TIGHT FOR CoRL SUBMISSION: A CoRL paper requires a well-positioned introduction, related work distinguishing from EA-WM/Dream2Act/VAG, technical method, and experiments section. With auto-research mode generating code and running experiments, 4 days for paper writing is possible only if the agent also drafts large portions of the paper. The proposal should explicitly state whether auto mode includes paper drafting assistance or whether the 4-day window assumes a human researcher writing.\"]\nFeedback: The proposal has resolved all critical issues from Rounds 1–2: compute budget is within 200h, EA-WM/VAG/Dream2Act are properly acknowledged and differentiated, user-required evaluation platforms (Isaac Lab G1, HumanoidBench, RoboCasa365) are included, venue labeling is correct, and the IDM domain gap has a mitigation plan. The residual issues are addressable in one more revision:\n\n1. **Fix the Dream2Act failure mode claim**: Change 'kinematic artifacts from post-hoc correction are cited as the primary failure mode' to 'we hypothesize that post-hoc URDF-IK correction introduces kinematic artifacts at contact poses — consistent with Dream2Act's 10% Box Hugging success rate — motivating in-loop FK conditioning.' Do not claim the paper cites this as primary failure mode.\n\n2. **Redesign the in-loop vs. post-hoc ablation**: The ablation should compare (a) URDF-DiT-generated videos vs. vanilla Wan 2.2 videos post-processed with URDF-IK (both used as training data for the same IDM), evaluating downstream Isaac Lab policy success rate. This is a fair, self-contained comparison that doesn't require reimplementing Dream2Act's zero-shot real-robot pipeline.\n\n3. **Add a targeted ablation for full-body vs. end-effector conditioning**: Even a 2-point ablation (all 29 DoF heatmaps vs. end-effector-only, 5 DoF) would directly validate whether full-body conditioning is necessary. This would be the paper's strongest scientific contribution claim and is achievable in the same compute budget.\n\n4. **Clarify the FK residual loss role**: Reframe it as 'enforcing kinematic consistency in generated video (reducing temporal joint jitter and limit violations)' rather than 'bridging the sim→video domain gap for IDM.' Domain-randomized rendering during IDM training is the primary domain gap mitigation; the FK residual loss ensures the generated videos are kinematically coherent inputs to the IDM.\n\n5. **Address paper writing in the timeline**: State explicitly whether auto mode includes paper drafting (using the agent to generate LaTeX drafts based on results), which is what makes the 4-day window feasible. Without this, the CoRL timeline is implausible even in auto mode.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"PERSISTENT CRITICAL MISCHARACTERIZATION — DREAM2ACT FAILURE MODE (ROUND 4, UNRESOLVED FROM ROUND 3): Independent verification via arXiv:2603.19709v1 confirms that Dream2Act does NOT cite 'kinematic artifacts from post-hoc URDF-IK correction' as its primary failure mode. Dream2Act generates video directly in the robot's native spatial coordinate system and explicitly avoids post-hoc correction — its stated limitation is inference latency, not kinematic artifacts. The per-task breakdown (Ball-kicking 40%, Box-hugging 10%, Bag-hitting 30%, Sofa-sitting 70%) reflects task difficulty, not IK correction artifacts. The proposal has now repeated this false claim through three consecutive rounds despite explicit correction instruction in Round 3. This is the most urgent issue to fix before any venue submission, as Dream2Act authors and CoRL reviewers familiar with the paper would immediately flag it.\", \"ABLATION DESIGN STILL APPLES-TO-ORANGES (UNRESOLVED FROM ROUND 3): The CoRL-scoped ablation remains 'in-loop vs. post-hoc URDF-IK at matched video budgets,' which Round 3 identified as comparing architectures that solve different problems (Dream2Act: zero-shot real-robot execution; URDF-DiT: synthetic training data for sim-IDM policy). The required redesign — compare downstream policy success rate on Isaac Lab after training on (a) URDF-DiT-generated data vs. (b) vanilla Wan 2.2 data post-processed with URDF-IK — was not implemented. Without this fix, the primary ablation is technically invalid as a comparison.\", \"FULL-BODY VS. END-EFFECTOR ABLATION STILL ABSENT (UNRESOLVED FROM ROUND 3): Round 3 explicitly requested a 2-point ablation (all 29 DoF FK heatmaps vs. end-effector-only, ~5 DoF) to validate whether full-body conditioning is necessary for whole-body tasks. This would be the paper's strongest scientific claim and is achievable within budget. It remains missing in Round 4.\", \"FK RESIDUAL LOSS ROLE STILL IMPRECISE (UNRESOLVED FROM ROUND 3): The approach still frames the FK residual loss as one of 'two primary mechanisms' mitigating the 'sim→video IDM domain gap.' Round 3 correctly identified that this loss operates on kinematics in the generated video (reducing temporal joint jitter and joint-limit violations), not on visual appearance. The appearance domain gap is addressed by domain-randomized rendering during IDM training; the FK residual loss should be reframed as enforcing kinematic consistency in generated outputs rather than bridging the visual distribution gap.\", \"MISSED CONCURRENT WORK — EVA (arXiv:2603.17808, March 2026): 'EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards' directly addresses the executability gap in video world models via inverse dynamics rewards, competing with URDF-DiT's IDM extraction pipeline. This paper is not cited in the landscape and should be acknowledged with explicit differentiation.\", \"PAPER WRITING TIMELINE STILL UNADDRESSED (UNRESOLVED FROM ROUND 3): Days 15–19 are allocated to 'paper writing and CoRL submission polish' in auto mode without stating whether the auto agent also drafts LaTeX sections. Without explicit acknowledgment that auto-mode includes paper drafting (introduction, related work distinguishing EA-WM/Dream2Act/VAG, method, experiments), the 4-day window is implausible for a full CoRL submission.\", \"EA-WM TITLE DISCREPANCY: The proposal calls EA-WM 'Embodiment-Aware World Model via Kinematic-Visual Action Fields for Bimanual Manipulation' but the actual title is 'EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields' (Event-Aware, not Embodiment-Aware). Additionally, independent search suggests EA-WM evaluates on WorldArena benchmark rather than being scoped exclusively to bimanual manipulation — verify this characterization before submission.\"]\nFeedback: The technical core of URDF-DiT (in-loop FK heatmap conditioning for 29+ DoF full-body humanoid via ControlNet frozen backbone + explicit IDM pipeline) remains defensible and competitive. The VAG differentiation is now independently verified as accurate. Three targeted fixes are required before this passes:\n\n1. **CRITICAL — Fix the Dream2Act framing (round 5 MUST fix this)**: Direct paper read confirms Dream2Act generates in robot-native space, does NOT use post-hoc URDF-IK correction as its mechanism, and cites inference latency as its limitation — not kinematic artifacts. Change the entire motivation: instead of 'Dream2Act fails due to post-hoc IK artifacts,' frame it as 'Dream2Act's robot-native video synthesis (37.5% ceiling) shows the gap is not retargeting but video fidelity — we push further by enforcing URDF joint-limit compliance throughout denoising rather than relying on video realism alone.' This is actually a stronger and more honest motivation.\n\n2. **Redesign the primary ablation**: Compare downstream Isaac Lab policy success rate: (a) policies trained on URDF-DiT-generated trajectories vs. (b) policies trained on trajectories extracted from vanilla Wan 2.2 videos via post-hoc URDF-IK. This is a self-contained, fair comparison that avoids reimplementing Dream2Act.\n\n3. **Add the full-body vs. end-effector ablation**: Even reporting 2 data points (all-joint heatmaps vs. end-effector-only, same IDM) would elevate this from a systems paper to a scientific contribution. It is the one claim that distinguishes URDF-DiT from EA-WM and requires empirical validation.\n\n4. **Cite and differentiate from EVA (arXiv:2603.17808)**: EVA trains IDMs as rewards for video generation to close the executability gap; explain that URDF-DiT enforces geometric kinematic constraints (joint angles, limits) rather than relying on a learned executability signal.\n\n5. **Reframe FK residual loss**: It enforces kinematic consistency in generated video (reducing temporal joint jitter, preventing limit violations during denoising) — not a visual domain gap bridge. Domain-randomized rendering handles the appearance gap; the FK loss handles geometric consistency. Say so precisely.\n\n6. **State explicitly in the auto-mode timeline**: 'Auto mode includes agent-assisted LaTeX drafting (introduction, related work, method, experiments) starting Day 14 — this is what makes the 4-day writing window feasible.'\n\n### Round 5 review\nVerdict: revise\nIssues: [\"EVALUATION SCOPE PARTIALLY VIOLATES USER REQUIREMENTS: User explicitly required testing on 'Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench.' The CoRL-scoped submission defers RoboCasa365 and HumanoidBench entirely to ICLR 2027, leaving the CoRL submission evaluated only on Isaac Lab G1 locomanipulation plus a Dream2Act ball-kicking contextual comparison. This is a conscious scope reduction that must be explicitly flagged to the user as a requirement tradeoff, not silently accepted as the default plan.\", \"DREAM2ACT MECHANISM REQUIRES CAREFUL PHRASING: Independent verification via the arXiv:2603.19709 HTML confirms Dream2Act DOES use post-hoc URDF-constrained IK (applying IK after video generation to convert pixel-space pose to joint trajectories) — the Round 5 proposal's description is factually correct. However, Dream2Act also frames this as generating 'within robot-native coordinate space,' meaning its videos hallucinate the G1 robot body (not a human), then apply IK to extract joint angles. The proposal should distinguish between (a) Dream2Act's video generation modality (robot-native appearance) and (b) Dream2Act's kinematic extraction approach (post-generation constrained IK) to avoid any conflation that reviewers could challenge.\", \"FLOWANY-R1 (arXiv:2601.10103, January 2026) NOT CITED: This paper targets 'interactive humanoid video generation' with 'holistic and fine-grained full-body control' at 25fps via MMDiT architecture. While its kinematic conditioning mechanism is underspecified in the abstract and it targets real-time interaction (not training data generation), it is directly in the humanoid video generation space and should appear in the landscape with a one-line differentiation (no URDF kinematic structure, no IDM policy extraction pipeline, interactive use case vs. offline training data generation).\", \"EA-WM COMPETITIVE RISK STILL HIGH — DIFFERENTIATION NEEDS EMPIRICAL BACKING: EA-WM (May 7, 2026) uses KVAFs (Gaussian heatmaps at projected end-effector/joint locations injected into Wan 2.2 cross-attention) — the same core design pattern as URDF-DiT's FK heatmap injection. The proposal differentiates on (a) full-body 29 DoF vs. arm manipulation, (b) ControlNet frozen backbone vs. bidirectional fusion joint fine-tuning, and (c) IDM pipeline vs. no policy output. These are real differentiators, but the scientific weight of (a) depends entirely on the full-body vs. end-effector ablation result — if the ablation shows marginal improvement from full-body conditioning, CoRL reviewers will question whether the 29 DoF scope is necessary rather than just incremental over EA-WM's end-effector approach. The ablation must be framed as the central scientific claim, not a supporting experiment.\", \"CORL 2026 TIMELINE PIVOT CRITERIA UNDERSPECIFIED: The proposal states 60–70% probability of submittable results by May 29 in auto mode, with 'immediate pivot to ICLR 2027 if results are negative by Day 14.' The Day 14 decision gate needs more precise criteria: what constitutes 'results that warrant ICLR 2027 pivot' vs. 'results that, while imperfect, constitute a submittable CoRL contribution'? Without specific metric thresholds (e.g., 'if URDF-DiT trained policy success rate > X% and > Y% improvement over vanilla Wan 2.2 baseline, proceed to CoRL; otherwise pivot'), the pivot decision is ambiguous and the 60–70% probability estimate has no anchoring.\"]\nFeedback: Round 5 has resolved all seven critical issues from Round 4: Dream2Act is correctly described (inference latency as primary limitation, post-hoc IK acknowledged), EA-WM title corrected (Event-Aware), FK residual loss precisely framed (kinematic consistency not domain gap), ablation redesigned to downstream Isaac Lab policy success rate comparison, full-body vs. end-effector ablation added, EVA cited and differentiated, and auto-mode LaTeX drafting explicitly stated. The proposal is now technically sound. Four targeted fixes remain before this should proceed:\n\n1. **Flag the user requirement tradeoff explicitly**: The CoRL submission evaluates only Isaac Lab G1 locomanipulation; HumanoidBench and RoboCasa365 are deferred. Present this to the user as an explicit tradeoff decision ('CoRL version covers 1 of 3 required benchmarks; full coverage requires ICLR 2027') rather than embedding it quietly in the venue notes. The user may prefer to target ICLR 2027 from the start.\n\n2. **Add FlowAct-R1 (arXiv:2601.10103) to the landscape**: One line — 'FlowAct-R1 (arXiv:2601.10103, January 2026) targets real-time interactive humanoid video generation via MMDiT chunkwise diffusion without URDF kinematic constraints or IDM policy extraction.' This paper predates the CoRL 2026 submission and reviewers may cite it.\n\n3. **Elevate the full-body vs. end-effector ablation to the primary scientific claim**: Frame the paper's core question as 'Does conditioning on all 29 DoF (pelvis, legs, torso, arms, hands) throughout denoising improve downstream IDM extraction quality for whole-body contact tasks compared to end-effector-only conditioning?' This directly differentiates from EA-WM empirically and positions the ablation result as the paper's central finding, not a supporting experiment.\n\n4. **Add specific metric thresholds for the Day 14 CoRL/ICLR 2027 pivot decision**: Define 'submittable' concretely — e.g., 'URDF-DiT policy success rate ≥ 10% on Isaac Lab G1 pick-and-place AND ≥ 5 percentage point improvement over vanilla Wan 2.2 + post-hoc IK baseline triggers CoRL submission; otherwise pivot to ICLR 2027.' This turns the 60–70% probability statement into an actionable decision gate.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"CRITICAL NEW ISSUE — BRIDGEV2W (arXiv:2602.03793, February 2026) NOT CITED: Independent verification confirms BridgeV2W explicitly 'converts coordinate-space actions into pixel-aligned embodiment masks rendered from the URDF and camera parameters. These masks are then injected into a pretrained video generation model via a ControlNet-style pathway.' This paper — applied to single-arm (DROID) and dual-arm (AgiBot-G1) robots — is architecturally nearly identical to URDF-DiT's core contribution (ControlNet + URDF conditioning for robot video DiT). A CoRL reviewer familiar with the embodied world model literature will immediately flag this omission. URDF-DiT must cite BridgeV2W and differentiate explicitly on: (a) full-body humanoid 29 DoF vs. arm/dual-arm scope; (b) Gaussian joint-position heatmaps from FK (continuous per-joint scalar fields encoding kinematic structure) vs. BridgeV2W's pixel-aligned binary embodiment masks (which encode link occupancy but not individual joint angles); (c) IDM training data generation as the downstream objective vs. BridgeV2W's policy evaluation and goal-conditioned planning. With BridgeV2W now in the landscape alongside EA-WM, the claim that URDF-DiT introduces ControlNet + URDF injection into video DiT is no longer defensible — the paper's novelty must be repositioned as 'full-body humanoid kinematic conditioning with Gaussian heatmaps for IDM training data generation,' not as a novel conditioning architecture.\", \"VAG 'EXPLICITLY ACKNOWLEDGES' CHARACTERIZATION REQUIRES PRECISION: The proposal states VAG 'explicitly acknowledges the video branch has not been influenced by the action branch.' Independent review of the VAG abstract finds it describes 'synchronized denoising in both branches' with 'adaptive 3D pooling to transfer compact global video context to the action branch' — suggesting the design routes video features to actions but not necessarily the reverse. If this quote comes from an ablation or analysis section in the full paper, it must be cited with section/page reference. If it is the proposal author's inference, it must be rewritten: 'VAG's architecture routes video context to the action branch via 3D pooling but does not inject action signals back into the video denoising process, leaving a video-action coupling gap that explicit FK heatmap injection in URDF-DiT addresses.' Misquoting a competitor's paper is a fast track to rejection at CoRL.\", \"NOVELTY BAR AT CORL IS NOW CRITICALLY THIN: With EA-WM (in-loop kinematic heatmap injection into Wan 2.2 cross-attention, May 2026) and BridgeV2W (ControlNet + URDF embodiment mask injection into pretrained video DiT, February 2026) both uncited-until-now, the paper's architectural contribution is no longer novel. The remaining novelty is exclusively in (a) full-body humanoid scope (29 DoF vs. arm-only) and (b) IDM-to-policy pipeline. Point (b) is primarily an engineering contribution. Point (a) is an empirical claim that depends on Ablation B showing meaningful improvement (≥5pp). If Ablation B shows marginal benefit from full-body vs. end-effector conditioning, the paper has no defensible novel claim over the combined EA-WM + BridgeV2W prior work. The proposal's 'submit with reframing' contingency (Ablation B < 3pp → 'end-effector conditioning suffices') would produce a paper saying 'our novel extension doesn't help' — which is not a CoRL-level contribution. This risk must be assessed before committing to the CoRL trajectory.\", \"CORL EVALUATION STILL 1 OF 3 USER-REQUIRED BENCHMARKS: This is flagged explicitly in the proposal (which is correct), but it remains a hard constraint — the CoRL submission does not satisfy the user's stated requirement of evaluating on Isaac Lab G1 locomanipulation, HumanoidBench, AND RoboCasa365. The proposal correctly identifies this as an explicit user decision, but the review record should note it is unresolved from the user's perspective until they make the opt-in/out decision. Without user confirmation, the CoRL path should be treated as provisional.\"]\nFeedback: Round 6 correctly resolved all four Round 5 issues: user tradeoff is explicitly and prominently flagged, FlowAct-R1 is in the landscape with a one-line differentiation, Ablation B is the primary scientific claim, and Day 14 pivot criteria have concrete numeric thresholds. The proposal is structurally sound. Two targeted fixes are required:\n\n1. **URGENT: Add BridgeV2W to the landscape and reposition the novelty claim.** BridgeV2W (arXiv:2602.03793, February 2026) uses 'coordinate-space actions → pixel-aligned embodiment masks rendered from URDF → ControlNet-style injection into pretrained video DiT.' This is the same architecture as URDF-DiT. Add a landscape entry: 'BridgeV2W (arXiv:2602.03793, Feb 2026) uses URDF-rendered pixel-aligned embodiment masks injected via ControlNet pathway into a pretrained video DiT for arm/dual-arm manipulation video generation and policy evaluation. URDF-DiT differentiates on three axes: (a) full-body humanoid 29 DoF (vs. arm/dual-arm) with Gaussian joint-position heatmaps encoding per-joint kinematic structure rather than binary link occupancy masks; (b) whole-body contact interaction tasks (pick-and-place with locomotion, ball-kicking) vs. arm manipulation; (c) IDM training data generation pipeline vs. policy evaluation and goal-conditioned planning.' Then revise the introduction to acknowledge that ControlNet + URDF conditioning for robot video DiTs is now an established approach (citing EA-WM and BridgeV2W) and position URDF-DiT as the first application of this approach to full-body humanoid whole-body contact tasks with an explicit IDM training data generation objective.\n\n2. **Fix the VAG 'explicitly acknowledges' characterization.** Change to: 'VAG's architecture routes compact global video context to the action branch via adaptive 3D pooling, but does not inject action signals back into the video denoising process — a design gap URDF-DiT addresses via bidirectional FK heatmap conditioning.' Do not use a direct quote unless you can cite the specific section where VAG uses those exact words.\n\n3. **Assess the Ablation B risk explicitly.** Given EA-WM + BridgeV2W now both in the landscape, the paper needs Ablation B to be strongly positive (≥5pp) to have a defensible novel claim at CoRL. Add to the pivot criteria: if Ablation B < 5pp AND BridgeV2W is the closest prior, the paper's CoRL-level novelty is insufficient — pivot to ICLR 2027 with full benchmark coverage and a deeper ablation suite (also including a direct comparison against BridgeV2W's embodiment mask approach).\n\n### Round 7 review\nVerdict: revise\nIssues: [\"CRITICAL UNRESOLVED FROM ROUND 6 — BridgeV2W (arXiv:2602.03793) STILL ABSENT: Independent verification confirms BridgeV2W (February 3, 2026) uses URDF-rendered pixel-aligned embodiment masks injected via ControlNet-style pathway into pretrained video DiT, tested on DROID (single-arm) and AgiBot-G1 (dual-arm). This paper is architecturally nearly identical to URDF-DiT's core mechanism and has been flagged as missing in every round since Round 6. It is absent from both the landscape section and key_references in Round 7. A CoRL reviewer familiar with embodied world model literature will flag this immediately. URDF-DiT must add BridgeV2W and explicitly differentiate on: (a) full-body humanoid 29 DoF vs. arm/dual-arm scope; (b) continuous per-joint Gaussian FK heatmaps encoding kinematic structure vs. BridgeV2W's binary pixel-aligned occupancy masks (which encode link presence but not individual joint angles or joint-limit constraints); (c) IDM training data generation as the downstream objective vs. BridgeV2W's goal-conditioned planning and policy evaluation. The introduction must acknowledge that ControlNet + URDF conditioning for robot video DiTs is an established approach (BridgeV2W: Feb 2026; EA-WM: May 2026) and position URDF-DiT as the first application to full-body humanoid 29 DoF whole-body contact tasks with explicit IDM training data generation.\", \"VAG SECTION ATTRIBUTION MISSING: The VAG quote 'video branch not influenced by action branch' is independently verified as accurate (confirmed from the paper's 'Limitations and Future Work' section, which explicitly states 'video generation has not been influenced by the action branch, wasting beneficial control signals'). The proposal should cite this as: 'VAG's authors explicitly acknowledge in their Limitations section that the video branch has not been influenced by the action branch' — or use the exact paper quote with section attribution — to preempt any reviewer challenge to this claim.\", \"SUBMIT-WITH-REFRAMING CONTINGENCY WEAKENED BY BRIDGEV2W + EA-WM LANDSCAPE: The proposal states that if Ablation B shows <3pp improvement from full-body vs. end-effector conditioning, the paper can be 'reframed as end-effector conditioning suffices' and remains 'a valid CoRL contribution.' This contingency is now significantly weaker given BridgeV2W and EA-WM both already demonstrate ControlNet + URDF conditioning for arm robots. If full-body conditioning over end-effector-only shows <3pp improvement, the paper is essentially validating that the arm-robot approaches (BridgeV2W, EA-WM) are sufficient for humanoids — which is a minor empirical finding, not a CoRL-level contribution. The pivot criteria must explicitly add: 'If Ablation B < 3pp AND BridgeV2W/EA-WM are closest prior work, pivot to ICLR 2027 (not CoRL reframing), as the novelty claim over existing arm-robot ControlNet+URDF approaches is insufficient for CoRL acceptance.'\", \"NEW UNCITED CONCURRENT WORK — MotuBrain (arXiv:2604.27792, April 2026): MotuBrain introduces a world action model that jointly supports video generation, inverse dynamics prediction, and joint video-action prediction for robot control — directly overlapping with URDF-DiT's IDM extraction pipeline goal. While the conditioning mechanism differs, MotuBrain's joint video-IDM modeling is a concurrent approach to the same problem of extracting executable actions from generated video, and CoRL reviewers in the embodied video generation track will likely be familiar with it. Add a one-line differentiation.\", \"EVALUATION SCOPE — USER REQUIREMENT TRADEOFF (EXPLICITLY FLAGGED BUT UNRESOLVED): The proposal now correctly and prominently flags that CoRL 2026 covers only 1 of 3 user-required benchmarks (Isaac Lab G1 locomanipulation only; HumanoidBench and RoboCasa365 deferred to ICLR 2027). This is appropriately presented as an explicit user decision (option A vs. option B). However, until the user makes this choice, the CoRL path should be treated as provisional — the reviewer record notes this remains open.\"]\nFeedback: Round 7 has resolved the majority of prior issues: user tradeoff is prominently and honestly flagged, Dream2Act two-component description is accurate and precise, VAG characterization is confirmed accurate (the quote is real), Ablation B is correctly elevated as the primary scientific claim, Day 14 pivot criteria have concrete numeric thresholds, FlowAct-R1 is in the landscape, EA-WM title is corrected, FK residual loss role is precisely framed, and EVA is cited and differentiated. The proposal is technically sound and structurally well-organized.\n\nOne critical fix remains before this can pass:\n\n**URGENT — Add BridgeV2W to landscape (3rd consecutive round flagged)**: BridgeV2W (arXiv:2602.03793, Feb 2026) is independently confirmed: URDF-rendered pixel-aligned embodiment masks → ControlNet pathway → pretrained video DiT, tested on DROID and AgiBot-G1 dual-arm datasets. Add this entry to landscape: 'BridgeV2W (arXiv:2602.03793, Feb 2026): converts coordinate-space robot actions to pixel-aligned binary embodiment masks rendered from URDF and camera parameters, injected via ControlNet-style pathway into pretrained video DiT for arm/dual-arm manipulation; evaluates on DROID and AgiBot-G1. URDF-DiT differentiates on: (a) full-body humanoid 29 DoF vs. arm/dual-arm scope; (b) continuous per-joint Gaussian FK heatmaps (encoding joint-angle-specific kinematic structure and joint-limit constraints) vs. binary occupancy masks (encoding link presence only); (c) IDM synthetic training data generation pipeline vs. goal-conditioned planning and policy evaluation.' Then revise the introduction to frame ControlNet+URDF+video-DiT as an established approach (BridgeV2W Feb 2026, EA-WM May 2026) and position URDF-DiT as the first extension to full-body humanoid 29 DoF whole-body contact tasks.\n\nTwo secondary fixes:\n1. Add section attribution to VAG quote: '(VAG Limitations and Future Work section: video generation has not been influenced by the action branch, wasting beneficial control signals)'\n2. Tighten pivot criteria: add 'If Ablation B < 3pp AND BridgeV2W/EA-WM are closest prior, pivot directly to ICLR 2027 — CoRL reframing insufficient over arm-robot ControlNet+URDF baseline'\n3. Add MotuBrain (arXiv:2604.27792, April 2026) as a one-line landscape entry.\n\n### Round 8 review\nVerdict: revise\nIssues: [\"UNCITED COMPETITOR — HumanX (arXiv:2602.02473, February 2026): HumanX introduces XGen, a video synthesis pipeline generating physically plausible humanoid training data for loco-manipulation tasks (basketball, football, cargo pickup) with zero-shot transfer to physical G1 and 8x higher generalization success than prior methods. Although retargeting-based (hence out of scope for URDF-DiT's contribution type), it competes in the same application space — generating synthetic humanoid training data for loco-manipulation — and a CoRL 2026 reviewer will expect to see it cited with a one-line differentiation explaining that URDF-DiT generates kinematically constrained video without retargeting from human motion, while HumanX synthesizes data by retargeting human motion videos to humanoid morphology. Failure to cite it will invite a 'missing related work' reviewer flag.\", \"KINEMA4D CHARACTERIZATION POTENTIALLY UNDERSTATED: The proposal describes Kinema4D (arXiv:2603.16669, March 2026) as 'URDF-driven FK for 4D pointmap conditioning for scene realism; not policy-data generation or video diffusion attention-layer injection' — but independent search finds it described as 'action-conditioned 4D generative simulator that drives a URDF robot via kinematics, then uses diffusion transformer to generate 4D world sequences' including 'robot control trajectories and environmental reactions.' The differentiation may still hold (4D geometric representation vs. RGB video; 4D world simulation vs. IDM training data pipeline) but the current one-line dismissal underspecifies the distinction. Reviewers familiar with Kinema4D may challenge this. Add a more precise differentiation: Kinema4D generates 4D geometric pointmap sequences for spatial simulation and scene realism — it does not generate photorealistic RGB video frames suitable for IDM training, does not inject kinematic conditioning into RGB video DiT attention layers, and provides no IDM extraction or downstream policy training pipeline.\", \"NOVELTY FRAMING RISK FOR CORL BAR: The title 'Does Full-Body Kinematic Conditioning Throughout Denoising Improve IDM Training Data...' frames the paper as an empirical hypothesis test — a valid framing for workshops or NeurIPS empirical tracks but atypical for CoRL, which expects papers that propose a method and demonstrate its superiority. If the submission explicitly frames its central contribution as an ablation study ('we test whether X is necessary'), CoRL reviewers may apply a higher scrutiny threshold to justify acceptance. The pivot to 'Ablation A as primary claim' contingency is logically sound but should be embedded in the paper structure naturally — not appear as an explicitly contingent fallback.\", \"CORL SUBMISSION COVERS ONLY 1 OF 3 USER-REQUIRED BENCHMARKS: This is explicitly and prominently flagged throughout the proposal (including top-of-document warnings), which is correct — but the issue remains unresolved from the user's perspective until they make the opt-in/out decision. Without user confirmation to proceed with the CoRL-scoped single-benchmark plan, the CoRL trajectory should be treated as provisional.\"]\nFeedback: Round 8 has resolved all critical persistent issues from prior rounds. BridgeV2W is now properly cited with precise three-axis differentiation in landscape, key_references, approach, and core_problem sections. VAG quote is correctly attributed to the Limitations and Future Work section. MotuBrain is cited. The submit-with-reframing contingency is correctly scoped ('if Ablation B < 3pp AND Ablation A < 5pp, pivot to ICLR 2027 — not CoRL reframing'). Dream2Act two-component decomposition is precise and independently verified. The proposal is now structurally sound for a Round 9 pass with two targeted fixes:\n\n1. **Add HumanX (arXiv:2602.02473, February 2026) to landscape**: One line — 'HumanX (arXiv:2602.02473, Feb 2026) generates humanoid loco-manipulation training data via XGen (video synthesis retargeting human motion to humanoid morphology) + XMimic (imitation learning), achieving zero-shot physical G1 transfer across sports/manipulation tasks. URDF-DiT differentiates: generative kinematic conditioning without retargeting from human videos, targeting IDM training data for whole-body contact tasks via explicit URDF FK heatmap injection.' This eliminates the likely reviewer flag without requiring substantive changes.\n\n2. **Expand Kinema4D differentiation**: Replace the current one-line description with: 'Kinema4D (arXiv:2603.16669, March 2026, NTU): action-conditioned 4D generative simulator using URDF kinematics to drive a diffusion transformer generating 4D pointmap world sequences for spatial simulation. Key distinction from URDF-DiT: Kinema4D generates 4D geometric representations for simulation realism — it does not generate photorealistic RGB video frames suitable for IDM training, does not inject kinematic conditioning into RGB video DiT cross-attention, and provides no IDM extraction or policy training pipeline. Complementary in the sense that Kinema4D handles 4D world simulation while URDF-DiT targets RGB video generation for IDM data.'\n\n3. **Optional — soften the hypothesis-test title framing**: If targeting CoRL, consider retitling to 'URDF-DiT: Full-Body Kinematic Conditioning for Humanoid IDM Training Data Generation via Video Diffusion' and reserving the 'Does X improve Y?' framing for the abstract's research question statement rather than the title — CoRL reviewers generally favor titles that state what the method is, not what question it asks.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T13:55:15.766Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T13:55:15.766Z",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9"
}
```

---

## Round 1

20 recorded events

### User

_source line 3 · 2026-05-10T13:55:15.809Z_

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

## Idea under review (round 9/10)
{
  "title": "URDF-DiT: Full-Body Kinematic Conditioning Throughout Video Denoising for Humanoid Whole-Body Contact Training Data",
  "project_name": "urdf_dit_loco_policy",
  "source": "web_research",
  "level": "solid",
  "core_problem": "URDF-DiT addresses the challenge of generating kinematically valid synthetic training videos for humanoid whole-body contact tasks at scale. Two design decisions define the system: (A) kinematic constraints are enforced IN-LOOP throughout video denoising — injecting URDF FK heatmaps into Wan 2.2 DiT cross-attention at every step — rather than post-hoc after generation (Dream2Act approach B: 2D pose estimation → 2D-to-3D lifting → URDF-IK applied after all frames are produced); (B) conditioning spans the full 29-DoF kinematic chain (pelvis, legs, torso, arms, hands) rather than end-effector-only (~5 DoF wrist/hand), as in established arm-manipulation approaches.\n\nThese design choices are validated by two ablations against the primary downstream metric — Isaac Lab G1 pick-and-place policy success rate — rather than against video quality metrics: (Ablation A) URDF-DiT vs. vanilla Wan 2.2 + post-hoc URDF-IK [same IDM, same downstream training — directly tests in-loop vs. post-hoc kinematic enforcement]; (Ablation B) 29-DoF full-body conditioning vs. end-effector-only conditioning [same IDM, same downstream evaluation — tests whether the full kinematic chain is necessary for whole-body contact task IDM data]. Neither BridgeV2W nor EA-WM tests either comparison — both evaluate video generation quality metrics, not downstream IDM training data quality.\n\nThe landscape context: BridgeV2W (arXiv:2602.03793, Feb 2026) and EA-WM (arXiv:2605.06192, May 2026) together establish the ControlNet+URDF+video-DiT paradigm for arm/dual-arm manipulation — validating in-loop URDF-derived conditioning for arm manipulation, but neither evaluates IDM training data quality or full-body humanoid DoF. Dream2Act (arXiv:2603.19709, March 2026) applies post-hoc URDF-IK for kinematic extraction after unconstrained video generation in robot-native visual space, achieving 37.5% on whole-body contact tasks. HumanX (arXiv:2602.02473, Feb 2026) demonstrates a parallel paradigm: XGen synthesizes humanoid loco-manipulation training data via motion retargeting (3D pose estimation → IK optimization to humanoid skeleton) + IsaacGym physics simulation — no video diffusion, no IDM. HumanX validates synthetic humanoid data generation without video diffusion; URDF-DiT's contribution is specific to the video-diffusion → IDM pathway. URDF-DiT is the first system in this pathway to extend full-body 29-DoF FK conditioning to whole-body contact tasks and validate the design choices via downstream policy success rate.\n\n⚠️ USER REQUIREMENT TRADEOFF — EXPLICIT FLAG: The user specified three required evaluation platforms: Isaac Lab G1 locomanipulation, HumanoidBench whole-body tasks, and RoboCasa365 humanoid kitchen. The CoRL 2026 scoped submission covers ONLY Isaac Lab G1 locomanipulation (1 of 3 required benchmarks). HumanoidBench and RoboCasa365 are deferred entirely to ICLR 2027. The user should make an explicit decision: (option A) target CoRL 2026 with 1-of-3 benchmark coverage and full results on all three platforms at ICLR 2027; (option B) skip CoRL 2026 entirely and target ICLR 2027 from the start with full user-required benchmark coverage.",
  "opportunity": "GR00T-Dreams/DreamGen (2025) validated the video-diffusion → IDM pipeline for tabletop manipulation. Dream2Act (arXiv:2603.19709, March 2026) extended to full-body G1 whole-body contact interaction by generating video in robot-native visual space — hallucinating the G1 robot body via Seedance 2.0 — then applying post-generation kinematic recovery: (a) native 2D pose estimation, (b) 2D-to-3D lifting, (c) URDF-constrained IK. This post-hoc extraction approach achieves 37.5% overall success across four whole-body contact tasks but is inherently corrective: it recovers joint-angle-consistent trajectories from video frames generated without kinematic constraints, which can introduce temporal jitter and joint-limit violations that propagate into IDM training. URDF-DiT addresses this at the source — FK heatmaps injected throughout denoising prevent kinematically infeasible transitions during generation rather than correcting them afterward. Dream2Act's two distinct components — (A) robot-native video generation modality and (B) post-generation URDF-constrained IK — are the baseline against which URDF-DiT's in-loop conditioning is tested.\n\nBridgeV2W (arXiv:2602.03793, February 3, 2026) established the ControlNet+URDF+video-DiT paradigm for arm/dual-arm manipulation: it converts coordinate-space robot actions into pixel-aligned binary embodiment masks rendered from URDF and camera parameters, injects them via a ControlNet-style pathway into a pretrained video DiT, and introduces a flow-based motion loss to prevent overfitting to static backgrounds. Evaluated on DROID (single-arm) and AgiBot-G1 (dual-arm) for goal-conditioned planning and policy evaluation. BridgeV2W's conditioning signal is a binary occupancy mask encoding link presence and location — it does not encode individual joint angles, temporal joint-angle transitions, or joint-limit constraints. URDF-DiT applies continuous per-joint Gaussian FK heatmaps, extends to full-body humanoid 29 DoF, and targets IDM synthetic training data generation.\n\nEA-WM (arXiv:2605.06192, May 7 2026) validates that in-loop kinematic heatmap injection into Wan 2.2 cross-attention enforces kinematic consistency — using KVAFs (Gaussian heatmaps at projected joint/end-effector positions) via event-aware bidirectional dual-stream fusion. But EA-WM evaluates arm manipulation only (WorldArena benchmark), requires joint fine-tuning of both video and kinematic branches, and produces no policy training output. URDF-DiT extends to full-body 29 DoF with a ControlNet-style frozen backbone (~40% fewer trainable parameters) and adds the IDM→policy pipeline.\n\nA concurrent parallel paradigm is established by HumanX (arXiv:2602.02473, February 2026): XGen generates physically plausible humanoid interaction data from human videos via motion retargeting (3D human pose extraction via GVHMR → IK optimization to humanoid skeleton) + physics simulation (IsaacGym for non-contact phases, force-closure optimization for contact), without video diffusion. XMimic is a unified imitation learning framework with teacher-student distillation (no IDM). Evaluates on 10 skills across 5 domains (basketball, football, badminton, cargo pickup, reactive fighting) with zero-shot G1 transfer; achieves 8× higher generalization success than prior methods. HumanX validates synthetic humanoid training data via the simulation paradigm; URDF-DiT's opportunity is specifically the video-diffusion → IDM pathway — testing whether FK-conditioned video generation can produce training data of comparable quality through the video synthesis route.\n\nTogether, BridgeV2W (Feb 2026) and EA-WM (May 2026) establish ControlNet+URDF conditioning into video DiTs as a validated paradigm for arm/dual-arm manipulation. The introduction acknowledges both as prior work establishing the paradigm and positions URDF-DiT as the first application to full-body humanoid 29 DoF whole-body contact tasks with explicit IDM training data generation.\n\nVAG (arXiv:2604.09330, April 2026) introduces dual-stream flow matching jointly denoising video and action for arm manipulation (7–16 DoF, 45% on AgiBot G1 dual-arm grasping vs. 8% IDM baseline) but explicitly acknowledges in its Limitations and Future Work section that 'video generation has not been influenced by the action branch, wasting beneficial control signals.' EVA (arXiv:2603.17808, March 2026) enforces executability via learned IDM reward signals (RL post-training, soft constraint) on bimanual tabletop tasks — distinct from URDF-DiT's hard geometric constraint at every diffusion step.\n\n⚠️ USER REQUIREMENT TRADEOFF: The user required evaluation on Isaac Lab G1 locomanipulation, HumanoidBench, and RoboCasa365. CoRL 2026 covers only Isaac Lab G1 locomanipulation. Full benchmark coverage requires ICLR 2027. This is a deliberate scope decision with direct implications for whether the work meets the user's original requirements at submission time.\n\nVENUE/TIMELINE NOTE: Today is May 10, 2026. CoRL 2026 deadline is May 29 — 19 days away. CoRL 2026 is feasible ONLY in auto-research mode with 8+ H100s available from Day 1, scoped to Isaac Lab G1 locomanipulation + Dream2Act ball kicking contextual comparison, with 2 ablations and a concrete Day 14 decision gate (see resource_estimate). Manual mode (4–6 months) and HIL mode (5–8 weeks) are incompatible with CoRL 2026.",
  "landscape": "GR00T-Dreams/DreamGen (arXiv 2025): fine-tunes Cosmos-Predict2 with language conditioning; extracts pseudo-actions via IDM or latent action model. No URDF kinematic constraint. Tabletop manipulation only.\n\nDream2Act (arXiv:2603.19709, March 2026): Two distinct components must be distinguished — (A) VIDEO GENERATION MODALITY: generates in robot-native visual space by hallucinating the G1 robot body (not retargeting from human video) using Seedance 2.0, achieving morphological consistency; (B) KINEMATIC EXTRACTION: post-generation pipeline applying native 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK to convert pixel-space poses to joint trajectories. Achieves 37.5% overall success across four whole-body contact interaction benchmarks (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%) vs. 0% for conventional retargeting. Primary stated limitation is inference latency as an offline planner. Dream2Act targets zero-shot real-robot execution; URDF-DiT targets synthetic IDM training data generation — complementary goals. Ablation A tests whether in-loop FK conditioning (URDF-DiT) outperforms Dream2Act's post-generation URDF-IK (approach B) for IDM training data quality.\n\nHumanX (arXiv:2602.02473, February 2026): 'HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos' — XGen synthesizes physically plausible humanoid training data from human videos via motion retargeting (3D human pose extraction via GVHMR → IK optimization to humanoid skeleton) + physics simulation (IsaacGym for non-contact phases, force-closure optimization for contact phases), without video diffusion. XMimic is a unified imitation learning framework with teacher-student distillation (no IDM). Evaluates on 10 skills across 5 domains (basketball, football, badminton, cargo pickup, reactive fighting) with zero-shot transfer to physical Unitree G1; achieves 8× higher generalization success than prior methods. Key distinction from URDF-DiT: HumanX generates humanoid training data via physics-based motion retargeting from human video — a simulation-space synthesis paradigm; URDF-DiT generates humanoid training data via kinematically constrained RGB video diffusion → IDM — a video-space synthesis paradigm. HumanX does not use video diffusion, has no IDM pipeline, and does not inject kinematic conditioning into a generative model's attention layers. The two approaches are paradigmatically complementary (simulation vs. video diffusion) and both validate synthetic humanoid training data generation. A CoRL reviewer expecting citation of concurrent synthetic humanoid data work should see HumanX cited with this differentiation.\n\nBridgeV2W (arXiv:2602.03793, February 3, 2026): 'BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks' — converts coordinate-space robot actions into pixel-aligned binary embodiment masks rendered from URDF and camera parameters, injected via ControlNet-style pathway into a pretrained video DiT; introduces a flow-based motion loss to focus learning on dynamic task-relevant regions and prevent background overfitting; evaluates on DROID (single-arm) and AgiBot-G1 (dual-arm) for goal-conditioned planning and policy evaluation. BridgeV2W establishes the ControlNet+URDF+video-DiT paradigm for arm/dual-arm manipulation. URDF-DiT differentiates on: (a) full-body humanoid 29 DoF (pelvis, legs, torso, arms, hands) vs. arm/dual-arm scope; (b) continuous per-joint Gaussian FK heatmaps encoding joint-angle-specific kinematic structure and joint-limit constraints at every denoising step vs. binary pixel-aligned occupancy masks (encoding link presence/location but not individual joint angles, temporal joint-angle transitions, or joint-limit compliance); (c) IDM synthetic training data generation pipeline targeting whole-body contact tasks vs. goal-conditioned planning and policy evaluation. The introduction acknowledges BridgeV2W alongside EA-WM as establishing the ControlNet+URDF paradigm and positions URDF-DiT as the first extension to full-body humanoid 29 DoF whole-body contact tasks.\n\nEA-WM (arXiv:2605.06192, May 2026): 'EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields' — injects Kinematic-to-Visual Action Fields (KVAF: Gaussian heatmaps at projected end-effector/joint locations) via event-aware bidirectional dual-stream fusion into Wan 2.2; evaluates on WorldArena benchmark for arm manipulation tasks; requires joint fine-tuning of both video and kinematic streams; no policy training pipeline (action recovery detection rate ~0.45). Note: 'EA' = Event-Aware, not Embodiment-Aware. Together with BridgeV2W, EA-WM establishes in-loop URDF-derived conditioning into video DiTs as validated for arm manipulation. URDF-DiT differentiates on three empirically testable axes: (a) full-body 29+ DoF vs. arm manipulation — tested by full-body vs. end-effector ablation; (b) ControlNet-style frozen backbone vs. joint fine-tuning — ~40% fewer trainable parameters; (c) explicit IDM→policy pipeline vs. no policy output.\n\nVAG (arXiv:2604.09330, April 2026): dual-stream video-action generation using flow matching for tabletop arm manipulation (7–16 DoF); 45% on AgiBot G1 dual-arm grasping vs. 8% ResNet+IDM baseline; no URDF kinematic constraints; authors explicitly acknowledge in the Limitations and Future Work section: 'video generation has not been influenced by the action branch, wasting beneficial control signals.' No full-body humanoid evaluation. URDF-DiT's in-loop FK heatmap injection directly addresses VAG's stated limitation while extending to 29+ DoF whole-body tasks.\n\nMotuBrain (arXiv:2604.27792, April 2026): 'MotuBrain: An Advanced World Action Model for Robot Control' — UniDiffuser formulation with three-stream Mixture-of-Transformers (video, action, language) jointly supporting five inference distributions: policy learning, world modeling, video generation, inverse dynamics, and joint video-action prediction; 95%+ average success on RoboTwin 2.0; tops WorldArena EWMScore; adapts to new humanoid embodiments with 50–100 trajectories. URDF-DiT differentiates: MotuBrain targets direct policy learning via joint video-action diffusion using robot-collected trajectory data; URDF-DiT generates FK-constrained synthetic training data in robot-native visual space without requiring robot-collected trajectory fine-tuning data, and validates whether in-loop geometric URDF FK conditioning improves IDM training data quality for whole-body contact tasks.\n\nEVA (arXiv:2603.17808, March 2026): closes executability gap via RL post-training using IDM-derived reward signals penalizing embodiment violations (joint-limit violations, velocity/acceleration/jerk penalties); evaluates on RoboTwin 2.0 bimanual manipulation. Key distinction: EVA = learned IDM reward (soft executability constraint via RL post-training); URDF-DiT = explicit geometric URDF FK heatmaps (hard geometric constraint injected at every diffusion step). EVA evaluates bimanual tabletop; URDF-DiT targets full-body 29+ DoF contact interaction.\n\nFlowAct-R1 (arXiv:2601.10103, January 2026): 'FlowAct-R1: Towards Interactive Humanoid Video Generation' — real-time interactive digital human character animation via MMDiT chunkwise diffusion with audio/text-based full-body control at 25fps; targets NPC-style animated digital humans for real-time interaction (lip-sync, facial expressions, body gestures), not physical robot embodiment; no URDF kinematic structure, no physical robot joint constraints, no IDM policy extraction pipeline. Differentiation: interactive character animation use case vs. offline robot training data generation; audio/text conditioning vs. geometric URDF FK heatmaps.\n\nKStar Diffuser (arXiv:2503.10743, CVPR 2025): URDF-parsed spatial-temporal graph with differentiable FK for bimanual arm action diffusion (68.2% ± 2.1 success with 100 demos vs. 33.9% for PerAct2); operates at the policy/action layer not video synthesis — complementary to URDF-DiT rather than competing.\n\nKinema4D (arXiv:2603.16669, March 2026, NTU): 'Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation' — action-conditioned 4D generative simulator that drives a URDF-based 3D robot via kinematics, projects the robot trajectory into a pointmap, then conditions a diffusion transformer to generate synchronized RGB+pointmap world sequences for spatiotemporal simulation (Robo4D-200k dataset, 201k episodes). Key distinction from URDF-DiT: (a) Kinema4D uses a decoupled architecture — URDF kinematics project into pointmap which conditions a separate generative model — rather than injecting FK heatmaps directly into RGB video DiT cross-attention in-loop during denoising; (b) Kinema4D targets 4D spatiotemporal world simulation (synchronized RGB+pointmap sequences for environment reaction dynamics and scene realism) rather than IDM training data generation; (c) Kinema4D provides no IDM extraction pipeline or downstream policy training evaluation. Kinema4D and URDF-DiT are complementary: the former handles 4D world simulation fidelity, the latter targets RGB video generation for IDM policy training data.\n\nControllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026): cascaded text-to-2D-skeleton → skeleton-to-video pipeline validates per-frame 2D pose-sequence conditioning in video diffusion for human motion synthesis — closest video-generation analogue to URDF-DiT's conditioning mechanism, but targets human motion not robot URDF kinematics or policy extraction.\n\nX-Humanoid (arXiv Dec 2025): replaces human with humanoid in video via Wan 2.2; no URDF constraint injection. MITTY (arXiv 2025): human-to-robot video diffusion without kinematic enforcement. G-DReaM (arXiv 2025): graph-conditioned diffusion for cross-embodiment motion retargeting on motion sequences, not RGB video.\n\nHumanoidBench (arXiv:2403.10506, 2024): 27 whole-body tasks (H1/Digit robots, MuJoCo); deferred to ICLR 2027 full paper. RoboCasa365 (arXiv:2603.04356, ICLR 2026): 365 kitchen tasks with humanoid support; deferred to ICLR 2027 full paper.",
  "approach": "SYSTEM CONTRIBUTION: URDF-DiT is the first system to inject full-body URDF FK heatmaps into a video DiT throughout the denoising process for humanoid whole-body contact task training data generation, producing a complete IDM → policy training pipeline for 29-DoF whole-body contact tasks. The ControlNet+URDF+video-DiT paradigm is established for arm/dual-arm manipulation by BridgeV2W (arXiv:2602.03793, Feb 2026) and EA-WM (arXiv:2605.06192, May 2026). URDF-DiT extends this paradigm to full-body humanoid 29 DoF — requiring continuous per-joint Gaussian FK heatmaps (not binary occupancy masks) and motivating a ControlNet-style frozen backbone (rather than EA-WM's joint fine-tuning, ~40% fewer trainable parameters). Two key design choices are validated via ablation against downstream Isaac Lab G1 policy success rate:\n\nABLATION A (in-loop vs. post-hoc kinematic enforcement): URDF-DiT vs. vanilla Wan 2.2 + post-hoc URDF-IK — same IDM, same downstream Isaac Lab G1 policy training procedure, same evaluation benchmark, only the video source differs. URDF-DiT-generated videos vs. vanilla Wan 2.2 videos post-processed with URDF-IK (the same IK pipeline as Dream2Act's kinematic extraction stage). This measures whether conditioning throughout denoising — preventing kinematically infeasible frame transitions — outperforms correcting them afterward for IDM training data quality. Neither BridgeV2W nor EA-WM tests this comparison: both evaluate video generation quality metrics, not downstream IDM training data quality.\n\nABLATION B (full-body 29 DoF vs. end-effector-only scope): Same IDM, same downstream policy evaluation — only the conditioning scope differs. Full-body 29 DoF (pelvis, legs, torso, arms, hands) vs. end-effector-only (~5 DoF wrist/hand positions). End-effector-only conditioning approximates the scope of BridgeV2W (binary arm/hand masks) and EA-WM (arm end-effector heatmaps), both applied to arm manipulation. For whole-body CONTACT tasks (ball kicking, pick-and-place with locomotion), leg and torso kinematics during approach and weight-shifting phases are hypothesized to affect interaction quality in ways that arm-scope conditioning cannot capture. Ablation B tests whether the scope extension from arm manipulation to full-body humanoid is necessary for whole-body contact task IDM data quality — the paper's core experimental differentiation from the BridgeV2W + EA-WM arm-manipulation landscape.\n\nARCHITECTURE: URDF-DiT uses a ControlNet-style conditioning module — Wan 2.2 backbone weights fully frozen; only the FK-heatmap encoder and zero-conv injection layers are trained — that encodes per-frame G1 URDF forward-kinematics outputs (all 29 DoF, projected to the camera plane via differentiable FK) as structured Gaussian joint-position heatmaps and injects them into the cross-attention layers of the Wan 2.2 DiT. Unlike EA-WM's event-aware bidirectional dual-stream fusion (requiring joint fine-tuning of both video and kinematic branches) and BridgeV2W's binary occupancy masks (encoding link presence but not individual joint angles or joint-limit constraints), URDF-DiT's continuous per-joint Gaussian heatmaps encode joint-angle-specific kinematic structure and enable the FK residual consistency loss to penalize joint-limit violations at every denoising step. The ControlNet-style frozen backbone concentrates all learning in the conditioning module, reducing trainable parameters ~40% versus EA-WM's architecture — enabling the full pipeline within ≤200 H100-hours. Full-body G1 scope (29 DoF: pelvis, legs, torso, arms, hands) is the embodiment extension validated by Ablation B.\n\nDIFFERENTIATING DREAM2ACT PRECISELY: Dream2Act operates as follows: (A) video generation modality = robot-native visual space (Seedance 2.0 hallucinating the G1 body for morphological consistency — not retargeting from human video); (B) kinematic extraction = post-generation pipeline applying 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK (applied AFTER all video frames are generated). URDF-DiT vs. Dream2Act is not a comparison of visual generation approach — both generate in robot-native-compatible space — but specifically a test of whether kinematic constraints applied IN-LOOP during denoising (URDF-DiT) produce better IDM training data than constraints applied POST-GENERATION (Dream2Act's approach B).\n\nJoint-angle sequences are sampled from an Isaac Lab G1 motion library covering locomotion primitives and upper-body reach plans, projected onto the camera plane, and encoded as per-frame kinematic tokens injected into DiT cross-attention.\n\nFK RESIDUAL LOSS: A per-frame FK residual consistency loss penalizes deviations between joint positions in generated video frames and URDF FK predictions from the conditioning signal. This is a kinematic consistency mechanism operating on geometric structure — reducing temporal joint jitter, preventing joint-limit violations during denoising. It is NOT a visual domain gap bridge. The visual appearance domain gap between Wan 2.2 outputs and Isaac Lab rendering is separately addressed via domain-randomized Isaac Lab rendering during IDM training (sampling lighting, camera noise, surface material variation to statistically overlap with Wan 2.2's output distribution). Two distinct mechanisms for two distinct problems.\n\nThe sim-bootstrapped IDM is trained on (frame_t, frame_{t+k}, joint-velocity) tuples from G1 Isaac Lab rollouts under domain-randomized conditions, then applied zero-shot to URDF-DiT-generated videos. If domain gap remains too large (joint-limit violation rate >15% in generated videos at the 3-day checkpoint), a contingency IDM adapter fine-tuned on ~200 URDF-DiT frame pairs matched to Isaac Lab rollouts via kinematic alignment (~8h additional compute) activates.\n\nEVALUATION STRATEGY:\n\n(1) CoRL 2026 scoped (2 benchmarks, 2 ablations): Isaac Lab G1 locomanipulation pick-and-place (primary); Dream2Act ball kicking (contextual comparison — 40% success, distinct use case: zero-shot real-robot execution vs. synthetic training data); Ablation A (in-loop URDF-DiT vs. post-hoc vanilla Wan 2.2 + URDF-IK); Ablation B (29 DoF full-body vs. end-effector-only). NOTE: covers 1 of 3 user-required benchmarks.\n\n(2) ICLR 2027 full paper (all user-required platforms): Isaac Lab G1 locomanipulation (multi-task: pick-and-place, reaching, pick-navigate-place); HumanoidBench H1 whole-body (carry + cabinet); RoboCasa365 humanoid kitchen (pick-and-place in kitchen); Dream2Act ball kicking + bag punching; Ablations A and B plus: ControlNet-style frozen backbone vs. EA-WM-style event-aware bidirectional fusion; URDF-DiT geometric FK conditioning vs. EVA-style learned IDM reward.",
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
          "strong_submission_additionally": "Full-body 29 DoF conditioning ≥ end-effector-only conditioning by ≥ 5 pp on downstream policy success (Ablation B strongly positive — validates the 29 DoF scope claim empirically, differentiating from BridgeV2W and EA-WM arm-robot conditioning scope)"
        },
        "submit_with_reframing": {
          "condition": "Ablation A positive (URDF-DiT ≥ baseline + 5 pp) AND absolute success ≥ 20% AND violation rate ≤ 10% — but Ablation B shows < 3 pp improvement from full-body vs. end-effector-only conditioning.",
          "reframing": "If Ablation B < 3 pp, the paper cannot claim 'full-body 29 DoF conditioning is necessary' — this would effectively validate that arm-scope conditioning (as in BridgeV2W, EA-WM) suffices for humanoid whole-body contact tasks. However, if Ablation A remains strongly positive (≥ 5 pp), the paper can be reframed around Ablation A as its primary novel contribution: 'in-loop FK conditioning outperforms post-hoc URDF-IK for IDM training data quality on whole-body contact tasks.' Neither BridgeV2W nor EA-WM test this comparison, so Ablation A remains a genuinely novel empirical finding. The reframed paper leads with Ablation A and treats Ablation B as a negative result that simplifies the conditioning design recommendation.",
          "critical_caveat": "⚠️ If Ablation B < 3 pp AND Ablation A is also weak (< 5 pp improvement over baseline), pivot directly to ICLR 2027 — no CoRL-level contribution remains. Do NOT attempt CoRL reframing if both ablations are inconclusive."
        },
        "pivot_to_iclr_2027": {
          "condition": "ANY of the following: (1) URDF-DiT fails to exceed baseline by ≥ 5 pp (Ablation A inconclusive); (2) joint-limit violation rate > 15% in URDF-DiT generated videos (FK conditioning not working — triggers IDM adapter contingency, but if adapter also fails, pivot); (3) absolute policy success < 15% (IDM domain gap too large for 19-day timeline); (4) contingency IDM adapter required AND results still negative after adapter training; (5) Ablation A < 5 pp AND Ablation B < 3 pp simultaneously (both ablations inconclusive — no CoRL-level claim survives)",
          "note": "ICLR 2027 pivot preserves all GPU investment — same implementation, full benchmark coverage (all 3 user-required platforms), full ablation suite including ControlNet-vs.-EA-WM-fusion and geometric-FK-vs.-EVA-RL comparisons. Pivot to ICLR 2027 is not a failure; it is the correct decision if CoRL results do not meet the above thresholds."
        }
      },
      "scope": "2 benchmarks (Isaac Lab G1 locomanipulation + Dream2Act ball kicking contextual comparison), 2 ablations (A: in-loop URDF-DiT vs. post-hoc vanilla Wan 2.2 + URDF-IK; B: full-body 29 DoF vs. end-effector-only conditioning). HumanoidBench and RoboCasa365 deferred to ICLR 2027. NOTE: covers 1 of 3 user-required benchmarks.",
      "feasibility_risk": "HIGH. Estimated 60–70% probability of obtaining submittable results by May 29 in auto mode. Key risks: (1) ControlNet training non-convergence adds 1–2 days; (2) IDM domain gap exceeds FK residual loss + domain randomization, triggering 8h contingency adapter; (3) Isaac Lab simulation evaluation wall-clock bottleneck if environment resets are slow. Day 14 decision gate with concrete thresholds provides an unambiguous pivot trigger.",
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
    "CoRL 2026 (paper deadline May 29, 2026 — 19 days from today): FEASIBLE only in auto-research mode with 8+ H100s available starting May 10. ⚠️ COVERS ONLY 1 OF 3 USER-REQUIRED BENCHMARKS (Isaac Lab G1 locomanipulation only; HumanoidBench and RoboCasa365 deferred to ICLR 2027). Scoped to 2 ablations: (A) in-loop URDF-DiT vs. post-hoc vanilla Wan 2.2 + URDF-IK extraction; (B) full-body 29 DoF vs. end-effector-only conditioning. Introduction acknowledges BridgeV2W (Feb 2026) + EA-WM (May 2026) as establishing ControlNet+URDF for arm/dual-arm robots; positions URDF-DiT as first extension to full-body humanoid 29 DoF whole-body contact tasks. Day 14 decision gate: submit if URDF-DiT ≥ 20% success AND ≥ 5 pp improvement over baseline AND joint-limit violation rate ≤ 10%; pivot to ICLR 2027 otherwise. Reframing contingency: valid ONLY if Ablation A ≥ 5 pp regardless of Ablation B result; if both ablations inconclusive, pivot directly to ICLR 2027. Estimated 60–70% probability of submittable results by deadline. If Day 14 shows negative results, same implementation pivots to ICLR 2027 with no wasted GPU investment.",
    "ICLR 2027 (expected submission deadline ~October 2026; official announcement pending at iclr.cc): RECOMMENDED if full user-required benchmark coverage is the priority. Covers all 3 required platforms (Isaac Lab G1 locomanipulation, HumanoidBench H1 whole-body, RoboCasa365 humanoid kitchen) and full ablation suite (A, B, ControlNet-vs.-bidirectional-fusion, geometric-FK-vs.-EVA-RL). All operation modes (manual 4–6 months, HIL 5–8 weeks, auto 1–2 weeks on 8 H100s) are compatible.",
    "CoRL 2027 (fallback if ICLR 2027 results are negative)"
  ],
  "key_references": [
    "DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories (arXiv 2025)",
    "Dream2Act (arXiv:2603.19709, March 2026) — TWO DISTINCT COMPONENTS: (A) video generation modality: robot-native visual space by hallucinating G1 robot body via Seedance 2.0 (not retargeting from human video); (B) kinematic extraction: post-generation pipeline via 2D pose estimation → 2D-to-3D lifting → URDF-constrained IK. Achieves 37.5% success (ball-kicking 40%, sofa-sitting 70%, bag-hitting 30%, box-hugging 10%); inference latency is primary stated limitation; targets zero-shot real-robot execution. URDF-DiT Ablation A tests whether in-loop FK conditioning outperforms Dream2Act's approach (B) for synthetic IDM training data quality.",
    "HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos (arXiv:2602.02473, February 2026) — XGen generates physically plausible humanoid training data from human videos via motion retargeting (3D human pose extraction via GVHMR → IK optimization to humanoid skeleton) + physics simulation (IsaacGym for non-contact phases, force-closure optimization for contact phases), without video diffusion; XMimic is a unified imitation learning framework with teacher-student distillation (no IDM). Evaluates on 10 skills across 5 domains (basketball, football, badminton, cargo pickup, reactive fighting) with zero-shot transfer to physical Unitree G1; achieves 8× higher generalization success than prior methods. Key distinction from URDF-DiT: HumanX = physics-based motion retargeting from human video (simulation-space synthesis paradigm, no IDM); URDF-DiT = kinematically constrained RGB video diffusion → IDM (video-space synthesis paradigm). Cited as concurrent work demonstrating synthetic humanoid training data viability via the simulation pathway — URDF-DiT's contribution is specific to the video-diffusion → IDM pathway.",
    "BridgeV2W (arXiv:2602.03793, February 3, 2026) — establishes ControlNet+URDF+video-DiT paradigm for arm/dual-arm manipulation: converts coordinate-space actions to pixel-aligned binary embodiment masks rendered from URDF + camera parameters → ControlNet pathway → pretrained video DiT; flow-based motion loss prevents background overfitting; evaluates on DROID (single-arm) and AgiBot-G1 (dual-arm) for goal-conditioned planning and policy evaluation. URDF-DiT differentiates: (a) full-body humanoid 29 DoF vs. arm/dual-arm scope; (b) continuous per-joint Gaussian FK heatmaps encoding joint-angle-specific kinematic structure and joint-limit constraints vs. binary pixel-aligned occupancy masks encoding link presence/location only; (c) IDM synthetic training data generation pipeline vs. goal-conditioned planning and policy evaluation.",
    "EA-WM (arXiv:2605.06192, May 2026) — primary concurrent work; injects KVAF kinematic heatmaps into Wan 2.2 via event-aware bidirectional dual-stream fusion; WorldArena benchmark for arm manipulation; requires joint fine-tuning of both branches; no policy training pipeline. Note: 'EA' = Event-Aware, not Embodiment-Aware. Together with BridgeV2W, establishes in-loop URDF-derived conditioning into video DiTs for arm manipulation. URDF-DiT differentiators are empirically testable: full-body 29 DoF vs. arm manipulation (Ablation B), ControlNet frozen backbone vs. joint fine-tuning (~40% fewer trainable parameters), explicit IDM→policy pipeline.",
    "VAG (arXiv:2604.09330, April 2026) — jointly denoises video+action via flow matching for tabletop arm manipulation (7–16 DoF); 45% on AgiBot G1 dual-arm grasping vs. 8% IDM baseline; no URDF kinematic constraints; authors explicitly acknowledge in the Limitations and Future Work section: 'video generation has not been influenced by the action branch, wasting beneficial control signals.' URDF-DiT's FK heatmap injection directly addresses this limitation while extending to 29+ DoF.",
    "MotuBrain (arXiv:2604.27792, April 2026) — UniDiffuser + three-stream Mixture-of-Transformers (video, action, language) supporting five inference distributions including inverse dynamics and joint video-action prediction; 95%+ on RoboTwin 2.0; tops WorldArena EWMScore; adapts to new humanoid embodiments with 50–100 trajectories. URDF-DiT differentiates: MotuBrain targets direct policy learning via joint video-action diffusion using robot-collected trajectory data; URDF-DiT generates FK-constrained synthetic training data in robot-native visual space without robot-trajectory fine-tuning.",
    "EVA (arXiv:2603.17808, March 2026) — executability via RL post-training using IDM-derived reward signals; evaluates bimanual tabletop. Key distinction: EVA = soft learned reward constraint; URDF-DiT = hard geometric FK constraint at every diffusion step. ICLR 2027 ablation directly compares these two executability enforcement approaches.",
    "FlowAct-R1 (arXiv:2601.10103, January 2026) — real-time interactive digital human character animation via MMDiT chunkwise diffusion with audio/text-based full-body control at 25fps; targets NPC-style animated digital humans (lip-sync, expressions, body gestures), not physical robot embodiment; no URDF kinematic constraints, no robot joint angles, no IDM policy extraction pipeline.",
    "KStar Diffuser (arXiv:2503.10743, CVPR 2025) — URDF-parsed spatial-temporal graph with differentiable FK for bimanual action diffusion (68.2% vs. 33.9% for PerAct2); policy layer not video synthesis; complementary.",
    "Kinema4D (arXiv:2603.16669, March 2026, NTU): 'Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation' — action-conditioned 4D generative simulator that drives a URDF-based 3D robot via kinematics, projects the robot trajectory into a pointmap, then conditions a diffusion transformer to generate synchronized RGB+pointmap world sequences for spatiotemporal simulation (Robo4D-200k dataset, 201k episodes). Key distinction from URDF-DiT: (a) decoupled architecture — URDF kinematics project into pointmap which conditions a separate generative model, rather than injecting FK heatmaps directly into RGB video DiT cross-attention in-loop during denoising; (b) targets 4D spatiotemporal world simulation (synchronized RGB+pointmap sequences for environment reaction dynamics) rather than IDM training data generation; (c) no IDM extraction pipeline or downstream policy training evaluation. Kinema4D and URDF-DiT are complementary: the former handles 4D world simulation fidelity, the latter targets RGB video generation for IDM policy training data.",
    "Controllable Complex Human Motion Video Generation (arXiv:2603.08028, March 2026) — validates per-frame 2D skeleton-sequence conditioning in video diffusion for human motion synthesis; closest video-generation analogue to URDF-DiT's conditioning mechanism; targets human motion not robot URDF kinematics or policy extraction.",
    "HumanoidBench (arXiv:2403.10506, 2024) — 27 tasks (H1/Digit, MuJoCo); ICLR 2027 cross-embodiment evaluation target.",
    "RoboCasa365 (arXiv:2603.04356, ICLR 2026) — 365 kitchen tasks with humanoid support; ICLR 2027 household generalization evaluation.",
    "X-Humanoid (arXiv Dec 2025); MITTY (arXiv 2025); G-DReaM (arXiv 2025)"
  ],
  "description": "URDF-DiT generates kinematically valid synthetic training videos for humanoid whole-body contact tasks by injecting 29-DoF URDF FK heatmaps into Wan 2.2 DiT cross-attention throughout the denoising process, then extracting joint-velocity actions via IDM for downstream policy training on Isaac Lab G1. Two design decisions are validated via ablation against downstream policy success rate: (A) in-loop FK conditioning throughout denoising vs. post-hoc URDF-IK applied to unconstrained video; (B) full-body 29-DoF conditioning vs. end-effector-only conditioning.\n\n⚠️ USER REQUIREMENT TRADEOFF: The user required evaluation on three platforms — Isaac Lab G1 locomanipulation, HumanoidBench whole-body tasks, and RoboCasa365 humanoid kitchen. The CoRL 2026 submission covers ONLY Isaac Lab G1 locomanipulation (1 of 3). The user must decide: (A) target CoRL 2026 with partial benchmark coverage now + ICLR 2027 for full coverage; or (B) skip CoRL 2026 and target ICLR 2027 directly with full coverage from the start. This is not a footnote — it is a deliberate scope decision.\n\nThe ControlNet+URDF+video-DiT paradigm for arm/dual-arm manipulation is established: BridgeV2W (arXiv:2602.03793, Feb 2026) injected URDF-rendered binary pixel-aligned embodiment masks via ControlNet into a pretrained video DiT for goal-conditioned planning on DROID and AgiBot-G1 dual-arm; EA-WM (arXiv:2605.06192, May 2026) injected per-joint Gaussian heatmaps (KVAFs) into Wan 2.2 via event-aware bidirectional fusion for arm manipulation on WorldArena. The introduction acknowledges both as prior work establishing the paradigm and positions URDF-DiT as the first extension to full-body humanoid 29-DoF whole-body contact tasks with explicit IDM training data generation.\n\nKey landscape context: Dream2Act (arXiv:2603.19709) generates in robot-native visual space then applies post-generation URDF-IK (approach B) — Ablation A tests whether in-loop FK conditioning outperforms this for IDM data quality, a comparison neither BridgeV2W nor EA-WM makes. HumanX (arXiv:2602.02473, Feb 2026) demonstrates a parallel synthesis paradigm: XGen (motion retargeting + IsaacGym physics simulation, no video diffusion) + XMimic (imitation learning, no IDM), achieving 8× generalization improvement on sports/cargo tasks with zero-shot G1 transfer — a physics-simulation paradigm complementary to URDF-DiT's video-diffusion paradigm, cited as concurrent work validating synthetic humanoid training data generation. Kinema4D (arXiv:2603.16669, March 2026, NTU) generates synchronized RGB+pointmap sequences via URDF-driven kinematics projected into pointmaps conditioning a diffusion transformer — a decoupled 4D world simulation architecture, distinct from URDF-DiT's in-loop FK injection into RGB video DiT cross-attention and IDM extraction pipeline.\n\nKey technical differentiators: (1) vs. Dream2Act: in-loop kinematic constraint enforcement (URDF-DiT) vs. post-generation kinematic extraction (Dream2Act approach B) — tested directly by Ablation A; (2) vs. BridgeV2W + EA-WM: continuous per-joint Gaussian FK heatmaps encoding joint angles and joint-limit constraints (not binary occupancy masks), ControlNet-style frozen backbone (~40% fewer trainable parameters than EA-WM), full-body 29-DoF scope, explicit IDM→policy pipeline; (3) vs. HumanX: video-diffusion paradigm (URDF-DiT) vs. physics-simulation paradigm (HumanX) — paradigmatically distinct, both validate synthetic humanoid training data generation; (4) FK residual consistency loss enforces kinematic geometry during denoising; visual domain gap addressed separately via domain-randomized Isaac Lab rendering during IDM training — two distinct mechanisms for two distinct problems."
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

### Round 2 review
Verdict: revise
Issues: ["USER REQUIREMENT VIOLATION — TARGET VENUE: The proposal has silently replaced CoRL 2026 (user's explicit target, deadline May 29, 2026) with ICLR 2027 (October 2026 deadline). This violates the primary constraint. The generator must either (a) produce a concrete CoRL 2026 plan with preliminary results achievable in ≤20 days, or (b) explicitly present the infeasibility argument to the user and request venue scope change before proceeding.", "USER REQUIREMENT VIOLATION — TIMELINE: Manual mode (4–6 months) and HIL mode (5–8 weeks) both violate the user's ≤20-day hard constraint. Only auto mode with 8+ H100s (1–2 weeks) approaches feasibility. If targeting CoRL 2026, the auto mode timeline with specific GPU allocation must be the primary mode, not the fallback.", "USER REQUIREMENT VIOLATION — EVALUATION PLATFORMS: User specified 'Test on Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench.' The proposal evaluates exclusively on three Dream2Act benchmarks (ball kicking, bag punching, box hugging). None of the user's required evaluation platforms are included.", "MISSED CRITICAL CONCURRENT WORK — VAG (arXiv:2604.09330, April 2026): VAG (Dual-Stream Video-Action Generation) jointly denoises video and robot action streams via flow matching, directly solving the paired data synthesis problem without a two-stage IDM. This paper is from April 2026 and directly competes with URDF-DiT's IDM extraction pipeline. The proposal's landscape section must acknowledge VAG and explain why URDF-DiT's explicit URDF kinematic conditioning offers advantages over VAG's implicit action learning, otherwise the IDM contribution is largely subsumed.", "RESOURCE ESTIMATE CONCERN — ControlNet Training: Community reports indicate Wan-family ControlNet training requires ~72h on RTX 3090 for similar tasks (implied ~35–50h on H100 depending on dataset size). The proposed 35h may be achievable but is at the boundary — the estimate should reflect worst-case sensitivity (e.g., if longer context/temporal attention training increases compute 1.5–2x, the manual budget risks exceeding 200h total).", "IDM DOMAIN GAP — MITIGATION UNPROVEN: The FK residual consistency loss during video generation (pulling generated frames toward sim-renderable kinematics) is a reasonable hypothesis but has no empirical precedent specifically for bridging Wan 2.2 generation distribution → Isaac Lab sim rollout distribution for IDM application. The proposal should cite or test whether this loss actually reduces IDM error or whether domain-randomized rendering alone is sufficient."]
Feedback: The Round 1 issues with EA-WM acknowledgment, Kimodo mischaracterization, venue labeling, and IDM domain gap are substantially addressed. The technical differentiation from EA-WM is now specific and compelling on three axes (full-body vs. arm-only, ControlNet frozen vs. joint fine-tuning, explicit IDM pipeline vs. no policy output). The remaining blockers are primarily user-requirement alignment issues:

1. **Address the venue/timeline mismatch directly**: If CoRL 2026 (May 29) is genuinely infeasible, say so explicitly and quantify why — e.g., 'ControlNet training requires ≥35h GPU compute + 3 days of debugging + evaluation, totaling ≥20 days even in auto mode, so the earliest feasible venue is CoRL 2027 or ICLR 2027.' Present this to the user as a constraint, not a silent substitution.

2. **Add user-required evaluation platforms**: At minimum, add one Isaac Lab humanoid manipulation task (e.g., G1 pick-and-place or table-top reaching from Isaac Lab humanoid suite) as a downstream policy training target. This directly satisfies user requirements and provides a more standardized comparison point than Dream2Act-only benchmarks.

3. **Acknowledge VAG (arXiv:2604.09330, April 2026)** in the landscape. VAG jointly generates video and action, which avoids the IDM domain gap entirely. URDF-DiT's advantage over VAG is the explicit URDF kinematic constraint (enforcing joint-limit compliance and embodiment geometry) rather than implicit action learning — this distinction must be made explicit.

4. **Tighten the ControlNet compute estimate**: Add a sensitivity analysis — if training takes 50h instead of 35h due to video temporal attention overhead, total manual budget becomes ~150h, still within constraint. This removes the ambiguity in the estimate.

5. **Scope the contribution more precisely for a 20-day auto-mode execution**: If targeting CoRL 2026 is reinstated, the evaluation scope must be reduced to 2 benchmarks (not 3), and the ablation set must be compressed to one primary comparison (in-loop vs. post-hoc), with the ControlNet-vs-bidirectional-fusion ablation deferred to the ICLR 2027 extended submission.

### Round 3 review
Verdict: revise
Issues: ["DREAM2ACT FAILURE MODE MISCHARACTERIZATION (PERSISTENT): The proposal states 'kinematic artifacts from post-hoc URDF-IK correction are cited as the primary failure mode' for Dream2Act's 37.5% success — this is inaccurate. The paper's failure analysis identifies the 'morphology gap' and 'severe spatial misalignments' as failures of the BASELINE (traditional retargeting, 0%), not as Dream2Act's own failure mode. Dream2Act's 37.5% performance is not attributed to post-hoc correction artifacts in the paper itself. The generator is presenting an inference as a citation, which will draw immediate reviewer fire. Correct to: 'We hypothesize that post-hoc URDF-IK correction in Dream2Act introduces kinematic artifacts (e.g., joint discontinuities from IK failure at contact poses); the 37.5% overall ceiling, including 10% on Box Hugging, is consistent with this hypothesis but may also reflect task difficulty.'", "COMPARISON VALIDITY — URDF-DiT vs. DREAM2ACT IS APPLES-TO-ORANGES: Dream2Act is a zero-shot real-robot execution system (video → URDF-IK → motor commands → physical robot); URDF-DiT generates synthetic training data for a sim-IDM policy (video → IDM → joint velocity commands → policy training in Isaac Lab). The proposed 'in-loop vs. post-hoc ablation at matched video budgets' is comparing architectures that solve different problems. This comparison needs to be redesigned: either (a) compare kinematic consistency metrics of generated videos (FK residual, joint-limit violation rate, temporal smoothness) between URDF-DiT and a post-hoc correction baseline, or (b) compare downstream policy success rate on Isaac Lab after training on URDF-DiT-generated data vs. data extracted via post-hoc URDF-IK from vanilla Wan 2.2 outputs — the latter is a fair ablation.", "NOVELTY ARGUMENT UNDERSPECIFIED FOR FULL-BODY VS. END-EFFECTOR CONDITIONING: EA-WM already injects end-effector heatmaps into Wan 2.2 cross-attention and achieves action recovery detection rate ~0.45. URDF-DiT's claim is that conditioning on all 29 DoF (pelvis, legs, torso, arms, hands) simultaneously is qualitatively different. But the technical argument for why whole-body joint conditioning outperforms end-effector-only conditioning for whole-body tasks (not just arm tasks) needs to be made explicitly — e.g., does the pelvis/leg conditioning actually improve foot contact realism in generated videos? Without a targeted ablation (all-joint FK heatmaps vs. end-effector-only heatmaps), reviewers will reasonably ask if end-effector conditioning would suffice for the manipulation component while leg conditioning is just noise.", "IDM DOMAIN GAP: FK RESIDUAL LOSS MECHANISM LACKS CLARITY: The proposal claims 'a per-frame FK residual consistency loss added to URDF-DiT's generation objective, penalizing deviations between generated joint positions and URDF FK predictions' bridges the Wan 2.2 → Isaac Lab appearance domain gap. But this loss operates on kinematics, not appearance. The domain gap for the IDM is primarily in the visual domain (Wan 2.2 texture/lighting vs. Isaac Lab domain-randomized rendering). The FK residual loss may enforce kinematic consistency in generated videos but does not directly reduce the appearance domain gap that causes IDM errors. Domain-randomized rendering during IDM training is the more direct mitigation; the FK residual loss role needs to be more precisely specified.", "COMPUTE ESTIMATE FOR CONTROLNET TRAINING REMAINS UNCERTAIN: The 35–70h range is wide (2x uncertainty). Community experience with Wan 2.2 LoRA fine-tuning (3-6h on A40) and the existence of TheDenk/wan2.2-ti2v-5b-controlnet-depth-v1 on HuggingFace suggest ControlNet module training on Wan 2.2 is feasible, but for FK heatmap conditioning specifically (multi-channel, time-varying, full-body), temporal attention overhead could push toward the 70h end. Given the 8 H100 parallelization, this is manageable within budget, but the estimate should be anchored to the existing depth-ControlNet training reports rather than stated as a 2x range with no empirical basis.", "PAPER WRITING TIMELINE (DAYS 15–19) IS EXTREMELY TIGHT FOR CoRL SUBMISSION: A CoRL paper requires a well-positioned introduction, related work distinguishing from EA-WM/Dream2Act/VAG, technical method, and experiments section. With auto-research mode generating code and running experiments, 4 days for paper writing is possible only if the agent also drafts large portions of the paper. The proposal should explicitly state whether auto mode includes paper drafting assistance or whether the 4-day window assumes a human researcher writing."]
Feedback: The proposal has resolved all critical issues from Rounds 1–2: compute budget is within 200h, EA-WM/VAG/Dream2Act are properly acknowledged and differentiated, user-required evaluation platforms (Isaac Lab G1, HumanoidBench, RoboCasa365) are included, venue labeling is correct, and the IDM domain gap has a mitigation plan. The residual issues are addressable in one more revision:

1. **Fix the Dream2Act failure mode claim**: Change 'kinematic artifacts from post-hoc correction are cited as the primary failure mode' to 'we hypothesize that post-hoc URDF-IK correction introduces kinematic artifacts at contact poses — consistent with Dream2Act's 10% Box Hugging success rate — motivating in-loop FK conditioning.' Do not claim the paper cites this as primary failure mode.

2. **Redesign the in-loop vs. post-hoc ablation**: The ablation should compare (a) URDF-DiT-generated videos vs. vanilla Wan 2.2 videos post-processed with URDF-IK (both used as training data for the same IDM), evaluating downstream Isaac Lab policy success rate. This is a fair, self-contained comparison that doesn't require reimplementing Dream2Act's zero-shot real-robot pipeline.

3. **Add a targeted ablation for full-body vs. end-effector conditioning**: Even a 2-point ablation (all 29 DoF heatmaps vs. end-effector-only, 5 DoF) would directly validate whether full-body conditioning is necessary. This would be the paper's strongest scientific contribution claim and is achievable in the same compute budget.

4. **Clarify the FK residual loss role**: Reframe it as 'enforcing kinematic consistency in generated video (reducing temporal joint jitter and limit violations)' rather than 'bridging the sim→video domain gap for IDM.' Domain-randomized rendering during IDM training is the primary domain gap mitigation; the FK residual loss ensures the generated videos are kinematically coherent inputs to the IDM.

5. **Address paper writing in the timeline**: State explicitly whether auto mode includes paper drafting (using the agent to generate LaTeX drafts based on results), which is what makes the 4-day window feasible. Without this, the CoRL timeline is implausible even in auto mode.

### Round 4 review
Verdict: revise
Issues: ["PERSISTENT CRITICAL MISCHARACTERIZATION — DREAM2ACT FAILURE MODE (ROUND 4, UNRESOLVED FROM ROUND 3): Independent verification via arXiv:2603.19709v1 confirms that Dream2Act does NOT cite 'kinematic artifacts from post-hoc URDF-IK correction' as its primary failure mode. Dream2Act generates video directly in the robot's native spatial coordinate system and explicitly avoids post-hoc correction — its stated limitation is inference latency, not kinematic artifacts. The per-task breakdown (Ball-kicking 40%, Box-hugging 10%, Bag-hitting 30%, Sofa-sitting 70%) reflects task difficulty, not IK correction artifacts. The proposal has now repeated this false claim through three consecutive rounds despite explicit correction instruction in Round 3. This is the most urgent issue to fix before any venue submission, as Dream2Act authors and CoRL reviewers familiar with the paper would immediately flag it.", "ABLATION DESIGN STILL APPLES-TO-ORANGES (UNRESOLVED FROM ROUND 3): The CoRL-scoped ablation remains 'in-loop vs. post-hoc URDF-IK at matched video budgets,' which Round 3 identified as comparing architectures that solve different problems (Dream2Act: zero-shot real-robot execution; URDF-DiT: synthetic training data for sim-IDM policy). The required redesign — compare downstream policy success rate on Isaac Lab after training on (a) URDF-DiT-generated data vs. (b) vanilla Wan 2.2 data post-processed with URDF-IK — was not implemented. Without this fix, the primary ablation is technically invalid as a comparison.", "FULL-BODY VS. END-EFFECTOR ABLATION STILL ABSENT (UNRESOLVED FROM ROUND 3): Round 3 explicitly requested a 2-point ablation (all 29 DoF FK heatmaps vs. end-effector-only, ~5 DoF) to validate whether full-body conditioning is necessary for whole-body tasks. This would be the paper's strongest scientific claim and is achievable within budget. It remains missing in Round 4.", "FK RESIDUAL LOSS ROLE STILL IMPRECISE (UNRESOLVED FROM ROUND 3): The approach still frames the FK residual loss as one of 'two primary mechanisms' mitigating the 'sim→video IDM domain gap.' Round 3 correctly identified that this loss operates on kinematics in the generated video (reducing temporal joint jitter and joint-limit violations), not on visual appearance. The appearance domain gap is addressed by domain-randomized rendering during IDM training; the FK residual loss should be reframed as enforcing kinematic consistency in generated outputs rather than bridging the visual distribution gap.", "MISSED CONCURRENT WORK — EVA (arXiv:2603.17808, March 2026): 'EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards' directly addresses the executability gap in video world models via inverse dynamics rewards, competing with URDF-DiT's IDM extraction pipeline. This paper is not cited in the landscape and should be acknowledged with explicit differentiation.", "PAPER WRITING TIMELINE STILL UNADDRESSED (UNRESOLVED FROM ROUND 3): Days 15–19 are allocated to 'paper writing and CoRL submission polish' in auto mode without stating whether the auto agent also drafts LaTeX sections. Without explicit acknowledgment that auto-mode includes paper drafting (introduction, related work distinguishing EA-WM/Dream2Act/VAG, method, experiments), the 4-day window is implausible for a full CoRL submission.", "EA-WM TITLE DISCREPANCY: The proposal calls EA-WM 'Embodiment-Aware World Model via Kinematic-Visual Action Fields for Bimanual Manipulation' but the actual title is 'EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields' (Event-Aware, not Embodiment-Aware). Additionally, independent search suggests EA-WM evaluates on WorldArena benchmark rather than being scoped exclusively to bimanual manipulation — verify this characterization before submission."]
Feedback: The technical core of URDF-DiT (in-loop FK heatmap conditioning for 29+ DoF full-body humanoid via ControlNet frozen backbone + explicit IDM pipeline) remains defensible and competitive. The VAG differentiation is now independently verified as accurate. Three targeted fixes are required before this passes:

1. **CRITICAL — Fix the Dream2Act framing (round 5 MUST fix this)**: Direct paper read confirms Dream2Act generates in robot-native space, does NOT use post-hoc URDF-IK correction as its mechanism, and cites inference latency as its limitation — not kinematic artifacts. Change the entire motivation: instead of 'Dream2Act fails due to post-hoc IK artifacts,' frame it as 'Dream2Act's robot-native video synthesis (37.5% ceiling) shows the gap is not retargeting but video fidelity — we push further by enforcing URDF joint-limit compliance throughout denoising rather than relying on video realism alone.' This is actually a stronger and more honest motivation.

2. **Redesign the primary ablation**: Compare downstream Isaac Lab policy success rate: (a) policies trained on URDF-DiT-generated trajectories vs. (b) policies trained on trajectories extracted from vanilla Wan 2.2 videos via post-hoc URDF-IK. This is a self-contained, fair comparison that avoids reimplementing Dream2Act.

3. **Add the full-body vs. end-effector ablation**: Even reporting 2 data points (all-joint heatmaps vs. end-effector-only, same IDM) would elevate this from a systems paper to a scientific contribution. It is the one claim that distinguishes URDF-DiT from EA-WM and requires empirical validation.

4. **Cite and differentiate from EVA (arXiv:2603.17808)**: EVA trains IDMs as rewards for video generation to close the executability gap; explain that URDF-DiT enforces geometric kinematic constraints (joint angles, limits) rather than relying on a learned executability signal.

5. **Reframe FK residual loss**: It enforces kinematic consistency in generated video (reducing temporal joint jitter, preventing limit violations during denoising) — not a visual domain gap bridge. Domain-randomized rendering handles the appearance gap; the FK loss handles geometric consistency. Say so precisely.

6. **State explicitly in the auto-mode timeline**: 'Auto mode includes agent-assisted LaTeX drafting (introduction, related work, method, experiments) starting Day 14 — this is what makes the 4-day writing window feasible.'

### Round 5 review
Verdict: revise
Issues: ["EVALUATION SCOPE PARTIALLY VIOLATES USER REQUIREMENTS: User explicitly required testing on 'Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench.' The CoRL-scoped submission defers RoboCasa365 and HumanoidBench entirely to ICLR 2027, leaving the CoRL submission evaluated only on Isaac Lab G1 locomanipulation plus a Dream2Act ball-kicking contextual comparison. This is a conscious scope reduction that must be explicitly flagged to the user as a requirement tradeoff, not silently accepted as the default plan.", "DREAM2ACT MECHANISM REQUIRES CAREFUL PHRASING: Independent verification via the arXiv:2603.19709 HTML confirms Dream2Act DOES use post-hoc URDF-constrained IK (applying IK after video generation to convert pixel-space pose to joint trajectories) — the Round 5 proposal's description is factually correct. However, Dream2Act also frames this as generating 'within robot-native coordinate space,' meaning its videos hallucinate the G1 robot body (not a human), then apply IK to extract joint angles. The proposal should distinguish between (a) Dream2Act's video generation modality (robot-native appearance) and (b) Dream2Act's kinematic extraction approach (post-generation constrained IK) to avoid any conflation that reviewers could challenge.", "FLOWANY-R1 (arXiv:2601.10103, January 2026) NOT CITED: This paper targets 'interactive humanoid video generation' with 'holistic and fine-grained full-body control' at 25fps via MMDiT architecture. While its kinematic conditioning mechanism is underspecified in the abstract and it targets real-time interaction (not training data generation), it is directly in the humanoid video generation space and should appear in the landscape with a one-line differentiation (no URDF kinematic structure, no IDM policy extraction pipeline, interactive use case vs. offline training data generation).", "EA-WM COMPETITIVE RISK STILL HIGH — DIFFERENTIATION NEEDS EMPIRICAL BACKING: EA-WM (May 7, 2026) uses KVAFs (Gaussian heatmaps at projected end-effector/joint locations injected into Wan 2.2 cross-attention) — the same core design pattern as URDF-DiT's FK heatmap injection. The proposal differentiates on (a) full-body 29 DoF vs. arm manipulation, (b) ControlNet frozen backbone vs. bidirectional fusion joint fine-tuning, and (c) IDM pipeline vs. no policy output. These are real differentiators, but the scientific weight of (a) depends entirely on the full-body vs. end-effector ablation result — if the ablation shows marginal improvement from full-body conditioning, CoRL reviewers will question whether the 29 DoF scope is necessary rather than just incremental over EA-WM's end-effector approach. The ablation must be framed as the central scientific claim, not a supporting experiment.", "CORL 2026 TIMELINE PIVOT CRITERIA UNDERSPECIFIED: The proposal states 60–70% probability of submittable results by May 29 in auto mode, with 'immediate pivot to ICLR 2027 if results are negative by Day 14.' The Day 14 decision gate needs more precise criteria: what constitutes 'results that warrant ICLR 2027 pivot' vs. 'results that, while imperfect, constitute a submittable CoRL contribution'? Without specific metric thresholds (e.g., 'if URDF-DiT trained policy success rate > X% and > Y% improvement over vanilla Wan 2.2 baseline, proceed to CoRL; otherwise pivot'), the pivot decision is ambiguous and the 60–70% probability estimate has no anchoring."]
Feedback: Round 5 has resolved all seven critical issues from Round 4: Dream2Act is correctly described (inference latency as primary limitation, post-hoc IK acknowledged), EA-WM title corrected (Event-Aware), FK residual loss precisely framed (kinematic consistency not domain gap), ablation redesigned to downstream Isaac Lab policy success rate comparison, full-body vs. end-effector ablation added, EVA cited and differentiated, and auto-mode LaTeX drafting explicitly stated. The proposal is now technically sound. Four targeted fixes remain before this should proceed:

1. **Flag the user requirement tradeoff explicitly**: The CoRL submission evaluates only Isaac Lab G1 locomanipulation; HumanoidBench and RoboCasa365 are deferred. Present this to the user as an explicit tradeoff decision ('CoRL version covers 1 of 3 required benchmarks; full coverage requires ICLR 2027') rather than embedding it quietly in the venue notes. The user may prefer to target ICLR 2027 from the start.

2. **Add FlowAct-R1 (arXiv:2601.10103) to the landscape**: One line — 'FlowAct-R1 (arXiv:2601.10103, January 2026) targets real-time interactive humanoid video generation via MMDiT chunkwise diffusion without URDF kinematic constraints or IDM policy extraction.' This paper predates the CoRL 2026 submission and reviewers may cite it.

3. **Elevate the full-body vs. end-effector ablation to the primary scientific claim**: Frame the paper's core question as 'Does conditioning on all 29 DoF (pelvis, legs, torso, arms, hands) throughout denoising improve downstream IDM extraction quality for whole-body contact tasks compared to end-effector-only conditioning?' This directly differentiates from EA-WM empirically and positions the ablation result as the paper's central finding, not a supporting experiment.

4. **Add specific metric thresholds for the Day 14 CoRL/ICLR 2027 pivot decision**: Define 'submittable' concretely — e.g., 'URDF-DiT policy success rate ≥ 10% on Isaac Lab G1 pick-and-place AND ≥ 5 percentage point improvement over vanilla Wan 2.2 + post-hoc IK baseline triggers CoRL submission; otherwise pivot to ICLR 2027.' This turns the 60–70% probability statement into an actionable decision gate.

### Round 6 review
Verdict: revise
Issues: ["CRITICAL NEW ISSUE — BRIDGEV2W (arXiv:2602.03793, February 2026) NOT CITED: Independent verification confirms BridgeV2W explicitly 'converts coordinate-space actions into pixel-aligned embodiment masks rendered from the URDF and camera parameters. These masks are then injected into a pretrained video generation model via a ControlNet-style pathway.' This paper — applied to single-arm (DROID) and dual-arm (AgiBot-G1) robots — is architecturally nearly identical to URDF-DiT's core contribution (ControlNet + URDF conditioning for robot video DiT). A CoRL reviewer familiar with the embodied world model literature will immediately flag this omission. URDF-DiT must cite BridgeV2W and differentiate explicitly on: (a) full-body humanoid 29 DoF vs. arm/dual-arm scope; (b) Gaussian joint-position heatmaps from FK (continuous per-joint scalar fields encoding kinematic structure) vs. BridgeV2W's pixel-aligned binary embodiment masks (which encode link occupancy but not individual joint angles); (c) IDM training data generation as the downstream objective vs. BridgeV2W's policy evaluation and goal-conditioned planning. With BridgeV2W now in the landscape alongside EA-WM, the claim that URDF-DiT introduces ControlNet + URDF injection into video DiT is no longer defensible — the paper's novelty must be repositioned as 'full-body humanoid kinematic conditioning with Gaussian heatmaps for IDM training data generation,' not as a novel conditioning architecture.", "VAG 'EXPLICITLY ACKNOWLEDGES' CHARACTERIZATION REQUIRES PRECISION: The proposal states VAG 'explicitly acknowledges the video branch has not been influenced by the action branch.' Independent review of the VAG abstract finds it describes 'synchronized denoising in both branches' with 'adaptive 3D pooling to transfer compact global video context to the action branch' — suggesting the design routes video features to actions but not necessarily the reverse. If this quote comes from an ablation or analysis section in the full paper, it must be cited with section/page reference. If it is the proposal author's inference, it must be rewritten: 'VAG's architecture routes video context to the action branch via 3D pooling but does not inject action signals back into the video denoising process, leaving a video-action coupling gap that explicit FK heatmap injection in URDF-DiT addresses.' Misquoting a competitor's paper is a fast track to rejection at CoRL.", "NOVELTY BAR AT CORL IS NOW CRITICALLY THIN: With EA-WM (in-loop kinematic heatmap injection into Wan 2.2 cross-attention, May 2026) and BridgeV2W (ControlNet + URDF embodiment mask injection into pretrained video DiT, February 2026) both uncited-until-now, the paper's architectural contribution is no longer novel. The remaining novelty is exclusively in (a) full-body humanoid scope (29 DoF vs. arm-only) and (b) IDM-to-policy pipeline. Point (b) is primarily an engineering contribution. Point (a) is an empirical claim that depends on Ablation B showing meaningful improvement (≥5pp). If Ablation B shows marginal benefit from full-body vs. end-effector conditioning, the paper has no defensible novel claim over the combined EA-WM + BridgeV2W prior work. The proposal's 'submit with reframing' contingency (Ablation B < 3pp → 'end-effector conditioning suffices') would produce a paper saying 'our novel extension doesn't help' — which is not a CoRL-level contribution. This risk must be assessed before committing to the CoRL trajectory.", "CORL EVALUATION STILL 1 OF 3 USER-REQUIRED BENCHMARKS: This is flagged explicitly in the proposal (which is correct), but it remains a hard constraint — the CoRL submission does not satisfy the user's stated requirement of evaluating on Isaac Lab G1 locomanipulation, HumanoidBench, AND RoboCasa365. The proposal correctly identifies this as an explicit user decision, but the review record should note it is unresolved from the user's perspective until they make the opt-in/out decision. Without user confirmation, the CoRL path should be treated as provisional."]
Feedback: Round 6 correctly resolved all four Round 5 issues: user tradeoff is explicitly and prominently flagged, FlowAct-R1 is in the landscape with a one-line differentiation, Ablation B is the primary scientific claim, and Day 14 pivot criteria have concrete numeric thresholds. The proposal is structurally sound. Two targeted fixes are required:

1. **URGENT: Add BridgeV2W to the landscape and reposition the novelty claim.** BridgeV2W (arXiv:2602.03793, February 2026) uses 'coordinate-space actions → pixel-aligned embodiment masks rendered from URDF → ControlNet-style injection into pretrained video DiT.' This is the same architecture as URDF-DiT. Add a landscape entry: 'BridgeV2W (arXiv:2602.03793, Feb 2026) uses URDF-rendered pixel-aligned embodiment masks injected via ControlNet pathway into a pretrained video DiT for arm/dual-arm manipulation video generation and policy evaluation. URDF-DiT differentiates on three axes: (a) full-body humanoid 29 DoF (vs. arm/dual-arm) with Gaussian joint-position heatmaps encoding per-joint kinematic structure rather than binary link occupancy masks; (b) whole-body contact interaction tasks (pick-and-place with locomotion, ball-kicking) vs. arm manipulation; (c) IDM training data generation pipeline vs. policy evaluation and goal-conditioned planning.' Then revise the introduction to acknowledge that ControlNet + URDF conditioning for robot video DiTs is now an established approach (citing EA-WM and BridgeV2W) and position URDF-DiT as the first application of this approach to full-body humanoid whole-body contact tasks with an explicit IDM training data generation objective.

2. **Fix the VAG 'explicitly acknowledges' characterization.** Change to: 'VAG's architecture routes compact global video context to the action branch via adaptive 3D pooling, but does not inject action signals back into the video denoising process — a design gap URDF-DiT addresses via bidirectional FK heatmap conditioning.' Do not use a direct quote unless you can cite the specific section where VAG uses those exact words.

3. **Assess the Ablation B risk explicitly.** Given EA-WM + BridgeV2W now both in the landscape, the paper needs Ablation B to be strongly positive (≥5pp) to have a defensible novel claim at CoRL. Add to the pivot criteria: if Ablation B < 5pp AND BridgeV2W is the closest prior, the paper's CoRL-level novelty is insufficient — pivot to ICLR 2027 with full benchmark coverage and a deeper ablation suite (also including a direct comparison against BridgeV2W's embodiment mask approach).

### Round 7 review
Verdict: revise
Issues: ["CRITICAL UNRESOLVED FROM ROUND 6 — BridgeV2W (arXiv:2602.03793) STILL ABSENT: Independent verification confirms BridgeV2W (February 3, 2026) uses URDF-rendered pixel-aligned embodiment masks injected via ControlNet-style pathway into pretrained video DiT, tested on DROID (single-arm) and AgiBot-G1 (dual-arm). This paper is architecturally nearly identical to URDF-DiT's core mechanism and has been flagged as missing in every round since Round 6. It is absent from both the landscape section and key_references in Round 7. A CoRL reviewer familiar with embodied world model literature will flag this immediately. URDF-DiT must add BridgeV2W and explicitly differentiate on: (a) full-body humanoid 29 DoF vs. arm/dual-arm scope; (b) continuous per-joint Gaussian FK heatmaps encoding kinematic structure vs. BridgeV2W's binary pixel-aligned occupancy masks (which encode link presence but not individual joint angles or joint-limit constraints); (c) IDM training data generation as the downstream objective vs. BridgeV2W's goal-conditioned planning and policy evaluation. The introduction must acknowledge that ControlNet + URDF conditioning for robot video DiTs is an established approach (BridgeV2W: Feb 2026; EA-WM: May 2026) and position URDF-DiT as the first application to full-body humanoid 29 DoF whole-body contact tasks with explicit IDM training data generation.", "VAG SECTION ATTRIBUTION MISSING: The VAG quote 'video branch not influenced by action branch' is independently verified as accurate (confirmed from the paper's 'Limitations and Future Work' section, which explicitly states 'video generation has not been influenced by the action branch, wasting beneficial control signals'). The proposal should cite this as: 'VAG's authors explicitly acknowledge in their Limitations section that the video branch has not been influenced by the action branch' — or use the exact paper quote with section attribution — to preempt any reviewer challenge to this claim.", "SUBMIT-WITH-REFRAMING CONTINGENCY WEAKENED BY BRIDGEV2W + EA-WM LANDSCAPE: The proposal states that if Ablation B shows <3pp improvement from full-body vs. end-effector conditioning, the paper can be 'reframed as end-effector conditioning suffices' and remains 'a valid CoRL contribution.' This contingency is now significantly weaker given BridgeV2W and EA-WM both already demonstrate ControlNet + URDF conditioning for arm robots. If full-body conditioning over end-effector-only shows <3pp improvement, the paper is essentially validating that the arm-robot approaches (BridgeV2W, EA-WM) are sufficient for humanoids — which is a minor empirical finding, not a CoRL-level contribution. The pivot criteria must explicitly add: 'If Ablation B < 3pp AND BridgeV2W/EA-WM are closest prior work, pivot to ICLR 2027 (not CoRL reframing), as the novelty claim over existing arm-robot ControlNet+URDF approaches is insufficient for CoRL acceptance.'", "NEW UNCITED CONCURRENT WORK — MotuBrain (arXiv:2604.27792, April 2026): MotuBrain introduces a world action model that jointly supports video generation, inverse dynamics prediction, and joint video-action prediction for robot control — directly overlapping with URDF-DiT's IDM extraction pipeline goal. While the conditioning mechanism differs, MotuBrain's joint video-IDM modeling is a concurrent approach to the same problem of extracting executable actions from generated video, and CoRL reviewers in the embodied video generation track will likely be familiar with it. Add a one-line differentiation.", "EVALUATION SCOPE — USER REQUIREMENT TRADEOFF (EXPLICITLY FLAGGED BUT UNRESOLVED): The proposal now correctly and prominently flags that CoRL 2026 covers only 1 of 3 user-required benchmarks (Isaac Lab G1 locomanipulation only; HumanoidBench and RoboCasa365 deferred to ICLR 2027). This is appropriately presented as an explicit user decision (option A vs. option B). However, until the user makes this choice, the CoRL path should be treated as provisional — the reviewer record notes this remains open."]
Feedback: Round 7 has resolved the majority of prior issues: user tradeoff is prominently and honestly flagged, Dream2Act two-component description is accurate and precise, VAG characterization is confirmed accurate (the quote is real), Ablation B is correctly elevated as the primary scientific claim, Day 14 pivot criteria have concrete numeric thresholds, FlowAct-R1 is in the landscape, EA-WM title is corrected, FK residual loss role is precisely framed, and EVA is cited and differentiated. The proposal is technically sound and structurally well-organized.

One critical fix remains before this can pass:

**URGENT — Add BridgeV2W to landscape (3rd consecutive round flagged)**: BridgeV2W (arXiv:2602.03793, Feb 2026) is independently confirmed: URDF-rendered pixel-aligned embodiment masks → ControlNet pathway → pretrained video DiT, tested on DROID and AgiBot-G1 dual-arm datasets. Add this entry to landscape: 'BridgeV2W (arXiv:2602.03793, Feb 2026): converts coordinate-space robot actions to pixel-aligned binary embodiment masks rendered from URDF and camera parameters, injected via ControlNet-style pathway into pretrained video DiT for arm/dual-arm manipulation; evaluates on DROID and AgiBot-G1. URDF-DiT differentiates on: (a) full-body humanoid 29 DoF vs. arm/dual-arm scope; (b) continuous per-joint Gaussian FK heatmaps (encoding joint-angle-specific kinematic structure and joint-limit constraints) vs. binary occupancy masks (encoding link presence only); (c) IDM synthetic training data generation pipeline vs. goal-conditioned planning and policy evaluation.' Then revise the introduction to frame ControlNet+URDF+video-DiT as an established approach (BridgeV2W Feb 2026, EA-WM May 2026) and position URDF-DiT as the first extension to full-body humanoid 29 DoF whole-body contact tasks.

Two secondary fixes:
1. Add section attribution to VAG quote: '(VAG Limitations and Future Work section: video generation has not been influenced by the action branch, wasting beneficial control signals)'
2. Tighten pivot criteria: add 'If Ablation B < 3pp AND BridgeV2W/EA-WM are closest prior, pivot directly to ICLR 2027 — CoRL reframing insufficient over arm-robot ControlNet+URDF baseline'
3. Add MotuBrain (arXiv:2604.27792, April 2026) as a one-line landscape entry.

### Round 8 review
Verdict: revise
Issues: ["UNCITED COMPETITOR — HumanX (arXiv:2602.02473, February 2026): HumanX introduces XGen, a video synthesis pipeline generating physically plausible humanoid training data for loco-manipulation tasks (basketball, football, cargo pickup) with zero-shot transfer to physical G1 and 8x higher generalization success than prior methods. Although retargeting-based (hence out of scope for URDF-DiT's contribution type), it competes in the same application space — generating synthetic humanoid training data for loco-manipulation — and a CoRL 2026 reviewer will expect to see it cited with a one-line differentiation explaining that URDF-DiT generates kinematically constrained video without retargeting from human motion, while HumanX synthesizes data by retargeting human motion videos to humanoid morphology. Failure to cite it will invite a 'missing related work' reviewer flag.", "KINEMA4D CHARACTERIZATION POTENTIALLY UNDERSTATED: The proposal describes Kinema4D (arXiv:2603.16669, March 2026) as 'URDF-driven FK for 4D pointmap conditioning for scene realism; not policy-data generation or video diffusion attention-layer injection' — but independent search finds it described as 'action-conditioned 4D generative simulator that drives a URDF robot via kinematics, then uses diffusion transformer to generate 4D world sequences' including 'robot control trajectories and environmental reactions.' The differentiation may still hold (4D geometric representation vs. RGB video; 4D world simulation vs. IDM training data pipeline) but the current one-line dismissal underspecifies the distinction. Reviewers familiar with Kinema4D may challenge this. Add a more precise differentiation: Kinema4D generates 4D geometric pointmap sequences for spatial simulation and scene realism — it does not generate photorealistic RGB video frames suitable for IDM training, does not inject kinematic conditioning into RGB video DiT attention layers, and provides no IDM extraction or downstream policy training pipeline.", "NOVELTY FRAMING RISK FOR CORL BAR: The title 'Does Full-Body Kinematic Conditioning Throughout Denoising Improve IDM Training Data...' frames the paper as an empirical hypothesis test — a valid framing for workshops or NeurIPS empirical tracks but atypical for CoRL, which expects papers that propose a method and demonstrate its superiority. If the submission explicitly frames its central contribution as an ablation study ('we test whether X is necessary'), CoRL reviewers may apply a higher scrutiny threshold to justify acceptance. The pivot to 'Ablation A as primary claim' contingency is logically sound but should be embedded in the paper structure naturally — not appear as an explicitly contingent fallback.", "CORL SUBMISSION COVERS ONLY 1 OF 3 USER-REQUIRED BENCHMARKS: This is explicitly and prominently flagged throughout the proposal (including top-of-document warnings), which is correct — but the issue remains unresolved from the user's perspective until they make the opt-in/out decision. Without user confirmation to proceed with the CoRL-scoped single-benchmark plan, the CoRL trajectory should be treated as provisional."]
Feedback: Round 8 has resolved all critical persistent issues from prior rounds. BridgeV2W is now properly cited with precise three-axis differentiation in landscape, key_references, approach, and core_problem sections. VAG quote is correctly attributed to the Limitations and Future Work section. MotuBrain is cited. The submit-with-reframing contingency is correctly scoped ('if Ablation B < 3pp AND Ablation A < 5pp, pivot to ICLR 2027 — not CoRL reframing'). Dream2Act two-component decomposition is precise and independently verified. The proposal is now structurally sound for a Round 9 pass with two targeted fixes:

1. **Add HumanX (arXiv:2602.02473, February 2026) to landscape**: One line — 'HumanX (arXiv:2602.02473, Feb 2026) generates humanoid loco-manipulation training data via XGen (video synthesis retargeting human motion to humanoid morphology) + XMimic (imitation learning), achieving zero-shot physical G1 transfer across sports/manipulation tasks. URDF-DiT differentiates: generative kinematic conditioning without retargeting from human videos, targeting IDM training data for whole-body contact tasks via explicit URDF FK heatmap injection.' This eliminates the likely reviewer flag without requiring substantive changes.

2. **Expand Kinema4D differentiation**: Replace the current one-line description with: 'Kinema4D (arXiv:2603.16669, March 2026, NTU): action-conditioned 4D generative simulator using URDF kinematics to drive a diffusion transformer generating 4D pointmap world sequences for spatial simulation. Key distinction from URDF-DiT: Kinema4D generates 4D geometric representations for simulation realism — it does not generate photorealistic RGB video frames suitable for IDM training, does not inject kinematic conditioning into RGB video DiT cross-attention, and provides no IDM extraction or policy training pipeline. Complementary in the sense that Kinema4D handles 4D world simulation while URDF-DiT targets RGB video generation for IDM data.'

3. **Optional — soften the hypothesis-test title framing**: If targeting CoRL, consider retitling to 'URDF-DiT: Full-Body Kinematic Conditioning for Humanoid IDM Training Data Generation via Video Diffusion' and reserving the 'Does X improve Y?' framing for the abstract's research question statement rather than the title — CoRL reviewers generally favor titles that state what the method is, not what question it asks.


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
  "promptId": "c7a86d90-025e-47d4-98c5-8fe2906cdffe",
  "type": "user",
  "uuid": "40d4f866-0591-414b-85d2-1ceb53057209",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T13:55:15.803Z_

```json
{
  "parentUuid": "40d4f866-0591-414b-85d2-1ceb53057209",
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
  "uuid": "84699038-fd49-4d59-a4b8-1d662a47911f",
  "timestamp": "2026-05-10T13:55:15.803Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T13:55:15.803Z_

```json
{
  "parentUuid": "84699038-fd49-4d59-a4b8-1d662a47911f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "099ec803-7aa2-4c8c-8d4c-2279be848c8c",
  "timestamp": "2026-05-10T13:55:15.803Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9",
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
  "leafUuid": "099ec803-7aa2-4c8c-8d4c-2279be848c8c",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "URDF-DiT: Full-body kinematic conditioning for humanoid IDM training data",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9"
}
```

---

### Assistant

_source line 8 · 2026-05-10T13:55:35.294Z_

<details><summary>Logged reasoning block</summary>

```text
This is Round 9 of 10. I need to conduct an independent adversarial review of the URDF-DiT idea. Let me analyze what's been resolved from previous rounds and what remains to be verified.

From the review history, the main issues resolved in Round 8 were:
1. BridgeV2W now properly cited ✓
2. VAG quote correctly attributed ✓
3. MotuBrain cited ✓
4. Submit-with-reframing contingency scoped ✓
5. Dream2Act decomposition precise ✓

Outstanding issues from Round 8 that should be addressed in Round 9:


1. HumanX (arXiv:2602.02473) - needed in landscape
2. Kinema4D differentiation needs expansion
3. Optional title framing softening
4. CoRL covers only 1 of 3 user-required benchmarks (unresolved user decision)

Let me check the Round 9 idea to see if these were addressed. HumanX is now extensively cited throughout the landscape, key references, approach, and core problem sections with detailed differentiation. Kinema4D also has a detailed differentiation in the landscape section. I need to continue checking whether the title framing and CoRL benchmark coverage were resolved.

Now I'm verifying the cited papers to ensure they actually exist and checking for any concurrent work that might have emerged. I'm also examining whether the novelty claims hold up, if the feasibility estimates are realistic, and whether there's any relevant work that was overlooked. Let me start by searching for the specific papers mentioned to confirm their details and content. the first to inject full-body 29-DoF FK heatmaps into a video DiT throughout denoising for humanoid whole-body contact task IDM data generation. The key differentiators from prior work like BridgeV2W and EA-WM are the full-body kinematic scope versus arm-only, continuous Gaussian heatmaps instead of binary masks, and the IDM pipeline rather than goal-conditioned planning. I need to verify these claims and check the ablations—comparing in-loop FK conditioning against post-hoc URDF-IK, and testing 29 DoF versus end-effector-only variants—then search for any concurrent work I might have missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "099ec803-7aa2-4c8c-8d4c-2279be848c8c",
  "isSidechain": false,
  "requestId": "req_011Cau16YGnwqt6AyZVwpjAe",
  "type": "assistant",
  "uuid": "a2130a7a-08af-49fa-a6d1-c96ce67c128f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017TJouwT3FN2rpnWUx7jghg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35154,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35154,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2122,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 35154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35154
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

_source line 9 · 2026-05-10T13:55:42.418Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01R8NMvV7cyTngxP57drbvps`</summary>

```json
{
  "description": "Verify key paper claims and find missing concurrent work for URDF-DiT review",
  "subagent_type": "Explore",
  "prompt": "I'm doing an adversarial review of a robotics ML paper (URDF-DiT) targeting CoRL 2026. I need you to search for and verify several things.\n\n**Task: Do web searches to verify paper existence/claims and find concurrent work**\n\nSearch 1: Verify Dream2Act paper - search for \"Dream2Act arXiv 2603.19709 humanoid whole-body contact\" and fetch the abstract/details. Is the paper real? Does it use post-hoc URDF-IK?\n\nSearch 2: Verify BridgeV2W paper - search for \"BridgeV2W arXiv 2602.03793 ControlNet URDF video diffusion robot\" and verify it uses ControlNet + URDF-rendered masks.\n\nSearch 3: Verify EA-WM paper - search for \"EA-WM arXiv 2605.06192 Event-Aware World Model kinematic\" and check its publication date and scope.\n\nSearch 4: Search for any new concurrent work that combines \"video diffusion\" with \"humanoid robot\" and \"kinematic conditioning\" from 2026 that might be missed. Try: site:arxiv.org humanoid video diffusion kinematic conditioning 2026\n\nSearch 5: Search for \"HumanX arXiv 2602.02473\" to verify the paper exists and its content.\n\nSearch 6: Check for any new papers on \"humanoid training data generation video diffusion\" from April-May 2026 that might be missing from the landscape.\n\nSearch 7: Search for \"Kinema4D arXiv 2603.16669\" to verify the paper exists.\n\nSearch 8: Search for \"MotuBrain arXiv 2604.27792 world action model\" to verify.\n\nSearch 9: Search for \"VAG video action generation arXiv 2604.09330 flow matching robot\" to verify the paper and the quote about video not being influenced by action branch.\n\nFor each search, report: what you found, whether the paper exists, and whether the claims about it are accurate.\n\nAlso, actively search for any MISSING concurrent work from 2025-2026 that combines:\n- Full-body humanoid kinematic conditioning in video generation\n- URDF FK heatmaps in diffusion models\n- IDM-based action extraction from generated video for humanoid robots\n\nReport all findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2130a7a-08af-49fa-a6d1-c96ce67c128f",
  "isSidechain": false,
  "requestId": "req_011Cau16YGnwqt6AyZVwpjAe",
  "type": "assistant",
  "uuid": "346b569b-2851-427d-860c-906ef463d80e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017TJouwT3FN2rpnWUx7jghg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35154,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35154,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2122,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 35154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35154
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

_source line 10 · 2026-05-10T13:55:50.892Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Pne4gjuxA4uwkxszHHi2KD`</summary>

```json
{
  "description": "Search for additional concurrent work on humanoid data generation and video diffusion",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing a ML paper called URDF-DiT about generating synthetic training data for humanoid robots using video diffusion. I need to find any concurrent or competing work that might be missing from the paper's landscape.\n\nPlease search for the following:\n\n1. Search \"site:arxiv.org humanoid loco-manipulation data generation 2026\" - find any papers on synthetic humanoid data generation\n\n2. Search \"humanoid whole-body video generation kinematic 2025 2026\" - find video generation papers for humanoid robots\n\n3. Search \"GR00T Dreams humanoid data generation NVIDIA 2025 2026\" - verify what GR00T Dreams/DreamGen actually does for humanoids\n\n4. Search \"DexMimicGen humanoid manipulation data 2026\" - verify DexMimicGen status\n\n5. Search \"Cosmos humanoid video generation synthetic data 2026\" - find what Cosmos does for humanoids\n\n6. Search \"inverse dynamics model IDM humanoid robot training 2025 2026\" - find IDM-based approaches for humanoid policy training\n\n7. Search \"Wan 2.2 video diffusion robot fine-tuning ControlNet 2026\" - find any other papers fine-tuning Wan 2.2 for robotics\n\n8. Search for \"PhysDreamer OR PhysGen OR RoboDreamer humanoid 2026\" - check adjacent physics-aware video generation for robots\n\n9. Search \"WorldDreamer OR UniSim humanoid data generation 2026\" - check general world model approaches applied to humanoids\n\n10. Search \"site:openreview.net humanoid video diffusion kinematic 2026\" - check CoRL or recent conference submissions\n\nFor each search: report what you found, paper titles, arXiv IDs, and whether they would be relevant concurrent work that the URDF-DiT paper should cite.\n\nSpecifically flag any papers that:\n- Combine video diffusion with full-body humanoid kinematic conditioning\n- Generate synthetic training data for humanoid policies via video synthesis\n- Use inverse dynamics models on generated robot video"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "346b569b-2851-427d-860c-906ef463d80e",
  "isSidechain": false,
  "requestId": "req_011Cau16YGnwqt6AyZVwpjAe",
  "type": "assistant",
  "uuid": "7d840273-708e-4e5d-8287-4f895921ebd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017TJouwT3FN2rpnWUx7jghg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35154,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 35154,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2122,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 35154,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 35154
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

_source line 11 · 2026-05-10T13:56:27.316Z_

<details><summary>↩ Tool result · `toolu_01Pne4gjuxA4uwkxszHHi2KD`</summary>

```text
## Summary of Concurrent and Competing Work for URDF-DiT

I've completed a comprehensive search across 10 different queries. Here are the key findings organized by relevance and the specific criteria you requested:

---

### **CRITICAL FINDINGS: Papers Combining Video Diffusion with Full-Body Humanoid Kinematic Conditioning**

These are the most directly competitive works:

1. **MITTY: Diffusion-Based Human-to-Robot Video Generation** (OpenReview, ICLR 2026 era)
   - Directly combines diffusion transformers with video generation for humanoid robots
   - Uses human-to-robot video conversion with explicit kinematic similarity reasoning
   - **HIGH RELEVANCE** - This is likely a concurrent submission that URDF-DiT should cite

2. **Stable Part Diffusion 4D (SP4D)** (OpenReview)
   - Generates paired RGB and kinematic part videos from monocular input
   - Created KinematicParts20K dataset with rigged objects and kinematic annotations
   - **HIGH RELEVANCE** - Directly addresses kinematic-conditioned video generation

3. **EchoMotion** (OpenReview, ICLR 2026)
   - Models joint distribution of human movement and video using SMPL kinematic parameters
   - Structures constraints around human kinematics rather than raw motion
   - **MODERATE-HIGH RELEVANCE** - Similar kinematic-aware approach but for human motion

---

### **Papers Generating Synthetic Training Data for Humanoid Policies via Video Synthesis**

4. **OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation** (arXiv:2509.26633)
   - Generates synthetic training data specifically for humanoid loco-manipulation
   - Preserves spatial and contact relationships between agent, terrain, and objects
   - Achieved 30-second long-horizon parkour/loco-manipulation on Unitree G1
   - **HIGH RELEVANCE** - Directly competitive data generation approach

5. **Psi-Zero (Ψ₀): An Open Foundation Model for Universal Humanoid Loco-Manipulation** (arXiv:2603.12263)
   - Addresses data generation and utilization for humanoid whole-body control
   - Co-trains on human and humanoid data with kinematic adaptation
   - **MODERATE-HIGH RELEVANCE** - Addresses training data strategy for humanoids

6. **NVIDIA Isaac GR00T-Dreams / DreamGen** (Published May 2025, Updated 2026)
   - Generates massive synthetic trajectory data from single image + language prompt
   - Built on NVIDIA Cosmos world foundation models
   - Used to develop GR00T N1.5 in 36 hours (vs. 3 months manual collection)
   - **HIGH RELEVANCE** - Direct competitor for synthetic humanoid data generation via generative models

7. **Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models** (IEEE 2025)
   - Uses latent diffusion to generate RGB human-object interaction scenes
   - Guides humanoid manipulation planning with contact locations and configurations
   - **MODERATE RELEVANCE** - Diffusion-based humanoid data generation

---

### **Papers Using Inverse Dynamics Models on Robot Video for Policy Training**

8. **Seer: Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation** (arXiv:2412.15109, ICLR 2025 Oral)
   - Predicts actions using inverse dynamics models conditioned on forecasted visual states
   - Designed to annotate action-less videos and treat them as training data
   - Used in GR00T N1 for humanoid training
   - **CRITICAL RELEVANCE** - Directly addresses using IDM to label generated video for policy training

9. **GR00T N1 Whitepaper** (March 2025)
   - Uses inverse dynamics models to infer pseudo-actions and label video
   - Treats annotated videos as additional robot embodiments for training
   - **CRITICAL RELEVANCE** - Production system using IDM on generated/video data

---

### **Motion/Video Generation with Kinematic Control (Related Infrastructure)**

10. **Kimodo: Scaling Controllable Human Motion Generation** (arXiv:2603.15546, March 2026)
    - Kinematic motion diffusion model trained on 700 hours of mocap data
    - Supports full-body keyframes, joint constraints, 2D waypoints, foot contact patterns
    - Available in variants for different skeletons (SOMA, G1 humanoid, SMPL-X)
    - **MODERATE RELEVANCE** - Infrastructure for kinematic-conditioned motion generation

11. **SONIC: Supersizing Motion Tracking for Natural Humanoid Motion** (NVIDIA)
    - Foundation model for motion tracking with universal kinematic planner
    - Supports VR teleoperation, human videos, and VLA models as input
    - 700 hours of high-quality motion data
    - **MODERATE RELEVANCE** - Kinematic-aware motion synthesis infrastructure

12. **Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis** (arXiv:2603.19709)
    - Video synthesis explicitly designed for humanoid morphologies
    - **MODERATE RELEVANCE** - Addresses humanoid-specific video generation

---

### **General World Models and Video Foundation Models (Less Direct but Used by Competitors)**

13. **NVIDIA Cosmos World Foundation Models** (2025-2026)
    - Cosmos Transfer 2.5 and Cosmos Predict 2.5 for synthetic video generation
    - Trained on 200M curated video clips
    - Powers GR00T-Dreams and 1X's humanoid training
    - **MODERATE RELEVANCE** - Infrastructure enabling competitors

14. **WorldDreamer: General World Models for Video Generation** (2024, still active 2025-2026)
    - World model for comprehensive physics and motion understanding
    - Supports image-to-video, text-to-video, action-to-video generation
    - **LOW-MODERATE RELEVANCE** - General infrastructure

15. **UniSim: Learning Interactive Real-World Simulators** (ICLR 2024)
    - World model approach for robot learning
    - 89% success on novel object manipulation vs. 34% for behavioral cloning
    - **LOW-MODERATE RELEVANCE** - General world model approach

---

### **Physics-Aware Video Generation (Less Directly Applicable to Humanoids)**

16. **PhysDreamer: Physics-Based Interaction with 3D Objects** 
    - Physics priors in video generation for object dynamics
    - **LOW RELEVANCE** - Focuses on object interactions, not humanoid kinematics

17. **DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation** (arXiv:2410.24185, ICRA 2025)
    - Synthesizes 21K demos from 60 human demonstrations for humanoid dexterous manipulation
    - Real-to-sim-to-real pipeline tested on real GR-1 humanoid
    - **MODERATE-HIGH RELEVANCE** - Humanoid manipulation data generation, but uses retargeting rather than video diffusion

---

### **Key Competitors NOT Found in Searches**

Based on my searches, I did NOT find papers on:
- **Wan 2.2 fine-tuned specifically for robotics** (General fine-tuning exists, but no published robotics-specific work)
- **PhysGen or RoboDreamer applied to humanoids in 2026** (These exist but no recent humanoid applications found)

---

### **RED FLAG: Critical Work to Cite**

The URDF-DiT paper should **absolutely cite**:

1. **MITTY** - Nearly identical problem statement (video diffusion for humanoid manipulation)
2. **Seer + GR00T N1** - The exact approach of using IDM to label generated video
3. **OmniRetarget** - Concurrent humanoid loco-manipulation synthetic data work
4. **GR00T-Dreams/DreamGen** - Major competitor from NVIDIA in exact space
5. **SP4D (Stable Part Diffusion 4D)** - Kinematic-conditioned video generation

These papers represent the active frontier in this space as of May 2026. The landscape is quite competitive with NVIDIA and several robotics labs actively working on this problem.

Sources:
- [MITTY: Diffusion-Based Human-to-Robot Video](https://openreview.net/pdf/6cd00b0c5b41530ac2f05042ae392df03104bf61.pdf)
- [Stable Part Diffusion 4D: Multi-View RGB and Kinematic Parts Video Generation](https://openreview.net/forum?id=I9F53Qlwur)
- [OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2509.26633)
- [Psi-Zero: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)
- [GR00T-Dreams Technical Blog](https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/)
- [Seer: Predictive Inverse Dynamics Models](https://arxiv.org/abs/2412.15109)
- [GR00T N1 Whitepaper](https://d1qx31qr3h6wln.cloudfront.net/publications/GR00T%20N1%20Whitepaper.pdf)
- [Kimodo: Scaling Controllable Human Motion Generation](https://arxiv.org/html/2603.15546v1)
- [NVIDIA Cosmos World Foundation Models](https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/)
- [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation](https://arxiv.org/abs/2410.24185)
- [WorldDreamer: Towards General World Models for Video Generation](https://world-dreamer.github.io/)
- [UniSim: Learning Interactive Real-World Simulators](https://universal-simulator.github.io/)
- [PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation](https://physdreamer.github.io/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d840273-708e-4e5d-8287-4f895921ebd0",
  "isSidechain": false,
  "promptId": "c7a86d90-025e-47d4-98c5-8fe2906cdffe",
  "type": "user",
  "uuid": "11d4d3bb-53c9-4fa0-8b67-3d14f4039b06",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a ML paper called URDF-DiT about generating synthetic training data for humanoid robots using video diffusion. I need to find any concurrent or competing work that might be missing from the paper's landscape.\n\nPlease search for the following:\n\n1. Search \"site:arxiv.org humanoid loco-manipulation data generation 2026\" - find any papers on synthetic humanoid data generation\n\n2. Search \"humanoid whole-body video generation kinematic 2025 2026\" - find video generation papers for humanoid robots\n\n3. Search \"GR00T Dreams humanoid data generation NVIDIA 2025 2026\" - verify what GR00T Dreams/DreamGen actually does for humanoids\n\n4. Search \"DexMimicGen humanoid manipulation data 2026\" - verify DexMimicGen status\n\n5. Search \"Cosmos humanoid video generation synthetic data 2026\" - find what Cosmos does for humanoids\n\n6. Search \"inverse dynamics model IDM humanoid robot training 2025 2026\" - find IDM-based approaches for humanoid policy training\n\n7. Search \"Wan 2.2 video diffusion robot fine-tuning ControlNet 2026\" - find any other papers fine-tuning Wan 2.2 for robotics\n\n8. Search for \"PhysDreamer OR PhysGen OR RoboDreamer humanoid 2026\" - check adjacent physics-aware video generation for robots\n\n9. Search \"WorldDreamer OR UniSim humanoid data generation 2026\" - check general world model approaches applied to humanoids\n\n10. Search \"site:openreview.net humanoid video diffusion kinematic 2026\" - check CoRL or recent conference submissions\n\nFor each search: report what you found, paper titles, arXiv IDs, and whether they would be relevant concurrent work that the URDF-DiT paper should cite.\n\nSpecifically flag any papers that:\n- Combine video diffusion with full-body humanoid kinematic conditioning\n- Generate synthetic training data for humanoid policies via video synthesis\n- Use inverse dynamics models on generated robot video",
    "agentId": "a64842748a78c3143",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Concurrent and Competing Work for URDF-DiT\n\nI've completed a comprehensive search across 10 different queries. Here are the key findings organized by relevance and the specific criteria you requested:\n\n---\n\n### **CRITICAL FINDINGS: Papers Combining Video Diffusion with Full-Body Humanoid Kinematic Conditioning**\n\nThese are the most directly competitive works:\n\n1. **MITTY: Diffusion-Based Human-to-Robot Video Generation** (OpenReview, ICLR 2026 era)\n   - Directly combines diffusion transformers with video generation for humanoid robots\n   - Uses human-to-robot video conversion with explicit kinematic similarity reasoning\n   - **HIGH RELEVANCE** - This is likely a concurrent submission that URDF-DiT should cite\n\n2. **Stable Part Diffusion 4D (SP4D)** (OpenReview)\n   - Generates paired RGB and kinematic part videos from monocular input\n   - Created KinematicParts20K dataset with rigged objects and kinematic annotations\n   - **HIGH RELEVANCE** - Directly addresses kinematic-conditioned video generation\n\n3. **EchoMotion** (OpenReview, ICLR 2026)\n   - Models joint distribution of human movement and video using SMPL kinematic parameters\n   - Structures constraints around human kinematics rather than raw motion\n   - **MODERATE-HIGH RELEVANCE** - Similar kinematic-aware approach but for human motion\n\n---\n\n### **Papers Generating Synthetic Training Data for Humanoid Policies via Video Synthesis**\n\n4. **OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation** (arXiv:2509.26633)\n   - Generates synthetic training data specifically for humanoid loco-manipulation\n   - Preserves spatial and contact relationships between agent, terrain, and objects\n   - Achieved 30-second long-horizon parkour/loco-manipulation on Unitree G1\n   - **HIGH RELEVANCE** - Directly competitive data generation approach\n\n5. **Psi-Zero (Ψ₀): An Open Foundation Model for Universal Humanoid Loco-Manipulation** (arXiv:2603.12263)\n   - Addresses data generation and utilization for humanoid whole-body control\n   - Co-trains on human and humanoid data with kinematic adaptation\n   - **MODERATE-HIGH RELEVANCE** - Addresses training data strategy for humanoids\n\n6. **NVIDIA Isaac GR00T-Dreams / DreamGen** (Published May 2025, Updated 2026)\n   - Generates massive synthetic trajectory data from single image + language prompt\n   - Built on NVIDIA Cosmos world foundation models\n   - Used to develop GR00T N1.5 in 36 hours (vs. 3 months manual collection)\n   - **HIGH RELEVANCE** - Direct competitor for synthetic humanoid data generation via generative models\n\n7. **Physically Consistent Humanoid Loco-Manipulation Using Latent Diffusion Models** (IEEE 2025)\n   - Uses latent diffusion to generate RGB human-object interaction scenes\n   - Guides humanoid manipulation planning with contact locations and configurations\n   - **MODERATE RELEVANCE** - Diffusion-based humanoid data generation\n\n---\n\n### **Papers Using Inverse Dynamics Models on Robot Video for Policy Training**\n\n8. **Seer: Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation** (arXiv:2412.15109, ICLR 2025 Oral)\n   - Predicts actions using inverse dynamics models conditioned on forecasted visual states\n   - Designed to annotate action-less videos and treat them as training data\n   - Used in GR00T N1 for humanoid training\n   - **CRITICAL RELEVANCE** - Directly addresses using IDM to label generated video for policy training\n\n9. **GR00T N1 Whitepaper** (March 2025)\n   - Uses inverse dynamics models to infer pseudo-actions and label video\n   - Treats annotated videos as additional robot embodiments for training\n   - **CRITICAL RELEVANCE** - Production system using IDM on generated/video data\n\n---\n\n### **Motion/Video Generation with Kinematic Control (Related Infrastructure)**\n\n10. **Kimodo: Scaling Controllable Human Motion Generation** (arXiv:2603.15546, March 2026)\n    - Kinematic motion diffusion model trained on 700 hours of mocap data\n    - Supports full-body keyframes, joint constraints, 2D waypoints, foot contact patterns\n    - Available in variants for different skeletons (SOMA, G1 humanoid, SMPL-X)\n    - **MODERATE RELEVANCE** - Infrastructure for kinematic-conditioned motion generation\n\n11. **SONIC: Supersizing Motion Tracking for Natural Humanoid Motion** (NVIDIA)\n    - Foundation model for motion tracking with universal kinematic planner\n    - Supports VR teleoperation, human videos, and VLA models as input\n    - 700 hours of high-quality motion data\n    - **MODERATE RELEVANCE** - Kinematic-aware motion synthesis infrastructure\n\n12. **Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis** (arXiv:2603.19709)\n    - Video synthesis explicitly designed for humanoid morphologies\n    - **MODERATE RELEVANCE** - Addresses humanoid-specific video generation\n\n---\n\n### **General World Models and Video Foundation Models (Less Direct but Used by Competitors)**\n\n13. **NVIDIA Cosmos World Foundation Models** (2025-2026)\n    - Cosmos Transfer 2.5 and Cosmos Predict 2.5 for synthetic video generation\n    - Trained on 200M curated video clips\n    - Powers GR00T-Dreams and 1X's humanoid training\n    - **MODERATE RELEVANCE** - Infrastructure enabling competitors\n\n14. **WorldDreamer: General World Models for Video Generation** (2024, still active 2025-2026)\n    - World model for comprehensive physics and motion understanding\n    - Supports image-to-video, text-to-video, action-to-video generation\n    - **LOW-MODERATE RELEVANCE** - General infrastructure\n\n15. **UniSim: Learning Interactive Real-World Simulators** (ICLR 2024)\n    - World model approach for robot learning\n    - 89% success on novel object manipulation vs. 34% for behavioral cloning\n    - **LOW-MODERATE RELEVANCE** - General world model approach\n\n---\n\n### **Physics-Aware Video Generation (Less Directly Applicable to Humanoids)**\n\n16. **PhysDreamer: Physics-Based Interaction with 3D Objects** \n    - Physics priors in video generation for object dynamics\n    - **LOW RELEVANCE** - Focuses on object interactions, not humanoid kinematics\n\n17. **DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation** (arXiv:2410.24185, ICRA 2025)\n    - Synthesizes 21K demos from 60 human demonstrations for humanoid dexterous manipulation\n    - Real-to-sim-to-real pipeline tested on real GR-1 humanoid\n    - **MODERATE-HIGH RELEVANCE** - Humanoid manipulation data generation, but uses retargeting rather than video diffusion\n\n---\n\n### **Key Competitors NOT Found in Searches**\n\nBased on my searches, I did NOT find papers on:\n- **Wan 2.2 fine-tuned specifically for robotics** (General fine-tuning exists, but no published robotics-specific work)\n- **PhysGen or RoboDreamer applied to humanoids in 2026** (These exist but no recent humanoid applications found)\n\n---\n\n### **RED FLAG: Critical Work to Cite**\n\nThe URDF-DiT paper should **absolutely cite**:\n\n1. **MITTY** - Nearly identical problem statement (video diffusion for humanoid manipulation)\n2. **Seer + GR00T N1** - The exact approach of using IDM to label generated video\n3. **OmniRetarget** - Concurrent humanoid loco-manipulation synthetic data work\n4. **GR00T-Dreams/DreamGen** - Major competitor from NVIDIA in exact space\n5. **SP4D (Stable Part Diffusion 4D)** - Kinematic-conditioned video generation\n\nThese papers represent the active frontier in this space as of May 2026. The landscape is quite competitive with NVIDIA and several robotics labs actively working on this problem.\n\nSources:\n- [MITTY: Diffusion-Based Human-to-Robot Video](https://openreview.net/pdf/6cd00b0c5b41530ac2f05042ae392df03104bf61.pdf)\n- [Stable Part Diffusion 4D: Multi-View RGB and Kinematic Parts Video Generation](https://openreview.net/forum?id=I9F53Qlwur)\n- [OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2509.26633)\n- [Psi-Zero: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)\n- [GR00T-Dreams Technical Blog](https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/)\n- [Seer: Predictive Inverse Dynamics Models](https://arxiv.org/abs/2412.15109)\n- [GR00T N1 Whitepaper](https://d1qx31qr3h6wln.cloudfront.net/publications/GR00T%20N1%20Whitepaper.pdf)\n- [Kimodo: Scaling Controllable Human Motion Generation](https://arxiv.org/html/2603.15546v1)\n- [NVIDIA Cosmos World Foundation Models](https://developer.nvidia.com/blog/scale-synthetic-data-and-physical-ai-reasoning-with-nvidia-cosmos-world-foundation-models/)\n- [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation](https://arxiv.org/abs/2410.24185)\n- [WorldDreamer: Towards General World Models for Video Generation](https://world-dreamer.github.io/)\n- [UniSim: Learning Interactive Real-World Simulators](https://universal-simulator.github.io/)\n- [PhysDreamer: Physics-Based Interaction with 3D Objects via Video Generation](https://physdreamer.github.io/)"
      }
    ],
    "totalDurationMs": 36420,
    "totalTokens": 31092,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 6716,
      "cache_creation_input_tokens": 4752,
      "cache_read_input_tokens": 17054,
      "output_tokens": 2570,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4752
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6716,
          "output_tokens": 2570,
          "cache_read_input_tokens": 17054,
          "cache_creation_input_tokens": 4752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4752,
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
      "otherToolCount": 10
    }
  },
  "sourceToolAssistantUUID": "7d840273-708e-4e5d-8287-4f895921ebd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "11d4d3bb-53c9-4fa0-8b67-3d14f4039b06",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "URDF-DiT: Full-body kinematic conditioning for humanoid IDM training data",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9"
}
```

---

### Tool result

_source line 14 · 2026-05-10T13:57:12.881Z_

<details><summary>↩ Tool result · `toolu_01R8NMvV7cyTngxP57drbvps`</summary>

```text
Excellent! Now let me compile my comprehensive findings report.

## COMPREHENSIVE VERIFICATION REPORT: URDF-DiT ADVERSARIAL REVIEW

### PAPER VERIFICATION RESULTS

#### Search 1: Dream2Act (arXiv 2603.19709)
**Status: VERIFIED - Paper EXISTS**
- **Full Title:** Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis
- **Publication Date:** March 20, 2026
- **Claims Verification:** The paper DOES use post-hoc URDF-constrained inverse kinematics. The framework employs a robust pose extraction system that cascades:
  1. 2D pose estimation
  2. 2D-to-3D lifting
  3. URDF-constrained inverse kinematics to recover physically feasible, robot-native joint trajectories
- **Key Technical Detail:** Uses this pipeline to avoid traditional retargeting errors and maintain robot-consistent spatial alignment, enabling reliable contact formation
- **Evaluation:** Tested on Unitree G1 across four whole-body mobile interaction tasks
- **Source:** https://arxiv.org/html/2603.19709v1

#### Search 2: BridgeV2W (arXiv 2602.03793)
**Status: VERIFIED - Paper EXISTS**
- **Full Title:** BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks
- **Publication Date:** February 2026
- **Claims Verification:** The paper DOES use ControlNet + URDF-rendered masks. Specifically:
  - Converts coordinate-space actions into pixel-aligned embodiment masks rendered from URDF and camera parameters
  - Injects these masks into a pretrained video generation model via a ControlNet-style pathway
  - Adds view-specific conditioning to accommodate camera viewpoints
  - Uses flow-based motion loss for mitigating overfitting to static backgrounds
- **Architecture:** Unified world model architecture across different embodiments
- **Source:** https://arxiv.org/abs/2602.03793

#### Search 3: EA-WM (arXiv 2605.06192)
**Status: VERIFIED - Paper EXISTS (very recent)**
- **Full Title:** EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields
- **Publication Date:** May 7, 2026 (published during adversarial review window)
- **Claims Verification:** Paper uses structured kinematic-to-visual action fields, projecting actions through kinematic-to-visual mappings rather than low-dimensional tokens
- **Problem Addressed:** Recent world-action models fail to preserve precise robot spatial geometry and fine-grained robot-object interaction dynamics
- **Institutions:** Fudan University, Zhongguanchan Academy, Zhongguanchan Institute of AI
- **Scope:** Fully addresses kinematic-to-visual action conditioning in video generation
- **Source:** https://arxiv.org/html/2605.06192v1

#### Search 4: HumanX (arXiv 2602.02473)
**Status: VERIFIED - Paper EXISTS**
- **Full Title:** HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos
- **Publication Date:** February 2, 2026
- **Key Features:**
  - XGen: Data generation pipeline synthesizing diverse, physically plausible robot interaction data from video
  - XMimic: Unified imitation learning framework for generalizable interaction skills
- **Evaluation:** 5 domains (basketball, football, badminton, cargo pickup, reactive fighting) with 10 learned skills
- **Performance:** 8x higher generalization success than prior methods; zero-shot transfer to Unitree G1
- **Source:** https://arxiv.org/html/2602.02473

#### Search 5: Kinema4D (arXiv 2603.16669)
**Status: VERIFIED - Paper EXISTS**
- **Full Title:** Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation
- **Publication Date:** March 17, 2026
- **Key Technical Detail:** Uses URDF-based 3D robot kinematics to produce precise 4D robot control trajectories
- **Dataset:** Robo4D-200k with 201,426 real-world and synthetic demonstrations with high-quality 4D annotations
- **Contribution:** Disentangles robot-world interaction with precise 4D representation of robot controls
- **Source:** https://arxiv.org/html/2603.16669v1; GitHub: https://github.com/mutianxu/Kinema4D

#### Search 6: MotuBrain (arXiv 2604.27792)
**Status: VERIFIED - Paper EXISTS**
- **Full Title:** MotuBrain: An Advanced World Action Model for Robot Control
- **Publication Date:** April 27, 2026 (v2)
- **Key Features:**
  - UniDiffuser for jointly modeling video and action as continuous modalities
  - Three-stream Mixture-of-Transformers architecture
  - Supports five inference distributions: VLA policy, world modeling, video generation, inverse dynamics, joint video-action prediction
- **Performance:** 63.77 EWM Score on WorldArena; 96.0 average on RoboTwin 2.0 across 50 tasks
- **Note:** Only model exceeding 95.0 on randomized environments
- **Source:** https://arxiv.org/html/2604.27792v2

#### Search 7: VAG (arXiv 2604.09330)
**Status: VERIFIED - Paper EXISTS**
- **Full Title:** VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis
- **Publication Date:** April 9, 2026
- **Technical Approach:** Flow-matching-based unified dual-stream framework jointly generating video and action
- **Problem Addressed:** Existing World-Action models lack strong video-action alignment; two-stage pipelines introduce inefficiency and error accumulation
- **Key Innovation:** Direct simultaneous generation of video and actions for improved alignment and efficiency
- **Source:** https://arxiv.org/html/2604.09330

---

### CONCURRENT WORK DISCOVERY - CRITICAL FINDINGS

#### Major Missing Works Identified:

**1. Kimodo (arXiv 2603.15546) - HIGHLY RELEVANT**
- **Publication Date:** March 16, 2026
- **Significance:** Kinematic motion diffusion model trained on 700 hours of optical mocap data
- **Key Features:** 
  - Full-body kinematic constraints (keyframes, joint positions/rotations, 2D waypoints, paths, foot contact)
  - Two-stage diffusion architecture for root and body motion decomposition
  - Text-guided controllable humanoid motion generation
  - Compatible with humanoid embodiments including Unitree G1
- **Technical Relevance:** Operates in kinematic space with explicit control over motion generation
- **Source:** https://arxiv.org/html/2603.15546v1; https://research.nvidia.com/labs/sil/projects/kimodo/

**2. G-DReaM (arXiv 2505.20857) - Cross-Embodiment Conditioning**
- **Publication Date:** May 27, 2025
- **Approach:** Graph-conditioned diffusion for motion retargeting across diverse embodiments
- **Technical Innovation:**
  - Graph-based encoding capturing topological and geometrical features
  - Unified handling of heterogeneous embodiments without requiring motion data
  - Energy-based guidance using retargeting losses
  - Custom transformer-based attention for joint-level knowledge exploitation
- **Relevance:** Addresses kinematic structure representation for embodiment-aware generation
- **Source:** https://arxiv.org/html/2505.20857v1

**3. Humanoid World Models (arXiv 2506.01182) - May 2026**
- **Full Title:** Humanoid World Models: Open World Foundation Models for Humanoid Robotics
- **Publication Date:** June 2025 (submitted May 2026)
- **Key Features:**
  - Lightweight, open-source models forecasting future egocentric video
  - Conditioned on humanoid control tokens
  - Trained on 100 hours of humanoid demonstrations
  - Two generative model types: Masked Transformers and Flow-Matching
- **Relevance:** Direct competitor for kinematic-conditioned humanoid video generation
- **Source:** https://arxiv.org/abs/2506.01182

**4. DreamGen (arXiv 2505.12705) - IDM-based Action Extraction**
- **Publication Date:** May 2025
- **Key Technical Detail:** Uses inverse dynamics diffusion transformers to extract actions from generated video
- **Vision Encoder:** SigLIP-2 with flow matching objective
- **Humanoid Performance:** Enabled 22 new behaviors in seen/unseen environments from single task data
- **Relevance:** Addresses IDM extraction from generated video for humanoid robots
- **Source:** https://arxiv.org/html/2505.12705v1; https://rpl.cs.utexas.edu/publications/2025/09/30/jang-corl25-dreamgen/

**5. TC-IDM (arXiv 2601.18323) - Executability-Aware IDM**
- **Full Title:** TC-IDM: Grounding Video Generation for Executable Zero-shot Robot Motion
- **Problem Addressed:** Video world models lack explicit executability constraints; visually coherent rollouts may violate rigid-body/kinematic consistency
- **Technical Approach:** Tool-centric IDM focusing on stable end-effector motion as envisioned by world models
- **Relevance:** Directly tackles the executability gap for kinematic models
- **Source:** https://arxiv.org/html/2601.18323v1

**6. DeFI (arXiv from GitHub info - ICLR 2026 Accepted)**
- **Full Title:** Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining
- **Institution:** Logos Robotics Group
- **Key Innovation:** Decouples visual forward and inverse dynamics pretraining
- **Components:**
  - General Forward Dynamics Model (GFDM) trained on diverse human/robot video
  - General Inverse Dynamics Model (GIDM) with self-supervised learning
- **Relevance:** Addresses separate kinematic forward-inverse model training
- **Source:** https://github.com/LogosRoboticsGroup/DeFi

**7. Hi-WM (arXiv 2604.21741) - April 2026**
- **Full Title:** Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training
- **Approach:** Post-training framework using learned world models as corrective substrate for failure-targeted policy improvement
- **Relevance:** Human-corrective world model refinement for humanoid control
- **Source:** https://arxiv.org/html/2604.21741v1

**8. UniMorphGrasp (arXiv 2602.00915) - URDF-Aware Diffusion**
- **Full Title:** UniMorphGrasp: Diffusion Model with Morphology-Awareness for Cross-Embodiment Dexterous Grasp Generation
- **Key Feature:** Encodes hand kinematics from URDF as graph-based features to guide denoising
- **Relevance:** Direct precedent for URDF-based kinematic conditioning in diffusion models
- **Source:** https://arxiv.org/html/2602.00915

**9. X-Humanoid (arXiv 2512.04537) - Humanoid Video Synthesis**
- **Publication Date:** December 2025
- **Approach:** Adapts Wan 2.2 diffusion transformer to human-to-humanoid video conversion
- **Relevance:** Direct humanoid video synthesis without explicit kinematic conditioning
- **Source:** https://arxiv.org/html/2512.04537v1

**10. FlowAct-R1 (arXiv 2601.10103) - Real-time Interactive Humanoid**
- **Full Title:** FlowAct-R1: Towards Interactive Humanoid Video Generation
- **Architecture:** MMDiT for streaming humanoid video synthesis
- **Relevance:** Low-latency humanoid-specific video generation framework
- **Source:** https://arxiv.org/html/2601.10103v1

---

### LANDSCAPE ANALYSIS: TRENDS & GAPS

#### 1. **Kinematic Conditioning Approaches (2025-2026)**
- **BridgeV2W:** URDF-rendered masks via ControlNet
- **EA-WM:** Structured kinematic-to-visual action fields  
- **Kimodo:** Text + kinematic constraints (keyframes, joint positions)
- **G-DReaM:** Graph-based kinematic structure encoding
- **UniMorphGrasp:** URDF as graph-based feature guidance

**Gap Analysis:** Most approaches render kinematics spatially (masks/heatmaps) or encode them in latent space (graphs/fields). Few combine both spatial rendering AND latent structural encoding simultaneously like URDF-DiT appears to propose.

#### 2. **URDF Usage Patterns**
- **Dream2Act:** Post-hoc IK with URDF for trajectory validation
- **BridgeV2W:** URDF rendering for embodiment masks
- **Kinema4D:** URDF kinematics for 4D trajectory generation
- **UniMorphGrasp:** URDF parsing for morphology encoding

**Gap Analysis:** URDF is primarily used for either post-hoc constraint satisfaction or mask rendering. Using URDF FK heatmaps as explicit conditioning during diffusion denoising appears less explored.

#### 3. **IDM Action Extraction (2025-2026)**
- **MotuBrain:** Unified model with explicit IDM head
- **VAG:** Joint video-action generation without sequential IDM
- **DreamGen:** IDM diffusion transformers for action extraction
- **TC-IDM:** Tool-centric IDM for executability
- **DeFI:** Decoupled forward-inverse dynamics models

**Gap Analysis:** IDM extraction exists but is typically post-hoc or requires task-specific training. Fully end-to-end IDM-aware diffusion during video generation training is less established for humanoids.

#### 4. **Humanoid-Specific Contributions (Feb-May 2026)**
- **HumanX:** 8x better generalization, zero-shot transfer
- **Dream2Act:** Whole-body contact-aware synthesis
- **EA-WM:** Event-aware kinematic-visual alignment
- **Humanoid World Models:** Egocentric video with control tokens

**Gap Analysis:** Recent work increasingly focuses on full-body control and contact dynamics. URDF-DiT's combination of full-body kinematic conditioning + FK heatmaps + IDM-aware training appears novel.

#### 5. **Complete Architecture Innovations (April-May 2026)**
- **MotuBrain:** Three-stream Mixture-of-Experts with unified action representation
- **VAG:** Flow-matching dual-stream for simultaneous video-action generation
- **EA-WM:** Structured kinematic fields as intermediate representation

**Gap Analysis:** The field is moving toward explicit kinematic structure integration rather than implicit conditioning.

---

### CRITICAL CONCURRENT WORK ALERT FOR CORL 2026 SUBMISSION

**HIGH PRIORITY PAPERS TO CITE:**
1. **BridgeV2W** (2602.03793) - Direct URDF conditioning precedent
2. **EA-WM** (2605.06192) - Just published May 7, 2026; kinematic-visual coupling
3. **Kimodo** (2603.15546) - Kinematic motion diffusion baseline
4. **Dream2Act** (2603.19709) - URDF IK post-processing pipeline
5. **MotuBrain** (2604.27792) - State-of-art world action model
6. **DreamGen** (2505.12705) - IDM-based action recovery from video

**NOVELTY CLAIMS TO VERIFY:**
- If URDF-DiT claims to use FK heatmaps as conditioning: Check if Kimodo, BridgeV2W, or other 2026 papers already explore this
- If URDF-DiT claims joint optimization of video+action with kinematic constraints: Compare to VAG and MotuBrain architectures
- If URDF-DiT claims full-body humanoid support: Compare to HumanX, Dream2Act, Humanoid World Models, and EA-WM on this dimension

**POTENTIAL LANDSCAPE GAPS THAT URDF-DiT MIGHT ADDRESS:**
1. Explicit URDF FK heatmap rendering during diffusion conditioning (vs. post-hoc or implicit)
2. End-to-end kinematic consistency enforcement throughout denoising
3. Joint full-body humanoid + IDM + kinematic structure optimization
4. Scalability to diverse humanoid morphologies with unified kinematic conditioning

---

### SOURCES

- [Dream2Act: Morphology-Consistent Humanoid Interaction](https://arxiv.org/html/2603.19709v1)
- [BridgeV2W: Bridging Video Generation Models](https://arxiv.org/abs/2602.03793)
- [EA-WM: Event-Aware Generative World Model](https://arxiv.org/html/2605.06192v1)
- [HumanX: Agile Humanoid Skills from Videos](https://arxiv.org/html/2602.02473)
- [Kinema4D: Kinematic 4D World Modeling](https://arxiv.org/html/2603.16669v1)
- [MotuBrain: Advanced World Action Model](https://arxiv.org/html/2604.27792v2)
- [VAG: Dual-Stream Video-Action Generation](https://arxiv.org/html/2604.09330)
- [Kimodo: Scaling Controllable Human Motion](https://arxiv.org/html/2603.15546v1)
- [G-DReaM: Graph-conditioned Diffusion Retargeting](https://arxiv.org/html/2505.20857v1)
- [DreamGen: Unlocking Generalization in Robot Learning](https://arxiv.org/html/2505.12705v1)
- [TC-IDM: Grounding Video Generation for Executable Robot Motion](https://arxiv.org/html/2601.18323v1)
- [DeFI: Disentangled Robot Learning via Separate Dynamics](https://github.com/LogosRoboticsGroup/DeFI)
- [Hi-WM: Human-in-the-World-Model](https://arxiv.org/html/2604.21741v1)
- [UniMorphGrasp: Morphology-Aware Grasp Generation](https://arxiv.org/html/2602.00915)
- [X-Humanoid: Robotize Human Videos](https://arxiv.org/html/2512.04537v1)
- [FlowAct-R1: Interactive Humanoid Video Generation](https://arxiv.org/html/2601.10103v1)
- [Humanoid World Models: Open Foundation Models](https://arxiv.org/abs/2506.01182)
- [Differentiable Robot Rendering](https://arxiv.org/html/2410.13851v1)
- [URDFormer: Constructing Simulation Environments](https://arxiv.org/html/2405.11656v2)
- [X-Diffusion: Cross-Embodiment Diffusion Policies](https://arxiv.org/html/2511.04671v2)
- [Controllable Complex Human Motion via Text-to-Skeleton](https://arxiv.org/html/2603.08028)
- [World Action Models are Zero-shot Policies](https://arxiv.org/html/2602.15922v1)
- [Unified 4D World Action Modeling](https://arxiv.org/html/2604.26694v2)
- [A Comprehensive Survey on World Models for Embodied AI](https://arxiv.org/html/2510.16732v1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "346b569b-2851-427d-860c-906ef463d80e",
  "isSidechain": false,
  "promptId": "c7a86d90-025e-47d4-98c5-8fe2906cdffe",
  "type": "user",
  "uuid": "bbc7df6d-4b7a-4490-9c80-c2cb43080596",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm doing an adversarial review of a robotics ML paper (URDF-DiT) targeting CoRL 2026. I need you to search for and verify several things.\n\n**Task: Do web searches to verify paper existence/claims and find concurrent work**\n\nSearch 1: Verify Dream2Act paper - search for \"Dream2Act arXiv 2603.19709 humanoid whole-body contact\" and fetch the abstract/details. Is the paper real? Does it use post-hoc URDF-IK?\n\nSearch 2: Verify BridgeV2W paper - search for \"BridgeV2W arXiv 2602.03793 ControlNet URDF video diffusion robot\" and verify it uses ControlNet + URDF-rendered masks.\n\nSearch 3: Verify EA-WM paper - search for \"EA-WM arXiv 2605.06192 Event-Aware World Model kinematic\" and check its publication date and scope.\n\nSearch 4: Search for any new concurrent work that combines \"video diffusion\" with \"humanoid robot\" and \"kinematic conditioning\" from 2026 that might be missed. Try: site:arxiv.org humanoid video diffusion kinematic conditioning 2026\n\nSearch 5: Search for \"HumanX arXiv 2602.02473\" to verify the paper exists and its content.\n\nSearch 6: Check for any new papers on \"humanoid training data generation video diffusion\" from April-May 2026 that might be missing from the landscape.\n\nSearch 7: Search for \"Kinema4D arXiv 2603.16669\" to verify the paper exists.\n\nSearch 8: Search for \"MotuBrain arXiv 2604.27792 world action model\" to verify.\n\nSearch 9: Search for \"VAG video action generation arXiv 2604.09330 flow matching robot\" to verify the paper and the quote about video not being influenced by action branch.\n\nFor each search, report: what you found, whether the paper exists, and whether the claims about it are accurate.\n\nAlso, actively search for any MISSING concurrent work from 2025-2026 that combines:\n- Full-body humanoid kinematic conditioning in video generation\n- URDF FK heatmaps in diffusion models\n- IDM-based action extraction from generated video for humanoid robots\n\nReport all findings.",
    "agentId": "a7d15b733ff6ae4db",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now let me compile my comprehensive findings report.\n\n## COMPREHENSIVE VERIFICATION REPORT: URDF-DiT ADVERSARIAL REVIEW\n\n### PAPER VERIFICATION RESULTS\n\n#### Search 1: Dream2Act (arXiv 2603.19709)\n**Status: VERIFIED - Paper EXISTS**\n- **Full Title:** Morphology-Consistent Humanoid Interaction through Robot-Centric Video Synthesis\n- **Publication Date:** March 20, 2026\n- **Claims Verification:** The paper DOES use post-hoc URDF-constrained inverse kinematics. The framework employs a robust pose extraction system that cascades:\n  1. 2D pose estimation\n  2. 2D-to-3D lifting\n  3. URDF-constrained inverse kinematics to recover physically feasible, robot-native joint trajectories\n- **Key Technical Detail:** Uses this pipeline to avoid traditional retargeting errors and maintain robot-consistent spatial alignment, enabling reliable contact formation\n- **Evaluation:** Tested on Unitree G1 across four whole-body mobile interaction tasks\n- **Source:** https://arxiv.org/html/2603.19709v1\n\n#### Search 2: BridgeV2W (arXiv 2602.03793)\n**Status: VERIFIED - Paper EXISTS**\n- **Full Title:** BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks\n- **Publication Date:** February 2026\n- **Claims Verification:** The paper DOES use ControlNet + URDF-rendered masks. Specifically:\n  - Converts coordinate-space actions into pixel-aligned embodiment masks rendered from URDF and camera parameters\n  - Injects these masks into a pretrained video generation model via a ControlNet-style pathway\n  - Adds view-specific conditioning to accommodate camera viewpoints\n  - Uses flow-based motion loss for mitigating overfitting to static backgrounds\n- **Architecture:** Unified world model architecture across different embodiments\n- **Source:** https://arxiv.org/abs/2602.03793\n\n#### Search 3: EA-WM (arXiv 2605.06192)\n**Status: VERIFIED - Paper EXISTS (very recent)**\n- **Full Title:** EA-WM: Event-Aware Generative World Model with Structured Kinematic-to-Visual Action Fields\n- **Publication Date:** May 7, 2026 (published during adversarial review window)\n- **Claims Verification:** Paper uses structured kinematic-to-visual action fields, projecting actions through kinematic-to-visual mappings rather than low-dimensional tokens\n- **Problem Addressed:** Recent world-action models fail to preserve precise robot spatial geometry and fine-grained robot-object interaction dynamics\n- **Institutions:** Fudan University, Zhongguanchan Academy, Zhongguanchan Institute of AI\n- **Scope:** Fully addresses kinematic-to-visual action conditioning in video generation\n- **Source:** https://arxiv.org/html/2605.06192v1\n\n#### Search 4: HumanX (arXiv 2602.02473)\n**Status: VERIFIED - Paper EXISTS**\n- **Full Title:** HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos\n- **Publication Date:** February 2, 2026\n- **Key Features:**\n  - XGen: Data generation pipeline synthesizing diverse, physically plausible robot interaction data from video\n  - XMimic: Unified imitation learning framework for generalizable interaction skills\n- **Evaluation:** 5 domains (basketball, football, badminton, cargo pickup, reactive fighting) with 10 learned skills\n- **Performance:** 8x higher generalization success than prior methods; zero-shot transfer to Unitree G1\n- **Source:** https://arxiv.org/html/2602.02473\n\n#### Search 5: Kinema4D (arXiv 2603.16669)\n**Status: VERIFIED - Paper EXISTS**\n- **Full Title:** Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation\n- **Publication Date:** March 17, 2026\n- **Key Technical Detail:** Uses URDF-based 3D robot kinematics to produce precise 4D robot control trajectories\n- **Dataset:** Robo4D-200k with 201,426 real-world and synthetic demonstrations with high-quality 4D annotations\n- **Contribution:** Disentangles robot-world interaction with precise 4D representation of robot controls\n- **Source:** https://arxiv.org/html/2603.16669v1; GitHub: https://github.com/mutianxu/Kinema4D\n\n#### Search 6: MotuBrain (arXiv 2604.27792)\n**Status: VERIFIED - Paper EXISTS**\n- **Full Title:** MotuBrain: An Advanced World Action Model for Robot Control\n- **Publication Date:** April 27, 2026 (v2)\n- **Key Features:**\n  - UniDiffuser for jointly modeling video and action as continuous modalities\n  - Three-stream Mixture-of-Transformers architecture\n  - Supports five inference distributions: VLA policy, world modeling, video generation, inverse dynamics, joint video-action prediction\n- **Performance:** 63.77 EWM Score on WorldArena; 96.0 average on RoboTwin 2.0 across 50 tasks\n- **Note:** Only model exceeding 95.0 on randomized environments\n- **Source:** https://arxiv.org/html/2604.27792v2\n\n#### Search 7: VAG (arXiv 2604.09330)\n**Status: VERIFIED - Paper EXISTS**\n- **Full Title:** VAG: Dual-Stream Video-Action Generation for Embodied Data Synthesis\n- **Publication Date:** April 9, 2026\n- **Technical Approach:** Flow-matching-based unified dual-stream framework jointly generating video and action\n- **Problem Addressed:** Existing World-Action models lack strong video-action alignment; two-stage pipelines introduce inefficiency and error accumulation\n- **Key Innovation:** Direct simultaneous generation of video and actions for improved alignment and efficiency\n- **Source:** https://arxiv.org/html/2604.09330\n\n---\n\n### CONCURRENT WORK DISCOVERY - CRITICAL FINDINGS\n\n#### Major Missing Works Identified:\n\n**1. Kimodo (arXiv 2603.15546) - HIGHLY RELEVANT**\n- **Publication Date:** March 16, 2026\n- **Significance:** Kinematic motion diffusion model trained on 700 hours of optical mocap data\n- **Key Features:** \n  - Full-body kinematic constraints (keyframes, joint positions/rotations, 2D waypoints, paths, foot contact)\n  - Two-stage diffusion architecture for root and body motion decomposition\n  - Text-guided controllable humanoid motion generation\n  - Compatible with humanoid embodiments including Unitree G1\n- **Technical Relevance:** Operates in kinematic space with explicit control over motion generation\n- **Source:** https://arxiv.org/html/2603.15546v1; https://research.nvidia.com/labs/sil/projects/kimodo/\n\n**2. G-DReaM (arXiv 2505.20857) - Cross-Embodiment Conditioning**\n- **Publication Date:** May 27, 2025\n- **Approach:** Graph-conditioned diffusion for motion retargeting across diverse embodiments\n- **Technical Innovation:**\n  - Graph-based encoding capturing topological and geometrical features\n  - Unified handling of heterogeneous embodiments without requiring motion data\n  - Energy-based guidance using retargeting losses\n  - Custom transformer-based attention for joint-level knowledge exploitation\n- **Relevance:** Addresses kinematic structure representation for embodiment-aware generation\n- **Source:** https://arxiv.org/html/2505.20857v1\n\n**3. Humanoid World Models (arXiv 2506.01182) - May 2026**\n- **Full Title:** Humanoid World Models: Open World Foundation Models for Humanoid Robotics\n- **Publication Date:** June 2025 (submitted May 2026)\n- **Key Features:**\n  - Lightweight, open-source models forecasting future egocentric video\n  - Conditioned on humanoid control tokens\n  - Trained on 100 hours of humanoid demonstrations\n  - Two generative model types: Masked Transformers and Flow-Matching\n- **Relevance:** Direct competitor for kinematic-conditioned humanoid video generation\n- **Source:** https://arxiv.org/abs/2506.01182\n\n**4. DreamGen (arXiv 2505.12705) - IDM-based Action Extraction**\n- **Publication Date:** May 2025\n- **Key Technical Detail:** Uses inverse dynamics diffusion transformers to extract actions from generated video\n- **Vision Encoder:** SigLIP-2 with flow matching objective\n- **Humanoid Performance:** Enabled 22 new behaviors in seen/unseen environments from single task data\n- **Relevance:** Addresses IDM extraction from generated video for humanoid robots\n- **Source:** https://arxiv.org/html/2505.12705v1; https://rpl.cs.utexas.edu/publications/2025/09/30/jang-corl25-dreamgen/\n\n**5. TC-IDM (arXiv 2601.18323) - Executability-Aware IDM**\n- **Full Title:** TC-IDM: Grounding Video Generation for Executable Zero-shot Robot Motion\n- **Problem Addressed:** Video world models lack explicit executability constraints; visually coherent rollouts may violate rigid-body/kinematic consistency\n- **Technical Approach:** Tool-centric IDM focusing on stable end-effector motion as envisioned by world models\n- **Relevance:** Directly tackles the executability gap for kinematic models\n- **Source:** https://arxiv.org/html/2601.18323v1\n\n**6. DeFI (arXiv from GitHub info - ICLR 2026 Accepted)**\n- **Full Title:** Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining\n- **Institution:** Logos Robotics Group\n- **Key Innovation:** Decouples visual forward and inverse dynamics pretraining\n- **Components:**\n  - General Forward Dynamics Model (GFDM) trained on diverse human/robot video\n  - General Inverse Dynamics Model (GIDM) with self-supervised learning\n- **Relevance:** Addresses separate kinematic forward-inverse model training\n- **Source:** https://github.com/LogosRoboticsGroup/DeFi\n\n**7. Hi-WM (arXiv 2604.21741) - April 2026**\n- **Full Title:** Hi-WM: Human-in-the-World-Model for Scalable Robot Post-Training\n- **Approach:** Post-training framework using learned world models as corrective substrate for failure-targeted policy improvement\n- **Relevance:** Human-corrective world model refinement for humanoid control\n- **Source:** https://arxiv.org/html/2604.21741v1\n\n**8. UniMorphGrasp (arXiv 2602.00915) - URDF-Aware Diffusion**\n- **Full Title:** UniMorphGrasp: Diffusion Model with Morphology-Awareness for Cross-Embodiment Dexterous Grasp Generation\n- **Key Feature:** Encodes hand kinematics from URDF as graph-based features to guide denoising\n- **Relevance:** Direct precedent for URDF-based kinematic conditioning in diffusion models\n- **Source:** https://arxiv.org/html/2602.00915\n\n**9. X-Humanoid (arXiv 2512.04537) - Humanoid Video Synthesis**\n- **Publication Date:** December 2025\n- **Approach:** Adapts Wan 2.2 diffusion transformer to human-to-humanoid video conversion\n- **Relevance:** Direct humanoid video synthesis without explicit kinematic conditioning\n- **Source:** https://arxiv.org/html/2512.04537v1\n\n**10. FlowAct-R1 (arXiv 2601.10103) - Real-time Interactive Humanoid**\n- **Full Title:** FlowAct-R1: Towards Interactive Humanoid Video Generation\n- **Architecture:** MMDiT for streaming humanoid video synthesis\n- **Relevance:** Low-latency humanoid-specific video generation framework\n- **Source:** https://arxiv.org/html/2601.10103v1\n\n---\n\n### LANDSCAPE ANALYSIS: TRENDS & GAPS\n\n#### 1. **Kinematic Conditioning Approaches (2025-2026)**\n- **BridgeV2W:** URDF-rendered masks via ControlNet\n- **EA-WM:** Structured kinematic-to-visual action fields  \n- **Kimodo:** Text + kinematic constraints (keyframes, joint positions)\n- **G-DReaM:** Graph-based kinematic structure encoding\n- **UniMorphGrasp:** URDF as graph-based feature guidance\n\n**Gap Analysis:** Most approaches render kinematics spatially (masks/heatmaps) or encode them in latent space (graphs/fields). Few combine both spatial rendering AND latent structural encoding simultaneously like URDF-DiT appears to propose.\n\n#### 2. **URDF Usage Patterns**\n- **Dream2Act:** Post-hoc IK with URDF for trajectory validation\n- **BridgeV2W:** URDF rendering for embodiment masks\n- **Kinema4D:** URDF kinematics for 4D trajectory generation\n- **UniMorphGrasp:** URDF parsing for morphology encoding\n\n**Gap Analysis:** URDF is primarily used for either post-hoc constraint satisfaction or mask rendering. Using URDF FK heatmaps as explicit conditioning during diffusion denoising appears less explored.\n\n#### 3. **IDM Action Extraction (2025-2026)**\n- **MotuBrain:** Unified model with explicit IDM head\n- **VAG:** Joint video-action generation without sequential IDM\n- **DreamGen:** IDM diffusion transformers for action extraction\n- **TC-IDM:** Tool-centric IDM for executability\n- **DeFI:** Decoupled forward-inverse dynamics models\n\n**Gap Analysis:** IDM extraction exists but is typically post-hoc or requires task-specific training. Fully end-to-end IDM-aware diffusion during video generation training is less established for humanoids.\n\n#### 4. **Humanoid-Specific Contributions (Feb-May 2026)**\n- **HumanX:** 8x better generalization, zero-shot transfer\n- **Dream2Act:** Whole-body contact-aware synthesis\n- **EA-WM:** Event-aware kinematic-visual alignment\n- **Humanoid World Models:** Egocentric video with control tokens\n\n**Gap Analysis:** Recent work increasingly focuses on full-body control and contact dynamics. URDF-DiT's combination of full-body kinematic conditioning + FK heatmaps + IDM-aware training appears novel.\n\n#### 5. **Complete Architecture Innovations (April-May 2026)**\n- **MotuBrain:** Three-stream Mixture-of-Experts with unified action representation\n- **VAG:** Flow-matching dual-stream for simultaneous video-action generation\n- **EA-WM:** Structured kinematic fields as intermediate representation\n\n**Gap Analysis:** The field is moving toward explicit kinematic structure integration rather than implicit conditioning.\n\n---\n\n### CRITICAL CONCURRENT WORK ALERT FOR CORL 2026 SUBMISSION\n\n**HIGH PRIORITY PAPERS TO CITE:**\n1. **BridgeV2W** (2602.03793) - Direct URDF conditioning precedent\n2. **EA-WM** (2605.06192) - Just published May 7, 2026; kinematic-visual coupling\n3. **Kimodo** (2603.15546) - Kinematic motion diffusion baseline\n4. **Dream2Act** (2603.19709) - URDF IK post-processing pipeline\n5. **MotuBrain** (2604.27792) - State-of-art world action model\n6. **DreamGen** (2505.12705) - IDM-based action recovery from video\n\n**NOVELTY CLAIMS TO VERIFY:**\n- If URDF-DiT claims to use FK heatmaps as conditioning: Check if Kimodo, BridgeV2W, or other 2026 papers already explore this\n- If URDF-DiT claims joint optimization of video+action with kinematic constraints: Compare to VAG and MotuBrain architectures\n- If URDF-DiT claims full-body humanoid support: Compare to HumanX, Dream2Act, Humanoid World Models, and EA-WM on this dimension\n\n**POTENTIAL LANDSCAPE GAPS THAT URDF-DiT MIGHT ADDRESS:**\n1. Explicit URDF FK heatmap rendering during diffusion conditioning (vs. post-hoc or implicit)\n2. End-to-end kinematic consistency enforcement throughout denoising\n3. Joint full-body humanoid + IDM + kinematic structure optimization\n4. Scalability to diverse humanoid morphologies with unified kinematic conditioning\n\n---\n\n### SOURCES\n\n- [Dream2Act: Morphology-Consistent Humanoid Interaction](https://arxiv.org/html/2603.19709v1)\n- [BridgeV2W: Bridging Video Generation Models](https://arxiv.org/abs/2602.03793)\n- [EA-WM: Event-Aware Generative World Model](https://arxiv.org/html/2605.06192v1)\n- [HumanX: Agile Humanoid Skills from Videos](https://arxiv.org/html/2602.02473)\n- [Kinema4D: Kinematic 4D World Modeling](https://arxiv.org/html/2603.16669v1)\n- [MotuBrain: Advanced World Action Model](https://arxiv.org/html/2604.27792v2)\n- [VAG: Dual-Stream Video-Action Generation](https://arxiv.org/html/2604.09330)\n- [Kimodo: Scaling Controllable Human Motion](https://arxiv.org/html/2603.15546v1)\n- [G-DReaM: Graph-conditioned Diffusion Retargeting](https://arxiv.org/html/2505.20857v1)\n- [DreamGen: Unlocking Generalization in Robot Learning](https://arxiv.org/html/2505.12705v1)\n- [TC-IDM: Grounding Video Generation for Executable Robot Motion](https://arxiv.org/html/2601.18323v1)\n- [DeFI: Disentangled Robot Learning via Separate Dynamics](https://github.com/LogosRoboticsGroup/DeFI)\n- [Hi-WM: Human-in-the-World-Model](https://arxiv.org/html/2604.21741v1)\n- [UniMorphGrasp: Morphology-Aware Grasp Generation](https://arxiv.org/html/2602.00915)\n- [X-Humanoid: Robotize Human Videos](https://arxiv.org/html/2512.04537v1)\n- [FlowAct-R1: Interactive Humanoid Video Generation](https://arxiv.org/html/2601.10103v1)\n- [Humanoid World Models: Open Foundation Models](https://arxiv.org/abs/2506.01182)\n- [Differentiable Robot Rendering](https://arxiv.org/html/2410.13851v1)\n- [URDFormer: Constructing Simulation Environments](https://arxiv.org/html/2405.11656v2)\n- [X-Diffusion: Cross-Embodiment Diffusion Policies](https://arxiv.org/html/2511.04671v2)\n- [Controllable Complex Human Motion via Text-to-Skeleton](https://arxiv.org/html/2603.08028)\n- [World Action Models are Zero-shot Policies](https://arxiv.org/html/2602.15922v1)\n- [Unified 4D World Action Modeling](https://arxiv.org/html/2604.26694v2)\n- [A Comprehensive Survey on World Models for Embodied AI](https://arxiv.org/html/2510.16732v1)"
      }
    ],
    "totalDurationMs": 90457,
    "totalTokens": 40387,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 903,
      "cache_creation_input_tokens": 2139,
      "cache_read_input_tokens": 32421,
      "output_tokens": 4924,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2139
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 903,
          "output_tokens": 4924,
          "cache_read_input_tokens": 32421,
          "cache_creation_input_tokens": 2139,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2139,
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
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "346b569b-2851-427d-860c-906ef463d80e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9",
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
  "leafUuid": "bbc7df6d-4b7a-4490-9c80-c2cb43080596",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "URDF-DiT: Full-body kinematic conditioning for humanoid IDM training data",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9"
}
```

---

### Assistant

_source line 17 · 2026-05-10T13:59:18.225Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have extensive research results. Let me analyze the current Round 9 idea against these findings.

Key findings from my research:

1. **All cited papers verified**: Dream2Act, BridgeV2W, EA-WM, HumanX, Kinema4D, MotuBrain, VAG are all real papers with the claimed properties.

2. **New potentially missing work**:
   - **OmniRetarget** (arXiv:2509.26633) - September 2025 paper on humanoid loco-manipulation data generation. 

OmniRetarget might be a retargeting-based approach that falls outside the proposal's scope. I'm also finding several other relevant papers like MITTY, a diffusion-based human-to-robot video generation method, and Psi-Zero, a humanoid foundation model for loco-manipulation. Seer appears to already be covered as part of the GR00T family, and I'm verifying whether Kimodo and GR00T N1 are already included in the landscape.

I'm also tracking some additional work like TC-IDM for tool-centric inverse dynamics, DeFI for decoupled forward-inverse dynamics, and Hi-WM as a human-in-world-model approach. Looking at the concurrent work status, I can see that several key papers have now been properly cited—BridgeV2W, EA-WM, HumanX, MotuBrain, and VAG all have citations in place, with VAG properly attributed to the Limitations section.

Now I'm checking what might still be missing from the literature coverage. Psi-Zero looks potentially relevant since it addresses humanoid loco-manipulation with training data generation and co-training on human and humanoid data, which could connect to the work here. TC-IDM also seems worth considering for its tool-centric approach to inverse dynamics executability, and I should verify whether OmniRetarget needs to be included as well.

Looking at OmniRetarget though—the user was explicit that retargeting falls outside the scope, and this appears to be a retargeting-focused approach from September 2025, so it probably doesn't belong in the discussion. For Humanoid World Models, there's some confusion around the dating—the arXiv agent flagged it as June 2025 but also mentioned May 2026, which doesn't quite add up. If it's actually from June 2025, it would predate much of the current landscape, though it might still be relevant if it covers open-source humanoid world models with control tokens.

I've confirmed BridgeV2W is properly cited and differentiated now, so that's resolved.

Now I'm checking what else might be missing from the landscape. Psi-Zero from March 2026 looks like it could be relevant since it addresses humanoid loco-manipulation and potentially includes data generation components, so I should evaluate whether that needs to be included.

Omni-Retarget from September 2025 is in the same application space but uses retargeting, which the user explicitly said is out of scope—and since URDF-DiT's contribution is specifically the video-diffusion to IDM pathway rather than retargeting, this probably just warrants a brief mention.

TC-IDM from January 2026 addresses IDM-based executability for video generation, which could be relevant and might need citing. I should also check whether the Humanoid World Models paper from 2025 needs to be included in the comparison.

Now I'm evaluating the novelty of URDF-DiT itself. The core contributions are extending the ControlNet+URDF+video-diffusion approach from arm robots to full-body humanoid tasks with 29 degrees of freedom, validating it through downstream IDM policy success rather than just video quality metrics, using continuous Gaussian FK heatmaps instead of binary masks, and keeping the ControlNet backbone frozen rather than fine-tuning it jointly. It's a solid incremental advance over BridgeV2W and EA-WM, with the full-body extension being the main contribution, though it does rely heavily on those prior works.

The feasibility looks reasonable—19 days to CoRL with 8+ H100s is tight but achievable, the compute budget of ~130 hours is within the 200-hour limit, and the main risks are the IDM domain gap and ControlNet convergence. The pivot criteria at day 14 gives a clear decision point.

The proposal itself is well-structured and clear, with precise descriptions of the Dream2Act components and explicit tradeoffs flagged. Impact-wise, the humanoid data scaling angle is interesting but depends on whether the approach actually generalizes beyond the specific task setup.

Now I'm noticing some potential gaps in the related work—there's Psi-Zero from March 2026 that directly tackles humanoid loco-manipulation with co-training on human and humanoid data, which a CoRL reviewer in this space would likely know about. There's also OmniRetarget from September 2025 focused on interaction-preserving data generation for humanoid whole-body loco-manipulation that seems relevant to the core contribution.

TC-IDM from January 2026 addresses the IDM executability problem through tool-centric video generation and probably warrants a citation. The strategy here is that if the ablation results fall short—specifically if Ablation B shows less than 3 percentage points improvement while Ablation A shows 5 or more—there's a contingency plan to reframe the paper's positioning.

The core question becomes whether Ablation A alone can carry a CoRL-level contribution: in-loop FK conditioning outperforming post-hoc URDF-IK for IDM data quality is genuinely novel since neither BridgeV2W nor EA-WM test this comparison directly. The catch is that validating this requires implementing a vanilla baseline with post-hoc URDF-IK, which essentially duplicates part of Dream2Act's work. Whether reviewers find that compelling as a standalone contribution is uncertain.

Looking at the broader novelty landscape, with both BridgeV2W and EA-WM now establishing ControlNet plus URDF conditioning for arm robots, the question is what truly differentiates URDF-DiT's core contribution.

The full-body humanoid extension becomes the key differentiator, but only if Ablation B shows strong gains of at least 5 percentage points. That's the threshold determining whether this extension justifies a CoRL submission.

Stepping back, the proposal has addressed nearly everything across these rounds: all concurrent papers are now properly cited, the Dream2Act comparison is precise, the ablation structure is sound with clear in-loop versus post-hoc and full-body versus end-effector comparisons, pivot criteria have concrete numbers, and the user tradeoff is flagged upfront. The remaining gap is Psi-Zero, a March 2026 humanoid loco-manipulation paper that's still missing from the related work.

I'm weighing whether to pass or request another revision. The core technical claims hold up, the differentiations are clear, and the ablation design is solid—these were the critical issues that needed fixing. The uncited papers like Psi-Zero, TC-IDM, and OmniRetarget are relatively peripheral to the main contribution, so the novelty claim remains defensible even without them.

The real decision hinges on two factors: whether Ablation B demonstrates sufficient novelty for CoRL's bar when combined with BridgeV2W and EA-WM's prior work on ControlNet+URDF conditioning, and whether the user requirement criteria are sufficiently defined to handle edge cases. Both of these are now addressed well enough that the remaining gaps are presentation-level rather than fundamental flaws. At Round 9 of 10, I think this is ready to pass.

Looking at the scoring: novelty sits at 3.5 given the incremental but genuine extension to full-body humanoids contingent on Ablation B results, feasibility is 3.5 with the aggressive timeline and IDM domain gap as real risks, clarity is strong at 4.5 for the organization and detail, and impact is 3.5 since the humanoid data contribution is meaningful but still incremental. That averages to 3.875 overall.

The score falls short of the 4.0 threshold, but I'm reconsidering whether these assessments are too conservative—the work genuinely tackles an important problem, the feasibility concerns are more about the CoRL deadline crunch than the idea's viability, and the novelty is legitimate if Ablation B validates the approach. The core mechanism extending ControlNet and URDF FK heatmaps to full-body humanoids with the IDM pipeline is real progress, even if it builds on established foundations. The full-body humanoid extension is genuinely novel—conditioning on 29 DoF with leg kinematics and whole-body contact is qualitatively different from prior arm-only work, so I'd bump novelty to 3.5-4. Feasibility is tight with the 19-day deadline and 8+ H100s, but the contingency plans bring it to 3.5. Now I'm checking for relevant papers I might have missed—Psi-Zero looks relevant for humanoid loco-manipulation training data, and I'm looking at what TC-IDM contributes to the landscape. I'm reconsidering whether "pass" is actually justified here. The core novelty comes down to applying existing methods (BridgeV2W and EA-WM) to full-body humanoid control with some pipeline modifications—the IDM integration and in-loop versus post-hoc ablation are genuinely new, but for a top-tier robotics venue like CoRL, I need to assess whether extending to 29 DoF and freezing the ControlNet backbone constitute sufficient novelty on their own. established architecture (ControlNet + URDF conditioning) to a new domain (full-body humanoid) and adds a downstream evaluation pipeline (IDM). This is the classic "application/extension" paper pattern.

The question is: is this enough for CoRL?

Looking at CoRL's scope: "The Conference on Robot Learning (CoRL) focuses on the intersection of robotics and machine learning." Papers at CoRL often include:
1. New algorithms with strong empirical evaluation
2. New benchmarks/datasets
3. System papers with clear contributions

URDF-DiT fits category 1/3: it's a new system with:
- Architectural contribution (FK heatmap conditioning for full-body humanoid)
- Empirical validation (Ablation B: full-body vs. end-effector)
- Practical contribution (IDM pipeline for synthetic humanoid training data)

At CoRL, this would likely be accepted if the ablation studies demonstrate meaningful improvements, the downstream policy training shows clear benefits, and the comparison against Dream2Act highlights the advantages of in-loop versus post-hoc conditioning. Given the well-defined pivot criteria and sound technical approach, I think this warrants a pass. The missing citations like Psi-Zero and TC-IDM are gaps I should flag, but they're unlikely to undermine the core contribution. My scoring leans toward novelty and feasibility at 3.5 each—real but incremental progress with an aggressive but achievable timeline—while clarity is strong at 4.5 and impact sits at 4.0.

The average comes to 3.875, which falls short of the 4.0 threshold for a pass, so my verdict should be revise. But since this is Round 9 of 10 and Round 10 forces a final decision between pass or fail, I have one more opportunity to push this toward acceptance. The remaining issues—missing citations and the unresolved user requirement tradeoff around CoRL benchmark coverage—are all addressable with targeted revisions.

I'm reconsidering whether Psi-Zero, TC-IDM, and OmniRetarget are truly critical enough to warrant another round. Psi-Zero seems directly relevant since it addresses humanoid loco-manipulation with synthetic data generation, which touches on the core proposal's data scarcity problem.

TC-IDM is related to the IDM pipeline but targets arm robots rather than full-body humanoid kinematics, so the differentiation is fairly clear. OmniRetarget is another retargeting approach for humanoid data, but given that URDF-DiT's kinematic consistency angle is distinct, these gaps feel more like completeness issues than fundamental oversights that would sink the paper.

The real question is whether these minor citation gaps warrant a "revise" verdict or if the core contributions are strong enough to pass. At CoRL, missing Psi-Zero could get flagged by reviewers in the humanoid loco-manipulation space, but it's borderline whether that tips into major revision territory.

I think I should also double-check if there are any deeper issues lurking beneath the surface—I've already verified the VAG quote and Dream2Act descriptions are accurate, so those are solid.

Now I'm going through the remaining technical claims: the EA-WM title correction, the resource estimate staying within budget, the pivot criteria being concrete, the user tradeoff being flagged, the FK residual loss framing, and the IDM domain gap mitigation all check out. So the only real gaps left are the three missing citations, the optional title framing question, and the unresolved user requirement decision.

Actually, let me reconsider the novelty angle here. The core of what URDF-DiT does is take the ControlNet+URDF FK heatmap approach that worked for arm robots in prior work and scale it to full-body humanoid control with 29 degrees of freedom, plus add an explicit IDM training pipeline and validate everything through downstream policy performance. That's genuinely novel because no one's done this specific combination for full-body humanoids before, and the IDM pipeline is a practical contribution that the prior work didn't provide.

The ablations are clean and testable, so while the incremental label fits—since the core mechanism is established—the extension to this harder domain with the IDM pipeline is a real contribution. For a venue like CoRL that cares about practical systems and solid empirical validation, this kind of novelty is usually enough for acceptance if the experiments hold up. I'm settling on novelty at 3.5 since it's incremental but genuine, feasibility at 3.5 given the aggressive scope but solid planning, clarity at 4.5, and impact at 4.0 for tackling a high-impact problem with practical value.

That puts the average at 3.875, below the 4.0 threshold, so the verdict is revise. The fixes are straightforward—add the Psi-Zero citation, consider TC-IDM, and maybe OmniRetarget if it's relevant—all doable in one round.

But let me reconsider whether I'm being too strict on novelty. CoRL papers typically fall into systems work with strong ablations showing meaningful improvements, method papers that extend existing techniques to challenging new domains, or benchmark papers with thorough evaluation. URDF-DiT fits squarely in that second category, and with proper ablations it should be competitive.

The submission really hinges on whether the experimental results deliver: if Ablation B shows at least a 5 percentage point improvement from full-body conditioning, the absolute performance hits 20% or better on Isaac Lab, and the comparison against the post-hoc baseline is convincing, then this becomes a solid CoRL paper. Those are concrete, testable conditions with clear success metrics already outlined in the proposal.

I'm sticking with revise, but the path forward is clear—incorporate those three citations with the specific focus on Psi-Zero as the key addition to the related work landscape.

Actually, let me reconsider the OmniRetarget situation. It's from September 2025 and directly addresses humanoid whole-body loco-manipulation through interaction-preserving generation, which is exactly the application space here. Even though it's retargeting-based, a CoRL reviewer might flag it as a competing approach. But the user was explicit: action retargeting innovations are out of scope, and existing retargeters should be treated as black-box tools. If OmniRetarget is fundamentally a retargeting method, it falls outside the scope boundary they set.

That said, I should still cite it with a brief one-liner distinguishing URDF-DiT's FK-conditioned video synthesis approach from OmniRetarget's interaction-preserving retargeting strategy, since they're both generating humanoid loco-manipulation training data.

For Psi-Zero, I'm less certain about what it actually does. The title mentions co-training on human and humanoid data, but that could mean policy co-training, retargeting, or something else entirely—not necessarily video synthesis. Given this uncertainty, I should be more cautious about how prominently I treat it.

TC-IDM from January 2026 is more straightforward—it's directly about IDM for robot video generation, so that's worth flagging as a medium-priority citation.

My final verdict is "revise" with these citation gaps noted as minor issues that need one more targeted pass. I'm weighing whether to push for one more revision given this is Round 9 of 10. The missing citations are genuinely relevant for peer review and straightforward to add, so I'll recommend revision one final time to give the generator that last opportunity before the mandatory pass/fail decision.

The scores across novelty, feasibility, clarity, and impact average to 3.875, which supports the revise recommendation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbc7df6d-4b7a-4490-9c80-c2cb43080596",
  "isSidechain": false,
  "requestId": "req_011Cau1FA9XGnv2V1iWUz8G4",
  "type": "assistant",
  "uuid": "cb1070e0-2ca5-4686-a436-9664ddb21f1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L6bjr6ev9aE19TQWjRwBzx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2597,
      "cache_creation_input_tokens": 7071,
      "cache_read_input_tokens": 46785,
      "output_tokens": 9884,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2597,
          "output_tokens": 9884,
          "cache_read_input_tokens": 46785,
          "cache_creation_input_tokens": 7071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7071
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

_source line 18 · 2026-05-10T13:59:41.380Z_

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3.5,
      "rationale": "The core ControlNet+URDF+video-DiT mechanism is now established by BridgeV2W (Feb 2026) and EA-WM (May 2026); URDF-DiT's novelty is the extension to full-body humanoid 29-DoF and the IDM→policy pipeline, which is real but incremental — its scientific weight depends entirely on Ablation B showing ≥5pp improvement from full-body vs. end-effector conditioning."
    },
    "feasibility": {
      "score": 3.5,
      "rationale": "The 19-day auto-research CoRL plan with 8+ H100s and ~130h total compute is within budget and has well-defined Day 14 pivot criteria, but the IDM sim→video domain gap and ControlNet convergence uncertainty remain genuine execution risks with a 60-70% stated success probability."
    },
    "clarity": {
      "score": 4.5,
      "rationale": "The proposal is exceptionally well-organized: Dream2Act two-component decomposition is precise and independently verified, all differentiation axes vs. BridgeV2W/EA-WM/VAG/HumanX/Kinema4D are clearly articulated, pivot criteria have concrete numeric thresholds, and the user tradeoff is prominently flagged throughout."
    },
    "impact": {
      "score": 4.0,
      "rationale": "Humanoid data scarcity is independently confirmed as the #1 bottleneck in 2026 humanoid papers; URDF-DiT's IDM pipeline directly addresses it for whole-body contact tasks, and the ablation design (in-loop vs. post-hoc, full-body vs. end-effector) would produce practically actionable findings even if results are mixed."
    }
  },
  "issues": [
    "MISSING CITATION — OmniRetarget (arXiv:2509.26633, September 2025): 'Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation' directly targets the same application space (generating synthetic training data for humanoid whole-body loco-manipulation tasks) and is a September 2025 paper a CoRL 2026 reviewer in this space would know. While retargeting-based (hence outside URDF-DiT's contribution scope), it must appear in the landscape with a one-line differentiation: 'OmniRetarget generates humanoid loco-manipulation data via interaction-preserving retargeting from human motion; URDF-DiT generates data via FK-conditioned video synthesis without retargeting, specifically targeting the video-diffusion → IDM pathway.'",
    "MISSING CITATION — TC-IDM (arXiv:2601.18323, January 2026): 'TC-IDM: Grounding Video Generation for Executable Zero-shot Robot Motion' addresses IDM-based executability for video generation for robot control — directly in URDF-DiT's problem space. A reviewer working on IDM+video generation for robots would flag its absence. Add a one-line differentiation: 'TC-IDM enforces tool-centric IDM executability (end-effector stability) for arm-manipulation video generation; URDF-DiT enforces hard geometric URDF FK constraints throughout denoising for full-body humanoid 29-DoF whole-body contact tasks.'",
    "MISSING CITATION — Psi-Zero (arXiv:2603.12263, March 2026): 'An Open Foundation Model Towards Universal Humanoid Loco-Manipulation' directly targets humanoid loco-manipulation capability with co-training on human and humanoid data, overlapping with URDF-DiT's application space. A CoRL 2026 reviewer on humanoid loco-manipulation would likely be familiar with this work and flag its absence.",
    "CORL EVALUATION SCOPE — USER DECISION UNRESOLVED (persistent from Round 5): The CoRL submission covers only 1 of 3 user-required evaluation benchmarks (Isaac Lab G1 locomanipulation; HumanoidBench and RoboCasa365 deferred to ICLR 2027). This is correctly and prominently flagged throughout the proposal, but the user has not yet confirmed option A (CoRL now + ICLR 2027 full coverage) vs. option B (skip CoRL, target ICLR 2027 from start). This decision is blocking — without user opt-in, the CoRL trajectory remains provisional."
  ],
  "feedback": "All critical issues from Rounds 1–8 are resolved. BridgeV2W, EA-WM, HumanX, MotuBrain, VAG (with Limitations section attribution), Dream2Act (two-component decomposition), Kinema4D (expanded differentiation), and EVA are all properly cited and differentiated. The FK residual loss is precisely framed. Pivot criteria have concrete thresholds. User tradeoff is prominently flagged. Three targeted additions remain for Round 10 pass:\n\n1. **Add OmniRetarget (arXiv:2509.26633, Sept 2025)**: One-line landscape entry noting it generates humanoid loco-manipulation training data via interaction-preserving retargeting — retargeting-based approach, out of URDF-DiT's contribution scope, but competes in the application space.\n\n2. **Add TC-IDM (arXiv:2601.18323, Jan 2026)**: One-line landscape entry noting it addresses IDM executability for video generation via tool-centric end-effector focus for arm robots — differentiate as arm-robot executability via soft IDM reward vs. URDF-DiT's hard geometric FK constraint at every denoising step for full-body humanoid 29 DoF.\n\n3. **Add or acknowledge Psi-Zero (arXiv:2603.12263, March 2026)**: One-line reference noting it targets universal humanoid loco-manipulation via co-training on human and humanoid data — differentiate as a policy learning/data co-training approach rather than the video-diffusion → IDM pathway URDF-DiT contributes to.\n\n4. **Seek explicit user confirmation** on CoRL vs. ICLR 2027 pathway given the 1-of-3 benchmark coverage constraint — this is the one remaining unresolved user requirement issue.\n\nWith these additions, the paper will have comprehensive coverage of the competing landscape for CoRL 2026 peer review.",
  "reason": "All critical issues from prior rounds are resolved; three minor missing citations (OmniRetarget, TC-IDM, Psi-Zero) from the 2025-2026 humanoid data generation landscape remain, plus the user opt-in decision on CoRL vs. ICLR 2027 scope."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb1070e0-2ca5-4686-a436-9664ddb21f1c",
  "isSidechain": false,
  "requestId": "req_011Cau1FA9XGnv2V1iWUz8G4",
  "type": "assistant",
  "uuid": "ebd9995b-606a-4e69-afde-63068979cd2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01L6bjr6ev9aE19TQWjRwBzx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2597,
      "cache_creation_input_tokens": 7071,
      "cache_read_input_tokens": 46785,
      "output_tokens": 9884,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2597,
          "output_tokens": 9884,
          "cache_read_input_tokens": 46785,
          "cache_creation_input_tokens": 7071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7071
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ebd9995b-606a-4e69-afde-63068979cd2f",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "URDF-DiT: Full-body kinematic conditioning for humanoid IDM training data",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ebd9995b-606a-4e69-afde-63068979cd2f",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "URDF-DiT: Full-body kinematic conditioning for humanoid IDM training data",
  "sessionId": "db3aeea3-bff8-4e0d-8d26-b79997933bd9"
}
```

---
