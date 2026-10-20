# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/818c6f04-ca23-4de4-b570-59c5989a81dd.jsonl`
- **Structured JSON:** [`b422a20f249d6884df53.json`](../../sessions/b4/b422a20f249d6884df53.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T06:25:06.475Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T06:25:06.475Z",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 6/10)\n{\n  \"title\": \"SeMutFL: Contrastive Mutation Augmentation for Surface-Form Robust Code Understanding in Fault Localization\",\n  \"core_problem\": \"Code-understanding LLMs exhibit shallow, surface-dependent representations: semantic-preserving mutations — program transformations that preserve behavior while changing syntax (variable renaming, loop reformulation, branch reordering) — cause models to change their fault localization predictions dramatically. The ICST 2026 study (arXiv 2504.04372, 750,013 tasks, 1,300+ programs, 10 LLMs) finds a 78% failure rate under such mutations. A concurrent study (arXiv 2505.10443) confirms performance drops of up to 70% across nine LLMs on LiveCodeBench and CruxEval under five mutation types. This is an NLP robustness phenomenon analogous to instruction-phrasing brittleness in text: models that correctly solve a task on one surface form fail on semantically equivalent but differently written code. The strongest current fault localization method, RGFL (arXiv 2601.18044), uses hierarchical reasoning to improve file-level Hit@1 from 71.4% to 85% on SWE-bench Verified, but is a retrieval-and-reasoning pipeline improvement — it does not modify training to enforce semantic invariance, and its representations would be expected to exhibit the same surface-form brittleness. No published method treats surface-form robustness in fault localization as a training objective.\",\n  \"opportunity\": \"EMNLP 2026's special theme 'New Missions for NLP Research' explicitly calls for contributions on trustworthiness, robustness, and longitudinal behavior of LLMs — making surface-form invariance in code understanding a directly on-theme submission under the 'NLP and Code Models' track. The gap is specific and well-documented: two independent diagnostic studies quantify the brittleness, RGFL establishes that reasoning-level improvements alone do not address it, and no training method enforcing semantic invariance for fault localization exists. Contrastive learning over semantically equivalent code pairs is a well-established NLP technique (ContraCode, EMNLP 2021), but has never been applied to fault localization fine-tuning in an LLM setting. arXiv 2604.05481 demonstrates that accurate file-level localization causally improves downstream repair success, motivating why robust localization — maintaining accuracy across the surface-form variation natural to real-world diverse codebases — matters for practical automated repair. Semantic-preserving mutation operators are fully automated and well-understood, making large-scale training data synthesis tractable within a 200 H100-hour compute ceiling using Qwen2.5-Coder-32B.\",\n  \"landscape\": \"RGFL (arXiv 2601.18044, January 2026) is the strongest current baseline, improving file-level Hit@1 from 71.4% to 85% on SWE-bench Verified via hierarchical reasoning with structured bug-specific explanations and two-stage LLM-plus-embedding ranking. RGFL directly competes on localization quality but addresses reasoning process rather than representation robustness — no training objective for surface-form invariance — and would be expected to remain brittle under semantic-preserving mutations. SpIDER (arXiv 2512.16956, December 2025) improves file localization with graph-aware dense retrieval on SWE-bench Lite; no robustness training. SWE-Fixer (ACL Findings 2025) fine-tunes a dedicated bug retriever without a robustness objective. ContraCode (EMNLP 2021) establishes the contrastive learning paradigm for semantic-invariant code embeddings but targets general pre-training embeddings, not the fault localization step in a repair pipeline. MACL-IRFL (Automated Software Engineering 2026) uses multi-view adaptive contrastive learning for information-retrieval fault localization but does not address LLM fine-tuning brittleness. arXiv 2602.11411 (February 2026, 'Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data') is the closest methodological predecessor: it fine-tunes code LLMs with perturbed training data to improve robustness. However, it is differentiated from SeMutFL on three axes: (a) perturbation type — 2602.11411 applies NLP-level perturbations to natural language prompts (character-level typos, word-level synonym substitution, sentence-level back-translation), whereas SeMutFL applies semantic-preserving program transformations (variable renaming, dead-code insertion, statement reordering) directly to code, targeting the code-structure brittleness documented in arXiv 2504.04372 and arXiv 2505.10443; (b) training objective — 2602.11411 uses standard supervised fine-tuning with augmented data and no contrastive loss, while SeMutFL adds an InfoNCE consistency loss that explicitly enforces invariance between (original, mutant) program pairs sharing the same fault location; and (c) task — 2602.11411 addresses code generation (HumanEval, MBPP) on small models (1B–7B parameters), while SeMutFL addresses fault localization on a 32B instruction-tuned LLM with fault-location labels and fault-negative pair sampling. arXiv 2504.04372 (ICST 2026) and arXiv 2505.10443 (May 2026) are both purely diagnostic, explicitly motivating training-level solutions without providing one. SeMutFL's unique position: the only method that (a) treats surface-form brittleness in fault localization as a first-class training objective, (b) applies InfoNCE contrastive consistency loss — rather than plain augmented SFT — to LLM fine-tuning for localization, enforcing semantic invariance over fault-negative pairs, and (c) empirically validates whether robustness gains translate to downstream repair outcomes — closing the diagnostic-to-improvement loop that both studies leave open.\",\n  \"approach\": \"SeMutFL augments fault localization fine-tuning data with five semantics-preserving mutation operators (variable renaming, dead-code insertion, statement reordering, loop normalization, alias introduction) applied to SWE-bench Verified and Defects4J, synthesizing (original, mutant) pairs sharing identical ground-truth fault locations.\\n\\nAll five operators are validated for semantic preservation using test-suite equivalence checking: a mutated program enters the training corpus only if it passes the same test suite as its original. On Defects4J — where ground-truth test suites are curated specifically to catch behavioral changes — this check is authoritative; on SWE-bench Verified, issue-linked test suites provide a complementary signal. Pairs failing equivalence checking are discarded. Inclusion rates differ substantially by operator and must be understood in a stratified way: variable renaming and alias introduction satisfy the equivalence check by construction and target ~100% inclusion (renaming introduces no new data or control dependencies); dead-code insertion is similarly safe by construction (unreachable statements cannot affect any test outcome). Statement reordering and loop normalization are restricted to provably dependency-free statement blocks identified via lightweight static dependency analysis on the AST (program-dependence-graph extraction), and are expected to achieve lower, program-dependent inclusion rates — conservative dependency analysis will filter any block with live variable dependencies, which may represent a substantial fraction of candidate blocks in heavily interdependent code. These lower-inclusion-rate operators are supplementary: any reduction in their coverage does not affect the soundness of the InfoNCE objective or the training signal from the three high-inclusion-rate operators (variable renaming, alias introduction, dead-code insertion), which constitute the reliable core of the mutation augmentation and will generate the majority of training pairs regardless of dataset composition. This stratified design directly addresses the 59% implementation failure rate for published semantic-preserving transformations documented in arXiv 2503.23448, by making training corpus soundness structurally independent of the complex operators.\\n\\nWe fine-tune Qwen2.5-Coder-32B-Instruct (strong, well-documented open model for code fine-tuning; fits 2×A100-80GB with QLoRA; chosen over 72B-scale models to satisfy the 200 H100-hour compute constraint) using a dual objective: standard cross-entropy localization loss plus an InfoNCE contrastive consistency loss that pulls representations of (original, mutant) views of the same fault together while pushing them apart from different-fault negatives. The InfoNCE objective uses an InfoNCE pairwise contrastive formulation — inspired by ContraCode's augmentation paradigm and consistent with the contrastive approach in MACL-IRFL, but applied to fault localization fine-tuning rather than general embedding pre-training or graph-based IR — with in-batch different-fault programs as hard negatives, a design suited to the QLoRA fine-tuning setting.\\n\\nEvaluation plan:\\n1. Primary — localization robustness: Hit@1 and MRR on a held-out mutation test set mirroring the ICST 2026 protocol, directly measuring brittleness reduction versus an untuned Qwen2.5-Coder-32B-Instruct baseline.\\n2. Comparison against RGFL: Evaluate SeMutFL and RGFL on both clean SWE-bench Verified (where RGFL reports 85% Hit@1) and on the mutation-perturbed test set. If faithful RGFL reimplementation within the 12-day execution window proves infeasible — likely given RGFL's complex hierarchical retrieval pipeline — we will use RGFL's published numbers (85% Hit@1 from arXiv 2601.18044) as the clean-code reference point and restrict the primary robustness comparison to SeMutFL vs. untuned Qwen2.5-Coder-32B-Instruct on the mutation-perturbed test set. This is the more defensible framing in any case, as it directly measures the training-robustness contribution rather than reimplementation fidelity.\\n3. Downstream repair validation: Empirically test whether improved localization robustness translates to better SWE-bench Verified repair success — directly validating, not assuming, the causal chain from arXiv 2604.05481. The 15-17x improvement cited in prior work comes from ground-truth localization versus no localization; we report the incremental gain from robustness over the untuned baseline, with no overclaim of replicating that gap.\\n\\nAblation schedule (4 runs, within 200 H100-hour budget):\\n- Full SeMutFL (all 5 operators + InfoNCE loss)\\n- Mutation augmentation only (no contrastive loss, plain SFT) — isolates the contribution of the InfoNCE objective\\n- Variable-renaming-only operator set (most common mutation type in practice; isolates operator breadth contribution)\\n- Untuned Qwen2.5-Coder-32B-Instruct baseline\\n\\nThe 'InfoNCE contrastive loss only (no augmented mutants)' condition is excluded: it is ill-posed because InfoNCE requires positive program pairs, and without augmented mutants there are no program-level positives to form the contrastive objective. The augmentation-only SFT condition already cleanly isolates the contribution of the contrastive loss. Reducing from five to four ablation conditions also ensures the worst-case budget (4 × 2 × 33h training + 70h evaluation + 8h data/validation = ~342 A100-hours ≈ 171 H100-hours at ±50% training time variance) remains genuinely under the 200 H100-hour ceiling.\\n\\nDifferentiation from RGFL: RGFL improves reasoning quality via structured explanations applied at inference time; SeMutFL improves representation-level robustness via training-time invariance enforcement. These are orthogonal: RGFL is not expected to be robust to mutations (no training change), while SeMutFL directly targets this gap.\\nDifferentiation from arXiv 2602.11411: That work improves generation robustness via NLP-level prompt perturbations and plain SFT augmentation; SeMutFL addresses code-structure brittleness in fault localization via semantic-preserving code mutations and InfoNCE contrastive invariance.\\nDifferentiation from arXiv 2505.10443: That work measures brittleness across 9 models; SeMutFL trains robustness in and empirically connects the fix to downstream repair, going from diagnostic to prescriptive.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~245h A100-80GB (Qwen2.5-Coder-32B QLoRA, 2×A100 per run, ~22h each; 4 ablations + evaluation)\",\n      \"gpu_utilization\": \"~35-45% effective\",\n      \"timeline\": \"4-6 months — INFEASIBLE: misses EMNLP 2026 ARR deadline of May 25, 2026\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$245-370 at ~$1.50/hr spot A100\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~176h A100-80GB (Qwen2.5-Coder-32B QLoRA, 2×A100 per run, ~22h each; 4 ablations + evaluation)\",\n      \"gpu_utilization\": \"~65-75% effective\",\n      \"timeline\": \"6-10 weeks — INFEASIBLE: misses EMNLP 2026 ARR deadline of May 25, 2026\",\n      \"team\": \"1 researcher, ~30 min/day for approving ablation configs and reviewing results\",\n      \"claude_api_cost\": \"$150-300 (~1,000-2,000 turns)\",\n      \"estimated_gpu_cost\": \"~$264-396 at ~$1.50/hr spot A100\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~254 A100-80GB hours total (~127 H100-equivalent hours at 2x speedup), well within the 200 H100-hour budget. Breakdown: training — 4 ablation runs × 2×A100 × ~22h = 176 A100-hours; SWE-bench evaluation — ~35h × 2×A100 = 70 A100-hours; mutation data generation + test-suite equivalence validation — ~8 A100-hours; total = ~254 A100-hours ≈ 127 H100-equivalent hours. Worst-case (+50% training time variance): 4 × 2 × 33h = 264 A100-hours training + 70 evaluation + 8 data/validation = ~342 A100-hours ≈ 171 H100-equivalent hours — genuinely under the 200 H100-hour ceiling even at worst-case variance. The ~22h/run estimate is derived from first principles, with SWE-Gym (arXiv 2412.21139) confirming the scale: 491 trajectories × 18,578 avg tokens (Table 8) × 5 epochs = 45.5M total training tokens for 32B LoRA fine-tuning at max context length 32,768 on 2-8 NVIDIA H100 80G GPUs. No published benchmark directly reports QLoRA timing for 30B+ models on 2×A100-80GB; the 22h/run estimate relies entirely on the following first-principles throughput calculation, with ±50% variance as the correct risk mitigation. SeMutFL's training corpus is approximately 1.5× larger than SWE-Gym's OpenHands experiment: ~4,500 fault localization pairs (SWE-bench Verified ~500 instances + Defects4J ~395 bugs, each yielding 4–5 valid mutation pairs on average after equivalence checking) × ~5,120 average tokens per example (fault localization inputs include issue description, repository file hierarchy, and candidate file content) × 3 training epochs ≈ 69M total training tokens. Throughput on 2×A100-80GB with QLoRA is estimated at 680–910 tokens/sec: 2 × 312 TFLOPS BF16 peak × 35–45% practical MFU × 0.70 for QLoRA quantization/dequantization overhead (Dettmers et al., NeurIPS 2023) = 130–175 effective TFLOPS; for a 32B model (6N = 192 GFLOP per training token), this yields 680–910 tokens/sec. This range is cross-validated against first-principles H100 scaling: H100 at 989 TFLOPS × 40% MFU = 396 TFLOPS → ~2,060 tokens/sec for 32B LoRA; applying the 2×A100-80GB/H100 compute ratio (~0.63) and QLoRA throughput penalty (0.70) gives ~910 tokens/sec at the optimistic end. At ~800 tokens/sec central estimate, 69M tokens ≈ 86,250 seconds ≈ 24h; the stated 22h rounds this to account for gradient checkpointing and activation offloading optimizations typical in QLoRA implementations, which improve effective throughput 5–15% over the baseline MFU estimate. The ±50% variance range (11–33h) bounds real-world uncertainty in batch scheduling, dataset composition, and hardware utilization variability, and remains the correct risk mitigation regardless of the base estimate's precision.\",\n      \"gpu_utilization\": \"~90% effective; agent chains mutation data synthesis, test-suite equivalence validation, QLoRA training, checkpoint evaluation, and SWE-bench scoring with near-zero idle\",\n      \"timeline\": \"7-12 days with 2 concurrent A100 pairs (4 GPUs total); with 4 ablations and 2 parallel pairs, training completes in 2 batches (~44h wall-clock GPU time per batch at 22h/run) for ~88h training + setup and evaluation — fits within the 16-day window to the May 25 ARR deadline\",\n      \"team\": \"0 (initial environment setup and mutation operator scaffolding only, ~3-4h one-time)\",\n      \"claude_api_cost\": \"$300-600 (~2,500-4,000 turns for mutation pipeline code generation, experiment orchestration, result parsing, and draft report generation)\",\n      \"estimated_gpu_cost\": \"~$381-572 at ~$1.50/hr spot A100 (254 A100-hours central × $1.50 ≈ $381 with ~50% buffer for worst-case re-runs)\",\n      \"speed_bottleneck\": \"Sequential dependency between QLoRA fine-tuning and downstream SWE-bench repair evaluation; each 32B QLoRA run uses 2×A100-80GB for ~22h (estimated; see gpu_hours note above for grounding). With 4 concurrent A100s, 2 runs execute in parallel, completing 4 ablations in 2 serial batches of ~44h wall-clock each.\",\n      \"risk_note\": \"Primary risk: InfoNCE temperature and mutation sampling rate may cause embedding collapse (silent loss decrease without localization improvement); automated per-epoch embedding variance monitoring and collapse detection must be wired into the agent loop before launch. Secondary risk: RGFL comparison requires either faithful reimplementation or careful scope qualification; explicit fallback is to use published RGFL numbers (85% Hit@1 on clean SWE-bench Verified) as clean-code reference and restrict robustness comparison to SeMutFL vs. untuned Qwen2.5-Coder-32B-Instruct baseline only. Tertiary risk: test-suite equivalence validation on SWE-bench Verified may reject more pairs than on Defects4J if SWE-bench test suites are less comprehensive; this would reduce training set size but is bounded by Defects4J as the primary training source and does not affect the soundness of the InfoNCE objective.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Main (ARR submission deadline May 25, 2026; 'NLP and Code Models' track; directly addresses the 2026 special theme on trustworthiness and robustness of LLMs)\",\n    \"EMNLP 2026 Findings (as fallback if main conference spots are exhausted)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (ICST 2026, arXiv 2504.04372)\",\n    \"Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations? (arXiv 2505.10443, May 2026)\",\n    \"Reasoning Guided Fault Localization for LLM-Based Automated Program Repair (RGFL, arXiv 2601.18044, January 2026)\",\n    \"On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481, 2026)\",\n    \"Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data (arXiv 2602.11411, February 2026)\",\n    \"Spatially Informed Dense Embedding Retrieval for Software Issue Localization (SpIDER, arXiv 2512.16956, December 2025)\",\n    \"SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution (ACL Findings 2025)\",\n    \"Contrastive Code Representation Learning (ContraCode, EMNLP 2021)\",\n    \"Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization (MACL-IRFL, Automated Software Engineering 2026)\",\n    \"Are Semantic-Preserving Transformations Reusable? Limitations of Published Semantic-Preserving Transformations for Code Models (arXiv 2503.23448, March 2025)\",\n    \"Qwen2.5-Coder Technical Report (arXiv 2409.12186)\",\n    \"SWE-smith: Scaling Data for Software Engineering Agents (arXiv 2504.21798, NeurIPS 2025)\",\n    \"Training Software Engineering Agents and Verifiers with SWE-Gym (arXiv 2412.21139)\",\n    \"QLoRA: Efficient Finetuning of Quantized LLMs (Dettmers et al., NeurIPS 2023)\"\n  ],\n  \"description\": \"LLMs trained for code exhibit surface-form brittleness: semantic-preserving mutations (variable renaming, loop reformulation, branch reordering) cause fault localization models to change their predictions in 78% of previously correct cases (ICST 2026), with concurrent evidence of up to 70% performance drops across nine leading models (arXiv 2505.10443). This is an NLP robustness problem — shallow pattern matching rather than semantic grounding — directly analogous to instruction-phrasing sensitivity in text. While RGFL (arXiv 2601.18044) achieves 85% file-level Hit@1 on SWE-bench Verified via improved reasoning, it does not modify training and would be expected to remain brittle under surface-form variation. arXiv 2602.11411 (February 2026) improves code LLM robustness via perturbed SFT, but applies NLP-level prompt perturbations (typos, synonyms, back-translation) to code generation tasks without a contrastive objective, leaving fault-localization brittleness under semantic-preserving code transformations unaddressed. SeMutFL addresses this gap by augmenting fine-tuning data with (original, mutant) program pairs sharing identical ground-truth fault locations, generated by five automated semantics-preserving mutation operators applied to SWE-bench Verified and Defects4J. Operator inclusion rates are stratified by construction-safety: variable renaming, alias introduction, and dead-code insertion target ~100% inclusion (safe by construction), while statement reordering and loop normalization achieve lower, program-dependent inclusion rates due to conservative AST dependency analysis — the three high-inclusion operators form the reliable training core, making corpus soundness structurally independent of the complex operators and directly addressing the 59% implementation failure rate documented in arXiv 2503.23448. Fine-tuning Qwen2.5-Coder-32B-Instruct with QLoRA under a dual cross-entropy plus InfoNCE contrastive consistency objective — using different-fault programs as hard negatives — enforces semantic invariance directly in the model's representations. Evaluation measures localization robustness on a held-out mutation test set mirroring the ICST 2026 protocol, comparison against RGFL on both clean and mutated code (with explicit fallback to published RGFL numbers if reimplementation is infeasible within the execution window), and empirical validation of whether robustness gains translate to downstream SWE-bench Verified repair success. The ~22h/run training time estimate is derived from first principles, with SWE-Gym (arXiv 2412.21139) confirming the scale: 491 trajectories × 18,578 avg tokens (Table 8) × 5 epochs = 45.5M training tokens for 32B LoRA on H100 hardware. No published benchmark directly reports QLoRA timing for 30B+ models on 2×A100-80GB; the estimate relies entirely on first-principles throughput: SeMutFL's ~4,500 training pairs × ~5,120 avg tokens × 3 epochs ≈ 69M tokens at ~800 tokens/sec (2 × 312 TFLOPS × 40% MFU × 0.70 QLoRA overhead, Dettmers et al. NeurIPS 2023) ≈ 24h, with ±50% variance bounding real-world uncertainty. The ablation design uses four conditions (Full SeMutFL, augmentation-only SFT, variable-renaming-only, untuned baseline) with worst-case budget of ~342 A100-hours ≈ 171 H100-hours — genuinely under the 200 H100-hour ceiling even at worst-case variance. The method requires no manual annotation, uses only publicly available datasets, and targets EMNLP 2026's explicit theme of LLM trustworthiness and robustness.\",\n  \"project_name\": \"semutfl_robust_fault_loc\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — VENUE MISMATCH: The user required EMNLP 2026 (ARR deadline May 25, 2026), but target_venues lists ICSE 2027, AAAI 2027, and ICLR 2027. The idea must be redesigned around the correct venue.\", \"CRITICAL — TIMELINE VIOLATION: Manual mode requires 4–6 months, HIL 6–10 weeks — both impossible in 16 days. Only auto research (5–14 days) is plausible, but violates the compute ceiling.\", \"CRITICAL — COMPUTE BUDGET VIOLATION: Auto research mode requires 900–1,400 A100-hours (≈450–700 H100-equivalent), 2.5–3.5× over the 200 H100-hour hard constraint. A version using Qwen2.5-Coder-32B (2×A100 per run, ~20–25h each) with ≤5 ablations would cost ≈100–130 H100-hours and fit the budget.\", \"OUTDATED BASE MODEL CLAIM: Kimi-Dev-72B is no longer open-source SOTA on SWE-bench Verified as of May 2026; GLM-4.7, Kimi K2 Thinking, Qwen3-Coder-Next, and DeepSeek v3.2 have superseded it. The experiment must be updated to reflect the current landscape or explicitly justify the model choice.\", \"UNACKNOWLEDGED COMPETITOR — RGFL (arXiv 2601.18044, January 2026): This paper improves file-level Hit@1 from 71.4% to 85% on SWE-bench Verified using hierarchical reasoning with structured explanations. It is the strongest current FL baseline and directly competes with SeMutFL's localization improvement claim — ignoring it will draw immediate rejection from reviewers.\", \"INDIRECT CONNECTION BETWEEN BRITTLENESS AND 15–17X REPAIR IMPROVEMENT: arXiv 2604.05481 shows the 15–17x gain comes from accurate file-level context quality (ground-truth localization vs none), not from reducing the 78% brittleness under mutations. SeMutFL must demonstrate empirically that reducing mutation-induced localization failures also improves downstream repair rates, not assume the causal link.\", \"EMNLP TRACK FIT RISK: Fault localization as a concept is strongly SE-scoped. For EMNLP NLP and Code Models reviewers, the framing must foreground LLM robustness to surface-form variation in code understanding (an NLP phenomenon), not mutation testing methodology (an SE concept). The current framing reads as an SE paper submitted to an NLP venue.\"]\nFeedback: The research core — training fault localization robustness via semantic-mutation augmentation — is genuinely novel and well-motivated by the two verified empirical studies. The idea is worth revising rather than abandoning. To meet user requirements, the generator must make four concrete changes:\n\n1. **Fix the venue**: Set target_venues to ['EMNLP 2026 Main', 'EMNLP 2026 Findings'] with ARR deadline May 25, 2026. Remove ICSE/AAAI/ICLR 2027 entirely.\n\n2. **Scale to fit 200 H100-hours in 16 days**: Replace Kimi-Dev-72B with Qwen2.5-Coder-32B-Instruct or DeepSeek-Coder-V2-16B as the fine-tuning base. At 32B, each QLoRA run uses 2×A100-80GB × ~20h = 40 A100-hours ≈ 20 H100-hours. Five ablations + evaluation = ≈130 H100-hours total — within budget. The 72B model is infeasible under both the compute ceiling and the 16-day clock.\n\n3. **Acknowledge and compare against RGFL (arXiv 2601.18044)**: This paper achieves 85% file-level Hit@1 on SWE-bench Verified and is the correct stronger baseline. SeMutFL must demonstrate improvement over RGFL or explicitly show that mutation robustness is complementary to reasoning-guided localization.\n\n4. **Reframe for NLP audience**: Lead with 'LLM code understanding is brittle under surface-form variation' (NLP robustness framing), not 'fault localization fails under mutation testing' (SE framing). Emphasize semantic grounding of code representations as the NLP contribution. The EMNLP NLP and Code Models track is receptive to this framing if the language is right.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — UNACKNOWLEDGED COMPETITOR arXiv 2602.11411: 'Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data' (Feb 2026) uses the same methodological core — fine-tuning code LLMs with semantically-perturbed code (variable renaming, dead-code insertion, statement reordering) + contrastive loss — to improve robustness. The task domain differs (code generation/summarization vs. fault localization), but any EMNLP reviewer familiar with this paper will flag the overlap. SeMutFL must cite this work and explicitly argue that (a) the FL task formulation is fundamentally different from generation robustness, (b) the training signal (fault location labels vs. functional correctness) creates a distinct objective, and (c) the InfoNCE formulation with fault-negative sampling is not subsumed by this prior work. Failure to do so is a near-certain rejection trigger.\", \"COMPUTE INCONSISTENCY: The itemized breakdown (5 runs × 2 A100s × 22h = 220 A100-hours for training; + 35h × 2 A100s = 70 A100-hours for SWE-bench evaluation; + 5 A100-hours for mutation synthesis = 295 total A100-hours) is inconsistent with the header claim of '220-260 A100-80GB hours total.' The correct total is approximately 295 A100-hours ≈ 148 H100-hours at 2x conversion, which is within the 200 H100-hour budget — but the stated numbers must be made internally consistent to survive reviewer scrutiny.\", \"RGFL COMPARISON RISK IS UNDER-MITIGATED: The evaluation plan compares SeMutFL against RGFL on both clean and mutation-perturbed SWE-bench Verified, but RGFL is a complex hierarchical reasoning pipeline. Within 7-12 days of auto_research execution, a faithful reimplementation is unlikely. The risk note acknowledges this but does not provide a fallback strategy. The proposal should explicitly state: (a) if RGFL reimplementation is infeasible, reported RGFL numbers from arXiv 2601.18044 will be used as reference with explicit scope qualification, or (b) only clean-code comparison against published RGFL numbers will be made, with mutation robustness evaluated only against the untuned Qwen2.5-Coder-32B-Instruct baseline.\", \"22H/RUN TRAINING TIME ESTIMATE IS UNCITED: The ~22h per QLoRA run for Qwen2.5-Coder-32B on 2×A100-80GB is plausible but unverified in the literature. This estimate should be grounded in a cited pilot run, a comparable training report (e.g., Qwen2.5-Coder-32B fine-tuning documentation from Alibaba), or explicitly marked as an estimate with ±50% variance acknowledged in the budget.\", \"MACL-IRFL ADAPTATION CLAIM IS SLIGHTLY OVERSTATED: The proposal says it 'adapts MACL-IRFL's multi-view contrastive framework to the LLM QLoRA fine-tuning setting,' but MACL-IRFL uses three-way graph-based views (bug-code interaction, bug similarity, code co-citation), while SeMutFL uses simple pairwise (original, mutant) pairs — structurally closer to ContraCode's augmentation strategy. This claim should be softened to avoid reviewer confusion about what exactly is being adapted.\"]\nFeedback: Round 1 critical fixes (venue, model scale, RGFL acknowledgment, causal chain correction, NLP framing) are all solid and substantially improve the proposal. The research core remains genuinely novel and well-motivated. To reach 'pass,' make four targeted fixes:\n\n1. **Acknowledge arXiv 2602.11411 in the landscape section.** Add it as a direct methodological predecessor: 'arXiv 2602.11411 (Feb 2026) fine-tunes code LLMs with perturbed data (including variable renaming and dead-code insertion) and a contrastive loss to improve robustness on code generation and summarization tasks. SeMutFL is differentiated by (a) fault localization as the task — requiring models to identify which file/function contains a bug, not to generate semantically equivalent code, (b) fault-location labels as the contrastive negative signal (different-fault programs, not different-program programs), and (c) evaluation on mutation-perturbed SWE-bench Verified specifically for localization accuracy under surface-form variation.' This differentiation is real and defensible — it just needs to be stated.\n\n2. **Fix the compute breakdown.** The correct total is ~295 A100-hours ≈ 148 H100-equivalent hours. Update the header to '~295 A100-80GB hours total (~148 H100-equivalent hours at 2x speedup), within the 200 H100-hour budget.' Make all sub-totals consistent.\n\n3. **Add a concrete RGFL comparison fallback.** State explicitly: 'If RGFL reimplementation within the 12-day execution window proves infeasible, we will use RGFL's published numbers (85% Hit@1 on clean SWE-bench Verified from arXiv 2601.18044) as the clean-code reference point and restrict the primary robustness comparison to SeMutFL vs. untuned Qwen2.5-Coder-32B-Instruct on the mutation-perturbed test set.' This doesn't weaken the contribution — it sets honest expectations.\n\n4. **Soften the MACL-IRFL adaptation claim.** Change 'adapting MACL-IRFL's multi-view contrastive framework' to 'using an InfoNCE pairwise contrastive objective, inspired by ContraCode's augmentation paradigm and consistent with the contrastive approach in MACL-IRFL, but applied to fault localization fine-tuning.' This is more accurate and avoids misleading reviewers about what is novel.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MODERATE — MUTATION VALIDITY GAP (arXiv 2503.23448): An independent March 2025 study tested 39 semantic-preserving transformations from the published literature and found 23/39 (59%) change code semantics when actually implemented. SeMutFL proposes five mutation operators (variable renaming, dead-code insertion, statement reordering, loop normalization, alias introduction) but provides no validation that these are genuinely semantics-preserving in practice. Statement reordering in particular is high-risk — if statements have data dependencies, reordering changes behavior. Without explicit validation (e.g., test-suite equivalence checking on Defects4J, where ground-truth test suites are available), the training corpus may contain pairs where 'mutant' versions have different fault locations from what the label says, directly corrupting the InfoNCE objective. This must be addressed before submission.\", \"MODERATE — BUDGET ARITHMETIC UNDER VARIANCE: The proposal acknowledges ±50% training time variance for the 22h/run estimate, but the budget arithmetic is inconsistent under this variance. Worst case: 5 ablations × 2 A100s × 33h = 330 A100-hours (training) + 70 (SWE-bench) + 5 (mutation) = 405 A100-hours = 202.5 H100-hours — exceeding the 200 H100-hour hard constraint. The stated '30% headroom for re-runs' is a separate buffer from training time variance headroom; the proposal implicitly conflates them as if one covers both. Reducing from 5 to 4 ablations (dropping the 'InfoNCE only, no augmented mutants' condition, which is confounded and hard to interpret without pairs) would bring worst-case training to 4 × 2 × 33h = 264 A100-hours = 132 H100-hours + 37.5 = 169.5 H100-hours — genuinely under budget even at worst-case variance.\", \"MINOR — TRAINING TIME ESTIMATE STILL UNCITED: The ~22h/run estimate for Qwen2.5-Coder-32B QLoRA on 2×A100-80GB could not be verified against any published community benchmark or Alibaba technical documentation. No comparable 30B-class QLoRA training time reports were found. The acknowledgment of ±50% variance partially addresses this, but a concrete citation (e.g., Qwen2.5-Coder technical report arXiv 2409.12186 Appendix, or a referenced pilot run) would strengthen the feasibility claim under reviewer scrutiny.\"]\nFeedback: Round 2 critical issues are all resolved — the proposal is structurally sound and the core novelty is confirmed by independent search. To reach 'pass' in Round 4, make two targeted fixes:\n\n1. **Add mutation validation protocol (addresses the 2503.23448 risk)**: In the approach section, add: 'All five mutation operators are validated for semantic preservation using test-suite equivalence checking on Defects4J: a mutated program is included in training only if it passes the same test suite as the original. Pairs failing this check are discarded, targeting a validation rate ≥95% per operator.' Variable renaming and alias introduction should pass easily; dead-code insertion is safe by construction; statement reordering and loop normalization should be restricted to provably dependency-free cases (detected via lightweight static analysis on the AST). This directly addresses the known implementation failure rate found in arXiv 2503.23448 and strengthens experimental integrity.\n\n2. **Tighten ablation set from 5 to 4 conditions**: Remove the 'InfoNCE contrastive loss only (no augmented mutants)' condition — this is ill-posed because InfoNCE requires positive pairs, and without augmented mutants there are no program-level positives. Replace it implicitly with the existing 'mutation augmentation only (no contrastive loss)' condition, which already cleanly isolates the contribution of the loss. The remaining four conditions (Full SeMutFL, augmentation-only SFT, variable-renaming-only, untuned baseline) are maximally informative. This reduces worst-case training from 202.5 to 169.5 H100-hours — genuinely under budget even at ±50% variance, resolving the arithmetic inconsistency cleanly.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MINOR — TRAINING TIME ESTIMATE STILL INSUFFICIENTLY GROUNDED: The ~22h/run estimate for Qwen2.5-Coder-32B QLoRA on 2×A100-80GB cites (a) the Qwen2.5-Coder technical report as confirming A100-80GB hardware class (not training time) and (b) SWE-smith as showing full-parameter fine-tuning is feasible 'within single-digit-day timescales' — which is a substantially weaker grounding than a specific QLoRA timing benchmark. The Alibaba Cloud Qwen2.5-Coder fine-tuning tutorial (alibabacloud.com/help/en/pai/use-cases/training-evaluation-compression-and-deployment-of-qwen2-5-coder-model) and the Hugging Face Qwen2.5-Coder-32B-Instruct discussion thread contain specific hardware-time data that directly supports or refutes the 22h estimate. The ±50% variance buffer is the correct risk mitigation, but the underlying estimate should be anchored to a concrete source to survive reviewer feasibility scrutiny.\", \"MINOR — ≥95% INCLUSION RATE TARGET IS UNSTRATIFIED: The proposal states a single ≥95% inclusion rate target for all five operators, but operator risk varies dramatically: variable renaming and alias introduction are safe by construction and will approach 100%, dead-code insertion is similarly safe, while statement reordering and loop normalization depend on conservative dependency analysis that may filter a large fraction of candidate statement blocks. Stating a uniform 95% target obscures that the effective training data from reordering/loop normalization operators may be substantially smaller. The proposal should acknowledge that per-operator inclusion rates will differ and that a smaller-than-expected contribution from complex operators does not invalidate the InfoNCE objective — it just reduces operator diversity for those categories. This is a framing fix, not a scientific problem.\"]\nFeedback: Round 3's three issues (mutation validity, budget arithmetic, ablation count) are all correctly resolved. The proposal is scientifically sound and the remaining issues are minor framing and grounding problems. Two targeted fixes bring this to pass:\n\n1. **Anchor the 22h/run estimate to a direct source**: Fetch the Alibaba Cloud Qwen2.5-Coder fine-tuning tutorial or cite the Hugging Face Qwen2.5-Coder-32B-Instruct hardware discussion thread for a specific QLoRA training time on 2×A100-80GB. If no direct source is available, replace the citation with: 'The 22h/run estimate is derived from first-principles: [sequence length] × [dataset size] × [QLoRA optimizer steps] at measured [tokens/sec] throughput on A100-80GB (citing any community QLoRA benchmark for a comparable 30B-class model).' The ±50% variance already provides adequate safety margin — the fix is about the base estimate's citation.\n\n2. **Stratify the inclusion rate claim by operator risk**: Change '≥95% inclusion rate per operator' to 'Variable renaming and alias introduction satisfy the equivalence check by construction (targeting ~100% inclusion); dead-code insertion is safe by construction; statement reordering and loop normalization are restricted to dependency-free blocks and are expected to achieve lower inclusion rates depending on program structure — but these are supplementary operators and any reduction in their coverage does not affect the soundness of the InfoNCE objective or the training signal from the remaining three operators.' This makes the claim defensible rather than aspirational.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MINOR — SWE-GYM ANCHOR CONTAINS VERIFIABLE FACTUAL INACCURACIES: The resource estimate describes SWE-Gym (arXiv 2412.21139) as using 'context length 10,240 tokens, on a single H100 GPU' for the 32B LoRA training anchoring the 22h/run estimate. Independent verification finds: (a) SWE-Gym's OpenHands training (the 491-trajectory experiment the proposal cites) specifies max context length 32,768 — not 10,240 — and uses 2-8 NVIDIA H100 80G GPUs, not a single H100; (b) the single-H100 setup applies to SWE-Gym's MoatlessTools 32B LoRA verifier experiment, which used only 62-172 trajectories, not 491. The token statistics (491 trajectories × 18,578 avg tokens, Table 8) are correctly cited. The ±50% variance buffer preserves the budget regardless, but a reviewer checking this reference will find the context length and hardware attribution wrong, which undermines credibility of the feasibility claim at a critical juncture of reviewer scrutiny.\"]\nFeedback: Round 4's two targeted issues are both correctly resolved: inclusion rate stratification is now properly differentiated by operator construction-safety, and the first-principles throughput calculation is substantially more detailed. One description fix remains:\n\n**Correct the SWE-Gym anchor.** The resource estimate claims SWE-Gym uses 'context length 10,240 tokens, on a single H100 GPU' for the 491-trajectory 32B LoRA training, but the paper specifies max context length 32,768 for that run (OpenHands training on 2-8 H100s). The correct framing is: 'SWE-Gym (arXiv 2412.21139) confirms the scale: 491 successful trajectories × 18,578 avg tokens (Table 8) × 5 epochs = 45.5M total training tokens for 32B LoRA fine-tuning on H100 hardware.' Do not specify context length (it is not 10,240) or imply a single-H100 setup for that run. Rely entirely on the first-principles throughput calculation for the 22h estimate, and explicitly note that no published benchmark directly reports QLoRA timing for 30B+ models on 2×A100-80GB — the ±50% variance is the correct risk mitigation. This is a description fix only; the token count, throughput calculation, and budget arithmetic are all correct as stated.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T06:25:06.480Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T06:25:06.480Z",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-10T06:25:06.506Z_

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
  "title": "SeMutFL: Contrastive Mutation Augmentation for Surface-Form Robust Code Understanding in Fault Localization",
  "core_problem": "Code-understanding LLMs exhibit shallow, surface-dependent representations: semantic-preserving mutations — program transformations that preserve behavior while changing syntax (variable renaming, loop reformulation, branch reordering) — cause models to change their fault localization predictions dramatically. The ICST 2026 study (arXiv 2504.04372, 750,013 tasks, 1,300+ programs, 10 LLMs) finds a 78% failure rate under such mutations. A concurrent study (arXiv 2505.10443) confirms performance drops of up to 70% across nine LLMs on LiveCodeBench and CruxEval under five mutation types. This is an NLP robustness phenomenon analogous to instruction-phrasing brittleness in text: models that correctly solve a task on one surface form fail on semantically equivalent but differently written code. The strongest current fault localization method, RGFL (arXiv 2601.18044), uses hierarchical reasoning to improve file-level Hit@1 from 71.4% to 85% on SWE-bench Verified, but is a retrieval-and-reasoning pipeline improvement — it does not modify training to enforce semantic invariance, and its representations would be expected to exhibit the same surface-form brittleness. No published method treats surface-form robustness in fault localization as a training objective.",
  "opportunity": "EMNLP 2026's special theme 'New Missions for NLP Research' explicitly calls for contributions on trustworthiness, robustness, and longitudinal behavior of LLMs — making surface-form invariance in code understanding a directly on-theme submission under the 'NLP and Code Models' track. The gap is specific and well-documented: two independent diagnostic studies quantify the brittleness, RGFL establishes that reasoning-level improvements alone do not address it, and no training method enforcing semantic invariance for fault localization exists. Contrastive learning over semantically equivalent code pairs is a well-established NLP technique (ContraCode, EMNLP 2021), but has never been applied to fault localization fine-tuning in an LLM setting. arXiv 2604.05481 demonstrates that accurate file-level localization causally improves downstream repair success, motivating why robust localization — maintaining accuracy across the surface-form variation natural to real-world diverse codebases — matters for practical automated repair. Semantic-preserving mutation operators are fully automated and well-understood, making large-scale training data synthesis tractable within a 200 H100-hour compute ceiling using Qwen2.5-Coder-32B.",
  "landscape": "RGFL (arXiv 2601.18044, January 2026) is the strongest current baseline, improving file-level Hit@1 from 71.4% to 85% on SWE-bench Verified via hierarchical reasoning with structured bug-specific explanations and two-stage LLM-plus-embedding ranking. RGFL directly competes on localization quality but addresses reasoning process rather than representation robustness — no training objective for surface-form invariance — and would be expected to remain brittle under semantic-preserving mutations. SpIDER (arXiv 2512.16956, December 2025) improves file localization with graph-aware dense retrieval on SWE-bench Lite; no robustness training. SWE-Fixer (ACL Findings 2025) fine-tunes a dedicated bug retriever without a robustness objective. ContraCode (EMNLP 2021) establishes the contrastive learning paradigm for semantic-invariant code embeddings but targets general pre-training embeddings, not the fault localization step in a repair pipeline. MACL-IRFL (Automated Software Engineering 2026) uses multi-view adaptive contrastive learning for information-retrieval fault localization but does not address LLM fine-tuning brittleness. arXiv 2602.11411 (February 2026, 'Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data') is the closest methodological predecessor: it fine-tunes code LLMs with perturbed training data to improve robustness. However, it is differentiated from SeMutFL on three axes: (a) perturbation type — 2602.11411 applies NLP-level perturbations to natural language prompts (character-level typos, word-level synonym substitution, sentence-level back-translation), whereas SeMutFL applies semantic-preserving program transformations (variable renaming, dead-code insertion, statement reordering) directly to code, targeting the code-structure brittleness documented in arXiv 2504.04372 and arXiv 2505.10443; (b) training objective — 2602.11411 uses standard supervised fine-tuning with augmented data and no contrastive loss, while SeMutFL adds an InfoNCE consistency loss that explicitly enforces invariance between (original, mutant) program pairs sharing the same fault location; and (c) task — 2602.11411 addresses code generation (HumanEval, MBPP) on small models (1B–7B parameters), while SeMutFL addresses fault localization on a 32B instruction-tuned LLM with fault-location labels and fault-negative pair sampling. arXiv 2504.04372 (ICST 2026) and arXiv 2505.10443 (May 2026) are both purely diagnostic, explicitly motivating training-level solutions without providing one. SeMutFL's unique position: the only method that (a) treats surface-form brittleness in fault localization as a first-class training objective, (b) applies InfoNCE contrastive consistency loss — rather than plain augmented SFT — to LLM fine-tuning for localization, enforcing semantic invariance over fault-negative pairs, and (c) empirically validates whether robustness gains translate to downstream repair outcomes — closing the diagnostic-to-improvement loop that both studies leave open.",
  "approach": "SeMutFL augments fault localization fine-tuning data with five semantics-preserving mutation operators (variable renaming, dead-code insertion, statement reordering, loop normalization, alias introduction) applied to SWE-bench Verified and Defects4J, synthesizing (original, mutant) pairs sharing identical ground-truth fault locations.\n\nAll five operators are validated for semantic preservation using test-suite equivalence checking: a mutated program enters the training corpus only if it passes the same test suite as its original. On Defects4J — where ground-truth test suites are curated specifically to catch behavioral changes — this check is authoritative; on SWE-bench Verified, issue-linked test suites provide a complementary signal. Pairs failing equivalence checking are discarded. Inclusion rates differ substantially by operator and must be understood in a stratified way: variable renaming and alias introduction satisfy the equivalence check by construction and target ~100% inclusion (renaming introduces no new data or control dependencies); dead-code insertion is similarly safe by construction (unreachable statements cannot affect any test outcome). Statement reordering and loop normalization are restricted to provably dependency-free statement blocks identified via lightweight static dependency analysis on the AST (program-dependence-graph extraction), and are expected to achieve lower, program-dependent inclusion rates — conservative dependency analysis will filter any block with live variable dependencies, which may represent a substantial fraction of candidate blocks in heavily interdependent code. These lower-inclusion-rate operators are supplementary: any reduction in their coverage does not affect the soundness of the InfoNCE objective or the training signal from the three high-inclusion-rate operators (variable renaming, alias introduction, dead-code insertion), which constitute the reliable core of the mutation augmentation and will generate the majority of training pairs regardless of dataset composition. This stratified design directly addresses the 59% implementation failure rate for published semantic-preserving transformations documented in arXiv 2503.23448, by making training corpus soundness structurally independent of the complex operators.\n\nWe fine-tune Qwen2.5-Coder-32B-Instruct (strong, well-documented open model for code fine-tuning; fits 2×A100-80GB with QLoRA; chosen over 72B-scale models to satisfy the 200 H100-hour compute constraint) using a dual objective: standard cross-entropy localization loss plus an InfoNCE contrastive consistency loss that pulls representations of (original, mutant) views of the same fault together while pushing them apart from different-fault negatives. The InfoNCE objective uses an InfoNCE pairwise contrastive formulation — inspired by ContraCode's augmentation paradigm and consistent with the contrastive approach in MACL-IRFL, but applied to fault localization fine-tuning rather than general embedding pre-training or graph-based IR — with in-batch different-fault programs as hard negatives, a design suited to the QLoRA fine-tuning setting.\n\nEvaluation plan:\n1. Primary — localization robustness: Hit@1 and MRR on a held-out mutation test set mirroring the ICST 2026 protocol, directly measuring brittleness reduction versus an untuned Qwen2.5-Coder-32B-Instruct baseline.\n2. Comparison against RGFL: Evaluate SeMutFL and RGFL on both clean SWE-bench Verified (where RGFL reports 85% Hit@1) and on the mutation-perturbed test set. If faithful RGFL reimplementation within the 12-day execution window proves infeasible — likely given RGFL's complex hierarchical retrieval pipeline — we will use RGFL's published numbers (85% Hit@1 from arXiv 2601.18044) as the clean-code reference point and restrict the primary robustness comparison to SeMutFL vs. untuned Qwen2.5-Coder-32B-Instruct on the mutation-perturbed test set. This is the more defensible framing in any case, as it directly measures the training-robustness contribution rather than reimplementation fidelity.\n3. Downstream repair validation: Empirically test whether improved localization robustness translates to better SWE-bench Verified repair success — directly validating, not assuming, the causal chain from arXiv 2604.05481. The 15-17x improvement cited in prior work comes from ground-truth localization versus no localization; we report the incremental gain from robustness over the untuned baseline, with no overclaim of replicating that gap.\n\nAblation schedule (4 runs, within 200 H100-hour budget):\n- Full SeMutFL (all 5 operators + InfoNCE loss)\n- Mutation augmentation only (no contrastive loss, plain SFT) — isolates the contribution of the InfoNCE objective\n- Variable-renaming-only operator set (most common mutation type in practice; isolates operator breadth contribution)\n- Untuned Qwen2.5-Coder-32B-Instruct baseline\n\nThe 'InfoNCE contrastive loss only (no augmented mutants)' condition is excluded: it is ill-posed because InfoNCE requires positive program pairs, and without augmented mutants there are no program-level positives to form the contrastive objective. The augmentation-only SFT condition already cleanly isolates the contribution of the contrastive loss. Reducing from five to four ablation conditions also ensures the worst-case budget (4 × 2 × 33h training + 70h evaluation + 8h data/validation = ~342 A100-hours ≈ 171 H100-hours at ±50% training time variance) remains genuinely under the 200 H100-hour ceiling.\n\nDifferentiation from RGFL: RGFL improves reasoning quality via structured explanations applied at inference time; SeMutFL improves representation-level robustness via training-time invariance enforcement. These are orthogonal: RGFL is not expected to be robust to mutations (no training change), while SeMutFL directly targets this gap.\nDifferentiation from arXiv 2602.11411: That work improves generation robustness via NLP-level prompt perturbations and plain SFT augmentation; SeMutFL addresses code-structure brittleness in fault localization via semantic-preserving code mutations and InfoNCE contrastive invariance.\nDifferentiation from arXiv 2505.10443: That work measures brittleness across 9 models; SeMutFL trains robustness in and empirically connects the fix to downstream repair, going from diagnostic to prescriptive.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~245h A100-80GB (Qwen2.5-Coder-32B QLoRA, 2×A100 per run, ~22h each; 4 ablations + evaluation)",
      "gpu_utilization": "~35-45% effective",
      "timeline": "4-6 months — INFEASIBLE: misses EMNLP 2026 ARR deadline of May 25, 2026",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$245-370 at ~$1.50/hr spot A100"
    },
    "human_in_loop": {
      "gpu_hours": "~176h A100-80GB (Qwen2.5-Coder-32B QLoRA, 2×A100 per run, ~22h each; 4 ablations + evaluation)",
      "gpu_utilization": "~65-75% effective",
      "timeline": "6-10 weeks — INFEASIBLE: misses EMNLP 2026 ARR deadline of May 25, 2026",
      "team": "1 researcher, ~30 min/day for approving ablation configs and reviewing results",
      "claude_api_cost": "$150-300 (~1,000-2,000 turns)",
      "estimated_gpu_cost": "~$264-396 at ~$1.50/hr spot A100"
    },
    "auto_research": {
      "gpu_hours": "~254 A100-80GB hours total (~127 H100-equivalent hours at 2x speedup), well within the 200 H100-hour budget. Breakdown: training — 4 ablation runs × 2×A100 × ~22h = 176 A100-hours; SWE-bench evaluation — ~35h × 2×A100 = 70 A100-hours; mutation data generation + test-suite equivalence validation — ~8 A100-hours; total = ~254 A100-hours ≈ 127 H100-equivalent hours. Worst-case (+50% training time variance): 4 × 2 × 33h = 264 A100-hours training + 70 evaluation + 8 data/validation = ~342 A100-hours ≈ 171 H100-equivalent hours — genuinely under the 200 H100-hour ceiling even at worst-case variance. The ~22h/run estimate is derived from first principles, with SWE-Gym (arXiv 2412.21139) confirming the scale: 491 trajectories × 18,578 avg tokens (Table 8) × 5 epochs = 45.5M total training tokens for 32B LoRA fine-tuning at max context length 32,768 on 2-8 NVIDIA H100 80G GPUs. No published benchmark directly reports QLoRA timing for 30B+ models on 2×A100-80GB; the 22h/run estimate relies entirely on the following first-principles throughput calculation, with ±50% variance as the correct risk mitigation. SeMutFL's training corpus is approximately 1.5× larger than SWE-Gym's OpenHands experiment: ~4,500 fault localization pairs (SWE-bench Verified ~500 instances + Defects4J ~395 bugs, each yielding 4–5 valid mutation pairs on average after equivalence checking) × ~5,120 average tokens per example (fault localization inputs include issue description, repository file hierarchy, and candidate file content) × 3 training epochs ≈ 69M total training tokens. Throughput on 2×A100-80GB with QLoRA is estimated at 680–910 tokens/sec: 2 × 312 TFLOPS BF16 peak × 35–45% practical MFU × 0.70 for QLoRA quantization/dequantization overhead (Dettmers et al., NeurIPS 2023) = 130–175 effective TFLOPS; for a 32B model (6N = 192 GFLOP per training token), this yields 680–910 tokens/sec. This range is cross-validated against first-principles H100 scaling: H100 at 989 TFLOPS × 40% MFU = 396 TFLOPS → ~2,060 tokens/sec for 32B LoRA; applying the 2×A100-80GB/H100 compute ratio (~0.63) and QLoRA throughput penalty (0.70) gives ~910 tokens/sec at the optimistic end. At ~800 tokens/sec central estimate, 69M tokens ≈ 86,250 seconds ≈ 24h; the stated 22h rounds this to account for gradient checkpointing and activation offloading optimizations typical in QLoRA implementations, which improve effective throughput 5–15% over the baseline MFU estimate. The ±50% variance range (11–33h) bounds real-world uncertainty in batch scheduling, dataset composition, and hardware utilization variability, and remains the correct risk mitigation regardless of the base estimate's precision.",
      "gpu_utilization": "~90% effective; agent chains mutation data synthesis, test-suite equivalence validation, QLoRA training, checkpoint evaluation, and SWE-bench scoring with near-zero idle",
      "timeline": "7-12 days with 2 concurrent A100 pairs (4 GPUs total); with 4 ablations and 2 parallel pairs, training completes in 2 batches (~44h wall-clock GPU time per batch at 22h/run) for ~88h training + setup and evaluation — fits within the 16-day window to the May 25 ARR deadline",
      "team": "0 (initial environment setup and mutation operator scaffolding only, ~3-4h one-time)",
      "claude_api_cost": "$300-600 (~2,500-4,000 turns for mutation pipeline code generation, experiment orchestration, result parsing, and draft report generation)",
      "estimated_gpu_cost": "~$381-572 at ~$1.50/hr spot A100 (254 A100-hours central × $1.50 ≈ $381 with ~50% buffer for worst-case re-runs)",
      "speed_bottleneck": "Sequential dependency between QLoRA fine-tuning and downstream SWE-bench repair evaluation; each 32B QLoRA run uses 2×A100-80GB for ~22h (estimated; see gpu_hours note above for grounding). With 4 concurrent A100s, 2 runs execute in parallel, completing 4 ablations in 2 serial batches of ~44h wall-clock each.",
      "risk_note": "Primary risk: InfoNCE temperature and mutation sampling rate may cause embedding collapse (silent loss decrease without localization improvement); automated per-epoch embedding variance monitoring and collapse detection must be wired into the agent loop before launch. Secondary risk: RGFL comparison requires either faithful reimplementation or careful scope qualification; explicit fallback is to use published RGFL numbers (85% Hit@1 on clean SWE-bench Verified) as clean-code reference and restrict robustness comparison to SeMutFL vs. untuned Qwen2.5-Coder-32B-Instruct baseline only. Tertiary risk: test-suite equivalence validation on SWE-bench Verified may reject more pairs than on Defects4J if SWE-bench test suites are less comprehensive; this would reduce training set size but is bounded by Defects4J as the primary training source and does not affect the soundness of the InfoNCE objective."
    }
  },
  "target_venues": [
    "EMNLP 2026 Main (ARR submission deadline May 25, 2026; 'NLP and Code Models' track; directly addresses the 2026 special theme on trustworthiness and robustness of LLMs)",
    "EMNLP 2026 Findings (as fallback if main conference spots are exhausted)"
  ],
  "level": "top-tier",
  "key_references": [
    "Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (ICST 2026, arXiv 2504.04372)",
    "Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations? (arXiv 2505.10443, May 2026)",
    "Reasoning Guided Fault Localization for LLM-Based Automated Program Repair (RGFL, arXiv 2601.18044, January 2026)",
    "On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481, 2026)",
    "Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data (arXiv 2602.11411, February 2026)",
    "Spatially Informed Dense Embedding Retrieval for Software Issue Localization (SpIDER, arXiv 2512.16956, December 2025)",
    "SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution (ACL Findings 2025)",
    "Contrastive Code Representation Learning (ContraCode, EMNLP 2021)",
    "Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization (MACL-IRFL, Automated Software Engineering 2026)",
    "Are Semantic-Preserving Transformations Reusable? Limitations of Published Semantic-Preserving Transformations for Code Models (arXiv 2503.23448, March 2025)",
    "Qwen2.5-Coder Technical Report (arXiv 2409.12186)",
    "SWE-smith: Scaling Data for Software Engineering Agents (arXiv 2504.21798, NeurIPS 2025)",
    "Training Software Engineering Agents and Verifiers with SWE-Gym (arXiv 2412.21139)",
    "QLoRA: Efficient Finetuning of Quantized LLMs (Dettmers et al., NeurIPS 2023)"
  ],
  "description": "LLMs trained for code exhibit surface-form brittleness: semantic-preserving mutations (variable renaming, loop reformulation, branch reordering) cause fault localization models to change their predictions in 78% of previously correct cases (ICST 2026), with concurrent evidence of up to 70% performance drops across nine leading models (arXiv 2505.10443). This is an NLP robustness problem — shallow pattern matching rather than semantic grounding — directly analogous to instruction-phrasing sensitivity in text. While RGFL (arXiv 2601.18044) achieves 85% file-level Hit@1 on SWE-bench Verified via improved reasoning, it does not modify training and would be expected to remain brittle under surface-form variation. arXiv 2602.11411 (February 2026) improves code LLM robustness via perturbed SFT, but applies NLP-level prompt perturbations (typos, synonyms, back-translation) to code generation tasks without a contrastive objective, leaving fault-localization brittleness under semantic-preserving code transformations unaddressed. SeMutFL addresses this gap by augmenting fine-tuning data with (original, mutant) program pairs sharing identical ground-truth fault locations, generated by five automated semantics-preserving mutation operators applied to SWE-bench Verified and Defects4J. Operator inclusion rates are stratified by construction-safety: variable renaming, alias introduction, and dead-code insertion target ~100% inclusion (safe by construction), while statement reordering and loop normalization achieve lower, program-dependent inclusion rates due to conservative AST dependency analysis — the three high-inclusion operators form the reliable training core, making corpus soundness structurally independent of the complex operators and directly addressing the 59% implementation failure rate documented in arXiv 2503.23448. Fine-tuning Qwen2.5-Coder-32B-Instruct with QLoRA under a dual cross-entropy plus InfoNCE contrastive consistency objective — using different-fault programs as hard negatives — enforces semantic invariance directly in the model's representations. Evaluation measures localization robustness on a held-out mutation test set mirroring the ICST 2026 protocol, comparison against RGFL on both clean and mutated code (with explicit fallback to published RGFL numbers if reimplementation is infeasible within the execution window), and empirical validation of whether robustness gains translate to downstream SWE-bench Verified repair success. The ~22h/run training time estimate is derived from first principles, with SWE-Gym (arXiv 2412.21139) confirming the scale: 491 trajectories × 18,578 avg tokens (Table 8) × 5 epochs = 45.5M training tokens for 32B LoRA on H100 hardware. No published benchmark directly reports QLoRA timing for 30B+ models on 2×A100-80GB; the estimate relies entirely on first-principles throughput: SeMutFL's ~4,500 training pairs × ~5,120 avg tokens × 3 epochs ≈ 69M tokens at ~800 tokens/sec (2 × 312 TFLOPS × 40% MFU × 0.70 QLoRA overhead, Dettmers et al. NeurIPS 2023) ≈ 24h, with ±50% variance bounding real-world uncertainty. The ablation design uses four conditions (Full SeMutFL, augmentation-only SFT, variable-renaming-only, untuned baseline) with worst-case budget of ~342 A100-hours ≈ 171 H100-hours — genuinely under the 200 H100-hour ceiling even at worst-case variance. The method requires no manual annotation, uses only publicly available datasets, and targets EMNLP 2026's explicit theme of LLM trustworthiness and robustness.",
  "project_name": "semutfl_robust_fault_loc",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL — VENUE MISMATCH: The user required EMNLP 2026 (ARR deadline May 25, 2026), but target_venues lists ICSE 2027, AAAI 2027, and ICLR 2027. The idea must be redesigned around the correct venue.", "CRITICAL — TIMELINE VIOLATION: Manual mode requires 4–6 months, HIL 6–10 weeks — both impossible in 16 days. Only auto research (5–14 days) is plausible, but violates the compute ceiling.", "CRITICAL — COMPUTE BUDGET VIOLATION: Auto research mode requires 900–1,400 A100-hours (≈450–700 H100-equivalent), 2.5–3.5× over the 200 H100-hour hard constraint. A version using Qwen2.5-Coder-32B (2×A100 per run, ~20–25h each) with ≤5 ablations would cost ≈100–130 H100-hours and fit the budget.", "OUTDATED BASE MODEL CLAIM: Kimi-Dev-72B is no longer open-source SOTA on SWE-bench Verified as of May 2026; GLM-4.7, Kimi K2 Thinking, Qwen3-Coder-Next, and DeepSeek v3.2 have superseded it. The experiment must be updated to reflect the current landscape or explicitly justify the model choice.", "UNACKNOWLEDGED COMPETITOR — RGFL (arXiv 2601.18044, January 2026): This paper improves file-level Hit@1 from 71.4% to 85% on SWE-bench Verified using hierarchical reasoning with structured explanations. It is the strongest current FL baseline and directly competes with SeMutFL's localization improvement claim — ignoring it will draw immediate rejection from reviewers.", "INDIRECT CONNECTION BETWEEN BRITTLENESS AND 15–17X REPAIR IMPROVEMENT: arXiv 2604.05481 shows the 15–17x gain comes from accurate file-level context quality (ground-truth localization vs none), not from reducing the 78% brittleness under mutations. SeMutFL must demonstrate empirically that reducing mutation-induced localization failures also improves downstream repair rates, not assume the causal link.", "EMNLP TRACK FIT RISK: Fault localization as a concept is strongly SE-scoped. For EMNLP NLP and Code Models reviewers, the framing must foreground LLM robustness to surface-form variation in code understanding (an NLP phenomenon), not mutation testing methodology (an SE concept). The current framing reads as an SE paper submitted to an NLP venue."]
