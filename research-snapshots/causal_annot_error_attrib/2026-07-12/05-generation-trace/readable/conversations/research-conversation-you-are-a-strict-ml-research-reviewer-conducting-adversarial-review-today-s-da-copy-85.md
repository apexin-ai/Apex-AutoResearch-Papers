# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-18 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 8
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/73519ec3-ea57-4f39-9bd9-306b1dc4b1d4.jsonl`
- **Structured JSON:** [`52df000957575ddca210.json`](../../sessions/52/52df000957575ddca210.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T17:28:56.548Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T17:28:56.548Z",
  "sessionId": "73519ec3-ea57-4f39-9bd9-306b1dc4b1d4",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-18 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **## Seed 4: Open-Vocabulary Affordance Zero-Shot VLA\n\nObjective: CoRL 2026 submission.\n\nDirection: Traditional affordance methods and VLAs rely on fixed category annotations and struggle with open-world unknown objects and free-form interaction instructions. CoA-VLA (arXiv 2412.20451, December 2024) integrates affordance chain-of-reasoning into VLA, but uses 4 predefined structured affordance types (object, grasp, spatial, motion) — not truly open-vocabulary — and cannot handle free-form interaction descriptions like \"use this thing to wipe off the dust over there.\" GeneralVLA (arXiv 2602.04315, February 2026) achieves zero-shot affordance perception and manipulation trajectory generation through VLM+SAM, but is a modular three-stage pipeline (affordance perception → trajectory planning → low-level control), not a unified end-to-end VLA — with information loss between modules and inability to jointly optimize. OVAL-Prompt (ICRA 2024 VLMNM Workshop, arXiv 2404.11000) achieves truly open-vocabulary affordance localization, but only performs detection/localization without generating actions. AffordDP (CVPR 2025, arXiv 2412.03142) achieves affordance cross-category transfer through 3D contact points and trajectories, but completely lacks language conditioning. Core gap: No work unifies open-vocabulary affordance reasoning into an end-to-end VLA for zero-shot manipulation — existing work either has fixed affordance types (CoA-VLA), or is a modular pipeline (GeneralVLA), or only does detection without actions (OVAL-Prompt), or lacks language (AffordDP).\n\nSeed Papers:\n- \"OpenVLA: An Open-Source Vision-Language-Action Model\" (Kim et al., CoRL 2024, arXiv 2406.09246)\n  — 7B parameter open-source VLA, trained on 970K real robot demonstrations, establishing the VLA open-source paradigm. The base architecture for this work — integrating open-vocabulary affordance reasoning on top.\n- \"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance\" (Li et al., arXiv 2412.20451, December 2024)\n  — Integrates affordance chain-of-reasoning into VLA: model sequentially reasons about object affordance, grasp affordance, spatial affordance, and motion affordance before predicting actions. Uses visual-language collaborative injection module. Surpasses OpenVLA and Octo. Key limitation: 4 affordance types are predefined/structured, not open-vocabulary — cannot handle arbitrary natural language descriptions of novel interactions.\n- \"GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning\" (Ma et al., arXiv 2602.04315, February 2026)\n  — Hierarchical three-module pipeline: (1) VLM+SAM affordance perception for keypoint detection, (2) mid-level planning agent for trajectory generation, (3) low-level control policy. Achieves zero-shot manipulation across 14 tasks without real-world data. Key limitation: Modular pipeline, not end-to-end — affordance module, trajectory planner, and controller are separated, with information bottlenecks between modules.\n- \"OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding\" (Tong et al., ICRA 2024 VLMNM Workshop, arXiv 2404.11000)\n  — Prompt-based method combining VLM for object part segmentation and LLM for part-affordance grounding mapping, achieving open-vocabulary affordance localization without prior training. Competitive with supervised methods on localization benchmarks. Key limitation: Only performs affordance detection/localization, does not generate robot actions — a perception module, not a complete manipulation system.\n- \"AffordDP: Generalizable Diffusion Policy with Transferable Affordance\" (Wu et al., CVPR 2025, arXiv 2412.03142)\n  — Models manipulation priors through 3D contact points and post-contact trajectories, achieving affordance cross-category transfer using visual models + point cloud registration. Affordance-guided diffusion policy generates actions. Key limitation: No language conditioning — affordances are geometric/contact-based, not language-driven, cannot handle open-vocabulary instructions.\n\nKnown Gap:\n- CoA-VLA integrates affordance into VLA but uses predefined structured types, does not support open vocabulary\n- GeneralVLA does zero-shot affordance manipulation but is a modular pipeline, not end-to-end\n- OVAL-Prompt does open-vocabulary affordance but only detection, no action generation\n- AffordDP does affordance cross-category transfer but no language conditioning\n- VoxPoser (CoRL 2023, arXiv 2307.05973) uses LLM to generate 3D affordance/constraint maps but is modular, no end-to-end learning\n- No work unifies open-vocabulary affordance reasoning into end-to-end VLA\n\nIn Scope: Methods unifying open-vocabulary affordance reasoning into end-to-end VLA architecture. Specifically includes: text prompt-driven open-vocabulary affordance feature activation mechanism, universal shape-function-interaction attribute association learning, end-to-end joint training of affordance reasoning and action generation, zero-shot generalization to unseen object categories and novel language interaction instructions. The core contribution should be a unified architecture, not a modular concatenation of affordance detection + action generation.\n\nOut of Scope: Predefined fixed affordance types (CoA-VLA already done). Modular affordance pipelines (GeneralVLA/VoxPoser already done). Affordance detection only without actions (OVAL-Prompt already done). Affordance transfer without language conditioning (AffordDP already done). Pure affordance benchmarking/analysis.\n\nContribution Type: Method contribution. Output must include (1) unified architecture design for open-vocabulary affordance and VLA, (2) end-to-end training strategy for affordance reasoning and action generation, (3) experimental validation of zero-shot generalization on unseen objects and novel interaction instructions, demonstrating advantages over structured affordance VLA and modular methods.\n\nEvaluation Protocol:\nTraining: Based on OpenVLA architecture, integrating open-vocabulary affordance module. Training data uses LIBERO + affordance annotation data (e.g., AGD20K/UMD Affordance).\nEvaluation Metrics:\n- Primary metric: Zero-shot manipulation success rate on unseen object categories\n- Novel interaction instruction generalization: Language interaction descriptions unseen during training (e.g., train on \"pick up,\" test on \"scoop out\")\n- Affordance localization precision: Compare with detection methods like OVAL-Prompt (ensure affordance understanding itself does not degrade)\n- Manipulation success rate: Compare with standard VLA baselines (ensure adding affordance does not degrade known task performance)\n- Baseline comparisons:\n  1. Affordance-free VLA (OpenVLA direct fine-tuning)\n  2. Structured affordance VLA (CoA-VLA reproduction)\n  3. Modular affordance pipeline (GeneralVLA approach)\n  4. Affordance detection + independent policy (OVAL-Prompt + policy learning)\n  5. LLM affordance map + planning (VoxPoser approach)\n- Ablation studies: Open-vocabulary affordance vs. fixed-type affordance, end-to-end vs. staged training, text-driven affordance vs. vision-driven affordance\n- Cross-object transfer tests: Shape-function association generalization (e.g., if trained on shovel's \"scooping\" affordance, can the model activate the same interaction for novel shovel-like tools?)\n- Free-form instruction tests: Non-templated natural language instruction understanding\n\nBuilding Blocks: OpenVLA codebase (VLA base architecture); CoA-VLA codebase (affordance VLA baseline); OVAL-Prompt codebase (open-vocabulary affordance detection reference); AGD20K/UMD Affordance datasets (affordance annotations); LIBERO benchmark (manipulation task evaluation); DINOv2/SigLIP visual encoders; SAM2 (segmentation); HuggingFace transformers + accelerate; CLIP/SigLIP (open-vocabulary semantic alignment).\n\nHard Constraints:\nCompute: ≤200 H100-hours. Strategy: Fine-tune based on 7B VLA, affordance module leveraging pre-trained VLM features (e.g., CLIP/SigLIP) to reduce training requirements. Training ~80 H100-hours, baseline reproduction ~50 H100-hours, ablation ~40 H100-hours, generalization testing ~30 H100-hours.\nEvaluation: Must validate zero-shot generalization on unseen object categories. Must include free-form language instruction tests. Must include ≥4 baselines. Must report both affordance precision and manipulation success rate. Must include ablation studies and cross-object transfer tests.\n\nExploration Directions: (1) End-to-end activation of VLM internal affordance features: Rather than adding an external affordance detection module to VLA, activate interaction-relevant visual features within VLA's VLM backbone network directly through language instructions. Key insight: Large-scale VLMs (e.g., PaliGemma, SigLIP) have already learned extensive shape-function associations during pre-training (\"knives can cut,\" \"bowls can hold\"), only requiring suitable activation mechanisms to release this implicit knowledge. (2) Affordance as intermediate reasoning tokens: Rather than explicitly outputting affordance heatmaps, have VLA generate a set of \"affordance reasoning tokens\" before generating action token sequences (similar to CoA-VLA's chain reasoning but open-vocabulary). These tokens encode interaction possibilities of objects in the current scene, then condition subsequent action generation. Differs from CoA-VLA: not limited to 4 predefined types; reasoning content is dynamically determined by language instructions. (3) Contrastive learning for universal shape-function-interaction mapping: Add contrastive objective during VLA training to pull together different-shaped objects with similar functions (various \"tools that can scoop things\") in affordance feature space, and push apart similar-shaped objects with different functions (decorative bowl vs. functional bowl). More flexible than CoA-VLA's structured types — any natural language-described interaction can participate in contrasting. (4) Knowledge distillation for zero-shot affordance reasoning: Use large VLMs' (e.g., GPT-4V level) zero-shot affordance reasoning capability (\"how can this object be interacted with?\") as teacher signals, distilling into small VLA. Large models have rich commonsense knowledge and can generate affordance descriptions for virtually any object, but are too large to deploy directly on robots. (5) Affordance consistency self-supervision: The same object under different language descriptions should have consistent affordance responses (\"grab the handle\" vs. \"pick it up by the stick part\" describe the same interaction). Use this consistency as self-supervision signals, reducing dependency on fine-grained affordance annotations.\n\nAvoid:\n- Using predefined fixed affordance types — duplicates CoA-VLA\n- Modular pipeline (affordance detection → planning → control) — duplicates GeneralVLA/VoxPoser, and prevents end-to-end optimization\n- Only doing affordance detection without actions — duplicates OVAL-Prompt\n- Ignoring CoA-VLA baseline — it is the most recent affordance + VLA work; must directly compare\n- Ignoring GeneralVLA — it is the most recent zero-shot affordance manipulation work; must clarify advantages of end-to-end vs. modular\n- Reporting results only on within-training-distribution objects — the core value of open vocabulary is on out-of-distribution objects\n- Over-relying on affordance annotation data — should design methods to reduce annotation requirements\n\nIdea Generation Quality Constraints (Hard rules based on historical cases):\n\n1. No strawman problems: Any claim of \"existing methods assume X\" or \"existing methods fail on Y\" must cite specific paragraphs from specific papers as evidence.\n\n2. No pure observation ideas: Output must include a complete method, not merely analysis/benchmark/empirical study.\n\n3. No mediocre methods: Methods must answer:\n   - Core insight: Large-scale VLMs have already implicitly learned rich shape-function association knowledge during pre-training; CoA-VLA released part of it through structured reasoning chains, but is limited by predefined types. We directly activate corresponding affordance features within VLA through open-vocabulary language instructions, fully releasing VLM's implicit shape-function knowledge into action generation.\n   - Why non-obvious: (1) CoA-VLA (December 2024) is the first work integrating affordance chain reasoning into VLA; affordance + VLA itself is a new paradigm; (2) open-vocabulary requires solving the infinite-dimensional affordance space problem — unlike 4 fixed types that can be directly classified; (3) end-to-end training of open-vocabulary affordance requires affordance annotation data, but such data is scarce — needs training strategies that reduce annotation dependency.\n   - What information is exploited: Implicit shape-function association knowledge from VLM pre-training — which neither 2D visual VLAs nor fixed-type affordance methods fully utilize.\n   - Mechanistic argument: When given a free-form language instruction (e.g., \"scoop the rice\"), the VLM internally already encodes knowledge that \"scooping requires a concave container-shaped tool.\" Through suitable activation mechanisms, this knowledge can be transformed into affordance attention in visual feature space — focusing on regions in the scene with corresponding geometric functional properties, then conditioning action generation. More flexible than CoA-VLA's fixed 4-type reasoning because affordance is dynamically defined by language.\n\n4. No duplicating existing work: Each core technical component must be confirmed with at least 3 different search queries to have no directly related work.\n\n5. No padding experiments:\n   - \"Delete experiment test\": Keep only the method description — does it teach the reader something non-trivial? Yes — VLM implicit shape-function knowledge can drive VLA action generation through open-vocabulary activation.\n   - \"Baseline fear test\": If CoA-VLA's 4 structured types already cover most scenarios, is the paper still valuable? Must prove open-vocabulary methods' advantages on free-form instructions and novel interactions.\n   - \"Citation test\": Will people cite the numbers or the insight 5 years later? The insight — open-vocabulary affordance in end-to-end VLA paradigm.\n\n6. The following method patterns are rejected (unless with extremely strong structural reasons):\n   - \"Add module X\" — Why this specific structure?\n   - \"Train on data Y\" — Is data construction itself a contribution?\n   - \"Transfer Z from domain A to domain B\" — What is the structural analogy?\n   - \"Combine P and Q\" — Where is the synergy? Combining open-vocabulary detection (OVAL-Prompt) with VLA — must prove end-to-end joint training outperforms simple concatenation.\n   - \"Use more/larger/stronger X\" — Scale is not a method contribution.\n\nCompetition Warning: CoA-VLA (December 2024) is the most recent affordance + VLA — uses structured reasoning chains but not open-vocabulary. GeneralVLA (February 2026) does zero-shot affordance manipulation but is a modular pipeline. OVAL-Prompt (ICRA 2024 Workshop) does open-vocabulary affordance detection but no actions. AffordDP (CVPR 2025) does affordance cross-category transfer but no language. VoxPoser (CoRL 2023) uses LLM to generate 3D affordance maps but is modular. π0 (Physical Intelligence) and RT-2 and other large VLAs may implicitly contain partial affordance knowledge but do not explicitly leverage it. Differentiation core: The only work integrating open-vocabulary affordance reasoning end-to-end into a unified VLA architecture. Highest risk: CoA-VLA is closest in space; if its author team quickly extends to open-vocabulary, differentiation shrinks. Monitor: CoA-VLA author team, GeneralVLA author team, Physical Intelligence (whether π0 follow-ups will integrate affordance).\n\nTags: direction=open_vocab_affordance_zero_shot_vla, contribution_type=method, sub_direction=unified_affordance_vla_end_to_end, target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-18?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 10/10)\n{\n  \"title\": \"Open-Vocabulary Affordance Chain-of-Reasoning for End-to-End VLA\",\n  \"core_problem\": \"Current affordance-integrated VLAs (CoA-VLA, PALM) use 3-4 predefined structured affordance types, making them unable to handle free-form interaction descriptions (e.g., 'use this to wipe off the dust') or reason about novel object-interaction pairings unseen during training.\",\n  \"opportunity\": \"CoT-VLA (CVPR 2025) proved that generating intermediate reasoning tokens before actions improves VLA by 17% in real-world tasks, while 3D-AffordanceLLM (ICLR 2025) demonstrated LLMs can perform open-vocabulary affordance detection with ~8% mIoU improvement. The natural synthesis — open-vocabulary affordance as the reasoning content in a CoT-VLA framework — remains unexplored. This is feasible now because both components (reasoning VLA and open-vocab affordance) are independently validated.\",\n  \"landscape\": \"CoA-VLA (ICCV 2025) integrates 4 structured affordance types (object, grasp, spatial, movement) into VLA chain reasoning, surpassing OpenVLA. PALM (arXiv 2026) similarly uses 4 structured affordance representations (object relevance, contact geometry, spatial placements, motion dynamics) for long-horizon tasks, achieving 91.8% on LIBERO-LONG. CoT-VLA (CVPR 2025) generates future visual goal frames as intermediate reasoning tokens, improving real-world success by 17%. DualCoT-VLA (arXiv 2026) introduces parallel visual-linguistic CoT with learnable query tokens. VLA-R1 (arXiv 2025) applies RLVR to enhance step-by-step reasoning in VLAs, improving affordance perception by 17.78%. LaST₀ (arXiv 2026) uses latent spatio-temporal CoT with a dual-expert Mixture-of-Transformers architecture. AffordGrasp (IROS 2025) performs open-vocabulary task-oriented grasping via VLM in-context affordance reasoning but is not end-to-end trainable. Affogato (arXiv 2025) provides 150K open-vocabulary 3D affordance annotations but targets grounding, not action generation. None support open-vocabulary affordance reasoning within an end-to-end VLA — all use fixed/structured types or non-affordance-specific reasoning, leaving a clear gap for dynamic, language-driven affordance reasoning before action generation.\",\n  \"approach\": \"We propose OVA-VLA, which replaces fixed affordance taxonomies with free-form, LLM-generated affordance chain-of-reasoning within an end-to-end VLA. Using Qwen3-VL-2B as backbone via the VLA Foundry framework, the model autoregressively generates open-vocabulary affordance rationales (e.g., 'the mug handle affords a lateral pinch grasp; rotate wrist 90° to pour into the bowl') before predicting action tokens, enabling generalization to novel interaction descriptions and unseen object-affordance pairings. Training data is created by augmenting LIBERO and RoboCasa365 demonstrations with diverse free-form affordance annotations generated at scale by Qwen3-VL-235B-Instruct, avoiding the manual effort of designing fixed affordance schemas. We evaluate on LIBERO-LONG, RoboCasa365, and a new open-vocabulary generalization split with paraphrased/novel interaction descriptions, with key ablations comparing open-vocabulary vs. fixed-type affordance reasoning and measuring the impact of annotation diversity on out-of-distribution generalization.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~500-800h A100 (10-15 training runs × ~50-80h each, including debugging and restarts)\",\n      \"gpu_utilization\": \"60-80% GPU idle — GPUs sit unused during human code writing, debugging, result analysis, and sleep cycles; each experiment-debug loop has multi-hour human latency\",\n      \"timeline\": \"3-5 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"$750-1200 (at ~$1.50/h A100 80GB on specialized cloud providers)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~600-1000h A100 (agent runs more experiments but human approval gates reduce wasted runs)\",\n      \"gpu_utilization\": \"30-50% idle — significant improvement over manual; agent queues next experiment during current run, but still waits for human approval on design decisions and result interpretation\",\n      \"timeline\": \"6-10 weeks\",\n      \"team\": \"1 researcher, ~1hr/day review and approval of experiment plans and results\",\n      \"claude_api_cost\": \"$200-500 (2000-5000 turns for code generation, experiment design, result analysis)\",\n      \"estimated_gpu_cost\": \"$900-1500\",\n      \"risk_note\": \"Affordance annotation quality — auto-generated free-form annotations from Qwen3-VL-235B may contain hallucinated spatial relationships; human spot-checking of annotation quality is critical before full-scale training\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~1500-2500h A100 (3-5× more experiment exploration including hyperparameter sweeps, annotation diversity ablations, and failed architecture variants; near-zero idle)\",\n      \"gpu_utilization\": \"GPU idle <5% — agent continuously pipelines data annotation, training, and evaluation; next experiment is queued before current one finishes; overnight/weekend runs proceed without pause\",\n      \"timeline\": \"1-3 weeks with 8× A100 cluster available continuously\",\n      \"team\": \"0 (initial setup only: define benchmark suite, configure VLA Foundry, set evaluation metrics)\",\n      \"claude_api_cost\": \"$500-1000 (5000-10000 turns for full autonomous experiment loop)\",\n      \"estimated_gpu_cost\": \"$2250-3750\",\n      \"speed_bottleneck\": \"GPU count is primary bottleneck — with 8× A100 the agent can parallelize training runs and annotation generation; secondary bottleneck is Qwen3-VL-235B inference throughput for generating 200K+ affordance annotations across LIBERO+RoboCasa365 datasets\",\n      \"risk_note\": \"Without human oversight, the agent may over-optimize for benchmark metrics while producing affordance reasoning that is syntactically diverse but semantically degenerate (e.g., generic descriptions that don't capture true physical affordances); recommend automated diversity metrics and periodic human audit checkpoints\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (abstract Sep 19, paper Sep 24, 2026) — top-tier ML venue, best fit for method contribution\",\n    \"AAAI 2027 (abstract Jul 21, paper Jul 28, 2026) — top-tier AI venue, earlier deadline\",\n    \"CoRL 2026 (abstract May 26, paper May 29, 2026) — top-tier robotics venue, tight but feasible with auto-research\",\n    \"CVPR 2027 (abstract Nov 7, paper Nov 13, 2026) — top-tier vision venue, fallback if earlier submissions need revision\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance (ICCV 2025)\",\n    \"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (CVPR 2025)\",\n    \"3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds (ICLR 2025)\",\n    \"PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation (arXiv 2026)\",\n    \"DualCoT-VLA: Visual-Linguistic Chain of Thought via Parallel Reasoning for Vision-Language-Action Models (arXiv 2026)\",\n    \"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models (arXiv 2025)\",\n    \"AffordGrasp: In-Context Affordance Reasoning for Open-Vocabulary Task-Oriented Grasping in Clutter (IROS 2025)\",\n    \"VLA Foundry: A Unified Framework for Training Vision-Language-Action Models (arXiv 2026)\",\n    \"LaST₀: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model (arXiv 2026)\"\n  ],\n  \"description\": \"We propose OVA-VLA, the first VLA framework that uses open-vocabulary affordance reasoning as intermediate chain-of-thought tokens for end-to-end robotic manipulation. While CoA-VLA (ICCV 2025) and PALM demonstrate that structured affordance reasoning with 3-4 fixed types improves VLA performance, and 3D-AffordanceLLM (ICLR 2025) shows LLMs can perform open-vocabulary affordance detection, no existing method combines these insights. OVA-VLA bridges this gap by building on Qwen3-VL-2B via VLA Foundry, autoregressively generating free-form affordance rationales before predicting action tokens. Training annotations are produced at scale by Qwen3-VL-235B-Instruct, eliminating manual affordance schema design. We evaluate on LIBERO-LONG, RoboCasa365, and a novel open-vocabulary generalization split with paraphrased and unseen interaction descriptions. Key ablations compare open-vocabulary vs. fixed-type affordance reasoning and measure annotation diversity's impact on generalization. No concurrent work addresses this specific gap — existing CoT-VLA variants (DualCoT-VLA, LaST₀) use non-affordance reasoning, while open-vocab affordance methods (AffordGrasp, Affogato) lack end-to-end action generation. This timely synthesis targets ICLR 2027 as a top-tier contribution.\",\n  \"project_name\": \"ov_afford_cot_vla\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: error\nIssues: []\nFeedback: Review subprocess failed (timeout or parse error)\n\n### Round 2 review\nVerdict: error\nIssues: []\nFeedback: Review subprocess failed (timeout or parse error)\n\n### Round 3 review\nVerdict: error\nIssues: []\nFeedback: Review subprocess failed (timeout or parse error)\n\n### Round 4 review\nVerdict: error\nIssues: []\nFeedback: Review subprocess failed (timeout or parse error)\n\n### Round 5 review\nVerdict: error\nIssues: []\nFeedback: Review subprocess failed (timeout or parse error)\n\n### Round 6 review\nVerdict: error\nIssues: []\nFeedback: Review subprocess failed (timeout or parse error)\n\n### Round 7 review\nVerdict: error\nIssues: []\nFeedback: Review subprocess failed (timeout or parse error)\n\n### Round 8 review\nVerdict: error\nIssues: []\nFeedback: Review subprocess failed (timeout or parse error)\n\n### Round 9 review\nVerdict: error\nIssues: []\nFeedback: Review subprocess failed (timeout or parse error)\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-18T17:28:56.557Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T17:28:56.557Z",
  "sessionId": "73519ec3-ea57-4f39-9bd9-306b1dc4b1d4"
}
```

