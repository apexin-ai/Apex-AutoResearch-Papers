# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-18 (UTC).** Your job: indep

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 144
- **Recorded user turns:** 1
- **Tool calls:** 43
- **Original source:** `logs/chats/exported-trajectories/account-3/bab35da4-a4d1-43b7-8915-527f62f88ec1.jsonl`
- **Structured JSON:** [`3ca48ae87d221ef45766.json`](../../sessions/3c/3ca48ae87d221ef45766.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T19:12:09.839Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T19:12:09.839Z",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-18 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **## Seed 4: Open-Vocabulary Affordance Zero-Shot VLA\n\nObjective: CoRL 2026 submission.\n\nDirection: Traditional affordance methods and VLAs rely on fixed category annotations and struggle with open-world unknown objects and free-form interaction instructions. CoA-VLA (arXiv 2412.20451, December 2024) integrates affordance chain-of-reasoning into VLA, but uses 4 predefined structured affordance types (object, grasp, spatial, motion) — not truly open-vocabulary — and cannot handle free-form interaction descriptions like \"use this thing to wipe off the dust over there.\" GeneralVLA (arXiv 2602.04315, February 2026) achieves zero-shot affordance perception and manipulation trajectory generation through VLM+SAM, but is a modular three-stage pipeline (affordance perception → trajectory planning → low-level control), not a unified end-to-end VLA — with information loss between modules and inability to jointly optimize. OVAL-Prompt (ICRA 2024 VLMNM Workshop, arXiv 2404.11000) achieves truly open-vocabulary affordance localization, but only performs detection/localization without generating actions. AffordDP (CVPR 2025, arXiv 2412.03142) achieves affordance cross-category transfer through 3D contact points and trajectories, but completely lacks language conditioning. Core gap: No work unifies open-vocabulary affordance reasoning into an end-to-end VLA for zero-shot manipulation — existing work either has fixed affordance types (CoA-VLA), or is a modular pipeline (GeneralVLA), or only does detection without actions (OVAL-Prompt), or lacks language (AffordDP).\n\nSeed Papers:\n- \"OpenVLA: An Open-Source Vision-Language-Action Model\" (Kim et al., CoRL 2024, arXiv 2406.09246)\n  — 7B parameter open-source VLA, trained on 970K real robot demonstrations, establishing the VLA open-source paradigm. The base architecture for this work — integrating open-vocabulary affordance reasoning on top.\n- \"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance\" (Li et al., arXiv 2412.20451, December 2024)\n  — Integrates affordance chain-of-reasoning into VLA: model sequentially reasons about object affordance, grasp affordance, spatial affordance, and motion affordance before predicting actions. Uses visual-language collaborative injection module. Surpasses OpenVLA and Octo. Key limitation: 4 affordance types are predefined/structured, not open-vocabulary — cannot handle arbitrary natural language descriptions of novel interactions.\n- \"GeneralVLA: Generalizable Vision-Language-Action Models with Knowledge-Guided Trajectory Planning\" (Ma et al., arXiv 2602.04315, February 2026)\n  — Hierarchical three-module pipeline: (1) VLM+SAM affordance perception for keypoint detection, (2) mid-level planning agent for trajectory generation, (3) low-level control policy. Achieves zero-shot manipulation across 14 tasks without real-world data. Key limitation: Modular pipeline, not end-to-end — affordance module, trajectory planner, and controller are separated, with information bottlenecks between modules.\n- \"OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot Manipulation through LLM Affordance-Grounding\" (Tong et al., ICRA 2024 VLMNM Workshop, arXiv 2404.11000)\n  — Prompt-based method combining VLM for object part segmentation and LLM for part-affordance grounding mapping, achieving open-vocabulary affordance localization without prior training. Competitive with supervised methods on localization benchmarks. Key limitation: Only performs affordance detection/localization, does not generate robot actions — a perception module, not a complete manipulation system.\n- \"AffordDP: Generalizable Diffusion Policy with Transferable Affordance\" (Wu et al., CVPR 2025, arXiv 2412.03142)\n  — Models manipulation priors through 3D contact points and post-contact trajectories, achieving affordance cross-category transfer using visual models + point cloud registration. Affordance-guided diffusion policy generates actions. Key limitation: No language conditioning — affordances are geometric/contact-based, not language-driven, cannot handle open-vocabulary instructions.\n\nKnown Gap:\n- CoA-VLA integrates affordance into VLA but uses predefined structured types, does not support open vocabulary\n- GeneralVLA does zero-shot affordance manipulation but is a modular pipeline, not end-to-end\n- OVAL-Prompt does open-vocabulary affordance but only detection, no action generation\n- AffordDP does affordance cross-category transfer but no language conditioning\n- VoxPoser (CoRL 2023, arXiv 2307.05973) uses LLM to generate 3D affordance/constraint maps but is modular, no end-to-end learning\n- No work unifies open-vocabulary affordance reasoning into end-to-end VLA\n\nIn Scope: Methods unifying open-vocabulary affordance reasoning into end-to-end VLA architecture. Specifically includes: text prompt-driven open-vocabulary affordance feature activation mechanism, universal shape-function-interaction attribute association learning, end-to-end joint training of affordance reasoning and action generation, zero-shot generalization to unseen object categories and novel language interaction instructions. The core contribution should be a unified architecture, not a modular concatenation of affordance detection + action generation.\n\nOut of Scope: Predefined fixed affordance types (CoA-VLA already done). Modular affordance pipelines (GeneralVLA/VoxPoser already done). Affordance detection only without actions (OVAL-Prompt already done). Affordance transfer without language conditioning (AffordDP already done). Pure affordance benchmarking/analysis.\n\nContribution Type: Method contribution. Output must include (1) unified architecture design for open-vocabulary affordance and VLA, (2) end-to-end training strategy for affordance reasoning and action generation, (3) experimental validation of zero-shot generalization on unseen objects and novel interaction instructions, demonstrating advantages over structured affordance VLA and modular methods.\n\nEvaluation Protocol:\nTraining: Based on OpenVLA architecture, integrating open-vocabulary affordance module. Training data uses LIBERO + affordance annotation data (e.g., AGD20K/UMD Affordance).\nEvaluation Metrics:\n- Primary metric: Zero-shot manipulation success rate on unseen object categories\n- Novel interaction instruction generalization: Language interaction descriptions unseen during training (e.g., train on \"pick up,\" test on \"scoop out\")\n- Affordance localization precision: Compare with detection methods like OVAL-Prompt (ensure affordance understanding itself does not degrade)\n- Manipulation success rate: Compare with standard VLA baselines (ensure adding affordance does not degrade known task performance)\n- Baseline comparisons:\n  1. Affordance-free VLA (OpenVLA direct fine-tuning)\n  2. Structured affordance VLA (CoA-VLA reproduction)\n  3. Modular affordance pipeline (GeneralVLA approach)\n  4. Affordance detection + independent policy (OVAL-Prompt + policy learning)\n  5. LLM affordance map + planning (VoxPoser approach)\n- Ablation studies: Open-vocabulary affordance vs. fixed-type affordance, end-to-end vs. staged training, text-driven affordance vs. vision-driven affordance\n- Cross-object transfer tests: Shape-function association generalization (e.g., if trained on shovel's \"scooping\" affordance, can the model activate the same interaction for novel shovel-like tools?)\n- Free-form instruction tests: Non-templated natural language instruction understanding\n\nBuilding Blocks: OpenVLA codebase (VLA base architecture); CoA-VLA codebase (affordance VLA baseline); OVAL-Prompt codebase (open-vocabulary affordance detection reference); AGD20K/UMD Affordance datasets (affordance annotations); LIBERO benchmark (manipulation task evaluation); DINOv2/SigLIP visual encoders; SAM2 (segmentation); HuggingFace transformers + accelerate; CLIP/SigLIP (open-vocabulary semantic alignment).\n\nHard Constraints:\nCompute: ≤200 H100-hours. Strategy: Fine-tune based on 7B VLA, affordance module leveraging pre-trained VLM features (e.g., CLIP/SigLIP) to reduce training requirements. Training ~80 H100-hours, baseline reproduction ~50 H100-hours, ablation ~40 H100-hours, generalization testing ~30 H100-hours.\nEvaluation: Must validate zero-shot generalization on unseen object categories. Must include free-form language instruction tests. Must include ≥4 baselines. Must report both affordance precision and manipulation success rate. Must include ablation studies and cross-object transfer tests.\n\nExploration Directions: (1) End-to-end activation of VLM internal affordance features: Rather than adding an external affordance detection module to VLA, activate interaction-relevant visual features within VLA's VLM backbone network directly through language instructions. Key insight: Large-scale VLMs (e.g., PaliGemma, SigLIP) have already learned extensive shape-function associations during pre-training (\"knives can cut,\" \"bowls can hold\"), only requiring suitable activation mechanisms to release this implicit knowledge. (2) Affordance as intermediate reasoning tokens: Rather than explicitly outputting affordance heatmaps, have VLA generate a set of \"affordance reasoning tokens\" before generating action token sequences (similar to CoA-VLA's chain reasoning but open-vocabulary). These tokens encode interaction possibilities of objects in the current scene, then condition subsequent action generation. Differs from CoA-VLA: not limited to 4 predefined types; reasoning content is dynamically determined by language instructions. (3) Contrastive learning for universal shape-function-interaction mapping: Add contrastive objective during VLA training to pull together different-shaped objects with similar functions (various \"tools that can scoop things\") in affordance feature space, and push apart similar-shaped objects with different functions (decorative bowl vs. functional bowl). More flexible than CoA-VLA's structured types — any natural language-described interaction can participate in contrasting. (4) Knowledge distillation for zero-shot affordance reasoning: Use large VLMs' (e.g., GPT-4V level) zero-shot affordance reasoning capability (\"how can this object be interacted with?\") as teacher signals, distilling into small VLA. Large models have rich commonsense knowledge and can generate affordance descriptions for virtually any object, but are too large to deploy directly on robots. (5) Affordance consistency self-supervision: The same object under different language descriptions should have consistent affordance responses (\"grab the handle\" vs. \"pick it up by the stick part\" describe the same interaction). Use this consistency as self-supervision signals, reducing dependency on fine-grained affordance annotations.\n\nAvoid:\n- Using predefined fixed affordance types — duplicates CoA-VLA\n- Modular pipeline (affordance detection → planning → control) — duplicates GeneralVLA/VoxPoser, and prevents end-to-end optimization\n- Only doing affordance detection without actions — duplicates OVAL-Prompt\n- Ignoring CoA-VLA baseline — it is the most recent affordance + VLA work; must directly compare\n- Ignoring GeneralVLA — it is the most recent zero-shot affordance manipulation work; must clarify advantages of end-to-end vs. modular\n- Reporting results only on within-training-distribution objects — the core value of open vocabulary is on out-of-distribution objects\n- Over-relying on affordance annotation data — should design methods to reduce annotation requirements\n\nIdea Generation Quality Constraints (Hard rules based on historical cases):\n\n1. No strawman problems: Any claim of \"existing methods assume X\" or \"existing methods fail on Y\" must cite specific paragraphs from specific papers as evidence.\n\n2. No pure observation ideas: Output must include a complete method, not merely analysis/benchmark/empirical study.\n\n3. No mediocre methods: Methods must answer:\n   - Core insight: Large-scale VLMs have already implicitly learned rich shape-function association knowledge during pre-training; CoA-VLA released part of it through structured reasoning chains, but is limited by predefined types. We directly activate corresponding affordance features within VLA through open-vocabulary language instructions, fully releasing VLM's implicit shape-function knowledge into action generation.\n   - Why non-obvious: (1) CoA-VLA (December 2024) is the first work integrating affordance chain reasoning into VLA; affordance + VLA itself is a new paradigm; (2) open-vocabulary requires solving the infinite-dimensional affordance space problem — unlike 4 fixed types that can be directly classified; (3) end-to-end training of open-vocabulary affordance requires affordance annotation data, but such data is scarce — needs training strategies that reduce annotation dependency.\n   - What information is exploited: Implicit shape-function association knowledge from VLM pre-training — which neither 2D visual VLAs nor fixed-type affordance methods fully utilize.\n   - Mechanistic argument: When given a free-form language instruction (e.g., \"scoop the rice\"), the VLM internally already encodes knowledge that \"scooping requires a concave container-shaped tool.\" Through suitable activation mechanisms, this knowledge can be transformed into affordance attention in visual feature space — focusing on regions in the scene with corresponding geometric functional properties, then conditioning action generation. More flexible than CoA-VLA's fixed 4-type reasoning because affordance is dynamically defined by language.\n\n4. No duplicating existing work: Each core technical component must be confirmed with at least 3 different search queries to have no directly related work.\n\n5. No padding experiments:\n   - \"Delete experiment test\": Keep only the method description — does it teach the reader something non-trivial? Yes — VLM implicit shape-function knowledge can drive VLA action generation through open-vocabulary activation.\n   - \"Baseline fear test\": If CoA-VLA's 4 structured types already cover most scenarios, is the paper still valuable? Must prove open-vocabulary methods' advantages on free-form instructions and novel interactions.\n   - \"Citation test\": Will people cite the numbers or the insight 5 years later? The insight — open-vocabulary affordance in end-to-end VLA paradigm.\n\n6. The following method patterns are rejected (unless with extremely strong structural reasons):\n   - \"Add module X\" — Why this specific structure?\n   - \"Train on data Y\" — Is data construction itself a contribution?\n   - \"Transfer Z from domain A to domain B\" — What is the structural analogy?\n   - \"Combine P and Q\" — Where is the synergy? Combining open-vocabulary detection (OVAL-Prompt) with VLA — must prove end-to-end joint training outperforms simple concatenation.\n   - \"Use more/larger/stronger X\" — Scale is not a method contribution.\n\nCompetition Warning: CoA-VLA (December 2024) is the most recent affordance + VLA — uses structured reasoning chains but not open-vocabulary. GeneralVLA (February 2026) does zero-shot affordance manipulation but is a modular pipeline. OVAL-Prompt (ICRA 2024 Workshop) does open-vocabulary affordance detection but no actions. AffordDP (CVPR 2025) does affordance cross-category transfer but no language. VoxPoser (CoRL 2023) uses LLM to generate 3D affordance maps but is modular. π0 (Physical Intelligence) and RT-2 and other large VLAs may implicitly contain partial affordance knowledge but do not explicitly leverage it. Differentiation core: The only work integrating open-vocabulary affordance reasoning end-to-end into a unified VLA architecture. Highest risk: CoA-VLA is closest in space; if its author team quickly extends to open-vocabulary, differentiation shrinks. Monitor: CoA-VLA author team, GeneralVLA author team, Physical Intelligence (whether π0 follow-ups will integrate affordance).\n\nTags: direction=open_vocab_affordance_zero_shot_vla, contribution_type=method, sub_direction=unified_affordance_vla_end_to_end, target_venues=[\"CoRL 2026\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-18?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 2/10)\n{\n  \"title\": \"AffordVLA: Distilling Open-Vocabulary Affordance into VLA Representations for Robust Manipulation\",\n  \"core_problem\": \"How can we distill open-vocabulary affordance knowledge from frozen foundation models into a VLA's intermediate representations as an explicit training signal, producing affordance-grounded features that are demonstrably more robust under distribution shift than both generic task-relevant attention mechanisms and modular affordance pipelines?\",\n  \"opportunity\": \"LIBERO-Plus (CVPR 2026) reveals that VLAs achieving 95–98% on standard LIBERO collapse to 30–60% under modest perturbations (camera shift, lighting, layout changes). Generic attention mechanisms like FocusVLA's Focus Attention and AVA-VLA's Active Visual Attention learn task-relevant but not affordance-grounded features — they overfit to visual statistics that break under distribution shift. Meanwhile, PALM (Jan 2026) achieves 91.8% on LIBERO-LONG with structured affordance supervision, proving affordance helps, but its 4 rigid types (object relevance, contact geometry, spatial placement, motion dynamics) depend on external tools (Grounding DINO, SAM, SpatialVLM, CoTracker) and cannot handle novel interaction verbs or compositional instructions. UAD (ICRA 2025 Best Paper Finalist) demonstrates that high-quality affordance pseudo-labels can be extracted from frozen VLMs unsupervised, but only feeds them to a modular pipeline — nobody has distilled this knowledge INTO VLA intermediate representations. The probing study (arXiv 2602.20501) confirms DINOv2 encodes part-level geometric structures and generative models contain verb-conditioned interaction priors. The context-dependency study (arXiv 2603.04419) shows >90% of affordance is context-dependent, arguing against fixed categories. The pieces exist — unsupervised pseudo-labels (UAD), rich VLM affordance features (probing study), and the robustness gap (LIBERO-Plus) — but no one has assembled them into an end-to-end affordance-distilled VLA.\",\n  \"landscape\": \"**Affordance-integrated VLAs**: PALM (arXiv 2601.07060, Jan 2026) structures VLA policy around 4 predefined affordance types with external tool supervision (Grounding DINO, SAM, SpatialVLM, CoTracker), achieving 94.5% avg on LIBERO and 91.8% on LIBERO-LONG — the strongest affordance-VLA baseline. CoA-VLA (ICCV 2025, arXiv 2412.20451) uses chain-of-affordance reasoning over 4 predefined types but underperforms PALM (55.0% LIBERO-LONG). Both rely on fixed affordance categories that cannot handle novel verbs or compositional instructions. **Attention-based VLAs without affordance supervision**: FocusVLA (arXiv 2603.28740, Mar 2026) proposes Modality Cascaded Attention and Focus Attention (top-K visual token selection via cross-attention gating on Qwen2.5-0.5B + DINOv2 + SigLIP), achieving 98.7% multi-weight on standard LIBERO — but with zero affordance-specific signal, purely task-relevant attention trained with action loss only. AVA-VLA (arXiv 2511.18960, Nov 2025) uses history-conditioned active visual attention via recurrent state; SOTA on LIBERO and CALVIN. DeepVision-VLA (arXiv 2603.15618) injects multi-level vision foundation features via mixture-of-transformers. VLA-Adapter (arXiv 2509.09372) shows mid-layer VLM features outperform final-layer for action generation. All of these are mechanistically similar to our earlier LA³ concept — language-conditioned attention on visual features — but lack any affordance-specific training signal. **Modular affordance pipelines**: UAD (arXiv 2506.09284, ICRA 2025 Best Paper Finalist) distills affordance pseudo-labels from frozen VLMs (large vision models + VLMs) without annotations, training a lightweight decoder on frozen features — generalizes with 10 demos but remains a modular perception-to-policy pipeline. RT-Affordance (arXiv 2411.02704) uses affordance as hierarchical intermediate representation — modular two-stage. AffordGrasp (arXiv 2503.00778, Mar 2025) leverages VLM reasoning for open-vocabulary affordance grasping in clutter — training-free but modular and grasping-only. GLOVER++ (CoRL 2025, arXiv 2505.11865) scales open-vocab affordance to 500K images, 93% grasping success, but remains a perception pipeline. Affordance Field Intervention (arXiv 2512.07472) uses 3D Spatial Affordance Fields as plug-in inference-time guidance for VLAs under distribution shift (+23.5% improvement on OOD scenarios), proving affordance helps robustness but requiring an external module at inference. **Reasoning and robustness VLAs**: CoT-VLA (CVPR 2025, arXiv 2503.22020) uses visual chain-of-thought via future frame prediction — 7B model, +17% on real-world tasks. ST4VLA (ICLR 2026, arXiv 2602.10109) uses spatial grounding pre-training. Stable Language Guidance (arXiv 2601.04052) identifies modality collapse where visual affordance priors overwhelm language, proposing Residual Semantic Steering to subtract affordance — studying the same affordance-language axis but in the opposite direction (subtracting vs. our activating). VLA-GSE (arXiv 2605.06175) achieves 81.2% on LIBERO-Plus with only 2.51% trainable parameters — the PEFT SOTA for VLA robustness. Contrastive Representation Regularization (RS-CL, arXiv 2510.01711) uses robot-state contrastive loss to align VLM representations — similar auxiliary loss idea but for state alignment, not affordance. A1 (arXiv 2604.05672, Apr 2026) mentions implicit affordance priors from VLMs but focuses on inference efficiency via adaptive layer truncation. **The gap**: No existing work distills open-vocabulary affordance pseudo-labels from frozen foundation models INTO VLA intermediate representations as an end-to-end auxiliary training signal. PALM uses fixed types with external tools; FocusVLA/AVA-VLA lack affordance supervision entirely; UAD/RT-Affordance/AffordGrasp are modular pipelines; AFI requires external inference-time modules.\",\n  \"approach\": \"We propose AffordVLA, which distills open-vocabulary affordance knowledge from frozen foundation models into a VLA's intermediate representations via an auxiliary affordance prediction loss, producing affordance-grounded features that are robust under distribution shift. The approach has three stages: **Stage 1 — Affordance Pseudo-Label Generation (offline, one-time):** For each (image, language instruction) pair in the training data, we generate dense affordance heatmaps using frozen foundation models. Following the probing study's insight (arXiv 2602.20501), we fuse DINOv2's geometric part features (extracted via attention-based part prototypes) with a frozen VLM's (Qwen2-VL-7B) instruction-conditioned interaction priors. Concretely, we prompt the VLM with the image and instruction to generate a textual affordance description (e.g., 'grasp the mug by its handle'), then use a lightweight grounding module (frozen GroundingDINO) to project this into a spatial affordance heatmap. This follows UAD's philosophy of unsupervised affordance extraction but generates spatial pseudo-labels rather than discrete descriptions. No manual affordance annotations are needed. **Stage 2 — Affordance-Distilled Training:** Built on OpenVLA-OFT (SigLIP + DINOv2 dual encoder, pretrained checkpoints), we add a lightweight auxiliary Affordance Prediction Head — a 3-layer MLP with ~2M parameters — that reads instruction-conditioned features from intermediate VLM layers (layers 16–20, where VLA-Adapter confirms action-generation utility peaks) and predicts the affordance heatmap. The total loss is L = L_action + λ·L_afford, where L_afford is a focal loss against the pseudo-labels and λ=0.1 is a weighting hyperparameter. The affordance head is dropped at inference (zero inference cost). The VLM backbone is fine-tuned with LoRA (rank 32, ~5M parameters). Total added parameters: ~7M (~0.1% of the 7B base model). **Stage 3 — Evaluation focused on robustness:** We evaluate on LIBERO-Plus (7 perturbation dimensions: camera, robot, language, light, background, noise, layout) as the primary benchmark, where current VLAs catastrophically fail. Secondary evaluation on standard LIBERO (to verify no regression) and on novel instruction sets with unseen interaction verbs (to test open-vocabulary advantage over PALM's fixed types). Baselines: PALM (structured affordance), FocusVLA (generic attention), AVA-VLA (history-conditioned attention), OpenVLA-OFT (base model), VLA-GSE (PEFT robustness SOTA), and a UAD→policy modular pipeline (to test end-to-end vs. modular). Key ablations: (a) affordance loss vs. no affordance loss (generic attention control), (b) pseudo-label quality (DINOv2-only vs. VLM-only vs. fused), (c) which VLM layers carry the strongest affordance signal (layers 8/12/16/20/24), (d) λ sensitivity, (e) qualitative visualization of learned attention maps under perturbation comparing AffordVLA vs. FocusVLA-style generic attention.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180h H100 (pseudo-label generation: 25h on 1×H100 for LIBERO dataset using frozen models; architecture search over 3 layer-selection variants: 45h; 4 full training runs at ~15h each on 1×H100 with LoRA: 60h; LIBERO-Plus + standard LIBERO evaluation: 30h; ablations on λ and pseudo-label variants: 20h)\",\n      \"gpu_utilization\": \"~40-50% effective utilization due to researcher iteration cycles\",\n      \"timeline\": \"3-4 months (targeting ICRA 2027 or ICLR 2027 deadline ~Sep 2026)\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"$540-720 (H100 80GB at $3.00-4.00/hr on Lambda/RunPod)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~200h H100 (agent explores 2 additional λ schedules and pseudo-label ablations)\",\n      \"gpu_utilization\": \"~65-70%; agent queues next experiment promptly but pauses at approval gates\",\n      \"timeline\": \"6-8 weeks\",\n      \"team\": \"1 researcher, ~20min/day reviewing agent proposals\",\n      \"claude_api_cost\": \"$50-80 (~500-800 turns at ~$0.10/turn Opus)\",\n      \"estimated_gpu_cost\": \"$600-800 (H100 80GB at $3.00-4.00/hr)\",\n      \"risk_note\": \"Agent may over-explore pseudo-label generation strategies; approval gates on architecture decisions mitigate waste\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~400-500h H100 (exhaustive layer search, full λ sweep, cross-backbone validation on SmolVLA, 3 seeds per final config, comprehensive LIBERO-Plus per-dimension analysis)\",\n      \"gpu_utilization\": \"~85-90%; agent queues experiments 24/7\",\n      \"timeline\": \"2-3 weeks with 4×H100\",\n      \"team\": \"0 researchers after ~2h initial setup\",\n      \"claude_api_cost\": \"$150-250 (~1,500-2,500 turns Opus)\",\n      \"estimated_gpu_cost\": \"$1,200-2,000 (H100 at $3.00-4.00/hr)\",\n      \"speed_bottleneck\": \"Pseudo-label generation is sequential per dataset split; parallelizable across task suites\",\n      \"risk_note\": \"Exceeds 200 H100-hour budget but produces a more thorough paper with multi-seed results and cross-backbone validation; manual and human-in-loop modes fit within budget\"\n    }\n  },\n  \"target_venues\": [\n    \"ICRA 2027 (expected deadline Sep 2026; top robotics venue, strong fit for affordance + robustness story — 4 months from now, primary target)\",\n    \"ICLR 2027 (expected deadline Sep-Oct 2026; top ML venue, backup if results are strong enough for broader ML audience)\",\n    \"CoRL 2026 IMPOSSIBLE (deadline May 28, 2026 — 10 days away, not feasible even with pre-existing codebase; acknowledged per reviewer feedback)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation (arXiv 2601.07060, Jan 2026) — strongest affordance-VLA baseline, 91.8% LIBERO-LONG with 4 structured affordance types\",\n    \"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models (arXiv 2603.28740, Mar 2026) — mechanistically closest work, Focus Attention for task-relevant token selection, 98.7% standard LIBERO but no affordance supervision\",\n    \"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation (arXiv 2506.09284, ICRA 2025 Best Paper Finalist) — demonstrates unsupervised affordance pseudo-labels from frozen VLMs, modular pipeline\",\n    \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (arXiv 2510.13626, CVPR 2026) — reveals catastrophic VLA brittleness under perturbation, primary evaluation benchmark\",\n    \"CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance (ICCV 2025, arXiv 2412.20451)\",\n    \"AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (arXiv 2511.18960) — history-conditioned attention, LIBERO+CALVIN SOTA\",\n    \"Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models (arXiv 2602.20501, Feb 2026) — confirms DINOv2 encodes geometric affordance, Flux encodes interaction priors\",\n    \"Context-Dependent Affordance Computation in Vision-Language Models (arXiv 2603.04419, Feb 2026) — >90% affordance is context-dependent, argues against fixed categories\",\n    \"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (CVPR 2025, arXiv 2503.22020)\",\n    \"AffordGrasp: In-Context Affordance Reasoning for Open-Vocabulary Task-Oriented Grasping in Clutter (arXiv 2503.00778, Mar 2025)\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT, arXiv 2502.19645, 2025) — base model, LoRA fine-tuning recipe\",\n    \"VLA-Adapter: An Effective Paradigm for Tiny-Scale VLA Model (arXiv 2509.09372, 2025) — mid-layer features best for action generation\",\n    \"Stable Language Guidance for Vision-Language-Action Models (arXiv 2601.04052, Jan 2026) — studies affordance-language interaction via subtraction\",\n    \"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps (arXiv 2512.07472, Dec 2024) — inference-time affordance guidance, +23.5% OOD\",\n    \"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (arXiv 2411.02704, 2024)\",\n    \"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts (arXiv 2605.06175, 2025) — 81.2% LIBERO-Plus with 2.51% params, PEFT robustness SOTA\",\n    \"Contrastive Representation Regularization for Vision-Language-Action Models (RS-CL, arXiv 2510.01711, 2025) — auxiliary contrastive loss for VLA representation alignment\",\n    \"GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation (CoRL 2025, arXiv 2505.11865)\",\n    \"DeepVision-VLA (arXiv 2603.15618) — multi-level vision feature injection via mixture-of-transformers\",\n    \"A1: A Fully Transparent Open-Source VLA (arXiv 2604.05672, Apr 2026) — adaptive inference with implicit affordance priors\"\n  ],\n  \"description\": \"Current VLAs achieve near-perfect scores on standard manipulation benchmarks but collapse under modest distribution shifts — LIBERO-Plus (CVPR 2026) shows performance drops from 97% to 30-60% under camera, lighting, and layout perturbations. We hypothesize that this brittleness stems from learning generic task-relevant attention (as in FocusVLA, AVA-VLA) that overfits to visual statistics, rather than affordance-grounded features that capture where and how to interact with objects — knowledge that is invariant across visual perturbations. We propose AffordVLA, which distills open-vocabulary affordance pseudo-labels from frozen foundation models (DINOv2 geometric features + VLM interaction priors, following UAD's unsupervised philosophy) into a VLA's intermediate representations via a lightweight auxiliary prediction head. Unlike PALM's 4 rigid affordance types requiring external tools, AffordVLA uses free-form language-conditioned affordance maps with no predefined categories and zero inference overhead (the affordance head is dropped after training). Unlike FocusVLA's generic attention, AffordVLA has an explicit affordance training signal that produces qualitatively different — and more robust — feature representations. Unlike UAD and RT-Affordance's modular pipelines, AffordVLA integrates affordance end-to-end in a single forward pass. Built on OpenVLA-OFT with LoRA (~7M added parameters), the approach fits within 200 H100-hours. Evaluation centers on LIBERO-Plus robustness across 7 perturbation dimensions, with ablations demonstrating that affordance-supervised attention learns different patterns than action-loss-only attention, and that open-vocabulary pseudo-labels outperform PALM's fixed categories on novel instruction verbs.\",\n  \"project_name\": \"afford_vla\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL OMISSION — PALM (arXiv 2601.07060, Jan 2026): Uses 4 predefined affordance types (Global/Local/Spatial/Dynamic) with language conditioning in an end-to-end VLA framework, achieving 91.8% on LIBERO-LONG (vs CoA-VLA's 55.0%). This is the strongest affordance-integrated VLA baseline as of early 2026 and is completely absent from the proposal's landscape and baselines.\", \"CRITICAL OMISSION — UAD (arXiv 2506.09284, ICRA 2025 Best Paper Finalist): Unsupervised affordance distillation from VLMs with open-vocabulary language instructions, demonstrating that affordance knowledge can be extracted from foundation models without manual annotations. Directly relevant as affordance quality baseline and as evidence that modular affordance extraction already works well.\", \"CRITICAL OMISSION — FocusVLA (arXiv 2603.28740, Mar 2026): Proposes 'Modality Cascaded Attention' to direct VLA attention to task-relevant visual regions and 'Focus Attention' for dynamic visual token selection. This is mechanistically near-identical to LA³'s cross-attention-based visual feature amplification, just without the 'affordance' label. The proposal must explicitly differentiate from FocusVLA.\", \"COMPUTE BUDGET VIOLATION: User specified ≤200 H100-hours. The manual estimate alone is 3,500h A100 (~17x over budget). The proposal has silently abandoned the user's hard constraint without justification.\", \"VENUE TARGET MISMATCH: User specified CoRL 2026. The proposal lists ICLR 2027 as primary target, relegating CoRL 2026 to 'feasible only under auto_research.' CoRL 2026 deadline is May 28, 2026 — 10 days from now — making even the auto_research path unrealistic.\", \"SUPERVISION SIGNAL GAP: The proposal claims LA³ requires 'no explicit affordance annotations' and trains end-to-end with action prediction loss only. But without any affordance-specific supervision, what distinguishes the learned cross-attention patterns from generic task-relevant attention? The probing study (arXiv 2602.20501) shows VLMs encode affordance for perception, not that action prediction loss alone can activate this knowledge for manipulation.\", \"NOVELTY INFLATION — 'Affordance' vs. 'Task-Relevant Attention': Multiple 2025-2026 works (FocusVLA, DeepVision-VLA, VLA-Adapter, AVA-VLA) already use language-conditioned attention mechanisms to amplify task-relevant visual features in VLA intermediate layers. The proposal's use of the word 'affordance' does not constitute a technical contribution beyond these existing mechanisms unless there is an affordance-specific training signal or architectural component.\", \"MISSING BASELINE — CoT-VLA (CVPR 2025): Visual chain-of-thought reasoning for VLA, representing the reasoning-augmented VLA paradigm that competes with affordance-based reasoning.\", \"MISSING BASELINE — AffordGrasp (arXiv 2503.00778, Mar 2025): Open-vocabulary affordance reasoning via VLM for grasping, relevant for open-vocabulary affordance quality comparison.\"]\nFeedback: The idea addresses a real gap (open-vocabulary affordance in end-to-end VLA) but has critical issues requiring revision:\n\n1. **Address PALM as primary baseline**: PALM (Jan 2026) is now the strongest affordance-VLA baseline (91.8% LIBERO-LONG). You must include it in your landscape and baselines, and argue specifically where open-vocabulary affordance provides gains over PALM's predefined types. Focus evaluation on scenarios where PALM's 4 types demonstrably fail (novel interaction verbs, compositional instructions, cross-domain objects).\n\n2. **Differentiate from FocusVLA/DeepVision-VLA**: Your cross-attention module is architecturally very similar to FocusVLA's Focus Attention and DeepVision-VLA's multi-level feature injection. Either (a) introduce an affordance-specific training signal (e.g., contrastive loss from the probing study, weak supervision from VLM-generated affordance descriptions à la UAD), or (b) demonstrate empirically that the 'affordance framing' produces qualitatively different attention patterns than generic task-relevant attention.\n\n3. **Resolve the supervision signal problem**: The current proposal has no mechanism for the model to learn 'affordance' attention vs. generic attention. Consider adding: (a) a contrastive auxiliary loss using VLM-generated affordance descriptions as pseudo-labels (leveraging the UAD approach), (b) an affordance consistency regularization (as suggested in your own exploration direction #5), or (c) knowledge distillation from a frozen VLM's affordance probing features (direction #4).\n\n4. **Respect compute constraints or justify deviation**: The user specified ≤200 H100-hours. Either redesign the experiments to fit (e.g., smaller-scale ablations, fewer baselines, leveraging pre-trained checkpoints more aggressively), or explicitly justify why this budget is insufficient and propose a minimal viable experiment plan within budget.\n\n5. **Fix venue targeting**: CoRL 2026 (May 28 deadline) is 10 days away and impossible. Either target CoRL 2026 with a drastically scoped-down version, or honestly acknowledge ICLR 2027 as the realistic target and adjust the timeline accordingly.\n\n6. **Include UAD, AffordGrasp, and CoT-VLA in landscape**: UAD (ICRA 2025 Best Paper) is particularly important as it demonstrates that unsupervised affordance distillation from VLMs already works — your approach must show end-to-end integration outperforms this modular distillation approach.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-18T19:12:09.844Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T19:12:09.844Z",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

## Round 1

142 recorded events

### User

_source line 3 · 2026-05-18T19:12:09.883Z_

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

## Idea under review (round 2/10)
{
  "title": "AffordVLA: Distilling Open-Vocabulary Affordance into VLA Representations for Robust Manipulation",
  "core_problem": "How can we distill open-vocabulary affordance knowledge from frozen foundation models into a VLA's intermediate representations as an explicit training signal, producing affordance-grounded features that are demonstrably more robust under distribution shift than both generic task-relevant attention mechanisms and modular affordance pipelines?",
  "opportunity": "LIBERO-Plus (CVPR 2026) reveals that VLAs achieving 95–98% on standard LIBERO collapse to 30–60% under modest perturbations (camera shift, lighting, layout changes). Generic attention mechanisms like FocusVLA's Focus Attention and AVA-VLA's Active Visual Attention learn task-relevant but not affordance-grounded features — they overfit to visual statistics that break under distribution shift. Meanwhile, PALM (Jan 2026) achieves 91.8% on LIBERO-LONG with structured affordance supervision, proving affordance helps, but its 4 rigid types (object relevance, contact geometry, spatial placement, motion dynamics) depend on external tools (Grounding DINO, SAM, SpatialVLM, CoTracker) and cannot handle novel interaction verbs or compositional instructions. UAD (ICRA 2025 Best Paper Finalist) demonstrates that high-quality affordance pseudo-labels can be extracted from frozen VLMs unsupervised, but only feeds them to a modular pipeline — nobody has distilled this knowledge INTO VLA intermediate representations. The probing study (arXiv 2602.20501) confirms DINOv2 encodes part-level geometric structures and generative models contain verb-conditioned interaction priors. The context-dependency study (arXiv 2603.04419) shows >90% of affordance is context-dependent, arguing against fixed categories. The pieces exist — unsupervised pseudo-labels (UAD), rich VLM affordance features (probing study), and the robustness gap (LIBERO-Plus) — but no one has assembled them into an end-to-end affordance-distilled VLA.",
  "landscape": "**Affordance-integrated VLAs**: PALM (arXiv 2601.07060, Jan 2026) structures VLA policy around 4 predefined affordance types with external tool supervision (Grounding DINO, SAM, SpatialVLM, CoTracker), achieving 94.5% avg on LIBERO and 91.8% on LIBERO-LONG — the strongest affordance-VLA baseline. CoA-VLA (ICCV 2025, arXiv 2412.20451) uses chain-of-affordance reasoning over 4 predefined types but underperforms PALM (55.0% LIBERO-LONG). Both rely on fixed affordance categories that cannot handle novel verbs or compositional instructions. **Attention-based VLAs without affordance supervision**: FocusVLA (arXiv 2603.28740, Mar 2026) proposes Modality Cascaded Attention and Focus Attention (top-K visual token selection via cross-attention gating on Qwen2.5-0.5B + DINOv2 + SigLIP), achieving 98.7% multi-weight on standard LIBERO — but with zero affordance-specific signal, purely task-relevant attention trained with action loss only. AVA-VLA (arXiv 2511.18960, Nov 2025) uses history-conditioned active visual attention via recurrent state; SOTA on LIBERO and CALVIN. DeepVision-VLA (arXiv 2603.15618) injects multi-level vision foundation features via mixture-of-transformers. VLA-Adapter (arXiv 2509.09372) shows mid-layer VLM features outperform final-layer for action generation. All of these are mechanistically similar to our earlier LA³ concept — language-conditioned attention on visual features — but lack any affordance-specific training signal. **Modular affordance pipelines**: UAD (arXiv 2506.09284, ICRA 2025 Best Paper Finalist) distills affordance pseudo-labels from frozen VLMs (large vision models + VLMs) without annotations, training a lightweight decoder on frozen features — generalizes with 10 demos but remains a modular perception-to-policy pipeline. RT-Affordance (arXiv 2411.02704) uses affordance as hierarchical intermediate representation — modular two-stage. AffordGrasp (arXiv 2503.00778, Mar 2025) leverages VLM reasoning for open-vocabulary affordance grasping in clutter — training-free but modular and grasping-only. GLOVER++ (CoRL 2025, arXiv 2505.11865) scales open-vocab affordance to 500K images, 93% grasping success, but remains a perception pipeline. Affordance Field Intervention (arXiv 2512.07472) uses 3D Spatial Affordance Fields as plug-in inference-time guidance for VLAs under distribution shift (+23.5% improvement on OOD scenarios), proving affordance helps robustness but requiring an external module at inference. **Reasoning and robustness VLAs**: CoT-VLA (CVPR 2025, arXiv 2503.22020) uses visual chain-of-thought via future frame prediction — 7B model, +17% on real-world tasks. ST4VLA (ICLR 2026, arXiv 2602.10109) uses spatial grounding pre-training. Stable Language Guidance (arXiv 2601.04052) identifies modality collapse where visual affordance priors overwhelm language, proposing Residual Semantic Steering to subtract affordance — studying the same affordance-language axis but in the opposite direction (subtracting vs. our activating). VLA-GSE (arXiv 2605.06175) achieves 81.2% on LIBERO-Plus with only 2.51% trainable parameters — the PEFT SOTA for VLA robustness. Contrastive Representation Regularization (RS-CL, arXiv 2510.01711) uses robot-state contrastive loss to align VLM representations — similar auxiliary loss idea but for state alignment, not affordance. A1 (arXiv 2604.05672, Apr 2026) mentions implicit affordance priors from VLMs but focuses on inference efficiency via adaptive layer truncation. **The gap**: No existing work distills open-vocabulary affordance pseudo-labels from frozen foundation models INTO VLA intermediate representations as an end-to-end auxiliary training signal. PALM uses fixed types with external tools; FocusVLA/AVA-VLA lack affordance supervision entirely; UAD/RT-Affordance/AffordGrasp are modular pipelines; AFI requires external inference-time modules.",
  "approach": "We propose AffordVLA, which distills open-vocabulary affordance knowledge from frozen foundation models into a VLA's intermediate representations via an auxiliary affordance prediction loss, producing affordance-grounded features that are robust under distribution shift. The approach has three stages: **Stage 1 — Affordance Pseudo-Label Generation (offline, one-time):** For each (image, language instruction) pair in the training data, we generate dense affordance heatmaps using frozen foundation models. Following the probing study's insight (arXiv 2602.20501), we fuse DINOv2's geometric part features (extracted via attention-based part prototypes) with a frozen VLM's (Qwen2-VL-7B) instruction-conditioned interaction priors. Concretely, we prompt the VLM with the image and instruction to generate a textual affordance description (e.g., 'grasp the mug by its handle'), then use a lightweight grounding module (frozen GroundingDINO) to project this into a spatial affordance heatmap. This follows UAD's philosophy of unsupervised affordance extraction but generates spatial pseudo-labels rather than discrete descriptions. No manual affordance annotations are needed. **Stage 2 — Affordance-Distilled Training:** Built on OpenVLA-OFT (SigLIP + DINOv2 dual encoder, pretrained checkpoints), we add a lightweight auxiliary Affordance Prediction Head — a 3-layer MLP with ~2M parameters — that reads instruction-conditioned features from intermediate VLM layers (layers 16–20, where VLA-Adapter confirms action-generation utility peaks) and predicts the affordance heatmap. The total loss is L = L_action + λ·L_afford, where L_afford is a focal loss against the pseudo-labels and λ=0.1 is a weighting hyperparameter. The affordance head is dropped at inference (zero inference cost). The VLM backbone is fine-tuned with LoRA (rank 32, ~5M parameters). Total added parameters: ~7M (~0.1% of the 7B base model). **Stage 3 — Evaluation focused on robustness:** We evaluate on LIBERO-Plus (7 perturbation dimensions: camera, robot, language, light, background, noise, layout) as the primary benchmark, where current VLAs catastrophically fail. Secondary evaluation on standard LIBERO (to verify no regression) and on novel instruction sets with unseen interaction verbs (to test open-vocabulary advantage over PALM's fixed types). Baselines: PALM (structured affordance), FocusVLA (generic attention), AVA-VLA (history-conditioned attention), OpenVLA-OFT (base model), VLA-GSE (PEFT robustness SOTA), and a UAD→policy modular pipeline (to test end-to-end vs. modular). Key ablations: (a) affordance loss vs. no affordance loss (generic attention control), (b) pseudo-label quality (DINOv2-only vs. VLM-only vs. fused), (c) which VLM layers carry the strongest affordance signal (layers 8/12/16/20/24), (d) λ sensitivity, (e) qualitative visualization of learned attention maps under perturbation comparing AffordVLA vs. FocusVLA-style generic attention.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180h H100 (pseudo-label generation: 25h on 1×H100 for LIBERO dataset using frozen models; architecture search over 3 layer-selection variants: 45h; 4 full training runs at ~15h each on 1×H100 with LoRA: 60h; LIBERO-Plus + standard LIBERO evaluation: 30h; ablations on λ and pseudo-label variants: 20h)",
      "gpu_utilization": "~40-50% effective utilization due to researcher iteration cycles",
      "timeline": "3-4 months (targeting ICRA 2027 or ICLR 2027 deadline ~Sep 2026)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$540-720 (H100 80GB at $3.00-4.00/hr on Lambda/RunPod)"
    },
    "human_in_loop": {
      "gpu_hours": "~200h H100 (agent explores 2 additional λ schedules and pseudo-label ablations)",
      "gpu_utilization": "~65-70%; agent queues next experiment promptly but pauses at approval gates",
      "timeline": "6-8 weeks",
      "team": "1 researcher, ~20min/day reviewing agent proposals",
      "claude_api_cost": "$50-80 (~500-800 turns at ~$0.10/turn Opus)",
      "estimated_gpu_cost": "$600-800 (H100 80GB at $3.00-4.00/hr)",
      "risk_note": "Agent may over-explore pseudo-label generation strategies; approval gates on architecture decisions mitigate waste"
    },
    "auto_research": {
      "gpu_hours": "~400-500h H100 (exhaustive layer search, full λ sweep, cross-backbone validation on SmolVLA, 3 seeds per final config, comprehensive LIBERO-Plus per-dimension analysis)",
      "gpu_utilization": "~85-90%; agent queues experiments 24/7",
      "timeline": "2-3 weeks with 4×H100",
      "team": "0 researchers after ~2h initial setup",
      "claude_api_cost": "$150-250 (~1,500-2,500 turns Opus)",
      "estimated_gpu_cost": "$1,200-2,000 (H100 at $3.00-4.00/hr)",
      "speed_bottleneck": "Pseudo-label generation is sequential per dataset split; parallelizable across task suites",
      "risk_note": "Exceeds 200 H100-hour budget but produces a more thorough paper with multi-seed results and cross-backbone validation; manual and human-in-loop modes fit within budget"
    }
  },
  "target_venues": [
    "ICRA 2027 (expected deadline Sep 2026; top robotics venue, strong fit for affordance + robustness story — 4 months from now, primary target)",
    "ICLR 2027 (expected deadline Sep-Oct 2026; top ML venue, backup if results are strong enough for broader ML audience)",
    "CoRL 2026 IMPOSSIBLE (deadline May 28, 2026 — 10 days away, not feasible even with pre-existing codebase; acknowledged per reviewer feedback)"
  ],
  "level": "top-tier",
  "key_references": [
    "PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation (arXiv 2601.07060, Jan 2026) — strongest affordance-VLA baseline, 91.8% LIBERO-LONG with 4 structured affordance types",
    "FocusVLA: Focused Visual Utilization for Vision-Language-Action Models (arXiv 2603.28740, Mar 2026) — mechanistically closest work, Focus Attention for task-relevant token selection, 98.7% standard LIBERO but no affordance supervision",
    "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation (arXiv 2506.09284, ICRA 2025 Best Paper Finalist) — demonstrates unsupervised affordance pseudo-labels from frozen VLMs, modular pipeline",
    "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models (arXiv 2510.13626, CVPR 2026) — reveals catastrophic VLA brittleness under perturbation, primary evaluation benchmark",
    "CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance (ICCV 2025, arXiv 2412.20451)",
    "AVA-VLA: Improving Vision-Language-Action Models with Active Visual Attention (arXiv 2511.18960) — history-conditioned attention, LIBERO+CALVIN SOTA",
    "Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models (arXiv 2602.20501, Feb 2026) — confirms DINOv2 encodes geometric affordance, Flux encodes interaction priors",
    "Context-Dependent Affordance Computation in Vision-Language Models (arXiv 2603.04419, Feb 2026) — >90% affordance is context-dependent, argues against fixed categories",
    "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (CVPR 2025, arXiv 2503.22020)",
    "AffordGrasp: In-Context Affordance Reasoning for Open-Vocabulary Task-Oriented Grasping in Clutter (arXiv 2503.00778, Mar 2025)",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT, arXiv 2502.19645, 2025) — base model, LoRA fine-tuning recipe",
    "VLA-Adapter: An Effective Paradigm for Tiny-Scale VLA Model (arXiv 2509.09372, 2025) — mid-layer features best for action generation",
    "Stable Language Guidance for Vision-Language-Action Models (arXiv 2601.04052, Jan 2026) — studies affordance-language interaction via subtraction",
    "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps (arXiv 2512.07472, Dec 2024) — inference-time affordance guidance, +23.5% OOD",
    "RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (arXiv 2411.02704, 2024)",
    "VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts (arXiv 2605.06175, 2025) — 81.2% LIBERO-Plus with 2.51% params, PEFT robustness SOTA",
    "Contrastive Representation Regularization for Vision-Language-Action Models (RS-CL, arXiv 2510.01711, 2025) — auxiliary contrastive loss for VLA representation alignment",
    "GLOVER++: Unleashing the Potential of Affordance Learning from Human Behaviors for Robotic Manipulation (CoRL 2025, arXiv 2505.11865)",
    "DeepVision-VLA (arXiv 2603.15618) — multi-level vision feature injection via mixture-of-transformers",
    "A1: A Fully Transparent Open-Source VLA (arXiv 2604.05672, Apr 2026) — adaptive inference with implicit affordance priors"
  ],
  "description": "Current VLAs achieve near-perfect scores on standard manipulation benchmarks but collapse under modest distribution shifts — LIBERO-Plus (CVPR 2026) shows performance drops from 97% to 30-60% under camera, lighting, and layout perturbations. We hypothesize that this brittleness stems from learning generic task-relevant attention (as in FocusVLA, AVA-VLA) that overfits to visual statistics, rather than affordance-grounded features that capture where and how to interact with objects — knowledge that is invariant across visual perturbations. We propose AffordVLA, which distills open-vocabulary affordance pseudo-labels from frozen foundation models (DINOv2 geometric features + VLM interaction priors, following UAD's unsupervised philosophy) into a VLA's intermediate representations via a lightweight auxiliary prediction head. Unlike PALM's 4 rigid affordance types requiring external tools, AffordVLA uses free-form language-conditioned affordance maps with no predefined categories and zero inference overhead (the affordance head is dropped after training). Unlike FocusVLA's generic attention, AffordVLA has an explicit affordance training signal that produces qualitatively different — and more robust — feature representations. Unlike UAD and RT-Affordance's modular pipelines, AffordVLA integrates affordance end-to-end in a single forward pass. Built on OpenVLA-OFT with LoRA (~7M added parameters), the approach fits within 200 H100-hours. Evaluation centers on LIBERO-Plus robustness across 7 perturbation dimensions, with ablations demonstrating that affordance-supervised attention learns different patterns than action-loss-only attention, and that open-vocabulary pseudo-labels outperform PALM's fixed categories on novel instruction verbs.",
  "project_name": "afford_vla",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL OMISSION — PALM (arXiv 2601.07060, Jan 2026): Uses 4 predefined affordance types (Global/Local/Spatial/Dynamic) with language conditioning in an end-to-end VLA framework, achieving 91.8% on LIBERO-LONG (vs CoA-VLA's 55.0%). This is the strongest affordance-integrated VLA baseline as of early 2026 and is completely absent from the proposal's landscape and baselines.", "CRITICAL OMISSION — UAD (arXiv 2506.09284, ICRA 2025 Best Paper Finalist): Unsupervised affordance distillation from VLMs with open-vocabulary language instructions, demonstrating that affordance knowledge can be extracted from foundation models without manual annotations. Directly relevant as affordance quality baseline and as evidence that modular affordance extraction already works well.", "CRITICAL OMISSION — FocusVLA (arXiv 2603.28740, Mar 2026): Proposes 'Modality Cascaded Attention' to direct VLA attention to task-relevant visual regions and 'Focus Attention' for dynamic visual token selection. This is mechanistically near-identical to LA³'s cross-attention-based visual feature amplification, just without the 'affordance' label. The proposal must explicitly differentiate from FocusVLA.", "COMPUTE BUDGET VIOLATION: User specified ≤200 H100-hours. The manual estimate alone is 3,500h A100 (~17x over budget). The proposal has silently abandoned the user's hard constraint without justification.", "VENUE TARGET MISMATCH: User specified CoRL 2026. The proposal lists ICLR 2027 as primary target, relegating CoRL 2026 to 'feasible only under auto_research.' CoRL 2026 deadline is May 28, 2026 — 10 days from now — making even the auto_research path unrealistic.", "SUPERVISION SIGNAL GAP: The proposal claims LA³ requires 'no explicit affordance annotations' and trains end-to-end with action prediction loss only. But without any affordance-specific supervision, what distinguishes the learned cross-attention patterns from generic task-relevant attention? The probing study (arXiv 2602.20501) shows VLMs encode affordance for perception, not that action prediction loss alone can activate this knowledge for manipulation.", "NOVELTY INFLATION — 'Affordance' vs. 'Task-Relevant Attention': Multiple 2025-2026 works (FocusVLA, DeepVision-VLA, VLA-Adapter, AVA-VLA) already use language-conditioned attention mechanisms to amplify task-relevant visual features in VLA intermediate layers. The proposal's use of the word 'affordance' does not constitute a technical contribution beyond these existing mechanisms unless there is an affordance-specific training signal or architectural component.", "MISSING BASELINE — CoT-VLA (CVPR 2025): Visual chain-of-thought reasoning for VLA, representing the reasoning-augmented VLA paradigm that competes with affordance-based reasoning.", "MISSING BASELINE — AffordGrasp (arXiv 2503.00778, Mar 2025): Open-vocabulary affordance reasoning via VLM for grasping, relevant for open-vocabulary affordance quality comparison."]
Feedback: The idea addresses a real gap (open-vocabulary affordance in end-to-end VLA) but has critical issues requiring revision:

1. **Address PALM as primary baseline**: PALM (Jan 2026) is now the strongest affordance-VLA baseline (91.8% LIBERO-LONG). You must include it in your landscape and baselines, and argue specifically where open-vocabulary affordance provides gains over PALM's predefined types. Focus evaluation on scenarios where PALM's 4 types demonstrably fail (novel interaction verbs, compositional instructions, cross-domain objects).

2. **Differentiate from FocusVLA/DeepVision-VLA**: Your cross-attention module is architecturally very similar to FocusVLA's Focus Attention and DeepVision-VLA's multi-level feature injection. Either (a) introduce an affordance-specific training signal (e.g., contrastive loss from the probing study, weak supervision from VLM-generated affordance descriptions à la UAD), or (b) demonstrate empirically that the 'affordance framing' produces qualitatively different attention patterns than generic task-relevant attention.

3. **Resolve the supervision signal problem**: The current proposal has no mechanism for the model to learn 'affordance' attention vs. generic attention. Consider adding: (a) a contrastive auxiliary loss using VLM-generated affordance descriptions as pseudo-labels (leveraging the UAD approach), (b) an affordance consistency regularization (as suggested in your own exploration direction #5), or (c) knowledge distillation from a frozen VLM's affordance probing features (direction #4).

4. **Respect compute constraints or justify deviation**: The user specified ≤200 H100-hours. Either redesign the experiments to fit (e.g., smaller-scale ablations, fewer baselines, leveraging pre-trained checkpoints more aggressively), or explicitly justify why this budget is insufficient and propose a minimal viable experiment plan within budget.

5. **Fix venue targeting**: CoRL 2026 (May 28 deadline) is 10 days away and impossible. Either target CoRL 2026 with a drastically scoped-down version, or honestly acknowledge ICLR 2027 as the realistic target and adjust the timeline accordingly.

6. **Include UAD, AffordGrasp, and CoT-VLA in landscape**: UAD (ICRA 2025 Best Paper) is particularly important as it demonstrates that unsupervised affordance distillation from VLMs already works — your approach must show end-to-end integration outperforms this modular distillation approach.


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
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "bf83c38f-4587-4d3d-a4d6-b4565bec693b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T19:12:09.879Z_

```json
{
  "parentUuid": "bf83c38f-4587-4d3d-a4d6-b4565bec693b",
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
  "uuid": "5e65aad4-9ead-4af9-8d53-204d5369dace",
  "timestamp": "2026-05-18T19:12:09.879Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T19:12:09.879Z_

```json
{
  "parentUuid": "5e65aad4-9ead-4af9-8d53-204d5369dace",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ad0eee02-ff07-4544-849c-cfaf5479fb58",
  "timestamp": "2026-05-18T19:12:09.879Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
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
  "leafUuid": "ad0eee02-ff07-4544-849c-cfaf5479fb58",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "AffordVLA: Open-vocabulary affordance distillation into VLA for robust manipulation",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Assistant

_source line 8 · 2026-05-18T19:12:18.883Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this revised idea for "AffordVLA: Distilling Open-Vocabulary Affordance into VLA Representations for Robust Manipulation." This is round 2 of review, and I need to verify the claims, check for missing work, and assess whether the previous round's issues have been adequately addressed.

Let me start by conducting independent searches to verify the key claims and check for missing work.

Key things to verify:
1. PALM (arXiv 2601.07060) - now included, verify claims
2. FocusVLA (arXiv 2603.28740) - now included, verify differentiation


3. UAD (arXiv 2506.09284) - now included, verify claims
4. LIBERO-Plus (arXiv 2510.13626) - verify as CVPR 2026
5. Check for any new concurrent work missed
6. Verify the supervision signal approach (auxiliary affordance prediction loss)
7. Check compute budget compliance
8. Verify venue targeting fix
9. Check novelty against existing work more carefully

Let me search systematically through these verification points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad0eee02-ff07-4544-849c-cfaf5479fb58",
  "isSidechain": false,
  "requestId": "req_011CbAZjU6b9N7jXz7muzQ5C",
  "type": "assistant",
  "uuid": "1212f5b3-6f0c-4398-baf6-dcf2f8c0b93e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152HezaH36rDoN88c6TrJc1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18808,
      "cache_read_input_tokens": 11841,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 378,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18808
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

_source line 9 · 2026-05-18T19:12:18.907Z_

I'll conduct an independent, thorough review of this revised proposal. Let me start by verifying key claims and searching for potentially missed work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1212f5b3-6f0c-4398-baf6-dcf2f8c0b93e",
  "isSidechain": false,
  "requestId": "req_011CbAZjU6b9N7jXz7muzQ5C",
  "type": "assistant",
  "uuid": "d3c82756-e3da-4bc0-882c-61b1c922dc4a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152HezaH36rDoN88c6TrJc1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18808,
      "cache_read_input_tokens": 11841,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 378,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18808
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

_source line 10 · 2026-05-18T19:12:18.909Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JraVxzhKVczi6aAhVNkSqQ`</summary>

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
  "parentUuid": "d3c82756-e3da-4bc0-882c-61b1c922dc4a",
  "isSidechain": false,
  "requestId": "req_011CbAZjU6b9N7jXz7muzQ5C",
  "type": "assistant",
  "uuid": "80689e7c-afd7-457a-b2e3-bd51280ef243",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152HezaH36rDoN88c6TrJc1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18808,
      "cache_read_input_tokens": 11841,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 378,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18808
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

_source line 11 · 2026-05-18T19:12:18.916Z_

<details><summary>↩ Tool result · `toolu_01JraVxzhKVczi6aAhVNkSqQ`</summary>

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
  "parentUuid": "80689e7c-afd7-457a-b2e3-bd51280ef243",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "68dbf665-330a-4cfb-8483-8c495ac8f7f8",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "80689e7c-afd7-457a-b2e3-bd51280ef243",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-18T19:12:21.816Z_

Now let me run several parallel searches to verify key claims and find potentially missed work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68dbf665-330a-4cfb-8483-8c495ac8f7f8",
  "isSidechain": false,
  "requestId": "req_011CbAZk8c6RLtNLetAz4hmz",
  "type": "assistant",
  "uuid": "08482b17-42c1-46b1-8d1f-636a1980f029",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SA1BFmqeAmaJM7k1ke3C1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 30649,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1398,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 30649,
          "cache_creation_input_tokens": 1398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1398
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

_source line 13 · 2026-05-18T19:12:21.977Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013HqhtXKJD2Y9DALUroXjqx`</summary>

```json
{
  "query": "PALM affordance VLA arXiv 2601.07060 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08482b17-42c1-46b1-8d1f-636a1980f029",
  "isSidechain": false,
  "requestId": "req_011CbAZk8c6RLtNLetAz4hmz",
  "type": "assistant",
  "uuid": "f9ee9e66-3035-41d4-9183-83bb27334759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014SA1BFmqeAmaJM7k1ke3C1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1398,
      "cache_read_input_tokens": 30649,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1398,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 88,
          "cache_read_input_tokens": 30649,
          "cache_creation_input_tokens": 1398,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1398
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

_source line 14 · 2026-05-18T19:12:41.595Z_

<details><summary>↩ Tool result · `toolu_013HqhtXKJD2Y9DALUroXjqx`</summary>

```text
Web search results for query: "PALM affordance VLA arXiv 2601.07060 2026"

Links: [{"title":"[2601.07060] PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation","url":"https://arxiv.org/abs/2601.07060"},{"title":"(PDF) PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation","url":"https://www.researchgate.net/publication/399707765_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_Manipulation"},{"title":"PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation","url":"https://arxiv.org/html/2601.07060"},{"title":"A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation | Request PDF","url":"https://www.researchgate.net/publication/390892539_A0_An_Affordance-Aware_Hierarchical_Model_for_General_Robotic_Manipulation"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"}]

Based on the search results, here's what I found about PALM and arXiv 2601.07060:

PALM is a VLA framework that structures policy learning around interaction-centric affordance reasoning and subtask progress cues. The paper was published in January 2026.

Recent advancements in vision-language-action (VLA) models have shown promise in robotic manipulation, yet they continue to struggle with long-horizon, multi-step tasks, with existing methods lacking internal reasoning mechanisms that can identify task-relevant interaction cues or track progress within a subtask.

PALM distills complementary affordance representations that capture object relevance, contact geometry, spatial placements, and motion dynamics, and serve as task-relevant anchors for visuomotor control, while also predicting continuous within-subtask progress to enable seamless subtask transitions.

Across extensive simulation and real-world experiments, PALM consistently outperforms baselines, achieving a 91.8% success rate on LIBERO-LONG, a 12.5% improvement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9ee9e66-3035-41d4-9183-83bb27334759",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "d12521da-8b21-43c1-a720-785d97b17ffa",
  "toolUseResult": {
    "query": "PALM affordance VLA arXiv 2601.07060 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TBQYsw8CFrk4KsnN2JbiaX",
        "content": [
          {
            "title": "[2601.07060] PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation",
            "url": "https://arxiv.org/abs/2601.07060"
          },
          {
            "title": "(PDF) PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation",
            "url": "https://www.researchgate.net/publication/399707765_PALM_Progress-Aware_Policy_Learning_via_Affordance_Reasoning_for_Long-Horizon_Robotic_Manipulation"
          },
          {
            "title": "PALM: Progress-Aware Policy Learning via Affordance Reasoning for Long-Horizon Robotic Manipulation",
            "url": "https://arxiv.org/html/2601.07060"
          },
          {
            "title": "A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation | Request PDF",
            "url": "https://www.researchgate.net/publication/390892539_A0_An_Affordance-Aware_Hierarchical_Model_for_General_Robotic_Manipulation"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          },
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance",
            "url": "https://arxiv.org/pdf/2412.20451"
          }
        ]
      },
      "Based on the search results, here's what I found about PALM and arXiv 2601.07060:\n\nPALM is a VLA framework that structures policy learning around interaction-centric affordance reasoning and subtask progress cues. The paper was published in January 2026.\n\nRecent advancements in vision-language-action (VLA) models have shown promise in robotic manipulation, yet they continue to struggle with long-horizon, multi-step tasks, with existing methods lacking internal reasoning mechanisms that can identify task-relevant interaction cues or track progress within a subtask.\n\nPALM distills complementary affordance representations that capture object relevance, contact geometry, spatial placements, and motion dynamics, and serve as task-relevant anchors for visuomotor control, while also predicting continuous within-subtask progress to enable seamless subtask transitions.\n\nAcross extensive simulation and real-world experiments, PALM consistently outperforms baselines, achieving a 91.8% success rate on LIBERO-LONG, a 12.5% improvement."
    ],
    "durationSeconds": 19.612750347000002
  },
  "sourceToolAssistantUUID": "f9ee9e66-3035-41d4-9183-83bb27334759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T19:12:44.133Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B5dpEGCihfNFwmen51dgWX`</summary>

```json
{
  "query": "FocusVLA Focus Attention visual token selection VLA 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d12521da-8b21-43c1-a720-785d97b17ffa",
  "isSidechain": false,
  "requestId": "req_011CbAZmoSV1fQXSRpMxkVof",
  "type": "assistant",
  "uuid": "b1b6017f-5b1c-4785-8189-9e2c9e9662fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5EyfgrHPhFAFhtSfnHQWR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 32047,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 737,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 32047,
          "cache_creation_input_tokens": 737,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 737
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

_source line 16 · 2026-05-18T19:12:52.635Z_

<details><summary>↩ Tool result · `toolu_01B5dpEGCihfNFwmen51dgWX`</summary>

```text
Web search results for query: "FocusVLA Focus Attention visual token selection VLA 2026 arXiv"

Links: [{"title":"Robotics arXiv Digest — 2026-03-30 - Kiru Park / Vision for Robotics","url":"https://www.visionforrobotics.com/robotics-digest/digest_2026-03-30.html"},{"title":"[2603.28740] FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.28740"},{"title":"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.28740"},{"title":"FocusVLA: Focused Visual Utilization for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.28740"},{"title":"Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.24941"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"}]

I found relevant information about FocusVLA from the arXiv search results.

## FocusVLA: Focused Visual Utilization for Vision-Language-Action Models

FocusVLA is a novel paradigm for Vision-Language-Action (VLA) models that improves action generation by conditioning policies on rich vision-language information, directing the model's attention to task-relevant visual regions to effectively bridge vision to action.

### Key Problem and Approach

Current auto-regressive VLA policies face three bottlenecks: architectural bias that drives models to overlook visual details, an excessive number of visual tokens that makes attention difficult to focus on the correct regions, and task-irrelevant visual information that introduces substantial noise. Unlike prior VLA work that addressed visual representation quality, FocusVLA addresses visual representation utilization — how the policy network uses existing representations — finding this to be the dominant bottleneck.

### Focus Attention Mechanism

FocusVLA proposes Focus Attention, which dynamically selects task-relevant visual patches to control information quantity while explicitly modulating their influence to suppress task-irrelevant noise. The paper's ablation reveals that a simple attention-focusing mechanism that restricts cross-attention to the top-K most task-relevant visual tokens outperforms standard attention by a larger margin than switching from a weaker to stronger visual encoder.

### Performance Benefits

Reducing visual token count via selective retention improves not only accuracy but also inference speed, making FocusVLA more suitable for real-time deployment than architectures that process all visual tokens uniformly.

The paper was published on arXiv on **March 30, 2026** (arXiv ID: 2603.28740).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1b6017f-5b1c-4785-8189-9e2c9e9662fb",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "06ecd27b-1391-4fe2-a907-64bf8da7ff87",
  "toolUseResult": {
    "query": "FocusVLA Focus Attention visual token selection VLA 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V2zen4C8YmpULD1eW74ANb",
        "content": [
          {
            "title": "Robotics arXiv Digest — 2026-03-30 - Kiru Park / Vision for Robotics",
            "url": "https://www.visionforrobotics.com/robotics-digest/digest_2026-03-30.html"
          },
          {
            "title": "[2603.28740] FocusVLA: Focused Visual Utilization for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.28740"
          },
          {
            "title": "FocusVLA: Focused Visual Utilization for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.28740"
          },
          {
            "title": "FocusVLA: Focused Visual Utilization for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.28740"
          },
          {
            "title": "Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2603.24941"
          },
          {
            "title": "[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/abs/2511.16449"
          }
        ]
      },
      "I found relevant information about FocusVLA from the arXiv search results.\n\n## FocusVLA: Focused Visual Utilization for Vision-Language-Action Models\n\nFocusVLA is a novel paradigm for Vision-Language-Action (VLA) models that improves action generation by conditioning policies on rich vision-language information, directing the model's attention to task-relevant visual regions to effectively bridge vision to action.\n\n### Key Problem and Approach\n\nCurrent auto-regressive VLA policies face three bottlenecks: architectural bias that drives models to overlook visual details, an excessive number of visual tokens that makes attention difficult to focus on the correct regions, and task-irrelevant visual information that introduces substantial noise. Unlike prior VLA work that addressed visual representation quality, FocusVLA addresses visual representation utilization — how the policy network uses existing representations — finding this to be the dominant bottleneck.\n\n### Focus Attention Mechanism\n\nFocusVLA proposes Focus Attention, which dynamically selects task-relevant visual patches to control information quantity while explicitly modulating their influence to suppress task-irrelevant noise. The paper's ablation reveals that a simple attention-focusing mechanism that restricts cross-attention to the top-K most task-relevant visual tokens outperforms standard attention by a larger margin than switching from a weaker to stronger visual encoder.\n\n### Performance Benefits\n\nReducing visual token count via selective retention improves not only accuracy but also inference speed, making FocusVLA more suitable for real-time deployment than architectures that process all visual tokens uniformly.\n\nThe paper was published on arXiv on **March 30, 2026** (arXiv ID: 2603.28740)."
    ],
    "durationSeconds": 8.497298452000003
  },
  "sourceToolAssistantUUID": "b1b6017f-5b1c-4785-8189-9e2c9e9662fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T19:12:55.522Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YXkf8bz4jekmv7bmhn2ct6`</summary>

```json
{
  "query": "LIBERO-Plus robustness VLA benchmark CVPR 2026 arXiv 2510.13626"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06ecd27b-1391-4fe2-a907-64bf8da7ff87",
  "isSidechain": false,
  "requestId": "req_011CbAZncdNxp1wvfQhj6pds",
  "type": "assistant",
  "uuid": "6cf34eef-efa6-463e-a161-039f531b8b09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbyzXYFmNH3kvbUxYi5fos",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 32784,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 32784,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 18 · 2026-05-18T19:13:03.772Z_

<details><summary>↩ Tool result · `toolu_01YXkf8bz4jekmv7bmhn2ct6`</summary>

```text
Web search results for query: "LIBERO-Plus robustness VLA benchmark CVPR 2026 arXiv 2510.13626"

Links: [{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"}]

Based on the search results, I found detailed information about LIBERO-Plus:

## LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models

LIBERO-Plus addresses how Visual-Language-Action (VLA) models report impressive success rates on robotic manipulation benchmarks, yet these results may mask fundamental weaknesses in robustness.

### Methodology

The paper performs a systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

### Key Findings

The analysis exposes critical weaknesses: models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. 

Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

### Broader Implications

The findings challenge the assumption that high original LIBERO benchmark scores equate to true competency, revealing that current VLA models remain brittle, showing particular vulnerability to camera and robot state changes, largely ignore language instructions, and exhibit positional bias rather than genuine semantic understanding.

The paper appears to have been presented at CVPR 2026 and is available on arXiv as preprint 2510.13626.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6cf34eef-efa6-463e-a161-039f531b8b09",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "680b40a6-52f6-40be-b425-cb9ffc62a63b",
  "toolUseResult": {
    "query": "LIBERO-Plus robustness VLA benchmark CVPR 2026 arXiv 2510.13626",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T9cod5eiv1HW3dvbxxpgmD",
        "content": [
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2026/poster/38735"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626v1"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301v1"
          }
        ]
      },
      "Based on the search results, I found detailed information about LIBERO-Plus:\n\n## LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\n\nLIBERO-Plus addresses how Visual-Language-Action (VLA) models report impressive success rates on robotic manipulation benchmarks, yet these results may mask fundamental weaknesses in robustness.\n\n### Methodology\n\nThe paper performs a systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.\n\n### Key Findings\n\nThe analysis exposes critical weaknesses: models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. \n\nSurprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.\n\n### Broader Implications\n\nThe findings challenge the assumption that high original LIBERO benchmark scores equate to true competency, revealing that current VLA models remain brittle, showing particular vulnerability to camera and robot state changes, largely ignore language instructions, and exhibit positional bias rather than genuine semantic understanding.\n\nThe paper appears to have been presented at CVPR 2026 and is available on arXiv as preprint 2510.13626."
    ],
    "durationSeconds": 8.245321005999998
  },
  "sourceToolAssistantUUID": "6cf34eef-efa6-463e-a161-039f531b8b09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-18T19:13:07.001Z_

Good, LIBERO-Plus at CVPR 2026 is confirmed. Now let me search for potentially missed concurrent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "680b40a6-52f6-40be-b425-cb9ffc62a63b",
  "isSidechain": false,
  "requestId": "req_011CbAZoSFKqicJHQyXVktEs",
  "type": "assistant",
  "uuid": "982635fb-1965-4808-b175-25789fab1766",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018amRWRPgUbZLQNoDPZkepq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 33592,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 859,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 33592,
          "cache_creation_input_tokens": 859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 859
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

_source line 20 · 2026-05-18T19:13:07.323Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QxPffYgF9XYhkdBZ3QZDPq`</summary>

```json
{
  "query": "affordance distillation VLA end-to-end robot manipulation 2025 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "982635fb-1965-4808-b175-25789fab1766",
  "isSidechain": false,
  "requestId": "req_011CbAZoSFKqicJHQyXVktEs",
  "type": "assistant",
  "uuid": "a7b9a7a2-00c2-4a34-b526-299ddc71a55f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018amRWRPgUbZLQNoDPZkepq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 33592,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 859,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 104,
          "cache_read_input_tokens": 33592,
          "cache_creation_input_tokens": 859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 859
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a7b9a7a2-00c2-4a34-b526-299ddc71a55f",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "AffordVLA: Open-vocabulary affordance distillation into VLA for robust manipulation",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Tool result

_source line 23 · 2026-05-18T19:13:17.209Z_

<details><summary>↩ Tool result · `toolu_01QxPffYgF9XYhkdBZ3QZDPq`</summary>

```text
Web search results for query: "affordance distillation VLA end-to-end robot manipulation 2025 2026 arXiv"

Links: [{"title":"[2506.09284] UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/abs/2506.09284"},{"title":"Parallels Between VLA Model Post-Training and Human ...","url":"https://arxiv.org/pdf/2506.20966"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.10109"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/html/2506.09284v1"},{"title":"End-to-End Affordance Learning for Robotic Manipulation","url":"https://arxiv.org/pdf/2209.12941"}]

Here are the search results for affordance distillation, VLA models, and end-to-end robot manipulation from 2025-2026 on arXiv:

## Key Recent Papers

1. **UAD: Unsupervised Affordance Distillation** (June 2025)
   - UAD is a method for distilling affordance knowledge from foundation models into a task-conditioned affordance model without any manual annotations
   - By leveraging the complementary strengths of large vision models and vision-language models, UAD automatically annotates a large-scale dataset with detailed image-affordance pairs
   - Using affordance provided by UAD as the observation space, an imitation learning policy demonstrates promising generalization to unseen object instances, object categories, and variations in task instructions after training on as few as 10 demonstrations

2. **Affordance Field Intervention (AFI)** (December 2025)
   - AFI is a lightweight hybrid framework that uses Spatial Affordance Fields (SAFs) as an on-demand plugin to guide VLA behavior
   - This addresses limitations of end-to-end VLA design, which lacks explicit 3D spatial reasoning and prevents reliable identification of actionable regions in unfamiliar environments

3. **VLA Model Post-Training Research**
   - Recent work post-trains VLMs to extract spatial affordances of target objects and guide manipulation, integrating consistency distillation with early-exit strategies to improve decoding efficiency

These papers represent recent advances in combining affordance learning with vision-language-action models for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7b9a7a2-00c2-4a34-b526-299ddc71a55f",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "29278277-1738-45c9-98ae-057394bf1ebe",
  "toolUseResult": {
    "query": "affordance distillation VLA end-to-end robot manipulation 2025 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q5ymnfDo4sjabe8ZFGiY8P",
        "content": [
          {
            "title": "[2506.09284] UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation",
            "url": "https://arxiv.org/abs/2506.09284"
          },
          {
            "title": "Parallels Between VLA Model Post-Training and Human ...",
            "url": "https://arxiv.org/pdf/2506.20966"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2602.10109"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation",
            "url": "https://arxiv.org/html/2506.09284v1"
          },
          {
            "title": "End-to-End Affordance Learning for Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2209.12941"
          }
        ]
      },
      "Here are the search results for affordance distillation, VLA models, and end-to-end robot manipulation from 2025-2026 on arXiv:\n\n## Key Recent Papers\n\n1. **UAD: Unsupervised Affordance Distillation** (June 2025)\n   - UAD is a method for distilling affordance knowledge from foundation models into a task-conditioned affordance model without any manual annotations\n   - By leveraging the complementary strengths of large vision models and vision-language models, UAD automatically annotates a large-scale dataset with detailed image-affordance pairs\n   - Using affordance provided by UAD as the observation space, an imitation learning policy demonstrates promising generalization to unseen object instances, object categories, and variations in task instructions after training on as few as 10 demonstrations\n\n2. **Affordance Field Intervention (AFI)** (December 2025)\n   - AFI is a lightweight hybrid framework that uses Spatial Affordance Fields (SAFs) as an on-demand plugin to guide VLA behavior\n   - This addresses limitations of end-to-end VLA design, which lacks explicit 3D spatial reasoning and prevents reliable identification of actionable regions in unfamiliar environments\n\n3. **VLA Model Post-Training Research**\n   - Recent work post-trains VLMs to extract spatial affordances of target objects and guide manipulation, integrating consistency distillation with early-exit strategies to improve decoding efficiency\n\nThese papers represent recent advances in combining affordance learning with vision-language-action models for robotic manipulation tasks."
    ],
    "durationSeconds": 9.882447475000001
  },
  "sourceToolAssistantUUID": "a7b9a7a2-00c2-4a34-b526-299ddc71a55f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T19:13:20.981Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KqWcBQ6ENnjYKzShTJyzyT`</summary>

```json
{
  "query": "open-vocabulary affordance VLA auxiliary loss training signal robot 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29278277-1738-45c9-98ae-057394bf1ebe",
  "isSidechain": false,
  "requestId": "req_011CbAZpRnKWnUy2hehfESDa",
  "type": "assistant",
  "uuid": "c7ae9d8d-e393-450f-8b04-531b71219a32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZwhLMW7vqfiapkN6Nt5uz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 34451,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 34451,
          "cache_creation_input_tokens": 880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 880
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

_source line 25 · 2026-05-18T19:13:27.841Z_

<details><summary>↩ Tool result · `toolu_01KqWcBQ6ENnjYKzShTJyzyT`</summary>

```text
Web search results for query: "open-vocabulary affordance VLA auxiliary loss training signal robot 2026"

Links: [{"title":"Open-Vocabulary Affordance Detection in 3D Point Clouds","url":"https://arxiv.org/pdf/2303.02401"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://www.researchgate.net/publication/403112103_SG-VLA_Learning_Spatially-Grounded_Vision-Language-Action_Models_for_Mobile_Manipulation"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot   Manipulation through LLM Affordance-Grounding","url":"https://arxiv.org/pdf/2404.11000"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"}]

I found relevant research on open-vocabulary affordance detection and vision-language-action (VLA) models for robotics. Here's what the search results show:

**Open-Vocabulary Affordance Detection:**
Open-Vocabulary Affordance Detection (OpenAD) is a method capable of detecting an unbounded number of affordances in 3D point clouds. This method enables zero-shot detection and can detect previously unseen affordances without a single annotation example.

**VLA Models and Auxiliary Training Signals:**
Recent work on VLA (Vision-Language-Action) models for robotics has explored auxiliary losses as training signals. SG-VLA co-trains auxiliary decoders that reconstruct interpretable intermediate signals - including global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks - from shared visual-language representations.

**VLA Generalization Challenges:**
Existing VLA models often struggle with robust action planning in unseen contexts, relying heavily instead on memorized or imitated trajectories from their training data distribution. Recent studies have explored the integration of reinforcement learning (RL) to enhance the generalization capabilities of VLA models, and these approaches aim to adapt VLA policies to diverse and unseen scenarios beyond mere imitation.

The search results indicate active research in 2025-2026 combining open-vocabulary affordance understanding with VLA training using auxiliary losses and various supervision signals for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7ae9d8d-e393-450f-8b04-531b71219a32",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "d8da9d8b-613c-4e84-a3f2-0054744abef2",
  "toolUseResult": {
    "query": "open-vocabulary affordance VLA auxiliary loss training signal robot 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QaJuo9P3dYKG3uj3m5n2TD",
        "content": [
          {
            "title": "Open-Vocabulary Affordance Detection in 3D Point Clouds",
            "url": "https://arxiv.org/pdf/2303.02401"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://www.researchgate.net/publication/403112103_SG-VLA_Learning_Spatially-Grounded_Vision-Language-Action_Models_for_Mobile_Manipulation"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "OpenVLA: Open Source VLA for Robotics",
            "url": "https://www.emergentmind.com/topics/openvla"
          },
          {
            "title": "OVAL-Prompt: Open-Vocabulary Affordance Localization for Robot   Manipulation through LLM Affordance-Grounding",
            "url": "https://arxiv.org/pdf/2404.11000"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          }
        ]
      },
      "I found relevant research on open-vocabulary affordance detection and vision-language-action (VLA) models for robotics. Here's what the search results show:\n\n**Open-Vocabulary Affordance Detection:**\nOpen-Vocabulary Affordance Detection (OpenAD) is a method capable of detecting an unbounded number of affordances in 3D point clouds. This method enables zero-shot detection and can detect previously unseen affordances without a single annotation example.\n\n**VLA Models and Auxiliary Training Signals:**\nRecent work on VLA (Vision-Language-Action) models for robotics has explored auxiliary losses as training signals. SG-VLA co-trains auxiliary decoders that reconstruct interpretable intermediate signals - including global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks - from shared visual-language representations.\n\n**VLA Generalization Challenges:**\nExisting VLA models often struggle with robust action planning in unseen contexts, relying heavily instead on memorized or imitated trajectories from their training data distribution. Recent studies have explored the integration of reinforcement learning (RL) to enhance the generalization capabilities of VLA models, and these approaches aim to adapt VLA policies to diverse and unseen scenarios beyond mere imitation.\n\nThe search results indicate active research in 2025-2026 combining open-vocabulary affordance understanding with VLA training using auxiliary losses and various supervision signals for robotic manipulation tasks."
    ],
    "durationSeconds": 6.856505345999991
  },
  "sourceToolAssistantUUID": "c7ae9d8d-e393-450f-8b04-531b71219a32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T19:13:30.582Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CVc5pde2YsbRvjJEj6wbmv`</summary>

```json
{
  "query": "SG-VLA spatially grounded VLA affordance auxiliary decoder 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8da9d8b-613c-4e84-a3f2-0054744abef2",
  "isSidechain": false,
  "requestId": "req_011CbAZqD8bX4VoZBLGp9X7w",
  "type": "assistant",
  "uuid": "6757473e-9b53-472d-8b64-a3f33c2b45c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RAnJjW6D9Z3CURUZDBazC5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 35331,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 35331,
          "cache_creation_input_tokens": 796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 796
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

_source line 27 · 2026-05-18T19:13:36.979Z_

<details><summary>↩ Tool result · `toolu_01CVc5pde2YsbRvjJEj6wbmv`</summary>

```text
Web search results for query: "SG-VLA spatially grounded VLA affordance auxiliary decoder 2026"

Links: [{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://www.researchgate.net/publication/403112103_SG-VLA_Learning_Spatially-Grounded_Vision-Language-Action_Models_for_Mobile_Manipulation"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/pdf/2603.22760"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/html/2603.22760v1"},{"title":"[2603.22760] SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/abs/2603.22760"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation · benchmark | Festivus","url":"https://festivus.hapticlabs.ai/data/benchmarks/sg-vla-learning-spatially-grounded-vision-language-action-models-for-mobile-mani"}]

Based on the search results, here's what I found about SG-VLA:

SG-VLA (Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation) is a research project from UC San Diego and Lambda, Inc.

**Key Features:**

The framework strengthens perception and representation learning through auxiliary task co-training and multi-modal input enhancement. The method addresses controlling a 13-dimensional action space involving coordinated base motion, arm articulation, and gripper actuation, and incorporates multi-view RGB observations, depth cues, and short temporal history.

**Auxiliary Decoders:**

The approach co-trains a suite of auxiliary decoders that reconstruct interpretable intermediate signals—including global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks—from shared visual-language features.

**Results:**

SG-VLA achieves average success rates of 73% compared to 60% for direct imitation learning on home rearrangement tasks on the ManiSkill-HAB benchmark.

The research was published in March 2026 and demonstrates that spatially-grounded vision-language-action models with auxiliary task learning are effective for mobile manipulation in household environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6757473e-9b53-472d-8b64-a3f33c2b45c3",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "de714b39-15bd-4e2d-8b39-cfe8d3ab0a5e",
  "toolUseResult": {
    "query": "SG-VLA spatially grounded VLA affordance auxiliary decoder 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014sCim4ejBEsMn4DqK3h97Q",
        "content": [
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://www.researchgate.net/publication/403112103_SG-VLA_Learning_Spatially-Grounded_Vision-Language-Action_Models_for_Mobile_Manipulation"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/pdf/2603.22760"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/html/2603.22760v1"
          },
          {
            "title": "[2603.22760] SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/abs/2603.22760"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation · benchmark | Festivus",
            "url": "https://festivus.hapticlabs.ai/data/benchmarks/sg-vla-learning-spatially-grounded-vision-language-action-models-for-mobile-mani"
          }
        ]
      },
      "Based on the search results, here's what I found about SG-VLA:\n\nSG-VLA (Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation) is a research project from UC San Diego and Lambda, Inc.\n\n**Key Features:**\n\nThe framework strengthens perception and representation learning through auxiliary task co-training and multi-modal input enhancement. The method addresses controlling a 13-dimensional action space involving coordinated base motion, arm articulation, and gripper actuation, and incorporates multi-view RGB observations, depth cues, and short temporal history.\n\n**Auxiliary Decoders:**\n\nThe approach co-trains a suite of auxiliary decoders that reconstruct interpretable intermediate signals—including global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks—from shared visual-language features.\n\n**Results:**\n\nSG-VLA achieves average success rates of 73% compared to 60% for direct imitation learning on home rearrangement tasks on the ManiSkill-HAB benchmark.\n\nThe research was published in March 2026 and demonstrates that spatially-grounded vision-language-action models with auxiliary task learning are effective for mobile manipulation in household environments."
    ],
    "durationSeconds": 6.392374824999992
  },
  "sourceToolAssistantUUID": "6757473e-9b53-472d-8b64-a3f33c2b45c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28 · 2026-05-18T19:13:36.987Z_

```json
{
  "parentUuid": "de714b39-15bd-4e2d-8b39-cfe8d3ab0a5e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8bf82ed4-d0dd-40e0-ba2f-138bacd0df4b",
  "timestamp": "2026-05-18T19:13:36.987Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 29 · 2026-05-18T19:13:40.448Z_

This is a critical find — SG-VLA uses auxiliary decoders for affordance-related signals. Let me dig deeper into this and search for more concurrent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bf82ed4-d0dd-40e0-ba2f-138bacd0df4b",
  "isSidechain": false,
  "requestId": "req_011CbAZqtE5VyXc5ZyDPzseG",
  "type": "assistant",
  "uuid": "22e31d8a-6326-4133-94a4-5a112e4542bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpkJv8n7rPSMaobXoW2fsP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 814,
      "cache_read_input_tokens": 36127,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 36127,
          "cache_creation_input_tokens": 814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 814
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

_source line 30 · 2026-05-18T19:13:41.912Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0183NJyZPvEWfrBBuZM9x938`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.22760",
  "prompt": "Extract the full abstract and key method details of SG-VLA. Specifically: 1) What auxiliary tasks are trained? 2) Does it use affordance prediction as an auxiliary loss? 3) What is the architecture? 4) What are the main results? 5) Is it end-to-end trained?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22e31d8a-6326-4133-94a4-5a112e4542bb",
  "isSidechain": false,
  "requestId": "req_011CbAZqtE5VyXc5ZyDPzseG",
  "type": "assistant",
  "uuid": "8d099992-66d7-4267-9630-558af1b3490a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpkJv8n7rPSMaobXoW2fsP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 814,
      "cache_read_input_tokens": 36127,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 36127,
          "cache_creation_input_tokens": 814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 814
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

_source line 31 · 2026-05-18T19:13:46.955Z_

<details><summary>↩ Tool result · `toolu_0183NJyZPvEWfrBBuZM9x938`</summary>

```text
# SG-VLA Paper Summary

Based on the arXiv abstract provided, here are the key details:

## 1) Auxiliary Tasks
The paper co-trains auxiliary decoders that reconstruct: "global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks."

## 2) Affordance Prediction
Yes, grasp affordance prediction is included as one of the auxiliary supervision signals mentioned above.

## 3) Architecture
The abstract doesn't provide specific architectural details. It only mentions that the approach uses "multi-view RGB observations, depth cues, and short temporal history" as inputs, with auxiliary decoders reconstructing intermediate signals from "shared visual-language features."

## 4) Main Results
The model shows "consistent improvements across picking, placing, opening, and closing operations, substantially outperforming direct imitation learning" on home rearrangement tasks. The framework addresses control of a "13-dimensional action space involving coordinated base motion, arm articulation, and gripper actuation."

## 5) End-to-End Training
The abstract indicates the auxiliary objectives provide "dense supervision that encourages the backbone to develop spatially grounded, manipulation-aware latent representations," suggesting joint training. However, explicit confirmation of end-to-end training methodology is not detailed in the provided abstract.

**Note:** Full methodological details would require reviewing the complete paper PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d099992-66d7-4267-9630-558af1b3490a",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "cb4982d4-1bf1-4037-bf6a-47fdca548ba2",
  "toolUseResult": {
    "bytes": 47985,
    "code": 200,
    "codeText": "OK",
    "result": "# SG-VLA Paper Summary\n\nBased on the arXiv abstract provided, here are the key details:\n\n## 1) Auxiliary Tasks\nThe paper co-trains auxiliary decoders that reconstruct: \"global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks.\"\n\n## 2) Affordance Prediction\nYes, grasp affordance prediction is included as one of the auxiliary supervision signals mentioned above.\n\n## 3) Architecture\nThe abstract doesn't provide specific architectural details. It only mentions that the approach uses \"multi-view RGB observations, depth cues, and short temporal history\" as inputs, with auxiliary decoders reconstructing intermediate signals from \"shared visual-language features.\"\n\n## 4) Main Results\nThe model shows \"consistent improvements across picking, placing, opening, and closing operations, substantially outperforming direct imitation learning\" on home rearrangement tasks. The framework addresses control of a \"13-dimensional action space involving coordinated base motion, arm articulation, and gripper actuation.\"\n\n## 5) End-to-End Training\nThe abstract indicates the auxiliary objectives provide \"dense supervision that encourages the backbone to develop spatially grounded, manipulation-aware latent representations,\" suggesting joint training. However, explicit confirmation of end-to-end training methodology is not detailed in the provided abstract.\n\n**Note:** Full methodological details would require reviewing the complete paper PDF.",
    "durationMs": 5039,
    "url": "https://arxiv.org/abs/2603.22760"
  },
  "sourceToolAssistantUUID": "8d099992-66d7-4267-9630-558af1b3490a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-18T19:13:50.086Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LMHEJjWsgsxybJ3RrTV6Nv`</summary>

```json
{
  "query": "affordance pseudo-label auxiliary loss VLA intermediate representation robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb4982d4-1bf1-4037-bf6a-47fdca548ba2",
  "isSidechain": false,
  "requestId": "req_011CbAZrcurdyP8GuCkKYySG",
  "type": "assistant",
  "uuid": "76c35f10-b67e-416c-ae0e-c10c3dcf2543",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VW8qLrGyaUdqQ7eD1H7qSk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 510,
      "cache_read_input_tokens": 36941,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 510,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 36941,
          "cache_creation_input_tokens": 510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 510
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

_source line 33 · 2026-05-18T19:13:57.841Z_

<details><summary>↩ Tool result · `toolu_01LMHEJjWsgsxybJ3RrTV6Nv`</summary>

```text
Web search results for query: "affordance pseudo-label auxiliary loss VLA intermediate representation robustness 2025 2026"

Links: [{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance","url":"https://arxiv.org/html/2507.22424v1"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"}]

I found several highly relevant research papers on this topic. Here are the search results:

1. **RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation** - This work explores how intermediate policy representations can facilitate generalization by providing guidance on how to perform manipulation tasks. RT-Affordance is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation.

2. **Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation** - This method achieves an average improvement of 23.5% across different VLA backbones under out-of-distribution scenarios on real-world robotic platforms, validating its effectiveness in enhancing VLA robustness to distribution shifts.

3. **CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance** (ICCV 2025) - The work introduces a novel vision-language co-injection module that integrates affordance knowledge into the policy network, allowing the robot to leverage essential contextual information during action inference, resulting in improved precision and robustness.

4. **Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges** - Recent VLA models have converged toward three major architectural paradigms that balance efficiency, modularity, and robustness: early fusion models, dual-system architectures, and self-correcting frameworks.

5. **Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance** - This work discusses recent advances in VLA acceleration and optimization techniques.

These papers represent cutting-edge research from 2025-2026 on using affordances as intermediate representations in VLA models to improve robustness and generalization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76c35f10-b67e-416c-ae0e-c10c3dcf2543",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "3067a109-8a77-4924-95dc-f0c214d2f1de",
  "toolUseResult": {
    "query": "affordance pseudo-label auxiliary loss VLA intermediate representation robustness 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QftS78ezCoMvWFsp6jHRJA",
        "content": [
          {
            "title": "RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation",
            "url": "https://arxiv.org/pdf/2411.02704"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          },
          {
            "title": "Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance",
            "url": "https://arxiv.org/html/2507.22424v1"
          },
          {
            "title": "ICCV 2025 Open Access Repository",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"
          },
          {
            "title": "Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v2"
          }
        ]
      },
      "I found several highly relevant research papers on this topic. Here are the search results:\n\n1. **RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation** - This work explores how intermediate policy representations can facilitate generalization by providing guidance on how to perform manipulation tasks. RT-Affordance is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation.\n\n2. **Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation** - This method achieves an average improvement of 23.5% across different VLA backbones under out-of-distribution scenarios on real-world robotic platforms, validating its effectiveness in enhancing VLA robustness to distribution shifts.\n\n3. **CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance** (ICCV 2025) - The work introduces a novel vision-language co-injection module that integrates affordance knowledge into the policy network, allowing the robot to leverage essential contextual information during action inference, resulting in improved precision and robustness.\n\n4. **Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges** - Recent VLA models have converged toward three major architectural paradigms that balance efficiency, modularity, and robustness: early fusion models, dual-system architectures, and self-correcting frameworks.\n\n5. **Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance** - This work discusses recent advances in VLA acceleration and optimization techniques.\n\nThese papers represent cutting-edge research from 2025-2026 on using affordances as intermediate representations in VLA models to improve robustness and generalization."
    ],
    "durationSeconds": 7.752129487999992
  },
  "sourceToolAssistantUUID": "76c35f10-b67e-416c-ae0e-c10c3dcf2543",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3067a109-8a77-4924-95dc-f0c214d2f1de",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "AffordVLA: Open-vocabulary affordance distillation into VLA for robust manipulation",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Tool call

_source line 36 · 2026-05-18T19:14:00.415Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VzvYMDhnVZZ9MnjRfQq7qa`</summary>

```json
{
  "query": "\"affordance\" \"auxiliary\" \"VLA\" \"training\" site:arxiv.org 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3067a109-8a77-4924-95dc-f0c214d2f1de",
  "isSidechain": false,
  "requestId": "req_011CbAZsRNr5V67vYdX4CaX6",
  "type": "assistant",
  "uuid": "7628041a-05de-498c-8832-1f12bdaa8620",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Law28JmmKrvVcyWDVEiugi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 821,
      "cache_read_input_tokens": 37451,
      "output_tokens": 74,
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
          "output_tokens": 74,
          "cache_read_input_tokens": 37451,
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

_source line 37 · 2026-05-18T19:14:08.210Z_

<details><summary>↩ Tool result · `toolu_01VzvYMDhnVZZ9MnjRfQq7qa`</summary>

```text
Web search results for query: ""affordance" "auxiliary" "VLA" "training" site:arxiv.org 2026"

Links: [{"title":"[2603.22760] SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/abs/2603.22760"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/pdf/2603.22760"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/html/2603.22760v1"},{"title":"Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance","url":"https://arxiv.org/pdf/2603.25661"},{"title":"VLA Model Post-Training via Action-Chunked PPO and Self Behavior Cloning","url":"https://arxiv.org/pdf/2509.25718"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"ST4VLA: Spatially Guided Training for Vision-Language-Action Model","url":"https://arxiv.org/html/2602.10109"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"}]

I found several relevant research papers on arxiv.org from 2026 that discuss affordance, auxiliary training, and VLA (Vision-Language-Action) models:

## Key Results:

1. **SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation** (March 24, 2026)
   - Co-trains auxiliary decoders that reconstruct interpretable intermediate signals including global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks from shared visual-language features.

2. **VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models** (March 24, 2026)
   - Formulates visual sequence compression as a dynamic affordance extraction process.

3. **ST4VLA: Spatially Guided Training for Vision-Language-Action Model** (February 10, 2026)
   - The VLM planner is aligned with a broad range of spatial grounding data, covering tasks such as object detection, affordance recognition, and visual trajectory planning.

4. **Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance**
   - Decouples the two objectives of auxiliary task training within the parameter space, namely, enhancing general capabilities and fitting task-specific action distributions.

5. **CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance** (December 2025)
   - Focuses on infusing affordance knowledge into policy learning for robots.

These papers represent recent advances in VLA model training that incorporate affordance learning through auxiliary training objectives.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7628041a-05de-498c-8832-1f12bdaa8620",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "499fca18-36ea-44fb-ab5d-087f39500919",
  "toolUseResult": {
    "query": "\"affordance\" \"auxiliary\" \"VLA\" \"training\" site:arxiv.org 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016BAzdZP2Tn1axQRE174Ms4",
        "content": [
          {
            "title": "[2603.22760] SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/abs/2603.22760"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/pdf/2603.22760"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/html/2603.22760v1"
          },
          {
            "title": "Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance",
            "url": "https://arxiv.org/pdf/2603.25661"
          },
          {
            "title": "VLA Model Post-Training via Action-Chunked PPO and Self Behavior Cloning",
            "url": "https://arxiv.org/pdf/2509.25718"
          },
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance",
            "url": "https://arxiv.org/pdf/2412.20451"
          },
          {
            "title": "ST4VLA: Spatially Guided Training for Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2602.10109"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          }
        ]
      },
      "I found several relevant research papers on arxiv.org from 2026 that discuss affordance, auxiliary training, and VLA (Vision-Language-Action) models:\n\n## Key Results:\n\n1. **SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation** (March 24, 2026)\n   - Co-trains auxiliary decoders that reconstruct interpretable intermediate signals including global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks from shared visual-language features.\n\n2. **VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models** (March 24, 2026)\n   - Formulates visual sequence compression as a dynamic affordance extraction process.\n\n3. **ST4VLA: Spatially Guided Training for Vision-Language-Action Model** (February 10, 2026)\n   - The VLM planner is aligned with a broad range of spatial grounding data, covering tasks such as object detection, affordance recognition, and visual trajectory planning.\n\n4. **Fast-dVLA: Accelerating Discrete Diffusion VLA to Real-Time Performance**\n   - Decouples the two objectives of auxiliary task training within the parameter space, namely, enhancing general capabilities and fitting task-specific action distributions.\n\n5. **CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance** (December 2025)\n   - Focuses on infusing affordance knowledge into policy learning for robots.\n\nThese papers represent recent advances in VLA model training that incorporate affordance learning through auxiliary training objectives."
    ],
    "durationSeconds": 7.791188125000001
  },
  "sourceToolAssistantUUID": "7628041a-05de-498c-8832-1f12bdaa8620",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-18T19:14:14.042Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FRHhm85x79ASTRRtZ4P3GY`</summary>

```json
{
  "query": "VLA-GSE LIBERO-Plus robustness PEFT arXiv 2605.06175"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "499fca18-36ea-44fb-ab5d-087f39500919",
  "isSidechain": false,
  "requestId": "req_011CbAZtBkaP7D1pjcrS4na4",
  "type": "assistant",
  "uuid": "8235d559-9c87-4989-96ed-635438738a18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L32hmJDHitpSzQY7wDTaNm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 38272,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 38272,
          "cache_creation_input_tokens": 940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 940
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

_source line 39 · 2026-05-18T19:14:21.934Z_

<details><summary>↩ Tool result · `toolu_01FRHhm85x79ASTRRtZ4P3GY`</summary>

```text
Web search results for query: "VLA-GSE LIBERO-Plus robustness PEFT arXiv 2605.06175"

Links: [{"title":"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts","url":"https://arxiv.org/html/2605.06175v1"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"}]

Based on the search results, I found relevant information about the paper and research:

## VLA-GSE: Parameter-Efficient Fine-Tuning for Vision-Language-Action Models

VLA-GSE (Generalized and Specialized Experts) is a parameter-efficient VLA fine-tuning framework designed to strengthen adaptation without sacrificing knowledge retention, updating only 2.51% of full model parameters.

### Performance on LIBERO-Plus

On LIBERO-Plus, VLA-GSE achieves 81.2% average zero-shot success, exceeding full fine-tuning by 6.3% and the strongest PEFT baseline by 4.4%, with strong robustness under diverse perturbations. At the suite level, it attains 90.3% on Spatial and 86.2% on Object, and remains stable on the more challenging Goal and Long suites with 74.2% and 74.1%, respectively.

### Robustness and Comparison to Other PEFT Methods

VLA-GSE is significantly more robust and effective for VLA fine-tuning than conventional LoRA-style, SVD-based, or LoRA-MoE variants. Additionally, on multimodal understanding benchmarks, VLA-GSE preserves pre-trained VLM capability comparably to LoRA and outperforms both full fine-tuning and co-trained VLA baselines.

The paper addresses the challenge of achieving sufficient expressiveness for precise robot-control adaptation while retaining the knowledge-preservation advantages of parameter-efficient fine-tuning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8235d559-9c87-4989-96ed-635438738a18",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "58039c83-bd47-498e-bdcb-8947648f26b5",
  "toolUseResult": {
    "query": "VLA-GSE LIBERO-Plus robustness PEFT arXiv 2605.06175",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UqNia6BEDBZ2yJd6C7wyLd",
        "content": [
          {
            "title": "VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts",
            "url": "https://arxiv.org/html/2605.06175v1"
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
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          }
        ]
      },
      "Based on the search results, I found relevant information about the paper and research:\n\n## VLA-GSE: Parameter-Efficient Fine-Tuning for Vision-Language-Action Models\n\nVLA-GSE (Generalized and Specialized Experts) is a parameter-efficient VLA fine-tuning framework designed to strengthen adaptation without sacrificing knowledge retention, updating only 2.51% of full model parameters.\n\n### Performance on LIBERO-Plus\n\nOn LIBERO-Plus, VLA-GSE achieves 81.2% average zero-shot success, exceeding full fine-tuning by 6.3% and the strongest PEFT baseline by 4.4%, with strong robustness under diverse perturbations. At the suite level, it attains 90.3% on Spatial and 86.2% on Object, and remains stable on the more challenging Goal and Long suites with 74.2% and 74.1%, respectively.\n\n### Robustness and Comparison to Other PEFT Methods\n\nVLA-GSE is significantly more robust and effective for VLA fine-tuning than conventional LoRA-style, SVD-based, or LoRA-MoE variants. Additionally, on multimodal understanding benchmarks, VLA-GSE preserves pre-trained VLM capability comparably to LoRA and outperforms both full fine-tuning and co-trained VLA baselines.\n\nThe paper addresses the challenge of achieving sufficient expressiveness for precise robot-control adaptation while retaining the knowledge-preservation advantages of parameter-efficient fine-tuning approaches."
    ],
    "durationSeconds": 7.88700134799999
  },
  "sourceToolAssistantUUID": "8235d559-9c87-4989-96ed-635438738a18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-18T19:14:25.071Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dfm4cSuLgbyxaK3QA59uwM`</summary>

```json
{
  "query": "A0 affordance-aware hierarchical VLA manipulation 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58039c83-bd47-498e-bdcb-8947648f26b5",
  "isSidechain": false,
  "requestId": "req_011CbAZuCQoApy4cdqLfEZx5",
  "type": "assistant",
  "uuid": "8911c1ec-b2ad-4876-8be6-16fe10c16334",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Wwey1HuXaEaxNsrVecFch",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 39212,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 39212,
          "cache_creation_input_tokens": 849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 849
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

_source line 41 · 2026-05-18T19:14:35.150Z_

<details><summary>↩ Tool result · `toolu_01Dfm4cSuLgbyxaK3QA59uwM`</summary>

```text
Web search results for query: "A0 affordance-aware hierarchical VLA manipulation 2026 arXiv"

Links: [{"title":"A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation | Request PDF","url":"https://www.researchgate.net/publication/390892539_A0_An_Affordance-Aware_Hierarchical_Model_for_General_Robotic_Manipulation"},{"title":"dblp: A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation.","url":"https://dblp.org/rec/journals/corr/abs-2504-12636.html"},{"title":"A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation","url":"https://arxiv.org/pdf/2504.12636"},{"title":"[Literature Review] A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation","url":"https://www.themoonlight.io/en/review/a0-an-affordance-aware-hierarchical-model-for-general-robotic-manipulation"},{"title":"A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_A0_An_Affordance-Aware_Hierarchical_Model_for_General_Robotic_Manipulation_ICCV_2025_paper.pdf"},{"title":"A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulatione","url":"https://a-embodied.github.io/A0/"}]

Based on the search results, I found information about A0, an affordance-aware hierarchical model for robotic manipulation:

## Overview

A0 is a novel Affordance-Aware Hierarchical Model designed for general robotic manipulation, addressing limitations in existing methods related to understanding spatial affordances.

## Architecture

A0 is a hierarchical affordance-aware diffusion model that decomposes manipulation tasks into high-level spatial affordance understanding and low-level action execution. A0 leverages the Embodiment-Agnostic Affordance Representation, which captures object-centric spatial affordances by predicting contact point and post-contact trajectories.

## Training and Data

A0 is pre-trained on 1 million contact-point localization data points, followed by supervised fine-tuning on an annotated spatial trajectory dataset.

## Performance

The method achieves an average success rate of 62.50% on Franka and 53.75% on Kinova, outperforming the strongest baselines on both platforms. The model was evaluated on multiple robotic systems (Franka, Kinova, Realman, and Dobot), demonstrating superior performance in complex tasks such as wiping a whiteboard, opening a drawer, and stacking objects.

## Publication

The paper was published on arXiv as abs/2504.12636 in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8911c1ec-b2ad-4876-8be6-16fe10c16334",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "cab2a4f3-0276-4266-b21c-0612c49502dd",
  "toolUseResult": {
    "query": "A0 affordance-aware hierarchical VLA manipulation 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Do198cMWGn7qBESoq54Sse",
        "content": [
          {
            "title": "A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation | Request PDF",
            "url": "https://www.researchgate.net/publication/390892539_A0_An_Affordance-Aware_Hierarchical_Model_for_General_Robotic_Manipulation"
          },
          {
            "title": "dblp: A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation.",
            "url": "https://dblp.org/rec/journals/corr/abs-2504-12636.html"
          },
          {
            "title": "A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2504.12636"
          },
          {
            "title": "[Literature Review] A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation",
            "url": "https://www.themoonlight.io/en/review/a0-an-affordance-aware-hierarchical-model-for-general-robotic-manipulation"
          },
          {
            "title": "A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulation",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_A0_An_Affordance-Aware_Hierarchical_Model_for_General_Robotic_Manipulation_ICCV_2025_paper.pdf"
          },
          {
            "title": "A0: An Affordance-Aware Hierarchical Model for General Robotic Manipulatione",
            "url": "https://a-embodied.github.io/A0/"
          }
        ]
      },
      "Based on the search results, I found information about A0, an affordance-aware hierarchical model for robotic manipulation:\n\n## Overview\n\nA0 is a novel Affordance-Aware Hierarchical Model designed for general robotic manipulation, addressing limitations in existing methods related to understanding spatial affordances.\n\n## Architecture\n\nA0 is a hierarchical affordance-aware diffusion model that decomposes manipulation tasks into high-level spatial affordance understanding and low-level action execution. A0 leverages the Embodiment-Agnostic Affordance Representation, which captures object-centric spatial affordances by predicting contact point and post-contact trajectories.\n\n## Training and Data\n\nA0 is pre-trained on 1 million contact-point localization data points, followed by supervised fine-tuning on an annotated spatial trajectory dataset.\n\n## Performance\n\nThe method achieves an average success rate of 62.50% on Franka and 53.75% on Kinova, outperforming the strongest baselines on both platforms. The model was evaluated on multiple robotic systems (Franka, Kinova, Realman, and Dobot), demonstrating superior performance in complex tasks such as wiping a whiteboard, opening a drawer, and stacking objects.\n\n## Publication\n\nThe paper was published on arXiv as abs/2504.12636 in 2025."
    ],
    "durationSeconds": 10.075111011
  },
  "sourceToolAssistantUUID": "8911c1ec-b2ad-4876-8be6-16fe10c16334",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-18T19:14:38.599Z_

