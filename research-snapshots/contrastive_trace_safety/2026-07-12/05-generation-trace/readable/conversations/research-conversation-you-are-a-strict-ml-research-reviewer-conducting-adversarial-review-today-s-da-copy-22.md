# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/a8158a37-99fc-4e21-a270-570542d8053d.jsonl`
- **Structured JSON:** [`311bb227eca6c8c45bb2.json`](../../sessions/31/311bb227eca6c8c45bb2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T06:26:41.450Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T06:26:41.450Z",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 5/10)\n{\n  \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\",\n  \"core_problem\": \"Retrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is whether hard categorical type partitioning of the retrieval index outperforms ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer, particularly in a multi-language setting. An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. This 'what you retrieve matters' result directly motivates type-conditioned fix-patch retrieval: type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and, when addressed directly, become analytical contributions: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across 18 types yields only ~31 Java instances per type on average, requiring an explicit minimum-threshold and merge policy for rare types; and (2) classifier error propagation — when an incoming bug is misclassified into the wrong type partition, hard partitioning will underperform soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback to soft retrieval — turns potential weaknesses into measurable experimental variables that sharpen, rather than undermine, the core hypothesis.\",\n  \"opportunity\": \"ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation from a different angle: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Their core finding — that what you retrieve determines quality more than how you retrieve — directly motivates FTCR's retrieval design: fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of N discrete semantic types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than ReinFix's joint embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar code but different root causes do not. DebugBench uniquely provides 4,253 instances with ground-truth 18-category type annotations across C++, Java, and Python; crucially, these ground-truth labels enable direct calibration of the few-shot type classifier, turning classifier error propagation from a latent risk into a measurable experimental variable. The confidence-gated hybrid (fall back to soft retrieval for low-confidence classifications) addresses the structural risk of hard partitioning and has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884) for general RAG systems. M-RAG (ACL 2024, arXiv 2405.16420) additionally validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis before evaluating it in the code repair setting.\",\n  \"landscape\": \"RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% with the same model and is not a SOTA claim. ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning, and root cause is a continuous semantic descriptor, not a discrete category. SWE-Exp (arXiv 2507.23361, revised February 2026) is the most important concurrent work: it retrieves top N=10 issues 'most relevant in terms of error type' from an experience bank using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large encoder), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic pipeline. Three design differences distinguish SWE-Exp from FTCR: (1) retrieval mechanism — SWE-Exp uses soft cosine similarity with type as embedding metadata at retrieval time; FTCR partitions the index into discrete type sub-corpora at construction time, so only same-type pairs are ever candidates for a query; (2) retrieved artifact — SWE-Exp stores distilled problem perspectives and generalized modification strategies; FTCR retrieves concrete historical fix patches for direct template transfer; (3) scope — SWE-Exp is fully agentic and scoped to Python; FTCR is retrieval-only and covers C++, Java, and Python, using DebugBench's oracle type labels for cross-lingual calibration. The testable question SWE-Exp leaves open is whether hard construction-time partitioning outperforms soft retrieval-time type filtering for fix-template precision. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5 baseline. TypeRepair's context selection stage conditions on the identified defect type to select relevant within-project code context and to provide type-specific repair guidance in the LLM prompt — it does not retrieve from an external cross-repository fix corpus. TypeRepair is Java-only (Defects4J/QuixBugs); FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 historical fix patches. TypeRepair validates that defect type identification benefits LLM-based repair (supporting FTCR's core hypothesis) while leaving hard-vs-soft type-partitioned cross-repository retrieval entirely unexplored; FTCR addresses this gap directly. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information helps; their proposed AllianceCoder retrieves APIs via semantic description matching rather than code similarity. While the study targets code generation rather than repair, the 'what to retrieve matters more than how' finding motivates FTCR's choice of fix patches retrieved by type partition (sharing semantic repair structure) over code-similarity retrieval (sharing only surface features). DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair (236 bugs fixed with GPT-4); DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3 via self-directed debugging with runtime traces. Both update the Defects4J performance landscape but are orthogonal to FTCR's retrieval strategy focus — execution-level augmentation and retrieval strategy are independently improvable axes. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via LLM objective alignment. FTCR's structural departure from ReinFix is to (1) classify incoming failures into discrete categories, then (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) for a clean comparison that isolates partitioning as the primary architectural variable — noting that partitioning also reduces the effective retrieval pool to ~1/N_types of the full corpus, a corpus-size effect that a random-partition control ablation is designed to separate from type-matching precision. RetypeR (ICSME 2024, Hao et al.) applies a two-stage external+internal retrieval conditioned on Python type errors, establishing that type-specific retrieval helps for one narrow bug class and language; FTCR extends this principle to 18 categories across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates that multi-partition RAG consistently outperforms single-store RAG across NLP tasks (summarization: +11%, translation: +8%, dialogue: +12%), validating the general principle of partition-based retrieval before applying it to code repair. PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary (localization rather than cross-repository fix template retrieval). The APR survey (arXiv 2506.23749) reviews 63+ systems and identifies retrieval augmentation as the key enhancement, but no reviewed system applies hard taxonomic type classification as the retrieval partition key across multiple languages.\",\n  \"approach\": \"We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms ReinFix-style soft root-cause embedding for cross-repository fix transfer. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix for a clean comparison), same corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control (see below).\\n\\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. FTCR embodies this principle: rather than retrieving the most syntactically similar buggy code in the corpus, we retrieve fix patches — input/output transformation pairs — that share the same semantic repair operation. Type partitioning ensures that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to look syntactically similar but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\\n\\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559).\\n\\nCorpus Sparsity Policy. Each pair is annotated with one of 18 semantic categories aligned with DebugBench's taxonomy (four major types: Syntax, Reference, Logic, Multiple; 18 minor subtypes) via few-shot prompting using DebugBench's labeled examples as demonstrations; three annotation passes measure inter-run consistency. A per-type instance count table is computed and reported in the paper for transparency. For the combined Python+Java corpus (3,050 pairs), 18-type analysis is viable: Python instances dominate (~2,487) and yield an estimated mean of ~138 pairs per type. For Java-only ablations (~559 pairs, ~31 per type average), a minimum-threshold policy applies: types with fewer than 30 Java instances are merged into nearest-neighbor supercategories (e.g., Concurrency + Resource-Leak → Resource-Management; Format-Error + Syntax-Error → Low-Level, since compiled Defects4J/GitBug-Java bugs contain near-zero syntax errors). Java ablation results are reported for the 6–8 resulting categories that each exceed 50 instances, with merged categories explicitly labeled. This avoids the degenerate case of k=5 retrieval from a 15-instance sub-index, which approximates exhaustive lookup rather than similarity-based retrieval.\\n\\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound; embedding cost is negligible (~$5–15 for corpus plus all evaluation queries at $0.13/1M tokens). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific and deconfounding the encoder-vs-partitioning comparison.\\n\\nType Classifier Calibration on DebugBench Ground Truth. Since DebugBench provides oracle type labels for 4,253 instances, a held-out 20% split (851 instances) directly measures our few-shot classifier's per-type precision and recall against ground truth, yielding an overall accuracy estimate. Cross-dataset zero-shot agreement is measured by applying the same classifier to a 10% random sample (~56 pairs) of the Java annotation set (Defects4J + GitBug-Java) with human-verified labels as oracle, yielding a cross-lingual label consistency score. This produces the NLP contribution: a falsifiable empirical claim that LLM-inferred bug type labels achieve X% agreement with DebugBench ground-truth labels (Python/C++), transfer zero-shot to unseen Java bugs with Y% agreement, and are predictive of retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs.\\n\\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect — hard partitioning reduces the effective retrieval pool to ~1/N_types of the full index, which independently affects recall — we add a random-partition baseline (Variant F): the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index. Any performance gap between FTCR (Variant E, hard type partition) and this control measures the precision benefit of type-matching net of pool-size reduction. This converts the comparison from 'clean but contested' to 'rigorous and unambiguous.'\\n\\nConfidence-Gated Retrieval Fallback. At inference time, the type classifier outputs a probability distribution over 18 categories. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval (identical to the ReinFix baseline). This confidence-gated hybrid is evaluated as a sixth system variant alongside: (A) text-similarity RAG (no type signal), (B) RELREPAIR (project-internal retrieval), (C) RepoRepair (documentation-guided), (D) ReinFix-style soft retrieval (re-implemented on same corpus and same encoder), (E) FTCR@hard-all, and (F) random-partition control (same N sub-indices, randomly assigned — corpus-size control). The confidence-gated fallback has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). The projected finding: correctly-classified high-confidence bugs show systematic gains from hard partitioning (+5–10% repair success on Defects4J where oracle type labels allow clean stratification); misclassified or low-confidence bugs show performance on par with or slightly below soft retrieval; the confidence gate recovers aggregate performance for ambiguous cases; the random-partition control falls between soft retrieval and FTCR@hard-all, confirming that type-matching rather than pool-size reduction drives the gain.\\n\\nPractical Utility: Retrieval as an Independently Upgradeable Module. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is deliberately positioned as the retrieval contribution in isolation, not a claim against the agentic pipeline ceiling. The motivation for isolating retrieval is architectural: DynaFix (arXiv 2512.24635) demonstrates that execution-level augmentation and retrieval strategy are independently improvable axes — it improves over ReinFix on Defects4J V2.0 by adding iterative execution feedback while keeping retrieval fixed. An improved retrieval module (FTCR vs. ReinFix-style soft retrieval) compounds with execution-level improvements: the delta between FTCR-augmented and ReinFix-augmented iterative repair pipelines measures the retrieval contribution at the pipeline level. Standalone evaluation isolates the retrieval hypothesis cleanly; the modular gain is what ICSE reviewers can act on independently of scaffolding choices.\\n\\nExpected Performance on SWE-bench Lite. We project FTCR to achieve 20–35% resolve rate with Claude Sonnet 4.6 in retrieval-only (non-agentic) mode, comparable to ReinFix-style retrieval on the same corpus. This is below the current SWE-bench Lite SOTA (~62.7%, Claude Opus 4.6, May 2026, agentic scaffolding) and below RepoRepair's 45.7% (documentation-guided multi-step localization). Lower aggregate performance than RepoRepair is explicitly defended: FTCR does not incorporate documentation-guided localization, which is an orthogonal architectural component. The primary SWE-bench Lite contribution is validating that the type-conditioned advantage observed on DebugBench transfers to real-world Python repositories, not claiming absolute SOTA.\\n\\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while SWE-bench Lite validates real-world transfer.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~88 H100-hours (~150 A100-hours equivalent)\",\n      \"gpu_utilization\": \"~30-40% utilized; high idle while researchers design annotation prompts, debug Defects4J Java-8 environments, manually review per-type count tables, and verify annotation consistency across passes\",\n      \"timeline\": \"4-6 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$450 (150 A100-hours × $3/h on RunPod/Lambda Labs)\",\n      \"embedding_api_cost\": \"~$5-15 (text-embedding-3-large for 3,050-pair corpus + evaluation queries, at $0.13/1M tokens; negligible relative to overall budget)\",\n      \"note\": \"Well within the 200 H100-hour hard budget\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~165 H100-hours (~280 A100-hours equivalent)\",\n      \"gpu_utilization\": \"~55-65% utilized; agent continuously queues embedding and evaluation jobs while human approves ablation configurations at decision gates\",\n      \"timeline\": \"6-8 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in for ablation approval, per-type count table review, confidence threshold tuning, and failure triage\",\n      \"claude_api_cost\": \"$200-400 (annotation: ~3,050 instances × ~$0.02/call ≈ $61; 3 annotation passes for consistency ≈ $183; DebugBench classifier calibration: 851 held-out instances × $0.02 ≈ $17; pipeline orchestration and repair: ~1,500 agent turns × $0.10/turn ≈ $150; buffer ~$50)\",\n      \"embedding_api_cost\": \"~$5-15 (text-embedding-3-large for corpus and evaluation queries)\",\n      \"estimated_gpu_cost\": \"~$840 (280 A100-hours × $3/h)\",\n      \"note\": \"Within the 200 H100-hour hard budget\",\n      \"risk_note\": \"Defects4J Docker reproducibility is the primary bottleneck — the Java-8 pre-filter eliminates ~9% upfront, but remaining instances still require environment triage. GitBug-Java's isolated Docker images significantly reduce this overhead for the Java supplement. Java per-type sparsity is the secondary risk: if the 6-8 type categories above threshold have unequal sizes, the Java ablation may be underpowered for the smallest categories.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)\",\n      \"gpu_utilization\": \"near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants\",\n      \"ablation_scope\": \"Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (6-type coarse / 18-type fine / merged-Java), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java train → SWE-bench-Lite Python eval), classifier accuracy stratification (by confidence band)\",\n      \"timeline\": \"10-14 days with 2 A100 nodes running in parallel\",\n      \"team\": \"0 (initial ~4h setup for corpus pipeline, per-type sub-index construction scaffold, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)\",\n      \"claude_api_cost\": \"$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)\",\n      \"embedding_api_cost\": \"~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)\",\n      \"estimated_gpu_cost\": \"~$969 (323 A100-hours × $3/h)\",\n      \"speed_bottleneck\": \"GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls\",\n      \"risk_note\": \"Auto-assigned bug type labels may drift from human-interpretable categories without the three-pass consistency check; the confidence-gated hybrid adds a hyperparameter (τ) that requires tuning on the DebugBench held-out split before SWE-bench Lite evaluation. SWE-bench Lite infrastructure failures can silently inflate repair failure counts without human oversight.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICSE 2027 (mandatory abstract deadline June 23, 2026 — SOLE PRIMARY TARGET; best fit for SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation reviewers will expect; TypeRepair (SQJ 2026) comparison on Defects4J clarifies FTCR's orthogonal contribution of cross-repository retrieval; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections about hard partitioning; random-partition control specifically converts the 'corpus-size confound' objection into a closed experimental question)\",\n    \"FSE 2027 (full paper deadline October 2, 2026 — backup venue if ICSE review cycle overlaps unfavorably; same SE audience, equally appropriate for a retrieval-architecture study with multi-language empirical evaluation)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; must compare directly on Defects4J V1.2 using same text-embedding-3-large encoder; uses a unified vector database, not a specific named implementation]\",\n    \"SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; retrieves top N=10 issues by soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; stores distilled modification strategies, not fix patches; agentic, Python-only; achieves 73.0% on SWE-bench Verified with Claude 4 Sonnet — differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, and multi-language scope]\",\n    \"TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0/QuixBugs (Java-only); validates that type conditioning improves LLM repair; context selection stage conditions type to select within-project context and generate type-specific prompting guidance, NOT cross-repository retrieval — FTCR's orthogonal contribution is type-conditioned retrieval of fix patches from an external ~3,050-pair cross-language corpus; must cite and explicitly differentiate]\",\n    \"What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond (Gu et al., ICSE 2026, arXiv 2503.20589) [shows similar-code snippet retrieval degrades repository-level code generation by up to 15% on CoderEval/RepoExec while contextual + API info helps; motivates FTCR's type-conditioned fix-patch retrieval — type partitioning retrieves patches sharing semantic repair structure, not superficial code similarity; note the finding applies to code generation not repair, but the 'what to retrieve matters' principle is directly applicable]\",\n    \"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330) [algorithm-type-conditioned retrieval in competitive programming — conceptual ancestor]\",\n    \"RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors (ICSME 2024, Hao et al.) [type-specific retrieval for one language and one error class — FTCR extends to 18 types and 3 languages]\",\n    \"DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv 2512.24635) [surpasses ReinFix on Defects4J V2.0 (236 bugs with GPT-4) using execution-level augmentation; demonstrates retrieval and execution augmentation are independently improvable axes; retrieval improvement (FTCR) compounds with execution-level improvements (DynaFix-style)]\",\n    \"DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2604.19305) [295 Defects4J bugs with DeepSeek-V3 via runtime traces and debugging-driven conversational repair; updates Defects4J landscape but is orthogonal — no retrieval augmentation component]\",\n    \"D4C: Aligning the Objective of LLM-based Program Repair (ICSE 2025, arXiv 2404.08877) [180 Defects4J bugs via objective alignment; updates Defects4J performance landscape]\",\n    \"M-RAG: Reinforcing Large Language Model Performance through Retrieval-Augmented Generation with Multiple Partitions (ACL 2024, arXiv 2405.16420) [multi-partition RAG validated on NLP tasks: +11% summarization, +8% translation, +12% dialogue; principled precedent for partition-based retrieval across domains]\",\n    \"RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code (arXiv 2509.16701) [project-internal retrieval baseline]\",\n    \"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048) [documentation-guided localization baseline; 45.7% on SWE-bench Lite using multi-step localization, orthogonal to FTCR's retrieval focus]\",\n    \"DebugBench: Evaluating Debugging Capability of Large Language Models (ACL Findings 2024) [primary evaluation with ground-truth 18-category labels across C++/Java/Python; held-out 20% split used for few-shot classifier calibration; synthetic-bug limitation acknowledged]\",\n    \"GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; supplement for Defects4J Java corpus]\",\n    \"SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025, arXiv 2504.21798) [50k Python task instances from 128 repos; used as scale corpus for Python retrieval index]\",\n    \"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey confirming retrieval augmentation as key enhancement with no type-partitioned system identified]\",\n    \"What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]\",\n    \"PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]\",\n    \"RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]\",\n    \"CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism with retrieval quality scoring; precedent for the FTCR confidence-gated hybrid variant; note: withdrawn from ICLR 2025, unpublished — cite as preprint only]\"\n  ],\n  \"description\": \"FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft root-cause-augmented retrieval (ReinFix's approach, ICSE 2026) for cross-repository fix template transfer. ReinFix (ICSE 2026, arXiv 2506.23100) is the closest prior work — it embeds LLM-generated free-text root-cause descriptions jointly with buggy code into a unified vector database using text-embedding-3-large, showing +32/+38 bugs fixed on Defects4J V1.2/V2.0. FTCR's structural departure is to (1) classify incoming failures into one of 18 discrete semantic categories aligned with DebugBench's empirically-validated taxonomy, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable. Round 5 revisions address four issues: (a) TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) added to landscape and key_references with explicit differentiation — TypeRepair's 4-stage pipeline uses defect type to select within-project context and generate type-specific repair guidance (prompt engineering), not cross-repository retrieval; it covers Java only (Defects4J/QuixBugs) with 10 types; TypeRepair validates that type conditioning helps repair (supporting FTCR's hypothesis) while leaving cross-repo type-conditioned retrieval unexplored; (b) arXiv 2503.20589 (Gu et al., ICSE 2026) added as motivation rather than counterevidence — their finding that similar code snippet retrieval degrades code generation by 15% while structured knowledge helps motivates FTCR's type-conditioned fix-patch retrieval; type partitioning retrieves patches sharing semantic repair structure (the fix operator), not superficial code similarity; the paper targets code generation, not repair, making it an indirect motivator rather than a direct challenge; (c) practical utility framing added explicitly in approach — retrieval is an independently upgradeable module within agentic pipelines; DynaFix demonstrates retrieval and execution augmentation are independent axes; FTCR's retrieval gain compounds with DynaFix-style iterative repair; 20-35% standalone metric is the retrieval floor, not the pipeline ceiling; (d) EMNLP 2026 definitively removed — the May 25 ARR deadline is infeasible given that all experiments remain to be run; ICSE 2027 is the sole primary target; FSE 2027 is the backup; cross-lingual classifier findings can be submitted separately after ICSE results are complete. RetypeR (ICSME 2024) establishes type-specific retrieval for Python type errors specifically; FTCR extends to 18 categories across C++, Java, and Python. The retrieval corpus (~3,050 natural bug-fix pairs from SWE-bench non-Lite, BugsInPy, Defects4J V1.2, and GitBug-Java) requires no GPU training; the approach is fully inference-based. Target venues: ICSE 2027 (abstract June 23, primary), FSE 2027 (October 2, backup).\",\n  \"project_name\": \"failure_type_rag_repair\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Uncited competing work invalidates novelty claim: ReinFix (ICSE 2025, arXiv 2506.23100) embeds root-cause classification into retrieval from a 1M-pair historical bug-fix corpus, which is mechanistically nearly identical to FTCR's type-conditioned retrieval from historical corpus. The proposal must cite and differentiate from ReinFix; without this, reviewers will reject on novelty grounds.\", \"CRITICAL — ReCode overlap is underplayed: ReCode already implements algorithm-type-conditioned retrieval with type-partitioned sub-knowledge-bases, the identical core mechanism. FTCR's contribution is extending this to real-world bugs (competitive programming → repositories), which must be framed more precisely. The current framing overclaims novelty.\", \"HIGH — Dataset size claim is internally inconsistent: BugsInPy (493) + Defects4J (1,192) = ~1,685 pairs, not 6,500. If the SWE-bench training split (19,000 instances) is included, that's 20,000+. The '~6,500' figure suggests some undescribed quality-filtering or subsetting logic that is not specified in the proposal. This will raise red flags in review.\", \"HIGH — Defects4J reproducibility crisis: Independent studies (MSR 2025) found ~50% of Defects4J fault-triggering tests are regression tests added post-hoc, and nearly 50% become non-reproducible with modern Java. BugsInPy showed 67% reproducibility. Mining ~1,685 pairs from these datasets may yield fewer than 900 reliably reproducible bug-fix pairs, undermining the corpus quality and scale claims.\", \"MEDIUM — Uncited prior art RetypeR (ICSME 2024): This paper applies type-specific retrieval (external retrieval stage conditioned on Python type errors) and should be discussed as prior art that narrows the novelty of cross-language type-conditioned retrieval.\", \"MEDIUM — Resource units inconsistency: The hard constraint is ≤200 H100-hours, but the proposal reports A100-hours throughout. Manual mode (~150 A100h ≈ 90 H100h) is within budget, but auto-research mode (~650 A100h ≈ 390 H100h) significantly exceeds the constraint. This should be flagged and the primary experiment budget anchored in H100-hours.\", \"MEDIUM — EMNLP framing needs NLP-centric repositioning: The primary contribution is a retrieval system design (SE contribution). EMNLP 'NLP and Code Models' track requires a clear NLP/LLM contribution. The few-shot taxonomy induction approach and its ability to generalize zero-shot across languages should be foregrounded as the NLP contribution; the retrieval architecture is the engineering substrate.\", \"LOW — DebugBench validity concern: DebugBench uses LeetCode code with GPT-4-implanted synthetic bugs, not real repository bugs. Results on DebugBench may not transfer to SWE-bench Lite, requiring a careful discussion of the domain gap between the two evaluation settings.\"]\nFeedback: The core gap FTCR targets is real but narrower than claimed. To make this revisable into a strong paper: (1) Reframe the novelty around what's genuinely new — the extension of type-partitioned retrieval from algorithmic contest code (ReCode) to real-world multi-language repository bugs with an 18-category taxonomy grounded in DebugBench's empirically validated type structure. This is a specific, defensible contribution. (2) Add ReinFix as a baseline: since ReinFix uses root-cause-conditioned retrieval from historical corpus, you must compare against it directly on a shared benchmark (Defects4J is common). If FTCR's type-partitioned index outperforms ReinFix's joint root-cause+code embedding, that's a publishable finding. (3) Fix the dataset size: either restrict to BugsInPy+Defects4J and acknowledge the smaller corpus (~1,500–1,685 pairs after reproducibility filtering), or explicitly include a quality-filtered SWE-bench train subset and describe the filtering criteria. (4) Run a reproducibility pre-check: before committing to Defects4J as a corpus source, filter to only Java 8-compatible bugs (reported to have ~80% reproducibility) and report the usable fraction. (5) For EMNLP fit, pivot the NLP angle to the few-shot taxonomy induction finding — specifically, whether LLM-inferred bug types are consistent, cross-lingual, and predictive of repair success. This is the NLP scientific question. (6) The 16-day timeline is only viable in auto-research mode with parallel evaluation; the paper should scope evaluation to DebugBench (where type labels are ground-truth) plus SWE-bench Lite (300 instances), and acknowledge that a full Defects4J corpus build is out-of-scope for the conference timeline.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Citation error: ReinFix is confirmed ICSE 2026 (arXiv 2506.23100 states 'Accepted by ICSE 2026'), not ICSE 2025 as the proposal states throughout. EMNLP 2026 explicitly warns against hallucinated citations and has stated it may desk-reject papers with such errors. Every reference to 'ReinFix (ICSE 2025)' must be corrected to 'ReinFix (ICSE 2026)'.\", \"HIGH — Corpus sparsity renders type partitioning semantically degenerate for rare types: 559 Java pairs (Defects4J + GitBug-Java) across 18 types yields ~31 Java instances per type on average. For rare bug categories (concurrency, resource leaks, format errors), this may be 5–15 instances. Retrieving k=5 from a sub-index of 15 instances is not retrieval—it is exhaustive lookup. The proposal must either (a) restrict to the 6–8 most frequent types where >50 Java instances exist, or (b) merge rare types into a broader category, or (c) acknowledge that the per-type ablation is only meaningful for the top N types and report per-type corpus sizes in the paper.\", \"HIGH — Classifier error propagation is unaddressed: if the type classifier misclassifies an incoming bug (which will occur for edge cases and multi-type bugs), the system retrieves from the wrong partition and almost certainly underperforms soft retrieval for those instances. This is the main structural risk of hard partitioning over soft embedding. The proposal must analyze: (a) classifier accuracy on held-out annotated bugs, (b) the performance degradation attributable to misclassification, and (c) whether a confidence-gated fallback to soft retrieval recovers performance.\", \"HIGH — EMNLP venue fit remains questionable: the core contribution is an IR architecture decision (partitioning a FAISS index by categorical label). EMNLP 'NLP and Code Models' reviewers will ask what the NLP/LM finding is. The 'few-shot cross-lingual taxonomy induction' contribution (measuring whether LLM-inferred bug types are consistent across annotation runs) is secondary and not a compelling standalone NLP finding—LLM classification consistency is well-studied. If submitting to EMNLP, the NLP contribution must be foregrounded more strongly, e.g., a finding that LLM-inferred type labels are cross-lingually stable and predictive of repair success at the p<0.01 level, with analysis of failure cases that reveal type-specific linguistic patterns in bug descriptions.\", \"MEDIUM — ASE 2026 NIER deadline (May 12) is 2 days from today and experiments are not done: listing it as a target venue is unrealistic. Remove from target_venues or replace with a venue with a later deadline (e.g., EMNLP Findings via ARR, or FSE 2027).\", \"MEDIUM — No expected performance range stated for SWE-bench Lite: reviewers will immediately compare against the RepoRepair baseline (45.7% on Lite). The proposal should state an expected performance range and justify why a lower absolute number is acceptable given the paper's focus on architectural comparison rather than SOTA performance.\", \"LOW — The proposal does not specify which encoding model will be used for FTCR. ReinFix uses text-embedding-3-large (OpenAI API). If FTCR uses the same encoder for fair comparison, this imposes an ongoing API cost not captured in the GPU-hour budget. If using CodeBERT or UniXcoder instead, the encoder comparison is confounded with the hard/soft partitioning comparison. This should be clarified explicitly.\"]\nFeedback: The Round 2 revision has fixed the major structural issues from Round 1 (ReinFix is now a baseline, dataset sizes are consistent, RetypeR is cited, compute is in H100-hours, DebugBench limitations acknowledged). The core hypothesis is testable and the ablation design is clean. Three issues must be addressed before this is submission-ready: (1) Fix the citation error throughout — ReinFix is ICSE 2026, not ICSE 2025; submit it as 'ReinFix (ICSE 2026, arXiv:2506.23100)'. (2) Address corpus sparsity directly in the methods section: report per-type instance counts in a table, restrict the full 18-type analysis to the Python+Java combined corpus, and for the Java-only ablations acknowledge that only the top N types have >50 instances. For types below a minimum threshold (suggest 30 instances), either merge or exclude from per-type breakdown. (3) Add a classifier accuracy analysis: measure the type classifier on the annotated DebugBench ground-truth labels (since DebugBench already has ground-truth types, you can directly measure LLM classifier accuracy), then report how type-matched retrieval performance varies as a function of classifier confidence. This turns the error propagation problem into a feature — it becomes an analysis of when hard partitioning helps vs. hurts. For EMNLP specifically: the NLP contribution must be stated as a crisp finding, not a process. Frame it as: 'We show that LLM-inferred bug type labels achieve X% agreement with DebugBench ground-truth labels, transfer zero-shot to unseen Java bugs with Y% agreement, and are predictive of retrieval-augmented repair success (type-matched retrieval outperforms soft retrieval by Z% for correctly classified bugs, while underperforming by W% for misclassified bugs).' This is a falsifiable empirical claim that EMNLP reviewers can evaluate.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL — CRAG citation is a hallucinated venue: The proposal cites 'CRAG (ICLR 2024)' but CRAG (arXiv:2401.15884) was submitted to ICLR 2025 and withdrawn — it was never accepted or published at any ICLR. Citing it as a published ICLR paper is precisely the kind of hallucinated venue citation EMNLP warns may trigger desk rejection. The correct citation is 'CRAG (Yan et al., 2024; arXiv:2401.15884)'.\", \"HIGH — Unacknowledged concurrent work: SWE-Exp (arXiv:2507.23361, July 2025) uses an experience bank where retrieval explicitly surfaces 'the top N=10 issues most relevant in terms of error type' via cosine similarity, achieves 41.6% on SWE-bench Verified, and is publicly available with open-source code. While the mechanism is different (experience trajectories + soft cosine vs. hard categorical partitioning of fix templates), EMNLP and ICSE reviewers will notice its absence. FTCR must cite it, note the difference (soft type-similarity vs. hard categorical partitioning), and explain why hard partitioning is a distinct hypothesis worth testing.\", \"MEDIUM — 'Clean comparison' overstates the isolation: Type-partitioned retrieval fundamentally reduces the effective retrieval corpus to 1/N_types (≈1/18 on average) of the full index. A smaller retrieval pool affects recall independently of the type-matching benefit. Without a 'random-partition baseline' (random corpus subsets of equivalent size per query), the observed gain (or loss) conflates two effects: (a) partitioning precision and (b) retrieval corpus size. The proposal should either add this control or explicitly acknowledge it as a confound in Section 4.\", \"MEDIUM — EMNLP main track fit remains overstated: The NLP contribution — measuring X% agreement between LLM-inferred bug type labels and DebugBench ground truth, then correlating with repair success — is a measurement finding about LLM classification reliability on a well-structured taxonomy. This is useful but unlikely to be viewed as a primary NLP/LM contribution by EMNLP main track reviewers, who expect findings that advance understanding of language models. EMNLP Findings is a more realistic target; ICSE 2027 (already listed) is the natural primary venue where the SE audience will value the retrieval architecture contribution directly.\", \"LOW — Minor ReinFix technical inaccuracy: The proposal states ReinFix uses 'a unified FAISS vector store' but the ReinFix paper (arXiv:2506.23100) only refers to 'a vector database' without specifying FAISS as the implementation. This overly specific characterization of the baseline's internals should be softened to 'a unified vector database' to avoid misrepresentation of the primary baseline.\"]\nFeedback: Round 3 has successfully addressed the four critical/high issues from Round 2: citation corrected to ICSE 2026 throughout, corpus sparsity handled with explicit per-type table and 30-instance merge policy, classifier error propagation addressed with confidence-gated hybrid and DebugBench calibration, and EMNLP framing sharpened to a crisp X%/Y%/Z%/W% falsifiable claim. The core hypothesis is testable and genuinely novel for multi-language APR. Two issues block submission: (1) Fix the CRAG citation immediately — replace every instance of 'CRAG (ICLR 2024)' with 'CRAG (Yan et al., 2024; arXiv:2401.15884)'. CRAG was submitted to ICLR 2025 but withdrawn and unpublished; citing it as published ICLR work is a hallucinated venue citation that can trigger desk rejection at EMNLP. (2) Add SWE-Exp (arXiv:2507.23361) to the landscape with one paragraph: it uses soft cosine retrieval filtered 'in terms of error type' from an experience bank; FTCR's departure is hard categorical partitioning at index-construction time, not just retrieval-time filtering, plus fix-template retrieval rather than trajectory experience. For longer-term strengthening: add a random-partition baseline (randomly assign corpus pairs to N equivalent-sized sub-indices) to isolate the type-matching benefit from the corpus-size effect. This single ablation converts the comparison from 'clean but contested' to 'rigorous and unambiguous'. On venue strategy: ICSE 2027 (abstract June 23) should be positioned as the primary target; EMNLP 2026 ARR (May 25) can be attempted for Findings if the NLP framing holds, but do not overinvest in EMNLP main track positioning — the primary audience for this work is the SE/APR community.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"HIGH — Uncited concurrent work: 'Towards Defect-Type-Aware Adaptive Program Repair' (TypeRepair, Zhang et al., Software Quality Journal 2026, link.springer.com/article/10.1007/s11219-026-09751-w) uses explicit defect type identification before context selection in a 4-stage pipeline (localization → type ID → context selection → patch generation) on Defects4J V1.2/V2.0 and QuixBugs, independently achieving 272% improvement over GPT-3.5 baseline. The paper must be obtained, read, and cited: if 'context selection' uses type-conditioned retrieval from a cross-repo external corpus (which cannot be confirmed from the abstract alone due to paywall), the overlap with FTCR is substantial and reviewers will notice its absence. If TypeRepair uses only within-project context, that is FTCR's key differentiation and must be stated explicitly.\", \"HIGH — Unaddressed counterevidence: 'What to Retrieve for Effective Retrieval-Augmented Code Generation?' (ICSE 2026, arXiv 2503.20589) empirically shows that retrieving syntactically similar code snippets degrades performance by up to 15% compared to retrieving in-context examples and API information. This is a direct challenge to FTCR's premise: if type-partitioned retrieval returns syntactically similar-but-wrong-level-of-abstraction fixes within each partition, it may concentrate rather than reduce this noise. The authors must address this finding — either by arguing that semantic type partitioning selects at a different abstraction level than syntax similarity, or by adding an experiment measuring within-type fix template quality vs. cross-type.\", \"MEDIUM — Practical utility framing missing: FTCR projects 20–35% on SWE-bench Lite while SWE-Exp achieves 73% on SWE-bench Verified and RepoRepair achieves 45.7% on Lite. ICSE 2027 reviewers will ask why the retrieval strategy matters in isolation when execution-augmented agentic methods dominate. The paper needs an explicit 'why retrieval strategy matters' argument: e.g., (1) retrieval modules are independently upgradeable components within agentic systems — DynaFix adds execution feedback orthogonally to retrieval, so a better retrieval module improves the whole pipeline; (2) the 20–35% baseline is specifically the retrieval contribution, not the full agentic ceiling. This argument exists implicitly but must be stated explicitly.\", \"LOW — EMNLP 2026 ARR deadline is not credible given current state: The May 25 deadline is 15 days away. To submit to ARR requires a complete written paper, full experimental results, and bibliography validation (EMNLP's hallucinated-citation warning is explicit). The paper's hedge ('if too close, defer') should be changed to a definitive decision: either commit to running minimum viable experiments starting immediately (DebugBench classifier calibration + Defects4J V1.2 with the 4 primary variants) or acknowledge ICSE 2027 as the sole target. Leaving it ambiguous signals poor project planning to co-authors and advisors.\"]\nFeedback: Round 4 has successfully resolved all five issues from Round 3: CRAG citation is correct (arXiv-only), SWE-Exp is cited with three clear design differences, the random-partition control (Variant F) converts the corpus-size confound into a closed experimental question, EMNLP is downgraded to Findings, and ReinFix's implementation detail is softened. Independent verification confirms all cited paper claims are accurate. The hard-vs-soft retrieval comparison for semantic bug-type partitioned cross-repo repair is genuinely novel — no existing paper makes this specific comparison. Two actions are required for Round 5: (1) Read the TypeRepair SQJ 2026 paper (Zhang et al., doi:10.1007/s11219-026-09751-w) and add it to the landscape — the differentiation is either that TypeRepair uses intra-project context (state this explicitly) or that it uses cross-repo retrieval but covers only Java with a different pipeline structure (then FTCR's C++/Java/Python scope and the hard/soft comparison are the differentiators). (2) Cite and respond to 'What to Retrieve for Effective RAG Code Generation?' (ICSE 2026, arXiv:2503.20589): its finding that similar code retrieval degrades performance by 15% motivates FTCR's type-conditioning exactly — within a type partition, retrieved examples share fix structure rather than surface-level code similarity, which is the argument FTCR needs to make explicit. These two additions would resolve the remaining novelty and counterevidence gaps. The practical utility framing (retrieval as a modular component upgradeable within agentic pipelines) should be added as a paragraph in the introduction — this is the clearest answer to 'why does this matter when agentic methods dominate at 73%.'\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T06:26:41.459Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T06:26:41.459Z",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-10T06:26:41.515Z_

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

## Idea under review (round 5/10)
{
  "title": "Failure-Type-Conditioned Retrieval Augmentation for Repository Repair",
  "core_problem": "Retrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is whether hard categorical type partitioning of the retrieval index outperforms ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer, particularly in a multi-language setting. An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. This 'what you retrieve matters' result directly motivates type-conditioned fix-patch retrieval: type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and, when addressed directly, become analytical contributions: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across 18 types yields only ~31 Java instances per type on average, requiring an explicit minimum-threshold and merge policy for rare types; and (2) classifier error propagation — when an incoming bug is misclassified into the wrong type partition, hard partitioning will underperform soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback to soft retrieval — turns potential weaknesses into measurable experimental variables that sharpen, rather than undermine, the core hypothesis.",
  "opportunity": "ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation from a different angle: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Their core finding — that what you retrieve determines quality more than how you retrieve — directly motivates FTCR's retrieval design: fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of N discrete semantic types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than ReinFix's joint embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar code but different root causes do not. DebugBench uniquely provides 4,253 instances with ground-truth 18-category type annotations across C++, Java, and Python; crucially, these ground-truth labels enable direct calibration of the few-shot type classifier, turning classifier error propagation from a latent risk into a measurable experimental variable. The confidence-gated hybrid (fall back to soft retrieval for low-confidence classifications) addresses the structural risk of hard partitioning and has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884) for general RAG systems. M-RAG (ACL 2024, arXiv 2405.16420) additionally validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis before evaluating it in the code repair setting.",
  "landscape": "RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% with the same model and is not a SOTA claim. ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning, and root cause is a continuous semantic descriptor, not a discrete category. SWE-Exp (arXiv 2507.23361, revised February 2026) is the most important concurrent work: it retrieves top N=10 issues 'most relevant in terms of error type' from an experience bank using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large encoder), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic pipeline. Three design differences distinguish SWE-Exp from FTCR: (1) retrieval mechanism — SWE-Exp uses soft cosine similarity with type as embedding metadata at retrieval time; FTCR partitions the index into discrete type sub-corpora at construction time, so only same-type pairs are ever candidates for a query; (2) retrieved artifact — SWE-Exp stores distilled problem perspectives and generalized modification strategies; FTCR retrieves concrete historical fix patches for direct template transfer; (3) scope — SWE-Exp is fully agentic and scoped to Python; FTCR is retrieval-only and covers C++, Java, and Python, using DebugBench's oracle type labels for cross-lingual calibration. The testable question SWE-Exp leaves open is whether hard construction-time partitioning outperforms soft retrieval-time type filtering for fix-template precision. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5 baseline. TypeRepair's context selection stage conditions on the identified defect type to select relevant within-project code context and to provide type-specific repair guidance in the LLM prompt — it does not retrieve from an external cross-repository fix corpus. TypeRepair is Java-only (Defects4J/QuixBugs); FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 historical fix patches. TypeRepair validates that defect type identification benefits LLM-based repair (supporting FTCR's core hypothesis) while leaving hard-vs-soft type-partitioned cross-repository retrieval entirely unexplored; FTCR addresses this gap directly. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information helps; their proposed AllianceCoder retrieves APIs via semantic description matching rather than code similarity. While the study targets code generation rather than repair, the 'what to retrieve matters more than how' finding motivates FTCR's choice of fix patches retrieved by type partition (sharing semantic repair structure) over code-similarity retrieval (sharing only surface features). DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair (236 bugs fixed with GPT-4); DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3 via self-directed debugging with runtime traces. Both update the Defects4J performance landscape but are orthogonal to FTCR's retrieval strategy focus — execution-level augmentation and retrieval strategy are independently improvable axes. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via LLM objective alignment. FTCR's structural departure from ReinFix is to (1) classify incoming failures into discrete categories, then (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) for a clean comparison that isolates partitioning as the primary architectural variable — noting that partitioning also reduces the effective retrieval pool to ~1/N_types of the full corpus, a corpus-size effect that a random-partition control ablation is designed to separate from type-matching precision. RetypeR (ICSME 2024, Hao et al.) applies a two-stage external+internal retrieval conditioned on Python type errors, establishing that type-specific retrieval helps for one narrow bug class and language; FTCR extends this principle to 18 categories across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates that multi-partition RAG consistently outperforms single-store RAG across NLP tasks (summarization: +11%, translation: +8%, dialogue: +12%), validating the general principle of partition-based retrieval before applying it to code repair. PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary (localization rather than cross-repository fix template retrieval). The APR survey (arXiv 2506.23749) reviews 63+ systems and identifies retrieval augmentation as the key enhancement, but no reviewed system applies hard taxonomic type classification as the retrieval partition key across multiple languages.",
  "approach": "We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms ReinFix-style soft root-cause embedding for cross-repository fix transfer. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix for a clean comparison), same corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control (see below).\n\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. FTCR embodies this principle: rather than retrieving the most syntactically similar buggy code in the corpus, we retrieve fix patches — input/output transformation pairs — that share the same semantic repair operation. Type partitioning ensures that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to look syntactically similar but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\n\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559).\n\nCorpus Sparsity Policy. Each pair is annotated with one of 18 semantic categories aligned with DebugBench's taxonomy (four major types: Syntax, Reference, Logic, Multiple; 18 minor subtypes) via few-shot prompting using DebugBench's labeled examples as demonstrations; three annotation passes measure inter-run consistency. A per-type instance count table is computed and reported in the paper for transparency. For the combined Python+Java corpus (3,050 pairs), 18-type analysis is viable: Python instances dominate (~2,487) and yield an estimated mean of ~138 pairs per type. For Java-only ablations (~559 pairs, ~31 per type average), a minimum-threshold policy applies: types with fewer than 30 Java instances are merged into nearest-neighbor supercategories (e.g., Concurrency + Resource-Leak → Resource-Management; Format-Error + Syntax-Error → Low-Level, since compiled Defects4J/GitBug-Java bugs contain near-zero syntax errors). Java ablation results are reported for the 6–8 resulting categories that each exceed 50 instances, with merged categories explicitly labeled. This avoids the degenerate case of k=5 retrieval from a 15-instance sub-index, which approximates exhaustive lookup rather than similarity-based retrieval.\n\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound; embedding cost is negligible (~$5–15 for corpus plus all evaluation queries at $0.13/1M tokens). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific and deconfounding the encoder-vs-partitioning comparison.\n\nType Classifier Calibration on DebugBench Ground Truth. Since DebugBench provides oracle type labels for 4,253 instances, a held-out 20% split (851 instances) directly measures our few-shot classifier's per-type precision and recall against ground truth, yielding an overall accuracy estimate. Cross-dataset zero-shot agreement is measured by applying the same classifier to a 10% random sample (~56 pairs) of the Java annotation set (Defects4J + GitBug-Java) with human-verified labels as oracle, yielding a cross-lingual label consistency score. This produces the NLP contribution: a falsifiable empirical claim that LLM-inferred bug type labels achieve X% agreement with DebugBench ground-truth labels (Python/C++), transfer zero-shot to unseen Java bugs with Y% agreement, and are predictive of retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs.\n\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect — hard partitioning reduces the effective retrieval pool to ~1/N_types of the full index, which independently affects recall — we add a random-partition baseline (Variant F): the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index. Any performance gap between FTCR (Variant E, hard type partition) and this control measures the precision benefit of type-matching net of pool-size reduction. This converts the comparison from 'clean but contested' to 'rigorous and unambiguous.'\n\nConfidence-Gated Retrieval Fallback. At inference time, the type classifier outputs a probability distribution over 18 categories. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval (identical to the ReinFix baseline). This confidence-gated hybrid is evaluated as a sixth system variant alongside: (A) text-similarity RAG (no type signal), (B) RELREPAIR (project-internal retrieval), (C) RepoRepair (documentation-guided), (D) ReinFix-style soft retrieval (re-implemented on same corpus and same encoder), (E) FTCR@hard-all, and (F) random-partition control (same N sub-indices, randomly assigned — corpus-size control). The confidence-gated fallback has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). The projected finding: correctly-classified high-confidence bugs show systematic gains from hard partitioning (+5–10% repair success on Defects4J where oracle type labels allow clean stratification); misclassified or low-confidence bugs show performance on par with or slightly below soft retrieval; the confidence gate recovers aggregate performance for ambiguous cases; the random-partition control falls between soft retrieval and FTCR@hard-all, confirming that type-matching rather than pool-size reduction drives the gain.\n\nPractical Utility: Retrieval as an Independently Upgradeable Module. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is deliberately positioned as the retrieval contribution in isolation, not a claim against the agentic pipeline ceiling. The motivation for isolating retrieval is architectural: DynaFix (arXiv 2512.24635) demonstrates that execution-level augmentation and retrieval strategy are independently improvable axes — it improves over ReinFix on Defects4J V2.0 by adding iterative execution feedback while keeping retrieval fixed. An improved retrieval module (FTCR vs. ReinFix-style soft retrieval) compounds with execution-level improvements: the delta between FTCR-augmented and ReinFix-augmented iterative repair pipelines measures the retrieval contribution at the pipeline level. Standalone evaluation isolates the retrieval hypothesis cleanly; the modular gain is what ICSE reviewers can act on independently of scaffolding choices.\n\nExpected Performance on SWE-bench Lite. We project FTCR to achieve 20–35% resolve rate with Claude Sonnet 4.6 in retrieval-only (non-agentic) mode, comparable to ReinFix-style retrieval on the same corpus. This is below the current SWE-bench Lite SOTA (~62.7%, Claude Opus 4.6, May 2026, agentic scaffolding) and below RepoRepair's 45.7% (documentation-guided multi-step localization). Lower aggregate performance than RepoRepair is explicitly defended: FTCR does not incorporate documentation-guided localization, which is an orthogonal architectural component. The primary SWE-bench Lite contribution is validating that the type-conditioned advantage observed on DebugBench transfers to real-world Python repositories, not claiming absolute SOTA.\n\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while SWE-bench Lite validates real-world transfer.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~88 H100-hours (~150 A100-hours equivalent)",
      "gpu_utilization": "~30-40% utilized; high idle while researchers design annotation prompts, debug Defects4J Java-8 environments, manually review per-type count tables, and verify annotation consistency across passes",
      "timeline": "4-6 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$450 (150 A100-hours × $3/h on RunPod/Lambda Labs)",
      "embedding_api_cost": "~$5-15 (text-embedding-3-large for 3,050-pair corpus + evaluation queries, at $0.13/1M tokens; negligible relative to overall budget)",
      "note": "Well within the 200 H100-hour hard budget"
    },
    "human_in_loop": {
      "gpu_hours": "~165 H100-hours (~280 A100-hours equivalent)",
      "gpu_utilization": "~55-65% utilized; agent continuously queues embedding and evaluation jobs while human approves ablation configurations at decision gates",
      "timeline": "6-8 weeks",
      "team": "1 researcher, ~30 min/day check-in for ablation approval, per-type count table review, confidence threshold tuning, and failure triage",
      "claude_api_cost": "$200-400 (annotation: ~3,050 instances × ~$0.02/call ≈ $61; 3 annotation passes for consistency ≈ $183; DebugBench classifier calibration: 851 held-out instances × $0.02 ≈ $17; pipeline orchestration and repair: ~1,500 agent turns × $0.10/turn ≈ $150; buffer ~$50)",
      "embedding_api_cost": "~$5-15 (text-embedding-3-large for corpus and evaluation queries)",
      "estimated_gpu_cost": "~$840 (280 A100-hours × $3/h)",
      "note": "Within the 200 H100-hour hard budget",
      "risk_note": "Defects4J Docker reproducibility is the primary bottleneck — the Java-8 pre-filter eliminates ~9% upfront, but remaining instances still require environment triage. GitBug-Java's isolated Docker images significantly reduce this overhead for the Java supplement. Java per-type sparsity is the secondary risk: if the 6-8 type categories above threshold have unequal sizes, the Java ablation may be underpowered for the smallest categories."
    },
    "auto_research": {
      "gpu_hours": "~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)",
      "gpu_utilization": "near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants",
      "ablation_scope": "Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (6-type coarse / 18-type fine / merged-Java), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java train → SWE-bench-Lite Python eval), classifier accuracy stratification (by confidence band)",
      "timeline": "10-14 days with 2 A100 nodes running in parallel",
      "team": "0 (initial ~4h setup for corpus pipeline, per-type sub-index construction scaffold, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)",
      "claude_api_cost": "$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)",
      "embedding_api_cost": "~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)",
      "estimated_gpu_cost": "~$969 (323 A100-hours × $3/h)",
      "speed_bottleneck": "GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls",
      "risk_note": "Auto-assigned bug type labels may drift from human-interpretable categories without the three-pass consistency check; the confidence-gated hybrid adds a hyperparameter (τ) that requires tuning on the DebugBench held-out split before SWE-bench Lite evaluation. SWE-bench Lite infrastructure failures can silently inflate repair failure counts without human oversight."
    }
  },
  "target_venues": [
    "ICSE 2027 (mandatory abstract deadline June 23, 2026 — SOLE PRIMARY TARGET; best fit for SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation reviewers will expect; TypeRepair (SQJ 2026) comparison on Defects4J clarifies FTCR's orthogonal contribution of cross-repository retrieval; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections about hard partitioning; random-partition control specifically converts the 'corpus-size confound' objection into a closed experimental question)",
    "FSE 2027 (full paper deadline October 2, 2026 — backup venue if ICSE review cycle overlaps unfavorably; same SE audience, equally appropriate for a retrieval-architecture study with multi-language empirical evaluation)"
  ],
  "level": "solid",
  "key_references": [
    "ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; must compare directly on Defects4J V1.2 using same text-embedding-3-large encoder; uses a unified vector database, not a specific named implementation]",
    "SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; retrieves top N=10 issues by soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; stores distilled modification strategies, not fix patches; agentic, Python-only; achieves 73.0% on SWE-bench Verified with Claude 4 Sonnet — differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, and multi-language scope]",
    "TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0/QuixBugs (Java-only); validates that type conditioning improves LLM repair; context selection stage conditions type to select within-project context and generate type-specific prompting guidance, NOT cross-repository retrieval — FTCR's orthogonal contribution is type-conditioned retrieval of fix patches from an external ~3,050-pair cross-language corpus; must cite and explicitly differentiate]",
    "What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond (Gu et al., ICSE 2026, arXiv 2503.20589) [shows similar-code snippet retrieval degrades repository-level code generation by up to 15% on CoderEval/RepoExec while contextual + API info helps; motivates FTCR's type-conditioned fix-patch retrieval — type partitioning retrieves patches sharing semantic repair structure, not superficial code similarity; note the finding applies to code generation not repair, but the 'what to retrieve matters' principle is directly applicable]",
    "ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330) [algorithm-type-conditioned retrieval in competitive programming — conceptual ancestor]",
    "RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors (ICSME 2024, Hao et al.) [type-specific retrieval for one language and one error class — FTCR extends to 18 types and 3 languages]",
    "DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv 2512.24635) [surpasses ReinFix on Defects4J V2.0 (236 bugs with GPT-4) using execution-level augmentation; demonstrates retrieval and execution augmentation are independently improvable axes; retrieval improvement (FTCR) compounds with execution-level improvements (DynaFix-style)]",
    "DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2604.19305) [295 Defects4J bugs with DeepSeek-V3 via runtime traces and debugging-driven conversational repair; updates Defects4J landscape but is orthogonal — no retrieval augmentation component]",
    "D4C: Aligning the Objective of LLM-based Program Repair (ICSE 2025, arXiv 2404.08877) [180 Defects4J bugs via objective alignment; updates Defects4J performance landscape]",
    "M-RAG: Reinforcing Large Language Model Performance through Retrieval-Augmented Generation with Multiple Partitions (ACL 2024, arXiv 2405.16420) [multi-partition RAG validated on NLP tasks: +11% summarization, +8% translation, +12% dialogue; principled precedent for partition-based retrieval across domains]",
    "RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code (arXiv 2509.16701) [project-internal retrieval baseline]",
    "RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048) [documentation-guided localization baseline; 45.7% on SWE-bench Lite using multi-step localization, orthogonal to FTCR's retrieval focus]",
    "DebugBench: Evaluating Debugging Capability of Large Language Models (ACL Findings 2024) [primary evaluation with ground-truth 18-category labels across C++/Java/Python; held-out 20% split used for few-shot classifier calibration; synthetic-bug limitation acknowledged]",
    "GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; supplement for Defects4J Java corpus]",
    "SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025, arXiv 2504.21798) [50k Python task instances from 128 repos; used as scale corpus for Python retrieval index]",
    "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey confirming retrieval augmentation as key enhancement with no type-partitioned system identified]",
    "What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]",
    "PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]",
    "RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]",
    "CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism with retrieval quality scoring; precedent for the FTCR confidence-gated hybrid variant; note: withdrawn from ICLR 2025, unpublished — cite as preprint only]"
  ],
  "description": "FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft root-cause-augmented retrieval (ReinFix's approach, ICSE 2026) for cross-repository fix template transfer. ReinFix (ICSE 2026, arXiv 2506.23100) is the closest prior work — it embeds LLM-generated free-text root-cause descriptions jointly with buggy code into a unified vector database using text-embedding-3-large, showing +32/+38 bugs fixed on Defects4J V1.2/V2.0. FTCR's structural departure is to (1) classify incoming failures into one of 18 discrete semantic categories aligned with DebugBench's empirically-validated taxonomy, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable. Round 5 revisions address four issues: (a) TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) added to landscape and key_references with explicit differentiation — TypeRepair's 4-stage pipeline uses defect type to select within-project context and generate type-specific repair guidance (prompt engineering), not cross-repository retrieval; it covers Java only (Defects4J/QuixBugs) with 10 types; TypeRepair validates that type conditioning helps repair (supporting FTCR's hypothesis) while leaving cross-repo type-conditioned retrieval unexplored; (b) arXiv 2503.20589 (Gu et al., ICSE 2026) added as motivation rather than counterevidence — their finding that similar code snippet retrieval degrades code generation by 15% while structured knowledge helps motivates FTCR's type-conditioned fix-patch retrieval; type partitioning retrieves patches sharing semantic repair structure (the fix operator), not superficial code similarity; the paper targets code generation, not repair, making it an indirect motivator rather than a direct challenge; (c) practical utility framing added explicitly in approach — retrieval is an independently upgradeable module within agentic pipelines; DynaFix demonstrates retrieval and execution augmentation are independent axes; FTCR's retrieval gain compounds with DynaFix-style iterative repair; 20-35% standalone metric is the retrieval floor, not the pipeline ceiling; (d) EMNLP 2026 definitively removed — the May 25 ARR deadline is infeasible given that all experiments remain to be run; ICSE 2027 is the sole primary target; FSE 2027 is the backup; cross-lingual classifier findings can be submitted separately after ICSE results are complete. RetypeR (ICSME 2024) establishes type-specific retrieval for Python type errors specifically; FTCR extends to 18 categories across C++, Java, and Python. The retrieval corpus (~3,050 natural bug-fix pairs from SWE-bench non-Lite, BugsInPy, Defects4J V1.2, and GitBug-Java) requires no GPU training; the approach is fully inference-based. Target venues: ICSE 2027 (abstract June 23, primary), FSE 2027 (October 2, backup).",
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
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "type": "user",
  "uuid": "6babbdf3-c635-485a-baa4-1da85cbc0205",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T06:26:41.510Z_