---

## Round 1

6 recorded events

### User

_source line 3 · 2026-05-18T17:28:56.644Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-18 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **## Seed 4: Open-Vocabulary Affordance Zero-Shot VLA

Objective: CoRL 2026 submission.

Direction: Traditional affordance methods and VLAs rely on fixed category annotations and struggle with open-world unknown objects and free-form interaction instructions. CoA-VLA (arXiv 2412.20451, December 2024) integrates affordance chain-of-reasoning into VLA, but uses 4 predefined structured affordance types (object, grasp, spatial, motion) — not truly open-vocabulary — and cannot handle free-form interaction descriptions like "use this thing to wipe off the dust over there." GeneralVLA (arXiv 2602.04315, February 2026) achieves zero-shot affordance perception and manipulation trajectory generation through VLM+SAM, but is a modular three-stage pipeline (affordance perception → trajectory planning → low-level control), not a unified end-to-end VLA — with information loss between modules and inability to jointly optimize. OVAL-Prompt (ICRA 2024 VLMNM Workshop, arXiv 2404.11000) achieves truly open-vocabulary affordance localization, but only performs detection/localization without generating actions. AffordDP (CVPR 2025, arXiv 2412.03142) achieves affordance cross-category transfer through 3D contact points and trajectories, but completely lacks language conditioning. Core gap: No work unifies open-vocabulary affordance reasoning into an end-to-end VLA for zero-shot manipulation — existing work either has fixed affordance types (CoA-VLA), or is a modular pipeline (GeneralVLA), or only does detection without actions (OVAL-Prompt), or lacks language (AffordDP).