Important find — A0 is an affordance-aware hierarchical model at ICCV 2025. Let me now check if there are more recent works specifically on affordance + robustness for VLAs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cab2a4f3-0276-4266-b21c-0612c49502dd",
  "isSidechain": false,
  "requestId": "req_011CbAZvAvXfKDbKGA4wpSiL",
  "type": "assistant",
  "uuid": "efc48e70-6028-4949-bc8d-d53a72ce85b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YLcLRT4DgGwax8ah8pJrm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 40061,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 40061,
          "cache_creation_input_tokens": 827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 827
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

_source line 43 · 2026-05-18T19:14:38.927Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014itUznCMwAGK6nKuwx9ftZ`</summary>

```json
{
  "query": "affordance robustness distribution shift VLA manipulation 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efc48e70-6028-4949-bc8d-d53a72ce85b7",
  "isSidechain": false,
  "requestId": "req_011CbAZvAvXfKDbKGA4wpSiL",
  "type": "assistant",
  "uuid": "5c8de4fb-4e70-4682-8e40-038f92af1ff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YLcLRT4DgGwax8ah8pJrm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 40061,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 40061,
          "cache_creation_input_tokens": 827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 827
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

_source line 44 · 2026-05-18T19:14:45.802Z_

<details><summary>↩ Tool result · `toolu_014itUznCMwAGK6nKuwx9ftZ`</summary>

```text
Web search results for query: "affordance robustness distribution shift VLA manipulation 2026 arXiv"

Links: [{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/html/2512.07472v1"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in","url":"https://www.arxiv.org/pdf/2512.07472"},{"title":"[2512.07472] Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://www.arxiv.org/abs/2512.07472"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study","url":"https://arxiv.org/html/2505.19789v4"},{"title":"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/pdf/2512.01715"}]

I found several relevant papers from arXiv on this topic. Here are the key results:

## Primary Result: Affordance Field Intervention (AFI)

Vision-Language-Action (VLA) models remain brittle under distribution shifts, with a failure mode called the "Memory Trap" where VLAs often reproduce memorized trajectories instead of adapting to updated scenes when test scenarios change.

The paper introduces Affordance Field Intervention (AFI), a lightweight hybrid framework that uses 3D Spatial Affordance Fields as an on-demand plugin to guide VLA behavior, detecting memory traps through proprioception, repositioning the robot to recent high-affordance regions, and proposing affordance-driven waypoints.

The method achieves an average improvement of 23.5% across different VLA backbones under out-of-distribution scenarios on real-world robotic platforms, and 20.2% on the LIBERO-Pro benchmark, validating its effectiveness in enhancing VLA robustness to distribution shifts.

## Related Work: DiG-Flow

Another recent paper addresses similar challenges: VLA models show substantial performance degradation under modest distribution shifts such as lighting changes, texture variations, or camera angle perturbations, with this problem particularly pronounced on complex tasks where sequential decisions compound.

Both papers from December 2025/January 2026 address critical robustness challenges for Vision-Language-Action models in robotic manipulation under distribution shifts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c8de4fb-4e70-4682-8e40-038f92af1ff9",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "03b0bdc6-f264-49d3-ace2-dbb17ca2d031",
  "toolUseResult": {
    "query": "affordance robustness distribution shift VLA manipulation 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_017fjf32j54aVyQURULXmjzA",
        "content": [
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/html/2512.07472v1"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in",
            "url": "https://www.arxiv.org/pdf/2512.07472"
          },
          {
            "title": "[2512.07472] Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://www.arxiv.org/abs/2512.07472"
          },
          {
            "title": "What Can RL Bring to VLA Generalization? An Empirical Study",
            "url": "https://arxiv.org/html/2505.19789v4"
          },
          {
            "title": "DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://arxiv.org/pdf/2512.01715"
          }
        ]
      },
      "I found several relevant papers from arXiv on this topic. Here are the key results:\n\n## Primary Result: Affordance Field Intervention (AFI)\n\nVision-Language-Action (VLA) models remain brittle under distribution shifts, with a failure mode called the \"Memory Trap\" where VLAs often reproduce memorized trajectories instead of adapting to updated scenes when test scenarios change.\n\nThe paper introduces Affordance Field Intervention (AFI), a lightweight hybrid framework that uses 3D Spatial Affordance Fields as an on-demand plugin to guide VLA behavior, detecting memory traps through proprioception, repositioning the robot to recent high-affordance regions, and proposing affordance-driven waypoints.\n\nThe method achieves an average improvement of 23.5% across different VLA backbones under out-of-distribution scenarios on real-world robotic platforms, and 20.2% on the LIBERO-Pro benchmark, validating its effectiveness in enhancing VLA robustness to distribution shifts.\n\n## Related Work: DiG-Flow\n\nAnother recent paper addresses similar challenges: VLA models show substantial performance degradation under modest distribution shifts such as lighting changes, texture variations, or camera angle perturbations, with this problem particularly pronounced on complex tasks where sequential decisions compound.\n\nBoth papers from December 2025/January 2026 address critical robustness challenges for Vision-Language-Action models in robotic manipulation under distribution shifts."
    ],
    "durationSeconds": 6.869954805000016
  },
  "sourceToolAssistantUUID": "5c8de4fb-4e70-4682-8e40-038f92af1ff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T19:14:48.562Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MWa3WwjYFh8NdFpCed2y5n`</summary>

```json
{
  "query": "CoRL 2026 submission deadline date call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03b0bdc6-f264-49d3-ace2-dbb17ca2d031",
  "isSidechain": false,
  "requestId": "req_011CbAZvxRyYpc17NmxSKCQH",
  "type": "assistant",
  "uuid": "e8ed4749-a800-4dce-85b9-da55990e4cd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQMQAnJwcnT9m4G1GSZoT9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 771,
      "cache_read_input_tokens": 40888,
      "output_tokens": 63,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 63,
          "cache_read_input_tokens": 40888,
          "cache_creation_input_tokens": 771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 771
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

_source line 46 · 2026-05-18T19:14:53.476Z_

<details><summary>↩ Tool result · `toolu_01MWa3WwjYFh8NdFpCed2y5n`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline date call for papers"

Links: [{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf?lang=en"},{"title":"Refactor conference data · huggingface/ai-deadlines at f3cc2d7","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"},{"title":"AI Conference Deadlines","url":"https://nunoduarte.github.io/deadlines/"}]

Based on the search results, here are the key submission deadlines and information for CoRL 2026:

**Submission Deadlines:**
- Abstract submission deadline: May 26, 2026 11:59 UTC
- Paper submission deadline: May 29, 2026

**Conference Details:**
- The conference will be held November 9-12, 2026 in Austin, Texas, US
- Papers may be submitted through OpenReview via the link here (https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference)

**Submission Requirements:**
- Page limit is 8 pages for the main paper
- Acknowledgments, References, and Appendix (optional) will not count towards the page limit

**Important Note:**
The deadlines are final, and they cannot make any accommodations for missing the abstract deadline or paper deadline


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8ed4749-a800-4dce-85b9-da55990e4cd5",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "2290b740-2cb5-46f8-9d6a-6cd0ff17fe5b",
  "toolUseResult": {
    "query": "CoRL 2026 submission deadline date call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_017MTZxCYsbf96RxyAAcVe9y",
        "content": [
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "CoRL 2026",
            "url": "https://www.corl.org/"
          },
          {
            "title": "Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"
          },
          {
            "title": "CoRL 2026 - Instruction for Authors",
            "url": "https://www.corl.org/contributions/instruction-for-authors"
          },
          {
            "title": "CoRL LaTeX Template | Robot Learning Conference Format | Underleaf",
            "url": "https://www.underleaf.ai/templates/corl"
          },
          {
            "title": "CoRL 2026 - Annoucements",
            "url": "https://www.corl.org/annoucements"
          },
          {
            "title": "Robot Learning Foundation",
            "url": "https://www.robot-learning.org/"
          },
          {
            "title": "Conference on Robot Learning (@corl_conf) / Posts / X",
            "url": "https://x.com/corl_conf?lang=en"
          },
          {
            "title": "Refactor conference data · huggingface/ai-deadlines at f3cc2d7",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/f3cc2d74f8283ae00d3005ff7cca51dd26540377"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://nunoduarte.github.io/deadlines/"
          }
        ]
      },
      "Based on the search results, here are the key submission deadlines and information for CoRL 2026:\n\n**Submission Deadlines:**\n- Abstract submission deadline: May 26, 2026 11:59 UTC\n- Paper submission deadline: May 29, 2026\n\n**Conference Details:**\n- The conference will be held November 9-12, 2026 in Austin, Texas, US\n- Papers may be submitted through OpenReview via the link here (https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference)\n\n**Submission Requirements:**\n- Page limit is 8 pages for the main paper\n- Acknowledgments, References, and Appendix (optional) will not count towards the page limit\n\n**Important Note:**\nThe deadlines are final, and they cannot make any accommodations for missing the abstract deadline or paper deadline"
    ],
    "durationSeconds": 4.910570493999985
  },
  "sourceToolAssistantUUID": "e8ed4749-a800-4dce-85b9-da55990e4cd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "2290b740-2cb5-46f8-9d6a-6cd0ff17fe5b",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "AffordVLA: Open-vocabulary affordance distillation into VLA for robust manipulation",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Assistant

_source line 49 · 2026-05-18T19:14:58.169Z_

Critical: CoRL 2026 deadline is May 29, 2026 — 11 days away. The proposal says "CoRL 2026 IMPOSSIBLE" with May 28 deadline. The actual deadline is May 29, but the point stands — this is impossibly close. Let me now check ICRA 2027 and ICLR 2027 deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2290b740-2cb5-46f8-9d6a-6cd0ff17fe5b",
  "isSidechain": false,
  "requestId": "req_011CbAZwXEgZXvaneUTewTxR",
  "type": "assistant",
  "uuid": "2ecf51f2-1615-4995-8bc1-03709ae691d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AN9u8F7DXNoU58E4thY2MG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 41659,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 41659,
          "cache_creation_input_tokens": 710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 710
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

_source line 50 · 2026-05-18T19:14:58.473Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GkrJRXEDwP1niJSPP9z8Xs`</summary>

```json
{
  "query": "ICRA 2027 submission deadline call for papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ecf51f2-1615-4995-8bc1-03709ae691d0",
  "isSidechain": false,
  "requestId": "req_011CbAZwXEgZXvaneUTewTxR",
  "type": "assistant",
  "uuid": "9070f98f-8a42-4431-bf08-f67cb0a53c71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AN9u8F7DXNoU58E4thY2MG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 41659,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 710,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 151,
          "cache_read_input_tokens": 41659,
          "cache_creation_input_tokens": 710,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 710
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

_source line 51 · 2026-05-18T19:15:02.654Z_

<details><summary>↩ Tool result · `toolu_01GkrJRXEDwP1niJSPP9z8Xs`</summary>

```text
Web search results for query: "ICRA 2027 submission deadline call for papers"

Links: [{"title":"IEEE ICRA 2027 | Calls for Papers and Posters","url":"https://2027.ieee-icra.org/contribute/"},{"title":"ICRA - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"},{"title":"2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"},{"title":"ICRA 2026 Papers - Submission closed - IEEE ICRA 2026","url":"https://2026.ieee-icra.org/contribute/call-for-icra-2026-papers-now-accepting-submissions/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Start Page of the Conference Management System","url":"https://ras.papercept.net/conferences/scripts/start.pl"},{"title":"Paper submission","url":"https://www.icrca.org/sub.html"},{"title":"AI Conference Deadlines","url":"https://nunoduarte.github.io/deadlines/"},{"title":"ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1454"},{"title":"IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com","url":"https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"}]

Based on the web search results, here's what I found about ICRA 2027:

IEEE ICRA 2027 is held in Seoul, South Korea, from May 24-28, 2027.

However, the search results do not contain specific information about the submission deadline or current call for papers for ICRA 2027. The most detailed information found was related to ICRA 2026, which has already passed its submission deadline. 

To find the official ICRA 2027 submission deadline and call for papers, I recommend visiting the official ICRA 2027 website at 2027.ieee-icra.org or checking the IEEE Robotics and Automation Society's official conference pages, as these would have the most up-to-date submission information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9070f98f-8a42-4431-bf08-f67cb0a53c71",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "44521163-9dea-4bbd-8eab-dfb07cb60511",
  "toolUseResult": {
    "query": "ICRA 2027 submission deadline call for papers",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q5qjc86sRM8y9xyJJrNcsX",
        "content": [
          {
            "title": "IEEE ICRA 2027 | Calls for Papers and Posters",
            "url": "https://2027.ieee-icra.org/contribute/"
          },
          {
            "title": "ICRA - IEEE Robotics and Automation Society Website",
            "url": "https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"
          },
          {
            "title": "2027 IEEE International Conference on Robotics and Automation ICRA",
            "url": "https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"
          },
          {
            "title": "ICRA 2026 Papers - Submission closed - IEEE ICRA 2026",
            "url": "https://2026.ieee-icra.org/contribute/call-for-icra-2026-papers-now-accepting-submissions/"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "Start Page of the Conference Management System",
            "url": "https://ras.papercept.net/conferences/scripts/start.pl"
          },
          {
            "title": "Paper submission",
            "url": "https://www.icrca.org/sub.html"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://nunoduarte.github.io/deadlines/"
          },
          {
            "title": "ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=1454"
          },
          {
            "title": "IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com",
            "url": "https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"
          }
        ]
      },
      "Based on the web search results, here's what I found about ICRA 2027:\n\nIEEE ICRA 2027 is held in Seoul, South Korea, from May 24-28, 2027.\n\nHowever, the search results do not contain specific information about the submission deadline or current call for papers for ICRA 2027. The most detailed information found was related to ICRA 2026, which has already passed its submission deadline. \n\nTo find the official ICRA 2027 submission deadline and call for papers, I recommend visiting the official ICRA 2027 website at 2027.ieee-icra.org or checking the IEEE Robotics and Automation Society's official conference pages, as these would have the most up-to-date submission information."
    ],
    "durationSeconds": 4.178322409999994
  },
  "sourceToolAssistantUUID": "9070f98f-8a42-4431-bf08-f67cb0a53c71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 52 · 2026-05-18T19:15:02.657Z_

