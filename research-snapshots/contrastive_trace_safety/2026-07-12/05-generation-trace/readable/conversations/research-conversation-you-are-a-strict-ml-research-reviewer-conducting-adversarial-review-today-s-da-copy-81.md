# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-11 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/374fbfc5-cb65-4184-9681-4b68ae4e643d.jsonl`
- **Structured JSON:** [`013162ab06d6b7823fd3.json`](../../sessions/01/013162ab06d6b7823fd3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-11T23:36:00.301Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-11T23:36:00.301Z",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-11 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 4/10)\n{\n  \"title\": \"GranRoute: Learning to Route Retrieval Configurations for Repository-Level Code Repair\",\n  \"core_problem\": \"Repository-level LLM-based code repair systems use fixed fault-localization granularity (file/function/line) and fixed context budgets, despite growing evidence that the optimal retrieval configuration is instance-dependent. Two April 2026 empirical studies confirm this: arXiv 2604.00167 shows function-level FL beats file- and line-level on average but the ranking shifts across difficulty tiers, and arXiv 2604.05481 finds that file-level context yields 15–17× improvement while line-level expansion causes noise amplification — yet neither proposes an adaptive selection method. Holloway et al. (NeurIPS 2024 ML for Systems Workshop) explicitly call for 'context granularity strategies tailored to specific bug types' but provide no method. Meanwhile, the LLM routing literature has matured rapidly — RouteLLM (ICLR 2025) routes between model tiers using preference data, RADAR (arXiv 2509.25426) routes over model-budget pairs via item-response theory, Route-To-Reason (arXiv 2505.19435) jointly selects models and reasoning strategies, and LTRR (SIGIR 2025 LiveRAG) learns to rank retrievers per query. However, no routing method targets the retrieval configuration (granularity + context budget) for code repair. Triage (arXiv 2604.07494) routes to model tiers using code health metrics but does not touch retrieval configuration. SIADAFIX (arXiv 2510.16059) classifies issues into difficulty modes but operates at fixed FL granularity. The gap: no existing work learns to select (granularity, context budget) per issue for code repair, despite both the routing methodology and the granularity-dependence evidence being well-established independently.\",\n  \"opportunity\": \"The convergence of two threads creates a clear opportunity: (1) empirically validated instance-dependent granularity in code repair (arXiv 2604.00167, 2604.05481, Holloway et al. NeurIPS 2024), and (2) a mature toolkit of routing methods from the LLM efficiency literature (RouteLLM, RADAR, Route-To-Reason, BEST-Route, LTRR). The question is not whether to route, but how to formulate and train a router for this specific problem. The routing literature offers several training paradigms — preference-based pairwise learning (RouteLLM), item-response models (RADAR), learning-to-rank (LTRR), and standard classification — but applying them to retrieval configuration selection for code repair requires: (a) defining the configuration space (granularity × context budget), (b) collecting oracle repair labels across configurations, (c) identifying which input signals predict optimal configurations, and (d) comparing training methods to determine what works for this specific routing target. NL features of issue descriptions (error type, stack trace structure, code entity density, location hint specificity) are available at zero retrieval cost, making them ideal pre-routing signals. Code structural signals (file complexity, coupling) available after cheap initial localization can refine the routing. This dual-signal approach differentiates from Triage (code-only, model-tier target) and SIADAFIX (NL-only, difficulty-mode target). LTRR's finding that pairwise ranking with XGBoost outperforms neural rankers for retriever selection suggests that the training method matters and should be empirically compared rather than assumed — motivating our multi-method ablation design.\",\n  \"landscape\": \"**Granularity-dependence evidence:** Holloway & Elenberg (NeurIPS 2024 ML for Systems Workshop) study 6 context granularities on 109 Defects4J bugs, finding sliced context achieves 79% Correct/Plausible ratio, and explicitly motivate tailored strategies as future work. arXiv 2604.00167 (50 instances, 2 repos) finds function-level at 45.6% vs. file-level at 42.6% with rankings shifting across difficulty tiers. arXiv 2604.05481 (500 instances, 61 configurations) finds file-level context yields 15–17× improvement while line-level expansion amplifies noise, with the most effective strategy combining broad semantic understanding with precise localization.\\n\\n**LLM routing methods:** RouteLLM (ICLR 2025, arXiv 2406.18665) trains 4 router architectures (SW ranking, matrix factorization, BERT classifier, causal LLM classifier) from human preference data to route between strong/weak LLMs; finds simpler methods outperform in low-data regimes but all improve with data augmentation. RADAR (arXiv 2509.25426) uses item-response theory to learn query difficulty and model-budget ability parameters for difficulty-aware routing. BEST-Route (ICML 2025, arXiv 2506.22716) selects both model and sampling count per query, cutting costs by 60% with <1% performance drop. Route-To-Reason (arXiv 2505.19435) jointly routes LLMs and reasoning strategies via compressed representations, achieving >60% token reduction. LTRR (SIGIR 2025 LiveRAG, arXiv 2506.13743) frames retriever selection as learning-to-rank, finding pairwise ranking with XGBoost yields the best results — the closest methodological parallel to our retrieval configuration routing, but in open-domain QA.\\n\\n**Code repair with adaptive components:** Triage (arXiv 2604.07494) routes SWE-bench tasks to cost-effective LLM tiers via 25+ code health metrics — parallel target (routing) but different routing dimension (model tier vs. retrieval config) and different features (code-only). AdaPatcher (AAAI 2025, arXiv 2503.06510) adapts repair via DPO-based preference learning for minimal modifications but at fixed localization. AdaEdit (arXiv 2604.27296) trains LLMs to choose token-efficient output formats via DPO — parallel adaptive concept but for output format. SWEzze (arXiv 2603.28119) trains a cross-encoder reranker for minimal sufficient context at a single fixed granularity. SWE-Pruner (arXiv 2601.16746) performs adaptive context pruning via neural skimming, also at fixed granularity. SIADAFIX (arXiv 2510.16059) classifies issues into difficulty modes via NL features but does not adapt FL granularity or context budget. CodeScout (arXiv 2603.05744) enriches problem statements via pre-exploration, yielding 20% SWE-bench improvement. ARISE (arXiv 2605.03117) builds multi-granularity program graphs with fixed representations.\\n\\n**Preference optimization for retrieval:** RPO (ACL 2025, arXiv 2501.13726) applies DPO-style preference learning to teach LLMs adaptive retrieval leverage in open-domain QA. DRO (arXiv 2505.03075) trains retrieval selection and generation end-to-end.\\n\\n**The gap:** The routing methodology exists (RouteLLM, RADAR, LTRR) and the granularity-dependence evidence exists (arXiv 2604.00167, 2604.05481, Holloway et al.), but no work connects them — learning to route over retrieval configurations for code repair from issue-level signals. This is a problem formulation gap, not a methodology gap, which is why we frame GranRoute as a routing framework that empirically compares training methods rather than proposing a single novel training algorithm.\",\n  \"approach\": \"We propose GranRoute, a retrieval configuration routing framework for code repair that learns to select the optimal (granularity, context budget) pair per issue. GranRoute integrates upstream of any retrieval-based repair pipeline (e.g., Agentless, SWE-agent) as a plug-in routing module.\\n\\n**Phase 1 — Headroom Pilot (2 days):** Run the Agentless pipeline via API (Qwen3-Coder-Next, ~$0.08/instance) across 12 configurations (3 granularities: file/function/line × 4 context budgets: 3, 5, 8, 12 retrieved elements) on 50 SWE-bench Verified instances, 3 runs each (majority-vote labels). Compute the headroom: oracle accuracy (per-instance best config) minus best fixed-config accuracy. Additionally compute the cost-efficiency headroom: average tokens consumed by oracle-selected configs vs. best fixed config. **Go/no-go gate:** If accuracy headroom < 5pp AND cost savings < 20%, the premise is too weak and we pivot to a diagnostic study analyzing *why* configurations fail differently. If accuracy headroom is modest (3–5pp) but cost savings are substantial (>20%), we proceed with a cost-efficiency-focused framing.\\n\\n**Phase 2 — Oracle Collection (3 days):** Extend to 300 SWE-bench Verified instances across the same 12 configurations, 3 runs each (total: 10,800 API calls, ~$864). Each instance receives per-configuration success rates via majority vote, yielding both binary labels and graded scores (0/3, 1/3, 2/3, 3/3). Cost: 10,800 × $0.08 ≈ $864.\\n\\n**Phase 3 — Training Data Construction (1 day):** Construct training data in multiple formats to support different training methods: (a) **Classification labels:** For each instance, assign the best-performing configuration as the class label (with ties broken by cost). (b) **Preference pairs:** For each instance, construct (issue_text, winning_config, losing_config) pairs from success/failure outcomes, yielding ~3,000–5,000 informative pairs. (c) **Graded scores:** Use success rates (0/3, 1/3, 2/3, 3/3) as regression targets. Extract features: NL features from issue text (via encoder), hand-crafted NL features (error-type keywords, stack trace depth, code entity count, description length, location specificity score), and lightweight code-structural features from localized files (cyclomatic complexity, file size, import count, class/function ratio).\\n\\n**Phase 4 — Router Training with Multi-Method Comparison (3 days):** Train and compare 5 routing methods on the same oracle data:\\n(a) **Random forest** on hand-crafted NL+code features — the simplest baseline, motivated by LTRR's finding that XGBoost outperforms neural rankers for retriever selection.\\n(b) **MLP classifier** on CodeSage-base (356M) embeddings — standard neural classification baseline.\\n(c) **Pairwise preference router** on CodeSage-base embeddings with a scoring head trained via Bradley-Terry preference loss — motivated by RouteLLM's preference-based routing paradigm. Maximizes score gap between winning and losing configurations given issue embedding.\\n(d) **Learning-to-rank router** using LambdaMART on combined encoder+hand-crafted features — motivated by LTRR's pairwise ranking approach.\\n(e) **IRT-inspired difficulty router** that learns issue difficulty and configuration ability parameters à la RADAR — routes harder issues to more precise (line-level) configurations.\\nAll methods operate in two variants: NL-only (zero pre-routing cost) and NL+Code (minimal cost after initial file localization). CodeSage-base (ICLR 2024, 356M params) replaces UniXcoder as the primary encoder, with UniXcoder included as an encoder ablation. Training is lightweight: ~8 H100-hours total across all methods.\\n\\n**Phase 5 — Evaluation (3 days):** Evaluate GranRoute on ~100 held-out SWE-bench-Live instances from the 2 most recent monthly batches (decontaminated by construction, as instances post-date all training data). Plan for ~10–15% Docker environment setup failures, targeting 85–90 successfully evaluated instances. Use the full Agentless pipeline. Baselines: (a) best fixed-granularity configuration, (b) random configuration selection, (c) Triage-style code-only routing (retrained on our oracle data), (d) SIADAFIX-style NL difficulty classification adapted for granularity routing, (e) oracle upper bound. Report: end-to-end repair rate, routing accuracy (predicted vs. oracle-optimal config), cost efficiency (tokens consumed per successful repair), and calibration (does the router's confidence correlate with routing accuracy?). Ablation: NL-only vs. NL+Code, CodeSage-base vs. UniXcoder encoder, and the 5-way training method comparison.\\n\\n**Phase 6 — Analysis (concurrent, 2 days):** SHAP-based feature importance analysis on the best-performing router to identify which NL features and code features most influence routing decisions. This provides interpretable insights into how NL bug descriptions predict optimal code comprehension granularity — serving as supporting evidence, not the main contribution.\\n\\n**Addressing the small-headroom scenario:** If the accuracy headroom is modest (5–8pp), we lead with cost-efficiency: GranRoute routes easy issues to cheaper configurations (fewer retrieved elements, coarser granularity) while reserving expensive configurations for hard issues. Even a 3pp accuracy gain with 25%+ cost reduction is a meaningful practical contribution. If the headroom is large (>10pp), we lead with accuracy improvement. The paper's framing adapts to the empirical findings.\\n\\nThe contribution is twofold: (1) **GranRoute**, a configuration routing framework that formalizes retrieval configuration selection for code repair and empirically compares 5 training methods (random forest, MLP, preference, LTR, IRT) with 2 feature families (NL-only, NL+Code) — the first systematic study of routing methods for this target; (2) **Empirical analysis** connecting NL bug features to optimal code comprehension granularity, with interpretable feature importance analysis. The framework is model-agnostic and pipeline-agnostic.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~25–40h H100 (8h for multi-method router training, 10–20h for feature extraction/analysis, 5–10h for ablation experiments; all Agentless runs are API-based)\",\n      \"gpu_utilization\": \"Low (~15–25%). Most compute is API-based. Local GPU used for encoder fine-tuning and analysis.\",\n      \"timeline\": \"14 days (tight for EMNLP ARR May 25 deadline)\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"$75–120\",\n      \"api_cost\": \"$1,100–1,500 (pilot: 1,800 runs × $0.08 ≈ $144; oracle: 10,800 runs × $0.08 ≈ $864; evaluation on SWE-bench-Live: ~100 instances × 12 configs × 3 runs × $0.08 ≈ $288; iteration/debugging: ~$100)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~35–55h H100 (agent explores more router architectures and feature combinations)\",\n      \"gpu_utilization\": \"Low-moderate (~25–35%). Agent queues API runs between check-ins.\",\n      \"timeline\": \"10–12 days\",\n      \"team\": \"1 researcher, ~30min/day for reviewing routing accuracy, validating preference pair quality, approving evaluation plan\",\n      \"claude_api_cost\": \"$100–200 (~1,000–2,000 agent turns)\",\n      \"estimated_gpu_cost\": \"$105–165\",\n      \"api_cost\": \"$1,300–1,800 (more configs explored: 15 configs instead of 12, robustness checks with alternative LLM backends)\",\n      \"risk_note\": \"SWE-bench Docker setup failures on ~10–15% of instances may require human triage. API rate limits mitigated by batching.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~70–130h H100 (agent explores neural router variants, multiple encoder backbones, extensive ablations)\",\n      \"gpu_utilization\": \"Moderate (~35–50%). Agent interleaves API calls with local training runs.\",\n      \"timeline\": \"8–10 days\",\n      \"team\": \"0 (only initial setup: SWE-bench Docker, API keys, Agentless installation)\",\n      \"claude_api_cost\": \"$250–500 (~2,500–5,000 agent turns)\",\n      \"estimated_gpu_cost\": \"$210–390\",\n      \"api_cost\": \"$1,700–2,600 (agent explores 18+ configs, multiple LLM backends, cross-benchmark evaluation)\",\n      \"speed_bottleneck\": \"API rate limits and SWE-bench Docker setup (~2min/container). Oracle collection is embarrassingly parallel via API but gated by provider throughput.\",\n      \"risk_note\": \"Agent may over-engineer the router architecture when simpler methods (random forest, LambdaMART) may suffice. May also drift toward optimizing repair rate rather than validating the routing framework's comparative contribution.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 short paper via ARR May cycle (submission: May 25, 2026; must select EMNLP at submission time) — tight 14-day window, feasible for focused 4-page method paper under 'NLP and Code Models' track\",\n    \"ICSE 2027 Research Track (abstract: June 23, 2026; paper: June 30, 2026) — comfortable timeline for full-length version with expanded evaluation and ablations\",\n    \"AAAI 2027 (abstract: July 25, 2026; paper: August 1, 2026) — suits the routing/configuration learning angle\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Holloway & Elenberg, 'On the Role of Context Granularity in LLM-Driven Program Repair' (NeurIPS 2024 ML for Systems Workshop) — studies 6 granularities, explicitly motivates tailored strategies as future work\",\n    \"RouteLLM: Learning to Route LLMs with Preference Data (ICLR 2025, arXiv 2406.18665) — trains 4 router types from preference data for model selection; closest methodological parallel (preference data → router), different routing target\",\n    \"RADAR: Reasoning-Ability and Difficulty-Aware Routing for Reasoning LLMs (arXiv 2509.25426) — IRT-based difficulty-aware routing over model-budget pairs; inspires our IRT-baseline variant\",\n    \"BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute (ICML 2025, arXiv 2506.22716) — routes model + sampling count based on query difficulty\",\n    \"Route-To-Reason: Adaptive Routing for LLM and Reasoning Strategy Selection (arXiv 2505.19435) — jointly routes models and reasoning strategies; closest conceptual parallel (strategy routing)\",\n    \"LTRR: Learning To Rank Retrievers for LLMs (SIGIR 2025 LiveRAG, arXiv 2506.13743) — frames retriever selection as learning-to-rank, finds XGBoost outperforms neural rankers; motivates our multi-method comparison\",\n    \"Triage: Routing Software Engineering Tasks to Cost-Effective LLM Tiers via Code Quality Signals (arXiv 2604.07494, April 2026) — ML classifier routing to model tiers via code health metrics\",\n    \"A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks (arXiv 2604.00167, April 2026) — function-level at 45.6% vs file-level at 42.6%, rankings shift across difficulty tiers\",\n    \"On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481, April 2026) — 61 configurations on 500 instances, noise amplification from line-level expansion\",\n    \"To Diff or Not to Diff: AdaEdit for Adaptive Output Formats in LLM-based Code Editing (arXiv 2604.27296, April 2026) — DPO-trained adaptive format selection\",\n    \"RPO: Retrieval Preference Optimization for Robust RAG (ACL 2025, arXiv 2501.13726) — DPO-style preference learning for adaptive retrieval leverage\",\n    \"Direct Retrieval-augmented Optimization: Synergizing Knowledge Selection and Language Models (arXiv 2505.03075, 2025)\",\n    \"AdaPatcher: Less is More — Adaptive Program Repair with Bug Localization and Preference Learning (AAAI 2025 oral, arXiv 2503.06510)\",\n    \"CodeSage: Code Representation Learning At Scale (ICLR 2024) — modern code encoder (130M–1.3B params), replaces UniXcoder as primary encoder\",\n    \"ORACLE-SWE: Quantifying the Contribution of Oracle Information Signals on SWE Agents (arXiv 2604.07789, April 2026) — quantifies headroom from oracle-quality signals in SWE-bench\",\n    \"CodeScout: Contextual Problem Statement Enhancement for Software Agents (arXiv 2603.05744, 2026)\",\n    \"RGFL: Reasoning Guided Fault Localization for APR Using LLMs (arXiv 2601.18044, 2026)\",\n    \"ARISE: A Repository-level Graph Representation for Agentic FL and Repair (arXiv 2605.03117, 2026)\",\n    \"SWEzze: Compressing Code Context for LLM-based Issue Resolution (arXiv 2603.28119, 2026)\",\n    \"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents (arXiv 2601.16746, 2026)\",\n    \"SIADAFIX: Issue Description Response for Adaptive Program Repair (arXiv 2510.16059, 2025)\",\n    \"SWE-bench Goes Live! (NeurIPS 2025 D&B, arXiv 2505.23419)\",\n    \"Agentless: Demystifying LLM-based Software Engineering Agents (FSE 2025)\",\n    \"Lost in the Middle: How Language Models Use Long Contexts (TACL 2024)\",\n    \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model (NeurIPS 2023)\",\n    \"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330)\"\n  ],\n  \"description\": \"Existing retrieval-based LLM code repair systems use fixed fault-localization granularity and context budgets, despite evidence that optimal configuration is instance-dependent (arXiv 2604.00167, 2604.05481). The LLM routing literature (RouteLLM ICLR 2025, RADAR, LTRR SIGIR 2025) provides mature training paradigms but none target retrieval configuration for code repair. We propose GranRoute, a configuration routing framework that learns to select the optimal (granularity, context budget) per issue. We collect oracle repair labels by running Agentless across 12 configurations on 300 SWE-bench Verified instances (10,800 API calls at ~$0.08/run ≈ $864), then systematically compare 5 training methods — random forest, MLP classifier, Bradley-Terry preference router, LambdaMART ranking, and IRT-based difficulty model — to determine what works best for this routing target. This multi-method comparison directly addresses whether preference-based training (à la RouteLLM) outperforms simpler classifiers for configuration routing, or whether tree-based methods dominate (as LTRR found for retriever selection). GranRoute operates in two stages: (1) NL-only pre-routing using issue text (zero retrieval cost), and (2) optional refinement with code-structural signals after initial file localization. We use CodeSage-base (ICLR 2024, 356M) as the primary encoder with UniXcoder as ablation. We evaluate on ~100 decontaminated SWE-bench-Live instances from the 2 most recent monthly batches against fixed-configuration baselines, Triage-style code-only routing, and oracle upper bound. A 50-instance headroom pilot serves as go/no-go gate: if oracle advantage over best fixed config is <5pp accuracy AND <20% cost savings, we pivot. If accuracy headroom is modest but cost savings are substantial, we lead with cost-efficiency. The contribution is twofold: (1) GranRoute, the first configuration routing framework for code repair with a systematic comparison of 5 training methods and 2 feature families, (2) interpretable analysis connecting NL bug features to optimal code comprehension granularity. All oracle profiling is API-based (~$1,200 total, <40 H100-hours GPU). Primary target: EMNLP 2026 short paper (ARR May 25); extended version for ICSE 2027.\",\n  \"project_name\": \"adaptive_context_orchestration\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"FATAL: Compute budget violation — proposal minimum (600-800 A100-hours ≈ 300-400 H100-equiv) is 2-4x the user's hard constraint of ≤200 H100-hours. Oracle profiling of 18 configs × 200+ instances with a self-hosted 80B model is the dominant cost and cannot be reduced without fundamentally changing the approach.\", \"FATAL: Timeline violation — manual estimate is 4-6 months, human-in-loop is 6-10 weeks, even auto mode is 10-18 days with 4× A100s. The 16-day constraint is incompatible with exhaustive oracle profiling.\", \"Poor EMNLP venue fit — the contribution is repair pipeline orchestration (an SE topic), not NLP/code understanding. The ML component (fine-tuning a 0.6B cross-encoder for 18-way classification) is too thin for an NLP venue. This work fits ICSE/ASE/FSE far better.\", \"Missing key competitor: AdaPatcher (AAAI 2025 oral, arXiv 2503.06510) — an adaptive program repair method with learned bug localization and preference learning — was not cited or discussed in the landscape.\", \"Oracle label noise: the Agentless pipeline has inherent randomness (temperature, sampling). Single runs per (config, instance) pair yield noisy training labels. Multiple runs per config would further inflate compute costs.\", \"Weak empirical foundation: the function-level FL granularity study (arXiv 2604.00167) was conducted on SWE-bench Mini (only 50 instances). Extrapolating that adaptive granularity selection will yield significant gains on the full 500-instance Verified set is speculative.\", \"SWE-bench Verified contamination: OpenAI's audit confirmed frontier models are contaminated on this benchmark, and 59.4% of hard tasks have flawed tests. Using it for both oracle label collection AND evaluation creates validity concerns.\", \"Overlap with SWEzze: the proposal uses the same base model (Qwen3-Reranker-0.6B) and same general approach (train a cross-encoder to select context) as SWEzze. The delta is adding granularity selection, which may not justify a separate paper at a top venue.\"]\nFeedback: The core insight (adaptive granularity + context budget selection) is sound but the execution plan fundamentally violates the user's constraints. To make this viable for EMNLP 2026 within ≤200 H100-hours and ≤16 days, the generator must: (1) **Eliminate exhaustive oracle profiling** — instead of running 18 configs × N instances, use a much cheaper proxy: analyze the already-published results from arXiv 2604.00167 and 2604.05481 to derive heuristic-based labels, or use a small pilot (3-5 configs × 50 instances) with API-based models (not self-hosted 80B) to collect training signal. (2) **Reframe for EMNLP** — the current framing is SE-centric (fault localization, repair pipelines). To fit EMNLP's 'NLP and Code Models' track, reframe around code understanding: how do LLMs process code at different granularities? What structural features of code predict optimal context? This shifts from pipeline engineering to understanding LLM code comprehension. (3) **Cite AdaPatcher (AAAI 2025)** and SWE-ContextBench (arXiv 2602.08316) in the landscape. (4) **Use API-based models for oracle collection** (e.g., Qwen3-Coder-Next via API at ~$0.30/instance) instead of self-hosting, converting GPU cost to manageable API cost. (5) **Address SWE-bench contamination** — consider using SWE-bench-Live or SWE-rebench for evaluation instead of Verified. (6) **Reduce scope** — rather than a full learned policy with RL fine-tuning, consider a simpler but more insightful contribution: a systematic empirical study of what bug features predict optimal granularity, with a lightweight rule-based or logistic-regression selector. This is more achievable in 16 days and more publishable at EMNLP if paired with analysis of LLM code understanding at different granularities.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL: Contribution type mismatch — the user explicitly required 'METHOD ONLY: new training methods, retrieval-augmented code repair, or inference algorithms for code tasks.' This proposal self-describes as a 'large-scale empirical study' with a 'lightweight interpretable predictor' (logistic regression/GBDT). A logistic regression on hand-crafted features is not a new training method, retrieval-augmented repair, or inference algorithm. This fundamentally violates the user's requirements.\", \"CRITICAL: Missing competitor — Triage (arXiv 2604.07494, April 2026) trains an ML classifier to route SWE-bench tasks to cost-effective LLM tiers based on code quality signals. The methodology is nearly identical: lightweight classifier + pre-computed features → select optimal configuration. The only differences are feature source (code health metrics vs. NL features) and target variable (model tier vs. granularity/budget). This paper was not cited or discussed.\", \"Missing competitor — Holloway et al., 'On the Role of Context Granularity in LLM-Driven Program Repair' (NeurIPS 2024 ML for Systems Workshop), which studies 6 context granularities including backward static slicing on Defects4J and explicitly calls for 'future work should explore context granularity strategies tailored to specific bug types.' This is exactly the proposed work's research question, already articulated as a future direction.\", \"Missing competitor — AdaEdit/To Diff or Not to Diff (arXiv 2604.27296, April 2026) trains LLMs to dynamically choose the most token-efficient output format based on task features. Parallel concept: using task features to adaptively select configuration for downstream code operations.\", \"Arithmetic error in API cost: 9 configs × 300 instances × 3 runs × $0.30 = $2,430, not the claimed $810. The factor-of-3 error (seemingly forgetting the '× 3 runs') propagates into the total budget estimates. While per-instance costs with Qwen3-Coder-Next may be lower than $0.30, the stated math is wrong and undermines cost credibility.\", \"Terminology misattribution: The proposal attributes 'context rot' to arXiv 2604.05481, but that paper actually describes 'noise amplification' from line-level expansion. 'Context rot' is attributed to Chroma Research 2025, a separate source. The conflation weakens the theoretical framing.\", \"Small training set concern: 300 instances split into train/test (say 200/100) with 9 configuration labels, where many features are sparse (e.g., stack trace presence may be binary), may yield an underpowered feature analysis. SHAP values and mutual information on ~200 training instances with ~7 features and 9 target classes may not produce statistically robust insights.\", \"Uncertain headroom: If the best fixed configuration (e.g., function-level + 6 elements) already resolves 70-80% of what the oracle resolves, the predictor's improvement ceiling is narrow. The proposal does not estimate this headroom or discuss what happens if it is small.\"]\nFeedback: The core research question (what NL features predict optimal code context?) has merit, but the execution plan mismatches the user's requirements in a fundamental way. To make this viable:\n\n1. **Transform from empirical study to METHOD.** The user asked for 'new training methods, retrieval-augmented code repair, or inference algorithms.' Instead of a post-hoc empirical study + logistic regression, design a retrieval-augmented repair method that dynamically adapts its retrieval granularity and context budget during inference. For example: a meta-controller that encodes the NL issue description, predicts a retrieval configuration, executes retrieval at the predicted granularity, and feeds the result to the repair model — trained end-to-end (or via RL/DPO) to maximize repair success. This would be a genuine method contribution. The empirical analysis of NL features becomes a supporting analysis section, not the main contribution.\n\n2. **Cite and differentiate from Triage (arXiv 2604.07494).** This April 2026 paper does the same thing with code features → model tier. You must show why NL features for granularity/budget selection is a distinct and valuable contribution. The strongest argument: NL features are available before any code retrieval, enabling zero-cost pre-routing.\n\n3. **Cite Holloway et al. (NeurIPS 2024 Workshop)** which explicitly motivated this direction.\n\n4. **Fix the arithmetic.** 9 × 300 × 3 × $0.30 = $2,430, not $810. If Qwen3-Coder-Next actually costs ~$0.05/instance, state that directly.\n\n5. **Estimate the improvement headroom** by first running the 3 granularity configs on a pilot (50 instances) to see how much variance there is in which config wins. If one config dominates (>80% of instances), adaptive selection has limited value and the paper's premise weakens.\n\n6. **For EMNLP venue fit,** the method version (point 1) is much stronger than an empirical study. Frame around how LLMs comprehend code at different abstraction levels and how NL signals can steer this comprehension — this is genuinely an NLP question.\n\n7. **Consider combining NL and code features** to differentiate from both SIADAFIX (NL, LLM classifier) and Triage (code, ML classifier). A lightweight model that uses both feature families, available at different stages of the pipeline, could be a stronger contribution.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"IMPORTANT: Missing justification for DPO over classification — the proposal frames this as 'configuration preference learning' using DPO-style loss, but the task is essentially 9-class configuration prediction from features. The evaluation plan lacks an ablation comparing DPO preference learning against simpler multi-class classification (e.g., random forest, logistic regression, or even a simple MLP classifier trained on oracle labels). Without this comparison, the DPO framing appears to be methodological window-dressing rather than a substantive contribution. RouteLLM (arXiv 2406.18665) showed that preference data can train effective routers, but it also demonstrated that simpler classifiers can perform comparably in certain regimes.\", \"Missing methodological competitors — RouteLLM (arXiv 2406.18665, ICML 2025) trains LLM routers from preference data, which is the identical training paradigm applied to a different routing target (model selection vs. config selection). RADAR (arXiv 2509.25426) is a difficulty-aware routing framework for reasoning LLMs using learned item-response models. Both should be cited and differentiated to strengthen the methodological positioning.\", \"Three contributions may be too many for a 4-page short paper — 'the method,' 'the design,' and 'the insight' are partially overlapping (the design IS the method). Consider consolidating to: (1) the DPO-trained configuration router as the method contribution, (2) the empirical analysis connecting NL features to optimal granularity as supporting evidence. The two-stage NL→NL+Code architecture is a design choice within the method, not a standalone contribution.\", \"Headroom quantification is deferred — the proposal correctly includes a go/no-go gate, but the paper's entire premise rests on the oracle advantage being ≥5pp over best fixed config. The arXiv 2604.00167 study (50 instances, 2 repos) found function-level at 45.6% vs. file-level at 42.6% — only a 3pp gap between best and worst fixed configs, with per-instance variance not quantified as an oracle bound. The headroom may be too small for meaningful routing improvement.\", \"SWE-bench-Live evaluation details are underspecified — the proposal says 'held-out SWE-bench-Live instances' but doesn't specify: how many instances will be used, which subset/time period, whether Docker environments are available for all instances, or how to handle the ~10-15% setup failure rate. SWE-bench-Live's automated curation pipeline may produce instances of varying difficulty distribution from the training set (SWE-bench Verified).\", \"UniXcoder (2022) encoder choice — while adequate, UniXcoder is 4 years old. More recent code encoders (CodeSage 2024, StarEncoder, or even a frozen Qwen2.5-Coder-1.5B as encoder) may provide better issue text representations. The choice should be justified or an encoder ablation included.\"]\nFeedback: The proposal has improved substantially from Round 2 — it's now a proper method contribution with realistic costs and a genuine gap. To push this to pass quality:\n\n1. **Add a DPO-vs-classification ablation.** This is the single most important missing piece. If a simple random forest on the same features performs comparably to the DPO-trained UniXcoder router, the 'preference learning' framing collapses into standard classification. Include at minimum: (a) random forest on NL+code features, (b) MLP classifier on UniXcoder embeddings, (c) your DPO preference router. If DPO wins, explain why (handles noisy/partial orderings better? learns from relative rather than absolute signals?). If it doesn't, the paper's main selling point is undermined.\n\n2. **Cite RouteLLM and RADAR.** RouteLLM (Ong et al., ICML 2025) is the closest methodological parallel — it trains routers from preference data, just for model selection instead of config selection. RADAR (arXiv 2509.25426) uses item-response theory for difficulty-aware routing. Both strengthen your related work section and help position your contribution.\n\n3. **Consolidate to 2 contributions** for the short paper: (1) the configuration preference learning method (encompassing the two-stage design), (2) the empirical analysis of which NL/code features predict optimal granularity. Three separate contributions in 4 pages will feel thin on each.\n\n4. **Run the headroom pilot FIRST**, then write the paper around the actual numbers. If headroom is 5-8pp, discuss the cost-efficiency angle (routing saves API cost by avoiding expensive configs). If headroom is >10pp, lead with accuracy improvement. The framing should adapt to the data.\n\n5. **Specify SWE-bench-Live evaluation**: target ~100-200 instances from the most recent monthly batch (to ensure decontamination), confirm Docker environment availability, and plan for the ~10-15% setup failure rate.\n\n6. **Discuss the minimal-headroom scenario** in the paper: if the oracle advantage is small, argue that the routing still provides value through cost efficiency (cheaper configs for easy instances) even if accuracy gains are modest. This makes the contribution robust to disappointing headroom numbers.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-11T23:36:00.309Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-11T23:36:00.309Z",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

## Round 1

57 recorded events

### User

_source line 3 · 2026-05-11T23:36:00.364Z_

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

## Idea under review (round 4/10)
{
  "title": "GranRoute: Learning to Route Retrieval Configurations for Repository-Level Code Repair",
  "core_problem": "Repository-level LLM-based code repair systems use fixed fault-localization granularity (file/function/line) and fixed context budgets, despite growing evidence that the optimal retrieval configuration is instance-dependent. Two April 2026 empirical studies confirm this: arXiv 2604.00167 shows function-level FL beats file- and line-level on average but the ranking shifts across difficulty tiers, and arXiv 2604.05481 finds that file-level context yields 15–17× improvement while line-level expansion causes noise amplification — yet neither proposes an adaptive selection method. Holloway et al. (NeurIPS 2024 ML for Systems Workshop) explicitly call for 'context granularity strategies tailored to specific bug types' but provide no method. Meanwhile, the LLM routing literature has matured rapidly — RouteLLM (ICLR 2025) routes between model tiers using preference data, RADAR (arXiv 2509.25426) routes over model-budget pairs via item-response theory, Route-To-Reason (arXiv 2505.19435) jointly selects models and reasoning strategies, and LTRR (SIGIR 2025 LiveRAG) learns to rank retrievers per query. However, no routing method targets the retrieval configuration (granularity + context budget) for code repair. Triage (arXiv 2604.07494) routes to model tiers using code health metrics but does not touch retrieval configuration. SIADAFIX (arXiv 2510.16059) classifies issues into difficulty modes but operates at fixed FL granularity. The gap: no existing work learns to select (granularity, context budget) per issue for code repair, despite both the routing methodology and the granularity-dependence evidence being well-established independently.",
  "opportunity": "The convergence of two threads creates a clear opportunity: (1) empirically validated instance-dependent granularity in code repair (arXiv 2604.00167, 2604.05481, Holloway et al. NeurIPS 2024), and (2) a mature toolkit of routing methods from the LLM efficiency literature (RouteLLM, RADAR, Route-To-Reason, BEST-Route, LTRR). The question is not whether to route, but how to formulate and train a router for this specific problem. The routing literature offers several training paradigms — preference-based pairwise learning (RouteLLM), item-response models (RADAR), learning-to-rank (LTRR), and standard classification — but applying them to retrieval configuration selection for code repair requires: (a) defining the configuration space (granularity × context budget), (b) collecting oracle repair labels across configurations, (c) identifying which input signals predict optimal configurations, and (d) comparing training methods to determine what works for this specific routing target. NL features of issue descriptions (error type, stack trace structure, code entity density, location hint specificity) are available at zero retrieval cost, making them ideal pre-routing signals. Code structural signals (file complexity, coupling) available after cheap initial localization can refine the routing. This dual-signal approach differentiates from Triage (code-only, model-tier target) and SIADAFIX (NL-only, difficulty-mode target). LTRR's finding that pairwise ranking with XGBoost outperforms neural rankers for retriever selection suggests that the training method matters and should be empirically compared rather than assumed — motivating our multi-method ablation design.",
  "landscape": "**Granularity-dependence evidence:** Holloway & Elenberg (NeurIPS 2024 ML for Systems Workshop) study 6 context granularities on 109 Defects4J bugs, finding sliced context achieves 79% Correct/Plausible ratio, and explicitly motivate tailored strategies as future work. arXiv 2604.00167 (50 instances, 2 repos) finds function-level at 45.6% vs. file-level at 42.6% with rankings shifting across difficulty tiers. arXiv 2604.05481 (500 instances, 61 configurations) finds file-level context yields 15–17× improvement while line-level expansion amplifies noise, with the most effective strategy combining broad semantic understanding with precise localization.\n\n**LLM routing methods:** RouteLLM (ICLR 2025, arXiv 2406.18665) trains 4 router architectures (SW ranking, matrix factorization, BERT classifier, causal LLM classifier) from human preference data to route between strong/weak LLMs; finds simpler methods outperform in low-data regimes but all improve with data augmentation. RADAR (arXiv 2509.25426) uses item-response theory to learn query difficulty and model-budget ability parameters for difficulty-aware routing. BEST-Route (ICML 2025, arXiv 2506.22716) selects both model and sampling count per query, cutting costs by 60% with <1% performance drop. Route-To-Reason (arXiv 2505.19435) jointly routes LLMs and reasoning strategies via compressed representations, achieving >60% token reduction. LTRR (SIGIR 2025 LiveRAG, arXiv 2506.13743) frames retriever selection as learning-to-rank, finding pairwise ranking with XGBoost yields the best results — the closest methodological parallel to our retrieval configuration routing, but in open-domain QA.\n\n**Code repair with adaptive components:** Triage (arXiv 2604.07494) routes SWE-bench tasks to cost-effective LLM tiers via 25+ code health metrics — parallel target (routing) but different routing dimension (model tier vs. retrieval config) and different features (code-only). AdaPatcher (AAAI 2025, arXiv 2503.06510) adapts repair via DPO-based preference learning for minimal modifications but at fixed localization. AdaEdit (arXiv 2604.27296) trains LLMs to choose token-efficient output formats via DPO — parallel adaptive concept but for output format. SWEzze (arXiv 2603.28119) trains a cross-encoder reranker for minimal sufficient context at a single fixed granularity. SWE-Pruner (arXiv 2601.16746) performs adaptive context pruning via neural skimming, also at fixed granularity. SIADAFIX (arXiv 2510.16059) classifies issues into difficulty modes via NL features but does not adapt FL granularity or context budget. CodeScout (arXiv 2603.05744) enriches problem statements via pre-exploration, yielding 20% SWE-bench improvement. ARISE (arXiv 2605.03117) builds multi-granularity program graphs with fixed representations.\n\n**Preference optimization for retrieval:** RPO (ACL 2025, arXiv 2501.13726) applies DPO-style preference learning to teach LLMs adaptive retrieval leverage in open-domain QA. DRO (arXiv 2505.03075) trains retrieval selection and generation end-to-end.\n\n**The gap:** The routing methodology exists (RouteLLM, RADAR, LTRR) and the granularity-dependence evidence exists (arXiv 2604.00167, 2604.05481, Holloway et al.), but no work connects them — learning to route over retrieval configurations for code repair from issue-level signals. This is a problem formulation gap, not a methodology gap, which is why we frame GranRoute as a routing framework that empirically compares training methods rather than proposing a single novel training algorithm.",
  "approach": "We propose GranRoute, a retrieval configuration routing framework for code repair that learns to select the optimal (granularity, context budget) pair per issue. GranRoute integrates upstream of any retrieval-based repair pipeline (e.g., Agentless, SWE-agent) as a plug-in routing module.\n\n**Phase 1 — Headroom Pilot (2 days):** Run the Agentless pipeline via API (Qwen3-Coder-Next, ~$0.08/instance) across 12 configurations (3 granularities: file/function/line × 4 context budgets: 3, 5, 8, 12 retrieved elements) on 50 SWE-bench Verified instances, 3 runs each (majority-vote labels). Compute the headroom: oracle accuracy (per-instance best config) minus best fixed-config accuracy. Additionally compute the cost-efficiency headroom: average tokens consumed by oracle-selected configs vs. best fixed config. **Go/no-go gate:** If accuracy headroom < 5pp AND cost savings < 20%, the premise is too weak and we pivot to a diagnostic study analyzing *why* configurations fail differently. If accuracy headroom is modest (3–5pp) but cost savings are substantial (>20%), we proceed with a cost-efficiency-focused framing.\n\n**Phase 2 — Oracle Collection (3 days):** Extend to 300 SWE-bench Verified instances across the same 12 configurations, 3 runs each (total: 10,800 API calls, ~$864). Each instance receives per-configuration success rates via majority vote, yielding both binary labels and graded scores (0/3, 1/3, 2/3, 3/3). Cost: 10,800 × $0.08 ≈ $864.\n\n**Phase 3 — Training Data Construction (1 day):** Construct training data in multiple formats to support different training methods: (a) **Classification labels:** For each instance, assign the best-performing configuration as the class label (with ties broken by cost). (b) **Preference pairs:** For each instance, construct (issue_text, winning_config, losing_config) pairs from success/failure outcomes, yielding ~3,000–5,000 informative pairs. (c) **Graded scores:** Use success rates (0/3, 1/3, 2/3, 3/3) as regression targets. Extract features: NL features from issue text (via encoder), hand-crafted NL features (error-type keywords, stack trace depth, code entity count, description length, location specificity score), and lightweight code-structural features from localized files (cyclomatic complexity, file size, import count, class/function ratio).\n\n**Phase 4 — Router Training with Multi-Method Comparison (3 days):** Train and compare 5 routing methods on the same oracle data:\n(a) **Random forest** on hand-crafted NL+code features — the simplest baseline, motivated by LTRR's finding that XGBoost outperforms neural rankers for retriever selection.\n(b) **MLP classifier** on CodeSage-base (356M) embeddings — standard neural classification baseline.\n(c) **Pairwise preference router** on CodeSage-base embeddings with a scoring head trained via Bradley-Terry preference loss — motivated by RouteLLM's preference-based routing paradigm. Maximizes score gap between winning and losing configurations given issue embedding.\n(d) **Learning-to-rank router** using LambdaMART on combined encoder+hand-crafted features — motivated by LTRR's pairwise ranking approach.\n(e) **IRT-inspired difficulty router** that learns issue difficulty and configuration ability parameters à la RADAR — routes harder issues to more precise (line-level) configurations.\nAll methods operate in two variants: NL-only (zero pre-routing cost) and NL+Code (minimal cost after initial file localization). CodeSage-base (ICLR 2024, 356M params) replaces UniXcoder as the primary encoder, with UniXcoder included as an encoder ablation. Training is lightweight: ~8 H100-hours total across all methods.\n\n**Phase 5 — Evaluation (3 days):** Evaluate GranRoute on ~100 held-out SWE-bench-Live instances from the 2 most recent monthly batches (decontaminated by construction, as instances post-date all training data). Plan for ~10–15% Docker environment setup failures, targeting 85–90 successfully evaluated instances. Use the full Agentless pipeline. Baselines: (a) best fixed-granularity configuration, (b) random configuration selection, (c) Triage-style code-only routing (retrained on our oracle data), (d) SIADAFIX-style NL difficulty classification adapted for granularity routing, (e) oracle upper bound. Report: end-to-end repair rate, routing accuracy (predicted vs. oracle-optimal config), cost efficiency (tokens consumed per successful repair), and calibration (does the router's confidence correlate with routing accuracy?). Ablation: NL-only vs. NL+Code, CodeSage-base vs. UniXcoder encoder, and the 5-way training method comparison.\n\n**Phase 6 — Analysis (concurrent, 2 days):** SHAP-based feature importance analysis on the best-performing router to identify which NL features and code features most influence routing decisions. This provides interpretable insights into how NL bug descriptions predict optimal code comprehension granularity — serving as supporting evidence, not the main contribution.\n\n**Addressing the small-headroom scenario:** If the accuracy headroom is modest (5–8pp), we lead with cost-efficiency: GranRoute routes easy issues to cheaper configurations (fewer retrieved elements, coarser granularity) while reserving expensive configurations for hard issues. Even a 3pp accuracy gain with 25%+ cost reduction is a meaningful practical contribution. If the headroom is large (>10pp), we lead with accuracy improvement. The paper's framing adapts to the empirical findings.\n\nThe contribution is twofold: (1) **GranRoute**, a configuration routing framework that formalizes retrieval configuration selection for code repair and empirically compares 5 training methods (random forest, MLP, preference, LTR, IRT) with 2 feature families (NL-only, NL+Code) — the first systematic study of routing methods for this target; (2) **Empirical analysis** connecting NL bug features to optimal code comprehension granularity, with interpretable feature importance analysis. The framework is model-agnostic and pipeline-agnostic.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~25–40h H100 (8h for multi-method router training, 10–20h for feature extraction/analysis, 5–10h for ablation experiments; all Agentless runs are API-based)",
      "gpu_utilization": "Low (~15–25%). Most compute is API-based. Local GPU used for encoder fine-tuning and analysis.",
      "timeline": "14 days (tight for EMNLP ARR May 25 deadline)",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "$75–120",
      "api_cost": "$1,100–1,500 (pilot: 1,800 runs × $0.08 ≈ $144; oracle: 10,800 runs × $0.08 ≈ $864; evaluation on SWE-bench-Live: ~100 instances × 12 configs × 3 runs × $0.08 ≈ $288; iteration/debugging: ~$100)"
    },
    "human_in_loop": {
      "gpu_hours": "~35–55h H100 (agent explores more router architectures and feature combinations)",
      "gpu_utilization": "Low-moderate (~25–35%). Agent queues API runs between check-ins.",
      "timeline": "10–12 days",
      "team": "1 researcher, ~30min/day for reviewing routing accuracy, validating preference pair quality, approving evaluation plan",
      "claude_api_cost": "$100–200 (~1,000–2,000 agent turns)",
      "estimated_gpu_cost": "$105–165",
      "api_cost": "$1,300–1,800 (more configs explored: 15 configs instead of 12, robustness checks with alternative LLM backends)",
      "risk_note": "SWE-bench Docker setup failures on ~10–15% of instances may require human triage. API rate limits mitigated by batching."
    },
    "auto_research": {
      "gpu_hours": "~70–130h H100 (agent explores neural router variants, multiple encoder backbones, extensive ablations)",
      "gpu_utilization": "Moderate (~35–50%). Agent interleaves API calls with local training runs.",
      "timeline": "8–10 days",
      "team": "0 (only initial setup: SWE-bench Docker, API keys, Agentless installation)",
      "claude_api_cost": "$250–500 (~2,500–5,000 agent turns)",
      "estimated_gpu_cost": "$210–390",
      "api_cost": "$1,700–2,600 (agent explores 18+ configs, multiple LLM backends, cross-benchmark evaluation)",
      "speed_bottleneck": "API rate limits and SWE-bench Docker setup (~2min/container). Oracle collection is embarrassingly parallel via API but gated by provider throughput.",
      "risk_note": "Agent may over-engineer the router architecture when simpler methods (random forest, LambdaMART) may suffice. May also drift toward optimizing repair rate rather than validating the routing framework's comparative contribution."
    }
  },
  "target_venues": [
    "EMNLP 2026 short paper via ARR May cycle (submission: May 25, 2026; must select EMNLP at submission time) — tight 14-day window, feasible for focused 4-page method paper under 'NLP and Code Models' track",
    "ICSE 2027 Research Track (abstract: June 23, 2026; paper: June 30, 2026) — comfortable timeline for full-length version with expanded evaluation and ablations",
    "AAAI 2027 (abstract: July 25, 2026; paper: August 1, 2026) — suits the routing/configuration learning angle"
  ],
  "level": "solid",
  "key_references": [
    "Holloway & Elenberg, 'On the Role of Context Granularity in LLM-Driven Program Repair' (NeurIPS 2024 ML for Systems Workshop) — studies 6 granularities, explicitly motivates tailored strategies as future work",
    "RouteLLM: Learning to Route LLMs with Preference Data (ICLR 2025, arXiv 2406.18665) — trains 4 router types from preference data for model selection; closest methodological parallel (preference data → router), different routing target",
    "RADAR: Reasoning-Ability and Difficulty-Aware Routing for Reasoning LLMs (arXiv 2509.25426) — IRT-based difficulty-aware routing over model-budget pairs; inspires our IRT-baseline variant",
    "BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute (ICML 2025, arXiv 2506.22716) — routes model + sampling count based on query difficulty",
    "Route-To-Reason: Adaptive Routing for LLM and Reasoning Strategy Selection (arXiv 2505.19435) — jointly routes models and reasoning strategies; closest conceptual parallel (strategy routing)",
    "LTRR: Learning To Rank Retrievers for LLMs (SIGIR 2025 LiveRAG, arXiv 2506.13743) — frames retriever selection as learning-to-rank, finds XGBoost outperforms neural rankers; motivates our multi-method comparison",
    "Triage: Routing Software Engineering Tasks to Cost-Effective LLM Tiers via Code Quality Signals (arXiv 2604.07494, April 2026) — ML classifier routing to model tiers via code health metrics",
    "A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks (arXiv 2604.00167, April 2026) — function-level at 45.6% vs file-level at 42.6%, rankings shift across difficulty tiers",
    "On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481, April 2026) — 61 configurations on 500 instances, noise amplification from line-level expansion",
    "To Diff or Not to Diff: AdaEdit for Adaptive Output Formats in LLM-based Code Editing (arXiv 2604.27296, April 2026) — DPO-trained adaptive format selection",
    "RPO: Retrieval Preference Optimization for Robust RAG (ACL 2025, arXiv 2501.13726) — DPO-style preference learning for adaptive retrieval leverage",
    "Direct Retrieval-augmented Optimization: Synergizing Knowledge Selection and Language Models (arXiv 2505.03075, 2025)",
    "AdaPatcher: Less is More — Adaptive Program Repair with Bug Localization and Preference Learning (AAAI 2025 oral, arXiv 2503.06510)",
    "CodeSage: Code Representation Learning At Scale (ICLR 2024) — modern code encoder (130M–1.3B params), replaces UniXcoder as primary encoder",
    "ORACLE-SWE: Quantifying the Contribution of Oracle Information Signals on SWE Agents (arXiv 2604.07789, April 2026) — quantifies headroom from oracle-quality signals in SWE-bench",
    "CodeScout: Contextual Problem Statement Enhancement for Software Agents (arXiv 2603.05744, 2026)",
    "RGFL: Reasoning Guided Fault Localization for APR Using LLMs (arXiv 2601.18044, 2026)",
    "ARISE: A Repository-level Graph Representation for Agentic FL and Repair (arXiv 2605.03117, 2026)",
    "SWEzze: Compressing Code Context for LLM-based Issue Resolution (arXiv 2603.28119, 2026)",
    "SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents (arXiv 2601.16746, 2026)",
    "SIADAFIX: Issue Description Response for Adaptive Program Repair (arXiv 2510.16059, 2025)",
    "SWE-bench Goes Live! (NeurIPS 2025 D&B, arXiv 2505.23419)",
    "Agentless: Demystifying LLM-based Software Engineering Agents (FSE 2025)",
    "Lost in the Middle: How Language Models Use Long Contexts (TACL 2024)",
    "Direct Preference Optimization: Your Language Model is Secretly a Reward Model (NeurIPS 2023)",
    "ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330)"
  ],
  "description": "Existing retrieval-based LLM code repair systems use fixed fault-localization granularity and context budgets, despite evidence that optimal configuration is instance-dependent (arXiv 2604.00167, 2604.05481). The LLM routing literature (RouteLLM ICLR 2025, RADAR, LTRR SIGIR 2025) provides mature training paradigms but none target retrieval configuration for code repair. We propose GranRoute, a configuration routing framework that learns to select the optimal (granularity, context budget) per issue. We collect oracle repair labels by running Agentless across 12 configurations on 300 SWE-bench Verified instances (10,800 API calls at ~$0.08/run ≈ $864), then systematically compare 5 training methods — random forest, MLP classifier, Bradley-Terry preference router, LambdaMART ranking, and IRT-based difficulty model — to determine what works best for this routing target. This multi-method comparison directly addresses whether preference-based training (à la RouteLLM) outperforms simpler classifiers for configuration routing, or whether tree-based methods dominate (as LTRR found for retriever selection). GranRoute operates in two stages: (1) NL-only pre-routing using issue text (zero retrieval cost), and (2) optional refinement with code-structural signals after initial file localization. We use CodeSage-base (ICLR 2024, 356M) as the primary encoder with UniXcoder as ablation. We evaluate on ~100 decontaminated SWE-bench-Live instances from the 2 most recent monthly batches against fixed-configuration baselines, Triage-style code-only routing, and oracle upper bound. A 50-instance headroom pilot serves as go/no-go gate: if oracle advantage over best fixed config is <5pp accuracy AND <20% cost savings, we pivot. If accuracy headroom is modest but cost savings are substantial, we lead with cost-efficiency. The contribution is twofold: (1) GranRoute, the first configuration routing framework for code repair with a systematic comparison of 5 training methods and 2 feature families, (2) interpretable analysis connecting NL bug features to optimal code comprehension granularity. All oracle profiling is API-based (~$1,200 total, <40 H100-hours GPU). Primary target: EMNLP 2026 short paper (ARR May 25); extended version for ICSE 2027.",
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
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "23a587b8-937e-4dbd-9e04-90a81dbd215e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-11T23:36:00.360Z_