Seed Papers:
- "OpenVLA: An Open-Source Vision-Language-Action Model" (Kim et al., CoRL 2024, arXiv 2406.09246)
  — 7B parameter open-source VLA, trained on 970K real robot demonstrations, establishing the VLA open-source paradigm. The base architecture for this work — integrating open-vocabulary affordance reasoning on top.
- "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance" (Li et al., arXiv 2412.20451, December 2024)
  — Integrates affordance chain-of-reasoning into VLA: model sequentially reasons about object affordance, grasp affordance, spatial affordance, and motion affordance before predicting actions. Uses visual-language collaborative injection module. Surpasses OpenVLA and Octo. Key limitation: 4 affordance types are predefined/structured, not open-vocabulary — cannot handle arbitrary natural language descriptions of novel interactions.
- "GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning" (Ma et al., arXiv 2602.04315, February 2026)
  — Hierarchical three-module pipeline: (1) VLM+SAM affordance perception for keypoint detection, (2) mid-level planning agent for trajectory generation, (3) low-level control policy. Achieves zero-shot manipulation across 14 tasks without real-world data. Key limitation: Modular pipeline, not end-to-end — affordance module, trajectory planner, and controller are separated, with information bottlenecks between modules.
- "OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding" (Tong et al., ICRA 2024 VLMNM Workshop, arXiv 2404.11000)
  — Prompt-based method combining VLM for object part segmentation and LLM for part-affordance grounding mapping, achieving open-vocabulary affordance localization without prior training. Competitive with supervised methods on localization benchmarks. Key limitation: Only performs affordance detection/localization, does not generate robot actions — a perception module, not a complete manipulation system.
