# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/53165300-8211-427a-abe2-57e64b57a116.jsonl`
- **Structured JSON:** [`c83c994f8dfd99018ff7.json`](../../sessions/c8/c83c994f8dfd99018ff7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:00:49.388Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:00:49.388Z",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 7/10)\n{\n  \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\",\n  \"core_problem\": \"The lead empirical question — tractable because DebugBench provides oracle ground-truth labels for 4,253 instances organized in a 4-major/18-minor hierarchical taxonomy — is: how accurately can a few-shot LLM assign semantic bug type labels from the 18 minor sub-categories, and does that label accuracy determine whether hard categorical retrieval index partitioning outperforms soft root-cause-augmented retrieval (ReinFix, ICSE 2026) for cross-repository fix template transfer? This frames FTCR as an empirical study of LLM-generated categorical label quality and its downstream retrieval impact, yielding four falsifiable quantities: (X%) few-shot classifier accuracy vs. DebugBench ground-truth oracle labels at the minor-type level, with major-type aggregation as a secondary result; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type-partitioned retrieval vs. the soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts — a finding with direct generalization to any retrieval system using LLM-inferred labels.\\n\\nRetrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. InferFix (ESEC/FSE 2023, arXiv:2303.07263) establishes that type-conditioned retrieval benefits code repair: its Retriever uses contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type from Infer static analysis), and at retrieval time filters candidates to same-type fixes; however, InferFix requires running the Infer static analyzer on each query bug — applicable only to bugs Infer can detect, using Infer-specific diagnostic categories rather than a general natural-bug taxonomy. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is therefore two-fold: (1) whether LLM-inferred type labels can substitute for Infer-derived labels to enable type-conditioned retrieval for general natural bugs not addressable by static analysis (the X%/Y% question vs. InferFix); and (2) whether hard categorical type partitioning of the retrieval index outperforms ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer (the Z%/W% question). An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. Type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and become analytical contributions when addressed directly: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4; the Multiple Bugs sub-types are excluded from the fix-template corpus as multi-fault commits are rare and represent a different repair regime) yields approximately ~217 pairs per minor type on average for the full Python+Java corpus; for Java-only ablations (~559 pairs across ~14 types, ~40 per type), types with fewer than 30 instances are merged within the same major category (e.g., rare Syntax sub-types merged within Syntax; rare Logic sub-types merged within Logic — never across major categories); and (2) classifier error propagation — when an incoming bug is misclassified, hard partitioning underperforms soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback — turns potential weaknesses into the core empirical variables (Z% and W%) that define the paper's scientific contribution.\",\n  \"opportunity\": \"ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-conditioned cross-repository retrieval system for code repair: its Retriever is pretrained via contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type labels from Infer static analysis), and at retrieval time filters candidates to same-type fixes using Infer-derived labels. The encoder itself encodes only the buggy code as a dense vector — type structures the contrastive training pairs but is not an explicit encoder input; the retriever learns type-correlated semantic similarity. InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#. Three properties distinguish InferFix from FTCR: (a) Type label acquisition — InferFix requires running the Infer static analyzer on each query bug to obtain its type label; only bugs Infer can detect are addressable; FTCR uses few-shot LLM classification, requiring no static analysis tooling and covering any natural bug that Infer cannot or would not detect; (b) Taxonomy scope — InferFix uses Infer-specific diagnostic IDs (null dereferences, resource leaks, thread-safety violations), not the 4-major/18-minor natural-bug taxonomy aligned with DebugBench (4 major categories: Syntax with 7 sub-types, Reference with 4 sub-types, Logic with 4 sub-types, Multiple Bugs with 3 sub-types); (c) Corpus — InferFix uses InferredBugs (Java/C# repos where Infer detected bugs); FTCR uses natural bug-fix pairs from issue trackers and CI logs. The open empirical question InferFix leaves unresolved is whether LLM-inferred type labels can substitute for Infer-derived labels to enable effective type-conditioned retrieval for general natural bugs — precisely what FTCR's X%/Y% calibration measures. InferFix validates that type-conditioned retrieval works (supporting FTCR's hypothesis) while leaving the LLM-label-quality-vs-retrieval-effectiveness question entirely unanswered. ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of the 18 minor semantic sub-types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than ReinFix's joint root-cause embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar embeddings but different repair operators do not. DebugBench's 4-major/18-minor hierarchical taxonomy uniquely provides 4,253 instances with ground-truth type annotations across C++, Java, and Python (organized as: Syntax/7 sub-types, Reference/4, Logic/4, Multiple Bugs/3), enabling direct classifier calibration at the minor-type level and turning error propagation from a latent risk into the paper's core measurable variable. The confidence-gated hybrid has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). M-RAG (ACL 2024, arXiv 2405.16420) validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis.\",\n  \"landscape\": \"RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% and is not a SOTA claim. InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-conditioned cross-repository retrieval system for code repair: it pretrains a Retriever via contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type from Infer static analysis), then at retrieval time filters candidates to same-type fixes using Infer-derived type labels. The encoder itself encodes only the buggy code as a dense vector — type structures the training pairs but is not an explicit encoder input; the retriever learns type-correlated semantic similarity. InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#, outperforming LLM baselines by 11–55%. Three design differences distinguish FTCR from InferFix: (a) Type label acquisition — InferFix requires Infer to run on each repository to produce type labels for both corpus and query bugs; FTCR uses few-shot LLM classification, covering any natural bug without static analysis tooling; the core empirical question vs. InferFix is whether LLM-inferred labels achieve sufficient accuracy (X%) to match Infer-derived retrieval quality; (b) Defect taxonomy — InferFix uses Infer-specific diagnostic IDs (covering only statically-detectable bug patterns), not the 4-major/18-minor natural-bug taxonomy aligned with DebugBench's empirically-grounded labels (Syntax/7, Reference/4, Logic/4, Multiple Bugs/3); (c) Corpus — InferFix uses InferredBugs (static-analysis artifacts); FTCR uses natural bug-fix pairs from SWE-bench, BugsInPy, Defects4J, and GitBug-Java. The scientific question InferFix leaves open — and FTCR directly tests — is whether LLM-inferred type labels achieve sufficient accuracy (X%) to enable type-conditioned retrieval that is effective for general natural bugs, and at what accuracy threshold does type-conditioned retrieval outperform soft embedding baselines (Z% > 0%, W% < Z%). ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning. Corpus quality confound: comparisons against published ReinFix results conflate two variables simultaneously — retrieval architecture (soft joint embedding vs. hard type partition) and corpus quality (100K TRANSFER synthetic pairs vs. 3,050 natural bug-fix pairs from issue trackers and CI logs). Intra-corpus ablations (FTCR vs. re-implemented ReinFix-style baseline on the same 3,050-pair natural corpus using the same text-embedding-3-large encoder) test the partitioning hypothesis cleanly and isolate architecture as the variable. Absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality differences simultaneously and are presented explicitly as such; they are not used to claim a clean head-to-head win on architecture alone. SWE-Exp (arXiv 2507.23361, revised February 2026) retrieves top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic Python-only pipeline. Three design differences: (1) soft vs. hard — SWE-Exp uses type as retrieval-time embedding metadata; FTCR partitions at index-construction time; (2) retrieved artifact — SWE-Exp stores distilled modification strategies; FTCR retrieves concrete fix patches; (3) scope — SWE-Exp is agentic and Python-only; FTCR covers C++/Java/Python in retrieval-only mode. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5. TypeRepair's context selection stage conditions on the identified defect type to select within-project code context and provide type-specific repair guidance — it does not retrieve from an external cross-repository fix corpus. Evidentiary basis: TypeRepair evaluates exclusively on Defects4J V1.2/V2.0 and QuixBugs — within-project Java bug collections that contain no external cross-repository retrieval component. The evaluation design (project-internal datasets, no external corpus described in benchmark setup) makes the within-project scope structurally evident from the experimental setup; any reviewer with full SQJ article access who finds this claim incorrect is encouraged to provide the correction, as the differentiation rests on the publicly visible evaluation design. TypeRepair is Java-only; FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 fix patches. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec while contextual and API information helps; the 'what to retrieve matters' finding motivates FTCR's type-partition design. DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3. Both update the landscape but are orthogonal to retrieval strategy. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via objective alignment. FTCR's structural departure from all prior work is to (1) classify incoming failures into discrete minor sub-categories of the 4-major/18-minor DebugBench taxonomy, then (2) retrieve only from the type-matched sub-index, using text-embedding-3-large (identical to ReinFix) for a clean intra-corpus partitioning comparison — with the random-partition control separating type-matching precision from pool-size reduction. RetypeR (ICSME 2024, Hao et al.) applies type-specific retrieval for Python type errors only; FTCR extends to 18 minor sub-types across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates multi-partition RAG outperforms single-store RAG across NLP tasks (+11% summarization, +8% translation, +12% dialogue). PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary scope. The APR survey (arXiv 2506.23749) reviews 63+ systems with no type-partitioned cross-language retrieval system identified.\",\n  \"approach\": \"We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms ReinFix's soft root-cause embedding for cross-repository fix template transfer, and that LLM-inferred type labels can substitute for the Infer-required labels used by InferFix to enable type-conditioned retrieval on general natural bugs. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix), same natural corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control.\\n\\nNLP Lead Contribution: LLM Label Quality and Downstream Retrieval Impact. The primary EMNLP Findings contribution is a complete causal decomposition of when hard type conditioning helps and when it hurts, parameterized by four falsifiable quantities measured at the minor-type level (18 sub-types of the 4-major/18-minor DebugBench hierarchy, with major-type aggregation reported as a secondary result): (X%) few-shot LLM classifier accuracy against DebugBench ground-truth oracle labels at the minor-type level; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement on DebugBench/Defects4J V1.2 for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances under hard partitioning vs. same baseline. Z% and W% are reported as aggregate rates across all correctly-classified and misclassified instances respectively; significance is tested via McNemar's test on paired pass/fail outcomes (baseline vs. FTCR, same instances); per-type breakdowns use Fisher's exact test with a minimum n≥30 instance threshold; 95% confidence intervals are reported for both Z% and W%. Together these quantities are a direct empirical answer to: 'LLM-inferred categorical labels enable hard retrieval partitioning only if X% and Y% are high enough to make the correctly-classified population (driving Z%) larger than the misclassified population (driving W%).' This generalizes beyond code repair to any system that uses LLM-generated labels to route queries into type-specific retrieval pools.\\n\\nExecution Plan for EMNLP 2026 ARR (May 25 deadline, 15 days from today). Auto-research mode (10–14 days) is the only constraint-compliant execution path. Day-by-day schedule with minimum viable submission (MVS) milestones:\\n\\n- Day 0 (May 10): Launch auto-research pipeline; begin 3-pass annotation of 3,050 corpus pairs using DebugBench few-shot examples as demonstrations for the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4); configure Defects4J V1.2 Java-8 Docker environments and GitBug-Java isolated containers. Compute: 2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.\\n- Day 1–3 (May 11–13): Annotation completes (~$183 Claude API cost). DebugBench classifier calibration: 20% held-out split (~851 instances, covering single-bug instances from the Syntax/Reference/Logic major categories and treated separately for the Multiple Bugs category) → X% per-minor-type accuracy with major-type aggregation as secondary. Cross-lingual Java transfer sample (56 human-verified pairs from Defects4J + GitBug-Java) → Y% transfer accuracy. Per-minor-type count table computed; within-major-category merge policy applied for rare minor types below the 30-instance Java threshold.\\n- Day 4–6 (May 14–16): Build type-partitioned sub-indices and ReinFix-style unified index (both text-embedding-3-large). Run Defects4J V1.2 ablations: Variant A (text-similarity RAG), Variant D (ReinFix-style re-implemented on same natural corpus), Variant E (FTCR@hard-all), Variant F (random-partition control, N equivalently-sized random sub-indices). Prepare pre-drafted paper skeleton (introduction, related work, method) during this window to reduce Day 13–15 writing pressure.\\n- Day 7–9 (May 17–19): DebugBench evaluation across all variants on single-bug instances (Syntax/Reference/Logic major categories); confidence-gated τ sweep on held-out validation split; stratify results by classifier confidence band: high-confidence correctly-classified → Z% (aggregate, McNemar's test); misclassified → W% (aggregate, McNemar's test); per-type Fisher's exact test for types with n≥30. SWE-bench Lite evaluation launched in parallel (requires 2 A100 nodes for ~10 min/instance).\\n- Day 10–12 (May 20–22): CodeBERT-base encoder ablation (same FTCR vs. ReinFix-style comparison, secondary encoder); taxonomy granularity ablation (major-type coarse/4 vs. minor-type fine/14 single-fault sub-types vs. merged-Java categories); retrieval k sweep (1/3/5/10).\\n- Day 13 (May 23): Results compilation; paper writing begins with NLP lead (X%/Y%/Z%/W% as opening contribution).\\n- Day 14–15 (May 24–25): Paper finalization and ARR submission. MVS for EMNLP Findings: DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. SWE-bench Lite Python results included if pipeline completes by Day 12, deferred to ICSE 2027 extended version otherwise.\\n\\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. InferFix demonstrates that type-conditioned retrieval improves over code-similarity retrieval, but requires Infer static analysis to label both corpus and query bugs. FTCR embodies a stronger form of this principle: classify the incoming bug using an LLM (no static analysis tooling required), then restrict the retrieval pool to same-type patches at index construction time, ensuring that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to score high in a shared embedding space but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\\n\\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559). The corpus is annotated against the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4); the Multiple Bugs sub-types (double/triple/quadruple) are not applicable to single-fix commit pairs in the retrieval corpus and are excluded from corpus annotation but evaluated separately in the DebugBench test set.\\n\\nCorpus Quality Confound (Explicit). The natural 3,050-pair corpus differs from ReinFix's 100K TRANSFER corpus in two simultaneous dimensions: (1) retrieval architecture (soft joint embedding vs. hard type partition) and (2) corpus quality (natural issue-tracker/CI bug-fix pairs vs. synthetic static-analysis-derived pairs). Intra-corpus ablations — FTCR vs. re-implemented ReinFix-style baseline using text-embedding-3-large on the identical 3,050-pair natural corpus — test the partitioning hypothesis cleanly and are the primary experimental contribution. Absolute performance comparisons against published ReinFix numbers on Defects4J reflect both architecture and corpus quality simultaneously; they are presented as joint-effect comparisons, not as clean head-to-head architectural wins. The random-partition control (Variant F) further isolates type-matching precision from pool-size reduction within the intra-corpus comparison.\\n\\nCorpus Sparsity Policy. Each pair is annotated with one of 14 single-fault minor sub-types via few-shot prompting; three annotation passes measure inter-run consistency. For the combined Python+Java corpus (~3,050 pairs, 14 active minor types), mean pairs per type is approximately ~218. For Java-only ablations (~559 pairs), types with fewer than 30 Java instances are merged into nearest-neighbor supercategories within the same major category (e.g., rare Syntax sub-types such as 'illegal separation' and 'illegal indentation' merged within Syntax — never across Syntax/Reference/Logic boundaries); Java ablation results are reported for the 4–6 resulting within-major-category merged groups that each exceed 50 instances, with merged categories explicitly labeled. Note that several Syntax sub-types (missing colons, illegal indentation) are Python-specific and may yield few or zero Java instances; these are expected to merge to the within-Syntax catch-all for Java ablations.\\n\\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound (~$5–15 total embedding cost). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific.\\n\\nType Classifier Calibration on DebugBench Ground Truth. A held-out 20% split (~851 instances) directly measures few-shot classifier precision and recall per minor sub-type against oracle ground-truth labels, yielding X% at the minor-type level (major-type aggregation reported as a secondary result). The primary repair evaluation uses single-bug instances from the Syntax, Reference, and Logic major categories (~2,035 of 4,253 instances); Multiple Bugs instances (double/triple/quadruple, ~2,218 instances) are evaluated separately as an auxiliary experiment to characterize classifier behavior on multi-type ambiguous queries. Cross-dataset zero-shot agreement on ~56 human-verified Java pairs yields Y%. These produce the core NLP finding: LLM-inferred bug type labels achieve X% agreement with DebugBench ground truth (Python/C++) at the minor-type level, transfer zero-shot to Java with Y% agreement, and predict retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs (both aggregate across all instances of each class, McNemar's test, 95% CI).\\n\\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect, the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index (Variant F). Any performance gap between FTCR (Variant E) and this control measures the precision benefit of type-matching net of pool-size reduction.\\n\\nConfidence-Gated Retrieval Fallback. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval. Six variants evaluated: (A) text-similarity RAG, (B) RELREPAIR, (C) RepoRepair, (D) ReinFix-style soft on same corpus, (E) FTCR@hard-all, (F) random-partition control. Confidence-gated hybrid evaluated as a seventh configuration. Precedent: CRAG (Yan et al., arXiv:2401.15884).\\n\\nPractical Utility. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is the retrieval contribution in isolation, not a pipeline SOTA claim. DynaFix demonstrates retrieval and execution augmentation are independently improvable axes; an improved retrieval module (FTCR vs. ReinFix-style) compounds with execution-level improvements. Standalone evaluation isolates the retrieval hypothesis cleanly.\\n\\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while Defects4J V1.2 (MVS) and SWE-bench Lite (full version) validate real-world transfer.\",\n  \"resource_estimate\": {\n    \"auto_research\": {\n      \"gpu_hours\": \"~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)\",\n      \"gpu_utilization\": \"near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants\",\n      \"ablation_scope\": \"Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline on same natural corpus), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (4-major coarse / 14-minor single-fault fine / merged-Java within-major), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java → SWE-bench-Lite Python), classifier accuracy stratification by confidence band\",\n      \"timeline\": \"10-14 days with 2 A100 nodes running in parallel — the ONLY constraint-compliant execution mode for the 16-day hard budget. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) both violate the user's timeline constraint and are not presented as viable paths.\",\n      \"day_by_day_schedule\": \"Day 0 (May 10): setup and corpus annotation launch. Compute confirmed: 2 A100 nodes provisioned; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested. Day 1–3 (May 11–13): annotation + DebugBench classifier calibration (X% minor-type level, Y%). Day 4–6 (May 14–16): index construction + Defects4J V1.2 ablations (Variants A/D/E/F) + pre-drafted paper skeleton. Day 7–9 (May 17–19): DebugBench evaluation (single-bug instances) + confidence stratification (Z%, W% aggregate with McNemar's test) + SWE-bench Lite launch. Day 10–12 (May 20–22): CodeBERT ablation + granularity + k-sweep. Day 13 (May 23): results compilation + paper skeleton. Day 14–15 (May 24–25): paper finalization + ARR submission.\",\n      \"team\": \"0 (initial ~4h setup for corpus pipeline, per-type sub-index construction, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)\",\n      \"claude_api_cost\": \"$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)\",\n      \"embedding_api_cost\": \"~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)\",\n      \"estimated_gpu_cost\": \"~$969 (323 A100-hours × $3/h)\",\n      \"speed_bottleneck\": \"GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls\",\n      \"risk_note\": \"SWE-bench Lite may not complete before Day 12; MVS for EMNLP Findings submission is DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control, achievable within the 10–14 day window. Compute pre-provisioned as of Day 0. Auto-assigned bug type labels may drift without the three-pass consistency check; confidence-gated hybrid adds hyperparameter τ requiring tuning on held-out split before SWE-bench evaluation. Two-day paper writing window (Days 13–15) requires pre-drafted skeleton prepared during Days 4–6.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings (via ARR, deadline May 25, 2026 11:59 PM AoE — PRIMARY TARGET; 15 days from today). The X%/Y%/Z%/W% calibration study — measuring LLM-generated bug type label quality and its downstream impact on retrieval-augmented repair — is appropriate for EMNLP Findings, which publishes solid empirical contributions that advance understanding of specific NLP phenomena. The Main track expects findings that advance understanding of language models at a deeper architectural or representational level and poses higher desk-rejection risk for an empirical calibration study; Findings is the correct target and the proposal commits to it without oscillation. Path: auto-research completes Days 0–12 (May 10–22); paper writing Days 13–15 (May 23–25). Minimum viable submission: DebugBench classifier calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. EMNLP Findings fits the paper's core contribution: LLM annotation reliability for a structured classification task and the downstream retrieval consequences of label noise — a contribution to the NLP literature on LLM-generated categorical labels and RAG system design. Timeline is extremely tight: the two-day writing window requires a pre-drafted paper skeleton prepared concurrently with Days 4–6 experiment setup. Risk: if SWE-bench Lite does not complete by Day 12, the EMNLP Findings version covers DebugBench + Defects4J only, with SWE-bench Lite results added in the ICSE 2027 version.\",\n    \"ICSE 2027 (mandatory abstract deadline June 23, 2026 — BACKUP venue if EMNLP ARR cycle overlaps unfavorably or EMNLP Findings submission is not accepted). SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation; InferFix paragraph establishes LLM-inferred vs. Infer-required type labels as the untested dimension; TypeRepair comparison clarifies FTCR's orthogonal contribution of cross-repository retrieval; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections; intra-corpus confound framing converts the corpus quality issue into a feature rather than a weakness.\",\n    \"FSE 2027 (full paper deadline October 2, 2026 — tertiary backup if both EMNLP and ICSE review cycles are unfavorable).\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"InferFix: End-to-End Program Repair with LLMs over Bug-Specific Retrieval (ESEC/FSE 2023, arXiv:2303.07263) [earliest type-conditioned cross-repository repair retrieval; Retriever pretrained via contrastive learning using same-type bug-fix pairs as positives and different-type pairs as negatives (type from Infer static analysis); encoder encodes only buggy code — type structures training pairs but is NOT an explicit encoder input; the retriever learns type-correlated semantic similarity; at retrieval time, candidates are filtered to same-type fixes using Infer-derived labels; achieves 76.8% Java top-1 accuracy; InferFix validates type-conditioned retrieval but requires Infer static analysis at both corpus construction and query time — FTCR's scientific contribution vs. InferFix is testing whether LLM-inferred labels can substitute for Infer-derived labels (X%/Y%) and enabling type-conditioned retrieval for general natural bugs Infer cannot detect; must differentiate: (a) Infer-required labels vs. LLM-inferred labels; (b) query-time type filtering vs. FTCR's construction-time index partitioning; (c) Infer-specific diagnostic IDs vs. 4-major/18-minor natural-bug taxonomy; (d) InferredBugs vs. natural issue-tracker/CI bug-fix pairs]\",\n    \"ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; soft root-cause augmentation using unified vector database with text-embedding-3-large; intra-corpus comparison (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) is the clean architectural test; absolute comparisons against published ReinFix numbers reflect corpus quality confound and are presented as such]\",\n    \"SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; 73.0% SWE-bench Verified with Claude 4 Sonnet; agentic, Python-only; differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, multi-language scope]\",\n    \"TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J/QuixBugs (Java-only); validates that type conditioning improves LLM repair; Stage 3 context selection draws from within-project code files, not external cross-repository corpus — differentiation supported by evaluation design (project-internal datasets, no external corpus described in benchmark setup); FTCR's orthogonal contribution is type-conditioned retrieval from external ~3,050-pair cross-language corpus]\",\n    \"What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond (Gu et al., ICSE 2026, arXiv 2503.20589) [similar-code retrieval degrades code generation by up to 15% on CoderEval/RepoExec while structured knowledge helps; motivates type-partition fix-patch retrieval as avoiding the similarity-noise trap; note: code generation study, not repair — applicable as indirect motivation]\",\n    \"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330) [algorithm-type-conditioned retrieval in competitive programming — conceptual ancestor scoped to algorithmic tags]\",\n    \"RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors (ICSME 2024, Hao et al.) [type-specific retrieval for Python type errors only — FTCR extends to 18 minor sub-types and 3 languages]\",\n    \"DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv 2512.24635) [surpasses ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; demonstrates retrieval and execution augmentation are independently improvable axes]\",\n    \"DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2604.19305) [295 Defects4J bugs with DeepSeek-V3; updates landscape but orthogonal — no retrieval augmentation]\",\n    \"D4C: Aligning the Objective of LLM-based Program Repair (ICSE 2025, arXiv 2404.08877) [180 Defects4J bugs via objective alignment; updates performance landscape]\",\n    \"M-RAG: Reinforcing Large Language Model Performance through Retrieval-Augmented Generation with Multiple Partitions (ACL 2024, arXiv 2405.16420) [multi-partition RAG: +11% summarization, +8% translation, +12% dialogue; principled precedent for partition-based retrieval across domains]\",\n    \"RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code (arXiv 2509.16701) [project-internal retrieval baseline]\",\n    \"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048) [documentation-guided localization baseline; 45.7% SWE-bench Lite]\",\n    \"DebugBench: Evaluating Debugging Capability of Large Language Models (ACL Findings 2024) [primary evaluation; ground-truth 4-major/18-minor hierarchical taxonomy: Syntax (7 sub-types: misused ==/=, missing colons, unclosed parentheses, illegal separation, illegal indentation, unclosed string, illegal comment), Reference (4 sub-types: faulty indexing, undefined objects, undefined methods, illegal keywords), Logic (4 sub-types: condition error, operation error, variable error, other error), Multiple Bugs (3 sub-types: double/triple/quadruple co-occurring bugs); 4,253 instances across C++/Java/Python; held-out 20% split (~851 instances) for classifier calibration (X%) at minor-type level; primary repair evaluation on single-bug major categories (Syntax/Reference/Logic, ~2,035 instances); Multiple Bugs treated as separate analysis; acknowledged synthetic-bug limitation]\",\n    \"GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; cross-lingual transfer calibration (Y%)]\",\n    \"SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025, arXiv 2504.21798) [50k Python task instances; scale corpus for Python retrieval index]\",\n    \"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey; confirms retrieval augmentation as key enhancement; no type-partitioned cross-language system identified; cites InferFix as a key retrieval-augmented approach]\",\n    \"What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]\",\n    \"PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]\",\n    \"RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]\",\n    \"CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism; precedent for FTCR confidence-gated hybrid; cite as preprint — withdrawn from ICLR 2025, unpublished]\"\n  ],\n  \"description\": \"FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft type-conditioned retrieval (ReinFix's root-cause embedding approach, ICSE 2026) for cross-repository fix template transfer, while LLM-inferred type labels can substitute for the Infer-required labels used by InferFix (ESEC/FSE 2023) to enable type-conditioned retrieval on general natural bugs. The primary NLP contribution — targeted at EMNLP 2026 Findings (via ARR, May 25, 2026) — is a complete causal decomposition parameterized by four falsifiable quantities measured at the minor-type level of DebugBench's 4-major/18-minor hierarchical taxonomy: (X%) few-shot LLM classifier accuracy vs. DebugBench ground-truth oracle labels at the minor-type level (major-type aggregation as secondary); (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline (aggregate, McNemar's test, 95% CI); (W%) repair degradation for misclassified instances (aggregate, McNemar's test, 95% CI). Together these characterize when hard categorical type conditioning helps and when it hurts, generalizing to any system using LLM-inferred categorical labels for retrieval routing. FTCR's structural departure from ReinFix is to (1) classify incoming failures into one of the 14 single-fault minor sub-types, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable in a clean intra-corpus comparison. Round 7 revisions address five issues: (a) EMNLP FINDINGS COMMITTED — target_venues now lists 'EMNLP 2026 Findings (via ARR)' as the sole EMNLP target; the X%/Y%/Z%/W% calibration study is appropriate for Findings, not Main; the oscillation between Main and Findings is resolved with a committed rationale. (b) DEBUGBENCH HIERARCHY CORRECTED — all references to '18-category taxonomy' replaced with '4-major/18-minor hierarchical taxonomy' (4 major: Syntax/7 sub-types, Reference/4, Logic/4, Multiple Bugs/3); primary repair evaluation scoped to single-bug instances (Syntax/Reference/Logic, ~2,035 of 4,253); Multiple Bugs (~2,218 instances, 52%) treated as separate analysis; merge policy now operates within-major-category-first (e.g., rare Syntax sub-types merged within Syntax, never across Syntax/Reference/Logic); X%/Y%/Z%/W% measured at minor-type level with major-type aggregation as secondary; per-minor-type Java instance estimate revised to ~40 per single-fault minor type for Java-only ablations. (c) COMPUTE READINESS CONFIRMED — Day 0 entry now states: '2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.' (d) INFERFIX ARCHITECTURE CORRECTED — the 'soft continuous embedding feature' characterization was inaccurate; InferFix's encoder learns type-correlated semantic similarity (type structures contrastive training pairs but is not an explicit encoder input); InferFix does filter retrieval candidates by type at query time using Infer-derived labels; FTCR's primary differentiation from InferFix is reframed as (i) type label acquisition: LLM classification vs. Infer static analysis required; (ii) taxonomy: 4-major/18-minor general natural-bug taxonomy vs. Infer-specific diagnostics; (iii) corpus: natural bug-fix pairs vs. InferredBugs; the empirical question vs. InferFix is now correctly stated as 'can LLM-inferred labels substitute for Infer-derived labels at sufficient accuracy (X%) to enable effective type-conditioned retrieval?'. (e) STATISTICAL SIGNIFICANCE SPECIFIED — Z%/W% reported as aggregate rates; McNemar's test on paired pass/fail outcomes; Fisher's exact test for per-type breakdowns (n≥30 threshold); 95% confidence intervals for Z% and W%.\",\n  \"project_name\": \"failure_type_rag_repair\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Uncited competing work invalidates novelty claim: ReinFix (ICSE 2025, arXiv 2506.23100) embeds root-cause classification into retrieval from a 1M-pair historical bug-fix corpus, which is mechanistically nearly identical to FTCR's type-conditioned retrieval from historical corpus. The proposal must cite and differentiate from ReinFix; without this, reviewers will reject on novelty grounds.\", \"CRITICAL — ReCode overlap is underplayed: ReCode already implements algorithm-type-conditioned retrieval with type-partitioned sub-knowledge-bases, the identical core mechanism. FTCR's contribution is extending this to real-world bugs (competitive programming → repositories), which must be framed more precisely. The current framing overclaims novelty.\", \"HIGH — Dataset size claim is internally inconsistent: BugsInPy (493) + Defects4J (1,192) = ~1,685 pairs, not 6,500. If the SWE-bench training split (19,000 instances) is included, that's 20,000+. The '~6,500' figure suggests some undescribed quality-filtering or subsetting logic that is not specified in the proposal. This will raise red flags in review.\", \"HIGH — Defects4J reproducibility crisis: Independent studies (MSR 2025) found ~50% of Defects4J fault-triggering tests are regression tests added post-hoc, and nearly 50% become non-reproducible with modern Java. BugsInPy showed 67% reproducibility. Mining ~1,685 pairs from these datasets may yield fewer than 900 reliably reproducible bug-fix pairs, undermining the corpus quality and scale claims.\", \"MEDIUM — Uncited prior art RetypeR (ICSME 2024): This paper applies type-specific retrieval (external retrieval stage conditioned on Python type errors) and should be discussed as prior art that narrows the novelty of cross-language type-conditioned retrieval.\", \"MEDIUM — Resource units inconsistency: The hard constraint is ≤200 H100-hours, but the proposal reports A100-hours throughout. Manual mode (~150 A100h ≈ 90 H100h) is within budget, but auto-research mode (~650 A100h ≈ 390 H100h) significantly exceeds the constraint. This should be flagged and the primary experiment budget anchored in H100-hours.\", \"MEDIUM — EMNLP framing needs NLP-centric repositioning: The primary contribution is a retrieval system design (SE contribution). EMNLP 'NLP and Code Models' track requires a clear NLP/LLM contribution. The few-shot taxonomy induction approach and its ability to generalize zero-shot across languages should be foregrounded as the NLP contribution; the retrieval architecture is the engineering substrate.\", \"LOW — DebugBench validity concern: DebugBench uses LeetCode code with GPT-4-implanted synthetic bugs, not real repository bugs. Results on DebugBench may not transfer to SWE-bench Lite, requiring a careful discussion of the domain gap between the two evaluation settings.\"]\nFeedback: The core gap FTCR targets is real but narrower than claimed. To make this revisable into a strong paper: (1) Reframe the novelty around what's genuinely new — the extension of type-partitioned retrieval from algorithmic contest code (ReCode) to real-world multi-language repository bugs with an 18-category taxonomy grounded in DebugBench's empirically validated type structure. This is a specific, defensible contribution. (2) Add ReinFix as a baseline: since ReinFix uses root-cause-conditioned retrieval from historical corpus, you must compare against it directly on a shared benchmark (Defects4J is common). If FTCR's type-partitioned index outperforms ReinFix's joint root-cause+code embedding, that's a publishable finding. (3) Fix the dataset size: either restrict to BugsInPy+Defects4J and acknowledge the smaller corpus (~1,500–1,685 pairs after reproducibility filtering), or explicitly include a quality-filtered SWE-bench train subset and describe the filtering criteria. (4) Run a reproducibility pre-check: before committing to Defects4J as a corpus source, filter to only Java 8-compatible bugs (reported to have ~80% reproducibility) and report the usable fraction. (5) For EMNLP fit, pivot the NLP angle to the few-shot taxonomy induction finding — specifically, whether LLM-inferred bug types are consistent, cross-lingual, and predictive of repair success. This is the NLP scientific question. (6) The 16-day timeline is only viable in auto-research mode with parallel evaluation; the paper should scope evaluation to DebugBench (where type labels are ground-truth) plus SWE-bench Lite (300 instances), and acknowledge that a full Defects4J corpus build is out-of-scope for the conference timeline.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Citation error: ReinFix is confirmed ICSE 2026 (arXiv 2506.23100 states 'Accepted by ICSE 2026'), not ICSE 2025 as the proposal states throughout. EMNLP 2026 explicitly warns against hallucinated citations and has stated it may desk-reject papers with such errors. Every reference to 'ReinFix (ICSE 2025)' must be corrected to 'ReinFix (ICSE 2026)'.\", \"HIGH — Corpus sparsity renders type partitioning semantically degenerate for rare types: 559 Java pairs (Defects4J + GitBug-Java) across 18 types yields ~31 Java instances per type on average. For rare bug categories (concurrency, resource leaks, format errors), this may be 5–15 instances. Retrieving k=5 from a sub-index of 15 instances is not retrieval—it is exhaustive lookup. The proposal must either (a) restrict to the 6–8 most frequent types where >50 Java instances exist, or (b) merge rare types into a broader category, or (c) acknowledge that the per-type ablation is only meaningful for the top N types and report per-type corpus sizes in the paper.\", \"HIGH — Classifier error propagation is unaddressed: if the type classifier misclassifies an incoming bug (which will occur for edge cases and multi-type bugs), the system retrieves from the wrong partition and almost certainly underperforms soft retrieval for those instances. This is the main structural risk of hard partitioning over soft embedding. The proposal must analyze: (a) classifier accuracy on held-out annotated bugs, (b) the performance degradation attributable to misclassification, and (c) whether a confidence-gated fallback to soft retrieval recovers performance.\", \"HIGH — EMNLP venue fit remains questionable: the core contribution is an IR architecture decision (partitioning a FAISS index by categorical label). EMNLP 'NLP and Code Models' reviewers will ask what the NLP/LM finding is. The 'few-shot cross-lingual taxonomy induction' contribution (measuring whether LLM-inferred bug types are consistent across annotation runs) is secondary and not a compelling standalone NLP finding—LLM classification consistency is well-studied. If submitting to EMNLP, the NLP contribution must be foregrounded more strongly, e.g., a finding that LLM-inferred type labels are cross-lingually stable and predictive of repair success at the p<0.01 level, with analysis of failure cases that reveal type-specific linguistic patterns in bug descriptions.\", \"MEDIUM — ASE 2026 NIER deadline (May 12) is 2 days from today and experiments are not done: listing it as a target venue is unrealistic. Remove from target_venues or replace with a venue with a later deadline (e.g., EMNLP Findings via ARR, or FSE 2027).\", \"MEDIUM — No expected performance range stated for SWE-bench Lite: reviewers will immediately compare against the RepoRepair baseline (45.7% on Lite). The proposal should state an expected performance range and justify why a lower absolute number is acceptable given the paper's focus on architectural comparison rather than SOTA performance.\", \"LOW — The proposal does not specify which encoding model will be used for FTCR. ReinFix uses text-embedding-3-large (OpenAI API). If FTCR uses the same encoder for fair comparison, this imposes an ongoing API cost not captured in the GPU-hour budget. If using CodeBERT or UniXcoder instead, the encoder comparison is confounded with the hard/soft partitioning comparison. This should be clarified explicitly.\"]\nFeedback: The Round 2 revision has fixed the major structural issues from Round 1 (ReinFix is now a baseline, dataset sizes are consistent, RetypeR is cited, compute is in H100-hours, DebugBench limitations acknowledged). The core hypothesis is testable and the ablation design is clean. Three issues must be addressed before this is submission-ready: (1) Fix the citation error throughout — ReinFix is ICSE 2026, not ICSE 2025; submit it as 'ReinFix (ICSE 2026, arXiv:2506.23100)'. (2) Address corpus sparsity directly in the methods section: report per-type instance counts in a table, restrict the full 18-type analysis to the Python+Java combined corpus, and for the Java-only ablations acknowledge that only the top N types have >50 instances. For types below a minimum threshold (suggest 30 instances), either merge or exclude from per-type breakdown. (3) Add a classifier accuracy analysis: measure the type classifier on the annotated DebugBench ground-truth labels (since DebugBench already has ground-truth types, you can directly measure LLM classifier accuracy), then report how type-matched retrieval performance varies as a function of classifier confidence. This turns the error propagation problem into a feature — it becomes an analysis of when hard partitioning helps vs. hurts. For EMNLP specifically: the NLP contribution must be stated as a crisp finding, not a process. Frame it as: 'We show that LLM-inferred bug type labels achieve X% agreement with DebugBench ground-truth labels, transfer zero-shot to unseen Java bugs with Y% agreement, and are predictive of retrieval-augmented repair success (type-matched retrieval outperforms soft retrieval by Z% for correctly classified bugs, while underperforming by W% for misclassified bugs).' This is a falsifiable empirical claim that EMNLP reviewers can evaluate.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL — CRAG citation is a hallucinated venue: The proposal cites 'CRAG (ICLR 2024)' but CRAG (arXiv:2401.15884) was submitted to ICLR 2025 and withdrawn — it was never accepted or published at any ICLR. Citing it as a published ICLR paper is precisely the kind of hallucinated venue citation EMNLP warns may trigger desk rejection. The correct citation is 'CRAG (Yan et al., 2024; arXiv:2401.15884)'.\", \"HIGH — Unacknowledged concurrent work: SWE-Exp (arXiv:2507.23361, July 2025) uses an experience bank where retrieval explicitly surfaces 'the top N=10 issues most relevant in terms of error type' via cosine similarity, achieves 41.6% on SWE-bench Verified, and is publicly available with open-source code. While the mechanism is different (experience trajectories + soft cosine vs. hard categorical partitioning of fix templates), EMNLP and ICSE reviewers will notice its absence. FTCR must cite it, note the difference (soft type-similarity vs. hard categorical partitioning), and explain why hard partitioning is a distinct hypothesis worth testing.\", \"MEDIUM — 'Clean comparison' overstates the isolation: Type-partitioned retrieval fundamentally reduces the effective retrieval corpus to 1/N_types (≈1/18 on average) of the full index. A smaller retrieval pool affects recall independently of the type-matching benefit. Without a 'random-partition baseline' (random corpus subsets of equivalent size per query), the observed gain (or loss) conflates two effects: (a) partitioning precision and (b) retrieval corpus size. The proposal should either add this control or explicitly acknowledge it as a confound in Section 4.\", \"MEDIUM — EMNLP main track fit remains overstated: The NLP contribution — measuring X% agreement between LLM-inferred bug type labels and DebugBench ground truth, then correlating with repair success — is a measurement finding about LLM classification reliability on a well-structured taxonomy. This is useful but unlikely to be viewed as a primary NLP/LM contribution by EMNLP main track reviewers, who expect findings that advance understanding of language models. EMNLP Findings is a more realistic target; ICSE 2027 (already listed) is the natural primary venue where the SE audience will value the retrieval architecture contribution directly.\", \"LOW — Minor ReinFix technical inaccuracy: The proposal states ReinFix uses 'a unified FAISS vector store' but the ReinFix paper (arXiv:2506.23100) only refers to 'a vector database' without specifying FAISS as the implementation. This overly specific characterization of the baseline's internals should be softened to 'a unified vector database' to avoid misrepresentation of the primary baseline.\"]\nFeedback: Round 3 has successfully addressed the four critical/high issues from Round 2: citation corrected to ICSE 2026 throughout, corpus sparsity handled with explicit per-type table and 30-instance merge policy, classifier error propagation addressed with confidence-gated hybrid and DebugBench calibration, and EMNLP framing sharpened to a crisp X%/Y%/Z%/W% falsifiable claim. The core hypothesis is testable and genuinely novel for multi-language APR. Two issues block submission: (1) Fix the CRAG citation immediately — replace every instance of 'CRAG (ICLR 2024)' with 'CRAG (Yan et al., 2024; arXiv:2401.15884)'. CRAG was submitted to ICLR 2025 but withdrawn and unpublished; citing it as published ICLR work is a hallucinated venue citation that can trigger desk rejection at EMNLP. (2) Add SWE-Exp (arXiv:2507.23361) to the landscape with one paragraph: it uses soft cosine retrieval filtered 'in terms of error type' from an experience bank; FTCR's departure is hard categorical partitioning at index-construction time, not just retrieval-time filtering, plus fix-template retrieval rather than trajectory experience. For longer-term strengthening: add a random-partition baseline (randomly assign corpus pairs to N equivalent-sized sub-indices) to isolate the type-matching benefit from the corpus-size effect. This single ablation converts the comparison from 'clean but contested' to 'rigorous and unambiguous'. On venue strategy: ICSE 2027 (abstract June 23) should be positioned as the primary target; EMNLP 2026 ARR (May 25) can be attempted for Findings if the NLP framing holds, but do not overinvest in EMNLP main track positioning — the primary audience for this work is the SE/APR community.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"HIGH — Uncited concurrent work: 'Towards Defect-Type-Aware Adaptive Program Repair' (TypeRepair, Zhang et al., Software Quality Journal 2026, link.springer.com/article/10.1007/s11219-026-09751-w) uses explicit defect type identification before context selection in a 4-stage pipeline (localization → type ID → context selection → patch generation) on Defects4J V1.2/V2.0 and QuixBugs, independently achieving 272% improvement over GPT-3.5 baseline. The paper must be obtained, read, and cited: if 'context selection' uses type-conditioned retrieval from a cross-repo external corpus (which cannot be confirmed from the abstract alone due to paywall), the overlap with FTCR is substantial and reviewers will notice its absence. If TypeRepair uses only within-project context, that is FTCR's key differentiation and must be stated explicitly.\", \"HIGH — Unaddressed counterevidence: 'What to Retrieve for Effective Retrieval-Augmented Code Generation?' (ICSE 2026, arXiv 2503.20589) empirically shows that retrieving syntactically similar code snippets degrades performance by up to 15% compared to retrieving in-context examples and API information. This is a direct challenge to FTCR's premise: if type-partitioned retrieval returns syntactically similar-but-wrong-level-of-abstraction fixes within each partition, it may concentrate rather than reduce this noise. The authors must address this finding — either by arguing that semantic type partitioning selects at a different abstraction level than syntax similarity, or by adding an experiment measuring within-type fix template quality vs. cross-type.\", \"MEDIUM — Practical utility framing missing: FTCR projects 20–35% on SWE-bench Lite while SWE-Exp achieves 73% on SWE-bench Verified and RepoRepair achieves 45.7% on Lite. ICSE 2027 reviewers will ask why the retrieval strategy matters in isolation when execution-augmented agentic methods dominate. The paper needs an explicit 'why retrieval strategy matters' argument: e.g., (1) retrieval modules are independently upgradeable components within agentic systems — DynaFix adds execution feedback orthogonally to retrieval, so a better retrieval module improves the whole pipeline; (2) the 20–35% baseline is specifically the retrieval contribution, not the full agentic ceiling. This argument exists implicitly but must be stated explicitly.\", \"LOW — EMNLP 2026 ARR deadline is not credible given current state: The May 25 deadline is 15 days away. To submit to ARR requires a complete written paper, full experimental results, and bibliography validation (EMNLP's hallucinated-citation warning is explicit). The paper's hedge ('if too close, defer') should be changed to a definitive decision: either commit to running minimum viable experiments starting immediately (DebugBench classifier calibration + Defects4J V1.2 with the 4 primary variants) or acknowledge ICSE 2027 as the sole target. Leaving it ambiguous signals poor project planning to co-authors and advisors.\"]\nFeedback: Round 4 has successfully resolved all five issues from Round 3: CRAG citation is correct (arXiv-only), SWE-Exp is cited with three clear design differences, the random-partition control (Variant F) converts the corpus-size confound into a closed experimental question, EMNLP is downgraded to Findings, and ReinFix's implementation detail is softened. Independent verification confirms all cited paper claims are accurate. The hard-vs-soft retrieval comparison for semantic bug-type partitioned cross-repo repair is genuinely novel — no existing paper makes this specific comparison. Two actions are required for Round 5: (1) Read the TypeRepair SQJ 2026 paper (Zhang et al., doi:10.1007/s11219-026-09751-w) and add it to the landscape — the differentiation is either that TypeRepair uses intra-project context (state this explicitly) or that it uses cross-repo retrieval but covers only Java with a different pipeline structure (then FTCR's C++/Java/Python scope and the hard/soft comparison are the differentiators). (2) Cite and respond to 'What to Retrieve for Effective RAG Code Generation?' (ICSE 2026, arXiv:2503.20589): its finding that similar code retrieval degrades performance by 15% motivates FTCR's type-conditioning exactly — within a type partition, retrieved examples share fix structure rather than surface-level code similarity, which is the argument FTCR needs to make explicit. These two additions would resolve the remaining novelty and counterevidence gaps. The practical utility framing (retrieval as a modular component upgradeable within agentic pipelines) should be added as a paragraph in the introduction — this is the clearest answer to 'why does this matter when agentic methods dominate at 73%.'\n\n### Round 5 review\nVerdict: revise\nIssues: [\"CRITICAL — Target venue violates user requirements: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026, 15 days from today). The proposal now targets ICSE 2027 (abstract June 23, 2026) exclusively, a full year late and a different research community. Previous reviewers flagged EMNLP as infeasible given experiment state, but the requirement was not to change venues — it was to make the idea work within the constraint. If auto-research starts immediately (day 0), 10–14 days of experiments complete by ~May 23, leaving 2 days to finalize the paper for the May 25 ARR deadline. This is technically achievable but requires an explicit, committed execution plan with the NLP framing (X%/Y%/Z%/W% classifier calibration finding) as the lead contribution. The proposal must either restore EMNLP 2026 as the primary target with a day-by-day execution schedule, or explicitly acknowledge that it fails the user's venue constraint and accept that verdict.\", \"HIGH — 16-day timeline constraint met only by auto-research mode: The user's hard constraint is ≤16 days. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) exceed this by 8–12× and should not appear as viable execution paths in resource_estimate. The paper should flag auto-research (10–14 days) as the only constraint-compliant mode, or restructure the three modes to reflect feasible timelines.\", \"MEDIUM — InferFix (ESEC/FSE 2023, arXiv:2303.07263) is unmentioned prior art: Independently confirmed that InferFix uses bug type annotations and contrastive learning to retrieve 'semantically equivalent bugs and corresponding fixes of the same bug type' from an external repository corpus (InferredBugs, thousands of Java and C# repos). This is the closest non-trivial precursor to type-conditioned cross-repo repair retrieval and is not cited anywhere in the proposal. ICSE 2027 reviewers familiar with the APR literature will notice its absence. FTCR should differentiate explicitly: InferFix uses soft contrastive similarity (learned embedding grouping) not hard categorical index partitioning; it targets Java/C# from Infer static analysis findings, not the 18-category natural-bug taxonomy; and the corpus construction and evaluation differ. This differentiation is achievable in one paragraph but must be present.\", \"MEDIUM — Cross-system corpus quality confound inadequately flagged: The 'clean comparison' correctly uses the same 3,050-pair natural corpus for both FTCR and the ReinFix-style baseline, isolating partitioning as the variable. But any performance comparison against the published ReinFix results uses 100K TRANSFER corpus pairs (synthetic, from static analysis), creating a corpus quality × retrieval architecture confound that the random-partition control does not address. The paper must explicitly state: (a) intra-corpus ablations (FTCR vs. re-implemented ReinFix on 3,050 pairs) test the partitioning hypothesis cleanly, and (b) absolute comparisons against published ReinFix results reflect both architecture and corpus quality differences simultaneously.\", \"LOW — TypeRepair context-selection scope unverifiable from publicly accessible sources: The critical differentiation claim — that TypeRepair's Stage 3 selects within-project context only, not from an external cross-repo corpus — could not be independently confirmed due to paywall access to the SQJ article. The proposal states this confidently; it should note the evidentiary basis (e.g., 'TypeRepair evaluates exclusively on Defects4J/QuixBugs, which are within-project datasets, and the paper's supplementary prompt templates confirm type-specific in-project context selection rather than external retrieval') to avoid a reviewer flagging this differentiation as unsubstantiated.\"]\nFeedback: This is the most polished version of FTCR to date. The random-partition control, confidence-gated hybrid, per-type merge policy, and ReinFix/SWE-Exp/TypeRepair differentiation all reflect genuine methodological rigor. Two actions would bring this to pass: (1) VENUE DECISION — the proposal must choose one of two paths and commit fully: either (a) restore EMNLP 2026 ARR (May 25) as the primary target with a specific day-by-day execution schedule (day 0-13: auto-research runs corpus annotation + DebugBench classifier calibration + Defects4J V1.2 ablations; day 13-15: paper writing with NLP lead framing the X%/Y%/Z%/W% falsifiable classifier finding), acknowledging the extreme timeline pressure; or (b) explicitly declare that the user's requirement cannot be met for EMNLP 2026 and accept ICSE 2027 as the sole target with a verdict of 'fail' on the original requirement. Leaving both venues while targeting neither by the May 25 deadline is a planning failure. (2) ADD INFERFIX — one paragraph in the landscape: 'InferFix (ESEC/FSE 2023, arXiv:2303.07263) retrieves fixes for bugs of the same type using contrastive-learned embeddings over bug type annotations, establishing type-aware retrieval for Java/C# static analysis bugs. FTCR differs in three respects: (a) hard categorical index partitioning at construction time rather than soft contrastive similarity at retrieval time; (b) 18-category natural-bug taxonomy across C++/Java/Python rather than InferBugs' Infer-specific defect categories; (c) direct comparison of hard vs. soft type conditioning as the scientific contribution.' If these two issues are resolved, the novelty and feasibility scores reach 3.5+ and the paper is close to a pass for ICSE 2027 (though not EMNLP 2026 unless the execution plan is credible).\n\n### Round 6 review\nVerdict: revise\nIssues: [\"HIGH — EMNLP Main vs. Findings target ambiguity persists: target_venues now lists 'EMNLP 2026 Main' AND 'EMNLP 2026 Findings' as separate entries, but the empirical calibration study (X%/Y%/Z%/W% LLM label reliability) is a measurement finding about LLM annotation quality — appropriate for EMNLP Findings, not the Main track, which expects findings that advance understanding of language models at a deeper level. Rounds 3 and 4 both explicitly downgraded the EMNLP target to Findings; Round 5 asked to restore EMNLP without specifying Main vs. Findings; Round 6 silently re-expanded to Main. The proposal must commit to EMNLP Findings as the EMNLP target and stop oscillating. Trying for Main and being desk-rejected wastes the submission cycle.\", \"MEDIUM — DebugBench hierarchical structure mischaracterized throughout: independently verified (ACL Findings 2024 paper) that DebugBench has 4 MAJOR categories (Syntax Bugs, Logic Bugs, Reference Bugs, Multiple Bugs) with 18 MINOR sub-types nested within them — not 18 independent categories. The proposal consistently refers to '18-category taxonomy' and '18-category natural-bug taxonomy aligned with DebugBench's taxonomy.' This is inaccurate and will flag with any reviewer who has read DebugBench. Concretely: the merge policy for rare types must operate within the 4-major/18-minor hierarchy (merge within major categories first, not across them); X%/Y%/Z%/W% measurements must specify whether they are measured at the major-type or minor-type level; and the '~31 Java instances per type' figure implies 18 equal partitions, which is not how the benchmark is structured.\", \"MEDIUM — Day-0-today execution assumption is unverified: the schedule commits to launching corpus annotation pipeline on May 10 (today) with 2 A100 nodes already available. No verification of compute availability, API rate limits on day 1, or Defects4J V1.2 Docker environment readiness is mentioned. If infrastructure setup takes 1–2 days (common in practice), the already-tight 2-day paper writing window (Days 13–15, May 23–25) disappears entirely. The proposal should either (a) confirm that compute is already provisioned and Docker environments tested, or (b) revise the schedule to account for a 1-day setup buffer by shifting MVS deliverables earlier.\", \"LOW — InferFix type-as-embedding-signal claim needs precision: independent verification found that InferFix adds bug type annotations as prompt context alongside retrieved fixes, while the contrastive retriever learns semantic similarity between bugs/fixes. The proposal claims 'type influences embedding proximity rather than pool membership' — this framing appears broadly correct but needs verification against the actual retriever architecture section (Section 3 of arXiv:2303.07263), not just the abstract. If InferFix's retriever does NOT explicitly condition on type labels during encoding (only using type for post-retrieval prompt augmentation), the 'soft type conditioning' differentiation needs rewording to 'type-correlated semantic similarity' to avoid misrepresenting the baseline.\", \"LOW — Statistical significance for Z% and W% unstated: the Z% (repair improvement for correctly classified) and W% (repair degradation for misclassified) measurements will have unequal sample sizes depending on classifier accuracy. With ~31 Java instances per minor type and a 20% held-out split (~6 per type), per-type statistical tests are underpowered. The proposal should specify: (a) whether Z% and W% are aggregated across all types or reported per type; (b) what statistical test is used; (c) minimum sample threshold for a type to contribute to the Z%/W% comparison.\"]\nFeedback: Round 6 has addressed all five Round 5 issues: EMNLP venue restored with committed schedule, InferFix added with three-point differentiation, corpus confound made explicit, TypeRepair evidentiary basis stated, resource estimate stripped to auto-research only. The core hypothesis is well-posed and the experimental design is increasingly rigorous. Three targeted fixes would make this submission-ready: (1) COMMIT TO EMNLP FINDINGS — remove 'EMNLP 2026 Main' from target_venues and replace with 'EMNLP 2026 Findings (via ARR)'. The X%/Y%/Z%/W% calibration study is a strong Findings paper; attempting Main track risks desk rejection on NLP-contribution grounds and wastes the submission cycle. (2) FIX DEBUGBENCH STRUCTURE — replace every instance of '18-category' with '4-major/18-minor hierarchical taxonomy' and state that X%/Y%/Z%/W% measurements operate at the minor-type level (18 sub-categories), with major-type aggregation reported as a secondary result. Revise the merge policy to explicitly merge within the same major category first (e.g., merge rare Reference Bug sub-types before merging across Logic and Reference). (3) CONFIRM COMPUTE READINESS — add one sentence to the Day 0 entry: 'Compute: 2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.' If this cannot be stated truthfully, shift the MVS timeline by 1 day and compress paper writing to 1 day with a more aggressive pre-drafted skeleton policy. These three changes are low-effort and directly address verifiable gaps; the underlying science is solid and the proposal is close to submission-ready for EMNLP 2026 Findings.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:00:49.393Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:00:49.393Z",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116"
}
```

---

## Round 1

21 recorded events

### User

_source line 3 · 2026-05-10T07:00:49.422Z_

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

## Idea under review (round 7/10)
{
  "title": "Failure-Type-Conditioned Retrieval Augmentation for Repository Repair",
  "core_problem": "The lead empirical question — tractable because DebugBench provides oracle ground-truth labels for 4,253 instances organized in a 4-major/18-minor hierarchical taxonomy — is: how accurately can a few-shot LLM assign semantic bug type labels from the 18 minor sub-categories, and does that label accuracy determine whether hard categorical retrieval index partitioning outperforms soft root-cause-augmented retrieval (ReinFix, ICSE 2026) for cross-repository fix template transfer? This frames FTCR as an empirical study of LLM-generated categorical label quality and its downstream retrieval impact, yielding four falsifiable quantities: (X%) few-shot classifier accuracy vs. DebugBench ground-truth oracle labels at the minor-type level, with major-type aggregation as a secondary result; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type-partitioned retrieval vs. the soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts — a finding with direct generalization to any retrieval system using LLM-inferred labels.\n\nRetrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. InferFix (ESEC/FSE 2023, arXiv:2303.07263) establishes that type-conditioned retrieval benefits code repair: its Retriever uses contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type from Infer static analysis), and at retrieval time filters candidates to same-type fixes; however, InferFix requires running the Infer static analyzer on each query bug — applicable only to bugs Infer can detect, using Infer-specific diagnostic categories rather than a general natural-bug taxonomy. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is therefore two-fold: (1) whether LLM-inferred type labels can substitute for Infer-derived labels to enable type-conditioned retrieval for general natural bugs not addressable by static analysis (the X%/Y% question vs. InferFix); and (2) whether hard categorical type partitioning of the retrieval index outperforms ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer (the Z%/W% question). An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. Type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and become analytical contributions when addressed directly: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4; the Multiple Bugs sub-types are excluded from the fix-template corpus as multi-fault commits are rare and represent a different repair regime) yields approximately ~217 pairs per minor type on average for the full Python+Java corpus; for Java-only ablations (~559 pairs across ~14 types, ~40 per type), types with fewer than 30 instances are merged within the same major category (e.g., rare Syntax sub-types merged within Syntax; rare Logic sub-types merged within Logic — never across major categories); and (2) classifier error propagation — when an incoming bug is misclassified, hard partitioning underperforms soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback — turns potential weaknesses into the core empirical variables (Z% and W%) that define the paper's scientific contribution.",
  "opportunity": "ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-conditioned cross-repository retrieval system for code repair: its Retriever is pretrained via contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type labels from Infer static analysis), and at retrieval time filters candidates to same-type fixes using Infer-derived labels. The encoder itself encodes only the buggy code as a dense vector — type structures the contrastive training pairs but is not an explicit encoder input; the retriever learns type-correlated semantic similarity. InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#. Three properties distinguish InferFix from FTCR: (a) Type label acquisition — InferFix requires running the Infer static analyzer on each query bug to obtain its type label; only bugs Infer can detect are addressable; FTCR uses few-shot LLM classification, requiring no static analysis tooling and covering any natural bug that Infer cannot or would not detect; (b) Taxonomy scope — InferFix uses Infer-specific diagnostic IDs (null dereferences, resource leaks, thread-safety violations), not the 4-major/18-minor natural-bug taxonomy aligned with DebugBench (4 major categories: Syntax with 7 sub-types, Reference with 4 sub-types, Logic with 4 sub-types, Multiple Bugs with 3 sub-types); (c) Corpus — InferFix uses InferredBugs (Java/C# repos where Infer detected bugs); FTCR uses natural bug-fix pairs from issue trackers and CI logs. The open empirical question InferFix leaves unresolved is whether LLM-inferred type labels can substitute for Infer-derived labels to enable effective type-conditioned retrieval for general natural bugs — precisely what FTCR's X%/Y% calibration measures. InferFix validates that type-conditioned retrieval works (supporting FTCR's hypothesis) while leaving the LLM-label-quality-vs-retrieval-effectiveness question entirely unanswered. ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of the 18 minor semantic sub-types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than ReinFix's joint root-cause embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar embeddings but different repair operators do not. DebugBench's 4-major/18-minor hierarchical taxonomy uniquely provides 4,253 instances with ground-truth type annotations across C++, Java, and Python (organized as: Syntax/7 sub-types, Reference/4, Logic/4, Multiple Bugs/3), enabling direct classifier calibration at the minor-type level and turning error propagation from a latent risk into the paper's core measurable variable. The confidence-gated hybrid has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). M-RAG (ACL 2024, arXiv 2405.16420) validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis.",
  "landscape": "RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% and is not a SOTA claim. InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-conditioned cross-repository retrieval system for code repair: it pretrains a Retriever via contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type from Infer static analysis), then at retrieval time filters candidates to same-type fixes using Infer-derived type labels. The encoder itself encodes only the buggy code as a dense vector — type structures the training pairs but is not an explicit encoder input; the retriever learns type-correlated semantic similarity. InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#, outperforming LLM baselines by 11–55%. Three design differences distinguish FTCR from InferFix: (a) Type label acquisition — InferFix requires Infer to run on each repository to produce type labels for both corpus and query bugs; FTCR uses few-shot LLM classification, covering any natural bug without static analysis tooling; the core empirical question vs. InferFix is whether LLM-inferred labels achieve sufficient accuracy (X%) to match Infer-derived retrieval quality; (b) Defect taxonomy — InferFix uses Infer-specific diagnostic IDs (covering only statically-detectable bug patterns), not the 4-major/18-minor natural-bug taxonomy aligned with DebugBench's empirically-grounded labels (Syntax/7, Reference/4, Logic/4, Multiple Bugs/3); (c) Corpus — InferFix uses InferredBugs (static-analysis artifacts); FTCR uses natural bug-fix pairs from SWE-bench, BugsInPy, Defects4J, and GitBug-Java. The scientific question InferFix leaves open — and FTCR directly tests — is whether LLM-inferred type labels achieve sufficient accuracy (X%) to enable type-conditioned retrieval that is effective for general natural bugs, and at what accuracy threshold does type-conditioned retrieval outperform soft embedding baselines (Z% > 0%, W% < Z%). ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning. Corpus quality confound: comparisons against published ReinFix results conflate two variables simultaneously — retrieval architecture (soft joint embedding vs. hard type partition) and corpus quality (100K TRANSFER synthetic pairs vs. 3,050 natural bug-fix pairs from issue trackers and CI logs). Intra-corpus ablations (FTCR vs. re-implemented ReinFix-style baseline on the same 3,050-pair natural corpus using the same text-embedding-3-large encoder) test the partitioning hypothesis cleanly and isolate architecture as the variable. Absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality differences simultaneously and are presented explicitly as such; they are not used to claim a clean head-to-head win on architecture alone. SWE-Exp (arXiv 2507.23361, revised February 2026) retrieves top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic Python-only pipeline. Three design differences: (1) soft vs. hard — SWE-Exp uses type as retrieval-time embedding metadata; FTCR partitions at index-construction time; (2) retrieved artifact — SWE-Exp stores distilled modification strategies; FTCR retrieves concrete fix patches; (3) scope — SWE-Exp is agentic and Python-only; FTCR covers C++/Java/Python in retrieval-only mode. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5. TypeRepair's context selection stage conditions on the identified defect type to select within-project code context and provide type-specific repair guidance — it does not retrieve from an external cross-repository fix corpus. Evidentiary basis: TypeRepair evaluates exclusively on Defects4J V1.2/V2.0 and QuixBugs — within-project Java bug collections that contain no external cross-repository retrieval component. The evaluation design (project-internal datasets, no external corpus described in benchmark setup) makes the within-project scope structurally evident from the experimental setup; any reviewer with full SQJ article access who finds this claim incorrect is encouraged to provide the correction, as the differentiation rests on the publicly visible evaluation design. TypeRepair is Java-only; FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 fix patches. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec while contextual and API information helps; the 'what to retrieve matters' finding motivates FTCR's type-partition design. DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3. Both update the landscape but are orthogonal to retrieval strategy. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via objective alignment. FTCR's structural departure from all prior work is to (1) classify incoming failures into discrete minor sub-categories of the 4-major/18-minor DebugBench taxonomy, then (2) retrieve only from the type-matched sub-index, using text-embedding-3-large (identical to ReinFix) for a clean intra-corpus partitioning comparison — with the random-partition control separating type-matching precision from pool-size reduction. RetypeR (ICSME 2024, Hao et al.) applies type-specific retrieval for Python type errors only; FTCR extends to 18 minor sub-types across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates multi-partition RAG outperforms single-store RAG across NLP tasks (+11% summarization, +8% translation, +12% dialogue). PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary scope. The APR survey (arXiv 2506.23749) reviews 63+ systems with no type-partitioned cross-language retrieval system identified.",
  "approach": "We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms ReinFix's soft root-cause embedding for cross-repository fix template transfer, and that LLM-inferred type labels can substitute for the Infer-required labels used by InferFix to enable type-conditioned retrieval on general natural bugs. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix), same natural corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control.\n\nNLP Lead Contribution: LLM Label Quality and Downstream Retrieval Impact. The primary EMNLP Findings contribution is a complete causal decomposition of when hard type conditioning helps and when it hurts, parameterized by four falsifiable quantities measured at the minor-type level (18 sub-types of the 4-major/18-minor DebugBench hierarchy, with major-type aggregation reported as a secondary result): (X%) few-shot LLM classifier accuracy against DebugBench ground-truth oracle labels at the minor-type level; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement on DebugBench/Defects4J V1.2 for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances under hard partitioning vs. same baseline. Z% and W% are reported as aggregate rates across all correctly-classified and misclassified instances respectively; significance is tested via McNemar's test on paired pass/fail outcomes (baseline vs. FTCR, same instances); per-type breakdowns use Fisher's exact test with a minimum n≥30 instance threshold; 95% confidence intervals are reported for both Z% and W%. Together these quantities are a direct empirical answer to: 'LLM-inferred categorical labels enable hard retrieval partitioning only if X% and Y% are high enough to make the correctly-classified population (driving Z%) larger than the misclassified population (driving W%).' This generalizes beyond code repair to any system that uses LLM-generated labels to route queries into type-specific retrieval pools.\n\nExecution Plan for EMNLP 2026 ARR (May 25 deadline, 15 days from today). Auto-research mode (10–14 days) is the only constraint-compliant execution path. Day-by-day schedule with minimum viable submission (MVS) milestones:\n\n- Day 0 (May 10): Launch auto-research pipeline; begin 3-pass annotation of 3,050 corpus pairs using DebugBench few-shot examples as demonstrations for the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4); configure Defects4J V1.2 Java-8 Docker environments and GitBug-Java isolated containers. Compute: 2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.\n- Day 1–3 (May 11–13): Annotation completes (~$183 Claude API cost). DebugBench classifier calibration: 20% held-out split (~851 instances, covering single-bug instances from the Syntax/Reference/Logic major categories and treated separately for the Multiple Bugs category) → X% per-minor-type accuracy with major-type aggregation as secondary. Cross-lingual Java transfer sample (56 human-verified pairs from Defects4J + GitBug-Java) → Y% transfer accuracy. Per-minor-type count table computed; within-major-category merge policy applied for rare minor types below the 30-instance Java threshold.\n- Day 4–6 (May 14–16): Build type-partitioned sub-indices and ReinFix-style unified index (both text-embedding-3-large). Run Defects4J V1.2 ablations: Variant A (text-similarity RAG), Variant D (ReinFix-style re-implemented on same natural corpus), Variant E (FTCR@hard-all), Variant F (random-partition control, N equivalently-sized random sub-indices). Prepare pre-drafted paper skeleton (introduction, related work, method) during this window to reduce Day 13–15 writing pressure.\n- Day 7–9 (May 17–19): DebugBench evaluation across all variants on single-bug instances (Syntax/Reference/Logic major categories); confidence-gated τ sweep on held-out validation split; stratify results by classifier confidence band: high-confidence correctly-classified → Z% (aggregate, McNemar's test); misclassified → W% (aggregate, McNemar's test); per-type Fisher's exact test for types with n≥30. SWE-bench Lite evaluation launched in parallel (requires 2 A100 nodes for ~10 min/instance).\n- Day 10–12 (May 20–22): CodeBERT-base encoder ablation (same FTCR vs. ReinFix-style comparison, secondary encoder); taxonomy granularity ablation (major-type coarse/4 vs. minor-type fine/14 single-fault sub-types vs. merged-Java categories); retrieval k sweep (1/3/5/10).\n- Day 13 (May 23): Results compilation; paper writing begins with NLP lead (X%/Y%/Z%/W% as opening contribution).\n- Day 14–15 (May 24–25): Paper finalization and ARR submission. MVS for EMNLP Findings: DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. SWE-bench Lite Python results included if pipeline completes by Day 12, deferred to ICSE 2027 extended version otherwise.\n\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. InferFix demonstrates that type-conditioned retrieval improves over code-similarity retrieval, but requires Infer static analysis to label both corpus and query bugs. FTCR embodies a stronger form of this principle: classify the incoming bug using an LLM (no static analysis tooling required), then restrict the retrieval pool to same-type patches at index construction time, ensuring that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to score high in a shared embedding space but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\n\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559). The corpus is annotated against the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4); the Multiple Bugs sub-types (double/triple/quadruple) are not applicable to single-fix commit pairs in the retrieval corpus and are excluded from corpus annotation but evaluated separately in the DebugBench test set.\n\nCorpus Quality Confound (Explicit). The natural 3,050-pair corpus differs from ReinFix's 100K TRANSFER corpus in two simultaneous dimensions: (1) retrieval architecture (soft joint embedding vs. hard type partition) and (2) corpus quality (natural issue-tracker/CI bug-fix pairs vs. synthetic static-analysis-derived pairs). Intra-corpus ablations — FTCR vs. re-implemented ReinFix-style baseline using text-embedding-3-large on the identical 3,050-pair natural corpus — test the partitioning hypothesis cleanly and are the primary experimental contribution. Absolute performance comparisons against published ReinFix numbers on Defects4J reflect both architecture and corpus quality simultaneously; they are presented as joint-effect comparisons, not as clean head-to-head architectural wins. The random-partition control (Variant F) further isolates type-matching precision from pool-size reduction within the intra-corpus comparison.\n\nCorpus Sparsity Policy. Each pair is annotated with one of 14 single-fault minor sub-types via few-shot prompting; three annotation passes measure inter-run consistency. For the combined Python+Java corpus (~3,050 pairs, 14 active minor types), mean pairs per type is approximately ~218. For Java-only ablations (~559 pairs), types with fewer than 30 Java instances are merged into nearest-neighbor supercategories within the same major category (e.g., rare Syntax sub-types such as 'illegal separation' and 'illegal indentation' merged within Syntax — never across Syntax/Reference/Logic boundaries); Java ablation results are reported for the 4–6 resulting within-major-category merged groups that each exceed 50 instances, with merged categories explicitly labeled. Note that several Syntax sub-types (missing colons, illegal indentation) are Python-specific and may yield few or zero Java instances; these are expected to merge to the within-Syntax catch-all for Java ablations.\n\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound (~$5–15 total embedding cost). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific.\n\nType Classifier Calibration on DebugBench Ground Truth. A held-out 20% split (~851 instances) directly measures few-shot classifier precision and recall per minor sub-type against oracle ground-truth labels, yielding X% at the minor-type level (major-type aggregation reported as a secondary result). The primary repair evaluation uses single-bug instances from the Syntax, Reference, and Logic major categories (~2,035 of 4,253 instances); Multiple Bugs instances (double/triple/quadruple, ~2,218 instances) are evaluated separately as an auxiliary experiment to characterize classifier behavior on multi-type ambiguous queries. Cross-dataset zero-shot agreement on ~56 human-verified Java pairs yields Y%. These produce the core NLP finding: LLM-inferred bug type labels achieve X% agreement with DebugBench ground truth (Python/C++) at the minor-type level, transfer zero-shot to Java with Y% agreement, and predict retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs (both aggregate across all instances of each class, McNemar's test, 95% CI).\n\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect, the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index (Variant F). Any performance gap between FTCR (Variant E) and this control measures the precision benefit of type-matching net of pool-size reduction.\n\nConfidence-Gated Retrieval Fallback. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval. Six variants evaluated: (A) text-similarity RAG, (B) RELREPAIR, (C) RepoRepair, (D) ReinFix-style soft on same corpus, (E) FTCR@hard-all, (F) random-partition control. Confidence-gated hybrid evaluated as a seventh configuration. Precedent: CRAG (Yan et al., arXiv:2401.15884).\n\nPractical Utility. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is the retrieval contribution in isolation, not a pipeline SOTA claim. DynaFix demonstrates retrieval and execution augmentation are independently improvable axes; an improved retrieval module (FTCR vs. ReinFix-style) compounds with execution-level improvements. Standalone evaluation isolates the retrieval hypothesis cleanly.\n\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while Defects4J V1.2 (MVS) and SWE-bench Lite (full version) validate real-world transfer.",
  "resource_estimate": {
    "auto_research": {
      "gpu_hours": "~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)",
      "gpu_utilization": "near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants",
      "ablation_scope": "Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline on same natural corpus), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (4-major coarse / 14-minor single-fault fine / merged-Java within-major), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java → SWE-bench-Lite Python), classifier accuracy stratification by confidence band",
      "timeline": "10-14 days with 2 A100 nodes running in parallel — the ONLY constraint-compliant execution mode for the 16-day hard budget. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) both violate the user's timeline constraint and are not presented as viable paths.",
      "day_by_day_schedule": "Day 0 (May 10): setup and corpus annotation launch. Compute confirmed: 2 A100 nodes provisioned; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested. Day 1–3 (May 11–13): annotation + DebugBench classifier calibration (X% minor-type level, Y%). Day 4–6 (May 14–16): index construction + Defects4J V1.2 ablations (Variants A/D/E/F) + pre-drafted paper skeleton. Day 7–9 (May 17–19): DebugBench evaluation (single-bug instances) + confidence stratification (Z%, W% aggregate with McNemar's test) + SWE-bench Lite launch. Day 10–12 (May 20–22): CodeBERT ablation + granularity + k-sweep. Day 13 (May 23): results compilation + paper skeleton. Day 14–15 (May 24–25): paper finalization + ARR submission.",
      "team": "0 (initial ~4h setup for corpus pipeline, per-type sub-index construction, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)",
      "claude_api_cost": "$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)",
      "embedding_api_cost": "~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)",
      "estimated_gpu_cost": "~$969 (323 A100-hours × $3/h)",
      "speed_bottleneck": "GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls",
      "risk_note": "SWE-bench Lite may not complete before Day 12; MVS for EMNLP Findings submission is DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control, achievable within the 10–14 day window. Compute pre-provisioned as of Day 0. Auto-assigned bug type labels may drift without the three-pass consistency check; confidence-gated hybrid adds hyperparameter τ requiring tuning on held-out split before SWE-bench evaluation. Two-day paper writing window (Days 13–15) requires pre-drafted skeleton prepared during Days 4–6."
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings (via ARR, deadline May 25, 2026 11:59 PM AoE — PRIMARY TARGET; 15 days from today). The X%/Y%/Z%/W% calibration study — measuring LLM-generated bug type label quality and its downstream impact on retrieval-augmented repair — is appropriate for EMNLP Findings, which publishes solid empirical contributions that advance understanding of specific NLP phenomena. The Main track expects findings that advance understanding of language models at a deeper architectural or representational level and poses higher desk-rejection risk for an empirical calibration study; Findings is the correct target and the proposal commits to it without oscillation. Path: auto-research completes Days 0–12 (May 10–22); paper writing Days 13–15 (May 23–25). Minimum viable submission: DebugBench classifier calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. EMNLP Findings fits the paper's core contribution: LLM annotation reliability for a structured classification task and the downstream retrieval consequences of label noise — a contribution to the NLP literature on LLM-generated categorical labels and RAG system design. Timeline is extremely tight: the two-day writing window requires a pre-drafted paper skeleton prepared concurrently with Days 4–6 experiment setup. Risk: if SWE-bench Lite does not complete by Day 12, the EMNLP Findings version covers DebugBench + Defects4J only, with SWE-bench Lite results added in the ICSE 2027 version.",
    "ICSE 2027 (mandatory abstract deadline June 23, 2026 — BACKUP venue if EMNLP ARR cycle overlaps unfavorably or EMNLP Findings submission is not accepted). SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation; InferFix paragraph establishes LLM-inferred vs. Infer-required type labels as the untested dimension; TypeRepair comparison clarifies FTCR's orthogonal contribution of cross-repository retrieval; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections; intra-corpus confound framing converts the corpus quality issue into a feature rather than a weakness.",
    "FSE 2027 (full paper deadline October 2, 2026 — tertiary backup if both EMNLP and ICSE review cycles are unfavorable)."
  ],
  "level": "solid",
  "key_references": [
    "InferFix: End-to-End Program Repair with LLMs over Bug-Specific Retrieval (ESEC/FSE 2023, arXiv:2303.07263) [earliest type-conditioned cross-repository repair retrieval; Retriever pretrained via contrastive learning using same-type bug-fix pairs as positives and different-type pairs as negatives (type from Infer static analysis); encoder encodes only buggy code — type structures training pairs but is NOT an explicit encoder input; the retriever learns type-correlated semantic similarity; at retrieval time, candidates are filtered to same-type fixes using Infer-derived labels; achieves 76.8% Java top-1 accuracy; InferFix validates type-conditioned retrieval but requires Infer static analysis at both corpus construction and query time — FTCR's scientific contribution vs. InferFix is testing whether LLM-inferred labels can substitute for Infer-derived labels (X%/Y%) and enabling type-conditioned retrieval for general natural bugs Infer cannot detect; must differentiate: (a) Infer-required labels vs. LLM-inferred labels; (b) query-time type filtering vs. FTCR's construction-time index partitioning; (c) Infer-specific diagnostic IDs vs. 4-major/18-minor natural-bug taxonomy; (d) InferredBugs vs. natural issue-tracker/CI bug-fix pairs]",
    "ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; soft root-cause augmentation using unified vector database with text-embedding-3-large; intra-corpus comparison (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) is the clean architectural test; absolute comparisons against published ReinFix numbers reflect corpus quality confound and are presented as such]",
    "SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; 73.0% SWE-bench Verified with Claude 4 Sonnet; agentic, Python-only; differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, multi-language scope]",
    "TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J/QuixBugs (Java-only); validates that type conditioning improves LLM repair; Stage 3 context selection draws from within-project code files, not external cross-repository corpus — differentiation supported by evaluation design (project-internal datasets, no external corpus described in benchmark setup); FTCR's orthogonal contribution is type-conditioned retrieval from external ~3,050-pair cross-language corpus]",
    "What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond (Gu et al., ICSE 2026, arXiv 2503.20589) [similar-code retrieval degrades code generation by up to 15% on CoderEval/RepoExec while structured knowledge helps; motivates type-partition fix-patch retrieval as avoiding the similarity-noise trap; note: code generation study, not repair — applicable as indirect motivation]",
    "ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330) [algorithm-type-conditioned retrieval in competitive programming — conceptual ancestor scoped to algorithmic tags]",
    "RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors (ICSME 2024, Hao et al.) [type-specific retrieval for Python type errors only — FTCR extends to 18 minor sub-types and 3 languages]",
    "DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv 2512.24635) [surpasses ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; demonstrates retrieval and execution augmentation are independently improvable axes]",
    "DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2604.19305) [295 Defects4J bugs with DeepSeek-V3; updates landscape but orthogonal — no retrieval augmentation]",
    "D4C: Aligning the Objective of LLM-based Program Repair (ICSE 2025, arXiv 2404.08877) [180 Defects4J bugs via objective alignment; updates performance landscape]",
    "M-RAG: Reinforcing Large Language Model Performance through Retrieval-Augmented Generation with Multiple Partitions (ACL 2024, arXiv 2405.16420) [multi-partition RAG: +11% summarization, +8% translation, +12% dialogue; principled precedent for partition-based retrieval across domains]",
    "RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code (arXiv 2509.16701) [project-internal retrieval baseline]",
    "RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048) [documentation-guided localization baseline; 45.7% SWE-bench Lite]",
    "DebugBench: Evaluating Debugging Capability of Large Language Models (ACL Findings 2024) [primary evaluation; ground-truth 4-major/18-minor hierarchical taxonomy: Syntax (7 sub-types: misused ==/=, missing colons, unclosed parentheses, illegal separation, illegal indentation, unclosed string, illegal comment), Reference (4 sub-types: faulty indexing, undefined objects, undefined methods, illegal keywords), Logic (4 sub-types: condition error, operation error, variable error, other error), Multiple Bugs (3 sub-types: double/triple/quadruple co-occurring bugs); 4,253 instances across C++/Java/Python; held-out 20% split (~851 instances) for classifier calibration (X%) at minor-type level; primary repair evaluation on single-bug major categories (Syntax/Reference/Logic, ~2,035 instances); Multiple Bugs treated as separate analysis; acknowledged synthetic-bug limitation]",
    "GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; cross-lingual transfer calibration (Y%)]",
    "SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025, arXiv 2504.21798) [50k Python task instances; scale corpus for Python retrieval index]",
    "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey; confirms retrieval augmentation as key enhancement; no type-partitioned cross-language system identified; cites InferFix as a key retrieval-augmented approach]",
    "What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]",
    "PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]",
    "RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]",
    "CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism; precedent for FTCR confidence-gated hybrid; cite as preprint — withdrawn from ICLR 2025, unpublished]"
  ],
  "description": "FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft type-conditioned retrieval (ReinFix's root-cause embedding approach, ICSE 2026) for cross-repository fix template transfer, while LLM-inferred type labels can substitute for the Infer-required labels used by InferFix (ESEC/FSE 2023) to enable type-conditioned retrieval on general natural bugs. The primary NLP contribution — targeted at EMNLP 2026 Findings (via ARR, May 25, 2026) — is a complete causal decomposition parameterized by four falsifiable quantities measured at the minor-type level of DebugBench's 4-major/18-minor hierarchical taxonomy: (X%) few-shot LLM classifier accuracy vs. DebugBench ground-truth oracle labels at the minor-type level (major-type aggregation as secondary); (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline (aggregate, McNemar's test, 95% CI); (W%) repair degradation for misclassified instances (aggregate, McNemar's test, 95% CI). Together these characterize when hard categorical type conditioning helps and when it hurts, generalizing to any system using LLM-inferred categorical labels for retrieval routing. FTCR's structural departure from ReinFix is to (1) classify incoming failures into one of the 14 single-fault minor sub-types, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable in a clean intra-corpus comparison. Round 7 revisions address five issues: (a) EMNLP FINDINGS COMMITTED — target_venues now lists 'EMNLP 2026 Findings (via ARR)' as the sole EMNLP target; the X%/Y%/Z%/W% calibration study is appropriate for Findings, not Main; the oscillation between Main and Findings is resolved with a committed rationale. (b) DEBUGBENCH HIERARCHY CORRECTED — all references to '18-category taxonomy' replaced with '4-major/18-minor hierarchical taxonomy' (4 major: Syntax/7 sub-types, Reference/4, Logic/4, Multiple Bugs/3); primary repair evaluation scoped to single-bug instances (Syntax/Reference/Logic, ~2,035 of 4,253); Multiple Bugs (~2,218 instances, 52%) treated as separate analysis; merge policy now operates within-major-category-first (e.g., rare Syntax sub-types merged within Syntax, never across Syntax/Reference/Logic); X%/Y%/Z%/W% measured at minor-type level with major-type aggregation as secondary; per-minor-type Java instance estimate revised to ~40 per single-fault minor type for Java-only ablations. (c) COMPUTE READINESS CONFIRMED — Day 0 entry now states: '2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.' (d) INFERFIX ARCHITECTURE CORRECTED — the 'soft continuous embedding feature' characterization was inaccurate; InferFix's encoder learns type-correlated semantic similarity (type structures contrastive training pairs but is not an explicit encoder input); InferFix does filter retrieval candidates by type at query time using Infer-derived labels; FTCR's primary differentiation from InferFix is reframed as (i) type label acquisition: LLM classification vs. Infer static analysis required; (ii) taxonomy: 4-major/18-minor general natural-bug taxonomy vs. Infer-specific diagnostics; (iii) corpus: natural bug-fix pairs vs. InferredBugs; the empirical question vs. InferFix is now correctly stated as 'can LLM-inferred labels substitute for Infer-derived labels at sufficient accuracy (X%) to enable effective type-conditioned retrieval?'. (e) STATISTICAL SIGNIFICANCE SPECIFIED — Z%/W% reported as aggregate rates; McNemar's test on paired pass/fail outcomes; Fisher's exact test for per-type breakdowns (n≥30 threshold); 95% confidence intervals for Z% and W%.",
  "project_name": "failure_type_rag_repair",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL — Uncited competing work invalidates novelty claim: ReinFix (ICSE 2025, arXiv 2506.23100) embeds root-cause classification into retrieval from a 1M-pair historical bug-fix corpus, which is mechanistically nearly identical to FTCR's type-conditioned retrieval from historical corpus. The proposal must cite and differentiate from ReinFix; without this, reviewers will reject on novelty grounds.", "CRITICAL — ReCode overlap is underplayed: ReCode already implements algorithm-type-conditioned retrieval with type-partitioned sub-knowledge-bases, the identical core mechanism. FTCR's contribution is extending this to real-world bugs (competitive programming → repositories), which must be framed more precisely. The current framing overclaims novelty.", "HIGH — Dataset size claim is internally inconsistent: BugsInPy (493) + Defects4J (1,192) = ~1,685 pairs, not 6,500. If the SWE-bench training split (19,000 instances) is included, that's 20,000+. The '~6,500' figure suggests some undescribed quality-filtering or subsetting logic that is not specified in the proposal. This will raise red flags in review.", "HIGH — Defects4J reproducibility crisis: Independent studies (MSR 2025) found ~50% of Defects4J fault-triggering tests are regression tests added post-hoc, and nearly 50% become non-reproducible with modern Java. BugsInPy showed 67% reproducibility. Mining ~1,685 pairs from these datasets may yield fewer than 900 reliably reproducible bug-fix pairs, undermining the corpus quality and scale claims.", "MEDIUM — Uncited prior art RetypeR (ICSME 2024): This paper applies type-specific retrieval (external retrieval stage conditioned on Python type errors) and should be discussed as prior art that narrows the novelty of cross-language type-conditioned retrieval.", "MEDIUM — Resource units inconsistency: The hard constraint is ≤200 H100-hours, but the proposal reports A100-hours throughout. Manual mode (~150 A100h ≈ 90 H100h) is within budget, but auto-research mode (~650 A100h ≈ 390 H100h) significantly exceeds the constraint. This should be flagged and the primary experiment budget anchored in H100-hours.", "MEDIUM — EMNLP framing needs NLP-centric repositioning: The primary contribution is a retrieval system design (SE contribution). EMNLP 'NLP and Code Models' track requires a clear NLP/LLM contribution. The few-shot taxonomy induction approach and its ability to generalize zero-shot across languages should be foregrounded as the NLP contribution; the retrieval architecture is the engineering substrate.", "LOW — DebugBench validity concern: DebugBench uses LeetCode code with GPT-4-implanted synthetic bugs, not real repository bugs. Results on DebugBench may not transfer to SWE-bench Lite, requiring a careful discussion of the domain gap between the two evaluation settings."]
Feedback: The core gap FTCR targets is real but narrower than claimed. To make this revisable into a strong paper: (1) Reframe the novelty around what's genuinely new — the extension of type-partitioned retrieval from algorithmic contest code (ReCode) to real-world multi-language repository bugs with an 18-category taxonomy grounded in DebugBench's empirically validated type structure. This is a specific, defensible contribution. (2) Add ReinFix as a baseline: since ReinFix uses root-cause-conditioned retrieval from historical corpus, you must compare against it directly on a shared benchmark (Defects4J is common). If FTCR's type-partitioned index outperforms ReinFix's joint root-cause+code embedding, that's a publishable finding. (3) Fix the dataset size: either restrict to BugsInPy+Defects4J and acknowledge the smaller corpus (~1,500–1,685 pairs after reproducibility filtering), or explicitly include a quality-filtered SWE-bench train subset and describe the filtering criteria. (4) Run a reproducibility pre-check: before committing to Defects4J as a corpus source, filter to only Java 8-compatible bugs (reported to have ~80% reproducibility) and report the usable fraction. (5) For EMNLP fit, pivot the NLP angle to the few-shot taxonomy induction finding — specifically, whether LLM-inferred bug types are consistent, cross-lingual, and predictive of repair success. This is the NLP scientific question. (6) The 16-day timeline is only viable in auto-research mode with parallel evaluation; the paper should scope evaluation to DebugBench (where type labels are ground-truth) plus SWE-bench Lite (300 instances), and acknowledge that a full Defects4J corpus build is out-of-scope for the conference timeline.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL — Citation error: ReinFix is confirmed ICSE 2026 (arXiv 2506.23100 states 'Accepted by ICSE 2026'), not ICSE 2025 as the proposal states throughout. EMNLP 2026 explicitly warns against hallucinated citations and has stated it may desk-reject papers with such errors. Every reference to 'ReinFix (ICSE 2025)' must be corrected to 'ReinFix (ICSE 2026)'.", "HIGH — Corpus sparsity renders type partitioning semantically degenerate for rare types: 559 Java pairs (Defects4J + GitBug-Java) across 18 types yields ~31 Java instances per type on average. For rare bug categories (concurrency, resource leaks, format errors), this may be 5–15 instances. Retrieving k=5 from a sub-index of 15 instances is not retrieval—it is exhaustive lookup. The proposal must either (a) restrict to the 6–8 most frequent types where >50 Java instances exist, or (b) merge rare types into a broader category, or (c) acknowledge that the per-type ablation is only meaningful for the top N types and report per-type corpus sizes in the paper.", "HIGH — Classifier error propagation is unaddressed: if the type classifier misclassifies an incoming bug (which will occur for edge cases and multi-type bugs), the system retrieves from the wrong partition and almost certainly underperforms soft retrieval for those instances. This is the main structural risk of hard partitioning over soft embedding. The proposal must analyze: (a) classifier accuracy on held-out annotated bugs, (b) the performance degradation attributable to misclassification, and (c) whether a confidence-gated fallback to soft retrieval recovers performance.", "HIGH — EMNLP venue fit remains questionable: the core contribution is an IR architecture decision (partitioning a FAISS index by categorical label). EMNLP 'NLP and Code Models' reviewers will ask what the NLP/LM finding is. The 'few-shot cross-lingual taxonomy induction' contribution (measuring whether LLM-inferred bug types are consistent across annotation runs) is secondary and not a compelling standalone NLP finding—LLM classification consistency is well-studied. If submitting to EMNLP, the NLP contribution must be foregrounded more strongly, e.g., a finding that LLM-inferred type labels are cross-lingually stable and predictive of repair success at the p<0.01 level, with analysis of failure cases that reveal type-specific linguistic patterns in bug descriptions.", "MEDIUM — ASE 2026 NIER deadline (May 12) is 2 days from today and experiments are not done: listing it as a target venue is unrealistic. Remove from target_venues or replace with a venue with a later deadline (e.g., EMNLP Findings via ARR, or FSE 2027).", "MEDIUM — No expected performance range stated for SWE-bench Lite: reviewers will immediately compare against the RepoRepair baseline (45.7% on Lite). The proposal should state an expected performance range and justify why a lower absolute number is acceptable given the paper's focus on architectural comparison rather than SOTA performance.", "LOW — The proposal does not specify which encoding model will be used for FTCR. ReinFix uses text-embedding-3-large (OpenAI API). If FTCR uses the same encoder for fair comparison, this imposes an ongoing API cost not captured in the GPU-hour budget. If using CodeBERT or UniXcoder instead, the encoder comparison is confounded with the hard/soft partitioning comparison. This should be clarified explicitly."]
Feedback: The Round 2 revision has fixed the major structural issues from Round 1 (ReinFix is now a baseline, dataset sizes are consistent, RetypeR is cited, compute is in H100-hours, DebugBench limitations acknowledged). The core hypothesis is testable and the ablation design is clean. Three issues must be addressed before this is submission-ready: (1) Fix the citation error throughout — ReinFix is ICSE 2026, not ICSE 2025; submit it as 'ReinFix (ICSE 2026, arXiv:2506.23100)'. (2) Address corpus sparsity directly in the methods section: report per-type instance counts in a table, restrict the full 18-type analysis to the Python+Java combined corpus, and for the Java-only ablations acknowledge that only the top N types have >50 instances. For types below a minimum threshold (suggest 30 instances), either merge or exclude from per-type breakdown. (3) Add a classifier accuracy analysis: measure the type classifier on the annotated DebugBench ground-truth labels (since DebugBench already has ground-truth types, you can directly measure LLM classifier accuracy), then report how type-matched retrieval performance varies as a function of classifier confidence. This turns the error propagation problem into a feature — it becomes an analysis of when hard partitioning helps vs. hurts. For EMNLP specifically: the NLP contribution must be stated as a crisp finding, not a process. Frame it as: 'We show that LLM-inferred bug type labels achieve X% agreement with DebugBench ground-truth labels, transfer zero-shot to unseen Java bugs with Y% agreement, and are predictive of retrieval-augmented repair success (type-matched retrieval outperforms soft retrieval by Z% for correctly classified bugs, while underperforming by W% for misclassified bugs).' This is a falsifiable empirical claim that EMNLP reviewers can evaluate.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL — CRAG citation is a hallucinated venue: The proposal cites 'CRAG (ICLR 2024)' but CRAG (arXiv:2401.15884) was submitted to ICLR 2025 and withdrawn — it was never accepted or published at any ICLR. Citing it as a published ICLR paper is precisely the kind of hallucinated venue citation EMNLP warns may trigger desk rejection. The correct citation is 'CRAG (Yan et al., 2024; arXiv:2401.15884)'.", "HIGH — Unacknowledged concurrent work: SWE-Exp (arXiv:2507.23361, July 2025) uses an experience bank where retrieval explicitly surfaces 'the top N=10 issues most relevant in terms of error type' via cosine similarity, achieves 41.6% on SWE-bench Verified, and is publicly available with open-source code. While the mechanism is different (experience trajectories + soft cosine vs. hard categorical partitioning of fix templates), EMNLP and ICSE reviewers will notice its absence. FTCR must cite it, note the difference (soft type-similarity vs. hard categorical partitioning), and explain why hard partitioning is a distinct hypothesis worth testing.", "MEDIUM — 'Clean comparison' overstates the isolation: Type-partitioned retrieval fundamentally reduces the effective retrieval corpus to 1/N_types (≈1/18 on average) of the full index. A smaller retrieval pool affects recall independently of the type-matching benefit. Without a 'random-partition baseline' (random corpus subsets of equivalent size per query), the observed gain (or loss) conflates two effects: (a) partitioning precision and (b) retrieval corpus size. The proposal should either add this control or explicitly acknowledge it as a confound in Section 4.", "MEDIUM — EMNLP main track fit remains overstated: The NLP contribution — measuring X% agreement between LLM-inferred bug type labels and DebugBench ground truth, then correlating with repair success — is a measurement finding about LLM classification reliability on a well-structured taxonomy. This is useful but unlikely to be viewed as a primary NLP/LM contribution by EMNLP main track reviewers, who expect findings that advance understanding of language models. EMNLP Findings is a more realistic target; ICSE 2027 (already listed) is the natural primary venue where the SE audience will value the retrieval architecture contribution directly.", "LOW — Minor ReinFix technical inaccuracy: The proposal states ReinFix uses 'a unified FAISS vector store' but the ReinFix paper (arXiv:2506.23100) only refers to 'a vector database' without specifying FAISS as the implementation. This overly specific characterization of the baseline's internals should be softened to 'a unified vector database' to avoid misrepresentation of the primary baseline."]
Feedback: Round 3 has successfully addressed the four critical/high issues from Round 2: citation corrected to ICSE 2026 throughout, corpus sparsity handled with explicit per-type table and 30-instance merge policy, classifier error propagation addressed with confidence-gated hybrid and DebugBench calibration, and EMNLP framing sharpened to a crisp X%/Y%/Z%/W% falsifiable claim. The core hypothesis is testable and genuinely novel for multi-language APR. Two issues block submission: (1) Fix the CRAG citation immediately — replace every instance of 'CRAG (ICLR 2024)' with 'CRAG (Yan et al., 2024; arXiv:2401.15884)'. CRAG was submitted to ICLR 2025 but withdrawn and unpublished; citing it as published ICLR work is a hallucinated venue citation that can trigger desk rejection at EMNLP. (2) Add SWE-Exp (arXiv:2507.23361) to the landscape with one paragraph: it uses soft cosine retrieval filtered 'in terms of error type' from an experience bank; FTCR's departure is hard categorical partitioning at index-construction time, not just retrieval-time filtering, plus fix-template retrieval rather than trajectory experience. For longer-term strengthening: add a random-partition baseline (randomly assign corpus pairs to N equivalent-sized sub-indices) to isolate the type-matching benefit from the corpus-size effect. This single ablation converts the comparison from 'clean but contested' to 'rigorous and unambiguous'. On venue strategy: ICSE 2027 (abstract June 23) should be positioned as the primary target; EMNLP 2026 ARR (May 25) can be attempted for Findings if the NLP framing holds, but do not overinvest in EMNLP main track positioning — the primary audience for this work is the SE/APR community.

### Round 4 review
Verdict: revise
Issues: ["HIGH — Uncited concurrent work: 'Towards Defect-Type-Aware Adaptive Program Repair' (TypeRepair, Zhang et al., Software Quality Journal 2026, link.springer.com/article/10.1007/s11219-026-09751-w) uses explicit defect type identification before context selection in a 4-stage pipeline (localization → type ID → context selection → patch generation) on Defects4J V1.2/V2.0 and QuixBugs, independently achieving 272% improvement over GPT-3.5 baseline. The paper must be obtained, read, and cited: if 'context selection' uses type-conditioned retrieval from a cross-repo external corpus (which cannot be confirmed from the abstract alone due to paywall), the overlap with FTCR is substantial and reviewers will notice its absence. If TypeRepair uses only within-project context, that is FTCR's key differentiation and must be stated explicitly.", "HIGH — Unaddressed counterevidence: 'What to Retrieve for Effective Retrieval-Augmented Code Generation?' (ICSE 2026, arXiv 2503.20589) empirically shows that retrieving syntactically similar code snippets degrades performance by up to 15% compared to retrieving in-context examples and API information. This is a direct challenge to FTCR's premise: if type-partitioned retrieval returns syntactically similar-but-wrong-level-of-abstraction fixes within each partition, it may concentrate rather than reduce this noise. The authors must address this finding — either by arguing that semantic type partitioning selects at a different abstraction level than syntax similarity, or by adding an experiment measuring within-type fix template quality vs. cross-type.", "MEDIUM — Practical utility framing missing: FTCR projects 20–35% on SWE-bench Lite while SWE-Exp achieves 73% on SWE-bench Verified and RepoRepair achieves 45.7% on Lite. ICSE 2027 reviewers will ask why the retrieval strategy matters in isolation when execution-augmented agentic methods dominate. The paper needs an explicit 'why retrieval strategy matters' argument: e.g., (1) retrieval modules are independently upgradeable components within agentic systems — DynaFix adds execution feedback orthogonally to retrieval, so a better retrieval module improves the whole pipeline; (2) the 20–35% baseline is specifically the retrieval contribution, not the full agentic ceiling. This argument exists implicitly but must be stated explicitly.", "LOW — EMNLP 2026 ARR deadline is not credible given current state: The May 25 deadline is 15 days away. To submit to ARR requires a complete written paper, full experimental results, and bibliography validation (EMNLP's hallucinated-citation warning is explicit). The paper's hedge ('if too close, defer') should be changed to a definitive decision: either commit to running minimum viable experiments starting immediately (DebugBench classifier calibration + Defects4J V1.2 with the 4 primary variants) or acknowledge ICSE 2027 as the sole target. Leaving it ambiguous signals poor project planning to co-authors and advisors."]
Feedback: Round 4 has successfully resolved all five issues from Round 3: CRAG citation is correct (arXiv-only), SWE-Exp is cited with three clear design differences, the random-partition control (Variant F) converts the corpus-size confound into a closed experimental question, EMNLP is downgraded to Findings, and ReinFix's implementation detail is softened. Independent verification confirms all cited paper claims are accurate. The hard-vs-soft retrieval comparison for semantic bug-type partitioned cross-repo repair is genuinely novel — no existing paper makes this specific comparison. Two actions are required for Round 5: (1) Read the TypeRepair SQJ 2026 paper (Zhang et al., doi:10.1007/s11219-026-09751-w) and add it to the landscape — the differentiation is either that TypeRepair uses intra-project context (state this explicitly) or that it uses cross-repo retrieval but covers only Java with a different pipeline structure (then FTCR's C++/Java/Python scope and the hard/soft comparison are the differentiators). (2) Cite and respond to 'What to Retrieve for Effective RAG Code Generation?' (ICSE 2026, arXiv:2503.20589): its finding that similar code retrieval degrades performance by 15% motivates FTCR's type-conditioning exactly — within a type partition, retrieved examples share fix structure rather than surface-level code similarity, which is the argument FTCR needs to make explicit. These two additions would resolve the remaining novelty and counterevidence gaps. The practical utility framing (retrieval as a modular component upgradeable within agentic pipelines) should be added as a paragraph in the introduction — this is the clearest answer to 'why does this matter when agentic methods dominate at 73%.'

### Round 5 review
Verdict: revise
Issues: ["CRITICAL — Target venue violates user requirements: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026, 15 days from today). The proposal now targets ICSE 2027 (abstract June 23, 2026) exclusively, a full year late and a different research community. Previous reviewers flagged EMNLP as infeasible given experiment state, but the requirement was not to change venues — it was to make the idea work within the constraint. If auto-research starts immediately (day 0), 10–14 days of experiments complete by ~May 23, leaving 2 days to finalize the paper for the May 25 ARR deadline. This is technically achievable but requires an explicit, committed execution plan with the NLP framing (X%/Y%/Z%/W% classifier calibration finding) as the lead contribution. The proposal must either restore EMNLP 2026 as the primary target with a day-by-day execution schedule, or explicitly acknowledge that it fails the user's venue constraint and accept that verdict.", "HIGH — 16-day timeline constraint met only by auto-research mode: The user's hard constraint is ≤16 days. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) exceed this by 8–12× and should not appear as viable execution paths in resource_estimate. The paper should flag auto-research (10–14 days) as the only constraint-compliant mode, or restructure the three modes to reflect feasible timelines.", "MEDIUM — InferFix (ESEC/FSE 2023, arXiv:2303.07263) is unmentioned prior art: Independently confirmed that InferFix uses bug type annotations and contrastive learning to retrieve 'semantically equivalent bugs and corresponding fixes of the same bug type' from an external repository corpus (InferredBugs, thousands of Java and C# repos). This is the closest non-trivial precursor to type-conditioned cross-repo repair retrieval and is not cited anywhere in the proposal. ICSE 2027 reviewers familiar with the APR literature will notice its absence. FTCR should differentiate explicitly: InferFix uses soft contrastive similarity (learned embedding grouping) not hard categorical index partitioning; it targets Java/C# from Infer static analysis findings, not the 18-category natural-bug taxonomy; and the corpus construction and evaluation differ. This differentiation is achievable in one paragraph but must be present.", "MEDIUM — Cross-system corpus quality confound inadequately flagged: The 'clean comparison' correctly uses the same 3,050-pair natural corpus for both FTCR and the ReinFix-style baseline, isolating partitioning as the variable. But any performance comparison against the published ReinFix results uses 100K TRANSFER corpus pairs (synthetic, from static analysis), creating a corpus quality × retrieval architecture confound that the random-partition control does not address. The paper must explicitly state: (a) intra-corpus ablations (FTCR vs. re-implemented ReinFix on 3,050 pairs) test the partitioning hypothesis cleanly, and (b) absolute comparisons against published ReinFix results reflect both architecture and corpus quality differences simultaneously.", "LOW — TypeRepair context-selection scope unverifiable from publicly accessible sources: The critical differentiation claim — that TypeRepair's Stage 3 selects within-project context only, not from an external cross-repo corpus — could not be independently confirmed due to paywall access to the SQJ article. The proposal states this confidently; it should note the evidentiary basis (e.g., 'TypeRepair evaluates exclusively on Defects4J/QuixBugs, which are within-project datasets, and the paper's supplementary prompt templates confirm type-specific in-project context selection rather than external retrieval') to avoid a reviewer flagging this differentiation as unsubstantiated."]
Feedback: This is the most polished version of FTCR to date. The random-partition control, confidence-gated hybrid, per-type merge policy, and ReinFix/SWE-Exp/TypeRepair differentiation all reflect genuine methodological rigor. Two actions would bring this to pass: (1) VENUE DECISION — the proposal must choose one of two paths and commit fully: either (a) restore EMNLP 2026 ARR (May 25) as the primary target with a specific day-by-day execution schedule (day 0-13: auto-research runs corpus annotation + DebugBench classifier calibration + Defects4J V1.2 ablations; day 13-15: paper writing with NLP lead framing the X%/Y%/Z%/W% falsifiable classifier finding), acknowledging the extreme timeline pressure; or (b) explicitly declare that the user's requirement cannot be met for EMNLP 2026 and accept ICSE 2027 as the sole target with a verdict of 'fail' on the original requirement. Leaving both venues while targeting neither by the May 25 deadline is a planning failure. (2) ADD INFERFIX — one paragraph in the landscape: 'InferFix (ESEC/FSE 2023, arXiv:2303.07263) retrieves fixes for bugs of the same type using contrastive-learned embeddings over bug type annotations, establishing type-aware retrieval for Java/C# static analysis bugs. FTCR differs in three respects: (a) hard categorical index partitioning at construction time rather than soft contrastive similarity at retrieval time; (b) 18-category natural-bug taxonomy across C++/Java/Python rather than InferBugs' Infer-specific defect categories; (c) direct comparison of hard vs. soft type conditioning as the scientific contribution.' If these two issues are resolved, the novelty and feasibility scores reach 3.5+ and the paper is close to a pass for ICSE 2027 (though not EMNLP 2026 unless the execution plan is credible).

### Round 6 review
Verdict: revise
Issues: ["HIGH — EMNLP Main vs. Findings target ambiguity persists: target_venues now lists 'EMNLP 2026 Main' AND 'EMNLP 2026 Findings' as separate entries, but the empirical calibration study (X%/Y%/Z%/W% LLM label reliability) is a measurement finding about LLM annotation quality — appropriate for EMNLP Findings, not the Main track, which expects findings that advance understanding of language models at a deeper level. Rounds 3 and 4 both explicitly downgraded the EMNLP target to Findings; Round 5 asked to restore EMNLP without specifying Main vs. Findings; Round 6 silently re-expanded to Main. The proposal must commit to EMNLP Findings as the EMNLP target and stop oscillating. Trying for Main and being desk-rejected wastes the submission cycle.", "MEDIUM — DebugBench hierarchical structure mischaracterized throughout: independently verified (ACL Findings 2024 paper) that DebugBench has 4 MAJOR categories (Syntax Bugs, Logic Bugs, Reference Bugs, Multiple Bugs) with 18 MINOR sub-types nested within them — not 18 independent categories. The proposal consistently refers to '18-category taxonomy' and '18-category natural-bug taxonomy aligned with DebugBench's taxonomy.' This is inaccurate and will flag with any reviewer who has read DebugBench. Concretely: the merge policy for rare types must operate within the 4-major/18-minor hierarchy (merge within major categories first, not across them); X%/Y%/Z%/W% measurements must specify whether they are measured at the major-type or minor-type level; and the '~31 Java instances per type' figure implies 18 equal partitions, which is not how the benchmark is structured.", "MEDIUM — Day-0-today execution assumption is unverified: the schedule commits to launching corpus annotation pipeline on May 10 (today) with 2 A100 nodes already available. No verification of compute availability, API rate limits on day 1, or Defects4J V1.2 Docker environment readiness is mentioned. If infrastructure setup takes 1–2 days (common in practice), the already-tight 2-day paper writing window (Days 13–15, May 23–25) disappears entirely. The proposal should either (a) confirm that compute is already provisioned and Docker environments tested, or (b) revise the schedule to account for a 1-day setup buffer by shifting MVS deliverables earlier.", "LOW — InferFix type-as-embedding-signal claim needs precision: independent verification found that InferFix adds bug type annotations as prompt context alongside retrieved fixes, while the contrastive retriever learns semantic similarity between bugs/fixes. The proposal claims 'type influences embedding proximity rather than pool membership' — this framing appears broadly correct but needs verification against the actual retriever architecture section (Section 3 of arXiv:2303.07263), not just the abstract. If InferFix's retriever does NOT explicitly condition on type labels during encoding (only using type for post-retrieval prompt augmentation), the 'soft type conditioning' differentiation needs rewording to 'type-correlated semantic similarity' to avoid misrepresenting the baseline.", "LOW — Statistical significance for Z% and W% unstated: the Z% (repair improvement for correctly classified) and W% (repair degradation for misclassified) measurements will have unequal sample sizes depending on classifier accuracy. With ~31 Java instances per minor type and a 20% held-out split (~6 per type), per-type statistical tests are underpowered. The proposal should specify: (a) whether Z% and W% are aggregated across all types or reported per type; (b) what statistical test is used; (c) minimum sample threshold for a type to contribute to the Z%/W% comparison."]
Feedback: Round 6 has addressed all five Round 5 issues: EMNLP venue restored with committed schedule, InferFix added with three-point differentiation, corpus confound made explicit, TypeRepair evidentiary basis stated, resource estimate stripped to auto-research only. The core hypothesis is well-posed and the experimental design is increasingly rigorous. Three targeted fixes would make this submission-ready: (1) COMMIT TO EMNLP FINDINGS — remove 'EMNLP 2026 Main' from target_venues and replace with 'EMNLP 2026 Findings (via ARR)'. The X%/Y%/Z%/W% calibration study is a strong Findings paper; attempting Main track risks desk rejection on NLP-contribution grounds and wastes the submission cycle. (2) FIX DEBUGBENCH STRUCTURE — replace every instance of '18-category' with '4-major/18-minor hierarchical taxonomy' and state that X%/Y%/Z%/W% measurements operate at the minor-type level (18 sub-categories), with major-type aggregation reported as a secondary result. Revise the merge policy to explicitly merge within the same major category first (e.g., merge rare Reference Bug sub-types before merging across Logic and Reference). (3) CONFIRM COMPUTE READINESS — add one sentence to the Day 0 entry: 'Compute: 2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.' If this cannot be stated truthfully, shift the MVS timeline by 1 day and compress paper writing to 1 day with a more aggressive pre-drafted skeleton policy. These three changes are low-effort and directly address verifiable gaps; the underlying science is solid and the proposal is close to submission-ready for EMNLP 2026 Findings.


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
  "promptId": "700da751-e77a-463d-863b-f81ff1e1c257",
  "type": "user",
  "uuid": "037ca502-5c54-4fd4-b6dd-52792d067df2",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:00:49.418Z_

```json
{
  "parentUuid": "037ca502-5c54-4fd4-b6dd-52792d067df2",
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
  "uuid": "eb77a11d-d77a-4998-b8c1-4402f8c61738",
  "timestamp": "2026-05-10T07:00:49.418Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:00:49.418Z_

```json
{
  "parentUuid": "eb77a11d-d77a-4998-b8c1-4402f8c61738",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5795f0ce-219e-42b4-88be-b4e1f9ff4bac",
  "timestamp": "2026-05-10T07:00:49.418Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116",
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
  "leafUuid": "5795f0ce-219e-42b4-88be-b4e1f9ff4bac",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate FTCR for EMNLP 2026 ARR Submission (Round 7)",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:01:03.852Z_

<details><summary>Logged reasoning block</summary>

```text
This is Round 7 of 10 for a paper review. I need to conduct an independent adversarial review of "Failure-Type-Conditioned Retrieval Augmentation for Repository Repair" (FTCR). Let me carefully analyze the current state of the proposal and conduct independent research to verify claims.

The proposal has gone through 6 rounds of revisions. The main issues addressed in Round 6 were:
1. Commit to EMNLP Findings (not Main)
2. Fix DebugBench structure to 4-major/18-minor hierarchical taxonomy
3. Confirm compute readiness


4. Correct InferFix architecture
5. Specify statistical significance

Now I'm systematically verifying the core claims—checking whether the cited papers are real and accurately represented, searching for competing work the authors might have overlooked, and looking for any counterevidence that challenges their SOTA positioning. I need to assess the feasibility, novelty, clarity, and potential impact of this work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5795f0ce-219e-42b4-88be-b4e1f9ff4bac",
  "isSidechain": false,
  "requestId": "req_011CatTVXMeAjLKRwLFgKHkU",
  "type": "assistant",
  "uuid": "fb9dd7e4-0bed-419f-8b2a-bafef9936cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0153vxZFSBwjDC8U3JJt7fWX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29701,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1873,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1873,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 29701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29701
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

_source line 9 · 2026-05-10T07:01:03.876Z_

I'll conduct independent verification searches to assess this Round 7 proposal before issuing a verdict.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb9dd7e4-0bed-419f-8b2a-bafef9936cb1",
  "isSidechain": false,
  "requestId": "req_011CatTVXMeAjLKRwLFgKHkU",
  "type": "assistant",
  "uuid": "fce805b2-d679-4094-ab06-5701d40c2ffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0153vxZFSBwjDC8U3JJt7fWX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29701,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1873,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1873,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 29701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29701
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

_source line 10 · 2026-05-10T07:01:13.576Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01X2duVDp6xHes59Z7WH36xB`</summary>

```json
{
  "description": "Adversarial review research for FTCR paper",
  "subagent_type": "general-purpose",
  "prompt": "You are helping conduct an adversarial review of a paper proposal called \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\" (FTCR). Your job is to conduct independent research to verify or challenge the paper's claims. Do NOT accept anything at face value — you must independently verify.\n\nPlease conduct the following specific searches and report your findings in detail:\n\n1. Search for DebugBench paper to verify its exact taxonomy structure: \"DebugBench ACL 2024\" and \"DebugBench evaluating debugging LLM 4253\". Report the exact structure (is it 4 major + 18 minor? What are the sub-types exactly?)\n\n2. Search for InferFix paper to verify its architecture: \"InferFix program repair LLM FSE 2023\" and \"InferFix arXiv 2303.07263\". Specifically: does InferFix use hard categorical index partitioning or soft contrastive similarity? Does it require Infer static analyzer at inference time?\n\n3. Search for ReinFix paper: \"ReinFix repair ingredients ICSE 2026\" and \"ReinFix arXiv 2506.23100\". Verify it's ICSE 2026 (not 2025), and verify its mechanism (soft root-cause embedding, text-embedding-3-large).\n\n4. Search for concurrent work: \"type-conditioned retrieval program repair 2025 2026\", \"categorical type partition retrieval code repair\", \"bug type classification retrieval augmented repair 2025\". Look for any papers that do hard categorical partitioning for code repair retrieval that may have been missed.\n\n5. Search for SWE-Exp: \"SWE-Exp experience bank software issue resolution arXiv 2507.23361\". Verify whether it uses hard or soft type conditioning.\n\n6. Search for TypeRepair: \"TypeRepair defect-type-aware program repair Zhang 2026 Software Quality Journal\". Try to verify whether its Stage 3 context selection uses within-project code only or external cross-repository retrieval.\n\n7. Search for recent concurrent work that might challenge novelty: \"retrieval augmented program repair taxonomy 2026\", \"LLM bug type classification retrieval 2025 2026\", \"partition-based retrieval code repair arxiv 2026\".\n\n8. Check EMNLP 2026 ARR deadline: search \"EMNLP 2026 ARR deadline May 2026\" to verify the submission deadline is indeed May 25, 2026.\n\nFor each search, report: what you found, the URL, and whether it confirms or challenges the paper's claims. Be specific and quote relevant passages where possible. Use WebSearch and WebFetch tools to read actual papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fce805b2-d679-4094-ab06-5701d40c2ffc",
  "isSidechain": false,
  "requestId": "req_011CatTVXMeAjLKRwLFgKHkU",
  "type": "assistant",
  "uuid": "7aa2f3a8-d269-4caf-9e14-732396d11bcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0153vxZFSBwjDC8U3JJt7fWX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29701,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1873,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1873,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 29701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29701
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

_source line 11 · 2026-05-10T07:01:25.099Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Ff3f7vAR4a3EmbANjCwQWv`</summary>

```json
{
  "description": "Search for competing/concurrent work for FTCR review",
  "subagent_type": "general-purpose",
  "prompt": "You are helping conduct an adversarial review of a paper called \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\" (FTCR). The paper proposes:\n1. A retrieval system for program repair that partitions a bug-fix corpus by bug TYPE (hard categorical partitioning)\n2. Uses LLM-inferred bug type labels from an 18-sub-type taxonomy (DebugBench-derived: Syntax, Reference, Logic categories)\n3. Claims this outperforms soft semantic retrieval (like ReinFix's root-cause embedding approach)\n4. Evaluates on DebugBench and Defects4J V1.2\n\nYour job: Find papers that the FTCR proposal may have MISSED that could challenge its novelty claims. Focus especially on:\n\n1. Search arXiv for very recent work (2025-2026): \"site:arxiv.org hard type partition retrieval repair 2026\", \"arxiv bug taxonomy retrieval augmented repair 2025 2026\"\n\n2. Search for papers on LLM-based bug classification accuracy: \"LLM bug type classification accuracy taxonomy 2025\", \"LLM defect classification evaluation benchmark 2025 2026\"\n\n3. Search paperswithcode for APR/program repair SOTA: \"paperswithcode automated program repair 2026 state of the art\", \"paperswithcode DebugBench benchmark leaderboard\"\n\n4. Search for RAG partition approaches in code: \"multi-partition RAG code repair 2025\", \"type-aware retrieval augmented generation code 2026\"\n\n5. Search for any work using DebugBench for retrieval: \"DebugBench retrieval augmented repair\", \"DebugBench type taxonomy retrieval\"\n\n6. Search for DynaFix and DebugRepair to verify they're real and what they achieve: \"DynaFix arXiv 2512.24635 program repair\", \"DebugRepair arXiv 2604.19305\"\n\n7. Search for ReCode CIKM 2025: \"ReCode algorithm-type retrieval CIKM 2025 arXiv 2509.02330\"\n\n8. Search for the APR survey: \"survey LLM automated program repair arXiv 2506.23749 63 systems\"\n\nReport findings with URLs, noting if any paper directly challenges FTCR's novelty claims. Pay special attention to any paper that does hard categorical partitioning + retrieval for code repair — that would be a direct competitor."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7aa2f3a8-d269-4caf-9e14-732396d11bcf",
  "isSidechain": false,
  "requestId": "req_011CatTVXMeAjLKRwLFgKHkU",
  "type": "assistant",
  "uuid": "46b0d409-43c8-493d-93c0-1f3acbb3a3b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0153vxZFSBwjDC8U3JJt7fWX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29701,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1873,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29701,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1873,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 29701,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29701
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

_source line 12 · 2026-05-10T07:05:12.667Z_

<details><summary>↩ Tool result · `toolu_01Ff3f7vAR4a3EmbANjCwQWv`</summary>

```text
I now have comprehensive results across all search categories. Let me compile the full adversarial review report.

---

## Adversarial Review: Papers That Challenge FTCR's Novelty Claims

Here is the full findings report, organized by threat level to FTCR's contributions.

---

### CRITICAL THREATS — Direct Prior Art for Hard Categorical Partition + Retrieval for Code Repair

**1. ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation**
- arXiv: [2509.02330](https://arxiv.org/abs/2509.02330) (September 2025; associated with CIKM 2025, Seoul)
- **This is FTCR's most direct competitor and likely the most damaging prior art.** ReCode does exactly what FTCR claims as novel: it uses LLM-inferred type labels (algorithm types: greedy, binary search, DP, graph, number theory, etc.) to partition a code-fix knowledge base into sub-knowledge bases, then performs parallel semantic retrieval within the predicted partition. Key architectural parallels to FTCR:
  - Hard categorical partitioning of the retrieval corpus by type label
  - LLM predicts multiple type labels (multi-label classification) before retrieval
  - Semantic retrieval within the predicted sub-knowledge bases in parallel
  - Dual-encoder (code + text features) for intra-partition retrieval
  - Evaluated on a dedicated benchmark (RACodeBench, derived from Codeforces) with stratified error-type sampling
- The only apparent difference from FTCR is that ReCode uses *algorithm-type* labels (domain of the problem) rather than *bug-type* labels (failure category). FTCR must explicitly address this distinction and argue why bug-type partitioning is non-obvious or superior.

---

### HIGH THREATS — Papers That Narrow or Precede Key Claims

**2. ReinFix (also titled "Repair Ingredients Are All You Need")**
- arXiv: [2506.23100](https://arxiv.org/abs/2506.23100) (June 2025; accepted ICSE 2026)
- The paper with this arXiv ID turns out to be "ReinFix," which is apparently the same ReinFix that FTCR claims to beat. FTCR presents ReinFix as a "soft semantic retrieval" baseline. But the paper title — "Repair Ingredients Are All You Need" — and its ICSE 2026 acceptance date mean that if FTCR was submitted before June 2025, the comparison may be fine; if submitted later, it needs to engage with this version carefully. ReinFix (per this paper) uses root-cause analysis in reasoning + external historical bug-fix retrieval in the solution phase, fixes 146 bugs on Defects4J V1.2 with GPT-4. FTCR claiming to "outperform soft semantic retrieval" must match or beat this exact number.

**3. RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code**
- arXiv: [2509.16701](https://arxiv.org/abs/2509.16701) (September 2025)
- Retrieval-augmented repair evaluated on Defects4J V1.2, repairs 101 bugs. Uses query rewriting + project-specific function signature and snippet retrieval. Not categorical partition, but a competitor baseline FTCR must include if claiming SOTA on Defects4J V1.2.

**4. DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information**
- arXiv: [2512.24635](https://arxiv.org/abs/2512.24635) (December 2025) — CONFIRMED REAL
- Repairs 236 single-function bugs on Defects4J V2.0 with GPT-4, and outperforms ReinFix by 52 bugs (+32.1%) with DeepSeek-V3.2. If FTCR evaluates on Defects4J and doesn't cite DynaFix (which was available December 2025), the related work section has a gap.

**5. DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging**
- arXiv: [2604.19305](https://arxiv.org/abs/2604.19305) (April 2026) — CONFIRMED REAL
- Fixes 295 Defects4J bugs with DeepSeek-V3, exceeding second-best by 59. Uses simulated instrumentation and test semantic purification rather than retrieval. This is very recent SOTA and FTCR almost certainly postdates this; if FTCR claims SOTA on Defects4J, it needs to engage with DebugRepair's 295-bug result.

---

### SIGNIFICANT THREATS — LLM Annotation Accuracy Directly Undermines Core Assumption

**6. "What's Wrong with Your Code Generated by Large Language Models?" (Extensive Study)**
- arXiv: [2407.06153](https://arxiv.org/abs/2407.06153) (2024)
- **This directly attacks FTCR's foundational assumption.** The study used GPT-4 to automatically classify bugs into a 3-level taxonomy and measured accuracy against human annotation:
  - Tertiary category (fine-grained) fully automated accuracy: **5.2%**
  - Secondary category fully automated accuracy: **35.7%**
  - AI-assisted (human-in-loop) accuracy: 84.4%
- FTCR uses LLM-inferred bug type labels from an 18-subtype taxonomy (which maps to tertiary/secondary levels). If FTCR's type labels are inferred with ~5–35% accuracy, the correctness of the partition boundary is questionable. FTCR must either report its own label accuracy numbers or explain why its labeling approach avoids this degradation.

---

### MODERATE THREATS — Related Work Gaps

**7. A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications**
- arXiv: [2506.23749](https://arxiv.org/abs/2506.23749) (June 2025; v2 title: "A Survey of LLM-based Software Repair")
- Catalogs 63 LLM-based APR systems from 2022–2025 into four paradigms (Fine-Tuning, Prompting, Procedural, Agentic), with retrieval-augmented and analysis-augmented approaches as cross-cutting overlays. If FTCR doesn't cite this survey, reviewers will notice immediately. The survey explicitly covers retrieval-augmented repair and may have directly comparable systems FTCR omits from its related work section.
- GitHub companion: https://github.com/GLEAM-Lab/ProgramRepair

**8. Hierarchical Knowledge Injection for Improving LLM-Based Program Repair (arXiv 2506.24015)**
- A.k.a. "Bug Fixing with Broader Context"
- arXiv: [2506.24015](https://arxiv.org/abs/2506.24015) (June 2025)
- Achieves 79% fix rate (250/314) on BugsInPy using Llama 3.3 (+23% improvement). Key finding: different bug types require different levels of contextual information for effective repair — this is related to FTCR's thesis but uses layered (hierarchical) rather than partitioned approaches. If FTCR doesn't cite this, it leaves a gap in justifying why categorical partition beats layered injection.

**9. ExpeRepair: Dual-Memory Enhanced LLM-based Repository-Level Program Repair**
- arXiv: [2506.10484](https://arxiv.org/abs/2506.10484) (June 2025)
- Achieves 49.3% pass@1 on SWE-bench Lite with Claude 3.7 Sonnet (SOTA among open-source at submission time). Uses episodic + semantic dual memory for retrieval. Not directly comparable to DebugBench/Defects4J, but the episodic memory is semantically similar to FTCR's historical-fix retrieval corpus, and FTCR should engage with it.

**10. SelRepair (arXiv 2507.10103)**
- Full title: "Accelerating Automatic Program Repair with Dual Retrieval-Augmented Fine-Tuning and Patch Generation on Large Language Models"
- arXiv: [2507.10103](https://arxiv.org/abs/2507.10103) (July 2025)
- Dual RAG combining semantic + syntactic/structural retrieval with selection gate. Another retrieval-augmented repair baseline FTCR should compare against on Defects4J.

**11. LTFix / Typestate-Guided Context Retrieval (arXiv 2506.18394)**
- Full title: "Tracing Errors, Constructing Fixes: Repository-Level Memory Error Repair via Typestate-Guided Context Retrieval"
- arXiv: [2506.18394](https://arxiv.org/abs/2506.18394) (June 2025)
- Type-guided (typestate automaton) retrieval for memory errors in C. A domain-specific variant of type-conditioned retrieval — directly relevant to FTCR's "type-aware retrieval" framing.

**12. Learner-Tailored Program Repair (arXiv 2601.08545)**
- arXiv: [2601.08545](https://arxiv.org/abs/2601.08545) (January 2026)
- Introduces LPR-Bench (student buggy programs + correct versions + retrieval database) and an edit-driven iterative retrieval approach. A competitor for the DebugBench-style evaluation setting.

---

### CONTEXTUAL NOTE — Papers with Code Shutdown

Papers with Code was shut down by Meta in July 2025. FTCR cannot cite PwC leaderboards as evidence of SOTA standing. The DebugBench leaderboard is no longer maintained there. FTCR should note alternative tracking via [HuggingFace trending](https://paperswithcode.com/) or the GLEAM-Lab survey GitHub repo.

---

### Summary Table of Novelty Threats

| Paper | arXiv ID | Threat | Why |
|---|---|---|---|
| ReCode | 2509.02330 | **CRITICAL** | Does hard type-partition + LLM type inference + parallel sub-KB retrieval for code repair — same core mechanism as FTCR |
| LLM annotation accuracy study | 2407.06153 | **HIGH** | LLM auto-labeling of fine-grained bug types achieves only 5.2–35.7% accuracy; directly undermines FTCR's labeling step |
| ReinFix (ICSE 2026) | 2506.23100 | **HIGH** | The baseline FTCR claims to beat is accepted at ICSE 2026 with strong Defects4J V1.2 numbers (146 bugs, GPT-4) |
| DebugRepair | 2604.19305 | **HIGH** | Current SOTA on Defects4J (295 bugs with DeepSeek-V3); FTCR must either beat this or predate it |
| DynaFix | 2512.24635 | **MODERATE** | Strongly outperforms ReinFix on Defects4J V2.0; likely uncited in FTCR |
| APR Survey | 2506.23749 | **MODERATE** | Catalogs 63 systems; absence from FTCR related work is conspicuous |
| LTFix | 2506.18394 | **MODERATE** | Type-guided retrieval for code repair (typestate-conditioned) |
| HKI / Bug Fixing with Layers | 2506.24015 | **MODERATE** | Bug-type-specific context injection; related framing to FTCR |
| RelRepair | 2509.16701 | **LOW** | RAG repair on Defects4J V1.2 (101 bugs); baseline gap |
| SelRepair | 2507.10103 | **LOW** | Dual RAG for APR; uncited baseline |

The single most damaging paper is **ReCode (arXiv 2509.02330)**, which implements the same hard-partition + LLM-type-inference + sub-corpus-retrieval pipeline as FTCR but using algorithm types. FTCR must either cite it as prior work (sharply narrowing its novelty claim) or demonstrate that *bug-type* partitioning is non-trivially distinct from *algorithm-type* partitioning and produces different architectural/empirical outcomes. The second most damaging finding is the **5.2% fully-automated tertiary-label accuracy** from arXiv 2407.06153, which calls into question whether LLM-inferred bug type labels at the 18-subtype granularity are reliable enough to gate retrieval partitions.

Sources:
- [ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation](https://arxiv.org/abs/2509.02330)
- [DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information](https://arxiv.org/abs/2512.24635)
- [DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging](https://arxiv.org/html/2604.19305v1)
- [A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications](https://arxiv.org/abs/2506.23749)
- [Repair Ingredients Are All You Need (ReinFix, ICSE 2026)](https://arxiv.org/abs/2506.23100)
- [Hierarchical Knowledge Injection for Improving LLM-based Program Repair](https://arxiv.org/abs/2506.24015)
- [ExpeRepair: Dual-Memory Enhanced LLM-based Repository-Level Program Repair](https://arxiv.org/abs/2506.10484)
- [RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code](https://arxiv.org/abs/2509.16701)
- [Accelerating Automatic Program Repair with Dual Retrieval-Augmented Fine-Tuning (SelRepair)](https://arxiv.org/abs/2507.10103)
- [Tracing Errors, Constructing Fixes: Repository-Level Memory Error Repair via Typestate-Guided Context Retrieval (LTFix)](https://arxiv.org/abs/2506.18394)
- [Learner-Tailored Program Repair: Iterative Edit-Driven Retrieval Enhancement](https://arxiv.org/abs/2601.08545)
- [What's Wrong with Your Code Generated by Large Language Models? (Bug annotation accuracy study)](https://arxiv.org/abs/2407.06153)
- [DebugBench: Evaluating Debugging Capability of Large Language Models](https://arxiv.org/abs/2401.04621)

agentId: a19d11bc0e201e7ba (use SendMessage with to: 'a19d11bc0e201e7ba' to continue this agent)
&lt;usage>total_tokens: 45691
tool_uses: 34
duration_ms: 227564&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46b0d409-43c8-493d-93c0-1f3acbb3a3b5",
  "isSidechain": false,
  "promptId": "700da751-e77a-463d-863b-f81ff1e1c257",
  "type": "user",
  "uuid": "c45a6760-bd3b-434e-a2f8-5946b10d5073",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping conduct an adversarial review of a paper called \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\" (FTCR). The paper proposes:\n1. A retrieval system for program repair that partitions a bug-fix corpus by bug TYPE (hard categorical partitioning)\n2. Uses LLM-inferred bug type labels from an 18-sub-type taxonomy (DebugBench-derived: Syntax, Reference, Logic categories)\n3. Claims this outperforms soft semantic retrieval (like ReinFix's root-cause embedding approach)\n4. Evaluates on DebugBench and Defects4J V1.2\n\nYour job: Find papers that the FTCR proposal may have MISSED that could challenge its novelty claims. Focus especially on:\n\n1. Search arXiv for very recent work (2025-2026): \"site:arxiv.org hard type partition retrieval repair 2026\", \"arxiv bug taxonomy retrieval augmented repair 2025 2026\"\n\n2. Search for papers on LLM-based bug classification accuracy: \"LLM bug type classification accuracy taxonomy 2025\", \"LLM defect classification evaluation benchmark 2025 2026\"\n\n3. Search paperswithcode for APR/program repair SOTA: \"paperswithcode automated program repair 2026 state of the art\", \"paperswithcode DebugBench benchmark leaderboard\"\n\n4. Search for RAG partition approaches in code: \"multi-partition RAG code repair 2025\", \"type-aware retrieval augmented generation code 2026\"\n\n5. Search for any work using DebugBench for retrieval: \"DebugBench retrieval augmented repair\", \"DebugBench type taxonomy retrieval\"\n\n6. Search for DynaFix and DebugRepair to verify they're real and what they achieve: \"DynaFix arXiv 2512.24635 program repair\", \"DebugRepair arXiv 2604.19305\"\n\n7. Search for ReCode CIKM 2025: \"ReCode algorithm-type retrieval CIKM 2025 arXiv 2509.02330\"\n\n8. Search for the APR survey: \"survey LLM automated program repair arXiv 2506.23749 63 systems\"\n\nReport findings with URLs, noting if any paper directly challenges FTCR's novelty claims. Pay special attention to any paper that does hard categorical partitioning + retrieval for code repair — that would be a direct competitor.",
    "agentId": "a19d11bc0e201e7ba",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive results across all search categories. Let me compile the full adversarial review report.\n\n---\n\n## Adversarial Review: Papers That Challenge FTCR's Novelty Claims\n\nHere is the full findings report, organized by threat level to FTCR's contributions.\n\n---\n\n### CRITICAL THREATS — Direct Prior Art for Hard Categorical Partition + Retrieval for Code Repair\n\n**1. ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation**\n- arXiv: [2509.02330](https://arxiv.org/abs/2509.02330) (September 2025; associated with CIKM 2025, Seoul)\n- **This is FTCR's most direct competitor and likely the most damaging prior art.** ReCode does exactly what FTCR claims as novel: it uses LLM-inferred type labels (algorithm types: greedy, binary search, DP, graph, number theory, etc.) to partition a code-fix knowledge base into sub-knowledge bases, then performs parallel semantic retrieval within the predicted partition. Key architectural parallels to FTCR:\n  - Hard categorical partitioning of the retrieval corpus by type label\n  - LLM predicts multiple type labels (multi-label classification) before retrieval\n  - Semantic retrieval within the predicted sub-knowledge bases in parallel\n  - Dual-encoder (code + text features) for intra-partition retrieval\n  - Evaluated on a dedicated benchmark (RACodeBench, derived from Codeforces) with stratified error-type sampling\n- The only apparent difference from FTCR is that ReCode uses *algorithm-type* labels (domain of the problem) rather than *bug-type* labels (failure category). FTCR must explicitly address this distinction and argue why bug-type partitioning is non-obvious or superior.\n\n---\n\n### HIGH THREATS — Papers That Narrow or Precede Key Claims\n\n**2. ReinFix (also titled \"Repair Ingredients Are All You Need\")**\n- arXiv: [2506.23100](https://arxiv.org/abs/2506.23100) (June 2025; accepted ICSE 2026)\n- The paper with this arXiv ID turns out to be \"ReinFix,\" which is apparently the same ReinFix that FTCR claims to beat. FTCR presents ReinFix as a \"soft semantic retrieval\" baseline. But the paper title — \"Repair Ingredients Are All You Need\" — and its ICSE 2026 acceptance date mean that if FTCR was submitted before June 2025, the comparison may be fine; if submitted later, it needs to engage with this version carefully. ReinFix (per this paper) uses root-cause analysis in reasoning + external historical bug-fix retrieval in the solution phase, fixes 146 bugs on Defects4J V1.2 with GPT-4. FTCR claiming to \"outperform soft semantic retrieval\" must match or beat this exact number.\n\n**3. RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code**\n- arXiv: [2509.16701](https://arxiv.org/abs/2509.16701) (September 2025)\n- Retrieval-augmented repair evaluated on Defects4J V1.2, repairs 101 bugs. Uses query rewriting + project-specific function signature and snippet retrieval. Not categorical partition, but a competitor baseline FTCR must include if claiming SOTA on Defects4J V1.2.\n\n**4. DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information**\n- arXiv: [2512.24635](https://arxiv.org/abs/2512.24635) (December 2025) — CONFIRMED REAL\n- Repairs 236 single-function bugs on Defects4J V2.0 with GPT-4, and outperforms ReinFix by 52 bugs (+32.1%) with DeepSeek-V3.2. If FTCR evaluates on Defects4J and doesn't cite DynaFix (which was available December 2025), the related work section has a gap.\n\n**5. DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging**\n- arXiv: [2604.19305](https://arxiv.org/abs/2604.19305) (April 2026) — CONFIRMED REAL\n- Fixes 295 Defects4J bugs with DeepSeek-V3, exceeding second-best by 59. Uses simulated instrumentation and test semantic purification rather than retrieval. This is very recent SOTA and FTCR almost certainly postdates this; if FTCR claims SOTA on Defects4J, it needs to engage with DebugRepair's 295-bug result.\n\n---\n\n### SIGNIFICANT THREATS — LLM Annotation Accuracy Directly Undermines Core Assumption\n\n**6. \"What's Wrong with Your Code Generated by Large Language Models?\" (Extensive Study)**\n- arXiv: [2407.06153](https://arxiv.org/abs/2407.06153) (2024)\n- **This directly attacks FTCR's foundational assumption.** The study used GPT-4 to automatically classify bugs into a 3-level taxonomy and measured accuracy against human annotation:\n  - Tertiary category (fine-grained) fully automated accuracy: **5.2%**\n  - Secondary category fully automated accuracy: **35.7%**\n  - AI-assisted (human-in-loop) accuracy: 84.4%\n- FTCR uses LLM-inferred bug type labels from an 18-subtype taxonomy (which maps to tertiary/secondary levels). If FTCR's type labels are inferred with ~5–35% accuracy, the correctness of the partition boundary is questionable. FTCR must either report its own label accuracy numbers or explain why its labeling approach avoids this degradation.\n\n---\n\n### MODERATE THREATS — Related Work Gaps\n\n**7. A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications**\n- arXiv: [2506.23749](https://arxiv.org/abs/2506.23749) (June 2025; v2 title: \"A Survey of LLM-based Software Repair\")\n- Catalogs 63 LLM-based APR systems from 2022–2025 into four paradigms (Fine-Tuning, Prompting, Procedural, Agentic), with retrieval-augmented and analysis-augmented approaches as cross-cutting overlays. If FTCR doesn't cite this survey, reviewers will notice immediately. The survey explicitly covers retrieval-augmented repair and may have directly comparable systems FTCR omits from its related work section.\n- GitHub companion: https://github.com/GLEAM-Lab/ProgramRepair\n\n**8. Hierarchical Knowledge Injection for Improving LLM-Based Program Repair (arXiv 2506.24015)**\n- A.k.a. \"Bug Fixing with Broader Context\"\n- arXiv: [2506.24015](https://arxiv.org/abs/2506.24015) (June 2025)\n- Achieves 79% fix rate (250/314) on BugsInPy using Llama 3.3 (+23% improvement). Key finding: different bug types require different levels of contextual information for effective repair — this is related to FTCR's thesis but uses layered (hierarchical) rather than partitioned approaches. If FTCR doesn't cite this, it leaves a gap in justifying why categorical partition beats layered injection.\n\n**9. ExpeRepair: Dual-Memory Enhanced LLM-based Repository-Level Program Repair**\n- arXiv: [2506.10484](https://arxiv.org/abs/2506.10484) (June 2025)\n- Achieves 49.3% pass@1 on SWE-bench Lite with Claude 3.7 Sonnet (SOTA among open-source at submission time). Uses episodic + semantic dual memory for retrieval. Not directly comparable to DebugBench/Defects4J, but the episodic memory is semantically similar to FTCR's historical-fix retrieval corpus, and FTCR should engage with it.\n\n**10. SelRepair (arXiv 2507.10103)**\n- Full title: \"Accelerating Automatic Program Repair with Dual Retrieval-Augmented Fine-Tuning and Patch Generation on Large Language Models\"\n- arXiv: [2507.10103](https://arxiv.org/abs/2507.10103) (July 2025)\n- Dual RAG combining semantic + syntactic/structural retrieval with selection gate. Another retrieval-augmented repair baseline FTCR should compare against on Defects4J.\n\n**11. LTFix / Typestate-Guided Context Retrieval (arXiv 2506.18394)**\n- Full title: \"Tracing Errors, Constructing Fixes: Repository-Level Memory Error Repair via Typestate-Guided Context Retrieval\"\n- arXiv: [2506.18394](https://arxiv.org/abs/2506.18394) (June 2025)\n- Type-guided (typestate automaton) retrieval for memory errors in C. A domain-specific variant of type-conditioned retrieval — directly relevant to FTCR's \"type-aware retrieval\" framing.\n\n**12. Learner-Tailored Program Repair (arXiv 2601.08545)**\n- arXiv: [2601.08545](https://arxiv.org/abs/2601.08545) (January 2026)\n- Introduces LPR-Bench (student buggy programs + correct versions + retrieval database) and an edit-driven iterative retrieval approach. A competitor for the DebugBench-style evaluation setting.\n\n---\n\n### CONTEXTUAL NOTE — Papers with Code Shutdown\n\nPapers with Code was shut down by Meta in July 2025. FTCR cannot cite PwC leaderboards as evidence of SOTA standing. The DebugBench leaderboard is no longer maintained there. FTCR should note alternative tracking via [HuggingFace trending](https://paperswithcode.com/) or the GLEAM-Lab survey GitHub repo.\n\n---\n\n### Summary Table of Novelty Threats\n\n| Paper | arXiv ID | Threat | Why |\n|---|---|---|---|\n| ReCode | 2509.02330 | **CRITICAL** | Does hard type-partition + LLM type inference + parallel sub-KB retrieval for code repair — same core mechanism as FTCR |\n| LLM annotation accuracy study | 2407.06153 | **HIGH** | LLM auto-labeling of fine-grained bug types achieves only 5.2–35.7% accuracy; directly undermines FTCR's labeling step |\n| ReinFix (ICSE 2026) | 2506.23100 | **HIGH** | The baseline FTCR claims to beat is accepted at ICSE 2026 with strong Defects4J V1.2 numbers (146 bugs, GPT-4) |\n| DebugRepair | 2604.19305 | **HIGH** | Current SOTA on Defects4J (295 bugs with DeepSeek-V3); FTCR must either beat this or predate it |\n| DynaFix | 2512.24635 | **MODERATE** | Strongly outperforms ReinFix on Defects4J V2.0; likely uncited in FTCR |\n| APR Survey | 2506.23749 | **MODERATE** | Catalogs 63 systems; absence from FTCR related work is conspicuous |\n| LTFix | 2506.18394 | **MODERATE** | Type-guided retrieval for code repair (typestate-conditioned) |\n| HKI / Bug Fixing with Layers | 2506.24015 | **MODERATE** | Bug-type-specific context injection; related framing to FTCR |\n| RelRepair | 2509.16701 | **LOW** | RAG repair on Defects4J V1.2 (101 bugs); baseline gap |\n| SelRepair | 2507.10103 | **LOW** | Dual RAG for APR; uncited baseline |\n\nThe single most damaging paper is **ReCode (arXiv 2509.02330)**, which implements the same hard-partition + LLM-type-inference + sub-corpus-retrieval pipeline as FTCR but using algorithm types. FTCR must either cite it as prior work (sharply narrowing its novelty claim) or demonstrate that *bug-type* partitioning is non-trivially distinct from *algorithm-type* partitioning and produces different architectural/empirical outcomes. The second most damaging finding is the **5.2% fully-automated tertiary-label accuracy** from arXiv 2407.06153, which calls into question whether LLM-inferred bug type labels at the 18-subtype granularity are reliable enough to gate retrieval partitions.\n\nSources:\n- [ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation](https://arxiv.org/abs/2509.02330)\n- [DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information](https://arxiv.org/abs/2512.24635)\n- [DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging](https://arxiv.org/html/2604.19305v1)\n- [A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications](https://arxiv.org/abs/2506.23749)\n- [Repair Ingredients Are All You Need (ReinFix, ICSE 2026)](https://arxiv.org/abs/2506.23100)\n- [Hierarchical Knowledge Injection for Improving LLM-based Program Repair](https://arxiv.org/abs/2506.24015)\n- [ExpeRepair: Dual-Memory Enhanced LLM-based Repository-Level Program Repair](https://arxiv.org/abs/2506.10484)\n- [RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code](https://arxiv.org/abs/2509.16701)\n- [Accelerating Automatic Program Repair with Dual Retrieval-Augmented Fine-Tuning (SelRepair)](https://arxiv.org/abs/2507.10103)\n- [Tracing Errors, Constructing Fixes: Repository-Level Memory Error Repair via Typestate-Guided Context Retrieval (LTFix)](https://arxiv.org/abs/2506.18394)\n- [Learner-Tailored Program Repair: Iterative Edit-Driven Retrieval Enhancement](https://arxiv.org/abs/2601.08545)\n- [What's Wrong with Your Code Generated by Large Language Models? (Bug annotation accuracy study)](https://arxiv.org/abs/2407.06153)\n- [DebugBench: Evaluating Debugging Capability of Large Language Models](https://arxiv.org/abs/2401.04621)"
      }
    ],
    "totalDurationMs": 227564,
    "totalTokens": 45691,
    "totalToolUseCount": 34,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 40169,
      "output_tokens": 3740,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1781
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3740,
          "cache_read_input_tokens": 40169,
          "cache_creation_input_tokens": 1781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1781,
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
      "otherToolCount": 34
    }
  },
  "sourceToolAssistantUUID": "46b0d409-43c8-493d-93c0-1f3acbb3a3b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116",
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
  "leafUuid": "c45a6760-bd3b-434e-a2f8-5946b10d5073",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate FTCR for EMNLP 2026 ARR Submission (Round 7)",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116"
}
```

---

### Tool result

_source line 15 · 2026-05-10T07:08:45.202Z_

<details><summary>↩ Tool result · `toolu_01X2duVDp6xHes59Z7WH36xB`</summary>

```text
I now have comprehensive findings across all 8 areas. Here is the full adversarial research report:

---

## Adversarial Research Report: FTCR Paper Claims

### 1. DebugBench Taxonomy Verification

**Verdict: The claim of "4 major + 18 minor" is CONFIRMED, but the exact enumeration of all 18 minor types is partially verified.**

Sources: ACL Anthology (https://aclanthology.org/2024.findings-acl.247/), arXiv:2401.04621, Hugging Face dataset (Rtian/DebugBench).

The paper appears in ACL 2024 Findings (not main track - worth noting if the FTCR paper claims "ACL 2024" without the "Findings" qualifier). Total instances: 4,253. The four major categories are confirmed as: **Syntax, Reference, Logic, and Multiple** (not "Other Error" as one Hugging Face dataset viewer suggested - the original paper's fourth category is "Multiple").

From the Hugging Face dataset viewer and multiple search results, the 18 minor types and their distributions are reconstructed as follows. Note: the exact complete enumeration below is pieced together from multiple sources since the PDF taxonomy figure was not directly machine-readable:

**Syntax** (confirmed sub-types include): missing colons (129), unclosed parentheses (133), illegal separation (68), illegal indentation (45), unclosed string (125), illegal comment (124) — that is 6 Syntax sub-types.

**Reference** (confirmed): faulty indexing (206), undefined objects (187), undefined methods (167), illegal keywords (124) — that is 4 Reference sub-types.

**Logic** (confirmed): condition error (260), operation error (180), variable error (100), other error (50) — that is 4 Logic sub-types.

**Multiple** (confirmed): double bugs (750), triple bugs (750), quadruple bugs (718) — that is 3 Multiple sub-types... but the total above only sums to 17.

**Critical gap:** The complete list sums to only 17 confirmed named sub-types. The 18th type is not recoverable from publicly available non-PDF sources. The paper itself states 18 minor types. FTCR's citation of "4 major + 18 minor" is consistent with the abstract/description but the 18th minor type cannot be independently confirmed without reading the PDF directly.

**Taxonomy basis:** The paper explicitly states the taxonomy derives from **Barr (2004)**, not from a novel contribution.

---

### 2. InferFix Architecture Verification

**Verdict: The FTCR characterization of InferFix as using "soft contrastive similarity" is CONFIRMED. The claim that InferFix does NOT use hard categorical index partitioning is CONFIRMED. InferFix DOES require Infer at inference time — this is a critical architectural constraint.**

Sources: arXiv:2303.07263, ar5iv.labs.arxiv.org/html/2303.07263, FSE 2023 conference page, Microsoft Research blog.

Key findings from the ar5iv HTML version of the InferFix paper:

- InferFix uses a **single unified dense index**: "The retrieval database is a key-value store with encoded buggy code snippets ℰ(c) serving as keys, and string representations of the corresponding fixes f serving as values." Retrieval uses cosine similarity `sim(q,c) = ℰ(c)^T · ℰ(q)` across the entire database — this is **soft contrastive similarity**, NOT hard categorical partitioning.
- Bug type acts as a **post-hoc filter**, not an index partition: "retrieved fixes must be of the same bug type as the query, and impose a minimum similarity threshold between retrieved fixes and a query of 60%." This is different from FTCR's claimed approach of pre-partitioning the retrieval corpus by type.
- **Infer IS required at inference time**: The system is deployed "alongside Infer" in the CI pipeline. The static analyzer runs first to detect, classify, and localize bugs before the retrieval prompt is constructed. Without Infer, the bug type label needed for filtering would be unavailable.

**Adversarial challenge to FTCR**: If FTCR claims novelty over InferFix by using hard categorical partitioning, this is a legitimate differentiation. However, FTCR should explicitly address whether its type classifier is a learned LLM component vs. requiring a hard-to-deploy static analyzer like Infer — this is a material practical difference. The InferredBugs dataset (the retrieval corpus) is organized by language, NOT by bug type, confirming the unified-index architecture.

---

### 3. ReinFix Verification

**Verdict: ICSE 2026 venue CONFIRMED. Soft root-cause embedding CONFIRMED. text-embedding-3-large CONFIRMED.**

Sources: arXiv:2506.23100, arXiv HTML version (https://arxiv.org/html/2506.23100).

- **Venue**: Explicitly states "the 48th International Conference on Software Engineering; 12–18 April, 2026; Rio de Janeiro, Brazil" — ICSE 2026 is confirmed.
- **Embedding model**: "we use the text-embedding-3-large (OpenAI, 2024) as the embedding model" — confirmed exactly.
- **Mechanism**: Uses formula `e_i = f_embed(c_i ⊕ r_i)` — buggy code and root cause are **concatenated** into one string, then embedded as a unified vector. This is soft/continuous embedding, NOT hard categorical partitioning.
- **Retrieval**: Uses cosine similarity in a continuous shared embedding space.

**Distinction from FTCR**: ReinFix retrieves based on (buggy code + root cause text) similarity — a soft, semantic similarity match. If FTCR's claimed novelty is hard type-conditioned partitioning (separate index per failure category), this is genuinely different from ReinFix. However, if FTCR merely appends a type label to the query string before embedding (rather than genuinely partitioning), the distinction may be weaker than claimed.

---

### 4. Concurrent Work Search — CRITICAL FINDING

**Verdict: A highly relevant concurrent paper was found that FTCR may need to address as a threat to novelty: ReCode (CIKM 2025, arXiv:2509.02330).**

Sources: arXiv:2509.02330 (HTML), ACL proceedings, CIKM 2025 proceedings.

**ReCode** ("Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation," accepted CIKM 2025, posted arXiv September 2, 2025) uses a mechanism that is functionally very similar to FTCR's claimed core contribution:

- It uses an **algorithm-aware retrieval strategy** with LLM-predicted type labels guiding retrieval.
- It maintains **separate algorithm-specific sub-knowledge bases**: "Using the original algorithmic tags (e.g., greedy, binary search, graph, and dp), we organize the knowledge base into a multi-level hierarchy."
- Retrieval explicitly operates within type-specific partitions: "Based on these predictions, the hybrid retrieval module selectively searches corresponding algorithm-specific sub-knowledge bases to retrieve the most relevant repair exemplars."
- This is genuine **hard categorical partitioning by predicted type**, operationally equivalent to what FTCR describes as its novel contribution.

The key difference is scope/domain: ReCode operates on competitive programming bugs (Codeforces) with algorithm-type labels (greedy, dp, graph, binary search), while FTCR presumably operates on repository-level software bugs with failure-type labels (from a taxonomy like DebugBench's). However, the **core mechanism — predict type, then retrieve within type-partitioned sub-corpus — is the same**. FTCR must explicitly distinguish itself from ReCode or risk rejection on novelty grounds.

No other papers were found using this exact mechanism for repository-level repair specifically, suggesting FTCR's repositioning of this idea to the SWE-bench/repository repair domain may represent incremental but real contribution.

---

### 5. SWE-Exp Verification

**Verdict: SWE-Exp uses soft similarity-based retrieval, NOT hard categorical type conditioning. CONFIRMED.**

Sources: arXiv:2507.23361, HTML version v2.

- **arXiv ID 2507.23361 exists** and matches the description. Posted July 31, 2025.
- **Retrieval mechanism**: Soft similarity. Uses "cosine similarity between the new issue type and attributes with keys in the vector database" with the **Multilingual-E5-Large** embedding model.
- **Bug type role**: Issue Type is one of several metadata fields used as retrieval keys, but retrieval is fundamentally embedding-based cosine similarity — not hard partition-then-search.
- **Experience bank structure**: Two facets — Comprehension Experiences and Modification Experiences. Retrieves top N=10 by similarity, then LLM-reranks to K=1.

**Adversarial note**: SWE-Exp does use "Issue Type" as a retrieval attribute, which is a form of type-aware conditioning. However, it does not pre-partition its corpus by type and restrict retrieval to within-type results. FTCR should be careful not to over-state the difference from SWE-Exp if FTCR's mechanism is similarly hybrid (type-informed but not hard-partitioned).

---

### 6. TypeRepair Stage 3 Context Selection Verification

**Verdict: TypeRepair CONFIRMED to exist at the cited venue. Stage 3 context selection details PARTIALLY verified — cross-project vs. within-project question UNRESOLVED.**

Sources: Springer Nature Link (https://link.springer.com/article/10.1007/s11219-026-09751-w), multiple search confirmations.

- **Paper confirmed**: Zhang, R., Zhang, S., and Xie, L., Software Quality Journal, 2026, Volume 34, Article 14. DOI: 10.1007/s11219-026-09751-w.
- **Four stages confirmed**: defect localization → defect type identification → context selection → patch generation.
- **10 defect types confirmed** (paper defines 10 common defect types, not 18 like DebugBench).
- **Stage 3 specifics**: The Springer paywall blocked direct access (HTTP 303 redirect to paywall). Search results confirm context selection is Stage 3, but do not specify whether it retrieves from within-project code only or external cross-repository sources.

**Unresolved adversarial issue**: FTCR's differentiation from TypeRepair may hinge on whether TypeRepair's Stage 3 uses within-project-only context (common in APR — using the project's own code as repair ingredients) vs. external cross-repository retrieval (what FTCR presumably does). Without full-text access to TypeRepair, this claim cannot be independently verified. **This is a potential vulnerability in FTCR's related work discussion.** The reviewers should push back unless FTCR can cite specific evidence that TypeRepair uses only within-project context.

---

### 7. Broader Concurrent Work Search

**Verdict: ReCode (see #4 above) is the most directly challenging concurrent work. Additional relevant papers found:**

- **ReCode** (CIKM 2025, arXiv:2509.02330): Hard categorical partitioned retrieval by algorithm type. Most similar to FTCR's mechanism. MUST be discussed.
- **ReinFix** (ICSE 2026, arXiv:2506.23100): Soft embedding, but uses root-cause as retrieval signal. Already noted.
- **TypeRepair** (Software Quality Journal 2026): Type-conditioned APR but unclear on retrieval scope.
- **SWE-Exp** (arXiv:2507.23361): Soft type-informed retrieval, experience bank.
- **SelRepair / arXiv:2507.10103**: Dual RAG module for code repair (not type-partitioned).
- **PatchRecall** (arXiv:2604.10481, April 2026): Hybrid retrieval for APR — not type-conditioned.

No paper was found that combines exactly (a) DebugBench-style failure type taxonomy + (b) hard categorical partitioning + (c) repository-level SWE-bench-type repair. This gives FTCR a narrow but potentially defensible novelty window over the existing field. However, the combination of ReCode's mechanism + InferFix's type-annotation prompting + ReinFix's root-cause embedding covers substantial ground.

Searches for "FTCR" and "Failure-Type-Conditioned Retrieval" returned no results, suggesting FTCR has not been publicly posted or indexed yet (as expected for a submission under review).

---

### 8. EMNLP 2026 ARR Deadline Verification

**Verdict: CONFIRMED. The ARR submission deadline for EMNLP 2026 is May 25, 2026.**

Source: Official EMNLP 2026 website (https://2026.emnlp.org/calls/main_conference_papers/), confirmed via the official @emnlpmeeting Twitter/X post.

Full timeline confirmed:
- ARR submission deadline: **May 25, 2026**
- Reviewer registration: May 27, 2026
- Author response: July 7–13, 2026
- Meta-reviews released: July 30, 2026
- Commitment deadline: August 2, 2026
- Acceptance notification: August 20, 2026
- Main Conference: October 24–29, 2026 (venue: Hungary)

**Important policy note confirmed**: Since EMNLP 2026 and AACL share the ARR May cycle, authors must explicitly select a target conference at submission time and this choice is binding.

---

## Summary of Key Adversarial Findings

| Claim | Status | Notes |
|---|---|---|
| DebugBench: 4 major + 18 minor | CONFIRMED | Fourth category is "Multiple," not "Other." 18th minor type unverifiable from non-PDF sources. |
| DebugBench: ACL 2024 | PARTIALLY — it is ACL 2024 Findings, not main track | Minor distinction but worth checking if FTCR says "ACL 2024" |
| InferFix: soft contrastive similarity | CONFIRMED | Single unified index, cosine similarity filter by type post-hoc |
| InferFix requires Infer at inference | CONFIRMED — yes it does | Key constraint not always noted |
| ReinFix: ICSE 2026 | CONFIRMED | 48th ICSE, April 2026, Rio de Janeiro |
| ReinFix: soft embedding, text-embedding-3-large | CONFIRMED | Concatenated code+root_cause → single vector |
| ReCode (CIKM 2025): UNLISTED THREAT | CRITICAL | Uses hard categorical sub-knowledge-base partitioning by predicted algorithm type — functionally equivalent mechanism to FTCR, must be discussed |
| SWE-Exp: soft retrieval | CONFIRMED | Type-influenced but not hard-partitioned |
| TypeRepair Stage 3 (within vs. cross-project) | UNRESOLVED | Paywall blocked; FTCR's differentiation here is unverifiable |
| EMNLP 2026 ARR deadline: May 25, 2026 | CONFIRMED | Exact date confirmed from official CFP |

**Most important adversarial finding**: **ReCode (CIKM 2025, arXiv:2509.02330)** implements hard categorical type-partitioned retrieval for code repair using LLM-predicted type labels, accepted September 2025. If FTCR does not cite and clearly differentiate from ReCode, this represents a significant novelty threat that could lead to rejection.

Sources:
- [DebugBench: ACL Anthology](https://aclanthology.org/2024.findings-acl.247/)
- [DebugBench: arXiv 2401.04621](https://arxiv.org/abs/2401.04621)
- [DebugBench GitHub](https://github.com/thunlp/DebugBench)
- [InferFix: arXiv 2303.07263](https://arxiv.org/abs/2303.07263)
- [InferFix: FSE 2023](https://2023.esec-fse.org/details/fse-2023-industry/33/InferFix-End-to-End-Program-Repair-with-LLMs)
- [InferFix: Microsoft Research](https://www.microsoft.com/en-us/research/publication/inferfix-end-to-end-program-repair-with-llms-over-retrieval-augmented-prompts/)
- [ReinFix: arXiv 2506.23100](https://arxiv.org/abs/2506.23100)
- [ReinFix HTML](https://arxiv.org/html/2506.23100)
- [ReCode: arXiv 2509.02330](https://arxiv.org/abs/2509.02330)
- [ReCode HTML](https://arxiv.org/html/2509.02330v1)
- [ReCode: CIKM 2025 ACM DL](https://dl.acm.org/doi/10.1145/3746252.3761035)
- [SWE-Exp: arXiv 2507.23361](https://arxiv.org/abs/2507.23361)
- [SWE-Exp HTML v2](https://arxiv.org/html/2507.23361v2)
- [TypeRepair: Software Quality Journal 2026](https://link.springer.com/article/10.1007/s11219-026-09751-w)
- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 Twitter confirmation](https://x.com/emnlpmeeting/status/2029508292637061462)
- [PatchRecall: arXiv 2604.10481](https://arxiv.org/abs/2604.10481)
- [LLM APR Survey: arXiv 2506.23749](https://arxiv.org/abs/2506.23749)

agentId: a3e9d569d6be90fcf (use SendMessage with to: 'a3e9d569d6be90fcf' to continue this agent)
&lt;usage>total_tokens: 57930
tool_uses: 66
duration_ms: 451620&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7aa2f3a8-d269-4caf-9e14-732396d11bcf",
  "isSidechain": false,
  "promptId": "700da751-e77a-463d-863b-f81ff1e1c257",
  "type": "user",
  "uuid": "a5ee9b1a-d877-41f4-8741-aed1965ce444",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping conduct an adversarial review of a paper proposal called \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\" (FTCR). Your job is to conduct independent research to verify or challenge the paper's claims. Do NOT accept anything at face value — you must independently verify.\n\nPlease conduct the following specific searches and report your findings in detail:\n\n1. Search for DebugBench paper to verify its exact taxonomy structure: \"DebugBench ACL 2024\" and \"DebugBench evaluating debugging LLM 4253\". Report the exact structure (is it 4 major + 18 minor? What are the sub-types exactly?)\n\n2. Search for InferFix paper to verify its architecture: \"InferFix program repair LLM FSE 2023\" and \"InferFix arXiv 2303.07263\". Specifically: does InferFix use hard categorical index partitioning or soft contrastive similarity? Does it require Infer static analyzer at inference time?\n\n3. Search for ReinFix paper: \"ReinFix repair ingredients ICSE 2026\" and \"ReinFix arXiv 2506.23100\". Verify it's ICSE 2026 (not 2025), and verify its mechanism (soft root-cause embedding, text-embedding-3-large).\n\n4. Search for concurrent work: \"type-conditioned retrieval program repair 2025 2026\", \"categorical type partition retrieval code repair\", \"bug type classification retrieval augmented repair 2025\". Look for any papers that do hard categorical partitioning for code repair retrieval that may have been missed.\n\n5. Search for SWE-Exp: \"SWE-Exp experience bank software issue resolution arXiv 2507.23361\". Verify whether it uses hard or soft type conditioning.\n\n6. Search for TypeRepair: \"TypeRepair defect-type-aware program repair Zhang 2026 Software Quality Journal\". Try to verify whether its Stage 3 context selection uses within-project code only or external cross-repository retrieval.\n\n7. Search for recent concurrent work that might challenge novelty: \"retrieval augmented program repair taxonomy 2026\", \"LLM bug type classification retrieval 2025 2026\", \"partition-based retrieval code repair arxiv 2026\".\n\n8. Check EMNLP 2026 ARR deadline: search \"EMNLP 2026 ARR deadline May 2026\" to verify the submission deadline is indeed May 25, 2026.\n\nFor each search, report: what you found, the URL, and whether it confirms or challenges the paper's claims. Be specific and quote relevant passages where possible. Use WebSearch and WebFetch tools to read actual papers.",
    "agentId": "a3e9d569d6be90fcf",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive findings across all 8 areas. Here is the full adversarial research report:\n\n---\n\n## Adversarial Research Report: FTCR Paper Claims\n\n### 1. DebugBench Taxonomy Verification\n\n**Verdict: The claim of \"4 major + 18 minor\" is CONFIRMED, but the exact enumeration of all 18 minor types is partially verified.**\n\nSources: ACL Anthology (https://aclanthology.org/2024.findings-acl.247/), arXiv:2401.04621, Hugging Face dataset (Rtian/DebugBench).\n\nThe paper appears in ACL 2024 Findings (not main track - worth noting if the FTCR paper claims \"ACL 2024\" without the \"Findings\" qualifier). Total instances: 4,253. The four major categories are confirmed as: **Syntax, Reference, Logic, and Multiple** (not \"Other Error\" as one Hugging Face dataset viewer suggested - the original paper's fourth category is \"Multiple\").\n\nFrom the Hugging Face dataset viewer and multiple search results, the 18 minor types and their distributions are reconstructed as follows. Note: the exact complete enumeration below is pieced together from multiple sources since the PDF taxonomy figure was not directly machine-readable:\n\n**Syntax** (confirmed sub-types include): missing colons (129), unclosed parentheses (133), illegal separation (68), illegal indentation (45), unclosed string (125), illegal comment (124) — that is 6 Syntax sub-types.\n\n**Reference** (confirmed): faulty indexing (206), undefined objects (187), undefined methods (167), illegal keywords (124) — that is 4 Reference sub-types.\n\n**Logic** (confirmed): condition error (260), operation error (180), variable error (100), other error (50) — that is 4 Logic sub-types.\n\n**Multiple** (confirmed): double bugs (750), triple bugs (750), quadruple bugs (718) — that is 3 Multiple sub-types... but the total above only sums to 17.\n\n**Critical gap:** The complete list sums to only 17 confirmed named sub-types. The 18th type is not recoverable from publicly available non-PDF sources. The paper itself states 18 minor types. FTCR's citation of \"4 major + 18 minor\" is consistent with the abstract/description but the 18th minor type cannot be independently confirmed without reading the PDF directly.\n\n**Taxonomy basis:** The paper explicitly states the taxonomy derives from **Barr (2004)**, not from a novel contribution.\n\n---\n\n### 2. InferFix Architecture Verification\n\n**Verdict: The FTCR characterization of InferFix as using \"soft contrastive similarity\" is CONFIRMED. The claim that InferFix does NOT use hard categorical index partitioning is CONFIRMED. InferFix DOES require Infer at inference time — this is a critical architectural constraint.**\n\nSources: arXiv:2303.07263, ar5iv.labs.arxiv.org/html/2303.07263, FSE 2023 conference page, Microsoft Research blog.\n\nKey findings from the ar5iv HTML version of the InferFix paper:\n\n- InferFix uses a **single unified dense index**: \"The retrieval database is a key-value store with encoded buggy code snippets ℰ(c) serving as keys, and string representations of the corresponding fixes f serving as values.\" Retrieval uses cosine similarity `sim(q,c) = ℰ(c)^T · ℰ(q)` across the entire database — this is **soft contrastive similarity**, NOT hard categorical partitioning.\n- Bug type acts as a **post-hoc filter**, not an index partition: \"retrieved fixes must be of the same bug type as the query, and impose a minimum similarity threshold between retrieved fixes and a query of 60%.\" This is different from FTCR's claimed approach of pre-partitioning the retrieval corpus by type.\n- **Infer IS required at inference time**: The system is deployed \"alongside Infer\" in the CI pipeline. The static analyzer runs first to detect, classify, and localize bugs before the retrieval prompt is constructed. Without Infer, the bug type label needed for filtering would be unavailable.\n\n**Adversarial challenge to FTCR**: If FTCR claims novelty over InferFix by using hard categorical partitioning, this is a legitimate differentiation. However, FTCR should explicitly address whether its type classifier is a learned LLM component vs. requiring a hard-to-deploy static analyzer like Infer — this is a material practical difference. The InferredBugs dataset (the retrieval corpus) is organized by language, NOT by bug type, confirming the unified-index architecture.\n\n---\n\n### 3. ReinFix Verification\n\n**Verdict: ICSE 2026 venue CONFIRMED. Soft root-cause embedding CONFIRMED. text-embedding-3-large CONFIRMED.**\n\nSources: arXiv:2506.23100, arXiv HTML version (https://arxiv.org/html/2506.23100).\n\n- **Venue**: Explicitly states \"the 48th International Conference on Software Engineering; 12–18 April, 2026; Rio de Janeiro, Brazil\" — ICSE 2026 is confirmed.\n- **Embedding model**: \"we use the text-embedding-3-large (OpenAI, 2024) as the embedding model\" — confirmed exactly.\n- **Mechanism**: Uses formula `e_i = f_embed(c_i ⊕ r_i)` — buggy code and root cause are **concatenated** into one string, then embedded as a unified vector. This is soft/continuous embedding, NOT hard categorical partitioning.\n- **Retrieval**: Uses cosine similarity in a continuous shared embedding space.\n\n**Distinction from FTCR**: ReinFix retrieves based on (buggy code + root cause text) similarity — a soft, semantic similarity match. If FTCR's claimed novelty is hard type-conditioned partitioning (separate index per failure category), this is genuinely different from ReinFix. However, if FTCR merely appends a type label to the query string before embedding (rather than genuinely partitioning), the distinction may be weaker than claimed.\n\n---\n\n### 4. Concurrent Work Search — CRITICAL FINDING\n\n**Verdict: A highly relevant concurrent paper was found that FTCR may need to address as a threat to novelty: ReCode (CIKM 2025, arXiv:2509.02330).**\n\nSources: arXiv:2509.02330 (HTML), ACL proceedings, CIKM 2025 proceedings.\n\n**ReCode** (\"Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation,\" accepted CIKM 2025, posted arXiv September 2, 2025) uses a mechanism that is functionally very similar to FTCR's claimed core contribution:\n\n- It uses an **algorithm-aware retrieval strategy** with LLM-predicted type labels guiding retrieval.\n- It maintains **separate algorithm-specific sub-knowledge bases**: \"Using the original algorithmic tags (e.g., greedy, binary search, graph, and dp), we organize the knowledge base into a multi-level hierarchy.\"\n- Retrieval explicitly operates within type-specific partitions: \"Based on these predictions, the hybrid retrieval module selectively searches corresponding algorithm-specific sub-knowledge bases to retrieve the most relevant repair exemplars.\"\n- This is genuine **hard categorical partitioning by predicted type**, operationally equivalent to what FTCR describes as its novel contribution.\n\nThe key difference is scope/domain: ReCode operates on competitive programming bugs (Codeforces) with algorithm-type labels (greedy, dp, graph, binary search), while FTCR presumably operates on repository-level software bugs with failure-type labels (from a taxonomy like DebugBench's). However, the **core mechanism — predict type, then retrieve within type-partitioned sub-corpus — is the same**. FTCR must explicitly distinguish itself from ReCode or risk rejection on novelty grounds.\n\nNo other papers were found using this exact mechanism for repository-level repair specifically, suggesting FTCR's repositioning of this idea to the SWE-bench/repository repair domain may represent incremental but real contribution.\n\n---\n\n### 5. SWE-Exp Verification\n\n**Verdict: SWE-Exp uses soft similarity-based retrieval, NOT hard categorical type conditioning. CONFIRMED.**\n\nSources: arXiv:2507.23361, HTML version v2.\n\n- **arXiv ID 2507.23361 exists** and matches the description. Posted July 31, 2025.\n- **Retrieval mechanism**: Soft similarity. Uses \"cosine similarity between the new issue type and attributes with keys in the vector database\" with the **Multilingual-E5-Large** embedding model.\n- **Bug type role**: Issue Type is one of several metadata fields used as retrieval keys, but retrieval is fundamentally embedding-based cosine similarity — not hard partition-then-search.\n- **Experience bank structure**: Two facets — Comprehension Experiences and Modification Experiences. Retrieves top N=10 by similarity, then LLM-reranks to K=1.\n\n**Adversarial note**: SWE-Exp does use \"Issue Type\" as a retrieval attribute, which is a form of type-aware conditioning. However, it does not pre-partition its corpus by type and restrict retrieval to within-type results. FTCR should be careful not to over-state the difference from SWE-Exp if FTCR's mechanism is similarly hybrid (type-informed but not hard-partitioned).\n\n---\n\n### 6. TypeRepair Stage 3 Context Selection Verification\n\n**Verdict: TypeRepair CONFIRMED to exist at the cited venue. Stage 3 context selection details PARTIALLY verified — cross-project vs. within-project question UNRESOLVED.**\n\nSources: Springer Nature Link (https://link.springer.com/article/10.1007/s11219-026-09751-w), multiple search confirmations.\n\n- **Paper confirmed**: Zhang, R., Zhang, S., and Xie, L., Software Quality Journal, 2026, Volume 34, Article 14. DOI: 10.1007/s11219-026-09751-w.\n- **Four stages confirmed**: defect localization → defect type identification → context selection → patch generation.\n- **10 defect types confirmed** (paper defines 10 common defect types, not 18 like DebugBench).\n- **Stage 3 specifics**: The Springer paywall blocked direct access (HTTP 303 redirect to paywall). Search results confirm context selection is Stage 3, but do not specify whether it retrieves from within-project code only or external cross-repository sources.\n\n**Unresolved adversarial issue**: FTCR's differentiation from TypeRepair may hinge on whether TypeRepair's Stage 3 uses within-project-only context (common in APR — using the project's own code as repair ingredients) vs. external cross-repository retrieval (what FTCR presumably does). Without full-text access to TypeRepair, this claim cannot be independently verified. **This is a potential vulnerability in FTCR's related work discussion.** The reviewers should push back unless FTCR can cite specific evidence that TypeRepair uses only within-project context.\n\n---\n\n### 7. Broader Concurrent Work Search\n\n**Verdict: ReCode (see #4 above) is the most directly challenging concurrent work. Additional relevant papers found:**\n\n- **ReCode** (CIKM 2025, arXiv:2509.02330): Hard categorical partitioned retrieval by algorithm type. Most similar to FTCR's mechanism. MUST be discussed.\n- **ReinFix** (ICSE 2026, arXiv:2506.23100): Soft embedding, but uses root-cause as retrieval signal. Already noted.\n- **TypeRepair** (Software Quality Journal 2026): Type-conditioned APR but unclear on retrieval scope.\n- **SWE-Exp** (arXiv:2507.23361): Soft type-informed retrieval, experience bank.\n- **SelRepair / arXiv:2507.10103**: Dual RAG module for code repair (not type-partitioned).\n- **PatchRecall** (arXiv:2604.10481, April 2026): Hybrid retrieval for APR — not type-conditioned.\n\nNo paper was found that combines exactly (a) DebugBench-style failure type taxonomy + (b) hard categorical partitioning + (c) repository-level SWE-bench-type repair. This gives FTCR a narrow but potentially defensible novelty window over the existing field. However, the combination of ReCode's mechanism + InferFix's type-annotation prompting + ReinFix's root-cause embedding covers substantial ground.\n\nSearches for \"FTCR\" and \"Failure-Type-Conditioned Retrieval\" returned no results, suggesting FTCR has not been publicly posted or indexed yet (as expected for a submission under review).\n\n---\n\n### 8. EMNLP 2026 ARR Deadline Verification\n\n**Verdict: CONFIRMED. The ARR submission deadline for EMNLP 2026 is May 25, 2026.**\n\nSource: Official EMNLP 2026 website (https://2026.emnlp.org/calls/main_conference_papers/), confirmed via the official @emnlpmeeting Twitter/X post.\n\nFull timeline confirmed:\n- ARR submission deadline: **May 25, 2026**\n- Reviewer registration: May 27, 2026\n- Author response: July 7–13, 2026\n- Meta-reviews released: July 30, 2026\n- Commitment deadline: August 2, 2026\n- Acceptance notification: August 20, 2026\n- Main Conference: October 24–29, 2026 (venue: Hungary)\n\n**Important policy note confirmed**: Since EMNLP 2026 and AACL share the ARR May cycle, authors must explicitly select a target conference at submission time and this choice is binding.\n\n---\n\n## Summary of Key Adversarial Findings\n\n| Claim | Status | Notes |\n|---|---|---|\n| DebugBench: 4 major + 18 minor | CONFIRMED | Fourth category is \"Multiple,\" not \"Other.\" 18th minor type unverifiable from non-PDF sources. |\n| DebugBench: ACL 2024 | PARTIALLY — it is ACL 2024 Findings, not main track | Minor distinction but worth checking if FTCR says \"ACL 2024\" |\n| InferFix: soft contrastive similarity | CONFIRMED | Single unified index, cosine similarity filter by type post-hoc |\n| InferFix requires Infer at inference | CONFIRMED — yes it does | Key constraint not always noted |\n| ReinFix: ICSE 2026 | CONFIRMED | 48th ICSE, April 2026, Rio de Janeiro |\n| ReinFix: soft embedding, text-embedding-3-large | CONFIRMED | Concatenated code+root_cause → single vector |\n| ReCode (CIKM 2025): UNLISTED THREAT | CRITICAL | Uses hard categorical sub-knowledge-base partitioning by predicted algorithm type — functionally equivalent mechanism to FTCR, must be discussed |\n| SWE-Exp: soft retrieval | CONFIRMED | Type-influenced but not hard-partitioned |\n| TypeRepair Stage 3 (within vs. cross-project) | UNRESOLVED | Paywall blocked; FTCR's differentiation here is unverifiable |\n| EMNLP 2026 ARR deadline: May 25, 2026 | CONFIRMED | Exact date confirmed from official CFP |\n\n**Most important adversarial finding**: **ReCode (CIKM 2025, arXiv:2509.02330)** implements hard categorical type-partitioned retrieval for code repair using LLM-predicted type labels, accepted September 2025. If FTCR does not cite and clearly differentiate from ReCode, this represents a significant novelty threat that could lead to rejection.\n\nSources:\n- [DebugBench: ACL Anthology](https://aclanthology.org/2024.findings-acl.247/)\n- [DebugBench: arXiv 2401.04621](https://arxiv.org/abs/2401.04621)\n- [DebugBench GitHub](https://github.com/thunlp/DebugBench)\n- [InferFix: arXiv 2303.07263](https://arxiv.org/abs/2303.07263)\n- [InferFix: FSE 2023](https://2023.esec-fse.org/details/fse-2023-industry/33/InferFix-End-to-End-Program-Repair-with-LLMs)\n- [InferFix: Microsoft Research](https://www.microsoft.com/en-us/research/publication/inferfix-end-to-end-program-repair-with-llms-over-retrieval-augmented-prompts/)\n- [ReinFix: arXiv 2506.23100](https://arxiv.org/abs/2506.23100)\n- [ReinFix HTML](https://arxiv.org/html/2506.23100)\n- [ReCode: arXiv 2509.02330](https://arxiv.org/abs/2509.02330)\n- [ReCode HTML](https://arxiv.org/html/2509.02330v1)\n- [ReCode: CIKM 2025 ACM DL](https://dl.acm.org/doi/10.1145/3746252.3761035)\n- [SWE-Exp: arXiv 2507.23361](https://arxiv.org/abs/2507.23361)\n- [SWE-Exp HTML v2](https://arxiv.org/html/2507.23361v2)\n- [TypeRepair: Software Quality Journal 2026](https://link.springer.com/article/10.1007/s11219-026-09751-w)\n- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)\n- [EMNLP 2026 Twitter confirmation](https://x.com/emnlpmeeting/status/2029508292637061462)\n- [PatchRecall: arXiv 2604.10481](https://arxiv.org/abs/2604.10481)\n- [LLM APR Survey: arXiv 2506.23749](https://arxiv.org/abs/2506.23749)"
      }
    ],
    "totalDurationMs": 451620,
    "totalTokens": 57930,
    "totalToolUseCount": 66,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 470,
      "cache_read_input_tokens": 52962,
      "output_tokens": 4497,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 470
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4497,
          "cache_read_input_tokens": 52962,
          "cache_creation_input_tokens": 470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 470,
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
      "otherToolCount": 66
    }
  },
  "sourceToolAssistantUUID": "7aa2f3a8-d269-4caf-9e14-732396d11bcf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116",
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
  "leafUuid": "a5ee9b1a-d877-41f4-8741-aed1965ce444",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate FTCR for EMNLP 2026 ARR Submission (Round 7)",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116"
}
```

---

### Assistant

_source line 18 · 2026-05-10T07:10:53.586Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research findings. Let me analyze the key findings from both agent searches and assess the FTCR proposal:

## Key findings from research:

### CONFIRMED CLAIMS:
1. **DebugBench**: 4 major + 18 minor taxonomy CONFIRMED (ACL 2024 Findings, not main track)
2. **InferFix**: Uses soft contrastive similarity with post-hoc type filtering (not hard partition), requires Infer at inference time — CONFIRMED
3. **ReinFix**: ICSE 2026 CONFIRMED, soft embedding with text-embedding-3-large CONFIRMED


4. **SWE-Exp**: Soft type-influenced retrieval CONFIRMED
5. **EMNLP 2026 ARR deadline**: May 25, 2026 CONFIRMED
6. **TypeRepair**: Exists at SQJ 2026, but the claim about Stage 3 within-project versus cross-repo comparisons is behind a paywall and can't be verified

### CRITICAL ISSUES FOUND:

#### 1. ReCode is already cited (CRITICAL BUT RESOLVED)
Looking back at the proposal, ReCode is actually already cited there: "ReCode (CIKM 2025, arXiv 2509.02

330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph)." It appears in both the main text and the landscape section.

So the real question becomes whether the differentiation from ReCode is sufficiently strong. Both approaches use hard categorical partitioning based on LLM-predicted types, but they differ in domain (algorithmic tags versus natural bug types), taxonomy structure (algorithmic categories versus DebugBench's 4-major/18-minor taxonomy), and corpus (competitive programming versus real repository bugs). The distinction feels primarily domain-based rather than mechanistically novel, though the proposal does acknowledge ReCode as prior work and explains the domain-specific motivation.

Looking more closely at what the proposal actually claims as its contribution: it's testing whether hard categorical type partitioning across the 18 minor semantic bug subtypes yields better precision than ReinFix's joint embedding approach. So the core question is whether applying the same mechanism to a different domain with a different taxonomy and corpus constitutes a meaningful contribution, or if it's just ReCode applied elsewhere.

The proposal does frame this as an empirical investigation — measuring whether X% improvement is achievable through hard partitioning. But there's a real concern lurking here: the LLM annotation study shows only 5.2-35.7% accuracy on automated bug type labeling, which could severely limit FTCR's ability to even construct those 18 fine-grained categories reliably. The proposal acknowledges this by treating X% as an unknown to be measured, but the low annotation accuracy might make the whole hard partitioning strategy infeasible in practice.

That said, DebugBench's taxonomy is purpose-built for LLM classification with clearer category definitions than the study's taxonomy, so performance could be better. Still, this is exactly the kind of prior work reviewers will cite as a red flag.

The InferFix architecture distinction holds up—it does post-hoc type filtering after retrieval, whereas FTCR partitions upfront. That's a genuine differentiation. And DebugBench is correctly cited as ACL 2024 Findings.

Now checking LTFix and its approach...

it uses typestate-guided retrieval for memory error repair in C code, which is domain-specific and not cited in FTCR—could be a gap, though the focus on memory errors in C might make it less directly applicable here.

Looking at what Round 6 required and what Round 7 addressed: the EMNLP Main versus Findings ambiguity is resolved by committing to EMNLP Findings, the DebugBench hierarchical structure is now correctly stated as a 4-major/18-minor taxonomy, and the Day-0 execution assumption is clarified with the A100 node provisioning detail.

Now I need to check what issues remain. The ReCode differentiation is present in the proposal—it's cited and the distinction between algorithm-type bugs in competitive programming versus bug-type in natural repository bugs is articulated. But mechanistically, the differentiation feels thin; the core contribution boils down to applying the same mechanism to a more practical domain, adding an empirical comparison between hard and soft partitioning strategies, and providing more comprehensive evaluation.

The bigger concern is the LLM annotation accuracy problem. There's a paper showing that LLM auto-labeling of fine-grained bug types only achieves 5.2-35.7% accuracy, which directly undermines the proposal's approach. If reviewers are familiar with this work, they'll immediately question whether the reported performance metrics are reliable enough to justify the hard partitioning strategy.

I'm also stuck on verifying the TypeRepair claim about within-project context—it requires paid access—but the proposal does attempt to build an evidentiary case by noting that TypeRepair evaluates exclusively on certain constraints.

The InferFix architecture details check out now: it uses a unified index with post-hoc type filtering, while FTCR proposes pre-partitioning at index time, which is a meaningful distinction. And there's an uncited LTFix paper on type-guided retrieval for code repair that I need to account for.

Looking at the missing citations more broadly, the annotation accuracy study seems more critical than the memory-error-specific LTFix work, since it directly questions whether LLM annotations are reliable. The other related works like ExpeRepair and SelRepair are less essential gaps.

Now I'm trying to pin down what the core scientific contribution actually is: measuring LLM classifier accuracy against DebugBench at the 18-minor-type level, zero-shot Java transfer performance, repair improvements when instances are correctly classified under hard partitioning, and then the degradation when misclassified.

The feasibility looks reasonable—the compute infrastructure is apparently ready, the corpus of 3,050 bug-fix pairs is manageable, and the annotation budget of around $183 for three passes is realistic, though the 10-14 day timeline is ambitious. For EMNLP Findings, this calibration study measuring when categorical type conditioning helps or hurts repair performance fits well, and the May 25, 2026 deadline gives some runway.

Now I'm thinking through what gaps remain after six rounds of feedback. The biggest issue is that the proposal needs to directly address the counterevidence showing LLM annotation accuracy struggles in general settings—specifically arXiv 2407.06153—and explain why their approach with DebugBench's clear taxonomy and few-shot prompting might sidestep those problems. There are also two smaller citation gaps: LTFix on type-guided retrieval for code repair, and a clarification needed on InferFix's filtering mechanism, since the current description conflates retrieval-time filtering with post-hoc filtering.

The more interesting challenge is articulating why FTCR's architectural choice actually matters compared to InferFix. The key insight is that partitioning indices at construction time versus filtering at query time creates a meaningful difference in recall—InferFix retrieves broadly then narrows down, potentially missing same-type patches with lower similarity scores, while FTCR only searches within the relevant type partition and returns the top-k regardless of absolute similarity. That's a legitimate structural distinction worth defending.

Now I'm trying to pin down what InferFix's "76.8% top-1 accuracy" actually measures. The paper claims this metric, but I need to be precise about whether it's top-1 retrieval accuracy (the probability the highest-ranked patch is correct) or something else entirely. This distinction matters because comparing retrieval metrics to repair success rates would be mixing different measurement types.

DebugBench is properly cited as ACL Findings 2024, which is correct. Looking at the proposal overall after multiple rounds of revision, it has a clear research question, a legitimate novelty angle around hard versus soft type partitioning for repository bugs, and most previous concerns have been addressed. The main unresolved issues are the LLM annotation accuracy counterevidence from arXiv 2407.06153 that hasn't been tackled, a couple of uncited papers that aren't critical, and the possibility that the core finding could be negative—which would actually still be scientifically valid.

Evaluating the proposal's viability: the novelty is solid for a Findings paper at 3.5/5, extending ReCode's mechanism to natural bugs with the DebugBench taxonomy and the empirical comparison. Feasibility sits at 3.5/5 given the extremely tight 15-day timeline and risky 2-day writing window, though auto-research mode and confirmed compute resources make it workable. The proposal is now well-structured and clear with the X%/Y%/Z%/W% framing, earning a 4/5 on clarity. Impact is moderate at 3/5—the findings would benefit the APR and RAG communities but the scope is fairly narrow.

Averaging 3.5/5 puts this below the 4.0 threshold, so the verdict is to revise. The critical issue is that prior work shows LLM auto-labeling of bug types achieves only 5.2% accuracy at fine-grained levels and 35.7% at secondary levels. The proposal should directly acknowledge this counterevidence and position the empirical X% finding as the paper's core contribution—either validating or challenging those low-accuracy results specifically for the DebugBench taxonomy.

I should also note that TFix uses type-guided retrieval for code repair and deserves a mention in related work. The distinction between InferFix's post-hoc filtering versus FTCR's pre-construction partitioning is clearer now, but I need to flag that this architectural choice affects retrieval recall—InferFix's unified index can retrieve any patch before filtering, while FTCR's pre-partitioned approach only retrieves from its matched sub-corpus.

Let me double-check the Round 7 proposal on InferFix's performance numbers—it claims 76.8% top-1 accuracy on Java and 65.6% on C#, outperforming LLM baselines by 11–55%, but I need to verify whether these results are actually in the landscape or if there's a citation issue here.

Looking more closely at what "top-1 accuracy" means in the InferFix paper: it's measuring whether the highest-ranked retrieved patch matches the ground-truth fix, which is fundamentally a retrieval metric rather than a repair success rate. This is different from FTCR's Z%/W% metrics that measure actual repair outcomes, so the comparison between them requires careful framing since they're evaluating different things. That said, FTCR isn't necessarily trying to match InferFix's retrieval accuracy—it's focused on repair success rates under different retrieval strategies, which is a distinct goal.

I should verify the remaining critical gaps: the proposal correctly identifies EMNLP Findings as the venue, includes the 4-major/18-minor taxonomy, addresses compute readiness, describes InferFix's architecture with type structures and post-hoc filtering, and specifies the statistical tests. The main missing citations are the LLM annotation accuracy paper (5.2-35.7% range) and a couple of recent repair papers, though those are less central. The interesting part is that FTCR's framing is actually quite solid—X% is empirically measured rather than assumed, so even if it turns out to be 35%, the paper still reports valid empirical results.

But reviewers will definitely push back by citing that prior work and asking what happens when X% is that low. The proposal should preemptively address this concern rather than leaving it as a potential weakness. I'm also reconsidering whether the distinction from InferFix is sufficiently clear and important—InferFix builds one dense index and filters post-hoc by type, while FTCR partitions upfront into 18 separate indices and classifies the query first. The architectural difference is real, but I need to articulate why this matters for performance or efficiency.

Actually, looking more carefully at InferFix's approach, it seems like it's more conservative than I initially thought—it can fall back to cross-type patches when same-type options are limited. FTCR's hard partitioning is the more aggressive strategy. I should reframe this as FTCR committing to within-type retrieval at construction time versus InferFix making that decision at query time. Let me double-check the exact InferFix methodology to make sure I'm characterizing this correctly.

Reading the paper more carefully, InferFix enforces same-type retrieval with a 60% similarity threshold, which means both approaches actually enforce the same-type constraint—just at different stages. So the real difference comes down to scale and taxonomy: InferFix operates on a much larger corpus across Java and C#, while FTCR works with only 3,050 natural pairs and uses a different type classification system.

But there's a subtle design distinction I'm noticing: InferFix can fall back to cross-type retrieval if same-type patches don't meet that 60% threshold, whereas FTCR's hard partitioning by type never crosses boundaries. That's actually a meaningful trade-off between flexibility and type-specificity.

The proposal's core differentiators hold up—LLM-inferred labels versus Infer's static analysis, the natural-bug taxonomy versus Infer-specific diagnostics, and the natural corpus versus InferredBugs—these are legitimate distinctions that justify the approach.

Looking at what remains, the main concerns are the LLM annotation accuracy evidence from prior work showing much lower performance at fine-grained levels, the existence of LTFix as a related baseline, and the tight 2-day writing timeline. The annotation accuracy issue is the most pressing since the proposal's central claim hinges on measuring LLM classifier performance against DebugBench ground truth, and if prior work already demonstrated that LLM auto-labeling struggles at the tertiary level, that could undermine the claimed performance gains.

The key insight is that even if the proposal finds X% accuracy (likely in the 35% range based on prior results), it can still make a valid contribution by showing that hard type partitioning only helps when classifier accuracy is high, and that a confidence-gated hybrid approach works better when accuracy is low. This is publishable, but the proposal needs to preemptively cite the prior work and frame the study as testing whether few-shot prompting with DebugBench-specific examples can improve upon those baseline accuracy numbers. Without this framing, reviewers familiar with that prior result will question why it wasn't addressed.

I should verify whether 2407.06153 is actually relevant though. The paper studies bug classification in LLM-generated code, but the FTCR proposal is about bugs in human-written code, so the taxonomies and accuracy baselines might not be directly comparable. Let me think about whether this distinction actually matters for the citation concern.

The core issue is that the proposal claims LLMs can achieve high accuracy on bug classification without citing evidence that contradicts this. Even if the domains differ, the paper still provides relevant counterevidence that should be acknowledged. The proposal should explain why their setting with DebugBench examples and few-shot prompting would perform better than the general case.

So my final assessment is: this is a real concern but somewhat mitigated by the domain and taxonomy differences. The authors need to cite 2407.06153 and explain how their approach differs. I'm also flagging two other issues—uncited work on type-guided retrieval and the risky two-day writing timeline—and settling on scores of 3.5 for novelty and feasibility, 4 for clarity, with an overall recommendation to revise.

Looking back at the individual scores more carefully: the novelty is genuinely incremental over ReCode despite the hard versus soft comparison being novel, the feasibility is tight but workable with confirmed compute, and the clarity is strong with a well-structured framework, though the writing window remains a risk factor that brings the overall average to 3.5—below the 4.0 threshold.

The core issues holding this back are the LLM annotation accuracy concern that hasn't been fully addressed, the compressed timeline, and the incremental nature of the contribution. Since this is Round 7 of 10, I should acknowledge the substantial progress while pushing for concrete improvements in these remaining areas. The LLM annotation accuracy study is the critical gap here—reviewers in this space will definitely notice its absence, so I need to cite it and clarify how their few-shot approach with DebugBench examples differs from general zero-shot settings. The other issues are relatively minor. The science itself holds up, so addressing the annotation accuracy concern and adding a brief mention of LTFix should be enough to push this toward acceptance in the next round.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5ee9b1a-d877-41f4-8741-aed1965ce444",
  "isSidechain": false,
  "requestId": "req_011CatU6bHkcb4X8VxDaw6oc",
  "type": "assistant",
  "uuid": "f1a6183f-913d-4cfe-9b86-cac7afcde7eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EQPXtuNAW5JWEKnBcCiFgr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3842,
      "cache_creation_input_tokens": 6476,
      "cache_read_input_tokens": 41332,
      "output_tokens": 9332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3842,
          "output_tokens": 9332,
          "cache_read_input_tokens": 41332,
          "cache_creation_input_tokens": 6476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6476
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

_source line 19 · 2026-05-10T07:11:32.159Z_

I now have comprehensive independent research findings. Let me synthesize and issue the verdict.

**Key independent findings:**

1. **ReCode IS cited** in the proposal — this was a prior issue now resolved. The differentiation (algorithm-types in competitive programming vs. bug-types in repository bugs) is explicitly stated.

2. **InferFix architecture confirmed**: Single unified index + post-hoc type filter at query time. The proposal's Round 7 correction ("type structures training pairs but is not an explicit encoder input") is **accurate**. The differentiation from FTCR (pre-construction partitioning vs. query-time filtering) is real and correctly stated.

3. **ReinFix ICSE 2026 confirmed**. Soft embedding with text-embedding-3-large confirmed. FTCR's characterization is correct.

4. **Critical uncited paper found**: arXiv:2407.06153 ("What's Wrong with Your Code Generated by Large Language Models?") measured LLM auto-labeling of fine-grained bug types — fully automated tertiary-level accuracy: **5.2%**; secondary-level: **35.7%**. This directly challenges FTCR's assumption that X% will be high enough for hard partitioning to help on net.

5. **TypeRepair differentiation**: Still unverifiable from publicly accessible sources (paywall). The evidentiary inference (evaluation on project-internal datasets only) is plausible but unconfirmed.

6. **Uncited related work**: LTFix (arXiv 2506.18394, "Tracing Errors, Constructing Fixes: Repository-Level Memory Error Repair via Typestate-Guided Context Retrieval") uses type-guided retrieval for code repair.

7. **EMNLP 2026 ARR deadline confirmed**: May 25, 2026.

8. **All Round 6 issues addressed**: DebugBench 4-major/18-minor hierarchy is correct throughout; InferFix architecture is correctly described; compute readiness is stated; statistical tests specified (McNemar's, Fisher's exact, 95% CI); EMNLP Findings commitment is firm.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The hard-categorical-partition + LLM-type-inference mechanism is identical to ReCode (CIKM 2025); FTCR's contribution is extending this to natural repository bugs with the DebugBench taxonomy and adding the direct hard-vs-soft empirical comparison, which is incremental but valid. No paper has made the specific hard-vs-soft comparison on natural bugs with this taxonomy."
    },
    "feasibility": {
      "score": 3,
      "rationale": "Compute is now confirmed provisioned (2 A100 nodes, Docker ready), annotation cost is well-estimated, and the MVS (DebugBench + Defects4J ablations) is achievable in 10-14 days; however, the 2-day paper writing window (Days 13-15) remains the critical path risk, and if X% is in the 5-35% range suggested by prior work, the positive-contribution framing may need to be revised mid-experiment."
    },
    "clarity": {
      "score": 4,
      "rationale": "The X%/Y%/Z%/W% falsifiable framework is well-defined, the EMNLP Findings target is committed, the DebugBench hierarchy is correctly stated, and the statistical analysis plan (McNemar's test, Fisher's exact, 95% CI, n≥30 threshold) is fully specified."
    },
    "impact": {
      "score": 3,
      "rationale": "Contributes a calibrated empirical finding about when LLM-inferred categorical labels enable effective retrieval routing — this generalizes beyond code repair to any RAG system using LLM-generated labels, which is the legitimate EMNLP Findings angle, but the scope is narrow and the primary venue is Findings rather than a flagship venue."
    }
  },
  "issues": [
    "MEDIUM — Uncited counterevidence on LLM annotation accuracy undermines X% expectations without preemption: arXiv:2407.06153 ('What's Wrong with Your Code Generated by Large Language Models?') independently measured LLM auto-labeling of fine-grained bug types and found fully automated tertiary-level accuracy of 5.2% and secondary-level accuracy of 35.7%. FTCR's core hypothesis depends on X% being high enough for correctly-classified instances (driving Z%) to outnumber misclassified instances (driving W%). If X% is in the 35% range, hard partitioning would hurt on average. The proposal must cite this paper and explain why its setting (few-shot prompting with DebugBench-specific demonstration examples, a taxonomy purpose-built for LLM classification) is expected to achieve substantially higher accuracy than the general case studied in 2407.06153. Framing FTCR as 'testing whether task-specific few-shot prompting overcomes the documented accuracy floor in general LLM bug classification' would strengthen both the motivation and the EMNLP NLP angle.",
    "LOW — LTFix (arXiv 2506.18394, 'Tracing Errors, Constructing Fixes: Repository-Level Memory Error Repair via Typestate-Guided Context Retrieval', June 2025) uses type-guided retrieval (typestate automaton) for memory errors in C code at the repository level. While domain-specific, it is the closest recent work to FTCR's type-guided retrieval architecture for repository-level repair and should be cited with a one-sentence differentiation (C memory errors only vs. FTCR's 18-subtype taxonomy across C++/Java/Python).",
    "LOW — The two-day paper writing window (Days 13–15, May 23–25) remains structurally fragile. If SWE-bench Lite results arrive on Day 12 and require reframing, or if any ablation produces surprising results requiring additional runs, the window collapses. The pre-drafted skeleton policy (stated as prepared during Days 4–6) is necessary but not sufficient mitigation. The proposal should commit to one additional write-up contingency: if any experiment is not complete by Day 12 EOD, drop it and close the paper with the MVS results only rather than attempting to extend experiments into the writing window.",
    "LOW — TypeRepair (SQJ 2026) differentiation remains technically unverifiable from publicly accessible sources: the claim that Stage 3 context selection draws from within-project code only is inferred from the evaluation design (Defects4J/QuixBugs are project-internal datasets) rather than directly stated in the paper. This evidentiary basis is now stated in the proposal ('The evaluation design makes the within-project scope structurally evident'), which is defensible. However, reviewers with full SQJ access could refute this if wrong. Consider adding a qualifier: 'To the best of our knowledge from the publicly accessible abstract and benchmark descriptions, TypeRepair's context selection stage draws from within-project code files; any reviewer with full SQJ article access who finds this claim incorrect is encouraged to provide the correction.' This signals intellectual honesty and invites correction rather than assertion."
  ],
  "feedback": "Round 7 has successfully resolved all five Round 6 issues: EMNLP Findings commitment is firm, DebugBench 4-major/18-minor hierarchy is correct throughout, compute readiness is confirmed, InferFix architecture is accurately characterized, and statistical significance is fully specified. The proposal is in its strongest state to date. Two targeted fixes would bring this to submission-ready: (1) CITE AND ADDRESS arXiv:2407.06153 — this is the most important remaining gap. Add a sentence in the introduction or related work: 'Prior work has shown that fully automated LLM classification of fine-grained bug types achieves ~35% accuracy at the secondary level (citation), motivating the question of whether task-specific few-shot prompting with a purpose-built taxonomy (DebugBench) achieves sufficient accuracy to make hard categorical partitioning beneficial on net. FTCR's X%/Y% measurements directly test this.' This frames X% as the paper's central NLP finding and preempts the most likely reviewer objection. (2) ADD ONE SENTENCE about LTFix in the landscape paragraph: 'LTFix applies typestate-automaton-guided retrieval to memory errors in C at the repository level; FTCR generalizes type-conditioned retrieval to 18 semantic sub-types across C++/Java/Python using LLM-inferred labels.' These two additions are low-effort and high-impact for reviewer confidence. The core science is sound — the X%/Y%/Z%/W% causal decomposition is a legitimate EMNLP Findings contribution that no existing paper has made for natural repository bugs.",
  "reason": "All Round 6 issues resolved, but one medium gap remains: arXiv:2407.06153 documents 5.2-35.7% LLM bug-type classification accuracy that directly challenges X% expectations and is not cited or preempted."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1a6183f-913d-4cfe-9b86-cac7afcde7eb",
  "isSidechain": false,
  "requestId": "req_011CatU6bHkcb4X8VxDaw6oc",
  "type": "assistant",
  "uuid": "edcec11c-cd77-4b1b-8a9b-0a5f5f33d04b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EQPXtuNAW5JWEKnBcCiFgr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3842,
      "cache_creation_input_tokens": 6476,
      "cache_read_input_tokens": 41332,
      "output_tokens": 9332,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6476,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3842,
          "output_tokens": 9332,
          "cache_read_input_tokens": 41332,
          "cache_creation_input_tokens": 6476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6476
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
  "leafUuid": "edcec11c-cd77-4b1b-8a9b-0a5f5f33d04b",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate FTCR for EMNLP 2026 ARR Submission (Round 7)",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "edcec11c-cd77-4b1b-8a9b-0a5f5f33d04b",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate FTCR for EMNLP 2026 ARR Submission (Round 7)",
  "sessionId": "53165300-8211-427a-abe2-57e64b57a116"
}
```

---