```json
{
  "parentUuid": "44521163-9dea-4bbd-8eab-dfb07cb60511",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "27bb65cc-d493-4152-ba89-72ec5c0b83a5",
  "timestamp": "2026-05-18T19:15:02.657Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 53 · 2026-05-18T19:15:05.913Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NJFGePYKPajT98Y95XYiQy`</summary>

```json
{
  "url": "https://2027.ieee-icra.org/contribute/",
  "prompt": "What is the paper submission deadline for ICRA 2027? Extract all key dates including abstract deadline, full paper deadline, notification date, and camera ready date."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27bb65cc-d493-4152-ba89-72ec5c0b83a5",
  "isSidechain": false,
  "requestId": "req_011CbAZxCW5zowCsLJP1A3mX",
  "type": "assistant",
  "uuid": "17e8214e-92f9-4a26-87b1-845f9ce9d63c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BU8j96YYT2YzNRwrmhYc4J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 42369,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 42369,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 913
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

_source line 54 · 2026-05-18T19:15:08.950Z_

<details><summary>↩ Tool result · `toolu_01NJFGePYKPajT98Y95XYiQy`</summary>

```text
# ICRA 2027 Paper Submission Deadlines

Based on the provided web page content, **specific submission deadlines are not available**. 

The page states: "Detailed schedules and further information will be updated soon." It directs readers to check the Media Room and calendar for deadline information, but these specific dates are not included in the current content.

