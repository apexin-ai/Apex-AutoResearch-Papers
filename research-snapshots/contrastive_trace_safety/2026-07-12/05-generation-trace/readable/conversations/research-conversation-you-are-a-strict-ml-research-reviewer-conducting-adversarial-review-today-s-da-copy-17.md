# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/b29c0f20-422e-4834-bd9e-75b9cee267e3.jsonl`
- **Structured JSON:** [`aa0ceb8f06366e25d3b2.json`](../../sessions/aa/aa0ceb8f06366e25d3b2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T18:28:21.687Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T18:28:21.687Z",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 3/10)\n{\n  \"title\": \"DiagPRM: Stage-Level Diagnostic Reasoning Rewards for Code Repair Search\",\n  \"core_problem\": \"Reward models for code repair agents operate at two granularities that each miss critical information. Trajectory-level scorers (SWE-RM achieves 62–74.6% on SWE-bench Verified via best-of-N) provide a single holistic score for the entire multi-turn interaction but cannot localize which reasoning stage—localization, diagnosis, or patch design—caused failure, limiting their value for credit assignment and trajectory steering. Patch-level verifiers (R4P achieves 72.2% verification accuracy via reasoning about final patches) skip the diagnostic process entirely. Step-level action-utility PRMs (SWE-Shepherd) attempt localized scoring but suffer fundamental credit assignment noise—actions that look locally useful may lead to dead ends, yielding 51% vs. 57% for greedy baselines. Can we build a step-level PRM that scores a more stable signal—the logical soundness of diagnostic reasoning at each repair stage—and use stage-level credit assignment to guide repair search?\",\n  \"opportunity\": \"Code repair follows a diagnostic reasoning structure (localize → diagnose → patch) where intermediate diagnostic claims make verifiable predictions checkable against test execution outcomes—a domain-specific advantage absent from code generation or general agent tasks. This creates three opportunities no existing system exploits simultaneously: (1) Stage-level decomposition enables localized credit assignment that trajectory-level scorers (SWE-RM) cannot provide—even when a trajectory fails, we can identify that localization reasoning was sound but diagnosis was flawed; (2) Reasoning quality is a property of the reasoning chain itself, not of future actions, making it a lower-variance scoring target than action utility (SWE-Shepherd), with a formal argument: Var(Q_reasoning|prefix) = 0 as Q depends only on observables, while Var(U_action|prefix) > 0 as U depends on stochastic future decisions; (3) Test execution outcomes serve as automatic validators for reasoning quality annotations during training—not as runtime input (addressing Haque et al.'s finding)—enabling training label quality verification that general-purpose reasoning evaluators (Agent-RRM) lack because they have no domain-specific ground truth. While RGFL generates structured reasoning explanations for fault localization (85% Hit@1) and R4P reasons about patches, neither trains a reward model for search guidance across the full diagnostic process. ORPS demonstrates execution-grounded process rewards without a trained PRM, but requires execution at every search tree node and targets generation, not repair. The gap—a trained step-level PRM that evaluates diagnostic reasoning quality across all repair stages, using test execution only for training label validation, execution-free at inference—remains open.\",\n  \"landscape\": \"SWE-RM (arXiv:2512.21919, Dec 2025, Qwen team) is the current strongest reward model for SWE agents: a 30B MoE model (3B active) trained on ~100K trajectories with binary whole-trajectory scoring, achieving 51.6→62.0% (Flash) and 67.0→74.6% (Max) on SWE-bench Verified via best-of-N, plus RL gains. It scores complete trajectories holistically but provides no step-level diagnostic feedback. R4P/Patch Reasoner (arXiv:2510.22775, Oct 2025) frames patch verification as reasoning via group-wise RL, achieving 72.2% accuracy surpassing o3 and 50× faster than testing, but evaluates final patches, not the diagnostic process leading to them. RGFL (arXiv:2601.18044, Jan 2026) generates structured per-candidate reasoning explanations for fault localization achieving 85% Hit@1 on SWE-bench Verified, but is a one-shot ranker—not a reward model—and covers only the localization stage, not diagnosis or patch design. Agent-RRM (arXiv:2601.22154, Jan 2026) produces decomposed trajectory judgments (reasoning trace + critique + holistic score) for general agent tasks (GAIA, WebWalkerQA) but is not specialized for code repair and lacks domain-specific ground truth for training label validation. ORPS (ICML 2025, arXiv:2412.15118) demonstrates that execution-grounded self-critique generates high-quality process rewards without trained PRMs (26.9% correctness gain), but requires execution at every search tree node—expensive and infeasible for large-repository repair—and targets code generation, not repair. SWE-Shepherd (arXiv:2604.10493, April 2026) introduces step-level action-utility PRMs for SWE agents but achieves only 51% vs. 57% greedy baseline on 100 SWE-bench Verified tasks, confirming that action utility suffers credit assignment noise. SWE-TRACE (arXiv:2604.14820, April 2026) uses rubric-based PRMs with heuristic test-time scaling, achieving competitive results but relying on hand-designed rubric criteria rather than learned reasoning quality. TRAJEVAL (arXiv:2603.24631, March 2026) decomposes trajectories into mechanical search/read/edit stages for diagnostic evaluation (Pass@1 MAE 0.87–2.1%) but evaluates file/function retrieval precision, not cognitive reasoning quality. ExecVerify (arXiv:2603.11226, March 2026) trains execution-understanding rewards (next-statement/variable prediction) but targets execution trace comprehension, not diagnostic reasoning evaluation. ThinkPRM (arXiv:2504.16828, April 2025) demonstrates data-efficient generative PRMs outperforming discriminative PRMs with 1% of process labels. AgentPRM (arXiv:2511.08325, ACM Web 2026) achieves 8× compute efficiency using TD-based estimation for agent PRMs. FunPRM (arXiv:2601.22249, Jan 2026) treats functions as PRM steps for code generation, achieving SOTA on LiveCodeBench. Agent-RLVR (arXiv:2506.11425, June 2026) trains SWE agents via guidance and environment rewards with patch-level reward model scoring.\",\n  \"approach\": \"We define a 3-stage diagnostic reasoning taxonomy for code repair—localize (connect symptoms to fault location), diagnose (identify root cause), patch (design fix from diagnosis)—and extract stage boundaries from natural language repair trajectories using an LLM parser. Using the publicly available SWE-smith 66K trajectory corpus (Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k), we annotate diagnostic reasoning quality at each stage via an LLM-judge (Claude/GPT-4o) that evaluates: (1) whether localization reasoning correctly connects error evidence to candidate locations, (2) whether the root cause hypothesis logically explains the observed failure, (3) whether the fix rationale follows from the diagnosis. We address the LLM-judge circularity concern through two mechanisms. First, we explicitly mine disagreement cases between reasoning quality and test outcomes as the most distinctive training signal: trajectories with sound reasoning but failed patches (correct diagnosis, implementation error) teach the PRM that the reasoning was good despite bad outcome, while trajectories with poor reasoning but passing patches (lucky guess, partial fix) teach it to penalize unsound reasoning despite success. These disagreement cases are exactly where DiagPRM provides information that outcome reward cannot. Second, the stage-level decomposition provides strictly more information than binary outcome: even when a trajectory fails, DiagPRM distinguishes 'good localization + bad diagnosis + bad patch' from 'bad localization + everything downstream wrong,' enabling localized credit assignment impossible with trajectory-level scoring. We validate LLM-judge annotation quality through a pilot study on 50 trajectories (150 reasoning steps): three LLM judges (Claude, GPT-4o, Gemini) independently annotate reasoning quality, and we measure inter-model Cohen's kappa, correlation with test outcomes (expecting moderate ~0.4-0.6, not perfect, correlation—high correlation would indicate the PRM is a mere outcome proxy, while moderate correlation confirms it captures distinct information), and compare inter-annotator agreement for reasoning quality labels vs. action utility labels on the same trajectories. We train DiagPRM as a lightweight LoRA-tuned classifier on Qwen3-8B (~15K annotated step-outcome pairs), following ThinkPRM's insight that small amounts of high-quality process labels suffice. We include a formal argument for the stability advantage: define reasoning quality Q(r_t) as a function of the reasoning chain r_t and observable evidence at step t. Q depends only on the trajectory prefix, so Var(Q|prefix) reflects only annotator noise. Action utility U(a_t) = E[R(τ)|prefix, a_t] depends on stochastic future actions, so Var(U|prefix) includes both annotator noise AND irreducible variance from unknown future decisions. Thus Var(Q|prefix) < Var(U|prefix) in expectation, explaining SWE-Shepherd's credit assignment failures. At inference, DiagPRM guides best-of-N selection and stage-level reranking. For SWE-bench Verified evaluation, we generate N=5 trajectories per instance on the same 100 instances used by SWE-Shepherd, using API-based agent trajectory generation (shifting cost from GPU to API budget). We evaluate against: (1) SWE-RM as primary baseline (trajectory-level scoring), testing both standalone comparison and DiagPRM+SWE-RM combination to demonstrate complementarity of step-level and trajectory-level signals; (2) SWE-Shepherd (step-level action utility PRM); (3) SWE-TRACE (rubric PRM); (4) outcome-only best-of-N reranking; (5) random selection. We additionally evaluate on 1000 DebugBench instances (N=3, local model) across bug categories to test whether DiagPRM's per-stage scoring captures the category-dependent reasoning quality variation documented in DebugBench. We differentiate from R4P by noting it evaluates final patches—orthogonal to diagnostic process evaluation, since a good patch can emerge from bad reasoning (lucky guess) and a bad patch from good reasoning (correct diagnosis, implementation error); from RGFL by noting it is a one-shot localization ranker that cannot guide multi-candidate search or serve as RL reward; from Agent-RRM by noting its general-purpose design lacks code repair's verifiable intermediate claims for training label validation; and from ORPS by noting it requires execution at every search node while DiagPRM is execution-free at inference.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~130h H100 (pilot study ~5h, LLM-judge annotation inference ~15h, PRM LoRA training iterations ~50h, DebugBench trajectory generation with local model ~40h, ablations ~20h)\",\n      \"gpu_utilization\": \"~35-45% effective utilization; GPUs idle during annotation pipeline design, pilot study analysis, and result interpretation\",\n      \"timeline\": \"5-7 weeks (pilot study 1 week, annotation pipeline + labeling 1-2 weeks, PRM training 1-2 weeks, evaluation 1-2 weeks)\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"$390-520 (at ~$3/hr H100)\",\n      \"llm_api_cost\": \"$2,200-3,200 (SWE-bench trajectory generation via API agent: 100×5=500 trajectories ~$1,500-2,500; LLM-judge annotation of ~15-20K steps ~$200-400; pilot study multi-judge ~$50; action-utility comparison labels ~$100)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~110h H100 (more targeted experiments due to faster iteration on pilot study and annotation quality)\",\n      \"gpu_utilization\": \"~55-70% utilization; agent handles annotation pipeline and training code, human reviews pilot study results and interprets disagreement cases\",\n      \"timeline\": \"14-18 days (pilot study + annotation pipeline 3-4 days, LLM-judge labeling 2 days, PRM training iterations 3-4 days, evaluation 3-4 days, paper 3-4 days)\",\n      \"team\": \"1 researcher, ~45min/day for pilot study review, annotation quality verification, and disagreement case analysis\",\n      \"claude_api_cost\": \"$150-300 (experiment orchestration and code generation)\",\n      \"estimated_gpu_cost\": \"$330-450 (at ~$3/hr H100)\",\n      \"llm_api_cost\": \"$2,200-3,200 (trajectory generation + annotation + pilot)\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~160h H100 (broader pilot study, multiple annotation strategies, full evaluation grid)\",\n      \"gpu_utilization\": \"~80-90% utilization; agent continuously runs pilot, annotation, training, and evaluation pipelines\",\n      \"timeline\": \"12-16 days with 4x H100 (pilot study 2-3 days, annotation 1-2 days, parallel PRM training sweeps 3-4 days, evaluation grid 3-4 days, paper assembly 2-3 days)\",\n      \"team\": \"0 (initial 1-hour setup for cluster access and API keys)\",\n      \"claude_api_cost\": \"$300-500 (end-to-end autonomous research)\",\n      \"estimated_gpu_cost\": \"$480-650 (at ~$3/hr H100)\",\n      \"llm_api_cost\": \"$2,500-3,800 (trajectory generation with multiple strategies + annotation + pilot)\",\n      \"speed_bottleneck\": \"API-based trajectory generation throughput (500 SWE-bench trajectories at ~3-5 min each with parallel API calls); secondary bottleneck is PRM training convergence\",\n      \"risk_note\": \"Two key risks: (1) LLM-judge inter-annotator agreement on reasoning quality may be low (<0.6 kappa)—mitigated by pilot study validating feasibility before full annotation; (2) DiagPRM may not outperform SWE-RM on best-of-N due to model size gap (8B vs 30B)—mitigated by framing contribution as complementary step-level signal and testing DiagPRM+SWE-RM combination\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline: May 25, 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"SWE-RM: Execution-free Feedback for SWE Agents (arXiv:2512.21919, Dec 2025) — trajectory-level RM, primary baseline\",\n    \"R4P/Patch Reasoner: Scalable Supervising SWE Agents (arXiv:2510.22775, Oct 2025) — patch-level reasoning verifier\",\n    \"RGFL: Reasoning Guided Fault Localization for APR (arXiv:2601.18044, Jan 2026) — structured reasoning for localization\",\n    \"Agent-RRM: Exploring Reasoning Reward Model for Agents (arXiv:2601.22154, Jan 2026) — general-purpose reasoning RM\",\n    \"ORPS: Reasoning Through Execution / Outcome-Refining Process Supervision (arXiv:2412.15118, ICML 2025) — execution-grounded process rewards without trained PRM\",\n    \"SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents (arXiv:2604.10493, April 2026)\",\n    \"SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric PRMs (arXiv:2604.14820, April 2026)\",\n    \"TRAJEVAL: Decomposing Code Agent Trajectories for Fine-Grained Diagnosis (arXiv:2603.24631, March 2026)\",\n    \"ExecVerify: White-Box RL with Verifiable Stepwise Rewards (arXiv:2603.11226, March 2026)\",\n    \"Towards Effectively Leveraging Execution Traces for Program Repair (Haque et al., arXiv:2505.04441, May 2025)\",\n    \"TraceRepair: Runtime Execution Traces Guided APR with Multi-Agent Debate (arXiv:2604.02647, April 2026)\",\n    \"Process Reward Models That Think (ThinkPRM) (arXiv:2504.16828, April 2025)\",\n    \"AgentPRM: Process Reward Models for LLM Agents (arXiv:2511.08325, ACM Web 2026)\",\n    \"FunPRM: Function-as-Step PRM for Code Generation (arXiv:2601.22249, Jan 2026)\",\n    \"Agent-RLVR: Training SWE Agents via Guidance and Environment Rewards (arXiv:2506.11425, June 2026)\",\n    \"SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025 D&B Spotlight)\",\n    \"DebugBench: Evaluating Debugging Capability of LLMs (ACL 2024 Findings)\",\n    \"RePair: Automated Program Repair with Process-based Feedback (ACL 2024 Findings)\",\n    \"CodePRM: Execution Feedback-enhanced PRM for Code Generation (ACL 2025 Findings)\"\n  ],\n  \"description\": \"We propose DiagPRM, a stage-level process reward model that evaluates the logical soundness of diagnostic reasoning in code repair trajectories. Existing reward models for code repair operate at either the trajectory level (SWE-RM scores whole trajectories holistically, achieving 62–74.6% via best-of-N but providing no step-level diagnostic feedback) or the patch level (R4P reasons about final patches, not the diagnostic process). Step-level action-utility PRMs (SWE-Shepherd, 51% vs. 57% greedy) suffer credit assignment noise because utility depends on stochastic future actions. DiagPRM addresses these limitations by scoring diagnostic reasoning quality—a property of the reasoning chain itself, not of future actions—at three cognitive stages: localize (connect symptoms to fault locations), diagnose (identify root cause), and patch (design fix from diagnosis). We provide a formal stability argument: reasoning quality Q(r_t) depends only on the trajectory prefix, so Var(Q|prefix) reflects only annotator noise, while action utility Var(U|prefix) additionally includes irreducible variance from unknown future decisions. We train DiagPRM as a LoRA-tuned Qwen3-8B classifier on ~15K annotated step-outcome pairs from the 66K SWE-smith trajectory corpus. To address LLM-judge circularity, we explicitly mine disagreement cases (sound reasoning + failed patch; poor reasoning + passing patch) as the most distinctive training signal—these are exactly where DiagPRM provides information that outcome reward cannot—and validate annotation quality through a 50-trajectory pilot comparing inter-model agreement on reasoning quality vs. action utility labels. The stage-level decomposition provides strictly more information than binary outcomes: even for failed trajectories, DiagPRM distinguishes 'correct localization + wrong diagnosis' from 'wrong localization + cascading failure,' enabling localized credit assignment. We differentiate from RGFL (one-shot localization ranker, not a reward model for search guidance), Agent-RRM (general-purpose, lacks code repair's verifiable intermediate claims), and ORPS (requires execution at every search node, generation-only). We evaluate best-of-N selection and stage-level reranking on 100 SWE-bench Verified instances against SWE-RM (primary baseline, testing both standalone and DiagPRM+SWE-RM complementarity), SWE-Shepherd, SWE-TRACE, outcome-only, and random baselines, plus 1000 DebugBench instances for category-dependent analysis. API-based trajectory generation for SWE-bench shifts primary evaluation cost from GPU to API budget (~$1,500-2,500 for 500 trajectories).\",\n  \"project_name\": \"diag_prm_repair\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL: Target venues (AAAI 2027, ICLR 2027, ICSE 2027) do not match user requirement of EMNLP 2026 (ARR deadline May 25, 2026). This is a fundamental requirement violation.\", \"CRITICAL: Resource estimate vastly exceeds user constraint of ≤200 H100-hours. Manual mode: ~400 A100-hours; auto mode: 900-1200 A100-hours. Even with H100 being ~2x faster than A100, auto mode still requires 450-600 H100-hours.\", \"CRITICAL: Timeline mismatch. User requires ≤16 days. Manual timeline is 4-6 months. Auto mode is 10-18 days but requires 3-6x the allowed compute budget.\", \"Counterevidence not addressed: Haque et al. (arXiv:2505.04441, May 2025) found execution traces provide limited APR benefit in 4/6 configurations, with effectiveness diminishing as trace complexity increases. The proposed idea's core assumption that traces serve as 'automatic verification oracles' directly contradicts this finding.\", \"ExecVerify (arXiv:2603.11226, March 2026) already uses execution traces for verifiable stepwise rewards in RL training, achieving 5.9% pass@1 improvement. This paper was not cited and significantly overlaps with the proposed execution-trace-as-verification-signal approach.\", \"Crowded competitive landscape: SWE-Shepherd, SWE-TRACE, ExecVerify, TraceRepair, TRAJEVAL, and CodeTracer all published March-April 2026, collectively covering PRMs for code agents, trace-based repair, and trajectory decomposition. The incremental novelty over this ensemble is unclear.\", \"The 5-stage diagnostic taxonomy requires reliable automatic segmentation of repair trajectories into fault localization, root cause diagnosis, causal hypothesis, patch synthesis, and verification stages. No evidence is provided that such segmentation can be done reliably at scale, and this engineering challenge alone could consume the entire timeline.\", \"SWE-Shepherd achieves 51% on SWE-bench Verified with a lightweight PRM. The proposed approach needs to demonstrate clear improvement over this baseline, but the idea provides no pilot results or theoretical argument for expected gains.\"]\nFeedback: This idea has a genuinely interesting core insight (repair follows diagnostic reasoning, not generation steps), but it fails to meet the user's requirements on three critical dimensions: venue, compute, and timeline. Here is specific guidance for revision:\n\n1. **Fix venue targeting**: Must target EMNLP 2026 ARR (May 25 deadline). Reframe the contribution around NLP/code understanding aspects (diagnostic reasoning as a language understanding problem) rather than pure SE.\n\n2. **Radically reduce scope to fit ≤200 H100-hours and ≤16 days**: Drop the full 5-stage taxonomy and VizTracer instrumentation pipeline. Instead, focus on a simpler 2-3 stage decomposition (localize → hypothesize → patch) using existing structured outputs from SWE-agent trajectories (which already contain file reads, edits, and test runs as natural stage boundaries). Use SWE-Shepherd's existing reward dataset as a starting point and add diagnostic reasoning annotations via an LLM judge rather than building a trace pipeline from scratch.\n\n3. **Address the trace effectiveness counterevidence**: Cite and discuss Haque et al. (2505.04441). Argue why your approach differs (you use traces for PRM training signal, not as direct prompt augmentation). Better yet, run a small pilot showing your trace-based verification signal is informative.\n\n4. **Cite and differentiate from ExecVerify (2603.11226)**: This paper already does execution-trace-based stepwise verification for RL. Explain why your diagnostic decomposition adds value beyond ExecVerify's general stepwise approach.\n\n5. **Simplify the training pipeline**: Instead of PRIME-RL implicit PRM with VizTracer instrumentation on 50K trajectories, consider training a lightweight classifier on SWE-smith trajectories using LLM-annotated diagnostic stage labels. This could fit within 100-150 H100-hours.\n\n6. **Narrow evaluation**: Drop CodeContests and CrossCodeEval (not relevant to repair). Focus on SWE-bench Verified and DebugBench only, with SWE-Shepherd as the primary baseline.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING BASELINE: SWE-RM (arXiv:2512.21919, Dec 2025, Qwen team) is a 30B MoE reward model for SWE agents achieving 51.6%→62.0% (Flash) and 67.0%→74.6% (Max) on SWE-bench Verified via best-of-N. This is dramatically stronger than SWE-Shepherd (51%) and must be the primary baseline. The proposal's framing of SWE-Shepherd as the main PRM competitor is misleading when SWE-RM exists.\", \"MISSING COMPETITOR: R4P/Patch Reasoner (arXiv:2510.22775, Oct 2025) explicitly frames patch verification as 'a reasoning task, mirroring how human repository maintainers review patches.' It achieves 72.2% verification accuracy surpassing OpenAI o3 and uses RL with group-wise objectives. This directly overlaps with DiagPRM's claim of evaluating reasoning quality in repair.\", \"MISSING COMPETITOR: RGFL (arXiv:2601.18044, Jan 2026) generates structured, bug-specific reasoning explanations for fault localization, achieving 85% Hit@1 on SWE-bench Verified. Its per-candidate 'reasoning about functionality and causal relationship to symptoms' directly overlaps with DiagPRM's localization reasoning stage.\", \"MISSING COMPETITOR: Agent-RRM (arXiv:2601.22154, Jan 2026) produces decomposed trajectory judgments: (1) reasoning trace analyzing logical consistency, (2) targeted critique identifying reasoning flaws, (3) holistic quality score. While general-purpose, it directly targets 'reasoning quality evaluation' in agent trajectories—DiagPRM's core contribution claim.\", \"MISSING COMPETITOR: ORPS (ICML 2025, arXiv:2412.15118) demonstrates that LLMs' intrinsic reasoning + execution feedback can generate high-quality process rewards WITHOUT trained PRMs, achieving 26.9% higher correctness. This challenges DiagPRM's premise that a trained PRM is needed when execution-grounded self-critique suffices.\", \"LLM-judge annotation quality risk is undersized: Research shows LLMs frequently misclassify code correctness. Scoring 'diagnostic reasoning quality'—whether localization reasoning correctly connects evidence to fault locations—is strictly harder than code correctness judgment. The proposal's validation against test outcomes helps but creates a circular dependency: if the LLM judge agrees with outcome labels, it's just a noisy proxy for outcome rewards; if it disagrees, which do you trust?\", \"Compute budget likely underestimated for evaluation: Best-of-N (N≥5) on 500 SWE-bench Verified instances requires ≥2500 trajectory generations. At ~3.5 min/trajectory with a local model, that's ~146 GPU-hours for evaluation alone, not 70h as estimated. Combined with annotation (20h) and training (50h), total exceeds 200h H100.\", \"Theoretical argument unsubstantiated: The claim that 'reasoning quality is more stable because logically sound reasoning generalizes across trajectory continuations' is intuitive but has no formal backing or empirical pilot. Reasoning quality labels from an LLM judge may be equally noisy as utility labels—the noise source differs (judge unreliability vs. credit assignment) but the effect on PRM training may be similar.\"]\nFeedback: The revision successfully addressed Round 1's venue, compute, and timeline issues, and the 3-stage diagnostic taxonomy is a meaningful simplification. However, the competitive landscape analysis has significant gaps that undermine the novelty claim. Here is specific guidance:\n\n1. **Add SWE-RM as primary baseline**: SWE-RM (arXiv:2512.21919) is the strongest existing reward model for SWE agents (62-74.6% on SWE-bench Verified). You must compare against it, not just SWE-Shepherd (51%). Argue why diagnostic reasoning scoring adds value over SWE-RM's execution-free whole-trajectory scoring.\n\n2. **Differentiate from R4P and RGFL**: R4P frames patch verification as reasoning; RGFL does structured reasoning for fault localization. DiagPRM's differentiation should emphasize that it evaluates the PROCESS of reasoning across stages (not just the final patch or individual localization), and that it trains a reward model to guide search (unlike RGFL which is a one-shot ranker).\n\n3. **Address Agent-RRM overlap**: Acknowledge that general agent reasoning evaluation exists and argue that code repair's verifiable intermediate claims (via test execution) provide a domain-specific advantage for training supervision that general-purpose reasoning evaluation lacks.\n\n4. **Fix compute budget**: Either reduce N in best-of-N (use N=3 instead of N=5), evaluate on fewer instances (e.g., the same 100 used by SWE-Shepherd), or account for using API-based trajectory generation (shifting cost from GPU to API budget). Be explicit about what generates trajectories.\n\n5. **Add a small pilot or theoretical grounding**: The reasoning quality stability claim is the paper's key theoretical contribution but is unargued. At minimum, add a formal argument: e.g., if reasoning quality Q is a property of the reasoning chain independent of future actions, then Var(Q|trajectory_prefix) < Var(utility|trajectory_prefix). Or describe a small-scale pilot (50 trajectories) comparing inter-annotator agreement for reasoning quality vs. action utility labels.\n\n6. **Address the LLM-judge circularity**: If LLM-judge labels are validated against test outcomes, and DiagPRM is trained on these labels, then DiagPRM may just be learning a noisy proxy for outcome rewards. Explain why this proxy is better than direct outcome reward (e.g., the decomposition into stages provides localized error signal even when the overall outcome is incorrect).\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T18:28:21.692Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T18:28:21.692Z",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-10T18:28:21.718Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-10 (UTC).**

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

## Idea under review (round 3/10)
{
  "title": "DiagPRM: Stage-Level Diagnostic Reasoning Rewards for Code Repair Search",
  "core_problem": "Reward models for code repair agents operate at two granularities that each miss critical information. Trajectory-level scorers (SWE-RM achieves 62–74.6% on SWE-bench Verified via best-of-N) provide a single holistic score for the entire multi-turn interaction but cannot localize which reasoning stage—localization, diagnosis, or patch design—caused failure, limiting their value for credit assignment and trajectory steering. Patch-level verifiers (R4P achieves 72.2% verification accuracy via reasoning about final patches) skip the diagnostic process entirely. Step-level action-utility PRMs (SWE-Shepherd) attempt localized scoring but suffer fundamental credit assignment noise—actions that look locally useful may lead to dead ends, yielding 51% vs. 57% for greedy baselines. Can we build a step-level PRM that scores a more stable signal—the logical soundness of diagnostic reasoning at each repair stage—and use stage-level credit assignment to guide repair search?",
  "opportunity": "Code repair follows a diagnostic reasoning structure (localize → diagnose → patch) where intermediate diagnostic claims make verifiable predictions checkable against test execution outcomes—a domain-specific advantage absent from code generation or general agent tasks. This creates three opportunities no existing system exploits simultaneously: (1) Stage-level decomposition enables localized credit assignment that trajectory-level scorers (SWE-RM) cannot provide—even when a trajectory fails, we can identify that localization reasoning was sound but diagnosis was flawed; (2) Reasoning quality is a property of the reasoning chain itself, not of future actions, making it a lower-variance scoring target than action utility (SWE-Shepherd), with a formal argument: Var(Q_reasoning|prefix) = 0 as Q depends only on observables, while Var(U_action|prefix) > 0 as U depends on stochastic future decisions; (3) Test execution outcomes serve as automatic validators for reasoning quality annotations during training—not as runtime input (addressing Haque et al.'s finding)—enabling training label quality verification that general-purpose reasoning evaluators (Agent-RRM) lack because they have no domain-specific ground truth. While RGFL generates structured reasoning explanations for fault localization (85% Hit@1) and R4P reasons about patches, neither trains a reward model for search guidance across the full diagnostic process. ORPS demonstrates execution-grounded process rewards without a trained PRM, but requires execution at every search tree node and targets generation, not repair. The gap—a trained step-level PRM that evaluates diagnostic reasoning quality across all repair stages, using test execution only for training label validation, execution-free at inference—remains open.",
  "landscape": "SWE-RM (arXiv:2512.21919, Dec 2025, Qwen team) is the current strongest reward model for SWE agents: a 30B MoE model (3B active) trained on ~100K trajectories with binary whole-trajectory scoring, achieving 51.6→62.0% (Flash) and 67.0→74.6% (Max) on SWE-bench Verified via best-of-N, plus RL gains. It scores complete trajectories holistically but provides no step-level diagnostic feedback. R4P/Patch Reasoner (arXiv:2510.22775, Oct 2025) frames patch verification as reasoning via group-wise RL, achieving 72.2% accuracy surpassing o3 and 50× faster than testing, but evaluates final patches, not the diagnostic process leading to them. RGFL (arXiv:2601.18044, Jan 2026) generates structured per-candidate reasoning explanations for fault localization achieving 85% Hit@1 on SWE-bench Verified, but is a one-shot ranker—not a reward model—and covers only the localization stage, not diagnosis or patch design. Agent-RRM (arXiv:2601.22154, Jan 2026) produces decomposed trajectory judgments (reasoning trace + critique + holistic score) for general agent tasks (GAIA, WebWalkerQA) but is not specialized for code repair and lacks domain-specific ground truth for training label validation. ORPS (ICML 2025, arXiv:2412.15118) demonstrates that execution-grounded self-critique generates high-quality process rewards without trained PRMs (26.9% correctness gain), but requires execution at every search tree node—expensive and infeasible for large-repository repair—and targets code generation, not repair. SWE-Shepherd (arXiv:2604.10493, April 2026) introduces step-level action-utility PRMs for SWE agents but achieves only 51% vs. 57% greedy baseline on 100 SWE-bench Verified tasks, confirming that action utility suffers credit assignment noise. SWE-TRACE (arXiv:2604.14820, April 2026) uses rubric-based PRMs with heuristic test-time scaling, achieving competitive results but relying on hand-designed rubric criteria rather than learned reasoning quality. TRAJEVAL (arXiv:2603.24631, March 2026) decomposes trajectories into mechanical search/read/edit stages for diagnostic evaluation (Pass@1 MAE 0.87–2.1%) but evaluates file/function retrieval precision, not cognitive reasoning quality. ExecVerify (arXiv:2603.11226, March 2026) trains execution-understanding rewards (next-statement/variable prediction) but targets execution trace comprehension, not diagnostic reasoning evaluation. ThinkPRM (arXiv:2504.16828, April 2025) demonstrates data-efficient generative PRMs outperforming discriminative PRMs with 1% of process labels. AgentPRM (arXiv:2511.08325, ACM Web 2026) achieves 8× compute efficiency using TD-based estimation for agent PRMs. FunPRM (arXiv:2601.22249, Jan 2026) treats functions as PRM steps for code generation, achieving SOTA on LiveCodeBench. Agent-RLVR (arXiv:2506.11425, June 2026) trains SWE agents via guidance and environment rewards with patch-level reward model scoring.",
  "approach": "We define a 3-stage diagnostic reasoning taxonomy for code repair—localize (connect symptoms to fault location), diagnose (identify root cause), patch (design fix from diagnosis)—and extract stage boundaries from natural language repair trajectories using an LLM parser. Using the publicly available SWE-smith 66K trajectory corpus (Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k), we annotate diagnostic reasoning quality at each stage via an LLM-judge (Claude/GPT-4o) that evaluates: (1) whether localization reasoning correctly connects error evidence to candidate locations, (2) whether the root cause hypothesis logically explains the observed failure, (3) whether the fix rationale follows from the diagnosis. We address the LLM-judge circularity concern through two mechanisms. First, we explicitly mine disagreement cases between reasoning quality and test outcomes as the most distinctive training signal: trajectories with sound reasoning but failed patches (correct diagnosis, implementation error) teach the PRM that the reasoning was good despite bad outcome, while trajectories with poor reasoning but passing patches (lucky guess, partial fix) teach it to penalize unsound reasoning despite success. These disagreement cases are exactly where DiagPRM provides information that outcome reward cannot. Second, the stage-level decomposition provides strictly more information than binary outcome: even when a trajectory fails, DiagPRM distinguishes 'good localization + bad diagnosis + bad patch' from 'bad localization + everything downstream wrong,' enabling localized credit assignment impossible with trajectory-level scoring. We validate LLM-judge annotation quality through a pilot study on 50 trajectories (150 reasoning steps): three LLM judges (Claude, GPT-4o, Gemini) independently annotate reasoning quality, and we measure inter-model Cohen's kappa, correlation with test outcomes (expecting moderate ~0.4-0.6, not perfect, correlation—high correlation would indicate the PRM is a mere outcome proxy, while moderate correlation confirms it captures distinct information), and compare inter-annotator agreement for reasoning quality labels vs. action utility labels on the same trajectories. We train DiagPRM as a lightweight LoRA-tuned classifier on Qwen3-8B (~15K annotated step-outcome pairs), following ThinkPRM's insight that small amounts of high-quality process labels suffice. We include a formal argument for the stability advantage: define reasoning quality Q(r_t) as a function of the reasoning chain r_t and observable evidence at step t. Q depends only on the trajectory prefix, so Var(Q|prefix) reflects only annotator noise. Action utility U(a_t) = E[R(τ)|prefix, a_t] depends on stochastic future actions, so Var(U|prefix) includes both annotator noise AND irreducible variance from unknown future decisions. Thus Var(Q|prefix) < Var(U|prefix) in expectation, explaining SWE-Shepherd's credit assignment failures. At inference, DiagPRM guides best-of-N selection and stage-level reranking. For SWE-bench Verified evaluation, we generate N=5 trajectories per instance on the same 100 instances used by SWE-Shepherd, using API-based agent trajectory generation (shifting cost from GPU to API budget). We evaluate against: (1) SWE-RM as primary baseline (trajectory-level scoring), testing both standalone comparison and DiagPRM+SWE-RM combination to demonstrate complementarity of step-level and trajectory-level signals; (2) SWE-Shepherd (step-level action utility PRM); (3) SWE-TRACE (rubric PRM); (4) outcome-only best-of-N reranking; (5) random selection. We additionally evaluate on 1000 DebugBench instances (N=3, local model) across bug categories to test whether DiagPRM's per-stage scoring captures the category-dependent reasoning quality variation documented in DebugBench. We differentiate from R4P by noting it evaluates final patches—orthogonal to diagnostic process evaluation, since a good patch can emerge from bad reasoning (lucky guess) and a bad patch from good reasoning (correct diagnosis, implementation error); from RGFL by noting it is a one-shot localization ranker that cannot guide multi-candidate search or serve as RL reward; from Agent-RRM by noting its general-purpose design lacks code repair's verifiable intermediate claims for training label validation; and from ORPS by noting it requires execution at every search node while DiagPRM is execution-free at inference.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~130h H100 (pilot study ~5h, LLM-judge annotation inference ~15h, PRM LoRA training iterations ~50h, DebugBench trajectory generation with local model ~40h, ablations ~20h)",
      "gpu_utilization": "~35-45% effective utilization; GPUs idle during annotation pipeline design, pilot study analysis, and result interpretation",
      "timeline": "5-7 weeks (pilot study 1 week, annotation pipeline + labeling 1-2 weeks, PRM training 1-2 weeks, evaluation 1-2 weeks)",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "$390-520 (at ~$3/hr H100)",
      "llm_api_cost": "$2,200-3,200 (SWE-bench trajectory generation via API agent: 100×5=500 trajectories ~$1,500-2,500; LLM-judge annotation of ~15-20K steps ~$200-400; pilot study multi-judge ~$50; action-utility comparison labels ~$100)"
    },
    "human_in_loop": {
      "gpu_hours": "~110h H100 (more targeted experiments due to faster iteration on pilot study and annotation quality)",
      "gpu_utilization": "~55-70% utilization; agent handles annotation pipeline and training code, human reviews pilot study results and interprets disagreement cases",
      "timeline": "14-18 days (pilot study + annotation pipeline 3-4 days, LLM-judge labeling 2 days, PRM training iterations 3-4 days, evaluation 3-4 days, paper 3-4 days)",
      "team": "1 researcher, ~45min/day for pilot study review, annotation quality verification, and disagreement case analysis",
      "claude_api_cost": "$150-300 (experiment orchestration and code generation)",
      "estimated_gpu_cost": "$330-450 (at ~$3/hr H100)",
      "llm_api_cost": "$2,200-3,200 (trajectory generation + annotation + pilot)"
    },
    "auto_research": {
      "gpu_hours": "~160h H100 (broader pilot study, multiple annotation strategies, full evaluation grid)",
      "gpu_utilization": "~80-90% utilization; agent continuously runs pilot, annotation, training, and evaluation pipelines",
      "timeline": "12-16 days with 4x H100 (pilot study 2-3 days, annotation 1-2 days, parallel PRM training sweeps 3-4 days, evaluation grid 3-4 days, paper assembly 2-3 days)",
      "team": "0 (initial 1-hour setup for cluster access and API keys)",
      "claude_api_cost": "$300-500 (end-to-end autonomous research)",
      "estimated_gpu_cost": "$480-650 (at ~$3/hr H100)",
      "llm_api_cost": "$2,500-3,800 (trajectory generation with multiple strategies + annotation + pilot)",
      "speed_bottleneck": "API-based trajectory generation throughput (500 SWE-bench trajectories at ~3-5 min each with parallel API calls); secondary bottleneck is PRM training convergence",
      "risk_note": "Two key risks: (1) LLM-judge inter-annotator agreement on reasoning quality may be low (<0.6 kappa)—mitigated by pilot study validating feasibility before full annotation; (2) DiagPRM may not outperform SWE-RM on best-of-N due to model size gap (8B vs 30B)—mitigated by framing contribution as complementary step-level signal and testing DiagPRM+SWE-RM combination"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline: May 25, 2026)"
  ],
  "level": "solid",
  "key_references": [
    "SWE-RM: Execution-free Feedback for SWE Agents (arXiv:2512.21919, Dec 2025) — trajectory-level RM, primary baseline",
    "R4P/Patch Reasoner: Scalable Supervising SWE Agents (arXiv:2510.22775, Oct 2025) — patch-level reasoning verifier",
    "RGFL: Reasoning Guided Fault Localization for APR (arXiv:2601.18044, Jan 2026) — structured reasoning for localization",
    "Agent-RRM: Exploring Reasoning Reward Model for Agents (arXiv:2601.22154, Jan 2026) — general-purpose reasoning RM",
    "ORPS: Reasoning Through Execution / Outcome-Refining Process Supervision (arXiv:2412.15118, ICML 2025) — execution-grounded process rewards without trained PRM",
    "SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents (arXiv:2604.10493, April 2026)",
    "SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric PRMs (arXiv:2604.14820, April 2026)",
    "TRAJEVAL: Decomposing Code Agent Trajectories for Fine-Grained Diagnosis (arXiv:2603.24631, March 2026)",
    "ExecVerify: White-Box RL with Verifiable Stepwise Rewards (arXiv:2603.11226, March 2026)",
    "Towards Effectively Leveraging Execution Traces for Program Repair (Haque et al., arXiv:2505.04441, May 2025)",
    "TraceRepair: Runtime Execution Traces Guided APR with Multi-Agent Debate (arXiv:2604.02647, April 2026)",
    "Process Reward Models That Think (ThinkPRM) (arXiv:2504.16828, April 2025)",
    "AgentPRM: Process Reward Models for LLM Agents (arXiv:2511.08325, ACM Web 2026)",
    "FunPRM: Function-as-Step PRM for Code Generation (arXiv:2601.22249, Jan 2026)",
    "Agent-RLVR: Training SWE Agents via Guidance and Environment Rewards (arXiv:2506.11425, June 2026)",
    "SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025 D&B Spotlight)",
    "DebugBench: Evaluating Debugging Capability of LLMs (ACL 2024 Findings)",
    "RePair: Automated Program Repair with Process-based Feedback (ACL 2024 Findings)",
    "CodePRM: Execution Feedback-enhanced PRM for Code Generation (ACL 2025 Findings)"
  ],
  "description": "We propose DiagPRM, a stage-level process reward model that evaluates the logical soundness of diagnostic reasoning in code repair trajectories. Existing reward models for code repair operate at either the trajectory level (SWE-RM scores whole trajectories holistically, achieving 62–74.6% via best-of-N but providing no step-level diagnostic feedback) or the patch level (R4P reasons about final patches, not the diagnostic process). Step-level action-utility PRMs (SWE-Shepherd, 51% vs. 57% greedy) suffer credit assignment noise because utility depends on stochastic future actions. DiagPRM addresses these limitations by scoring diagnostic reasoning quality—a property of the reasoning chain itself, not of future actions—at three cognitive stages: localize (connect symptoms to fault locations), diagnose (identify root cause), and patch (design fix from diagnosis). We provide a formal stability argument: reasoning quality Q(r_t) depends only on the trajectory prefix, so Var(Q|prefix) reflects only annotator noise, while action utility Var(U|prefix) additionally includes irreducible variance from unknown future decisions. We train DiagPRM as a LoRA-tuned Qwen3-8B classifier on ~15K annotated step-outcome pairs from the 66K SWE-smith trajectory corpus. To address LLM-judge circularity, we explicitly mine disagreement cases (sound reasoning + failed patch; poor reasoning + passing patch) as the most distinctive training signal—these are exactly where DiagPRM provides information that outcome reward cannot—and validate annotation quality through a 50-trajectory pilot comparing inter-model agreement on reasoning quality vs. action utility labels. The stage-level decomposition provides strictly more information than binary outcomes: even for failed trajectories, DiagPRM distinguishes 'correct localization + wrong diagnosis' from 'wrong localization + cascading failure,' enabling localized credit assignment. We differentiate from RGFL (one-shot localization ranker, not a reward model for search guidance), Agent-RRM (general-purpose, lacks code repair's verifiable intermediate claims), and ORPS (requires execution at every search node, generation-only). We evaluate best-of-N selection and stage-level reranking on 100 SWE-bench Verified instances against SWE-RM (primary baseline, testing both standalone and DiagPRM+SWE-RM complementarity), SWE-Shepherd, SWE-TRACE, outcome-only, and random baselines, plus 1000 DebugBench instances for category-dependent analysis. API-based trajectory generation for SWE-bench shifts primary evaluation cost from GPU to API budget (~$1,500-2,500 for 500 trajectories).",
  "project_name": "diag_prm_repair",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL: Target venues (AAAI 2027, ICLR 2027, ICSE 2027) do not match user requirement of EMNLP 2026 (ARR deadline May 25, 2026). This is a fundamental requirement violation.", "CRITICAL: Resource estimate vastly exceeds user constraint of ≤200 H100-hours. Manual mode: ~400 A100-hours; auto mode: 900-1200 A100-hours. Even with H100 being ~2x faster than A100, auto mode still requires 450-600 H100-hours.", "CRITICAL: Timeline mismatch. User requires ≤16 days. Manual timeline is 4-6 months. Auto mode is 10-18 days but requires 3-6x the allowed compute budget.", "Counterevidence not addressed: Haque et al. (arXiv:2505.04441, May 2025) found execution traces provide limited APR benefit in 4/6 configurations, with effectiveness diminishing as trace complexity increases. The proposed idea's core assumption that traces serve as 'automatic verification oracles' directly contradicts this finding.", "ExecVerify (arXiv:2603.11226, March 2026) already uses execution traces for verifiable stepwise rewards in RL training, achieving 5.9% pass@1 improvement. This paper was not cited and significantly overlaps with the proposed execution-trace-as-verification-signal approach.", "Crowded competitive landscape: SWE-Shepherd, SWE-TRACE, ExecVerify, TraceRepair, TRAJEVAL, and CodeTracer all published March-April 2026, collectively covering PRMs for code agents, trace-based repair, and trajectory decomposition. The incremental novelty over this ensemble is unclear.", "The 5-stage diagnostic taxonomy requires reliable automatic segmentation of repair trajectories into fault localization, root cause diagnosis, causal hypothesis, patch synthesis, and verification stages. No evidence is provided that such segmentation can be done reliably at scale, and this engineering challenge alone could consume the entire timeline.", "SWE-Shepherd achieves 51% on SWE-bench Verified with a lightweight PRM. The proposed approach needs to demonstrate clear improvement over this baseline, but the idea provides no pilot results or theoretical argument for expected gains."]