Feedback: The research core — training fault localization robustness via semantic-mutation augmentation — is genuinely novel and well-motivated by the two verified empirical studies. The idea is worth revising rather than abandoning. To meet user requirements, the generator must make four concrete changes:

1. **Fix the venue**: Set target_venues to ['EMNLP 2026 Main', 'EMNLP 2026 Findings'] with ARR deadline May 25, 2026. Remove ICSE/AAAI/ICLR 2027 entirely.

2. **Scale to fit 200 H100-hours in 16 days**: Replace Kimi-Dev-72B with Qwen2.5-Coder-32B-Instruct or DeepSeek-Coder-V2-16B as the fine-tuning base. At 32B, each QLoRA run uses 2×A100-80GB × ~20h = 40 A100-hours ≈ 20 H100-hours. Five ablations + evaluation = ≈130 H100-hours total — within budget. The 72B model is infeasible under both the compute ceiling and the 16-day clock.

3. **Acknowledge and compare against RGFL (arXiv 2601.18044)**: This paper achieves 85% file-level Hit@1 on SWE-bench Verified and is the correct stronger baseline. SeMutFL must demonstrate improvement over RGFL or explicitly show that mutation robustness is complementary to reasoning-guided localization.

4. **Reframe for NLP audience**: Lead with 'LLM code understanding is brittle under surface-form variation' (NLP robustness framing), not 'fault localization fails under mutation testing' (SE framing). Emphasize semantic grounding of code representations as the NLP contribution. The EMNLP NLP and Code Models track is receptive to this framing if the language is right.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL — UNACKNOWLEDGED COMPETITOR arXiv 2602.11411: 'Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data' (Feb 2026) uses the same methodological core — fine-tuning code LLMs with semantically-perturbed code (variable renaming, dead-code insertion, statement reordering) + contrastive loss — to improve robustness. The task domain differs (code generation/summarization vs. fault localization), but any EMNLP reviewer familiar with this paper will flag the overlap. SeMutFL must cite this work and explicitly argue that (a) the FL task formulation is fundamentally different from generation robustness, (b) the training signal (fault location labels vs. functional correctness) creates a distinct objective, and (c) the InfoNCE formulation with fault-negative sampling is not subsumed by this prior work. Failure to do so is a near-certain rejection trigger.", "COMPUTE INCONSISTENCY: The itemized breakdown (5 runs × 2 A100s × 22h = 220 A100-hours for training; + 35h × 2 A100s = 70 A100-hours for SWE-bench evaluation; + 5 A100-hours for mutation synthesis = 295 total A100-hours) is inconsistent with the header claim of '220-260 A100-80GB hours total.' The correct total is approximately 295 A100-hours ≈ 148 H100-hours at 2x conversion, which is within the 200 H100-hour budget — but the stated numbers must be made internally consistent to survive reviewer scrutiny.", "RGFL COMPARISON RISK IS UNDER-MITIGATED: The evaluation plan compares SeMutFL against RGFL on both clean and mutation-perturbed SWE-bench Verified, but RGFL is a complex hierarchical reasoning pipeline. Within 7-12 days of auto_research execution, a faithful reimplementation is unlikely. The risk note acknowledges this but does not provide a fallback strategy. The proposal should explicitly state: (a) if RGFL reimplementation is infeasible, reported RGFL numbers from arXiv 2601.18044 will be used as reference with explicit scope qualification, or (b) only clean-code comparison against published RGFL numbers will be made, with mutation robustness evaluated only against the untuned Qwen2.5-Coder-32B-Instruct baseline.", "22H/RUN TRAINING TIME ESTIMATE IS UNCITED: The ~22h per QLoRA run for Qwen2.5-Coder-32B on 2×A100-80GB is plausible but unverified in the literature. This estimate should be grounded in a cited pilot run, a comparable training report (e.g., Qwen2.5-Coder-32B fine-tuning documentation from Alibaba), or explicitly marked as an estimate with ±50% variance acknowledged in the budget.", "MACL-IRFL ADAPTATION CLAIM IS SLIGHTLY OVERSTATED: The proposal says it 'adapts MACL-IRFL's multi-view contrastive framework to the LLM QLoRA fine-tuning setting,' but MACL-IRFL uses three-way graph-based views (bug-code interaction, bug similarity, code co-citation), while SeMutFL uses simple pairwise (original, mutant) pairs — structurally closer to ContraCode's augmentation strategy. This claim should be softened to avoid reviewer confusion about what exactly is being adapted."]
Feedback: Round 1 critical fixes (venue, model scale, RGFL acknowledgment, causal chain correction, NLP framing) are all solid and substantially improve the proposal. The research core remains genuinely novel and well-motivated. To reach 'pass,' make four targeted fixes:

1. **Acknowledge arXiv 2602.11411 in the landscape section.** Add it as a direct methodological predecessor: 'arXiv 2602.11411 (Feb 2026) fine-tunes code LLMs with perturbed data (including variable renaming and dead-code insertion) and a contrastive loss to improve robustness on code generation and summarization tasks. SeMutFL is differentiated by (a) fault localization as the task — requiring models to identify which file/function contains a bug, not to generate semantically equivalent code, (b) fault-location labels as the contrastive negative signal (different-fault programs, not different-program programs), and (c) evaluation on mutation-perturbed SWE-bench Verified specifically for localization accuracy under surface-form variation.' This differentiation is real and defensible — it just needs to be stated.

2. **Fix the compute breakdown.** The correct total is ~295 A100-hours ≈ 148 H100-equivalent hours. Update the header to '~295 A100-80GB hours total (~148 H100-equivalent hours at 2x speedup), within the 200 H100-hour budget.' Make all sub-totals consistent.

3. **Add a concrete RGFL comparison fallback.** State explicitly: 'If RGFL reimplementation within the 12-day execution window proves infeasible, we will use RGFL's published numbers (85% Hit@1 on clean SWE-bench Verified from arXiv 2601.18044) as the clean-code reference point and restrict the primary robustness comparison to SeMutFL vs. untuned Qwen2.5-Coder-32B-Instruct on the mutation-perturbed test set.' This doesn't weaken the contribution — it sets honest expectations.

