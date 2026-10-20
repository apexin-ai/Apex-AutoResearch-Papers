# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-11 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/9dc8ea75-e85f-4dda-a834-b95c01def98c.jsonl`
- **Structured JSON:** [`c96035366d38a4b984f7.json`](../../sessions/c9/c96035366d38a4b984f7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T01:55:02.345Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T01:55:02.345Z",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-11 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 7/10)\n{\n  \"title\": \"ExeSpec: Verifiable Specification Reasoning for Code LLMs via Execution Grounding\",\n  \"core_problem\": \"Training-free inference-time methods for LLM code improvement—AlphaCodium (arXiv 2401.08500), CodeT (ICLR 2023), Self-Debugging (arXiv 2304.05128), S* (EMNLP 2025 Findings)—have demonstrated that execution feedback at inference time substantially boosts code generation quality. However, these methods uniformly treat test cases as their intermediate representation: they generate I/O test pairs, execute candidate code against them, and refine based on pass/fail signals. Tests are point samples—they verify specific inputs but do not capture behavioral intent (preconditions, postconditions, invariants, type constraints). This creates two limitations: (1) test-based methods provide pass/fail validation but not structured reasoning scaffolds that inform how code should behave across all inputs, and (2) they are largely restricted to code generation tasks where test generation is natural, without principled extension to debugging (where intended-vs-observed behavioral contrasts are needed), completion (where interface contracts must be inferred), or reasoning (where execution expectations must be formalized). Meanwhile, Self-Spec (Agents4Science 2025) showed that model-authored behavioral specifications improve generation (+2–5pp on HumanEval), but these specifications are never verified against execution—CodeSpecBench (arXiv 2604.12268) reveals only 20.2% success at repo-level spec generation, demonstrating that unverified LLM-generated specs are unreliable. Can execution-grounded behavioral specifications—richer than test cases, capturing universal behavioral properties—serve as verifiable structured intermediate reasoning that outperforms test-based refinement methods across diverse code tasks without model training?\",\n  \"opportunity\": \"Four research threads converge but remain disconnected: (1) Test-based inference-time refinement (AlphaCodium, CodeT, Self-Debugging, S*, BACE) proves execution feedback improves code generation—AlphaCodium's flow engineering raises CodeContests pass@5 from 19% to 44%, CodeT improves HumanEval pass@1 by +18.8pp via dual execution agreement, S* enables a 3B model to outperform GPT-4o-mini on LiveCodeBench—but all use test cases (point samples) as the intermediate representation, not property-level behavioral descriptions. (2) Specification-mediated reasoning (Self-Spec) demonstrates that LLM-authored specs improve generation by +2–5pp, establishing that structured behavioral intent aids code reasoning—but specs are never execution-verified, and 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025) shows that self-generated test feedback introduces systematic bias that degrades performance for some models, motivating richer intermediate representations beyond tests. (3) Execution-trace training (Think Like You Execute, RLEF at ICML 2025) achieves dramatic gains (+22–27pp) by grounding reasoning in execution, but requires fine-tuning on 54K+ verified rationales—not usable with frozen models. (4) CodeSpecBench reveals that LLMs achieve only 20.2% on repo-level spec generation, and SSDE (FSE Companion 2026) shows structured specs (Gherkin) can guide repo-level generation but requires human-authored specifications. The unexploited synthesis: use execution to verify LLM-generated behavioral specifications (pre/postconditions, invariants, type constraints—not just I/O pairs) at inference time, creating property-level reasoning scaffolds that capture universal behavioral intent rather than point samples. The key hypothesis: specifications provide fundamentally richer intermediate reasoning than tests because they describe what must hold for all inputs (universal properties) rather than what happens for specific inputs (existential examples), enabling the LLM to reason about behavioral correctness at a higher abstraction level.\",\n  \"landscape\": \"**Test-based inference-time methods.** AlphaCodium (arXiv 2401.08500, Jan 2024) is the most direct predecessor: a training-free multi-stage flow with problem reflection, AI test generation (6–8 diverse I/O pairs), and iterative execution-based refinement with test anchoring, achieving 44% pass@5 on CodeContests (vs. 19% direct prompting). Its pre-processing phase (problem reflection → public test reasoning → solution ranking → AI test generation) produces structured problem analysis in YAML format, and its code iteration phase uses test anchoring to prevent regression—fixes that break anchor tests are rejected. CodeT (ICLR 2023, arXiv 2207.10397) generates tests via LLMs and uses dual execution agreement (output consistency against generated tests + cross-sample agreement) for solution selection, improving HumanEval pass@1 by +18.8pp with code-davinci-002. Self-Debugging (arXiv 2304.05128, 2023) teaches LLMs to iteratively debug using execution results and natural language explanations (rubber-duck debugging), achieving up to 12% improvement on TransCoder and MBPP. 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025 Long, arXiv 2501.12793) reveals that post-execution self-debugging suffers from systematic bias in self-generated tests—in-execution debugging using intermediate program states mitigates this, demonstrating that test quality is a fundamental bottleneck for test-based methods. S* (EMNLP 2025 Findings, arXiv 2502.14382) combines parallel sampling (16 candidates) with sequential debugging and adaptive distinguishing input synthesis for execution-grounded selection, enabling a 3B model to outperform GPT-4o-mini and GPT-4o-mini+S* to outperform o1-preview by 3.7% on LiveCodeBench. BACE (GECCO 2026, arXiv 2603.28653) treats generated tests as noisy sensors via Bayesian updates, co-evolving code and test populations on LiveCodeBench v6, outperforming CodeSIM by +2.5–5.4pp. All these methods use test cases as the intermediate representation—point samples that verify specific inputs but don't capture universal behavioral properties.\\n\\n**Specification-based approaches.** Self-Spec (Agents4Science 2025) has LLMs author specification languages before code generation, improving GPT-4o HumanEval pass@1 from 87% to 92% (+5pp) and Claude 3.7 from 92% to 94% (+2pp), but only evaluates on single-function HumanEval, never verifies specs against execution, and doesn't extend beyond generation. SpecRover/AutoCodeRover-v2 (ICSE 2025) performs iterative NL specification inference for automated program repair, achieving 19.31% on SWE-bench (50%+ improvement over AutoCodeRover). VibeRepair (arXiv 2602.08263) translates code into NL behavioral specs for repair but specs are imprecise and hallucination-prone. SSDE (FSE Companion 2026, arXiv 2605.02455) uses Gherkin specifications and domain models for repo-level MVC generation—concurrent work demonstrating structured specs guide LLM generation, but requires human-authored specifications rather than LLM-generated and verified ones. CodeSpecBench (arXiv 2604.12268) benchmarks LLM spec generation showing only 20.2% repo-level pass rate, motivating execution-based verification of LLM-generated specs.\\n\\n**Execution-grounded training methods.** Think Like You Execute (arXiv 2512.00127) achieves +22–27pp on CRUXEval/LiveCodeBench via fine-tuning on 54K execution-trace-verified rationales. EG-CFG (NeurIPS 2025, arXiv 2506.10948) uses real-time execution via beam search over candidate lines—computationally expensive and generation-only. RLEF (ICML 2025) trains code LLMs with RL execution feedback. Think Anywhere (arXiv 2603.29957) enables on-demand reasoning during code generation via RL training, achieving 70.3% average across four benchmarks. CURE (NeurIPS 2025 Spotlight) co-evolves coder and tester via RL. All require training—not applicable with frozen models.\\n\\n**Other relevant work.** SCoT (ACL 2024) adds program structure to CoT without execution grounding. Test overfitting studies show 21.8–35.9% of LLM patches overfit visible tests (arXiv 2511.16858), and ICSE 2026 NIER proves overfitting is undecidable without full specifications—motivating property-level specs as reasoning scaffolds.\\n\\n**The gap.** Existing training-free methods use tests (point samples) for validation. No work uses property-level behavioral specifications (pre/postconditions, invariants, type constraints) as execution-grounded structured intermediate reasoning in a training-free framework, with controlled evidence that property-level specs outperform test-based refinement across diverse code tasks.\",\n  \"approach\": \"We propose ExeSpec, a training-free inference-time framework that uses execution-grounded behavioral specifications as verifiable structured intermediate reasoning for LLM code tasks. The critical distinction from test-based methods (AlphaCodium, CodeT, S*) is that ExeSpec generates property-level behavioral descriptions—universal constraints about what code must satisfy for all inputs—rather than point-sample test cases that verify specific I/O pairs. This provides richer reasoning scaffolds: knowing 'f(x) returns 2x for all non-negative integers, raises ValueError for negative inputs' (specification) enables different reasoning than knowing 'f(5)=10, f(3)=6' (tests).\\n\\n**Stage 1: Spec Elicitation.** Given a task input, prompt the LLM to generate structured behavioral specifications in a lightweight JSON schema containing five component types: (a) I/O example pairs (shared with test-based methods—this is the overlap with AlphaCodium), (b) preconditions (constraints on valid inputs/states, e.g., 'n >= 0', 'input list is non-empty'), (c) postconditions (properties guaranteed on outputs, e.g., 'output is sorted in ascending order', 'len(output) == len(input)'), (d) type constraints (parameter and return type annotations with generics, e.g., 'List[int] -> int'), and (e) invariants (loop invariants, monotonicity, ordering properties, e.g., 'partial_sum increases monotonically'). The schema is task-adapted: generation tasks derive specs from docstrings and problem descriptions; debugging tasks elicit intended-vs-observed behavioral contrasts (the spec says the output should be sorted, but the code produces [3,1,2]); issue resolution tasks extract expected behavioral changes from issue descriptions and failing test context.\\n\\n**Stage 2: Execution Grounding.** Validate and refine specifications by executing lightweight probes against available code context, catching hallucinated or contradictory specs before they corrupt downstream reasoning. For generation tasks: generate a quick candidate solution, execute against spec-derived assertions—both I/O examples (like AlphaCodium) AND postcondition property checks (e.g., assert all(output[i] <= output[i+1] for i in range(len(output)-1)) for a sorting postcondition)—identify spec-execution mismatches, and revise contradicted specs. For debugging tasks: execute the buggy code, compare execution traces against specs to identify precisely which behavioral constraints (not just which test cases) are violated, producing structured violation reports (e.g., 'postcondition violated: output should be sorted but is [3,1,2]; invariant violated: partial_sum is not monotonically increasing at iteration 3'). For issue resolution (SWE-bench): extract behavioral expectations from issue descriptions and failing tests, generate specs characterizing the intended fix behavior, and validate spec consistency against the existing test suite via Docker-based execution. When full execution is unavailable, static grounding serves as fallback: cross-spec consistency checking (e.g., precondition implies postcondition is satisfiable), type inference from signatures, and contradiction detection across spec components.\\n\\n**Stage 3: Spec-Guided Task Completion.** Feed grounded specs alongside the original task input to the LLM for final output. The model reasons about behavioral intent (what the code should do per verified property-level specs) rather than surface patterns. When outputs violate specs, structured violation reports (which constraints failed, expected vs. actual, which spec component) feed back for iterative refinement (up to 3 rounds). The key difference from test-based iteration (AlphaCodium): violation reports reference behavioral properties ('postcondition: output must be monotonically increasing'), not just I/O failures ('test case 3 failed'), giving the LLM richer corrective signal.\\n\\n**Baselines and controlled experiments.** The experimental design explicitly isolates the spec-vs-test distinction through four controlled conditions: (a) ExeSpec full (property-level specs + execution grounding), (b) AlphaCodium-style baseline (problem reflection + AI test generation + iterative execution/refinement, no property-level specs)—this directly tests whether specs provide gains beyond test-based refinement and is the paper's critical comparison, (c) Self-Spec baseline (specs without execution grounding)—tests the contribution of grounding, (d) direct prompting (no intermediate reasoning). The delta between (a) and (b) is the paper's core contribution. Additionally, a controlled spec-component ablation isolates the value of each spec type: (i) full specs (I/O + pre/postconditions + invariants + type constraints), (ii) I/O-only specs (functionally equivalent to AlphaCodium's AI test cases—the overlap region), (iii) structural specs only (pre/postconditions + invariants + type constraints, no I/O examples). If (ii) performs similarly to (i), the novelty claim is weakened—this ablation is the critical honesty test for the paper. S* is positioned as complementary (parallel/sequential scaling with execution-based selection) and could be combined with ExeSpec's spec-mediated reasoning; we note this in Related Work and Future Work but do not implement the combination.\\n\\n**Benchmarks.** Primary benchmarks with full baselines (all four conditions + spec-component ablation): DebugBench (C++/Java/Python debugging—specs naturally capture intended-vs-observed behavioral contrasts, the task type most differentiated from test-only methods), CodeContests (competitive programming—direct comparison to AlphaCodium on its home turf, using the same benchmark), and SWE-bench Verified (real-world issue resolution with Docker-based test execution—noting contamination concerns per OpenAI's 2026 audit, we report held-out test pass rates alongside standard metrics). Supplementary benchmarks with ExeSpec vs. direct prompting only: HumanEval+/MBPP+ (for Self-Spec comparability only, not primary given frontier models score 93%+), CrossCodeEval and RepoBench (cross-file completion with static grounding). For supplementary cross-file completion benchmarks, ExeSpec relies on static grounding: extracting type signatures from imported modules, inferring parameter/return types from usage context at call sites, and validating completions via type checkers (mypy/pyright for Python, tsc for TypeScript). We explicitly acknowledge this is weaker grounding than dynamic execution and report the proportion of instances where only static grounding was available.\\n\\n**Analysis.** Beyond standard metrics, we report: (1) spec quality analysis—correlation between spec correctness (measured by agreement with ground-truth behavior) and downstream task performance; (2) grounding effectiveness—proportion of hallucinated specs caught by execution grounding vs. passing through undetected; (3) spec-component contribution—which spec types (I/O, preconditions, postconditions, invariants, type constraints) most improve each task type; (4) test overfitting rates—proportion of solutions passing visible tests but failing held-out tests, comparing ExeSpec vs. baselines (addressing ICSE 2026 undecidability concern); (5) qualitative case studies showing where property-level specs enable corrections that test-only methods miss (e.g., off-by-one errors caught by ordering invariants but missed by finite test cases, type constraint violations caught by postcondition checks).\\n\\nAll experiments use Qwen2.5-Coder-7B-Instruct and Qwen2.5-Coder-32B-Instruct via vLLM batch inference on H100 GPUs, with SWE-bench evaluation using the existing Docker harness.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~100–150 H100-hours (primary benchmarks DebugBench + CodeContests + SWE-bench Verified with 4 conditions × 2 models + spec-component ablation on primary benchmarks; supplementary HumanEval+/MBPP+ + CrossCodeEval + RepoBench with ExeSpec vs. direct prompting × 2 models; using vLLM batch inference with Qwen2.5-Coder-7B on 1 H100 and 32B on 1–2 H100s)\",\n      \"gpu_utilization\": \"Moderate (~40–55%): alternating between inference bursts and execution-grounding phases (running generated code against assertions, Docker-based test execution for SWE-bench); execution harness is CPU-bottlenecked while GPU idles during test runs\",\n      \"timeline\": \"14–18 days (days 1–3: framework implementation + AlphaCodium-style baseline reimplementation using open-source AlphaCodium code + eval harness setup leveraging existing SWE-bench Docker harness, EvalPlus, and benchmark repositories; days 4–7: primary benchmarks DebugBench + CodeContests with all 4 conditions; days 8–10: SWE-bench Verified with all 4 conditions; days 11–12: supplementary benchmarks HumanEval+/MBPP+ + CrossCodeEval + RepoBench with ExeSpec vs. direct prompting; days 13–15: spec-component ablation on DebugBench + CodeContests + analysis; days 16–18: writing)\",\n      \"team\": \"2 researchers (1 lead for ExeSpec framework + spec-grounding pipeline + spec-component ablation design, 1 for AlphaCodium baseline adaptation from open-source code + benchmark integration + evaluation infrastructure)\",\n      \"estimated_gpu_cost\": \"$300–450 (on-demand H100 at ~$3/hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~120–170 H100-hours (same scope as manual with more systematic spec quality validation and additional analysis iterations)\",\n      \"gpu_utilization\": \"Moderate–High (~50–65%): agent queues experiment batches across benchmarks while human reviews spec quality between rounds\",\n      \"timeline\": \"10–14 days (agent handles framework code, experiment orchestration, and result collection; human validates spec schema design, reviews AlphaCodium baseline fidelity, and guides ablation priorities)\",\n      \"team\": \"1 researcher, ~2–3 hrs/day reviewing spec elicitation outputs, validating AlphaCodium baseline implementation matches the published flow, approving experiment plans, and analyzing spec-component ablation results\",\n      \"claude_api_cost\": \"$100–200 (1000–2000 orchestration turns at ~$0.10/turn for code generation, experiment design, and result analysis)\",\n      \"estimated_gpu_cost\": \"$360–510\",\n      \"risk_note\": \"AlphaCodium baseline reimplementation fidelity is a key risk—must reproduce the core flow (problem reflection + AI test generation + iterative execution with test anchoring) faithfully; recommend using AlphaCodium's open-source code (github.com/Codium-ai/AlphaCodium) as starting point and adapting for non-CodeContests benchmarks (DebugBench, SWE-bench)\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~150–200 H100-hours (systematic sweeps over spec granularity levels, grounding strategies per benchmark, additional model backbone DeepSeek-Coder-V2-Lite-16B, temperature and sample-count variations)\",\n      \"gpu_utilization\": \"High (~80–90%): agent pipelines experiments back-to-back with minimal idle; parallel runs across benchmarks on multiple H100s\",\n      \"timeline\": \"6–9 days with 4–8 H100s available concurrently (bottlenecked by SWE-bench Docker container builds and sequential test execution per instance)\",\n      \"team\": \"0 (initial setup ~3–4 hours for benchmark harness configuration, AlphaCodium baseline setup from open-source code, and vLLM model serving, then fully autonomous)\",\n      \"claude_api_cost\": \"$200–400 (2000–4000 turns for iterative experiment design, spec schema optimization, cross-benchmark analysis, and paper section drafting)\",\n      \"estimated_gpu_cost\": \"$450–600\",\n      \"speed_bottleneck\": \"SWE-bench Verified Docker-based test execution (sequential per instance, ~2–5 min per task including container setup) and DebugBench compilation/execution harness; inference itself is fast with vLLM on H100\",\n      \"risk_note\": \"Agent may over-optimize spec schema for one benchmark at the expense of others; need guardrails to ensure the AlphaCodium baseline is faithfully implemented (using open-source code, not strawmanned) and that the spec-component ablation is run completely even if early results are unfavorable\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission May 25, 2026; commitment Aug 2, 2026; NLP and Code Models track; Budapest, Hungary)\",\n    \"ACL 2027 (expected ARR commitment ~Jan 2027; fallback if EMNLP revision needed)\",\n    \"NAACL 2027 (expected ARR commitment ~Mar 2027; second fallback)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"AlphaCodium: Code Generation through Flow Engineering (arXiv 2401.08500, Jan 2024)\",\n    \"CodeT: Code Generation with Generated Tests (ICLR 2023, arXiv 2207.10397)\",\n    \"Teaching Large Language Models to Self-Debug (Self-Debugging; arXiv 2304.05128, 2023)\",\n    \"Revisit Self-Debugging with Self-Generated Tests for Code Generation (ACL 2025 Long, arXiv 2501.12793)\",\n    \"S*: Test Time Scaling for Code Generation (EMNLP 2025 Findings, arXiv 2502.14382)\",\n    \"BACE: Bayesian Anchored Co-Evolution of Code and Test Populations (GECCO 2026, arXiv 2603.28653)\",\n    \"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation (Agents4Science 2025)\",\n    \"Execution Guided Line-by-Line Code Generation (EG-CFG; NeurIPS 2025, arXiv 2506.10948)\",\n    \"Think Like You Execute: Verifiable Chain of Thought from Program Traces (arXiv 2512.00127)\",\n    \"Think Anywhere in Code Generation (arXiv 2603.29957, Mar 2026)\",\n    \"SpecRover: Code Intent Extraction via LLMs (ICSE 2025)\",\n    \"CURE: Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning (NeurIPS 2025 Spotlight)\",\n    \"Code Execution as Grounded Supervision for LLM Reasoning (EMNLP 2025)\",\n    \"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (arXiv 2604.12268, Apr 2026)\",\n    \"Specification Vibing for Automated Program Repair (VibeRepair; arXiv 2602.08263, Feb 2026)\",\n    \"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering (SSDE; FSE Companion 2026, arXiv 2605.02455)\",\n    \"Investigating Test Overfitting on SWE-bench (arXiv 2511.16858)\",\n    \"The Undecidability of Overfitting in Automated Program Repair (ICSE 2026 NIER)\",\n    \"RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning (ICML 2025)\",\n    \"Structured Chain-of-Thought Prompting for Code Generation (SCoT; ACL 2024)\",\n    \"Qwen2.5-Coder Technical Report (arXiv 2409.12186)\"\n  ],\n  \"description\": \"We propose ExeSpec, a training-free inference-time framework that uses execution-grounded behavioral specifications as verifiable structured intermediate reasoning for LLM code tasks. The critical distinction from existing test-based methods (AlphaCodium, CodeT, Self-Debugging, S*) is that ExeSpec generates property-level behavioral descriptions—preconditions, postconditions, invariants, type constraints—that capture universal behavioral intent, rather than point-sample test cases that verify specific I/O pairs. The method operates in three stages: (1) Spec Elicitation—prompt the LLM to generate structured behavioral specifications (I/O examples, pre/postconditions, invariants, type constraints) in a JSON schema; (2) Execution Grounding—validate specs by executing lightweight probes (running candidate code against spec-derived property assertions, comparing buggy code behavior against intended specs, type-checking completion context), catching hallucinated specs before they corrupt reasoning; (3) Spec-Guided Completion—use grounded specs as verified intermediate reasoning with structured violation feedback for iterative refinement. The experimental design explicitly isolates the paper's contribution through four controlled conditions: (a) ExeSpec full (property-level specs + execution grounding), (b) AlphaCodium-style baseline (problem reflection + AI test generation + iterative execution/refinement, no property-level specs), (c) Self-Spec baseline (specs, no execution grounding), (d) direct prompting. The delta between (a) and (b) is the core contribution—whether property-level specs provide gains beyond test-based refinement. A critical spec-component ablation further decomposes: (i) full specs, (ii) I/O-only specs (≈ tests, AlphaCodium-equivalent), (iii) structural specs only (pre/postconditions + invariants, no I/O)—if (ii) ≈ (i), the novelty claim collapses, and we commit to reporting this honestly. Primary benchmarks with full baselines: DebugBench (debugging), CodeContests (competitive programming—AlphaCodium's home benchmark), SWE-bench Verified (issue resolution). Supplementary with ExeSpec vs. direct prompting only: HumanEval+/MBPP+ (Self-Spec comparability), CrossCodeEval/RepoBench (cross-file completion with static grounding via type checkers). S* is positioned as complementary (test-time scaling via execution-based selection); SSDE is concurrent work using human-authored Gherkin specs. All experiments use Qwen2.5-Coder-7B/32B-Instruct via vLLM on H100 GPUs. Within 100–150 H100-hours and ~16 days. Primary target: EMNLP 2026 (ARR May 25, 2026).\",\n  \"project_name\": \"test_spec_guided_repair\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL VENUE MISMATCH: User explicitly requested EMNLP 2026 (ARR deadline 2026-05-25, NLP and Code Models track), but the idea targets ICSE 2027, AAAI 2027, and FSE 2027 — all SE venues. The idea must be redesigned or reframed for EMNLP.\", \"CRITICAL COMPUTE VIOLATION: User constrained to ≤200 H100-hours total. The idea estimates 250-400 A100-80GB hours (manual mode). Running Kimi K2-Instruct (1T params MoE, requiring 4×A100 per instance) adds substantial inference costs not fully accounted for.\", \"CRITICAL TIMELINE VIOLATION: User has ~14 days. The idea estimates 3-5 months (manual), 6-10 weeks (HIL), or 1-3 weeks with 8-16 A100s (auto). None of these fit the user's constraint.\", \"EVAL BENCHMARK MISMATCH: User requested evaluation on SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, and CodeContests. The idea only covers SWE-bench Verified and Defects4J (which isn't even in the user's list). Missing 5 of 6 required benchmarks.\", \"MISSING CRITICAL RELATED WORK: (1) SpecRover/AutoCodeRover-v2 (ICSE 2025) — already does specification inference for patching; (2) CURE (NeurIPS 2025 Spotlight) — RL co-evolution of coder and tester; (3) CodeSpecBench (arXiv 2604.12268, Apr 2026) — benchmark showing LLMs achieve only 20.2% on repo-level behavioral spec generation; (4) Test overfitting undecidability (ICSE 2026 NIER) + empirical study (arXiv 2511.16858) showing 21-33% of LLM patches overfit on visible tests; (5) Dynamic Cogeneration at Google (arXiv 2601.19066); (6) SWE-Tester (arXiv 2601.13713).\", \"NOVELTY CONCERN: The idea is too similar to VibeRepair (arXiv 2602.08263, Feb 2026). VibeRepair already translates code into structured behavioral specifications for repair, achieving SOTA on Defects4J. The proposed delta — using test assertions instead of NL as the specification source — is an incremental variant, not a fundamentally new paradigm. SpecRover (ICSE 2025) also does specification inference for repair.\", \"TOPIC SCOPE TOO NARROW: User asked for 'code understanding and generation' covering repo-level comprehension, code reasoning, debugging, test generation, code-to-documentation, cross-language transfer. The idea focuses narrowly on Java program repair via Defects4J, which is only one subtask and one language.\", \"MISLEADING CLAIMS: '174/178 correct repairs' reads as a fraction but actually means 174 on v1.2 and 178 on v2.0. 'Proving specification-level repair is superior' overstates VibeRepair's own conclusions. The 48.29% for Repair-R1 represents only a 2.68pp improvement over baseline.\", \"TEST OVERFITTING NOT ADDRESSED: An ICSE 2026 NIER paper proves test overfitting is theoretically undecidable when full specifications are unavailable. An empirical study shows 21-33% of LLM patches overfit on visible tests. The idea's reliance on auto-generated tests as specifications is directly vulnerable to this fundamental limitation.\"]\nFeedback: This idea has a reasonable technical intuition (test assertions as behavioral specs) but fundamentally fails to meet the user's requirements. Here is what needs to change:\n\n1. **VENUE**: Reframe for EMNLP 2026 (NLP and Code Models track) or propose a different idea entirely. For EMNLP, the contribution must emphasize NLP methodology (e.g., how LLMs reason about code specifications, a new inference-time algorithm for code understanding) rather than SE pipeline engineering. EMNLP reviewers care about language model capabilities, not Defects4J leaderboard numbers.\n\n2. **SCOPE**: Broaden beyond Java program repair. The user wants 'code understanding and generation' covering multiple tasks (debugging, test generation, code reasoning, cross-language transfer). Consider a method that applies across multiple code tasks, not just APR.\n\n3. **BENCHMARKS**: Must evaluate on the user's required benchmarks: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests. Drop Defects4J (not requested).\n\n4. **COMPUTE**: Stay within ≤200 H100-hours. Use smaller models (DeepSeek-Coder-V2-Lite-Instruct 16B, StarCoder2-15B, Qwen2.5-Coder-7B/32B) as the user suggested, not 1T-param Kimi K2. This also aligns with the user's suggested model list.\n\n5. **TIMELINE**: Design for ≤16 days of execution. Build on existing frameworks (aider, SWE-agent, Moatless) as the user suggested. The current 3-5 month estimate is a non-starter.\n\n6. **NOVELTY BOOST**: Differentiate more clearly from VibeRepair and SpecRover. Instead of 'yet another spec-guided repair pipeline,' consider: (a) a novel inference algorithm that uses execution feedback to iteratively refine code understanding, (b) a retrieval-augmented approach with semantic code search for cross-repo transfer, or (c) a method for repo-level context compression that enables better code reasoning — all directions the user explicitly suggested.\n\n7. **ADDRESS TEST OVERFITTING**: Any test-based approach must engage with the ICSE 2026 undecidability result and the empirical overfitting findings. Propose concrete mitigation strategies.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MISSING CRITICAL BASELINES: AlphaCodium (arXiv 2401.08500, Jan 2024) is a training-free, inference-time, test-based iterative flow with problem analysis + AI test generation + iterative refinement against tests. It is the most direct conceptual predecessor to ExeSpec and MUST be cited and compared as a baseline. CodeT (ICLR 2022) and Self-Debugging (arXiv 2304.05128, 2023) are also missing—both are foundational works in execution-based code refinement at inference time.\", \"MISSING CONCURRENT WORK: BACE (arXiv 2603.28653, Mar 2026) addresses the same 'noisy self-generated tests' problem via Bayesian co-evolution of code and test populations. 'Revisit Self-Debugging with Self-Generated Tests' (arXiv 2501.12793, Jan 2025) directly studies post-execution vs. in-execution self-debugging paradigms with LLM-generated tests. Both must be discussed.\", \"THIN NOVELTY BOUNDARY: The distinction between 'structured behavioral specifications' (I/O example pairs, pre/postconditions, invariants in JSON schema) and 'self-generated test assertions' is conceptually thin. I/O examples ARE test cases. Pre/postconditions and invariants add something, but AlphaCodium's 'problem analysis' + 'edge case identification' phase also generates structured problem understanding before coding. The paper needs to sharpen why spec-mediated reasoning is fundamentally different from test-mediated refinement, with controlled experiments isolating this distinction.\", \"HUMANEVAL SATURATION: HumanEval+ and MBPP+ are listed as primary benchmarks, but frontier models already score 93%+ on HumanEval. Even with EvalPlus's harder tests, the benchmark is near saturation. The paper should emphasize DebugBench, CrossCodeEval, CodeContests, and SWE-bench Verified as primary evaluation, and use HumanEval+/MBPP+ only for comparability with Self-Spec.\", \"SPEC QUALITY BOOTSTRAPPING RISK: CodeSpecBench shows LLMs achieve only 20.2% on repo-level spec generation. If the LLM generates mostly bad specs, execution grounding catches them—but then the method degrades to 'generate specs → discard most → fall back to direct generation.' The paper needs analysis of what happens when spec generation quality is low (e.g., on CrossCodeEval/RepoBench repo-level tasks), including a failure mode analysis.\", \"TIMELINE IS VERY AGGRESSIVE: 12–16 days for implementing a 3-stage framework with task-adapted spec schemas, integrating 6 benchmarks (including SWE-bench Docker), running 48+ experiment configurations (6 benchmarks × 2 models × 4 baselines + ablations), AND writing a full paper. SWE-bench Verified Docker setup alone can take 2–3 days. Recommend reducing scope: run full comparison on 3 primary benchmarks (DebugBench, CodeContests, SWE-bench Verified) and use 3 others (HumanEval+/MBPP+, CrossCodeEval/RepoBench) for supplementary evaluation with fewer baselines.\", \"COST ESTIMATE MISSING API COSTS FOR EG-CFG BASELINE: Reproducing an EG-CFG-style execution-only baseline requires beam search with per-line execution, which is substantially more expensive than standard inference. This is either infeasible within budget or needs to be replaced with a simpler 'execution feedback without specs' baseline.\"]\nFeedback: The revision successfully addresses the critical venue, compute, and scope issues from Round 1. The idea is now properly scoped for EMNLP 2026 with correct benchmarks, models, and budget. However, several issues need resolution:\n\n1. **Sharpen novelty vs. AlphaCodium/CodeT**: These are the most important missing baselines. AlphaCodium (2024) already does training-free, multi-stage, test-based iterative refinement at inference time. ExeSpec must demonstrate that specification-mediated reasoning (structured I/O examples + pre/postconditions + invariants) provides gains BEYOND what test-based refinement alone achieves. Add a controlled experiment: (a) ExeSpec with full specs, (b) AlphaCodium-style test-only refinement, (c) Self-Spec without execution grounding, (d) direct prompting. The delta between (a) and (b) is the paper's core contribution.\n\n2. **De-emphasize saturated benchmarks**: Make DebugBench, CodeContests, and SWE-bench Verified the primary evaluation. Use HumanEval+/MBPP+ for Self-Spec comparability only. Consider adding LiveCodeBench for contamination resistance.\n\n3. **Address spec quality gracefully**: Add a spec quality analysis section showing: (a) what fraction of elicited specs survive execution grounding, (b) how grounding changes spec accuracy, (c) what happens when most specs fail (does the method degrade gracefully?). This directly responds to the CodeSpecBench 20.2% finding and strengthens the paper's analytical contribution.\n\n4. **Simplify the EG-CFG baseline**: Replace the full EG-CFG-style baseline (beam search + per-line execution) with a simpler 'execution feedback without specs' baseline: generate code → execute → feed error messages back → regenerate. This is cheaper and more directly tests the spec contribution.\n\n5. **Reduce timeline risk**: Implement the framework first on HumanEval+/MBPP+ (fast turnaround), validate the approach, then extend to harder benchmarks. Consider submitting to ARR May 25 with 4 benchmarks instead of 6, adding the remaining 2 for the camera-ready.\n\n6. **Cite and discuss**: AlphaCodium (2401.08500), CodeT (ICLR 2022), Self-Debugging (2304.05128), BACE (2603.28653), Revisit Self-Debugging (2501.12793). Position ExeSpec as advancing beyond test-only refinement by introducing verifiable specification reasoning as a structured intermediate representation.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL UNADDRESSED R2 FEEDBACK: AlphaCodium (arXiv 2401.08500, Jan 2024), CodeT (ICLR 2023), Self-Debugging (arXiv 2304.05128, 2023), BACE (arXiv 2603.28653, Mar 2026), and 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025, arXiv 2501.12793) are ALL still missing from key_references and baselines. Round 2 explicitly stated these MUST be cited and compared. AlphaCodium is the most direct conceptual predecessor — a training-free, multi-stage flow with problem reflection, test generation, and iterative execution-based refinement — and must be a baseline, not just a citation.\", \"NEW MISSING WORK — S* (EMNLP 2025 Findings, arXiv 2502.14382): A training-free test-time scaling framework for code generation that uses execution-based selection with adaptive distinguishing input synthesis. Enables a 3B model to outperform GPT-4o-mini. Published at EMNLP 2025 — the same venue being targeted. This is a highly relevant prior art that directly competes in the 'training-free inference-time code improvement' space.\", \"NEW MISSING CONCURRENT WORK — SSDE (arXiv 2605.02455, May 2026): 'LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering' uses Gherkin specifications and domain models to guide LLM generation with verification against test suites. Concurrent work that overlaps with ExeSpec's structured specification approach at the repo level.\", \"THIN NOVELTY BOUNDARY WITH ALPHACODIUM: AlphaCodium's pre-processing phase (problem reflection → public tests reasoning → possible solutions ranking) IS structured problem analysis before code generation. AlphaCodium's iterative phase (generate → execute → fix against public + AI tests) IS execution-grounded refinement. ExeSpec's I/O example specs are functionally identical to AlphaCodium's AI-generated test cases. The actual novelty delta — pre/postconditions, invariants, type constraints in JSON schema — must be isolated via controlled ablation: (a) ExeSpec full specs, (b) I/O-only specs (≈ test-only, AlphaCodium-style), (c) structural specs only (pre/postconditions + invariants without I/O). Without this, reviewers will reject for insufficient novelty.\", \"UNDERSPECIFIED NON-GENERATION TASKS: The approach for cross-file completion (CrossCodeEval, RepoBench) says 'type-check and partially execute the surrounding context to verify inferred specs.' This is vague. How do you generate behavioral specs for incomplete code in a multi-file context? What executable probes work for partial programs? CodeSpecBench shows only 20.2% success at repo-level spec generation — the method may degrade to fallback (soft grounding) for most repo-level instances, making the execution grounding contribution negligible on these benchmarks.\", \"HUMANEVAL+ STILL NOT DE-EMPHASIZED: Round 2 explicitly recommended making DebugBench, CodeContests, and SWE-bench Verified primary, with HumanEval+/MBPP+ for Self-Spec comparability only. The idea still lists them alongside other benchmarks without prioritization. Frontier models score 93%+ on HumanEval — gains here are not impressive.\", \"AGGRESSIVE TIMELINE NOT MITIGATED: Round 2 suggested reducing to 3 primary benchmarks + 3 supplementary. The idea still plans full comparison on all 6 benchmarks within 12–16 days. SWE-bench Docker setup alone takes 2–3 days. Recommend: primary (DebugBench, CodeContests, SWE-bench Verified) with full baselines; supplementary (HumanEval+/MBPP+, CrossCodeEval, RepoBench) with ExeSpec vs. direct prompting only.\"]\nFeedback: This is Round 3, and the idea has improved significantly from Round 1 (correct venue, benchmarks, compute budget) but has failed to address the MOST CRITICAL Round 2 feedback: citing and comparing against AlphaCodium, CodeT, Self-Debugging, BACE, and 'Revisit Self-Debugging.' This is not optional — these are the papers that define the competitive landscape for training-free, execution-based code improvement methods.\n\nHere is exactly what needs to change:\n\n1. **ADD ALPHACODIUM AS PRIMARY BASELINE** (non-negotiable): Replace the 'EG-CFG-style execution-only feedback' baseline with an AlphaCodium-style baseline: problem analysis → AI test generation → iterative code execution/refinement (no structured specs). This directly tests the paper's core claim that specification-mediated reasoning provides gains beyond test-based refinement. The controlled experiment should be: (a) ExeSpec full (specs + execution grounding), (b) AlphaCodium-style (tests + execution feedback, no specs), (c) Self-Spec (specs, no execution grounding), (d) direct prompting. The delta between (a) and (b) is the paper's contribution.\n\n2. **CITE AND POSITION AGAINST S* (EMNLP 2025 Findings)**: S* is the most recent training-free test-time scaling method for code generation, published at your target venue. Position ExeSpec as complementary: S* focuses on parallel/sequential scaling with execution-based selection; ExeSpec focuses on structured intermediate reasoning via verified specs. They could potentially be combined.\n\n3. **SHARPEN THE SPEC VS. TEST DISTINCTION**: The paper must clearly argue why structured behavioral specifications (pre/postconditions, invariants, type constraints) provide fundamentally different reasoning scaffolding compared to test cases. Add a controlled ablation: (a) full specs (I/O + pre/postconditions + invariants), (b) I/O-only specs (≈ test cases), (c) structural specs only (pre/postconditions + invariants, no I/O). If (b) performs similarly to (a), the novelty claim collapses.\n\n4. **SPECIFY THE CROSS-FILE COMPLETION APPROACH**: Describe concretely how ExeSpec generates and validates specs for CrossCodeEval/RepoBench tasks. What does the spec schema look like for incomplete code with cross-file dependencies? What 'lightweight probes' execute for partial programs? If the approach fundamentally differs from function-level generation, say so explicitly.\n\n5. **REDUCE SCOPE TO FIT TIMELINE**: Primary benchmarks with full baselines: DebugBench, CodeContests, SWE-bench Verified. Supplementary with ExeSpec vs. direct prompting only: HumanEval+/MBPP+, CrossCodeEval, RepoBench. This halves the experiment matrix.\n\n6. **ADD TO KEY REFERENCES**: AlphaCodium (2401.08500), CodeT (ICLR 2023, 2207.10397), Self-Debugging (2304.05128), BACE (2603.28653), 'Revisit Self-Debugging' (ACL 2025, 2501.12793), S* (EMNLP 2025 Findings, 2502.14382), SSDE (2605.02455).\n\n### Round 4 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING COMPETITOR: PGS (Property-Generated Solver, arXiv:2506.18315, June 2025, revised May 2026) uses high-level program properties instead of test cases as feedback for LLM code refinement, with execution-based property verification and minimal counterexample generation. It achieves 13.4% pass@1 improvement over TDD methods and 1.4-1.6x higher bug fix rate. This shares ExeSpec's core insight (properties > tests) and must be cited, compared against, and clearly differentiated.\", \"MISSING RELATED WORK: (1) 'From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing' (FSE 2025) directly challenges test-based paradigm in favor of properties; (2) ContractEval/PACT (arXiv:2510.12047) benchmarks LLM contract satisfaction showing 0% under standard prompting, validating the problem but also raising spec generation quality concerns; (3) 'Preconditions and Postconditions as Design Constraints for LLM Code Generation' (IEEE Access 2024/2025) directly studies ExeSpec's premise with controlled experiments; (4) StoryCoder (arXiv:2604.14631, ACL 2026) is another training-free structured intermediate reasoning method achieving 18.7% improvement.\", \"SWE-BENCH VERIFIED CONTAMINATION: The benchmark is now severely contaminated — top score is 93.9% (Claude Mythos), while the same models score only ~46% on SWE-bench Pro. OpenAI has stopped reporting Verified scores. The paper acknowledges contamination but should more seriously consider using SWE-bench Pro as the primary evaluation or running both and comparing. Reporting only Verified results risks reviewer skepticism.\", \"MODEL CURRENCY: Qwen3-Coder has been released since the idea was designed. EMNLP reviewers may question why the paper uses Qwen2.5-Coder-7B/32B rather than the latest version. Either justify the choice (reproducibility, available at experiment time) or update.\", \"SPEC GENERATION QUALITY RISK INSUFFICIENTLY ADDRESSED: ContractEval shows 0% contract satisfaction under standard prompting and only 23-41% with explicit contracts. CodeSpecBench shows 20.2% repo-level success. The paper's execution grounding is meant to catch bad specs, but if >60% of specs fail grounding, the method effectively degrades to 'generate specs → discard most → fall back to whatever survives' — potentially no better than test-only methods with fewer but higher-quality tests. The paper should include analysis of spec survival rates and graceful degradation behavior.\", \"TIMELINE MARGINAL: The manual estimate of 14-18 days with 2 researchers overlaps but can exceed the 16-day deadline. The upper bound should be trimmed to fit. Consider dropping one supplementary benchmark (e.g., RepoBench) to ensure the primary benchmarks are completed thoroughly.\"]\nFeedback: This is now a well-structured idea that has improved substantially through four rounds. The controlled experimental design with honest ablations is the strongest aspect. However, one critical competitor was discovered that must be addressed before this can pass:\n\n1. **CITE AND DIFFERENTIATE FROM PGS** (most important): PGS (arXiv:2506.18315) shares ExeSpec's core insight that properties outperform tests as LLM code feedback. Differentiate on: (a) ExeSpec execution-grounds the specs themselves (catches hallucinated specs before use), while PGS assumes properties are correct; (b) ExeSpec applies across 4 task types (generation, debugging, completion, issue resolution), PGS focuses on generation/repair; (c) ExeSpec's comprehensive spec schema (5 component types) vs. PGS's single-property checking; (d) ExeSpec's controlled ablation isolates each spec component's contribution. Add PGS as a fifth baseline condition, or at minimum cite and discuss in Related Work with clear differentiation.\n\n2. **CITE FSE 2025 AND ContractEval**: 'From Prompts to Properties' (FSE 2025) validates the property-vs-test framing from a PBT perspective. ContractEval (arXiv:2510.12047) both validates your problem (LLMs fail at contracts) and raises spec quality concerns — use it to motivate your execution grounding stage.\n\n3. **ADDRESS SWE-BENCH CONTAMINATION SERIOUSLY**: Either (a) add SWE-bench Pro as the primary SE benchmark alongside Verified, or (b) follow the paper's current plan but add a contamination analysis section comparing performance on instances with/without known gold patch exposure. Option (a) is safer but adds implementation effort.\n\n4. **ADD SPEC SURVIVAL RATE ANALYSIS**: Report what fraction of generated specs survive execution grounding by task type and model. If survival is low, analyze whether the surviving specs still provide gains over test-only methods. This directly addresses the CodeSpecBench/ContractEval concern and strengthens the paper's analytical contribution.\n\n5. **JUSTIFY MODEL CHOICE**: Add a sentence noting that Qwen2.5-Coder was selected as the strongest open-source code model available at experiment design time, and that the method is model-agnostic. If time permits, add one data point with a newer model.\n\nThese are all fixable in one more revision round. The idea's core structure, experimental design, and positioning are sound — the main gap is incomplete coverage of the competitive landscape.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"CRITICAL — PGS STILL NOT CITED (Round 4 issue unresolved): PGS (arXiv:2506.18315, 'Use Property-Based Testing to Bridge LLM Code Generation and Validation', June 2025, revised May 2026) shares ExeSpec's core contribution: using program properties instead of test cases for LLM code refinement at inference time. PGS achieves 97.6% HumanEval, 87.2% MBPP, 76.5% LiveCodeBench, 49.7% CodeContests, 37.3% SWE-bench Verified using DeepSeek-R1-32B. It reports 23.1-37.3% relative pass@1 gains over TDD methods and 1.4-1.6x higher bug fix rates. This paper validates ExeSpec's hypothesis but also substantially reduces its novelty. Without citing and differentiating from PGS, any informed reviewer will reject on novelty grounds.\", \"ROUND 4 ISSUES LARGELY UNADDRESSED: (1) ContractEval/PACT (arXiv:2510.12047) — shows 0% contract satisfaction under standard prompting, motivates execution grounding but raises spec quality concerns — not cited; (2) 'From Prompts to Properties' (FSE 2025 LLanMER) — validates property-vs-test framing — not cited; (3) 'Preconditions and Postconditions as Design Constraints' (IEEE Access 2025) — directly studies ExeSpec's premise with controlled experiments — not cited; (4) StoryCoder (arXiv:2604.14631) — concurrent training-free structured intermediate reasoning — not cited.\", \"SWE-BENCH VERIFIED CONTAMINATION INSUFFICIENTLY ADDRESSED: OpenAI has officially stopped reporting SWE-bench Verified scores (blog post: 'Why SWE-bench Verified no longer measures frontier coding capabilities'). Top score is 93.9% vs. ~46% on SWE-bench Pro. The idea mentions 'noting contamination concerns per OpenAI's 2026 audit' but still uses Verified as a primary benchmark without proposing SWE-bench Pro as an alternative or replacement. EMNLP reviewers aware of the contamination will question evaluation credibility.\", \"MODEL CURRENCY: Qwen3-Coder-Next (3B/80B MoE, 256k context, >70% SWE-bench Verified) and DeepSeek V4 have been released. Using Qwen2.5-Coder without justification looks dated. Either justify the choice (available at experiment design time, reproducibility) or add a data point with a newer model.\", \"NOVELTY BOUNDARY WITH PGS IS THIN: PGS uses LLM-generated abstract properties with execution-based validation and minimal counterexample feedback. ExeSpec uses LLM-generated behavioral specifications (pre/postconditions, invariants, type constraints) with execution grounding and structured violation reports. Both are training-free, inference-time, property-level-rather-than-test-level approaches. The genuine differentiators — (a) execution grounding of specs themselves (PGS assumes properties are ~87% accurate), (b) structured 5-component schema with component ablation, (c) multi-task applicability beyond generation — must be explicitly argued. Without this, the paper reads as a PGS variant with a different spec format.\", \"MISSING NL-DEBUGGING (EMNLP 2025 Oral): 'Natural Language as Intermediate Representation for Code Debugging' (arXiv:2505.15356) was accepted as an Oral at EMNLP 2025 — the same venue being targeted. It uses NL (not specifications) as an intermediate representation for debugging and shows consistent gains over code-level debugging. This is a strong baseline for the debugging task (DebugBench) and establishes the 'intermediate representation for code tasks' paradigm at this exact venue.\"]\nFeedback: The idea has matured substantially over 5 rounds — the experimental design with honest ablations, primary/supplementary benchmark distinction, and AlphaCodium baseline are all strong. However, the most critical Round 4 issue (PGS) remains unaddressed, and this is now blocking passage. Here is exactly what needs to change:\n\n1. **CITE AND DIFFERENTIATE FROM PGS** (highest priority, non-negotiable): Add PGS to key_references and landscape. Position ExeSpec's contributions BEYOND PGS's established result (properties > tests): (a) ExeSpec execution-grounds the specs themselves — PGS's verification asymmetry (87% property accuracy) means ~13% of properties are wrong, and PGS has no mechanism to catch them before use; ExeSpec's Stage 2 catches hallucinated specs via execution probes; (b) ExeSpec evaluates across 4 task types (generation, debugging, completion, issue resolution) while PGS evaluates generation and repair; (c) ExeSpec's 5-component schema with component ablation provides fine-grained analysis of which spec types help which tasks — PGS treats properties as a monolithic category. Consider adding PGS as a 5th baseline condition on at least CodeContests and DebugBench, or at minimum cite and discuss with clear differentiation.\n\n2. **ADDRESS SWE-BENCH CONTAMINATION**: Either (a) replace SWE-bench Verified with SWE-bench Pro as primary (preferred — aligns with community trend), or (b) keep Verified but add contamination analysis comparing performance on high-contamination vs. low-contamination instances (requires the contamination labels from OpenAI's audit). Option (a) adds implementation effort but makes the paper future-proof.\n\n3. **CITE ADDITIONAL MISSING WORK**: Add to key_references and discuss in landscape: ContractEval/PACT (2510.12047), NL-Debugging (2505.15356, EMNLP 2025 Oral — important as it's at the same venue), 'From Prompts to Properties' (FSE 2025). These validate ExeSpec's problem framing and provide important context.\n\n4. **JUSTIFY OR UPDATE MODEL CHOICE**: Add one sentence: 'We use Qwen2.5-Coder as the strongest open-source code model with publicly available weights at experiment design time; the method is model-agnostic and we expect consistent gains across model generations.' If feasible within budget, add one supplementary data point with Qwen3-Coder-Next-3B to demonstrate model-agnostic applicability.\n\n5. **SHARPEN THE NARRATIVE**: After citing PGS, reframe ExeSpec's contribution as: 'PGS demonstrated that property-level feedback outperforms test-based feedback for code generation. We advance this finding in three ways: (1) we show that execution-grounded specification verification catches ~X% of hallucinated specs that would corrupt reasoning, (2) we extend property-level reasoning beyond generation to debugging, completion, and issue resolution, and (3) we decompose the contribution of different spec components (I/O, preconditions, postconditions, invariants, type constraints) across task types, providing actionable guidance for spec-mediated code reasoning.'\n\nThese changes are all feasible in one revision round. The idea's core structure is sound — it just needs to acknowledge and position against the competitive landscape that has emerged.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"CRITICAL — PGS STILL NOT CITED (4th consecutive round): PGS (arXiv:2506.18315, 'Use Property-Based Testing to Bridge LLM Code Generation and Validation', June 2025, revised May 2026) shares ExeSpec's core contribution: using LLM-generated properties (not tests) for code refinement with execution-based validation. PGS validates properties via soundness checks against public tests + sensitivity to known errors, then provides minimal counterexample feedback. It evaluates on HumanEval (97.6%), MBPP (81.2%), and LiveCodeBench (74.5%) with DeepSeek-R1-Distilled-32B. Note: PGS does NOT evaluate on CodeContests or SWE-bench (the Round 5 reviewer's numbers for those benchmarks were incorrect). ExeSpec's genuine differentiators vs. PGS: (1) execution-grounds specs themselves before use via probes, catching hallucinated specs; (2) covers 4 task types vs. PGS's generation-only scope; (3) structured 5-component schema with component ablation vs. PGS's monolithic property checking; (4) structured violation reports vs. minimal counterexamples. These are meaningful but incremental. This is the 4th consecutive round raising this issue — if unaddressed in the next round, this should be grounds for failure.\", \"NL-DEBUGGING STILL NOT CITED (EMNLP 2025 ORAL): NL-Debugging (arXiv:2505.15356, ACL Anthology 2025.emnlp-main.80) uses natural language as an intermediate representation for debugging, demonstrating gains over code-level debugging. Published as an ORAL at EMNLP 2025 — the exact target venue. This establishes the 'intermediate representation for code tasks' paradigm at this venue and is a critical baseline for DebugBench evaluation. Reviewers at EMNLP 2026 will know this paper.\", \"CONTRACTEVAL STILL NOT CITED: ContractEval (arXiv:2510.12047) shows 0% contract satisfaction under standard prompting, 23-41% with explicit contracts, 49-53% with contract-violating test examples. This validates ExeSpec's motivation (LLMs need grounding for spec generation) but also quantifies the spec quality challenge. Must be cited to strengthen the execution grounding motivation.\", \"SWE-BENCH VERIFIED CONTAMINATION INSUFFICIENTLY ADDRESSED: OpenAI has officially stopped reporting SWE-bench Verified scores. All frontier models show training data contamination — models can reproduce exact gold patches verbatim. Claude Opus 4.5 scores 80.9% on Verified but only 45.9% on Pro. While Qwen2.5-Coder (sub-frontier) may be less contaminated, the benchmark's credibility is severely damaged. The paper's approach of 'noting contamination concerns per OpenAI's 2026 audit' and 'reporting held-out test pass rates alongside standard metrics' is insufficient. Either: (a) add SWE-bench Pro as a co-primary benchmark, (b) demonstrate Qwen2.5-Coder-7B/32B are not contaminated on Verified via gold-patch reproduction tests, or (c) at minimum acknowledge that the community has moved to Pro and explain why Verified remains informative for sub-frontier models.\", \"MODEL CURRENCY UNJUSTIFIED: Qwen3-Coder-Next (3B active / 80B total MoE, 256k context, >70% SWE-bench Verified) has been released. Qwen2.5-Coder remains a valid reproducibility choice, but the paper needs one sentence justifying it (e.g., 'strongest open-source code model with dense architecture available at experiment design time; the method is model-agnostic'). Without justification, EMNLP reviewers may question currency.\", \"'FROM PROMPTS TO PROPERTIES' (FSE 2025/LLanMER) STILL NOT CITED: This paper applied property-based testing to evaluate StarCoder and CodeLlama on MBPP/HumanEval, finding 30-32% of generated solutions only partially adhere to correctness properties and 18-23% fail outright. Validates ExeSpec's property-vs-test framing from the evaluation side.\"]\nFeedback: This is Round 6, and the idea's experimental design, controlled baselines, and honest ablation commitment are genuinely strong. However, the repeated failure to cite PGS — now raised for the 4th consecutive round as non-negotiable — is becoming a disqualifying pattern. Here is exactly what must change:\n\n1. **CITE AND DIFFERENTIATE FROM PGS** (FINAL WARNING — if unaddressed in Round 7, this warrants failure): Add PGS to key_references and landscape. Note that PGS evaluates ONLY on HumanEval/MBPP/LiveCodeBench and does NOT evaluate on CodeContests, SWE-bench, or DebugBench — this is actually ExeSpec's opportunity. Position ExeSpec's contributions BEYOND PGS: (a) ExeSpec execution-grounds specs before use (probes catch hallucinated specs); PGS validates properties against public tests but doesn't catch internally inconsistent properties before use. (b) ExeSpec evaluates across 4 task types including debugging and issue resolution — PGS only covers generation. (c) ExeSpec's 5-component ablation decomposes which spec types help which tasks — PGS treats properties as monolithic. (d) ExeSpec directly compares against AlphaCodium on CodeContests (PGS's home turf overlap — neither AlphaCodium nor PGS compares against each other). Reframe the narrative: 'PGS demonstrated that property-level feedback outperforms test-based feedback for code generation. We advance this finding by: (1) showing execution-grounded spec verification catches hallucinated specs that corrupt reasoning, (2) extending property-level reasoning to debugging, completion, and issue resolution, (3) providing fine-grained ablation of which specification components help which task types.'\n\n2. **CITE NL-DEBUGGING AS DEBUGGING BASELINE**: Add NL-Debugging (2505.15356, EMNLP 2025 Oral) to key_references. Position ExeSpec's debugging approach as advancing beyond NL-level debugging by providing structured, execution-verified behavioral constraints (not just NL descriptions). If feasible, add NL-Debugging as a 5th baseline condition on DebugBench — this would strongly differentiate ExeSpec.\n\n3. **ADDRESS SWE-BENCH CONTAMINATION CONCRETELY**: Add one of: (a) 'We additionally evaluate on SWE-bench Pro on a representative subset to validate that gains generalize beyond Verified'; (b) 'We verify Qwen2.5-Coder models are not contaminated by testing gold-patch reproduction rates'; (c) 'We acknowledge SWE-bench Verified's contamination concerns are most severe for frontier models; Qwen2.5-Coder-7B/32B are sub-frontier models unlikely to have been trained on the SWE-bench gold patches.' Option (c) is the minimum acceptable response.\n\n4. **CITE CONTRACTEVAL AND 'FROM PROMPTS TO PROPERTIES'**: ContractEval (2510.12047) motivates execution grounding (0% contract satisfaction without it). 'From Prompts to Properties' (FSE 2025) validates the property-vs-test evaluation framing. Both strengthen ExeSpec's problem statement.\n\n5. **ADD MODEL JUSTIFICATION**: One sentence: 'We use Qwen2.5-Coder-7B/32B-Instruct as well-established dense models with strong code performance and reproducible inference via vLLM; the method is model-agnostic and we expect consistent gains across model generations.' If time/budget permit, add one supplementary data point with a Qwen3 model.\n\nThe core idea is sound and the experimental design is rigorous. But an EMNLP reviewer who has read PGS (published June 2025, revised May 2026 — highly visible) will immediately recognize the overlap and reject if PGS is not acknowledged. This is the most critical fix.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-12T01:55:02.351Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T01:55:02.351Z",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---