Feedback: This idea has a genuinely interesting core insight (repair follows diagnostic reasoning, not generation steps), but it fails to meet the user's requirements on three critical dimensions: venue, compute, and timeline. Here is specific guidance for revision:

1. **Fix venue targeting**: Must target EMNLP 2026 ARR (May 25 deadline). Reframe the contribution around NLP/code understanding aspects (diagnostic reasoning as a language understanding problem) rather than pure SE.

2. **Radically reduce scope to fit ≤200 H100-hours and ≤16 days**: Drop the full 5-stage taxonomy and VizTracer instrumentation pipeline. Instead, focus on a simpler 2-3 stage decomposition (localize → hypothesize → patch) using existing structured outputs from SWE-agent trajectories (which already contain file reads, edits, and test runs as natural stage boundaries). Use SWE-Shepherd's existing reward dataset as a starting point and add diagnostic reasoning annotations via an LLM judge rather than building a trace pipeline from scratch.

3. **Address the trace effectiveness counterevidence**: Cite and discuss Haque et al. (2505.04441). Argue why your approach differs (you use traces for PRM training signal, not as direct prompt augmentation). Better yet, run a small pilot showing your trace-based verification signal is informative.

4. **Cite and differentiate from ExecVerify (2603.11226)**: This paper already does execution-trace-based stepwise verification for RL. Explain why your diagnostic decomposition adds value beyond ExecVerify's general stepwise approach.