4. **Soften the MACL-IRFL adaptation claim.** Change 'adapting MACL-IRFL's multi-view contrastive framework' to 'using an InfoNCE pairwise contrastive objective, inspired by ContraCode's augmentation paradigm and consistent with the contrastive approach in MACL-IRFL, but applied to fault localization fine-tuning.' This is more accurate and avoids misleading reviewers about what is novel.

### Round 3 review
Verdict: revise
Issues: ["MODERATE — MUTATION VALIDITY GAP (arXiv 2503.23448): An independent March 2025 study tested 39 semantic-preserving transformations from the published literature and found 23/39 (59%) change code semantics when actually implemented. SeMutFL proposes five mutation operators (variable renaming, dead-code insertion, statement reordering, loop normalization, alias introduction) but provides no validation that these are genuinely semantics-preserving in practice. Statement reordering in particular is high-risk — if statements have data dependencies, reordering changes behavior. Without explicit validation (e.g., test-suite equivalence checking on Defects4J, where ground-truth test suites are available), the training corpus may contain pairs where 'mutant' versions have different fault locations from what the label says, directly corrupting the InfoNCE objective. This must be addressed before submission.", "MODERATE — BUDGET ARITHMETIC UNDER VARIANCE: The proposal acknowledges ±50% training time variance for the 22h/run estimate, but the budget arithmetic is inconsistent under this variance. Worst case: 5 ablations × 2 A100s × 33h = 330 A100-hours (training) + 70 (SWE-bench) + 5 (mutation) = 405 A100-hours = 202.5 H100-hours — exceeding the 200 H100-hour hard constraint. The stated '30% headroom for re-runs' is a separate buffer from training time variance headroom; the proposal implicitly conflates them as if one covers both. Reducing from 5 to 4 ablations (dropping the 'InfoNCE only, no augmented mutants' condition, which is confounded and hard to interpret without pairs) would bring worst-case training to 4 × 2 × 33h = 264 A100-hours = 132 H100-hours + 37.5 = 169.5 H100-hours — genuinely under budget even at worst-case variance.", "MINOR — TRAINING TIME ESTIMATE STILL UNCITED: The ~22h/run estimate for Qwen2.5-Coder-32B QLoRA on 2×A100-80GB could not be verified against any published community benchmark or Alibaba technical documentation. No comparable 30B-class QLoRA training time reports were found. The acknowledgment of ±50% variance partially addresses this, but a concrete citation (e.g., Qwen2.5-Coder technical report arXiv 2409.12186 Appendix, or a referenced pilot run) would strengthen the feasibility claim under reviewer scrutiny."]
Feedback: Round 2 critical issues are all resolved — the proposal is structurally sound and the core novelty is confirmed by independent search. To reach 'pass' in Round 4, make two targeted fixes:

1. **Add mutation validation protocol (addresses the 2503.23448 risk)**: In the approach section, add: 'All five mutation operators are validated for semantic preservation using test-suite equivalence checking on Defects4J: a mutated program is included in training only if it passes the same test suite as the original. Pairs failing this check are discarded, targeting a validation rate ≥95% per operator.' Variable renaming and alias introduction should pass easily; dead-code insertion is safe by construction; statement reordering and loop normalization should be restricted to provably dependency-free cases (detected via lightweight static analysis on the AST). This directly addresses the known implementation failure rate found in arXiv 2503.23448 and strengthens experimental integrity.

2. **Tighten ablation set from 5 to 4 conditions**: Remove the 'InfoNCE contrastive loss only (no augmented mutants)' condition — this is ill-posed because InfoNCE requires positive pairs, and without augmented mutants there are no program-level positives. Replace it implicitly with the existing 'mutation augmentation only (no contrastive loss)' condition, which already cleanly isolates the contribution of the loss. The remaining four conditions (Full SeMutFL, augmentation-only SFT, variable-renaming-only, untuned baseline) are maximally informative. This reduces worst-case training from 202.5 to 169.5 H100-hours — genuinely under budget even at ±50% variance, resolving the arithmetic inconsistency cleanly.

### Round 4 review
Verdict: revise
Issues: ["MINOR — TRAINING TIME ESTIMATE STILL INSUFFICIENTLY GROUNDED: The ~22h/run estimate for Qwen2.5-Coder-32B QLoRA on 2×A100-80GB cites (a) the Qwen2.5-Coder technical report as confirming A100-80GB hardware class (not training time) and (b) SWE-smith as showing full-parameter fine-tuning is feasible 'within single-digit-day timescales' — which is a substantially weaker grounding than a specific QLoRA timing benchmark. The Alibaba Cloud Qwen2.5-Coder fine-tuning tutorial (alibabacloud.com/help/en/pai/use-cases/training-evaluation-compression-and-deployment-of-qwen2-5-coder-model) and the Hugging Face Qwen2.5-Coder-32B-Instruct discussion thread contain specific hardware-time data that directly supports or refutes the 22h estimate. The ±50% variance buffer is the correct risk mitigation, but the underlying estimate should be anchored to a concrete source to survive reviewer feasibility scrutiny.", "MINOR — ≥95% INCLUSION RATE TARGET IS UNSTRATIFIED: The proposal states a single ≥95% inclusion rate target for all five operators, but operator risk varies dramatically: variable renaming and alias introduction are safe by construction and will approach 100%, dead-code insertion is similarly safe, while statement reordering and loop normalization depend on conservative dependency analysis that may filter a large fraction of candidate statement blocks. Stating a uniform 95% target obscures that the effective training data from reordering/loop normalization operators may be substantially smaller. The proposal should acknowledge that per-operator inclusion rates will differ and that a smaller-than-expected contribution from complex operators does not invalidate the InfoNCE objective — it just reduces operator diversity for those categories. This is a framing fix, not a scientific problem."]
Feedback: Round 3's three issues (mutation validity, budget arithmetic, ablation count) are all correctly resolved. The proposal is scientifically sound and the remaining issues are minor framing and grounding problems. Two targeted fixes bring this to pass:

1. **Anchor the 22h/run estimate to a direct source**: Fetch the Alibaba Cloud Qwen2.5-Coder fine-tuning tutorial or cite the Hugging Face Qwen2.5-Coder-32B-Instruct hardware discussion thread for a specific QLoRA training time on 2×A100-80GB. If no direct source is available, replace the citation with: 'The 22h/run estimate is derived from first-principles: [sequence length] × [dataset size] × [QLoRA optimizer steps] at measured [tokens/sec] throughput on A100-80GB (citing any community QLoRA benchmark for a comparable 30B-class model).' The ±50% variance already provides adequate safety margin — the fix is about the base estimate's citation.

2. **Stratify the inclusion rate claim by operator risk**: Change '≥95% inclusion rate per operator' to 'Variable renaming and alias introduction satisfy the equivalence check by construction (targeting ~100% inclusion); dead-code insertion is safe by construction; statement reordering and loop normalization are restricted to dependency-free blocks and are expected to achieve lower inclusion rates depending on program structure — but these are supplementary operators and any reduction in their coverage does not affect the soundness of the InfoNCE objective or the training signal from the remaining three operators.' This makes the claim defensible rather than aspirational.

### Round 5 review
Verdict: revise
Issues: ["MINOR — SWE-GYM ANCHOR CONTAINS VERIFIABLE FACTUAL INACCURACIES: The resource estimate describes SWE-Gym (arXiv 2412.21139) as using 'context length 10,240 tokens, on a single H100 GPU' for the 32B LoRA training anchoring the 22h/run estimate. Independent verification finds: (a) SWE-Gym's OpenHands training (the 491-trajectory experiment the proposal cites) specifies max context length 32,768 — not 10,240 — and uses 2-8 NVIDIA H100 80G GPUs, not a single H100; (b) the single-H100 setup applies to SWE-Gym's MoatlessTools 32B LoRA verifier experiment, which used only 62-172 trajectories, not 491. The token statistics (491 trajectories × 18,578 avg tokens, Table 8) are correctly cited. The ±50% variance buffer preserves the budget regardless, but a reviewer checking this reference will find the context length and hardware attribution wrong, which undermines credibility of the feasibility claim at a critical juncture of reviewer scrutiny."]
Feedback: Round 4's two targeted issues are both correctly resolved: inclusion rate stratification is now properly differentiated by operator construction-safety, and the first-principles throughput calculation is substantially more detailed. One description fix remains:

**Correct the SWE-Gym anchor.** The resource estimate claims SWE-Gym uses 'context length 10,240 tokens, on a single H100 GPU' for the 491-trajectory 32B LoRA training, but the paper specifies max context length 32,768 for that run (OpenHands training on 2-8 H100s). The correct framing is: 'SWE-Gym (arXiv 2412.21139) confirms the scale: 491 successful trajectories × 18,578 avg tokens (Table 8) × 5 epochs = 45.5M total training tokens for 32B LoRA fine-tuning on H100 hardware.' Do not specify context length (it is not 10,240) or imply a single-H100 setup for that run. Rely entirely on the first-principles throughput calculation for the 22h estimate, and explicitly note that no published benchmark directly reports QLoRA timing for 30B+ models on 2×A100-80GB — the ±50% variance is the correct risk mitigation. This is a description fix only; the token count, throughput calculation, and budget arithmetic are all correct as stated.


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
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "type": "user",
  "uuid": "b2ba9440-e09a-4ea3-a4bd-d22179accef1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T06:25:06.503Z_

```json
{
  "parentUuid": "b2ba9440-e09a-4ea3-a4bd-d22179accef1",
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
  "uuid": "90e29d5f-fac1-4c6f-be7f-cb45bc506e9b",
  "timestamp": "2026-05-10T06:25:06.503Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T06:25:06.503Z_

```json
{
  "parentUuid": "90e29d5f-fac1-4c6f-be7f-cb45bc506e9b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3a186239-8721-4d1c-9b62-fb0cf5a75067",
  "timestamp": "2026-05-10T06:25:06.503Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
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
  "leafUuid": "3a186239-8721-4d1c-9b62-fb0cf5a75067",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "SeMutFL: Training Fault Localization Robustness via Semantic Mutation Augmentation",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd"
}
```

---

### Assistant

_source line 8 · 2026-05-10T06:25:41.347Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea (SeMutFL) which is now in round 6 of 10. I need to independently verify claims, search for competitive work, and assess whether the round 5 issue has been properly addressed.

The round 5 issue was:
- MINOR — SWE-GYM ANCHOR CONTAINS VERIFIABLE FACTUAL INACCURACIES: The resource estimate incorrectly described SWE-Gym as using 'context length 10,240 tokens, on a single H100 GPU' for the 491-trajectory experiment. The correct values are max context length 32,768 and 2-8 NVIDIA H100 80G GPUs.
  
Now I'm checking the resource estimates in round 6 to see if they've corrected the GPU specifications and whether the computational breakdown for training, evaluation, and data generation is accurate and properly justified.

Even with a worst-case 50% variance in training time, the total comes to around 171 H100-equivalent hours, which stays under the 200-hour budget. The 22-hour per-run estimate is grounded in the SWE-Gym paper's token counts and training configuration across the specified GPU setup.

Now I'm verifying the token calculation from the paper and checking other key claims in the proposal, particularly around the stratified inclusion rates and the first-principles throughput assumptions that underpin the timing estimates.

The stratification approach is well-documented: variable renaming and dead-code insertion are safe by construction and should hit near-complete inclusion, while statement reordering and loop normalization are constrained to dependency-free blocks via AST analysis, which will naturally yield lower inclusion rates depending on program structure.

For the RGFL fallback, if a faithful reimplementation isn't feasible within the timeline, the proposal defaults to using RGFL's published benchmark numbers as the reference point rather than attempting a partial implementation.

The contrastive learning setup draws from ContraCode's augmentation strategy, applying an InfoNCE formulation specifically to fault localization fine-tuning rather than general embedding pre-training.

All mutations are validated through test-suite equivalence checking—a mutant only enters the training set if it preserves the original program's test behavior.

Now I'm moving into independent verification of the paper's claims. I need to check whether the cited arXiv papers actually exist and support what's being claimed, verify the RGFL reference, and search for any recent competitive work that might have emerged since the last review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a186239-8721-4d1c-9b62-fb0cf5a75067",
  "isSidechain": false,
  "requestId": "req_011CatQmZwmLAFKrcvnED3MK",
  "type": "assistant",
  "uuid": "cb5ce172-db9f-4f52-bc67-f118236f212f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JCxg5K1jJZ9MoqRbHZUf2w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20685,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2473,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2473,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 20685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20685
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

_source line 9 · 2026-05-10T06:25:41.350Z_

I'll conduct independent verification searches to assess this round 6 proposal. Let me check whether the round 5 fix (SWE-Gym anchor correction) was properly applied, and search for any new competitive work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb5ce172-db9f-4f52-bc67-f118236f212f",
  "isSidechain": false,
  "requestId": "req_011CatQmZwmLAFKrcvnED3MK",
  "type": "assistant",
  "uuid": "e339b564-4211-4f9d-b3c9-d2a332ff9598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JCxg5K1jJZ9MoqRbHZUf2w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20685,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2473,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2473,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 20685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20685
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

_source line 10 · 2026-05-10T06:25:51.675Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Gw4r1vWYRKPdqGz8GCy2rq`</summary>

```json
{
  "description": "Verify key paper claims and search for competitive work",
  "subagent_type": "Explore",
  "prompt": "I'm conducting an adversarial review of a research proposal called \"SeMutFL: Contrastive Mutation Augmentation for Surface-Form Robust Code Understanding in Fault Localization.\" I need you to search for and verify several claims. Please conduct the following searches and report what you find:\n\n1. Search for arXiv paper 2504.04372 - \"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models\" - does it exist and does it report a 78% failure rate under semantic-preserving mutations?\n\n2. Search for arXiv paper 2505.10443 - \"Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?\" - does it exist and does it show performance drops up to 70% across nine LLMs?\n\n3. Search for RGFL (arXiv 2601.18044) - \"Reasoning Guided Fault Localization for LLM-Based Automated Program Repair\" - does it exist and does it report 85% Hit@1 on SWE-bench Verified?\n\n4. Search for arXiv 2602.11411 - \"Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data\" - does it exist and does it apply NLP-level perturbations (typos, synonyms, back-translation) rather than semantic-preserving code mutations?\n\n5. Search for any NEW papers from March-May 2026 that address surface-form robustness in fault localization via contrastive learning or mutation augmentation for LLMs. Try searches like:\n   - \"fault localization robustness contrastive 2026\"\n   - \"semantic mutation augmentation code LLM 2026\"\n   - \"code understanding surface-form invariance training 2026\"\n   - site:arxiv.org \"fault localization\" \"contrastive\" \"mutation\" 2026\n\n6. Search for SWE-Gym (arXiv 2412.21139) - specifically verify: does it describe training with 491 trajectories × 18,578 avg tokens for 32B LoRA on H100 hardware? Does Table 8 contain these token statistics?\n\nReport findings concisely for each item."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e339b564-4211-4f9d-b3c9-d2a332ff9598",
  "isSidechain": false,
  "requestId": "req_011CatQmZwmLAFKrcvnED3MK",
  "type": "assistant",
  "uuid": "9bd75308-5fef-4190-8845-2ff788d8a977",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JCxg5K1jJZ9MoqRbHZUf2w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20685,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2473,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2473,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 20685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20685
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

_source line 11 · 2026-05-10T06:25:59.321Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HR5rJrZXBvoUvDsh4QmsRc`</summary>

```json
{
  "description": "Search for competitive work on code robustness and fault localization",
  "subagent_type": "Explore",
  "prompt": "I'm conducting an adversarial review of a research proposal about training LLMs to be robust to semantic-preserving code mutations for fault localization (identifying which file/function has a bug). The proposal uses contrastive learning (InfoNCE loss) with mutation-augmented training data.\n\nPlease search for competitive and potentially overlooked work:\n\n1. Search \"site:arxiv.org contrastive learning code robustness fault localization 2025 2026\"\n2. Search \"code LLM robustness mutation invariant training 2026 arxiv\"\n3. Search \"semantic preserving code transformation robustness training 2026\"\n4. Search for ContraCode (EMNLP 2021) - \"Contrastive Code Representation Learning\" - verify it exists and targets general pre-training embeddings, not fault localization\n5. Search \"MACL-IRFL multi-view adaptive contrastive learning fault localization 2026\" - verify this exists\n6. Search \"SWE-bench fault localization robustness 2026 arxiv\"\n7. Search \"arXiv 2503.23448 semantic preserving transformations limitations\" - does this paper exist and does it find 59% of transformations change semantics?\n8. Search for any recent (2025-2026) papers on:\n   - \"program transformation augmentation LLM robustness\"\n   - \"code mutation data augmentation fine-tuning robustness\"\n   - \"fault localization contrastive learning\"\n\nReport what you find for each search, including paper titles, venues, and key findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bd75308-5fef-4190-8845-2ff788d8a977",
  "isSidechain": false,
  "requestId": "req_011CatQmZwmLAFKrcvnED3MK",
  "type": "assistant",
  "uuid": "2f8efb91-93ac-49aa-ba5b-51dc5a602436",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JCxg5K1jJZ9MoqRbHZUf2w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20685,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2473,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2473,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 20685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20685
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

_source line 12 · 2026-05-10T06:26:55.441Z_

<details><summary>↩ Tool result · `toolu_01HR5rJrZXBvoUvDsh4QmsRc`</summary>

```text
Perfect! Now let me compile the comprehensive report of all findings.

## Comprehensive Competitive Work Analysis Report

I've completed an extensive search for competitive and potentially overlooked work on LLM robustness to semantic-preserving code mutations for fault localization. Here are the key findings:

---

### **1. Direct Competition on Fault Localization Robustness (2026)**