```json
{
  "parentUuid": "23a587b8-937e-4dbd-9e04-90a81dbd215e",
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
  "uuid": "efc15c0f-9fa9-48d0-a193-326667d14f58",
  "timestamp": "2026-05-11T23:36:00.360Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-11T23:36:00.361Z_

```json
{
  "parentUuid": "efc15c0f-9fa9-48d0-a193-326667d14f58",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "dd13a1e6-6860-48b2-97af-458ac9d374cf",
  "timestamp": "2026-05-11T23:36:00.361Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
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
  "leafUuid": "dd13a1e6-6860-48b2-97af-458ac9d374cf",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate GranRoute: Configuration Routing for Code Repair",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Assistant

_source line 8 · 2026-05-11T23:36:05.655Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea - "GranRoute: Learning to Route Retrieval Configurations for Repository-Level Code Repair" - in its 4th revision. I need to independently verify claims, check for missing competitors, assess feasibility, and determine if this meets the user's requirements.

Let me start by searching for the key claims and competitors mentioned in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd13a1e6-6860-48b2-97af-458ac9d374cf",
  "isSidechain": false,
  "requestId": "req_011CawfBzfN4ez6qDnt43bet",
  "type": "assistant",
  "uuid": "454f12c6-89d7-4660-9fe5-f559dd921a42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBBm8J2LkuvVw9He7fVuSK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18990,
      "cache_read_input_tokens": 11841,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 722,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18990
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

_source line 9 · 2026-05-11T23:36:06.667Z_

I'll conduct a thorough independent review of this Round 4 proposal. Let me verify claims, check for missing competitors, and assess feasibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "454f12c6-89d7-4660-9fe5-f559dd921a42",
  "isSidechain": false,
  "requestId": "req_011CawfBzfN4ez6qDnt43bet",
  "type": "assistant",
  "uuid": "7a6e6b58-6508-4dd9-b1c8-8b1abf1beb94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBBm8J2LkuvVw9He7fVuSK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18990,
      "cache_read_input_tokens": 11841,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 722,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18990
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

_source line 10 · 2026-05-11T23:36:20.075Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JgKSdFTNvSV7PeNXcSHAnL`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify SOTA and key references",
  "prompt": "I'm reviewing an ML paper proposal called \"GranRoute\" that proposes learning to route retrieval configurations (granularity + context budget) for repository-level code repair. I need to verify several claims independently.\n\nPlease search for and verify the following:\n\n1. **RouteLLM** — claimed as ICLR 2025, arXiv 2406.18665. Verify this paper exists, its venue, and whether it trains routers from preference data for model selection.\n\n2. **RADAR** — claimed as arXiv 2509.25426. Verify existence and whether it does difficulty-aware routing via item-response theory.\n\n3. **LTRR (Learning To Rank Retrievers)** — claimed as SIGIR 2025 LiveRAG, arXiv 2506.13743. Verify existence and whether it frames retriever selection as learning-to-rank with XGBoost outperforming neural rankers.\n\n4. **Triage** — claimed as arXiv 2604.07494 (April 2026). Routes SWE-bench tasks to cost-effective LLM tiers via code quality signals.\n\n5. **BEST-Route** — claimed as ICML 2025, arXiv 2506.22716. Routes model + sampling count.\n\n6. **Route-To-Reason** — claimed as arXiv 2505.19435. Jointly routes models and reasoning strategies.\n\n7. **CodeSage** — claimed as ICLR 2024, 356M params code encoder.\n\n8. **SIADAFIX** — claimed as arXiv 2510.16059. Issue description classification for adaptive program repair.\n\nFor each paper, use WebSearch to verify: (a) does it exist? (b) is the venue correct? (c) does it do what the proposal claims?\n\nAlso search for \"arXiv 2604.00167 fault localization granularity\" and \"arXiv 2604.05481 fault localization context\" to verify these two empirical studies exist and make the claimed findings.\n\nReport your findings concisely — which papers check out, which don't, and any discrepancies."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a6e6b58-6508-4dd9-b1c8-8b1abf1beb94",
  "isSidechain": false,
  "requestId": "req_011CawfBzfN4ez6qDnt43bet",
  "type": "assistant",
  "uuid": "8bc90726-ffaa-4e34-afdf-36e552198a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBBm8J2LkuvVw9He7fVuSK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18990,
      "cache_read_input_tokens": 11841,
      "output_tokens": 722,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 722,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18990
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

_source line 11 · 2026-05-11T23:37:52.256Z_

<details><summary>↩ Tool result · `toolu_01JgKSdFTNvSV7PeNXcSHAnL`</summary>

```text
All verifications are complete. Here is my consolidated report:

---

## Verification Results

### 1. RouteLLM -- VERIFIED
- **arXiv ID**: 2406.18665 -- correct
- **Venue**: ICLR 2025 -- confirmed (published as a conference paper)
- **Claim**: Trains routers from preference data for model selection -- confirmed. It learns router models from human preference data to dynamically select between stronger/weaker LLMs, reducing costs by up to 85% while maintaining 95% of GPT-4 performance.

### 2. RADAR -- VERIFIED
- **arXiv ID**: 2509.25426 -- correct
- **Claim**: Difficulty-aware routing via item-response theory -- confirmed. RADAR is inspired by psychometrics and learns an item response model (IRT) from model responses to jointly estimate query difficulties and model-budget abilities, then routes accordingly.
- **Note**: The proposal says "item-response theory" which is accurate. The paper's full title is "Reasoning-Ability and Difficulty-Aware Routing for Reasoning LLMs."

### 3. LTRR (Learning To Rank Retrievers) -- VERIFIED
- **arXiv ID**: 2506.13743 -- correct
- **Venue**: SIGIR 2025 LiveRAG -- confirmed (selected for spotlight talk)
- **Claim**: Frames retriever selection as learning-to-rank with XGBoost outperforming neural rankers -- confirmed. Pairwise XGBoost yielded the best results, outperforming standard single-retriever RAG systems.

### 4. Triage -- VERIFIED
- **arXiv ID**: 2604.07494 -- correct
- **Date**: April 2026 -- consistent with search results
- **Claim**: Routes SWE-bench tasks to cost-effective LLM tiers via code quality signals -- confirmed. Uses code health metrics as routing signals to assign tasks to cheapest viable model tier (light/standard/heavy corresponding to Haiku/Sonnet/Opus). Evaluated on SWE-bench Lite with 300 tasks.

### 5. BEST-Route -- VERIFIED
- **arXiv ID**: 2506.22716 -- correct
- **Venue**: ICML 2025 -- confirmed (ICML poster)
- **Claim**: Routes model + sampling count -- confirmed. BEST-Route selects both which LLM to use and how many responses to sample, reducing costs by up to 60% with less than 1% performance drop. Microsoft research.

### 6. Route-To-Reason -- VERIFIED
- **arXiv ID**: 2505.19435 -- correct
- **Claim**: Jointly routes models and reasoning strategies -- confirmed. RTR jointly trains low-dimensional embeddings for LLMs and reasoning strategies, selecting an optimal (model, strategy) pair per task. Achieves 82.5% accuracy while reducing token usage by over 60%.

### 7. CodeSage -- VERIFIED
- **Venue**: ICLR 2024 -- confirmed
- **Claim**: 356M params code encoder -- confirmed. CodeSage-Base is the 356M parameter variant (part of a family: Small 130M, Base 356M, Large 1.3B). Produces 1024-dimensional code embeddings. Amazon Science research.

### 8. SIADAFIX -- VERIFIED with nuance
- **arXiv ID**: 2510.16059 -- correct
- **Claim**: Issue description classification for adaptive program repair -- partially accurate. SIADAFIX does classify/optimize issue descriptions and adaptively selects repair modes (easy/middle/hard), but the paper's framing is broader: it uses "slow thinking" bug fix agents with "fast thinking" workflow decision components that classify issue descriptions to orchestrate repair workflows. The term "classification" is reasonable but somewhat reductive -- it is more of an issue-description-guided workflow orchestration system. Achieves 60.67% on SWE-bench Lite.

### 9. arXiv 2604.00167 (Fault Localization Granularity) -- VERIFIED
- **Title**: "A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks"
- **Finding**: Function-level granularity yields the highest repair rate compared to line-level and file-level on SWE-Bench-Mini, but the ideal granularity is task-dependent. From Fujitsu Research of Europe, submitted March 31, 2026.

### 10. arXiv 2604.05481 (Fault Localization Context) -- VERIFIED
- **Title**: "On the Role of Fault Localization Context for LLM-Based Program Repair"
- **Key findings**: More context does not consistently improve repair; file-level localization is the dominant factor (15-17x improvement over no-file baseline); line-level context expansion frequently degrades performance due to noise amplification; LLM-based retrieval outperforms structural heuristics. Large-scale study on 500 SWE-bench Verified instances. From York University, submitted April 7, 2026.

---

## Summary

**All 10 references check out.** Every arXiv ID resolves to a real paper, every venue claim is correct, and the functional descriptions are accurate. The only minor nuance is SIADAFIX (#8), where "issue description classification" is a somewhat simplified characterization of what is really issue-description-guided workflow orchestration with mode selection -- but the core idea (classifying issues to adapt the repair approach) is not wrong.

The two empirical studies (2604.00167 and 2604.05481) are particularly relevant to the "GranRoute" proposal, as they provide the empirical motivation: granularity matters and is task-dependent, and more context can hurt. A routing approach that learns per-task granularity and context budget decisions would be a natural next step from these findings.

Sources:
- [RouteLLM (2406.18665)](https://arxiv.org/abs/2406.18665)
- [ICLR 2025 RouteLLM Poster](https://iclr.cc/virtual/2025/poster/30737)
- [RADAR (2509.25426)](https://arxiv.org/abs/2509.25426)
- [LTRR (2506.13743)](https://arxiv.org/abs/2506.13743)
- [LTRR GitHub - SIGIR LiveRAG](https://github.com/kimdanny/Starlight-LiveRAG)
- [Triage (2604.07494)](https://arxiv.org/abs/2604.07494)
- [BEST-Route (2506.22716)](https://arxiv.org/abs/2506.22716)
- [ICML 2025 BEST-Route Poster](https://icml.cc/virtual/2025/poster/43788)
- [Route-To-Reason (2505.19435)](https://arxiv.org/abs/2505.19435)
- [CodeSage GitHub (ICLR 2024)](https://github.com/amazon-science/CodeSage)
- [CodeSage HuggingFace](https://huggingface.co/codesage/codesage-base)
- [SIADAFIX (2510.16059)](https://arxiv.org/abs/2510.16059)
- [Fault Localization Granularity (2604.00167)](https://arxiv.org/abs/2604.00167)
- [Fault Localization Context (2604.05481)](https://arxiv.org/abs/2604.05481)

agentId: acefe90f4eb922927 (use SendMessage with to: 'acefe90f4eb922927' to continue this agent)
&lt;usage>total_tokens: 22554
tool_uses: 12
duration_ms: 92175&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bc90726-ffaa-4e34-afdf-36e552198a36",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "b7c4ec91-fa8f-452a-b051-7aa845e46809",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing an ML paper proposal called \"GranRoute\" that proposes learning to route retrieval configurations (granularity + context budget) for repository-level code repair. I need to verify several claims independently.\n\nPlease search for and verify the following:\n\n1. **RouteLLM** — claimed as ICLR 2025, arXiv 2406.18665. Verify this paper exists, its venue, and whether it trains routers from preference data for model selection.\n\n2. **RADAR** — claimed as arXiv 2509.25426. Verify existence and whether it does difficulty-aware routing via item-response theory.\n\n3. **LTRR (Learning To Rank Retrievers)** — claimed as SIGIR 2025 LiveRAG, arXiv 2506.13743. Verify existence and whether it frames retriever selection as learning-to-rank with XGBoost outperforming neural rankers.\n\n4. **Triage** — claimed as arXiv 2604.07494 (April 2026). Routes SWE-bench tasks to cost-effective LLM tiers via code quality signals.\n\n5. **BEST-Route** — claimed as ICML 2025, arXiv 2506.22716. Routes model + sampling count.\n\n6. **Route-To-Reason** — claimed as arXiv 2505.19435. Jointly routes models and reasoning strategies.\n\n7. **CodeSage** — claimed as ICLR 2024, 356M params code encoder.\n\n8. **SIADAFIX** — claimed as arXiv 2510.16059. Issue description classification for adaptive program repair.\n\nFor each paper, use WebSearch to verify: (a) does it exist? (b) is the venue correct? (c) does it do what the proposal claims?\n\nAlso search for \"arXiv 2604.00167 fault localization granularity\" and \"arXiv 2604.05481 fault localization context\" to verify these two empirical studies exist and make the claimed findings.\n\nReport your findings concisely — which papers check out, which don't, and any discrepancies.",
    "agentId": "acefe90f4eb922927",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "All verifications are complete. Here is my consolidated report:\n\n---\n\n## Verification Results\n\n### 1. RouteLLM -- VERIFIED\n- **arXiv ID**: 2406.18665 -- correct\n- **Venue**: ICLR 2025 -- confirmed (published as a conference paper)\n- **Claim**: Trains routers from preference data for model selection -- confirmed. It learns router models from human preference data to dynamically select between stronger/weaker LLMs, reducing costs by up to 85% while maintaining 95% of GPT-4 performance.\n\n### 2. RADAR -- VERIFIED\n- **arXiv ID**: 2509.25426 -- correct\n- **Claim**: Difficulty-aware routing via item-response theory -- confirmed. RADAR is inspired by psychometrics and learns an item response model (IRT) from model responses to jointly estimate query difficulties and model-budget abilities, then routes accordingly.\n- **Note**: The proposal says \"item-response theory\" which is accurate. The paper's full title is \"Reasoning-Ability and Difficulty-Aware Routing for Reasoning LLMs.\"\n\n### 3. LTRR (Learning To Rank Retrievers) -- VERIFIED\n- **arXiv ID**: 2506.13743 -- correct\n- **Venue**: SIGIR 2025 LiveRAG -- confirmed (selected for spotlight talk)\n- **Claim**: Frames retriever selection as learning-to-rank with XGBoost outperforming neural rankers -- confirmed. Pairwise XGBoost yielded the best results, outperforming standard single-retriever RAG systems.\n\n### 4. Triage -- VERIFIED\n- **arXiv ID**: 2604.07494 -- correct\n- **Date**: April 2026 -- consistent with search results\n- **Claim**: Routes SWE-bench tasks to cost-effective LLM tiers via code quality signals -- confirmed. Uses code health metrics as routing signals to assign tasks to cheapest viable model tier (light/standard/heavy corresponding to Haiku/Sonnet/Opus). Evaluated on SWE-bench Lite with 300 tasks.\n\n### 5. BEST-Route -- VERIFIED\n- **arXiv ID**: 2506.22716 -- correct\n- **Venue**: ICML 2025 -- confirmed (ICML poster)\n- **Claim**: Routes model + sampling count -- confirmed. BEST-Route selects both which LLM to use and how many responses to sample, reducing costs by up to 60% with less than 1% performance drop. Microsoft research.\n\n### 6. Route-To-Reason -- VERIFIED\n- **arXiv ID**: 2505.19435 -- correct\n- **Claim**: Jointly routes models and reasoning strategies -- confirmed. RTR jointly trains low-dimensional embeddings for LLMs and reasoning strategies, selecting an optimal (model, strategy) pair per task. Achieves 82.5% accuracy while reducing token usage by over 60%.\n\n### 7. CodeSage -- VERIFIED\n- **Venue**: ICLR 2024 -- confirmed\n- **Claim**: 356M params code encoder -- confirmed. CodeSage-Base is the 356M parameter variant (part of a family: Small 130M, Base 356M, Large 1.3B). Produces 1024-dimensional code embeddings. Amazon Science research.\n\n### 8. SIADAFIX -- VERIFIED with nuance\n- **arXiv ID**: 2510.16059 -- correct\n- **Claim**: Issue description classification for adaptive program repair -- partially accurate. SIADAFIX does classify/optimize issue descriptions and adaptively selects repair modes (easy/middle/hard), but the paper's framing is broader: it uses \"slow thinking\" bug fix agents with \"fast thinking\" workflow decision components that classify issue descriptions to orchestrate repair workflows. The term \"classification\" is reasonable but somewhat reductive -- it is more of an issue-description-guided workflow orchestration system. Achieves 60.67% on SWE-bench Lite.\n\n### 9. arXiv 2604.00167 (Fault Localization Granularity) -- VERIFIED\n- **Title**: \"A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks\"\n- **Finding**: Function-level granularity yields the highest repair rate compared to line-level and file-level on SWE-Bench-Mini, but the ideal granularity is task-dependent. From Fujitsu Research of Europe, submitted March 31, 2026.\n\n### 10. arXiv 2604.05481 (Fault Localization Context) -- VERIFIED\n- **Title**: \"On the Role of Fault Localization Context for LLM-Based Program Repair\"\n- **Key findings**: More context does not consistently improve repair; file-level localization is the dominant factor (15-17x improvement over no-file baseline); line-level context expansion frequently degrades performance due to noise amplification; LLM-based retrieval outperforms structural heuristics. Large-scale study on 500 SWE-bench Verified instances. From York University, submitted April 7, 2026.\n\n---\n\n## Summary\n\n**All 10 references check out.** Every arXiv ID resolves to a real paper, every venue claim is correct, and the functional descriptions are accurate. The only minor nuance is SIADAFIX (#8), where \"issue description classification\" is a somewhat simplified characterization of what is really issue-description-guided workflow orchestration with mode selection -- but the core idea (classifying issues to adapt the repair approach) is not wrong.\n\nThe two empirical studies (2604.00167 and 2604.05481) are particularly relevant to the \"GranRoute\" proposal, as they provide the empirical motivation: granularity matters and is task-dependent, and more context can hurt. A routing approach that learns per-task granularity and context budget decisions would be a natural next step from these findings.\n\nSources:\n- [RouteLLM (2406.18665)](https://arxiv.org/abs/2406.18665)\n- [ICLR 2025 RouteLLM Poster](https://iclr.cc/virtual/2025/poster/30737)\n- [RADAR (2509.25426)](https://arxiv.org/abs/2509.25426)\n- [LTRR (2506.13743)](https://arxiv.org/abs/2506.13743)\n- [LTRR GitHub - SIGIR LiveRAG](https://github.com/kimdanny/Starlight-LiveRAG)\n- [Triage (2604.07494)](https://arxiv.org/abs/2604.07494)\n- [BEST-Route (2506.22716)](https://arxiv.org/abs/2506.22716)\n- [ICML 2025 BEST-Route Poster](https://icml.cc/virtual/2025/poster/43788)\n- [Route-To-Reason (2505.19435)](https://arxiv.org/abs/2505.19435)\n- [CodeSage GitHub (ICLR 2024)](https://github.com/amazon-science/CodeSage)\n- [CodeSage HuggingFace](https://huggingface.co/codesage/codesage-base)\n- [SIADAFIX (2510.16059)](https://arxiv.org/abs/2510.16059)\n- [Fault Localization Granularity (2604.00167)](https://arxiv.org/abs/2604.00167)\n- [Fault Localization Context (2604.05481)](https://arxiv.org/abs/2604.05481)"
      }
    ],
    "totalDurationMs": 92175,
    "totalTokens": 22554,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 922,
      "cache_read_input_tokens": 19787,
      "output_tokens": 1844,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 922
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1844,
          "cache_read_input_tokens": 19787,
          "cache_creation_input_tokens": 922,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 922,
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
  "sourceToolAssistantUUID": "8bc90726-ffaa-4e34-afdf-36e552198a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-11T23:37:58.094Z_

Good — all references verified. Now let me search for missing competitors and potential issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7c4ec91-fa8f-452a-b051-7aa845e46809",
  "isSidechain": false,
  "requestId": "req_011CawfLEakAvuswNv4PHnRX",
  "type": "assistant",
  "uuid": "c055ad86-1964-4b97-8315-e033bc22a376",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F61bR2JZCa9j1xKnBQtM6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2640,
      "cache_read_input_tokens": 30831,
      "output_tokens": 1671,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2640,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1671,
          "cache_read_input_tokens": 30831,
          "cache_creation_input_tokens": 2640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2640
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

_source line 13 · 2026-05-11T23:38:10.088Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01A8i3EytBdyDekcWSAJg2BR`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for missing competitors",
  "prompt": "I'm reviewing a paper proposal about \"GranRoute\" — learning to route retrieval configurations (granularity + context budget) for repository-level code repair. I need to find competitors the proposal may have missed. Search for:\n\n1. Search: \"adaptive retrieval configuration code repair 2025 2026\" — are there other papers that adaptively select retrieval strategies for code repair?\n\n2. Search: \"retrieval routing LLM code 2026\" — anything about routing retrieval for code tasks?\n\n3. Search: \"configuration selection software engineering LLM 2025 2026\" — automatic configuration selection for SE agents?\n\n4. Search: \"context window optimization code repair 2025 2026\" — optimizing context for code repair?\n\n5. Search: \"SWE-bench adaptive agent 2026\" — any SWE-bench agents that adaptively change their strategies?\n\n6. Search: \"meta-learning code repair retrieval 2025 2026\" — meta-learning approaches for code repair?\n\n7. Search: \"dynamic fault localization LLM 2026\" — dynamic/adaptive fault localization?\n\n8. Search: \"Agentless adaptive configuration 2026\" — any work extending Agentless with adaptive configs?\n\n9. Search for \"MASAI\" or \"CodeR\" or \"AutoCodeRover adaptive\" — known SWE-bench agents that might have adaptive retrieval.\n\n10. Search: \"learn to retrieve code generation 2025 2026\" — learning retrieval strategies for code tasks.\n\nFor each search, report the most relevant results. Focus on papers from 2025-2026 that are NOT already cited in the proposal. The cited papers include: RouteLLM, RADAR, BEST-Route, Route-To-Reason, LTRR, Triage, SIADAFIX, AdaPatcher, AdaEdit, SWEzze, SWE-Pruner, CodeScout, ARISE, RPO, DRO, ReCode, RGFL.\n\nReport concisely: paper title, venue/arXiv, and why it's relevant or not."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c055ad86-1964-4b97-8315-e033bc22a376",
  "isSidechain": false,
  "requestId": "req_011CawfLEakAvuswNv4PHnRX",
  "type": "assistant",
  "uuid": "42e5ff9c-b030-4af5-9c05-41458ba0ca3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F61bR2JZCa9j1xKnBQtM6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2640,
      "cache_read_input_tokens": 30831,
      "output_tokens": 1671,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2640,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1671,
          "cache_read_input_tokens": 30831,
          "cache_creation_input_tokens": 2640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2640
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

_source line 14 · 2026-05-11T23:38:23.877Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DenV85SMZtqESxy9qS66xZ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check feasibility and cost claims",
  "prompt": "I'm reviewing a paper proposal that plans to:\n1. Run Agentless (code repair pipeline) via API using \"Qwen3-Coder-Next\" at ~$0.08/instance\n2. Run 12 configurations × 300 instances × 3 runs each = 10,800 API calls for oracle collection (~$864)\n3. Run 12 configs × 50 instances × 3 runs = 1,800 calls for pilot (~$144)\n4. Evaluate on ~100 SWE-bench-Live instances × 12 configs × 3 runs (~$288)\n5. Train 5 lightweight routers (random forest, MLP, preference router, LambdaMART, IRT model) in ~8 H100-hours\n6. Total budget: <40 H100-hours GPU, ~$1,200 API cost\n7. Timeline: 14 days\n\nPlease verify:\n1. Search for \"Qwen3-Coder-Next API pricing 2026\" — does this model exist and what does it cost? Is $0.08/instance reasonable for SWE-bench repair runs?\n2. Search for \"SWE-bench Verified Agentless API cost per instance\" — what's the typical cost of running Agentless on one SWE-bench instance via API?\n3. Search for \"SWE-bench Live 2026 instances\" — how many SWE-bench-Live instances are available? Are recent monthly batches accessible?\n4. Search for \"Agentless SWE-bench setup time\" — how long does it take to run Agentless on SWE-bench instances? Is 14 days realistic for 10,800+ runs?\n5. Search for \"CodeSage base model fine-tuning cost\" — is CodeSage-base (356M) cheap to fine-tune/use for embeddings?\n6. Search for \"SWE-bench Docker environment setup failure rate\" — is the 10-15% failure rate claim realistic?\n\nReport your findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42e5ff9c-b030-4af5-9c05-41458ba0ca3d",
  "isSidechain": false,
  "requestId": "req_011CawfLEakAvuswNv4PHnRX",
  "type": "assistant",
  "uuid": "60214385-27af-494a-8cd4-f4dc85763871",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F61bR2JZCa9j1xKnBQtM6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2640,
      "cache_read_input_tokens": 30831,
      "output_tokens": 1671,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2640,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1671,
          "cache_read_input_tokens": 30831,
          "cache_creation_input_tokens": 2640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2640
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

_source line 15 · 2026-05-11T23:38:32.990Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GnmvNpPYnyHxTbZn9kVvUL`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check novelty and venue fit",
  "prompt": "I'm reviewing a paper for EMNLP 2026 (ARR May 25 deadline). The paper proposes \"GranRoute\" — learning to route retrieval configurations for code repair. I need to verify:\n\n1. **EMNLP 2026 ARR deadline**: Search for \"ARR May 2026 submission deadline EMNLP\" to verify the May 25, 2026 deadline is correct and that EMNLP 2026 accepts from this cycle.\n\n2. **EMNLP short paper page limit**: Search for \"EMNLP 2026 short paper page limit\" or \"ARR short paper format 2026\" — is 4 pages correct?\n\n3. **Novelty check — routing for retrieval in code tasks**: Search for:\n   - \"adaptive retrieval strategy selection code 2025 2026\" \n   - \"learn to select retrieval granularity 2025 2026\"\n   - \"routing retrieval configuration 2025 2026\"\n   Are there any papers that already do what GranRoute proposes (learning to select retrieval configuration for code tasks)?\n\n4. **Venue fit**: Search for \"EMNLP NLP and code models track\" or \"EMNLP code understanding papers 2024 2025\" — does this type of routing/configuration selection work fit EMNLP's scope? Look for examples of similar SE-adjacent papers accepted at EMNLP.\n\n5. **Multi-method comparison as contribution**: Search for \"systematic comparison routing methods LLM 2025 2026\" — is a multi-method comparison (comparing 5 training methods) a sufficiently novel contribution, or is it considered ablation-as-paper?\n\n6. **Bradley-Terry preference loss for routing**: Search for \"Bradley-Terry preference learning routing 2025 2026\" — has Bradley-Terry been used for routing configuration selection before?\n\nReport findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60214385-27af-494a-8cd4-f4dc85763871",
  "isSidechain": false,
  "requestId": "req_011CawfLEakAvuswNv4PHnRX",
  "type": "assistant",
  "uuid": "cda8961b-d892-4f40-b515-22c771a306ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F61bR2JZCa9j1xKnBQtM6j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2640,
      "cache_read_input_tokens": 30831,
      "output_tokens": 1671,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2640,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1671,
          "cache_read_input_tokens": 30831,
          "cache_creation_input_tokens": 2640,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2640
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

_source line 16 · 2026-05-11T23:40:08.504Z_

<details><summary>↩ Tool result · `toolu_01DenV85SMZtqESxy9qS66xZ`</summary>

```text
Now I have enough information to compile a thorough assessment. Here are my findings:

---

## Verification Report

### 1. Qwen3-Coder-Next: Existence, Pricing, and $0.08/instance Estimate

**The model exists.** Qwen3-Coder-Next was released on February 4, 2026. It achieves ~70-74% on SWE-Bench Verified and supports a 262K context window.

**Pricing:** $0.110/M input tokens, $0.800/M output tokens (via Qwen API; providers like OpenRouter/DeepInfra may vary).

**Is $0.08/instance reasonable?** This is plausible but tight. The original Agentless paper (with GPT-4o-class models) reported ~$0.34/instance. Agentless-Lite reports $0.12-$0.21/instance. Qwen3-Coder-Next is significantly cheaper per token than GPT-4o, so the Agentless pipeline with this model could plausibly hit $0.08/instance -- but this depends heavily on token consumption per instance. A rough estimate: if Agentless uses ~50K input + ~10K output tokens per instance, the cost would be ~$0.0135, which is actually well under $0.08. If it uses ~500K input + 50K output (more realistic for multi-step localization + repair + validation), it would be ~$0.095. **The $0.08 figure is in the right ballpark but should be validated with a small pilot; it could be slightly optimistic or conservative depending on actual token consumption.**

### 2. Typical Cost of Running Agentless on One SWE-bench Instance

- **Original Agentless (GPT-4o, 2024):** ~$0.34/instance average
- **Agentless-Lite (RAG-optimized):** ~$0.12-$0.21/instance
- With cheaper models like Qwen3-Coder-Next ($0.11/$0.80 per M tokens vs. GPT-4o's $2.50/$10.00), costs scale down roughly proportionally, making $0.08-$0.15/instance reasonable.

**Verdict:** The $0.08 figure is plausible given Qwen3-Coder-Next's low pricing, but it assumes a lean token budget. The total API budget of ~$1,200 for 10,800 + 1,800 + 3,600 = 16,200 calls at $0.08 each = $1,296, which is slightly over the stated $1,200 but close enough. The math roughly checks out.

### 3. SWE-bench-Live Instance Count

**SWE-bench-Live currently has ~1,890 task instances** (as of recent data), spanning 223 repositories. It adds ~50 new verified instances per month. The dataset started at 1,319 instances (May 2025) and has grown to 1,890.

**Are ~100 instances available for evaluation?** Yes, easily. The proposal could use any subset. Recent monthly batches are accessible via the [HuggingFace dataset](https://huggingface.co/datasets/SWE-bench-Live/SWE-bench-Live). **No issue here.**

### 4. Is 14 Days Realistic for 10,800+ Agentless Runs?

**Yes, likely feasible -- the bottleneck is API throughput, not compute.**

- Agentless is an API-only pipeline (localization + repair + validation via LLM calls). There is no local GPU training involved for this phase.
- SWE-bench evaluation (running tests in Docker) is fast: Epoch AI reports ~8 seconds/sample on a 32-core machine, meaning 300 instances can be evaluated in ~40 minutes.
- The 10,800 API calls are embarrassingly parallel. With even modest concurrency (e.g., 50 parallel requests), you could complete all calls in a few days.
- The main risk is **API rate limits** from Qwen's API platform. If rate-limited to, say, 100 RPM, 10,800 calls would take ~108 minutes of pure API time (not counting latency). At 10 RPM, it would take ~18 hours.

**Verdict: 14 days is realistic** assuming reasonable API rate limits and no major debugging surprises. The pilot (1,800 calls) could be done in 1-2 days, leaving ample time for the oracle collection and evaluation.

### 5. CodeSage-base (356M) Fine-tuning Cost

**CodeSage-base is a 356M parameter encoder model** that produces 1024-dimensional embeddings. It is publicly available on [HuggingFace](https://huggingface.co/codesage/codesage-base).

- At 356M parameters, this is a small model by modern standards (comparable to BERT-large). Fine-tuning or using it for inference is very cheap.
- Fine-tuning a 356M model requires a single GPU (even a consumer-grade one). On an H100, fine-tuning would take minutes to a few hours depending on dataset size.
- For the proposal's purpose (generating code embeddings as features for lightweight routers), CodeSage-base likely doesn't need fine-tuning at all -- just inference. Running inference on 300-1,890 code instances with a 356M model is trivially cheap (~minutes on a single GPU).
- The 8 H100-hours budget for training 5 lightweight routers (random forest, MLP, preference router, LambdaMART, IRT model) is **very generous** for this task. These are small classical ML / shallow neural models trained on features extracted from CodeSage embeddings. Most would train in seconds to minutes.

**Verdict: Entirely reasonable.** 8 H100-hours is more than sufficient; the real cost here is negligible.

### 6. SWE-bench Docker Environment Setup Failure Rate (10-15% Claim)

**This claim is likely overstated for curated subsets but could be realistic for the full dataset or SWE-bench-Live.**

- **SWE-bench Verified** was specifically designed to exclude instances with environment/build failures. The failure rate on Verified is very low (~2 instances failing out of 500 in Lite, ~10 in full).
- **SWE-bench-Live** adds new instances monthly and may have higher failure rates since instances are newer and less battle-tested. The SWE-bench-Live paper acknowledges filtering for buildability.
- The aorwall/SWE-bench-docker project reported 18 failing instances in SWE-bench Lite alone, plus intermittent failures. On the full SWE-bench dataset (2,294 instances), a 10-15% failure rate is plausible.
- For **SWE-bench-Live specifically**, since it continuously adds new instances from recent GitHub issues, some environment flakiness (dependency resolution, version pinning) is expected. A 10-15% failure rate for newly added monthly batches before curation is plausible.

**Verdict:** 10-15% is a reasonable estimate for SWE-bench-Live or uncurated portions of the dataset. For SWE-bench Verified, it would be too high (~1-2%). The proposal should clarify which subset they are referring to.

---

## Overall Assessment

| Claim | Verdict |
|-------|---------|
| $0.08/instance with Qwen3-Coder-Next | Plausible but should be validated with pilot |
| Total ~$1,200 API cost | Math roughly checks out (~$1,296 at $0.08) |
| 14-day timeline | Feasible if API rate limits are manageable |
| ~100 SWE-bench-Live instances | Available (dataset has ~1,890 total) |
| 8 H100-hours for router training | More than sufficient |
| <40 H100-hours total GPU | Generous for this workload |
| 10-15% Docker failure rate | Reasonable for Live; too high for Verified |

**Key risks to flag:**
- API rate limits from Qwen could bottleneck the 14-day timeline
- The $0.08/instance estimate should be validated early in the pilot phase
- The proposal should specify whether the 10-15% failure rate refers to Live or Verified instances
- The budget is slightly tight ($1,296 vs $1,200 stated) if every run costs $0.08

Sources:
- [Qwen3-Coder-Next on OpenRouter](https://openrouter.ai/qwen/qwen3-coder-next)
- [Qwen API Pricing 2026](https://pricepertoken.com/pricing-page/provider/qwen)
- [Agentless GitHub Repository](https://github.com/OpenAutoCoder/Agentless)
- [Agentless-Lite GitHub Repository](https://github.com/sorendunn/Agentless-Lite)
- [SWE-bench-Live Leaderboard](https://swe-bench-live.github.io/)
- [SWE-bench-Live on HuggingFace](https://huggingface.co/datasets/SWE-bench-Live/SWE-bench-Live)
- [SWE-bench-Live GitHub (Microsoft)](https://github.com/microsoft/SWE-bench-Live)
- [Epoch AI: SWE-bench in One Hour](https://epoch.ai/blog/swebench-docker)
- [CodeSage-base on HuggingFace](https://huggingface.co/codesage/codesage-base)
- [SWE-bench Docker Issues](https://github.com/aorwall/SWE-bench-docker)
- [SWE-bench Failing Instances Issue #167](https://github.com/swe-bench/SWE-bench/issues/167)
- [Qwen3-Coder-Next Technical Report](https://arxiv.org/html/2603.00729v1)

agentId: aa0aca10fb85708bf (use SendMessage with to: 'aa0aca10fb85708bf' to continue this agent)
&lt;usage>total_tokens: 24036
tool_uses: 14
duration_ms: 104625&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60214385-27af-494a-8cd4-f4dc85763871",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "693cde3d-29e3-45fe-a258-9c9af07d9e37",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper proposal that plans to:\n1. Run Agentless (code repair pipeline) via API using \"Qwen3-Coder-Next\" at ~$0.08/instance\n2. Run 12 configurations × 300 instances × 3 runs each = 10,800 API calls for oracle collection (~$864)\n3. Run 12 configs × 50 instances × 3 runs = 1,800 calls for pilot (~$144)\n4. Evaluate on ~100 SWE-bench-Live instances × 12 configs × 3 runs (~$288)\n5. Train 5 lightweight routers (random forest, MLP, preference router, LambdaMART, IRT model) in ~8 H100-hours\n6. Total budget: <40 H100-hours GPU, ~$1,200 API cost\n7. Timeline: 14 days\n\nPlease verify:\n1. Search for \"Qwen3-Coder-Next API pricing 2026\" — does this model exist and what does it cost? Is $0.08/instance reasonable for SWE-bench repair runs?\n2. Search for \"SWE-bench Verified Agentless API cost per instance\" — what's the typical cost of running Agentless on one SWE-bench instance via API?\n3. Search for \"SWE-bench Live 2026 instances\" — how many SWE-bench-Live instances are available? Are recent monthly batches accessible?\n4. Search for \"Agentless SWE-bench setup time\" — how long does it take to run Agentless on SWE-bench instances? Is 14 days realistic for 10,800+ runs?\n5. Search for \"CodeSage base model fine-tuning cost\" — is CodeSage-base (356M) cheap to fine-tune/use for embeddings?\n6. Search for \"SWE-bench Docker environment setup failure rate\" — is the 10-15% failure rate claim realistic?\n\nReport your findings concisely.",
    "agentId": "aa0aca10fb85708bf",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to compile a thorough assessment. Here are my findings:\n\n---\n\n## Verification Report\n\n### 1. Qwen3-Coder-Next: Existence, Pricing, and $0.08/instance Estimate\n\n**The model exists.** Qwen3-Coder-Next was released on February 4, 2026. It achieves ~70-74% on SWE-Bench Verified and supports a 262K context window.\n\n**Pricing:** $0.110/M input tokens, $0.800/M output tokens (via Qwen API; providers like OpenRouter/DeepInfra may vary).\n\n**Is $0.08/instance reasonable?** This is plausible but tight. The original Agentless paper (with GPT-4o-class models) reported ~$0.34/instance. Agentless-Lite reports $0.12-$0.21/instance. Qwen3-Coder-Next is significantly cheaper per token than GPT-4o, so the Agentless pipeline with this model could plausibly hit $0.08/instance -- but this depends heavily on token consumption per instance. A rough estimate: if Agentless uses ~50K input + ~10K output tokens per instance, the cost would be ~$0.0135, which is actually well under $0.08. If it uses ~500K input + 50K output (more realistic for multi-step localization + repair + validation), it would be ~$0.095. **The $0.08 figure is in the right ballpark but should be validated with a small pilot; it could be slightly optimistic or conservative depending on actual token consumption.**\n\n### 2. Typical Cost of Running Agentless on One SWE-bench Instance\n\n- **Original Agentless (GPT-4o, 2024):** ~$0.34/instance average\n- **Agentless-Lite (RAG-optimized):** ~$0.12-$0.21/instance\n- With cheaper models like Qwen3-Coder-Next ($0.11/$0.80 per M tokens vs. GPT-4o's $2.50/$10.00), costs scale down roughly proportionally, making $0.08-$0.15/instance reasonable.\n\n**Verdict:** The $0.08 figure is plausible given Qwen3-Coder-Next's low pricing, but it assumes a lean token budget. The total API budget of ~$1,200 for 10,800 + 1,800 + 3,600 = 16,200 calls at $0.08 each = $1,296, which is slightly over the stated $1,200 but close enough. The math roughly checks out.\n\n### 3. SWE-bench-Live Instance Count\n\n**SWE-bench-Live currently has ~1,890 task instances** (as of recent data), spanning 223 repositories. It adds ~50 new verified instances per month. The dataset started at 1,319 instances (May 2025) and has grown to 1,890.\n\n**Are ~100 instances available for evaluation?** Yes, easily. The proposal could use any subset. Recent monthly batches are accessible via the [HuggingFace dataset](https://huggingface.co/datasets/SWE-bench-Live/SWE-bench-Live). **No issue here.**\n\n### 4. Is 14 Days Realistic for 10,800+ Agentless Runs?\n\n**Yes, likely feasible -- the bottleneck is API throughput, not compute.**\n\n- Agentless is an API-only pipeline (localization + repair + validation via LLM calls). There is no local GPU training involved for this phase.\n- SWE-bench evaluation (running tests in Docker) is fast: Epoch AI reports ~8 seconds/sample on a 32-core machine, meaning 300 instances can be evaluated in ~40 minutes.\n- The 10,800 API calls are embarrassingly parallel. With even modest concurrency (e.g., 50 parallel requests), you could complete all calls in a few days.\n- The main risk is **API rate limits** from Qwen's API platform. If rate-limited to, say, 100 RPM, 10,800 calls would take ~108 minutes of pure API time (not counting latency). At 10 RPM, it would take ~18 hours.\n\n**Verdict: 14 days is realistic** assuming reasonable API rate limits and no major debugging surprises. The pilot (1,800 calls) could be done in 1-2 days, leaving ample time for the oracle collection and evaluation.\n\n### 5. CodeSage-base (356M) Fine-tuning Cost\n\n**CodeSage-base is a 356M parameter encoder model** that produces 1024-dimensional embeddings. It is publicly available on [HuggingFace](https://huggingface.co/codesage/codesage-base).\n\n- At 356M parameters, this is a small model by modern standards (comparable to BERT-large). Fine-tuning or using it for inference is very cheap.\n- Fine-tuning a 356M model requires a single GPU (even a consumer-grade one). On an H100, fine-tuning would take minutes to a few hours depending on dataset size.\n- For the proposal's purpose (generating code embeddings as features for lightweight routers), CodeSage-base likely doesn't need fine-tuning at all -- just inference. Running inference on 300-1,890 code instances with a 356M model is trivially cheap (~minutes on a single GPU).\n- The 8 H100-hours budget for training 5 lightweight routers (random forest, MLP, preference router, LambdaMART, IRT model) is **very generous** for this task. These are small classical ML / shallow neural models trained on features extracted from CodeSage embeddings. Most would train in seconds to minutes.\n\n**Verdict: Entirely reasonable.** 8 H100-hours is more than sufficient; the real cost here is negligible.\n\n### 6. SWE-bench Docker Environment Setup Failure Rate (10-15% Claim)\n\n**This claim is likely overstated for curated subsets but could be realistic for the full dataset or SWE-bench-Live.**\n\n- **SWE-bench Verified** was specifically designed to exclude instances with environment/build failures. The failure rate on Verified is very low (~2 instances failing out of 500 in Lite, ~10 in full).\n- **SWE-bench-Live** adds new instances monthly and may have higher failure rates since instances are newer and less battle-tested. The SWE-bench-Live paper acknowledges filtering for buildability.\n- The aorwall/SWE-bench-docker project reported 18 failing instances in SWE-bench Lite alone, plus intermittent failures. On the full SWE-bench dataset (2,294 instances), a 10-15% failure rate is plausible.\n- For **SWE-bench-Live specifically**, since it continuously adds new instances from recent GitHub issues, some environment flakiness (dependency resolution, version pinning) is expected. A 10-15% failure rate for newly added monthly batches before curation is plausible.\n\n**Verdict:** 10-15% is a reasonable estimate for SWE-bench-Live or uncurated portions of the dataset. For SWE-bench Verified, it would be too high (~1-2%). The proposal should clarify which subset they are referring to.\n\n---\n\n## Overall Assessment\n\n| Claim | Verdict |\n|-------|---------|\n| $0.08/instance with Qwen3-Coder-Next | Plausible but should be validated with pilot |\n| Total ~$1,200 API cost | Math roughly checks out (~$1,296 at $0.08) |\n| 14-day timeline | Feasible if API rate limits are manageable |\n| ~100 SWE-bench-Live instances | Available (dataset has ~1,890 total) |\n| 8 H100-hours for router training | More than sufficient |\n| <40 H100-hours total GPU | Generous for this workload |\n| 10-15% Docker failure rate | Reasonable for Live; too high for Verified |\n\n**Key risks to flag:**\n- API rate limits from Qwen could bottleneck the 14-day timeline\n- The $0.08/instance estimate should be validated early in the pilot phase\n- The proposal should specify whether the 10-15% failure rate refers to Live or Verified instances\n- The budget is slightly tight ($1,296 vs $1,200 stated) if every run costs $0.08\n\nSources:\n- [Qwen3-Coder-Next on OpenRouter](https://openrouter.ai/qwen/qwen3-coder-next)\n- [Qwen API Pricing 2026](https://pricepertoken.com/pricing-page/provider/qwen)\n- [Agentless GitHub Repository](https://github.com/OpenAutoCoder/Agentless)\n- [Agentless-Lite GitHub Repository](https://github.com/sorendunn/Agentless-Lite)\n- [SWE-bench-Live Leaderboard](https://swe-bench-live.github.io/)\n- [SWE-bench-Live on HuggingFace](https://huggingface.co/datasets/SWE-bench-Live/SWE-bench-Live)\n- [SWE-bench-Live GitHub (Microsoft)](https://github.com/microsoft/SWE-bench-Live)\n- [Epoch AI: SWE-bench in One Hour](https://epoch.ai/blog/swebench-docker)\n- [CodeSage-base on HuggingFace](https://huggingface.co/codesage/codesage-base)\n- [SWE-bench Docker Issues](https://github.com/aorwall/SWE-bench-docker)\n- [SWE-bench Failing Instances Issue #167](https://github.com/swe-bench/SWE-bench/issues/167)\n- [Qwen3-Coder-Next Technical Report](https://arxiv.org/html/2603.00729v1)"
      }
    ],
    "totalDurationMs": 104625,
    "totalTokens": 24036,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2776,
      "cache_read_input_tokens": 18815,
      "output_tokens": 2444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2776
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2444,
          "cache_read_input_tokens": 18815,
          "cache_creation_input_tokens": 2776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2776,
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
  "sourceToolAssistantUUID": "60214385-27af-494a-8cd4-f4dc85763871",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
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
  "leafUuid": "693cde3d-29e3-45fe-a258-9c9af07d9e37",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate GranRoute: Configuration Routing for Code Repair",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Tool result

_source line 19 · 2026-05-11T23:40:22.961Z_

<details><summary>↩ Tool result · `toolu_01GnmvNpPYnyHxTbZn9kVvUL`</summary>

```text
Here are my consolidated findings across all six questions:

---

## 1. EMNLP 2026 ARR Deadline

**Confirmed: May 25, 2026 is correct.** The EMNLP 2026 CFP and official Twitter account both state the ARR submission deadline is May 25, 2026. One important wrinkle: since EMNLP 2026 and AACL share the ARR May cycle, authors must explicitly declare their target conference at submission time, and the choice is binding. Post-submission timeline: author response July 7-13, meta-review July 30, commitment deadline August 2, notification August 20.

Sources:
- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)
- [ARR Dates](http://aclrollingreview.org/dates)
- [EMNLP 2026 Twitter announcement](https://x.com/emnlpmeeting/status/2029508292637061462)

---

## 2. Short Paper Page Limit

**Confirmed: 4 pages is correct.** EMNLP 2026 follows the standard ARR format: 8 pages for long papers, 4 pages for short papers (excluding references/appendices).

Sources:
- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)
- [ARR CFP](http://aclrollingreview.org/cfp)

---

## 3. Novelty Check -- Routing for Retrieval in Code Tasks

**There is closely related prior work, but GranRoute appears to occupy a specific niche.** Key papers to be aware of:

- **ProCC (TOSEM 2025)**: Uses a contextual multi-armed bandit algorithm to adaptively select among multiple retrieval perspectives for code completion. This is the most directly comparable work -- it frames retrieval strategy selection as a bandit problem for code tasks. GranRoute needs to clearly differentiate from ProCC.

- **Mix-of-Granularity (MoG, COLING 2025)**: Learns a router to dynamically select the optimal retrieval granularity for RAG based on input queries. Not code-specific, but the mechanism (a trained router selecting granularity) is very close to what GranRoute describes.

- **Pre-Route (submitted to ICLR 2026)**: Routes between RAG vs. long-context using metadata, but is not code-specific and not about retrieval configuration.

- **RouteLLM (2024)**: Routes between strong/weak LLMs using preference data, including a Bradley-Terry-based router. Not retrieval configuration, but the training methodology overlaps.

- **"Less is More" (AAAI 2025)**: Adaptive program repair with preference learning, but focuses on bug localization rather than retrieval routing.

**Assessment**: The specific combination of (a) learning to route retrieval *configurations* (not just granularity or model choice) for (b) code repair tasks appears novel. However, ProCC's adaptive retrieval selection for code and MoG's learned granularity router are close enough that the paper must explicitly discuss them. If GranRoute does not cite and differentiate from ProCC and MoG, that is a significant gap.

Sources:
- [ProCC (arXiv/TOSEM)](https://arxiv.org/abs/2405.07530)
- [Mix-of-Granularity (COLING 2025)](https://aclanthology.org/2025.coling-main.384/)
- [Dense X Retrieval](https://arxiv.org/abs/2312.06648)
- [Less is More (AAAI 2025)](https://arxiv.org/abs/2503.06510)

---

## 4. Venue Fit

**EMNLP is a reasonable venue, but borderline.** Evidence:

- EMNLP 2025 accepted "Think-Search-Patch: A Retrieval-Augmented Reasoning Framework for Repository-Level Code Repair" in its **Industry Track** (note: industry, not main conference).
- EMNLP 2025 accepted "Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs."
- A retrieval-augmented code generation survey notes EMNLP had ~4.5% of peer-reviewed RACG papers, indicating modest but real representation.
- EMNLP 2025 Findings included "Training-Free LLM Routing for Knowledge Graph Retrieval" and "A Comprehensive Benchmark for Routing LLMs," showing routing work is accepted.

**Assessment**: Code repair + retrieval routing is at the intersection of SE and NLP. EMNLP accepts such work but tends to favor it more when the NLP contribution (e.g., novel training methodology, preference modeling, language understanding) is front and center rather than pure SE evaluation. If the paper's primary contribution is the routing methodology and training signal rather than the SE evaluation, EMNLP is a good fit. If it reads more like an SE systems paper, venues like ASE/ICSE/FSE would be stronger. As a reviewer, check whether the framing emphasizes the NLP/ML contributions.

Sources:
- [EMNLP 2025 Industry Track](https://2025.emnlp.org/program/ind_papers/)
- [EMNLP 2025 Findings - Routing for KG Retrieval](https://aclanthology.org/2025.findings-emnlp.606.pdf)
- [Routing LLMs Benchmark (EMNLP 2025 Findings)](https://aclanthology.org/2025.findings-emnlp.208.pdf)

---

## 5. Multi-Method Comparison as Contribution

**A 5-method comparison alone is thin; the field has moved toward systematic benchmarking.** Relevant context:

- **LLMRouterBench** already integrates 10+ routing methods with standardized evaluation, ablation support, and reproducible comparison.
- **RouterEval (2025)** provides 200M+ performance records across 8,500+ LLMs and 12 benchmarks for systematic router evaluation.
- A notable finding from "Rethinking Predictive LLM Routing" shows that a simple kNN baseline matches or beats complex learned routers, calling into question the value of elaborate method comparisons without novel insight.

**Assessment**: If GranRoute's contribution is primarily "we tried 5 training methods and report which works best," that is indeed closer to ablation-as-paper, especially given that RouterEval and LLMRouterBench already provide more comprehensive comparison frameworks. However, if the comparison yields a *novel finding* (e.g., Bradley-Terry outperforms alternatives specifically for retrieval configuration routing, or code tasks require different routing strategies than NL tasks), that transforms it from mere comparison to empirical contribution. Check whether the paper draws generalizable insights from the comparison or just reports numbers.

Sources:
- [LLMRouterBench](https://www.emergentmind.com/topics/llmrouterbench)
- [Rethinking Predictive LLM Routing (OpenReview)](https://openreview.net/forum?id=Chn50flK4X)
- [Dynamic Model Routing Survey](https://arxiv.org/abs/2603.04445)

---

## 6. Bradley-Terry for Routing Configuration Selection

**Yes, Bradley-Terry has been used for routing, but not specifically for retrieval configuration routing.**

- **RouteLLM (2024, ICLR 2025)**: Directly uses a Bradley-Terry-based router trained on preference data from Chatbot Arena to route between strong/weak LLMs. This is the most established use of BT for routing.
- **Prompt-to-Leaderboard (P2L, 2025)**: Extends BT to compute prompt-dependent leaderboards and route queries to optimal models. Their BT-based router hit #1 on Chatbot Arena.
- **Beyond Bradley-Terry (ICLR 2025, ICML 2025)**: Multiple papers critique BT's limitations (intransitive preferences, expressiveness) and propose alternatives like General Preference Models.

**Assessment**: Using BT for routing is well-established (RouteLLM is the canonical reference). The novelty would need to be in applying BT specifically to *retrieval configuration* selection rather than model selection -- that appears to be a new application domain. However, the paper should cite RouteLLM and acknowledge this lineage. If it presents BT for routing as novel without citing RouteLLM, that is a red flag.

Sources:
- [RouteLLM (arXiv)](https://arxiv.org/abs/2406.18665)
- [RouteLLM (ICLR 2025)](https://openreview.net/forum?id=8sSqNntaMr)
- [Prompt-to-Leaderboard](https://arxiv.org/pdf/2502.14855)
- [Rethinking BT in Reward Modeling (ICLR 2025)](https://github.com/holarissun/RewardModelingBeyondBradleyTerry)
- [General Preference Model (ICML 2025)](https://github.com/general-preference/general-preference-model)

---

## Summary for Your Review

| Question | Verdict |
|---|---|
| May 25 deadline | Confirmed correct |
| 4-page short paper | Confirmed correct |
| Novelty | Niche is defensible but must cite ProCC and MoG; differentiation needed |
| Venue fit | Acceptable if NLP/ML contribution is foregrounded; borderline if SE-heavy |
| 5-method comparison | Risky as sole contribution; needs novel insight, not just numbers |
| BT for routing | Well-established for model routing (RouteLLM); new for retrieval config routing if properly framed |

agentId: a30cab4ee1ca19082 (use SendMessage with to: 'a30cab4ee1ca19082' to continue this agent)
&lt;usage>total_tokens: 26366
tool_uses: 15
duration_ms: 109967&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cda8961b-d892-4f40-b515-22c771a306ed",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "fb61a1e5-1593-4837-b5e9-8fc8eaf41c96",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper for EMNLP 2026 (ARR May 25 deadline). The paper proposes \"GranRoute\" — learning to route retrieval configurations for code repair. I need to verify:\n\n1. **EMNLP 2026 ARR deadline**: Search for \"ARR May 2026 submission deadline EMNLP\" to verify the May 25, 2026 deadline is correct and that EMNLP 2026 accepts from this cycle.\n\n2. **EMNLP short paper page limit**: Search for \"EMNLP 2026 short paper page limit\" or \"ARR short paper format 2026\" — is 4 pages correct?\n\n3. **Novelty check — routing for retrieval in code tasks**: Search for:\n   - \"adaptive retrieval strategy selection code 2025 2026\" \n   - \"learn to select retrieval granularity 2025 2026\"\n   - \"routing retrieval configuration 2025 2026\"\n   Are there any papers that already do what GranRoute proposes (learning to select retrieval configuration for code tasks)?\n\n4. **Venue fit**: Search for \"EMNLP NLP and code models track\" or \"EMNLP code understanding papers 2024 2025\" — does this type of routing/configuration selection work fit EMNLP's scope? Look for examples of similar SE-adjacent papers accepted at EMNLP.\n\n5. **Multi-method comparison as contribution**: Search for \"systematic comparison routing methods LLM 2025 2026\" — is a multi-method comparison (comparing 5 training methods) a sufficiently novel contribution, or is it considered ablation-as-paper?\n\n6. **Bradley-Terry preference loss for routing**: Search for \"Bradley-Terry preference learning routing 2025 2026\" — has Bradley-Terry been used for routing configuration selection before?\n\nReport findings concisely.",
    "agentId": "a30cab4ee1ca19082",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my consolidated findings across all six questions:\n\n---\n\n## 1. EMNLP 2026 ARR Deadline\n\n**Confirmed: May 25, 2026 is correct.** The EMNLP 2026 CFP and official Twitter account both state the ARR submission deadline is May 25, 2026. One important wrinkle: since EMNLP 2026 and AACL share the ARR May cycle, authors must explicitly declare their target conference at submission time, and the choice is binding. Post-submission timeline: author response July 7-13, meta-review July 30, commitment deadline August 2, notification August 20.\n\nSources:\n- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)\n- [ARR Dates](http://aclrollingreview.org/dates)\n- [EMNLP 2026 Twitter announcement](https://x.com/emnlpmeeting/status/2029508292637061462)\n\n---\n\n## 2. Short Paper Page Limit\n\n**Confirmed: 4 pages is correct.** EMNLP 2026 follows the standard ARR format: 8 pages for long papers, 4 pages for short papers (excluding references/appendices).\n\nSources:\n- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)\n- [ARR CFP](http://aclrollingreview.org/cfp)\n\n---\n\n## 3. Novelty Check -- Routing for Retrieval in Code Tasks\n\n**There is closely related prior work, but GranRoute appears to occupy a specific niche.** Key papers to be aware of:\n\n- **ProCC (TOSEM 2025)**: Uses a contextual multi-armed bandit algorithm to adaptively select among multiple retrieval perspectives for code completion. This is the most directly comparable work -- it frames retrieval strategy selection as a bandit problem for code tasks. GranRoute needs to clearly differentiate from ProCC.\n\n- **Mix-of-Granularity (MoG, COLING 2025)**: Learns a router to dynamically select the optimal retrieval granularity for RAG based on input queries. Not code-specific, but the mechanism (a trained router selecting granularity) is very close to what GranRoute describes.\n\n- **Pre-Route (submitted to ICLR 2026)**: Routes between RAG vs. long-context using metadata, but is not code-specific and not about retrieval configuration.\n\n- **RouteLLM (2024)**: Routes between strong/weak LLMs using preference data, including a Bradley-Terry-based router. Not retrieval configuration, but the training methodology overlaps.\n\n- **\"Less is More\" (AAAI 2025)**: Adaptive program repair with preference learning, but focuses on bug localization rather than retrieval routing.\n\n**Assessment**: The specific combination of (a) learning to route retrieval *configurations* (not just granularity or model choice) for (b) code repair tasks appears novel. However, ProCC's adaptive retrieval selection for code and MoG's learned granularity router are close enough that the paper must explicitly discuss them. If GranRoute does not cite and differentiate from ProCC and MoG, that is a significant gap.\n\nSources:\n- [ProCC (arXiv/TOSEM)](https://arxiv.org/abs/2405.07530)\n- [Mix-of-Granularity (COLING 2025)](https://aclanthology.org/2025.coling-main.384/)\n- [Dense X Retrieval](https://arxiv.org/abs/2312.06648)\n- [Less is More (AAAI 2025)](https://arxiv.org/abs/2503.06510)\n\n---\n\n## 4. Venue Fit\n\n**EMNLP is a reasonable venue, but borderline.** Evidence:\n\n- EMNLP 2025 accepted \"Think-Search-Patch: A Retrieval-Augmented Reasoning Framework for Repository-Level Code Repair\" in its **Industry Track** (note: industry, not main conference).\n- EMNLP 2025 accepted \"Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs.\"\n- A retrieval-augmented code generation survey notes EMNLP had ~4.5% of peer-reviewed RACG papers, indicating modest but real representation.\n- EMNLP 2025 Findings included \"Training-Free LLM Routing for Knowledge Graph Retrieval\" and \"A Comprehensive Benchmark for Routing LLMs,\" showing routing work is accepted.\n\n**Assessment**: Code repair + retrieval routing is at the intersection of SE and NLP. EMNLP accepts such work but tends to favor it more when the NLP contribution (e.g., novel training methodology, preference modeling, language understanding) is front and center rather than pure SE evaluation. If the paper's primary contribution is the routing methodology and training signal rather than the SE evaluation, EMNLP is a good fit. If it reads more like an SE systems paper, venues like ASE/ICSE/FSE would be stronger. As a reviewer, check whether the framing emphasizes the NLP/ML contributions.\n\nSources:\n- [EMNLP 2025 Industry Track](https://2025.emnlp.org/program/ind_papers/)\n- [EMNLP 2025 Findings - Routing for KG Retrieval](https://aclanthology.org/2025.findings-emnlp.606.pdf)\n- [Routing LLMs Benchmark (EMNLP 2025 Findings)](https://aclanthology.org/2025.findings-emnlp.208.pdf)\n\n---\n\n## 5. Multi-Method Comparison as Contribution\n\n**A 5-method comparison alone is thin; the field has moved toward systematic benchmarking.** Relevant context:\n\n- **LLMRouterBench** already integrates 10+ routing methods with standardized evaluation, ablation support, and reproducible comparison.\n- **RouterEval (2025)** provides 200M+ performance records across 8,500+ LLMs and 12 benchmarks for systematic router evaluation.\n- A notable finding from \"Rethinking Predictive LLM Routing\" shows that a simple kNN baseline matches or beats complex learned routers, calling into question the value of elaborate method comparisons without novel insight.\n\n**Assessment**: If GranRoute's contribution is primarily \"we tried 5 training methods and report which works best,\" that is indeed closer to ablation-as-paper, especially given that RouterEval and LLMRouterBench already provide more comprehensive comparison frameworks. However, if the comparison yields a *novel finding* (e.g., Bradley-Terry outperforms alternatives specifically for retrieval configuration routing, or code tasks require different routing strategies than NL tasks), that transforms it from mere comparison to empirical contribution. Check whether the paper draws generalizable insights from the comparison or just reports numbers.\n\nSources:\n- [LLMRouterBench](https://www.emergentmind.com/topics/llmrouterbench)\n- [Rethinking Predictive LLM Routing (OpenReview)](https://openreview.net/forum?id=Chn50flK4X)\n- [Dynamic Model Routing Survey](https://arxiv.org/abs/2603.04445)\n\n---\n\n## 6. Bradley-Terry for Routing Configuration Selection\n\n**Yes, Bradley-Terry has been used for routing, but not specifically for retrieval configuration routing.**\n\n- **RouteLLM (2024, ICLR 2025)**: Directly uses a Bradley-Terry-based router trained on preference data from Chatbot Arena to route between strong/weak LLMs. This is the most established use of BT for routing.\n- **Prompt-to-Leaderboard (P2L, 2025)**: Extends BT to compute prompt-dependent leaderboards and route queries to optimal models. Their BT-based router hit #1 on Chatbot Arena.\n- **Beyond Bradley-Terry (ICLR 2025, ICML 2025)**: Multiple papers critique BT's limitations (intransitive preferences, expressiveness) and propose alternatives like General Preference Models.\n\n**Assessment**: Using BT for routing is well-established (RouteLLM is the canonical reference). The novelty would need to be in applying BT specifically to *retrieval configuration* selection rather than model selection -- that appears to be a new application domain. However, the paper should cite RouteLLM and acknowledge this lineage. If it presents BT for routing as novel without citing RouteLLM, that is a red flag.\n\nSources:\n- [RouteLLM (arXiv)](https://arxiv.org/abs/2406.18665)\n- [RouteLLM (ICLR 2025)](https://openreview.net/forum?id=8sSqNntaMr)\n- [Prompt-to-Leaderboard](https://arxiv.org/pdf/2502.14855)\n- [Rethinking BT in Reward Modeling (ICLR 2025)](https://github.com/holarissun/RewardModelingBeyondBradleyTerry)\n- [General Preference Model (ICML 2025)](https://github.com/general-preference/general-preference-model)\n\n---\n\n## Summary for Your Review\n\n| Question | Verdict |\n|---|---|\n| May 25 deadline | Confirmed correct |\n| 4-page short paper | Confirmed correct |\n| Novelty | Niche is defensible but must cite ProCC and MoG; differentiation needed |\n| Venue fit | Acceptable if NLP/ML contribution is foregrounded; borderline if SE-heavy |\n| 5-method comparison | Risky as sole contribution; needs novel insight, not just numbers |\n| BT for routing | Well-established for model routing (RouteLLM); new for retrieval config routing if properly framed |"
      }
    ],
    "totalDurationMs": 109967,
    "totalTokens": 26366,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2627,
      "cache_read_input_tokens": 21323,
      "output_tokens": 2415,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2627
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2415,
          "cache_read_input_tokens": 21323,
          "cache_creation_input_tokens": 2627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2627,
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
  "sourceToolAssistantUUID": "cda8961b-d892-4f40-b515-22c771a306ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-11T23:41:23.387Z_

<details><summary>↩ Tool result · `toolu_01A8i3EytBdyDekcWSAJg2BR`</summary>

```text
Now I have comprehensive results. Here is my consolidated report.

---

## Competitor Analysis for GranRoute: Papers Potentially Missing from the Proposal

Below are papers found across 10 search queries, organized by relevance category. I have excluded the 17 already-cited papers (RouteLLM, RADAR, BEST-Route, Route-To-Reason, LTRR, Triage, SIADAFIX, AdaPatcher, AdaEdit, SWEzze, SWE-Pruner, CodeScout, ARISE, RPO, DRO, ReCode, RGFL).

---

### TIER 1: HIGH RELEVANCE -- Directly overlapping with GranRoute's contributions

**1. "A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks"**
- arXiv:2604.00167, April 2026
- **Why critical:** This paper directly studies the impact of different FL granularity levels (file, function, line) on repository-scale repair using SWE-bench Mini, finding function-level yields the highest repair rate but the ideal granularity is task-dependent. This is extremely close to GranRoute's core thesis about routing granularity. If not cited, it should be.

**2. "On the Role of Fault Localization Context for LLM-Based Program Repair"**
- arXiv:2604.05481, April 2026
- **Why critical:** Large-scale empirical study on 500 SWE-bench Verified instances evaluating 61 configurations varying file-level, element-level, and line-level context. Finds more context does not consistently help, file-level localization gives 15-17x improvement, and line-level context can degrade performance via noise. Directly validates GranRoute's premise that retrieval configuration matters.

**3. Mix-of-Granularity (MoG)**
- COLING 2025, arXiv:2406.00456
- **Why critical:** Proposes a router that dynamically selects optimal chunking granularity for RAG based on input queries, trained with soft labels. The granularity routing concept is very similar to GranRoute's granularity selection, though applied to general QA rather than code repair.

**4. RAGRouter**
- NeurIPS 2025, arXiv:2505.23052
- **Why relevant:** Routes queries to the best retrieval-augmented LLM using document embeddings and RAG capability embeddings with contrastive learning. First work on LLM routing in the RAG setting. The routing-over-retrieval-configurations concept overlaps with GranRoute.

**5. LongCodeZip**
- ASE 2025, arXiv:2510.00446
- **Why relevant:** Code-specific compression framework with two-stage strategy: coarse-grained (function-level ranking by conditional perplexity) then fine-grained (block-level pruning via knapsack). Uses adaptive budget allocation proportional to function importance. The adaptive context budget idea parallels GranRoute's context budget routing.

**6. "Compressing Code Context for LLM-based Issue Resolution" (the paper describing SWEzze training)**
- arXiv:2603.28119, March 2026
- **Why relevant:** Although SWEzze is already cited, this paper introduces Oracle-guided Code Distillation (OCD) which finds minimal sufficient context subsequences for code repair. The method of learning what context is necessary vs. noise is conceptually related to GranRoute's context budget optimization. Check whether this specific paper (vs. just the SWEzze tool) is cited.

---

### TIER 2: STRONG RELEVANCE -- Overlapping techniques or problem formulation

**7. RouteRAG**
- arXiv:2512.09487, December 2025
- Routes between passage, graph, and hybrid retrieval modes using two-stage RL. End-to-end learned routing over retrieval strategies is conceptually close to GranRoute's retrieval configuration routing.

**8. Router-R1**
- NeurIPS 2025, arXiv:2506.09033
- RL-based multi-round routing and aggregation framework that interleaves "think" and "route" actions. Uses cost-aware reward. The cost-performance trade-off optimization parallels GranRoute's budget-aware routing.

**9. GraphRouter**
- ICLR 2025, arXiv:2410.03834
- Graph-based router for LLM selection using heterogeneous graphs of tasks, queries, and LLMs. Generalizes to new LLMs without retraining. Relevant as a routing methodology competitor.

**10. GraphRAG-Router**
- arXiv:2604.16401, April 2026
- Hierarchical routing over heterogeneous GraphRAGs and generator LLMs using RL with curriculum cost-aware reward. Routes based on query complexity. Relevant for its cost-efficient routing over retrieval configurations.

**11. BoundaryRouter ("Learning Agent Routing From Early Experience")**
- arXiv:2605.07180, May 2026
- Training-free routing framework using early behavioral experience to decide between direct LLM inference vs. agent escalation. Reduces inference time by 60.6%. Relevant as a lightweight routing alternative.

**12. RouteProfile**
- arXiv:2605.00180, May 2026
- General framework for designing LLM profiles for routing across four dimensions (organizational form, representation type, aggregation depth, learning configuration). Systematic study of routing design choices that could inform GranRoute's design.

**13. CigaR**
- arXiv:2402.06598, 2024 (ICSE track)
- Cost-efficient program repair with three-stage prompt design (initiation, improvement, multiplication). Achieves 73% token cost reduction. Relevant as a baseline for cost-efficient repair without adaptive routing.

---

### TIER 3: MODERATE RELEVANCE -- Related problem domain

**14. RepoRepair**
- arXiv:2603.01048, March 2026
- Uses LLM-generated hierarchical code documentation (function-to-file) for repository-level FL and repair. Achieves 45.7% on SWE-bench Lite. Relevant as a retrieval-based repo-level repair competitor.

**15. RelRepair**
- arXiv:2509.16701, September 2025
- RAG approach for program repair with query rewriting, dataset indexing, and similarity retrieval of function signatures and code snippets. Relevant as a retrieval-augmented repair system.

**16. PatchRecall**
- arXiv:2604.10481, April 2026
- Combines codebase retrieval (issue-to-code matching) with history-based retrieval (similar past issues) for file retrieval in APR, with reranking. Directly addresses retrieval quality for code repair.

**17. ReAPR**
- Software Quality Journal 2025
- Retrieval-augmented program repair using BM25/DPR to fetch similar bug-fix pairs from a curated database. Relevant as a retrieval-augmented repair baseline.

**18. MemFL**
- arXiv:2506.03585, 2025
- LLM-based fault localization with external memory (static project summaries + dynamic debugging guidance). Localizes 12.7% more bugs than baselines. Relevant for adaptive, memory-augmented FL.

**19. FlexFL**
- IEEE TSE 2025, arXiv:2411.10714
- Two-stage FL framework: first reduces search space with traditional FL, then uses LLMs to refine. Works with open-source LLMs. Relevant as a flexible FL approach.

**20. LLM4FL**
- OpenReview (under review)
- Multi-agent FL with three specialized agents (Context Extraction, Debugger with Graph-RAG navigation, Reviewer with verbal RL). 18.55% improvement in Top-1 accuracy. Relevant for multi-agent adaptive FL.

**21. LIDL**
- arXiv:2601.05539, January 2026
- Knowledge graph + multi-agent analysis for LLM integration defect localization. First to combine code knowledge graphs with LLM semantic reasoning. Relevant for graph-enhanced FL.

**22. "Towards Defect-Type-Aware Adaptive Program Repair"**
- Software Quality Journal 2026
- Stage-wise approach that adapts repair strategy based on defect type using LLMs. The defect-type-aware adaptation is philosophically similar to GranRoute's per-instance routing.

**23. RepairAgent**
- ICSE 2025, arXiv:2403.17134
- Autonomous LLM agent that dynamically interleaves information gathering, repair ingredient collection, and fix validation using a finite state machine. Relevant as an adaptive repair agent baseline.

**24. SWE-ContextBench**
- arXiv:2602.08316, February 2026
- Benchmark evaluating how accurately/efficiently agents solve related issues when prior context is available. Finds correctly selected context improves resolution while unfiltered context hurts. Validates the premise that context selection matters.

**25. "Learning to Route: A Rule-Driven Agent Framework for Hybrid-Source Retrieval-Augmented Generation"**
- arXiv:2510.02388, October 2025
- Rule-driven routing agent for hybrid-source RAG. Relevant for learned routing over heterogeneous retrieval sources.

---

### TIER 4: CONTEXTUAL / SURVEY PAPERS

**26. "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches"**
- arXiv:2510.04905, October 2025
- Comprehensive survey covering retrieval granularity levels (directory, module, class/function, line) for code generation. Useful for positioning GranRoute's contribution.

**27. "A Survey of LLM-based Automated Program Repair" (TOSEM 2026)**
- arXiv:2506.23749
- Systematic survey categorizing APR into fine-tuning, prompting, procedural, and agentic paradigms with RAG/AAG cross-cutting concerns. Useful for situating GranRoute.

---

### Summary of Most Critical Missing Competitors

The papers most likely to be flagged by reviewers as missing are:

1. **"Impact of FL Granularity for Repository-Scale Code Repair"** (arXiv:2604.00167) -- directly studies the same granularity question on SWE-bench
2. **"On the Role of FL Context for LLM-Based Program Repair"** (arXiv:2604.05481) -- 61-configuration empirical study on context impact
3. **Mix-of-Granularity** (COLING 2025) -- routes optimal chunking granularity, very close concept
4. **RAGRouter** (NeurIPS 2025) -- routing in RAG settings with contrastive learning
5. **LongCodeZip** (ASE 2025) -- adaptive budget allocation for code compression
6. **Router-R1** (NeurIPS 2025) -- RL-based multi-round routing with cost-aware reward
7. **RouteRAG** (arXiv Dec 2025) -- RL for routing between retrieval modes
8. **PatchRecall** (arXiv Apr 2026) -- hybrid retrieval for APR on SWE-bench
9. **RepoRepair** (arXiv Mar 2026) -- hierarchical documentation for repo-level repair

Sources:
- [FL Granularity Study](https://arxiv.org/abs/2604.00167)
- [FL Context Role](https://arxiv.org/abs/2604.05481)
- [Mix-of-Granularity](https://aclanthology.org/2025.coling-main.384/)
- [RAGRouter](https://arxiv.org/abs/2505.23052)
- [LongCodeZip](https://arxiv.org/abs/2510.00446)
- [Router-R1](https://arxiv.org/abs/2506.09033)
- [RouteRAG](https://arxiv.org/abs/2512.09487)
- [PatchRecall](https://arxiv.org/abs/2604.10481)
- [RepoRepair](https://arxiv.org/abs/2603.01048)
- [GraphRouter](https://arxiv.org/abs/2410.03834)
- [GraphRAG-Router](https://arxiv.org/html/2604.16401v1)
- [BoundaryRouter](https://arxiv.org/abs/2605.07180)
- [RouteProfile](https://arxiv.org/abs/2605.00180)
- [CigaR](https://arxiv.org/abs/2402.06598)
- [RelRepair](https://arxiv.org/abs/2509.16701)
- [ReAPR](https://link.springer.com/article/10.1007/s11219-025-09728-1)
- [MemFL](https://arxiv.org/abs/2506.03585)
- [FlexFL](https://arxiv.org/abs/2411.10714)
- [LLM4FL](https://openreview.net/forum?id=z91EvZbSI1)
- [LIDL](https://arxiv.org/abs/2601.05539)
- [Defect-Type-Aware APR](https://link.springer.com/article/10.1007/s11219-026-09751-w)
- [RepairAgent](https://arxiv.org/abs/2403.17134)
- [SWE-ContextBench](https://arxiv.org/abs/2602.08316)
- [SWEzze/OCD paper](https://arxiv.org/abs/2603.28119)
- [RACG Survey](https://arxiv.org/abs/2510.04905)
- [LLM4APR Survey](https://arxiv.org/abs/2506.23749)

agentId: a091ca136193f2c66 (use SendMessage with to: 'a091ca136193f2c66' to continue this agent)
&lt;usage>total_tokens: 52410
tool_uses: 40
duration_ms: 193294&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42e5ff9c-b030-4af5-9c05-41458ba0ca3d",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "57d87649-cf32-484c-8d37-262eafaa5f11",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper proposal about \"GranRoute\" — learning to route retrieval configurations (granularity + context budget) for repository-level code repair. I need to find competitors the proposal may have missed. Search for:\n\n1. Search: \"adaptive retrieval configuration code repair 2025 2026\" — are there other papers that adaptively select retrieval strategies for code repair?\n\n2. Search: \"retrieval routing LLM code 2026\" — anything about routing retrieval for code tasks?\n\n3. Search: \"configuration selection software engineering LLM 2025 2026\" — automatic configuration selection for SE agents?\n\n4. Search: \"context window optimization code repair 2025 2026\" — optimizing context for code repair?\n\n5. Search: \"SWE-bench adaptive agent 2026\" — any SWE-bench agents that adaptively change their strategies?\n\n6. Search: \"meta-learning code repair retrieval 2025 2026\" — meta-learning approaches for code repair?\n\n7. Search: \"dynamic fault localization LLM 2026\" — dynamic/adaptive fault localization?\n\n8. Search: \"Agentless adaptive configuration 2026\" — any work extending Agentless with adaptive configs?\n\n9. Search for \"MASAI\" or \"CodeR\" or \"AutoCodeRover adaptive\" — known SWE-bench agents that might have adaptive retrieval.\n\n10. Search: \"learn to retrieve code generation 2025 2026\" — learning retrieval strategies for code tasks.\n\nFor each search, report the most relevant results. Focus on papers from 2025-2026 that are NOT already cited in the proposal. The cited papers include: RouteLLM, RADAR, BEST-Route, Route-To-Reason, LTRR, Triage, SIADAFIX, AdaPatcher, AdaEdit, SWEzze, SWE-Pruner, CodeScout, ARISE, RPO, DRO, ReCode, RGFL.\n\nReport concisely: paper title, venue/arXiv, and why it's relevant or not.",
    "agentId": "a091ca136193f2c66",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive results. Here is my consolidated report.\n\n---\n\n## Competitor Analysis for GranRoute: Papers Potentially Missing from the Proposal\n\nBelow are papers found across 10 search queries, organized by relevance category. I have excluded the 17 already-cited papers (RouteLLM, RADAR, BEST-Route, Route-To-Reason, LTRR, Triage, SIADAFIX, AdaPatcher, AdaEdit, SWEzze, SWE-Pruner, CodeScout, ARISE, RPO, DRO, ReCode, RGFL).\n\n---\n\n### TIER 1: HIGH RELEVANCE -- Directly overlapping with GranRoute's contributions\n\n**1. \"A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks\"**\n- arXiv:2604.00167, April 2026\n- **Why critical:** This paper directly studies the impact of different FL granularity levels (file, function, line) on repository-scale repair using SWE-bench Mini, finding function-level yields the highest repair rate but the ideal granularity is task-dependent. This is extremely close to GranRoute's core thesis about routing granularity. If not cited, it should be.\n\n**2. \"On the Role of Fault Localization Context for LLM-Based Program Repair\"**\n- arXiv:2604.05481, April 2026\n- **Why critical:** Large-scale empirical study on 500 SWE-bench Verified instances evaluating 61 configurations varying file-level, element-level, and line-level context. Finds more context does not consistently help, file-level localization gives 15-17x improvement, and line-level context can degrade performance via noise. Directly validates GranRoute's premise that retrieval configuration matters.\n\n**3. Mix-of-Granularity (MoG)**\n- COLING 2025, arXiv:2406.00456\n- **Why critical:** Proposes a router that dynamically selects optimal chunking granularity for RAG based on input queries, trained with soft labels. The granularity routing concept is very similar to GranRoute's granularity selection, though applied to general QA rather than code repair.\n\n**4. RAGRouter**\n- NeurIPS 2025, arXiv:2505.23052\n- **Why relevant:** Routes queries to the best retrieval-augmented LLM using document embeddings and RAG capability embeddings with contrastive learning. First work on LLM routing in the RAG setting. The routing-over-retrieval-configurations concept overlaps with GranRoute.\n\n**5. LongCodeZip**\n- ASE 2025, arXiv:2510.00446\n- **Why relevant:** Code-specific compression framework with two-stage strategy: coarse-grained (function-level ranking by conditional perplexity) then fine-grained (block-level pruning via knapsack). Uses adaptive budget allocation proportional to function importance. The adaptive context budget idea parallels GranRoute's context budget routing.\n\n**6. \"Compressing Code Context for LLM-based Issue Resolution\" (the paper describing SWEzze training)**\n- arXiv:2603.28119, March 2026\n- **Why relevant:** Although SWEzze is already cited, this paper introduces Oracle-guided Code Distillation (OCD) which finds minimal sufficient context subsequences for code repair. The method of learning what context is necessary vs. noise is conceptually related to GranRoute's context budget optimization. Check whether this specific paper (vs. just the SWEzze tool) is cited.\n\n---\n\n### TIER 2: STRONG RELEVANCE -- Overlapping techniques or problem formulation\n\n**7. RouteRAG**\n- arXiv:2512.09487, December 2025\n- Routes between passage, graph, and hybrid retrieval modes using two-stage RL. End-to-end learned routing over retrieval strategies is conceptually close to GranRoute's retrieval configuration routing.\n\n**8. Router-R1**\n- NeurIPS 2025, arXiv:2506.09033\n- RL-based multi-round routing and aggregation framework that interleaves \"think\" and \"route\" actions. Uses cost-aware reward. The cost-performance trade-off optimization parallels GranRoute's budget-aware routing.\n\n**9. GraphRouter**\n- ICLR 2025, arXiv:2410.03834\n- Graph-based router for LLM selection using heterogeneous graphs of tasks, queries, and LLMs. Generalizes to new LLMs without retraining. Relevant as a routing methodology competitor.\n\n**10. GraphRAG-Router**\n- arXiv:2604.16401, April 2026\n- Hierarchical routing over heterogeneous GraphRAGs and generator LLMs using RL with curriculum cost-aware reward. Routes based on query complexity. Relevant for its cost-efficient routing over retrieval configurations.\n\n**11. BoundaryRouter (\"Learning Agent Routing From Early Experience\")**\n- arXiv:2605.07180, May 2026\n- Training-free routing framework using early behavioral experience to decide between direct LLM inference vs. agent escalation. Reduces inference time by 60.6%. Relevant as a lightweight routing alternative.\n\n**12. RouteProfile**\n- arXiv:2605.00180, May 2026\n- General framework for designing LLM profiles for routing across four dimensions (organizational form, representation type, aggregation depth, learning configuration). Systematic study of routing design choices that could inform GranRoute's design.\n\n**13. CigaR**\n- arXiv:2402.06598, 2024 (ICSE track)\n- Cost-efficient program repair with three-stage prompt design (initiation, improvement, multiplication). Achieves 73% token cost reduction. Relevant as a baseline for cost-efficient repair without adaptive routing.\n\n---\n\n### TIER 3: MODERATE RELEVANCE -- Related problem domain\n\n**14. RepoRepair**\n- arXiv:2603.01048, March 2026\n- Uses LLM-generated hierarchical code documentation (function-to-file) for repository-level FL and repair. Achieves 45.7% on SWE-bench Lite. Relevant as a retrieval-based repo-level repair competitor.\n\n**15. RelRepair**\n- arXiv:2509.16701, September 2025\n- RAG approach for program repair with query rewriting, dataset indexing, and similarity retrieval of function signatures and code snippets. Relevant as a retrieval-augmented repair system.\n\n**16. PatchRecall**\n- arXiv:2604.10481, April 2026\n- Combines codebase retrieval (issue-to-code matching) with history-based retrieval (similar past issues) for file retrieval in APR, with reranking. Directly addresses retrieval quality for code repair.\n\n**17. ReAPR**\n- Software Quality Journal 2025\n- Retrieval-augmented program repair using BM25/DPR to fetch similar bug-fix pairs from a curated database. Relevant as a retrieval-augmented repair baseline.\n\n**18. MemFL**\n- arXiv:2506.03585, 2025\n- LLM-based fault localization with external memory (static project summaries + dynamic debugging guidance). Localizes 12.7% more bugs than baselines. Relevant for adaptive, memory-augmented FL.\n\n**19. FlexFL**\n- IEEE TSE 2025, arXiv:2411.10714\n- Two-stage FL framework: first reduces search space with traditional FL, then uses LLMs to refine. Works with open-source LLMs. Relevant as a flexible FL approach.\n\n**20. LLM4FL**\n- OpenReview (under review)\n- Multi-agent FL with three specialized agents (Context Extraction, Debugger with Graph-RAG navigation, Reviewer with verbal RL). 18.55% improvement in Top-1 accuracy. Relevant for multi-agent adaptive FL.\n\n**21. LIDL**\n- arXiv:2601.05539, January 2026\n- Knowledge graph + multi-agent analysis for LLM integration defect localization. First to combine code knowledge graphs with LLM semantic reasoning. Relevant for graph-enhanced FL.\n\n**22. \"Towards Defect-Type-Aware Adaptive Program Repair\"**\n- Software Quality Journal 2026\n- Stage-wise approach that adapts repair strategy based on defect type using LLMs. The defect-type-aware adaptation is philosophically similar to GranRoute's per-instance routing.\n\n**23. RepairAgent**\n- ICSE 2025, arXiv:2403.17134\n- Autonomous LLM agent that dynamically interleaves information gathering, repair ingredient collection, and fix validation using a finite state machine. Relevant as an adaptive repair agent baseline.\n\n**24. SWE-ContextBench**\n- arXiv:2602.08316, February 2026\n- Benchmark evaluating how accurately/efficiently agents solve related issues when prior context is available. Finds correctly selected context improves resolution while unfiltered context hurts. Validates the premise that context selection matters.\n\n**25. \"Learning to Route: A Rule-Driven Agent Framework for Hybrid-Source Retrieval-Augmented Generation\"**\n- arXiv:2510.02388, October 2025\n- Rule-driven routing agent for hybrid-source RAG. Relevant for learned routing over heterogeneous retrieval sources.\n\n---\n\n### TIER 4: CONTEXTUAL / SURVEY PAPERS\n\n**26. \"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches\"**\n- arXiv:2510.04905, October 2025\n- Comprehensive survey covering retrieval granularity levels (directory, module, class/function, line) for code generation. Useful for positioning GranRoute's contribution.\n\n**27. \"A Survey of LLM-based Automated Program Repair\" (TOSEM 2026)**\n- arXiv:2506.23749\n- Systematic survey categorizing APR into fine-tuning, prompting, procedural, and agentic paradigms with RAG/AAG cross-cutting concerns. Useful for situating GranRoute.\n\n---\n\n### Summary of Most Critical Missing Competitors\n\nThe papers most likely to be flagged by reviewers as missing are:\n\n1. **\"Impact of FL Granularity for Repository-Scale Code Repair\"** (arXiv:2604.00167) -- directly studies the same granularity question on SWE-bench\n2. **\"On the Role of FL Context for LLM-Based Program Repair\"** (arXiv:2604.05481) -- 61-configuration empirical study on context impact\n3. **Mix-of-Granularity** (COLING 2025) -- routes optimal chunking granularity, very close concept\n4. **RAGRouter** (NeurIPS 2025) -- routing in RAG settings with contrastive learning\n5. **LongCodeZip** (ASE 2025) -- adaptive budget allocation for code compression\n6. **Router-R1** (NeurIPS 2025) -- RL-based multi-round routing with cost-aware reward\n7. **RouteRAG** (arXiv Dec 2025) -- RL for routing between retrieval modes\n8. **PatchRecall** (arXiv Apr 2026) -- hybrid retrieval for APR on SWE-bench\n9. **RepoRepair** (arXiv Mar 2026) -- hierarchical documentation for repo-level repair\n\nSources:\n- [FL Granularity Study](https://arxiv.org/abs/2604.00167)\n- [FL Context Role](https://arxiv.org/abs/2604.05481)\n- [Mix-of-Granularity](https://aclanthology.org/2025.coling-main.384/)\n- [RAGRouter](https://arxiv.org/abs/2505.23052)\n- [LongCodeZip](https://arxiv.org/abs/2510.00446)\n- [Router-R1](https://arxiv.org/abs/2506.09033)\n- [RouteRAG](https://arxiv.org/abs/2512.09487)\n- [PatchRecall](https://arxiv.org/abs/2604.10481)\n- [RepoRepair](https://arxiv.org/abs/2603.01048)\n- [GraphRouter](https://arxiv.org/abs/2410.03834)\n- [GraphRAG-Router](https://arxiv.org/html/2604.16401v1)\n- [BoundaryRouter](https://arxiv.org/abs/2605.07180)\n- [RouteProfile](https://arxiv.org/abs/2605.00180)\n- [CigaR](https://arxiv.org/abs/2402.06598)\n- [RelRepair](https://arxiv.org/abs/2509.16701)\n- [ReAPR](https://link.springer.com/article/10.1007/s11219-025-09728-1)\n- [MemFL](https://arxiv.org/abs/2506.03585)\n- [FlexFL](https://arxiv.org/abs/2411.10714)\n- [LLM4FL](https://openreview.net/forum?id=z91EvZbSI1)\n- [LIDL](https://arxiv.org/abs/2601.05539)\n- [Defect-Type-Aware APR](https://link.springer.com/article/10.1007/s11219-026-09751-w)\n- [RepairAgent](https://arxiv.org/abs/2403.17134)\n- [SWE-ContextBench](https://arxiv.org/abs/2602.08316)\n- [SWEzze/OCD paper](https://arxiv.org/abs/2603.28119)\n- [RACG Survey](https://arxiv.org/abs/2510.04905)\n- [LLM4APR Survey](https://arxiv.org/abs/2506.23749)"
      }
    ],
    "totalDurationMs": 193294,
    "totalTokens": 52410,
    "totalToolUseCount": 40,
    "usage": {
      "input_tokens": 876,
      "cache_creation_input_tokens": 2046,
      "cache_read_input_tokens": 46071,
      "output_tokens": 3417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2046
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 876,
          "output_tokens": 3417,
          "cache_read_input_tokens": 46071,
          "cache_creation_input_tokens": 2046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2046,
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
  "sourceToolAssistantUUID": "42e5ff9c-b030-4af5-9c05-41458ba0ca3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "57d87649-cf32-484c-8d37-262eafaa5f11",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate GranRoute: Configuration Routing for Code Repair",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Assistant

_source line 23 · 2026-05-11T23:42:16.198Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have thorough research results. Let me synthesize my findings and produce the review.

Key findings from my research:

**References verified**: All 10 key references check out — correct arXiv IDs, venues, and descriptions.

**Missing competitors identified**:
1. **Mix-of-Granularity (MoG, COLING 2025)** — This is a CRITICAL miss. MoG proposes a router that dynamically selects optimal chunking granularity for RAG based on input queries. This is essentially the same concept as GranRoute but for general QA instead of code repair. The proposal does not cite this paper.


2. **RAGRouter (NeurIPS 2025)** — Routes queries to the best retrieval-augmented LLM, relevant as a routing-over-retrieval-configurations approach.
3. **ProCC (TOSEM 2025)** — Uses contextual multi-armed bandit to adaptively select retrieval perspectives for code completion, which is quite relevant.
4. **RouteRAG (arXiv Dec 2025)** — Routes between passage, graph, and hybrid retrieval modes using RL.
5. **LongCodeZip (ASE 2025)** — Adaptive budget allocation for code compression.

Now I need to assess the feasibility of the approach with Qwen3-C.

The costs look reasonable—Claude-Next instances at $0.08 each and a total API budget around $1,200-$1,300 is workable. The 14-day timeline is aggressive but doable, and SWE-bench-Live's ~1,890 instances give me enough data to evaluate properly. Training the router on 8 H100-hours is plenty, and staying under 40 H100-hours total is realistic.

EMNLP could work as a venue if I emphasize the NLP and ML contributions strongly. The main novelty challenge is that MoG already does routing granularity for RAG, but GranRoute differentiates itself through the code repair focus and the comprehensive multi-method comparison. ProCC also tackles adaptive retrieval selection for code, so I need to be clear about what makes this distinct.

Looking at the improvements from the last round, I've addressed the key feedback—added the five-method comparison instead of relying solely on DPO, cited RouteLLM and RADAR, consolidated the contributions, included the headroom pilot with a go/no-go decision point, specified the SWE-bench-Live evaluation using ~100 recent instances, and upgraded to CodeSage-base with UniXcoder as an ablation. The core contribution is applying routing methodology to code repair, which is a solid application but I need to extract deeper insights from the multi-method comparison to strengthen the novelty argument.

On novelty, the routing idea itself isn't entirely new—MoG handles granularity routing for RAG and ProCC does adaptive retrieval for code, both of which I should have cited. The multi-method comparison risks becoming just an ablation study, but the specific combination of routing retrieval configurations (granularity plus budget) for code repair using both natural language and code features does offer enough novelty to stand on its own. Feasibility looks solid with realistic budget constraints around $1,200 in API costs and under 40 H100-hours, though the 14-day timeline is tight and API rate limits could become a bottleneck. The go/no-go gate helps mitigate risk, though there's a concern that the headroom might be too small to enable meaningful routing decisions.

The proposal itself is well-structured with clear phases and cost breakdowns, though I'm missing citations for MoG, ProCC, and RAGRouter—all recent work in routing and adaptive retrieval that directly compete with this approach. Impact-wise, if the headroom turns out to be substantial, this could be a practical contribution, but fundamentally it's an application of routing to a new domain, which limits the field-level impact. The insights about which natural language features predict optimal granularity could be interesting, but for an EMNLP short paper, the contribution feels incremental.

Looking at the scores—3.5 overall—I'm below the 4.0 threshold, though this is Round 4 and the proposal has improved. The core issues are the missing competitors, which are fixable, but the deeper problem is that novelty is limited. This is essentially applying existing routing methods to a new setting, and without novel findings from the multi-method comparison, the contribution becomes thin. That said, for a short paper format, there's still potential here if the empirical results are strong enough. Comparing five existing methods on a new task is fairly standard work, so novelty sits at 3/5, though the clear gap and connection between established areas could push it higher for a short paper venue. Feasibility is solid at 4/5, clarity at 4/5, and impact at 3/5 for practical but incremental work—averaging 3.5, which falls short of the 4.0 bar. The missing competitors like MoG and ProCC are the main fixable issue, and addressing them could strengthen the novelty argument enough to warrant a revise verdict rather than reject.

Reconsidering the proposal's maturity after four rounds of iteration, those missing competitors aren't fatal since they operate in different domains and the differentiation is defensible. For EMNLP Findings this could work, but Main track requires stronger novelty. Since the proposal targets both, I'm settling on revise with concrete feedback: cite MoG and ProCC, sharpen the differentiation, and ensure the multi-method comparison yields insights beyond raw performance numbers. Final scores remain Novelty 3, Feasibility 4, Clarity 4, Impact 3, averaging 3.5.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57d87649-cf32-484c-8d37-262eafaa5f11",
  "isSidechain": false,
  "requestId": "req_011CawfboFC8s8t6AgLwVGBB",
  "type": "assistant",
  "uuid": "a59fbd3c-8baf-4b2e-a5d7-088fb400af9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xJNGVXtMHQiYQCunP3oCN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5050,
      "cache_creation_input_tokens": 5187,
      "cache_read_input_tokens": 33471,
      "output_tokens": 2081,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5050,
          "output_tokens": 2081,
          "cache_read_input_tokens": 33471,
          "cache_creation_input_tokens": 5187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5187
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

_source line 24 · 2026-05-11T23:42:16.226Z_

Now let me check the most critical missing competitor — Mix-of-Granularity — more closely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a59fbd3c-8baf-4b2e-a5d7-088fb400af9c",
  "isSidechain": false,
  "requestId": "req_011CawfboFC8s8t6AgLwVGBB",
  "type": "assistant",
  "uuid": "4ca3d8b2-c8c7-414b-ac2e-7ec2f911d1ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xJNGVXtMHQiYQCunP3oCN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5050,
      "cache_creation_input_tokens": 5187,
      "cache_read_input_tokens": 33471,
      "output_tokens": 2081,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5050,
          "output_tokens": 2081,
          "cache_read_input_tokens": 33471,
          "cache_creation_input_tokens": 5187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5187
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

_source line 25 · 2026-05-11T23:42:16.250Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01H9RTafXQ6z3n3PjyLLPpSw`</summary>

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
  "parentUuid": "4ca3d8b2-c8c7-414b-ac2e-7ec2f911d1ed",
  "isSidechain": false,
  "requestId": "req_011CawfboFC8s8t6AgLwVGBB",
  "type": "assistant",
  "uuid": "dc03b8b6-991d-466d-98a1-f10a31ea84a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xJNGVXtMHQiYQCunP3oCN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5050,
      "cache_creation_input_tokens": 5187,
      "cache_read_input_tokens": 33471,
      "output_tokens": 2081,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5187,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5050,
          "output_tokens": 2081,
          "cache_read_input_tokens": 33471,
          "cache_creation_input_tokens": 5187,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5187
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

_source line 26 · 2026-05-11T23:42:16.261Z_

<details><summary>↩ Tool result · `toolu_01H9RTafXQ6z3n3PjyLLPpSw`</summary>

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
  "parentUuid": "dc03b8b6-991d-466d-98a1-f10a31ea84a5",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "05cc9d6e-88d8-4e0b-89a3-8ae2e0ce0f79",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "dc03b8b6-991d-466d-98a1-f10a31ea84a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-11T23:42:19.519Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the most critical missing competitors: Mix-of-Granularity (MoG) and ProCC.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05cc9d6e-88d8-4e0b-89a3-8ae2e0ce0f79",
  "isSidechain": false,
  "requestId": "req_011CawffhW2gJVc1pLJiQYxv",
  "type": "assistant",
  "uuid": "dc7512ff-3cfc-4722-9c3e-ec9fb1acf908",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8SdQo4Z5tXPeii2YjuCz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8145,
      "cache_read_input_tokens": 38658,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8145,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 38658,
          "cache_creation_input_tokens": 8145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8145
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

_source line 28 · 2026-05-11T23:42:20.488Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WtEtYuhQmE4sYttfYguv3Q`</summary>

```json
{
  "query": "Mix-of-Granularity MoG dynamic chunking granularity RAG routing COLING 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc7512ff-3cfc-4722-9c3e-ec9fb1acf908",
  "isSidechain": false,
  "requestId": "req_011CawffhW2gJVc1pLJiQYxv",
  "type": "assistant",
  "uuid": "85375956-975f-4c51-81e4-cb1aa5c17333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8SdQo4Z5tXPeii2YjuCz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8145,
      "cache_read_input_tokens": 38658,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8145,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 38658,
          "cache_creation_input_tokens": 8145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8145
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

_source line 29 · 2026-05-11T23:42:21.487Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013eRL9w54xdMGcsgC8NyW7N`</summary>

```json
{
  "query": "ProCC adaptive retrieval strategy code completion multi-armed bandit TOSEM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85375956-975f-4c51-81e4-cb1aa5c17333",
  "isSidechain": false,
  "requestId": "req_011CawffhW2gJVc1pLJiQYxv",
  "type": "assistant",
  "uuid": "62ab5632-99c5-4407-a0af-e019a12b7f39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8SdQo4Z5tXPeii2YjuCz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8145,
      "cache_read_input_tokens": 38658,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8145,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 38658,
          "cache_creation_input_tokens": 8145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8145
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

_source line 30 · 2026-05-11T23:42:21.939Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rir5GSYdqAn6JjeA9QqMhB`</summary>

```json
{
  "query": "RAGRouter NeurIPS 2025 routing retrieval augmented LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62ab5632-99c5-4407-a0af-e019a12b7f39",
  "isSidechain": false,
  "requestId": "req_011CawffhW2gJVc1pLJiQYxv",
  "type": "assistant",
  "uuid": "e6bbc9ae-580c-4cff-a044-04a00a7c5dcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SS8SdQo4Z5tXPeii2YjuCz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8145,
      "cache_read_input_tokens": 38658,
      "output_tokens": 226,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8145,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 226,
          "cache_read_input_tokens": 38658,
          "cache_creation_input_tokens": 8145,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8145
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

_source line 31 · 2026-05-11T23:42:26.873Z_

<details><summary>↩ Tool result · `toolu_01WtEtYuhQmE4sYttfYguv3Q`</summary>

```text
Web search results for query: "Mix-of-Granularity MoG dynamic chunking granularity RAG routing COLING 2025"

Links: [{"title":"Optimize the Chunking Granularity for Retrieval- ...","url":"https://aclanthology.org/2025.coling-main.384.pdf"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.384/"},{"title":"GitHub - ZGChung/Mix-of-Granularity: [COLING 2025] Mix-of-Granularity paper","url":"https://github.com/ZGChung/Mix-of-Granularity"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2406.00456v1"},{"title":"[2406.00456] Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2406.00456"},{"title":"Paper page - Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://huggingface.co/papers/2406.00456"},{"title":"[PDF] UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities | Semantic Scholar","url":"https://www.semanticscholar.org/paper/UniversalRAG:-Retrieval-Augmented-Generation-over-Yeo-Kim/94cf17cdb8df7016ebe7decb91257a2d0b14d1e8"},{"title":"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation","url":"https://powerdrill.ai/discover/discover-Mix-of-Granularity-Optimize-the-clx4ktn2104l6019n4h6q5sy2"},{"title":"Revisiting Chunking in the RAG Pipeline - by Florian","url":"https://aiexpjourney.substack.com/p/revisiting-chunking-in-the-rag-pipeline"},{"title":"A Deep-Dive into Chunking Strategy, Chunking Methods, and Precision in RAG Applications - Superteams.ai","url":"https://www.superteams.ai/blog/a-deep-dive-into-chunking-strategy-chunking-methods-and-precision-in-rag-applications"}]

I found relevant results for your query. Here's what I found:

## Mix-of-Granularity (MoG) - COLING 2025

The paper "Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation" was presented at the 31st International Conference on Computational Linguistics (COLING) held in Abu Dhabi, UAE in January 2025.

### Key Concept

Mix-of-Granularity (MoG) is a method that dynamically determines the optimal granularity of a knowledge source based on input queries using a router, inspired by Mix-of-Expert. The router is efficiently trained with a newly proposed loss function employing soft labels.

### Problem It Addresses

Integrating information from various reference databases is a major challenge for RAG systems because each knowledge source adopts a unique data structure and follows different conventions, and retrieving from multiple knowledge sources with one fixed strategy usually leads to under-exploitation of information.

### Extensions and Results

The method is further extended to MoG-Graph (MoGG), where reference documents are pre-processed as graphs, enabling the retrieval of distantly situated snippets. Experiments demonstrate that MoG and MoGG effectively predict optimal granularity levels, significantly enhancing the performance of the RAG system in downstream tasks.

The research code and implementation are available on GitHub and through the ACL Anthology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85375956-975f-4c51-81e4-cb1aa5c17333",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "acfd65bf-f494-44b8-ac67-67fb254fe9c8",
  "toolUseResult": {
    "query": "Mix-of-Granularity MoG dynamic chunking granularity RAG routing COLING 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UieJMFnAj6T4D9jsdprgh5",
        "content": [
          {
            "title": "Optimize the Chunking Granularity for Retrieval- ...",
            "url": "https://aclanthology.org/2025.coling-main.384.pdf"
          },
          {
            "title": "Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation - ACL Anthology",
            "url": "https://aclanthology.org/2025.coling-main.384/"
          },
          {
            "title": "GitHub - ZGChung/Mix-of-Granularity: [COLING 2025] Mix-of-Granularity paper",
            "url": "https://github.com/ZGChung/Mix-of-Granularity"
          },
          {
            "title": "Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2406.00456v1"
          },
          {
            "title": "[2406.00456] Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2406.00456"
          },
          {
            "title": "Paper page - Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation",
            "url": "https://huggingface.co/papers/2406.00456"
          },
          {
            "title": "[PDF] UniversalRAG: Retrieval-Augmented Generation over Corpora of Diverse Modalities and Granularities | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/UniversalRAG:-Retrieval-Augmented-Generation-over-Yeo-Kim/94cf17cdb8df7016ebe7decb91257a2d0b14d1e8"
          },
          {
            "title": "Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation",
            "url": "https://powerdrill.ai/discover/discover-Mix-of-Granularity-Optimize-the-clx4ktn2104l6019n4h6q5sy2"
          },
          {
            "title": "Revisiting Chunking in the RAG Pipeline - by Florian",
            "url": "https://aiexpjourney.substack.com/p/revisiting-chunking-in-the-rag-pipeline"
          },
          {
            "title": "A Deep-Dive into Chunking Strategy, Chunking Methods, and Precision in RAG Applications - Superteams.ai",
            "url": "https://www.superteams.ai/blog/a-deep-dive-into-chunking-strategy-chunking-methods-and-precision-in-rag-applications"
          }
        ]
      },
      "I found relevant results for your query. Here's what I found:\n\n## Mix-of-Granularity (MoG) - COLING 2025\n\nThe paper \"Mix-of-Granularity: Optimize the Chunking Granularity for Retrieval-Augmented Generation\" was presented at the 31st International Conference on Computational Linguistics (COLING) held in Abu Dhabi, UAE in January 2025.\n\n### Key Concept\n\nMix-of-Granularity (MoG) is a method that dynamically determines the optimal granularity of a knowledge source based on input queries using a router, inspired by Mix-of-Expert. The router is efficiently trained with a newly proposed loss function employing soft labels.\n\n### Problem It Addresses\n\nIntegrating information from various reference databases is a major challenge for RAG systems because each knowledge source adopts a unique data structure and follows different conventions, and retrieving from multiple knowledge sources with one fixed strategy usually leads to under-exploitation of information.\n\n### Extensions and Results\n\nThe method is further extended to MoG-Graph (MoGG), where reference documents are pre-processed as graphs, enabling the retrieval of distantly situated snippets. Experiments demonstrate that MoG and MoGG effectively predict optimal granularity levels, significantly enhancing the performance of the RAG system in downstream tasks.\n\nThe research code and implementation are available on GitHub and through the ACL Anthology."
    ],
    "durationSeconds": 6.38043983800005
  },
  "sourceToolAssistantUUID": "85375956-975f-4c51-81e4-cb1aa5c17333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "acfd65bf-f494-44b8-ac67-67fb254fe9c8",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate GranRoute: Configuration Routing for Code Repair",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Tool result

_source line 34 · 2026-05-11T23:42:28.588Z_

<details><summary>↩ Tool result · `toolu_013eRL9w54xdMGcsgC8NyW7N`</summary>

```text
Web search results for query: "ProCC adaptive retrieval strategy code completion multi-armed bandit TOSEM 2025"

Links: [{"title":"Prompt-based Code Completion via Multi-Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2405.07530"},{"title":"MBA-RAG: a Bandit Approach for Adaptive Retrieval-Augmented Generation through Question Complexity - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.218/"},{"title":"Multi-Armed Bandits Meet Large Language Models","url":"https://arxiv.org/html/2505.13355v1"},{"title":"Adapting to Non-Stationary Environments: Multi-Armed Bandit Enhanced","url":"https://ojs.aaai.org/index.php/AAAI/article/view/33380/35535"},{"title":"Adapting to Non-Stationary Environments: Multi-Armed Bandit Enhanced Retrieval-Augmented Generation on Knowledge Graphs | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/33380"},{"title":"Week 6: Multi-Armed Bandits - Deep RL Course","url":"https://deeprlcourse.github.io/recitations/week6/"},{"title":"Multi-armed bandit - Wikipedia","url":"https://en.wikipedia.org/wiki/Multi-armed_bandit"},{"title":"Multi-Armed Bandit Environments","url":"https://www.emergentmind.com/topics/multi-armed-bandit-environments"},{"title":"Multi-armed Bandit Problem in Reinforcement Learning - GeeksforGeeks","url":"https://www.geeksforgeeks.org/machine-learning/multi-armed-bandit-problem-in-reinforcement-learning/"},{"title":"MBA-RAG: a Bandit Approach for Adaptive Retrieval- ...","url":"https://aclanthology.org/2025.coling-main.218.pdf"}]

Based on the search results, here's what I found regarding your query:

## ProCC - Prompt-based Code Completion

ProCC is a framework that uses a prompt-based multi-retriever system encoding lexical semantics, hypothetical line, and code summarization to derive multi-perspective representations. The adaptive retrieval selection algorithm makes decisions based on code semantics similarities and selects the optimal context from retrievals.

Evaluation results indicate that ProCC outperforms state-of-the-art code completion techniques by 8.6% on the open-source benchmark.

## Related Multi-Armed Bandit Approaches for RAG

The search results also show related work on multi-armed bandit approaches for adaptive retrieval-augmented generation:

Multi-armed bandit algorithms treat each retrieval method as a distinct "arm" and adapt the selection process by balancing exploration and exploitation. 

A Multi-objective Multi-Armed Bandit enhanced RAG framework treats each retrieval method as a distinct "arm" and uses real-time user feedback to adapt to dynamic environments, by selecting the appropriate retrieval method based on input queries and historical multi-objective performance.

**Note:** I found information about ProCC from arXiv (paper 2405.07530) and related bandit-based RAG approaches published at COLING 2025 and AAAI 2025. However, I did not find a specific TOSEM 2025 publication matching your exact query in these search results. You may want to check ACM's TOSEM journal directly for the most current publications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62ab5632-99c5-4407-a0af-e019a12b7f39",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "50f567dd-6eb0-4dd7-b588-c046446bfe64",
  "toolUseResult": {
    "query": "ProCC adaptive retrieval strategy code completion multi-armed bandit TOSEM 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_011Xt7ekmiq31WyYhzTNYbuN",
        "content": [
          {
            "title": "Prompt-based Code Completion via Multi-Retrieval Augmented Generation",
            "url": "https://arxiv.org/pdf/2405.07530"
          },
          {
            "title": "MBA-RAG: a Bandit Approach for Adaptive Retrieval-Augmented Generation through Question Complexity - ACL Anthology",
            "url": "https://aclanthology.org/2025.coling-main.218/"
          },
          {
            "title": "Multi-Armed Bandits Meet Large Language Models",
            "url": "https://arxiv.org/html/2505.13355v1"
          },
          {
            "title": "Adapting to Non-Stationary Environments: Multi-Armed Bandit Enhanced",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/33380/35535"
          },
          {
            "title": "Adapting to Non-Stationary Environments: Multi-Armed Bandit Enhanced Retrieval-Augmented Generation on Knowledge Graphs | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/33380"
          },
          {
            "title": "Week 6: Multi-Armed Bandits - Deep RL Course",
            "url": "https://deeprlcourse.github.io/recitations/week6/"
          },
          {
            "title": "Multi-armed bandit - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Multi-armed_bandit"
          },
          {
            "title": "Multi-Armed Bandit Environments",
            "url": "https://www.emergentmind.com/topics/multi-armed-bandit-environments"
          },
          {
            "title": "Multi-armed Bandit Problem in Reinforcement Learning - GeeksforGeeks",
            "url": "https://www.geeksforgeeks.org/machine-learning/multi-armed-bandit-problem-in-reinforcement-learning/"
          },
          {
            "title": "MBA-RAG: a Bandit Approach for Adaptive Retrieval- ...",
            "url": "https://aclanthology.org/2025.coling-main.218.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found regarding your query:\n\n## ProCC - Prompt-based Code Completion\n\nProCC is a framework that uses a prompt-based multi-retriever system encoding lexical semantics, hypothetical line, and code summarization to derive multi-perspective representations. The adaptive retrieval selection algorithm makes decisions based on code semantics similarities and selects the optimal context from retrievals.\n\nEvaluation results indicate that ProCC outperforms state-of-the-art code completion techniques by 8.6% on the open-source benchmark.\n\n## Related Multi-Armed Bandit Approaches for RAG\n\nThe search results also show related work on multi-armed bandit approaches for adaptive retrieval-augmented generation:\n\nMulti-armed bandit algorithms treat each retrieval method as a distinct \"arm\" and adapt the selection process by balancing exploration and exploitation. \n\nA Multi-objective Multi-Armed Bandit enhanced RAG framework treats each retrieval method as a distinct \"arm\" and uses real-time user feedback to adapt to dynamic environments, by selecting the appropriate retrieval method based on input queries and historical multi-objective performance.\n\n**Note:** I found information about ProCC from arXiv (paper 2405.07530) and related bandit-based RAG approaches published at COLING 2025 and AAAI 2025. However, I did not find a specific TOSEM 2025 publication matching your exact query in these search results. You may want to check ACM's TOSEM journal directly for the most current publications."
    ],
    "durationSeconds": 7.098478170000017
  },
  "sourceToolAssistantUUID": "62ab5632-99c5-4407-a0af-e019a12b7f39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-11T23:42:28.734Z_

<details><summary>↩ Tool result · `toolu_01Rir5GSYdqAn6JjeA9QqMhB`</summary>

```text
Web search results for query: "RAGRouter NeurIPS 2025 routing retrieval augmented LLM"

Links: [{"title":"NeurIPS Poster RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/119935"},{"title":"RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models | OpenReview","url":"https://openreview.net/forum?id=4VKVUmE1I8"},{"title":"RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2505.23052v2"},{"title":"[2505.23052] RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models","url":"https://arxiv.org/abs/2505.23052"},{"title":"Query Routing for Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2505.23052v1"},{"title":"RAGRouter: Retrieval-Augmented Routing","url":"https://www.emergentmind.com/topics/ragrouter"},{"title":"RAGRouter: Learning to Route Queries to Multiple ...","url":"https://openreview.net/pdf?id=4VKVUmE1I8"},{"title":"[2602.20735] RMIT-ADM+S at the MMU-RAG NeurIPS 2025 Competition","url":"https://arxiv.org/abs/2602.20735"},{"title":"GitHub - DavidZWZ/Awesome-RAG-Reasoning: [EMNLP 2025] Awesome RAG Reasoning Resources · GitHub","url":"https://github.com/DavidZWZ/Awesome-RAG-Reasoning"},{"title":"[PDF] RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RAGRouter:-Learning-to-Route-Queries-to-Multiple-Zhang-Liu/bbc2dcac1d4e52e607dc17104414b6b0cee5fb44"}]

Based on the search results, here's what I found about RAGRouter at NeurIPS 2025:

## RAGRouter Overview

RAGRouter is a RAG-aware routing design which leverages document embeddings and RAG capability embeddings with contrastive learning to capture knowledge representation shifts and enable informed routing decisions.

## The Problem It Addresses

RAGRouter addresses the need for intelligent routing mechanisms that select the most suitable model for each query from multiple retrieval-augmented LLMs via a dedicated router model. The key insight is that external documents dynamically affect LLMs' ability to answer queries, while existing routing methods, which rely on static parametric knowledge representations, exhibit suboptimal performance in RAG scenarios.

## Key Technical Contributions

RAGRouter incorporates a document encoder and a cross encoder to capture document semantics and query interactions, and assigns each LLM a RAG capability embedding—a learnable vector representing its proficiency in utilizing retrieved content.

## Performance Results

RAGRouter outperforms the best individual LLM by 3.61% on average and existing routing methods by 3.29%–9.33%. Additionally, with an extended score-threshold-based mechanism, it also achieves strong performance-efficiency trade-offs under low-latency constraints.

## Evaluation Scope

The method was validated on five knowledge-intensive tasks under local and online retrieval settings, using open-source LLMs such as the Qwen and LLaMA series scales from 0.5B to 72B and closed-source LLMs including GPT-4o, Qwen2.5-Max, and DeepSeek-R1.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6bbc9ae-580c-4cff-a044-04a00a7c5dcf",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "e8d3b69d-9924-4ad7-ba85-7614028cb7fd",
  "toolUseResult": {
    "query": "RAGRouter NeurIPS 2025 routing retrieval augmented LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XP21Bf7THizRz354Qp4aK2",
        "content": [
          {
            "title": "NeurIPS Poster RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models",
            "url": "https://neurips.cc/virtual/2025/loc/san-diego/poster/119935"
          },
          {
            "title": "RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=4VKVUmE1I8"
          },
          {
            "title": "RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models",
            "url": "https://arxiv.org/html/2505.23052v2"
          },
          {
            "title": "[2505.23052] RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models",
            "url": "https://arxiv.org/abs/2505.23052"
          },
          {
            "title": "Query Routing for Retrieval-Augmented Language Models",
            "url": "https://arxiv.org/html/2505.23052v1"
          },
          {
            "title": "RAGRouter: Retrieval-Augmented Routing",
            "url": "https://www.emergentmind.com/topics/ragrouter"
          },
          {
            "title": "RAGRouter: Learning to Route Queries to Multiple ...",
            "url": "https://openreview.net/pdf?id=4VKVUmE1I8"
          },
          {
            "title": "[2602.20735] RMIT-ADM+S at the MMU-RAG NeurIPS 2025 Competition",
            "url": "https://arxiv.org/abs/2602.20735"
          },
          {
            "title": "GitHub - DavidZWZ/Awesome-RAG-Reasoning: [EMNLP 2025] Awesome RAG Reasoning Resources · GitHub",
            "url": "https://github.com/DavidZWZ/Awesome-RAG-Reasoning"
          },
          {
            "title": "[PDF] RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/RAGRouter:-Learning-to-Route-Queries-to-Multiple-Zhang-Liu/bbc2dcac1d4e52e607dc17104414b6b0cee5fb44"
          }
        ]
      },
      "Based on the search results, here's what I found about RAGRouter at NeurIPS 2025:\n\n## RAGRouter Overview\n\nRAGRouter is a RAG-aware routing design which leverages document embeddings and RAG capability embeddings with contrastive learning to capture knowledge representation shifts and enable informed routing decisions.\n\n## The Problem It Addresses\n\nRAGRouter addresses the need for intelligent routing mechanisms that select the most suitable model for each query from multiple retrieval-augmented LLMs via a dedicated router model. The key insight is that external documents dynamically affect LLMs' ability to answer queries, while existing routing methods, which rely on static parametric knowledge representations, exhibit suboptimal performance in RAG scenarios.\n\n## Key Technical Contributions\n\nRAGRouter incorporates a document encoder and a cross encoder to capture document semantics and query interactions, and assigns each LLM a RAG capability embedding—a learnable vector representing its proficiency in utilizing retrieved content.\n\n## Performance Results\n\nRAGRouter outperforms the best individual LLM by 3.61% on average and existing routing methods by 3.29%–9.33%. Additionally, with an extended score-threshold-based mechanism, it also achieves strong performance-efficiency trade-offs under low-latency constraints.\n\n## Evaluation Scope\n\nThe method was validated on five knowledge-intensive tasks under local and online retrieval settings, using open-source LLMs such as the Qwen and LLaMA series scales from 0.5B to 72B and closed-source LLMs including GPT-4o, Qwen2.5-Max, and DeepSeek-R1."
    ],
    "durationSeconds": 6.7932016239999795
  },
  "sourceToolAssistantUUID": "e6bbc9ae-580c-4cff-a044-04a00a7c5dcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-11T23:42:28.736Z_

```json
{
  "parentUuid": "e8d3b69d-9924-4ad7-ba85-7614028cb7fd",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "868ed18f-1467-4eb7-a4c2-33c7b8e52864",
  "timestamp": "2026-05-11T23:42:28.736Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-11T23:42:46.525Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have confirmed the three most critical missing competitors:

1. **Mix-of-Granularity (MoG, COLING 2025)** — directly routes retrieval granularity for RAG using a trained router with soft labels. This is the closest methodological parallel to GranRoute's core idea.

2. **ProCC (arXiv 2405.07530)** — multi-retriever code completion with adaptive retrieval selection. Though it's for code completion (not repair), it's in the same domain and uses adaptive retrieval strategy selection.


3. **RAGRouter (NeurIPS 2025)** — routes queries to multiple RAG-augmented LLMs using document embeddings, which directly addresses the routing-over-RAG concept that's central to my work.

I should dive into the MoG paper first since it's the most directly comparable approach to what I'm proposing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "868ed18f-1467-4eb7-a4c2-33c7b8e52864",
  "isSidechain": false,
  "requestId": "req_011CawfgcZPixGU3wSYLrLWx",
  "type": "assistant",
  "uuid": "f6032c62-7585-4678-bc60-4b292ac78b11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQqCxZ4ipos1LWmGFJHozo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3243,
      "cache_read_input_tokens": 46803,
      "output_tokens": 455,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 455,
          "cache_read_input_tokens": 46803,
          "cache_creation_input_tokens": 3243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3243
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

_source line 38 · 2026-05-11T23:42:48.508Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017wVyh3cjaPKF5cFTrZDjdy`</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.00456",
  "prompt": "Extract the full abstract and the key technical details of the Mix-of-Granularity (MoG) method. Specifically: (1) What is the router architecture? (2) How is the router trained (what loss function/training paradigm)? (3) What is the granularity space (what options does the router choose from)? (4) What are the main experimental results? (5) Does it apply to code tasks at all?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6032c62-7585-4678-bc60-4b292ac78b11",
  "isSidechain": false,
  "requestId": "req_011CawfgcZPixGU3wSYLrLWx",
  "type": "assistant",
  "uuid": "d5828122-cdb1-4348-bfd6-d1677982dbdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQqCxZ4ipos1LWmGFJHozo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3243,
      "cache_read_input_tokens": 46803,
      "output_tokens": 455,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 455,
          "cache_read_input_tokens": 46803,
          "cache_creation_input_tokens": 3243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3243
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

_source line 39 · 2026-05-11T23:42:49.303Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MbKnQ8QKpzCMjEPuhHERzL`</summary>

```json
{
  "query": "\"adaptive context\" OR \"adaptive retrieval\" \"code repair\" \"SWE-bench\" routing configuration selection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5828122-cdb1-4348-bfd6-d1677982dbdd",
  "isSidechain": false,
  "requestId": "req_011CawfgcZPixGU3wSYLrLWx",
  "type": "assistant",
  "uuid": "acad0a75-98d2-4cc7-a14a-345d16e0b410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQqCxZ4ipos1LWmGFJHozo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3243,
      "cache_read_input_tokens": 46803,
      "output_tokens": 455,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3243,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 455,
          "cache_read_input_tokens": 46803,
          "cache_creation_input_tokens": 3243,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3243
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

_source line 40 · 2026-05-11T23:42:53.075Z_

<details><summary>↩ Tool result · `toolu_017wVyh3cjaPKF5cFTrZDjdy`</summary>

```text
# Mix-of-Granularity (MoG) Method Analysis

Based on the arXiv abstract provided, here's what can be extracted:

## (1) Router Architecture
The abstract does not specify the router architecture details. It only mentions that MoG uses "a router" to dynamically determine optimal granularity, without describing its specific design.

## (2) Training Approach
The method employs "a newly proposed loss function employing soft labels." However, the specific loss function formulation and detailed training procedures are not described in the abstract provided.

## (3) Granularity Space
The abstract does not enumerate the specific granularity options the router selects from. It references dynamically determining "optimal granularity levels" but doesn't list concrete choices.

## (4) Experimental Results
The abstract states results "significantly enhance the performance of the RAG system in downstream tasks," but provides no numerical metrics or specific benchmark details in this summary.

## (5) Application to Code Tasks
The abstract contains no mention of code-related applications. The focus appears limited to general "knowledge source" retrieval across "reference databases."

**Note:** The full paper (19 pages, 6 figures, 11 tables) would contain comprehensive technical details absent from this abstract page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5828122-cdb1-4348-bfd6-d1677982dbdd",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "c17a873d-1666-45ef-989e-bf0c802c3891",
  "toolUseResult": {
    "bytes": 47250,
    "code": 200,
    "codeText": "OK",
    "result": "# Mix-of-Granularity (MoG) Method Analysis\n\nBased on the arXiv abstract provided, here's what can be extracted:\n\n## (1) Router Architecture\nThe abstract does not specify the router architecture details. It only mentions that MoG uses \"a router\" to dynamically determine optimal granularity, without describing its specific design.\n\n## (2) Training Approach\nThe method employs \"a newly proposed loss function employing soft labels.\" However, the specific loss function formulation and detailed training procedures are not described in the abstract provided.\n\n## (3) Granularity Space\nThe abstract does not enumerate the specific granularity options the router selects from. It references dynamically determining \"optimal granularity levels\" but doesn't list concrete choices.\n\n## (4) Experimental Results\nThe abstract states results \"significantly enhance the performance of the RAG system in downstream tasks,\" but provides no numerical metrics or specific benchmark details in this summary.\n\n## (5) Application to Code Tasks\nThe abstract contains no mention of code-related applications. The focus appears limited to general \"knowledge source\" retrieval across \"reference databases.\"\n\n**Note:** The full paper (19 pages, 6 figures, 11 tables) would contain comprehensive technical details absent from this abstract page.",
    "durationMs": 4561,
    "url": "https://arxiv.org/abs/2406.00456"
  },
  "sourceToolAssistantUUID": "d5828122-cdb1-4348-bfd6-d1677982dbdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-11T23:43:00.017Z_

<details><summary>↩ Tool result · `toolu_01MbKnQ8QKpzCMjEPuhHERzL`</summary>

```text
Web search results for query: ""adaptive context" OR "adaptive retrieval" "code repair" "SWE-bench" routing configuration selection 2025 2026"

Links: [{"title":"SWE Context Bench: A Benchmark for Context Learning in Coding","url":"https://arxiv.org/html/2602.08316v3"},{"title":"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents","url":"https://www.arxiv.org/pdf/2601.16746"},{"title":"SWE-Adept: An LLM-Based Agentic Framework for Deep Codebase Analysis and Structured Issue Resolution","url":"https://arxiv.org/html/2603.01327v1"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and","url":"https://arxiv.org/pdf/2506.17208"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v1"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"},{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"},{"title":"SWE Context Bench: A Benchmark for Context Learning in Coding Jared Zhu","url":"https://www.arxiv.org/pdf/2602.08316"},{"title":"Auggie tops SWE-Bench Pro | Augment Code","url":"https://www.augmentcode.com/blog/auggie-tops-swe-bench-pro"},{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"}]

Based on the search results, I found several highly relevant papers and research on adaptive context and retrieval approaches for code repair and SWE-bench from 2025-2026:

## Key Findings:

### 1. **SWE-Pruner: Self-Adaptive Context Pruning**
For multi-turn agent tasks like SWE-Bench, agents dynamically generate Goal Hints at each round based on their evolving reasoning trace, enabling them to shift focus from high-level navigation to detailed debugging as needed. SWE-Pruner delivers substantial efficiency gains with a 39% reduction in tokens on SWE-Bench Verified with Claude Sonnet 4.5, while also improving agent decision quality and reducing interaction rounds by up to 26%.

### 2. **SWE Context Bench: Context Learning Benchmark**
The benchmark compares four widely-used memory retrieval frameworks: Mem0 (2025), OpenViking (2026), LangMem (2026), and Supermemory (2026). Supermemory performs best overall, achieving a FAIL_TO_PASS test rate of 55.95% and the highest resolution rate of 30.30%, while maintaining strong PASS_TO_PASS scores (90.23% at test level, 88.89% at task level).

### 3. **SWE-Adept: Context Management Framework**
Achieving thorough search while maintaining effective context management is challenging yet critical, since excessive irrelevant retrieval can degrade localization accuracy. SWE-Adept interfaces with a shared working memory that stores code-state checkpoints indexed by execution steps, facilitating precise checkpoint retrieval and enabling reliable agent-driven version-control operations.

### 4. **Semantic Retrieval for Code Repair**
Augment's Context Engine builds a semantic index of the full codebase. The Context Engine found relevant code because it understands semantic relationships, not just matching keywords.

### 5. **Advanced Retrieval Techniques in RACG**
SWE-Fixer employs a coarse-to-fine retriever that combines BM25 with a fine-tuned 7B model to enhance retrieval precision. SweRank utilizes dual-encoder embedding models as code retrievers and instruction-tuned LLMs as code re-rankers.

These research works demonstrate significant progress in adaptive context selection and retrieval strategies specifically tailored for the SWE-bench code repair tasks in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "acad0a75-98d2-4cc7-a14a-345d16e0b410",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "a4de47b0-76e6-44c8-b529-e17e535aa75b",
  "toolUseResult": {
    "query": "\"adaptive context\" OR \"adaptive retrieval\" \"code repair\" \"SWE-bench\" routing configuration selection 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JuhGqAuLHrmAuzzZLHoiK9",
        "content": [
          {
            "title": "SWE Context Bench: A Benchmark for Context Learning in Coding",
            "url": "https://arxiv.org/html/2602.08316v3"
          },
          {
            "title": "SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents",
            "url": "https://www.arxiv.org/pdf/2601.16746"
          },
          {
            "title": "SWE-Adept: An LLM-Based Agentic Framework for Deep Codebase Analysis and Structured Issue Resolution",
            "url": "https://arxiv.org/html/2603.01327v1"
          },
          {
            "title": "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and",
            "url": "https://arxiv.org/pdf/2506.17208"
          },
          {
            "title": "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems",
            "url": "https://arxiv.org/html/2506.17208v1"
          },
          {
            "title": "GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥",
            "url": "https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"
          },
          {
            "title": "What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair",
            "url": "https://arxiv.org/pdf/2602.04449"
          },
          {
            "title": "SWE Context Bench: A Benchmark for Context Learning in Coding Jared Zhu",
            "url": "https://www.arxiv.org/pdf/2602.08316"
          },
          {
            "title": "Auggie tops SWE-Bench Pro | Augment Code",
            "url": "https://www.augmentcode.com/blog/auggie-tops-swe-bench-pro"
          },
          {
            "title": "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/html/2510.04905v1"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers and research on adaptive context and retrieval approaches for code repair and SWE-bench from 2025-2026:\n\n## Key Findings:\n\n### 1. **SWE-Pruner: Self-Adaptive Context Pruning**\nFor multi-turn agent tasks like SWE-Bench, agents dynamically generate Goal Hints at each round based on their evolving reasoning trace, enabling them to shift focus from high-level navigation to detailed debugging as needed. SWE-Pruner delivers substantial efficiency gains with a 39% reduction in tokens on SWE-Bench Verified with Claude Sonnet 4.5, while also improving agent decision quality and reducing interaction rounds by up to 26%.\n\n### 2. **SWE Context Bench: Context Learning Benchmark**\nThe benchmark compares four widely-used memory retrieval frameworks: Mem0 (2025), OpenViking (2026), LangMem (2026), and Supermemory (2026). Supermemory performs best overall, achieving a FAIL_TO_PASS test rate of 55.95% and the highest resolution rate of 30.30%, while maintaining strong PASS_TO_PASS scores (90.23% at test level, 88.89% at task level).\n\n### 3. **SWE-Adept: Context Management Framework**\nAchieving thorough search while maintaining effective context management is challenging yet critical, since excessive irrelevant retrieval can degrade localization accuracy. SWE-Adept interfaces with a shared working memory that stores code-state checkpoints indexed by execution steps, facilitating precise checkpoint retrieval and enabling reliable agent-driven version-control operations.\n\n### 4. **Semantic Retrieval for Code Repair**\nAugment's Context Engine builds a semantic index of the full codebase. The Context Engine found relevant code because it understands semantic relationships, not just matching keywords.\n\n### 5. **Advanced Retrieval Techniques in RACG**\nSWE-Fixer employs a coarse-to-fine retriever that combines BM25 with a fine-tuned 7B model to enhance retrieval precision. SweRank utilizes dual-encoder embedding models as code retrievers and instruction-tuned LLMs as code re-rankers.\n\nThese research works demonstrate significant progress in adaptive context selection and retrieval strategies specifically tailored for the SWE-bench code repair tasks in 2025-2026."
    ],
    "durationSeconds": 10.710157179000031
  },
  "sourceToolAssistantUUID": "acad0a75-98d2-4cc7-a14a-345d16e0b410",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a4de47b0-76e6-44c8-b529-e17e535aa75b",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate GranRoute: Configuration Routing for Code Repair",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Assistant

_source line 44 · 2026-05-11T23:43:03.296Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the MoG paper's full content to understand the method better, since it's the most critical competitor.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4de47b0-76e6-44c8-b529-e17e535aa75b",
  "isSidechain": false,
  "requestId": "req_011CawfivLnENW7QmXPEJA9v",
  "type": "assistant",
  "uuid": "8429dc22-abf4-4b07-89ae-a104e3582f6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LG9kG7wgiaCWi3nnDGwGXP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1905,
      "cache_read_input_tokens": 50046,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1905,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 50046,
          "cache_creation_input_tokens": 1905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1905
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

_source line 45 · 2026-05-11T23:43:05.723Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0151Uc4m2MpQMAUDDXeECtHW`</summary>

```json
{
  "url": "https://aclanthology.org/2025.coling-main.384/",
  "prompt": "Extract the full abstract and any technical details visible on this page about Mix-of-Granularity (MoG). What granularity levels does the router choose between? What is the router architecture? What benchmarks are used? What domain is it applied to?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8429dc22-abf4-4b07-89ae-a104e3582f6d",
  "isSidechain": false,
  "requestId": "req_011CawfivLnENW7QmXPEJA9v",
  "type": "assistant",
  "uuid": "241f6638-3197-4245-ae16-91944239ffbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LG9kG7wgiaCWi3nnDGwGXP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1905,
      "cache_read_input_tokens": 50046,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1905,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 50046,
          "cache_creation_input_tokens": 1905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1905
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

_source line 46 · 2026-05-11T23:43:06.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SFpbbfxbE44fBU6ic4wWZ6`</summary>

```json
{
  "query": "site:arxiv.org \"retrieval configuration\" OR \"retrieval strategy selection\" \"code\" \"learning\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "241f6638-3197-4245-ae16-91944239ffbb",
  "isSidechain": false,
  "requestId": "req_011CawfivLnENW7QmXPEJA9v",
  "type": "assistant",
  "uuid": "7f609ac9-f563-4703-988c-afd7ca5a1061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LG9kG7wgiaCWi3nnDGwGXP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1905,
      "cache_read_input_tokens": 50046,
      "output_tokens": 245,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1905,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 245,
          "cache_read_input_tokens": 50046,
          "cache_creation_input_tokens": 1905,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1905
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

_source line 47 · 2026-05-11T23:43:10.233Z_

<details><summary>↩ Tool result · `toolu_0151Uc4m2MpQMAUDDXeECtHW`</summary>

```text
# Mix-of-Granularity: Technical Summary

## Abstract
The paper addresses the challenge of integrating multiple reference databases in RAG systems. The authors propose "a method that dynamically determines the optimal granularity of a knowledge source based on input queries using a router."

## Technical Architecture
The page provides limited architectural details. It confirms the router uses "a newly proposed loss function employing soft labels" for training, but does not specify the router's internal structure or which granularity levels it selects between.

## Extensions
The authors extend their approach to MoG-Graph (MoGG), where "reference documents are pre-processed as graphs, enabling the retrieval of distantly situated snippets."

## Evaluation & Application Domains
**Not specified on this page.** The abstract only notes that "experiments demonstrate that MoG and MoGG effectively predict optimal granularity levels, significantly enhancing the performance of the RAG system in downstream tasks," without identifying specific benchmarks or application domains.

## Publication Details
- Conference: COLING 2025 (31st International Conference on Computational Linguistics)
- Pages: 5756–5774
- Location: Abu Dhabi, UAE

The full technical details regarding granularity levels, router architecture, specific benchmarks, and domains would require consulting the complete PDF paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "241f6638-3197-4245-ae16-91944239ffbb",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "ae2354af-a633-47b3-b329-a66f29c1a303",
  "toolUseResult": {
    "bytes": 39605,
    "code": 200,
    "codeText": "OK",
    "result": "# Mix-of-Granularity: Technical Summary\n\n## Abstract\nThe paper addresses the challenge of integrating multiple reference databases in RAG systems. The authors propose \"a method that dynamically determines the optimal granularity of a knowledge source based on input queries using a router.\"\n\n## Technical Architecture\nThe page provides limited architectural details. It confirms the router uses \"a newly proposed loss function employing soft labels\" for training, but does not specify the router's internal structure or which granularity levels it selects between.\n\n## Extensions\nThe authors extend their approach to MoG-Graph (MoGG), where \"reference documents are pre-processed as graphs, enabling the retrieval of distantly situated snippets.\"\n\n## Evaluation & Application Domains\n**Not specified on this page.** The abstract only notes that \"experiments demonstrate that MoG and MoGG effectively predict optimal granularity levels, significantly enhancing the performance of the RAG system in downstream tasks,\" without identifying specific benchmarks or application domains.\n\n## Publication Details\n- Conference: COLING 2025 (31st International Conference on Computational Linguistics)\n- Pages: 5756–5774\n- Location: Abu Dhabi, UAE\n\nThe full technical details regarding granularity levels, router architecture, specific benchmarks, and domains would require consulting the complete PDF paper.",
    "durationMs": 4506,
    "url": "https://aclanthology.org/2025.coling-main.384/"
  },
  "sourceToolAssistantUUID": "241f6638-3197-4245-ae16-91944239ffbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-11T23:43:16.705Z_

<details><summary>↩ Tool result · `toolu_01SFpbbfxbE44fBU6ic4wWZ6`</summary>

```text
Web search results for query: "site:arxiv.org "retrieval configuration" OR "retrieval strategy selection" "code" "learning" 2026"

No links found.

I apologize, but the web search with the special operators (site: and OR) didn't return results. This is because I'm not able to use special search operators like `site:` and `OR` in my search queries. 

Let me try a revised search focused on the key concepts without the special operators:

Links: [{"title":"Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/html/2510.04905v1"},{"title":"RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH","url":"https://arxiv.org/pdf/2510.04905"},{"title":"From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning","url":"https://arxiv.org/html/2604.19516v1"},{"title":"1 Retrieval-Augmented Generation for Large Language Models: A Survey","url":"https://arxiv.org/pdf/2312.10997"},{"title":"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction","url":"https://arxiv.org/html/2605.06676"},{"title":"Reasoning in Trees: Improving Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2601.11255"},{"title":"CHORUS: Zero-shot Hierarchical Retrieval and Orchestration for Generating Linear Programming CodeThis paper has been accepted for presentation at the 19th Learning and Intelligent Optimization Conference (LION 19).","url":"https://arxiv.org/html/2505.01485v1"},{"title":"[2601.00509] Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback","url":"https://arxiv.org/abs/2601.00509"},{"title":"[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches","url":"https://arxiv.org/abs/2510.04905"},{"title":"A Survey on Retrieval And Structuring Augmented Generation","url":"https://arxiv.org/pdf/2509.10697"}]

I found several relevant papers from arxiv related to retrieval configuration, strategy selection, code, and learning. Here are the key findings:

## Survey on Retrieval-Augmented Code Generation

A retriever is a module that selects relevant context from the repository based on the input query or partial code, with various retrieval strategies available including identifier matching, which is the most basic and widely used approach. Recent research in retrieval-augmented code generation increasingly treats training as a vital component for improving performance, reflecting growing recognition that aligning retrieval modules with downstream generation tasks and adapting pre-trained language models to code-specific domains is important.

## Key Retrieval Strategies for Code

The common approaches for retrieval include identifier matching for exact name or signature matching, sparse retrieval using lexical or sparse-vector matching like TF-IDF and BM25, dense retrieval employing neural embeddings like CodeBERT and UniXcoder with nearest-neighbor search, graph-based retrieval utilizing abstract syntax trees and call graphs, and hybrid retrieval combining lexical, embedding, and structural signals.

## Related 2026 Papers

Several papers from 2026 address related topics:

- A retrieval-augmented multi-tool repair workflow uses a single code-generating LLM that iteratively refines its outputs, with a lightweight embedding model used for semantic retrieval of previously successful repairs to provide security-focused examples.

- For multi-hop question answering, hierarchical approaches involve explicit generation and selection of a reasoning tree where each node represents precisely defined subproblems with clear logical dependencies.

These papers demonstrate active research into retrieval configuration strategies for code generation and learning systems in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f609ac9-f563-4703-988c-afd7ca5a1061",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "ca75d009-3ed3-476e-879b-08db252cfd10",
  "toolUseResult": {
    "query": "site:arxiv.org \"retrieval configuration\" OR \"retrieval strategy selection\" \"code\" \"learning\" 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FGpBrMbyc2mj1JDuLezsmv",
        "content": []
      },
      "I apologize, but the web search with the special operators (site: and OR) didn't return results. This is because I'm not able to use special search operators like `site:` and `OR` in my search queries. \n\nLet me try a revised search focused on the key concepts without the special operators:",
      {
        "tool_use_id": "srvtoolu_01NH5eCqyDGqANr6B7X26c6y",
        "content": [
          {
            "title": "Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/html/2510.04905v1"
          },
          {
            "title": "RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY WITH",
            "url": "https://arxiv.org/pdf/2510.04905"
          },
          {
            "title": "From Experience to Skill: Multi-Agent Generative Engine Optimization via Reusable Strategy Learning",
            "url": "https://arxiv.org/html/2604.19516v1"
          },
          {
            "title": "1 Retrieval-Augmented Generation for Large Language Models: A Survey",
            "url": "https://arxiv.org/pdf/2312.10997"
          },
          {
            "title": "LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction",
            "url": "https://arxiv.org/html/2605.06676"
          },
          {
            "title": "Reasoning in Trees: Improving Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2601.11255"
          },
          {
            "title": "CHORUS: Zero-shot Hierarchical Retrieval and Orchestration for Generating Linear Programming CodeThis paper has been accepted for presentation at the 19th Learning and Intelligent Optimization Conference (LION 19).",
            "url": "https://arxiv.org/html/2505.01485v1"
          },
          {
            "title": "[2601.00509] Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback",
            "url": "https://arxiv.org/abs/2601.00509"
          },
          {
            "title": "[2510.04905] Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches",
            "url": "https://arxiv.org/abs/2510.04905"
          },
          {
            "title": "A Survey on Retrieval And Structuring Augmented Generation",
            "url": "https://arxiv.org/pdf/2509.10697"
          }
        ]
      },
      "I found several relevant papers from arxiv related to retrieval configuration, strategy selection, code, and learning. Here are the key findings:\n\n## Survey on Retrieval-Augmented Code Generation\n\nA retriever is a module that selects relevant context from the repository based on the input query or partial code, with various retrieval strategies available including identifier matching, which is the most basic and widely used approach. Recent research in retrieval-augmented code generation increasingly treats training as a vital component for improving performance, reflecting growing recognition that aligning retrieval modules with downstream generation tasks and adapting pre-trained language models to code-specific domains is important.\n\n## Key Retrieval Strategies for Code\n\nThe common approaches for retrieval include identifier matching for exact name or signature matching, sparse retrieval using lexical or sparse-vector matching like TF-IDF and BM25, dense retrieval employing neural embeddings like CodeBERT and UniXcoder with nearest-neighbor search, graph-based retrieval utilizing abstract syntax trees and call graphs, and hybrid retrieval combining lexical, embedding, and structural signals.\n\n## Related 2026 Papers\n\nSeveral papers from 2026 address related topics:\n\n- A retrieval-augmented multi-tool repair workflow uses a single code-generating LLM that iteratively refines its outputs, with a lightweight embedding model used for semantic retrieval of previously successful repairs to provide security-focused examples.\n\n- For multi-hop question answering, hierarchical approaches involve explicit generation and selection of a reasoning tree where each node represents precisely defined subproblems with clear logical dependencies.\n\nThese papers demonstrate active research into retrieval configuration strategies for code generation and learning systems in 2026."
    ],
    "durationSeconds": 10.289245617999986
  },
  "sourceToolAssistantUUID": "7f609ac9-f563-4703-988c-afd7ca5a1061",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-11T23:43:21.456Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now do a final check on the "kNN baseline beats complex routers" finding mentioned by the novelty agent, and check the headroom question more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca75d009-3ed3-476e-879b-08db252cfd10",
  "isSidechain": false,
  "requestId": "req_011Cawfk9gEkVYs1TqSYjFyY",
  "type": "assistant",
  "uuid": "a953c653-b6ac-496d-81fe-dcedfc02dd49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oykm8frctJBPHm2NjRHEY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1555,
      "cache_read_input_tokens": 51951,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 51951,
          "cache_creation_input_tokens": 1555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1555
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

_source line 50 · 2026-05-11T23:43:22.633Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FuxgR5pofTCXDFpUmi64Ep`</summary>

```json
{
  "query": "\"rethinking predictive LLM routing\" kNN baseline simple router 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a953c653-b6ac-496d-81fe-dcedfc02dd49",
  "isSidechain": false,
  "requestId": "req_011Cawfk9gEkVYs1TqSYjFyY",
  "type": "assistant",
  "uuid": "9082875a-1147-4570-810a-46f30298c942",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oykm8frctJBPHm2NjRHEY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1555,
      "cache_read_input_tokens": 51951,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 51951,
          "cache_creation_input_tokens": 1555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1555
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

_source line 51 · 2026-05-11T23:43:23.521Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VtzmLTvpgR8MtyWHGakKYd`</summary>

```json
{
  "query": "oracle configuration selection code repair headroom gap fixed vs adaptive SWE-bench 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9082875a-1147-4570-810a-46f30298c942",
  "isSidechain": false,
  "requestId": "req_011Cawfk9gEkVYs1TqSYjFyY",
  "type": "assistant",
  "uuid": "2734a900-623e-4b72-8bb4-777b6e84b76d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011oykm8frctJBPHm2NjRHEY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1555,
      "cache_read_input_tokens": 51951,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 51951,
          "cache_creation_input_tokens": 1555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1555
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

_source line 52 · 2026-05-11T23:43:30.222Z_

<details><summary>↩ Tool result · `toolu_01FuxgR5pofTCXDFpUmi64Ep`</summary>

```text
Web search results for query: ""rethinking predictive LLM routing" kNN baseline simple router 2025 2026"

Links: [{"title":"Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers","url":"https://arxiv.org/html/2505.12601v1"},{"title":"Rethinking Predictive LLM Routing: When Simple KNN Beats Complex Learned Routers | OpenReview","url":"https://openreview.net/forum?id=Chn50flK4X"},{"title":"[2505.12601] Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers","url":"https://arxiv.org/abs/2505.12601"},{"title":"Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250512601L/abstract"},{"title":"When Simple kNN Beats Complex Learned Routers","url":"https://arxiv.org/pdf/2505.12601"},{"title":"Paper page - Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers","url":"https://huggingface.co/papers/2505.12601"},{"title":"LLM Router: Rethinking Routing with Prefill Activations","url":"https://arxiv.org/html/2603.20895"},{"title":"RETHINKING PREDICTIVE LLM ROUTING","url":"https://openreview.net/pdf/09a1cf8eea342f695327cb4308918d85676c6637.pdf"},{"title":"[Literature Review] Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers","url":"https://www.themoonlight.io/en/review/rethinking-predictive-modeling-for-llm-routing-when-simple-knn-beats-complex-learned-routers"},{"title":"MARS: A BENCHMARK FOR MULTI-LLM ALGO","url":"https://openreview.net/pdf?id=C0rs3wM0N8"}]

I found excellent results for your query! Here's what I found:

## Key Findings

A well-tuned k-Nearest Neighbors (kNN) approach not only matches but often outperforms state-of-the-art learned routers across diverse tasks, according to a recent research paper titled "Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers."

### Main Research Contributions

The paper, published in May 2025, makes several important points:

1. **Challenge to Complexity**: The results challenge the prevailing notion that sophisticated learning-based routers are necessary for high-quality LLM routing, finding that simple, robust methods grounded in existing evaluation signals often perform best.

2. **Theoretical Basis**: The effectiveness stems from the strong locality properties in embedding spaces, where semantically similar queries tend to benefit from similar models, allowing kNN approaches to achieve strong performance with lower sample complexity than parametric methods.

3. **Benchmarking**: The work introduces a suite of standardized routing benchmarks spanning instruction-following, question-answering, and reasoning tasks, as well as the first multi-modal routing dataset involving visual inputs.

4. **kNN Router Mechanism**: The kNN router retrieves the k most similar examples from a training set and aggregates their performance outcomes—for utility prediction, it averages the observed scores and costs from neighbors; for model selection, it uses majority voting among the top-performing models for similar queries.

The research fundamentally demonstrates that simple, non-parametric methods deserve serious consideration in practical multi-model LLM systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9082875a-1147-4570-810a-46f30298c942",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "bd8f772e-a3ce-47a9-9c89-e87aac333eb1",
  "toolUseResult": {
    "query": "\"rethinking predictive LLM routing\" kNN baseline simple router 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V13MoDbnmDWs2uMhFWwk1k",
        "content": [
          {
            "title": "Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers",
            "url": "https://arxiv.org/html/2505.12601v1"
          },
          {
            "title": "Rethinking Predictive LLM Routing: When Simple KNN Beats Complex Learned Routers | OpenReview",
            "url": "https://openreview.net/forum?id=Chn50flK4X"
          },
          {
            "title": "[2505.12601] Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers",
            "url": "https://arxiv.org/abs/2505.12601"
          },
          {
            "title": "Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250512601L/abstract"
          },
          {
            "title": "When Simple kNN Beats Complex Learned Routers",
            "url": "https://arxiv.org/pdf/2505.12601"
          },
          {
            "title": "Paper page - Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers",
            "url": "https://huggingface.co/papers/2505.12601"
          },
          {
            "title": "LLM Router: Rethinking Routing with Prefill Activations",
            "url": "https://arxiv.org/html/2603.20895"
          },
          {
            "title": "RETHINKING PREDICTIVE LLM ROUTING",
            "url": "https://openreview.net/pdf/09a1cf8eea342f695327cb4308918d85676c6637.pdf"
          },
          {
            "title": "[Literature Review] Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers",
            "url": "https://www.themoonlight.io/en/review/rethinking-predictive-modeling-for-llm-routing-when-simple-knn-beats-complex-learned-routers"
          },
          {
            "title": "MARS: A BENCHMARK FOR MULTI-LLM ALGO",
            "url": "https://openreview.net/pdf?id=C0rs3wM0N8"
          }
        ]
      },
      "I found excellent results for your query! Here's what I found:\n\n## Key Findings\n\nA well-tuned k-Nearest Neighbors (kNN) approach not only matches but often outperforms state-of-the-art learned routers across diverse tasks, according to a recent research paper titled \"Rethinking Predictive Modeling for LLM Routing: When Simple kNN Beats Complex Learned Routers.\"\n\n### Main Research Contributions\n\nThe paper, published in May 2025, makes several important points:\n\n1. **Challenge to Complexity**: The results challenge the prevailing notion that sophisticated learning-based routers are necessary for high-quality LLM routing, finding that simple, robust methods grounded in existing evaluation signals often perform best.\n\n2. **Theoretical Basis**: The effectiveness stems from the strong locality properties in embedding spaces, where semantically similar queries tend to benefit from similar models, allowing kNN approaches to achieve strong performance with lower sample complexity than parametric methods.\n\n3. **Benchmarking**: The work introduces a suite of standardized routing benchmarks spanning instruction-following, question-answering, and reasoning tasks, as well as the first multi-modal routing dataset involving visual inputs.\n\n4. **kNN Router Mechanism**: The kNN router retrieves the k most similar examples from a training set and aggregates their performance outcomes—for utility prediction, it averages the observed scores and costs from neighbors; for model selection, it uses majority voting among the top-performing models for similar queries.\n\nThe research fundamentally demonstrates that simple, non-parametric methods deserve serious consideration in practical multi-model LLM systems."
    ],
    "durationSeconds": 7.5852658090000045
  },
  "sourceToolAssistantUUID": "9082875a-1147-4570-810a-46f30298c942",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-11T23:43:35.272Z_

<details><summary>↩ Tool result · `toolu_01VtzmLTvpgR8MtyWHGakKYd`</summary>

```text
Web search results for query: "oracle configuration selection code repair headroom gap fixed vs adaptive SWE-bench 2025 2026"

Links: [{"title":"SWE-bench Verified Benchmark","url":"https://www.emergentmind.com/topics/swe-bench-verified"},{"title":"Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study","url":"https://arxiv.org/pdf/2503.15223"},{"title":"princeton-nlp/SWE-bench_Lite_oracle · Datasets at Hugging Face","url":"https://huggingface.co/datasets/princeton-nlp/SWE-bench_Lite_oracle"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and","url":"https://arxiv.org/pdf/2506.17208"},{"title":"SWE-Bench: Real-World Software Benchmark","url":"https://www.emergentmind.com/topics/swe-bench"},{"title":"Introduction to SWE Bench & Patch Centric Approach | by Zain ul Abideen | Medium","url":"https://medium.com/@zaiinn440/introduction-to-swe-bench-patch-centric-approach-1b02f0517304"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"princeton-nlp/SWE-bench_oracle · Datasets at Hugging Face","url":"https://huggingface.co/datasets/princeton-nlp/SWE-bench_oracle"},{"title":"SWE-Bench Lite: Bug-Fixing Benchmark","url":"https://www.emergentmind.com/topics/swe-bench-lite-dataset"},{"title":"princeton-nlp/SWE-bench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/princeton-nlp/SWE-bench"}]

The search results provide information about SWE-bench, oracle retrieval settings, and various code repair approaches, but they don't contain specific research on the exact terms you're looking for regarding "headroom gap fixed vs adaptive" oracle configuration selection. Let me search for more specific information.

Links: [{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and","url":"https://arxiv.org/pdf/2506.17208"},{"title":"SWE-Bench Leaderboards","url":"https://www.emergentmind.com/topics/swe-bench-leaderboards"},{"title":"SWE-bench Verified Benchmark","url":"https://www.emergentmind.com/topics/swe-bench-verified"},{"title":"Rigorous Evaluation of Coding Agents on SWE-Bench","url":"https://aclanthology.org/2025.acl-long.189.pdf"},{"title":"SWE-bench","url":"https://www.swebench.com/original.html"},{"title":"Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study","url":"https://arxiv.org/html/2503.15223v1"},{"title":"SWE-Bench: Real-World Software Benchmark","url":"https://www.emergentmind.com/topics/swe-bench"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"},{"title":"2026-1-27 SWE-EVO: Benchmarking Coding Agents in","url":"https://arxiv.org/pdf/2512.18470"}]

The search results still don't contain the specific terminology you mentioned ("headroom gap fixed vs adaptive" oracle configuration selection). Let me try a more targeted search.

No links found.

Unfortunately, the search for the exact phrase "headroom gap fixed vs adaptive" did not return results. Based on my comprehensive searches, I found extensive information about SWE-bench oracle configurations and code repair evaluation, but I was unable to locate specific research or documentation using the exact terminology "oracle configuration selection code repair headroom gap fixed vs adaptive SWE-bench 2025 2026."

The search results do show:

1. SWE-bench includes an "Oracle" retrieval setting where each instance uses the oracle-retrieved file format, which is a known retrieval configuration.

2. The highest-performing agents use single- or multi-agent frameworks with a degree of autonomous control flow, allowing for adaptive reasoning and context-sensitive repair strategies.

3. Recent submissions employ sophisticated patch selection strategies, such as TRAE using o1 to select among patches generated by multiple models, and AgentScope using Qwen2.5 to select the best result among multiple trials.

However, I was unable to find specific research papers or documentation specifically discussing "headroom gap fixed vs adaptive" oracle configuration selection. This particular terminology may be from a very recent paper (early 2026), a preprint not yet widely indexed, or it may be using non-standard terminology. If you have a specific paper title or ArXiv link, I'd be happy to search for that.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2734a900-623e-4b72-8bb4-777b6e84b76d",
  "isSidechain": false,
  "promptId": "e71a9702-1527-4fd9-9872-1a99d659c992",
  "type": "user",
  "uuid": "a5c1b554-252c-440c-94cb-d423c11a1fea",
  "toolUseResult": {
    "query": "oracle configuration selection code repair headroom gap fixed vs adaptive SWE-bench 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013p3ggQdy5etUg9NkmUUXrX",
        "content": [
          {
            "title": "SWE-bench Verified Benchmark",
            "url": "https://www.emergentmind.com/topics/swe-bench-verified"
          },
          {
            "title": "Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study",
            "url": "https://arxiv.org/pdf/2503.15223"
          },
          {
            "title": "princeton-nlp/SWE-bench_Lite_oracle · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/princeton-nlp/SWE-bench_Lite_oracle"
          },
          {
            "title": "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and",
            "url": "https://arxiv.org/pdf/2506.17208"
          },
          {
            "title": "SWE-Bench: Real-World Software Benchmark",
            "url": "https://www.emergentmind.com/topics/swe-bench"
          },
          {
            "title": "Introduction to SWE Bench & Patch Centric Approach | by Zain ul Abideen | Medium",
            "url": "https://medium.com/@zaiinn440/introduction-to-swe-bench-patch-centric-approach-1b02f0517304"
          },
          {
            "title": "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems",
            "url": "https://arxiv.org/html/2506.17208v2"
          },
          {
            "title": "princeton-nlp/SWE-bench_oracle · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/princeton-nlp/SWE-bench_oracle"
          },
          {
            "title": "SWE-Bench Lite: Bug-Fixing Benchmark",
            "url": "https://www.emergentmind.com/topics/swe-bench-lite-dataset"
          },
          {
            "title": "princeton-nlp/SWE-bench · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/princeton-nlp/SWE-bench"
          }
        ]
      },
      "The search results provide information about SWE-bench, oracle retrieval settings, and various code repair approaches, but they don't contain specific research on the exact terms you're looking for regarding \"headroom gap fixed vs adaptive\" oracle configuration selection. Let me search for more specific information.",
      {
        "tool_use_id": "srvtoolu_01VrZGMLntACLAkRYyF4hgag",
        "content": [
          {
            "title": "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and",
            "url": "https://arxiv.org/pdf/2506.17208"
          },
          {
            "title": "SWE-Bench Leaderboards",
            "url": "https://www.emergentmind.com/topics/swe-bench-leaderboards"
          },
          {
            "title": "SWE-bench Verified Benchmark",
            "url": "https://www.emergentmind.com/topics/swe-bench-verified"
          },
          {
            "title": "Rigorous Evaluation of Coding Agents on SWE-Bench",
            "url": "https://aclanthology.org/2025.acl-long.189.pdf"
          },
          {
            "title": "SWE-bench",
            "url": "https://www.swebench.com/original.html"
          },
          {
            "title": "Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study",
            "url": "https://arxiv.org/html/2503.15223v1"
          },
          {
            "title": "SWE-Bench: Real-World Software Benchmark",
            "url": "https://www.emergentmind.com/topics/swe-bench"
          },
          {
            "title": "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems",
            "url": "https://arxiv.org/html/2506.17208v2"
          },
          {
            "title": "What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair",
            "url": "https://arxiv.org/pdf/2602.04449"
          },
          {
            "title": "2026-1-27 SWE-EVO: Benchmarking Coding Agents in",
            "url": "https://arxiv.org/pdf/2512.18470"
          }
        ]
      },
      "The search results still don't contain the specific terminology you mentioned (\"headroom gap fixed vs adaptive\" oracle configuration selection). Let me try a more targeted search.",
      {
        "tool_use_id": "srvtoolu_01RFycqRV8kHJj8PfSbmCvXZ",
        "content": []
      },
      "Unfortunately, the search for the exact phrase \"headroom gap fixed vs adaptive\" did not return results. Based on my comprehensive searches, I found extensive information about SWE-bench oracle configurations and code repair evaluation, but I was unable to locate specific research or documentation using the exact terminology \"oracle configuration selection code repair headroom gap fixed vs adaptive SWE-bench 2025 2026.\"\n\nThe search results do show:\n\n1. SWE-bench includes an \"Oracle\" retrieval setting where each instance uses the oracle-retrieved file format, which is a known retrieval configuration.\n\n2. The highest-performing agents use single- or multi-agent frameworks with a degree of autonomous control flow, allowing for adaptive reasoning and context-sensitive repair strategies.\n\n3. Recent submissions employ sophisticated patch selection strategies, such as TRAE using o1 to select among patches generated by multiple models, and AgentScope using Qwen2.5 to select the best result among multiple trials.\n\nHowever, I was unable to find specific research papers or documentation specifically discussing \"headroom gap fixed vs adaptive\" oracle configuration selection. This particular terminology may be from a very recent paper (early 2026), a preprint not yet widely indexed, or it may be using non-standard terminology. If you have a specific paper title or ArXiv link, I'd be happy to search for that."
    ],
    "durationSeconds": 11.748534398999997
  },
  "sourceToolAssistantUUID": "2734a900-623e-4b72-8bb4-777b6e84b76d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a5c1b554-252c-440c-94cb-d423c11a1fea",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate GranRoute: Configuration Routing for Code Repair",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Assistant

_source line 56 · 2026-05-11T23:44:16.674Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to write my review. Let me synthesize everything.

## Key Findings

### References
All cited references check out. The proposal has done an excellent job of citing relevant work.

### Missing Competitors (Critical)
1. **Mix-of-Granularity (MoG, COLING 2025, arXiv 2406.00456)** — This is the most critical missing competitor. MoG trains a router to dynamically select optimal chunking granularity for RAG, using a Mix-of-Experts-inspired approach with soft labels. While it's applied to general QA (not code repair), the core mechanism — a trained router that selects retrieval granularity — is essentially what GranRoute proposes. 

The proposal absolutely needs to cite this work and clearly explain how GranRoute differs from it.

2. **RAGRouter (NeurIPS 2025, arXiv 2505.23052)** — Routes queries to the best retrieval-augmented LLM using document embeddings and RAG capability embeddings with contrastive learning. First work on LLM routing specifically for RAG settings. Should be cited.

3. **ProCC (arXiv 2405.07530)** — Multi-retrieval augmented code completion with adaptive retrieval selection. Code-domain specific. Should be cited.

4. **"Rethinking Predictive LLM Routing" (arXiv 2505...)** — Looking at additional routing-related work that may be relevant.

Now I'm assessing the feasibility of the project. The budget looks reasonable at $0.08 per instance using Qwen3-Coder-Next, totaling around $1,200-$1,300 for API costs plus less than 40 H100-hours of GPU time, which comfortably fits within the 200 H100-hour limit. The 14-day timeline is tight but achievable with the API-based approach, and SWE-bench-Live provides enough instances for solid evaluation. The expected 10-15% Docker failure rate for Live is acceptable.

The core innovation here is taking routing methodology and applying it to retrieval configuration selection for code completion tasks.

However, there's a credibility issue: MoG already does granularity routing for RAG in a different domain using the same mechanism, and recent work like "Rethinking Predictive LLM Routing" demonstrates that simple kNN baselines often outperform more complex learned routers. While the proposal frames this as a problem formulation gap rather than a methodology gap, that distinction means the methodological contribution is limited. The novelty is fundamentally incremental—adapting existing routing techniques to a new domain. For an EMNLP short or Findings paper, this could work if the missing baselines are properly cited, the multi-method comparison produces meaningful insights, and the performance gains are substantial.

EMNLP is a borderline fit since the NLP angle centers on connecting natural language features of bug descriptions to optimal code comprehension granularity, though the routing methodology itself is well-established. The practical impact depends on headroom—anything above 10 percentage points would be a solid contribution, while 5-8pp still has value from a cost-efficiency perspective. The interpretable feature analysis linking linguistic properties to granularity choices is the most interesting angle here.

Against the requirements, the framework covers the methodology contribution, stays well under the compute budget, fits the timeline, and leverages existing code models appropriately. The main gap is that evaluation should extend beyond SWE-bench Verified to include HumanEval and MBPP for broader validation.

On balance, this scores as moderately novel—routing methods applied to a new domain with useful comparative analysis but no fundamental methodological innovation. Feasibility is strong with realistic costs and a smart go/no-go checkpoint. The proposal is clearly structured with good contingency planning, though the impact remains modest since the routing improvements themselves might be incremental. Overall assessment lands around 3.5 out of 5.

The core issues are significant gaps in related work—missing MoG, RAGRouter, ProCC, and the kNN baseline paper that questions whether simpler routing suffices. The evaluation plan also doesn't align with the user's original specification of HumanEval, MBPP, and other benchmarks, though there's a valid argument that repo-level code repair doesn't map cleanly to those single-file tasks. The fundamental uncertainty is whether there's enough headroom for meaningful improvement, and whether the multi-method comparison adds value if a basic kNN approach already works well.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5c1b554-252c-440c-94cb-d423c11a1fea",
  "isSidechain": false,
  "requestId": "req_011CawfmX49G1tnHmrZjD4Gd",
  "type": "assistant",
  "uuid": "c43850f8-f49f-46b6-8e06-c86e1da7a11c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkFB7bKSJvarL4pQ9ZPwP7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 53506,
      "output_tokens": 3473,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2533,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3473,
          "cache_read_input_tokens": 53506,
          "cache_creation_input_tokens": 2533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2533
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

_source line 57 · 2026-05-11T23:45:03.352Z_

Now I have comprehensive data. Let me synthesize my review.

**Summary of findings:**
- All cited references verified correctly (10/10)
- Feasibility checks out: costs, timeline, and data availability are realistic
- Three critical missing competitors found: MoG (COLING 2025), RAGRouter (NeurIPS 2025), and "Rethinking Predictive LLM Routing" (arXiv 2505.12601)
- Venue deadline confirmed (May 25, 2026)

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "Mix-of-Granularity (MoG, COLING 2025) already trains a router to dynamically select optimal retrieval granularity for RAG — the same core mechanism GranRoute proposes, applied to general QA rather than code repair. GranRoute's novelty reduces to domain transfer (code repair) plus the multi-method comparison, which is incremental. The proposal honestly self-identifies this as 'a problem formulation gap, not a methodology gap,' confirming limited methodological novelty."},
    "feasibility": {"score": 4, "rationale": "API-based oracle collection with Qwen3-Coder-Next at ~$0.08/instance is verified as plausible. Total budget (~$1,200 API + <40 H100-hours GPU) is well within the ≤200 H100-hour constraint. The 14-day timeline is tight but achievable. The go/no-go gate at 50 instances is a smart de-risking strategy."},
    "clarity": {"score": 4, "rationale": "Exceptionally well-structured proposal with clear phases, cost breakdowns, contingency plans, and extensive related work coverage. The phased design with explicit headroom pilot and adaptation strategy for small-headroom scenarios shows mature research planning. Minor gap: missing critical competitors undermines the landscape completeness."},
    "impact": {"score": 3, "rationale": "The practical contribution depends entirely on the headroom, which is unverified. The cited evidence (arXiv 2604.00167) shows only 3pp gap between best and worst fixed configs on 50 instances — the oracle-over-best-fixed gap could be even smaller. If headroom is modest, the cost-efficiency angle is a fallback but a thin one. The interpretable NL-feature analysis is interesting but supporting, not impactful on its own."}
  },
  "issues": [
    "CRITICAL: Missing Mix-of-Granularity (MoG, COLING 2025, arXiv 2406.00456) — trains a router to dynamically select optimal retrieval granularity for RAG using soft labels, which is the same core mechanism as GranRoute. The only difference is domain (general QA vs. code repair). This must be cited and explicitly differentiated; without it, the novelty claim ('no routing method targets retrieval configuration') is factually incorrect — MoG targets retrieval granularity, which is a subset of GranRoute's configuration space.",
    "CRITICAL: Missing RAGRouter (NeurIPS 2025, arXiv 2505.23052) — the first routing method specifically designed for RAG settings, using document embeddings and RAG capability embeddings. As a NeurIPS 2025 paper on routing in RAG, it is highly relevant and would be noticed by any reviewer familiar with the routing literature.",
    "IMPORTANT: Missing 'Rethinking Predictive LLM Routing' (arXiv 2505.12601, May 2025) — demonstrates that a simple kNN baseline matches or outperforms complex learned routers across diverse tasks. This directly challenges GranRoute's elaborate 5-method comparison: if kNN dominates, the entire multi-method contribution collapses. This paper must be cited, and kNN must be included as a 6th baseline method.",
    "IMPORTANT: Missing ProCC (arXiv 2405.07530, TOSEM 2025) — uses multi-retrieval augmented generation with adaptive retrieval selection for code completion. While it targets code completion rather than repair, it is in the same domain (adaptive retrieval for code tasks) and must be cited.",
    "Headroom risk remains unresolved and foundational — the arXiv 2604.00167 study found only 3pp difference between best and worst fixed granularities (function 45.6% vs. file 42.6%) on 50 instances. The oracle bound (per-instance best) over the best fixed config could be only 2-5pp. The go/no-go gate is good, but if the headroom is <5pp, the paper's entire premise weakens to a cost-efficiency argument, which may not sustain a publication even as a short paper.",
    "The 5-method comparison contribution is vulnerable to the 'ablation-as-paper' criticism, especially given that existing routing benchmarks (LLMRouterBench, RouterEval) already provide more comprehensive method comparisons. The paper needs a clear narrative about what novel insight emerges from the comparison (e.g., 'code repair routing requires fundamentally different methods than model routing because...'), not just which method achieves the highest number."
  ],
  "feedback": "The proposal has matured substantially over 4 rounds — the feasibility is now realistic, the gap argument is well-supported, and the approach is sensible. The remaining issues are fixable but important:\n\n1. **Cite and differentiate from MoG (COLING 2025).** MoG is the single biggest threat to novelty. The differentiation should argue: (a) MoG routes over text chunking granularity for knowledge QA, while GranRoute routes over fault-localization granularity + context budget jointly for code repair — a 2D configuration space vs. 1D; (b) MoG uses soft labels from retrieval quality, while GranRoute uses downstream repair success as oracle signal — end-task alignment; (c) code repair has unique routing signals (stack traces, error types, code structure) unavailable in QA. This is a legitimate distinction but must be made explicit.\n\n2. **Cite RAGRouter (NeurIPS 2025)** and position GranRoute as targeting a different routing dimension (retrieval configuration vs. which RAG-LLM to use).\n\n3. **Add kNN as a baseline method.** Given the findings from 'Rethinking Predictive LLM Routing,' include a 6th method — kNN on the same feature space. If kNN dominates, the paper's insight becomes 'simple non-parametric methods suffice for code repair routing' — still publishable as a short paper. If learned methods beat kNN, you have stronger justification for the routing framework.\n\n4. **Cite ProCC** and distinguish by target task (completion vs. repair) and routing target (retrieval perspective vs. configuration).\n\n5. **Strengthen the multi-method comparison narrative.** The paper should not just report 'Method X wins.' It should extract a generalizable insight: Do preference-based methods (à la RouteLLM) work better for configuration routing than classification? Does the answer depend on data size? Does code-specific structure create different routing dynamics than NL routing? Frame the comparison as answering a specific research question about routing methodology, not as an ablation.\n\n6. **Address the small-headroom scenario more concretely.** If the pilot shows 3-5pp headroom, the paper could pivot to a diagnostic contribution: 'We find that retrieval configuration routing for code repair yields X% accuracy gain and Y% cost savings, and that the dominant routing signal is Z.' Even a modest-headroom finding is publishable if the analysis is insightful.\n\nWith these changes, the proposal is viable for EMNLP Findings as a short paper. EMNLP Main would require stronger novelty — consider whether the 2D routing space (granularity × budget) with dual-signal architecture (NL + code features at different pipeline stages) can be positioned as a methodological contribution rather than pure domain transfer.",
  "reason": "Critical missing competitor (MoG, COLING 2025) undermines the core novelty claim; kNN baseline omission leaves the multi-method contribution vulnerable; incremental novelty (domain transfer of known routing methods) yields average score 3.5, below the 4.0 threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c43850f8-f49f-46b6-8e06-c86e1da7a11c",
  "isSidechain": false,
  "requestId": "req_011CawfmX49G1tnHmrZjD4Gd",
  "type": "assistant",
  "uuid": "f2f903d0-6c1f-49fa-8918-7fad5d89c71c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UkFB7bKSJvarL4pQ9ZPwP7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 53506,
      "output_tokens": 3473,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2533,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3473,
          "cache_read_input_tokens": 53506,
          "cache_creation_input_tokens": 2533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2533
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

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "f2f903d0-6c1f-49fa-8918-7fad5d89c71c",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate GranRoute: Configuration Routing for Code Repair",
  "sessionId": "374fbfc5-cb65-4184-9681-4b68ae4e643d"
}
```

---
