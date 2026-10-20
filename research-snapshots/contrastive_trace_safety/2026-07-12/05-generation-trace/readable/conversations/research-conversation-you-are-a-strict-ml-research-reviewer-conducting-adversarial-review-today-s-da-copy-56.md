# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/49a4fdd9-9f29-4597-b21f-1decd19e6826.jsonl`
- **Structured JSON:** [`6838c9d3ab4bff709698.json`](../../sessions/68/6838c9d3ab4bff709698.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T06:43:43.344Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T06:43:43.344Z",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 6/10)\n{\n  \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\",\n  \"core_problem\": \"The lead empirical question — tractable because DebugBench provides oracle ground-truth labels for 4,253 instances — is: how accurately can a few-shot LLM assign semantic bug type labels from an 18-category taxonomy, and does that label accuracy determine whether hard categorical retrieval index partitioning outperforms soft root-cause-augmented retrieval (ReinFix, ICSE 2026) for cross-repository fix template transfer? This frames FTCR as an empirical study of LLM-generated categorical label quality and its downstream retrieval impact, yielding four falsifiable quantities: (X%) few-shot classifier accuracy vs. DebugBench ground-truth oracle labels; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type-partitioned retrieval vs. the soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts — a finding with direct generalization to any retrieval system using LLM-inferred labels.\\n\\nRetrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. InferFix (ESEC/FSE 2023, arXiv:2303.07263) establishes that type-aware retrieval benefits code repair by using contrastive-learned embeddings over Infer's static-analysis-derived bug type annotations, but its type signal remains a soft continuous embedding feature — retrieval is still nearest-neighbor search across a unified corpus, not hard index-construction partitioning. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is whether hard categorical type partitioning of the retrieval index outperforms both InferFix's soft contrastive type conditioning and ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer, particularly in a multi-language setting. An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. Type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and become analytical contributions when addressed directly: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across 18 types yields only ~31 Java instances per type on average, requiring an explicit minimum-threshold and merge policy for rare types; and (2) classifier error propagation — when an incoming bug is misclassified, hard partitioning underperforms soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback — turns potential weaknesses into the core empirical variables (Z% and W%) that define the paper's scientific contribution.\",\n  \"opportunity\": \"ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-aware cross-repository retrieval system for code repair: its Retriever is pretrained via contrastive learning to bring semantically equivalent bugs and their fixes closer in embedding space, conditioned on Infer's static-analysis-derived bug type annotations (null dereferences, resource leaks, thread-safety violations), and achieves 76.8% top-1 accuracy on Java and 65.6% on C#. Three properties distinguish InferFix from FTCR: (a) InferFix's type signal is a soft contrastive embedding feature at retrieval time — the retrieval pool is the full unified corpus, and type influences embedding proximity rather than pool membership — whereas FTCR hard-partitions the corpus into discrete type sub-indices at construction time so only same-type pairs are candidates for any query; (b) InferFix's 'types' are Infer diagnostic IDs (static-analysis-specific), not the 18-category natural-bug taxonomy aligned with DebugBench; (c) InferFix uses InferredBugs (static-analysis-artifact bugs in Java/C# repos), not natural bug-fix pairs from issue trackers and CI logs. InferFix validates that type-aware retrieval helps repair (supporting FTCR's hypothesis) while leaving the hard vs. soft type-partitioning comparison unresolved. ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of N discrete semantic types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than either InferFix's soft contrastive type conditioning or ReinFix's joint root-cause embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar embeddings but different repair operators do not. DebugBench uniquely provides 4,253 instances with ground-truth 18-category type annotations across C++, Java, and Python, enabling direct classifier calibration and turning error propagation from a latent risk into the paper's core measurable variable. The confidence-gated hybrid has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). M-RAG (ACL 2024, arXiv 2405.16420) validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis.\",\n  \"landscape\": \"RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% and is not a SOTA claim. InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-aware cross-repository retrieval system for code repair: it pretrains a Retriever via contrastive learning to embed semantically equivalent bugs and their fixes close together, conditioned on Infer's static-analysis-derived bug type annotations (null dereferences, resource leaks, thread-safety violations), then retrieves the most similar fix from InferredBugs (Java/C# repos with Infer-detected bugs). InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#, outperforming LLM baselines by 11–55%. Three design differences distinguish FTCR from InferFix: (a) retrieval mechanism — InferFix uses soft contrastive similarity where type is an embedding-time signal and retrieval is nearest-neighbor search over the full unified corpus; FTCR partitions the corpus into discrete type sub-indices at construction time, so the retrieval pool for any query is restricted to same-type pairs before similarity scoring; (b) defect taxonomy — InferFix uses Infer's diagnostic IDs (covering only statically-detectable bug patterns), not the 18-category natural-bug taxonomy aligned with DebugBench's empirically-grounded labels; (c) corpus — InferFix uses InferredBugs (static-analysis artifacts); FTCR uses natural bug-fix pairs from SWE-bench, BugsInPy, Defects4J, and GitBug-Java. The scientific question InferFix leaves open — and FTCR directly tests — is whether hard construction-time partitioning outperforms soft retrieval-time type conditioning for fix-template precision. ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning. Corpus quality confound: comparisons against published ReinFix results conflate two variables simultaneously — retrieval architecture (soft joint embedding vs. hard type partition) and corpus quality (100K TRANSFER synthetic pairs vs. 3,050 natural bug-fix pairs from issue trackers and CI logs). Intra-corpus ablations (FTCR vs. re-implemented ReinFix-style baseline on the same 3,050-pair natural corpus using the same text-embedding-3-large encoder) test the partitioning hypothesis cleanly and isolate architecture as the variable. Absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality differences simultaneously and are presented explicitly as such; they are not used to claim a clean head-to-head win on architecture alone. SWE-Exp (arXiv 2507.23361, revised February 2026) retrieves top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic Python-only pipeline. Three design differences: (1) soft vs. hard — SWE-Exp uses type as retrieval-time embedding metadata; FTCR partitions at index-construction time; (2) retrieved artifact — SWE-Exp stores distilled modification strategies; FTCR retrieves concrete fix patches; (3) scope — SWE-Exp is agentic and Python-only; FTCR covers C++/Java/Python in retrieval-only mode. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5. TypeRepair's context selection stage conditions on the identified defect type to select within-project code context and provide type-specific repair guidance — it does not retrieve from an external cross-repository fix corpus. Evidentiary basis: TypeRepair evaluates exclusively on Defects4J V1.2/V2.0 and QuixBugs — within-project Java bug collections that contain no external cross-repository retrieval component. The evaluation design (project-internal datasets, no external corpus described in benchmark setup) makes the within-project scope structurally evident from the experimental setup; any reviewer with full SQJ article access who finds this claim incorrect is encouraged to provide the correction, as the differentiation rests on the publicly visible evaluation design. TypeRepair is Java-only; FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 fix patches. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec while contextual and API information helps; the 'what to retrieve matters' finding motivates FTCR's type-partition design. DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3. Both update the landscape but are orthogonal to retrieval strategy. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via objective alignment. FTCR's structural departure from all prior work is to (1) classify incoming failures into discrete categories, then (2) retrieve only from the type-matched sub-index, using text-embedding-3-large (identical to ReinFix) for a clean intra-corpus partitioning comparison — with the random-partition control separating type-matching precision from pool-size reduction. RetypeR (ICSME 2024, Hao et al.) applies type-specific retrieval for Python type errors only; FTCR extends to 18 categories across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates multi-partition RAG outperforms single-store RAG across NLP tasks (+11% summarization, +8% translation, +12% dialogue). PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary scope. The APR survey (arXiv 2506.23749) reviews 63+ systems with no type-partitioned cross-language retrieval system identified.\",\n  \"approach\": \"We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms both InferFix's soft contrastive type conditioning and ReinFix's soft root-cause embedding for cross-repository fix template transfer. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix), same natural corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control.\\n\\nNLP Lead Contribution: LLM Label Quality and Downstream Retrieval Impact. The primary EMNLP contribution is a complete causal decomposition of when hard type conditioning helps and when it hurts, parameterized by four falsifiable quantities: (X%) few-shot LLM classifier accuracy against DebugBench ground-truth oracle labels; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement on DebugBench/Defects4J V1.2 for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances under hard partitioning vs. same baseline. Together these quantities are a direct empirical answer to: 'LLM-inferred categorical labels enable hard retrieval partitioning only if X% and Y% are high enough to make the correctly-classified population (driving Z%) larger than the misclassified population (driving W%).' This generalizes beyond code repair to any system that uses LLM-generated labels to route queries into type-specific retrieval pools.\\n\\nExecution Plan for EMNLP 2026 ARR (May 25 deadline, 15 days). Auto-research mode (10–14 days) is the only constraint-compliant execution path. Day-by-day schedule with minimum viable submission (MVS) milestones:\\n\\n- Day 0 (May 10): Launch auto-research pipeline; begin 3-pass annotation of 3,050 corpus pairs using DebugBench few-shot examples as demonstrations; configure Defects4J V1.2 Java-8 Docker environments and GitBug-Java isolated containers.\\n- Day 1–3 (May 11–13): Annotation completes (~$183 Claude API cost). DebugBench classifier calibration: 851 held-out instances → X% per-type accuracy. Cross-lingual Java transfer sample (56 human-verified pairs from Defects4J + GitBug-Java) → Y% transfer accuracy. Per-type count table computed; merge policy applied for rare Java types.\\n- Day 4–6 (May 14–16): Build type-partitioned sub-indices and ReinFix-style unified index (both text-embedding-3-large). Run Defects4J V1.2 ablations: Variant A (text-similarity RAG), Variant D (ReinFix-style re-implemented on same natural corpus), Variant E (FTCR@hard-all), Variant F (random-partition control, N equivalently-sized random sub-indices).\\n- Day 7–9 (May 17–19): DebugBench evaluation across all variants; confidence-gated τ sweep on held-out validation split; stratify results by classifier confidence band: high-confidence correctly-classified → Z%; misclassified → W%. SWE-bench Lite evaluation launched in parallel (requires 2 A100 nodes for ~10 min/instance).\\n- Day 10–12 (May 20–22): CodeBERT-base encoder ablation (same FTCR vs. ReinFix-style comparison, secondary encoder); taxonomy granularity ablation (6-type coarse vs. 18-type fine vs. merged-Java categories); retrieval k sweep (1/3/5/10).\\n- Day 13 (May 23): Results compilation; paper writing begins with NLP lead (X%/Y%/Z%/W% as opening contribution).\\n- Day 14–15 (May 24–25): Paper finalization and ARR submission. MVS for EMNLP: DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. SWE-bench Lite Python results included if pipeline completes by Day 12, deferred to ICSE 2027 extended version otherwise. The two-day writing window is extremely tight and requires a pre-drafted paper skeleton (introduction, related work, method) to be prepared during the Day 4–6 experiment-build window.\\n\\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. InferFix demonstrates that type conditioning improves over code-similarity retrieval, but uses a soft contrastive mechanism where type influences embedding distance rather than pool membership. FTCR embodies a stronger form of this principle: rather than retrieving the most similar embedding from a type-influenced but unified pool, we restrict the retrieval pool to same-type pairs at index construction, ensuring that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to score high in a shared embedding space but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\\n\\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559).\\n\\nCorpus Quality Confound (Explicit). The natural 3,050-pair corpus differs from ReinFix's 100K TRANSFER corpus in two simultaneous dimensions: (1) retrieval architecture (soft joint embedding vs. hard type partition) and (2) corpus quality (natural issue-tracker/CI bug-fix pairs vs. synthetic static-analysis-derived pairs). Intra-corpus ablations — FTCR vs. re-implemented ReinFix-style baseline using text-embedding-3-large on the identical 3,050-pair natural corpus — test the partitioning hypothesis cleanly and are the primary experimental contribution. Absolute performance comparisons against published ReinFix numbers on Defects4J reflect both architecture and corpus quality simultaneously; they are presented as joint-effect comparisons, not as clean head-to-head architectural wins. The random-partition control (Variant F) further isolates type-matching precision from pool-size reduction within the intra-corpus comparison.\\n\\nCorpus Sparsity Policy. Each pair is annotated with one of 18 semantic categories aligned with DebugBench's taxonomy via few-shot prompting; three annotation passes measure inter-run consistency. For the combined Python+Java corpus (~3,050 pairs), 18-type analysis yields an estimated mean of ~138 pairs per type, driven by Python (~2,487). For Java-only ablations (~559 pairs, ~31 per type average), types with fewer than 30 Java instances are merged into nearest-neighbor supercategories; Java ablation results are reported for the 6–8 resulting categories that each exceed 50 instances, with merged categories explicitly labeled.\\n\\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound (~$5–15 total embedding cost). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific.\\n\\nType Classifier Calibration on DebugBench Ground Truth. A held-out 20% split (851 instances) directly measures few-shot classifier precision and recall per type against oracle ground-truth labels, yielding X%. Cross-dataset zero-shot agreement on ~56 human-verified Java pairs yields Y%. These produce the core NLP finding: LLM-inferred bug type labels achieve X% agreement with DebugBench ground truth (Python/C++), transfer zero-shot to Java with Y% agreement, and predict retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs.\\n\\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect, the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index (Variant F). Any performance gap between FTCR (Variant E) and this control measures the precision benefit of type-matching net of pool-size reduction.\\n\\nConfidence-Gated Retrieval Fallback. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval. Six variants evaluated: (A) text-similarity RAG, (B) RELREPAIR, (C) RepoRepair, (D) ReinFix-style soft on same corpus, (E) FTCR@hard-all, (F) random-partition control. Confidence-gated hybrid evaluated as a seventh configuration. Precedent: CRAG (Yan et al., arXiv:2401.15884).\\n\\nPractical Utility. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is the retrieval contribution in isolation, not a pipeline SOTA claim. DynaFix demonstrates retrieval and execution augmentation are independently improvable axes; an improved retrieval module (FTCR vs. ReinFix-style) compounds with execution-level improvements. Standalone evaluation isolates the retrieval hypothesis cleanly.\\n\\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while Defects4J V1.2 (MVS) and SWE-bench Lite (full version) validate real-world transfer.\",\n  \"resource_estimate\": {\n    \"auto_research\": {\n      \"gpu_hours\": \"~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)\",\n      \"gpu_utilization\": \"near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants\",\n      \"ablation_scope\": \"Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline on same natural corpus), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (6-type coarse / 18-type fine / merged-Java), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java → SWE-bench-Lite Python), classifier accuracy stratification by confidence band\",\n      \"timeline\": \"10-14 days with 2 A100 nodes running in parallel — the ONLY constraint-compliant execution mode for the 16-day hard budget. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) both violate the user's timeline constraint and are not presented as viable paths.\",\n      \"day_by_day_schedule\": \"Day 0 (May 10): setup and corpus annotation launch. Day 1–3 (May 11–13): annotation + DebugBench classifier calibration (X%, Y%). Day 4–6 (May 14–16): index construction + Defects4J V1.2 ablations (Variants A/D/E/F). Day 7–9 (May 17–19): DebugBench evaluation + confidence stratification (Z%, W%) + SWE-bench Lite launch. Day 10–12 (May 20–22): CodeBERT ablation + granularity + k-sweep. Day 13 (May 23): results compilation + paper skeleton. Day 14–15 (May 24–25): paper finalization + ARR submission.\",\n      \"team\": \"0 (initial ~4h setup for corpus pipeline, per-type sub-index construction, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)\",\n      \"claude_api_cost\": \"$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)\",\n      \"embedding_api_cost\": \"~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)\",\n      \"estimated_gpu_cost\": \"~$969 (323 A100-hours × $3/h)\",\n      \"speed_bottleneck\": \"GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls\",\n      \"risk_note\": \"SWE-bench Lite may not complete before Day 12; MVS for EMNLP submission is DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control, which is achievable within the 10–14 day window. Auto-assigned bug type labels may drift without the three-pass consistency check; confidence-gated hybrid adds hyperparameter τ requiring tuning on held-out split before SWE-bench evaluation. Two-day paper writing window (Days 13–15) requires pre-drafted skeleton prepared during Days 4–6.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 ARR (deadline May 25, 2026 11:59 PM AoE — PRIMARY TARGET; 15 days from today). Path: auto-research completes Days 0–12 (May 10–22); paper writing Days 13–15 (May 23–25). Minimum viable submission: DebugBench classifier calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. NLP lead framing: LLM-generated bug type label quality and its downstream retrieval impact — a contribution to the NLP literature on LLM annotation reliability and retrieval-augmented generation. EMNLP's Empirical Methods track and code NLP community regularly accept papers evaluating LLM-generated categorical labels and RAG system design; the X%/Y%/Z%/W% falsifiable finding fits this tradition. Timeline is extremely tight: the two-day writing window requires a pre-drafted skeleton prepared concurrently with Days 4–6 experiment setup. Risk: if SWE-bench Lite does not complete by Day 12, the EMNLP version covers DebugBench + Defects4J only, with SWE-bench Lite results added in the ICSE 2027 version.\",\n    \"ICSE 2027 (mandatory abstract deadline June 23, 2026 — BACKUP venue if EMNLP ARR cycle overlaps unfavorably or EMNLP submission is not accepted). SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation; TypeRepair comparison clarifies FTCR's orthogonal contribution of cross-repository retrieval; InferFix paragraph establishes that hard vs. soft type partitioning is the untested dimension; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections; intra-corpus confound framing converts the corpus quality issue into a feature rather than a weakness.\",\n    \"FSE 2027 (full paper deadline October 2, 2026 — tertiary backup if both EMNLP and ICSE review cycles are unfavorable).\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"InferFix: End-to-End Program Repair with LLMs over Bug-Specific Retrieval (ESEC/FSE 2023, arXiv:2303.07263) [earliest type-aware cross-repository repair retrieval; Retriever pretrained via contrastive learning over Infer bug type annotations (null dereferences, resource leaks, thread safety) on InferredBugs corpus (Java/C# repos); 76.8% Java top-1 accuracy; uses soft contrastive similarity at retrieval time, NOT hard index-construction partitioning — FTCR's scientific contribution is testing hard vs. soft partitioning as the variable InferFix leaves unresolved; must differentiate explicitly: (a) soft contrastive embedding vs. hard construction-time partition; (b) Infer-specific diagnostic IDs vs. 18-category natural-bug taxonomy; (c) InferredBugs (static-analysis artifacts) vs. natural issue-tracker/CI bug-fix pairs]\",\n    \"ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; soft root-cause augmentation using unified vector database with text-embedding-3-large; intra-corpus comparison (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) is the clean architectural test; absolute comparisons against published ReinFix numbers reflect corpus quality confound and are presented as such]\",\n    \"SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; 73.0% SWE-bench Verified with Claude 4 Sonnet; agentic, Python-only; differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, multi-language scope]\",\n    \"TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J/QuixBugs (Java-only); validates that type conditioning improves LLM repair; Stage 3 context selection draws from within-project code files, not external cross-repository corpus — differentiation supported by evaluation design (project-internal datasets, no external corpus described in benchmark setup); FTCR's orthogonal contribution is type-conditioned retrieval from external ~3,050-pair cross-language corpus]\",\n    \"What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond (Gu et al., ICSE 2026, arXiv 2503.20589) [similar-code retrieval degrades code generation by up to 15% on CoderEval/RepoExec while structured knowledge helps; motivates type-partition fix-patch retrieval as avoiding the similarity-noise trap; note: code generation study, not repair — applicable as indirect motivation]\",\n    \"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330) [algorithm-type-conditioned retrieval in competitive programming — conceptual ancestor scoped to algorithmic tags]\",\n    \"RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors (ICSME 2024, Hao et al.) [type-specific retrieval for Python type errors only — FTCR extends to 18 types and 3 languages]\",\n    \"DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv 2512.24635) [surpasses ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; demonstrates retrieval and execution augmentation are independently improvable axes]\",\n    \"DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2604.19305) [295 Defects4J bugs with DeepSeek-V3; updates landscape but orthogonal — no retrieval augmentation]\",\n    \"D4C: Aligning the Objective of LLM-based Program Repair (ICSE 2025, arXiv 2404.08877) [180 Defects4J bugs via objective alignment; updates performance landscape]\",\n    \"M-RAG: Reinforcing Large Language Model Performance through Retrieval-Augmented Generation with Multiple Partitions (ACL 2024, arXiv 2405.16420) [multi-partition RAG: +11% summarization, +8% translation, +12% dialogue; principled precedent for partition-based retrieval across domains]\",\n    \"RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code (arXiv 2509.16701) [project-internal retrieval baseline]\",\n    \"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048) [documentation-guided localization baseline; 45.7% SWE-bench Lite]\",\n    \"DebugBench: Evaluating Debugging Capability of Large Language Models (ACL Findings 2024) [primary evaluation; ground-truth 18-category labels across C++/Java/Python for 4,253 instances; held-out 20% split for classifier calibration (X%); acknowledged synthetic-bug limitation]\",\n    \"GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; cross-lingual transfer calibration (Y%)]\",\n    \"SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025, arXiv 2504.21798) [50k Python task instances; scale corpus for Python retrieval index]\",\n    \"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey; confirms retrieval augmentation as key enhancement; no type-partitioned cross-language system identified; cites InferFix as a key retrieval-augmented approach]\",\n    \"What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]\",\n    \"PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]\",\n    \"RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]\",\n    \"CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism; precedent for FTCR confidence-gated hybrid; cite as preprint — withdrawn from ICLR 2025, unpublished]\"\n  ],\n  \"description\": \"FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft type-conditioned retrieval (InferFix's contrastive approach, ESEC/FSE 2023; ReinFix's root-cause embedding approach, ICSE 2026) for cross-repository fix template transfer. The primary NLP contribution — targeted at EMNLP 2026 ARR (May 25, 2026) — is a complete causal decomposition parameterized by four falsifiable quantities: (X%) few-shot LLM classifier accuracy vs. DebugBench ground-truth oracle labels; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts, generalizing to any system using LLM-inferred categorical labels for retrieval routing. FTCR's structural departure from ReinFix is to (1) classify incoming failures into one of 18 discrete semantic categories aligned with DebugBench's taxonomy, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable in a clean intra-corpus comparison. Round 6 revisions address five issues: (a) VENUE RESTORED — EMNLP 2026 ARR (May 25) reinstated as primary target with explicit day-by-day execution schedule (Days 0–12: auto-research; Days 13–15: paper finalization); auto-research is the only constraint-compliant mode (10–14 days); manual and human-in-loop modes removed from resource_estimate as they violate the 16-day budget; NLP lead framing (X%/Y%/Z%/W% classifier calibration) is the EMNLP submission's opening contribution; MVS = DebugBench calibration + Defects4J V1.2 ablations + random-partition control; SWE-bench Lite deferred to ICSE 2027 version if not complete by Day 12. (b) INFERFIX ADDED — InferFix (ESEC/FSE 2023, arXiv:2303.07263) added to landscape, opportunity, core_problem, and key_references with explicit three-point differentiation: soft contrastive embedding at retrieval time vs. FTCR's hard construction-time partitioning; Infer-specific diagnostic IDs vs. 18-category natural-bug taxonomy; InferredBugs (static-analysis artifacts) vs. natural bug-fix pairs; InferFix leaves the hard vs. soft comparison unresolved and FTCR tests it directly. (c) CORPUS CONFOUND EXPLICIT — landscape and approach now explicitly state that intra-corpus ablations (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) are the clean architectural test; absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality simultaneously and are presented as joint-effect comparisons. (d) TYPEREPAIR EVIDENTIARY BASIS — differentiation claim supported by evaluation design argument: TypeRepair evaluates exclusively on within-project datasets (Defects4J, QuixBugs) with no external cross-repository corpus in the benchmark setup, making within-project scope structurally evident from the experimental design. (e) RESOURCE_ESTIMATE RESTRUCTURED — stripped to auto-research mode only with day-by-day schedule integrated into the approach section.\",\n  \"project_name\": \"failure_type_rag_repair\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Uncited competing work invalidates novelty claim: ReinFix (ICSE 2025, arXiv 2506.23100) embeds root-cause classification into retrieval from a 1M-pair historical bug-fix corpus, which is mechanistically nearly identical to FTCR's type-conditioned retrieval from historical corpus. The proposal must cite and differentiate from ReinFix; without this, reviewers will reject on novelty grounds.\", \"CRITICAL — ReCode overlap is underplayed: ReCode already implements algorithm-type-conditioned retrieval with type-partitioned sub-knowledge-bases, the identical core mechanism. FTCR's contribution is extending this to real-world bugs (competitive programming → repositories), which must be framed more precisely. The current framing overclaims novelty.\", \"HIGH — Dataset size claim is internally inconsistent: BugsInPy (493) + Defects4J (1,192) = ~1,685 pairs, not 6,500. If the SWE-bench training split (19,000 instances) is included, that's 20,000+. The '~6,500' figure suggests some undescribed quality-filtering or subsetting logic that is not specified in the proposal. This will raise red flags in review.\", \"HIGH — Defects4J reproducibility crisis: Independent studies (MSR 2025) found ~50% of Defects4J fault-triggering tests are regression tests added post-hoc, and nearly 50% become non-reproducible with modern Java. BugsInPy showed 67% reproducibility. Mining ~1,685 pairs from these datasets may yield fewer than 900 reliably reproducible bug-fix pairs, undermining the corpus quality and scale claims.\", \"MEDIUM — Uncited prior art RetypeR (ICSME 2024): This paper applies type-specific retrieval (external retrieval stage conditioned on Python type errors) and should be discussed as prior art that narrows the novelty of cross-language type-conditioned retrieval.\", \"MEDIUM — Resource units inconsistency: The hard constraint is ≤200 H100-hours, but the proposal reports A100-hours throughout. Manual mode (~150 A100h ≈ 90 H100h) is within budget, but auto-research mode (~650 A100h ≈ 390 H100h) significantly exceeds the constraint. This should be flagged and the primary experiment budget anchored in H100-hours.\", \"MEDIUM — EMNLP framing needs NLP-centric repositioning: The primary contribution is a retrieval system design (SE contribution). EMNLP 'NLP and Code Models' track requires a clear NLP/LLM contribution. The few-shot taxonomy induction approach and its ability to generalize zero-shot across languages should be foregrounded as the NLP contribution; the retrieval architecture is the engineering substrate.\", \"LOW — DebugBench validity concern: DebugBench uses LeetCode code with GPT-4-implanted synthetic bugs, not real repository bugs. Results on DebugBench may not transfer to SWE-bench Lite, requiring a careful discussion of the domain gap between the two evaluation settings.\"]\nFeedback: The core gap FTCR targets is real but narrower than claimed. To make this revisable into a strong paper: (1) Reframe the novelty around what's genuinely new — the extension of type-partitioned retrieval from algorithmic contest code (ReCode) to real-world multi-language repository bugs with an 18-category taxonomy grounded in DebugBench's empirically validated type structure. This is a specific, defensible contribution. (2) Add ReinFix as a baseline: since ReinFix uses root-cause-conditioned retrieval from historical corpus, you must compare against it directly on a shared benchmark (Defects4J is common). If FTCR's type-partitioned index outperforms ReinFix's joint root-cause+code embedding, that's a publishable finding. (3) Fix the dataset size: either restrict to BugsInPy+Defects4J and acknowledge the smaller corpus (~1,500–1,685 pairs after reproducibility filtering), or explicitly include a quality-filtered SWE-bench train subset and describe the filtering criteria. (4) Run a reproducibility pre-check: before committing to Defects4J as a corpus source, filter to only Java 8-compatible bugs (reported to have ~80% reproducibility) and report the usable fraction. (5) For EMNLP fit, pivot the NLP angle to the few-shot taxonomy induction finding — specifically, whether LLM-inferred bug types are consistent, cross-lingual, and predictive of repair success. This is the NLP scientific question. (6) The 16-day timeline is only viable in auto-research mode with parallel evaluation; the paper should scope evaluation to DebugBench (where type labels are ground-truth) plus SWE-bench Lite (300 instances), and acknowledge that a full Defects4J corpus build is out-of-scope for the conference timeline.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Citation error: ReinFix is confirmed ICSE 2026 (arXiv 2506.23100 states 'Accepted by ICSE 2026'), not ICSE 2025 as the proposal states throughout. EMNLP 2026 explicitly warns against hallucinated citations and has stated it may desk-reject papers with such errors. Every reference to 'ReinFix (ICSE 2025)' must be corrected to 'ReinFix (ICSE 2026)'.\", \"HIGH — Corpus sparsity renders type partitioning semantically degenerate for rare types: 559 Java pairs (Defects4J + GitBug-Java) across 18 types yields ~31 Java instances per type on average. For rare bug categories (concurrency, resource leaks, format errors), this may be 5–15 instances. Retrieving k=5 from a sub-index of 15 instances is not retrieval—it is exhaustive lookup. The proposal must either (a) restrict to the 6–8 most frequent types where >50 Java instances exist, or (b) merge rare types into a broader category, or (c) acknowledge that the per-type ablation is only meaningful for the top N types and report per-type corpus sizes in the paper.\", \"HIGH — Classifier error propagation is unaddressed: if the type classifier misclassifies an incoming bug (which will occur for edge cases and multi-type bugs), the system retrieves from the wrong partition and almost certainly underperforms soft retrieval for those instances. This is the main structural risk of hard partitioning over soft embedding. The proposal must analyze: (a) classifier accuracy on held-out annotated bugs, (b) the performance degradation attributable to misclassification, and (c) whether a confidence-gated fallback to soft retrieval recovers performance.\", \"HIGH — EMNLP venue fit remains questionable: the core contribution is an IR architecture decision (partitioning a FAISS index by categorical label). EMNLP 'NLP and Code Models' reviewers will ask what the NLP/LM finding is. The 'few-shot cross-lingual taxonomy induction' contribution (measuring whether LLM-inferred bug types are consistent across annotation runs) is secondary and not a compelling standalone NLP finding—LLM classification consistency is well-studied. If submitting to EMNLP, the NLP contribution must be foregrounded more strongly, e.g., a finding that LLM-inferred type labels are cross-lingually stable and predictive of repair success at the p<0.01 level, with analysis of failure cases that reveal type-specific linguistic patterns in bug descriptions.\", \"MEDIUM — ASE 2026 NIER deadline (May 12) is 2 days from today and experiments are not done: listing it as a target venue is unrealistic. Remove from target_venues or replace with a venue with a later deadline (e.g., EMNLP Findings via ARR, or FSE 2027).\", \"MEDIUM — No expected performance range stated for SWE-bench Lite: reviewers will immediately compare against the RepoRepair baseline (45.7% on Lite). The proposal should state an expected performance range and justify why a lower absolute number is acceptable given the paper's focus on architectural comparison rather than SOTA performance.\", \"LOW — The proposal does not specify which encoding model will be used for FTCR. ReinFix uses text-embedding-3-large (OpenAI API). If FTCR uses the same encoder for fair comparison, this imposes an ongoing API cost not captured in the GPU-hour budget. If using CodeBERT or UniXcoder instead, the encoder comparison is confounded with the hard/soft partitioning comparison. This should be clarified explicitly.\"]\nFeedback: The Round 2 revision has fixed the major structural issues from Round 1 (ReinFix is now a baseline, dataset sizes are consistent, RetypeR is cited, compute is in H100-hours, DebugBench limitations acknowledged). The core hypothesis is testable and the ablation design is clean. Three issues must be addressed before this is submission-ready: (1) Fix the citation error throughout — ReinFix is ICSE 2026, not ICSE 2025; submit it as 'ReinFix (ICSE 2026, arXiv:2506.23100)'. (2) Address corpus sparsity directly in the methods section: report per-type instance counts in a table, restrict the full 18-type analysis to the Python+Java combined corpus, and for the Java-only ablations acknowledge that only the top N types have >50 instances. For types below a minimum threshold (suggest 30 instances), either merge or exclude from per-type breakdown. (3) Add a classifier accuracy analysis: measure the type classifier on the annotated DebugBench ground-truth labels (since DebugBench already has ground-truth types, you can directly measure LLM classifier accuracy), then report how type-matched retrieval performance varies as a function of classifier confidence. This turns the error propagation problem into a feature — it becomes an analysis of when hard partitioning helps vs. hurts. For EMNLP specifically: the NLP contribution must be stated as a crisp finding, not a process. Frame it as: 'We show that LLM-inferred bug type labels achieve X% agreement with DebugBench ground-truth labels, transfer zero-shot to unseen Java bugs with Y% agreement, and are predictive of retrieval-augmented repair success (type-matched retrieval outperforms soft retrieval by Z% for correctly classified bugs, while underperforming by W% for misclassified bugs).' This is a falsifiable empirical claim that EMNLP reviewers can evaluate.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL — CRAG citation is a hallucinated venue: The proposal cites 'CRAG (ICLR 2024)' but CRAG (arXiv:2401.15884) was submitted to ICLR 2025 and withdrawn — it was never accepted or published at any ICLR. Citing it as a published ICLR paper is precisely the kind of hallucinated venue citation EMNLP warns may trigger desk rejection. The correct citation is 'CRAG (Yan et al., 2024; arXiv:2401.15884)'.\", \"HIGH — Unacknowledged concurrent work: SWE-Exp (arXiv:2507.23361, July 2025) uses an experience bank where retrieval explicitly surfaces 'the top N=10 issues most relevant in terms of error type' via cosine similarity, achieves 41.6% on SWE-bench Verified, and is publicly available with open-source code. While the mechanism is different (experience trajectories + soft cosine vs. hard categorical partitioning of fix templates), EMNLP and ICSE reviewers will notice its absence. FTCR must cite it, note the difference (soft type-similarity vs. hard categorical partitioning), and explain why hard partitioning is a distinct hypothesis worth testing.\", \"MEDIUM — 'Clean comparison' overstates the isolation: Type-partitioned retrieval fundamentally reduces the effective retrieval corpus to 1/N_types (≈1/18 on average) of the full index. A smaller retrieval pool affects recall independently of the type-matching benefit. Without a 'random-partition baseline' (random corpus subsets of equivalent size per query), the observed gain (or loss) conflates two effects: (a) partitioning precision and (b) retrieval corpus size. The proposal should either add this control or explicitly acknowledge it as a confound in Section 4.\", \"MEDIUM — EMNLP main track fit remains overstated: The NLP contribution — measuring X% agreement between LLM-inferred bug type labels and DebugBench ground truth, then correlating with repair success — is a measurement finding about LLM classification reliability on a well-structured taxonomy. This is useful but unlikely to be viewed as a primary NLP/LM contribution by EMNLP main track reviewers, who expect findings that advance understanding of language models. EMNLP Findings is a more realistic target; ICSE 2027 (already listed) is the natural primary venue where the SE audience will value the retrieval architecture contribution directly.\", \"LOW — Minor ReinFix technical inaccuracy: The proposal states ReinFix uses 'a unified FAISS vector store' but the ReinFix paper (arXiv:2506.23100) only refers to 'a vector database' without specifying FAISS as the implementation. This overly specific characterization of the baseline's internals should be softened to 'a unified vector database' to avoid misrepresentation of the primary baseline.\"]\nFeedback: Round 3 has successfully addressed the four critical/high issues from Round 2: citation corrected to ICSE 2026 throughout, corpus sparsity handled with explicit per-type table and 30-instance merge policy, classifier error propagation addressed with confidence-gated hybrid and DebugBench calibration, and EMNLP framing sharpened to a crisp X%/Y%/Z%/W% falsifiable claim. The core hypothesis is testable and genuinely novel for multi-language APR. Two issues block submission: (1) Fix the CRAG citation immediately — replace every instance of 'CRAG (ICLR 2024)' with 'CRAG (Yan et al., 2024; arXiv:2401.15884)'. CRAG was submitted to ICLR 2025 but withdrawn and unpublished; citing it as published ICLR work is a hallucinated venue citation that can trigger desk rejection at EMNLP. (2) Add SWE-Exp (arXiv:2507.23361) to the landscape with one paragraph: it uses soft cosine retrieval filtered 'in terms of error type' from an experience bank; FTCR's departure is hard categorical partitioning at index-construction time, not just retrieval-time filtering, plus fix-template retrieval rather than trajectory experience. For longer-term strengthening: add a random-partition baseline (randomly assign corpus pairs to N equivalent-sized sub-indices) to isolate the type-matching benefit from the corpus-size effect. This single ablation converts the comparison from 'clean but contested' to 'rigorous and unambiguous'. On venue strategy: ICSE 2027 (abstract June 23) should be positioned as the primary target; EMNLP 2026 ARR (May 25) can be attempted for Findings if the NLP framing holds, but do not overinvest in EMNLP main track positioning — the primary audience for this work is the SE/APR community.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"HIGH — Uncited concurrent work: 'Towards Defect-Type-Aware Adaptive Program Repair' (TypeRepair, Zhang et al., Software Quality Journal 2026, link.springer.com/article/10.1007/s11219-026-09751-w) uses explicit defect type identification before context selection in a 4-stage pipeline (localization → type ID → context selection → patch generation) on Defects4J V1.2/V2.0 and QuixBugs, independently achieving 272% improvement over GPT-3.5 baseline. The paper must be obtained, read, and cited: if 'context selection' uses type-conditioned retrieval from a cross-repo external corpus (which cannot be confirmed from the abstract alone due to paywall), the overlap with FTCR is substantial and reviewers will notice its absence. If TypeRepair uses only within-project context, that is FTCR's key differentiation and must be stated explicitly.\", \"HIGH — Unaddressed counterevidence: 'What to Retrieve for Effective Retrieval-Augmented Code Generation?' (ICSE 2026, arXiv 2503.20589) empirically shows that retrieving syntactically similar code snippets degrades performance by up to 15% compared to retrieving in-context examples and API information. This is a direct challenge to FTCR's premise: if type-partitioned retrieval returns syntactically similar-but-wrong-level-of-abstraction fixes within each partition, it may concentrate rather than reduce this noise. The authors must address this finding — either by arguing that semantic type partitioning selects at a different abstraction level than syntax similarity, or by adding an experiment measuring within-type fix template quality vs. cross-type.\", \"MEDIUM — Practical utility framing missing: FTCR projects 20–35% on SWE-bench Lite while SWE-Exp achieves 73% on SWE-bench Verified and RepoRepair achieves 45.7% on Lite. ICSE 2027 reviewers will ask why the retrieval strategy matters in isolation when execution-augmented agentic methods dominate. The paper needs an explicit 'why retrieval strategy matters' argument: e.g., (1) retrieval modules are independently upgradeable components within agentic systems — DynaFix adds execution feedback orthogonally to retrieval, so a better retrieval module improves the whole pipeline; (2) the 20–35% baseline is specifically the retrieval contribution, not the full agentic ceiling. This argument exists implicitly but must be stated explicitly.\", \"LOW — EMNLP 2026 ARR deadline is not credible given current state: The May 25 deadline is 15 days away. To submit to ARR requires a complete written paper, full experimental results, and bibliography validation (EMNLP's hallucinated-citation warning is explicit). The paper's hedge ('if too close, defer') should be changed to a definitive decision: either commit to running minimum viable experiments starting immediately (DebugBench classifier calibration + Defects4J V1.2 with the 4 primary variants) or acknowledge ICSE 2027 as the sole target. Leaving it ambiguous signals poor project planning to co-authors and advisors.\"]\nFeedback: Round 4 has successfully resolved all five issues from Round 3: CRAG citation is correct (arXiv-only), SWE-Exp is cited with three clear design differences, the random-partition control (Variant F) converts the corpus-size confound into a closed experimental question, EMNLP is downgraded to Findings, and ReinFix's implementation detail is softened. Independent verification confirms all cited paper claims are accurate. The hard-vs-soft retrieval comparison for semantic bug-type partitioned cross-repo repair is genuinely novel — no existing paper makes this specific comparison. Two actions are required for Round 5: (1) Read the TypeRepair SQJ 2026 paper (Zhang et al., doi:10.1007/s11219-026-09751-w) and add it to the landscape — the differentiation is either that TypeRepair uses intra-project context (state this explicitly) or that it uses cross-repo retrieval but covers only Java with a different pipeline structure (then FTCR's C++/Java/Python scope and the hard/soft comparison are the differentiators). (2) Cite and respond to 'What to Retrieve for Effective RAG Code Generation?' (ICSE 2026, arXiv:2503.20589): its finding that similar code retrieval degrades performance by 15% motivates FTCR's type-conditioning exactly — within a type partition, retrieved examples share fix structure rather than surface-level code similarity, which is the argument FTCR needs to make explicit. These two additions would resolve the remaining novelty and counterevidence gaps. The practical utility framing (retrieval as a modular component upgradeable within agentic pipelines) should be added as a paragraph in the introduction — this is the clearest answer to 'why does this matter when agentic methods dominate at 73%.'\n\n### Round 5 review\nVerdict: revise\nIssues: [\"CRITICAL — Target venue violates user requirements: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026, 15 days from today). The proposal now targets ICSE 2027 (abstract June 23, 2026) exclusively, a full year late and a different research community. Previous reviewers flagged EMNLP as infeasible given experiment state, but the requirement was not to change venues — it was to make the idea work within the constraint. If auto-research starts immediately (day 0), 10–14 days of experiments complete by ~May 23, leaving 2 days to finalize the paper for the May 25 ARR deadline. This is technically achievable but requires an explicit, committed execution plan with the NLP framing (X%/Y%/Z%/W% classifier calibration finding) as the lead contribution. The proposal must either restore EMNLP 2026 as the primary target with a day-by-day execution schedule, or explicitly acknowledge that it fails the user's venue constraint and accept that verdict.\", \"HIGH — 16-day timeline constraint met only by auto-research mode: The user's hard constraint is ≤16 days. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) exceed this by 8–12× and should not appear as viable execution paths in resource_estimate. The paper should flag auto-research (10–14 days) as the only constraint-compliant mode, or restructure the three modes to reflect feasible timelines.\", \"MEDIUM — InferFix (ESEC/FSE 2023, arXiv:2303.07263) is unmentioned prior art: Independently confirmed that InferFix uses bug type annotations and contrastive learning to retrieve 'semantically equivalent bugs and corresponding fixes of the same bug type' from an external repository corpus (InferredBugs, thousands of Java and C# repos). This is the closest non-trivial precursor to type-conditioned cross-repo repair retrieval and is not cited anywhere in the proposal. ICSE 2027 reviewers familiar with the APR literature will notice its absence. FTCR should differentiate explicitly: InferFix uses soft contrastive similarity (learned embedding grouping) not hard categorical index partitioning; it targets Java/C# from Infer static analysis findings, not the 18-category natural-bug taxonomy; and the corpus construction and evaluation differ. This differentiation is achievable in one paragraph but must be present.\", \"MEDIUM — Cross-system corpus quality confound inadequately flagged: The 'clean comparison' correctly uses the same 3,050-pair natural corpus for both FTCR and the ReinFix-style baseline, isolating partitioning as the variable. But any performance comparison against the published ReinFix results uses 100K TRANSFER corpus pairs (synthetic, from static analysis), creating a corpus quality × retrieval architecture confound that the random-partition control does not address. The paper must explicitly state: (a) intra-corpus ablations (FTCR vs. re-implemented ReinFix on 3,050 pairs) test the partitioning hypothesis cleanly, and (b) absolute comparisons against published ReinFix results reflect both architecture and corpus quality differences simultaneously.\", \"LOW — TypeRepair context-selection scope unverifiable from publicly accessible sources: The critical differentiation claim — that TypeRepair's Stage 3 selects within-project context only, not from an external cross-repo corpus — could not be independently confirmed due to paywall access to the SQJ article. The proposal states this confidently; it should note the evidentiary basis (e.g., 'TypeRepair evaluates exclusively on Defects4J/QuixBugs, which are within-project datasets, and the paper's supplementary prompt templates confirm type-specific in-project context selection rather than external retrieval') to avoid a reviewer flagging this differentiation as unsubstantiated.\"]\nFeedback: This is the most polished version of FTCR to date. The random-partition control, confidence-gated hybrid, per-type merge policy, and ReinFix/SWE-Exp/TypeRepair differentiation all reflect genuine methodological rigor. Two actions would bring this to pass: (1) VENUE DECISION — the proposal must choose one of two paths and commit fully: either (a) restore EMNLP 2026 ARR (May 25) as the primary target with a specific day-by-day execution schedule (day 0-13: auto-research runs corpus annotation + DebugBench classifier calibration + Defects4J V1.2 ablations; day 13-15: paper writing with NLP lead framing the X%/Y%/Z%/W% falsifiable classifier finding), acknowledging the extreme timeline pressure; or (b) explicitly declare that the user's requirement cannot be met for EMNLP 2026 and accept ICSE 2027 as the sole target with a verdict of 'fail' on the original requirement. Leaving both venues while targeting neither by the May 25 deadline is a planning failure. (2) ADD INFERFIX — one paragraph in the landscape: 'InferFix (ESEC/FSE 2023, arXiv:2303.07263) retrieves fixes for bugs of the same type using contrastive-learned embeddings over bug type annotations, establishing type-aware retrieval for Java/C# static analysis bugs. FTCR differs in three respects: (a) hard categorical index partitioning at construction time rather than soft contrastive similarity at retrieval time; (b) 18-category natural-bug taxonomy across C++/Java/Python rather than InferBugs' Infer-specific defect categories; (c) direct comparison of hard vs. soft type conditioning as the scientific contribution.' If these two issues are resolved, the novelty and feasibility scores reach 3.5+ and the paper is close to a pass for ICSE 2027 (though not EMNLP 2026 unless the execution plan is credible).\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T06:43:43.349Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T06:43:43.349Z",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-10T06:43:43.377Z_

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

## Idea under review (round 6/10)
{
  "title": "Failure-Type-Conditioned Retrieval Augmentation for Repository Repair",
  "core_problem": "The lead empirical question — tractable because DebugBench provides oracle ground-truth labels for 4,253 instances — is: how accurately can a few-shot LLM assign semantic bug type labels from an 18-category taxonomy, and does that label accuracy determine whether hard categorical retrieval index partitioning outperforms soft root-cause-augmented retrieval (ReinFix, ICSE 2026) for cross-repository fix template transfer? This frames FTCR as an empirical study of LLM-generated categorical label quality and its downstream retrieval impact, yielding four falsifiable quantities: (X%) few-shot classifier accuracy vs. DebugBench ground-truth oracle labels; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type-partitioned retrieval vs. the soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts — a finding with direct generalization to any retrieval system using LLM-inferred labels.\n\nRetrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. InferFix (ESEC/FSE 2023, arXiv:2303.07263) establishes that type-aware retrieval benefits code repair by using contrastive-learned embeddings over Infer's static-analysis-derived bug type annotations, but its type signal remains a soft continuous embedding feature — retrieval is still nearest-neighbor search across a unified corpus, not hard index-construction partitioning. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is whether hard categorical type partitioning of the retrieval index outperforms both InferFix's soft contrastive type conditioning and ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer, particularly in a multi-language setting. An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. Type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and become analytical contributions when addressed directly: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across 18 types yields only ~31 Java instances per type on average, requiring an explicit minimum-threshold and merge policy for rare types; and (2) classifier error propagation — when an incoming bug is misclassified, hard partitioning underperforms soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback — turns potential weaknesses into the core empirical variables (Z% and W%) that define the paper's scientific contribution.",
  "opportunity": "ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-aware cross-repository retrieval system for code repair: its Retriever is pretrained via contrastive learning to bring semantically equivalent bugs and their fixes closer in embedding space, conditioned on Infer's static-analysis-derived bug type annotations (null dereferences, resource leaks, thread-safety violations), and achieves 76.8% top-1 accuracy on Java and 65.6% on C#. Three properties distinguish InferFix from FTCR: (a) InferFix's type signal is a soft contrastive embedding feature at retrieval time — the retrieval pool is the full unified corpus, and type influences embedding proximity rather than pool membership — whereas FTCR hard-partitions the corpus into discrete type sub-indices at construction time so only same-type pairs are candidates for any query; (b) InferFix's 'types' are Infer diagnostic IDs (static-analysis-specific), not the 18-category natural-bug taxonomy aligned with DebugBench; (c) InferFix uses InferredBugs (static-analysis-artifact bugs in Java/C# repos), not natural bug-fix pairs from issue trackers and CI logs. InferFix validates that type-aware retrieval helps repair (supporting FTCR's hypothesis) while leaving the hard vs. soft type-partitioning comparison unresolved. ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of N discrete semantic types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than either InferFix's soft contrastive type conditioning or ReinFix's joint root-cause embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar embeddings but different repair operators do not. DebugBench uniquely provides 4,253 instances with ground-truth 18-category type annotations across C++, Java, and Python, enabling direct classifier calibration and turning error propagation from a latent risk into the paper's core measurable variable. The confidence-gated hybrid has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). M-RAG (ACL 2024, arXiv 2405.16420) validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis.",
  "landscape": "RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% and is not a SOTA claim. InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-aware cross-repository retrieval system for code repair: it pretrains a Retriever via contrastive learning to embed semantically equivalent bugs and their fixes close together, conditioned on Infer's static-analysis-derived bug type annotations (null dereferences, resource leaks, thread-safety violations), then retrieves the most similar fix from InferredBugs (Java/C# repos with Infer-detected bugs). InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#, outperforming LLM baselines by 11–55%. Three design differences distinguish FTCR from InferFix: (a) retrieval mechanism — InferFix uses soft contrastive similarity where type is an embedding-time signal and retrieval is nearest-neighbor search over the full unified corpus; FTCR partitions the corpus into discrete type sub-indices at construction time, so the retrieval pool for any query is restricted to same-type pairs before similarity scoring; (b) defect taxonomy — InferFix uses Infer's diagnostic IDs (covering only statically-detectable bug patterns), not the 18-category natural-bug taxonomy aligned with DebugBench's empirically-grounded labels; (c) corpus — InferFix uses InferredBugs (static-analysis artifacts); FTCR uses natural bug-fix pairs from SWE-bench, BugsInPy, Defects4J, and GitBug-Java. The scientific question InferFix leaves open — and FTCR directly tests — is whether hard construction-time partitioning outperforms soft retrieval-time type conditioning for fix-template precision. ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning. Corpus quality confound: comparisons against published ReinFix results conflate two variables simultaneously — retrieval architecture (soft joint embedding vs. hard type partition) and corpus quality (100K TRANSFER synthetic pairs vs. 3,050 natural bug-fix pairs from issue trackers and CI logs). Intra-corpus ablations (FTCR vs. re-implemented ReinFix-style baseline on the same 3,050-pair natural corpus using the same text-embedding-3-large encoder) test the partitioning hypothesis cleanly and isolate architecture as the variable. Absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality differences simultaneously and are presented explicitly as such; they are not used to claim a clean head-to-head win on architecture alone. SWE-Exp (arXiv 2507.23361, revised February 2026) retrieves top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic Python-only pipeline. Three design differences: (1) soft vs. hard — SWE-Exp uses type as retrieval-time embedding metadata; FTCR partitions at index-construction time; (2) retrieved artifact — SWE-Exp stores distilled modification strategies; FTCR retrieves concrete fix patches; (3) scope — SWE-Exp is agentic and Python-only; FTCR covers C++/Java/Python in retrieval-only mode. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5. TypeRepair's context selection stage conditions on the identified defect type to select within-project code context and provide type-specific repair guidance — it does not retrieve from an external cross-repository fix corpus. Evidentiary basis: TypeRepair evaluates exclusively on Defects4J V1.2/V2.0 and QuixBugs — within-project Java bug collections that contain no external cross-repository retrieval component. The evaluation design (project-internal datasets, no external corpus described in benchmark setup) makes the within-project scope structurally evident from the experimental setup; any reviewer with full SQJ article access who finds this claim incorrect is encouraged to provide the correction, as the differentiation rests on the publicly visible evaluation design. TypeRepair is Java-only; FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 fix patches. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec while contextual and API information helps; the 'what to retrieve matters' finding motivates FTCR's type-partition design. DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3. Both update the landscape but are orthogonal to retrieval strategy. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via objective alignment. FTCR's structural departure from all prior work is to (1) classify incoming failures into discrete categories, then (2) retrieve only from the type-matched sub-index, using text-embedding-3-large (identical to ReinFix) for a clean intra-corpus partitioning comparison — with the random-partition control separating type-matching precision from pool-size reduction. RetypeR (ICSME 2024, Hao et al.) applies type-specific retrieval for Python type errors only; FTCR extends to 18 categories across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates multi-partition RAG outperforms single-store RAG across NLP tasks (+11% summarization, +8% translation, +12% dialogue). PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary scope. The APR survey (arXiv 2506.23749) reviews 63+ systems with no type-partitioned cross-language retrieval system identified.",
  "approach": "We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms both InferFix's soft contrastive type conditioning and ReinFix's soft root-cause embedding for cross-repository fix template transfer. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix), same natural corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control.\n\nNLP Lead Contribution: LLM Label Quality and Downstream Retrieval Impact. The primary EMNLP contribution is a complete causal decomposition of when hard type conditioning helps and when it hurts, parameterized by four falsifiable quantities: (X%) few-shot LLM classifier accuracy against DebugBench ground-truth oracle labels; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement on DebugBench/Defects4J V1.2 for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances under hard partitioning vs. same baseline. Together these quantities are a direct empirical answer to: 'LLM-inferred categorical labels enable hard retrieval partitioning only if X% and Y% are high enough to make the correctly-classified population (driving Z%) larger than the misclassified population (driving W%).' This generalizes beyond code repair to any system that uses LLM-generated labels to route queries into type-specific retrieval pools.\n\nExecution Plan for EMNLP 2026 ARR (May 25 deadline, 15 days). Auto-research mode (10–14 days) is the only constraint-compliant execution path. Day-by-day schedule with minimum viable submission (MVS) milestones:\n\n- Day 0 (May 10): Launch auto-research pipeline; begin 3-pass annotation of 3,050 corpus pairs using DebugBench few-shot examples as demonstrations; configure Defects4J V1.2 Java-8 Docker environments and GitBug-Java isolated containers.\n- Day 1–3 (May 11–13): Annotation completes (~$183 Claude API cost). DebugBench classifier calibration: 851 held-out instances → X% per-type accuracy. Cross-lingual Java transfer sample (56 human-verified pairs from Defects4J + GitBug-Java) → Y% transfer accuracy. Per-type count table computed; merge policy applied for rare Java types.\n- Day 4–6 (May 14–16): Build type-partitioned sub-indices and ReinFix-style unified index (both text-embedding-3-large). Run Defects4J V1.2 ablations: Variant A (text-similarity RAG), Variant D (ReinFix-style re-implemented on same natural corpus), Variant E (FTCR@hard-all), Variant F (random-partition control, N equivalently-sized random sub-indices).\n- Day 7–9 (May 17–19): DebugBench evaluation across all variants; confidence-gated τ sweep on held-out validation split; stratify results by classifier confidence band: high-confidence correctly-classified → Z%; misclassified → W%. SWE-bench Lite evaluation launched in parallel (requires 2 A100 nodes for ~10 min/instance).\n- Day 10–12 (May 20–22): CodeBERT-base encoder ablation (same FTCR vs. ReinFix-style comparison, secondary encoder); taxonomy granularity ablation (6-type coarse vs. 18-type fine vs. merged-Java categories); retrieval k sweep (1/3/5/10).\n- Day 13 (May 23): Results compilation; paper writing begins with NLP lead (X%/Y%/Z%/W% as opening contribution).\n- Day 14–15 (May 24–25): Paper finalization and ARR submission. MVS for EMNLP: DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. SWE-bench Lite Python results included if pipeline completes by Day 12, deferred to ICSE 2027 extended version otherwise. The two-day writing window is extremely tight and requires a pre-drafted paper skeleton (introduction, related work, method) to be prepared during the Day 4–6 experiment-build window.\n\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. InferFix demonstrates that type conditioning improves over code-similarity retrieval, but uses a soft contrastive mechanism where type influences embedding distance rather than pool membership. FTCR embodies a stronger form of this principle: rather than retrieving the most similar embedding from a type-influenced but unified pool, we restrict the retrieval pool to same-type pairs at index construction, ensuring that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to score high in a shared embedding space but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\n\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559).\n\nCorpus Quality Confound (Explicit). The natural 3,050-pair corpus differs from ReinFix's 100K TRANSFER corpus in two simultaneous dimensions: (1) retrieval architecture (soft joint embedding vs. hard type partition) and (2) corpus quality (natural issue-tracker/CI bug-fix pairs vs. synthetic static-analysis-derived pairs). Intra-corpus ablations — FTCR vs. re-implemented ReinFix-style baseline using text-embedding-3-large on the identical 3,050-pair natural corpus — test the partitioning hypothesis cleanly and are the primary experimental contribution. Absolute performance comparisons against published ReinFix numbers on Defects4J reflect both architecture and corpus quality simultaneously; they are presented as joint-effect comparisons, not as clean head-to-head architectural wins. The random-partition control (Variant F) further isolates type-matching precision from pool-size reduction within the intra-corpus comparison.\n\nCorpus Sparsity Policy. Each pair is annotated with one of 18 semantic categories aligned with DebugBench's taxonomy via few-shot prompting; three annotation passes measure inter-run consistency. For the combined Python+Java corpus (~3,050 pairs), 18-type analysis yields an estimated mean of ~138 pairs per type, driven by Python (~2,487). For Java-only ablations (~559 pairs, ~31 per type average), types with fewer than 30 Java instances are merged into nearest-neighbor supercategories; Java ablation results are reported for the 6–8 resulting categories that each exceed 50 instances, with merged categories explicitly labeled.\n\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound (~$5–15 total embedding cost). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific.\n\nType Classifier Calibration on DebugBench Ground Truth. A held-out 20% split (851 instances) directly measures few-shot classifier precision and recall per type against oracle ground-truth labels, yielding X%. Cross-dataset zero-shot agreement on ~56 human-verified Java pairs yields Y%. These produce the core NLP finding: LLM-inferred bug type labels achieve X% agreement with DebugBench ground truth (Python/C++), transfer zero-shot to Java with Y% agreement, and predict retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs.\n\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect, the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index (Variant F). Any performance gap between FTCR (Variant E) and this control measures the precision benefit of type-matching net of pool-size reduction.\n\nConfidence-Gated Retrieval Fallback. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval. Six variants evaluated: (A) text-similarity RAG, (B) RELREPAIR, (C) RepoRepair, (D) ReinFix-style soft on same corpus, (E) FTCR@hard-all, (F) random-partition control. Confidence-gated hybrid evaluated as a seventh configuration. Precedent: CRAG (Yan et al., arXiv:2401.15884).\n\nPractical Utility. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is the retrieval contribution in isolation, not a pipeline SOTA claim. DynaFix demonstrates retrieval and execution augmentation are independently improvable axes; an improved retrieval module (FTCR vs. ReinFix-style) compounds with execution-level improvements. Standalone evaluation isolates the retrieval hypothesis cleanly.\n\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while Defects4J V1.2 (MVS) and SWE-bench Lite (full version) validate real-world transfer.",
  "resource_estimate": {
    "auto_research": {
      "gpu_hours": "~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)",
      "gpu_utilization": "near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants",
      "ablation_scope": "Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline on same natural corpus), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (6-type coarse / 18-type fine / merged-Java), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java → SWE-bench-Lite Python), classifier accuracy stratification by confidence band",
      "timeline": "10-14 days with 2 A100 nodes running in parallel — the ONLY constraint-compliant execution mode for the 16-day hard budget. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) both violate the user's timeline constraint and are not presented as viable paths.",
      "day_by_day_schedule": "Day 0 (May 10): setup and corpus annotation launch. Day 1–3 (May 11–13): annotation + DebugBench classifier calibration (X%, Y%). Day 4–6 (May 14–16): index construction + Defects4J V1.2 ablations (Variants A/D/E/F). Day 7–9 (May 17–19): DebugBench evaluation + confidence stratification (Z%, W%) + SWE-bench Lite launch. Day 10–12 (May 20–22): CodeBERT ablation + granularity + k-sweep. Day 13 (May 23): results compilation + paper skeleton. Day 14–15 (May 24–25): paper finalization + ARR submission.",
      "team": "0 (initial ~4h setup for corpus pipeline, per-type sub-index construction, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)",
      "claude_api_cost": "$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)",
      "embedding_api_cost": "~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)",
      "estimated_gpu_cost": "~$969 (323 A100-hours × $3/h)",
      "speed_bottleneck": "GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls",
      "risk_note": "SWE-bench Lite may not complete before Day 12; MVS for EMNLP submission is DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control, which is achievable within the 10–14 day window. Auto-assigned bug type labels may drift without the three-pass consistency check; confidence-gated hybrid adds hyperparameter τ requiring tuning on held-out split before SWE-bench evaluation. Two-day paper writing window (Days 13–15) requires pre-drafted skeleton prepared during Days 4–6."
    }
  },
  "target_venues": [
    "EMNLP 2026 ARR (deadline May 25, 2026 11:59 PM AoE — PRIMARY TARGET; 15 days from today). Path: auto-research completes Days 0–12 (May 10–22); paper writing Days 13–15 (May 23–25). Minimum viable submission: DebugBench classifier calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. NLP lead framing: LLM-generated bug type label quality and its downstream retrieval impact — a contribution to the NLP literature on LLM annotation reliability and retrieval-augmented generation. EMNLP's Empirical Methods track and code NLP community regularly accept papers evaluating LLM-generated categorical labels and RAG system design; the X%/Y%/Z%/W% falsifiable finding fits this tradition. Timeline is extremely tight: the two-day writing window requires a pre-drafted skeleton prepared concurrently with Days 4–6 experiment setup. Risk: if SWE-bench Lite does not complete by Day 12, the EMNLP version covers DebugBench + Defects4J only, with SWE-bench Lite results added in the ICSE 2027 version.",
    "ICSE 2027 (mandatory abstract deadline June 23, 2026 — BACKUP venue if EMNLP ARR cycle overlaps unfavorably or EMNLP submission is not accepted). SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation; TypeRepair comparison clarifies FTCR's orthogonal contribution of cross-repository retrieval; InferFix paragraph establishes that hard vs. soft type partitioning is the untested dimension; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections; intra-corpus confound framing converts the corpus quality issue into a feature rather than a weakness.",
    "FSE 2027 (full paper deadline October 2, 2026 — tertiary backup if both EMNLP and ICSE review cycles are unfavorable)."
  ],
  "level": "solid",
  "key_references": [
    "InferFix: End-to-End Program Repair with LLMs over Bug-Specific Retrieval (ESEC/FSE 2023, arXiv:2303.07263) [earliest type-aware cross-repository repair retrieval; Retriever pretrained via contrastive learning over Infer bug type annotations (null dereferences, resource leaks, thread safety) on InferredBugs corpus (Java/C# repos); 76.8% Java top-1 accuracy; uses soft contrastive similarity at retrieval time, NOT hard index-construction partitioning — FTCR's scientific contribution is testing hard vs. soft partitioning as the variable InferFix leaves unresolved; must differentiate explicitly: (a) soft contrastive embedding vs. hard construction-time partition; (b) Infer-specific diagnostic IDs vs. 18-category natural-bug taxonomy; (c) InferredBugs (static-analysis artifacts) vs. natural issue-tracker/CI bug-fix pairs]",
    "ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; soft root-cause augmentation using unified vector database with text-embedding-3-large; intra-corpus comparison (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) is the clean architectural test; absolute comparisons against published ReinFix numbers reflect corpus quality confound and are presented as such]",
    "SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; 73.0% SWE-bench Verified with Claude 4 Sonnet; agentic, Python-only; differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, multi-language scope]",
    "TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J/QuixBugs (Java-only); validates that type conditioning improves LLM repair; Stage 3 context selection draws from within-project code files, not external cross-repository corpus — differentiation supported by evaluation design (project-internal datasets, no external corpus described in benchmark setup); FTCR's orthogonal contribution is type-conditioned retrieval from external ~3,050-pair cross-language corpus]",
    "What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond (Gu et al., ICSE 2026, arXiv 2503.20589) [similar-code retrieval degrades code generation by up to 15% on CoderEval/RepoExec while structured knowledge helps; motivates type-partition fix-patch retrieval as avoiding the similarity-noise trap; note: code generation study, not repair — applicable as indirect motivation]",
    "ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330) [algorithm-type-conditioned retrieval in competitive programming — conceptual ancestor scoped to algorithmic tags]",
    "RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors (ICSME 2024, Hao et al.) [type-specific retrieval for Python type errors only — FTCR extends to 18 types and 3 languages]",
    "DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv 2512.24635) [surpasses ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; demonstrates retrieval and execution augmentation are independently improvable axes]",
    "DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2604.19305) [295 Defects4J bugs with DeepSeek-V3; updates landscape but orthogonal — no retrieval augmentation]",
    "D4C: Aligning the Objective of LLM-based Program Repair (ICSE 2025, arXiv 2404.08877) [180 Defects4J bugs via objective alignment; updates performance landscape]",
    "M-RAG: Reinforcing Large Language Model Performance through Retrieval-Augmented Generation with Multiple Partitions (ACL 2024, arXiv 2405.16420) [multi-partition RAG: +11% summarization, +8% translation, +12% dialogue; principled precedent for partition-based retrieval across domains]",
    "RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code (arXiv 2509.16701) [project-internal retrieval baseline]",
    "RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048) [documentation-guided localization baseline; 45.7% SWE-bench Lite]",
    "DebugBench: Evaluating Debugging Capability of Large Language Models (ACL Findings 2024) [primary evaluation; ground-truth 18-category labels across C++/Java/Python for 4,253 instances; held-out 20% split for classifier calibration (X%); acknowledged synthetic-bug limitation]",
    "GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; cross-lingual transfer calibration (Y%)]",
    "SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025, arXiv 2504.21798) [50k Python task instances; scale corpus for Python retrieval index]",
    "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey; confirms retrieval augmentation as key enhancement; no type-partitioned cross-language system identified; cites InferFix as a key retrieval-augmented approach]",
    "What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]",
    "PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]",
    "RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]",
    "CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism; precedent for FTCR confidence-gated hybrid; cite as preprint — withdrawn from ICLR 2025, unpublished]"
  ],
  "description": "FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft type-conditioned retrieval (InferFix's contrastive approach, ESEC/FSE 2023; ReinFix's root-cause embedding approach, ICSE 2026) for cross-repository fix template transfer. The primary NLP contribution — targeted at EMNLP 2026 ARR (May 25, 2026) — is a complete causal decomposition parameterized by four falsifiable quantities: (X%) few-shot LLM classifier accuracy vs. DebugBench ground-truth oracle labels; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts, generalizing to any system using LLM-inferred categorical labels for retrieval routing. FTCR's structural departure from ReinFix is to (1) classify incoming failures into one of 18 discrete semantic categories aligned with DebugBench's taxonomy, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable in a clean intra-corpus comparison. Round 6 revisions address five issues: (a) VENUE RESTORED — EMNLP 2026 ARR (May 25) reinstated as primary target with explicit day-by-day execution schedule (Days 0–12: auto-research; Days 13–15: paper finalization); auto-research is the only constraint-compliant mode (10–14 days); manual and human-in-loop modes removed from resource_estimate as they violate the 16-day budget; NLP lead framing (X%/Y%/Z%/W% classifier calibration) is the EMNLP submission's opening contribution; MVS = DebugBench calibration + Defects4J V1.2 ablations + random-partition control; SWE-bench Lite deferred to ICSE 2027 version if not complete by Day 12. (b) INFERFIX ADDED — InferFix (ESEC/FSE 2023, arXiv:2303.07263) added to landscape, opportunity, core_problem, and key_references with explicit three-point differentiation: soft contrastive embedding at retrieval time vs. FTCR's hard construction-time partitioning; Infer-specific diagnostic IDs vs. 18-category natural-bug taxonomy; InferredBugs (static-analysis artifacts) vs. natural bug-fix pairs; InferFix leaves the hard vs. soft comparison unresolved and FTCR tests it directly. (c) CORPUS CONFOUND EXPLICIT — landscape and approach now explicitly state that intra-corpus ablations (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) are the clean architectural test; absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality simultaneously and are presented as joint-effect comparisons. (d) TYPEREPAIR EVIDENTIARY BASIS — differentiation claim supported by evaluation design argument: TypeRepair evaluates exclusively on within-project datasets (Defects4J, QuixBugs) with no external cross-repository corpus in the benchmark setup, making within-project scope structurally evident from the experimental design. (e) RESOURCE_ESTIMATE RESTRUCTURED — stripped to auto-research mode only with day-by-day schedule integrated into the approach section.",
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
  "promptId": "8fa8f109-01fd-483a-ae0a-c4a3b7f43787",
  "type": "user",
  "uuid": "9a6b775c-2166-4b04-8ad4-c4313512bb65",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T06:43:43.373Z_

```json
{
  "parentUuid": "9a6b775c-2166-4b04-8ad4-c4313512bb65",
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
  "uuid": "e3d4c7f8-356d-4691-82e2-18ce644f92fb",
  "timestamp": "2026-05-10T06:43:43.373Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T06:43:43.374Z_

```json
{
  "parentUuid": "e3d4c7f8-356d-4691-82e2-18ce644f92fb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4fc8cccf-fbf1-4730-ae54-f680312292b4",
  "timestamp": "2026-05-10T06:43:43.374Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826",
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
  "leafUuid": "4fc8cccf-fbf1-4730-ae54-f680312292b4",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Failure-Type-Conditioned Retrieval for Multi-Language Repository Repair",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826"
}
```

---

### Assistant

_source line 8 · 2026-05-10T06:43:53.669Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this idea carefully. This is Round 6 of 10, and I need to conduct an adversarial review of the FTCR (Failure-Type-Conditioned Retrieval Augmentation for Repository Repair) proposal. 

Let me first understand what's been addressed from Round 5:
1. VENUE RESTORED - EMNLP 2026 ARR (May 25) reinstated as primary target with day-by-day schedule
2. INFERFIX ADDED - InferFix (ESEC/FSE 2023) added throughout with three-point differentiation


3. CORPUS CONFOUND EXPLICIT - intra-corpus ablations framed as clean test
4. TYPEREPAIR EVIDENTIARY BASIS - differentiation claim supported by evaluation design argument
5. RESOURCE_ESTIMATE RESTRUCTURED - stripped to auto-research mode only

Now I need to independently verify the claims and identify remaining issues. Let me search for current SOTA on relevant benchmarks, whether cited papers exist and their claims are accurate, any competitive or concurrent works that might have been missed, feasibility of the timeline and resource estimates, and confirm whether the EMNLP 2026 ARR deadline is actually May 25, 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fc8cccf-fbf1-4730-ae54-f680312292b4",
  "isSidechain": false,
  "requestId": "req_011CatSBtXkLsS8PEjXdGXmy",
  "type": "assistant",
  "uuid": "ed74dc2d-1d2e-46fe-80e2-7983399b8743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XVsNVw5mzfmWHVAQKWcnZP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26504,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1919,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26504,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1919,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26504,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26504
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

_source line 9 · 2026-05-10T06:43:53.671Z_

I'll conduct targeted web searches to independently verify the key claims in this Round 6 proposal before issuing my verdict.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed74dc2d-1d2e-46fe-80e2-7983399b8743",
  "isSidechain": false,
  "requestId": "req_011CatSBtXkLsS8PEjXdGXmy",
  "type": "assistant",
  "uuid": "9b85ff2e-4ba5-45f0-b030-92c8af4933ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XVsNVw5mzfmWHVAQKWcnZP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26504,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1919,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26504,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1919,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26504,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26504
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

_source line 10 · 2026-05-10T06:44:13.171Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KBvMM4MXW9omkg7pRgcRfz`</summary>

```json
{
  "description": "Verify FTCR paper claims and search for competing work",
  "subagent_type": "Explore",
  "prompt": "I'm conducting an adversarial review of a research proposal called FTCR (Failure-Type-Conditioned Retrieval Augmentation for Repository Repair). I need you to search the web to independently verify several claims and find any competing work the proposal may have missed.\n\nPlease search for ALL of the following, using WebSearch and WebFetch as needed:\n\n1. Search \"EMNLP 2026 ARR deadline May 2026\" to verify whether the ARR submission deadline is actually May 25, 2026. Check https://2026.emnlp.org or official EMNLP 2026 pages.\n\n2. Search \"InferFix end-to-end program repair LLMs bug-specific retrieval arXiv 2303.07263\" - verify this paper exists and check its claims about type-aware retrieval, particularly whether it uses soft contrastive similarity (not hard index partitioning).\n\n3. Search \"ReinFix repair ingredients ICSE 2026 arXiv 2506.23100\" - verify this paper's existence and its mechanism (soft root-cause augmented retrieval with text-embedding-3-large on TRANSFER corpus).\n\n4. Search \"SWE-Exp experience-driven software issue resolution arXiv 2507.23361\" - check if this paper uses soft cosine similarity for type-based retrieval, and its SWE-bench Verified score.\n\n5. Search \"TypeRepair defect-type-aware adaptive program repair Zhang SQJ 2026\" OR \"doi 10.1007/s11219-026-09751-w\" - check whether TypeRepair uses within-project or cross-repository retrieval.\n\n6. Search \"DebugBench evaluating debugging capability large language models\" - verify it has 4,253 instances with 18-category ground-truth type annotations across C++/Java/Python.\n\n7. Search \"hard vs soft retrieval partitioning bug type program repair 2025 2026\" - look for any papers that directly compare hard categorical index partitioning vs soft type-conditioned retrieval for code repair.\n\n8. Search \"M-RAG multiple partitions retrieval augmented generation ACL 2024 arXiv 2405.16420\" - verify this paper and its claimed improvements (+11% summarization, +8% translation, +12% dialogue).\n\n9. Search \"CRAG corrective retrieval augmented generation arXiv 2401.15884 ICLR\" - confirm it was submitted to ICLR 2025 but withdrawn (never published at ICLR).\n\n10. Search \"SWE-bench Lite SOTA 2026\" to check if 62.7% is actually the current SOTA.\n\n11. Search \"code repair type-conditioned cross-repository retrieval 2025 2026\" - any concurrent work doing type-conditioned cross-repo retrieval that isn't cited.\n\n12. Search \"GitBug-Java reproducible benchmark Java bugs MSR 2024 arXiv 2402.02961\" - verify it has 199 Java bugs in isolated Docker environments.\n\nFor each search, report what you found - whether claims are verified, and any important discrepancies or competing papers found. Be specific about what each paper actually says vs. what the proposal claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b85ff2e-4ba5-45f0-b030-92c8af4933ed",
  "isSidechain": false,
  "requestId": "req_011CatSBtXkLsS8PEjXdGXmy",
  "type": "assistant",
  "uuid": "228fdae8-6222-4c1b-9e2e-116994274d27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XVsNVw5mzfmWHVAQKWcnZP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26504,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1919,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26504,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1919,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26504,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26504
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

_source line 11 · 2026-05-10T06:44:25.518Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01J1xomDMV3wfd8QtXnyDdQE`</summary>

```json
{
  "description": "Search for novelty threats and concurrent work for FTCR",
  "subagent_type": "Explore",
  "prompt": "I'm conducting an adversarial review of a research proposal about retrieval-augmented program repair using bug type categorization. The proposal is called FTCR (Failure-Type-Conditioned Retrieval Augmentation for Repository Repair). I need to find any competing or concurrent work that might undermine the novelty claims.\n\nThe core idea: classify bugs into one of 18 semantic types (null dereference, off-by-one, API misuse, etc.), then retrieve fixes ONLY from a type-matched sub-index (hard partitioning at corpus construction time), rather than retrieving from a unified index using soft similarity. Compare against soft retrieval baselines (InferFix's contrastive type embedding, ReinFix's root-cause-augmented embedding).\n\nPlease search for:\n\n1. \"type-aware program repair retrieval 2024 2025 2026\" - any papers using type-conditioned retrieval for code repair\n2. \"categorical retrieval partitioning code repair\" OR \"hard partitioning retrieval bug fix\" - any papers using hard index partitioning for code repair\n3. \"bug taxonomy retrieval augmented repair LLM\" - papers combining bug taxonomies with retrieval\n4. \"arXiv 2025 2026 program repair type retrieval benchmark\" - recent papers on type-guided repair\n5. site:arxiv.org \"type-conditioned\" \"program repair\" 2025 - arxiv papers on this topic\n6. site:arxiv.org \"defect type\" \"retrieval\" \"program repair\" 2025 2026\n7. \"cross-repository program repair retrieval 2025 2026\" - concurrent cross-repo repair papers\n8. \"PatchRecall arXiv 2604.10481\" - verify this paper's scope (file-level localization, not type-conditioned retrieval)\n9. \"DynaFix iterative automated program repair dynamic information arXiv 2512.24635\" - verify this paper and its Defects4J V2.0 results\n10. \"DebugRepair self-directed debugging arXiv 2604.19305\" - verify this paper's Defects4J results (295 bugs with DeepSeek-V3)\n11. \"ReCode fine-grained retrieval augmented code repair CIKM 2025\" OR \"arXiv 2509.02330\" - verify ReCode's mechanism (algorithm-type-conditioned retrieval in competitive programming)\n12. \"semantic type partitioning retrieval augmented generation\" - any NLP papers using semantic type partitioning for RAG\n\nFocus especially on papers from 2025-2026 that might do hard type partitioning or very similar mechanisms to FTCR. Report actual findings with paper titles, venues, and key claims."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "228fdae8-6222-4c1b-9e2e-116994274d27",
  "isSidechain": false,
  "requestId": "req_011CatSBtXkLsS8PEjXdGXmy",
  "type": "assistant",
  "uuid": "75687e16-c5d3-4234-b332-bcd756085db4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XVsNVw5mzfmWHVAQKWcnZP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26504,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1919,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26504,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1919,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26504,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26504
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

_source line 12 · 2026-05-10T06:45:59.537Z_

<details><summary>↩ Tool result · `toolu_01KBvMM4MXW9omkg7pRgcRfz`</summary>

```text
Perfect. Now let me compile my comprehensive findings report. Let me organize all the verification results:

## ADVERSARIAL REVIEW: FTCR CLAIMS VERIFICATION REPORT

Based on my comprehensive web search and analysis, here are my findings for each claim in the FTCR proposal:

---

### 1. **EMNLP 2026 ARR Deadline (May 25, 2026)** ✓ VERIFIED
**Status: CORRECT**
- The ARR submission deadline for EMNLP 2026 is confirmed as May 25, 2026
- Critical policy note: Authors must explicitly select between EMNLP and AACL at submission time (this choice is binding)
- Reviewer registration deadline: May 27, 2026
- Meta reviews released: July 30, 2026

**Sources:** Official EMNLP 2026 website and X announcements confirm this deadline.

---

### 2. **InferFix (arXiv 2303.07263)** - PARTIAL VERIFICATION WITH IMPORTANT DETAILS
**Status: PAPER EXISTS, BUT CLAIMS NEED CLARIFICATION**

**What the paper actually does:**
- InferFix uses a **contrastive learning objective** for its retriever (transformer encoder model)
- The retriever aims at "searching for semantically equivalent bugs and corresponding fixes"
- The system includes **bug type annotations** as part of prompt augmentation alongside retrieved fixes
- Uses a finetuned 12B Codex model (generator)
- Uses an external non-parametric memory database of historical fixes

**Critical finding:** The proposal claims InferFix uses "soft contrastive similarity" for type-aware retrieval. However, InferFix actually uses contrastive learning for **semantic similarity** between bugs/fixes—this is not the same as "type-conditioned" retrieval. Bug types are added as **annotations in prompts**, not used as a hard retrieval index. The paper retrieves based on semantic similarity, not by type partitioning.

**Performance:** 76.8% top-1 accuracy on Java bugs (InferredBugs dataset)

---

### 3. **ReinFix (arXiv 2506.23100)** - VERIFIED BUT DETAILS MISSING FROM ABSTRACTS
**Status: PAPER EXISTS AT ICSE 2026**

**What is confirmed:**
- Published at ICSE 2026 (48th International Conference on Software Engineering, April 2026)
- Repairs 146 bugs on Defects4J V1.2 (32 more than baselines)
- On Defects4J V2.0: 38 more bugs fixed than SOTA
- Framework enables LLMs to search for "repair ingredients" during both reasoning and solution phases
- Uses "root cause" information to guide repair ingredient search

**NOT verified from abstracts:** The specific claim about text-embedding-3-large and TRANSFER corpus cannot be confirmed from available abstract/summary data. Full paper analysis would be needed.

**Key mechanism:** Searches for historical bug fixes with "similar bug patterns" using both buggy code AND root cause information.

---

### 4. **SWE-Exp (arXiv 2507.23361)** - IMPORTANT DISCREPANCY FOUND
**Status: PAPER EXISTS BUT CLAIMED SCORE IS DIFFERENT**

**Critical finding:**
- The proposal may claim SWE-Exp uses "soft cosine similarity for type-based retrieval" — this specific claim cannot be verified from abstracts
- **SWE-bench Verified score reported in paper: 73.0% Pass@1** (using Claude 4 Sonnet)
- This is HIGHER than the SOTA claim of 62.7% for SWE-bench Lite

**Methodology confirmed:** SWE-Exp is "experience-enhanced" and extracts reusable knowledge from prior agent trajectories at different levels.

**Discrepancy:** If the proposal claims SWE-Exp achieved 62.7%, this appears to be incorrect or referring to a different benchmark (possibly SWE-bench Lite vs. SWE-bench Verified confusion).

---

### 5. **TypeRepair (DOI 10.1007/s11219-026-09751-w)** - CANNOT FULLY VERIFY DUE TO PAYWALL
**Status: PAPER EXISTS, SCOPE CANNOT BE CONFIRMED**

**What is confirmed:**
- Published in Software Quality Journal, 2026 by Zhang, R., Zhang, S. & Xie, L.
- Multi-stage framework: defect localization → defect type identification → context selection → patch generation
- On Defects4J v2.0: 272.73% improvement with GPT-3.5, 257.89% improvement with GPT-4

**Cannot verify:** Whether TypeRepair uses within-project or cross-repository retrieval. The Springer link is behind a paywall, and search results don't clarify the retrieval scope claim.

---

### 6. **DebugBench** - SLIGHT DISCREPANCY IN CATEGORIZATION
**Status: VERIFIED BUT CLAIM MAY BE SLIGHTLY INACCURATE**

**What the paper actually has:**
- 4,253 instances covering **4 major bug categories and 18 minor types** in C++, Java, and Python
- Published in ACL 2024 (Findings)

**Potential discrepancy:** The proposal states "18-category ground-truth type annotations" — the paper actually has **4 major + 18 minor types**, not just 18 categories. This is an accurate technical detail but the phrasing in the proposal might be slightly misleading about the structure.

**Coverage verified:** C++, Java, Python with quality checks to minimize data leakage (code snippets from after July 2022).

---

### 7. **Hard vs. Soft Retrieval Partitioning** - NO COMPARABLE WORK FOUND
**Status: NO DIRECTLY COMPARATIVE WORK IDENTIFIED**

**Finding:** I found NO published papers in 2025-2026 that directly compare "hard categorical index partitioning vs soft type-conditioned retrieval" for code repair. This appears to be a novel contribution or positioning of FTCR.

**Related work found instead:**
- ReCode (2509.02330): Algorithm-aware categorization + fine-grained retrieval
- ARSP (2508.16517): Semantic partitioning of modules
- Various retrieval-augmented approaches, but none explicitly framing the hard vs. soft distinction

**Assessment:** This comparison framework may be novel to FTCR, or the proposal may be positioning existing work differently than the original papers.

---

### 8. **M-RAG (arXiv 2405.16420)** ✓ VERIFIED
**Status: CORRECT**

**Confirmed improvements:**
- +11% on text summarization
- +8% on machine translation
- +12% on dialogue generation

**Conference:** ACL 2024 (Proceedings of 62nd Annual Meeting)

**Key innovation:** Multiple database partitions as basic RAG units, optimized via Multi-Agent Reinforcement Learning

---

### 9. **CRAG (arXiv 2401.15884)** ✓ VERIFIED
**Status: CORRECT REGARDING ICLR SUBMISSION**

**Confirmed:**
- Submitted to ICLR 2025
- **WITHDRAWN submission** (confirmed via OpenReview: https://openreview.net/forum?id=JnWJbrnaUE)
- Never published at ICLR

**Important note:** The paper remains on arXiv and is available; it was withdrawn from ICLR 2025 but not removed from arxiv or academic circulation.

---

### 10. **SWE-bench Lite SOTA (62.7%)** ✓ VERIFIED
**Status: CORRECT AS OF MAY 2026**

**Current SOTA:** Claude Opus 4.6 with 62.7% on SWE-bench Lite (as of May 9, 2026)

**Top performers:**
1. Claude Opus 4.6: 62.7%
2. Claude Opus 4.6: 62.7%
3. MiniMax M2.5: 56.3%

Note: 62 models evaluated with average 26.8%, std dev 19.9%

---

### 11. **Type-Conditioned Cross-Repo Retrieval Concurrent Work** - LIMITED FINDINGS
**Status: SOME RELATED WORK, NO EXACT DUPLICATE**

**Related work found but not exact duplicates:**
- RepoRepair (2603.01048): Documentation-enhanced repository-level repair
- CI-Repair-Bench (2604.27148): Repository-aware benchmark for patch validation
- Various retrieval-augmented code generation surveys (2510.04905)

**Assessment:** No paper found doing exactly "type-conditioned cross-repository retrieval" with the explicit framing FTCR uses. Closest works use other approaches (documentation-enhanced, CI-aware, general retrieval-augmented).

---

### 12. **GitBug-Java (arXiv 2402.02961)** ✓ VERIFIED
**Status: CORRECT**

**Confirmed details:**
- 199 Java bugs from 55 open-source repositories
- MSR 2024 (21st International Conference on Mining Software Repositories)
- All bugs from 2023 (after LLM training cutoffs)
- Reproducible environments using GitHub Actions framework
- Docker-based isolated execution

---

## SUMMARY OF DISCREPANCIES AND MISSING VERIFICATIONS

| Claim | Status | Issue |
|-------|--------|-------|
| ARR May 25 deadline | ✓ Verified | None |
| InferFix soft contrastive | ⚠️ Partially verified | Uses contrastive learning for semantic similarity, not type partitioning; bug types added as annotations |
| ReinFix text-embedding-3-large | ✗ Not verifiable | Cannot confirm from available abstracts |
| SWE-Exp type-based retrieval | ✗ Not verifiable | Cannot confirm soft cosine similarity claim |
| SWE-Exp 62.7% score | ✗ Incorrect | Paper reports 73.0% on SWE-bench Verified |
| TypeRepair cross-repo scope | ✗ Not verifiable | Springer paywall; scope cannot be confirmed |
| DebugBench categories | ✓ Verified | 4 major + 18 minor types (phrasing nuance) |
| Hard vs. soft comparison | ✗ No comparable work | No papers found making this explicit comparison |
| M-RAG improvements | ✓ Verified | All three percentages correct |
| CRAG withdrawn | ✓ Verified | Correct, confirmed on OpenReview |
| SWE-bench Lite SOTA | ✓ Verified | 62.7% correct as of May 2026 |
| Type-conditioned cross-repo | ⚠️ Limited findings | Related work exists but no exact duplicate found |
| GitBug-Java | ✓ Verified | 199 bugs confirmed |

---

## KEY OBSERVATIONS FOR ADVERSARIAL REVIEW

1. **Methodological distinctions matter:** InferFix uses semantic contrastive similarity with type annotations, not type-conditioned partitioning. The proposal should clarify how FTCR's approach differs fundamentally.

2. **Score discrepancy:** SWE-Exp's actual reported score (73.0%) is significantly higher than what might be claimed. Verify which paper/benchmark this refers to.

3. **Verification limitations:** Several key implementation details (ReinFix's embeddings, SWE-Exp's retrieval method, TypeRepair's scope) cannot be verified from available abstracts/summaries, suggesting the proposal may be inferring implementation details not explicitly stated in papers.

4. **No comparative framework found:** The hard vs. soft retrieval partitioning framing appears novel—neither existing papers nor comparative studies frame the distinction this way, which could be a strength (novel insight) or weakness (unclear positioning relative to actual prior work).

5. **Related but distinct work:** ReCode and other fine-grained retrieval approaches exist but with different mechanisms than type-conditioned retrieval.

---

**Sources:**
- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)
- [InferFix arXiv](https://arxiv.org/abs/2303.07263)
- [ReinFix arXiv](https://arxiv.org/abs/2506.23100)
- [SWE-Exp arXiv](https://arxiv.org/abs/2507.23361)
- [TypeRepair SQJ](https://link.springer.com/article/10.1007/s11219-026-09751-w)
- [DebugBench ACL](https://aclanthology.org/2024.findings-acl.247/)
- [M-RAG ACL](https://aclanthology.org/2024.acl-long.108/)
- [CRAG OpenReview](https://openreview.net/forum?id=JnWJbrnaUE)
- [SWE-bench Leaderboard](https://www.swebench.com/)
- [GitBug-Java arXiv](https://arxiv.org/abs/2402.02961)
- [RepoRepair arXiv](https://arxiv.org/html/2603.01048)
- [ReCode arXiv](https://arxiv.org/html/2509.02330)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "228fdae8-6222-4c1b-9e2e-116994274d27",
  "isSidechain": false,
  "promptId": "8fa8f109-01fd-483a-ae0a-c4a3b7f43787",
  "type": "user",
  "uuid": "4bdb0165-eb4e-4e5f-95b4-c4b890d27904",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm conducting an adversarial review of a research proposal called FTCR (Failure-Type-Conditioned Retrieval Augmentation for Repository Repair). I need you to search the web to independently verify several claims and find any competing work the proposal may have missed.\n\nPlease search for ALL of the following, using WebSearch and WebFetch as needed:\n\n1. Search \"EMNLP 2026 ARR deadline May 2026\" to verify whether the ARR submission deadline is actually May 25, 2026. Check https://2026.emnlp.org or official EMNLP 2026 pages.\n\n2. Search \"InferFix end-to-end program repair LLMs bug-specific retrieval arXiv 2303.07263\" - verify this paper exists and check its claims about type-aware retrieval, particularly whether it uses soft contrastive similarity (not hard index partitioning).\n\n3. Search \"ReinFix repair ingredients ICSE 2026 arXiv 2506.23100\" - verify this paper's existence and its mechanism (soft root-cause augmented retrieval with text-embedding-3-large on TRANSFER corpus).\n\n4. Search \"SWE-Exp experience-driven software issue resolution arXiv 2507.23361\" - check if this paper uses soft cosine similarity for type-based retrieval, and its SWE-bench Verified score.\n\n5. Search \"TypeRepair defect-type-aware adaptive program repair Zhang SQJ 2026\" OR \"doi 10.1007/s11219-026-09751-w\" - check whether TypeRepair uses within-project or cross-repository retrieval.\n\n6. Search \"DebugBench evaluating debugging capability large language models\" - verify it has 4,253 instances with 18-category ground-truth type annotations across C++/Java/Python.\n\n7. Search \"hard vs soft retrieval partitioning bug type program repair 2025 2026\" - look for any papers that directly compare hard categorical index partitioning vs soft type-conditioned retrieval for code repair.\n\n8. Search \"M-RAG multiple partitions retrieval augmented generation ACL 2024 arXiv 2405.16420\" - verify this paper and its claimed improvements (+11% summarization, +8% translation, +12% dialogue).\n\n9. Search \"CRAG corrective retrieval augmented generation arXiv 2401.15884 ICLR\" - confirm it was submitted to ICLR 2025 but withdrawn (never published at ICLR).\n\n10. Search \"SWE-bench Lite SOTA 2026\" to check if 62.7% is actually the current SOTA.\n\n11. Search \"code repair type-conditioned cross-repository retrieval 2025 2026\" - any concurrent work doing type-conditioned cross-repo retrieval that isn't cited.\n\n12. Search \"GitBug-Java reproducible benchmark Java bugs MSR 2024 arXiv 2402.02961\" - verify it has 199 Java bugs in isolated Docker environments.\n\nFor each search, report what you found - whether claims are verified, and any important discrepancies or competing papers found. Be specific about what each paper actually says vs. what the proposal claims.",
    "agentId": "a9be796eea331c846",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now let me compile my comprehensive findings report. Let me organize all the verification results:\n\n## ADVERSARIAL REVIEW: FTCR CLAIMS VERIFICATION REPORT\n\nBased on my comprehensive web search and analysis, here are my findings for each claim in the FTCR proposal:\n\n---\n\n### 1. **EMNLP 2026 ARR Deadline (May 25, 2026)** ✓ VERIFIED\n**Status: CORRECT**\n- The ARR submission deadline for EMNLP 2026 is confirmed as May 25, 2026\n- Critical policy note: Authors must explicitly select between EMNLP and AACL at submission time (this choice is binding)\n- Reviewer registration deadline: May 27, 2026\n- Meta reviews released: July 30, 2026\n\n**Sources:** Official EMNLP 2026 website and X announcements confirm this deadline.\n\n---\n\n### 2. **InferFix (arXiv 2303.07263)** - PARTIAL VERIFICATION WITH IMPORTANT DETAILS\n**Status: PAPER EXISTS, BUT CLAIMS NEED CLARIFICATION**\n\n**What the paper actually does:**\n- InferFix uses a **contrastive learning objective** for its retriever (transformer encoder model)\n- The retriever aims at \"searching for semantically equivalent bugs and corresponding fixes\"\n- The system includes **bug type annotations** as part of prompt augmentation alongside retrieved fixes\n- Uses a finetuned 12B Codex model (generator)\n- Uses an external non-parametric memory database of historical fixes\n\n**Critical finding:** The proposal claims InferFix uses \"soft contrastive similarity\" for type-aware retrieval. However, InferFix actually uses contrastive learning for **semantic similarity** between bugs/fixes—this is not the same as \"type-conditioned\" retrieval. Bug types are added as **annotations in prompts**, not used as a hard retrieval index. The paper retrieves based on semantic similarity, not by type partitioning.\n\n**Performance:** 76.8% top-1 accuracy on Java bugs (InferredBugs dataset)\n\n---\n\n### 3. **ReinFix (arXiv 2506.23100)** - VERIFIED BUT DETAILS MISSING FROM ABSTRACTS\n**Status: PAPER EXISTS AT ICSE 2026**\n\n**What is confirmed:**\n- Published at ICSE 2026 (48th International Conference on Software Engineering, April 2026)\n- Repairs 146 bugs on Defects4J V1.2 (32 more than baselines)\n- On Defects4J V2.0: 38 more bugs fixed than SOTA\n- Framework enables LLMs to search for \"repair ingredients\" during both reasoning and solution phases\n- Uses \"root cause\" information to guide repair ingredient search\n\n**NOT verified from abstracts:** The specific claim about text-embedding-3-large and TRANSFER corpus cannot be confirmed from available abstract/summary data. Full paper analysis would be needed.\n\n**Key mechanism:** Searches for historical bug fixes with \"similar bug patterns\" using both buggy code AND root cause information.\n\n---\n\n### 4. **SWE-Exp (arXiv 2507.23361)** - IMPORTANT DISCREPANCY FOUND\n**Status: PAPER EXISTS BUT CLAIMED SCORE IS DIFFERENT**\n\n**Critical finding:**\n- The proposal may claim SWE-Exp uses \"soft cosine similarity for type-based retrieval\" — this specific claim cannot be verified from abstracts\n- **SWE-bench Verified score reported in paper: 73.0% Pass@1** (using Claude 4 Sonnet)\n- This is HIGHER than the SOTA claim of 62.7% for SWE-bench Lite\n\n**Methodology confirmed:** SWE-Exp is \"experience-enhanced\" and extracts reusable knowledge from prior agent trajectories at different levels.\n\n**Discrepancy:** If the proposal claims SWE-Exp achieved 62.7%, this appears to be incorrect or referring to a different benchmark (possibly SWE-bench Lite vs. SWE-bench Verified confusion).\n\n---\n\n### 5. **TypeRepair (DOI 10.1007/s11219-026-09751-w)** - CANNOT FULLY VERIFY DUE TO PAYWALL\n**Status: PAPER EXISTS, SCOPE CANNOT BE CONFIRMED**\n\n**What is confirmed:**\n- Published in Software Quality Journal, 2026 by Zhang, R., Zhang, S. & Xie, L.\n- Multi-stage framework: defect localization → defect type identification → context selection → patch generation\n- On Defects4J v2.0: 272.73% improvement with GPT-3.5, 257.89% improvement with GPT-4\n\n**Cannot verify:** Whether TypeRepair uses within-project or cross-repository retrieval. The Springer link is behind a paywall, and search results don't clarify the retrieval scope claim.\n\n---\n\n### 6. **DebugBench** - SLIGHT DISCREPANCY IN CATEGORIZATION\n**Status: VERIFIED BUT CLAIM MAY BE SLIGHTLY INACCURATE**\n\n**What the paper actually has:**\n- 4,253 instances covering **4 major bug categories and 18 minor types** in C++, Java, and Python\n- Published in ACL 2024 (Findings)\n\n**Potential discrepancy:** The proposal states \"18-category ground-truth type annotations\" — the paper actually has **4 major + 18 minor types**, not just 18 categories. This is an accurate technical detail but the phrasing in the proposal might be slightly misleading about the structure.\n\n**Coverage verified:** C++, Java, Python with quality checks to minimize data leakage (code snippets from after July 2022).\n\n---\n\n### 7. **Hard vs. Soft Retrieval Partitioning** - NO COMPARABLE WORK FOUND\n**Status: NO DIRECTLY COMPARATIVE WORK IDENTIFIED**\n\n**Finding:** I found NO published papers in 2025-2026 that directly compare \"hard categorical index partitioning vs soft type-conditioned retrieval\" for code repair. This appears to be a novel contribution or positioning of FTCR.\n\n**Related work found instead:**\n- ReCode (2509.02330): Algorithm-aware categorization + fine-grained retrieval\n- ARSP (2508.16517): Semantic partitioning of modules\n- Various retrieval-augmented approaches, but none explicitly framing the hard vs. soft distinction\n\n**Assessment:** This comparison framework may be novel to FTCR, or the proposal may be positioning existing work differently than the original papers.\n\n---\n\n### 8. **M-RAG (arXiv 2405.16420)** ✓ VERIFIED\n**Status: CORRECT**\n\n**Confirmed improvements:**\n- +11% on text summarization\n- +8% on machine translation\n- +12% on dialogue generation\n\n**Conference:** ACL 2024 (Proceedings of 62nd Annual Meeting)\n\n**Key innovation:** Multiple database partitions as basic RAG units, optimized via Multi-Agent Reinforcement Learning\n\n---\n\n### 9. **CRAG (arXiv 2401.15884)** ✓ VERIFIED\n**Status: CORRECT REGARDING ICLR SUBMISSION**\n\n**Confirmed:**\n- Submitted to ICLR 2025\n- **WITHDRAWN submission** (confirmed via OpenReview: https://openreview.net/forum?id=JnWJbrnaUE)\n- Never published at ICLR\n\n**Important note:** The paper remains on arXiv and is available; it was withdrawn from ICLR 2025 but not removed from arxiv or academic circulation.\n\n---\n\n### 10. **SWE-bench Lite SOTA (62.7%)** ✓ VERIFIED\n**Status: CORRECT AS OF MAY 2026**\n\n**Current SOTA:** Claude Opus 4.6 with 62.7% on SWE-bench Lite (as of May 9, 2026)\n\n**Top performers:**\n1. Claude Opus 4.6: 62.7%\n2. Claude Opus 4.6: 62.7%\n3. MiniMax M2.5: 56.3%\n\nNote: 62 models evaluated with average 26.8%, std dev 19.9%\n\n---\n\n### 11. **Type-Conditioned Cross-Repo Retrieval Concurrent Work** - LIMITED FINDINGS\n**Status: SOME RELATED WORK, NO EXACT DUPLICATE**\n\n**Related work found but not exact duplicates:**\n- RepoRepair (2603.01048): Documentation-enhanced repository-level repair\n- CI-Repair-Bench (2604.27148): Repository-aware benchmark for patch validation\n- Various retrieval-augmented code generation surveys (2510.04905)\n\n**Assessment:** No paper found doing exactly \"type-conditioned cross-repository retrieval\" with the explicit framing FTCR uses. Closest works use other approaches (documentation-enhanced, CI-aware, general retrieval-augmented).\n\n---\n\n### 12. **GitBug-Java (arXiv 2402.02961)** ✓ VERIFIED\n**Status: CORRECT**\n\n**Confirmed details:**\n- 199 Java bugs from 55 open-source repositories\n- MSR 2024 (21st International Conference on Mining Software Repositories)\n- All bugs from 2023 (after LLM training cutoffs)\n- Reproducible environments using GitHub Actions framework\n- Docker-based isolated execution\n\n---\n\n## SUMMARY OF DISCREPANCIES AND MISSING VERIFICATIONS\n\n| Claim | Status | Issue |\n|-------|--------|-------|\n| ARR May 25 deadline | ✓ Verified | None |\n| InferFix soft contrastive | ⚠️ Partially verified | Uses contrastive learning for semantic similarity, not type partitioning; bug types added as annotations |\n| ReinFix text-embedding-3-large | ✗ Not verifiable | Cannot confirm from available abstracts |\n| SWE-Exp type-based retrieval | ✗ Not verifiable | Cannot confirm soft cosine similarity claim |\n| SWE-Exp 62.7% score | ✗ Incorrect | Paper reports 73.0% on SWE-bench Verified |\n| TypeRepair cross-repo scope | ✗ Not verifiable | Springer paywall; scope cannot be confirmed |\n| DebugBench categories | ✓ Verified | 4 major + 18 minor types (phrasing nuance) |\n| Hard vs. soft comparison | ✗ No comparable work | No papers found making this explicit comparison |\n| M-RAG improvements | ✓ Verified | All three percentages correct |\n| CRAG withdrawn | ✓ Verified | Correct, confirmed on OpenReview |\n| SWE-bench Lite SOTA | ✓ Verified | 62.7% correct as of May 2026 |\n| Type-conditioned cross-repo | ⚠️ Limited findings | Related work exists but no exact duplicate found |\n| GitBug-Java | ✓ Verified | 199 bugs confirmed |\n\n---\n\n## KEY OBSERVATIONS FOR ADVERSARIAL REVIEW\n\n1. **Methodological distinctions matter:** InferFix uses semantic contrastive similarity with type annotations, not type-conditioned partitioning. The proposal should clarify how FTCR's approach differs fundamentally.\n\n2. **Score discrepancy:** SWE-Exp's actual reported score (73.0%) is significantly higher than what might be claimed. Verify which paper/benchmark this refers to.\n\n3. **Verification limitations:** Several key implementation details (ReinFix's embeddings, SWE-Exp's retrieval method, TypeRepair's scope) cannot be verified from available abstracts/summaries, suggesting the proposal may be inferring implementation details not explicitly stated in papers.\n\n4. **No comparative framework found:** The hard vs. soft retrieval partitioning framing appears novel—neither existing papers nor comparative studies frame the distinction this way, which could be a strength (novel insight) or weakness (unclear positioning relative to actual prior work).\n\n5. **Related but distinct work:** ReCode and other fine-grained retrieval approaches exist but with different mechanisms than type-conditioned retrieval.\n\n---\n\n**Sources:**\n- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)\n- [InferFix arXiv](https://arxiv.org/abs/2303.07263)\n- [ReinFix arXiv](https://arxiv.org/abs/2506.23100)\n- [SWE-Exp arXiv](https://arxiv.org/abs/2507.23361)\n- [TypeRepair SQJ](https://link.springer.com/article/10.1007/s11219-026-09751-w)\n- [DebugBench ACL](https://aclanthology.org/2024.findings-acl.247/)\n- [M-RAG ACL](https://aclanthology.org/2024.acl-long.108/)\n- [CRAG OpenReview](https://openreview.net/forum?id=JnWJbrnaUE)\n- [SWE-bench Leaderboard](https://www.swebench.com/)\n- [GitBug-Java arXiv](https://arxiv.org/abs/2402.02961)\n- [RepoRepair arXiv](https://arxiv.org/html/2603.01048)\n- [ReCode arXiv](https://arxiv.org/html/2509.02330)"
      }
    ],
    "totalDurationMs": 106358,
    "totalTokens": 40430,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 984,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 35504,
      "output_tokens": 3263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 679
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 984,
          "output_tokens": 3263,
          "cache_read_input_tokens": 35504,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 679,
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
      "otherToolCount": 23
    }
  },
  "sourceToolAssistantUUID": "228fdae8-6222-4c1b-9e2e-116994274d27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826",
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
  "leafUuid": "4bdb0165-eb4e-4e5f-95b4-c4b890d27904",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Failure-Type-Conditioned Retrieval for Multi-Language Repository Repair",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826"
}
```

---

### Tool result

_source line 15 · 2026-05-10T06:46:21.898Z_

<details><summary>↩ Tool result · `toolu_01J1xomDMV3wfd8QtXnyDdQE`</summary>

```text
Now let me compile a comprehensive report based on all the findings.

## COMPREHENSIVE ADVERSARIAL REVIEW: Competing and Concurrent Work on Type-Aware Program Repair Retrieval

Based on systematic web searches, I have identified the following relevant competing or concurrent work that could challenge the novelty claims of FTCR (Failure-Type-Conditioned Retrieval Augmentation for Repository Repair):

---

### **CRITICAL FINDING: ReCode (arXiv:2509.02330) - DIRECT COMPETITOR**

**Title:** ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation

**Publication:** September 2, 2025 | Accepted to CIKM 2025

**Key Mechanism:** Algorithm-type-conditioned retrieval with hard partitioning
- Predicts multiple algorithm type labels for buggy code
- Performs semantic retrieval in **parallel across sub-knowledge bases** using predicted labels
- Uses dual encoding strategy (textual + code features)
- Creates separate retrieval indexes by algorithm type

**Critical Overlap with FTCR:** ReCode uses hard partitioning of retrieval corpus by algorithm type (similar to FTCR's 18 semantic bug types), rather than soft similarity-based retrieval. This directly parallels FTCR's claimed innovation of type-matched sub-index retrieval vs. unified index soft similarity approaches.

**Novelty Impact:** This is **not a direct duplicate** but demonstrates the same core principle (type-conditioned hard partitioning vs. soft similarity) in the competitive programming domain. If FTCR claims the hard partitioning approach is novel, ReCode's acceptance at CIKM 2025 challenges this.

---

### **TypeRepair (Software Quality Journal 2026) - SEMANTIC BUG TYPE CLASSIFICATION**

**Title:** Towards defect-type-aware adaptive program repair: A stage-wise approach with large language models

**Publication:** 2026 | Software Quality Journal, Vol. 34, Article 14

**Authors:** Zhang, R., Zhang, S., Xie, L.

**Key Features:**
- Divides APR into four stages: defect localization → **defect type identification** → context selection → patch generation
- Defines 10 common defect types with tailored repair guidance per type
- Achieves 272.73% improvement over baseline on Defects4J v2.0 (GPT-3.5)
- Independently repairs 33 bugs not fixed by other methods

**Overlap with FTCR:** Like FTCR, this work uses defect type classification to guide repair. However, TypeRepair uses soft type-aware guidance in the prompt, not hard index partitioning. **Not a direct threat to FTCR's hard partitioning novelty**, but demonstrates active academic interest in type-aware repair.

---

### **DebugRepair (arXiv:2604.19305) - RUNTIME-GUIDED REPAIR**

**Title:** DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging

**Publication:** April 2026

**Key Results:**
- With DeepSeek-V3: **295 bugs fixed on Defects4J**
- Outperforms second-best baseline by 59 fixes
- Uses simulated instrumentation + debugging-driven conversational repair
- Hierarchically iterative framework

**Overlap with FTCR:** None in terms of retrieval methodology. DebugRepair is orthogonal—it uses runtime traces instead of static type classification. However, it achieves stronger results on Defects4J v2.0 (295 vs. reported numbers for other approaches), which could be a **competitive benchmark claim** if FTCR also uses Defects4J v2.0.

---

### **DynaFix (arXiv:2512.24635) - EXECUTION-DRIVEN ITERATIVE REPAIR**

**Title:** DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information

**Publication:** December 31, 2025 (revised April 19, 2026) | NeurIPS 2025

**Key Results:**
- 236 bugs fixed with GPT-4 on Defects4J v2.0
- 186 bugs with GPT-4o (includes 23 bugs not fixed by any baseline)
- 60-70% reduction in token consumption vs. SOTA

**Overlap with FTCR:** None in retrieval methodology. This is an orthogonal approach using dynamic execution traces. Not a direct threat unless FTCR and DynaFix share the same benchmark comparisons.

---

### **InferFix (ESEC/FSE 2023) - CONTRASTIVE TYPE EMBEDDING (YOUR BASELINE)**

**Title:** InferFix: End-to-End Program Repair with LLMs

**Publication:** 2023 | Proceedings of ESEC/FSE 2023 (Industry Track)

**Key Features:**
- Retriever trained with **contrastive learning** objective to find semantically equivalent bugs
- Bug type annotations + semantically similar fixes retrieved from memory
- Deployed at Microsoft alongside Infer static analyzer
- Top-1 accuracy: 65.6% (C#), 76.8% (Java)

**This is your explicitly mentioned soft similarity baseline.** FTCR should compare favorably against InferFix's contrastive embeddings.

---

### **ReinFix (arXiv:2506.23100) - ROOT-CAUSE-AUGMENTED EMBEDDING (YOUR BASELINE)**

**Title:** Repair Ingredients Are All You Need: Improving Large Language Model-Based Program Repair via Repair Ingredients Search

**Publication:** June 2025

**Key Features:**
- Retrieves from vector database of bug-fix pairs
- Uses root cause analysis to guide embedding-based retrieval
- Integrates **internal ingredients** (variable definitions via static analysis) and **external ingredients** (historical bug fixes)
- LLM-based agent searches during both reasoning and solution phases

**This is your explicitly mentioned root-cause-augmented baseline.** FTCR should demonstrate hard partitioning advantages over ReinFix's soft embedding-based retrieval.

---

### **PatchRecall (arXiv:2604.10481) - FILE-LEVEL LOCALIZATION, NOT TYPE-CONDITIONED**

**Title:** PatchRecall: Patch-Driven Retrieval for Automated Program Repair

**Publication:** April 12, 2026

**Key Features:**
- Hybrid retrieval: codebase retrieval + history-based retrieval
- Targets **file-level candidate selection** (not bug type)
- Combines current issue with similar past issues
- Evaluated on SWE-Bench

**Assessment:** As you suspected, PatchRecall is **NOT a competitor** to FTCR on type-conditioned retrieval. It operates at the file/module level, not semantic bug type level. No novelty threat.

---

### **SelRepair (arXiv:2507.10103) - DUAL RETRIEVAL WITH SELECTION GATE**

**Title:** Accelerating Automatic Program Repair with Dual Retrieval-Augmented Fine-Tuning and Patch Generation on Large Language Models

**Publication:** July 14, 2025

**Key Features:**
- Fine-tuned LLM + dual RAG module
- Incorporates **semantic AND syntactic/structural similarity**
- RAG selection gate determines when to add bug-fix pairs
- Results: 26.29% exact match on Java datasets, 6.42% inference speedup

**Overlap with FTCR:** SelRepair uses "dual" retrieval (semantic + structural), not type-conditioned hard partitioning. This is a **soft similarity hybrid approach**, not a hard partitioning strategy. Not a direct threat to FTCR's novelty if FTCR's core claim is type-driven hard partitioning.

---

### **RetypeR (ICSME 2024) - TYPE ERROR REPAIR, LANGUAGE-SPECIFIC**

**Title:** RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors

**Publication:** October 6-11, 2024 | ICSME 2024

**Features:**
- External + internal retrieval stages
- Domain-specific to Python type errors (not general bug categories)
- Retrieval-based framework with integrated approach

**Assessment:** Language-specific (Python) and focused on type errors (a narrow category). Not a general competitor to FTCR's 18-type semantic classification. Limited threat to novelty claims.

---

### **LFTBench & ReduceFix (arXiv:2507.15251) - INPUT REDUCTION, NOT TYPE-AWARE**

**Title:** Input Reduction Enhanced LLM-based Program Repair

**Publication:** July 2025

**Features:**
- LFTBench: 200 real bugs, 1MB median failure-inducing input size
- ReduceFix: custom task-specific input reducer
- Addresses "lost-in-the-middle" problem in long prompts

**Assessment:** Orthogonal to type-based retrieval. Addresses input complexity, not retrieval strategy. No novelty conflict.

---

### **ThinkRepair (ISSTA 2024) - CHAIN-OF-THOUGHT PROMPTING, NOT RETRIEVAL-BASED**

**Title:** ThinkRepair: Self-Directed Automated Program Repair

**Publication:** July 2024 | ISSTA 2024

**Key Features:**
- Chain-of-Thought (CoT) pre-fixed knowledge collection
- Few-shot learning with example selection
- Results: 98 bugs fixed on Defects4J v1.2 (27%-344.4% improvement)

**Assessment:** Focused on prompting strategy and few-shot learning, not on **retrieval corpus partitioning strategy**. Not a direct threat to FTCR's type-partitioned retrieval methodology.

---

### **RepoRepair (arXiv:2603.01048) - DOCUMENTATION-ENHANCED, CROSS-FILE**

**Title:** RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair

**Publication:** March 2026

**Features:**
- Hierarchical code documentation generation
- Cross-file repair via semantic abstractions
- Repository-level context awareness

**Assessment:** Orthogonal—focuses on repository-level multi-file repair, not type-conditioned retrieval indexing. Not a competitor on the hard partitioning approach.

---

### **CPRet Dataset (arXiv:2505.12925) - COMPETITIVE PROGRAMMING RETRIEVAL**

**Title:** CPRet: A Dataset, Benchmark, and Model for Retrieval in Competitive Programming

**Publication:** May 2025

**Features:**
- Problem-code alignment, solution diversity, duplication detection
- Broader temporal coverage, language diversity
- Multiple online judges (ICPC, OI-style problems)

**Assessment:** Dataset for competitive programming, not bug repair. ReCode (your direct competitor) also targets competitive programming bug fixes. This dataset may be used in ReCode-like evaluations.

---

### **Recent Systematic Surveys**

**[2506.23749] A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications**

**Publication:** June 2025

**Coverage:** 62 LLM-based APR systems (Jan 2022 – June 2025)

**Key Framework:**
- Four paradigms: fine-tuning, prompting, procedural pipelines, agentic frameworks
- Cross-cutting layers: RAG and Analysis-Augmented Generation (AAG)
- Notes that **different bug types benefit from different kinds of retrieved context**

**Significance:** This TOSEM 2026-listed survey explicitly acknowledges that bug-type-aware retrieval is an active research area, supporting FTCR's motivation but not directly implementing hard partitioning.

---

## **SUMMARY OF NOVELTY THREATS**

### **CRITICAL THREAT (Direct Competitor):**
- **ReCode (CIKM 2025):** Hard partitioning by algorithm type; parallel sub-index retrieval. Nearly identical mechanism to FTCR but in competitive programming domain (Sept 2025).

### **MODERATE THREATS (Type-Aware but Different Strategy):**
- **TypeRepair (SQJ 2026):** Type-aware repair via stage-wise guidance (soft approach, not hard partitioning)
- **ReinFix (June 2025):** Root-cause-conditioned soft retrieval (explicitly mentioned as your baseline)
- **SelRepair (July 2025):** Dual semantic/structural retrieval with selection gate (soft hybrid)

### **NO THREAT (Orthogonal or Scope-Limited):**
- **DebugRepair, DynaFix:** Runtime/dynamic approaches, not retrieval-partitioning strategies
- **PatchRecall:** File-level, not type-level
- **RetypeR:** Python type errors only, narrow domain
- **ThinkRepair:** Prompting strategy, not retrieval corpus design
- **RepoRepair:** Cross-file documentation, not type partitioning

---

## **CRITICAL TIMING ISSUE**

**ReCode was published September 2, 2025 to arXiv and accepted to CIKM 2025.** If FTCR was submitted around the same time or later, ReCode **predates or is concurrent with FTCR**, directly undermining the novelty claim of "type-conditioned hard partitioning for program repair retrieval."

**Key question for your adversarial review:** When was FTCR submitted to arXiv or to a conference? If after September 2, 2025, ReCode is prior art.

---

## **RECOMMENDATION FOR YOUR REVIEW**

1. **Directly compare FTCR vs. ReCode** on identical benchmarks (Defects4J v2.0, others). If ReCode achieves better results with a nearly identical mechanism, FTCR's contribution is incremental.

2. **Verify claim specificity:** Is FTCR claiming the hard partitioning approach is novel, or the specific set of 18 bug types? If the latter, the novelty bar is lower but still vulnerable to the 10-type TypeRepair or ReCode's algorithm-based partitioning.

3. **Check benchmark overlap:** Do all these papers use Defects4J v2.0? If yes, compare absolute numbers:
   - DynaFix: 236 (GPT-4)
   - DebugRepair: 295 (DeepSeek-V3)
   - TypeRepair: ~272 improvements reported, exact numbers unclear
   - FTCR: ?

4. **Evaluate ReCode's claims vs. FTCR's claims** on whether hard partitioning is truly more effective than soft similarity (InferFix, ReinFix).

---

## **Sources:**

- [ReCode: CIKM 2025](https://arxiv.org/abs/2509.02330)
- [TypeRepair: SQJ 2026](https://link.springer.com/article/10.1007/s11219-026-09751-w)
- [DebugRepair: arXiv 2604.19305](https://arxiv.org/abs/2604.19305)
- [DynaFix: arXiv 2512.24635](https://arxiv.org/abs/2512.24635)
- [InferFix: ESEC/FSE 2023](https://arxiv.org/abs/2303.07263)
- [ReinFix: arXiv 2506.23100](https://arxiv.org/abs/2506.23100)
- [PatchRecall: arXiv 2604.10481](https://arxiv.org/abs/2604.10481)
- [SelRepair: arXiv 2507.10103](https://arxiv.org/abs/2507.10103)
- [RetypeR: ICSME 2024](https://conf.researchr.org/details/icsme-2024/icsme-2024-papers/20/RetypeR-Integrated-Retrieval-based-Automatic-Program-Repair-for-Python-Type-Errors)
- [LFTBench/ReduceFix: arXiv 2507.15251](https://arxiv.org/abs/2507.15251)
- [ThinkRepair: ISSTA 2024](https://arxiv.org/abs/2407.20898)
- [RepoRepair: arXiv 2603.01048](https://arxiv.org/abs/2603.01048)
- [CPRet: arXiv 2505.12925](https://arxiv.org/abs/2505.12925)
- [APR Survey: arXiv 2506.23749](https://arxiv.org/abs/2506.23749)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75687e16-c5d3-4234-b332-bcd756085db4",
  "isSidechain": false,
  "promptId": "8fa8f109-01fd-483a-ae0a-c4a3b7f43787",
  "type": "user",
  "uuid": "c6d5b82a-9f62-4e99-b38a-c01b5f7f699b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm conducting an adversarial review of a research proposal about retrieval-augmented program repair using bug type categorization. The proposal is called FTCR (Failure-Type-Conditioned Retrieval Augmentation for Repository Repair). I need to find any competing or concurrent work that might undermine the novelty claims.\n\nThe core idea: classify bugs into one of 18 semantic types (null dereference, off-by-one, API misuse, etc.), then retrieve fixes ONLY from a type-matched sub-index (hard partitioning at corpus construction time), rather than retrieving from a unified index using soft similarity. Compare against soft retrieval baselines (InferFix's contrastive type embedding, ReinFix's root-cause-augmented embedding).\n\nPlease search for:\n\n1. \"type-aware program repair retrieval 2024 2025 2026\" - any papers using type-conditioned retrieval for code repair\n2. \"categorical retrieval partitioning code repair\" OR \"hard partitioning retrieval bug fix\" - any papers using hard index partitioning for code repair\n3. \"bug taxonomy retrieval augmented repair LLM\" - papers combining bug taxonomies with retrieval\n4. \"arXiv 2025 2026 program repair type retrieval benchmark\" - recent papers on type-guided repair\n5. site:arxiv.org \"type-conditioned\" \"program repair\" 2025 - arxiv papers on this topic\n6. site:arxiv.org \"defect type\" \"retrieval\" \"program repair\" 2025 2026\n7. \"cross-repository program repair retrieval 2025 2026\" - concurrent cross-repo repair papers\n8. \"PatchRecall arXiv 2604.10481\" - verify this paper's scope (file-level localization, not type-conditioned retrieval)\n9. \"DynaFix iterative automated program repair dynamic information arXiv 2512.24635\" - verify this paper and its Defects4J V2.0 results\n10. \"DebugRepair self-directed debugging arXiv 2604.19305\" - verify this paper's Defects4J results (295 bugs with DeepSeek-V3)\n11. \"ReCode fine-grained retrieval augmented code repair CIKM 2025\" OR \"arXiv 2509.02330\" - verify ReCode's mechanism (algorithm-type-conditioned retrieval in competitive programming)\n12. \"semantic type partitioning retrieval augmented generation\" - any NLP papers using semantic type partitioning for RAG\n\nFocus especially on papers from 2025-2026 that might do hard type partitioning or very similar mechanisms to FTCR. Report actual findings with paper titles, venues, and key claims.",
    "agentId": "abc33bd9cecf27f53",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Now let me compile a comprehensive report based on all the findings.\n\n## COMPREHENSIVE ADVERSARIAL REVIEW: Competing and Concurrent Work on Type-Aware Program Repair Retrieval\n\nBased on systematic web searches, I have identified the following relevant competing or concurrent work that could challenge the novelty claims of FTCR (Failure-Type-Conditioned Retrieval Augmentation for Repository Repair):\n\n---\n\n### **CRITICAL FINDING: ReCode (arXiv:2509.02330) - DIRECT COMPETITOR**\n\n**Title:** ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation\n\n**Publication:** September 2, 2025 | Accepted to CIKM 2025\n\n**Key Mechanism:** Algorithm-type-conditioned retrieval with hard partitioning\n- Predicts multiple algorithm type labels for buggy code\n- Performs semantic retrieval in **parallel across sub-knowledge bases** using predicted labels\n- Uses dual encoding strategy (textual + code features)\n- Creates separate retrieval indexes by algorithm type\n\n**Critical Overlap with FTCR:** ReCode uses hard partitioning of retrieval corpus by algorithm type (similar to FTCR's 18 semantic bug types), rather than soft similarity-based retrieval. This directly parallels FTCR's claimed innovation of type-matched sub-index retrieval vs. unified index soft similarity approaches.\n\n**Novelty Impact:** This is **not a direct duplicate** but demonstrates the same core principle (type-conditioned hard partitioning vs. soft similarity) in the competitive programming domain. If FTCR claims the hard partitioning approach is novel, ReCode's acceptance at CIKM 2025 challenges this.\n\n---\n\n### **TypeRepair (Software Quality Journal 2026) - SEMANTIC BUG TYPE CLASSIFICATION**\n\n**Title:** Towards defect-type-aware adaptive program repair: A stage-wise approach with large language models\n\n**Publication:** 2026 | Software Quality Journal, Vol. 34, Article 14\n\n**Authors:** Zhang, R., Zhang, S., Xie, L.\n\n**Key Features:**\n- Divides APR into four stages: defect localization → **defect type identification** → context selection → patch generation\n- Defines 10 common defect types with tailored repair guidance per type\n- Achieves 272.73% improvement over baseline on Defects4J v2.0 (GPT-3.5)\n- Independently repairs 33 bugs not fixed by other methods\n\n**Overlap with FTCR:** Like FTCR, this work uses defect type classification to guide repair. However, TypeRepair uses soft type-aware guidance in the prompt, not hard index partitioning. **Not a direct threat to FTCR's hard partitioning novelty**, but demonstrates active academic interest in type-aware repair.\n\n---\n\n### **DebugRepair (arXiv:2604.19305) - RUNTIME-GUIDED REPAIR**\n\n**Title:** DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging\n\n**Publication:** April 2026\n\n**Key Results:**\n- With DeepSeek-V3: **295 bugs fixed on Defects4J**\n- Outperforms second-best baseline by 59 fixes\n- Uses simulated instrumentation + debugging-driven conversational repair\n- Hierarchically iterative framework\n\n**Overlap with FTCR:** None in terms of retrieval methodology. DebugRepair is orthogonal—it uses runtime traces instead of static type classification. However, it achieves stronger results on Defects4J v2.0 (295 vs. reported numbers for other approaches), which could be a **competitive benchmark claim** if FTCR also uses Defects4J v2.0.\n\n---\n\n### **DynaFix (arXiv:2512.24635) - EXECUTION-DRIVEN ITERATIVE REPAIR**\n\n**Title:** DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information\n\n**Publication:** December 31, 2025 (revised April 19, 2026) | NeurIPS 2025\n\n**Key Results:**\n- 236 bugs fixed with GPT-4 on Defects4J v2.0\n- 186 bugs with GPT-4o (includes 23 bugs not fixed by any baseline)\n- 60-70% reduction in token consumption vs. SOTA\n\n**Overlap with FTCR:** None in retrieval methodology. This is an orthogonal approach using dynamic execution traces. Not a direct threat unless FTCR and DynaFix share the same benchmark comparisons.\n\n---\n\n### **InferFix (ESEC/FSE 2023) - CONTRASTIVE TYPE EMBEDDING (YOUR BASELINE)**\n\n**Title:** InferFix: End-to-End Program Repair with LLMs\n\n**Publication:** 2023 | Proceedings of ESEC/FSE 2023 (Industry Track)\n\n**Key Features:**\n- Retriever trained with **contrastive learning** objective to find semantically equivalent bugs\n- Bug type annotations + semantically similar fixes retrieved from memory\n- Deployed at Microsoft alongside Infer static analyzer\n- Top-1 accuracy: 65.6% (C#), 76.8% (Java)\n\n**This is your explicitly mentioned soft similarity baseline.** FTCR should compare favorably against InferFix's contrastive embeddings.\n\n---\n\n### **ReinFix (arXiv:2506.23100) - ROOT-CAUSE-AUGMENTED EMBEDDING (YOUR BASELINE)**\n\n**Title:** Repair Ingredients Are All You Need: Improving Large Language Model-Based Program Repair via Repair Ingredients Search\n\n**Publication:** June 2025\n\n**Key Features:**\n- Retrieves from vector database of bug-fix pairs\n- Uses root cause analysis to guide embedding-based retrieval\n- Integrates **internal ingredients** (variable definitions via static analysis) and **external ingredients** (historical bug fixes)\n- LLM-based agent searches during both reasoning and solution phases\n\n**This is your explicitly mentioned root-cause-augmented baseline.** FTCR should demonstrate hard partitioning advantages over ReinFix's soft embedding-based retrieval.\n\n---\n\n### **PatchRecall (arXiv:2604.10481) - FILE-LEVEL LOCALIZATION, NOT TYPE-CONDITIONED**\n\n**Title:** PatchRecall: Patch-Driven Retrieval for Automated Program Repair\n\n**Publication:** April 12, 2026\n\n**Key Features:**\n- Hybrid retrieval: codebase retrieval + history-based retrieval\n- Targets **file-level candidate selection** (not bug type)\n- Combines current issue with similar past issues\n- Evaluated on SWE-Bench\n\n**Assessment:** As you suspected, PatchRecall is **NOT a competitor** to FTCR on type-conditioned retrieval. It operates at the file/module level, not semantic bug type level. No novelty threat.\n\n---\n\n### **SelRepair (arXiv:2507.10103) - DUAL RETRIEVAL WITH SELECTION GATE**\n\n**Title:** Accelerating Automatic Program Repair with Dual Retrieval-Augmented Fine-Tuning and Patch Generation on Large Language Models\n\n**Publication:** July 14, 2025\n\n**Key Features:**\n- Fine-tuned LLM + dual RAG module\n- Incorporates **semantic AND syntactic/structural similarity**\n- RAG selection gate determines when to add bug-fix pairs\n- Results: 26.29% exact match on Java datasets, 6.42% inference speedup\n\n**Overlap with FTCR:** SelRepair uses \"dual\" retrieval (semantic + structural), not type-conditioned hard partitioning. This is a **soft similarity hybrid approach**, not a hard partitioning strategy. Not a direct threat to FTCR's novelty if FTCR's core claim is type-driven hard partitioning.\n\n---\n\n### **RetypeR (ICSME 2024) - TYPE ERROR REPAIR, LANGUAGE-SPECIFIC**\n\n**Title:** RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors\n\n**Publication:** October 6-11, 2024 | ICSME 2024\n\n**Features:**\n- External + internal retrieval stages\n- Domain-specific to Python type errors (not general bug categories)\n- Retrieval-based framework with integrated approach\n\n**Assessment:** Language-specific (Python) and focused on type errors (a narrow category). Not a general competitor to FTCR's 18-type semantic classification. Limited threat to novelty claims.\n\n---\n\n### **LFTBench & ReduceFix (arXiv:2507.15251) - INPUT REDUCTION, NOT TYPE-AWARE**\n\n**Title:** Input Reduction Enhanced LLM-based Program Repair\n\n**Publication:** July 2025\n\n**Features:**\n- LFTBench: 200 real bugs, 1MB median failure-inducing input size\n- ReduceFix: custom task-specific input reducer\n- Addresses \"lost-in-the-middle\" problem in long prompts\n\n**Assessment:** Orthogonal to type-based retrieval. Addresses input complexity, not retrieval strategy. No novelty conflict.\n\n---\n\n### **ThinkRepair (ISSTA 2024) - CHAIN-OF-THOUGHT PROMPTING, NOT RETRIEVAL-BASED**\n\n**Title:** ThinkRepair: Self-Directed Automated Program Repair\n\n**Publication:** July 2024 | ISSTA 2024\n\n**Key Features:**\n- Chain-of-Thought (CoT) pre-fixed knowledge collection\n- Few-shot learning with example selection\n- Results: 98 bugs fixed on Defects4J v1.2 (27%-344.4% improvement)\n\n**Assessment:** Focused on prompting strategy and few-shot learning, not on **retrieval corpus partitioning strategy**. Not a direct threat to FTCR's type-partitioned retrieval methodology.\n\n---\n\n### **RepoRepair (arXiv:2603.01048) - DOCUMENTATION-ENHANCED, CROSS-FILE**\n\n**Title:** RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair\n\n**Publication:** March 2026\n\n**Features:**\n- Hierarchical code documentation generation\n- Cross-file repair via semantic abstractions\n- Repository-level context awareness\n\n**Assessment:** Orthogonal—focuses on repository-level multi-file repair, not type-conditioned retrieval indexing. Not a competitor on the hard partitioning approach.\n\n---\n\n### **CPRet Dataset (arXiv:2505.12925) - COMPETITIVE PROGRAMMING RETRIEVAL**\n\n**Title:** CPRet: A Dataset, Benchmark, and Model for Retrieval in Competitive Programming\n\n**Publication:** May 2025\n\n**Features:**\n- Problem-code alignment, solution diversity, duplication detection\n- Broader temporal coverage, language diversity\n- Multiple online judges (ICPC, OI-style problems)\n\n**Assessment:** Dataset for competitive programming, not bug repair. ReCode (your direct competitor) also targets competitive programming bug fixes. This dataset may be used in ReCode-like evaluations.\n\n---\n\n### **Recent Systematic Surveys**\n\n**[2506.23749] A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications**\n\n**Publication:** June 2025\n\n**Coverage:** 62 LLM-based APR systems (Jan 2022 – June 2025)\n\n**Key Framework:**\n- Four paradigms: fine-tuning, prompting, procedural pipelines, agentic frameworks\n- Cross-cutting layers: RAG and Analysis-Augmented Generation (AAG)\n- Notes that **different bug types benefit from different kinds of retrieved context**\n\n**Significance:** This TOSEM 2026-listed survey explicitly acknowledges that bug-type-aware retrieval is an active research area, supporting FTCR's motivation but not directly implementing hard partitioning.\n\n---\n\n## **SUMMARY OF NOVELTY THREATS**\n\n### **CRITICAL THREAT (Direct Competitor):**\n- **ReCode (CIKM 2025):** Hard partitioning by algorithm type; parallel sub-index retrieval. Nearly identical mechanism to FTCR but in competitive programming domain (Sept 2025).\n\n### **MODERATE THREATS (Type-Aware but Different Strategy):**\n- **TypeRepair (SQJ 2026):** Type-aware repair via stage-wise guidance (soft approach, not hard partitioning)\n- **ReinFix (June 2025):** Root-cause-conditioned soft retrieval (explicitly mentioned as your baseline)\n- **SelRepair (July 2025):** Dual semantic/structural retrieval with selection gate (soft hybrid)\n\n### **NO THREAT (Orthogonal or Scope-Limited):**\n- **DebugRepair, DynaFix:** Runtime/dynamic approaches, not retrieval-partitioning strategies\n- **PatchRecall:** File-level, not type-level\n- **RetypeR:** Python type errors only, narrow domain\n- **ThinkRepair:** Prompting strategy, not retrieval corpus design\n- **RepoRepair:** Cross-file documentation, not type partitioning\n\n---\n\n## **CRITICAL TIMING ISSUE**\n\n**ReCode was published September 2, 2025 to arXiv and accepted to CIKM 2025.** If FTCR was submitted around the same time or later, ReCode **predates or is concurrent with FTCR**, directly undermining the novelty claim of \"type-conditioned hard partitioning for program repair retrieval.\"\n\n**Key question for your adversarial review:** When was FTCR submitted to arXiv or to a conference? If after September 2, 2025, ReCode is prior art.\n\n---\n\n## **RECOMMENDATION FOR YOUR REVIEW**\n\n1. **Directly compare FTCR vs. ReCode** on identical benchmarks (Defects4J v2.0, others). If ReCode achieves better results with a nearly identical mechanism, FTCR's contribution is incremental.\n\n2. **Verify claim specificity:** Is FTCR claiming the hard partitioning approach is novel, or the specific set of 18 bug types? If the latter, the novelty bar is lower but still vulnerable to the 10-type TypeRepair or ReCode's algorithm-based partitioning.\n\n3. **Check benchmark overlap:** Do all these papers use Defects4J v2.0? If yes, compare absolute numbers:\n   - DynaFix: 236 (GPT-4)\n   - DebugRepair: 295 (DeepSeek-V3)\n   - TypeRepair: ~272 improvements reported, exact numbers unclear\n   - FTCR: ?\n\n4. **Evaluate ReCode's claims vs. FTCR's claims** on whether hard partitioning is truly more effective than soft similarity (InferFix, ReinFix).\n\n---\n\n## **Sources:**\n\n- [ReCode: CIKM 2025](https://arxiv.org/abs/2509.02330)\n- [TypeRepair: SQJ 2026](https://link.springer.com/article/10.1007/s11219-026-09751-w)\n- [DebugRepair: arXiv 2604.19305](https://arxiv.org/abs/2604.19305)\n- [DynaFix: arXiv 2512.24635](https://arxiv.org/abs/2512.24635)\n- [InferFix: ESEC/FSE 2023](https://arxiv.org/abs/2303.07263)\n- [ReinFix: arXiv 2506.23100](https://arxiv.org/abs/2506.23100)\n- [PatchRecall: arXiv 2604.10481](https://arxiv.org/abs/2604.10481)\n- [SelRepair: arXiv 2507.10103](https://arxiv.org/abs/2507.10103)\n- [RetypeR: ICSME 2024](https://conf.researchr.org/details/icsme-2024/icsme-2024-papers/20/RetypeR-Integrated-Retrieval-based-Automatic-Program-Repair-for-Python-Type-Errors)\n- [LFTBench/ReduceFix: arXiv 2507.15251](https://arxiv.org/abs/2507.15251)\n- [ThinkRepair: ISSTA 2024](https://arxiv.org/abs/2407.20898)\n- [RepoRepair: arXiv 2603.01048](https://arxiv.org/abs/2603.01048)\n- [CPRet: arXiv 2505.12925](https://arxiv.org/abs/2505.12925)\n- [APR Survey: arXiv 2506.23749](https://arxiv.org/abs/2506.23749)"
      }
    ],
    "totalDurationMs": 116377,
    "totalTokens": 47726,
    "totalToolUseCount": 27,
    "usage": {
      "input_tokens": 917,
      "cache_creation_input_tokens": 3684,
      "cache_read_input_tokens": 39069,
      "output_tokens": 4056,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3684
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 917,
          "output_tokens": 4056,
          "cache_read_input_tokens": 39069,
          "cache_creation_input_tokens": 3684,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3684,
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
      "otherToolCount": 27
    }
  },
  "sourceToolAssistantUUID": "75687e16-c5d3-4234-b332-bcd756085db4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T06:47:56.932Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now carefully synthesize all the research findings and previous review rounds to produce a comprehensive adversarial review for Round 6.

Key findings from the research:

**What's been verified:**
1. EMNLP 2026 ARR deadline of May 25, 2026 - CONFIRMED
2. InferFix (arXiv:2303.07263) - EXISTS; uses contrastive learning for semantic similarity, not direct type partitioning. Type annotations are added as prompt annotations, not hard partitioning keys. The proposal's characterization seems mostly accurate.


3. ReinFix confirmed as ICSE 2026, and SWE-Exp verified at 73.0% on SWE-bench Verified, which aligns with what the proposal states. TypeRepair exists in SQJ 2026 but I can't fully verify its scope due to access restrictions, and I'm still checking on DebugBench.

4. DebugBench has 4 major and 18 minor bug categories, though the proposal simplifies this to an 18-category framework. M-RAG improvements check out, CRAG was indeed submitted to ICLR 2025 then withdrawn, and SWE-bench Lite's 62.7% SOTA with Claude Opus 4.6 is confirmed. GitBug-Java with 199 bugs, ReCode as a cited ancestor from CIKM 2025, and the other tools like DynaFix, DebugRepair, and PatchRecall all verify against what's cited.

5. I'm finding a potential issue with how InferFix is characterized—the research shows it uses contrastive learning for semantic similarity between bugs and fixes, which might not match the proposal's framing.

6. The EMNLP 2026 deadline of May 25 is confirmed, and with Day 0 starting today (May 10), there's only a 10-14 day window to produce publication-quality results, which is an extremely tight constraint for the auto-research mode.

7. SelRepair from July 2025 wasn't cited in the proposal, but it's not a direct competitor since it uses soft hybrid retrieval rather than type-conditioned hard partitioning like FTCR does.

Now evaluating the Round 6 proposal against the review criteria: the EMNLP 2026 ARR target with May 25 deadline has been reinstated with an explicit day-by-day execution schedule, and auto-research is confirmed as the only constraint-compliant mode for the 10-14 day timeframe.

InferFix has been added with clear differentiation across three dimensions: soft contrastive embedding versus hard construction-time partitioning, Infer-specific diagnostic IDs versus the 18-category taxonomy, and InferredBugs versus natural bug-fix pairs. The corpus confound is now explicitly addressed through intra-corpus ablations for clean architectural testing and joint-effect comparisons for cross-corpus analysis. TypeRepair's evidentiary basis is stated with an evaluation design argument centered on within-project datasets, and the resource estimate has been restructured to focus on auto-research only.

However, there's a significant feasibility concern with the technical timeline. The day-by-day schedule begins May 10, but the execution plan requires setup and corpus annotation launch on Day 0 itself, which creates immediate pressure on the initial phase. The venue targeting seems optimistic—EMNLP Main is a stretch given that reviewers have flagged this as more of a Findings-level contribution, so I should probably prioritize EMNLP Findings as the realistic target. For InferFix, I need to verify the exact retrieval mechanism since my characterization of soft contrastive type conditioning might not perfectly match how the paper actually implements it. DebugBench's category structure is a minor concern, but I should check the specifics there too.

On the corpus size question, the 3,050-pair natural dataset versus ReinFix's 100K is a real limitation that I'm handling through ablations, though reviewers will likely push back on whether that's statistically sufficient across all 18 types. And I haven't fully verified SWE-Exp's type mechanism yet—that claim needs checking against the actual paper.

Looking at the bigger picture, I've resolved the critical issues across multiple rounds: InferFix is now properly cited, the venue plan is concrete, the corpus confound is acknowledged, and I've added the random-partition baseline. The main remaining concerns are that EMNLP main track might be optimistic (Findings is more realistic) and the 15-day timeline is tight starting from today.

Now I'm scoring each dimension to determine if this passes round 6. For novelty, the hard versus soft partitioning comparison is genuinely novel in the multi-language APR space—InferFix and ReinFix are the right soft baselines, and while ReCode does hard partitioning in competitive programming, FTCR's extension to real-world code is meaningful. TypeRepair provides within-project type guidance but operates in a different scope.

On feasibility, the timeline is extremely tight starting today with only 15 days to the deadline. The auto-research setup with 2 A100 nodes is viable if compute is immediately available, and the $1,500-1,820 budget with 190 H100-hours stays within the ≤200 constraint, though SWE-bench Lite completion is deferred to MVS and the 2-day paper writing window is aggressive.

For clarity, the proposal is well-structured with explicit falsifiable hypotheses and a concrete day-by-day schedule, though there's a minor inconsistency in how DebugBench's category structure is described.

On impact, the finding about when hard type conditioning helps versus hurts could be genuinely useful, and the generalization claim about LLM-inferred labels for retrieval routing is interesting, but the practical gains are limited.

Averaging across all dimensions gives me 3.625, which falls short of the 4.0 threshold. The core tension is whether this lands at EMNLP Findings or Main Track—previous feedback has leaned toward Findings, though there's some inconsistency in the reviewer comments on this point.

I'm also noticing a structural issue with DebugBench that wasn't flagged before: the 18 subtypes are actually nested within 4 major categories, not independent, which affects how the experimental design should handle rare type merging. With six rounds of revision already completed and most major issues from Round 5 addressed, I need to decide whether another revision cycle is worth it or if this should move forward as-is.

The score of 3.6 is below my 4.0 threshold, and there are still meaningful gaps—the EMNLP track framing isn't crisp enough, the 15-day timeline starting immediately is genuinely tight, and that DebugBench hierarchy is a factual inaccuracy I should correct. I'm leaning toward REVISE to tighten these remaining issues, particularly clarifying that EMNLP Findings is the right target and making sure the experimental design properly accounts for the hierarchical structure of DebugBench. Correct "18-category" to "4-major/18-minor" structure throughout. Day 0 is TODAY (May 10), so the proposal needs to be realistic about whether 3-pass annotation of 3,050 pairs can actually complete in 3 days with auto-research mode, especially since corpus annotation hasn't started yet. The statistical power concern remains: after Java-only filtering, we're looking at roughly 31 pairs per type, which may be too thin for reliable Z% and W% comparisons—the proposal mentions merge policies but doesn't specify what statistical tests will determine significance.

My verdict is REVISE (Round 6/10). The proposal has genuinely addressed all five Round 5 issues, but two critical problems remain. First, the target_venues field lists both EMNLP Main and Findings, but multiple reviewers across Rounds 3 and 4 flagged that an empirical calibration study belongs in Findings, not Main—I need to push for a clear commitment to EMNLP Findings. Second, the timeline is still problematic: launching 3-pass annotation today with a 3-day completion window is aggressive and needs either a reality check or stronger justification for why auto-research mode makes this feasible. I need to verify whether InferFix actually uses type as an embedding signal or just as annotation context in its prompts, since that distinction affects how accurately I'm characterizing the "soft type conditioning" approach. Looking at the overall assessment, the proposal scores around 3.5/5 on novelty and feasibility—the hard/soft partitioning idea is genuinely novel but builds incrementally on existing work, and while technically doable, the 15-day timeline with 190 H100-hours leaves almost no margin for error.

The average of 3.625/5 falls below the 4.0 threshold, so this needs revision.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6d5b82a-9f62-4e99-b38a-c01b5f7f699b",
  "isSidechain": false,
  "requestId": "req_011CatSPa9XwuRsL8krmwJiT",
  "type": "assistant",
  "uuid": "ce80eaa8-e41e-4983-bce2-855818d59260",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Te1QVVfpEyJGp5fNueBgAU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9289,
      "cache_read_input_tokens": 38135,
      "output_tokens": 6190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6190,
          "cache_read_input_tokens": 38135,
          "cache_creation_input_tokens": 9289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9289
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

_source line 17 · 2026-05-10T06:48:39.363Z_

Based on my independent research, here is my adversarial verdict for Round 6:

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3.5,
      "rationale": "Hard vs. soft type partitioning for real-world multi-language APR is a genuine gap: InferFix (soft contrastive, verified), ReinFix (soft root-cause, verified), and TypeRepair (within-project guidance, partially verified) all leave hard construction-time partitioning untested for natural bug-fix corpora. However, the contribution is incremental — ReCode (CIKM 2025) already implements algorithm-type hard partitioning in competitive programming and is acknowledged as prior art; FTCR's extension to 18 natural bug categories is meaningful but not a conceptual leap."
    },
    "feasibility": {
      "score": 3.5,
      "rationale": "190 H100-hours is within the ≤200 budget (independently verified SWE-bench Lite SOTA at 62.7% and GitBug-Java at 199 bugs confirm the evaluation landscape is real), but the 15-day window starting Day 0 TODAY is genuinely precarious: 3-pass annotation of 3,050 pairs must pipeline immediately, and the 2-day writing window requires a pre-drafted skeleton built concurrently with Day 4–6 experiments — any infrastructure delay collapses the schedule."
    },
    "clarity": {
      "score": 4.0,
      "rationale": "The day-by-day execution schedule, four falsifiable quantities (X%/Y%/Z%/W%), explicit corpus confound acknowledgment, and three-point InferFix differentiation all represent genuine clarity improvements; the DebugBench structure is consistently mischaracterized as '18-category' when it is actually 4-major/18-minor hierarchical, which will confuse reviewers familiar with the benchmark."
    },
    "impact": {
      "score": 3.5,
      "rationale": "The causal decomposition of when LLM-inferred categorical labels enable hard retrieval partitioning (and when misclassification causes degradation) generalizes beyond code repair — this is the most impactful framing. But FTCR's 20–35% standalone resolve rate against SWE-Exp's 73.0% on SWE-bench Verified (independently confirmed) will require a cleaner 'retrieval is an independent axis' argument to land with reviewers."
    }
  },
  "issues": [
    "HIGH — EMNLP Main vs. Findings target ambiguity persists: target_venues now lists 'EMNLP 2026 Main' AND 'EMNLP 2026 Findings' as separate entries, but the empirical calibration study (X%/Y%/Z%/W% LLM label reliability) is a measurement finding about LLM annotation quality — appropriate for EMNLP Findings, not the Main track, which expects findings that advance understanding of language models at a deeper level. Rounds 3 and 4 both explicitly downgraded the EMNLP target to Findings; Round 5 asked to restore EMNLP without specifying Main vs. Findings; Round 6 silently re-expanded to Main. The proposal must commit to EMNLP Findings as the EMNLP target and stop oscillating. Trying for Main and being desk-rejected wastes the submission cycle.",
    "MEDIUM — DebugBench hierarchical structure mischaracterized throughout: independently verified (ACL Findings 2024 paper) that DebugBench has 4 MAJOR categories (Syntax Bugs, Logic Bugs, Reference Bugs, Multiple Bugs) with 18 MINOR sub-types nested within them — not 18 independent categories. The proposal consistently refers to '18-category taxonomy' and '18-category natural-bug taxonomy aligned with DebugBench's taxonomy.' This is inaccurate and will flag with any reviewer who has read DebugBench. Concretely: the merge policy for rare types must operate within the 4-major/18-minor hierarchy (merge within major categories first, not across them); X%/Y%/Z%/W% measurements must specify whether they are measured at the major-type or minor-type level; and the '~31 Java instances per type' figure implies 18 equal partitions, which is not how the benchmark is structured.",
    "MEDIUM — Day-0-today execution assumption is unverified: the schedule commits to launching corpus annotation pipeline on May 10 (today) with 2 A100 nodes already available. No verification of compute availability, API rate limits on day 1, or Defects4J V1.2 Docker environment readiness is mentioned. If infrastructure setup takes 1–2 days (common in practice), the already-tight 2-day paper writing window (Days 13–15, May 23–25) disappears entirely. The proposal should either (a) confirm that compute is already provisioned and Docker environments tested, or (b) revise the schedule to account for a 1-day setup buffer by shifting MVS deliverables earlier.",
    "LOW — InferFix type-as-embedding-signal claim needs precision: independent verification found that InferFix adds bug type annotations as prompt context alongside retrieved fixes, while the contrastive retriever learns semantic similarity between bugs/fixes. The proposal claims 'type influences embedding proximity rather than pool membership' — this framing appears broadly correct but needs verification against the actual retriever architecture section (Section 3 of arXiv:2303.07263), not just the abstract. If InferFix's retriever does NOT explicitly condition on type labels during encoding (only using type for post-retrieval prompt augmentation), the 'soft type conditioning' differentiation needs rewording to 'type-correlated semantic similarity' to avoid misrepresenting the baseline.",
    "LOW — Statistical significance for Z% and W% unstated: the Z% (repair improvement for correctly classified) and W% (repair degradation for misclassified) measurements will have unequal sample sizes depending on classifier accuracy. With ~31 Java instances per minor type and a 20% held-out split (~6 per type), per-type statistical tests are underpowered. The proposal should specify: (a) whether Z% and W% are aggregated across all types or reported per type; (b) what statistical test is used; (c) minimum sample threshold for a type to contribute to the Z%/W% comparison."
  ],
  "feedback": "Round 6 has addressed all five Round 5 issues: EMNLP venue restored with committed schedule, InferFix added with three-point differentiation, corpus confound made explicit, TypeRepair evidentiary basis stated, resource estimate stripped to auto-research only. The core hypothesis is well-posed and the experimental design is increasingly rigorous. Three targeted fixes would make this submission-ready: (1) COMMIT TO EMNLP FINDINGS — remove 'EMNLP 2026 Main' from target_venues and replace with 'EMNLP 2026 Findings (via ARR)'. The X%/Y%/Z%/W% calibration study is a strong Findings paper; attempting Main track risks desk rejection on NLP-contribution grounds and wastes the submission cycle. (2) FIX DEBUGBENCH STRUCTURE — replace every instance of '18-category' with '4-major/18-minor hierarchical taxonomy' and state that X%/Y%/Z%/W% measurements operate at the minor-type level (18 sub-categories), with major-type aggregation reported as a secondary result. Revise the merge policy to explicitly merge within the same major category first (e.g., merge rare Reference Bug sub-types before merging across Logic and Reference). (3) CONFIRM COMPUTE READINESS — add one sentence to the Day 0 entry: 'Compute: 2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.' If this cannot be stated truthfully, shift the MVS timeline by 1 day and compress paper writing to 1 day with a more aggressive pre-drafted skeleton policy. These three changes are low-effort and directly address verifiable gaps; the underlying science is solid and the proposal is close to submission-ready for EMNLP 2026 Findings.",
  "reason": "Round 6 resolved all five Round 5 issues but introduces a new venue ambiguity (Main vs. Findings re-opened), mischaracterizes DebugBench's 4-major/18-minor structure throughout, and the Day-0-today execution plan has unverified compute readiness; avg score 3.625/5 is below the 4.0 pass threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce80eaa8-e41e-4983-bce2-855818d59260",
  "isSidechain": false,
  "requestId": "req_011CatSPa9XwuRsL8krmwJiT",
  "type": "assistant",
  "uuid": "d5a04db9-c08f-4f60-b68e-2b53e0aee0d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Te1QVVfpEyJGp5fNueBgAU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9289,
      "cache_read_input_tokens": 38135,
      "output_tokens": 6190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9289,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6190,
          "cache_read_input_tokens": 38135,
          "cache_creation_input_tokens": 9289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9289
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
  "leafUuid": "d5a04db9-c08f-4f60-b68e-2b53e0aee0d7",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Failure-Type-Conditioned Retrieval for Multi-Language Repository Repair",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d5a04db9-c08f-4f60-b68e-2b53e0aee0d7",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Failure-Type-Conditioned Retrieval for Multi-Language Repository Repair",
  "sessionId": "49a4fdd9-9f29-4597-b21f-1decd19e6826"
}
```

---
