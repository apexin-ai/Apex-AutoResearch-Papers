# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/99d62b10-815d-4248-b519-008464906ca6.jsonl`
- **Structured JSON:** [`585a6417a17289f587e8.json`](../../sessions/58/585a6417a17289f587e8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T13:01:57.223Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T13:01:57.223Z",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\n\nDirection: Generative models specifically targeting HUMANOID robot training data — addressing the high-DoF, whole-body, loco-manipulation data scarcity that bottlenecks humanoid VLA / WM training. SCOPE LIMITED TO TWO CONTRIBUTION TYPES:\n  (a) Generation ALGORITHMS — e.g., video diffusion conditioned on humanoid action streams, action-conditioned generative models, latent humanoid trajectory generators, physics-aware whole-body video generation.\n  (b) Procedural data-generation PIPELINES — e.g., MimicGen-style automated demo multiplication for humanoids, procedural whole-body task/scene generation, automated quality filtering pipelines for synthetic humanoid trajectories.\n\nOUT OF SCOPE: action retargeting innovations (human-video → humanoid-action retargeting). Treat existing retargeters (HumanPlus, OmniH2O) as black-box upstream tools if needed; do NOT propose new retargeting methods.\n\nRecent landscape (do not duplicate): NVIDIA GR00T-Dreams, DexMimicGen, MimicGen extensions for humanoid, Helix self-supervised humanoid pipelines, Cosmos for synthetic humanoid video. Humanoid data scarcity is the #1 bottleneck cited in 2026 humanoid papers — high impact area.\n\nContribution type: METHOD ONLY. New generation algorithm OR new procedural pipeline. Not a new released humanoid dataset alone.\n\nSIM-ONLY MITIGATION: Validate generated data by training a downstream humanoid policy/VLA in sim and comparing against models trained on baseline data. Frame contribution as method, not dataset.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Strategies: (a) fine-tune existing video diffusion (CogVideoX, OpenSora, Cosmos) with humanoid-action conditioning, (b) procedural pipeline that requires negligible training compute, (c) small efficient humanoid-specific generator that beats general baselines.\n2. Time: ≤20 days. Build on HF Diffusers, OpenSora, NVIDIA Cosmos repos, Isaac Lab humanoid suite (G1, H1), MimicGen, RoboCasa with humanoid embodiments if available.\n3. Eval: train humanoid policy/VLA on generated vs baseline data. Test on Isaac Lab humanoid manipulation/locomanipulation tasks, RoboCasa kitchen with humanoid embodiment, HumanoidBench. Report success rate + data efficiency curves.\n\nLook for: physics-aware whole-body video generation with kinematic consistency, action-conditioned generators that exploit humanoid kinematic structure, procedural pipelines that produce diverse loco-manipulation (not just static manipulation) data, automatic quality filtering for synthetic humanoid trajectories. Avoid: any retargeting-based contribution, arm-only generation rebadged as humanoid, naive fine-tuning of video diffusion on humanoid clips without method.\n\nTag: direction=humanoid_data_gen, contribution_type=method. target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 7/10)\n{\n  \"title\": \"LocoMimicGen: Coupled SE(3) Object-Centric Demo Multiplication for Mobile Humanoid Loco-Manipulation\",\n  \"core_problem\": \"How can a handful of expensive teleoperated whole-body loco-manipulation demonstrations be multiplied by orders of magnitude across diverse spatial configurations — new object positions, table heights, room obstacle layouts — while maintaining physical validity for the mobile bipedal humanoid platform? Isaac Lab's 2.3 GA release contains three directly relevant prior contributions. PR #3150 (merged Sept 9, 2025) adds the G1 loco-manipulation environment integrating a pretrained RL locomotion policy with Pink IK arm control. PR #3259 ('Adds locomanipulation data generation via disjoint navigation', merged Sept 10, 2025) adds pick-navigate-place phase segmentation with occupancy-map path planning between phases and scene randomization of tabletop positions, navigation destinations, and floor obstacles — making it the closest structural predecessor to LocoMimicGen. PR #3992 (merged Dec 1, 2025) extends the Mimic framework with a 'body end-effector' API and navigation controller integration. Despite this infrastructure, three technical gaps prevent room-level combinatorial scaling: PR #3259 handles navigation 'disjointly' — the manipulation stance (where the robot stands to manipulate) is fixed from the source demo and navigation is handled as path-level occupancy-map planning between fixed phases, NOT as coupled SE(3) object-centric encoding of stances jointly with arm trajectories. None of these PRs enforce arm-reachability constraints on base-pose selection during retargeting — the robot manipulates from whatever stance the source demo used, regardless of arm workspace feasibility for new object positions. And none perform combinatorial composition of subtask segments from multiple source demonstrations. These three absences cap achievable diversity at object-position randomization within a single source demo's reach envelope, rather than the combinatorial room-level scaling that MimicGen achieves for tabletop tasks.\",\n  \"opportunity\": \"Isaac Lab's 2.3 GA release (PRs #3150, #3259, #3992) now provides the exact scaffolding — G1 environment, pick-navigate-place phase segmentation, occupancy-map path planning, Mimic segmentation framework, and navigation controller integration — needed to build a principled extension. The precise technical gap is narrow but high-impact: adding (1) SE(3) object-centric encoding of navigation stances jointly with arm trajectories into the existing Mimic segment representation (replacing the disjoint path-planning approach of PR #3259 with coupled frame-transform retargeting), (2) stance-conditioned reachability-map-guided base-pose optimization enforcing arm feasibility at each manipulation stance during retargeting (adapting IRM methodology from the mobile-manipulator literature to the bipedal humanoid setting, where the reachability map is conditioned on whole-body configuration rather than just SE(2) base pose), and (3) combinatorial subtask segment composition from multiple source demonstrations. OmniRetarget (Amazon, Sept 2025) addresses humanoid loco-manipulation data generation from MoCap sequences via interaction-mesh Laplacian deformation on the G1, but retargets continuous motion sequences and cannot combinatorially compose segments across scene variants. DemoHLM (Oct 2025) demonstrates generalizable single-demonstration adaptation across 10 G1 loco-manipulation household tasks but the single-demo paradigm limits scaling to spatial interpolation within one source demo's envelope. The three-part Isaac Lab Mimic extension proposed here is tractable within existing infrastructure, precisely bounded against Isaac Lab's own 2.3 baseline (including PR #3259 as the most direct predecessor), and is the missing ingredient for room-level combinatorial scaling. MoMaGen (ICLR 2026, arXiv:2510.18316) imposes reachability as a hard constraint for wheeled bimanual mobile base-pose sampling — SE(2) for a wheeled platform. Now peer-reviewed at ICLR 2026, MoMaGen's coverage of hard-reachability-constrained demo generation makes the bipedal differentiation the critical point of departure: MoMaGen's reachability constraint operates over SE(2) base pose for a wheeled bimanual platform where the base pose fully determines arm workspace, whereas LocoMimicGen's stance-conditioned IRM addresses the qualitatively harder bipedal case where arm reachability is conditioned on whole-body configuration — COM height, foot contact, balance state — a higher-dimensional reachability function not covered by any prior data-generation work. EgoHumanoid (OpenDriveLab, arXiv:2602.10106, Feb 2026) represents a concurrent complementary paradigm — co-training VLA policies on human egocentric video alongside robot demonstrations — that highlights the orthogonal value of LocoMimicGen's combinatorial simulation synthesis approach.\",\n  \"landscape\": \"MimicGen (CoRL 2023) decomposes arm demonstrations into object-centric subtask segments and applies SE(3) frame transformations — manipulation-only. DexMimicGen (ICRA 2025) extends this to bimanual dexterous humanoids, still tabletop. HumanoidGen (NeurIPS 2025) uses LLM-driven planning for tabletop dexterous tasks with 120+ scene variants — explicitly excludes locomotion.\\n\\nIsaac Lab 2.3 loco-manipulation infrastructure comprises three PRs that together form the primary baseline. PR #3150 (merged Sept 9, 2025) adds Isaac-PickPlace-Locomanipulation-G1-Abs-v0, integrating a pretrained RL locomotion policy (velocity commands vx, vy, wz) with Pink IK arm control, achieving 92% success on pick-and-place. PR #3259 ('Adds locomanipulation data generation via disjoint navigation', merged Sept 10, 2025, release/2.3.0) is the closest structural predecessor to LocoMimicGen: it adds pick-navigate-place phase segmentation, occupancy-map-based collision-free path planning between phases, and scene randomization of tabletop object positions, navigation destinations, and floor obstacles. The implementation lives under disjoint_navigation/ and works by (a) recording static manipulation teleoperation with the base stationary, (b) applying Mimic augmentation to manipulation segments, and (c) stitching path-planned navigation trajectories between the resulting phases. Critically, PR #3259 does NOT encode navigation stances in the object's SE(3) local frame — navigation is occupancy-map path planning at the trajectory level, while the manipulation stance (where the robot stands to manipulate) is fixed from the source demo, not retargeted to new object positions. There is no arm-reachability constraint on base-pose selection: if a new object position falls outside the arm workspace at the source demo's stance, the generation produces infeasible trajectories rather than finding a feasible stance. There is no combinatorial composition from multiple source demonstrations. PR #3992 (merged Dec 1, 2025) adds a 'body end-effector' API and get_navigation_state() integration into the Mimic framework but relies on the same state-based navigation repetition/skipping, not object-centric stance encoding.\\n\\nInverse reachability maps (IRM) for robot base placement are a well-established technique. Vahrenkamp et al. 2013 introduced IRM for robot placement by inverting precomputed reachability maps to generate SE(2) distributions of feasible base poses. Burget et al. (ICRA 2015) applied IRM specifically to humanoid stance selection for grasping tasks — but in a static grasping context where balance is assumed, not within a data-generation retargeting loop. MoMa-Pos (arXiv:2403.19940, Oct 2024 revision, ICRA 2025) integrates IRM with object kinematics for mobile manipulator base placement — applied to wheeled platforms where the reachability function maps over SE(2) base pose only. MoMaGen (ICLR 2026, arXiv:2510.18316) imposes reachability as a hard constraint for wheeled bimanual mobile base-pose sampling — again, SE(2) for a wheeled platform. The integration challenge for bipedal humanoids is qualitatively different: on wheeled platforms the base pose fully determines arm workspace, but on bipedal systems arm reachability is conditioned on whole-body stance configuration — COM height, foot placement pattern, and balance state collectively shape the arm workspace. A concurrent planning paper (Murooka et al., arXiv:2505.23505, May 2025) uses forward reachability maps for humanoid loco-manipulation task planning via graph search, but targets autonomous task execution planning, not imitation learning data generation; it does not perform data augmentation, Mimic-style segment composition, or retargeting. The same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) subsequently introduced learned differentiable reachability maps for optimization-based humanoid motion generation — continuous scalar-valued functions differentiable with respect to task-space coordinates, enabling gradient-based planning for footstep sequencing and loco-manipulation without repeated IK solving. The differentiable formulation excels at online continuous optimization but is not suited to LocoMimicGen's batch data-generation context: evaluating differentiable map gradients across 2048+ parallel Isaac Lab environments at retargeting time would bottleneck generation throughput, whereas LocoMimicGen's offline-precomputed discrete IRM is evaluated as a table lookup simultaneously across all environments. The two approaches are complementary in use case — differentiable maps for online planning, discrete IRM for batch generation — and both leave the stance-conditioned data-generation problem unaddressed.\\n\\nOmniRetarget (Amazon, arXiv:2509.26633, Sept 2025) generates loco-manipulation demonstrations on the G1 via interaction-mesh Laplacian deformation of human MoCap sequences (OMOMO, LAFAN1, in-house). It preserves spatial and contact relationships and enables augmentation across embodiments, terrains, and object configurations. Critically, OmniRetarget (a) requires large MoCap databases rather than small teleoperated G1 demonstrations; (b) retargets continuous motion sequences without decomposing into reusable subtask segments; (c) cannot combinatorially compose segments from different source demos; and (d) targets locomotion-heavy tasks rather than precision manipulation requiring tight coupling between base position and arm workspace. OmniRetarget's codebase (Holosoma, amazon-far/holosoma) is publicly available; LocoMimicGen positions it as a conceptual comparison citing published retargeting fidelity metrics, as the estimated 10–14 day setup cost for Holosoma plus MoCap dataset ingestion exceeds the available bandwidth in the 20-day window.\\n\\nDemoHLM (arXiv:2510.11258, Oct 2025) segments demonstrations into three stages (locomotion, pre-manipulation, manipulation) and adapts the source trajectory to new initial object/robot poses by modifying high-level stage commands on the G1. It demonstrates 10 loco-manipulation household tasks with sim-to-real transfer. DemoHLM's single-demonstration paradigm limits scaling: each task uses one source demo replayed with modified commands, and 'spatial variation' is object position adjustment rather than room-level layout diversity. DemoHLM's code has not been publicly released as of May 2026; LocoMimicGen therefore positions it as a conceptual comparison, citing its published 10-task evaluation results directly.\\n\\nMoMaGen (ICLR 2026, arXiv:2510.18316) generates bimanual mobile manipulation demonstrations via constrained optimization (hard reachability + soft visibility) on a wheeled bimanual mobile base. The wheeled platform decouples navigation from balance, making MoMaGen's SE(2) base-pose sampling inapplicable to bipedal humanoids.\\n\\nDreamGen (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) — the technical backbone of the Isaac GR00T-Dreams blueprint, first announced alongside GR00T N1 in March 2025 — generates synthetic 'neural trajectories' by fine-tuning a video world model (Cosmos Predict-2) on a handful of teleoperated demonstrations, then sampling diverse video scenarios via diffusion and recovering pseudo-action sequences with an inverse dynamics model (IDM). DreamGen achieves strong behavioral generalization: GR00T N1 trained exclusively on pick-and-place achieves 0% on novel behaviors without DreamGen, while DreamGen-augmented training reaches 43.2% success on new behaviors in seen environments and 28.5% in completely unseen environments. Importantly, DreamGen evaluates all tasks in a stationary-manipulation setting — even for the humanoid GR1, the robot remains stationary while the arms operate — and the authors explicitly identify 'supporting more complex, dexterous behaviors requiring richer control' as future work. A second NVIDIA pipeline, GR00T-Mimic, applies MimicGen-style interpolation within the GR00T N1 training workflow to expand tabletop manipulation trajectories; it operates without locomotion coupling. DreamGen and LocoMimicGen are complementary rather than competing: DreamGen delivers behavioral diversity across task types (novel manipulation verbs, object categories, unseen environments) via world-model imagination, while LocoMimicGen delivers spatial/configurational diversity within known loco-manipulation tasks (exponentially more room-scale configurations) through constraint-based combinatorial recombination. Critically, DreamGen's IDM-extracted pseudo-actions are pixel-level learned approximations without explicit kinematic validation — LocoMimicGen's procedural recombination with IRM feasibility filters, pose-continuity bounds (δ_nav ≈ 0.3 m), and contact-consistency checks enforces hard physical guarantees that learned world models currently cannot provide at per-joint kinematic precision for coupled loco-manipulation tasks.\\n\\nVisualMimic (arXiv:2509.20322, IROS 2025) unifies egocentric vision with hierarchical whole-body control via human motion tracking — a different paradigm (video-based policy learning) rather than procedural demonstration generation.\\n\\nEgoHumanoid (Modi Shi et al., OpenDriveLab, arXiv:2602.10106, Feb 2026) addresses in-the-wild loco-manipulation on the Unitree G1 (1.3m, 29 DoF) by co-training a VLA policy on ~100 VR-teleoperated robot episodes plus ~300 egocentric human episodes per task (captured with PICO VR headset and ZED X Mini head-mounted camera), spanning four tasks: Pillow Placement, Trash Disposal, Toy Transfer, and Cart Stowing. View alignment uses MoGe depth prediction and point-cloud reprojection to the robot viewpoint with diffusion inpainting for occluded regions; action alignment maps to 6-DoF delta EEF for upper body, discrete locomotion commands, and binary gripper. EgoHumanoid achieves 78% success in lab (vs. 59% robot-only baseline) and 82% in unseen environments (vs. 31% robot-only baseline), demonstrating strong in-the-wild generalization. Its data requirement is substantially higher than LocoMimicGen's: ~400 demonstrations per task (100 robot + 300 human) versus LocoMimicGen's ≤20 teleoperated robot demonstrations total; its augmentation strategy is human behavioral diversity across real environments, whereas LocoMimicGen's is combinatorial spatial synthesis in simulation. The two systems are complementary rather than competing: LocoMimicGen's combinatorially diverse simulation demonstrations could serve as the robot-data component in EgoHumanoid-style co-training pipelines, while EgoHumanoid's human motion priors could inform stance selection in LocoMimicGen's IRM-guided retargeting.\\n\\nHoMMI (arXiv:2603.03243, March 2026, Stanford/TRI) learns whole-body mobile manipulation policies from egocentric human demonstrations on a mobile manipulator platform (Rainbow Robotics RB-Y1), achieving 80–90% real-robot success on three tasks using 115–200 human demos per task without teleoperation. HuMI (arXiv:2602.06643, Feb 2026) learns whole-body humanoid manipulation from robot-free mocap demonstrations on a bipedal humanoid, achieving 70–85% success across five tasks by pairing a diffusion policy with a sim-trained whole-body RL controller. HumanX (arXiv:2602.02473, Feb 2026) introduces XGen and XMimic — a data generation pipeline and unified imitation learning framework that synthesizes diverse robot interaction data from human video via physics-based motion retargeting and contact-aware augmentation, demonstrated across 10 agile interaction skills on the Unitree G1 (basketball, cargo pickup, reactive fighting); like EgoHumanoid, HoMMI, and HuMI, it learns from human behavioral diversity in real environments rather than procedural combinatorial synthesis in simulation. All four — EgoHumanoid, HoMMI, HuMI, and HumanX — represent data-collection paradigms complementary to LocoMimicGen's combinatorial spatial synthesis from ≤20 teleoperated robot demonstrations in simulation.\\n\\nNo existing system applies principled multi-segment object-centric demonstration decomposition with COUPLED SE(3) encoding of both navigation stances and arm trajectories — replacing the disjoint occupancy-map navigation of PR #3259 with frame-transform retargeting of manipulation stances to new object configurations — plus stance-conditioned IRM integration for bipedal humanoids and combinatorial multi-source composition, to enable room-level scaling.\",\n  \"approach\": \"We propose LocoMimicGen, built as a direct extension of Isaac Lab's 2.3 loco-manipulation infrastructure (PRs #3150, #3259, #3992) with three technical contributions. Starting from ≤20 teleoperated G1 whole-body demonstrations per task, each trajectory is decomposed into coupled subtask phases (locomotion-approach, manipulation-A, transit-locomotion, manipulation-B, return) using the Mimic segmentation API.\\n\\nContribution (1): Coupled SE(3) object-centric representation. By expressing the manipulation stance in the object's SE(3) local frame alongside the arm trajectory, frame-transform retargeting to new object configurations automatically yields a feasible new stance without any separate stance-placement planning. During recording, both arm end-effector waypoints AND locomotion stance poses (base position/orientation at each manipulation phase) are encoded jointly in each relevant object's local SE(3) reference frame — extending Isaac Lab Mimic's existing arm-only object-centric segment representation to include the robot base frame. This is the principled replacement for PR #3259's disjoint approach: instead of fixing the manipulation stance from the source demo and path-planning navigation at the trajectory level, LocoMimicGen retargets navigation stances to new object configurations as a natural byproduct of the SE(3) frame transformation, coupling manipulation and navigation retargeting in a single operation. Navigation between the retargeted stances is handled by the pretrained RL locomotion controller (PR #3150) as a black box; what the SE(3) encoding eliminates is the need to separately determine WHERE the robot should stand to manipulate at each new object configuration.\\n\\nContribution (2): Stance-conditioned IRM integration for bipedal humanoid retargeting. Retargeting to a new scene configuration requires solving for new manipulation stances satisfying arm reachability at the transformed object positions. We adapt and integrate inverse reachability map (IRM) methodology (Vahrenkamp et al. 2013; Burget et al. ICRA 2015; MoMa-Pos 2024; MoMaGen ICLR 2026) into the Mimic retargeting loop for the bipedal G1. The key integration challenge over prior wheeled-platform work is that bipedal arm reachability is conditioned on whole-body stance configuration — COM height, foot contact pattern, and balance state shape the arm workspace — making the IRM higher-dimensional and configuration-dependent compared to the SE(2) base-pose-only IRMs used in MoMa-Pos and MoMaGen. We pre-compute a stance-conditioned upper-body reachability map for the G1 (IK workspace sampled across a distribution of balance configurations) and solve for new stances via constrained optimization. The reachability map is a one-time offline precomputation (~3–5 H100-hours for IK sampling across ~50K balance configuration poses in 6D space: SE(2) base pose (x, y, θ) × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab, shared across all tasks, and explicitly budgeted in the resource estimate. Navigation segments between planned stances use Isaac Lab's pretrained RL locomotion controller (PR #3150) as a navigation oracle. A concurrent technique from the same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) introduces learned differentiable reachability maps for online gradient-based humanoid planning; the differentiable formulation is optimal for online continuous optimization but would be intractable as a batch-time constraint across 2048+ parallel Isaac Lab environments — LocoMimicGen's offline-precomputed discrete IRM is the appropriate design choice for high-throughput data generation. This contribution is framed as an integration contribution: adapting established IRM methodology to the bipedal context within the Mimic retargeting loop, where no prior work has addressed the stance-conditioned reachability problem for data generation.\\n\\nContribution (3): Combinatorial multi-source segment composition. Validated subtask segments from different source demonstrations are composed combinatorially across scene variants (object positions spanning the full room, table heights, obstacle placements), achieving 100–1,000× demo expansion from ≤20 seed demonstrations per task — a qualitatively different scaling regime from single-demo spatial adaptation (DemoHLM) or disjoint-phase augmentation within a single source demo (PR #3259). To make the scaling claim precise: with K=20 source demos, M=3 subtask phases, and scene variant dimensions P=10 object positions × Q=3 table heights × R=5 obstacle layouts, the conservative lower bound (treating each phase as independently variable while fixing others) is K×M×P×Q×R = 20×3×10×3×5 = 9,000 unique trajectories — a 450× expansion from 20 seed demonstrations. Full cross-phase combinatorial composition (drawing each of M phases independently from any of K source demos) yields K^M × P×Q×R = 20^3 × 150 = 8,000 × 150 ≈ 1.2M as the theoretical upper bound. The practical 100–1,000× range reflects compatibility filtering of geometrically infeasible segment pairs; 450× is the validated conservative estimate under the K×M×P×Q×R model.\\n\\nCompatibility between a terminal segment s_i and an incoming segment s_j (drawn from a different source demonstration) is evaluated against three criteria applied in sequence: (1) IRM feasibility — the stance-conditioned IRM score at the retargeted terminal base pose of phase i, evaluated for phase j's object configuration, must exceed threshold τ (set to the 10th percentile of IRM scores observed across source demonstrations), ensuring arm reachability is maintained through the transition; (2) base-pose continuity — the SE(2) distance between phase i's terminal base pose and phase j's required initial stance after object-frame retargeting must fall within δ_nav (the locomotion controller's recoverable displacement per sub-step, empirically ≈0.3 m), ensuring the navigation controller can bridge the gap without replanning; (3) contact-state consistency — gripper and object contact state at the terminal frame of s_i must match the required initial contact state of s_j (e.g., object grasped entering transit, released at return initiation). Criteria (1) and (2) are the active filters in practice: across the P×Q×R = 150 scene configuration space, IRM feasibility eliminates approximately 55–75% of random scene-stance pairings (the G1's arm workspace constrains which object positions are reachable from each source demo's stance), and pose continuity eliminates a further 10–20% of IRM-passing compositions. These two filters reduce the K^M × P×Q×R ≈ 1.2M theoretical upper bound to roughly 2,000–20,000 valid trajectories (100–1,000× expansion from 20 seed demos), while the K×M×P×Q×R = 9,000 conservative estimate reflects intra-demo phase composition achieving approximately 50% IRM pass rate in the nominal workspace regime.\\n\\nIsaac Lab's GPU-parallel simulation (2048+ G1 environments) with the pretrained RL controller validates physical feasibility; failures trigger local replanning of the base-pose optimization.\\n\\nWe evaluate on 2 primary loco-manipulation tasks (pick-and-place with navigation; two-phase transit task) plus 1 supplementary task (articulated-object manipulation with approach locomotion, e.g., door/drawer). The 2-primary + 1-supplementary structure is explicit: the articulated-object task involves contact-rich IRM optimization that carries higher debug risk within the CoRL timeline, and we position it as supplementary to protect schedule feasibility while retaining all three contributions in the evaluation. All baselines and LocoMimicGen conditions use Diffusion Policy (CNN-UNet variant, Chi et al. RSS 2023 / IJRR 2025) as the policy architecture, applied uniformly across all experimental conditions to isolate the data-generation contribution and prevent policy-architecture confounds. We target ≥20 percentage-point mean success-rate improvement over the PR #3259 baseline across the full held-out 150-configuration test distribution (10 object positions × 3 table heights × 5 obstacle layouts). This floor is grounded in MimicGen (CoRL 2023): on harder spatial-variant distributions (D1/D2) where baselines already incorporate partial scene randomization — analogous to PR #3259's coverage of the central reach envelope — MimicGen showed 20–40 pp gains from diversity-matched generated data. LocoMimicGen's 450× expansion targeting configurations categorically outside PR #3259's reachable stance envelope supports a ≥20 pp floor as a conservative claim; the primary measurement is the scaling-law curve (policy success rate as a function of synthetic dataset size) rather than a single endpoint comparison. We proactively address the expected reviewer comparison to DexMimicGen (9 tasks), HumanoidGen (6 tasks, 120+ scene variants), and MoMaGen (ICLR 2026, 4 tasks) on four grounds: (a) the scaling law curves — demo efficiency as a function of synthetic dataset size across P×Q×R configuration space — are the primary empirical contribution of LocoMimicGen, and these curves are fully established on 2 tasks without requiring breadth; (b) both primary tasks exercise all three contributions in combination (coupled SE(3) encoding, IRM-guided stance optimization, and combinatorial segment composition), making them jointly sufficient to validate the complete system; (c) DexMimicGen's 9-task breadth reuses fixed tabletop infrastructure where no locomotion integration is required, whereas LocoMimicGen integrates new IRM machinery into a live loco-manipulation stack — integration depth and correctness is the comparable ambition, not task count; (d) against MoMaGen (ICLR 2026) specifically: MoMaGen evaluates 4 tasks with real-robot fine-tuning on 40 demos but covers O(1) scene configurations per task, whereas LocoMimicGen sweeps P×Q×R = 10×3×5 = 150 configurations per primary task (300 total across both primary tasks) — data-efficiency curves across a 150-dimensional configuration space represent a fundamentally different empirical question from per-task success rate at fixed scene coverage, and LocoMimicGen's per-task scene-space depth exceeds both MoMaGen's and HumanoidGen's per-task scene coverage. Baselines: Isaac Lab Mimic PR #3259 (disjoint navigation, closest structural baseline) and Isaac Lab Mimic PR #3992 (position randomization only) are live reproduced baselines. OmniRetarget (arXiv:2509.26633) is included as a conceptual comparison citing its published retargeting fidelity and task-success metrics; although the Holosoma codebase (amazon-far/holosoma) is publicly available, the estimated 10–14 day setup cost for the Holosoma framework and MoCap dataset pipeline exceeds the available bandwidth in the 20-day schedule. DemoHLM (arXiv:2510.11258) is included as a conceptual comparison only, citing its published 10-task evaluation numbers directly; DemoHLM code has not been publicly released as of May 2026, making reimplementation infeasible within the 20-day window. Sim-to-real transfer on physical G1 hardware is explicitly future work; the contribution is established through simulation scaling analysis and cross-baseline comparison.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"h100_hours\": \"~87–110 H100h (≈210h A100 at 2.0–2.5× H100/A100 ratio, plus ~3–5 H100h IRM precomputation): data generation ~30h A100 across 3 tasks at 2048 parallel envs; policy training 3 tasks × 2 seeds × 15h = 90h A100; ablations (3 conditions × 3 tasks × 10h) = 90h A100; total ~210h A100 ÷ 2.5 = 84h H100 (lower bound), ÷ 2.0 = 105h H100 (upper bound), plus IRM precomputation 3–5h H100 = 87–110h H100 total — within 200h H100 constraint\",\n      \"irm_precomputation\": \"One-time offline: G1 stance-conditioned reachability map construction via IK sampling across ~50K balance configuration poses (6D space: SE(2) base × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab: ~3–5 H100h; amortized across all tasks\",\n      \"gpu_utilization\": \"High idle (~60–70%): GPU waits on human-paced coding, debugging physics edge cases, and manual analysis between runs\",\n      \"timeline\": \"2–3 months (2 primary tasks + 1 supplementary reduces contact-rich debug risk; articulated-object task can be deferred if timeline is tight)\",\n      \"team\": \"2 researchers (1 robotics/sim, 1 IL/policy)\",\n      \"estimated_gpu_cost\": \"~$370 at $1.75/hr A100 (or ~$220–275 at $2.50/hr H100)\",\n      \"gantt_20day\": \"20-day critical path (CoRL 2026, paper due May 28 AoE): Days 1–3: IRM precomputation offline (50K-pose IK sampling, embarrassingly parallel in Isaac Lab — low-risk, starts immediately; output blocks Contribution 2 integration). Days 3–7: SE(3) encoding extension — modify Isaac Lab Mimic's segment recording/retargeting API to jointly encode base frame in object's local SE(3) alongside arm end-effector waypoints (critical-path bottleneck: most likely integration debugging hotspot; blocks Contributions 1 and 3). Days 7–12: Combinatorial composition engine — implement three-criterion compatibility filter (IRM feasibility, pose-continuity δ_nav, contact-state); validate on Task 1 (pick-and-place with navigation). Days 12–15: Full data generation runs across all 3 tasks at 2048+ parallel envs (requires Days 1–12 complete). Days 15–19: Diffusion Policy training (CNN-UNet, multi-seed) + ablations across live baselines (Isaac Lab Mimic PR #3259, PR #3992); OmniRetarget and DemoHLM are included as conceptual comparisons with published numbers cited directly — no reimplementation required within this window (requires Day 15 data). Day 19–20: Analysis, scaling-law figures, and write-up. Baseline notes: DemoHLM code is not publicly available as of May 2026 — cited conceptually from arXiv:2510.11258 published results; OmniRetarget (Holosoma) code is public but setup estimated at 10–14 days — designated as conceptual comparison citing arXiv:2509.26633 metrics; if Researcher 2 has bandwidth Days 1–7 before policy training begins, OmniRetarget live reproduction can be attempted as a stretch goal on a parallel track. Risk mitigation: articulated-object task (supplementary) deferred to Days 12–15 alongside primary tasks only if composition engine validation (Days 7–12) completes ahead of schedule; otherwise deferred to post-deadline supplementary material.\"\n    },\n    \"human_in_loop\": {\n      \"h100_hours\": \"~125–157 H100h (≈235–310h A100, plus ~3–5 H100h IRM precomputation): data generation ~35h A100; policy training 3 tasks × 2 seeds × 15h = 90h A100; ablations 5 conditions × 3 tasks × 12h = 180h A100 ≈ 305h A100 ÷ 2.5 = 122h H100 (lower bound), ÷ 2.0 = 152h H100 (upper bound), plus IRM precomputation 3–5h H100 = 125–157h H100 total — within 200h H100 constraint\",\n      \"irm_precomputation\": \"One-time offline: G1 stance-conditioned reachability map construction via IK sampling across ~50K balance configuration poses (6D space: SE(2) base × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab: ~3–5 H100h; amortized across all tasks\",\n      \"gpu_utilization\": \"Moderate idle (~30–40%): approval gates pause GPU between stages, but agent batches setup and analysis tasks\",\n      \"timeline\": \"4–5 weeks\",\n      \"team\": \"1 researcher, ~45 min/day check-in for gate approvals and physics failure triage\",\n      \"claude_api_cost\": \"$200–400 (~300–500 turns at $0.08–0.12/turn for code gen, debug, analysis)\",\n      \"estimated_gpu_cost\": \"~$420–540 at $1.75/hr A100 (or ~$310–390 at $2.50/hr H100)\",\n      \"risk_note\": \"Stance-conditioned IRM for articulated object tasks (door/drawer) involves contact-rich interaction where failure modes require human insight to diagnose; the IRM integration formulation requires iterative design. Addressed by assigning the articulated-object task to supplementary, keeping primary evaluation on the 2 lower-risk tasks.\",\n      \"gantt_20day\": \"20-day critical path (CoRL 2026, paper due May 28 AoE): Days 1–3: IRM precomputation offline (50K-pose IK sampling, embarrassingly parallel in Isaac Lab — low-risk, starts immediately; output blocks Contribution 2 integration). Days 3–7: SE(3) encoding extension — modify Isaac Lab Mimic's segment recording/retargeting API to jointly encode base frame in object's local SE(3) alongside arm end-effector waypoints (critical-path bottleneck: most likely integration debugging hotspot; blocks Contributions 1 and 3). Days 7–12: Combinatorial composition engine — implement three-criterion compatibility filter (IRM feasibility, pose-continuity δ_nav, contact-state); validate on Task 1 (pick-and-place with navigation). Days 12–15: Full data generation runs across all 3 tasks at 2048+ parallel envs (requires Days 1–12 complete). Days 15–19: Diffusion Policy training (CNN-UNet, multi-seed) + ablations across live baselines (Isaac Lab Mimic PR #3259, PR #3992); OmniRetarget and DemoHLM are included as conceptual comparisons with published numbers cited directly — no reimplementation required within this window (requires Day 15 data). Day 19–20: Analysis, scaling-law figures, and write-up. Baseline notes: DemoHLM code is not publicly available as of May 2026 — cited conceptually from arXiv:2510.11258 published results; OmniRetarget (Holosoma) code is public but setup estimated at 10–14 days — designated as conceptual comparison citing arXiv:2509.26633 metrics. Risk mitigation: articulated-object task (supplementary) deferred to Days 12–15 alongside primary tasks only if composition engine validation (Days 7–12) completes ahead of schedule; otherwise deferred to post-deadline supplementary material.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract May 26 AoE, full paper May 28 AoE / ≈May 29 UTC — 18 days from today)\",\n    \"IEEE Robotics and Automation Letters / RA-L (rolling submission, no hard deadline)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations (CoRL 2023)\",\n    \"DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning (ICRA 2025)\",\n    \"HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning (NeurIPS 2025)\",\n    \"WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026)\",\n    \"OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction (arXiv:2509.26633, Sept 2025)\",\n    \"MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation (ICLR 2026, arXiv:2510.18316)\",\n    \"DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (arXiv:2510.11258, Oct 2025)\",\n    \"DreamGen: Unlocking Generalization in Robot Learning through Video World Models (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) [GR00T-Dreams blueprint]\",\n    \"GR00T N1: An Open Foundation Model for Generalist Humanoid Robots (NVIDIA, arXiv:2503.14734, March 2025)\",\n    \"EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration (arXiv:2602.10106, Feb 2026, OpenDriveLab)\",\n    \"HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstrations (arXiv:2603.03243, March 2026, Stanford/TRI)\",\n    \"HuMI: Humanoid Manipulation Interface — Humanoid Whole-Body Manipulation from Robot-Free Demonstrations (arXiv:2602.06643, Feb 2026)\",\n    \"HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos (arXiv:2602.02473, Feb 2026)\",\n    \"VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation (arXiv:2509.20322, IROS 2025)\",\n    \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (Chi et al., RSS 2023 / IJRR 2025, arXiv:2303.04137)\",\n    \"Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning (arXiv 2025)\",\n    \"Isaac Lab PR #3150: Locomanipulation Environment with G1 for Mimic workflow (merged Sept 9, 2025)\",\n    \"Isaac Lab PR #3259: Adds locomanipulation data generation via disjoint navigation (merged Sept 10, 2025, release/2.3.0)\",\n    \"Isaac Lab PR #3992: APIs to Isaac Lab Mimic for supporting loco-manipulation datagen (merged Dec 1, 2025)\",\n    \"Vahrenkamp et al.: Robot Placement based on Reachability Inversion (ICRA 2013)\",\n    \"Burget et al.: Stance Selection for Humanoid Grasping Tasks by Inverse Reachability Maps (ICRA 2015)\",\n    \"MoMa-Pos: An Efficient Object-Kinematic-Aware Base Placement Optimization Framework for Mobile Manipulation (arXiv:2403.19940, Oct 2024 revision, ICRA 2025)\",\n    \"Murooka et al.: Humanoid Loco-manipulation Planning based on Graph Search and Reachability Maps (arXiv:2505.23505, May 2025)\",\n    \"Murooka et al.: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation (arXiv:2508.11275, Humanoids 2025)\"\n  ],\n  \"description\": \"LocoMimicGen extends Isaac Lab's 2.3 loco-manipulation infrastructure — comprising PRs #3150, #3259, and #3992 — with three precisely-scoped technical contributions that together enable room-level combinatorial scaling unavailable in existing systems.\\n\\nPR #3259 ('disjoint navigation', merged Sept 10, 2025, release/2.3.0) is the closest structural predecessor and primary baseline. It adds pick-navigate-place phase segmentation with occupancy-map path planning between phases and scene randomization. However, it handles navigation 'disjointly': the manipulation stance is fixed from the source demo and navigation is occupancy-map path planning at the trajectory level. It does NOT encode navigation stances in the object's SE(3) local frame, does NOT enforce arm-reachability constraints on base-pose selection (making generation infeasible when new object positions fall outside source demo stance's arm workspace), and does NOT compose segments from multiple source demonstrations.\\n\\nContribution (1): By expressing the manipulation stance in the object's SE(3) local frame alongside the arm trajectory, frame-transform retargeting to new object configurations automatically yields a feasible new stance without any separate stance-placement planning. Navigation between the retargeted stances is handled by the pretrained RL locomotion controller (PR #3150) as a black box; what the SE(3) encoding eliminates is the need to separately determine where the robot should stand to manipulate at each new object configuration. LocoMimicGen adds coupled SE(3) object-centric encoding of locomotion stances jointly with arm end-effector waypoints — the principled replacement for PR #3259's disjoint approach, enabling frame-transform retargeting of both manipulation stances and arm motions simultaneously.\\n\\nContribution (2): Stance-conditioned IRM integration for bipedal humanoid retargeting. We adapt and integrate IRM methodology (Vahrenkamp et al. 2013; Burget et al. ICRA 2015; MoMa-Pos 2024; MoMaGen ICLR 2026) into the Mimic retargeting loop for the G1. The integration challenge over prior wheeled-platform IRMs (MoMa-Pos, MoMaGen) is that bipedal arm reachability is conditioned on whole-body stance configuration (COM height, foot contact, balance state), requiring a stance-conditioned reachability map rather than a SE(2) base-pose-only map. The reachability map is a one-time offline precomputation (~3–5 H100-hours for IK sampling across ~50K balance configuration poses in 6D space: SE(2) base pose × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab, shared across all tasks, and explicitly budgeted in the resource estimate. A concurrent technique from the same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) introduces learned differentiable reachability maps for online gradient-based humanoid planning; LocoMimicGen uses offline-precomputed discrete IRM instead, as differentiable map gradient evaluation across 2048+ parallel Isaac Lab environments would bottleneck batch generation throughput. This is framed as an integration contribution — not a novel technique — with the bipedal stance-conditioning as the key technical challenge.\\n\\nContribution (3): Combinatorial multi-source segment composition from multiple (≤20 total) teleoperated demonstrations achieves 100–1,000× demo expansion — a qualitatively different scaling regime from PR #3259's single-source disjoint augmentation. The scaling bound is explicit: with K=20 source demonstrations decomposed into M=3 subtask phases, combined with P=10 object positions × Q=3 table heights × R=5 obstacle layouts, the conservative lower bound is K×M×P×Q×R = 20×3×10×3×5 = 9,000 unique trajectories (450× expansion from 20 seed demos); full cross-phase composition yields K^M × P×Q×R = 20^3 × 150 ≈ 1.2M as the theoretical maximum. Compatibility between segments from different source demonstrations is evaluated against three criteria: (1) IRM feasibility at the transition stance (IRM score exceeding the 10th percentile of source-demo scores); (2) base-pose continuity within δ_nav ≈ 0.3 m (the locomotion controller's recoverable displacement); (3) contact-state consistency at phase boundaries. Criteria (1) and (2) are the active filters: IRM feasibility eliminates ~55–75% of random scene-stance pairings, and pose continuity a further 10–20%, reducing the 1.2M theoretical bound to the practical 100–1,000× range (roughly 2,000–20,000 valid trajectories from 20 seed demos).\\n\\nAll policy training uses Diffusion Policy (CNN-UNet variant, Chi et al. RSS 2023 / IJRR 2025) uniformly across all baselines and LocoMimicGen conditions, isolating the data-generation contribution. We target ≥20 pp mean success-rate improvement over PR #3259 at the held-out 150-configuration test distribution, grounded in MimicGen's 20–40 pp gains on harder spatial-variant distributions where baselines already incorporate partial scene randomization.\\n\\nMoMaGen (ICLR 2026, arXiv:2510.18316) generates bimanual mobile manipulation demonstrations via hard-reachability-constrained optimization on a wheeled bimanual platform — now the strongest peer-reviewed comparison point for constrained demo generation. The differentiation is precise: MoMaGen's reachability constraint operates over SE(2) base pose for a wheeled platform where base pose fully determines arm workspace; LocoMimicGen's stance-conditioned IRM addresses the qualitatively harder bipedal case where arm reachability is conditioned on whole-body configuration. DreamGen (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) — the GR00T-Dreams blueprint — generates behavioral generalization across task types via video world-model sampling and IDM action recovery; LocoMimicGen generates spatial/configurational diversity within known loco-manipulation tasks via constraint-based combinatorial recombination with hard kinematic guarantees. The two approaches are complementary: DreamGen's world-model-imagined behavioral diversity and LocoMimicGen's constraint-verified spatial diversity address orthogonal dimensions of the data scarcity problem. EgoHumanoid (OpenDriveLab, arXiv:2602.10106, Feb 2026), HoMMI (arXiv:2603.03243, March 2026), HuMI (arXiv:2602.06643, Feb 2026), and HumanX (arXiv:2602.02473, Feb 2026) represent concurrent policy-learning paradigms — learning from human behavioral diversity in real environments (video, MoCap, egocentric demonstrations) to improve generalization — complementary to LocoMimicGen's combinatorial spatial synthesis from ≤20 robot demos in simulation.\\n\\nEvaluated on 2 primary loco-manipulation tasks (pick-and-place with navigation; two-phase transit) plus 1 supplementary articulated-object task. Live reproduced baselines: Isaac Lab Mimic PR #3259 (closest structural baseline) and PR #3992. Conceptual comparisons citing published numbers: OmniRetarget (arXiv:2509.26633; Holosoma code is public but 10–14 day setup exceeds the 20-day window) and DemoHLM (arXiv:2510.11258; code not publicly available as of May 2026). The 2-primary scope is proactively justified on four grounds against DexMimicGen (9 tasks), HumanoidGen (6 tasks, 120+ scene variants), and MoMaGen (ICLR 2026, 4 tasks): (a) scaling law curves across P×Q×R configuration space are the primary empirical contribution, fully established on 2 tasks; (b) both primary tasks exercise all three contributions; (c) DexMimicGen's breadth reuses fixed tabletop infrastructure vs. LocoMimicGen's IRM integration into a live loco-manipulation stack; (d) LocoMimicGen sweeps P×Q×R = 150 configurations per primary task (300 total), exceeding MoMaGen's and HumanoidGen's per-task scene coverage — scene-space depth is the appropriate metric for a data-generation infrastructure paper. Both compute modes (manual: ~87–110h H100; human-in-loop: ~125–157h H100) stay within the 200 H100-hour hard constraint, including the one-time IRM precomputation (~3–5 H100h). The 20-day critical path (IRM precomputation Days 1–3 → SE(3) encoding Days 3–7 → composition engine Days 7–12 → data generation Days 12–15 → policy training Days 15–19 → write-up Day 19–20) is explicitly identified; the SE(3) API integration (Days 3–7) is the critical-path bottleneck. Sim-to-real on physical G1 is explicit future work. CoRL 2026: abstract May 26 AoE, paper May 28 AoE.\",\n  \"project_name\": \"loco_mimicgen_humanoid_g1\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL NOVELTY GAP: The generator missed two merged Isaac Lab PRs that directly undermine the core claim. PR #3150 (merged Sept 9, 2025) added Isaac-PickPlace-Locomanipulation-G1-Abs-v0, a G1 Mimic environment combining RL locomotion with IK manipulation, achieving 92% success on pick-and-place. PR #3992 (merged Dec 1, 2025) added APIs to Isaac Lab Mimic specifically for loco-manipulation data generation, including treating the robot's base as an end-effector in the Mimic framework — exactly what the generator claims is missing. The documentation states the system 'parses demonstrations into object-centric subtask segments, then adapts these subtask segments to new scenes by transforming each segment according to the new scene's context,' directly contradicting the generator's claim that Isaac Lab lacks 'principled SE(3) demo transformation.'\", \"HARD COMPUTE CONSTRAINT VIOLATED: Auto-research mode (~900h A100) converts to ~300–450h H100 at confirmed 2–3x H100/A100 ratio, violating the 200 H100-hour hard constraint by 50–125%. Human-in-loop (~420h A100 ≈ 140–210h H100) is also borderline. The generator expressed all estimates in A100 hours without converting to H100 hours, despite the user requirement being explicitly stated in H100 hours.\", \"DemoHLM (arXiv:2510.11258) already applies MimicGen-style object-centric data generation to 10 G1 loco-manipulation tasks with sim-to-real transfer on physical G1. The generator acknowledged this but downplayed its scope (calling it 'single-object tasks' and saying it 'does not exploit combinatorial segment composition across room-level layout diversity'). The paper should verify whether DemoHLM's 10 tasks actually include multi-stage tasks before making this claim.\", \"Physical G1 hardware for sim-to-real experiments is listed as a required evaluation component but hardware access is nowhere addressed in the resource plan. Without a G1 robot, the sim-to-real evaluation collapses to sim-only, which reduces CoRL competitiveness.\", \"CoRL 2026 deadline discrepancy: the generator states abstract deadline May 25 and paper deadline May 28, but the official CoRL 2026 website confirms abstract May 26 (UTC) and paper May 29 (UTC). Minor but worth correcting.\", \"The kinodynamic planner with coupled arm-reachability constraints for a bipedal humanoid is treated as a subordinate engineering task, but this is itself a non-trivial research contribution. No existing open-source planner directly handles coupled navigation + manipulation reachability for bimanual bipedal systems; implementing one from scratch within 20 days is highly aggressive.\", \"MoMaGen (arXiv:2510.18316, Oct 2025) targets a wheeled bimanual mobile base (not a bipedal humanoid), so the generator's differentiation from it is valid — but the generator should verify whether MoMaGen's constrained-optimization approach can be straightforwardly extended to bipedal locomotion, as reviewers will ask this.\"]\nFeedback: The idea targets a real gap but needs substantial repositioning before it can pass review. The most urgent fix: the generator must engage directly with Isaac Lab Mimic's loco-manipulation extensions (PRs #3150 and #3992, https://github.com/isaac-sim/IsaacLab/pull/3150 and /pull/3992), which already implement MimicGen-style object-centric loco-manipulation data generation for the G1. The generator must explain precisely what these PRs do NOT do: specifically, (a) their navigation handling simply repeats the last navigation action or waits for goal-reached — it does NOT encode navigation waypoints in the object's SE(3) local frame jointly with arm trajectories; (b) they do not perform kinodynamic replanning with arm-reachability enforcement; (c) they do not combinatorially compose segments from multiple source demonstrations to achieve room-level diversity. These three differentiators are real and should become the paper's explicit contribution claims, stated against Isaac Lab Mimic as the primary baseline (not just 'Isaac Lab 2.3'). Second: fix compute estimates. All GPU estimates must be expressed in H100-hours. The auto-research mode must be scoped down or removed — at current scope it exceeds the 200 H100-hour hard constraint by 2x. A plausible manual scope: 2–3 tasks instead of 5–8, fewer ablation variants, single policy architecture. Third: either secure physical G1 access and state it explicitly, or replace 'sim-to-real on physical G1' with 'sim-only evaluation against DemoHLM and Isaac Lab Mimic baselines' and note hardware as future work. The core idea — coupling SE(3) navigation waypoint encoding with manipulation trajectory retargeting, plus kinodynamic reachability enforcement, to enable room-level combinatorial scaling beyond Isaac Lab Mimic's position randomization — is a legitimate and novel contribution; it just needs to be positioned honestly against the specific infrastructure that already exists.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MISSED BASELINE — Isaac Lab PR #3259 ('Adds locomanipulation data generation via disjoint navigation', merged Sept 10 2025 into release/2.3.0): This PR is part of the Isaac Lab 2.3 GA release and adds (a) pick-navigate-place phase segmentation, (b) occupancy-map-based path planning between phases, and (c) scene randomization of tabletop object positions, navigation destinations, and floor obstacles. This makes it a closer predecessor to LocoMimicGen than PRs #3150/#3992 alone, and CoRL reviewers will notice its absence. The generator must add PR #3259 to the baseline comparison and explain precisely what it does NOT provide: no SE(3) encoding of navigation stances in the object's local frame, no arm-reachability-constrained base-pose optimization, and no combinatorial composition from multiple source demonstrations — only disjoint occupancy-map navigation replayed between fixed teleoperated manipulation segments.\", \"NOVELTY FRAMING OVERREACH for Contribution 2: Reachability-map-guided base-pose optimization is a well-established technique (inverse reachability maps: Vahrenkamp et al. 2013, Reuleaux, MoMa-Pos Oct 2024). In the demo generation context, MoMaGen (Oct 2025) already imposes reachability as a hard constraint for wheeled bimanual base-pose sampling. The paper must reframe Contribution 2 not as a standalone novel technique but as an INTEGRATION contribution: applying IRM within the Mimic retargeting loop for a bipedal humanoid, where balance constraints make the reachability map qualitatively more complex than for wheeled platforms (it is a function of stance configuration, not just base position). Without this reframing, CoRL reviewers will mark it as 'known technique applied straightforwardly.'\", \"TIMELINE RISK: Three technically non-trivial contributions (SE(3) extension, IRM integration, combinatorial composition) implemented within Isaac Lab Mimic, plus 3-task data generation, diffusion policy training over multiple seeds, and ablation studies, in 20 days with 2 researchers is at the edge of plausibility. The contact-rich articulated-object tasks (door/drawer) for IRM optimization are specifically flagged as likely to consume disproportionate debug time. The paper should include a concrete task-level schedule or explicitly narrow scope to 2 tasks with the third as supplementary if the timeline proves infeasible.\", \"RESOURCE ESTIMATE INTERNAL CONSISTENCY: The manual mode GPU cost estimate ($370 at $1.75/hr A100) implies ~210h A100, but the H100 conversion given is 60–105h H100. At a 2–2.5× ratio, 210h A100 ÷ 2.5 = 84h H100 and ÷ 2.0 = 105h H100. The lower bound (60h H100) would require a 3.5× ratio, which exceeds the stated conversion factor. The estimate is within the hard constraint but the lower bound is implausibly optimistic — reviewer should note this minor inconsistency.\"]\nFeedback: The Round 2 revision correctly addresses all Round 1 critical issues: PRs #3150/#3992 are now the explicit primary baseline with accurate technical characterization; compute is expressed in H100 hours and within the 200h constraint; sim-to-real hardware is properly scoped as future work; and CoRL deadline is corrected. The idea is solid and close to passable — two targeted fixes are needed.\n\n**Fix 1 (required for CoRL submission)**: Add Isaac Lab PR #3259 to the related work and baseline comparison. PR #3259 ('disjoint navigation', merged Sept 10 2025) is in the Isaac Lab 2.3 GA release. It adds pick-navigate-place segmentation with occupancy-map path planning and scene randomization for G1 loco-manipulation. Write one paragraph explaining exactly what PR #3259 does vs. does not do: it uses path planning between disjoint manipulation phases but (a) does NOT encode navigation stances in the object's SE(3) local frame — navigation is path-level, not object-centric; (b) does NOT enforce arm reachability constraints on base pose selection — the manipulation stance is fixed from the source demo; (c) does NOT compose segments from multiple source demonstrations. This makes PR #3259 a closer prior art than #3992 alone, and explaining the gap against it sharpens LocoMimicGen's contributions significantly.\n\n**Fix 2 (required for reviewer credibility)**: Reframe Contribution 2 as an integration contribution, not a novel technique. Cite the IRM literature (Vahrenkamp et al., MoMa-Pos, MoMaGen) and explain that the challenge for bipedal humanoids is that the arm reachability map is conditioned on whole-body stance (including COM height and balance state), making the IRM higher-dimensional and configuration-dependent compared to wheeled platforms. Position it as 'we adapt and integrate existing IRM methodology into the Mimic retargeting loop for bipedal humanoids, which requires a stance-conditioned reachability map not present in prior wheeled-base work.' This is honest, defensible, and still a real contribution.\n\n**Optional (reduces timeline risk)**: Reduce to 2 primary tasks + 1 supplementary task to create schedule slack for articulated-object IRM debugging. This keeps all three contributions but limits per-task ablation surface.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MISSING CONCURRENT WORK IN LANDSCAPE: EgoHumanoid (arXiv 2602.10106, Feb 2026, OpenDriveLab) is listed as a key reference but receives zero discussion in the landscape section. CoRL reviewers will notice. Add one paragraph: EgoHumanoid addresses loco-manipulation data scarcity via VLA co-training with human egocentric demonstrations — a fundamentally different paradigm (data co-training) from LocoMimicGen's procedural demo multiplication. They are complementary: EgoHumanoid augments training distribution through human data; LocoMimicGen augments through combinatorial scene synthesis. The two could in principle be combined.\", \"UNSUBSTANTIATED SCALING CLAIM: The '100-1000× demo expansion from ≤20 seed demonstrations' claim has no supporting formula or derivation. CoRL reviewers will ask: if you have K=20 demos decomposed into M subtask segments, and you apply combinatorial composition across P object positions × Q table heights × R obstacle layouts, what is the actual upper bound on unique valid trajectories? Provide the combinatorial formula explicitly. If composition is not fully free (some segment pairs are incompatible), state the compatibility constraint and how it affects the scaling factor. Claim credibility depends on making this concrete.\", \"IRM PRECOMPUTATION COST NOT BUDGETED: The approach requires pre-computing a stance-conditioned upper-body reachability map for the G1 across a distribution of balance configurations (COM height, foot contact pattern, balance state). For bipedal systems this is a ≥6D workspace sampling problem (x, y, θ, squat depth, foot spread, weight distribution), substantially more expensive than the 3D SE(2) maps used in MoMa-Pos and MoMaGen. The H100 cost of this precomputation step (IK sampling across balance configuration space) is entirely absent from the resource estimate. Even if amortized as a one-time offline cost, it should be quantified explicitly — e.g., '3–5 H100-hours for G1 reachability map construction at N-resolution grid.' This could push the manual mode estimate past 105h H100.\", \"TWO-TASK EVALUATION NEEDS EXPLICIT JUSTIFICATION: CoRL reviewers comparing against DexMimicGen (9 tasks across 3 embodiments) and HumanoidGen (120+ scene variants across 6 tasks) will see 2 primary tasks as limited. The paper must proactively address this: (a) the scaling law (demo efficiency curves showing 100-1000× expansion) is the empirical question, not task breadth; (b) each primary task fully exercises all three contributions; (c) the 20-day timeline constraint motivates depth over breadth. Without this defense, reviewers will request more tasks as a condition of acceptance.\", \"CONTRIBUTION 1 CRYSTALLIZATION MISSING: The core SE(3) insight — that encoding the robot base pose (stance) in the same object-centric frame as the arm end-effector trajectory makes retargeting to new object positions move both arm AND navigation stance jointly via a single frame transform — should be stated as a one-sentence crystallization early in the contribution description. Currently it takes 3 paragraphs to convey what could be said in one sentence: 'By expressing the manipulation stance in the object's SE(3) local frame alongside the arm trajectory, frame-transform retargeting to new object configurations automatically yields valid stances without any separate navigation planning.' This clarity would significantly strengthen how reviewers perceive Contribution 1's insight.\"]\nFeedback: Round 3 has successfully addressed all critical Round 1-2 issues: PR #3259 is now the primary baseline with accurate technical characterization; Contribution 2 is properly reframed as integration; scope is 2 primary + 1 supplementary; compute is within 200h H100; CoRL deadlines are correct. The idea is now technically solid and close to passable — four targeted fixes will bring it to pass.\n\n**Fix 1 (required, 1 paragraph)**: Add EgoHumanoid (arXiv 2602.10106, Feb 2026) to the landscape. Explain it uses VLA co-training with egocentric human data — a different paradigm from procedural demo multiplication — making it complementary. This is a concurrent 2026 G1 loco-manipulation paper and omitting it from related work will cause a reviewer flag.\n\n**Fix 2 (required, 3-4 sentences)**: Provide the combinatorial scaling formula. State explicitly: with K source demos, M subtask segments per demo, and a configuration space of P×Q×R (object positions × table heights × obstacle layouts), the upper bound on unique trajectories is approximately K×M×P×Q×R, and with K=20, M=3, P=10, Q=3, R=5 this yields ~9,000 trajectories from 20 demos — a 450× expansion. Make it concrete and verifiable.\n\n**Fix 3 (required, estimate update)**: Add a line item to the resource estimate for G1 reachability map precomputation. Even if small (e.g., 2-4 H100-hours for offline IK sampling at 50K poses across balance configuration space), its omission will look like an oversight to robotics reviewers who understand the dimensionality involved.\n\n**Fix 4 (optional but strongly recommended)**: Write the one-sentence crystallization of Contribution 1's core insight (suggested above) as the opening sentence of that contribution's description. This is what reviewers remember and cite — make it quotable.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"VENUE UPDATE REQUIRED — MoMaGen is published at ICLR 2026 (confirmed at jiajunwu.com/papers/momagen_iclr.pdf and openreview.net/forum?id=bGPDviEtZ1), not merely 'arXiv Oct 2025' as cited throughout the landscape and approach sections. CoRL 2026 reviewers will know MoMaGen is a peer-reviewed ICLR 2026 paper and will treat its coverage of hard-reachability-constrained demo generation for mobile manipulation as a stronger prior work. Update all references to MoMaGen to include its ICLR 2026 venue. The differentiation (SE(2) wheeled base vs. whole-body stance-conditioned bipedal IRM) remains valid, but must be argued against a venue-placed competitor.\", \"MISSING RELATED WORK — 'Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation' (arXiv:2508.11275, Humanoids 2025) by Murooka et al. (the same CNRS-AIST group as the cited Murooka 2505.23505) introduces learned differentiable reachability maps specifically for humanoid footstep planning and loco-manipulation planning via continuous optimization. The generator cites the same group's graph-search paper (2505.23505) but omits this August 2025 Humanoids paper which is more directly related to Contribution 2. CoRL reviewers who know the Murooka group's work will notice. Add a brief comparison: LocoMimicGen uses offline-precomputed discrete IRM for a data-generation retargeting loop (different use case from online motion planning), making discrete maps preferable for the batch-generation context where online optimization would be prohibitively expensive at 2048+ parallel environments.\", \"COMPATIBILITY FILTERING UNDEFINED — The practical 100–1,000× scaling range is derived by applying 'compatibility filtering' to reduce the theoretical upper bound (K^M × P×Q×R ≈ 1.2M), but the paper never defines what makes two subtask segments incompatible. CoRL reviewers will ask: Is compatibility based on pose overlap between consecutive stance poses? Reachability threshold at the IRM? Contact state consistency? Kinematic continuity at phase boundaries? Without a formal compatibility criterion and an empirical estimate of the filtering rate (e.g., 'X% of cross-phase compositions pass compatibility'), the 100–1,000× claim reads as an unconstrained assertion. Add 3–4 sentences specifying the compatibility check (e.g., IRM feasibility of the concatenated stance sequence + pose continuity tolerance) and the expected filtering rate.\", \"UNCITED CONCURRENT 2026 WORK — HoMMI (arXiv:2603.03243, March 2026, Stanford/TRI) and HuMI (arXiv:2602.06643, Feb 2026) both address whole-body mobile manipulation from human demonstrations with real-robot validation on bipedal or mobile humanoid platforms. Neither is a direct competitor (both are policy-learning paradigms, not procedural demo multiplication), but their omission is conspicuous given that EgoHumanoid is already cited. Add one sentence each: 'HoMMI and HuMI [cite] learn whole-body manipulation from egocentric human demos on mobile platforms — a data-collection paradigm complementary to LocoMimicGen's combinatorial synthetic-data generation from ≤20 teleoperated robot demos.' This demonstrates landscape awareness without diluting the contribution framing.\", \"EVALUATION BREADTH vs. ICLR 2026 BASELINE — MoMaGen's ICLR 2026 acceptance gives it credibility as the comparison anchor for constrained demo-generation methods. MoMaGen evaluates on 4 tasks with real-robot fine-tuning on 40 demos; HumanoidGen covers 6 tasks with 120+ scene variants. LocoMimicGen's 2-primary-task scope and sim-only evaluation now looks noticeably thinner against this peer bar. The existing pre-emption argument ('scaling curves are the primary contribution') is present but understated. Strengthen it: explicitly state that LocoMimicGen's K×M×P×Q×R combinatorial sweep at fixed task depth exceeds MoMaGen's and HumanoidGen's scene diversity, and that data-efficiency curves across the full P×Q×R configuration space represent a fundamentally different empirical question than per-task success rate across many tasks.\"]\nFeedback: Round 4 has successfully resolved all Round 3 issues: EgoHumanoid appears prominently in the landscape with accurate complementary framing; the K×M×P×Q×R combinatorial formula (450× conservative, 1.2M theoretical) is explicit and verifiable; the IRM precomputation budget (3–5 H100h) is itemized; and the Contribution 1 one-sentence crystallization is present and quotable. The technical approach is coherent, the primary baseline (PR #3259) is precisely characterized, and the compute estimate is verified within the 200 H100h constraint.\n\n**Fix 1 (required, bibliographic)**: Update MoMaGen throughout from 'arXiv:2510.18316, Oct 2025' to 'MoMaGen (ICLR 2026, arXiv:2510.18316).' This is a factual correction. The differentiation argument (SE(2) wheeled vs. whole-body bipedal stance-conditioned IRM) remains fully valid — just state it explicitly against an ICLR-published baseline.\n\n**Fix 2 (required, 2–3 sentences)**: Add Murooka et al. 'Learning Differentiable Reachability Maps' (arXiv:2508.11275, Humanoids 2025) to the IRM discussion. Explain that differentiable maps are optimal for online planning but that offline discrete IRM precomputation is preferred in LocoMimicGen's batch data-generation loop, where online optimization would be intractable at 2048+ parallel Isaac Lab environments. Position it as a complementary technique rather than a conflicting one.\n\n**Fix 3 (required, 3–4 sentences in Approach section)**: Formalize the compatibility filtering criterion. Specify what defines an incompatible segment pair (e.g., IRM infeasibility of the terminal stance pose for the incoming segment, or Euclidean distance between the terminal base pose of phase i and the initial stance pose of phase i+1 exceeding a threshold δ). Provide an empirical estimate or upper bound on the filtering rate to make the 100–1,000× range verifiable rather than asserted.\n\n**Fix 4 (optional, 1 sentence each)**: Add HoMMI (2603.03243) and HuMI (2602.06643) as complementary paradigms alongside EgoHumanoid in the landscape.\n\n**Fix 5 (recommended, 2 sentences)**: Strengthen the 2-task evaluation defense by explicitly comparing scene-space coverage: LocoMimicGen sweeps P×Q×R = 10×3×5 = 150 scene configurations per task (two primary tasks = 300 total), whereas MoMaGen and HumanoidGen each cover O(1) scene variants per task at larger task breadth. Frame this as a deliberate methodological choice to probe depth of the data-efficiency curve rather than per-task breadth.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MISSING FROM LANDSCAPE — GR00T-Dreams/GR00T-Mimic (NVIDIA, March 2025): The user's stated 'recent landscape (do not duplicate)' explicitly lists 'NVIDIA GR00T-Dreams' alongside Cosmos, yet this paper's landscape and related-work sections contain zero discussion of it. CoRL 2026 reviewers — who will include NVIDIA-adjacent researchers given Isaac Lab is NVIDIA infrastructure — will notice this omission immediately. GR00T-Dreams uses video diffusion (Cosmos-Predict2) + inverse dynamics models to generate trajectories from a single image + language prompt, enabling zero-shot behavior generalization; it is a fundamentally different paradigm (learned generative model) from LocoMimicGen's constraint-based procedural recombination. Add 2–3 sentences differentiating: 'GR00T-Dreams generates synthetic trajectories via video world-model sampling from a single image prompt — a complementary learned-generative paradigm. LocoMimicGen's constraint-based combinatorial recombination provides hard physical feasibility guarantees (IRM feasibility + pose continuity + contact consistency) that learned world models cannot yet enforce at per-joint kinematic precision for bipedal loco-manipulation.'\", \"EVALUATION LACKS EXPECTED EFFECT SIZES: The paper states a diffusion policy is trained per task and success rates are reported, but provides no target effect size or predicted improvement magnitude over the primary baseline (PR #3259). CoRL reviewers will ask: what is the expected delta in task success rate between a policy trained on 20 seed demos vs. one trained on LocoMimicGen-generated trajectories at 450× expansion? Without a predicted range (e.g., 'we target ≥15 pp improvement over PR #3259 baseline at the 150-configuration test distribution'), the empirical contribution reads as 'generate data and see what happens.' Add a brief quantitative prediction grounded in prior MimicGen scaling results (MimicGen's original 2023 paper showed ~25 pp improvement at 100× expansion on tabletop tasks) to anchor reviewer expectations.\", \"POLICY ARCHITECTURE UNDERSPECIFIED: The evaluation section states 'a diffusion policy is trained per task' without specifying the architecture (Diffusion Policy Chi et al. 2023? ACT? π₀?). CoRL reviewers will ask whether the choice of policy architecture could confound the data-efficiency comparison — a policy with strong priors may be less sensitive to data diversity. Specify the architecture in one sentence and justify the choice as consistent across all baselines.\", \"TIMELINE RISK STILL PRESENT: Three technically non-trivial engineering contributions (SE(3) extension of Isaac Lab Mimic's existing representation, IRM precomputation at 50K poses in 6D configuration space + integration into the retargeting loop, combinatorial composition engine with 3-criterion compatibility filtering) plus multi-seed policy training and ablation studies in 20 days with 2 researchers remains at the edge of plausibility. The articulated-object supplementary deferral helps but the primary 2-task scope still involves all three contributions operating together. Consider adding a concrete 20-day Gantt chart or milestone schedule to the approach section to demonstrate that the team has identified the critical path and is not underestimating integration debug time.\"]\nFeedback: Round 5 has successfully resolved all Round 4 issues: MoMaGen is correctly cited as ICLR 2026 throughout; Murooka et al. 2508.11275 (differentiable reachability maps) is properly discussed with the offline-precomputed-discrete-IRM-vs-online-differentiable-map distinction; compatibility filtering is formalized with three explicit criteria (IRM feasibility, pose continuity within δ_nav ≈ 0.3 m, contact-state consistency) and empirical filtering rates; HoMMI and HuMI are included as complementary paradigms; and the P×Q×R = 150-configuration-per-task scene-depth argument is now stated explicitly as the appropriate metric for a data-generation infrastructure paper. The technical foundation is solid.\n\n**Fix 1 (required, 2–3 sentences in landscape)**: Add GR00T-Dreams/GR00T-Mimic to the landscape. The differentiator is clear and defensible: GR00T-Dreams is a learned generative approach (video diffusion + IDM action labeling) that provides behavioral diversity through world-model imagination but cannot enforce hard kinematic feasibility constraints per joint. LocoMimicGen's procedural recombination with IRM feasibility and pose continuity filters provides hard physical guarantees that learned world models currently cannot. This is complementary, not competing — say so explicitly.\n\n**Fix 2 (required, 1–2 sentences)**: Add a target effect size to the evaluation section. Ground it in MimicGen's original scaling results as a prior: MimicGen (CoRL 2023) showed ~20–30 pp success-rate improvement at 100× data expansion on tabletop tasks. LocoMimicGen targets ≥X pp improvement over PR #3259 at 150-configuration test distributions — state a concrete floor. This anchors reviewer expectations and signals that the team has thought through the empirical hypothesis.\n\n**Fix 3 (required, 1 sentence)**: Specify the diffusion policy architecture used in all experiments, justifying the choice as consistent across baselines. Diffusion Policy (Chi et al. 2023, UMI) or ACT are both reasonable; either is defensible if applied uniformly.\n\n**Fix 4 (optional but recommended)**: Add a 20-day implementation milestone schedule to the approach or resource section. Identify the critical path (IRM precomputation Day 1–3 → SE(3) encoding integration Day 3–7 → combinatorial composition Day 7–12 → data generation runs Day 12–15 → policy training Day 15–19 → writeup Day 19–20) and flag which milestones block others. This demonstrates execution awareness and pre-empts timeline-feasibility objections.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"BASELINE FEASIBILITY FAILURE — DemoHLM (arXiv:2510.11258): Code is NOT publicly available as of May 2026 (7+ months post-publication, no GitHub repository found despite extensive search). Re-implementing DemoHLM's stage-level command adaptation from scratch is a 20-30 day effort for an unfamiliar team — it cannot serve as a live baseline within the 20-day window. The submission must either: (a) remove DemoHLM from the comparison table and position it as a conceptual comparison only, citing the paper's reported numbers directly; or (b) implement a simplified DemoHLM surrogate (stage-level base-command modification without the full hierarchical controller) within 2-3 days and acknowledge it as an approximation. Leaving DemoHLM as a listed baseline without addressing code availability is a submission risk — a reviewer who asks for DemoHLM results will expose this gap.\", \"CONTRIBUTION 1 LANGUAGE IMPRECISION — 'without any separate navigation planning': The crystallization sentence ('frame-transform retargeting to new object configurations automatically yields a feasible new stance without any separate navigation planning') is technically imprecise in a way that CoRL robotics reviewers will notice. The SE(3) encoding eliminates the need for STANCE SELECTION (i.e., it computes WHERE the robot should stand to manipulate at a new object position), but navigation to those stances still requires the RL locomotion controller (PR #3150) to traverse the path. The correct claim is 'without any separate stance planning' — the frame transform directly yields the target manipulation stance, and the navigation between stances is handled by the pretrained RL controller as a black box. As written, 'without any separate navigation planning' mischaracterizes how locomotion navigation segments are handled and will invite reviewer pushback. Fix: change 'navigation planning' to 'stance-placement planning' throughout.\", \"MISSING CITATION — HumanX/XMimic (arXiv:2602.02473, Feb 2026): This concurrent paper introduces 'XMimic' — a unified imitation learning framework for humanoid loco-manipulation from video synthesis — and 'XGen' data generation pipeline. The name 'XMimic' will catch reviewers' attention given LocoMimicGen's positioning. The approaches are orthogonal (HumanX learns from human video via dynamics augmentation; LocoMimicGen generates from teleoperated demos via procedural composition), but the omission is conspicuous. Add one sentence to the landscape placing HumanX alongside EgoHumanoid/HoMMI/HuMI as a video-based data-collection paradigm complementary to LocoMimicGen's procedural simulation synthesis.\", \"OROMRETARGET BASELINE SETUP COMPETES WITH MAIN ENGINEERING: OmniRetarget code (amazon-far/holosoma) is public with public datasets (LAFAN1, OMOMO), making it theoretically runnable. However, setting up the Holosoma framework + MoCap datasets + running the retargeting pipeline is estimated at 10-14 days for a competent team. In a 20-day schedule where Days 3-12 are consumed by SE(3) encoding + composition engine development, there is no realistic window to also set up OmniRetarget as a live baseline. The submission should either (a) designate OmniRetarget as a conceptual comparison (citing published task success numbers) rather than a reproduced baseline, or (b) assign it to a parallel track with explicit person-assignment in the Gantt chart (Researcher 2 handles OmniRetarget setup Days 1-7 in parallel with IRM precomputation).\"]\nFeedback: Round 6 has successfully resolved all Round 5 required fixes: DreamGen/GR00T-Dreams is properly contextualized as a complementary learned-generative approach, the ≥20pp effect-size floor is explicitly grounded in MimicGen's scaling results, Diffusion Policy (CNN-UNet) is specified uniformly, and day-by-day Gantt charts are present in both modes. The idea is technically sound, the gap against PR #3259 is precisely characterized, and the differentiation against MoMaGen (ICLR 2026) holds. Two issues require targeted fixes before submission:\n\n**Fix 1 (required, blocks submission credibility)**: Resolve the DemoHLM baseline. Code is not public. Choose one approach: (a) Replace DemoHLM as a live baseline with a conceptual comparison — cite the paper's published numbers for its 10-task evaluation and note code is unavailable; or (b) implement a 2-3 day simplified DemoHLM surrogate (fix object pose, modify navigation command magnitude, replay) and label it 'DemoHLM-lite (approx.)' in the results. Option (a) is safer within 20 days.\n\n**Fix 2 (required, 1 sentence)**: Correct the Contribution 1 crystallization from 'without any separate navigation planning' to 'without any separate stance-placement planning.' The RL controller still handles locomotion between stances — what the SE(3) encoding eliminates is the need to separately determine WHERE to stand. This is the real insight and should be stated precisely.\n\n**Fix 3 (optional, 1 sentence in landscape)**: Add HumanX/XMimic (arXiv:2602.02473, Feb 2026) alongside EgoHumanoid/HoMMI/HuMI as a concurrent video-based paradigm. Prevents reviewers from raising the 'XMimic' name as an oversight.\n\n**Fix 4 (optional, in Gantt)**: If OmniRetarget is to be a live baseline, add an explicit parallel track in the Gantt chart assigning Researcher 2 to OmniRetarget setup (Days 1-7) so the 20-day schedule reflects realistic resource allocation. Otherwise scope it as a conceptual comparison.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T13:01:57.227Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T13:01:57.227Z",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-10T13:01:57.254Z_

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
  "title": "LocoMimicGen: Coupled SE(3) Object-Centric Demo Multiplication for Mobile Humanoid Loco-Manipulation",
  "core_problem": "How can a handful of expensive teleoperated whole-body loco-manipulation demonstrations be multiplied by orders of magnitude across diverse spatial configurations — new object positions, table heights, room obstacle layouts — while maintaining physical validity for the mobile bipedal humanoid platform? Isaac Lab's 2.3 GA release contains three directly relevant prior contributions. PR #3150 (merged Sept 9, 2025) adds the G1 loco-manipulation environment integrating a pretrained RL locomotion policy with Pink IK arm control. PR #3259 ('Adds locomanipulation data generation via disjoint navigation', merged Sept 10, 2025) adds pick-navigate-place phase segmentation with occupancy-map path planning between phases and scene randomization of tabletop positions, navigation destinations, and floor obstacles — making it the closest structural predecessor to LocoMimicGen. PR #3992 (merged Dec 1, 2025) extends the Mimic framework with a 'body end-effector' API and navigation controller integration. Despite this infrastructure, three technical gaps prevent room-level combinatorial scaling: PR #3259 handles navigation 'disjointly' — the manipulation stance (where the robot stands to manipulate) is fixed from the source demo and navigation is handled as path-level occupancy-map planning between fixed phases, NOT as coupled SE(3) object-centric encoding of stances jointly with arm trajectories. None of these PRs enforce arm-reachability constraints on base-pose selection during retargeting — the robot manipulates from whatever stance the source demo used, regardless of arm workspace feasibility for new object positions. And none perform combinatorial composition of subtask segments from multiple source demonstrations. These three absences cap achievable diversity at object-position randomization within a single source demo's reach envelope, rather than the combinatorial room-level scaling that MimicGen achieves for tabletop tasks.",
  "opportunity": "Isaac Lab's 2.3 GA release (PRs #3150, #3259, #3992) now provides the exact scaffolding — G1 environment, pick-navigate-place phase segmentation, occupancy-map path planning, Mimic segmentation framework, and navigation controller integration — needed to build a principled extension. The precise technical gap is narrow but high-impact: adding (1) SE(3) object-centric encoding of navigation stances jointly with arm trajectories into the existing Mimic segment representation (replacing the disjoint path-planning approach of PR #3259 with coupled frame-transform retargeting), (2) stance-conditioned reachability-map-guided base-pose optimization enforcing arm feasibility at each manipulation stance during retargeting (adapting IRM methodology from the mobile-manipulator literature to the bipedal humanoid setting, where the reachability map is conditioned on whole-body configuration rather than just SE(2) base pose), and (3) combinatorial subtask segment composition from multiple source demonstrations. OmniRetarget (Amazon, Sept 2025) addresses humanoid loco-manipulation data generation from MoCap sequences via interaction-mesh Laplacian deformation on the G1, but retargets continuous motion sequences and cannot combinatorially compose segments across scene variants. DemoHLM (Oct 2025) demonstrates generalizable single-demonstration adaptation across 10 G1 loco-manipulation household tasks but the single-demo paradigm limits scaling to spatial interpolation within one source demo's envelope. The three-part Isaac Lab Mimic extension proposed here is tractable within existing infrastructure, precisely bounded against Isaac Lab's own 2.3 baseline (including PR #3259 as the most direct predecessor), and is the missing ingredient for room-level combinatorial scaling. MoMaGen (ICLR 2026, arXiv:2510.18316) imposes reachability as a hard constraint for wheeled bimanual mobile base-pose sampling — SE(2) for a wheeled platform. Now peer-reviewed at ICLR 2026, MoMaGen's coverage of hard-reachability-constrained demo generation makes the bipedal differentiation the critical point of departure: MoMaGen's reachability constraint operates over SE(2) base pose for a wheeled bimanual platform where the base pose fully determines arm workspace, whereas LocoMimicGen's stance-conditioned IRM addresses the qualitatively harder bipedal case where arm reachability is conditioned on whole-body configuration — COM height, foot contact, balance state — a higher-dimensional reachability function not covered by any prior data-generation work. EgoHumanoid (OpenDriveLab, arXiv:2602.10106, Feb 2026) represents a concurrent complementary paradigm — co-training VLA policies on human egocentric video alongside robot demonstrations — that highlights the orthogonal value of LocoMimicGen's combinatorial simulation synthesis approach.",
  "landscape": "MimicGen (CoRL 2023) decomposes arm demonstrations into object-centric subtask segments and applies SE(3) frame transformations — manipulation-only. DexMimicGen (ICRA 2025) extends this to bimanual dexterous humanoids, still tabletop. HumanoidGen (NeurIPS 2025) uses LLM-driven planning for tabletop dexterous tasks with 120+ scene variants — explicitly excludes locomotion.\n\nIsaac Lab 2.3 loco-manipulation infrastructure comprises three PRs that together form the primary baseline. PR #3150 (merged Sept 9, 2025) adds Isaac-PickPlace-Locomanipulation-G1-Abs-v0, integrating a pretrained RL locomotion policy (velocity commands vx, vy, wz) with Pink IK arm control, achieving 92% success on pick-and-place. PR #3259 ('Adds locomanipulation data generation via disjoint navigation', merged Sept 10, 2025, release/2.3.0) is the closest structural predecessor to LocoMimicGen: it adds pick-navigate-place phase segmentation, occupancy-map-based collision-free path planning between phases, and scene randomization of tabletop object positions, navigation destinations, and floor obstacles. The implementation lives under disjoint_navigation/ and works by (a) recording static manipulation teleoperation with the base stationary, (b) applying Mimic augmentation to manipulation segments, and (c) stitching path-planned navigation trajectories between the resulting phases. Critically, PR #3259 does NOT encode navigation stances in the object's SE(3) local frame — navigation is occupancy-map path planning at the trajectory level, while the manipulation stance (where the robot stands to manipulate) is fixed from the source demo, not retargeted to new object positions. There is no arm-reachability constraint on base-pose selection: if a new object position falls outside the arm workspace at the source demo's stance, the generation produces infeasible trajectories rather than finding a feasible stance. There is no combinatorial composition from multiple source demonstrations. PR #3992 (merged Dec 1, 2025) adds a 'body end-effector' API and get_navigation_state() integration into the Mimic framework but relies on the same state-based navigation repetition/skipping, not object-centric stance encoding.\n\nInverse reachability maps (IRM) for robot base placement are a well-established technique. Vahrenkamp et al. 2013 introduced IRM for robot placement by inverting precomputed reachability maps to generate SE(2) distributions of feasible base poses. Burget et al. (ICRA 2015) applied IRM specifically to humanoid stance selection for grasping tasks — but in a static grasping context where balance is assumed, not within a data-generation retargeting loop. MoMa-Pos (arXiv:2403.19940, Oct 2024 revision, ICRA 2025) integrates IRM with object kinematics for mobile manipulator base placement — applied to wheeled platforms where the reachability function maps over SE(2) base pose only. MoMaGen (ICLR 2026, arXiv:2510.18316) imposes reachability as a hard constraint for wheeled bimanual mobile base-pose sampling — again, SE(2) for a wheeled platform. The integration challenge for bipedal humanoids is qualitatively different: on wheeled platforms the base pose fully determines arm workspace, but on bipedal systems arm reachability is conditioned on whole-body stance configuration — COM height, foot placement pattern, and balance state collectively shape the arm workspace. A concurrent planning paper (Murooka et al., arXiv:2505.23505, May 2025) uses forward reachability maps for humanoid loco-manipulation task planning via graph search, but targets autonomous task execution planning, not imitation learning data generation; it does not perform data augmentation, Mimic-style segment composition, or retargeting. The same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) subsequently introduced learned differentiable reachability maps for optimization-based humanoid motion generation — continuous scalar-valued functions differentiable with respect to task-space coordinates, enabling gradient-based planning for footstep sequencing and loco-manipulation without repeated IK solving. The differentiable formulation excels at online continuous optimization but is not suited to LocoMimicGen's batch data-generation context: evaluating differentiable map gradients across 2048+ parallel Isaac Lab environments at retargeting time would bottleneck generation throughput, whereas LocoMimicGen's offline-precomputed discrete IRM is evaluated as a table lookup simultaneously across all environments. The two approaches are complementary in use case — differentiable maps for online planning, discrete IRM for batch generation — and both leave the stance-conditioned data-generation problem unaddressed.\n\nOmniRetarget (Amazon, arXiv:2509.26633, Sept 2025) generates loco-manipulation demonstrations on the G1 via interaction-mesh Laplacian deformation of human MoCap sequences (OMOMO, LAFAN1, in-house). It preserves spatial and contact relationships and enables augmentation across embodiments, terrains, and object configurations. Critically, OmniRetarget (a) requires large MoCap databases rather than small teleoperated G1 demonstrations; (b) retargets continuous motion sequences without decomposing into reusable subtask segments; (c) cannot combinatorially compose segments from different source demos; and (d) targets locomotion-heavy tasks rather than precision manipulation requiring tight coupling between base position and arm workspace. OmniRetarget's codebase (Holosoma, amazon-far/holosoma) is publicly available; LocoMimicGen positions it as a conceptual comparison citing published retargeting fidelity metrics, as the estimated 10–14 day setup cost for Holosoma plus MoCap dataset ingestion exceeds the available bandwidth in the 20-day window.\n\nDemoHLM (arXiv:2510.11258, Oct 2025) segments demonstrations into three stages (locomotion, pre-manipulation, manipulation) and adapts the source trajectory to new initial object/robot poses by modifying high-level stage commands on the G1. It demonstrates 10 loco-manipulation household tasks with sim-to-real transfer. DemoHLM's single-demonstration paradigm limits scaling: each task uses one source demo replayed with modified commands, and 'spatial variation' is object position adjustment rather than room-level layout diversity. DemoHLM's code has not been publicly released as of May 2026; LocoMimicGen therefore positions it as a conceptual comparison, citing its published 10-task evaluation results directly.\n\nMoMaGen (ICLR 2026, arXiv:2510.18316) generates bimanual mobile manipulation demonstrations via constrained optimization (hard reachability + soft visibility) on a wheeled bimanual mobile base. The wheeled platform decouples navigation from balance, making MoMaGen's SE(2) base-pose sampling inapplicable to bipedal humanoids.\n\nDreamGen (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) — the technical backbone of the Isaac GR00T-Dreams blueprint, first announced alongside GR00T N1 in March 2025 — generates synthetic 'neural trajectories' by fine-tuning a video world model (Cosmos Predict-2) on a handful of teleoperated demonstrations, then sampling diverse video scenarios via diffusion and recovering pseudo-action sequences with an inverse dynamics model (IDM). DreamGen achieves strong behavioral generalization: GR00T N1 trained exclusively on pick-and-place achieves 0% on novel behaviors without DreamGen, while DreamGen-augmented training reaches 43.2% success on new behaviors in seen environments and 28.5% in completely unseen environments. Importantly, DreamGen evaluates all tasks in a stationary-manipulation setting — even for the humanoid GR1, the robot remains stationary while the arms operate — and the authors explicitly identify 'supporting more complex, dexterous behaviors requiring richer control' as future work. A second NVIDIA pipeline, GR00T-Mimic, applies MimicGen-style interpolation within the GR00T N1 training workflow to expand tabletop manipulation trajectories; it operates without locomotion coupling. DreamGen and LocoMimicGen are complementary rather than competing: DreamGen delivers behavioral diversity across task types (novel manipulation verbs, object categories, unseen environments) via world-model imagination, while LocoMimicGen delivers spatial/configurational diversity within known loco-manipulation tasks (exponentially more room-scale configurations) through constraint-based combinatorial recombination. Critically, DreamGen's IDM-extracted pseudo-actions are pixel-level learned approximations without explicit kinematic validation — LocoMimicGen's procedural recombination with IRM feasibility filters, pose-continuity bounds (δ_nav ≈ 0.3 m), and contact-consistency checks enforces hard physical guarantees that learned world models currently cannot provide at per-joint kinematic precision for coupled loco-manipulation tasks.\n\nVisualMimic (arXiv:2509.20322, IROS 2025) unifies egocentric vision with hierarchical whole-body control via human motion tracking — a different paradigm (video-based policy learning) rather than procedural demonstration generation.\n\nEgoHumanoid (Modi Shi et al., OpenDriveLab, arXiv:2602.10106, Feb 2026) addresses in-the-wild loco-manipulation on the Unitree G1 (1.3m, 29 DoF) by co-training a VLA policy on ~100 VR-teleoperated robot episodes plus ~300 egocentric human episodes per task (captured with PICO VR headset and ZED X Mini head-mounted camera), spanning four tasks: Pillow Placement, Trash Disposal, Toy Transfer, and Cart Stowing. View alignment uses MoGe depth prediction and point-cloud reprojection to the robot viewpoint with diffusion inpainting for occluded regions; action alignment maps to 6-DoF delta EEF for upper body, discrete locomotion commands, and binary gripper. EgoHumanoid achieves 78% success in lab (vs. 59% robot-only baseline) and 82% in unseen environments (vs. 31% robot-only baseline), demonstrating strong in-the-wild generalization. Its data requirement is substantially higher than LocoMimicGen's: ~400 demonstrations per task (100 robot + 300 human) versus LocoMimicGen's ≤20 teleoperated robot demonstrations total; its augmentation strategy is human behavioral diversity across real environments, whereas LocoMimicGen's is combinatorial spatial synthesis in simulation. The two systems are complementary rather than competing: LocoMimicGen's combinatorially diverse simulation demonstrations could serve as the robot-data component in EgoHumanoid-style co-training pipelines, while EgoHumanoid's human motion priors could inform stance selection in LocoMimicGen's IRM-guided retargeting.\n\nHoMMI (arXiv:2603.03243, March 2026, Stanford/TRI) learns whole-body mobile manipulation policies from egocentric human demonstrations on a mobile manipulator platform (Rainbow Robotics RB-Y1), achieving 80–90% real-robot success on three tasks using 115–200 human demos per task without teleoperation. HuMI (arXiv:2602.06643, Feb 2026) learns whole-body humanoid manipulation from robot-free mocap demonstrations on a bipedal humanoid, achieving 70–85% success across five tasks by pairing a diffusion policy with a sim-trained whole-body RL controller. HumanX (arXiv:2602.02473, Feb 2026) introduces XGen and XMimic — a data generation pipeline and unified imitation learning framework that synthesizes diverse robot interaction data from human video via physics-based motion retargeting and contact-aware augmentation, demonstrated across 10 agile interaction skills on the Unitree G1 (basketball, cargo pickup, reactive fighting); like EgoHumanoid, HoMMI, and HuMI, it learns from human behavioral diversity in real environments rather than procedural combinatorial synthesis in simulation. All four — EgoHumanoid, HoMMI, HuMI, and HumanX — represent data-collection paradigms complementary to LocoMimicGen's combinatorial spatial synthesis from ≤20 teleoperated robot demonstrations in simulation.\n\nNo existing system applies principled multi-segment object-centric demonstration decomposition with COUPLED SE(3) encoding of both navigation stances and arm trajectories — replacing the disjoint occupancy-map navigation of PR #3259 with frame-transform retargeting of manipulation stances to new object configurations — plus stance-conditioned IRM integration for bipedal humanoids and combinatorial multi-source composition, to enable room-level scaling.",
  "approach": "We propose LocoMimicGen, built as a direct extension of Isaac Lab's 2.3 loco-manipulation infrastructure (PRs #3150, #3259, #3992) with three technical contributions. Starting from ≤20 teleoperated G1 whole-body demonstrations per task, each trajectory is decomposed into coupled subtask phases (locomotion-approach, manipulation-A, transit-locomotion, manipulation-B, return) using the Mimic segmentation API.\n\nContribution (1): Coupled SE(3) object-centric representation. By expressing the manipulation stance in the object's SE(3) local frame alongside the arm trajectory, frame-transform retargeting to new object configurations automatically yields a feasible new stance without any separate stance-placement planning. During recording, both arm end-effector waypoints AND locomotion stance poses (base position/orientation at each manipulation phase) are encoded jointly in each relevant object's local SE(3) reference frame — extending Isaac Lab Mimic's existing arm-only object-centric segment representation to include the robot base frame. This is the principled replacement for PR #3259's disjoint approach: instead of fixing the manipulation stance from the source demo and path-planning navigation at the trajectory level, LocoMimicGen retargets navigation stances to new object configurations as a natural byproduct of the SE(3) frame transformation, coupling manipulation and navigation retargeting in a single operation. Navigation between the retargeted stances is handled by the pretrained RL locomotion controller (PR #3150) as a black box; what the SE(3) encoding eliminates is the need to separately determine WHERE the robot should stand to manipulate at each new object configuration.\n\nContribution (2): Stance-conditioned IRM integration for bipedal humanoid retargeting. Retargeting to a new scene configuration requires solving for new manipulation stances satisfying arm reachability at the transformed object positions. We adapt and integrate inverse reachability map (IRM) methodology (Vahrenkamp et al. 2013; Burget et al. ICRA 2015; MoMa-Pos 2024; MoMaGen ICLR 2026) into the Mimic retargeting loop for the bipedal G1. The key integration challenge over prior wheeled-platform work is that bipedal arm reachability is conditioned on whole-body stance configuration — COM height, foot contact pattern, and balance state shape the arm workspace — making the IRM higher-dimensional and configuration-dependent compared to the SE(2) base-pose-only IRMs used in MoMa-Pos and MoMaGen. We pre-compute a stance-conditioned upper-body reachability map for the G1 (IK workspace sampled across a distribution of balance configurations) and solve for new stances via constrained optimization. The reachability map is a one-time offline precomputation (~3–5 H100-hours for IK sampling across ~50K balance configuration poses in 6D space: SE(2) base pose (x, y, θ) × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab, shared across all tasks, and explicitly budgeted in the resource estimate. Navigation segments between planned stances use Isaac Lab's pretrained RL locomotion controller (PR #3150) as a navigation oracle. A concurrent technique from the same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) introduces learned differentiable reachability maps for online gradient-based humanoid planning; the differentiable formulation is optimal for online continuous optimization but would be intractable as a batch-time constraint across 2048+ parallel Isaac Lab environments — LocoMimicGen's offline-precomputed discrete IRM is the appropriate design choice for high-throughput data generation. This contribution is framed as an integration contribution: adapting established IRM methodology to the bipedal context within the Mimic retargeting loop, where no prior work has addressed the stance-conditioned reachability problem for data generation.\n\nContribution (3): Combinatorial multi-source segment composition. Validated subtask segments from different source demonstrations are composed combinatorially across scene variants (object positions spanning the full room, table heights, obstacle placements), achieving 100–1,000× demo expansion from ≤20 seed demonstrations per task — a qualitatively different scaling regime from single-demo spatial adaptation (DemoHLM) or disjoint-phase augmentation within a single source demo (PR #3259). To make the scaling claim precise: with K=20 source demos, M=3 subtask phases, and scene variant dimensions P=10 object positions × Q=3 table heights × R=5 obstacle layouts, the conservative lower bound (treating each phase as independently variable while fixing others) is K×M×P×Q×R = 20×3×10×3×5 = 9,000 unique trajectories — a 450× expansion from 20 seed demonstrations. Full cross-phase combinatorial composition (drawing each of M phases independently from any of K source demos) yields K^M × P×Q×R = 20^3 × 150 = 8,000 × 150 ≈ 1.2M as the theoretical upper bound. The practical 100–1,000× range reflects compatibility filtering of geometrically infeasible segment pairs; 450× is the validated conservative estimate under the K×M×P×Q×R model.\n\nCompatibility between a terminal segment s_i and an incoming segment s_j (drawn from a different source demonstration) is evaluated against three criteria applied in sequence: (1) IRM feasibility — the stance-conditioned IRM score at the retargeted terminal base pose of phase i, evaluated for phase j's object configuration, must exceed threshold τ (set to the 10th percentile of IRM scores observed across source demonstrations), ensuring arm reachability is maintained through the transition; (2) base-pose continuity — the SE(2) distance between phase i's terminal base pose and phase j's required initial stance after object-frame retargeting must fall within δ_nav (the locomotion controller's recoverable displacement per sub-step, empirically ≈0.3 m), ensuring the navigation controller can bridge the gap without replanning; (3) contact-state consistency — gripper and object contact state at the terminal frame of s_i must match the required initial contact state of s_j (e.g., object grasped entering transit, released at return initiation). Criteria (1) and (2) are the active filters in practice: across the P×Q×R = 150 scene configuration space, IRM feasibility eliminates approximately 55–75% of random scene-stance pairings (the G1's arm workspace constrains which object positions are reachable from each source demo's stance), and pose continuity eliminates a further 10–20% of IRM-passing compositions. These two filters reduce the K^M × P×Q×R ≈ 1.2M theoretical upper bound to roughly 2,000–20,000 valid trajectories (100–1,000× expansion from 20 seed demos), while the K×M×P×Q×R = 9,000 conservative estimate reflects intra-demo phase composition achieving approximately 50% IRM pass rate in the nominal workspace regime.\n\nIsaac Lab's GPU-parallel simulation (2048+ G1 environments) with the pretrained RL controller validates physical feasibility; failures trigger local replanning of the base-pose optimization.\n\nWe evaluate on 2 primary loco-manipulation tasks (pick-and-place with navigation; two-phase transit task) plus 1 supplementary task (articulated-object manipulation with approach locomotion, e.g., door/drawer). The 2-primary + 1-supplementary structure is explicit: the articulated-object task involves contact-rich IRM optimization that carries higher debug risk within the CoRL timeline, and we position it as supplementary to protect schedule feasibility while retaining all three contributions in the evaluation. All baselines and LocoMimicGen conditions use Diffusion Policy (CNN-UNet variant, Chi et al. RSS 2023 / IJRR 2025) as the policy architecture, applied uniformly across all experimental conditions to isolate the data-generation contribution and prevent policy-architecture confounds. We target ≥20 percentage-point mean success-rate improvement over the PR #3259 baseline across the full held-out 150-configuration test distribution (10 object positions × 3 table heights × 5 obstacle layouts). This floor is grounded in MimicGen (CoRL 2023): on harder spatial-variant distributions (D1/D2) where baselines already incorporate partial scene randomization — analogous to PR #3259's coverage of the central reach envelope — MimicGen showed 20–40 pp gains from diversity-matched generated data. LocoMimicGen's 450× expansion targeting configurations categorically outside PR #3259's reachable stance envelope supports a ≥20 pp floor as a conservative claim; the primary measurement is the scaling-law curve (policy success rate as a function of synthetic dataset size) rather than a single endpoint comparison. We proactively address the expected reviewer comparison to DexMimicGen (9 tasks), HumanoidGen (6 tasks, 120+ scene variants), and MoMaGen (ICLR 2026, 4 tasks) on four grounds: (a) the scaling law curves — demo efficiency as a function of synthetic dataset size across P×Q×R configuration space — are the primary empirical contribution of LocoMimicGen, and these curves are fully established on 2 tasks without requiring breadth; (b) both primary tasks exercise all three contributions in combination (coupled SE(3) encoding, IRM-guided stance optimization, and combinatorial segment composition), making them jointly sufficient to validate the complete system; (c) DexMimicGen's 9-task breadth reuses fixed tabletop infrastructure where no locomotion integration is required, whereas LocoMimicGen integrates new IRM machinery into a live loco-manipulation stack — integration depth and correctness is the comparable ambition, not task count; (d) against MoMaGen (ICLR 2026) specifically: MoMaGen evaluates 4 tasks with real-robot fine-tuning on 40 demos but covers O(1) scene configurations per task, whereas LocoMimicGen sweeps P×Q×R = 10×3×5 = 150 configurations per primary task (300 total across both primary tasks) — data-efficiency curves across a 150-dimensional configuration space represent a fundamentally different empirical question from per-task success rate at fixed scene coverage, and LocoMimicGen's per-task scene-space depth exceeds both MoMaGen's and HumanoidGen's per-task scene coverage. Baselines: Isaac Lab Mimic PR #3259 (disjoint navigation, closest structural baseline) and Isaac Lab Mimic PR #3992 (position randomization only) are live reproduced baselines. OmniRetarget (arXiv:2509.26633) is included as a conceptual comparison citing its published retargeting fidelity and task-success metrics; although the Holosoma codebase (amazon-far/holosoma) is publicly available, the estimated 10–14 day setup cost for the Holosoma framework and MoCap dataset pipeline exceeds the available bandwidth in the 20-day schedule. DemoHLM (arXiv:2510.11258) is included as a conceptual comparison only, citing its published 10-task evaluation numbers directly; DemoHLM code has not been publicly released as of May 2026, making reimplementation infeasible within the 20-day window. Sim-to-real transfer on physical G1 hardware is explicitly future work; the contribution is established through simulation scaling analysis and cross-baseline comparison.",
  "resource_estimate": {
    "manual": {
      "h100_hours": "~87–110 H100h (≈210h A100 at 2.0–2.5× H100/A100 ratio, plus ~3–5 H100h IRM precomputation): data generation ~30h A100 across 3 tasks at 2048 parallel envs; policy training 3 tasks × 2 seeds × 15h = 90h A100; ablations (3 conditions × 3 tasks × 10h) = 90h A100; total ~210h A100 ÷ 2.5 = 84h H100 (lower bound), ÷ 2.0 = 105h H100 (upper bound), plus IRM precomputation 3–5h H100 = 87–110h H100 total — within 200h H100 constraint",
      "irm_precomputation": "One-time offline: G1 stance-conditioned reachability map construction via IK sampling across ~50K balance configuration poses (6D space: SE(2) base × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab: ~3–5 H100h; amortized across all tasks",
      "gpu_utilization": "High idle (~60–70%): GPU waits on human-paced coding, debugging physics edge cases, and manual analysis between runs",
      "timeline": "2–3 months (2 primary tasks + 1 supplementary reduces contact-rich debug risk; articulated-object task can be deferred if timeline is tight)",
      "team": "2 researchers (1 robotics/sim, 1 IL/policy)",
      "estimated_gpu_cost": "~$370 at $1.75/hr A100 (or ~$220–275 at $2.50/hr H100)",
      "gantt_20day": "20-day critical path (CoRL 2026, paper due May 28 AoE): Days 1–3: IRM precomputation offline (50K-pose IK sampling, embarrassingly parallel in Isaac Lab — low-risk, starts immediately; output blocks Contribution 2 integration). Days 3–7: SE(3) encoding extension — modify Isaac Lab Mimic's segment recording/retargeting API to jointly encode base frame in object's local SE(3) alongside arm end-effector waypoints (critical-path bottleneck: most likely integration debugging hotspot; blocks Contributions 1 and 3). Days 7–12: Combinatorial composition engine — implement three-criterion compatibility filter (IRM feasibility, pose-continuity δ_nav, contact-state); validate on Task 1 (pick-and-place with navigation). Days 12–15: Full data generation runs across all 3 tasks at 2048+ parallel envs (requires Days 1–12 complete). Days 15–19: Diffusion Policy training (CNN-UNet, multi-seed) + ablations across live baselines (Isaac Lab Mimic PR #3259, PR #3992); OmniRetarget and DemoHLM are included as conceptual comparisons with published numbers cited directly — no reimplementation required within this window (requires Day 15 data). Day 19–20: Analysis, scaling-law figures, and write-up. Baseline notes: DemoHLM code is not publicly available as of May 2026 — cited conceptually from arXiv:2510.11258 published results; OmniRetarget (Holosoma) code is public but setup estimated at 10–14 days — designated as conceptual comparison citing arXiv:2509.26633 metrics; if Researcher 2 has bandwidth Days 1–7 before policy training begins, OmniRetarget live reproduction can be attempted as a stretch goal on a parallel track. Risk mitigation: articulated-object task (supplementary) deferred to Days 12–15 alongside primary tasks only if composition engine validation (Days 7–12) completes ahead of schedule; otherwise deferred to post-deadline supplementary material."
    },
    "human_in_loop": {
      "h100_hours": "~125–157 H100h (≈235–310h A100, plus ~3–5 H100h IRM precomputation): data generation ~35h A100; policy training 3 tasks × 2 seeds × 15h = 90h A100; ablations 5 conditions × 3 tasks × 12h = 180h A100 ≈ 305h A100 ÷ 2.5 = 122h H100 (lower bound), ÷ 2.0 = 152h H100 (upper bound), plus IRM precomputation 3–5h H100 = 125–157h H100 total — within 200h H100 constraint",
      "irm_precomputation": "One-time offline: G1 stance-conditioned reachability map construction via IK sampling across ~50K balance configuration poses (6D space: SE(2) base × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab: ~3–5 H100h; amortized across all tasks",
      "gpu_utilization": "Moderate idle (~30–40%): approval gates pause GPU between stages, but agent batches setup and analysis tasks",
      "timeline": "4–5 weeks",
      "team": "1 researcher, ~45 min/day check-in for gate approvals and physics failure triage",
      "claude_api_cost": "$200–400 (~300–500 turns at $0.08–0.12/turn for code gen, debug, analysis)",
      "estimated_gpu_cost": "~$420–540 at $1.75/hr A100 (or ~$310–390 at $2.50/hr H100)",
      "risk_note": "Stance-conditioned IRM for articulated object tasks (door/drawer) involves contact-rich interaction where failure modes require human insight to diagnose; the IRM integration formulation requires iterative design. Addressed by assigning the articulated-object task to supplementary, keeping primary evaluation on the 2 lower-risk tasks.",
      "gantt_20day": "20-day critical path (CoRL 2026, paper due May 28 AoE): Days 1–3: IRM precomputation offline (50K-pose IK sampling, embarrassingly parallel in Isaac Lab — low-risk, starts immediately; output blocks Contribution 2 integration). Days 3–7: SE(3) encoding extension — modify Isaac Lab Mimic's segment recording/retargeting API to jointly encode base frame in object's local SE(3) alongside arm end-effector waypoints (critical-path bottleneck: most likely integration debugging hotspot; blocks Contributions 1 and 3). Days 7–12: Combinatorial composition engine — implement three-criterion compatibility filter (IRM feasibility, pose-continuity δ_nav, contact-state); validate on Task 1 (pick-and-place with navigation). Days 12–15: Full data generation runs across all 3 tasks at 2048+ parallel envs (requires Days 1–12 complete). Days 15–19: Diffusion Policy training (CNN-UNet, multi-seed) + ablations across live baselines (Isaac Lab Mimic PR #3259, PR #3992); OmniRetarget and DemoHLM are included as conceptual comparisons with published numbers cited directly — no reimplementation required within this window (requires Day 15 data). Day 19–20: Analysis, scaling-law figures, and write-up. Baseline notes: DemoHLM code is not publicly available as of May 2026 — cited conceptually from arXiv:2510.11258 published results; OmniRetarget (Holosoma) code is public but setup estimated at 10–14 days — designated as conceptual comparison citing arXiv:2509.26633 metrics. Risk mitigation: articulated-object task (supplementary) deferred to Days 12–15 alongside primary tasks only if composition engine validation (Days 7–12) completes ahead of schedule; otherwise deferred to post-deadline supplementary material."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract May 26 AoE, full paper May 28 AoE / ≈May 29 UTC — 18 days from today)",
    "IEEE Robotics and Automation Letters / RA-L (rolling submission, no hard deadline)"
  ],
  "level": "top-tier",
  "key_references": [
    "MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations (CoRL 2023)",
    "DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning (ICRA 2025)",
    "HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning (NeurIPS 2025)",
    "WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control (ICLR 2026)",
    "OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction (arXiv:2509.26633, Sept 2025)",
    "MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation (ICLR 2026, arXiv:2510.18316)",
    "DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation (arXiv:2510.11258, Oct 2025)",
    "DreamGen: Unlocking Generalization in Robot Learning through Video World Models (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) [GR00T-Dreams blueprint]",
    "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots (NVIDIA, arXiv:2503.14734, March 2025)",
    "EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration (arXiv:2602.10106, Feb 2026, OpenDriveLab)",
    "HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstrations (arXiv:2603.03243, March 2026, Stanford/TRI)",
    "HuMI: Humanoid Manipulation Interface — Humanoid Whole-Body Manipulation from Robot-Free Demonstrations (arXiv:2602.06643, Feb 2026)",
    "HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos (arXiv:2602.02473, Feb 2026)",
    "VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation (arXiv:2509.20322, IROS 2025)",
    "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion (Chi et al., RSS 2023 / IJRR 2025, arXiv:2303.04137)",
    "Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning (arXiv 2025)",
    "Isaac Lab PR #3150: Locomanipulation Environment with G1 for Mimic workflow (merged Sept 9, 2025)",
    "Isaac Lab PR #3259: Adds locomanipulation data generation via disjoint navigation (merged Sept 10, 2025, release/2.3.0)",
    "Isaac Lab PR #3992: APIs to Isaac Lab Mimic for supporting loco-manipulation datagen (merged Dec 1, 2025)",
    "Vahrenkamp et al.: Robot Placement based on Reachability Inversion (ICRA 2013)",
    "Burget et al.: Stance Selection for Humanoid Grasping Tasks by Inverse Reachability Maps (ICRA 2015)",
    "MoMa-Pos: An Efficient Object-Kinematic-Aware Base Placement Optimization Framework for Mobile Manipulation (arXiv:2403.19940, Oct 2024 revision, ICRA 2025)",
    "Murooka et al.: Humanoid Loco-manipulation Planning based on Graph Search and Reachability Maps (arXiv:2505.23505, May 2025)",
    "Murooka et al.: Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation (arXiv:2508.11275, Humanoids 2025)"
  ],
  "description": "LocoMimicGen extends Isaac Lab's 2.3 loco-manipulation infrastructure — comprising PRs #3150, #3259, and #3992 — with three precisely-scoped technical contributions that together enable room-level combinatorial scaling unavailable in existing systems.\n\nPR #3259 ('disjoint navigation', merged Sept 10, 2025, release/2.3.0) is the closest structural predecessor and primary baseline. It adds pick-navigate-place phase segmentation with occupancy-map path planning between phases and scene randomization. However, it handles navigation 'disjointly': the manipulation stance is fixed from the source demo and navigation is occupancy-map path planning at the trajectory level. It does NOT encode navigation stances in the object's SE(3) local frame, does NOT enforce arm-reachability constraints on base-pose selection (making generation infeasible when new object positions fall outside source demo stance's arm workspace), and does NOT compose segments from multiple source demonstrations.\n\nContribution (1): By expressing the manipulation stance in the object's SE(3) local frame alongside the arm trajectory, frame-transform retargeting to new object configurations automatically yields a feasible new stance without any separate stance-placement planning. Navigation between the retargeted stances is handled by the pretrained RL locomotion controller (PR #3150) as a black box; what the SE(3) encoding eliminates is the need to separately determine where the robot should stand to manipulate at each new object configuration. LocoMimicGen adds coupled SE(3) object-centric encoding of locomotion stances jointly with arm end-effector waypoints — the principled replacement for PR #3259's disjoint approach, enabling frame-transform retargeting of both manipulation stances and arm motions simultaneously.\n\nContribution (2): Stance-conditioned IRM integration for bipedal humanoid retargeting. We adapt and integrate IRM methodology (Vahrenkamp et al. 2013; Burget et al. ICRA 2015; MoMa-Pos 2024; MoMaGen ICLR 2026) into the Mimic retargeting loop for the G1. The integration challenge over prior wheeled-platform IRMs (MoMa-Pos, MoMaGen) is that bipedal arm reachability is conditioned on whole-body stance configuration (COM height, foot contact, balance state), requiring a stance-conditioned reachability map rather than a SE(2) base-pose-only map. The reachability map is a one-time offline precomputation (~3–5 H100-hours for IK sampling across ~50K balance configuration poses in 6D space: SE(2) base pose × squat depth × foot spread × weight distribution), GPU-parallel in Isaac Lab, shared across all tasks, and explicitly budgeted in the resource estimate. A concurrent technique from the same CNRS-AIST group (Murooka et al., arXiv:2508.11275, Humanoids 2025) introduces learned differentiable reachability maps for online gradient-based humanoid planning; LocoMimicGen uses offline-precomputed discrete IRM instead, as differentiable map gradient evaluation across 2048+ parallel Isaac Lab environments would bottleneck batch generation throughput. This is framed as an integration contribution — not a novel technique — with the bipedal stance-conditioning as the key technical challenge.\n\nContribution (3): Combinatorial multi-source segment composition from multiple (≤20 total) teleoperated demonstrations achieves 100–1,000× demo expansion — a qualitatively different scaling regime from PR #3259's single-source disjoint augmentation. The scaling bound is explicit: with K=20 source demonstrations decomposed into M=3 subtask phases, combined with P=10 object positions × Q=3 table heights × R=5 obstacle layouts, the conservative lower bound is K×M×P×Q×R = 20×3×10×3×5 = 9,000 unique trajectories (450× expansion from 20 seed demos); full cross-phase composition yields K^M × P×Q×R = 20^3 × 150 ≈ 1.2M as the theoretical maximum. Compatibility between segments from different source demonstrations is evaluated against three criteria: (1) IRM feasibility at the transition stance (IRM score exceeding the 10th percentile of source-demo scores); (2) base-pose continuity within δ_nav ≈ 0.3 m (the locomotion controller's recoverable displacement); (3) contact-state consistency at phase boundaries. Criteria (1) and (2) are the active filters: IRM feasibility eliminates ~55–75% of random scene-stance pairings, and pose continuity a further 10–20%, reducing the 1.2M theoretical bound to the practical 100–1,000× range (roughly 2,000–20,000 valid trajectories from 20 seed demos).\n\nAll policy training uses Diffusion Policy (CNN-UNet variant, Chi et al. RSS 2023 / IJRR 2025) uniformly across all baselines and LocoMimicGen conditions, isolating the data-generation contribution. We target ≥20 pp mean success-rate improvement over PR #3259 at the held-out 150-configuration test distribution, grounded in MimicGen's 20–40 pp gains on harder spatial-variant distributions where baselines already incorporate partial scene randomization.\n\nMoMaGen (ICLR 2026, arXiv:2510.18316) generates bimanual mobile manipulation demonstrations via hard-reachability-constrained optimization on a wheeled bimanual platform — now the strongest peer-reviewed comparison point for constrained demo generation. The differentiation is precise: MoMaGen's reachability constraint operates over SE(2) base pose for a wheeled platform where base pose fully determines arm workspace; LocoMimicGen's stance-conditioned IRM addresses the qualitatively harder bipedal case where arm reachability is conditioned on whole-body configuration. DreamGen (NVIDIA GEAR Lab, arXiv:2505.12705, May 2025) — the GR00T-Dreams blueprint — generates behavioral generalization across task types via video world-model sampling and IDM action recovery; LocoMimicGen generates spatial/configurational diversity within known loco-manipulation tasks via constraint-based combinatorial recombination with hard kinematic guarantees. The two approaches are complementary: DreamGen's world-model-imagined behavioral diversity and LocoMimicGen's constraint-verified spatial diversity address orthogonal dimensions of the data scarcity problem. EgoHumanoid (OpenDriveLab, arXiv:2602.10106, Feb 2026), HoMMI (arXiv:2603.03243, March 2026), HuMI (arXiv:2602.06643, Feb 2026), and HumanX (arXiv:2602.02473, Feb 2026) represent concurrent policy-learning paradigms — learning from human behavioral diversity in real environments (video, MoCap, egocentric demonstrations) to improve generalization — complementary to LocoMimicGen's combinatorial spatial synthesis from ≤20 robot demos in simulation.\n\nEvaluated on 2 primary loco-manipulation tasks (pick-and-place with navigation; two-phase transit) plus 1 supplementary articulated-object task. Live reproduced baselines: Isaac Lab Mimic PR #3259 (closest structural baseline) and PR #3992. Conceptual comparisons citing published numbers: OmniRetarget (arXiv:2509.26633; Holosoma code is public but 10–14 day setup exceeds the 20-day window) and DemoHLM (arXiv:2510.11258; code not publicly available as of May 2026). The 2-primary scope is proactively justified on four grounds against DexMimicGen (9 tasks), HumanoidGen (6 tasks, 120+ scene variants), and MoMaGen (ICLR 2026, 4 tasks): (a) scaling law curves across P×Q×R configuration space are the primary empirical contribution, fully established on 2 tasks; (b) both primary tasks exercise all three contributions; (c) DexMimicGen's breadth reuses fixed tabletop infrastructure vs. LocoMimicGen's IRM integration into a live loco-manipulation stack; (d) LocoMimicGen sweeps P×Q×R = 150 configurations per primary task (300 total), exceeding MoMaGen's and HumanoidGen's per-task scene coverage — scene-space depth is the appropriate metric for a data-generation infrastructure paper. Both compute modes (manual: ~87–110h H100; human-in-loop: ~125–157h H100) stay within the 200 H100-hour hard constraint, including the one-time IRM precomputation (~3–5 H100h). The 20-day critical path (IRM precomputation Days 1–3 → SE(3) encoding Days 3–7 → composition engine Days 7–12 → data generation Days 12–15 → policy training Days 15–19 → write-up Day 19–20) is explicitly identified; the SE(3) API integration (Days 3–7) is the critical-path bottleneck. Sim-to-real on physical G1 is explicit future work. CoRL 2026: abstract May 26 AoE, paper May 28 AoE.",
  "project_name": "loco_mimicgen_humanoid_g1",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL NOVELTY GAP: The generator missed two merged Isaac Lab PRs that directly undermine the core claim. PR #3150 (merged Sept 9, 2025) added Isaac-PickPlace-Locomanipulation-G1-Abs-v0, a G1 Mimic environment combining RL locomotion with IK manipulation, achieving 92% success on pick-and-place. PR #3992 (merged Dec 1, 2025) added APIs to Isaac Lab Mimic specifically for loco-manipulation data generation, including treating the robot's base as an end-effector in the Mimic framework — exactly what the generator claims is missing. The documentation states the system 'parses demonstrations into object-centric subtask segments, then adapts these subtask segments to new scenes by transforming each segment according to the new scene's context,' directly contradicting the generator's claim that Isaac Lab lacks 'principled SE(3) demo transformation.'", "HARD COMPUTE CONSTRAINT VIOLATED: Auto-research mode (~900h A100) converts to ~300–450h H100 at confirmed 2–3x H100/A100 ratio, violating the 200 H100-hour hard constraint by 50–125%. Human-in-loop (~420h A100 ≈ 140–210h H100) is also borderline. The generator expressed all estimates in A100 hours without converting to H100 hours, despite the user requirement being explicitly stated in H100 hours.", "DemoHLM (arXiv:2510.11258) already applies MimicGen-style object-centric data generation to 10 G1 loco-manipulation tasks with sim-to-real transfer on physical G1. The generator acknowledged this but downplayed its scope (calling it 'single-object tasks' and saying it 'does not exploit combinatorial segment composition across room-level layout diversity'). The paper should verify whether DemoHLM's 10 tasks actually include multi-stage tasks before making this claim.", "Physical G1 hardware for sim-to-real experiments is listed as a required evaluation component but hardware access is nowhere addressed in the resource plan. Without a G1 robot, the sim-to-real evaluation collapses to sim-only, which reduces CoRL competitiveness.", "CoRL 2026 deadline discrepancy: the generator states abstract deadline May 25 and paper deadline May 28, but the official CoRL 2026 website confirms abstract May 26 (UTC) and paper May 29 (UTC). Minor but worth correcting.", "The kinodynamic planner with coupled arm-reachability constraints for a bipedal humanoid is treated as a subordinate engineering task, but this is itself a non-trivial research contribution. No existing open-source planner directly handles coupled navigation + manipulation reachability for bimanual bipedal systems; implementing one from scratch within 20 days is highly aggressive.", "MoMaGen (arXiv:2510.18316, Oct 2025) targets a wheeled bimanual mobile base (not a bipedal humanoid), so the generator's differentiation from it is valid — but the generator should verify whether MoMaGen's constrained-optimization approach can be straightforwardly extended to bipedal locomotion, as reviewers will ask this."]
Feedback: The idea targets a real gap but needs substantial repositioning before it can pass review. The most urgent fix: the generator must engage directly with Isaac Lab Mimic's loco-manipulation extensions (PRs #3150 and #3992, https://github.com/isaac-sim/IsaacLab/pull/3150 and /pull/3992), which already implement MimicGen-style object-centric loco-manipulation data generation for the G1. The generator must explain precisely what these PRs do NOT do: specifically, (a) their navigation handling simply repeats the last navigation action or waits for goal-reached — it does NOT encode navigation waypoints in the object's SE(3) local frame jointly with arm trajectories; (b) they do not perform kinodynamic replanning with arm-reachability enforcement; (c) they do not combinatorially compose segments from multiple source demonstrations to achieve room-level diversity. These three differentiators are real and should become the paper's explicit contribution claims, stated against Isaac Lab Mimic as the primary baseline (not just 'Isaac Lab 2.3'). Second: fix compute estimates. All GPU estimates must be expressed in H100-hours. The auto-research mode must be scoped down or removed — at current scope it exceeds the 200 H100-hour hard constraint by 2x. A plausible manual scope: 2–3 tasks instead of 5–8, fewer ablation variants, single policy architecture. Third: either secure physical G1 access and state it explicitly, or replace 'sim-to-real on physical G1' with 'sim-only evaluation against DemoHLM and Isaac Lab Mimic baselines' and note hardware as future work. The core idea — coupling SE(3) navigation waypoint encoding with manipulation trajectory retargeting, plus kinodynamic reachability enforcement, to enable room-level combinatorial scaling beyond Isaac Lab Mimic's position randomization — is a legitimate and novel contribution; it just needs to be positioned honestly against the specific infrastructure that already exists.

### Round 2 review
Verdict: revise
Issues: ["MISSED BASELINE — Isaac Lab PR #3259 ('Adds locomanipulation data generation via disjoint navigation', merged Sept 10 2025 into release/2.3.0): This PR is part of the Isaac Lab 2.3 GA release and adds (a) pick-navigate-place phase segmentation, (b) occupancy-map-based path planning between phases, and (c) scene randomization of tabletop object positions, navigation destinations, and floor obstacles. This makes it a closer predecessor to LocoMimicGen than PRs #3150/#3992 alone, and CoRL reviewers will notice its absence. The generator must add PR #3259 to the baseline comparison and explain precisely what it does NOT provide: no SE(3) encoding of navigation stances in the object's local frame, no arm-reachability-constrained base-pose optimization, and no combinatorial composition from multiple source demonstrations — only disjoint occupancy-map navigation replayed between fixed teleoperated manipulation segments.", "NOVELTY FRAMING OVERREACH for Contribution 2: Reachability-map-guided base-pose optimization is a well-established technique (inverse reachability maps: Vahrenkamp et al. 2013, Reuleaux, MoMa-Pos Oct 2024). In the demo generation context, MoMaGen (Oct 2025) already imposes reachability as a hard constraint for wheeled bimanual base-pose sampling. The paper must reframe Contribution 2 not as a standalone novel technique but as an INTEGRATION contribution: applying IRM within the Mimic retargeting loop for a bipedal humanoid, where balance constraints make the reachability map qualitatively more complex than for wheeled platforms (it is a function of stance configuration, not just base position). Without this reframing, CoRL reviewers will mark it as 'known technique applied straightforwardly.'", "TIMELINE RISK: Three technically non-trivial contributions (SE(3) extension, IRM integration, combinatorial composition) implemented within Isaac Lab Mimic, plus 3-task data generation, diffusion policy training over multiple seeds, and ablation studies, in 20 days with 2 researchers is at the edge of plausibility. The contact-rich articulated-object tasks (door/drawer) for IRM optimization are specifically flagged as likely to consume disproportionate debug time. The paper should include a concrete task-level schedule or explicitly narrow scope to 2 tasks with the third as supplementary if the timeline proves infeasible.", "RESOURCE ESTIMATE INTERNAL CONSISTENCY: The manual mode GPU cost estimate ($370 at $1.75/hr A100) implies ~210h A100, but the H100 conversion given is 60–105h H100. At a 2–2.5× ratio, 210h A100 ÷ 2.5 = 84h H100 and ÷ 2.0 = 105h H100. The lower bound (60h H100) would require a 3.5× ratio, which exceeds the stated conversion factor. The estimate is within the hard constraint but the lower bound is implausibly optimistic — reviewer should note this minor inconsistency."]
Feedback: The Round 2 revision correctly addresses all Round 1 critical issues: PRs #3150/#3992 are now the explicit primary baseline with accurate technical characterization; compute is expressed in H100 hours and within the 200h constraint; sim-to-real hardware is properly scoped as future work; and CoRL deadline is corrected. The idea is solid and close to passable — two targeted fixes are needed.

**Fix 1 (required for CoRL submission)**: Add Isaac Lab PR #3259 to the related work and baseline comparison. PR #3259 ('disjoint navigation', merged Sept 10 2025) is in the Isaac Lab 2.3 GA release. It adds pick-navigate-place segmentation with occupancy-map path planning and scene randomization for G1 loco-manipulation. Write one paragraph explaining exactly what PR #3259 does vs. does not do: it uses path planning between disjoint manipulation phases but (a) does NOT encode navigation stances in the object's SE(3) local frame — navigation is path-level, not object-centric; (b) does NOT enforce arm reachability constraints on base pose selection — the manipulation stance is fixed from the source demo; (c) does NOT compose segments from multiple source demonstrations. This makes PR #3259 a closer prior art than #3992 alone, and explaining the gap against it sharpens LocoMimicGen's contributions significantly.

**Fix 2 (required for reviewer credibility)**: Reframe Contribution 2 as an integration contribution, not a novel technique. Cite the IRM literature (Vahrenkamp et al., MoMa-Pos, MoMaGen) and explain that the challenge for bipedal humanoids is that the arm reachability map is conditioned on whole-body stance (including COM height and balance state), making the IRM higher-dimensional and configuration-dependent compared to wheeled platforms. Position it as 'we adapt and integrate existing IRM methodology into the Mimic retargeting loop for bipedal humanoids, which requires a stance-conditioned reachability map not present in prior wheeled-base work.' This is honest, defensible, and still a real contribution.

**Optional (reduces timeline risk)**: Reduce to 2 primary tasks + 1 supplementary task to create schedule slack for articulated-object IRM debugging. This keeps all three contributions but limits per-task ablation surface.

### Round 3 review
Verdict: revise
Issues: ["MISSING CONCURRENT WORK IN LANDSCAPE: EgoHumanoid (arXiv 2602.10106, Feb 2026, OpenDriveLab) is listed as a key reference but receives zero discussion in the landscape section. CoRL reviewers will notice. Add one paragraph: EgoHumanoid addresses loco-manipulation data scarcity via VLA co-training with human egocentric demonstrations — a fundamentally different paradigm (data co-training) from LocoMimicGen's procedural demo multiplication. They are complementary: EgoHumanoid augments training distribution through human data; LocoMimicGen augments through combinatorial scene synthesis. The two could in principle be combined.", "UNSUBSTANTIATED SCALING CLAIM: The '100-1000× demo expansion from ≤20 seed demonstrations' claim has no supporting formula or derivation. CoRL reviewers will ask: if you have K=20 demos decomposed into M subtask segments, and you apply combinatorial composition across P object positions × Q table heights × R obstacle layouts, what is the actual upper bound on unique valid trajectories? Provide the combinatorial formula explicitly. If composition is not fully free (some segment pairs are incompatible), state the compatibility constraint and how it affects the scaling factor. Claim credibility depends on making this concrete.", "IRM PRECOMPUTATION COST NOT BUDGETED: The approach requires pre-computing a stance-conditioned upper-body reachability map for the G1 across a distribution of balance configurations (COM height, foot contact pattern, balance state). For bipedal systems this is a ≥6D workspace sampling problem (x, y, θ, squat depth, foot spread, weight distribution), substantially more expensive than the 3D SE(2) maps used in MoMa-Pos and MoMaGen. The H100 cost of this precomputation step (IK sampling across balance configuration space) is entirely absent from the resource estimate. Even if amortized as a one-time offline cost, it should be quantified explicitly — e.g., '3–5 H100-hours for G1 reachability map construction at N-resolution grid.' This could push the manual mode estimate past 105h H100.", "TWO-TASK EVALUATION NEEDS EXPLICIT JUSTIFICATION: CoRL reviewers comparing against DexMimicGen (9 tasks across 3 embodiments) and HumanoidGen (120+ scene variants across 6 tasks) will see 2 primary tasks as limited. The paper must proactively address this: (a) the scaling law (demo efficiency curves showing 100-1000× expansion) is the empirical question, not task breadth; (b) each primary task fully exercises all three contributions; (c) the 20-day timeline constraint motivates depth over breadth. Without this defense, reviewers will request more tasks as a condition of acceptance.", "CONTRIBUTION 1 CRYSTALLIZATION MISSING: The core SE(3) insight — that encoding the robot base pose (stance) in the same object-centric frame as the arm end-effector trajectory makes retargeting to new object positions move both arm AND navigation stance jointly via a single frame transform — should be stated as a one-sentence crystallization early in the contribution description. Currently it takes 3 paragraphs to convey what could be said in one sentence: 'By expressing the manipulation stance in the object's SE(3) local frame alongside the arm trajectory, frame-transform retargeting to new object configurations automatically yields valid stances without any separate navigation planning.' This clarity would significantly strengthen how reviewers perceive Contribution 1's insight."]
Feedback: Round 3 has successfully addressed all critical Round 1-2 issues: PR #3259 is now the primary baseline with accurate technical characterization; Contribution 2 is properly reframed as integration; scope is 2 primary + 1 supplementary; compute is within 200h H100; CoRL deadlines are correct. The idea is now technically solid and close to passable — four targeted fixes will bring it to pass.

**Fix 1 (required, 1 paragraph)**: Add EgoHumanoid (arXiv 2602.10106, Feb 2026) to the landscape. Explain it uses VLA co-training with egocentric human data — a different paradigm from procedural demo multiplication — making it complementary. This is a concurrent 2026 G1 loco-manipulation paper and omitting it from related work will cause a reviewer flag.

**Fix 2 (required, 3-4 sentences)**: Provide the combinatorial scaling formula. State explicitly: with K source demos, M subtask segments per demo, and a configuration space of P×Q×R (object positions × table heights × obstacle layouts), the upper bound on unique trajectories is approximately K×M×P×Q×R, and with K=20, M=3, P=10, Q=3, R=5 this yields ~9,000 trajectories from 20 demos — a 450× expansion. Make it concrete and verifiable.

**Fix 3 (required, estimate update)**: Add a line item to the resource estimate for G1 reachability map precomputation. Even if small (e.g., 2-4 H100-hours for offline IK sampling at 50K poses across balance configuration space), its omission will look like an oversight to robotics reviewers who understand the dimensionality involved.

**Fix 4 (optional but strongly recommended)**: Write the one-sentence crystallization of Contribution 1's core insight (suggested above) as the opening sentence of that contribution's description. This is what reviewers remember and cite — make it quotable.

### Round 4 review
Verdict: revise
Issues: ["VENUE UPDATE REQUIRED — MoMaGen is published at ICLR 2026 (confirmed at jiajunwu.com/papers/momagen_iclr.pdf and openreview.net/forum?id=bGPDviEtZ1), not merely 'arXiv Oct 2025' as cited throughout the landscape and approach sections. CoRL 2026 reviewers will know MoMaGen is a peer-reviewed ICLR 2026 paper and will treat its coverage of hard-reachability-constrained demo generation for mobile manipulation as a stronger prior work. Update all references to MoMaGen to include its ICLR 2026 venue. The differentiation (SE(2) wheeled base vs. whole-body stance-conditioned bipedal IRM) remains valid, but must be argued against a venue-placed competitor.", "MISSING RELATED WORK — 'Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation' (arXiv:2508.11275, Humanoids 2025) by Murooka et al. (the same CNRS-AIST group as the cited Murooka 2505.23505) introduces learned differentiable reachability maps specifically for humanoid footstep planning and loco-manipulation planning via continuous optimization. The generator cites the same group's graph-search paper (2505.23505) but omits this August 2025 Humanoids paper which is more directly related to Contribution 2. CoRL reviewers who know the Murooka group's work will notice. Add a brief comparison: LocoMimicGen uses offline-precomputed discrete IRM for a data-generation retargeting loop (different use case from online motion planning), making discrete maps preferable for the batch-generation context where online optimization would be prohibitively expensive at 2048+ parallel environments.", "COMPATIBILITY FILTERING UNDEFINED — The practical 100–1,000× scaling range is derived by applying 'compatibility filtering' to reduce the theoretical upper bound (K^M × P×Q×R ≈ 1.2M), but the paper never defines what makes two subtask segments incompatible. CoRL reviewers will ask: Is compatibility based on pose overlap between consecutive stance poses? Reachability threshold at the IRM? Contact state consistency? Kinematic continuity at phase boundaries? Without a formal compatibility criterion and an empirical estimate of the filtering rate (e.g., 'X% of cross-phase compositions pass compatibility'), the 100–1,000× claim reads as an unconstrained assertion. Add 3–4 sentences specifying the compatibility check (e.g., IRM feasibility of the concatenated stance sequence + pose continuity tolerance) and the expected filtering rate.", "UNCITED CONCURRENT 2026 WORK — HoMMI (arXiv:2603.03243, March 2026, Stanford/TRI) and HuMI (arXiv:2602.06643, Feb 2026) both address whole-body mobile manipulation from human demonstrations with real-robot validation on bipedal or mobile humanoid platforms. Neither is a direct competitor (both are policy-learning paradigms, not procedural demo multiplication), but their omission is conspicuous given that EgoHumanoid is already cited. Add one sentence each: 'HoMMI and HuMI [cite] learn whole-body manipulation from egocentric human demos on mobile platforms — a data-collection paradigm complementary to LocoMimicGen's combinatorial synthetic-data generation from ≤20 teleoperated robot demos.' This demonstrates landscape awareness without diluting the contribution framing.", "EVALUATION BREADTH vs. ICLR 2026 BASELINE — MoMaGen's ICLR 2026 acceptance gives it credibility as the comparison anchor for constrained demo-generation methods. MoMaGen evaluates on 4 tasks with real-robot fine-tuning on 40 demos; HumanoidGen covers 6 tasks with 120+ scene variants. LocoMimicGen's 2-primary-task scope and sim-only evaluation now looks noticeably thinner against this peer bar. The existing pre-emption argument ('scaling curves are the primary contribution') is present but understated. Strengthen it: explicitly state that LocoMimicGen's K×M×P×Q×R combinatorial sweep at fixed task depth exceeds MoMaGen's and HumanoidGen's scene diversity, and that data-efficiency curves across the full P×Q×R configuration space represent a fundamentally different empirical question than per-task success rate across many tasks."]
Feedback: Round 4 has successfully resolved all Round 3 issues: EgoHumanoid appears prominently in the landscape with accurate complementary framing; the K×M×P×Q×R combinatorial formula (450× conservative, 1.2M theoretical) is explicit and verifiable; the IRM precomputation budget (3–5 H100h) is itemized; and the Contribution 1 one-sentence crystallization is present and quotable. The technical approach is coherent, the primary baseline (PR #3259) is precisely characterized, and the compute estimate is verified within the 200 H100h constraint.

**Fix 1 (required, bibliographic)**: Update MoMaGen throughout from 'arXiv:2510.18316, Oct 2025' to 'MoMaGen (ICLR 2026, arXiv:2510.18316).' This is a factual correction. The differentiation argument (SE(2) wheeled vs. whole-body bipedal stance-conditioned IRM) remains fully valid — just state it explicitly against an ICLR-published baseline.

**Fix 2 (required, 2–3 sentences)**: Add Murooka et al. 'Learning Differentiable Reachability Maps' (arXiv:2508.11275, Humanoids 2025) to the IRM discussion. Explain that differentiable maps are optimal for online planning but that offline discrete IRM precomputation is preferred in LocoMimicGen's batch data-generation loop, where online optimization would be intractable at 2048+ parallel Isaac Lab environments. Position it as a complementary technique rather than a conflicting one.

**Fix 3 (required, 3–4 sentences in Approach section)**: Formalize the compatibility filtering criterion. Specify what defines an incompatible segment pair (e.g., IRM infeasibility of the terminal stance pose for the incoming segment, or Euclidean distance between the terminal base pose of phase i and the initial stance pose of phase i+1 exceeding a threshold δ). Provide an empirical estimate or upper bound on the filtering rate to make the 100–1,000× range verifiable rather than asserted.

**Fix 4 (optional, 1 sentence each)**: Add HoMMI (2603.03243) and HuMI (2602.06643) as complementary paradigms alongside EgoHumanoid in the landscape.

**Fix 5 (recommended, 2 sentences)**: Strengthen the 2-task evaluation defense by explicitly comparing scene-space coverage: LocoMimicGen sweeps P×Q×R = 10×3×5 = 150 scene configurations per task (two primary tasks = 300 total), whereas MoMaGen and HumanoidGen each cover O(1) scene variants per task at larger task breadth. Frame this as a deliberate methodological choice to probe depth of the data-efficiency curve rather than per-task breadth.

### Round 5 review
Verdict: revise
Issues: ["MISSING FROM LANDSCAPE — GR00T-Dreams/GR00T-Mimic (NVIDIA, March 2025): The user's stated 'recent landscape (do not duplicate)' explicitly lists 'NVIDIA GR00T-Dreams' alongside Cosmos, yet this paper's landscape and related-work sections contain zero discussion of it. CoRL 2026 reviewers — who will include NVIDIA-adjacent researchers given Isaac Lab is NVIDIA infrastructure — will notice this omission immediately. GR00T-Dreams uses video diffusion (Cosmos-Predict2) + inverse dynamics models to generate trajectories from a single image + language prompt, enabling zero-shot behavior generalization; it is a fundamentally different paradigm (learned generative model) from LocoMimicGen's constraint-based procedural recombination. Add 2–3 sentences differentiating: 'GR00T-Dreams generates synthetic trajectories via video world-model sampling from a single image prompt — a complementary learned-generative paradigm. LocoMimicGen's constraint-based combinatorial recombination provides hard physical feasibility guarantees (IRM feasibility + pose continuity + contact consistency) that learned world models cannot yet enforce at per-joint kinematic precision for bipedal loco-manipulation.'", "EVALUATION LACKS EXPECTED EFFECT SIZES: The paper states a diffusion policy is trained per task and success rates are reported, but provides no target effect size or predicted improvement magnitude over the primary baseline (PR #3259). CoRL reviewers will ask: what is the expected delta in task success rate between a policy trained on 20 seed demos vs. one trained on LocoMimicGen-generated trajectories at 450× expansion? Without a predicted range (e.g., 'we target ≥15 pp improvement over PR #3259 baseline at the 150-configuration test distribution'), the empirical contribution reads as 'generate data and see what happens.' Add a brief quantitative prediction grounded in prior MimicGen scaling results (MimicGen's original 2023 paper showed ~25 pp improvement at 100× expansion on tabletop tasks) to anchor reviewer expectations.", "POLICY ARCHITECTURE UNDERSPECIFIED: The evaluation section states 'a diffusion policy is trained per task' without specifying the architecture (Diffusion Policy Chi et al. 2023? ACT? π₀?). CoRL reviewers will ask whether the choice of policy architecture could confound the data-efficiency comparison — a policy with strong priors may be less sensitive to data diversity. Specify the architecture in one sentence and justify the choice as consistent across all baselines.", "TIMELINE RISK STILL PRESENT: Three technically non-trivial engineering contributions (SE(3) extension of Isaac Lab Mimic's existing representation, IRM precomputation at 50K poses in 6D configuration space + integration into the retargeting loop, combinatorial composition engine with 3-criterion compatibility filtering) plus multi-seed policy training and ablation studies in 20 days with 2 researchers remains at the edge of plausibility. The articulated-object supplementary deferral helps but the primary 2-task scope still involves all three contributions operating together. Consider adding a concrete 20-day Gantt chart or milestone schedule to the approach section to demonstrate that the team has identified the critical path and is not underestimating integration debug time."]
Feedback: Round 5 has successfully resolved all Round 4 issues: MoMaGen is correctly cited as ICLR 2026 throughout; Murooka et al. 2508.11275 (differentiable reachability maps) is properly discussed with the offline-precomputed-discrete-IRM-vs-online-differentiable-map distinction; compatibility filtering is formalized with three explicit criteria (IRM feasibility, pose continuity within δ_nav ≈ 0.3 m, contact-state consistency) and empirical filtering rates; HoMMI and HuMI are included as complementary paradigms; and the P×Q×R = 150-configuration-per-task scene-depth argument is now stated explicitly as the appropriate metric for a data-generation infrastructure paper. The technical foundation is solid.

**Fix 1 (required, 2–3 sentences in landscape)**: Add GR00T-Dreams/GR00T-Mimic to the landscape. The differentiator is clear and defensible: GR00T-Dreams is a learned generative approach (video diffusion + IDM action labeling) that provides behavioral diversity through world-model imagination but cannot enforce hard kinematic feasibility constraints per joint. LocoMimicGen's procedural recombination with IRM feasibility and pose continuity filters provides hard physical guarantees that learned world models currently cannot. This is complementary, not competing — say so explicitly.

**Fix 2 (required, 1–2 sentences)**: Add a target effect size to the evaluation section. Ground it in MimicGen's original scaling results as a prior: MimicGen (CoRL 2023) showed ~20–30 pp success-rate improvement at 100× data expansion on tabletop tasks. LocoMimicGen targets ≥X pp improvement over PR #3259 at 150-configuration test distributions — state a concrete floor. This anchors reviewer expectations and signals that the team has thought through the empirical hypothesis.

**Fix 3 (required, 1 sentence)**: Specify the diffusion policy architecture used in all experiments, justifying the choice as consistent across baselines. Diffusion Policy (Chi et al. 2023, UMI) or ACT are both reasonable; either is defensible if applied uniformly.

**Fix 4 (optional but recommended)**: Add a 20-day implementation milestone schedule to the approach or resource section. Identify the critical path (IRM precomputation Day 1–3 → SE(3) encoding integration Day 3–7 → combinatorial composition Day 7–12 → data generation runs Day 12–15 → policy training Day 15–19 → writeup Day 19–20) and flag which milestones block others. This demonstrates execution awareness and pre-empts timeline-feasibility objections.

### Round 6 review
Verdict: revise
Issues: ["BASELINE FEASIBILITY FAILURE — DemoHLM (arXiv:2510.11258): Code is NOT publicly available as of May 2026 (7+ months post-publication, no GitHub repository found despite extensive search). Re-implementing DemoHLM's stage-level command adaptation from scratch is a 20-30 day effort for an unfamiliar team — it cannot serve as a live baseline within the 20-day window. The submission must either: (a) remove DemoHLM from the comparison table and position it as a conceptual comparison only, citing the paper's reported numbers directly; or (b) implement a simplified DemoHLM surrogate (stage-level base-command modification without the full hierarchical controller) within 2-3 days and acknowledge it as an approximation. Leaving DemoHLM as a listed baseline without addressing code availability is a submission risk — a reviewer who asks for DemoHLM results will expose this gap.", "CONTRIBUTION 1 LANGUAGE IMPRECISION — 'without any separate navigation planning': The crystallization sentence ('frame-transform retargeting to new object configurations automatically yields a feasible new stance without any separate navigation planning') is technically imprecise in a way that CoRL robotics reviewers will notice. The SE(3) encoding eliminates the need for STANCE SELECTION (i.e., it computes WHERE the robot should stand to manipulate at a new object position), but navigation to those stances still requires the RL locomotion controller (PR #3150) to traverse the path. The correct claim is 'without any separate stance planning' — the frame transform directly yields the target manipulation stance, and the navigation between stances is handled by the pretrained RL controller as a black box. As written, 'without any separate navigation planning' mischaracterizes how locomotion navigation segments are handled and will invite reviewer pushback. Fix: change 'navigation planning' to 'stance-placement planning' throughout.", "MISSING CITATION — HumanX/XMimic (arXiv:2602.02473, Feb 2026): This concurrent paper introduces 'XMimic' — a unified imitation learning framework for humanoid loco-manipulation from video synthesis — and 'XGen' data generation pipeline. The name 'XMimic' will catch reviewers' attention given LocoMimicGen's positioning. The approaches are orthogonal (HumanX learns from human video via dynamics augmentation; LocoMimicGen generates from teleoperated demos via procedural composition), but the omission is conspicuous. Add one sentence to the landscape placing HumanX alongside EgoHumanoid/HoMMI/HuMI as a video-based data-collection paradigm complementary to LocoMimicGen's procedural simulation synthesis.", "OROMRETARGET BASELINE SETUP COMPETES WITH MAIN ENGINEERING: OmniRetarget code (amazon-far/holosoma) is public with public datasets (LAFAN1, OMOMO), making it theoretically runnable. However, setting up the Holosoma framework + MoCap datasets + running the retargeting pipeline is estimated at 10-14 days for a competent team. In a 20-day schedule where Days 3-12 are consumed by SE(3) encoding + composition engine development, there is no realistic window to also set up OmniRetarget as a live baseline. The submission should either (a) designate OmniRetarget as a conceptual comparison (citing published task success numbers) rather than a reproduced baseline, or (b) assign it to a parallel track with explicit person-assignment in the Gantt chart (Researcher 2 handles OmniRetarget setup Days 1-7 in parallel with IRM precomputation)."]
Feedback: Round 6 has successfully resolved all Round 5 required fixes: DreamGen/GR00T-Dreams is properly contextualized as a complementary learned-generative approach, the ≥20pp effect-size floor is explicitly grounded in MimicGen's scaling results, Diffusion Policy (CNN-UNet) is specified uniformly, and day-by-day Gantt charts are present in both modes. The idea is technically sound, the gap against PR #3259 is precisely characterized, and the differentiation against MoMaGen (ICLR 2026) holds. Two issues require targeted fixes before submission:

**Fix 1 (required, blocks submission credibility)**: Resolve the DemoHLM baseline. Code is not public. Choose one approach: (a) Replace DemoHLM as a live baseline with a conceptual comparison — cite the paper's published numbers for its 10-task evaluation and note code is unavailable; or (b) implement a 2-3 day simplified DemoHLM surrogate (fix object pose, modify navigation command magnitude, replay) and label it 'DemoHLM-lite (approx.)' in the results. Option (a) is safer within 20 days.

**Fix 2 (required, 1 sentence)**: Correct the Contribution 1 crystallization from 'without any separate navigation planning' to 'without any separate stance-placement planning.' The RL controller still handles locomotion between stances — what the SE(3) encoding eliminates is the need to separately determine WHERE to stand. This is the real insight and should be stated precisely.

**Fix 3 (optional, 1 sentence in landscape)**: Add HumanX/XMimic (arXiv:2602.02473, Feb 2026) alongside EgoHumanoid/HoMMI/HuMI as a concurrent video-based paradigm. Prevents reviewers from raising the 'XMimic' name as an oversight.

**Fix 4 (optional, in Gantt)**: If OmniRetarget is to be a live baseline, add an explicit parallel track in the Gantt chart assigning Researcher 2 to OmniRetarget setup (Days 1-7) so the 20-day schedule reflects realistic resource allocation. Otherwise scope it as a conceptual comparison.


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
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "type": "user",
  "uuid": "d53b92e3-8490-4680-873f-ca1c4117160b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T13:01:57.250Z_

```json
{
  "parentUuid": "d53b92e3-8490-4680-873f-ca1c4117160b",
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
  "uuid": "5ff3cef1-535e-4cc1-afd5-bae4f3260f23",
  "timestamp": "2026-05-10T13:01:57.250Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T13:01:57.250Z_

```json
{
  "parentUuid": "5ff3cef1-535e-4cc1-afd5-bae4f3260f23",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f4a0d03c-4d85-44bb-b4ef-d1ea2e927e92",
  "timestamp": "2026-05-10T13:01:57.250Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
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
  "leafUuid": "f4a0d03c-4d85-44bb-b4ef-d1ea2e927e92",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify LocoMimicGen against SOTA and assess feasibility for CoRL 2026",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6"
}
```

---

### Assistant

_source line 8 · 2026-05-10T13:02:56.117Z_

<details><summary>Logged reasoning block</summary>

```text
This is round 7 of 10. I need to conduct an adversarial review of the LocoMimicGen idea. Let me look at what the previous rounds have established and what fixes the Round 6 review requested, then verify whether those fixes have been addressed in the current submission.

Round 6 required fixes:
1. **Fix 1 (required)**: Resolve DemoHLM baseline — code is not public. Either replace as conceptual comparison citing published numbers, or implement simplified surrogate.


2. **Fix 2 (required)**: Correct Contribution 1 crystallization from "without any separate navigation planning" to "without any separate stance-placement planning."
3. **Fix 3 (optional)**: Add HumanX/XMimic (arXiv:2602.02473, Feb 2026).
4. **Fix 4 (optional)**: Add OmniRetarget as conceptual comparison or parallel Gantt track.

Now I'm checking the current Round 7 submission to see if these fixes have been implemented. Looking at Fix 1 first — the DemoHLM baseline issue — I can see the landscape acknowledges that DemoHLM's code hasn't been publicly released as of May 2026.

The submission correctly positions it as a conceptual comparison using its published 10-task evaluation results, and the approach section explicitly states that DemoHLM is included only as a conceptual comparison since reimplementation would be infeasible within the 20-day window. Fix 2 on the language is also in place — the description now properly refers to "stance-placement planning" rather than the earlier phrasing. For Fix 3, I can see HumanX is mentioned in the landscape with its arXiv reference from February 2026.

Now I'm checking Fix 4 on OmniRetarget, which correctly notes it's a conceptual comparison citing published metrics, and explains why the Holosoma framework setup would exceed the available time budget. All four Round 6 fixes appear to be addressed, so I need to do independent verification of the claims and check for any remaining issues before finalizing.

I'm planning to verify the referenced arXiv papers actually exist, search for any concurrent work in humanoid loco-manipulation data generation that might have been missed, validate the Isaac Lab PR #3259 claim about SE(3) encoding, and check whether DreamGen/GR00T-Dreams and the Murooka papers are properly characterized. Let me start searching to confirm these details.

Now I'm reviewing what's been addressed across the revisions—the submission has incorporated all the major fixes including proper positioning of DemoHLM and OmniRetarget as conceptual comparisons, the correct terminology for stance-placement planning, inclusion of HumanX/XMimic, the IRM precomputation budget, combinatorial formula, Gantt chart, effect size targets, and Diffusion Policy specifications. At this point, the core issues have been resolved through multiple rounds of refinement.

I'm now checking a couple of remaining details: whether the DreamGen description accurately characterizes it as evaluating tasks in a stationary-manipulation setting even for the GR1 humanoid, and verifying the timeline consistency between the May 28 AoE and May 29 UTC deadline mentions, though these should be equivalent representations of the same deadline.

I should also consider what other relevant papers might have emerged in the months leading up to this review, and I want to double-check the core claims about the Isaac Lab PR not encoding navigation stances in the object's SE(3) local frame, plus whether the computational estimate of 3-5 H100 hours for generating 50K balance configuration poses across the six-dimensional space is realistic.

Now I'm planning to search for recent humanoid loco-manipulation data generation work from 2026, verify whether DreamGen and MoMaGen have the limitations claimed, and check if any other papers have tackled coupled SE(3) loco-manipulation for humanoids that might have been overlooked.

Looking more carefully at the submission, I'm noticing a potential issue with the reachability map precomputation claim—50K poses in 6D space seems sparse for adequate coverage across SE(2) base poses combined with squat depth, foot spread, and weight distribution, though this might be acceptable depending on the actual sampling strategy.

The paper's defense for evaluating only 2 tasks versus DexMimicGen's 9 tasks relies on the "scene-space depth" argument about sweeping 150 configurations per task, but this justification feels somewhat thin and CoRL reviewers might push back on it. There's also the explicit acknowledgment that sim-to-real transfer on physical hardware is future work, which is a notable limitation for a venue like CoRL 2026 that typically emphasizes real-world demonstrations.

On the policy side, using Diffusion Policy throughout is reasonable and at least consistent across baselines, though there's a question of whether it's optimal for loco-manipulation tasks that require tight coordination between locomotion and manipulation. The 20-day timeline with two researchers is still quite aggressive, especially since the SE(3) API extension is the critical path and simulator modifications often take longer than expected.

Looking at the novelty criterion, the work has three distinct contributions compared to the closest baseline, with the bipedal IRM approach being novel relative to wheeled platforms.

Scoring against the rubric: novelty gets a 4/5, feasibility is 3/5 due to the aggressive timeline despite the compute budget being manageable, clarity is 4/5 after multiple rounds of refinement, and impact is 4/5 given the value for humanoid robotics but limited by the simulation-only evaluation. That averages to 3.75, which falls short of the 4.0 passing threshold.

The key weaknesses are the simulation-only evaluation with just two tasks, which feels thin for a venue like CoRL, the tight 20-day schedule, and potential concurrent work from 2026 that might need citation. I should do some targeted searches to check if there are relevant papers I'm missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4a0d03c-4d85-44bb-b4ef-d1ea2e927e92",
  "isSidechain": false,
  "requestId": "req_011Catw2katL2w3xeVwL5c2z",
  "type": "assistant",
  "uuid": "c79a8b55-ec7c-40e8-b2b4-334ed33edd24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013bduUizxMGcizZXTdFoFgp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30395,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3484,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 30395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30395
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

_source line 9 · 2026-05-10T13:02:56.215Z_

I need to conduct an adversarial review of the round 7 LocoMimicGen submission. Let me verify key claims and search for any missed concurrent work before issuing my verdict.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c79a8b55-ec7c-40e8-b2b4-334ed33edd24",
  "isSidechain": false,
  "requestId": "req_011Catw2katL2w3xeVwL5c2z",
  "type": "assistant",
  "uuid": "1b066b5c-7675-453f-8fb4-7fb80916f802",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013bduUizxMGcizZXTdFoFgp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30395,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3484,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 30395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30395
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

_source line 10 · 2026-05-10T13:03:08.650Z_

<details open><summary>🔧 Tool call — Agent · `toolu_018pbAJ1An4GsLCraJiDm2he`</summary>

```json
{
  "description": "Verify recent humanoid loco-manipulation papers and concurrent work",
  "subagent_type": "Explore",
  "prompt": "Search for recent papers (2025-2026) related to humanoid loco-manipulation data generation, specifically looking for any work that does SE(3) object-centric demonstration multiplication for mobile humanoids, combined locomotion+manipulation data augmentation, or MimicGen-style extensions for bipedal humanoid robots. Also verify whether DreamGen (arXiv:2505.12705) truly only addresses stationary manipulation or also mobile/loco-manipulation.\n\nSearch queries to use:\n1. \"humanoid loco-manipulation data generation 2026\" on arxiv\n2. \"mobile manipulation demonstration augmentation bipedal 2026\" \n3. \"MimicGen humanoid locomotion\" or \"humanoid demo multiplication\"\n4. DreamGen arXiv 2505.12705 to verify its scope (stationary vs mobile manipulation)\n5. \"whole-body humanoid data generation\" 2025 2026\n6. Search arxiv.org for \"loco-manipulation data\" 2026\n\nReport back: (a) any papers that do coupled SE(3) stance+arm encoding for humanoid demo multiplication (would undermine novelty), (b) whether DreamGen truly is stationary-manipulation only as claimed, (c) any other concurrent 2026 work doing procedural humanoid data generation that isn't in the paper's landscape."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b066b5c-7675-453f-8fb4-7fb80916f802",
  "isSidechain": false,
  "requestId": "req_011Catw2katL2w3xeVwL5c2z",
  "type": "assistant",
  "uuid": "dfd320dc-5e47-4e1c-a109-cc67b8b5102a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013bduUizxMGcizZXTdFoFgp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30395,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3484,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 30395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30395
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

_source line 11 · 2026-05-10T13:03:10.104Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0186L9mvEKgpDtd7xthyt2X1`</summary>

```json
{
  "description": "Verify Isaac Lab PR #3259 and key baseline claims",
  "subagent_type": "Explore",
  "prompt": "Search for information about Isaac Lab PR #3259 (titled \"Adds locomanipulation data generation via disjoint navigation\") and verify the paper's claims about it. Also search for any recent (2026) Isaac Lab updates or papers that might have added SE(3) object-centric stance encoding for loco-manipulation.\n\nSearches to perform:\n1. Search GitHub for \"IsaacLab PR 3259 disjoint navigation locomanipulation\"\n2. Search for \"Isaac Lab 2.3 locomanipulation mimic\" to understand the current state\n3. Search for \"isaac lab locomanipulation SE3\" or similar to see if the gap still exists\n4. Search for \"IsaacSim humanoid mimic 2026\" for any new extensions\n5. Look for any Isaac Lab changelogs or release notes from late 2025/early 2026\n\nReport: (a) whether PR #3259 truly handles navigation \"disjointly\" without SE(3) encoding as claimed, (b) whether any subsequent PRs or releases (after Dec 2025) have added the SE(3) coupling that LocoMimicGen proposes, (c) what the current state of Isaac Lab's loco-manipulation data generation is as of May 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfd320dc-5e47-4e1c-a109-cc67b8b5102a",
  "isSidechain": false,
  "requestId": "req_011Catw2katL2w3xeVwL5c2z",
  "type": "assistant",
  "uuid": "3a33a945-a8fb-4a75-a2ec-d259fcf9c1b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013bduUizxMGcizZXTdFoFgp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 30395,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30395,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3484,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 30395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30395
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

_source line 12 · 2026-05-10T13:04:07.424Z_

<details><summary>↩ Tool result · `toolu_0186L9mvEKgpDtd7xthyt2X1`</summary>

```text
Based on my comprehensive search, here is my report on Isaac Lab PR #3259 and the current state of loco-manipulation data generation:

## Report: Isaac Lab Loco-Manipulation Status (May 2026)

### (A) PR #3259 "Disjoint Navigation" Implementation

**Claim Verification**: PR #3259 **does indeed handle navigation "disjointly"** as claimed. The key architectural feature is:

- Navigation is treated as a completely separate pipeline component from manipulation
- Static manipulation data (collected separately via teleoperation) is replayed as-is
- Path planning and navigation are applied independently afterward
- The pipeline segmentation follows: **pick → navigate → place** phases

However, this comes with an important caveat: **the PR contains no SE(3) object-centric stance encoding**. The implementation relies on:
- Occupancy maps for obstacle representation
- Path planning utilities (path_utils.py)
- Scene randomization (occupancy_map.py, replay.py)
- Direct task segmentation rather than coupled state representations

This is a systems-level engineering approach that treats navigation and manipulation as largely decoupled tasks.

### (B) Subsequent SE(3) Coupling Additions (Post-December 2025)

**Finding**: No subsequent Isaac Lab PRs or official releases (through May 2026) have added SE(3) object-centric stance encoding for loco-manipulation that would address the gap your research proposes.

The closest related work found:
- **PR #3992** (April 2026): Added APIs for loco-manipulation datagen including "body end effector processing" and navigation controller interface, but **no mention of SE(3) or object-centric representations**
- **NVIDIA's SPOT framework** (November 2024, arxiv 2411.00965): A separate object-centric SE(3) diffusion model for manipulation, but not integrated into Isaac Lab's loco-manipulation pipeline

### (C) Current State of Isaac Lab Loco-Manipulation (May 2026)

As of Isaac Lab 2.3.0 (current):

1. **G1 Humanoid Environment**: Combines RL-based locomotion with IK-based manipulation
2. **Mimic Integration**: Supports data generation via separate pick/navigate/place segments
3. **Data Generation Pipeline**: Uses disjoint navigation (PR #3259) with scene randomization
4. **Architecture**: Treats base and arm control largely independently
5. **Missing**: **SE(3) coupling between base pose and manipulation state** - the arm's end-effector commands are not encoded relative to the robot's base pose in a coupled object-centric representation

**Conclusion**: The gap you identified in LocoMimicGen—the lack of SE(3) object-centric stance encoding that couples navigation and manipulation—remains unfilled in official Isaac Lab releases as of May 2026. The current implementation successfully handles data generation through task decomposition, but does not provide the coupled SE(3) representations that your work proposes.

### Sources:
- [Isaac Lab PR #3259: Adds locomanipulation data generation via disjoint navigation](https://github.com/isaac-sim/IsaacLab/pull/3259)
- [Isaac Lab PR #3150: Adds Locomanipulation Environment with G1 for Mimic workflow](https://github.com/isaac-sim/IsaacLab/pull/3150)
- [Isaac Lab PR #3992: Adds APIs to Isaac Lab Mimic for supporting loco-manipulation datagen](https://github.com/isaac-sim/IsaacLab/pull/3992)
- [Streamline Robot Learning with Whole-Body Control and Enhanced Teleoperation in NVIDIA Isaac Lab 2.3](https://developer.nvidia.com/blog/streamline-robot-learning-with-whole-body-control-and-enhanced-teleoperation-in-nvidia-isaac-lab-2-3/)
- [SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation](https://arxiv.org/abs/2411.00965)
- [Isaac Lab Release Notes](https://isaac-sim.github.io/IsaacLab/main/source/refs/release_notes.html)
- [Teleoperation and Imitation Learning with Isaac Lab Mimic](https://isaac-sim.github.io/IsaacLab/main/source/overview/imitation-learning/teleop_imitation.html)
- [Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning](https://arxiv.org/html/2511.04831v1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a33a945-a8fb-4a75-a2ec-d259fcf9c1b2",
  "isSidechain": false,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "type": "user",
  "uuid": "d6b8e849-62e5-4341-bd97-2abdb050b165",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for information about Isaac Lab PR #3259 (titled \"Adds locomanipulation data generation via disjoint navigation\") and verify the paper's claims about it. Also search for any recent (2026) Isaac Lab updates or papers that might have added SE(3) object-centric stance encoding for loco-manipulation.\n\nSearches to perform:\n1. Search GitHub for \"IsaacLab PR 3259 disjoint navigation locomanipulation\"\n2. Search for \"Isaac Lab 2.3 locomanipulation mimic\" to understand the current state\n3. Search for \"isaac lab locomanipulation SE3\" or similar to see if the gap still exists\n4. Search for \"IsaacSim humanoid mimic 2026\" for any new extensions\n5. Look for any Isaac Lab changelogs or release notes from late 2025/early 2026\n\nReport: (a) whether PR #3259 truly handles navigation \"disjointly\" without SE(3) encoding as claimed, (b) whether any subsequent PRs or releases (after Dec 2025) have added the SE(3) coupling that LocoMimicGen proposes, (c) what the current state of Isaac Lab's loco-manipulation data generation is as of May 2026.",
    "agentId": "a1e20e18b47948503",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search, here is my report on Isaac Lab PR #3259 and the current state of loco-manipulation data generation:\n\n## Report: Isaac Lab Loco-Manipulation Status (May 2026)\n\n### (A) PR #3259 \"Disjoint Navigation\" Implementation\n\n**Claim Verification**: PR #3259 **does indeed handle navigation \"disjointly\"** as claimed. The key architectural feature is:\n\n- Navigation is treated as a completely separate pipeline component from manipulation\n- Static manipulation data (collected separately via teleoperation) is replayed as-is\n- Path planning and navigation are applied independently afterward\n- The pipeline segmentation follows: **pick → navigate → place** phases\n\nHowever, this comes with an important caveat: **the PR contains no SE(3) object-centric stance encoding**. The implementation relies on:\n- Occupancy maps for obstacle representation\n- Path planning utilities (path_utils.py)\n- Scene randomization (occupancy_map.py, replay.py)\n- Direct task segmentation rather than coupled state representations\n\nThis is a systems-level engineering approach that treats navigation and manipulation as largely decoupled tasks.\n\n### (B) Subsequent SE(3) Coupling Additions (Post-December 2025)\n\n**Finding**: No subsequent Isaac Lab PRs or official releases (through May 2026) have added SE(3) object-centric stance encoding for loco-manipulation that would address the gap your research proposes.\n\nThe closest related work found:\n- **PR #3992** (April 2026): Added APIs for loco-manipulation datagen including \"body end effector processing\" and navigation controller interface, but **no mention of SE(3) or object-centric representations**\n- **NVIDIA's SPOT framework** (November 2024, arxiv 2411.00965): A separate object-centric SE(3) diffusion model for manipulation, but not integrated into Isaac Lab's loco-manipulation pipeline\n\n### (C) Current State of Isaac Lab Loco-Manipulation (May 2026)\n\nAs of Isaac Lab 2.3.0 (current):\n\n1. **G1 Humanoid Environment**: Combines RL-based locomotion with IK-based manipulation\n2. **Mimic Integration**: Supports data generation via separate pick/navigate/place segments\n3. **Data Generation Pipeline**: Uses disjoint navigation (PR #3259) with scene randomization\n4. **Architecture**: Treats base and arm control largely independently\n5. **Missing**: **SE(3) coupling between base pose and manipulation state** - the arm's end-effector commands are not encoded relative to the robot's base pose in a coupled object-centric representation\n\n**Conclusion**: The gap you identified in LocoMimicGen—the lack of SE(3) object-centric stance encoding that couples navigation and manipulation—remains unfilled in official Isaac Lab releases as of May 2026. The current implementation successfully handles data generation through task decomposition, but does not provide the coupled SE(3) representations that your work proposes.\n\n### Sources:\n- [Isaac Lab PR #3259: Adds locomanipulation data generation via disjoint navigation](https://github.com/isaac-sim/IsaacLab/pull/3259)\n- [Isaac Lab PR #3150: Adds Locomanipulation Environment with G1 for Mimic workflow](https://github.com/isaac-sim/IsaacLab/pull/3150)\n- [Isaac Lab PR #3992: Adds APIs to Isaac Lab Mimic for supporting loco-manipulation datagen](https://github.com/isaac-sim/IsaacLab/pull/3992)\n- [Streamline Robot Learning with Whole-Body Control and Enhanced Teleoperation in NVIDIA Isaac Lab 2.3](https://developer.nvidia.com/blog/streamline-robot-learning-with-whole-body-control-and-enhanced-teleoperation-in-nvidia-isaac-lab-2-3/)\n- [SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation](https://arxiv.org/abs/2411.00965)\n- [Isaac Lab Release Notes](https://isaac-sim.github.io/IsaacLab/main/source/refs/release_notes.html)\n- [Teleoperation and Imitation Learning with Isaac Lab Mimic](https://isaac-sim.github.io/IsaacLab/main/source/overview/imitation-learning/teleop_imitation.html)\n- [Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning](https://arxiv.org/html/2511.04831v1)"
      }
    ],
    "totalDurationMs": 57317,
    "totalTokens": 29562,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 917,
      "cache_creation_input_tokens": 2128,
      "cache_read_input_tokens": 25431,
      "output_tokens": 1086,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2128
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 917,
          "output_tokens": 1086,
          "cache_read_input_tokens": 25431,
          "cache_creation_input_tokens": 2128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2128,
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
      "otherToolCount": 12
    }
  },
  "sourceToolAssistantUUID": "3a33a945-a8fb-4a75-a2ec-d259fcf9c1b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d6b8e849-62e5-4341-bd97-2abdb050b165",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify LocoMimicGen against SOTA and assess feasibility for CoRL 2026",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6"
}
```

---

### Tool result

_source line 15 · 2026-05-10T13:05:08.678Z_

<details><summary>↩ Tool result · `toolu_018pbAJ1An4GsLCraJiDm2he`</summary>

```text
Excellent. Now I have comprehensive information. Let me compile my findings into a detailed report.

## COMPREHENSIVE SEARCH REPORT: Humanoid Loco-Manipulation Data Generation (2025-2026)

Based on an extensive search of recent literature (2025-2026), here are my findings addressing your specific questions:

---

### **(A) COUPLED SE(3) STANCE+ARM ENCODING FOR HUMANOID DEMO MULTIPLICATION**

**Finding: SPOT (arXiv:2411.00965 / ICRA 2025) is the primary work using SE(3) object-centric representations.**

SPOT uses SE(3) pose trajectory diffusion for object-centric manipulation, enabling cross-embodiment generalization. However, **SPOT focuses exclusively on stationary object manipulation tasks** (pick-and-place, object pushing, etc.). It does not encode coupled stance+manipulation or address locomotion at all.

**Other works checked for coupled SE(3) stance encoding:**
- **ResMimic (arXiv:2510.05070)**: Uses point-cloud-based object tracking rewards and contact rewards, but does NOT use SE(3) representations. Instead uses residual learning on top of human motion tracking.
- **OmniRetarget (arXiv:2509.26633)**: Uses an "interaction mesh" with Laplacian deformation to preserve spatial and contact relationships between agent-terrain-objects, but this is **not an SE(3) object-centric representation**. It's a mesh-based retargeting approach that preserves task-relevant interactions across embodiments.
- **DexMimicGen (arXiv:2410.24185)**: Focuses on bimanual dexterous manipulation synthesis from demonstrations, but does not address locomotion.

**Conclusion**: No existing work discovered that implements **coupled SE(3) stance+arm encoding** for humanoid loco-manipulation demonstration multiplication. This appears to be genuinely novel territory.

---

### **(B) DREAMGEN SCOPE VERIFICATION**

**Finding: DreamGen (arXiv:2505.12705) is EXCLUSIVELY stationary manipulation.**

Based on the full paper HTML, DreamGen evaluates on:
- **Humanoid tasks** (GR1): hammering, wiping, folding towels, stacking bowls
- **Robotic arm tasks** (Franka): pick-and-place, cube stacking, tool use
- **Low-cost arm tasks** (SO-100): strawberry picking, tic-tac-toe
- **Simulation tasks** (RoboCasa): 24 tasks including doors, drawers, knobs
- **Novel behaviors** (14 tasks): pouring, opening appliances, tool use

**Confirmed**: DreamGen does **NOT** address mobile manipulation, humanoid locomotion, or loco-manipulation. The humanoid (GR1) is used only for upper-body manipulation from fixed positions. The work explicitly uses teleoperation data from "a single pick-and-place task in one environment" to generalize to behaviors like pouring and hammering.

---

### **(C) CONCURRENT 2026 HUMANOID LOCO-MANIPULATION DATA GENERATION WORK**

Several projects are addressing procedural/synthetic data generation for humanoid loco-manipulation that may not have been in your paper's landscape:

**1. EgoHumanoid (arXiv:2602.10106, Feb 2026)**
- First framework for loco-manipulation using robot-free egocentric human demonstrations
- Uses view alignment (depth-based reprojection) and action alignment (unified action space)
- 51% improvement over robot-only baselines
- **Approach**: Not procedural generation, but human demonstration bridging via embodiment alignment

**2. WholeBodyVLA (ICLR 2026, arXiv:2512.11047)**
- Unified latent VLA for whole-body loco-manipulation via action-free egocentric videos
- **Novel aspect**: Learns latent actions from **action-free video** (no action labels needed)
- Proposes loco-manipulation-oriented (LMO) RL for stable whole-body coordination
- Verified on AgiBot X2 humanoid
- **Approach**: Vision-language conditioning + latent action learning (not procedural generation, but data-efficient learning)

**3. Ψ₀ / Psi-Zero (arXiv:2603.12263, Mar 2026, RSS 2026)**
- Open foundation model for universal humanoid loco-manipulation
- Training approach: Pre-trains VLM on large-scale egocentric human videos, then post-trains on humanoid-specific data
- Achieves 40% improvement over baselines with minimal robot data (80 trajectories to fine-tune)
- **Not procedural generation but efficient pre-training + fine-tuning**

**4. ULTRA (arXiv:2603.03279, Mar 2026)**
- Unified multimodal control for autonomous whole-body loco-manipulation
- **Physics-driven neural retargeting algorithm** that translates motion capture to humanoid embodiments while preserving physical plausibility
- Distills universal tracking policy + applies RL fine-tuning
- Verified on Unitree G1 in real world
- **Approach**: Retargeting + distillation + sparse task specs (not SE(3) demo multiplication)

**5. VisualMimic (arXiv:2509.20322, Sep 2025)**
- Visual sim-to-real for humanoid loco-manipulation
- Unifies egocentric vision with hierarchical whole-body control
- Uses task-agnostic keypoint tracker trained from human motion data
- **Approach**: Keypoint tracking + hierarchical control (not procedural data generation)

**6. ResMimic (arXiv:2510.05070, Oct 2025)**
- Two-stage residual learning: general motion tracking + residual refinement
- Trained on large-scale human-only motion, refined for object interaction
- Verified on Unitree G1
- **Approach**: Human motion transfer + residual RL (not demonstration multiplication)

**7. OmniRetarget (arXiv:2509.26633, Sep 2025)**
- Interaction-preserving data generation via interaction mesh
- Generates 8+ hours of trajectories from source datasets
- Interaction mesh explicitly preserves agent-terrain-object spatial relationships
- Verified on Unitree G1 for parkour + loco-manipulation
- **Approach**: Mesh-based retargeting that preserves contact, not SE(3)-based multiplication

**8. GR00T N1.x (Foundation Model)**
- Vision-language-action model for humanoid whole-body control
- **Current state**: "Focuses primarily on short-horizon tabletop manipulation tasks"
- **Explicitly stated limitation**: "In future work, they aim to extend to long-horizon loco-manipulation"
- Uses NVIDIA Cosmos world models for synthetic data generation (DreamGen-style video generation)

---

### **SUMMARY OF KEY FINDINGS**

| Finding | Status |
|---------|--------|
| **Coupled SE(3) stance+arm encoding for demo multiplication** | NOT FOUND - appears novel |
| **DreamGen scope (stationary vs mobile)** | CONFIRMED: Stationary manipulation only |
| **SE(3) object-centric methods in humanoid loco-manipulation** | Only SPOT (2025), but stationary manipulation only |
| **Concurrent procedural data generation for humanoid loco-manipulation (2026)** | Multiple approaches found, but none use SE(3) demo multiplication |

---

### **MOST RELEVANT CONCURRENT WORK**

The closest competing approaches in your space are:

1. **OmniRetarget** - Interaction mesh approach to preserve contact relationships during retargeting (but no SE(3) encoding)
2. **ULTRA** - Physics-driven retargeting for loco-manipulation, but uses sparse task specs not SE(3) trajectories
3. **ResMimic** - Human motion transfer with contact rewards, but residual-learning approach not demonstration multiplication
4. **Ψ₀ (Psi-Zero)** - Large-scale pre-training on human egocentric video + humanoid post-training (data-efficient but not procedural generation)

None of these use **coupled SE(3) stance+manipulation encodings for demonstration multiplication**, which appears to be your novel contribution.

---

## Sources

- [OmniRetarget: Interaction-Preserving Data Generation](https://arxiv.org/abs/2509.26633)
- [ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning](https://arxiv.org/abs/2510.05070)
- [VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation](https://arxiv.org/abs/2509.20322)
- [DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories](https://arxiv.org/abs/2505.12705)
- [EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration](https://arxiv.org/abs/2602.10106)
- [SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation](https://arxiv.org/abs/2411.00965)
- [ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2603.03279)
- [Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)
- [WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control](https://arxiv.org/abs/2512.11047)
- [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](https://arxiv.org/abs/2410.24185)
- [MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation](https://arxiv.org/abs/2510.18316)
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)
- [awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfd320dc-5e47-4e1c-a109-cc67b8b5102a",
  "isSidechain": false,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "type": "user",
  "uuid": "0a363e13-db7d-413e-9add-dced7901391f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent papers (2025-2026) related to humanoid loco-manipulation data generation, specifically looking for any work that does SE(3) object-centric demonstration multiplication for mobile humanoids, combined locomotion+manipulation data augmentation, or MimicGen-style extensions for bipedal humanoid robots. Also verify whether DreamGen (arXiv:2505.12705) truly only addresses stationary manipulation or also mobile/loco-manipulation.\n\nSearch queries to use:\n1. \"humanoid loco-manipulation data generation 2026\" on arxiv\n2. \"mobile manipulation demonstration augmentation bipedal 2026\" \n3. \"MimicGen humanoid locomotion\" or \"humanoid demo multiplication\"\n4. DreamGen arXiv 2505.12705 to verify its scope (stationary vs mobile manipulation)\n5. \"whole-body humanoid data generation\" 2025 2026\n6. Search arxiv.org for \"loco-manipulation data\" 2026\n\nReport back: (a) any papers that do coupled SE(3) stance+arm encoding for humanoid demo multiplication (would undermine novelty), (b) whether DreamGen truly is stationary-manipulation only as claimed, (c) any other concurrent 2026 work doing procedural humanoid data generation that isn't in the paper's landscape.",
    "agentId": "ae1ebe7f07cf40db0",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent. Now I have comprehensive information. Let me compile my findings into a detailed report.\n\n## COMPREHENSIVE SEARCH REPORT: Humanoid Loco-Manipulation Data Generation (2025-2026)\n\nBased on an extensive search of recent literature (2025-2026), here are my findings addressing your specific questions:\n\n---\n\n### **(A) COUPLED SE(3) STANCE+ARM ENCODING FOR HUMANOID DEMO MULTIPLICATION**\n\n**Finding: SPOT (arXiv:2411.00965 / ICRA 2025) is the primary work using SE(3) object-centric representations.**\n\nSPOT uses SE(3) pose trajectory diffusion for object-centric manipulation, enabling cross-embodiment generalization. However, **SPOT focuses exclusively on stationary object manipulation tasks** (pick-and-place, object pushing, etc.). It does not encode coupled stance+manipulation or address locomotion at all.\n\n**Other works checked for coupled SE(3) stance encoding:**\n- **ResMimic (arXiv:2510.05070)**: Uses point-cloud-based object tracking rewards and contact rewards, but does NOT use SE(3) representations. Instead uses residual learning on top of human motion tracking.\n- **OmniRetarget (arXiv:2509.26633)**: Uses an \"interaction mesh\" with Laplacian deformation to preserve spatial and contact relationships between agent-terrain-objects, but this is **not an SE(3) object-centric representation**. It's a mesh-based retargeting approach that preserves task-relevant interactions across embodiments.\n- **DexMimicGen (arXiv:2410.24185)**: Focuses on bimanual dexterous manipulation synthesis from demonstrations, but does not address locomotion.\n\n**Conclusion**: No existing work discovered that implements **coupled SE(3) stance+arm encoding** for humanoid loco-manipulation demonstration multiplication. This appears to be genuinely novel territory.\n\n---\n\n### **(B) DREAMGEN SCOPE VERIFICATION**\n\n**Finding: DreamGen (arXiv:2505.12705) is EXCLUSIVELY stationary manipulation.**\n\nBased on the full paper HTML, DreamGen evaluates on:\n- **Humanoid tasks** (GR1): hammering, wiping, folding towels, stacking bowls\n- **Robotic arm tasks** (Franka): pick-and-place, cube stacking, tool use\n- **Low-cost arm tasks** (SO-100): strawberry picking, tic-tac-toe\n- **Simulation tasks** (RoboCasa): 24 tasks including doors, drawers, knobs\n- **Novel behaviors** (14 tasks): pouring, opening appliances, tool use\n\n**Confirmed**: DreamGen does **NOT** address mobile manipulation, humanoid locomotion, or loco-manipulation. The humanoid (GR1) is used only for upper-body manipulation from fixed positions. The work explicitly uses teleoperation data from \"a single pick-and-place task in one environment\" to generalize to behaviors like pouring and hammering.\n\n---\n\n### **(C) CONCURRENT 2026 HUMANOID LOCO-MANIPULATION DATA GENERATION WORK**\n\nSeveral projects are addressing procedural/synthetic data generation for humanoid loco-manipulation that may not have been in your paper's landscape:\n\n**1. EgoHumanoid (arXiv:2602.10106, Feb 2026)**\n- First framework for loco-manipulation using robot-free egocentric human demonstrations\n- Uses view alignment (depth-based reprojection) and action alignment (unified action space)\n- 51% improvement over robot-only baselines\n- **Approach**: Not procedural generation, but human demonstration bridging via embodiment alignment\n\n**2. WholeBodyVLA (ICLR 2026, arXiv:2512.11047)**\n- Unified latent VLA for whole-body loco-manipulation via action-free egocentric videos\n- **Novel aspect**: Learns latent actions from **action-free video** (no action labels needed)\n- Proposes loco-manipulation-oriented (LMO) RL for stable whole-body coordination\n- Verified on AgiBot X2 humanoid\n- **Approach**: Vision-language conditioning + latent action learning (not procedural generation, but data-efficient learning)\n\n**3. Ψ₀ / Psi-Zero (arXiv:2603.12263, Mar 2026, RSS 2026)**\n- Open foundation model for universal humanoid loco-manipulation\n- Training approach: Pre-trains VLM on large-scale egocentric human videos, then post-trains on humanoid-specific data\n- Achieves 40% improvement over baselines with minimal robot data (80 trajectories to fine-tune)\n- **Not procedural generation but efficient pre-training + fine-tuning**\n\n**4. ULTRA (arXiv:2603.03279, Mar 2026)**\n- Unified multimodal control for autonomous whole-body loco-manipulation\n- **Physics-driven neural retargeting algorithm** that translates motion capture to humanoid embodiments while preserving physical plausibility\n- Distills universal tracking policy + applies RL fine-tuning\n- Verified on Unitree G1 in real world\n- **Approach**: Retargeting + distillation + sparse task specs (not SE(3) demo multiplication)\n\n**5. VisualMimic (arXiv:2509.20322, Sep 2025)**\n- Visual sim-to-real for humanoid loco-manipulation\n- Unifies egocentric vision with hierarchical whole-body control\n- Uses task-agnostic keypoint tracker trained from human motion data\n- **Approach**: Keypoint tracking + hierarchical control (not procedural data generation)\n\n**6. ResMimic (arXiv:2510.05070, Oct 2025)**\n- Two-stage residual learning: general motion tracking + residual refinement\n- Trained on large-scale human-only motion, refined for object interaction\n- Verified on Unitree G1\n- **Approach**: Human motion transfer + residual RL (not demonstration multiplication)\n\n**7. OmniRetarget (arXiv:2509.26633, Sep 2025)**\n- Interaction-preserving data generation via interaction mesh\n- Generates 8+ hours of trajectories from source datasets\n- Interaction mesh explicitly preserves agent-terrain-object spatial relationships\n- Verified on Unitree G1 for parkour + loco-manipulation\n- **Approach**: Mesh-based retargeting that preserves contact, not SE(3)-based multiplication\n\n**8. GR00T N1.x (Foundation Model)**\n- Vision-language-action model for humanoid whole-body control\n- **Current state**: \"Focuses primarily on short-horizon tabletop manipulation tasks\"\n- **Explicitly stated limitation**: \"In future work, they aim to extend to long-horizon loco-manipulation\"\n- Uses NVIDIA Cosmos world models for synthetic data generation (DreamGen-style video generation)\n\n---\n\n### **SUMMARY OF KEY FINDINGS**\n\n| Finding | Status |\n|---------|--------|\n| **Coupled SE(3) stance+arm encoding for demo multiplication** | NOT FOUND - appears novel |\n| **DreamGen scope (stationary vs mobile)** | CONFIRMED: Stationary manipulation only |\n| **SE(3) object-centric methods in humanoid loco-manipulation** | Only SPOT (2025), but stationary manipulation only |\n| **Concurrent procedural data generation for humanoid loco-manipulation (2026)** | Multiple approaches found, but none use SE(3) demo multiplication |\n\n---\n\n### **MOST RELEVANT CONCURRENT WORK**\n\nThe closest competing approaches in your space are:\n\n1. **OmniRetarget** - Interaction mesh approach to preserve contact relationships during retargeting (but no SE(3) encoding)\n2. **ULTRA** - Physics-driven retargeting for loco-manipulation, but uses sparse task specs not SE(3) trajectories\n3. **ResMimic** - Human motion transfer with contact rewards, but residual-learning approach not demonstration multiplication\n4. **Ψ₀ (Psi-Zero)** - Large-scale pre-training on human egocentric video + humanoid post-training (data-efficient but not procedural generation)\n\nNone of these use **coupled SE(3) stance+manipulation encodings for demonstration multiplication**, which appears to be your novel contribution.\n\n---\n\n## Sources\n\n- [OmniRetarget: Interaction-Preserving Data Generation](https://arxiv.org/abs/2509.26633)\n- [ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning](https://arxiv.org/abs/2510.05070)\n- [VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation](https://arxiv.org/abs/2509.20322)\n- [DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories](https://arxiv.org/abs/2505.12705)\n- [EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration](https://arxiv.org/abs/2602.10106)\n- [SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation](https://arxiv.org/abs/2411.00965)\n- [ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2603.03279)\n- [Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)\n- [WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control](https://arxiv.org/abs/2512.11047)\n- [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning](https://arxiv.org/abs/2410.24185)\n- [MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation](https://arxiv.org/abs/2510.18316)\n- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)\n- [awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning)"
      }
    ],
    "totalDurationMs": 120021,
    "totalTokens": 44500,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3415,
      "cache_read_input_tokens": 38544,
      "output_tokens": 2534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3415
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2534,
          "cache_read_input_tokens": 38544,
          "cache_creation_input_tokens": 3415,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3415,
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
      "otherToolCount": 25
    }
  },
  "sourceToolAssistantUUID": "dfd320dc-5e47-4e1c-a109-cc67b8b5102a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T13:06:02.754Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have some useful research. Let me now evaluate the key findings:

1. **Coupled SE(3) stance+arm encoding for humanoid demo multiplication**: Not found in existing literature. The gap appears genuine.

2. **DreamGen scope**: Confirmed - stationary manipulation only. The paper's claim is verified.

3. **Isaac Lab PR #3259**: Confirmed as disjoint navigation without SE(3) encoding. The gap claimed is real.

4. **ULTRA (arXiv:2603.03279)**: A new paper from March 2026 that does "physics-driven neural retargeting" for loco-manipulation. 

Looking at ULTRA more closely, it translates motion capture to humanoid embodiments while preserving physical plausibility—this is a retargeting approach from human data rather than demonstration multiplication, so it falls outside the scope constraints.

5. **Ψ₀/Psi-Zero (arXiv:2603.12263, Mar 2026)**: Uses pre-training on egocentric video plus fine-tuning, not procedural data generation, so not directly competing.

Now I need to assess what remaining issues exist with the current submission. Looking at these additional concerns, I'm seeing several papers that touch on related areas but operate in different spaces—ULTRA and Ψ₀ are data-efficient approaches rather than procedural generation, ResMimic has naming overlap but distinct methodology, and the evaluation scope remains narrow with only simulation-based tasks. The IRM precomputation timeline might be tight but plausible given Isaac Lab's GPU parallelization, so that's less of a red flag than the evaluation limitations. assessment:**

1. **ULTRA and Psi-Zero uncited**: These are March 2026 papers that should probably be cited. ULTRA does something adjacent (physics-driven retargeting for loco-manipulation), and Psi-Zero addresses humanoid loco-manipulation data efficiency. However, neither directly competes with LocoMimicGen's core contribution (SE(3) demo multiplication). Missing citations are a reviewability concern but not a fundamental flaw.

2. **2-task sim-only evaluation**: This continues to be the weakest point. The paper has a defense for this ("scaling curves are the primary contribution"), but it's still a risk at CoRL where reviewers expect broader evaluation.

3. **The SE(3) stance encoding insight**: Based on my research, this appears genuinely novel and not covered by existing work. The gap in Isaac Lab is real.

4. **Overall novelty**: The three-contribution approach stands apart from prior work—the wheeled versus bipedal distinction from MoMaGen is solid, and the SE(3) coupled versus disjoint framing versus PR #3259 is equally valid.

Now I'm weighing whether to recommend acceptance or request revisions. Looking at the scores: novelty is strong at 4/5 with three clearly differentiated contributions and no direct competitor, feasibility sits at 3.5/5 given the aggressive timeline despite reasonable compute requirements, clarity improved to 4/5 after seven rounds of refinement, and impact lands at 3.5/5 since the sim-only limitation affects real-world applicability. That averages around 3.75, which puts this below the typical acceptance threshold.

The missing citations and evaluation scope are addressable in a revision round. I'm leaning toward "revise" rather than "pass" because the concurrent papers should be in the landscape, and the 2-task evaluation remains a CoRL acceptance risk that hasn't been fully resolved—just defended.

Let me reconsider whether ULTRA is actually a blocking concern. It's positioned as a retargeting approach, which the user marked as out of scope, so it's more complementary than competing. Psi-Zero is a foundation model paper using pre-training, not really in the data generation space. Maybe I'm being too strict about the concurrent papers after seven rounds of feedback.

Looking at the full picture: the core SE(3) coupling contribution is genuinely novel with a confirmed gap, there are three solid technical contributions, baselines are properly positioned, and the evaluation plan has clear effect size targets. The main issues are the missing citations and the aggressive timeline, but those are revision-level concerns, not fundamental flaws. I'm settling on a revise verdict with a 4/5 for novelty since the core idea is legitimately novel even if the landscape coverage could be tighter.

The feasibility score of 3/5 is the limiting factor—the 20-day timeline is the real risk, particularly around SE(3) API integration. Even with careful estimation, that's where things could slip. The other dimensions are solid: clarity is 4/5 after seven rounds of refinement, impact is 4/5 given the real bottleneck being addressed, and the average lands at 3.75, which means one more revision could push this over the 4.0 threshold if I can either tighten the timeline or find a way to de-risk the integration work.

Looking at what's holding this back, there are a few concrete issues to address. The evaluation is limited to two simulation tasks because of the deadline constraint, not resources—that's a vulnerability for CoRL. OmniRetarget exists only as a conceptual baseline without live comparison, which weakens the retargeting comparison. And I'm noticing that ULTRA from March 2026 on unified whole-body loco-manipulation should be acknowledged; it's a concurrent retargeting approach using physics-driven neural methods that complements what we're doing procedurally. The paper's argument that scaling curves matter more than task breadth is defensible but risky given reviewer expectations. Adding the articulated-object task more prominently in the supplementary material might help shore up the evaluation concern.

The schedule itself has a critical bottleneck in days 3-7 where the SE(3) encoding extension happens—any delay there cascades through everything, and with just two researchers there's almost no buffer. I should also flag Ψ₀ from March 2026, which tackles the humanoid loco-manipulation data problem from a different angle. Actually, I need to clarify whether ULTRA really falls outside scope—the user said action retargeting from human video to humanoid is out of scope, and ULTRA does MoCap-to-humanoid retargeting, so it probably counts as in-scope and needs proper positioning.

As a reviewer though, I should still call out both ULTRA and Psi-Zero as concurrent 2026 papers that belong in the landscape section. I'm also concerned about the evaluation breadth—only two tasks and everything's in simulation. The main issues to flag are those two missing citations, the narrow evaluation scope, and the concentration of schedule risk on that SE(3) integration work. Round 6 fixes all look good though. This warrants a revise verdict for round 7, with scores around 3.75 average across novelty, feasibility, clarity, and impact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a363e13-db7d-413e-9add-dced7901391f",
  "isSidechain": false,
  "requestId": "req_011CatwGrr4NKMSWDTA7UaZ8",
  "type": "assistant",
  "uuid": "5c1698b8-96e2-4b26-8584-3b5414455f26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019tB9dzu2CNgW4zHqgJkHi3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1112,
      "cache_creation_input_tokens": 6040,
      "cache_read_input_tokens": 42026,
      "output_tokens": 3108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1112,
          "output_tokens": 3108,
          "cache_read_input_tokens": 42026,
          "cache_creation_input_tokens": 6040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6040
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

_source line 17 · 2026-05-10T13:06:08.928Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01E2MHH2u1kZrkjVR413dq7x`</summary>

```json
{
  "description": "Search for ULTRA and Psi-Zero papers and any other missing concurrent work",
  "subagent_type": "Explore",
  "prompt": "Search for these specific March 2026 papers on humanoid loco-manipulation to get their details and determine if they're relevant to a paper called \"LocoMimicGen\" about procedural demonstration multiplication for humanoid robots:\n\n1. ULTRA (arXiv:2603.03279, March 2026): \"Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation\" - Search arxiv for this paper to understand what it does. Is it retargeting-based or procedural generation?\n\n2. Psi-Zero / Ψ₀ (arXiv:2603.12263, March 2026): \"Open Foundation Model Towards Universal Humanoid Loco-Manipulation\" - What approach does it use? Foundation model pre-training vs. procedural generation?\n\n3. Also search for any other 2026 papers that might be doing MimicGen-style data generation for mobile humanoids, or any work on \"inverse reachability map for humanoid\" or \"bipedal arm reachability data generation\" that isn't already in this list: [DemoHLM, OmniRetarget, MoMaGen, DreamGen, EgoHumanoid, HoMMI, HuMI, HumanX]\n\n4. Search for \"Unitree G1 loco-manipulation 2026\" and \"bipedal humanoid manipulation data 2026\" to catch anything missed.\n\nReport: the core approach of ULTRA and Psi-Zero (are they retargeting? generative? procedural?), whether they could be considered direct competitors to SE(3)-based demo multiplication, and any other papers found that the landscape might be missing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c1698b8-96e2-4b26-8584-3b5414455f26",
  "isSidechain": false,
  "requestId": "req_011CatwGrr4NKMSWDTA7UaZ8",
  "type": "assistant",
  "uuid": "e8403093-4a0d-44c4-b8c4-372c7b076124",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019tB9dzu2CNgW4zHqgJkHi3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1112,
      "cache_creation_input_tokens": 6040,
      "cache_read_input_tokens": 42026,
      "output_tokens": 3108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1112,
          "output_tokens": 3108,
          "cache_read_input_tokens": 42026,
          "cache_creation_input_tokens": 6040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6040
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e8403093-4a0d-44c4-b8c4-372c7b076124",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify LocoMimicGen against SOTA and assess feasibility for CoRL 2026",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6"
}
```

---

### Tool result

_source line 20 · 2026-05-10T13:07:17.428Z_

<details><summary>↩ Tool result · `toolu_01E2MHH2u1kZrkjVR413dq7x`</summary>

```text
Perfect! Now I have comprehensive information. Let me compile my findings into a clear report.

## Report: March 2026 Humanoid Loco-Manipulation Landscape Analysis

### Papers Found and Core Approaches

**1. ULTRA (arXiv:2603.03279, March 2026)**
- **Core Approach:** Physics-driven retargeting (NOT procedural generation)
- **Method:** Two-component framework: (1) physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions, (2) unified multimodal controller supporting both dense references and sparse task specifications
- **Key Innovation:** Addresses scarce/low-quality retargeted data through physics preservation
- **Relevance to SE(3) demo multiplication:** Direct competitor via retargeting, but different mechanism—uses physics constraints rather than procedural SE(3) transformation. Both aim to scale from limited demonstrations

**2. Ψ₀ (Psi-Zero) (arXiv:2603.12263, March 2026)**
- **Core Approach:** Foundation model pre-training (NOT procedural generation)
- **Method:** Staged training paradigm: (1) Autoregressive VLM pre-training on 800 hours of egocentric human videos, (2) Flow-based action expert post-training on 30 hours of high-quality robot data
- **Key Innovation:** Decoupled learning addressing kinematic/motion disparities between humans and humanoids; outperforms 10x larger datasets by 40% success rate improvement
- **Relevance to SE(3) demo multiplication:** Orthogonal approach—uses foundation model scaling rather than procedural transformation. Not a direct competitor to demo multiplication but complementary (large-scale pre-training vs. small-scale synthesis)

### Additional Papers Found (Not in Original List)

**3. WholeBodyVLA (ICLR 2026, December 2025 arXiv:2512.11047)**
- **Core Approach:** Unified latent VLA from action-free videos + RL
- **Method:** Learns from low-cost action-free egocentric videos via unified latent learning framework, with locomotion-oriented RL policy for stable whole-body coordination
- **Implementation:** Verified on AgiBot X2, outperforms baselines by 21.3%
- **Relevance:** Data generation adjacent—uses RL for augmentation but not procedural transformation

**4. EgoHumanoid (arXiv:2602.10106, February 2026)**
- **Core Approach:** Human-to-robot transfer with view/action alignment (NOT procedural generation)
- **Method:** Co-trains vision-language-action policy using egocentric human demonstrations + limited robot data; view alignment (transforms human egocentric to robot viewpoint) + action alignment (unified action space with delta end-effector poses)
- **Key Innovation:** 51% performance improvement over robot-only baselines using robot-free data
- **Relevance:** Alignment-based data synthesis rather than procedural multiplication

**5. DexMimicGen (2024, extended to humanoids 2025)**
- **Core Approach:** Procedural demo transformation (most similar to LocoMimicGen)
- **Method:** Extends MimicGen to humanoid robots; uses per-arm subtask segmentation, synchronization strategy for coordination, ordering constraints for sequential subtasks
- **Key Innovation:** Automated large-scale data generation for dexterous humanoids (e.g., GR-1)
- **Relevance:** **Highly relevant—this IS a MimicGen-style procedural demonstration multiplier for humanoids.** Uses scene/configuration adaptation rather than SE(3) but same philosophy of expanding limited demos

**6. GR00T N1 (arXiv:2503.14734, March 2026)**
- **Core Approach:** Foundation model VLA with dual-system architecture
- **Method:** Vision-language module (System 2) + diffusion transformer module (System 1); trained on heterogeneous mix of real robot trajectories, human videos, synthetically generated datasets
- **Key Innovation:** Deployed on Fourier GR-1 for bimanual manipulation
- **Relevance:** Foundation model approach—complementary to procedural generation, not a direct competitor

**7. OmniRetarget (arXiv:2509.26633, September 2025)**
- **Core Approach:** Interaction-preserving retargeting (mentioned in your original list)
- **Method:** Uses interaction mesh to explicitly model/preserve spatial and contact relationships between agent, terrain, manipulated objects
- **Key Innovation:** Generates 8+ hour trajectories with better kinematic constraint satisfaction and contact preservation than baselines
- **Relevance:** Retargeting-based (similar philosophy to ULTRA), not procedural generation

### Competitive Landscape Summary

**Direct Competitors to SE(3)-based Demo Multiplication:**
- **ULTRA** — retargeting-based, not procedural, but competing approach for scaling from limited demos
- **DexMimicGen** — procedural but uses scene/configuration adaptation rather than SE(3) transformation
- Neither ULTRA nor Psi-Zero are direct SE(3) competitors; both use different scaling mechanisms

**Orthogonal Approaches (Foundation Models):**
- Ψ₀, GR00T N1, EgoHumanoid, WholeBodyVLA all use foundation model pre-training or large-scale dataset approaches
- These complement rather than compete with procedural demo multiplication (can be used together)

**Key Gaps in Landscape:**
- Most 2026 papers focus on either (1) retargeting with better contact preservation (ULTRA, OmniRetarget), or (2) foundation model scaling (Psi-Zero, GR00T N1)
- **No papers found specifically on SE(3)-based procedural demo multiplication for whole-body loco-manipulation**
- DexMimicGen is the closest existing procedural approach but for dexterous arms, not mobile humanoids
- WholeBodyVLA uses RL-based augmentation but not explicit procedural transformation
- This suggests **LocoMimicGen would be filling a gap**: SE(3)-based procedural multiplication for mobile humanoid loco-manipulation

### Sources
- [ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2603.03279)
- [Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)
- [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation](https://arxiv.org/html/2410.24185v1)
- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)
- [EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration](https://arxiv.org/abs/2602.10106)
- [WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control](https://arxiv.org/abs/2512.11047)
- [OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2509.26633)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8403093-4a0d-44c4-b8c4-372c7b076124",
  "isSidechain": false,
  "promptId": "05d7956b-1411-4a05-8ea2-644dd347c42e",
  "type": "user",
  "uuid": "be29bd2b-43cb-466c-8890-6fa4bfd763cf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for these specific March 2026 papers on humanoid loco-manipulation to get their details and determine if they're relevant to a paper called \"LocoMimicGen\" about procedural demonstration multiplication for humanoid robots:\n\n1. ULTRA (arXiv:2603.03279, March 2026): \"Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation\" - Search arxiv for this paper to understand what it does. Is it retargeting-based or procedural generation?\n\n2. Psi-Zero / Ψ₀ (arXiv:2603.12263, March 2026): \"Open Foundation Model Towards Universal Humanoid Loco-Manipulation\" - What approach does it use? Foundation model pre-training vs. procedural generation?\n\n3. Also search for any other 2026 papers that might be doing MimicGen-style data generation for mobile humanoids, or any work on \"inverse reachability map for humanoid\" or \"bipedal arm reachability data generation\" that isn't already in this list: [DemoHLM, OmniRetarget, MoMaGen, DreamGen, EgoHumanoid, HoMMI, HuMI, HumanX]\n\n4. Search for \"Unitree G1 loco-manipulation 2026\" and \"bipedal humanoid manipulation data 2026\" to catch anything missed.\n\nReport: the core approach of ULTRA and Psi-Zero (are they retargeting? generative? procedural?), whether they could be considered direct competitors to SE(3)-based demo multiplication, and any other papers found that the landscape might be missing.",
    "agentId": "a83e64755b4ce8ece",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information. Let me compile my findings into a clear report.\n\n## Report: March 2026 Humanoid Loco-Manipulation Landscape Analysis\n\n### Papers Found and Core Approaches\n\n**1. ULTRA (arXiv:2603.03279, March 2026)**\n- **Core Approach:** Physics-driven retargeting (NOT procedural generation)\n- **Method:** Two-component framework: (1) physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions, (2) unified multimodal controller supporting both dense references and sparse task specifications\n- **Key Innovation:** Addresses scarce/low-quality retargeted data through physics preservation\n- **Relevance to SE(3) demo multiplication:** Direct competitor via retargeting, but different mechanism—uses physics constraints rather than procedural SE(3) transformation. Both aim to scale from limited demonstrations\n\n**2. Ψ₀ (Psi-Zero) (arXiv:2603.12263, March 2026)**\n- **Core Approach:** Foundation model pre-training (NOT procedural generation)\n- **Method:** Staged training paradigm: (1) Autoregressive VLM pre-training on 800 hours of egocentric human videos, (2) Flow-based action expert post-training on 30 hours of high-quality robot data\n- **Key Innovation:** Decoupled learning addressing kinematic/motion disparities between humans and humanoids; outperforms 10x larger datasets by 40% success rate improvement\n- **Relevance to SE(3) demo multiplication:** Orthogonal approach—uses foundation model scaling rather than procedural transformation. Not a direct competitor to demo multiplication but complementary (large-scale pre-training vs. small-scale synthesis)\n\n### Additional Papers Found (Not in Original List)\n\n**3. WholeBodyVLA (ICLR 2026, December 2025 arXiv:2512.11047)**\n- **Core Approach:** Unified latent VLA from action-free videos + RL\n- **Method:** Learns from low-cost action-free egocentric videos via unified latent learning framework, with locomotion-oriented RL policy for stable whole-body coordination\n- **Implementation:** Verified on AgiBot X2, outperforms baselines by 21.3%\n- **Relevance:** Data generation adjacent—uses RL for augmentation but not procedural transformation\n\n**4. EgoHumanoid (arXiv:2602.10106, February 2026)**\n- **Core Approach:** Human-to-robot transfer with view/action alignment (NOT procedural generation)\n- **Method:** Co-trains vision-language-action policy using egocentric human demonstrations + limited robot data; view alignment (transforms human egocentric to robot viewpoint) + action alignment (unified action space with delta end-effector poses)\n- **Key Innovation:** 51% performance improvement over robot-only baselines using robot-free data\n- **Relevance:** Alignment-based data synthesis rather than procedural multiplication\n\n**5. DexMimicGen (2024, extended to humanoids 2025)**\n- **Core Approach:** Procedural demo transformation (most similar to LocoMimicGen)\n- **Method:** Extends MimicGen to humanoid robots; uses per-arm subtask segmentation, synchronization strategy for coordination, ordering constraints for sequential subtasks\n- **Key Innovation:** Automated large-scale data generation for dexterous humanoids (e.g., GR-1)\n- **Relevance:** **Highly relevant—this IS a MimicGen-style procedural demonstration multiplier for humanoids.** Uses scene/configuration adaptation rather than SE(3) but same philosophy of expanding limited demos\n\n**6. GR00T N1 (arXiv:2503.14734, March 2026)**\n- **Core Approach:** Foundation model VLA with dual-system architecture\n- **Method:** Vision-language module (System 2) + diffusion transformer module (System 1); trained on heterogeneous mix of real robot trajectories, human videos, synthetically generated datasets\n- **Key Innovation:** Deployed on Fourier GR-1 for bimanual manipulation\n- **Relevance:** Foundation model approach—complementary to procedural generation, not a direct competitor\n\n**7. OmniRetarget (arXiv:2509.26633, September 2025)**\n- **Core Approach:** Interaction-preserving retargeting (mentioned in your original list)\n- **Method:** Uses interaction mesh to explicitly model/preserve spatial and contact relationships between agent, terrain, manipulated objects\n- **Key Innovation:** Generates 8+ hour trajectories with better kinematic constraint satisfaction and contact preservation than baselines\n- **Relevance:** Retargeting-based (similar philosophy to ULTRA), not procedural generation\n\n### Competitive Landscape Summary\n\n**Direct Competitors to SE(3)-based Demo Multiplication:**\n- **ULTRA** — retargeting-based, not procedural, but competing approach for scaling from limited demos\n- **DexMimicGen** — procedural but uses scene/configuration adaptation rather than SE(3) transformation\n- Neither ULTRA nor Psi-Zero are direct SE(3) competitors; both use different scaling mechanisms\n\n**Orthogonal Approaches (Foundation Models):**\n- Ψ₀, GR00T N1, EgoHumanoid, WholeBodyVLA all use foundation model pre-training or large-scale dataset approaches\n- These complement rather than compete with procedural demo multiplication (can be used together)\n\n**Key Gaps in Landscape:**\n- Most 2026 papers focus on either (1) retargeting with better contact preservation (ULTRA, OmniRetarget), or (2) foundation model scaling (Psi-Zero, GR00T N1)\n- **No papers found specifically on SE(3)-based procedural demo multiplication for whole-body loco-manipulation**\n- DexMimicGen is the closest existing procedural approach but for dexterous arms, not mobile humanoids\n- WholeBodyVLA uses RL-based augmentation but not explicit procedural transformation\n- This suggests **LocoMimicGen would be filling a gap**: SE(3)-based procedural multiplication for mobile humanoid loco-manipulation\n\n### Sources\n- [ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2603.03279)\n- [Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation](https://arxiv.org/abs/2603.12263)\n- [DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation](https://arxiv.org/html/2410.24185v1)\n- [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)\n- [EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration](https://arxiv.org/abs/2602.10106)\n- [WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control](https://arxiv.org/abs/2512.11047)\n- [OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation](https://arxiv.org/abs/2509.26633)"
      }
    ],
    "totalDurationMs": 68495,
    "totalTokens": 34827,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 875,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 31085,
      "output_tokens": 1784,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 875,
          "output_tokens": 1784,
          "cache_read_input_tokens": 31085,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1083,
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
  "sourceToolAssistantUUID": "e8403093-4a0d-44c4-b8c4-372c7b076124",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T13:07:52.887Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research findings. Let me synthesize everything and issue my round 7 verdict.

**Summary of findings:**
1. **Coupled SE(3) stance+arm encoding for humanoid demo multiplication**: NOT FOUND - appears genuinely novel
2. **DreamGen scope**: CONFIRMED stationary manipulation only
3. **Isaac Lab PR #3259**: Confirmed as disjoint navigation without SE(3) encoding - gap is real
4. **ULTRA (2603.03279)**: Physics-driven retargeting (NOT procedural generation) - complementary, should be cited


5. **Psi-Zero (2603.12263)**: Foundation model pre-training - orthogonal, should be cited
6. **No direct SE(3) demo multiplication competitor for mobile humanoids found**

For round 7, I need to flag that ULTRA and Psi-Zero are concurrent March 2026 papers that reviewers will likely know about—ULTRA as a complementary retargeting approach for whole-body loco-manipulation, and Psi-Zero as an orthogonal foundation model pre-training method—both warrant citations in the related work landscape.

The 2-task sim-only evaluation remains the most vulnerable aspect; while the "scene-space depth over task breadth" defense has held through multiple rounds, CoRL reviewers may still push back on this limitation.

All Round 6 fixes are confirmed complete, and the novelty assessment stands at 4/5—the SE(3) coupling is genuinely novel with no direct competitor, the Isaac Lab gap is validated, and the bipedal IRM adaptation represents a real contribution.

Feasibility scores at 3/5 due to the aggressive 20-day timeline for three non-trivial contributions, the sim-only constraint, and uncertainty around precomputing 50K poses in 6D space, though Isaac Lab should handle it. Clarity and impact both rate 4/5—the paper is well-written with a solid Gantt chart, and it addresses a real humanoid data scarcity problem with quantified targets, though sim-only evaluation does limit immediate real-world deployment potential. Overall average lands at 3.75.

The missing citations for ULTRA and Psi-Zero are minor issues compared to the core technical concerns. Since we're at round 7 of 10, I'm leaning toward "revise" to address those citation gaps and tighten the feasibility argument, even though the core idea has been well-validated across multiple rounds.

Wait, I'm noticing a potential timeline inconsistency—the Gantt chart shows May 28 AoE for the paper deadline, but the user's requirements specify May 29 for CoRL 2026. Let me check if that's actually a problem or just a minor date discrepancy.

Actually, looking at the submission details, May 28 AoE does convert to May 29 UTC, so the Gantt chart is consistent with the actual deadline. That's fine.

Now I'm thinking through the IRM precomputation claim about 50K balance configuration poses in 6D space—whether that's actually feasible given the dimensionality and sampling density.

The sparsity is a real concern with only 5-6 points per dimension, but since this is a one-time precomputation that Isaac Lab can handle in parallel across thousands of environments, it's not a fundamental blocker. The paper should just reference similar resolution choices from prior work to justify the approach.

So my final assessment is revise. The main issues are the missing concurrent papers from March 2026 (ULTRA and Psi-Zero on loco-manipulation), the sparse IRM resolution worth noting, and the evaluation breadth as an ongoing CoRL risk factor.

Scoring it out: novelty is solid at 4/5, feasibility drops to 3/5 due to the sparsity and concurrent work, clarity stays at 4/5, and impact is 4/5, averaging to 3.75 overall.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be29bd2b-43cb-466c-8890-6fa4bfd763cf",
  "isSidechain": false,
  "requestId": "req_011CatwSMGbgPFUCSoDoM14j",
  "type": "assistant",
  "uuid": "dedf5dbe-8559-4268-84ec-fb81e82f6c1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013vKhFManJK2kLCXhEWXgtP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6005,
      "cache_read_input_tokens": 48066,
      "output_tokens": 3867,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3867,
          "cache_read_input_tokens": 48066,
          "cache_creation_input_tokens": 6005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6005
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

_source line 22 · 2026-05-10T13:08:34.742Z_

Now I have the research I need. Let me assess the Round 7 submission against the Round 6 required fixes and any new issues.

**Round 6 fix verification:**
- Fix 1 (DemoHLM conceptual comparison): ✅ Addressed — "DemoHLM code has not been publicly released as of May 2026, making reimplementation infeasible within the 20-day window"
- Fix 2 (language correction): ✅ Addressed — "without any separate stance-placement planning" is used correctly
- Fix 3 (HumanX/XMimic): ✅ Added to landscape
- Fix 4 (OmniRetarget as conceptual comparison): ✅ Addressed — estimated 10-14 day setup cost cited as reason

**Research findings:**
- Isaac Lab PR #3259's disjoint navigation claim: **confirmed** — no SE(3) object-centric stance encoding exists
- DreamGen scope claim: **confirmed** — stationary manipulation only, G1 GR1 used only for upper-body
- Core SE(3) stance+arm coupling for humanoid demo multiplication: **no competitor found**
- Two uncited March 2026 concurrent papers: ULTRA (arXiv:2603.03279) and Psi-Zero (arXiv:2603.12263)

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "Research confirms no existing work performs coupled SE(3) stance+arm encoding for humanoid loco-manipulation demo multiplication; the gap in Isaac Lab PR #3259 is real and unfilled. The bipedal IRM adaptation over wheeled-platform IRMs (MoMaGen, MoMa-Pos) is a genuine technical challenge, though it's framed correctly as integration rather than novel technique."
    },
    "feasibility": {
      "score": 3,
      "rationale": "Compute stays within the 200 H100h hard constraint (87-110h manual), but the 20-day timeline concentrating all three non-trivial contributions (SE(3) API extension, IRM integration, combinatorial composition) into Days 3-12 with a single identified critical-path bottleneck leaves minimal slack; the 50K-pose 6D IRM grid is also sparse (~5-6 points per dimension) and may require resolution tuning that isn't budgeted."
    },
    "clarity": {
      "score": 4,
      "rationale": "After seven rounds the technical characterization is precise: Contribution 1 crystallization is quotable, compatibility filtering is formally defined with empirical filtering rates, the Gantt chart identifies the critical path, and the K×M×P×Q×R formula makes the scaling claim verifiable."
    },
    "impact": {
      "score": 4,
      "rationale": "Addresses the #1 cited bottleneck in humanoid robot learning with a principled infrastructure contribution grounded in validated prior art; the ≥20pp effect-size target is explicitly grounded in MimicGen scaling results, though the sim-only evaluation and 2-task scope limit near-term transfer confidence."
    }
  },
  "issues": [
    "MISSING CONCURRENT CITATION — ULTRA (arXiv:2603.03279, March 2026): 'Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation' uses physics-driven neural retargeting to translate large-scale MoCap to humanoid embodiments while preserving physical plausibility for contact-rich loco-manipulation. Although retargeting-based (not SE(3) demo multiplication), it is a direct March 2026 paper on whole-body humanoid loco-manipulation data generation and CoRL reviewers will expect to see it. Positioning is identical to OmniRetarget: 'ULTRA [arXiv:2603.03279] scales loco-manipulation data via physics-preserving MoCap retargeting — a complementary human-data-driven paradigm that requires large MoCap libraries, cannot combinatorially compose subtask segments across scene configurations, and does not address the manipulation-stance feasibility problem for new object positions.' One sentence in the landscape alongside OmniRetarget is sufficient.",
    "MISSING CONCURRENT CITATION — Psi-Zero / Ψ₀ (arXiv:2603.12263, March 2026): 'Open Foundation Model Towards Universal Humanoid Loco-Manipulation' pre-trains a VLM on 800 hours of egocentric human video, then post-trains a flow-based action expert on 30 hours of robot data, achieving 40% better success with 10× less robot data than baselines. Foundation model scaling (not procedural generation), but it is a March 2026 paper in the same problem space. CoRL reviewers will recognize it. One sentence alongside EgoHumanoid/HoMMI/HuMI/HumanX as a human-data-driven foundation model approach complementary to LocoMimicGen's combinatorial synthetic generation from ≤20 robot demos.",
    "IRM GRID RESOLUTION SPARSENESS NOT ACKNOWLEDGED: The proposed 50K-pose sampling across 6D configuration space (SE(2) base pose × squat depth × foot spread × weight distribution) yields approximately 50,000^(1/6) ≈ 5-6 points per dimension — a very coarse grid for reachability boundary detection. At this resolution, reachability map boundaries may be insufficiently smooth to reliably filter edge cases where the manipulator is at the limit of its workspace. The paper should acknowledge this resolution choice and reference how analogous IRM work (MoMa-Pos, MoMaGen) selected grid resolution, or note that it can be refined offline post-hoc without additional training cost.",
    "EVALUATION BREADTH RISK (ONGOING): Two primary tasks with sim-only evaluation continues to be the most likely cause of CoRL 2026 rejection or major revision requests. The existing scene-space-depth defense ('150 configurations per task vs. O(1) in MoMaGen/HumanoidGen') is the best available argument within the 20-day constraint, but it is a methodological claim that reviewers accustomed to DexMimicGen (9 tasks) and HumanoidGen (6 tasks) may not find sufficient. The paper should consider whether the supplementary articulated-object task can be elevated to co-primary status if the composition engine validates on schedule by Day 12, as three tasks with three contributions exercised would substantially reduce this risk."
  ],
  "feedback": "All four Round 6 required fixes are correctly implemented: DemoHLM is a conceptual comparison citing published numbers, the language reads 'stance-placement planning' not 'navigation planning,' HumanX/XMimic is in the landscape, and OmniRetarget is correctly scoped as a conceptual comparison. The idea's technical foundation is now solid and the gap against Isaac Lab PR #3259 is independently confirmed by research.\n\n**Fix 1 (required, 1 sentence)**: Add ULTRA (arXiv:2603.03279, March 2026) to the landscape paragraph alongside OmniRetarget. Frame it as a complementary physics-preserving MoCap retargeting approach that requires large motion capture libraries and cannot perform combinatorial subtask segment composition — the same positioning as OmniRetarget. CoRL reviewers will notice its absence.\n\n**Fix 2 (required, 1 sentence)**: Add Psi-Zero/Ψ₀ (arXiv:2603.12263, March 2026) to the landscape alongside EgoHumanoid/HoMMI/HuMI/HumanX as a foundation model pre-training approach. One sentence: 'Ψ₀ [arXiv:2603.12263] pre-trains a VLM on 800 hours of human egocentric video and post-trains a flow-based action expert on 30 hours of robot data — a human-data-driven scaling paradigm orthogonal to LocoMimicGen's combinatorial spatial synthesis from ≤20 teleoperated robot demonstrations.'\n\n**Fix 3 (optional but recommended, 1 sentence)**: Acknowledge the IRM grid resolution choice explicitly — something like 'The 50K-pose resolution (~5-6 samples per dimension) is consistent with offline IRM construction in prior work (MoMa-Pos, Vahrenkamp et al.) and can be refined post-hoc at no additional training cost.' This preempts a reviewer question about whether the reachability boundary is smooth enough at this resolution.\n\n**Fix 4 (contingency plan, 1 sentence)**: Add a sentence noting that if the composition engine validates on Task 1 by Day 11 rather than Day 12, the supplementary articulated-object task will be elevated to co-primary status in the evaluation, bringing the primary task count to three. This signals execution awareness and reduces the evaluation-breadth risk without changing the critical path.",
  "reason": "All Round 6 fixes addressed; two concurrent March 2026 papers (ULTRA arXiv:2603.03279, Psi-Zero arXiv:2603.12263) are missing from the landscape and will be noticed by CoRL reviewers; average score 3.75 remains below the 4.0 pass threshold due to timeline feasibility risk and 2-task sim-only evaluation scope."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dedf5dbe-8559-4268-84ec-fb81e82f6c1f",
  "isSidechain": false,
  "requestId": "req_011CatwSMGbgPFUCSoDoM14j",
  "type": "assistant",
  "uuid": "9dc10788-90a6-4c4f-a0ce-d915aa13747d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013vKhFManJK2kLCXhEWXgtP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6005,
      "cache_read_input_tokens": 48066,
      "output_tokens": 3867,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6005,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3867,
          "cache_read_input_tokens": 48066,
          "cache_creation_input_tokens": 6005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6005
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

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "9dc10788-90a6-4c4f-a0ce-d915aa13747d",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify LocoMimicGen against SOTA and assess feasibility for CoRL 2026",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "9dc10788-90a6-4c4f-a0ce-d915aa13747d",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify LocoMimicGen against SOTA and assess feasibility for CoRL 2026",
  "sessionId": "99d62b10-815d-4248-b519-008464906ca6"
}
```

---
