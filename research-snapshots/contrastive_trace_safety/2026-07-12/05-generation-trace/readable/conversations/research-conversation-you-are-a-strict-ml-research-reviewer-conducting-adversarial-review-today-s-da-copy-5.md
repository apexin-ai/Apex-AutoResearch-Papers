# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-11 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 102
- **Recorded user turns:** 1
- **Tool calls:** 28
- **Original source:** `logs/chats/exported-trajectories/account-1/9785eb62-9283-4705-9db2-c7b83aec5cc9.jsonl`
- **Structured JSON:** [`03ce9a4574eaf5d158fd.json`](../../sessions/03/03ce9a4574eaf5d158fd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T02:12:09.824Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T02:12:09.824Z",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-11 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 8/10)\n{\n  \"title\": \"ExeSpec: Verifiable Specification Reasoning for Code LLMs via Execution Grounding\",\n  \"core_problem\": \"Training-free inference-time methods for LLM code improvement—AlphaCodium (arXiv 2401.08500), CodeT (ICLR 2023), Self-Debugging (arXiv 2304.05128), S* (EMNLP 2025 Findings)—have demonstrated that execution feedback substantially boosts code generation quality using test cases as intermediate representations. Recently, PGS (arXiv 2506.18315, revised May 2026) showed that property-based feedback—abstract behavioral properties rather than I/O test cases—outperforms test-driven methods by 23.1–37.3% relative pass@1 on HumanEval, MBPP, and LiveCodeBench, validating that properties provide richer reasoning scaffolds than point-sample tests. However, three critical limitations remain unresolved. (1) Property reliability: LLM-generated properties are unreliable at scale—PGS reports property generation accuracy of only 48.9% on hard LiveCodeBench problems, ContractEval (arXiv 2510.12047) finds 0% contract satisfaction under standard prompting despite 75–82% pass@1, and CodeSpecBench (arXiv 2604.12268) reveals only 20.2% success at repo-level spec generation—yet no method systematically execution-grounds properties before use to catch hallucinated or internally contradictory specifications. PGS validates properties against public test cases for soundness but does not check inter-property consistency or proactively detect contradictions within the property set. (2) Task generalization: PGS and all property/test-based inference-time methods evaluate exclusively on code generation and simple repair (HumanEval, MBPP, LiveCodeBench), without extension to debugging (where intended-vs-observed behavioral contrasts are needed), issue resolution (where behavioral changes must be extracted from issue context and failing tests), or cross-file completion (where interface contracts must be inferred). NL-Debugging (EMNLP 2025 Main) demonstrated that natural language intermediate representations improve debugging by 4–6pp over code-level methods, but NL descriptions lack the structured, execution-verifiable format needed for systematic property checking. (3) Property decomposition: all property-based methods treat properties as a monolithic category—no work decomposes which property types (preconditions, postconditions, invariants, type constraints, I/O examples) contribute to which task types, preventing targeted optimization. Can execution-grounded, decomposed behavioral specifications address property reliability while extending property-based reasoning across diverse code tasks without model training?\",\n  \"opportunity\": \"Five research threads converge but remain disconnected: (1) Test-based inference-time refinement (AlphaCodium, CodeT, Self-Debugging, S*, BACE) proves execution feedback improves code generation—AlphaCodium raises CodeContests pass@5 from 19% to 44% on the validation set (12% to 29% on the 165-problem test set), CodeT improves HumanEval pass@1 by +18.8pp via dual execution agreement, S* enables a 3B model to outperform GPT-4o-mini on LiveCodeBench—but all use test cases (point samples) as the intermediate representation. (2) Property-based refinement: PGS (arXiv 2506.18315) demonstrates that LLM-generated abstract properties outperform test-driven feedback by 23.1–37.3% relative pass@1, establishing that property-level reasoning is superior to test-level reasoning for code refinement. However, PGS evaluates only on HumanEval/MBPP/LiveCodeBench (not CodeContests, SWE-bench, or debugging benchmarks), reports property generation accuracy dropping to 48.9% on hard problems, and does not verify inter-property consistency before use. Self-Spec (Agents4Science 2025) showed model-authored specs improve generation by +2–5pp but never verifies specs against execution. ContractEval (arXiv 2510.12047) reveals 0% contract satisfaction under standard prompting despite 75–82% pass@1, rising to only 23–41% with explicit contracts—demonstrating that even when contracts are provided, LLMs struggle to enforce them, motivating execution-based verification. 'From Prompts to Properties' (FSE Companion 2025/LLanMER) finds 30–32% of LLM-generated solutions exhibit partial property failures that pass@k metrics miss entirely. (3) Structured intermediate representations for code: NL-Debugging (EMNLP 2025 Main, arXiv 2505.15356) uses natural language as an intermediate representation for debugging via backtranslation → NL refinement → regeneration, outperforming code-level debugging by 4–6pp on APPS and Codeforces—establishing that higher-level abstractions aid debugging at ExeSpec's target venue. StoryCoder (ACL 2026 Main, arXiv 2604.14631) demonstrates narrative reformulation as structured intermediate reasoning, achieving +18.7% pass@10 across 11 models—concurrent work validating that structured intermediate representations improve code generation. Both use natural language (unverified against execution), not execution-grounded behavioral specifications. (4) Execution-grounded training (Think Like You Execute, RLEF at ICML 2025, FixAudit arXiv 2604.05560) achieves dramatic gains but requires fine-tuning—not usable with frozen models. FixAudit jointly trains fixer and auditor achieving 35–37% improvement on CodeContests, demonstrating the value of audit-style verification but requiring training. (5) Specification quality challenges: CodeSpecBench reveals 20.2% repo-level spec accuracy; 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025) shows self-generated test feedback introduces systematic bias—motivating richer, verified intermediate representations. The unexploited synthesis: PGS proved properties outperform tests, but property reliability remains the bottleneck (48.9% accuracy on hard problems). Execution grounding can close this gap—verifying LLM-generated property-level specs before use, catching hallucinated and contradictory properties. Additionally, decomposing properties into typed components (pre/postconditions, invariants, type constraints) and evaluating across task types (generation, debugging, issue resolution, completion) addresses the generalization gap that no prior work has tested.\",\n  \"landscape\": \"**Test-based inference-time methods.** AlphaCodium (arXiv 2401.08500, Jan 2024) is a training-free multi-stage flow with problem reflection, AI test generation, and iterative execution-based refinement with test anchoring, raising CodeContests validation-set pass@5 from 19% to 44% and test-set pass@5 from 12% to 29% with GPT-4. CodeT (ICLR 2023, arXiv 2207.10397) generates tests via LLMs and uses dual execution agreement for solution selection, improving HumanEval pass@1 by +18.8pp. Self-Debugging (arXiv 2304.05128) teaches LLMs to iteratively debug using execution results and natural language explanations, achieving up to 12% improvement on TransCoder and MBPP. 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025 Long, arXiv 2501.12793) reveals systematic bias in self-generated tests—in-execution debugging using intermediate program states mitigates this, demonstrating that test quality is a fundamental bottleneck for test-based methods. S* (EMNLP 2025 Findings, arXiv 2502.14382) combines parallel sampling with sequential debugging and adaptive distinguishing input synthesis, enabling a 3B model to outperform GPT-4o-mini on LiveCodeBench. BACE (GECCO 2026, arXiv 2603.28653) treats generated tests as noisy sensors via Bayesian updates, outperforming CodeSIM by +2.5–5.4pp on LiveCodeBench v6. All use test cases as the intermediate representation—point samples that verify specific inputs but don't capture universal behavioral properties.\\n\\n**Property-based and specification approaches.** PGS (arXiv 2506.18315, June 2025; revised as 'Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback', May 2026) is the closest prior work. PGS introduces a Generator-Tester framework where the Tester generates abstract behavioral properties (e.g., 'the product of output factors must equal the input integer') and validates code against them using property-based testing, with structurally minimal counterexamples as feedback. PGS achieves 23.1–37.3% relative pass@1 improvement over TDD methods (Reflexion, Self-Debugging, MGDebugger) using DeepSeek-Coder-V2, Qwen2.5-Coder, and DeepSeek-R1-Distilled-32B on HumanEval, MBPP, and LiveCodeBench. PGS validates properties against public test cases for soundness, reporting property generation accuracy of 82.4% (easy), 62.8% (medium), and 48.9% (hard) on LiveCodeBench. Critically, PGS does not check inter-property consistency, does not evaluate on CodeContests, SWE-bench, or debugging benchmarks, and treats properties as a monolithic category without decomposing which property types contribute to which tasks. ExeSpec differs from PGS in three ways: (a) execution grounding verifies specs before use via candidate-code probes and cross-spec consistency checks, catching hallucinated and contradictory specs that PGS's public-test validation misses; (b) evaluation spans four task types (generation, debugging, issue resolution, completion) on benchmarks PGS does not cover (CodeContests, SWE-bench Pro, DebugBench); (c) a 5-component schema with controlled ablation decomposes property contributions per task type. Self-Spec (Agents4Science 2025) has LLMs author specification languages before code generation, improving GPT-4o HumanEval pass@1 from 87% to 92%, but only evaluates on HumanEval and never verifies specs against execution. ContractEval (arXiv 2510.12047) benchmarks contract satisfaction in code generation, finding 0% satisfaction under standard prompting despite 75–82% pass@1 scores, 23–41% with explicit contracts, and 49–53% with example-augmented specifications—simultaneously validating that LLMs need external grounding for contract/spec enforcement AND quantifying the difficulty of the spec quality challenge. 'From Prompts to Properties' (FSE Companion 2025/LLanMER) applies property-based testing to evaluate LLM code, finding 30–32% partial property failures that pass@k metrics miss, motivating property-level evaluation. SpecRover/AutoCodeRover-v2 (ICSE 2025) performs iterative NL specification inference for automated program repair, achieving 19.31% on SWE-bench. VibeRepair (arXiv 2602.08263) translates code into NL behavioral specs for repair but specs are imprecise. SSDE (FSE Companion 2026, arXiv 2605.02455) uses Gherkin specifications and domain models for repo-level MVC generation—concurrent work demonstrating structured specs guide LLM generation, but requires human-authored specifications. CodeSpecBench (arXiv 2604.12268) benchmarks LLM spec generation showing only 20.2% repo-level pass rate, motivating execution-based verification.\\n\\n**Structured intermediate representations.** NL-Debugging (EMNLP 2025 Main, ACL Anthology 2025.emnlp-main.80, arXiv 2505.15356) uses natural language as an intermediate representation for code debugging via a three-stage pipeline: backtranslation (buggy code → NL sketch), NL refinement (identify and correct logical flaws in the NL representation using execution feedback), and regeneration (refined NL → corrected code). NL-Debugging outperforms code-level Self-Debugging by 4–6pp pass@1 on APPS and Codeforces across difficulty levels using GPT-4o-mini, Claude-3.5-Sonnet, and DeepSeek-Coder-V2-Lite. The key finding is that the 'Sketch' NL format—detailed natural language descriptions—enables broader modification space than code-level edits, and that refinement in the NL space (not NL→code translation) drives the gains. This establishes structured intermediate representations as valuable for debugging at ExeSpec's target venue (EMNLP). ExeSpec's specifications provide a more structured, execution-verifiable intermediate representation than free-form NL sketches—enabling systematic property checking rather than holistic NL reasoning. StoryCoder (ACL 2026 Main, arXiv 2604.14631) transforms code generation problems into structured narratives (task overview, constraints, test examples), achieving +18.7% zero-shot pass@10 across 11 models on HumanEval, LiveCodeBench, and Codeforces—concurrent training-free work validating structured reformulation, but using narrative structure rather than behavioral specifications. SCoT (ACL 2024) adds program structure to CoT without execution grounding.\\n\\n**Execution-grounded and RL training methods.** Think Like You Execute (arXiv 2512.00127) achieves +22–27pp on CRUXEval/LiveCodeBench via fine-tuning on 54K execution-trace-verified rationales. EG-CFG (NeurIPS 2025, arXiv 2506.10948) uses real-time execution via beam search over candidate lines—computationally expensive and generation-only. RLEF (ICML 2025) trains code LLMs with RL execution feedback. Think Anywhere (arXiv 2603.29957) enables on-demand reasoning during code generation via RL training. CURE (NeurIPS 2025 Spotlight) co-evolves coder and tester via RL. FixAudit (arXiv 2604.05560) jointly trains a fixer and auditor—the auditor generates new tests revealing implementation-specific bugs in the fixer's candidate code, achieving 35–37% pass@1 improvement on APPS, CodeContests, and xCodeEval with a 7B model. All require training—not applicable with frozen models.\\n\\n**The gap.** PGS established that property-based feedback outperforms test-based feedback for code generation. Three open questions remain: (1) Can execution grounding improve property reliability beyond PGS's public-test validation (addressing the 48.9% accuracy on hard problems)? (2) Do property-based approaches generalize to debugging, issue resolution, and completion—task types no property-based method has evaluated? (3) Which property types contribute to which tasks? No work addresses all three questions in a unified, training-free framework with controlled experimental design.\",\n  \"approach\": \"We propose ExeSpec, a training-free inference-time framework that uses execution-grounded behavioral specifications as verifiable structured intermediate reasoning for LLM code tasks. Building on PGS's demonstration that property-based feedback outperforms test-based feedback for code generation, ExeSpec advances the property-based paradigm in three directions: (1) execution grounding that verifies spec consistency and catches hallucinated properties before downstream use, (2) extension to debugging, issue resolution, and cross-file completion beyond generation/repair, and (3) decomposition of specifications into typed components with controlled ablation.\\n\\n**Stage 1: Spec Elicitation.** Given a task input, prompt the LLM to generate structured behavioral specifications in a lightweight JSON schema containing five component types: (a) I/O example pairs (shared with both PGS properties and AlphaCodium test cases—the overlap region), (b) preconditions (constraints on valid inputs/states, e.g., 'n >= 0', 'input list is non-empty'), (c) postconditions (properties guaranteed on outputs, e.g., 'output is sorted in ascending order', 'len(output) == len(input)'), (d) type constraints (parameter and return type annotations with generics), and (e) invariants (loop invariants, monotonicity, ordering properties). The schema is task-adapted: generation tasks derive specs from docstrings; debugging tasks elicit intended-vs-observed behavioral contrasts; issue resolution tasks extract expected behavioral changes from issue descriptions and failing test context; completion tasks infer interface contracts from cross-file context.\\n\\n**Stage 2: Execution Grounding.** This is ExeSpec's primary differentiator from PGS. While PGS validates properties against public test cases for soundness, ExeSpec additionally performs: (i) cross-spec consistency checking—verifying that preconditions, postconditions, invariants, and type constraints are mutually satisfiable and non-contradictory (e.g., a postcondition asserting 'output is sorted' does not contradict an invariant asserting 'elements maintain original order'); (ii) candidate-code probing—generating a quick candidate solution, executing against spec-derived assertions including both I/O examples AND postcondition property checks, identifying spec-execution mismatches, and revising contradicted specs before final generation. For debugging tasks: execute the buggy code, compare execution traces against specs to identify precisely which behavioral constraints are violated, producing structured violation reports. For issue resolution (SWE-bench Pro): extract behavioral expectations from issue descriptions and failing tests, generate specs characterizing the intended fix behavior, and validate spec consistency against the existing test suite via Docker-based execution. For cross-file completion: static grounding via type inference from imported modules, parameter/return types from call-site usage context, and validation via type checkers (mypy/pyright for Python, tsc for TypeScript). When full execution is unavailable, static grounding serves as fallback: cross-spec consistency checking, type inference, and contradiction detection.\\n\\n**Stage 3: Spec-Guided Task Completion.** Feed grounded specs alongside the original task input to the LLM for final output. When outputs violate specs, structured violation reports (which constraints failed, expected vs. actual, which spec component) feed back for iterative refinement (up to 3 rounds). Unlike PGS's structurally minimal counterexamples, ExeSpec's feedback references typed behavioral properties ('postcondition: output must be monotonically increasing') with component attribution, enabling the LLM to reason about which aspect of behavioral intent was violated.\\n\\n**Baselines and controlled experiments.** The experimental design isolates contributions through six controlled conditions: (a) ExeSpec full (5-component specs + execution grounding), (b) PGS baseline (property-based testing following PGS's Generator-Tester framework, reimplemented on our benchmarks—the paper's critical comparison, isolating the contribution of execution grounding and component decomposition beyond PGS's approach), (c) AlphaCodium-style baseline (problem reflection + AI test generation + iterative execution/refinement with test anchoring—isolating the property-vs-test distinction, extending PGS's finding to new benchmarks), (d) Self-Spec baseline (specs without execution grounding—isolating the grounding contribution), (e) direct prompting (no intermediate reasoning), (f) NL-Debugging baseline on DebugBench only (NL intermediate representation via backtranslation/refinement/regeneration—isolating structured specs vs. free-form NL for debugging, providing venue-relevant comparison to EMNLP 2025 work). The delta between (a) and (b) is the paper's core contribution—whether execution grounding and component decomposition provide gains beyond PGS's property-based approach. The delta between (b) and (c) replicates PGS's finding (properties > tests) on new benchmarks (CodeContests, DebugBench, SWE-bench Pro) where PGS has not been evaluated. A critical spec-component ablation further decomposes: (i) full specs (I/O + pre/postconditions + invariants + type constraints), (ii) I/O-only specs (functionally equivalent to test cases—if this matches full specs, the novelty claim collapses), (iii) structural specs only (pre/postconditions + invariants + type constraints, no I/O)—this ablation is the critical honesty test.\\n\\n**Benchmarks.** Primary benchmarks with all six conditions + spec-component ablation: DebugBench (C++/Java/Python debugging—specs naturally capture intended-vs-observed behavioral contrasts, and NL-Debugging comparison is venue-relevant), CodeContests (competitive programming—direct comparison to AlphaCodium on its home benchmark, and first evaluation of PGS-style property feedback on CodeContests), and SWE-bench Pro (real-world issue resolution—adopted as co-primary benchmark given that SWE-bench Verified is compromised by contamination in frontier models; OpenAI stopped reporting Verified scores in February 2026 after finding frontier models could reproduce verbatim gold patches. We use Qwen2.5-Coder-7B/32B, sub-frontier models unlikely to exhibit the verbatim gold-patch reproduction observed in GPT-5.2 and Claude Opus 4.5, providing a contamination-resistant evaluation baseline. We report results on both SWE-bench Pro and Verified for completeness, noting the community's shift toward Pro for reliable evaluation). Supplementary benchmarks with ExeSpec vs. direct prompting only: HumanEval+/MBPP+ (for Self-Spec and PGS comparability—PGS reports results on these benchmarks, enabling direct numerical comparison), CrossCodeEval and RepoBench (cross-file completion with static grounding via type checkers). We explicitly acknowledge that cross-file completion relies on weaker static grounding than dynamic execution and report the proportion of instances where only static grounding was available.\\n\\n**Models.** We use Qwen2.5-Coder-7B-Instruct and Qwen2.5-Coder-32B-Instruct as established dense models with strong code performance and reproducible vLLM inference; the method is model-agnostic and we expect gains to transfer to newer architectures including MoE models (e.g., Qwen3-Coder-Next). Using established models enables direct comparison with PGS, which evaluates Qwen2.5-Coder on the same model family.\\n\\n**Analysis.** Beyond standard metrics: (1) spec quality analysis—correlation between spec correctness and downstream task performance; (2) grounding effectiveness—proportion of hallucinated specs caught by execution grounding vs. PGS's public-test validation (the key comparison); (3) spec-component contribution—which spec types most improve each task type; (4) test overfitting rates—proportion of solutions passing visible tests but failing held-out tests, comparing ExeSpec vs. baselines; (5) property accuracy by difficulty—replicating PGS's accuracy breakdown (82.4%/62.8%/48.9% by difficulty) on our benchmarks and measuring whether execution grounding improves it; (6) qualitative case studies showing where execution-grounded specs enable corrections that both test-only and ungrounded property methods miss.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~150–200 H100-hours (primary benchmarks DebugBench + CodeContests + SWE-bench Pro with 6 conditions × 2 models + NL-Debugging on DebugBench + spec-component ablation on primary benchmarks; supplementary HumanEval+/MBPP+ + CrossCodeEval + RepoBench with ExeSpec vs. direct prompting × 2 models; PGS baseline reimplementation on all primary benchmarks; using vLLM batch inference with Qwen2.5-Coder-7B on 1 H100 and 32B on 1–2 H100s)\",\n      \"gpu_utilization\": \"Moderate (~40–55%): alternating between inference bursts and execution-grounding phases; SWE-bench Pro Docker execution and DebugBench compilation are CPU-bottlenecked\",\n      \"timeline\": \"18–22 days (days 1–4: framework implementation + PGS baseline reimplementation following published Generator-Tester method + AlphaCodium baseline adaptation from open-source code + NL-Debugging baseline setup + eval harness configuration leveraging SWE-bench Docker harness and EvalPlus; days 5–8: primary benchmarks DebugBench + CodeContests with all 6 conditions; days 9–12: SWE-bench Pro + SWE-bench Verified with all 6 conditions; days 13–14: supplementary benchmarks HumanEval+/MBPP+ + CrossCodeEval + RepoBench with ExeSpec vs. direct prompting; days 15–17: spec-component ablation + grounding effectiveness analysis + property accuracy comparison vs. PGS; days 18–22: writing + analysis)\",\n      \"team\": \"2 researchers (1 lead for ExeSpec framework + execution-grounding pipeline + spec-component ablation design, 1 for PGS/AlphaCodium/NL-Debugging baseline reimplementation + benchmark integration + evaluation infrastructure)\",\n      \"estimated_gpu_cost\": \"$450–600 (on-demand H100 at ~$3/hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~170–230 H100-hours (same scope as manual with more systematic spec quality validation, PGS comparison analysis, and additional analysis iterations)\",\n      \"gpu_utilization\": \"Moderate–High (~50–65%): agent queues experiment batches across benchmarks while human reviews spec quality and PGS baseline fidelity between rounds\",\n      \"timeline\": \"14–18 days (agent handles framework code, experiment orchestration, and result collection; human validates spec schema design, reviews PGS and AlphaCodium baseline fidelity, and guides ablation priorities)\",\n      \"team\": \"1 researcher, ~3–4 hrs/day reviewing spec elicitation outputs, validating PGS baseline implementation matches the published Generator-Tester framework, reviewing NL-Debugging baseline, approving experiment plans, and analyzing results\",\n      \"claude_api_cost\": \"$150–250 (1500–2500 orchestration turns at ~$0.10/turn)\",\n      \"estimated_gpu_cost\": \"$510–690\",\n      \"risk_note\": \"PGS baseline reimplementation fidelity is critical—must reproduce the Generator-Tester property-based testing framework faithfully; NL-Debugging baseline must reproduce the backtranslation→NL refinement→regeneration pipeline; SWE-bench Pro evaluation infrastructure may require additional setup compared to the established Verified harness\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~200–270 H100-hours (systematic sweeps over spec granularity levels, grounding strategies per benchmark, additional model backbone DeepSeek-R1-Distilled-32B for PGS comparability, temperature and sample-count variations)\",\n      \"gpu_utilization\": \"High (~80–90%): agent pipelines experiments back-to-back with minimal idle; parallel runs across benchmarks on multiple H100s\",\n      \"timeline\": \"8–12 days with 4–8 H100s available concurrently (bottlenecked by SWE-bench Pro Docker execution and DebugBench compilation)\",\n      \"team\": \"0 (initial setup ~4–5 hours for benchmark harness configuration, PGS/AlphaCodium/NL-Debugging baseline setup, and vLLM model serving, then fully autonomous)\",\n      \"claude_api_cost\": \"$250–450 (2500–4500 turns for iterative experiment design, cross-benchmark analysis, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$600–810\",\n      \"speed_bottleneck\": \"SWE-bench Pro Docker-based test execution and DebugBench compilation/execution; inference itself is fast with vLLM on H100\",\n      \"risk_note\": \"Agent may over-optimize for one benchmark; need guardrails to ensure PGS baseline is faithfully implemented (not strawmanned), NL-Debugging baseline is accurate, and spec-component ablation runs completely even if early results are unfavorable\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission May 25, 2026; commitment Aug 2, 2026; NLP and Code Models track; Budapest, Hungary)\",\n    \"ACL 2027 (expected ARR commitment ~Jan 2027; fallback if EMNLP revision needed)\",\n    \"NAACL 2027 (expected ARR commitment ~Mar 2027; second fallback)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Use Property-Based Testing to Bridge LLM Code Generation and Validation / Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback (PGS; arXiv 2506.18315, June 2025, revised May 2026)\",\n    \"NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging (EMNLP 2025 Main, ACL Anthology 2025.emnlp-main.80, arXiv 2505.15356)\",\n    \"ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation (arXiv 2510.12047)\",\n    \"AlphaCodium: Code Generation through Flow Engineering (arXiv 2401.08500, Jan 2024)\",\n    \"CodeT: Code Generation with Generated Tests (ICLR 2023, arXiv 2207.10397)\",\n    \"Teaching Large Language Models to Self-Debug (Self-Debugging; arXiv 2304.05128, 2023)\",\n    \"Revisit Self-Debugging with Self-Generated Tests for Code Generation (ACL 2025 Long, arXiv 2501.12793)\",\n    \"S*: Test Time Scaling for Code Generation (EMNLP 2025 Findings, arXiv 2502.14382)\",\n    \"BACE: Bayesian Anchored Co-Evolution of Code and Test Populations (GECCO 2026, arXiv 2603.28653)\",\n    \"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation (Agents4Science 2025)\",\n    \"StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation (ACL 2026 Main, arXiv 2604.14631)\",\n    \"FixAudit: An Iterative Test-and-Repair Framework for Competitive Code Generation (arXiv 2604.05560)\",\n    \"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing (FSE Companion 2025/LLanMER, ACM 10.1145/3696630.3728702)\",\n    \"Execution Guided Line-by-Line Code Generation (EG-CFG; NeurIPS 2025, arXiv 2506.10948)\",\n    \"Think Like You Execute: Verifiable Chain of Thought from Program Traces (arXiv 2512.00127)\",\n    \"Think Anywhere in Code Generation (arXiv 2603.29957, Mar 2026)\",\n    \"SpecRover: Code Intent Extraction via LLMs (ICSE 2025)\",\n    \"CURE: Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning (NeurIPS 2025 Spotlight)\",\n    \"Code Execution as Grounded Supervision for LLM Reasoning (EMNLP 2025)\",\n    \"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (arXiv 2604.12268, Apr 2026)\",\n    \"Specification Vibing for Automated Program Repair (VibeRepair; arXiv 2602.08263, Feb 2026)\",\n    \"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering (SSDE; FSE Companion 2026, arXiv 2605.02455)\",\n    \"Investigating Test Overfitting on SWE-bench (arXiv 2511.16858)\",\n    \"The Undecidability of Overfitting in Automated Program Repair (ICSE 2026 NIER)\",\n    \"RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning (ICML 2025)\",\n    \"Structured Chain-of-Thought Prompting for Code Generation (SCoT; ACL 2024)\",\n    \"Qwen2.5-Coder Technical Report (arXiv 2409.12186)\"\n  ],\n  \"description\": \"We propose ExeSpec, a training-free inference-time framework that uses execution-grounded behavioral specifications as verifiable structured intermediate reasoning for LLM code tasks. Building on PGS's demonstration (arXiv 2506.18315) that property-based feedback outperforms test-based methods by 23.1–37.3% relative pass@1 on generation benchmarks, ExeSpec advances the property-based paradigm in three directions: (1) execution grounding that verifies spec consistency and catches hallucinated properties before downstream use—addressing PGS's property accuracy drop to 48.9% on hard problems and ContractEval's finding of 0% contract satisfaction under standard prompting; (2) extension to four task types (generation, debugging, issue resolution, completion) on benchmarks PGS does not cover (CodeContests, DebugBench, SWE-bench Pro); (3) decomposition into 5 typed spec components (I/O examples, preconditions, postconditions, invariants, type constraints) with controlled ablation revealing which components aid which tasks. The method operates in three stages: Spec Elicitation (task-adapted structured spec generation), Execution Grounding (cross-spec consistency checking + candidate-code probing to verify specs before use), and Spec-Guided Completion (grounded specs as verified intermediate reasoning with typed violation feedback). The experimental design isolates contributions through six conditions: (a) ExeSpec full, (b) PGS baseline (property-based testing reimplemented on our benchmarks—the critical comparison isolating execution grounding's contribution), (c) AlphaCodium-style baseline (test-based—extending PGS's property-vs-test finding to new benchmarks), (d) Self-Spec baseline (specs without grounding), (e) direct prompting, (f) NL-Debugging baseline on DebugBench (NL intermediate representation from EMNLP 2025—venue-relevant comparison). The spec-component ablation tests whether I/O-only specs match full specs (if so, the novelty claim collapses—reported honestly). Primary benchmarks: DebugBench (debugging), CodeContests (competitive programming, AlphaCodium's benchmark), SWE-bench Pro (issue resolution, replacing Verified as primary due to contamination—Qwen2.5-Coder-7B/32B are sub-frontier models unlikely to exhibit the verbatim gold-patch reproduction observed in frontier models). Supplementary: HumanEval+/MBPP+ (PGS/Self-Spec comparability), CrossCodeEval/RepoBench (completion with static grounding). Models: Qwen2.5-Coder-7B/32B-Instruct as established dense models with reproducible vLLM inference; the method is model-agnostic. Within 150–200 H100-hours and ~20 days. Primary target: EMNLP 2026 (ARR May 25, 2026).\",\n  \"project_name\": \"test_spec_guided_repair\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL VENUE MISMATCH: User explicitly requested EMNLP 2026 (ARR deadline 2026-05-25, NLP and Code Models track), but the idea targets ICSE 2027, AAAI 2027, and FSE 2027 — all SE venues. The idea must be redesigned or reframed for EMNLP.\", \"CRITICAL COMPUTE VIOLATION: User constrained to ≤200 H100-hours total. The idea estimates 250-400 A100-80GB hours (manual mode). Running Kimi K2-Instruct (1T params MoE, requiring 4×A100 per instance) adds substantial inference costs not fully accounted for.\", \"CRITICAL TIMELINE VIOLATION: User has ~14 days. The idea estimates 3-5 months (manual), 6-10 weeks (HIL), or 1-3 weeks with 8-16 A100s (auto). None of these fit the user's constraint.\", \"EVAL BENCHMARK MISMATCH: User requested evaluation on SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, and CodeContests. The idea only covers SWE-bench Verified and Defects4J (which isn't even in the user's list). Missing 5 of 6 required benchmarks.\", \"MISSING CRITICAL RELATED WORK: (1) SpecRover/AutoCodeRover-v2 (ICSE 2025) — already does specification inference for patching; (2) CURE (NeurIPS 2025 Spotlight) — RL co-evolution of coder and tester; (3) CodeSpecBench (arXiv 2604.12268, Apr 2026) — benchmark showing LLMs achieve only 20.2% on repo-level behavioral spec generation; (4) Test overfitting undecidability (ICSE 2026 NIER) + empirical study (arXiv 2511.16858) showing 21-33% of LLM patches overfit on visible tests; (5) Dynamic Cogeneration at Google (arXiv 2601.19066); (6) SWE-Tester (arXiv 2601.13713).\", \"NOVELTY CONCERN: The idea is too similar to VibeRepair (arXiv 2602.08263, Feb 2026). VibeRepair already translates code into structured behavioral specifications for repair, achieving SOTA on Defects4J. The proposed delta — using test assertions instead of NL as the specification source — is an incremental variant, not a fundamentally new paradigm. SpecRover (ICSE 2025) also does specification inference for repair.\", \"TOPIC SCOPE TOO NARROW: User asked for 'code understanding and generation' covering repo-level comprehension, code reasoning, debugging, test generation, code-to-documentation, cross-language transfer. The idea focuses narrowly on Java program repair via Defects4J, which is only one subtask and one language.\", \"MISLEADING CLAIMS: '174/178 correct repairs' reads as a fraction but actually means 174 on v1.2 and 178 on v2.0. 'Proving specification-level repair is superior' overstates VibeRepair's own conclusions. The 48.29% for Repair-R1 represents only a 2.68pp improvement over baseline.\", \"TEST OVERFITTING NOT ADDRESSED: An ICSE 2026 NIER paper proves test overfitting is theoretically undecidable when full specifications are unavailable. An empirical study shows 21-33% of LLM patches overfit on visible tests. The idea's reliance on auto-generated tests as specifications is directly vulnerable to this fundamental limitation.\"]\nFeedback: This idea has a reasonable technical intuition (test assertions as behavioral specs) but fundamentally fails to meet the user's requirements. Here is what needs to change:\n\n1. **VENUE**: Reframe for EMNLP 2026 (NLP and Code Models track) or propose a different idea entirely. For EMNLP, the contribution must emphasize NLP methodology (e.g., how LLMs reason about code specifications, a new inference-time algorithm for code understanding) rather than SE pipeline engineering. EMNLP reviewers care about language model capabilities, not Defects4J leaderboard numbers.\n\n2. **SCOPE**: Broaden beyond Java program repair. The user wants 'code understanding and generation' covering multiple tasks (debugging, test generation, code reasoning, cross-language transfer). Consider a method that applies across multiple code tasks, not just APR.\n\n3. **BENCHMARKS**: Must evaluate on the user's required benchmarks: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests. Drop Defects4J (not requested).\n\n4. **COMPUTE**: Stay within ≤200 H100-hours. Use smaller models (DeepSeek-Coder-V2-Lite-Instruct 16B, StarCoder2-15B, Qwen2.5-Coder-7B/32B) as the user suggested, not 1T-param Kimi K2. This also aligns with the user's suggested model list.\n\n5. **TIMELINE**: Design for ≤16 days of execution. Build on existing frameworks (aider, SWE-agent, Moatless) as the user suggested. The current 3-5 month estimate is a non-starter.\n\n6. **NOVELTY BOOST**: Differentiate more clearly from VibeRepair and SpecRover. Instead of 'yet another spec-guided repair pipeline,' consider: (a) a novel inference algorithm that uses execution feedback to iteratively refine code understanding, (b) a retrieval-augmented approach with semantic code search for cross-repo transfer, or (c) a method for repo-level context compression that enables better code reasoning — all directions the user explicitly suggested.\n\n7. **ADDRESS TEST OVERFITTING**: Any test-based approach must engage with the ICSE 2026 undecidability result and the empirical overfitting findings. Propose concrete mitigation strategies.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MISSING CRITICAL BASELINES: AlphaCodium (arXiv 2401.08500, Jan 2024) is a training-free, inference-time, test-based iterative flow with problem analysis + AI test generation + iterative refinement against tests. It is the most direct conceptual predecessor to ExeSpec and MUST be cited and compared as a baseline. CodeT (ICLR 2022) and Self-Debugging (arXiv 2304.05128, 2023) are also missing—both are foundational works in execution-based code refinement at inference time.\", \"MISSING CONCURRENT WORK: BACE (arXiv 2603.28653, Mar 2026) addresses the same 'noisy self-generated tests' problem via Bayesian co-evolution of code and test populations. 'Revisit Self-Debugging with Self-Generated Tests' (arXiv 2501.12793, Jan 2025) directly studies post-execution vs. in-execution self-debugging paradigms with LLM-generated tests. Both must be discussed.\", \"THIN NOVELTY BOUNDARY: The distinction between 'structured behavioral specifications' (I/O example pairs, pre/postconditions, invariants in JSON schema) and 'self-generated test assertions' is conceptually thin. I/O examples ARE test cases. Pre/postconditions and invariants add something, but AlphaCodium's 'problem analysis' + 'edge case identification' phase also generates structured problem understanding before coding. The paper needs to sharpen why spec-mediated reasoning is fundamentally different from test-mediated refinement, with controlled experiments isolating this distinction.\", \"HUMANEVAL SATURATION: HumanEval+ and MBPP+ are listed as primary benchmarks, but frontier models already score 93%+ on HumanEval. Even with EvalPlus's harder tests, the benchmark is near saturation. The paper should emphasize DebugBench, CrossCodeEval, CodeContests, and SWE-bench Verified as primary evaluation, and use HumanEval+/MBPP+ only for comparability with Self-Spec.\", \"SPEC QUALITY BOOTSTRAPPING RISK: CodeSpecBench shows LLMs achieve only 20.2% on repo-level spec generation. If the LLM generates mostly bad specs, execution grounding catches them—but then the method degrades to 'generate specs → discard most → fall back to direct generation.' The paper needs analysis of what happens when spec generation quality is low (e.g., on CrossCodeEval/RepoBench repo-level tasks), including a failure mode analysis.\", \"TIMELINE IS VERY AGGRESSIVE: 12–16 days for implementing a 3-stage framework with task-adapted spec schemas, integrating 6 benchmarks (including SWE-bench Docker), running 48+ experiment configurations (6 benchmarks × 2 models × 4 baselines + ablations), AND writing a full paper. SWE-bench Verified Docker setup alone can take 2–3 days. Recommend reducing scope: run full comparison on 3 primary benchmarks (DebugBench, CodeContests, SWE-bench Verified) and use 3 others (HumanEval+/MBPP+, CrossCodeEval/RepoBench) for supplementary evaluation with fewer baselines.\", \"COST ESTIMATE MISSING API COSTS FOR EG-CFG BASELINE: Reproducing an EG-CFG-style execution-only baseline requires beam search with per-line execution, which is substantially more expensive than standard inference. This is either infeasible within budget or needs to be replaced with a simpler 'execution feedback without specs' baseline.\"]\nFeedback: The revision successfully addresses the critical venue, compute, and scope issues from Round 1. The idea is now properly scoped for EMNLP 2026 with correct benchmarks, models, and budget. However, several issues need resolution:\n\n1. **Sharpen novelty vs. AlphaCodium/CodeT**: These are the most important missing baselines. AlphaCodium (2024) already does training-free, multi-stage, test-based iterative refinement at inference time. ExeSpec must demonstrate that specification-mediated reasoning (structured I/O examples + pre/postconditions + invariants) provides gains BEYOND what test-based refinement alone achieves. Add a controlled experiment: (a) ExeSpec with full specs, (b) AlphaCodium-style test-only refinement, (c) Self-Spec without execution grounding, (d) direct prompting. The delta between (a) and (b) is the paper's core contribution.\n\n2. **De-emphasize saturated benchmarks**: Make DebugBench, CodeContests, and SWE-bench Verified the primary evaluation. Use HumanEval+/MBPP+ for Self-Spec comparability only. Consider adding LiveCodeBench for contamination resistance.\n\n3. **Address spec quality gracefully**: Add a spec quality analysis section showing: (a) what fraction of elicited specs survive execution grounding, (b) how grounding changes spec accuracy, (c) what happens when most specs fail (does the method degrade gracefully?). This directly responds to the CodeSpecBench 20.2% finding and strengthens the paper's analytical contribution.\n\n4. **Simplify the EG-CFG baseline**: Replace the full EG-CFG-style baseline (beam search + per-line execution) with a simpler 'execution feedback without specs' baseline: generate code → execute → feed error messages back → regenerate. This is cheaper and more directly tests the spec contribution.\n\n5. **Reduce timeline risk**: Implement the framework first on HumanEval+/MBPP+ (fast turnaround), validate the approach, then extend to harder benchmarks. Consider submitting to ARR May 25 with 4 benchmarks instead of 6, adding the remaining 2 for the camera-ready.\n\n6. **Cite and discuss**: AlphaCodium (2401.08500), CodeT (ICLR 2022), Self-Debugging (2304.05128), BACE (2603.28653), Revisit Self-Debugging (2501.12793). Position ExeSpec as advancing beyond test-only refinement by introducing verifiable specification reasoning as a structured intermediate representation.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL UNADDRESSED R2 FEEDBACK: AlphaCodium (arXiv 2401.08500, Jan 2024), CodeT (ICLR 2023), Self-Debugging (arXiv 2304.05128, 2023), BACE (arXiv 2603.28653, Mar 2026), and 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025, arXiv 2501.12793) are ALL still missing from key_references and baselines. Round 2 explicitly stated these MUST be cited and compared. AlphaCodium is the most direct conceptual predecessor — a training-free, multi-stage flow with problem reflection, test generation, and iterative execution-based refinement — and must be a baseline, not just a citation.\", \"NEW MISSING WORK — S* (EMNLP 2025 Findings, arXiv 2502.14382): A training-free test-time scaling framework for code generation that uses execution-based selection with adaptive distinguishing input synthesis. Enables a 3B model to outperform GPT-4o-mini. Published at EMNLP 2025 — the same venue being targeted. This is a highly relevant prior art that directly competes in the 'training-free inference-time code improvement' space.\", \"NEW MISSING CONCURRENT WORK — SSDE (arXiv 2605.02455, May 2026): 'LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering' uses Gherkin specifications and domain models to guide LLM generation with verification against test suites. Concurrent work that overlaps with ExeSpec's structured specification approach at the repo level.\", \"THIN NOVELTY BOUNDARY WITH ALPHACODIUM: AlphaCodium's pre-processing phase (problem reflection → public tests reasoning → possible solutions ranking) IS structured problem analysis before code generation. AlphaCodium's iterative phase (generate → execute → fix against public + AI tests) IS execution-grounded refinement. ExeSpec's I/O example specs are functionally identical to AlphaCodium's AI-generated test cases. The actual novelty delta — pre/postconditions, invariants, type constraints in JSON schema — must be isolated via controlled ablation: (a) ExeSpec full specs, (b) I/O-only specs (≈ test-only, AlphaCodium-style), (c) structural specs only (pre/postconditions + invariants without I/O). Without this, reviewers will reject for insufficient novelty.\", \"UNDERSPECIFIED NON-GENERATION TASKS: The approach for cross-file completion (CrossCodeEval, RepoBench) says 'type-check and partially execute the surrounding context to verify inferred specs.' This is vague. How do you generate behavioral specs for incomplete code in a multi-file context? What executable probes work for partial programs? CodeSpecBench shows only 20.2% success at repo-level spec generation — the method may degrade to fallback (soft grounding) for most repo-level instances, making the execution grounding contribution negligible on these benchmarks.\", \"HUMANEVAL+ STILL NOT DE-EMPHASIZED: Round 2 explicitly recommended making DebugBench, CodeContests, and SWE-bench Verified primary, with HumanEval+/MBPP+ for Self-Spec comparability only. The idea still lists them alongside other benchmarks without prioritization. Frontier models score 93%+ on HumanEval — gains here are not impressive.\", \"AGGRESSIVE TIMELINE NOT MITIGATED: Round 2 suggested reducing to 3 primary benchmarks + 3 supplementary. The idea still plans full comparison on all 6 benchmarks within 12–16 days. SWE-bench Docker setup alone takes 2–3 days. Recommend: primary (DebugBench, CodeContests, SWE-bench Verified) with full baselines; supplementary (HumanEval+/MBPP+, CrossCodeEval, RepoBench) with ExeSpec vs. direct prompting only.\"]\nFeedback: This is Round 3, and the idea has improved significantly from Round 1 (correct venue, benchmarks, compute budget) but has failed to address the MOST CRITICAL Round 2 feedback: citing and comparing against AlphaCodium, CodeT, Self-Debugging, BACE, and 'Revisit Self-Debugging.' This is not optional — these are the papers that define the competitive landscape for training-free, execution-based code improvement methods.\n\nHere is exactly what needs to change:\n\n1. **ADD ALPHACODIUM AS PRIMARY BASELINE** (non-negotiable): Replace the 'EG-CFG-style execution-only feedback' baseline with an AlphaCodium-style baseline: problem analysis → AI test generation → iterative code execution/refinement (no structured specs). This directly tests the paper's core claim that specification-mediated reasoning provides gains beyond test-based refinement. The controlled experiment should be: (a) ExeSpec full (specs + execution grounding), (b) AlphaCodium-style (tests + execution feedback, no specs), (c) Self-Spec (specs, no execution grounding), (d) direct prompting. The delta between (a) and (b) is the paper's contribution.\n\n2. **CITE AND POSITION AGAINST S* (EMNLP 2025 Findings)**: S* is the most recent training-free test-time scaling method for code generation, published at your target venue. Position ExeSpec as complementary: S* focuses on parallel/sequential scaling with execution-based selection; ExeSpec focuses on structured intermediate reasoning via verified specs. They could potentially be combined.\n\n3. **SHARPEN THE SPEC VS. TEST DISTINCTION**: The paper must clearly argue why structured behavioral specifications (pre/postconditions, invariants, type constraints) provide fundamentally different reasoning scaffolding compared to test cases. Add a controlled ablation: (a) full specs (I/O + pre/postconditions + invariants), (b) I/O-only specs (≈ test cases), (c) structural specs only (pre/postconditions + invariants, no I/O). If (b) performs similarly to (a), the novelty claim collapses.\n\n4. **SPECIFY THE CROSS-FILE COMPLETION APPROACH**: Describe concretely how ExeSpec generates and validates specs for CrossCodeEval/RepoBench tasks. What does the spec schema look like for incomplete code with cross-file dependencies? What 'lightweight probes' execute for partial programs? If the approach fundamentally differs from function-level generation, say so explicitly.\n\n5. **REDUCE SCOPE TO FIT TIMELINE**: Primary benchmarks with full baselines: DebugBench, CodeContests, SWE-bench Verified. Supplementary with ExeSpec vs. direct prompting only: HumanEval+/MBPP+, CrossCodeEval, RepoBench. This halves the experiment matrix.\n\n6. **ADD TO KEY REFERENCES**: AlphaCodium (2401.08500), CodeT (ICLR 2023, 2207.10397), Self-Debugging (2304.05128), BACE (2603.28653), 'Revisit Self-Debugging' (ACL 2025, 2501.12793), S* (EMNLP 2025 Findings, 2502.14382), SSDE (2605.02455).\n\n### Round 4 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING COMPETITOR: PGS (Property-Generated Solver, arXiv:2506.18315, June 2025, revised May 2026) uses high-level program properties instead of test cases as feedback for LLM code refinement, with execution-based property verification and minimal counterexample generation. It achieves 13.4% pass@1 improvement over TDD methods and 1.4-1.6x higher bug fix rate. This shares ExeSpec's core insight (properties > tests) and must be cited, compared against, and clearly differentiated.\", \"MISSING RELATED WORK: (1) 'From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing' (FSE 2025) directly challenges test-based paradigm in favor of properties; (2) ContractEval/PACT (arXiv:2510.12047) benchmarks LLM contract satisfaction showing 0% under standard prompting, validating the problem but also raising spec generation quality concerns; (3) 'Preconditions and Postconditions as Design Constraints for LLM Code Generation' (IEEE Access 2024/2025) directly studies ExeSpec's premise with controlled experiments; (4) StoryCoder (arXiv:2604.14631, ACL 2026) is another training-free structured intermediate reasoning method achieving 18.7% improvement.\", \"SWE-BENCH VERIFIED CONTAMINATION: The benchmark is now severely contaminated — top score is 93.9% (Claude Mythos), while the same models score only ~46% on SWE-bench Pro. OpenAI has stopped reporting Verified scores. The paper acknowledges contamination but should more seriously consider using SWE-bench Pro as the primary evaluation or running both and comparing. Reporting only Verified results risks reviewer skepticism.\", \"MODEL CURRENCY: Qwen3-Coder has been released since the idea was designed. EMNLP reviewers may question why the paper uses Qwen2.5-Coder-7B/32B rather than the latest version. Either justify the choice (reproducibility, available at experiment time) or update.\", \"SPEC GENERATION QUALITY RISK INSUFFICIENTLY ADDRESSED: ContractEval shows 0% contract satisfaction under standard prompting and only 23-41% with explicit contracts. CodeSpecBench shows 20.2% repo-level success. The paper's execution grounding is meant to catch bad specs, but if >60% of specs fail grounding, the method effectively degrades to 'generate specs → discard most → fall back to whatever survives' — potentially no better than test-only methods with fewer but higher-quality tests. The paper should include analysis of spec survival rates and graceful degradation behavior.\", \"TIMELINE MARGINAL: The manual estimate of 14-18 days with 2 researchers overlaps but can exceed the 16-day deadline. The upper bound should be trimmed to fit. Consider dropping one supplementary benchmark (e.g., RepoBench) to ensure the primary benchmarks are completed thoroughly.\"]\nFeedback: This is now a well-structured idea that has improved substantially through four rounds. The controlled experimental design with honest ablations is the strongest aspect. However, one critical competitor was discovered that must be addressed before this can pass:\n\n1. **CITE AND DIFFERENTIATE FROM PGS** (most important): PGS (arXiv:2506.18315) shares ExeSpec's core insight that properties outperform tests as LLM code feedback. Differentiate on: (a) ExeSpec execution-grounds the specs themselves (catches hallucinated specs before use), while PGS assumes properties are correct; (b) ExeSpec applies across 4 task types (generation, debugging, completion, issue resolution), PGS focuses on generation/repair; (c) ExeSpec's comprehensive spec schema (5 component types) vs. PGS's single-property checking; (d) ExeSpec's controlled ablation isolates each spec component's contribution. Add PGS as a fifth baseline condition, or at minimum cite and discuss in Related Work with clear differentiation.\n\n2. **CITE FSE 2025 AND ContractEval**: 'From Prompts to Properties' (FSE 2025) validates the property-vs-test framing from a PBT perspective. ContractEval (arXiv:2510.12047) both validates your problem (LLMs fail at contracts) and raises spec quality concerns — use it to motivate your execution grounding stage.\n\n3. **ADDRESS SWE-BENCH CONTAMINATION SERIOUSLY**: Either (a) add SWE-bench Pro as the primary SE benchmark alongside Verified, or (b) follow the paper's current plan but add a contamination analysis section comparing performance on instances with/without known gold patch exposure. Option (a) is safer but adds implementation effort.\n\n4. **ADD SPEC SURVIVAL RATE ANALYSIS**: Report what fraction of generated specs survive execution grounding by task type and model. If survival is low, analyze whether the surviving specs still provide gains over test-only methods. This directly addresses the CodeSpecBench/ContractEval concern and strengthens the paper's analytical contribution.\n\n5. **JUSTIFY MODEL CHOICE**: Add a sentence noting that Qwen2.5-Coder was selected as the strongest open-source code model available at experiment design time, and that the method is model-agnostic. If time permits, add one data point with a newer model.\n\nThese are all fixable in one more revision round. The idea's core structure, experimental design, and positioning are sound — the main gap is incomplete coverage of the competitive landscape.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"CRITICAL — PGS STILL NOT CITED (Round 4 issue unresolved): PGS (arXiv:2506.18315, 'Use Property-Based Testing to Bridge LLM Code Generation and Validation', June 2025, revised May 2026) shares ExeSpec's core contribution: using program properties instead of test cases for LLM code refinement at inference time. PGS achieves 97.6% HumanEval, 87.2% MBPP, 76.5% LiveCodeBench, 49.7% CodeContests, 37.3% SWE-bench Verified using DeepSeek-R1-32B. It reports 23.1-37.3% relative pass@1 gains over TDD methods and 1.4-1.6x higher bug fix rates. This paper validates ExeSpec's hypothesis but also substantially reduces its novelty. Without citing and differentiating from PGS, any informed reviewer will reject on novelty grounds.\", \"ROUND 4 ISSUES LARGELY UNADDRESSED: (1) ContractEval/PACT (arXiv:2510.12047) — shows 0% contract satisfaction under standard prompting, motivates execution grounding but raises spec quality concerns — not cited; (2) 'From Prompts to Properties' (FSE 2025 LLanMER) — validates property-vs-test framing — not cited; (3) 'Preconditions and Postconditions as Design Constraints' (IEEE Access 2025) — directly studies ExeSpec's premise with controlled experiments — not cited; (4) StoryCoder (arXiv:2604.14631) — concurrent training-free structured intermediate reasoning — not cited.\", \"SWE-BENCH VERIFIED CONTAMINATION INSUFFICIENTLY ADDRESSED: OpenAI has officially stopped reporting SWE-bench Verified scores (blog post: 'Why SWE-bench Verified no longer measures frontier coding capabilities'). Top score is 93.9% vs. ~46% on SWE-bench Pro. The idea mentions 'noting contamination concerns per OpenAI's 2026 audit' but still uses Verified as a primary benchmark without proposing SWE-bench Pro as an alternative or replacement. EMNLP reviewers aware of the contamination will question evaluation credibility.\", \"MODEL CURRENCY: Qwen3-Coder-Next (3B/80B MoE, 256k context, >70% SWE-bench Verified) and DeepSeek V4 have been released. Using Qwen2.5-Coder without justification looks dated. Either justify the choice (available at experiment design time, reproducibility) or add a data point with a newer model.\", \"NOVELTY BOUNDARY WITH PGS IS THIN: PGS uses LLM-generated abstract properties with execution-based validation and minimal counterexample feedback. ExeSpec uses LLM-generated behavioral specifications (pre/postconditions, invariants, type constraints) with execution grounding and structured violation reports. Both are training-free, inference-time, property-level-rather-than-test-level approaches. The genuine differentiators — (a) execution grounding of specs themselves (PGS assumes properties are ~87% accurate), (b) structured 5-component schema with component ablation, (c) multi-task applicability beyond generation — must be explicitly argued. Without this, the paper reads as a PGS variant with a different spec format.\", \"MISSING NL-DEBUGGING (EMNLP 2025 Oral): 'Natural Language as Intermediate Representation for Code Debugging' (arXiv:2505.15356) was accepted as an Oral at EMNLP 2025 — the same venue being targeted. It uses NL (not specifications) as an intermediate representation for debugging and shows consistent gains over code-level debugging. This is a strong baseline for the debugging task (DebugBench) and establishes the 'intermediate representation for code tasks' paradigm at this exact venue.\"]\nFeedback: The idea has matured substantially over 5 rounds — the experimental design with honest ablations, primary/supplementary benchmark distinction, and AlphaCodium baseline are all strong. However, the most critical Round 4 issue (PGS) remains unaddressed, and this is now blocking passage. Here is exactly what needs to change:\n\n1. **CITE AND DIFFERENTIATE FROM PGS** (highest priority, non-negotiable): Add PGS to key_references and landscape. Position ExeSpec's contributions BEYOND PGS's established result (properties > tests): (a) ExeSpec execution-grounds the specs themselves — PGS's verification asymmetry (87% property accuracy) means ~13% of properties are wrong, and PGS has no mechanism to catch them before use; ExeSpec's Stage 2 catches hallucinated specs via execution probes; (b) ExeSpec evaluates across 4 task types (generation, debugging, completion, issue resolution) while PGS evaluates generation and repair; (c) ExeSpec's 5-component schema with component ablation provides fine-grained analysis of which spec types help which tasks — PGS treats properties as a monolithic category. Consider adding PGS as a 5th baseline condition on at least CodeContests and DebugBench, or at minimum cite and discuss with clear differentiation.\n\n2. **ADDRESS SWE-BENCH CONTAMINATION**: Either (a) replace SWE-bench Verified with SWE-bench Pro as primary (preferred — aligns with community trend), or (b) keep Verified but add contamination analysis comparing performance on high-contamination vs. low-contamination instances (requires the contamination labels from OpenAI's audit). Option (a) adds implementation effort but makes the paper future-proof.\n\n3. **CITE ADDITIONAL MISSING WORK**: Add to key_references and discuss in landscape: ContractEval/PACT (2510.12047), NL-Debugging (2505.15356, EMNLP 2025 Oral — important as it's at the same venue), 'From Prompts to Properties' (FSE 2025). These validate ExeSpec's problem framing and provide important context.\n\n4. **JUSTIFY OR UPDATE MODEL CHOICE**: Add one sentence: 'We use Qwen2.5-Coder as the strongest open-source code model with publicly available weights at experiment design time; the method is model-agnostic and we expect consistent gains across model generations.' If feasible within budget, add one supplementary data point with Qwen3-Coder-Next-3B to demonstrate model-agnostic applicability.\n\n5. **SHARPEN THE NARRATIVE**: After citing PGS, reframe ExeSpec's contribution as: 'PGS demonstrated that property-level feedback outperforms test-based feedback for code generation. We advance this finding in three ways: (1) we show that execution-grounded specification verification catches ~X% of hallucinated specs that would corrupt reasoning, (2) we extend property-level reasoning beyond generation to debugging, completion, and issue resolution, and (3) we decompose the contribution of different spec components (I/O, preconditions, postconditions, invariants, type constraints) across task types, providing actionable guidance for spec-mediated code reasoning.'\n\nThese changes are all feasible in one revision round. The idea's core structure is sound — it just needs to acknowledge and position against the competitive landscape that has emerged.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"CRITICAL — PGS STILL NOT CITED (4th consecutive round): PGS (arXiv:2506.18315, 'Use Property-Based Testing to Bridge LLM Code Generation and Validation', June 2025, revised May 2026) shares ExeSpec's core contribution: using LLM-generated properties (not tests) for code refinement with execution-based validation. PGS validates properties via soundness checks against public tests + sensitivity to known errors, then provides minimal counterexample feedback. It evaluates on HumanEval (97.6%), MBPP (81.2%), and LiveCodeBench (74.5%) with DeepSeek-R1-Distilled-32B. Note: PGS does NOT evaluate on CodeContests or SWE-bench (the Round 5 reviewer's numbers for those benchmarks were incorrect). ExeSpec's genuine differentiators vs. PGS: (1) execution-grounds specs themselves before use via probes, catching hallucinated specs; (2) covers 4 task types vs. PGS's generation-only scope; (3) structured 5-component schema with component ablation vs. PGS's monolithic property checking; (4) structured violation reports vs. minimal counterexamples. These are meaningful but incremental. This is the 4th consecutive round raising this issue — if unaddressed in the next round, this should be grounds for failure.\", \"NL-DEBUGGING STILL NOT CITED (EMNLP 2025 ORAL): NL-Debugging (arXiv:2505.15356, ACL Anthology 2025.emnlp-main.80) uses natural language as an intermediate representation for debugging, demonstrating gains over code-level debugging. Published as an ORAL at EMNLP 2025 — the exact target venue. This establishes the 'intermediate representation for code tasks' paradigm at this venue and is a critical baseline for DebugBench evaluation. Reviewers at EMNLP 2026 will know this paper.\", \"CONTRACTEVAL STILL NOT CITED: ContractEval (arXiv:2510.12047) shows 0% contract satisfaction under standard prompting, 23-41% with explicit contracts, 49-53% with contract-violating test examples. This validates ExeSpec's motivation (LLMs need grounding for spec generation) but also quantifies the spec quality challenge. Must be cited to strengthen the execution grounding motivation.\", \"SWE-BENCH VERIFIED CONTAMINATION INSUFFICIENTLY ADDRESSED: OpenAI has officially stopped reporting SWE-bench Verified scores. All frontier models show training data contamination — models can reproduce exact gold patches verbatim. Claude Opus 4.5 scores 80.9% on Verified but only 45.9% on Pro. While Qwen2.5-Coder (sub-frontier) may be less contaminated, the benchmark's credibility is severely damaged. The paper's approach of 'noting contamination concerns per OpenAI's 2026 audit' and 'reporting held-out test pass rates alongside standard metrics' is insufficient. Either: (a) add SWE-bench Pro as a co-primary benchmark, (b) demonstrate Qwen2.5-Coder-7B/32B are not contaminated on Verified via gold-patch reproduction tests, or (c) at minimum acknowledge that the community has moved to Pro and explain why Verified remains informative for sub-frontier models.\", \"MODEL CURRENCY UNJUSTIFIED: Qwen3-Coder-Next (3B active / 80B total MoE, 256k context, >70% SWE-bench Verified) has been released. Qwen2.5-Coder remains a valid reproducibility choice, but the paper needs one sentence justifying it (e.g., 'strongest open-source code model with dense architecture available at experiment design time; the method is model-agnostic'). Without justification, EMNLP reviewers may question currency.\", \"'FROM PROMPTS TO PROPERTIES' (FSE 2025/LLanMER) STILL NOT CITED: This paper applied property-based testing to evaluate StarCoder and CodeLlama on MBPP/HumanEval, finding 30-32% of generated solutions only partially adhere to correctness properties and 18-23% fail outright. Validates ExeSpec's property-vs-test framing from the evaluation side.\"]\nFeedback: This is Round 6, and the idea's experimental design, controlled baselines, and honest ablation commitment are genuinely strong. However, the repeated failure to cite PGS — now raised for the 4th consecutive round as non-negotiable — is becoming a disqualifying pattern. Here is exactly what must change:\n\n1. **CITE AND DIFFERENTIATE FROM PGS** (FINAL WARNING — if unaddressed in Round 7, this warrants failure): Add PGS to key_references and landscape. Note that PGS evaluates ONLY on HumanEval/MBPP/LiveCodeBench and does NOT evaluate on CodeContests, SWE-bench, or DebugBench — this is actually ExeSpec's opportunity. Position ExeSpec's contributions BEYOND PGS: (a) ExeSpec execution-grounds specs before use (probes catch hallucinated specs); PGS validates properties against public tests but doesn't catch internally inconsistent properties before use. (b) ExeSpec evaluates across 4 task types including debugging and issue resolution — PGS only covers generation. (c) ExeSpec's 5-component ablation decomposes which spec types help which tasks — PGS treats properties as monolithic. (d) ExeSpec directly compares against AlphaCodium on CodeContests (PGS's home turf overlap — neither AlphaCodium nor PGS compares against each other). Reframe the narrative: 'PGS demonstrated that property-level feedback outperforms test-based feedback for code generation. We advance this finding by: (1) showing execution-grounded spec verification catches hallucinated specs that corrupt reasoning, (2) extending property-level reasoning to debugging, completion, and issue resolution, (3) providing fine-grained ablation of which specification components help which task types.'\n\n2. **CITE NL-DEBUGGING AS DEBUGGING BASELINE**: Add NL-Debugging (2505.15356, EMNLP 2025 Oral) to key_references. Position ExeSpec's debugging approach as advancing beyond NL-level debugging by providing structured, execution-verified behavioral constraints (not just NL descriptions). If feasible, add NL-Debugging as a 5th baseline condition on DebugBench — this would strongly differentiate ExeSpec.\n\n3. **ADDRESS SWE-BENCH CONTAMINATION CONCRETELY**: Add one of: (a) 'We additionally evaluate on SWE-bench Pro on a representative subset to validate that gains generalize beyond Verified'; (b) 'We verify Qwen2.5-Coder models are not contaminated by testing gold-patch reproduction rates'; (c) 'We acknowledge SWE-bench Verified's contamination concerns are most severe for frontier models; Qwen2.5-Coder-7B/32B are sub-frontier models unlikely to have been trained on the SWE-bench gold patches.' Option (c) is the minimum acceptable response.\n\n4. **CITE CONTRACTEVAL AND 'FROM PROMPTS TO PROPERTIES'**: ContractEval (2510.12047) motivates execution grounding (0% contract satisfaction without it). 'From Prompts to Properties' (FSE 2025) validates the property-vs-test evaluation framing. Both strengthen ExeSpec's problem statement.\n\n5. **ADD MODEL JUSTIFICATION**: One sentence: 'We use Qwen2.5-Coder-7B/32B-Instruct as well-established dense models with strong code performance and reproducible inference via vLLM; the method is model-agnostic and we expect consistent gains across model generations.' If time/budget permit, add one supplementary data point with a Qwen3 model.\n\nThe core idea is sound and the experimental design is rigorous. But an EMNLP reviewer who has read PGS (published June 2025, revised May 2026 — highly visible) will immediately recognize the overlap and reject if PGS is not acknowledged. This is the most critical fix.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"CRITICAL — PGS STILL NOT CITED (5TH CONSECUTIVE ROUND): PGS (arXiv:2506.18315, 'Use Property-Based Testing to Bridge LLM Code Generation and Validation', June 2025, revised as 'Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback', May 2026) shares ExeSpec's core contribution: using LLM-generated abstract properties instead of test cases for code refinement with execution-based validation at inference time, training-free. PGS evaluates on HumanEval, MBPP, and LiveCodeBench ONLY (NOT CodeContests or SWE-bench — earlier reviewer claims about PGS's CodeContests/SWE-bench numbers were incorrect). PGS achieves 23.1-37.3% relative pass@1 improvement over TDD methods using DeepSeek-R1-Distilled-32B. This has been raised in Rounds 4, 5, 6, and 7 — all unaddressed. If unaddressed in Round 8, this MUST result in failure. No exceptions.\", \"NL-DEBUGGING STILL NOT CITED (3RD ROUND): NL-Debugging (arXiv:2505.15356, ACL Anthology 2025.emnlp-main.80) was accepted as an ORAL at EMNLP 2025 — the exact target venue. It uses natural language as an intermediate representation for debugging via backtranslation → NL refinement → regeneration, achieving substantial gains on APPS and Codeforces. EMNLP 2026 reviewers WILL know this paper. It establishes the 'structured intermediate representation for code tasks' paradigm at this venue and is a critical baseline for DebugBench evaluation.\", \"CONTRACTEVAL STILL NOT CITED (3RD ROUND): ContractEval (arXiv:2510.12047) shows 0% contract satisfaction under standard prompting, 23-41% with explicit contracts, 49-53% with example-augmented specification. This simultaneously validates ExeSpec's motivation (LLMs need grounding for contract/spec generation) AND quantifies the spec quality challenge. Must be cited to strengthen execution grounding motivation.\", \"ALPHACODIUM 44% CLAIM IS MISLEADING: The idea states 'AlphaCodium's flow engineering raises CodeContests pass@5 from 19% to 44%.' This is the VALIDATION SET result (117 problems). On the TEST SET (165 problems), AlphaCodium achieves 29% pass@5 (up from 12% baseline). The distinction must be clarified to avoid misleading readers.\", \"SWE-BENCH VERIFIED CONTAMINATION REMAINS INADEQUATELY ADDRESSED: OpenAI officially stopped reporting Verified scores in February 2026 after finding frontier models could reproduce verbatim gold patches. The current response ('noting contamination concerns, we report held-out test pass rates alongside standard metrics') is insufficient. Minimum acceptable: explicitly argue that Qwen2.5-Coder-7B/32B are sub-frontier models unlikely to exhibit the same contamination patterns as GPT-5.2/Claude Opus 4.5, and note that the community has moved to SWE-bench Pro. Better: add SWE-bench Pro as a co-primary benchmark.\", \"MODEL CURRENCY UNJUSTIFIED: Qwen3-Coder-Next (3B active/80B total MoE, 256k context, >70% SWE-bench Verified) was released February 2026. Using Qwen2.5-Coder without a justification sentence will invite reviewer questions. Add: 'We use Qwen2.5-Coder-7B/32B-Instruct as established dense models with reproducible vLLM inference; the method is model-agnostic.'\", \"MISSING ADDITIONAL RELEVANT WORK: (1) StoryCoder (arXiv:2604.14631, ACL 2026 Main) — training-free structured intermediate reasoning via narrative reformulation, +18.7% pass@10 across 11 models. Concurrent work using structured intermediate representations for code. (2) FixAudit (arXiv:2604.05560, April 2026) — jointly trains fixer and auditor, 35-37% improvement on CodeContests. (3) 'From Prompts to Properties' (FSE Companion 2025/LLanMER) — applies PBT to evaluate LLM code, finding 30-32% partial failures that pass@k misses. These should be cited in landscape or related work.\"]\nFeedback: This is Round 7, and the idea's experimental design, controlled baselines, and honest ablation commitment are the strongest aspects of the proposal. However, the repeated failure to cite PGS — now flagged for the 5TH CONSECUTIVE ROUND — is approaching disqualification territory. Here is exactly what must change:\n\n1. **CITE AND DIFFERENTIATE FROM PGS** (ABSOLUTE FINAL CHANCE — failure to address in Round 8 means automatic fail): Add PGS (arXiv:2506.18315) to key_references and landscape. Critically, note that PGS evaluates ONLY on HumanEval/MBPP/LiveCodeBench and does NOT evaluate on CodeContests, SWE-bench, or DebugBench. ExeSpec's differentiators vs. PGS: (a) ExeSpec execution-grounds specs BEFORE use via probes, catching hallucinated/contradictory specs — PGS validates properties against public tests but assumes ~87% property accuracy without catching internally inconsistent properties; (b) ExeSpec evaluates across 4 task types (generation, debugging, completion, issue resolution) — PGS covers generation/repair only; (c) ExeSpec's 5-component schema with component ablation decomposes which spec types help which tasks — PGS treats properties as a monolithic category; (d) ExeSpec directly compares against AlphaCodium on CodeContests, a benchmark neither PGS nor AlphaCodium compares against each other on. Reframe narrative: 'PGS demonstrated that property-level feedback outperforms test-based feedback for code generation. We advance this by: (1) execution-grounding specs to catch hallucinated properties, (2) extending to debugging/completion/issue-resolution, (3) decomposing spec component contributions via controlled ablation.'\n\n2. **CITE NL-DEBUGGING** (EMNLP 2025 Oral — reviewers at your target venue will know this): Add NL-Debugging (2505.15356) to key_references and landscape. Position ExeSpec's debugging as advancing beyond NL-level intermediate reasoning by providing structured, execution-verified behavioral constraints. Consider adding NL-Debugging as a 5th baseline condition on DebugBench for a strong venue-specific comparison.\n\n3. **CITE CONTRACTEVAL**: Add ContractEval (2510.12047) to motivate execution grounding: '0% contract satisfaction under standard prompting validates the need for execution-based spec verification.'\n\n4. **FIX ALPHACODIUM 44% CLAIM**: Clarify as 'AlphaCodium raises CodeContests validation-set pass@5 from 19% to 44% (test-set: 12% to 29%)' or simply cite the test-set numbers.\n\n5. **ADDRESS SWE-BENCH CONTAMINATION**: Add one paragraph: 'We use Qwen2.5-Coder-7B/32B, sub-frontier models unlikely to exhibit the verbatim gold-patch reproduction observed in frontier models (GPT-5.2, Claude Opus 4.5). We additionally note that the community has moved toward SWE-bench Pro for frontier evaluation; our results on sub-frontier models provide a contamination-resistant baseline.'\n\n6. **ADD MODEL JUSTIFICATION**: One sentence: 'We use Qwen2.5-Coder as established dense models with strong code performance and reproducible vLLM inference; the method is model-agnostic.'\n\nThe core structure is sound. Fix the competitive landscape and this can pass.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-12T02:12:09.829Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T02:12:09.829Z",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

## Round 1

100 recorded events

### User

_source line 3 · 2026-05-12T02:12:09.869Z_

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

## Idea under review (round 8/10)
{
  "title": "ExeSpec: Verifiable Specification Reasoning for Code LLMs via Execution Grounding",
  "core_problem": "Training-free inference-time methods for LLM code improvement—AlphaCodium (arXiv 2401.08500), CodeT (ICLR 2023), Self-Debugging (arXiv 2304.05128), S* (EMNLP 2025 Findings)—have demonstrated that execution feedback substantially boosts code generation quality using test cases as intermediate representations. Recently, PGS (arXiv 2506.18315, revised May 2026) showed that property-based feedback—abstract behavioral properties rather than I/O test cases—outperforms test-driven methods by 23.1–37.3% relative pass@1 on HumanEval, MBPP, and LiveCodeBench, validating that properties provide richer reasoning scaffolds than point-sample tests. However, three critical limitations remain unresolved. (1) Property reliability: LLM-generated properties are unreliable at scale—PGS reports property generation accuracy of only 48.9% on hard LiveCodeBench problems, ContractEval (arXiv 2510.12047) finds 0% contract satisfaction under standard prompting despite 75–82% pass@1, and CodeSpecBench (arXiv 2604.12268) reveals only 20.2% success at repo-level spec generation—yet no method systematically execution-grounds properties before use to catch hallucinated or internally contradictory specifications. PGS validates properties against public test cases for soundness but does not check inter-property consistency or proactively detect contradictions within the property set. (2) Task generalization: PGS and all property/test-based inference-time methods evaluate exclusively on code generation and simple repair (HumanEval, MBPP, LiveCodeBench), without extension to debugging (where intended-vs-observed behavioral contrasts are needed), issue resolution (where behavioral changes must be extracted from issue context and failing tests), or cross-file completion (where interface contracts must be inferred). NL-Debugging (EMNLP 2025 Main) demonstrated that natural language intermediate representations improve debugging by 4–6pp over code-level methods, but NL descriptions lack the structured, execution-verifiable format needed for systematic property checking. (3) Property decomposition: all property-based methods treat properties as a monolithic category—no work decomposes which property types (preconditions, postconditions, invariants, type constraints, I/O examples) contribute to which task types, preventing targeted optimization. Can execution-grounded, decomposed behavioral specifications address property reliability while extending property-based reasoning across diverse code tasks without model training?",
  "opportunity": "Five research threads converge but remain disconnected: (1) Test-based inference-time refinement (AlphaCodium, CodeT, Self-Debugging, S*, BACE) proves execution feedback improves code generation—AlphaCodium raises CodeContests pass@5 from 19% to 44% on the validation set (12% to 29% on the 165-problem test set), CodeT improves HumanEval pass@1 by +18.8pp via dual execution agreement, S* enables a 3B model to outperform GPT-4o-mini on LiveCodeBench—but all use test cases (point samples) as the intermediate representation. (2) Property-based refinement: PGS (arXiv 2506.18315) demonstrates that LLM-generated abstract properties outperform test-driven feedback by 23.1–37.3% relative pass@1, establishing that property-level reasoning is superior to test-level reasoning for code refinement. However, PGS evaluates only on HumanEval/MBPP/LiveCodeBench (not CodeContests, SWE-bench, or debugging benchmarks), reports property generation accuracy dropping to 48.9% on hard problems, and does not verify inter-property consistency before use. Self-Spec (Agents4Science 2025) showed model-authored specs improve generation by +2–5pp but never verifies specs against execution. ContractEval (arXiv 2510.12047) reveals 0% contract satisfaction under standard prompting despite 75–82% pass@1, rising to only 23–41% with explicit contracts—demonstrating that even when contracts are provided, LLMs struggle to enforce them, motivating execution-based verification. 'From Prompts to Properties' (FSE Companion 2025/LLanMER) finds 30–32% of LLM-generated solutions exhibit partial property failures that pass@k metrics miss entirely. (3) Structured intermediate representations for code: NL-Debugging (EMNLP 2025 Main, arXiv 2505.15356) uses natural language as an intermediate representation for debugging via backtranslation → NL refinement → regeneration, outperforming code-level debugging by 4–6pp on APPS and Codeforces—establishing that higher-level abstractions aid debugging at ExeSpec's target venue. StoryCoder (ACL 2026 Main, arXiv 2604.14631) demonstrates narrative reformulation as structured intermediate reasoning, achieving +18.7% pass@10 across 11 models—concurrent work validating that structured intermediate representations improve code generation. Both use natural language (unverified against execution), not execution-grounded behavioral specifications. (4) Execution-grounded training (Think Like You Execute, RLEF at ICML 2025, FixAudit arXiv 2604.05560) achieves dramatic gains but requires fine-tuning—not usable with frozen models. FixAudit jointly trains fixer and auditor achieving 35–37% improvement on CodeContests, demonstrating the value of audit-style verification but requiring training. (5) Specification quality challenges: CodeSpecBench reveals 20.2% repo-level spec accuracy; 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025) shows self-generated test feedback introduces systematic bias—motivating richer, verified intermediate representations. The unexploited synthesis: PGS proved properties outperform tests, but property reliability remains the bottleneck (48.9% accuracy on hard problems). Execution grounding can close this gap—verifying LLM-generated property-level specs before use, catching hallucinated and contradictory properties. Additionally, decomposing properties into typed components (pre/postconditions, invariants, type constraints) and evaluating across task types (generation, debugging, issue resolution, completion) addresses the generalization gap that no prior work has tested.",
  "landscape": "**Test-based inference-time methods.** AlphaCodium (arXiv 2401.08500, Jan 2024) is a training-free multi-stage flow with problem reflection, AI test generation, and iterative execution-based refinement with test anchoring, raising CodeContests validation-set pass@5 from 19% to 44% and test-set pass@5 from 12% to 29% with GPT-4. CodeT (ICLR 2023, arXiv 2207.10397) generates tests via LLMs and uses dual execution agreement for solution selection, improving HumanEval pass@1 by +18.8pp. Self-Debugging (arXiv 2304.05128) teaches LLMs to iteratively debug using execution results and natural language explanations, achieving up to 12% improvement on TransCoder and MBPP. 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025 Long, arXiv 2501.12793) reveals systematic bias in self-generated tests—in-execution debugging using intermediate program states mitigates this, demonstrating that test quality is a fundamental bottleneck for test-based methods. S* (EMNLP 2025 Findings, arXiv 2502.14382) combines parallel sampling with sequential debugging and adaptive distinguishing input synthesis, enabling a 3B model to outperform GPT-4o-mini on LiveCodeBench. BACE (GECCO 2026, arXiv 2603.28653) treats generated tests as noisy sensors via Bayesian updates, outperforming CodeSIM by +2.5–5.4pp on LiveCodeBench v6. All use test cases as the intermediate representation—point samples that verify specific inputs but don't capture universal behavioral properties.\n\n**Property-based and specification approaches.** PGS (arXiv 2506.18315, June 2025; revised as 'Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback', May 2026) is the closest prior work. PGS introduces a Generator-Tester framework where the Tester generates abstract behavioral properties (e.g., 'the product of output factors must equal the input integer') and validates code against them using property-based testing, with structurally minimal counterexamples as feedback. PGS achieves 23.1–37.3% relative pass@1 improvement over TDD methods (Reflexion, Self-Debugging, MGDebugger) using DeepSeek-Coder-V2, Qwen2.5-Coder, and DeepSeek-R1-Distilled-32B on HumanEval, MBPP, and LiveCodeBench. PGS validates properties against public test cases for soundness, reporting property generation accuracy of 82.4% (easy), 62.8% (medium), and 48.9% (hard) on LiveCodeBench. Critically, PGS does not check inter-property consistency, does not evaluate on CodeContests, SWE-bench, or debugging benchmarks, and treats properties as a monolithic category without decomposing which property types contribute to which tasks. ExeSpec differs from PGS in three ways: (a) execution grounding verifies specs before use via candidate-code probes and cross-spec consistency checks, catching hallucinated and contradictory specs that PGS's public-test validation misses; (b) evaluation spans four task types (generation, debugging, issue resolution, completion) on benchmarks PGS does not cover (CodeContests, SWE-bench Pro, DebugBench); (c) a 5-component schema with controlled ablation decomposes property contributions per task type. Self-Spec (Agents4Science 2025) has LLMs author specification languages before code generation, improving GPT-4o HumanEval pass@1 from 87% to 92%, but only evaluates on HumanEval and never verifies specs against execution. ContractEval (arXiv 2510.12047) benchmarks contract satisfaction in code generation, finding 0% satisfaction under standard prompting despite 75–82% pass@1 scores, 23–41% with explicit contracts, and 49–53% with example-augmented specifications—simultaneously validating that LLMs need external grounding for contract/spec enforcement AND quantifying the difficulty of the spec quality challenge. 'From Prompts to Properties' (FSE Companion 2025/LLanMER) applies property-based testing to evaluate LLM code, finding 30–32% partial property failures that pass@k metrics miss, motivating property-level evaluation. SpecRover/AutoCodeRover-v2 (ICSE 2025) performs iterative NL specification inference for automated program repair, achieving 19.31% on SWE-bench. VibeRepair (arXiv 2602.08263) translates code into NL behavioral specs for repair but specs are imprecise. SSDE (FSE Companion 2026, arXiv 2605.02455) uses Gherkin specifications and domain models for repo-level MVC generation—concurrent work demonstrating structured specs guide LLM generation, but requires human-authored specifications. CodeSpecBench (arXiv 2604.12268) benchmarks LLM spec generation showing only 20.2% repo-level pass rate, motivating execution-based verification.\n\n**Structured intermediate representations.** NL-Debugging (EMNLP 2025 Main, ACL Anthology 2025.emnlp-main.80, arXiv 2505.15356) uses natural language as an intermediate representation for code debugging via a three-stage pipeline: backtranslation (buggy code → NL sketch), NL refinement (identify and correct logical flaws in the NL representation using execution feedback), and regeneration (refined NL → corrected code). NL-Debugging outperforms code-level Self-Debugging by 4–6pp pass@1 on APPS and Codeforces across difficulty levels using GPT-4o-mini, Claude-3.5-Sonnet, and DeepSeek-Coder-V2-Lite. The key finding is that the 'Sketch' NL format—detailed natural language descriptions—enables broader modification space than code-level edits, and that refinement in the NL space (not NL→code translation) drives the gains. This establishes structured intermediate representations as valuable for debugging at ExeSpec's target venue (EMNLP). ExeSpec's specifications provide a more structured, execution-verifiable intermediate representation than free-form NL sketches—enabling systematic property checking rather than holistic NL reasoning. StoryCoder (ACL 2026 Main, arXiv 2604.14631) transforms code generation problems into structured narratives (task overview, constraints, test examples), achieving +18.7% zero-shot pass@10 across 11 models on HumanEval, LiveCodeBench, and Codeforces—concurrent training-free work validating structured reformulation, but using narrative structure rather than behavioral specifications. SCoT (ACL 2024) adds program structure to CoT without execution grounding.\n\n**Execution-grounded and RL training methods.** Think Like You Execute (arXiv 2512.00127) achieves +22–27pp on CRUXEval/LiveCodeBench via fine-tuning on 54K execution-trace-verified rationales. EG-CFG (NeurIPS 2025, arXiv 2506.10948) uses real-time execution via beam search over candidate lines—computationally expensive and generation-only. RLEF (ICML 2025) trains code LLMs with RL execution feedback. Think Anywhere (arXiv 2603.29957) enables on-demand reasoning during code generation via RL training. CURE (NeurIPS 2025 Spotlight) co-evolves coder and tester via RL. FixAudit (arXiv 2604.05560) jointly trains a fixer and auditor—the auditor generates new tests revealing implementation-specific bugs in the fixer's candidate code, achieving 35–37% pass@1 improvement on APPS, CodeContests, and xCodeEval with a 7B model. All require training—not applicable with frozen models.\n\n**The gap.** PGS established that property-based feedback outperforms test-based feedback for code generation. Three open questions remain: (1) Can execution grounding improve property reliability beyond PGS's public-test validation (addressing the 48.9% accuracy on hard problems)? (2) Do property-based approaches generalize to debugging, issue resolution, and completion—task types no property-based method has evaluated? (3) Which property types contribute to which tasks? No work addresses all three questions in a unified, training-free framework with controlled experimental design.",
  "approach": "We propose ExeSpec, a training-free inference-time framework that uses execution-grounded behavioral specifications as verifiable structured intermediate reasoning for LLM code tasks. Building on PGS's demonstration that property-based feedback outperforms test-based feedback for code generation, ExeSpec advances the property-based paradigm in three directions: (1) execution grounding that verifies spec consistency and catches hallucinated properties before downstream use, (2) extension to debugging, issue resolution, and cross-file completion beyond generation/repair, and (3) decomposition of specifications into typed components with controlled ablation.\n\n**Stage 1: Spec Elicitation.** Given a task input, prompt the LLM to generate structured behavioral specifications in a lightweight JSON schema containing five component types: (a) I/O example pairs (shared with both PGS properties and AlphaCodium test cases—the overlap region), (b) preconditions (constraints on valid inputs/states, e.g., 'n >= 0', 'input list is non-empty'), (c) postconditions (properties guaranteed on outputs, e.g., 'output is sorted in ascending order', 'len(output) == len(input)'), (d) type constraints (parameter and return type annotations with generics), and (e) invariants (loop invariants, monotonicity, ordering properties). The schema is task-adapted: generation tasks derive specs from docstrings; debugging tasks elicit intended-vs-observed behavioral contrasts; issue resolution tasks extract expected behavioral changes from issue descriptions and failing test context; completion tasks infer interface contracts from cross-file context.\n\n**Stage 2: Execution Grounding.** This is ExeSpec's primary differentiator from PGS. While PGS validates properties against public test cases for soundness, ExeSpec additionally performs: (i) cross-spec consistency checking—verifying that preconditions, postconditions, invariants, and type constraints are mutually satisfiable and non-contradictory (e.g., a postcondition asserting 'output is sorted' does not contradict an invariant asserting 'elements maintain original order'); (ii) candidate-code probing—generating a quick candidate solution, executing against spec-derived assertions including both I/O examples AND postcondition property checks, identifying spec-execution mismatches, and revising contradicted specs before final generation. For debugging tasks: execute the buggy code, compare execution traces against specs to identify precisely which behavioral constraints are violated, producing structured violation reports. For issue resolution (SWE-bench Pro): extract behavioral expectations from issue descriptions and failing tests, generate specs characterizing the intended fix behavior, and validate spec consistency against the existing test suite via Docker-based execution. For cross-file completion: static grounding via type inference from imported modules, parameter/return types from call-site usage context, and validation via type checkers (mypy/pyright for Python, tsc for TypeScript). When full execution is unavailable, static grounding serves as fallback: cross-spec consistency checking, type inference, and contradiction detection.\n\n**Stage 3: Spec-Guided Task Completion.** Feed grounded specs alongside the original task input to the LLM for final output. When outputs violate specs, structured violation reports (which constraints failed, expected vs. actual, which spec component) feed back for iterative refinement (up to 3 rounds). Unlike PGS's structurally minimal counterexamples, ExeSpec's feedback references typed behavioral properties ('postcondition: output must be monotonically increasing') with component attribution, enabling the LLM to reason about which aspect of behavioral intent was violated.\n\n**Baselines and controlled experiments.** The experimental design isolates contributions through six controlled conditions: (a) ExeSpec full (5-component specs + execution grounding), (b) PGS baseline (property-based testing following PGS's Generator-Tester framework, reimplemented on our benchmarks—the paper's critical comparison, isolating the contribution of execution grounding and component decomposition beyond PGS's approach), (c) AlphaCodium-style baseline (problem reflection + AI test generation + iterative execution/refinement with test anchoring—isolating the property-vs-test distinction, extending PGS's finding to new benchmarks), (d) Self-Spec baseline (specs without execution grounding—isolating the grounding contribution), (e) direct prompting (no intermediate reasoning), (f) NL-Debugging baseline on DebugBench only (NL intermediate representation via backtranslation/refinement/regeneration—isolating structured specs vs. free-form NL for debugging, providing venue-relevant comparison to EMNLP 2025 work). The delta between (a) and (b) is the paper's core contribution—whether execution grounding and component decomposition provide gains beyond PGS's property-based approach. The delta between (b) and (c) replicates PGS's finding (properties > tests) on new benchmarks (CodeContests, DebugBench, SWE-bench Pro) where PGS has not been evaluated. A critical spec-component ablation further decomposes: (i) full specs (I/O + pre/postconditions + invariants + type constraints), (ii) I/O-only specs (functionally equivalent to test cases—if this matches full specs, the novelty claim collapses), (iii) structural specs only (pre/postconditions + invariants + type constraints, no I/O)—this ablation is the critical honesty test.\n\n**Benchmarks.** Primary benchmarks with all six conditions + spec-component ablation: DebugBench (C++/Java/Python debugging—specs naturally capture intended-vs-observed behavioral contrasts, and NL-Debugging comparison is venue-relevant), CodeContests (competitive programming—direct comparison to AlphaCodium on its home benchmark, and first evaluation of PGS-style property feedback on CodeContests), and SWE-bench Pro (real-world issue resolution—adopted as co-primary benchmark given that SWE-bench Verified is compromised by contamination in frontier models; OpenAI stopped reporting Verified scores in February 2026 after finding frontier models could reproduce verbatim gold patches. We use Qwen2.5-Coder-7B/32B, sub-frontier models unlikely to exhibit the verbatim gold-patch reproduction observed in GPT-5.2 and Claude Opus 4.5, providing a contamination-resistant evaluation baseline. We report results on both SWE-bench Pro and Verified for completeness, noting the community's shift toward Pro for reliable evaluation). Supplementary benchmarks with ExeSpec vs. direct prompting only: HumanEval+/MBPP+ (for Self-Spec and PGS comparability—PGS reports results on these benchmarks, enabling direct numerical comparison), CrossCodeEval and RepoBench (cross-file completion with static grounding via type checkers). We explicitly acknowledge that cross-file completion relies on weaker static grounding than dynamic execution and report the proportion of instances where only static grounding was available.\n\n**Models.** We use Qwen2.5-Coder-7B-Instruct and Qwen2.5-Coder-32B-Instruct as established dense models with strong code performance and reproducible vLLM inference; the method is model-agnostic and we expect gains to transfer to newer architectures including MoE models (e.g., Qwen3-Coder-Next). Using established models enables direct comparison with PGS, which evaluates Qwen2.5-Coder on the same model family.\n\n**Analysis.** Beyond standard metrics: (1) spec quality analysis—correlation between spec correctness and downstream task performance; (2) grounding effectiveness—proportion of hallucinated specs caught by execution grounding vs. PGS's public-test validation (the key comparison); (3) spec-component contribution—which spec types most improve each task type; (4) test overfitting rates—proportion of solutions passing visible tests but failing held-out tests, comparing ExeSpec vs. baselines; (5) property accuracy by difficulty—replicating PGS's accuracy breakdown (82.4%/62.8%/48.9% by difficulty) on our benchmarks and measuring whether execution grounding improves it; (6) qualitative case studies showing where execution-grounded specs enable corrections that both test-only and ungrounded property methods miss.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~150–200 H100-hours (primary benchmarks DebugBench + CodeContests + SWE-bench Pro with 6 conditions × 2 models + NL-Debugging on DebugBench + spec-component ablation on primary benchmarks; supplementary HumanEval+/MBPP+ + CrossCodeEval + RepoBench with ExeSpec vs. direct prompting × 2 models; PGS baseline reimplementation on all primary benchmarks; using vLLM batch inference with Qwen2.5-Coder-7B on 1 H100 and 32B on 1–2 H100s)",
      "gpu_utilization": "Moderate (~40–55%): alternating between inference bursts and execution-grounding phases; SWE-bench Pro Docker execution and DebugBench compilation are CPU-bottlenecked",
      "timeline": "18–22 days (days 1–4: framework implementation + PGS baseline reimplementation following published Generator-Tester method + AlphaCodium baseline adaptation from open-source code + NL-Debugging baseline setup + eval harness configuration leveraging SWE-bench Docker harness and EvalPlus; days 5–8: primary benchmarks DebugBench + CodeContests with all 6 conditions; days 9–12: SWE-bench Pro + SWE-bench Verified with all 6 conditions; days 13–14: supplementary benchmarks HumanEval+/MBPP+ + CrossCodeEval + RepoBench with ExeSpec vs. direct prompting; days 15–17: spec-component ablation + grounding effectiveness analysis + property accuracy comparison vs. PGS; days 18–22: writing + analysis)",
      "team": "2 researchers (1 lead for ExeSpec framework + execution-grounding pipeline + spec-component ablation design, 1 for PGS/AlphaCodium/NL-Debugging baseline reimplementation + benchmark integration + evaluation infrastructure)",
      "estimated_gpu_cost": "$450–600 (on-demand H100 at ~$3/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "~170–230 H100-hours (same scope as manual with more systematic spec quality validation, PGS comparison analysis, and additional analysis iterations)",
      "gpu_utilization": "Moderate–High (~50–65%): agent queues experiment batches across benchmarks while human reviews spec quality and PGS baseline fidelity between rounds",
      "timeline": "14–18 days (agent handles framework code, experiment orchestration, and result collection; human validates spec schema design, reviews PGS and AlphaCodium baseline fidelity, and guides ablation priorities)",
      "team": "1 researcher, ~3–4 hrs/day reviewing spec elicitation outputs, validating PGS baseline implementation matches the published Generator-Tester framework, reviewing NL-Debugging baseline, approving experiment plans, and analyzing results",
      "claude_api_cost": "$150–250 (1500–2500 orchestration turns at ~$0.10/turn)",
      "estimated_gpu_cost": "$510–690",
      "risk_note": "PGS baseline reimplementation fidelity is critical—must reproduce the Generator-Tester property-based testing framework faithfully; NL-Debugging baseline must reproduce the backtranslation→NL refinement→regeneration pipeline; SWE-bench Pro evaluation infrastructure may require additional setup compared to the established Verified harness"
    },
    "auto_research": {
      "gpu_hours": "~200–270 H100-hours (systematic sweeps over spec granularity levels, grounding strategies per benchmark, additional model backbone DeepSeek-R1-Distilled-32B for PGS comparability, temperature and sample-count variations)",
      "gpu_utilization": "High (~80–90%): agent pipelines experiments back-to-back with minimal idle; parallel runs across benchmarks on multiple H100s",
      "timeline": "8–12 days with 4–8 H100s available concurrently (bottlenecked by SWE-bench Pro Docker execution and DebugBench compilation)",
      "team": "0 (initial setup ~4–5 hours for benchmark harness configuration, PGS/AlphaCodium/NL-Debugging baseline setup, and vLLM model serving, then fully autonomous)",
      "claude_api_cost": "$250–450 (2500–4500 turns for iterative experiment design, cross-benchmark analysis, and paper drafting)",
      "estimated_gpu_cost": "$600–810",
      "speed_bottleneck": "SWE-bench Pro Docker-based test execution and DebugBench compilation/execution; inference itself is fast with vLLM on H100",
      "risk_note": "Agent may over-optimize for one benchmark; need guardrails to ensure PGS baseline is faithfully implemented (not strawmanned), NL-Debugging baseline is accurate, and spec-component ablation runs completely even if early results are unfavorable"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission May 25, 2026; commitment Aug 2, 2026; NLP and Code Models track; Budapest, Hungary)",
    "ACL 2027 (expected ARR commitment ~Jan 2027; fallback if EMNLP revision needed)",
    "NAACL 2027 (expected ARR commitment ~Mar 2027; second fallback)"
  ],
  "level": "solid",
  "key_references": [
    "Use Property-Based Testing to Bridge LLM Code Generation and Validation / Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback (PGS; arXiv 2506.18315, June 2025, revised May 2026)",
    "NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging (EMNLP 2025 Main, ACL Anthology 2025.emnlp-main.80, arXiv 2505.15356)",
    "ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation (arXiv 2510.12047)",
    "AlphaCodium: Code Generation through Flow Engineering (arXiv 2401.08500, Jan 2024)",
    "CodeT: Code Generation with Generated Tests (ICLR 2023, arXiv 2207.10397)",
    "Teaching Large Language Models to Self-Debug (Self-Debugging; arXiv 2304.05128, 2023)",
    "Revisit Self-Debugging with Self-Generated Tests for Code Generation (ACL 2025 Long, arXiv 2501.12793)",
    "S*: Test Time Scaling for Code Generation (EMNLP 2025 Findings, arXiv 2502.14382)",
    "BACE: Bayesian Anchored Co-Evolution of Code and Test Populations (GECCO 2026, arXiv 2603.28653)",
    "Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation (Agents4Science 2025)",
    "StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation (ACL 2026 Main, arXiv 2604.14631)",
    "FixAudit: An Iterative Test-and-Repair Framework for Competitive Code Generation (arXiv 2604.05560)",
    "From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing (FSE Companion 2025/LLanMER, ACM 10.1145/3696630.3728702)",
    "Execution Guided Line-by-Line Code Generation (EG-CFG; NeurIPS 2025, arXiv 2506.10948)",
    "Think Like You Execute: Verifiable Chain of Thought from Program Traces (arXiv 2512.00127)",
    "Think Anywhere in Code Generation (arXiv 2603.29957, Mar 2026)",
    "SpecRover: Code Intent Extraction via LLMs (ICSE 2025)",
    "CURE: Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning (NeurIPS 2025 Spotlight)",
    "Code Execution as Grounded Supervision for LLM Reasoning (EMNLP 2025)",
    "CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (arXiv 2604.12268, Apr 2026)",
    "Specification Vibing for Automated Program Repair (VibeRepair; arXiv 2602.08263, Feb 2026)",
    "LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering (SSDE; FSE Companion 2026, arXiv 2605.02455)",
    "Investigating Test Overfitting on SWE-bench (arXiv 2511.16858)",
    "The Undecidability of Overfitting in Automated Program Repair (ICSE 2026 NIER)",
    "RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning (ICML 2025)",
    "Structured Chain-of-Thought Prompting for Code Generation (SCoT; ACL 2024)",
    "Qwen2.5-Coder Technical Report (arXiv 2409.12186)"
  ],
  "description": "We propose ExeSpec, a training-free inference-time framework that uses execution-grounded behavioral specifications as verifiable structured intermediate reasoning for LLM code tasks. Building on PGS's demonstration (arXiv 2506.18315) that property-based feedback outperforms test-based methods by 23.1–37.3% relative pass@1 on generation benchmarks, ExeSpec advances the property-based paradigm in three directions: (1) execution grounding that verifies spec consistency and catches hallucinated properties before downstream use—addressing PGS's property accuracy drop to 48.9% on hard problems and ContractEval's finding of 0% contract satisfaction under standard prompting; (2) extension to four task types (generation, debugging, issue resolution, completion) on benchmarks PGS does not cover (CodeContests, DebugBench, SWE-bench Pro); (3) decomposition into 5 typed spec components (I/O examples, preconditions, postconditions, invariants, type constraints) with controlled ablation revealing which components aid which tasks. The method operates in three stages: Spec Elicitation (task-adapted structured spec generation), Execution Grounding (cross-spec consistency checking + candidate-code probing to verify specs before use), and Spec-Guided Completion (grounded specs as verified intermediate reasoning with typed violation feedback). The experimental design isolates contributions through six conditions: (a) ExeSpec full, (b) PGS baseline (property-based testing reimplemented on our benchmarks—the critical comparison isolating execution grounding's contribution), (c) AlphaCodium-style baseline (test-based—extending PGS's property-vs-test finding to new benchmarks), (d) Self-Spec baseline (specs without grounding), (e) direct prompting, (f) NL-Debugging baseline on DebugBench (NL intermediate representation from EMNLP 2025—venue-relevant comparison). The spec-component ablation tests whether I/O-only specs match full specs (if so, the novelty claim collapses—reported honestly). Primary benchmarks: DebugBench (debugging), CodeContests (competitive programming, AlphaCodium's benchmark), SWE-bench Pro (issue resolution, replacing Verified as primary due to contamination—Qwen2.5-Coder-7B/32B are sub-frontier models unlikely to exhibit the verbatim gold-patch reproduction observed in frontier models). Supplementary: HumanEval+/MBPP+ (PGS/Self-Spec comparability), CrossCodeEval/RepoBench (completion with static grounding). Models: Qwen2.5-Coder-7B/32B-Instruct as established dense models with reproducible vLLM inference; the method is model-agnostic. Within 150–200 H100-hours and ~20 days. Primary target: EMNLP 2026 (ARR May 25, 2026).",
  "project_name": "test_spec_guided_repair",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL VENUE MISMATCH: User explicitly requested EMNLP 2026 (ARR deadline 2026-05-25, NLP and Code Models track), but the idea targets ICSE 2027, AAAI 2027, and FSE 2027 — all SE venues. The idea must be redesigned or reframed for EMNLP.", "CRITICAL COMPUTE VIOLATION: User constrained to ≤200 H100-hours total. The idea estimates 250-400 A100-80GB hours (manual mode). Running Kimi K2-Instruct (1T params MoE, requiring 4×A100 per instance) adds substantial inference costs not fully accounted for.", "CRITICAL TIMELINE VIOLATION: User has ~14 days. The idea estimates 3-5 months (manual), 6-10 weeks (HIL), or 1-3 weeks with 8-16 A100s (auto). None of these fit the user's constraint.", "EVAL BENCHMARK MISMATCH: User requested evaluation on SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, and CodeContests. The idea only covers SWE-bench Verified and Defects4J (which isn't even in the user's list). Missing 5 of 6 required benchmarks.", "MISSING CRITICAL RELATED WORK: (1) SpecRover/AutoCodeRover-v2 (ICSE 2025) — already does specification inference for patching; (2) CURE (NeurIPS 2025 Spotlight) — RL co-evolution of coder and tester; (3) CodeSpecBench (arXiv 2604.12268, Apr 2026) — benchmark showing LLMs achieve only 20.2% on repo-level behavioral spec generation; (4) Test overfitting undecidability (ICSE 2026 NIER) + empirical study (arXiv 2511.16858) showing 21-33% of LLM patches overfit on visible tests; (5) Dynamic Cogeneration at Google (arXiv 2601.19066); (6) SWE-Tester (arXiv 2601.13713).", "NOVELTY CONCERN: The idea is too similar to VibeRepair (arXiv 2602.08263, Feb 2026). VibeRepair already translates code into structured behavioral specifications for repair, achieving SOTA on Defects4J. The proposed delta — using test assertions instead of NL as the specification source — is an incremental variant, not a fundamentally new paradigm. SpecRover (ICSE 2025) also does specification inference for repair.", "TOPIC SCOPE TOO NARROW: User asked for 'code understanding and generation' covering repo-level comprehension, code reasoning, debugging, test generation, code-to-documentation, cross-language transfer. The idea focuses narrowly on Java program repair via Defects4J, which is only one subtask and one language.", "MISLEADING CLAIMS: '174/178 correct repairs' reads as a fraction but actually means 174 on v1.2 and 178 on v2.0. 'Proving specification-level repair is superior' overstates VibeRepair's own conclusions. The 48.29% for Repair-R1 represents only a 2.68pp improvement over baseline.", "TEST OVERFITTING NOT ADDRESSED: An ICSE 2026 NIER paper proves test overfitting is theoretically undecidable when full specifications are unavailable. An empirical study shows 21-33% of LLM patches overfit on visible tests. The idea's reliance on auto-generated tests as specifications is directly vulnerable to this fundamental limitation."]
Feedback: This idea has a reasonable technical intuition (test assertions as behavioral specs) but fundamentally fails to meet the user's requirements. Here is what needs to change:

1. **VENUE**: Reframe for EMNLP 2026 (NLP and Code Models track) or propose a different idea entirely. For EMNLP, the contribution must emphasize NLP methodology (e.g., how LLMs reason about code specifications, a new inference-time algorithm for code understanding) rather than SE pipeline engineering. EMNLP reviewers care about language model capabilities, not Defects4J leaderboard numbers.

2. **SCOPE**: Broaden beyond Java program repair. The user wants 'code understanding and generation' covering multiple tasks (debugging, test generation, code reasoning, cross-language transfer). Consider a method that applies across multiple code tasks, not just APR.

3. **BENCHMARKS**: Must evaluate on the user's required benchmarks: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests. Drop Defects4J (not requested).

4. **COMPUTE**: Stay within ≤200 H100-hours. Use smaller models (DeepSeek-Coder-V2-Lite-Instruct 16B, StarCoder2-15B, Qwen2.5-Coder-7B/32B) as the user suggested, not 1T-param Kimi K2. This also aligns with the user's suggested model list.

5. **TIMELINE**: Design for ≤16 days of execution. Build on existing frameworks (aider, SWE-agent, Moatless) as the user suggested. The current 3-5 month estimate is a non-starter.

6. **NOVELTY BOOST**: Differentiate more clearly from VibeRepair and SpecRover. Instead of 'yet another spec-guided repair pipeline,' consider: (a) a novel inference algorithm that uses execution feedback to iteratively refine code understanding, (b) a retrieval-augmented approach with semantic code search for cross-repo transfer, or (c) a method for repo-level context compression that enables better code reasoning — all directions the user explicitly suggested.

7. **ADDRESS TEST OVERFITTING**: Any test-based approach must engage with the ICSE 2026 undecidability result and the empirical overfitting findings. Propose concrete mitigation strategies.

### Round 2 review
Verdict: revise
Issues: ["MISSING CRITICAL BASELINES: AlphaCodium (arXiv 2401.08500, Jan 2024) is a training-free, inference-time, test-based iterative flow with problem analysis + AI test generation + iterative refinement against tests. It is the most direct conceptual predecessor to ExeSpec and MUST be cited and compared as a baseline. CodeT (ICLR 2022) and Self-Debugging (arXiv 2304.05128, 2023) are also missing—both are foundational works in execution-based code refinement at inference time.", "MISSING CONCURRENT WORK: BACE (arXiv 2603.28653, Mar 2026) addresses the same 'noisy self-generated tests' problem via Bayesian co-evolution of code and test populations. 'Revisit Self-Debugging with Self-Generated Tests' (arXiv 2501.12793, Jan 2025) directly studies post-execution vs. in-execution self-debugging paradigms with LLM-generated tests. Both must be discussed.", "THIN NOVELTY BOUNDARY: The distinction between 'structured behavioral specifications' (I/O example pairs, pre/postconditions, invariants in JSON schema) and 'self-generated test assertions' is conceptually thin. I/O examples ARE test cases. Pre/postconditions and invariants add something, but AlphaCodium's 'problem analysis' + 'edge case identification' phase also generates structured problem understanding before coding. The paper needs to sharpen why spec-mediated reasoning is fundamentally different from test-mediated refinement, with controlled experiments isolating this distinction.", "HUMANEVAL SATURATION: HumanEval+ and MBPP+ are listed as primary benchmarks, but frontier models already score 93%+ on HumanEval. Even with EvalPlus's harder tests, the benchmark is near saturation. The paper should emphasize DebugBench, CrossCodeEval, CodeContests, and SWE-bench Verified as primary evaluation, and use HumanEval+/MBPP+ only for comparability with Self-Spec.", "SPEC QUALITY BOOTSTRAPPING RISK: CodeSpecBench shows LLMs achieve only 20.2% on repo-level spec generation. If the LLM generates mostly bad specs, execution grounding catches them—but then the method degrades to 'generate specs → discard most → fall back to direct generation.' The paper needs analysis of what happens when spec generation quality is low (e.g., on CrossCodeEval/RepoBench repo-level tasks), including a failure mode analysis.", "TIMELINE IS VERY AGGRESSIVE: 12–16 days for implementing a 3-stage framework with task-adapted spec schemas, integrating 6 benchmarks (including SWE-bench Docker), running 48+ experiment configurations (6 benchmarks × 2 models × 4 baselines + ablations), AND writing a full paper. SWE-bench Verified Docker setup alone can take 2–3 days. Recommend reducing scope: run full comparison on 3 primary benchmarks (DebugBench, CodeContests, SWE-bench Verified) and use 3 others (HumanEval+/MBPP+, CrossCodeEval/RepoBench) for supplementary evaluation with fewer baselines.", "COST ESTIMATE MISSING API COSTS FOR EG-CFG BASELINE: Reproducing an EG-CFG-style execution-only baseline requires beam search with per-line execution, which is substantially more expensive than standard inference. This is either infeasible within budget or needs to be replaced with a simpler 'execution feedback without specs' baseline."]
Feedback: The revision successfully addresses the critical venue, compute, and scope issues from Round 1. The idea is now properly scoped for EMNLP 2026 with correct benchmarks, models, and budget. However, several issues need resolution:

1. **Sharpen novelty vs. AlphaCodium/CodeT**: These are the most important missing baselines. AlphaCodium (2024) already does training-free, multi-stage, test-based iterative refinement at inference time. ExeSpec must demonstrate that specification-mediated reasoning (structured I/O examples + pre/postconditions + invariants) provides gains BEYOND what test-based refinement alone achieves. Add a controlled experiment: (a) ExeSpec with full specs, (b) AlphaCodium-style test-only refinement, (c) Self-Spec without execution grounding, (d) direct prompting. The delta between (a) and (b) is the paper's core contribution.

2. **De-emphasize saturated benchmarks**: Make DebugBench, CodeContests, and SWE-bench Verified the primary evaluation. Use HumanEval+/MBPP+ for Self-Spec comparability only. Consider adding LiveCodeBench for contamination resistance.

3. **Address spec quality gracefully**: Add a spec quality analysis section showing: (a) what fraction of elicited specs survive execution grounding, (b) how grounding changes spec accuracy, (c) what happens when most specs fail (does the method degrade gracefully?). This directly responds to the CodeSpecBench 20.2% finding and strengthens the paper's analytical contribution.

4. **Simplify the EG-CFG baseline**: Replace the full EG-CFG-style baseline (beam search + per-line execution) with a simpler 'execution feedback without specs' baseline: generate code → execute → feed error messages back → regenerate. This is cheaper and more directly tests the spec contribution.

5. **Reduce timeline risk**: Implement the framework first on HumanEval+/MBPP+ (fast turnaround), validate the approach, then extend to harder benchmarks. Consider submitting to ARR May 25 with 4 benchmarks instead of 6, adding the remaining 2 for the camera-ready.

6. **Cite and discuss**: AlphaCodium (2401.08500), CodeT (ICLR 2022), Self-Debugging (2304.05128), BACE (2603.28653), Revisit Self-Debugging (2501.12793). Position ExeSpec as advancing beyond test-only refinement by introducing verifiable specification reasoning as a structured intermediate representation.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL UNADDRESSED R2 FEEDBACK: AlphaCodium (arXiv 2401.08500, Jan 2024), CodeT (ICLR 2023), Self-Debugging (arXiv 2304.05128, 2023), BACE (arXiv 2603.28653, Mar 2026), and 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025, arXiv 2501.12793) are ALL still missing from key_references and baselines. Round 2 explicitly stated these MUST be cited and compared. AlphaCodium is the most direct conceptual predecessor — a training-free, multi-stage flow with problem reflection, test generation, and iterative execution-based refinement — and must be a baseline, not just a citation.", "NEW MISSING WORK — S* (EMNLP 2025 Findings, arXiv 2502.14382): A training-free test-time scaling framework for code generation that uses execution-based selection with adaptive distinguishing input synthesis. Enables a 3B model to outperform GPT-4o-mini. Published at EMNLP 2025 — the same venue being targeted. This is a highly relevant prior art that directly competes in the 'training-free inference-time code improvement' space.", "NEW MISSING CONCURRENT WORK — SSDE (arXiv 2605.02455, May 2026): 'LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering' uses Gherkin specifications and domain models to guide LLM generation with verification against test suites. Concurrent work that overlaps with ExeSpec's structured specification approach at the repo level.", "THIN NOVELTY BOUNDARY WITH ALPHACODIUM: AlphaCodium's pre-processing phase (problem reflection → public tests reasoning → possible solutions ranking) IS structured problem analysis before code generation. AlphaCodium's iterative phase (generate → execute → fix against public + AI tests) IS execution-grounded refinement. ExeSpec's I/O example specs are functionally identical to AlphaCodium's AI-generated test cases. The actual novelty delta — pre/postconditions, invariants, type constraints in JSON schema — must be isolated via controlled ablation: (a) ExeSpec full specs, (b) I/O-only specs (≈ test-only, AlphaCodium-style), (c) structural specs only (pre/postconditions + invariants without I/O). Without this, reviewers will reject for insufficient novelty.", "UNDERSPECIFIED NON-GENERATION TASKS: The approach for cross-file completion (CrossCodeEval, RepoBench) says 'type-check and partially execute the surrounding context to verify inferred specs.' This is vague. How do you generate behavioral specs for incomplete code in a multi-file context? What executable probes work for partial programs? CodeSpecBench shows only 20.2% success at repo-level spec generation — the method may degrade to fallback (soft grounding) for most repo-level instances, making the execution grounding contribution negligible on these benchmarks.", "HUMANEVAL+ STILL NOT DE-EMPHASIZED: Round 2 explicitly recommended making DebugBench, CodeContests, and SWE-bench Verified primary, with HumanEval+/MBPP+ for Self-Spec comparability only. The idea still lists them alongside other benchmarks without prioritization. Frontier models score 93%+ on HumanEval — gains here are not impressive.", "AGGRESSIVE TIMELINE NOT MITIGATED: Round 2 suggested reducing to 3 primary benchmarks + 3 supplementary. The idea still plans full comparison on all 6 benchmarks within 12–16 days. SWE-bench Docker setup alone takes 2–3 days. Recommend: primary (DebugBench, CodeContests, SWE-bench Verified) with full baselines; supplementary (HumanEval+/MBPP+, CrossCodeEval, RepoBench) with ExeSpec vs. direct prompting only."]
Feedback: This is Round 3, and the idea has improved significantly from Round 1 (correct venue, benchmarks, compute budget) but has failed to address the MOST CRITICAL Round 2 feedback: citing and comparing against AlphaCodium, CodeT, Self-Debugging, BACE, and 'Revisit Self-Debugging.' This is not optional — these are the papers that define the competitive landscape for training-free, execution-based code improvement methods.

Here is exactly what needs to change:

1. **ADD ALPHACODIUM AS PRIMARY BASELINE** (non-negotiable): Replace the 'EG-CFG-style execution-only feedback' baseline with an AlphaCodium-style baseline: problem analysis → AI test generation → iterative code execution/refinement (no structured specs). This directly tests the paper's core claim that specification-mediated reasoning provides gains beyond test-based refinement. The controlled experiment should be: (a) ExeSpec full (specs + execution grounding), (b) AlphaCodium-style (tests + execution feedback, no specs), (c) Self-Spec (specs, no execution grounding), (d) direct prompting. The delta between (a) and (b) is the paper's contribution.

2. **CITE AND POSITION AGAINST S* (EMNLP 2025 Findings)**: S* is the most recent training-free test-time scaling method for code generation, published at your target venue. Position ExeSpec as complementary: S* focuses on parallel/sequential scaling with execution-based selection; ExeSpec focuses on structured intermediate reasoning via verified specs. They could potentially be combined.

3. **SHARPEN THE SPEC VS. TEST DISTINCTION**: The paper must clearly argue why structured behavioral specifications (pre/postconditions, invariants, type constraints) provide fundamentally different reasoning scaffolding compared to test cases. Add a controlled ablation: (a) full specs (I/O + pre/postconditions + invariants), (b) I/O-only specs (≈ test cases), (c) structural specs only (pre/postconditions + invariants, no I/O). If (b) performs similarly to (a), the novelty claim collapses.

4. **SPECIFY THE CROSS-FILE COMPLETION APPROACH**: Describe concretely how ExeSpec generates and validates specs for CrossCodeEval/RepoBench tasks. What does the spec schema look like for incomplete code with cross-file dependencies? What 'lightweight probes' execute for partial programs? If the approach fundamentally differs from function-level generation, say so explicitly.

5. **REDUCE SCOPE TO FIT TIMELINE**: Primary benchmarks with full baselines: DebugBench, CodeContests, SWE-bench Verified. Supplementary with ExeSpec vs. direct prompting only: HumanEval+/MBPP+, CrossCodeEval, RepoBench. This halves the experiment matrix.

6. **ADD TO KEY REFERENCES**: AlphaCodium (2401.08500), CodeT (ICLR 2023, 2207.10397), Self-Debugging (2304.05128), BACE (2603.28653), 'Revisit Self-Debugging' (ACL 2025, 2501.12793), S* (EMNLP 2025 Findings, 2502.14382), SSDE (2605.02455).

### Round 4 review
Verdict: revise
Issues: ["CRITICAL MISSING COMPETITOR: PGS (Property-Generated Solver, arXiv:2506.18315, June 2025, revised May 2026) uses high-level program properties instead of test cases as feedback for LLM code refinement, with execution-based property verification and minimal counterexample generation. It achieves 13.4% pass@1 improvement over TDD methods and 1.4-1.6x higher bug fix rate. This shares ExeSpec's core insight (properties > tests) and must be cited, compared against, and clearly differentiated.", "MISSING RELATED WORK: (1) 'From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing' (FSE 2025) directly challenges test-based paradigm in favor of properties; (2) ContractEval/PACT (arXiv:2510.12047) benchmarks LLM contract satisfaction showing 0% under standard prompting, validating the problem but also raising spec generation quality concerns; (3) 'Preconditions and Postconditions as Design Constraints for LLM Code Generation' (IEEE Access 2024/2025) directly studies ExeSpec's premise with controlled experiments; (4) StoryCoder (arXiv:2604.14631, ACL 2026) is another training-free structured intermediate reasoning method achieving 18.7% improvement.", "SWE-BENCH VERIFIED CONTAMINATION: The benchmark is now severely contaminated — top score is 93.9% (Claude Mythos), while the same models score only ~46% on SWE-bench Pro. OpenAI has stopped reporting Verified scores. The paper acknowledges contamination but should more seriously consider using SWE-bench Pro as the primary evaluation or running both and comparing. Reporting only Verified results risks reviewer skepticism.", "MODEL CURRENCY: Qwen3-Coder has been released since the idea was designed. EMNLP reviewers may question why the paper uses Qwen2.5-Coder-7B/32B rather than the latest version. Either justify the choice (reproducibility, available at experiment time) or update.", "SPEC GENERATION QUALITY RISK INSUFFICIENTLY ADDRESSED: ContractEval shows 0% contract satisfaction under standard prompting and only 23-41% with explicit contracts. CodeSpecBench shows 20.2% repo-level success. The paper's execution grounding is meant to catch bad specs, but if >60% of specs fail grounding, the method effectively degrades to 'generate specs → discard most → fall back to whatever survives' — potentially no better than test-only methods with fewer but higher-quality tests. The paper should include analysis of spec survival rates and graceful degradation behavior.", "TIMELINE MARGINAL: The manual estimate of 14-18 days with 2 researchers overlaps but can exceed the 16-day deadline. The upper bound should be trimmed to fit. Consider dropping one supplementary benchmark (e.g., RepoBench) to ensure the primary benchmarks are completed thoroughly."]
Feedback: This is now a well-structured idea that has improved substantially through four rounds. The controlled experimental design with honest ablations is the strongest aspect. However, one critical competitor was discovered that must be addressed before this can pass:

1. **CITE AND DIFFERENTIATE FROM PGS** (most important): PGS (arXiv:2506.18315) shares ExeSpec's core insight that properties outperform tests as LLM code feedback. Differentiate on: (a) ExeSpec execution-grounds the specs themselves (catches hallucinated specs before use), while PGS assumes properties are correct; (b) ExeSpec applies across 4 task types (generation, debugging, completion, issue resolution), PGS focuses on generation/repair; (c) ExeSpec's comprehensive spec schema (5 component types) vs. PGS's single-property checking; (d) ExeSpec's controlled ablation isolates each spec component's contribution. Add PGS as a fifth baseline condition, or at minimum cite and discuss in Related Work with clear differentiation.

2. **CITE FSE 2025 AND ContractEval**: 'From Prompts to Properties' (FSE 2025) validates the property-vs-test framing from a PBT perspective. ContractEval (arXiv:2510.12047) both validates your problem (LLMs fail at contracts) and raises spec quality concerns — use it to motivate your execution grounding stage.

3. **ADDRESS SWE-BENCH CONTAMINATION SERIOUSLY**: Either (a) add SWE-bench Pro as the primary SE benchmark alongside Verified, or (b) follow the paper's current plan but add a contamination analysis section comparing performance on instances with/without known gold patch exposure. Option (a) is safer but adds implementation effort.

4. **ADD SPEC SURVIVAL RATE ANALYSIS**: Report what fraction of generated specs survive execution grounding by task type and model. If survival is low, analyze whether the surviving specs still provide gains over test-only methods. This directly addresses the CodeSpecBench/ContractEval concern and strengthens the paper's analytical contribution.

5. **JUSTIFY MODEL CHOICE**: Add a sentence noting that Qwen2.5-Coder was selected as the strongest open-source code model available at experiment design time, and that the method is model-agnostic. If time permits, add one data point with a newer model.

These are all fixable in one more revision round. The idea's core structure, experimental design, and positioning are sound — the main gap is incomplete coverage of the competitive landscape.

### Round 5 review
Verdict: revise
Issues: ["CRITICAL — PGS STILL NOT CITED (Round 4 issue unresolved): PGS (arXiv:2506.18315, 'Use Property-Based Testing to Bridge LLM Code Generation and Validation', June 2025, revised May 2026) shares ExeSpec's core contribution: using program properties instead of test cases for LLM code refinement at inference time. PGS achieves 97.6% HumanEval, 87.2% MBPP, 76.5% LiveCodeBench, 49.7% CodeContests, 37.3% SWE-bench Verified using DeepSeek-R1-32B. It reports 23.1-37.3% relative pass@1 gains over TDD methods and 1.4-1.6x higher bug fix rates. This paper validates ExeSpec's hypothesis but also substantially reduces its novelty. Without citing and differentiating from PGS, any informed reviewer will reject on novelty grounds.", "ROUND 4 ISSUES LARGELY UNADDRESSED: (1) ContractEval/PACT (arXiv:2510.12047) — shows 0% contract satisfaction under standard prompting, motivates execution grounding but raises spec quality concerns — not cited; (2) 'From Prompts to Properties' (FSE 2025 LLanMER) — validates property-vs-test framing — not cited; (3) 'Preconditions and Postconditions as Design Constraints' (IEEE Access 2025) — directly studies ExeSpec's premise with controlled experiments — not cited; (4) StoryCoder (arXiv:2604.14631) — concurrent training-free structured intermediate reasoning — not cited.", "SWE-BENCH VERIFIED CONTAMINATION INSUFFICIENTLY ADDRESSED: OpenAI has officially stopped reporting SWE-bench Verified scores (blog post: 'Why SWE-bench Verified no longer measures frontier coding capabilities'). Top score is 93.9% vs. ~46% on SWE-bench Pro. The idea mentions 'noting contamination concerns per OpenAI's 2026 audit' but still uses Verified as a primary benchmark without proposing SWE-bench Pro as an alternative or replacement. EMNLP reviewers aware of the contamination will question evaluation credibility.", "MODEL CURRENCY: Qwen3-Coder-Next (3B/80B MoE, 256k context, >70% SWE-bench Verified) and DeepSeek V4 have been released. Using Qwen2.5-Coder without justification looks dated. Either justify the choice (available at experiment design time, reproducibility) or add a data point with a newer model.", "NOVELTY BOUNDARY WITH PGS IS THIN: PGS uses LLM-generated abstract properties with execution-based validation and minimal counterexample feedback. ExeSpec uses LLM-generated behavioral specifications (pre/postconditions, invariants, type constraints) with execution grounding and structured violation reports. Both are training-free, inference-time, property-level-rather-than-test-level approaches. The genuine differentiators — (a) execution grounding of specs themselves (PGS assumes properties are ~87% accurate), (b) structured 5-component schema with component ablation, (c) multi-task applicability beyond generation — must be explicitly argued. Without this, the paper reads as a PGS variant with a different spec format.", "MISSING NL-DEBUGGING (EMNLP 2025 Oral): 'Natural Language as Intermediate Representation for Code Debugging' (arXiv:2505.15356) was accepted as an Oral at EMNLP 2025 — the same venue being targeted. It uses NL (not specifications) as an intermediate representation for debugging and shows consistent gains over code-level debugging. This is a strong baseline for the debugging task (DebugBench) and establishes the 'intermediate representation for code tasks' paradigm at this exact venue."]
Feedback: The idea has matured substantially over 5 rounds — the experimental design with honest ablations, primary/supplementary benchmark distinction, and AlphaCodium baseline are all strong. However, the most critical Round 4 issue (PGS) remains unaddressed, and this is now blocking passage. Here is exactly what needs to change:

1. **CITE AND DIFFERENTIATE FROM PGS** (highest priority, non-negotiable): Add PGS to key_references and landscape. Position ExeSpec's contributions BEYOND PGS's established result (properties > tests): (a) ExeSpec execution-grounds the specs themselves — PGS's verification asymmetry (87% property accuracy) means ~13% of properties are wrong, and PGS has no mechanism to catch them before use; ExeSpec's Stage 2 catches hallucinated specs via execution probes; (b) ExeSpec evaluates across 4 task types (generation, debugging, completion, issue resolution) while PGS evaluates generation and repair; (c) ExeSpec's 5-component schema with component ablation provides fine-grained analysis of which spec types help which tasks — PGS treats properties as a monolithic category. Consider adding PGS as a 5th baseline condition on at least CodeContests and DebugBench, or at minimum cite and discuss with clear differentiation.

2. **ADDRESS SWE-BENCH CONTAMINATION**: Either (a) replace SWE-bench Verified with SWE-bench Pro as primary (preferred — aligns with community trend), or (b) keep Verified but add contamination analysis comparing performance on high-contamination vs. low-contamination instances (requires the contamination labels from OpenAI's audit). Option (a) adds implementation effort but makes the paper future-proof.

3. **CITE ADDITIONAL MISSING WORK**: Add to key_references and discuss in landscape: ContractEval/PACT (2510.12047), NL-Debugging (2505.15356, EMNLP 2025 Oral — important as it's at the same venue), 'From Prompts to Properties' (FSE 2025). These validate ExeSpec's problem framing and provide important context.

4. **JUSTIFY OR UPDATE MODEL CHOICE**: Add one sentence: 'We use Qwen2.5-Coder as the strongest open-source code model with publicly available weights at experiment design time; the method is model-agnostic and we expect consistent gains across model generations.' If feasible within budget, add one supplementary data point with Qwen3-Coder-Next-3B to demonstrate model-agnostic applicability.

5. **SHARPEN THE NARRATIVE**: After citing PGS, reframe ExeSpec's contribution as: 'PGS demonstrated that property-level feedback outperforms test-based feedback for code generation. We advance this finding in three ways: (1) we show that execution-grounded specification verification catches ~X% of hallucinated specs that would corrupt reasoning, (2) we extend property-level reasoning beyond generation to debugging, completion, and issue resolution, and (3) we decompose the contribution of different spec components (I/O, preconditions, postconditions, invariants, type constraints) across task types, providing actionable guidance for spec-mediated code reasoning.'

These changes are all feasible in one revision round. The idea's core structure is sound — it just needs to acknowledge and position against the competitive landscape that has emerged.

### Round 6 review
Verdict: revise
Issues: ["CRITICAL — PGS STILL NOT CITED (4th consecutive round): PGS (arXiv:2506.18315, 'Use Property-Based Testing to Bridge LLM Code Generation and Validation', June 2025, revised May 2026) shares ExeSpec's core contribution: using LLM-generated properties (not tests) for code refinement with execution-based validation. PGS validates properties via soundness checks against public tests + sensitivity to known errors, then provides minimal counterexample feedback. It evaluates on HumanEval (97.6%), MBPP (81.2%), and LiveCodeBench (74.5%) with DeepSeek-R1-Distilled-32B. Note: PGS does NOT evaluate on CodeContests or SWE-bench (the Round 5 reviewer's numbers for those benchmarks were incorrect). ExeSpec's genuine differentiators vs. PGS: (1) execution-grounds specs themselves before use via probes, catching hallucinated specs; (2) covers 4 task types vs. PGS's generation-only scope; (3) structured 5-component schema with component ablation vs. PGS's monolithic property checking; (4) structured violation reports vs. minimal counterexamples. These are meaningful but incremental. This is the 4th consecutive round raising this issue — if unaddressed in the next round, this should be grounds for failure.", "NL-DEBUGGING STILL NOT CITED (EMNLP 2025 ORAL): NL-Debugging (arXiv:2505.15356, ACL Anthology 2025.emnlp-main.80) uses natural language as an intermediate representation for debugging, demonstrating gains over code-level debugging. Published as an ORAL at EMNLP 2025 — the exact target venue. This establishes the 'intermediate representation for code tasks' paradigm at this venue and is a critical baseline for DebugBench evaluation. Reviewers at EMNLP 2026 will know this paper.", "CONTRACTEVAL STILL NOT CITED: ContractEval (arXiv:2510.12047) shows 0% contract satisfaction under standard prompting, 23-41% with explicit contracts, 49-53% with contract-violating test examples. This validates ExeSpec's motivation (LLMs need grounding for spec generation) but also quantifies the spec quality challenge. Must be cited to strengthen the execution grounding motivation.", "SWE-BENCH VERIFIED CONTAMINATION INSUFFICIENTLY ADDRESSED: OpenAI has officially stopped reporting SWE-bench Verified scores. All frontier models show training data contamination — models can reproduce exact gold patches verbatim. Claude Opus 4.5 scores 80.9% on Verified but only 45.9% on Pro. While Qwen2.5-Coder (sub-frontier) may be less contaminated, the benchmark's credibility is severely damaged. The paper's approach of 'noting contamination concerns per OpenAI's 2026 audit' and 'reporting held-out test pass rates alongside standard metrics' is insufficient. Either: (a) add SWE-bench Pro as a co-primary benchmark, (b) demonstrate Qwen2.5-Coder-7B/32B are not contaminated on Verified via gold-patch reproduction tests, or (c) at minimum acknowledge that the community has moved to Pro and explain why Verified remains informative for sub-frontier models.", "MODEL CURRENCY UNJUSTIFIED: Qwen3-Coder-Next (3B active / 80B total MoE, 256k context, >70% SWE-bench Verified) has been released. Qwen2.5-Coder remains a valid reproducibility choice, but the paper needs one sentence justifying it (e.g., 'strongest open-source code model with dense architecture available at experiment design time; the method is model-agnostic'). Without justification, EMNLP reviewers may question currency.", "'FROM PROMPTS TO PROPERTIES' (FSE 2025/LLanMER) STILL NOT CITED: This paper applied property-based testing to evaluate StarCoder and CodeLlama on MBPP/HumanEval, finding 30-32% of generated solutions only partially adhere to correctness properties and 18-23% fail outright. Validates ExeSpec's property-vs-test framing from the evaluation side."]
Feedback: This is Round 6, and the idea's experimental design, controlled baselines, and honest ablation commitment are genuinely strong. However, the repeated failure to cite PGS — now raised for the 4th consecutive round as non-negotiable — is becoming a disqualifying pattern. Here is exactly what must change:

1. **CITE AND DIFFERENTIATE FROM PGS** (FINAL WARNING — if unaddressed in Round 7, this warrants failure): Add PGS to key_references and landscape. Note that PGS evaluates ONLY on HumanEval/MBPP/LiveCodeBench and does NOT evaluate on CodeContests, SWE-bench, or DebugBench — this is actually ExeSpec's opportunity. Position ExeSpec's contributions BEYOND PGS: (a) ExeSpec execution-grounds specs before use (probes catch hallucinated specs); PGS validates properties against public tests but doesn't catch internally inconsistent properties before use. (b) ExeSpec evaluates across 4 task types including debugging and issue resolution — PGS only covers generation. (c) ExeSpec's 5-component ablation decomposes which spec types help which tasks — PGS treats properties as monolithic. (d) ExeSpec directly compares against AlphaCodium on CodeContests (PGS's home turf overlap — neither AlphaCodium nor PGS compares against each other). Reframe the narrative: 'PGS demonstrated that property-level feedback outperforms test-based feedback for code generation. We advance this finding by: (1) showing execution-grounded spec verification catches hallucinated specs that corrupt reasoning, (2) extending property-level reasoning to debugging, completion, and issue resolution, (3) providing fine-grained ablation of which specification components help which task types.'

2. **CITE NL-DEBUGGING AS DEBUGGING BASELINE**: Add NL-Debugging (2505.15356, EMNLP 2025 Oral) to key_references. Position ExeSpec's debugging approach as advancing beyond NL-level debugging by providing structured, execution-verified behavioral constraints (not just NL descriptions). If feasible, add NL-Debugging as a 5th baseline condition on DebugBench — this would strongly differentiate ExeSpec.

3. **ADDRESS SWE-BENCH CONTAMINATION CONCRETELY**: Add one of: (a) 'We additionally evaluate on SWE-bench Pro on a representative subset to validate that gains generalize beyond Verified'; (b) 'We verify Qwen2.5-Coder models are not contaminated by testing gold-patch reproduction rates'; (c) 'We acknowledge SWE-bench Verified's contamination concerns are most severe for frontier models; Qwen2.5-Coder-7B/32B are sub-frontier models unlikely to have been trained on the SWE-bench gold patches.' Option (c) is the minimum acceptable response.

4. **CITE CONTRACTEVAL AND 'FROM PROMPTS TO PROPERTIES'**: ContractEval (2510.12047) motivates execution grounding (0% contract satisfaction without it). 'From Prompts to Properties' (FSE 2025) validates the property-vs-test evaluation framing. Both strengthen ExeSpec's problem statement.

5. **ADD MODEL JUSTIFICATION**: One sentence: 'We use Qwen2.5-Coder-7B/32B-Instruct as well-established dense models with strong code performance and reproducible inference via vLLM; the method is model-agnostic and we expect consistent gains across model generations.' If time/budget permit, add one supplementary data point with a Qwen3 model.

The core idea is sound and the experimental design is rigorous. But an EMNLP reviewer who has read PGS (published June 2025, revised May 2026 — highly visible) will immediately recognize the overlap and reject if PGS is not acknowledged. This is the most critical fix.

### Round 7 review
Verdict: revise
Issues: ["CRITICAL — PGS STILL NOT CITED (5TH CONSECUTIVE ROUND): PGS (arXiv:2506.18315, 'Use Property-Based Testing to Bridge LLM Code Generation and Validation', June 2025, revised as 'Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback', May 2026) shares ExeSpec's core contribution: using LLM-generated abstract properties instead of test cases for code refinement with execution-based validation at inference time, training-free. PGS evaluates on HumanEval, MBPP, and LiveCodeBench ONLY (NOT CodeContests or SWE-bench — earlier reviewer claims about PGS's CodeContests/SWE-bench numbers were incorrect). PGS achieves 23.1-37.3% relative pass@1 improvement over TDD methods using DeepSeek-R1-Distilled-32B. This has been raised in Rounds 4, 5, 6, and 7 — all unaddressed. If unaddressed in Round 8, this MUST result in failure. No exceptions.", "NL-DEBUGGING STILL NOT CITED (3RD ROUND): NL-Debugging (arXiv:2505.15356, ACL Anthology 2025.emnlp-main.80) was accepted as an ORAL at EMNLP 2025 — the exact target venue. It uses natural language as an intermediate representation for debugging via backtranslation → NL refinement → regeneration, achieving substantial gains on APPS and Codeforces. EMNLP 2026 reviewers WILL know this paper. It establishes the 'structured intermediate representation for code tasks' paradigm at this venue and is a critical baseline for DebugBench evaluation.", "CONTRACTEVAL STILL NOT CITED (3RD ROUND): ContractEval (arXiv:2510.12047) shows 0% contract satisfaction under standard prompting, 23-41% with explicit contracts, 49-53% with example-augmented specification. This simultaneously validates ExeSpec's motivation (LLMs need grounding for contract/spec generation) AND quantifies the spec quality challenge. Must be cited to strengthen execution grounding motivation.", "ALPHACODIUM 44% CLAIM IS MISLEADING: The idea states 'AlphaCodium's flow engineering raises CodeContests pass@5 from 19% to 44%.' This is the VALIDATION SET result (117 problems). On the TEST SET (165 problems), AlphaCodium achieves 29% pass@5 (up from 12% baseline). The distinction must be clarified to avoid misleading readers.", "SWE-BENCH VERIFIED CONTAMINATION REMAINS INADEQUATELY ADDRESSED: OpenAI officially stopped reporting Verified scores in February 2026 after finding frontier models could reproduce verbatim gold patches. The current response ('noting contamination concerns, we report held-out test pass rates alongside standard metrics') is insufficient. Minimum acceptable: explicitly argue that Qwen2.5-Coder-7B/32B are sub-frontier models unlikely to exhibit the same contamination patterns as GPT-5.2/Claude Opus 4.5, and note that the community has moved to SWE-bench Pro. Better: add SWE-bench Pro as a co-primary benchmark.", "MODEL CURRENCY UNJUSTIFIED: Qwen3-Coder-Next (3B active/80B total MoE, 256k context, >70% SWE-bench Verified) was released February 2026. Using Qwen2.5-Coder without a justification sentence will invite reviewer questions. Add: 'We use Qwen2.5-Coder-7B/32B-Instruct as established dense models with reproducible vLLM inference; the method is model-agnostic.'", "MISSING ADDITIONAL RELEVANT WORK: (1) StoryCoder (arXiv:2604.14631, ACL 2026 Main) — training-free structured intermediate reasoning via narrative reformulation, +18.7% pass@10 across 11 models. Concurrent work using structured intermediate representations for code. (2) FixAudit (arXiv:2604.05560, April 2026) — jointly trains fixer and auditor, 35-37% improvement on CodeContests. (3) 'From Prompts to Properties' (FSE Companion 2025/LLanMER) — applies PBT to evaluate LLM code, finding 30-32% partial failures that pass@k misses. These should be cited in landscape or related work."]
Feedback: This is Round 7, and the idea's experimental design, controlled baselines, and honest ablation commitment are the strongest aspects of the proposal. However, the repeated failure to cite PGS — now flagged for the 5TH CONSECUTIVE ROUND — is approaching disqualification territory. Here is exactly what must change:

1. **CITE AND DIFFERENTIATE FROM PGS** (ABSOLUTE FINAL CHANCE — failure to address in Round 8 means automatic fail): Add PGS (arXiv:2506.18315) to key_references and landscape. Critically, note that PGS evaluates ONLY on HumanEval/MBPP/LiveCodeBench and does NOT evaluate on CodeContests, SWE-bench, or DebugBench. ExeSpec's differentiators vs. PGS: (a) ExeSpec execution-grounds specs BEFORE use via probes, catching hallucinated/contradictory specs — PGS validates properties against public tests but assumes ~87% property accuracy without catching internally inconsistent properties; (b) ExeSpec evaluates across 4 task types (generation, debugging, completion, issue resolution) — PGS covers generation/repair only; (c) ExeSpec's 5-component schema with component ablation decomposes which spec types help which tasks — PGS treats properties as a monolithic category; (d) ExeSpec directly compares against AlphaCodium on CodeContests, a benchmark neither PGS nor AlphaCodium compares against each other on. Reframe narrative: 'PGS demonstrated that property-level feedback outperforms test-based feedback for code generation. We advance this by: (1) execution-grounding specs to catch hallucinated properties, (2) extending to debugging/completion/issue-resolution, (3) decomposing spec component contributions via controlled ablation.'

2. **CITE NL-DEBUGGING** (EMNLP 2025 Oral — reviewers at your target venue will know this): Add NL-Debugging (2505.15356) to key_references and landscape. Position ExeSpec's debugging as advancing beyond NL-level intermediate reasoning by providing structured, execution-verified behavioral constraints. Consider adding NL-Debugging as a 5th baseline condition on DebugBench for a strong venue-specific comparison.

3. **CITE CONTRACTEVAL**: Add ContractEval (2510.12047) to motivate execution grounding: '0% contract satisfaction under standard prompting validates the need for execution-based spec verification.'

4. **FIX ALPHACODIUM 44% CLAIM**: Clarify as 'AlphaCodium raises CodeContests validation-set pass@5 from 19% to 44% (test-set: 12% to 29%)' or simply cite the test-set numbers.

5. **ADDRESS SWE-BENCH CONTAMINATION**: Add one paragraph: 'We use Qwen2.5-Coder-7B/32B, sub-frontier models unlikely to exhibit the verbatim gold-patch reproduction observed in frontier models (GPT-5.2, Claude Opus 4.5). We additionally note that the community has moved toward SWE-bench Pro for frontier evaluation; our results on sub-frontier models provide a contamination-resistant baseline.'

6. **ADD MODEL JUSTIFICATION**: One sentence: 'We use Qwen2.5-Coder as established dense models with strong code performance and reproducible vLLM inference; the method is model-agnostic.'

The core structure is sound. Fix the competitive landscape and this can pass.


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
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "9261ef51-358c-406d-ade0-77adaa70d4a4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T02:12:09.864Z_

```json
{
  "parentUuid": "9261ef51-358c-406d-ade0-77adaa70d4a4",
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
  "uuid": "9dd22144-f3bd-4c9a-8ec3-366d2acbd4a4",
  "timestamp": "2026-05-12T02:12:09.864Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T02:12:09.864Z_

```json
{
  "parentUuid": "9dd22144-f3bd-4c9a-8ec3-366d2acbd4a4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ec8b9956-f72d-4e3c-b880-75c44abd8c2a",
  "timestamp": "2026-05-12T02:12:09.864Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
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
  "leafUuid": "ec8b9956-f72d-4e3c-b880-75c44abd8c2a",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "ExeSpec: Execution-grounded Behavioral Specifications for Code LLMs",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Assistant

_source line 8 · 2026-05-12T02:12:33.307Z_

<details><summary>Logged reasoning block</summary>

```text
This is Round 8 of 10 for reviewing the ExeSpec idea. Let me carefully analyze what's happened across the previous 7 rounds and what the current state of the idea is.

**Key history:**
- Rounds 1-3: Major structural issues (wrong venue, compute violations, missing baselines) gradually fixed
- Rounds 4-7: The SAME critical issue has been raised repeatedly — PGS (arXiv:2506.18315) is not cited. This has been flagged as non-negotiable for 5 consecutive rounds.


- Round 7 explicitly stated: "failure to address in Round 8 means automatic fail"

**Now in Round 8:** Let me check — has PGS been addressed in this revision? Looking at the current submission, PGS is now cited in the key references and discussed in the landscape section, which means the critical blocker from the previous rounds has finally been resolved.

I'm also verifying the other required citations. NL-Debugging is there in the references and landscape. ContractEval is included as well. Let me continue checking the remaining items...

The AlphaCodium numbers check out—the idea correctly cites both the validation-set improvement (19% to 44%) and the test-set results (12% to 29%). For the SWE-bench contamination concern, the idea addresses this by switching to SWE-bench Pro as a co-primary benchmark and explaining why frontier models can no longer be reliably evaluated on the original Verified set. The approach also uses sub-frontier models to ensure fair comparison. On model currency, the method is positioned as model-agnostic...

Actually, looking at the next part—the idea explains that gains should transfer to newer architectures like MoE models, and using established models allows direct comparison with prior work on the same family. All the major references I flagged earlier are now properly cited: StoryCoder, FixAudit, 'From Prompts to Properties', SSDE, and CodeSpecBench. This revision has addressed every significant issue from previous rounds. Now I want to independently verify the current state-of-the-art numbers on these benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec8b9956-f72d-4e3c-b880-75c44abd8c2a",
  "isSidechain": false,
  "requestId": "req_011Caws6f4uNeB6vSoP5XNow",
  "type": "assistant",
  "uuid": "500cb412-2a74-488e-b8a7-6d123fa3b0a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175ZjBh6vBHThwyf9vqTnRE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29467,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1098,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29467,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1098,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 29467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29467
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

_source line 9 · 2026-05-12T02:12:33.642Z_

I'll conduct an independent review of this Round 8 submission. First, let me verify whether the repeatedly flagged issues have finally been addressed, then check for any new concerns.

Let me start by checking the current competitive landscape and verifying the key claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "500cb412-2a74-488e-b8a7-6d123fa3b0a3",
  "isSidechain": false,
  "requestId": "req_011Caws6f4uNeB6vSoP5XNow",
  "type": "assistant",
  "uuid": "04e4c862-76cd-41b7-9df1-232347ab76df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175ZjBh6vBHThwyf9vqTnRE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29467,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1098,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29467,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1098,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 29467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29467
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

_source line 10 · 2026-05-12T02:12:33.951Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019mFHEK4bThfF8CRRxyonef`</summary>

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
  "parentUuid": "04e4c862-76cd-41b7-9df1-232347ab76df",
  "isSidechain": false,
  "requestId": "req_011Caws6f4uNeB6vSoP5XNow",
  "type": "assistant",
  "uuid": "467d4531-8eb8-45f5-90b6-ce0a6a10f7b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175ZjBh6vBHThwyf9vqTnRE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29467,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1098,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29467,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1098,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 29467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29467
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

_source line 11 · 2026-05-12T02:12:33.958Z_

<details><summary>↩ Tool result · `toolu_019mFHEK4bThfF8CRRxyonef`</summary>

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
  "parentUuid": "467d4531-8eb8-45f5-90b6-ce0a6a10f7b7",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "0542d3ea-2845-45c3-9784-951896f2a13e",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "467d4531-8eb8-45f5-90b6-ce0a6a10f7b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-12T02:12:36.718Z_

Now let me conduct thorough independent verification. I'll start with multiple parallel searches to check the key claims and find any missing competitors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0542d3ea-2845-45c3-9784-951896f2a13e",
  "isSidechain": false,
  "requestId": "req_011Caws8SNUhMRXcT5L5sv6A",
  "type": "assistant",
  "uuid": "b30657cd-0018-42c6-a91e-25657ccc2430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CgpnbojtyrgxtCBux4JmwW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2117,
      "cache_read_input_tokens": 41308,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2117,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 41308,
          "cache_creation_input_tokens": 2117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2117
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

_source line 13 · 2026-05-12T02:12:37.376Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RnQEbaXFk4A7fj5F1wTkvu`</summary>

```json
{
  "query": "PGS property-based testing LLM code refinement arXiv 2506.18315 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b30657cd-0018-42c6-a91e-25657ccc2430",
  "isSidechain": false,
  "requestId": "req_011Caws8SNUhMRXcT5L5sv6A",
  "type": "assistant",
  "uuid": "44f697c5-b6be-4ef1-be97-712eea07f3bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CgpnbojtyrgxtCBux4JmwW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2117,
      "cache_read_input_tokens": 41308,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2117,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 108,
          "cache_read_input_tokens": 41308,
          "cache_creation_input_tokens": 2117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2117
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

_source line 14 · 2026-05-12T02:12:46.298Z_

<details><summary>↩ Tool result · `toolu_01RnQEbaXFk4A7fj5F1wTkvu`</summary>

```text
Web search results for query: "PGS property-based testing LLM code refinement arXiv 2506.18315 2025 2026"

Links: [{"title":"[2506.18315] Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/abs/2506.18315"},{"title":"Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/html/2506.18315v1"},{"title":"Paper page - Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://huggingface.co/papers/2506.18315"},{"title":"Use Property-Based Testing to Bridge LLM Code Generation and Validation | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.18315v1"},{"title":"[Literature Review] Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://www.themoonlight.io/en/review/use-property-based-testing-to-bridge-llm-code-generation-and-validation"},{"title":"Enhanced LLM code generation with property-based testing! New Framework PGS to Break Self-Deception | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/llm-paper/property-generated-solver"},{"title":"Understanding the Characteristics of LLM-Generated Property-Based Tests in Exploring Edge Cases","url":"https://arxiv.org/html/2510.25297v1"},{"title":"From Exploration to Specification: LLM-Based Property Generation for Mobile App Testing","url":"https://arxiv.org/html/2604.13463"},{"title":"(PDF) Understanding the Characteristics of LLM-Generated Property-Based Tests in Exploring Edge Cases","url":"https://www.researchgate.net/publication/397040980_Understanding_the_Characteristics_of_LLM-Generated_Property-Based_Tests_in_Exploring_Edge_Cases"},{"title":"Can Large Language Models Write Good Property-Based Tests? Vasudev Vikram","url":"https://arxiv.org/pdf/2307.04346"}]

I found detailed information about the arXiv paper 2506.18315. Here's what I discovered:

## Paper Overview

The paper introduces Property-Generated Solver, a novel framework that leverages Property-Based Testing (PBT) to validate high-level program properties or invariants, instead of relying on specific input-output examples.

## Key Problem Being Addressed

Large Language Models (LLMs) excel at code generation, but ensuring their outputs to be functionally correct, especially in complex programming tasks, is a persistent challenge. While traditional Test-Driven Development (TDD) offers a path for code refinement, its efficacy with LLMs is often undermined by the scarcity of high-quality test cases or the pitfalls of automated test generation, including biased tests or inaccurate output predictions that can misdirect the correction process.

## The PGS Framework

Property-Generated Solver employs two collaborative LLM-based agents: a Generator dedicated to code generation and iterative refinement, and a Tester that manages the PBT life-cycle and formulate semantically rich feedback from property violations.

After the Generator produces initial candidate programs, these agents collaborate iteratively: the Tester rigorously validates them using defined properties, while the Generator refines the programs based on the feedback from validation results.

## Results

Extensive experimental results on multiple code generation benchmarks demonstrate that Property-Generated Solver achieves substantial pass@1 improvements, ranging from 23.1% to 37.3% relative gains over established TDD methods.

The paper was submitted on 23 Jun 2025 to arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44f697c5-b6be-4ef1-be97-712eea07f3bb",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "01574d82-93ed-4703-ab43-3ea6b9a02ea3",
  "toolUseResult": {
    "query": "PGS property-based testing LLM code refinement arXiv 2506.18315 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SW1LA3GkLFWTXHLeWDZkrY",
        "content": [
          {
            "title": "[2506.18315] Use Property-Based Testing to Bridge LLM Code Generation and Validation",
            "url": "https://arxiv.org/abs/2506.18315"
          },
          {
            "title": "Use Property-Based Testing to Bridge LLM Code Generation and Validation",
            "url": "https://arxiv.org/html/2506.18315v1"
          },
          {
            "title": "Paper page - Use Property-Based Testing to Bridge LLM Code Generation and Validation",
            "url": "https://huggingface.co/papers/2506.18315"
          },
          {
            "title": "Use Property-Based Testing to Bridge LLM Code Generation and Validation | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2506.18315v1"
          },
          {
            "title": "[Literature Review] Use Property-Based Testing to Bridge LLM Code Generation and Validation",
            "url": "https://www.themoonlight.io/en/review/use-property-based-testing-to-bridge-llm-code-generation-and-validation"
          },
          {
            "title": "Enhanced LLM code generation with property-based testing! New Framework PGS to Break Self-Deception | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media",
            "url": "https://ai-scholar.tech/en/articles/llm-paper/property-generated-solver"
          },
          {
            "title": "Understanding the Characteristics of LLM-Generated Property-Based Tests in Exploring Edge Cases",
            "url": "https://arxiv.org/html/2510.25297v1"
          },
          {
            "title": "From Exploration to Specification: LLM-Based Property Generation for Mobile App Testing",
            "url": "https://arxiv.org/html/2604.13463"
          },
          {
            "title": "(PDF) Understanding the Characteristics of LLM-Generated Property-Based Tests in Exploring Edge Cases",
            "url": "https://www.researchgate.net/publication/397040980_Understanding_the_Characteristics_of_LLM-Generated_Property-Based_Tests_in_Exploring_Edge_Cases"
          },
          {
            "title": "Can Large Language Models Write Good Property-Based Tests? Vasudev Vikram",
            "url": "https://arxiv.org/pdf/2307.04346"
          }
        ]
      },
      "I found detailed information about the arXiv paper 2506.18315. Here's what I discovered:\n\n## Paper Overview\n\nThe paper introduces Property-Generated Solver, a novel framework that leverages Property-Based Testing (PBT) to validate high-level program properties or invariants, instead of relying on specific input-output examples.\n\n## Key Problem Being Addressed\n\nLarge Language Models (LLMs) excel at code generation, but ensuring their outputs to be functionally correct, especially in complex programming tasks, is a persistent challenge. While traditional Test-Driven Development (TDD) offers a path for code refinement, its efficacy with LLMs is often undermined by the scarcity of high-quality test cases or the pitfalls of automated test generation, including biased tests or inaccurate output predictions that can misdirect the correction process.\n\n## The PGS Framework\n\nProperty-Generated Solver employs two collaborative LLM-based agents: a Generator dedicated to code generation and iterative refinement, and a Tester that manages the PBT life-cycle and formulate semantically rich feedback from property violations.\n\nAfter the Generator produces initial candidate programs, these agents collaborate iteratively: the Tester rigorously validates them using defined properties, while the Generator refines the programs based on the feedback from validation results.\n\n## Results\n\nExtensive experimental results on multiple code generation benchmarks demonstrate that Property-Generated Solver achieves substantial pass@1 improvements, ranging from 23.1% to 37.3% relative gains over established TDD methods.\n\nThe paper was submitted on 23 Jun 2025 to arXiv."
    ],
    "durationSeconds": 8.917303001
  },
  "sourceToolAssistantUUID": "44f697c5-b6be-4ef1-be97-712eea07f3bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-12T02:12:48.901Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012CGj1wuis7UfkvGmcLgAeW`</summary>

```json
{
  "query": "NL-Debugging natural language intermediate representation code debugging EMNLP 2025 arXiv 2505.15356"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01574d82-93ed-4703-ab43-3ea6b9a02ea3",
  "isSidechain": false,
  "requestId": "req_011Caws9LbEkmQoe9ynDWQ1L",
  "type": "assistant",
  "uuid": "0ed2a6f4-dfb6-4a89-a4c5-10a3610ee181",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B7eFXk439p9RY7aia7P9md",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1040,
      "cache_read_input_tokens": 43425,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 43425,
          "cache_creation_input_tokens": 1040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1040
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

_source line 16 · 2026-05-12T02:12:55.518Z_

<details><summary>↩ Tool result · `toolu_012CGj1wuis7UfkvGmcLgAeW`</summary>

```text
Web search results for query: "NL-Debugging natural language intermediate representation code debugging EMNLP 2025 arXiv 2505.15356"

Links: [{"title":"NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.80/"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"[2505.15356] NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging","url":"https://arxiv.org/abs/2505.15356"},{"title":"NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging","url":"https://arxiv.org/html/2505.15356"},{"title":"Weiming Zhang - Homepage","url":"https://wmzhang02.github.io/"},{"title":"NL-Debugging: Exploiting Natural Language as an ...","url":"https://aclanthology.org/2025.emnlp-main.80.pdf"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Code Execution as Grounded Supervision for LLM ...","url":"https://aclanthology.org/2025.emnlp-main.1260.pdf"},{"title":"EMNLP 2025 The 2025 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2025.emnlp-tutorials.pdf"},{"title":"dblp: EMNLP","url":"https://dblp.org/db/conf/emnlp/index.html"}]

I found the paper! Here's the information about NL-Debugging:

## NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging

NL-DEBUGGING is a novel framework that employs natural language as an intermediate representation to improve code debugging.

**Publication Details:**
- Published in Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 1533–1549, Suzhou, China
- ArXiv preprint 2505.15356 (submitted May 21, 2025)

**Authors:** Weiming Zhang, Qingyao Li, Xinyi Dai, Jizheng Chen, Kounianhua Du, Weiwen Liu, Yasheng Wang, Ruiming Tang, Yong Yu, and Weinan Zhang

**Key Contribution:**
By debugging at a natural language level, NL-DEBUGGING outperforms traditional debugging methods and enables a broader modification space through direct refinement guided by execution feedback.

**Approach:**
The framework has two main stages: In the Backtranslation stage, the buggy code is converted into a natural language version that captures its underlying logic. Next, in the Natural Language Refinement stage, execution feedback is used to analyze the natural language representation, identifying discrepancies between the intended behavior and the actual behavior.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ed2a6f4-dfb6-4a89-a4c5-10a3610ee181",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "4a7654b7-8356-4665-8114-1178f041f434",
  "toolUseResult": {
    "query": "NL-Debugging natural language intermediate representation code debugging EMNLP 2025 arXiv 2505.15356",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KAVNrZjnxpMBnQGd83crfm",
        "content": [
          {
            "title": "NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.80/"
          },
          {
            "title": "Accepted Main Conference Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/main_papers/"
          },
          {
            "title": "[2505.15356] NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging",
            "url": "https://arxiv.org/abs/2505.15356"
          },
          {
            "title": "NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging",
            "url": "https://arxiv.org/html/2505.15356"
          },
          {
            "title": "Weiming Zhang - Homepage",
            "url": "https://wmzhang02.github.io/"
          },
          {
            "title": "NL-Debugging: Exploiting Natural Language as an ...",
            "url": "https://aclanthology.org/2025.emnlp-main.80.pdf"
          },
          {
            "title": "EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=883"
          },
          {
            "title": "Code Execution as Grounded Supervision for LLM ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1260.pdf"
          },
          {
            "title": "EMNLP 2025 The 2025 Conference on Empirical Methods in Natural",
            "url": "https://aclanthology.org/2025.emnlp-tutorials.pdf"
          },
          {
            "title": "dblp: EMNLP",
            "url": "https://dblp.org/db/conf/emnlp/index.html"
          }
        ]
      },
      "I found the paper! Here's the information about NL-Debugging:\n\n## NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging\n\nNL-DEBUGGING is a novel framework that employs natural language as an intermediate representation to improve code debugging.\n\n**Publication Details:**\n- Published in Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 1533–1549, Suzhou, China\n- ArXiv preprint 2505.15356 (submitted May 21, 2025)\n\n**Authors:** Weiming Zhang, Qingyao Li, Xinyi Dai, Jizheng Chen, Kounianhua Du, Weiwen Liu, Yasheng Wang, Ruiming Tang, Yong Yu, and Weinan Zhang\n\n**Key Contribution:**\nBy debugging at a natural language level, NL-DEBUGGING outperforms traditional debugging methods and enables a broader modification space through direct refinement guided by execution feedback.\n\n**Approach:**\nThe framework has two main stages: In the Backtranslation stage, the buggy code is converted into a natural language version that captures its underlying logic. Next, in the Natural Language Refinement stage, execution feedback is used to analyze the natural language representation, identifying discrepancies between the intended behavior and the actual behavior."
    ],
    "durationSeconds": 6.612211240999997
  },
  "sourceToolAssistantUUID": "0ed2a6f4-dfb6-4a89-a4c5-10a3610ee181",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T02:12:58.352Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011JuxqZaB5jDQ5pKp8uezxL`</summary>

```json
{
  "query": "ContractEval benchmark contract satisfaction code generation LLM arXiv 2510.12047"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a7654b7-8356-4665-8114-1178f041f434",
  "isSidechain": false,
  "requestId": "req_011CawsA1zpgxuEFc1FtcCE6",
  "type": "assistant",
  "uuid": "4e8afa01-f8db-4327-8032-e87bb1665502",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EtQNpPzrghR4j89tfnM7rB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 893,
      "cache_read_input_tokens": 44465,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 893,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 44465,
          "cache_creation_input_tokens": 893,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 893
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

_source line 18 · 2026-05-12T02:13:04.407Z_

<details><summary>↩ Tool result · `toolu_011JuxqZaB5jDQ5pKp8uezxL`</summary>

```text
Web search results for query: "ContractEval benchmark contract satisfaction code generation LLM arXiv 2510.12047"

Links: [{"title":"[2510.12047] ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation","url":"https://arxiv.org/abs/2510.12047"},{"title":"ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation","url":"https://arxiv.org/html/2510.12047"},{"title":"ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in","url":"https://arxiv.org/pdf/2508.03080"},{"title":"ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts","url":"https://arxiv.org/html/2508.03080v1"},{"title":"GitHub - olivialiu121/ContractEval · GitHub","url":"https://github.com/olivialiu121/ContractEval"},{"title":"[2508.03080] ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts","url":"https://arxiv.org/abs/2508.03080"},{"title":"ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts","url":"https://www.researchgate.net/publication/394322713_ContractEval_Benchmarking_LLMs_for_Clause-Level_Legal_Risk_Identification_in_Commercial_Contracts"},{"title":"Do Large Language Models Respect Contracts? Evaluating and Enforcing Contract-Adherence in Code Generation","url":"https://arxiv.org/html/2510.12047v2"},{"title":"ContractEval: Benchmarking LLMs for Clause-Level Legal Risk ...","url":"https://www.semanticscholar.org/paper/ContractEval%3A-Benchmarking-LLMs-for-Clause-Level-in-Liu-Li/074acc90e1741ef7f64f4d460e38774068a86b00"},{"title":"ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts - ACL Anthology","url":"https://aclanthology.org/2025.nllp-1.19/"}]

Based on the search results, I found information about arXiv paper 2510.12047:

## ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation

ContractEval is a benchmark for evaluating contract-satisfying assertions in code generation, i.e., whether code rejects contract-violating inputs by triggering intended assertions.

**Key Features:**

Built on HumanEval+ and MBPP+, ContractEval augments each task with contract-violation tests derived from reference assertions. The benchmark synthesizes tests via a neuro-symbolic pipeline: an LLM converts assertion clauses into constraints, and an SMT solver enumerates satisfiable violation combinations to generate inputs that violate selected clauses while satisfying the rest.

**Key Findings:**

Across five code LLMs, standard prompting yields 0% contract satisfaction, while adding a few contract-violation examples boosts contract satisfaction to 49–53% while maintaining pass@1 by 92% of the original. This demonstrates a significant gap between code that appears functionally correct and code that actually respects the contracts and input constraints specified in the task.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e8afa01-f8db-4327-8032-e87bb1665502",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "46222518-4033-4fda-8c10-04fb603521ee",
  "toolUseResult": {
    "query": "ContractEval benchmark contract satisfaction code generation LLM arXiv 2510.12047",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PY6J8kT8U4mPBP1iGRCAUK",
        "content": [
          {
            "title": "[2510.12047] ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation",
            "url": "https://arxiv.org/abs/2510.12047"
          },
          {
            "title": "ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation",
            "url": "https://arxiv.org/html/2510.12047"
          },
          {
            "title": "ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in",
            "url": "https://arxiv.org/pdf/2508.03080"
          },
          {
            "title": "ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts",
            "url": "https://arxiv.org/html/2508.03080v1"
          },
          {
            "title": "GitHub - olivialiu121/ContractEval · GitHub",
            "url": "https://github.com/olivialiu121/ContractEval"
          },
          {
            "title": "[2508.03080] ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts",
            "url": "https://arxiv.org/abs/2508.03080"
          },
          {
            "title": "ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts",
            "url": "https://www.researchgate.net/publication/394322713_ContractEval_Benchmarking_LLMs_for_Clause-Level_Legal_Risk_Identification_in_Commercial_Contracts"
          },
          {
            "title": "Do Large Language Models Respect Contracts? Evaluating and Enforcing Contract-Adherence in Code Generation",
            "url": "https://arxiv.org/html/2510.12047v2"
          },
          {
            "title": "ContractEval: Benchmarking LLMs for Clause-Level Legal Risk ...",
            "url": "https://www.semanticscholar.org/paper/ContractEval%3A-Benchmarking-LLMs-for-Clause-Level-in-Liu-Li/074acc90e1741ef7f64f4d460e38774068a86b00"
          },
          {
            "title": "ContractEval: Benchmarking LLMs for Clause-Level Legal Risk Identification in Commercial Contracts - ACL Anthology",
            "url": "https://aclanthology.org/2025.nllp-1.19/"
          }
        ]
      },
      "Based on the search results, I found information about arXiv paper 2510.12047:\n\n## ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation\n\nContractEval is a benchmark for evaluating contract-satisfying assertions in code generation, i.e., whether code rejects contract-violating inputs by triggering intended assertions.\n\n**Key Features:**\n\nBuilt on HumanEval+ and MBPP+, ContractEval augments each task with contract-violation tests derived from reference assertions. The benchmark synthesizes tests via a neuro-symbolic pipeline: an LLM converts assertion clauses into constraints, and an SMT solver enumerates satisfiable violation combinations to generate inputs that violate selected clauses while satisfying the rest.\n\n**Key Findings:**\n\nAcross five code LLMs, standard prompting yields 0% contract satisfaction, while adding a few contract-violation examples boosts contract satisfaction to 49–53% while maintaining pass@1 by 92% of the original. This demonstrates a significant gap between code that appears functionally correct and code that actually respects the contracts and input constraints specified in the task."
    ],
    "durationSeconds": 6.050950127999997
  },
  "sourceToolAssistantUUID": "4e8afa01-f8db-4327-8032-e87bb1665502",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "46222518-4033-4fda-8c10-04fb603521ee",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "ExeSpec: Execution-grounded Behavioral Specifications for Code LLMs",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Assistant

_source line 21 · 2026-05-12T02:13:07.528Z_

Good, PGS, NL-Debugging, and ContractEval all confirmed as real papers. Now let me search for any NEW competitors the idea might still be missing, and verify the PGS claims more carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46222518-4033-4fda-8c10-04fb603521ee",
  "isSidechain": false,
  "requestId": "req_011CawsAgKftkCGcawsySv2q",
  "type": "assistant",
  "uuid": "8acbfc8a-f4fb-4320-951c-0e0e8f144238",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016USrdVTqkYh3KqApyma76j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 45358,
      "output_tokens": 118,
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
          "output_tokens": 118,
          "cache_read_input_tokens": 45358,
          "cache_creation_input_tokens": 949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 949
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

_source line 22 · 2026-05-12T02:13:08.084Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MJt4wgrEuk2Ax9AyAwZ45a`</summary>

```json
{
  "query": "execution-grounded specification code LLM inference time 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8acbfc8a-f4fb-4320-951c-0e0e8f144238",
  "isSidechain": false,
  "requestId": "req_011CawsAgKftkCGcawsySv2q",
  "type": "assistant",
  "uuid": "bfa457c6-0cfb-4152-af5e-710d92046c92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016USrdVTqkYh3KqApyma76j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 45358,
      "output_tokens": 118,
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
          "output_tokens": 118,
          "cache_read_input_tokens": 45358,
          "cache_creation_input_tokens": 949,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 949
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

_source line 23 · 2026-05-12T02:13:16.409Z_

<details><summary>↩ Tool result · `toolu_01MJt4wgrEuk2Ax9AyAwZ45a`</summary>

```text
Web search results for query: "execution-grounded specification code LLM inference time 2026 arXiv"

Links: [{"title":"Towards Execution-Grounded Automated AI Research","url":"https://arxiv.org/html/2601.14525v1"},{"title":"RLEF: GROUNDING CODE LLMS IN EXECUTION FEEDBACK WITH REINFORCEMENT LEARNING","url":"https://www.arxiv.org/pdf/2410.02089"},{"title":"Code Execution as Grounded Supervision for LLM Reasoning","url":"https://arxiv.org/html/2506.10343"},{"title":"1 Introduction","url":"https://arxiv.org/html/2604.24039"},{"title":"AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering","url":"https://arxiv.org/html/2604.13120v1"},{"title":"Environment-Aware Code Generation: How far are We?","url":"https://arxiv.org/html/2601.12262"},{"title":"[2601.14525] Towards Execution-Grounded Automated AI Research","url":"https://arxiv.org/abs/2601.14525"},{"title":"[2506.10343] Code Execution as Grounded Supervision for LLM Reasoning","url":"https://arxiv.org/abs/2506.10343"},{"title":"RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning","url":"https://arxiv.org/html/2410.02089"},{"title":"Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis","url":"https://arxiv.org/html/2604.10800v1"}]

I found several recent arXiv papers related to execution-grounded specification code and LLM inference. Here are the key results:

## Primary Results:

1. **"Towards Execution-Grounded Automated AI Research"** (January 20, 2026) - This paper discusses how recent work directly guides code generation with execution signals during inference time. The authors built a large-scale parallel executor for automatically executing model-generated ideas to verify their effectiveness on open-ended LLM research problems, and analyzed the effectiveness of execution-guided evolutionary search.

2. **"Code Execution as Grounded Supervision for LLM Reasoning"** (October 17, 2025) - The paper proposes a scalable method for generating high-quality CoT supervision dataset by leveraging the determinism of program execution, extracting verifiable, step-by-step reasoning traces from code execution and transforming them into natural language CoT reasoning. The ablation studies validate that the method reduces overall token length during inference by reducing meaningless repetition and overthinking.

3. **"RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning"** (2024/2025) - Intermediate feedback is crucial to ground LLM generations in concrete situations encountered at inference time, and feedback is naturally provided as the result of the execution of generated code in the form of error messages and unit test results.

4. **"AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering"** (1 month ago) - The paper introduces execution-grounded verification as a first-class principle: every code change must survive sandboxed execution before propagation.

These papers collectively demonstrate the trend of using execution feedback to improve LLM code generation and reasoning at inference time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfa457c6-0cfb-4152-af5e-710d92046c92",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "e87050e6-75f7-429a-8966-1ca3adcfd75e",
  "toolUseResult": {
    "query": "execution-grounded specification code LLM inference time 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_017fy3fBuwNNdacoR6PPkLSn",
        "content": [
          {
            "title": "Towards Execution-Grounded Automated AI Research",
            "url": "https://arxiv.org/html/2601.14525v1"
          },
          {
            "title": "RLEF: GROUNDING CODE LLMS IN EXECUTION FEEDBACK WITH REINFORCEMENT LEARNING",
            "url": "https://www.arxiv.org/pdf/2410.02089"
          },
          {
            "title": "Code Execution as Grounded Supervision for LLM Reasoning",
            "url": "https://arxiv.org/html/2506.10343"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2604.24039"
          },
          {
            "title": "AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering",
            "url": "https://arxiv.org/html/2604.13120v1"
          },
          {
            "title": "Environment-Aware Code Generation: How far are We?",
            "url": "https://arxiv.org/html/2601.12262"
          },
          {
            "title": "[2601.14525] Towards Execution-Grounded Automated AI Research",
            "url": "https://arxiv.org/abs/2601.14525"
          },
          {
            "title": "[2506.10343] Code Execution as Grounded Supervision for LLM Reasoning",
            "url": "https://arxiv.org/abs/2506.10343"
          },
          {
            "title": "RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning",
            "url": "https://arxiv.org/html/2410.02089"
          },
          {
            "title": "Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis",
            "url": "https://arxiv.org/html/2604.10800v1"
          }
        ]
      },
      "I found several recent arXiv papers related to execution-grounded specification code and LLM inference. Here are the key results:\n\n## Primary Results:\n\n1. **\"Towards Execution-Grounded Automated AI Research\"** (January 20, 2026) - This paper discusses how recent work directly guides code generation with execution signals during inference time. The authors built a large-scale parallel executor for automatically executing model-generated ideas to verify their effectiveness on open-ended LLM research problems, and analyzed the effectiveness of execution-guided evolutionary search.\n\n2. **\"Code Execution as Grounded Supervision for LLM Reasoning\"** (October 17, 2025) - The paper proposes a scalable method for generating high-quality CoT supervision dataset by leveraging the determinism of program execution, extracting verifiable, step-by-step reasoning traces from code execution and transforming them into natural language CoT reasoning. The ablation studies validate that the method reduces overall token length during inference by reducing meaningless repetition and overthinking.\n\n3. **\"RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning\"** (2024/2025) - Intermediate feedback is crucial to ground LLM generations in concrete situations encountered at inference time, and feedback is naturally provided as the result of the execution of generated code in the form of error messages and unit test results.\n\n4. **\"AgentForge: Execution-Grounded Multi-Agent LLM Framework for Autonomous Software Engineering\"** (1 month ago) - The paper introduces execution-grounded verification as a first-class principle: every code change must survive sandboxed execution before propagation.\n\nThese papers collectively demonstrate the trend of using execution feedback to improve LLM code generation and reasoning at inference time."
    ],
    "durationSeconds": 8.320512901000003
  },
  "sourceToolAssistantUUID": "bfa457c6-0cfb-4152-af5e-710d92046c92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-12T02:13:18.751Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lk7Qgq8uKSjCvMdNGm6y9Q`</summary>

```json
{
  "query": "specification-guided code repair debugging LLM 2026 training-free inference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e87050e6-75f7-429a-8966-1ca3adcfd75e",
  "isSidechain": false,
  "requestId": "req_011CawsBZLWksrQ7C59BpqBt",
  "type": "assistant",
  "uuid": "4fa3dc95-58cc-476a-83e2-691afda5d2b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRPntAXDUhkTigHaqbfXbL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 46307,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 976,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 46307,
          "cache_creation_input_tokens": 976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 976
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

_source line 25 · 2026-05-12T02:13:25.997Z_

<details><summary>↩ Tool result · `toolu_01Lk7Qgq8uKSjCvMdNGm6y9Q`</summary>

```text
Web search results for query: "specification-guided code repair debugging LLM 2026 training-free inference"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"1 Understanding and Mitigating Errors of LLM-Generated RTL Code","url":"https://arxiv.org/pdf/2508.05266"},{"title":"Code Repair with LLMs gives an Exploration-Exploitation Tradeoff Hao Tang","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d5c56ec4f69c9a473089b16000d3f8cd-Paper-Conference.pdf"},{"title":"Automated Program Repair via Conversation:","url":"https://lingming.cs.illinois.edu/publications/issta2024.pdf"},{"title":"Published as a conference paper at ICLR 2024 TEACHING LARGE LANGUAGE MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf"},{"title":"An empirical evaluation of pre-trained large language models for repairing","url":"https://research.chalmers.se/publication/547703/file/547703_Fulltext.pdf"},{"title":"LLM-Aided Efficient Hardware Design Automation","url":"https://arxiv.org/pdf/2410.18582"},{"title":"1 Synthetic Code Surgery: Repairing Bugs and Vulnerabilities with LLMs","url":"https://arxiv.org/pdf/2505.07372"},{"title":"Automated Repair of Programs from Large Language Models Zhiyu Fan","url":"https://people.cs.umass.edu/~brun/class/2024Fall/CS692P/aprllm.pdf"},{"title":"FVDebug: An LLM-Driven Debugging Assistant for ...","url":"https://arxiv.org/pdf/2510.15906"}]

I found relevant search results on LLM-based code repair and debugging. Here's what the search revealed:

## Overview of Specification-Guided Code Repair with LLMs

Recent work includes "A Systematic Literature Review on Large Language Models for Automated Program Repair" published in TOSEM 2026, which comprehensively covers this emerging field.

## Key Research Areas

**Training-Free and Inference Approaches:**
SELF-DEBUGGING utilizes pretrained LLMs and teaches the model to debug via prompting without requiring a separate code repair model. Additionally, few-shot learning enables LLMs to generalize from a minimal number of examples directly provided in input prompts requiring no additional training, while zero-shot learning further extends adaptability by requiring no task-specific training or examples.

**Specification-Guided Approaches:**
Rule-based description refinement leverages LLMs to enforce key circuit design rules such as register initialization, reset/enable signal integrity, and internal logical consistency. FVDebug features a novel pipeline including Causal Graph Synthesis that structures failure traces into directed acyclic graphs, Graph Scanner using batched LLM analysis with for-and-against prompting to identify suspicious nodes, and Insight Rover leveraging agentic narrative exploration to generate high-level causal explanations.

**Recent 2025 Work:**
Recent advances include Template-Guided Program Repair in the Era of Large Language Models and Aligning the Objective of LLM-based Program Repair, both from 2025-ICSE.

The research demonstrates substantial progress in developing LLM-based debugging and repair systems that can work effectively without extensive fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fa3dc95-58cc-476a-83e2-691afda5d2b2",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "aebbe94e-0e9a-4f67-9d34-42807ed03684",
  "toolUseResult": {
    "query": "specification-guided code repair debugging LLM 2026 training-free inference",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UEka9H9XHV9SJrF5v7hqCp",
        "content": [
          {
            "title": "GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub",
            "url": "https://github.com/iSEngLab/AwesomeLLM4APR"
          },
          {
            "title": "1 Understanding and Mitigating Errors of LLM-Generated RTL Code",
            "url": "https://arxiv.org/pdf/2508.05266"
          },
          {
            "title": "Code Repair with LLMs gives an Exploration-Exploitation Tradeoff Hao Tang",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/d5c56ec4f69c9a473089b16000d3f8cd-Paper-Conference.pdf"
          },
          {
            "title": "Automated Program Repair via Conversation:",
            "url": "https://lingming.cs.illinois.edu/publications/issta2024.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 TEACHING LARGE LANGUAGE MODELS",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/2460396f2d0d421885997dd1612ac56b-Paper-Conference.pdf"
          },
          {
            "title": "An empirical evaluation of pre-trained large language models for repairing",
            "url": "https://research.chalmers.se/publication/547703/file/547703_Fulltext.pdf"
          },
          {
            "title": "LLM-Aided Efficient Hardware Design Automation",
            "url": "https://arxiv.org/pdf/2410.18582"
          },
          {
            "title": "1 Synthetic Code Surgery: Repairing Bugs and Vulnerabilities with LLMs",
            "url": "https://arxiv.org/pdf/2505.07372"
          },
          {
            "title": "Automated Repair of Programs from Large Language Models Zhiyu Fan",
            "url": "https://people.cs.umass.edu/~brun/class/2024Fall/CS692P/aprllm.pdf"
          },
          {
            "title": "FVDebug: An LLM-Driven Debugging Assistant for ...",
            "url": "https://arxiv.org/pdf/2510.15906"
          }
        ]
      },
      "I found relevant search results on LLM-based code repair and debugging. Here's what the search revealed:\n\n## Overview of Specification-Guided Code Repair with LLMs\n\nRecent work includes \"A Systematic Literature Review on Large Language Models for Automated Program Repair\" published in TOSEM 2026, which comprehensively covers this emerging field.\n\n## Key Research Areas\n\n**Training-Free and Inference Approaches:**\nSELF-DEBUGGING utilizes pretrained LLMs and teaches the model to debug via prompting without requiring a separate code repair model. Additionally, few-shot learning enables LLMs to generalize from a minimal number of examples directly provided in input prompts requiring no additional training, while zero-shot learning further extends adaptability by requiring no task-specific training or examples.\n\n**Specification-Guided Approaches:**\nRule-based description refinement leverages LLMs to enforce key circuit design rules such as register initialization, reset/enable signal integrity, and internal logical consistency. FVDebug features a novel pipeline including Causal Graph Synthesis that structures failure traces into directed acyclic graphs, Graph Scanner using batched LLM analysis with for-and-against prompting to identify suspicious nodes, and Insight Rover leveraging agentic narrative exploration to generate high-level causal explanations.\n\n**Recent 2025 Work:**\nRecent advances include Template-Guided Program Repair in the Era of Large Language Models and Aligning the Objective of LLM-based Program Repair, both from 2025-ICSE.\n\nThe research demonstrates substantial progress in developing LLM-based debugging and repair systems that can work effectively without extensive fine-tuning."
    ],
    "durationSeconds": 7.2414387120000026
  },
  "sourceToolAssistantUUID": "4fa3dc95-58cc-476a-83e2-691afda5d2b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-12T02:13:28.396Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G9B3e6HMXtdSvyov4ZvM3Y`</summary>

```json
{
  "query": "property-based feedback code generation LLM precondition postcondition invariant 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aebbe94e-0e9a-4f67-9d34-42807ed03684",
  "isSidechain": false,
  "requestId": "req_011CawsCGJc4rtwPEcP4DmE8",
  "type": "assistant",
  "uuid": "36f67a74-b6b1-40c8-b331-ab0a7e026de2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KAEGM99jxTxHdJz7WdJDYn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1010,
      "cache_read_input_tokens": 47283,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1010,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 47283,
          "cache_creation_input_tokens": 1010,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1010
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

_source line 27 · 2026-05-12T02:13:39.156Z_

<details><summary>↩ Tool result · `toolu_01G9B3e6HMXtdSvyov4ZvM3Y`</summary>

```text
Web search results for query: "property-based feedback code generation LLM precondition postcondition invariant 2025 2026"

Links: [{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"Clover: Closed-Loop Verifiable Code Generation Chuyue Sun1⋆ Ying Sheng1∗","url":"https://theory.stanford.edu/~barrett/pubs/SSP+24.pdf"},{"title":"LLMs and Fuzzing in Tandem: A New Approach to Automatically Generating Weakest Preconditions","url":"https://arxiv.org/html/2507.05272"},{"title":"Beyond Postconditions: Can Large Language Models infer Formal Contracts for","url":"https://arxiv.org/pdf/2510.12702"},{"title":"LLM For Loop Invariant Generation and Fixing","url":"https://arxiv.org/pdf/2511.06552"},{"title":"Integrating Symbolic Execution with LLMs for Automated Generation of Program Specifications","url":"https://arxiv.org/html/2506.09550v4"},{"title":"Hoare Logic for Code and Cloud: What 1969 Computer Science Offers 2026 Engineering","url":"https://zircon.tech/blog/hoare-logic-for-code-and-cloud-what-1969-computer-science-offers-2026-engineering/"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"FuzzFeed: An Automatic Approach to Weakest Precondition Generation using LLMs and Fuzzing This work was conducted with the financial support of the Research Ireland Centre for Research Training in Digitally-Enhanced Reality (d-real) under Grant No. 18/CRT/6224, Taighde Éireann – Research Ireland under Grant number 13/RC/2094/\\_2, and the ERC Consolidator Grant ARTIST 101002685. For the purpose of Open Access, the author has applied a CC BY public copyright licence to any Author Accepted Manuscript versio","url":"https://arxiv.org/html/2507.05272v1"},{"title":"Enchanting Program Specification Synthesis by","url":"https://arxiv.org/pdf/2404.00762"}]

Based on the search results, here's a comprehensive overview of recent research on property-based feedback for code generation with LLMs, focusing on preconditions, postconditions, and loop invariants (2025-2026):

## Key Recent Systems and Approaches

**AutoSpec and Verification-Driven Systems**
AutoSpec generates pre/postconditions and loop invariants using LLMs and verifier feedback, relying on ACSL assertions encoding general correctness properties, making it property-driven rather than test-driven. Using an iterative feedback loop, AutoSpec verifies 79% of 251 C programs within five attempts.

**Clover: Closed-Loop Verifiable Code Generation**
LLMs are reasonably successful at automatically generating formal specifications, and consistency checkers achieve promising acceptance rates (up to 87%) for correct instances while maintaining zero tolerance for adversarial incorrect ones.

**LLMs and Fuzzing Integration (2025)**
Research proposes the combination of Large Language Models and fuzz testing for generating weakest preconditions, introducing Fuzzing Guidance (FG) to direct LLMs towards correct WPs using program execution feedback.

**NL2Contract: Formal Contract Inference (2025)**
The task of NL2Contract involves employing LLMs to translate informal natural language into formal functional contracts, consisting of postconditions as well as preconditions.

**Loop Invariant Generation (2025)**
Recent work studies the effectiveness of LLMs to create and repair loop invariants, examining whether LLMs can repair incorrect loop invariants using feedback.

**SESpec: Integration with Symbolic Execution (January 2026)**
A framework integrates symbolic execution with large language models to automatically synthesize formally verified program specifications, using symbolic execution results and automatically generated invariant templates to guide the LLM to propose and iteratively refine loop invariants.

**NeuroInv and Production-Ready Approaches (2025)**
NeuroInv combines LLMs with Hoare logic directly, using an LLM to derive candidate loop invariants via backward-chaining weakest precondition reasoning, with a symbolic component repairing them using counterexamples from the verifier, achieving 99.5% success rate on 150 Java programs.

## Common Pattern

The pattern across research is consistent: an LLM generates specifications (preconditions, postconditions, invariants), an automated verifier checks them against the code, and if verification fails, the LLM uses the verifier's counterexample to refine the specification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36f67a74-b6b1-40c8-b331-ab0a7e026de2",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "c5ca7b2e-e878-4225-a665-a895b6acd627",
  "toolUseResult": {
    "query": "property-based feedback code generation LLM precondition postcondition invariant 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XTCK7uuWofMT7moBW62QuB",
        "content": [
          {
            "title": "Automatic Generation of Formal Specification and ...",
            "url": "https://arxiv.org/pdf/2601.12845"
          },
          {
            "title": "Clover: Closed-Loop Verifiable Code Generation Chuyue Sun1⋆ Ying Sheng1∗",
            "url": "https://theory.stanford.edu/~barrett/pubs/SSP+24.pdf"
          },
          {
            "title": "LLMs and Fuzzing in Tandem: A New Approach to Automatically Generating Weakest Preconditions",
            "url": "https://arxiv.org/html/2507.05272"
          },
          {
            "title": "Beyond Postconditions: Can Large Language Models infer Formal Contracts for",
            "url": "https://arxiv.org/pdf/2510.12702"
          },
          {
            "title": "LLM For Loop Invariant Generation and Fixing",
            "url": "https://arxiv.org/pdf/2511.06552"
          },
          {
            "title": "Integrating Symbolic Execution with LLMs for Automated Generation of Program Specifications",
            "url": "https://arxiv.org/html/2506.09550v4"
          },
          {
            "title": "Hoare Logic for Code and Cloud: What 1969 Computer Science Offers 2026 Engineering",
            "url": "https://zircon.tech/blog/hoare-logic-for-code-and-cloud-what-1969-computer-science-offers-2026-engineering/"
          },
          {
            "title": "GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub",
            "url": "https://github.com/iSEngLab/AwesomeLLM4SE"
          },
          {
            "title": "FuzzFeed: An Automatic Approach to Weakest Precondition Generation using LLMs and Fuzzing This work was conducted with the financial support of the Research Ireland Centre for Research Training in Digitally-Enhanced Reality (d-real) under Grant No. 18/CRT/6224, Taighde Éireann – Research Ireland under Grant number 13/RC/2094/\\_2, and the ERC Consolidator Grant ARTIST 101002685. For the purpose of Open Access, the author has applied a CC BY public copyright licence to any Author Accepted Manuscript versio",
            "url": "https://arxiv.org/html/2507.05272v1"
          },
          {
            "title": "Enchanting Program Specification Synthesis by",
            "url": "https://arxiv.org/pdf/2404.00762"
          }
        ]
      },
      "Based on the search results, here's a comprehensive overview of recent research on property-based feedback for code generation with LLMs, focusing on preconditions, postconditions, and loop invariants (2025-2026):\n\n## Key Recent Systems and Approaches\n\n**AutoSpec and Verification-Driven Systems**\nAutoSpec generates pre/postconditions and loop invariants using LLMs and verifier feedback, relying on ACSL assertions encoding general correctness properties, making it property-driven rather than test-driven. Using an iterative feedback loop, AutoSpec verifies 79% of 251 C programs within five attempts.\n\n**Clover: Closed-Loop Verifiable Code Generation**\nLLMs are reasonably successful at automatically generating formal specifications, and consistency checkers achieve promising acceptance rates (up to 87%) for correct instances while maintaining zero tolerance for adversarial incorrect ones.\n\n**LLMs and Fuzzing Integration (2025)**\nResearch proposes the combination of Large Language Models and fuzz testing for generating weakest preconditions, introducing Fuzzing Guidance (FG) to direct LLMs towards correct WPs using program execution feedback.\n\n**NL2Contract: Formal Contract Inference (2025)**\nThe task of NL2Contract involves employing LLMs to translate informal natural language into formal functional contracts, consisting of postconditions as well as preconditions.\n\n**Loop Invariant Generation (2025)**\nRecent work studies the effectiveness of LLMs to create and repair loop invariants, examining whether LLMs can repair incorrect loop invariants using feedback.\n\n**SESpec: Integration with Symbolic Execution (January 2026)**\nA framework integrates symbolic execution with large language models to automatically synthesize formally verified program specifications, using symbolic execution results and automatically generated invariant templates to guide the LLM to propose and iteratively refine loop invariants.\n\n**NeuroInv and Production-Ready Approaches (2025)**\nNeuroInv combines LLMs with Hoare logic directly, using an LLM to derive candidate loop invariants via backward-chaining weakest precondition reasoning, with a symbolic component repairing them using counterexamples from the verifier, achieving 99.5% success rate on 150 Java programs.\n\n## Common Pattern\n\nThe pattern across research is consistent: an LLM generates specifications (preconditions, postconditions, invariants), an automated verifier checks them against the code, and if verification fails, the LLM uses the verifier's counterexample to refine the specification."
    ],
    "durationSeconds": 10.753983945
  },
  "sourceToolAssistantUUID": "36f67a74-b6b1-40c8-b331-ab0a7e026de2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28 · 2026-05-12T02:13:39.163Z_

```json
{
  "parentUuid": "c5ca7b2e-e878-4225-a665-a895b6acd627",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8dee9959-a86d-4b83-a0c0-06bfbc5e2b55",
  "timestamp": "2026-05-12T02:13:39.163Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 29 · 2026-05-12T02:13:42.254Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RRuNvcf3eRckTqW4mSq5Y4`</summary>

```json
{
  "query": "StoryCoder narrative reformulation code generation ACL 2026 arXiv 2604.14631"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dee9959-a86d-4b83-a0c0-06bfbc5e2b55",
  "isSidechain": false,
  "requestId": "req_011CawsDEawwji24HZM8vZ41",
  "type": "assistant",
  "uuid": "8384bd55-0eb0-4eee-ab6c-6fac428107e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168UU9CkbafvJVf16ktDHM5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 48293,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1390,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 48293,
          "cache_creation_input_tokens": 1390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1390
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

_source line 30 · 2026-05-12T02:13:48.986Z_

<details><summary>↩ Tool result · `toolu_01RRuNvcf3eRckTqW4mSq5Y4`</summary>

```text
Web search results for query: "StoryCoder narrative reformulation code generation ACL 2026 arXiv 2604.14631"

Links: [{"title":"[2604.14631] StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation","url":"https://arxiv.org/abs/2604.14631"},{"title":"StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation","url":"https://arxiv.org/html/2604.14631"},{"title":"StoryCoder: Narrative Reformulation for Structured Reasoning in LLM","url":"https://openreview.net/pdf/40080f64660a67f08c570e52ada2a3a1b40a1789.pdf"},{"title":"Hierarchical Neural Story Generation","url":"https://aclanthology.org/P18-1082.pdf"},{"title":"A Survey on LLMs for Story Generation","url":"https://aclanthology.org/2025.findings-emnlp.750.pdf"},{"title":"NarrativeLoom: Enhancing Creative Storytelling through Multi-Persona Collaborative Improvisation","url":"https://arxiv.org/html/2603.07155v1"},{"title":"story · ArXiv Text Gen Searches","url":"https://arnicas.github.io/text-gen-arxiv-papers/categories/story/story.html"},{"title":"[2406.00554] Guiding and Diversifying LLM-Based Story Generation via Answer Set Programming","url":"https://arxiv.org/abs/2406.00554"},{"title":"Guiding and Diversifying LLM-Based Story Generation via Answer Set Programming","url":"https://arxiv.org/html/2406.00554v1"},{"title":"Learning to Reason for Long-Form Story Generation","url":"https://arxiv.org/pdf/2503.22828"}]

Based on the search results, I found information about StoryCoder (arXiv 2604.14631):

## StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation

StoryCoder was submitted to arXiv on April 16, 2026, with authors Geonhui Jang, Dongyoon Han, and YoungJoon Yoo.

**Overview:**
StoryCoder is a narrative reformulation framework that transforms code generation questions into coherent natural language narratives, providing richer contextual structure than simple rephrasings.

**Key Components:**
Each narrative consists of three components: a task overview, constraints, and example test cases, guided by the selected algorithm and genre.

**Methodology:**
In this framework, models identify the appropriate algorithm that will form the logic of the code, align it with a suitable narrative genre, and reformulate it into a story with three sections: task overview, constraints, and example input/output.

**Evaluation:**
Experiments across 11 models on HumanEval, LiveCodeBench, and CodeForces demonstrate consistent improvements.

**Underlying Motivation:**
The design is based on findings of cognitive science that humans comprehend and reason more effectively when organizing fragmented conditions into coherent mental models using analogical structures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8384bd55-0eb0-4eee-ab6c-6fac428107e5",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "c42286fb-edf4-445f-a491-ba52b863f9ff",
  "toolUseResult": {
    "query": "StoryCoder narrative reformulation code generation ACL 2026 arXiv 2604.14631",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VnKgsigFcC4gpHsnhQwueJ",
        "content": [
          {
            "title": "[2604.14631] StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation",
            "url": "https://arxiv.org/abs/2604.14631"
          },
          {
            "title": "StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation",
            "url": "https://arxiv.org/html/2604.14631"
          },
          {
            "title": "StoryCoder: Narrative Reformulation for Structured Reasoning in LLM",
            "url": "https://openreview.net/pdf/40080f64660a67f08c570e52ada2a3a1b40a1789.pdf"
          },
          {
            "title": "Hierarchical Neural Story Generation",
            "url": "https://aclanthology.org/P18-1082.pdf"
          },
          {
            "title": "A Survey on LLMs for Story Generation",
            "url": "https://aclanthology.org/2025.findings-emnlp.750.pdf"
          },
          {
            "title": "NarrativeLoom: Enhancing Creative Storytelling through Multi-Persona Collaborative Improvisation",
            "url": "https://arxiv.org/html/2603.07155v1"
          },
          {
            "title": "story · ArXiv Text Gen Searches",
            "url": "https://arnicas.github.io/text-gen-arxiv-papers/categories/story/story.html"
          },
          {
            "title": "[2406.00554] Guiding and Diversifying LLM-Based Story Generation via Answer Set Programming",
            "url": "https://arxiv.org/abs/2406.00554"
          },
          {
            "title": "Guiding and Diversifying LLM-Based Story Generation via Answer Set Programming",
            "url": "https://arxiv.org/html/2406.00554v1"
          },
          {
            "title": "Learning to Reason for Long-Form Story Generation",
            "url": "https://arxiv.org/pdf/2503.22828"
          }
        ]
      },
      "Based on the search results, I found information about StoryCoder (arXiv 2604.14631):\n\n## StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation\n\nStoryCoder was submitted to arXiv on April 16, 2026, with authors Geonhui Jang, Dongyoon Han, and YoungJoon Yoo.\n\n**Overview:**\nStoryCoder is a narrative reformulation framework that transforms code generation questions into coherent natural language narratives, providing richer contextual structure than simple rephrasings.\n\n**Key Components:**\nEach narrative consists of three components: a task overview, constraints, and example test cases, guided by the selected algorithm and genre.\n\n**Methodology:**\nIn this framework, models identify the appropriate algorithm that will form the logic of the code, align it with a suitable narrative genre, and reformulate it into a story with three sections: task overview, constraints, and example input/output.\n\n**Evaluation:**\nExperiments across 11 models on HumanEval, LiveCodeBench, and CodeForces demonstrate consistent improvements.\n\n**Underlying Motivation:**\nThe design is based on findings of cognitive science that humans comprehend and reason more effectively when organizing fragmented conditions into coherent mental models using analogical structures."
    ],
    "durationSeconds": 6.727348067999992
  },
  "sourceToolAssistantUUID": "8384bd55-0eb0-4eee-ab6c-6fac428107e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "c42286fb-edf4-445f-a491-ba52b863f9ff",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "ExeSpec: Execution-grounded Behavioral Specifications for Code LLMs",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Tool call

_source line 33 · 2026-05-12T02:13:51.459Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GiGMsN5KSZQBdiMd8n8ovk`</summary>

```json
{
  "query": "SWE-bench Pro contamination verified 2026 frontier models gold patch"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c42286fb-edf4-445f-a491-ba52b863f9ff",
  "isSidechain": false,
  "requestId": "req_011CawsDxa4RRa3b7teBXQfu",
  "type": "assistant",
  "uuid": "72f3eebe-30bd-4d75-b513-cac949bdab22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QqzDZp344w8bCUuVq6VZTD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 857,
      "cache_read_input_tokens": 49683,
      "output_tokens": 68,
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
          "output_tokens": 68,
          "cache_read_input_tokens": 49683,
          "cache_creation_input_tokens": 857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 857
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

_source line 34 · 2026-05-12T02:13:59.357Z_

<details><summary>↩ Tool result · `toolu_01GiGMsN5KSZQBdiMd8n8ovk`</summary>

```text
Web search results for query: "SWE-bench Pro contamination verified 2026 frontier models gold patch"

Links: [{"title":"Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI","url":"https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"},{"title":"SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean","url":"https://www.codeant.ai/blogs/swe-bench-scores"},{"title":"SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%","url":"https://www.morphllm.com/swe-bench-pro"},{"title":"SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale","url":"https://labs.scale.com/leaderboard/swe_bench_pro_public"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"SWE-Bench Explained (2026): Methodology, Scoring, Contamination | CodeSOTA","url":"https://www.codesota.com/guides/swe-bench-explained"},{"title":"SWE-bench Verified","url":"https://www.swebench.com/verified.html"},{"title":"SWE-Bench Explained: Benchmarks, Verified, Pro, and the 2026 Leaderboard","url":"https://www.morphllm.com/swe-benchmark"},{"title":"SWE-bench Verified Benchmark 2026: 44 LLM scores | BenchLM.ai","url":"https://benchlm.ai/benchmarks/sweVerified"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"}]

Based on the search results, here's what has been verified about SWE-bench Pro contamination and frontier models in 2026:

## Contamination Verification

OpenAI's audit found that every frontier model tested (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could reproduce verbatim gold patches or problem statement specifics for certain SWE-Bench Verified tasks. They also found that 59.4% of the hardest unsolved problems had flawed test cases.

## SWE-bench Pro vs. Verified

The contamination issues with SWE-bench Verified prompted the development of SWE-bench Pro. SWE-bench Pro is the newest and hardest version, built by Scale AI to be contamination-resistant. The best model scores 46% on Pro but 81% on Verified, because Verified is contaminated. Claude Opus 4.5 scores 80.9% on SWE-Bench Verified and 45.9% on SWE-Bench Pro. Same model, half the score.

## Contamination Prevention in Pro

SWE-bench Pro contains 1,865 tasks across 41 actively maintained repositories in Python, Go, TypeScript, and JavaScript, including private proprietary startup codebases that have never been publicly available. Tasks come from real commit histories. Because the private codebases are legally inaccessible to model trainers, contamination is structurally prevented.

## Industry Response

OpenAI has stopped reporting Verified scores after finding that every frontier model showed training data contamination on the dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72f3eebe-30bd-4d75-b513-cac949bdab22",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "17a26f19-807e-4783-a8a9-60f6f6cd429a",
  "toolUseResult": {
    "query": "SWE-bench Pro contamination verified 2026 frontier models gold patch",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JaZ8R1Yb3tDyLzs342ZvXe",
        "content": [
          {
            "title": "Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI",
            "url": "https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"
          },
          {
            "title": "SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean",
            "url": "https://www.codeant.ai/blogs/swe-bench-scores"
          },
          {
            "title": "SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%",
            "url": "https://www.morphllm.com/swe-bench-pro"
          },
          {
            "title": "SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale",
            "url": "https://labs.scale.com/leaderboard/swe_bench_pro_public"
          },
          {
            "title": "SWE-Bench Verified Benchmark Leaderboard",
            "url": "https://llm-stats.com/benchmarks/swe-bench-verified"
          },
          {
            "title": "SWE-Bench Explained (2026): Methodology, Scoring, Contamination | CodeSOTA",
            "url": "https://www.codesota.com/guides/swe-bench-explained"
          },
          {
            "title": "SWE-bench Verified",
            "url": "https://www.swebench.com/verified.html"
          },
          {
            "title": "SWE-Bench Explained: Benchmarks, Verified, Pro, and the 2026 Leaderboard",
            "url": "https://www.morphllm.com/swe-benchmark"
          },
          {
            "title": "SWE-bench Verified Benchmark 2026: 44 LLM scores | BenchLM.ai",
            "url": "https://benchlm.ai/benchmarks/sweVerified"
          },
          {
            "title": "SWE-bench Verified | Epoch AI",
            "url": "https://epoch.ai/benchmarks/swe-bench-verified"
          }
        ]
      },
      "Based on the search results, here's what has been verified about SWE-bench Pro contamination and frontier models in 2026:\n\n## Contamination Verification\n\nOpenAI's audit found that every frontier model tested (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could reproduce verbatim gold patches or problem statement specifics for certain SWE-Bench Verified tasks. They also found that 59.4% of the hardest unsolved problems had flawed test cases.\n\n## SWE-bench Pro vs. Verified\n\nThe contamination issues with SWE-bench Verified prompted the development of SWE-bench Pro. SWE-bench Pro is the newest and hardest version, built by Scale AI to be contamination-resistant. The best model scores 46% on Pro but 81% on Verified, because Verified is contaminated. Claude Opus 4.5 scores 80.9% on SWE-Bench Verified and 45.9% on SWE-Bench Pro. Same model, half the score.\n\n## Contamination Prevention in Pro\n\nSWE-bench Pro contains 1,865 tasks across 41 actively maintained repositories in Python, Go, TypeScript, and JavaScript, including private proprietary startup codebases that have never been publicly available. Tasks come from real commit histories. Because the private codebases are legally inaccessible to model trainers, contamination is structurally prevented.\n\n## Industry Response\n\nOpenAI has stopped reporting Verified scores after finding that every frontier model showed training data contamination on the dataset."
    ],
    "durationSeconds": 7.894649730000005
  },
  "sourceToolAssistantUUID": "72f3eebe-30bd-4d75-b513-cac949bdab22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-12T02:14:02.140Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WwEV3NfL2rwS73QbHjj15x`</summary>

```json
{
  "query": "CodeSpecBench LLM behavioral specification generation benchmark arXiv 2604.12268"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17a26f19-807e-4783-a8a9-60f6f6cd429a",
  "isSidechain": false,
  "requestId": "req_011CawsEiv48XBL8y8fUPBDx",
  "type": "assistant",
  "uuid": "45a3bdca-7383-4e0c-a623-d7276c5a453c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SjFWixUrm67Ka5kwcJufW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 938,
      "cache_read_input_tokens": 50540,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 938,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 50540,
          "cache_creation_input_tokens": 938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 938
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

_source line 36 · 2026-05-12T02:14:09.350Z_

<details><summary>↩ Tool result · `toolu_01WwEV3NfL2rwS73QbHjj15x`</summary>

```text
Web search results for query: "CodeSpecBench LLM behavioral specification generation benchmark arXiv 2604.12268"

Links: [{"title":"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/html/2604.12268v1"},{"title":"[2604.12268] CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation","url":"https://arxiv.org/abs/2604.12268"},{"title":"GitHub - tongye98/Awesome-Code-Benchmark: A comprehensive code domain benchmark review of LLM researches. · GitHub","url":"https://github.com/tongye98/Awesome-Code-Benchmark"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"Paper page - Precise Debugging Benchmark: Is Your Model Debugging or Regenerating?","url":"https://huggingface.co/papers/2604.17338"},{"title":"15 LLM coding benchmarks","url":"https://www.evidentlyai.com/blog/llm-coding-benchmarks"},{"title":"Benchmarks and Metrics for Evaluations of Code Generation: A Critical Review","url":"https://arxiv.org/html/2406.12655v1"},{"title":"CLEVER: A Curated Benchmark for Formally Verified Code Generation","url":"https://arxiv.org/pdf/2505.13938"},{"title":"GitHub - akitaonrails/llm-coding-benchmark: Simple benchmark to test the most popular open source and commercial LLMs with automated OpenCode · GitHub","url":"https://github.com/akitaonrails/llm-coding-benchmark"},{"title":"LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code","url":"https://livecodebench.github.io/"}]

Based on the web search results, I found the arXiv paper you were looking for. Here's the information about CodeSpecBench:

## CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation

CodeSpecBench is a benchmark for executable behavioral specification generation under an execution-based evaluation protocol that supports both function-level and repository-level tasks and encodes specifications as executable Python functions.

### Key Features

Constructed from diverse real-world codebases, it enables a realistic assessment of both correctness (accepting valid behaviors) and completeness (rejecting invalid behaviors). CodeSpecBench includes both preconditions and postconditions, expressed as executable Python functions, allowing flexible and expressive behavioral constraints.

### Performance Findings

Evaluating 15 state-of-the-art LLMs on CodeSpecBench, the benchmark shows a sharp performance degradation on repository-level tasks, where the best model attains only a 20.2% pass rate. On CodeSpecBench-Func, the overall pass rate remains limited even for the strongest models: the best is 47.0% (GPT-5-mini), followed by 46.2% (Gemini-2.5-Pro) and 42.5% (GPT-OSS-120B).

### Key Insight

Specification generation is substantially more challenging than code generation, indicating that strong coding performance does not necessarily reflect deep understanding of intended program semantics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45a3bdca-7383-4e0c-a623-d7276c5a453c",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "89bb2860-d60e-4329-8faa-11c28d7ba3d5",
  "toolUseResult": {
    "query": "CodeSpecBench LLM behavioral specification generation benchmark arXiv 2604.12268",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LXiPmjsVjo9RWKut9XSQB1",
        "content": [
          {
            "title": "CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation",
            "url": "https://arxiv.org/html/2604.12268v1"
          },
          {
            "title": "[2604.12268] CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation",
            "url": "https://arxiv.org/abs/2604.12268"
          },
          {
            "title": "GitHub - tongye98/Awesome-Code-Benchmark: A comprehensive code domain benchmark review of LLM researches. · GitHub",
            "url": "https://github.com/tongye98/Awesome-Code-Benchmark"
          },
          {
            "title": "LLM Benchmarks 2026 - Compare AI Benchmarks and Tests",
            "url": "https://llm-stats.com/benchmarks"
          },
          {
            "title": "Paper page - Precise Debugging Benchmark: Is Your Model Debugging or Regenerating?",
            "url": "https://huggingface.co/papers/2604.17338"
          },
          {
            "title": "15 LLM coding benchmarks",
            "url": "https://www.evidentlyai.com/blog/llm-coding-benchmarks"
          },
          {
            "title": "Benchmarks and Metrics for Evaluations of Code Generation: A Critical Review",
            "url": "https://arxiv.org/html/2406.12655v1"
          },
          {
            "title": "CLEVER: A Curated Benchmark for Formally Verified Code Generation",
            "url": "https://arxiv.org/pdf/2505.13938"
          },
          {
            "title": "GitHub - akitaonrails/llm-coding-benchmark: Simple benchmark to test the most popular open source and commercial LLMs with automated OpenCode · GitHub",
            "url": "https://github.com/akitaonrails/llm-coding-benchmark"
          },
          {
            "title": "LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code",
            "url": "https://livecodebench.github.io/"
          }
        ]
      },
      "Based on the web search results, I found the arXiv paper you were looking for. Here's the information about CodeSpecBench:\n\n## CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation\n\nCodeSpecBench is a benchmark for executable behavioral specification generation under an execution-based evaluation protocol that supports both function-level and repository-level tasks and encodes specifications as executable Python functions.\n\n### Key Features\n\nConstructed from diverse real-world codebases, it enables a realistic assessment of both correctness (accepting valid behaviors) and completeness (rejecting invalid behaviors). CodeSpecBench includes both preconditions and postconditions, expressed as executable Python functions, allowing flexible and expressive behavioral constraints.\n\n### Performance Findings\n\nEvaluating 15 state-of-the-art LLMs on CodeSpecBench, the benchmark shows a sharp performance degradation on repository-level tasks, where the best model attains only a 20.2% pass rate. On CodeSpecBench-Func, the overall pass rate remains limited even for the strongest models: the best is 47.0% (GPT-5-mini), followed by 46.2% (Gemini-2.5-Pro) and 42.5% (GPT-OSS-120B).\n\n### Key Insight\n\nSpecification generation is substantially more challenging than code generation, indicating that strong coding performance does not necessarily reflect deep understanding of intended program semantics."
    ],
    "durationSeconds": 7.206628515999997
  },
  "sourceToolAssistantUUID": "45a3bdca-7383-4e0c-a623-d7276c5a453c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-12T02:14:12.494Z_

Now let me search for any NEW competitors that might have emerged since the last round, and do deeper verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89bb2860-d60e-4329-8faa-11c28d7ba3d5",
  "isSidechain": false,
  "requestId": "req_011CawsFTcagCt54Q8u9CRSu",
  "type": "assistant",
  "uuid": "86029fd2-3fac-4cd6-8fe9-b2408eb5ff09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfukiQutndAFeTuQdkFZRW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 51478,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 51478,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 896
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

_source line 38 · 2026-05-12T02:14:12.630Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FzSZcnjtPjhhrAVzD3JH7P`</summary>

```json
{
  "query": "inference-time code improvement behavioral property verification LLM 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86029fd2-3fac-4cd6-8fe9-b2408eb5ff09",
  "isSidechain": false,
  "requestId": "req_011CawsFTcagCt54Q8u9CRSu",
  "type": "assistant",
  "uuid": "763b6a66-3433-4b9f-9ab5-45ad3af398d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NfukiQutndAFeTuQdkFZRW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 51478,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 92,
          "cache_read_input_tokens": 51478,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 896
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

_source line 39 · 2026-05-12T02:14:19.243Z_

<details><summary>↩ Tool result · `toolu_01FzSZcnjtPjhhrAVzD3JH7P`</summary>

```text
Web search results for query: "inference-time code improvement behavioral property verification LLM 2026 arXiv"

Links: [{"title":"ICLR 2026 Workshop: Principled Design for Trustworthy AI INFERENCE-TIME SAFETY","url":"https://arxiv.org/pdf/2603.01494"},{"title":"Inference-Time Safety for Code LLMs via Retrieval-Augmented Revision","url":"https://arxiv.org/html/2603.01494"},{"title":"A Survey on LLM Inference-Time Self-Improvement","url":"https://arxiv.org/html/2412.14352v1"},{"title":"[2603.01494] Inference-Time Safety For Code LLMs Via Retrieval-Augmented Revision","url":"https://arxiv.org/abs/2603.01494"},{"title":"Incentivizing LLMs to Self-Verify Their Answers","url":"https://arxiv.org/html/2506.01369"},{"title":"Rethinking Thinking Tokens: LLMs as Improvement Operators","url":"https://arxiv.org/html/2510.01123v1"},{"title":"[2502.12521] Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights","url":"https://arxiv.org/abs/2502.12521"},{"title":"[2503.14130] Inference-Time Intervention in Large Language Models for Reliable Requirement Verification","url":"https://arxiv.org/abs/2503.14130"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v3"},{"title":"Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights","url":"https://arxiv.org/html/2502.12521v1"}]

Based on the search results, I found several highly relevant papers on inference-time improvements for code and LLMs published on arXiv in 2026. Here are the key findings:

## Primary Result: SOSecure

The most directly relevant paper is "Inference-Time Safety For Code LLMs Via Retrieval-Augmented Revision," which presents an inference-time safety mechanism that employs retrieval-augmented generation to surface relevant security risks in generated code and retrieve related security discussions from a curated Stack Overflow knowledge base, which are then used to guide an LLM during code revision.

The key finding is that self-revision alone yields only marginal improvements, while the addition of retrieved community discussions leads to substantial gains, suggesting that the benefits stem not from prompting the model to reconsider its output, but from exposing it to concrete explanations of why certain patterns are unsafe.

The approach emphasizes interpretability through transparent safety interventions grounded in expert community explanations, robustness by allowing adaptation to evolving security practices without model retraining, and safety alignment through real-time intervention before unsafe code reaches deployment. Across real-world and benchmark datasets, the approach improves the security of LLM-generated code compared to prompting alone, while introducing no new vulnerabilities as measured by static analysis.

This paper was published on March 2, 2026, and appears to be presented at the ICLR 2026 Workshop on Principled Design for Trustworthy AI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "763b6a66-3433-4b9f-9ab5-45ad3af398d8",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "53371a44-0f5b-453e-b7c9-f1c4c56aaf51",
  "toolUseResult": {
    "query": "inference-time code improvement behavioral property verification LLM 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_018qVPABKpK5kVAx65hnHD3Z",
        "content": [
          {
            "title": "ICLR 2026 Workshop: Principled Design for Trustworthy AI INFERENCE-TIME SAFETY",
            "url": "https://arxiv.org/pdf/2603.01494"
          },
          {
            "title": "Inference-Time Safety for Code LLMs via Retrieval-Augmented Revision",
            "url": "https://arxiv.org/html/2603.01494"
          },
          {
            "title": "A Survey on LLM Inference-Time Self-Improvement",
            "url": "https://arxiv.org/html/2412.14352v1"
          },
          {
            "title": "[2603.01494] Inference-Time Safety For Code LLMs Via Retrieval-Augmented Revision",
            "url": "https://arxiv.org/abs/2603.01494"
          },
          {
            "title": "Incentivizing LLMs to Self-Verify Their Answers",
            "url": "https://arxiv.org/html/2506.01369"
          },
          {
            "title": "Rethinking Thinking Tokens: LLMs as Improvement Operators",
            "url": "https://arxiv.org/html/2510.01123v1"
          },
          {
            "title": "[2502.12521] Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights",
            "url": "https://arxiv.org/abs/2502.12521"
          },
          {
            "title": "[2503.14130] Inference-Time Intervention in Large Language Models for Reliable Requirement Verification",
            "url": "https://arxiv.org/abs/2503.14130"
          },
          {
            "title": "Trust but Verify! A Survey on Verification Design for Test-time Scaling",
            "url": "https://arxiv.org/html/2508.16665v3"
          },
          {
            "title": "Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights",
            "url": "https://arxiv.org/html/2502.12521v1"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers on inference-time improvements for code and LLMs published on arXiv in 2026. Here are the key findings:\n\n## Primary Result: SOSecure\n\nThe most directly relevant paper is \"Inference-Time Safety For Code LLMs Via Retrieval-Augmented Revision,\" which presents an inference-time safety mechanism that employs retrieval-augmented generation to surface relevant security risks in generated code and retrieve related security discussions from a curated Stack Overflow knowledge base, which are then used to guide an LLM during code revision.\n\nThe key finding is that self-revision alone yields only marginal improvements, while the addition of retrieved community discussions leads to substantial gains, suggesting that the benefits stem not from prompting the model to reconsider its output, but from exposing it to concrete explanations of why certain patterns are unsafe.\n\nThe approach emphasizes interpretability through transparent safety interventions grounded in expert community explanations, robustness by allowing adaptation to evolving security practices without model retraining, and safety alignment through real-time intervention before unsafe code reaches deployment. Across real-world and benchmark datasets, the approach improves the security of LLM-generated code compared to prompting alone, while introducing no new vulnerabilities as measured by static analysis.\n\nThis paper was published on March 2, 2026, and appears to be presented at the ICLR 2026 Workshop on Principled Design for Trustworthy AI."
    ],
    "durationSeconds": 6.610000293999998
  },
  "sourceToolAssistantUUID": "763b6a66-3433-4b9f-9ab5-45ad3af398d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-12T02:14:23.321Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TM66S6qwRTK2d1yKaQPJfv`</summary>

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
  "parentUuid": "53371a44-0f5b-453e-b7c9-f1c4c56aaf51",
  "isSidechain": false,
  "requestId": "req_011CawsGBw2xXMirJ8t78jxw",
  "type": "assistant",
  "uuid": "e14a3647-4e6c-47b3-8438-bbf9c69081aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V1C66oygwEqb18yFoafQv6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 911,
      "cache_read_input_tokens": 52374,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 52374,
          "cache_creation_input_tokens": 911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 911
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

_source line 41 · 2026-05-12T02:14:27.690Z_

<details><summary>↩ Tool result · `toolu_01TM66S6qwRTK2d1yKaQPJfv`</summary>

```text
Web search results for query: "EMNLP 2026 ARR submission deadline May 2026"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here's the information about EMNLP 2026 ARR submission deadline in May 2026:

## EMNLP 2026 ARR Submission Deadline

The ARR Submission Deadline for EMNLP 2026 is May 25, 2026.

### Important Related Deadlines:

- Reviewer registration deadline for ALL authors: May 27, 2026
- Author response and author-reviewer discussion: July 7 - July 13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026

### Important Note:

Since the ARR 2026 May cycle is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026—ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e14a3647-4e6c-47b3-8438-bbf9c69081aa",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "7ea7651e-c14f-49a3-b4ac-ad101bd7509b",
  "toolUseResult": {
    "query": "EMNLP 2026 ARR submission deadline May 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013oBJ8ogKWH996tuJUxM58E",
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
      "Based on the search results, here's the information about EMNLP 2026 ARR submission deadline in May 2026:\n\n## EMNLP 2026 ARR Submission Deadline\n\nThe ARR Submission Deadline for EMNLP 2026 is May 25, 2026.\n\n### Important Related Deadlines:\n\n- Reviewer registration deadline for ALL authors: May 27, 2026\n- Author response and author-reviewer discussion: July 7 - July 13, 2026\n- Meta review released: July 30, 2026\n- EMNLP commitment deadline: August 2, 2026\n- Notification of acceptance: August 20, 2026\n\n### Important Note:\n\nSince the ARR 2026 May cycle is aligned with both EMNLP and AACL, authors must explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026—ARR 2026 May submissions that do not select EMNLP 2026 during submission will not be able to commit to EMNLP 2026."
    ],
    "durationSeconds": 4.364335801999987
  },
  "sourceToolAssistantUUID": "e14a3647-4e6c-47b3-8438-bbf9c69081aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-12T02:14:31.532Z_

Good — venue deadline confirmed. Now let me do deeper verification on PGS's actual claims and ExeSpec's differentiation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ea7651e-c14f-49a3-b4ac-ad101bd7509b",
  "isSidechain": false,
  "requestId": "req_011CawsGp3gbE7cvR1NAeUTx",
  "type": "assistant",
  "uuid": "3a461873-698e-485d-9c72-d429afc6baf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175HTkVsW42Buq2BXLSvCaM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 977,
      "cache_read_input_tokens": 53285,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 977,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 53285,
          "cache_creation_input_tokens": 977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 977
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

_source line 43 · 2026-05-12T02:14:35.762Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TRDuasQaGSAbs4eFRGNzuP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.18315",
  "prompt": "Extract: (1) What benchmarks does PGS evaluate on? (2) What models does PGS use? (3) What are the specific pass@1 results? (4) Does PGS check inter-property consistency? (5) What is the property generation accuracy by difficulty level? (6) Does PGS evaluate on CodeContests, SWE-bench, or DebugBench? (7) What is the revision date of the latest version?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a461873-698e-485d-9c72-d429afc6baf3",
  "isSidechain": false,
  "requestId": "req_011CawsGp3gbE7cvR1NAeUTx",
  "type": "assistant",
  "uuid": "5470ecb5-14dd-41c5-9b46-85c78cde27c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175HTkVsW42Buq2BXLSvCaM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 977,
      "cache_read_input_tokens": 53285,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 977,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 53285,
          "cache_creation_input_tokens": 977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 977
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "5470ecb5-14dd-41c5-9b46-85c78cde27c4",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "ExeSpec: Execution-grounded Behavioral Specifications for Code LLMs",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Tool result

_source line 46 · 2026-05-12T02:14:42.586Z_

<details><summary>↩ Tool result · `toolu_01TRDuasQaGSAbs4eFRGNzuP`</summary>

```text
# PGS Research Paper Information

Based on the arXiv abstract provided, here's what can be determined:

**(1) Benchmarks:** Not specified in the abstract.

**(2) Models Used:** Not specified in the abstract.

**(3) Pass@1 Results:** The paper mentions "an improvement of up to 13.4% in pass@1 against other TDD-based methods" and "over 64% fix rate on problems where the model initially failed," but exact baseline numbers aren't provided in the abstract.

**(4) Inter-property Consistency:** No information provided in the abstract.

**(5) Property Generation Accuracy by Difficulty:** Not mentioned in the abstract.

**(6) CodeContests/SWE-bench/DebugBench Evaluation:** The abstract states the approach demonstrates "superior performance across diverse benchmarks" but doesn't name specific benchmark suites in the abstract text provided.

**(7) Latest Version Revision Date:** "Fri, 1 May 2026" (version 2)

**Note:** Most technical details would require accessing the full paper PDF or HTML version. The abstract focuses on the core contribution—that the Property-Generated Solver framework achieves "a bug fix rate 1.4x-1.6x higher than the strongest debugging-based approaches"—but omits specific experimental details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5470ecb5-14dd-41c5-9b46-85c78cde27c4",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "863c23cb-afc3-4dec-98c8-b82bce6949ca",
  "toolUseResult": {
    "bytes": 47303,
    "code": 200,
    "codeText": "OK",
    "result": "# PGS Research Paper Information\n\nBased on the arXiv abstract provided, here's what can be determined:\n\n**(1) Benchmarks:** Not specified in the abstract.\n\n**(2) Models Used:** Not specified in the abstract.\n\n**(3) Pass@1 Results:** The paper mentions \"an improvement of up to 13.4% in pass@1 against other TDD-based methods\" and \"over 64% fix rate on problems where the model initially failed,\" but exact baseline numbers aren't provided in the abstract.\n\n**(4) Inter-property Consistency:** No information provided in the abstract.\n\n**(5) Property Generation Accuracy by Difficulty:** Not mentioned in the abstract.\n\n**(6) CodeContests/SWE-bench/DebugBench Evaluation:** The abstract states the approach demonstrates \"superior performance across diverse benchmarks\" but doesn't name specific benchmark suites in the abstract text provided.\n\n**(7) Latest Version Revision Date:** \"Fri, 1 May 2026\" (version 2)\n\n**Note:** Most technical details would require accessing the full paper PDF or HTML version. The abstract focuses on the core contribution—that the Property-Generated Solver framework achieves \"a bug fix rate 1.4x-1.6x higher than the strongest debugging-based approaches\"—but omits specific experimental details.",
    "durationMs": 6819,
    "url": "https://arxiv.org/abs/2506.18315"
  },
  "sourceToolAssistantUUID": "5470ecb5-14dd-41c5-9b46-85c78cde27c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-12T02:14:48.000Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013zx9rLsrAKbQfCqoD96yGC`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.18315",
  "prompt": "Extract the following specific details: (1) Exact benchmarks PGS evaluates on (list all). (2) Exact models used (list all). (3) Exact pass@1 results on each benchmark. (4) Property generation accuracy by difficulty (easy/medium/hard). (5) Does PGS perform inter-property consistency checking? (6) Does PGS evaluate on CodeContests, SWE-bench, or DebugBench? (7) What is PGS's specific approach to property validation — does it validate against public tests only, or does it have additional verification? (8) What are the relative improvements over TDD methods (23.1-37.3% claimed)?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "863c23cb-afc3-4dec-98c8-b82bce6949ca",
  "isSidechain": false,
  "requestId": "req_011CawsHuk1rTZh3GjdRgkz9",
  "type": "assistant",
  "uuid": "3e2837af-dbf6-4c9a-a57f-f0a09dde601d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPo9uXGDuMfD3Pxy7t4iRa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 526,
      "cache_read_input_tokens": 54262,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 526,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 54262,
          "cache_creation_input_tokens": 526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 526
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

_source line 48 · 2026-05-12T02:14:54.376Z_

<details><summary>↩ Tool result · `toolu_013zx9rLsrAKbQfCqoD96yGC`</summary>

```text
# PGS Framework: Key Details

## (1) Benchmarks Evaluated
PGS evaluates on five benchmarks: HumanEval, MBPP, LiveCodeBench (LCB), CodeContests, and SWE-Bench.

## (2) Models Used
Six LLMs tested: DeepSeek-Coder-V2, Qwen2.5-Coder, DeepSeek-R1-32B, Qwen3-30B, DeepSeek-V3.1, and Claude-Sonnet-4.

## (3) Pass@1 Results Summary
- **HumanEval**: PGS achieves 89.0-99.1% across models
- **MBPP**: 67.6-96.5%
- **LiveCodeBench**: 34.1-83.2%
- **CodeContests**: 20.2-60.2%
- **SWE-Bench**: 11.9-70.2%

## (4) Property Generation Accuracy by Difficulty
The paper provides verification accuracy across difficulty levels: "87.0% overall (63.0% generation)" with breakdown showing Easy 93.8%, Medium 91.2%, Hard 76.5% verification rates.

## (5) Inter-Property Consistency Checking
The document does not explicitly describe inter-property consistency validation mechanisms.

## (6) CodeContests and SWE-Bench Evaluation
**Yes**, PGS evaluates on both: CodeContests (competition-level problems) and SWE-Bench (real GitHub issues).

## (7) Property Validation Approach
PGS validates properties "against public test cases" first for soundness. The framework "translates abstract properties into executable checking code" and filters "properties that contradict known ground truth."

## (8) Relative Improvements Over TDD
The paper claims PGS achieves "1.4x-1.6x higher bug fix rate than strongest debugging-based approaches," establishing state-of-the-art performance across benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e2837af-dbf6-4c9a-a57f-f0a09dde601d",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "97aa22eb-356a-451e-8387-f0408842aee7",
  "toolUseResult": {
    "bytes": 526190,
    "code": 200,
    "codeText": "OK",
    "result": "# PGS Framework: Key Details\n\n## (1) Benchmarks Evaluated\nPGS evaluates on five benchmarks: HumanEval, MBPP, LiveCodeBench (LCB), CodeContests, and SWE-Bench.\n\n## (2) Models Used\nSix LLMs tested: DeepSeek-Coder-V2, Qwen2.5-Coder, DeepSeek-R1-32B, Qwen3-30B, DeepSeek-V3.1, and Claude-Sonnet-4.\n\n## (3) Pass@1 Results Summary\n- **HumanEval**: PGS achieves 89.0-99.1% across models\n- **MBPP**: 67.6-96.5%\n- **LiveCodeBench**: 34.1-83.2%\n- **CodeContests**: 20.2-60.2%\n- **SWE-Bench**: 11.9-70.2%\n\n## (4) Property Generation Accuracy by Difficulty\nThe paper provides verification accuracy across difficulty levels: \"87.0% overall (63.0% generation)\" with breakdown showing Easy 93.8%, Medium 91.2%, Hard 76.5% verification rates.\n\n## (5) Inter-Property Consistency Checking\nThe document does not explicitly describe inter-property consistency validation mechanisms.\n\n## (6) CodeContests and SWE-Bench Evaluation\n**Yes**, PGS evaluates on both: CodeContests (competition-level problems) and SWE-Bench (real GitHub issues).\n\n## (7) Property Validation Approach\nPGS validates properties \"against public test cases\" first for soundness. The framework \"translates abstract properties into executable checking code\" and filters \"properties that contradict known ground truth.\"\n\n## (8) Relative Improvements Over TDD\nThe paper claims PGS achieves \"1.4x-1.6x higher bug fix rate than strongest debugging-based approaches,\" establishing state-of-the-art performance across benchmarks.",
    "durationMs": 6373,
    "url": "https://arxiv.org/html/2506.18315"
  },
  "sourceToolAssistantUUID": "3e2837af-dbf6-4c9a-a57f-f0a09dde601d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-12T02:15:22.324Z_

<details><summary>Logged reasoning block</summary>

```text
This is CRITICAL. The PGS paper has been REVISED (v2, May 1, 2026) and now evaluates on CodeContests AND SWE-bench! The idea claims "PGS evaluates ONLY on HumanEval/MBPP/LiveCodeBench and does NOT evaluate on CodeContests or SWE-bench" — but that appears to be based on the v1 of the paper. The v2 revision (May 2026) has expanded to include these benchmarks.

Let me verify this more carefully, because this significantly changes the novelty assessment. 

If PGS now covers CodeContests and SWE-bench, then ExeSpec's claim of "extending to benchmarks PGS does not cover" is partially invalidated. The idea does reference the May 2026 revision, so it seems aware of it, but still insists PGS doesn't evaluate on those benchmarks. I need to re-read the idea's actual claims about what PGS validates to see if there's a distinction I'm missing.

The idea reports property generation accuracy of 82.4% (easy), 62.8% (medium), and 48.9% (hard) on LiveCodeBench, but my search found PGS v2 achieving 93.8%/91.2%/76.5% on those same benchmarks — though these could be different metrics like verification rates versus generation accuracy. The idea also claims PGS doesn't cover CodeContests and SWE-bench Pro, yet the WebFetch results show PGS v2 does evaluate on these, which is a critical discrepancy I need to verify further.

The models listed in PGS v2 include very recent ones like Qwen3-30B and Claude-Sonnet-4, confirming this is a substantial revision. If PGS v2 truly covers CodeContests and SWE-bench now, ExeSpec's main differentiator of extending to uncovered benchmarks gets significantly weakened — leaving execution grounding of specs, the debugging task type, the 5-component schema with ablation, and cross-file completion as the remaining distinguishing factors. I need to dig deeper to confirm these findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97aa22eb-356a-451e-8387-f0408842aee7",
  "isSidechain": false,
  "requestId": "req_011CawsJnBsVx1jLQCBQNBpi",
  "type": "assistant",
  "uuid": "02ba5ba7-5976-45c9-98cb-be948859a9d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWuZ39eaoFTVJamV7JHgHD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 54788,
      "output_tokens": 1030,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1030,
          "cache_read_input_tokens": 54788,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 727
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

_source line 50 · 2026-05-12T02:15:22.328Z_

This is a critical finding — PGS v2 (May 2026) now evaluates on CodeContests AND SWE-bench, contradicting the idea's claim. Let me verify this further.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02ba5ba7-5976-45c9-98cb-be948859a9d1",
  "isSidechain": false,
  "requestId": "req_011CawsJnBsVx1jLQCBQNBpi",
  "type": "assistant",
  "uuid": "b491b849-11b6-49aa-b1a4-dd0f7231982f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWuZ39eaoFTVJamV7JHgHD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 54788,
      "output_tokens": 1030,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1030,
          "cache_read_input_tokens": 54788,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 727
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

_source line 51 · 2026-05-12T02:15:24.212Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015oMxv1yT5Frqji2pr1DgCK`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.18315",
  "prompt": "I need to verify: (1) Does the REVISED v2 (May 2026) version of PGS evaluate on CodeContests and SWE-bench? Please confirm by finding the exact experimental tables or sections mentioning these benchmarks. (2) What specific results does PGS achieve on CodeContests and SWE-bench? (3) Does PGS v2 use any newer models like Qwen3 or Claude Sonnet 4? (4) What is the exact title of the v2 revision? (5) Is the property generation accuracy breakdown (82.4% easy, 62.8% medium, 48.9% hard) from the v1 or v2 version?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b491b849-11b6-49aa-b1a4-dd0f7231982f",
  "isSidechain": false,
  "requestId": "req_011CawsJnBsVx1jLQCBQNBpi",
  "type": "assistant",
  "uuid": "1059464a-cb61-41ce-b54f-732934ff745f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWuZ39eaoFTVJamV7JHgHD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 54788,
      "output_tokens": 1030,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1030,
          "cache_read_input_tokens": 54788,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 727
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

_source line 52 · 2026-05-12T02:15:28.991Z_

<details><summary>↩ Tool result · `toolu_015oMxv1yT5Frqji2pr1DgCK`</summary>

```text
# PGS v2 Evaluation Summary

## (1) CodeContests and SWE-bench Evaluation

**Confirmed**: The v2 version (arXiv:2506.18315v2) evaluates on both benchmarks. Table 3 explicitly shows results for "CodeContest" and "SWE-Bench" across multiple models.

## (2) Specific Results

**CodeContests**: PGS achieves 20.2% pass@1 (DeepSeek-V2), 22.4% (Qwen2.5), 49.7% (DeepSeek-R1-32B)

**SWE-Bench**: PGS achieves 11.9% (DeepSeek-V2), 12.8% (Qwen2.5), 37.3% (DeepSeek-R1-32B), 70.2% (Claude-4)

## (3) Newer Models

**Yes**: The v2 revision incorporates Qwen3-30B, DeepSeek-V3.1, and Claude-Sonnet-4 alongside earlier models.

## (4) Exact v2 Title

"PGS: Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback" (arXiv:2506.18315v2, dated 01 May 2026)

## (5) Accuracy Breakdown Source

The property generation accuracy figures (easy/medium/hard percentages) cannot be located in the provided v2 content excerpts. These statistics do not appear in the visible sections shown.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1059464a-cb61-41ce-b54f-732934ff745f",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "b34e301b-3e80-41e4-a5f7-520ef690470c",
  "toolUseResult": {
    "bytes": 526190,
    "code": 200,
    "codeText": "OK",
    "result": "# PGS v2 Evaluation Summary\n\n## (1) CodeContests and SWE-bench Evaluation\n\n**Confirmed**: The v2 version (arXiv:2506.18315v2) evaluates on both benchmarks. Table 3 explicitly shows results for \"CodeContest\" and \"SWE-Bench\" across multiple models.\n\n## (2) Specific Results\n\n**CodeContests**: PGS achieves 20.2% pass@1 (DeepSeek-V2), 22.4% (Qwen2.5), 49.7% (DeepSeek-R1-32B)\n\n**SWE-Bench**: PGS achieves 11.9% (DeepSeek-V2), 12.8% (Qwen2.5), 37.3% (DeepSeek-R1-32B), 70.2% (Claude-4)\n\n## (3) Newer Models\n\n**Yes**: The v2 revision incorporates Qwen3-30B, DeepSeek-V3.1, and Claude-Sonnet-4 alongside earlier models.\n\n## (4) Exact v2 Title\n\n\"PGS: Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback\" (arXiv:2506.18315v2, dated 01 May 2026)\n\n## (5) Accuracy Breakdown Source\n\nThe property generation accuracy figures (easy/medium/hard percentages) cannot be located in the provided v2 content excerpts. These statistics do not appear in the visible sections shown.",
    "durationMs": 4773,
    "url": "https://arxiv.org/html/2506.18315"
  },
  "sourceToolAssistantUUID": "1059464a-cb61-41ce-b54f-732934ff745f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 53 · 2026-05-12T02:15:28.996Z_

```json
{
  "parentUuid": "b34e301b-3e80-41e4-a5f7-520ef690470c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "334a2fcd-460f-41b2-b2ee-7a2249058fd6",
  "timestamp": "2026-05-12T02:15:28.996Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 54 · 2026-05-12T02:15:47.873Z_

<details><summary>Logged reasoning block</summary>

```text
This is a CRITICAL finding. PGS v2 (May 1, 2026) now evaluates on CodeContests AND SWE-bench. The idea claims "evaluation spans four task types (generation, debugging, issue resolution, completion) on benchmarks PGS does not cover (CodeContests, SWE-bench Pro, DebugBench)" — but PGS v2 now covers CodeContests and SWE-bench.

This significantly weakens ExeSpec's novelty claim. Let me assess what differentiators remain:


Execution grounding of specs before use, debugging on DebugBench, the 5-component schema with ablation studies, cross-file completion capabilities, and the use of contamination-resistant SWE-bench Pro all appear to be areas where ExeSpec still has ground to stand on.

But I need to reconsider the core claim here — the idea states PGS doesn't cover CodeContests and SWE-bench, yet the May 2026 revision explicitly addresses this. Looking back at the landscape section, it mentions PGS validates properties against public test cases with specific accuracy numbers on LiveCodeBench, but then cuts off mid-sentence about what PGS doesn't check. I should verify whether the original claim about benchmark coverage is actually false or if I'm misreading what the idea is asserting.

Actually, rereading more carefully, the idea does explicitly state that PGS doesn't evaluate on CodeContests, SWE-bench, or debugging benchmarks. But PGS v2 uses more recent models like Qwen3-30B and Claude-Sonnet-4, making it substantially more capable than what the idea acknowledges. Even accounting for this, ExeSpec still maintains some differentiation through execution grounding and cross-spec consistency checking.

However, the core issue is that ExeSpec uses much smaller models like Qwen2.5-Coder-7B/32B compared to PGS v2's Claude-Sonnet-4, which achieves 70.2% on SWE-bench. Any meaningful comparison would need to control for model size and capability, which fundamentally undermines the novelty claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "334a2fcd-460f-41b2-b2ee-7a2249058fd6",
  "isSidechain": false,
  "requestId": "req_011CawsML93SwGs5DCMNEA3G",
  "type": "assistant",
  "uuid": "a1f19841-c493-46b8-8945-4b99eb229985",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBeJNWMG3341wYEDMddMZ9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1523,
      "cache_read_input_tokens": 55515,
      "output_tokens": 1082,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1082,
          "cache_read_input_tokens": 55515,
          "cache_creation_input_tokens": 1523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1523
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

_source line 55 · 2026-05-12T02:15:47.877Z_

This is a major finding. PGS v2 (revised May 1, 2026) now evaluates on CodeContests AND SWE-bench, directly contradicting the idea's claims. Let me search for additional verification and any other missing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1f19841-c493-46b8-8945-4b99eb229985",
  "isSidechain": false,
  "requestId": "req_011CawsML93SwGs5DCMNEA3G",
  "type": "assistant",
  "uuid": "28e96886-1306-47c6-b862-a7f1b167b203",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBeJNWMG3341wYEDMddMZ9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1523,
      "cache_read_input_tokens": 55515,
      "output_tokens": 1082,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1082,
          "cache_read_input_tokens": 55515,
          "cache_creation_input_tokens": 1523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1523
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

_source line 56 · 2026-05-12T02:15:48.422Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HDUFF5jnGa3vcfZosc3xDD`</summary>

```json
{
  "query": "SSDE structured spec-driven engineering Gherkin LLM repo-level generation arXiv 2605.02455"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28e96886-1306-47c6-b862-a7f1b167b203",
  "isSidechain": false,
  "requestId": "req_011CawsML93SwGs5DCMNEA3G",
  "type": "assistant",
  "uuid": "215ce0be-f193-4f22-b54b-298299ad577e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBeJNWMG3341wYEDMddMZ9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1523,
      "cache_read_input_tokens": 55515,
      "output_tokens": 1082,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1082,
          "cache_read_input_tokens": 55515,
          "cache_creation_input_tokens": 1523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1523
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

_source line 57 · 2026-05-12T02:15:54.974Z_

<details><summary>↩ Tool result · `toolu_01HDUFF5jnGa3vcfZosc3xDD`</summary>

```text
Web search results for query: "SSDE structured spec-driven engineering Gherkin LLM repo-level generation arXiv 2605.02455"

Links: [{"title":"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/html/2605.02455"},{"title":"[2605.02455] LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/abs/2605.02455"},{"title":"[2605.02455v1] LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/abs/2605.02455v1"},{"title":"Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants","url":"https://arxiv.org/html/2602.00180v1"},{"title":"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.","url":"https://arxiv.org/html/2601.03878v1"},{"title":"LLM-based Behaviour Driven Development for Hardware Design","url":"https://arxiv.org/html/2512.17814v2"},{"title":"LLM-as-a-Judge for Scalable Test Coverage Evaluation","url":"https://www.arxiv.org/pdf/2512.01232"},{"title":"Towards Specification-Driven LLM-Based Generation of Embedded Automotive Software","url":"https://arxiv.org/html/2411.13269v1"},{"title":"[2508.20744] From Law to Gherkin: A Human-Centred Quasi-Experiment on the Quality of LLM-Generated Behavioural Specifications from Food-Safety Regulations","url":"https://arxiv.org/abs/2508.20744"},{"title":"Acceptance Test Generation with Large Language Models: An Industrial Case Study","url":"https://arxiv.org/html/2504.07244v1"}]

Based on the search results, here's what I found about the arXiv paper 2605.02455:

## LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering

The paper proposes structured spec-driven engineering (SSDE), a paradigm that leverages structured artifacts to guide LLM generation. 

**Problem Being Addressed:**
While state-of-the-art Large Language Models excel in code generation at the function level, the output quality significantly declines when scaling to repository-level systems, and current workflows relying only on natural language prompts suffer from inherent ambiguity and a lack of verifiability.

**Proposed Solution:**
The authors argue that structured specifications as LLM inputs make high-quality, repository-level code generation a tangible goal, while at the same time offering superior verifiability, leading to significant potential for improvement.

**Research Approach:**
They investigate the feasibility of this vision through a pilot study generating Model-View-Controller (MVC) business logic for three software systems using five LLMs, and then highlight the potential, challenges, and future roadmap for SSDE.

**Input Specifications:**
The approach uses Gherkin specifications—standardized scenarios following the systematic template of Gherkin—which contain concrete examples describing expected system behavior under varying conditions that can be directly mapped to executable test cases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "215ce0be-f193-4f22-b54b-298299ad577e",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "83be0a7f-2884-4b0f-9e94-050995a05f44",
  "toolUseResult": {
    "query": "SSDE structured spec-driven engineering Gherkin LLM repo-level generation arXiv 2605.02455",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FyYtB8DDwRtkrN2hWjfQAW",
        "content": [
          {
            "title": "LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering",
            "url": "https://arxiv.org/html/2605.02455"
          },
          {
            "title": "[2605.02455] LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering",
            "url": "https://arxiv.org/abs/2605.02455"
          },
          {
            "title": "[2605.02455v1] LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering",
            "url": "https://arxiv.org/abs/2605.02455v1"
          },
          {
            "title": "Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants",
            "url": "https://arxiv.org/html/2602.00180v1"
          },
          {
            "title": "Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.",
            "url": "https://arxiv.org/html/2601.03878v1"
          },
          {
            "title": "LLM-based Behaviour Driven Development for Hardware Design",
            "url": "https://arxiv.org/html/2512.17814v2"
          },
          {
            "title": "LLM-as-a-Judge for Scalable Test Coverage Evaluation",
            "url": "https://www.arxiv.org/pdf/2512.01232"
          },
          {
            "title": "Towards Specification-Driven LLM-Based Generation of Embedded Automotive Software",
            "url": "https://arxiv.org/html/2411.13269v1"
          },
          {
            "title": "[2508.20744] From Law to Gherkin: A Human-Centred Quasi-Experiment on the Quality of LLM-Generated Behavioural Specifications from Food-Safety Regulations",
            "url": "https://arxiv.org/abs/2508.20744"
          },
          {
            "title": "Acceptance Test Generation with Large Language Models: An Industrial Case Study",
            "url": "https://arxiv.org/html/2504.07244v1"
          }
        ]
      },
      "Based on the search results, here's what I found about the arXiv paper 2605.02455:\n\n## LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering\n\nThe paper proposes structured spec-driven engineering (SSDE), a paradigm that leverages structured artifacts to guide LLM generation. \n\n**Problem Being Addressed:**\nWhile state-of-the-art Large Language Models excel in code generation at the function level, the output quality significantly declines when scaling to repository-level systems, and current workflows relying only on natural language prompts suffer from inherent ambiguity and a lack of verifiability.\n\n**Proposed Solution:**\nThe authors argue that structured specifications as LLM inputs make high-quality, repository-level code generation a tangible goal, while at the same time offering superior verifiability, leading to significant potential for improvement.\n\n**Research Approach:**\nThey investigate the feasibility of this vision through a pilot study generating Model-View-Controller (MVC) business logic for three software systems using five LLMs, and then highlight the potential, challenges, and future roadmap for SSDE.\n\n**Input Specifications:**\nThe approach uses Gherkin specifications—standardized scenarios following the systematic template of Gherkin—which contain concrete examples describing expected system behavior under varying conditions that can be directly mapped to executable test cases."
    ],
    "durationSeconds": 6.546378377000016
  },
  "sourceToolAssistantUUID": "215ce0be-f193-4f22-b54b-298299ad577e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
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
  "leafUuid": "83be0a7f-2884-4b0f-9e94-050995a05f44",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "ExeSpec: Execution-grounded Behavioral Specifications for Code LLMs",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Tool call

_source line 60 · 2026-05-12T02:15:58.772Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MT9pk1NXktqNYQUNV1PCHU`</summary>

```json
{
  "query": "FixAudit iterative test repair framework competitive code generation arXiv 2604.05560"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83be0a7f-2884-4b0f-9e94-050995a05f44",
  "isSidechain": false,
  "requestId": "req_011CawsPFSKsCeKRbfWXPrqn",
  "type": "assistant",
  "uuid": "e84b4a55-c4c1-41f0-8abe-013883501d78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HVaP9UFvachHfT7Ns7riTD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1954,
      "cache_read_input_tokens": 57038,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1954,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 57038,
          "cache_creation_input_tokens": 1954,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1954
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

_source line 61 · 2026-05-12T02:16:05.438Z_

<details><summary>↩ Tool result · `toolu_01MT9pk1NXktqNYQUNV1PCHU`</summary>

```text
Web search results for query: "FixAudit iterative test repair framework competitive code generation arXiv 2604.05560"

Links: [{"title":"An Iterative Test-and-Repair Framework for Competitive Code Generation","url":"https://arxiv.org/html/2604.05560"},{"title":"How Many Tries Does It Take? Iterative Self-Repair in LLM Code Generation Across Model Scales and Benchmarks","url":"https://arxiv.org/html/2604.10508"},{"title":"Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis","url":"https://arxiv.org/html/2604.10800v1"},{"title":"AutoCode: LLMs as Problem Setters for Competitive ...","url":"https://arxiv.org/pdf/2510.12803"},{"title":"[2604.10508] How Many Tries Does It Take? Iterative Self-Repair in LLM Code Generation Across Model Scales and Benchmarks","url":"https://arxiv.org/abs/2604.10508"},{"title":"Advancements in automated program repair: a comprehensive review | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-025-02383-9"},{"title":"The Art of Repair: Optimizing Iterative Program Repair with Instruction-Tuned Models","url":"https://arxiv.org/html/2505.02931v1"},{"title":"A Pair Programming Framework for Code Generation via ...","url":"https://arxiv.org/pdf/2409.05001"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥","url":"https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"}]

Based on the web search results, I found the paper you're looking for. Here's what FixAudit is about:

FixAudit is a framework that jointly trains one shared model with two roles: the Fixer, which repairs the current candidate, and the Auditor, which generates tests to expose its remaining bugs.

The framework approaches competitive code generation from a new perspective: starting from a single initial candidate, it iteratively improves the candidate through a targeted test-and-repair debugging cycle.

The key innovation addresses limitations in prior work: the Tester never reads any candidate code, so its tests often fail to expose implementation-specific bugs, and the Coder generates every candidate from scratch and never learns to fix a buggy program based on a failed test.

**Performance Results:**
FixAudit improves average Pass@1 by 35.1% to 36.8% and average AvgPassRatio by 7.1% to 24.5% compared to strong baselines built on the same 7B base model. The framework was evaluated on three benchmarks: APPS, CodeContests, and xCodeEval.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e84b4a55-c4c1-41f0-8abe-013883501d78",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "f8faccde-d177-42e5-ae9f-3ae2b7c3cbe6",
  "toolUseResult": {
    "query": "FixAudit iterative test repair framework competitive code generation arXiv 2604.05560",
    "results": [
      {
        "tool_use_id": "srvtoolu_019dsnvyeuucmyWGk1wKmEoM",
        "content": [
          {
            "title": "An Iterative Test-and-Repair Framework for Competitive Code Generation",
            "url": "https://arxiv.org/html/2604.05560"
          },
          {
            "title": "How Many Tries Does It Take? Iterative Self-Repair in LLM Code Generation Across Model Scales and Benchmarks",
            "url": "https://arxiv.org/html/2604.10508"
          },
          {
            "title": "Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis",
            "url": "https://arxiv.org/html/2604.10800v1"
          },
          {
            "title": "AutoCode: LLMs as Problem Setters for Competitive ...",
            "url": "https://arxiv.org/pdf/2510.12803"
          },
          {
            "title": "[2604.10508] How Many Tries Does It Take? Iterative Self-Repair in LLM Code Generation Across Model Scales and Benchmarks",
            "url": "https://arxiv.org/abs/2604.10508"
          },
          {
            "title": "Advancements in automated program repair: a comprehensive review | Knowledge and Information Systems | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10115-025-02383-9"
          },
          {
            "title": "The Art of Repair: Optimizing Iterative Program Repair with Instruction-Tuned Models",
            "url": "https://arxiv.org/html/2505.02931v1"
          },
          {
            "title": "A Pair Programming Framework for Code Generation via ...",
            "url": "https://arxiv.org/pdf/2409.05001"
          },
          {
            "title": "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications",
            "url": "https://arxiv.org/html/2506.23749v1"
          },
          {
            "title": "GitHub - YerbaPage/Awesome-Repo-Level-Code-Generation: Must-read papers on Repository-level Code Generation & Issue Resolution 🔥",
            "url": "https://github.com/YerbaPage/Awesome-Repo-Level-Code-Generation"
          }
        ]
      },
      "Based on the web search results, I found the paper you're looking for. Here's what FixAudit is about:\n\nFixAudit is a framework that jointly trains one shared model with two roles: the Fixer, which repairs the current candidate, and the Auditor, which generates tests to expose its remaining bugs.\n\nThe framework approaches competitive code generation from a new perspective: starting from a single initial candidate, it iteratively improves the candidate through a targeted test-and-repair debugging cycle.\n\nThe key innovation addresses limitations in prior work: the Tester never reads any candidate code, so its tests often fail to expose implementation-specific bugs, and the Coder generates every candidate from scratch and never learns to fix a buggy program based on a failed test.\n\n**Performance Results:**\nFixAudit improves average Pass@1 by 35.1% to 36.8% and average AvgPassRatio by 7.1% to 24.5% compared to strong baselines built on the same 7B base model. The framework was evaluated on three benchmarks: APPS, CodeContests, and xCodeEval."
    ],
    "durationSeconds": 6.662426173999993
  },
  "sourceToolAssistantUUID": "e84b4a55-c4c1-41f0-8abe-013883501d78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-12T02:16:08.149Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VBm9VzQs8sLUqKVG8wvc2u`</summary>

```json
{
  "query": "code reasoning specification verification LLM training-free May 2026 arXiv new method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8faccde-d177-42e5-ae9f-3ae2b7c3cbe6",
  "isSidechain": false,
  "requestId": "req_011CawsQ1xEgfheR8CwZwc4L",
  "type": "assistant",
  "uuid": "ecdcec84-abfe-4626-ae67-e17e1360b072",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QPo6pMDbvJiRW9ohhqvP6N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 58992,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 867,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 58992,
          "cache_creation_input_tokens": 867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 867
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

_source line 63 · 2026-05-12T02:16:16.025Z_

<details><summary>↩ Tool result · `toolu_01VBm9VzQs8sLUqKVG8wvc2u`</summary>

```text
Web search results for query: "code reasoning specification verification LLM training-free May 2026 arXiv new method"

Links: [{"title":"Towards Formal Verification of LLM-Generated Code from Natural Language Prompts","url":"https://arxiv.org/html/2507.13290v1"},{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"Improving Human Verification of LLM Reasoning through Interactive Explanation Interfaces","url":"https://arxiv.org/html/2510.22922v4"},{"title":"Towards Formal Verification of LLM-Generated Code from Natural Language Prompts","url":"https://www.arxiv.org/pdf/2507.13290v2"},{"title":"Towards Verified Code Reasoning by LLMs","url":"https://arxiv.org/html/2509.26546"},{"title":"[2604.17010] Improving LLM Code Reasoning via Semantic Equivalence Self-Play with Formal Verification","url":"https://arxiv.org/abs/2604.17010"},{"title":"AutoICE: Automatically Synthesizing Verifiable C Code via LLM-driven Evolution","url":"https://www.arxiv.org/pdf/2512.07501"},{"title":"Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning","url":"https://arxiv.org/html/2502.13820v3"},{"title":"VERINA: BENCHMARKING VERIFIABLE CODE GENER- ATION","url":"https://arxiv.org/pdf/2505.23135"},{"title":"[2507.13290] Towards Formal Verification of LLM-Generated Code from Natural Language Prompts","url":"https://arxiv.org/abs/2507.13290"}]

Based on the search results, I found several relevant papers on arXiv related to code reasoning, specification, verification, and LLM methods. Here are the key findings:

## Recent arXiv Papers on Code Verification and LLM Reasoning

**1. Formal Verification of LLM-Generated Code**

One approach explores ways to offer formal guarantees of correctness to LLM-generated code by incorporating a Formal Query Language that can represent a user's intent in a formally defined but natural language-like manner. The system, called Astrogator, is implemented for the Ansible programming language and includes an intuitive formal query language, a calculus for representing the behavior of Ansible programs, and a symbolic interpreter and unification algorithm used for verification.

**2. Verified Code Reasoning**

A method has been proposed to automatically validate answers provided by code reasoning agents by verifying their reasoning steps. This addresses the challenge that while LLM-based agents are able to tackle a wide variety of code reasoning questions, the answers are not always correct, which prevents the agent from being useful in situations where high precision is desired.

**3. Semantic Equivalence and Formal Verification**

A self-play framework for semantic equivalence in Haskell utilizes formal verification to guide adversarial training between a generator and an evaluator, leveraging Liquid Haskell proofs for validating equivalence and execution-based counterexamples for inequivalence.

**4. Verifiable Code Generation Benchmark**

LLMs have the potential to jointly generate code, formal specifications, and formal proofs of alignment between code and specifications, offering higher levels of correctness assurance in what is known as verifiable code generation.

These papers represent recent advances in training-free and verification-based approaches to ensuring code correctness in LLM-generated code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecdcec84-abfe-4626-ae67-e17e1360b072",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "ff51dc53-d684-4d3c-9709-952b0f3f1a06",
  "toolUseResult": {
    "query": "code reasoning specification verification LLM training-free May 2026 arXiv new method",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Jkh41RdFbqHmqy6aN6frcT",
        "content": [
          {
            "title": "Towards Formal Verification of LLM-Generated Code from Natural Language Prompts",
            "url": "https://arxiv.org/html/2507.13290v1"
          },
          {
            "title": "Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models",
            "url": "https://arxiv.org/html/2504.04372"
          },
          {
            "title": "Improving Human Verification of LLM Reasoning through Interactive Explanation Interfaces",
            "url": "https://arxiv.org/html/2510.22922v4"
          },
          {
            "title": "Towards Formal Verification of LLM-Generated Code from Natural Language Prompts",
            "url": "https://www.arxiv.org/pdf/2507.13290v2"
          },
          {
            "title": "Towards Verified Code Reasoning by LLMs",
            "url": "https://arxiv.org/html/2509.26546"
          },
          {
            "title": "[2604.17010] Improving LLM Code Reasoning via Semantic Equivalence Self-Play with Formal Verification",
            "url": "https://arxiv.org/abs/2604.17010"
          },
          {
            "title": "AutoICE: Automatically Synthesizing Verifiable C Code via LLM-driven Evolution",
            "url": "https://www.arxiv.org/pdf/2512.07501"
          },
          {
            "title": "Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning",
            "url": "https://arxiv.org/html/2502.13820v3"
          },
          {
            "title": "VERINA: BENCHMARKING VERIFIABLE CODE GENER- ATION",
            "url": "https://arxiv.org/pdf/2505.23135"
          },
          {
            "title": "[2507.13290] Towards Formal Verification of LLM-Generated Code from Natural Language Prompts",
            "url": "https://arxiv.org/abs/2507.13290"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on arXiv related to code reasoning, specification, verification, and LLM methods. Here are the key findings:\n\n## Recent arXiv Papers on Code Verification and LLM Reasoning\n\n**1. Formal Verification of LLM-Generated Code**\n\nOne approach explores ways to offer formal guarantees of correctness to LLM-generated code by incorporating a Formal Query Language that can represent a user's intent in a formally defined but natural language-like manner. The system, called Astrogator, is implemented for the Ansible programming language and includes an intuitive formal query language, a calculus for representing the behavior of Ansible programs, and a symbolic interpreter and unification algorithm used for verification.\n\n**2. Verified Code Reasoning**\n\nA method has been proposed to automatically validate answers provided by code reasoning agents by verifying their reasoning steps. This addresses the challenge that while LLM-based agents are able to tackle a wide variety of code reasoning questions, the answers are not always correct, which prevents the agent from being useful in situations where high precision is desired.\n\n**3. Semantic Equivalence and Formal Verification**\n\nA self-play framework for semantic equivalence in Haskell utilizes formal verification to guide adversarial training between a generator and an evaluator, leveraging Liquid Haskell proofs for validating equivalence and execution-based counterexamples for inequivalence.\n\n**4. Verifiable Code Generation Benchmark**\n\nLLMs have the potential to jointly generate code, formal specifications, and formal proofs of alignment between code and specifications, offering higher levels of correctness assurance in what is known as verifiable code generation.\n\nThese papers represent recent advances in training-free and verification-based approaches to ensuring code correctness in LLM-generated code."
    ],
    "durationSeconds": 7.8707681739999975
  },
  "sourceToolAssistantUUID": "ecdcec84-abfe-4626-ae67-e17e1360b072",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-12T02:16:19.001Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NwBqCyfZXgCgErK9wiKguW`</summary>

```json
{
  "query": "\"test time scaling\" code generation repair debugging 2026 arXiv property specification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff51dc53-d684-4d3c-9709-952b0f3f1a06",
  "isSidechain": false,
  "requestId": "req_011CawsQoFHQ8k9ynu4d23KD",
  "type": "assistant",
  "uuid": "46a5ff4f-b7f3-41e2-82c6-0cccfdbeb57f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011w4hqyqSBEsvsuyKzVFPSU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 988,
      "cache_read_input_tokens": 59859,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 59859,
          "cache_creation_input_tokens": 988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 988
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

_source line 65 · 2026-05-12T02:16:26.073Z_

<details><summary>↩ Tool result · `toolu_01NwBqCyfZXgCgErK9wiKguW`</summary>

```text
Web search results for query: ""test time scaling" code generation repair debugging 2026 arXiv property specification"

Links: [{"title":"𝑆^∗: Test Time Scaling for Code Generation","url":"https://arxiv.org/html/2502.14382v1"},{"title":"Scaling Test-Driven Code Generation from Functions to Classes: An Empirical Study","url":"https://arxiv.org/html/2602.03557v1"},{"title":"An Iterative Test-and-Repair Framework for Competitive Code Generation","url":"https://arxiv.org/html/2604.05560"},{"title":"\\name: Scaling LLMs with Reasoning Data and Test-Time Compute for Accurate RTL Code Generation","url":"https://arxiv.org/html/2506.05566v1"},{"title":"[2602.03557] Scaling Test-Driven Code Generation from Functions to Classes: An Empirical Study","url":"https://arxiv.org/abs/2602.03557"},{"title":"S*: Test-Time Scaling for Code Generation","url":"https://novasky-ai.github.io/posts/S*/"},{"title":"Learning to Generate Unit Tests for Automated Debugging","url":"https://arxiv.org/html/2502.01619"},{"title":"EGSS: Entropy-guided Stepwise Scaling for Reliable Software Engineering","url":"https://arxiv.org/html/2602.05242"},{"title":"From Code to Correctness: Closing the Last Mile of Code Generation with Hierarchical Debugging","url":"https://arxiv.org/html/2410.01215"},{"title":"[2502.14382] S*: Test Time Scaling for Code Generation","url":"https://arxiv.org/abs/2502.14382"}]

The search has returned several relevant results about test-time scaling for code generation and related topics from recent arXiv papers. Here are the key findings:

## Main Results

**S*: Test Time Scaling for Code Generation**

Test-time compute for LLMs shows promise in code generation, and S* is the first hybrid test-time scaling framework that substantially improves the coverage and selection accuracy of generated code. The approach explores iterative debugging with model-generated test cases and finds that iteratively debugging from test execution feedback improves performance, even for reasoning models.

**Scaling Test-Driven Code Generation from Functions to Classes**

Test-driven development (TDD) has been adopted to improve LLM-based code generation by using tests as executable specifications, and the approach scales test-driven code generation from functions to classes via an iterative TDD framework that analyzes intra-class method dependencies and incrementally implements each method under method-level public tests with reflection-style execution feedback.

**Competitive Code Generation with Test-and-Repair**

FixAudit proposes a new perspective for competitive code generation by treating it as a continuous, targeted test-and-repair debugging process centered on the current candidate solution.

**Additional Related Work**

Other relevant papers in the 2026 arXiv submissions include work on unit test generation for automated debugging, RTL code generation with reasoning data, and entropy-guided stepwise scaling for software engineering—all addressing code quality through testing, repair, and property specification verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46a5ff4f-b7f3-41e2-82c6-0cccfdbeb57f",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "b637ba40-9811-42a4-8244-ef4e469a75f7",
  "toolUseResult": {
    "query": "\"test time scaling\" code generation repair debugging 2026 arXiv property specification",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NphqTELQyKXwPgecHxj2FB",
        "content": [
          {
            "title": "𝑆^∗: Test Time Scaling for Code Generation",
            "url": "https://arxiv.org/html/2502.14382v1"
          },
          {
            "title": "Scaling Test-Driven Code Generation from Functions to Classes: An Empirical Study",
            "url": "https://arxiv.org/html/2602.03557v1"
          },
          {
            "title": "An Iterative Test-and-Repair Framework for Competitive Code Generation",
            "url": "https://arxiv.org/html/2604.05560"
          },
          {
            "title": "\\name: Scaling LLMs with Reasoning Data and Test-Time Compute for Accurate RTL Code Generation",
            "url": "https://arxiv.org/html/2506.05566v1"
          },
          {
            "title": "[2602.03557] Scaling Test-Driven Code Generation from Functions to Classes: An Empirical Study",
            "url": "https://arxiv.org/abs/2602.03557"
          },
          {
            "title": "S*: Test-Time Scaling for Code Generation",
            "url": "https://novasky-ai.github.io/posts/S*/"
          },
          {
            "title": "Learning to Generate Unit Tests for Automated Debugging",
            "url": "https://arxiv.org/html/2502.01619"
          },
          {
            "title": "EGSS: Entropy-guided Stepwise Scaling for Reliable Software Engineering",
            "url": "https://arxiv.org/html/2602.05242"
          },
          {
            "title": "From Code to Correctness: Closing the Last Mile of Code Generation with Hierarchical Debugging",
            "url": "https://arxiv.org/html/2410.01215"
          },
          {
            "title": "[2502.14382] S*: Test Time Scaling for Code Generation",
            "url": "https://arxiv.org/abs/2502.14382"
          }
        ]
      },
      "The search has returned several relevant results about test-time scaling for code generation and related topics from recent arXiv papers. Here are the key findings:\n\n## Main Results\n\n**S*: Test Time Scaling for Code Generation**\n\nTest-time compute for LLMs shows promise in code generation, and S* is the first hybrid test-time scaling framework that substantially improves the coverage and selection accuracy of generated code. The approach explores iterative debugging with model-generated test cases and finds that iteratively debugging from test execution feedback improves performance, even for reasoning models.\n\n**Scaling Test-Driven Code Generation from Functions to Classes**\n\nTest-driven development (TDD) has been adopted to improve LLM-based code generation by using tests as executable specifications, and the approach scales test-driven code generation from functions to classes via an iterative TDD framework that analyzes intra-class method dependencies and incrementally implements each method under method-level public tests with reflection-style execution feedback.\n\n**Competitive Code Generation with Test-and-Repair**\n\nFixAudit proposes a new perspective for competitive code generation by treating it as a continuous, targeted test-and-repair debugging process centered on the current candidate solution.\n\n**Additional Related Work**\n\nOther relevant papers in the 2026 arXiv submissions include work on unit test generation for automated debugging, RTL code generation with reasoning data, and entropy-guided stepwise scaling for software engineering—all addressing code quality through testing, repair, and property specification verification."
    ],
    "durationSeconds": 7.068356024000008
  },
  "sourceToolAssistantUUID": "46a5ff4f-b7f3-41e2-82c6-0cccfdbeb57f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-12T02:16:28.761Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BpPY3jA5fY85ZjQByEEiWD`</summary>

```json
{
  "query": "Self-Spec model-authored specifications LLM code generation Agents4Science 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b637ba40-9811-42a4-8244-ef4e469a75f7",
  "isSidechain": false,
  "requestId": "req_011CawsRYH9YzdgjEUnLnUny",
  "type": "assistant",
  "uuid": "151404ed-d231-4d52-82e4-578de9c0dc6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWKyyUUzvVxUbcpdJ6Xkjh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 60847,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 851,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 60847,
          "cache_creation_input_tokens": 851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 851
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

_source line 67 · 2026-05-12T02:16:36.413Z_

<details><summary>↩ Tool result · `toolu_01BpPY3jA5fY85ZjQByEEiWD`</summary>

```text
Web search results for query: "Self-Spec model-authored specifications LLM code generation Agents4Science 2025"

Links: [{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation | OpenReview","url":"https://openreview.net/forum?id=6pr7BUGkLp"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering","url":"https://arxiv.org/html/2605.02455"},{"title":"SpecGen: Automated Generation of Formal Program Specifications via Large Language Models | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering","url":"https://dl.acm.org/doi/10.1109/ICSE55347.2025.00129"},{"title":"[2401.08807] SpecGen: Automated Generation of Formal Program Specifications via Large Language Models","url":"https://arxiv.org/abs/2401.08807"},{"title":"Spec2RTL-Agent: Automated Hardware Code Generation from Complex Specifications Using LLM Agent Systems","url":"https://arxiv.org/html/2506.13905v1"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.","url":"https://arxiv.org/html/2601.03878v1"},{"title":"Spec-driven development: Unpacking one of 2025’s key new AI-assisted engineering practices | Thoughtworks United States","url":"https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices"},{"title":"A Survey on Large Language Models in Scientific Discovery","url":"https://aclanthology.org/2025.emnlp-main.895.pdf"}]

Based on the web search results, here's what I found about Self-Spec and related research:

## Self-Spec: Model-Authored Specifications

Self-Spec investigates whether large language models (LLMs) code more reliably when they first author a task-specific specification language and then implement strictly from that spec.

### How It Works

Self-Spec is a lightweight, deterministic (T=0) orchestration that prompts a model to: (i) design a compact spec schema it prefers, (ii) instantiate that schema from a problem's docstring and signature, (iii) resolve ambiguities via a minimal Q&A loop, and (iv) generate code only from the confirmed spec.

### Key Insight

The intuition is distributional: a self-authored spec better aligns with a model's internal representational bias, reducing docstring drift and format/edge-case mistakes.

### Research Results

On HumanEval (pass@1, single sample), Self-Spec improves over direct NL→code for stronger models: GPT-4o 87%→92% (+5) and Claude 3.7 92%→94% (+2); Claude 3.5 dips 90%→89% (-1).

### Publication

The research was published at the Agents4Science 2025 Conference in October 2025. This is the first systematic study that lets an LLM design its own spec language for coding. The method is simple (no finetuning), model-agnostic (each model chooses its spec shape), and practical (assumptions are made explicit).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "151404ed-d231-4d52-82e4-578de9c0dc6b",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "f81ae629-df96-44d8-8d72-7fb01e1ec8fd",
  "toolUseResult": {
    "query": "Self-Spec model-authored specifications LLM code generation Agents4Science 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_017hibbnewZbtDMmfQStuFkw",
        "content": [
          {
            "title": "Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation | OpenReview",
            "url": "https://openreview.net/forum?id=6pr7BUGkLp"
          },
          {
            "title": "Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation",
            "url": "https://openreview.net/pdf?id=6pr7BUGkLp"
          },
          {
            "title": "LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering",
            "url": "https://arxiv.org/html/2605.02455"
          },
          {
            "title": "SpecGen: Automated Generation of Formal Program Specifications via Large Language Models | Proceedings of the IEEE/ACM 47th International Conference on Software Engineering",
            "url": "https://dl.acm.org/doi/10.1109/ICSE55347.2025.00129"
          },
          {
            "title": "[2401.08807] SpecGen: Automated Generation of Formal Program Specifications via Large Language Models",
            "url": "https://arxiv.org/abs/2401.08807"
          },
          {
            "title": "Spec2RTL-Agent: Automated Hardware Code Generation from Complex Specifications Using LLM Agent Systems",
            "url": "https://arxiv.org/html/2506.13905v1"
          },
          {
            "title": "GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub",
            "url": "https://github.com/iSEngLab/AwesomeLLM4SE"
          },
          {
            "title": "Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design**This paper is a Stage 1 Registered Report. The study protocol and analysis plan were peer reviewed and accepted at SANER 2026 with a Continuity Acceptance (CA) score for Stage 2.",
            "url": "https://arxiv.org/html/2601.03878v1"
          },
          {
            "title": "Spec-driven development: Unpacking one of 2025’s key new AI-assisted engineering practices | Thoughtworks United States",
            "url": "https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices"
          },
          {
            "title": "A Survey on Large Language Models in Scientific Discovery",
            "url": "https://aclanthology.org/2025.emnlp-main.895.pdf"
          }
        ]
      },
      "Based on the web search results, here's what I found about Self-Spec and related research:\n\n## Self-Spec: Model-Authored Specifications\n\nSelf-Spec investigates whether large language models (LLMs) code more reliably when they first author a task-specific specification language and then implement strictly from that spec.\n\n### How It Works\n\nSelf-Spec is a lightweight, deterministic (T=0) orchestration that prompts a model to: (i) design a compact spec schema it prefers, (ii) instantiate that schema from a problem's docstring and signature, (iii) resolve ambiguities via a minimal Q&A loop, and (iv) generate code only from the confirmed spec.\n\n### Key Insight\n\nThe intuition is distributional: a self-authored spec better aligns with a model's internal representational bias, reducing docstring drift and format/edge-case mistakes.\n\n### Research Results\n\nOn HumanEval (pass@1, single sample), Self-Spec improves over direct NL→code for stronger models: GPT-4o 87%→92% (+5) and Claude 3.7 92%→94% (+2); Claude 3.5 dips 90%→89% (-1).\n\n### Publication\n\nThe research was published at the Agents4Science 2025 Conference in October 2025. This is the first systematic study that lets an LLM design its own spec language for coding. The method is simple (no finetuning), model-agnostic (each model chooses its spec shape), and practical (assumptions are made explicit)."
    ],
    "durationSeconds": 7.649051204999996
  },
  "sourceToolAssistantUUID": "151404ed-d231-4d52-82e4-578de9c0dc6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
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
  "leafUuid": "f81ae629-df96-44d8-8d72-7fb01e1ec8fd",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "ExeSpec: Execution-grounded Behavioral Specifications for Code LLMs",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Assistant

_source line 70 · 2026-05-12T02:16:39.479Z_

Now let me check for any additional very recent competitors the idea might be missing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f81ae629-df96-44d8-8d72-7fb01e1ec8fd",
  "isSidechain": false,
  "requestId": "req_011CawsSJNX3B5vqzeCUDnmn",
  "type": "assistant",
  "uuid": "7e0e5586-864a-4cd8-8c47-f26c41dc69ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUA6tA3sR2m5qwK6WnXfyr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 61698,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1063,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 61698,
          "cache_creation_input_tokens": 1063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1063
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

_source line 71 · 2026-05-12T02:16:40.215Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0185PDNVsx42J9afe7FSefM4`</summary>

```json
{
  "query": "code LLM structured intermediate reasoning debugging repair specification 2026 ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e0e5586-864a-4cd8-8c47-f26c41dc69ac",
  "isSidechain": false,
  "requestId": "req_011CawsSJNX3B5vqzeCUDnmn",
  "type": "assistant",
  "uuid": "4b9fe615-ddda-457a-beb6-343f6269d899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUA6tA3sR2m5qwK6WnXfyr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 61698,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1063,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 61698,
          "cache_creation_input_tokens": 1063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1063
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

_source line 72 · 2026-05-12T02:16:48.051Z_

<details><summary>↩ Tool result · `toolu_0185PDNVsx42J9afe7FSefM4`</summary>

```text
Web search results for query: "code LLM structured intermediate reasoning debugging repair specification 2026 ACL EMNLP"

Links: [{"title":"A Survey on Code-Enhanced Reasoning and ...","url":"https://aclanthology.org/2025.emnlp-main.130.pdf"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"NL-Debugging: Exploiting Natural Language as an ...","url":"https://aclanthology.org/2025.emnlp-main.80.pdf"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Code Execution as Grounded Supervision for LLM ...","url":"https://aclanthology.org/2025.emnlp-main.1260.pdf"},{"title":"Distilling Multi-Agent Coding into a Single Small LLM","url":"https://aclanthology.org/2026.findings-eacl.346.pdf"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Usage of Large Language Model for Code Generation Tasks: A Review | SN Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s42979-025-04241-5"},{"title":"S∗: Test Time Scaling for Code Generation","url":"https://aclanthology.org/2025.findings-emnlp.865.pdf"},{"title":"Weaver: Interweaving SQL and LLM for Table Reasoning","url":"https://aclanthology.org/2025.emnlp-main.1436.pdf"}]

Based on the web search results, I found several relevant papers related to your query about code, LLMs, structured intermediate reasoning, debugging, and repair. Here are the key findings:

## Related Papers Found:

**NL-Debugging (EMNLP 2025):** One paper focuses on exploiting natural language for debugging by expanding and elaborating on problematic steps in greater detail to explain correct reasoning. This approach involves generating natural language sketches of solutions and then refining them to fix issues.

**Code-Enhanced Reasoning Survey (EMNLP 2025):** A survey titled "Code to Think, Think to Code" examines code-enhanced reasoning and various applications.

**MapCoder-Lite (ACL 2026):** A paper presented at the March 24-29, 2026 ACL conference discusses multi-agent coding systems, where given a natural language problem, a retrieval agent fetches relevant algorithmic knowledge, a planning agent generates a solution plan, the coding agent implements the plan, and the debugging agent iteratively refines the code based on test outcomes.

**Test Time Scaling for Code Generation (EMNLP 2025):** An approach called S* enhances parallel samples through iterative debugging, with each sample tested using public test cases executed via an interpreter, using outputs and error messages to guide development.

## General Trends:

Chain-of-Thought prompting guides LLMs to break down complex problems into sequential, intermediate reasoning steps, with this explicit articulation of thought process before generating final code helping models manage intricate logic.

Would you like me to search for more specific papers or information about any of these approaches?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b9fe615-ddda-457a-beb6-343f6269d899",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "8c73531f-ae75-408d-941f-ba4d8af3f192",
  "toolUseResult": {
    "query": "code LLM structured intermediate reasoning debugging repair specification 2026 ACL EMNLP",
    "results": [
      {
        "tool_use_id": "srvtoolu_014cQa4iYvGmWBavbHQ5ndNE",
        "content": [
          {
            "title": "A Survey on Code-Enhanced Reasoning and ...",
            "url": "https://aclanthology.org/2025.emnlp-main.130.pdf"
          },
          {
            "title": "GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub",
            "url": "https://github.com/acl-org/emnlp-2026"
          },
          {
            "title": "NL-Debugging: Exploiting Natural Language as an ...",
            "url": "https://aclanthology.org/2025.emnlp-main.80.pdf"
          },
          {
            "title": "FAQ - EMNLP 2026",
            "url": "https://2026.emnlp.org/faq/"
          },
          {
            "title": "Code Execution as Grounded Supervision for LLM ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1260.pdf"
          },
          {
            "title": "Distilling Multi-Agent Coding into a Single Small LLM",
            "url": "https://aclanthology.org/2026.findings-eacl.346.pdf"
          },
          {
            "title": "GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub",
            "url": "https://github.com/iSEngLab/AwesomeLLM4APR"
          },
          {
            "title": "Usage of Large Language Model for Code Generation Tasks: A Review | SN Computer Science | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s42979-025-04241-5"
          },
          {
            "title": "S∗: Test Time Scaling for Code Generation",
            "url": "https://aclanthology.org/2025.findings-emnlp.865.pdf"
          },
          {
            "title": "Weaver: Interweaving SQL and LLM for Table Reasoning",
            "url": "https://aclanthology.org/2025.emnlp-main.1436.pdf"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers related to your query about code, LLMs, structured intermediate reasoning, debugging, and repair. Here are the key findings:\n\n## Related Papers Found:\n\n**NL-Debugging (EMNLP 2025):** One paper focuses on exploiting natural language for debugging by expanding and elaborating on problematic steps in greater detail to explain correct reasoning. This approach involves generating natural language sketches of solutions and then refining them to fix issues.\n\n**Code-Enhanced Reasoning Survey (EMNLP 2025):** A survey titled \"Code to Think, Think to Code\" examines code-enhanced reasoning and various applications.\n\n**MapCoder-Lite (ACL 2026):** A paper presented at the March 24-29, 2026 ACL conference discusses multi-agent coding systems, where given a natural language problem, a retrieval agent fetches relevant algorithmic knowledge, a planning agent generates a solution plan, the coding agent implements the plan, and the debugging agent iteratively refines the code based on test outcomes.\n\n**Test Time Scaling for Code Generation (EMNLP 2025):** An approach called S* enhances parallel samples through iterative debugging, with each sample tested using public test cases executed via an interpreter, using outputs and error messages to guide development.\n\n## General Trends:\n\nChain-of-Thought prompting guides LLMs to break down complex problems into sequential, intermediate reasoning steps, with this explicit articulation of thought process before generating final code helping models manage intricate logic.\n\nWould you like me to search for more specific papers or information about any of these approaches?"
    ],
    "durationSeconds": 7.831202935000008
  },
  "sourceToolAssistantUUID": "4b9fe615-ddda-457a-beb6-343f6269d899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-12T02:16:50.672Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013qpDcMqbCTyzJeJMdBdU7u`</summary>

```json
{
  "query": "Clover closed-loop verifiable code generation specification LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c73531f-ae75-408d-941f-ba4d8af3f192",
  "isSidechain": false,
  "requestId": "req_011CawsTAFtQSbamFWXwkpQq",
  "type": "assistant",
  "uuid": "a677097e-2889-410a-8f4e-c1cac092ba64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSemdVVfK7tGF1Z9gcexEg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 62761,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 990,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 62761,
          "cache_creation_input_tokens": 990,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 990
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

_source line 74 · 2026-05-12T02:16:57.182Z_

<details><summary>↩ Tool result · `toolu_013qpDcMqbCTyzJeJMdBdU7u`</summary>

```text
Web search results for query: "Clover closed-loop verifiable code generation specification LLM 2024 2025"

Links: [{"title":"[2310.17807] Clover: Closed-Loop Verifiable Code Generation","url":"https://arxiv.org/abs/2310.17807"},{"title":"Clover: Closed-Loop Verifiable Code Generation | OpenReview","url":"https://openreview.net/forum?id=oSuVEv4X7w"},{"title":"GitHub - ChuyueSun/Clover: Clover: Closed-Loop Verifiable Code Generation · GitHub","url":"https://github.com/ChuyueSun/Clover"},{"title":"Clover: Closed-Loop Verifiable Code Generation Chuyue Sun1⋆ Ying Sheng1∗","url":"https://theory.stanford.edu/~barrett/pubs/SSP+24.pdf"},{"title":"Clover: Closed-Loop Verifiable Code Generation | SAIL Blog","url":"http://ai.stanford.edu/blog/clover/"},{"title":"Clover: Closed-Loop Verifiable Code Generation","url":"https://arxiv.org/html/2310.17807v4"},{"title":"Clover: Closed-Loop Verifiable Code Generation | AI Verification","url":"https://dl.acm.org/doi/10.1007/978-3-031-65112-0_7"},{"title":"CLOVER: Closed-Loop Verifiable Code Generation (Dafny 2024) - POPL 2024","url":"https://popl24.sigplan.org/details/dafny-2024-papers/1/CLOVER-Closed-Loop-Verifiable-Code-Generation"},{"title":"CLOVER: CLOSED-LOOP VERIFIABLE CODE GENERATION Anonymous authors","url":"https://openreview.net/pdf?id=oSuVEv4X7w"},{"title":"Clover: Closed-Loop Verifiable Code Generation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-65112-0_7"}]

Based on the search results, here's information about Clover - Closed-Loop Verifiable Code Generation:

## Overview

Clover is a paradigm for Closed-Loop Verifiable Code Generation that uses consistency checking to provide a strong filter for incorrect code. At the core of Clover lies a checker that performs consistency checks among code, docstrings, and formal annotations, implemented using a novel integration of formal verification tools and large language models.

## Key Methodology

Clover reduces correctness checking to the more accessible problem of consistency checking and safeguards LLM-powered code generation from potentially costly mistakes. One key idea used to check consistency is reconstruction testing, where given code, docstring, and annotations as input, the system tries to reconstruct a single component from another, then checks if the reconstructed result is equivalent to the original.

## Empirical Results

The research was evaluated on a hand-designed dataset (CloverBench) featuring annotated Dafny programs, showing that LLMs are reasonably successful at automatically generating formal specifications, with the consistency checker achieving a promising acceptance rate (up to 87%) for correct instances while maintaining zero tolerance for adversarial incorrect ones (no false positives).

## Publication History

The paper was initially submitted in October 2023 with subsequent versions released through June and November 2024. The work has been presented at venues including POPL 2024 and published in academic proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a677097e-2889-410a-8f4e-c1cac092ba64",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "2d00557e-172d-445e-9b03-eb75e9f11ac0",
  "toolUseResult": {
    "query": "Clover closed-loop verifiable code generation specification LLM 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_013UmFy7wbGxUBMQsPLFqxRh",
        "content": [
          {
            "title": "[2310.17807] Clover: Closed-Loop Verifiable Code Generation",
            "url": "https://arxiv.org/abs/2310.17807"
          },
          {
            "title": "Clover: Closed-Loop Verifiable Code Generation | OpenReview",
            "url": "https://openreview.net/forum?id=oSuVEv4X7w"
          },
          {
            "title": "GitHub - ChuyueSun/Clover: Clover: Closed-Loop Verifiable Code Generation · GitHub",
            "url": "https://github.com/ChuyueSun/Clover"
          },
          {
            "title": "Clover: Closed-Loop Verifiable Code Generation Chuyue Sun1⋆ Ying Sheng1∗",
            "url": "https://theory.stanford.edu/~barrett/pubs/SSP+24.pdf"
          },
          {
            "title": "Clover: Closed-Loop Verifiable Code Generation | SAIL Blog",
            "url": "http://ai.stanford.edu/blog/clover/"
          },
          {
            "title": "Clover: Closed-Loop Verifiable Code Generation",
            "url": "https://arxiv.org/html/2310.17807v4"
          },
          {
            "title": "Clover: Closed-Loop Verifiable Code Generation | AI Verification",
            "url": "https://dl.acm.org/doi/10.1007/978-3-031-65112-0_7"
          },
          {
            "title": "CLOVER: Closed-Loop Verifiable Code Generation (Dafny 2024) - POPL 2024",
            "url": "https://popl24.sigplan.org/details/dafny-2024-papers/1/CLOVER-Closed-Loop-Verifiable-Code-Generation"
          },
          {
            "title": "CLOVER: CLOSED-LOOP VERIFIABLE CODE GENERATION Anonymous authors",
            "url": "https://openreview.net/pdf?id=oSuVEv4X7w"
          },
          {
            "title": "Clover: Closed-Loop Verifiable Code Generation | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-031-65112-0_7"
          }
        ]
      },
      "Based on the search results, here's information about Clover - Closed-Loop Verifiable Code Generation:\n\n## Overview\n\nClover is a paradigm for Closed-Loop Verifiable Code Generation that uses consistency checking to provide a strong filter for incorrect code. At the core of Clover lies a checker that performs consistency checks among code, docstrings, and formal annotations, implemented using a novel integration of formal verification tools and large language models.\n\n## Key Methodology\n\nClover reduces correctness checking to the more accessible problem of consistency checking and safeguards LLM-powered code generation from potentially costly mistakes. One key idea used to check consistency is reconstruction testing, where given code, docstring, and annotations as input, the system tries to reconstruct a single component from another, then checks if the reconstructed result is equivalent to the original.\n\n## Empirical Results\n\nThe research was evaluated on a hand-designed dataset (CloverBench) featuring annotated Dafny programs, showing that LLMs are reasonably successful at automatically generating formal specifications, with the consistency checker achieving a promising acceptance rate (up to 87%) for correct instances while maintaining zero tolerance for adversarial incorrect ones (no false positives).\n\n## Publication History\n\nThe paper was initially submitted in October 2023 with subsequent versions released through June and November 2024. The work has been presented at venues including POPL 2024 and published in academic proceedings."
    ],
    "durationSeconds": 6.505768417999963
  },
  "sourceToolAssistantUUID": "a677097e-2889-410a-8f4e-c1cac092ba64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-12T02:18:01.645Z_

<details><summary>Logged reasoning block</summary>

```text
Clover is interesting but uses formal verification (Dafny), not the same as ExeSpec's approach. It's cited in the broad field but not a direct competitor.

Now let me check a few more things before forming my verdict:

1. PGS v2 now covers CodeContests and SWE-bench — this is a critical finding
2. Need to verify if there are any other very recent competitors
3. Need to assess the overall novelty given PGS v2's expanded scope

Let me also check the idea's property accuracy numbers against what PGS v2 reports.


The numbers don't match up — the idea cites PGS v1 results (82.4% easy, 62.8% medium, 48.9% hard on LiveCodeBench), but my search found v2 reports different metrics entirely (93.8% easy, 91.2% medium, 76.5% hard verification rates). These appear to be different measurement types, suggesting the idea is working from older v1 data while v2 has evolved significantly.

Now I'm formulating my assessment. The major shift here is that PGS is finally properly cited and included as a baseline after multiple rounds of flagging — that's genuine progress. However, there's a critical factual error: the idea claims PGS doesn't evaluate on CodeContests or SWE-bench, but the May 2026 v2 revision actually does cover these benchmarks. Since the idea explicitly acknowledges the v2 revision, this misrepresentation of its scope significantly undermines the novelty argument.

The other additions are solid — NL-Debugging, ContractEval, StoryCoder, FixAudit, and the other papers are now cited, and SWE-bench Pro as a co-primary benchmark addresses contamination concerns. But once I correct for PGS v2's actual capabilities, the remaining differentiator is really just the execution grounding of specs before use, where PGS validates against public tests for soundness but doesn't enforce cross-spec consistency.

Looking at what's left, ExeSpec still has meaningful ground to stand on: the DebugBench evaluation, the five-component decomposition with ablation studies, cross-file completion on CrossCodeEval and RepoBench, the use of SWE-bench Pro specifically, and the structured violation reports with component attribution. Even after accounting for PGS v2, the core claim about execution grounding of specs themselves holds up, though the benchmark expansion argument needs refinement.

The real issue is that since PGS v2 already covers CodeContests and SWE-bench, the paper's strength now depends entirely on whether ExeSpec actually outperforms PGS on those shared benchmarks—the narrative has to shift from "we're extending PGS to new domains" to "we're improving PGS through execution grounding and decomposition on overlapping tasks, plus adding debugging and completion capabilities." It's a fixable problem since the experimental design already includes PGS as a baseline, but the factual error about PGS v2's coverage needs to be corrected.

Looking at the overall assessment, I'd rate novelty at 3/5 since the execution-grounding approach is meaningful but incremental relative to PGS v2's expanded scope, and the component decomposition plus debugging extension, while valid, aren't particularly groundbreaking. Feasibility sits around 3.5/5—the timeline is tight with manual annotation taking 18-22 days against a 16-day constraint, SWE-bench Pro integration adds complexity, and there's lingering concern about spec quality given CodeSpecBench's 20.2% repo-level performance affecting downstream tasks. Clarity rates well at 4/5 with solid experimental design and honest ablations, though the narrative is dense. Impact lands at 3/5 depending on whether execution grounding actually delivers meaningful gains over PGS on the shared benchmarks.

That puts me at 3.375 overall—below the 4.0 threshold. Since this is Round 8 of 10, I need to decide whether to pass or revise. The core issues are the PGS v2 coverage misrepresentation, which is fixable, the timeline that genuinely exceeds the constraint, and the deeper novelty question given PGS v2's improvements. The PGS v2 factual claim is critical but correctable with repositioning, the timeline concern is real though the idea acknowledges different modes, but the novelty gap is the hardest problem to solve.

Actually, stepping back—the experimental design is solid with honest ablations, and execution grounding does address a real weakness where PGS's property accuracy drops on harder problems. The debugging extension with DebugBench and a new baseline, plus the component decomposition analysis, are genuine contributions even if incremental. This reads more like a strong Findings paper for EMNLP 2026 than a Main Conference paper, which would require execution grounding to show substantial gains over PGS on their shared benchmarks.

Rescoring with this in mind: novelty is 3/5—three modest but valid advances stacked together—and feasibility is 3/5 given the timeline tension between the 16-day constraint and the realistic 18-22 day estimate.

The clarity is solid at 4/5 with well-specified experiments, and impact lands at 3/5 as a useful but incremental contribution. That averages to 3.25, still below threshold, but with two rounds left in this cycle, the fixes are concrete: correct the PGS v2 claims, tighten the timeline, and reposition the novelty more compellingly. Let me look more carefully at what the idea actually says about PGS's validation approach to make sure I'm not mischaracterizing it.

I'm catching a critical factual error here—the idea cites PGS v1 benchmarks (82.4% on easy, 62.8% on medium, 48.9% on hard LiveCodeBench) and claims PGS doesn't evaluate on CodeContests or SWE-bench, but PGS v2 from May 2026 explicitly does both. The idea mentions the v2 revision in passing but based its analysis on v1, which undermines the differentiation argument that hinges on broader evaluation coverage.

The valid differentiators that remain are DebugBench and cross-file completion, plus the use of SWE-bench Pro instead of standard SWE-bench to address contamination concerns. I need to recommend a revision that corrects the PGS v2 coverage claims, repositions the novelty narrative around what's genuinely uncovered, and addresses the timeline constraint where the idea references a future paper. The fact that Qwen2.5-Coder appears in both the PGS v2 benchmark and ExeSpec's planned approach actually gives us a solid basis for direct comparison. Given we're at Round 8 of 10, I think "revise" is the right call—the PGS v2 factual error is too significant to overlook, and the novelty framing needs adjustment once we correct that.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d00557e-172d-445e-9b03-eb75e9f11ac0",
  "isSidechain": false,
  "requestId": "req_011CawsTqAxYuUHEABZ43vBL",
  "type": "assistant",
  "uuid": "490354d1-8eab-4cb5-afd7-799a3aee1d85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSW7Ti8N8UA53ftXDyHUik",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 63751,
      "output_tokens": 2748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2748,
          "cache_read_input_tokens": 63751,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 944
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

_source line 76 · 2026-05-12T02:18:01.647Z_

Now let me do one final check — searching for any very recent concurrent work that might have appeared in the past few weeks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "490354d1-8eab-4cb5-afd7-799a3aee1d85",
  "isSidechain": false,
  "requestId": "req_011CawsTqAxYuUHEABZ43vBL",
  "type": "assistant",
  "uuid": "540a3a6c-7192-4c1d-8339-a4157577a81a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSW7Ti8N8UA53ftXDyHUik",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 63751,
      "output_tokens": 2748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2748,
          "cache_read_input_tokens": 63751,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 944
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

_source line 77 · 2026-05-12T02:18:01.659Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S8M6YUs9LFgbmp2S4i4DBC`</summary>

```json
{
  "query": "code generation property verification execution grounding arXiv April May 2026 new"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "540a3a6c-7192-4c1d-8339-a4157577a81a",
  "isSidechain": false,
  "requestId": "req_011CawsTqAxYuUHEABZ43vBL",
  "type": "assistant",
  "uuid": "9fef8687-1a6d-4b0b-b3a6-d6a7204fc033",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CSW7Ti8N8UA53ftXDyHUik",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 63751,
      "output_tokens": 2748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2748,
          "cache_read_input_tokens": 63751,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 944
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

_source line 78_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "9fef8687-1a6d-4b0b-b3a6-d6a7204fc033",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "ExeSpec: Execution-grounded Behavioral Specifications for Code LLMs",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Tool result

_source line 80 · 2026-05-12T02:18:09.536Z_

<details><summary>↩ Tool result · `toolu_01S8M6YUs9LFgbmp2S4i4DBC`</summary>

```text
Web search results for query: "code generation property verification execution grounding arXiv April May 2026 new"

Links: [{"title":"Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis","url":"https://arxiv.org/html/2604.10800v1"},{"title":"[2604.10800v1] Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis","url":"https://arxiv.org/abs/2604.10800v1"},{"title":"Grounding Data Science Code Generation with Input-Output Specifications","url":"https://arxiv.org/html/2402.08073v2"},{"title":"Generating Verifiable CoT from Execution-Traces","url":"https://arxiv.org/pdf/2512.00127"},{"title":"RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning","url":"https://arxiv.org/html/2410.02089v2"},{"title":"[2410.02089] RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning","url":"https://arxiv.org/abs/2410.02089"},{"title":"Rethinking the Evaluation of Secure Code Generation","url":"https://arxiv.org/html/2503.15554v2"},{"title":"Towards Execution-Grounded Automated AI Research","url":"https://arxiv.org/pdf/2601.14525.pdf?curius=526"},{"title":"[2402.08073] Grounding Data Science Code Generation with Input-Output Specifications","url":"https://arxiv.org/abs/2402.08073"},{"title":"RLEF: GROUNDING CODE LLMS IN EXECUTION FEEDBACK WITH REINFORCEMENT LEARNING","url":"https://www.arxiv.org/pdf/2410.02089"}]

Based on the search results, here are the relevant papers from arXiv in April-May 2026 related to code generation, property verification, execution, and grounding:

## Key Paper: April 2026

**"Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis"** (published April 12, 2026)

This paper addresses a fundamental challenge in agentic AI systems by proposing a unified cross-language vulnerability lifecycle framework with three LLM-driven reasoning stages: hybrid structural-semantic detection, execution-grounded agentic validation, and validation-aware iterative repair—governed by a strict invariant that no repair action is taken without execution-based confirmation of exploitability.

**Key Technical Contributions:**
- Cross-language generalization via a Universal Abstract Syntax Tree (uAST) normalizing Java, Python, and C++ into a shared structural schema, combined with a hybrid fusion of GraphSAGE and Qwen2.5-Coder-1.5B embeddings
- The framework achieves 89.84-92.02% intra-language detection accuracy and 74.43-80.12% zero-shot cross-language F1, resolving 69.74% of vulnerabilities end-to-end
- Repair activates exclusively for execution-confirmed samples using a LoRA fine-tuned Qwen2.5-Coder-1.5B-Instruct to generate minimal patches from structured prompts

This work exemplifies how execution-grounded feedback can improve the reliability of code generation and verification in multi-stage agentic systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fef8687-1a6d-4b0b-b3a6-d6a7204fc033",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "02e928c6-4d6e-4c9a-9046-4bbb41b7976c",
  "toolUseResult": {
    "query": "code generation property verification execution grounding arXiv April May 2026 new",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Bd9AhCxiwYzXy773GXqyVs",
        "content": [
          {
            "title": "Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis",
            "url": "https://arxiv.org/html/2604.10800v1"
          },
          {
            "title": "[2604.10800v1] Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis",
            "url": "https://arxiv.org/abs/2604.10800v1"
          },
          {
            "title": "Grounding Data Science Code Generation with Input-Output Specifications",
            "url": "https://arxiv.org/html/2402.08073v2"
          },
          {
            "title": "Generating Verifiable CoT from Execution-Traces",
            "url": "https://arxiv.org/pdf/2512.00127"
          },
          {
            "title": "RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning",
            "url": "https://arxiv.org/html/2410.02089v2"
          },
          {
            "title": "[2410.02089] RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning",
            "url": "https://arxiv.org/abs/2410.02089"
          },
          {
            "title": "Rethinking the Evaluation of Secure Code Generation",
            "url": "https://arxiv.org/html/2503.15554v2"
          },
          {
            "title": "Towards Execution-Grounded Automated AI Research",
            "url": "https://arxiv.org/pdf/2601.14525.pdf?curius=526"
          },
          {
            "title": "[2402.08073] Grounding Data Science Code Generation with Input-Output Specifications",
            "url": "https://arxiv.org/abs/2402.08073"
          },
          {
            "title": "RLEF: GROUNDING CODE LLMS IN EXECUTION FEEDBACK WITH REINFORCEMENT LEARNING",
            "url": "https://www.arxiv.org/pdf/2410.02089"
          }
        ]
      },
      "Based on the search results, here are the relevant papers from arXiv in April-May 2026 related to code generation, property verification, execution, and grounding:\n\n## Key Paper: April 2026\n\n**\"Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis\"** (published April 12, 2026)\n\nThis paper addresses a fundamental challenge in agentic AI systems by proposing a unified cross-language vulnerability lifecycle framework with three LLM-driven reasoning stages: hybrid structural-semantic detection, execution-grounded agentic validation, and validation-aware iterative repair—governed by a strict invariant that no repair action is taken without execution-based confirmation of exploitability.\n\n**Key Technical Contributions:**\n- Cross-language generalization via a Universal Abstract Syntax Tree (uAST) normalizing Java, Python, and C++ into a shared structural schema, combined with a hybrid fusion of GraphSAGE and Qwen2.5-Coder-1.5B embeddings\n- The framework achieves 89.84-92.02% intra-language detection accuracy and 74.43-80.12% zero-shot cross-language F1, resolving 69.74% of vulnerabilities end-to-end\n- Repair activates exclusively for execution-confirmed samples using a LoRA fine-tuned Qwen2.5-Coder-1.5B-Instruct to generate minimal patches from structured prompts\n\nThis work exemplifies how execution-grounded feedback can improve the reliability of code generation and verification in multi-stage agentic systems."
    ],
    "durationSeconds": 7.871344233000011
  },
  "sourceToolAssistantUUID": "9fef8687-1a6d-4b0b-b3a6-d6a7204fc033",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 81 · 2026-05-12T02:18:09.542Z_

```json
{
  "parentUuid": "02e928c6-4d6e-4c9a-9046-4bbb41b7976c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "abe3848d-2679-4329-b5fb-4ebe57156637",
  "timestamp": "2026-05-12T02:18:09.542Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 82 · 2026-05-12T02:18:12.500Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0155aaHfscgHUA4BsY2MwcT7`</summary>

```json
{
  "query": "PGS arXiv 2506.18315 v2 May 2026 CodeContests SWE-bench results evaluation benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abe3848d-2679-4329-b5fb-4ebe57156637",
  "isSidechain": false,
  "requestId": "req_011CawsZAc99P11q2ABgQDsX",
  "type": "assistant",
  "uuid": "82801196-20e9-49ca-bbfa-ef8a2433e43c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nt8Eg53dzQZQh3yvtrRr19",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3716,
      "cache_read_input_tokens": 64695,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3716,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 84,
          "cache_read_input_tokens": 64695,
          "cache_creation_input_tokens": 3716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3716
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

_source line 83 · 2026-05-12T02:18:27.760Z_

<details><summary>↩ Tool result · `toolu_0155aaHfscgHUA4BsY2MwcT7`</summary>

```text
Web search results for query: "PGS arXiv 2506.18315 v2 May 2026 CodeContests SWE-bench results evaluation benchmarks"

Links: [{"title":"The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason","url":"https://arxiv.org/html/2506.12286v4"},{"title":"SWE Context Bench: A Benchmark for Context Learning in Coding","url":"https://arxiv.org/html/2602.08316"},{"title":"[2602.08316] SWE Context Bench: A Benchmark for Context Learning in Coding","url":"https://arxiv.org/abs/2602.08316"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"[2512.17419] SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/abs/2512.17419"},{"title":"Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study","url":"https://arxiv.org/html/2503.15223v1"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving","url":"https://arxiv.org/html/2504.02605v1"},{"title":"SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories","url":"https://arxiv.org/html/2512.17419v1"},{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"}]

The search didn't find the specific arXiv paper 2506.18315 v2. Let me try a more specific search:

Links: [{"title":"[2506.18315] Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/abs/2506.18315"},{"title":"Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/html/2506.18315"},{"title":"[2510.18315] Higher Embedding Dimension Creates a Stronger World Model for a Simple Sorting Task","url":"https://arxiv.org/abs/2510.18315"},{"title":"[2505.18315] COLORA: Efficient Fine-Tuning for Convolutional Models with a Study Case on Optical Coherence Tomography Image Classification","url":"https://arxiv.org/abs/2505.18315"},{"title":"[2503.18315] Scalable architecture for dark photon searches: Superconducting-qubit proof of principle","url":"https://arxiv.org/abs/2503.18315"},{"title":"1 Introduction","url":"https://arxiv.org/html/2501.18315"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=9425&show=2000"},{"title":"[2501.18315] Surface Defect Identification using Bayesian Filtering on a 3D Mesh","url":"https://arxiv.org/abs/2501.18315"},{"title":"Topological Vector Spaces: a non-standard approach with monads and galaxies.","url":"https://arxiv.org/html/2403.18315"},{"title":"[2502.18315] GraphRank Pro+: Advancing Talent Analytics Through Knowledge Graphs and Sentiment-Enhanced Skill Profiling","url":"https://arxiv.org/abs/2502.18315"}]

Now let me search for more details about PGS results on CodeContests and SWE-bench:

Links: [{"title":"Enhanced LLM code generation with property-based testing! New Framework PGS to Break Self-Deception | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/llm-paper/property-generated-solver"},{"title":"Use Property-Based Testing to Bridge LLM Code Generation and Validation","url":"https://arxiv.org/html/2506.18315v1"},{"title":"CodeContests+: High-Quality Test Case Generation for ...","url":"https://aclanthology.org/2025.findings-emnlp.299.pdf"},{"title":"CodeContests Dataset Overview","url":"https://www.emergentmind.com/topics/codecontests-dataset"},{"title":"Improved PGS Solver Studio Beta - Announcements - Developer Forum | Roblox","url":"https://devforum.roblox.com/t/improved-pgs-solver-studio-beta/187184"},{"title":"CodeContests Benchmark (Code Generation)","url":"https://paperswithcode.com/sota/code-generation-on-codecontests"},{"title":"Improving Simulation and Performance with an Advanced Physics Solver | Medium","url":"https://mizerski.medium.com/improving-simulation-and-performance-with-an-advanced-physics-solver-da071a98d35"},{"title":"CodeContests+: High-Quality Test Case Generation for Competitive Programming","url":"https://arxiv.org/html/2506.05817v1"},{"title":"Differences between PGS ad TGS solvers - Isaac Sim - NVIDIA Developer Forums","url":"https://forums.developer.nvidia.com/t/differences-between-pgs-ad-tgs-solvers/277935"},{"title":"(PDF) CodeContests+: High-Quality Test Case Generation for Competitive Programming","url":"https://www.researchgate.net/publication/392514571_CodeContests_High-Quality_Test_Case_Generation_for_Competitive_Programming"}]

Perfect! I found the paper and good information about it. Let me search for more specific details about SWE-bench results if available in the v2:

Links: [{"title":"SWE-bench Verified","url":"https://www.vals.ai/benchmarks/swebench"},{"title":"Evaluation - SWE-bench","url":"https://www.swebench.com/SWE-bench/guides/evaluation/"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"SWE-Bench Verified Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/swe-bench-verified"},{"title":"GitHub - SWE-bench/experiments: Open sourced predictions, execution logs, trajectories, and results from model inference + evaluation runs on the SWE-bench task. · GitHub","url":"https://github.com/SWE-bench/experiments"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and","url":"https://arxiv.org/pdf/2506.17208"},{"title":"SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?","url":"https://static.scale.com/uploads/654197dc94d34f66c0f5184e/SWEAP_Eval_Scale%20(9).pdf"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-bench Leaderboards","url":"https://www.swebench.com/"},{"title":"SWE-bench Verified | Epoch AI","url":"https://epoch.ai/benchmarks/swe-bench-verified"}]

Based on my search results, I found information about the arXiv paper 2506.18315 (v2, May 2026). Here's what I found:

## Paper Overview

The paper introduces Property-Generated Solver (PGS), a novel framework that leverages Property-Based Testing (PBT) to validate high-level program properties or invariants, instead of relying on specific input-output examples. These properties are often simpler to define and verify than directly predicting exhaustive test oracles.

## Key Results and Benchmarks

The paper evaluates PGS across multiple code generation benchmarks (HumanEval, MBPP and LivecodeBench) of varying difficulty using LLMs with different capabilities, showcasing that PGS achieves a 23.1%–37.3% relative improvement (pass@1) over previous TDD methods on problems that are challenging for direct prompting approaches.

The authors used three code generation benchmarks (HumanEval, MBPP, and LiveCodeBench) and compared them to traditional TDD methods and state-of-the-art debugging assistance methods.

## Framework Architecture

PGS employs two key agents—a Generator and a Tester—that systematically decouple code generation from its validation. After the Generator produces initial candidate programs, these agents collaborate iteratively: the Tester rigorously validates them using defined properties, while the Generator refines the programs based on the feedback from validation results.

## Technical Details

For the PGS framework, both the Generator and Tester roles are implemented using the LLMs mentioned. All generation tasks within PGS are conducted with a consistent temperature of 0.5 and a maximum generation limit of 32,768 tokens per LLM call. The iterative refinement cycle between Generator and Tester is capped at a maximum of 5 iterations per problem.

The search results did not show specific results for CodeContests or SWE-bench benchmarks in the available paper excerpts, though the paper focuses primarily on code generation benchmarks like HumanEval, MBPP, and LiveCodeBench.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82801196-20e9-49ca-bbfa-ef8a2433e43c",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "85778d9d-fb0c-4733-8905-23d1a16b9a7b",
  "toolUseResult": {
    "query": "PGS arXiv 2506.18315 v2 May 2026 CodeContests SWE-bench results evaluation benchmarks",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QZBnL2BYKeAurHaqdmPfZv",
        "content": [
          {
            "title": "The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason",
            "url": "https://arxiv.org/html/2506.12286v4"
          },
          {
            "title": "SWE Context Bench: A Benchmark for Context Learning in Coding",
            "url": "https://arxiv.org/html/2602.08316"
          },
          {
            "title": "[2602.08316] SWE Context Bench: A Benchmark for Context Learning in Coding",
            "url": "https://arxiv.org/abs/2602.08316"
          },
          {
            "title": "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems",
            "url": "https://arxiv.org/html/2506.17208v2"
          },
          {
            "title": "[2512.17419] SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories",
            "url": "https://arxiv.org/abs/2512.17419"
          },
          {
            "title": "Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study",
            "url": "https://arxiv.org/html/2503.15223v1"
          },
          {
            "title": "SWE-Bench Verified Benchmark Leaderboard",
            "url": "https://llm-stats.com/benchmarks/swe-bench-verified"
          },
          {
            "title": "Multi-SWE-bench: A Multilingual Benchmark for Issue Resolving",
            "url": "https://arxiv.org/html/2504.02605v1"
          },
          {
            "title": "SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories",
            "url": "https://arxiv.org/html/2512.17419v1"
          },
          {
            "title": "What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair",
            "url": "https://arxiv.org/pdf/2602.04449"
          }
        ]
      },
      "The search didn't find the specific arXiv paper 2506.18315 v2. Let me try a more specific search:",
      {
        "tool_use_id": "srvtoolu_01YZd5iAxyfZ4odL7vAwJAkY",
        "content": [
          {
            "title": "[2506.18315] Use Property-Based Testing to Bridge LLM Code Generation and Validation",
            "url": "https://arxiv.org/abs/2506.18315"
          },
          {
            "title": "Use Property-Based Testing to Bridge LLM Code Generation and Validation",
            "url": "https://arxiv.org/html/2506.18315"
          },
          {
            "title": "[2510.18315] Higher Embedding Dimension Creates a Stronger World Model for a Simple Sorting Task",
            "url": "https://arxiv.org/abs/2510.18315"
          },
          {
            "title": "[2505.18315] COLORA: Efficient Fine-Tuning for Convolutional Models with a Study Case on Optical Coherence Tomography Image Classification",
            "url": "https://arxiv.org/abs/2505.18315"
          },
          {
            "title": "[2503.18315] Scalable architecture for dark photon searches: Superconducting-qubit proof of principle",
            "url": "https://arxiv.org/abs/2503.18315"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2501.18315"
          },
          {
            "title": "Computer Science Jun 2025",
            "url": "https://arxiv.org/list/cs/2025-06?skip=9425&show=2000"
          },
          {
            "title": "[2501.18315] Surface Defect Identification using Bayesian Filtering on a 3D Mesh",
            "url": "https://arxiv.org/abs/2501.18315"
          },
          {
            "title": "Topological Vector Spaces: a non-standard approach with monads and galaxies.",
            "url": "https://arxiv.org/html/2403.18315"
          },
          {
            "title": "[2502.18315] GraphRank Pro+: Advancing Talent Analytics Through Knowledge Graphs and Sentiment-Enhanced Skill Profiling",
            "url": "https://arxiv.org/abs/2502.18315"
          }
        ]
      },
      "Now let me search for more details about PGS results on CodeContests and SWE-bench:",
      {
        "tool_use_id": "srvtoolu_01Tjq2T9xwcqogA5YDZaQaAT",
        "content": [
          {
            "title": "Enhanced LLM code generation with property-based testing! New Framework PGS to Break Self-Deception | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media",
            "url": "https://ai-scholar.tech/en/articles/llm-paper/property-generated-solver"
          },
          {
            "title": "Use Property-Based Testing to Bridge LLM Code Generation and Validation",
            "url": "https://arxiv.org/html/2506.18315v1"
          },
          {
            "title": "CodeContests+: High-Quality Test Case Generation for ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.299.pdf"
          },
          {
            "title": "CodeContests Dataset Overview",
            "url": "https://www.emergentmind.com/topics/codecontests-dataset"
          },
          {
            "title": "Improved PGS Solver Studio Beta - Announcements - Developer Forum | Roblox",
            "url": "https://devforum.roblox.com/t/improved-pgs-solver-studio-beta/187184"
          },
          {
            "title": "CodeContests Benchmark (Code Generation)",
            "url": "https://paperswithcode.com/sota/code-generation-on-codecontests"
          },
          {
            "title": "Improving Simulation and Performance with an Advanced Physics Solver | Medium",
            "url": "https://mizerski.medium.com/improving-simulation-and-performance-with-an-advanced-physics-solver-da071a98d35"
          },
          {
            "title": "CodeContests+: High-Quality Test Case Generation for Competitive Programming",
            "url": "https://arxiv.org/html/2506.05817v1"
          },
          {
            "title": "Differences between PGS ad TGS solvers - Isaac Sim - NVIDIA Developer Forums",
            "url": "https://forums.developer.nvidia.com/t/differences-between-pgs-ad-tgs-solvers/277935"
          },
          {
            "title": "(PDF) CodeContests+: High-Quality Test Case Generation for Competitive Programming",
            "url": "https://www.researchgate.net/publication/392514571_CodeContests_High-Quality_Test_Case_Generation_for_Competitive_Programming"
          }
        ]
      },
      "Perfect! I found the paper and good information about it. Let me search for more specific details about SWE-bench results if available in the v2:",
      {
        "tool_use_id": "srvtoolu_01LjgNoqbtxPd2xMmoPJ6dTA",
        "content": [
          {
            "title": "SWE-bench Verified",
            "url": "https://www.vals.ai/benchmarks/swebench"
          },
          {
            "title": "Evaluation - SWE-bench",
            "url": "https://www.swebench.com/SWE-bench/guides/evaluation/"
          },
          {
            "title": "GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub",
            "url": "https://github.com/swe-bench/SWE-bench"
          },
          {
            "title": "SWE-Bench Verified Benchmark Leaderboard",
            "url": "https://llm-stats.com/benchmarks/swe-bench-verified"
          },
          {
            "title": "GitHub - SWE-bench/experiments: Open sourced predictions, execution logs, trajectories, and results from model inference + evaluation runs on the SWE-bench task. · GitHub",
            "url": "https://github.com/SWE-bench/experiments"
          },
          {
            "title": "Dissecting the SWE-Bench Leaderboards: Profiling Submitters and",
            "url": "https://arxiv.org/pdf/2506.17208"
          },
          {
            "title": "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?",
            "url": "https://static.scale.com/uploads/654197dc94d34f66c0f5184e/SWEAP_Eval_Scale%20(9).pdf"
          },
          {
            "title": "Introducing SWE-bench Verified | OpenAI",
            "url": "https://openai.com/index/introducing-swe-bench-verified/"
          },
          {
            "title": "SWE-bench Leaderboards",
            "url": "https://www.swebench.com/"
          },
          {
            "title": "SWE-bench Verified | Epoch AI",
            "url": "https://epoch.ai/benchmarks/swe-bench-verified"
          }
        ]
      },
      "Based on my search results, I found information about the arXiv paper 2506.18315 (v2, May 2026). Here's what I found:\n\n## Paper Overview\n\nThe paper introduces Property-Generated Solver (PGS), a novel framework that leverages Property-Based Testing (PBT) to validate high-level program properties or invariants, instead of relying on specific input-output examples. These properties are often simpler to define and verify than directly predicting exhaustive test oracles.\n\n## Key Results and Benchmarks\n\nThe paper evaluates PGS across multiple code generation benchmarks (HumanEval, MBPP and LivecodeBench) of varying difficulty using LLMs with different capabilities, showcasing that PGS achieves a 23.1%–37.3% relative improvement (pass@1) over previous TDD methods on problems that are challenging for direct prompting approaches.\n\nThe authors used three code generation benchmarks (HumanEval, MBPP, and LiveCodeBench) and compared them to traditional TDD methods and state-of-the-art debugging assistance methods.\n\n## Framework Architecture\n\nPGS employs two key agents—a Generator and a Tester—that systematically decouple code generation from its validation. After the Generator produces initial candidate programs, these agents collaborate iteratively: the Tester rigorously validates them using defined properties, while the Generator refines the programs based on the feedback from validation results.\n\n## Technical Details\n\nFor the PGS framework, both the Generator and Tester roles are implemented using the LLMs mentioned. All generation tasks within PGS are conducted with a consistent temperature of 0.5 and a maximum generation limit of 32,768 tokens per LLM call. The iterative refinement cycle between Generator and Tester is capped at a maximum of 5 iterations per problem.\n\nThe search results did not show specific results for CodeContests or SWE-bench benchmarks in the available paper excerpts, though the paper focuses primarily on code generation benchmarks like HumanEval, MBPP, and LiveCodeBench."
    ],
    "durationSeconds": 15.25579112900002
  },
  "sourceToolAssistantUUID": "82801196-20e9-49ca-bbfa-ef8a2433e43c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 84 · 2026-05-12T02:18:31.733Z_

<details><summary>Logged reasoning block</summary>

```text
This is interesting — the general search results about PGS seem to describe the v1 version (only HumanEval, MBPP, LiveCodeBench). But my earlier WebFetch of the full HTML page found references to CodeContests and SWE-bench in the v2 version. 

Let me try to access the v2 specifically to confirm.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85778d9d-fb0c-4733-8905-23d1a16b9a7b",
  "isSidechain": false,
  "requestId": "req_011CawsaWWjvQJJhW5TnEtNc",
  "type": "assistant",
  "uuid": "0c927227-6ff9-4a48-b3c7-353c3e332949",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpdVUeNV8SdFC9ZbudcMoB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2551,
      "cache_read_input_tokens": 68411,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 68411,
          "cache_creation_input_tokens": 2551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2551
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

_source line 85 · 2026-05-12T02:18:32.235Z_

Let me directly fetch the v2 of PGS to confirm the benchmark expansion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c927227-6ff9-4a48-b3c7-353c3e332949",
  "isSidechain": false,
  "requestId": "req_011CawsaWWjvQJJhW5TnEtNc",
  "type": "assistant",
  "uuid": "e4ccbc63-e170-4eb6-9d48-0d2e17e7c9da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpdVUeNV8SdFC9ZbudcMoB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2551,
      "cache_read_input_tokens": 68411,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 68411,
          "cache_creation_input_tokens": 2551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2551
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

_source line 86 · 2026-05-12T02:18:33.728Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01KERAJMrN9qYRdxJuUupcaT`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.18315v2",
  "prompt": "What is the title of this version? What benchmarks are listed in the abstract or paper? Does this version evaluate on CodeContests and SWE-bench? What is the submission/revision date? List all benchmarks mentioned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4ccbc63-e170-4eb6-9d48-0d2e17e7c9da",
  "isSidechain": false,
  "requestId": "req_011CawsaWWjvQJJhW5TnEtNc",
  "type": "assistant",
  "uuid": "95157c4f-c82f-4da7-b36a-588c4a531358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JpdVUeNV8SdFC9ZbudcMoB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2551,
      "cache_read_input_tokens": 68411,
      "output_tokens": 247,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 247,
          "cache_read_input_tokens": 68411,
          "cache_creation_input_tokens": 2551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2551
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

_source line 87 · 2026-05-12T02:18:37.844Z_

<details><summary>↩ Tool result · `toolu_01KERAJMrN9qYRdxJuUupcaT`</summary>

```text
# Paper Summary

**Title:** "Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback"

**Submission/Revision Date:** Originally submitted June 23, 2025 (v1); revised May 1, 2026 (v2)

**Benchmarks Mentioned in Abstract:** The abstract does not specify particular benchmark names. It references "diverse benchmarks" generally and mentions achieving improvements in "pass@1" metrics and "bug fix rate[s]," but does not name CodeContests, SWE-bench, or other specific datasets.

**Evaluation on CodeContests/SWE-bench:** The provided content does not indicate whether this version evaluates on CodeContests or SWE-bench. The abstract states the method achieves results "across diverse benchmarks" but does not list specific benchmark names.

**Key Claim:** The proposed Property-Generated Solver (PGS) approach demonstrates improvements of up to 13.4% in pass@1 metrics and a 64% fix rate on initially failing problems, with bug fix rates described as "1.4x-1.6x higher than the strongest debugging-based approaches."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95157c4f-c82f-4da7-b36a-588c4a531358",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "8c146814-cf6b-449c-adca-9f1723359fec",
  "toolUseResult": {
    "bytes": 47317,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** \"Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback\"\n\n**Submission/Revision Date:** Originally submitted June 23, 2025 (v1); revised May 1, 2026 (v2)\n\n**Benchmarks Mentioned in Abstract:** The abstract does not specify particular benchmark names. It references \"diverse benchmarks\" generally and mentions achieving improvements in \"pass@1\" metrics and \"bug fix rate[s],\" but does not name CodeContests, SWE-bench, or other specific datasets.\n\n**Evaluation on CodeContests/SWE-bench:** The provided content does not indicate whether this version evaluates on CodeContests or SWE-bench. The abstract states the method achieves results \"across diverse benchmarks\" but does not list specific benchmark names.\n\n**Key Claim:** The proposed Property-Generated Solver (PGS) approach demonstrates improvements of up to 13.4% in pass@1 metrics and a 64% fix rate on initially failing problems, with bug fix rates described as \"1.4x-1.6x higher than the strongest debugging-based approaches.\"",
    "durationMs": 4114,
    "url": "https://arxiv.org/abs/2506.18315v2"
  },
  "sourceToolAssistantUUID": "95157c4f-c82f-4da7-b36a-588c4a531358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 88_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "8c146814-cf6b-449c-adca-9f1723359fec",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "ai-title",
  "aiTitle": "ExeSpec: Execution-grounded Behavioral Specifications for Code LLMs",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Tool call

_source line 90 · 2026-05-12T02:18:42.304Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ha5LtfJrvrzBHqKtkVrx5K`</summary>

```json
{
  "url": "https://arxiv.org/html/2506.18315v2",
  "prompt": "I need to verify the EXACT benchmarks evaluated in this v2 paper. Please list: (1) ALL benchmark names mentioned in the experiments/evaluation section (tables or text). (2) Whether CodeContests is evaluated — find the exact table or text. (3) Whether SWE-bench is evaluated — find the exact table or text. (4) ALL models used in the evaluation. (5) The EXACT property generation accuracy numbers broken down by difficulty (easy/medium/hard)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c146814-cf6b-449c-adca-9f1723359fec",
  "isSidechain": false,
  "requestId": "req_011CawsbFYMb4xiZiWra4Ej1",
  "type": "assistant",
  "uuid": "be7bf8f0-1b25-4936-8edd-02eed542092d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8TDJEhZ4k8ubHqmhfSasj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 70962,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 70962,
          "cache_creation_input_tokens": 523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 523
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

_source line 91 · 2026-05-12T02:18:48.217Z_

<details><summary>↩ Tool result · `toolu_01Ha5LtfJrvrzBHqKtkVrx5K`</summary>

```text
# PGS Paper Evaluation Benchmarks and Models

## (1) ALL Benchmarks in Experiments/Evaluation

The paper evaluates on **five benchmarks**:
- HumanEval
- MBPP
- LiveCodeBench (LCB)
- CodeContests
- SWE-Bench

## (2) CodeContests Evaluation

**YES, CodeContests is evaluated.** Table 3 shows results with the header "CodeContest" containing pass@1 scores across multiple models (DeepSeek-V2, Qwen2.5, DeepSeek-R1-32B, etc.). The baseline achieves 12.5% ± 0.6%, while PGS reaches 20.2% ± 1.8% on DeepSeek-V2.

## (3) SWE-Bench Evaluation

**YES, SWE-Bench is evaluated.** Table 3 includes "SWE-Bench" results comparing SWE-agent baseline against PGS across multiple models. For example, on DeepSeek-V2, the baseline achieves 9.8% ± 1.4% versus PGS's 11.9% ± 1.0%.

## (4) ALL Models Used

Six LLMs evaluated:
- DeepSeek-Coder-V2
- Qwen2.5-Coder
- DeepSeek-R1-32B
- Qwen3-30B
- DeepSeek-V3.1
- Claude-Sonnet-4

## (5) Property Generation Accuracy by Difficulty

**Table 2** presents "Asymmetry of Verification" with accuracy metrics:
- Easy: 90.6% generation vs. 93.8% verification
- Medium: 67.6% generation vs. 91.2% verification
- Hard: 32.4% generation vs. 76.5% verification
- Overall: 63.0% generation vs. 87.0% verification
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be7bf8f0-1b25-4936-8edd-02eed542092d",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "69e2c16f-caf0-4404-9bb4-09a985dca82c",
  "toolUseResult": {
    "bytes": 526190,
    "code": 200,
    "codeText": "OK",
    "result": "# PGS Paper Evaluation Benchmarks and Models\n\n## (1) ALL Benchmarks in Experiments/Evaluation\n\nThe paper evaluates on **five benchmarks**:\n- HumanEval\n- MBPP\n- LiveCodeBench (LCB)\n- CodeContests\n- SWE-Bench\n\n## (2) CodeContests Evaluation\n\n**YES, CodeContests is evaluated.** Table 3 shows results with the header \"CodeContest\" containing pass@1 scores across multiple models (DeepSeek-V2, Qwen2.5, DeepSeek-R1-32B, etc.). The baseline achieves 12.5% ± 0.6%, while PGS reaches 20.2% ± 1.8% on DeepSeek-V2.\n\n## (3) SWE-Bench Evaluation\n\n**YES, SWE-Bench is evaluated.** Table 3 includes \"SWE-Bench\" results comparing SWE-agent baseline against PGS across multiple models. For example, on DeepSeek-V2, the baseline achieves 9.8% ± 1.4% versus PGS's 11.9% ± 1.0%.\n\n## (4) ALL Models Used\n\nSix LLMs evaluated:\n- DeepSeek-Coder-V2\n- Qwen2.5-Coder\n- DeepSeek-R1-32B\n- Qwen3-30B\n- DeepSeek-V3.1\n- Claude-Sonnet-4\n\n## (5) Property Generation Accuracy by Difficulty\n\n**Table 2** presents \"Asymmetry of Verification\" with accuracy metrics:\n- Easy: 90.6% generation vs. 93.8% verification\n- Medium: 67.6% generation vs. 91.2% verification\n- Hard: 32.4% generation vs. 76.5% verification\n- Overall: 63.0% generation vs. 87.0% verification",
    "durationMs": 5888,
    "url": "https://arxiv.org/html/2506.18315v2"
  },
  "sourceToolAssistantUUID": "be7bf8f0-1b25-4936-8edd-02eed542092d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 92 · 2026-05-12T02:19:27.576Z_

<details><summary>Logged reasoning block</summary>

```text
This is CRITICAL. PGS v2 DOES evaluate on CodeContests and SWE-bench. The idea claims PGS doesn't — this is factually incorrect.

Moreover, PGS v2's property generation accuracy by difficulty is:
- Easy: 90.6% generation / 93.8% verification  
- Medium: 67.6% generation / 91.2% verification
- Hard: 32.4% generation / 76.5% verification

The idea claims "82.4% (easy), 62.8% (medium), and 48.9% (hard)" — these numbers don't match v2's numbers at all. 

Looking more closely, the idea cites these figures on LiveCodeBench, but the v2 paper's "Asymmetry of Verification" table shows different property generation accuracy numbers entirely. The discrepancy suggests either the idea is pulling from v1 data or the numbers have been misreported.

What's striking is that the idea references v2 by its revised title and May 2026 date, yet makes claims about PGS not evaluating on certain benchmarks that only apply to v1. So it seems the generator knew v2 existed but actually based its analysis on v1 content while mixing in numbers that don't match either version.

Now I need to check whether this discrepancy actually undermines ExeSpec's novelty. Looking at PGS v2's actual performance across the benchmarks ExeSpec targets—CodeContests and SWE-Bench show meaningful gaps between PGS and stronger models like DeepSeek-R1-32B—ExeSpec still has room to differentiate through execution grounding and cross-spec consistency checks, which PGS doesn't employ.

The bigger concern is that PGS v2's property generation accuracy is actually worse than the original idea suggested (32.4% versus the claimed 48.9%), which paradoxically strengthens the case for execution grounding as a necessary correction mechanism. But the framing needs to shift: this isn't about extending PGS to new benchmarks, it's about improving PGS's core approach through execution grounding while also expanding into debugging and code completion tasks.

The critical issue I'm flagging is that PGS v2's benchmark coverage appears to have been misrepresented in the original proposal. May 2026) evaluates on CodeContests AND SWE-bench. The idea claims it doesn't. This undermines one of three claimed differentiators.

2. **CRITICAL: PGS property accuracy numbers are incorrect** — The idea cites "82.4% (easy), 62.8% (medium), 48.9% (hard)" but PGS v2 reports generation accuracy of 90.6%/67.6%/32.4%. While the general trend is correct (accuracy drops with difficulty), the specific numbers are wrong.

3. **IMPORTANT: Timeline violation** — Manual estimate of 18-22 days exceeds the user's 16-day constraint. Even HIL is 14-18 days (barely fits at the low end).

4. **MODERATE: Novelty repositioning needed** — With PGS v2 covering CodeContests and SWE-bench, ExeSpec's differentiation shifts from expanding to new benchmarks toward execution grounding and debugging capabilities, which is still valuable but represents a narrower advantage than initially framed. The scores reflect this: novelty and feasibility both sit at 3/5 due to timeline pressures and the complexity of reimplementing PGS as a baseline, while the experimental design is solid with honest ablations and controlled comparisons. The impact hinges on whether execution grounding actually delivers meaningful performance gains.

5. **MINOR: Debugging evaluation clarity** — The debugging extension is mentioned but not deeply specified. How exactly are debugging tasks evaluated? What's the success metric?

**Verdict: Revise (Round 8 of 10)**

The paper is fixable. Correct the PGS v2 claims, tighten the timeline, and clarify the debugging evaluation. But I should be honest: the novelty ceiling may be inherently limited by PGS v2's scope. To reach EMNLP Main Conference quality, the execution grounding mechanism or debugging evaluation would need to be more ambitious. As it stands, this is more likely a Findings-track contribution than Main Conference.

Let me draft the review now.

The scores average to 3.25, which is below the 4.0 threshold for acceptance. The core issues are fixable—correcting the PGS v2 claims, repositioning the novelty narrative, and tightening the timeline—but the fundamental challenge is that PGS v2 has already narrowed the differentiation space. The execution grounding and debugging capabilities are valuable, but they'd need to be more ambitious to justify Main Conference acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69e2c16f-caf0-4404-9bb4-09a985dca82c",
  "isSidechain": false,
  "requestId": "req_011Cawsc1tMJdwN1w66rwgZc",
  "type": "assistant",
  "uuid": "520ab515-1f68-4471-86b6-849aff62d575",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01De6qz86GucfVL5ZAJnHdRY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 71485,
      "output_tokens": 1682,
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
          "output_tokens": 1682,
          "cache_read_input_tokens": 71485,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
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

_source line 93 · 2026-05-12T02:19:27.578Z_

This confirms PGS v2 evaluates on five benchmarks including CodeContests and SWE-bench. The idea's claims about PGS are factually incorrect. Let me now do one final search to verify the idea's remaining uniqueness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "520ab515-1f68-4471-86b6-849aff62d575",
  "isSidechain": false,
  "requestId": "req_011Cawsc1tMJdwN1w66rwgZc",
  "type": "assistant",
  "uuid": "eb50a173-9bec-438a-ac4e-7c9f1cbe077d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01De6qz86GucfVL5ZAJnHdRY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 71485,
      "output_tokens": 1682,
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
          "output_tokens": 1682,
          "cache_read_input_tokens": 71485,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
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

_source line 94 · 2026-05-12T02:19:27.585Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UJsRyvAys6ATdiXjKqY8Pp`</summary>

```json
{
  "query": "BACE Bayesian anchored co-evolution code test arXiv 2603.28653 GECCO 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb50a173-9bec-438a-ac4e-7c9f1cbe077d",
  "isSidechain": false,
  "requestId": "req_011Cawsc1tMJdwN1w66rwgZc",
  "type": "assistant",
  "uuid": "94d03dfc-b648-4f7c-b65d-0a951e3a8ec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01De6qz86GucfVL5ZAJnHdRY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 71485,
      "output_tokens": 1682,
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
          "output_tokens": 1682,
          "cache_read_input_tokens": 71485,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
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

_source line 95 · 2026-05-12T02:19:35.517Z_

<details><summary>↩ Tool result · `toolu_01UJsRyvAys6ATdiXjKqY8Pp`</summary>

```text
Web search results for query: "BACE Bayesian anchored co-evolution code test arXiv 2603.28653 GECCO 2026"

Links: [{"title":"BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations","url":"https://arxiv.org/html/2603.28653"},{"title":"[2603.28653] BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations","url":"https://arxiv.org/abs/2603.28653"},{"title":"(PDF) BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations","url":"https://www.researchgate.net/publication/403307603_BACE_LLM-based_Code_Generation_through_Bayesian_Anchored_Co-Evolution_of_Code_and_Test_Populations"},{"title":"[2603.03233] AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework","url":"https://arxiv.org/abs/2603.03233"},{"title":"[2603.03233v1] AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework","url":"https://arxiv.org/abs/2603.03233v1"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1398&show=1000"},{"title":"[2603.18104] Adaptive Domain Models: Bayesian Evolution, Warm Rotation, and Principled Training for Geometric and Neuromorphic AI","url":"https://arxiv.org/abs/2603.18104"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"},{"title":"April 12, 2026 References","url":"https://iridia-ulb.github.io/references/testbib.pdf"},{"title":"Bayesian neural network with autoencoder for model- ...","url":"https://arxiv.org/pdf/2603.07976"}]

Based on the search results, I found the paper you're looking for:

## BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations

BACE (Bayesian Anchored Co-Evolution) is a framework that reformulates synthesis as a Bayesian co-evolutionary process where code and test populations are evolved, guided by belief distributions that are reciprocally updated based on noisy interaction evidence.

**Key Problem Addressed:**
Large Language Models (LLMs) have demonstrated impressive capabilities in code generation. While an interactive feedback loop can improve performance, writing effective tests is a non-trivial task. Early multi-agent frameworks, such as AgentCoder, automated this process but relied on generated tests as absolute ground truth. This approach is fragile: incorrect code frequently passes faulty or trivial tests, while valid solutions are often degraded to satisfy incorrect assertions.

**Core Innovation:**
The framework argues that generated tests remain a valuable signal if modeled as noisy sensors guided by bayesian updates. By anchoring this search on minimal public examples, BACE prevents the co-evolutionary drift typical of self-validating loops.

**Results:**
Extensive evaluations on LiveCodeBench v6 (post-March 2025) reveal that BACE achieves superior performance across both proprietary models and open-weight small language models.

**Publication Details:**
The paper is published in the Genetic and Evolutionary Computation Conference (GECCO '26), July 13–17, 2026, San Jose, Costa Rica. The arXiv ID is 2603.28653, with authors Kaushitha Silva and Srinath Perera.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94d03dfc-b648-4f7c-b65d-0a951e3a8ec7",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "7576dba0-a197-47c9-9772-2a7304242fba",
  "toolUseResult": {
    "query": "BACE Bayesian anchored co-evolution code test arXiv 2603.28653 GECCO 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TqGuJLyvt8hb8b1z3w4Pdw",
        "content": [
          {
            "title": "BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations",
            "url": "https://arxiv.org/html/2603.28653"
          },
          {
            "title": "[2603.28653] BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations",
            "url": "https://arxiv.org/abs/2603.28653"
          },
          {
            "title": "(PDF) BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations",
            "url": "https://www.researchgate.net/publication/403307603_BACE_LLM-based_Code_Generation_through_Bayesian_Anchored_Co-Evolution_of_Code_and_Test_Populations"
          },
          {
            "title": "[2603.03233] AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework",
            "url": "https://arxiv.org/abs/2603.03233"
          },
          {
            "title": "[2603.03233v1] AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework",
            "url": "https://arxiv.org/abs/2603.03233v1"
          },
          {
            "title": "Computer Science",
            "url": "https://arxiv.org/list/cs/recent?skip=1398&show=1000"
          },
          {
            "title": "[2603.18104] Adaptive Domain Models: Bayesian Evolution, Warm Rotation, and Principled Training for Geometric and Neuromorphic AI",
            "url": "https://arxiv.org/abs/2603.18104"
          },
          {
            "title": "Artificial Intelligence Jun 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"
          },
          {
            "title": "April 12, 2026 References",
            "url": "https://iridia-ulb.github.io/references/testbib.pdf"
          },
          {
            "title": "Bayesian neural network with autoencoder for model- ...",
            "url": "https://arxiv.org/pdf/2603.07976"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n## BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations\n\nBACE (Bayesian Anchored Co-Evolution) is a framework that reformulates synthesis as a Bayesian co-evolutionary process where code and test populations are evolved, guided by belief distributions that are reciprocally updated based on noisy interaction evidence.\n\n**Key Problem Addressed:**\nLarge Language Models (LLMs) have demonstrated impressive capabilities in code generation. While an interactive feedback loop can improve performance, writing effective tests is a non-trivial task. Early multi-agent frameworks, such as AgentCoder, automated this process but relied on generated tests as absolute ground truth. This approach is fragile: incorrect code frequently passes faulty or trivial tests, while valid solutions are often degraded to satisfy incorrect assertions.\n\n**Core Innovation:**\nThe framework argues that generated tests remain a valuable signal if modeled as noisy sensors guided by bayesian updates. By anchoring this search on minimal public examples, BACE prevents the co-evolutionary drift typical of self-validating loops.\n\n**Results:**\nExtensive evaluations on LiveCodeBench v6 (post-March 2025) reveal that BACE achieves superior performance across both proprietary models and open-weight small language models.\n\n**Publication Details:**\nThe paper is published in the Genetic and Evolutionary Computation Conference (GECCO '26), July 13–17, 2026, San Jose, Costa Rica. The arXiv ID is 2603.28653, with authors Kaushitha Silva and Srinath Perera."
    ],
    "durationSeconds": 7.925035043000011
  },
  "sourceToolAssistantUUID": "94d03dfc-b648-4f7c-b65d-0a951e3a8ec7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-12T02:19:39.117Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DPQwYrPCWXNh6iojeJCzNs`</summary>

```json
{
  "query": "\"execution grounding\" specification \"code debugging\" OR \"code repair\" LLM precondition postcondition 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7576dba0-a197-47c9-9772-2a7304242fba",
  "isSidechain": false,
  "requestId": "req_011CawsfWB399uZFKppgoWGT",
  "type": "assistant",
  "uuid": "8d1c1b0e-46b6-44f0-9a3f-cea06882b746",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rzw8xd2rW8G9JQZ6Ycgx9A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2625,
      "cache_read_input_tokens": 72161,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 72161,
          "cache_creation_input_tokens": 2625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2625
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

_source line 97 · 2026-05-12T02:19:48.083Z_

<details><summary>↩ Tool result · `toolu_01DPQwYrPCWXNh6iojeJCzNs`</summary>

```text
Web search results for query: ""execution grounding" specification "code debugging" OR "code repair" LLM precondition postcondition 2025 2026"

Links: [{"title":"Automatic Generation of Formal Specification and ...","url":"https://arxiv.org/pdf/2601.12845"},{"title":"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation","url":"https://openreview.net/pdf?id=6pr7BUGkLp"},{"title":"Beyond Postconditions: Can Large Language Models infer Formal Contracts for","url":"https://arxiv.org/pdf/2510.12702"},{"title":"Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis","url":"https://arxiv.org/html/2604.10800v1"},{"title":"Large Language Model Powered Symbolic Execution","url":"https://mengrj.github.io/pdfs/autobug-oopsla25.pdf"},{"title":"Code Repair with LLMs gives an Exploration-Exploitation Tradeoff Hao Tang","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/d5c56ec4f69c9a473089b16000d3f8cd-Paper-Conference.pdf"},{"title":"LADYBUG: an LLM Agent DeBUGger for data-driven applications Joel Rorseth","url":"https://openproceedings.org/2025/conf/edbt/paper-313.pdf"},{"title":"Revisit Self-Debugging with Self-Generated Tests for Code ...","url":"https://aclanthology.org/2025.acl-long.881.pdf"},{"title":"Hoare Logic for Code and Cloud: What 1969 Computer Science Offers 2026 Engineering","url":"https://zircon.tech/blog/hoare-logic-for-code-and-cloud-what-1969-computer-science-offers-2026-engineering/"},{"title":"Automated Generation of Code Contracts – Generative AI to the Rescue?","url":"https://scg.unibe.ch/archive/papers/Grei24a-CodeContracts.pdf"}]

Based on my web search, I found several relevant papers and resources addressing execution grounding, code specification, code debugging/repair, and LLMs with preconditions and postconditions from 2025-2026:

## Key Research Findings

**Execution Grounding for Code Analysis:**
A recent paper titled "Verify Before You Fix" implements a plan-execute-verify reasoning loop that converts probabilistic detector outputs into binary, execution-backed verdicts, with an LLM planner generating structured exploit hypotheses specifying attack vectors, concrete payloads, and environmental preconditions.

**LLM-Based Formal Specification Generation:**
The NL2Contract task involves employing LLMs to translate informal natural language into formal functional contracts consisting of postconditions as well as preconditions, with metrics to validate soundness and bug discriminative power.

**Specification and Verification Annotations:**
Research addresses how effectively current LLMs can generate specification and verification annotations (preconditions, postconditions, loop invariants, and proof helpers) to successfully verify programs.

**Model-Authored Specifications:**
The Self-Spec framework allows models to design their own specification schema, populate it from natural language and function signatures, run a minimal interviewer loop to resolve unknowns, and then generate code only from that contract.

**LLM-Based Symbolic Execution:**
AutoBug represents an LLM-based symbolic execution engine for real-world programming languages such as C/Java/Python.

**Self-Debugging with Execution Feedback:**
Self-debugging approaches have models generate initial programs along with test suites based on problem descriptions, with programs executed on self-generated tests to provide feedback.

These recent works demonstrate active research combining LLMs with formal specification, execution-based verification, code repair, and precondition/postcondition reasoning for 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d1c1b0e-46b6-44f0-9a3f-cea06882b746",
  "isSidechain": false,
  "promptId": "b6c9be92-a053-41ab-9cd1-984ff72d3bc9",
  "type": "user",
  "uuid": "5837c88e-a53a-44c7-87c2-343f6aaf9a2a",
  "toolUseResult": {
    "query": "\"execution grounding\" specification \"code debugging\" OR \"code repair\" LLM precondition postcondition 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HTqdibRXYZbaWjF5gPKqRa",
        "content": [
          {
            "title": "Automatic Generation of Formal Specification and ...",
            "url": "https://arxiv.org/pdf/2601.12845"
          },
          {
            "title": "Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation",
            "url": "https://openreview.net/pdf?id=6pr7BUGkLp"
          },
          {
            "title": "Beyond Postconditions: Can Large Language Models infer Formal Contracts for",
            "url": "https://arxiv.org/pdf/2510.12702"
          },
          {
            "title": "Verify Before You Fix: Agentic Execution Grounding for Trustworthy Cross-Language Code Analysis",
            "url": "https://arxiv.org/html/2604.10800v1"
          },
          {
            "title": "Large Language Model Powered Symbolic Execution",
            "url": "https://mengrj.github.io/pdfs/autobug-oopsla25.pdf"
          },
          {
            "title": "Code Repair with LLMs gives an Exploration-Exploitation Tradeoff Hao Tang",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/d5c56ec4f69c9a473089b16000d3f8cd-Paper-Conference.pdf"
          },
          {
            "title": "LADYBUG: an LLM Agent DeBUGger for data-driven applications Joel Rorseth",
            "url": "https://openproceedings.org/2025/conf/edbt/paper-313.pdf"
          },
          {
            "title": "Revisit Self-Debugging with Self-Generated Tests for Code ...",
            "url": "https://aclanthology.org/2025.acl-long.881.pdf"
          },
          {
            "title": "Hoare Logic for Code and Cloud: What 1969 Computer Science Offers 2026 Engineering",
            "url": "https://zircon.tech/blog/hoare-logic-for-code-and-cloud-what-1969-computer-science-offers-2026-engineering/"
          },
          {
            "title": "Automated Generation of Code Contracts – Generative AI to the Rescue?",
            "url": "https://scg.unibe.ch/archive/papers/Grei24a-CodeContracts.pdf"
          }
        ]
      },
      "Based on my web search, I found several relevant papers and resources addressing execution grounding, code specification, code debugging/repair, and LLMs with preconditions and postconditions from 2025-2026:\n\n## Key Research Findings\n\n**Execution Grounding for Code Analysis:**\nA recent paper titled \"Verify Before You Fix\" implements a plan-execute-verify reasoning loop that converts probabilistic detector outputs into binary, execution-backed verdicts, with an LLM planner generating structured exploit hypotheses specifying attack vectors, concrete payloads, and environmental preconditions.\n\n**LLM-Based Formal Specification Generation:**\nThe NL2Contract task involves employing LLMs to translate informal natural language into formal functional contracts consisting of postconditions as well as preconditions, with metrics to validate soundness and bug discriminative power.\n\n**Specification and Verification Annotations:**\nResearch addresses how effectively current LLMs can generate specification and verification annotations (preconditions, postconditions, loop invariants, and proof helpers) to successfully verify programs.\n\n**Model-Authored Specifications:**\nThe Self-Spec framework allows models to design their own specification schema, populate it from natural language and function signatures, run a minimal interviewer loop to resolve unknowns, and then generate code only from that contract.\n\n**LLM-Based Symbolic Execution:**\nAutoBug represents an LLM-based symbolic execution engine for real-world programming languages such as C/Java/Python.\n\n**Self-Debugging with Execution Feedback:**\nSelf-debugging approaches have models generate initial programs along with test suites based on problem descriptions, with programs executed on self-generated tests to provide feedback.\n\nThese recent works demonstrate active research combining LLMs with formal specification, execution-based verification, code repair, and precondition/postcondition reasoning for 2025-2026."
    ],
    "durationSeconds": 8.961670698000002
  },
  "sourceToolAssistantUUID": "8d1c1b0e-46b6-44f0-9a3f-cea06882b746",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 98_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "5837c88e-a53a-44c7-87c2-343f6aaf9a2a",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Runtime record

_source line 99_

```json
{
  "type": "ai-title",
  "aiTitle": "ExeSpec: Execution-grounded Behavioral Specifications for Code LLMs",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Assistant

_source line 100 · 2026-05-12T02:20:41.810Z_

I now have sufficient evidence to form my assessment. Let me compile the review.

**Key findings from my independent verification:**

1. **PGS v2 (May 1, 2026) now evaluates on 5 benchmarks** including CodeContests and SWE-bench — the idea falsely claims PGS doesn't cover these.
2. **PGS v2 property accuracy numbers differ** from what the idea cites: v2 reports generation accuracy of 90.6%/67.6%/32.4% (easy/medium/hard), not 82.4%/62.8%/48.9%.
3. **PGS v2 uses 6 models** including Qwen3-30B, DeepSeek-V3.1, and Claude-Sonnet-4.
4. All other cited papers (NL-Debugging, ContractEval, StoryCoder, BACE, etc.) verified as real.
5. EMNLP 2026 ARR deadline May 25 confirmed.
6. SWE-bench contamination concerns confirmed.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "PGS v2 (May 2026) now evaluates on CodeContests AND SWE-bench with 6 models including Qwen3-30B and Claude-Sonnet-4, directly contradicting the idea's claim that 'PGS does not evaluate on CodeContests, SWE-bench, or debugging benchmarks.' This substantially narrows ExeSpec's novelty—the remaining differentiators (execution grounding of specs, debugging/DebugBench, component decomposition, cross-file completion) are valid but incremental over PGS v2's expanded scope."},
    "feasibility": {"score": 3, "rationale": "Manual timeline of 18–22 days exceeds the user's hard constraint of ≤16 days. Even HIL at 14–18 days barely fits. PGS v2's expanded benchmark coverage means reimplementing PGS as a baseline is more complex than anticipated—PGS v2 already covers CodeContests and SWE-bench with Qwen2.5-Coder, making faithful reimplementation both more important and more labor-intensive. Spec quality bootstrapping risk (CodeSpecBench 20.2% repo-level, PGS v2 shows 32.4% generation accuracy on hard problems) remains underaddressed for CrossCodeEval/RepoBench tasks."},
    "clarity": {"score": 4, "rationale": "The experimental design with six controlled conditions and honest ablation (the I/O-only critical test) is genuinely well-specified. The narrative structure is clear despite being dense. However, the factual errors about PGS v2 undermine the paper's positioning credibility—EMNLP reviewers who have read PGS v2 will immediately notice."},
    "impact": {"score": 3, "rationale": "If execution grounding provides meaningful gains over PGS v2 on shared benchmarks (CodeContests, SWE-bench), this is a useful contribution. But PGS v2's expanded scope means the impact ceiling is lower than presented—this is more likely an EMNLP Findings paper than Main Conference unless the execution grounding and debugging results are compelling."}
  },
  "issues": [
    "CRITICAL FACTUAL ERROR — PGS v2 BENCHMARK COVERAGE: The idea states 'PGS does not evaluate on CodeContests, SWE-bench, or debugging benchmarks' (landscape section) and 'evaluation spans four task types on benchmarks PGS does not cover (CodeContests, SWE-bench Pro, DebugBench)' (approach section). PGS v2 (revised May 1, 2026, title 'Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback') evaluates on FIVE benchmarks: HumanEval, MBPP, LiveCodeBench, CodeContests, AND SWE-bench. On CodeContests with Qwen2.5-Coder: PGS achieves ~22.4% pass@1 vs. baseline ~15%. On SWE-bench with Qwen2.5-Coder: PGS achieves ~12.8% vs. baseline ~10%. PGS v2 uses 6 models including Qwen3-30B, DeepSeek-V3.1, and Claude-Sonnet-4. The idea claims awareness of the v2 revision ('revised May 2026') but bases its differentiation on v1's benchmark scope. This invalidates one of ExeSpec's three claimed differentiators and must be corrected.",
    "CRITICAL — PGS PROPERTY ACCURACY NUMBERS ARE INCORRECT: The idea cites 'property generation accuracy of 82.4% (easy), 62.8% (medium), and 48.9% (hard) on LiveCodeBench.' PGS v2 Table 2 reports property GENERATION accuracy of 90.6% (easy), 67.6% (medium), 32.4% (hard), with VERIFICATION accuracy of 93.8%/91.2%/76.5%. Neither metric matches the idea's cited numbers. The hard-problem generation accuracy (32.4%) is actually WORSE than claimed (48.9%), which ironically strengthens ExeSpec's motivation—but the numbers must be corrected for credibility.",
    "TIMELINE VIOLATION: The manual estimate of 18–22 days exceeds the user's hard constraint of ≤16 days. The HIL estimate of 14–18 days barely fits at the low end. The idea should scope to fit within 16 days—either by using the HIL/auto mode as the primary plan or by reducing scope (e.g., dropping one supplementary benchmark).",
    "NOVELTY REPOSITIONING NEEDED: With PGS v2 covering CodeContests and SWE-bench, ExeSpec's narrative must shift from 'extending PGS to new benchmarks' to 'improving upon PGS via execution grounding on shared benchmarks (catching hallucinated specs that PGS misses) + extending to genuinely new tasks (debugging on DebugBench, cross-file completion on CrossCodeEval/RepoBench) + providing component-level decomposition PGS lacks.' The remaining differentiators are valid: (1) execution grounding catches internally inconsistent specs (PGS validates against public tests but doesn't check inter-property consistency), (2) DebugBench evaluation (PGS doesn't cover debugging), (3) 5-component decomposition with ablation, (4) SWE-bench Pro (contamination-resistant vs. PGS's standard SWE-bench), (5) cross-file completion. But the narrative must be honest about overlap.",
    "PGS BASELINE COMPARISON MORE COMPLEX THAN ACKNOWLEDGED: PGS v2 already reports Qwen2.5-Coder results on CodeContests and SWE-bench. Rather than reimplementing PGS from scratch, ExeSpec should cite PGS v2's published numbers as the baseline on these benchmarks (with appropriate caveats about experimental setup differences), and reimplement PGS only for DebugBench/CrossCodeEval where PGS has no published numbers. This saves significant implementation time and avoids the risk of a strawmanned reimplementation.",
    "MODEL CURRENCY GAP WIDENED: PGS v2 uses Qwen3-30B, DeepSeek-V3.1, and Claude-Sonnet-4 alongside Qwen2.5-Coder. ExeSpec uses only Qwen2.5-Coder-7B/32B. While the method is model-agnostic and using Qwen2.5-Coder enables model-controlled comparison with PGS v2, EMNLP reviewers may question why ExeSpec doesn't also evaluate on at least one newer model. Consider adding one data point with Qwen3-30B (used by PGS v2) on a primary benchmark."
  ],
  "feedback": "The idea has improved dramatically over 8 rounds — PGS is finally cited, NL-Debugging is a baseline, ContractEval motivates execution grounding, the experimental design is rigorous, and the honest ablation commitment is the proposal's strongest feature. However, a critical factual error undermines the paper's positioning: PGS v2 (May 1, 2026) now evaluates on CodeContests AND SWE-bench, directly contradicting the idea's central differentiator claim. Here is exactly what must change:\n\n1. **CORRECT PGS v2 CLAIMS** (non-negotiable): Update the landscape section to accurately reflect PGS v2's benchmark coverage (5 benchmarks: HumanEval, MBPP, LiveCodeBench, CodeContests, SWE-bench) and model coverage (6 models including Qwen3-30B and Claude-Sonnet-4). Fix the property accuracy numbers to match v2's Table 2 (generation: 90.6%/67.6%/32.4%; verification: 93.8%/91.2%/76.5%). Note that the 32.4% generation accuracy on hard problems actually STRENGTHENS ExeSpec's execution-grounding motivation.\n\n2. **REPOSITION NOVELTY**: Reframe from 'extending PGS to new benchmarks' to: (a) 'Execution grounding catches internally inconsistent and hallucinated specs that PGS's public-test validation misses—particularly critical given PGS v2's 32.4% generation accuracy on hard problems'; (b) 'Extending property-based reasoning to debugging (DebugBench) and cross-file completion (CrossCodeEval/RepoBench)—task types PGS v2 still does not cover'; (c) 'Component-level decomposition revealing which spec types help which tasks—PGS treats properties monolithically'; (d) 'SWE-bench Pro for contamination-resistant evaluation vs. PGS's standard SWE-bench.'\n\n3. **USE PGS v2 PUBLISHED NUMBERS**: On CodeContests and SWE-bench, cite PGS v2's published Qwen2.5-Coder results as the baseline rather than reimplementing from scratch. Reimplement PGS only for DebugBench and CrossCodeEval where PGS v2 has no numbers. This saves time and avoids strawmanning.\n\n4. **FIT TIMELINE TO 16 DAYS**: Either (a) commit to HIL mode with reduced scope (3 primary benchmarks with full baselines, 3 supplementary with ExeSpec vs. direct only), or (b) leverage PGS v2's published numbers to reduce reimplementation effort. The manual 18–22 day estimate violates the user's constraint.\n\n5. **CONSIDER ADDING ONE NEWER MODEL**: PGS v2 uses Qwen3-30B. Adding one data point on a primary benchmark would demonstrate model-agnostic applicability and enable direct comparison with PGS v2's newer-model results.\n\nThe core value proposition—execution grounding to catch the 67.6% of hard-problem specs that PGS's generation gets wrong—remains strong. But the paper must be honest about where PGS v2 has already gone and position ExeSpec's contributions accurately.",
  "reason": "PGS v2 (May 2026) now evaluates on CodeContests AND SWE-bench with 6 models—the idea's central differentiator claim ('PGS does not evaluate on CodeContests, SWE-bench') is factually incorrect and must be corrected, with novelty repositioned around execution grounding, debugging extension, and component decomposition."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5837c88e-a53a-44c7-87c2-343f6aaf9a2a",
  "isSidechain": false,
  "requestId": "req_011CawsgRsMhRoky6nL2z2Bq",
  "type": "assistant",
  "uuid": "3bfe441e-49dc-4a16-9f4a-fdb385171bbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019SShyyLWJ2G6j5VLqCFgi9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 74786,
      "output_tokens": 2826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1063,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2826,
          "cache_read_input_tokens": 74786,
          "cache_creation_input_tokens": 1063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1063
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

_source line 101_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3bfe441e-49dc-4a16-9f4a-fdb385171bbf",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---

### Runtime record

_source line 102_

```json
{
  "type": "ai-title",
  "aiTitle": "ExeSpec: Execution-grounded Behavioral Specifications for Code LLMs",
  "sessionId": "9785eb62-9283-4705-9db2-c7b83aec5cc9"
}
```

---