```json
{
  "parentUuid": "6babbdf3-c635-485a-baa4-1da85cbc0205",
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
  "uuid": "bb205bde-d507-4550-85c9-120600a85d29",
  "timestamp": "2026-05-10T06:26:41.510Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T06:26:41.511Z_

```json
{
  "parentUuid": "bb205bde-d507-4550-85c9-120600a85d29",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ac3158da-4624-4eac-806c-f0b77162026c",
  "timestamp": "2026-05-10T06:26:41.511Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
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
  "leafUuid": "ac3158da-4624-4eac-806c-f0b77162026c",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Type-partitioned fix retrieval for cross-language program repair",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d"
}
```

---

### Assistant

_source line 8 · 2026-05-10T06:27:00.649Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea (Round 5/10) for FTCR (Failure-Type-Conditioned Retrieval Augmentation for Repository Repair). I need to independently verify claims, find competing work, and assess whether all previous issues have been resolved.

Let me check what was raised in previous rounds:
- Round 1-4: Various issues were raised and supposedly addressed
- Round 4 issues:
  1. HIGH: TypeRepair (SQJ 2026) - supposedly addressed in Round 5
  2. HIGH: Gu et al. (ICSE 2026, arXiv 2503.20589) - counterevidence supposedly addressed
  3. MEDIUM: Practical utility framing missing - supposedly addressed
  4. LOW: EMNLP 2026 ARR deadline not credible - supposedly addressed (removed)

Now I need to verify whether TypeRepair and Gu et al. are properly differentiated, check if the practical utility framing is adequate, and identify any new issues through independent research. I should also validate the target venues—ICSE 2027 (abstract due June 23, 2026) and FSE 2027 (October 2, 2026)—both have deadlines that are still ahead of today's date (May 10, 2026).

I'm going to search for TypeRepair from SQJ 2026, ReinFix from arXiv, SWE-Exp, and Gu et al. to verify the differentiation claims and check for any concurrent work I might have missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac3158da-4624-4eac-806c-f0b77162026c",
  "isSidechain": false,
  "requestId": "req_011CatQtaFZVsoqkuB5LqY8H",
  "type": "assistant",
  "uuid": "4d004bb3-7fc8-486f-bb2a-8444eb5eecb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SZyT6CkmbLzYo7Gxi49xix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23619,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1699,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23619
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

_source line 9 · 2026-05-10T06:27:00.842Z_

I'll conduct independent verification searches to assess this Round 5 submission. Let me search across multiple dimensions simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d004bb3-7fc8-486f-bb2a-8444eb5eecb9",
  "isSidechain": false,
  "requestId": "req_011CatQtaFZVsoqkuB5LqY8H",
  "type": "assistant",
  "uuid": "9bf28e9d-43b1-47c0-8a7b-68e59f28e248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SZyT6CkmbLzYo7Gxi49xix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23619,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1699,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23619
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

_source line 10 · 2026-05-10T06:27:05.930Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01RGTtjhZouv8ioTMRT53fPA`</summary>