To find the paper submission deadlines, abstract deadline, full paper deadline, notification date, and camera ready date, you would need to:

1. Visit the [Media Room](https://2027.ieee-icra.org/media/)
2. Check the [calendar](https://2027.ieee-icra.org/calendar/)
3. Contact the organizing committee through the [contact page](https://2027.ieee-icra.org/about/contact/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "17e8214e-92f9-4a26-87b1-845f9ce9d63c",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "5b2be75b-1736-46b1-824f-070e4cac4662",
  "toolUseResult": {
    "bytes": 144521,
    "code": 200,
    "codeText": "OK",
    "result": "# ICRA 2027 Paper Submission Deadlines\n\nBased on the provided web page content, **specific submission deadlines are not available**. \n\nThe page states: \"Detailed schedules and further information will be updated soon.\" It directs readers to check the Media Room and calendar for deadline information, but these specific dates are not included in the current content.\n\nTo find the paper submission deadlines, abstract deadline, full paper deadline, notification date, and camera ready date, you would need to:\n\n1. Visit the [Media Room](https://2027.ieee-icra.org/media/)\n2. Check the [calendar](https://2027.ieee-icra.org/calendar/)\n3. Contact the organizing committee through the [contact page](https://2027.ieee-icra.org/about/contact/)",
    "durationMs": 3032,
    "url": "https://2027.ieee-icra.org/contribute/"
  },
  "sourceToolAssistantUUID": "17e8214e-92f9-4a26-87b1-845f9ce9d63c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-18T19:15:11.482Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NyKyDo9xEgDdFjutHoCyQ4`</summary>

```json
{
  "query": "ICRA 2027 paper submission deadline September October 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b2be75b-1736-46b1-824f-070e4cac4662",
  "isSidechain": false,
  "requestId": "req_011CbAZxfSaSSwy6ZWYtqHbn",
  "type": "assistant",
  "uuid": "8a4f2526-cc76-4eea-8ea2-8e35dc6b96ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018vrp7safFxfBdy2qvf615p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 308,
      "cache_read_input_tokens": 43282,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 43282,
          "cache_creation_input_tokens": 308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 308
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

_source line 56 · 2026-05-18T19:15:25.235Z_

<details><summary>↩ Tool result · `toolu_01NyKyDo9xEgDdFjutHoCyQ4`</summary>

```text
Web search results for query: "ICRA 2027 paper submission deadline September October 2026"

Links: [{"title":"IEEE ICRA 2027 | Calls for Papers and Posters","url":"https://2027.ieee-icra.org/contribute/"},{"title":"2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"},{"title":"IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com","url":"https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"},{"title":"ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1454"},{"title":"ICRA 2026 Papers - Submission closed - IEEE ICRA 2026","url":"https://2026.ieee-icra.org/contribute/call-for-icra-2026-papers-now-accepting-submissions/"},{"title":"Position: Machine Learning Conferences Should Establish a \"Refutations and Critiques\" Track","url":"https://arxiv.org/pdf/2506.19882"},{"title":"ICRA - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"},{"title":"Use of machine learning for triage and transfer of ICU patients in the Covid-19 pandemic period: Scope Review","url":"https://www.medrxiv.org/content/10.1101/2023.02.08.23285446.full.pdf"}]

Let me search for more specific information about ICRA 2027 deadlines.

Links: [{"title":"2027 IEEE International Conference on Robotics ... - ICRA 2026","url":"https://2027.ieee-icra.org/"},{"title":"IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com","url":"https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Workshop on Field Robotics - ICRA 2026","url":"https://norlab-ulaval.github.io/icra_workshop_field_robotics/"},{"title":"IEEE ICRA 2026 | Calls for Papers and Posters","url":"https://2026.ieee-icra.org/contribute/"},{"title":"IEEE ICRA on X: \"Final Reminder: ICRA 2026 Paper Submission Deadline – 15 September 2025 (23:59 PST)! Submit your cutting-edge robotics research to the flagship IEEE Robotics &amp; Automation conference. Learn more about the submission process: https://t.co/lopnwGFNTd https://t.co/4FMfIL93Tl\" / X","url":"https://x.com/ieee_ras_icra/status/1966540573549973863"},{"title":"ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1454"},{"title":"2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"ICRA - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"}]

Let me search more specifically for ICRA 2027 paper submission deadlines.

Links: [{"title":"IEEE ICRA 2027 | Calls for Papers and Posters","url":"https://2027.ieee-icra.org/contribute/"},{"title":"2027 IEEE International Conference on Robotics and Automation ICRA","url":"https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"},{"title":"IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com","url":"https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"},{"title":"ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=1454"},{"title":"ICRA 2026 Papers - Submission closed - IEEE ICRA 2026","url":"https://2026.ieee-icra.org/contribute/call-for-icra-2026-papers-now-accepting-submissions/"},{"title":"Position: Machine Learning Conferences Should Establish a \"Refutations and Critiques\" Track","url":"https://arxiv.org/pdf/2506.19882"},{"title":"ICRA - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"},{"title":"Use of machine learning for triage and transfer of ICU patients in the Covid-19 pandemic period: Scope Review","url":"https://www.medrxiv.org/content/10.1101/2023.02.08.23285446.full.pdf"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"}]

Based on my search results, I found that the official ICRA 2027 conference website shows information about paper submission deadlines. However, the page appears to have cached or outdated information. The ICRA 2027 website currently shows submissions are due by 15 September 2024, but this is outdated information since we are currently in May 2026.

Based on the pattern from recent ICRA conferences, ICRA 2026 submissions were due by 15 September 2025, suggesting that ICRA typically follows a similar timeline each year with paper submission deadlines in mid-September.

For the most current and accurate ICRA 2027 paper submission deadline information, I recommend:

1. Visiting the official ICRA 2027 website directly at 2027.ieee-icra.org/contribute/
2. Checking the IEEE Robotics and Automation Society's conference page at ieee-ras.org

The conference itself is scheduled for May 24-28, 2027 in Seoul, South Korea, so you can expect the paper submission deadline to likely fall in September 2026 based on historical patterns, but you should verify the exact deadline on the official conference website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a4f2526-cc76-4eea-8ea2-8e35dc6b96ea",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "c48788a0-27de-4236-9c76-8070e79ff065",
  "toolUseResult": {
    "query": "ICRA 2027 paper submission deadline September October 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011yPYMJ68qwjaW6ETYnZdra",
        "content": [
          {
            "title": "IEEE ICRA 2027 | Calls for Papers and Posters",
            "url": "https://2027.ieee-icra.org/contribute/"
          },
          {
            "title": "2027 IEEE International Conference on Robotics and Automation ICRA",
            "url": "https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"
          },
          {
            "title": "IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com",
            "url": "https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"
          },
          {
            "title": "ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=1454"
          },
          {
            "title": "ICRA 2026 Papers - Submission closed - IEEE ICRA 2026",
            "url": "https://2026.ieee-icra.org/contribute/call-for-icra-2026-papers-now-accepting-submissions/"
          },
          {
            "title": "Position: Machine Learning Conferences Should Establish a \"Refutations and Critiques\" Track",
            "url": "https://arxiv.org/pdf/2506.19882"
          },
          {
            "title": "ICRA - IEEE Robotics and Automation Society Website",
            "url": "https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"
          },
          {
            "title": "Use of machine learning for triage and transfer of ICU patients in the Covid-19 pandemic period: Scope Review",
            "url": "https://www.medrxiv.org/content/10.1101/2023.02.08.23285446.full.pdf"
          }
        ]
      },
      "Let me search for more specific information about ICRA 2027 deadlines.",
      {
        "tool_use_id": "srvtoolu_01CGU9QJt2T23dqyfcbS2PLy",
        "content": [
          {
            "title": "2027 IEEE International Conference on Robotics ... - ICRA 2026",
            "url": "https://2027.ieee-icra.org/"
          },
          {
            "title": "IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com",
            "url": "https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "Workshop on Field Robotics - ICRA 2026",
            "url": "https://norlab-ulaval.github.io/icra_workshop_field_robotics/"
          },
          {
            "title": "IEEE ICRA 2026 | Calls for Papers and Posters",
            "url": "https://2026.ieee-icra.org/contribute/"
          },
          {
            "title": "IEEE ICRA on X: \"Final Reminder: ICRA 2026 Paper Submission Deadline – 15 September 2025 (23:59 PST)! Submit your cutting-edge robotics research to the flagship IEEE Robotics &amp; Automation conference. Learn more about the submission process: https://t.co/lopnwGFNTd https://t.co/4FMfIL93Tl\" / X",
            "url": "https://x.com/ieee_ras_icra/status/1966540573549973863"
          },
          {
            "title": "ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=1454"
          },
          {
            "title": "2027 IEEE International Conference on Robotics and Automation ICRA",
            "url": "https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "ICRA - IEEE Robotics and Automation Society Website",
            "url": "https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"
          }
        ]
      },
      "Let me search more specifically for ICRA 2027 paper submission deadlines.",
      {
        "tool_use_id": "srvtoolu_01GGAwJbNJ6ap1RwWNeHaDvf",
        "content": [
          {
            "title": "IEEE ICRA 2027 | Calls for Papers and Posters",
            "url": "https://2027.ieee-icra.org/contribute/"
          },
          {
            "title": "2027 IEEE International Conference on Robotics and Automation ICRA",
            "url": "https://www.aconf.org/conf_211853.2027_IEEE_International_Conference_on_Robotics_and_Automation.html"
          },
          {
            "title": "IEEE ICRA 2027 (Seoul) - International Conference on Robotics and Automation (ICRA) -- showsbee.com",
            "url": "https://www.showsbee.com/fairs/95745-IEEE-ICRA-2027.html"
          },
          {
            "title": "ICRA: International Conference on Robotics and Automation 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=1454"
          },
          {
            "title": "ICRA 2026 Papers - Submission closed - IEEE ICRA 2026",
            "url": "https://2026.ieee-icra.org/contribute/call-for-icra-2026-papers-now-accepting-submissions/"
          },
          {
            "title": "Position: Machine Learning Conferences Should Establish a \"Refutations and Critiques\" Track",
            "url": "https://arxiv.org/pdf/2506.19882"
          },
          {
            "title": "ICRA - IEEE Robotics and Automation Society Website",
            "url": "https://www.ieee-ras.org/conferences-workshops/fully-sponsored/icra/"
          },
          {
            "title": "Use of machine learning for triage and transfer of ICU patients in the Covid-19 pandemic period: Scope Review",
            "url": "https://www.medrxiv.org/content/10.1101/2023.02.08.23285446.full.pdf"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          }
        ]
      },
      "Based on my search results, I found that the official ICRA 2027 conference website shows information about paper submission deadlines. However, the page appears to have cached or outdated information. The ICRA 2027 website currently shows submissions are due by 15 September 2024, but this is outdated information since we are currently in May 2026.\n\nBased on the pattern from recent ICRA conferences, ICRA 2026 submissions were due by 15 September 2025, suggesting that ICRA typically follows a similar timeline each year with paper submission deadlines in mid-September.\n\nFor the most current and accurate ICRA 2027 paper submission deadline information, I recommend:\n\n1. Visiting the official ICRA 2027 website directly at 2027.ieee-icra.org/contribute/\n2. Checking the IEEE Robotics and Automation Society's conference page at ieee-ras.org\n\nThe conference itself is scheduled for May 24-28, 2027 in Seoul, South Korea, so you can expect the paper submission deadline to likely fall in September 2026 based on historical patterns, but you should verify the exact deadline on the official conference website."
    ],
    "durationSeconds": 13.744597699999984
  },
  "sourceToolAssistantUUID": "8a4f2526-cc76-4eea-8ea2-8e35dc6b96ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-18T19:15:29.181Z_

Good — ICRA 2026 had a Sep 15 deadline, so ICRA 2027 likely ~Sep 2026. Now let me verify some critical technical claims and search for the most important potentially missed work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c48788a0-27de-4236-9c76-8070e79ff065",
  "isSidechain": false,
  "requestId": "req_011CbAZys4MGKb5BcUByPvdd",
  "type": "assistant",
  "uuid": "b37f45e3-e400-4a41-87e0-102968202178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmZTuydMC9KRq13sRwC6Lj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1840,
      "cache_read_input_tokens": 43590,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 43590,
          "cache_creation_input_tokens": 1840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1840
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

_source line 58 · 2026-05-18T19:15:29.607Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019zJFbSq9BFKTNgs7Crm8NF`</summary>

```json
{
  "query": "UAD unsupervised affordance distillation arXiv 2506.09284 ICRA 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b37f45e3-e400-4a41-87e0-102968202178",
  "isSidechain": false,
  "requestId": "req_011CbAZys4MGKb5BcUByPvdd",
  "type": "assistant",
  "uuid": "95f9a461-b6c6-4e8c-b95a-220aaaf71d20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MmZTuydMC9KRq13sRwC6Lj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1840,
      "cache_read_input_tokens": 43590,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 43590,
          "cache_creation_input_tokens": 1840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1840
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

_source line 59 · 2026-05-18T19:15:36.475Z_

<details><summary>↩ Tool result · `toolu_019zJFbSq9BFKTNgs7Crm8NF`</summary>

```text
Web search results for query: "UAD unsupervised affordance distillation arXiv 2506.09284 ICRA 2025"

Links: [{"title":"[2506.09284] UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/abs/2506.09284"},{"title":"[PDF] UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/UAD:-Unsupervised-Affordance-Distillation-for-in-Tang-Huang/a7992218b0f8c8663e8ac144fcf58017a2a3c335"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/11128868/;jsessionid=D67802792FD60A8A904686287211734E"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/pdf/2506.09284"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | alphaXiv","url":"https://www.alphaxiv.org/resources/2506.09284v1"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/html/2506.09284v1"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://www.researchgate.net/publication/392597063_UAD_Unsupervised_Affordance_Distillation_for_Generalization_in_Robotic_Manipulation"}]

I found detailed information about the paper you searched for. Here's what I found:

**UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation**

UAD (Unsupervised Affordance Distillation) is a method for distilling affordance knowledge from foundation models into a task-conditioned affordance model without any manual annotations.

**Key Contributions:**

By leveraging the complementary strengths of large vision models and vision-language models, UAD automatically annotates a large-scale dataset with detailed instruction and visual affordance pairs.

Training only a lightweight task-conditioned decoder atop frozen features, UAD exhibits notable generalization to in-the-wild robotic scenes and to various human activities, despite only being trained on rendered objects in simulation.

**Performance:**

Using affordance provided by UAD as the observation space, an imitation learning policy demonstrates promising generalization to unseen object instances, object categories, and even variations in task instructions after training on as few as 10 demonstrations.

**Publication:**

The paper was published in the 2025 IEEE International Conference on Robotics and Automation (ICRA), with authors including Yihe Tang, Wenlong Huang, Yingke Wang, Chengshu Li, Roy Yuan, Ruohan Zhang, Jiajun Wu, and Fei-Fei Li.

The paper is available on arXiv at 2506.09284.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95f9a461-b6c6-4e8c-b95a-220aaaf71d20",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "e5a8260e-f6c7-48d6-8cc2-396781a7612f",
  "toolUseResult": {
    "query": "UAD unsupervised affordance distillation arXiv 2506.09284 ICRA 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YVg5G1twJQfD1XBrFo8sGH",
        "content": [
          {
            "title": "[2506.09284] UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation",
            "url": "https://arxiv.org/abs/2506.09284"
          },
          {
            "title": "[PDF] UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/UAD:-Unsupervised-Affordance-Distillation-for-in-Tang-Huang/a7992218b0f8c8663e8ac144fcf58017a2a3c335"
          },
          {
            "title": "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/document/11128868/;jsessionid=D67802792FD60A8A904686287211734E"
          },
          {
            "title": "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2506.09284"
          },
          {
            "title": "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2506.09284v1"
          },
          {
            "title": "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation",
            "url": "https://arxiv.org/html/2506.09284v1"
          },
          {
            "title": "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation",
            "url": "https://www.researchgate.net/publication/392597063_UAD_Unsupervised_Affordance_Distillation_for_Generalization_in_Robotic_Manipulation"
          }
        ]
      },
      "I found detailed information about the paper you searched for. Here's what I found:\n\n**UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation**\n\nUAD (Unsupervised Affordance Distillation) is a method for distilling affordance knowledge from foundation models into a task-conditioned affordance model without any manual annotations.\n\n**Key Contributions:**\n\nBy leveraging the complementary strengths of large vision models and vision-language models, UAD automatically annotates a large-scale dataset with detailed instruction and visual affordance pairs.\n\nTraining only a lightweight task-conditioned decoder atop frozen features, UAD exhibits notable generalization to in-the-wild robotic scenes and to various human activities, despite only being trained on rendered objects in simulation.\n\n**Performance:**\n\nUsing affordance provided by UAD as the observation space, an imitation learning policy demonstrates promising generalization to unseen object instances, object categories, and even variations in task instructions after training on as few as 10 demonstrations.\n\n**Publication:**\n\nThe paper was published in the 2025 IEEE International Conference on Robotics and Automation (ICRA), with authors including Yihe Tang, Wenlong Huang, Yingke Wang, Chengshu Li, Roy Yuan, Ruohan Zhang, Jiajun Wu, and Fei-Fei Li.\n\nThe paper is available on arXiv at 2506.09284."
    ],
    "durationSeconds": 6.863247164000001
  },
  "sourceToolAssistantUUID": "95f9a461-b6c6-4e8c-b95a-220aaaf71d20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 60_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e5a8260e-f6c7-48d6-8cc2-396781a7612f",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 61_

```json
{
  "type": "ai-title",
  "aiTitle": "AffordVLA: Open-vocabulary affordance distillation into VLA for robust manipulation",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Tool call

_source line 62 · 2026-05-18T19:15:39.630Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D4gw5NbwMZHrA2HeJNNvnG`</summary>

```json
{
  "query": "\"affordance\" \"heatmap\" \"VLA\" \"auxiliary\" OR \"distill\" site:arxiv.org 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5a8260e-f6c7-48d6-8cc2-396781a7612f",
  "isSidechain": false,
  "requestId": "req_011CbAZzh76ZnstDWfxBbAEh",
  "type": "assistant",
  "uuid": "0f3e699c-3137-4c72-a5c3-f95d9c3c8b4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RB2GeGAeR3jJeWcsGW6t5c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1000,
      "cache_read_input_tokens": 45430,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1000,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 45430,
          "cache_creation_input_tokens": 1000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1000
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

_source line 63 · 2026-05-18T19:15:48.091Z_

<details><summary>↩ Tool result · `toolu_01D4gw5NbwMZHrA2HeJNNvnG`</summary>

```text
Web search results for query: ""affordance" "heatmap" "VLA" "auxiliary" OR "distill" site:arxiv.org 2026"

Links: [{"title":"More than A Point: Capturing Uncertainty with Adaptive Affordance Heatmaps for Spatial Grounding in Robotic Tasks","url":"https://arxiv.org/html/2510.10912v1"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation","url":"https://arxiv.org/html/2506.09284v1"},{"title":"ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2511.18082"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v2"}]

I found several relevant papers on arxiv.org matching your search criteria. Here are the results:

1. **More than A Point: Capturing Uncertainty with Adaptive Affordance Heatmaps for Spatial Grounding in Robotic Tasks** (October 13, 2025)
   - Introduces RoboMAP, a framework that generates adaptive affordance heatmaps as an intermediate representation for robotic manipulation tasks guided by vision-language models.

2. **UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation** (June 10, 2025)
   - Presents Unsupervised Affordance Distillation (UAD), a method that extracts affordance knowledge from foundation models and distills it into a task-conditioned affordance model, all without manual annotation.

3. **ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models** (April 13, 2026)
   - Proposes a method where auxiliary components are removed during inference, allowing the student to execute only dynamically routed layers and generate high-precision actions, achieving comparable or superior performance to full-scale VLA models while reducing computation by over 50%.

4. **Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation** (December 2025)
   - Introduces Affordance Field Intervention (AFI), a lightweight hybrid framework that uses Spatial Affordance Fields as an on-demand plugin to guide VLA behavior.

5. **CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance** (July 31, 2025)
   - Proposes improvements to VLA models through visual-textual chain-of-affordance reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f3e699c-3137-4c72-a5c3-f95d9c3c8b4c",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "6c5a55ed-2f46-40a3-a377-2c8f3f90af39",
  "toolUseResult": {
    "query": "\"affordance\" \"heatmap\" \"VLA\" \"auxiliary\" OR \"distill\" site:arxiv.org 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WsGZW2bHJZ9XJfPo2LZhep",
        "content": [
          {
            "title": "More than A Point: Capturing Uncertainty with Adaptive Affordance Heatmaps for Spatial Grounding in Robotic Tasks",
            "url": "https://arxiv.org/html/2510.10912v1"
          },
          {
            "title": "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation",
            "url": "https://arxiv.org/html/2506.09284v1"
          },
          {
            "title": "ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.18082"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          },
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance",
            "url": "https://arxiv.org/html/2412.20451v2"
          }
        ]
      },
      "I found several relevant papers on arxiv.org matching your search criteria. Here are the results:\n\n1. **More than A Point: Capturing Uncertainty with Adaptive Affordance Heatmaps for Spatial Grounding in Robotic Tasks** (October 13, 2025)\n   - Introduces RoboMAP, a framework that generates adaptive affordance heatmaps as an intermediate representation for robotic manipulation tasks guided by vision-language models.\n\n2. **UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation** (June 10, 2025)\n   - Presents Unsupervised Affordance Distillation (UAD), a method that extracts affordance knowledge from foundation models and distills it into a task-conditioned affordance model, all without manual annotation.\n\n3. **ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models** (April 13, 2026)\n   - Proposes a method where auxiliary components are removed during inference, allowing the student to execute only dynamically routed layers and generate high-precision actions, achieving comparable or superior performance to full-scale VLA models while reducing computation by over 50%.\n\n4. **Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation** (December 2025)\n   - Introduces Affordance Field Intervention (AFI), a lightweight hybrid framework that uses Spatial Affordance Fields as an on-demand plugin to guide VLA behavior.\n\n5. **CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance** (July 31, 2025)\n   - Proposes improvements to VLA models through visual-textual chain-of-affordance reasoning."
    ],
    "durationSeconds": 8.457099053999992
  },
  "sourceToolAssistantUUID": "0f3e699c-3137-4c72-a5c3-f95d9c3c8b4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-18T19:15:50.479Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JVgSvrvee4miU5qUdWDmrx`</summary>

```json
{
  "query": "RoboMAP adaptive affordance heatmaps VLA spatial grounding arXiv 2510.10912"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c5a55ed-2f46-40a3-a377-2c8f3f90af39",
  "isSidechain": false,
  "requestId": "req_011CbAa1YkptxLiNph23WqdD",
  "type": "assistant",
  "uuid": "f8298822-58f1-4642-b135-b2b8e5dbbcfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtWB2u9KGrhVqw4eLoUAV2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 46430,
      "output_tokens": 77,
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
          "output_tokens": 77,
          "cache_read_input_tokens": 46430,
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

### Tool result

_source line 65 · 2026-05-18T19:15:57.492Z_

<details><summary>↩ Tool result · `toolu_01JVgSvrvee4miU5qUdWDmrx`</summary>

```text
Web search results for query: "RoboMAP adaptive affordance heatmaps VLA spatial grounding arXiv 2510.10912"

Links: [{"title":"[2510.10912] More than A Point: Capturing Uncertainty with Adaptive Affordance Heatmaps for Spatial Grounding in Robotic Tasks","url":"https://arxiv.org/abs/2510.10912"},{"title":"Capturing Uncertainty with Adaptive Affordance Heatmaps ...","url":"https://arxiv.org/pdf/2510.10912"},{"title":"More than A Point: Capturing Uncertainty with Adaptive Affordance Heatmaps for Spatial Grounding in Robotic Tasks","url":"https://arxiv.org/html/2510.10912"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos","url":"https://arxiv.org/pdf/2512.13080"},{"title":"SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding","url":"https://arxiv.org/pdf/2512.12842"}]

I found the paper! Here's what the search revealed:

RoboMAP is a framework that represents spatial targets as continuous, adaptive affordance heatmaps, which captures uncertainty in spatial grounding and provides richer information for downstream policies, enhancing task success and interpretability.

The paper addresses the brittleness of language-guided robotic systems that collapse spatial reasoning into discrete points, which makes them vulnerable to perceptual noise and semantic ambiguity. The heatmap models the entire workspace as a continuous probability distribution, quantifying the suitability of each region for a given language-conditioned task.

RoboMAP combines a vision-language backbone with an Adaptive Heatmap Decoder (AHD) to produce adaptive affordance heatmaps.

**Key Results:**
- RoboMAP surpasses previous state-of-the-art on a majority of grounding benchmarks with up to 50x speed improvement and achieves an 82% success rate in real-world manipulation.
- The system demonstrates successful zero-shot transfer to complex tasks such as pick-and-place, industrial sorting, and navigation.

The paper was published in October 2025. You can access the full paper at https://arxiv.org/abs/2510.10912.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8298822-58f1-4642-b135-b2b8e5dbbcfe",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "a833a2e1-a09e-402b-a8ec-e081668e6e81",
  "toolUseResult": {
    "query": "RoboMAP adaptive affordance heatmaps VLA spatial grounding arXiv 2510.10912",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WkTN4D5CeGJDCkU2kQYJ8o",
        "content": [
          {
            "title": "[2510.10912] More than A Point: Capturing Uncertainty with Adaptive Affordance Heatmaps for Spatial Grounding in Robotic Tasks",
            "url": "https://arxiv.org/abs/2510.10912"
          },
          {
            "title": "Capturing Uncertainty with Adaptive Affordance Heatmaps ...",
            "url": "https://arxiv.org/pdf/2510.10912"
          },
          {
            "title": "More than A Point: Capturing Uncertainty with Adaptive Affordance Heatmaps for Spatial Grounding in Robotic Tasks",
            "url": "https://arxiv.org/html/2510.10912"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          },
          {
            "title": "Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos",
            "url": "https://arxiv.org/pdf/2512.13080"
          },
          {
            "title": "SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding",
            "url": "https://arxiv.org/pdf/2512.12842"
          }
        ]
      },
      "I found the paper! Here's what the search revealed:\n\nRoboMAP is a framework that represents spatial targets as continuous, adaptive affordance heatmaps, which captures uncertainty in spatial grounding and provides richer information for downstream policies, enhancing task success and interpretability.\n\nThe paper addresses the brittleness of language-guided robotic systems that collapse spatial reasoning into discrete points, which makes them vulnerable to perceptual noise and semantic ambiguity. The heatmap models the entire workspace as a continuous probability distribution, quantifying the suitability of each region for a given language-conditioned task.\n\nRoboMAP combines a vision-language backbone with an Adaptive Heatmap Decoder (AHD) to produce adaptive affordance heatmaps.\n\n**Key Results:**\n- RoboMAP surpasses previous state-of-the-art on a majority of grounding benchmarks with up to 50x speed improvement and achieves an 82% success rate in real-world manipulation.\n- The system demonstrates successful zero-shot transfer to complex tasks such as pick-and-place, industrial sorting, and navigation.\n\nThe paper was published in October 2025. You can access the full paper at https://arxiv.org/abs/2510.10912."
    ],
    "durationSeconds": 7.00747507700001
  },
  "sourceToolAssistantUUID": "f8298822-58f1-4642-b135-b2b8e5dbbcfe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-18T19:16:00.233Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FHswALhVResHQJht1Wvp9z`</summary>

```json
{
  "query": "SAGA structured affordance grounding VLA mobile manipulation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a833a2e1-a09e-402b-a8ec-e081668e6e81",
  "isSidechain": false,
  "requestId": "req_011CbAa2Fq7x1GvU2naTJWe2",
  "type": "assistant",
  "uuid": "4d210590-8f10-4baa-a698-37311b4158c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsxFB7kwxcuztetYgWvjv2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 47259,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 705,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 47259,
          "cache_creation_input_tokens": 705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 705
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

_source line 67 · 2026-05-18T19:16:07.337Z_

<details><summary>↩ Tool result · `toolu_01FHswALhVResHQJht1Wvp9z`</summary>

```text
Web search results for query: "SAGA structured affordance grounding VLA mobile manipulation 2025 2026"

Links: [{"title":"SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding","url":"https://arxiv.org/html/2512.12842"},{"title":"[2512.12842] SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding","url":"https://arxiv.org/abs/2512.12842"},{"title":"SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding","url":"https://arxiv.org/pdf/2512.12842"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/pdf/2603.22760"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/html/2512.07472v1"}]

Based on the search results, here's what I found about SAGA and related research:

## SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding

SAGA is a versatile and adaptive framework for visuomotor control that can generalize across various environments, task objectives, and user specifications. It disentangles high-level semantic intent from low-level visuomotor control by explicitly grounding task objectives in the observed environment, using an affordance-based task representation to express diverse and complex behaviors in a unified, structured form.

### Key Technical Approach

SAGA grounds the task representation to the robot's visual observation as 3D affordance heatmaps, highlighting task-relevant entities while abstracting away spurious appearance variations that would hinder generalization. These grounded affordances enable training a conditional policy on multi-task demonstration data for whole-body control, and SAGA can solve tasks specified in different forms, including language instructions, selected points, and example demonstrations, enabling both zero-shot execution and few-shot adaptation.

### Experimental Results

The work instantiated SAGA on a quadrupedal manipulator and conducted extensive experiments across eleven real-world tasks, with SAGA consistently outperforming end-to-end and modular baselines by substantial margins. These results demonstrate that structured affordance grounding offers a scalable and effective pathway toward generalist mobile manipulation.

The paper was published in December 2025 on arXiv (paper ID: 2512.12842).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d210590-8f10-4baa-a698-37311b4158c4",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "d4bff699-3fe3-418c-bbfd-d80b3099d706",
  "toolUseResult": {
    "query": "SAGA structured affordance grounding VLA mobile manipulation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E9LX9xUSbvrgrA9z95R6u4",
        "content": [
          {
            "title": "SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding",
            "url": "https://arxiv.org/html/2512.12842"
          },
          {
            "title": "[2512.12842] SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding",
            "url": "https://arxiv.org/abs/2512.12842"
          },
          {
            "title": "SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding",
            "url": "https://arxiv.org/pdf/2512.12842"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/pdf/2603.22760"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/html/2512.07472v1"
          }
        ]
      },
      "Based on the search results, here's what I found about SAGA and related research:\n\n## SAGA: Open-World Mobile Manipulation via Structured Affordance Grounding\n\nSAGA is a versatile and adaptive framework for visuomotor control that can generalize across various environments, task objectives, and user specifications. It disentangles high-level semantic intent from low-level visuomotor control by explicitly grounding task objectives in the observed environment, using an affordance-based task representation to express diverse and complex behaviors in a unified, structured form.\n\n### Key Technical Approach\n\nSAGA grounds the task representation to the robot's visual observation as 3D affordance heatmaps, highlighting task-relevant entities while abstracting away spurious appearance variations that would hinder generalization. These grounded affordances enable training a conditional policy on multi-task demonstration data for whole-body control, and SAGA can solve tasks specified in different forms, including language instructions, selected points, and example demonstrations, enabling both zero-shot execution and few-shot adaptation.\n\n### Experimental Results\n\nThe work instantiated SAGA on a quadrupedal manipulator and conducted extensive experiments across eleven real-world tasks, with SAGA consistently outperforming end-to-end and modular baselines by substantial margins. These results demonstrate that structured affordance grounding offers a scalable and effective pathway toward generalist mobile manipulation.\n\nThe paper was published in December 2025 on arXiv (paper ID: 2512.12842)."
    ],
    "durationSeconds": 7.099449523999996
  },
  "sourceToolAssistantUUID": "4d210590-8f10-4baa-a698-37311b4158c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-18T19:16:10.186Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0177ARoTzoKf6x5kLYMmNf6A`</summary>

```json
{
  "query": "OpenVLA-OFT fine-tuning LoRA arXiv 2502.19645 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4bff699-3fe3-418c-bbfd-d80b3099d706",
  "isSidechain": false,
  "requestId": "req_011CbAa2yD2DfopKeqbchojY",
  "type": "assistant",
  "uuid": "62f56f9a-3741-4e6b-804f-63433b0a3034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bm2rbYK22M74bR1FqYGh5j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 47964,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 47964,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
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

_source line 69 · 2026-05-18T19:16:16.898Z_

<details><summary>↩ Tool result · `toolu_0177ARoTzoKf6x5kLYMmNf6A`</summary>

```text
Web search results for query: "OpenVLA-OFT fine-tuning LoRA arXiv 2502.19645 2025"

Links: [{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"moojink/openvla-7b-oft-finetuned-libero-goal · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"},{"title":"moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"},{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"[2502.19645v1] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645v1"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"}]

Based on the search results, here's what I found about OpenVLA-OFT fine-tuning with arXiv 2502.19645:

## Overview

OpenVLA-OFT (arXiv 2502.19645, Kim et al., February 2025) addresses the three main practical limitations of the original OpenVLA fine-tuning recipe: slow inference speed, action discretization artifacts, and lack of temporal action coherence.

## Key Design Changes

OFT changes three design decisions during the fine-tuning stage while keeping the pre-trained VLM backbone identical. First, parallel decoding replaces autoregressive generation. Instead of predicting 7 action tokens sequentially (requiring 7 forward passes), OFT predicts all action dimensions simultaneously in a single forward pass. This change alone increases inference speed from approximately 5 Hz to over 100 Hz.

Second, continuous L1 regression replaces discretized token prediction. Rather than mapping continuous actions to 256 discrete bins (which introduces quantization noise), OFT regresses directly to continuous action values using an L1 loss.

## LoRA Fine-tuning Efficiency

With LoRA (Low-Rank Adaptation), fine-tuning takes 10-15 hours on a single A100 GPU.

## Performance Results

OpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26x. In real-world evaluations, the fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs and strong imitation learning policies by up to 15% in average success rate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62f56f9a-3741-4e6b-804f-63433b0a3034",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "d83da6e7-fcbf-406a-89f5-4172f99fe6ca",
  "toolUseResult": {
    "query": "OpenVLA-OFT fine-tuning LoRA arXiv 2502.19645 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Wtcp1Hjfv4QNLpmEz7zUUo",
        "content": [
          {
            "title": "Training Data for OpenVLA | Data Requirements & Formats | Claru",
            "url": "https://claru.ai/models/openvla"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v1"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "moojink/openvla-7b-oft-finetuned-libero-goal · Hugging Face",
            "url": "https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal"
          },
          {
            "title": "Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation",
            "url": "https://arxiv.org/pdf/2603.16044"
          },
          {
            "title": "moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face",
            "url": "https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"
          },
          {
            "title": "moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face",
            "url": "https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"
          },
          {
            "title": "[2502.19645v1] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/abs/2502.19645v1"
          },
          {
            "title": "[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/abs/2502.19645"
          }
        ]
      },
      "Based on the search results, here's what I found about OpenVLA-OFT fine-tuning with arXiv 2502.19645:\n\n## Overview\n\nOpenVLA-OFT (arXiv 2502.19645, Kim et al., February 2025) addresses the three main practical limitations of the original OpenVLA fine-tuning recipe: slow inference speed, action discretization artifacts, and lack of temporal action coherence.\n\n## Key Design Changes\n\nOFT changes three design decisions during the fine-tuning stage while keeping the pre-trained VLM backbone identical. First, parallel decoding replaces autoregressive generation. Instead of predicting 7 action tokens sequentially (requiring 7 forward passes), OFT predicts all action dimensions simultaneously in a single forward pass. This change alone increases inference speed from approximately 5 Hz to over 100 Hz.\n\nSecond, continuous L1 regression replaces discretized token prediction. Rather than mapping continuous actions to 256 discrete bins (which introduces quantization noise), OFT regresses directly to continuous action values using an L1 loss.\n\n## LoRA Fine-tuning Efficiency\n\nWith LoRA (Low-Rank Adaptation), fine-tuning takes 10-15 hours on a single A100 GPU.\n\n## Performance Results\n\nOpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26x. In real-world evaluations, the fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs and strong imitation learning policies by up to 15% in average success rate."
    ],
    "durationSeconds": 6.709833665000013
  },
  "sourceToolAssistantUUID": "62f56f9a-3741-4e6b-804f-63433b0a3034",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-18T19:16:21.047Z_

Good. Now let me search for the most critical potential gap — has anyone already done exactly what AffordVLA proposes (affordance pseudo-labels as auxiliary loss in VLA training)?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d83da6e7-fcbf-406a-89f5-4172f99fe6ca",
  "isSidechain": false,
  "requestId": "req_011CbAa3fuVh31b9QjHJW3xB",
  "type": "assistant",
  "uuid": "0ee4bbf7-846e-4846-aaf8-58c26170dc67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcdSoARGwJxXThxemkEZ6U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 48640,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 48640,
          "cache_creation_input_tokens": 1023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1023
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

_source line 71 · 2026-05-18T19:16:21.966Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PMaksgbBevkKHtk8wdd5SB`</summary>

```json
{
  "query": "\"auxiliary affordance\" OR \"affordance prediction head\" VLA training end-to-end 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ee4bbf7-846e-4846-aaf8-58c26170dc67",
  "isSidechain": false,
  "requestId": "req_011CbAa3fuVh31b9QjHJW3xB",
  "type": "assistant",
  "uuid": "9b5f2c10-8d3d-43b1-810d-7b71d8996337",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RcdSoARGwJxXThxemkEZ6U",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1023,
      "cache_read_input_tokens": 48640,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 48640,
          "cache_creation_input_tokens": 1023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1023
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

_source line 72 · 2026-05-18T19:16:28.904Z_

<details><summary>↩ Tool result · `toolu_01PMaksgbBevkKHtk8wdd5SB`</summary>

```text
Web search results for query: ""auxiliary affordance" OR "affordance prediction head" VLA training end-to-end 2025 2026"

Links: [{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"},{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"2025-9-18 ThinkAct: Vision-Language-Action Reasoning via","url":"https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"},{"title":"A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model","url":"https://arxiv.org/pdf/2604.05672"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/pdf/2603.22760"}]

Based on the search results, here are the relevant findings related to your query about auxiliary affordance and affordance prediction in VLA training:

## Key Papers and Research

**CoA-VLA (Chain-of-Affordance VLA)** - This approach incorporates reasoning in the format of sequential robot affordances to facilitate task completion. The model considers four types of affordances: object affordance, grasp affordance, placement affordance, and regrasp affordance. A vision-language co-injection module integrates this knowledge into the policy network, allowing the robot to leverage essential contextual information during action inference.

**Auxiliary Prediction Tasks in VLAs** - Recent work augments policies with predictive capacities by introducing auxiliary prediction tasks or co-training the policy with a predictive model. Examples include:
- WorldVLA enhances the VLA policy by adding an image prediction component to generate future scenes
- DreamVLA augments the policy with three auxiliary predictive tasks: semantic, depth and dynamic prediction

**SG-VLA (Spatially-Grounded VLA)** - This framework enhances learning through enriching sensory input and providing denser learning signals through auxiliary co-training, using a co-training strategy that simultaneously predicts actions and auxiliary tasks to force the model to learn more interpretable and spatially aware representations.

These represent recent advances (2025-2026) in VLA training that incorporate various forms of auxiliary affordance prediction to improve end-to-end policy learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b5f2c10-8d3d-43b1-810d-7b71d8996337",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "7efb4c5a-c463-43b0-8808-10f5294fe7e7",
  "toolUseResult": {
    "query": "\"auxiliary affordance\" OR \"affordance prediction head\" VLA training end-to-end 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012GsDJYFtNjGWH6bPZRtjhc",
        "content": [
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance",
            "url": "https://arxiv.org/pdf/2412.20451"
          },
          {
            "title": "Improving Vision-Language-Action Models via Chain-of-Affordance",
            "url": "https://arxiv.org/html/2412.20451v1"
          },
          {
            "title": "ICCV 2025 Open Access Repository",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"
          },
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          },
          {
            "title": "2025-9-18 ThinkAct: Vision-Language-Action Reasoning via",
            "url": "https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"
          },
          {
            "title": "A1: A Fully Transparent Open-Source, Adaptive and Efficient Truncated Vision-Language-Action Model",
            "url": "https://arxiv.org/pdf/2604.05672"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/pdf/2603.22760"
          }
        ]
      },
      "Based on the search results, here are the relevant findings related to your query about auxiliary affordance and affordance prediction in VLA training:\n\n## Key Papers and Research\n\n**CoA-VLA (Chain-of-Affordance VLA)** - This approach incorporates reasoning in the format of sequential robot affordances to facilitate task completion. The model considers four types of affordances: object affordance, grasp affordance, placement affordance, and regrasp affordance. A vision-language co-injection module integrates this knowledge into the policy network, allowing the robot to leverage essential contextual information during action inference.\n\n**Auxiliary Prediction Tasks in VLAs** - Recent work augments policies with predictive capacities by introducing auxiliary prediction tasks or co-training the policy with a predictive model. Examples include:\n- WorldVLA enhances the VLA policy by adding an image prediction component to generate future scenes\n- DreamVLA augments the policy with three auxiliary predictive tasks: semantic, depth and dynamic prediction\n\n**SG-VLA (Spatially-Grounded VLA)** - This framework enhances learning through enriching sensory input and providing denser learning signals through auxiliary co-training, using a co-training strategy that simultaneously predicts actions and auxiliary tasks to force the model to learn more interpretable and spatially aware representations.\n\nThese represent recent advances (2025-2026) in VLA training that incorporate various forms of auxiliary affordance prediction to improve end-to-end policy learning."
    ],
    "durationSeconds": 6.9317830130000075
  },
  "sourceToolAssistantUUID": "9b5f2c10-8d3d-43b1-810d-7b71d8996337",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 73 · 2026-05-18T19:16:28.908Z_

```json
{
  "parentUuid": "7efb4c5a-c463-43b0-8808-10f5294fe7e7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6a3b1a0a-789e-4a81-96c1-99e0f121137c",
  "timestamp": "2026-05-18T19:16:28.908Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 74_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "6a3b1a0a-789e-4a81-96c1-99e0f121137c",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 75_

```json
{
  "type": "ai-title",
  "aiTitle": "AffordVLA: Open-vocabulary affordance distillation into VLA for robust manipulation",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Tool call

_source line 76 · 2026-05-18T19:16:31.624Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012aKKZvti5PBstdk5EC49cA`</summary>

```json
{
  "query": "DreamVLA WorldVLA auxiliary prediction depth affordance VLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a3b1a0a-789e-4a81-96c1-99e0f121137c",
  "isSidechain": false,
  "requestId": "req_011CbAa4ZFvM73AMVbNYCV63",
  "type": "assistant",
  "uuid": "a5029e22-e71c-4312-a4ad-17dcc5555119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRL6AG29iHRJAKgJjCfAkE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 49663,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1024,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 49663,
          "cache_creation_input_tokens": 1024,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1024
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

_source line 77 · 2026-05-18T19:16:39.022Z_

<details><summary>↩ Tool result · `toolu_012aKKZvti5PBstdk5EC49cA`</summary>

```text
Web search results for query: "DreamVLA WorldVLA auxiliary prediction depth affordance VLA 2025 2026"

Links: [{"title":"Do World Action Models Generalize Better than VLAs? A Robustness Study","url":"https://arxiv.org/html/2603.22078v1"},{"title":"DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge | OpenReview","url":"https://openreview.net/forum?id=PK07eretkF"},{"title":"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision–Language–Action Models","url":"https://arxiv.org/html/2510.14836v1"},{"title":"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.14836"},{"title":"Reasoning Vision Language Action Models","url":"https://www.emergentmind.com/topics/reasoning-vision-language-action-vla-models"},{"title":"DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge","url":"https://arxiv.org/pdf/2507.04447"},{"title":"DreamVLA: A Vision-Language-Action Model Dreamed ...","url":"https://openreview.net/pdf/c3f9cfb29eaaaa177caf91f3e479582fa97f5442.pdf"},{"title":"DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge","url":"https://arxiv.org/html/2507.04447v2"},{"title":"GitHub - Zhangwenyao1/DreamVLA: [NeurIPS 2025] DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge · GitHub","url":"https://github.com/Zhangwenyao1/DreamVLA"}]

Based on the search results, I found relevant information about the research topics you queried:

## DreamVLA

DreamVLA augments the policy with three auxiliary predictive tasks: semantic, depth and dynamic prediction. More specifically, DreamVLA explicitly predicts dynamic regions, depth map, semantics (DINOv2 and SAM) knowledge, significantly enhancing the model's action reasoning and generalization.

DreamVLA is a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perception-prediction-action loop for manipulation tasks. The model addresses limitations of existing approaches by avoiding redundant pixel information and incorporating explicit 3D knowledge of environments.

DreamVLA was published as a NeurIPS 2025 paper on comprehensive world knowledge.

## WorldVLA

WorldVLA enhances the VLA policy by adding image prediction component to generate future scenes given the observation and current action.

## Depth and Affordance Prediction in VLAs

Recent work has explored depth as an auxiliary prediction task for VLAs. QDepth-VLA augments VLA models with an auxiliary depth prediction task, with a dedicated depth expert designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5029e22-e71c-4312-a4ad-17dcc5555119",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "4fa29a5b-ee0d-4924-bc13-c272f05e49f4",
  "toolUseResult": {
    "query": "DreamVLA WorldVLA auxiliary prediction depth affordance VLA 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0113CAdSWgvyWMdibgxpMFVk",
        "content": [
          {
            "title": "Do World Action Models Generalize Better than VLAs? A Robustness Study",
            "url": "https://arxiv.org/html/2603.22078v1"
          },
          {
            "title": "DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge | OpenReview",
            "url": "https://openreview.net/forum?id=PK07eretkF"
          },
          {
            "title": "QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision–Language–Action Models",
            "url": "https://arxiv.org/html/2510.14836v1"
          },
          {
            "title": "QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2510.14836"
          },
          {
            "title": "Reasoning Vision Language Action Models",
            "url": "https://www.emergentmind.com/topics/reasoning-vision-language-action-vla-models"
          },
          {
            "title": "DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge",
            "url": "https://arxiv.org/pdf/2507.04447"
          },
          {
            "title": "DreamVLA: A Vision-Language-Action Model Dreamed ...",
            "url": "https://openreview.net/pdf/c3f9cfb29eaaaa177caf91f3e479582fa97f5442.pdf"
          },
          {
            "title": "DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge",
            "url": "https://arxiv.org/html/2507.04447v2"
          },
          {
            "title": "GitHub - Zhangwenyao1/DreamVLA: [NeurIPS 2025] DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge · GitHub",
            "url": "https://github.com/Zhangwenyao1/DreamVLA"
          }
        ]
      },
      "Based on the search results, I found relevant information about the research topics you queried:\n\n## DreamVLA\n\nDreamVLA augments the policy with three auxiliary predictive tasks: semantic, depth and dynamic prediction. More specifically, DreamVLA explicitly predicts dynamic regions, depth map, semantics (DINOv2 and SAM) knowledge, significantly enhancing the model's action reasoning and generalization.\n\nDreamVLA is a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perception-prediction-action loop for manipulation tasks. The model addresses limitations of existing approaches by avoiding redundant pixel information and incorporating explicit 3D knowledge of environments.\n\nDreamVLA was published as a NeurIPS 2025 paper on comprehensive world knowledge.\n\n## WorldVLA\n\nWorldVLA enhances the VLA policy by adding image prediction component to generate future scenes given the observation and current action.\n\n## Depth and Affordance Prediction in VLAs\n\nRecent work has explored depth as an auxiliary prediction task for VLAs. QDepth-VLA augments VLA models with an auxiliary depth prediction task, with a dedicated depth expert designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder."
    ],
    "durationSeconds": 7.395082886000047
  },
  "sourceToolAssistantUUID": "a5029e22-e71c-4312-a4ad-17dcc5555119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-18T19:16:42.918Z_

Very important — QDepth-VLA uses auxiliary depth prediction, and DreamVLA uses auxiliary semantic/depth/dynamic prediction. The pattern of auxiliary losses for VLAs is well-established. Let me check QDepth-VLA more closely, and search for the most critical missing piece.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fa29a5b-ee0d-4924-bc13-c272f05e49f4",
  "isSidechain": false,
  "requestId": "req_011CbAa5JVwKpECTLtyvqncm",
  "type": "assistant",
  "uuid": "fde582aa-61ed-481f-b755-78731e34e2dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193CeXVkeRDQzxjBjgFdQB6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 50687,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 50687,
          "cache_creation_input_tokens": 857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 857
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

_source line 79 · 2026-05-18T19:16:43.217Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MoBKgRqcUDDXn31hVCoNZr`</summary>

```json
{
  "query": "QDepth-VLA quantized depth auxiliary supervision VLA arXiv 2510.14836"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fde582aa-61ed-481f-b755-78731e34e2dc",
  "isSidechain": false,
  "requestId": "req_011CbAa5JVwKpECTLtyvqncm",
  "type": "assistant",
  "uuid": "514973b6-228a-488a-add3-e8548f3079db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193CeXVkeRDQzxjBjgFdQB6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 50687,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 137,
          "cache_read_input_tokens": 50687,
          "cache_creation_input_tokens": 857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 857
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

_source line 80 · 2026-05-18T19:16:50.327Z_

<details><summary>↩ Tool result · `toolu_01MoBKgRqcUDDXn31hVCoNZr`</summary>

```text
Web search results for query: "QDepth-VLA quantized depth auxiliary supervision VLA arXiv 2510.14836"

Links: [{"title":"[2510.14836] QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.14836"},{"title":"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251014836L/abstract"},{"title":"QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.14836"},{"title":"[Literature Review] QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/qdepth-vla-quantized-depth-prediction-as-auxiliary-supervision-for-vision-language-action-models"},{"title":"机器之心 JIQIZHIXIN on X: \"Do existing Vision–Language–Action (VLA) models struggle with fine-grained manipulation tasks? This study points out that current approaches often can't understand essential 3D structures for precise control. To fix this, researchers propose QDepth-VLA, a framework that adds https://t.co/mcyFfhAOwa\" / X","url":"https://x.com/jiqizhixin/status/1996684434326606046"},{"title":"GitHub - ucasmichael/QDepth-VLA: QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models · GitHub","url":"https://github.com/ucasmichael/QDepth-VLA"},{"title":"Paper page - VLA-0: Building State-of-the-Art VLAs with Zero Modification","url":"https://huggingface.co/papers/2510.13054"}]

Based on the search results, here's what I found about QDepth-VLA:

## Overview

QDepth-VLA is a general framework that augments VLA models with an auxiliary depth prediction task. The paper is authored by Yixuan Li and colleagues from the University of the Chinese Academy of Sciences and the Institute of Automation, Chinese Academy of Science.

## Problem and Solution

Existing approaches often lack the ability to understand and reason over the essential 3D structures necessary for precise control. A dedicated depth expert is designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder, enabling the model to learn depth-aware representations that capture critical geometric cues.

## Key Features

The core idea is to augment VLA models with an auxiliary quantized depth prediction task, addressing limitations of existing methods that often struggle with 3D structural understanding, suffer from noisy depth supervision, or interfere with pretrained vision-language representations. The Video-Depth-Anything (ViDA) framework, a state-of-the-art monocular video depth estimation model, is applied to RGB frames from datasets like OXE and LIBERO.

## Results

Experimental results on the simulation benchmarks and real-world tasks demonstrate that QDepth-VLA yields strong spatial reasoning and competitive performance on manipulation tasks.

The paper (arXiv 2510.14836) was submitted on October 16, 2025, with the latest revision on December 22, 2025, and the code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "514973b6-228a-488a-add3-e8548f3079db",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "8ef00828-6f45-463e-ac4f-dda72d2a0f02",
  "toolUseResult": {
    "query": "QDepth-VLA quantized depth auxiliary supervision VLA arXiv 2510.14836",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XyxZtLBuFGkQsJTAsPMARu",
        "content": [
          {
            "title": "[2510.14836] QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.14836"
          },
          {
            "title": "QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv251014836L/abstract"
          },
          {
            "title": "QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2510.14836"
          },
          {
            "title": "[Literature Review] QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models",
            "url": "https://www.themoonlight.io/en/review/qdepth-vla-quantized-depth-prediction-as-auxiliary-supervision-for-vision-language-action-models"
          },
          {
            "title": "机器之心 JIQIZHIXIN on X: \"Do existing Vision–Language–Action (VLA) models struggle with fine-grained manipulation tasks? This study points out that current approaches often can't understand essential 3D structures for precise control. To fix this, researchers propose QDepth-VLA, a framework that adds https://t.co/mcyFfhAOwa\" / X",
            "url": "https://x.com/jiqizhixin/status/1996684434326606046"
          },
          {
            "title": "GitHub - ucasmichael/QDepth-VLA: QDepth-VLA: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models · GitHub",
            "url": "https://github.com/ucasmichael/QDepth-VLA"
          },
          {
            "title": "Paper page - VLA-0: Building State-of-the-Art VLAs with Zero Modification",
            "url": "https://huggingface.co/papers/2510.13054"
          }
        ]
      },
      "Based on the search results, here's what I found about QDepth-VLA:\n\n## Overview\n\nQDepth-VLA is a general framework that augments VLA models with an auxiliary depth prediction task. The paper is authored by Yixuan Li and colleagues from the University of the Chinese Academy of Sciences and the Institute of Automation, Chinese Academy of Science.\n\n## Problem and Solution\n\nExisting approaches often lack the ability to understand and reason over the essential 3D structures necessary for precise control. A dedicated depth expert is designed to predict quantized latent tokens of depth maps obtained from a VQ-VAE encoder, enabling the model to learn depth-aware representations that capture critical geometric cues.\n\n## Key Features\n\nThe core idea is to augment VLA models with an auxiliary quantized depth prediction task, addressing limitations of existing methods that often struggle with 3D structural understanding, suffer from noisy depth supervision, or interfere with pretrained vision-language representations. The Video-Depth-Anything (ViDA) framework, a state-of-the-art monocular video depth estimation model, is applied to RGB frames from datasets like OXE and LIBERO.\n\n## Results\n\nExperimental results on the simulation benchmarks and real-world tasks demonstrate that QDepth-VLA yields strong spatial reasoning and competitive performance on manipulation tasks.\n\nThe paper (arXiv 2510.14836) was submitted on October 16, 2025, with the latest revision on December 22, 2025, and the code is available on GitHub."
    ],
    "durationSeconds": 7.105867131999985
  },
  "sourceToolAssistantUUID": "514973b6-228a-488a-add3-e8548f3079db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-18T19:16:53.514Z_

Now let me look at whether anyone has specifically done affordance heatmap prediction as auxiliary loss (not depth, but affordance specifically) in a VLA.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ef00828-6f45-463e-ac4f-dda72d2a0f02",
  "isSidechain": false,
  "requestId": "req_011CbAa68sHMtYy3nnMK2VNr",
  "type": "assistant",
  "uuid": "b54f6512-9e11-4fab-86c4-424db76d88b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuH7KDeKPGrCtDZpEJjWhy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1017,
      "cache_read_input_tokens": 51544,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1017,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 51544,
          "cache_creation_input_tokens": 1017,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1017
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

_source line 82 · 2026-05-18T19:16:54.514Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014qJLsSo3guHebm9tBQBZgq`</summary>

```json
{
  "query": "\"affordance heatmap\" \"auxiliary\" OR \"distill\" policy learning manipulation end-to-end 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b54f6512-9e11-4fab-86c4-424db76d88b9",
  "isSidechain": false,
  "requestId": "req_011CbAa68sHMtYy3nnMK2VNr",
  "type": "assistant",
  "uuid": "617be155-9291-47fd-9928-37fe21e21613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DuH7KDeKPGrCtDZpEJjWhy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1017,
      "cache_read_input_tokens": 51544,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1017,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 114,
          "cache_read_input_tokens": 51544,
          "cache_creation_input_tokens": 1017,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1017
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

_source line 83 · 2026-05-18T19:17:00.724Z_

<details><summary>↩ Tool result · `toolu_014qJLsSo3guHebm9tBQBZgq`</summary>

```text
Web search results for query: ""affordance heatmap" "auxiliary" OR "distill" policy learning manipulation end-to-end 2025 2026"

Links: [{"title":"RoboPCA: Pose-centered Affordance Learning from Human Demonstrations for Robot Manipulation","url":"https://arxiv.org/html/2603.07691v1"},{"title":"UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | Request PDF","url":"https://www.researchgate.net/publication/395210639_UAD_Unsupervised_Affordance_Distillation_for_Generalization_in_Robotic_Manipulation"},{"title":"End-to-End Affordance Learning for Robotic Manipulation","url":"https://arxiv.org/pdf/2209.12941"},{"title":"Affordance Learning for End-to-End Visuomotor Robot Control","url":"https://arxiv.org/pdf/1903.04053"},{"title":"AnchorDP3: 3D Affordance Guided Sparse Diffusion Policy for Robotic Manipulation RoboTwin Challenge Simulation Champion @ CVPR 2025 MEIS Workshop RoboTwin Dual-Arm Collaboration Challenge Technical Report","url":"https://arxiv.org/html/2506.19269v1"}]

Based on the search results, I found several relevant papers on affordance learning for robotic manipulation:

1. **UAD: Unsupervised Affordance Distillation** - This work constructs the 3D AffordanceNet benchmark and predicts per-point affordance heatmaps on object point clouds. Published May 2025, it appears to directly address affordance heatmaps and distillation for manipulation.

2. **End-to-End Affordance Learning for Robotic Manipulation** - This study uses contact information generated during RL training to predict contact maps and presents an end-to-end affordance learning framework that can generalize over different types of manipulation tasks.

3. **AnchorDP3: 3D Affordance Guided Sparse Diffusion Policy** - This approach integrates affordance priors with task-conditioned feature encoders and affordance-anchored keypose diffusion for robotic manipulation. This paper from June 2025 directly addresses end-to-end policy learning using affordance guidance.

4. **RoboPCA: Pose-centered Affordance Learning** - Published March 2026, this paper focuses on affordance learning from human demonstrations for robot manipulation.

The search results show active research in 2025-2026 on combining affordance representations (particularly heatmaps) with policy learning methods for manipulation tasks, including distillation and auxiliary learning approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "617be155-9291-47fd-9928-37fe21e21613",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "e2963b6b-f4e6-4209-8a39-0c6d1cc113cf",
  "toolUseResult": {
    "query": "\"affordance heatmap\" \"auxiliary\" OR \"distill\" policy learning manipulation end-to-end 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RUyw5PN8yywDyCaMt496pG",
        "content": [
          {
            "title": "RoboPCA: Pose-centered Affordance Learning from Human Demonstrations for Robot Manipulation",
            "url": "https://arxiv.org/html/2603.07691v1"
          },
          {
            "title": "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation | Request PDF",
            "url": "https://www.researchgate.net/publication/395210639_UAD_Unsupervised_Affordance_Distillation_for_Generalization_in_Robotic_Manipulation"
          },
          {
            "title": "End-to-End Affordance Learning for Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2209.12941"
          },
          {
            "title": "Affordance Learning for End-to-End Visuomotor Robot Control",
            "url": "https://arxiv.org/pdf/1903.04053"
          },
          {
            "title": "AnchorDP3: 3D Affordance Guided Sparse Diffusion Policy for Robotic Manipulation RoboTwin Challenge Simulation Champion @ CVPR 2025 MEIS Workshop RoboTwin Dual-Arm Collaboration Challenge Technical Report",
            "url": "https://arxiv.org/html/2506.19269v1"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on affordance learning for robotic manipulation:\n\n1. **UAD: Unsupervised Affordance Distillation** - This work constructs the 3D AffordanceNet benchmark and predicts per-point affordance heatmaps on object point clouds. Published May 2025, it appears to directly address affordance heatmaps and distillation for manipulation.\n\n2. **End-to-End Affordance Learning for Robotic Manipulation** - This study uses contact information generated during RL training to predict contact maps and presents an end-to-end affordance learning framework that can generalize over different types of manipulation tasks.\n\n3. **AnchorDP3: 3D Affordance Guided Sparse Diffusion Policy** - This approach integrates affordance priors with task-conditioned feature encoders and affordance-anchored keypose diffusion for robotic manipulation. This paper from June 2025 directly addresses end-to-end policy learning using affordance guidance.\n\n4. **RoboPCA: Pose-centered Affordance Learning** - Published March 2026, this paper focuses on affordance learning from human demonstrations for robot manipulation.\n\nThe search results show active research in 2025-2026 on combining affordance representations (particularly heatmaps) with policy learning methods for manipulation tasks, including distillation and auxiliary learning approaches."
    ],
    "durationSeconds": 6.204807325000002
  },
  "sourceToolAssistantUUID": "617be155-9291-47fd-9928-37fe21e21613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-18T19:17:03.804Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RsodRo3F84f4Aqy9SUn8T6`</summary>

```json
{
  "query": "Stable Language Guidance VLA modality collapse affordance arXiv 2601.04052"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2963b6b-f4e6-4209-8a39-0c6d1cc113cf",
  "isSidechain": false,
  "requestId": "req_011CbAa6uHVYSmywN1dLATn2",
  "type": "assistant",
  "uuid": "f5451359-9d11-424b-931c-815e1a7c5571",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015wkdnWUnYuanwkcbRaqRYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 790,
      "cache_read_input_tokens": 52561,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 790,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 52561,
          "cache_creation_input_tokens": 790,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 790
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

_source line 85 · 2026-05-18T19:17:10.522Z_

<details><summary>↩ Tool result · `toolu_01RsodRo3F84f4Aqy9SUn8T6`</summary>

```text
Web search results for query: "Stable Language Guidance VLA modality collapse affordance arXiv 2601.04052"

Links: [{"title":"[2601.04052] Stable Language Guidance for Vision-Language-Action Models","url":"https://arxiv.org/abs/2601.04052"},{"title":"Stable Language Guidance for Vision–Language–Action Models","url":"https://arxiv.org/html/2601.04052v1"},{"title":"Stable Language Guidance for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2601.04052"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"}]

Based on the search results, I found the arXiv paper you're looking for:

**Paper Title:** "Stable Language Guidance for Vision-Language-Action Models" (arXiv:2601.04052)

**Authors:** Zhihao Zhan, Yuhao Chen, Jiaying Zhou, Qinhan Lv, Hao Liu, Keze Wang, Liang Lin, and Guangrun Wang from Sun Yat-sen University

**Key Findings:**

The paper identifies a critical "modality collapse" phenomenon where strong visual priors overwhelm sparse linguistic signals, causing agents to overfit to specific instruction phrasings while ignoring the underlying semantic intent.

**Proposed Solution:**

The authors propose Residual Semantic Steering (RSS), a probabilistic framework that disentangles physical affordance from semantic execution, introducing Monte Carlo Syntactic Integration and Residual Affordance Steering—a dual-stream decoding mechanism that explicitly isolates the causal influence of language by subtracting the visual affordance prior.

**Results:** Empirical results across diverse manipulation benchmarks demonstrate that RSS achieves state-of-the-art robustness, maintaining performance even under adversarial linguistic perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5451359-9d11-424b-931c-815e1a7c5571",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "229f2ce3-a1f6-49b8-8a87-2789e1a649af",
  "toolUseResult": {
    "query": "Stable Language Guidance VLA modality collapse affordance arXiv 2601.04052",
    "results": [
      {
        "tool_use_id": "srvtoolu_012HG2ce6BZhVX1ZdBDa2Sga",
        "content": [
          {
            "title": "[2601.04052] Stable Language Guidance for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2601.04052"
          },
          {
            "title": "Stable Language Guidance for Vision–Language–Action Models",
            "url": "https://arxiv.org/html/2601.04052v1"
          },
          {
            "title": "Stable Language Guidance for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2601.04052"
          },
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance",
            "url": "https://arxiv.org/pdf/2412.20451"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          }
        ]
      },
      "Based on the search results, I found the arXiv paper you're looking for:\n\n**Paper Title:** \"Stable Language Guidance for Vision-Language-Action Models\" (arXiv:2601.04052)\n\n**Authors:** Zhihao Zhan, Yuhao Chen, Jiaying Zhou, Qinhan Lv, Hao Liu, Keze Wang, Liang Lin, and Guangrun Wang from Sun Yat-sen University\n\n**Key Findings:**\n\nThe paper identifies a critical \"modality collapse\" phenomenon where strong visual priors overwhelm sparse linguistic signals, causing agents to overfit to specific instruction phrasings while ignoring the underlying semantic intent.\n\n**Proposed Solution:**\n\nThe authors propose Residual Semantic Steering (RSS), a probabilistic framework that disentangles physical affordance from semantic execution, introducing Monte Carlo Syntactic Integration and Residual Affordance Steering—a dual-stream decoding mechanism that explicitly isolates the causal influence of language by subtracting the visual affordance prior.\n\n**Results:** Empirical results across diverse manipulation benchmarks demonstrate that RSS achieves state-of-the-art robustness, maintaining performance even under adversarial linguistic perturbations."
    ],
    "durationSeconds": 6.713613337000017
  },
  "sourceToolAssistantUUID": "f5451359-9d11-424b-931c-815e1a7c5571",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-18T19:17:14.886Z_

Now let me do the most critical search — verifying whether the specific combination proposed (affordance pseudo-labels from frozen VLMs as auxiliary training signal distilled into VLA intermediate representations) has been done.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "229f2ce3-a1f6-49b8-8a87-2789e1a649af",
  "isSidechain": false,
  "requestId": "req_011CbAa7dE8CuUnsDKnMBUfn",
  "type": "assistant",
  "uuid": "1e2206e9-a599-4537-b07c-13c74771a09f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112QfTCLW1bZruUtTg6ahqv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 53351,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 53351,
          "cache_creation_input_tokens": 618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 618
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

_source line 87 · 2026-05-18T19:17:15.298Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S4cJctmtCCUFFCyNJceNut`</summary>

```json
{
  "query": "affordance prediction auxiliary loss intermediate representation VLA robustness distribution shift 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e2206e9-a599-4537-b07c-13c74771a09f",
  "isSidechain": false,
  "requestId": "req_011CbAa7dE8CuUnsDKnMBUfn",
  "type": "assistant",
  "uuid": "250b9dc2-8c7a-46d2-8300-d2d9ebeff1e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112QfTCLW1bZruUtTg6ahqv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 53351,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 618,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 112,
          "cache_read_input_tokens": 53351,
          "cache_creation_input_tokens": 618,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 618
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

_source line 88_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "250b9dc2-8c7a-46d2-8300-d2d9ebeff1e1",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "ai-title",
  "aiTitle": "AffordVLA: Open-vocabulary affordance distillation into VLA for robust manipulation",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Tool result

_source line 90 · 2026-05-18T19:17:25.360Z_

<details><summary>↩ Tool result · `toolu_01S4cJctmtCCUFFCyNJceNut`</summary>

```text
Web search results for query: "affordance prediction auxiliary loss intermediate representation VLA robustness distribution shift 2026"

Links: [{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"},{"title":"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/pdf/2512.01715"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators","url":"https://arxiv.org/pdf/2510.00406"},{"title":"SA-VLA: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning","url":"https://arxiv.org/pdf/2602.00743"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"}]

I found several recent papers related to your search query. Here are the key findings:

## Recent VLA Research on Robustness and Affordances

Vision-Language-Action models show performance degradation under distribution shifts such as lighting changes, texture variations, or camera angle perturbations. Several approaches are being developed to address this:

**DiG-Flow** - This method uses an auxiliary signal to modulate representation learning as a representation-side intervention that enables robustness to distributional drift.

**Affordance-Based Methods** - RT-Affordance is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation. Additionally, empirical results demonstrate that affordances are robust to novel settings.

**Affordance Field Intervention (AFI)** - This method achieves an average improvement of 23.5% across different VLA backbones under out-of-distribution scenarios on real-world robotic platforms, validating its effectiveness in enhancing VLA robustness to distribution shifts.

**Chain-of-Affordance** - CoA-VLA introduces multiple types of affordances and formulates them as chain-of-thought reasoning to further improve VLA model performance.

These papers are from late 2025 and early 2026, directly addressing the intersection of affordance prediction, intermediate representations, and VLA robustness to distribution shifts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "250b9dc2-8c7a-46d2-8300-d2d9ebeff1e1",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "64baba80-eb8f-4b43-bbb2-79afe6923378",
  "toolUseResult": {
    "query": "affordance prediction auxiliary loss intermediate representation VLA robustness distribution shift 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Kb9sr4tXRsbkoysYECJw6T",
        "content": [
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          },
          {
            "title": "VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview",
            "url": "https://openreview.net/forum?id=Jaut99EHeu"
          },
          {
            "title": "DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://arxiv.org/pdf/2512.01715"
          },
          {
            "title": "VLA-RFT: Vision-Language-Action Reinforcement Fine-tuning with Verified Rewards in World Simulators",
            "url": "https://arxiv.org/pdf/2510.00406"
          },
          {
            "title": "SA-VLA: Spatially-Aware Flow-Matching for Vision-Language-Action Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2602.00743"
          },
          {
            "title": "RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation",
            "url": "https://arxiv.org/pdf/2411.02704"
          },
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance",
            "url": "https://arxiv.org/pdf/2412.20451"
          }
        ]
      },
      "I found several recent papers related to your search query. Here are the key findings:\n\n## Recent VLA Research on Robustness and Affordances\n\nVision-Language-Action models show performance degradation under distribution shifts such as lighting changes, texture variations, or camera angle perturbations. Several approaches are being developed to address this:\n\n**DiG-Flow** - This method uses an auxiliary signal to modulate representation learning as a representation-side intervention that enables robustness to distributional drift.\n\n**Affordance-Based Methods** - RT-Affordance is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation. Additionally, empirical results demonstrate that affordances are robust to novel settings.\n\n**Affordance Field Intervention (AFI)** - This method achieves an average improvement of 23.5% across different VLA backbones under out-of-distribution scenarios on real-world robotic platforms, validating its effectiveness in enhancing VLA robustness to distribution shifts.\n\n**Chain-of-Affordance** - CoA-VLA introduces multiple types of affordances and formulates them as chain-of-thought reasoning to further improve VLA model performance.\n\nThese papers are from late 2025 and early 2026, directly addressing the intersection of affordance prediction, intermediate representations, and VLA robustness to distribution shifts."
    ],
    "durationSeconds": 10.055953295999963
  },
  "sourceToolAssistantUUID": "250b9dc2-8c7a-46d2-8300-d2d9ebeff1e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-18T19:17:27.877Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018H3kVMnMMmGLsCtc5UGD2i`</summary>

```json
{
  "query": "DiG-Flow discrepancy-guided flow matching robust VLA arXiv 2512.01715"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64baba80-eb8f-4b43-bbb2-79afe6923378",
  "isSidechain": false,
  "requestId": "req_011CbAa8igZtWAbLmmLZ86nZ",
  "type": "assistant",
  "uuid": "c804286d-3d0d-49f2-a9a4-263405b9dfe5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBnjHNMLVcwVbxhTru4Jma",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 53969,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 822,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 53969,
          "cache_creation_input_tokens": 822,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 822
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

_source line 92 · 2026-05-18T19:17:35.193Z_

<details><summary>↩ Tool result · `toolu_018H3kVMnMMmGLsCtc5UGD2i`</summary>

```text
Web search results for query: "DiG-Flow discrepancy-guided flow matching robust VLA arXiv 2512.01715"

Links: [{"title":"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/html/2512.01715v1"},{"title":"[2512.01715] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/abs/2512.01715"},{"title":"[Literature Review] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://www.themoonlight.io/en/review/dig-flow-discrepancy-guided-flow-matching-for-robust-vla-models"},{"title":"[Quick Review] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://liner.com/review/digflow-discrepancyguided-flow-matching-for-robust-vla-models"},{"title":"GitHub - BeingBeyond/DiG-Flow: DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://github.com/BeingBeyond/DiG-Flow"},{"title":"DiG-Flow","url":"https://beingbeyond.github.io/DiG-Flow/"},{"title":"BeingBeyond ∝ DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/pdf/2512.01715"},{"title":"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models - Takara TLDR | Takara TLDR","url":"https://tldr.takara.ai/p/2512.01715"},{"title":"Training-Free Refinement of Flow Matching with Divergence-based Sampling","url":"https://arxiv.org/pdf/2604.04646"},{"title":"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation","url":"https://arxiv.org/pdf/2604.05656"}]

I found comprehensive information about DiG-Flow. Here's what the paper is about:

## Overview

DiG-Flow is a principled framework that enhances VLA (Vision-Language-Action) robustness through geometric regularization. Vision-Language-Action models trained with flow matching have demonstrated impressive capabilities on robotic manipulation tasks.

## Problem Statement

VLA model performance often degrades under distribution shift and on complex multi-step tasks, suggesting that the learned representations may not robustly capture task-relevant semantics.

## Core Approach

The key insight is that the distributional discrepancy between observation and action embeddings provides a meaningful geometric signal: lower transport cost indicates compatible representations, while higher cost suggests potential misalignment. The core methodology revolves around three principal components: a discrepancy function, a monotone weight mapping, and a lightweight residual operator, integrated into existing VLA architectures.

## Technical Details

DiG-Flow is a plug-and-play module for flow-matching based VLAs that rebalances control between the autoregressive foundation model and the flow expert. It embeds model inputs and flow outputs into a unified discrepancy space and uses this signal to gate the flow path, preventing shortcut transports that bypass the pretrained model.

## Results

DiG-Flow excels on long-horizon tasks. By forcing the foundation model to play a more active role in action generation, it better coordinates the slow reasoning system with the fast controller system, leading to stronger long-horizon performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c804286d-3d0d-49f2-a9a4-263405b9dfe5",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "abb82762-47d1-4395-acb1-ecd59737edc3",
  "toolUseResult": {
    "query": "DiG-Flow discrepancy-guided flow matching robust VLA arXiv 2512.01715",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XpQUVp63pnKNVrP8M97TYx",
        "content": [
          {
            "title": "DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://arxiv.org/html/2512.01715v1"
          },
          {
            "title": "[2512.01715] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://arxiv.org/abs/2512.01715"
          },
          {
            "title": "[Literature Review] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://www.themoonlight.io/en/review/dig-flow-discrepancy-guided-flow-matching-for-robust-vla-models"
          },
          {
            "title": "[Quick Review] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://liner.com/review/digflow-discrepancyguided-flow-matching-for-robust-vla-models"
          },
          {
            "title": "GitHub - BeingBeyond/DiG-Flow: DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://github.com/BeingBeyond/DiG-Flow"
          },
          {
            "title": "DiG-Flow",
            "url": "https://beingbeyond.github.io/DiG-Flow/"
          },
          {
            "title": "BeingBeyond ∝ DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models",
            "url": "https://arxiv.org/pdf/2512.01715"
          },
          {
            "title": "DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models - Takara TLDR | Takara TLDR",
            "url": "https://tldr.takara.ai/p/2512.01715"
          },
          {
            "title": "Training-Free Refinement of Flow Matching with Divergence-based Sampling",
            "url": "https://arxiv.org/pdf/2604.04646"
          },
          {
            "title": "SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation",
            "url": "https://arxiv.org/pdf/2604.05656"
          }
        ]
      },
      "I found comprehensive information about DiG-Flow. Here's what the paper is about:\n\n## Overview\n\nDiG-Flow is a principled framework that enhances VLA (Vision-Language-Action) robustness through geometric regularization. Vision-Language-Action models trained with flow matching have demonstrated impressive capabilities on robotic manipulation tasks.\n\n## Problem Statement\n\nVLA model performance often degrades under distribution shift and on complex multi-step tasks, suggesting that the learned representations may not robustly capture task-relevant semantics.\n\n## Core Approach\n\nThe key insight is that the distributional discrepancy between observation and action embeddings provides a meaningful geometric signal: lower transport cost indicates compatible representations, while higher cost suggests potential misalignment. The core methodology revolves around three principal components: a discrepancy function, a monotone weight mapping, and a lightweight residual operator, integrated into existing VLA architectures.\n\n## Technical Details\n\nDiG-Flow is a plug-and-play module for flow-matching based VLAs that rebalances control between the autoregressive foundation model and the flow expert. It embeds model inputs and flow outputs into a unified discrepancy space and uses this signal to gate the flow path, preventing shortcut transports that bypass the pretrained model.\n\n## Results\n\nDiG-Flow excels on long-horizon tasks. By forcing the foundation model to play a more active role in action generation, it better coordinates the slow reasoning system with the fast controller system, leading to stronger long-horizon performance."
    ],
    "durationSeconds": 7.312211155999976
  },
  "sourceToolAssistantUUID": "c804286d-3d0d-49f2-a9a4-263405b9dfe5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 93 · 2026-05-18T19:17:38.081Z_

Now let me check the probing study and context-dependency study that the proposal references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abb82762-47d1-4395-acb1-ecd59737edc3",
  "isSidechain": false,
  "requestId": "req_011CbAa9ShvDDnACZrv6v1yE",
  "type": "assistant",
  "uuid": "2f4fb2b4-e403-42cc-84b8-5545b885f226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTzEaCwNtCq6RjhNuoLMmg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 971,
      "cache_read_input_tokens": 54791,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 54791,
          "cache_creation_input_tokens": 971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 971
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

_source line 94 · 2026-05-18T19:17:38.798Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EnXbZeUSJzq1axbUiFiS7F`</summary>

```json
{
  "query": "probing affordance vision foundation models DINOv2 geometry interaction arXiv 2602.20501"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f4fb2b4-e403-42cc-84b8-5545b885f226",
  "isSidechain": false,
  "requestId": "req_011CbAa9ShvDDnACZrv6v1yE",
  "type": "assistant",
  "uuid": "cf004e40-230a-4791-8663-f0ee43c90b70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XTzEaCwNtCq6RjhNuoLMmg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 971,
      "cache_read_input_tokens": 54791,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 54791,
          "cache_creation_input_tokens": 971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 971
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

_source line 95 · 2026-05-18T19:17:45.463Z_

<details><summary>↩ Tool result · `toolu_01EnXbZeUSJzq1axbUiFiS7F`</summary>

```text
Web search results for query: "probing affordance vision foundation models DINOv2 geometry interaction arXiv 2602.20501"

Links: [{"title":"[2602.20501] Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models","url":"https://arxiv.org/abs/2602.20501"},{"title":"Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models","url":"https://arxiv.org/pdf/2602.20501"},{"title":"Probing and Bridging Geometry–Interaction Cues for Affordance Reasoning in Vision Foundation Models","url":"https://arxiv.org/html/2602.20501"},{"title":"Do Foundation Models Know Geometry? Probing Frozen Features for Continuous Physical Measurement","url":"https://arxiv.org/pdf/2603.06459"},{"title":"Lexicon3D: Probing Visual Foundation Models for Complex 3D Scene   Understanding","url":"https://arxiv.org/pdf/2409.03757"}]

I found the paper you're looking for! Here's information about arXiv 2602.20501:

**Title:** Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models

**Authors:** Qing Zhang, Xuesong Li, and Jing Zhang (The Australian National University and CSIRO)

**Main Contribution:** The paper argues that understanding affordance hinges on two complementary capacities: geometric perception, which identifies the structural parts of objects that enable interaction, and interaction perception, which models how an agent's actions engage with those parts. To test this hypothesis, they conduct a systematic probing of Visual Foundation Models (VFMs).

**Key Findings:** Models like DINO inherently encode part-level geometric structures, while generative models like Flux contain rich, verb-conditioned spatial attention maps that serve as implicit interaction priors. By simply fusing DINO's geometric prototypes with Flux's interaction maps in a training-free and zero-shot manner, they achieve affordance estimation competitive with weakly-supervised methods.

The paper was published on March 16, 2026, and provides insights into how different vision foundation models encode geometric and interactive information relevant to understanding object affordances.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf004e40-230a-4791-8663-f0ee43c90b70",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "40868584-a237-4b86-80f0-f8112bf25d11",
  "toolUseResult": {
    "query": "probing affordance vision foundation models DINOv2 geometry interaction arXiv 2602.20501",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QiHV7DsiQk3dDkBHMYiQee",
        "content": [
          {
            "title": "[2602.20501] Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models",
            "url": "https://arxiv.org/abs/2602.20501"
          },
          {
            "title": "Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models",
            "url": "https://arxiv.org/pdf/2602.20501"
          },
          {
            "title": "Probing and Bridging Geometry–Interaction Cues for Affordance Reasoning in Vision Foundation Models",
            "url": "https://arxiv.org/html/2602.20501"
          },
          {
            "title": "Do Foundation Models Know Geometry? Probing Frozen Features for Continuous Physical Measurement",
            "url": "https://arxiv.org/pdf/2603.06459"
          },
          {
            "title": "Lexicon3D: Probing Visual Foundation Models for Complex 3D Scene   Understanding",
            "url": "https://arxiv.org/pdf/2409.03757"
          }
        ]
      },
      "I found the paper you're looking for! Here's information about arXiv 2602.20501:\n\n**Title:** Probing and Bridging Geometry-Interaction Cues for Affordance Reasoning in Vision Foundation Models\n\n**Authors:** Qing Zhang, Xuesong Li, and Jing Zhang (The Australian National University and CSIRO)\n\n**Main Contribution:** The paper argues that understanding affordance hinges on two complementary capacities: geometric perception, which identifies the structural parts of objects that enable interaction, and interaction perception, which models how an agent's actions engage with those parts. To test this hypothesis, they conduct a systematic probing of Visual Foundation Models (VFMs).\n\n**Key Findings:** Models like DINO inherently encode part-level geometric structures, while generative models like Flux contain rich, verb-conditioned spatial attention maps that serve as implicit interaction priors. By simply fusing DINO's geometric prototypes with Flux's interaction maps in a training-free and zero-shot manner, they achieve affordance estimation competitive with weakly-supervised methods.\n\nThe paper was published on March 16, 2026, and provides insights into how different vision foundation models encode geometric and interactive information relevant to understanding object affordances."
    ],
    "durationSeconds": 6.660500915000041
  },
  "sourceToolAssistantUUID": "cf004e40-230a-4791-8663-f0ee43c90b70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 96 · 2026-05-18T19:17:45.466Z_

```json
{
  "parentUuid": "40868584-a237-4b86-80f0-f8112bf25d11",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e32e3558-9776-4f9d-b0c3-2c8e284fe164",
  "timestamp": "2026-05-18T19:17:45.466Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 97 · 2026-05-18T19:17:48.405Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NtmdAjbj1KVpAmH75L5sM4`</summary>

```json
{
  "query": "context-dependent affordance vision language models arXiv 2603.04419 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e32e3558-9776-4f9d-b0c3-2c8e284fe164",
  "isSidechain": false,
  "requestId": "req_011CbAaACbNdbuf87hKtAScB",
  "type": "assistant",
  "uuid": "cdf4caec-3df4-4fe6-be0d-de1400dbc132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YCG3tjwtj4UprPsPx5PPco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 55762,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 55762,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 770
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

_source line 98 · 2026-05-18T19:17:55.846Z_

<details><summary>↩ Tool result · `toolu_01NtmdAjbj1KVpAmH75L5sM4`</summary>

```text
Web search results for query: "context-dependent affordance vision language models arXiv 2603.04419 2026"

Links: [{"title":"[2603.04419] Context-Dependent Affordance Computation in Vision-Language Models","url":"https://arxiv.org/abs/2603.04419"},{"title":"Context-Dependent Affordance Computation in Vision-Language Models","url":"https://arxiv.org/pdf/2603.04419"},{"title":"Acknowledgements","url":"https://arxiv.org/html/2603.04419"},{"title":"AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://arxiv.org/pdf/2401.06341"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"Affordance Perception by a Knowledge-Guided Vision-Language Model with   Efficient Error Correction","url":"https://arxiv.org/pdf/2407.13368"}]

I found the paper you were looking for! Here are the key details about arXiv paper 2603.04419:

**Title:** Context-Dependent Affordance Computation in Vision-Language Models

**Author:** Murad Farzulla (Dissensus AI and King's College London)

**Publication Date:** February 14, 2026

**Main Findings:**

The study examined 3,213 scene-context pairs from COCO-2017 using Qwen-VL 30B and LLaVA-1.5-13B models across 7 agentic personas, demonstrating massive affordance drift with a mean Jaccard similarity of 0.095 between context conditions, indicating that over 90% of lexical scene description is context-dependent. Sentence-level cosine similarity confirms substantial drift at the semantic level at 58.5% context-dependent.

**Key Technical Results:**

Tucker decomposition with bootstrap stability analysis revealed stable orthogonal latent factors: a "Culinary Manifold" isolated to chef contexts and an "Access Axis" spanning child-mobility contrasts.

**Implications:** These findings suggest a direction for robotics research: dynamic, query-dependent ontological projection (JIT Ontology) rather than static world modeling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cdf4caec-3df4-4fe6-be0d-de1400dbc132",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "fad794fd-2324-4e2a-8b8f-eef78a622500",
  "toolUseResult": {
    "query": "context-dependent affordance vision language models arXiv 2603.04419 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016mksXGVhrbnxxzRwyKhfN9",
        "content": [
          {
            "title": "[2603.04419] Context-Dependent Affordance Computation in Vision-Language Models",
            "url": "https://arxiv.org/abs/2603.04419"
          },
          {
            "title": "Context-Dependent Affordance Computation in Vision-Language Models",
            "url": "https://arxiv.org/pdf/2603.04419"
          },
          {
            "title": "Acknowledgements",
            "url": "https://arxiv.org/html/2603.04419"
          },
          {
            "title": "AffordanceLLM: Grounding Affordance from Vision Language Models",
            "url": "https://arxiv.org/pdf/2401.06341"
          },
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance",
            "url": "https://arxiv.org/pdf/2412.20451"
          },
          {
            "title": "Affordance Perception by a Knowledge-Guided Vision-Language Model with   Efficient Error Correction",
            "url": "https://arxiv.org/pdf/2407.13368"
          }
        ]
      },
      "I found the paper you were looking for! Here are the key details about arXiv paper 2603.04419:\n\n**Title:** Context-Dependent Affordance Computation in Vision-Language Models\n\n**Author:** Murad Farzulla (Dissensus AI and King's College London)\n\n**Publication Date:** February 14, 2026\n\n**Main Findings:**\n\nThe study examined 3,213 scene-context pairs from COCO-2017 using Qwen-VL 30B and LLaVA-1.5-13B models across 7 agentic personas, demonstrating massive affordance drift with a mean Jaccard similarity of 0.095 between context conditions, indicating that over 90% of lexical scene description is context-dependent. Sentence-level cosine similarity confirms substantial drift at the semantic level at 58.5% context-dependent.\n\n**Key Technical Results:**\n\nTucker decomposition with bootstrap stability analysis revealed stable orthogonal latent factors: a \"Culinary Manifold\" isolated to chef contexts and an \"Access Axis\" spanning child-mobility contrasts.\n\n**Implications:** These findings suggest a direction for robotics research: dynamic, query-dependent ontological projection (JIT Ontology) rather than static world modeling."
    ],
    "durationSeconds": 7.436705388000002
  },
  "sourceToolAssistantUUID": "cdf4caec-3df4-4fe6-be0d-de1400dbc132",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 99 · 2026-05-18T19:17:59.437Z_

Good — both papers verified as real. Now let me do the most critical competitive search: check if anyone has published something very close to AffordVLA in the last 3 months.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fad794fd-2324-4e2a-8b8f-eef78a622500",
  "isSidechain": false,
  "requestId": "req_011CbAaAxx7u2cVEoBumrVLJ",
  "type": "assistant",
  "uuid": "d3c42d81-50f1-43af-a0e3-2729ef30a935",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WpE2TUSKaxviNszLqTCYAE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 56532,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 56532,
          "cache_creation_input_tokens": 656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 656
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

_source line 100 · 2026-05-18T19:18:00.334Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VHkdcdA6nESeHxZy7MzmGC`</summary>

```json
{
  "query": "affordance grounded VLA representation learning pseudo label distillation robot 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3c42d81-50f1-43af-a0e3-2729ef30a935",
  "isSidechain": false,
  "requestId": "req_011CbAaAxx7u2cVEoBumrVLJ",
  "type": "assistant",
  "uuid": "b18cf8e6-8344-4eb0-b2e5-dd293980219e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WpE2TUSKaxviNszLqTCYAE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 56532,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 656,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 111,
          "cache_read_input_tokens": 56532,
          "cache_creation_input_tokens": 656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 656
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

_source line 101 · 2026-05-18T19:18:09.285Z_

<details><summary>↩ Tool result · `toolu_01VHkdcdA6nESeHxZy7MzmGC`</summary>

```text
Web search results for query: "affordance grounded VLA representation learning pseudo label distillation robot 2026 arxiv"

Links: [{"title":"[2603.22760] SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/abs/2603.22760"},{"title":"Parallels Between VLA Model Post-Training and Human ...","url":"https://arxiv.org/pdf/2506.20966"},{"title":"Learning to Label Affordances from Simulated and Real Data","url":"https://arxiv.org/pdf/1709.08872"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/pdf/2603.22760"},{"title":"HRP: Human Affordances for Robotic Pre-Training","url":"https://arxiv.org/pdf/2407.18911"},{"title":"Contrastive Representation Regularization for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.01711"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"GitHub - yueen-ma/Awesome-VLA · GitHub","url":"https://github.com/yueen-ma/awesome-vla"}]

Based on the web search results, I found several relevant papers on Vision-Language-Action (VLA) models for robotic manipulation that incorporate affordance learning and representation learning techniques:

## Key Results:

**SG-VLA: Spatially-Grounded Vision-Language-Action Models** - The most directly relevant result. This approach co-trains auxiliary decoders that reconstruct interpretable intermediate signals including global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks from shared visual-language features, providing dense supervision that encourages the backbone to develop spatially grounded, manipulation-aware latent representations. The findings suggest that spatial grounding through auxiliary and multi-modal learning provides a strong direction for scaling VLA models toward general-purpose domestic robots.

**HRP (Human Affordances for Robotic Pre-Training)** - This semi-supervised pipeline learns effective robotic representations from human video by extracting hand-object "affordance" information from human videos using off-the-shelf tracking models, then distilling these affordances into a pre-existing representation network before the policy fine-tuning stage.

**Contrastive Representation Regularization** - This approach aligns representations more closely with the robot's proprioceptive states by using relative distances between states as soft supervision, complementing the original action prediction objective to enhance control-relevant representation learning.

**Affordance Field Intervention (AFI)** - This lightweight hybrid framework uses Spatial Affordance Fields (SAFs) as an on-demand plugin to guide VLA behavior, detecting memory traps through proprioception and repositioning the robot to recent high-affordance regions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b18cf8e6-8344-4eb0-b2e5-dd293980219e",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "201dc015-6061-4260-819c-923cba041ada",
  "toolUseResult": {
    "query": "affordance grounded VLA representation learning pseudo label distillation robot 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QkRcYm5mmbJTP6GpYEqbXh",
        "content": [
          {
            "title": "[2603.22760] SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/abs/2603.22760"
          },
          {
            "title": "Parallels Between VLA Model Post-Training and Human ...",
            "url": "https://arxiv.org/pdf/2506.20966"
          },
          {
            "title": "Learning to Label Affordances from Simulated and Real Data",
            "url": "https://arxiv.org/pdf/1709.08872"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/pdf/2603.22760"
          },
          {
            "title": "HRP: Human Affordances for Robotic Pre-Training",
            "url": "https://arxiv.org/pdf/2407.18911"
          },
          {
            "title": "Contrastive Representation Regularization for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2510.01711"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          },
          {
            "title": "GitHub - yueen-ma/Awesome-VLA · GitHub",
            "url": "https://github.com/yueen-ma/awesome-vla"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers on Vision-Language-Action (VLA) models for robotic manipulation that incorporate affordance learning and representation learning techniques:\n\n## Key Results:\n\n**SG-VLA: Spatially-Grounded Vision-Language-Action Models** - The most directly relevant result. This approach co-trains auxiliary decoders that reconstruct interpretable intermediate signals including global robot position, joint configurations, grasp affordances, target-object relative pose, and segmentation masks from shared visual-language features, providing dense supervision that encourages the backbone to develop spatially grounded, manipulation-aware latent representations. The findings suggest that spatial grounding through auxiliary and multi-modal learning provides a strong direction for scaling VLA models toward general-purpose domestic robots.\n\n**HRP (Human Affordances for Robotic Pre-Training)** - This semi-supervised pipeline learns effective robotic representations from human video by extracting hand-object \"affordance\" information from human videos using off-the-shelf tracking models, then distilling these affordances into a pre-existing representation network before the policy fine-tuning stage.\n\n**Contrastive Representation Regularization** - This approach aligns representations more closely with the robot's proprioceptive states by using relative distances between states as soft supervision, complementing the original action prediction objective to enhance control-relevant representation learning.\n\n**Affordance Field Intervention (AFI)** - This lightweight hybrid framework uses Spatial Affordance Fields (SAFs) as an on-demand plugin to guide VLA behavior, detecting memory traps through proprioception and repositioning the robot to recent high-affordance regions."
    ],
    "durationSeconds": 8.945360134999966
  },
  "sourceToolAssistantUUID": "b18cf8e6-8344-4eb0-b2e5-dd293980219e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 102_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "201dc015-6061-4260-819c-923cba041ada",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 103_

```json
{
  "type": "ai-title",
  "aiTitle": "AffordVLA: Open-vocabulary affordance distillation into VLA for robust manipulation",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Assistant

_source line 104 · 2026-05-18T19:18:12.706Z_

Very important find — **HRP (Human Affordances for Robotic Pre-Training)** distills affordance information from human videos into representation networks before policy fine-tuning. This is conceptually similar. Let me examine it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "201dc015-6061-4260-819c-923cba041ada",
  "isSidechain": false,
  "requestId": "req_011CbAaBxV7pMsc9jdycaqNC",
  "type": "assistant",
  "uuid": "1c35460f-fac6-4940-9da0-7b1294fef628",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fv62euUX1oxzUB2nYTtHcw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 57188,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 859,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 57188,
          "cache_creation_input_tokens": 859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 859
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

_source line 105 · 2026-05-18T19:18:14.452Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01D5PdzcRry8AjHXFoSiFpxL`</summary>

```json
{
  "url": "https://arxiv.org/abs/2407.18911",
  "prompt": "Extract the full abstract. What is the method exactly? Does it distill affordance knowledge into representations used by a policy? How does it generate affordance labels? Is it end-to-end or two-stage? What model is it built on?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c35460f-fac6-4940-9da0-7b1294fef628",
  "isSidechain": false,
  "requestId": "req_011CbAaBxV7pMsc9jdycaqNC",
  "type": "assistant",
  "uuid": "45358e0b-db1a-4a13-b04c-9e3ace50ff18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fv62euUX1oxzUB2nYTtHcw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 859,
      "cache_read_input_tokens": 57188,
      "output_tokens": 185,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 859,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 185,
          "cache_read_input_tokens": 57188,
          "cache_creation_input_tokens": 859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 859
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

_source line 106 · 2026-05-18T19:18:19.837Z_

<details><summary>↩ Tool result · `toolu_01D5PdzcRry8AjHXFoSiFpxL`</summary>

```text
# HRP: Human Affordances for Robotic Pre-Training - Analysis

## Full Abstract

The paper proposes using internet-scale human videos to extract affordances at the environment and agent level, then distill them into pre-trained representations. The approach fine-tunes existing representations using "hand, object, and contact affordance labels" automatically extracted from human video data with off-the-shelf computer vision modules. Testing on 3000+ robot trials across five real-world tasks shows minimum 15% performance improvements across three robot morphologies and camera views.

## Method Overview

**Affordance Label Generation:** "automatically extracted from human video data (with the help of off-the-shelf computer vision modules)" — This indicates a two-stage pipeline where standard CV tools identify relevant features in human videos.

**Training Approach:** The method is **two-stage**: affordance labels are first extracted from human videos, then used to fine-tune existing vision representations.

**Integration with Policy:** The abstract indicates affordance knowledge enhances the representation itself (the vision network), which the policy then uses to "predict optimal actions given high dimensional vision inputs."

**Base Model:** The paper emphasizes that the approach "can efficiently fine-tune *any* existing representation," suggesting it's representation-agnostic rather than built on a specific model architecture.

The core innovation centers on leveraging human video as a scalable data source to improve robotic perception through structured affordance supervision.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45358e0b-db1a-4a13-b04c-9e3ace50ff18",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "957af676-0185-4120-84e3-56e01d425c49",
  "toolUseResult": {
    "bytes": 47353,
    "code": 200,
    "codeText": "OK",
    "result": "# HRP: Human Affordances for Robotic Pre-Training - Analysis\n\n## Full Abstract\n\nThe paper proposes using internet-scale human videos to extract affordances at the environment and agent level, then distill them into pre-trained representations. The approach fine-tunes existing representations using \"hand, object, and contact affordance labels\" automatically extracted from human video data with off-the-shelf computer vision modules. Testing on 3000+ robot trials across five real-world tasks shows minimum 15% performance improvements across three robot morphologies and camera views.\n\n## Method Overview\n\n**Affordance Label Generation:** \"automatically extracted from human video data (with the help of off-the-shelf computer vision modules)\" — This indicates a two-stage pipeline where standard CV tools identify relevant features in human videos.\n\n**Training Approach:** The method is **two-stage**: affordance labels are first extracted from human videos, then used to fine-tune existing vision representations.\n\n**Integration with Policy:** The abstract indicates affordance knowledge enhances the representation itself (the vision network), which the policy then uses to \"predict optimal actions given high dimensional vision inputs.\"\n\n**Base Model:** The paper emphasizes that the approach \"can efficiently fine-tune *any* existing representation,\" suggesting it's representation-agnostic rather than built on a specific model architecture.\n\nThe core innovation centers on leveraging human video as a scalable data source to improve robotic perception through structured affordance supervision.",
    "durationMs": 5380,
    "url": "https://arxiv.org/abs/2407.18911"
  },
  "sourceToolAssistantUUID": "45358e0b-db1a-4a13-b04c-9e3ace50ff18",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 107 · 2026-05-18T19:18:23.929Z_

HRP is two-stage (affordance pre-training then policy), not end-to-end with a VLA. Different enough. Now let me check one more critical thing — whether any very recent (Apr-May 2026) work has been published on this exact topic.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "957af676-0185-4120-84e3-56e01d425c49",
  "isSidechain": false,
  "requestId": "req_011CbAaCmDyn8iYYFEXiTezn",
  "type": "assistant",
  "uuid": "aa3fc57f-d6c7-4d02-bb9e-91769cdb836a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WPaGXLLFkevmw87M8CBbv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 58047,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 58047,
          "cache_creation_input_tokens": 506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 506
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

_source line 108 · 2026-05-18T19:18:24.301Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AiDuToidoQvEtiTXBjRJft`</summary>

```json
{
  "query": "affordance VLA auxiliary training robust manipulation April May 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa3fc57f-d6c7-4d02-bb9e-91769cdb836a",
  "isSidechain": false,
  "requestId": "req_011CbAaCmDyn8iYYFEXiTezn",
  "type": "assistant",
  "uuid": "5277d7b8-2dfb-4b9b-9703-60cc46dab46b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015WPaGXLLFkevmw87M8CBbv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 58047,
      "output_tokens": 128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 506,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 128,
          "cache_read_input_tokens": 58047,
          "cache_creation_input_tokens": 506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 506
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

_source line 109 · 2026-05-18T19:18:31.777Z_

<details><summary>↩ Tool result · `toolu_01AiDuToidoQvEtiTXBjRJft`</summary>

```text
Web search results for query: "affordance VLA auxiliary training robust manipulation April May 2026 arXiv"

Links: [{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation","url":"https://arxiv.org/html/2411.02704v1"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/html/2603.22760"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/pdf/2512.07472"},{"title":"SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation","url":"https://arxiv.org/pdf/2603.22760"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation","url":"https://arxiv.org/html/2512.07472v1"},{"title":"Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in","url":"https://www.arxiv.org/pdf/2512.07472"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation","url":"https://arxiv.org/pdf/2411.02704"}]

I found several relevant papers on arXiv related to affordances, VLAs (Vision-Language-Action models), and robotic manipulation. Here are the key results:

1. **SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation** - This work introduces a framework for learning spatially-grounded VLA models that strengthens both perception and representation learning through auxiliary task co-training and multi-modal input enhancement. This paper was published on March 24, 2026.

2. **RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation** - This paper trains a dedicated VLA for affordance prediction, trained on web data, affordances extracted from robot trajectories, and in-domain affordance images. Published November 5, 2024.

3. **Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation** - This method achieves an average improvement of 23.5% across different VLA backbones under out-of-distribution scenarios on real-world robotic platforms, and 20.2% on the LIBERO-Pro benchmark, validating its effectiveness in enhancing VLA robustness to distribution shifts. Published December 8, 2025.

4. **CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance** - This paper prompts the model to consider four types of affordances before taking action, and transforms each affordance into two prompting formats: visual affordance and textual affordance. Published July 31, 2025.

The SG-VLA paper from March 2026 most closely matches your search criteria, specifically addressing auxiliary training for robust manipulation in VLAs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5277d7b8-2dfb-4b9b-9703-60cc46dab46b",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "e8883b49-5acb-42f9-a28c-dcf054c897d4",
  "toolUseResult": {
    "query": "affordance VLA auxiliary training robust manipulation April May 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_015nkRvJqcuWDyKqhzXJz9VP",
        "content": [
          {
            "title": "RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation",
            "url": "https://arxiv.org/html/2411.02704v1"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/html/2603.22760"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/pdf/2512.07472"
          },
          {
            "title": "SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation",
            "url": "https://arxiv.org/pdf/2603.22760"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation",
            "url": "https://arxiv.org/html/2512.07472v1"
          },
          {
            "title": "Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in",
            "url": "https://www.arxiv.org/pdf/2512.07472"
          },
          {
            "title": "[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance",
            "url": "https://arxiv.org/abs/2412.20451"
          },
          {
            "title": "RT-Affordance: Affordances are Versatile Intermediate Representations   for Robot Manipulation",
            "url": "https://arxiv.org/pdf/2411.02704"
          }
        ]
      },
      "I found several relevant papers on arXiv related to affordances, VLAs (Vision-Language-Action models), and robotic manipulation. Here are the key results:\n\n1. **SG-VLA: Learning Spatially-Grounded Vision-Language-Action Models for Mobile Manipulation** - This work introduces a framework for learning spatially-grounded VLA models that strengthens both perception and representation learning through auxiliary task co-training and multi-modal input enhancement. This paper was published on March 24, 2026.\n\n2. **RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation** - This paper trains a dedicated VLA for affordance prediction, trained on web data, affordances extracted from robot trajectories, and in-domain affordance images. Published November 5, 2024.\n\n3. **Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation** - This method achieves an average improvement of 23.5% across different VLA backbones under out-of-distribution scenarios on real-world robotic platforms, and 20.2% on the LIBERO-Pro benchmark, validating its effectiveness in enhancing VLA robustness to distribution shifts. Published December 8, 2025.\n\n4. **CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance** - This paper prompts the model to consider four types of affordances before taking action, and transforms each affordance into two prompting formats: visual affordance and textual affordance. Published July 31, 2025.\n\nThe SG-VLA paper from March 2026 most closely matches your search criteria, specifically addressing auxiliary training for robust manipulation in VLAs."
    ],
    "durationSeconds": 7.473499043999997
  },
  "sourceToolAssistantUUID": "5277d7b8-2dfb-4b9b-9703-60cc46dab46b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-18T19:18:34.707Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WArLZAJjxWpqENxAypeRpr`</summary>

```json
{
  "query": "VLA open vocabulary affordance zero-shot generalization unseen objects 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8883b49-5acb-42f9-a28c-dcf054c897d4",
  "isSidechain": false,
  "requestId": "req_011CbAaDcf4pQeGQ8khm4rbi",
  "type": "assistant",
  "uuid": "99e699bf-3056-43d8-8c3a-3d6baaaba82b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qDJ3Q3g5U5UNHEpmhgLU1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 963,
      "cache_read_input_tokens": 58553,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 963,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 58553,
          "cache_creation_input_tokens": 963,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 963
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

_source line 111 · 2026-05-18T19:18:42.082Z_

<details><summary>↩ Tool result · `toolu_01WArLZAJjxWpqENxAypeRpr`</summary>

```text
Web search results for query: "VLA open vocabulary affordance zero-shot generalization unseen objects 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=yngvAamNQi"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/pdf/2412.20451"},{"title":"VLA-R1: Enhancing Reasoning in Vision-Language-Action Models Angen Ye12∗","url":"https://arxiv.org/pdf/2510.01623"},{"title":"Open-Vocabulary Affordance Detection in 3D Point Clouds","url":"https://arxiv.org/pdf/2303.02401"},{"title":"VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation","url":"https://arxiv.org/pdf/2510.14902"},{"title":"One-Shot Open Affordance Learning with Foundation Models","url":"https://arxiv.org/pdf/2311.17776"},{"title":"DexGraspVLA: A Vision-Language-Action Framework Towards General","url":"https://arxiv.org/pdf/2502.20900"},{"title":"Benchmarking Affordance Generalization with BusyBox","url":"https://arxiv.org/pdf/2602.05441"},{"title":"GeneralVLA: Generalizable Vision–Language–Action Models with Knowledge-Guided Trajectory Planning","url":"https://arxiv.org/html/2602.04315"},{"title":"OVAL-Grasp: Open-Vocabulary Affordance Localization for Task Oriented Grasping","url":"https://arxiv.org/pdf/2511.20841"}]

I found several relevant research papers on Vision-Language-Action (VLA) models with open vocabulary affordance understanding and zero-shot generalization to unseen objects from 2026. Here are the key findings:

## Recent VLA Research (2026)

**FSD - Affordance-Based VLA:**
FSD is an enhanced affordance-based VLA that generalizes effectively to new instructions and scenes through its reasoning abilities. FSD adopts a reasoning-driven paradigm, leveraging the VLM's general world knowledge for visual aids generation, thereby enhancing zero-shot generalization.

**CoA-VLA:**
CoA-VLA exhibits strong generalization capabilities, including recognizing unseen object poses, identifying free space, and avoiding obstacles in novel environments.

**DexGraspVLA:**
DexGraspVLA is a hierarchical VLA framework that reaches a 90+% dexterous grasping success rate under thousands of unseen cluttered scenes in a "zero-shot" environment.

**GeneralVLA:**
GeneralVLA is a hierarchical vision-language-action model that can be more effective in utilizing the generalization of foundation models, enabling zero-shot manipulation.

**OVAL-Grasp:**
OVAL-Grasp is a zero-shot open-vocabulary approach to task-oriented, affordance based grasping that uses large-language models (LLM) and vision-language models (VLM) to allow a robot to grasp objects at the correct part according to a given task.

These models represent the current state-of-the-art in addressing generalization challenges for VLAs on unseen objects and novel scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99e699bf-3056-43d8-8c3a-3d6baaaba82b",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "a9097ab5-f639-4e3a-a5fa-1e27e1208222",
  "toolUseResult": {
    "query": "VLA open vocabulary affordance zero-shot generalization unseen objects 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QhBGi4xJxqMxomwW6ZRRsC",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf?id=yngvAamNQi"
          },
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance",
            "url": "https://arxiv.org/pdf/2412.20451"
          },
          {
            "title": "VLA-R1: Enhancing Reasoning in Vision-Language-Action Models Angen Ye12∗",
            "url": "https://arxiv.org/pdf/2510.01623"
          },
          {
            "title": "Open-Vocabulary Affordance Detection in 3D Point Clouds",
            "url": "https://arxiv.org/pdf/2303.02401"
          },
          {
            "title": "VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation",
            "url": "https://arxiv.org/pdf/2510.14902"
          },
          {
            "title": "One-Shot Open Affordance Learning with Foundation Models",
            "url": "https://arxiv.org/pdf/2311.17776"
          },
          {
            "title": "DexGraspVLA: A Vision-Language-Action Framework Towards General",
            "url": "https://arxiv.org/pdf/2502.20900"
          },
          {
            "title": "Benchmarking Affordance Generalization with BusyBox",
            "url": "https://arxiv.org/pdf/2602.05441"
          },
          {
            "title": "GeneralVLA: Generalizable Vision–Language–Action Models with Knowledge-Guided Trajectory Planning",
            "url": "https://arxiv.org/html/2602.04315"
          },
          {
            "title": "OVAL-Grasp: Open-Vocabulary Affordance Localization for Task Oriented Grasping",
            "url": "https://arxiv.org/pdf/2511.20841"
          }
        ]
      },
      "I found several relevant research papers on Vision-Language-Action (VLA) models with open vocabulary affordance understanding and zero-shot generalization to unseen objects from 2026. Here are the key findings:\n\n## Recent VLA Research (2026)\n\n**FSD - Affordance-Based VLA:**\nFSD is an enhanced affordance-based VLA that generalizes effectively to new instructions and scenes through its reasoning abilities. FSD adopts a reasoning-driven paradigm, leveraging the VLM's general world knowledge for visual aids generation, thereby enhancing zero-shot generalization.\n\n**CoA-VLA:**\nCoA-VLA exhibits strong generalization capabilities, including recognizing unseen object poses, identifying free space, and avoiding obstacles in novel environments.\n\n**DexGraspVLA:**\nDexGraspVLA is a hierarchical VLA framework that reaches a 90+% dexterous grasping success rate under thousands of unseen cluttered scenes in a \"zero-shot\" environment.\n\n**GeneralVLA:**\nGeneralVLA is a hierarchical vision-language-action model that can be more effective in utilizing the generalization of foundation models, enabling zero-shot manipulation.\n\n**OVAL-Grasp:**\nOVAL-Grasp is a zero-shot open-vocabulary approach to task-oriented, affordance based grasping that uses large-language models (LLM) and vision-language models (VLM) to allow a robot to grasp objects at the correct part according to a given task.\n\nThese models represent the current state-of-the-art in addressing generalization challenges for VLAs on unseen objects and novel scenarios."
    ],
    "durationSeconds": 7.367456625999999
  },
  "sourceToolAssistantUUID": "99e699bf-3056-43d8-8c3a-3d6baaaba82b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-18T19:18:46.128Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GD3vA691S8XT1YTtuVdVPn`</summary>

```json
{
  "query": "VLA^2 VLA2 agentic framework unseen concept manipulation arXiv 2510.14902"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9097ab5-f639-4e3a-a5fa-1e27e1208222",
  "isSidechain": false,
  "requestId": "req_011CbAaENhCsjoDjX1ECSDso",
  "type": "assistant",
  "uuid": "93f2a7b5-85ac-4a9b-8cf5-8062fc279c2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jYnYvYwCoU5hGDfscsErn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 920,
      "cache_read_input_tokens": 59516,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 920,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 59516,
          "cache_creation_input_tokens": 920,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 920
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

_source line 113 · 2026-05-18T19:18:53.406Z_

<details><summary>↩ Tool result · `toolu_01GD3vA691S8XT1YTtuVdVPn`</summary>

```text
Web search results for query: "VLA^2 VLA2 agentic framework unseen concept manipulation arXiv 2510.14902"

Links: [{"title":"VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation","url":"https://paperreading.club/page?id=348445"},{"title":"[2510.14902] VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation","url":"https://arxiv.org/abs/2510.14902"},{"title":"VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation [Quick Review]","url":"https://liner.com/review/vla2-empowering-visionlanguageaction-models-with-agentic-framework-for-unseen-concept"},{"title":"VLA²: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation","url":"https://vla-2.github.io/"},{"title":"VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251014902Z/abstract"},{"title":"VLA2: Empowering Vision-Language-Action Models with an Agentic","url":"https://arxiv.org/pdf/2510.14902"},{"title":"Paper page - VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation","url":"https://huggingface.co/papers/2510.14902"},{"title":"SELF-VLA: A Skill Enhanced Agentic Vision-Language-Action Framework for Contact-Rich Disassembly","url":"https://arxiv.org/html/2603.11080"},{"title":"GitHub - OpenHelix-Team/VLA-2: VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation · GitHub","url":"https://github.com/OpenHelix-Team/VLA-2"},{"title":"VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework forUnseen Concept Manipulation - DEV Community","url":"https://dev.to/paperium/vla2-empowering-vision-language-action-models-with-an-agentic-framework-forunseen-concept-4405"}]

Based on the search results, I found comprehensive information about the paper you requested:

## VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation

**Paper Information:**
- arXiv: 2510.14902
- Authors: Han Zhao, Jiaxuan Zhang, Wenxuan Song, Pengxiang Ding, Donglin Wang
- Released: October 2025

**Overview:**
VLA^2 is a novel agentic framework that leverages OpenVLA as the execution backbone and effectively leverages external modules such as web retrieval and object detection to provide visual and textual knowledge about target objects to the VLA.

**Problem Addressed:**
Current vision-language-action (VLA) models' success rate drops significantly when faced with object concepts outside the training data, such as unseen object descriptions and textures in the dataset.

**Framework Components:**
VLA² integrates four modules to enhance the ability of VLA: Task Planning, Web/Memory Retrieval, Object Grounding, and Result Verification.

**Approach:**
The authors processed target objects and placement locations by applying colored masks and fine-tuned OpenVLA to work with this modified input. This use of colored masks serves as a bridge between upstream unseen concept recognition and downstream task execution by the VLA.

**Evaluation:**
Based on the LIBERO simulation environment, the authors introduced novel objects and object descriptions to construct a new evaluation benchmark with three difficulty levels.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93f2a7b5-85ac-4a9b-8cf5-8062fc279c2b",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "807e0203-462f-4dbc-8a4e-67f9f76e839e",
  "toolUseResult": {
    "query": "VLA^2 VLA2 agentic framework unseen concept manipulation arXiv 2510.14902",
    "results": [
      {
        "tool_use_id": "srvtoolu_018LrDsfr5MjzJmxQSPFHhGt",
        "content": [
          {
            "title": "VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation",
            "url": "https://paperreading.club/page?id=348445"
          },
          {
            "title": "[2510.14902] VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation",
            "url": "https://arxiv.org/abs/2510.14902"
          },
          {
            "title": "VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation [Quick Review]",
            "url": "https://liner.com/review/vla2-empowering-visionlanguageaction-models-with-agentic-framework-for-unseen-concept"
          },
          {
            "title": "VLA²: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation",
            "url": "https://vla-2.github.io/"
          },
          {
            "title": "VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv251014902Z/abstract"
          },
          {
            "title": "VLA2: Empowering Vision-Language-Action Models with an Agentic",
            "url": "https://arxiv.org/pdf/2510.14902"
          },
          {
            "title": "Paper page - VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation",
            "url": "https://huggingface.co/papers/2510.14902"
          },
          {
            "title": "SELF-VLA: A Skill Enhanced Agentic Vision-Language-Action Framework for Contact-Rich Disassembly",
            "url": "https://arxiv.org/html/2603.11080"
          },
          {
            "title": "GitHub - OpenHelix-Team/VLA-2: VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation · GitHub",
            "url": "https://github.com/OpenHelix-Team/VLA-2"
          },
          {
            "title": "VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework forUnseen Concept Manipulation - DEV Community",
            "url": "https://dev.to/paperium/vla2-empowering-vision-language-action-models-with-an-agentic-framework-forunseen-concept-4405"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the paper you requested:\n\n## VLA^2: Empowering Vision-Language-Action Models with an Agentic Framework for Unseen Concept Manipulation\n\n**Paper Information:**\n- arXiv: 2510.14902\n- Authors: Han Zhao, Jiaxuan Zhang, Wenxuan Song, Pengxiang Ding, Donglin Wang\n- Released: October 2025\n\n**Overview:**\nVLA^2 is a novel agentic framework that leverages OpenVLA as the execution backbone and effectively leverages external modules such as web retrieval and object detection to provide visual and textual knowledge about target objects to the VLA.\n\n**Problem Addressed:**\nCurrent vision-language-action (VLA) models' success rate drops significantly when faced with object concepts outside the training data, such as unseen object descriptions and textures in the dataset.\n\n**Framework Components:**\nVLA² integrates four modules to enhance the ability of VLA: Task Planning, Web/Memory Retrieval, Object Grounding, and Result Verification.\n\n**Approach:**\nThe authors processed target objects and placement locations by applying colored masks and fine-tuned OpenVLA to work with this modified input. This use of colored masks serves as a bridge between upstream unseen concept recognition and downstream task execution by the VLA.\n\n**Evaluation:**\nBased on the LIBERO simulation environment, the authors introduced novel objects and object descriptions to construct a new evaluation benchmark with three difficulty levels."
    ],
    "durationSeconds": 7.2753892190000045
  },
  "sourceToolAssistantUUID": "93f2a7b5-85ac-4a9b-8cf5-8062fc279c2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 114_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "807e0203-462f-4dbc-8a4e-67f9f76e839e",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 115_

```json
{
  "type": "ai-title",
  "aiTitle": "AffordVLA: Open-vocabulary affordance distillation into VLA for robust manipulation",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Assistant

_source line 116 · 2026-05-18T19:18:56.730Z_

Now let me read the PALM paper more carefully since it's the closest affordance-VLA baseline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "807e0203-462f-4dbc-8a4e-67f9f76e839e",
  "isSidechain": false,
  "requestId": "req_011CbAaFD53VPmikcR16fHA3",
  "type": "assistant",
  "uuid": "ceec2dea-d44b-4c50-8e68-a8cf3e04d3d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxPUaNpXx4dHuyqcjLXcaz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1090,
      "cache_read_input_tokens": 60436,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1090,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 60436,
          "cache_creation_input_tokens": 1090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1090
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

_source line 117 · 2026-05-18T19:18:59.482Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WAwbCbX67T8Emg3eKgwdJM`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.07060",
  "prompt": "Extract the full abstract. What are the 4 affordance types exactly? How are they generated? Is it end-to-end trained? What external tools does it rely on? What are its limitations regarding open-vocabulary or novel instructions? What are the exact LIBERO results?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ceec2dea-d44b-4c50-8e68-a8cf3e04d3d7",
  "isSidechain": false,
  "requestId": "req_011CbAaFD53VPmikcR16fHA3",
  "type": "assistant",
  "uuid": "acd95eb8-8e5e-4022-b04c-88e3e427fa55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxPUaNpXx4dHuyqcjLXcaz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1090,
      "cache_read_input_tokens": 60436,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1090,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 60436,
          "cache_creation_input_tokens": 1090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1090
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

_source line 118 · 2026-05-18T19:19:06.336Z_

<details><summary>↩ Tool result · `toolu_01WAwbCbX67T8Emg3eKgwdJM`</summary>

```text
# PALM Research Summary

## Full Abstract
"Recent advancements in vision-language-action (VLA) models have shown promise in robotic manipulation, yet they continue to struggle with long-horizon, multi-step tasks. Existing methods lack internal reasoning mechanisms that can identify task-relevant interaction cues or track progress within a subtask, leading to critical execution errors such as repeated actions, missed steps, and premature termination. To address these challenges, we introduce PALM, a VLA framework that structures policy learning around interaction-centric affordance reasoning and subtask progress cues. PALM distills complementary affordance representations that capture object relevance, contact geometry, spatial placements, and motion dynamics, and serve as task-relevant anchors for visuomotor control. To further stabilize long-horizon execution, PALM predicts continuous within-subtask progress, enabling seamless subtask transitions. Across extensive simulation and real-world experiments, PALM consistently outperforms baselines, achieving a 91.8% success rate on LIBERO-LONG, a 12.5% improvement in average length on CALVIN ABC->D, and a 2x improvement over real-world baselines across three long-horizon generalization settings."

## Four Affordance Types
The abstract specifies that affordances capture: (1) object relevance, (2) contact geometry, (3) spatial placements, and (4) motion dynamics.

## Generation Method, Training, and External Dependencies
The provided content does not detail how these affordances are generated, whether training is end-to-end, or what external tools are utilized.

## Limitations and Open-Vocabulary Capabilities
No information regarding limitations, open-vocabulary support, or novel instruction handling appears in the webpage content.

## LIBERO Results
"91.8% success rate on LIBERO-LONG" is the sole specific result provided.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acd95eb8-8e5e-4022-b04c-88e3e427fa55",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "84f9b5dc-6b7f-4a1d-a883-5404640455a1",
  "toolUseResult": {
    "bytes": 46708,
    "code": 200,
    "codeText": "OK",
    "result": "# PALM Research Summary\n\n## Full Abstract\n\"Recent advancements in vision-language-action (VLA) models have shown promise in robotic manipulation, yet they continue to struggle with long-horizon, multi-step tasks. Existing methods lack internal reasoning mechanisms that can identify task-relevant interaction cues or track progress within a subtask, leading to critical execution errors such as repeated actions, missed steps, and premature termination. To address these challenges, we introduce PALM, a VLA framework that structures policy learning around interaction-centric affordance reasoning and subtask progress cues. PALM distills complementary affordance representations that capture object relevance, contact geometry, spatial placements, and motion dynamics, and serve as task-relevant anchors for visuomotor control. To further stabilize long-horizon execution, PALM predicts continuous within-subtask progress, enabling seamless subtask transitions. Across extensive simulation and real-world experiments, PALM consistently outperforms baselines, achieving a 91.8% success rate on LIBERO-LONG, a 12.5% improvement in average length on CALVIN ABC->D, and a 2x improvement over real-world baselines across three long-horizon generalization settings.\"\n\n## Four Affordance Types\nThe abstract specifies that affordances capture: (1) object relevance, (2) contact geometry, (3) spatial placements, and (4) motion dynamics.\n\n## Generation Method, Training, and External Dependencies\nThe provided content does not detail how these affordances are generated, whether training is end-to-end, or what external tools are utilized.\n\n## Limitations and Open-Vocabulary Capabilities\nNo information regarding limitations, open-vocabulary support, or novel instruction handling appears in the webpage content.\n\n## LIBERO Results\n\"91.8% success rate on LIBERO-LONG\" is the sole specific result provided.",
    "durationMs": 6850,
    "url": "https://arxiv.org/abs/2601.07060"
  },
  "sourceToolAssistantUUID": "acd95eb8-8e5e-4022-b04c-88e3e427fa55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 119 · 2026-05-18T19:19:06.344Z_

```json
{
  "parentUuid": "84f9b5dc-6b7f-4a1d-a883-5404640455a1",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "59f6e21a-01e1-4276-b06e-fcaa57830446",
  "timestamp": "2026-05-18T19:19:06.344Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 120 · 2026-05-18T19:19:12.058Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YG7XWWBbC8a8eAnnmnrcKx`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.07060",
  "prompt": "Extract key details about PALM's method: 1) How are the 4 affordance types (object relevance, contact geometry, spatial placements, motion dynamics) generated/supervised? Does it use external tools like Grounding DINO, SAM, SpatialVLM, CoTracker? 2) Is the full system end-to-end trained or does it have modular components? 3) What are the LIBERO benchmark results (all suites, not just LONG)? 4) What are the stated limitations? 5) Can it handle open-vocabulary/novel instructions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59f6e21a-01e1-4276-b06e-fcaa57830446",
  "isSidechain": false,
  "requestId": "req_011CbAaGAPqS7idr7ijo99Sq",
  "type": "assistant",
  "uuid": "47c37550-0957-415f-a02d-188102434274",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLUBMU6mgzLrqzjyCbtKaZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 690,
      "cache_read_input_tokens": 61526,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 61526,
          "cache_creation_input_tokens": 690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 690
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

_source line 121 · 2026-05-18T19:19:19.709Z_

<details><summary>↩ Tool result · `toolu_01YG7XWWBbC8a8eAnnmnrcKx`</summary>

```text
# PALM Method Key Details

## 1) Affordance Generation & Supervision

PALM uses external tools for ground-truth supervision during training:

- **Global Affordance**: "Grounding DINO [liu2024grounding] and then segmenting the instance with SAM [kirillov2023segment]"
- **Local Affordance**: Annotated contact points converted to Gaussian heatmaps (following GLOVER++)
- **Spatial Affordance**: "SpatialVLM [chen2024spatialvlm] and then sampling executable 2D coordinates with RoboPoint [yuan2024robopoint]"
- **Dynamic Affordance**: "CoTracker [karaev2024cotracker] follows each point forward in time"

These four types predict future interaction cues at time t+n.

## 2) Training Architecture

Not fully end-to-end. The system has:
- Frozen vision/text encoders (CLIP, MAE ViT-B)
- Learnable backbone (GPT-2 transformer) with two query sets
- Four affordance supervision heads (training only)
- Diffusion Transformer decoder for action-progress

"During training, affordance queries attend to context tokens to predict foresight... At inference, the affordance heads are removed."

## 3) LIBERO Results (All Suites)

Complete benchmark performance:
- **Spatial**: 95.2 ± 1.2%
- **Object**: 96.7 ± 0.7%
- **Goal**: 94.3 ± 1.6%
- **Long**: 91.8 ± 0.8%
- **Average**: 94.5 ± 1.0%

## 4) Stated Limitations

"Online recovery capability remains limited under execution drift caused by partial observability, contact uncertainty, occlusions, and geometric deformations." The paper also notes affordance annotation, perception, and inference introduce "nontrivial overhead."

## 5) Open-Vocabulary Capability

PALM uses CLIP text encoders and language grounding via external VLMs (Grounding DINO, SpatialVLM), suggesting open-vocabulary support, though the paper doesn't explicitly claim or test this systematically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47c37550-0957-415f-a02d-188102434274",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "af1489b5-1a27-45ee-81a2-4a2fa6ac0ea9",
  "toolUseResult": {
    "bytes": 305395,
    "code": 200,
    "codeText": "OK",
    "result": "# PALM Method Key Details\n\n## 1) Affordance Generation & Supervision\n\nPALM uses external tools for ground-truth supervision during training:\n\n- **Global Affordance**: \"Grounding DINO [liu2024grounding] and then segmenting the instance with SAM [kirillov2023segment]\"\n- **Local Affordance**: Annotated contact points converted to Gaussian heatmaps (following GLOVER++)\n- **Spatial Affordance**: \"SpatialVLM [chen2024spatialvlm] and then sampling executable 2D coordinates with RoboPoint [yuan2024robopoint]\"\n- **Dynamic Affordance**: \"CoTracker [karaev2024cotracker] follows each point forward in time\"\n\nThese four types predict future interaction cues at time t+n.\n\n## 2) Training Architecture\n\nNot fully end-to-end. The system has:\n- Frozen vision/text encoders (CLIP, MAE ViT-B)\n- Learnable backbone (GPT-2 transformer) with two query sets\n- Four affordance supervision heads (training only)\n- Diffusion Transformer decoder for action-progress\n\n\"During training, affordance queries attend to context tokens to predict foresight... At inference, the affordance heads are removed.\"\n\n## 3) LIBERO Results (All Suites)\n\nComplete benchmark performance:\n- **Spatial**: 95.2 ± 1.2%\n- **Object**: 96.7 ± 0.7%\n- **Goal**: 94.3 ± 1.6%\n- **Long**: 91.8 ± 0.8%\n- **Average**: 94.5 ± 1.0%\n\n## 4) Stated Limitations\n\n\"Online recovery capability remains limited under execution drift caused by partial observability, contact uncertainty, occlusions, and geometric deformations.\" The paper also notes affordance annotation, perception, and inference introduce \"nontrivial overhead.\"\n\n## 5) Open-Vocabulary Capability\n\nPALM uses CLIP text encoders and language grounding via external VLMs (Grounding DINO, SpatialVLM), suggesting open-vocabulary support, though the paper doesn't explicitly claim or test this systematically.",
    "durationMs": 7646,
    "url": "https://arxiv.org/html/2601.07060"
  },
  "sourceToolAssistantUUID": "47c37550-0957-415f-a02d-188102434274",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 122 · 2026-05-18T19:19:26.197Z_

This is extremely valuable. PALM uses 4 predefined affordance types with external tools during training but drops them at inference — very similar to AffordVLA's approach of dropping the affordance head at inference. But PALM's affordance types are fixed/structured, while AffordVLA proposes open-vocabulary affordance heatmaps. Let me verify the compute feasibility claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af1489b5-1a27-45ee-81a2-4a2fa6ac0ea9",
  "isSidechain": false,
  "requestId": "req_011CbAaH9fxPGRmaRNADBTUk",
  "type": "assistant",
  "uuid": "6b032ccd-c24b-4275-a9cb-97a01e80a514",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CnBtbyAaETUyQWdPwV8qK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 62216,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 62216,
          "cache_creation_input_tokens": 753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 753
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

_source line 123 · 2026-05-18T19:19:27.269Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RQrBSL9kQVHLammsGfQSBp`</summary>

```json
{
  "query": "OpenVLA-OFT LoRA fine-tuning training hours GPU cost LIBERO H100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b032ccd-c24b-4275-a9cb-97a01e80a514",
  "isSidechain": false,
  "requestId": "req_011CbAaH9fxPGRmaRNADBTUk",
  "type": "assistant",
  "uuid": "9b9d1c21-c1da-4954-a067-3eecd777f2f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012CnBtbyAaETUyQWdPwV8qK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 62216,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 62216,
          "cache_creation_input_tokens": 753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 753
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

_source line 124 · 2026-05-18T19:19:39.303Z_

<details><summary>↩ Tool result · `toolu_01RQrBSL9kQVHLammsGfQSBp`</summary>

```text
Web search results for query: "OpenVLA-OFT LoRA fine-tuning training hours GPU cost LIBERO H100"

Links: [{"title":"Deploy OpenVLA on GPU Cloud: Self-Host the Open Vision-Language-Action Robotics Foundation Model (2026 Setup Guide) | Spheron Blog","url":"https://www.spheron.network/blog/deploy-openvla-gpu-cloud/"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v1"},{"title":"Training Data for OpenVLA | Data Requirements & Formats | Claru","url":"https://claru.ai/models/openvla"},{"title":"OpenVLA: Open Source VLA for Robotics","url":"https://www.emergentmind.com/topics/openvla"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/html/2406.09246v3"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"Scaling VLA Model Training on a Budget: Lessons From 100+ Fine-Tunes | Silicon Valley Robotics Center","url":"https://www.roboticscenter.ai/blog/scaling-vla-training-on-a-budget"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"How can I fine-tune large language models on a budget using LoRA and QLoRA on cloud GPUs?","url":"https://www.runpod.io/articles/guides/how-to-fine-tune-large-language-models-on-a-budget"}]

Based on the search results, here's the information about OpenVLA-OFT LoRA fine-tuning with the specifications you asked about:

## Training Hours and GPU Requirements

OpenVLA-OFT training jobs were run with 8 A100 or H100 GPUs with 80 GB memory and trained for 50K to 150K gradient steps, which took 1-2 days. For smaller-scale training, a 10,000-step dataset typically requires 4-6 GPU-hours on an H100 80GB.

## GPU Cost

Cost is based on $3.10/hr on-demand H100 SXM5 pricing according to a recent guide from May 2026.

## LIBERO Benchmark Performance

OpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×. Additionally, the optimized fine-tuning recipe with parallel decoding and continuous action representations increased inference speed by 26x and boosted the LIBERO benchmark average from 76.5% to 97.1%.

## Memory Requirements for LIBERO

For LIBERO with 1 input image (third-person camera), 7 action dimensions, action chunk size 8, and batch size 8 per device, 44.1 GB GPU memory is required.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b9d1c21-c1da-4954-a067-3eecd777f2f5",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "54ef94ca-04b5-4ed4-b833-76ef7abeecad",
  "toolUseResult": {
    "query": "OpenVLA-OFT LoRA fine-tuning training hours GPU cost LIBERO H100",
    "results": [
      {
        "tool_use_id": "srvtoolu_015FzZa1FVweiuiZQyFojC6N",
        "content": [
          {
            "title": "Deploy OpenVLA on GPU Cloud: Self-Host the Open Vision-Language-Action Robotics Foundation Model (2026 Setup Guide) | Spheron Blog",
            "url": "https://www.spheron.network/blog/deploy-openvla-gpu-cloud/"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/html/2502.19645v1"
          },
          {
            "title": "Training Data for OpenVLA | Data Requirements & Formats | Claru",
            "url": "https://claru.ai/models/openvla"
          },
          {
            "title": "OpenVLA: Open Source VLA for Robotics",
            "url": "https://www.emergentmind.com/topics/openvla"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://openvla-oft.github.io/"
          },
          {
            "title": "OpenVLA: An Open-Source Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2406.09246v3"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/pdf/2502.19645"
          },
          {
            "title": "Scaling VLA Model Training on a Budget: Lessons From 100+ Fine-Tunes | Silicon Valley Robotics Center",
            "url": "https://www.roboticscenter.ai/blog/scaling-vla-training-on-a-budget"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "How can I fine-tune large language models on a budget using LoRA and QLoRA on cloud GPUs?",
            "url": "https://www.runpod.io/articles/guides/how-to-fine-tune-large-language-models-on-a-budget"
          }
        ]
      },
      "Based on the search results, here's the information about OpenVLA-OFT LoRA fine-tuning with the specifications you asked about:\n\n## Training Hours and GPU Requirements\n\nOpenVLA-OFT training jobs were run with 8 A100 or H100 GPUs with 80 GB memory and trained for 50K to 150K gradient steps, which took 1-2 days. For smaller-scale training, a 10,000-step dataset typically requires 4-6 GPU-hours on an H100 80GB.\n\n## GPU Cost\n\nCost is based on $3.10/hr on-demand H100 SXM5 pricing according to a recent guide from May 2026.\n\n## LIBERO Benchmark Performance\n\nOpenVLA-OFT sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26×. Additionally, the optimized fine-tuning recipe with parallel decoding and continuous action representations increased inference speed by 26x and boosted the LIBERO benchmark average from 76.5% to 97.1%.\n\n## Memory Requirements for LIBERO\n\nFor LIBERO with 1 input image (third-person camera), 7 action dimensions, action chunk size 8, and batch size 8 per device, 44.1 GB GPU memory is required."
    ],
    "durationSeconds": 12.029546955000027
  },
  "sourceToolAssistantUUID": "9b9d1c21-c1da-4954-a067-3eecd777f2f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 125 · 2026-05-18T19:19:44.163Z_

Good. Training is feasible on 1×H100 with ~15h per run. The proposal's compute estimate of ~180h H100 for manual mode seems realistic. Let me verify one more thing — the AGD20K and UMD affordance datasets mentioned in the original user spec.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54ef94ca-04b5-4ed4-b833-76ef7abeecad",
  "isSidechain": false,
  "requestId": "req_011CbAaJbJqXtZewgkyZzAEi",
  "type": "assistant",
  "uuid": "b5503f10-b785-462a-abda-73502ad64587",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHY66F4UbVHff65byrL315",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 62969,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 62969,
          "cache_creation_input_tokens": 1025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1025
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

_source line 126 · 2026-05-18T19:19:44.629Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AZBbuu7yTXqfCdXKZxdbVi`</summary>

```json
{
  "query": "AGD20K affordance grounding dataset availability 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5503f10-b785-462a-abda-73502ad64587",
  "isSidechain": false,
  "requestId": "req_011CbAaJbJqXtZewgkyZzAEi",
  "type": "assistant",
  "uuid": "fdc66d75-bcea-4bd0-91ec-95236ce0db6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHY66F4UbVHff65byrL315",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1025,
      "cache_read_input_tokens": 62969,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 132,
          "cache_read_input_tokens": 62969,
          "cache_creation_input_tokens": 1025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1025
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

_source line 127 · 2026-05-18T19:19:51.350Z_

<details><summary>↩ Tool result · `toolu_01AZBbuu7yTXqfCdXKZxdbVi`</summary>

```text
Web search results for query: "AGD20K affordance grounding dataset availability 2024 2025"

Links: [{"title":"Grounding 3D Object Affordance with Language Instructions, Visual Observations and Interactions | Request PDF","url":"https://www.researchgate.net/publication/394512560_Grounding_3D_Object_Affordance_with_Language_Instructions_Visual_Observations_and_Interactions"},{"title":"The results of the different methods on the AGD20K for each affordance... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/The-results-of-the-different-methods-on-the-AGD20K-for-each-affordance-category-We_fig8_376833041"},{"title":"GitHub - lhc1224/Cross-View-AG: Official PyTorch Implementation of Learning Affordance Grounding from Exocentric Images, CVPR 2022","url":"https://github.com/lhc1224/Cross-View-AG"},{"title":"[2503.02600] Resource-Efficient Affordance Grounding with Complementary Depth and Semantic Prompts","url":"https://arxiv.org/abs/2503.02600"},{"title":"Learning Affordance Grounding from Exocentric Images","url":"https://arxiv.org/pdf/2203.09905"},{"title":"Weakly-Supervised Affordance Grounding Guided by Part-Level Semantic Priors","url":"https://arxiv.org/html/2505.24103v1"},{"title":"Grounding 3D Object Affordance with Language Instructions, Visual Observations and Interactions","url":"https://arxiv.org/html/2504.04744v1"},{"title":"Grounded Affordance from Exocentric View","url":"https://arxiv.org/pdf/2208.13196"},{"title":"AffordanceLLM: Grounding Affordance from Vision Language Models","url":"https://arxiv.org/pdf/2401.06341"}]

Based on the search results, here's what I found about the AGD20K affordance grounding dataset availability:

## Dataset Overview

The AGD20K dataset consists of 20,061 exocentric images and 3,755 egocentric images from 36 affordance categories. It was constructed by collecting and labeling over 20K images from 36 affordance categories.

## Recent Activity (2024-2025)

The dataset continues to be actively used in research as of 2024-2025. AGD20K is described as a widely-used weakly supervised affordance grounding dataset containing about 30K exocentric and egocentric images, annotated with 36 affordance classes and 50 object classes.

Recent papers utilizing the dataset include:
- Research from March 2025 demonstrates significant performance improvements on the AGD20K dataset, achieving a 6.0% improvement in the KLD metric.
- A May 2025 paper on weakly-supervised affordance grounding conducted experiments on AGD20K.

## Data Access

The code and dataset are available through GitHub at github.com/lhc1224/Cross-View-AG. However, the search results do not provide specific information about direct download links or access procedures for obtaining the dataset itself in 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdc66d75-bcea-4bd0-91ec-95236ce0db6f",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "87642c83-9458-4e38-ab6c-96cc345fd3f6",
  "toolUseResult": {
    "query": "AGD20K affordance grounding dataset availability 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_017LmftqwdEybVyoU6Dmr6EJ",
        "content": [
          {
            "title": "Grounding 3D Object Affordance with Language Instructions, Visual Observations and Interactions | Request PDF",
            "url": "https://www.researchgate.net/publication/394512560_Grounding_3D_Object_Affordance_with_Language_Instructions_Visual_Observations_and_Interactions"
          },
          {
            "title": "The results of the different methods on the AGD20K for each affordance... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/The-results-of-the-different-methods-on-the-AGD20K-for-each-affordance-category-We_fig8_376833041"
          },
          {
            "title": "GitHub - lhc1224/Cross-View-AG: Official PyTorch Implementation of Learning Affordance Grounding from Exocentric Images, CVPR 2022",
            "url": "https://github.com/lhc1224/Cross-View-AG"
          },
          {
            "title": "[2503.02600] Resource-Efficient Affordance Grounding with Complementary Depth and Semantic Prompts",
            "url": "https://arxiv.org/abs/2503.02600"
          },
          {
            "title": "Learning Affordance Grounding from Exocentric Images",
            "url": "https://arxiv.org/pdf/2203.09905"
          },
          {
            "title": "Weakly-Supervised Affordance Grounding Guided by Part-Level Semantic Priors",
            "url": "https://arxiv.org/html/2505.24103v1"
          },
          {
            "title": "Grounding 3D Object Affordance with Language Instructions, Visual Observations and Interactions",
            "url": "https://arxiv.org/html/2504.04744v1"
          },
          {
            "title": "Grounded Affordance from Exocentric View",
            "url": "https://arxiv.org/pdf/2208.13196"
          },
          {
            "title": "AffordanceLLM: Grounding Affordance from Vision Language Models",
            "url": "https://arxiv.org/pdf/2401.06341"
          }
        ]
      },
      "Based on the search results, here's what I found about the AGD20K affordance grounding dataset availability:\n\n## Dataset Overview\n\nThe AGD20K dataset consists of 20,061 exocentric images and 3,755 egocentric images from 36 affordance categories. It was constructed by collecting and labeling over 20K images from 36 affordance categories.\n\n## Recent Activity (2024-2025)\n\nThe dataset continues to be actively used in research as of 2024-2025. AGD20K is described as a widely-used weakly supervised affordance grounding dataset containing about 30K exocentric and egocentric images, annotated with 36 affordance classes and 50 object classes.\n\nRecent papers utilizing the dataset include:\n- Research from March 2025 demonstrates significant performance improvements on the AGD20K dataset, achieving a 6.0% improvement in the KLD metric.\n- A May 2025 paper on weakly-supervised affordance grounding conducted experiments on AGD20K.\n\n## Data Access\n\nThe code and dataset are available through GitHub at github.com/lhc1224/Cross-View-AG. However, the search results do not provide specific information about direct download links or access procedures for obtaining the dataset itself in 2024-2025."
    ],
    "durationSeconds": 6.717395147000032
  },
  "sourceToolAssistantUUID": "fdc66d75-bcea-4bd0-91ec-95236ce0db6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 128 · 2026-05-18T19:19:54.830Z_

Now let me assess the key differentiation claim — that AffordVLA's open-vocabulary affordance pseudo-labels are meaningfully different from SG-VLA's grasp affordance auxiliary loss.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87642c83-9458-4e38-ab6c-96cc345fd3f6",
  "isSidechain": false,
  "requestId": "req_011CbAaKUqSNK6REAGvmqEPy",
  "type": "assistant",
  "uuid": "3f1c41a9-2414-490a-9071-65a06d9fed9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pChWr541XrV6FMpxyoZJk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 63994,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 63994,
          "cache_creation_input_tokens": 949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 949
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

_source line 129 · 2026-05-18T19:19:56.461Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011rmb9aLUXB77icea4M3Zwv`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.22760",
  "prompt": "Extract the full abstract of SG-VLA. What exactly are the auxiliary tasks? How does it use affordance? Is the affordance open-vocabulary or fixed categories? What are the results on which benchmarks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f1c41a9-2414-490a-9071-65a06d9fed9b",
  "isSidechain": false,
  "requestId": "req_011CbAaKUqSNK6REAGvmqEPy",
  "type": "assistant",
  "uuid": "5e672ed8-ab60-4e2b-8b13-5fe7e5047e8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019pChWr541XrV6FMpxyoZJk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 63994,
      "output_tokens": 170,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 949,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 170,
          "cache_read_input_tokens": 63994,
          "cache_creation_input_tokens": 949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 949
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

_source line 130_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "5e672ed8-ab60-4e2b-8b13-5fe7e5047e8c",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 131_

```json
{
  "type": "ai-title",
  "aiTitle": "AffordVLA: Open-vocabulary affordance distillation into VLA for robust manipulation",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Tool result

_source line 132 · 2026-05-18T19:20:01.487Z_

<details><summary>↩ Tool result · `toolu_011rmb9aLUXB77icea4M3Zwv`</summary>

```text
# SG-VLA Paper Analysis

## Full Abstract

The paper presents a framework for learning spatially-grounded Vision-Language-Action models addressing mobile manipulation challenges. The approach combines auxiliary task co-training and multi-modal input enhancement to improve perception for controlling a 13-dimensional action space involving base motion, arm articulation, and gripper control. The model processes multi-view RGB, depth, and temporal history to understand both global scene structure and local manipulation context.

## Auxiliary Tasks

The co-trained auxiliary decoders reconstruct five interpretable intermediate signals from shared visual-language features:
- Global robot position
- Joint configurations
- Grasp affordances
- Target-object relative pose
- Segmentation masks

These objectives provide "dense supervision that encourages the backbone to develop spatially grounded, manipulation-aware latent representations."

## Affordance Details

The document does not specify whether affordance predictions use open-vocabulary or fixed categories. It only mentions that the model includes "grasp affordances" among its auxiliary outputs, without elaborating on the affordance representation scheme.

## Benchmark Results

The abstract states the method "achieves consistent improvements across picking, placing, opening, and closing operations, substantially outperforming direct imitation learning" on "home rearrangement tasks." However, no specific numerical results or named benchmark datasets are mentioned in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e672ed8-ab60-4e2b-8b13-5fe7e5047e8c",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "4a4c81c5-7907-40e0-af04-9243d901a598",
  "toolUseResult": {
    "bytes": 47985,
    "code": 200,
    "codeText": "OK",
    "result": "# SG-VLA Paper Analysis\n\n## Full Abstract\n\nThe paper presents a framework for learning spatially-grounded Vision-Language-Action models addressing mobile manipulation challenges. The approach combines auxiliary task co-training and multi-modal input enhancement to improve perception for controlling a 13-dimensional action space involving base motion, arm articulation, and gripper control. The model processes multi-view RGB, depth, and temporal history to understand both global scene structure and local manipulation context.\n\n## Auxiliary Tasks\n\nThe co-trained auxiliary decoders reconstruct five interpretable intermediate signals from shared visual-language features:\n- Global robot position\n- Joint configurations\n- Grasp affordances\n- Target-object relative pose\n- Segmentation masks\n\nThese objectives provide \"dense supervision that encourages the backbone to develop spatially grounded, manipulation-aware latent representations.\"\n\n## Affordance Details\n\nThe document does not specify whether affordance predictions use open-vocabulary or fixed categories. It only mentions that the model includes \"grasp affordances\" among its auxiliary outputs, without elaborating on the affordance representation scheme.\n\n## Benchmark Results\n\nThe abstract states the method \"achieves consistent improvements across picking, placing, opening, and closing operations, substantially outperforming direct imitation learning\" on \"home rearrangement tasks.\" However, no specific numerical results or named benchmark datasets are mentioned in the provided content.",
    "durationMs": 5022,
    "url": "https://arxiv.org/abs/2603.22760"
  },
  "sourceToolAssistantUUID": "5e672ed8-ab60-4e2b-8b13-5fe7e5047e8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-18T19:20:05.545Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BS5gyyE95pHiGb2Tj9mQqr`</summary>

```json
{
  "query": "AVA-VLA active visual attention arXiv 2511.18960 LIBERO results 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a4c81c5-7907-40e0-af04-9243d901a598",
  "isSidechain": false,
  "requestId": "req_011CbAaLEAQgbnBxk4wZhDdS",
  "type": "assistant",
  "uuid": "26c3d978-ed17-4f0e-bc8a-0cf18230b2a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZJoJ8zDGHerpZL3qPAgUs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 477,
      "cache_read_input_tokens": 64943,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 477,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 64943,
          "cache_creation_input_tokens": 477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 477
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

_source line 134 · 2026-05-18T19:20:11.957Z_

<details><summary>↩ Tool result · `toolu_01BS5gyyE95pHiGb2Tj9mQqr`</summary>

```text
Web search results for query: "AVA-VLA active visual attention arXiv 2511.18960 LIBERO results 2025"

Links: [{"title":"[2511.18960] AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/abs/2511.18960"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/pdf/2511.18960"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251118960X/abstract"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/html/2511.18960v1"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://www.researchgate.net/publication/397934001_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.18960v1"},{"title":"Recursive Belief Vision Language Action Model","url":"https://arxiv.org/html/2602.20659v1"}]

Based on the search results, I found detailed information about the AVA-VLA paper (arXiv 2511.18960):

## Overview

AVA-VLA is a framework that improves Vision-Language-Action (VLA) models with Active Visual Attention. The paper addresses a key limitation in existing VLA models.

## Key Contribution

AVA-VLA reformulates VLA policy learning from a Partially Observable Markov Decision Process perspective and conditions action generation on a recurrent state that serves as a neural approximation to the agent's belief over task history. The AVA module uses the recurrent state to compute soft weights to actively process task-relevant visual tokens based on its historical context.

## LIBERO Results

Comprehensive evaluations demonstrate that AVA-VLA achieves state-of-the-art performance across popular robotic benchmarks, including LIBERO and CALVIN. Extensive experiments show that AVA-VLA achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dual-arm manipulation tasks.

## Authors and Publication

The paper was submitted in November 2025 and last revised in April 2026, authored by Lei Xiao and 8 other co-authors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26c3d978-ed17-4f0e-bc8a-0cf18230b2a9",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "f6599d2b-7837-41c1-b796-ec2ea62cf8e1",
  "toolUseResult": {
    "query": "AVA-VLA active visual attention arXiv 2511.18960 LIBERO results 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WeXy5A7UDVHiWLsLyJMKgc",
        "content": [
          {
            "title": "[2511.18960] AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention",
            "url": "https://arxiv.org/abs/2511.18960"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention",
            "url": "https://arxiv.org/pdf/2511.18960"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv251118960X/abstract"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention",
            "url": "https://arxiv.org/html/2511.18960v1"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention",
            "url": "https://www.researchgate.net/publication/397934001_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2511.18960v1"
          },
          {
            "title": "Recursive Belief Vision Language Action Model",
            "url": "https://arxiv.org/html/2602.20659v1"
          }
        ]
      },
      "Based on the search results, I found detailed information about the AVA-VLA paper (arXiv 2511.18960):\n\n## Overview\n\nAVA-VLA is a framework that improves Vision-Language-Action (VLA) models with Active Visual Attention. The paper addresses a key limitation in existing VLA models.\n\n## Key Contribution\n\nAVA-VLA reformulates VLA policy learning from a Partially Observable Markov Decision Process perspective and conditions action generation on a recurrent state that serves as a neural approximation to the agent's belief over task history. The AVA module uses the recurrent state to compute soft weights to actively process task-relevant visual tokens based on its historical context.\n\n## LIBERO Results\n\nComprehensive evaluations demonstrate that AVA-VLA achieves state-of-the-art performance across popular robotic benchmarks, including LIBERO and CALVIN. Extensive experiments show that AVA-VLA achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dual-arm manipulation tasks.\n\n## Authors and Publication\n\nThe paper was submitted in November 2025 and last revised in April 2026, authored by Lei Xiao and 8 other co-authors."
    ],
    "durationSeconds": 6.4081752550000095
  },
  "sourceToolAssistantUUID": "26c3d978-ed17-4f0e-bc8a-0cf18230b2a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 135 · 2026-05-18T19:20:14.897Z_

Now I have enough information. Let me do one final check — whether the proposal's framing of the robustness gap is accurate and whether the proposed method is the right approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6599d2b-7837-41c1-b796-ec2ea62cf8e1",
  "isSidechain": false,
  "requestId": "req_011CbAaLztjHm158F9MgbsCV",
  "type": "assistant",
  "uuid": "033c1ea5-e440-4f23-9178-4bebd64937a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkPHcucuwSshesRBidxfR1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 65420,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 65420,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 762
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

_source line 136 · 2026-05-18T19:20:15.765Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KFaD3fx3uYdmUF679TwC9i`</summary>

```json
{
  "query": "LIBERO-Plus VLA robustness results OpenVLA performance perturbation camera lighting 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "033c1ea5-e440-4f23-9178-4bebd64937a0",
  "isSidechain": false,
  "requestId": "req_011CbAaLztjHm158F9MgbsCV",
  "type": "assistant",
  "uuid": "5eff3c9f-afb8-4b9c-b9e8-c8ff751e7248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkPHcucuwSshesRBidxfR1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 65420,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 65420,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 762
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

_source line 137 · 2026-05-18T19:20:25.558Z_

<details><summary>↩ Tool result · `toolu_01KFaD3fx3uYdmUF679TwC9i`</summary>

```text
Web search results for query: "LIBERO-Plus VLA robustness results OpenVLA performance perturbation camera lighting 2025 2026"

Links: [{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata · Hugging Face","url":"https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/pdf/2510.00037"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling","url":"https://arxiv.org/pdf/2512.02902"}]

The search results reveal comprehensive robustness findings from the LIBERO-Plus benchmark evaluation of Vision-Language-Action models. Here are the key results:

## OpenVLA Performance Under Perturbations

OpenVLA models that depend exclusively on third-person observations suffer severe drops under light perturbations, often exceeding 60 points. In contrast, wrist cameras provide critical robustness to illumination changes due to their close-range perspective, which provides illumination-invariant geometric cues.

## Overall Robustness Findings

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. The evaluation introduced controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

## Specific Lighting Findings

In all-black conditions, performance collapses to nearly zero across models, but under 3rd-black settings (wrist view only), models still achieve accuracies ranging from 43.0 to 67.3.

## Language Insensitivity

Interestingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

The LIBERO-Plus paper was published in October 2025, providing the most recent systematic analysis of VLA robustness vulnerabilities across multiple models including OpenVLA and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5eff3c9f-afb8-4b9c-b9e8-c8ff751e7248",
  "isSidechain": false,
  "promptId": "da7bc473-33b6-4015-b311-9f22305fddcf",
  "type": "user",
  "uuid": "2c7bb6ce-e9a4-43b8-99b0-f6d8a5bb5907",
  "toolUseResult": {
    "query": "LIBERO-Plus VLA robustness results OpenVLA performance perturbation camera lighting 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PhWyeCfcmhLZGCbTTc3bGU",
        "content": [
          {
            "title": "OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata · Hugging Face",
            "url": "https://huggingface.co/Sylvest/openvla-7b-oft-finetuned-libero-plus-mixdata"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
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
            "title": "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/pdf/2510.00037"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling",
            "url": "https://arxiv.org/pdf/2512.02902"
          }
        ]
      },
      "The search results reveal comprehensive robustness findings from the LIBERO-Plus benchmark evaluation of Vision-Language-Action models. Here are the key results:\n\n## OpenVLA Performance Under Perturbations\n\nOpenVLA models that depend exclusively on third-person observations suffer severe drops under light perturbations, often exceeding 60 points. In contrast, wrist cameras provide critical robustness to illumination changes due to their close-range perspective, which provides illumination-invariant geometric cues.\n\n## Overall Robustness Findings\n\nModels exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations. The evaluation introduced controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.\n\n## Specific Lighting Findings\n\nIn all-black conditions, performance collapses to nearly zero across models, but under 3rd-black settings (wrist view only), models still achieve accuracies ranging from 43.0 to 67.3.\n\n## Language Insensitivity\n\nInterestingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.\n\nThe LIBERO-Plus paper was published in October 2025, providing the most recent systematic analysis of VLA robustness vulnerabilities across multiple models including OpenVLA and others."
    ],
    "durationSeconds": 9.78949692799995
  },
  "sourceToolAssistantUUID": "5eff3c9f-afb8-4b9c-b9e8-c8ff751e7248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 138 · 2026-05-18T19:20:25.566Z_

```json
{
  "parentUuid": "2c7bb6ce-e9a4-43b8-99b0-f6d8a5bb5907",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3a034350-0b3f-4ab6-9556-500175b24312",
  "timestamp": "2026-05-18T19:20:25.566Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 139 · 2026-05-18T19:21:33.895Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize everything I've found and make my assessment.

## Summary of findings:

### Previous round issues addressed:
1. **PALM included** ✓ — Correctly characterized as strongest affordance-VLA baseline. The proposal now properly includes PALM with its 4 affordance types (object relevance, contact geometry, spatial placements, motion dynamics) using external tools (Grounding DINO, SAM, SpatialVLM, CoTracker). Claims about PALM's 91.8% LIBERO-LONG and 94.5% average LIBERO are verified.

2. **FocusVLA differentiation** ✓ — Now explicitly contrasted. 

The key difference is that AffordVLA trains on an explicit affordance signal, whereas FocusVLA only learns task-relevant attention through action loss—a meaningful distinction in how the models acquire their capabilities.

3. **UAD included** ✓ — Properly characterized as modular pipeline. The proposal adopts UAD's philosophy of unsupervised affordance extraction from frozen VLMs.

4. **Compute budget** — The proposal acknowledges CoRL 2026 is impossible (confirmed: deadline May 29, 2026 = 11 days away). Manual mode at ~180h H100 fits within the 200h constraint. Auto mode at 400-500h explicitly exceeds it.

5. **Venue targeting** — CoRL 2026 acknowledged as impossible.

ICRA 2027 with a likely September 2026 deadline is the realistic primary target, giving us about four months to work with. The supervision signal is now concretely resolved through an auxiliary affordance prediction head that uses pseudo-labels from frozen foundation models like DINOv2, Qwen2-VL-7B, and GroundingDINO. I've also incorporated AffordGrasp and CoT-VLA into the related work landscape.

Now I'm spotting a critical gap: SG-VLA from March 2026 uses auxiliary decoders to predict grasp affordances alongside robot position, joint configurations, relative pose, and segmentation masks from shared visual-language features—this is architecturally quite similar to what AffordVLA is proposing, and I need to address this overlap directly.

Beyond that, I'm seeing that the auxiliary prediction paradigm on intermediate representations is already well-established across multiple works: QDepth-VLA adds quantized depth, DreamVLA combines semantics with depth and dynamics, SG-VLA handles grasp affordances, and RS-CL predicts robot state. AffordVLA's contribution of open-vocabulary affordance heatmaps is another variant in this family, which means the novelty is more incremental than foundational.

The core claim that affordance grounding improves robustness under distribution shift is testable but not yet proven—the cited evidence conflates different approaches. AFI demonstrates that affordance helps at inference time, which is mechanistically different from using affordance supervision only during training. And looking at PALM's design, it's remarkably similar: four affordance prediction heads during training that get discarded at inference, with the main distinction being PALM's use of structured types versus AffordVLA's open-vocabulary approach. PALM generates those types through external models like Grounding DINO and SAM, which parallels how AffordVLA constructs its pseudo-labels.

The novelty gap is concerning—swapping PALM's fixed affordance types for VLM-conditioned heatmaps feels incremental when both methods rely on external frozen models for label generation, both add auxiliary prediction heads, and both discard them at inference. There's also a tension in the robustness framing: if LIBERO-Plus shows that VLAs ignore language instructions, then language-conditioned affordance features may not actually improve robustness in the way the proposal suggests.

The pseudo-label pipeline introduces several failure points. GroundingDINO may struggle to accurately localize fine-grained regions like "the handle of a mug," creating noisy training signals that the proposal doesn't address. More fundamentally, the "open-vocabulary" affordance claim depends on a chain of assumptions—the VLM must understand the instruction correctly, GroundingDINO must localize the described region accurately, and those spatial heatmaps must actually capture task-relevant affordances—but the proposal doesn't validate this pipeline or discuss failure modes.

I'm also noticing that AffordVLA applies affordances only during training, whereas Affordance Field Intervention uses them at inference time and achieves +23.5% OOD gains. The proposal doesn't justify why training-time affordances would provide comparable robustness benefits, and this comparison deserves more depth.

Finally, the venue shift from CoRL 2026 to ICRA 2027 is understandable given the timeline constraints, but it does diverge from the original request.

Looking at the scoring now: the core novelty of open-vocabulary affordance pseudo-labels as an auxiliary signal is solid but incremental—auxiliary prediction heads are well-established in VLA work, and PALM already uses affordance auxiliary training. The main distinction is the open-vocabulary angle rather than structured types, which feels like a modest delta. Feasibility-wise, the scope is reasonable with OpenVLA-OFT and LoRA fine-tuning on 180 hours of H100 compute, and the pipeline is implementable, though pseudo-label quality from GroundingDINO and whether the robustness hypothesis actually holds are real risks. The proposal itself is clearly written overall.

On impact, if the robustness hypothesis pans out—that affordance-grounded features transfer better—it could matter, but the gains are capped by the incremental novelty over PALM, uncertainty around the magnitude of the robustness effect, and the fact that affordance auxiliary losses are already established in the field. This lands around 3.5/5, below the 4.0 bar.

The revision needs to directly engage with SG-VLA, which is the most recent affordance auxiliary work in VLAs and can't be glossed over, and I need to sharpen what actually differentiates this from PALM beyond just the vocabulary scope.

The robustness claim also needs real teeth—why would an auxiliary loss during training create robustness when LIBERO-Plus shows models often ignore language signals anyway? And the pseudo-label pipeline itself is a potential weakness: VLM to text to GroundingDINO to heatmap introduces compounding noise at each step.

Given this is round 2, the prior issues were mostly handled, so the remaining gaps—SG-VLA, incremental novelty, and weak robustness justification—are fixable with revision rather than rejection. incremental over PALM?

PALM: Fixed 4 affordance types → auxiliary prediction heads → drop at inference
AffordVLA: Open-vocabulary affordance heatmaps from VLM → auxiliary prediction head → drop at inference

The structural similarity is very high. The key claim is that open-vocabulary heatmaps capture richer/more robust affordance information than 4 structured types. This is testable and could be significant if true. But architecturally, this is PALM with a different pseudo-label generation pipeline.

The probing study (2602.20501) provides theoretical backing that frozen VLMs encode rich affordance features. UAD shows these can be extracted unsupervised. The novel combination is specifically using VLM-generated open-vocabulary affordance pseudo-labels as auxiliary training signal for VLA intermediate layers, targeting robustness.

The novelty hinges on framing this not as a new architecture, but as a principled test of whether open-vocabulary affordance supervision produces more robust VLA features than fixed structured types. That's the core hypothesis worth validating.

There's also a venue mismatch — the user asked for CoRL 2026, which isn't feasible, but ICRA 2027 is a legitimate target even if it doesn't match their request. The work needs revision with clearer positioning.

Looking at the scores more carefully: novelty sits at 3/5 since the auxiliary affordance paradigm already exists across several prior works, and the main delta is just swapping pseudo-label types. Pushing to 4/5 would require a more distinctive technical contribution beyond that change. Feasibility is solid at 4/5 — the scope is realistic and the compute requirements are manageable with available resources.

The proposal is exceptionally well-written at 4/5 clarity with specific details and clear baselines. Impact is limited to 3/5 because the incremental novelty constrains how transformative the results could be. The average lands at 3.5, below the 4.0 threshold, so revision is the right call.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a034350-0b3f-4ab6-9556-500175b24312",
  "isSidechain": false,
  "requestId": "req_011CbAaN15RJG8jCe6zNMzgN",
  "type": "assistant",
  "uuid": "5ff17904-2622-4a3a-85a0-9ced85d12c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EC3nBhWEbHQi2hFEkfd3gY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 66182,
      "output_tokens": 5136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5136,
          "cache_read_input_tokens": 66182,
          "cache_creation_input_tokens": 1066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1066
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

_source line 140 · 2026-05-18T19:22:15.622Z_

Now I have enough data to form a thorough assessment. Let me synthesize my findings.

**Key verified facts:**
- PALM (arXiv 2601.07060): 94.5% avg LIBERO, 91.8% LIBERO-LONG with 4 affordance types + auxiliary heads dropped at inference — **confirmed**
- FocusVLA (arXiv 2603.28740): Focus Attention for task-relevant token selection, no affordance signal — **confirmed**
- LIBERO-Plus (CVPR 2026): 95% → <30% under perturbation — **confirmed**
- UAD (ICRA 2025 Best Paper Finalist): unsupervised affordance from frozen VLMs — **confirmed**
- CoRL 2026 deadline: May 29, 2026 (11 days) — **effectively impossible**
- OpenVLA-OFT LoRA: ~15h per run on 1×H100 — **confirmed**, compute budget realistic
- SG-VLA (arXiv 2603.22760, Mar 2026): **CRITICAL FIND** — uses auxiliary affordance prediction in VLA, not cited
- QDepth-VLA, DreamVLA: auxiliary prediction paradigm well-established
- PALM architecture structurally very similar to AffordVLA (auxiliary heads dropped at inference)

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "The auxiliary prediction paradigm for VLAs is well-established (QDepth-VLA for depth, DreamVLA for semantics/depth/dynamics, SG-VLA for grasp affordance, PALM for 4 structured affordance types). AffordVLA's specific contribution — replacing PALM's fixed affordance types with open-vocabulary VLM-generated heatmaps — is incremental. Both PALM and AffordVLA use auxiliary affordance heads dropped at inference; the delta is the pseudo-label generation pipeline."},
    "feasibility": {"score": 4, "rationale": "Well-scoped: OpenVLA-OFT base with LoRA (~15h/run on 1×H100) is verified; pseudo-label generation from frozen models (DINOv2 + Qwen2-VL + GroundingDINO) is implementable. 180h H100 manual budget fits within the 200h constraint. Risk: pseudo-label quality from the VLM→text→GroundingDINO→heatmap pipeline introduces compounding noise at each stage."},
    "clarity": {"score": 4, "rationale": "Very well-organized three-stage approach with specific architectural details (layers 16-20, 3-layer MLP ~2M params, LoRA rank 32 ~5M params, focal loss with λ=0.1). Clear baselines, ablations, and evaluation protocol. Landscape is comprehensive."},
    "impact": {"score": 3, "rationale": "If the robustness hypothesis holds (affordance-grounded features resist distribution shift better than generic attention), this is useful but not transformative. The hypothesis faces headwinds: LIBERO-Plus shows VLAs ignore language instructions entirely, yet AffordVLA's open-vocabulary advantage depends on language conditioning. AFI achieves +23.5% OOD improvement using affordance at inference time — unclear if training-time-only affordance produces comparable robustness gains."}
  },
  "issues": [
    "CRITICAL OMISSION — SG-VLA (arXiv 2603.22760, Mar 2026): Uses auxiliary decoders predicting grasp affordances (among other signals: robot position, joint configs, relative pose, segmentation masks) from shared visual-language features in a VLA framework. This is the most architecturally similar concurrent work — auxiliary affordance prediction training within a VLA. Must be included in landscape and differentiated from AffordVLA's open-vocabulary affordance heatmaps.",
    "NOVELTY CONCERN — Structural similarity to PALM is underemphasized: Both PALM and AffordVLA (1) generate affordance pseudo-labels from external frozen models during training, (2) add auxiliary affordance prediction heads to VLA intermediate layers, (3) drop those heads at inference for zero overhead. The only architectural delta is the pseudo-label type (4 structured types vs. open-vocabulary heatmaps). This needs a stronger differentiating technical contribution beyond changing the label generation pipeline.",
    "ROBUSTNESS HYPOTHESIS FACES CONTRADICTORY EVIDENCE: LIBERO-Plus (the primary evaluation benchmark) demonstrates that VLAs 'tend to ignore language instructions completely' and exhibit 'positional bias rather than genuine semantic understanding.' If models ignore language, how will language-conditioned affordance features help robustness? The proposal's core claim — that affordance-grounded features resist distribution shift — is undermined by evidence that the problem is deeper than feature quality (it's about fundamental model behavior).",
    "MISSING COMPARISON — Affordance at training-time vs. inference-time: AFI (arXiv 2512.07472) achieves +23.5% OOD improvement by using affordance at inference time as an external plug-in. AffordVLA uses affordance only during training (head dropped at inference). It's not obvious that training-time affordance regularization will match inference-time affordance guidance for robustness. This comparison should be explicitly discussed and ideally tested (AffordVLA + AFI combination vs. each alone).",
    "PSEUDO-LABEL QUALITY PIPELINE UNADDRESSED: The VLM→text description→GroundingDINO→spatial heatmap pipeline compounds errors at each stage. VLM may hallucinate incorrect affordance descriptions; GroundingDINO may mislocalize described regions. No quality filtering, confidence thresholding, or noise-robustness strategy is proposed. This is critical because the entire approach depends on pseudo-label quality.",
    "AUXILIARY PREDICTION PARADIGM SATURATION: QDepth-VLA (depth), DreamVLA (NeurIPS 2025, semantics+depth+dynamics), SG-VLA (grasp affordance+pose+segmentation), RS-CL (robot state contrastive), PALM (4 affordance types) — the paradigm of 'add auxiliary prediction head to VLA intermediate representations' is well-explored. Reviewers may perceive AffordVLA as 'yet another auxiliary loss variant' unless the open-vocabulary affordance framing provides demonstrably different (not just theoretically different) representations.",
    "VENUE MISMATCH PERSISTS: User originally requested CoRL 2026. CoRL 2026 deadline is May 29, 2026 (11 days away) — correctly acknowledged as impossible. But the proposal targets ICRA 2027 (expected Sep 2026 deadline), which doesn't match the user's original venue preference. This is a constraint the user set that cannot be met."
  ],
  "feedback": "The revision substantially improved by addressing PALM, FocusVLA, UAD, supervision signal, and compute budget from Round 1. However, new issues require attention:\n\n1. **Add SG-VLA to landscape and baselines**: SG-VLA (Mar 2026) is the most architecturally similar concurrent work — it uses auxiliary affordance prediction within a VLA. Differentiate explicitly: SG-VLA uses task-specific grasp affordance; AffordVLA uses open-vocabulary language-conditioned affordance heatmaps.\n\n2. **Strengthen differentiation from PALM beyond pseudo-label type**: Currently AffordVLA ≈ PALM with different pseudo-labels. Consider: (a) adding a contrastive loss that explicitly enforces that affordance representations cluster by interaction type rather than object appearance (leveraging exploration direction #3 from the original spec); (b) demonstrating that open-vocabulary pseudo-labels enable a curriculum/data-augmentation strategy impossible with PALM's fixed types (e.g., VLM-generated paraphrases of affordance descriptions as augmentation); (c) showing that the VLM-conditioned heatmap captures qualitatively different spatial patterns than PALM's decomposed types.\n\n3. **Address the LIBERO-Plus language-insensitivity finding**: LIBERO-Plus shows VLAs ignore language. Either: (a) argue that affordance supervision forces the model to attend to language (cite evidence), (b) add a language-conditioned ablation testing whether affordance loss improves language sensitivity, or (c) reframe the robustness story around visual affordance invariance rather than language conditioning.\n\n4. **Add pseudo-label quality analysis**: Propose confidence-based filtering of pseudo-labels (e.g., GroundingDINO confidence threshold), or a consistency check (same object under paraphrased instructions should produce similar heatmaps — your exploration direction #5). This addresses a key feasibility concern.\n\n5. **Explicitly compare training-time vs. inference-time affordance**: Include AFI as a baseline. Test: (a) AffordVLA alone (training-time affordance), (b) AFI alone (inference-time affordance), (c) AffordVLA + AFI (both). If (c) >> (b), this proves training-time affordance provides unique value. If (b) ≈ (a), the training-time approach is insufficient.\n\n6. **Acknowledge and address the 'auxiliary loss saturation' reviewer concern**: Explicitly argue why affordance-specific auxiliary loss produces qualitatively different representations than depth (QDepth-VLA), semantics (DreamVLA), or robot state (RS-CL) auxiliary losses. The argument should be grounded in the probing study (2602.20501): affordance encodes *interaction* geometry, not just scene geometry.",
  "reason": "Substantially improved from Round 1 but incremental novelty over PALM (same architecture pattern with different pseudo-labels), missing SG-VLA as critical concurrent work, and unresolved tension between language-conditioned affordance and LIBERO-Plus evidence that VLAs ignore language."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ff17904-2622-4a3a-85a0-9ced85d12c97",
  "isSidechain": false,
  "requestId": "req_011CbAaN15RJG8jCe6zNMzgN",
  "type": "assistant",
  "uuid": "6db8be1b-a9b5-447b-bda4-98c450a19267",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EC3nBhWEbHQi2hFEkfd3gY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1066,
      "cache_read_input_tokens": 66182,
      "output_tokens": 5136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5136,
          "cache_read_input_tokens": 66182,
          "cache_creation_input_tokens": 1066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1066
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

_source line 141_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "6db8be1b-a9b5-447b-bda4-98c450a19267",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 142_

```json
{
  "type": "ai-title",
  "aiTitle": "AffordVLA: Open-vocabulary affordance distillation into VLA for robust manipulation",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 143_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-18 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "6db8be1b-a9b5-447b-bda4-98c450a19267",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---

### Runtime record

_source line 144_

```json
{
  "type": "ai-title",
  "aiTitle": "AffordVLA: Open-vocabulary affordance distillation into VLA for robust manipulation",
  "sessionId": "bab35da4-a4d1-43b7-8915-527f62f88ec1"
}
```

---