## Round 1

35 recorded events

### User

_source line 3 · 2026-05-12T01:55:02.395Z_

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

## Idea under review (round 7/10)
{
  "title": "ExeSpec: Verifiable Specification Reasoning for Code LLMs via Execution Grounding",
  "core_problem": "Training-free inference-time methods for LLM code improvement—AlphaCodium (arXiv 2401.08500), CodeT (ICLR 2023), Self-Debugging (arXiv 2304.05128), S* (EMNLP 2025 Findings)—have demonstrated that execution feedback at inference time substantially boosts code generation quality. However, these methods uniformly treat test cases as their intermediate representation: they generate I/O test pairs, execute candidate code against them, and refine based on pass/fail signals. Tests are point samples—they verify specific inputs but do not capture behavioral intent (preconditions, postconditions, invariants, type constraints). This creates two limitations: (1) test-based methods provide pass/fail validation but not structured reasoning scaffolds that inform how code should behave across all inputs, and (2) they are largely restricted to code generation tasks where test generation is natural, without principled extension to debugging (where intended-vs-observed behavioral contrasts are needed), completion (where interface contracts must be inferred), or reasoning (where execution expectations must be formalized). Meanwhile, Self-Spec (Agents4Science 2025) showed that model-authored behavioral specifications improve generation (+2–5pp on HumanEval), but these specifications are never verified against execution—CodeSpecBench (arXiv 2604.12268) reveals only 20.2% success at repo-level spec generation, demonstrating that unverified LLM-generated specs are unreliable. Can execution-grounded behavioral specifications—richer than test cases, capturing universal behavioral properties—serve as verifiable structured intermediate reasoning that outperforms test-based refinement methods across diverse code tasks without model training?",
  "opportunity": "Four research threads converge but remain disconnected: (1) Test-based inference-time refinement (AlphaCodium, CodeT, Self-Debugging, S*, BACE) proves execution feedback improves code generation—AlphaCodium's flow engineering raises CodeContests pass@5 from 19% to 44%, CodeT improves HumanEval pass@1 by +18.8pp via dual execution agreement, S* enables a 3B model to outperform GPT-4o-mini on LiveCodeBench—but all use test cases (point samples) as the intermediate representation, not property-level behavioral descriptions. (2) Specification-mediated reasoning (Self-Spec) demonstrates that LLM-authored specs improve generation by +2–5pp, establishing that structured behavioral intent aids code reasoning—but specs are never execution-verified, and 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025) shows that self-generated test feedback introduces systematic bias that degrades performance for some models, motivating richer intermediate representations beyond tests. (3) Execution-trace training (Think Like You Execute, RLEF at ICML 2025) achieves dramatic gains (+22–27pp) by grounding reasoning in execution, but requires fine-tuning on 54K+ verified rationales—not usable with frozen models. (4) CodeSpecBench reveals that LLMs achieve only 20.2% on repo-level spec generation, and SSDE (FSE Companion 2026) shows structured specs (Gherkin) can guide repo-level generation but requires human-authored specifications. The unexploited synthesis: use execution to verify LLM-generated behavioral specifications (pre/postconditions, invariants, type constraints—not just I/O pairs) at inference time, creating property-level reasoning scaffolds that capture universal behavioral intent rather than point samples. The key hypothesis: specifications provide fundamentally richer intermediate reasoning than tests because they describe what must hold for all inputs (universal properties) rather than what happens for specific inputs (existential examples), enabling the LLM to reason about behavioral correctness at a higher abstraction level.",
  "landscape": "**Test-based inference-time methods.** AlphaCodium (arXiv 2401.08500, Jan 2024) is the most direct predecessor: a training-free multi-stage flow with problem reflection, AI test generation (6–8 diverse I/O pairs), and iterative execution-based refinement with test anchoring, achieving 44% pass@5 on CodeContests (vs. 19% direct prompting). Its pre-processing phase (problem reflection → public test reasoning → solution ranking → AI test generation) produces structured problem analysis in YAML format, and its code iteration phase uses test anchoring to prevent regression—fixes that break anchor tests are rejected. CodeT (ICLR 2023, arXiv 2207.10397) generates tests via LLMs and uses dual execution agreement (output consistency against generated tests + cross-sample agreement) for solution selection, improving HumanEval pass@1 by +18.8pp with code-davinci-002. Self-Debugging (arXiv 2304.05128, 2023) teaches LLMs to iteratively debug using execution results and natural language explanations (rubber-duck debugging), achieving up to 12% improvement on TransCoder and MBPP. 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025 Long, arXiv 2501.12793) reveals that post-execution self-debugging suffers from systematic bias in self-generated tests—in-execution debugging using intermediate program states mitigates this, demonstrating that test quality is a fundamental bottleneck for test-based methods. S* (EMNLP 2025 Findings, arXiv 2502.14382) combines parallel sampling (16 candidates) with sequential debugging and adaptive distinguishing input synthesis for execution-grounded selection, enabling a 3B model to outperform GPT-4o-mini and GPT-4o-mini+S* to outperform o1-preview by 3.7% on LiveCodeBench. BACE (GECCO 2026, arXiv 2603.28653) treats generated tests as noisy sensors via Bayesian updates, co-evolving code and test populations on LiveCodeBench v6, outperforming CodeSIM by +2.5–5.4pp. All these methods use test cases as the intermediate representation—point samples that verify specific inputs but don't capture universal behavioral properties.\n\n**Specification-based approaches.** Self-Spec (Agents4Science 2025) has LLMs author specification languages before code generation, improving GPT-4o HumanEval pass@1 from 87% to 92% (+5pp) and Claude 3.7 from 92% to 94% (+2pp), but only evaluates on single-function HumanEval, never verifies specs against execution, and doesn't extend beyond generation. SpecRover/AutoCodeRover-v2 (ICSE 2025) performs iterative NL specification inference for automated program repair, achieving 19.31% on SWE-bench (50%+ improvement over AutoCodeRover). VibeRepair (arXiv 2602.08263) translates code into NL behavioral specs for repair but specs are imprecise and hallucination-prone. SSDE (FSE Companion 2026, arXiv 2605.02455) uses Gherkin specifications and domain models for repo-level MVC generation—concurrent work demonstrating structured specs guide LLM generation, but requires human-authored specifications rather than LLM-generated and verified ones. CodeSpecBench (arXiv 2604.12268) benchmarks LLM spec generation showing only 20.2% repo-level pass rate, motivating execution-based verification of LLM-generated specs.\n\n**Execution-grounded training methods.** Think Like You Execute (arXiv 2512.00127) achieves +22–27pp on CRUXEval/LiveCodeBench via fine-tuning on 54K execution-trace-verified rationales. EG-CFG (NeurIPS 2025, arXiv 2506.10948) uses real-time execution via beam search over candidate lines—computationally expensive and generation-only. RLEF (ICML 2025) trains code LLMs with RL execution feedback. Think Anywhere (arXiv 2603.29957) enables on-demand reasoning during code generation via RL training, achieving 70.3% average across four benchmarks. CURE (NeurIPS 2025 Spotlight) co-evolves coder and tester via RL. All require training—not applicable with frozen models.\n\n**Other relevant work.** SCoT (ACL 2024) adds program structure to CoT without execution grounding. Test overfitting studies show 21.8–35.9% of LLM patches overfit visible tests (arXiv 2511.16858), and ICSE 2026 NIER proves overfitting is undecidable without full specifications—motivating property-level specs as reasoning scaffolds.\n\n**The gap.** Existing training-free methods use tests (point samples) for validation. No work uses property-level behavioral specifications (pre/postconditions, invariants, type constraints) as execution-grounded structured intermediate reasoning in a training-free framework, with controlled evidence that property-level specs outperform test-based refinement across diverse code tasks.",
  "approach": "We propose ExeSpec, a training-free inference-time framework that uses execution-grounded behavioral specifications as verifiable structured intermediate reasoning for LLM code tasks. The critical distinction from test-based methods (AlphaCodium, CodeT, S*) is that ExeSpec generates property-level behavioral descriptions—universal constraints about what code must satisfy for all inputs—rather than point-sample test cases that verify specific I/O pairs. This provides richer reasoning scaffolds: knowing 'f(x) returns 2x for all non-negative integers, raises ValueError for negative inputs' (specification) enables different reasoning than knowing 'f(5)=10, f(3)=6' (tests).\n\n**Stage 1: Spec Elicitation.** Given a task input, prompt the LLM to generate structured behavioral specifications in a lightweight JSON schema containing five component types: (a) I/O example pairs (shared with test-based methods—this is the overlap with AlphaCodium), (b) preconditions (constraints on valid inputs/states, e.g., 'n >= 0', 'input list is non-empty'), (c) postconditions (properties guaranteed on outputs, e.g., 'output is sorted in ascending order', 'len(output) == len(input)'), (d) type constraints (parameter and return type annotations with generics, e.g., 'List[int] -> int'), and (e) invariants (loop invariants, monotonicity, ordering properties, e.g., 'partial_sum increases monotonically'). The schema is task-adapted: generation tasks derive specs from docstrings and problem descriptions; debugging tasks elicit intended-vs-observed behavioral contrasts (the spec says the output should be sorted, but the code produces [3,1,2]); issue resolution tasks extract expected behavioral changes from issue descriptions and failing test context.\n\n**Stage 2: Execution Grounding.** Validate and refine specifications by executing lightweight probes against available code context, catching hallucinated or contradictory specs before they corrupt downstream reasoning. For generation tasks: generate a quick candidate solution, execute against spec-derived assertions—both I/O examples (like AlphaCodium) AND postcondition property checks (e.g., assert all(output[i] <= output[i+1] for i in range(len(output)-1)) for a sorting postcondition)—identify spec-execution mismatches, and revise contradicted specs. For debugging tasks: execute the buggy code, compare execution traces against specs to identify precisely which behavioral constraints (not just which test cases) are violated, producing structured violation reports (e.g., 'postcondition violated: output should be sorted but is [3,1,2]; invariant violated: partial_sum is not monotonically increasing at iteration 3'). For issue resolution (SWE-bench): extract behavioral expectations from issue descriptions and failing tests, generate specs characterizing the intended fix behavior, and validate spec consistency against the existing test suite via Docker-based execution. When full execution is unavailable, static grounding serves as fallback: cross-spec consistency checking (e.g., precondition implies postcondition is satisfiable), type inference from signatures, and contradiction detection across spec components.\n\n**Stage 3: Spec-Guided Task Completion.** Feed grounded specs alongside the original task input to the LLM for final output. The model reasons about behavioral intent (what the code should do per verified property-level specs) rather than surface patterns. When outputs violate specs, structured violation reports (which constraints failed, expected vs. actual, which spec component) feed back for iterative refinement (up to 3 rounds). The key difference from test-based iteration (AlphaCodium): violation reports reference behavioral properties ('postcondition: output must be monotonically increasing'), not just I/O failures ('test case 3 failed'), giving the LLM richer corrective signal.\n\n**Baselines and controlled experiments.** The experimental design explicitly isolates the spec-vs-test distinction through four controlled conditions: (a) ExeSpec full (property-level specs + execution grounding), (b) AlphaCodium-style baseline (problem reflection + AI test generation + iterative execution/refinement, no property-level specs)—this directly tests whether specs provide gains beyond test-based refinement and is the paper's critical comparison, (c) Self-Spec baseline (specs without execution grounding)—tests the contribution of grounding, (d) direct prompting (no intermediate reasoning). The delta between (a) and (b) is the paper's core contribution. Additionally, a controlled spec-component ablation isolates the value of each spec type: (i) full specs (I/O + pre/postconditions + invariants + type constraints), (ii) I/O-only specs (functionally equivalent to AlphaCodium's AI test cases—the overlap region), (iii) structural specs only (pre/postconditions + invariants + type constraints, no I/O examples). If (ii) performs similarly to (i), the novelty claim is weakened—this ablation is the critical honesty test for the paper. S* is positioned as complementary (parallel/sequential scaling with execution-based selection) and could be combined with ExeSpec's spec-mediated reasoning; we note this in Related Work and Future Work but do not implement the combination.\n\n**Benchmarks.** Primary benchmarks with full baselines (all four conditions + spec-component ablation): DebugBench (C++/Java/Python debugging—specs naturally capture intended-vs-observed behavioral contrasts, the task type most differentiated from test-only methods), CodeContests (competitive programming—direct comparison to AlphaCodium on its home turf, using the same benchmark), and SWE-bench Verified (real-world issue resolution with Docker-based test execution—noting contamination concerns per OpenAI's 2026 audit, we report held-out test pass rates alongside standard metrics). Supplementary benchmarks with ExeSpec vs. direct prompting only: HumanEval+/MBPP+ (for Self-Spec comparability only, not primary given frontier models score 93%+), CrossCodeEval and RepoBench (cross-file completion with static grounding). For supplementary cross-file completion benchmarks, ExeSpec relies on static grounding: extracting type signatures from imported modules, inferring parameter/return types from usage context at call sites, and validating completions via type checkers (mypy/pyright for Python, tsc for TypeScript). We explicitly acknowledge this is weaker grounding than dynamic execution and report the proportion of instances where only static grounding was available.\n\n**Analysis.** Beyond standard metrics, we report: (1) spec quality analysis—correlation between spec correctness (measured by agreement with ground-truth behavior) and downstream task performance; (2) grounding effectiveness—proportion of hallucinated specs caught by execution grounding vs. passing through undetected; (3) spec-component contribution—which spec types (I/O, preconditions, postconditions, invariants, type constraints) most improve each task type; (4) test overfitting rates—proportion of solutions passing visible tests but failing held-out tests, comparing ExeSpec vs. baselines (addressing ICSE 2026 undecidability concern); (5) qualitative case studies showing where property-level specs enable corrections that test-only methods miss (e.g., off-by-one errors caught by ordering invariants but missed by finite test cases, type constraint violations caught by postcondition checks).\n\nAll experiments use Qwen2.5-Coder-7B-Instruct and Qwen2.5-Coder-32B-Instruct via vLLM batch inference on H100 GPUs, with SWE-bench evaluation using the existing Docker harness.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~100–150 H100-hours (primary benchmarks DebugBench + CodeContests + SWE-bench Verified with 4 conditions × 2 models + spec-component ablation on primary benchmarks; supplementary HumanEval+/MBPP+ + CrossCodeEval + RepoBench with ExeSpec vs. direct prompting × 2 models; using vLLM batch inference with Qwen2.5-Coder-7B on 1 H100 and 32B on 1–2 H100s)",
      "gpu_utilization": "Moderate (~40–55%): alternating between inference bursts and execution-grounding phases (running generated code against assertions, Docker-based test execution for SWE-bench); execution harness is CPU-bottlenecked while GPU idles during test runs",
      "timeline": "14–18 days (days 1–3: framework implementation + AlphaCodium-style baseline reimplementation using open-source AlphaCodium code + eval harness setup leveraging existing SWE-bench Docker harness, EvalPlus, and benchmark repositories; days 4–7: primary benchmarks DebugBench + CodeContests with all 4 conditions; days 8–10: SWE-bench Verified with all 4 conditions; days 11–12: supplementary benchmarks HumanEval+/MBPP+ + CrossCodeEval + RepoBench with ExeSpec vs. direct prompting; days 13–15: spec-component ablation on DebugBench + CodeContests + analysis; days 16–18: writing)",
      "team": "2 researchers (1 lead for ExeSpec framework + spec-grounding pipeline + spec-component ablation design, 1 for AlphaCodium baseline adaptation from open-source code + benchmark integration + evaluation infrastructure)",
      "estimated_gpu_cost": "$300–450 (on-demand H100 at ~$3/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "~120–170 H100-hours (same scope as manual with more systematic spec quality validation and additional analysis iterations)",
      "gpu_utilization": "Moderate–High (~50–65%): agent queues experiment batches across benchmarks while human reviews spec quality between rounds",
      "timeline": "10–14 days (agent handles framework code, experiment orchestration, and result collection; human validates spec schema design, reviews AlphaCodium baseline fidelity, and guides ablation priorities)",
      "team": "1 researcher, ~2–3 hrs/day reviewing spec elicitation outputs, validating AlphaCodium baseline implementation matches the published flow, approving experiment plans, and analyzing spec-component ablation results",
      "claude_api_cost": "$100–200 (1000–2000 orchestration turns at ~$0.10/turn for code generation, experiment design, and result analysis)",
      "estimated_gpu_cost": "$360–510",
      "risk_note": "AlphaCodium baseline reimplementation fidelity is a key risk—must reproduce the core flow (problem reflection + AI test generation + iterative execution with test anchoring) faithfully; recommend using AlphaCodium's open-source code (github.com/Codium-ai/AlphaCodium) as starting point and adapting for non-CodeContests benchmarks (DebugBench, SWE-bench)"
    },
    "auto_research": {
      "gpu_hours": "~150–200 H100-hours (systematic sweeps over spec granularity levels, grounding strategies per benchmark, additional model backbone DeepSeek-Coder-V2-Lite-16B, temperature and sample-count variations)",
      "gpu_utilization": "High (~80–90%): agent pipelines experiments back-to-back with minimal idle; parallel runs across benchmarks on multiple H100s",
      "timeline": "6–9 days with 4–8 H100s available concurrently (bottlenecked by SWE-bench Docker container builds and sequential test execution per instance)",
      "team": "0 (initial setup ~3–4 hours for benchmark harness configuration, AlphaCodium baseline setup from open-source code, and vLLM model serving, then fully autonomous)",
      "claude_api_cost": "$200–400 (2000–4000 turns for iterative experiment design, spec schema optimization, cross-benchmark analysis, and paper section drafting)",
      "estimated_gpu_cost": "$450–600",
      "speed_bottleneck": "SWE-bench Verified Docker-based test execution (sequential per instance, ~2–5 min per task including container setup) and DebugBench compilation/execution harness; inference itself is fast with vLLM on H100",
      "risk_note": "Agent may over-optimize spec schema for one benchmark at the expense of others; need guardrails to ensure the AlphaCodium baseline is faithfully implemented (using open-source code, not strawmanned) and that the spec-component ablation is run completely even if early results are unfavorable"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission May 25, 2026; commitment Aug 2, 2026; NLP and Code Models track; Budapest, Hungary)",
    "ACL 2027 (expected ARR commitment ~Jan 2027; fallback if EMNLP revision needed)",
    "NAACL 2027 (expected ARR commitment ~Mar 2027; second fallback)"
  ],
  "level": "solid",
  "key_references": [
    "AlphaCodium: Code Generation through Flow Engineering (arXiv 2401.08500, Jan 2024)",
    "CodeT: Code Generation with Generated Tests (ICLR 2023, arXiv 2207.10397)",
    "Teaching Large Language Models to Self-Debug (Self-Debugging; arXiv 2304.05128, 2023)",
    "Revisit Self-Debugging with Self-Generated Tests for Code Generation (ACL 2025 Long, arXiv 2501.12793)",
    "S*: Test Time Scaling for Code Generation (EMNLP 2025 Findings, arXiv 2502.14382)",
    "BACE: Bayesian Anchored Co-Evolution of Code and Test Populations (GECCO 2026, arXiv 2603.28653)",
    "Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation (Agents4Science 2025)",
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
  "description": "We propose ExeSpec, a training-free inference-time framework that uses execution-grounded behavioral specifications as verifiable structured intermediate reasoning for LLM code tasks. The critical distinction from existing test-based methods (AlphaCodium, CodeT, Self-Debugging, S*) is that ExeSpec generates property-level behavioral descriptions—preconditions, postconditions, invariants, type constraints—that capture universal behavioral intent, rather than point-sample test cases that verify specific I/O pairs. The method operates in three stages: (1) Spec Elicitation—prompt the LLM to generate structured behavioral specifications (I/O examples, pre/postconditions, invariants, type constraints) in a JSON schema; (2) Execution Grounding—validate specs by executing lightweight probes (running candidate code against spec-derived property assertions, comparing buggy code behavior against intended specs, type-checking completion context), catching hallucinated specs before they corrupt reasoning; (3) Spec-Guided Completion—use grounded specs as verified intermediate reasoning with structured violation feedback for iterative refinement. The experimental design explicitly isolates the paper's contribution through four controlled conditions: (a) ExeSpec full (property-level specs + execution grounding), (b) AlphaCodium-style baseline (problem reflection + AI test generation + iterative execution/refinement, no property-level specs), (c) Self-Spec baseline (specs, no execution grounding), (d) direct prompting. The delta between (a) and (b) is the core contribution—whether property-level specs provide gains beyond test-based refinement. A critical spec-component ablation further decomposes: (i) full specs, (ii) I/O-only specs (≈ tests, AlphaCodium-equivalent), (iii) structural specs only (pre/postconditions + invariants, no I/O)—if (ii) ≈ (i), the novelty claim collapses, and we commit to reporting this honestly. Primary benchmarks with full baselines: DebugBench (debugging), CodeContests (competitive programming—AlphaCodium's home benchmark), SWE-bench Verified (issue resolution). Supplementary with ExeSpec vs. direct prompting only: HumanEval+/MBPP+ (Self-Spec comparability), CrossCodeEval/RepoBench (cross-file completion with static grounding via type checkers). S* is positioned as complementary (test-time scaling via execution-based selection); SSDE is concurrent work using human-authored Gherkin specs. All experiments use Qwen2.5-Coder-7B/32B-Instruct via vLLM on H100 GPUs. Within 100–150 H100-hours and ~16 days. Primary target: EMNLP 2026 (ARR May 25, 2026).",
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
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "type": "user",
  "uuid": "356efcea-dd18-4770-9409-51129222b334",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T01:55:02.390Z_

```json
{
  "parentUuid": "356efcea-dd18-4770-9409-51129222b334",
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
  "uuid": "a2e56301-95df-4f78-8d3c-8e022e9a4645",
  "timestamp": "2026-05-12T01:55:02.390Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T01:55:02.390Z_

```json
{
  "parentUuid": "a2e56301-95df-4f78-8d3c-8e022e9a4645",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "28d18463-b9aa-44f3-afbd-511a1818ba6f",
  "timestamp": "2026-05-12T01:55:02.390Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
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
  "leafUuid": "28d18463-b9aa-44f3-afbd-511a1818ba6f",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Specification-Grounded Code Reasoning at Inference Time",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---

### Assistant

_source line 8 · 2026-05-12T01:55:20.183Z_

<details><summary>Logged reasoning block</summary>

```text
This is Round 7 of 10 for reviewing the ExeSpec idea. Let me conduct a thorough independent review, focusing especially on:

1. Whether PGS has finally been cited (this was raised for 4 consecutive rounds as non-negotiable)
2. Whether other missing references have been addressed
3. Independent verification of claims
4. The overall quality and novelty assessment

Let me start by searching for the key papers and claims.

First, let me check the idea carefully. Looking at the key_references list... I see:
- AlphaCodium ✓
- CodeT ✓


- Self-Debugging ✓
- Revisit Self-Debugging ✓
- S* ✓
- BACE ✓
- Self-Spec ✓
- EG-CFG ✓
- Think Like You Execute ✓
- Think Anywhere ✓
- SpecRover ✓
- CURE ✓
- CodeSpecBench ✓
- VibeRepair ✓
- SSDE ✓
- Test Overfitting ✓
- ICSE 2026 NIER ✓
- RLEF ✓
- SCo ✓
- Qwen2.5-Coder ✓

I'm noticing some critical gaps that keep coming up: PGS, NL-Debugging, ContractEval, and "From Prompts to Properties" are still missing after multiple rounds of requests, with PGS now flagged as a final warning issue. I need to independently verify whether these papers actually exist and check what the current state-of-the-art really is.

Now I'm searching for these papers and their benchmarks to see what competitors I might be missing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28d18463-b9aa-44f3-afbd-511a1818ba6f",
  "isSidechain": false,
  "requestId": "req_011Cawqnvqa3sv4aQiYcWqTw",
  "type": "assistant",
  "uuid": "a61957b0-4aab-4ce5-821b-ff08dc6c2614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQ7Hc7AHd2QbYs7RxV5AMz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25590,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1878,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25590
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

_source line 9 · 2026-05-12T01:55:20.263Z_

I'll conduct an independent review of this idea, focusing on verifying claims, checking for missing competitors (especially PGS, which has been flagged for 4 consecutive rounds), and assessing overall quality. Let me search in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a61957b0-4aab-4ce5-821b-ff08dc6c2614",
  "isSidechain": false,
  "requestId": "req_011Cawqnvqa3sv4aQiYcWqTw",
  "type": "assistant",
  "uuid": "e322bbd3-eeaf-4de9-897a-c21fa4694eb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQ7Hc7AHd2QbYs7RxV5AMz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25590,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1878,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25590
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

_source line 10 · 2026-05-12T01:55:26.039Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015ndzMFhCXG5JkF1jabY18Y`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for PGS property-based testing paper",
  "prompt": "Search the web for the paper \"Use Property-Based Testing to Bridge LLM Code Generation and Validation\" (arXiv:2506.18315). This is also known as \"PGS\" or \"Property-Generated Solver.\" \n\nI need to verify:\n1. Does this paper exist?\n2. What are its actual results (HumanEval, MBPP, LiveCodeBench, CodeContests, SWE-bench)?\n3. What is its core method?\n4. When was it published/revised?\n\nSearch queries to try:\n- \"arXiv 2506.18315\"\n- \"Property-Based Testing Bridge LLM Code Generation Validation\"\n- \"PGS property generated solver code LLM\"\n- \"property-based testing LLM code generation 2025\"\n\nUse WebSearch and WebFetch to find and read the actual paper. Report back with detailed findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e322bbd3-eeaf-4de9-897a-c21fa4694eb2",
  "isSidechain": false,
  "requestId": "req_011Cawqnvqa3sv4aQiYcWqTw",
  "type": "assistant",
  "uuid": "26d7ea99-b51e-416a-a78b-96cf00a10b65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQ7Hc7AHd2QbYs7RxV5AMz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25590,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1878,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25590
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

_source line 11 · 2026-05-12T01:55:29.778Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0196EHkJ5pxMaqVe2JvX8agz`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for NL-Debugging EMNLP 2025",
  "prompt": "Search the web for the paper \"Natural Language as Intermediate Representation for Code Debugging\" (arXiv:2505.15356). This was reportedly accepted as an ORAL at EMNLP 2025.\n\nI need to verify:\n1. Does this paper exist?\n2. Was it really accepted at EMNLP 2025 as an Oral?\n3. What is its core method — using NL as intermediate representation for debugging?\n4. What benchmarks and results does it report?\n\nSearch queries:\n- \"arXiv 2505.15356\"\n- \"Natural Language Intermediate Representation Code Debugging EMNLP 2025\"\n- \"NL-Debugging code LLM 2025\"\n- \"site:aclanthology.org 2025.emnlp-main natural language debugging\"\n\nUse WebSearch and WebFetch. Report back with detailed findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26d7ea99-b51e-416a-a78b-96cf00a10b65",
  "isSidechain": false,
  "requestId": "req_011Cawqnvqa3sv4aQiYcWqTw",
  "type": "assistant",
  "uuid": "0162cd6e-8057-42e7-94a5-8b74671b73b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQ7Hc7AHd2QbYs7RxV5AMz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25590,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1878,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25590
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

_source line 12 · 2026-05-12T01:55:34.832Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01AAfmLggtAf7coZrsCKstk7`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for ContractEval and property-based code papers",
  "prompt": "Search the web for these papers:\n\n1. ContractEval / PACT (arXiv:2510.12047) — about benchmarking LLM contract satisfaction\n2. \"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing\" (FSE 2025 / LLanMER workshop)\n3. \"Preconditions and Postconditions as Design Constraints for LLM Code Generation\" (IEEE Access 2024/2025)\n\nFor each, I need:\n- Does the paper exist?\n- Core method and findings\n- Venue and date\n\nSearch queries:\n- \"arXiv 2510.12047\"\n- \"ContractEval PACT LLM contract satisfaction\"\n- \"From Prompts to Properties property-based testing LLM code generation FSE 2025\"\n- \"Preconditions Postconditions Design Constraints LLM Code Generation IEEE Access\"\n\nUse WebSearch and WebFetch. Report detailed findings for each."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0162cd6e-8057-42e7-94a5-8b74671b73b9",
  "isSidechain": false,
  "requestId": "req_011Cawqnvqa3sv4aQiYcWqTw",
  "type": "assistant",
  "uuid": "b132215b-3b89-4c01-9391-2b341b5c9308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQ7Hc7AHd2QbYs7RxV5AMz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25590,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1878,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25590
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

_source line 13 · 2026-05-12T01:55:40.982Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01K8RT3VcimCYW8pY7Rb66BU`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for latest code LLM SOTA and competitors",
  "prompt": "Search the web for the latest state-of-the-art on these code benchmarks as of May 2026:\n\n1. SWE-bench Verified — current top scores, contamination concerns, SWE-bench Pro status\n2. CodeContests — current best training-free/inference-time methods\n3. DebugBench — current best methods for LLM code debugging\n4. HumanEval/MBPP — current saturation level\n\nAlso search for:\n- Any new training-free inference-time code improvement methods from 2026\n- \"specification guided code generation 2026\"\n- \"property-based testing code LLM 2026\"\n- \"execution grounded code reasoning 2026\"\n- Qwen3-Coder status and availability\n\nSearch queries:\n- \"SWE-bench Verified contamination 2026 OpenAI\"\n- \"SWE-bench Pro benchmark 2026\"\n- \"CodeContests SOTA inference time 2026\"\n- \"DebugBench LLM debugging SOTA 2026\"\n- \"Qwen3 Coder release 2026\"\n- \"training-free code generation improvement 2026 arxiv\"\n\nUse WebSearch. Report detailed findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b132215b-3b89-4c01-9391-2b341b5c9308",
  "isSidechain": false,
  "requestId": "req_011Cawqnvqa3sv4aQiYcWqTw",
  "type": "assistant",
  "uuid": "511b7672-7097-4db3-b827-5b9b5659c1cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KQ7Hc7AHd2QbYs7RxV5AMz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25590,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25590,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1878,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25590
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

_source line 14 · 2026-05-12T01:56:38.876Z_

<details><summary>↩ Tool result · `toolu_0196EHkJ5pxMaqVe2JvX8agz`</summary>

```text
Excellent -- I now have all the information needed. Here is the full report.

---

## Verification Report: "NL-Debugging" (arXiv:2505.15356)

### 1. Does this paper exist?

**Yes.** The paper is real and fully published:

- **Title:** "NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging"
- **arXiv ID:** 2505.15356 (submitted May 21, 2025; revised October 29, 2025)
- **Authors:** Weiming Zhang, Qingyao Li, Xinyi Dai, Jizheng Chen, Kounianhua Du, Weiwen Liu, Yasheng Wang, Ruiming Tang, Yong Yu, and Weinan Zhang
- **DOI:** 10.18653/v1/2025.emnlp-main.80
- **Pages:** 1533--1549 in the proceedings

### 2. Was it accepted at EMNLP 2025 as an Oral?

**Yes, confirmed.** The paper appears in the EMNLP 2025 main conference proceedings (published by the Association for Computational Linguistics, Suzhou, China, November 2025). The first author's homepage (Weiming Zhang) explicitly lists it as an **Oral Presentation** at EMNLP 2025, announced in August 2025.

### 3. Core Method

The NL-Debugging framework uses natural language as an intermediate representation for code debugging. It operates in three stages:

1. **Backtranslation** -- The buggy code is converted into a natural language representation that captures its underlying algorithmic logic.
2. **Natural Language Refinement** -- Execution feedback (error messages, test case failures) is analyzed to identify discrepancies between intended and actual behavior. The erroneous natural language representation is then modified at the NL level.
3. **Regeneration (Forward Translation)** -- The refined natural language representation is translated back into executable code.

A key finding is that among different NL formats tested (pseudocode, key points, and sketch), **sketch-based NL-Debugging** yields the best results by a significant margin. Sketches provide more detailed natural language descriptions, enabling greater flexibility and a larger modification space compared to code-level debugging.

### 4. Benchmarks and Results

**Datasets used:**
- **APPS** -- 3 difficulty levels (introductory, interview, competition), 100 problems per level
- **Codeforces** -- 3 rating levels (1200, 1500, 1800), 100 problems per level

**LLM backbones tested:**
- GPT-4o-mini
- Claude 3.5-Sonnet
- DeepSeek-Coder-V2-Lite (16B, locally deployed)

**Key quantitative results (pass rate, baseline vs. NL-Debugging):**

| Dataset | Level | Baseline | NL-Debugging |
|---|---|---|---|
| APPS (GPT-4o-mini) | Introductory | 56.45% | 71.36% |
| APPS (GPT-4o-mini) | Competition | 34.67% | 44.17% |
| Codeforces (Claude 3.5-Sonnet) | Rating 1200 | 68.59% | 85.82% |
| Codeforces (Claude 3.5-Sonnet) | Rating 1800 | 42.06% | 61.28% |

The results show consistent and substantial improvements across all difficulty levels, models, and datasets, demonstrating that debugging at the natural language level outperforms traditional code-level debugging approaches.

---

Sources:
- [arXiv:2505.15356 Abstract](https://arxiv.org/abs/2505.15356)
- [arXiv:2505.15356 Full HTML](https://arxiv.org/html/2505.15356)
- [ACL Anthology: 2025.emnlp-main.80](https://aclanthology.org/2025.emnlp-main.80/)
- [EMNLP 2025 Accepted Main Conference Papers](https://2025.emnlp.org/program/main_papers/)
- [Weiming Zhang Homepage](https://wmzhang02.github.io/)

agentId: a888ea2ff2d9175fc (use SendMessage with to: 'a888ea2ff2d9175fc' to continue this agent)
&lt;usage>total_tokens: 17757
tool_uses: 10
duration_ms: 69096&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0162cd6e-8057-42e7-94a5-8b74671b73b9",
  "isSidechain": false,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "type": "user",
  "uuid": "b2264798-5f11-4849-91b3-6f44b5928542",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the paper \"Natural Language as Intermediate Representation for Code Debugging\" (arXiv:2505.15356). This was reportedly accepted as an ORAL at EMNLP 2025.\n\nI need to verify:\n1. Does this paper exist?\n2. Was it really accepted at EMNLP 2025 as an Oral?\n3. What is its core method — using NL as intermediate representation for debugging?\n4. What benchmarks and results does it report?\n\nSearch queries:\n- \"arXiv 2505.15356\"\n- \"Natural Language Intermediate Representation Code Debugging EMNLP 2025\"\n- \"NL-Debugging code LLM 2025\"\n- \"site:aclanthology.org 2025.emnlp-main natural language debugging\"\n\nUse WebSearch and WebFetch. Report back with detailed findings.",
    "agentId": "a888ea2ff2d9175fc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Excellent -- I now have all the information needed. Here is the full report.\n\n---\n\n## Verification Report: \"NL-Debugging\" (arXiv:2505.15356)\n\n### 1. Does this paper exist?\n\n**Yes.** The paper is real and fully published:\n\n- **Title:** \"NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging\"\n- **arXiv ID:** 2505.15356 (submitted May 21, 2025; revised October 29, 2025)\n- **Authors:** Weiming Zhang, Qingyao Li, Xinyi Dai, Jizheng Chen, Kounianhua Du, Weiwen Liu, Yasheng Wang, Ruiming Tang, Yong Yu, and Weinan Zhang\n- **DOI:** 10.18653/v1/2025.emnlp-main.80\n- **Pages:** 1533--1549 in the proceedings\n\n### 2. Was it accepted at EMNLP 2025 as an Oral?\n\n**Yes, confirmed.** The paper appears in the EMNLP 2025 main conference proceedings (published by the Association for Computational Linguistics, Suzhou, China, November 2025). The first author's homepage (Weiming Zhang) explicitly lists it as an **Oral Presentation** at EMNLP 2025, announced in August 2025.\n\n### 3. Core Method\n\nThe NL-Debugging framework uses natural language as an intermediate representation for code debugging. It operates in three stages:\n\n1. **Backtranslation** -- The buggy code is converted into a natural language representation that captures its underlying algorithmic logic.\n2. **Natural Language Refinement** -- Execution feedback (error messages, test case failures) is analyzed to identify discrepancies between intended and actual behavior. The erroneous natural language representation is then modified at the NL level.\n3. **Regeneration (Forward Translation)** -- The refined natural language representation is translated back into executable code.\n\nA key finding is that among different NL formats tested (pseudocode, key points, and sketch), **sketch-based NL-Debugging** yields the best results by a significant margin. Sketches provide more detailed natural language descriptions, enabling greater flexibility and a larger modification space compared to code-level debugging.\n\n### 4. Benchmarks and Results\n\n**Datasets used:**\n- **APPS** -- 3 difficulty levels (introductory, interview, competition), 100 problems per level\n- **Codeforces** -- 3 rating levels (1200, 1500, 1800), 100 problems per level\n\n**LLM backbones tested:**\n- GPT-4o-mini\n- Claude 3.5-Sonnet\n- DeepSeek-Coder-V2-Lite (16B, locally deployed)\n\n**Key quantitative results (pass rate, baseline vs. NL-Debugging):**\n\n| Dataset | Level | Baseline | NL-Debugging |\n|---|---|---|---|\n| APPS (GPT-4o-mini) | Introductory | 56.45% | 71.36% |\n| APPS (GPT-4o-mini) | Competition | 34.67% | 44.17% |\n| Codeforces (Claude 3.5-Sonnet) | Rating 1200 | 68.59% | 85.82% |\n| Codeforces (Claude 3.5-Sonnet) | Rating 1800 | 42.06% | 61.28% |\n\nThe results show consistent and substantial improvements across all difficulty levels, models, and datasets, demonstrating that debugging at the natural language level outperforms traditional code-level debugging approaches.\n\n---\n\nSources:\n- [arXiv:2505.15356 Abstract](https://arxiv.org/abs/2505.15356)\n- [arXiv:2505.15356 Full HTML](https://arxiv.org/html/2505.15356)\n- [ACL Anthology: 2025.emnlp-main.80](https://aclanthology.org/2025.emnlp-main.80/)\n- [EMNLP 2025 Accepted Main Conference Papers](https://2025.emnlp.org/program/main_papers/)\n- [Weiming Zhang Homepage](https://wmzhang02.github.io/)"
      }
    ],
    "totalDurationMs": 69096,
    "totalTokens": 17757,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 259,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 15550,
      "output_tokens": 1053,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 895
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 259,
          "output_tokens": 1053,
          "cache_read_input_tokens": 15550,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 895,
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
  "sourceToolAssistantUUID": "0162cd6e-8057-42e7-94a5-8b74671b73b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T01:57:10.283Z_

<details><summary>↩ Tool result · `toolu_015ndzMFhCXG5JkF1jabY18Y`</summary>

```text
I now have comprehensive information from the actual paper. Here is my detailed report.

---

## Findings: arXiv:2506.18315

### 1. Does this paper exist?

**Yes.** The paper is real and available at [https://arxiv.org/abs/2506.18315](https://arxiv.org/abs/2506.18315).

- **Title:** "Use Property-Based Testing to Bridge LLM Code Generation and Validation"
- **Revised title (v2):** "Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback"
- **Authors:** Lehan He, Zeren Chen, Zhe Zhang, Jing Shao, Xiang Gao, Lu Sheng (Beihang University / Shanghai AI Laboratory)
- **GitHub:** https://github.com/HeLeHanPrivate/PBTwithCodeGen

### 2. Actual Results

The paper evaluates on **three benchmarks only: HumanEval, MBPP, and LiveCodeBench**. It does **NOT** evaluate on CodeContests or SWE-bench.

**Key results from the paper itself:**

- PGS achieves **23.1% to 37.3% relative improvement** in pass@1 over established TDD methods on problems that are challenging for direct prompting.
- Average absolute pass@1 improvement of **9.2%** over prompting techniques.
- Average absolute RSR (Repair Success Rate) improvement of approximately **15.7%** over TDD baselines on HumanEval and MBPP.
- Gains range from **4.2%** (Qwen2.5-Coder on LiveCodeBench) to **17.4%** (DeepSeek-R1-Distilled-32B on MBPP).
- On LiveCodeBench Hard tasks with DeepSeek-R1-Distilled-32B, PGS achieves **40.7%** pass@1 vs. **28.1%** for direct prompting.
- PBT-driven feedback boosted repair success from **46.6%** (public tests only) to **75.9%** (with PBT) on a challenging subset of LiveCodeBench.
- "Wrong Answer" outcomes dropped from **25.3%** to **10.5%** with PGS on LiveCodeBench.
- Bug fix rate reported as **1.4x-1.6x** higher than strongest debugging approaches.

**Models tested:** DeepSeek-Coder-V2, Qwen2.5-Coder, DeepSeek-R1-Distilled-32B (three models, not six).

**Important note about fabricated results:** The earlier WebFetch of the HTML paper returned a table with results for "DeepSeek-V3.1" and "Claude-4" on HumanEval, MBPP, LiveCodeBench, CodeContests, and SWE-bench. These results do NOT appear in the actual paper. The paper explicitly states it uses only three LLMs and three benchmarks. Those additional numbers with six models and five benchmarks were fabricated by the AI summarization layer and should be disregarded entirely.

### 3. Core Method

**Property-Generated Solver (PGS)** is a two-agent framework:

- **Generator agent:** Produces initial code from a natural language specification, then iteratively refines it based on feedback.
- **Tester agent:** Manages the Property-Based Testing lifecycle:
  1. **Property Definition:** Derives high-level abstract properties/invariants from the problem specification (e.g., "the product of prime factors must equal the input number" for a factorization problem).
  2. **Property Instantiation:** Translates properties into executable checking code, validates them against public test cases, and generates diverse test inputs.
  3. **Property-Driven Validation:** Runs the candidate code against property checks and public tests.
  4. **Feedback Formulation:** Selects the **shortest/simplest** failing input (inspired by delta debugging) to provide concise, actionable feedback to the Generator.
  5. **Code Refinement:** The Generator fixes the code based on this feedback.

The key insight is that LLMs are **better at generating validation properties** than at generating correct code directly. By validating invariants (e.g., "output is non-decreasing" for sorting) rather than predicting exact outputs, PGS breaks the "cycle of self-deception" where LLM-generated tests share the same biases as LLM-generated code.

The iterative cycle runs for up to **5 iterations**, with up to 5 properties per problem and 20 synthesized PBT inputs.

### 4. Publication/Revision Dates

- **v1:** June 23, 2025
- **v2 (current):** May 1, 2026

The v2 revision changed the title to "Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback" and may have updated results (the v2 abstract mentions "up to 13.4% improvement in pass@1" and "over 64% fix rate").

Sources:
- [arXiv:2506.18315 Abstract](https://arxiv.org/abs/2506.18315)
- [arXiv:2506.18315 Full HTML (v1)](https://arxiv.org/html/2506.18315v1)
- [HuggingFace Paper Page](https://huggingface.co/papers/2506.18315)
- [Semantic Scholar](https://www.semanticscholar.org/paper/Use-Property-Based-Testing-to-Bridge-LLM-Code-and-He-Chen/976a0c7318053c050609c4732729ef37eddc0199)
- [AI-SCHOLAR Summary](https://ai-scholar.tech/en/articles/llm-paper/property-generated-solver)
- [alphaXiv Discussion](https://www.alphaxiv.org/overview/2506.18315v1)

agentId: a49185959fb573e94 (use SendMessage with to: 'a49185959fb573e94' to continue this agent)
&lt;usage>total_tokens: 43487
tool_uses: 12
duration_ms: 104239&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26d7ea99-b51e-416a-a78b-96cf00a10b65",
  "isSidechain": false,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "type": "user",
  "uuid": "d403719f-b73a-4d2c-b049-3aa153db4d53",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the paper \"Use Property-Based Testing to Bridge LLM Code Generation and Validation\" (arXiv:2506.18315). This is also known as \"PGS\" or \"Property-Generated Solver.\" \n\nI need to verify:\n1. Does this paper exist?\n2. What are its actual results (HumanEval, MBPP, LiveCodeBench, CodeContests, SWE-bench)?\n3. What is its core method?\n4. When was it published/revised?\n\nSearch queries to try:\n- \"arXiv 2506.18315\"\n- \"Property-Based Testing Bridge LLM Code Generation Validation\"\n- \"PGS property generated solver code LLM\"\n- \"property-based testing LLM code generation 2025\"\n\nUse WebSearch and WebFetch to find and read the actual paper. Report back with detailed findings.",
    "agentId": "a49185959fb573e94",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information from the actual paper. Here is my detailed report.\n\n---\n\n## Findings: arXiv:2506.18315\n\n### 1. Does this paper exist?\n\n**Yes.** The paper is real and available at [https://arxiv.org/abs/2506.18315](https://arxiv.org/abs/2506.18315).\n\n- **Title:** \"Use Property-Based Testing to Bridge LLM Code Generation and Validation\"\n- **Revised title (v2):** \"Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback\"\n- **Authors:** Lehan He, Zeren Chen, Zhe Zhang, Jing Shao, Xiang Gao, Lu Sheng (Beihang University / Shanghai AI Laboratory)\n- **GitHub:** https://github.com/HeLeHanPrivate/PBTwithCodeGen\n\n### 2. Actual Results\n\nThe paper evaluates on **three benchmarks only: HumanEval, MBPP, and LiveCodeBench**. It does **NOT** evaluate on CodeContests or SWE-bench.\n\n**Key results from the paper itself:**\n\n- PGS achieves **23.1% to 37.3% relative improvement** in pass@1 over established TDD methods on problems that are challenging for direct prompting.\n- Average absolute pass@1 improvement of **9.2%** over prompting techniques.\n- Average absolute RSR (Repair Success Rate) improvement of approximately **15.7%** over TDD baselines on HumanEval and MBPP.\n- Gains range from **4.2%** (Qwen2.5-Coder on LiveCodeBench) to **17.4%** (DeepSeek-R1-Distilled-32B on MBPP).\n- On LiveCodeBench Hard tasks with DeepSeek-R1-Distilled-32B, PGS achieves **40.7%** pass@1 vs. **28.1%** for direct prompting.\n- PBT-driven feedback boosted repair success from **46.6%** (public tests only) to **75.9%** (with PBT) on a challenging subset of LiveCodeBench.\n- \"Wrong Answer\" outcomes dropped from **25.3%** to **10.5%** with PGS on LiveCodeBench.\n- Bug fix rate reported as **1.4x-1.6x** higher than strongest debugging approaches.\n\n**Models tested:** DeepSeek-Coder-V2, Qwen2.5-Coder, DeepSeek-R1-Distilled-32B (three models, not six).\n\n**Important note about fabricated results:** The earlier WebFetch of the HTML paper returned a table with results for \"DeepSeek-V3.1\" and \"Claude-4\" on HumanEval, MBPP, LiveCodeBench, CodeContests, and SWE-bench. These results do NOT appear in the actual paper. The paper explicitly states it uses only three LLMs and three benchmarks. Those additional numbers with six models and five benchmarks were fabricated by the AI summarization layer and should be disregarded entirely.\n\n### 3. Core Method\n\n**Property-Generated Solver (PGS)** is a two-agent framework:\n\n- **Generator agent:** Produces initial code from a natural language specification, then iteratively refines it based on feedback.\n- **Tester agent:** Manages the Property-Based Testing lifecycle:\n  1. **Property Definition:** Derives high-level abstract properties/invariants from the problem specification (e.g., \"the product of prime factors must equal the input number\" for a factorization problem).\n  2. **Property Instantiation:** Translates properties into executable checking code, validates them against public test cases, and generates diverse test inputs.\n  3. **Property-Driven Validation:** Runs the candidate code against property checks and public tests.\n  4. **Feedback Formulation:** Selects the **shortest/simplest** failing input (inspired by delta debugging) to provide concise, actionable feedback to the Generator.\n  5. **Code Refinement:** The Generator fixes the code based on this feedback.\n\nThe key insight is that LLMs are **better at generating validation properties** than at generating correct code directly. By validating invariants (e.g., \"output is non-decreasing\" for sorting) rather than predicting exact outputs, PGS breaks the \"cycle of self-deception\" where LLM-generated tests share the same biases as LLM-generated code.\n\nThe iterative cycle runs for up to **5 iterations**, with up to 5 properties per problem and 20 synthesized PBT inputs.\n\n### 4. Publication/Revision Dates\n\n- **v1:** June 23, 2025\n- **v2 (current):** May 1, 2026\n\nThe v2 revision changed the title to \"Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback\" and may have updated results (the v2 abstract mentions \"up to 13.4% improvement in pass@1\" and \"over 64% fix rate\").\n\nSources:\n- [arXiv:2506.18315 Abstract](https://arxiv.org/abs/2506.18315)\n- [arXiv:2506.18315 Full HTML (v1)](https://arxiv.org/html/2506.18315v1)\n- [HuggingFace Paper Page](https://huggingface.co/papers/2506.18315)\n- [Semantic Scholar](https://www.semanticscholar.org/paper/Use-Property-Based-Testing-to-Bridge-LLM-Code-and-He-Chen/976a0c7318053c050609c4732729ef37eddc0199)\n- [AI-SCHOLAR Summary](https://ai-scholar.tech/en/articles/llm-paper/property-generated-solver)\n- [alphaXiv Discussion](https://www.alphaxiv.org/overview/2506.18315v1)"
      }
    ],
    "totalDurationMs": 104239,
    "totalTokens": 43487,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11564,
      "cache_read_input_tokens": 30471,
      "output_tokens": 1451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11564
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1451,
          "cache_read_input_tokens": 30471,
          "cache_creation_input_tokens": 11564,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11564,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 10
    }
  },
  "sourceToolAssistantUUID": "26d7ea99-b51e-416a-a78b-96cf00a10b65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d403719f-b73a-4d2c-b049-3aa153db4d53",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Specification-Grounded Code Reasoning at Inference Time",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---

### Tool result

_source line 18 · 2026-05-12T01:58:08.266Z_

<details><summary>↩ Tool result · `toolu_01AAfmLggtAf7coZrsCKstk7`</summary>

```text
I now have comprehensive information on all three papers. Let me compile the final report.

---

Here are the detailed findings for each paper:

---

## Paper 1: ContractEval (arXiv:2510.12047)

**Does the paper exist?** Yes.

**Full Title:** "ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation"

**Authors:** Soohan Lim, Joonghyuk Hahn, Hyunwoo Park, Sang-Ki Ko, Yo-Sub Han

**Venue and Date:** arXiv preprint, first submitted October 14, 2025 (v1), last revised April 20, 2026 (v4). Categorized under cs.AI and cs.SE. No conference venue listed on the preprint itself.

**Core Method:** ContractEval introduces a neuro-symbolic pipeline that pairs LLMs with an SMT solver to evaluate whether generated code properly satisfies contracts (preconditions that reject ill-formed inputs via assertions). The benchmark comprises 364 tasks (built on HumanEval+ and MBPP+) with 4,907 verified contract-violating tests (CVTs). The pipeline works in three stages: (1) an LLM judge reconstructs contract-aware queries and filters misaligned contracts, (2) assertions are translated into SMT-LIB constraints and the solver enumerates feasible violation combinations to generate concrete test inputs, (3) feasibility filtering validates that CVTs genuinely violate intended contracts.

**Key Findings:**
- Under standard prompting, five open-source models (Gemma-3-12B-it, DeepSeek-R1-Distill-Qwen-14B, Qwen3-14B, Phi-4-reasoning, Phi-4-reasoning-plus) achieved pass@1 of 75--82% but **0% contract satisfaction rate (CSR)**.
- With contract specification in the prompt, CSR improved by 23--41 percentage points.
- With example-augmented specification (EAS), CSR reached 49--53% while preserving 92% of pass@1.
- Even functionally correct programs (pass@1=100%) only achieved 51--59% CSR under EAS.
- Commercial models (GPT-4o, Gemini-3-flash) showed similar patterns: 56.51% and 62.94% CSR under EAS respectively.

**Regarding "PACT":** The term PACT does **not** appear in the ContractEval paper (arXiv:2510.12047). However, the same author team (Lim, Hahn, Park, Ko, Han) submitted a related paper to ICLR 2026 titled "Do Large Language Models Respect Contracts? Evaluating and Enforcing Contract-Adherence in Code Generation" which introduces the **PACT** (Program Assessment and Contract-Adherence evaluation) framework. That submission was withdrawn from ICLR 2026 (OpenReview ID: HDSlPuFoEu). ContractEval appears to be a revised/evolved version of that PACT work.

---

## Paper 2: "From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing"

**Does the paper exist?** Yes.

**Full Title:** "From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing"

**Author:** Dibyendu Brinto Bose (Virginia Tech, USA)

**Venue and Date:** Published in the Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering (FSE Companion '25), specifically at the **LLanMER 2025 workshop** (co-located with FSE 2025). Presented June 27, 2025, in Trondheim, Norway. DOI: `10.1145/3696630.3728702`.

**Core Method:** The paper applies Property-Based Testing (PBT) as an alternative/complementary evaluation strategy for LLM-generated code. Rather than relying solely on example-based unit tests (pass@k), PBT generates randomized inputs satisfying declared properties to find counterexamples. The study tested **StarCoder** and **CodeLlama** on the **MBPP** and **HumanEval** benchmarks.

**Key Findings:**
- While pass@k evaluation shows moderate success, PBT exposes additional correctness gaps that unit tests miss.
- **30--32%** of generated solutions only **partially** met correctness properties.
- **18--23%** of generated code **failed** correctness properties entirely.
- Property extraction was incomplete, with **9--13%** of logical constraints missed.
- The paper demonstrates that combining unit testing with property-based testing offers more comprehensive evaluation, revealing "fundamental logical errors" that conventional methods overlook.

---

## Paper 3: "Preconditions and Postconditions as Design Constraints for LLM Code Generation"

**Does the paper exist?** Yes -- in two forms.

**Full Title (IEEE Access):** "Preconditions and Postconditions as Design Constraints for LLM Code Generation"

**Full Title (Thesis):** "A Study of Preconditions and Postconditions as Design Constraints for LLM Code Generation"

**Authors:** Luke Newcomb (with advisor Yoonsik Cheon, Embry-Riddle Aeronautical University)

**Venue and Date:**
- **IEEE Access** journal article (IEEE Xplore document ID: 11218044), published 2025. This is the journal version.
- **Master's thesis** (M.S. in Software Engineering), Embry-Riddle Aeronautical University, Spring 2025, available via Scholarly Commons (commons.erau.edu/edt/927).

**Core Method:** The study uses a Design-by-Contract (DbC) paradigm, providing explicit preconditions and postconditions as formal constraints in LLM prompts for **class-level** code generation tasks (not just function-level). Six state-of-the-art LLMs were evaluated generating complete software implementations of a medium-complexity system from systematically designed class-level specifications. The evaluation uses **pass@k** metrics across **Python, Java, and C++**.

**Key Findings:**
- Incorporating explicit design constraints (preconditions/postconditions) during prompting **significantly boosts initial generation accuracy** compared to natural language descriptions alone.
- The effect was most pronounced in **Python**, with strong improvements also observed in **Java and C++**.
- Models with **fewer parameters or weaker initial performance** saw especially large benefits from adding formal constraints.
- The findings suggest that integrating structured software engineering constraints into LLM-based code generation workflows enhances both accuracy and maintainability.

---

## Summary Table

| Paper | Exists? | Venue | Date | Core Idea |
|-------|---------|-------|------|-----------|
| ContractEval (2510.12047) | Yes | arXiv preprint (cs.AI/cs.SE); PACT variant withdrawn from ICLR 2026 | Oct 2025 (v1), Apr 2026 (v4) | Neuro-symbolic benchmark showing LLMs achieve 0% contract satisfaction under standard prompting despite 75-82% pass@1 |
| From Prompts to Properties | Yes | FSE Companion '25 / LLanMER 2025 workshop (ACM) | June 2025 | PBT reveals 30-32% partial and 18-23% full failures in LLM code that pass@k misses |
| Preconditions & Postconditions | Yes | IEEE Access + ERAU Master's thesis | 2025 | DbC constraints in prompts significantly boost class-level code generation accuracy, especially for smaller models |

Sources:
- [ContractEval - arXiv:2510.12047](https://arxiv.org/abs/2510.12047)
- [ContractEval - Full HTML](https://arxiv.org/html/2510.12047)
- [PACT / "Do LLMs Respect Contracts?" - OpenReview (ICLR 2026 withdrawn)](https://openreview.net/forum?id=HDSlPuFoEu)
- [From Prompts to Properties - ACM DL](https://dl.acm.org/doi/10.1145/3696630.3728702)
- [From Prompts to Properties - LLanMER 2025 program](https://conf.researchr.org/details/llanmer-2025/llanmer-2025-papers/7/From-Prompts-to-Properties-Rethinking-LLM-Code-Generation-with-Property-Based-Testin)
- [From Prompts to Properties - VTechWorks](https://vtechworks.lib.vt.edu/items/702015c7-5db2-4dfc-a098-a8333c50faf6)
- [Preconditions & Postconditions - IEEE Xplore](https://ieeexplore.ieee.org/document/11218044/)
- [Preconditions & Postconditions - ERAU Thesis](https://commons.erau.edu/edt/927/)

agentId: a028714c9c51a69ff (use SendMessage with to: 'a028714c9c51a69ff' to continue this agent)
&lt;usage>total_tokens: 23585
tool_uses: 19
duration_ms: 153429&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b132215b-3b89-4c01-9391-2b341b5c9308",
  "isSidechain": false,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "type": "user",
  "uuid": "2f6c8795-a033-42f8-9cfc-717f68b9a437",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for these papers:\n\n1. ContractEval / PACT (arXiv:2510.12047) — about benchmarking LLM contract satisfaction\n2. \"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing\" (FSE 2025 / LLanMER workshop)\n3. \"Preconditions and Postconditions as Design Constraints for LLM Code Generation\" (IEEE Access 2024/2025)\n\nFor each, I need:\n- Does the paper exist?\n- Core method and findings\n- Venue and date\n\nSearch queries:\n- \"arXiv 2510.12047\"\n- \"ContractEval PACT LLM contract satisfaction\"\n- \"From Prompts to Properties property-based testing LLM code generation FSE 2025\"\n- \"Preconditions Postconditions Design Constraints LLM Code Generation IEEE Access\"\n\nUse WebSearch and WebFetch. Report detailed findings for each.",
    "agentId": "a028714c9c51a69ff",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on all three papers. Let me compile the final report.\n\n---\n\nHere are the detailed findings for each paper:\n\n---\n\n## Paper 1: ContractEval (arXiv:2510.12047)\n\n**Does the paper exist?** Yes.\n\n**Full Title:** \"ContractEval: A Benchmark for Evaluating Contract-Satisfying Assertions in Code Generation\"\n\n**Authors:** Soohan Lim, Joonghyuk Hahn, Hyunwoo Park, Sang-Ki Ko, Yo-Sub Han\n\n**Venue and Date:** arXiv preprint, first submitted October 14, 2025 (v1), last revised April 20, 2026 (v4). Categorized under cs.AI and cs.SE. No conference venue listed on the preprint itself.\n\n**Core Method:** ContractEval introduces a neuro-symbolic pipeline that pairs LLMs with an SMT solver to evaluate whether generated code properly satisfies contracts (preconditions that reject ill-formed inputs via assertions). The benchmark comprises 364 tasks (built on HumanEval+ and MBPP+) with 4,907 verified contract-violating tests (CVTs). The pipeline works in three stages: (1) an LLM judge reconstructs contract-aware queries and filters misaligned contracts, (2) assertions are translated into SMT-LIB constraints and the solver enumerates feasible violation combinations to generate concrete test inputs, (3) feasibility filtering validates that CVTs genuinely violate intended contracts.\n\n**Key Findings:**\n- Under standard prompting, five open-source models (Gemma-3-12B-it, DeepSeek-R1-Distill-Qwen-14B, Qwen3-14B, Phi-4-reasoning, Phi-4-reasoning-plus) achieved pass@1 of 75--82% but **0% contract satisfaction rate (CSR)**.\n- With contract specification in the prompt, CSR improved by 23--41 percentage points.\n- With example-augmented specification (EAS), CSR reached 49--53% while preserving 92% of pass@1.\n- Even functionally correct programs (pass@1=100%) only achieved 51--59% CSR under EAS.\n- Commercial models (GPT-4o, Gemini-3-flash) showed similar patterns: 56.51% and 62.94% CSR under EAS respectively.\n\n**Regarding \"PACT\":** The term PACT does **not** appear in the ContractEval paper (arXiv:2510.12047). However, the same author team (Lim, Hahn, Park, Ko, Han) submitted a related paper to ICLR 2026 titled \"Do Large Language Models Respect Contracts? Evaluating and Enforcing Contract-Adherence in Code Generation\" which introduces the **PACT** (Program Assessment and Contract-Adherence evaluation) framework. That submission was withdrawn from ICLR 2026 (OpenReview ID: HDSlPuFoEu). ContractEval appears to be a revised/evolved version of that PACT work.\n\n---\n\n## Paper 2: \"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing\"\n\n**Does the paper exist?** Yes.\n\n**Full Title:** \"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing\"\n\n**Author:** Dibyendu Brinto Bose (Virginia Tech, USA)\n\n**Venue and Date:** Published in the Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering (FSE Companion '25), specifically at the **LLanMER 2025 workshop** (co-located with FSE 2025). Presented June 27, 2025, in Trondheim, Norway. DOI: `10.1145/3696630.3728702`.\n\n**Core Method:** The paper applies Property-Based Testing (PBT) as an alternative/complementary evaluation strategy for LLM-generated code. Rather than relying solely on example-based unit tests (pass@k), PBT generates randomized inputs satisfying declared properties to find counterexamples. The study tested **StarCoder** and **CodeLlama** on the **MBPP** and **HumanEval** benchmarks.\n\n**Key Findings:**\n- While pass@k evaluation shows moderate success, PBT exposes additional correctness gaps that unit tests miss.\n- **30--32%** of generated solutions only **partially** met correctness properties.\n- **18--23%** of generated code **failed** correctness properties entirely.\n- Property extraction was incomplete, with **9--13%** of logical constraints missed.\n- The paper demonstrates that combining unit testing with property-based testing offers more comprehensive evaluation, revealing \"fundamental logical errors\" that conventional methods overlook.\n\n---\n\n## Paper 3: \"Preconditions and Postconditions as Design Constraints for LLM Code Generation\"\n\n**Does the paper exist?** Yes -- in two forms.\n\n**Full Title (IEEE Access):** \"Preconditions and Postconditions as Design Constraints for LLM Code Generation\"\n\n**Full Title (Thesis):** \"A Study of Preconditions and Postconditions as Design Constraints for LLM Code Generation\"\n\n**Authors:** Luke Newcomb (with advisor Yoonsik Cheon, Embry-Riddle Aeronautical University)\n\n**Venue and Date:**\n- **IEEE Access** journal article (IEEE Xplore document ID: 11218044), published 2025. This is the journal version.\n- **Master's thesis** (M.S. in Software Engineering), Embry-Riddle Aeronautical University, Spring 2025, available via Scholarly Commons (commons.erau.edu/edt/927).\n\n**Core Method:** The study uses a Design-by-Contract (DbC) paradigm, providing explicit preconditions and postconditions as formal constraints in LLM prompts for **class-level** code generation tasks (not just function-level). Six state-of-the-art LLMs were evaluated generating complete software implementations of a medium-complexity system from systematically designed class-level specifications. The evaluation uses **pass@k** metrics across **Python, Java, and C++**.\n\n**Key Findings:**\n- Incorporating explicit design constraints (preconditions/postconditions) during prompting **significantly boosts initial generation accuracy** compared to natural language descriptions alone.\n- The effect was most pronounced in **Python**, with strong improvements also observed in **Java and C++**.\n- Models with **fewer parameters or weaker initial performance** saw especially large benefits from adding formal constraints.\n- The findings suggest that integrating structured software engineering constraints into LLM-based code generation workflows enhances both accuracy and maintainability.\n\n---\n\n## Summary Table\n\n| Paper | Exists? | Venue | Date | Core Idea |\n|-------|---------|-------|------|-----------|\n| ContractEval (2510.12047) | Yes | arXiv preprint (cs.AI/cs.SE); PACT variant withdrawn from ICLR 2026 | Oct 2025 (v1), Apr 2026 (v4) | Neuro-symbolic benchmark showing LLMs achieve 0% contract satisfaction under standard prompting despite 75-82% pass@1 |\n| From Prompts to Properties | Yes | FSE Companion '25 / LLanMER 2025 workshop (ACM) | June 2025 | PBT reveals 30-32% partial and 18-23% full failures in LLM code that pass@k misses |\n| Preconditions & Postconditions | Yes | IEEE Access + ERAU Master's thesis | 2025 | DbC constraints in prompts significantly boost class-level code generation accuracy, especially for smaller models |\n\nSources:\n- [ContractEval - arXiv:2510.12047](https://arxiv.org/abs/2510.12047)\n- [ContractEval - Full HTML](https://arxiv.org/html/2510.12047)\n- [PACT / \"Do LLMs Respect Contracts?\" - OpenReview (ICLR 2026 withdrawn)](https://openreview.net/forum?id=HDSlPuFoEu)\n- [From Prompts to Properties - ACM DL](https://dl.acm.org/doi/10.1145/3696630.3728702)\n- [From Prompts to Properties - LLanMER 2025 program](https://conf.researchr.org/details/llanmer-2025/llanmer-2025-papers/7/From-Prompts-to-Properties-Rethinking-LLM-Code-Generation-with-Property-Based-Testin)\n- [From Prompts to Properties - VTechWorks](https://vtechworks.lib.vt.edu/items/702015c7-5db2-4dfc-a098-a8333c50faf6)\n- [Preconditions & Postconditions - IEEE Xplore](https://ieeexplore.ieee.org/document/11218044/)\n- [Preconditions & Postconditions - ERAU Thesis](https://commons.erau.edu/edt/927/)"
      }
    ],
    "totalDurationMs": 153429,
    "totalTokens": 23585,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 459,
      "cache_read_input_tokens": 20916,
      "output_tokens": 2209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 459
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2209,
          "cache_read_input_tokens": 20916,
          "cache_creation_input_tokens": 459,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 459,
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
  "sourceToolAssistantUUID": "b132215b-3b89-4c01-9391-2b341b5c9308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T01:58:11.246Z_

<details><summary>↩ Tool result · `toolu_01K8RT3VcimCYW8pY7Rb66BU`</summary>

```text
Here is a comprehensive report of findings across all requested topics.

---

## 1. SWE-bench Verified -- Current Top Scores, Contamination, and SWE-bench Pro

### Top Scores (May 2026)
As of May 7, 2026, the SWE-bench Verified leaderboard is led by:
- **Claude Mythos Preview**: 93.9%
- **Claude Opus 4.7 (Adaptive)**: 87.6%
- **GPT-5.3 Codex**: 85%

There are 89 evaluated AI models on the leaderboard.

### Contamination Concerns
In **February 2026**, OpenAI published a detailed analysis titled "Why SWE-bench Verified no longer measures frontier coding capabilities" and announced they would stop reporting Verified scores. Key findings:

- Every frontier model tested (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could **reproduce verbatim gold patches** or problem statement specifics for certain SWE-bench Verified tasks.
- **59.4% of the hardest unsolved problems had flawed test cases.**
- GPT-5.2 solved 31 tasks that OpenAI identified as "almost impossible to solve," which triggered the contamination investigation.
- The root cause is that SWE-bench Verified and the underlying repositories are open-source and broadly discussed, making contamination avoidance difficult.

### SWE-bench Pro
SWE-bench Pro is the recommended replacement. Key characteristics:
- **1,865 long-horizon tasks** from 41 real repositories across Python, Go, TypeScript, and JavaScript.
- Every task requires at least 10 lines of change; 100+ tasks require more than 100 lines.
- Contamination cases are "significantly rarer and less egregious" -- no model produced a complete verbatim gold patch.

**SWE-bench Pro leaderboard (May 2026):**
- Claude Mythos Preview: **77.8%**
- Claude Opus 4.7 (Adaptive): **64.3%**
- GPT-5.5: **58.6%**

---

## 2. CodeContests -- Current Best Training-Free/Inference-Time Methods

### EG-CFG (Execution-Guided Classifier-Free Guidance)
The current state-of-the-art on CodeContests is **EG-CFG**, achieving **60.6% accuracy** using DeepSeek-V3-0324. This is a **training-free, inference-time method** that:

- Injects real-time execution feedback directly into the model's decoding loop.
- Uses a multi-stage process: beam search for candidate completions per line, execution of candidates against test cases, and incorporation of signals into prompts during generation.
- Significantly surpasses the DeepSeek-V3 baseline and prior methods like MapCoder, LPW, and CodeSim.

Beyond CodeContests, EG-CFG also achieves: 99.4% on HumanEval, 96.6% on MBPP, 73.0% on MBPP-ET, 89.02% on HumanEval-ET, and 69.9% on DS-1000.

### RLEF (Training-Based but Relevant)
RLEF (Reinforcement Learning from Execution Feedback), published at ICML 2025, is a complementary training-based approach that teaches models to leverage execution feedback iteratively. An RLEF-trained 70B model achieved SOTA on CodeContests while reducing sample requirements by an order of magnitude. The 8B RLEF model outperformed AlphaCodium with 100 samples.

---

## 3. DebugBench -- Current Best Methods

DebugBench (4,253 instances covering 4 major bug categories and 18 minor types in C++, Java, and Python) was originally published in 2024. Key findings from the original work:

- Closed-source models exhibit inferior debugging performance compared to humans.
- Open-source models have relatively lower pass rates.
- Incorporating runtime feedback has a clear but not always helpful impact.
- Strong correlation between debugging and code generation ability for closed-source models.

As of 2026, **no specific new SOTA results on DebugBench itself** appeared in the search results. The benchmark appears to have been somewhat eclipsed by the broader shift toward agentic evaluation frameworks (like SWE-bench Pro) that inherently test debugging as part of long-horizon tasks. The leading coding models in 2026 (GPT-5.5 xhigh, GLM-4.7 Thinking, DeepSeek V3.2) are cited as top performers on general coding benchmarks but without specific DebugBench numbers.

---

## 4. HumanEval/MBPP -- Current Saturation Level

**Both benchmarks are effectively saturated for frontier models.** Multiple frontier models score above 90% on MBPP and near-perfect on HumanEval. EG-CFG with DeepSeek-V3 achieves **99.4% on HumanEval** and **96.6% on MBPP**.

To address saturation, researchers have developed:
- **HumanEval Pro and MBPP Pro** (ACL 2025 Findings): These evaluate LLMs on self-invoking code generation, where models must generate code that calls other generated functions. Most LLMs that excel on traditional versions show declining performance on these variants.
- **HumanEval-ET and MBPP-ET**: Extended test versions with more rigorous test suites.
- **BigCodeBench-Lite Pro**: Another harder alternative.

The community consensus is that HumanEval and MBPP no longer differentiate between frontier models and should not be used as primary evaluation metrics.

---

## 5. New Training-Free Inference-Time Code Improvement Methods (2026)

### Think Anywhere (arXiv:2603.29957, March 2026)
A novel reasoning mechanism enabling LLMs to invoke thinking on-demand at any token position during code generation, rather than only at the beginning:
- Shortens the upfront thinking phase while adding `&lt;thinkanywhere>` tokens where deliberation is needed.
- Achieves **17.3% pass@1 on AIME 2024** (vs. 5.3% base, 6.0% GRPO).
- Generates fewer total tokens than GRPO and CoT baselines.

### PonderTTT (arXiv:2601.00894, January 2026)
Adaptive compute allocation using Test-Time Training with a training-free gating mechanism:
- Uses the TTT layer's self-supervised reconstruction loss to selectively trigger updates.
- The gating decision requires no learned classifier -- only a single scalar threshold calibrated on unlabeled data.
- Achieves **82-89% Oracle Recovery** while being fully training-free, outperforming Random Skip baselines by up to 16%.

### EG-CFG (described above)
The execution-guided classifier-free guidance method that steers decoding using real-time execution feedback -- fully training-free, achieving SOTA on CodeContests.

---

## 6. Specification-Guided Code Generation (2026)

### Academic Research
- **CURRANTE** (SANER 2026): A VS Code extension enabling human-in-the-loop specification-driven code generation through three stages -- Specification, Tests, and Function.
- **SpecOps 2026**: The 1st International Workshop on Specification-Driven Development Life Cycle (co-located with SPLASH/ISSTA 2026), focused on how AI-powered tools can transform specifications from static documentation into living, executable drivers.
- **Grounding Code Generation with Input-Output Specifications**: Research on using I/O specifications to ground code generation (OpenReview).

### Industry Adoption
Specification-driven development (SDD) has become mainstream in 2026:
- **Amazon Kiro** shipped with built-in Spec Mode.
- **Cursor and Windsurf** have plan-before-code workflows.
- Specs are treated as "living, executable contracts" that constrain what AI agents generate and serve as validation gates.

---

## 7. Property-Based Testing + Code LLMs (2026)

### Property-Generated Solver Framework
A novel framework using Property-Based Testing (PBT) to validate high-level program properties instead of specific I/O examples:
- Uses two collaborative LLM agents: a **Generator** for code generation/refinement and a **Tester** managing the PBT lifecycle.
- Achieves **23.1% to 37.3% relative pass@1 improvements** over established TDD methods.

### PropGen (April 2026)
Automates property construction for mobile app testing using LLMs:
- Generated 985 properties, of which 912 were valid.
- Found 25 previously unknown functional bugs in latest app versions.

### Combined Approaches
Research shows that combining property-based testing with example-based testing improves bug detection from 68.75% (either alone) to **81.25%** (combined).

---

## 8. Execution-Grounded Code Reasoning (2026)

### Structured SE Agents (arXiv:2602.04640)
Proposes using finite-state machine abstractions with explicit pre- and post-conditions for agent reasoning, leading to more stable and accurate multi-step reasoning.

### Agentic Execution Grounding (arXiv:2604.10800, April 2026)
A cross-language vulnerability lifecycle framework with three LLM-driven reasoning stages: hybrid structural-semantic detection, execution-grounded agentic validation, and validation-aware iterative repair.

### TraceLift (arXiv:2605.03862, May 2026)
An executor-grounded training framework for reasoning planners that rewards trajectories using both rubric-based reasoning quality and measured uplift on a frozen executor.

### Code Execution as Supervision (EMNLP 2025)
Leverages code execution traces as verifiable, scalable supervision for enhancing step-by-step reasoning in LLMs by transforming execution traces into natural language chain-of-thought reasoning.

---

## 9. Qwen3-Coder Status and Availability

### Qwen3-Coder-Next (February 2026)
- Released **February 4, 2026**.
- **3B activated parameters, 80B total parameters** (mixture-of-experts).
- **256K context length**.
- Achieves **70%+ on SWE-bench Verified** using SWE-Agent scaffold.
- Pricing: $0.110/M input tokens, $0.800/M output tokens.
- Excels at long-horizon reasoning, complex tool usage, and recovery from execution failures.

### Qwen3-Coder 480B A35B Instruct
- A larger variant released in mid-2025.
- 480B total parameters with 35B activated.
- Scores 25 on Artificial Analysis Intelligence Index (above median of 23 for similar open-weight models).
- Performance comparable to Claude Sonnet on agentic coding and browser-use tasks.

### Qwen3-Coder 30B A3B Instruct
- A smaller variant also available, targeting local/edge deployment.

### Broader Qwen Ecosystem
The Qwen team has continued development with **Qwen3.6** now on GitHub, and **Qwen3.6-Max-Preview** available as a preview model.

---

Sources:
- [Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)
- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%](https://www.morphllm.com/swe-bench-pro)
- [SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean](https://www.codeant.ai/blogs/swe-bench-scores)
- [OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)
- [Is SWE-bench Verified Contaminated? OpenAI Shifts to SWE-bench Pro | CodeSOTA](https://www.codesota.com/news/swe-bench-contamination-debate)
- [SWE-Bench Pro Leaderboard AI Coding Benchmark | Scale](https://labs.scale.com/leaderboard/swe_bench_pro_public)
- [SWE-bench Pro Benchmark 2026: 30 LLM scores | BenchLM.ai](https://benchlm.ai/benchmarks/swePro)
- [SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? | OpenReview](https://openreview.net/forum?id=9R2iUHhVfr)
- [SWE-Bench Verified Benchmark Leaderboard](https://llm-stats.com/benchmarks/swe-bench-verified)
- [EG-CFG GitHub Repository](https://github.com/boazlavon/eg_cfg)
- [Execution Guided Line-by-Line Code Generation | arXiv](https://arxiv.org/abs/2506.10948)
- [EG-CFG: Enhancing Code Generation with Real-Time Execution Feedback | MarkTechPost](https://www.marktechpost.com/2025/07/18/eg-cfg-enhancing-code-generation-with-real-time-execution-feedback/)
- [DebugBench: Evaluating Debugging Capability of Large Language Models | arXiv](https://arxiv.org/abs/2401.04621)
- [Code Generation Benchmarks 2026: SOTA LLMs | CodeSOTA](https://www.codesota.com/code-generation)
- [HumanEval Pro and MBPP Pro | arXiv](https://arxiv.org/abs/2412.21199)
- [EvalPlus Leaderboard](https://evalplus.github.io/leaderboard.html)
- [Think Anywhere in Code Generation | arXiv](https://arxiv.org/abs/2603.29957)
- [When to Ponder: Adaptive Compute Allocation for Code Generation via Test-Time Training | arXiv](https://arxiv.org/abs/2601.00894)
- [Understanding Specification-Driven Code Generation with LLMs | arXiv](https://arxiv.org/abs/2601.03878)
- [SpecOps 2026 Workshop](https://conf.researchr.org/home/splash-issta-2026/specops-2026)
- [From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing | ACM](https://dl.acm.org/doi/10.1145/3696630.3728702)
- [Use Property-Based Testing to Bridge LLM Code Generation and Validation | arXiv](https://arxiv.org/abs/2506.18315)
- [Towards Structured, State-Aware, and Execution-Grounded Reasoning for SE Agents | arXiv](https://arxiv.org/html/2602.04640)
- [Verify Before You Fix: Agentic Execution Grounding | arXiv](https://arxiv.org/abs/2604.10800v1)
- [Correct Is Not Enough: Training Reasoning Planners with Executor-Grounded Rewards | arXiv](https://arxiv.org/abs/2605.03862)
- [RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning | arXiv](https://arxiv.org/abs/2410.02089)
- [Qwen3-Coder-Next | Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-Next)
- [Qwen3-Coder-Next: Pushing Small Hybrid Models | Qwen Blog](https://qwen.ai/blog?id=qwen3-coder-next)
- [Qwen3-Coder GitHub Repository](https://github.com/QwenLM/Qwen3-Coder)
- [Qwen3 Coder 480B Analysis | Artificial Analysis](https://artificialanalysis.ai/models/qwen3-coder-480b-a35b-instruct)
- [The End of SWE-Bench Verified | Latent Space](https://www.latent.space/p/swe-bench-dead)
- [Best LLM for Coding in 2026 | WhatLLM.org](https://whatllm.org/best-llm-for-coding)

agentId: ad3a73c00bdf3d34a (use SendMessage with to: 'ad3a73c00bdf3d34a' to continue this agent)
&lt;usage>total_tokens: 28676
tool_uses: 16
duration_ms: 150262&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "511b7672-7097-4db3-b827-5b9b5659c1cc",
  "isSidechain": false,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "type": "user",
  "uuid": "70de90c2-5540-437d-97de-1c29c82dcbf4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the latest state-of-the-art on these code benchmarks as of May 2026:\n\n1. SWE-bench Verified — current top scores, contamination concerns, SWE-bench Pro status\n2. CodeContests — current best training-free/inference-time methods\n3. DebugBench — current best methods for LLM code debugging\n4. HumanEval/MBPP — current saturation level\n\nAlso search for:\n- Any new training-free inference-time code improvement methods from 2026\n- \"specification guided code generation 2026\"\n- \"property-based testing code LLM 2026\"\n- \"execution grounded code reasoning 2026\"\n- Qwen3-Coder status and availability\n\nSearch queries:\n- \"SWE-bench Verified contamination 2026 OpenAI\"\n- \"SWE-bench Pro benchmark 2026\"\n- \"CodeContests SOTA inference time 2026\"\n- \"DebugBench LLM debugging SOTA 2026\"\n- \"Qwen3 Coder release 2026\"\n- \"training-free code generation improvement 2026 arxiv\"\n\nUse WebSearch. Report detailed findings.",
    "agentId": "ad3a73c00bdf3d34a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive report of findings across all requested topics.\n\n---\n\n## 1. SWE-bench Verified -- Current Top Scores, Contamination, and SWE-bench Pro\n\n### Top Scores (May 2026)\nAs of May 7, 2026, the SWE-bench Verified leaderboard is led by:\n- **Claude Mythos Preview**: 93.9%\n- **Claude Opus 4.7 (Adaptive)**: 87.6%\n- **GPT-5.3 Codex**: 85%\n\nThere are 89 evaluated AI models on the leaderboard.\n\n### Contamination Concerns\nIn **February 2026**, OpenAI published a detailed analysis titled \"Why SWE-bench Verified no longer measures frontier coding capabilities\" and announced they would stop reporting Verified scores. Key findings:\n\n- Every frontier model tested (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could **reproduce verbatim gold patches** or problem statement specifics for certain SWE-bench Verified tasks.\n- **59.4% of the hardest unsolved problems had flawed test cases.**\n- GPT-5.2 solved 31 tasks that OpenAI identified as \"almost impossible to solve,\" which triggered the contamination investigation.\n- The root cause is that SWE-bench Verified and the underlying repositories are open-source and broadly discussed, making contamination avoidance difficult.\n\n### SWE-bench Pro\nSWE-bench Pro is the recommended replacement. Key characteristics:\n- **1,865 long-horizon tasks** from 41 real repositories across Python, Go, TypeScript, and JavaScript.\n- Every task requires at least 10 lines of change; 100+ tasks require more than 100 lines.\n- Contamination cases are \"significantly rarer and less egregious\" -- no model produced a complete verbatim gold patch.\n\n**SWE-bench Pro leaderboard (May 2026):**\n- Claude Mythos Preview: **77.8%**\n- Claude Opus 4.7 (Adaptive): **64.3%**\n- GPT-5.5: **58.6%**\n\n---\n\n## 2. CodeContests -- Current Best Training-Free/Inference-Time Methods\n\n### EG-CFG (Execution-Guided Classifier-Free Guidance)\nThe current state-of-the-art on CodeContests is **EG-CFG**, achieving **60.6% accuracy** using DeepSeek-V3-0324. This is a **training-free, inference-time method** that:\n\n- Injects real-time execution feedback directly into the model's decoding loop.\n- Uses a multi-stage process: beam search for candidate completions per line, execution of candidates against test cases, and incorporation of signals into prompts during generation.\n- Significantly surpasses the DeepSeek-V3 baseline and prior methods like MapCoder, LPW, and CodeSim.\n\nBeyond CodeContests, EG-CFG also achieves: 99.4% on HumanEval, 96.6% on MBPP, 73.0% on MBPP-ET, 89.02% on HumanEval-ET, and 69.9% on DS-1000.\n\n### RLEF (Training-Based but Relevant)\nRLEF (Reinforcement Learning from Execution Feedback), published at ICML 2025, is a complementary training-based approach that teaches models to leverage execution feedback iteratively. An RLEF-trained 70B model achieved SOTA on CodeContests while reducing sample requirements by an order of magnitude. The 8B RLEF model outperformed AlphaCodium with 100 samples.\n\n---\n\n## 3. DebugBench -- Current Best Methods\n\nDebugBench (4,253 instances covering 4 major bug categories and 18 minor types in C++, Java, and Python) was originally published in 2024. Key findings from the original work:\n\n- Closed-source models exhibit inferior debugging performance compared to humans.\n- Open-source models have relatively lower pass rates.\n- Incorporating runtime feedback has a clear but not always helpful impact.\n- Strong correlation between debugging and code generation ability for closed-source models.\n\nAs of 2026, **no specific new SOTA results on DebugBench itself** appeared in the search results. The benchmark appears to have been somewhat eclipsed by the broader shift toward agentic evaluation frameworks (like SWE-bench Pro) that inherently test debugging as part of long-horizon tasks. The leading coding models in 2026 (GPT-5.5 xhigh, GLM-4.7 Thinking, DeepSeek V3.2) are cited as top performers on general coding benchmarks but without specific DebugBench numbers.\n\n---\n\n## 4. HumanEval/MBPP -- Current Saturation Level\n\n**Both benchmarks are effectively saturated for frontier models.** Multiple frontier models score above 90% on MBPP and near-perfect on HumanEval. EG-CFG with DeepSeek-V3 achieves **99.4% on HumanEval** and **96.6% on MBPP**.\n\nTo address saturation, researchers have developed:\n- **HumanEval Pro and MBPP Pro** (ACL 2025 Findings): These evaluate LLMs on self-invoking code generation, where models must generate code that calls other generated functions. Most LLMs that excel on traditional versions show declining performance on these variants.\n- **HumanEval-ET and MBPP-ET**: Extended test versions with more rigorous test suites.\n- **BigCodeBench-Lite Pro**: Another harder alternative.\n\nThe community consensus is that HumanEval and MBPP no longer differentiate between frontier models and should not be used as primary evaluation metrics.\n\n---\n\n## 5. New Training-Free Inference-Time Code Improvement Methods (2026)\n\n### Think Anywhere (arXiv:2603.29957, March 2026)\nA novel reasoning mechanism enabling LLMs to invoke thinking on-demand at any token position during code generation, rather than only at the beginning:\n- Shortens the upfront thinking phase while adding `&lt;thinkanywhere>` tokens where deliberation is needed.\n- Achieves **17.3% pass@1 on AIME 2024** (vs. 5.3% base, 6.0% GRPO).\n- Generates fewer total tokens than GRPO and CoT baselines.\n\n### PonderTTT (arXiv:2601.00894, January 2026)\nAdaptive compute allocation using Test-Time Training with a training-free gating mechanism:\n- Uses the TTT layer's self-supervised reconstruction loss to selectively trigger updates.\n- The gating decision requires no learned classifier -- only a single scalar threshold calibrated on unlabeled data.\n- Achieves **82-89% Oracle Recovery** while being fully training-free, outperforming Random Skip baselines by up to 16%.\n\n### EG-CFG (described above)\nThe execution-guided classifier-free guidance method that steers decoding using real-time execution feedback -- fully training-free, achieving SOTA on CodeContests.\n\n---\n\n## 6. Specification-Guided Code Generation (2026)\n\n### Academic Research\n- **CURRANTE** (SANER 2026): A VS Code extension enabling human-in-the-loop specification-driven code generation through three stages -- Specification, Tests, and Function.\n- **SpecOps 2026**: The 1st International Workshop on Specification-Driven Development Life Cycle (co-located with SPLASH/ISSTA 2026), focused on how AI-powered tools can transform specifications from static documentation into living, executable drivers.\n- **Grounding Code Generation with Input-Output Specifications**: Research on using I/O specifications to ground code generation (OpenReview).\n\n### Industry Adoption\nSpecification-driven development (SDD) has become mainstream in 2026:\n- **Amazon Kiro** shipped with built-in Spec Mode.\n- **Cursor and Windsurf** have plan-before-code workflows.\n- Specs are treated as \"living, executable contracts\" that constrain what AI agents generate and serve as validation gates.\n\n---\n\n## 7. Property-Based Testing + Code LLMs (2026)\n\n### Property-Generated Solver Framework\nA novel framework using Property-Based Testing (PBT) to validate high-level program properties instead of specific I/O examples:\n- Uses two collaborative LLM agents: a **Generator** for code generation/refinement and a **Tester** managing the PBT lifecycle.\n- Achieves **23.1% to 37.3% relative pass@1 improvements** over established TDD methods.\n\n### PropGen (April 2026)\nAutomates property construction for mobile app testing using LLMs:\n- Generated 985 properties, of which 912 were valid.\n- Found 25 previously unknown functional bugs in latest app versions.\n\n### Combined Approaches\nResearch shows that combining property-based testing with example-based testing improves bug detection from 68.75% (either alone) to **81.25%** (combined).\n\n---\n\n## 8. Execution-Grounded Code Reasoning (2026)\n\n### Structured SE Agents (arXiv:2602.04640)\nProposes using finite-state machine abstractions with explicit pre- and post-conditions for agent reasoning, leading to more stable and accurate multi-step reasoning.\n\n### Agentic Execution Grounding (arXiv:2604.10800, April 2026)\nA cross-language vulnerability lifecycle framework with three LLM-driven reasoning stages: hybrid structural-semantic detection, execution-grounded agentic validation, and validation-aware iterative repair.\n\n### TraceLift (arXiv:2605.03862, May 2026)\nAn executor-grounded training framework for reasoning planners that rewards trajectories using both rubric-based reasoning quality and measured uplift on a frozen executor.\n\n### Code Execution as Supervision (EMNLP 2025)\nLeverages code execution traces as verifiable, scalable supervision for enhancing step-by-step reasoning in LLMs by transforming execution traces into natural language chain-of-thought reasoning.\n\n---\n\n## 9. Qwen3-Coder Status and Availability\n\n### Qwen3-Coder-Next (February 2026)\n- Released **February 4, 2026**.\n- **3B activated parameters, 80B total parameters** (mixture-of-experts).\n- **256K context length**.\n- Achieves **70%+ on SWE-bench Verified** using SWE-Agent scaffold.\n- Pricing: $0.110/M input tokens, $0.800/M output tokens.\n- Excels at long-horizon reasoning, complex tool usage, and recovery from execution failures.\n\n### Qwen3-Coder 480B A35B Instruct\n- A larger variant released in mid-2025.\n- 480B total parameters with 35B activated.\n- Scores 25 on Artificial Analysis Intelligence Index (above median of 23 for similar open-weight models).\n- Performance comparable to Claude Sonnet on agentic coding and browser-use tasks.\n\n### Qwen3-Coder 30B A3B Instruct\n- A smaller variant also available, targeting local/edge deployment.\n\n### Broader Qwen Ecosystem\nThe Qwen team has continued development with **Qwen3.6** now on GitHub, and **Qwen3.6-Max-Preview** available as a preview model.\n\n---\n\nSources:\n- [Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)\n- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%](https://www.morphllm.com/swe-bench-pro)\n- [SWE-bench Leaderboard 2026: All Model Scores, Rankings & What They Actually Mean](https://www.codeant.ai/blogs/swe-bench-scores)\n- [OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)\n- [Is SWE-bench Verified Contaminated? OpenAI Shifts to SWE-bench Pro | CodeSOTA](https://www.codesota.com/news/swe-bench-contamination-debate)\n- [SWE-Bench Pro Leaderboard AI Coding Benchmark | Scale](https://labs.scale.com/leaderboard/swe_bench_pro_public)\n- [SWE-bench Pro Benchmark 2026: 30 LLM scores | BenchLM.ai](https://benchlm.ai/benchmarks/swePro)\n- [SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? | OpenReview](https://openreview.net/forum?id=9R2iUHhVfr)\n- [SWE-Bench Verified Benchmark Leaderboard](https://llm-stats.com/benchmarks/swe-bench-verified)\n- [EG-CFG GitHub Repository](https://github.com/boazlavon/eg_cfg)\n- [Execution Guided Line-by-Line Code Generation | arXiv](https://arxiv.org/abs/2506.10948)\n- [EG-CFG: Enhancing Code Generation with Real-Time Execution Feedback | MarkTechPost](https://www.marktechpost.com/2025/07/18/eg-cfg-enhancing-code-generation-with-real-time-execution-feedback/)\n- [DebugBench: Evaluating Debugging Capability of Large Language Models | arXiv](https://arxiv.org/abs/2401.04621)\n- [Code Generation Benchmarks 2026: SOTA LLMs | CodeSOTA](https://www.codesota.com/code-generation)\n- [HumanEval Pro and MBPP Pro | arXiv](https://arxiv.org/abs/2412.21199)\n- [EvalPlus Leaderboard](https://evalplus.github.io/leaderboard.html)\n- [Think Anywhere in Code Generation | arXiv](https://arxiv.org/abs/2603.29957)\n- [When to Ponder: Adaptive Compute Allocation for Code Generation via Test-Time Training | arXiv](https://arxiv.org/abs/2601.00894)\n- [Understanding Specification-Driven Code Generation with LLMs | arXiv](https://arxiv.org/abs/2601.03878)\n- [SpecOps 2026 Workshop](https://conf.researchr.org/home/splash-issta-2026/specops-2026)\n- [From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing | ACM](https://dl.acm.org/doi/10.1145/3696630.3728702)\n- [Use Property-Based Testing to Bridge LLM Code Generation and Validation | arXiv](https://arxiv.org/abs/2506.18315)\n- [Towards Structured, State-Aware, and Execution-Grounded Reasoning for SE Agents | arXiv](https://arxiv.org/html/2602.04640)\n- [Verify Before You Fix: Agentic Execution Grounding | arXiv](https://arxiv.org/abs/2604.10800v1)\n- [Correct Is Not Enough: Training Reasoning Planners with Executor-Grounded Rewards | arXiv](https://arxiv.org/abs/2605.03862)\n- [RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning | arXiv](https://arxiv.org/abs/2410.02089)\n- [Qwen3-Coder-Next | Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-Next)\n- [Qwen3-Coder-Next: Pushing Small Hybrid Models | Qwen Blog](https://qwen.ai/blog?id=qwen3-coder-next)\n- [Qwen3-Coder GitHub Repository](https://github.com/QwenLM/Qwen3-Coder)\n- [Qwen3 Coder 480B Analysis | Artificial Analysis](https://artificialanalysis.ai/models/qwen3-coder-480b-a35b-instruct)\n- [The End of SWE-Bench Verified | Latent Space](https://www.latent.space/p/swe-bench-dead)\n- [Best LLM for Coding in 2026 | WhatLLM.org](https://whatllm.org/best-llm-for-coding)"
      }
    ],
    "totalDurationMs": 150262,
    "totalTokens": 28676,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 982,
      "cache_creation_input_tokens": 6246,
      "cache_read_input_tokens": 17333,
      "output_tokens": 4115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6246
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 982,
          "output_tokens": 4115,
          "cache_read_input_tokens": 17333,
          "cache_creation_input_tokens": 6246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6246,
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
  "sourceToolAssistantUUID": "511b7672-7097-4db3-b827-5b9b5659c1cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "70de90c2-5540-437d-97de-1c29c82dcbf4",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Specification-Grounded Code Reasoning at Inference Time",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---

### Assistant

_source line 22 · 2026-05-12T01:59:16.361Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research results. Let me analyze the findings and form my review.

## Key Findings:

### 1. PGS (arXiv:2506.18315) - CONFIRMED EXISTS
- Title: "Use Property-Based Testing to Bridge LLM Code Generation and Validation" (v1) / "Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback" (v2)
- Published June 2025, revised May 2026
- Core method: Uses LLM-generated abstract properties instead of test cases for code refinement


- Shows 23.1-37.3% relative improvement in pass@1 over traditional test-driven approaches, though the evaluation is limited to HumanEval, MBPP, and LiveCodeBench without coverage on harder benchmarks like CodeContests or SWE-bench. Notably, this is the fifth consecutive instance where PGS was reported as missing from key references despite being confirmed to exist.

### 2. NL-Debugging (arXiv:2505.15356) - CONFIRMED EXISTS
- Accepted as an oral presentation at EMNLP 2025, which is the exact target venue
- Leverages natural language as an intermediate representation for the debugging process
- Demonstrates substantial improvements on APPS and Codeforces benchmarks

### 3. Cont

Now looking at ContractEval and the subsequent papers. ContractEval shows that standard prompting achieves 0% contract satisfaction, jumping to 23-41% when explicit contracts are provided, which validates ExeSpec's core motivation but highlights potential issues with specification quality. From Prompts to Properties, presented at FSE 2025 as part of LLanMER, reveals that property-based testing uncovers 30-32% partial failures in LLM-generated code. There's also work on preconditions and postconditions published in IEEE Access 2025. On the SWE-bench front, OpenAI stopped reporting scores in February 2026 due to contamination concerns, with the gap between Verified (93.9%) and Pro (~46%) being substantial—the paper acknowledges this by reporting held-out test pass rates alongside standard metrics, though this approach seems insufficient given the severity of the contamination issue.

Qwen released their next-generation coder model in February 2026 with impressive specs, but the idea relies on Qwen2.5-Coder without explaining why the newer version wasn't chosen. Meanwhile, EG-CFG has achieved state-of-the-art performance on CodeContests at 60.6%. Looking at the critical issues with this work, PGS remains unaddressed for the fifth consecutive round despite explicit warnings from reviewers—it's not mentioned in the key references or the landscape section, and this pattern has persisted from Round 3 through Round 7, with the previous reviewer marking Round 4 as the first instance, though the history suggests it goes back further.

The generator has been responsive to some earlier feedback by including papers like AlphaCodium, CodeT, and Self-Debugging variants, but PGS has been systematically overlooked. Beyond that, there are several other significant gaps: NL-Debugging from EMNLP 2025 (an oral presentation at the target venue) uses intermediate representations for debugging and would be directly relevant for DebugBench evaluation, ContractEval still isn't cited despite validating the core motivation while raising concerns about specification quality, and the SWE-bench Verified contamination issue has only been partially addressed with a mention of OpenAI's 2026 audit findings.

The real tension is whether this warrants failure or revision. The case for failure is compelling: PGS has been flagged for four consecutive rounds with an explicit warning in Round 6 that unaddressed issues would trigger failure, and it represents a core contribution overlap with ExeSpec around using properties rather than tests at inference time. But the case for revision acknowledges that the paper has genuinely improved across seven rounds, even if some critical feedback keeps getting sidestepped.

Looking at the actual execution, the controlled experimental design with honest ablations is exactly what was requested—comparing ExeSpec against AlphaCodium-style approaches, Self-Spec variants, and direct prompting. The scope differences are real too: PGS only covers HumanEval/MBPP/LiveCodeBench while ExeSpec's evaluation is broader. The differentiators around execution grounding, multi-task learning, and component-level ablation are substantive. With two rounds still remaining, there's room for one more revision to address the lingering concerns.

But I keep coming back to the same problem: PGS has been flagged four times now and remains unaddressed, and the Round 6 reviewer's "FINAL WARNING" was explicit. The idea's core is genuinely solid—the improvements across other dimensions are real, the citations have been substantially expanded, and the experimental rigor is there—but ignoring a critical competitor after a final warning is a serious issue that could tip this toward failure regardless of the other strengths.

Still, I think "revise" is the right call. The work shows consistent improvement, the contribution is genuinely differentiated from PGS in meaningful ways (execution grounding of specs themselves, multi-task scope, component ablation), and we're at Round 7 with three rounds remaining. But this has to come with unambiguous language that PGS is non-negotiable for Round 8.

Now I'm scoring the novelty: with PGS in the landscape, ExeSpec's novelty is reduced but not eliminated—it extends to four task types, grounds execution at the spec level rather than just code generation, and includes component ablation that PGS doesn't. It's incremental over PGS but still represents a meaningful advance.

For feasibility, the timeline is aggressive—14-18 days with 100-150 H100-hours is tight given the SWE-bench setup, reimplementing AlphaCodium, and running four conditions across two models on three primary benchmarks plus supplementary ones. There's also the lingering question of SWE-bench contamination. Clarity is strong with well-structured stages and honest ablation commitments. Impact is meaningful if the ablations show property-level specs help beyond I/O specs, though PGS has already demonstrated that properties outperform tests. Averaging these scores gives me around 3.25.

That's below the 4.0 threshold, so revision makes sense. But stepping back, the experimental design itself is genuinely rigorous—the ablation between I/O-only and full specs is necessary, the baseline choices are solid, and the three-stage approach is clear. The real issues are fixable: missing citations for PGS, NL-Debugging, and ContractEval, inadequate treatment of SWE-bench contamination, and model currency. None of these undermine the core idea.

Recalibrating my scores: novelty drops to 3/5 because PGS substantially overlaps this work, and without clear differentiation EMNLP reviewers will see it as a variant. Feasibility is also 3/5—the timeline is tight, especially with SWE-bench setup taking 2-3 days alone. Clarity stays at 4/5 since the proposal is well-structured. Impact is 3/5; the multi-task extension adds value, but PGS has already demonstrated part of the benefit. That averages to 3.25/5, so the verdict is revision.

The core idea is sound, but the competitive positioning against PGS is the critical gap that needs addressing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70de90c2-5540-437d-97de-1c29c82dcbf4",
  "isSidechain": false,
  "requestId": "req_011Cawr2qQHbZ56kBhCxN7XJ",
  "type": "assistant",
  "uuid": "8b6586a6-8644-4994-8416-158d93229a6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwzU6npnrbtsWKHr6j51kV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11093,
      "cache_read_input_tokens": 37431,
      "output_tokens": 3276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3276,
          "cache_read_input_tokens": 37431,
          "cache_creation_input_tokens": 11093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11093
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

_source line 23 · 2026-05-12T01:59:16.362Z_

Now let me do a few more targeted searches to verify specific claims in the idea.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b6586a6-8644-4994-8416-158d93229a6e",
  "isSidechain": false,
  "requestId": "req_011Cawr2qQHbZ56kBhCxN7XJ",
  "type": "assistant",
  "uuid": "0c9e9847-f884-4012-942e-e73b105b2d20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwzU6npnrbtsWKHr6j51kV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11093,
      "cache_read_input_tokens": 37431,
      "output_tokens": 3276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3276,
          "cache_read_input_tokens": 37431,
          "cache_creation_input_tokens": 11093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11093
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

_source line 24 · 2026-05-12T01:59:20.910Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01EJQGHDPMmTk86W1hcYtBpG`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for StoryCoder and SSDE papers",
  "prompt": "Search the web for these two papers:\n\n1. StoryCoder (arXiv:2604.14631) — reportedly a training-free structured intermediate reasoning method for code\n2. SSDE (arXiv:2605.02455) — \"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering\"\n\nFor each, verify:\n- Does the paper exist?\n- What is the core method?\n- When published?\n- What benchmarks/results?\n\nSearch queries:\n- \"arXiv 2604.14631 StoryCoder\"\n- \"arXiv 2605.02455 SSDE structured spec-driven engineering\"\n- \"StoryCoder code generation 2026\"\n\nUse WebSearch. Report findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c9e9847-f884-4012-942e-e73b105b2d20",
  "isSidechain": false,
  "requestId": "req_011Cawr2qQHbZ56kBhCxN7XJ",
  "type": "assistant",
  "uuid": "770c163f-6686-4965-a424-55e93d8ff0b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwzU6npnrbtsWKHr6j51kV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11093,
      "cache_read_input_tokens": 37431,
      "output_tokens": 3276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3276,
          "cache_read_input_tokens": 37431,
          "cache_creation_input_tokens": 11093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11093
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

_source line 25 · 2026-05-12T01:59:24.132Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014hweVoG4Z5EEVk1pspQLKk`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for AlphaCodium open-source implementation",
  "prompt": "Search for:\n1. AlphaCodium open-source implementation — does github.com/Codium-ai/AlphaCodium exist and is it usable?\n2. What is AlphaCodium's actual pass@5 on CodeContests? The idea claims 44%.\n3. Are there any recent (2025-2026) papers that build on or improve AlphaCodium?\n\nSearch queries:\n- \"site:github.com Codium-ai AlphaCodium\"\n- \"AlphaCodium CodeContests pass@5 44%\"\n- \"AlphaCodium 2025 2026 improvement\"\n\nUse WebSearch. Report findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "770c163f-6686-4965-a424-55e93d8ff0b4",
  "isSidechain": false,
  "requestId": "req_011Cawr2qQHbZ56kBhCxN7XJ",
  "type": "assistant",
  "uuid": "cab408cc-8d76-481e-a541-85bccbe21487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwzU6npnrbtsWKHr6j51kV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11093,
      "cache_read_input_tokens": 37431,
      "output_tokens": 3276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3276,
          "cache_read_input_tokens": 37431,
          "cache_creation_input_tokens": 11093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11093
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

_source line 26 · 2026-05-12T01:59:28.777Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TEY1mSrHy4vymHWWBYtzkh`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Self-Spec paper claims",
  "prompt": "Search for \"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation\" at Agents4Science 2025.\n\nI need to verify:\n1. Does this paper exist?\n2. What venue — \"Agents4Science 2025\"?\n3. Claims: GPT-4o HumanEval pass@1 from 87% to 92% (+5pp), Claude 3.7 from 92% to 94% (+2pp)\n4. Does it really ONLY generate specs without execution verification?\n\nSearch queries:\n- \"Self-Spec Model-Authored Specifications LLM Code Generation\"\n- \"Self-Spec Agents4Science 2025\"\n- \"model authored specification code generation\"\n\nUse WebSearch. Report findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cab408cc-8d76-481e-a541-85bccbe21487",
  "isSidechain": false,
  "requestId": "req_011Cawr2qQHbZ56kBhCxN7XJ",
  "type": "assistant",
  "uuid": "038a02c0-4485-41b7-aa75-26e8090947df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CwzU6npnrbtsWKHr6j51kV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11093,
      "cache_read_input_tokens": 37431,
      "output_tokens": 3276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11093,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3276,
          "cache_read_input_tokens": 37431,
          "cache_creation_input_tokens": 11093,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11093
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

_source line 27 · 2026-05-12T02:00:19.973Z_

<details><summary>↩ Tool result · `toolu_01EJQGHDPMmTk86W1hcYtBpG`</summary>

```text
Here are the findings for both papers.

---

## Paper 1: StoryCoder (arXiv:2604.14631)

**Exists:** Yes, confirmed on arXiv.

**Full title:** "StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation"

**Authors:** Geonhui Jang, Dongyoon Han, YoungJoon Yoo

**Published:** April 16, 2026 (accepted to ACL 2026 Main Conference; 21 pages, 12 figures)

**Core method:** StoryCoder is a training-free framework that reformulates code generation problems into coherent natural language narratives. Each narrative has three components: (1) a task overview, (2) constraints, and (3) example test cases, guided by a selected algorithm and genre. The design draws on cognitive science findings that humans reason more effectively when organizing fragmented conditions into coherent mental models via analogical structures. Notably, it requires no model fine-tuning -- it operates purely at the prompt/input level.

**Benchmarks and results:**
- Evaluated across **11 models** on **HumanEval**, **LiveCodeBench**, and **CodeForces**
- Achieved an **average gain of 18.7% in zero-shot pass@10**
- Consistent improvements across different model scales and architectures
- Analysis showed narrative reformulation guides models toward correct algorithmic strategies, reduces implementation errors, and induces more modular code structure

---

## Paper 2: SSDE (arXiv:2605.02455)

**Exists:** Yes, confirmed on arXiv.

**Full title:** "LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering"

**Authors:** Shuzhao Feng, Boqi Chen, Brett H Meyer, Gunter Mussbacher

**Published:** May 4, 2026 (accepted to the 34th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering -- FSE Companion '26)

**Core method:** SSDE (Structured Spec-Driven Engineering) is a paradigm that uses structured artifacts (specifically Gherkin specifications and domain models) as inputs to guide LLM code generation at the repository level. The key insight is that natural language prompts alone are inherently ambiguous and lack verifiability, whereas structured specifications provide both higher quality generation and superior verifiability. The approach targets Model-View-Controller (MVC) business logic generation.

**Benchmarks and results:**
- Pilot study generating MVC business logic for **3 software systems** using **5 LLMs**
- The study is more qualitative/feasibility-oriented than benchmark-driven
- Demonstrates that high-quality automated repository-level generation is a "tangible goal" with SSDE
- No specific quantitative benchmark numbers (e.g., pass@k) are reported in the abstract; the contribution is more about establishing the SSDE paradigm and demonstrating its feasibility

---

## Summary comparison

| Aspect | StoryCoder | SSDE |
|---|---|---|
| Scope | Function-level code generation | Repository-level code generation |
| Approach | Narrative reformulation of prompts (training-free) | Structured specifications (Gherkin + domain models) |
| Venue | ACL 2026 | FSE Companion '26 |
| Quantitative results | 18.7% avg. gain on pass@10 across 11 models | Feasibility study across 3 systems, 5 LLMs |
| Key novelty | Cognitive-science-inspired narrative structure | Spec-driven engineering for repo-level generation |

Both papers are real, published in 2026, and address structured intermediate representations for LLM code generation -- but at very different scales (function-level vs. repository-level).

Sources:
- [StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation](https://arxiv.org/abs/2604.14631)
- [StoryCoder (HTML version)](https://arxiv.org/html/2604.14631)
- [LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering](https://arxiv.org/abs/2605.02455)
- [SSDE (HTML version)](https://arxiv.org/html/2605.02455)

agentId: a8782099bb64677a1 (use SendMessage with to: 'a8782099bb64677a1' to continue this agent)
&lt;usage>total_tokens: 15111
tool_uses: 6
duration_ms: 59059&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "770c163f-6686-4965-a424-55e93d8ff0b4",
  "isSidechain": false,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "type": "user",
  "uuid": "f06f0289-8a75-40e1-9721-89fd817f6444",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for these two papers:\n\n1. StoryCoder (arXiv:2604.14631) — reportedly a training-free structured intermediate reasoning method for code\n2. SSDE (arXiv:2605.02455) — \"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering\"\n\nFor each, verify:\n- Does the paper exist?\n- What is the core method?\n- When published?\n- What benchmarks/results?\n\nSearch queries:\n- \"arXiv 2604.14631 StoryCoder\"\n- \"arXiv 2605.02455 SSDE structured spec-driven engineering\"\n- \"StoryCoder code generation 2026\"\n\nUse WebSearch. Report findings.",
    "agentId": "a8782099bb64677a1",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings for both papers.\n\n---\n\n## Paper 1: StoryCoder (arXiv:2604.14631)\n\n**Exists:** Yes, confirmed on arXiv.\n\n**Full title:** \"StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation\"\n\n**Authors:** Geonhui Jang, Dongyoon Han, YoungJoon Yoo\n\n**Published:** April 16, 2026 (accepted to ACL 2026 Main Conference; 21 pages, 12 figures)\n\n**Core method:** StoryCoder is a training-free framework that reformulates code generation problems into coherent natural language narratives. Each narrative has three components: (1) a task overview, (2) constraints, and (3) example test cases, guided by a selected algorithm and genre. The design draws on cognitive science findings that humans reason more effectively when organizing fragmented conditions into coherent mental models via analogical structures. Notably, it requires no model fine-tuning -- it operates purely at the prompt/input level.\n\n**Benchmarks and results:**\n- Evaluated across **11 models** on **HumanEval**, **LiveCodeBench**, and **CodeForces**\n- Achieved an **average gain of 18.7% in zero-shot pass@10**\n- Consistent improvements across different model scales and architectures\n- Analysis showed narrative reformulation guides models toward correct algorithmic strategies, reduces implementation errors, and induces more modular code structure\n\n---\n\n## Paper 2: SSDE (arXiv:2605.02455)\n\n**Exists:** Yes, confirmed on arXiv.\n\n**Full title:** \"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering\"\n\n**Authors:** Shuzhao Feng, Boqi Chen, Brett H Meyer, Gunter Mussbacher\n\n**Published:** May 4, 2026 (accepted to the 34th ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering -- FSE Companion '26)\n\n**Core method:** SSDE (Structured Spec-Driven Engineering) is a paradigm that uses structured artifacts (specifically Gherkin specifications and domain models) as inputs to guide LLM code generation at the repository level. The key insight is that natural language prompts alone are inherently ambiguous and lack verifiability, whereas structured specifications provide both higher quality generation and superior verifiability. The approach targets Model-View-Controller (MVC) business logic generation.\n\n**Benchmarks and results:**\n- Pilot study generating MVC business logic for **3 software systems** using **5 LLMs**\n- The study is more qualitative/feasibility-oriented than benchmark-driven\n- Demonstrates that high-quality automated repository-level generation is a \"tangible goal\" with SSDE\n- No specific quantitative benchmark numbers (e.g., pass@k) are reported in the abstract; the contribution is more about establishing the SSDE paradigm and demonstrating its feasibility\n\n---\n\n## Summary comparison\n\n| Aspect | StoryCoder | SSDE |\n|---|---|---|\n| Scope | Function-level code generation | Repository-level code generation |\n| Approach | Narrative reformulation of prompts (training-free) | Structured specifications (Gherkin + domain models) |\n| Venue | ACL 2026 | FSE Companion '26 |\n| Quantitative results | 18.7% avg. gain on pass@10 across 11 models | Feasibility study across 3 systems, 5 LLMs |\n| Key novelty | Cognitive-science-inspired narrative structure | Spec-driven engineering for repo-level generation |\n\nBoth papers are real, published in 2026, and address structured intermediate representations for LLM code generation -- but at very different scales (function-level vs. repository-level).\n\nSources:\n- [StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation](https://arxiv.org/abs/2604.14631)\n- [StoryCoder (HTML version)](https://arxiv.org/html/2604.14631)\n- [LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering](https://arxiv.org/abs/2605.02455)\n- [SSDE (HTML version)](https://arxiv.org/html/2605.02455)"
      }
    ],
    "totalDurationMs": 59059,
    "totalTokens": 15111,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1483,
      "cache_read_input_tokens": 12603,
      "output_tokens": 1024,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1483
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1024,
          "cache_read_input_tokens": 12603,
          "cache_creation_input_tokens": 1483,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1483,
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
  "sourceToolAssistantUUID": "770c163f-6686-4965-a424-55e93d8ff0b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "f06f0289-8a75-40e1-9721-89fd817f6444",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Specification-Grounded Code Reasoning at Inference Time",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---

### Tool result

_source line 30 · 2026-05-12T02:01:18.432Z_

<details><summary>↩ Tool result · `toolu_01TEY1mSrHy4vymHWWBYtzkh`</summary>

```text
Here are my findings across all four questions:

---

**1. Does the paper exist?**

Yes. "Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation" is a real paper. It is hosted on OpenReview at submission ID `6pr7BUGkLp`. Authors are **Zihao Xu, Xiao Cheng, Jingling Xue, and Yuekang Li**. It was published on October 8, 2025, and last modified October 18, 2025.

**2. What venue -- "Agents4Science 2025"?**

Confirmed. The paper's OpenReview page lists the venue as **Agents4Science 2025 Conference** (the 1st Open Conference of AI Agents for Science, affiliated with Stanford). It also appears on the conference's official accepted papers page at `agents4science.stanford.edu/accepted-papers.html`. The conference took place on October 22, 2025, with an acceptance rate of approximately 16% (24 out of 300+ submissions).

**3. Claims: GPT-4o HumanEval pass@1 from 87% to 92% (+5pp), Claude 3.7 from 92% to 94% (+2pp)?**

Confirmed. Multiple search results corroborate the exact figures:
- **GPT-4o**: 87% -> 92% (+5 percentage points)
- **Claude 3.7**: 92% -> 94% (+2 percentage points)
- **Claude 3.5**: 90% -> 89% (-1 percentage point, a slight regression)

All measured on HumanEval pass@1 with a single sample under deterministic decoding (temperature = 0).

**4. Does it really ONLY generate specs without execution verification?**

Yes, confirmed. Self-Spec is a **pure generation pipeline** with no execution-based verification or runtime feedback. The four-step pipeline is:
1. The model designs a compact spec schema it prefers
2. It instantiates that schema from the problem's docstring and signature
3. It resolves ambiguities via a minimal Q&A loop (still purely generative, no code execution)
4. It generates code solely from the confirmed spec

There is no intermediate test execution, no code running, and no runtime verification loop within the method. The pass@1 evaluation uses the standard HumanEval test suite *after* generation, but that is the benchmark's evaluation protocol, not part of the Self-Spec method itself. The paper explicitly describes the approach as "lightweight" and requiring "no finetuning."

---

Sources:
- [Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation (OpenReview forum)](https://openreview.net/forum?id=6pr7BUGkLp)
- [Self-Spec PDF](https://openreview.net/pdf?id=6pr7BUGkLp)
- [Agents4Science 2025 Conference (OpenReview)](https://openreview.net/group?id=Agents4Science%2F2025%2FConference)
- [Agents4Science 2025 Accepted Papers](https://agents4science.stanford.edu/accepted-papers.html)
- [Agents4Science 2025 Main Site](https://agents4science.stanford.edu/)

agentId: a0cddc46ccf143ae0 (use SendMessage with to: 'a0cddc46ccf143ae0' to continue this agent)
&lt;usage>total_tokens: 20040
tool_uses: 13
duration_ms: 109652&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "038a02c0-4485-41b7-aa75-26e8090947df",
  "isSidechain": false,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "type": "user",
  "uuid": "9dd74b53-7317-4f2c-b1a8-a851f6e44952",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for \"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation\" at Agents4Science 2025.\n\nI need to verify:\n1. Does this paper exist?\n2. What venue — \"Agents4Science 2025\"?\n3. Claims: GPT-4o HumanEval pass@1 from 87% to 92% (+5pp), Claude 3.7 from 92% to 94% (+2pp)\n4. Does it really ONLY generate specs without execution verification?\n\nSearch queries:\n- \"Self-Spec Model-Authored Specifications LLM Code Generation\"\n- \"Self-Spec Agents4Science 2025\"\n- \"model authored specification code generation\"\n\nUse WebSearch. Report findings.",
    "agentId": "a0cddc46ccf143ae0",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings across all four questions:\n\n---\n\n**1. Does the paper exist?**\n\nYes. \"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation\" is a real paper. It is hosted on OpenReview at submission ID `6pr7BUGkLp`. Authors are **Zihao Xu, Xiao Cheng, Jingling Xue, and Yuekang Li**. It was published on October 8, 2025, and last modified October 18, 2025.\n\n**2. What venue -- \"Agents4Science 2025\"?**\n\nConfirmed. The paper's OpenReview page lists the venue as **Agents4Science 2025 Conference** (the 1st Open Conference of AI Agents for Science, affiliated with Stanford). It also appears on the conference's official accepted papers page at `agents4science.stanford.edu/accepted-papers.html`. The conference took place on October 22, 2025, with an acceptance rate of approximately 16% (24 out of 300+ submissions).\n\n**3. Claims: GPT-4o HumanEval pass@1 from 87% to 92% (+5pp), Claude 3.7 from 92% to 94% (+2pp)?**\n\nConfirmed. Multiple search results corroborate the exact figures:\n- **GPT-4o**: 87% -> 92% (+5 percentage points)\n- **Claude 3.7**: 92% -> 94% (+2 percentage points)\n- **Claude 3.5**: 90% -> 89% (-1 percentage point, a slight regression)\n\nAll measured on HumanEval pass@1 with a single sample under deterministic decoding (temperature = 0).\n\n**4. Does it really ONLY generate specs without execution verification?**\n\nYes, confirmed. Self-Spec is a **pure generation pipeline** with no execution-based verification or runtime feedback. The four-step pipeline is:\n1. The model designs a compact spec schema it prefers\n2. It instantiates that schema from the problem's docstring and signature\n3. It resolves ambiguities via a minimal Q&A loop (still purely generative, no code execution)\n4. It generates code solely from the confirmed spec\n\nThere is no intermediate test execution, no code running, and no runtime verification loop within the method. The pass@1 evaluation uses the standard HumanEval test suite *after* generation, but that is the benchmark's evaluation protocol, not part of the Self-Spec method itself. The paper explicitly describes the approach as \"lightweight\" and requiring \"no finetuning.\"\n\n---\n\nSources:\n- [Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation (OpenReview forum)](https://openreview.net/forum?id=6pr7BUGkLp)\n- [Self-Spec PDF](https://openreview.net/pdf?id=6pr7BUGkLp)\n- [Agents4Science 2025 Conference (OpenReview)](https://openreview.net/group?id=Agents4Science%2F2025%2FConference)\n- [Agents4Science 2025 Accepted Papers](https://agents4science.stanford.edu/accepted-papers.html)\n- [Agents4Science 2025 Main Site](https://agents4science.stanford.edu/)"
      }
    ],
    "totalDurationMs": 109652,
    "totalTokens": 20040,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 18540,
      "output_tokens": 795,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 704
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 795,
          "cache_read_input_tokens": 18540,
          "cache_creation_input_tokens": 704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 704,
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
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "038a02c0-4485-41b7-aa75-26e8090947df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-12T02:02:02.064Z_

<details><summary>↩ Tool result · `toolu_014hweVoG4Z5EEVk1pspQLKk`</summary>

```text
Now I have all the information needed. Here is the full report:

---

## Findings

### 1. GitHub Repository: Does github.com/Codium-ai/AlphaCodium Exist and Is It Usable?

**Yes, the repository exists and is usable**, though with caveats.

- **URL:** [github.com/Codium-ai/AlphaCodium](https://github.com/Codium-ai/AlphaCodium)
- **Stars:** ~3.9k
- **License:** AGPL-3.0
- **Last meaningful update:** Around May 2024 (leaderboard updated with new GPT model scores); the last commit activity visible is from November 2024. The repo is **not archived** but development appears to have slowed/stopped.
- **Dependencies:** Requires an OpenAI API key (GPT-4 or GPT-3.5), Python 3, and the CodeContests dataset downloaded separately from Hugging Face.
- **Usability notes:**
  - The code is runnable, with a Dockerfile provided.
  - There is a community fork ([AlphaCodium-Ollama](https://github.com/10Nates/AlphaCodium-Ollama)) that removes the OpenAI dependency for local model use.
  - Known limitation: context window constraints (works within 8192 tokens but performance degrades above ~4000 tokens).
  - Each solution requires 15-20 LLM calls.
  - The company behind it (CodiumAI) has rebranded to **Qodo**, and the methodology has been folded into their commercial "QodoFlow" product.

### 2. AlphaCodium's Actual pass@5 on CodeContests -- Is the 44% Claim Accurate?

**The 44% figure is real but it applies only to the validation set, not the test set.** This is a critical distinction:

| Model | Split | Direct Prompt (pass@5) | AlphaCodium (pass@5) |
|-------|-------|----------------------|---------------------|
| GPT-4 | **Validation** (117 problems) | 19% | **44%** |
| GPT-4 | **Test** (165 problems) | 12% | **29%** |
| GPT-3.5 | Validation | 17% | 25% |
| GPT-3.5 | Test | 8% | 17% |
| DeepSeek-33B | Validation | 5% | 20% |
| DeepSeek-33B | Test | 12% | 24% |

**Key takeaways on the numbers:**
- The headline "44%" is the **validation set** result for GPT-4. On the harder, unseen **test set**, GPT-4 + AlphaCodium achieves **29%** (pass@5).
- The improvement is still substantial (12% to 29% on test, a 2.4x uplift).
- The paper argues no data leakage on the test set since it comprises problems published after GPT-4's September 2021 training cutoff.
- Compared to AlphaCode: AlphaCodium's 29% (pass@5, ~15-20 LLM calls) versus AlphaCode's 28% (pass@10@100K, millions of generated solutions) -- comparable accuracy with **four orders of magnitude fewer calls**.

### 3. Recent (2025-2026) Papers Building on or Improving AlphaCodium

The AlphaCodium paper (arXiv:2401.08500) has accumulated ~81 citations on Semantic Scholar. Several recent papers directly build on or extend its core ideas of iterative, test-driven code generation:

**a) CodeContests-O (January 2026)** -- [arXiv:2601.13682](https://arxiv.org/abs/2601.13682)
- Proposes a feedback-driven iterative framework for test case construction -- generating tests, executing them against correct/incorrect solutions, and using failures as feedback to refine tests. Directly extends AlphaCodium's insight that "generating useful tests is easier than generating correct code."
- Released an improved dataset on [Hugging Face](https://huggingface.co/datasets/caijanfeng/CodeContests-O).

**b) FixAudit: An Iterative Test-and-Repair Framework (April 2026)** -- [arXiv:2604.05560](https://arxiv.org/html/2604.05560)
- Jointly trains a "Fixer" (repairs code) and "Auditor" (generates tests to expose bugs) in an iterative loop. Addresses a limitation of earlier approaches where the tester never reads candidate code.
- On a 7B model, surpasses the average performance of a 32B baseline. Improves average Pass@1 by 35-37% over baselines on APPS, CodeContests, and xCodeEval.

**c) CodeContests+ (June 2025)** -- [arXiv:2506.05817](https://arxiv.org/abs/2506.05817)
- An LLM-based agent system for creating high-quality test cases for competitive programming, proposing an enhanced version of the CodeContests dataset with significantly higher True Positive Rate.

**d) Qodo's own follow-up work (2024-2025)**
- Qodo (formerly CodiumAI) published results showing [AlphaCodium outperforms direct prompting of OpenAI o1](https://www.qodo.ai/blog/system-2-thinking-alphacodium-outperforms-direct-prompting-of-openai-o1/) on Codeforces problems, demonstrating that the flow engineering approach provides additive value even on top of reasoning models. A Hacker News thread noted GPT-4o reached 54% validation accuracy with AlphaCodium.

---

**Bottom line:** The repo is real, open-source (AGPL-3.0), and runnable. The 44% number is technically accurate but misleading if presented without context -- it is the validation-set result; the test-set pass@5 is 29%. The approach has been influential, with multiple 2025-2026 papers extending its iterative test-driven paradigm.

Sources:
- [AlphaCodium GitHub Repository](https://github.com/Codium-ai/AlphaCodium)
- [AlphaCodium Paper (arXiv:2401.08500)](https://arxiv.org/abs/2401.08500)
- [AlphaCodium Paper Full HTML (ar5iv)](https://ar5iv.labs.arxiv.org/html/2401.08500)
- [Qodo Blog: AlphaCodium State-of-the-Art Code Generation](https://www.qodo.ai/blog/qodoflow-state-of-the-art-code-generation-for-code-contests/)
- [Qodo Blog: AlphaCodium Outperforms o1](https://www.qodo.ai/blog/system-2-thinking-alphacodium-outperforms-direct-prompting-of-openai-o1/)
- [CodeContests-O (arXiv:2601.13682)](https://arxiv.org/abs/2601.13682)
- [FixAudit (arXiv:2604.05560)](https://arxiv.org/html/2604.05560)
- [CodeContests+ (arXiv:2506.05817)](https://arxiv.org/abs/2506.05817)
- [AlphaCodium-Ollama Fork](https://github.com/10Nates/AlphaCodium-Ollama)
- [Semantic Scholar Entry](https://www.semanticscholar.org/paper/Code-Generation-with-AlphaCodium:-From-Prompt-to-Ridnik-Kredo/1566d96346927ad4dced85de4d55356f6aee6fb6)
- [Hacker News: GPT-4o + AlphaCodium 54%](https://news.ycombinator.com/item?id=40396818)

agentId: abefab949d06c096e (use SendMessage with to: 'abefab949d06c096e' to continue this agent)
&lt;usage>total_tokens: 28790
tool_uses: 20
duration_ms: 157928&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cab408cc-8d76-481e-a541-85bccbe21487",
  "isSidechain": false,
  "promptId": "2b18e4d3-7fa5-48b0-b481-c2f75e49b2be",
  "type": "user",
  "uuid": "2268578d-c9c3-49bb-8d87-e53b695b4e06",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for:\n1. AlphaCodium open-source implementation — does github.com/Codium-ai/AlphaCodium exist and is it usable?\n2. What is AlphaCodium's actual pass@5 on CodeContests? The idea claims 44%.\n3. Are there any recent (2025-2026) papers that build on or improve AlphaCodium?\n\nSearch queries:\n- \"site:github.com Codium-ai AlphaCodium\"\n- \"AlphaCodium CodeContests pass@5 44%\"\n- \"AlphaCodium 2025 2026 improvement\"\n\nUse WebSearch. Report findings.",
    "agentId": "abefab949d06c096e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Here is the full report:\n\n---\n\n## Findings\n\n### 1. GitHub Repository: Does github.com/Codium-ai/AlphaCodium Exist and Is It Usable?\n\n**Yes, the repository exists and is usable**, though with caveats.\n\n- **URL:** [github.com/Codium-ai/AlphaCodium](https://github.com/Codium-ai/AlphaCodium)\n- **Stars:** ~3.9k\n- **License:** AGPL-3.0\n- **Last meaningful update:** Around May 2024 (leaderboard updated with new GPT model scores); the last commit activity visible is from November 2024. The repo is **not archived** but development appears to have slowed/stopped.\n- **Dependencies:** Requires an OpenAI API key (GPT-4 or GPT-3.5), Python 3, and the CodeContests dataset downloaded separately from Hugging Face.\n- **Usability notes:**\n  - The code is runnable, with a Dockerfile provided.\n  - There is a community fork ([AlphaCodium-Ollama](https://github.com/10Nates/AlphaCodium-Ollama)) that removes the OpenAI dependency for local model use.\n  - Known limitation: context window constraints (works within 8192 tokens but performance degrades above ~4000 tokens).\n  - Each solution requires 15-20 LLM calls.\n  - The company behind it (CodiumAI) has rebranded to **Qodo**, and the methodology has been folded into their commercial \"QodoFlow\" product.\n\n### 2. AlphaCodium's Actual pass@5 on CodeContests -- Is the 44% Claim Accurate?\n\n**The 44% figure is real but it applies only to the validation set, not the test set.** This is a critical distinction:\n\n| Model | Split | Direct Prompt (pass@5) | AlphaCodium (pass@5) |\n|-------|-------|----------------------|---------------------|\n| GPT-4 | **Validation** (117 problems) | 19% | **44%** |\n| GPT-4 | **Test** (165 problems) | 12% | **29%** |\n| GPT-3.5 | Validation | 17% | 25% |\n| GPT-3.5 | Test | 8% | 17% |\n| DeepSeek-33B | Validation | 5% | 20% |\n| DeepSeek-33B | Test | 12% | 24% |\n\n**Key takeaways on the numbers:**\n- The headline \"44%\" is the **validation set** result for GPT-4. On the harder, unseen **test set**, GPT-4 + AlphaCodium achieves **29%** (pass@5).\n- The improvement is still substantial (12% to 29% on test, a 2.4x uplift).\n- The paper argues no data leakage on the test set since it comprises problems published after GPT-4's September 2021 training cutoff.\n- Compared to AlphaCode: AlphaCodium's 29% (pass@5, ~15-20 LLM calls) versus AlphaCode's 28% (pass@10@100K, millions of generated solutions) -- comparable accuracy with **four orders of magnitude fewer calls**.\n\n### 3. Recent (2025-2026) Papers Building on or Improving AlphaCodium\n\nThe AlphaCodium paper (arXiv:2401.08500) has accumulated ~81 citations on Semantic Scholar. Several recent papers directly build on or extend its core ideas of iterative, test-driven code generation:\n\n**a) CodeContests-O (January 2026)** -- [arXiv:2601.13682](https://arxiv.org/abs/2601.13682)\n- Proposes a feedback-driven iterative framework for test case construction -- generating tests, executing them against correct/incorrect solutions, and using failures as feedback to refine tests. Directly extends AlphaCodium's insight that \"generating useful tests is easier than generating correct code.\"\n- Released an improved dataset on [Hugging Face](https://huggingface.co/datasets/caijanfeng/CodeContests-O).\n\n**b) FixAudit: An Iterative Test-and-Repair Framework (April 2026)** -- [arXiv:2604.05560](https://arxiv.org/html/2604.05560)\n- Jointly trains a \"Fixer\" (repairs code) and \"Auditor\" (generates tests to expose bugs) in an iterative loop. Addresses a limitation of earlier approaches where the tester never reads candidate code.\n- On a 7B model, surpasses the average performance of a 32B baseline. Improves average Pass@1 by 35-37% over baselines on APPS, CodeContests, and xCodeEval.\n\n**c) CodeContests+ (June 2025)** -- [arXiv:2506.05817](https://arxiv.org/abs/2506.05817)\n- An LLM-based agent system for creating high-quality test cases for competitive programming, proposing an enhanced version of the CodeContests dataset with significantly higher True Positive Rate.\n\n**d) Qodo's own follow-up work (2024-2025)**\n- Qodo (formerly CodiumAI) published results showing [AlphaCodium outperforms direct prompting of OpenAI o1](https://www.qodo.ai/blog/system-2-thinking-alphacodium-outperforms-direct-prompting-of-openai-o1/) on Codeforces problems, demonstrating that the flow engineering approach provides additive value even on top of reasoning models. A Hacker News thread noted GPT-4o reached 54% validation accuracy with AlphaCodium.\n\n---\n\n**Bottom line:** The repo is real, open-source (AGPL-3.0), and runnable. The 44% number is technically accurate but misleading if presented without context -- it is the validation-set result; the test-set pass@5 is 29%. The approach has been influential, with multiple 2025-2026 papers extending its iterative test-driven paradigm.\n\nSources:\n- [AlphaCodium GitHub Repository](https://github.com/Codium-ai/AlphaCodium)\n- [AlphaCodium Paper (arXiv:2401.08500)](https://arxiv.org/abs/2401.08500)\n- [AlphaCodium Paper Full HTML (ar5iv)](https://ar5iv.labs.arxiv.org/html/2401.08500)\n- [Qodo Blog: AlphaCodium State-of-the-Art Code Generation](https://www.qodo.ai/blog/qodoflow-state-of-the-art-code-generation-for-code-contests/)\n- [Qodo Blog: AlphaCodium Outperforms o1](https://www.qodo.ai/blog/system-2-thinking-alphacodium-outperforms-direct-prompting-of-openai-o1/)\n- [CodeContests-O (arXiv:2601.13682)](https://arxiv.org/abs/2601.13682)\n- [FixAudit (arXiv:2604.05560)](https://arxiv.org/html/2604.05560)\n- [CodeContests+ (arXiv:2506.05817)](https://arxiv.org/abs/2506.05817)\n- [AlphaCodium-Ollama Fork](https://github.com/10Nates/AlphaCodium-Ollama)\n- [Semantic Scholar Entry](https://www.semanticscholar.org/paper/Code-Generation-with-AlphaCodium:-From-Prompt-to-Ridnik-Kredo/1566d96346927ad4dced85de4d55356f6aee6fb6)\n- [Hacker News: GPT-4o + AlphaCodium 54%](https://news.ycombinator.com/item?id=40396818)"
      }
    ],
    "totalDurationMs": 157928,
    "totalTokens": 28790,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 25906,
      "output_tokens": 1976,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 907
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1976,
          "cache_read_input_tokens": 25906,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 907,
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
  "sourceToolAssistantUUID": "cab408cc-8d76-481e-a541-85bccbe21487",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-12T02:03:06.830Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive findings. Let me also check the idea for a few more things:

1. The AlphaCodium 44% claim: The idea says "AlphaCodium's flow engineering raises CodeContests pass@5 from 19% to 44%." My research confirms this is the validation set number, not the test set. On the test set, it's 12% → 29%. This is potentially misleading in the idea's landscape section.

2. Additional missing work I discovered:
   - FixAudit (arXiv:2604.05560, April 2026): Jointly trains fixer and auditor, achieves 35-37% improvement on CodeContests. This is another important competitor.
   - StoryCoder (arXiv:2604.14631, ACL 2026): Uses narrative reformulation as structured intermediate reasoning — conceptually similar to ExeSpec's approach.

Now I'm moving into the critical assessment. The PGS issue has been flagged repeatedly across five consecutive review rounds, with Round 6 issuing a final warning. Looking at the current idea, PGS isn't listed in key_references or mentioned in the landscape section, which is a serious oversight that needs to be addressed immediately.

PGS and ExeSpec share the same fundamental insight about property-level feedback outperforming test-based feedback at inference time, and both are training-free with execution-based property validation. But there are meaningful differences: PGS only evaluates on HumanEval, MBPP, and LiveCodeBench while ExeSpec covers DebugBench, CodeContests, and SWE-bench Verified; PGS is limited to code generation whereas ExeSpec extends to debugging, completion, and issue resolution; ExeSpec validates specs before use while PGS doesn't execution-ground its properties; and ExeSpec's five-component schema with ablation studies contrasts with PGS treating properties as monolithic. These distinctions are genuine but they need to be explicitly argued in the paper rather than left implicit.

I'm also noticing several critical gaps. NL-Debugging is being flagged for the third time—this is an oral at EMNLP 2025, the exact target venue, so EMNLP 2026 reviewers will almost certainly know this work. ContractEval is missing too, which validates the core motivation that LLMs fail at contracts without grounding, though it also raises questions about spec quality. On SWE-bench Verified, the contamination issue is more severe than the current framing suggests: OpenAI officially stopped reporting Verified scores, the gap between top scores on Verified versus Pro is massive, and while using sub-frontier models like Qwen2.5-Coder helps mitigate some concerns, the benchmark's credibility in the community is fundamentally damaged. And the AlphaCodium claim about raising CodeContests pass@5 from 19% to 44% needs verification against my research findings.

The AlphaCodium numbers are actually from the validation set—on the test set it's 12% to 29%, which should be clarified. There's also a model currency issue: Qwen3-Coder-Next just released in February 2026 with significantly better specs, but the idea uses Qwen2.5-Coder without justification. I should also note FixAudit and StoryCoder from April and ACL 2026 respectively, though they're less critical than the PGS and NL-Debugging gaps. On the positive side, the idea is now targeting the correct venue and using the right benchmarks, which is progress.

Now I'm looking at the novelty score—PGS shares the same core insight about properties being better than tests for LLM code refinement, so ExeSpec's differentiators need to be clearly articulated.

The feasibility concerns are significant: the 14-18 day timeline is pushing against the 16-day constraint, especially with SWE-bench Docker setup taking 2-3 days alone, and the Verified contamination issue undermines one of the three primary benchmarks.

The proposal is well-structured with clear stages and honest ablations, though the core contribution—showing specs help beyond tests—has been partially established by PGS for generation tasks. The real impact would come from extending this to debugging and completion, particularly if DebugBench results show meaningful gains for ExeSpec over NL-Debugging approaches.

Averaging the scores puts this at 3.25, below the 4.0 threshold, so the verdict is to revise. Given the previous "FINAL WARNING" about PGS, I'm concerned whether this addresses those concerns sufficiently.

Weighing the options: PGS has been flagged for four consecutive rounds without substantive response, and R6 explicitly warned that ignoring it in R7 would warrant failure. But the idea itself has genuinely improved from earlier rounds, the experimental design is solid, and the core contribution—extending specs beyond generation to multiple code tasks—is still meaningful. The PGS gap is more about positioning and citation than a fundamental flaw. Since we're at R7 of 10 with three rounds remaining, I think one more revision is justified, but I need to be explicit that PGS differentiation must be addressed next round or this fails. The idea's core is strong enough to warrant one more chance at fixing the competitive landscape.

Actually, wait. The previous reviewer already said "FINAL WARNING — if unaddressed in Round 7, this warrants failure." I am the Round 7 reviewer. So the question is: should I honor the R6 reviewer's warning?

The issue is that PGS is genuinely a critical competitor that cannot be ignored. However, failing the idea ONLY because of a missing citation when the idea itself is sound seems harsh. The idea is genuinely differentiated from PGS in meaningful ways. The problem is that without citing PGS, reviewers won't see the differentiation.

I'll go with "revise" but with the strongest possible language. This is the last chance. Round 8 must address PGS, NL-Debugging, ContractEval, and SWE-bench contamination, or the idea should fail.

We're at Round 7 of 10, which means saying "revise" gives only two more realistic opportunities before the final pass/fail decision at Round 10. The generator's pattern of ignoring PGS across four rounds is troubling, but the core idea has genuine merit and the fix is specific and actionable—the generator has proven it can respond to other feedback like AlphaCodium and CodeT citations. I'm betting on "revise" because the differentiation from PGS is real, it just needs to be articulated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2268578d-c9c3-49bb-8d87-e53b695b4e06",
  "isSidechain": false,
  "requestId": "req_011CawrKrE7XMYCwurxsxp6C",
  "type": "assistant",
  "uuid": "ea1ac364-7422-4719-8d1f-bd8636ce98b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbDdbzvjMwCz2mE7gbaSVa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 6456,
      "cache_read_input_tokens": 48524,
      "output_tokens": 5268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 897,
          "output_tokens": 5268,
          "cache_read_input_tokens": 48524,
          "cache_creation_input_tokens": 6456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6456
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

_source line 33 · 2026-05-12T02:04:06.969Z_

I now have comprehensive research findings. Let me compile the final review.

## Key Research Findings Summary

**PGS (arXiv:2506.18315)**: Confirmed exists. "Use Property-Based Testing to Bridge LLM Code Generation and Validation" (v1, June 2025; v2 renamed "Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback", May 2026). Uses LLM-generated abstract properties + execution-based validation + minimal counterexample feedback. Evaluates on HumanEval/MBPP/LiveCodeBench only (NOT CodeContests or SWE-bench). 23.1-37.3% relative pass@1 improvement over TDD methods.

**NL-Debugging (arXiv:2505.15356)**: Confirmed exists. EMNLP 2025 **Oral** (ACL Anthology 2025.emnlp-main.80). Uses NL as intermediate representation for debugging via backtranslation → NL refinement → regeneration. Substantial gains on APPS and Codeforces.

**ContractEval (arXiv:2510.12047)**: Confirmed exists. Shows 0% contract satisfaction under standard prompting, 23-41% with explicit contracts, 49-53% with example-augmented specification.

**AlphaCodium 44% claim**: This is the **validation set** number. Test set pass@5 is 12% → 29% (still a 2.4x uplift, but the distinction matters).

**SWE-bench Verified contamination**: OpenAI officially stopped reporting in Feb 2026. Top score 93.9% on Verified vs ~46% on Pro. Severely compromised for frontier models.

**Qwen3-Coder-Next**: Released Feb 2026 (3B active/80B total MoE, 256k context, >70% SWE-bench Verified).

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "PGS (arXiv:2506.18315, June 2025/May 2026) already demonstrates properties > tests for LLM code refinement at inference time — ExeSpec's core insight. ExeSpec's genuine differentiators (execution grounding of specs, 4 task types vs generation-only, 5-component schema with ablation) are meaningful but incremental. Without citing PGS (5th consecutive round flagging this), an EMNLP reviewer familiar with PGS will reject on novelty."},
    "feasibility": {"score": 3, "rationale": "The 14–18 day timeline for a 3-stage framework + AlphaCodium baseline reimplementation + SWE-bench Docker setup + 4 conditions × 2 models × 3 primary benchmarks + supplementary benchmarks + ablations + paper writing is very aggressive; upper bound exceeds the 16-day constraint. SWE-bench Verified contamination undermines one of three primary benchmarks."},
    "clarity": {"score": 4, "rationale": "Well-structured proposal with clear 3-stage pipeline, controlled baselines (ExeSpec vs AlphaCodium-style vs Self-Spec vs direct prompting), honest spec-component ablation, and primary/supplementary benchmark distinction. The approach section is detailed and specific enough to implement."},
    "impact": {"score": 3, "rationale": "If property-level specs genuinely help beyond tests across debugging, completion, and issue resolution (not just generation, which PGS already covers), the multi-task extension is impactful. But DebugBench comparison against NL-Debugging (EMNLP 2025 Oral) is missing, and SWE-bench Verified contamination weakens the issue-resolution evaluation."}
  },
  "issues": [
    "CRITICAL — PGS STILL NOT CITED (5TH CONSECUTIVE ROUND): PGS (arXiv:2506.18315, 'Use Property-Based Testing to Bridge LLM Code Generation and Validation', June 2025, revised as 'Effective LLM Code Refinement via Property-Oriented and Structurally Minimal Feedback', May 2026) shares ExeSpec's core contribution: using LLM-generated abstract properties instead of test cases for code refinement with execution-based validation at inference time, training-free. PGS evaluates on HumanEval, MBPP, and LiveCodeBench ONLY (NOT CodeContests or SWE-bench — earlier reviewer claims about PGS's CodeContests/SWE-bench numbers were incorrect). PGS achieves 23.1-37.3% relative pass@1 improvement over TDD methods using DeepSeek-R1-Distilled-32B. This has been raised in Rounds 4, 5, 6, and 7 — all unaddressed. If unaddressed in Round 8, this MUST result in failure. No exceptions.",
    "NL-DEBUGGING STILL NOT CITED (3RD ROUND): NL-Debugging (arXiv:2505.15356, ACL Anthology 2025.emnlp-main.80) was accepted as an ORAL at EMNLP 2025 — the exact target venue. It uses natural language as an intermediate representation for debugging via backtranslation → NL refinement → regeneration, achieving substantial gains on APPS and Codeforces. EMNLP 2026 reviewers WILL know this paper. It establishes the 'structured intermediate representation for code tasks' paradigm at this venue and is a critical baseline for DebugBench evaluation.",
    "CONTRACTEVAL STILL NOT CITED (3RD ROUND): ContractEval (arXiv:2510.12047) shows 0% contract satisfaction under standard prompting, 23-41% with explicit contracts, 49-53% with example-augmented specification. This simultaneously validates ExeSpec's motivation (LLMs need grounding for contract/spec generation) AND quantifies the spec quality challenge. Must be cited to strengthen execution grounding motivation.",
    "ALPHACODIUM 44% CLAIM IS MISLEADING: The idea states 'AlphaCodium's flow engineering raises CodeContests pass@5 from 19% to 44%.' This is the VALIDATION SET result (117 problems). On the TEST SET (165 problems), AlphaCodium achieves 29% pass@5 (up from 12% baseline). The distinction must be clarified to avoid misleading readers.",
    "SWE-BENCH VERIFIED CONTAMINATION REMAINS INADEQUATELY ADDRESSED: OpenAI officially stopped reporting Verified scores in February 2026 after finding frontier models could reproduce verbatim gold patches. The current response ('noting contamination concerns, we report held-out test pass rates alongside standard metrics') is insufficient. Minimum acceptable: explicitly argue that Qwen2.5-Coder-7B/32B are sub-frontier models unlikely to exhibit the same contamination patterns as GPT-5.2/Claude Opus 4.5, and note that the community has moved to SWE-bench Pro. Better: add SWE-bench Pro as a co-primary benchmark.",
    "MODEL CURRENCY UNJUSTIFIED: Qwen3-Coder-Next (3B active/80B total MoE, 256k context, >70% SWE-bench Verified) was released February 2026. Using Qwen2.5-Coder without a justification sentence will invite reviewer questions. Add: 'We use Qwen2.5-Coder-7B/32B-Instruct as established dense models with reproducible vLLM inference; the method is model-agnostic.'",
    "MISSING ADDITIONAL RELEVANT WORK: (1) StoryCoder (arXiv:2604.14631, ACL 2026 Main) — training-free structured intermediate reasoning via narrative reformulation, +18.7% pass@10 across 11 models. Concurrent work using structured intermediate representations for code. (2) FixAudit (arXiv:2604.05560, April 2026) — jointly trains fixer and auditor, 35-37% improvement on CodeContests. (3) 'From Prompts to Properties' (FSE Companion 2025/LLanMER) — applies PBT to evaluate LLM code, finding 30-32% partial failures that pass@k misses. These should be cited in landscape or related work."
  ],
  "feedback": "This is Round 7, and the idea's experimental design, controlled baselines, and honest ablation commitment are the strongest aspects of the proposal. However, the repeated failure to cite PGS — now flagged for the 5TH CONSECUTIVE ROUND — is approaching disqualification territory. Here is exactly what must change:\n\n1. **CITE AND DIFFERENTIATE FROM PGS** (ABSOLUTE FINAL CHANCE — failure to address in Round 8 means automatic fail): Add PGS (arXiv:2506.18315) to key_references and landscape. Critically, note that PGS evaluates ONLY on HumanEval/MBPP/LiveCodeBench and does NOT evaluate on CodeContests, SWE-bench, or DebugBench. ExeSpec's differentiators vs. PGS: (a) ExeSpec execution-grounds specs BEFORE use via probes, catching hallucinated/contradictory specs — PGS validates properties against public tests but assumes ~87% property accuracy without catching internally inconsistent properties; (b) ExeSpec evaluates across 4 task types (generation, debugging, completion, issue resolution) — PGS covers generation/repair only; (c) ExeSpec's 5-component schema with component ablation decomposes which spec types help which tasks — PGS treats properties as a monolithic category; (d) ExeSpec directly compares against AlphaCodium on CodeContests, a benchmark neither PGS nor AlphaCodium compares against each other on. Reframe narrative: 'PGS demonstrated that property-level feedback outperforms test-based feedback for code generation. We advance this by: (1) execution-grounding specs to catch hallucinated properties, (2) extending to debugging/completion/issue-resolution, (3) decomposing spec component contributions via controlled ablation.'\n\n2. **CITE NL-DEBUGGING** (EMNLP 2025 Oral — reviewers at your target venue will know this): Add NL-Debugging (2505.15356) to key_references and landscape. Position ExeSpec's debugging as advancing beyond NL-level intermediate reasoning by providing structured, execution-verified behavioral constraints. Consider adding NL-Debugging as a 5th baseline condition on DebugBench for a strong venue-specific comparison.\n\n3. **CITE CONTRACTEVAL**: Add ContractEval (2510.12047) to motivate execution grounding: '0% contract satisfaction under standard prompting validates the need for execution-based spec verification.'\n\n4. **FIX ALPHACODIUM 44% CLAIM**: Clarify as 'AlphaCodium raises CodeContests validation-set pass@5 from 19% to 44% (test-set: 12% to 29%)' or simply cite the test-set numbers.\n\n5. **ADDRESS SWE-BENCH CONTAMINATION**: Add one paragraph: 'We use Qwen2.5-Coder-7B/32B, sub-frontier models unlikely to exhibit the verbatim gold-patch reproduction observed in frontier models (GPT-5.2, Claude Opus 4.5). We additionally note that the community has moved toward SWE-bench Pro for frontier evaluation; our results on sub-frontier models provide a contamination-resistant baseline.'\n\n6. **ADD MODEL JUSTIFICATION**: One sentence: 'We use Qwen2.5-Coder as established dense models with strong code performance and reproducible vLLM inference; the method is model-agnostic.'\n\nThe core structure is sound. Fix the competitive landscape and this can pass.",
  "reason": "PGS (arXiv:2506.18315) shares ExeSpec's core contribution (properties > tests at inference time) and has been flagged for 5 consecutive rounds without being cited — this is now the single blocking issue preventing passage."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea1ac364-7422-4719-8d1f-bd8636ce98b8",
  "isSidechain": false,
  "requestId": "req_011CawrKrE7XMYCwurxsxp6C",
  "type": "assistant",
  "uuid": "a31ff3b4-e610-4f3d-84b2-06c845c25b5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VbDdbzvjMwCz2mE7gbaSVa",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 897,
      "cache_creation_input_tokens": 6456,
      "cache_read_input_tokens": 48524,
      "output_tokens": 5268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6456,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 897,
          "output_tokens": 5268,
          "cache_read_input_tokens": 48524,
          "cache_creation_input_tokens": 6456,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6456
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

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a31ff3b4-e610-4f3d-84b2-06c845c25b5c",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Specification-Grounded Code Reasoning at Inference Time",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a31ff3b4-e610-4f3d-84b2-06c845c25b5c",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Specification-Grounded Code Reasoning at Inference Time",
  "sessionId": "9dc8ea75-e85f-4dda-a834-b95c01def98c"
}
```

---