5. **Simplify the training pipeline**: Instead of PRIME-RL implicit PRM with VizTracer instrumentation on 50K trajectories, consider training a lightweight classifier on SWE-smith trajectories using LLM-annotated diagnostic stage labels. This could fit within 100-150 H100-hours.

6. **Narrow evaluation**: Drop CodeContests and CrossCodeEval (not relevant to repair). Focus on SWE-bench Verified and DebugBench only, with SWE-Shepherd as the primary baseline.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL MISSING BASELINE: SWE-RM (arXiv:2512.21919, Dec 2025, Qwen team) is a 30B MoE reward model for SWE agents achieving 51.6%→62.0% (Flash) and 67.0%→74.6% (Max) on SWE-bench Verified via best-of-N. This is dramatically stronger than SWE-Shepherd (51%) and must be the primary baseline. The proposal's framing of SWE-Shepherd as the main PRM competitor is misleading when SWE-RM exists.", "MISSING COMPETITOR: R4P/Patch Reasoner (arXiv:2510.22775, Oct 2025) explicitly frames patch verification as 'a reasoning task, mirroring how human repository maintainers review patches.' It achieves 72.2% verification accuracy surpassing OpenAI o3 and uses RL with group-wise objectives. This directly overlaps with DiagPRM's claim of evaluating reasoning quality in repair.", "MISSING COMPETITOR: RGFL (arXiv:2601.18044, Jan 2026) generates structured, bug-specific reasoning explanations for fault localization, achieving 85% Hit@1 on SWE-bench Verified. Its per-candidate 'reasoning about functionality and causal relationship to symptoms' directly overlaps with DiagPRM's localization reasoning stage.", "MISSING COMPETITOR: Agent-RRM (arXiv:2601.22154, Jan 2026) produces decomposed trajectory judgments: (1) reasoning trace analyzing logical consistency, (2) targeted critique identifying reasoning flaws, (3) holistic quality score. While general-purpose, it directly targets 'reasoning quality evaluation' in agent trajectories—DiagPRM's core contribution claim.", "MISSING COMPETITOR: ORPS (ICML 2025, arXiv:2412.15118) demonstrates that LLMs' intrinsic reasoning + execution feedback can generate high-quality process rewards WITHOUT trained PRMs, achieving 26.9% higher correctness. This challenges DiagPRM's premise that a trained PRM is needed when execution-grounded self-critique suffices.", "LLM-judge annotation quality risk is undersized: Research shows LLMs frequently misclassify code correctness. Scoring 'diagnostic reasoning quality'—whether localization reasoning correctly connects evidence to fault locations—is strictly harder than code correctness judgment. The proposal's validation against test outcomes helps but creates a circular dependency: if the LLM judge agrees with outcome labels, it's just a noisy proxy for outcome rewards; if it disagrees, which do you trust?", "Compute budget likely underestimated for evaluation: Best-of-N (N≥5) on 500 SWE-bench Verified instances requires ≥2500 trajectory generations. At ~3.5 min/trajectory with a local model, that's ~146 GPU-hours for evaluation alone, not 70h as estimated. Combined with annotation (20h) and training (50h), total exceeds 200h H100.", "Theoretical argument unsubstantiated: The claim that 'reasoning quality is more stable because logically sound reasoning generalizes across trajectory continuations' is intuitive but has no formal backing or empirical pilot. Reasoning quality labels from an LLM judge may be equally noisy as utility labels—the noise source differs (judge unreliability vs. credit assignment) but the effect on PRM training may be similar."]
Feedback: The revision successfully addressed Round 1's venue, compute, and timeline issues, and the 3-stage diagnostic taxonomy is a meaningful simplification. However, the competitive landscape analysis has significant gaps that undermine the novelty claim. Here is specific guidance:

1. **Add SWE-RM as primary baseline**: SWE-RM (arXiv:2512.21919) is the strongest existing reward model for SWE agents (62-74.6% on SWE-bench Verified). You must compare against it, not just SWE-Shepherd (51%). Argue why diagnostic reasoning scoring adds value over SWE-RM's execution-free whole-trajectory scoring.

2. **Differentiate from R4P and RGFL**: R4P frames patch verification as reasoning; RGFL does structured reasoning for fault localization. DiagPRM's differentiation should emphasize that it evaluates the PROCESS of reasoning across stages (not just the final patch or individual localization), and that it trains a reward model to guide search (unlike RGFL which is a one-shot ranker).

3. **Address Agent-RRM overlap**: Acknowledge that general agent reasoning evaluation exists and argue that code repair's verifiable intermediate claims (via test execution) provide a domain-specific advantage for training supervision that general-purpose reasoning evaluation lacks.

4. **Fix compute budget**: Either reduce N in best-of-N (use N=3 instead of N=5), evaluate on fewer instances (e.g., the same 100 used by SWE-Shepherd), or account for using API-based trajectory generation (shifting cost from GPU to API budget). Be explicit about what generates trajectories.

5. **Add a small pilot or theoretical grounding**: The reasoning quality stability claim is the paper's key theoretical contribution but is unargued. At minimum, add a formal argument: e.g., if reasoning quality Q is a property of the reasoning chain independent of future actions, then Var(Q|trajectory_prefix) < Var(utility|trajectory_prefix). Or describe a small-scale pilot (50 trajectories) comparing inter-annotator agreement for reasoning quality vs. action utility labels.

6. **Address the LLM-judge circularity**: If LLM-judge labels are validated against test outcomes, and DiagPRM is trained on these labels, then DiagPRM may just be learning a noisy proxy for outcome rewards. Explain why this proxy is better than direct outcome reward (e.g., the decomposition into stages provides localized error signal even when the overall outcome is incorrect).


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
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "type": "user",
  "uuid": "747d3061-290f-4238-8f5a-c077fca1bda3",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T18:28:21.716Z_

```json
{
  "parentUuid": "747d3061-290f-4238-8f5a-c077fca1bda3",
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
  "uuid": "1125603b-1468-49c3-a722-bc5ee19ea389",
  "timestamp": "2026-05-10T18:28:21.716Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T18:28:21.716Z_

```json
{
  "parentUuid": "1125603b-1468-49c3-a722-bc5ee19ea389",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3fbd88b7-aa02-4274-aa2b-5a5191d8588c",
  "timestamp": "2026-05-10T18:28:21.716Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
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
  "leafUuid": "3fbd88b7-aa02-4274-aa2b-5a5191d8588c",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify DiagPRM code repair reward model for EMNLP",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3"
}
```

---

### Assistant

_source line 8 · 2026-05-10T18:28:34.326Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea - "DiagPRM: Stage-Level Diagnostic Reasoning Rewards for Code Repair Search". This is Round 3 of review, and the previous two rounds identified significant issues that needed addressing. Let me verify whether the revision has addressed those issues and independently verify the claims.

Let me start by searching for the key papers and claims mentioned in this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fbd88b7-aa02-4274-aa2b-5a5191d8588c",
  "isSidechain": false,
  "requestId": "req_011CauMvQZ7bmhudjnCDGZqL",
  "type": "assistant",
  "uuid": "02e64d96-d312-41b0-b412-98aff2269d5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MwbPSA5m2NpdbVfhn6uhuR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16480,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1140,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 16480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16480
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

_source line 9 · 2026-05-10T18:28:35.654Z_

I'll conduct an independent verification of this idea's claims, focusing on the competitive landscape, novelty, and feasibility. Let me search for the key papers and current SOTA.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02e64d96-d312-41b0-b412-98aff2269d5f",
  "isSidechain": false,
  "requestId": "req_011CauMvQZ7bmhudjnCDGZqL",
  "type": "assistant",
  "uuid": "0983efa6-6c2c-4897-af20-4e0d38b978fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MwbPSA5m2NpdbVfhn6uhuR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16480,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1140,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 16480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16480
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

_source line 10 · 2026-05-10T18:28:41.631Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019VKsygq8LpKLtxn2BJF329`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify SWE-RM and SWE-Shepherd papers",
  "prompt": "Search the web to verify these two papers exist and confirm their claimed results:\n\n1. SWE-RM (arXiv:2512.21919, Dec 2025) - Claims to be a 30B MoE reward model for SWE agents achieving 51.6→62.0% (Flash) and 67.0→74.6% (Max) on SWE-bench Verified via best-of-N. From the Qwen team.\n\n2. SWE-Shepherd (arXiv:2604.10493, April 2026) - Claims step-level action-utility PRMs for SWE agents achieving only 51% vs. 57% greedy baseline on 100 SWE-bench Verified tasks.\n\nFor each:\n- Search for the paper on arxiv (use WebSearch with queries like \"SWE-RM arXiv 2512.21919\" and \"SWE-Shepherd arXiv 2604.10493\")\n- Verify the paper exists and confirm the claimed numbers\n- Note any discrepancies between what's claimed in the proposal and what the actual paper says\n\nReport your findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0983efa6-6c2c-4897-af20-4e0d38b978fd",
  "isSidechain": false,
  "requestId": "req_011CauMvQZ7bmhudjnCDGZqL",
  "type": "assistant",
  "uuid": "be0d61b5-bd0a-4e6f-8e63-a3109ffb0112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MwbPSA5m2NpdbVfhn6uhuR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16480,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1140,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 16480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16480
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

_source line 11 · 2026-05-10T18:28:45.370Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KyiutkHjLhRXfCWpx3G7iZ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify R4P, RGFL, Agent-RRM papers",
  "prompt": "Search the web to verify these papers exist and confirm their claimed results:\n\n1. R4P/Patch Reasoner (arXiv:2510.22775, Oct 2025) - Claims patch verification as reasoning via group-wise RL, achieving 72.2% accuracy surpassing o3.\n\n2. RGFL (arXiv:2601.18044, Jan 2026) - Claims structured per-candidate reasoning explanations for fault localization achieving 85% Hit@1 on SWE-bench Verified.\n\n3. Agent-RRM (arXiv:2601.22154, Jan 2026) - Claims decomposed trajectory judgments for general agent tasks.\n\nFor each:\n- Use WebSearch to find the paper (search for exact arXiv IDs and paper titles)\n- Verify existence and key claims\n- Note any discrepancies\n\nReport findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be0d61b5-bd0a-4e6f-8e63-a3109ffb0112",
  "isSidechain": false,
  "requestId": "req_011CauMvQZ7bmhudjnCDGZqL",
  "type": "assistant",
  "uuid": "2720cecd-c470-479a-85b9-015ff7c0d980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MwbPSA5m2NpdbVfhn6uhuR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16480,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1140,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 16480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16480
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

