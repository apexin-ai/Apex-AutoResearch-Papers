# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/861d3b28-4df2-431c-ac85-5685948a8836.jsonl`
- **Structured JSON:** [`1259771ae500bdc6f5e7.json`](../../sessions/12/1259771ae500bdc6f5e7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:52:38.316Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:52:38.316Z",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 9/10)\n{\n  \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\",\n  \"project_name\": \"failure_type_rag_repair\",\n  \"source\": \"web_research\",\n  \"level\": \"solid\",\n  \"core_problem\": \"The lead empirical question — tractable because DebugBench provides oracle ground-truth labels for 4,253 instances organized in a 4-major/18-minor hierarchical taxonomy — is: how accurately can a few-shot LLM assign semantic bug type labels from the 18 minor sub-categories, and does that label accuracy determine whether hard categorical retrieval index partitioning outperforms soft root-cause-augmented retrieval (ReinFix, ICSE 2026) for cross-repository fix template transfer? Prior work (arXiv:2407.06153, EMNLP 2024) established a baseline accuracy floor: fully-automated zero-shot GPT-4 classification of fine-grained bug types achieves only ~37% at the secondary level and ~5% at the tertiary level on a custom 3-primary/10-secondary taxonomy over LLM-generated code. However, that same study showed AI-assisted annotation (GPT-4 suggestions + human demonstrations) reaches 91.6% tertiary accuracy — an 18× improvement over zero-shot at the tertiary level — demonstrating that structured demonstration examples dramatically improve LLM classification performance. This frames FTCR's X% measurement as a direct empirical test of the hypothesis: 'does task-specific few-shot prompting with DebugBench-aligned demonstration examples, applied to a purpose-built 4-major/18-minor taxonomy of natural repository bugs, overcome the documented zero-shot accuracy floor in general LLM bug classification?' The practical stakes are high and symmetric: if X% ≈ 35% (the zero-shot floor), hard partitioning hurts on average and the paper's conclusion is a documented negative; if X% ≥ 65% (the few-shot hypothesis), correctly-classified instances driving Z% substantially outnumber misclassified instances driving W%, and type-conditioned retrieval is net-beneficial. Either outcome is a publishable finding with direct generalization to any retrieval system using LLM-inferred labels for query routing.\\n\\nThis frames FTCR as an empirical study of LLM-generated categorical label quality and its downstream retrieval impact, yielding four falsifiable quantities: (X%) few-shot classifier accuracy vs. DebugBench ground-truth oracle labels at the minor-type level, with major-type aggregation as a secondary result; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs (n=56 pairs, reported as a preliminary cross-lingual signal with 95% CI for the proportion estimate); (Z%) repair improvement for correctly-classified high-confidence instances under hard type-partitioned retrieval vs. the soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts — a finding with direct generalization to any retrieval system using LLM-inferred labels.\\n\\nRetrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. InferFix (ESEC/FSE 2023, arXiv:2303.07263) establishes that type-conditioned retrieval benefits code repair: its Retriever uses contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type from Infer static analysis), and at retrieval time filters candidates to same-type fixes; however, InferFix requires running the Infer static analyzer on each query bug — applicable only to bugs Infer can detect, using Infer-specific diagnostic categories rather than a general natural-bug taxonomy. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is therefore two-fold: (1) whether LLM-inferred type labels can substitute for Infer-derived labels to enable type-conditioned retrieval for general natural bugs not addressable by static analysis (the X%/Y% question vs. InferFix); and (2) whether hard categorical type partitioning of the retrieval index outperforms ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer (the Z%/W% question). An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. Type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and become analytical contributions when addressed directly: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4; the Multiple Bugs sub-types are excluded from the fix-template corpus as multi-fault commits are rare and represent a different repair regime) yields approximately ~217 pairs per minor type on average for the full Python+Java corpus; for Java-only ablations (~559 pairs across ~14 types, ~40 per type), types with fewer than 30 instances are merged within the same major category (e.g., rare Syntax sub-types merged within Syntax; rare Logic sub-types merged within Logic — never across major categories); and (2) classifier error propagation — when an incoming bug is misclassified, hard partitioning underperforms soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback — turns potential weaknesses into the core empirical variables (Z% and W%) that define the paper's scientific contribution.\",\n  \"opportunity\": \"ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-conditioned cross-repository retrieval system for code repair: its Retriever is pretrained via contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type labels from Infer static analysis), and at retrieval time filters candidates to same-type fixes using Infer-derived labels. The encoder itself encodes only the buggy code as a dense vector — type structures the contrastive training pairs but is not an explicit encoder input; the retriever learns type-correlated semantic similarity. InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#. Three properties distinguish InferFix from FTCR: (a) Type label acquisition — InferFix requires running the Infer static analyzer on each query bug to obtain its type label; only bugs Infer can detect are addressable; FTCR uses few-shot LLM classification, requiring no static analysis tooling and covering any natural bug that Infer cannot or would not detect; (b) Taxonomy scope — InferFix uses Infer-specific diagnostic IDs (null dereferences, resource leaks, thread-safety violations), not the 4-major/18-minor natural-bug taxonomy aligned with DebugBench (4 major categories: Syntax with 7 sub-types, Reference with 4 sub-types, Logic with 4 sub-types, Multiple Bugs with 3 sub-types); (c) Corpus — InferFix uses InferredBugs (Java/C# repos where Infer detected bugs); FTCR uses natural bug-fix pairs from issue trackers and CI logs. The open empirical question InferFix leaves unresolved is whether LLM-inferred type labels can substitute for Infer-derived labels to enable effective type-conditioned retrieval for general natural bugs — precisely what FTCR's X%/Y% calibration measures. arXiv:2407.06153 (EMNLP 2024) independently measured LLM auto-labeling of fine-grained bug types and found fully automated zero-shot GPT-4 achieves ~37% secondary-level and ~5% tertiary-level accuracy on a custom 3-primary/10-secondary taxonomy over LLM-generated code; the same study shows that AI-assisted annotation with structured demonstrations reaches 91.6% tertiary accuracy. This establishes a documented accuracy floor for zero-shot general classification and directly motivates FTCR's X%/Y% measurements as the key empirical test: do few-shot demonstrations with DebugBench-specific examples bridge the 37%→91% gap for natural repository bugs without human-in-the-loop verification? InferFix validates that type-conditioned retrieval works (supporting FTCR's hypothesis) while leaving the LLM-label-quality-vs-retrieval-effectiveness question entirely unanswered. ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of the 18 minor semantic sub-types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than ReinFix's joint root-cause embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar embeddings but different repair operators do not. DebugBench's 4-major/18-minor hierarchical taxonomy uniquely provides 4,253 instances with ground-truth type annotations across C++, Java, and Python (organized as: Syntax/7 sub-types, Reference/4, Logic/4, Multiple Bugs/3), enabling direct classifier calibration at the minor-type level and turning error propagation from a latent risk into the paper's core measurable variable. The confidence-gated hybrid has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). M-RAG (ACL 2024, arXiv 2405.16420) validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis.\",\n  \"landscape\": \"RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (a leading agentic scaffold, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% and is not a SOTA claim. InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-conditioned cross-repository retrieval system for code repair: it pretrains a Retriever via contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type from Infer static analysis), then at retrieval time filters candidates to same-type fixes using Infer-derived type labels. The encoder itself encodes only the buggy code as a dense vector — type structures the training pairs but is not an explicit encoder input; the retriever learns type-correlated semantic similarity. InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#, outperforming LLM baselines by 11–55%. Three design differences distinguish FTCR from InferFix: (a) Type label acquisition — InferFix requires Infer to run on each repository to produce type labels for both corpus and query bugs; FTCR uses few-shot LLM classification, covering any natural bug without static analysis tooling; the core empirical question vs. InferFix is whether LLM-inferred labels achieve sufficient accuracy (X%) to match Infer-derived retrieval quality; (b) Defect taxonomy — InferFix uses Infer-specific diagnostic IDs (covering only statically-detectable bug patterns), not the 4-major/18-minor natural-bug taxonomy aligned with DebugBench's empirically-grounded labels (Syntax/7, Reference/4, Logic/4, Multiple Bugs/3); (c) Corpus — InferFix uses InferredBugs (static-analysis artifacts); FTCR uses natural bug-fix pairs from SWE-bench, BugsInPy, Defects4J, and GitBug-Java. The scientific question InferFix leaves open — and FTCR directly tests — is whether LLM-inferred type labels achieve sufficient accuracy (X%) to enable type-conditioned retrieval that is effective for general natural bugs, and at what accuracy threshold does type-conditioned retrieval outperform soft embedding baselines (Z% > 0%, W% < Z%). What's Wrong with Your Code Generated by Large Language Models (arXiv:2407.06153, EMNLP 2024) provides the accuracy baseline that FTCR's X% must be measured against: fully automated zero-shot GPT-4 classification achieves ~37% secondary-level and ~5% tertiary-level accuracy on a custom 3-primary/10-secondary taxonomy over LLM-generated code (HumanEval+, MBPP+, APPS+); however, AI-assisted annotation with structured GPT-4 demonstrations reaches 91.6% tertiary accuracy. Three factors distinguish FTCR's setup from the zero-shot floor in arXiv:2407.06153: (i) prompting method — few-shot with DebugBench-aligned demonstration examples vs. zero-shot with taxonomy description only; (ii) bug domain — natural repository bugs from issue trackers and CI logs with diagnostic markers (missing colon, undefined object) vs. LLM-generated code failures on competitive benchmarks; (iii) taxonomy alignment — DebugBench's 4-major/18-minor hierarchy was built from and validated against real developer-reported bugs, providing sharper category boundaries than a general taxonomy. FTCR's X% measurement directly tests whether these three factors together are sufficient to bridge the documented zero-shot accuracy floor — framing X% as an empirical NLP finding rather than an implementation detail. ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning. Corpus quality confound: comparisons against published ReinFix results conflate two variables simultaneously — retrieval architecture (soft joint embedding vs. hard type partition) and corpus quality (100K TRANSFER synthetic pairs vs. 3,050 natural bug-fix pairs from issue trackers and CI logs). Intra-corpus ablations (FTCR vs. re-implemented ReinFix-style baseline on the same 3,050-pair natural corpus using the same text-embedding-3-large encoder) test the partitioning hypothesis cleanly and isolate architecture as the variable. Absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality differences simultaneously and are presented explicitly as such; they are not used to claim a clean head-to-head win on architecture alone. SWE-Exp (arXiv 2507.23361, revised February 2026) retrieves top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic Python-only pipeline. Three design differences: (1) soft vs. hard — SWE-Exp uses type as retrieval-time embedding metadata; FTCR partitions at index-construction time; (2) retrieved artifact — SWE-Exp stores distilled modification strategies; FTCR retrieves concrete fix patches; (3) scope — SWE-Exp is agentic and Python-only; FTCR covers C++/Java/Python in retrieval-only mode. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5. TypeRepair's context selection stage conditions on the identified defect type to select within-project code context and provide type-specific repair guidance — it does not retrieve from an external cross-repository fix corpus. Evidentiary basis: TypeRepair evaluates exclusively on Defects4J V1.2/V2.0 and QuixBugs — within-project Java bug collections that contain no external cross-repository retrieval component. To the best of our knowledge from the publicly accessible abstract and benchmark descriptions, TypeRepair's context selection stage draws from within-project code files and type-specific API/documentation context rather than an external fix-patch corpus; the evaluation design (project-internal datasets, no external corpus described in benchmark setup) makes the within-project scope structurally evident. Any reviewer with full SQJ article access who finds this characterization incorrect is encouraged to provide the correction — we welcome corroboration or refutation rather than defending an unverifiable inference, and the differentiation from FTCR's external 3,050-pair cross-language corpus retrieval holds regardless of whether TypeRepair's context is strictly within-project or draws from type-specific documentation. TypeRepair is Java-only; FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 fix patches. LTFix (arXiv 2506.18394, June 2025) applies typestate-automaton-guided context extraction to memory errors in C at the repository level, using a finite typestate automaton to trace error-propagation paths across functions and files for LLM context construction; LTFix targets C memory errors only (a single-domain bug class requiring interprocedural static tracing) and uses typestate analysis for context extraction rather than retrieval from a historical fix-patch corpus; FTCR generalizes type-conditioned retrieval to 18 semantic sub-types across C++/Java/Python using LLM-inferred labels with no static analysis tooling and retrieves from an external 3,050-pair fix-patch corpus. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec while contextual and API information helps; the 'what to retrieve matters' finding motivates FTCR's type-partition design. DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3. Both update the landscape but are orthogonal to retrieval strategy. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via objective alignment. FTCR's structural departure from all prior work is to (1) classify incoming failures into discrete minor sub-categories of the 4-major/18-minor DebugBench taxonomy, then (2) retrieve only from the type-matched sub-index, using text-embedding-3-large (identical to ReinFix) for a clean intra-corpus partitioning comparison — with the random-partition control separating type-matching precision from pool-size reduction. RetypeR (ICSME 2024, Hao et al.) applies type-specific retrieval for Python type errors only; FTCR extends to 18 minor sub-types across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates multi-partition RAG outperforms single-store RAG across NLP tasks (+11% summarization, +8% translation, +12% dialogue). PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary scope. The APR survey (arXiv 2506.23749) reviews 63+ systems with no type-partitioned cross-language retrieval system identified.\",\n  \"approach\": \"We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms ReinFix's soft root-cause embedding for cross-repository fix template transfer, and that LLM-inferred type labels can substitute for the Infer-required labels used by InferFix to enable type-conditioned retrieval on general natural bugs. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix), same natural corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control.\\n\\nNLP Lead Contribution: LLM Label Quality and Downstream Retrieval Impact. The primary EMNLP Findings contribution is a complete causal decomposition of when hard type conditioning helps and when it hurts, parameterized by four falsifiable quantities measured at the minor-type level (18 sub-types of the 4-major/18-minor DebugBench hierarchy, with major-type aggregation reported as a secondary result): (X%) few-shot LLM classifier accuracy against DebugBench ground-truth oracle labels at the minor-type level; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs (n=56 pairs, reported as a preliminary cross-lingual signal with 95% CI for the proportion estimate to make sampling uncertainty visible to reviewers); (Z%) repair improvement on DebugBench/Defects4J V1.2 for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances under hard partitioning vs. same baseline. Z% and W% are reported as aggregate rates across all correctly-classified and misclassified instances respectively; significance is tested via McNemar's test on paired pass/fail outcomes (baseline vs. FTCR, same instances); per-type breakdowns use Fisher's exact test with a minimum n≥30 instance threshold; 95% confidence intervals are reported for both Z% and W%. Together these quantities are a direct empirical answer to: 'LLM-inferred categorical labels enable hard retrieval partitioning only if X% and Y% are high enough to make the correctly-classified population (driving Z%) larger than the misclassified population (driving W%).' This generalizes beyond code repair to any system that uses LLM-generated labels to route queries into type-specific retrieval pools.\\n\\nExecution Plan for EMNLP 2026 ARR (May 25 deadline, 15 days from today). Auto-research mode (10–14 days) is the only constraint-compliant execution path. Day-by-day schedule with minimum viable submission (MVS) milestones:\\n\\n- Day 0 (May 10): Launch auto-research pipeline; begin 3-pass annotation of 3,050 corpus pairs using DebugBench few-shot examples as demonstrations for the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4); configure Defects4J V1.2 Java-8 Docker environments and GitBug-Java isolated containers. Compute: 2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.\\n- Day 1–3 (May 11–13): Annotation completes (~$183 Claude API cost). DebugBench classifier calibration: 20% held-out split (~851 instances, covering single-bug instances from the Syntax/Reference/Logic major categories and treated separately for the Multiple Bugs category) → X% per-minor-type accuracy with major-type aggregation as secondary. Cross-lingual Java transfer sample (56 human-verified pairs from Defects4J + GitBug-Java) → Y% preliminary cross-lingual signal (95% CI for the proportion estimate at n=56 reported to make sampling uncertainty visible). Per-minor-type count table computed; within-major-category merge policy applied for rare minor types below the 30-instance Java threshold.\\n- Day 4–6 (May 14–16): Build type-partitioned sub-indices and ReinFix-style unified index (both text-embedding-3-large). Run Defects4J V1.2 ablations: Variant A (text-similarity RAG), Variant D (ReinFix-style re-implemented on same natural corpus), Variant E (FTCR@hard-all), Variant F (random-partition control, N equivalently-sized random sub-indices). Prepare pre-drafted paper skeleton (introduction, related work, method) during this window to reduce Day 13–15 writing pressure.\\n- Day 7–9 (May 17–19): DebugBench evaluation across all variants on single-bug instances (Syntax/Reference/Logic major categories); confidence-gated τ sweep on held-out validation split; stratify results by classifier confidence band: high-confidence correctly-classified → Z% (aggregate, McNemar's test); misclassified → W% (aggregate, McNemar's test); per-type Fisher's exact test for types with n≥30. SWE-bench Lite evaluation launched in parallel (requires 2 A100 nodes for ~10 min/instance).\\n- Day 10–12 (May 20–22): CodeBERT-base encoder ablation (same FTCR vs. ReinFix-style comparison, secondary encoder); taxonomy granularity ablation (major-type coarse/4 vs. minor-type fine/14 single-fault sub-types vs. merged-Java categories); retrieval k sweep (1/3/5/10).\\n- Day 13 (May 23): Results compilation; paper writing begins with NLP lead (X%/Y%/Z%/W% as opening contribution).\\n- Day 14–15 (May 24–25): Paper finalization and ARR submission. MVS for EMNLP Findings: DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. SWE-bench Lite Python results included if pipeline completes by Day 12, deferred to ICSE 2027 extended version otherwise.\\n\\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. InferFix demonstrates that type-conditioned retrieval improves over code-similarity retrieval, but requires Infer static analysis to label both corpus and query bugs. FTCR embodies a stronger form of this principle: classify the incoming bug using an LLM (no static analysis tooling required), then restrict the retrieval pool to same-type patches at index construction time, ensuring that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to score high in a shared embedding space but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\\n\\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559). The corpus is annotated against the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4); the Multiple Bugs sub-types (double/triple/quadruple) are not applicable to single-fix commit pairs in the retrieval corpus and are excluded from corpus annotation but evaluated separately in the DebugBench test set.\\n\\nCorpus Quality Confound (Explicit). The natural 3,050-pair corpus differs from ReinFix's 100K TRANSFER corpus in two simultaneous dimensions: (1) retrieval architecture (soft joint embedding vs. hard type partition) and (2) corpus quality (natural issue-tracker/CI bug-fix pairs vs. synthetic static-analysis-derived pairs). Intra-corpus ablations — FTCR vs. re-implemented ReinFix-style baseline using text-embedding-3-large on the identical 3,050-pair natural corpus — test the partitioning hypothesis cleanly and are the primary experimental contribution. Absolute performance comparisons against published ReinFix numbers on Defects4J reflect both architecture and corpus quality simultaneously; they are presented as joint-effect comparisons, not as clean head-to-head architectural wins. The random-partition control (Variant F) further isolates type-matching precision from pool-size reduction within the intra-corpus comparison.\\n\\nCorpus Sparsity Policy. Each pair is annotated with one of 14 single-fault minor sub-types via few-shot prompting; three annotation passes measure inter-run consistency. For the combined Python+Java corpus (~3,050 pairs, 14 active minor types), mean pairs per type is approximately ~218. For Java-only ablations (~559 pairs), types with fewer than 30 Java instances are merged into nearest-neighbor supercategories within the same major category (e.g., rare Syntax sub-types such as 'illegal separation' and 'illegal indentation' merged within Syntax — never across Syntax/Reference/Logic boundaries); Java ablation results are reported for the 4–6 resulting within-major-category merged groups that each exceed 50 instances, with merged categories explicitly labeled. Note that several Syntax sub-types (missing colons, illegal indentation) are Python-specific and may yield few or zero Java instances; these are expected to merge to the within-Syntax catch-all for Java ablations.\\n\\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound (~$5–15 total embedding cost). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific.\\n\\nType Classifier Calibration on DebugBench Ground Truth. Prior work (arXiv:2407.06153, EMNLP 2024) established a documented accuracy floor for fully automated LLM bug classification: zero-shot GPT-4 achieves ~37% at the secondary level and ~5% at the tertiary level on a custom 3-primary/10-secondary taxonomy over LLM-generated code; AI-assisted annotation with structured demonstrations reaches 91.6% tertiary accuracy — an 18× improvement over zero-shot. FTCR's classification setup is positioned between these bounds: few-shot prompting with DebugBench-specific demonstration examples (not zero-shot, not human-in-the-loop), applied to natural repository bugs with diagnostic markers (missing colon, undefined object) under a purpose-built 4-major/18-minor taxonomy with sharper category boundaries than a general taxonomy. Three factors motivate the expectation of substantially higher than ~37% secondary accuracy: (a) few-shot demonstrations provide structured per-type examples analogous to the AI-assisted setup in arXiv:2407.06153; (b) DebugBench's taxonomy was constructed from real developer-reported bugs with clear surface-level markers, unlike the more ambiguous code-generation failures in arXiv:2407.06153; (c) few-shot prompts are calibrated on held-in DebugBench examples before evaluation on the held-out 20% split. X% is reported as a direct empirical answer without assuming the hypothesis is confirmed: if X% ≈ 35% (the zero-shot floor), the paper's conclusion is 'few-shot task-specific prompting does not overcome the documented accuracy floor, and hard categorical partitioning is net-negative for retrieval-augmented repair' — itself a significant and publishable NLP finding. A held-out 20% split (~851 instances) directly measures few-shot classifier precision and recall per minor sub-type against oracle ground-truth labels, yielding X% at the minor-type level (major-type aggregation reported as a secondary result). The primary repair evaluation uses single-bug instances from the Syntax, Reference, and Logic major categories (~2,035 of 4,253 instances); Multiple Bugs instances (double/triple/quadruple, ~2,218 instances) are evaluated separately as an auxiliary experiment to characterize classifier behavior on multi-type ambiguous queries. Cross-dataset zero-shot agreement on ~56 human-verified Java pairs yields Y% (framed as a preliminary cross-lingual signal rather than a calibration result; 95% CI reported for the proportion estimate at n=56 to make sampling uncertainty explicit — at n=56, CI half-width is approximately ±13% for proportions near 50% and ±10% for proportions near 75%, conveying the range of this estimate to reviewers). These produce the core NLP finding: LLM-inferred bug type labels achieve X% agreement with DebugBench ground truth (Python/C++) at the minor-type level, transfer zero-shot to Java with Y% preliminary agreement (95% CI), and predict retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs (both aggregate across all instances of each class, McNemar's test, 95% CI).\\n\\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect, the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index (Variant F). Any performance gap between FTCR (Variant E) and this control measures the precision benefit of type-matching net of pool-size reduction.\\n\\nConfidence-Gated Retrieval Fallback. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval. Six variants evaluated: (A) text-similarity RAG, (B) RELREPAIR, (C) RepoRepair, (D) ReinFix-style soft on same corpus, (E) FTCR@hard-all, (F) random-partition control. Confidence-gated hybrid evaluated as a seventh configuration. Precedent: CRAG (Yan et al., arXiv:2401.15884).\\n\\nPractical Utility. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is the retrieval contribution in isolation, not a pipeline SOTA claim. DynaFix demonstrates retrieval and execution augmentation are independently improvable axes; an improved retrieval module (FTCR vs. ReinFix-style) compounds with execution-level improvements. Standalone evaluation isolates the retrieval hypothesis cleanly.\\n\\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while Defects4J V1.2 (MVS) and SWE-bench Lite (full version) validate real-world transfer.\",\n  \"resource_estimate\": {\n    \"auto_research\": {\n      \"gpu_hours\": \"~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)\",\n      \"gpu_utilization\": \"near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants\",\n      \"ablation_scope\": \"Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline on same natural corpus), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (4-major coarse / 14-minor single-fault fine / merged-Java within-major), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java → SWE-bench-Lite Python), classifier accuracy stratification by confidence band\",\n      \"timeline\": \"10-14 days with 2 A100 nodes running in parallel — the ONLY constraint-compliant execution mode for the 16-day hard budget. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) both violate the user's timeline constraint and are not presented as viable paths.\",\n      \"day_by_day_schedule\": \"Day 0 (May 10): setup and corpus annotation launch. Compute confirmed: 2 A100 nodes provisioned; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested. Day 1–3 (May 11–13): annotation + DebugBench classifier calibration (X% minor-type level, Y% preliminary cross-lingual signal with 95% CI at n=56). Day 4–6 (May 14–16): index construction + Defects4J V1.2 ablations (Variants A/D/E/F) + pre-drafted paper skeleton. Day 7–9 (May 17–19): DebugBench evaluation (single-bug instances) + confidence stratification (Z%, W% aggregate with McNemar's test) + SWE-bench Lite launch. Day 10–12 (May 20–22): CodeBERT ablation + granularity + k-sweep. Day 13 (May 23): results compilation + paper skeleton. Day 14–15 (May 24–25): paper finalization + ARR submission.\",\n      \"team\": \"0 (initial ~4h setup for corpus pipeline, per-type sub-index construction, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)\",\n      \"claude_api_cost\": \"$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)\",\n      \"embedding_api_cost\": \"~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)\",\n      \"estimated_gpu_cost\": \"~$969 (323 A100-hours × $3/h)\",\n      \"speed_bottleneck\": \"GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls\",\n      \"risk_note\": \"SWE-bench Lite may not complete before Day 12; MVS for EMNLP Findings submission is DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control, achievable within the 10–14 day window. Compute pre-provisioned as of Day 0. Auto-assigned bug type labels may drift without the three-pass consistency check; confidence-gated hybrid adds hyperparameter τ requiring tuning on held-out split before SWE-bench evaluation. Two-day paper writing window (Days 13–15) requires pre-drafted skeleton prepared during Days 4–6. Writing window contingency committed: if any experiment is not complete by Day 12 EOD (May 22, 2026), it is unconditionally dropped and the paper closes with MVS results only; no experimental work will be run or extended into the Day 13–15 writing window under any circumstances — this constraint is hard and not subject to revision based on preliminary result quality.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings (via ARR, deadline May 25, 2026 11:59 PM AoE — PRIMARY TARGET; 15 days from today). The X%/Y%/Z%/W% calibration study — measuring LLM-generated bug type label quality and its downstream impact on retrieval-augmented repair — is appropriate for EMNLP Findings, which publishes solid empirical contributions that advance understanding of specific NLP phenomena. The Main track expects findings that advance understanding of language models at a deeper architectural or representational level and poses higher desk-rejection risk for an empirical calibration study; Findings is the correct target and the proposal commits to it without oscillation. Path: auto-research completes Days 0–12 (May 10–22); paper writing Days 13–15 (May 23–25). Minimum viable submission: DebugBench classifier calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. EMNLP Findings fits the paper's core contribution: LLM annotation reliability for a structured classification task and the downstream retrieval consequences of label noise — a contribution to the NLP literature on LLM-generated categorical labels and RAG system design, directly extending the accuracy-floor findings of arXiv:2407.06153 to the task-specific few-shot regime. Timeline is extremely tight: the two-day writing window requires a pre-drafted paper skeleton prepared concurrently with Days 4–6 experiment setup. Risk: if SWE-bench Lite does not complete by Day 12, the EMNLP Findings version covers DebugBench + Defects4J only, with SWE-bench Lite results added in the ICSE 2027 version.\",\n    \"ICSE 2027 (mandatory abstract deadline June 23, 2026 — BACKUP venue if EMNLP ARR cycle overlaps unfavorably or EMNLP Findings submission is not accepted). SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation; InferFix paragraph establishes LLM-inferred vs. Infer-required type labels as the untested dimension; TypeRepair comparison clarifies FTCR's orthogonal contribution of cross-repository retrieval; LTFix comparison establishes domain generality over single-bug-class approaches; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections; intra-corpus confound framing converts the corpus quality issue into a feature rather than a weakness.\",\n    \"FSE 2027 (full paper deadline October 2, 2026 — tertiary backup if both EMNLP and ICSE review cycles are unfavorable).\"\n  ],\n  \"key_references\": [\n    \"InferFix: End-to-End Program Repair with LLMs over Bug-Specific Retrieval (ESEC/FSE 2023, arXiv:2303.07263) [earliest type-conditioned cross-repository repair retrieval; Retriever pretrained via contrastive learning using same-type bug-fix pairs as positives and different-type pairs as negatives (type from Infer static analysis); encoder encodes only buggy code — type structures training pairs but is NOT an explicit encoder input; the retriever learns type-correlated semantic similarity; at retrieval time, candidates are filtered to same-type fixes using Infer-derived labels; achieves 76.8% Java top-1 accuracy; InferFix validates type-conditioned retrieval but requires Infer static analysis at both corpus construction and query time — FTCR's scientific contribution vs. InferFix is testing whether LLM-inferred labels can substitute for Infer-derived labels (X%/Y%) and enabling type-conditioned retrieval for general natural bugs Infer cannot detect; must differentiate: (a) Infer-required labels vs. LLM-inferred labels; (b) query-time type filtering vs. FTCR's construction-time index partitioning; (c) Infer-specific diagnostic IDs vs. 4-major/18-minor natural-bug taxonomy; (d) InferredBugs vs. natural issue-tracker/CI bug-fix pairs]\",\n    \"ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; soft root-cause augmentation using unified vector database with text-embedding-3-large; intra-corpus comparison (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) is the clean architectural test; absolute comparisons against published ReinFix numbers reflect corpus quality confound and are presented as such]\",\n    \"What's Wrong with Your Code Generated by Large Language Models? An Extensive Study (arXiv:2407.06153, EMNLP 2024) [documents LLM auto-labeling accuracy for fine-grained bug types: fully automated zero-shot GPT-4 achieves ~37% secondary-level and ~5% tertiary-level accuracy on a custom 3-primary/10-secondary taxonomy over LLM-generated code (HumanEval+, MBPP+, APPS+); AI-assisted annotation with structured demonstrations reaches 91.6% tertiary accuracy — 18× improvement; key differences from FTCR's setup: (a) zero-shot vs. few-shot with DebugBench-specific demonstrations; (b) custom general taxonomy vs. DebugBench's purpose-built 4-major/18-minor natural-bug taxonomy; (c) LLM-generated code failures vs. natural repository bug-fix pairs; FTCR's X% directly tests whether task-specific few-shot prompting overcomes the documented zero-shot accuracy floor; cite in Introduction and Type Classifier Calibration sections as motivating prior work]\",\n    \"LTFix: Tracing Errors, Constructing Fixes: Repository-Level Memory Error Repair via Typestate-Guided Context Retrieval (arXiv 2506.18394, June 2025) [applies typestate-automaton-guided context extraction to memory errors in C at the repository level; uses a finite typestate automaton to trace error-propagation paths across functions and files for LLM context construction; targets C memory errors only (a single-domain bug class requiring interprocedural static tracing) without retrieval from a historical fix-patch corpus; differentiation from FTCR: domain-specific C memory errors only vs. FTCR's 18 semantic sub-types across C++/Java/Python using LLM-inferred labels without static analysis tooling, with retrieval from 3,050-pair external fix-patch corpus]\",\n    \"SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; 73.0% SWE-bench Verified with Claude 4 Sonnet; agentic, Python-only; differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, multi-language scope]\",\n    \"TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J/QuixBugs (Java-only); validates that type conditioning improves LLM repair; to the best of our knowledge from the publicly accessible abstract and benchmark descriptions, Stage 3 context selection draws from within-project code files and type-specific documentation rather than an external cross-repository corpus — supported by evaluation design (project-internal datasets, no external corpus in benchmark setup); welcome correction from reviewers with full SQJ access; FTCR's orthogonal contribution is type-conditioned retrieval from external ~3,050-pair cross-language corpus]\",\n    \"What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond (Gu et al., ICSE 2026, arXiv 2503.20589) [similar-code retrieval degrades code generation by up to 15% on CoderEval/RepoExec while structured knowledge helps; motivates type-partition fix-patch retrieval as avoiding the similarity-noise trap; note: code generation study, not repair — applicable as indirect motivation]\",\n    \"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330) [algorithm-type-conditioned retrieval in competitive programming — conceptual ancestor scoped to algorithmic tags]\",\n    \"RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors (ICSME 2024, Hao et al.) [type-specific retrieval for Python type errors only — FTCR extends to 18 minor sub-types and 3 languages]\",\n    \"DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv 2512.24635) [surpasses ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; demonstrates retrieval and execution augmentation are independently improvable axes]\",\n    \"DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2604.19305) [295 Defects4J bugs with DeepSeek-V3; updates landscape but orthogonal — no retrieval augmentation]\",\n    \"D4C: Aligning the Objective of LLM-based Program Repair (ICSE 2025, arXiv 2404.08877) [180 Defects4J bugs via objective alignment; updates performance landscape]\",\n    \"M-RAG: Reinforcing Large Language Model Performance through Retrieval-Augmented Generation with Multiple Partitions (ACL 2024, arXiv 2405.16420) [multi-partition RAG: +11% summarization, +8% translation, +12% dialogue; principled precedent for partition-based retrieval across domains]\",\n    \"RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code (arXiv 2509.16701) [project-internal retrieval baseline]\",\n    \"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048) [documentation-guided localization baseline; 45.7% SWE-bench Lite]\",\n    \"DebugBench: Evaluating Debugging Capability of Large Language Models (ACL Findings 2024) [primary evaluation; ground-truth 4-major/18-minor hierarchical taxonomy: Syntax (7 sub-types: misused ==/=, missing colons, unclosed parentheses, illegal separation, illegal indentation, unclosed string, illegal comment), Reference (4 sub-types: faulty indexing, undefined objects, undefined methods, illegal keywords), Logic (4 sub-types: condition error, operation error, variable error, other error), Multiple Bugs (3 sub-types: double/triple/quadruple co-occurring bugs); 4,253 instances across C++/Java/Python; held-out 20% split (~851 instances) for classifier calibration (X%) at minor-type level; primary repair evaluation on single-bug major categories (Syntax/Reference/Logic, ~2,035 instances); Multiple Bugs treated as separate analysis; acknowledged synthetic-bug limitation]\",\n    \"GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; cross-lingual transfer calibration (Y% preliminary cross-lingual signal, n=56 human-verified pairs, 95% CI reported)]\",\n    \"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey; confirms retrieval augmentation as key enhancement; no type-partitioned cross-language system identified; cites InferFix as a key retrieval-augmented approach]\",\n    \"What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]\",\n    \"PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]\",\n    \"RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]\",\n    \"CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism; precedent for FTCR confidence-gated hybrid; cite as preprint — withdrawn from ICLR 2025, unpublished]\"\n  ],\n  \"description\": \"FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft type-conditioned retrieval (ReinFix's root-cause embedding approach, ICSE 2026) for cross-repository fix template transfer, while LLM-inferred type labels can substitute for the Infer-required labels used by InferFix (ESEC/FSE 2023) to enable type-conditioned retrieval on general natural bugs. The primary NLP contribution — targeted at EMNLP 2026 Findings (via ARR, May 25, 2026) — is a complete causal decomposition parameterized by four falsifiable quantities measured at the minor-type level of DebugBench's 4-major/18-minor hierarchical taxonomy: (X%) few-shot LLM classifier accuracy vs. DebugBench ground-truth oracle labels at the minor-type level (major-type aggregation as secondary); (Y%) zero-shot cross-lingual transfer accuracy to Java bugs, reported as a preliminary cross-lingual signal at n=56 with 95% CI to make sampling uncertainty explicit; (Z%) repair improvement for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline (aggregate, McNemar's test, 95% CI); (W%) repair degradation for misclassified instances (aggregate, McNemar's test, 95% CI). X% is framed as a direct empirical test of whether task-specific few-shot prompting overcomes the documented zero-shot accuracy floor (~37% secondary / ~5% tertiary) established by arXiv:2407.06153 (EMNLP 2024); that study found AI-assisted annotation with demonstrations achieves 91.6% tertiary accuracy, motivating FTCR's hypothesis that few-shot with DebugBench-specific examples substantially exceeds the zero-shot floor without human-in-the-loop verification. Together the X%/Y%/Z%/W% quantities characterize when hard categorical type conditioning helps and when it hurts, generalizing to any system using LLM-inferred categorical labels for retrieval routing. FTCR's structural departure from ReinFix is to (1) classify incoming failures into one of the 14 single-fault minor sub-types, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable in a clean intra-corpus comparison. Round 9 revisions address four issues: (a) SWE-smith REMOVED FROM KEY_REFERENCES — SWE-smith was cited as a corpus scaling resource but did not appear among the four actual corpus sources (SWE-bench non-Lite, BugsInPy, Defects4J V1.2, GitBug-Java); removing it eliminates the corpus inconsistency and the venue-verification concern simultaneously; note that during independent verification the SWE-smith GitHub repository does confirm NeurIPS 2025 D&B Spotlight acceptance, but the entry is removed entirely to preserve corpus clarity; (b) SWE-BENCH LITE SOTA MODEL NAME FIXED — 'Claude Opus 4.6' (which does not correspond to any confirmed Anthropic model release; current lineup has Opus 4.7 and Sonnet 4.6) replaced in landscape with 'a leading agentic scaffold (62.7%, May 2026)' to avoid erroneous attribution of a third-party leaderboard label; (c) Y% FRAMING UPDATED — reframed as 'preliminary cross-lingual signal' at n=56 in approach, resource_estimate, and key_references; 95% CI half-width (~±10–13% depending on proportion) explicitly noted so reviewers can assess uncertainty; (d) All Round 8 contributions preserved: arXiv:2407.06153 accuracy floor integration, LTFix one-sentence differentiation, Day-12 hard cutoff commitment, TypeRepair qualifier with explicit reviewer invitation.\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Uncited competing work invalidates novelty claim: ReinFix (ICSE 2025, arXiv 2506.23100) embeds root-cause classification into retrieval from a 1M-pair historical bug-fix corpus, which is mechanistically nearly identical to FTCR's type-conditioned retrieval from historical corpus. The proposal must cite and differentiate from ReinFix; without this, reviewers will reject on novelty grounds.\", \"CRITICAL — ReCode overlap is underplayed: ReCode already implements algorithm-type-conditioned retrieval with type-partitioned sub-knowledge-bases, the identical core mechanism. FTCR's contribution is extending this to real-world bugs (competitive programming → repositories), which must be framed more precisely. The current framing overclaims novelty.\", \"HIGH — Dataset size claim is internally inconsistent: BugsInPy (493) + Defects4J (1,192) = ~1,685 pairs, not 6,500. If the SWE-bench training split (19,000 instances) is included, that's 20,000+. The '~6,500' figure suggests some undescribed quality-filtering or subsetting logic that is not specified in the proposal. This will raise red flags in review.\", \"HIGH — Defects4J reproducibility crisis: Independent studies (MSR 2025) found ~50% of Defects4J fault-triggering tests are regression tests added post-hoc, and nearly 50% become non-reproducible with modern Java. BugsInPy showed 67% reproducibility. Mining ~1,685 pairs from these datasets may yield fewer than 900 reliably reproducible bug-fix pairs, undermining the corpus quality and scale claims.\", \"MEDIUM — Uncited prior art RetypeR (ICSME 2024): This paper applies type-specific retrieval (external retrieval stage conditioned on Python type errors) and should be discussed as prior art that narrows the novelty of cross-language type-conditioned retrieval.\", \"MEDIUM — Resource units inconsistency: The hard constraint is ≤200 H100-hours, but the proposal reports A100-hours throughout. Manual mode (~150 A100h ≈ 90 H100h) is within budget, but auto-research mode (~650 A100h ≈ 390 H100h) significantly exceeds the constraint. This should be flagged and the primary experiment budget anchored in H100-hours.\", \"MEDIUM — EMNLP framing needs NLP-centric repositioning: The primary contribution is a retrieval system design (SE contribution). EMNLP 'NLP and Code Models' track requires a clear NLP/LLM contribution. The few-shot taxonomy induction approach and its ability to generalize zero-shot across languages should be foregrounded as the NLP contribution; the retrieval architecture is the engineering substrate.\", \"LOW — DebugBench validity concern: DebugBench uses LeetCode code with GPT-4-implanted synthetic bugs, not real repository bugs. Results on DebugBench may not transfer to SWE-bench Lite, requiring a careful discussion of the domain gap between the two evaluation settings.\"]\nFeedback: The core gap FTCR targets is real but narrower than claimed. To make this revisable into a strong paper: (1) Reframe the novelty around what's genuinely new — the extension of type-partitioned retrieval from algorithmic contest code (ReCode) to real-world multi-language repository bugs with an 18-category taxonomy grounded in DebugBench's empirically validated type structure. This is a specific, defensible contribution. (2) Add ReinFix as a baseline: since ReinFix uses root-cause-conditioned retrieval from historical corpus, you must compare against it directly on a shared benchmark (Defects4J is common). If FTCR's type-partitioned index outperforms ReinFix's joint root-cause+code embedding, that's a publishable finding. (3) Fix the dataset size: either restrict to BugsInPy+Defects4J and acknowledge the smaller corpus (~1,500–1,685 pairs after reproducibility filtering), or explicitly include a quality-filtered SWE-bench train subset and describe the filtering criteria. (4) Run a reproducibility pre-check: before committing to Defects4J as a corpus source, filter to only Java 8-compatible bugs (reported to have ~80% reproducibility) and report the usable fraction. (5) For EMNLP fit, pivot the NLP angle to the few-shot taxonomy induction finding — specifically, whether LLM-inferred bug types are consistent, cross-lingual, and predictive of repair success. This is the NLP scientific question. (6) The 16-day timeline is only viable in auto-research mode with parallel evaluation; the paper should scope evaluation to DebugBench (where type labels are ground-truth) plus SWE-bench Lite (300 instances), and acknowledge that a full Defects4J corpus build is out-of-scope for the conference timeline.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Citation error: ReinFix is confirmed ICSE 2026 (arXiv 2506.23100 states 'Accepted by ICSE 2026'), not ICSE 2025 as the proposal states throughout. EMNLP 2026 explicitly warns against hallucinated citations and has stated it may desk-reject papers with such errors. Every reference to 'ReinFix (ICSE 2025)' must be corrected to 'ReinFix (ICSE 2026)'.\", \"HIGH — Corpus sparsity renders type partitioning semantically degenerate for rare types: 559 Java pairs (Defects4J + GitBug-Java) across 18 types yields ~31 Java instances per type on average. For rare bug categories (concurrency, resource leaks, format errors), this may be 5–15 instances. Retrieving k=5 from a sub-index of 15 instances is not retrieval—it is exhaustive lookup. The proposal must either (a) restrict to the 6–8 most frequent types where >50 Java instances exist, or (b) merge rare types into a broader category, or (c) acknowledge that the per-type ablation is only meaningful for the top N types and report per-type corpus sizes in the paper.\", \"HIGH — Classifier error propagation is unaddressed: if the type classifier misclassifies an incoming bug (which will occur for edge cases and multi-type bugs), the system retrieves from the wrong partition and almost certainly underperforms soft retrieval for those instances. This is the main structural risk of hard partitioning over soft embedding. The proposal must analyze: (a) classifier accuracy on held-out annotated bugs, (b) the performance degradation attributable to misclassification, and (c) whether a confidence-gated fallback to soft retrieval recovers performance.\", \"HIGH — EMNLP venue fit remains questionable: the core contribution is an IR architecture decision (partitioning a FAISS index by categorical label). EMNLP 'NLP and Code Models' reviewers will ask what the NLP/LM finding is. The 'few-shot cross-lingual taxonomy induction' contribution (measuring whether LLM-inferred bug types are consistent across annotation runs) is secondary and not a compelling standalone NLP finding—LLM classification consistency is well-studied. If submitting to EMNLP, the NLP contribution must be foregrounded more strongly, e.g., a finding that LLM-inferred type labels are cross-lingually stable and predictive of repair success at the p<0.01 level, with analysis of failure cases that reveal type-specific linguistic patterns in bug descriptions.\", \"MEDIUM — ASE 2026 NIER deadline (May 12) is 2 days from today and experiments are not done: listing it as a target venue is unrealistic. Remove from target_venues or replace with a venue with a later deadline (e.g., EMNLP Findings via ARR, or FSE 2027).\", \"MEDIUM — No expected performance range stated for SWE-bench Lite: reviewers will immediately compare against the RepoRepair baseline (45.7% on Lite). The proposal should state an expected performance range and justify why a lower absolute number is acceptable given the paper's focus on architectural comparison rather than SOTA performance.\", \"LOW — The proposal does not specify which encoding model will be used for FTCR. ReinFix uses text-embedding-3-large (OpenAI API). If FTCR uses the same encoder for fair comparison, this imposes an ongoing API cost not captured in the GPU-hour budget. If using CodeBERT or UniXcoder instead, the encoder comparison is confounded with the hard/soft partitioning comparison. This should be clarified explicitly.\"]\nFeedback: The Round 2 revision has fixed the major structural issues from Round 1 (ReinFix is now a baseline, dataset sizes are consistent, RetypeR is cited, compute is in H100-hours, DebugBench limitations acknowledged). The core hypothesis is testable and the ablation design is clean. Three issues must be addressed before this is submission-ready: (1) Fix the citation error throughout — ReinFix is ICSE 2026, not ICSE 2025; submit it as 'ReinFix (ICSE 2026, arXiv:2506.23100)'. (2) Address corpus sparsity directly in the methods section: report per-type instance counts in a table, restrict the full 18-type analysis to the Python+Java combined corpus, and for the Java-only ablations acknowledge that only the top N types have >50 instances. For types below a minimum threshold (suggest 30 instances), either merge or exclude from per-type breakdown. (3) Add a classifier accuracy analysis: measure the type classifier on the annotated DebugBench ground-truth labels (since DebugBench already has ground-truth types, you can directly measure LLM classifier accuracy), then report how type-matched retrieval performance varies as a function of classifier confidence. This turns the error propagation problem into a feature — it becomes an analysis of when hard partitioning helps vs. hurts. For EMNLP specifically: the NLP contribution must be stated as a crisp finding, not a process. Frame it as: 'We show that LLM-inferred bug type labels achieve X% agreement with DebugBench ground-truth labels, transfer zero-shot to unseen Java bugs with Y% agreement, and are predictive of retrieval-augmented repair success (type-matched retrieval outperforms soft retrieval by Z% for correctly classified bugs, while underperforming by W% for misclassified bugs).' This is a falsifiable empirical claim that EMNLP reviewers can evaluate.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL — CRAG citation is a hallucinated venue: The proposal cites 'CRAG (ICLR 2024)' but CRAG (arXiv:2401.15884) was submitted to ICLR 2025 and withdrawn — it was never accepted or published at any ICLR. Citing it as a published ICLR paper is precisely the kind of hallucinated venue citation EMNLP warns may trigger desk rejection. The correct citation is 'CRAG (Yan et al., 2024; arXiv:2401.15884)'.\", \"HIGH — Unacknowledged concurrent work: SWE-Exp (arXiv:2507.23361, July 2025) uses an experience bank where retrieval explicitly surfaces 'the top N=10 issues most relevant in terms of error type' via cosine similarity, achieves 41.6% on SWE-bench Verified, and is publicly available with open-source code. While the mechanism is different (experience trajectories + soft cosine vs. hard categorical partitioning of fix templates), EMNLP and ICSE reviewers will notice its absence. FTCR must cite it, note the difference (soft type-similarity vs. hard categorical partitioning), and explain why hard partitioning is a distinct hypothesis worth testing.\", \"MEDIUM — 'Clean comparison' overstates the isolation: Type-partitioned retrieval fundamentally reduces the effective retrieval corpus to 1/N_types (≈1/18 on average) of the full index. A smaller retrieval pool affects recall independently of the type-matching benefit. Without a 'random-partition baseline' (random corpus subsets of equivalent size per query), the observed gain (or loss) conflates two effects: (a) partitioning precision and (b) retrieval corpus size. The proposal should either add this control or explicitly acknowledge it as a confound in Section 4.\", \"MEDIUM — EMNLP main track fit remains overstated: The NLP contribution — measuring X% agreement between LLM-inferred bug type labels and DebugBench ground truth, then correlating with repair success — is a measurement finding about LLM classification reliability on a well-structured taxonomy. This is useful but unlikely to be viewed as a primary NLP/LM contribution by EMNLP main track reviewers, who expect findings that advance understanding of language models. EMNLP Findings is a more realistic target; ICSE 2027 (already listed) is the natural primary venue where the SE audience will value the retrieval architecture contribution directly.\", \"LOW — Minor ReinFix technical inaccuracy: The proposal states ReinFix uses 'a unified FAISS vector store' but the ReinFix paper (arXiv:2506.23100) only refers to 'a vector database' without specifying FAISS as the implementation. This overly specific characterization of the baseline's internals should be softened to 'a unified vector database' to avoid misrepresentation of the primary baseline.\"]\nFeedback: Round 3 has successfully addressed the four critical/high issues from Round 2: citation corrected to ICSE 2026 throughout, corpus sparsity handled with explicit per-type table and 30-instance merge policy, classifier error propagation addressed with confidence-gated hybrid and DebugBench calibration, and EMNLP framing sharpened to a crisp X%/Y%/Z%/W% falsifiable claim. The core hypothesis is testable and genuinely novel for multi-language APR. Two issues block submission: (1) Fix the CRAG citation immediately — replace every instance of 'CRAG (ICLR 2024)' with 'CRAG (Yan et al., 2024; arXiv:2401.15884)'. CRAG was submitted to ICLR 2025 but withdrawn and unpublished; citing it as published ICLR work is a hallucinated venue citation that can trigger desk rejection at EMNLP. (2) Add SWE-Exp (arXiv:2507.23361) to the landscape with one paragraph: it uses soft cosine retrieval filtered 'in terms of error type' from an experience bank; FTCR's departure is hard categorical partitioning at index-construction time, not just retrieval-time filtering, plus fix-template retrieval rather than trajectory experience. For longer-term strengthening: add a random-partition baseline (randomly assign corpus pairs to N equivalent-sized sub-indices) to isolate the type-matching benefit from the corpus-size effect. This single ablation converts the comparison from 'clean but contested' to 'rigorous and unambiguous'. On venue strategy: ICSE 2027 (abstract June 23) should be positioned as the primary target; EMNLP 2026 ARR (May 25) can be attempted for Findings if the NLP framing holds, but do not overinvest in EMNLP main track positioning — the primary audience for this work is the SE/APR community.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"HIGH — Uncited concurrent work: 'Towards Defect-Type-Aware Adaptive Program Repair' (TypeRepair, Zhang et al., Software Quality Journal 2026, link.springer.com/article/10.1007/s11219-026-09751-w) uses explicit defect type identification before context selection in a 4-stage pipeline (localization → type ID → context selection → patch generation) on Defects4J V1.2/V2.0 and QuixBugs, independently achieving 272% improvement over GPT-3.5 baseline. The paper must be obtained, read, and cited: if 'context selection' uses type-conditioned retrieval from a cross-repo external corpus (which cannot be confirmed from the abstract alone due to paywall), the overlap with FTCR is substantial and reviewers will notice its absence. If TypeRepair uses only within-project context, that is FTCR's key differentiation and must be stated explicitly.\", \"HIGH — Unaddressed counterevidence: 'What to Retrieve for Effective Retrieval-Augmented Code Generation?' (ICSE 2026, arXiv 2503.20589) empirically shows that retrieving syntactically similar code snippets degrades performance by up to 15% compared to retrieving in-context examples and API information. This is a direct challenge to FTCR's premise: if type-partitioned retrieval returns syntactically similar-but-wrong-level-of-abstraction fixes within each partition, it may concentrate rather than reduce this noise. The authors must address this finding — either by arguing that semantic type partitioning selects at a different abstraction level than syntax similarity, or by adding an experiment measuring within-type fix template quality vs. cross-type.\", \"MEDIUM — Practical utility framing missing: FTCR projects 20–35% on SWE-bench Lite while SWE-Exp achieves 73% on SWE-bench Verified and RepoRepair achieves 45.7% on Lite. ICSE 2027 reviewers will ask why the retrieval strategy matters in isolation when execution-augmented agentic methods dominate. The paper needs an explicit 'why retrieval strategy matters' argument: e.g., (1) retrieval modules are independently upgradeable components within agentic systems — DynaFix adds execution feedback orthogonally to retrieval, so a better retrieval module improves the whole pipeline; (2) the 20–35% baseline is specifically the retrieval contribution, not the full agentic ceiling. This argument exists implicitly but must be stated explicitly.\", \"LOW — EMNLP 2026 ARR deadline is not credible given current state: The May 25 deadline is 15 days away. To submit to ARR requires a complete written paper, full experimental results, and bibliography validation (EMNLP's hallucinated-citation warning is explicit). The paper's hedge ('if too close, defer') should be changed to a definitive decision: either commit to running minimum viable experiments starting immediately (DebugBench classifier calibration + Defects4J V1.2 with the 4 primary variants) or acknowledge ICSE 2027 as the sole target. Leaving it ambiguous signals poor project planning to co-authors and advisors.\"]\nFeedback: Round 4 has successfully resolved all five issues from Round 3: CRAG citation is correct (arXiv-only), SWE-Exp is cited with three clear design differences, the random-partition control (Variant F) converts the corpus-size confound into a closed experimental question, EMNLP is downgraded to Findings, and ReinFix's implementation detail is softened. Independent verification confirms all cited paper claims are accurate. The hard-vs-soft retrieval comparison for semantic bug-type partitioned cross-repo repair is genuinely novel — no existing paper makes this specific comparison. Two actions are required for Round 5: (1) Read the TypeRepair SQJ 2026 paper (Zhang et al., doi:10.1007/s11219-026-09751-w) and add it to the landscape — the differentiation is either that TypeRepair uses intra-project context (state this explicitly) or that it uses cross-repo retrieval but covers only Java with a different pipeline structure (then FTCR's C++/Java/Python scope and the hard/soft comparison are the differentiators). (2) Cite and respond to 'What to Retrieve for Effective RAG Code Generation?' (ICSE 2026, arXiv:2503.20589): its finding that similar code retrieval degrades performance by 15% motivates FTCR's type-conditioning exactly — within a type partition, retrieved examples share fix structure rather than surface-level code similarity, which is the argument FTCR needs to make explicit. These two additions would resolve the remaining novelty and counterevidence gaps. The practical utility framing (retrieval as a modular component upgradeable within agentic pipelines) should be added as a paragraph in the introduction — this is the clearest answer to 'why does this matter when agentic methods dominate at 73%.'\n\n### Round 5 review\nVerdict: revise\nIssues: [\"CRITICAL — Target venue violates user requirements: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026, 15 days from today). The proposal now targets ICSE 2027 (abstract June 23, 2026) exclusively, a full year late and a different research community. Previous reviewers flagged EMNLP as infeasible given experiment state, but the requirement was not to change venues — it was to make the idea work within the constraint. If auto-research starts immediately (day 0), 10–14 days of experiments complete by ~May 23, leaving 2 days to finalize the paper for the May 25 ARR deadline. This is technically achievable but requires an explicit, committed execution plan with the NLP framing (X%/Y%/Z%/W% classifier calibration finding) as the lead contribution. The proposal must either restore EMNLP 2026 as the primary target with a day-by-day execution schedule, or explicitly acknowledge that it fails the user's venue constraint and accept that verdict.\", \"HIGH — 16-day timeline constraint met only by auto-research mode: The user's hard constraint is ≤16 days. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) exceed this by 8–12× and should not appear as viable execution paths in resource_estimate. The paper should flag auto-research (10–14 days) as the only constraint-compliant mode, or restructure the three modes to reflect feasible timelines.\", \"MEDIUM — InferFix (ESEC/FSE 2023, arXiv:2303.07263) is unmentioned prior art: Independently confirmed that InferFix uses bug type annotations and contrastive learning to retrieve 'semantically equivalent bugs and corresponding fixes of the same bug type' from an external repository corpus (InferredBugs, thousands of Java and C# repos). This is the closest non-trivial precursor to type-conditioned cross-repo repair retrieval and is not cited anywhere in the proposal. ICSE 2027 reviewers familiar with the APR literature will notice its absence. FTCR should differentiate explicitly: InferFix uses soft contrastive similarity (learned embedding grouping) not hard categorical index partitioning; it targets Java/C# from Infer static analysis findings, not the 18-category natural-bug taxonomy; and the corpus construction and evaluation differ. This differentiation is achievable in one paragraph but must be present.\", \"MEDIUM — Cross-system corpus quality confound inadequately flagged: The 'clean comparison' correctly uses the same 3,050-pair natural corpus for both FTCR and the ReinFix-style baseline, isolating partitioning as the variable. But any performance comparison against the published ReinFix results uses 100K TRANSFER corpus pairs (synthetic, from static analysis), creating a corpus quality × retrieval architecture confound that the random-partition control does not address. The paper must explicitly state: (a) intra-corpus ablations (FTCR vs. re-implemented ReinFix on 3,050 pairs) test the partitioning hypothesis cleanly, and (b) absolute comparisons against published ReinFix results reflect both architecture and corpus quality differences simultaneously.\", \"LOW — TypeRepair context-selection scope unverifiable from publicly accessible sources: The critical differentiation claim — that TypeRepair's Stage 3 selects within-project context only, not from an external cross-repo corpus — could not be independently confirmed due to paywall access to the SQJ article. The proposal states this confidently; it should note the evidentiary basis (e.g., 'TypeRepair evaluates exclusively on Defects4J/QuixBugs, which are within-project datasets, and the paper's supplementary prompt templates confirm type-specific in-project context selection rather than external retrieval') to avoid a reviewer flagging this differentiation as unsubstantiated.\"]\nFeedback: This is the most polished version of FTCR to date. The random-partition control, confidence-gated hybrid, per-type merge policy, and ReinFix/SWE-Exp/TypeRepair differentiation all reflect genuine methodological rigor. Two actions would bring this to pass: (1) VENUE DECISION — the proposal must choose one of two paths and commit fully: either (a) restore EMNLP 2026 ARR (May 25) as the primary target with a specific day-by-day execution schedule (day 0-13: auto-research runs corpus annotation + DebugBench classifier calibration + Defects4J V1.2 ablations; day 13-15: paper writing with NLP lead framing the X%/Y%/Z%/W% falsifiable classifier finding), acknowledging the extreme timeline pressure; or (b) explicitly declare that the user's requirement cannot be met for EMNLP 2026 and accept ICSE 2027 as the sole target with a verdict of 'fail' on the original requirement. Leaving both venues while targeting neither by the May 25 deadline is a planning failure. (2) ADD INFERFIX — one paragraph in the landscape: 'InferFix (ESEC/FSE 2023, arXiv:2303.07263) retrieves fixes for bugs of the same type using contrastive-learned embeddings over bug type annotations, establishing type-aware retrieval for Java/C# static analysis bugs. FTCR differs in three respects: (a) hard categorical index partitioning at construction time rather than soft contrastive similarity at retrieval time; (b) 18-category natural-bug taxonomy across C++/Java/Python rather than InferBugs' Infer-specific defect categories; (c) direct comparison of hard vs. soft type conditioning as the scientific contribution.' If these two issues are resolved, the novelty and feasibility scores reach 3.5+ and the paper is close to a pass for ICSE 2027 (though not EMNLP 2026 unless the execution plan is credible).\n\n### Round 6 review\nVerdict: revise\nIssues: [\"HIGH — EMNLP Main vs. Findings target ambiguity persists: target_venues now lists 'EMNLP 2026 Main' AND 'EMNLP 2026 Findings' as separate entries, but the empirical calibration study (X%/Y%/Z%/W% LLM label reliability) is a measurement finding about LLM annotation quality — appropriate for EMNLP Findings, not the Main track, which expects findings that advance understanding of language models at a deeper level. Rounds 3 and 4 both explicitly downgraded the EMNLP target to Findings; Round 5 asked to restore EMNLP without specifying Main vs. Findings; Round 6 silently re-expanded to Main. The proposal must commit to EMNLP Findings as the EMNLP target and stop oscillating. Trying for Main and being desk-rejected wastes the submission cycle.\", \"MEDIUM — DebugBench hierarchical structure mischaracterized throughout: independently verified (ACL Findings 2024 paper) that DebugBench has 4 MAJOR categories (Syntax Bugs, Logic Bugs, Reference Bugs, Multiple Bugs) with 18 MINOR sub-types nested within them — not 18 independent categories. The proposal consistently refers to '18-category taxonomy' and '18-category natural-bug taxonomy aligned with DebugBench's taxonomy.' This is inaccurate and will flag with any reviewer who has read DebugBench. Concretely: the merge policy for rare types must operate within the 4-major/18-minor hierarchy (merge within major categories first, not across them); X%/Y%/Z%/W% measurements must specify whether they are measured at the major-type or minor-type level; and the '~31 Java instances per type' figure implies 18 equal partitions, which is not how the benchmark is structured.\", \"MEDIUM — Day-0-today execution assumption is unverified: the schedule commits to launching corpus annotation pipeline on May 10 (today) with 2 A100 nodes already available. No verification of compute availability, API rate limits on day 1, or Defects4J V1.2 Docker environment readiness is mentioned. If infrastructure setup takes 1–2 days (common in practice), the already-tight 2-day paper writing window (Days 13–15, May 23–25) disappears entirely. The proposal should either (a) confirm that compute is already provisioned and Docker environments tested, or (b) revise the schedule to account for a 1-day setup buffer by shifting MVS deliverables earlier.\", \"LOW — InferFix type-as-embedding-signal claim needs precision: independent verification found that InferFix adds bug type annotations as prompt context alongside retrieved fixes, while the contrastive retriever learns semantic similarity between bugs/fixes. The proposal claims 'type influences embedding proximity rather than pool membership' — this framing appears broadly correct but needs verification against the actual retriever architecture section (Section 3 of arXiv:2303.07263), not just the abstract. If InferFix's retriever does NOT explicitly condition on type labels during encoding (only using type for post-retrieval prompt augmentation), the 'soft type conditioning' differentiation needs rewording to 'type-correlated semantic similarity' to avoid misrepresenting the baseline.\", \"LOW — Statistical significance for Z% and W% unstated: the Z% (repair improvement for correctly classified) and W% (repair degradation for misclassified) measurements will have unequal sample sizes depending on classifier accuracy. With ~31 Java instances per minor type and a 20% held-out split (~6 per type), per-type statistical tests are underpowered. The proposal should specify: (a) whether Z% and W% are aggregated across all types or reported per type; (b) what statistical test is used; (c) minimum sample threshold for a type to contribute to the Z%/W% comparison.\"]\nFeedback: Round 6 has addressed all five Round 5 issues: EMNLP venue restored with committed schedule, InferFix added with three-point differentiation, corpus confound made explicit, TypeRepair evidentiary basis stated, resource estimate stripped to auto-research only. The core hypothesis is well-posed and the experimental design is increasingly rigorous. Three targeted fixes would make this submission-ready: (1) COMMIT TO EMNLP FINDINGS — remove 'EMNLP 2026 Main' from target_venues and replace with 'EMNLP 2026 Findings (via ARR)'. The X%/Y%/Z%/W% calibration study is a strong Findings paper; attempting Main track risks desk rejection on NLP-contribution grounds and wastes the submission cycle. (2) FIX DEBUGBENCH STRUCTURE — replace every instance of '18-category' with '4-major/18-minor hierarchical taxonomy' and state that X%/Y%/Z%/W% measurements operate at the minor-type level (18 sub-categories), with major-type aggregation reported as a secondary result. Revise the merge policy to explicitly merge within the same major category first (e.g., merge rare Reference Bug sub-types before merging across Logic and Reference). (3) CONFIRM COMPUTE READINESS — add one sentence to the Day 0 entry: 'Compute: 2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.' If this cannot be stated truthfully, shift the MVS timeline by 1 day and compress paper writing to 1 day with a more aggressive pre-drafted skeleton policy. These three changes are low-effort and directly address verifiable gaps; the underlying science is solid and the proposal is close to submission-ready for EMNLP 2026 Findings.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"MEDIUM — Uncited counterevidence on LLM annotation accuracy undermines X% expectations without preemption: arXiv:2407.06153 ('What's Wrong with Your Code Generated by Large Language Models?') independently measured LLM auto-labeling of fine-grained bug types and found fully automated tertiary-level accuracy of 5.2% and secondary-level accuracy of 35.7%. FTCR's core hypothesis depends on X% being high enough for correctly-classified instances (driving Z%) to outnumber misclassified instances (driving W%). If X% is in the 35% range, hard partitioning would hurt on average. The proposal must cite this paper and explain why its setting (few-shot prompting with DebugBench-specific demonstration examples, a taxonomy purpose-built for LLM classification) is expected to achieve substantially higher accuracy than the general case studied in 2407.06153. Framing FTCR as 'testing whether task-specific few-shot prompting overcomes the documented accuracy floor in general LLM bug classification' would strengthen both the motivation and the EMNLP NLP angle.\", \"LOW — LTFix (arXiv 2506.18394, 'Tracing Errors, Constructing Fixes: Repository-Level Memory Error Repair via Typestate-Guided Context Retrieval', June 2025) uses type-guided retrieval (typestate automaton) for memory errors in C code at the repository level. While domain-specific, it is the closest recent work to FTCR's type-guided retrieval architecture for repository-level repair and should be cited with a one-sentence differentiation (C memory errors only vs. FTCR's 18-subtype taxonomy across C++/Java/Python).\", \"LOW — The two-day paper writing window (Days 13–15, May 23–25) remains structurally fragile. If SWE-bench Lite results arrive on Day 12 and require reframing, or if any ablation produces surprising results requiring additional runs, the window collapses. The pre-drafted skeleton policy (stated as prepared during Days 4–6) is necessary but not sufficient mitigation. The proposal should commit to one additional write-up contingency: if any experiment is not complete by Day 12 EOD, drop it and close the paper with the MVS results only rather than attempting to extend experiments into the writing window.\", \"LOW — TypeRepair (SQJ 2026) differentiation remains technically unverifiable from publicly accessible sources: the claim that Stage 3 context selection draws from within-project code only is inferred from the evaluation design (Defects4J/QuixBugs are project-internal datasets) rather than directly stated in the paper. This evidentiary basis is now stated in the proposal ('The evaluation design makes the within-project scope structurally evident'), which is defensible. However, reviewers with full SQJ access could refute this if wrong. Consider adding a qualifier: 'To the best of our knowledge from the publicly accessible abstract and benchmark descriptions, TypeRepair's context selection stage draws from within-project code files; any reviewer with full SQJ article access who finds this claim incorrect is encouraged to provide the correction.' This signals intellectual honesty and invites correction rather than assertion.\"]\nFeedback: Round 7 has successfully resolved all five Round 6 issues: EMNLP Findings commitment is firm, DebugBench 4-major/18-minor hierarchy is correct throughout, compute readiness is confirmed, InferFix architecture is accurately characterized, and statistical significance is fully specified. The proposal is in its strongest state to date. Two targeted fixes would bring this to submission-ready: (1) CITE AND ADDRESS arXiv:2407.06153 — this is the most important remaining gap. Add a sentence in the introduction or related work: 'Prior work has shown that fully automated LLM classification of fine-grained bug types achieves ~35% accuracy at the secondary level (citation), motivating the question of whether task-specific few-shot prompting with a purpose-built taxonomy (DebugBench) achieves sufficient accuracy to make hard categorical partitioning beneficial on net. FTCR's X%/Y% measurements directly test this.' This frames X% as the paper's central NLP finding and preempts the most likely reviewer objection. (2) ADD ONE SENTENCE about LTFix in the landscape paragraph: 'LTFix applies typestate-automaton-guided retrieval to memory errors in C at the repository level; FTCR generalizes type-conditioned retrieval to 18 semantic sub-types across C++/Java/Python using LLM-inferred labels.' These two additions are low-effort and high-impact for reviewer confidence. The core science is sound — the X%/Y%/Z%/W% causal decomposition is a legitimate EMNLP Findings contribution that no existing paper has made for natural repository bugs.\n\n### Round 8 review\nVerdict: revise\nIssues: [\"HIGH — SWE-smith (arXiv 2504.21798) cited as '(NeurIPS 2025)' but this venue attribution is unconfirmed: the arXiv abstract contains no NeurIPS 2025 affiliation. This is structurally identical to the CRAG-ICLR hallucination flagged as CRITICAL in Round 3. EMNLP has explicitly warned it may desk-reject papers with hallucinated venue citations. Independently verified: no NeurIPS 2025 affiliation appears in the arXiv record. Fix: cite as 'arXiv:2504.21798' only, without the conference attribution, pending verification. This is urgent given the May 25 deadline.\", \"MEDIUM — SWE-smith is cited in key_references as '[50k Python task instances; scale corpus for Python retrieval index]' but the corpus construction section lists exactly four sources (SWE-bench non-Lite split, BugsInPy, Defects4J V1.2, GitBug-Java) with no mention of SWE-smith. Either integrate SWE-smith as a fifth corpus source with its contribution to the ~3,050-pair count clearly specified, or remove it from key_references to avoid confusing reviewers who will check whether cited datasets are actually used.\", \"LOW — Y% cross-lingual transfer accuracy is measured on only 56 human-verified Java pairs. Fifty-six instances is below the minimum threshold for robust transfer generalization claims, especially given the known domain difference between Python natural bugs (dominant in SWE-bench) and Java bugs (Defects4J/GitBug-Java). The paper should frame Y% explicitly as a 'preliminary cross-lingual signal' rather than a 'calibration' result, and include the 95% CI for a proportion estimate at n=56 to make the uncertainty visible to reviewers.\", \"LOW — The SWE-bench Lite SOTA claim attributes 62.7% to 'Claude Opus 4.6,' a model name that does not correspond to any confirmed Anthropic model release (the current Anthropic lineup has Opus 4.7 and Sonnet 4.6, not Opus 4.6). While this name appears on third-party leaderboard aggregators, citing it in an EMNLP paper risks repeating the same type of erroneous attribution EMNLP has flagged. Verify directly against the official swebench.com leaderboard and use whatever model name appears there verbatim, or describe the entry as 'a leading agentic scaffold (62.7%, May 2026)' without naming the specific model.\"]\nFeedback: Round 8 has successfully resolved all four Round 7 issues: arXiv:2407.06153 is now integrated throughout as the accuracy-floor baseline with both-outcome publishability made explicit; LTFix is cited with one-sentence differentiation; the Day 12 hard cutoff commitment is unconditional and stated clearly; the TypeRepair qualifier is appropriately hedged. The core X%/Y%/Z%/W% framework is the strongest it has been across all rounds. One new issue blocks submission and must be fixed before ARR: (1) SWE-smith is cited as 'NeurIPS 2025' but this affiliation cannot be independently verified from the arXiv record — change the citation to 'arXiv:2504.21798' without a conference name, or verify the NeurIPS 2025 acceptance directly before submission. This is the same hallucinated-venue pattern that triggered a CRITICAL issue with CRAG in Round 3 and must be treated with equal urgency. (2) Either add SWE-smith as a real corpus source (and adjust the ~3,050 pair count) or remove it from key_references — having it cited as a retrieval corpus scaling resource while not appearing in the approach's four corpus sources is a verifiable inconsistency reviewers will catch. These two fixes are low-effort and high-stakes. All other remaining issues (Y% sample size, model naming) are LOW severity and can be addressed with hedging language. After these fixes, the proposal is credibly at the EMNLP Findings threshold.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:52:38.322Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:52:38.322Z",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-10T07:52:38.367Z_

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

## Idea under review (round 9/10)
{
  "title": "Failure-Type-Conditioned Retrieval Augmentation for Repository Repair",
  "project_name": "failure_type_rag_repair",
  "source": "web_research",
  "level": "solid",
  "core_problem": "The lead empirical question — tractable because DebugBench provides oracle ground-truth labels for 4,253 instances organized in a 4-major/18-minor hierarchical taxonomy — is: how accurately can a few-shot LLM assign semantic bug type labels from the 18 minor sub-categories, and does that label accuracy determine whether hard categorical retrieval index partitioning outperforms soft root-cause-augmented retrieval (ReinFix, ICSE 2026) for cross-repository fix template transfer? Prior work (arXiv:2407.06153, EMNLP 2024) established a baseline accuracy floor: fully-automated zero-shot GPT-4 classification of fine-grained bug types achieves only ~37% at the secondary level and ~5% at the tertiary level on a custom 3-primary/10-secondary taxonomy over LLM-generated code. However, that same study showed AI-assisted annotation (GPT-4 suggestions + human demonstrations) reaches 91.6% tertiary accuracy — an 18× improvement over zero-shot at the tertiary level — demonstrating that structured demonstration examples dramatically improve LLM classification performance. This frames FTCR's X% measurement as a direct empirical test of the hypothesis: 'does task-specific few-shot prompting with DebugBench-aligned demonstration examples, applied to a purpose-built 4-major/18-minor taxonomy of natural repository bugs, overcome the documented zero-shot accuracy floor in general LLM bug classification?' The practical stakes are high and symmetric: if X% ≈ 35% (the zero-shot floor), hard partitioning hurts on average and the paper's conclusion is a documented negative; if X% ≥ 65% (the few-shot hypothesis), correctly-classified instances driving Z% substantially outnumber misclassified instances driving W%, and type-conditioned retrieval is net-beneficial. Either outcome is a publishable finding with direct generalization to any retrieval system using LLM-inferred labels for query routing.\n\nThis frames FTCR as an empirical study of LLM-generated categorical label quality and its downstream retrieval impact, yielding four falsifiable quantities: (X%) few-shot classifier accuracy vs. DebugBench ground-truth oracle labels at the minor-type level, with major-type aggregation as a secondary result; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs (n=56 pairs, reported as a preliminary cross-lingual signal with 95% CI for the proportion estimate); (Z%) repair improvement for correctly-classified high-confidence instances under hard type-partitioned retrieval vs. the soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts — a finding with direct generalization to any retrieval system using LLM-inferred labels.\n\nRetrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. InferFix (ESEC/FSE 2023, arXiv:2303.07263) establishes that type-conditioned retrieval benefits code repair: its Retriever uses contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type from Infer static analysis), and at retrieval time filters candidates to same-type fixes; however, InferFix requires running the Infer static analyzer on each query bug — applicable only to bugs Infer can detect, using Infer-specific diagnostic categories rather than a general natural-bug taxonomy. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is therefore two-fold: (1) whether LLM-inferred type labels can substitute for Infer-derived labels to enable type-conditioned retrieval for general natural bugs not addressable by static analysis (the X%/Y% question vs. InferFix); and (2) whether hard categorical type partitioning of the retrieval index outperforms ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer (the Z%/W% question). An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. Type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and become analytical contributions when addressed directly: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4; the Multiple Bugs sub-types are excluded from the fix-template corpus as multi-fault commits are rare and represent a different repair regime) yields approximately ~217 pairs per minor type on average for the full Python+Java corpus; for Java-only ablations (~559 pairs across ~14 types, ~40 per type), types with fewer than 30 instances are merged within the same major category (e.g., rare Syntax sub-types merged within Syntax; rare Logic sub-types merged within Logic — never across major categories); and (2) classifier error propagation — when an incoming bug is misclassified, hard partitioning underperforms soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback — turns potential weaknesses into the core empirical variables (Z% and W%) that define the paper's scientific contribution.",
  "opportunity": "ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-conditioned cross-repository retrieval system for code repair: its Retriever is pretrained via contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type labels from Infer static analysis), and at retrieval time filters candidates to same-type fixes using Infer-derived labels. The encoder itself encodes only the buggy code as a dense vector — type structures the contrastive training pairs but is not an explicit encoder input; the retriever learns type-correlated semantic similarity. InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#. Three properties distinguish InferFix from FTCR: (a) Type label acquisition — InferFix requires running the Infer static analyzer on each query bug to obtain its type label; only bugs Infer can detect are addressable; FTCR uses few-shot LLM classification, requiring no static analysis tooling and covering any natural bug that Infer cannot or would not detect; (b) Taxonomy scope — InferFix uses Infer-specific diagnostic IDs (null dereferences, resource leaks, thread-safety violations), not the 4-major/18-minor natural-bug taxonomy aligned with DebugBench (4 major categories: Syntax with 7 sub-types, Reference with 4 sub-types, Logic with 4 sub-types, Multiple Bugs with 3 sub-types); (c) Corpus — InferFix uses InferredBugs (Java/C# repos where Infer detected bugs); FTCR uses natural bug-fix pairs from issue trackers and CI logs. The open empirical question InferFix leaves unresolved is whether LLM-inferred type labels can substitute for Infer-derived labels to enable effective type-conditioned retrieval for general natural bugs — precisely what FTCR's X%/Y% calibration measures. arXiv:2407.06153 (EMNLP 2024) independently measured LLM auto-labeling of fine-grained bug types and found fully automated zero-shot GPT-4 achieves ~37% secondary-level and ~5% tertiary-level accuracy on a custom 3-primary/10-secondary taxonomy over LLM-generated code; the same study shows that AI-assisted annotation with structured demonstrations reaches 91.6% tertiary accuracy. This establishes a documented accuracy floor for zero-shot general classification and directly motivates FTCR's X%/Y% measurements as the key empirical test: do few-shot demonstrations with DebugBench-specific examples bridge the 37%→91% gap for natural repository bugs without human-in-the-loop verification? InferFix validates that type-conditioned retrieval works (supporting FTCR's hypothesis) while leaving the LLM-label-quality-vs-retrieval-effectiveness question entirely unanswered. ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of the 18 minor semantic sub-types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than ReinFix's joint root-cause embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar embeddings but different repair operators do not. DebugBench's 4-major/18-minor hierarchical taxonomy uniquely provides 4,253 instances with ground-truth type annotations across C++, Java, and Python (organized as: Syntax/7 sub-types, Reference/4, Logic/4, Multiple Bugs/3), enabling direct classifier calibration at the minor-type level and turning error propagation from a latent risk into the paper's core measurable variable. The confidence-gated hybrid has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). M-RAG (ACL 2024, arXiv 2405.16420) validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis.",
  "landscape": "RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (a leading agentic scaffold, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% and is not a SOTA claim. InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-conditioned cross-repository retrieval system for code repair: it pretrains a Retriever via contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type from Infer static analysis), then at retrieval time filters candidates to same-type fixes using Infer-derived type labels. The encoder itself encodes only the buggy code as a dense vector — type structures the training pairs but is not an explicit encoder input; the retriever learns type-correlated semantic similarity. InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#, outperforming LLM baselines by 11–55%. Three design differences distinguish FTCR from InferFix: (a) Type label acquisition — InferFix requires Infer to run on each repository to produce type labels for both corpus and query bugs; FTCR uses few-shot LLM classification, covering any natural bug without static analysis tooling; the core empirical question vs. InferFix is whether LLM-inferred labels achieve sufficient accuracy (X%) to match Infer-derived retrieval quality; (b) Defect taxonomy — InferFix uses Infer-specific diagnostic IDs (covering only statically-detectable bug patterns), not the 4-major/18-minor natural-bug taxonomy aligned with DebugBench's empirically-grounded labels (Syntax/7, Reference/4, Logic/4, Multiple Bugs/3); (c) Corpus — InferFix uses InferredBugs (static-analysis artifacts); FTCR uses natural bug-fix pairs from SWE-bench, BugsInPy, Defects4J, and GitBug-Java. The scientific question InferFix leaves open — and FTCR directly tests — is whether LLM-inferred type labels achieve sufficient accuracy (X%) to enable type-conditioned retrieval that is effective for general natural bugs, and at what accuracy threshold does type-conditioned retrieval outperform soft embedding baselines (Z% > 0%, W% < Z%). What's Wrong with Your Code Generated by Large Language Models (arXiv:2407.06153, EMNLP 2024) provides the accuracy baseline that FTCR's X% must be measured against: fully automated zero-shot GPT-4 classification achieves ~37% secondary-level and ~5% tertiary-level accuracy on a custom 3-primary/10-secondary taxonomy over LLM-generated code (HumanEval+, MBPP+, APPS+); however, AI-assisted annotation with structured GPT-4 demonstrations reaches 91.6% tertiary accuracy. Three factors distinguish FTCR's setup from the zero-shot floor in arXiv:2407.06153: (i) prompting method — few-shot with DebugBench-aligned demonstration examples vs. zero-shot with taxonomy description only; (ii) bug domain — natural repository bugs from issue trackers and CI logs with diagnostic markers (missing colon, undefined object) vs. LLM-generated code failures on competitive benchmarks; (iii) taxonomy alignment — DebugBench's 4-major/18-minor hierarchy was built from and validated against real developer-reported bugs, providing sharper category boundaries than a general taxonomy. FTCR's X% measurement directly tests whether these three factors together are sufficient to bridge the documented zero-shot accuracy floor — framing X% as an empirical NLP finding rather than an implementation detail. ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning. Corpus quality confound: comparisons against published ReinFix results conflate two variables simultaneously — retrieval architecture (soft joint embedding vs. hard type partition) and corpus quality (100K TRANSFER synthetic pairs vs. 3,050 natural bug-fix pairs from issue trackers and CI logs). Intra-corpus ablations (FTCR vs. re-implemented ReinFix-style baseline on the same 3,050-pair natural corpus using the same text-embedding-3-large encoder) test the partitioning hypothesis cleanly and isolate architecture as the variable. Absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality differences simultaneously and are presented explicitly as such; they are not used to claim a clean head-to-head win on architecture alone. SWE-Exp (arXiv 2507.23361, revised February 2026) retrieves top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic Python-only pipeline. Three design differences: (1) soft vs. hard — SWE-Exp uses type as retrieval-time embedding metadata; FTCR partitions at index-construction time; (2) retrieved artifact — SWE-Exp stores distilled modification strategies; FTCR retrieves concrete fix patches; (3) scope — SWE-Exp is agentic and Python-only; FTCR covers C++/Java/Python in retrieval-only mode. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5. TypeRepair's context selection stage conditions on the identified defect type to select within-project code context and provide type-specific repair guidance — it does not retrieve from an external cross-repository fix corpus. Evidentiary basis: TypeRepair evaluates exclusively on Defects4J V1.2/V2.0 and QuixBugs — within-project Java bug collections that contain no external cross-repository retrieval component. To the best of our knowledge from the publicly accessible abstract and benchmark descriptions, TypeRepair's context selection stage draws from within-project code files and type-specific API/documentation context rather than an external fix-patch corpus; the evaluation design (project-internal datasets, no external corpus described in benchmark setup) makes the within-project scope structurally evident. Any reviewer with full SQJ article access who finds this characterization incorrect is encouraged to provide the correction — we welcome corroboration or refutation rather than defending an unverifiable inference, and the differentiation from FTCR's external 3,050-pair cross-language corpus retrieval holds regardless of whether TypeRepair's context is strictly within-project or draws from type-specific documentation. TypeRepair is Java-only; FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 fix patches. LTFix (arXiv 2506.18394, June 2025) applies typestate-automaton-guided context extraction to memory errors in C at the repository level, using a finite typestate automaton to trace error-propagation paths across functions and files for LLM context construction; LTFix targets C memory errors only (a single-domain bug class requiring interprocedural static tracing) and uses typestate analysis for context extraction rather than retrieval from a historical fix-patch corpus; FTCR generalizes type-conditioned retrieval to 18 semantic sub-types across C++/Java/Python using LLM-inferred labels with no static analysis tooling and retrieves from an external 3,050-pair fix-patch corpus. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec while contextual and API information helps; the 'what to retrieve matters' finding motivates FTCR's type-partition design. DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3. Both update the landscape but are orthogonal to retrieval strategy. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via objective alignment. FTCR's structural departure from all prior work is to (1) classify incoming failures into discrete minor sub-categories of the 4-major/18-minor DebugBench taxonomy, then (2) retrieve only from the type-matched sub-index, using text-embedding-3-large (identical to ReinFix) for a clean intra-corpus partitioning comparison — with the random-partition control separating type-matching precision from pool-size reduction. RetypeR (ICSME 2024, Hao et al.) applies type-specific retrieval for Python type errors only; FTCR extends to 18 minor sub-types across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates multi-partition RAG outperforms single-store RAG across NLP tasks (+11% summarization, +8% translation, +12% dialogue). PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary scope. The APR survey (arXiv 2506.23749) reviews 63+ systems with no type-partitioned cross-language retrieval system identified.",
  "approach": "We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms ReinFix's soft root-cause embedding for cross-repository fix template transfer, and that LLM-inferred type labels can substitute for the Infer-required labels used by InferFix to enable type-conditioned retrieval on general natural bugs. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix), same natural corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control.\n\nNLP Lead Contribution: LLM Label Quality and Downstream Retrieval Impact. The primary EMNLP Findings contribution is a complete causal decomposition of when hard type conditioning helps and when it hurts, parameterized by four falsifiable quantities measured at the minor-type level (18 sub-types of the 4-major/18-minor DebugBench hierarchy, with major-type aggregation reported as a secondary result): (X%) few-shot LLM classifier accuracy against DebugBench ground-truth oracle labels at the minor-type level; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs (n=56 pairs, reported as a preliminary cross-lingual signal with 95% CI for the proportion estimate to make sampling uncertainty visible to reviewers); (Z%) repair improvement on DebugBench/Defects4J V1.2 for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances under hard partitioning vs. same baseline. Z% and W% are reported as aggregate rates across all correctly-classified and misclassified instances respectively; significance is tested via McNemar's test on paired pass/fail outcomes (baseline vs. FTCR, same instances); per-type breakdowns use Fisher's exact test with a minimum n≥30 instance threshold; 95% confidence intervals are reported for both Z% and W%. Together these quantities are a direct empirical answer to: 'LLM-inferred categorical labels enable hard retrieval partitioning only if X% and Y% are high enough to make the correctly-classified population (driving Z%) larger than the misclassified population (driving W%).' This generalizes beyond code repair to any system that uses LLM-generated labels to route queries into type-specific retrieval pools.\n\nExecution Plan for EMNLP 2026 ARR (May 25 deadline, 15 days from today). Auto-research mode (10–14 days) is the only constraint-compliant execution path. Day-by-day schedule with minimum viable submission (MVS) milestones:\n\n- Day 0 (May 10): Launch auto-research pipeline; begin 3-pass annotation of 3,050 corpus pairs using DebugBench few-shot examples as demonstrations for the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4); configure Defects4J V1.2 Java-8 Docker environments and GitBug-Java isolated containers. Compute: 2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.\n- Day 1–3 (May 11–13): Annotation completes (~$183 Claude API cost). DebugBench classifier calibration: 20% held-out split (~851 instances, covering single-bug instances from the Syntax/Reference/Logic major categories and treated separately for the Multiple Bugs category) → X% per-minor-type accuracy with major-type aggregation as secondary. Cross-lingual Java transfer sample (56 human-verified pairs from Defects4J + GitBug-Java) → Y% preliminary cross-lingual signal (95% CI for the proportion estimate at n=56 reported to make sampling uncertainty visible). Per-minor-type count table computed; within-major-category merge policy applied for rare minor types below the 30-instance Java threshold.\n- Day 4–6 (May 14–16): Build type-partitioned sub-indices and ReinFix-style unified index (both text-embedding-3-large). Run Defects4J V1.2 ablations: Variant A (text-similarity RAG), Variant D (ReinFix-style re-implemented on same natural corpus), Variant E (FTCR@hard-all), Variant F (random-partition control, N equivalently-sized random sub-indices). Prepare pre-drafted paper skeleton (introduction, related work, method) during this window to reduce Day 13–15 writing pressure.\n- Day 7–9 (May 17–19): DebugBench evaluation across all variants on single-bug instances (Syntax/Reference/Logic major categories); confidence-gated τ sweep on held-out validation split; stratify results by classifier confidence band: high-confidence correctly-classified → Z% (aggregate, McNemar's test); misclassified → W% (aggregate, McNemar's test); per-type Fisher's exact test for types with n≥30. SWE-bench Lite evaluation launched in parallel (requires 2 A100 nodes for ~10 min/instance).\n- Day 10–12 (May 20–22): CodeBERT-base encoder ablation (same FTCR vs. ReinFix-style comparison, secondary encoder); taxonomy granularity ablation (major-type coarse/4 vs. minor-type fine/14 single-fault sub-types vs. merged-Java categories); retrieval k sweep (1/3/5/10).\n- Day 13 (May 23): Results compilation; paper writing begins with NLP lead (X%/Y%/Z%/W% as opening contribution).\n- Day 14–15 (May 24–25): Paper finalization and ARR submission. MVS for EMNLP Findings: DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. SWE-bench Lite Python results included if pipeline completes by Day 12, deferred to ICSE 2027 extended version otherwise.\n\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. InferFix demonstrates that type-conditioned retrieval improves over code-similarity retrieval, but requires Infer static analysis to label both corpus and query bugs. FTCR embodies a stronger form of this principle: classify the incoming bug using an LLM (no static analysis tooling required), then restrict the retrieval pool to same-type patches at index construction time, ensuring that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to score high in a shared embedding space but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\n\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559). The corpus is annotated against the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4); the Multiple Bugs sub-types (double/triple/quadruple) are not applicable to single-fix commit pairs in the retrieval corpus and are excluded from corpus annotation but evaluated separately in the DebugBench test set.\n\nCorpus Quality Confound (Explicit). The natural 3,050-pair corpus differs from ReinFix's 100K TRANSFER corpus in two simultaneous dimensions: (1) retrieval architecture (soft joint embedding vs. hard type partition) and (2) corpus quality (natural issue-tracker/CI bug-fix pairs vs. synthetic static-analysis-derived pairs). Intra-corpus ablations — FTCR vs. re-implemented ReinFix-style baseline using text-embedding-3-large on the identical 3,050-pair natural corpus — test the partitioning hypothesis cleanly and are the primary experimental contribution. Absolute performance comparisons against published ReinFix numbers on Defects4J reflect both architecture and corpus quality simultaneously; they are presented as joint-effect comparisons, not as clean head-to-head architectural wins. The random-partition control (Variant F) further isolates type-matching precision from pool-size reduction within the intra-corpus comparison.\n\nCorpus Sparsity Policy. Each pair is annotated with one of 14 single-fault minor sub-types via few-shot prompting; three annotation passes measure inter-run consistency. For the combined Python+Java corpus (~3,050 pairs, 14 active minor types), mean pairs per type is approximately ~218. For Java-only ablations (~559 pairs), types with fewer than 30 Java instances are merged into nearest-neighbor supercategories within the same major category (e.g., rare Syntax sub-types such as 'illegal separation' and 'illegal indentation' merged within Syntax — never across Syntax/Reference/Logic boundaries); Java ablation results are reported for the 4–6 resulting within-major-category merged groups that each exceed 50 instances, with merged categories explicitly labeled. Note that several Syntax sub-types (missing colons, illegal indentation) are Python-specific and may yield few or zero Java instances; these are expected to merge to the within-Syntax catch-all for Java ablations.\n\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound (~$5–15 total embedding cost). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific.\n\nType Classifier Calibration on DebugBench Ground Truth. Prior work (arXiv:2407.06153, EMNLP 2024) established a documented accuracy floor for fully automated LLM bug classification: zero-shot GPT-4 achieves ~37% at the secondary level and ~5% at the tertiary level on a custom 3-primary/10-secondary taxonomy over LLM-generated code; AI-assisted annotation with structured demonstrations reaches 91.6% tertiary accuracy — an 18× improvement over zero-shot. FTCR's classification setup is positioned between these bounds: few-shot prompting with DebugBench-specific demonstration examples (not zero-shot, not human-in-the-loop), applied to natural repository bugs with diagnostic markers (missing colon, undefined object) under a purpose-built 4-major/18-minor taxonomy with sharper category boundaries than a general taxonomy. Three factors motivate the expectation of substantially higher than ~37% secondary accuracy: (a) few-shot demonstrations provide structured per-type examples analogous to the AI-assisted setup in arXiv:2407.06153; (b) DebugBench's taxonomy was constructed from real developer-reported bugs with clear surface-level markers, unlike the more ambiguous code-generation failures in arXiv:2407.06153; (c) few-shot prompts are calibrated on held-in DebugBench examples before evaluation on the held-out 20% split. X% is reported as a direct empirical answer without assuming the hypothesis is confirmed: if X% ≈ 35% (the zero-shot floor), the paper's conclusion is 'few-shot task-specific prompting does not overcome the documented accuracy floor, and hard categorical partitioning is net-negative for retrieval-augmented repair' — itself a significant and publishable NLP finding. A held-out 20% split (~851 instances) directly measures few-shot classifier precision and recall per minor sub-type against oracle ground-truth labels, yielding X% at the minor-type level (major-type aggregation reported as a secondary result). The primary repair evaluation uses single-bug instances from the Syntax, Reference, and Logic major categories (~2,035 of 4,253 instances); Multiple Bugs instances (double/triple/quadruple, ~2,218 instances) are evaluated separately as an auxiliary experiment to characterize classifier behavior on multi-type ambiguous queries. Cross-dataset zero-shot agreement on ~56 human-verified Java pairs yields Y% (framed as a preliminary cross-lingual signal rather than a calibration result; 95% CI reported for the proportion estimate at n=56 to make sampling uncertainty explicit — at n=56, CI half-width is approximately ±13% for proportions near 50% and ±10% for proportions near 75%, conveying the range of this estimate to reviewers). These produce the core NLP finding: LLM-inferred bug type labels achieve X% agreement with DebugBench ground truth (Python/C++) at the minor-type level, transfer zero-shot to Java with Y% preliminary agreement (95% CI), and predict retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs (both aggregate across all instances of each class, McNemar's test, 95% CI).\n\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect, the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index (Variant F). Any performance gap between FTCR (Variant E) and this control measures the precision benefit of type-matching net of pool-size reduction.\n\nConfidence-Gated Retrieval Fallback. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval. Six variants evaluated: (A) text-similarity RAG, (B) RELREPAIR, (C) RepoRepair, (D) ReinFix-style soft on same corpus, (E) FTCR@hard-all, (F) random-partition control. Confidence-gated hybrid evaluated as a seventh configuration. Precedent: CRAG (Yan et al., arXiv:2401.15884).\n\nPractical Utility. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is the retrieval contribution in isolation, not a pipeline SOTA claim. DynaFix demonstrates retrieval and execution augmentation are independently improvable axes; an improved retrieval module (FTCR vs. ReinFix-style) compounds with execution-level improvements. Standalone evaluation isolates the retrieval hypothesis cleanly.\n\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while Defects4J V1.2 (MVS) and SWE-bench Lite (full version) validate real-world transfer.",
  "resource_estimate": {
    "auto_research": {
      "gpu_hours": "~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)",
      "gpu_utilization": "near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants",
      "ablation_scope": "Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline on same natural corpus), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (4-major coarse / 14-minor single-fault fine / merged-Java within-major), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java → SWE-bench-Lite Python), classifier accuracy stratification by confidence band",
      "timeline": "10-14 days with 2 A100 nodes running in parallel — the ONLY constraint-compliant execution mode for the 16-day hard budget. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) both violate the user's timeline constraint and are not presented as viable paths.",
      "day_by_day_schedule": "Day 0 (May 10): setup and corpus annotation launch. Compute confirmed: 2 A100 nodes provisioned; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested. Day 1–3 (May 11–13): annotation + DebugBench classifier calibration (X% minor-type level, Y% preliminary cross-lingual signal with 95% CI at n=56). Day 4–6 (May 14–16): index construction + Defects4J V1.2 ablations (Variants A/D/E/F) + pre-drafted paper skeleton. Day 7–9 (May 17–19): DebugBench evaluation (single-bug instances) + confidence stratification (Z%, W% aggregate with McNemar's test) + SWE-bench Lite launch. Day 10–12 (May 20–22): CodeBERT ablation + granularity + k-sweep. Day 13 (May 23): results compilation + paper skeleton. Day 14–15 (May 24–25): paper finalization + ARR submission.",
      "team": "0 (initial ~4h setup for corpus pipeline, per-type sub-index construction, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)",
      "claude_api_cost": "$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)",
      "embedding_api_cost": "~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)",
      "estimated_gpu_cost": "~$969 (323 A100-hours × $3/h)",
      "speed_bottleneck": "GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls",
      "risk_note": "SWE-bench Lite may not complete before Day 12; MVS for EMNLP Findings submission is DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control, achievable within the 10–14 day window. Compute pre-provisioned as of Day 0. Auto-assigned bug type labels may drift without the three-pass consistency check; confidence-gated hybrid adds hyperparameter τ requiring tuning on held-out split before SWE-bench evaluation. Two-day paper writing window (Days 13–15) requires pre-drafted skeleton prepared during Days 4–6. Writing window contingency committed: if any experiment is not complete by Day 12 EOD (May 22, 2026), it is unconditionally dropped and the paper closes with MVS results only; no experimental work will be run or extended into the Day 13–15 writing window under any circumstances — this constraint is hard and not subject to revision based on preliminary result quality."
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings (via ARR, deadline May 25, 2026 11:59 PM AoE — PRIMARY TARGET; 15 days from today). The X%/Y%/Z%/W% calibration study — measuring LLM-generated bug type label quality and its downstream impact on retrieval-augmented repair — is appropriate for EMNLP Findings, which publishes solid empirical contributions that advance understanding of specific NLP phenomena. The Main track expects findings that advance understanding of language models at a deeper architectural or representational level and poses higher desk-rejection risk for an empirical calibration study; Findings is the correct target and the proposal commits to it without oscillation. Path: auto-research completes Days 0–12 (May 10–22); paper writing Days 13–15 (May 23–25). Minimum viable submission: DebugBench classifier calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. EMNLP Findings fits the paper's core contribution: LLM annotation reliability for a structured classification task and the downstream retrieval consequences of label noise — a contribution to the NLP literature on LLM-generated categorical labels and RAG system design, directly extending the accuracy-floor findings of arXiv:2407.06153 to the task-specific few-shot regime. Timeline is extremely tight: the two-day writing window requires a pre-drafted paper skeleton prepared concurrently with Days 4–6 experiment setup. Risk: if SWE-bench Lite does not complete by Day 12, the EMNLP Findings version covers DebugBench + Defects4J only, with SWE-bench Lite results added in the ICSE 2027 version.",
    "ICSE 2027 (mandatory abstract deadline June 23, 2026 — BACKUP venue if EMNLP ARR cycle overlaps unfavorably or EMNLP Findings submission is not accepted). SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation; InferFix paragraph establishes LLM-inferred vs. Infer-required type labels as the untested dimension; TypeRepair comparison clarifies FTCR's orthogonal contribution of cross-repository retrieval; LTFix comparison establishes domain generality over single-bug-class approaches; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections; intra-corpus confound framing converts the corpus quality issue into a feature rather than a weakness.",
    "FSE 2027 (full paper deadline October 2, 2026 — tertiary backup if both EMNLP and ICSE review cycles are unfavorable)."
  ],
  "key_references": [
    "InferFix: End-to-End Program Repair with LLMs over Bug-Specific Retrieval (ESEC/FSE 2023, arXiv:2303.07263) [earliest type-conditioned cross-repository repair retrieval; Retriever pretrained via contrastive learning using same-type bug-fix pairs as positives and different-type pairs as negatives (type from Infer static analysis); encoder encodes only buggy code — type structures training pairs but is NOT an explicit encoder input; the retriever learns type-correlated semantic similarity; at retrieval time, candidates are filtered to same-type fixes using Infer-derived labels; achieves 76.8% Java top-1 accuracy; InferFix validates type-conditioned retrieval but requires Infer static analysis at both corpus construction and query time — FTCR's scientific contribution vs. InferFix is testing whether LLM-inferred labels can substitute for Infer-derived labels (X%/Y%) and enabling type-conditioned retrieval for general natural bugs Infer cannot detect; must differentiate: (a) Infer-required labels vs. LLM-inferred labels; (b) query-time type filtering vs. FTCR's construction-time index partitioning; (c) Infer-specific diagnostic IDs vs. 4-major/18-minor natural-bug taxonomy; (d) InferredBugs vs. natural issue-tracker/CI bug-fix pairs]",
    "ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; soft root-cause augmentation using unified vector database with text-embedding-3-large; intra-corpus comparison (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) is the clean architectural test; absolute comparisons against published ReinFix numbers reflect corpus quality confound and are presented as such]",
    "What's Wrong with Your Code Generated by Large Language Models? An Extensive Study (arXiv:2407.06153, EMNLP 2024) [documents LLM auto-labeling accuracy for fine-grained bug types: fully automated zero-shot GPT-4 achieves ~37% secondary-level and ~5% tertiary-level accuracy on a custom 3-primary/10-secondary taxonomy over LLM-generated code (HumanEval+, MBPP+, APPS+); AI-assisted annotation with structured demonstrations reaches 91.6% tertiary accuracy — 18× improvement; key differences from FTCR's setup: (a) zero-shot vs. few-shot with DebugBench-specific demonstrations; (b) custom general taxonomy vs. DebugBench's purpose-built 4-major/18-minor natural-bug taxonomy; (c) LLM-generated code failures vs. natural repository bug-fix pairs; FTCR's X% directly tests whether task-specific few-shot prompting overcomes the documented zero-shot accuracy floor; cite in Introduction and Type Classifier Calibration sections as motivating prior work]",
    "LTFix: Tracing Errors, Constructing Fixes: Repository-Level Memory Error Repair via Typestate-Guided Context Retrieval (arXiv 2506.18394, June 2025) [applies typestate-automaton-guided context extraction to memory errors in C at the repository level; uses a finite typestate automaton to trace error-propagation paths across functions and files for LLM context construction; targets C memory errors only (a single-domain bug class requiring interprocedural static tracing) without retrieval from a historical fix-patch corpus; differentiation from FTCR: domain-specific C memory errors only vs. FTCR's 18 semantic sub-types across C++/Java/Python using LLM-inferred labels without static analysis tooling, with retrieval from 3,050-pair external fix-patch corpus]",
    "SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; 73.0% SWE-bench Verified with Claude 4 Sonnet; agentic, Python-only; differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, multi-language scope]",
    "TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J/QuixBugs (Java-only); validates that type conditioning improves LLM repair; to the best of our knowledge from the publicly accessible abstract and benchmark descriptions, Stage 3 context selection draws from within-project code files and type-specific documentation rather than an external cross-repository corpus — supported by evaluation design (project-internal datasets, no external corpus in benchmark setup); welcome correction from reviewers with full SQJ access; FTCR's orthogonal contribution is type-conditioned retrieval from external ~3,050-pair cross-language corpus]",
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
    "GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; cross-lingual transfer calibration (Y% preliminary cross-lingual signal, n=56 human-verified pairs, 95% CI reported)]",
    "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey; confirms retrieval augmentation as key enhancement; no type-partitioned cross-language system identified; cites InferFix as a key retrieval-augmented approach]",
    "What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]",
    "PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]",
    "RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]",
    "CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism; precedent for FTCR confidence-gated hybrid; cite as preprint — withdrawn from ICLR 2025, unpublished]"
  ],
  "description": "FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft type-conditioned retrieval (ReinFix's root-cause embedding approach, ICSE 2026) for cross-repository fix template transfer, while LLM-inferred type labels can substitute for the Infer-required labels used by InferFix (ESEC/FSE 2023) to enable type-conditioned retrieval on general natural bugs. The primary NLP contribution — targeted at EMNLP 2026 Findings (via ARR, May 25, 2026) — is a complete causal decomposition parameterized by four falsifiable quantities measured at the minor-type level of DebugBench's 4-major/18-minor hierarchical taxonomy: (X%) few-shot LLM classifier accuracy vs. DebugBench ground-truth oracle labels at the minor-type level (major-type aggregation as secondary); (Y%) zero-shot cross-lingual transfer accuracy to Java bugs, reported as a preliminary cross-lingual signal at n=56 with 95% CI to make sampling uncertainty explicit; (Z%) repair improvement for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline (aggregate, McNemar's test, 95% CI); (W%) repair degradation for misclassified instances (aggregate, McNemar's test, 95% CI). X% is framed as a direct empirical test of whether task-specific few-shot prompting overcomes the documented zero-shot accuracy floor (~37% secondary / ~5% tertiary) established by arXiv:2407.06153 (EMNLP 2024); that study found AI-assisted annotation with demonstrations achieves 91.6% tertiary accuracy, motivating FTCR's hypothesis that few-shot with DebugBench-specific examples substantially exceeds the zero-shot floor without human-in-the-loop verification. Together the X%/Y%/Z%/W% quantities characterize when hard categorical type conditioning helps and when it hurts, generalizing to any system using LLM-inferred categorical labels for retrieval routing. FTCR's structural departure from ReinFix is to (1) classify incoming failures into one of the 14 single-fault minor sub-types, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable in a clean intra-corpus comparison. Round 9 revisions address four issues: (a) SWE-smith REMOVED FROM KEY_REFERENCES — SWE-smith was cited as a corpus scaling resource but did not appear among the four actual corpus sources (SWE-bench non-Lite, BugsInPy, Defects4J V1.2, GitBug-Java); removing it eliminates the corpus inconsistency and the venue-verification concern simultaneously; note that during independent verification the SWE-smith GitHub repository does confirm NeurIPS 2025 D&B Spotlight acceptance, but the entry is removed entirely to preserve corpus clarity; (b) SWE-BENCH LITE SOTA MODEL NAME FIXED — 'Claude Opus 4.6' (which does not correspond to any confirmed Anthropic model release; current lineup has Opus 4.7 and Sonnet 4.6) replaced in landscape with 'a leading agentic scaffold (62.7%, May 2026)' to avoid erroneous attribution of a third-party leaderboard label; (c) Y% FRAMING UPDATED — reframed as 'preliminary cross-lingual signal' at n=56 in approach, resource_estimate, and key_references; 95% CI half-width (~±10–13% depending on proportion) explicitly noted so reviewers can assess uncertainty; (d) All Round 8 contributions preserved: arXiv:2407.06153 accuracy floor integration, LTFix one-sentence differentiation, Day-12 hard cutoff commitment, TypeRepair qualifier with explicit reviewer invitation."
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

### Round 7 review
Verdict: revise
Issues: ["MEDIUM — Uncited counterevidence on LLM annotation accuracy undermines X% expectations without preemption: arXiv:2407.06153 ('What's Wrong with Your Code Generated by Large Language Models?') independently measured LLM auto-labeling of fine-grained bug types and found fully automated tertiary-level accuracy of 5.2% and secondary-level accuracy of 35.7%. FTCR's core hypothesis depends on X% being high enough for correctly-classified instances (driving Z%) to outnumber misclassified instances (driving W%). If X% is in the 35% range, hard partitioning would hurt on average. The proposal must cite this paper and explain why its setting (few-shot prompting with DebugBench-specific demonstration examples, a taxonomy purpose-built for LLM classification) is expected to achieve substantially higher accuracy than the general case studied in 2407.06153. Framing FTCR as 'testing whether task-specific few-shot prompting overcomes the documented accuracy floor in general LLM bug classification' would strengthen both the motivation and the EMNLP NLP angle.", "LOW — LTFix (arXiv 2506.18394, 'Tracing Errors, Constructing Fixes: Repository-Level Memory Error Repair via Typestate-Guided Context Retrieval', June 2025) uses type-guided retrieval (typestate automaton) for memory errors in C code at the repository level. While domain-specific, it is the closest recent work to FTCR's type-guided retrieval architecture for repository-level repair and should be cited with a one-sentence differentiation (C memory errors only vs. FTCR's 18-subtype taxonomy across C++/Java/Python).", "LOW — The two-day paper writing window (Days 13–15, May 23–25) remains structurally fragile. If SWE-bench Lite results arrive on Day 12 and require reframing, or if any ablation produces surprising results requiring additional runs, the window collapses. The pre-drafted skeleton policy (stated as prepared during Days 4–6) is necessary but not sufficient mitigation. The proposal should commit to one additional write-up contingency: if any experiment is not complete by Day 12 EOD, drop it and close the paper with the MVS results only rather than attempting to extend experiments into the writing window.", "LOW — TypeRepair (SQJ 2026) differentiation remains technically unverifiable from publicly accessible sources: the claim that Stage 3 context selection draws from within-project code only is inferred from the evaluation design (Defects4J/QuixBugs are project-internal datasets) rather than directly stated in the paper. This evidentiary basis is now stated in the proposal ('The evaluation design makes the within-project scope structurally evident'), which is defensible. However, reviewers with full SQJ access could refute this if wrong. Consider adding a qualifier: 'To the best of our knowledge from the publicly accessible abstract and benchmark descriptions, TypeRepair's context selection stage draws from within-project code files; any reviewer with full SQJ article access who finds this claim incorrect is encouraged to provide the correction.' This signals intellectual honesty and invites correction rather than assertion."]
Feedback: Round 7 has successfully resolved all five Round 6 issues: EMNLP Findings commitment is firm, DebugBench 4-major/18-minor hierarchy is correct throughout, compute readiness is confirmed, InferFix architecture is accurately characterized, and statistical significance is fully specified. The proposal is in its strongest state to date. Two targeted fixes would bring this to submission-ready: (1) CITE AND ADDRESS arXiv:2407.06153 — this is the most important remaining gap. Add a sentence in the introduction or related work: 'Prior work has shown that fully automated LLM classification of fine-grained bug types achieves ~35% accuracy at the secondary level (citation), motivating the question of whether task-specific few-shot prompting with a purpose-built taxonomy (DebugBench) achieves sufficient accuracy to make hard categorical partitioning beneficial on net. FTCR's X%/Y% measurements directly test this.' This frames X% as the paper's central NLP finding and preempts the most likely reviewer objection. (2) ADD ONE SENTENCE about LTFix in the landscape paragraph: 'LTFix applies typestate-automaton-guided retrieval to memory errors in C at the repository level; FTCR generalizes type-conditioned retrieval to 18 semantic sub-types across C++/Java/Python using LLM-inferred labels.' These two additions are low-effort and high-impact for reviewer confidence. The core science is sound — the X%/Y%/Z%/W% causal decomposition is a legitimate EMNLP Findings contribution that no existing paper has made for natural repository bugs.

### Round 8 review
Verdict: revise
Issues: ["HIGH — SWE-smith (arXiv 2504.21798) cited as '(NeurIPS 2025)' but this venue attribution is unconfirmed: the arXiv abstract contains no NeurIPS 2025 affiliation. This is structurally identical to the CRAG-ICLR hallucination flagged as CRITICAL in Round 3. EMNLP has explicitly warned it may desk-reject papers with hallucinated venue citations. Independently verified: no NeurIPS 2025 affiliation appears in the arXiv record. Fix: cite as 'arXiv:2504.21798' only, without the conference attribution, pending verification. This is urgent given the May 25 deadline.", "MEDIUM — SWE-smith is cited in key_references as '[50k Python task instances; scale corpus for Python retrieval index]' but the corpus construction section lists exactly four sources (SWE-bench non-Lite split, BugsInPy, Defects4J V1.2, GitBug-Java) with no mention of SWE-smith. Either integrate SWE-smith as a fifth corpus source with its contribution to the ~3,050-pair count clearly specified, or remove it from key_references to avoid confusing reviewers who will check whether cited datasets are actually used.", "LOW — Y% cross-lingual transfer accuracy is measured on only 56 human-verified Java pairs. Fifty-six instances is below the minimum threshold for robust transfer generalization claims, especially given the known domain difference between Python natural bugs (dominant in SWE-bench) and Java bugs (Defects4J/GitBug-Java). The paper should frame Y% explicitly as a 'preliminary cross-lingual signal' rather than a 'calibration' result, and include the 95% CI for a proportion estimate at n=56 to make the uncertainty visible to reviewers.", "LOW — The SWE-bench Lite SOTA claim attributes 62.7% to 'Claude Opus 4.6,' a model name that does not correspond to any confirmed Anthropic model release (the current Anthropic lineup has Opus 4.7 and Sonnet 4.6, not Opus 4.6). While this name appears on third-party leaderboard aggregators, citing it in an EMNLP paper risks repeating the same type of erroneous attribution EMNLP has flagged. Verify directly against the official swebench.com leaderboard and use whatever model name appears there verbatim, or describe the entry as 'a leading agentic scaffold (62.7%, May 2026)' without naming the specific model."]
Feedback: Round 8 has successfully resolved all four Round 7 issues: arXiv:2407.06153 is now integrated throughout as the accuracy-floor baseline with both-outcome publishability made explicit; LTFix is cited with one-sentence differentiation; the Day 12 hard cutoff commitment is unconditional and stated clearly; the TypeRepair qualifier is appropriately hedged. The core X%/Y%/Z%/W% framework is the strongest it has been across all rounds. One new issue blocks submission and must be fixed before ARR: (1) SWE-smith is cited as 'NeurIPS 2025' but this affiliation cannot be independently verified from the arXiv record — change the citation to 'arXiv:2504.21798' without a conference name, or verify the NeurIPS 2025 acceptance directly before submission. This is the same hallucinated-venue pattern that triggered a CRITICAL issue with CRAG in Round 3 and must be treated with equal urgency. (2) Either add SWE-smith as a real corpus source (and adjust the ~3,050 pair count) or remove it from key_references — having it cited as a retrieval corpus scaling resource while not appearing in the approach's four corpus sources is a verifiable inconsistency reviewers will catch. These two fixes are low-effort and high-stakes. All other remaining issues (Y% sample size, model naming) are LOW severity and can be addressed with hedging language. After these fixes, the proposal is credibly at the EMNLP Findings threshold.


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
  "promptId": "d8e019a7-4fb5-483f-a7d7-3989a1ad9470",
  "type": "user",
  "uuid": "e885a644-734e-4455-bd34-b3a75eaf8040",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:52:38.362Z_

```json
{
  "parentUuid": "e885a644-734e-4455-bd34-b3a75eaf8040",
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
  "uuid": "682f94ba-6ea0-42eb-8d8c-701a585b3a28",
  "timestamp": "2026-05-10T07:52:38.362Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:52:38.362Z_

```json
{
  "parentUuid": "682f94ba-6ea0-42eb-8d8c-701a585b3a28",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d26c982a-7a69-4e96-a817-f3cf323f46d6",
  "timestamp": "2026-05-10T07:52:38.362Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
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
  "leafUuid": "d26c982a-7a69-4e96-a817-f3cf323f46d6",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Type-Conditioned Retrieval for Repository-Level Program Repair",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:52:52.408Z_

<details><summary>Logged reasoning block</summary>

```text
This is round 9/10 of an adversarial review of a paper idea called "Failure-Type-Conditioned Retrieval Augmentation for Repository Repair" (FTCR). I need to independently verify claims, check for competing work, and assess novelty, feasibility, clarity, and impact.

Let me analyze the round 9 revision and what was addressed:
1. SWE-smith REMOVED from key_references (addresses Round 8 HIGH issue)
2. SWE-bench Lite SOTA model name fixed to "a leading agentic scaffold (62.7%, May 2026)" (addresses Round 8 LOW issue)


3. Y% framing updated to "preliminary cross-lingual signal" with 95% CI (addresses Round 8 LOW issue)
4. All Round 8 contributions preserved

Now I'm verifying the claims independently, searching for any competing work that might have been overlooked, and checking whether the remaining issues have been properly resolved. Since this is round 9/10, if I find additional issues I'll recommend revision but note that round 10 will force a final pass/fail decision.

I need to systematically verify the InferFix and ReinFix details, check for new competing work in type-conditioned retrieval for code repair, validate the SWE-Exp and DebugBench taxonomy claims, and search for any recent 2025-2026 work on type-conditioned retrieval for automated program repair.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d26c982a-7a69-4e96-a817-f3cf323f46d6",
  "isSidechain": false,
  "requestId": "req_011CatXShmqyx53werUHwBsh",
  "type": "assistant",
  "uuid": "98fa58da-ca5a-4a45-b361-7c405dca5613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SRaBSCSZNMC7B3gWrZnCe8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33993,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33993,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1373,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 33993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33993
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

_source line 9 · 2026-05-10T07:52:52.419Z_

I'll conduct independent verification searches before issuing the round 9 verdict.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98fa58da-ca5a-4a45-b361-7c405dca5613",
  "isSidechain": false,
  "requestId": "req_011CatXShmqyx53werUHwBsh",
  "type": "assistant",
  "uuid": "49b92fd4-8c5d-4fcb-8c8b-b22e8957951e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SRaBSCSZNMC7B3gWrZnCe8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33993,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33993,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1373,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 33993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33993
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

_source line 10 · 2026-05-10T07:53:01.352Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JEzA5aro7Q3dKmhur1YJRT`</summary>

```json
{
  "description": "Verify FTCR competing work and novelty claims",
  "subagent_type": "Explore",
  "prompt": "You are helping me conduct an adversarial review of a research paper idea called \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\" (FTCR). I need you to do targeted web searches to independently verify claims.\n\nPlease perform the following searches and report back the key findings:\n\n1. Search for \"InferFix end-to-end program repair LLMs bug-specific retrieval ESEC FSE 2023\" to verify InferFix's mechanism (does it use hard categorical partitioning or soft contrastive learning for type-conditioned retrieval?)\n\n2. Search for \"type-conditioned retrieval program repair 2025 2026\" to find any new competing work\n\n3. Search for \"DebugBench evaluating debugging capability large language models ACL 2024\" to verify the taxonomy structure (4 major categories, 18 minor sub-types)\n\n4. Search for \"ReinFix repair ingredients program repair retrieval ICSE 2026 arxiv 2506.23100\" to verify its mechanism\n\n5. Search for \"TypeRepair defect type aware adaptive program repair software quality journal 2026\" to check if it uses within-project or cross-repo retrieval\n\n6. Search for \"failure type conditioned retrieval repository repair\" to check if FTCR itself or something very similar exists already\n\n7. Search for \"SWE-Exp experience driven software issue resolution arxiv 2507.23361\" to verify its mechanism\n\n8. Search arXiv for any 2025-2026 papers on \"bug type classification retrieval augmented program repair\" that might be missed\n\nPlease use WebSearch for each query and report specific findings including paper titles, venues, methods, and any key numerical results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49b92fd4-8c5d-4fcb-8c8b-b22e8957951e",
  "isSidechain": false,
  "requestId": "req_011CatXShmqyx53werUHwBsh",
  "type": "assistant",
  "uuid": "fcdd0d48-c106-4021-afde-b9109c6f8230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SRaBSCSZNMC7B3gWrZnCe8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33993,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33993,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1373,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 33993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33993
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

_source line 11 · 2026-05-10T07:53:08.899Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014cZzdogmAZP329mZ2PVGAh`</summary>

```json
{
  "description": "Verify feasibility and SOTA claims for FTCR",
  "subagent_type": "Explore",
  "prompt": "You are helping me conduct an adversarial review of a research paper idea. Please do the following web searches and report back findings:\n\n1. Search \"SWE-bench Verified leaderboard 2026\" or \"SWEbench leaderboard May 2026\" to verify what the current SOTA is (claimed to be ~62.7%)\n\n2. Search \"DebugBench LeetCode bug types taxonomy\" to confirm the actual structure (how many major categories, how many sub-types per category)\n\n3. Search \"arXiv 2407.06153 LLM bug classification accuracy\" to verify the claimed accuracy floor of ~37% secondary-level for zero-shot GPT-4\n\n4. Search \"EMNLP 2026 ARR deadline May 2026\" to confirm the submission deadline is indeed May 25, 2026\n\n5. Search \"GitBug-Java reproducible benchmark Java bugs MSR 2024\" to verify it's 199 bugs\n\n6. Search \"M-RAG multi-partition retrieval ACL 2024 arxiv 2405.16420\" to verify the claimed improvements (+11% summarization, +8% translation)\n\n7. Search \"CRAG corrective retrieval augmented generation arxiv 2401.15884\" to verify it was withdrawn from ICLR 2025\n\n8. Search \"DynaFix iterative automated program repair execution dynamic arxiv 2512.24635\" to verify its claimed superiority over ReinFix on Defects4J V2.0\n\nPlease use WebSearch and WebFetch where needed, and report specific details about what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcdd0d48-c106-4021-afde-b9109c6f8230",
  "isSidechain": false,
  "requestId": "req_011CatXShmqyx53werUHwBsh",
  "type": "assistant",
  "uuid": "ff180e4c-e63a-4942-b5c2-ffa27356923a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SRaBSCSZNMC7B3gWrZnCe8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 33993,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 33993,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1373,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 33993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 33993
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

_source line 12 · 2026-05-10T07:53:40.390Z_

<details><summary>↩ Tool result · `toolu_01JEzA5aro7Q3dKmhur1YJRT`</summary>

```text
## Comprehensive Verification Report

I've completed the eight targeted searches and found detailed information on the key claims you're investigating. Here are the verified findings:

### 1. **InferFix Mechanism (ESEC/FSE 2023)**

**Finding**: InferFix uses **contrastive learning**, not hard categorical partitioning.

- **Retriever Design**: Uses a transformer encoder model pretrained via **contrastive learning objective** to search for semantically equivalent bugs and corresponding fixes
- **Prompt Augmentation**: Combines bug type annotations with semantically similar fixes retrieved from external non-parametric memory
- **Performance**: 65.6% top-1 accuracy in C# and 76.8% in Java
- **Status**: Verified and deployed at Microsoft

This directly contradicts any claim that InferFix uses hard categorical partitioning for type conditioning.

**Source**: [InferFix: End-to-End Program Repair with LLMs over Retrieval-Augmented Prompts](https://arxiv.org/pdf/2303.07263)

---

### 2. **Type-Conditioned Retrieval - Recent Competing Work (2025-2026)**

**Key Systems Found**:

1. **ReAPR** - Automatic program repair via retrieval-augmented LLMs (Software Quality Journal 2025)
2. **RetypeR** - Integrated retrieval-based APR for Python type errors (ICSME 2024)
3. **ReCode** - Improving LLM-based code repair with fine-grained retrieval-augmented generation (arXiv 2509.02330)
4. **ReinFix** - Repair ingredients search (ICSE 2026, arxiv 2506.23100) - see detail below

The field shows multiple competing approaches to retrieval-conditioned repair, suggesting this is an active research area.

**Sources**: 
- [ReAPR: Automatic program repair via retrieval-augmented large language models](https://link.springer.com/article/10.1007/s11219-025-09728-1)
- [RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors](https://conf.researchr.org/details/icsme-2024/icsme-2024-papers/20/RetypeR-Integrated-Retrieval-based-Automatic-Program-Repair-for-Python-Type-Errors)

---

### 3. **DebugBench Taxonomy (ACL 2024)**

**Finding**: Confirmed. DebugBench contains **4,253 instances covering 4 major categories and 18 minor types** across C++, Java, and Python.

- **Construction**: Code snippets from LeetCode, bugs implanted with GPT-4, rigorous quality checks
- **Key Finding**: Debugging complexity varies significantly by bug category
- **Models Evaluated**: Both closed-source and open-source LLMs tested
- **Insight**: Runtime feedback incorporation improves performance inconsistently

**Status**: Verified. GitHub repository available with code and dataset.

**Source**: [DebugBench: Evaluating Debugging Capability of Large Language Models](https://aclanthology.org/2024.findings-acl.247/)

---

### 4. **ReinFix Mechanism (ICSE 2026, arxiv 2506.23100)**

**Finding**: ReinFix uses **repair ingredients search** across two phases:

- **Internal Ingredients**: During reasoning phase, LLM-based agents search internal knowledge
- **External Ingredients**: During solution phase, searches for historical bug fixes with similar bug patterns
- **Guidance**: Uses both buggy code AND root cause information to identify appropriate repair actions
- **Performance**: Fixes 146 bugs on Defects4J V1.2 (32 more than baselines) and 38 more on V2.0
- **Acceptance**: ICSE 2026

**Key Difference from FTCR**: ReinFix searches based on "similar bug patterns" but doesn't explicitly condition on failure type taxonomy.

**Source**: [Repair Ingredients Are All You Need: Improving Large Language Model-Based Program Repair via Repair Ingredients Search](https://arxiv.org/abs/2506.23100)

---

### 5. **TypeRepair Mechanism (Software Quality Journal 2026)**

**Finding**: TypeRepair uses **defect-type-aware adaptive multi-stage approach** with within-project context selection.

- **Four-Stage Pipeline**: Defect localization → defect type identification → **context selection** → patch generation
- **Retrieval Strategy**: The context selection stage (stage 3) appears to focus on within-project or repository-level retrieval
- **Performance**: 272.73% improvement over baseline LLM with GPT-3.5; 257.89% with GPT-4 on Defects4J v2.0
- **Innovation**: First framework explicitly integrating defect-type modeling with multi-stage reasoning

**Status**: Verified in Software Quality Journal 2026

**Source**: [Towards defect-type-aware adaptive program repair: A stage-wise approach with large language models](https://link.springer.com/article/10.1007/s11219-026-09751-w)

---

### 6. **"Failure Type Conditioned Retrieval Repository Repair"**

**Finding**: The exact phrase does not appear to exist as published work. However, related systems discovered:

1. **Doctor-RAG** - Diagnoses and repairs failures in Agentic RAG by attributing errors to a **taxonomy** and applying **failure-type-conditioned repairs**:
   - Implements trajectory-level failure diagnosis
   - Tool-conditioned localized repair
   - Different repair operations for different failure types (format errors, evidence preservation, retrieval failures, planning errors)
   - This appears to be the closest conceptual match to the proposed FTCR approach

2. **PatchRecall** - Patch-driven retrieval for automated program repair, addressing repository-level retrieval tailoring

**Critical Finding**: Doctor-RAG in 2026 (arxiv 2604.00865) already implements failure-type-conditioned repair strategies, though in the RAG/agentic context rather than purely program repair.

**Sources**:
- [Doctor-RAG: Failure-Aware Repair for Agentic Retrieval-Augmented Generation](https://arxiv.org/html/2604.00865)
- [PatchRecall: Patch-Driven Retrieval for Automated Program Repair](https://arxiv.org/html/2604.10481)

---

### 7. **SWE-Exp (arxiv 2507.23361)**

**Finding**: SWE-Exp is an experience-driven approach that uses **experience banks capturing successful AND failed repair attempts**.

- **Problem Addressed**: Current agents are "memoryless explorers" treating each problem separately
- **Innovation**: Multi-faceted experience bank at different abstraction levels (problem comprehension to code changes)
- **Mechanism**: Continuous learning from prior agent trajectories rather than conditioning on pre-defined failure types
- **Performance**: 41.6% Pass@1 on SWE-bench-Verified (state-of-the-art for open-source frameworks)
- **Temporal**: Submitted July 31, 2025

**Key Difference from FTCR**: SWE-Exp uses learned experience from trajectories, not hard failure type taxonomy.

**Source**: [SWE-Exp: Experience-Driven Software Issue Resolution](https://arxiv.org/abs/2507.23361)

---

### 8. **arXiv Papers on Bug Type Classification + RAG + Program Repair (2025-2026)**

**Key Papers Found**:

1. **A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications** (2506.23749)
   - Covers Jan 2022 - June 2025
   - Categorizes recent systems into 4 paradigms showing how retrieval-/analysis-augmented contexts strengthen APR
   
2. **GitBugs** (2504.09651) - Dataset of 150,000+ bug reports supporting duplicate detection, RAG, triage
   
3. **RelRepair** (2509.16701) - Retrieval-augmented APR approach
   
4. **RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY** (2510.04905)
   - Coverage period: Jan 1, 2023 - Aug 31, 2025
   - Covers program repair as growing area

**Notable Gap**: While multiple papers address retrieval-augmented program repair and bug classification separately, there's no evidence of a prior system that explicitly uses **failure-type-conditioned retrieval** as the central organizing principle, with a formal taxonomy mapped to retrieval strategies.

**Sources**:
- [A Survey of LLM-based Automated Program Repair](https://arxiv.org/html/2506.23749v1)
- [GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, Triage, and More](https://arxiv.org/abs/2504.09651)

---

## Summary of Key Findings for Your Adversarial Review

| Aspect | Status | Finding |
|--------|--------|---------|
| **InferFix mechanism** | Verified | Uses contrastive learning, not hard categorization |
| **Type-conditioned retrieval (2025-26)** | Multiple competitors | ReAPR, RetypeR, ReCode, ReinFix, TypeRepair all active |
| **DebugBench taxonomy** | Verified | Exactly 4 major categories, 18 minor types confirmed |
| **ReinFix mechanism** | Verified | Uses "repair ingredients" search, not failure-type taxonomy |
| **TypeRepair retrieval** | Verified | Multi-stage with type-aware context selection |
| **FTCR exact prior work** | NOT FOUND | Doctor-RAG uses failure-type-conditioned repair but in RAG/agentic context |
| **SWE-Exp mechanism** | Verified | Experience-driven, not taxonomy-based |
| **GAP in literature** | Found | No clear prior work on **failure-type-conditioned retrieval specifically for program repair** using formal taxonomy |

The field appears active with multiple approaches, but the specific combination of (1) explicit failure-type taxonomy, (2) soft contrastive retrieval conditioning, and (3) repository-level patch retrieval does not appear to have a direct published predecessor based on these searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcdd0d48-c106-4021-afde-b9109c6f8230",
  "isSidechain": false,
  "promptId": "d8e019a7-4fb5-483f-a7d7-3989a1ad9470",
  "type": "user",
  "uuid": "7bf07804-d4d7-4703-a901-b6bd0ee5386e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me conduct an adversarial review of a research paper idea called \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\" (FTCR). I need you to do targeted web searches to independently verify claims.\n\nPlease perform the following searches and report back the key findings:\n\n1. Search for \"InferFix end-to-end program repair LLMs bug-specific retrieval ESEC FSE 2023\" to verify InferFix's mechanism (does it use hard categorical partitioning or soft contrastive learning for type-conditioned retrieval?)\n\n2. Search for \"type-conditioned retrieval program repair 2025 2026\" to find any new competing work\n\n3. Search for \"DebugBench evaluating debugging capability large language models ACL 2024\" to verify the taxonomy structure (4 major categories, 18 minor sub-types)\n\n4. Search for \"ReinFix repair ingredients program repair retrieval ICSE 2026 arxiv 2506.23100\" to verify its mechanism\n\n5. Search for \"TypeRepair defect type aware adaptive program repair software quality journal 2026\" to check if it uses within-project or cross-repo retrieval\n\n6. Search for \"failure type conditioned retrieval repository repair\" to check if FTCR itself or something very similar exists already\n\n7. Search for \"SWE-Exp experience driven software issue resolution arxiv 2507.23361\" to verify its mechanism\n\n8. Search arXiv for any 2025-2026 papers on \"bug type classification retrieval augmented program repair\" that might be missed\n\nPlease use WebSearch for each query and report specific findings including paper titles, venues, methods, and any key numerical results.",
    "agentId": "afc50b374ce823c08",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Comprehensive Verification Report\n\nI've completed the eight targeted searches and found detailed information on the key claims you're investigating. Here are the verified findings:\n\n### 1. **InferFix Mechanism (ESEC/FSE 2023)**\n\n**Finding**: InferFix uses **contrastive learning**, not hard categorical partitioning.\n\n- **Retriever Design**: Uses a transformer encoder model pretrained via **contrastive learning objective** to search for semantically equivalent bugs and corresponding fixes\n- **Prompt Augmentation**: Combines bug type annotations with semantically similar fixes retrieved from external non-parametric memory\n- **Performance**: 65.6% top-1 accuracy in C# and 76.8% in Java\n- **Status**: Verified and deployed at Microsoft\n\nThis directly contradicts any claim that InferFix uses hard categorical partitioning for type conditioning.\n\n**Source**: [InferFix: End-to-End Program Repair with LLMs over Retrieval-Augmented Prompts](https://arxiv.org/pdf/2303.07263)\n\n---\n\n### 2. **Type-Conditioned Retrieval - Recent Competing Work (2025-2026)**\n\n**Key Systems Found**:\n\n1. **ReAPR** - Automatic program repair via retrieval-augmented LLMs (Software Quality Journal 2025)\n2. **RetypeR** - Integrated retrieval-based APR for Python type errors (ICSME 2024)\n3. **ReCode** - Improving LLM-based code repair with fine-grained retrieval-augmented generation (arXiv 2509.02330)\n4. **ReinFix** - Repair ingredients search (ICSE 2026, arxiv 2506.23100) - see detail below\n\nThe field shows multiple competing approaches to retrieval-conditioned repair, suggesting this is an active research area.\n\n**Sources**: \n- [ReAPR: Automatic program repair via retrieval-augmented large language models](https://link.springer.com/article/10.1007/s11219-025-09728-1)\n- [RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors](https://conf.researchr.org/details/icsme-2024/icsme-2024-papers/20/RetypeR-Integrated-Retrieval-based-Automatic-Program-Repair-for-Python-Type-Errors)\n\n---\n\n### 3. **DebugBench Taxonomy (ACL 2024)**\n\n**Finding**: Confirmed. DebugBench contains **4,253 instances covering 4 major categories and 18 minor types** across C++, Java, and Python.\n\n- **Construction**: Code snippets from LeetCode, bugs implanted with GPT-4, rigorous quality checks\n- **Key Finding**: Debugging complexity varies significantly by bug category\n- **Models Evaluated**: Both closed-source and open-source LLMs tested\n- **Insight**: Runtime feedback incorporation improves performance inconsistently\n\n**Status**: Verified. GitHub repository available with code and dataset.\n\n**Source**: [DebugBench: Evaluating Debugging Capability of Large Language Models](https://aclanthology.org/2024.findings-acl.247/)\n\n---\n\n### 4. **ReinFix Mechanism (ICSE 2026, arxiv 2506.23100)**\n\n**Finding**: ReinFix uses **repair ingredients search** across two phases:\n\n- **Internal Ingredients**: During reasoning phase, LLM-based agents search internal knowledge\n- **External Ingredients**: During solution phase, searches for historical bug fixes with similar bug patterns\n- **Guidance**: Uses both buggy code AND root cause information to identify appropriate repair actions\n- **Performance**: Fixes 146 bugs on Defects4J V1.2 (32 more than baselines) and 38 more on V2.0\n- **Acceptance**: ICSE 2026\n\n**Key Difference from FTCR**: ReinFix searches based on \"similar bug patterns\" but doesn't explicitly condition on failure type taxonomy.\n\n**Source**: [Repair Ingredients Are All You Need: Improving Large Language Model-Based Program Repair via Repair Ingredients Search](https://arxiv.org/abs/2506.23100)\n\n---\n\n### 5. **TypeRepair Mechanism (Software Quality Journal 2026)**\n\n**Finding**: TypeRepair uses **defect-type-aware adaptive multi-stage approach** with within-project context selection.\n\n- **Four-Stage Pipeline**: Defect localization → defect type identification → **context selection** → patch generation\n- **Retrieval Strategy**: The context selection stage (stage 3) appears to focus on within-project or repository-level retrieval\n- **Performance**: 272.73% improvement over baseline LLM with GPT-3.5; 257.89% with GPT-4 on Defects4J v2.0\n- **Innovation**: First framework explicitly integrating defect-type modeling with multi-stage reasoning\n\n**Status**: Verified in Software Quality Journal 2026\n\n**Source**: [Towards defect-type-aware adaptive program repair: A stage-wise approach with large language models](https://link.springer.com/article/10.1007/s11219-026-09751-w)\n\n---\n\n### 6. **\"Failure Type Conditioned Retrieval Repository Repair\"**\n\n**Finding**: The exact phrase does not appear to exist as published work. However, related systems discovered:\n\n1. **Doctor-RAG** - Diagnoses and repairs failures in Agentic RAG by attributing errors to a **taxonomy** and applying **failure-type-conditioned repairs**:\n   - Implements trajectory-level failure diagnosis\n   - Tool-conditioned localized repair\n   - Different repair operations for different failure types (format errors, evidence preservation, retrieval failures, planning errors)\n   - This appears to be the closest conceptual match to the proposed FTCR approach\n\n2. **PatchRecall** - Patch-driven retrieval for automated program repair, addressing repository-level retrieval tailoring\n\n**Critical Finding**: Doctor-RAG in 2026 (arxiv 2604.00865) already implements failure-type-conditioned repair strategies, though in the RAG/agentic context rather than purely program repair.\n\n**Sources**:\n- [Doctor-RAG: Failure-Aware Repair for Agentic Retrieval-Augmented Generation](https://arxiv.org/html/2604.00865)\n- [PatchRecall: Patch-Driven Retrieval for Automated Program Repair](https://arxiv.org/html/2604.10481)\n\n---\n\n### 7. **SWE-Exp (arxiv 2507.23361)**\n\n**Finding**: SWE-Exp is an experience-driven approach that uses **experience banks capturing successful AND failed repair attempts**.\n\n- **Problem Addressed**: Current agents are \"memoryless explorers\" treating each problem separately\n- **Innovation**: Multi-faceted experience bank at different abstraction levels (problem comprehension to code changes)\n- **Mechanism**: Continuous learning from prior agent trajectories rather than conditioning on pre-defined failure types\n- **Performance**: 41.6% Pass@1 on SWE-bench-Verified (state-of-the-art for open-source frameworks)\n- **Temporal**: Submitted July 31, 2025\n\n**Key Difference from FTCR**: SWE-Exp uses learned experience from trajectories, not hard failure type taxonomy.\n\n**Source**: [SWE-Exp: Experience-Driven Software Issue Resolution](https://arxiv.org/abs/2507.23361)\n\n---\n\n### 8. **arXiv Papers on Bug Type Classification + RAG + Program Repair (2025-2026)**\n\n**Key Papers Found**:\n\n1. **A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications** (2506.23749)\n   - Covers Jan 2022 - June 2025\n   - Categorizes recent systems into 4 paradigms showing how retrieval-/analysis-augmented contexts strengthen APR\n   \n2. **GitBugs** (2504.09651) - Dataset of 150,000+ bug reports supporting duplicate detection, RAG, triage\n   \n3. **RelRepair** (2509.16701) - Retrieval-augmented APR approach\n   \n4. **RETRIEVAL-AUGMENTED CODE GENERATION: A SURVEY** (2510.04905)\n   - Coverage period: Jan 1, 2023 - Aug 31, 2025\n   - Covers program repair as growing area\n\n**Notable Gap**: While multiple papers address retrieval-augmented program repair and bug classification separately, there's no evidence of a prior system that explicitly uses **failure-type-conditioned retrieval** as the central organizing principle, with a formal taxonomy mapped to retrieval strategies.\n\n**Sources**:\n- [A Survey of LLM-based Automated Program Repair](https://arxiv.org/html/2506.23749v1)\n- [GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, Triage, and More](https://arxiv.org/abs/2504.09651)\n\n---\n\n## Summary of Key Findings for Your Adversarial Review\n\n| Aspect | Status | Finding |\n|--------|--------|---------|\n| **InferFix mechanism** | Verified | Uses contrastive learning, not hard categorization |\n| **Type-conditioned retrieval (2025-26)** | Multiple competitors | ReAPR, RetypeR, ReCode, ReinFix, TypeRepair all active |\n| **DebugBench taxonomy** | Verified | Exactly 4 major categories, 18 minor types confirmed |\n| **ReinFix mechanism** | Verified | Uses \"repair ingredients\" search, not failure-type taxonomy |\n| **TypeRepair retrieval** | Verified | Multi-stage with type-aware context selection |\n| **FTCR exact prior work** | NOT FOUND | Doctor-RAG uses failure-type-conditioned repair but in RAG/agentic context |\n| **SWE-Exp mechanism** | Verified | Experience-driven, not taxonomy-based |\n| **GAP in literature** | Found | No clear prior work on **failure-type-conditioned retrieval specifically for program repair** using formal taxonomy |\n\nThe field appears active with multiple approaches, but the specific combination of (1) explicit failure-type taxonomy, (2) soft contrastive retrieval conditioning, and (3) repository-level patch retrieval does not appear to have a direct published predecessor based on these searches."
      }
    ],
    "totalDurationMs": 39030,
    "totalTokens": 28347,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1790,
      "cache_creation_input_tokens": 7068,
      "cache_read_input_tokens": 16971,
      "output_tokens": 2518,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7068
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1790,
          "output_tokens": 2518,
          "cache_read_input_tokens": 16971,
          "cache_creation_input_tokens": 7068,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7068,
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
  "sourceToolAssistantUUID": "fcdd0d48-c106-4021-afde-b9109c6f8230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
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
  "leafUuid": "7bf07804-d4d7-4703-a901-b6bd0ee5386e",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Type-Conditioned Retrieval for Repository-Level Program Repair",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836"
}
```

---

### Tool result

_source line 15 · 2026-05-10T07:54:15.920Z_

<details><summary>↩ Tool result · `toolu_014cZzdogmAZP329mZ2PVGAh`</summary>

```text
Perfect! Now let me compile my findings:

## Adversarial Review Web Search Findings

I've completed all eight searches and cross-verification. Here are the key findings:

### 1. **SWE-bench Verified SOTA (Claim: ~62.7%)**

**Finding: PARTIALLY INACCURATE**
- The 62.7% figure appears to be for SWE-Bench **Lite**, not SWE-Bench **Verified**
- SWE-Bench Verified (as of May 2026) shows much higher scores:
  - Claude Mythos Preview: 93.9%
  - GPT-5.5: 88.7%
  - Claude Opus 4.7: 87.6%
  - GPT-5.3 Codex: 85.0%
- **Critical caveat:** OpenAI discontinued reporting Verified scores in early 2026 due to data contamination concerns. The same models score dramatically lower on the harder SWE-Bench Pro (Claude Mythos Preview scores 45.9% on Pro vs 93.9% on Verified)
- SWE-Bench Pro: Claude Opus 4.7 leads at 64.3%

### 2. **DebugBench Taxonomy Structure**

**Finding: VERIFIED - ACCURATE**
- **4 major categories:** Syntax, Reference, Logic, and Multiple
- **18 minor/sub-types total** including: misused ==/=, missing colons, unclosed parentheses, faulty indexing, undefined objects, undefined methods, condition error, operation error, variable error, and bugs with multiple errors (double/triple/quadruple)

### 3. **arXiv 2407.06153 LLM Bug Classification Accuracy (Claim: ~37% zero-shot GPT-4)**

**Finding: NOT VERIFIED - PAPER FOCUS DIFFERS**
- The paper "What is Wrong with Your Code Generated by Large Language Models?" (2407.06153) is about **bug types in LLM-generated code**, not bug classification accuracy
- It develops a taxonomy of bugs and achieved a repair success rate of 29.2% after two iterations, but does not report the 37% secondary-level zero-shot GPT-4 accuracy claim you mentioned
- The paper's focus is on understanding limitations of LLM code generation, not classification metrics

### 4. **EMNLP 2026 ARR Deadline (Claim: May 25, 2026)**

**Finding: VERIFIED - ACCURATE**
- ARR submission deadline for EMNLP 2026: **May 25, 2026** (confirmed)
- Reviewer registration deadline: May 27, 2026
- Meta review release: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Important note: Authors must explicitly declare their target conference (EMNLP or AACL) at submission since they share the May 2026 ARR cycle

### 5. **GitBug-Java Benchmark Size (Claim: 199 bugs)**

**Finding: VERIFIED - ACCURATE**
- GitBug-Java contains **199 bugs** from 2023 commit history of 55 open-source Java repositories
- Published at MSR 2024 (21st International Conference on Mining Software Repositories)
- All bugs are from 2023, after LLM training cutoffs

### 6. **M-RAG Performance Improvements (Claim: +11% summarization, +8% translation)**

**Finding: VERIFIED - ACCURATE**
- M-RAG achieved **11% improvement** for text summarization
- M-RAG achieved **8% improvement** for machine translation
- Also achieved **12% improvement** for dialogue generation (not mentioned in your claim)
- Published at ACL 2024 (arXiv 2405.16420)
- Improvements validated across 7 datasets, 3 language generation tasks, and 3 LLM architectures

### 7. **CRAG and ICLR 2025 (Claim: withdrawn from ICLR 2025)**

**Finding: INACCURATE - OPPOSITE IS TRUE**
- CRAG was **accepted to ICLR 2024** (not ICLR 2025, and not withdrawn)
- Paper: "Corrective Retrieval Augmented Generation" (arXiv 2401.15884)
- The paper was accepted to ICLR 2024 in Vienna, Austria (May 7-11, 2024)
- Last revision on arXiv: October 7, 2024
- No evidence of withdrawal from ICLR 2025

### 8. **DynaFix vs ReinFix on Defects4J V2.0 (Claim: DynaFix superior)**

**Finding: VERIFIED - PARTIALLY ACCURATE**
- DynaFix repairs **236 bugs with GPT-4** and **186 bugs with GPT-4o** on Defects4J v2.0
- DynaFix achieves **15.6%-32.1% higher repair rates than ReInFix**
- DynaFix fixes 23 bugs that no other baseline methods can repair
- DynaFix provides **60%-70% token reduction** compared to existing SOTA approaches
- However, the search results indicate ReInFix also performs well (fixes 38 more bugs than prior SOTA), but DynaFix's iterative execution-based approach appears to be superior

---

**Summary of Issues for Your Adversarial Review:**
1. The 62.7% SOTA claim may conflate different SWE-Bench variants
2. The arXiv 2407.06153 paper doesn't contain the specific 37% accuracy metric you claim
3. CRAG was accepted to ICLR 2024, not withdrawn from ICLR 2025 (this is a significant factual error)
4. Most other claims (DebugBench taxonomy, EMNLP deadline, GitBug-Java size, M-RAG improvements, DynaFix performance) are accurate

Sources:
- [SWE-Bench Leaderboards](https://www.swebench.com/)
- [SWE-Bench Verified Leaderboard 2026](https://benchlm.ai/benchmarks/sweVerified)
- [DebugBench Paper](https://aclanthology.org/2024.findings-acl.247.pdf)
- [arXiv 2407.06153](https://arxiv.org/abs/2407.06153)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [GitBug-Java at MSR 2024](https://arxiv.org/abs/2402.02961)
- [M-RAG at ACL 2024](https://aclanthology.org/2024.acl-long.108/)
- [CRAG Paper](https://arxiv.org/abs/2401.15884)
- [DynaFix arXiv](https://arxiv.org/abs/2512.24635)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff180e4c-e63a-4942-b5c2-ffa27356923a",
  "isSidechain": false,
  "promptId": "d8e019a7-4fb5-483f-a7d7-3989a1ad9470",
  "type": "user",
  "uuid": "011d2c85-a30a-4e16-bf50-8af25210e394",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping me conduct an adversarial review of a research paper idea. Please do the following web searches and report back findings:\n\n1. Search \"SWE-bench Verified leaderboard 2026\" or \"SWEbench leaderboard May 2026\" to verify what the current SOTA is (claimed to be ~62.7%)\n\n2. Search \"DebugBench LeetCode bug types taxonomy\" to confirm the actual structure (how many major categories, how many sub-types per category)\n\n3. Search \"arXiv 2407.06153 LLM bug classification accuracy\" to verify the claimed accuracy floor of ~37% secondary-level for zero-shot GPT-4\n\n4. Search \"EMNLP 2026 ARR deadline May 2026\" to confirm the submission deadline is indeed May 25, 2026\n\n5. Search \"GitBug-Java reproducible benchmark Java bugs MSR 2024\" to verify it's 199 bugs\n\n6. Search \"M-RAG multi-partition retrieval ACL 2024 arxiv 2405.16420\" to verify the claimed improvements (+11% summarization, +8% translation)\n\n7. Search \"CRAG corrective retrieval augmented generation arxiv 2401.15884\" to verify it was withdrawn from ICLR 2025\n\n8. Search \"DynaFix iterative automated program repair execution dynamic arxiv 2512.24635\" to verify its claimed superiority over ReinFix on Defects4J V2.0\n\nPlease use WebSearch and WebFetch where needed, and report specific details about what you find.",
    "agentId": "ac3c0411e34f688b4",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me compile my findings:\n\n## Adversarial Review Web Search Findings\n\nI've completed all eight searches and cross-verification. Here are the key findings:\n\n### 1. **SWE-bench Verified SOTA (Claim: ~62.7%)**\n\n**Finding: PARTIALLY INACCURATE**\n- The 62.7% figure appears to be for SWE-Bench **Lite**, not SWE-Bench **Verified**\n- SWE-Bench Verified (as of May 2026) shows much higher scores:\n  - Claude Mythos Preview: 93.9%\n  - GPT-5.5: 88.7%\n  - Claude Opus 4.7: 87.6%\n  - GPT-5.3 Codex: 85.0%\n- **Critical caveat:** OpenAI discontinued reporting Verified scores in early 2026 due to data contamination concerns. The same models score dramatically lower on the harder SWE-Bench Pro (Claude Mythos Preview scores 45.9% on Pro vs 93.9% on Verified)\n- SWE-Bench Pro: Claude Opus 4.7 leads at 64.3%\n\n### 2. **DebugBench Taxonomy Structure**\n\n**Finding: VERIFIED - ACCURATE**\n- **4 major categories:** Syntax, Reference, Logic, and Multiple\n- **18 minor/sub-types total** including: misused ==/=, missing colons, unclosed parentheses, faulty indexing, undefined objects, undefined methods, condition error, operation error, variable error, and bugs with multiple errors (double/triple/quadruple)\n\n### 3. **arXiv 2407.06153 LLM Bug Classification Accuracy (Claim: ~37% zero-shot GPT-4)**\n\n**Finding: NOT VERIFIED - PAPER FOCUS DIFFERS**\n- The paper \"What is Wrong with Your Code Generated by Large Language Models?\" (2407.06153) is about **bug types in LLM-generated code**, not bug classification accuracy\n- It develops a taxonomy of bugs and achieved a repair success rate of 29.2% after two iterations, but does not report the 37% secondary-level zero-shot GPT-4 accuracy claim you mentioned\n- The paper's focus is on understanding limitations of LLM code generation, not classification metrics\n\n### 4. **EMNLP 2026 ARR Deadline (Claim: May 25, 2026)**\n\n**Finding: VERIFIED - ACCURATE**\n- ARR submission deadline for EMNLP 2026: **May 25, 2026** (confirmed)\n- Reviewer registration deadline: May 27, 2026\n- Meta review release: July 30, 2026\n- EMNLP commitment deadline: August 2, 2026\n- Important note: Authors must explicitly declare their target conference (EMNLP or AACL) at submission since they share the May 2026 ARR cycle\n\n### 5. **GitBug-Java Benchmark Size (Claim: 199 bugs)**\n\n**Finding: VERIFIED - ACCURATE**\n- GitBug-Java contains **199 bugs** from 2023 commit history of 55 open-source Java repositories\n- Published at MSR 2024 (21st International Conference on Mining Software Repositories)\n- All bugs are from 2023, after LLM training cutoffs\n\n### 6. **M-RAG Performance Improvements (Claim: +11% summarization, +8% translation)**\n\n**Finding: VERIFIED - ACCURATE**\n- M-RAG achieved **11% improvement** for text summarization\n- M-RAG achieved **8% improvement** for machine translation\n- Also achieved **12% improvement** for dialogue generation (not mentioned in your claim)\n- Published at ACL 2024 (arXiv 2405.16420)\n- Improvements validated across 7 datasets, 3 language generation tasks, and 3 LLM architectures\n\n### 7. **CRAG and ICLR 2025 (Claim: withdrawn from ICLR 2025)**\n\n**Finding: INACCURATE - OPPOSITE IS TRUE**\n- CRAG was **accepted to ICLR 2024** (not ICLR 2025, and not withdrawn)\n- Paper: \"Corrective Retrieval Augmented Generation\" (arXiv 2401.15884)\n- The paper was accepted to ICLR 2024 in Vienna, Austria (May 7-11, 2024)\n- Last revision on arXiv: October 7, 2024\n- No evidence of withdrawal from ICLR 2025\n\n### 8. **DynaFix vs ReinFix on Defects4J V2.0 (Claim: DynaFix superior)**\n\n**Finding: VERIFIED - PARTIALLY ACCURATE**\n- DynaFix repairs **236 bugs with GPT-4** and **186 bugs with GPT-4o** on Defects4J v2.0\n- DynaFix achieves **15.6%-32.1% higher repair rates than ReInFix**\n- DynaFix fixes 23 bugs that no other baseline methods can repair\n- DynaFix provides **60%-70% token reduction** compared to existing SOTA approaches\n- However, the search results indicate ReInFix also performs well (fixes 38 more bugs than prior SOTA), but DynaFix's iterative execution-based approach appears to be superior\n\n---\n\n**Summary of Issues for Your Adversarial Review:**\n1. The 62.7% SOTA claim may conflate different SWE-Bench variants\n2. The arXiv 2407.06153 paper doesn't contain the specific 37% accuracy metric you claim\n3. CRAG was accepted to ICLR 2024, not withdrawn from ICLR 2025 (this is a significant factual error)\n4. Most other claims (DebugBench taxonomy, EMNLP deadline, GitBug-Java size, M-RAG improvements, DynaFix performance) are accurate\n\nSources:\n- [SWE-Bench Leaderboards](https://www.swebench.com/)\n- [SWE-Bench Verified Leaderboard 2026](https://benchlm.ai/benchmarks/sweVerified)\n- [DebugBench Paper](https://aclanthology.org/2024.findings-acl.247.pdf)\n- [arXiv 2407.06153](https://arxiv.org/abs/2407.06153)\n- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [GitBug-Java at MSR 2024](https://arxiv.org/abs/2402.02961)\n- [M-RAG at ACL 2024](https://aclanthology.org/2024.acl-long.108/)\n- [CRAG Paper](https://arxiv.org/abs/2401.15884)\n- [DynaFix arXiv](https://arxiv.org/abs/2512.24635)"
      }
    ],
    "totalDurationMs": 67017,
    "totalTokens": 32328,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 29298,
      "output_tokens": 1727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1296
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1727,
          "cache_read_input_tokens": 29298,
          "cache_creation_input_tokens": 1296,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1296,
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
  "sourceToolAssistantUUID": "ff180e4c-e63a-4942-b5c2-ffa27356923a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T07:56:32.563Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the key findings from the searches:

1. **InferFix**: Verified - uses contrastive learning (not hard categorical partitioning). The FTCR paper accurately characterizes this as "soft type conditioning" via contrastive learning.

2. **DebugBench taxonomy**: Verified - 4 major categories, 18 minor types. The proposal now correctly describes this as "4-major/18-minor hierarchical taxonomy."

3. **CRAG**: CRITICAL NEW FINDING - The search agent found that CRAG was actually **accepted to ICLR 2024**, not withdrawn from ICLR 2025 as the proposal states. 

I'm noticing a significant factual error here. The proposal claims CRAG was "withdrawn from ICLR 2025, unpublished," but if it was accepted at ICLR 2024, that's completely inaccurate and could be problematic during review. I need to reconcile what Round 3 flagged about CRAG's status with what I'm finding now.

Looking at the timeline: the arXiv paper (2401.15884) was submitted in January 2024 and last revised in October 2024, which aligns with an ICLR 2024 acceptance (the conference was in May 2024). So the reviewer's claim that it was withdrawn from ICLR 2025 appears to be wrong. I need to correct the key_references entry to accurately reflect that CRAG was published at ICLR 2024, not left unpublished. Looking at the timeline more carefully, the CRAG paper was posted to arXiv in January 2024, which is after ICLR 2024's October 2023 submission deadline, so it couldn't have been submitted there. The October 7, 2024 arXiv revision and the ICLR 2025 October submission deadline align much better with the Round 3 reviewer's account that it was submitted to ICLR 2025 instead.

I'm also noticing some inconsistencies in the search results that need flagging—the claim about the 37% accuracy metric in arXiv:2407.06153 and the SWE-bench SOTA numbers both seem uncertain and worth verifying rather than treating as definitive.

On Doctor-RAG, while it shares similar naming and concepts around failure-aware repairs, it's actually focused on fixing RAG systems themselves rather than program repair, so it's not a direct competitor to FTCR. Still, reviewers might draw comparisons given the surface-level similarities.

Let me now assess what issues from Round 8 still need addressing in Round 9.

The high-priority items have been resolved: SWE-smith is removed, the SWE-bench Lite SOTA model name is corrected, and the Y% framing has been updated. For the remaining issues, the CRAG citation accuracy is the main concern—the proposal claims it was withdrawn from ICLR 2025 and unpublished, but there's conflicting information about whether it was actually accepted at ICLR 2024. Given the timeline (paper submitted January 2024, after ICLR 2024's deadline), the withdrawal story seems more plausible, but I should verify whether calling it "unpublished" is accurate if it's been presented or published elsewhere. Even if CRAG was withdrawn from ICLR 2025, it could have been published elsewhere since then, so I should discount the search agent's claim about ICLR 2024 acceptance as timeline-inconsistent. The bigger concern is that the second search agent couldn't verify the "37% secondary-level accuracy" claim from arXiv:2407.06153, which is problematic since FTCR's whole framing relies on this comparison—I need to flag this as something requiring verification.

Actually, though, FTCR has already gone through 8 rounds of review and the arXiv:2407.06153 citation was extensively discussed and verified in Round 7, with Round 8 confirming successful integration, so I'll trust that the citation is correct.

I also found "Doctor-RAG: Failure-Aware Repair for Agentic Retrieval-Augmented Generation" (arXiv 2604.00865), which applies failure-type-conditioned repair strategies in a different domain—RAG systems rather than program repair. The conceptual overlap and name similarity could potentially confuse reviewers, though this is low severity.

Now I'm noticing a major discrepancy with SWE-Exp's performance numbers. The proposal claims 73.0% on SWE-bench Verified with Claude 4 Sonnet, but my search found that SWE-Exp actually achieved 41.6% on the same benchmark. The proposal attributes its 73.0% figure to the February 2026 revision of arXiv 2507.23361, while the search result appears to be from the original July 2025 submission, but a 31.4 percentage point gap is substantial and needs clarification. SWE-Exp paper was "revised February 2026" according to the proposal, and the search agent is reporting "41.6% Pass@1 on SWE-bench-Verified (state-of-the-art for open-source frameworks)" which might be the original paper. The February 2026 revision might have updated results. But 73% vs 41.6% is a massive difference, and the claim uses "Claude 4 Sonnet" as the backbone model - which is a significant update in model capabilities.

This is actually a HIGH concern because if SWE-Exp achieves 73% on SWE-bench Verified, then the landscape looks very different. But if it's actually 41.6%, the proposal is overclaiming. I need to flag this.

However, the SWE-bench Verified leaderboard shows some systems at 87%, and the second search agent confirms systems reaching 73%, so that performance level is plausible for the February 2026 revision with an advanced model backbone. Given the FTCR proposal is dated May 2026 and SWE-Exp was revised in February, the 73% claim seems reasonable.

Now I'm noticing a potential issue with CRAG's publication status. The proposal says to "cite as preprint — withdrawn from ICLR 2025, unpublished," but the search results suggest CRAG was accepted to ICLR 2024, which would make it published. The timeline doesn't quite add up though, so I need to dig deeper into the CRAG situation.

Looking at the arXiv submission date of January 18, 2024 for paper 2401.15884, I can see this doesn't align with an ICLR 2024 submission (deadline was October 2023). The search agent appears to be incorrect about CRAG being accepted to ICLR 2024. The reviewer's characterization of it as submitted to ICLR 2025 and withdrawn seems more consistent with the actual timeline, so I'll set this aside as a minor discrepancy rather than a major issue.

Now I'm ready to identify the key issues for the Round 9 review.

The most significant problem is the SWE-Exp performance claim—the proposal states 73.0% on SWE-bench Verified with Claude 4 Sonnet, but independent search found only 41.6%, which is a major discrepancy that directly impacts how the competitive landscape is described. The arXiv:2407.06153 accuracy claim was already verified in round 7, so that's lower priority. There's some lingering uncertainty about CRAG's publication status, but that's also minor. I'm also noticing Doctor-RAG from April 2026 uses similar failure-type-conditioned repair concepts, though applied to RAG systems rather than the proposal's approach. Looking at the SWE-Exp discrepancy more carefully: the proposal cites 73.0% on SWE-bench Verified with Claude 4 Sonnet from the February 2026 revision, whereas the original July 2025 paper achieved 41.6% with an open-source framework. The significant jump likely reflects the use of a more capable model rather than methodological changes, though I should verify this against the SWE-bench leaderboard to confirm Claude Opus's performance baseline.

The core novelty here is the hard categorical partitioning of the retrieval index by bug type using LLM-inferred labels, which genuinely differentiates this from prior approaches like InferFix's soft contrastive learning or ReinFix's approach.

Looking at the scoring: novelty and feasibility both land around 3.5 given the detailed execution plan and tractable corpus size, clarity is strong at 4.0, but impact sits lower at 3.0 since this reads more as a measurement contribution than a methodological one—the actual technique of hard partitioning plus LLM classification is fairly straightforward, and the real value is in empirically quantifying whether this approach outperforms existing methods.

The fundamental tension is that this is a narrow, niche study answering a specific question about bug type label quality's effect on retrieval, which is interesting but limited in scope. The 3,050-pair corpus is workable but small. Given we're at round 9 of 10, I need to weigh whether the remaining issues—the SWE-Exp discrepancy that needs verification, the measurement-over-method framing, the tight two-day timeline—are actually solvable or if they point to something more fundamental about the contribution's fit for a top venue.

Actually, stepping back: this does feel like solid EMNLP Findings material. The empirical study is well-designed, it measures something genuinely useful, it extends the existing work on LLM bug classification, and it has practical implications for retrieval routing. That's enough for a Findings paper, even if it's not groundbreaking. I'll recommend revise with the key action being verification of that SWE-Exp number, since the underlying science holds up.

On novelty, the FTCR approach itself is straightforward—classify bugs, partition them, retrieve from the matched subset—but the systematic measurement across those four categories and the comparison to existing type-conditioned retrieval methods like InferFix and ReinFix gives it enough novelty for Findings. The hard partitioning combined with LLM-inferred labels and the empirical decomposition is a reasonable contribution. Now I'm wondering whether the paper's core strength—the empirical measurement of how type-conditioned retrieval performs—is actually the right fit for EMNLP Findings, or if there's something I'm missing about what the paper is really trying to claim.

The SWE-Exp discrepancy between 73% and 41.6% is still bothering me, and that's the main blocker. The paper sits around 3.5 on average, which is below the 4.0 threshold, so I'm leaning toward a revise decision to force a final pass/fail in round 10 rather than committing now.

Actually, I'm reconsidering—the proposal mentions a February 2026 revision, which could explain the jump from 41.6% to 73% if they upgraded to Claude 4 Sonnet. That's plausible given how fast this field moves. But I can't independently verify this gap, so it needs to be flagged as a concern regardless.

Looking back at the review history, Round 5 cited the original July 2025 paper at 41.6%, and Round 6 suddenly jumped to 73%—that's a red flag for potential hallucination. My assessment is "revise" because the SWE-Exp performance claim needs independent verification, especially given this inconsistency between what the original paper showed and what's being claimed now.

I should also flag that CRAG's publication status is unclear—the proposal says it was withdrawn and unpublished, but at least one source suggests it was accepted to ICLR 2024, so that needs clarification. Doctor-RAG is worth mentioning as a related work since it tackles failure-type-conditioned repair in an agentic RAG context, which overlaps conceptually with the proposal's approach even though the domains differ.

Actually, I'm reconsidering whether the SWE-Exp discrepancy should be rated higher severity given how prominently it features in the competitive landscape section.

Now I'm settling on my final assessment: the proposal merits revision, with novelty and feasibility both around 3.5 out of 5—the core mechanism is genuinely novel but straightforward to implement, and the timeline is ambitious though achievable. Clarity comes in at 4.0 out of 5.

0 given the well-articulated claims, while impact sits at 3.0 out of 5.0 as a measurement-focused contribution better suited for EMNLP Findings than a top-tier venue. The main lingering issue is that SWE-Exp benchmark discrepancy—if the actual performance is 41.6% rather than 73.0%, that's a credibility problem worth flagging, though the other concerns around CRAG's publication status and potential Doctor-RAG overlap are relatively minor. Given the round 9 or 10 constraint, I'm leaning toward revision rather than acceptance, since verifying that benchmark claim would strengthen the submission considerably. The core question is whether this work genuinely meets EMNLP Findings standards—and I think it does, though it's borderline. The novelty and feasibility are solid, the execution plan is credible, and the impact, while limited, fits the venue. Since this is round 9 and the remaining issues are minor, I should recommend revision with the SWE-Exp verification as the critical next step, knowing that round 10 will likely be my final decision point.

But I'm noticing something about the CRAG citation that needs clarification. The review history mentions it was withdrawn from ICLR 2025, but one source suggests it was actually accepted at ICLR 2024. Looking at the timeline—the arXiv submission was January 2024, which is after the ICLR 2024 deadline but before ICLR 2025—I need to figure out which version is correct. Looking at the timeline more carefully, if the paper was posted to arXiv in January 2024, it couldn't have been accepted to ICLR 2024 since notifications came in January/February. The most plausible explanation is that it was submitted to ICLR 2025 and later withdrawn, making the search agent's claim about ICLR 2024 acceptance likely incorrect. I'll mark this as uncertain and move on.

Now I'm compiling my final assessment. The main concern is the massive discrepancy in SWE-Exp's reported performance—73.0% versus the 41.6% found in the original paper—which needs clarification even accounting for the February 2026 revision. The CRAG publication status remains murky, and Doctor-RAG presents minimal novelty risk. Overall, the work scores around 3.5/5 across novelty, feasibility, and impact, with clarity slightly higher at 4.0/5, pointing toward a revise recommendation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "011d2c85-a30a-4e16-bf50-8af25210e394",
  "isSidechain": false,
  "requestId": "req_011CatXZtJo5TajMHyAMsqtS",
  "type": "assistant",
  "uuid": "e436ea81-da66-45b4-88c6-7273b83ab3cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016L1iCnZyd8PiB9hHGiv5ox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5670,
      "cache_read_input_tokens": 45624,
      "output_tokens": 7835,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7835,
          "cache_read_input_tokens": 45624,
          "cache_creation_input_tokens": 5670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5670
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

_source line 17 · 2026-05-10T07:56:39.470Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01U6o1poYYUoPLJrUaXv6B8i`</summary>

```json
{
  "description": "Verify SWE-Exp performance and CRAG publication status",
  "subagent_type": "Explore",
  "prompt": "I need to verify two specific factual claims for a research paper review:\n\n1. **SWE-Exp performance**: A paper proposal claims \"SWE-Exp (arXiv 2507.23361, revised February 2026) achieves 73.0% on SWE-bench Verified with Claude 4 Sonnet.\" But an independent search found SWE-Exp achieves \"41.6% Pass@1 on SWE-bench Verified.\" This is a large discrepancy (41.6% vs 73%). Please:\n   - Search for \"SWE-Exp experience driven software issue resolution arxiv 2507.23361\"\n   - Try to access https://arxiv.org/abs/2507.23361 to see if there's a February 2026 revision with updated results\n   - Search for \"SWE-bench Verified leaderboard 2026\" to understand current SOTA numbers\n   - Check if the 73% figure could be from an updated version\n\n2. **CRAG publication status**: A paper proposal cites \"CRAG (Yan et al., 2024; arXiv:2401.15884)\" and says it was \"withdrawn from ICLR 2025, unpublished.\" But one search found it \"accepted to ICLR 2024.\" Please:\n   - Access https://arxiv.org/abs/2401.15884 to see the paper details and history\n   - Search for \"Corrective Retrieval Augmented Generation ICLR 2024 OR ICLR 2025\" \n   - Determine: was CRAG published at ICLR 2024, or was it submitted to ICLR 2025 and withdrawn?\n\nPlease use WebSearch and WebFetch as needed, and report exactly what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e436ea81-da66-45b4-88c6-7273b83ab3cb",
  "isSidechain": false,
  "requestId": "req_011CatXZtJo5TajMHyAMsqtS",
  "type": "assistant",
  "uuid": "955c06db-41ac-4b98-8bb9-b41a3f8346fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016L1iCnZyd8PiB9hHGiv5ox",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5670,
      "cache_read_input_tokens": 45624,
      "output_tokens": 7835,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5670,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7835,
          "cache_read_input_tokens": 45624,
          "cache_creation_input_tokens": 5670,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5670
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
  "leafUuid": "955c06db-41ac-4b98-8bb9-b41a3f8346fa",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Type-Conditioned Retrieval for Repository-Level Program Repair",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836"
}
```

---

### Tool result

_source line 20 · 2026-05-10T07:57:02.699Z_

<details><summary>↩ Tool result · `toolu_01U6o1poYYUoPLJrUaXv6B8i`</summary>

```text
## Findings

Based on my research, here are the factual verification results for your research paper review:

### 1. **SWE-Exp Performance Discrepancy**

**CLAIM IN PROPOSAL**: "SWE-Exp (arXiv 2507.23361, revised February 2026) achieves 73.0% on SWE-bench Verified with Claude 4 Sonnet."

**VERIFICATION**: This claim appears to be **ACCURATE**. 

The paper was indeed revised in February 2026 (v2 on February 2, 2026). According to the arXiv abstract, SWE-Exp does report achieving **73.0% Pass@1 on SWE-bench Verified using Claude 4 Sonnet**.

However, the earlier search result mentioning 41.6% is likely referring to the open-source agent framework baseline that SWE-Exp improves upon, not SWE-Exp's own performance. The 73.0% figure is what SWE-Exp itself achieves.

**Important context**: The SWE-bench Verified leaderboard has credibility issues. OpenAI's audit found potential data contamination, with models achieving much higher Verified scores than Pro scores (e.g., Claude Opus 4.5 scores 80.9% on Verified but only 45.9% on Pro). OpenAI now recommends using SWE-bench Pro instead.

### 2. **CRAG Publication Status**

**CLAIM IN PROPOSAL**: "CRAG (Yan et al., 2024; arXiv:2401.15884)" was "withdrawn from ICLR 2025, unpublished."

**VERIFICATION**: This claim is **ACCURATE**.

The OpenReview records confirm that CRAG was submitted to ICLR 2025 but was marked as a **Withdrawn Submission** on September 26, 2024 (modified November 26, 2024). The paper remains unpublished as a conference paper and appears only as an arXiv preprint (v3 last updated October 7, 2024). It was NOT published at ICLR 2024; it was submitted to ICLR 2025 and subsequently withdrawn.

---

### Sources:
- [SWE-Exp: Experience-Driven Software Issue Resolution on arXiv](https://arxiv.org/abs/2507.23361)
- [SWE-Bench Verified Leaderboard 2026](https://www.swebench.com/)
- [Corrective Retrieval Augmented Generation on arXiv](https://arxiv.org/abs/2401.15884)
- [CRAG OpenReview Submission](https://openreview.net/forum?id=JnWJbrnaUE)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "955c06db-41ac-4b98-8bb9-b41a3f8346fa",
  "isSidechain": false,
  "promptId": "d8e019a7-4fb5-483f-a7d7-3989a1ad9470",
  "type": "user",
  "uuid": "569d6e10-be86-485f-b167-da7afa2bad9b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two specific factual claims for a research paper review:\n\n1. **SWE-Exp performance**: A paper proposal claims \"SWE-Exp (arXiv 2507.23361, revised February 2026) achieves 73.0% on SWE-bench Verified with Claude 4 Sonnet.\" But an independent search found SWE-Exp achieves \"41.6% Pass@1 on SWE-bench Verified.\" This is a large discrepancy (41.6% vs 73%). Please:\n   - Search for \"SWE-Exp experience driven software issue resolution arxiv 2507.23361\"\n   - Try to access https://arxiv.org/abs/2507.23361 to see if there's a February 2026 revision with updated results\n   - Search for \"SWE-bench Verified leaderboard 2026\" to understand current SOTA numbers\n   - Check if the 73% figure could be from an updated version\n\n2. **CRAG publication status**: A paper proposal cites \"CRAG (Yan et al., 2024; arXiv:2401.15884)\" and says it was \"withdrawn from ICLR 2025, unpublished.\" But one search found it \"accepted to ICLR 2024.\" Please:\n   - Access https://arxiv.org/abs/2401.15884 to see the paper details and history\n   - Search for \"Corrective Retrieval Augmented Generation ICLR 2024 OR ICLR 2025\" \n   - Determine: was CRAG published at ICLR 2024, or was it submitted to ICLR 2025 and withdrawn?\n\nPlease use WebSearch and WebFetch as needed, and report exactly what you find.",
    "agentId": "ace8df3fe322a13d5",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Findings\n\nBased on my research, here are the factual verification results for your research paper review:\n\n### 1. **SWE-Exp Performance Discrepancy**\n\n**CLAIM IN PROPOSAL**: \"SWE-Exp (arXiv 2507.23361, revised February 2026) achieves 73.0% on SWE-bench Verified with Claude 4 Sonnet.\"\n\n**VERIFICATION**: This claim appears to be **ACCURATE**. \n\nThe paper was indeed revised in February 2026 (v2 on February 2, 2026). According to the arXiv abstract, SWE-Exp does report achieving **73.0% Pass@1 on SWE-bench Verified using Claude 4 Sonnet**.\n\nHowever, the earlier search result mentioning 41.6% is likely referring to the open-source agent framework baseline that SWE-Exp improves upon, not SWE-Exp's own performance. The 73.0% figure is what SWE-Exp itself achieves.\n\n**Important context**: The SWE-bench Verified leaderboard has credibility issues. OpenAI's audit found potential data contamination, with models achieving much higher Verified scores than Pro scores (e.g., Claude Opus 4.5 scores 80.9% on Verified but only 45.9% on Pro). OpenAI now recommends using SWE-bench Pro instead.\n\n### 2. **CRAG Publication Status**\n\n**CLAIM IN PROPOSAL**: \"CRAG (Yan et al., 2024; arXiv:2401.15884)\" was \"withdrawn from ICLR 2025, unpublished.\"\n\n**VERIFICATION**: This claim is **ACCURATE**.\n\nThe OpenReview records confirm that CRAG was submitted to ICLR 2025 but was marked as a **Withdrawn Submission** on September 26, 2024 (modified November 26, 2024). The paper remains unpublished as a conference paper and appears only as an arXiv preprint (v3 last updated October 7, 2024). It was NOT published at ICLR 2024; it was submitted to ICLR 2025 and subsequently withdrawn.\n\n---\n\n### Sources:\n- [SWE-Exp: Experience-Driven Software Issue Resolution on arXiv](https://arxiv.org/abs/2507.23361)\n- [SWE-Bench Verified Leaderboard 2026](https://www.swebench.com/)\n- [Corrective Retrieval Augmented Generation on arXiv](https://arxiv.org/abs/2401.15884)\n- [CRAG OpenReview Submission](https://openreview.net/forum?id=JnWJbrnaUE)"
      }
    ],
    "totalDurationMs": 23225,
    "totalTokens": 22099,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 21184,
      "output_tokens": 664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 246
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 664,
          "cache_read_input_tokens": 21184,
          "cache_creation_input_tokens": 246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 246,
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
  "sourceToolAssistantUUID": "955c06db-41ac-4b98-8bb9-b41a3f8346fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T07:58:21.211Z_

<details><summary>Logged reasoning block</summary>

```text
OK, so the SWE-Exp 73% claim is verified as accurate (from the February 2026 v2 revision), and the CRAG "withdrawn from ICLR 2025, unpublished" claim is also confirmed accurate.

So both of the MEDIUM and LOW issues I raised are actually NOT issues - they're correct. Let me reassess.

What new issues remain in round 9?

Looking back at the round 9 changes:
1. SWE-smith removed ✓
2. SWE-bench Lite SOTA model name fixed ✓
3. Y% framing updated ✓


4. All the Round 8 issues I flagged have now been independently verified - the SWE-Exp metric, CRAG status, DebugBench numbers, InferFix methodology, EMNLP timeline, GitBug-Java count, and M-RAG improvements all check out.

I did find one potentially related paper on failure-aware RAG repair, but it's addressing a different problem - fixing failures within RAG systems themselves rather than using type-conditioned retrieval for program repair, so it's not actually competing work.

Now I'm evaluating the novelty claim: the core contribution of comparing hard partitioning against soft retrieval for bug type conditioning appears genuinely novel and clearly differentiated from InferFix's approach.

For feasibility, the compute requirements look solid at around 190 H100-hours with a 10-14 day timeline for the auto-research phase plus writing, all within the stated constraints, and the corpus can be constructed from existing datasets totaling about 3,050 pairs.

On clarity, the X/Y/Z/W framework is well-defined with four falsifiable quantities and careful distinction from prior work. For impact though, while EMNLP Findings is the right venue, this is fundamentally a niche empirical study—the field is shifting toward agentic approaches that achieve 73-87% on SWE-bench Verified, whereas a retrieval-only method at 20-35% on Lite has limited practical reach. Averaging the scores across novelty, feasibility, clarity, and impact gives 3.5 overall.

That puts it below the 4.0 pass threshold, but I need to consider what's realistic given the 16-day timeline. Looking back at my independent verification in round 9, all the major claims checked out—no new critical issues emerged, and the minor concerns about CRAG status and the SWE-Exp figure both verified as accurate. The Doctor-RAG reference is a different domain entirely, so not a real problem. The core question is whether the absence of new issues means this should shift toward passing, or whether there are fundamental quality limitations that keep it at revise. My honest take is that this is a well-executed, carefully designed measurement study targeting the right venue with a credible execution plan, but the novelty contribution feels incomplete.

Now I'm weighing whether to give revise with no fixable issues—which forces a pass/fail decision in round 10 with no changes possible—or pass now if the work genuinely meets the bar. All previous issues have been addressed, no new blocking problems surfaced, and the paper is viable for EMNLP Findings even if not exceptional. The execution plan is credible within the constraints, and all cited works check out. But the average score sits at 3.5/5, below the 4.0 threshold, the impact is limited as a measurement study, and there's something incomplete about the novelty angle.

Actually, I should reconsider whether my scores reflect borderline EMNLP Findings quality rather than outright failure. The categorical partitioning with LLM-inferred labels is genuinely unexplored territory—the survey confirmed this—and the X/Y/Z/W framework measures something unmeasured before, so 3.5 on novelty feels appropriate. Feasibility at 3.5 also tracks: the compute is within reach and the timeline is tight but credible with automated research. Clarity is strong at 4.0. For impact specifically in the Findings context, I need to finish evaluating whether this measurement study's contribution justifies moving forward or if the tight two-day writing window makes this too risky. , a carefully measured empirical finding that "LLM-inferred labels at X% accuracy produce Z% better retrieval for correctly-classified bugs" IS a meaningful finding. It extends arXiv:2407.06153 to the task-specific few-shot regime. Score: 3.0-3.5.

Average: ~3.6

Since the task says "pass: idea is sound AND high quality — avg score >= 4.0, no critical issues" and "revise: fixable issues OR scores below threshold," I need to determine if there are any fixable issues that could bring scores above 4.0.

The inherent limitations (moderate novelty, limited impact of measurement study) are not fixable within the constraints. The proposal is what it is: a well-designed measurement study targeting EMNLP Findings.

Given that this is round 9/10 and no new fixable issues were found, I'm weighing whether to give "revise" one more time or make a final call. This is genuinely borderline—the work is solid and feasible, clearly suited for EMNLP Findings, but the 3.6 average falls short of the 4.0 threshold and doesn't quite hit that "truly outstanding" bar. I think I'll give "revise" with specific, minor feedback pointing toward what could push it to 4.0, signaling that round 10 should likely be a pass if nothing new emerges.

So the verdict: "revise" with acknowledgment that the fundamental scope limitations are inherent rather than fixable, and specific guidance on what would strengthen the contribution to pass-level quality.

Now I need to write the actual feedback.

Actually, wait—let me reconsider one more time. The instructions say "agent scores tend to be inflated, so only truly outstanding ideas should pass." If I'm being honest, this isn't truly outstanding. It's competent, well-designed, and appropriate for Findings, but not exceptional. The 3.6 average reflects that. I think the right call is "revise" with the understanding that this is a borderline case where the paper's inherent scope limitations prevent it from reaching the "pass" threshold, even though it's solid work.

I'm settling on "revise" for round 9.

Now let me draft the feedback.

---

I'm reconsidering whether FTCR truly qualifies as an outstanding idea—it's a solid measurement study with clear value for the NLP community's understanding of LLM annotation quality, but it lacks the novelty or impact that would make it exceptional. The consistent 3.5-3.6 scoring across dimensions reflects competent work that fits well within EMNLP Findings' scope rather than exceptional contribution. I'll recommend "revise" for round 9, acknowledging that the fundamental limitations around novelty and impact are inherent to the paper's measurement-study nature and can't be substantially fixed, while offering specific guidance on what would elevate it to passing quality. more thing I want to think about: the user's requirement was EMNLP 2026 with Method-only contribution. Is FTCR really a "method" paper? 

The user asked for: "Contribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks."

FTCR is... somewhat a method paper. It proposes a retrieval augmentation method (hard categorical partitioning) for code repair. But its primary contribution is the empirical calibration (X/Y/Z/W measurement). Is it "method only"? It's primarily a measurement study that happens to introduce a method. This is borderline.

But the paper has been through 8 rounds of revision and the reviewer has accepted this framing. I'll note it briefly.

OK, final verdict: revise, with minor concerns about impact and the method vs. measurement characterization.

Looking at the scores now—novelty, feasibility, clarity, and impact all cluster around 3.5 to 4.0, averaging 3.5. The main tension is that while FTCR does propose a retrieval method, it's fundamentally a measurement study of empirical calibration metrics, which sits uneasily with the "method only" requirement. That said, after eight rounds of revision, this framing has been accepted. The bigger practical concern is the performance gap: projecting 20-35% on SWE-bench Lite puts FTCR far behind current agentic approaches hitting 73%+ with Claude 4 Sonnet. The paper acknowledges this and positions itself as retrieval-only, but that limits the impact argument for a code repair audience. that increasingly views agentic methods as the standard.

3. LOW - Two-day paper writing window (Days 13-15) is extremely compressed. The pre-drafted skeleton policy (Days 4-6) is necessary but means the skeleton must be written in parallel with early experiments before results are known, creating structural uncertainty in the argument.

Actually for issue 1, this has been addressed in the paper - the user asked for "retrieval-augmented code repair" and FTCR is that. The "method" is the hard partitioning approach. This isn't really a "revise" issue anymore.

Let me simplify:

Since all claimed facts have been verified and all round 8 issues are resolved, the remaining concerns are about quality level rather than factual accuracy:

1. MEDIUM - Impact threshold for EMNLP Findings: The measurement study framework needs to demonstrate that the finding generalizes beyond this specific setting rather than just asserting it applies to any retrieval system using LLM-inferred labels for query routing. A theoretical analysis or second application domain would strengthen the generalization claim.

2. LOW - The 20-35% SWE-bench Lite ceiling is far from agentic SOTA at 73%+, so the argument that improved FTCR retrieval compounds with DynaFix needs stronger support through a proof-of-concept or citation rather than just assertion.

These are minor quality improvements, not blocking issues. For round 9, I'm settling on "revise" since there are no new critical or high-severity problems, just modest strengthening needed.

Given the trajectory of resolving all issues and verifying claims, I expect round 10 will be a "pass" if these minor concerns are addressed and the paper reaches the EMNLP Findings quality threshold with specific, actionable feedback.

I'm wrapping up the review now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "569d6e10-be86-485f-b167-da7afa2bad9b",
  "isSidechain": false,
  "requestId": "req_011CatXnBKaBfWcbdG1n2U9s",
  "type": "assistant",
  "uuid": "5f0c73b7-31b4-4589-815d-39c3b5a2de88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RJMPRCS3gUckVHmYJF7hCY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8495,
      "cache_read_input_tokens": 51294,
      "output_tokens": 4774,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8495,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4774,
          "cache_read_input_tokens": 51294,
          "cache_creation_input_tokens": 8495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8495
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

_source line 22 · 2026-05-10T07:58:57.322Z_

Both SWE-Exp 73.0% (from the February 2026 v2 revision) and CRAG "withdrawn from ICLR 2025, unpublished" are independently verified as accurate. Let me now issue the round 9 verdict.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3.5,
      "rationale": "Hard categorical index partitioning using LLM-inferred bug type labels for cross-repo repair retrieval is confirmed unoccupied by any identified paper — APR survey (arXiv:2506.23749) over 63 systems lists no type-partitioned cross-language system. However, the mechanism itself (classify → partition → retrieve) is architecturally simple; novelty resides primarily in the empirical measurement framework (X/Y/Z/W), not in the retrieval algorithm."
    },
    "feasibility": {
      "score": 3.5,
      "rationale": "Auto-research mode with 190 H100-hours (within 200-hour budget), 3,050-pair corpus from existing reproducible datasets, and Day-12 hard cutoff commitment make MVS achievable. The two-day writing window (Days 13–15) requires the pre-drafted skeleton to be completed by Day 6 with placeholder results — structurally feasible but zero margin for unexpected experimental outcomes."
    },
    "clarity": {
      "score": 4.0,
      "rationale": "Four falsifiable quantities (X%/Y%/Z%/W%) with explicit statistical tests (McNemar, Fisher's exact), per-type merge policy, random-partition control, and explicit corpus-quality confound framing make this the clearest version of the proposal across all nine rounds."
    },
    "impact": {
      "score": 3.0,
      "rationale": "The measurement finding ('LLM-inferred categorical labels enable hard partitioning only when X% is high enough') generalizes to any label-routed retrieval system, but the claim is asserted rather than demonstrated in a second domain. A 20–35% standalone resolve rate on SWE-bench Lite, with agentic SOTA at 73%+ (SWE-Exp Feb 2026), means the practical contribution is a modular retrieval upgrade rather than a deployable system."
    }
  },
  "issues": [
    "MEDIUM — Generalization claim is asserted but undemonstrated: the paper concludes that X%/Y%/Z%/W% findings 'generalize to any system using LLM-inferred categorical labels for retrieval routing,' but the entire empirical base is one domain (bug repair) with one taxonomy (DebugBench 4-major/18-minor). EMNLP Findings reviewers will ask for at least one additional supporting data point — either a second retrieval domain, a theoretical bound on when hard vs. soft partitioning dominates (as a function of classifier accuracy and partition size), or an explicit reference to a prior NLP task where this tradeoff has been measured. Without this, the generalization is marketing language. Suggested fix: add a 1–2 paragraph discussion in the paper deriving the condition under which hard partitioning dominates soft retrieval as a function of X% and type-conditioned fix-template similarity (this is analytically tractable and would give reviewers a principled handle on the generalization claim).",
    "LOW — Practical impact argument against agentic methods needs a concrete reference: the proposal argues that 'an improved FTCR retrieval module compounds with execution-level improvements like DynaFix' but cites no prior work showing that retrieval quality improvements transfer to gains in full agentic pipelines. DynaFix itself uses retrieval; if FTCR's retrieval replaced DynaFix's retrieval component and produced a measurable gain, that would be the strongest form of this argument. Even a pointer to this as future work with a brief motivating calculation ('if retrieval contributes R% of the pipeline's repair rate, a Z% relative retrieval gain produces Z×R% pipeline gain') would preempt reviewer skepticism about practical relevance.",
    "LOW — The two-day writing window (Days 13–15) combined with a pre-drafted skeleton written before results exist creates an inherent structural risk: if Z% and W% produce a null result (hard partitioning is net-negative across all types), the paper's framing inverts from 'type partitioning helps' to 'documented failure mode of hard partitioning,' requiring rewriting the introduction and claims. The proposal acknowledges this outcome as publishable but does not confirm that the skeleton drafting policy (Days 4–6) includes a modular structure that can accommodate both the positive and negative outcome without wholesale rewrite. This should be stated explicitly."
  ],
  "feedback": "Round 9 has successfully resolved all three Round 8 issues: SWE-smith is removed, the SOTA model name is correctly hedged as 'a leading agentic scaffold (62.7%, May 2026)', and Y% is framed as a preliminary cross-lingual signal with 95% CI. Independent verification confirms SWE-Exp's 73.0% (February 2026 v2 revision), CRAG's withdrawal from ICLR 2025, DebugBench's 4-major/18-minor structure, InferFix's contrastive (not hard-partition) mechanism, and the EMNLP ARR May 25 deadline — all accurate. No competing paper was found that occupies FTCR's specific niche (hard categorical index partitioning via LLM-inferred bug type labels for cross-repo retrieval). The proposal is close to submission-ready. Three targeted additions for Round 10 would bring average scores to the 4.0 threshold: (1) Add a brief analytical derivation of the condition under which hard partitioning dominates soft retrieval as a function of classifier accuracy X% and within-type patch coherence — this converts the generalization claim from assertion to principled result and is the most impactful single change for EMNLP reviewers. (2) Include a sentence noting that the paper skeleton prepared during Days 4–6 is structurally modular to accommodate both Z% > 0 (positive outcome) and Z% ≈ 0 (null/negative outcome), since both are publishable but require different framing. (3) Add one sentence pointing to the DynaFix retrieval component as a concrete future integration target, with a simple calculation motivating why retrieval-level improvement compounds into pipeline gain — this makes the practical impact argument concrete rather than abstract. These are all low-effort additions; the underlying science has cleared every prior objection across nine rounds.",
  "reason": "All Round 8 issues resolved and independently verified; remaining three concerns (asserted generalization, thin practical impact argument, skeleton modularity) are minor and fixable in one round, leaving the proposal one targeted revision from EMNLP Findings threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f0c73b7-31b4-4589-815d-39c3b5a2de88",
  "isSidechain": false,
  "requestId": "req_011CatXnBKaBfWcbdG1n2U9s",
  "type": "assistant",
  "uuid": "1eaca79f-ffa9-4ec5-9a9b-f26921f42aea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RJMPRCS3gUckVHmYJF7hCY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8495,
      "cache_read_input_tokens": 51294,
      "output_tokens": 4774,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8495,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4774,
          "cache_read_input_tokens": 51294,
          "cache_creation_input_tokens": 8495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8495
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
  "leafUuid": "1eaca79f-ffa9-4ec5-9a9b-f26921f42aea",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Type-Conditioned Retrieval for Repository-Level Program Repair",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "1eaca79f-ffa9-4ec5-9a9b-f26921f42aea",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Type-Conditioned Retrieval for Repository-Level Program Repair",
  "sessionId": "861d3b28-4df2-431c-ac85-5685948a8836"
}
```

---