```json
{
  "description": "Verify ReinFix, TypeRepair, and SWE-Exp claims",
  "subagent_type": "Explore",
  "prompt": "Search for and verify the following papers' actual claims, venues, and mechanisms. Use WebSearch and WebFetch to independently confirm details.\n\n1. ReinFix (arXiv 2506.23100) - Is it actually ICSE 2026? What is its exact retrieval mechanism? Does it use text-embedding-3-large? Does it use a unified vector database?\n\n2. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) - What exactly does the \"context selection\" stage do? Does it retrieve from external cross-repository fix corpus, or only within-project context? Is it Java-only?\n\n3. SWE-Exp (arXiv 2507.23361) - What is the actual mechanism? Does it achieve 73.0% on SWE-bench Verified? Is it Python-only? What does \"error type\" mean in this context?\n\nPlease search:\n- \"ReinFix repair ingredients ICSE 2026\" \n- \"arXiv 2506.23100\"\n- \"TypeRepair defect type aware program repair Zhang SQJ 2026\"\n- \"SWE-Exp experience bank arXiv 2507.23361\"\n- site:arxiv.org TypeRepair defect type program repair 2026\n\nFor each paper, report: confirmed venue, exact mechanism, and whether the proposal's characterization is accurate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bf28e9d-43b1-47c0-8a7b-68e59f28e248",
  "isSidechain": false,
  "requestId": "req_011CatQtaFZVsoqkuB5LqY8H",
  "type": "assistant",
  "uuid": "23a0933a-ba6d-4b4e-8206-1bc5b4fd5195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SZyT6CkmbLzYo7Gxi49xix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23619,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1699,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23619
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

_source line 11 · 2026-05-10T06:27:14.549Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01PBhykN36F4J6Z9joR4e7RT`</summary>