- "AffordDP: Generalizable Diffusion Policy with Transferable Affordance" (Wu et al., CVPR 2025, arXiv 2412.03142)
  — Models manipulation priors through 3D contact points and post-contact trajectories, achieving affordance cross-category transfer using visual models + point cloud registration. Affordance-guided diffusion policy generates actions. Key limitation: No language conditioning — affordances are geometric/contact-based, not language-driven, cannot handle open-vocabulary instructions.

Known Gap:
- CoA-VLA integrates affordance into VLA but uses predefined structured types, does not support open vocabulary
- GeneralVLA does zero-shot affordance manipulation but is a modular pipeline, not end-to-end
- OVAL-Prompt does open-vocabulary affordance but only detection, no action generation
- AffordDP does affordance cross-category transfer but no language conditioning
- VoxPoser (CoRL 2023, arXiv 2307.05973) uses LLM to generate 3D affordance/constraint maps but is modular, no end-to-end learning
- No work unifies open-vocabulary affordance reasoning into end-to-end VLA

In Scope: Methods unifying open-vocabulary affordance reasoning into end-to-end VLA architecture. Specifically includes: text prompt-driven open-vocabulary affordance feature activation mechanism, universal shape-function-interaction attribute association learning, end-to-end joint training of affordance reasoning and action generation, zero-shot generalization to unseen object categories and novel language interaction instructions. The core contribution should be a unified architecture, not a modular concatenation of affordance detection + action generation.