**Primary Competitive Work: "Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models"**
- **Venue:** ICST 2026 (IEEE International Conference on Software Testing, Verification and Validation)
- **ArXiv ID:** [2504.04372](https://arxiv.org/abs/2504.04372)
- **Key Finding:** 78% failure rate - When semantic-preserving mutations are applied, LLMs fail to localize the same fault they correctly identified previously in 78% of cases
- **Approach:** Tests LLM fault localization robustness using multiple semantic-preserving mutation types (identifier renaming, comment insertion/modification, formatting changes, dead-code insertion)
- **Critical Issue:** This directly addresses the core problem your proposal targets and reports empirically that LLMs' fault reasoning is tied to syntactically-irrelevant features

---

### **2. Multi-View Adaptive Contrastive Learning Approach (MACL-IRFL, 2025)**

**Paper:** "Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization"
- **Venue:** Automated Software Engineering journal (published November 6, 2025), also [arXiv 2409.12519](https://arxiv.org/abs/2409.12519)
- **Publisher:** Springer Nature
- **Key Innovation:** Uses graph neural networks modeling three views:
  - Report-code interaction relationships
  - Report-report similarity relationships  
  - Code-code co-citation relationships
- **Results:** Up to 28.93% improvement on Accuracy@1, 25.57% MAP, 20.35% MRR
- **Approach Similarity:** Uses contrastive learning for fault localization but focuses on multi-view graph modeling rather than mutation-based augmentation

---

### **3. Semantic-Preserving Transformation Limitations (Critical, March 2025)**

**Paper:** "Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection"
- **ArXiv ID:** [2503.23448](https://arxiv.org/abs/2503.23448)
- **Authors:** Max Hort, Linas Vidziunas, Leon Moonen
- **Publication Date:** March 30, 2025
- **CRITICAL FINDING:** **59% of implemented transformations actually change semantics** (23 of 39 transformations changed semantics; only 16 of 39 were truly semantic-preserving)
- **Implication:** This directly undermines the foundation of mutation-based augmentation approaches - the authors found they could not improve defect detection models even with supposedly semantic-preserving transformations
- **Conclusion:** "reusing shared semantic-preserving transformation is difficult, sometimes even causing wrongful changes to the semantics"

---

### **4. ContraCode (EMNLP 2021) - Foundational Pre-training Work**

**Paper:** "Contrastive Code Representation Learning"
- **Venue:** EMNLP 2021
- **Authors:** Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica
- **ArXiv ID:** [2007.04973](https://arxiv.org/abs/2007.04973)
- **GitHub:** [github.com/parasj/contracode](https://github.com/parasj/contracode)
- **Key Focus:** General pre-training embeddings using contrastive learning, NOT fault localization
- **Approach:** Pre-trains on 1.8m JavaScript methods from GitHub using source-to-source compiler transformations to generate functionally similar variants
- **Results:** 39% AUROC improvement on adversarial code clone detection; 2-13 point improvements on summarization and type inference
- **Relevance:** Demonstrates that contrastive pre-training on mutation variants improves robustness, but targets general code understanding, not fault localization specifically

---

### **5. Automated Semantic-Preserving Transformations (Auto-SPT, December 2024)**

**Paper:** "Auto-SPT: Automating Semantic Preserving Transformations for Code"
- **ArXiv ID:** [2512.06042](https://arxiv.org/abs/2512.06042)
- **Venue:** OpenReview (appears to be under review/accepted)
- **Key Innovation:** Uses LLMs to automatically generate diverse and strong semantic-preserving transformations, addressing the problem that heuristic-based transformations are limited
- **Results:** Successfully generates more diverse SPTs than existing heuristic approaches; significantly drops performance of code clone detectors when applied
- **Practical Finding:** Successfully uses Auto-SPT to augment training data and improve robustness of code clone detection models
- **Relevance:** Provides a potentially more reliable way to generate mutation-augmented training data than manual/heuristic approaches

---

### **6. Code Mutation-Based Robustness Studies (2025-2026)**

**"Memorize or Generalize? Evaluating LLM Code Generation with Code Rewriting"**
- **ArXiv ID:** [2503.02296](https://arxiv.org/abs/2503.02296)
- **Finding:** Mutation causes moderate performance drops; paraphrase is nearly invariant; rewrites are most disruptive - suggests harmful memorization beyond surface-level robustness

**"Fine-Tuning LLMs for Code Mutation: A New Era of Cyber Threats"**
- **ArXiv ID:** [2410.22293](https://arxiv.org/abs/2410.22293)
- **Finding:** Explores how fine-tuning LLMs on mutated code creates cybersecurity risks

---

### **7. Data Augmentation Framework Results (AAAI-26, January 2026)**

**"When Does Data Augmentation Improve Robustness?"** (accepted AAAI-26)
- **Key Finding:** Mathematical framework shows data augmentation increases variability and diversity in training data, but the relationship between diversity and robustness is complex and context-dependent
- **Implication:** Simply augmenting with more mutations doesn't guarantee robustness improvements

---

### **8. Synthetic Data and Fine-tuning Robustness Trade-offs (2025)**

**"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning"**
- **ArXiv ID:** [2511.01490](https://arxiv.org/abs/2511.01490)
- **Critical Finding:** Synthetic fine-tuning data (including augmented variants) can **decrease adversarial robustness** while preserving output quality
- **Implication:** Your contrastive learning approach using augmented data must carefully balance robustness gains against potential degradation in other robustness dimensions

---

### **9. Robustness in LLMs - General Survey (2025)**

**"Robustness in Large Language Models: A Survey of Mitigation Strategies and Evaluation Metrics"**
- **ArXiv ID:** [2505.18658](https://arxiv.org/abs/2505.18658)
- **Published:** 2025
- **Scope:** Comprehensive survey of robustness techniques; provides context for where mutation-based augmentation fits in the broader landscape

---

## Key Overlaps and Gaps Identified

### Direct Competition:
1. **ICST 2026 paper (2504.04372)** - Likely the most direct competitor, also studies fault localization robustness to semantic-preserving mutations
2. **MACL-IRFL** - Different approach (multi-view graphs) but same fault localization problem domain

### Critical Vulnerabilities in Your Approach:
1. **arXiv 2503.23448** - Demonstrates that 59% of "semantic-preserving" transformations actually change semantics, undermining the foundation of mutation-augmented training
2. **arXiv 2511.01490** - Shows synthetic augmented data can degrade adversarial robustness in fine-tuning
3. **The 78% failure rate (ICST 2026)** - Shows the scale of the problem is severe; contrastive learning with current mutation approaches may not solve this

### Potentially Overlooked Opportunities:
1. **Auto-SPT** - Could improve your mutation generation quality by using LLM-based transformation generation rather than heuristic/manual approaches
2. **ContraCode pre-training** - Your work could build on ContraCode's general pre-training approach but adapt it specifically for fault localization
3. **Multi-view contrastive approaches** - MACL-IRFL suggests that modeling multiple relationship types (not just code-fault pairs) could improve results

---

## Summary Assessment

Your proposal directly addresses a critical gap identified in ICST 2026 (the 78% robustness failure), and uses a promising technique (contrastive learning with InfoNCE loss). However, you face substantial competitive and methodological challenges:

- **Direct competitor:** ICST 2026 paper already quantifies the problem you're solving
- **Methodological risk:** arXiv 2503.23448 shows 59% of supposedly semantic-preserving transformations actually change semantics—this is a fundamental threat to mutation-based augmentation approaches
- **Data augmentation risk:** Recent work shows synthetic augmentation can paradoxically reduce robustness
- **Potential mitigation:** Adopt LLM-based transformation generation (Auto-SPT) and consider multi-view contrastive approaches (MACL-IRFL model)

Sources:
- [Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (ICST 2026)](https://arxiv.org/abs/2504.04372)
- [Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization](https://arxiv.org/abs/2409.12519)
- [Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection](https://arxiv.org/abs/2503.23448)
- [Contrastive Code Representation Learning (ContraCode)](https://arxiv.org/abs/2007.04973)
- [Auto-SPT: Automating Semantic Preserving Transformations for Code](https://arxiv.org/abs/2512.06042)
- [Memorize or Generalize? Evaluating LLM Code Generation with Code Rewriting](https://arxiv.org/abs/2503.02296)
- [Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning](https://arxiv.org/abs/2511.01490)
- [Robustness in Large Language Models: A Survey of Mitigation Strategies and Evaluation Metrics](https://arxiv.org/abs/2505.18658)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f8efb91-93ac-49aa-ba5b-51dc5a602436",
  "isSidechain": false,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "type": "user",
  "uuid": "0a9d8892-0eff-40ed-909a-bb83be2f10c5",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm conducting an adversarial review of a research proposal about training LLMs to be robust to semantic-preserving code mutations for fault localization (identifying which file/function has a bug). The proposal uses contrastive learning (InfoNCE loss) with mutation-augmented training data.\n\nPlease search for competitive and potentially overlooked work:\n\n1. Search \"site:arxiv.org contrastive learning code robustness fault localization 2025 2026\"\n2. Search \"code LLM robustness mutation invariant training 2026 arxiv\"\n3. Search \"semantic preserving code transformation robustness training 2026\"\n4. Search for ContraCode (EMNLP 2021) - \"Contrastive Code Representation Learning\" - verify it exists and targets general pre-training embeddings, not fault localization\n5. Search \"MACL-IRFL multi-view adaptive contrastive learning fault localization 2026\" - verify this exists\n6. Search \"SWE-bench fault localization robustness 2026 arxiv\"\n7. Search \"arXiv 2503.23448 semantic preserving transformations limitations\" - does this paper exist and does it find 59% of transformations change semantics?\n8. Search for any recent (2025-2026) papers on:\n   - \"program transformation augmentation LLM robustness\"\n   - \"code mutation data augmentation fine-tuning robustness\"\n   - \"fault localization contrastive learning\"\n\nReport what you find for each search, including paper titles, venues, and key findings.",
    "agentId": "aca4c7bbcf815a9c8",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me compile the comprehensive report of all findings.\n\n## Comprehensive Competitive Work Analysis Report\n\nI've completed an extensive search for competitive and potentially overlooked work on LLM robustness to semantic-preserving code mutations for fault localization. Here are the key findings:\n\n---\n\n### **1. Direct Competition on Fault Localization Robustness (2026)**\n\n**Primary Competitive Work: \"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models\"**\n- **Venue:** ICST 2026 (IEEE International Conference on Software Testing, Verification and Validation)\n- **ArXiv ID:** [2504.04372](https://arxiv.org/abs/2504.04372)\n- **Key Finding:** 78% failure rate - When semantic-preserving mutations are applied, LLMs fail to localize the same fault they correctly identified previously in 78% of cases\n- **Approach:** Tests LLM fault localization robustness using multiple semantic-preserving mutation types (identifier renaming, comment insertion/modification, formatting changes, dead-code insertion)\n- **Critical Issue:** This directly addresses the core problem your proposal targets and reports empirically that LLMs' fault reasoning is tied to syntactically-irrelevant features\n\n---\n\n### **2. Multi-View Adaptive Contrastive Learning Approach (MACL-IRFL, 2025)**\n\n**Paper:** \"Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization\"\n- **Venue:** Automated Software Engineering journal (published November 6, 2025), also [arXiv 2409.12519](https://arxiv.org/abs/2409.12519)\n- **Publisher:** Springer Nature\n- **Key Innovation:** Uses graph neural networks modeling three views:\n  - Report-code interaction relationships\n  - Report-report similarity relationships  \n  - Code-code co-citation relationships\n- **Results:** Up to 28.93% improvement on Accuracy@1, 25.57% MAP, 20.35% MRR\n- **Approach Similarity:** Uses contrastive learning for fault localization but focuses on multi-view graph modeling rather than mutation-based augmentation\n\n---\n\n### **3. Semantic-Preserving Transformation Limitations (Critical, March 2025)**\n\n**Paper:** \"Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection\"\n- **ArXiv ID:** [2503.23448](https://arxiv.org/abs/2503.23448)\n- **Authors:** Max Hort, Linas Vidziunas, Leon Moonen\n- **Publication Date:** March 30, 2025\n- **CRITICAL FINDING:** **59% of implemented transformations actually change semantics** (23 of 39 transformations changed semantics; only 16 of 39 were truly semantic-preserving)\n- **Implication:** This directly undermines the foundation of mutation-based augmentation approaches - the authors found they could not improve defect detection models even with supposedly semantic-preserving transformations\n- **Conclusion:** \"reusing shared semantic-preserving transformation is difficult, sometimes even causing wrongful changes to the semantics\"\n\n---\n\n### **4. ContraCode (EMNLP 2021) - Foundational Pre-training Work**\n\n**Paper:** \"Contrastive Code Representation Learning\"\n- **Venue:** EMNLP 2021\n- **Authors:** Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica\n- **ArXiv ID:** [2007.04973](https://arxiv.org/abs/2007.04973)\n- **GitHub:** [github.com/parasj/contracode](https://github.com/parasj/contracode)\n- **Key Focus:** General pre-training embeddings using contrastive learning, NOT fault localization\n- **Approach:** Pre-trains on 1.8m JavaScript methods from GitHub using source-to-source compiler transformations to generate functionally similar variants\n- **Results:** 39% AUROC improvement on adversarial code clone detection; 2-13 point improvements on summarization and type inference\n- **Relevance:** Demonstrates that contrastive pre-training on mutation variants improves robustness, but targets general code understanding, not fault localization specifically\n\n---\n\n### **5. Automated Semantic-Preserving Transformations (Auto-SPT, December 2024)**\n\n**Paper:** \"Auto-SPT: Automating Semantic Preserving Transformations for Code\"\n- **ArXiv ID:** [2512.06042](https://arxiv.org/abs/2512.06042)\n- **Venue:** OpenReview (appears to be under review/accepted)\n- **Key Innovation:** Uses LLMs to automatically generate diverse and strong semantic-preserving transformations, addressing the problem that heuristic-based transformations are limited\n- **Results:** Successfully generates more diverse SPTs than existing heuristic approaches; significantly drops performance of code clone detectors when applied\n- **Practical Finding:** Successfully uses Auto-SPT to augment training data and improve robustness of code clone detection models\n- **Relevance:** Provides a potentially more reliable way to generate mutation-augmented training data than manual/heuristic approaches\n\n---\n\n### **6. Code Mutation-Based Robustness Studies (2025-2026)**\n\n**\"Memorize or Generalize? Evaluating LLM Code Generation with Code Rewriting\"**\n- **ArXiv ID:** [2503.02296](https://arxiv.org/abs/2503.02296)\n- **Finding:** Mutation causes moderate performance drops; paraphrase is nearly invariant; rewrites are most disruptive - suggests harmful memorization beyond surface-level robustness\n\n**\"Fine-Tuning LLMs for Code Mutation: A New Era of Cyber Threats\"**\n- **ArXiv ID:** [2410.22293](https://arxiv.org/abs/2410.22293)\n- **Finding:** Explores how fine-tuning LLMs on mutated code creates cybersecurity risks\n\n---\n\n### **7. Data Augmentation Framework Results (AAAI-26, January 2026)**\n\n**\"When Does Data Augmentation Improve Robustness?\"** (accepted AAAI-26)\n- **Key Finding:** Mathematical framework shows data augmentation increases variability and diversity in training data, but the relationship between diversity and robustness is complex and context-dependent\n- **Implication:** Simply augmenting with more mutations doesn't guarantee robustness improvements\n\n---\n\n### **8. Synthetic Data and Fine-tuning Robustness Trade-offs (2025)**\n\n**\"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning\"**\n- **ArXiv ID:** [2511.01490](https://arxiv.org/abs/2511.01490)\n- **Critical Finding:** Synthetic fine-tuning data (including augmented variants) can **decrease adversarial robustness** while preserving output quality\n- **Implication:** Your contrastive learning approach using augmented data must carefully balance robustness gains against potential degradation in other robustness dimensions\n\n---\n\n### **9. Robustness in LLMs - General Survey (2025)**\n\n**\"Robustness in Large Language Models: A Survey of Mitigation Strategies and Evaluation Metrics\"**\n- **ArXiv ID:** [2505.18658](https://arxiv.org/abs/2505.18658)\n- **Published:** 2025\n- **Scope:** Comprehensive survey of robustness techniques; provides context for where mutation-based augmentation fits in the broader landscape\n\n---\n\n## Key Overlaps and Gaps Identified\n\n### Direct Competition:\n1. **ICST 2026 paper (2504.04372)** - Likely the most direct competitor, also studies fault localization robustness to semantic-preserving mutations\n2. **MACL-IRFL** - Different approach (multi-view graphs) but same fault localization problem domain\n\n### Critical Vulnerabilities in Your Approach:\n1. **arXiv 2503.23448** - Demonstrates that 59% of \"semantic-preserving\" transformations actually change semantics, undermining the foundation of mutation-augmented training\n2. **arXiv 2511.01490** - Shows synthetic augmented data can degrade adversarial robustness in fine-tuning\n3. **The 78% failure rate (ICST 2026)** - Shows the scale of the problem is severe; contrastive learning with current mutation approaches may not solve this\n\n### Potentially Overlooked Opportunities:\n1. **Auto-SPT** - Could improve your mutation generation quality by using LLM-based transformation generation rather than heuristic/manual approaches\n2. **ContraCode pre-training** - Your work could build on ContraCode's general pre-training approach but adapt it specifically for fault localization\n3. **Multi-view contrastive approaches** - MACL-IRFL suggests that modeling multiple relationship types (not just code-fault pairs) could improve results\n\n---\n\n## Summary Assessment\n\nYour proposal directly addresses a critical gap identified in ICST 2026 (the 78% robustness failure), and uses a promising technique (contrastive learning with InfoNCE loss). However, you face substantial competitive and methodological challenges:\n\n- **Direct competitor:** ICST 2026 paper already quantifies the problem you're solving\n- **Methodological risk:** arXiv 2503.23448 shows 59% of supposedly semantic-preserving transformations actually change semantics—this is a fundamental threat to mutation-based augmentation approaches\n- **Data augmentation risk:** Recent work shows synthetic augmentation can paradoxically reduce robustness\n- **Potential mitigation:** Adopt LLM-based transformation generation (Auto-SPT) and consider multi-view contrastive approaches (MACL-IRFL model)\n\nSources:\n- [Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (ICST 2026)](https://arxiv.org/abs/2504.04372)\n- [Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization](https://arxiv.org/abs/2409.12519)\n- [Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection](https://arxiv.org/abs/2503.23448)\n- [Contrastive Code Representation Learning (ContraCode)](https://arxiv.org/abs/2007.04973)\n- [Auto-SPT: Automating Semantic Preserving Transformations for Code](https://arxiv.org/abs/2512.06042)\n- [Memorize or Generalize? Evaluating LLM Code Generation with Code Rewriting](https://arxiv.org/abs/2503.02296)\n- [Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning](https://arxiv.org/abs/2511.01490)\n- [Robustness in Large Language Models: A Survey of Mitigation Strategies and Evaluation Metrics](https://arxiv.org/abs/2505.18658)"
      }
    ],
    "totalDurationMs": 56115,
    "totalTokens": 30689,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 27714,
      "output_tokens": 2696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 273
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2696,
          "cache_read_input_tokens": 27714,
          "cache_creation_input_tokens": 273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 273,
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
  "sourceToolAssistantUUID": "2f8efb91-93ac-49aa-ba5b-51dc5a602436",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
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
  "leafUuid": "0a9d8892-0eff-40ed-909a-bb83be2f10c5",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "SeMutFL: Training Fault Localization Robustness via Semantic Mutation Augmentation",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd"
}
```

---

### Tool result

_source line 15 · 2026-05-10T06:27:20.812Z_

<details><summary>↩ Tool result · `toolu_01Gw4r1vWYRKPdqGz8GCy2rq`</summary>

```text
Excellent. Now let me compile my findings into a comprehensive report for the user.

## Adversarial Review: Verification of Claims in "SeMutFL" Proposal

Based on my comprehensive search of arXiv and academic databases, here are my findings for each claim:

---

### 1. **arXiv 2504.04372 - "Assessing the Impact of Code Changes on the Fault Localizability"**

**Status: VERIFIED**

- **Existence**: Paper exists and was accepted at ICST 2026.
- **78% failure rate claim**: CONFIRMED. The paper reports that semantic-preserving mutations (SPMs) cause LLMs to fail to localize the same fault they correctly localized earlier in **78% of cases**.
- **Scope**: Evaluated 10 state-of-the-art LLMs on ~1,300 Java and Python programs, generating 750,013 unique faulty programs.

**Sources:**
- [arXiv 2504.04372 Abstract](https://arxiv.org/abs/2504.04372)
- [ICST 2026 Conference Paper](https://conf.researchr.org/details/icst-2026/icst-2026-research/30/Assessing-the-Impact-of-Code-Changes-on-the-Fault-Localizability-of-Large-Language-Mo)

---

### 2. **arXiv 2505.10443 - "Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?"**

**Status: PARTIALLY VERIFIED (with clarifications needed)**

- **Existence**: Paper exists.
- **Performance drops up to 70%**: CONFIRMED. Abstract states "performance drops reaching up to 70%."
- **Nine LLMs tested**: CONFIRMED. The study evaluated nine LLMs:
  - **Open-source**: CodeGemma (7B), GraniteCode (8B), Mistral (7B), Qwen2.5-Coder (7B), Qwen3-Coder (30B), SemCoder (7B), Llama3.2 (3B)
  - **Proprietary**: GPT-5.2, Gemini-3

- **Specific performance drops (LiveCodeBench, loop unrolling mutation)**:
  - Gemini-3: **−70.4 percentage points** (highest reported)
  - GPT-5.2: −68.1 points
  - Qwen2.5-Coder: −44.3 points
  - Qwen3-Coder: −35.1 points
  - Others: ranging from −22.1 to −32.8 points

**Important clarification**: The paper measures models' reasoning soundness (10-50% of correct answers derived from flawed logic) rather than purely performance degradation percentages across all mutations.

**Sources:**
- [arXiv 2505.10443 Abstract](https://arxiv.org/abs/2505.10443)
- [Full Paper HTML](https://arxiv.org/html/2505.10443)

---

### 3. **arXiv 2601.18044 - RGFL "Reasoning Guided Fault Localization"**

**Status: VERIFIED (with important clarification)**

- **Existence**: Paper exists.
- **Hit@1 claim (85%)**: PARTIALLY CONFIRMED, but context matters. The paper reports:
  - **File-level Hit@1**: Improves from 71.4% to **85%** (confirmed)
  - **File-level MRR**: Improves from 81.8% to 88.8%
  - **Element-level Exact Match@3**: Increases from 36% to 69%

**Important clarification**: The 85% is specifically for file-level Hit@1 on SWE-bench Verified, not a general performance metric. The method shows hierarchical improvements at different granularity levels.

**Sources:**
- [arXiv 2601.18044 Abstract](https://arxiv.org/abs/2601.18044)
- [Full Paper](https://arxiv.org/html/2601.18044)

---

### 4. **arXiv 2602.11411 - "Improving the Robustness of LLMs for Code Tasks via Fine-tuning with Perturbed Data"**

**Status: VERIFIED (with important distinction)**

- **Existence**: Paper exists.
- **Perturbation types**: CONFIRMED. The paper applies NLP-level perturbations (NOT semantic-preserving code mutations):

  **Character-level (C1-C3)**:
  - ButterFingers: Random character insertions/typos
  - SwapCharacters: Character swaps within words
  - ChangeCharCase: Case modifications

  **Word-level (W1-W3)**:
  - SynonymInsertion: Insertion of synonyms
  - SynonymSubstitution: Replacement with synonyms
  - InflectionalVariation: Word inflection changes

  **Sentence-level (S1-S3)**:
  - BackTranslation: Round-trip translation
  - TenseTransformationPast: Conversion to past tense
  - TenseTransformationFuture: Conversion to future tense

**Critical distinction**: This paper uses NLP-style perturbations (typos, synonyms, back-translation), NOT semantic-preserving code mutations like variable renaming, control flow transformations, or dead code insertion.

**Sources:**
- [arXiv 2602.11411 Abstract](https://arxiv.org/abs/2602.11411)
- [Full Paper HTML](https://arxiv.org/html/2602.11411)

---

### 5. **NEW Papers from March-May 2026 on Surface-Form Robustness**

**Status: LARGELY NEGATIVE SEARCH RESULTS**

I conducted extensive searches using multiple query combinations:
- "fault localization robustness contrastive 2026"
- "semantic mutation augmentation code LLM 2026"
- "code understanding surface-form invariance training 2026"
- "surface-form robust fault localization LLM 2026"

**Key findings:**

1. **No explicit "SeMutFL" paper found**: A paper with the exact title "SeMutFL: Contrastive Mutation Augmentation for Surface-Form Robust Code Understanding in Fault Localization" does not appear in arXiv search results.

2. **Related work from early 2026**:
   - arXiv 2504.04372 (ICST 2026): Semantic-preserving mutations for robustness evaluation
   - arXiv 2506.17369 ("Re-Evaluating Code LLM Benchmarks Under Semantic Mutation"): June 2025, addresses semantic mutations
   - arXiv 2510.23208: "Increasing LLM Coding Capabilities through Diverse Synthetic Coding Tasks" (October 2025): Uses genetic instruction mutation

3. **No papers specifically combining "contrastive mutation" + "surface-form robustness" in fault localization**: The searches returned related work on mutation-based fault localization and contrastive learning separately, but not the specific combination described in your proposal title.

**Sources:**
- [arXiv Fault Localization Search Results](https://arxiv.org/search/?query=fault+localization+contrastive+mutation&searchtype=all)
- [Multi-View Adaptive Contrastive Learning (2409.12519)](https://arxiv.org/html/2409.12519)

---

### 6. **SWE-Gym (arXiv 2412.21139) - Training Configuration Verification**

**Status: VERIFIED**

- **Paper exists**: Yes, published at ICLR 2025.

- **Table 8 statistics - CONFIRMED**:
  - **491 trajectories**: Confirmed (491 resolved successful trajectories)
  - **18,578 average tokens**: CONFIRMED (18,578.5 tokens per trajectory)
  - **Additional metrics in Table 8**:
    - 39.9 LM completion messages per trajectory (~19 turns)
    - Token range: 2,560 to 81,245 tokens

- **Hardware and LoRA configuration - CONFIRMED**:
  - **Model**: Qwen-2.5-Coder (7B, 14B, 32B variants)
  - **Hardware**: 2-8x NVIDIA H100 80G GPUs on Modal
  - **LoRA training specifics** (for 32B verifier):
    - LoRA rank: 64
    - Learning rate: 5×10⁻⁴
    - Max epochs: 2
    - Uses Unsloth library
  - **Standard fine-tuning** (for policy):
    - Learning rate: 1e-4
    - Epochs: 5 maximum
    - Global batch size: 8
    - Max context length: 32,768 tokens

**Sources:**
- [SWE-Gym arXiv 2412.21139](https://arxiv.org/abs/2412.21139)
- [SWE-Gym HTML Version](https://arxiv.org/html/2412.21139v1)
- [Official Paper PDF](https://nlp.cs.berkeley.edu/pubs/Pan-Wang-Neubig-Jaitly-Ji-Suhr-Zhang_2025_SWEGym_paper.pdf)

---

## Summary for Adversarial Review

**Key findings for your proposal evaluation:**

1. ✓ The motivation papers (2504.04372, 2505.10443) with the claimed failure rates **do exist and are verified**.
2. ✓ RGFL (2601.18044) with 85% Hit@1 on SWE-bench **is verified** (file-level metric).
3. ✓ Paper 2602.11411 **exists but applies NLP perturbations, NOT semantic-preserving code mutations** — this is a critical distinction that undermines any claim it's a direct baseline.
4. ✗ **No existing "SeMutFL" paper** with "Contrastive Mutation Augmentation for Surface-Form Robust Code Understanding" appears in March-May 2026 literature.
5. ✓ SWE-Gym table and configuration **fully verified**.

**Critical gap**: Your proposal's novelty claim hinges on the absence of prior work combining contrastive learning with semantic-preserving mutations for fault localization robustness. The search found ample work on each component separately (2504.04372 uses semantic mutations, MACL-IRFL uses contrastive learning), but no prior work combining both specifically for surface-form robustness in fault localization—which would support your proposal's novelty claim if the SeMutFL approach is genuinely new.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bd75308-5fef-4190-8845-2ff788d8a977",
  "isSidechain": false,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "type": "user",
  "uuid": "4a153edf-653e-466d-85d6-00fd049d699a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm conducting an adversarial review of a research proposal called \"SeMutFL: Contrastive Mutation Augmentation for Surface-Form Robust Code Understanding in Fault Localization.\" I need you to search for and verify several claims. Please conduct the following searches and report what you find:\n\n1. Search for arXiv paper 2504.04372 - \"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models\" - does it exist and does it report a 78% failure rate under semantic-preserving mutations?\n\n2. Search for arXiv paper 2505.10443 - \"Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?\" - does it exist and does it show performance drops up to 70% across nine LLMs?\n\n3. Search for RGFL (arXiv 2601.18044) - \"Reasoning Guided Fault Localization for LLM-Based Automated Program Repair\" - does it exist and does it report 85% Hit@1 on SWE-bench Verified?\n\n4. Search for arXiv 2602.11411 - \"Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data\" - does it exist and does it apply NLP-level perturbations (typos, synonyms, back-translation) rather than semantic-preserving code mutations?\n\n5. Search for any NEW papers from March-May 2026 that address surface-form robustness in fault localization via contrastive learning or mutation augmentation for LLMs. Try searches like:\n   - \"fault localization robustness contrastive 2026\"\n   - \"semantic mutation augmentation code LLM 2026\"\n   - \"code understanding surface-form invariance training 2026\"\n   - site:arxiv.org \"fault localization\" \"contrastive\" \"mutation\" 2026\n\n6. Search for SWE-Gym (arXiv 2412.21139) - specifically verify: does it describe training with 491 trajectories × 18,578 avg tokens for 32B LoRA on H100 hardware? Does Table 8 contain these token statistics?\n\nReport findings concisely for each item.",
    "agentId": "a3f1dbc964cde1dc5",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent. Now let me compile my findings into a comprehensive report for the user.\n\n## Adversarial Review: Verification of Claims in \"SeMutFL\" Proposal\n\nBased on my comprehensive search of arXiv and academic databases, here are my findings for each claim:\n\n---\n\n### 1. **arXiv 2504.04372 - \"Assessing the Impact of Code Changes on the Fault Localizability\"**\n\n**Status: VERIFIED**\n\n- **Existence**: Paper exists and was accepted at ICST 2026.\n- **78% failure rate claim**: CONFIRMED. The paper reports that semantic-preserving mutations (SPMs) cause LLMs to fail to localize the same fault they correctly localized earlier in **78% of cases**.\n- **Scope**: Evaluated 10 state-of-the-art LLMs on ~1,300 Java and Python programs, generating 750,013 unique faulty programs.\n\n**Sources:**\n- [arXiv 2504.04372 Abstract](https://arxiv.org/abs/2504.04372)\n- [ICST 2026 Conference Paper](https://conf.researchr.org/details/icst-2026/icst-2026-research/30/Assessing-the-Impact-of-Code-Changes-on-the-Fault-Localizability-of-Large-Language-Mo)\n\n---\n\n### 2. **arXiv 2505.10443 - \"Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?\"**\n\n**Status: PARTIALLY VERIFIED (with clarifications needed)**\n\n- **Existence**: Paper exists.\n- **Performance drops up to 70%**: CONFIRMED. Abstract states \"performance drops reaching up to 70%.\"\n- **Nine LLMs tested**: CONFIRMED. The study evaluated nine LLMs:\n  - **Open-source**: CodeGemma (7B), GraniteCode (8B), Mistral (7B), Qwen2.5-Coder (7B), Qwen3-Coder (30B), SemCoder (7B), Llama3.2 (3B)\n  - **Proprietary**: GPT-5.2, Gemini-3\n\n- **Specific performance drops (LiveCodeBench, loop unrolling mutation)**:\n  - Gemini-3: **−70.4 percentage points** (highest reported)\n  - GPT-5.2: −68.1 points\n  - Qwen2.5-Coder: −44.3 points\n  - Qwen3-Coder: −35.1 points\n  - Others: ranging from −22.1 to −32.8 points\n\n**Important clarification**: The paper measures models' reasoning soundness (10-50% of correct answers derived from flawed logic) rather than purely performance degradation percentages across all mutations.\n\n**Sources:**\n- [arXiv 2505.10443 Abstract](https://arxiv.org/abs/2505.10443)\n- [Full Paper HTML](https://arxiv.org/html/2505.10443)\n\n---\n\n### 3. **arXiv 2601.18044 - RGFL \"Reasoning Guided Fault Localization\"**\n\n**Status: VERIFIED (with important clarification)**\n\n- **Existence**: Paper exists.\n- **Hit@1 claim (85%)**: PARTIALLY CONFIRMED, but context matters. The paper reports:\n  - **File-level Hit@1**: Improves from 71.4% to **85%** (confirmed)\n  - **File-level MRR**: Improves from 81.8% to 88.8%\n  - **Element-level Exact Match@3**: Increases from 36% to 69%\n\n**Important clarification**: The 85% is specifically for file-level Hit@1 on SWE-bench Verified, not a general performance metric. The method shows hierarchical improvements at different granularity levels.\n\n**Sources:**\n- [arXiv 2601.18044 Abstract](https://arxiv.org/abs/2601.18044)\n- [Full Paper](https://arxiv.org/html/2601.18044)\n\n---\n\n### 4. **arXiv 2602.11411 - \"Improving the Robustness of LLMs for Code Tasks via Fine-tuning with Perturbed Data\"**\n\n**Status: VERIFIED (with important distinction)**\n\n- **Existence**: Paper exists.\n- **Perturbation types**: CONFIRMED. The paper applies NLP-level perturbations (NOT semantic-preserving code mutations):\n\n  **Character-level (C1-C3)**:\n  - ButterFingers: Random character insertions/typos\n  - SwapCharacters: Character swaps within words\n  - ChangeCharCase: Case modifications\n\n  **Word-level (W1-W3)**:\n  - SynonymInsertion: Insertion of synonyms\n  - SynonymSubstitution: Replacement with synonyms\n  - InflectionalVariation: Word inflection changes\n\n  **Sentence-level (S1-S3)**:\n  - BackTranslation: Round-trip translation\n  - TenseTransformationPast: Conversion to past tense\n  - TenseTransformationFuture: Conversion to future tense\n\n**Critical distinction**: This paper uses NLP-style perturbations (typos, synonyms, back-translation), NOT semantic-preserving code mutations like variable renaming, control flow transformations, or dead code insertion.\n\n**Sources:**\n- [arXiv 2602.11411 Abstract](https://arxiv.org/abs/2602.11411)\n- [Full Paper HTML](https://arxiv.org/html/2602.11411)\n\n---\n\n### 5. **NEW Papers from March-May 2026 on Surface-Form Robustness**\n\n**Status: LARGELY NEGATIVE SEARCH RESULTS**\n\nI conducted extensive searches using multiple query combinations:\n- \"fault localization robustness contrastive 2026\"\n- \"semantic mutation augmentation code LLM 2026\"\n- \"code understanding surface-form invariance training 2026\"\n- \"surface-form robust fault localization LLM 2026\"\n\n**Key findings:**\n\n1. **No explicit \"SeMutFL\" paper found**: A paper with the exact title \"SeMutFL: Contrastive Mutation Augmentation for Surface-Form Robust Code Understanding in Fault Localization\" does not appear in arXiv search results.\n\n2. **Related work from early 2026**:\n   - arXiv 2504.04372 (ICST 2026): Semantic-preserving mutations for robustness evaluation\n   - arXiv 2506.17369 (\"Re-Evaluating Code LLM Benchmarks Under Semantic Mutation\"): June 2025, addresses semantic mutations\n   - arXiv 2510.23208: \"Increasing LLM Coding Capabilities through Diverse Synthetic Coding Tasks\" (October 2025): Uses genetic instruction mutation\n\n3. **No papers specifically combining \"contrastive mutation\" + \"surface-form robustness\" in fault localization**: The searches returned related work on mutation-based fault localization and contrastive learning separately, but not the specific combination described in your proposal title.\n\n**Sources:**\n- [arXiv Fault Localization Search Results](https://arxiv.org/search/?query=fault+localization+contrastive+mutation&searchtype=all)\n- [Multi-View Adaptive Contrastive Learning (2409.12519)](https://arxiv.org/html/2409.12519)\n\n---\n\n### 6. **SWE-Gym (arXiv 2412.21139) - Training Configuration Verification**\n\n**Status: VERIFIED**\n\n- **Paper exists**: Yes, published at ICLR 2025.\n\n- **Table 8 statistics - CONFIRMED**:\n  - **491 trajectories**: Confirmed (491 resolved successful trajectories)\n  - **18,578 average tokens**: CONFIRMED (18,578.5 tokens per trajectory)\n  - **Additional metrics in Table 8**:\n    - 39.9 LM completion messages per trajectory (~19 turns)\n    - Token range: 2,560 to 81,245 tokens\n\n- **Hardware and LoRA configuration - CONFIRMED**:\n  - **Model**: Qwen-2.5-Coder (7B, 14B, 32B variants)\n  - **Hardware**: 2-8x NVIDIA H100 80G GPUs on Modal\n  - **LoRA training specifics** (for 32B verifier):\n    - LoRA rank: 64\n    - Learning rate: 5×10⁻⁴\n    - Max epochs: 2\n    - Uses Unsloth library\n  - **Standard fine-tuning** (for policy):\n    - Learning rate: 1e-4\n    - Epochs: 5 maximum\n    - Global batch size: 8\n    - Max context length: 32,768 tokens\n\n**Sources:**\n- [SWE-Gym arXiv 2412.21139](https://arxiv.org/abs/2412.21139)\n- [SWE-Gym HTML Version](https://arxiv.org/html/2412.21139v1)\n- [Official Paper PDF](https://nlp.cs.berkeley.edu/pubs/Pan-Wang-Neubig-Jaitly-Ji-Suhr-Zhang_2025_SWEGym_paper.pdf)\n\n---\n\n## Summary for Adversarial Review\n\n**Key findings for your proposal evaluation:**\n\n1. ✓ The motivation papers (2504.04372, 2505.10443) with the claimed failure rates **do exist and are verified**.\n2. ✓ RGFL (2601.18044) with 85% Hit@1 on SWE-bench **is verified** (file-level metric).\n3. ✓ Paper 2602.11411 **exists but applies NLP perturbations, NOT semantic-preserving code mutations** — this is a critical distinction that undermines any claim it's a direct baseline.\n4. ✗ **No existing \"SeMutFL\" paper** with \"Contrastive Mutation Augmentation for Surface-Form Robust Code Understanding\" appears in March-May 2026 literature.\n5. ✓ SWE-Gym table and configuration **fully verified**.\n\n**Critical gap**: Your proposal's novelty claim hinges on the absence of prior work combining contrastive learning with semantic-preserving mutations for fault localization robustness. The search found ample work on each component separately (2504.04372 uses semantic mutations, MACL-IRFL uses contrastive learning), but no prior work combining both specifically for surface-form robustness in fault localization—which would support your proposal's novelty claim if the SeMutFL approach is genuinely new."
      }
    ],
    "totalDurationMs": 89130,
    "totalTokens": 37572,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4615,
      "cache_read_input_tokens": 30328,
      "output_tokens": 2622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4615
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2622,
          "cache_read_input_tokens": 30328,
          "cache_creation_input_tokens": 4615,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4615,
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
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "9bd75308-5fef-4190-8845-2ff788d8a977",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T06:29:06.411Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the independent verification results. Let me now analyze what I've found and assess the proposal:

**Key findings from my independent verification:**

1. **arXiv 2504.04372** - VERIFIED. The 78% failure rate claim is confirmed. Paper exists.

2. **arXiv 2505.10443** - VERIFIED. Performance drops up to 70% across nine LLMs confirmed.

3. **RGFL (arXiv 2601.18044)** - VERIFIED. 85% file-level Hit@1 on SWE-bench Verified confirmed.


4. **arXiv 2602.11411** - VERIFIED. The perturbation approach uses NLP-level techniques like typos and back-translation rather than semantic-preserving mutations, validating the differentiation claims.

5. **SWE-Gym (arXiv 2412.21139)** - VERIFIED. Context window of 32,768 tokens with 2-8 H100 GPUs, and the round 5 correction has been properly incorporated.

6. **arXiv 2503.23448** - VERIFIED. The 59% implementation failure rate is confirmed and properly cited in the proposal.

I found Auto-SPT generates semantic-preserving transformations for code clone detection, which is tangential rather than directly competitive. Now checking the resource estimates in the proposal—SWE-Gym's training calculation is correct at 45.5M tokens across 491 trajectories with the proper context length and hardware specifications confirmed.

For novelty, the contrastive learning approach combined with semantic-preserving mutations for fault localization is genuinely novel, even though the individual components are established. The closest related work uses either NLP perturbations with standard fine-tuning or graph-based contrastive learning without mutation augmentation, so the specific combination fills a real gap. Feasibility looks solid with the corrected SWE-Gym citation and budget arithmetic checks out.

Now I'm verifying the computational requirements—the training and evaluation costs come in well under the 200 H100-hour ceiling even in the worst case scenario. The model choice is sound, datasets are publicly available, and the mutation validity concern has been addressed through test-suite equivalence checking. The main remaining uncertainty is the per-run time estimate, which I've acknowledged could vary by ±50%, but that's acceptable given the explicit reasoning behind it.

The proposal scores well on clarity and impact—it's well-structured with a clear problem statement, concrete approach combining contrastive learning with mutation augmentation, and a thorough evaluation plan including ablations and downstream effects. This directly tackles a documented weakness in fault localization and aligns with EMNLP's focus on robustness. The one remaining issue about SWE-Gym factual accuracy has been resolved.

Now I'm checking whether there are any lingering concerns. The training time estimate is properly framed now with honest uncertainty—it's based on first-principles calculations with a ±50% variance buffer, which is the right way to handle unpublished benchmarks. I'm also noticing Auto-SPT (arXiv 2512.06042) as a potentially relevant paper that generates semantic-preserving transformations, though it targets code clones rather than fault localization, so it's more of a tangential reference than a direct competitor. The core question is whether the round 5 fix fully addresses the remaining feedback, and it appears to have done so.

Now I need to correct the SWE-Gym anchor. The resource estimate incorrectly claims a 10,240-token context length on a single H100, but the paper actually specifies 32,768 max context length across 2-8 H100s. The right approach is to cite the actual numbers from Table 8—491 trajectories with 18,578 average tokens per trajectory across 5 epochs gives 45.5M total training tokens for the 32B LoRA run. I should drop the context length specification entirely and the single-GPU framing, then rely on the first-principles throughput calculation for the 22-hour estimate.

The key risk I need to flag is that no published benchmark directly measures QLoRA timing for 30B+ models on 2×A100-80GB hardware, so the ±50% variance is the appropriate safety margin.

For the auto_research GPU budget, I'm looking at roughly 254 A100-80GB hours total, which translates to about 127 H100-equivalent hours at 2× speedup—comfortably under the 200 H100-hour ceiling. The breakdown is: four ablation runs at 2×A100 for ~22 hours each equals 176 A100-hours, SWE-bench evaluation at ~35 hours on 2×A100 adds 70 A100-hours, and mutation data generation plus test-suite equivalence validation takes another ~8 A100-hours. Even with a worst-case 50% training variance, the total stays manageable.

The ~22-hour-per-run estimate comes from first principles: SWE-Gym's 491 trajectories with 18,578 average tokens per trajectory across 5 epochs yields 45.5M total training tokens for 32B LoRA fine-tuning at the full 32,768 context length on 2-8 H100 80G GPUs. Since there's no direct published benchmark for this specific hardware and model size combination, I'm grounding the calculation entirely in first-principles throughput analysis.

The proposal has now been refined through multiple rounds and addresses all previous concerns. The novelty is solid—this is the first method combining surface-form robustness with InfoNCE loss specifically for fault localization, with a well-documented gap and clear differentiation from related work. The feasibility checks out too: the compute budget is tight but grounded in realistic first-principles estimates with appropriate uncertainty margins, and it stays within the 200 H100-hour ceiling.

The writing is clear and well-supported throughout, with concrete methods and explicit positioning relative to existing approaches. The problem itself carries real weight—a 78% failure rate in current methods, alignment with EMNLP 2026's robustness theme, and potential to bridge the gap between diagnostic and prescriptive approaches in program repair. All the critical issues from previous rounds have been resolved, and no new problems have surfaced. This looks ready to move forward.

I'm noticing a potential inconsistency in the resource estimates though. The SWE-bench evaluation is budgeted at 35 hours on 2×A100 GPUs, but that 70 A100-hour figure doesn't get the ±50% variance applied in the worst-case calculation like other components do. It seems intentional—evaluation time is more predictable than training—but I should verify whether 35 hours is actually realistic for SWE-bench Verified's ~500 instances, especially given the patch generation and test execution overhead involved.

The mutation data generation and test-suite equivalence validation at 8 A100-hours also seems potentially underestimated. With Defects4J's ~395 bugs and SWE-bench Verified's ~500 instances, generating 4-5 mutations per bug creates thousands of program-mutation pairs that each need test suite verification. Even if the GPU hours only account for the LLM-based components and the actual test execution runs on CPU, the total wall-clock time could stretch significantly longer than anticipated.

Looking at the evaluation breakdown more carefully, the 35 A100-hours for SWE-bench evaluation appears to be for LLM inference during localization generation, while the CPU-bound test suite execution for equivalence checking would be separate. Overall, the fix was correctly applied, previous issues have been addressed, there are no critical new problems, and the compute, venue, novelty, and feasibility all check out—so this seems ready to move forward. The proposal has been through multiple revision cycles addressing specific issues, and the latest round correctly fixed the SWE-Gym citation problem. My verification confirms no critical competitive work was missed, the budget is consistent, and the differentiation from related work holds up—the Auto-SPT paper is methodologically relevant but not a direct competitor since it targets code clone detection rather than fault localization. I think this is ready to pass. I'm settling on a 4.0 average score and a pass verdict, though I should push back more critically here. The novelty is real but incremental—while ContraCode already combines contrastive learning with mutation augmentation, this work's specific application to fault localization with targeted labels does fill a genuine gap. The feasibility still hinges on that 22-hour runtime estimate, which even with reasonable variance could be problematic if it runs significantly longer.

The bigger issue is that this is a fairly narrow fault localization paper for EMNLP, and there's no guarantee the robustness gains will actually improve downstream repair—though they're testing that causal chain, which is good. The 78% failure rate comes from a limited diagnostic study, so the real-world impact remains uncertain. That said, it does align well with EMNLP's trust theme, and the concerns aren't blocking.

Weighing everything together, this feels like a solid incremental contribution with clear methodology and appropriate scope. The compute is justified, the venue fits, and five rounds of revision show real refinement. I'm settling on 4/5 across novelty, feasibility, clarity, and impact—that's a pass with no critical flaws. So I'm settling on 4/4/4/4 for a solid pass. Let me break down my reasoning more carefully across each dimension. Novelty is clearly a 4 — the specific pairing of contrastive learning with mutation-based augmentation for fault localization fine-tuning hasn't been done before, even though the individual pieces are established. The combination meaningfully addresses a documented gap. For feasibility, I'm working through the compute requirements: the ablation studies and training runs are well within budget at around 176 A100-hours, and while the SWE-bench evaluation estimate is a bit loose, it's not unreasonable. Now I need to think through the remaining dimensions and whether this truly qualifies as outstanding or just solid work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a153edf-653e-466d-85d6-00fd049d699a",
  "isSidechain": false,
  "requestId": "req_011CatQwTSd9PPjZLQ2qTzCT",
  "type": "assistant",
  "uuid": "f966f597-566b-47a5-9031-783c7ce23d02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TuYYv8SwyoM1oCGraBN46d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2722,
      "cache_creation_input_tokens": 5121,
      "cache_read_input_tokens": 32316,
      "output_tokens": 5307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2722,
          "output_tokens": 5307,
          "cache_read_input_tokens": 32316,
          "cache_creation_input_tokens": 5121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5121
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

_source line 17 · 2026-05-10T06:29:06.659Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WWdeSnRVZqfhWd3aDsFLUu`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f966f597-566b-47a5-9031-783c7ce23d02",
  "isSidechain": false,
  "requestId": "req_011CatQwTSd9PPjZLQ2qTzCT",
  "type": "assistant",
  "uuid": "94cf1e46-1c93-4215-a345-1b11fb7a9a07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TuYYv8SwyoM1oCGraBN46d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2722,
      "cache_creation_input_tokens": 5121,
      "cache_read_input_tokens": 32316,
      "output_tokens": 5307,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5121,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2722,
          "output_tokens": 5307,
          "cache_read_input_tokens": 32316,
          "cache_creation_input_tokens": 5121,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5121
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

_source line 18 · 2026-05-10T06:29:06.667Z_

<details><summary>↩ Tool result · `toolu_01WWdeSnRVZqfhWd3aDsFLUu`</summary>

````text
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
  "parentUuid": "94cf1e46-1c93-4215-a345-1b11fb7a9a07",
  "isSidechain": false,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "type": "user",
  "uuid": "ee10af32-1b45-486b-90b9-41218d094e18",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "94cf1e46-1c93-4215-a345-1b11fb7a9a07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ee10af32-1b45-486b-90b9-41218d094e18",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "SeMutFL: Training Fault Localization Robustness via Semantic Mutation Augmentation",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd"
}
```

---

### Assistant

_source line 21 · 2026-05-10T06:29:31.735Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me verify one more important paper - the SWE-Gym paper to make sure the round 5 fix is verified correctly, and also check arXiv 2602.11411 more carefully to ensure the differentiation claims are accurate.

Actually, the search agents have already verified:
1. SWE-Gym: 491 trajectories × 18,578 avg tokens (Table 8) × 5 epochs, max context length 32,768, 2-8 NVIDIA H100 80G GPUs ✓
2. arXiv 2602.11411: Uses NLP-level perturbations (typos, synonyms, back-translation), NOT semantic-preserving code mutations ✓


3. All key papers verified and no new competitive work found that would undermine the novelty claims, so I have what I need to write up the verdict.

The SWE-Gym anchor fix in round 5 is correct—it now properly specifies 32,768 token context on 2-8 H100s instead of the previous 10,240 claim on a single GPU, and acknowledges the ±50% variance in the first-principles throughput calculation. All six prior issues have been systematically addressed: the venue, model size, RGFL comparison, NLP framing, differentiation from the related arXiv work, budget arithmetic, and mutation validity checks.

I've also verified that the key papers cited actually exist and support the claimed findings, and while Auto-SPT is a related work using LLMs for mutation generation, it targets code clone detection rather than fault localization, so it doesn't directly threaten the novelty here. The paper passes overall, with novelty scoring at 4/5 for introducing the first training method for surface-form robustness in this context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee10af32-1b45-486b-90b9-41218d094e18",
  "isSidechain": false,
  "requestId": "req_011CatR5HBCzsNsxroZfhoPj",
  "type": "assistant",
  "uuid": "28076bb7-6ad5-4871-aaac-759aaed8d437",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EhK29mKQA1KE9cVr7aeKSK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8528,
      "cache_read_input_tokens": 37437,
      "output_tokens": 1939,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1939,
          "cache_read_input_tokens": 37437,
          "cache_creation_input_tokens": 8528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8528
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

_source line 22 · 2026-05-10T06:29:54.193Z_

Based on my independent verification, I now have sufficient information to render a verdict. Here is my assessment:

```json
{
  "verdict": "pass",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "The combination of InfoNCE contrastive loss with semantic-preserving mutation augmentation specifically for fault localization fine-tuning is genuinely novel — independently confirmed: no paper combines these for FL robustness training. arXiv 2602.11411 (the closest methodological predecessor) independently verified to use NLP-level perturbations (typos, synonyms, back-translation), not semantic-preserving code mutations, and applies standard SFT without contrastive objective. The differentiation is real and survives scrutiny."
    },
    "feasibility": {
      "score": 4,
      "rationale": "Round 5 fix correctly applied: SWE-Gym anchor now states max context length 32,768 on 2-8 NVIDIA H100 80G GPUs (not 10,240 / single H100), and the estimate explicitly notes no published QLoRA benchmark for 30B+ on 2×A100-80GB exists. Worst-case budget of 342 A100-hours ≈ 171 H100-hours is genuinely under the 200-hour ceiling; 4-ablation structure and ±50% variance framing are correct risk mitigation."
    },
    "clarity": {
      "score": 4,
      "rationale": "All five rounds of key claims — differentiation from arXiv 2602.11411, RGFL fallback, stratified inclusion rates, MACL-IRFL framing, ablation justification — are specific, accurate, and independently verifiable. The evaluation plan is concrete with metrics, fallback conditions, and explicit scope limitations."
    },
    "impact": {
      "score": 4,
      "rationale": "The problem is well-quantified by two independent diagnostic studies (78% FL failure rate from ICST 2026, up to 70% drop across nine LLMs from arXiv 2505.10443), both verified correct. Closing the diagnostic-to-prescriptive loop on an EMNLP 2026 robustness-theme track with a compute-feasible empirical method is a genuine contribution."
    }
  },
  "issues": [
    "MARGINAL — SWE-BENCH EVALUATION TIME UNGROUNDED: The '35h × 2×A100 = 70 A100-hours' estimate for SWE-bench Verified evaluation is the second-largest budget item after training but has no first-principles derivation or citation — unlike the carefully grounded 22h training estimate. At ~500 instances, if each requires LLM localization inference plus test harness interaction, 35h could be tight or loose by a factor of 2. This does not affect the budget ceiling (worst-case total remains 171 H100-hours) but a single-sentence derivation would prevent reviewer questions.",
    "MINOR — AUTO-SPT (arXiv 2512.06042) IS UNCITED: A December 2024 paper ('Auto-SPT: Automating Semantic Preserving Transformations for Code') uses LLMs to generate semantic-preserving transformations and demonstrates augmented training improves robustness for code clone detection. It is not a direct competitor (different task, no contrastive loss, no FL), but reviewers familiar with it may expect acknowledgment of LLM-based mutation generation as an alternative to the heuristic operators in SeMutFL. A brief citation noting it targets code clone detection (not FL) and uses LLM generation rather than AST-based operators would preempt the question."
  ],
  "feedback": "The proposal is ready. The two remaining issues are marginal: (1) add a sentence grounding the 35h SWE-bench evaluation estimate (e.g., '500 instances × ~250 tokens/sec inference on 2×A100 ≈ X hours'); (2) cite Auto-SPT (arXiv 2512.06042) in the landscape section with a one-line note that it targets code clone detection with LLM-generated mutations rather than fault localization with AST-based operators. Neither issue affects the scientific soundness or budget validity.",
  "reason": "All five rounds of tracked issues are resolved; key claims independently verified; no overlooked competitive work threatens novelty; compute budget within 200 H100-hour ceiling even at worst-case variance; venue and deadline correct."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28076bb7-6ad5-4871-aaac-759aaed8d437",
  "isSidechain": false,
  "requestId": "req_011CatR5HBCzsNsxroZfhoPj",
  "type": "assistant",
  "uuid": "ad2cab2f-8ddb-4531-a107-8010005868da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EhK29mKQA1KE9cVr7aeKSK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8528,
      "cache_read_input_tokens": 37437,
      "output_tokens": 1939,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8528,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1939,
          "cache_read_input_tokens": 37437,
          "cache_creation_input_tokens": 8528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8528
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
  "leafUuid": "ad2cab2f-8ddb-4531-a107-8010005868da",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "SeMutFL: Training Fault Localization Robustness via Semantic Mutation Augmentation",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd"
}
```

---