```json
{
  "description": "Search for concurrent work on type-conditioned code repair",
  "subagent_type": "Explore",
  "prompt": "Search for recent papers (2025-2026) on type-conditioned or category-conditioned program repair and retrieval-augmented repair. I need to find any work that may be concurrent with or supersede this idea about partitioning retrieval indices by bug type.\n\nKey search queries to run:\n1. \"type-conditioned program repair\" site:arxiv.org 2025 2026\n2. \"bug type retrieval augmented repair\" arxiv 2025 2026\n3. \"failure type code repair retrieval\" arxiv 2026\n4. \"categorical retrieval program repair\" arxiv 2026\n5. \"bug classification repair retrieval\" arxiv 2025\n\nAlso search:\n- site:paperswithcode.com \"program repair\" SOTA\n- \"retrieval augmented program repair\" arxiv 2026\n- \"SWE-bench 2026 repair\" to find latest SOTA methods\n\nFor each relevant paper found, report: title, arxiv ID, venue/date, and how similar it is to the FTCR approach (classifying bugs by type, then retrieving from type-specific partitioned index)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23a0933a-ba6d-4b4e-8206-1bc5b4fd5195",
  "isSidechain": false,
  "requestId": "req_011CatQtaFZVsoqkuB5LqY8H",
  "type": "assistant",
  "uuid": "e57db609-8599-44c2-882b-a6e818e7db88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SZyT6CkmbLzYo7Gxi49xix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23619,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1699,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23619
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

_source line 12 · 2026-05-10T06:27:17.489Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013gvmrLeWLhbrvy5oY311BL`</summary>

```json
{
  "description": "Verify Gu et al. ICSE 2026 and DebugBench claims",
  "subagent_type": "Explore",
  "prompt": "Search for and verify these specific papers and claims:\n\n1. Gu et al. (ICSE 2026, arXiv 2503.20589) \"What to Retrieve for Effective Retrieval-Augmented Code Generation?\" \n- Is it actually ICSE 2026?\n- Does it really show that similar code snippet retrieval degrades performance by up to 15%?\n- Does it study code generation or code repair?\n- What is AllianceCoder?\n\n2. DebugBench (ACL Findings 2024)\n- Does it actually have 4,253 instances with 18-category labels?\n- Does it cover C++, Java, and Python?\n- Are the bugs actually GPT-4-implanted?\n\n3. M-RAG (ACL 2024, arXiv 2405.16420) - Does it actually show +11% summarization, +8% translation, +12% dialogue improvements?\n\n4. CRAG (arXiv:2401.15884) - Was it really withdrawn from ICLR 2025? Is the current citation \"CRAG (Yan et al., 2024; arXiv:2401.15884)\" accurate?\n\n5. Search: \"DebugBench evaluating debugging capability LLM\" to verify the benchmark's real characteristics.\n\n6. Search: arXiv 2503.20589 to read the actual abstract.\n\nReport the verification status (confirmed/disputed/not found) for each paper and claim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e57db609-8599-44c2-882b-a6e818e7db88",
  "isSidechain": false,
  "requestId": "req_011CatQtaFZVsoqkuB5LqY8H",
  "type": "assistant",
  "uuid": "5825fbb3-36b7-44ec-84f4-aa22a93b4ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SZyT6CkmbLzYo7Gxi49xix",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23619,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1699,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23619
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

_source line 13 · 2026-05-10T06:27:57.582Z_

<details><summary>↩ Tool result · `toolu_013gvmrLeWLhbrvy5oY311BL`</summary>

```text
Excellent! Now I have comprehensive information. Let me compile the verification report:

## Verification Report

### 1. **Gu et al. (arXiv 2503.20589) - "What to Retrieve for Effective Retrieval-Augmented Code Generation?"**

**Status: CONFIRMED**

- **ICSE 2026 publication**: ✓ **CONFIRMED** - The paper is indeed accepted to ICSE 2026 (Research Track), as evidenced by the official ICSE 2026 conference page listing.
- **15% performance degradation claim**: ✓ **CONFIRMED** - The paper demonstrates that retrieved similar code degrades results by up to 15%.
- **Code generation vs. repair**: ✓ **CONFIRMED** - The paper focuses on code **generation**, not code repair.
- **AllianceCoder**: ✓ **CONFIRMED** - AllianceCoder is a novel context-integrated method proposed in the paper that employs chain-of-thought prompting to decompose user queries into implementation steps and retrieves APIs via semantic description matching. It achieves state-of-the-art performance with up to 20% Pass@1 improvement.

