# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-11 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 69
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/52683256-87d3-4685-99bf-86185e903121.jsonl`
- **Structured JSON:** [`99a2a8ec9114c3c485b2.json`](../../sessions/99/99a2a8ec9114c3c485b2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T00:19:06.839Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T00:19:06.839Z",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-11 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 6/10)\n{\n  \"title\": \"GranRoute: When Does Structural Retrieval Granularity Matter for Repository-Level Code Repair?\",\n  \"core_problem\": \"Repository-level LLM-based code repair systems use fixed fault-localization granularity (file/function/line) and fixed context budgets, despite growing evidence that the optimal retrieval configuration is instance-dependent. Two April 2026 empirical studies confirm this: arXiv 2604.00167 shows function-level FL beats file- and line-level on average but the ranking shifts across difficulty tiers, and arXiv 2604.05481 finds that file-level context yields 15–17× improvement while line-level expansion causes noise amplification — yet neither proposes an adaptive selection method. Holloway et al. (NeurIPS 2024 ML for Systems Workshop) explicitly call for 'context granularity strategies tailored to specific bug types' but provide no method.\\n\\nHowever, recent work raises a critical counter-question: does retrieval configuration even matter, or is the bottleneck downstream context utilization? SWEzze (arXiv 2603.28119) shows that compressing retrieved code by 6× (removing 51–71% of tokens) improves issue resolution by 5–9.2%, because retrieved contexts have only 8.4% relevance density. Du & Tian (arXiv 2510.05381) find 13.9–85% performance degradation from context length growth even with perfect retrieval, with at least 7.9% degradation persisting even when distractor tokens are replaced with whitespace. If removing context helps, does selecting the 'right' retrieval configuration matter?\\n\\nWe argue yes, because this framing conflates two orthogonal dimensions: **structural selection** (which program abstraction level — file, function, or line — defines the unit of retrieval) and **quantitative compression** (how many tokens to retain within a chosen structural level). The strongest evidence for this distinction is the arXiv 2604.05481 finding that line-level context *hurts* despite containing fewer tokens per element than file-level. If the bottleneck were purely quantitative, line-level should always win (less text = less noise). Instead, line-level fails because isolated lines lack the semantic coherence of functions or files — the structural boundaries themselves determine how effectively the LLM reasons about code. SWEzze operates at a fixed structural level (function-level) and compresses within it; it never asks *which* structural level to use. GranRoute addresses this complementary upstream question.\\n\\nA second counter-argument is that compute budget may be better spent on diverse patch generation rather than retrieval optimization. Top SWE-bench systems (Devlo at 70.2%) achieve results through multi-LLM diverse sampling, and arXiv 2405.17503 frames the dominant lever as sampling diversity. We acknowledge this but note that GranRoute operates on the *input* side (retrieval configuration) while diversity operates on the *output* side (patch generation). Critically, GranRoute's routing cost is near-zero — an embedding lookup plus a lightweight classifier, no LLM calls — so it does not compete for the compute budget allocated to diverse sampling. Input quality (retrieval configuration) determines the *ceiling* of what any single sample can achieve; output diversity determines how close the system gets to that ceiling. They should compose.\\n\\nThe gap that remains: the granularity routing literature (MoG, COLING 2025; LTRR, SIGIR 2025) and the adaptive retrieval HP literature (AutoRAG-HP, EMNLP 2024 Findings) have not been extended to code repair's structurally richer setting, where granularity choices represent distinct program abstractions, end-task repair success is the training signal, and code-specific routing signals (stack traces, error types, code structure) are available. No existing work learns to jointly select (fault-localization granularity, context budget) per issue for code repair.\",\n  \"opportunity\": \"The core empirical question this paper answers is: **Does the structural abstraction level of retrieved context matter per-instance for LLM code repair, independently from context quantity — and if so, can simple methods predict the optimal level?**\\n\\nThis question is motivated by the convergence of three threads with an unresolved tension:\\n\\n(1) **Granularity matters per-instance in code repair** (arXiv 2604.00167, 2604.05481, Holloway et al. NeurIPS 2024), but no adaptive method exists.\\n\\n(2) **Context compression alone helps** (SWEzze, arXiv 2510.05381), raising the question of whether retrieval *configuration* is secondary to retrieval *compression*.\\n\\n(3) **Granularity routing works in text QA** (MoG, COLING 2025) and **simple methods suffice for model routing** (kNN matches learned routers, arXiv 2505.12601), but neither has been tested in the structurally richer code repair setting.\\n\\nThe tension between (1) and (2) is precisely what makes this paper interesting. If granularity selection and compression are redundant, GranRoute adds nothing — SWEzze already solves the problem. If they are complementary — as we hypothesize based on the structural vs. quantitative distinction — then GranRoute addresses a dimension that compression cannot: which program abstraction level defines the unit of reasoning. The pilot is designed to resolve this tension empirically.\\n\\nCode repair introduces three specific challenges that distinguish it from prior routing work: (a) the configuration space is 2D (granularity × budget) with hypothesized *interaction effects* — the optimal budget likely depends on the granularity level, because file-level elements are self-contained while line-level elements lack structural coherence; (b) the oracle signal must be end-task repair success, not retrieval similarity (MoG) or LLM-as-judge scores (AutoRAG-HP); (c) code-specific routing signals (stack trace structure, error type, cyclomatic complexity) may enable more effective routing than generic text embeddings.\\n\\nA critical empirical sub-question, raised by arXiv 2505.12601, is whether the kNN simplicity advantage demonstrated for model routing transfers to configuration routing. If kNN suffices, the structural complexity of the 2D configuration space is navigable without parametric learning. If not, the interaction effects between granularity and budget justify learned methods. GranRoute is designed to answer this through systematic comparison.\\n\\nSeleCom (arXiv 2602.15856) provides independent evidence for our complementarity argument: it shows that selection and compression compose because 'full-compression approaches dilute query-relevant signals by treating all content equally.' GranRoute is upstream selection (structural level); SWEzze/SeleCom is downstream compression (token reduction).\",\n  \"landscape\": \"**Granularity-dependence evidence in code repair:** Holloway & Elenberg (NeurIPS 2024 ML for Systems Workshop) study 6 context granularities on 109 Defects4J bugs, finding sliced context achieves 79% Correct/Plausible ratio, and explicitly motivate tailored strategies as future work. arXiv 2604.00167 (50 instances, 2 repos) finds function-level at 45.6% vs. file-level at 42.6% with rankings shifting across difficulty tiers. arXiv 2604.05481 (500 instances, 61 configurations) finds file-level context yields 15–17× improvement while line-level expansion amplifies noise — crucially, this shows structural level matters independently from context quantity.\\n\\n**Context compression and the quantitative bottleneck:** SWEzze (arXiv 2603.28119) compresses code context by 6× (51–71% token reduction) at fixed function-level granularity, improving resolution by 5–9.2% on SWE-bench Verified with Agentless, SWE-agent, and Moatless — because retrieved contexts have only 8.4% relevance density. Du & Tian (arXiv 2510.05381) show 13.9–85% performance degradation from context length even with perfect retrieval, with at least 7.9% residual degradation from length alone (whitespace-replaced distractors). SWE-Pruner (arXiv 2601.16746) performs adaptive neural skimming at fixed granularity. SeleCom (arXiv 2602.15856) demonstrates that selection and compression are complementary: query-conditioned selection first, then compression of selected spans, reducing computation by 33.8–84.6% while maintaining quality. These papers establish that context quantity is a bottleneck but operate within a fixed structural level — none addresses which structural level to use.\\n\\n**Sampling diversity vs. input optimization:** arXiv 2405.17503 frames code repair as a bandit problem and argues the dominant lever is sampling diversity. arXiv 2502.11027 finds prompt perturbations that increase diversity improve Best-of-N by ~10% but harm majority voting, revealing the mechanism as exploration breadth. Top SWE-bench systems (Devlo at 70.2%) use multi-LLM diverse sampling. However, BEST-Route (ICML 2025) jointly optimizes model selection AND sampling count, suggesting input and output optimization compose. Input quality determines the ceiling; output diversity determines proximity to the ceiling.\\n\\n**Granularity routing in text QA:** Mix-of-Granularity (MoG, COLING 2025, arXiv 2406.00456) trains a MLP router to select optimal text chunking granularity (5 levels: {1/2, 1, 2, 4, 8}× base chunk size) for RAG. The router takes RoBERTa query embeddings and is trained with BCE loss using soft labels derived from BM25 retrieval similarity. MoG is the closest prior work on granularity routing; key differences: (1) 1D chunk-size routing vs. our 2D (granularity × budget) space with interaction effects, (2) retrieval-similarity soft labels vs. end-task repair labels, (3) text QA vs. code repair with code-specific signals. FreeChunker (arXiv 2510.20356) critiques MoE-based chunking methods as 'fundamentally bounded by the capabilities of the underlying chunker experts.'\\n\\n**Adaptive retrieval HP tuning:** AutoRAG-HP (EMNLP 2024 Findings, arXiv 2406.19251) formulates RAG hyperparameter tuning as online multi-armed bandit, tuning top-k, compression ratio, and embedding model via Hierarchical UCB. Key differences from GranRoute: AutoRAG-HP optimizes *globally* (one best config for the entire dataset, not per-instance), operates *online* (sequential exploration), and tunes *numeric/categorical* parameters (top-k values, compression ratios), while GranRoute routes per-instance over *structurally distinct program abstractions* (file/function/line) using *offline* trained routers with *end-task* repair success labels.\\n\\n**LLM routing methods:** RouteLLM (ICLR 2025, arXiv 2406.18665) trains 4 router architectures from preference data. RADAR (arXiv 2509.25426) uses IRT for difficulty-aware routing. BEST-Route (ICML 2025, arXiv 2506.22716) routes model + sampling count. LTRR (SIGIR 2025, arXiv 2506.13743) frames retriever selection as learning-to-rank, finding pairwise XGBoost outperforms neural rankers. arXiv 2505.12601 demonstrates kNN matches or outperforms learned routers for model selection — directly motivating our central methodological question.\\n\\n**RAG-aware routing and configuration adaptation:** RAGRouter (NeurIPS 2025, arXiv 2505.23052) routes queries to the best RAG-LLM — model selection, not retrieval configuration. METIS (SOSP 2025, arXiv 2412.10543) jointly adapts RAG configuration (chunk count + synthesis method) per query, achieving 1.6–2.5× latency reduction — the closest configuration-level adaptation, but in general QA with latency focus. GraphRAG-Router (arXiv 2604.16401) uses RL to route over GraphRAG infrastructure.\\n\\n**Code repair with adaptive components:** Triage (arXiv 2604.07494) routes SWE-bench tasks to cost-effective LLM tiers — model routing, not retrieval config. ProCC (TOSEM 2025, arXiv 2405.07530) uses contextual bandits to select retrieval perspectives for code completion — adaptive retrieval in the code domain but for completion with online bandits, not repair with offline routing. AdaPatcher (AAAI 2025, arXiv 2503.06510) adapts repair via DPO at fixed localization. SIADAFIX (arXiv 2510.16059) classifies issues into difficulty modes via NL features but does not adapt FL granularity. ARISE (arXiv 2605.03117) builds multi-granularity program graphs with fixed representations.\\n\\n**The gap:** Structural granularity selection and context compression are complementary dimensions (established by SeleCom, arXiv 2602.15856). Compression (SWEzze, SWE-Pruner) addresses how many tokens to retain within a structural level. Granularity routing (MoG) addresses which text chunking size to use for QA. AutoRAG-HP tunes retrieval hyperparameters globally online. But no work targets per-instance selection of which program abstraction level (file/function/line) and what context budget to use for code repair, where structural boundaries determine reasoning effectiveness independently from context quantity.\",\n  \"approach\": \"We propose GranRoute, a retrieval configuration routing framework for code repair that learns to select the optimal (granularity, context budget) pair per issue. GranRoute integrates upstream of any retrieval-based repair pipeline as a plug-in module, complementing downstream context compression.\\n\\nThe paper is organized around two research questions that distinguish it from prior routing work:\\n- **RQ1 (Structural abstraction):** Does per-instance structural granularity routing improve code repair independently from context compression? Specifically: does GranRoute compose with downstream compression, or are they redundant?\\n- **RQ2 (Routing methods):** Does the kNN simplicity advantage observed in model routing (arXiv 2505.12601) transfer to code repair configuration routing, or does the 2D configuration space with interaction effects favor parametric methods?\\n\\n**Phase 1 — Headroom & Interaction Pilot (2 days):** Run the Agentless pipeline via API (Qwen3-Coder-Next, ~$0.08/instance) across 12 configurations (3 granularities: file/function/line × 4 context budgets: 3, 5, 8, 12 retrieved elements) on 50 SWE-bench Verified instances, 3 runs each (majority-vote labels). Compute:\\n(a) **Accuracy headroom:** Oracle accuracy (per-instance best config) minus best fixed-config accuracy.\\n(b) **Cost-efficiency headroom:** Average tokens consumed by oracle-selected configs vs. best fixed config.\\n(c) **Configuration diversity:** How many distinct configurations appear in the oracle set.\\n(d) **Interaction analysis:** For each granularity level, compute the optimal budget distribution. Test whether the optimal budget depends on granularity using a two-way contingency analysis (chi-squared or Fisher's exact test). **Interaction hypothesis:** File-level elements are self-contained, so larger budgets (8–12) help by providing broader context; line-level elements lack structural coherence, so larger budgets amplify noise (consistent with arXiv 2604.05481) and smaller budgets (3–5) are optimal; function-level has an intermediate optimum. If interaction effects exist, the 2D configuration space does not decompose into two independent 1D problems, justifying joint routing over MoG's 1D approach.\\n(e) **Compression composition test:** For the 50 pilot instances, additionally run the best-fixed config and oracle-selected config with a simple post-retrieval compression (retain top 50% of retrieved elements by BM25 relevance, approximating SWEzze-style filtering). Compare: best-fixed, best-fixed+compression, oracle-selected, oracle-selected+compression. If oracle+compression > compression-only, structural selection adds value beyond compression.\\n\\n**Go/no-go gate:** If accuracy headroom < 3pp AND cost savings < 15% AND no significant interaction effects AND compression-only matches oracle-selected: the structural selection dimension adds negligible value, and we pivot to a diagnostic study analyzing why code repair is configuration-invariant despite text QA being configuration-sensitive. If accuracy headroom is modest (3–5pp) but interactions exist or compression composition shows gains: proceed with focused framing on when and why structural granularity matters.\\n\\n**Phase 2 — Oracle Collection (3 days):** Extend to 300 SWE-bench Verified instances across the same 12 configurations, 3 runs each (total: 10,800 API calls, ~$864). Each instance receives per-configuration success rates via majority vote. Cost: ~$864.\\n\\n**Phase 3 — Training Data Construction (1 day):** Construct training data: (a) Classification labels: best-performing config per instance (ties broken by cost). (b) Preference pairs: (issue_text, winning_config, losing_config) from success/failure outcomes. (c) kNN support set: (issue_embedding, config_performance_vector) pairs. Extract features: NL features from issue text (via CodeSage-base encoder, 356M), hand-crafted NL features (error-type keywords, stack trace depth, code entity count, description length, location specificity score), and lightweight code-structural features from localized files (cyclomatic complexity, file size, import count, class/function ratio).\\n\\n**Phase 4 — Router Training with Multi-Method Comparison (2 days):** Train and compare 4 core routing methods, organized to answer RQ2:\\n(a) **kNN router** on CodeSage-base embeddings — the critical simplicity baseline motivated by arXiv 2505.12601. Uses k-nearest neighbor retrieval in embedding space with majority voting over oracle-optimal configurations.\\n(b) **Random forest** on hand-crafted NL+code features — a standard ML baseline, motivated by LTRR's finding that tree-based methods outperform neural rankers.\\n(c) **MLP classifier** on CodeSage-base embeddings — standard neural classification baseline, comparable to MoG's MLP router but with end-task labels.\\n(d) **Bradley-Terry preference router** on CodeSage-base embeddings with a scoring head trained via preference loss — motivated by RouteLLM's paradigm.\\nSupplementary methods (reported in appendix): LambdaMART learning-to-rank on combined features, IRT-based difficulty router.\\nAll methods operate in two variants: NL-only (zero pre-routing cost) and NL+Code (minimal cost after initial file localization), addressing the signal question within RQ2. Training is lightweight: ~7 H100-hours total.\\n\\n**Phase 5 — Evaluation (3 days):** Evaluate on ~100 SWE-bench-Live instances from recent monthly batches (confirmed operational: 50 new issues/month since mid-2025). Plan for ~10–15% Docker failures, targeting 85–90 evaluated instances. Fallback: if fewer than 80 SWE-bench-Live instances are available, supplement with a stratified held-out split from SWE-bench Verified, noting the weaker decontamination guarantee. Use the full Agentless pipeline.\\n\\nBaselines and conditions: (a) best fixed-granularity configuration, (b) random configuration, (c) MoG-adapted baseline (MLP + soft labels retrained on our code repair data), (d) best-fixed + post-retrieval compression (addresses whether compression alone suffices), (e) GranRoute (best method from RQ2), (f) GranRoute + compression (tests composition), (g) oracle upper bound.\\nReport: end-to-end repair rate, routing accuracy, cost efficiency, calibration. Key analyses: (1) GranRoute vs. compression-only: does structural selection add value? (2) GranRoute + compression vs. each alone: do they compose? (3) kNN vs. learned methods (RQ2), (4) NL-only vs. NL+Code feature ablation, (5) MoG-adapted vs. end-task-trained methods.\\n\\n**Phase 6 — Analysis (concurrent, 2 days):** SHAP-based feature importance on the best-performing router. Target question: which NL features predict optimal structural granularity? If stack trace depth or error type dominate, this explains why code repair routing requires different signals from text QA routing (where MoG uses generic query embeddings). Interaction analysis: visualize the granularity × budget performance surface to characterize when structural level matters most.\\n\\n**Narrative framing by outcome:**\\n- If GranRoute + compression > compression alone: 'Structural selection and context compression are complementary dimensions — GranRoute selects *what program abstraction* to retrieve; compression reduces *how much* to retain. Together they outperform either alone.' Strong contribution.\\n- If compression alone matches GranRoute: 'Structural granularity matters less than context quantity for code repair — a surprising finding that contrasts with text QA (MoG) and suggests LLMs are robust to structural boundaries when context is sufficiently compressed.' Diagnostic contribution.\\n- If kNN dominates: 'Configuration routing in code repair, like model routing, is solved by simple non-parametric methods.' If learned methods dominate: 'The 2D configuration space with interaction effects requires parametric learning, unlike model routing.'\\n- If headroom < 3pp: pivot to diagnostic study.\\n\\nThe contribution hierarchy leads with the empirical question, not the framework: (1) **Empirical finding** answering whether per-instance structural granularity selection matters for code repair independently from context compression — testing whether the structural vs. quantitative distinction holds in practice; (2) **Methodological comparison** of 4 routing methods testing whether kNN sufficiency transfers from model routing to configuration routing; (3) **Interpretable analysis** connecting code-specific NL bug features to optimal structural granularity, explaining when and why code repair routing differs from text QA routing; (4) **GranRoute framework** as the practical vehicle for these findings — a plug-in module that complements downstream compression.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~25–40h H100 (7h for 4-method router training, 8–15h for feature extraction/analysis, 5–10h for ablation experiments including MoG-adapted baseline and supplementary methods; all Agentless runs are API-based)\",\n      \"gpu_utilization\": \"Low (~15–25%). Most compute is API-based. Local GPU used for encoder inference and router training.\",\n      \"timeline\": \"14 days (tight for EMNLP ARR May 25 deadline)\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"$75–120\",\n      \"api_cost\": \"$1,150–1,550 (pilot with interaction+composition: 1,800 runs × $0.08 + ~200 compression runs × $0.08 ≈ $160; oracle: 10,800 runs × $0.08 ≈ $864; evaluation: ~100 instances × (7 conditions) × 3 runs × $0.08 ≈ $168; iteration/debugging: ~$100)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~35–50h H100 (agent explores router architectures including kNN variants, feature combinations, and supplementary methods)\",\n      \"gpu_utilization\": \"Low-moderate (~25–35%). Agent queues API runs between check-ins.\",\n      \"timeline\": \"10–12 days\",\n      \"team\": \"1 researcher, ~30min/day for reviewing interaction analysis, validating composition results, approving evaluation plan\",\n      \"claude_api_cost\": \"$100–200\",\n      \"estimated_gpu_cost\": \"$105–150\",\n      \"api_cost\": \"$1,300–1,800 (more configs explored for interaction analysis, robustness checks)\",\n      \"risk_note\": \"SWE-bench Docker setup failures on ~10–15% of instances may require human triage.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~60–110h H100 (agent explores neural router variants, kNN hyperparameter sweeps, extensive interaction and composition analysis)\",\n      \"gpu_utilization\": \"Moderate (~35–50%).\",\n      \"timeline\": \"8–10 days\",\n      \"team\": \"0 (only initial setup)\",\n      \"claude_api_cost\": \"$250–500\",\n      \"estimated_gpu_cost\": \"$180–330\",\n      \"api_cost\": \"$1,700–2,600 (agent explores 15+ configs, composition experiments with multiple compression ratios)\",\n      \"speed_bottleneck\": \"API rate limits and SWE-bench Docker setup (~2min/container).\",\n      \"risk_note\": \"Agent may over-engineer router architecture — explicitly instruct to prioritize interaction analysis and composition experiment as the paper's central empirical questions.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings short paper via ARR May cycle (submission: May 25, 2026) — tight 14-day window, feasible for focused 4-page empirical paper; Findings suits the domain-transfer and empirical question framing\",\n    \"ICSE 2027 Research Track (abstract: June 23, 2026; paper: June 30, 2026) — comfortable timeline for full-length version with 6 methods, encoder ablation, and expanded composition analysis\",\n    \"AAAI 2027 (abstract: July 25, 2026; paper: August 1, 2026) — suits the routing/configuration learning angle\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation (COLING 2025, arXiv 2406.00456) — trains MLP router to select text chunking granularity via soft labels; closest prior work on granularity routing, but 1D chunk-size space with retrieval-similarity labels in text QA vs. our 2D (granularity × budget) space with end-task repair labels in code repair\",\n    \"AutoRAG-HP: Automatic Online Hyper-Parameter Tuning for Retrieval-Augmented Generation (EMNLP 2024 Findings, arXiv 2406.19251) — formulates RAG HP tuning as online multi-armed bandit with Hierarchical UCB; tunes top-k, compression ratio, embedding model globally (one best config per dataset), while GranRoute routes per-instance over structurally distinct program abstractions offline\",\n    \"SWEzze: Compressing Code Context for LLM-based Issue Resolution (arXiv 2603.28119) — 6× compression (51–71% token reduction) improves resolution by 5–9.2%; establishes that context quantity is a bottleneck but operates at fixed structural granularity; GranRoute addresses the complementary upstream question of which structural level to use\",\n    \"Context Length Alone Hurts LLM Performance Despite Perfect Retrieval (arXiv 2510.05381) — 13.9–85% degradation from length even with perfect retrieval; motivates the structural vs. quantitative distinction: if length hurts regardless, the structural boundaries that define reasoning units matter even more\",\n    \"Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers (arXiv 2505.12601) — kNN matches/outperforms learned routers for model selection; directly motivates RQ2 on whether this simplicity advantage transfers to configuration routing\",\n    \"SeleCom: Query-Conditioned Selection and Compression for RAG (arXiv 2602.15856) — demonstrates selection and compression are complementary ('full-compression dilutes query-relevant signals'); supports our argument that structural selection (GranRoute) and token compression (SWEzze) address different dimensions\",\n    \"On the Effect of Sampling Diversity in LLM Inference (arXiv 2502.11027) — prompt perturbations that increase diversity improve Best-of-N by ~10%; positions output diversity and input quality as complementary, not competing, optimization axes\",\n    \"Exploration-Exploitation in Code Repair (arXiv 2405.17503) — frames code repair as bandit problem, argues sampling diversity is dominant lever; GranRoute is orthogonal (input-side routing vs. output-side diversity) with near-zero routing cost\",\n    \"RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models (NeurIPS 2025, arXiv 2505.23052) — first RAG-aware router using document and RAG capability embeddings; model selection (which RAG-LLM), not retrieval configuration\",\n    \"ProCC: Prompt-based Code Completion via Multi-Retrieval Augmented Generation (TOSEM 2025, arXiv 2405.07530) — adaptive retrieval perspective selection via contextual bandits for code completion; validates adaptive retrieval in code domain but targets completion with online bandits, not repair with offline routing\",\n    \"METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation (SOSP 2025, arXiv 2412.10543) — jointly adapts RAG configuration per query; closest configuration-level adaptation but in general QA with latency focus\",\n    \"Holloway & Elenberg, 'On the Role of Context Granularity in LLM-Driven Program Repair' (NeurIPS 2024 ML for Systems Workshop) — studies 6 granularities, explicitly motivates tailored strategies\",\n    \"RouteLLM: Learning to Route LLMs with Preference Data (ICLR 2025, arXiv 2406.18665) — 4 router architectures from preference data; methodological parallel for preference-based routing\",\n    \"RADAR: Reasoning-Ability and Difficulty-Aware Routing for Reasoning LLMs (arXiv 2509.25426) — IRT-based difficulty-aware routing; inspires supplementary IRT variant\",\n    \"BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute (ICML 2025, arXiv 2506.22716) — jointly routes model + sampling count; supports composability of input and output optimization\",\n    \"LTRR: Learning To Rank Retrievers for LLMs (SIGIR 2025, arXiv 2506.13743) — pairwise XGBoost outperforms neural rankers for retriever selection; motivates random forest baseline\",\n    \"Triage: Routing Software Engineering Tasks to Cost-Effective LLM Tiers (arXiv 2604.07494) — model-tier routing via code health metrics\",\n    \"A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks (arXiv 2604.00167) — function-level at 45.6% vs file-level at 42.6%, rankings shift across difficulty tiers\",\n    \"On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481) — 61 configurations on 500 instances, line-level noise amplification despite being more targeted; key evidence that structural boundaries matter independently from context quantity\",\n    \"RPO: Retrieval Preference Optimization for Robust RAG (ACL 2025, arXiv 2501.13726) — DPO-style preference learning for adaptive retrieval\",\n    \"AdaPatcher: Less is More — Adaptive Program Repair with Bug Localization and Preference Learning (AAAI 2025 oral, arXiv 2503.06510)\",\n    \"CodeSage: Code Representation Learning At Scale (ICLR 2024) — primary code encoder (356M params)\",\n    \"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents (arXiv 2601.16746) — adaptive neural skimming at fixed granularity\",\n    \"SIADAFIX: Issue Description Response for Adaptive Program Repair (arXiv 2510.16059) — NL difficulty classification, does not adapt FL granularity\",\n    \"ARISE: A Repository-level Graph Representation for Agentic FL and Repair (arXiv 2605.03117) — multi-granularity program graphs with fixed representations\",\n    \"FreeChunker: A Cross-Granularity Chunking Framework (arXiv 2510.20356) — critiques MoE-based granularity methods\",\n    \"SWE-bench Goes Live! (NeurIPS 2025 D&B, arXiv 2505.23419)\",\n    \"Agentless: Demystifying LLM-based Software Engineering Agents (FSE 2025)\",\n    \"GraphRAG-Router: Cost-Efficient Routing over GraphRAGs and LLMs (arXiv 2604.16401)\"\n  ],\n  \"description\": \"Recent evidence shows that optimal fault-localization granularity is instance-dependent in LLM code repair (arXiv 2604.00167, 2604.05481), but a strong counter-argument holds that context compression alone suffices — SWEzze improves resolution by 5–9.2% through 6× token reduction, and context length degrades performance even with perfect retrieval (arXiv 2510.05381). We argue these findings are complementary, not competing: compression addresses context *quantity* (how many tokens to retain), while granularity selection addresses *structural abstraction* (which program unit — file, function, or line — defines the reasoning boundary). The evidence that line-level context *hurts* despite containing fewer tokens (arXiv 2604.05481) directly supports this distinction.\\n\\nWe propose GranRoute, a near-zero-cost routing module that selects (fault-localization granularity, context budget) per issue — a 2D configuration space with hypothesized interaction effects (optimal budget depends on structural level). Our pilot (50 SWE-bench Verified instances, 12 configs, ~$160) tests three premises: (1) accuracy headroom exists, (2) granularity and budget interact, (3) routing composes with compression. We then systematically compare 4 routing methods — kNN, random forest, MLP, and Bradley-Terry preference router — testing whether kNN sufficiency (arXiv 2505.12601) transfers from model routing to configuration routing. All methods operate in NL-only and NL+Code variants. Evaluation on ~100 SWE-bench-Live instances includes a MoG-adapted baseline and composition conditions (GranRoute + compression vs. compression alone). SHAP analysis identifies which bug features predict optimal structural granularity.\\n\\nThe contribution is framed as an empirical investigation: (1) does structural granularity matter per-instance independently from compression? (2) can simple methods predict the optimal level? (3) what bug features drive the structural abstraction choice? GranRoute is the vehicle for these findings. API-based oracle collection (~$864), <40 H100-hours GPU. Primary target: EMNLP 2026 Findings (ARR May 25).\",\n  \"project_name\": \"adaptive_context_orchestration\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"FATAL: Compute budget violation — proposal minimum (600-800 A100-hours ≈ 300-400 H100-equiv) is 2-4x the user's hard constraint of ≤200 H100-hours. Oracle profiling of 18 configs × 200+ instances with a self-hosted 80B model is the dominant cost and cannot be reduced without fundamentally changing the approach.\", \"FATAL: Timeline violation — manual estimate is 4-6 months, human-in-loop is 6-10 weeks, even auto mode is 10-18 days with 4× A100s. The 16-day constraint is incompatible with exhaustive oracle profiling.\", \"Poor EMNLP venue fit — the contribution is repair pipeline orchestration (an SE topic), not NLP/code understanding. The ML component (fine-tuning a 0.6B cross-encoder for 18-way classification) is too thin for an NLP venue. This work fits ICSE/ASE/FSE far better.\", \"Missing key competitor: AdaPatcher (AAAI 2025 oral, arXiv 2503.06510) — an adaptive program repair method with learned bug localization and preference learning — was not cited or discussed in the landscape.\", \"Oracle label noise: the Agentless pipeline has inherent randomness (temperature, sampling). Single runs per (config, instance) pair yield noisy training labels. Multiple runs per config would further inflate compute costs.\", \"Weak empirical foundation: the function-level FL granularity study (arXiv 2604.00167) was conducted on SWE-bench Mini (only 50 instances). Extrapolating that adaptive granularity selection will yield significant gains on the full 500-instance Verified set is speculative.\", \"SWE-bench Verified contamination: OpenAI's audit confirmed frontier models are contaminated on this benchmark, and 59.4% of hard tasks have flawed tests. Using it for both oracle label collection AND evaluation creates validity concerns.\", \"Overlap with SWEzze: the proposal uses the same base model (Qwen3-Reranker-0.6B) and same general approach (train a cross-encoder to select context) as SWEzze. The delta is adding granularity selection, which may not justify a separate paper at a top venue.\"]\nFeedback: The core insight (adaptive granularity + context budget selection) is sound but the execution plan fundamentally violates the user's constraints. To make this viable for EMNLP 2026 within ≤200 H100-hours and ≤16 days, the generator must: (1) **Eliminate exhaustive oracle profiling** — instead of running 18 configs × N instances, use a much cheaper proxy: analyze the already-published results from arXiv 2604.00167 and 2604.05481 to derive heuristic-based labels, or use a small pilot (3-5 configs × 50 instances) with API-based models (not self-hosted 80B) to collect training signal. (2) **Reframe for EMNLP** — the current framing is SE-centric (fault localization, repair pipelines). To fit EMNLP's 'NLP and Code Models' track, reframe around code understanding: how do LLMs process code at different granularities? What structural features of code predict optimal context? This shifts from pipeline engineering to understanding LLM code comprehension. (3) **Cite AdaPatcher (AAAI 2025)** and SWE-ContextBench (arXiv 2602.08316) in the landscape. (4) **Use API-based models for oracle collection** (e.g., Qwen3-Coder-Next via API at ~$0.30/instance) instead of self-hosting, converting GPU cost to manageable API cost. (5) **Address SWE-bench contamination** — consider using SWE-bench-Live or SWE-rebench for evaluation instead of Verified. (6) **Reduce scope** — rather than a full learned policy with RL fine-tuning, consider a simpler but more insightful contribution: a systematic empirical study of what bug features predict optimal granularity, with a lightweight rule-based or logistic-regression selector. This is more achievable in 16 days and more publishable at EMNLP if paired with analysis of LLM code understanding at different granularities.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL: Contribution type mismatch — the user explicitly required 'METHOD ONLY: new training methods, retrieval-augmented code repair, or inference algorithms for code tasks.' This proposal self-describes as a 'large-scale empirical study' with a 'lightweight interpretable predictor' (logistic regression/GBDT). A logistic regression on hand-crafted features is not a new training method, retrieval-augmented repair, or inference algorithm. This fundamentally violates the user's requirements.\", \"CRITICAL: Missing competitor — Triage (arXiv 2604.07494, April 2026) trains an ML classifier to route SWE-bench tasks to cost-effective LLM tiers based on code quality signals. The methodology is nearly identical: lightweight classifier + pre-computed features → select optimal configuration. The only differences are feature source (code health metrics vs. NL features) and target variable (model tier vs. granularity/budget). This paper was not cited or discussed.\", \"Missing competitor — Holloway et al., 'On the Role of Context Granularity in LLM-Driven Program Repair' (NeurIPS 2024 ML for Systems Workshop), which studies 6 context granularities including backward static slicing on Defects4J and explicitly calls for 'future work should explore context granularity strategies tailored to specific bug types.' This is exactly the proposed work's research question, already articulated as a future direction.\", \"Missing competitor — AdaEdit/To Diff or Not to Diff (arXiv 2604.27296, April 2026) trains LLMs to dynamically choose the most token-efficient output format based on task features. Parallel concept: using task features to adaptively select configuration for downstream code operations.\", \"Arithmetic error in API cost: 9 configs × 300 instances × 3 runs × $0.30 = $2,430, not the claimed $810. The factor-of-3 error (seemingly forgetting the '× 3 runs') propagates into the total budget estimates. While per-instance costs with Qwen3-Coder-Next may be lower than $0.30, the stated math is wrong and undermines cost credibility.\", \"Terminology misattribution: The proposal attributes 'context rot' to arXiv 2604.05481, but that paper actually describes 'noise amplification' from line-level expansion. 'Context rot' is attributed to Chroma Research 2025, a separate source. The conflation weakens the theoretical framing.\", \"Small training set concern: 300 instances split into train/test (say 200/100) with 9 configuration labels, where many features are sparse (e.g., stack trace presence may be binary), may yield an underpowered feature analysis. SHAP values and mutual information on ~200 training instances with ~7 features and 9 target classes may not produce statistically robust insights.\", \"Uncertain headroom: If the best fixed configuration (e.g., function-level + 6 elements) already resolves 70-80% of what the oracle resolves, the predictor's improvement ceiling is narrow. The proposal does not estimate this headroom or discuss what happens if it is small.\"]\nFeedback: The core research question (what NL features predict optimal code context?) has merit, but the execution plan mismatches the user's requirements in a fundamental way. To make this viable:\n\n1. **Transform from empirical study to METHOD.** The user asked for 'new training methods, retrieval-augmented code repair, or inference algorithms.' Instead of a post-hoc empirical study + logistic regression, design a retrieval-augmented repair method that dynamically adapts its retrieval granularity and context budget during inference. For example: a meta-controller that encodes the NL issue description, predicts a retrieval configuration, executes retrieval at the predicted granularity, and feeds the result to the repair model — trained end-to-end (or via RL/DPO) to maximize repair success. This would be a genuine method contribution. The empirical analysis of NL features becomes a supporting analysis section, not the main contribution.\n\n2. **Cite and differentiate from Triage (arXiv 2604.07494).** This April 2026 paper does the same thing with code features → model tier. You must show why NL features for granularity/budget selection is a distinct and valuable contribution. The strongest argument: NL features are available before any code retrieval, enabling zero-cost pre-routing.\n\n3. **Cite Holloway et al. (NeurIPS 2024 Workshop)** which explicitly motivated this direction.\n\n4. **Fix the arithmetic.** 9 × 300 × 3 × $0.30 = $2,430, not $810. If Qwen3-Coder-Next actually costs ~$0.05/instance, state that directly.\n\n5. **Estimate the improvement headroom** by first running the 3 granularity configs on a pilot (50 instances) to see how much variance there is in which config wins. If one config dominates (>80% of instances), adaptive selection has limited value and the paper's premise weakens.\n\n6. **For EMNLP venue fit,** the method version (point 1) is much stronger than an empirical study. Frame around how LLMs comprehend code at different abstraction levels and how NL signals can steer this comprehension — this is genuinely an NLP question.\n\n7. **Consider combining NL and code features** to differentiate from both SIADAFIX (NL, LLM classifier) and Triage (code, ML classifier). A lightweight model that uses both feature families, available at different stages of the pipeline, could be a stronger contribution.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"IMPORTANT: Missing justification for DPO over classification — the proposal frames this as 'configuration preference learning' using DPO-style loss, but the task is essentially 9-class configuration prediction from features. The evaluation plan lacks an ablation comparing DPO preference learning against simpler multi-class classification (e.g., random forest, logistic regression, or even a simple MLP classifier trained on oracle labels). Without this comparison, the DPO framing appears to be methodological window-dressing rather than a substantive contribution. RouteLLM (arXiv 2406.18665) showed that preference data can train effective routers, but it also demonstrated that simpler classifiers can perform comparably in certain regimes.\", \"Missing methodological competitors — RouteLLM (arXiv 2406.18665, ICML 2025) trains LLM routers from preference data, which is the identical training paradigm applied to a different routing target (model selection vs. config selection). RADAR (arXiv 2509.25426) is a difficulty-aware routing framework for reasoning LLMs using learned item-response models. Both should be cited and differentiated to strengthen the methodological positioning.\", \"Three contributions may be too many for a 4-page short paper — 'the method,' 'the design,' and 'the insight' are partially overlapping (the design IS the method). Consider consolidating to: (1) the DPO-trained configuration router as the method contribution, (2) the empirical analysis connecting NL features to optimal granularity as supporting evidence. The two-stage NL→NL+Code architecture is a design choice within the method, not a standalone contribution.\", \"Headroom quantification is deferred — the proposal correctly includes a go/no-go gate, but the paper's entire premise rests on the oracle advantage being ≥5pp over best fixed config. The arXiv 2604.00167 study (50 instances, 2 repos) found function-level at 45.6% vs. file-level at 42.6% — only a 3pp gap between best and worst fixed configs, with per-instance variance not quantified as an oracle bound. The headroom may be too small for meaningful routing improvement.\", \"SWE-bench-Live evaluation details are underspecified — the proposal says 'held-out SWE-bench-Live instances' but doesn't specify: how many instances will be used, which subset/time period, whether Docker environments are available for all instances, or how to handle the ~10-15% setup failure rate. SWE-bench-Live's automated curation pipeline may produce instances of varying difficulty distribution from the training set (SWE-bench Verified).\", \"UniXcoder (2022) encoder choice — while adequate, UniXcoder is 4 years old. More recent code encoders (CodeSage 2024, StarEncoder, or even a frozen Qwen2.5-Coder-1.5B as encoder) may provide better issue text representations. The choice should be justified or an encoder ablation included.\"]\nFeedback: The proposal has improved substantially from Round 2 — it's now a proper method contribution with realistic costs and a genuine gap. To push this to pass quality:\n\n1. **Add a DPO-vs-classification ablation.** This is the single most important missing piece. If a simple random forest on the same features performs comparably to the DPO-trained UniXcoder router, the 'preference learning' framing collapses into standard classification. Include at minimum: (a) random forest on NL+code features, (b) MLP classifier on UniXcoder embeddings, (c) your DPO preference router. If DPO wins, explain why (handles noisy/partial orderings better? learns from relative rather than absolute signals?). If it doesn't, the paper's main selling point is undermined.\n\n2. **Cite RouteLLM and RADAR.** RouteLLM (Ong et al., ICML 2025) is the closest methodological parallel — it trains routers from preference data, just for model selection instead of config selection. RADAR (arXiv 2509.25426) uses item-response theory for difficulty-aware routing. Both strengthen your related work section and help position your contribution.\n\n3. **Consolidate to 2 contributions** for the short paper: (1) the configuration preference learning method (encompassing the two-stage design), (2) the empirical analysis of which NL/code features predict optimal granularity. Three separate contributions in 4 pages will feel thin on each.\n\n4. **Run the headroom pilot FIRST**, then write the paper around the actual numbers. If headroom is 5-8pp, discuss the cost-efficiency angle (routing saves API cost by avoiding expensive configs). If headroom is >10pp, lead with accuracy improvement. The framing should adapt to the data.\n\n5. **Specify SWE-bench-Live evaluation**: target ~100-200 instances from the most recent monthly batch (to ensure decontamination), confirm Docker environment availability, and plan for the ~10-15% setup failure rate.\n\n6. **Discuss the minimal-headroom scenario** in the paper: if the oracle advantage is small, argue that the routing still provides value through cost efficiency (cheaper configs for easy instances) even if accuracy gains are modest. This makes the contribution robust to disappointing headroom numbers.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"CRITICAL: Missing Mix-of-Granularity (MoG, COLING 2025, arXiv 2406.00456) — trains a router to dynamically select optimal retrieval granularity for RAG using soft labels, which is the same core mechanism as GranRoute. The only difference is domain (general QA vs. code repair). This must be cited and explicitly differentiated; without it, the novelty claim ('no routing method targets retrieval configuration') is factually incorrect — MoG targets retrieval granularity, which is a subset of GranRoute's configuration space.\", \"CRITICAL: Missing RAGRouter (NeurIPS 2025, arXiv 2505.23052) — the first routing method specifically designed for RAG settings, using document embeddings and RAG capability embeddings. As a NeurIPS 2025 paper on routing in RAG, it is highly relevant and would be noticed by any reviewer familiar with the routing literature.\", \"IMPORTANT: Missing 'Rethinking Predictive LLM Routing' (arXiv 2505.12601, May 2025) — demonstrates that a simple kNN baseline matches or outperforms complex learned routers across diverse tasks. This directly challenges GranRoute's elaborate 5-method comparison: if kNN dominates, the entire multi-method contribution collapses. This paper must be cited, and kNN must be included as a 6th baseline method.\", \"IMPORTANT: Missing ProCC (arXiv 2405.07530, TOSEM 2025) — uses multi-retrieval augmented generation with adaptive retrieval selection for code completion. While it targets code completion rather than repair, it is in the same domain (adaptive retrieval for code tasks) and must be cited.\", \"Headroom risk remains unresolved and foundational — the arXiv 2604.00167 study found only 3pp difference between best and worst fixed granularities (function 45.6% vs. file 42.6%) on 50 instances. The oracle bound (per-instance best) over the best fixed config could be only 2-5pp. The go/no-go gate is good, but if the headroom is <5pp, the paper's entire premise weakens to a cost-efficiency argument, which may not sustain a publication even as a short paper.\", \"The 5-method comparison contribution is vulnerable to the 'ablation-as-paper' criticism, especially given that existing routing benchmarks (LLMRouterBench, RouterEval) already provide more comprehensive method comparisons. The paper needs a clear narrative about what novel insight emerges from the comparison (e.g., 'code repair routing requires fundamentally different methods than model routing because...'), not just which method achieves the highest number.\"]\nFeedback: The proposal has matured substantially over 4 rounds — the feasibility is now realistic, the gap argument is well-supported, and the approach is sensible. The remaining issues are fixable but important:\n\n1. **Cite and differentiate from MoG (COLING 2025).** MoG is the single biggest threat to novelty. The differentiation should argue: (a) MoG routes over text chunking granularity for knowledge QA, while GranRoute routes over fault-localization granularity + context budget jointly for code repair — a 2D configuration space vs. 1D; (b) MoG uses soft labels from retrieval quality, while GranRoute uses downstream repair success as oracle signal — end-task alignment; (c) code repair has unique routing signals (stack traces, error types, code structure) unavailable in QA. This is a legitimate distinction but must be made explicit.\n\n2. **Cite RAGRouter (NeurIPS 2025)** and position GranRoute as targeting a different routing dimension (retrieval configuration vs. which RAG-LLM to use).\n\n3. **Add kNN as a baseline method.** Given the findings from 'Rethinking Predictive LLM Routing,' include a 6th method — kNN on the same feature space. If kNN dominates, the paper's insight becomes 'simple non-parametric methods suffice for code repair routing' — still publishable as a short paper. If learned methods beat kNN, you have stronger justification for the routing framework.\n\n4. **Cite ProCC** and distinguish by target task (completion vs. repair) and routing target (retrieval perspective vs. configuration).\n\n5. **Strengthen the multi-method comparison narrative.** The paper should not just report 'Method X wins.' It should extract a generalizable insight: Do preference-based methods (à la RouteLLM) work better for configuration routing than classification? Does the answer depend on data size? Does code-specific structure create different routing dynamics than NL routing? Frame the comparison as answering a specific research question about routing methodology, not as an ablation.\n\n6. **Address the small-headroom scenario more concretely.** If the pilot shows 3-5pp headroom, the paper could pivot to a diagnostic contribution: 'We find that retrieval configuration routing for code repair yields X% accuracy gain and Y% cost savings, and that the dominant routing signal is Z.' Even a modest-headroom finding is publishable if the analysis is insightful.\n\nWith these changes, the proposal is viable for EMNLP Findings as a short paper. EMNLP Main would require stronger novelty — consider whether the 2D routing space (granularity × budget) with dual-signal architecture (NL + code features at different pipeline stages) can be positioned as a methodological contribution rather than pure domain transfer.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"IMPORTANT: Missing AutoRAG-HP (EMNLP 2024 Findings, arXiv 2406.19251) — formulates RAG hyperparameter tuning (top-k, compression ratio, embedding methods) as online multi-armed bandit. This is a published EMNLP paper on adaptive retrieval configuration selection. It differs from GranRoute in domain (general QA vs. code repair) and paradigm (online bandit vs. offline routing), but must be cited as it directly addresses the same problem category — learning to adapt retrieval parameters per instance.\", \"IMPORTANT: Anti-evidence not addressed — SWEzze (arXiv 2603.28119) shows that *compressing* code context by 6x (removing 51-71% of tokens) improves issue resolution rates by 5-9.2%. This directly challenges the premise that selecting the right retrieval configuration matters — if aggressively removing context *helps*, the bottleneck is LLM context utilization, not retrieval strategy. Similarly, 'Context Length Alone Hurts LLM Performance Despite Perfect Retrieval' (arXiv 2510.05381) shows 13.9-85% performance degradation from input length growth even with perfect retrieval. The proposal must acknowledge and address this tension: if the LLM can't effectively use retrieved context, routing to the 'right' configuration may have a low ceiling.\", \"IMPORTANT: The NeurIPS 2024 exploration-exploitation paper (arXiv 2405.17503) frames code repair as a bandit problem and argues the dominant lever is sampling diversity (generating diverse patches via different prompts/LLMs), not retrieval configuration. Top SWE-bench systems (Devlo at 70.2%) achieve results through multi-LLM diverse sampling, not adaptive retrieval. The proposal should discuss whether compute budget is better spent on retrieval routing vs. diverse patch generation.\", \"Short paper scope overload — 6 routing methods × 2 feature families × CodeSage-base vs. UniXcoder encoder ablation × MoG-adapted baseline = at least 24 cells in the main comparison table, plus per-difficulty-tier analysis, SHAP analysis, and cost-efficiency analysis. This is too much for 4 pages. Consider reducing to 4 core methods (kNN, random forest, MLP, Bradley-Terry) with LambdaMART and IRT as supplementary, and dropping the encoder ablation from the main paper.\", \"The 3pp gap between best and worst fixed granularities in arXiv 2604.00167 (45.6% vs 42.6%) is concerning for headroom. While the oracle bound (per-instance best) should be higher, the 2D configuration space only helps if granularity and budget interact — i.e., the optimal budget differs by granularity. The proposal should explicitly hypothesize about interaction effects and include interaction analysis in the pilot.\", \"Minor: SWE-bench-Live's monthly batches are a 'stated plan' (arXiv 2505.23419), not confirmed operational practice. The proposal should verify that monthly batches are actually being released before depending on them for evaluation.\"]\nFeedback: The proposal has matured impressively over 5 rounds — feasibility is nailed, the gap is genuine, and the experimental design (especially the MoG-adapted baseline and kNN comparison) is thoughtful. The remaining barrier to passing is that the proposal doesn't engage with the strongest counterargument to its premise.\n\nSpecific changes needed:\n\n1. **Address the compression-beats-retrieval tension head-on.** The SWEzze finding (6x compression improves results) and the context-length-hurts evidence (arXiv 2510.05381) are the strongest objections any reviewer will raise. Argue explicitly: GranRoute's routing is *complementary* to context compression — it selects the right structural granularity (file vs. function vs. line) and budget *before* compression. The insight is that starting from the right abstraction level matters even after compression. You could even frame GranRoute as the upstream complement to SWEzze's downstream compression: GranRoute selects *what* to retrieve, SWEzze compresses *how much* to keep. If the pilot data shows that GranRoute + compression outperforms either alone, this becomes a strong narrative.\n\n2. **Cite AutoRAG-HP (EMNLP 2024 Findings)** and differentiate: AutoRAG-HP tunes continuous retrieval hyperparameters (top-k, compression ratio) online via bandit learning; GranRoute selects discrete structural abstractions (file/function/line) offline via end-task labels. The key distinction is that GranRoute's granularity choices are *structurally distinct program abstractions*, not just different numeric parameter values.\n\n3. **Discuss the exploration-exploitation tradeoff.** Acknowledge that diverse patch generation (multiple LLMs/prompts) is an alternative way to spend compute budget. Position GranRoute as orthogonal: routing selects the best *input* to the repair model, while diversity operates on the *output* side. They should compose.\n\n4. **Tighten scope for short paper.** Reduce to 4 core methods (kNN, random forest, MLP, Bradley-Terry) in the main paper. Move LambdaMART, IRT, and encoder ablation to supplementary. This focuses the narrative on the kNN vs. learned methods question (RQ1) and NL vs. NL+Code signals question (RQ2) without diluting across too many comparisons.\n\n5. **Add interaction analysis to the pilot.** In Phase 1, explicitly measure whether the optimal budget depends on granularity (and vice versa). If there are no interaction effects, the 2D routing problem decomposes into two independent 1D problems, which weakens the contribution relative to MoG. If interactions exist, highlight them as the key differentiator.\n\n6. **Reframe the contribution hierarchy.** Lead with the empirical question ('Does configuration routing help code repair, and does it behave differently from text QA routing?') rather than the framework ('GranRoute, the first...'). The most publishable version of this paper answers a question about code understanding at different abstraction levels — when does structural granularity matter, what bug features predict it, and can simple methods capture it? This is an NLP question, not just an SE pipeline question.\n\nWith these changes, the novelty framing becomes: 'We test whether granularity routing (MoG) and kNN routing sufficiency (arXiv 2505.12601) transfer from text QA and model routing to the structurally richer code repair setting, finding [specific insight about when they do/don't transfer].' This is a solid Findings contribution.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-12T00:19:06.845Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T00:19:06.845Z",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

## Round 1

67 recorded events

### User

_source line 3 · 2026-05-12T00:19:06.885Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-11 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.

Direction: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.

Contribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.
2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).
3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.

Look for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.

Tag: direction=code_models, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].**
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
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?
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

## Idea under review (round 6/10)
{
  "title": "GranRoute: When Does Structural Retrieval Granularity Matter for Repository-Level Code Repair?",
  "core_problem": "Repository-level LLM-based code repair systems use fixed fault-localization granularity (file/function/line) and fixed context budgets, despite growing evidence that the optimal retrieval configuration is instance-dependent. Two April 2026 empirical studies confirm this: arXiv 2604.00167 shows function-level FL beats file- and line-level on average but the ranking shifts across difficulty tiers, and arXiv 2604.05481 finds that file-level context yields 15–17× improvement while line-level expansion causes noise amplification — yet neither proposes an adaptive selection method. Holloway et al. (NeurIPS 2024 ML for Systems Workshop) explicitly call for 'context granularity strategies tailored to specific bug types' but provide no method.\n\nHowever, recent work raises a critical counter-question: does retrieval configuration even matter, or is the bottleneck downstream context utilization? SWEzze (arXiv 2603.28119) shows that compressing retrieved code by 6× (removing 51–71% of tokens) improves issue resolution by 5–9.2%, because retrieved contexts have only 8.4% relevance density. Du & Tian (arXiv 2510.05381) find 13.9–85% performance degradation from context length growth even with perfect retrieval, with at least 7.9% degradation persisting even when distractor tokens are replaced with whitespace. If removing context helps, does selecting the 'right' retrieval configuration matter?\n\nWe argue yes, because this framing conflates two orthogonal dimensions: **structural selection** (which program abstraction level — file, function, or line — defines the unit of retrieval) and **quantitative compression** (how many tokens to retain within a chosen structural level). The strongest evidence for this distinction is the arXiv 2604.05481 finding that line-level context *hurts* despite containing fewer tokens per element than file-level. If the bottleneck were purely quantitative, line-level should always win (less text = less noise). Instead, line-level fails because isolated lines lack the semantic coherence of functions or files — the structural boundaries themselves determine how effectively the LLM reasons about code. SWEzze operates at a fixed structural level (function-level) and compresses within it; it never asks *which* structural level to use. GranRoute addresses this complementary upstream question.\n\nA second counter-argument is that compute budget may be better spent on diverse patch generation rather than retrieval optimization. Top SWE-bench systems (Devlo at 70.2%) achieve results through multi-LLM diverse sampling, and arXiv 2405.17503 frames the dominant lever as sampling diversity. We acknowledge this but note that GranRoute operates on the *input* side (retrieval configuration) while diversity operates on the *output* side (patch generation). Critically, GranRoute's routing cost is near-zero — an embedding lookup plus a lightweight classifier, no LLM calls — so it does not compete for the compute budget allocated to diverse sampling. Input quality (retrieval configuration) determines the *ceiling* of what any single sample can achieve; output diversity determines how close the system gets to that ceiling. They should compose.\n\nThe gap that remains: the granularity routing literature (MoG, COLING 2025; LTRR, SIGIR 2025) and the adaptive retrieval HP literature (AutoRAG-HP, EMNLP 2024 Findings) have not been extended to code repair's structurally richer setting, where granularity choices represent distinct program abstractions, end-task repair success is the training signal, and code-specific routing signals (stack traces, error types, code structure) are available. No existing work learns to jointly select (fault-localization granularity, context budget) per issue for code repair.",
  "opportunity": "The core empirical question this paper answers is: **Does the structural abstraction level of retrieved context matter per-instance for LLM code repair, independently from context quantity — and if so, can simple methods predict the optimal level?**\n\nThis question is motivated by the convergence of three threads with an unresolved tension:\n\n(1) **Granularity matters per-instance in code repair** (arXiv 2604.00167, 2604.05481, Holloway et al. NeurIPS 2024), but no adaptive method exists.\n\n(2) **Context compression alone helps** (SWEzze, arXiv 2510.05381), raising the question of whether retrieval *configuration* is secondary to retrieval *compression*.\n\n(3) **Granularity routing works in text QA** (MoG, COLING 2025) and **simple methods suffice for model routing** (kNN matches learned routers, arXiv 2505.12601), but neither has been tested in the structurally richer code repair setting.\n\nThe tension between (1) and (2) is precisely what makes this paper interesting. If granularity selection and compression are redundant, GranRoute adds nothing — SWEzze already solves the problem. If they are complementary — as we hypothesize based on the structural vs. quantitative distinction — then GranRoute addresses a dimension that compression cannot: which program abstraction level defines the unit of reasoning. The pilot is designed to resolve this tension empirically.\n\nCode repair introduces three specific challenges that distinguish it from prior routing work: (a) the configuration space is 2D (granularity × budget) with hypothesized *interaction effects* — the optimal budget likely depends on the granularity level, because file-level elements are self-contained while line-level elements lack structural coherence; (b) the oracle signal must be end-task repair success, not retrieval similarity (MoG) or LLM-as-judge scores (AutoRAG-HP); (c) code-specific routing signals (stack trace structure, error type, cyclomatic complexity) may enable more effective routing than generic text embeddings.\n\nA critical empirical sub-question, raised by arXiv 2505.12601, is whether the kNN simplicity advantage demonstrated for model routing transfers to configuration routing. If kNN suffices, the structural complexity of the 2D configuration space is navigable without parametric learning. If not, the interaction effects between granularity and budget justify learned methods. GranRoute is designed to answer this through systematic comparison.\n\nSeleCom (arXiv 2602.15856) provides independent evidence for our complementarity argument: it shows that selection and compression compose because 'full-compression approaches dilute query-relevant signals by treating all content equally.' GranRoute is upstream selection (structural level); SWEzze/SeleCom is downstream compression (token reduction).",
  "landscape": "**Granularity-dependence evidence in code repair:** Holloway & Elenberg (NeurIPS 2024 ML for Systems Workshop) study 6 context granularities on 109 Defects4J bugs, finding sliced context achieves 79% Correct/Plausible ratio, and explicitly motivate tailored strategies as future work. arXiv 2604.00167 (50 instances, 2 repos) finds function-level at 45.6% vs. file-level at 42.6% with rankings shifting across difficulty tiers. arXiv 2604.05481 (500 instances, 61 configurations) finds file-level context yields 15–17× improvement while line-level expansion amplifies noise — crucially, this shows structural level matters independently from context quantity.\n\n**Context compression and the quantitative bottleneck:** SWEzze (arXiv 2603.28119) compresses code context by 6× (51–71% token reduction) at fixed function-level granularity, improving resolution by 5–9.2% on SWE-bench Verified with Agentless, SWE-agent, and Moatless — because retrieved contexts have only 8.4% relevance density. Du & Tian (arXiv 2510.05381) show 13.9–85% performance degradation from context length even with perfect retrieval, with at least 7.9% residual degradation from length alone (whitespace-replaced distractors). SWE-Pruner (arXiv 2601.16746) performs adaptive neural skimming at fixed granularity. SeleCom (arXiv 2602.15856) demonstrates that selection and compression are complementary: query-conditioned selection first, then compression of selected spans, reducing computation by 33.8–84.6% while maintaining quality. These papers establish that context quantity is a bottleneck but operate within a fixed structural level — none addresses which structural level to use.\n\n**Sampling diversity vs. input optimization:** arXiv 2405.17503 frames code repair as a bandit problem and argues the dominant lever is sampling diversity. arXiv 2502.11027 finds prompt perturbations that increase diversity improve Best-of-N by ~10% but harm majority voting, revealing the mechanism as exploration breadth. Top SWE-bench systems (Devlo at 70.2%) use multi-LLM diverse sampling. However, BEST-Route (ICML 2025) jointly optimizes model selection AND sampling count, suggesting input and output optimization compose. Input quality determines the ceiling; output diversity determines proximity to the ceiling.\n\n**Granularity routing in text QA:** Mix-of-Granularity (MoG, COLING 2025, arXiv 2406.00456) trains a MLP router to select optimal text chunking granularity (5 levels: {1/2, 1, 2, 4, 8}× base chunk size) for RAG. The router takes RoBERTa query embeddings and is trained with BCE loss using soft labels derived from BM25 retrieval similarity. MoG is the closest prior work on granularity routing; key differences: (1) 1D chunk-size routing vs. our 2D (granularity × budget) space with interaction effects, (2) retrieval-similarity soft labels vs. end-task repair labels, (3) text QA vs. code repair with code-specific signals. FreeChunker (arXiv 2510.20356) critiques MoE-based chunking methods as 'fundamentally bounded by the capabilities of the underlying chunker experts.'\n\n**Adaptive retrieval HP tuning:** AutoRAG-HP (EMNLP 2024 Findings, arXiv 2406.19251) formulates RAG hyperparameter tuning as online multi-armed bandit, tuning top-k, compression ratio, and embedding model via Hierarchical UCB. Key differences from GranRoute: AutoRAG-HP optimizes *globally* (one best config for the entire dataset, not per-instance), operates *online* (sequential exploration), and tunes *numeric/categorical* parameters (top-k values, compression ratios), while GranRoute routes per-instance over *structurally distinct program abstractions* (file/function/line) using *offline* trained routers with *end-task* repair success labels.\n\n**LLM routing methods:** RouteLLM (ICLR 2025, arXiv 2406.18665) trains 4 router architectures from preference data. RADAR (arXiv 2509.25426) uses IRT for difficulty-aware routing. BEST-Route (ICML 2025, arXiv 2506.22716) routes model + sampling count. LTRR (SIGIR 2025, arXiv 2506.13743) frames retriever selection as learning-to-rank, finding pairwise XGBoost outperforms neural rankers. arXiv 2505.12601 demonstrates kNN matches or outperforms learned routers for model selection — directly motivating our central methodological question.\n\n**RAG-aware routing and configuration adaptation:** RAGRouter (NeurIPS 2025, arXiv 2505.23052) routes queries to the best RAG-LLM — model selection, not retrieval configuration. METIS (SOSP 2025, arXiv 2412.10543) jointly adapts RAG configuration (chunk count + synthesis method) per query, achieving 1.6–2.5× latency reduction — the closest configuration-level adaptation, but in general QA with latency focus. GraphRAG-Router (arXiv 2604.16401) uses RL to route over GraphRAG infrastructure.\n\n**Code repair with adaptive components:** Triage (arXiv 2604.07494) routes SWE-bench tasks to cost-effective LLM tiers — model routing, not retrieval config. ProCC (TOSEM 2025, arXiv 2405.07530) uses contextual bandits to select retrieval perspectives for code completion — adaptive retrieval in the code domain but for completion with online bandits, not repair with offline routing. AdaPatcher (AAAI 2025, arXiv 2503.06510) adapts repair via DPO at fixed localization. SIADAFIX (arXiv 2510.16059) classifies issues into difficulty modes via NL features but does not adapt FL granularity. ARISE (arXiv 2605.03117) builds multi-granularity program graphs with fixed representations.\n\n**The gap:** Structural granularity selection and context compression are complementary dimensions (established by SeleCom, arXiv 2602.15856). Compression (SWEzze, SWE-Pruner) addresses how many tokens to retain within a structural level. Granularity routing (MoG) addresses which text chunking size to use for QA. AutoRAG-HP tunes retrieval hyperparameters globally online. But no work targets per-instance selection of which program abstraction level (file/function/line) and what context budget to use for code repair, where structural boundaries determine reasoning effectiveness independently from context quantity.",
  "approach": "We propose GranRoute, a retrieval configuration routing framework for code repair that learns to select the optimal (granularity, context budget) pair per issue. GranRoute integrates upstream of any retrieval-based repair pipeline as a plug-in module, complementing downstream context compression.\n\nThe paper is organized around two research questions that distinguish it from prior routing work:\n- **RQ1 (Structural abstraction):** Does per-instance structural granularity routing improve code repair independently from context compression? Specifically: does GranRoute compose with downstream compression, or are they redundant?\n- **RQ2 (Routing methods):** Does the kNN simplicity advantage observed in model routing (arXiv 2505.12601) transfer to code repair configuration routing, or does the 2D configuration space with interaction effects favor parametric methods?\n\n**Phase 1 — Headroom & Interaction Pilot (2 days):** Run the Agentless pipeline via API (Qwen3-Coder-Next, ~$0.08/instance) across 12 configurations (3 granularities: file/function/line × 4 context budgets: 3, 5, 8, 12 retrieved elements) on 50 SWE-bench Verified instances, 3 runs each (majority-vote labels). Compute:\n(a) **Accuracy headroom:** Oracle accuracy (per-instance best config) minus best fixed-config accuracy.\n(b) **Cost-efficiency headroom:** Average tokens consumed by oracle-selected configs vs. best fixed config.\n(c) **Configuration diversity:** How many distinct configurations appear in the oracle set.\n(d) **Interaction analysis:** For each granularity level, compute the optimal budget distribution. Test whether the optimal budget depends on granularity using a two-way contingency analysis (chi-squared or Fisher's exact test). **Interaction hypothesis:** File-level elements are self-contained, so larger budgets (8–12) help by providing broader context; line-level elements lack structural coherence, so larger budgets amplify noise (consistent with arXiv 2604.05481) and smaller budgets (3–5) are optimal; function-level has an intermediate optimum. If interaction effects exist, the 2D configuration space does not decompose into two independent 1D problems, justifying joint routing over MoG's 1D approach.\n(e) **Compression composition test:** For the 50 pilot instances, additionally run the best-fixed config and oracle-selected config with a simple post-retrieval compression (retain top 50% of retrieved elements by BM25 relevance, approximating SWEzze-style filtering). Compare: best-fixed, best-fixed+compression, oracle-selected, oracle-selected+compression. If oracle+compression > compression-only, structural selection adds value beyond compression.\n\n**Go/no-go gate:** If accuracy headroom < 3pp AND cost savings < 15% AND no significant interaction effects AND compression-only matches oracle-selected: the structural selection dimension adds negligible value, and we pivot to a diagnostic study analyzing why code repair is configuration-invariant despite text QA being configuration-sensitive. If accuracy headroom is modest (3–5pp) but interactions exist or compression composition shows gains: proceed with focused framing on when and why structural granularity matters.\n\n**Phase 2 — Oracle Collection (3 days):** Extend to 300 SWE-bench Verified instances across the same 12 configurations, 3 runs each (total: 10,800 API calls, ~$864). Each instance receives per-configuration success rates via majority vote. Cost: ~$864.\n\n**Phase 3 — Training Data Construction (1 day):** Construct training data: (a) Classification labels: best-performing config per instance (ties broken by cost). (b) Preference pairs: (issue_text, winning_config, losing_config) from success/failure outcomes. (c) kNN support set: (issue_embedding, config_performance_vector) pairs. Extract features: NL features from issue text (via CodeSage-base encoder, 356M), hand-crafted NL features (error-type keywords, stack trace depth, code entity count, description length, location specificity score), and lightweight code-structural features from localized files (cyclomatic complexity, file size, import count, class/function ratio).\n\n**Phase 4 — Router Training with Multi-Method Comparison (2 days):** Train and compare 4 core routing methods, organized to answer RQ2:\n(a) **kNN router** on CodeSage-base embeddings — the critical simplicity baseline motivated by arXiv 2505.12601. Uses k-nearest neighbor retrieval in embedding space with majority voting over oracle-optimal configurations.\n(b) **Random forest** on hand-crafted NL+code features — a standard ML baseline, motivated by LTRR's finding that tree-based methods outperform neural rankers.\n(c) **MLP classifier** on CodeSage-base embeddings — standard neural classification baseline, comparable to MoG's MLP router but with end-task labels.\n(d) **Bradley-Terry preference router** on CodeSage-base embeddings with a scoring head trained via preference loss — motivated by RouteLLM's paradigm.\nSupplementary methods (reported in appendix): LambdaMART learning-to-rank on combined features, IRT-based difficulty router.\nAll methods operate in two variants: NL-only (zero pre-routing cost) and NL+Code (minimal cost after initial file localization), addressing the signal question within RQ2. Training is lightweight: ~7 H100-hours total.\n\n**Phase 5 — Evaluation (3 days):** Evaluate on ~100 SWE-bench-Live instances from recent monthly batches (confirmed operational: 50 new issues/month since mid-2025). Plan for ~10–15% Docker failures, targeting 85–90 evaluated instances. Fallback: if fewer than 80 SWE-bench-Live instances are available, supplement with a stratified held-out split from SWE-bench Verified, noting the weaker decontamination guarantee. Use the full Agentless pipeline.\n\nBaselines and conditions: (a) best fixed-granularity configuration, (b) random configuration, (c) MoG-adapted baseline (MLP + soft labels retrained on our code repair data), (d) best-fixed + post-retrieval compression (addresses whether compression alone suffices), (e) GranRoute (best method from RQ2), (f) GranRoute + compression (tests composition), (g) oracle upper bound.\nReport: end-to-end repair rate, routing accuracy, cost efficiency, calibration. Key analyses: (1) GranRoute vs. compression-only: does structural selection add value? (2) GranRoute + compression vs. each alone: do they compose? (3) kNN vs. learned methods (RQ2), (4) NL-only vs. NL+Code feature ablation, (5) MoG-adapted vs. end-task-trained methods.\n\n**Phase 6 — Analysis (concurrent, 2 days):** SHAP-based feature importance on the best-performing router. Target question: which NL features predict optimal structural granularity? If stack trace depth or error type dominate, this explains why code repair routing requires different signals from text QA routing (where MoG uses generic query embeddings). Interaction analysis: visualize the granularity × budget performance surface to characterize when structural level matters most.\n\n**Narrative framing by outcome:**\n- If GranRoute + compression > compression alone: 'Structural selection and context compression are complementary dimensions — GranRoute selects *what program abstraction* to retrieve; compression reduces *how much* to retain. Together they outperform either alone.' Strong contribution.\n- If compression alone matches GranRoute: 'Structural granularity matters less than context quantity for code repair — a surprising finding that contrasts with text QA (MoG) and suggests LLMs are robust to structural boundaries when context is sufficiently compressed.' Diagnostic contribution.\n- If kNN dominates: 'Configuration routing in code repair, like model routing, is solved by simple non-parametric methods.' If learned methods dominate: 'The 2D configuration space with interaction effects requires parametric learning, unlike model routing.'\n- If headroom < 3pp: pivot to diagnostic study.\n\nThe contribution hierarchy leads with the empirical question, not the framework: (1) **Empirical finding** answering whether per-instance structural granularity selection matters for code repair independently from context compression — testing whether the structural vs. quantitative distinction holds in practice; (2) **Methodological comparison** of 4 routing methods testing whether kNN sufficiency transfers from model routing to configuration routing; (3) **Interpretable analysis** connecting code-specific NL bug features to optimal structural granularity, explaining when and why code repair routing differs from text QA routing; (4) **GranRoute framework** as the practical vehicle for these findings — a plug-in module that complements downstream compression.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~25–40h H100 (7h for 4-method router training, 8–15h for feature extraction/analysis, 5–10h for ablation experiments including MoG-adapted baseline and supplementary methods; all Agentless runs are API-based)",
      "gpu_utilization": "Low (~15–25%). Most compute is API-based. Local GPU used for encoder inference and router training.",
      "timeline": "14 days (tight for EMNLP ARR May 25 deadline)",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "$75–120",
      "api_cost": "$1,150–1,550 (pilot with interaction+composition: 1,800 runs × $0.08 + ~200 compression runs × $0.08 ≈ $160; oracle: 10,800 runs × $0.08 ≈ $864; evaluation: ~100 instances × (7 conditions) × 3 runs × $0.08 ≈ $168; iteration/debugging: ~$100)"
    },
    "human_in_loop": {
      "gpu_hours": "~35–50h H100 (agent explores router architectures including kNN variants, feature combinations, and supplementary methods)",
      "gpu_utilization": "Low-moderate (~25–35%). Agent queues API runs between check-ins.",
      "timeline": "10–12 days",
      "team": "1 researcher, ~30min/day for reviewing interaction analysis, validating composition results, approving evaluation plan",
      "claude_api_cost": "$100–200",
      "estimated_gpu_cost": "$105–150",
      "api_cost": "$1,300–1,800 (more configs explored for interaction analysis, robustness checks)",
      "risk_note": "SWE-bench Docker setup failures on ~10–15% of instances may require human triage."
    },
    "auto_research": {
      "gpu_hours": "~60–110h H100 (agent explores neural router variants, kNN hyperparameter sweeps, extensive interaction and composition analysis)",
      "gpu_utilization": "Moderate (~35–50%).",
      "timeline": "8–10 days",
      "team": "0 (only initial setup)",
      "claude_api_cost": "$250–500",
      "estimated_gpu_cost": "$180–330",
      "api_cost": "$1,700–2,600 (agent explores 15+ configs, composition experiments with multiple compression ratios)",
      "speed_bottleneck": "API rate limits and SWE-bench Docker setup (~2min/container).",
      "risk_note": "Agent may over-engineer router architecture — explicitly instruct to prioritize interaction analysis and composition experiment as the paper's central empirical questions."
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings short paper via ARR May cycle (submission: May 25, 2026) — tight 14-day window, feasible for focused 4-page empirical paper; Findings suits the domain-transfer and empirical question framing",
    "ICSE 2027 Research Track (abstract: June 23, 2026; paper: June 30, 2026) — comfortable timeline for full-length version with 6 methods, encoder ablation, and expanded composition analysis",
    "AAAI 2027 (abstract: July 25, 2026; paper: August 1, 2026) — suits the routing/configuration learning angle"
  ],
  "level": "solid",
  "key_references": [
    "Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation (COLING 2025, arXiv 2406.00456) — trains MLP router to select text chunking granularity via soft labels; closest prior work on granularity routing, but 1D chunk-size space with retrieval-similarity labels in text QA vs. our 2D (granularity × budget) space with end-task repair labels in code repair",
    "AutoRAG-HP: Automatic Online Hyper-Parameter Tuning for Retrieval-Augmented Generation (EMNLP 2024 Findings, arXiv 2406.19251) — formulates RAG HP tuning as online multi-armed bandit with Hierarchical UCB; tunes top-k, compression ratio, embedding model globally (one best config per dataset), while GranRoute routes per-instance over structurally distinct program abstractions offline",
    "SWEzze: Compressing Code Context for LLM-based Issue Resolution (arXiv 2603.28119) — 6× compression (51–71% token reduction) improves resolution by 5–9.2%; establishes that context quantity is a bottleneck but operates at fixed structural granularity; GranRoute addresses the complementary upstream question of which structural level to use",
    "Context Length Alone Hurts LLM Performance Despite Perfect Retrieval (arXiv 2510.05381) — 13.9–85% degradation from length even with perfect retrieval; motivates the structural vs. quantitative distinction: if length hurts regardless, the structural boundaries that define reasoning units matter even more",
    "Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers (arXiv 2505.12601) — kNN matches/outperforms learned routers for model selection; directly motivates RQ2 on whether this simplicity advantage transfers to configuration routing",
    "SeleCom: Query-Conditioned Selection and Compression for RAG (arXiv 2602.15856) — demonstrates selection and compression are complementary ('full-compression dilutes query-relevant signals'); supports our argument that structural selection (GranRoute) and token compression (SWEzze) address different dimensions",
    "On the Effect of Sampling Diversity in LLM Inference (arXiv 2502.11027) — prompt perturbations that increase diversity improve Best-of-N by ~10%; positions output diversity and input quality as complementary, not competing, optimization axes",
    "Exploration-Exploitation in Code Repair (arXiv 2405.17503) — frames code repair as bandit problem, argues sampling diversity is dominant lever; GranRoute is orthogonal (input-side routing vs. output-side diversity) with near-zero routing cost",
    "RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models (NeurIPS 2025, arXiv 2505.23052) — first RAG-aware router using document and RAG capability embeddings; model selection (which RAG-LLM), not retrieval configuration",
    "ProCC: Prompt-based Code Completion via Multi-Retrieval Augmented Generation (TOSEM 2025, arXiv 2405.07530) — adaptive retrieval perspective selection via contextual bandits for code completion; validates adaptive retrieval in code domain but targets completion with online bandits, not repair with offline routing",
    "METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation (SOSP 2025, arXiv 2412.10543) — jointly adapts RAG configuration per query; closest configuration-level adaptation but in general QA with latency focus",
    "Holloway & Elenberg, 'On the Role of Context Granularity in LLM-Driven Program Repair' (NeurIPS 2024 ML for Systems Workshop) — studies 6 granularities, explicitly motivates tailored strategies",
    "RouteLLM: Learning to Route LLMs with Preference Data (ICLR 2025, arXiv 2406.18665) — 4 router architectures from preference data; methodological parallel for preference-based routing",
    "RADAR: Reasoning-Ability and Difficulty-Aware Routing for Reasoning LLMs (arXiv 2509.25426) — IRT-based difficulty-aware routing; inspires supplementary IRT variant",
    "BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute (ICML 2025, arXiv 2506.22716) — jointly routes model + sampling count; supports composability of input and output optimization",
    "LTRR: Learning To Rank Retrievers for LLMs (SIGIR 2025, arXiv 2506.13743) — pairwise XGBoost outperforms neural rankers for retriever selection; motivates random forest baseline",
    "Triage: Routing Software Engineering Tasks to Cost-Effective LLM Tiers (arXiv 2604.07494) — model-tier routing via code health metrics",
    "A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks (arXiv 2604.00167) — function-level at 45.6% vs file-level at 42.6%, rankings shift across difficulty tiers",
    "On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481) — 61 configurations on 500 instances, line-level noise amplification despite being more targeted; key evidence that structural boundaries matter independently from context quantity",
    "RPO: Retrieval Preference Optimization for Robust RAG (ACL 2025, arXiv 2501.13726) — DPO-style preference learning for adaptive retrieval",
    "AdaPatcher: Less is More — Adaptive Program Repair with Bug Localization and Preference Learning (AAAI 2025 oral, arXiv 2503.06510)",
    "CodeSage: Code Representation Learning At Scale (ICLR 2024) — primary code encoder (356M params)",
    "SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents (arXiv 2601.16746) — adaptive neural skimming at fixed granularity",
    "SIADAFIX: Issue Description Response for Adaptive Program Repair (arXiv 2510.16059) — NL difficulty classification, does not adapt FL granularity",
    "ARISE: A Repository-level Graph Representation for Agentic FL and Repair (arXiv 2605.03117) — multi-granularity program graphs with fixed representations",
    "FreeChunker: A Cross-Granularity Chunking Framework (arXiv 2510.20356) — critiques MoE-based granularity methods",
    "SWE-bench Goes Live! (NeurIPS 2025 D&B, arXiv 2505.23419)",
    "Agentless: Demystifying LLM-based Software Engineering Agents (FSE 2025)",
    "GraphRAG-Router: Cost-Efficient Routing over GraphRAGs and LLMs (arXiv 2604.16401)"
  ],
  "description": "Recent evidence shows that optimal fault-localization granularity is instance-dependent in LLM code repair (arXiv 2604.00167, 2604.05481), but a strong counter-argument holds that context compression alone suffices — SWEzze improves resolution by 5–9.2% through 6× token reduction, and context length degrades performance even with perfect retrieval (arXiv 2510.05381). We argue these findings are complementary, not competing: compression addresses context *quantity* (how many tokens to retain), while granularity selection addresses *structural abstraction* (which program unit — file, function, or line — defines the reasoning boundary). The evidence that line-level context *hurts* despite containing fewer tokens (arXiv 2604.05481) directly supports this distinction.\n\nWe propose GranRoute, a near-zero-cost routing module that selects (fault-localization granularity, context budget) per issue — a 2D configuration space with hypothesized interaction effects (optimal budget depends on structural level). Our pilot (50 SWE-bench Verified instances, 12 configs, ~$160) tests three premises: (1) accuracy headroom exists, (2) granularity and budget interact, (3) routing composes with compression. We then systematically compare 4 routing methods — kNN, random forest, MLP, and Bradley-Terry preference router — testing whether kNN sufficiency (arXiv 2505.12601) transfers from model routing to configuration routing. All methods operate in NL-only and NL+Code variants. Evaluation on ~100 SWE-bench-Live instances includes a MoG-adapted baseline and composition conditions (GranRoute + compression vs. compression alone). SHAP analysis identifies which bug features predict optimal structural granularity.\n\nThe contribution is framed as an empirical investigation: (1) does structural granularity matter per-instance independently from compression? (2) can simple methods predict the optimal level? (3) what bug features drive the structural abstraction choice? GranRoute is the vehicle for these findings. API-based oracle collection (~$864), <40 H100-hours GPU. Primary target: EMNLP 2026 Findings (ARR May 25).",
  "project_name": "adaptive_context_orchestration",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["FATAL: Compute budget violation — proposal minimum (600-800 A100-hours ≈ 300-400 H100-equiv) is 2-4x the user's hard constraint of ≤200 H100-hours. Oracle profiling of 18 configs × 200+ instances with a self-hosted 80B model is the dominant cost and cannot be reduced without fundamentally changing the approach.", "FATAL: Timeline violation — manual estimate is 4-6 months, human-in-loop is 6-10 weeks, even auto mode is 10-18 days with 4× A100s. The 16-day constraint is incompatible with exhaustive oracle profiling.", "Poor EMNLP venue fit — the contribution is repair pipeline orchestration (an SE topic), not NLP/code understanding. The ML component (fine-tuning a 0.6B cross-encoder for 18-way classification) is too thin for an NLP venue. This work fits ICSE/ASE/FSE far better.", "Missing key competitor: AdaPatcher (AAAI 2025 oral, arXiv 2503.06510) — an adaptive program repair method with learned bug localization and preference learning — was not cited or discussed in the landscape.", "Oracle label noise: the Agentless pipeline has inherent randomness (temperature, sampling). Single runs per (config, instance) pair yield noisy training labels. Multiple runs per config would further inflate compute costs.", "Weak empirical foundation: the function-level FL granularity study (arXiv 2604.00167) was conducted on SWE-bench Mini (only 50 instances). Extrapolating that adaptive granularity selection will yield significant gains on the full 500-instance Verified set is speculative.", "SWE-bench Verified contamination: OpenAI's audit confirmed frontier models are contaminated on this benchmark, and 59.4% of hard tasks have flawed tests. Using it for both oracle label collection AND evaluation creates validity concerns.", "Overlap with SWEzze: the proposal uses the same base model (Qwen3-Reranker-0.6B) and same general approach (train a cross-encoder to select context) as SWEzze. The delta is adding granularity selection, which may not justify a separate paper at a top venue."]
Feedback: The core insight (adaptive granularity + context budget selection) is sound but the execution plan fundamentally violates the user's constraints. To make this viable for EMNLP 2026 within ≤200 H100-hours and ≤16 days, the generator must: (1) **Eliminate exhaustive oracle profiling** — instead of running 18 configs × N instances, use a much cheaper proxy: analyze the already-published results from arXiv 2604.00167 and 2604.05481 to derive heuristic-based labels, or use a small pilot (3-5 configs × 50 instances) with API-based models (not self-hosted 80B) to collect training signal. (2) **Reframe for EMNLP** — the current framing is SE-centric (fault localization, repair pipelines). To fit EMNLP's 'NLP and Code Models' track, reframe around code understanding: how do LLMs process code at different granularities? What structural features of code predict optimal context? This shifts from pipeline engineering to understanding LLM code comprehension. (3) **Cite AdaPatcher (AAAI 2025)** and SWE-ContextBench (arXiv 2602.08316) in the landscape. (4) **Use API-based models for oracle collection** (e.g., Qwen3-Coder-Next via API at ~$0.30/instance) instead of self-hosting, converting GPU cost to manageable API cost. (5) **Address SWE-bench contamination** — consider using SWE-bench-Live or SWE-rebench for evaluation instead of Verified. (6) **Reduce scope** — rather than a full learned policy with RL fine-tuning, consider a simpler but more insightful contribution: a systematic empirical study of what bug features predict optimal granularity, with a lightweight rule-based or logistic-regression selector. This is more achievable in 16 days and more publishable at EMNLP if paired with analysis of LLM code understanding at different granularities.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL: Contribution type mismatch — the user explicitly required 'METHOD ONLY: new training methods, retrieval-augmented code repair, or inference algorithms for code tasks.' This proposal self-describes as a 'large-scale empirical study' with a 'lightweight interpretable predictor' (logistic regression/GBDT). A logistic regression on hand-crafted features is not a new training method, retrieval-augmented repair, or inference algorithm. This fundamentally violates the user's requirements.", "CRITICAL: Missing competitor — Triage (arXiv 2604.07494, April 2026) trains an ML classifier to route SWE-bench tasks to cost-effective LLM tiers based on code quality signals. The methodology is nearly identical: lightweight classifier + pre-computed features → select optimal configuration. The only differences are feature source (code health metrics vs. NL features) and target variable (model tier vs. granularity/budget). This paper was not cited or discussed.", "Missing competitor — Holloway et al., 'On the Role of Context Granularity in LLM-Driven Program Repair' (NeurIPS 2024 ML for Systems Workshop), which studies 6 context granularities including backward static slicing on Defects4J and explicitly calls for 'future work should explore context granularity strategies tailored to specific bug types.' This is exactly the proposed work's research question, already articulated as a future direction.", "Missing competitor — AdaEdit/To Diff or Not to Diff (arXiv 2604.27296, April 2026) trains LLMs to dynamically choose the most token-efficient output format based on task features. Parallel concept: using task features to adaptively select configuration for downstream code operations.", "Arithmetic error in API cost: 9 configs × 300 instances × 3 runs × $0.30 = $2,430, not the claimed $810. The factor-of-3 error (seemingly forgetting the '× 3 runs') propagates into the total budget estimates. While per-instance costs with Qwen3-Coder-Next may be lower than $0.30, the stated math is wrong and undermines cost credibility.", "Terminology misattribution: The proposal attributes 'context rot' to arXiv 2604.05481, but that paper actually describes 'noise amplification' from line-level expansion. 'Context rot' is attributed to Chroma Research 2025, a separate source. The conflation weakens the theoretical framing.", "Small training set concern: 300 instances split into train/test (say 200/100) with 9 configuration labels, where many features are sparse (e.g., stack trace presence may be binary), may yield an underpowered feature analysis. SHAP values and mutual information on ~200 training instances with ~7 features and 9 target classes may not produce statistically robust insights.", "Uncertain headroom: If the best fixed configuration (e.g., function-level + 6 elements) already resolves 70-80% of what the oracle resolves, the predictor's improvement ceiling is narrow. The proposal does not estimate this headroom or discuss what happens if it is small."]
Feedback: The core research question (what NL features predict optimal code context?) has merit, but the execution plan mismatches the user's requirements in a fundamental way. To make this viable:

1. **Transform from empirical study to METHOD.** The user asked for 'new training methods, retrieval-augmented code repair, or inference algorithms.' Instead of a post-hoc empirical study + logistic regression, design a retrieval-augmented repair method that dynamically adapts its retrieval granularity and context budget during inference. For example: a meta-controller that encodes the NL issue description, predicts a retrieval configuration, executes retrieval at the predicted granularity, and feeds the result to the repair model — trained end-to-end (or via RL/DPO) to maximize repair success. This would be a genuine method contribution. The empirical analysis of NL features becomes a supporting analysis section, not the main contribution.

2. **Cite and differentiate from Triage (arXiv 2604.07494).** This April 2026 paper does the same thing with code features → model tier. You must show why NL features for granularity/budget selection is a distinct and valuable contribution. The strongest argument: NL features are available before any code retrieval, enabling zero-cost pre-routing.

3. **Cite Holloway et al. (NeurIPS 2024 Workshop)** which explicitly motivated this direction.

4. **Fix the arithmetic.** 9 × 300 × 3 × $0.30 = $2,430, not $810. If Qwen3-Coder-Next actually costs ~$0.05/instance, state that directly.

5. **Estimate the improvement headroom** by first running the 3 granularity configs on a pilot (50 instances) to see how much variance there is in which config wins. If one config dominates (>80% of instances), adaptive selection has limited value and the paper's premise weakens.

6. **For EMNLP venue fit,** the method version (point 1) is much stronger than an empirical study. Frame around how LLMs comprehend code at different abstraction levels and how NL signals can steer this comprehension — this is genuinely an NLP question.

7. **Consider combining NL and code features** to differentiate from both SIADAFIX (NL, LLM classifier) and Triage (code, ML classifier). A lightweight model that uses both feature families, available at different stages of the pipeline, could be a stronger contribution.

### Round 3 review
Verdict: revise
Issues: ["IMPORTANT: Missing justification for DPO over classification — the proposal frames this as 'configuration preference learning' using DPO-style loss, but the task is essentially 9-class configuration prediction from features. The evaluation plan lacks an ablation comparing DPO preference learning against simpler multi-class classification (e.g., random forest, logistic regression, or even a simple MLP classifier trained on oracle labels). Without this comparison, the DPO framing appears to be methodological window-dressing rather than a substantive contribution. RouteLLM (arXiv 2406.18665) showed that preference data can train effective routers, but it also demonstrated that simpler classifiers can perform comparably in certain regimes.", "Missing methodological competitors — RouteLLM (arXiv 2406.18665, ICML 2025) trains LLM routers from preference data, which is the identical training paradigm applied to a different routing target (model selection vs. config selection). RADAR (arXiv 2509.25426) is a difficulty-aware routing framework for reasoning LLMs using learned item-response models. Both should be cited and differentiated to strengthen the methodological positioning.", "Three contributions may be too many for a 4-page short paper — 'the method,' 'the design,' and 'the insight' are partially overlapping (the design IS the method). Consider consolidating to: (1) the DPO-trained configuration router as the method contribution, (2) the empirical analysis connecting NL features to optimal granularity as supporting evidence. The two-stage NL→NL+Code architecture is a design choice within the method, not a standalone contribution.", "Headroom quantification is deferred — the proposal correctly includes a go/no-go gate, but the paper's entire premise rests on the oracle advantage being ≥5pp over best fixed config. The arXiv 2604.00167 study (50 instances, 2 repos) found function-level at 45.6% vs. file-level at 42.6% — only a 3pp gap between best and worst fixed configs, with per-instance variance not quantified as an oracle bound. The headroom may be too small for meaningful routing improvement.", "SWE-bench-Live evaluation details are underspecified — the proposal says 'held-out SWE-bench-Live instances' but doesn't specify: how many instances will be used, which subset/time period, whether Docker environments are available for all instances, or how to handle the ~10-15% setup failure rate. SWE-bench-Live's automated curation pipeline may produce instances of varying difficulty distribution from the training set (SWE-bench Verified).", "UniXcoder (2022) encoder choice — while adequate, UniXcoder is 4 years old. More recent code encoders (CodeSage 2024, StarEncoder, or even a frozen Qwen2.5-Coder-1.5B as encoder) may provide better issue text representations. The choice should be justified or an encoder ablation included."]
Feedback: The proposal has improved substantially from Round 2 — it's now a proper method contribution with realistic costs and a genuine gap. To push this to pass quality:

1. **Add a DPO-vs-classification ablation.** This is the single most important missing piece. If a simple random forest on the same features performs comparably to the DPO-trained UniXcoder router, the 'preference learning' framing collapses into standard classification. Include at minimum: (a) random forest on NL+code features, (b) MLP classifier on UniXcoder embeddings, (c) your DPO preference router. If DPO wins, explain why (handles noisy/partial orderings better? learns from relative rather than absolute signals?). If it doesn't, the paper's main selling point is undermined.

2. **Cite RouteLLM and RADAR.** RouteLLM (Ong et al., ICML 2025) is the closest methodological parallel — it trains routers from preference data, just for model selection instead of config selection. RADAR (arXiv 2509.25426) uses item-response theory for difficulty-aware routing. Both strengthen your related work section and help position your contribution.

3. **Consolidate to 2 contributions** for the short paper: (1) the configuration preference learning method (encompassing the two-stage design), (2) the empirical analysis of which NL/code features predict optimal granularity. Three separate contributions in 4 pages will feel thin on each.

4. **Run the headroom pilot FIRST**, then write the paper around the actual numbers. If headroom is 5-8pp, discuss the cost-efficiency angle (routing saves API cost by avoiding expensive configs). If headroom is >10pp, lead with accuracy improvement. The framing should adapt to the data.

5. **Specify SWE-bench-Live evaluation**: target ~100-200 instances from the most recent monthly batch (to ensure decontamination), confirm Docker environment availability, and plan for the ~10-15% setup failure rate.

6. **Discuss the minimal-headroom scenario** in the paper: if the oracle advantage is small, argue that the routing still provides value through cost efficiency (cheaper configs for easy instances) even if accuracy gains are modest. This makes the contribution robust to disappointing headroom numbers.

### Round 4 review
Verdict: revise
Issues: ["CRITICAL: Missing Mix-of-Granularity (MoG, COLING 2025, arXiv 2406.00456) — trains a router to dynamically select optimal retrieval granularity for RAG using soft labels, which is the same core mechanism as GranRoute. The only difference is domain (general QA vs. code repair). This must be cited and explicitly differentiated; without it, the novelty claim ('no routing method targets retrieval configuration') is factually incorrect — MoG targets retrieval granularity, which is a subset of GranRoute's configuration space.", "CRITICAL: Missing RAGRouter (NeurIPS 2025, arXiv 2505.23052) — the first routing method specifically designed for RAG settings, using document embeddings and RAG capability embeddings. As a NeurIPS 2025 paper on routing in RAG, it is highly relevant and would be noticed by any reviewer familiar with the routing literature.", "IMPORTANT: Missing 'Rethinking Predictive LLM Routing' (arXiv 2505.12601, May 2025) — demonstrates that a simple kNN baseline matches or outperforms complex learned routers across diverse tasks. This directly challenges GranRoute's elaborate 5-method comparison: if kNN dominates, the entire multi-method contribution collapses. This paper must be cited, and kNN must be included as a 6th baseline method.", "IMPORTANT: Missing ProCC (arXiv 2405.07530, TOSEM 2025) — uses multi-retrieval augmented generation with adaptive retrieval selection for code completion. While it targets code completion rather than repair, it is in the same domain (adaptive retrieval for code tasks) and must be cited.", "Headroom risk remains unresolved and foundational — the arXiv 2604.00167 study found only 3pp difference between best and worst fixed granularities (function 45.6% vs. file 42.6%) on 50 instances. The oracle bound (per-instance best) over the best fixed config could be only 2-5pp. The go/no-go gate is good, but if the headroom is <5pp, the paper's entire premise weakens to a cost-efficiency argument, which may not sustain a publication even as a short paper.", "The 5-method comparison contribution is vulnerable to the 'ablation-as-paper' criticism, especially given that existing routing benchmarks (LLMRouterBench, RouterEval) already provide more comprehensive method comparisons. The paper needs a clear narrative about what novel insight emerges from the comparison (e.g., 'code repair routing requires fundamentally different methods than model routing because...'), not just which method achieves the highest number."]
Feedback: The proposal has matured substantially over 4 rounds — the feasibility is now realistic, the gap argument is well-supported, and the approach is sensible. The remaining issues are fixable but important:

1. **Cite and differentiate from MoG (COLING 2025).** MoG is the single biggest threat to novelty. The differentiation should argue: (a) MoG routes over text chunking granularity for knowledge QA, while GranRoute routes over fault-localization granularity + context budget jointly for code repair — a 2D configuration space vs. 1D; (b) MoG uses soft labels from retrieval quality, while GranRoute uses downstream repair success as oracle signal — end-task alignment; (c) code repair has unique routing signals (stack traces, error types, code structure) unavailable in QA. This is a legitimate distinction but must be made explicit.

2. **Cite RAGRouter (NeurIPS 2025)** and position GranRoute as targeting a different routing dimension (retrieval configuration vs. which RAG-LLM to use).

3. **Add kNN as a baseline method.** Given the findings from 'Rethinking Predictive LLM Routing,' include a 6th method — kNN on the same feature space. If kNN dominates, the paper's insight becomes 'simple non-parametric methods suffice for code repair routing' — still publishable as a short paper. If learned methods beat kNN, you have stronger justification for the routing framework.

4. **Cite ProCC** and distinguish by target task (completion vs. repair) and routing target (retrieval perspective vs. configuration).

5. **Strengthen the multi-method comparison narrative.** The paper should not just report 'Method X wins.' It should extract a generalizable insight: Do preference-based methods (à la RouteLLM) work better for configuration routing than classification? Does the answer depend on data size? Does code-specific structure create different routing dynamics than NL routing? Frame the comparison as answering a specific research question about routing methodology, not as an ablation.

6. **Address the small-headroom scenario more concretely.** If the pilot shows 3-5pp headroom, the paper could pivot to a diagnostic contribution: 'We find that retrieval configuration routing for code repair yields X% accuracy gain and Y% cost savings, and that the dominant routing signal is Z.' Even a modest-headroom finding is publishable if the analysis is insightful.

With these changes, the proposal is viable for EMNLP Findings as a short paper. EMNLP Main would require stronger novelty — consider whether the 2D routing space (granularity × budget) with dual-signal architecture (NL + code features at different pipeline stages) can be positioned as a methodological contribution rather than pure domain transfer.

### Round 5 review
Verdict: revise
Issues: ["IMPORTANT: Missing AutoRAG-HP (EMNLP 2024 Findings, arXiv 2406.19251) — formulates RAG hyperparameter tuning (top-k, compression ratio, embedding methods) as online multi-armed bandit. This is a published EMNLP paper on adaptive retrieval configuration selection. It differs from GranRoute in domain (general QA vs. code repair) and paradigm (online bandit vs. offline routing), but must be cited as it directly addresses the same problem category — learning to adapt retrieval parameters per instance.", "IMPORTANT: Anti-evidence not addressed — SWEzze (arXiv 2603.28119) shows that *compressing* code context by 6x (removing 51-71% of tokens) improves issue resolution rates by 5-9.2%. This directly challenges the premise that selecting the right retrieval configuration matters — if aggressively removing context *helps*, the bottleneck is LLM context utilization, not retrieval strategy. Similarly, 'Context Length Alone Hurts LLM Performance Despite Perfect Retrieval' (arXiv 2510.05381) shows 13.9-85% performance degradation from input length growth even with perfect retrieval. The proposal must acknowledge and address this tension: if the LLM can't effectively use retrieved context, routing to the 'right' configuration may have a low ceiling.", "IMPORTANT: The NeurIPS 2024 exploration-exploitation paper (arXiv 2405.17503) frames code repair as a bandit problem and argues the dominant lever is sampling diversity (generating diverse patches via different prompts/LLMs), not retrieval configuration. Top SWE-bench systems (Devlo at 70.2%) achieve results through multi-LLM diverse sampling, not adaptive retrieval. The proposal should discuss whether compute budget is better spent on retrieval routing vs. diverse patch generation.", "Short paper scope overload — 6 routing methods × 2 feature families × CodeSage-base vs. UniXcoder encoder ablation × MoG-adapted baseline = at least 24 cells in the main comparison table, plus per-difficulty-tier analysis, SHAP analysis, and cost-efficiency analysis. This is too much for 4 pages. Consider reducing to 4 core methods (kNN, random forest, MLP, Bradley-Terry) with LambdaMART and IRT as supplementary, and dropping the encoder ablation from the main paper.", "The 3pp gap between best and worst fixed granularities in arXiv 2604.00167 (45.6% vs 42.6%) is concerning for headroom. While the oracle bound (per-instance best) should be higher, the 2D configuration space only helps if granularity and budget interact — i.e., the optimal budget differs by granularity. The proposal should explicitly hypothesize about interaction effects and include interaction analysis in the pilot.", "Minor: SWE-bench-Live's monthly batches are a 'stated plan' (arXiv 2505.23419), not confirmed operational practice. The proposal should verify that monthly batches are actually being released before depending on them for evaluation."]
Feedback: The proposal has matured impressively over 5 rounds — feasibility is nailed, the gap is genuine, and the experimental design (especially the MoG-adapted baseline and kNN comparison) is thoughtful. The remaining barrier to passing is that the proposal doesn't engage with the strongest counterargument to its premise.

Specific changes needed:

1. **Address the compression-beats-retrieval tension head-on.** The SWEzze finding (6x compression improves results) and the context-length-hurts evidence (arXiv 2510.05381) are the strongest objections any reviewer will raise. Argue explicitly: GranRoute's routing is *complementary* to context compression — it selects the right structural granularity (file vs. function vs. line) and budget *before* compression. The insight is that starting from the right abstraction level matters even after compression. You could even frame GranRoute as the upstream complement to SWEzze's downstream compression: GranRoute selects *what* to retrieve, SWEzze compresses *how much* to keep. If the pilot data shows that GranRoute + compression outperforms either alone, this becomes a strong narrative.

2. **Cite AutoRAG-HP (EMNLP 2024 Findings)** and differentiate: AutoRAG-HP tunes continuous retrieval hyperparameters (top-k, compression ratio) online via bandit learning; GranRoute selects discrete structural abstractions (file/function/line) offline via end-task labels. The key distinction is that GranRoute's granularity choices are *structurally distinct program abstractions*, not just different numeric parameter values.

3. **Discuss the exploration-exploitation tradeoff.** Acknowledge that diverse patch generation (multiple LLMs/prompts) is an alternative way to spend compute budget. Position GranRoute as orthogonal: routing selects the best *input* to the repair model, while diversity operates on the *output* side. They should compose.

4. **Tighten scope for short paper.** Reduce to 4 core methods (kNN, random forest, MLP, Bradley-Terry) in the main paper. Move LambdaMART, IRT, and encoder ablation to supplementary. This focuses the narrative on the kNN vs. learned methods question (RQ1) and NL vs. NL+Code signals question (RQ2) without diluting across too many comparisons.

5. **Add interaction analysis to the pilot.** In Phase 1, explicitly measure whether the optimal budget depends on granularity (and vice versa). If there are no interaction effects, the 2D routing problem decomposes into two independent 1D problems, which weakens the contribution relative to MoG. If interactions exist, highlight them as the key differentiator.

6. **Reframe the contribution hierarchy.** Lead with the empirical question ('Does configuration routing help code repair, and does it behave differently from text QA routing?') rather than the framework ('GranRoute, the first...'). The most publishable version of this paper answers a question about code understanding at different abstraction levels — when does structural granularity matter, what bug features predict it, and can simple methods capture it? This is an NLP question, not just an SE pipeline question.

With these changes, the novelty framing becomes: 'We test whether granularity routing (MoG) and kNN routing sufficiency (arXiv 2505.12601) transfer from text QA and model routing to the structurally richer code repair setting, finding [specific insight about when they do/don't transfer].' This is a solid Findings contribution.


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
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "355eb5ea-af0c-4995-9941-6e738e41a87c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T00:19:06.881Z_

```json
{
  "parentUuid": "355eb5ea-af0c-4995-9941-6e738e41a87c",
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
  "uuid": "45b34fc8-fdc8-4307-b799-97ab0e758492",
  "timestamp": "2026-05-12T00:19:06.881Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T00:19:06.881Z_

```json
{
  "parentUuid": "45b34fc8-fdc8-4307-b799-97ab0e758492",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c3bd8711-1c69-43be-af91-255b64c9d443",
  "timestamp": "2026-05-12T00:19:06.881Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "c3bd8711-1c69-43be-af91-255b64c9d443",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive context routing for code repair",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Assistant

_source line 8 · 2026-05-12T00:19:15.718Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea, which is now in round 6 of 10. The proposal has evolved significantly over 5 rounds of revision. Let me conduct independent verification of the key claims and assess whether the remaining issues from round 5 have been addressed.

Let me systematically verify:
1. Whether the cited papers exist and say what's claimed
2. Whether the gap is real (especially checking for MoG, AutoRAG-HP, and other competitors)
3. Whether the anti-evidence (SWEzze, context-length-hurts) is properly addressed


4. Whether the feasibility is realistic
5. Whether the novelty is sufficient for EMNLP Findings

Now I need to search for evidence on these points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3bd8711-1c69-43be-af91-255b64c9d443",
  "isSidechain": false,
  "requestId": "req_011CawiUfLLytSW8inkpGn4h",
  "type": "assistant",
  "uuid": "2f5f13c5-5ee8-433a-a40e-bd7e694c4b4d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TXxvmro93CaU96ErGa6c5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24241,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1286,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24241
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

_source line 9 · 2026-05-12T00:19:16.468Z_

I'll conduct independent verification of this proposal's claims, checking for missing competitors, validating cited work, and stress-testing the novelty argument. Let me run several parallel searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f5f13c5-5ee8-433a-a40e-bd7e694c4b4d",
  "isSidechain": false,
  "requestId": "req_011CawiUfLLytSW8inkpGn4h",
  "type": "assistant",
  "uuid": "91f5e078-347f-456d-8363-6d46147aa94e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TXxvmro93CaU96ErGa6c5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24241,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1286,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24241
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

_source line 10 · 2026-05-12T00:19:22.429Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01QFjJ4kHAp1eHBF36Nfq7i1`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Verify MoG and AutoRAG-HP papers",
  "prompt": "Search for these two papers and verify they exist and match the claims made about them:\n\n1. \"Mix-of-Granularity\" (MoG) - claimed to be at COLING 2025, arXiv 2406.00456. Claimed to train an MLP router to select optimal text chunking granularity for RAG using soft labels from BM25 retrieval similarity.\n\n2. \"AutoRAG-HP\" - claimed to be at EMNLP 2024 Findings, arXiv 2406.19251. Claimed to formulate RAG hyperparameter tuning as online multi-armed bandit.\n\nUse WebSearch to find these papers and verify: (a) they exist, (b) their venue is correct, (c) the description of what they do is accurate.\n\nReport findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91f5e078-347f-456d-8363-6d46147aa94e",
  "isSidechain": false,
  "requestId": "req_011CawiUfLLytSW8inkpGn4h",
  "type": "assistant",
  "uuid": "c6ede56d-bb2f-419b-87ae-5543f698bc5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TXxvmro93CaU96ErGa6c5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24241,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1286,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24241
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

_source line 11 · 2026-05-12T00:19:27.262Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NoyvbMUvfR7d8vGBUAsYZT`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search for competing work on adaptive code repair",
  "prompt": "Search for recent papers (2024-2026) on adaptive retrieval configuration for code repair or code generation. I need to find any work the proposal may have missed. Use WebSearch with these queries:\n\n1. \"adaptive retrieval granularity code repair 2025 2026\"\n2. \"fault localization context selection LLM program repair\"\n3. \"retrieval-augmented code repair adaptive context\"\n4. \"site:arxiv.org code repair retrieval configuration 2026\"\n5. \"per-instance retrieval adaptation code generation\"\n\nReport any papers found that are relevant to dynamically selecting retrieval granularity or context configuration for code tasks. Include titles, venues, and brief descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6ede56d-bb2f-419b-87ae-5543f698bc5f",
  "isSidechain": false,
  "requestId": "req_011CawiUfLLytSW8inkpGn4h",
  "type": "assistant",
  "uuid": "69fb23c5-42d4-4697-a2a8-d6905450c4c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TXxvmro93CaU96ErGa6c5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24241,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1286,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24241
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

_source line 12 · 2026-05-12T00:19:33.444Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013zUksxBufZ3yXwfd9v9WMs`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Verify SWEzze and context-length papers",
  "prompt": "Search for and verify these papers:\n\n1. SWEzze (arXiv 2603.28119) - claimed to show 6x compression of code context improves issue resolution by 5-9.2%, with only 8.4% relevance density in retrieved contexts.\n\n2. \"Context Length Alone Hurts LLM Performance Despite Perfect Retrieval\" (arXiv 2510.05381) - claimed to show 13.9-85% performance degradation from context length growth even with perfect retrieval.\n\n3. SeleCom (arXiv 2602.15856) - claimed to show selection and compression are complementary.\n\n4. \"Rethinking Predictive Modeling for LLM Routing: kNN\" (arXiv 2505.12601) - claimed to show kNN matches or outperforms learned routers.\n\nUse WebSearch to verify existence and accuracy of claims. Report findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69fb23c5-42d4-4697-a2a8-d6905450c4c8",
  "isSidechain": false,
  "requestId": "req_011CawiUfLLytSW8inkpGn4h",
  "type": "assistant",
  "uuid": "14cd820b-13ab-457f-807b-3fd0e3e03b28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TXxvmro93CaU96ErGa6c5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24241,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1286,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24241
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

_source line 13 · 2026-05-12T00:19:37.970Z_

<details><summary>↩ Tool result · `toolu_01QFjJ4kHAp1eHBF36Nfq7i1`</summary>

```text
## Findings

### Paper 1: Mix-of-Granularity (MoG)

**Status: VERIFIED**

- **Existence**: Confirmed - arXiv 2406.00456
- **Venue**: CONFIRMED - Published at COLING 2025 (Proceedings of the 31st International Conference on Computational Linguistics)
- **Description Accuracy**: PARTIALLY ACCURATE with refinement needed
  - The paper does train a router to select optimal text chunking granularity for RAG
  - The router is trained with a "newly proposed loss function employing soft labels" (confirmed)
  - However, the description of "soft labels from BM25 retrieval similarity" is not explicitly mentioned in the search results - it mentions soft labels but doesn't specify BM25 as the source

### Paper 2: AutoRAG-HP

**Status: VERIFIED**

- **Existence**: Confirmed - arXiv 2406.19251
- **Venue**: CONFIRMED - Published at EMNLP 2024 Findings (not main conference, but Findings track)
- **Description Accuracy**: CONFIRMED
  - The paper does formulate RAG hyperparameter tuning as an online multi-armed bandit (MAB) problem
  - Introduces a Hierarchical MAB (Hier-MAB) method for efficient exploration
  - Evaluates tuning of hyperparameters like top-k retrieved documents, prompt compression ratio, and embedding methods

## Summary

Both papers exist and their venues are correctly identified. The AutoRAG-HP description is fully accurate. The MoG description is largely accurate regarding the core method (router for granularity selection with soft labels), though the specific mention of "BM25 retrieval similarity" as the source of soft labels would require reading the full paper to verify.

**Sources:**
- [Mix-of-Granularity arXiv](https://arxiv.org/abs/2406.00456)
- [Mix-of-Granularity COLING 2025](https://aclanthology.org/2025.coling-main.384/)
- [AutoRAG-HP arXiv](https://arxiv.org/abs/2406.19251)
- [AutoRAG-HP EMNLP 2024 Findings](https://aclanthology.org/2024.findings-emnlp.223/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6ede56d-bb2f-419b-87ae-5543f698bc5f",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "673a46d7-e65e-4a90-8ae7-8a448b22bfea",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for these two papers and verify they exist and match the claims made about them:\n\n1. \"Mix-of-Granularity\" (MoG) - claimed to be at COLING 2025, arXiv 2406.00456. Claimed to train an MLP router to select optimal text chunking granularity for RAG using soft labels from BM25 retrieval similarity.\n\n2. \"AutoRAG-HP\" - claimed to be at EMNLP 2024 Findings, arXiv 2406.19251. Claimed to formulate RAG hyperparameter tuning as online multi-armed bandit.\n\nUse WebSearch to find these papers and verify: (a) they exist, (b) their venue is correct, (c) the description of what they do is accurate.\n\nReport findings concisely.",
    "agentId": "a4f427789cc93ebc1",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Findings\n\n### Paper 1: Mix-of-Granularity (MoG)\n\n**Status: VERIFIED**\n\n- **Existence**: Confirmed - arXiv 2406.00456\n- **Venue**: CONFIRMED - Published at COLING 2025 (Proceedings of the 31st International Conference on Computational Linguistics)\n- **Description Accuracy**: PARTIALLY ACCURATE with refinement needed\n  - The paper does train a router to select optimal text chunking granularity for RAG\n  - The router is trained with a \"newly proposed loss function employing soft labels\" (confirmed)\n  - However, the description of \"soft labels from BM25 retrieval similarity\" is not explicitly mentioned in the search results - it mentions soft labels but doesn't specify BM25 as the source\n\n### Paper 2: AutoRAG-HP\n\n**Status: VERIFIED**\n\n- **Existence**: Confirmed - arXiv 2406.19251\n- **Venue**: CONFIRMED - Published at EMNLP 2024 Findings (not main conference, but Findings track)\n- **Description Accuracy**: CONFIRMED\n  - The paper does formulate RAG hyperparameter tuning as an online multi-armed bandit (MAB) problem\n  - Introduces a Hierarchical MAB (Hier-MAB) method for efficient exploration\n  - Evaluates tuning of hyperparameters like top-k retrieved documents, prompt compression ratio, and embedding methods\n\n## Summary\n\nBoth papers exist and their venues are correctly identified. The AutoRAG-HP description is fully accurate. The MoG description is largely accurate regarding the core method (router for granularity selection with soft labels), though the specific mention of \"BM25 retrieval similarity\" as the source of soft labels would require reading the full paper to verify.\n\n**Sources:**\n- [Mix-of-Granularity arXiv](https://arxiv.org/abs/2406.00456)\n- [Mix-of-Granularity COLING 2025](https://aclanthology.org/2025.coling-main.384/)\n- [AutoRAG-HP arXiv](https://arxiv.org/abs/2406.19251)\n- [AutoRAG-HP EMNLP 2024 Findings](https://aclanthology.org/2024.findings-emnlp.223/)"
      }
    ],
    "totalDurationMs": 15536,
    "totalTokens": 20099,
    "totalToolUseCount": 2,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2771,
      "cache_read_input_tokens": 16765,
      "output_tokens": 556,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2771
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 556,
          "cache_read_input_tokens": 16765,
          "cache_creation_input_tokens": 2771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2771,
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
      "otherToolCount": 2
    }
  },
  "sourceToolAssistantUUID": "c6ede56d-bb2f-419b-87ae-5543f698bc5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-12T00:19:38.338Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SR2hfrSHa6c1c6FuQdi7zR`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Search for concurrent/missing competitors",
  "prompt": "Search for recent papers (2025-2026) that might compete with or overlap with a proposal to do per-instance routing of retrieval configuration (granularity + context budget) for code repair. Use WebSearch with these queries:\n\n1. \"METIS RAG configuration adaptation per query 2025\"\n2. \"BEST-Route LLM routing sampling ICML 2025\"\n3. \"LTRR learning to rank retrievers SIGIR 2025\"\n4. \"RouteLLM preference data routing ICLR 2025\"\n5. \"adaptive context selection software engineering agents 2026\"\n6. \"SWE-bench retrieval optimization 2026\"\n\nReport any papers found with titles, venues, and relevance to per-instance retrieval configuration routing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "673a46d7-e65e-4a90-8ae7-8a448b22bfea",
  "isSidechain": false,
  "requestId": "req_011CawiUfLLytSW8inkpGn4h",
  "type": "assistant",
  "uuid": "0f91e6ef-a577-4f9a-b6e5-1093ee95ba2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017TXxvmro93CaU96ErGa6c5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 24241,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 24241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1286,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 24241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 24241
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

_source line 15 · 2026-05-12T00:19:49.097Z_

<details><summary>↩ Tool result · `toolu_013zUksxBufZ3yXwfd9v9WMs`</summary>

```text
## Summary of Paper Verification

All four papers exist and I verified the key claims. Here are the findings:

### 1. SWEzze (arXiv 2603.28119) - VERIFIED
**Title:** "Compressing Code Context for LLM-based Issue Resolution"
- **6x compression:** Confirmed - maintains stable compression rate of ~6x across models
- **5-9.2% improvement:** Confirmed - improves issue resolution rates by 5.0%-9.2%
- **8.4% relevance density claim:** Not found in search results - claim not verified

### 2. Context Length Alone Hurts LLM Performance (arXiv 2510.05381) - VERIFIED
**Title:** "Context Length Alone Hurts LLM Performance Despite Perfect Retrieval"
- **13.9-85% degradation claim:** Not explicitly stated in search summary, but the paper confirms substantial performance degradation from context length growth even with perfect retrieval
- Core finding confirmed - performance degrades substantially even when models can perfectly retrieve all relevant information

### 3. SeleCom (arXiv 2602.15856) - VERIFIED
**Title:** "Rethinking Soft Compression in Retrieval-Augmented Generation: A Query-Conditioned Selector Perspective"
- **Selection and compression complementarity:** Confirmed indirectly - SeleCom redefines the encoder as a query-conditioned selector and achieves competitive performance with 33.8%-84.6% reduction in computation and latency
- The paper's approach demonstrates selection and compression working together within a unified framework

### 4. Rethinking Predictive Modeling for LLM Routing (arXiv 2505.12601) - VERIFIED
**Title:** "Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers"
- **kNN matches/outperforms learned routers:** Confirmed - kNN with k=100 achieves AUC of 52.68, competitive with MLP (51.71) and Graph Neural Networks (51.82)

**Status:** All four papers exist. Three have their main claims fully verified. The 8.4% relevance density claim for SWEzze and specific percentage figures for paper #2 could not be confirmed from available abstracts/summaries.

Sources:
- [SWEzze - arXiv 2603.28119](https://arxiv.org/abs/2603.28119)
- [Context Length Alone Hurts LLM Performance - arXiv 2510.05381](https://arxiv.org/abs/2510.05381)
- [SeleCom - arXiv 2602.15856](https://arxiv.org/abs/2602.15856)
- [Rethinking Predictive Modeling for LLM Routing - arXiv 2505.12601](https://arxiv.org/abs/2505.12601)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14cd820b-13ab-457f-807b-3fd0e3e03b28",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "024c0715-0bd4-4e14-a0c4-87e73122eef5",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify these papers:\n\n1. SWEzze (arXiv 2603.28119) - claimed to show 6x compression of code context improves issue resolution by 5-9.2%, with only 8.4% relevance density in retrieved contexts.\n\n2. \"Context Length Alone Hurts LLM Performance Despite Perfect Retrieval\" (arXiv 2510.05381) - claimed to show 13.9-85% performance degradation from context length growth even with perfect retrieval.\n\n3. SeleCom (arXiv 2602.15856) - claimed to show selection and compression are complementary.\n\n4. \"Rethinking Predictive Modeling for LLM Routing: kNN\" (arXiv 2505.12601) - claimed to show kNN matches or outperforms learned routers.\n\nUse WebSearch to verify existence and accuracy of claims. Report findings concisely.",
    "agentId": "ad4cf765371b883b1",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Paper Verification\n\nAll four papers exist and I verified the key claims. Here are the findings:\n\n### 1. SWEzze (arXiv 2603.28119) - VERIFIED\n**Title:** \"Compressing Code Context for LLM-based Issue Resolution\"\n- **6x compression:** Confirmed - maintains stable compression rate of ~6x across models\n- **5-9.2% improvement:** Confirmed - improves issue resolution rates by 5.0%-9.2%\n- **8.4% relevance density claim:** Not found in search results - claim not verified\n\n### 2. Context Length Alone Hurts LLM Performance (arXiv 2510.05381) - VERIFIED\n**Title:** \"Context Length Alone Hurts LLM Performance Despite Perfect Retrieval\"\n- **13.9-85% degradation claim:** Not explicitly stated in search summary, but the paper confirms substantial performance degradation from context length growth even with perfect retrieval\n- Core finding confirmed - performance degrades substantially even when models can perfectly retrieve all relevant information\n\n### 3. SeleCom (arXiv 2602.15856) - VERIFIED\n**Title:** \"Rethinking Soft Compression in Retrieval-Augmented Generation: A Query-Conditioned Selector Perspective\"\n- **Selection and compression complementarity:** Confirmed indirectly - SeleCom redefines the encoder as a query-conditioned selector and achieves competitive performance with 33.8%-84.6% reduction in computation and latency\n- The paper's approach demonstrates selection and compression working together within a unified framework\n\n### 4. Rethinking Predictive Modeling for LLM Routing (arXiv 2505.12601) - VERIFIED\n**Title:** \"Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers\"\n- **kNN matches/outperforms learned routers:** Confirmed - kNN with k=100 achieves AUC of 52.68, competitive with MLP (51.71) and Graph Neural Networks (51.82)\n\n**Status:** All four papers exist. Three have their main claims fully verified. The 8.4% relevance density claim for SWEzze and specific percentage figures for paper #2 could not be confirmed from available abstracts/summaries.\n\nSources:\n- [SWEzze - arXiv 2603.28119](https://arxiv.org/abs/2603.28119)\n- [Context Length Alone Hurts LLM Performance - arXiv 2510.05381](https://arxiv.org/abs/2510.05381)\n- [SeleCom - arXiv 2602.15856](https://arxiv.org/abs/2602.15856)\n- [Rethinking Predictive Modeling for LLM Routing - arXiv 2505.12601](https://arxiv.org/abs/2505.12601)"
      }
    ],
    "totalDurationMs": 15649,
    "totalTokens": 22027,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 2672,
      "cache_creation_input_tokens": 1864,
      "cache_read_input_tokens": 16790,
      "output_tokens": 701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1864
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2672,
          "output_tokens": 701,
          "cache_read_input_tokens": 16790,
          "cache_creation_input_tokens": 1864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1864,
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
  "sourceToolAssistantUUID": "14cd820b-13ab-457f-807b-3fd0e3e03b28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T00:19:51.655Z_

<details><summary>↩ Tool result · `toolu_01NoyvbMUvfR7d8vGBUAsYZT`</summary>

```text
## Research Findings: Recent Papers on Adaptive Retrieval Configuration for Code Repair/Generation

Based on the web searches, I found several highly relevant papers from 2024-2026 that address adaptive retrieval configuration, context selection, and granularity for code tasks:

### Most Relevant Papers

**1. On the Role of Fault Localization Context for LLM-Based Program Repair** (2026)
- **Venue**: arXiv
- **Key Finding**: Empirical study showing that more context does not consistently improve repair performance. File-level localization is the dominant factor (15-17x improvement over no-file baseline), while line-level context expansion frequently degrades performance due to noise. Optimal results found with 6-10 relevant files.
- **Relevance**: Directly addresses dynamic context selection and granularity configuration for program repair.

**2. ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation** (September 2025)
- **Venue**: ACM CIKM 2025
- **Key Finding**: Proposes an algorithm-aware hybrid retrieval mechanism that analyzes user queries to infer algorithm type and retrieves relevant exemplars from algorithm-specific knowledge corpus. Uses modular representations for both code and descriptions.
- **Relevance**: Demonstrates adaptive retrieval based on problem characteristics rather than static configuration.

**3. RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code** (2025)
- **Venue**: arXiv
- **Key Finding**: Retrieves relevant code (function signatures and snippets) to guide LLM patch generation using specialized RAG strategies for program repair.
- **Relevance**: Focuses on optimized retrieval granularity specifically for repair tasks.

**4. Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement** (January 2026)
- **Venue**: arXiv
- **Key Finding**: Uses edit-driven code retrieval approach with iterative solution retrieval to dynamically select relevant repair solutions.
- **Relevance**: Per-instance retrieval adaptation through iterative refinement.

**5. ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair** (2026)
- **Venue**: arXiv
- **Key Finding**: Uses graph-based tools and structured representations instead of lexical retrieval, providing agentic systems with fine-grained navigational capabilities.
- **Relevance**: Structured approach to adaptive context selection via graph-based reasoning.

**6. What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond** (March 2025)
- **Venue**: arXiv (2503.20589)
- **Key Finding**: Empirical study finding that in-context code and API information significantly enhance performance (up to 15% improvement), while retrieved similar code introduces noise and degrades results.
- **Relevance**: Addresses what granularity/type of information should be retrieved per-instance.

**7. Improving LLM-Based Fault Localization with External Memory and Project Context** (2025)
- **Venue**: arXiv
- **Key Finding**: Uses static memory with fixed project and class-level summaries prepared before fault localization, dynamically selecting context depth.
- **Relevance**: Pre-computation of multi-level context summaries for dynamic selection.

**8. An Empirical Study of Retrieval-Augmented Code Generation: Challenges and Opportunities** (2025)
- **Venue**: ACM TOSEM
- **Key Finding**: Comprehensive empirical study on RACG identifying challenges and opportunities for adaptive retrieval in code generation.
- **Relevance**: Broad analysis of retrieval configuration challenges across code generation tasks.

### Survey Works Covering Adaptive Approaches

**9. Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches** (October 2025)
- **Venue**: arXiv
- **Coverage**: Discusses diverse RAG strategies including sparse/dense retrieval, graph-based retrieval, hybrid pipelines, and agent-style retrieval with iterative refinement.
- **Relevance**: Comprehensive overview of adaptive retrieval strategies at repository scale.

### Key Themes Across Papers

These papers collectively identify several adaptive retrieval dimensions:
- **Granularity adaptation**: File-level vs. line-level vs. function-level context
- **Type adaptation**: Algorithm-aware retrieval, API information vs. code examples
- **Quantity adaptation**: Optimal number of files/chunks per query
- **Iterative adaptation**: Multi-step retrieval refinement
- **Noise management**: Dynamic filtering to avoid degradation from irrelevant context

Sources:
- [On the Role of Fault Localization Context for LLM-Based Program Repair](https://arxiv.org/abs/2604.05481)
- [ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation](https://arxiv.org/abs/2509.02330)
- [RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code](https://arxiv.org/html/2509.16701)
- [Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement](https://arxiv.org/html/2601.08545.pdf)
- [ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair](https://arxiv.org/html/2605.03117)
- [What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond](https://arxiv.org/abs/2503.20589)
- [Improving LLM-Based Fault Localization with External Memory and Project Context](https://arxiv.org/html/2506.03585v1)
- [An Empirical Study of Retrieval-Augmented Code Generation: Challenges and Opportunities](https://arxiv.org/html/2501.13742)
- [Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches](https://arxiv.org/abs/2510.04905)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69fb23c5-42d4-4697-a2a8-d6905450c4c8",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "6c508210-aa2a-40c6-9b79-ef6c50f52d7d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent papers (2024-2026) on adaptive retrieval configuration for code repair or code generation. I need to find any work the proposal may have missed. Use WebSearch with these queries:\n\n1. \"adaptive retrieval granularity code repair 2025 2026\"\n2. \"fault localization context selection LLM program repair\"\n3. \"retrieval-augmented code repair adaptive context\"\n4. \"site:arxiv.org code repair retrieval configuration 2026\"\n5. \"per-instance retrieval adaptation code generation\"\n\nReport any papers found that are relevant to dynamically selecting retrieval granularity or context configuration for code tasks. Include titles, venues, and brief descriptions.",
    "agentId": "aff9ac7a51a59e977",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Research Findings: Recent Papers on Adaptive Retrieval Configuration for Code Repair/Generation\n\nBased on the web searches, I found several highly relevant papers from 2024-2026 that address adaptive retrieval configuration, context selection, and granularity for code tasks:\n\n### Most Relevant Papers\n\n**1. On the Role of Fault Localization Context for LLM-Based Program Repair** (2026)\n- **Venue**: arXiv\n- **Key Finding**: Empirical study showing that more context does not consistently improve repair performance. File-level localization is the dominant factor (15-17x improvement over no-file baseline), while line-level context expansion frequently degrades performance due to noise. Optimal results found with 6-10 relevant files.\n- **Relevance**: Directly addresses dynamic context selection and granularity configuration for program repair.\n\n**2. ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation** (September 2025)\n- **Venue**: ACM CIKM 2025\n- **Key Finding**: Proposes an algorithm-aware hybrid retrieval mechanism that analyzes user queries to infer algorithm type and retrieves relevant exemplars from algorithm-specific knowledge corpus. Uses modular representations for both code and descriptions.\n- **Relevance**: Demonstrates adaptive retrieval based on problem characteristics rather than static configuration.\n\n**3. RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code** (2025)\n- **Venue**: arXiv\n- **Key Finding**: Retrieves relevant code (function signatures and snippets) to guide LLM patch generation using specialized RAG strategies for program repair.\n- **Relevance**: Focuses on optimized retrieval granularity specifically for repair tasks.\n\n**4. Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement** (January 2026)\n- **Venue**: arXiv\n- **Key Finding**: Uses edit-driven code retrieval approach with iterative solution retrieval to dynamically select relevant repair solutions.\n- **Relevance**: Per-instance retrieval adaptation through iterative refinement.\n\n**5. ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair** (2026)\n- **Venue**: arXiv\n- **Key Finding**: Uses graph-based tools and structured representations instead of lexical retrieval, providing agentic systems with fine-grained navigational capabilities.\n- **Relevance**: Structured approach to adaptive context selection via graph-based reasoning.\n\n**6. What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond** (March 2025)\n- **Venue**: arXiv (2503.20589)\n- **Key Finding**: Empirical study finding that in-context code and API information significantly enhance performance (up to 15% improvement), while retrieved similar code introduces noise and degrades results.\n- **Relevance**: Addresses what granularity/type of information should be retrieved per-instance.\n\n**7. Improving LLM-Based Fault Localization with External Memory and Project Context** (2025)\n- **Venue**: arXiv\n- **Key Finding**: Uses static memory with fixed project and class-level summaries prepared before fault localization, dynamically selecting context depth.\n- **Relevance**: Pre-computation of multi-level context summaries for dynamic selection.\n\n**8. An Empirical Study of Retrieval-Augmented Code Generation: Challenges and Opportunities** (2025)\n- **Venue**: ACM TOSEM\n- **Key Finding**: Comprehensive empirical study on RACG identifying challenges and opportunities for adaptive retrieval in code generation.\n- **Relevance**: Broad analysis of retrieval configuration challenges across code generation tasks.\n\n### Survey Works Covering Adaptive Approaches\n\n**9. Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches** (October 2025)\n- **Venue**: arXiv\n- **Coverage**: Discusses diverse RAG strategies including sparse/dense retrieval, graph-based retrieval, hybrid pipelines, and agent-style retrieval with iterative refinement.\n- **Relevance**: Comprehensive overview of adaptive retrieval strategies at repository scale.\n\n### Key Themes Across Papers\n\nThese papers collectively identify several adaptive retrieval dimensions:\n- **Granularity adaptation**: File-level vs. line-level vs. function-level context\n- **Type adaptation**: Algorithm-aware retrieval, API information vs. code examples\n- **Quantity adaptation**: Optimal number of files/chunks per query\n- **Iterative adaptation**: Multi-step retrieval refinement\n- **Noise management**: Dynamic filtering to avoid degradation from irrelevant context\n\nSources:\n- [On the Role of Fault Localization Context for LLM-Based Program Repair](https://arxiv.org/abs/2604.05481)\n- [ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation](https://arxiv.org/abs/2509.02330)\n- [RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code](https://arxiv.org/html/2509.16701)\n- [Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement](https://arxiv.org/html/2601.08545.pdf)\n- [ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair](https://arxiv.org/html/2605.03117)\n- [What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond](https://arxiv.org/abs/2503.20589)\n- [Improving LLM-Based Fault Localization with External Memory and Project Context](https://arxiv.org/html/2506.03585v1)\n- [An Empirical Study of Retrieval-Augmented Code Generation: Challenges and Opportunities](https://arxiv.org/html/2501.13742)\n- [Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches](https://arxiv.org/abs/2510.04905)"
      }
    ],
    "totalDurationMs": 24389,
    "totalTokens": 23958,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 2754,
      "cache_creation_input_tokens": 2978,
      "cache_read_input_tokens": 16730,
      "output_tokens": 1496,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2978
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2754,
          "output_tokens": 1496,
          "cache_read_input_tokens": 16730,
          "cache_creation_input_tokens": 2978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2978,
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
      "otherToolCount": 5
    }
  },
  "sourceToolAssistantUUID": "69fb23c5-42d4-4697-a2a8-d6905450c4c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "6c508210-aa2a-40c6-9b79-ef6c50f52d7d",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive context routing for code repair",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Tool result

_source line 19 · 2026-05-12T00:20:03.891Z_

<details><summary>↩ Tool result · `toolu_01SR2hfrSHa6c1c6FuQdi7zR`</summary>

```text
## Summary of Competitive Papers Found (2025-2026)

I found several highly relevant papers that directly compete with or closely overlap your proposal on per-instance routing of retrieval configuration:

### Direct Competitors:

1. **METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation** (SOSP 2025)
   - **Venue:** ACM SIGOPS 31st Symposium on Operating Systems Principles
   - **Relevance:** Direct overlap. METIS jointly schedules queries and adapts RAG configurations per-query, including number of retrieved chunks and synthesis methods. Uses query profiling to determine optimal configurations on a per-query basis. Reports 1.64-2.54× latency reduction without quality loss.
   - **Key Distinction:** Focuses on latency/resource optimization through joint scheduling; your proposal likely emphasizes code repair effectiveness.

2. **LTRR: Learning To Rank Retrievers for LLMs** (SIGIR 2025)
   - **Venue:** SIGIR 2025 LiveRAG Workshop (Spotlight)
   - **Relevance:** Highly relevant. Frames retriever selection as a learning-to-rank problem, with per-query routing decisions based on expected utility to downstream LLM performance. Uses pairwise learning approaches.
   - **Key Distinction:** Focuses on ranking multiple retrievers; your proposal appears to focus on granularity and context budget knobs.

3. **RouteLLM: Learning to Route LLMs from Preference Data** (ICLR 2025)
   - **Venue:** International Conference on Learning Representations (ICLR)
   - **Relevance:** Related but different scope. Routes between stronger/weaker LLMs based on query difficulty using preference data. Achieves 2× cost reduction without quality loss.
   - **Key Distinction:** Routes between models rather than retrieval configurations, though the adaptive per-instance routing framework is similar.

4. **BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute** (ICLR 2025)
   - **Venue:** International Conference on Learning Representations (ICLR) / ICML 2025
   - **Relevance:** Related methodology. Adaptively determines compute allocation (number of samples) per query based on difficulty. Cuts costs up to 60% with <1% performance drop.
   - **Key Distinction:** Routes number of samples to generate rather than retrieval parameters, but uses similar per-instance adaptive allocation.

### Secondary/Related:

5. **Adaptive Context Selection for Software Engineering Agents** (2026)
   - **Findings:** Context engineering for coding agents involves adaptive context selection mechanisms, with research showing that better context retrieval and scaffolding yields 4-10 point improvements in SWE-bench scores.
   - **Relevance:** Tangential. Addresses context management in coding agents but at a higher level than specific retrieval configuration routing.

6. **SWE-bench Retrieval Optimization Trends** (2026)
   - **Finding:** Notable result that custom scaffolding and context retrieval can lift SWE-bench scores by 4-10 points, suggesting high impact of retrieval optimization for code repair tasks.
   - **Relevance:** Demonstrates the problem domain but doesn't propose specific per-instance routing methods.

### Key Competitive Insight:

METIS appears to be the most direct competitor—it's already published at a top-tier venue (SOSP 2025) and tackles per-instance configuration adaptation in RAG systems. However, METIS focuses on general RAG quality/latency tradeoffs and resource scheduling, whereas your proposal appears more specialized to code repair tasks with specific focus on granularity and context budget routing.

Sources:
- [METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation](https://arxiv.org/abs/2412.10543)
- [LTRR: Learning To Rank Retrievers for LLMs](https://arxiv.org/abs/2506.13743)
- [RouteLLM: Learning to Route LLMs from Preference Data](https://arxiv.org/abs/2406.18665)
- [BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute](https://arxiv.org/abs/2506.22716)
- [Anthropic 2026 Agentic Coding Trends Report](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f91e6ef-a577-4f9a-b6e5-1093ee95ba2e",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "526f5779-fcd4-45f2-a229-4459d1230628",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent papers (2025-2026) that might compete with or overlap with a proposal to do per-instance routing of retrieval configuration (granularity + context budget) for code repair. Use WebSearch with these queries:\n\n1. \"METIS RAG configuration adaptation per query 2025\"\n2. \"BEST-Route LLM routing sampling ICML 2025\"\n3. \"LTRR learning to rank retrievers SIGIR 2025\"\n4. \"RouteLLM preference data routing ICLR 2025\"\n5. \"adaptive context selection software engineering agents 2026\"\n6. \"SWE-bench retrieval optimization 2026\"\n\nReport any papers found with titles, venues, and relevance to per-instance retrieval configuration routing.",
    "agentId": "a9ae3a878aa277851",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary of Competitive Papers Found (2025-2026)\n\nI found several highly relevant papers that directly compete with or closely overlap your proposal on per-instance routing of retrieval configuration:\n\n### Direct Competitors:\n\n1. **METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation** (SOSP 2025)\n   - **Venue:** ACM SIGOPS 31st Symposium on Operating Systems Principles\n   - **Relevance:** Direct overlap. METIS jointly schedules queries and adapts RAG configurations per-query, including number of retrieved chunks and synthesis methods. Uses query profiling to determine optimal configurations on a per-query basis. Reports 1.64-2.54× latency reduction without quality loss.\n   - **Key Distinction:** Focuses on latency/resource optimization through joint scheduling; your proposal likely emphasizes code repair effectiveness.\n\n2. **LTRR: Learning To Rank Retrievers for LLMs** (SIGIR 2025)\n   - **Venue:** SIGIR 2025 LiveRAG Workshop (Spotlight)\n   - **Relevance:** Highly relevant. Frames retriever selection as a learning-to-rank problem, with per-query routing decisions based on expected utility to downstream LLM performance. Uses pairwise learning approaches.\n   - **Key Distinction:** Focuses on ranking multiple retrievers; your proposal appears to focus on granularity and context budget knobs.\n\n3. **RouteLLM: Learning to Route LLMs from Preference Data** (ICLR 2025)\n   - **Venue:** International Conference on Learning Representations (ICLR)\n   - **Relevance:** Related but different scope. Routes between stronger/weaker LLMs based on query difficulty using preference data. Achieves 2× cost reduction without quality loss.\n   - **Key Distinction:** Routes between models rather than retrieval configurations, though the adaptive per-instance routing framework is similar.\n\n4. **BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute** (ICLR 2025)\n   - **Venue:** International Conference on Learning Representations (ICLR) / ICML 2025\n   - **Relevance:** Related methodology. Adaptively determines compute allocation (number of samples) per query based on difficulty. Cuts costs up to 60% with <1% performance drop.\n   - **Key Distinction:** Routes number of samples to generate rather than retrieval parameters, but uses similar per-instance adaptive allocation.\n\n### Secondary/Related:\n\n5. **Adaptive Context Selection for Software Engineering Agents** (2026)\n   - **Findings:** Context engineering for coding agents involves adaptive context selection mechanisms, with research showing that better context retrieval and scaffolding yields 4-10 point improvements in SWE-bench scores.\n   - **Relevance:** Tangential. Addresses context management in coding agents but at a higher level than specific retrieval configuration routing.\n\n6. **SWE-bench Retrieval Optimization Trends** (2026)\n   - **Finding:** Notable result that custom scaffolding and context retrieval can lift SWE-bench scores by 4-10 points, suggesting high impact of retrieval optimization for code repair tasks.\n   - **Relevance:** Demonstrates the problem domain but doesn't propose specific per-instance routing methods.\n\n### Key Competitive Insight:\n\nMETIS appears to be the most direct competitor—it's already published at a top-tier venue (SOSP 2025) and tackles per-instance configuration adaptation in RAG systems. However, METIS focuses on general RAG quality/latency tradeoffs and resource scheduling, whereas your proposal appears more specialized to code repair tasks with specific focus on granularity and context budget routing.\n\nSources:\n- [METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation](https://arxiv.org/abs/2412.10543)\n- [LTRR: Learning To Rank Retrievers for LLMs](https://arxiv.org/abs/2506.13743)\n- [RouteLLM: Learning to Route LLMs from Preference Data](https://arxiv.org/abs/2406.18665)\n- [BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute](https://arxiv.org/abs/2506.22716)\n- [Anthropic 2026 Agentic Coding Trends Report](https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf)"
      }
    ],
    "totalDurationMs": 25551,
    "totalTokens": 24305,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 5640,
      "cache_read_input_tokens": 16753,
      "output_tokens": 1067,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5640
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 845,
          "output_tokens": 1067,
          "cache_read_input_tokens": 16753,
          "cache_creation_input_tokens": 5640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5640,
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
  "sourceToolAssistantUUID": "0f91e6ef-a577-4f9a-b6e5-1093ee95ba2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-12T00:20:09.949Z_

Good, the key references check out. Now let me do targeted searches for the most critical remaining concerns — anti-evidence, the latest SWE-bench SOTA, and any very recent concurrent work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "526f5779-fcd4-45f2-a229-4459d1230628",
  "isSidechain": false,
  "requestId": "req_011CawiYrNEKJYtveuk4kY8v",
  "type": "assistant",
  "uuid": "a32db3a5-0610-4aeb-a775-67a92ed11e55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6pzBmC3nn7vM3THwrL7rM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5197,
      "cache_read_input_tokens": 36082,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5197,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 36082,
          "cache_creation_input_tokens": 5197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5197
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

_source line 21 · 2026-05-12T00:20:10.473Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UjdLGY2zurMsvTuXeNCvsR`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a32db3a5-0610-4aeb-a775-67a92ed11e55",
  "isSidechain": false,
  "requestId": "req_011CawiYrNEKJYtveuk4kY8v",
  "type": "assistant",
  "uuid": "2d80fa14-9673-4dfa-801e-ed2786f5461a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6pzBmC3nn7vM3THwrL7rM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5197,
      "cache_read_input_tokens": 36082,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5197,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 36082,
          "cache_creation_input_tokens": 5197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5197
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

_source line 22 · 2026-05-12T00:20:10.479Z_

<details><summary>↩ Tool result · `toolu_01UjdLGY2zurMsvTuXeNCvsR`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d80fa14-9673-4dfa-801e-ed2786f5461a",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "290c079f-1612-4c22-ba94-e432cb81c6fe",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "2d80fa14-9673-4dfa-801e-ed2786f5461a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-12T00:20:19.358Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for the most critical things I need to verify independently:

1. SWE-bench SOTA - is Devlo at 70.2% still current?
2. Any very recent work on adaptive retrieval for code repair (2026)
3. The specific arXiv papers cited (2604.00167, 2604.05481)
4. Whether SWE-bench-Live monthly batches are actually operational
5. Anti-evidence: does compression alone suffice?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "290c079f-1612-4c22-ba94-e432cb81c6fe",
  "isSidechain": false,
  "requestId": "req_011CawiZM8cDSTvB9N7Jxka7",
  "type": "assistant",
  "uuid": "62b37ee1-6b9f-4c4a-bf10-b38cb00a21eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012B1Q8kE13GqDqucGDhYxKn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 41279,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 301,
          "cache_read_input_tokens": 41279,
          "cache_creation_input_tokens": 645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 645
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

_source line 24 · 2026-05-12T00:20:19.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pc6B4Br6Y3Hvs2xx1RsizS`</summary>

```json
{
  "query": "SWE-bench Verified leaderboard SOTA 2026 top results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62b37ee1-6b9f-4c4a-bf10-b38cb00a21eb",
  "isSidechain": false,
  "requestId": "req_011CawiZM8cDSTvB9N7Jxka7",
  "type": "assistant",
  "uuid": "a859a27d-d844-462c-aebb-34397f7c1af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012B1Q8kE13GqDqucGDhYxKn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 41279,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 301,
          "cache_read_input_tokens": 41279,
          "cache_creation_input_tokens": 645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 645
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

_source line 25 · 2026-05-12T00:20:20.330Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EVJbpyn59Es3mR5Fk7CuJ8`</summary>

```json
{
  "query": "site:arxiv.org 2604.00167 fault localization granularity code repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a859a27d-d844-462c-aebb-34397f7c1af0",
  "isSidechain": false,
  "requestId": "req_011CawiZM8cDSTvB9N7Jxka7",
  "type": "assistant",
  "uuid": "50ac65e9-6d7c-4063-91ad-80392055c952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012B1Q8kE13GqDqucGDhYxKn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 41279,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 301,
          "cache_read_input_tokens": 41279,
          "cache_creation_input_tokens": 645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 645
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

_source line 26 · 2026-05-12T00:20:20.735Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ryt6fUG4y6TJzEDZ8G8PPd`</summary>

```json
{
  "query": "SWE-bench Live monthly batches operational 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50ac65e9-6d7c-4063-91ad-80392055c952",
  "isSidechain": false,
  "requestId": "req_011CawiZM8cDSTvB9N7Jxka7",
  "type": "assistant",
  "uuid": "6d42614e-b00b-4dc9-82ab-13348f0cf11d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012B1Q8kE13GqDqucGDhYxKn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 41279,
      "output_tokens": 301,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 301,
          "cache_read_input_tokens": 41279,
          "cache_creation_input_tokens": 645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 645
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

_source line 27 · 2026-05-12T00:20:25.903Z_

<details><summary>↩ Tool result · `toolu_01Ryt6fUG4y6TJzEDZ8G8PPd`</summary>

```text
Web search results for query: "SWE-bench Live monthly batches operational 2025 2026"

Links: [{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"GitHub - microsoft/SWE-bench-Live: [NeurIPS 2025 D&B] 🚀 SWE-bench Goes Live!","url":"https://github.com/microsoft/SWE-bench-Live"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-bench-Live/SWE-bench-Live · Datasets at Hugging Face","url":"https://huggingface.co/datasets/SWE-bench-Live/SWE-bench-Live"},{"title":"SWE-bench Goes Live! | OpenReview","url":"https://openreview.net/forum?id=OGWkr7gXka"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Goes Live!","url":"https://arxiv.org/html/2505.23419v2"},{"title":"Overview - SWE-bench","url":"https://www.swebench.com/SWE-bench/"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"NeurIPS Poster SWE-bench Goes Live!","url":"https://neurips.cc/virtual/2025/poster/121677"}]

Based on the search results, here's what I found about SWE-bench Live's monthly batch operations:

## Monthly Update Schedule

SWE-bench-Live is planned to be updated on a monthly basis to provide the community with up-to-date task instances and support rigorous and contamination-free evaluation.

## Batch Details

Each month, 50 newly verified, high-quality issues will be added to the dataset test split. The lite and verified splits will remain frozen, ensuring fair leaderboard comparisons and keeping evaluation costs manageable.

## Current Status

As of September 17, 2025, the dataset was updated with the finalized update process. The most recent statistics show that SWE-bench-Live currently includes 1,890 tasks derived from real GitHub issues created since 2024, spanning 223 repositories.

The benchmark continues to maintain its operational monthly batch updates through 2025 and into 2026, allowing for continuous, contamination-free evaluation of AI systems on real-world software engineering tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d42614e-b00b-4dc9-82ab-13348f0cf11d",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "95caa7be-e51c-4d3b-b16f-61662089f9bb",
  "toolUseResult": {
    "query": "SWE-bench Live monthly batches operational 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RySwGUqhVvkG1hL9V4D9TF",
        "content": [
          {
            "title": "SWE-bench-Live Leaderboard",
            "url": "https://swe-bench-live.github.io/"
          },
          {
            "title": "GitHub - microsoft/SWE-bench-Live: [NeurIPS 2025 D&B] 🚀 SWE-bench Goes Live!",
            "url": "https://github.com/microsoft/SWE-bench-Live"
          },
          {
            "title": "SWE-bench Verified",
            "url": "https://www.vals.ai/benchmarks/swebench"
          },
          {
            "title": "SWE-bench-Live/SWE-bench-Live · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/SWE-bench-Live/SWE-bench-Live"
          },
          {
            "title": "SWE-bench Goes Live! | OpenReview",
            "url": "https://openreview.net/forum?id=OGWkr7gXka"
          },
          {
            "title": "SWE-bench Leaderboards",
            "url": "https://www.swebench.com/"
          },
          {
            "title": "SWE-bench Goes Live!",
            "url": "https://arxiv.org/html/2505.23419v2"
          },
          {
            "title": "Overview - SWE-bench",
            "url": "https://www.swebench.com/SWE-bench/"
          },
          {
            "title": "SWE-Bench Verified Benchmark Leaderboard",
            "url": "https://llm-stats.com/benchmarks/swe-bench-verified"
          },
          {
            "title": "NeurIPS Poster SWE-bench Goes Live!",
            "url": "https://neurips.cc/virtual/2025/poster/121677"
          }
        ]
      },
      "Based on the search results, here's what I found about SWE-bench Live's monthly batch operations:\n\n## Monthly Update Schedule\n\nSWE-bench-Live is planned to be updated on a monthly basis to provide the community with up-to-date task instances and support rigorous and contamination-free evaluation.\n\n## Batch Details\n\nEach month, 50 newly verified, high-quality issues will be added to the dataset test split. The lite and verified splits will remain frozen, ensuring fair leaderboard comparisons and keeping evaluation costs manageable.\n\n## Current Status\n\nAs of September 17, 2025, the dataset was updated with the finalized update process. The most recent statistics show that SWE-bench-Live currently includes 1,890 tasks derived from real GitHub issues created since 2024, spanning 223 repositories.\n\nThe benchmark continues to maintain its operational monthly batch updates through 2025 and into 2026, allowing for continuous, contamination-free evaluation of AI systems on real-world software engineering tasks."
    ],
    "durationSeconds": 5.165098675999994
  },
  "sourceToolAssistantUUID": "6d42614e-b00b-4dc9-82ab-13348f0cf11d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T00:20:26.609Z_

<details><summary>↩ Tool result · `toolu_01Pc6B4Br6Y3Hvs2xx1RsizS`</summary>

```text
Web search results for query: "SWE-bench Verified leaderboard SOTA 2026 top results"

Links: [{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"AI Coding Benchmark Leaderboard 2026: Code Generation and SWE-bench | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-bench Leaderboard: AI Coding Agent SOTA Results | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/browse/agentic/swe-bench"},{"title":"SWE-bench-Live Leaderboard","url":"https://swe-bench-live.github.io/"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"}]

Based on the search results, here are the top results for the SWE-bench Verified leaderboard in 2026:

## SWE-bench Verified SOTA Results (2026)

**Top Performers:**

1. Claude Mythos Preview from Anthropic currently leads the SWE-Bench Verified leaderboard with a score of 0.939 across 89 evaluated AI models (as of April 2026)

2. GPT-5.3 Codex at 85%

3. Claude Opus 4.7 shipped on 2026-04-16 and leads SWE-bench Verified at 87.6% under the Claude Code harness

4. Claude Opus 4.5 at 80.9%

**Important Context:**

It's crucial to note that OpenAI stopped reporting Verified scores in early 2026 and now recommends SWE-bench Pro instead. This shift reflects concerns about data contamination in the Verified benchmark. OpenAI's audit found that every frontier model tested (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could reproduce verbatim gold patches or problem statement specifics for certain SWE-Bench Verified tasks.

For more reliable evaluation, SWE-Bench Pro contains 1,865 tasks across 41 actively maintained repositories spanning Python, Go, TypeScript, and JavaScript, and represents a more contamination-resistant benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a859a27d-d844-462c-aebb-34397f7c1af0",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "80649d13-161b-4485-9963-a62c93e48d64",
  "toolUseResult": {
    "query": "SWE-bench Verified leaderboard SOTA 2026 top results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Cws3SEczLcGw2agotK1DkW",
        "content": [
          {
            "title": "SWE-bench Leaderboards",
            "url": "https://www.swebench.com/"
          },
          {
            "title": "SWE-Bench Verified Benchmark Leaderboard",
            "url": "https://llm-stats.com/benchmarks/swe-bench-verified"
          },
          {
            "title": "SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%",
            "url": "https://www.morphllm.com/swe-bench-pro"
          },
          {
            "title": "SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean",
            "url": "https://www.codeant.ai/blogs/swe-bench-scores"
          },
          {
            "title": "SWE-bench Verified | Epoch AI",
            "url": "https://epoch.ai/benchmarks/swe-bench-verified"
          },
          {
            "title": "AI Coding Benchmark Leaderboard 2026: Code Generation and SWE-bench | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/code-generation"
          },
          {
            "title": "SWE-bench Verified",
            "url": "https://www.swebench.com/verified.html"
          },
          {
            "title": "SWE-bench Leaderboard: AI Coding Agent SOTA Results | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/browse/agentic/swe-bench"
          },
          {
            "title": "SWE-bench-Live Leaderboard",
            "url": "https://swe-bench-live.github.io/"
          },
          {
            "title": "SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale",
            "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public"
          }
        ]
      },
      "Based on the search results, here are the top results for the SWE-bench Verified leaderboard in 2026:\n\n## SWE-bench Verified SOTA Results (2026)\n\n**Top Performers:**\n\n1. Claude Mythos Preview from Anthropic currently leads the SWE-Bench Verified leaderboard with a score of 0.939 across 89 evaluated AI models (as of April 2026)\n\n2. GPT-5.3 Codex at 85%\n\n3. Claude Opus 4.7 shipped on 2026-04-16 and leads SWE-bench Verified at 87.6% under the Claude Code harness\n\n4. Claude Opus 4.5 at 80.9%\n\n**Important Context:**\n\nIt's crucial to note that OpenAI stopped reporting Verified scores in early 2026 and now recommends SWE-bench Pro instead. This shift reflects concerns about data contamination in the Verified benchmark. OpenAI's audit found that every frontier model tested (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could reproduce verbatim gold patches or problem statement specifics for certain SWE-Bench Verified tasks.\n\nFor more reliable evaluation, SWE-Bench Pro contains 1,865 tasks across 41 actively maintained repositories spanning Python, Go, TypeScript, and JavaScript, and represents a more contamination-resistant benchmark."
    ],
    "durationSeconds": 6.730593846000003
  },
  "sourceToolAssistantUUID": "a859a27d-d844-462c-aebb-34397f7c1af0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-12T00:20:30.512Z_

<details><summary>↩ Tool result · `toolu_01EVJbpyn59Es3mR5Fk7CuJ8`</summary>

```text
Web search results for query: "site:arxiv.org 2604.00167 fault localization granularity code repair"

Links: [{"title":"[2604.00167] A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/abs/2604.00167"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale","url":"https://arxiv.org/pdf/2604.00167"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"Exploring Generalizable Automated Program Repair with Large Language Models","url":"https://arxiv.org/html/2506.03283"},{"title":"GALA: Multimodal Graph Alignment for Bug Localization in Automated Program Repair","url":"https://arxiv.org/html/2604.08089"},{"title":"Explainable Fault Localization for Programming Assignments via LLM-Guided Annotation","url":"https://arxiv.org/html/2509.25676"},{"title":"Efficient Black-Box Fault Localization for System-Level Test Code Using Large Language Models","url":"https://arxiv.org/html/2506.19045"},{"title":"Efficient Black-Box Fault Localization for System-Level Test ...","url":"https://arxiv.org/pdf/2506.19045"}]

I found the paper you're looking for! Here's what I found:

The arxiv paper 2604.00167 is titled "A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks", with authors Joseph Townsend, Chandresh Pravin, Kwun Ho Ngan, and Matthieu Parizy from Fujitsu Research of Europe.

**Key findings:**

The study notes that no repository-scale studies have explicitly investigated granularity under the assumption of perfect fault localization, and proposes a framework for performing such tests by modifying the localization phase of the Agentless framework to retrieve ground-truth localization data and include this as context in the prompt fed to the repair phase.

The results show that under this configuration and as a generalization over the SWE-Bench-Mini dataset, function-level granularity yields the highest repair rate against line-level and file-level. However, a deeper dive suggests that the ideal granularity may in fact be task dependent.

The study is not intended to improve on the state-of-the-art, nor do the authors intend for results to be compared against any complete agentic frameworks. Rather, they present a proof of concept for investigating how fault localization may impact automatic code repair in repository-scale scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50ac65e9-6d7c-4063-91ad-80392055c952",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "f287f598-bd94-4141-b025-8bf62279b84d",
  "toolUseResult": {
    "query": "site:arxiv.org 2604.00167 fault localization granularity code repair",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QXNZbpgH4dmnLKCcqCARE3",
        "content": [
          {
            "title": "[2604.00167] A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks",
            "url": "https://arxiv.org/abs/2604.00167"
          },
          {
            "title": "A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks",
            "url": "https://arxiv.org/html/2604.00167"
          },
          {
            "title": "A Study on the Impact of Fault localization Granularity for Repository-Scale",
            "url": "https://arxiv.org/pdf/2604.00167"
          },
          {
            "title": "On the Role of Fault Localization Context for LLM-Based Program Repair",
            "url": "https://arxiv.org/html/2604.05481"
          },
          {
            "title": "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/html/2605.03117"
          },
          {
            "title": "Exploring Generalizable Automated Program Repair with Large Language Models",
            "url": "https://arxiv.org/html/2506.03283"
          },
          {
            "title": "GALA: Multimodal Graph Alignment for Bug Localization in Automated Program Repair",
            "url": "https://arxiv.org/html/2604.08089"
          },
          {
            "title": "Explainable Fault Localization for Programming Assignments via LLM-Guided Annotation",
            "url": "https://arxiv.org/html/2509.25676"
          },
          {
            "title": "Efficient Black-Box Fault Localization for System-Level Test Code Using Large Language Models",
            "url": "https://arxiv.org/html/2506.19045"
          },
          {
            "title": "Efficient Black-Box Fault Localization for System-Level Test ...",
            "url": "https://arxiv.org/pdf/2506.19045"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\nThe arxiv paper 2604.00167 is titled \"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks\", with authors Joseph Townsend, Chandresh Pravin, Kwun Ho Ngan, and Matthieu Parizy from Fujitsu Research of Europe.\n\n**Key findings:**\n\nThe study notes that no repository-scale studies have explicitly investigated granularity under the assumption of perfect fault localization, and proposes a framework for performing such tests by modifying the localization phase of the Agentless framework to retrieve ground-truth localization data and include this as context in the prompt fed to the repair phase.\n\nThe results show that under this configuration and as a generalization over the SWE-Bench-Mini dataset, function-level granularity yields the highest repair rate against line-level and file-level. However, a deeper dive suggests that the ideal granularity may in fact be task dependent.\n\nThe study is not intended to improve on the state-of-the-art, nor do the authors intend for results to be compared against any complete agentic frameworks. Rather, they present a proof of concept for investigating how fault localization may impact automatic code repair in repository-scale scenarios."
    ],
    "durationSeconds": 10.179834711000003
  },
  "sourceToolAssistantUUID": "50ac65e9-6d7c-4063-91ad-80392055c952",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-12T00:20:30.518Z_

```json
{
  "parentUuid": "f287f598-bd94-4141-b025-8bf62279b84d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "adc2dd4c-f971-45b2-bd7a-69f3f2391871",
  "timestamp": "2026-05-12T00:20:30.518Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "adc2dd4c-f971-45b2-bd7a-69f3f2391871",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive context routing for code repair",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Assistant

_source line 33 · 2026-05-12T00:20:40.510Z_

<details><summary>Logged reasoning block</summary>

```text
Important findings:
1. SWE-bench Verified SOTA is now much higher than the claimed 70.2% (Devlo). Claude Mythos Preview at 93.9%, Claude Opus 4.7 at 87.6%. The proposal mentions Devlo at 70.2% which is outdated.
2. arXiv 2604.00167 exists and confirms the claims about function-level granularity.
3. SWE-bench-Live is operational with monthly batches of 50 instances. The proposal plans for ~100 instances which is feasible from recent batches.


4. I should verify a few more details: whether there are recent papers on code repair configuration adaptation from 2026, check the EMNLP 2026 ARR May deadline, and confirm if BEST-Route is actually an ICML 2025 paper rather than ICLR.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adc2dd4c-f971-45b2-bd7a-69f3f2391871",
  "isSidechain": false,
  "requestId": "req_011CawiapE3mFAFs6v88i8GG",
  "type": "assistant",
  "uuid": "d40ca435-765b-4375-bab8-33e92ab70270",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuBNu6W7BrrDhzMgHyp6NT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 685,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 41924,
      "output_tokens": 400,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2021,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 685,
          "output_tokens": 400,
          "cache_read_input_tokens": 41924,
          "cache_creation_input_tokens": 2021,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2021
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

_source line 34 · 2026-05-12T00:20:40.517Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CkAKzQTNoaSTwPn9G8iXQe`</summary>

```json
{
  "query": "EMNLP 2026 ARR submission deadline May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d40ca435-765b-4375-bab8-33e92ab70270",
  "isSidechain": false,
  "requestId": "req_011CawiapE3mFAFs6v88i8GG",
  "type": "assistant",
  "uuid": "fb93686b-44da-4a16-8b80-8856fa97ed70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuBNu6W7BrrDhzMgHyp6NT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 685,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 41924,
      "output_tokens": 400,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2021,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 685,
          "output_tokens": 400,
          "cache_read_input_tokens": 41924,
          "cache_creation_input_tokens": 2021,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2021
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

_source line 35 · 2026-05-12T00:20:41.047Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019VsNBySGxhodDK4EVAucqv`</summary>

```json
{
  "query": "\"adaptive retrieval\" \"code repair\" OR \"program repair\" configuration routing 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb93686b-44da-4a16-8b80-8856fa97ed70",
  "isSidechain": false,
  "requestId": "req_011CawiapE3mFAFs6v88i8GG",
  "type": "assistant",
  "uuid": "cb7a0af8-1214-491f-9b62-bb503a649e1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuBNu6W7BrrDhzMgHyp6NT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 685,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 41924,
      "output_tokens": 400,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2021,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 685,
          "output_tokens": 400,
          "cache_read_input_tokens": 41924,
          "cache_creation_input_tokens": 2021,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2021
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

_source line 36 · 2026-05-12T00:20:41.675Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AEqkHzuj8nKDQFS7a2SFij`</summary>

```json
{
  "query": "Qwen3-Coder-Next API pricing cost per instance 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb7a0af8-1214-491f-9b62-bb503a649e1e",
  "isSidechain": false,
  "requestId": "req_011CawiapE3mFAFs6v88i8GG",
  "type": "assistant",
  "uuid": "ee31bf39-2a6d-47ea-a615-f0632ed4c4b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HuBNu6W7BrrDhzMgHyp6NT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 685,
      "cache_creation_input_tokens": 2021,
      "cache_read_input_tokens": 41924,
      "output_tokens": 400,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2021,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 685,
          "output_tokens": 400,
          "cache_read_input_tokens": 41924,
          "cache_creation_input_tokens": 2021,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2021
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

_source line 37 · 2026-05-12T00:20:44.240Z_

<details><summary>↩ Tool result · `toolu_01CkAKzQTNoaSTwPn9G8iXQe`</summary>

```text
Web search results for query: "EMNLP 2026 ARR submission deadline May 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here's the information about the EMNLP 2026 ARR submission deadline:

The ARR submission deadline for EMNLP 2026 is May 25, 2026.

Additional important deadlines and details:

- Reviewer registration deadline for ALL authors is May 27, 2026
- Author response and author-reviewer discussion takes place July 7 - July 13, 2026
- Meta review is released July 30, 2026
- The EMNLP commitment deadline is August 2, 2026

It's also worth noting that since the ARR 2026 May cycle is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb93686b-44da-4a16-8b80-8856fa97ed70",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "b3a7286c-84f5-4ac2-9b24-ae6549d92d3c",
  "toolUseResult": {
    "query": "EMNLP 2026 ARR submission deadline May 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AbTtSbPAvwJfDxUfA1tJhr",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "Dates and Venues",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X",
            "url": "https://x.com/emnlpmeeting/status/2029508292637061462"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "EMNLP 2026 (@emnlpmeeting) / Posts / X",
            "url": "https://x.com/emnlpmeeting?lang=en"
          },
          {
            "title": "emnlp 2026 - AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/conference/?id=emnlp26"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X",
            "url": "https://x.com/emnlpmeeting/status/2047754845919031450"
          }
        ]
      },
      "Based on the search results, here's the information about the EMNLP 2026 ARR submission deadline:\n\nThe ARR submission deadline for EMNLP 2026 is May 25, 2026.\n\nAdditional important deadlines and details:\n\n- Reviewer registration deadline for ALL authors is May 27, 2026\n- Author response and author-reviewer discussion takes place July 7 - July 13, 2026\n- Meta review is released July 30, 2026\n- The EMNLP commitment deadline is August 2, 2026\n\nIt's also worth noting that since the ARR 2026 May cycle is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time, and this choice will be binding for EMNLP 2026."
    ],
    "durationSeconds": 3.7185499300000084
  },
  "sourceToolAssistantUUID": "fb93686b-44da-4a16-8b80-8856fa97ed70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-12T00:20:45.825Z_

<details><summary>↩ Tool result · `toolu_01AEqkHzuj8nKDQFS7a2SFij`</summary>

```text
Web search results for query: "Qwen3-Coder-Next API pricing cost per instance 2026"

Links: [{"title":"Qwen3 Coder Next API Pricing 2026 - Costs, Performance & Providers","url":"https://pricepertoken.com/pricing-page/model/qwen-qwen3-coder-next"},{"title":"Qwen3 Coder Next - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/qwen/qwen3-coder-next"},{"title":"Qwen API Pricing Guide 2026: Max Performance on a Budget","url":"https://deepinfra.com/blog/qwen-api-pricing-2026-guide"},{"title":"Qwen API Pricing (Updated 2026) – All Models & Token Costs","url":"https://pricepertoken.com/pricing-page/provider/qwen"},{"title":"Qwen3.6 Plus - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/qwen/qwen3.6-plus"},{"title":"Qwen3 Coder 480B A35B (exacto) API Pricing 2026 - Costs, Performance & Providers","url":"https://pricepertoken.com/pricing-page/model/qwen-qwen3-coder"},{"title":"Qwen3 Coder Next pricing & specs — Alibaba | CloudPrice","url":"https://cloudprice.net/models/alibaba-qwen3-coder-next"},{"title":"Qwen: Qwen3 Coder Next in Kilo Code — Benchmarks, Pricing & How to Use","url":"https://kilo.ai/models/qwen3-coder-next"},{"title":"Qwen3 Coder Plus API Pricing 2026 - Costs, Performance & Providers","url":"https://pricepertoken.com/pricing-page/model/qwen-qwen3-coder-plus"},{"title":"Alibaba Cloud Model Studio model pricing - Alibaba Cloud Model Studio - Alibaba Cloud Documentation Center","url":"https://www.alibabacloud.com/help/en/model-studio/model-pricing"}]

Based on the search results, here's the pricing information for Qwen3-Coder-Next API in 2026:

Pricing starts at $0.110 per million input tokens and $0.800 per million output tokens. Qwen3 Coder Next was released on February 4, 2026.

The model supports a context window of up to 262K tokens. Cache read pricing is $0.07 per 1M tokens.

For reference, analyzing a 10,000 line codebase (≈40k input tokens, 10k output tokens) costs approximately $0.0124.

Note: The pricing shown is per token usage, not "per instance" - the model operates on a token-based pricing model rather than instance-based billing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee31bf39-2a6d-47ea-a615-f0632ed4c4b7",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "b7eb9cde-d444-4593-b6e2-05bfbd084bdf",
  "toolUseResult": {
    "query": "Qwen3-Coder-Next API pricing cost per instance 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LNyDW3SdXYpEwr2jL1cssw",
        "content": [
          {
            "title": "Qwen3 Coder Next API Pricing 2026 - Costs, Performance & Providers",
            "url": "https://pricepertoken.com/pricing-page/model/qwen-qwen3-coder-next"
          },
          {
            "title": "Qwen3 Coder Next - API Pricing & Benchmarks | OpenRouter",
            "url": "https://openrouter.ai/qwen/qwen3-coder-next"
          },
          {
            "title": "Qwen API Pricing Guide 2026: Max Performance on a Budget",
            "url": "https://deepinfra.com/blog/qwen-api-pricing-2026-guide"
          },
          {
            "title": "Qwen API Pricing (Updated 2026) – All Models & Token Costs",
            "url": "https://pricepertoken.com/pricing-page/provider/qwen"
          },
          {
            "title": "Qwen3.6 Plus - API Pricing & Benchmarks | OpenRouter",
            "url": "https://openrouter.ai/qwen/qwen3.6-plus"
          },
          {
            "title": "Qwen3 Coder 480B A35B (exacto) API Pricing 2026 - Costs, Performance & Providers",
            "url": "https://pricepertoken.com/pricing-page/model/qwen-qwen3-coder"
          },
          {
            "title": "Qwen3 Coder Next pricing & specs — Alibaba | CloudPrice",
            "url": "https://cloudprice.net/models/alibaba-qwen3-coder-next"
          },
          {
            "title": "Qwen: Qwen3 Coder Next in Kilo Code — Benchmarks, Pricing & How to Use",
            "url": "https://kilo.ai/models/qwen3-coder-next"
          },
          {
            "title": "Qwen3 Coder Plus API Pricing 2026 - Costs, Performance & Providers",
            "url": "https://pricepertoken.com/pricing-page/model/qwen-qwen3-coder-plus"
          },
          {
            "title": "Alibaba Cloud Model Studio model pricing - Alibaba Cloud Model Studio - Alibaba Cloud Documentation Center",
            "url": "https://www.alibabacloud.com/help/en/model-studio/model-pricing"
          }
        ]
      },
      "Based on the search results, here's the pricing information for Qwen3-Coder-Next API in 2026:\n\nPricing starts at $0.110 per million input tokens and $0.800 per million output tokens. Qwen3 Coder Next was released on February 4, 2026.\n\nThe model supports a context window of up to 262K tokens. Cache read pricing is $0.07 per 1M tokens.\n\nFor reference, analyzing a 10,000 line codebase (≈40k input tokens, 10k output tokens) costs approximately $0.0124.\n\nNote: The pricing shown is per token usage, not \"per instance\" - the model operates on a token-based pricing model rather than instance-based billing."
    ],
    "durationSeconds": 4.148200626999999
  },
  "sourceToolAssistantUUID": "ee31bf39-2a6d-47ea-a615-f0632ed4c4b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-12T00:20:48.932Z_

<details><summary>↩ Tool result · `toolu_019VsNBySGxhodDK4EVAucqv`</summary>

```text
Web search results for query: ""adaptive retrieval" "code repair" OR "program repair" configuration routing 2026 arxiv"

Links: [{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement","url":"https://arxiv.org/html/2601.08545.pdf"},{"title":"RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE","url":"https://arxiv.org/pdf/2509.16701"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Less is More: Adaptive Program Repair with Bug Localization and Preference Learning","url":"https://arxiv.org/html/2503.06510"},{"title":"Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback","url":"https://arxiv.org/html/2601.00509v1"},{"title":"ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11219-025-09728-1"},{"title":"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation","url":"https://arxiv.org/html/2509.02330v1"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"}]

I found several relevant arxiv papers related to your search query on adaptive retrieval, code repair, and program repair. Here are the key findings:

## Recent Research Papers (2025-2026)

ARISE is a repository-level approach that scales fault localization by combining agents with static analysis tools, published in May 2026. Recent reasoning-guided approaches generate structured, bug-specific explanations before ranking candidate locations, demonstrating that prompting the model to reason about why a location is relevant improves accuracy over purely similarity-based retrieval.

AdaPR (Adaptive Program Repair) is a novel task with a two-stage approach called AdaPatcher (Adaptive Patch Generator) to enhance program repair while maintaining consistency, from March 2025.

ReCode is a fine-grained retrieval-augmented generation framework that leverages modular code representations and an algorithm-aware retrieval strategy to enhance automated code repair, published in September 2025.

## Configuration and Routing Patterns

Some approaches adaptively adjust parameters (α and β) based on their contributions toward minimizing the gap between current similarity and a predefined target similarity, where structural similarity's role determines parameter adjustment.

Recent LLM-based APR systems published from January 2022 to June 2025 are categorized into four paradigms, showing how retrieval- or analysis-augmented contexts strengthen any of them.

Future work will need more selective retrieval, adaptive compression, and context-aware parameter-efficient fine-tuning strategies to retain the benefits of additional signals without compromising scalability or robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb7a0af8-1214-491f-9b62-bb503a649e1e",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "570f5bf2-acaa-4095-bece-0442e34cd33c",
  "toolUseResult": {
    "query": "\"adaptive retrieval\" \"code repair\" OR \"program repair\" configuration routing 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01982sjSJeSaL3KK2pPDNBco",
        "content": [
          {
            "title": "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/html/2605.03117"
          },
          {
            "title": "Learner-Tailored Program Repair: A Solution Generator with Iterative Edit-Driven Retrieval Enhancement",
            "url": "https://arxiv.org/html/2601.08545.pdf"
          },
          {
            "title": "RELREPAIR: ENHANCING AUTOMATED PROGRAM REPAIR BY RETRIEVING RELEVANT CODE",
            "url": "https://arxiv.org/pdf/2509.16701"
          },
          {
            "title": "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications",
            "url": "https://arxiv.org/html/2506.23749v1"
          },
          {
            "title": "Less is More: Adaptive Program Repair with Bug Localization and Preference Learning",
            "url": "https://arxiv.org/html/2503.06510"
          },
          {
            "title": "Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback",
            "url": "https://arxiv.org/html/2601.00509v1"
          },
          {
            "title": "ReAPR: Automatic program repair via retrieval-augmented large language models | Software Quality Journal | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11219-025-09728-1"
          },
          {
            "title": "ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2509.02330v1"
          },
          {
            "title": "GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub",
            "url": "https://github.com/iSEngLab/AwesomeLLM4APR"
          },
          {
            "title": "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/html/2510.04905v1"
          }
        ]
      },
      "I found several relevant arxiv papers related to your search query on adaptive retrieval, code repair, and program repair. Here are the key findings:\n\n## Recent Research Papers (2025-2026)\n\nARISE is a repository-level approach that scales fault localization by combining agents with static analysis tools, published in May 2026. Recent reasoning-guided approaches generate structured, bug-specific explanations before ranking candidate locations, demonstrating that prompting the model to reason about why a location is relevant improves accuracy over purely similarity-based retrieval.\n\nAdaPR (Adaptive Program Repair) is a novel task with a two-stage approach called AdaPatcher (Adaptive Patch Generator) to enhance program repair while maintaining consistency, from March 2025.\n\nReCode is a fine-grained retrieval-augmented generation framework that leverages modular code representations and an algorithm-aware retrieval strategy to enhance automated code repair, published in September 2025.\n\n## Configuration and Routing Patterns\n\nSome approaches adaptively adjust parameters (α and β) based on their contributions toward minimizing the gap between current similarity and a predefined target similarity, where structural similarity's role determines parameter adjustment.\n\nRecent LLM-based APR systems published from January 2022 to June 2025 are categorized into four paradigms, showing how retrieval- or analysis-augmented contexts strengthen any of them.\n\nFuture work will need more selective retrieval, adaptive compression, and context-aware parameter-efficient fine-tuning strategies to retain the benefits of additional signals without compromising scalability or robustness."
    ],
    "durationSeconds": 7.882332084999987
  },
  "sourceToolAssistantUUID": "cb7a0af8-1214-491f-9b62-bb503a649e1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-12T00:21:02.076Z_

<details><summary>Logged reasoning block</summary>

```text
Key findings:
1. EMNLP 2026 ARR deadline is indeed May 25, 2026 — confirmed.
2. No new competing work on adaptive retrieval configuration routing for code repair that the proposal hasn't already cited.
3. Qwen3-Coder-Next pricing: $0.11/M input, $0.80/M output. The proposal claims ~$0.08/instance. Let me check if this is reasonable. A typical SWE-bench instance would involve maybe ~50K input tokens and ~5K output tokens. That would be: 50K * $0.11/M + 5K * $0.80/M = $0.0055 + $0.004 = ~$0.01 per instance. 

But when I factor in the full Agentless pipeline with multiple localization rounds, repair attempts, and test generation steps, the cumulative LLM costs across all those stages could plausibly reach $0.08 per complete run. I should verify a few more details to be sure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "570f5bf2-acaa-4095-bece-0442e34cd33c",
  "isSidechain": false,
  "requestId": "req_011CawicAy1ATF3JPKX8Rje4",
  "type": "assistant",
  "uuid": "cd1e38f2-881f-4c4d-ac1c-bf8a0785511c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2UkpxVePjThUJbsWPKGHh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 764,
      "cache_creation_input_tokens": 2863,
      "cache_read_input_tokens": 43945,
      "output_tokens": 433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2863,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 764,
          "output_tokens": 433,
          "cache_read_input_tokens": 43945,
          "cache_creation_input_tokens": 2863,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2863
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

_source line 41 · 2026-05-12T00:21:02.079Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NQHr4bWSN9WSYvRypuhX7R`</summary>

```json
{
  "query": "CodeSage code encoder model 2024 ICLR huggingface availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd1e38f2-881f-4c4d-ac1c-bf8a0785511c",
  "isSidechain": false,
  "requestId": "req_011CawicAy1ATF3JPKX8Rje4",
  "type": "assistant",
  "uuid": "9578c1b1-3844-4d47-a070-d59d0ffc43f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2UkpxVePjThUJbsWPKGHh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 764,
      "cache_creation_input_tokens": 2863,
      "cache_read_input_tokens": 43945,
      "output_tokens": 433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2863,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 764,
          "output_tokens": 433,
          "cache_read_input_tokens": 43945,
          "cache_creation_input_tokens": 2863,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2863
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

_source line 42 · 2026-05-12T00:21:02.258Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FxeUaV1nxQmg6dJ1gjUeTw`</summary>

```json
{
  "query": "\"granularity routing\" OR \"granularity selection\" \"code\" OR \"program\" adaptive per-instance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9578c1b1-3844-4d47-a070-d59d0ffc43f4",
  "isSidechain": false,
  "requestId": "req_011CawicAy1ATF3JPKX8Rje4",
  "type": "assistant",
  "uuid": "2482a632-a1a2-4670-a2ac-78238fb480e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2UkpxVePjThUJbsWPKGHh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 764,
      "cache_creation_input_tokens": 2863,
      "cache_read_input_tokens": 43945,
      "output_tokens": 433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2863,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 764,
          "output_tokens": 433,
          "cache_read_input_tokens": 43945,
          "cache_creation_input_tokens": 2863,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2863
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

_source line 43 · 2026-05-12T00:21:08.559Z_

<details><summary>↩ Tool result · `toolu_01NQHr4bWSN9WSYvRypuhX7R`</summary>

```text
Web search results for query: "CodeSage code encoder model 2024 ICLR huggingface availability"

Links: [{"title":"codesage/codesage-large · Hugging Face","url":"https://huggingface.co/codesage/codesage-large"},{"title":"codesage/codesage-large-v2 · Hugging Face","url":"https://huggingface.co/codesage/codesage-large-v2"},{"title":"GitHub - amazon-science/CodeSage: CodeSage: Code Representation Learning At Scale (ICLR 2024) · GitHub","url":"https://github.com/amazon-science/CodeSage"},{"title":"codesage/codesage-small-v2 · Hugging Face","url":"https://huggingface.co/codesage/codesage-small-v2"},{"title":"codesage/codesage-base · Hugging Face","url":"https://huggingface.co/codesage/codesage-base"},{"title":"codesage/codesage-base-v2 · Hugging Face","url":"https://huggingface.co/codesage/codesage-base-v2"},{"title":"codesage/codesage-small · Hugging Face","url":"https://huggingface.co/codesage/codesage-small"},{"title":"CodeSage/README.md at main · amazon-science/CodeSage","url":"https://github.com/amazon-science/CodeSage/blob/main/README.md"},{"title":"Code Representation Learning At Scale - Academic Homepage","url":"https://wasiahmad.github.io/publications/41_codesage/"},{"title":"codesage (CodeSage)","url":"https://huggingface.co/codesage/models"}]

Based on the search results, here's what I found about CodeSage:

## Overview
CodeSage is a new family of open code embedding models with an encoder architecture that support a wide range of source code understanding tasks. It is from the ICLR 2024 paper "CodeSage: Code Representation Learning At Scale" by Dejiao Zhang, Wasi Uddin Ahmad, Ming Tan, Hantian Ding, Ramesh Nallapati, Dan Roth, Xiaofei Ma, and Bing Xiang.

## HuggingFace Availability
The CodeSage models are actively available on HuggingFace. Multiple versions are available:

**V1 Models:**
- codesage-small: 130M encoder model with 1024 dimension embeddings
- codesage-base: 356M encoder model with 1024 dimension embeddings
- codesage-large: 1.3B encoder model with 1024 dimension embeddings

**V2 Models (Enhanced versions):**
The V2 models enhanced semantic search performance by improving the quality of the contrastive learning data through consistency filtering. These are available as codesage-small-v2, codesage-base-v2, and codesage-large-v2.

## Key Features
- Supported languages (9 in total) are: c, c-sharp, go, java, javascript, typescript, php, python, ruby.
- As of 11/2024, you can now access CodeSage models through SentenceTransformer.
- CodeSage has been trained with block-attention and requires appending the EOS token at the end of each sequence to ensure good performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9578c1b1-3844-4d47-a070-d59d0ffc43f4",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "117601e7-4c0c-428b-a74a-c47f173c457c",
  "toolUseResult": {
    "query": "CodeSage code encoder model 2024 ICLR huggingface availability",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V3gYcBeMR9DyYQUwANBy5a",
        "content": [
          {
            "title": "codesage/codesage-large · Hugging Face",
            "url": "https://huggingface.co/codesage/codesage-large"
          },
          {
            "title": "codesage/codesage-large-v2 · Hugging Face",
            "url": "https://huggingface.co/codesage/codesage-large-v2"
          },
          {
            "title": "GitHub - amazon-science/CodeSage: CodeSage: Code Representation Learning At Scale (ICLR 2024) · GitHub",
            "url": "https://github.com/amazon-science/CodeSage"
          },
          {
            "title": "codesage/codesage-small-v2 · Hugging Face",
            "url": "https://huggingface.co/codesage/codesage-small-v2"
          },
          {
            "title": "codesage/codesage-base · Hugging Face",
            "url": "https://huggingface.co/codesage/codesage-base"
          },
          {
            "title": "codesage/codesage-base-v2 · Hugging Face",
            "url": "https://huggingface.co/codesage/codesage-base-v2"
          },
          {
            "title": "codesage/codesage-small · Hugging Face",
            "url": "https://huggingface.co/codesage/codesage-small"
          },
          {
            "title": "CodeSage/README.md at main · amazon-science/CodeSage",
            "url": "https://github.com/amazon-science/CodeSage/blob/main/README.md"
          },
          {
            "title": "Code Representation Learning At Scale - Academic Homepage",
            "url": "https://wasiahmad.github.io/publications/41_codesage/"
          },
          {
            "title": "codesage (CodeSage)",
            "url": "https://huggingface.co/codesage/models"
          }
        ]
      },
      "Based on the search results, here's what I found about CodeSage:\n\n## Overview\nCodeSage is a new family of open code embedding models with an encoder architecture that support a wide range of source code understanding tasks. It is from the ICLR 2024 paper \"CodeSage: Code Representation Learning At Scale\" by Dejiao Zhang, Wasi Uddin Ahmad, Ming Tan, Hantian Ding, Ramesh Nallapati, Dan Roth, Xiaofei Ma, and Bing Xiang.\n\n## HuggingFace Availability\nThe CodeSage models are actively available on HuggingFace. Multiple versions are available:\n\n**V1 Models:**\n- codesage-small: 130M encoder model with 1024 dimension embeddings\n- codesage-base: 356M encoder model with 1024 dimension embeddings\n- codesage-large: 1.3B encoder model with 1024 dimension embeddings\n\n**V2 Models (Enhanced versions):**\nThe V2 models enhanced semantic search performance by improving the quality of the contrastive learning data through consistency filtering. These are available as codesage-small-v2, codesage-base-v2, and codesage-large-v2.\n\n## Key Features\n- Supported languages (9 in total) are: c, c-sharp, go, java, javascript, typescript, php, python, ruby.\n- As of 11/2024, you can now access CodeSage models through SentenceTransformer.\n- CodeSage has been trained with block-attention and requires appending the EOS token at the end of each sequence to ensure good performance."
    ],
    "durationSeconds": 6.473200719
  },
  "sourceToolAssistantUUID": "9578c1b1-3844-4d47-a070-d59d0ffc43f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "117601e7-4c0c-428b-a74a-c47f173c457c",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive context routing for code repair",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Tool result

_source line 46 · 2026-05-12T00:21:10.445Z_

<details><summary>↩ Tool result · `toolu_01FxeUaV1nxQmg6dJ1gjUeTw`</summary>

```text
Web search results for query: ""granularity routing" OR "granularity selection" "code" OR "program" adaptive per-instance 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/b23c35b1c6696c4e4fa1a8dd1059ec7c669a704b.pdf"},{"title":"Granularity Control Mechanism","url":"https://www.emergentmind.com/topics/granularity-control-mechanism"},{"title":"Dual-Granularity Semantic Guided Sparse Routing Diffusion Model for General","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Xing_Dual-Granularity_Semantic_Guided_Sparse_Routing_Diffusion_Model_for_General_Pansharpening_CVPR_2025_paper.pdf"},{"title":"A Comprehensive Benchmark for Routing LLMs to Explore ...","url":"https://aclanthology.org/2025.findings-emnlp.208.pdf"},{"title":"Research on Computer Network Routing Based on Granular Computational Intelligence | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel7/10420831/10420858/10421390.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf"},{"title":"Towards Multi-Granularity Memory Association and Selection for Long-Term Conversational Agents","url":"https://arxiv.org/html/2505.19549v1"},{"title":"RECODE: UNIFY PLAN AND ACTION FOR UNIVERSAL GRANULARITY CONTROL","url":"https://www.arxiv.org/pdf/2510.23564"},{"title":"Optimal granularity selection based on algorithm stability with application to attribute reduction in rough set theory - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0020025523014305"},{"title":"Multi-Dimensional Resources Management with GNN for Adaptive Routing Optimization - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12987051/"}]

I've completed the web search for your query about granularity routing, granularity selection, code, programs, adaptive per-instance approaches from 2025-2026. Here are the key findings:

## Recent Research Findings (2025-2026)

### Memory and Retrieval Systems

A framework called MemGAS proposes an entropy-based router that adaptively selects granularity for multi-granularity memory retrieval in conversational agents. Existing methods rely on single predefined granularity for memory retrieval, limiting their ability to adaptively prioritize fine- or coarse-grained information based on query.

### Code Generation and Planning

ReCode unifies all decision granularities—abstract plans and primitive actions—by recursively decomposing placeholder functions down to environmental primitives within a single code-generation paradigm, with model-determined recursion depth (granularity) at inference. Achieving adaptive intelligence is a primary goal for LLM-based agents, yet current frameworks fall short because they operate at fixed granularities, as existing approaches explicitly separate planning from action into distinct decision-making processes.

### Graph-Based Interpretability

An adaptive routing module dynamically identifies the most informative root-to-leaf paths, providing both final prediction and multi-granular interpretability of the decision-making in tree-structured graph neural networks.

### General Granularity Control Challenges

In many systems, granularity selection is externally initiated rather than learned or adaptively inferred; automatic granularity selection from task context remains largely unaddressed.

These recent publications demonstrate active research interest in adaptive, per-instance granularity selection across code generation, memory systems, and machine learning models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2482a632-a1a2-4670-a2ac-78238fb480e9",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "3fed354d-15be-43ba-ad38-059f968527ad",
  "toolUseResult": {
    "query": "\"granularity routing\" OR \"granularity selection\" \"code\" OR \"program\" adaptive per-instance 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VPzWnB2oaAMk8uKPBYYGCa",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf/b23c35b1c6696c4e4fa1a8dd1059ec7c669a704b.pdf"
          },
          {
            "title": "Granularity Control Mechanism",
            "url": "https://www.emergentmind.com/topics/granularity-control-mechanism"
          },
          {
            "title": "Dual-Granularity Semantic Guided Sparse Routing Diffusion Model for General",
            "url": "https://openaccess.thecvf.com/content/CVPR2025/papers/Xing_Dual-Granularity_Semantic_Guided_Sparse_Routing_Diffusion_Model_for_General_Pansharpening_CVPR_2025_paper.pdf"
          },
          {
            "title": "A Comprehensive Benchmark for Routing LLMs to Explore ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.208.pdf"
          },
          {
            "title": "Research on Computer Network Routing Based on Granular Computational Intelligence | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/iel7/10420831/10420858/10421390.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/46a126492ea6fb87410e55a58df2e189-Paper-Conference.pdf"
          },
          {
            "title": "Towards Multi-Granularity Memory Association and Selection for Long-Term Conversational Agents",
            "url": "https://arxiv.org/html/2505.19549v1"
          },
          {
            "title": "RECODE: UNIFY PLAN AND ACTION FOR UNIVERSAL GRANULARITY CONTROL",
            "url": "https://www.arxiv.org/pdf/2510.23564"
          },
          {
            "title": "Optimal granularity selection based on algorithm stability with application to attribute reduction in rough set theory - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0020025523014305"
          },
          {
            "title": "Multi-Dimensional Resources Management with GNN for Adaptive Routing Optimization - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12987051/"
          }
        ]
      },
      "I've completed the web search for your query about granularity routing, granularity selection, code, programs, adaptive per-instance approaches from 2025-2026. Here are the key findings:\n\n## Recent Research Findings (2025-2026)\n\n### Memory and Retrieval Systems\n\nA framework called MemGAS proposes an entropy-based router that adaptively selects granularity for multi-granularity memory retrieval in conversational agents. Existing methods rely on single predefined granularity for memory retrieval, limiting their ability to adaptively prioritize fine- or coarse-grained information based on query.\n\n### Code Generation and Planning\n\nReCode unifies all decision granularities—abstract plans and primitive actions—by recursively decomposing placeholder functions down to environmental primitives within a single code-generation paradigm, with model-determined recursion depth (granularity) at inference. Achieving adaptive intelligence is a primary goal for LLM-based agents, yet current frameworks fall short because they operate at fixed granularities, as existing approaches explicitly separate planning from action into distinct decision-making processes.\n\n### Graph-Based Interpretability\n\nAn adaptive routing module dynamically identifies the most informative root-to-leaf paths, providing both final prediction and multi-granular interpretability of the decision-making in tree-structured graph neural networks.\n\n### General Granularity Control Challenges\n\nIn many systems, granularity selection is externally initiated rather than learned or adaptively inferred; automatic granularity selection from task context remains largely unaddressed.\n\nThese recent publications demonstrate active research interest in adaptive, per-instance granularity selection across code generation, memory systems, and machine learning models."
    ],
    "durationSeconds": 8.183625379999997
  },
  "sourceToolAssistantUUID": "2482a632-a1a2-4670-a2ac-78238fb480e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-12T00:21:19.653Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for a few more things to complete my review:

1. Check if SeleCom (arXiv 2602.15856) actually says what's claimed about "selection and compression are complementary"
2. Check the Devlo claim (70.2%) - is this outdated?
3. Check if there's an important paper on "What to Retrieve for Effective Retrieval-Augmented Code Generation" (arXiv 2503.20589) that might be relevant but is not cited

Let me also check one more thing - the claim about Holloway et al. 

's work at NeurIPS 2024.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fed354d-15be-43ba-ad38-059f968527ad",
  "isSidechain": false,
  "requestId": "req_011CawidkxS2K7xjCiYLiusx",
  "type": "assistant",
  "uuid": "cd6f5456-b29f-4bec-8ba9-dbfdf0feeb5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBqCpoCiigMAshVJLgGPFg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3109,
      "cache_read_input_tokens": 46808,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 46808,
          "cache_creation_input_tokens": 3109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3109
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

_source line 48 · 2026-05-12T00:21:19.692Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xm3fG4tD6hVCyKKhuAogZ7`</summary>

```json
{
  "query": "Holloway Elenberg \"context granularity\" \"program repair\" NeurIPS 2024 workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd6f5456-b29f-4bec-8ba9-dbfdf0feeb5f",
  "isSidechain": false,
  "requestId": "req_011CawidkxS2K7xjCiYLiusx",
  "type": "assistant",
  "uuid": "bdba894c-a17b-4528-b87c-8a65f31d9392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBqCpoCiigMAshVJLgGPFg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3109,
      "cache_read_input_tokens": 46808,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 46808,
          "cache_creation_input_tokens": 3109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3109
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

_source line 49 · 2026-05-12T00:21:20.356Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CJPV3q1Be3ntQ5kQoCQiDG`</summary>

```json
{
  "query": "\"What to Retrieve for Effective Retrieval-Augmented Code Generation\" arxiv 2503 empirical study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdba894c-a17b-4528-b87c-8a65f31d9392",
  "isSidechain": false,
  "requestId": "req_011CawidkxS2K7xjCiYLiusx",
  "type": "assistant",
  "uuid": "38bc1bfa-f1e9-4efa-9940-d90de69a8bbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBqCpoCiigMAshVJLgGPFg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3109,
      "cache_read_input_tokens": 46808,
      "output_tokens": 294,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3109,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 294,
          "cache_read_input_tokens": 46808,
          "cache_creation_input_tokens": 3109,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3109
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

_source line 50 · 2026-05-12T00:21:23.440Z_

<details><summary>↩ Tool result · `toolu_01Xm3fG4tD6hVCyKKhuAogZ7`</summary>

```text
Web search results for query: "Holloway Elenberg "context granularity" "program repair" NeurIPS 2024 workshop"

Links: [{"title":"NeurIPS On the Role of Context Granularity in LLM-Driven Program Repair","url":"https://neurips.cc/virtual/2024/103609"},{"title":"On the Role of Context Granularity in LLM-Driven Program Repair Tyler Holloway∗","url":"https://mlforsystems.org/assets/papers/neurips2024/paper23.pdf"},{"title":"Ethan R. Elenberg","url":"https://eelenberg.github.io/"},{"title":"NeurIPS 2024 Workshop | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc/2024/Workshop"},{"title":"Announcing the NeurIPS 2024 Workshops – NeurIPS Blog","url":"https://blog.neurips.cc/2024/08/02/announcing-the-neurips-2024-workshops/"},{"title":"NeurIPS 2024","url":"https://sites.google.com/view/neurips2024-ftw/home"},{"title":"NeurIPS 2026","url":"https://neurips.cc/"},{"title":"NeurIPS 2024 Workshop on Large Foundation Models for Educational Assessment","url":"https://neurips2024edu.github.io/"},{"title":"The Fourth Workshop on Efficient Natural Language and Speech Processing (ENLSP-IV): Highlighting New Architectures for Future Foundation Models","url":"https://neurips.cc/virtual/2024/workshop/84731"},{"title":"NeurIPS 2024","url":"https://joltml.com/neurips-2024/"}]

Based on the search results, I found the paper you're looking for. Tyler Holloway and Ethan R. Elenberg presented "On the Role of Context Granularity in LLM-Driven Program Repair" at the NeurIPS Workshop on Machine Learning for Systems in 2024.

The paper proposes a novel context granularity based on backward static slicing, capturing lines on which the buggy line is data- and control-dependent. They evaluate its performance against five commonly used APR (Automated Program Repair) context granularities as well as state-of-the-art APR systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdba894c-a17b-4528-b87c-8a65f31d9392",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "69898df1-0046-48c4-979b-1185a74e8596",
  "toolUseResult": {
    "query": "Holloway Elenberg \"context granularity\" \"program repair\" NeurIPS 2024 workshop",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L5skiUDeKbzmeq8NUADi1E",
        "content": [
          {
            "title": "NeurIPS On the Role of Context Granularity in LLM-Driven Program Repair",
            "url": "https://neurips.cc/virtual/2024/103609"
          },
          {
            "title": "On the Role of Context Granularity in LLM-Driven Program Repair Tyler Holloway∗",
            "url": "https://mlforsystems.org/assets/papers/neurips2024/paper23.pdf"
          },
          {
            "title": "Ethan R. Elenberg",
            "url": "https://eelenberg.github.io/"
          },
          {
            "title": "NeurIPS 2024 Workshop | OpenReview",
            "url": "https://openreview.net/group?id=NeurIPS.cc/2024/Workshop"
          },
          {
            "title": "Announcing the NeurIPS 2024 Workshops – NeurIPS Blog",
            "url": "https://blog.neurips.cc/2024/08/02/announcing-the-neurips-2024-workshops/"
          },
          {
            "title": "NeurIPS 2024",
            "url": "https://sites.google.com/view/neurips2024-ftw/home"
          },
          {
            "title": "NeurIPS 2026",
            "url": "https://neurips.cc/"
          },
          {
            "title": "NeurIPS 2024 Workshop on Large Foundation Models for Educational Assessment",
            "url": "https://neurips2024edu.github.io/"
          },
          {
            "title": "The Fourth Workshop on Efficient Natural Language and Speech Processing (ENLSP-IV): Highlighting New Architectures for Future Foundation Models",
            "url": "https://neurips.cc/virtual/2024/workshop/84731"
          },
          {
            "title": "NeurIPS 2024",
            "url": "https://joltml.com/neurips-2024/"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Tyler Holloway and Ethan R. Elenberg presented \"On the Role of Context Granularity in LLM-Driven Program Repair\" at the NeurIPS Workshop on Machine Learning for Systems in 2024.\n\nThe paper proposes a novel context granularity based on backward static slicing, capturing lines on which the buggy line is data- and control-dependent. They evaluate its performance against five commonly used APR (Automated Program Repair) context granularities as well as state-of-the-art APR systems."
    ],
    "durationSeconds": 3.7440528480000212
  },
  "sourceToolAssistantUUID": "bdba894c-a17b-4528-b87c-8a65f31d9392",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-12T00:21:29.840Z_

<details><summary>↩ Tool result · `toolu_01CJPV3q1Be3ntQ5kQoCQiDG`</summary>

```text
Web search results for query: ""What to Retrieve for Effective Retrieval-Augmented Code Generation" arxiv 2503 empirical study"

Links: [{"title":"[2503.20589] What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond","url":"https://arxiv.org/abs/2503.20589"},{"title":"What to Retrieve for Effective Retrieval-Augmented Code ...","url":"https://arxiv.org/pdf/2503.20589"},{"title":"What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond | alphaXiv","url":"https://www.alphaxiv.org/overview/2503.20589v1"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond | Space Frontiers","url":"https://spacefrontiers.org/r/10.48550/arxiv.2503.20589"},{"title":"Retrieval-Augmented Generation with Hierarchical Knowledge","url":"https://arxiv.org/html/2503.10150v1"},{"title":"What Truly Matters? An Empirical Study on the Effectiveness of Retrieved Information in Retrieval-Augmented Code Generation","url":"https://arxiv.org/html/2503.20589"},{"title":"When LLMs Meet API Documentation: Can Retrieval Augmentation Aid Code Generation Just as It Helps Developers?","url":"https://arxiv.org/html/2503.15231v1"},{"title":"DeepRetrieval: Powerful Query Generation for Information Retrieval with Reinforcement Learning","url":"https://arxiv.org/html/2503.00223v1"}]

I found the paper you're looking for! Here's information about the arxiv 2503 empirical study on retrieval-augmented code generation:

## "What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond"

**ArXiv ID:** 2503.20589 (Published March 26, 2025)

**Key Findings:**

Through an empirical study on two benchmarks, the paper demonstrates that in-context code and potential API information significantly enhance LLM performance, whereas retrieved similar code often introduces noise, degrading results by up to 15%.

**Proposed Solution:**

Based on the preliminary results, the authors propose AllianceCoder, a novel context-integrated method that employs chain-of-thought prompting to decompose user queries into implementation steps and retrieves APIs via semantic description matching.

**Problem Context:**

Repository-level code generation remains challenging due to complex code dependencies and the limitations of large language models (LLMs) in processing long contexts. While retrieval-augmented generation (RAG) frameworks are widely adopted, the effectiveness of different retrieved information sources—contextual code, APIs, and similar snippets—has not been rigorously analyzed.

**Performance:**

Through extensive experiments on CoderEval and RepoExec, AllianceCoder achieves state-of-the-art performance, improving Pass@1 by up to 20%.

You can access the full paper at: https://arxiv.org/abs/2503.20589


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38bc1bfa-f1e9-4efa-9940-d90de69a8bbe",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "7c324f47-049d-46c7-b699-e1bd9e2c69db",
  "toolUseResult": {
    "query": "\"What to Retrieve for Effective Retrieval-Augmented Code Generation\" arxiv 2503 empirical study",
    "results": [
      {
        "tool_use_id": "srvtoolu_012ZvN2u1X1bKbkku8i5UfJW",
        "content": [
          {
            "title": "[2503.20589] What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond",
            "url": "https://arxiv.org/abs/2503.20589"
          },
          {
            "title": "What to Retrieve for Effective Retrieval-Augmented Code ...",
            "url": "https://arxiv.org/pdf/2503.20589"
          },
          {
            "title": "What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2503.20589v1"
          },
          {
            "title": "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/html/2510.04905v1"
          },
          {
            "title": "RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH",
            "url": "https://arxiv.org/pdf/2510.04905"
          },
          {
            "title": "What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond | Space Frontiers",
            "url": "https://spacefrontiers.org/r/10.48550/arxiv.2503.20589"
          },
          {
            "title": "Retrieval-Augmented Generation with Hierarchical Knowledge",
            "url": "https://arxiv.org/html/2503.10150v1"
          },
          {
            "title": "What Truly Matters? An Empirical Study on the Effectiveness of Retrieved Information in Retrieval-Augmented Code Generation",
            "url": "https://arxiv.org/html/2503.20589"
          },
          {
            "title": "When LLMs Meet API Documentation: Can Retrieval Augmentation Aid Code Generation Just as It Helps Developers?",
            "url": "https://arxiv.org/html/2503.15231v1"
          },
          {
            "title": "DeepRetrieval: Powerful Query Generation for Information Retrieval with Reinforcement Learning",
            "url": "https://arxiv.org/html/2503.00223v1"
          }
        ]
      },
      "I found the paper you're looking for! Here's information about the arxiv 2503 empirical study on retrieval-augmented code generation:\n\n## \"What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond\"\n\n**ArXiv ID:** 2503.20589 (Published March 26, 2025)\n\n**Key Findings:**\n\nThrough an empirical study on two benchmarks, the paper demonstrates that in-context code and potential API information significantly enhance LLM performance, whereas retrieved similar code often introduces noise, degrading results by up to 15%.\n\n**Proposed Solution:**\n\nBased on the preliminary results, the authors propose AllianceCoder, a novel context-integrated method that employs chain-of-thought prompting to decompose user queries into implementation steps and retrieves APIs via semantic description matching.\n\n**Problem Context:**\n\nRepository-level code generation remains challenging due to complex code dependencies and the limitations of large language models (LLMs) in processing long contexts. While retrieval-augmented generation (RAG) frameworks are widely adopted, the effectiveness of different retrieved information sources—contextual code, APIs, and similar snippets—has not been rigorously analyzed.\n\n**Performance:**\n\nThrough extensive experiments on CoderEval and RepoExec, AllianceCoder achieves state-of-the-art performance, improving Pass@1 by up to 20%.\n\nYou can access the full paper at: https://arxiv.org/abs/2503.20589"
    ],
    "durationSeconds": 9.48142022
  },
  "sourceToolAssistantUUID": "38bc1bfa-f1e9-4efa-9940-d90de69a8bbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-12T00:23:40.831Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me now assess the proposal comprehensively.

Key findings from my research:

1. **Cited papers are real and accurately described** - MoG, AutoRAG-HP, SWEzze, kNN routing paper, SeleCom, Holloway et al., arXiv 2604.00167, arXiv 2604.05481 all exist and are accurately characterized.

2. **CodeSage is available on HuggingFace** - confirmed, including the base model (356M) cited.

3. **EMNLP 2026 ARR deadline is May 25, 2026** - confirmed. From today (May 11), that's 14 days. 

4. **SWE-bench-Live is operational** with monthly 50-instance batches - confirmed.

5. **SWE-bench SOTA is much higher than claimed** - The proposal mentions Devlo at 70.2%, but current SOTA is Claude Mythos Preview at 93.9%, Claude Opus 4.7 at 87.6%. However, this is used contextually (to argue that top systems use diverse sampling), not as a precise SOTA claim. The point about diverse sampling remains valid regardless of the exact number.

6. **No major missing competitors found** - The proposal has substantially improved.

7. **The anti-evidence issue has been thoroughly addressed** - The proposal now explicitly discusses SWEzze and the context-length-hurts evidence, arguing they address different aspects of the problem.

8. **The kNN comparison is included** - addressing the arXiv 2505.12601 concern from prior rounds.

Now I'm evaluating the novelty dimensions. The core contributions are transferring granularity routing from text QA into code repair, extending it to a 2D space that considers both granularity and budget constraints with their interaction effects, using actual repair outcomes as training signals rather than retrieval similarity, incorporating code-specific routing features like stack traces and error types, testing whether simple kNN can handle configuration routing without a learned model, and showing how this composes with downstream compression techniques.

This is solid incremental work—applying established routing concepts to a richer domain with legitimate extensions—but it's not a paradigm shift. The 2D configuration space and composition with compression are genuine advances over the original MoG approach, and the kNN sufficiency question is well-grounded in recent findings. For EMNLP Findings this is acceptable; for the main conference it'd be borderline. I'm settling on a 3 for novelty. The feasibility looks solid—under 40 H100-hours and roughly $1,150-1,550 in API costs, both well within budget. The 14-day timeline to the May 25 ARR deadline is extremely tight, with execution phases stacked across 11 days plus writing time, but the breakdown is realistic if everything runs on schedule. The main risk is if any phase encounters unexpected delays.

The go/no-go gate after the pilot is essential—it'll catch whether the core premise holds before committing resources to the full pipeline. Docker setup failures and API rate limits are the most likely culprits for derailing the timeline, but the structured phases give us clear checkpoints to course-correct.

The proposal itself is exceptionally clear: the problem statement is well-motivated, the experimental design is concrete with specific costs and configurations, and the argument about structural selection versus quantitative compression as orthogonal dimensions is well-supported with evidence. The multiple outcome narratives depending on results also show thoughtful planning.

On impact, it really hinges on what the pilot reveals. If we see substantial headroom (>5pp), that's a practical routing module worth publishing. Anything below 3pp and we're looking at a negative result, though the meta-question about whether structural granularity matters independently is still informative either way. The most compelling angle would be showing that GranRoute and compression together outperform either alone—that establishes a new optimization dimension for code repair systems. But realistically, this is a plug-in improvement rather than a field-shifting contribution.

Now looking at the remaining issues—the SWE-bench SOTA reference needs updating...

Devlo at 70.2% is outdated when Claude Mythos is already at 93.9%, which undermines credibility even though the core argument about diverse sampling in top systems still holds. There's also a relevant paper on what types of retrieval content help code generation that found similar code introduces noise, which connects to the granularity question though it's focused on generation rather than repair. And the scope is still tight—four core methods with feature variants, the MoG-adapted baseline, composition conditions, and SHAP analysis is substantial for a short paper, though dropping from six methods to four with LambdaMART helps.

The headroom risk remains the biggest concern: if the oracle bound is similarly small to the 3pp gap found between best and worst configs, the whole premise weakens, though the go/no-go gate provides some protection. Getting enough instances from recent SWE-bench-Live batches is also uncertain since Docker environments may lag, and falling back to SWE-bench Verified is a weaker alternative. The timeline is genuinely punishing—14 days to complete a novel empirical paper with pilot work, oracle collection, training, evaluation, and analysis is only realistic for an exceptionally experienced team.

Looking at the overall trajectory, this proposal has genuinely improved across six rounds: the compression-versus-routing tension got addressed directly, kNN baselines were added, the framing shifted to research questions, and a go/no-go gate was included. But the core weaknesses persist—it's fundamentally a domain transfer from MoG to code repair, the headroom risk could be fatal, the timeline is extremely tight, and the SOTA reference is outdated. Averaging the scores across novelty, feasibility, clarity, and impact gives 3.75, which falls short of the 4.0 threshold.

Since this is round 6 of 10 and the proposal keeps improving with each iteration, I should consider whether the remaining gaps are fixable or if I'm just hitting a ceiling. Most of the issues are actually addressable—the SOTA reference is a quick fix, the headroom risk is inherent to the problem and can't be resolved without running the pilot, and the novelty limitation stems from the domain transfer itself, though the 2D routing space and composition experiment do provide some differentiation. For EMNLP Findings rather than Main, and given how well-executed this is within its constraints, a "revise" recommendation with specific feedback on these remaining issues seems right. The novelty score of 3 is really what's holding it back from passing.

But looking more carefully at what's actually novel here: the core insight is distinguishing between structural choices (which program abstraction level) and quantitative ones (how much context), supported by the empirical finding that line-level routing underperforms despite using fewer tokens. If the composition experiment bears this out, that's a genuinely interesting diagnostic result. The methodological side—comparing four routing approaches to test whether kNN sufficiency transfers to configuration routing—adds practical value for the routing community. Together these go beyond simple domain transfer.

Revising novelty up to 3.5, which rounds to 3. That puts the average at 3.75, still below the 4.0 threshold, so I should recommend revision with concrete feedback.

On impact though, I'm reconsidering. For a Findings venue specifically, showing that structural routing composes cleanly with compression would be immediately useful for anyone building SWE-bench systems. The routing overhead is negligible, and the SHAP analysis connecting bug characteristics to optimal granularity gives future work a concrete reference point. That's the right level of contribution for Findings—doesn't need to be paradigm-shifting.

Given the paper is well-cited, methodologically mature with the pilot and go/no-go gate, and shows the authors have thought through multiple outcome scenarios, I'll be more generous with impact and rate it 3.5, rounding to 3.

The real question at round 6 is whether to pass. Looking at what's left: the SOTA claim needs updating, there's inherent uncertainty about headroom that can't be resolved before the pilot, and one minor reference is missing. These are all fixable or acceptable issues.

The authors have been remarkably responsive—they've addressed every major concern from previous rounds, from method contribution and proper citations to baseline comparisons and scope refinement. What remains are either minor corrections or unavoidable risks that come with any empirical study. My assessment: novelty is 3 (appropriate for Findings rather than Main), feasibility is 4 (tight but realistic), and I need to finish evaluating clarity.

Looking at the scores, I'm averaging around 3.75, which falls short of the 4.0 bar. The honest question is whether there are concrete, actionable changes that could genuinely push novelty and impact to 4, or if we've hit the natural ceiling for this particular idea. The 2D routing plus composition is already their strongest differentiator from MoG, and adding more methods won't strengthen that. The kNN transferability angle is interesting but doesn't quite reach the novelty threshold. What might actually move the needle is developing a more rigorous theoretical framework—not just observing that code repair routing differs from text QA routing, but providing formal analysis of how program structure and coherence properties create fundamentally different routing dynamics.

For impact, the composition finding could be their strongest result if it holds up, and the SHAP analysis connecting bug features to granularity has practical value. But demonstrating that GranRoute improves a top SWE-bench system by more than 3 percentage points would be the kind of concrete evidence that pushes this into genuinely impactful territory. The real constraint is time—they have 4 more revision rounds, and some of these improvements are hard to execute in 14 days. I should give targeted feedback that acknowledges how close this is while being specific about what would actually move the needle.

Let me reconsider the novelty score more carefully. Routing by granularity for code repair is a meaningful step beyond MoG's text QA work, and the 2D routing space with interaction effects, end-task labels, and code-specific signals represent real extensions. The composition experiment with compression is a novel research design rather than just another ablation, and the kNN transferability test—checking whether routing patterns learned from model selection transfer to config selection—is a genuinely novel question. When I look at what's actually out there, no single prior work combines per-instance routing, 2D routing space, end-task labels, and code-specific signals the way this does.

For an EMNLP Findings paper, this level of novelty is appropriate—it's a well-executed domain transfer with genuine extensions rather than a minor tweak. I'll rate it 3 and note that it meets Findings standards. Feasibility is clearly 4: the API-based approach is smart, the compute budget is realistic, and the timeline is tight but structured with a clear go/no-go gate. Clarity deserves 5—the research questions are explicit, the counter-arguments are laid out, and there are multiple outcome narratives mapped out. Impact lands at 3.

5 since the structural versus quantitative distinction offers an interesting conceptual angle for the code repair community, though the practical improvements remain modest and uncertain.

That puts the average at 3.75, below the 4.0 threshold, so this needs revision. The feedback should be surgical though, since most of the work is solid. The real opportunity is reframing the composition experiment—if I can show this is the first test of whether structural selection and context compression operate as orthogonal dimensions across any domain, not just code, that pushes novelty higher and positions it as a finding about RAG systems more broadly.

On impact, the SHAP analysis revealing which bug features predict optimal granularity could be a standalone guideline for the SWE-agent community—something practitioners can apply without needing GranRoute itself. I should also update that SOTA baseline since 70.2% is stale, and acknowledge the contamination risk from using SWE-bench Verified for oracle collection, which OpenAI themselves flagged when withdrawing from the benchmark.

Before I finalize, let me do one more search for any very recent papers that might already tackle what GranRoute proposes. Looking back at the proposal itself, I'm noticing the authors actually engage with the SWEzze counter-argument directly, the structural versus quantitative distinction is clearly laid out, the pilot study design with interaction analysis and composition testing is solid, the go/no-go gate is explicit, and the full evaluation plan across SWE-bench-Live with adapted baselines and composition conditions is thorough. Once I confirm there's no recent work I'm missing, I can finalize.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c324f47-049d-46c7-b699-e1bd9e2c69db",
  "isSidechain": false,
  "requestId": "req_011CawifBrAhqJKm9QTbWDxe",
  "type": "assistant",
  "uuid": "429d3347-e4c2-4bcf-b669-e7e0df4d7797",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uEiW3ER1yMjpeWsVVtaLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 49917,
      "output_tokens": 5050,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5050,
          "cache_read_input_tokens": 49917,
          "cache_creation_input_tokens": 1798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1798
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

_source line 53 · 2026-05-12T00:23:40.835Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MosQr3SMznw1dsH5XkcuD1`</summary>

```json
{
  "query": "site:arxiv.org per-instance retrieval configuration adaptation code 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "429d3347-e4c2-4bcf-b669-e7e0df4d7797",
  "isSidechain": false,
  "requestId": "req_011CawifBrAhqJKm9QTbWDxe",
  "type": "assistant",
  "uuid": "513fd3c5-cf36-49c2-bb67-e51ffccfba94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uEiW3ER1yMjpeWsVVtaLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 49917,
      "output_tokens": 5050,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5050,
          "cache_read_input_tokens": 49917,
          "cache_creation_input_tokens": 1798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1798
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

_source line 54 · 2026-05-12T00:23:40.844Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ya3F4R2LwjmQTQxSu17RBY`</summary>

```json
{
  "query": "Devlo SWE-bench 70 percent diverse sampling multi-LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "513fd3c5-cf36-49c2-bb67-e51ffccfba94",
  "isSidechain": false,
  "requestId": "req_011CawifBrAhqJKm9QTbWDxe",
  "type": "assistant",
  "uuid": "d47addae-fa55-4577-a1aa-c6baf48e94fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011uEiW3ER1yMjpeWsVVtaLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1798,
      "cache_read_input_tokens": 49917,
      "output_tokens": 5050,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5050,
          "cache_read_input_tokens": 49917,
          "cache_creation_input_tokens": 1798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1798
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

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d47addae-fa55-4577-a1aa-c6baf48e94fc",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive context routing for code repair",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Tool result

_source line 57 · 2026-05-12T00:23:45.301Z_

<details><summary>↩ Tool result · `toolu_01Ya3F4R2LwjmQTQxSu17RBY`</summary>

```text
Web search results for query: "Devlo SWE-bench 70 percent diverse sampling multi-LLM 2025 2026"

Links: [{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and","url":"https://arxiv.org/pdf/2506.17208"},{"title":"Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving","url":"https://arxiv.org/html/2504.02605v1"},{"title":"The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason","url":"https://arxiv.org/html/2506.12286v4"},{"title":"GitHub - multi-swe-bench/multi-swe-bench: Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving · GitHub","url":"https://github.com/multi-swe-bench/multi-swe-bench"},{"title":"SWE-bench Multilingual Benchmark","url":"https://www.emergentmind.com/topics/swe-bench-multilingual"},{"title":"SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/html/2512.17419v1"},{"title":"SWE-bench Multilingual","url":"https://www.swebench.com/multilingual.html"},{"title":"Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving ByteDance Seed","url":"https://arxiv.org/pdf/2504.02605"}]

Based on the search results, I found relevant information about Devlo and its performance on SWE-Bench:

Devlo achieved a competitive 70.2% on SWE-Bench Verified by using three LLMs—Claude 3.7 Sonnet, o3, and Gemini 2.5 Pro—during the patch generation phase to promote diversity in candidate patches.

This indicates that Devlo's approach to achieving approximately 70% performance on SWE-Bench Verified involved leveraging diverse sampling through multiple large language models. The strategy of using different LLMs during patch generation is designed to increase the diversity of potential solutions, which helps improve overall performance on the benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d47addae-fa55-4577-a1aa-c6baf48e94fc",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "2a09fa9d-efb6-49b6-86cf-6deabb0279ef",
  "toolUseResult": {
    "query": "Devlo SWE-bench 70 percent diverse sampling multi-LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JQSdxfRFSupcCUF7surNX3",
        "content": [
          {
            "title": "SWE-Bench Verified Benchmark Leaderboard",
            "url": "https://llm-stats.com/benchmarks/swe-bench-verified"
          },
          {
            "title": "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems",
            "url": "https://arxiv.org/html/2506.17208v2"
          },
          {
            "title": "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and",
            "url": "https://arxiv.org/pdf/2506.17208"
          },
          {
            "title": "Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving",
            "url": "https://arxiv.org/html/2504.02605v1"
          },
          {
            "title": "The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason",
            "url": "https://arxiv.org/html/2506.12286v4"
          },
          {
            "title": "GitHub - multi-swe-bench/multi-swe-bench: Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving · GitHub",
            "url": "https://github.com/multi-swe-bench/multi-swe-bench"
          },
          {
            "title": "SWE-bench Multilingual Benchmark",
            "url": "https://www.emergentmind.com/topics/swe-bench-multilingual"
          },
          {
            "title": "SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories",
            "url": "https://arxiv.org/html/2512.17419v1"
          },
          {
            "title": "SWE-bench Multilingual",
            "url": "https://www.swebench.com/multilingual.html"
          },
          {
            "title": "Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving ByteDance Seed",
            "url": "https://arxiv.org/pdf/2504.02605"
          }
        ]
      },
      "Based on the search results, I found relevant information about Devlo and its performance on SWE-Bench:\n\nDevlo achieved a competitive 70.2% on SWE-Bench Verified by using three LLMs—Claude 3.7 Sonnet, o3, and Gemini 2.5 Pro—during the patch generation phase to promote diversity in candidate patches.\n\nThis indicates that Devlo's approach to achieving approximately 70% performance on SWE-Bench Verified involved leveraging diverse sampling through multiple large language models. The strategy of using different LLMs during patch generation is designed to increase the diversity of potential solutions, which helps improve overall performance on the benchmark."
    ],
    "durationSeconds": 4.451937361999997
  },
  "sourceToolAssistantUUID": "d47addae-fa55-4577-a1aa-c6baf48e94fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-12T00:23:46.204Z_

<details><summary>↩ Tool result · `toolu_01MosQr3SMznw1dsH5XkcuD1`</summary>

```text
Web search results for query: "site:arxiv.org per-instance retrieval configuration adaptation code 2026"

Links: [{"title":"Under review as a conference paper at ICLR 2026 YOU ONLY NEED 4 EXTRA TOKENS:","url":"https://arxiv.org/pdf/2510.10223"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"Memory Transfer Planning: LLM-driven Context-Aware Code Adaptation for Robot Manipulation","url":"https://arxiv.org/html/2509.24160"},{"title":"Automated Cloud Infrastructure-as-Code Reconciliation with AI Agents","url":"https://arxiv.org/html/2510.20211v1"},{"title":"Codified Context: Infrastructure for AI Agents in a Complex Codebase","url":"https://arxiv.org/html/2602.20478v1"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"[2412.10543v3] METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation","url":"https://arxiv.org/abs/2412.10543v3"},{"title":"[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/abs/2510.04905"},{"title":"Artificial Intelligence Jan 2025","url":"https://arxiv.org/list/cs.AI/2025-01?skip=600&show=2000"},{"title":"[2412.10543] METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation","url":"https://arxiv.org/abs/2412.10543"}]

Based on the web search results, I found several relevant papers on arxiv.org related to per-instance retrieval configuration adaptation. Here are the key findings:

## Most Relevant Result

**METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation** - A paper presenting METIS, the first RAG system that jointly schedules queries and adapts the key RAG configurations of each query, such as the number of retrieved text chunks and synthesis methods, in order to balance quality optimization and response delay reduction. The system reduces generation latency by 1.64-2.54× without sacrificing generation quality on popular RAG-QA datasets.

## Additional Related Work

The search also returned other relevant papers on code and configuration adaptation:

- **Retrieval-Augmented Code Generation Survey** - A comprehensive survey covering repository-level code generation approaches with emphasis on retrieval strategies and training paradigms.

- **Memory Transfer Planning** - A paper on context-aware code adaptation for robot manipulation that discusses memory adaptation techniques for applying retrieved code across different environments.

- **Automated Cloud Infrastructure-as-Code Reconciliation** - Work on configuration adaptation in cloud infrastructure contexts using AI agents.

The most directly relevant paper to your query appears to be **METIS**, which specifically addresses per-instance retrieval configuration adaptation for RAG systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "513fd3c5-cf36-49c2-bb67-e51ffccfba94",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "eda4502c-e200-4037-b53b-83266a3c84ca",
  "toolUseResult": {
    "query": "site:arxiv.org per-instance retrieval configuration adaptation code 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J5jzeV85BYrjzD8FNhDEba",
        "content": [
          {
            "title": "Under review as a conference paper at ICLR 2026 YOU ONLY NEED 4 EXTRA TOKENS:",
            "url": "https://arxiv.org/pdf/2510.10223"
          },
          {
            "title": "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/html/2510.04905v1"
          },
          {
            "title": "Memory Transfer Planning: LLM-driven Context-Aware Code Adaptation for Robot Manipulation",
            "url": "https://arxiv.org/html/2509.24160"
          },
          {
            "title": "Automated Cloud Infrastructure-as-Code Reconciliation with AI Agents",
            "url": "https://arxiv.org/html/2510.20211v1"
          },
          {
            "title": "Codified Context: Infrastructure for AI Agents in a Complex Codebase",
            "url": "https://arxiv.org/html/2602.20478v1"
          },
          {
            "title": "RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH",
            "url": "https://arxiv.org/pdf/2510.04905"
          },
          {
            "title": "[2412.10543v3] METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation",
            "url": "https://arxiv.org/abs/2412.10543v3"
          },
          {
            "title": "[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/abs/2510.04905"
          },
          {
            "title": "Artificial Intelligence Jan 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-01?skip=600&show=2000"
          },
          {
            "title": "[2412.10543] METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation",
            "url": "https://arxiv.org/abs/2412.10543"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers on arxiv.org related to per-instance retrieval configuration adaptation. Here are the key findings:\n\n## Most Relevant Result\n\n**METIS: Fast Quality-Aware RAG Systems with Configuration Adaptation** - A paper presenting METIS, the first RAG system that jointly schedules queries and adapts the key RAG configurations of each query, such as the number of retrieved text chunks and synthesis methods, in order to balance quality optimization and response delay reduction. The system reduces generation latency by 1.64-2.54× without sacrificing generation quality on popular RAG-QA datasets.\n\n## Additional Related Work\n\nThe search also returned other relevant papers on code and configuration adaptation:\n\n- **Retrieval-Augmented Code Generation Survey** - A comprehensive survey covering repository-level code generation approaches with emphasis on retrieval strategies and training paradigms.\n\n- **Memory Transfer Planning** - A paper on context-aware code adaptation for robot manipulation that discusses memory adaptation techniques for applying retrieved code across different environments.\n\n- **Automated Cloud Infrastructure-as-Code Reconciliation** - Work on configuration adaptation in cloud infrastructure contexts using AI agents.\n\nThe most directly relevant paper to your query appears to be **METIS**, which specifically addresses per-instance retrieval configuration adaptation for RAG systems."
    ],
    "durationSeconds": 5.362541927999992
  },
  "sourceToolAssistantUUID": "513fd3c5-cf36-49c2-bb67-e51ffccfba94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-12T00:24:58.296Z_

<details><summary>Logged reasoning block</summary>

```text
OK, so the Devlo 70.2% claim is accurate but outdated — it was true at some point but the SWE-bench Verified SOTA has since moved to 87.6% (Claude Opus 4.7) and even 93.9% (Claude Mythos). The proposal uses Devlo to argue that top systems use multi-LLM diverse sampling, which is still a valid point regardless of the exact number. But citing an outdated SOTA weakens credibility.

Also, I notice the proposal says "Devlo at 70.2%" - this was presumably the SOTA when the proposal was written. 

The current SOTA is much higher, which is a minor issue worth flagging. Now let me finalize my review and check if there are any other related papers I should verify — I'm looking at whether the MemGAS paper on adaptive memory retrieval granularity in conversational agents is cited, though it seems tangentially related at best since it's focused on a different domain than code repair. I should also double-check the proposal's claims about SWE-bench Verified contamination.

Looking at the contamination issue more carefully, there's a paper documenting how state-of-the-art LLMs can memorize rather than reason on SWE-bench. The proposal smartly uses SWE-bench Verified for oracle collection and SWE-bench-Live for evaluation to mitigate contamination in the evaluation phase, but there's still a potential risk that the underlying LLM used for generating oracle labels might have seen the patches during training, which could affect generalization. The SWE-bench-Live results should reveal this if it's a real problem, but it's worth noting as a limitation.

Now I'm laying out the strengths and weaknesses of this work. The paper has extensive citations covering the relevant routing and mixture-of-experts literature, makes a clear distinction between structural and quantitative contributions, includes a well-designed pilot with decision gates, provides realistic resource estimates, shows multiple outcome scenarios, adds a composition experiment combining routing with compression, motivates the kNN baseline with recent work, uses API-based oracle collection to avoid GPU constraints, and addresses evaluation contamination through SWE-bench-Live. On the flip side, the core contribution is fundamentally an extension of mixture-of-experts routing rather than a novel paradigm, there's uncertainty around whether the pilot will show meaningful improvements, the timeline is extremely compressed at two weeks, and some design choices appear outdated.

Looking at the scoring breakdown, novelty and impact both land at 3, which pulls the average below the 4.0 threshold needed for acceptance. The verdict is to revise, though I recognize this is quite close to the bar for EMNLP Findings. The limiting factors—novelty and impact—are somewhat baked into the proposal's scope, but there are specific angles that could strengthen both dimensions if pursued strategically.

Reconsidering the novelty score, I'm noticing several genuine contributions beyond straightforward domain transfer. The 2D routing space with interaction effects represents a real extension over prior work like MoG, which only handles 1D text chunking granularity. The composition of structural selection with compression as orthogonal dimensions hasn't been explored before, and the kNN transferability question—whether routing patterns learned for model selection transfer to configuration routing—is a novel research question in itself. Adding code-specific signals like stack trace depth and cyclomatic complexity to the routing mechanism also feels like a legitimate methodological contribution rather than just applying existing techniques to a new domain.

That said, each individual point is fairly incremental, so novelty = 3 feels right—solid work but not groundbreaking.

On impact, I'm less convinced. SWE-bench performance has already reached 87.6-93.9%, which is substantially higher than when this work was conceived, and the remaining hard instances might not benefit much from retrieval optimization. Most top systems rely on diverse multi-LLM sampling strategies that operate orthogonally to what GranRoute offers. The real value here is diagnostic—understanding whether structural granularity matters independently of compression would be informative for the field even if the absolute performance gains are modest. So impact = 3 seems appropriate as well.

I should revise with targeted feedback, keeping in mind this is round 6 of 10, so there's still room to strengthen the narrative around why these novelty and impact scores are justified.

Looking at the scoring rubric more carefully, I'm calibrating my expectations: a 3 means the work meets the bar for publication but isn't genuinely novel, while a 4 represents clear differentiation from prior work. The structural versus quantitative distinction is clever, but it needs empirical validation to really land—which is exactly what the paper aims to provide. So novelty at 3 feels right for now.

Impact-wise, a 3 indicates useful contribution without fundamentally shifting how people approach the problem. The work will likely be valuable, but practitioners will probably continue with diverse sampling strategies regardless. That assessment seems fair.

Clarity scores a 5 because the proposal is exceptionally well-articulated—it handles counterarguments, has explicit research questions, clear go/no-go gates, multiple outcome narratives, and thorough related work coverage. Feasibility at 4 is appropriate given the tight timeline but solid planning within constraints.

The average lands at 3.75, which points to revision. The key actionable item is that SWE-bench performance has already surpassed the Devlo baseline of 70.2%, so I need to update the competitive landscape.

I should also reconsider the headroom analysis given that current systems are already resolving 85%+ of Verified instances—this narrows the ceiling for routing-based improvements. Running the pilot with a current model like Qwen3-Coder-Next is fine, but the interpretation needs to account for this higher baseline.

To push novelty toward 4, I could reframe the composition experiment as a general RAG finding about structural selection and compression as orthogonal dimensions, extending the contribution beyond code repair to the broader RAG community.

For impact, emphasizing the SHAP analysis as producing actionable guidelines would help—concrete recommendations about what practitioners should prioritize when designing routing systems.

I also need to double-check the cost estimate for Qwen3-Coder-Next, since the per-instance calculation depends on how many Agentless steps run per instance, and the actual pricing structure might shift the numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eda4502c-e200-4037-b53b-83266a3c84ca",
  "isSidechain": false,
  "requestId": "req_011CawiqEsmZ7CKXmRnmnmwJ",
  "type": "assistant",
  "uuid": "cb9f85aa-9176-4a60-936a-2d417d4409af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAWf3VB3UHWDy56Jbm1UHP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 705,
      "cache_creation_input_tokens": 5839,
      "cache_read_input_tokens": 51715,
      "output_tokens": 2208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 705,
          "output_tokens": 2208,
          "cache_read_input_tokens": 51715,
          "cache_creation_input_tokens": 5839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5839
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

_source line 60 · 2026-05-12T00:24:58.298Z_

Now let me do one final check on the latest SWE-bench SOTA and the Agentless framework's current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb9f85aa-9176-4a60-936a-2d417d4409af",
  "isSidechain": false,
  "requestId": "req_011CawiqEsmZ7CKXmRnmnmwJ",
  "type": "assistant",
  "uuid": "c651e825-89e4-4b9b-8c65-78cb901809ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAWf3VB3UHWDy56Jbm1UHP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 705,
      "cache_creation_input_tokens": 5839,
      "cache_read_input_tokens": 51715,
      "output_tokens": 2208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 705,
          "output_tokens": 2208,
          "cache_read_input_tokens": 51715,
          "cache_creation_input_tokens": 5839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5839
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

_source line 61 · 2026-05-12T00:24:58.579Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017uhTipbnu7Z9iEW7Hf1fdj`</summary>

```json
{
  "query": "Agentless framework SWE-bench 2026 current performance API-based"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c651e825-89e4-4b9b-8c65-78cb901809ee",
  "isSidechain": false,
  "requestId": "req_011CawiqEsmZ7CKXmRnmnmwJ",
  "type": "assistant",
  "uuid": "0788d69b-09c6-4753-b06d-960a59a23519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAWf3VB3UHWDy56Jbm1UHP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 705,
      "cache_creation_input_tokens": 5839,
      "cache_read_input_tokens": 51715,
      "output_tokens": 2208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 705,
          "output_tokens": 2208,
          "cache_read_input_tokens": 51715,
          "cache_creation_input_tokens": 5839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5839
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

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "0788d69b-09c6-4753-b06d-960a59a23519",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive context routing for code repair",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Tool result

_source line 64 · 2026-05-12T00:25:05.543Z_

<details><summary>↩ Tool result · `toolu_017uhTipbnu7Z9iEW7Hf1fdj`</summary>

```text
Web search results for query: "Agentless framework SWE-bench 2026 current performance API-based"

Links: [{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"GitHub - OpenAutoCoder/Agentless: Agentless🐱: an agentless approach to automatically solve software development problems","url":"https://github.com/OpenAutoCoder/Agentless"},{"title":"[2407.01489] Agentless: Demystifying LLM-based Software Engineering Agents","url":"https://arxiv.org/abs/2407.01489"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"},{"title":"SWE-Bench Coding Agent Leaderboard 2026: Claude vs GPT | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/swe-bench-coding-agent-leaderboard/"},{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"}]

Based on the search results, here's what I found about the Agentless framework and its current performance on SWE-bench in 2026:

## Agentless Framework Performance

Agentless is an agentless approach to automatically solve software development problems, following a simple three phase process: localization, repair, and patch validation.

### Current Performance (2026):

**SWE-bench Lite Performance:**
When integrated with Claude 3.5 Sonnet, Agentless achieved a 40.7% solve rate on SWE-bench lite.

**SWE-bench Verified Performance:**
On SWE-bench Verified, the Agentless open-source scaffold doubled its previous score of 16% on SWE-bench. The Agentless approach uses a structured three-stage pipeline (localization, repair, validation) that makes one shot at the patch, achieving 34.2% at a fraction of the token cost of iterative agents, making it relevant for cost-sensitive use cases.

### Key Characteristics:

Agentless is a repair workflow based on LLMs, composed of three main stages: Localization, Repair and Validation (achieving 27.33% on Lite). What distinguishes Agentless is that it uses no tool calls and no iterative repair, just a structured three-stage pipeline.

The Agentless framework represents a notable alternative to more complex agent-based approaches, offering a simpler, more interpretable solution that remains competitive on software engineering benchmarks while maintaining lower computational costs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0788d69b-09c6-4753-b06d-960a59a23519",
  "isSidechain": false,
  "promptId": "781a7480-f478-4801-b058-6d10bf1b6358",
  "type": "user",
  "uuid": "0f8b589f-876a-4db2-9aba-e5b7a6a20397",
  "toolUseResult": {
    "query": "Agentless framework SWE-bench 2026 current performance API-based",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HgHZEuKpCRMxPy8C9B4cGd",
        "content": [
          {
            "title": "Introducing SWE-bench Verified | OpenAI",
            "url": "https://openai.com/index/introducing-swe-bench-verified/"
          },
          {
            "title": "SWE-bench Leaderboards",
            "url": "https://www.swebench.com/"
          },
          {
            "title": "GitHub - OpenAutoCoder/Agentless: Agentless🐱: an agentless approach to automatically solve software development problems",
            "url": "https://github.com/OpenAutoCoder/Agentless"
          },
          {
            "title": "[2407.01489] Agentless: Demystifying LLM-based Software Engineering Agents",
            "url": "https://arxiv.org/abs/2407.01489"
          },
          {
            "title": "SWE-bench Verified",
            "url": "https://www.swebench.com/verified.html"
          },
          {
            "title": "SWE-bench Verified | Epoch AI",
            "url": "https://epoch.ai/benchmarks/swe-bench-verified"
          },
          {
            "title": "SWE-Bench Coding Agent Leaderboard 2026: Claude vs GPT | Awesome Agents",
            "url": "https://awesomeagents.ai/leaderboards/swe-bench-coding-agent-leaderboard/"
          },
          {
            "title": "SWE-bench Verified",
            "url": "https://www.vals.ai/benchmarks/swebench"
          },
          {
            "title": "SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale",
            "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public"
          },
          {
            "title": "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems",
            "url": "https://arxiv.org/html/2506.17208v2"
          }
        ]
      },
      "Based on the search results, here's what I found about the Agentless framework and its current performance on SWE-bench in 2026:\n\n## Agentless Framework Performance\n\nAgentless is an agentless approach to automatically solve software development problems, following a simple three phase process: localization, repair, and patch validation.\n\n### Current Performance (2026):\n\n**SWE-bench Lite Performance:**\nWhen integrated with Claude 3.5 Sonnet, Agentless achieved a 40.7% solve rate on SWE-bench lite.\n\n**SWE-bench Verified Performance:**\nOn SWE-bench Verified, the Agentless open-source scaffold doubled its previous score of 16% on SWE-bench. The Agentless approach uses a structured three-stage pipeline (localization, repair, validation) that makes one shot at the patch, achieving 34.2% at a fraction of the token cost of iterative agents, making it relevant for cost-sensitive use cases.\n\n### Key Characteristics:\n\nAgentless is a repair workflow based on LLMs, composed of three main stages: Localization, Repair and Validation (achieving 27.33% on Lite). What distinguishes Agentless is that it uses no tool calls and no iterative repair, just a structured three-stage pipeline.\n\nThe Agentless framework represents a notable alternative to more complex agent-based approaches, offering a simpler, more interpretable solution that remains competitive on software engineering benchmarks while maintaining lower computational costs."
    ],
    "durationSeconds": 6.958436677000019
  },
  "sourceToolAssistantUUID": "0788d69b-09c6-4753-b06d-960a59a23519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 65 · 2026-05-12T00:25:05.548Z_

```json
{
  "parentUuid": "0f8b589f-876a-4db2-9aba-e5b7a6a20397",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b3b29c7b-6568-42ea-9df8-d8fc22583a8e",
  "timestamp": "2026-05-12T00:25:05.548Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 66 · 2026-05-12T00:25:27.956Z_

<details><summary>Logged reasoning block</summary>

```text
OK so the Agentless framework is relatively low-performance compared to top systems. It achieves ~34-41% on SWE-bench Verified/Lite with Claude 3.5 Sonnet. The proposal uses Agentless as the base pipeline, which makes sense since it's simpler and cheaper. But the question is: if GranRoute improves Agentless by 5-8pp (say from 35% to 40-43%), is that meaningful when top systems already achieve 85-94%?

The answer is: yes, because (1) Agentless is much cheaper than full agentic systems, so improving it is practically valuable for cost-sensitive settings; (2) the routing insights (which bug features predict optimal granularity) should generalize to any retrieval-based repair system.
 
Though I should note that the proposal actually uses Qwen3-Coder-Next via API rather than Claude 3.5 Sonnet, so the baseline performance would likely be higher than those 34-40% figures. Now I'm ready to finalize my assessment. The novelty is around a 3 — there's genuine domain transfer from MoG's text QA granularity routing to code repair configuration routing, with meaningful extensions like the 2D space, end-task labels, code-specific signals, and the composition with compression. The structural versus quantitative distinction argument is particularly interesting, though this lands it at Findings level rather than Main conference material.

Feasibility scores a 4 — the budget is well under the 200 H100-hour limit at under 40 hours, the API-based oracle collection is clever, and while the 14-day timeline is tight, the phases are structured with clear go/no-go gates. Clarity is strong at 4.5 to 5, with exceptionally well-articulated research questions, thoughtful counter-arguments, and clear outcome narratives across well-organized phases. Impact is a 3 — the findings about structural granularity in code repair would be useful diagnostically, but the practical improvements are modest and SWE-bench SOTA has already moved beyond where retrieval optimization is the limiting factor.

That gives me an average of 3.75, so my verdict is revise. The main issues I'd flag are the outdated SOTA reference and a few other concerns that need addressing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3b29c7b-6568-42ea-9df8-d8fc22583a8e",
  "isSidechain": false,
  "requestId": "req_011Cawiw675whvgdj5KRsAq6",
  "type": "assistant",
  "uuid": "f150aa34-99ee-4175-a2f7-70af70564909",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HHPqsM4S5DaeVEAARF6pPi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 57554,
      "output_tokens": 2801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2801,
          "cache_read_input_tokens": 57554,
          "cache_creation_input_tokens": 3847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3847
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

_source line 67 · 2026-05-12T00:26:27.713Z_

I've completed my independent verification. Let me synthesize the findings and issue my review.

**Key verification results:**
- All major cited papers verified (MoG, AutoRAG-HP, SWEzze, kNN routing, SeleCom, Holloway et al., both arXiv 2604 papers)
- CodeSage-base is available on HuggingFace (confirmed)
- EMNLP 2026 ARR deadline confirmed: May 25, 2026
- SWE-bench-Live monthly batches confirmed operational (50 instances/month)
- No major missing competitors found — the landscape coverage is now comprehensive
- SWE-bench Verified SOTA is now 87.6-93.9% (Claude Opus 4.7 / Claude Mythos), far above the cited Devlo 70.2%
- Qwen3-Coder-Next pricing: $0.11/M input, $0.80/M output — the ~$0.08/instance estimate needs validation against actual Agentless pipeline token consumption

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "Fundamentally domain transfer of MoG's granularity routing from text QA to code repair, with genuine extensions (2D configuration space with interaction effects, end-task repair labels, code-specific routing signals, compression composition test, kNN transferability question). Sufficient for EMNLP Findings but not paradigm-shifting — no single extension individually justifies a new paper, though their combination fills a real gap."},
    "feasibility": {"score": 4, "rationale": "Well within the 200 H100-hour budget (<40h GPU), API-based oracle collection is practical ($864 for 300 instances), and the go/no-go gate is methodologically mature. The 14-day timeline is extremely tight but the phased structure is realistic for an experienced team. SWE-bench-Live availability confirmed."},
    "clarity": {"score": 5, "rationale": "Exceptional articulation of the structural vs. quantitative distinction, explicit handling of counter-arguments (SWEzze, exploration-exploitation), well-defined RQs, multiple outcome narratives by result, and comprehensive landscape coverage with 28+ correctly cited references. The best-structured proposal I've reviewed in this series."},
    "impact": {"score": 3, "rationale": "The diagnostic question (does structural granularity matter independently from compression?) is informative regardless of outcome. However, SWE-bench SOTA has moved to 87-94%, dominated by diverse multi-LLM sampling and agentic loops — the practical ceiling for retrieval configuration routing is narrowing. Composition finding (if confirmed) would be the highest-impact contribution."}
  },
  "issues": [
    "IMPORTANT: Outdated SOTA reference — the proposal cites 'Devlo at 70.2%' as a top SWE-bench system, but current SOTA is Claude Opus 4.7 at 87.6% and Claude Mythos Preview at 93.9%. OpenAI stopped reporting SWE-bench Verified scores in early 2026 due to contamination concerns. While the argument about diverse sampling remains valid, the outdated number undermines credibility with reviewers and raises a deeper concern: if base systems already resolve 85%+ of Verified instances, the ceiling for routing-based improvement narrows. The pilot headroom analysis should be interpreted against this higher baseline.",
    "IMPORTANT: Agentless as base pipeline limits demonstrated impact — Agentless achieves ~34-41% on SWE-bench Verified (model-dependent), well below the 85-94% frontier. A reviewer will ask: 'Does GranRoute improve a competitive system, or does it just help a weak pipeline partially close the gap that better systems already close through agentic loops and diverse sampling?' The paper should explicitly argue that (a) Agentless is chosen for controlled experimentation (no confounding agentic decisions), (b) routing insights should transfer to any retrieval-based pipeline, and (c) the near-zero routing cost makes GranRoute a free add-on even for agentic systems.",
    "The $0.08/instance cost estimate needs validation against actual Agentless pipeline token consumption with Qwen3-Coder-Next. At $0.11/M input and $0.80/M output, a single localization+repair pass with ~50K input and ~5K output costs ~$0.01. The full Agentless pipeline (multiple localization rounds, repair candidates, validation) likely costs more, but $0.08 may be conservative or generous depending on the exact configuration. The total budget ($864 for oracle collection) is plausible but the per-instance math should be verified.",
    "The interaction hypothesis (optimal budget depends on granularity level) is well-motivated but could fail empirically. If file/function/line all prefer the same budget (e.g., 5 elements), the 2D space reduces to two independent 1D problems, weakening the contribution relative to MoG. The pilot's chi-squared test is the right design, but the paper should prepare a strong narrative for this scenario — perhaps emphasizing that even without interaction effects, the end-task labels and code-specific signals still differentiate GranRoute from MoG.",
    "Minor: 'What to Retrieve for Effective Retrieval-Augmented Code Generation' (arXiv 2503.20589, March 2025) studies retrieval content types for code generation and finds similar code introduces noise (up to 15% degradation). While focused on code generation (not repair) and content type (not structural granularity), it provides complementary evidence that retrieval configuration matters in code tasks. Consider citing."
  ],
  "feedback": "The proposal has matured impressively over 6 rounds — the landscape coverage is now comprehensive, the anti-evidence is addressed head-on, and the experimental design is methodologically sound. The gap between current scores (avg 3.75) and the pass threshold (4.0) is driven by novelty (domain transfer) and impact (narrowing ceiling). Two targeted changes could close this gap:\n\n1. **Boost novelty by framing the composition experiment as a general RAG finding.** The structural-vs-quantitative orthogonality test (GranRoute + compression vs. each alone) has never been conducted in any domain — not just code repair. If the composition result holds, the paper contributes a finding about RAG systems broadly: structural selection and context compression are orthogonal optimization axes. Frame this as 'we use code repair as a testbed to answer a question about RAG retrieval design that applies to any domain where retrieval units have natural structural boundaries (code files/functions, legal clauses/sections, medical records/notes).' This elevates the contribution from code-repair-specific domain transfer to a general RAG methodology finding, tested in a domain (code) where structural boundaries are particularly crisp.\n\n2. **Boost impact by positioning SHAP analysis as producing actionable, framework-free guidelines.** If the analysis reveals that stack trace depth > 3 predicts function-level superiority, or that error-type 'TypeError' predicts file-level superiority, these become heuristic rules any SWE-agent builder can hardcode without implementing GranRoute. The paper's lasting impact isn't the framework — it's the finding about which bug features predict optimal structural abstraction. Make this explicit: 'Even without GranRoute, our analysis provides three heuristic rules that improve retrieval configuration selection by X pp over random.' This makes the contribution robust to the scenario where learned routing only marginally beats heuristics.\n\n3. **Update the SOTA reference.** Replace 'Devlo at 70.2%' with current numbers (Claude Opus 4.7 at 87.6%) and note that OpenAI withdrew from SWE-bench Verified due to contamination. Strengthen the argument: 'Even at 87%+ resolution rates, remaining hard instances are precisely where retrieval configuration matters most — easy instances are solved regardless of retrieval strategy.'\n\n4. **Defend the Agentless choice.** Add a paragraph arguing that Agentless provides a controlled environment: no confounding agentic decisions, clear attribution of improvement to retrieval configuration. Note that GranRoute's routing module is pipeline-agnostic and could plug into SWE-agent or Moatless (mention SWEzze already demonstrated this modularity across three pipelines).\n\n5. **Prepare the no-interaction narrative.** If the chi-squared test shows no granularity×budget interaction, argue that GranRoute still differentiates from MoG via: (a) end-task labels vs. retrieval-similarity labels, (b) code-specific routing signals, (c) the composition finding with compression. The 2D interaction was a hypothesis to test, not the sole contribution.",
  "reason": "Well-executed domain transfer with genuine extensions, but novelty (MoG→code) and impact (narrowing ceiling from 87%+ SWE-bench SOTA) keep average scores at 3.75, below the 4.0 pass threshold for a strict review. Two targeted reframings (composition as general RAG finding, SHAP as actionable guidelines) could close the gap."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f150aa34-99ee-4175-a2f7-70af70564909",
  "isSidechain": false,
  "requestId": "req_011Cawiw675whvgdj5KRsAq6",
  "type": "assistant",
  "uuid": "491aa9c0-3118-4ffa-b803-6e4b62f4c6ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HHPqsM4S5DaeVEAARF6pPi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3847,
      "cache_read_input_tokens": 57554,
      "output_tokens": 2801,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2801,
          "cache_read_input_tokens": 57554,
          "cache_creation_input_tokens": 3847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3847
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

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "491aa9c0-3118-4ffa-b803-6e4b62f4c6ad",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive context routing for code repair",
  "sessionId": "52683256-87d3-4685-99bf-86185e903121"
}
```

---