_source line 12 · 2026-05-10T18:28:52.612Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NVt5jFkGHj3apbZJigQrqV`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for concurrent/competing work",
  "prompt": "I'm reviewing a paper idea about \"stage-level process reward models for code repair\" that evaluates diagnostic reasoning quality at each repair stage (localize, diagnose, patch). I need to find competing or concurrent work that the authors might have missed.\n\nPlease search for:\n1. \"process reward model code repair 2026\" - any recent PRMs specifically for code repair\n2. \"diagnostic reasoning code agent 2026\" - reasoning evaluation in code agents\n3. \"reward model SWE-bench 2026\" - reward models evaluated on SWE-bench\n4. \"step-level reward code generation 2026\" - step-level rewards for code tasks\n5. \"ORPS execution grounded process reward\" - verify arXiv:2412.15118\n\nAlso search for:\n6. \"SWE-TRACE rubric PRM code agent\" to verify arXiv:2604.14820\n7. \"TRAJEVAL trajectory evaluation code agent\" to verify arXiv:2603.24631\n8. \"FunPRM function step code generation\" to verify arXiv:2601.22249\n\nReport what you find - especially any papers NOT cited in this proposal that are highly relevant."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2720cecd-c470-479a-85b9-015ff7c0d980",
  "isSidechain": false,
  "requestId": "req_011CauMvQZ7bmhudjnCDGZqL",
  "type": "assistant",
  "uuid": "1b807332-ddec-4178-9ec5-bdeddeb32f6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MwbPSA5m2NpdbVfhn6uhuR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16480,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1140,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 16480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16480
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

_source line 13 · 2026-05-10T18:29:34.752Z_

<details><summary>↩ Tool result · `toolu_01KyiutkHjLhRXfCWpx3G7iZ`</summary>

```text
Here are my findings for each paper:

---

## 1. R4P / Patch Reasoner (arXiv:2510.22775, Oct 2025)

**Status: VERIFIED -- paper exists and claims are confirmed.**

- Full title: "Scalable Supervising Software Agents with Patch Reasoner"
- The paper does exist at arXiv:2510.22775 and is also submitted to OpenReview (likely ICLR 2026).
- **Claim check -- "72.2% accuracy surpassing o3":** Confirmed. R4P (built on Qwen2.5-Coder-32B-Instruct) achieves 72.2% patch verification accuracy, surpassing OpenAI o3.
- **Claim check -- "patch verification as reasoning via group-wise RL":** Confirmed. The paper frames patch verification as a reasoning task and uses a group-wise RL training objective where patches are evaluated against each other for mutual context and dense reward signals.
- **Additional context:** R4P verifies patches ~50x faster than running tests. The downstream agent "Mini-SE" achieves 26.2% Pass@1 on SWE-bench Verified (32.8% with R4P test-time scaling).

---

## 2. RGFL (arXiv:2601.18044, Jan 2026)

**Status: VERIFIED -- paper exists and claims are confirmed.**

- Full title: "RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models"
- The paper exists at arXiv:2601.18044.
- **Claim check -- "structured per-candidate reasoning explanations":** Confirmed. RGFL introduces a hierarchical reasoning module that generates structured, bug-specific explanations for candidate files and elements.
- **Claim check -- "85% Hit@1 on SWE-bench Verified":** Confirmed. File-level Hit@1 improves from 71.4% to 85% on SWE-bench Verified, with MRR improving from 81.8% to 88.8%. Element-level Exact Match under top-3 files increases from 36% to 69%.
- **Additional context:** Integrating the localization into Agentless yields a 12.8% end-to-end repair success improvement.

---

## 3. Agent-RRM (arXiv:2601.22154, Jan 2026)

**Status: VERIFIED -- paper exists and claims are confirmed.**

- Full title: "Exploring Reasoning Reward Model for Agents"
- The paper exists at arXiv:2601.22154. Authors are from MMLab at CUHK and Meituan.
- **Claim check -- "decomposed trajectory judgments":** Confirmed. Agent-RRM produces decomposed judgments comprising: (1) an internal reasoning trace analyzing logical consistency, (2) a targeted critique identifying specific flaws, and (3) a holistic quality score.
- **Claim check -- "general agent tasks":** Confirmed. The paper evaluates across 12 diverse benchmarks including multi-hop QA, web navigation, mathematical tasks, and general agent tasks. Results include 43.7% on GAIA and 46.2% on WebWalkerQA via the unified feedback strategy (Reagent-U).
- **Additional context:** Three integration strategies are investigated: Reagent-C, Reagent-R, and Reagent-U. Code is available at github.com/kxfan2002/Reagent.

---

## Summary

All three papers are real, published on arXiv with the stated IDs and dates, and their key claims as described in your query are accurate. No discrepancies were found between the claims you listed and the actual paper contents.