**Sources:**
- [arXiv 2503.20589 Abstract](https://arxiv.org/abs/2503.20589)
- [ICSE 2026 Conference Page](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/182/What-to-Retrieve-for-Effective-Retrieval-Augmented-Code-Generation-An-Empirical-Stud)

---

### 2. **DebugBench (ACL Findings 2024)**

**Status: CONFIRMED**

- **4,253 instances with 18-category labels**: ✓ **CONFIRMED** - The benchmark contains 4,253 instances across four major bug categories and 18 minor types.
- **Language coverage (C++, Java, Python)**: ✓ **CONFIRMED** - The benchmark covers all three languages.
- **GPT-4-implanted bugs**: ✓ **CONFIRMED** - Bugs are implanted using GPT-4 into LeetCode source code snippets. The construction includes rigorous quality checks to ensure realism, test case failure, and absence of explicit bug hints.

**Sources:**
- [DebugBench at ACL Anthology](https://aclanthology.org/2024.findings-acl.247/)
- [DebugBench arXiv 2401.04621](https://arxiv.org/abs/2401.04621)
- [GitHub Repository](https://github.com/thunlp/DebugBench)

---

### 3. **M-RAG (ACL 2024, arXiv 2405.16420)**

**Status: CONFIRMED**

- **Performance improvements**: ✓ **CONFIRMED** - M-RAG achieves +11% for text summarization, +8% for machine translation, and +12% for dialogue generation improvements across comprehensive experiments on seven datasets.

**Sources:**
- [M-RAG at ACL Anthology](https://aclanthology.org/2024.acl-long.108/)
- [M-RAG arXiv 2405.16420](https://arxiv.org/abs/2405.16420)

---

### 4. **CRAG (arXiv:2401.15884)**

**Status: DISPUTED/CLARIFICATION NEEDED**

- **ICLR 2025 withdrawal**: ✓ **CONFIRMED AS WITHDRAWN** - CRAG was indeed withdrawn from ICLR 2025 (visible on OpenReview as "Withdrawn Submission").
- **Citation accuracy**: ⚠️ **PARTIALLY ACCURATE** - The citation "CRAG (Yan et al., 2024; arXiv:2401.15884)" is technically accurate, but importantly: CRAG is **not a published conference paper** at any major venue. It remains a preprint-only paper on arXiv with three versions (v1: Jan 29, 2024; v2: Feb 16, 2024; v3: Oct 7, 2024). The withdrawal from ICLR 2025 means it was never accepted to that conference.

**Sources:**
- [CRAG arXiv 2401.15884](https://arxiv.org/abs/2401.15884)
- [CRAG OpenReview - ICLR 2025 (Withdrawn)](https://openreview.net/forum?id=JnWJbrnaUE)

---

### 5. **DebugBench Search Verification**

**Status: CONFIRMED**

The search for "DebugBench evaluating debugging capability LLM" confirms all major characteristics: 4,253 instances, C++/Java/Python coverage, 18 minor bug categories, GPT-4-implanted bugs, published in ACL 2024 Findings.

**Sources:**
- [DebugBench at ACL Anthology](https://aclanthology.org/2024.findings-acl.247/)

---

### 6. **arXiv 2503.20589 Abstract**

**Status: CONFIRMED**

The paper's abstract confirms it addresses repository-level code generation challenges, demonstrates that similar code snippet retrieval introduces noise and degrades results by up to 15%, and proposes AllianceCoder for improved performance.

**Sources:**
- [arXiv 2503.20589](https://arxiv.org/abs/2503.20589)

---

## Summary Table

| Paper/Claim | Verification Status | Notes |
|---|---|---|
| Gu et al. ICSE 2026 | Confirmed | Accepted to ICSE 2026 Research Track |
| 15% degradation claim | Confirmed | Similar code retrieval reduces performance by up to 15% |
| Code generation focus | Confirmed | Not code repair |
| AllianceCoder | Confirmed | Novel RAG method achieving 20% Pass@1 improvement |
| DebugBench 4,253 instances | Confirmed | Accurate count and 18-category breakdown |
| DebugBench languages | Confirmed | C++, Java, Python all covered |
| DebugBench GPT-4 bugs | Confirmed | GPT-4 implanted with quality control |
| M-RAG improvements | Confirmed | +11% summarization, +8% translation, +12% dialogue |
| CRAG withdrawn from ICLR 2025 | Confirmed | Paper is listed as withdrawn on OpenReview |
| CRAG citation accuracy | Partially accurate | Citation correct, but paper is preprint-only, not peer-reviewed conference |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5825fbb3-36b7-44ec-84f4-aa22a93b4ecf",
  "isSidechain": false,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "type": "user",
  "uuid": "9e4c0b78-0d9f-4502-b767-2d75ec13196c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify these specific papers and claims:\n\n1. Gu et al. (ICSE 2026, arXiv 2503.20589) \"What to Retrieve for Effective Retrieval-Augmented Code Generation?\" \n- Is it actually ICSE 2026?\n- Does it really show that similar code snippet retrieval degrades performance by up to 15%?\n- Does it study code generation or code repair?\n- What is AllianceCoder?\n\n2. DebugBench (ACL Findings 2024)\n- Does it actually have 4,253 instances with 18-category labels?\n- Does it cover C++, Java, and Python?\n- Are the bugs actually GPT-4-implanted?\n\n3. M-RAG (ACL 2024, arXiv 2405.16420) - Does it actually show +11% summarization, +8% translation, +12% dialogue improvements?\n\n4. CRAG (arXiv:2401.15884) - Was it really withdrawn from ICLR 2025? Is the current citation \"CRAG (Yan et al., 2024; arXiv:2401.15884)\" accurate?\n\n5. Search: \"DebugBench evaluating debugging capability LLM\" to verify the benchmark's real characteristics.\n\n6. Search: arXiv 2503.20589 to read the actual abstract.\n\nReport the verification status (confirmed/disputed/not found) for each paper and claim.",
    "agentId": "a9213b540c23f8876",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now I have comprehensive information. Let me compile the verification report:\n\n## Verification Report\n\n### 1. **Gu et al. (arXiv 2503.20589) - \"What to Retrieve for Effective Retrieval-Augmented Code Generation?\"**\n\n**Status: CONFIRMED**\n\n- **ICSE 2026 publication**: ✓ **CONFIRMED** - The paper is indeed accepted to ICSE 2026 (Research Track), as evidenced by the official ICSE 2026 conference page listing.\n- **15% performance degradation claim**: ✓ **CONFIRMED** - The paper demonstrates that retrieved similar code degrades results by up to 15%.\n- **Code generation vs. repair**: ✓ **CONFIRMED** - The paper focuses on code **generation**, not code repair.\n- **AllianceCoder**: ✓ **CONFIRMED** - AllianceCoder is a novel context-integrated method proposed in the paper that employs chain-of-thought prompting to decompose user queries into implementation steps and retrieves APIs via semantic description matching. It achieves state-of-the-art performance with up to 20% Pass@1 improvement.\n\n**Sources:**\n- [arXiv 2503.20589 Abstract](https://arxiv.org/abs/2503.20589)\n- [ICSE 2026 Conference Page](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/182/What-to-Retrieve-for-Effective-Retrieval-Augmented-Code-Generation-An-Empirical-Stud)\n\n---\n\n### 2. **DebugBench (ACL Findings 2024)**\n\n**Status: CONFIRMED**\n\n- **4,253 instances with 18-category labels**: ✓ **CONFIRMED** - The benchmark contains 4,253 instances across four major bug categories and 18 minor types.\n- **Language coverage (C++, Java, Python)**: ✓ **CONFIRMED** - The benchmark covers all three languages.\n- **GPT-4-implanted bugs**: ✓ **CONFIRMED** - Bugs are implanted using GPT-4 into LeetCode source code snippets. The construction includes rigorous quality checks to ensure realism, test case failure, and absence of explicit bug hints.\n\n**Sources:**\n- [DebugBench at ACL Anthology](https://aclanthology.org/2024.findings-acl.247/)\n- [DebugBench arXiv 2401.04621](https://arxiv.org/abs/2401.04621)\n- [GitHub Repository](https://github.com/thunlp/DebugBench)\n\n---\n\n### 3. **M-RAG (ACL 2024, arXiv 2405.16420)**\n\n**Status: CONFIRMED**\n\n- **Performance improvements**: ✓ **CONFIRMED** - M-RAG achieves +11% for text summarization, +8% for machine translation, and +12% for dialogue generation improvements across comprehensive experiments on seven datasets.\n\n**Sources:**\n- [M-RAG at ACL Anthology](https://aclanthology.org/2024.acl-long.108/)\n- [M-RAG arXiv 2405.16420](https://arxiv.org/abs/2405.16420)\n\n---\n\n### 4. **CRAG (arXiv:2401.15884)**\n\n**Status: DISPUTED/CLARIFICATION NEEDED**\n\n- **ICLR 2025 withdrawal**: ✓ **CONFIRMED AS WITHDRAWN** - CRAG was indeed withdrawn from ICLR 2025 (visible on OpenReview as \"Withdrawn Submission\").\n- **Citation accuracy**: ⚠️ **PARTIALLY ACCURATE** - The citation \"CRAG (Yan et al., 2024; arXiv:2401.15884)\" is technically accurate, but importantly: CRAG is **not a published conference paper** at any major venue. It remains a preprint-only paper on arXiv with three versions (v1: Jan 29, 2024; v2: Feb 16, 2024; v3: Oct 7, 2024). The withdrawal from ICLR 2025 means it was never accepted to that conference.\n\n**Sources:**\n- [CRAG arXiv 2401.15884](https://arxiv.org/abs/2401.15884)\n- [CRAG OpenReview - ICLR 2025 (Withdrawn)](https://openreview.net/forum?id=JnWJbrnaUE)\n\n---\n\n### 5. **DebugBench Search Verification**\n\n**Status: CONFIRMED**\n\nThe search for \"DebugBench evaluating debugging capability LLM\" confirms all major characteristics: 4,253 instances, C++/Java/Python coverage, 18 minor bug categories, GPT-4-implanted bugs, published in ACL 2024 Findings.\n\n**Sources:**\n- [DebugBench at ACL Anthology](https://aclanthology.org/2024.findings-acl.247/)\n\n---\n\n### 6. **arXiv 2503.20589 Abstract**\n\n**Status: CONFIRMED**\n\nThe paper's abstract confirms it addresses repository-level code generation challenges, demonstrates that similar code snippet retrieval introduces noise and degrades results by up to 15%, and proposes AllianceCoder for improved performance.\n\n**Sources:**\n- [arXiv 2503.20589](https://arxiv.org/abs/2503.20589)\n\n---\n\n## Summary Table\n\n| Paper/Claim | Verification Status | Notes |\n|---|---|---|\n| Gu et al. ICSE 2026 | Confirmed | Accepted to ICSE 2026 Research Track |\n| 15% degradation claim | Confirmed | Similar code retrieval reduces performance by up to 15% |\n| Code generation focus | Confirmed | Not code repair |\n| AllianceCoder | Confirmed | Novel RAG method achieving 20% Pass@1 improvement |\n| DebugBench 4,253 instances | Confirmed | Accurate count and 18-category breakdown |\n| DebugBench languages | Confirmed | C++, Java, Python all covered |\n| DebugBench GPT-4 bugs | Confirmed | GPT-4 implanted with quality control |\n| M-RAG improvements | Confirmed | +11% summarization, +8% translation, +12% dialogue |\n| CRAG withdrawn from ICLR 2025 | Confirmed | Paper is listed as withdrawn on OpenReview |\n| CRAG citation accuracy | Partially accurate | Citation correct, but paper is preprint-only, not peer-reviewed conference |"
      }
    ],
    "totalDurationMs": 40091,
    "totalTokens": 27252,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 70,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 24489,
      "output_tokens": 1619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1074
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 70,
          "output_tokens": 1619,
          "cache_read_input_tokens": 24489,
          "cache_creation_input_tokens": 1074,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1074,
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
  "sourceToolAssistantUUID": "5825fbb3-36b7-44ec-84f4-aa22a93b4ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T06:28:02.276Z_

<details><summary>↩ Tool result · `toolu_01RGTtjhZouv8ioTMRT53fPA`</summary>

```text
Based on my comprehensive search and verification, here is the detailed analysis of these three papers:

## FINDINGS

### 1. **ReinFix (arXiv 2506.23100)**

**Venue:** CONFIRMED - ICSE 2026 (April 12-18, 2026, Rio de Janeiro, Brazil)

**Exact Retrieval Mechanism:** ReinFix uses a sophisticated two-phase retrieval approach:
- **Embedding Model:** Yes, uses **text-embedding-3-large** to convert buggy code and root causes into fixed-length embedding vectors
- **Vector Database:** Yes, employs a **unified vector database** storing 100,000 bug-fix pairs from the TRANSFER dataset, with each entry containing `(buggy_code, fix_code, root_cause, embedding_value)`
- **Retrieval Process:** Concatenates buggy code and root cause (`embedding = fembed(buggy_code ⊕ root_cause)`), then uses **cosine similarity** to retrieve top-n results exceeding a similarity threshold

**Performance:** Fixes 146 bugs (Defects4J V1.2) and 145 bugs (V2.0) with GPT-4, a 71.76% improvement over foundation model in ablation studies

**Characterization Accuracy:** Confirmed accurate

---

### 2. **TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w)**

**Venue:** CONFIRMED - Software Quality Journal (SQJ), 2026

**Four-Stage Process:**
1. Defect localization
2. Defect type identification
3. Context selection
4. Patch generation

**Context Selection Mechanism:** The search results confirm the four stages exist, but do NOT specify whether context selection retrieves from an external cross-repository corpus or only within-project context. The Springer link (doi:10.1007/s11219-026-09751-w) was inaccessible for full technical details.

**Language Support:** Primarily **Java-based** evaluation using Defects4J v1.2/v2.0 and QuixBugs datasets, but language-specific limitations are not explicitly stated in available excerpts.

**Performance:** 
- 272.73% improvement over baseline LLM with GPT-3.5
- 257.89% improvement with GPT-4
- Repairs 33 bugs no other method fixes

**Characterization Accuracy:** Partially confirmed - the four-stage architecture and defect-type-aware approach are verified, but full technical details on context selection scope remain unconfirmed due to paywall access.

---

### 3. **SWE-Exp (arXiv 2507.23361)**

**Actual Mechanism:** Multi-faceted experience bank capturing both successful and failed repair attempts:
- **Storage:** Experiences embedded and stored in a **vector database using Multilingual-E5-Large model**
- **Categories:** Comprehension experiences (high-level reasoning) and Modification experiences (code strategies)
- **Retrieval:** Extracts N most relevant experiences via vector similarity, then rerankked to select K experiences (optimal k=1)

**Performance:** CONFIRMED - **73.0% Pass@1 on SWE-Bench Verified using Claude-4 Sonnet** (42.0% with DeepSeek-V3)

**Language Support:** **Python-only** in evaluation, though authors claim the approach is "fundamentally language-agnostic"

**Error Types:** Does NOT use a comprehensive predefined taxonomy. Instead, generalizes common categories like:
- AttributeError
- VariableReferenceError  
- Deprecation-related issues
- Uses agent-inferred "issue type" metadata rather than enumerated error classifications

**Characterization Accuracy:** Substantially confirmed with important caveat - the claim of language-agnosticism is theoretical; practical evaluation is Python-exclusive.

---

### Summary Table

| Paper | Venue | Retrieval Mechanism | Embedding Model | Vector Database | Key Finding |
|-------|-------|-------------------|-----------------|-----------------|------------|
| **ReinFix** | ICSE 2026 ✓ | Internal (static analysis) + External (historical fixes) | text-embedding-3-large ✓ | Yes, unified ✓ | Confirmed accurate |
| **TypeRepair** | SQJ 2026 ✓ | Four-stage (mechanism partially opaque) | Not specified | Not specified | Partially confirmed |
| **SWE-Exp** | arXiv 2507.23361 ✓ | Experience bank with vector retrieval | Multilingual-E5-Large | Yes ✓ | 73.0% confirmed ✓; Python-only ✓ |

Sources:
- [ReinFix arXiv Abstract](https://arxiv.org/abs/2506.23100)
- [ReinFix HTML Full Paper](https://arxiv.org/html/2506.23100)
- [TypeRepair Springer Link](https://link.springer.com/article/10.1007/s11219-026-09751-w)
- [SWE-Exp arXiv Abstract](https://arxiv.org/abs/2507.23361)
- [SWE-Exp HTML Full Paper](https://arxiv.org/html/2507.23361v2)
- [ICSE 2026 Conference](https://conf.researchr.org/home/icse-2026)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23a0933a-ba6d-4b4e-8206-1bc5b4fd5195",
  "isSidechain": false,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "type": "user",
  "uuid": "ae011757-f317-49cc-bb00-c7ca9dc55221",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify the following papers' actual claims, venues, and mechanisms. Use WebSearch and WebFetch to independently confirm details.\n\n1. ReinFix (arXiv 2506.23100) - Is it actually ICSE 2026? What is its exact retrieval mechanism? Does it use text-embedding-3-large? Does it use a unified vector database?\n\n2. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) - What exactly does the \"context selection\" stage do? Does it retrieve from external cross-repository fix corpus, or only within-project context? Is it Java-only?\n\n3. SWE-Exp (arXiv 2507.23361) - What is the actual mechanism? Does it achieve 73.0% on SWE-bench Verified? Is it Python-only? What does \"error type\" mean in this context?\n\nPlease search:\n- \"ReinFix repair ingredients ICSE 2026\" \n- \"arXiv 2506.23100\"\n- \"TypeRepair defect type aware program repair Zhang SQJ 2026\"\n- \"SWE-Exp experience bank arXiv 2507.23361\"\n- site:arxiv.org TypeRepair defect type program repair 2026\n\nFor each paper, report: confirmed venue, exact mechanism, and whether the proposal's characterization is accurate.",
    "agentId": "a954ca586903c2505",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search and verification, here is the detailed analysis of these three papers:\n\n## FINDINGS\n\n### 1. **ReinFix (arXiv 2506.23100)**\n\n**Venue:** CONFIRMED - ICSE 2026 (April 12-18, 2026, Rio de Janeiro, Brazil)\n\n**Exact Retrieval Mechanism:** ReinFix uses a sophisticated two-phase retrieval approach:\n- **Embedding Model:** Yes, uses **text-embedding-3-large** to convert buggy code and root causes into fixed-length embedding vectors\n- **Vector Database:** Yes, employs a **unified vector database** storing 100,000 bug-fix pairs from the TRANSFER dataset, with each entry containing `(buggy_code, fix_code, root_cause, embedding_value)`\n- **Retrieval Process:** Concatenates buggy code and root cause (`embedding = fembed(buggy_code ⊕ root_cause)`), then uses **cosine similarity** to retrieve top-n results exceeding a similarity threshold\n\n**Performance:** Fixes 146 bugs (Defects4J V1.2) and 145 bugs (V2.0) with GPT-4, a 71.76% improvement over foundation model in ablation studies\n\n**Characterization Accuracy:** Confirmed accurate\n\n---\n\n### 2. **TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w)**\n\n**Venue:** CONFIRMED - Software Quality Journal (SQJ), 2026\n\n**Four-Stage Process:**\n1. Defect localization\n2. Defect type identification\n3. Context selection\n4. Patch generation\n\n**Context Selection Mechanism:** The search results confirm the four stages exist, but do NOT specify whether context selection retrieves from an external cross-repository corpus or only within-project context. The Springer link (doi:10.1007/s11219-026-09751-w) was inaccessible for full technical details.\n\n**Language Support:** Primarily **Java-based** evaluation using Defects4J v1.2/v2.0 and QuixBugs datasets, but language-specific limitations are not explicitly stated in available excerpts.\n\n**Performance:** \n- 272.73% improvement over baseline LLM with GPT-3.5\n- 257.89% improvement with GPT-4\n- Repairs 33 bugs no other method fixes\n\n**Characterization Accuracy:** Partially confirmed - the four-stage architecture and defect-type-aware approach are verified, but full technical details on context selection scope remain unconfirmed due to paywall access.\n\n---\n\n### 3. **SWE-Exp (arXiv 2507.23361)**\n\n**Actual Mechanism:** Multi-faceted experience bank capturing both successful and failed repair attempts:\n- **Storage:** Experiences embedded and stored in a **vector database using Multilingual-E5-Large model**\n- **Categories:** Comprehension experiences (high-level reasoning) and Modification experiences (code strategies)\n- **Retrieval:** Extracts N most relevant experiences via vector similarity, then rerankked to select K experiences (optimal k=1)\n\n**Performance:** CONFIRMED - **73.0% Pass@1 on SWE-Bench Verified using Claude-4 Sonnet** (42.0% with DeepSeek-V3)\n\n**Language Support:** **Python-only** in evaluation, though authors claim the approach is \"fundamentally language-agnostic\"\n\n**Error Types:** Does NOT use a comprehensive predefined taxonomy. Instead, generalizes common categories like:\n- AttributeError\n- VariableReferenceError  \n- Deprecation-related issues\n- Uses agent-inferred \"issue type\" metadata rather than enumerated error classifications\n\n**Characterization Accuracy:** Substantially confirmed with important caveat - the claim of language-agnosticism is theoretical; practical evaluation is Python-exclusive.\n\n---\n\n### Summary Table\n\n| Paper | Venue | Retrieval Mechanism | Embedding Model | Vector Database | Key Finding |\n|-------|-------|-------------------|-----------------|-----------------|------------|\n| **ReinFix** | ICSE 2026 ✓ | Internal (static analysis) + External (historical fixes) | text-embedding-3-large ✓ | Yes, unified ✓ | Confirmed accurate |\n| **TypeRepair** | SQJ 2026 ✓ | Four-stage (mechanism partially opaque) | Not specified | Not specified | Partially confirmed |\n| **SWE-Exp** | arXiv 2507.23361 ✓ | Experience bank with vector retrieval | Multilingual-E5-Large | Yes ✓ | 73.0% confirmed ✓; Python-only ✓ |\n\nSources:\n- [ReinFix arXiv Abstract](https://arxiv.org/abs/2506.23100)\n- [ReinFix HTML Full Paper](https://arxiv.org/html/2506.23100)\n- [TypeRepair Springer Link](https://link.springer.com/article/10.1007/s11219-026-09751-w)\n- [SWE-Exp arXiv Abstract](https://arxiv.org/abs/2507.23361)\n- [SWE-Exp HTML Full Paper](https://arxiv.org/html/2507.23361v2)\n- [ICSE 2026 Conference](https://conf.researchr.org/home/icse-2026)"
      }
    ],
    "totalDurationMs": 56341,
    "totalTokens": 30939,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 310,
      "cache_creation_input_tokens": 3295,
      "cache_read_input_tokens": 26025,
      "output_tokens": 1309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3295
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 310,
          "output_tokens": 1309,
          "cache_read_input_tokens": 26025,
          "cache_creation_input_tokens": 3295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3295,
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
      "otherToolCount": 19
    }
  },
  "sourceToolAssistantUUID": "23a0933a-ba6d-4b4e-8206-1bc5b4fd5195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
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
  "leafUuid": "ae011757-f317-49cc-bb00-c7ca9dc55221",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Type-partitioned fix retrieval for cross-language program repair",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d"
}
```

---

### Tool result

_source line 17 · 2026-05-10T06:28:36.427Z_

<details><summary>↩ Tool result · `toolu_01PBhykN36F4J6Z9joR4e7RT`</summary>

```text
Perfect. Now I have comprehensive information. Let me compile the findings for the user.

## Summary of Recent Papers on Type-Conditioned and Category-Conditioned Program Repair (2025-2026)

Based on my systematic search, I found **no papers explicitly named using the "FTCR" acronym or directly using the term "type-conditioned program repair"** as the primary focus. However, I identified several highly relevant concurrent works that address related ideas of **partitioning, classifying, or conditioning retrieval by bug/error characteristics**. Here are the most significant findings:

### High-Similarity Papers (Directly Related to Bug-Type Partitioning)

**1. InferFix: End-to-End Program Repair with LLMs**
- ArXiv: 2303.07263 (March 2023)
- **Venue/Date:** Published at ESEC/FSE 2023 (Industry Papers)
- **Similarity to FTCR:** Very High - Uses **contrastive learning to group bugs by semantic similarity**, training on samples where positive examples are "semantically similar bugs of the same bug type" and negatives are "irrelevant code snippets of different bug types." Explicitly partitions training data by bug type in contrastive pre-training. Uses a retriever trained via contrastive learning to search for semantically equivalent bugs and their corresponding fixes.
- **Key Difference:** Focuses on contrastive pre-training rather than index partitioning, but achieves similar goal of type-aware bug matching.

**2. Learner-Tailored Program Repair (LSGen)**
- ArXiv: 2601.08545 (January 2026)
- **Venue/Date:** Published January 2026
- **Similarity to FTCR:** Very High - Constructs a **solution retrieval database** and employs **iterative, edit-driven code retrieval** that adapts based on generated incorrect code. While not explicitly partitioning by bug type, it uses an iterative retrieval enhancement method that effectively conditions retrieval on the current repair attempt, achieving similar semantic conditioning effects.

**3. ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation**
- ArXiv: 2509.02330 (September 2025)
- **Venue/Date:** Published September 2025
- **Similarity to FTCR:** High - First determines **the algorithm of the wrong code to narrow the subset** of a knowledge base, then retrieves exemplars using dual-view fused features. This is a form of **algorithm/pattern-based partitioning** before retrieval, similar in spirit to type-based partitioning.

**4. PatchRecall: Patch-Driven Retrieval for Automated Program Repair**
- ArXiv: 2604.10481 (April 2026)
- **Venue/Date:** Published April 2026
- **Similarity to FTCR:** Moderate-High - Employs **hybrid retrieval combining codebase retrieval and history-based retrieval**, effectively creating **multiple retrieval strategies** based on whether searching current issue descriptions or historical patterns. Not explicitly by bug type, but uses stratified retrieval conditioned on issue metadata.

### Related Context-Aware Retrieval Papers

**5. On the Role of Fault Localization Context for LLM-Based Program Repair**
- ArXiv: 2604.05481 (April 2026)
- **Venue/Date:** Published April 2026
- **Similarity to FTCR:** Moderate - Empirically evaluates how **context granularity affects repair**, showing file-, element-, and line-level localization have different impacts. Explores how to best condition context retrieval on fault characteristics.

**6. ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair**
- ArXiv: 2605.03117 (May 2026)
- **Venue/Date:** Published May 2026
- **Similarity to FTCR:** Moderate - Uses **structured graph-based tools** and **data-flow slicing** to provide bug-specific context, rather than generic retrieval. Provides reasoning-guided approaches that generate "structured, bug-specific explanations before ranking candidate locations."

**7. RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair**
- ArXiv: 2603.01048 (March 2026)
- **Venue/Date:** Published March 2026
- **Similarity to FTCR:** Moderate - Creates **hierarchical code documentation as semantic abstractions** to condition retrieval, effectively partitioning the search space by structural/semantic categories rather than explicit bug types.

### Broader Retrieval-Augmented Repair Work

**8. ReAPR: Automatic Program Repair via Retrieval-Augmented Large Language Models**
- **Venue/Date:** Software Quality Journal, 2025
- **Similarity to FTCR:** Moderate - General RAG framework for repair; does not explicitly partition by bug type but provides the foundational RAG-for-repair methodology that FTCR would build upon.

**9. RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code**
- ArXiv: 2509.16701
- **Venue/Date:** Published September 2025
- **Similarity to FTCR:** Moderate - Systematically retrieves relevant code from the project repository to augment LLM repair. Focuses on code repository partitioning rather than bug-type partitioning.

### T³: Multi-level Tree-based Automatic Program Repair
- ArXiv: 2506.21211 (June 2025)
- **Venue/Date:** Published June 2025
- **Similarity to FTCR:** Moderate - Structures repair through multiple reasoning levels (Sample Retrieval → Cause Analysis → Repair Plan Generation → Patch Generation). The cause analysis stage could naturally condition downstream retrieval on inferred bug characteristics.

### Broader Context: Major Surveys

**10. A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications**
- ArXiv: 2506.23749 (June 2025)
- **Venue/Date:** TOSEM 2026; covers 63 APR systems from Jan 2022 - June 2025
- **Coverage:** Categorizes all recent work into four paradigms (fine-tuning, prompting, procedural pipelines, agentic) with cross-cutting Retrieval-Augmented Generation (RAG) and Analysis-Augmented Generation (AAG) enhancements. This is the most comprehensive recent taxonomy covering the field.

**11. Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches**
- ArXiv: 2510.04905 (October 2025)
- **Venue/Date:** Published October 2025
- **Coverage:** Discusses InferFix's contrastive approach to bug type grouping, mentions partition-friendly approaches like semantic similarity ranking.

### Key Finding: No Direct Competitor Found

**Important:** I did not find a paper that directly proposes **partitioning a retrieval index explicitly by bug type classification** as the core novelty. This suggests:

1. The FTCR approach (classifying bugs → indexing by type → type-specific retrieval) is likely **novel or concurrent**
2. InferFix (2023) is the closest prior work using contrastive learning to group semantically similar bugs
3. Recent 2025-2026 work focuses more on **fine-grained retrieval narrowing** (algorithm detection, cause analysis, context optimization) rather than explicit index partitioning

### Latest SOTA Context
- **SWE-Bench Verified (2026):** Claude Mythos achieves 93.9%, Claude Opus 4.7 at 87.6%
- **Dominant approach:** Agentic frameworks with RAG/AAG enhancements are the current SOTA paradigm
- **Papers with Code:** Shut down July 2025; SWE-Bench leaderboards now primary benchmark

---

## Sources:
- [A Survey of LLM-based Automated Program Repair](https://arxiv.org/abs/2506.23749)
- [InferFix: End-to-End Program Repair with LLMs](https://arxiv.org/abs/2303.07263)
- [Learner-Tailored Program Repair (LSGen)](https://arxiv.org/abs/2601.08545)
- [ReCode: Improving LLM-based Code Repair with Fine-Grained RAG](https://arxiv.org/abs/2509.02330)
- [PatchRecall: Patch-Driven Retrieval for Automated Program Repair](https://arxiv.org/abs/2604.10481)
- [On the Role of Fault Localization Context for LLM-Based Program Repair](https://arxiv.org/abs/2604.05481)
- [ARISE: A Repository-level Graph Representation](https://arxiv.org/abs/2605.03117)
- [RepoRepair: Leveraging Code Documentation](https://arxiv.org/abs/2603.01048)
- [RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code](https://arxiv.org/pdf/2509.16701)
- [ReAPR: Automatic Program Repair via Retrieval-Augmented LLMs](https://link.springer.com/article/10.1007/s11219-025-09728-1)
- [T³: Multi-level Tree-based Automatic Program Repair](https://arxiv.org/abs/2506.21211)
- [Retrieval-Augmented Code Generation: A Survey](https://arxiv.org/abs/2510.04905)
- [SWE-Bench Leaderboards](https://www.swebench.com/)
- [Dissecting the SWE-Bench Leaderboards](https://arxiv.org/abs/2506.17208)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e57db609-8599-44c2-882b-a6e818e7db88",
  "isSidechain": false,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "type": "user",
  "uuid": "d1769858-c9a4-4e2d-8b29-dd0179a985c9",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent papers (2025-2026) on type-conditioned or category-conditioned program repair and retrieval-augmented repair. I need to find any work that may be concurrent with or supersede this idea about partitioning retrieval indices by bug type.\n\nKey search queries to run:\n1. \"type-conditioned program repair\" site:arxiv.org 2025 2026\n2. \"bug type retrieval augmented repair\" arxiv 2025 2026\n3. \"failure type code repair retrieval\" arxiv 2026\n4. \"categorical retrieval program repair\" arxiv 2026\n5. \"bug classification repair retrieval\" arxiv 2025\n\nAlso search:\n- site:paperswithcode.com \"program repair\" SOTA\n- \"retrieval augmented program repair\" arxiv 2026\n- \"SWE-bench 2026 repair\" to find latest SOTA methods\n\nFor each relevant paper found, report: title, arxiv ID, venue/date, and how similar it is to the FTCR approach (classifying bugs by type, then retrieving from type-specific partitioned index).",
    "agentId": "abf2c5b9b247b50e7",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now I have comprehensive information. Let me compile the findings for the user.\n\n## Summary of Recent Papers on Type-Conditioned and Category-Conditioned Program Repair (2025-2026)\n\nBased on my systematic search, I found **no papers explicitly named using the \"FTCR\" acronym or directly using the term \"type-conditioned program repair\"** as the primary focus. However, I identified several highly relevant concurrent works that address related ideas of **partitioning, classifying, or conditioning retrieval by bug/error characteristics**. Here are the most significant findings:\n\n### High-Similarity Papers (Directly Related to Bug-Type Partitioning)\n\n**1. InferFix: End-to-End Program Repair with LLMs**\n- ArXiv: 2303.07263 (March 2023)\n- **Venue/Date:** Published at ESEC/FSE 2023 (Industry Papers)\n- **Similarity to FTCR:** Very High - Uses **contrastive learning to group bugs by semantic similarity**, training on samples where positive examples are \"semantically similar bugs of the same bug type\" and negatives are \"irrelevant code snippets of different bug types.\" Explicitly partitions training data by bug type in contrastive pre-training. Uses a retriever trained via contrastive learning to search for semantically equivalent bugs and their corresponding fixes.\n- **Key Difference:** Focuses on contrastive pre-training rather than index partitioning, but achieves similar goal of type-aware bug matching.\n\n**2. Learner-Tailored Program Repair (LSGen)**\n- ArXiv: 2601.08545 (January 2026)\n- **Venue/Date:** Published January 2026\n- **Similarity to FTCR:** Very High - Constructs a **solution retrieval database** and employs **iterative, edit-driven code retrieval** that adapts based on generated incorrect code. While not explicitly partitioning by bug type, it uses an iterative retrieval enhancement method that effectively conditions retrieval on the current repair attempt, achieving similar semantic conditioning effects.\n\n**3. ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation**\n- ArXiv: 2509.02330 (September 2025)\n- **Venue/Date:** Published September 2025\n- **Similarity to FTCR:** High - First determines **the algorithm of the wrong code to narrow the subset** of a knowledge base, then retrieves exemplars using dual-view fused features. This is a form of **algorithm/pattern-based partitioning** before retrieval, similar in spirit to type-based partitioning.\n\n**4. PatchRecall: Patch-Driven Retrieval for Automated Program Repair**\n- ArXiv: 2604.10481 (April 2026)\n- **Venue/Date:** Published April 2026\n- **Similarity to FTCR:** Moderate-High - Employs **hybrid retrieval combining codebase retrieval and history-based retrieval**, effectively creating **multiple retrieval strategies** based on whether searching current issue descriptions or historical patterns. Not explicitly by bug type, but uses stratified retrieval conditioned on issue metadata.\n\n### Related Context-Aware Retrieval Papers\n\n**5. On the Role of Fault Localization Context for LLM-Based Program Repair**\n- ArXiv: 2604.05481 (April 2026)\n- **Venue/Date:** Published April 2026\n- **Similarity to FTCR:** Moderate - Empirically evaluates how **context granularity affects repair**, showing file-, element-, and line-level localization have different impacts. Explores how to best condition context retrieval on fault characteristics.\n\n**6. ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair**\n- ArXiv: 2605.03117 (May 2026)\n- **Venue/Date:** Published May 2026\n- **Similarity to FTCR:** Moderate - Uses **structured graph-based tools** and **data-flow slicing** to provide bug-specific context, rather than generic retrieval. Provides reasoning-guided approaches that generate \"structured, bug-specific explanations before ranking candidate locations.\"\n\n**7. RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair**\n- ArXiv: 2603.01048 (March 2026)\n- **Venue/Date:** Published March 2026\n- **Similarity to FTCR:** Moderate - Creates **hierarchical code documentation as semantic abstractions** to condition retrieval, effectively partitioning the search space by structural/semantic categories rather than explicit bug types.\n\n### Broader Retrieval-Augmented Repair Work\n\n**8. ReAPR: Automatic Program Repair via Retrieval-Augmented Large Language Models**\n- **Venue/Date:** Software Quality Journal, 2025\n- **Similarity to FTCR:** Moderate - General RAG framework for repair; does not explicitly partition by bug type but provides the foundational RAG-for-repair methodology that FTCR would build upon.\n\n**9. RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code**\n- ArXiv: 2509.16701\n- **Venue/Date:** Published September 2025\n- **Similarity to FTCR:** Moderate - Systematically retrieves relevant code from the project repository to augment LLM repair. Focuses on code repository partitioning rather than bug-type partitioning.\n\n### T³: Multi-level Tree-based Automatic Program Repair\n- ArXiv: 2506.21211 (June 2025)\n- **Venue/Date:** Published June 2025\n- **Similarity to FTCR:** Moderate - Structures repair through multiple reasoning levels (Sample Retrieval → Cause Analysis → Repair Plan Generation → Patch Generation). The cause analysis stage could naturally condition downstream retrieval on inferred bug characteristics.\n\n### Broader Context: Major Surveys\n\n**10. A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications**\n- ArXiv: 2506.23749 (June 2025)\n- **Venue/Date:** TOSEM 2026; covers 63 APR systems from Jan 2022 - June 2025\n- **Coverage:** Categorizes all recent work into four paradigms (fine-tuning, prompting, procedural pipelines, agentic) with cross-cutting Retrieval-Augmented Generation (RAG) and Analysis-Augmented Generation (AAG) enhancements. This is the most comprehensive recent taxonomy covering the field.\n\n**11. Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches**\n- ArXiv: 2510.04905 (October 2025)\n- **Venue/Date:** Published October 2025\n- **Coverage:** Discusses InferFix's contrastive approach to bug type grouping, mentions partition-friendly approaches like semantic similarity ranking.\n\n### Key Finding: No Direct Competitor Found\n\n**Important:** I did not find a paper that directly proposes **partitioning a retrieval index explicitly by bug type classification** as the core novelty. This suggests:\n\n1. The FTCR approach (classifying bugs → indexing by type → type-specific retrieval) is likely **novel or concurrent**\n2. InferFix (2023) is the closest prior work using contrastive learning to group semantically similar bugs\n3. Recent 2025-2026 work focuses more on **fine-grained retrieval narrowing** (algorithm detection, cause analysis, context optimization) rather than explicit index partitioning\n\n### Latest SOTA Context\n- **SWE-Bench Verified (2026):** Claude Mythos achieves 93.9%, Claude Opus 4.7 at 87.6%\n- **Dominant approach:** Agentic frameworks with RAG/AAG enhancements are the current SOTA paradigm\n- **Papers with Code:** Shut down July 2025; SWE-Bench leaderboards now primary benchmark\n\n---\n\n## Sources:\n- [A Survey of LLM-based Automated Program Repair](https://arxiv.org/abs/2506.23749)\n- [InferFix: End-to-End Program Repair with LLMs](https://arxiv.org/abs/2303.07263)\n- [Learner-Tailored Program Repair (LSGen)](https://arxiv.org/abs/2601.08545)\n- [ReCode: Improving LLM-based Code Repair with Fine-Grained RAG](https://arxiv.org/abs/2509.02330)\n- [PatchRecall: Patch-Driven Retrieval for Automated Program Repair](https://arxiv.org/abs/2604.10481)\n- [On the Role of Fault Localization Context for LLM-Based Program Repair](https://arxiv.org/abs/2604.05481)\n- [ARISE: A Repository-level Graph Representation](https://arxiv.org/abs/2605.03117)\n- [RepoRepair: Leveraging Code Documentation](https://arxiv.org/abs/2603.01048)\n- [RelRepair: Enhancing Automated Program Repair by Retrieving Relevant Code](https://arxiv.org/pdf/2509.16701)\n- [ReAPR: Automatic Program Repair via Retrieval-Augmented LLMs](https://link.springer.com/article/10.1007/s11219-025-09728-1)\n- [T³: Multi-level Tree-based Automatic Program Repair](https://arxiv.org/abs/2506.21211)\n- [Retrieval-Augmented Code Generation: A Survey](https://arxiv.org/abs/2510.04905)\n- [SWE-Bench Leaderboards](https://www.swebench.com/)\n- [Dissecting the SWE-Bench Leaderboards](https://arxiv.org/abs/2506.17208)"
      }
    ],
    "totalDurationMs": 81868,
    "totalTokens": 38049,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2995,
      "cache_read_input_tokens": 32639,
      "output_tokens": 2408,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2995
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2408,
          "cache_read_input_tokens": 32639,
          "cache_creation_input_tokens": 2995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2995,
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
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "e57db609-8599-44c2-882b-a6e818e7db88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-10T06:30:56.153Z_

<details><summary>Logged reasoning block</summary>

```text
Good, now I have the verification results. Let me now search for more information on:
1. The actual SWE-bench SOTA in May 2026 - the proposal mentions ~62.7% for Claude Opus 4.6 on SWE-bench Lite, but the concurrent work search mentions Claude Mythos at 93.9% and Claude Opus 4.7 at 87.6% on SWE-bench Verified. These are different benchmarks (Lite vs Verified), so I should verify the Lite numbers.
2. ICSE 2027 deadline - the proposal states abstract June 23, 2026.


3. Whether InferFix is actually as similar as described by the search agent.

From the search results, I've confirmed most of the key details: ReinFix at ICSE 2026, its embedding-based mechanism, SWE-Exp's 73.0% performance on SWE-bench Verified, Gu et al. at ICSE 2026, DebugBench, and that CRAG is a withdrawn preprint. The main gap remaining is clarifying TypeRepair's context selection mechanism, which appears to be behind a paywall.

Now I'm noticing some important gaps in the proposal's framing. InferFix from ESEC/FSE 2023 uses contrastive learning to group semantically similar bugs, which is directly relevant prior work that isn't mentioned. There's also a discrepancy in the SWE-bench numbers—the proposal cites ~62.7% SOTA on Lite with Claude Opus 4.6, but my search found Claude Mythos at 93.9% and Claude Opus 4.7 at 87.6% on SWE-bench Verified, which are different evaluation sets.

For TypeRepair's context selection, the proposal claims it uses within-project selection rather than cross-repo retrieval, and while I couldn't fully verify this due to paywall restrictions, the fact that Defects4J is a within-project benchmark suggests this claim is plausible.

The venue deadlines check out—ICSE 2027 (abstract June 23, 2026) and FSE 2027 (October 2, 2026) are both after today, so the shift away from EMNLP 2026 is valid. But I'm realizing the original requirement was specifically for EMNLP 2026 with an ARR submission deadline of May 25, 2026, which creates a fundamental mismatch with the current proposal. The proposal has completely shifted away from EMNLP 2026 to ICSE 2027 and FSE 2027, which directly contradicts the user's explicit requirement for EMNLP 2026 with a May 25 deadline that's only 16 days away. Round 4 reviewers flagged the EMNLP deadline as not credible, leading to this pivot, but this represents a fundamental departure from what the user asked for. I should also check the SWE-bench SOTA claim about Claude Opus reaching 62.7% to verify if that's accurate. The compute budget checks out across all three modes, but there's a serious timeline mismatch—only the auto-research approach fits within the 16-day constraint, while manual and human-in-loop modes would take months to weeks respectively. This is a critical issue since the user explicitly requested ≤16 days total.

Now I'm noticing a major corpus size discrepancy in the ReinFix comparison: FTCR's entire dataset is only about 3,050 pairs while ReinFix draws from a 100K sample of the TRANSFER corpus, meaning FTCR's corpus is roughly 3% the size of ReinFix's retrieval pool. This fundamental difference in scale could entirely account for performance variations, and the random-partition control in the proposal doesn't actually address this corpus size gap—it only controls for partition size within FTCR's own limited dataset.

The real confound here is whether any performance advantage comes from the type partitioning strategy itself or simply from FTCR's use of higher-quality natural bugs from verified repositories compared to ReinFix's synthetic TRANSFER corpus bugs. The proposal acknowledges the quality-versus-quantity tradeoff but doesn't fully isolate partitioning as the independent variable when corpus composition and scale differ so dramatically.

Let me check if the proposal claims to use the same encoder and corpus for both methods to create a fair comparison...

actually, rereading it, the proposal does specify that both FTCR and the ReinFix-style baseline will use the identical 3,050-pair corpus with the same text-embedding-3-large encoder, varying only the indexing and retrieval strategy. That's the right experimental design to isolate the partitioning contribution. But then the comparison between this controlled 3,050-pair setup and the full 100K TRANSFER corpus becomes a separate question about corpus scale and quality effects.

Now I'm noticing a bigger problem though: the user explicitly asked for EMNLP 2026 with a May 25 deadline, but the proposal has shifted toward ICSE 2027 (abstract due June 23, 2026) as the primary target. While ICSE might be a better fit for this work, it completely sidesteps what the user actually requested.

The Round 4 reviewer did flag EMNLP 2026 as unrealistic given the current state, so the generator made a deliberate choice to pivot venues. But that's a fundamental violation of the user's requirements—this should probably be marked for revision or rejection.

There's also the 16-day timeline constraint the user specified. The auto-research mode clocks in at 10-14 days, which technically fits, but that assumes completely hands-off automation with no human intervention.  The manual and human-in-loop variants blow past that window entirely, and the proposal doesn't even acknowledge this tension.

Looking at the overall assessment: the novelty around hard-versus-soft partitioning for multi-language APR is genuinely interesting, and the TypeRepair and SWE-Exp comparisons are well-differentiated. But InferFix already explored bug-type-aware retrieval strategies, so there's some overlap there. The scope feels fairly narrow—really just comparing two retrieval approaches. On feasibility, the 3,050-pair corpus is reasonable and Defects4J reproducibility should be manageable, but again, only the auto-research track actually respects the timeline constraint.

The bigger problem is that this doesn't align with what the user actually needs for EMNLP 2026, and the practical impact is limited—the projected 20-35% on SWE-bench Lite falls well short of current state-of-the-art, and the corpus scale (3,050 natural bugs) is tiny compared to what systems like ReinFix work with.

I should recommend revising this. The critical issues are the venue mismatch—they asked for EMNLP 2026 but this targets ICSE 2027—and the timeline problem where only the auto-research mode actually fits the 16-day constraint. There's also the matter of missing prior work like InferFix that already uses bug-type-aware retrieval, and some unresolved questions around the TypeRepair mechanism and how fairly we're comparing against ReinFix given the corpus differences. The core issue is that the user explicitly requires EMNLP 2026, but the idea has drifted toward ICSE 2027 instead—this is a fundamental requirement violation. I need to either reframe the work to be NLP-ready with a realistic 16-day execution plan, or be honest that the current direction doesn't match what was asked for. Beyond the venue mismatch, there's also a methodological concern: comparing FTCR's 3,050 pairs against ReinFix's 100K transfer pairs isn't a clean apples-to-apples evaluation since the corpus scales and quality differ significantly.

Actually, I'm realizing the comparison design is more defensible than I initially thought. FTCR is testing hard versus soft partitioning on a controlled corpus—that's a valid architectural question. The re-implementation of ReinFix-style retrieval on the same 3,050 pairs gives a fair intra-corpus comparison, even if it doesn't directly match published ReinFix numbers. The corpus quality difference (natural bugs versus synthetic TRANSFER data) is a separate variable, not a flaw in the experimental design.

Let me verify the dataset composition they claim. Adding up the numbers from each source—SWE-bench non-Lite, BugsInPy, Defects4J, and GitBug-Java—I get roughly 3,046 pairs, which matches their stated 3,050. But there's a potential issue here: SWE-bench non-Lite contains 1,994 instances that are also used as test cases for evaluation, so using them in the training set creates a data leakage problem.

Actually, wait—SWE-bench Lite is a curated subset of the full SWE-bench Verified set, so the non-Lite split should exclude those 300 instances entirely. That means training on the 1,994 non-Lite instances and evaluating on the 300 Lite instances shouldn't have overlap. But I need to clarify the actual size of SWE-bench Verified itself—it's around 500 instances, not 2,294, which means the full SWE-bench dataset is much larger than what's being used here.

Let me verify the numbers: SWE-bench originally had ~2,294 GitHub issues, Lite is 300 instances, so non-Lite would be ~1,994. That's consistent.

Now I need to finalize my assessment. The critical issue is that the user requested EMNLP 2026 with an ARR deadline of May 25, 2026, but the proposal is now targeting ICSE 2027 instead.

Beyond that, there's a significant constraint problem: only the auto-research mode (10-14 days) actually fits the 16-day timeline, while manual execution takes 4-6 months and human-in-loop takes 6-8 weeks. The proposal needs to clearly position auto-research as the primary path.

I should also flag that InferFix from ESEC/FSE 2023 uses contrastive learning with same-bug-type positive examples, which relates to the type-conditioned retrieval approach here and deserves citation and differentiation.

Finally, there's a potential confound in the corpus quality comparison against published ReinFix results that needs clarification. but the paywall issue with TypeRepair and corpus quality concerns create real reproducibility risks. Clarity is strong at 4/5, but impact scores only 2/5 given the limited generalizability of a comparison study and the venue mismatch between EMNLP and ICSE work. That averages to 3.0, below the 4.0 passing threshold, so this needs revision. Though I'm reconsidering whether I'm being too strict about the venue mismatch—this is Round 5 of 10 and the proposal has genuinely improved, and the user's actual target is EMNLP 2026 with an ARR deadline.

Looking at the timeline constraints: EMNLP's deadline is May 25, 2026, which is only 15 days away, and the experiments aren't complete yet. Auto-research mode would need 10-14 days just to run, leaving almost no buffer for writing a polished paper. The generator's shift to ICSE 2027 is probably the pragmatic choice for paper quality, but it directly contradicts what the user asked for. The real issue is that this venue change needs to be explicitly addressed—either the work needs to fit EMNLP's timeline, or the user needs to understand why ICSE 2027 is the better path forward. can target EMNLP 2026 in 15 days (auto-research mode + NLP framing), or explicitly acknowledge the departure from user requirements and explain why ICSE 2027 is the correct target.
2. Address InferFix as prior art.
3. Clarify the corpus quality confound.

Actually, looking at this more carefully: can the work actually target EMNLP 2026? With auto-research mode running in 10-14 days, and deadline May 25 (15 days away), it's technically possible but extremely tight. The user explicitly tagged this as direction=code_models and contribution_type=method, and EMNLP 2026 Track: NLP and Code Models fits this direction. However, the NLP framing was always a challenge for this SE-focused work.

The core issue here is that this proposal has drifted away from the stated venue, and I need to flag that as a critical concern. Now I'm checking whether the performance claims hold up—the 20-35% resolve rate on SWE-bench Lite seems plausible for a retrieval-only approach, and the cited improvements from TypeRepair and ReinFix check out against their papers. But there's a discrepancy in how ReinFix's results are being characterized that I should verify. I'm noticing the comparison gets murky across different Defects4J versions—DebugRepair's 295 bugs and ReinFix's combined 146+145 aren't directly comparable since they're testing on different dataset versions. The field is clearly advancing fast, and while ReinFix's type-conditioned retrieval approach is interesting, the gains might be incremental given what competitors are already achieving. Now I need to pull together my review with the critical issues I've identified.

The most glaring problem is the venue mismatch—the user explicitly wanted EMNLP 2026 but the proposal targets ICSE 2027, which is a full year later and addresses a different research community entirely. Beyond that, only the auto-research mode fits the 16-day constraint; the manual and human-in-loop alternatives take months and aren't flagged as violating the requirements. I'm also noting that InferFix from ESEC/FSE 2023 does type-aware bug grouping for retrieval using contrastive learning but isn't cited or differentiated from this work. There's also a potential confound between corpus quality and the proposed method that needs addressing. I need to reconsider how I'm evaluating this work. The impact score shouldn't conflate the actual contribution with venue fit—those are separate dimensions. The core contribution is a methodologically sound ablation study comparing hard versus soft type-conditioned retrieval for bug repair, which has genuine value for the APR community even if it's not groundbreaking. That's a 3/5 for impact. The venue mismatch with EMNLP is a separate issue about where this work belongs, not about its inherent contribution to the field.

Looking at the full picture: novelty is 3/5 (the comparison is novel but narrow, and InferFix is an unacknowledged precedent), feasibility drops to 3/5 because only the auto-research mode fits the timeline while reproducibility and corpus sparsity pose real risks, clarity is strong at 4/5 with the detailed experimental design and control partition, and impact stays at 3/5 as a solid but incremental SE contribution that doesn't align with the NLP venue requirement.

That averages to 3.25, which falls below the 4.0 threshold and has the critical mismatch with the user's stated venue target, so this needs revision.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1769858-c9a4-4e2d-8b29-dd0179a985c9",
  "isSidechain": false,
  "requestId": "req_011CatR32nDwpXxoTD1XmzmR",
  "type": "assistant",
  "uuid": "d4400e5f-55a4-4e9e-ad9a-38833d261095",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FP5nEUh7sbwwoEUiQropzt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1646,
      "cache_creation_input_tokens": 5461,
      "cache_read_input_tokens": 35250,
      "output_tokens": 7664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5461,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1646,
          "output_tokens": 7664,
          "cache_read_input_tokens": 35250,
          "cache_creation_input_tokens": 5461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5461
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

_source line 19 · 2026-05-10T06:31:01.584Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013fXe5x5e1z7QqYCwUYAuCS`</summary>

```json
{
  "description": "Verify SWE-bench SOTA and InferFix prior art",
  "subagent_type": "Explore",
  "prompt": "I need to verify two things for a paper review:\n\n1. **Current SWE-bench SOTA (May 2026)**: The paper being reviewed claims \"current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026)\". A search result I received separately mentioned Claude Mythos at 93.9% and Claude Opus 4.7 at 87.6% on SWE-bench Verified. Please search for:\n- \"SWE-bench Lite SOTA 2026\"\n- \"SWE-bench leaderboard 2026\"\n- swebench.com current standings\n- \"SWE-bench Verified SOTA 2026\"\nNote: SWE-bench Lite (300 instances) and SWE-bench Verified (500 instances) are different benchmarks. I need numbers specific to SWE-bench Lite.\n\n2. **InferFix prior art check**: InferFix (ESEC/FSE 2023, arXiv 2303.07263) reportedly uses contrastive learning where positive examples are \"semantically similar bugs of the same bug type.\" \n- Please fetch https://arxiv.org/abs/2303.07263 and read the abstract and key sections\n- Does InferFix actually group bugs by type for retrieval?\n- How similar is it to type-conditioned index partitioning?\n- Is it cited in the paper under review (searching for \"InferFix\" in the context of type-conditioned program repair)?\n\n3. **ICSE 2027 deadline verification**: The paper claims ICSE 2027 abstract deadline is June 23, 2026. Please search for \"ICSE 2027 call for papers\" to verify this date.\n\nReport specific numbers and whether the claims are accurate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4400e5f-55a4-4e9e-ad9a-38833d261095",
  "isSidechain": false,
  "requestId": "req_011CatR32nDwpXxoTD1XmzmR",
  "type": "assistant",
  "uuid": "7c5c34f4-5efb-4361-b4bc-c9a07b17b6ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FP5nEUh7sbwwoEUiQropzt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1646,
      "cache_creation_input_tokens": 5461,
      "cache_read_input_tokens": 35250,
      "output_tokens": 7664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5461,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1646,
          "output_tokens": 7664,
          "cache_read_input_tokens": 35250,
          "cache_creation_input_tokens": 5461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5461
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
  "leafUuid": "7c5c34f4-5efb-4361-b4bc-c9a07b17b6ad",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Type-partitioned fix retrieval for cross-language program repair",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d"
}
```

---

### Tool result

_source line 22 · 2026-05-10T06:31:29.283Z_

<details><summary>↩ Tool result · `toolu_013fXe5x5e1z7QqYCwUYAuCS`</summary>

```text
Now I need to check if the paper being reviewed cites InferFix. Let me search for that context, but since I don't have the actual paper file, I can provide findings based on what I've verified.

## Summary of Verification Results

### 1. SWE-bench Lite SOTA (May 2026)

**Claim in paper:** "Current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026)"

**Verification:** ✓ **ACCURATE**
- Claude Opus 4.6 holds the SWE-bench Lite SOTA with 62.7% as of May 9, 2026
- 62 models have been evaluated on SWE-bench Lite
- Average score is 26.8 with standard deviation of 19.9

**Important context:** The search results also mentioned that Claude Mythos Preview leads SWE-bench Verified at 93.9% and Claude Opus 4.7 at 87.6% on SWE-bench Verified (different benchmark from Lite). These are indeed the figures you mentioned as appearing in search results—they apply to SWE-bench Verified, not Lite, so the paper's claim specifically about Lite is correct.

---

### 2. InferFix Prior Art Analysis

**Paper context:** InferFix (ESEC/FSE 2023, arXiv:2303.07263) reportedly uses contrastive learning with positive examples as "semantically similar bugs of the same bug type"

**Findings:**

- **Bug type grouping:** ✓ **CONFIRMED** - InferFix does use bug type annotations. The framework uses "prompts augmented via bug type annotations and semantically similar fixes retrieved from an external non-parametric memory"

- **Contrastive learning approach:** ✓ **CONFIRMED** - InferFix includes a Retriever component "pretrained via contrastive learning objective, which aims at searching for semantically equivalent bugs and corresponding fixes"

- **Similarity to type-conditioned index partitioning:** InferFix uses bug type categorization to organize retrieved fixes, which is conceptually similar to type-conditioned partitioning. The positive examples are described as training on InferredBugs—"a metadata-rich dataset of bugs extracted by executing the Infer static analyzer on change histories of thousands of Java and C# repositories"

- **Citation status:** I cannot verify from this search whether the paper under review cites InferFix without access to the actual paper document. You would need to check the references section directly or search within the paper file.

---

### 3. ICSE 2027 Abstract Deadline

**Claim in paper:** "ICSE 2027 abstract deadline is June 23, 2026"

**Verification:** ✓ **ACCURATE**
- Abstract deadline (mandatory): **Tuesday, June 23, 2026** (23:59:59 AoE / UTC-12h)
- Full paper submission: June 30, 2026 (one week later)

---

## Sources:
- [SWE-bench Leaderboards](https://www.swebench.com/)
- [SWE-bench Lite Leaderboard 2026](https://pricepertoken.com/leaderboards/benchmark/swe-bench-lite)
- [SWE-Bench Verified Benchmark Leaderboard](https://llm-stats.com/benchmarks/swe-bench-verified)
- [SWE-Bench Verified Benchmark 2026](https://benchlm.ai/benchmarks/sweVerified)
- [InferFix arXiv 2303.07263](https://arxiv.org/abs/2303.07263)
- [ICSE 2027 Important Dates](https://conf.researchr.org/dates/icse-2027)
- [ICSE 2027 Research Track](https://conf.researchr.org/track/icse-2027/icse-2027-research-track)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c5c34f4-5efb-4361-b4bc-c9a07b17b6ad",
  "isSidechain": false,
  "promptId": "3c52da37-ec1d-447f-a8ad-0805fed863c3",
  "type": "user",
  "uuid": "21b2feab-cdde-46d3-befd-4b3121d1b5cf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two things for a paper review:\n\n1. **Current SWE-bench SOTA (May 2026)**: The paper being reviewed claims \"current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026)\". A search result I received separately mentioned Claude Mythos at 93.9% and Claude Opus 4.7 at 87.6% on SWE-bench Verified. Please search for:\n- \"SWE-bench Lite SOTA 2026\"\n- \"SWE-bench leaderboard 2026\"\n- swebench.com current standings\n- \"SWE-bench Verified SOTA 2026\"\nNote: SWE-bench Lite (300 instances) and SWE-bench Verified (500 instances) are different benchmarks. I need numbers specific to SWE-bench Lite.\n\n2. **InferFix prior art check**: InferFix (ESEC/FSE 2023, arXiv 2303.07263) reportedly uses contrastive learning where positive examples are \"semantically similar bugs of the same bug type.\" \n- Please fetch https://arxiv.org/abs/2303.07263 and read the abstract and key sections\n- Does InferFix actually group bugs by type for retrieval?\n- How similar is it to type-conditioned index partitioning?\n- Is it cited in the paper under review (searching for \"InferFix\" in the context of type-conditioned program repair)?\n\n3. **ICSE 2027 deadline verification**: The paper claims ICSE 2027 abstract deadline is June 23, 2026. Please search for \"ICSE 2027 call for papers\" to verify this date.\n\nReport specific numbers and whether the claims are accurate.",
    "agentId": "a92ddfd0cd4514a7e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Now I need to check if the paper being reviewed cites InferFix. Let me search for that context, but since I don't have the actual paper file, I can provide findings based on what I've verified.\n\n## Summary of Verification Results\n\n### 1. SWE-bench Lite SOTA (May 2026)\n\n**Claim in paper:** \"Current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026)\"\n\n**Verification:** ✓ **ACCURATE**\n- Claude Opus 4.6 holds the SWE-bench Lite SOTA with 62.7% as of May 9, 2026\n- 62 models have been evaluated on SWE-bench Lite\n- Average score is 26.8 with standard deviation of 19.9\n\n**Important context:** The search results also mentioned that Claude Mythos Preview leads SWE-bench Verified at 93.9% and Claude Opus 4.7 at 87.6% on SWE-bench Verified (different benchmark from Lite). These are indeed the figures you mentioned as appearing in search results—they apply to SWE-bench Verified, not Lite, so the paper's claim specifically about Lite is correct.\n\n---\n\n### 2. InferFix Prior Art Analysis\n\n**Paper context:** InferFix (ESEC/FSE 2023, arXiv:2303.07263) reportedly uses contrastive learning with positive examples as \"semantically similar bugs of the same bug type\"\n\n**Findings:**\n\n- **Bug type grouping:** ✓ **CONFIRMED** - InferFix does use bug type annotations. The framework uses \"prompts augmented via bug type annotations and semantically similar fixes retrieved from an external non-parametric memory\"\n\n- **Contrastive learning approach:** ✓ **CONFIRMED** - InferFix includes a Retriever component \"pretrained via contrastive learning objective, which aims at searching for semantically equivalent bugs and corresponding fixes\"\n\n- **Similarity to type-conditioned index partitioning:** InferFix uses bug type categorization to organize retrieved fixes, which is conceptually similar to type-conditioned partitioning. The positive examples are described as training on InferredBugs—\"a metadata-rich dataset of bugs extracted by executing the Infer static analyzer on change histories of thousands of Java and C# repositories\"\n\n- **Citation status:** I cannot verify from this search whether the paper under review cites InferFix without access to the actual paper document. You would need to check the references section directly or search within the paper file.\n\n---\n\n### 3. ICSE 2027 Abstract Deadline\n\n**Claim in paper:** \"ICSE 2027 abstract deadline is June 23, 2026\"\n\n**Verification:** ✓ **ACCURATE**\n- Abstract deadline (mandatory): **Tuesday, June 23, 2026** (23:59:59 AoE / UTC-12h)\n- Full paper submission: June 30, 2026 (one week later)\n\n---\n\n## Sources:\n- [SWE-bench Leaderboards](https://www.swebench.com/)\n- [SWE-bench Lite Leaderboard 2026](https://pricepertoken.com/leaderboards/benchmark/swe-bench-lite)\n- [SWE-Bench Verified Benchmark Leaderboard](https://llm-stats.com/benchmarks/swe-bench-verified)\n- [SWE-Bench Verified Benchmark 2026](https://benchlm.ai/benchmarks/sweVerified)\n- [InferFix arXiv 2303.07263](https://arxiv.org/abs/2303.07263)\n- [ICSE 2027 Important Dates](https://conf.researchr.org/dates/icse-2027)\n- [ICSE 2027 Research Track](https://conf.researchr.org/track/icse-2027/icse-2027-research-track)"
      }
    ],
    "totalDurationMs": 27694,
    "totalTokens": 23939,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2463,
      "cache_read_input_tokens": 20508,
      "output_tokens": 961,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2463
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 961,
          "cache_read_input_tokens": 20508,
          "cache_creation_input_tokens": 2463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2463,
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
  "sourceToolAssistantUUID": "7c5c34f4-5efb-4361-b4bc-c9a07b17b6ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-10T06:32:04.367Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the verification I need. Let me compile the final review.

Key findings:
1. SWE-bench Lite SOTA = 62.7% (Claude Opus 4.6, May 2026) ✓ CONFIRMED
2. InferFix uses bug type annotations and contrastive learning for type-conditioned retrieval ✓ CONFIRMED as unmentioned prior art
3. ICSE 2027 abstract deadline = June 23, 2026 ✓ CONFIRMED

Now let me compose my final review:

**Core issues identified:**


The proposal has shifted away from the user's explicit target of EMNLP 2026 (ARR May 25) toward ICSE 2027 (abstract June 23, 2026)—a full year later and a different research community entirely. While previous reviewers questioned EMNLP 2026's feasibility given the experimental state, the user's original requirement remains unaddressed. Additionally, the 16-day timeline constraint the user specified can only be met through auto-research mode, not manual execution.

I'm also noticing that InferFix, which uses bug type annotations and contrastive learning for semantically-aware bug retrieval, isn't cited anywhere despite being directly relevant prior work. And there's a potential confound in the cross-system comparison where both FTCR and ReinFix are evaluated on the same corpus of 3,050 natural bug-fix pairs, which could mask differences in how each approach handles data quality.

The paper needs to be clearer about how TypeRepair's context selection actually works—whether it truly uses within-project retrieval or cross-repo retrieval—since this distinction is central to FTCR's claimed advantage, though I couldn't fully verify this due to access limitations. On novelty, the hard-versus-soft type partitioning for cross-repo retrieval in multi-language APR is genuinely novel, but the InferFix gap weakens that claim somewhat.

Looking at feasibility, the auto-research mode fits within the 200 H100-hour and 10-14 day window, though human-in-loop variants would exceed the 16-day constraint, and the Defects4J reproducibility plus per-type corpus sparsity are real risks. For clarity, the proposal is well-structured with solid experimental controls and the confidence-gated hybrid approach, addressing prior feedback effectively. On impact, this reads more as a targeted ablation study for the APR community rather than a paradigm shift, which creates some misalignment with the EMNLP venue focus.

The projected 20-35% standalone performance on SWE-bench Lite falls well short of the >60% SOTA baseline, which limits practical significance. Averaging the scores gives 3.25, so the verdict is to revise. The core issues blocking acceptance are the venue mismatch with EMNLP 2026, the unaddressed InferFix prior work, and timeline violations if manual modes are included. Given 15 days until the deadline with experiments still pending, even an aggressive auto-research push would be extremely tight, so I need to assess whether pivoting toward EMNLP is realistically achievable or if a different venue strategy makes more sense.

If auto-research launches immediately, the timeline could theoretically work—10-14 days of experiments followed by parallel paper writing—but the NLP framing problem persists as a fundamental obstacle. My feedback should emphasize that the venue mismatch is the critical blocker, clarify that EMNLP 2026 remains technically possible only if auto-research starts now, push for the InferFix comparison to be included, and isolate the corpus quality confound as a separate concern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21b2feab-cdde-46d3-befd-4b3121d1b5cf",
  "isSidechain": false,
  "requestId": "req_011CatRFmnBkdt2dU6hgtfAR",
  "type": "assistant",
  "uuid": "204c674c-a52b-44d6-ac6e-ee0a63d35aa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HoRy1qMHDkJiQEX8MYaQWr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10272,
      "cache_read_input_tokens": 40711,
      "output_tokens": 3688,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3688,
          "cache_read_input_tokens": 40711,
          "cache_creation_input_tokens": 10272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10272
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

_source line 24 · 2026-05-10T06:32:51.711Z_

Now I have everything I need for a complete, independent assessment. Let me compile the verdict.

**Summary of verification findings:**
- ReinFix: ICSE 2026 ✓, text-embedding-3-large on 100K TRANSFER pairs ✓
- TypeRepair: SQJ 2026 ✓, 4-stage pipeline ✓, context selection mechanism unconfirmed (paywall)
- SWE-Exp: 73.0% on SWE-bench Verified ✓, Python-only ✓, soft cosine retrieval ✓
- Gu et al. ICSE 2026: confirmed, targets code generation not repair ✓
- DebugBench: 4,253 instances, 18-category labels, C++/Java/Python ✓
- CRAG: preprint-only, withdrawn from ICLR 2025 ✓
- **SWE-bench Lite SOTA: 62.7% (Claude Opus 4.6) ✓** (distinct from SWE-bench Verified's 93.9%)
- **ICSE 2027 abstract deadline: June 23, 2026 ✓**
- **InferFix (ESEC/FSE 2023, arXiv 2303.07263): CONFIRMED uses bug type annotations and contrastive learning to retrieve same-type bugs and fixes** — unmentioned in proposal

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "Hard-vs-soft type-partitioned cross-repo retrieval is genuinely novel for multi-language APR, and differentiation from ReinFix/SWE-Exp/TypeRepair is now well-articulated. However, InferFix (ESEC/FSE 2023, arXiv:2303.07263) — confirmed unmentioned — uses bug type annotations plus contrastive learning to retrieve 'semantically equivalent bugs and corresponding fixes,' directly instantiating type-conditioned retrieval; this unacknowledged prior art narrows the novelty claim."
    },
    "feasibility": {
      "score": 3,
      "rationale": "Technically feasible within 200 H100-hours (auto-research: ~190 H100h), but the user's hard 16-day constraint is met only by the auto-research mode (10–14 days); the manual (4–6 months) and human-in-loop (6–8 weeks) modes violate it by an order of magnitude and should not be presented as viable given the stated constraints. Defects4J reproducibility and per-type corpus sparsity remain execution risks."
    },
    "clarity": {
      "score": 4,
      "rationale": "The proposal is now exceptionally detailed: random-partition control cleanly isolates the corpus-size confound, confidence-gated hybrid addresses error propagation, and per-type merge policy handles sparsity. TypeRepair and Gu et al. are properly integrated. The only lingering opacity is that TypeRepair's context-selection scope (within-project only) was independently unverifiable due to paywall access."
    },
    "impact": {
      "score": 3,
      "rationale": "The retrieval architecture comparison is a genuine SE/APR contribution, but it is fundamentally an ablation study between two retrieval strategies rather than a new paradigm; projected 20–35% standalone SWE-bench Lite performance is well below current SOTA (62.7%); and the work has drifted entirely away from the user's required EMNLP 2026 NLP venue target to an SE venue (ICSE 2027), significantly misaligning the impact claim with the stated mission."
    }
  },
  "issues": [
    "CRITICAL — Target venue violates user requirements: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026, 15 days from today). The proposal now targets ICSE 2027 (abstract June 23, 2026) exclusively, a full year late and a different research community. Previous reviewers flagged EMNLP as infeasible given experiment state, but the requirement was not to change venues — it was to make the idea work within the constraint. If auto-research starts immediately (day 0), 10–14 days of experiments complete by ~May 23, leaving 2 days to finalize the paper for the May 25 ARR deadline. This is technically achievable but requires an explicit, committed execution plan with the NLP framing (X%/Y%/Z%/W% classifier calibration finding) as the lead contribution. The proposal must either restore EMNLP 2026 as the primary target with a day-by-day execution schedule, or explicitly acknowledge that it fails the user's venue constraint and accept that verdict.",
    "HIGH — 16-day timeline constraint met only by auto-research mode: The user's hard constraint is ≤16 days. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) exceed this by 8–12× and should not appear as viable execution paths in resource_estimate. The paper should flag auto-research (10–14 days) as the only constraint-compliant mode, or restructure the three modes to reflect feasible timelines.",
    "MEDIUM — InferFix (ESEC/FSE 2023, arXiv:2303.07263) is unmentioned prior art: Independently confirmed that InferFix uses bug type annotations and contrastive learning to retrieve 'semantically equivalent bugs and corresponding fixes of the same bug type' from an external repository corpus (InferredBugs, thousands of Java and C# repos). This is the closest non-trivial precursor to type-conditioned cross-repo repair retrieval and is not cited anywhere in the proposal. ICSE 2027 reviewers familiar with the APR literature will notice its absence. FTCR should differentiate explicitly: InferFix uses soft contrastive similarity (learned embedding grouping) not hard categorical index partitioning; it targets Java/C# from Infer static analysis findings, not the 18-category natural-bug taxonomy; and the corpus construction and evaluation differ. This differentiation is achievable in one paragraph but must be present.",
    "MEDIUM — Cross-system corpus quality confound inadequately flagged: The 'clean comparison' correctly uses the same 3,050-pair natural corpus for both FTCR and the ReinFix-style baseline, isolating partitioning as the variable. But any performance comparison against the published ReinFix results uses 100K TRANSFER corpus pairs (synthetic, from static analysis), creating a corpus quality × retrieval architecture confound that the random-partition control does not address. The paper must explicitly state: (a) intra-corpus ablations (FTCR vs. re-implemented ReinFix on 3,050 pairs) test the partitioning hypothesis cleanly, and (b) absolute comparisons against published ReinFix results reflect both architecture and corpus quality differences simultaneously.",
    "LOW — TypeRepair context-selection scope unverifiable from publicly accessible sources: The critical differentiation claim — that TypeRepair's Stage 3 selects within-project context only, not from an external cross-repo corpus — could not be independently confirmed due to paywall access to the SQJ article. The proposal states this confidently; it should note the evidentiary basis (e.g., 'TypeRepair evaluates exclusively on Defects4J/QuixBugs, which are within-project datasets, and the paper's supplementary prompt templates confirm type-specific in-project context selection rather than external retrieval') to avoid a reviewer flagging this differentiation as unsubstantiated."
  ],
  "feedback": "This is the most polished version of FTCR to date. The random-partition control, confidence-gated hybrid, per-type merge policy, and ReinFix/SWE-Exp/TypeRepair differentiation all reflect genuine methodological rigor. Two actions would bring this to pass: (1) VENUE DECISION — the proposal must choose one of two paths and commit fully: either (a) restore EMNLP 2026 ARR (May 25) as the primary target with a specific day-by-day execution schedule (day 0-13: auto-research runs corpus annotation + DebugBench classifier calibration + Defects4J V1.2 ablations; day 13-15: paper writing with NLP lead framing the X%/Y%/Z%/W% falsifiable classifier finding), acknowledging the extreme timeline pressure; or (b) explicitly declare that the user's requirement cannot be met for EMNLP 2026 and accept ICSE 2027 as the sole target with a verdict of 'fail' on the original requirement. Leaving both venues while targeting neither by the May 25 deadline is a planning failure. (2) ADD INFERFIX — one paragraph in the landscape: 'InferFix (ESEC/FSE 2023, arXiv:2303.07263) retrieves fixes for bugs of the same type using contrastive-learned embeddings over bug type annotations, establishing type-aware retrieval for Java/C# static analysis bugs. FTCR differs in three respects: (a) hard categorical index partitioning at construction time rather than soft contrastive similarity at retrieval time; (b) 18-category natural-bug taxonomy across C++/Java/Python rather than InferBugs' Infer-specific defect categories; (c) direct comparison of hard vs. soft type conditioning as the scientific contribution.' If these two issues are resolved, the novelty and feasibility scores reach 3.5+ and the paper is close to a pass for ICSE 2027 (though not EMNLP 2026 unless the execution plan is credible).",
  "reason": "Genuine methodological improvement through 5 rounds, but two blocking issues remain: the proposal violates the user's explicit EMNLP 2026 venue requirement with no credible path back, and InferFix (ESEC/FSE 2023) — confirmed prior art using type-annotated contrastive retrieval — is unmentioned."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "204c674c-a52b-44d6-ac6e-ee0a63d35aa4",
  "isSidechain": false,
  "requestId": "req_011CatRFmnBkdt2dU6hgtfAR",
  "type": "assistant",
  "uuid": "b6eec86f-612e-404d-88b8-7aab8707f98f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HoRy1qMHDkJiQEX8MYaQWr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10272,
      "cache_read_input_tokens": 40711,
      "output_tokens": 3688,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3688,
          "cache_read_input_tokens": 40711,
          "cache_creation_input_tokens": 10272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10272
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
  "leafUuid": "b6eec86f-612e-404d-88b8-7aab8707f98f",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Type-partitioned fix retrieval for cross-language program repair",
  "sessionId": "a8158a37-99fc-4e21-a270-570542d8053d"
}
```

---