Out of Scope: Predefined fixed affordance types (CoA-VLA already done). Modular affordance pipelines (GeneralVLA/VoxPoser already done). Affordance detection only without actions (OVAL-Prompt already done). Affordance transfer without language conditioning (AffordDP already done). Pure affordance benchmarking/analysis.

Contribution Type: Method contribution. Output must include (1) unified architecture design for open-vocabulary affordance and VLA, (2) end-to-end training strategy for affordance reasoning and action generation, (3) experimental validation of zero-shot generalization on unseen objects and novel interaction instructions, demonstrating advantages over structured affordance VLA and modular methods.

Evaluation Protocol:
Training: Based on OpenVLA architecture, integrating open-vocabulary affordance module. Training data uses LIBERO + affordance annotation data (e.g., AGD20K/UMD Affordance).
Evaluation Metrics:
- Primary metric: Zero-shot manipulation success rate on unseen object categories
- Novel interaction instruction generalization: Language interaction descriptions unseen during training (e.g., train on "pick up," test on "scoop out")
- Affordance localization precision: Compare with detection methods like OVAL-Prompt (ensure affordance understanding itself does not degrade)
- Manipulation success rate: Compare with standard VLA baselines (ensure adding affordance does not degrade known task performance)
- Baseline comparisons:
  1. Affordance-free VLA (OpenVLA direct fine-tuning)
  2. Structured affordance VLA (CoA-VLA reproduction)
  3. Modular affordance pipeline (GeneralVLA approach)
  4. Affordance detection + independent policy (OVAL-Prompt + policy learning)
  5. LLM affordance map + planning (VoxPoser approach)