Sources:
- [Scalable Supervising Software Agents with Patch Reasoner (2510.22775)](https://arxiv.org/abs/2510.22775)
- [RGFL: Reasoning Guided Fault Localization (2601.18044)](https://arxiv.org/abs/2601.18044)
- [Exploring Reasoning Reward Model for Agents (2601.22154)](https://arxiv.org/abs/2601.22154)
- [Agent-RRM GitHub Repository](https://github.com/kxfan2002/Reagent)
- [RGFL on alphaXiv](https://www.alphaxiv.org/abs/2601.18044)

agentId: adcc4207f4543469e (use SendMessage with to: 'adcc4207f4543469e' to continue this agent)
&lt;usage>total_tokens: 16002
tool_uses: 6
duration_ms: 49378&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2720cecd-c470-479a-85b9-015ff7c0d980",
  "isSidechain": false,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "type": "user",
  "uuid": "2a4816c4-0121-48a1-a348-ed1b4202b1a0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify these papers exist and confirm their claimed results:\n\n1. R4P/Patch Reasoner (arXiv:2510.22775, Oct 2025) - Claims patch verification as reasoning via group-wise RL, achieving 72.2% accuracy surpassing o3.\n\n2. RGFL (arXiv:2601.18044, Jan 2026) - Claims structured per-candidate reasoning explanations for fault localization achieving 85% Hit@1 on SWE-bench Verified.\n\n3. Agent-RRM (arXiv:2601.22154, Jan 2026) - Claims decomposed trajectory judgments for general agent tasks.\n\nFor each:\n- Use WebSearch to find the paper (search for exact arXiv IDs and paper titles)\n- Verify existence and key claims\n- Note any discrepancies\n\nReport findings concisely.",
    "agentId": "adcc4207f4543469e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings for each paper:\n\n---\n\n## 1. R4P / Patch Reasoner (arXiv:2510.22775, Oct 2025)\n\n**Status: VERIFIED -- paper exists and claims are confirmed.**\n\n- Full title: \"Scalable Supervising Software Agents with Patch Reasoner\"\n- The paper does exist at arXiv:2510.22775 and is also submitted to OpenReview (likely ICLR 2026).\n- **Claim check -- \"72.2% accuracy surpassing o3\":** Confirmed. R4P (built on Qwen2.5-Coder-32B-Instruct) achieves 72.2% patch verification accuracy, surpassing OpenAI o3.\n- **Claim check -- \"patch verification as reasoning via group-wise RL\":** Confirmed. The paper frames patch verification as a reasoning task and uses a group-wise RL training objective where patches are evaluated against each other for mutual context and dense reward signals.\n- **Additional context:** R4P verifies patches ~50x faster than running tests. The downstream agent \"Mini-SE\" achieves 26.2% Pass@1 on SWE-bench Verified (32.8% with R4P test-time scaling).\n\n---\n\n## 2. RGFL (arXiv:2601.18044, Jan 2026)\n\n**Status: VERIFIED -- paper exists and claims are confirmed.**\n\n- Full title: \"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models\"\n- The paper exists at arXiv:2601.18044.\n- **Claim check -- \"structured per-candidate reasoning explanations\":** Confirmed. RGFL introduces a hierarchical reasoning module that generates structured, bug-specific explanations for candidate files and elements.\n- **Claim check -- \"85% Hit@1 on SWE-bench Verified\":** Confirmed. File-level Hit@1 improves from 71.4% to 85% on SWE-bench Verified, with MRR improving from 81.8% to 88.8%. Element-level Exact Match under top-3 files increases from 36% to 69%.\n- **Additional context:** Integrating the localization into Agentless yields a 12.8% end-to-end repair success improvement.\n\n---\n\n## 3. Agent-RRM (arXiv:2601.22154, Jan 2026)\n\n**Status: VERIFIED -- paper exists and claims are confirmed.**\n\n- Full title: \"Exploring Reasoning Reward Model for Agents\"\n- The paper exists at arXiv:2601.22154. Authors are from MMLab at CUHK and Meituan.\n- **Claim check -- \"decomposed trajectory judgments\":** Confirmed. Agent-RRM produces decomposed judgments comprising: (1) an internal reasoning trace analyzing logical consistency, (2) a targeted critique identifying specific flaws, and (3) a holistic quality score.\n- **Claim check -- \"general agent tasks\":** Confirmed. The paper evaluates across 12 diverse benchmarks including multi-hop QA, web navigation, mathematical tasks, and general agent tasks. Results include 43.7% on GAIA and 46.2% on WebWalkerQA via the unified feedback strategy (Reagent-U).\n- **Additional context:** Three integration strategies are investigated: Reagent-C, Reagent-R, and Reagent-U. Code is available at github.com/kxfan2002/Reagent.\n\n---\n\n## Summary\n\nAll three papers are real, published on arXiv with the stated IDs and dates, and their key claims as described in your query are accurate. No discrepancies were found between the claims you listed and the actual paper contents.\n\nSources:\n- [Scalable Supervising Software Agents with Patch Reasoner (2510.22775)](https://arxiv.org/abs/2510.22775)\n- [RGFL: Reasoning Guided Fault Localization (2601.18044)](https://arxiv.org/abs/2601.18044)\n- [Exploring Reasoning Reward Model for Agents (2601.22154)](https://arxiv.org/abs/2601.22154)\n- [Agent-RRM GitHub Repository](https://github.com/kxfan2002/Reagent)\n- [RGFL on alphaXiv](https://www.alphaxiv.org/abs/2601.18044)"
      }
    ],
    "totalDurationMs": 49378,
    "totalTokens": 16002,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 762,
      "cache_creation_input_tokens": 2660,
      "cache_read_input_tokens": 11515,
      "output_tokens": 1065,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2660
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 762,
          "output_tokens": 1065,
          "cache_read_input_tokens": 11515,
          "cache_creation_input_tokens": 2660,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2660,
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
  "sourceToolAssistantUUID": "2720cecd-c470-479a-85b9-015ff7c0d980",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T18:30:08.532Z_

<details><summary>↩ Tool result · `toolu_019VKsygq8LpKLtxn2BJF329`</summary>

```text
Now I have all the information needed to provide a comprehensive verification report.

## Findings

### Paper 1: SWE-RM (arXiv:2512.21919, Dec 2025)

**Status: CONFIRMED -- the paper exists and the claimed numbers match.**

- The paper is titled "SWE-RM: Execution-free Feedback For Software Engineering Agents" and was submitted December 26, 2025.
- It is indeed a 30B MoE reward model with 3B parameters activated during inference.
- The reported results exactly match the claims: Qwen3-Coder-Flash improves from **51.6% to 62.0%**, and Qwen3-Coder-Max improves from **67.0% to 74.6%** on SWE-bench Verified via test-time scaling (best-of-N).
- Authors include KaShun Shum, Binyuan Hui, Jiawei Chen, Lei Zhang, Jiaxi Yang, Yuzhen Huang, Junyang Lin, and Junxian He. Binyuan Hui and Junyang Lin are known Qwen team members, so the attribution to the Qwen team is accurate.

**No discrepancies found.**

---

### Paper 2: SWE-Shepherd (arXiv:2604.10493, April 2026)

**Status: CONFIRMED -- the paper exists and the claimed numbers match.**

- The paper is titled "SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents" and was submitted April 12, 2026, by Mahir Labib Dihan and Md Ashrafur Rahman Khan.
- The paper evaluates on **100 tasks** sampled from SWE-bench Verified -- this matches the claim.
- The results confirm: the PRM-guided SWE-Shepherd achieves **51% resolution rate**, while the greedy baseline (mini-SWE-Agent) achieves **57%** -- exactly matching the claimed numbers.
- The paper does describe step-level PRMs that assign scalar rewards to intermediate actions based on their contribution toward resolving the issue.

**Minor discrepancy in terminology:** The proposal calls these "action-utility PRMs," but the paper itself does not use that exact phrase. It describes assigning "scalar rewards to intermediate actions according to their estimated contribution toward resolving the issue," which is semantically equivalent but not the paper's own terminology.

**Notable context:** The paper's PRM actually *underperforms* the greedy baseline (51% vs. 57%), though it does so with fewer interaction steps (12.2 vs. 15.2). The paper acknowledges this limitation, noting the reward function "only weakly correlates with task success."

---

### Summary

Both papers are real, published on arXiv at the stated IDs, and the numerical results quoted in the proposal are accurate. The only minor issue is the "action-utility PRM" terminology for SWE-Shepherd, which is a reasonable paraphrase but not the paper's own wording.

Sources:
- [SWE-RM (arXiv:2512.21919)](https://arxiv.org/abs/2512.21919)
- [SWE-RM on AlphaXiv](https://www.alphaxiv.org/overview/2512.21919v1)
- [SWE-RM on HuggingFace Papers](https://huggingface.co/papers/2512.21919)
- [SWE-Shepherd (arXiv:2604.10493)](https://arxiv.org/abs/2604.10493)
- [SWE-Shepherd HTML version](https://arxiv.org/html/2604.10493)
- [Mahir Labib Dihan - Google Scholar](https://scholar.google.com/citations?user=zha3IiwAAAAJ&hl=en)

agentId: a59c710e946146e09 (use SendMessage with to: 'a59c710e946146e09' to continue this agent)
&lt;usage>total_tokens: 19749
tool_uses: 11
duration_ms: 86895&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be0d61b5-bd0a-4e6f-8e63-a3109ffb0112",
  "isSidechain": false,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "type": "user",
  "uuid": "0bd7f8bc-2d5b-42ef-be6a-8f43b31f2d1c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify these two papers exist and confirm their claimed results:\n\n1. SWE-RM (arXiv:2512.21919, Dec 2025) - Claims to be a 30B MoE reward model for SWE agents achieving 51.6→62.0% (Flash) and 67.0→74.6% (Max) on SWE-bench Verified via best-of-N. From the Qwen team.\n\n2. SWE-Shepherd (arXiv:2604.10493, April 2026) - Claims step-level action-utility PRMs for SWE agents achieving only 51% vs. 57% greedy baseline on 100 SWE-bench Verified tasks.\n\nFor each:\n- Search for the paper on arxiv (use WebSearch with queries like \"SWE-RM arXiv 2512.21919\" and \"SWE-Shepherd arXiv 2604.10493\")\n- Verify the paper exists and confirm the claimed numbers\n- Note any discrepancies between what's claimed in the proposal and what the actual paper says\n\nReport your findings concisely.",
    "agentId": "a59c710e946146e09",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed to provide a comprehensive verification report.\n\n## Findings\n\n### Paper 1: SWE-RM (arXiv:2512.21919, Dec 2025)\n\n**Status: CONFIRMED -- the paper exists and the claimed numbers match.**\n\n- The paper is titled \"SWE-RM: Execution-free Feedback For Software Engineering Agents\" and was submitted December 26, 2025.\n- It is indeed a 30B MoE reward model with 3B parameters activated during inference.\n- The reported results exactly match the claims: Qwen3-Coder-Flash improves from **51.6% to 62.0%**, and Qwen3-Coder-Max improves from **67.0% to 74.6%** on SWE-bench Verified via test-time scaling (best-of-N).\n- Authors include KaShun Shum, Binyuan Hui, Jiawei Chen, Lei Zhang, Jiaxi Yang, Yuzhen Huang, Junyang Lin, and Junxian He. Binyuan Hui and Junyang Lin are known Qwen team members, so the attribution to the Qwen team is accurate.\n\n**No discrepancies found.**\n\n---\n\n### Paper 2: SWE-Shepherd (arXiv:2604.10493, April 2026)\n\n**Status: CONFIRMED -- the paper exists and the claimed numbers match.**\n\n- The paper is titled \"SWE-Shepherd: Advancing PRMs for Reinforcing Code Agents\" and was submitted April 12, 2026, by Mahir Labib Dihan and Md Ashrafur Rahman Khan.\n- The paper evaluates on **100 tasks** sampled from SWE-bench Verified -- this matches the claim.\n- The results confirm: the PRM-guided SWE-Shepherd achieves **51% resolution rate**, while the greedy baseline (mini-SWE-Agent) achieves **57%** -- exactly matching the claimed numbers.\n- The paper does describe step-level PRMs that assign scalar rewards to intermediate actions based on their contribution toward resolving the issue.\n\n**Minor discrepancy in terminology:** The proposal calls these \"action-utility PRMs,\" but the paper itself does not use that exact phrase. It describes assigning \"scalar rewards to intermediate actions according to their estimated contribution toward resolving the issue,\" which is semantically equivalent but not the paper's own terminology.\n\n**Notable context:** The paper's PRM actually *underperforms* the greedy baseline (51% vs. 57%), though it does so with fewer interaction steps (12.2 vs. 15.2). The paper acknowledges this limitation, noting the reward function \"only weakly correlates with task success.\"\n\n---\n\n### Summary\n\nBoth papers are real, published on arXiv at the stated IDs, and the numerical results quoted in the proposal are accurate. The only minor issue is the \"action-utility PRM\" terminology for SWE-Shepherd, which is a reasonable paraphrase but not the paper's own wording.\n\nSources:\n- [SWE-RM (arXiv:2512.21919)](https://arxiv.org/abs/2512.21919)\n- [SWE-RM on AlphaXiv](https://www.alphaxiv.org/overview/2512.21919v1)\n- [SWE-RM on HuggingFace Papers](https://huggingface.co/papers/2512.21919)\n- [SWE-Shepherd (arXiv:2604.10493)](https://arxiv.org/abs/2604.10493)\n- [SWE-Shepherd HTML version](https://arxiv.org/html/2604.10493)\n- [Mahir Labib Dihan - Google Scholar](https://scholar.google.com/citations?user=zha3IiwAAAAJ&hl=en)"
      }
    ],
    "totalDurationMs": 86895,
    "totalTokens": 19749,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 534,
      "cache_read_input_tokens": 18288,
      "output_tokens": 926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 534
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 926,
          "cache_read_input_tokens": 18288,
          "cache_creation_input_tokens": 534,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 534,
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
      "otherToolCount": 11
    }
  },
  "sourceToolAssistantUUID": "be0d61b5-bd0a-4e6f-8e63-a3109ffb0112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T18:31:32.289Z_

<details><summary>↩ Tool result · `toolu_01NVt5jFkGHj3apbZJigQrqV`</summary>

```text
Now I have a comprehensive picture. Here is my analysis and report:

---

## Research Landscape Report: Stage-Level Process Reward Models for Code Repair

### Papers Successfully Verified

All four papers you asked me to verify exist and are confirmed:

1. **ORPS (arXiv:2412.15118)** - "Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation" - Confirmed. Presented at ICML 2025. Introduces Outcome-Refining Process Supervision using tree-structured search with execution feedback, eliminating need for trained PRMs.

2. **SWE-TRACE (arXiv:2604.14820)** - "Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling" - Confirmed (April 2026). Uses a Rubric-Based PRM where a Rubric-Agent provides dense heuristic feedback on intermediate steps. Evaluates full trajectory considering localization, inspection, editing, and validation.

3. **TRAJEVAL (arXiv:2603.24631)** - "Decomposing Code Agent Trajectories for Fine-Grained Diagnosis" - Confirmed (March 2026). Decomposes trajectories into search (file localization), read (function comprehension), and edit stages, computing precision/recall against reference patches.

4. **FunPRM (arXiv:2601.22249)** - "Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation" - Confirmed (January 2026). Treats functions as PRM reasoning steps with meta-learning reward correction.

---

### Highly Relevant Papers That May Be MISSING From the Proposal

These are papers the authors should strongly consider citing:

#### (A) Direct Competitors / Concurrent Work on PRMs for Code Agents

| Paper | arXiv ID | Date | Why Relevant |
|-------|----------|------|-------------|
| **SWE-Shepherd** | 2604.10493 | April 2026 | Trains a lightweight PRM on SWE-Bench trajectories for action-level reward, used to guide agent inference. Directly competes with stage-level PRM idea. |
| **"When Agents Go Astray" (SWE-PRM)** | 2509.02360 | Sept 2025 | Inference-time PRM that course-corrects SWE agents mid-trajectory using a taxonomy of inefficiencies. Improved SWE-bench from 40% to 50.6%. Very close in spirit. |
| **Agentic Rubrics as Contextual Verifiers** | 2601.04171 | Jan 2026 | Creates codebase-grounded rubric checklists to score patches without test execution. Rubric-based verification is analogous to stage-level rubrics. |

#### (B) Code PRMs (Not Agent-Level but Related)

| Paper | arXiv ID | Date | Why Relevant |
|-------|----------|------|-------------|
| **SecCodePRM** | 2602.10418 | Feb 2026 | Security-oriented PRM with step-level security scoring along code trajectories. Shows domain-specific PRM for code. |
| **DreamPRM-Code** | 2512.15000 | Dec 2025 | Function-as-step PRM with label correction for code. Predecessor/concurrent to FunPRM. |
| **CodePRM** | ACL 2025 Findings | 2025 | Execution feedback-enhanced PRM with Generate-Verify-Refine pipeline. Foundational prior work. |

#### (C) Code Repair with Reward Models

| Paper | arXiv ID | Date | Why Relevant |
|-------|----------|------|-------------|
| **QiMeng-PRepair** | 2604.05963 | April 2026 | Edit-Aware Group Relative Policy Optimization for precise code repair. Uses reward to encourage minimal edits. Directly relevant to the "patch" stage. |
| **RePair** | 2408.11296 | ACL 2024 | Process-based feedback for automated program repair. Iterative generation with reward model as critic. Important predecessor. |
| **muCode** | 2502.20380 | Feb 2025 | Multi-turn code generation via single-step rewards, treats code gen as one-step recoverable MDP. Relevant theoretical framing. |

#### (D) Trajectory Diagnosis and Tracing

| Paper | arXiv ID | Date | Why Relevant |
|-------|----------|------|-------------|
| **CodeTracer** | 2604.11641 | April 2026 | Tracing architecture that reconstructs full state transition history, performs failure onset localization and diagnoses error chains in code agents. Very close to diagnostic reasoning evaluation. |
| **AgentRewardBench** | 2504.08942 | April 2025 | Benchmark for evaluating automatic evaluators of agent trajectories. Methodology relevant to validating stage-level PRMs. |

#### (E) Stage-Decomposed Code Repair (Non-PRM)

| Paper | arXiv ID | Date | Why Relevant |
|-------|----------|------|-------------|
| **Lingma SWE-GPT** | 2411.00622 | Nov 2024 | Explicitly decomposes software improvement into three stages: repository understanding, fault localization, patch generation. Same stage taxonomy. |
| **ARISE** | 2605.03117 | May 2026 | Repository-level graph representation for agentic fault localization and repair on SWE-bench Lite. Very recent. |
| **A Self-Improving Coding Agent** | 2504.15228 | April 2025 | Self-improvement via reflection on SWE-bench. ICLR 2025 workshop. Related to using reward signals for agent improvement. |

---

### Key Recommendations

The papers most likely to be **missed** and most directly competing are:

1. **SWE-Shepherd (2604.10493)** - This is the closest concurrent work: it explicitly trains PRMs for SWE-bench code agents at the action level. Published just days before SWE-TRACE.

2. **CodeTracer (2604.11641)** - Directly addresses diagnosing where agents go wrong in code repair, with stage-level and step-level failure localization. Highly overlapping motivation.

3. **"When Agents Go Astray" / SWE-PRM (2509.02360)** - The earlier work that established inference-time PRMs for SWE agents with trajectory-level error detection.

4. **QiMeng-PRepair (2604.05963)** - Reward-based optimization specifically for the patch/edit stage of code repair.

5. **Agentic Rubrics (2601.04171)** - Rubric-based evaluation without execution, relevant to how "stage-level" quality is assessed.

6. **DreamPRM-Code (2512.15000)** - Predecessor to FunPRM that established function-as-step paradigm.

Sources:
- [SWE-TRACE](https://arxiv.org/abs/2604.14820)
- [TRAJEVAL](https://arxiv.org/abs/2603.24631)
- [FunPRM](https://arxiv.org/abs/2601.22249)
- [ORPS](https://arxiv.org/abs/2412.15118)
- [SWE-Shepherd](https://arxiv.org/abs/2604.10493)
- [When Agents Go Astray (SWE-PRM)](https://arxiv.org/abs/2509.02360)
- [Agentic Rubrics](https://arxiv.org/abs/2601.04171)
- [SecCodePRM](https://arxiv.org/abs/2602.10418)
- [DreamPRM-Code](https://arxiv.org/abs/2512.15000)
- [CodePRM (ACL 2025)](https://aclanthology.org/2025.findings-acl.428/)
- [QiMeng-PRepair](https://arxiv.org/abs/2604.05963)
- [RePair (ACL 2024)](https://arxiv.org/abs/2408.11296)
- [muCode](https://arxiv.org/abs/2502.20380)
- [CodeTracer](https://arxiv.org/abs/2604.11641)
- [AgentRewardBench](https://arxiv.org/abs/2504.08942)
- [Lingma SWE-GPT](https://arxiv.org/abs/2411.00622)
- [ARISE](https://arxiv.org/abs/2605.03117)
- [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228)

agentId: afe11fc8aa27ebe28 (use SendMessage with to: 'afe11fc8aa27ebe28' to continue this agent)
&lt;usage>total_tokens: 34643
tool_uses: 24
duration_ms: 159673&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b807332-ddec-4178-9ec5-bdeddeb32f6c",
  "isSidechain": false,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "type": "user",
  "uuid": "af0518b2-a8c1-4fd8-8437-797ff5c96bbb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper idea about \"stage-level process reward models for code repair\" that evaluates diagnostic reasoning quality at each repair stage (localize, diagnose, patch). I need to find competing or concurrent work that the authors might have missed.\n\nPlease search for:\n1. \"process reward model code repair 2026\" - any recent PRMs specifically for code repair\n2. \"diagnostic reasoning code agent 2026\" - reasoning evaluation in code agents\n3. \"reward model SWE-bench 2026\" - reward models evaluated on SWE-bench\n4. \"step-level reward code generation 2026\" - step-level rewards for code tasks\n5. \"ORPS execution grounded process reward\" - verify arXiv:2412.15118\n\nAlso search for:\n6. \"SWE-TRACE rubric PRM code agent\" to verify arXiv:2604.14820\n7. \"TRAJEVAL trajectory evaluation code agent\" to verify arXiv:2603.24631\n8. \"FunPRM function step code generation\" to verify arXiv:2601.22249\n\nReport what you find - especially any papers NOT cited in this proposal that are highly relevant.",
    "agentId": "afe11fc8aa27ebe28",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Here is my analysis and report:\n\n---\n\n## Research Landscape Report: Stage-Level Process Reward Models for Code Repair\n\n### Papers Successfully Verified\n\nAll four papers you asked me to verify exist and are confirmed:\n\n1. **ORPS (arXiv:2412.15118)** - \"Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation\" - Confirmed. Presented at ICML 2025. Introduces Outcome-Refining Process Supervision using tree-structured search with execution feedback, eliminating need for trained PRMs.\n\n2. **SWE-TRACE (arXiv:2604.14820)** - \"Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling\" - Confirmed (April 2026). Uses a Rubric-Based PRM where a Rubric-Agent provides dense heuristic feedback on intermediate steps. Evaluates full trajectory considering localization, inspection, editing, and validation.\n\n3. **TRAJEVAL (arXiv:2603.24631)** - \"Decomposing Code Agent Trajectories for Fine-Grained Diagnosis\" - Confirmed (March 2026). Decomposes trajectories into search (file localization), read (function comprehension), and edit stages, computing precision/recall against reference patches.\n\n4. **FunPRM (arXiv:2601.22249)** - \"Function-as-Step Process Reward Model with Meta Reward Correction for Code Generation\" - Confirmed (January 2026). Treats functions as PRM reasoning steps with meta-learning reward correction.\n\n---\n\n### Highly Relevant Papers That May Be MISSING From the Proposal\n\nThese are papers the authors should strongly consider citing:\n\n#### (A) Direct Competitors / Concurrent Work on PRMs for Code Agents\n\n| Paper | arXiv ID | Date | Why Relevant |\n|-------|----------|------|-------------|\n| **SWE-Shepherd** | 2604.10493 | April 2026 | Trains a lightweight PRM on SWE-Bench trajectories for action-level reward, used to guide agent inference. Directly competes with stage-level PRM idea. |\n| **\"When Agents Go Astray\" (SWE-PRM)** | 2509.02360 | Sept 2025 | Inference-time PRM that course-corrects SWE agents mid-trajectory using a taxonomy of inefficiencies. Improved SWE-bench from 40% to 50.6%. Very close in spirit. |\n| **Agentic Rubrics as Contextual Verifiers** | 2601.04171 | Jan 2026 | Creates codebase-grounded rubric checklists to score patches without test execution. Rubric-based verification is analogous to stage-level rubrics. |\n\n#### (B) Code PRMs (Not Agent-Level but Related)\n\n| Paper | arXiv ID | Date | Why Relevant |\n|-------|----------|------|-------------|\n| **SecCodePRM** | 2602.10418 | Feb 2026 | Security-oriented PRM with step-level security scoring along code trajectories. Shows domain-specific PRM for code. |\n| **DreamPRM-Code** | 2512.15000 | Dec 2025 | Function-as-step PRM with label correction for code. Predecessor/concurrent to FunPRM. |\n| **CodePRM** | ACL 2025 Findings | 2025 | Execution feedback-enhanced PRM with Generate-Verify-Refine pipeline. Foundational prior work. |\n\n#### (C) Code Repair with Reward Models\n\n| Paper | arXiv ID | Date | Why Relevant |\n|-------|----------|------|-------------|\n| **QiMeng-PRepair** | 2604.05963 | April 2026 | Edit-Aware Group Relative Policy Optimization for precise code repair. Uses reward to encourage minimal edits. Directly relevant to the \"patch\" stage. |\n| **RePair** | 2408.11296 | ACL 2024 | Process-based feedback for automated program repair. Iterative generation with reward model as critic. Important predecessor. |\n| **muCode** | 2502.20380 | Feb 2025 | Multi-turn code generation via single-step rewards, treats code gen as one-step recoverable MDP. Relevant theoretical framing. |\n\n#### (D) Trajectory Diagnosis and Tracing\n\n| Paper | arXiv ID | Date | Why Relevant |\n|-------|----------|------|-------------|\n| **CodeTracer** | 2604.11641 | April 2026 | Tracing architecture that reconstructs full state transition history, performs failure onset localization and diagnoses error chains in code agents. Very close to diagnostic reasoning evaluation. |\n| **AgentRewardBench** | 2504.08942 | April 2025 | Benchmark for evaluating automatic evaluators of agent trajectories. Methodology relevant to validating stage-level PRMs. |\n\n#### (E) Stage-Decomposed Code Repair (Non-PRM)\n\n| Paper | arXiv ID | Date | Why Relevant |\n|-------|----------|------|-------------|\n| **Lingma SWE-GPT** | 2411.00622 | Nov 2024 | Explicitly decomposes software improvement into three stages: repository understanding, fault localization, patch generation. Same stage taxonomy. |\n| **ARISE** | 2605.03117 | May 2026 | Repository-level graph representation for agentic fault localization and repair on SWE-bench Lite. Very recent. |\n| **A Self-Improving Coding Agent** | 2504.15228 | April 2025 | Self-improvement via reflection on SWE-bench. ICLR 2025 workshop. Related to using reward signals for agent improvement. |\n\n---\n\n### Key Recommendations\n\nThe papers most likely to be **missed** and most directly competing are:\n\n1. **SWE-Shepherd (2604.10493)** - This is the closest concurrent work: it explicitly trains PRMs for SWE-bench code agents at the action level. Published just days before SWE-TRACE.\n\n2. **CodeTracer (2604.11641)** - Directly addresses diagnosing where agents go wrong in code repair, with stage-level and step-level failure localization. Highly overlapping motivation.\n\n3. **\"When Agents Go Astray\" / SWE-PRM (2509.02360)** - The earlier work that established inference-time PRMs for SWE agents with trajectory-level error detection.\n\n4. **QiMeng-PRepair (2604.05963)** - Reward-based optimization specifically for the patch/edit stage of code repair.\n\n5. **Agentic Rubrics (2601.04171)** - Rubric-based evaluation without execution, relevant to how \"stage-level\" quality is assessed.\n\n6. **DreamPRM-Code (2512.15000)** - Predecessor to FunPRM that established function-as-step paradigm.\n\nSources:\n- [SWE-TRACE](https://arxiv.org/abs/2604.14820)\n- [TRAJEVAL](https://arxiv.org/abs/2603.24631)\n- [FunPRM](https://arxiv.org/abs/2601.22249)\n- [ORPS](https://arxiv.org/abs/2412.15118)\n- [SWE-Shepherd](https://arxiv.org/abs/2604.10493)\n- [When Agents Go Astray (SWE-PRM)](https://arxiv.org/abs/2509.02360)\n- [Agentic Rubrics](https://arxiv.org/abs/2601.04171)\n- [SecCodePRM](https://arxiv.org/abs/2602.10418)\n- [DreamPRM-Code](https://arxiv.org/abs/2512.15000)\n- [CodePRM (ACL 2025)](https://aclanthology.org/2025.findings-acl.428/)\n- [QiMeng-PRepair](https://arxiv.org/abs/2604.05963)\n- [RePair (ACL 2024)](https://arxiv.org/abs/2408.11296)\n- [muCode](https://arxiv.org/abs/2502.20380)\n- [CodeTracer](https://arxiv.org/abs/2604.11641)\n- [AgentRewardBench](https://arxiv.org/abs/2504.08942)\n- [Lingma SWE-GPT](https://arxiv.org/abs/2411.00622)\n- [ARISE](https://arxiv.org/abs/2605.03117)\n- [A Self-Improving Coding Agent](https://arxiv.org/abs/2504.15228)"
      }
    ],
    "totalDurationMs": 159673,
    "totalTokens": 34643,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1966,
      "cache_read_input_tokens": 30517,
      "output_tokens": 2159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1966
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2159,
          "cache_read_input_tokens": 30517,
          "cache_creation_input_tokens": 1966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1966,
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
  "sourceToolAssistantUUID": "1b807332-ddec-4178-9ec5-bdeddeb32f6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "af0518b2-a8c1-4fd8-8437-797ff5c96bbb",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify DiagPRM code repair reward model for EMNLP",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3"
}
```

---

### Assistant

_source line 18 · 2026-05-10T18:31:38.623Z_

Good, I've confirmed the key papers. Now let me search for some specific concerns: the SWE-smith dataset availability, the "When Agents Go Astray" paper which seems highly relevant, and verify the Agent-RLVR reference (June 2026 - future paper?).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af0518b2-a8c1-4fd8-8437-797ff5c96bbb",
  "isSidechain": false,
  "requestId": "req_011CauNATDVf3U69ymwg9syL",
  "type": "assistant",
  "uuid": "8868cf80-104a-4666-9856-10299c075fc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KPzqTZKqWL4D4qjd3okVH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5581,
      "cache_read_input_tokens": 28284,
      "output_tokens": 737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5581,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 737,
          "cache_read_input_tokens": 28284,
          "cache_creation_input_tokens": 5581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5581
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

_source line 19 · 2026-05-10T18:31:47.668Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Ta9MWSTPq8i9k7Bu7Sj5ep`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify SWE-smith dataset and Agent-RLVR",
  "prompt": "I need to verify two things:\n\n1. SWE-smith trajectory dataset: Search for \"Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k\" on HuggingFace or the web. Is this dataset publicly available? Also search for \"SWE-smith NeurIPS 2025\" to verify the paper.\n\n2. Agent-RLVR (arXiv:2506.11425, June 2026): This paper is claimed to be from June 2026, but today is May 2026. Search for \"Agent-RLVR arXiv 2506.11425\" and \"Training SWE Agents via Guidance and Environment Rewards\". Does this paper actually exist? A June 2026 arXiv ID would be suspicious since we're in May 2026.\n\n3. Also search for \"When Agents Go Astray SWE-PRM arXiv 2509.02360\" - this was flagged as a potentially missing competitor. Verify it exists and what it does.\n\nReport findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8868cf80-104a-4666-9856-10299c075fc7",
  "isSidechain": false,
  "requestId": "req_011CauNATDVf3U69ymwg9syL",
  "type": "assistant",
  "uuid": "1726994e-5969-4edc-a71a-a54bd23d83d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KPzqTZKqWL4D4qjd3okVH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5581,
      "cache_read_input_tokens": 28284,
      "output_tokens": 737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5581,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 737,
          "cache_read_input_tokens": 28284,
          "cache_creation_input_tokens": 5581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5581
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

_source line 20 · 2026-05-10T18:31:52.078Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013Zv4DmjbXTronaeqUVVChJ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify LLM-judge annotation feasibility",
  "prompt": "I'm evaluating whether LLM judges can reliably annotate \"diagnostic reasoning quality\" in code repair trajectories. This is a key assumption in a paper I'm reviewing.\n\nPlease search for:\n1. \"LLM judge code correctness reliability\" or \"LLM as judge code quality\" - how reliable are LLMs at judging code reasoning?\n2. \"inter-annotator agreement LLM judge\" - what kappa values do LLM judges typically achieve?\n3. \"process reward model annotation quality\" or \"PRM label noise\" - how noisy are PRM training labels?\n4. \"ThinkPRM arXiv 2504.16828\" - verify this paper about data-efficient generative PRMs\n\nI want to understand: Is it realistic to expect LLM judges to reliably distinguish \"sound reasoning that led to a bad patch\" from \"unsound reasoning that happened to produce a good patch\"? What does the literature say about LLM judge reliability for nuanced reasoning quality assessment?\n\nReport findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1726994e-5969-4edc-a71a-a54bd23d83d2",
  "isSidechain": false,
  "requestId": "req_011CauNATDVf3U69ymwg9syL",
  "type": "assistant",
  "uuid": "87f3d853-d6b4-42dd-8d6a-9a3209da96a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KPzqTZKqWL4D4qjd3okVH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5581,
      "cache_read_input_tokens": 28284,
      "output_tokens": 737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5581,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 737,
          "cache_read_input_tokens": 28284,
          "cache_creation_input_tokens": 5581,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5581
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

_source line 21 · 2026-05-10T18:32:27.791Z_

<details><summary>↩ Tool result · `toolu_01Ta9MWSTPq8i9k7Bu7Sj5ep`</summary>

```text
Here are my findings on all three items:

---

## 1. SWE-smith Trajectory Dataset (Kwai-Klear)

**Status: EXISTS and is publicly available.**

The dataset `Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k` is live on HuggingFace with 65,994 rows (1.58 GB). It contains trajectories used to train Klear-Agent-8B (Qwen3-8B fine-tuned) to a 39% solve rate on SWE-bench Verified.

**SWE-smith NeurIPS 2025: CONFIRMED.** The paper "SWE-smith: Scaling Data for Software Engineering Agents" (arXiv:2504.21798) was accepted as a **Spotlight** at the NeurIPS 2025 Datasets & Benchmarks Track. Authors include John Yang, Kilian Lieret, Carlos E. Jimenez, et al. It introduces a pipeline for generating SWE training data at scale (50k instances from 128 repos) and trains SWE-agent-LM-32B to 40.2% on SWE-bench Verified.

---

## 2. Agent-RLVR (arXiv:2506.11425)

**Status: EXISTS -- but the date anomaly is notable.**

The paper is live on arXiv at `2506.11425` and also on ResearchGate, alphaXiv, Scale Labs, and paperreading.club. The arXiv ID prefix `2506` indicates a June 2025 submission (not June 2026). ArXiv IDs use the format YYMM, so `2506` = June 2025, which is perfectly valid given today's date of May 2026.

**What it does:** Agent-RLVR introduces "agent guidance" to make RLVR work in multi-step agentic settings. It lifts Qwen-2.5-72B-Instruct from 9.4% to 22.4% on SWE-Bench Verified (pass@1), and to 27.8% with test-time reward model augmentation. Published by Scale AI.

**Conclusion:** The paper is NOT from June 2026 -- it is from June 2025. The `2506` prefix means 2025-06, not 2026-06. It is a legitimate, existing paper.

---

## 3. "When Agents Go Astray" / SWE-PRM (arXiv:2509.02360)

**Status: EXISTS.**

The paper is on arXiv (`2509.02360` = September 2025), also listed on OpenReview and IBM Research (confirming IBM affiliation). It was submitted to NeurIPS 2025.

**What it does:** Introduces SWE-PRM, an inference-time Process Reward Model that detects and course-corrects trajectory-level errors (redundant exploration, looping, failure to terminate) in real time during SWE agent execution. On SWE-bench Verified, closed-source PRMs improve resolution from 40.0% to 50.6% (+10.6 percentage points) at only ~$0.2 added inference cost per instance. This is the first application of PRMs for real-time trajectory-level error correction in SWE agents.

---

## Summary

| Item | Exists? | Notes |
|------|---------|-------|
| Kwai-Klear trajectories-66k | Yes | Public on HuggingFace, 66k rows |
| SWE-smith NeurIPS 2025 | Yes | Spotlight at D&B track, arXiv:2504.21798 |
| Agent-RLVR arXiv:2506.11425 | Yes | June **2025** (not 2026), by Scale AI |
| SWE-PRM arXiv:2509.02360 | Yes | September 2025, IBM Research, submitted to NeurIPS 2025 |

The claim that Agent-RLVR is from "June 2026" appears to be a misreading of the arXiv ID. `2506` in arXiv notation means year 20**25**, month 06. The paper is real and roughly one year old.

Sources:
- [Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k](https://huggingface.co/datasets/Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k)
- [SWE-smith GitHub (NeurIPS 2025 D&B Spotlight)](https://github.com/SWE-bench/SWE-smith)
- [SWE-smith on arXiv](https://arxiv.org/abs/2504.21798)
- [Agent-RLVR on arXiv](https://arxiv.org/abs/2506.11425)
- [Agent-RLVR on Scale Labs](https://labs.scale.com/papers/agent_rlvr)
- [When Agents Go Astray on arXiv](https://arxiv.org/abs/2509.02360)
- [When Agents Go Astray - IBM Research](https://research.ibm.com/publications/when-agents-go-astray-course-correcting-swe-agents-with-prms)

agentId: a859236b7efeb0da8 (use SendMessage with to: 'a859236b7efeb0da8' to continue this agent)
&lt;usage>total_tokens: 15592
tool_uses: 5
duration_ms: 40115&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1726994e-5969-4edc-a71a-a54bd23d83d2",
  "isSidechain": false,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "type": "user",
  "uuid": "f05b3cc2-aeaa-4a29-88fd-3bf2356a579a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two things:\n\n1. SWE-smith trajectory dataset: Search for \"Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k\" on HuggingFace or the web. Is this dataset publicly available? Also search for \"SWE-smith NeurIPS 2025\" to verify the paper.\n\n2. Agent-RLVR (arXiv:2506.11425, June 2026): This paper is claimed to be from June 2026, but today is May 2026. Search for \"Agent-RLVR arXiv 2506.11425\" and \"Training SWE Agents via Guidance and Environment Rewards\". Does this paper actually exist? A June 2026 arXiv ID would be suspicious since we're in May 2026.\n\n3. Also search for \"When Agents Go Astray SWE-PRM arXiv 2509.02360\" - this was flagged as a potentially missing competitor. Verify it exists and what it does.\n\nReport findings concisely.",
    "agentId": "a859236b7efeb0da8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings on all three items:\n\n---\n\n## 1. SWE-smith Trajectory Dataset (Kwai-Klear)\n\n**Status: EXISTS and is publicly available.**\n\nThe dataset `Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k` is live on HuggingFace with 65,994 rows (1.58 GB). It contains trajectories used to train Klear-Agent-8B (Qwen3-8B fine-tuned) to a 39% solve rate on SWE-bench Verified.\n\n**SWE-smith NeurIPS 2025: CONFIRMED.** The paper \"SWE-smith: Scaling Data for Software Engineering Agents\" (arXiv:2504.21798) was accepted as a **Spotlight** at the NeurIPS 2025 Datasets & Benchmarks Track. Authors include John Yang, Kilian Lieret, Carlos E. Jimenez, et al. It introduces a pipeline for generating SWE training data at scale (50k instances from 128 repos) and trains SWE-agent-LM-32B to 40.2% on SWE-bench Verified.\n\n---\n\n## 2. Agent-RLVR (arXiv:2506.11425)\n\n**Status: EXISTS -- but the date anomaly is notable.**\n\nThe paper is live on arXiv at `2506.11425` and also on ResearchGate, alphaXiv, Scale Labs, and paperreading.club. The arXiv ID prefix `2506` indicates a June 2025 submission (not June 2026). ArXiv IDs use the format YYMM, so `2506` = June 2025, which is perfectly valid given today's date of May 2026.\n\n**What it does:** Agent-RLVR introduces \"agent guidance\" to make RLVR work in multi-step agentic settings. It lifts Qwen-2.5-72B-Instruct from 9.4% to 22.4% on SWE-Bench Verified (pass@1), and to 27.8% with test-time reward model augmentation. Published by Scale AI.\n\n**Conclusion:** The paper is NOT from June 2026 -- it is from June 2025. The `2506` prefix means 2025-06, not 2026-06. It is a legitimate, existing paper.\n\n---\n\n## 3. \"When Agents Go Astray\" / SWE-PRM (arXiv:2509.02360)\n\n**Status: EXISTS.**\n\nThe paper is on arXiv (`2509.02360` = September 2025), also listed on OpenReview and IBM Research (confirming IBM affiliation). It was submitted to NeurIPS 2025.\n\n**What it does:** Introduces SWE-PRM, an inference-time Process Reward Model that detects and course-corrects trajectory-level errors (redundant exploration, looping, failure to terminate) in real time during SWE agent execution. On SWE-bench Verified, closed-source PRMs improve resolution from 40.0% to 50.6% (+10.6 percentage points) at only ~$0.2 added inference cost per instance. This is the first application of PRMs for real-time trajectory-level error correction in SWE agents.\n\n---\n\n## Summary\n\n| Item | Exists? | Notes |\n|------|---------|-------|\n| Kwai-Klear trajectories-66k | Yes | Public on HuggingFace, 66k rows |\n| SWE-smith NeurIPS 2025 | Yes | Spotlight at D&B track, arXiv:2504.21798 |\n| Agent-RLVR arXiv:2506.11425 | Yes | June **2025** (not 2026), by Scale AI |\n| SWE-PRM arXiv:2509.02360 | Yes | September 2025, IBM Research, submitted to NeurIPS 2025 |\n\nThe claim that Agent-RLVR is from \"June 2026\" appears to be a misreading of the arXiv ID. `2506` in arXiv notation means year 20**25**, month 06. The paper is real and roughly one year old.\n\nSources:\n- [Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k](https://huggingface.co/datasets/Kwai-Klear/SWE-smith-mini_swe_agent_plus-trajectories-66k)\n- [SWE-smith GitHub (NeurIPS 2025 D&B Spotlight)](https://github.com/SWE-bench/SWE-smith)\n- [SWE-smith on arXiv](https://arxiv.org/abs/2504.21798)\n- [Agent-RLVR on arXiv](https://arxiv.org/abs/2506.11425)\n- [Agent-RLVR on Scale Labs](https://labs.scale.com/papers/agent_rlvr)\n- [When Agents Go Astray on arXiv](https://arxiv.org/abs/2509.02360)\n- [When Agents Go Astray - IBM Research](https://research.ibm.com/publications/when-agents-go-astray-course-correcting-swe-agents-with-prms)"
      }
    ],
    "totalDurationMs": 40115,
    "totalTokens": 15592,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 1707,
      "cache_creation_input_tokens": 2147,
      "cache_read_input_tokens": 10416,
      "output_tokens": 1322,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2147
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1707,
          "output_tokens": 1322,
          "cache_read_input_tokens": 10416,
          "cache_creation_input_tokens": 2147,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2147,
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
  "sourceToolAssistantUUID": "1726994e-5969-4edc-a71a-a54bd23d83d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T18:33:21.526Z_

<details><summary>↩ Tool result · `toolu_013Zv4DmjbXTronaeqUVVChJ`</summary>

```text
Here is my synthesis of the literature on LLM judge reliability for diagnostic reasoning quality in code repair trajectories:

---

## Summary of Findings

### 1. LLM Judge Reliability for Code Correctness

The evidence is **mixed but cautionary** for your specific use case:

- **General agreement rates**: Top-tier LLM judges achieve Cohen's Kappa of ~0.8 with humans on straightforward evaluation tasks (comparable to human-human agreement). However, this is for relatively clear-cut quality dimensions, not nuanced reasoning assessment.
- **Code-specific weakness**: LLMs frequently misclassify wrong code as correct (false positives) and correct code as wrong (false negatives) when they cannot execute the code. This is a fundamental limitation for judging "diagnostic reasoning quality" without execution feedback.
- **Overcorrection bias**: When prompted to explain reasoning and propose fixes, models become *more* prone to incorrectly classifying conforming code as erroneous -- a direct concern for your scenario of distinguishing sound-but-unsuccessful reasoning from unsound-but-lucky reasoning.

### 2. Inter-Annotator Agreement (Kappa Values)

- A comprehensive study of 54 LLM judges across 1,994 samples found average human-human Cohen's Kappa of **0.801** as the benchmark.
- **27 Tier-1 judges** achieved "substantial" to "almost perfect" agreement (kappa in the 0.6-0.8+ range) on standard tasks.
- However, [arXiv 2412.12509](https://arxiv.org/abs/2412.12509) demonstrates that even at fixed temperature, varying only the random seed produces significant judgment variability -- reliability (McDonald's omega) degrades for more nuanced assessments.
- **Position bias** can shift accuracy by 10%+ in pairwise code judgments just from swapping presentation order.

### 3. PRM Label Noise

This is where the picture gets most concerning for your paper's assumption:

- **PRM800K** (the gold-standard process supervision dataset) uses expensive human expert annotation, yet Monte Carlo Estimation (MCE) methods used for scaling introduce **false positives** when an initially incorrect step is later corrected within a trajectory that still reaches the correct answer -- a direct analog to your "unsound reasoning that happened to produce a good patch" scenario.
- **Credit misattribution** is a known, fundamental problem: MCE assigns step-level labels based on rollout outcomes, leading to noisy, misaligned supervision.
- Recent papers (SCAN, FreePRM, DreamPRM-Code) all exist precisely because label noise is so severe that entire research programs focus on denoising PRM annotations.

### 4. ThinkPRM (arXiv 2504.16828) -- Verified

ThinkPRM is real and demonstrates that **generative verification via chain-of-thought outperforms discriminative PRMs** using only ~1% of PRM800K's process labels (fine-tuned on ~1K synthetic verification CoTs filtered using only 8K gold labels). Key results:
- Outperforms LLM-as-a-Judge baselines on ProcessBench, MATH-500, AIME '24
- Surpasses discriminative verifiers trained on full PRM800K by 8% (GPQA-Diamond) and 4.5% (LiveCodeBench) out-of-domain

This suggests that *if* you use a reasoning model as the judge (generating explicit verification traces), you get substantially better step-level assessment than naive LLM-as-a-Judge approaches.

---

## Direct Answer to Your Question

**Is it realistic to expect LLM judges to reliably distinguish "sound reasoning that led to a bad patch" from "unsound reasoning that happened to produce a good patch"?**

**Probably not with standard LLM-as-a-Judge setups.** The literature indicates:

1. **The exact failure mode you describe is a known problem**: MCE-based PRM labels suffer from precisely this credit misattribution -- correct outcomes mask incorrect intermediate steps, and incorrect outcomes mask correct intermediate reasoning.

2. **LLM judges without execution struggle with code correctness**: They cannot reliably determine whether code works without running it, making judgments about reasoning *quality* even harder.

3. **Achievable reliability degrades with task nuance**: Kappa values of 0.8 are for relatively clear evaluations. For "diagnostic reasoning quality" -- a subjective, multi-dimensional construct -- expect substantially lower agreement.

4. **Mitigation exists but requires care**: ThinkPRM-style generative verification (having the judge produce explicit reasoning traces about each step) significantly outperforms naive judging. Chain-of-thought evaluation and "slow thinking" prompts help, but introduce overcorrection bias.

**Bottom line**: The paper you're reviewing should acknowledge this as a significant threat to validity. LLM judges can *approximate* reasoning quality annotations, but the literature suggests 10-20%+ error rates on nuanced code reasoning distinctions, with systematic biases (verbosity preference, position effects, overcorrection) that could confound results. The strongest mitigation would be a ThinkPRM-style generative verifier with human-validated calibration on a subset.

---

Sources:
- [A Survey on LLM-as-a-Judge (arXiv 2411.15594)](https://arxiv.org/abs/2411.15594)
- [Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge (arXiv 2412.12509)](https://arxiv.org/abs/2412.12509)
- [Judge's Verdict: LLM Judge Capability Through Human Agreement](https://arxiv.org/html/2510.09738v1)
- [ThinkPRM: Process Reward Models That Think (arXiv 2504.16828)](https://arxiv.org/abs/2504.16828)
- [Towards Robust Process Reward Modeling via Noise-aware Learning](https://arxiv.org/html/2601.12748)
- [Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://llm-judge-bias.github.io/)
- [LLM-as-a-Judge for Human-AI Co-Creation: A Reliability-Aware Evaluation Framework for Coding](https://arxiv.org/html/2604.27727)
- [CodeJudgeBench: Benchmarking LLM-as-a-Judge for Coding Tasks (arXiv 2507.10535)](https://arxiv.org/abs/2507.10535)
- [SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning](https://openreview.net/pdf/90e683c8f88b8fe14fd41acb175f70e1cbcdd305.pdf)
- [Free Process Rewards without Process Labels](https://arxiv.org/html/2412.01981v1)
- [RAND Judge Reliability Harness](https://www.rand.org/pubs/tools/TLA4547-1.html)

agentId: a5e1ca385a27e9225 (use SendMessage with to: 'a5e1ca385a27e9225' to continue this agent)
&lt;usage>total_tokens: 20120
tool_uses: 9
duration_ms: 89446&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87f3d853-d6b4-42dd-8d6a-9a3209da96a6",
  "isSidechain": false,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "type": "user",
  "uuid": "281fe74a-add5-4b9d-82d4-78cbf099a8ee",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm evaluating whether LLM judges can reliably annotate \"diagnostic reasoning quality\" in code repair trajectories. This is a key assumption in a paper I'm reviewing.\n\nPlease search for:\n1. \"LLM judge code correctness reliability\" or \"LLM as judge code quality\" - how reliable are LLMs at judging code reasoning?\n2. \"inter-annotator agreement LLM judge\" - what kappa values do LLM judges typically achieve?\n3. \"process reward model annotation quality\" or \"PRM label noise\" - how noisy are PRM training labels?\n4. \"ThinkPRM arXiv 2504.16828\" - verify this paper about data-efficient generative PRMs\n\nI want to understand: Is it realistic to expect LLM judges to reliably distinguish \"sound reasoning that led to a bad patch\" from \"unsound reasoning that happened to produce a good patch\"? What does the literature say about LLM judge reliability for nuanced reasoning quality assessment?\n\nReport findings concisely.",
    "agentId": "a5e1ca385a27e9225",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my synthesis of the literature on LLM judge reliability for diagnostic reasoning quality in code repair trajectories:\n\n---\n\n## Summary of Findings\n\n### 1. LLM Judge Reliability for Code Correctness\n\nThe evidence is **mixed but cautionary** for your specific use case:\n\n- **General agreement rates**: Top-tier LLM judges achieve Cohen's Kappa of ~0.8 with humans on straightforward evaluation tasks (comparable to human-human agreement). However, this is for relatively clear-cut quality dimensions, not nuanced reasoning assessment.\n- **Code-specific weakness**: LLMs frequently misclassify wrong code as correct (false positives) and correct code as wrong (false negatives) when they cannot execute the code. This is a fundamental limitation for judging \"diagnostic reasoning quality\" without execution feedback.\n- **Overcorrection bias**: When prompted to explain reasoning and propose fixes, models become *more* prone to incorrectly classifying conforming code as erroneous -- a direct concern for your scenario of distinguishing sound-but-unsuccessful reasoning from unsound-but-lucky reasoning.\n\n### 2. Inter-Annotator Agreement (Kappa Values)\n\n- A comprehensive study of 54 LLM judges across 1,994 samples found average human-human Cohen's Kappa of **0.801** as the benchmark.\n- **27 Tier-1 judges** achieved \"substantial\" to \"almost perfect\" agreement (kappa in the 0.6-0.8+ range) on standard tasks.\n- However, [arXiv 2412.12509](https://arxiv.org/abs/2412.12509) demonstrates that even at fixed temperature, varying only the random seed produces significant judgment variability -- reliability (McDonald's omega) degrades for more nuanced assessments.\n- **Position bias** can shift accuracy by 10%+ in pairwise code judgments just from swapping presentation order.\n\n### 3. PRM Label Noise\n\nThis is where the picture gets most concerning for your paper's assumption:\n\n- **PRM800K** (the gold-standard process supervision dataset) uses expensive human expert annotation, yet Monte Carlo Estimation (MCE) methods used for scaling introduce **false positives** when an initially incorrect step is later corrected within a trajectory that still reaches the correct answer -- a direct analog to your \"unsound reasoning that happened to produce a good patch\" scenario.\n- **Credit misattribution** is a known, fundamental problem: MCE assigns step-level labels based on rollout outcomes, leading to noisy, misaligned supervision.\n- Recent papers (SCAN, FreePRM, DreamPRM-Code) all exist precisely because label noise is so severe that entire research programs focus on denoising PRM annotations.\n\n### 4. ThinkPRM (arXiv 2504.16828) -- Verified\n\nThinkPRM is real and demonstrates that **generative verification via chain-of-thought outperforms discriminative PRMs** using only ~1% of PRM800K's process labels (fine-tuned on ~1K synthetic verification CoTs filtered using only 8K gold labels). Key results:\n- Outperforms LLM-as-a-Judge baselines on ProcessBench, MATH-500, AIME '24\n- Surpasses discriminative verifiers trained on full PRM800K by 8% (GPQA-Diamond) and 4.5% (LiveCodeBench) out-of-domain\n\nThis suggests that *if* you use a reasoning model as the judge (generating explicit verification traces), you get substantially better step-level assessment than naive LLM-as-a-Judge approaches.\n\n---\n\n## Direct Answer to Your Question\n\n**Is it realistic to expect LLM judges to reliably distinguish \"sound reasoning that led to a bad patch\" from \"unsound reasoning that happened to produce a good patch\"?**\n\n**Probably not with standard LLM-as-a-Judge setups.** The literature indicates:\n\n1. **The exact failure mode you describe is a known problem**: MCE-based PRM labels suffer from precisely this credit misattribution -- correct outcomes mask incorrect intermediate steps, and incorrect outcomes mask correct intermediate reasoning.\n\n2. **LLM judges without execution struggle with code correctness**: They cannot reliably determine whether code works without running it, making judgments about reasoning *quality* even harder.\n\n3. **Achievable reliability degrades with task nuance**: Kappa values of 0.8 are for relatively clear evaluations. For \"diagnostic reasoning quality\" -- a subjective, multi-dimensional construct -- expect substantially lower agreement.\n\n4. **Mitigation exists but requires care**: ThinkPRM-style generative verification (having the judge produce explicit reasoning traces about each step) significantly outperforms naive judging. Chain-of-thought evaluation and \"slow thinking\" prompts help, but introduce overcorrection bias.\n\n**Bottom line**: The paper you're reviewing should acknowledge this as a significant threat to validity. LLM judges can *approximate* reasoning quality annotations, but the literature suggests 10-20%+ error rates on nuanced code reasoning distinctions, with systematic biases (verbosity preference, position effects, overcorrection) that could confound results. The strongest mitigation would be a ThinkPRM-style generative verifier with human-validated calibration on a subset.\n\n---\n\nSources:\n- [A Survey on LLM-as-a-Judge (arXiv 2411.15594)](https://arxiv.org/abs/2411.15594)\n- [Can You Trust LLM Judgments? Reliability of LLM-as-a-Judge (arXiv 2412.12509)](https://arxiv.org/abs/2412.12509)\n- [Judge's Verdict: LLM Judge Capability Through Human Agreement](https://arxiv.org/html/2510.09738v1)\n- [ThinkPRM: Process Reward Models That Think (arXiv 2504.16828)](https://arxiv.org/abs/2504.16828)\n- [Towards Robust Process Reward Modeling via Noise-aware Learning](https://arxiv.org/html/2601.12748)\n- [Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://llm-judge-bias.github.io/)\n- [LLM-as-a-Judge for Human-AI Co-Creation: A Reliability-Aware Evaluation Framework for Coding](https://arxiv.org/html/2604.27727)\n- [CodeJudgeBench: Benchmarking LLM-as-a-Judge for Coding Tasks (arXiv 2507.10535)](https://arxiv.org/abs/2507.10535)\n- [SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning](https://openreview.net/pdf/90e683c8f88b8fe14fd41acb175f70e1cbcdd305.pdf)\n- [Free Process Rewards without Process Labels](https://arxiv.org/html/2412.01981v1)\n- [RAND Judge Reliability Harness](https://www.rand.org/pubs/tools/TLA4547-1.html)"
      }
    ],
    "totalDurationMs": 89446,
    "totalTokens": 20120,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 971,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 16418,
      "output_tokens": 1672,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1059
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 971,
          "output_tokens": 1672,
          "cache_read_input_tokens": 16418,
          "cache_creation_input_tokens": 1059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1059,
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
      "otherToolCount": 9
    }
  },
  "sourceToolAssistantUUID": "87f3d853-d6b4-42dd-8d6a-9a3209da96a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T18:33:26.635Z_

Now let me check the most critical missing competitor - "When Agents Go Astray" (SWE-PRM) - and verify the compute estimates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "281fe74a-add5-4b9d-82d4-78cbf099a8ee",
  "isSidechain": false,
  "requestId": "req_011CauNJWFHSUaGdrLynKJQv",
  "type": "assistant",
  "uuid": "fa1fd945-c3c8-462a-8c32-3d949ebc3905",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019j7sfepQPkrwc3rJqLUN52",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3934,
      "cache_read_input_tokens": 33865,
      "output_tokens": 467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3934,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 467,
          "cache_read_input_tokens": 33865,
          "cache_creation_input_tokens": 3934,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3934
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

_source line 24 · 2026-05-10T18:33:35.353Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LPtRWqXr5RD1jNzmfSjqCn`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify SWE-PRM overlap and compute estimates",
  "prompt": "I'm reviewing a paper called \"DiagPRM\" that proposes a stage-level process reward model for code repair. A potentially critical missing competitor is \"When Agents Go Astray\" / SWE-PRM (arXiv:2509.02360, September 2025, IBM Research).\n\nPlease help me understand:\n\n1. Search for \"When Agents Go Astray SWE-PRM process reward model\" and fetch the abstract or key details. Specifically:\n   - Does SWE-PRM operate at step/stage level or trajectory level?\n   - Does it detect specific types of errors (like localization errors vs. diagnosis errors)?\n   - How does it compare to what DiagPRM proposes (scoring diagnostic reasoning quality at each of three stages: localize, diagnose, patch)?\n\n2. Also search for \"CodeTracer arXiv 2604.11641 April 2026\" - this was flagged as another highly relevant competitor that does \"failure onset localization and diagnoses error chains in code agents.\"\n\n3. Search for \"SWE-bench Verified trajectory generation cost\" or \"SWE-bench API cost per instance\" - I want to verify whether generating 500 trajectories via API agents costs $1,500-2,500 as claimed. What are typical costs for running agents on SWE-bench instances?\n\nReport concisely - focus on the overlap with DiagPRM and whether these papers challenge DiagPRM's novelty."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa1fd945-c3c8-462a-8c32-3d949ebc3905",
  "isSidechain": false,
  "requestId": "req_011CauNJWFHSUaGdrLynKJQv",
  "type": "assistant",
  "uuid": "f7e48c7a-439c-4657-87dd-ddecb90d6a98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019j7sfepQPkrwc3rJqLUN52",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3934,
      "cache_read_input_tokens": 33865,
      "output_tokens": 467,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3934,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 467,
          "cache_read_input_tokens": 33865,
          "cache_creation_input_tokens": 3934,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3934
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
  "leafUuid": "f7e48c7a-439c-4657-87dd-ddecb90d6a98",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify DiagPRM code repair reward model for EMNLP",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3"
}
```

---

### Tool result

_source line 27 · 2026-05-10T18:37:07.230Z_

<details><summary>↩ Tool result · `toolu_01LPtRWqXr5RD1jNzmfSjqCn`</summary>

```text
I now have enough information to provide a comprehensive report. Here is my synthesis:

---

## 1. SWE-PRM ("When Agents Go Astray," arXiv:2509.02360, Sept 2025)

**Key differences from DiagPRM:**

- **Granularity:** SWE-PRM operates on a **sliding window of recent steps** (k=8 steps, invoked every n=5 steps). It does NOT decompose the repair process into semantic stages (localize/diagnose/patch). It monitors trajectory-level behavioral patterns.

- **Error taxonomy:** SWE-PRM uses three families of *process inefficiencies*:
  - Specification Errors (task violations, step repetition, termination unawareness)
  - Reasoning Errors (problem misidentification, tool selection errors, hallucinations)
  - Coordination Errors (task derailment, goal deviation, context handling)

  These are **behavioral/trajectory patterns**, not task-phase-specific categories. It does NOT distinguish localization errors from diagnosis errors from patch errors.

- **Mechanism:** SWE-PRM is an inference-time intervention tool -- it provides natural-language course-corrective feedback to a running agent. It is NOT a trained reward model; it uses off-the-shelf LLMs (Claude Sonnet, open-source models) with taxonomy-guided prompts. No fine-tuning is involved.

- **Overlap with DiagPRM:** Both are "process reward models" for code repair, but the overlap is mostly at the motivation level. SWE-PRM scores trajectory efficiency/health; DiagPRM (presumably) scores diagnostic reasoning quality at each of three semantic stages. SWE-PRM does not assess whether the agent correctly localized a bug or correctly diagnosed root cause -- it detects looping, redundancy, and drift.

**Novelty implications:** SWE-PRM does NOT challenge DiagPRM's stage-level decomposition (localize/diagnose/patch) or its focus on diagnostic reasoning quality. A paper could reasonably argue DiagPRM is complementary: SWE-PRM detects *how* the agent is behaving (efficiently vs. inefficiently), while DiagPRM evaluates *what* the agent concluded at each reasoning stage. However, SWE-PRM must be cited and differentiated.

---

## 2. CodeTracer (arXiv:2604.11641, April 2026)

**Key findings:**

- **Nature:** CodeTracer is a **post-hoc tracing and diagnostic tool**, NOT a reward model. It analyzes completed trajectories, not ongoing ones.

- **Failure onset localization:** Uses chain-based backward tracing from the failing output to identify the earliest decision causing downstream failure. It reconstructs a hierarchical trace tree and identifies error chains.

- **Stage decomposition:** CodeTracer identifies five workflow stages (environment verification, dependency installation, inspection/debugging, patching, verification), which partially overlaps with DiagPRM's three stages.

- **Error types:** Identifies "environment/setup issues, dependency resolution failures, mislocalized edits, incorrect hypotheses, verification misinterpretation, and unproductive looping." It distinguishes "incorrect" steps from "unuseful" steps but does NOT score diagnostic reasoning quality.

- **No reward model component:** CodeTracer does not produce reward scores. It provides diagnostic labels that could feed into reflective replay for recovery, but it is not designed to train or rank models.

**Novelty implications:** CodeTracer is more directly relevant to DiagPRM than SWE-PRM because it does failure onset localization and identifies error chains across stages. However, it operates purely post-hoc as an analysis framework -- it does not produce per-stage reward scores for training. If DiagPRM trains a reward model that scores diagnostic reasoning quality to improve generation, that is a distinct contribution from CodeTracer's diagnostic tracing. Still, CodeTracer must be cited as concurrent work doing stage-level failure analysis.

---

## 3. SWE-bench Trajectory Generation Cost

Based on available evidence:

- **Per-instance cost with frontier models:** The SWE-Gym paper (ICML 2025) states "solving software engineering tasks is computationally intensive, costing usually **$1 or more per task** with frontier models."
- **SWE-agent documentation** recommends a cost cap of ~$1-2 per instance for conservative runs.
- **Agentless** costs ~$0.34 per issue; simpler approaches cost as little as $0.07-0.14 per issue.
- **For 500 instances at $1-5/instance:** Total cost = $500-$2,500.

The claim of "$1,500-$2,500 for 500 trajectories" is **plausible but on the high end**. It would correspond to $3-5 per instance, which is realistic if:
- Using expensive models (Claude Opus / GPT-4) rather than Sonnet/GPT-4o
- Running multi-attempt configurations
- Allowing high turn counts (50+) without early stopping
- Including failed trajectories in the cost

With today's pricing (Sonnet at $3/$15 per MTok) and typical ~19 turns per trajectory, $1-3 per instance is a reasonable central estimate for competent agents, making $500-$1,500 the likely range for 500 instances. The $2,500 upper bound would require Opus-tier models or very long trajectories.

---

## Summary Assessment for DiagPRM's Novelty

| Competitor | Threat to Novelty | Key Distinction |
|---|---|---|
| SWE-PRM | Moderate -- must cite and differentiate | SWE-PRM monitors behavioral efficiency, not diagnostic reasoning quality per stage |
| CodeTracer | Moderate-High -- concurrent, partially overlapping | CodeTracer is a diagnostic tool, not a reward model; no training signal produced |

**DiagPRM's defensible novelty** rests on: (1) stage-level decomposition into localize/diagnose/patch as a reward signal, (2) scoring *reasoning quality* (not just correctness/efficiency), and (3) producing a trainable reward model (not just post-hoc analysis). Neither SWE-PRM nor CodeTracer do all three. However, both must be prominently discussed in related work, and the paper should clearly articulate why behavioral-pattern detection (SWE-PRM) and post-hoc tracing (CodeTracer) are insufficient substitutes for stage-level reasoning quality scoring.

Sources:
- [When Agents Go Astray: Course-Correcting SWE Agents with PRMs](https://arxiv.org/abs/2509.02360)
- [CodeTracer: Towards Traceable Agent States](https://arxiv.org/abs/2604.11641)
- [Training Software Engineering Agents and Verifiers with SWE-Gym](https://arxiv.org/abs/2412.21139)
- [SWE-agent Competitive Runs Documentation](https://swe-agent.com/latest/usage/competitive_runs/)
- [SWE-PRM at IBM Research](https://research.ibm.com/publications/when-agents-go-astray-course-correcting-swe-agents-with-prms)
- [CodeTracer on HuggingFace](https://huggingface.co/papers/2604.11641)

agentId: ae77a32d76f5d1507 (use SendMessage with to: 'ae77a32d76f5d1507' to continue this agent)
&lt;usage>total_tokens: 24951
tool_uses: 16
duration_ms: 211871&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7e48c7a-439c-4657-87dd-ddecb90d6a98",
  "isSidechain": false,
  "promptId": "93a4d80f-4afa-4710-953b-48076ba14215",
  "type": "user",
  "uuid": "dbecd38a-a5ec-4594-bc45-6c7969ce83b8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper called \"DiagPRM\" that proposes a stage-level process reward model for code repair. A potentially critical missing competitor is \"When Agents Go Astray\" / SWE-PRM (arXiv:2509.02360, September 2025, IBM Research).\n\nPlease help me understand:\n\n1. Search for \"When Agents Go Astray SWE-PRM process reward model\" and fetch the abstract or key details. Specifically:\n   - Does SWE-PRM operate at step/stage level or trajectory level?\n   - Does it detect specific types of errors (like localization errors vs. diagnosis errors)?\n   - How does it compare to what DiagPRM proposes (scoring diagnostic reasoning quality at each of three stages: localize, diagnose, patch)?\n\n2. Also search for \"CodeTracer arXiv 2604.11641 April 2026\" - this was flagged as another highly relevant competitor that does \"failure onset localization and diagnoses error chains in code agents.\"\n\n3. Search for \"SWE-bench Verified trajectory generation cost\" or \"SWE-bench API cost per instance\" - I want to verify whether generating 500 trajectories via API agents costs $1,500-2,500 as claimed. What are typical costs for running agents on SWE-bench instances?\n\nReport concisely - focus on the overlap with DiagPRM and whether these papers challenge DiagPRM's novelty.",
    "agentId": "ae77a32d76f5d1507",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have enough information to provide a comprehensive report. Here is my synthesis:\n\n---\n\n## 1. SWE-PRM (\"When Agents Go Astray,\" arXiv:2509.02360, Sept 2025)\n\n**Key differences from DiagPRM:**\n\n- **Granularity:** SWE-PRM operates on a **sliding window of recent steps** (k=8 steps, invoked every n=5 steps). It does NOT decompose the repair process into semantic stages (localize/diagnose/patch). It monitors trajectory-level behavioral patterns.\n\n- **Error taxonomy:** SWE-PRM uses three families of *process inefficiencies*:\n  - Specification Errors (task violations, step repetition, termination unawareness)\n  - Reasoning Errors (problem misidentification, tool selection errors, hallucinations)\n  - Coordination Errors (task derailment, goal deviation, context handling)\n\n  These are **behavioral/trajectory patterns**, not task-phase-specific categories. It does NOT distinguish localization errors from diagnosis errors from patch errors.\n\n- **Mechanism:** SWE-PRM is an inference-time intervention tool -- it provides natural-language course-corrective feedback to a running agent. It is NOT a trained reward model; it uses off-the-shelf LLMs (Claude Sonnet, open-source models) with taxonomy-guided prompts. No fine-tuning is involved.\n\n- **Overlap with DiagPRM:** Both are \"process reward models\" for code repair, but the overlap is mostly at the motivation level. SWE-PRM scores trajectory efficiency/health; DiagPRM (presumably) scores diagnostic reasoning quality at each of three semantic stages. SWE-PRM does not assess whether the agent correctly localized a bug or correctly diagnosed root cause -- it detects looping, redundancy, and drift.\n\n**Novelty implications:** SWE-PRM does NOT challenge DiagPRM's stage-level decomposition (localize/diagnose/patch) or its focus on diagnostic reasoning quality. A paper could reasonably argue DiagPRM is complementary: SWE-PRM detects *how* the agent is behaving (efficiently vs. inefficiently), while DiagPRM evaluates *what* the agent concluded at each reasoning stage. However, SWE-PRM must be cited and differentiated.\n\n---\n\n## 2. CodeTracer (arXiv:2604.11641, April 2026)\n\n**Key findings:**\n\n- **Nature:** CodeTracer is a **post-hoc tracing and diagnostic tool**, NOT a reward model. It analyzes completed trajectories, not ongoing ones.\n\n- **Failure onset localization:** Uses chain-based backward tracing from the failing output to identify the earliest decision causing downstream failure. It reconstructs a hierarchical trace tree and identifies error chains.\n\n- **Stage decomposition:** CodeTracer identifies five workflow stages (environment verification, dependency installation, inspection/debugging, patching, verification), which partially overlaps with DiagPRM's three stages.\n\n- **Error types:** Identifies \"environment/setup issues, dependency resolution failures, mislocalized edits, incorrect hypotheses, verification misinterpretation, and unproductive looping.\" It distinguishes \"incorrect\" steps from \"unuseful\" steps but does NOT score diagnostic reasoning quality.\n\n- **No reward model component:** CodeTracer does not produce reward scores. It provides diagnostic labels that could feed into reflective replay for recovery, but it is not designed to train or rank models.\n\n**Novelty implications:** CodeTracer is more directly relevant to DiagPRM than SWE-PRM because it does failure onset localization and identifies error chains across stages. However, it operates purely post-hoc as an analysis framework -- it does not produce per-stage reward scores for training. If DiagPRM trains a reward model that scores diagnostic reasoning quality to improve generation, that is a distinct contribution from CodeTracer's diagnostic tracing. Still, CodeTracer must be cited as concurrent work doing stage-level failure analysis.\n\n---\n\n## 3. SWE-bench Trajectory Generation Cost\n\nBased on available evidence:\n\n- **Per-instance cost with frontier models:** The SWE-Gym paper (ICML 2025) states \"solving software engineering tasks is computationally intensive, costing usually **$1 or more per task** with frontier models.\"\n- **SWE-agent documentation** recommends a cost cap of ~$1-2 per instance for conservative runs.\n- **Agentless** costs ~$0.34 per issue; simpler approaches cost as little as $0.07-0.14 per issue.\n- **For 500 instances at $1-5/instance:** Total cost = $500-$2,500.\n\nThe claim of \"$1,500-$2,500 for 500 trajectories\" is **plausible but on the high end**. It would correspond to $3-5 per instance, which is realistic if:\n- Using expensive models (Claude Opus / GPT-4) rather than Sonnet/GPT-4o\n- Running multi-attempt configurations\n- Allowing high turn counts (50+) without early stopping\n- Including failed trajectories in the cost\n\nWith today's pricing (Sonnet at $3/$15 per MTok) and typical ~19 turns per trajectory, $1-3 per instance is a reasonable central estimate for competent agents, making $500-$1,500 the likely range for 500 instances. The $2,500 upper bound would require Opus-tier models or very long trajectories.\n\n---\n\n## Summary Assessment for DiagPRM's Novelty\n\n| Competitor | Threat to Novelty | Key Distinction |\n|---|---|---|\n| SWE-PRM | Moderate -- must cite and differentiate | SWE-PRM monitors behavioral efficiency, not diagnostic reasoning quality per stage |\n| CodeTracer | Moderate-High -- concurrent, partially overlapping | CodeTracer is a diagnostic tool, not a reward model; no training signal produced |\n\n**DiagPRM's defensible novelty** rests on: (1) stage-level decomposition into localize/diagnose/patch as a reward signal, (2) scoring *reasoning quality* (not just correctness/efficiency), and (3) producing a trainable reward model (not just post-hoc analysis). Neither SWE-PRM nor CodeTracer do all three. However, both must be prominently discussed in related work, and the paper should clearly articulate why behavioral-pattern detection (SWE-PRM) and post-hoc tracing (CodeTracer) are insufficient substitutes for stage-level reasoning quality scoring.\n\nSources:\n- [When Agents Go Astray: Course-Correcting SWE Agents with PRMs](https://arxiv.org/abs/2509.02360)\n- [CodeTracer: Towards Traceable Agent States](https://arxiv.org/abs/2604.11641)\n- [Training Software Engineering Agents and Verifiers with SWE-Gym](https://arxiv.org/abs/2412.21139)\n- [SWE-agent Competitive Runs Documentation](https://swe-agent.com/latest/usage/competitive_runs/)\n- [SWE-PRM at IBM Research](https://research.ibm.com/publications/when-agents-go-astray-course-correcting-swe-agents-with-prms)\n- [CodeTracer on HuggingFace](https://huggingface.co/papers/2604.11641)"
      }
    ],
    "totalDurationMs": 211871,
    "totalTokens": 24951,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 407,
      "cache_read_input_tokens": 22803,
      "output_tokens": 1740,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 407
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1740,
          "cache_read_input_tokens": 22803,
          "cache_creation_input_tokens": 407,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 407,
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
  "sourceToolAssistantUUID": "f7e48c7a-439c-4657-87dd-ddecb90d6a98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T18:38:27.749Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information. Let me synthesize my findings and form my review judgment.

## Key Findings from My Research:

### Papers Verified:
- **SWE-RM** (2512.21919): Confirmed. 30B MoE, 62-74.6% on SWE-bench Verified. Now properly cited as primary baseline. ✓
- **SWE-Shepherd** (2604.10493): Confirmed. 51% vs 57% greedy. ✓
- **R4P** (2510.22775): Confirmed. 72.2% patch verification. ✓


- **RGFL** (2601.18044): Confirmed. 85% Hit@1. ✓
- **Agent-RRM** (2601.22154): Confirmed. ✓
- **SWE-smith dataset**: Confirmed publicly available on HuggingFace. ✓
- **ThinkPRM** (2504.16828): Confirmed. ✓
- **Agent-RLVR** (2506.11425): Confirmed, though the date is June 2025 rather than June 2026 as mentioned. ✓

### Missing but Important Papers (NOT cited in proposal):
1. **SWE-PRM / "When Agents Go Astray"**  (2509.02360, Sept 2025): Uses prompting at inference time to detect behavioral inefficiencies in SWE agents, improving performance from 40% to 50.6% on SWE-bench—distinct from trained reward models and from DiagPRM, so it needs to be cited.
2. **CodeTracer** (2604.11641, April 2026): Performs post-hoc diagnosis of agent trajectories with failure localization and error chain tracking, but isn't a reward model itself.
3. **QiMeng-PRepair** (2604.05963, April 2026): Applies reward-based optimization to code repair patches.

### Novelty Assessment:
The proposal now addresses Round 2's concerns by properly including SWE-RM as a primary baseline, clearly differentiating R4P and RGFL, addressing Agent-RRM overlap, and handling ORPS.

I'm noticing a few remaining gaps: SWE-PRM needs to be cited since it's a relevant behavioral PRM for SWE agents achieving 50.6% on the benchmark, CodeTracer should be included for its stage-level failure analysis in code agents, and there's a date error with Agent-RLVR listed as June 2026 when it should be June 2025.

On the LLM-judge side, the proposal acknowledges the 10-20%+ error rates in the literature and realistically expects kappa around 0.4-0.6 from the pilot study, which shows they're being appropriately cautious rather than overclaiming.

The feasibility checks out across the board: compute stays within the 200-hour budget, the 12-16 day timeline is tight but workable, SWE-smith's 66K trajectories are accessible, and the $1,500-2,500 API cost estimate for 500 trajectories is defensible even if on the higher end.

Now looking at the novelty more carefully, the key differentiator is training a step-level PRM that judges diagnostic reasoning quality across the entire repair pipeline while remaining execution-free at inference—using test execution only to validate training labels. Comparing against existing work, SWE-RM operates at trajectory level without diagnostic decomposition, SWE-Shepherd scores action utility rather than reasoning quality and underperforms greedy baselines, SWE-TRACE relies on hand-crafted rubric criteria, ORPS requires execution at every node, R4P only handles patches, and RGFL focuses solely on localization.

The proposal's real strength is that no prior work combines step-level process rewards with learned diagnostic reasoning quality across localization, diagnosis, and patching stages—SWE-Shepherd comes closest with step-level scoring but misses the reasoning quality angle, while ORPS has process rewards but demands execution overhead. If DiagPRM achieves better best-of-N performance than SWE-RM, it could meaningfully advance the SWE agent landscape, especially given the formal variance reduction argument and the potential of mining disagreement cases for harder training examples.

That said, the 8B-to-30B model size gap makes standalone outperformance unlikely—the more credible story is that DiagPRM complements SWE-RM rather than replaces it. The proposal itself is exceptionally well-crafted with sound experimental design: a pilot validates the annotation scheme, baselines include SWE-RM, the combination tests complementarity, DebugBench enables category-level analysis, and the variance argument provides theoretical grounding. The main gap is that SWE-PRM (September 2025, 50.6% performance) isn't cited and needs clear differentiation.

Beyond that, CodeTracer is missing from the related work, LLM-judge reliability is acknowledged with reasonable mitigations, and the 100-instance scale limits statistical power—if DiagPRM only marginally improves over SWE-RM or only helps in combination, reviewers might view it as incremental. There's also a positioning risk: while framing this as a language understanding problem fits EMNLP's NLP track, the systems-heavy nature of the work could push it toward SE venues instead.

On novelty, I'm reconsidering—the core contributions are solid. Decomposing into cognitive stages like localize/diagnose/patch rather than mechanical ones, scoring reasoning quality directly instead of action utility, the formal stability argument about variance reduction, and using disagreement cases as training signal all represent genuine advances, even if the crowded 2025-2026 landscape means the incremental novelty over ensemble approaches is moderate rather than transformative.

For feasibility, the compute and timeline work out, but the real risks are LLM-judge reliability and whether this actually outperforms strong baselines. I'm settling on 3.5/5 there. The proposal is exceptionally clear and well-structured with strong differentiation from competitors and a formal argument backing it up—that's 4.5/5 on clarity. On impact, if successful it contributes meaningfully to the growing SWE agent reward modeling space and the stage-level decomposition could have broader applications, though the 100-instance evaluation scale and model size gap with existing SWE-RM systems temper expectations for transformative gains.

The average comes to 3.625, which falls short of the 4.0 pass threshold. I'm noticing a few citations that should be included—SWE-PRM and CodeTracer both do related work on stage-level diagnosis for SWE agents—and the statistical power of 100 instances with N=5 is a legitimate concern, especially given the 8B versus 30B model size difference makes it harder to isolate the approach's independent contribution. That said, these are addressable issues. The core concept is solid, the methodology is thoughtful, the competitive analysis is comprehensive despite those two missing papers, and the project fits within the stated constraints.

Now I'm reconsidering whether my scores were calibrated correctly. The novelty at 3.5 feels right—the work is genuinely distinct and the formal variance framing adds rigor, but it's still an incremental step in a saturated area. For feasibility, I initially marked it 3.5 due to timeline pressure and LLM-judge reliability risks, but the pilot study actually does a lot to mitigate those concerns. The data pipeline is solid, the compute budget checks out, and the team has thought through the main failure modes. I think feasibility deserves a bump up.

With that adjustment, my revised average lands at 3.75, which still falls short of the 4.0 threshold. The missing citations and evaluation scope are both addressable in revision—those aren't fundamental flaws. The impact score of 3 reflects that this is competent and well-crafted work, but it doesn't feel like a breakthrough contribution for the field. For a venue like EMNLP 2026, I'm weighing whether this represents the kind of solid, methodical research they'd want to accept, or whether the limited scope and incremental nature push it toward revision.

Since this is already Round 3 and the authors have been responsive to previous feedback, I'm inclined toward "revise" rather than reject. The two missing citations are straightforward additions, and they don't actually undermine DiagPRM's core novelty—SWE-PRM operates differently (prompt-based), and CodeTracer isn't even a reward model. They belong in related work but don't change my assessment of the contribution itself.

The real constraint is the scoring: my honest read puts this around 3.75 average, which falls short of the 4.0 threshold required for acceptance. So despite the solid work and genuine novelty, I need to recommend revision with specific, actionable fixes: add those two citations, correct the Agent-RLVR date to June 2025, and consider adding discussion of expected effect size and statistical power to strengthen the empirical claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbecd38a-a5ec-4594-bc45-6c7969ce83b8",
  "isSidechain": false,
  "requestId": "req_011CauNb9FTNx9eB6MiJDM54",
  "type": "assistant",
  "uuid": "be1c9b85-2b50-492b-b2f9-f2e9cd41a33c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2tjzGenRk89CySTBC6hnj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2286,
      "cache_read_input_tokens": 37799,
      "output_tokens": 5166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5166,
          "cache_read_input_tokens": 37799,
          "cache_creation_input_tokens": 2286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2286
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

_source line 29 · 2026-05-10T18:39:02.239Z_

Now I have comprehensive research findings. Let me synthesize my assessment.

## Key Findings from Independent Verification

**Papers verified as real with accurate claims:**
- SWE-RM (2512.21919): ✓ Confirmed 62-74.6% on SWE-bench Verified
- SWE-Shepherd (2604.10493): ✓ Confirmed 51% vs 57% greedy
- R4P (2510.22775): ✓ Confirmed 72.2% accuracy
- RGFL (2601.18044): ✓ Confirmed 85% Hit@1
- Agent-RRM (2601.22154): ✓ Confirmed
- SWE-smith dataset: ✓ Publicly available on HuggingFace (65,994 rows)
- ThinkPRM (2504.16828): ✓ Confirmed data-efficient generative PRMs

**Missing competitors identified:**
1. **SWE-PRM / "When Agents Go Astray"** (arXiv:2509.02360, Sept 2025, IBM): The first PRM applied to SWE agents, achieving 40%→50.6% on SWE-bench Verified. Uses taxonomy of process inefficiencies but is prompt-based (not trained) and detects behavioral patterns rather than diagnostic reasoning quality.
2. **CodeTracer** (arXiv:2604.11641, April 2026): Post-hoc stage-level failure onset localization across five workflow stages with error chain diagnosis. Not a reward model, but highly overlapping in motivation.

**Date error:** Agent-RLVR (arXiv:2506.11425) is from June **2025**, not June 2026 as stated (arXiv IDs use YYMM format).

**LLM-judge reliability concern:** Literature indicates 10-20%+ error rates on nuanced code reasoning distinctions, with position bias shifting accuracy by 10%+. The proposal's expected kappa of ~0.4-0.6 is realistic, and disagreement-case mining is a reasonable mitigation, but this remains a real risk.

**Compute/cost:** API trajectory generation at $1,500-2,500 for 500 trajectories is plausible (corresponds to $3-5/instance with frontier models). GPU budget of 130-160h H100 is within the 200h constraint.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "Stage-level diagnostic reasoning quality scoring is genuinely distinct from all identified competitors (SWE-RM=trajectory-level, SWE-Shepherd=action-utility, ORPS=execution-required, R4P=patch-only, SWE-PRM=behavioral-patterns), but the incremental advance over this crowded ensemble of 10+ related papers from 2025-2026 limits excitement."},
    "feasibility": {"score": 4, "rationale": "Compute (130-160h H100) and timeline (12-16 days auto) fit constraints; SWE-smith data is publicly available; pilot study design appropriately mitigates the key LLM-judge reliability risk; API cost estimates are plausible."},
    "clarity": {"score": 4.5, "rationale": "Exceptionally well-structured proposal with clear differentiation from competitors, formal variance argument, and thorough experimental design addressing previous review feedback comprehensively."},
    "impact": {"score": 3, "rationale": "100-instance evaluation limits statistical power for claiming improvement over SWE-RM (30B model); the complementarity framing is realistic but positions DiagPRM as an auxiliary signal rather than a standalone advance; contribution is solid but incremental for EMNLP main."}
  },
  "issues": [
    "MISSING CITATION: SWE-PRM / 'When Agents Go Astray' (arXiv:2509.02360, Sept 2025, IBM Research) is the first PRM applied to SWE agents (40%→50.6% on SWE-bench Verified). While prompt-based and behaviorally focused (not trained, not reasoning-quality-focused), it establishes the PRM-for-SWE-agents paradigm and must be cited and differentiated.",
    "MISSING CITATION: CodeTracer (arXiv:2604.11641, April 2026) performs stage-level failure onset localization with error chain diagnosis across five workflow stages. Though not a reward model, it directly shares DiagPRM's motivation of stage-level diagnostic analysis and is concurrent work requiring explicit positioning.",
    "DATE ERROR: Agent-RLVR (arXiv:2506.11425) is from June 2025, not June 2026. ArXiv IDs use YYMM format, so 2506 = 2025-06.",
    "STATISTICAL POWER CONCERN: Evaluating on only 100 SWE-bench Verified instances with N=5 may yield statistically insignificant differences vs. SWE-RM, especially given the 8B vs. 30B model size gap. The proposal should discuss expected effect size and statistical significance testing (e.g., bootstrap confidence intervals).",
    "LLM-JUDGE RELIABILITY NOT FULLY ADDRESSED: Literature shows 10-20%+ error rates on nuanced code reasoning judgments with systematic biases (position, verbosity). The pilot study helps but 50 trajectories (150 steps) may be too small to reliably estimate inter-annotator kappa for a multi-dimensional construct like 'diagnostic reasoning quality.' Consider 100+ trajectories for the pilot or adopting ThinkPRM-style generative verification."
  ],
  "feedback": "The revision is strong and addresses Round 2 feedback comprehensively. The remaining issues are minor but need fixing:\n\n1. **Add SWE-PRM citation**: Cite arXiv:2509.02360 in the landscape section. Differentiate: SWE-PRM uses prompt-based behavioral pattern detection (looping, drift, redundancy) without training, while DiagPRM trains a reward model scoring cognitive diagnostic reasoning quality. They are complementary: SWE-PRM monitors process efficiency, DiagPRM evaluates reasoning soundness.\n\n2. **Add CodeTracer citation**: Cite arXiv:2604.11641. Differentiate: CodeTracer is a post-hoc diagnostic analysis tool producing failure labels for human consumption, while DiagPRM produces per-stage reward scores for search guidance and RL training.\n\n3. **Fix Agent-RLVR date**: June 2025, not 2026.\n\n4. **Strengthen statistical methodology**: For the 100-instance SWE-bench evaluation, commit to bootstrap confidence intervals (1000 resamples) and report whether DiagPRM vs. SWE-RM differences are statistically significant. If expected effect size is small (2-5%), acknowledge this and emphasize the qualitative contribution (localized credit assignment enabling targeted resampling at failing stages, not just N selection).\n\n5. **Consider larger pilot**: 50 trajectories for pilot may be underpowered for estimating kappa reliably. If feasible, 100 trajectories (300 steps) would give more confident inter-annotator statistics.\n\nThe idea is close to passing—address these citations and the statistical power concern, and it should be publication-ready for EMNLP 2026 Findings.",
  "reason": "Solid, well-designed idea with genuine novelty in a crowded space, but two missing competitor citations (SWE-PRM, CodeTracer) and statistical power concerns on 100-instance evaluation keep average score (3.75) below the 4.0 pass threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be1c9b85-2b50-492b-b2f9-f2e9cd41a33c",
  "isSidechain": false,
  "requestId": "req_011CauNb9FTNx9eB6MiJDM54",
  "type": "assistant",
  "uuid": "d0e0a81f-9016-472b-8adc-130f7a46c7c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B2tjzGenRk89CySTBC6hnj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2286,
      "cache_read_input_tokens": 37799,
      "output_tokens": 5166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5166,
          "cache_read_input_tokens": 37799,
          "cache_creation_input_tokens": 2286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2286
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d0e0a81f-9016-472b-8adc-130f7a46c7c0",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify DiagPRM code repair reward model for EMNLP",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d0e0a81f-9016-472b-8adc-130f7a46c7c0",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify DiagPRM code repair reward model for EMNLP",
  "sessionId": "b29c0f20-422e-4834-bd9e-75b9cee267e3"
}
```

---