- Ablation studies: Open-vocabulary affordance vs. fixed-type affordance, end-to-end vs. staged training, text-driven affordance vs. vision-driven affordance
- Cross-object transfer tests: Shape-function association generalization (e.g., if trained on shovel's "scooping" affordance, can the model activate the same interaction for novel shovel-like tools?)
- Free-form instruction tests: Non-templated natural language instruction understanding

Building Blocks: OpenVLA codebase (VLA base architecture); CoA-VLA codebase (affordance VLA baseline); OVAL-Prompt codebase (open-vocabulary affordance detection reference); AGD20K/UMD Affordance datasets (affordance annotations); LIBERO benchmark (manipulation task evaluation); DINOv2/SigLIP visual encoders; SAM2 (segmentation); HuggingFace transformers + accelerate; CLIP/SigLIP (open-vocabulary semantic alignment).

Hard Constraints:
Compute: ≤200 H100-hours. Strategy: Fine-tune based on 7B VLA, affordance module leveraging pre-trained VLM features (e.g., CLIP/SigLIP) to reduce training requirements. Training ~80 H100-hours, baseline reproduction ~50 H100-hours, ablation ~40 H100-hours, generalization testing ~30 H100-hours.
Evaluation: Must validate zero-shot generalization on unseen object categories. Must include free-form language instruction tests. Must include ≥4 baselines. Must report both affordance precision and manipulation success rate. Must include ablation studies and cross-object transfer tests.

Exploration Directions: (1) End-to-end activation of VLM internal affordance features: Rather than adding an external affordance detection module to VLA, activate interaction-relevant visual features within VLA's VLM backbone network directly through language instructions. Key insight: Large-scale VLMs (e.g., PaliGemma, SigLIP) have already learned extensive shape-function associations during pre-training ("knives can cut," "bowls can hold"), only requiring suitable activation mechanisms to release this implicit knowledge. (2) Affordance as intermediate reasoning tokens: Rather than explicitly outputting affordance heatmaps, have VLA generate a set of "affordance reasoning tokens" before generating action token sequences (similar to CoA-VLA's chain reasoning but open-vocabulary). These tokens encode interaction possibilities of objects in the current scene, then condition subsequent action generation. Differs from CoA-VLA: not limited to 4 predefined types; reasoning content is dynamically determined by language instructions. (3) Contrastive learning for universal shape-function-interaction mapping: Add contrastive objective during VLA training to pull together different-shaped objects with similar functions (various "tools that can scoop things") in affordance feature space, and push apart similar-shaped objects with different functions (decorative bowl vs. functional bowl). More flexible than CoA-VLA's structured types — any natural language-described interaction can participate in contrasting. (4) Knowledge distillation for zero-shot affordance reasoning: Use large VLMs' (e.g., GPT-4V level) zero-shot affordance reasoning capability ("how can this object be interacted with?") as teacher signals, distilling into small VLA. Large models have rich commonsense knowledge and can generate affordance descriptions for virtually any object, but are too large to deploy directly on robots. (5) Affordance consistency self-supervision: The same object under different language descriptions should have consistent affordance responses ("grab the handle" vs. "pick it up by the stick part" describe the same interaction). Use this consistency as self-supervision signals, reducing dependency on fine-grained affordance annotations.

Avoid:
- Using predefined fixed affordance types — duplicates CoA-VLA
- Modular pipeline (affordance detection → planning → control) — duplicates GeneralVLA/VoxPoser, and prevents end-to-end optimization
- Only doing affordance detection without actions — duplicates OVAL-Prompt
- Ignoring CoA-VLA baseline — it is the most recent affordance + VLA work; must directly compare
- Ignoring GeneralVLA — it is the most recent zero-shot affordance manipulation work; must clarify advantages of end-to-end vs. modular
- Reporting results only on within-training-distribution objects — the core value of open vocabulary is on out-of-distribution objects
- Over-relying on affordance annotation data — should design methods to reduce annotation requirements

Idea Generation Quality Constraints (Hard rules based on historical cases):

1. No strawman problems: Any claim of "existing methods assume X" or "existing methods fail on Y" must cite specific paragraphs from specific papers as evidence.

2. No pure observation ideas: Output must include a complete method, not merely analysis/benchmark/empirical study.

3. No mediocre methods: Methods must answer:
   - Core insight: Large-scale VLMs have already implicitly learned rich shape-function association knowledge during pre-training; CoA-VLA released part of it through structured reasoning chains, but is limited by predefined types. We directly activate corresponding affordance features within VLA through open-vocabulary language instructions, fully releasing VLM's implicit shape-function knowledge into action generation.
   - Why non-obvious: (1) CoA-VLA (December 2024) is the first work integrating affordance chain reasoning into VLA; affordance + VLA itself is a new paradigm; (2) open-vocabulary requires solving the infinite-dimensional affordance space problem — unlike 4 fixed types that can be directly classified; (3) end-to-end training of open-vocabulary affordance requires affordance annotation data, but such data is scarce — needs training strategies that reduce annotation dependency.
   - What information is exploited: Implicit shape-function association knowledge from VLM pre-training — which neither 2D visual VLAs nor fixed-type affordance methods fully utilize.
   - Mechanistic argument: When given a free-form language instruction (e.g., "scoop the rice"), the VLM internally already encodes knowledge that "scooping requires a concave container-shaped tool." Through suitable activation mechanisms, this knowledge can be transformed into affordance attention in visual feature space — focusing on regions in the scene with corresponding geometric functional properties, then conditioning action generation. More flexible than CoA-VLA's fixed 4-type reasoning because affordance is dynamically defined by language.

4. No duplicating existing work: Each core technical component must be confirmed with at least 3 different search queries to have no directly related work.

5. No padding experiments:
   - "Delete experiment test": Keep only the method description — does it teach the reader something non-trivial? Yes — VLM implicit shape-function knowledge can drive VLA action generation through open-vocabulary activation.
   - "Baseline fear test": If CoA-VLA's 4 structured types already cover most scenarios, is the paper still valuable? Must prove open-vocabulary methods' advantages on free-form instructions and novel interactions.
   - "Citation test": Will people cite the numbers or the insight 5 years later? The insight — open-vocabulary affordance in end-to-end VLA paradigm.

6. The following method patterns are rejected (unless with extremely strong structural reasons):
   - "Add module X" — Why this specific structure?
   - "Train on data Y" — Is data construction itself a contribution?
   - "Transfer Z from domain A to domain B" — What is the structural analogy?
   - "Combine P and Q" — Where is the synergy? Combining open-vocabulary detection (OVAL-Prompt) with VLA — must prove end-to-end joint training outperforms simple concatenation.
   - "Use more/larger/stronger X" — Scale is not a method contribution.

Competition Warning: CoA-VLA (December 2024) is the most recent affordance + VLA — uses structured reasoning chains but not open-vocabulary. GeneralVLA (February 2026) does zero-shot affordance manipulation but is a modular pipeline. OVAL-Prompt (ICRA 2024 Workshop) does open-vocabulary affordance detection but no actions. AffordDP (CVPR 2025) does affordance cross-category transfer but no language. VoxPoser (CoRL 2023) uses LLM to generate 3D affordance maps but is modular. π0 (Physical Intelligence) and RT-2 and other large VLAs may implicitly contain partial affordance knowledge but do not explicitly leverage it. Differentiation core: The only work integrating open-vocabulary affordance reasoning end-to-end into a unified VLA architecture. Highest risk: CoA-VLA is closest in space; if its author team quickly extends to open-vocabulary, differentiation shrinks. Monitor: CoA-VLA author team, GeneralVLA author team, Physical Intelligence (whether π0 follow-ups will integrate affordance).

Tags: direction=open_vocab_affordance_zero_shot_vla, contribution_type=method, sub_direction=unified_affordance_vla_end_to_end, target_venues=["CoRL 2026"].**
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
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-18?
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

## Idea under review (round 10/10)
{
  "title": "Open-Vocabulary Affordance Chain-of-Reasoning for End-to-End VLA",
  "core_problem": "Current affordance-integrated VLAs (CoA-VLA, PALM) use 3-4 predefined structured affordance types, making them unable to handle free-form interaction descriptions (e.g., 'use this to wipe off the dust') or reason about novel object-interaction pairings unseen during training.",
  "opportunity": "CoT-VLA (CVPR 2025) proved that generating intermediate reasoning tokens before actions improves VLA by 17% in real-world tasks, while 3D-AffordanceLLM (ICLR 2025) demonstrated LLMs can perform open-vocabulary affordance detection with ~8% mIoU improvement. The natural synthesis — open-vocabulary affordance as the reasoning content in a CoT-VLA framework — remains unexplored. This is feasible now because both components (reasoning VLA and open-vocab affordance) are independently validated.",
  "landscape": "CoA-VLA (ICCV 2025) integrates 4 structured affordance types (object, grasp, spatial, movement) into VLA chain reasoning, surpassing OpenVLA. PALM (arXiv 2026) similarly uses 4 structured affordance representations (object relevance, contact geometry, spatial placements, motion dynamics) for long-horizon tasks, achieving 91.8% on LIBERO-LONG. CoT-VLA (CVPR 2025) generates future visual goal frames as intermediate reasoning tokens, improving real-world success by 17%. DualCoT-VLA (arXiv 2026) introduces parallel visual-linguistic CoT with learnable query tokens. VLA-R1 (arXiv 2025) applies RLVR to enhance step-by-step reasoning in VLAs, improving affordance perception by 17.78%. LaST₀ (arXiv 2026) uses latent spatio-temporal CoT with a dual-expert Mixture-of-Transformers architecture. AffordGrasp (IROS 2025) performs open-vocabulary task-oriented grasping via VLM in-context affordance reasoning but is not end-to-end trainable. Affogato (arXiv 2025) provides 150K open-vocabulary 3D affordance annotations but targets grounding, not action generation. None support open-vocabulary affordance reasoning within an end-to-end VLA — all use fixed/structured types or non-affordance-specific reasoning, leaving a clear gap for dynamic, language-driven affordance reasoning before action generation.",
  "approach": "We propose OVA-VLA, which replaces fixed affordance taxonomies with free-form, LLM-generated affordance chain-of-reasoning within an end-to-end VLA. Using Qwen3-VL-2B as backbone via the VLA Foundry framework, the model autoregressively generates open-vocabulary affordance rationales (e.g., 'the mug handle affords a lateral pinch grasp; rotate wrist 90° to pour into the bowl') before predicting action tokens, enabling generalization to novel interaction descriptions and unseen object-affordance pairings. Training data is created by augmenting LIBERO and RoboCasa365 demonstrations with diverse free-form affordance annotations generated at scale by Qwen3-VL-235B-Instruct, avoiding the manual effort of designing fixed affordance schemas. We evaluate on LIBERO-LONG, RoboCasa365, and a new open-vocabulary generalization split with paraphrased/novel interaction descriptions, with key ablations comparing open-vocabulary vs. fixed-type affordance reasoning and measuring the impact of annotation diversity on out-of-distribution generalization.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~500-800h A100 (10-15 training runs × ~50-80h each, including debugging and restarts)",
      "gpu_utilization": "60-80% GPU idle — GPUs sit unused during human code writing, debugging, result analysis, and sleep cycles; each experiment-debug loop has multi-hour human latency",
      "timeline": "3-5 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$750-1200 (at ~$1.50/h A100 80GB on specialized cloud providers)"
    },
    "human_in_loop": {
      "gpu_hours": "~600-1000h A100 (agent runs more experiments but human approval gates reduce wasted runs)",
      "gpu_utilization": "30-50% idle — significant improvement over manual; agent queues next experiment during current run, but still waits for human approval on design decisions and result interpretation",
      "timeline": "6-10 weeks",
      "team": "1 researcher, ~1hr/day review and approval of experiment plans and results",
      "claude_api_cost": "$200-500 (2000-5000 turns for code generation, experiment design, result analysis)",
      "estimated_gpu_cost": "$900-1500",
      "risk_note": "Affordance annotation quality — auto-generated free-form annotations from Qwen3-VL-235B may contain hallucinated spatial relationships; human spot-checking of annotation quality is critical before full-scale training"
    },
    "auto_research": {
      "gpu_hours": "~1500-2500h A100 (3-5× more experiment exploration including hyperparameter sweeps, annotation diversity ablations, and failed architecture variants; near-zero idle)",
      "gpu_utilization": "GPU idle <5% — agent continuously pipelines data annotation, training, and evaluation; next experiment is queued before current one finishes; overnight/weekend runs proceed without pause",
      "timeline": "1-3 weeks with 8× A100 cluster available continuously",
      "team": "0 (initial setup only: define benchmark suite, configure VLA Foundry, set evaluation metrics)",
      "claude_api_cost": "$500-1000 (5000-10000 turns for full autonomous experiment loop)",
      "estimated_gpu_cost": "$2250-3750",
      "speed_bottleneck": "GPU count is primary bottleneck — with 8× A100 the agent can parallelize training runs and annotation generation; secondary bottleneck is Qwen3-VL-235B inference throughput for generating 200K+ affordance annotations across LIBERO+RoboCasa365 datasets",
      "risk_note": "Without human oversight, the agent may over-optimize for benchmark metrics while producing affordance reasoning that is syntactically diverse but semantically degenerate (e.g., generic descriptions that don't capture true physical affordances); recommend automated diversity metrics and periodic human audit checkpoints"
    }
  },
  "target_venues": [
    "ICLR 2027 (abstract Sep 19, paper Sep 24, 2026) — top-tier ML venue, best fit for method contribution",
    "AAAI 2027 (abstract Jul 21, paper Jul 28, 2026) — top-tier AI venue, earlier deadline",
    "CoRL 2026 (abstract May 26, paper May 29, 2026) — top-tier robotics venue, tight but feasible with auto-research",
    "CVPR 2027 (abstract Nov 7, paper Nov 13, 2026) — top-tier vision venue, fallback if earlier submissions need revision"
  ],
  "level": "top-tier",
  "key_references": [
    "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance (ICCV 2025)",
    "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (CVPR 2025)",
    "3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds (ICLR 2025)",
    "PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation (arXiv 2026)",
    "DualCoT-VLA: Visual-Linguistic Chain of Thought via Parallel Reasoning for Vision-Language-Action Models (arXiv 2026)",
    "VLA-R1: Enhancing Reasoning in Vision-Language-Action Models (arXiv 2025)",
    "AffordGrasp: In-Context Affordance Reasoning for Open-Vocabulary Task-Oriented Grasping in Clutter (IROS 2025)",
    "VLA Foundry: A Unified Framework for Training Vision-Language-Action Models (arXiv 2026)",
    "LaST₀: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model (arXiv 2026)"
  ],
  "description": "We propose OVA-VLA, the first VLA framework that uses open-vocabulary affordance reasoning as intermediate chain-of-thought tokens for end-to-end robotic manipulation. While CoA-VLA (ICCV 2025) and PALM demonstrate that structured affordance reasoning with 3-4 fixed types improves VLA performance, and 3D-AffordanceLLM (ICLR 2025) shows LLMs can perform open-vocabulary affordance detection, no existing method combines these insights. OVA-VLA bridges this gap by building on Qwen3-VL-2B via VLA Foundry, autoregressively generating free-form affordance rationales before predicting action tokens. Training annotations are produced at scale by Qwen3-VL-235B-Instruct, eliminating manual affordance schema design. We evaluate on LIBERO-LONG, RoboCasa365, and a novel open-vocabulary generalization split with paraphrased and unseen interaction descriptions. Key ablations compare open-vocabulary vs. fixed-type affordance reasoning and measure annotation diversity's impact on generalization. No concurrent work addresses this specific gap — existing CoT-VLA variants (DualCoT-VLA, LaST₀) use non-affordance reasoning, while open-vocab affordance methods (AffordGrasp, Affogato) lack end-to-end action generation. This timely synthesis targets ICLR 2027 as a top-tier contribution.",
  "project_name": "ov_afford_cot_vla",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: error
Issues: []
Feedback: Review subprocess failed (timeout or parse error)

### Round 2 review
Verdict: error
Issues: []
Feedback: Review subprocess failed (timeout or parse error)

### Round 3 review
Verdict: error
Issues: []
Feedback: Review subprocess failed (timeout or parse error)

### Round 4 review
Verdict: error
Issues: []
Feedback: Review subprocess failed (timeout or parse error)

### Round 5 review
Verdict: error
Issues: []
Feedback: Review subprocess failed (timeout or parse error)

### Round 6 review
Verdict: error
Issues: []
Feedback: Review subprocess failed (timeout or parse error)

### Round 7 review
Verdict: error
Issues: []
Feedback: Review subprocess failed (timeout or parse error)

### Round 8 review
Verdict: error
Issues: []
Feedback: Review subprocess failed (timeout or parse error)

### Round 9 review
Verdict: error
Issues: []
Feedback: Review subprocess failed (timeout or parse error)


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
  "promptId": "9c1065e4-9cac-491e-8608-81f97bff1235",
  "type": "user",
  "uuid": "da727f26-0dc2-432c-9b77-41883743dd6f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73519ec3-ea57-4f39-9bd9-306b1dc4b1d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T17:28:56.641Z_

```json
{
  "parentUuid": "da727f26-0dc2-432c-9b77-41883743dd6f",
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
  "uuid": "20b5652a-38c1-4e47-92ae-8bcb74dc7e92",
  "timestamp": "2026-05-18T17:28:56.641Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73519ec3-ea57-4f39-9bd9-306b1dc4b1d4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T17:28:56.641Z_

```json
{
  "parentUuid": "20b5652a-38c1-4e47-92ae-8bcb74dc7e92",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9728aaa3-4158-459e-a243-f6c914597839",
  "timestamp": "2026-05-18T17:28:56.641Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73519ec3-ea57-4f39-9bd9-306b1dc4b1d4",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "9728aaa3-4158-459e-a243-f6c914597839",
  "sessionId": "73519ec3-ea57-4f39-9bd9-306b1dc4b1d4"
}
```

---

### Assistant

_source line 7 · 2026-05-18T17:28:59.308Z_

Failed to authenticate. API Error: 401 {"type":"error","error":{"type":"authentication_error","message":"Invalid authentication credentials"},"request_id":"req_011CbARs2E8VfsXE2DHzPigb"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9728aaa3-4158-459e-a243-f6c914597839",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "e91e1c35-2955-424d-91cc-144baf5f354b",
  "error": "authentication_failed",
  "isApiErrorMessage": true,
  "apiErrorStatus": 401,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "73519ec3-ea57-4f39-9bd9-306b1dc4b1d4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "26b3c50b-581f-481d-8219-2d3e7c735964",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---

### Runtime record

_source line 8_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e91e1c35-2955-424d-91cc-144baf5f354b",
  "sessionId": "73519ec3-ea57-4f39-9bd9-306b1dc4b1d4"
}
```

---
