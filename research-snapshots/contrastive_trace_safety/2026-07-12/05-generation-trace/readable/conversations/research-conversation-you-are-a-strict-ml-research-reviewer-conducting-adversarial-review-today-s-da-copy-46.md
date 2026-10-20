# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-11 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/dfc514ab-163a-43aa-8fe2-f6ee8596621e.jsonl`
- **Structured JSON:** [`0dc3a4e108916f696a86.json`](../../sessions/0d/0dc3a4e108916f696a86.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T00:56:11.072Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T00:56:11.072Z",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-11 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 4/10)\n{\n  \"title\": \"ExeSpec: Verifiable Specification Reasoning for Code LLMs via Execution Grounding\",\n  \"core_problem\": \"Training-free inference-time methods for LLM code improvement—AlphaCodium (arXiv 2401.08500), CodeT (ICLR 2023), Self-Debugging (arXiv 2304.05128), S* (EMNLP 2025 Findings)—have demonstrated that execution feedback at inference time substantially boosts code generation quality. However, these methods uniformly treat test cases as their intermediate representation: they generate I/O test pairs, execute candidate code against them, and refine based on pass/fail signals. Tests are point samples—they verify specific inputs but do not capture behavioral intent (preconditions, postconditions, invariants, type constraints). This creates two limitations: (1) test-based methods provide pass/fail validation but not structured reasoning scaffolds that inform how code should behave across all inputs, and (2) they are largely restricted to code generation tasks where test generation is natural, without principled extension to debugging (where intended-vs-observed behavioral contrasts are needed), completion (where interface contracts must be inferred), or reasoning (where execution expectations must be formalized). Meanwhile, Self-Spec (Agents4Science 2025) showed that model-authored behavioral specifications improve generation (+2–5pp on HumanEval), but these specifications are never verified against execution—CodeSpecBench (arXiv 2604.12268) reveals only 20.2% success at repo-level spec generation, demonstrating that unverified LLM-generated specs are unreliable. Can execution-grounded behavioral specifications—richer than test cases, capturing universal behavioral properties—serve as verifiable structured intermediate reasoning that outperforms test-based refinement methods across diverse code tasks without model training?\",\n  \"opportunity\": \"Four research threads converge but remain disconnected: (1) Test-based inference-time refinement (AlphaCodium, CodeT, Self-Debugging, S*, BACE) proves execution feedback improves code generation—AlphaCodium's flow engineering raises CodeContests pass@5 from 19% to 44%, CodeT improves HumanEval pass@1 by +18.8pp via dual execution agreement, S* enables a 3B model to outperform GPT-4o-mini on LiveCodeBench—but all use test cases (point samples) as the intermediate representation, not property-level behavioral descriptions. (2) Specification-mediated reasoning (Self-Spec) demonstrates that LLM-authored specs improve generation by +2–5pp, establishing that structured behavioral intent aids code reasoning—but specs are never execution-verified, and 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025) shows that self-generated test feedback introduces systematic bias that degrades performance for some models, motivating richer intermediate representations beyond tests. (3) Execution-trace training (Think Like You Execute, RLEF at ICML 2025) achieves dramatic gains (+22–27pp) by grounding reasoning in execution, but requires fine-tuning on 54K+ verified rationales—not usable with frozen models. (4) CodeSpecBench reveals that LLMs achieve only 20.2% on repo-level spec generation, and SSDE (FSE Companion 2026) shows structured specs (Gherkin) can guide repo-level generation but requires human-authored specifications. The unexploited synthesis: use execution to verify LLM-generated behavioral specifications (pre/postconditions, invariants, type constraints—not just I/O pairs) at inference time, creating property-level reasoning scaffolds that capture universal behavioral intent rather than point samples. The key hypothesis: specifications provide fundamentally richer intermediate reasoning than tests because they describe what must hold for all inputs (universal properties) rather than what happens for specific inputs (existential examples), enabling the LLM to reason about behavioral correctness at a higher abstraction level.\",\n  \"landscape\": \"**Test-based inference-time methods.** AlphaCodium (arXiv 2401.08500, Jan 2024) is the most direct predecessor: a training-free multi-stage flow with problem reflection, AI test generation (6–8 diverse I/O pairs), and iterative execution-based refinement with test anchoring, achieving 44% pass@5 on CodeContests (vs. 19% direct prompting). Its pre-processing phase (problem reflection → public test reasoning → solution ranking → AI test generation) produces structured problem analysis in YAML format, and its code iteration phase uses test anchoring to prevent regression—fixes that break anchor tests are rejected. CodeT (ICLR 2023, arXiv 2207.10397) generates tests via LLMs and uses dual execution agreement (output consistency against generated tests + cross-sample agreement) for solution selection, improving HumanEval pass@1 by +18.8pp with code-davinci-002. Self-Debugging (arXiv 2304.05128, 2023) teaches LLMs to iteratively debug using execution results and natural language explanations (rubber-duck debugging), achieving up to 12% improvement on TransCoder and MBPP. 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025 Long, arXiv 2501.12793) reveals that post-execution self-debugging suffers from systematic bias in self-generated tests—in-execution debugging using intermediate program states mitigates this, demonstrating that test quality is a fundamental bottleneck for test-based methods. S* (EMNLP 2025 Findings, arXiv 2502.14382) combines parallel sampling (16 candidates) with sequential debugging and adaptive distinguishing input synthesis for execution-grounded selection, enabling a 3B model to outperform GPT-4o-mini and GPT-4o-mini+S* to outperform o1-preview by 3.7% on LiveCodeBench. BACE (GECCO 2026, arXiv 2603.28653) treats generated tests as noisy sensors via Bayesian updates, co-evolving code and test populations on LiveCodeBench v6, outperforming CodeSIM by +2.5–5.4pp. All these methods use test cases as the intermediate representation—point samples that verify specific inputs but don't capture universal behavioral properties.\\n\\n**Specification-based approaches.** Self-Spec (Agents4Science 2025) has LLMs author specification languages before code generation, improving GPT-4o HumanEval pass@1 from 87% to 92% (+5pp) and Claude 3.7 from 92% to 94% (+2pp), but only evaluates on single-function HumanEval, never verifies specs against execution, and doesn't extend beyond generation. SpecRover/AutoCodeRover-v2 (ICSE 2025) performs iterative NL specification inference for automated program repair, achieving 19.31% on SWE-bench (50%+ improvement over AutoCodeRover). VibeRepair (arXiv 2602.08263) translates code into NL behavioral specs for repair but specs are imprecise and hallucination-prone. SSDE (FSE Companion 2026, arXiv 2605.02455) uses Gherkin specifications and domain models for repo-level MVC generation—concurrent work demonstrating structured specs guide LLM generation, but requires human-authored specifications rather than LLM-generated and verified ones. CodeSpecBench (arXiv 2604.12268) benchmarks LLM spec generation showing only 20.2% repo-level pass rate, motivating execution-based verification of LLM-generated specs.\\n\\n**Execution-grounded training methods.** Think Like You Execute (arXiv 2512.00127) achieves +22–27pp on CRUXEval/LiveCodeBench via fine-tuning on 54K execution-trace-verified rationales. EG-CFG (NeurIPS 2025, arXiv 2506.10948) uses real-time execution via beam search over candidate lines—computationally expensive and generation-only. RLEF (ICML 2025) trains code LLMs with RL execution feedback. Think Anywhere (arXiv 2603.29957) enables on-demand reasoning during code generation via RL training, achieving 70.3% average across four benchmarks. CURE (NeurIPS 2025 Spotlight) co-evolves coder and tester via RL. All require training—not applicable with frozen models.\\n\\n**Other relevant work.** SCoT (ACL 2024) adds program structure to CoT without execution grounding. Test overfitting studies show 21.8–35.9% of LLM patches overfit visible tests (arXiv 2511.16858), and ICSE 2026 NIER proves overfitting is undecidable without full specifications—motivating property-level specs as reasoning scaffolds.\\n\\n**The gap.** Existing training-free methods use tests (point samples) for validation. No work uses property-level behavioral specifications (pre/postconditions, invariants, type constraints) as execution-grounded structured intermediate reasoning in a training-free framework, with controlled evidence that property-level specs outperform test-based refinement across diverse code tasks.\",\n  \"approach\": \"We propose ExeSpec, a training-free inference-time framework that uses execution-grounded behavioral specifications as verifiable structured intermediate reasoning for LLM code tasks. The critical distinction from test-based methods (AlphaCodium, CodeT, S*) is that ExeSpec generates property-level behavioral descriptions—universal constraints about what code must satisfy for all inputs—rather than point-sample test cases that verify specific I/O pairs. This provides richer reasoning scaffolds: knowing 'f(x) returns 2x for all non-negative integers, raises ValueError for negative inputs' (specification) enables different reasoning than knowing 'f(5)=10, f(3)=6' (tests).\\n\\n**Stage 1: Spec Elicitation.** Given a task input, prompt the LLM to generate structured behavioral specifications in a lightweight JSON schema containing five component types: (a) I/O example pairs (shared with test-based methods—this is the overlap with AlphaCodium), (b) preconditions (constraints on valid inputs/states, e.g., 'n >= 0', 'input list is non-empty'), (c) postconditions (properties guaranteed on outputs, e.g., 'output is sorted in ascending order', 'len(output) == len(input)'), (d) type constraints (parameter and return type annotations with generics, e.g., 'List[int] -> int'), and (e) invariants (loop invariants, monotonicity, ordering properties, e.g., 'partial_sum increases monotonically'). The schema is task-adapted: generation tasks derive specs from docstrings and problem descriptions; debugging tasks elicit intended-vs-observed behavioral contrasts (the spec says the output should be sorted, but the code produces [3,1,2]); issue resolution tasks extract expected behavioral changes from issue descriptions and failing test context.\\n\\n**Stage 2: Execution Grounding.** Validate and refine specifications by executing lightweight probes against available code context, catching hallucinated or contradictory specs before they corrupt downstream reasoning. For generation tasks: generate a quick candidate solution, execute against spec-derived assertions—both I/O examples (like AlphaCodium) AND postcondition property checks (e.g., assert all(output[i] <= output[i+1] for i in range(len(output)-1)) for a sorting postcondition)—identify spec-execution mismatches, and revise contradicted specs. For debugging tasks: execute the buggy code, compare execution traces against specs to identify precisely which behavioral constraints (not just which test cases) are violated, producing structured violation reports (e.g., 'postcondition violated: output should be sorted but is [3,1,2]; invariant violated: partial_sum is not monotonically increasing at iteration 3'). For issue resolution (SWE-bench): extract behavioral expectations from issue descriptions and failing tests, generate specs characterizing the intended fix behavior, and validate spec consistency against the existing test suite via Docker-based execution. When full execution is unavailable, static grounding serves as fallback: cross-spec consistency checking (e.g., precondition implies postcondition is satisfiable), type inference from signatures, and contradiction detection across spec components.\\n\\n**Stage 3: Spec-Guided Task Completion.** Feed grounded specs alongside the original task input to the LLM for final output. The model reasons about behavioral intent (what the code should do per verified property-level specs) rather than surface patterns. When outputs violate specs, structured violation reports (which constraints failed, expected vs. actual, which spec component) feed back for iterative refinement (up to 3 rounds). The key difference from test-based iteration (AlphaCodium): violation reports reference behavioral properties ('postcondition: output must be monotonically increasing'), not just I/O failures ('test case 3 failed'), giving the LLM richer corrective signal.\\n\\n**Baselines and controlled experiments.** The experimental design explicitly isolates the spec-vs-test distinction through four controlled conditions: (a) ExeSpec full (property-level specs + execution grounding), (b) AlphaCodium-style baseline (problem reflection + AI test generation + iterative execution/refinement, no property-level specs)—this directly tests whether specs provide gains beyond test-based refinement and is the paper's critical comparison, (c) Self-Spec baseline (specs without execution grounding)—tests the contribution of grounding, (d) direct prompting (no intermediate reasoning). The delta between (a) and (b) is the paper's core contribution. Additionally, a controlled spec-component ablation isolates the value of each spec type: (i) full specs (I/O + pre/postconditions + invariants + type constraints), (ii) I/O-only specs (functionally equivalent to AlphaCodium's AI test cases—the overlap region), (iii) structural specs only (pre/postconditions + invariants + type constraints, no I/O examples). If (ii) performs similarly to (i), the novelty claim is weakened—this ablation is the critical honesty test for the paper. S* is positioned as complementary (parallel/sequential scaling with execution-based selection) and could be combined with ExeSpec's spec-mediated reasoning; we note this in Related Work and Future Work but do not implement the combination.\\n\\n**Benchmarks.** Primary benchmarks with full baselines (all four conditions + spec-component ablation): DebugBench (C++/Java/Python debugging—specs naturally capture intended-vs-observed behavioral contrasts, the task type most differentiated from test-only methods), CodeContests (competitive programming—direct comparison to AlphaCodium on its home turf, using the same benchmark), and SWE-bench Verified (real-world issue resolution with Docker-based test execution—noting contamination concerns per OpenAI's 2026 audit, we report held-out test pass rates alongside standard metrics). Supplementary benchmarks with ExeSpec vs. direct prompting only: HumanEval+/MBPP+ (for Self-Spec comparability only, not primary given frontier models score 93%+), CrossCodeEval and RepoBench (cross-file completion with static grounding). For supplementary cross-file completion benchmarks, ExeSpec relies on static grounding: extracting type signatures from imported modules, inferring parameter/return types from usage context at call sites, and validating completions via type checkers (mypy/pyright for Python, tsc for TypeScript). We explicitly acknowledge this is weaker grounding than dynamic execution and report the proportion of instances where only static grounding was available.\\n\\n**Analysis.** Beyond standard metrics, we report: (1) spec quality analysis—correlation between spec correctness (measured by agreement with ground-truth behavior) and downstream task performance; (2) grounding effectiveness—proportion of hallucinated specs caught by execution grounding vs. passing through undetected; (3) spec-component contribution—which spec types (I/O, preconditions, postconditions, invariants, type constraints) most improve each task type; (4) test overfitting rates—proportion of solutions passing visible tests but failing held-out tests, comparing ExeSpec vs. baselines (addressing ICSE 2026 undecidability concern); (5) qualitative case studies showing where property-level specs enable corrections that test-only methods miss (e.g., off-by-one errors caught by ordering invariants but missed by finite test cases, type constraint violations caught by postcondition checks).\\n\\nAll experiments use Qwen2.5-Coder-7B-Instruct and Qwen2.5-Coder-32B-Instruct via vLLM batch inference on H100 GPUs, with SWE-bench evaluation using the existing Docker harness.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~100–150 H100-hours (primary benchmarks DebugBench + CodeContests + SWE-bench Verified with 4 conditions × 2 models + spec-component ablation on primary benchmarks; supplementary HumanEval+/MBPP+ + CrossCodeEval + RepoBench with ExeSpec vs. direct prompting × 2 models; using vLLM batch inference with Qwen2.5-Coder-7B on 1 H100 and 32B on 1–2 H100s)\",\n      \"gpu_utilization\": \"Moderate (~40–55%): alternating between inference bursts and execution-grounding phases (running generated code against assertions, Docker-based test execution for SWE-bench); execution harness is CPU-bottlenecked while GPU idles during test runs\",\n      \"timeline\": \"14–18 days (days 1–3: framework implementation + AlphaCodium-style baseline reimplementation using open-source AlphaCodium code + eval harness setup leveraging existing SWE-bench Docker harness, EvalPlus, and benchmark repositories; days 4–7: primary benchmarks DebugBench + CodeContests with all 4 conditions; days 8–10: SWE-bench Verified with all 4 conditions; days 11–12: supplementary benchmarks HumanEval+/MBPP+ + CrossCodeEval + RepoBench with ExeSpec vs. direct prompting; days 13–15: spec-component ablation on DebugBench + CodeContests + analysis; days 16–18: writing)\",\n      \"team\": \"2 researchers (1 lead for ExeSpec framework + spec-grounding pipeline + spec-component ablation design, 1 for AlphaCodium baseline adaptation from open-source code + benchmark integration + evaluation infrastructure)\",\n      \"estimated_gpu_cost\": \"$300–450 (on-demand H100 at ~$3/hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~120–170 H100-hours (same scope as manual with more systematic spec quality validation and additional analysis iterations)\",\n      \"gpu_utilization\": \"Moderate–High (~50–65%): agent queues experiment batches across benchmarks while human reviews spec quality between rounds\",\n      \"timeline\": \"10–14 days (agent handles framework code, experiment orchestration, and result collection; human validates spec schema design, reviews AlphaCodium baseline fidelity, and guides ablation priorities)\",\n      \"team\": \"1 researcher, ~2–3 hrs/day reviewing spec elicitation outputs, validating AlphaCodium baseline implementation matches the published flow, approving experiment plans, and analyzing spec-component ablation results\",\n      \"claude_api_cost\": \"$100–200 (1000–2000 orchestration turns at ~$0.10/turn for code generation, experiment design, and result analysis)\",\n      \"estimated_gpu_cost\": \"$360–510\",\n      \"risk_note\": \"AlphaCodium baseline reimplementation fidelity is a key risk—must reproduce the core flow (problem reflection + AI test generation + iterative execution with test anchoring) faithfully; recommend using AlphaCodium's open-source code (github.com/Codium-ai/AlphaCodium) as starting point and adapting for non-CodeContests benchmarks (DebugBench, SWE-bench)\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~150–200 H100-hours (systematic sweeps over spec granularity levels, grounding strategies per benchmark, additional model backbone DeepSeek-Coder-V2-Lite-16B, temperature and sample-count variations)\",\n      \"gpu_utilization\": \"High (~80–90%): agent pipelines experiments back-to-back with minimal idle; parallel runs across benchmarks on multiple H100s\",\n      \"timeline\": \"6–9 days with 4–8 H100s available concurrently (bottlenecked by SWE-bench Docker container builds and sequential test execution per instance)\",\n      \"team\": \"0 (initial setup ~3–4 hours for benchmark harness configuration, AlphaCodium baseline setup from open-source code, and vLLM model serving, then fully autonomous)\",\n      \"claude_api_cost\": \"$200–400 (2000–4000 turns for iterative experiment design, spec schema optimization, cross-benchmark analysis, and paper section drafting)\",\n      \"estimated_gpu_cost\": \"$450–600\",\n      \"speed_bottleneck\": \"SWE-bench Verified Docker-based test execution (sequential per instance, ~2–5 min per task including container setup) and DebugBench compilation/execution harness; inference itself is fast with vLLM on H100\",\n      \"risk_note\": \"Agent may over-optimize spec schema for one benchmark at the expense of others; need guardrails to ensure the AlphaCodium baseline is faithfully implemented (using open-source code, not strawmanned) and that the spec-component ablation is run completely even if early results are unfavorable\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission May 25, 2026; commitment Aug 2, 2026; NLP and Code Models track; Budapest, Hungary)\",\n    \"ACL 2027 (expected ARR commitment ~Jan 2027; fallback if EMNLP revision needed)\",\n    \"NAACL 2027 (expected ARR commitment ~Mar 2027; second fallback)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"AlphaCodium: Code Generation through Flow Engineering (arXiv 2401.08500, Jan 2024)\",\n    \"CodeT: Code Generation with Generated Tests (ICLR 2023, arXiv 2207.10397)\",\n    \"Teaching Large Language Models to Self-Debug (Self-Debugging; arXiv 2304.05128, 2023)\",\n    \"Revisit Self-Debugging with Self-Generated Tests for Code Generation (ACL 2025 Long, arXiv 2501.12793)\",\n    \"S*: Test Time Scaling for Code Generation (EMNLP 2025 Findings, arXiv 2502.14382)\",\n    \"BACE: Bayesian Anchored Co-Evolution of Code and Test Populations (GECCO 2026, arXiv 2603.28653)\",\n    \"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation (Agents4Science 2025)\",\n    \"Execution Guided Line-by-Line Code Generation (EG-CFG; NeurIPS 2025, arXiv 2506.10948)\",\n    \"Think Like You Execute: Verifiable Chain of Thought from Program Traces (arXiv 2512.00127)\",\n    \"Think Anywhere in Code Generation (arXiv 2603.29957, Mar 2026)\",\n    \"SpecRover: Code Intent Extraction via LLMs (ICSE 2025)\",\n    \"CURE: Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning (NeurIPS 2025 Spotlight)\",\n    \"Code Execution as Grounded Supervision for LLM Reasoning (EMNLP 2025)\",\n    \"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (arXiv 2604.12268, Apr 2026)\",\n    \"Specification Vibing for Automated Program Repair (VibeRepair; arXiv 2602.08263, Feb 2026)\",\n    \"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering (SSDE; FSE Companion 2026, arXiv 2605.02455)\",\n    \"Investigating Test Overfitting on SWE-bench (arXiv 2511.16858)\",\n    \"The Undecidability of Overfitting in Automated Program Repair (ICSE 2026 NIER)\",\n    \"RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning (ICML 2025)\",\n    \"Structured Chain-of-Thought Prompting for Code Generation (SCoT; ACL 2024)\",\n    \"Qwen2.5-Coder Technical Report (arXiv 2409.12186)\"\n  ],\n  \"description\": \"We propose ExeSpec, a training-free inference-time framework that uses execution-grounded behavioral specifications as verifiable structured intermediate reasoning for LLM code tasks. The critical distinction from existing test-based methods (AlphaCodium, CodeT, Self-Debugging, S*) is that ExeSpec generates property-level behavioral descriptions—preconditions, postconditions, invariants, type constraints—that capture universal behavioral intent, rather than point-sample test cases that verify specific I/O pairs. The method operates in three stages: (1) Spec Elicitation—prompt the LLM to generate structured behavioral specifications (I/O examples, pre/postconditions, invariants, type constraints) in a JSON schema; (2) Execution Grounding—validate specs by executing lightweight probes (running candidate code against spec-derived property assertions, comparing buggy code behavior against intended specs, type-checking completion context), catching hallucinated specs before they corrupt reasoning; (3) Spec-Guided Completion—use grounded specs as verified intermediate reasoning with structured violation feedback for iterative refinement. The experimental design explicitly isolates the paper's contribution through four controlled conditions: (a) ExeSpec full (property-level specs + execution grounding), (b) AlphaCodium-style baseline (problem reflection + AI test generation + iterative execution/refinement, no property-level specs), (c) Self-Spec baseline (specs, no execution grounding), (d) direct prompting. The delta between (a) and (b) is the core contribution—whether property-level specs provide gains beyond test-based refinement. A critical spec-component ablation further decomposes: (i) full specs, (ii) I/O-only specs (≈ tests, AlphaCodium-equivalent), (iii) structural specs only (pre/postconditions + invariants, no I/O)—if (ii) ≈ (i), the novelty claim collapses, and we commit to reporting this honestly. Primary benchmarks with full baselines: DebugBench (debugging), CodeContests (competitive programming—AlphaCodium's home benchmark), SWE-bench Verified (issue resolution). Supplementary with ExeSpec vs. direct prompting only: HumanEval+/MBPP+ (Self-Spec comparability), CrossCodeEval/RepoBench (cross-file completion with static grounding via type checkers). S* is positioned as complementary (test-time scaling via execution-based selection); SSDE is concurrent work using human-authored Gherkin specs. All experiments use Qwen2.5-Coder-7B/32B-Instruct via vLLM on H100 GPUs. Within 100–150 H100-hours and ~16 days. Primary target: EMNLP 2026 (ARR May 25, 2026).\",\n  \"project_name\": \"test_spec_guided_repair\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL VENUE MISMATCH: User explicitly requested EMNLP 2026 (ARR deadline 2026-05-25, NLP and Code Models track), but the idea targets ICSE 2027, AAAI 2027, and FSE 2027 — all SE venues. The idea must be redesigned or reframed for EMNLP.\", \"CRITICAL COMPUTE VIOLATION: User constrained to ≤200 H100-hours total. The idea estimates 250-400 A100-80GB hours (manual mode). Running Kimi K2-Instruct (1T params MoE, requiring 4×A100 per instance) adds substantial inference costs not fully accounted for.\", \"CRITICAL TIMELINE VIOLATION: User has ~14 days. The idea estimates 3-5 months (manual), 6-10 weeks (HIL), or 1-3 weeks with 8-16 A100s (auto). None of these fit the user's constraint.\", \"EVAL BENCHMARK MISMATCH: User requested evaluation on SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, and CodeContests. The idea only covers SWE-bench Verified and Defects4J (which isn't even in the user's list). Missing 5 of 6 required benchmarks.\", \"MISSING CRITICAL RELATED WORK: (1) SpecRover/AutoCodeRover-v2 (ICSE 2025) — already does specification inference for patching; (2) CURE (NeurIPS 2025 Spotlight) — RL co-evolution of coder and tester; (3) CodeSpecBench (arXiv 2604.12268, Apr 2026) — benchmark showing LLMs achieve only 20.2% on repo-level behavioral spec generation; (4) Test overfitting undecidability (ICSE 2026 NIER) + empirical study (arXiv 2511.16858) showing 21-33% of LLM patches overfit on visible tests; (5) Dynamic Cogeneration at Google (arXiv 2601.19066); (6) SWE-Tester (arXiv 2601.13713).\", \"NOVELTY CONCERN: The idea is too similar to VibeRepair (arXiv 2602.08263, Feb 2026). VibeRepair already translates code into structured behavioral specifications for repair, achieving SOTA on Defects4J. The proposed delta — using test assertions instead of NL as the specification source — is an incremental variant, not a fundamentally new paradigm. SpecRover (ICSE 2025) also does specification inference for repair.\", \"TOPIC SCOPE TOO NARROW: User asked for 'code understanding and generation' covering repo-level comprehension, code reasoning, debugging, test generation, code-to-documentation, cross-language transfer. The idea focuses narrowly on Java program repair via Defects4J, which is only one subtask and one language.\", \"MISLEADING CLAIMS: '174/178 correct repairs' reads as a fraction but actually means 174 on v1.2 and 178 on v2.0. 'Proving specification-level repair is superior' overstates VibeRepair's own conclusions. The 48.29% for Repair-R1 represents only a 2.68pp improvement over baseline.\", \"TEST OVERFITTING NOT ADDRESSED: An ICSE 2026 NIER paper proves test overfitting is theoretically undecidable when full specifications are unavailable. An empirical study shows 21-33% of LLM patches overfit on visible tests. The idea's reliance on auto-generated tests as specifications is directly vulnerable to this fundamental limitation.\"]\nFeedback: This idea has a reasonable technical intuition (test assertions as behavioral specs) but fundamentally fails to meet the user's requirements. Here is what needs to change:\n\n1. **VENUE**: Reframe for EMNLP 2026 (NLP and Code Models track) or propose a different idea entirely. For EMNLP, the contribution must emphasize NLP methodology (e.g., how LLMs reason about code specifications, a new inference-time algorithm for code understanding) rather than SE pipeline engineering. EMNLP reviewers care about language model capabilities, not Defects4J leaderboard numbers.\n\n2. **SCOPE**: Broaden beyond Java program repair. The user wants 'code understanding and generation' covering multiple tasks (debugging, test generation, code reasoning, cross-language transfer). Consider a method that applies across multiple code tasks, not just APR.\n\n3. **BENCHMARKS**: Must evaluate on the user's required benchmarks: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests. Drop Defects4J (not requested).\n\n4. **COMPUTE**: Stay within ≤200 H100-hours. Use smaller models (DeepSeek-Coder-V2-Lite-Instruct 16B, StarCoder2-15B, Qwen2.5-Coder-7B/32B) as the user suggested, not 1T-param Kimi K2. This also aligns with the user's suggested model list.\n\n5. **TIMELINE**: Design for ≤16 days of execution. Build on existing frameworks (aider, SWE-agent, Moatless) as the user suggested. The current 3-5 month estimate is a non-starter.\n\n6. **NOVELTY BOOST**: Differentiate more clearly from VibeRepair and SpecRover. Instead of 'yet another spec-guided repair pipeline,' consider: (a) a novel inference algorithm that uses execution feedback to iteratively refine code understanding, (b) a retrieval-augmented approach with semantic code search for cross-repo transfer, or (c) a method for repo-level context compression that enables better code reasoning — all directions the user explicitly suggested.\n\n7. **ADDRESS TEST OVERFITTING**: Any test-based approach must engage with the ICSE 2026 undecidability result and the empirical overfitting findings. Propose concrete mitigation strategies.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MISSING CRITICAL BASELINES: AlphaCodium (arXiv 2401.08500, Jan 2024) is a training-free, inference-time, test-based iterative flow with problem analysis + AI test generation + iterative refinement against tests. It is the most direct conceptual predecessor to ExeSpec and MUST be cited and compared as a baseline. CodeT (ICLR 2022) and Self-Debugging (arXiv 2304.05128, 2023) are also missing—both are foundational works in execution-based code refinement at inference time.\", \"MISSING CONCURRENT WORK: BACE (arXiv 2603.28653, Mar 2026) addresses the same 'noisy self-generated tests' problem via Bayesian co-evolution of code and test populations. 'Revisit Self-Debugging with Self-Generated Tests' (arXiv 2501.12793, Jan 2025) directly studies post-execution vs. in-execution self-debugging paradigms with LLM-generated tests. Both must be discussed.\", \"THIN NOVELTY BOUNDARY: The distinction between 'structured behavioral specifications' (I/O example pairs, pre/postconditions, invariants in JSON schema) and 'self-generated test assertions' is conceptually thin. I/O examples ARE test cases. Pre/postconditions and invariants add something, but AlphaCodium's 'problem analysis' + 'edge case identification' phase also generates structured problem understanding before coding. The paper needs to sharpen why spec-mediated reasoning is fundamentally different from test-mediated refinement, with controlled experiments isolating this distinction.\", \"HUMANEVAL SATURATION: HumanEval+ and MBPP+ are listed as primary benchmarks, but frontier models already score 93%+ on HumanEval. Even with EvalPlus's harder tests, the benchmark is near saturation. The paper should emphasize DebugBench, CrossCodeEval, CodeContests, and SWE-bench Verified as primary evaluation, and use HumanEval+/MBPP+ only for comparability with Self-Spec.\", \"SPEC QUALITY BOOTSTRAPPING RISK: CodeSpecBench shows LLMs achieve only 20.2% on repo-level spec generation. If the LLM generates mostly bad specs, execution grounding catches them—but then the method degrades to 'generate specs → discard most → fall back to direct generation.' The paper needs analysis of what happens when spec generation quality is low (e.g., on CrossCodeEval/RepoBench repo-level tasks), including a failure mode analysis.\", \"TIMELINE IS VERY AGGRESSIVE: 12–16 days for implementing a 3-stage framework with task-adapted spec schemas, integrating 6 benchmarks (including SWE-bench Docker), running 48+ experiment configurations (6 benchmarks × 2 models × 4 baselines + ablations), AND writing a full paper. SWE-bench Verified Docker setup alone can take 2–3 days. Recommend reducing scope: run full comparison on 3 primary benchmarks (DebugBench, CodeContests, SWE-bench Verified) and use 3 others (HumanEval+/MBPP+, CrossCodeEval/RepoBench) for supplementary evaluation with fewer baselines.\", \"COST ESTIMATE MISSING API COSTS FOR EG-CFG BASELINE: Reproducing an EG-CFG-style execution-only baseline requires beam search with per-line execution, which is substantially more expensive than standard inference. This is either infeasible within budget or needs to be replaced with a simpler 'execution feedback without specs' baseline.\"]\nFeedback: The revision successfully addresses the critical venue, compute, and scope issues from Round 1. The idea is now properly scoped for EMNLP 2026 with correct benchmarks, models, and budget. However, several issues need resolution:\n\n1. **Sharpen novelty vs. AlphaCodium/CodeT**: These are the most important missing baselines. AlphaCodium (2024) already does training-free, multi-stage, test-based iterative refinement at inference time. ExeSpec must demonstrate that specification-mediated reasoning (structured I/O examples + pre/postconditions + invariants) provides gains BEYOND what test-based refinement alone achieves. Add a controlled experiment: (a) ExeSpec with full specs, (b) AlphaCodium-style test-only refinement, (c) Self-Spec without execution grounding, (d) direct prompting. The delta between (a) and (b) is the paper's core contribution.\n\n2. **De-emphasize saturated benchmarks**: Make DebugBench, CodeContests, and SWE-bench Verified the primary evaluation. Use HumanEval+/MBPP+ for Self-Spec comparability only. Consider adding LiveCodeBench for contamination resistance.\n\n3. **Address spec quality gracefully**: Add a spec quality analysis section showing: (a) what fraction of elicited specs survive execution grounding, (b) how grounding changes spec accuracy, (c) what happens when most specs fail (does the method degrade gracefully?). This directly responds to the CodeSpecBench 20.2% finding and strengthens the paper's analytical contribution.\n\n4. **Simplify the EG-CFG baseline**: Replace the full EG-CFG-style baseline (beam search + per-line execution) with a simpler 'execution feedback without specs' baseline: generate code → execute → feed error messages back → regenerate. This is cheaper and more directly tests the spec contribution.\n\n5. **Reduce timeline risk**: Implement the framework first on HumanEval+/MBPP+ (fast turnaround), validate the approach, then extend to harder benchmarks. Consider submitting to ARR May 25 with 4 benchmarks instead of 6, adding the remaining 2 for the camera-ready.\n\n6. **Cite and discuss**: AlphaCodium (2401.08500), CodeT (ICLR 2022), Self-Debugging (2304.05128), BACE (2603.28653), Revisit Self-Debugging (2501.12793). Position ExeSpec as advancing beyond test-only refinement by introducing verifiable specification reasoning as a structured intermediate representation.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL UNADDRESSED R2 FEEDBACK: AlphaCodium (arXiv 2401.08500, Jan 2024), CodeT (ICLR 2023), Self-Debugging (arXiv 2304.05128, 2023), BACE (arXiv 2603.28653, Mar 2026), and 'Revisit Self-Debugging with Self-Generated Tests' (ACL 2025, arXiv 2501.12793) are ALL still missing from key_references and baselines. Round 2 explicitly stated these MUST be cited and compared. AlphaCodium is the most direct conceptual predecessor — a training-free, multi-stage flow with problem reflection, test generation, and iterative execution-based refinement — and must be a baseline, not just a citation.\", \"NEW MISSING WORK — S* (EMNLP 2025 Findings, arXiv 2502.14382): A training-free test-time scaling framework for code generation that uses execution-based selection with adaptive distinguishing input synthesis. Enables a 3B model to outperform GPT-4o-mini. Published at EMNLP 2025 — the same venue being targeted. This is a highly relevant prior art that directly competes in the 'training-free inference-time code improvement' space.\", \"NEW MISSING CONCURRENT WORK — SSDE (arXiv 2605.02455, May 2026): 'LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering' uses Gherkin specifications and domain models to guide LLM generation with verification against test suites. Concurrent work that overlaps with ExeSpec's structured specification approach at the repo level.\", \"THIN NOVELTY BOUNDARY WITH ALPHACODIUM: AlphaCodium's pre-processing phase (problem reflection → public tests reasoning → possible solutions ranking) IS structured problem analysis before code generation. AlphaCodium's iterative phase (generate → execute → fix against public + AI tests) IS execution-grounded refinement. ExeSpec's I/O example specs are functionally identical to AlphaCodium's AI-generated test cases. The actual novelty delta — pre/postconditions, invariants, type constraints in JSON schema — must be isolated via controlled ablation: (a) ExeSpec full specs, (b) I/O-only specs (≈ test-only, AlphaCodium-style), (c) structural specs only (pre/postconditions + invariants without I/O). Without this, reviewers will reject for insufficient novelty.\", \"UNDERSPECIFIED NON-GENERATION TASKS: The approach for cross-file completion (CrossCodeEval, RepoBench) says 'type-check and partially execute the surrounding context to verify inferred specs.' This is vague. How do you generate behavioral specs for incomplete code in a multi-file context? What executable probes work for partial programs? CodeSpecBench shows only 20.2% success at repo-level spec generation — the method may degrade to fallback (soft grounding) for most repo-level instances, making the execution grounding contribution negligible on these benchmarks.\", \"HUMANEVAL+ STILL NOT DE-EMPHASIZED: Round 2 explicitly recommended making DebugBench, CodeContests, and SWE-bench Verified primary, with HumanEval+/MBPP+ for Self-Spec comparability only. The idea still lists them alongside other benchmarks without prioritization. Frontier models score 93%+ on HumanEval — gains here are not impressive.\", \"AGGRESSIVE TIMELINE NOT MITIGATED: Round 2 suggested reducing to 3 primary benchmarks + 3 supplementary. The idea still plans full comparison on all 6 benchmarks within 12–16 days. SWE-bench Docker setup alone takes 2–3 days. Recommend: primary (DebugBench, CodeContests, SWE-bench Verified) with full baselines; supplementary (HumanEval+/MBPP+, CrossCodeEval, RepoBench) with ExeSpec vs. direct prompting only.\"]\nFeedback: This is Round 3, and the idea has improved significantly from Round 1 (correct venue, benchmarks, compute budget) but has failed to address the MOST CRITICAL Round 2 feedback: citing and comparing against AlphaCodium, CodeT, Self-Debugging, BACE, and 'Revisit Self-Debugging.' This is not optional — these are the papers that define the competitive landscape for training-free, execution-based code improvement methods.\n\nHere is exactly what needs to change:\n\n1. **ADD ALPHACODIUM AS PRIMARY BASELINE** (non-negotiable): Replace the 'EG-CFG-style execution-only feedback' baseline with an AlphaCodium-style baseline: problem analysis → AI test generation → iterative code execution/refinement (no structured specs). This directly tests the paper's core claim that specification-mediated reasoning provides gains beyond test-based refinement. The controlled experiment should be: (a) ExeSpec full (specs + execution grounding), (b) AlphaCodium-style (tests + execution feedback, no specs), (c) Self-Spec (specs, no execution grounding), (d) direct prompting. The delta between (a) and (b) is the paper's contribution.\n\n2. **CITE AND POSITION AGAINST S* (EMNLP 2025 Findings)**: S* is the most recent training-free test-time scaling method for code generation, published at your target venue. Position ExeSpec as complementary: S* focuses on parallel/sequential scaling with execution-based selection; ExeSpec focuses on structured intermediate reasoning via verified specs. They could potentially be combined.\n\n3. **SHARPEN THE SPEC VS. TEST DISTINCTION**: The paper must clearly argue why structured behavioral specifications (pre/postconditions, invariants, type constraints) provide fundamentally different reasoning scaffolding compared to test cases. Add a controlled ablation: (a) full specs (I/O + pre/postconditions + invariants), (b) I/O-only specs (≈ test cases), (c) structural specs only (pre/postconditions + invariants, no I/O). If (b) performs similarly to (a), the novelty claim collapses.\n\n4. **SPECIFY THE CROSS-FILE COMPLETION APPROACH**: Describe concretely how ExeSpec generates and validates specs for CrossCodeEval/RepoBench tasks. What does the spec schema look like for incomplete code with cross-file dependencies? What 'lightweight probes' execute for partial programs? If the approach fundamentally differs from function-level generation, say so explicitly.\n\n5. **REDUCE SCOPE TO FIT TIMELINE**: Primary benchmarks with full baselines: DebugBench, CodeContests, SWE-bench Verified. Supplementary with ExeSpec vs. direct prompting only: HumanEval+/MBPP+, CrossCodeEval, RepoBench. This halves the experiment matrix.\n\n6. **ADD TO KEY REFERENCES**: AlphaCodium (2401.08500), CodeT (ICLR 2023, 2207.10397), Self-Debugging (2304.05128), BACE (2603.28653), 'Revisit Self-Debugging' (ACL 2025, 2501.12793), S* (EMNLP 2025 Findings, 2502.14382), SSDE (2605.02455).\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-12T00:56:11.077Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T00:56:11.077Z",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---

## Round 1

47 recorded events

### User

_source line 3 · 2026-05-12T00:56:11.118Z_

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
  "promptId": "9e08ddf0-33d2-4d92-a77f-55540a5b8b2a",
  "type": "user",
  "uuid": "5028706f-6a5c-4598-a4af-9052ea922606",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T00:56:11.115Z_

```json
{
  "parentUuid": "5028706f-6a5c-4598-a4af-9052ea922606",
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
  "uuid": "b29ce045-df45-4e17-8ad4-31454ea849e8",
  "timestamp": "2026-05-12T00:56:11.115Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T00:56:11.115Z_

```json
{
  "parentUuid": "b29ce045-df45-4e17-8ad4-31454ea849e8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "432ba109-4e15-4b06-940a-94cb7ba267bc",
  "timestamp": "2026-05-12T00:56:11.115Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
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
  "leafUuid": "432ba109-4e15-4b06-940a-94cb7ba267bc",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Execution-grounded behavioral specifications for code reasoning",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---

### Assistant

_source line 8 · 2026-05-12T00:56:25.381Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea - "ExeSpec: Verifiable Specification Reasoning for Code LLMs via Execution Grounding" - in its Round 4 revision. I need to independently verify claims, check for missing work, assess novelty, feasibility, and overall quality.

Let me start by understanding what changed from Round 3:
1. AlphaCodium is now cited and positioned as a primary baseline - this was the most critical R2/R3 feedback
2. CodeT, Self-Debugging, BACE, "Revisit Self-Debugging" are now all in key_references


3. S* (EMNLP 2025 Findings) and SSDE are now properly positioned as complementary and concurrent work respectively
4. The experimental design is much more rigorous now - I can see they're comparing against AlphaCodium-style baselines and Self-Spec, with direct prompting as a control, plus a detailed ablation that isolates I/O specs from structural specs to show where ExeSpec actually adds value beyond what AlphaCodium already does
5. The benchmark selection is now more strategic, prioritizing DebugBench, CodeContests, and SWE-bench Verified as primary evaluation targets while using HumanEval+ and others for supplementary validation
6. Cross-file completion is grounded in actual type checker output rather than being speculative
7. The timeline of 14-18 days is feasible within the constraints

Now I need to verify the core claims - whether the cited papers actually exist and support what's being claimed, check for any overlooked competing work, validate that specs are genuinely different from using tests as intermediate reasoning, and assess whether the timeline and compute requirements are realistic for this scope.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "432ba109-4e15-4b06-940a-94cb7ba267bc",
  "isSidechain": false,
  "requestId": "req_011CawmJczH57PSbp4Vbpaqk",
  "type": "assistant",
  "uuid": "c1f5c979-9aee-404a-b5ee-ae59f5a01621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKLyqh5pWMPZdPTsQhfpDG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20585,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1901,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1901,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20585
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

_source line 9 · 2026-05-12T00:56:25.398Z_

I'll conduct an independent adversarial review of this Round 4 submission. Let me start by verifying key claims and searching for competing work the generator may have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1f5c979-9aee-404a-b5ee-ae59f5a01621",
  "isSidechain": false,
  "requestId": "req_011CawmJczH57PSbp4Vbpaqk",
  "type": "assistant",
  "uuid": "580a7c46-899d-4302-8b43-92c7ba9df6d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKLyqh5pWMPZdPTsQhfpDG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20585,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1901,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1901,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20585
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

_source line 10 · 2026-05-12T00:56:35.053Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FcXqrLRoB5kTBywj63Dz4W`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify key references exist",
  "prompt": "I need you to verify that the following papers actually exist and that the claims about them are accurate. For each paper, do a WebSearch to confirm its existence, venue, and key findings. Report back with verification status for each.\n\n1. AlphaCodium (arXiv 2401.08500) - claimed: training-free multi-stage flow, CodeContests pass@5 from 19% to 44%\n2. S* (arXiv 2502.14382) - claimed: EMNLP 2025 Findings, 3B model outperforms GPT-4o-mini on LiveCodeBench\n3. BACE (arXiv 2603.28653) - claimed: GECCO 2026, Bayesian anchored co-evolution\n4. CodeSpecBench (arXiv 2604.12268) - claimed: 20.2% repo-level spec generation success\n5. SSDE (arXiv 2605.02455) - claimed: FSE Companion 2026, Gherkin specifications for repo-level generation\n6. Self-Spec (Agents4Science 2025) - claimed: model-authored specs improve HumanEval by +2-5pp\n7. \"Revisit Self-Debugging with Self-Generated Tests\" (arXiv 2501.12793) - claimed: ACL 2025 Long\n8. Think Anywhere (arXiv 2603.29957) - claimed: on-demand reasoning during code generation via RL\n\nFor each, search with the arXiv ID or paper title. Report: exists (yes/no), venue correct (yes/no/uncertain), key claim accurate (yes/no/uncertain). Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "580a7c46-899d-4302-8b43-92c7ba9df6d0",
  "isSidechain": false,
  "requestId": "req_011CawmJczH57PSbp4Vbpaqk",
  "type": "assistant",
  "uuid": "3ccf0ff2-3651-47aa-87cf-ce77562ea4cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKLyqh5pWMPZdPTsQhfpDG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20585,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1901,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1901,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20585
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

_source line 11 · 2026-05-12T00:56:46.481Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GPfdGtgFrbeDUa5wjnQFWL`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for competing/missing work",
  "prompt": "I'm reviewing a paper idea called \"ExeSpec\" that proposes using execution-grounded behavioral specifications (preconditions, postconditions, invariants, type constraints) as structured intermediate reasoning for LLM code tasks, WITHOUT training. It positions itself against test-based methods like AlphaCodium, CodeT, Self-Debugging, and S*.\n\nI need to find competing work the authors may have missed. Please do multiple WebSearches with different keyword combinations:\n\n1. Search: \"specification guided code generation LLM 2025 2026\" \n2. Search: \"precondition postcondition LLM code repair 2025 2026\"\n3. Search: \"formal specification inference code LLM\"\n4. Search: \"contract-based code generation language model\"\n5. Search: \"invariant guided program repair LLM\"\n6. Search: \"property-based testing LLM code generation\"\n7. Search: \"execution feedback code refinement inference time 2025 2026\"\n8. Search: \"structured reasoning code LLM beyond test cases\"\n9. Search: site:arxiv.org \"behavioral specification\" code LLM 2025 2026\n10. Search: \"test-free code verification LLM\"\n\nFor each search, report the most relevant papers found that are NOT in this list of already-cited works:\n- AlphaCodium, CodeT, Self-Debugging, S*, BACE, Self-Spec, EG-CFG, Think Like You Execute, Think Anywhere, SpecRover, CURE, CodeSpecBench, VibeRepair, SSDE, SCoT, RLEF, Revisit Self-Debugging\n\nFocus on papers from 2024-2026 that could be direct competitors or highly related. For any promising hit, try to fetch the abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ccf0ff2-3651-47aa-87cf-ce77562ea4cd",
  "isSidechain": false,
  "requestId": "req_011CawmJczH57PSbp4Vbpaqk",
  "type": "assistant",
  "uuid": "ced62a1d-723d-456c-8620-4a2122d7986a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKLyqh5pWMPZdPTsQhfpDG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20585,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1901,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1901,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20585
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

_source line 12 · 2026-05-12T00:56:52.975Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01VTchuuXeW4xn6CdeQSkXrB`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "SOTA verification on benchmarks",
  "prompt": "I need to verify the current state-of-the-art on several code benchmarks to assess whether a proposed method has realistic positioning. Please search for the following:\n\n1. Search: \"SWE-bench Verified leaderboard 2026 state of the art\" - What are the current top scores on SWE-bench Verified? What methods achieve them?\n2. Search: \"CodeContests benchmark SOTA 2025 2026\" - What are the best results on CodeContests? Is AlphaCodium's 44% pass@5 still competitive?\n3. Search: \"DebugBench LLM debugging benchmark results 2025 2026\" - What are the current best results?\n4. Search: \"CrossCodeEval benchmark results 2025 2026\" - Current SOTA?\n5. Search: site:paperswithcode.com \"SWE-bench\" - Check leaderboard\n6. Search: \"Qwen2.5-Coder-32B performance benchmarks\" - What does this model achieve on standard code benchmarks?\n7. Search: \"training-free code generation improvement 2025 2026 inference time\" - What training-free methods currently achieve the best results?\n\nReport what you find for each search. I want to know if the proposed baselines (Qwen2.5-Coder-7B/32B) and the claimed gaps are realistic."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ced62a1d-723d-456c-8620-4a2122d7986a",
  "isSidechain": false,
  "requestId": "req_011CawmJczH57PSbp4Vbpaqk",
  "type": "assistant",
  "uuid": "1de02ba5-1601-42e5-ba1d-7381a331ed7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YKLyqh5pWMPZdPTsQhfpDG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 20585,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1901,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20585,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1901,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20585
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

_source line 13 · 2026-05-12T00:59:43.503Z_

<details><summary>↩ Tool result · `toolu_01FcXqrLRoB5kTBywj63Dz4W`</summary>

```text
I now have all the information needed. Here is the comprehensive verification report:

---

## Paper Verification Report

### 1. AlphaCodium (arXiv 2401.08500)

- **Exists:** YES
- **Title:** "Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering"
- **Venue correct:** N/A (no specific venue was claimed beyond arXiv; it is an arXiv preprint)
- **Key claim accurate:** YES. The paper confirms it is a training-free, multi-stage iterative flow. GPT-4 accuracy (pass@5) on CodeContests increased from 19% (single direct prompt) to 44% with the AlphaCodium flow. All claims match.

---

### 2. S* (arXiv 2502.14382)

- **Exists:** YES
- **Title:** "S*: Test Time Scaling for Code Generation"
- **Venue correct:** YES. Confirmed published at EMNLP 2025 Findings via ACL Anthology entry `2025.findings-emnlp.865`.
- **Key claim accurate:** YES. The paper explicitly states that S* enables a 3B model to outperform GPT-4o-mini on LiveCodeBench. All claims match.

---

### 3. BACE (arXiv 2603.28653)

- **Exists:** YES
- **Title:** "BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations"
- **Venue correct:** YES. Confirmed accepted at GECCO 2026 (Genetic and Evolutionary Computation Conference, July 13-17, 2026, San Jose, Costa Rica).
- **Key claim accurate:** YES. The paper describes Bayesian Anchored Co-Evolution of code and test populations, exactly as claimed.

---

### 4. CodeSpecBench (arXiv 2604.12268)

- **Exists:** YES
- **Title:** "CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation"
- **Venue correct:** No specific peer-reviewed venue was claimed; it is an arXiv preprint (submitted April 2026).
- **Key claim accurate:** YES. The paper confirms that on repo-level specification generation tasks, the best model attains only a 20.2% pass rate. Claim matches exactly.

---

### 5. SSDE (arXiv 2605.02455)

- **Exists:** YES
- **Title:** "LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering"
- **Venue correct:** YES. The paper is identified as part of the FSE Companion '26 (34th ACM Joint European Software Engineering Conference).
- **Key claim accurate:** YES. The paper uses Gherkin specifications and domain models as inputs for repo-level generation, exactly as claimed.

---

### 6. Self-Spec (Agents4Science 2025)

- **Exists:** YES
- **Title:** "Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation"
- **Venue correct:** YES. Confirmed published at Agents4Science 2025, verified via OpenReview and the conference accepted papers page at `agents4science.stanford.edu`.
- **Key claim accurate:** YES, with nuance. GPT-4o improved from 87% to 92% (+5pp) and Claude 3.7 from 92% to 94% (+2pp) on HumanEval, consistent with the "+2-5pp" claim. However, Claude 3.5 showed a slight decrease (-1pp), so the improvement is model-dependent and not universal.

---

### 7. "Revisit Self-Debugging with Self-Generated Tests" (arXiv 2501.12793)

- **Exists:** YES
- **Title:** "Revisit Self-Debugging with Self-Generated Tests for Code Generation"
- **Venue correct:** YES. Confirmed published at ACL 2025 as a long paper via ACL Anthology entry `2025.acl-long.881` (pages 18003-18023, Vienna, Austria).
- **Key claim accurate:** YES. It is an ACL 2025 Long paper as claimed.

---

### 8. Think Anywhere (arXiv 2603.29957)

- **Exists:** YES
- **Title:** "Think Anywhere in Code Generation"
- **Venue correct:** No specific peer-reviewed venue was claimed; it is an arXiv preprint (submitted March 31, 2026).
- **Key claim accurate:** YES. The paper proposes on-demand reasoning during code generation, using cold-start training followed by outcome-based RL (reinforcement learning) to enable the model to autonomously decide when and where to invoke reasoning. All claims match.

---

## Summary

| # | Paper | Exists | Venue | Key Claim |
|---|-------|--------|-------|-----------|
| 1 | AlphaCodium | YES | N/A (arXiv only) | ACCURATE |
| 2 | S* | YES | YES (EMNLP 2025 Findings) | ACCURATE |
| 3 | BACE | YES | YES (GECCO 2026) | ACCURATE |
| 4 | CodeSpecBench | YES | N/A (arXiv only) | ACCURATE |
| 5 | SSDE | YES | YES (FSE Companion 2026) | ACCURATE |
| 6 | Self-Spec | YES | YES (Agents4Science 2025) | ACCURATE (model-dependent) |
| 7 | Revisit Self-Debugging | YES | YES (ACL 2025 Long) | ACCURATE |
| 8 | Think Anywhere | YES | N/A (arXiv only) | ACCURATE |

All 8 papers are confirmed to exist. All venue claims that were made are verified as correct. All key technical claims are accurate based on the papers' own reported results.

Sources:
- [AlphaCodium (2401.08500)](https://arxiv.org/abs/2401.08500)
- [S* (2502.14382)](https://arxiv.org/abs/2502.14382)
- [S* at EMNLP 2025 Findings](https://aclanthology.org/2025.findings-emnlp.865/)
- [BACE (2603.28653)](https://arxiv.org/abs/2603.28653)
- [CodeSpecBench (2604.12268)](https://arxiv.org/abs/2604.12268)
- [SSDE (2605.02455)](https://arxiv.org/abs/2605.02455)
- [Self-Spec on OpenReview](https://openreview.net/forum?id=6pr7BUGkLp)
- [Agents4Science 2025 Accepted Papers](https://agents4science.stanford.edu/accepted-papers.html)
- [Revisit Self-Debugging at ACL 2025](https://aclanthology.org/2025.acl-long.881/)
- [Think Anywhere (2603.29957)](https://arxiv.org/abs/2603.29957)
- [AlphaCodium GitHub](https://github.com/Codium-ai/AlphaCodium)
- [NovaSky S* Blog](https://novasky-ai.github.io/posts/S*/)

agentId: ae324a4700303ae6d (use SendMessage with to: 'ae324a4700303ae6d' to continue this agent)
&lt;usage>total_tokens: 24704
tool_uses: 14
duration_ms: 188443&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ccf0ff2-3651-47aa-87cf-ce77562ea4cd",
  "isSidechain": false,
  "promptId": "9e08ddf0-33d2-4d92-a77f-55540a5b8b2a",
  "type": "user",
  "uuid": "430de909-1e01-496e-9696-b14043027156",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to verify that the following papers actually exist and that the claims about them are accurate. For each paper, do a WebSearch to confirm its existence, venue, and key findings. Report back with verification status for each.\n\n1. AlphaCodium (arXiv 2401.08500) - claimed: training-free multi-stage flow, CodeContests pass@5 from 19% to 44%\n2. S* (arXiv 2502.14382) - claimed: EMNLP 2025 Findings, 3B model outperforms GPT-4o-mini on LiveCodeBench\n3. BACE (arXiv 2603.28653) - claimed: GECCO 2026, Bayesian anchored co-evolution\n4. CodeSpecBench (arXiv 2604.12268) - claimed: 20.2% repo-level spec generation success\n5. SSDE (arXiv 2605.02455) - claimed: FSE Companion 2026, Gherkin specifications for repo-level generation\n6. Self-Spec (Agents4Science 2025) - claimed: model-authored specs improve HumanEval by +2-5pp\n7. \"Revisit Self-Debugging with Self-Generated Tests\" (arXiv 2501.12793) - claimed: ACL 2025 Long\n8. Think Anywhere (arXiv 2603.29957) - claimed: on-demand reasoning during code generation via RL\n\nFor each, search with the arXiv ID or paper title. Report: exists (yes/no), venue correct (yes/no/uncertain), key claim accurate (yes/no/uncertain). Be thorough.",
    "agentId": "ae324a4700303ae6d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here is the comprehensive verification report:\n\n---\n\n## Paper Verification Report\n\n### 1. AlphaCodium (arXiv 2401.08500)\n\n- **Exists:** YES\n- **Title:** \"Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering\"\n- **Venue correct:** N/A (no specific venue was claimed beyond arXiv; it is an arXiv preprint)\n- **Key claim accurate:** YES. The paper confirms it is a training-free, multi-stage iterative flow. GPT-4 accuracy (pass@5) on CodeContests increased from 19% (single direct prompt) to 44% with the AlphaCodium flow. All claims match.\n\n---\n\n### 2. S* (arXiv 2502.14382)\n\n- **Exists:** YES\n- **Title:** \"S*: Test Time Scaling for Code Generation\"\n- **Venue correct:** YES. Confirmed published at EMNLP 2025 Findings via ACL Anthology entry `2025.findings-emnlp.865`.\n- **Key claim accurate:** YES. The paper explicitly states that S* enables a 3B model to outperform GPT-4o-mini on LiveCodeBench. All claims match.\n\n---\n\n### 3. BACE (arXiv 2603.28653)\n\n- **Exists:** YES\n- **Title:** \"BACE: LLM-based Code Generation through Bayesian Anchored Co-Evolution of Code and Test Populations\"\n- **Venue correct:** YES. Confirmed accepted at GECCO 2026 (Genetic and Evolutionary Computation Conference, July 13-17, 2026, San Jose, Costa Rica).\n- **Key claim accurate:** YES. The paper describes Bayesian Anchored Co-Evolution of code and test populations, exactly as claimed.\n\n---\n\n### 4. CodeSpecBench (arXiv 2604.12268)\n\n- **Exists:** YES\n- **Title:** \"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation\"\n- **Venue correct:** No specific peer-reviewed venue was claimed; it is an arXiv preprint (submitted April 2026).\n- **Key claim accurate:** YES. The paper confirms that on repo-level specification generation tasks, the best model attains only a 20.2% pass rate. Claim matches exactly.\n\n---\n\n### 5. SSDE (arXiv 2605.02455)\n\n- **Exists:** YES\n- **Title:** \"LLM-Assisted Repository-Level Generation with Structured Spec-Driven Engineering\"\n- **Venue correct:** YES. The paper is identified as part of the FSE Companion '26 (34th ACM Joint European Software Engineering Conference).\n- **Key claim accurate:** YES. The paper uses Gherkin specifications and domain models as inputs for repo-level generation, exactly as claimed.\n\n---\n\n### 6. Self-Spec (Agents4Science 2025)\n\n- **Exists:** YES\n- **Title:** \"Self-Spec: Model-Authored Specifications for Reliable LLM Code Generation\"\n- **Venue correct:** YES. Confirmed published at Agents4Science 2025, verified via OpenReview and the conference accepted papers page at `agents4science.stanford.edu`.\n- **Key claim accurate:** YES, with nuance. GPT-4o improved from 87% to 92% (+5pp) and Claude 3.7 from 92% to 94% (+2pp) on HumanEval, consistent with the \"+2-5pp\" claim. However, Claude 3.5 showed a slight decrease (-1pp), so the improvement is model-dependent and not universal.\n\n---\n\n### 7. \"Revisit Self-Debugging with Self-Generated Tests\" (arXiv 2501.12793)\n\n- **Exists:** YES\n- **Title:** \"Revisit Self-Debugging with Self-Generated Tests for Code Generation\"\n- **Venue correct:** YES. Confirmed published at ACL 2025 as a long paper via ACL Anthology entry `2025.acl-long.881` (pages 18003-18023, Vienna, Austria).\n- **Key claim accurate:** YES. It is an ACL 2025 Long paper as claimed.\n\n---\n\n### 8. Think Anywhere (arXiv 2603.29957)\n\n- **Exists:** YES\n- **Title:** \"Think Anywhere in Code Generation\"\n- **Venue correct:** No specific peer-reviewed venue was claimed; it is an arXiv preprint (submitted March 31, 2026).\n- **Key claim accurate:** YES. The paper proposes on-demand reasoning during code generation, using cold-start training followed by outcome-based RL (reinforcement learning) to enable the model to autonomously decide when and where to invoke reasoning. All claims match.\n\n---\n\n## Summary\n\n| # | Paper | Exists | Venue | Key Claim |\n|---|-------|--------|-------|-----------|\n| 1 | AlphaCodium | YES | N/A (arXiv only) | ACCURATE |\n| 2 | S* | YES | YES (EMNLP 2025 Findings) | ACCURATE |\n| 3 | BACE | YES | YES (GECCO 2026) | ACCURATE |\n| 4 | CodeSpecBench | YES | N/A (arXiv only) | ACCURATE |\n| 5 | SSDE | YES | YES (FSE Companion 2026) | ACCURATE |\n| 6 | Self-Spec | YES | YES (Agents4Science 2025) | ACCURATE (model-dependent) |\n| 7 | Revisit Self-Debugging | YES | YES (ACL 2025 Long) | ACCURATE |\n| 8 | Think Anywhere | YES | N/A (arXiv only) | ACCURATE |\n\nAll 8 papers are confirmed to exist. All venue claims that were made are verified as correct. All key technical claims are accurate based on the papers' own reported results.\n\nSources:\n- [AlphaCodium (2401.08500)](https://arxiv.org/abs/2401.08500)\n- [S* (2502.14382)](https://arxiv.org/abs/2502.14382)\n- [S* at EMNLP 2025 Findings](https://aclanthology.org/2025.findings-emnlp.865/)\n- [BACE (2603.28653)](https://arxiv.org/abs/2603.28653)\n- [CodeSpecBench (2604.12268)](https://arxiv.org/abs/2604.12268)\n- [SSDE (2605.02455)](https://arxiv.org/abs/2605.02455)\n- [Self-Spec on OpenReview](https://openreview.net/forum?id=6pr7BUGkLp)\n- [Agents4Science 2025 Accepted Papers](https://agents4science.stanford.edu/accepted-papers.html)\n- [Revisit Self-Debugging at ACL 2025](https://aclanthology.org/2025.acl-long.881/)\n- [Think Anywhere (2603.29957)](https://arxiv.org/abs/2603.29957)\n- [AlphaCodium GitHub](https://github.com/Codium-ai/AlphaCodium)\n- [NovaSky S* Blog](https://novasky-ai.github.io/posts/S*/)"
      }
    ],
    "totalDurationMs": 188443,
    "totalTokens": 24704,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1001,
      "cache_read_input_tokens": 21892,
      "output_tokens": 1810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1001
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1810,
          "cache_read_input_tokens": 21892,
          "cache_creation_input_tokens": 1001,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1001,
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
  "sourceToolAssistantUUID": "3ccf0ff2-3651-47aa-87cf-ce77562ea4cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T01:00:09.823Z_

<details><summary>↩ Tool result · `toolu_01GPfdGtgFrbeDUa5wjnQFWL`</summary>

```text
Here is my comprehensive report of potentially missed competing work, organized by relevance tier.

---

## TIER 1 -- DIRECT COMPETITORS (Highest relevance to ExeSpec)

These papers operate in nearly the same conceptual space: using specifications (preconditions, postconditions, contracts, properties) as structured intermediates for LLM code tasks, often without training.

### 1. Property-Generated Solver (PGS)
- **Paper:** "Use Property-Based Testing to Bridge LLM Code Generation and Validation" (arXiv:2506.18315)
- **Authors:** Lehan He, Zeren Chen, Zhe Zhang, Xiang Gao, Lu Sheng
- **Why it matters:** PGS uses two LLM agents -- a Generator and a Tester -- where the Tester generates high-level program *properties* (not just test cases) and provides the simplest failing counterexample as feedback. It achieves 23-37% relative pass@1 gains over TDD methods. This is extremely close to ExeSpec's idea of using behavioral specifications instead of tests, though PGS frames them as PBT properties rather than preconditions/postconditions.
- [arXiv link](https://arxiv.org/abs/2506.18315)

### 2. NL2Contract / "Beyond Postconditions"
- **Paper:** "Beyond Postconditions: Can Large Language Models infer Formal Contracts for Automatic Software Verification?" (arXiv:2510.12702)
- **Authors:** Cedric Richter, Heike Wehrheim
- **Why it matters:** Directly studies LLMs generating complete functional contracts (both preconditions AND postconditions) from natural language. Shows that LLM-inferred contracts reduce false alarms vs. postconditions alone and can discriminate buggy from correct code. The framing of "contracts as verification artifacts generated by LLMs" is very close to ExeSpec's behavioral specifications.
- [arXiv link](https://arxiv.org/abs/2510.12702)

### 3. ContractEval / PACT
- **Paper:** "Do Large Language Models Respect Contracts? Evaluating and Enforcing Contract-Adherence in Code Generation" (arXiv:2510.12047)
- **Authors:** Soohan Lim, Joonghyuk Hahn, Hyunwoo Park, Sang-Ki Ko, Yo-Sub Han
- **Why it matters:** Introduces ContractEval, a benchmark of 364 tasks testing whether LLM-generated code satisfies precondition/postcondition contracts. Key finding: models achieve 75-82% pass@1 but 0% contract satisfaction under standard prompting; even with explicit contract prompts, only 23-41% satisfaction. Establishes contract enforcement as "a crucial and previously overlooked axis of code generation quality." Directly validates the problem ExeSpec addresses.
- [arXiv link](https://arxiv.org/abs/2510.12047)

### 4. "Preconditions and Postconditions as Design Constraints for LLM Code Generation"
- **Published:** IEEE Access, 2024/2025
- **Why it matters:** Directly studies how explicit preconditions and postconditions in the Design-by-Contract paradigm affect class-level LLM code generation. Finds that incorporating explicit design constraints during prompting significantly boosts initial generation accuracy. This is essentially a controlled experiment validating ExeSpec's core premise.
- [IEEE Xplore](https://ieeexplore.ieee.org/document/11218044/)

### 5. ReDeFo
- **Paper:** "Requirements Development and Formalization for Reliable Code Generation: A Multi-Agent Vision" (ASE 2025 NIER)
- **Authors:** Xu Lu, Weisong Sun, Yiran Zhang, Ming Hu, Cong Tian, Zhi Jin, Yang Liu
- **Why it matters:** Multi-agent framework that uses formal specifications to bridge natural language requirements and executable code. Three agents with formal methods knowledge verify correctness and enforce critical properties. Very similar pipeline concept to ExeSpec but uses multi-agent architecture.
- [ASE 2025](https://conf.researchr.org/details/ase-2025/ase-2025-nier-track/30/)

### 6. "From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing"
- **Published:** FSE 2025 (ACM SIGSOFT)
- **Why it matters:** Proposes rethinking LLM code generation validation using property-based testing rather than example-based tests. Directly challenges the test-based paradigm that ExeSpec also critiques.
- [ACM DL](https://dl.acm.org/doi/10.1145/3696630.3728702)

### 7. Type-Constrained Code Generation
- **Paper:** "Type-Constrained Code Generation with Language Models" (arXiv:2504.09246)
- **Authors:** Niels Mundler, Jingxuan He, Hao Wang, Koushik Sen, Dawn Song, Martin Vechev
- **Why it matters:** Enforces type constraints during LLM decoding via novel prefix automata. Reduces compilation errors by more than half and improves functional correctness. ExeSpec includes type constraints as one of its specification dimensions -- this paper shows type enforcement alone already helps substantially.
- [arXiv link](https://arxiv.org/abs/2504.09246)

---

## TIER 2 -- STRONGLY RELATED (Complementary or overlapping methods)

### 8. Preguss
- **Paper:** "A Tale of 1001 LoC: Potential Runtime Error-Guided Specification Synthesis for Verifying Large-Scale Programs" (OOPSLA 2026, arXiv:2512.24594)
- **Authors:** Zhongyi Wang et al.
- **Why it matters:** Uses LLMs to synthesize interprocedural specifications (pre/postconditions) guided by potential runtime errors. Achieves 80-89% reduction in human verification effort on programs >1000 LoC. Relevant as it shows LLM-generated specifications being used for practical verification at scale.
- [arXiv link](https://arxiv.org/abs/2512.24594)

### 9. NeuroInv
- **Paper:** "A Neurosymbolic Approach to Loop Invariant Generation via Weakest Precondition Reasoning" (arXiv:2512.15816)
- **Authors:** Daragh King, Vasileios Koutavas, Laura Kovacs
- **Why it matters:** Neurosymbolic system combining LLMs with Hoare logic for invariant generation via weakest precondition backward chaining, plus symbolic repair using counterexamples. 99.5% success rate on 150 Java programs. Relevant because ExeSpec uses invariants as one specification type.
- [arXiv link](https://arxiv.org/abs/2512.15816)

### 10. Specification-Guided Repair of Dafny Programs
- **Paper:** "Specification-Guided Repair of Arithmetic Errors in Dafny Programs using LLMs" (arXiv:2507.03659)
- **Authors:** Valentina Wu, Alexandra Mendes, Alexandre Abreu
- **Why it matters:** Uses formal specifications (not tests) as oracles for fault localization and repair via Hoare logic. 89.7% fault localization, 74% repair rate. Shows specifications guiding LLM repair without test cases -- exactly ExeSpec's use case for code repair.
- [arXiv link](https://arxiv.org/abs/2507.03659)

### 11. FuzzFeed
- **Paper:** "LLMs and Fuzzing in Tandem: A New Approach to Automatically Generating Weakest Preconditions" (arXiv:2507.05272)
- **Authors:** Daragh King, Vasileios Koutavas, Laura Kovacs
- **Why it matters:** Combines LLMs with fuzz testing to generate weakest preconditions, using execution feedback to guide the LLM. Relevant to ExeSpec's precondition generation component.
- [arXiv link](https://arxiv.org/abs/2507.05272)

### 12. ORPS (Outcome-Refining Process Supervision)
- **Paper:** "Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation" (arXiv:2412.15118)
- **Authors:** Zhuohao Yu et al.
- **Why it matters:** Uses execution-based verification with tree-structured exploration during inference. 26.9% higher correctness, 42.2% improved efficiency. Combines execution signals with structured reasoning -- a different take on execution-grounded intermediate reasoning.
- [arXiv link](https://arxiv.org/abs/2412.15118)

### 13. Abstractions-of-Thought (AoT)
- **Paper:** "Abstractions-of-Thought: Intermediate Representations for LLM Reasoning in Hardware Design" (arXiv:2505.15873)
- **Authors:** Matthew DeLorenzo et al.
- **Why it matters:** Training-free prompting framework that uses a structured intermediate representation separating functional decomposition from syntax. Though for hardware (Verilog), the concept of using structured IRs as reasoning scaffolds at inference time is methodologically parallel to ExeSpec. Reduces tokens 1.8-5.2x vs. Tree-of-Thought.
- [arXiv link](https://arxiv.org/abs/2505.15873)

### 14. StoryCoder
- **Paper:** "StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation" (arXiv:2604.14631)
- **Authors:** Geonhui Jang, Dongyoon Han, YoungJoon Yoo
- **Why it matters:** Converts code problems into structured narratives including constraints and invariants. 18.7% improvement in zero-shot pass@10. Relevant as another training-free structured intermediate reasoning approach, though it uses narratives rather than formal specifications.
- [arXiv link](https://arxiv.org/abs/2604.14631)

### 15. CRANE
- **Paper:** "Reasoning with Constrained LLM Generation" (arXiv:2502.09061)
- **Why it matters:** Alternates between unconstrained generation for reasoning and constrained generation for correct outputs. Theoretically shows that constrained decoding loses expressivity because the grammar is too restrictive for intermediate reasoning steps. Relevant to ExeSpec's argument about structured intermediate reasoning.
- [arXiv link](https://arxiv.org/abs/2502.09061)

---

## TIER 3 -- BENCHMARKS AND EVALUATION FRAMEWORKS

### 16. VERINA
- **Paper:** "VERINA: Benchmarking Verifiable Code Generation" (arXiv:2505.23135)
- **Authors:** Zhe Ye et al.
- **Why it matters:** 189-task benchmark for generating code + specifications + proofs in Lean. Best model (o3) achieves only 4.9% proof success. Could serve as an evaluation benchmark for ExeSpec-style approaches.
- [arXiv link](https://arxiv.org/abs/2505.23135)

### 17. CLEVER
- **Paper:** "CLEVER: A Curated Benchmark for Formally Verified Code Generation" (arXiv:2505.13938)
- **Authors:** Amitayush Thakur et al.
- **Why it matters:** 161 problems requiring specification generation + implementation + proof in Lean. No test-case supervision allowed. Relevant as a test-free evaluation framework.
- [arXiv link](https://arxiv.org/abs/2505.13938)

### 18. "Beyond Code Generation: Assessing Code LLM Maturity with Postconditions"
- **Paper:** arXiv:2407.14118
- **Authors:** Fusen He, Juan Zhai, Minxue Pan
- **Why it matters:** Proposes postcondition generation as a maturity metric for code LLMs, arguing it captures semantic understanding better than code generation benchmarks.
- [arXiv link](https://arxiv.org/abs/2407.14118)

### 19. FormalSpecCpp
- **Paper:** "FormalSpecCpp: A Dataset of C++ Formal Specifications created using LLMs" (arXiv:2502.15217, MSR 2025)
- **Authors:** Madhurima Chakraborty, Peter Pirkelbauer, Qing Yi
- **Why it matters:** First comprehensive C++ dataset with preconditions and postconditions, created using LLMs. Benchmarking resource for specification inference.
- [arXiv link](https://arxiv.org/abs/2502.15217)

### 20. Astrogator
- **Paper:** "Towards Formal Verification of LLM-Generated Code from Natural Language Prompts" (arXiv:2507.13290)
- **Authors:** Aaron Councilman et al.
- **Why it matters:** Uses a Formal Query Language to capture user intent and verify LLM code. 83% correct code validation, 92% flawed code detection. Represents the "formal spec as verification oracle" approach.
- [arXiv link](https://arxiv.org/abs/2507.13290)

---

## TIER 4 -- PERIPHERALLY RELEVANT

### 21. Metamorphic Prompt Testing (arXiv:2406.06864)
- Test-free validation via prompt paraphrasing and cross-validation. 75% error detection rate.

### 22. REA-Coder (arXiv:2604.16198)
- Requirement alignment before code generation. 7-30% improvement.

### 23. SAGA / TCGBench (arXiv:2507.06920)
- Better test generation via human + LLM collaboration. Relevant to ExeSpec's critique of test-based methods.

### 24. Quokka (arXiv:2509.21629)
- LLM-based invariant synthesis for program verification with direct validation framework.

### 25. Correctness-Guaranteed Code Generation via Constrained Decoding (arXiv:2508.15866)
- Context-sensitive constrained decoding enforcing type and scoping rules during generation.

---

## SUMMARY OF HIGHEST-PRIORITY GAPS

The papers ExeSpec most urgently needs to cite or differentiate against are:

1. **PGS** (arXiv:2506.18315) -- Uses properties (not tests) as feedback; most direct methodological competitor
2. **NL2Contract** (arXiv:2510.12702) -- LLMs generating full contracts (pre+post); validates the core idea
3. **ContractEval** (arXiv:2510.12047) -- Benchmarks contract satisfaction; shows the problem is real
4. **"Preconditions and Postconditions as Design Constraints"** (IEEE) -- Controlled study of exactly ExeSpec's premise
5. **ReDeFo** (ASE 2025) -- Multi-agent formal specification pipeline; architectural competitor
6. **Type-Constrained Code Generation** (arXiv:2504.09246) -- Proves type constraints alone help substantially
7. **Specification-Guided Repair of Dafny** (arXiv:2507.03659) -- Spec-guided repair without tests

Sources:
- [PGS - Property-Based Testing for LLM Code](https://arxiv.org/abs/2506.18315)
- [NL2Contract - Beyond Postconditions](https://arxiv.org/abs/2510.12702)
- [ContractEval](https://arxiv.org/abs/2510.12047)
- [Preconditions/Postconditions as Design Constraints](https://ieeexplore.ieee.org/document/11218044/)
- [ReDeFo - ASE 2025](https://conf.researchr.org/details/ase-2025/ase-2025-nier-track/30/)
- [Type-Constrained Code Generation](https://arxiv.org/abs/2504.09246)
- [Spec-Guided Repair of Dafny Programs](https://arxiv.org/abs/2507.03659)
- [Preguss - OOPSLA 2026](https://arxiv.org/abs/2512.24594)
- [NeuroInv](https://arxiv.org/abs/2512.15816)
- [FuzzFeed - Weakest Preconditions](https://arxiv.org/abs/2507.05272)
- [ORPS](https://arxiv.org/abs/2412.15118)
- [Abstractions-of-Thought](https://arxiv.org/abs/2505.15873)
- [StoryCoder](https://arxiv.org/abs/2604.14631)
- [CRANE](https://arxiv.org/abs/2502.09061)
- [VERINA](https://arxiv.org/abs/2505.23135)
- [CLEVER](https://arxiv.org/abs/2505.13938)
- [LLM Maturity with Postconditions](https://arxiv.org/abs/2407.14118)
- [FormalSpecCpp](https://arxiv.org/abs/2502.15217)
- [Astrogator](https://arxiv.org/abs/2507.13290)
- [Metamorphic Prompt Testing](https://arxiv.org/abs/2406.06864)
- [REA-Coder](https://arxiv.org/abs/2604.16198)
- [SAGA / TCGBench](https://arxiv.org/abs/2507.06920)
- [Quokka](https://arxiv.org/abs/2509.21629)
- [Constrained Decoding for Correctness](https://arxiv.org/abs/2508.15866)
- [Specification-Driven Code Generation Study - SANER 2026](https://arxiv.org/html/2601.03878v1)
- [From Prompts to Properties - FSE 2025](https://dl.acm.org/doi/10.1145/3696630.3728702)

agentId: ab768184e99694848 (use SendMessage with to: 'ab768184e99694848' to continue this agent)
&lt;usage>total_tokens: 40864
tool_uses: 46
duration_ms: 203337&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ced62a1d-723d-456c-8620-4a2122d7986a",
  "isSidechain": false,
  "promptId": "9e08ddf0-33d2-4d92-a77f-55540a5b8b2a",
  "type": "user",
  "uuid": "7fe6204f-e041-4c85-8ce3-26e4a2cdae89",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper idea called \"ExeSpec\" that proposes using execution-grounded behavioral specifications (preconditions, postconditions, invariants, type constraints) as structured intermediate reasoning for LLM code tasks, WITHOUT training. It positions itself against test-based methods like AlphaCodium, CodeT, Self-Debugging, and S*.\n\nI need to find competing work the authors may have missed. Please do multiple WebSearches with different keyword combinations:\n\n1. Search: \"specification guided code generation LLM 2025 2026\" \n2. Search: \"precondition postcondition LLM code repair 2025 2026\"\n3. Search: \"formal specification inference code LLM\"\n4. Search: \"contract-based code generation language model\"\n5. Search: \"invariant guided program repair LLM\"\n6. Search: \"property-based testing LLM code generation\"\n7. Search: \"execution feedback code refinement inference time 2025 2026\"\n8. Search: \"structured reasoning code LLM beyond test cases\"\n9. Search: site:arxiv.org \"behavioral specification\" code LLM 2025 2026\n10. Search: \"test-free code verification LLM\"\n\nFor each search, report the most relevant papers found that are NOT in this list of already-cited works:\n- AlphaCodium, CodeT, Self-Debugging, S*, BACE, Self-Spec, EG-CFG, Think Like You Execute, Think Anywhere, SpecRover, CURE, CodeSpecBench, VibeRepair, SSDE, SCoT, RLEF, Revisit Self-Debugging\n\nFocus on papers from 2024-2026 that could be direct competitors or highly related. For any promising hit, try to fetch the abstract.",
    "agentId": "ab768184e99694848",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my comprehensive report of potentially missed competing work, organized by relevance tier.\n\n---\n\n## TIER 1 -- DIRECT COMPETITORS (Highest relevance to ExeSpec)\n\nThese papers operate in nearly the same conceptual space: using specifications (preconditions, postconditions, contracts, properties) as structured intermediates for LLM code tasks, often without training.\n\n### 1. Property-Generated Solver (PGS)\n- **Paper:** \"Use Property-Based Testing to Bridge LLM Code Generation and Validation\" (arXiv:2506.18315)\n- **Authors:** Lehan He, Zeren Chen, Zhe Zhang, Xiang Gao, Lu Sheng\n- **Why it matters:** PGS uses two LLM agents -- a Generator and a Tester -- where the Tester generates high-level program *properties* (not just test cases) and provides the simplest failing counterexample as feedback. It achieves 23-37% relative pass@1 gains over TDD methods. This is extremely close to ExeSpec's idea of using behavioral specifications instead of tests, though PGS frames them as PBT properties rather than preconditions/postconditions.\n- [arXiv link](https://arxiv.org/abs/2506.18315)\n\n### 2. NL2Contract / \"Beyond Postconditions\"\n- **Paper:** \"Beyond Postconditions: Can Large Language Models infer Formal Contracts for Automatic Software Verification?\" (arXiv:2510.12702)\n- **Authors:** Cedric Richter, Heike Wehrheim\n- **Why it matters:** Directly studies LLMs generating complete functional contracts (both preconditions AND postconditions) from natural language. Shows that LLM-inferred contracts reduce false alarms vs. postconditions alone and can discriminate buggy from correct code. The framing of \"contracts as verification artifacts generated by LLMs\" is very close to ExeSpec's behavioral specifications.\n- [arXiv link](https://arxiv.org/abs/2510.12702)\n\n### 3. ContractEval / PACT\n- **Paper:** \"Do Large Language Models Respect Contracts? Evaluating and Enforcing Contract-Adherence in Code Generation\" (arXiv:2510.12047)\n- **Authors:** Soohan Lim, Joonghyuk Hahn, Hyunwoo Park, Sang-Ki Ko, Yo-Sub Han\n- **Why it matters:** Introduces ContractEval, a benchmark of 364 tasks testing whether LLM-generated code satisfies precondition/postcondition contracts. Key finding: models achieve 75-82% pass@1 but 0% contract satisfaction under standard prompting; even with explicit contract prompts, only 23-41% satisfaction. Establishes contract enforcement as \"a crucial and previously overlooked axis of code generation quality.\" Directly validates the problem ExeSpec addresses.\n- [arXiv link](https://arxiv.org/abs/2510.12047)\n\n### 4. \"Preconditions and Postconditions as Design Constraints for LLM Code Generation\"\n- **Published:** IEEE Access, 2024/2025\n- **Why it matters:** Directly studies how explicit preconditions and postconditions in the Design-by-Contract paradigm affect class-level LLM code generation. Finds that incorporating explicit design constraints during prompting significantly boosts initial generation accuracy. This is essentially a controlled experiment validating ExeSpec's core premise.\n- [IEEE Xplore](https://ieeexplore.ieee.org/document/11218044/)\n\n### 5. ReDeFo\n- **Paper:** \"Requirements Development and Formalization for Reliable Code Generation: A Multi-Agent Vision\" (ASE 2025 NIER)\n- **Authors:** Xu Lu, Weisong Sun, Yiran Zhang, Ming Hu, Cong Tian, Zhi Jin, Yang Liu\n- **Why it matters:** Multi-agent framework that uses formal specifications to bridge natural language requirements and executable code. Three agents with formal methods knowledge verify correctness and enforce critical properties. Very similar pipeline concept to ExeSpec but uses multi-agent architecture.\n- [ASE 2025](https://conf.researchr.org/details/ase-2025/ase-2025-nier-track/30/)\n\n### 6. \"From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing\"\n- **Published:** FSE 2025 (ACM SIGSOFT)\n- **Why it matters:** Proposes rethinking LLM code generation validation using property-based testing rather than example-based tests. Directly challenges the test-based paradigm that ExeSpec also critiques.\n- [ACM DL](https://dl.acm.org/doi/10.1145/3696630.3728702)\n\n### 7. Type-Constrained Code Generation\n- **Paper:** \"Type-Constrained Code Generation with Language Models\" (arXiv:2504.09246)\n- **Authors:** Niels Mundler, Jingxuan He, Hao Wang, Koushik Sen, Dawn Song, Martin Vechev\n- **Why it matters:** Enforces type constraints during LLM decoding via novel prefix automata. Reduces compilation errors by more than half and improves functional correctness. ExeSpec includes type constraints as one of its specification dimensions -- this paper shows type enforcement alone already helps substantially.\n- [arXiv link](https://arxiv.org/abs/2504.09246)\n\n---\n\n## TIER 2 -- STRONGLY RELATED (Complementary or overlapping methods)\n\n### 8. Preguss\n- **Paper:** \"A Tale of 1001 LoC: Potential Runtime Error-Guided Specification Synthesis for Verifying Large-Scale Programs\" (OOPSLA 2026, arXiv:2512.24594)\n- **Authors:** Zhongyi Wang et al.\n- **Why it matters:** Uses LLMs to synthesize interprocedural specifications (pre/postconditions) guided by potential runtime errors. Achieves 80-89% reduction in human verification effort on programs >1000 LoC. Relevant as it shows LLM-generated specifications being used for practical verification at scale.\n- [arXiv link](https://arxiv.org/abs/2512.24594)\n\n### 9. NeuroInv\n- **Paper:** \"A Neurosymbolic Approach to Loop Invariant Generation via Weakest Precondition Reasoning\" (arXiv:2512.15816)\n- **Authors:** Daragh King, Vasileios Koutavas, Laura Kovacs\n- **Why it matters:** Neurosymbolic system combining LLMs with Hoare logic for invariant generation via weakest precondition backward chaining, plus symbolic repair using counterexamples. 99.5% success rate on 150 Java programs. Relevant because ExeSpec uses invariants as one specification type.\n- [arXiv link](https://arxiv.org/abs/2512.15816)\n\n### 10. Specification-Guided Repair of Dafny Programs\n- **Paper:** \"Specification-Guided Repair of Arithmetic Errors in Dafny Programs using LLMs\" (arXiv:2507.03659)\n- **Authors:** Valentina Wu, Alexandra Mendes, Alexandre Abreu\n- **Why it matters:** Uses formal specifications (not tests) as oracles for fault localization and repair via Hoare logic. 89.7% fault localization, 74% repair rate. Shows specifications guiding LLM repair without test cases -- exactly ExeSpec's use case for code repair.\n- [arXiv link](https://arxiv.org/abs/2507.03659)\n\n### 11. FuzzFeed\n- **Paper:** \"LLMs and Fuzzing in Tandem: A New Approach to Automatically Generating Weakest Preconditions\" (arXiv:2507.05272)\n- **Authors:** Daragh King, Vasileios Koutavas, Laura Kovacs\n- **Why it matters:** Combines LLMs with fuzz testing to generate weakest preconditions, using execution feedback to guide the LLM. Relevant to ExeSpec's precondition generation component.\n- [arXiv link](https://arxiv.org/abs/2507.05272)\n\n### 12. ORPS (Outcome-Refining Process Supervision)\n- **Paper:** \"Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation\" (arXiv:2412.15118)\n- **Authors:** Zhuohao Yu et al.\n- **Why it matters:** Uses execution-based verification with tree-structured exploration during inference. 26.9% higher correctness, 42.2% improved efficiency. Combines execution signals with structured reasoning -- a different take on execution-grounded intermediate reasoning.\n- [arXiv link](https://arxiv.org/abs/2412.15118)\n\n### 13. Abstractions-of-Thought (AoT)\n- **Paper:** \"Abstractions-of-Thought: Intermediate Representations for LLM Reasoning in Hardware Design\" (arXiv:2505.15873)\n- **Authors:** Matthew DeLorenzo et al.\n- **Why it matters:** Training-free prompting framework that uses a structured intermediate representation separating functional decomposition from syntax. Though for hardware (Verilog), the concept of using structured IRs as reasoning scaffolds at inference time is methodologically parallel to ExeSpec. Reduces tokens 1.8-5.2x vs. Tree-of-Thought.\n- [arXiv link](https://arxiv.org/abs/2505.15873)\n\n### 14. StoryCoder\n- **Paper:** \"StoryCoder: Narrative Reformulation for Structured Reasoning in LLM Code Generation\" (arXiv:2604.14631)\n- **Authors:** Geonhui Jang, Dongyoon Han, YoungJoon Yoo\n- **Why it matters:** Converts code problems into structured narratives including constraints and invariants. 18.7% improvement in zero-shot pass@10. Relevant as another training-free structured intermediate reasoning approach, though it uses narratives rather than formal specifications.\n- [arXiv link](https://arxiv.org/abs/2604.14631)\n\n### 15. CRANE\n- **Paper:** \"Reasoning with Constrained LLM Generation\" (arXiv:2502.09061)\n- **Why it matters:** Alternates between unconstrained generation for reasoning and constrained generation for correct outputs. Theoretically shows that constrained decoding loses expressivity because the grammar is too restrictive for intermediate reasoning steps. Relevant to ExeSpec's argument about structured intermediate reasoning.\n- [arXiv link](https://arxiv.org/abs/2502.09061)\n\n---\n\n## TIER 3 -- BENCHMARKS AND EVALUATION FRAMEWORKS\n\n### 16. VERINA\n- **Paper:** \"VERINA: Benchmarking Verifiable Code Generation\" (arXiv:2505.23135)\n- **Authors:** Zhe Ye et al.\n- **Why it matters:** 189-task benchmark for generating code + specifications + proofs in Lean. Best model (o3) achieves only 4.9% proof success. Could serve as an evaluation benchmark for ExeSpec-style approaches.\n- [arXiv link](https://arxiv.org/abs/2505.23135)\n\n### 17. CLEVER\n- **Paper:** \"CLEVER: A Curated Benchmark for Formally Verified Code Generation\" (arXiv:2505.13938)\n- **Authors:** Amitayush Thakur et al.\n- **Why it matters:** 161 problems requiring specification generation + implementation + proof in Lean. No test-case supervision allowed. Relevant as a test-free evaluation framework.\n- [arXiv link](https://arxiv.org/abs/2505.13938)\n\n### 18. \"Beyond Code Generation: Assessing Code LLM Maturity with Postconditions\"\n- **Paper:** arXiv:2407.14118\n- **Authors:** Fusen He, Juan Zhai, Minxue Pan\n- **Why it matters:** Proposes postcondition generation as a maturity metric for code LLMs, arguing it captures semantic understanding better than code generation benchmarks.\n- [arXiv link](https://arxiv.org/abs/2407.14118)\n\n### 19. FormalSpecCpp\n- **Paper:** \"FormalSpecCpp: A Dataset of C++ Formal Specifications created using LLMs\" (arXiv:2502.15217, MSR 2025)\n- **Authors:** Madhurima Chakraborty, Peter Pirkelbauer, Qing Yi\n- **Why it matters:** First comprehensive C++ dataset with preconditions and postconditions, created using LLMs. Benchmarking resource for specification inference.\n- [arXiv link](https://arxiv.org/abs/2502.15217)\n\n### 20. Astrogator\n- **Paper:** \"Towards Formal Verification of LLM-Generated Code from Natural Language Prompts\" (arXiv:2507.13290)\n- **Authors:** Aaron Councilman et al.\n- **Why it matters:** Uses a Formal Query Language to capture user intent and verify LLM code. 83% correct code validation, 92% flawed code detection. Represents the \"formal spec as verification oracle\" approach.\n- [arXiv link](https://arxiv.org/abs/2507.13290)\n\n---\n\n## TIER 4 -- PERIPHERALLY RELEVANT\n\n### 21. Metamorphic Prompt Testing (arXiv:2406.06864)\n- Test-free validation via prompt paraphrasing and cross-validation. 75% error detection rate.\n\n### 22. REA-Coder (arXiv:2604.16198)\n- Requirement alignment before code generation. 7-30% improvement.\n\n### 23. SAGA / TCGBench (arXiv:2507.06920)\n- Better test generation via human + LLM collaboration. Relevant to ExeSpec's critique of test-based methods.\n\n### 24. Quokka (arXiv:2509.21629)\n- LLM-based invariant synthesis for program verification with direct validation framework.\n\n### 25. Correctness-Guaranteed Code Generation via Constrained Decoding (arXiv:2508.15866)\n- Context-sensitive constrained decoding enforcing type and scoping rules during generation.\n\n---\n\n## SUMMARY OF HIGHEST-PRIORITY GAPS\n\nThe papers ExeSpec most urgently needs to cite or differentiate against are:\n\n1. **PGS** (arXiv:2506.18315) -- Uses properties (not tests) as feedback; most direct methodological competitor\n2. **NL2Contract** (arXiv:2510.12702) -- LLMs generating full contracts (pre+post); validates the core idea\n3. **ContractEval** (arXiv:2510.12047) -- Benchmarks contract satisfaction; shows the problem is real\n4. **\"Preconditions and Postconditions as Design Constraints\"** (IEEE) -- Controlled study of exactly ExeSpec's premise\n5. **ReDeFo** (ASE 2025) -- Multi-agent formal specification pipeline; architectural competitor\n6. **Type-Constrained Code Generation** (arXiv:2504.09246) -- Proves type constraints alone help substantially\n7. **Specification-Guided Repair of Dafny** (arXiv:2507.03659) -- Spec-guided repair without tests\n\nSources:\n- [PGS - Property-Based Testing for LLM Code](https://arxiv.org/abs/2506.18315)\n- [NL2Contract - Beyond Postconditions](https://arxiv.org/abs/2510.12702)\n- [ContractEval](https://arxiv.org/abs/2510.12047)\n- [Preconditions/Postconditions as Design Constraints](https://ieeexplore.ieee.org/document/11218044/)\n- [ReDeFo - ASE 2025](https://conf.researchr.org/details/ase-2025/ase-2025-nier-track/30/)\n- [Type-Constrained Code Generation](https://arxiv.org/abs/2504.09246)\n- [Spec-Guided Repair of Dafny Programs](https://arxiv.org/abs/2507.03659)\n- [Preguss - OOPSLA 2026](https://arxiv.org/abs/2512.24594)\n- [NeuroInv](https://arxiv.org/abs/2512.15816)\n- [FuzzFeed - Weakest Preconditions](https://arxiv.org/abs/2507.05272)\n- [ORPS](https://arxiv.org/abs/2412.15118)\n- [Abstractions-of-Thought](https://arxiv.org/abs/2505.15873)\n- [StoryCoder](https://arxiv.org/abs/2604.14631)\n- [CRANE](https://arxiv.org/abs/2502.09061)\n- [VERINA](https://arxiv.org/abs/2505.23135)\n- [CLEVER](https://arxiv.org/abs/2505.13938)\n- [LLM Maturity with Postconditions](https://arxiv.org/abs/2407.14118)\n- [FormalSpecCpp](https://arxiv.org/abs/2502.15217)\n- [Astrogator](https://arxiv.org/abs/2507.13290)\n- [Metamorphic Prompt Testing](https://arxiv.org/abs/2406.06864)\n- [REA-Coder](https://arxiv.org/abs/2604.16198)\n- [SAGA / TCGBench](https://arxiv.org/abs/2507.06920)\n- [Quokka](https://arxiv.org/abs/2509.21629)\n- [Constrained Decoding for Correctness](https://arxiv.org/abs/2508.15866)\n- [Specification-Driven Code Generation Study - SANER 2026](https://arxiv.org/html/2601.03878v1)\n- [From Prompts to Properties - FSE 2025](https://dl.acm.org/doi/10.1145/3696630.3728702)"
      }
    ],
    "totalDurationMs": 203337,
    "totalTokens": 40864,
    "totalToolUseCount": 46,
    "usage": {
      "input_tokens": 208,
      "cache_creation_input_tokens": 978,
      "cache_read_input_tokens": 35195,
      "output_tokens": 4483,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 978
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 208,
          "output_tokens": 4483,
          "cache_read_input_tokens": 35195,
          "cache_creation_input_tokens": 978,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 978,
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
      "otherToolCount": 46
    }
  },
  "sourceToolAssistantUUID": "ced62a1d-723d-456c-8620-4a2122d7986a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "7fe6204f-e041-4c85-8ce3-26e4a2cdae89",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Execution-grounded behavioral specifications for code reasoning",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---

### Tool result

_source line 17 · 2026-05-12T01:00:59.941Z_

<details><summary>↩ Tool result · `toolu_01VTchuuXeW4xn6CdeQSkXrB`</summary>

```text
Here is a consolidated report for each of your seven searches.

---

## 1. SWE-bench Verified -- Current SOTA

The leaderboard is now widely regarded as **contaminated**. OpenAI's audit found frontier models can reproduce verbatim gold patches, and OpenAI has stopped reporting Verified scores, recommending **SWE-bench Pro** instead.

**Verified top scores (May 2026):**
| Rank | System | % Resolved |
|------|--------|-----------|
| 1 | Claude Mythos Preview | 93.9% |
| 2 | Claude Opus 4.7 (Adaptive) | 87.6% |
| 3 | GPT-5.3 Codex | ~85% |
| 4 | Claude Opus 4.5 | 80.9% |

**SWE-bench Pro (contamination-resistant):**
The *same* best model scores only ~46% on Pro vs. ~81% on Verified. Claude Opus 4.5 scores 45.9% on Pro with standardized scaffolding. This massive gap is evidence of benchmark contamination on Verified.

**Implication for your proposal:** If your paper cites SWE-bench Verified numbers, reviewers will likely challenge them. SWE-bench Pro is now the credible variant.

---

## 2. CodeContests -- SOTA and AlphaCodium Positioning

**AlphaCodium (GPT-4 + flow engineering):** 44% pass@5 on CodeContests validation set (up from GPT-4 baseline of 19%).

**AlphaCode 2 (DeepMind, Gemini-based):** Solves 43% of problems; achieved 85th percentile on Codeforces (between Expert and Candidate Master).

**Reasoning models have dramatically surpassed both:**
- **o1:** Codeforces Elo ~1807 (93rd percentile of humans)
- **o3:** Codeforces Elo ~2700 (top ~200 active users worldwide); gold medal at IOI without hand-crafted strategies
- RL-trained models on CodeContests+ achieve Pass@1 up to 34.57% on LiveCodeBench

**Implication:** AlphaCodium's 44% pass@5 is **no longer competitive** as a SOTA claim. The reasoning-model era (o1/o3) has moved the frontier significantly. However, AlphaCodium's result is still a valid reference point for *training-free, flow-engineering approaches* applied to standard LLMs.

---

## 3. DebugBench -- Current Best Results

DebugBench (4,253 instances, C++/Java/Python, 4 bug categories, 18 minor types):

**Original paper results (2024):**
- GPT-4: 75.0% (zero-shot)
- GPT-3.5-turbo: 62.1%
- Open-source models: 43.9%--66.6% (DeepSeek-Coder best among OSS)
- Human proficiency is *above* all of these

**No widely-cited 2025-2026 updates** were found. The benchmark appears to have seen limited adoption beyond the original paper. No results for GPT-4o, Claude Sonnet, or o1/o3 on DebugBench were found in search results.

**Implication:** DebugBench is a relatively niche benchmark. If your paper reports results on it, there is limited competition to compare against, which makes the gap claim harder to validate but also harder for reviewers to challenge with counter-evidence.

---

## 4. CrossCodeEval -- Current SOTA

CrossCodeEval (NeurIPS 2023; cross-file code completion in Python/Java/TypeScript/C#):

- **Baseline (no cross-file context):** Exact Match (EM) consistently < 11%
- **With BM25 retrieval:** EM roughly doubles/triples (e.g., CodeGen2.5-7B: 7.7% -> 14.5% on Python)
- **Current SOTA for 7B-16B models with advanced retrieval + static analysis:**
  - Java: **EM ~44%** (GrepRAG)
  - Python: **EM ~35%** (STALL+ + RAG)

**Implication:** The benchmark is still genuinely hard. Performance remains low enough that a meaningful improvement (e.g., +5-10% EM) would be noteworthy. The gap between in-file-only and retrieval-augmented is large and well-documented.

---

## 5. Papers with Code SWE-bench

Papers with Code tracks the SWE-bench-lite variant. The site also now lists variants including SWE-bench-java, Multi-SWE-bench (7 languages, 4,723 instances), and SWE-bench Multimodal. The leaderboard data largely mirrors what is reported on swebench.com (see item 1 above).

---

## 6. Qwen2.5-Coder-32B Performance

**Qwen2.5-Coder-32B-Instruct key scores:**
| Benchmark | Score |
|-----------|-------|
| HumanEval pass@1 | 88.4% (after SFT+DPO+GRPO) |
| HumanEval+ | ~87.2% |
| Aider (code repair) | 73.7 |
| MdEval | 75.2 (1st among OSS) |
| McEval (40+ languages) | 65.9 |
| LiveCodeBench Elo | ~2056 |

**Qwen2.5-Coder-7B-Instruct:**
| Benchmark | Score |
|-----------|-------|
| HumanEval+ | 84.1% |
| HumanEval | 61.6% |

The 32B variant is described as achieving "competitive performance with GPT-4o" and is the **best open-source model** on EvalPlus, LiveCodeBench, and BigCodeBench. The 7B variant outperforms many models with 20B+ parameters.

**Implication:** Qwen2.5-Coder-7B and -32B are strong, well-documented baselines. Using them is defensible. However, note that **Qwen3-Coder** has since been released, so reviewers may ask why you did not use the newer model. The 32B model's 88.4% HumanEval score means there is limited headroom on that benchmark -- improvements need to be demonstrated on harder benchmarks (LiveCodeBench, SWE-bench, CrossCodeEval) to be convincing.

---

## 7. Training-Free / Inference-Time Code Generation Methods

**Key methods and results:**

- **ReflexiCoder-8B (2025-2026):** Uses RL to internalize self-reflection. Achieves 94.51% HumanEval, 35.00% BigCodeBench, 52.21% LiveCodeBench, 37.34% CodeForces in single-attempt. Uses ~40% fewer tokens than base in iterative mode. (Note: this involves RL training, so is not purely training-free.)

- **EffiPair:** Training-free framework using Relative Contrastive Feedback. Compares structurally similar candidates with different efficiency profiles to improve runtime efficiency while preserving correctness.

- **PonderTTT:** Training-free adaptive compute allocation using test-time training with a gating strategy. Requires no learned classifier -- only a single scalar threshold calibrated on unlabeled data.

- **Self-repair / self-debugging:** Universally effective across model families. AST-based detectors identify reintroduction of previously resolved errors, improving accuracy by >10%.

- **Latent-trajectory early accept:** Reduces token usage by 48-70% vs. self-consistency while improving accuracy by 2.6% on average.

**Implication:** The space is active. If your method is truly training-free, the competitive landscape includes EffiPair, PonderTTT, and various self-repair frameworks. The key differentiator will be showing gains on hard benchmarks (not just HumanEval where scores are already >90%).

---

## Overall Assessment: Are the Proposed Baselines and Gaps Realistic?

1. **Qwen2.5-Coder-7B/32B as baselines:** Reasonable and well-documented, but Qwen3-Coder now exists. Reviewers may push for newer baselines.

2. **HumanEval gaps:** Very limited headroom (32B already at 88.4%). Claims of improvement here are hard to make impressive.

3. **CodeContests gap vs. AlphaCodium:** If positioning against AlphaCodium's 44%, be aware that reasoning models (o1/o3) have far surpassed this. The comparison is only valid within the "training-free + standard LLM" category.

4. **SWE-bench Verified:** Numbers are contaminated. Use SWE-bench Pro if possible, or clearly caveat Verified results.

5. **DebugBench / CrossCodeEval:** These remain genuinely hard with room for improvement. They are better venues to demonstrate meaningful gaps than saturated benchmarks like HumanEval.

Sources:
- [SWE-bench Verified Leaderboard - llm-stats.com](https://llm-stats.com/benchmarks/swe-bench-verified)
- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%](https://www.morphllm.com/swe-bench-pro)
- [SWE-bench Official Leaderboards](https://www.swebench.com/)
- [SWE-bench Verified - BenchLM.ai](https://benchlm.ai/benchmarks/sweVerified)
- [SWE-bench Verified - Epoch AI](https://epoch.ai/benchmarks/swe-bench-verified)
- [CodeContests - Papers with Code](https://paperswithcode.com/sota/code-generation-on-codecontests)
- [AlphaCodium - Qodo Blog](https://www.qodo.ai/blog/qodoflow-state-of-the-art-code-generation-for-code-contests/)
- [AlphaCode Statistics](https://www.aboutchromebooks.com/alphacode-statistics/)
- [Competitive Programming with Large Reasoning Models (o3)](https://arxiv.org/abs/2502.06807)
- [DebugBench Paper - arXiv](https://arxiv.org/abs/2401.04621)
- [DebugBench - ACL Anthology](https://aclanthology.org/2024.findings-acl.247/)
- [CrossCodeEval - GitHub](https://github.com/amazon-science/cceval)
- [CrossCodeEval Paper - arXiv](https://arxiv.org/abs/2310.11248)
- [Qwen2.5-Coder Family Blog](https://qwenlm.github.io/blog/qwen2.5-coder-family/)
- [Qwen2.5-Coder Technical Report](https://arxiv.org/html/2409.12186v3)
- [Qwen2.5-Coder-32B Overview - Emergent Mind](https://www.emergentmind.com/topics/qwen2-5-coder-32b-instruct)
- [EffiPair - arXiv](https://arxiv.org/html/2604.05137)
- [Inference-Time Techniques for Efficient Code Generation (UW)](https://courses.cs.washington.edu/courses/cse503/25wi/final-reports/Inference-Time%20Techniques%20for%20Efficient%20Code%20Generation.pdf)
- [ReflexiCoder - arXiv](https://arxiv.org/html/2603.05863)
- [PonderTTT - arXiv](https://arxiv.org/abs/2601.00894)
- [Self-Repair in LLM Code Generation](https://arxiv.org/html/2604.10508v1)
- [LiveCodeBench Leaderboard](https://livecodebench.github.io/leaderboard.html)
- [Best LLM for Coding 2026 - WhatLLM](https://whatllm.org/best-llm-for-coding)
- [CodeSOTA Code Generation Leaderboard](https://www.codesota.com/code-generation)

agentId: a7e449c952c5042c3 (use SendMessage with to: 'a7e449c952c5042c3' to continue this agent)
&lt;usage>total_tokens: 29076
tool_uses: 17
duration_ms: 246963&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1de02ba5-1601-42e5-ba1d-7381a331ed7c",
  "isSidechain": false,
  "promptId": "9e08ddf0-33d2-4d92-a77f-55540a5b8b2a",
  "type": "user",
  "uuid": "08f3dfcd-3a32-473a-b90f-0bf676acbff7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify the current state-of-the-art on several code benchmarks to assess whether a proposed method has realistic positioning. Please search for the following:\n\n1. Search: \"SWE-bench Verified leaderboard 2026 state of the art\" - What are the current top scores on SWE-bench Verified? What methods achieve them?\n2. Search: \"CodeContests benchmark SOTA 2025 2026\" - What are the best results on CodeContests? Is AlphaCodium's 44% pass@5 still competitive?\n3. Search: \"DebugBench LLM debugging benchmark results 2025 2026\" - What are the current best results?\n4. Search: \"CrossCodeEval benchmark results 2025 2026\" - Current SOTA?\n5. Search: site:paperswithcode.com \"SWE-bench\" - Check leaderboard\n6. Search: \"Qwen2.5-Coder-32B performance benchmarks\" - What does this model achieve on standard code benchmarks?\n7. Search: \"training-free code generation improvement 2025 2026 inference time\" - What training-free methods currently achieve the best results?\n\nReport what you find for each search. I want to know if the proposed baselines (Qwen2.5-Coder-7B/32B) and the claimed gaps are realistic.",
    "agentId": "a7e449c952c5042c3",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a consolidated report for each of your seven searches.\n\n---\n\n## 1. SWE-bench Verified -- Current SOTA\n\nThe leaderboard is now widely regarded as **contaminated**. OpenAI's audit found frontier models can reproduce verbatim gold patches, and OpenAI has stopped reporting Verified scores, recommending **SWE-bench Pro** instead.\n\n**Verified top scores (May 2026):**\n| Rank | System | % Resolved |\n|------|--------|-----------|\n| 1 | Claude Mythos Preview | 93.9% |\n| 2 | Claude Opus 4.7 (Adaptive) | 87.6% |\n| 3 | GPT-5.3 Codex | ~85% |\n| 4 | Claude Opus 4.5 | 80.9% |\n\n**SWE-bench Pro (contamination-resistant):**\nThe *same* best model scores only ~46% on Pro vs. ~81% on Verified. Claude Opus 4.5 scores 45.9% on Pro with standardized scaffolding. This massive gap is evidence of benchmark contamination on Verified.\n\n**Implication for your proposal:** If your paper cites SWE-bench Verified numbers, reviewers will likely challenge them. SWE-bench Pro is now the credible variant.\n\n---\n\n## 2. CodeContests -- SOTA and AlphaCodium Positioning\n\n**AlphaCodium (GPT-4 + flow engineering):** 44% pass@5 on CodeContests validation set (up from GPT-4 baseline of 19%).\n\n**AlphaCode 2 (DeepMind, Gemini-based):** Solves 43% of problems; achieved 85th percentile on Codeforces (between Expert and Candidate Master).\n\n**Reasoning models have dramatically surpassed both:**\n- **o1:** Codeforces Elo ~1807 (93rd percentile of humans)\n- **o3:** Codeforces Elo ~2700 (top ~200 active users worldwide); gold medal at IOI without hand-crafted strategies\n- RL-trained models on CodeContests+ achieve Pass@1 up to 34.57% on LiveCodeBench\n\n**Implication:** AlphaCodium's 44% pass@5 is **no longer competitive** as a SOTA claim. The reasoning-model era (o1/o3) has moved the frontier significantly. However, AlphaCodium's result is still a valid reference point for *training-free, flow-engineering approaches* applied to standard LLMs.\n\n---\n\n## 3. DebugBench -- Current Best Results\n\nDebugBench (4,253 instances, C++/Java/Python, 4 bug categories, 18 minor types):\n\n**Original paper results (2024):**\n- GPT-4: 75.0% (zero-shot)\n- GPT-3.5-turbo: 62.1%\n- Open-source models: 43.9%--66.6% (DeepSeek-Coder best among OSS)\n- Human proficiency is *above* all of these\n\n**No widely-cited 2025-2026 updates** were found. The benchmark appears to have seen limited adoption beyond the original paper. No results for GPT-4o, Claude Sonnet, or o1/o3 on DebugBench were found in search results.\n\n**Implication:** DebugBench is a relatively niche benchmark. If your paper reports results on it, there is limited competition to compare against, which makes the gap claim harder to validate but also harder for reviewers to challenge with counter-evidence.\n\n---\n\n## 4. CrossCodeEval -- Current SOTA\n\nCrossCodeEval (NeurIPS 2023; cross-file code completion in Python/Java/TypeScript/C#):\n\n- **Baseline (no cross-file context):** Exact Match (EM) consistently < 11%\n- **With BM25 retrieval:** EM roughly doubles/triples (e.g., CodeGen2.5-7B: 7.7% -> 14.5% on Python)\n- **Current SOTA for 7B-16B models with advanced retrieval + static analysis:**\n  - Java: **EM ~44%** (GrepRAG)\n  - Python: **EM ~35%** (STALL+ + RAG)\n\n**Implication:** The benchmark is still genuinely hard. Performance remains low enough that a meaningful improvement (e.g., +5-10% EM) would be noteworthy. The gap between in-file-only and retrieval-augmented is large and well-documented.\n\n---\n\n## 5. Papers with Code SWE-bench\n\nPapers with Code tracks the SWE-bench-lite variant. The site also now lists variants including SWE-bench-java, Multi-SWE-bench (7 languages, 4,723 instances), and SWE-bench Multimodal. The leaderboard data largely mirrors what is reported on swebench.com (see item 1 above).\n\n---\n\n## 6. Qwen2.5-Coder-32B Performance\n\n**Qwen2.5-Coder-32B-Instruct key scores:**\n| Benchmark | Score |\n|-----------|-------|\n| HumanEval pass@1 | 88.4% (after SFT+DPO+GRPO) |\n| HumanEval+ | ~87.2% |\n| Aider (code repair) | 73.7 |\n| MdEval | 75.2 (1st among OSS) |\n| McEval (40+ languages) | 65.9 |\n| LiveCodeBench Elo | ~2056 |\n\n**Qwen2.5-Coder-7B-Instruct:**\n| Benchmark | Score |\n|-----------|-------|\n| HumanEval+ | 84.1% |\n| HumanEval | 61.6% |\n\nThe 32B variant is described as achieving \"competitive performance with GPT-4o\" and is the **best open-source model** on EvalPlus, LiveCodeBench, and BigCodeBench. The 7B variant outperforms many models with 20B+ parameters.\n\n**Implication:** Qwen2.5-Coder-7B and -32B are strong, well-documented baselines. Using them is defensible. However, note that **Qwen3-Coder** has since been released, so reviewers may ask why you did not use the newer model. The 32B model's 88.4% HumanEval score means there is limited headroom on that benchmark -- improvements need to be demonstrated on harder benchmarks (LiveCodeBench, SWE-bench, CrossCodeEval) to be convincing.\n\n---\n\n## 7. Training-Free / Inference-Time Code Generation Methods\n\n**Key methods and results:**\n\n- **ReflexiCoder-8B (2025-2026):** Uses RL to internalize self-reflection. Achieves 94.51% HumanEval, 35.00% BigCodeBench, 52.21% LiveCodeBench, 37.34% CodeForces in single-attempt. Uses ~40% fewer tokens than base in iterative mode. (Note: this involves RL training, so is not purely training-free.)\n\n- **EffiPair:** Training-free framework using Relative Contrastive Feedback. Compares structurally similar candidates with different efficiency profiles to improve runtime efficiency while preserving correctness.\n\n- **PonderTTT:** Training-free adaptive compute allocation using test-time training with a gating strategy. Requires no learned classifier -- only a single scalar threshold calibrated on unlabeled data.\n\n- **Self-repair / self-debugging:** Universally effective across model families. AST-based detectors identify reintroduction of previously resolved errors, improving accuracy by >10%.\n\n- **Latent-trajectory early accept:** Reduces token usage by 48-70% vs. self-consistency while improving accuracy by 2.6% on average.\n\n**Implication:** The space is active. If your method is truly training-free, the competitive landscape includes EffiPair, PonderTTT, and various self-repair frameworks. The key differentiator will be showing gains on hard benchmarks (not just HumanEval where scores are already >90%).\n\n---\n\n## Overall Assessment: Are the Proposed Baselines and Gaps Realistic?\n\n1. **Qwen2.5-Coder-7B/32B as baselines:** Reasonable and well-documented, but Qwen3-Coder now exists. Reviewers may push for newer baselines.\n\n2. **HumanEval gaps:** Very limited headroom (32B already at 88.4%). Claims of improvement here are hard to make impressive.\n\n3. **CodeContests gap vs. AlphaCodium:** If positioning against AlphaCodium's 44%, be aware that reasoning models (o1/o3) have far surpassed this. The comparison is only valid within the \"training-free + standard LLM\" category.\n\n4. **SWE-bench Verified:** Numbers are contaminated. Use SWE-bench Pro if possible, or clearly caveat Verified results.\n\n5. **DebugBench / CrossCodeEval:** These remain genuinely hard with room for improvement. They are better venues to demonstrate meaningful gaps than saturated benchmarks like HumanEval.\n\nSources:\n- [SWE-bench Verified Leaderboard - llm-stats.com](https://llm-stats.com/benchmarks/swe-bench-verified)\n- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%](https://www.morphllm.com/swe-bench-pro)\n- [SWE-bench Official Leaderboards](https://www.swebench.com/)\n- [SWE-bench Verified - BenchLM.ai](https://benchlm.ai/benchmarks/sweVerified)\n- [SWE-bench Verified - Epoch AI](https://epoch.ai/benchmarks/swe-bench-verified)\n- [CodeContests - Papers with Code](https://paperswithcode.com/sota/code-generation-on-codecontests)\n- [AlphaCodium - Qodo Blog](https://www.qodo.ai/blog/qodoflow-state-of-the-art-code-generation-for-code-contests/)\n- [AlphaCode Statistics](https://www.aboutchromebooks.com/alphacode-statistics/)\n- [Competitive Programming with Large Reasoning Models (o3)](https://arxiv.org/abs/2502.06807)\n- [DebugBench Paper - arXiv](https://arxiv.org/abs/2401.04621)\n- [DebugBench - ACL Anthology](https://aclanthology.org/2024.findings-acl.247/)\n- [CrossCodeEval - GitHub](https://github.com/amazon-science/cceval)\n- [CrossCodeEval Paper - arXiv](https://arxiv.org/abs/2310.11248)\n- [Qwen2.5-Coder Family Blog](https://qwenlm.github.io/blog/qwen2.5-coder-family/)\n- [Qwen2.5-Coder Technical Report](https://arxiv.org/html/2409.12186v3)\n- [Qwen2.5-Coder-32B Overview - Emergent Mind](https://www.emergentmind.com/topics/qwen2-5-coder-32b-instruct)\n- [EffiPair - arXiv](https://arxiv.org/html/2604.05137)\n- [Inference-Time Techniques for Efficient Code Generation (UW)](https://courses.cs.washington.edu/courses/cse503/25wi/final-reports/Inference-Time%20Techniques%20for%20Efficient%20Code%20Generation.pdf)\n- [ReflexiCoder - arXiv](https://arxiv.org/html/2603.05863)\n- [PonderTTT - arXiv](https://arxiv.org/abs/2601.00894)\n- [Self-Repair in LLM Code Generation](https://arxiv.org/html/2604.10508v1)\n- [LiveCodeBench Leaderboard](https://livecodebench.github.io/leaderboard.html)\n- [Best LLM for Coding 2026 - WhatLLM](https://whatllm.org/best-llm-for-coding)\n- [CodeSOTA Code Generation Leaderboard](https://www.codesota.com/code-generation)"
      }
    ],
    "totalDurationMs": 246963,
    "totalTokens": 29076,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 24787,
      "output_tokens": 3093,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1195
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3093,
          "cache_read_input_tokens": 24787,
          "cache_creation_input_tokens": 1195,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1195,
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
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "1de02ba5-1601-42e5-ba1d-7381a331ed7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-12T01:01:03.042Z_

Good — all references verified. Now let me fetch the most critical competing papers that the generator missed to assess the novelty threat.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08f3dfcd-3a32-473a-b90f-0bf676acbff7",
  "isSidechain": false,
  "requestId": "req_011Cawmfu5jccaJ23NEEryHT",
  "type": "assistant",
  "uuid": "838097da-53bb-4ae0-9708-9f69e2d551e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRoNtV6g9GT8G8nyVJnfRL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11574,
      "cache_read_input_tokens": 32426,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 32426,
          "cache_creation_input_tokens": 11574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11574
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

_source line 19 · 2026-05-12T01:01:03.715Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VeDho5dApe5p5m2iupwp7H`</summary>

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
  "parentUuid": "838097da-53bb-4ae0-9708-9f69e2d551e8",
  "isSidechain": false,
  "requestId": "req_011Cawmfu5jccaJ23NEEryHT",
  "type": "assistant",
  "uuid": "c8e9d2e2-fe85-4d7f-a7d8-af4537603c50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRoNtV6g9GT8G8nyVJnfRL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11574,
      "cache_read_input_tokens": 32426,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 32426,
          "cache_creation_input_tokens": 11574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11574
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

_source line 20 · 2026-05-12T01:01:03.721Z_

<details><summary>↩ Tool result · `toolu_01VeDho5dApe5p5m2iupwp7H`</summary>

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
  "parentUuid": "c8e9d2e2-fe85-4d7f-a7d8-af4537603c50",
  "isSidechain": false,
  "promptId": "9e08ddf0-33d2-4d92-a77f-55540a5b8b2a",
  "type": "user",
  "uuid": "d1fa7249-f134-4a3e-840e-5c9131785914",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "c8e9d2e2-fe85-4d7f-a7d8-af4537603c50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-12T01:01:11.490Z_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the most critical competing papers to assess the novelty threat. The most important ones identified are:

1. **PGS (arXiv:2506.18315)** - Uses properties (not tests) as feedback; most direct methodological competitor
2. **"From Prompts to Properties" (FSE 2025)** - Rethinking LLM code generation with property-based testing
3. **ContractEval (arXiv:2510.12047)** - Benchmarks contract satisfaction
4. **"Preconditions and Postconditions as Design Constraints" (IEEE)** - Controlled study of ExeSpec's premise


5. **PGS and "From Prompts to Properties"** - These are the most direct competitors I need to examine closely.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1fa7249-f134-4a3e-840e-5c9131785914",
  "isSidechain": false,
  "requestId": "req_011CawmgBRkAHCThimsA4w8X",
  "type": "assistant",
  "uuid": "b9b1e54b-1b6c-48a6-bc75-210d22bd6d5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Twxcisfeq19vWy3UyiKCE2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 44000,
      "output_tokens": 737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 737,
          "cache_read_input_tokens": 44000,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 622
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

_source line 22 · 2026-05-12T01:01:11.560Z_

Let me fetch the most critical competing papers to assess novelty threats.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9b1e54b-1b6c-48a6-bc75-210d22bd6d5d",
  "isSidechain": false,
  "requestId": "req_011CawmgBRkAHCThimsA4w8X",
  "type": "assistant",
  "uuid": "51014952-8f5d-4971-bf6f-090bedc2021b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Twxcisfeq19vWy3UyiKCE2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 44000,
      "output_tokens": 737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 737,
          "cache_read_input_tokens": 44000,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 622
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

_source line 23 · 2026-05-12T01:01:13.771Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FWF7DMRjrj4atwd7kU7SYQ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.18315",
  "prompt": "Extract the full abstract, key methodology, and main results of this paper. Specifically: (1) Does it use property-based testing as feedback for LLM code generation? (2) How does it differ from using test cases? (3) What benchmarks does it evaluate on and what improvements does it achieve? (4) Is it training-free?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51014952-8f5d-4971-bf6f-090bedc2021b",
  "isSidechain": false,
  "requestId": "req_011CawmgBRkAHCThimsA4w8X",
  "type": "assistant",
  "uuid": "bd81562d-bb54-4e8b-a1c0-35a4f68279b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Twxcisfeq19vWy3UyiKCE2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 44000,
      "output_tokens": 737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 737,
          "cache_read_input_tokens": 44000,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 622
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

_source line 24 · 2026-05-12T01:01:15.828Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q4M9hKjyvSHuQfbKyfbYP1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.12702",
  "prompt": "Extract the full abstract and key findings. Specifically: (1) Does it study LLMs generating formal contracts (preconditions and postconditions)? (2) What is the success rate? (3) How does it relate to using specifications as intermediate reasoning for code generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd81562d-bb54-4e8b-a1c0-35a4f68279b2",
  "isSidechain": false,
  "requestId": "req_011CawmgBRkAHCThimsA4w8X",
  "type": "assistant",
  "uuid": "3ac4a4e7-ecda-4c29-9553-71eb34937747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Twxcisfeq19vWy3UyiKCE2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 44000,
      "output_tokens": 737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 737,
          "cache_read_input_tokens": 44000,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 622
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

_source line 25 · 2026-05-12T01:01:17.042Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NRbmESUcyMeK2y2Hanimim`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.12047",
  "prompt": "Extract the full abstract and key findings. Specifically: (1) What is ContractEval? (2) How well do LLMs satisfy precondition/postcondition contracts? (3) What does this tell us about specification-guided code generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ac4a4e7-ecda-4c29-9553-71eb34937747",
  "isSidechain": false,
  "requestId": "req_011CawmgBRkAHCThimsA4w8X",
  "type": "assistant",
  "uuid": "e11df646-6332-438b-ab7f-641159d912f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Twxcisfeq19vWy3UyiKCE2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 44000,
      "output_tokens": 737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 737,
          "cache_read_input_tokens": 44000,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 622
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

_source line 26 · 2026-05-12T01:01:18.575Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S8bQm4iq8WspRAnCBvARAk`</summary>

```json
{
  "url": "https://dl.acm.org/doi/10.1145/3696630.3728702",
  "prompt": "Extract the full abstract and key findings of this paper about property-based testing for LLM code generation from FSE 2025. What does it propose? How does property-based testing compare to example-based testing for LLM code validation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e11df646-6332-438b-ab7f-641159d912f9",
  "isSidechain": false,
  "requestId": "req_011CawmgBRkAHCThimsA4w8X",
  "type": "assistant",
  "uuid": "fb78c5f3-7690-4f42-b68c-9ae7c112c6a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Twxcisfeq19vWy3UyiKCE2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 44000,
      "output_tokens": 737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 737,
          "cache_read_input_tokens": 44000,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 622
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

_source line 27 · 2026-05-12T01:01:18.590Z_

<details><summary>↩ Tool result · reported error · `toolu_01S8bQm4iq8WspRAnCBvARAk`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb78c5f3-7690-4f42-b68c-9ae7c112c6a1",
  "isSidechain": false,
  "promptId": "9e08ddf0-33d2-4d92-a77f-55540a5b8b2a",
  "type": "user",
  "uuid": "0665907a-aacf-427d-a0b1-11a36a001d69",
  "toolUseResult": "Error: Request failed with status code 403",
  "sourceToolAssistantUUID": "fb78c5f3-7690-4f42-b68c-9ae7c112c6a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
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
  "leafUuid": "0665907a-aacf-427d-a0b1-11a36a001d69",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Execution-grounded behavioral specifications for code reasoning",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---

### Tool result

_source line 30 · 2026-05-12T01:01:18.825Z_

<details><summary>↩ Tool result · `toolu_01FWF7DMRjrj4atwd7kU7SYQ`</summary>

```text
# Analysis of arXiv Paper 2506.18315

## (1) Property-Based Testing for Feedback?

Yes. The paper introduces the **Property-Generated Solver (PGS)**, which uses high-level program properties (e.g., sorting functions producing non-decreasing sequences) to generate feedback for LLM code refinement.

## (2) Difference from Test Cases

The key distinction is in feedback quality over quantity. Rather than relying on numerous test cases, PGS provides:
- **Property-oriented feedback**: Semantic guidance addressing "high-level program properties" rather than simple input-output mismatches
- **Structurally minimal counterexamples**: The simplest failing example to "reduce cognitive load and isolate root causes"

This targets root cause identification rather than test volume.

## (3) Benchmarks and Improvements

The document specifies these results:
- Up to **13.4% improvement in pass@1** versus other Test-Driven Development methods
- Over **64% fix rate** on initially-failed problems
- **1.4x-1.6x higher bug fix rate** compared to strongest debugging-based approaches
- Evaluates across "diverse benchmarks" establishing "state-of-the-art in automated code refinement"

Specific benchmark names aren't detailed in the abstract provided.

## (4) Training-Free Status

The abstract doesn't explicitly address whether PGS requires model training, so this cannot be confirmed from the available content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd81562d-bb54-4e8b-a1c0-35a4f68279b2",
  "isSidechain": false,
  "promptId": "9e08ddf0-33d2-4d92-a77f-55540a5b8b2a",
  "type": "user",
  "uuid": "5c368848-4a31-4906-a4aa-e1c540102dd0",
  "toolUseResult": {
    "bytes": 47303,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of arXiv Paper 2506.18315\n\n## (1) Property-Based Testing for Feedback?\n\nYes. The paper introduces the **Property-Generated Solver (PGS)**, which uses high-level program properties (e.g., sorting functions producing non-decreasing sequences) to generate feedback for LLM code refinement.\n\n## (2) Difference from Test Cases\n\nThe key distinction is in feedback quality over quantity. Rather than relying on numerous test cases, PGS provides:\n- **Property-oriented feedback**: Semantic guidance addressing \"high-level program properties\" rather than simple input-output mismatches\n- **Structurally minimal counterexamples**: The simplest failing example to \"reduce cognitive load and isolate root causes\"\n\nThis targets root cause identification rather than test volume.\n\n## (3) Benchmarks and Improvements\n\nThe document specifies these results:\n- Up to **13.4% improvement in pass@1** versus other Test-Driven Development methods\n- Over **64% fix rate** on initially-failed problems\n- **1.4x-1.6x higher bug fix rate** compared to strongest debugging-based approaches\n- Evaluates across \"diverse benchmarks\" establishing \"state-of-the-art in automated code refinement\"\n\nSpecific benchmark names aren't detailed in the abstract provided.\n\n## (4) Training-Free Status\n\nThe abstract doesn't explicitly address whether PGS requires model training, so this cannot be confirmed from the available content.",
    "durationMs": 5050,
    "url": "https://arxiv.org/abs/2506.18315"
  },
  "sourceToolAssistantUUID": "bd81562d-bb54-4e8b-a1c0-35a4f68279b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-12T01:01:20.213Z_

<details><summary>↩ Tool result · `toolu_01Q4M9hKjyvSHuQfbKyfbYP1`</summary>

```text
# Analysis of arXiv:2510.12702

## Full Abstract
The paper addresses the challenge that automatic software verifiers struggle when formal specifications are absent from real-world code. It introduces **NL2Contract**, a task employing LLMs to convert natural language into formal functional contracts (both preconditions and postconditions). The study evaluates approaches using soundness, bug discrimination, and verification utility as metrics, comparing against postcondition-only generation.

## Key Findings

**(1) Does it study LLMs generating formal contracts?**
Yes. The paper explicitly states: "employ LLMs to translate informal natural language into formal functional contracts, consisting of postconditions as well as preconditions."

**(2) Success Rate**
The abstract reports three positive outcomes:
- "LLMs are generally effective at generating functional contracts sound for all possible inputs"
- Generated contracts successfully discriminate buggy from correct behavior
- "Verifiers supplied with LLM inferred functional contracts produce fewer false alarms than when provided with postconditions alone"

However, no specific numerical success rates are provided in the abstract.

**(3) Relation to Specifications as Intermediate Reasoning**
The abstract does **not** address using specifications for code generation or intermediate reasoning. Instead, it frames specifications as outputs for **verification purposes**—to reduce false alarms in automatic software verification rather than to guide generation tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ac4a4e7-ecda-4c29-9553-71eb34937747",
  "isSidechain": false,
  "promptId": "9e08ddf0-33d2-4d92-a77f-55540a5b8b2a",
  "type": "user",
  "uuid": "b8057975-b54a-4601-a9d6-4e1b874d3f59",
  "toolUseResult": {
    "bytes": 47198,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of arXiv:2510.12702\n\n## Full Abstract\nThe paper addresses the challenge that automatic software verifiers struggle when formal specifications are absent from real-world code. It introduces **NL2Contract**, a task employing LLMs to convert natural language into formal functional contracts (both preconditions and postconditions). The study evaluates approaches using soundness, bug discrimination, and verification utility as metrics, comparing against postcondition-only generation.\n\n## Key Findings\n\n**(1) Does it study LLMs generating formal contracts?**\nYes. The paper explicitly states: \"employ LLMs to translate informal natural language into formal functional contracts, consisting of postconditions as well as preconditions.\"\n\n**(2) Success Rate**\nThe abstract reports three positive outcomes:\n- \"LLMs are generally effective at generating functional contracts sound for all possible inputs\"\n- Generated contracts successfully discriminate buggy from correct behavior\n- \"Verifiers supplied with LLM inferred functional contracts produce fewer false alarms than when provided with postconditions alone\"\n\nHowever, no specific numerical success rates are provided in the abstract.\n\n**(3) Relation to Specifications as Intermediate Reasoning**\nThe abstract does **not** address using specifications for code generation or intermediate reasoning. Instead, it frames specifications as outputs for **verification purposes**—to reduce false alarms in automatic software verification rather than to guide generation tasks.",
    "durationMs": 4383,
    "url": "https://arxiv.org/abs/2510.12702"
  },
  "sourceToolAssistantUUID": "3ac4a4e7-ecda-4c29-9553-71eb34937747",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-12T01:01:21.219Z_

<details><summary>↩ Tool result · `toolu_01NRbmESUcyMeK2y2Hanimim`</summary>

```text
# ContractEval: Contract Satisfaction in Code Generation

## What is ContractEval?

ContractEval is a benchmark built on HumanEval+ and MBPP+ comprising 364 tasks designed to evaluate whether generated code enforces input preconditions and postconditions—referred to as "contracts." Each task includes reconstructed descriptions explicitly stating contracts, synthesized test cases from a neuro-symbolic LLM-SMT solver pipeline, and reference code with contracts.

## LLM Contract Satisfaction Performance

The findings are striking. Under standard prompting, five open-source code LLMs achieved "pass@1 of 75-82% with 0% contract satisfaction." Even with explicit contract statements in prompts, satisfaction rates only reached "23-41%," demonstrating severe deficiencies in enforcing preconditions despite strong functional correctness metrics.

## Implications for Specification-Guided Code Generation

This research establishes contract satisfaction as a critical, previously overlooked dimension of code quality. The stark disparity between functional correctness and contract adherence reveals that current LLMs fundamentally struggle with specification compliance—a crucial gap for real-world applications where enforcing preconditions is essential for reliability and safety.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e11df646-6332-438b-ab7f-641159d912f9",
  "isSidechain": false,
  "promptId": "9e08ddf0-33d2-4d92-a77f-55540a5b8b2a",
  "type": "user",
  "uuid": "4381bdd8-cb17-4d15-8e27-2ae0be8dbb73",
  "toolUseResult": {
    "bytes": 48671,
    "code": 200,
    "codeText": "OK",
    "result": "# ContractEval: Contract Satisfaction in Code Generation\n\n## What is ContractEval?\n\nContractEval is a benchmark built on HumanEval+ and MBPP+ comprising 364 tasks designed to evaluate whether generated code enforces input preconditions and postconditions—referred to as \"contracts.\" Each task includes reconstructed descriptions explicitly stating contracts, synthesized test cases from a neuro-symbolic LLM-SMT solver pipeline, and reference code with contracts.\n\n## LLM Contract Satisfaction Performance\n\nThe findings are striking. Under standard prompting, five open-source code LLMs achieved \"pass@1 of 75-82% with 0% contract satisfaction.\" Even with explicit contract statements in prompts, satisfaction rates only reached \"23-41%,\" demonstrating severe deficiencies in enforcing preconditions despite strong functional correctness metrics.\n\n## Implications for Specification-Guided Code Generation\n\nThis research establishes contract satisfaction as a critical, previously overlooked dimension of code quality. The stark disparity between functional correctness and contract adherence reveals that current LLMs fundamentally struggle with specification compliance—a crucial gap for real-world applications where enforcing preconditions is essential for reliability and safety.",
    "durationMs": 4174,
    "url": "https://arxiv.org/abs/2510.12047"
  },
  "sourceToolAssistantUUID": "e11df646-6332-438b-ab7f-641159d912f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-12T01:01:21.222Z_

```json
{
  "parentUuid": "4381bdd8-cb17-4d15-8e27-2ae0be8dbb73",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "71a4cc8c-4a45-411f-8de4-e6e2c71cf800",
  "timestamp": "2026-05-12T01:01:21.222Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-12T01:02:43.502Z_

<details><summary>Logged reasoning block</summary>

```text
The FSE 2025 paper fetch failed. Let me try to search for it differently. But I have enough information now. Let me also check one more critical thing - the PGS paper is very relevant. Let me fetch more details on it.

Actually, let me now assess what I've found:

## Key findings from my research:

### Reference Verification
All 8 papers verified as existing with correct venues and claims. Good.

### Critical Missing Competing Work

1. **PGS (Property-Generated Solver, arXiv:2506.18315)** - This is a VERY direct competitor. 

PGS uses high-level program properties as feedback instead of test cases, achieving significant improvements in pass@1 and bug fix rates. The core idea overlaps substantially with ExeSpec—both leverage properties or specifications as intermediate feedback rather than relying solely on tests, though PGS frames this through property-based testing while ExeSpec emphasizes behavioral specifications for structured reasoning.

2. **"From Prompts to Properties" (FSE 2025)** - Couldn't fetch details, but it's about rethinking LLM code generation with property-based testing. Very relevant.

3. **ContractEval (arXiv:2510.12047)** - Shows...

ContractEval reveals a critical tension: LLMs achieve 0% contract satisfaction under standard prompting but 23-41% when contracts are explicitly provided, which validates ExeSpec's core problem while raising a troubling question about whether LLMs can reliably generate good specifications if they struggle to satisfy them even when given explicit guidance.

4. **NL2Contract (arXiv:2510.12702)** - LLMs generating formal contracts for verification, more focused on verification than generation but still overlapping.

5. **"Preconditions and Postconditions as Design Constraints" (IEEE)** - Directly examines how pre/postconditions influence LLM code generation.

6. **Type-Constrained Code Generation (arXiv:2504.09246)** - Shows type constraints alone help during decoding.

Now I'm looking at the state-of-the-art verification benchmarks. SWE-bench Verified is heavily contaminated with a 93.9% top score, so SWE-bench Pro is the recommended alternative. AlphaCodium's...

Looking at the competitive landscape across different benchmarks: CodeContests shows 44% pass@5 which isn't competitive against reasoning models like o3, DebugBench has limited adoption with GPT-4 at 75% and open-source models at 43-66%, CrossCodeEval remains challenging with SOTA around 35-44% exact match, and HumanEval is essentially saturated at 88%+ for recent models like Qwen2.5-Coder-32B. There's also the question of whether reviewers will expect evaluation on Qwen3-Coder since it exists now.

For novelty, the core claim is that property-level behavioral specifications like pre/postconditions, invariants, and type constraints provide richer intermediate reasoning than test cases for LLM code tasks. But PGS already uses properties rather than tests as feedback for code refinement, so I need to identify what actually differentiates this work—possibly the specific way properties are used or the scope of what's being refined.

There's also a feasibility concern from ContractEval: if LLMs achieve 0% contract satisfaction under standard prompting, how well can they even generate specs in the first place? The execution grounding is meant to catch bad specs, but if most generated specs are bad anyway (CodeSpecBench shows only 20.2% repo-level satisfaction), the whole method might degrade significantly.

Looking at the strengths, the revision is well-structured with verified references, controlled ablations, and honest positioning against AlphaCodium. The compute budget seems reasonable at 100-150 H100-hours.

But there are critical gaps: PGS is a major missing competitor with the exact same core insight about properties outperforming tests, and it shows 13.4% improvement gains. "From Prompts to Properties" is also directly relevant for property-based testing in LLM code generation. These need to be cited and differentiated against.

ContractEval raises a real concern—LLMs only satisfy contracts 23-41% of the time with prompting, which questions whether the spec generation quality is actually sufficient. I should also note the SWE-bench Verified contamination issue and consider using SWE-bench Pro instead. Qwen3-Coder exists as an alternative model choice that reviewers might question. The timeline is still tight with only 14-18 days to build the framework, run 6 benchmarks, and write everything up.

On novelty, the core idea of using specs over tests for intermediate reasoning isn't particularly novel given PGS and related work—I'd rate it around a 3. The execution-grounded spec verification and multi-task application add some differentiation, but it's fairly incremental. PGS is a significant threat to the novelty claim, though ExeSpec does push further in some directions.

For feasibility, the plan is detailed and realistic with the compute budget, but 14-18 days for implementing a 3-stage framework across multiple benchmarks with ablations is genuinely tight. The author has clearly thought through the execution carefully, so I'll give this a fair 3 on feasibility.

The clarity is strong—the three-stage pipeline, experimental design, and positioning are all well-articulated with specific examples, so that's a 4.

On impact, if property-level specs outperform test-based refinement across tasks, that's meaningful, but the contribution is somewhat limited by the training-free nature and potentially modest gains compared to prior work.

Averaging the scores gives 3.25, below the 4.0 threshold. The core issues are the missing PGS competitor that questions novelty, the tight timeline, and the SWE-bench contamination concern. But since this is Round 4 and the idea has improved, these feel fixable—I should give a revise verdict with concrete guidance.

Actually, I need to verify when PGS was published. The arXiv ID 2506.18315 indicates June 2025, so it's already out there.

That said, ExeSpec has meaningful distinctions from PGS: it uses specs as reasoning scaffolds rather than just testing feedback, it grounds specs through execution to catch hallucinations, it spans multiple task types beyond code generation, and its spec schema is richer with pre/postconditions, invariants, and type constraints. These aren't trivial differences—it's more of a "cite and differentiate" situation than a novelty problem.

Now I'm thinking about whether this clears the bar for EMNLP's NLP and Code Models track.

The controlled experiments with honest ablations are solid, and the multi-task evaluation across diverse benchmarks strengthens the work. The main risk is whether reviewers see this as systems engineering rather than NLP methodology, though framing it as structured intermediate reasoning for LLMs should address that concern.

Looking at my assessment: novelty scores around 3 because the core insight overlaps with prior work, though execution grounding and multi-task scope add some methodological value. Feasibility is also around 3—the timeline is tight at 14-18 days with a 16-day constraint, the approach is complex, and there's contamination risk with SWE-bench to navigate.

The writing is clear with a well-structured pipeline and honest ablation design, so clarity gets a 4. Impact lands at 3 since inference-time methods are useful but modest in scope. That puts me at an average of 3.25, leaning toward revision.

The revision priorities are clear: differentiate against PGS more explicitly, address the SWE-bench contamination head-on, and engage with "From Prompts to Properties" and ContractEval. But stepping back, I'm wondering if I'm being too critical here. The problem formulation is solid, the positioning against 21 key papers is thorough, and the experimental rigor is genuinely strong.

Looking at the actual contributions—the multi-stage execution grounding of specs and the multi-task evaluation across generation, debugging, completion, and issue resolution—these do meaningfully extend beyond what PGS does. The ablation structure honestly tests the novelty claim. So I'll keep the scores but reframe this as a straightforward revision with targeted fixes rather than a fundamental rejection. The main work is citing PGS properly, clarifying the conceptual differences, and handling the contamination concern.

Now checking the timeline: today is May 11th, and the ARR deadline is May 25th—that's 14 days, which aligns with the manual estimate of 14-18 days. It's tight but feasible with two people working focused on this.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71a4cc8c-4a45-411f-8de4-e6e2c71cf800",
  "isSidechain": false,
  "requestId": "req_011CawmhU3AE5Z7c2AdRa63H",
  "type": "assistant",
  "uuid": "ba224490-5a8b-48cd-8fe8-e2cf381b5b78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S259mmtuTFCvC6dBCoxote",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 1825,
      "cache_read_input_tokens": 44622,
      "output_tokens": 3436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1825,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 39,
          "output_tokens": 3436,
          "cache_read_input_tokens": 44622,
          "cache_creation_input_tokens": 1825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1825
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

_source line 35 · 2026-05-12T01:02:43.504Z_

Now let me fetch the PGS paper in more detail — it's the most direct novelty threat.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba224490-5a8b-48cd-8fe8-e2cf381b5b78",
  "isSidechain": false,
  "requestId": "req_011CawmhU3AE5Z7c2AdRa63H",
  "type": "assistant",
  "uuid": "5abc8d8e-41eb-4af5-99e2-30f7ae6969c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S259mmtuTFCvC6dBCoxote",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 1825,
      "cache_read_input_tokens": 44622,
      "output_tokens": 3436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1825,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 39,
          "output_tokens": 3436,
          "cache_read_input_tokens": 44622,
          "cache_creation_input_tokens": 1825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1825
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

_source line 36 · 2026-05-12T01:02:46.193Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018BVXZot79MTwKbLQmuHTCY`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.18315",
  "prompt": "Extract: (1) the full abstract, (2) whether this is training-free, (3) what benchmarks it evaluates on, (4) does it use execution to verify properties, (5) does it apply to debugging or just code generation, (6) publication venue if any. I need detailed methodology - how exactly are properties generated and used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5abc8d8e-41eb-4af5-99e2-30f7ae6969c8",
  "isSidechain": false,
  "requestId": "req_011CawmhU3AE5Z7c2AdRa63H",
  "type": "assistant",
  "uuid": "88602708-e076-4d60-a29b-b8a496744f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S259mmtuTFCvC6dBCoxote",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 1825,
      "cache_read_input_tokens": 44622,
      "output_tokens": 3436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1825,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 39,
          "output_tokens": 3436,
          "cache_read_input_tokens": 44622,
          "cache_creation_input_tokens": 1825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1825
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

_source line 37 · 2026-05-12T01:02:50.083Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FCe73JC3XAazKL3PAHV1PU`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify ARR May 2026 deadline",
  "prompt": "Search the web for the ARR (ACL Rolling Review) submission deadline for May 2026, and the EMNLP 2026 commitment deadline. I need to verify:\n1. Is there an ARR submission cycle with deadline around May 25, 2026?\n2. When is the EMNLP 2026 commitment deadline?\n3. Is EMNLP 2026 in Budapest?\n\nSearch: \"ACL Rolling Review May 2026 submission deadline\"\nSearch: \"EMNLP 2026 dates Budapest commitment deadline\"\nSearch: \"ARR 2026 submission cycles dates\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88602708-e076-4d60-a29b-b8a496744f23",
  "isSidechain": false,
  "requestId": "req_011CawmhU3AE5Z7c2AdRa63H",
  "type": "assistant",
  "uuid": "0ed927e3-506a-45fe-97f3-9295d652f4ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S259mmtuTFCvC6dBCoxote",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 1825,
      "cache_read_input_tokens": 44622,
      "output_tokens": 3436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1825,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 39,
          "output_tokens": 3436,
          "cache_read_input_tokens": 44622,
          "cache_creation_input_tokens": 1825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1825
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

_source line 38 · 2026-05-12T01:02:51.757Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PPaZFXvqvJRb7DZgz2kk8f`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.14631",
  "prompt": "Extract the abstract and key methodology of StoryCoder. Does it use structured intermediate representations for code generation? What improvements does it achieve? Is it training-free?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ed927e3-506a-45fe-97f3-9295d652f4ca",
  "isSidechain": false,
  "requestId": "req_011CawmhU3AE5Z7c2AdRa63H",
  "type": "assistant",
  "uuid": "a9cba3e8-4158-46e8-abd5-7c8f168ee215",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S259mmtuTFCvC6dBCoxote",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 1825,
      "cache_read_input_tokens": 44622,
      "output_tokens": 3436,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1825,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 39,
          "output_tokens": 3436,
          "cache_read_input_tokens": 44622,
          "cache_creation_input_tokens": 1825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1825
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a9cba3e8-4158-46e8-abd5-7c8f168ee215",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Execution-grounded behavioral specifications for code reasoning",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---

### Tool result

_source line 41 · 2026-05-12T01:02:55.015Z_

<details><summary>↩ Tool result · `toolu_018BVXZot79MTwKbLQmuHTCY`</summary>

```text
# Analysis of arXiv:2506.18315

## (1) Full Abstract

"LLMs excel at code generation, yet ensuring the functional correctness of their outputs remains a persistent challenge. While recent studies have applied Test-Driven Development (TDD) to refine code, these methods are often undermined by poor feedback quality, stemming from the scarcity of high-quality test cases and noisy signals from auto-generated ones. In this work, we shift the focus from test quantity to feedback quality. We introduce the Property-Generated Solver (PGS), a novel paradigm designed to generate highly effective feedback via two principles: it must be property-oriented, to provide semantic guidance beyond simple I/O mismatches, and structurally minimal, to reduce cognitive load and isolate root causes. PGS operates by checking high-level program properties (e.g., a sorting function must produce a non-decreasing sequence) then providing the simplest failing counterexample to the LLM. By adhering to these principles, this targeted feedback mechanism leads to significant performance gains. Specifically, PGS achieves an improvement of up to 13.4% in pass@1 against other TDD-based methods and an over 64% fix rate on problems where the model initially failed. This property-driven, minimal feedback steers LLMs toward correct and generalizable solutions. Across diverse benchmarks, PGS demonstrates superior performance, achieving a bug fix rate 1.4x-1.6x higher than the strongest debugging-based approaches and establishing a new state-of-the-art in automated code refinement."

## (2) Training-Free Status
**Not specified** in the provided content.

## (3) Benchmarks
The abstract mentions "diverse benchmarks" but specific benchmark names are not listed in this excerpt.

## (4) Execution for Property Verification
**Yes.** The methodology "operates by checking high-level program properties" and providing counterexamples, implying execution-based verification.

## (5) Scope: Debugging vs. Generation
**Both.** The work addresses code refinement and debugging, achieving "a bug fix rate 1.4x-1.6x higher than the strongest debugging-based approaches."

## (6) Publication Venue
**No venue listed.** This is a preprint (arXiv:2506.18315, submitted June 2025, revised May 2026).

## Methodology Details (Property Generation & Usage)
The document provides limited specificity. The approach:
- Defines "high-level program properties" (semantic constraints like sorting producing non-decreasing sequences)
- Executes properties against generated code
- Generates "simplest failing counterexample[s]" for feedback
- Emphasizes "structurally minimal" feedback to isolate root causes

**Complete algorithmic details are unavailable** in this arXiv abstract page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88602708-e076-4d60-a29b-b8a496744f23",
  "isSidechain": false,
  "promptId": "9e08ddf0-33d2-4d92-a77f-55540a5b8b2a",
  "type": "user",
  "uuid": "3d8d2511-e92b-47dd-939c-9b815796cce0",
  "toolUseResult": {
    "bytes": 47303,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of arXiv:2506.18315\n\n## (1) Full Abstract\n\n\"LLMs excel at code generation, yet ensuring the functional correctness of their outputs remains a persistent challenge. While recent studies have applied Test-Driven Development (TDD) to refine code, these methods are often undermined by poor feedback quality, stemming from the scarcity of high-quality test cases and noisy signals from auto-generated ones. In this work, we shift the focus from test quantity to feedback quality. We introduce the Property-Generated Solver (PGS), a novel paradigm designed to generate highly effective feedback via two principles: it must be property-oriented, to provide semantic guidance beyond simple I/O mismatches, and structurally minimal, to reduce cognitive load and isolate root causes. PGS operates by checking high-level program properties (e.g., a sorting function must produce a non-decreasing sequence) then providing the simplest failing counterexample to the LLM. By adhering to these principles, this targeted feedback mechanism leads to significant performance gains. Specifically, PGS achieves an improvement of up to 13.4% in pass@1 against other TDD-based methods and an over 64% fix rate on problems where the model initially failed. This property-driven, minimal feedback steers LLMs toward correct and generalizable solutions. Across diverse benchmarks, PGS demonstrates superior performance, achieving a bug fix rate 1.4x-1.6x higher than the strongest debugging-based approaches and establishing a new state-of-the-art in automated code refinement.\"\n\n## (2) Training-Free Status\n**Not specified** in the provided content.\n\n## (3) Benchmarks\nThe abstract mentions \"diverse benchmarks\" but specific benchmark names are not listed in this excerpt.\n\n## (4) Execution for Property Verification\n**Yes.** The methodology \"operates by checking high-level program properties\" and providing counterexamples, implying execution-based verification.\n\n## (5) Scope: Debugging vs. Generation\n**Both.** The work addresses code refinement and debugging, achieving \"a bug fix rate 1.4x-1.6x higher than the strongest debugging-based approaches.\"\n\n## (6) Publication Venue\n**No venue listed.** This is a preprint (arXiv:2506.18315, submitted June 2025, revised May 2026).\n\n## Methodology Details (Property Generation & Usage)\nThe document provides limited specificity. The approach:\n- Defines \"high-level program properties\" (semantic constraints like sorting producing non-decreasing sequences)\n- Executes properties against generated code\n- Generates \"simplest failing counterexample[s]\" for feedback\n- Emphasizes \"structurally minimal\" feedback to isolate root causes\n\n**Complete algorithmic details are unavailable** in this arXiv abstract page.",
    "durationMs": 8818,
    "url": "https://arxiv.org/abs/2506.18315"
  },
  "sourceToolAssistantUUID": "88602708-e076-4d60-a29b-b8a496744f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-12T01:03:05.464Z_

<details><summary>↩ Tool result · `toolu_01PPaZFXvqvJRb7DZgz2kk8f`</summary>

```text
# StoryCoder Overview

## Abstract Summary
StoryCoder transforms code generation questions into coherent natural language narratives rather than using simple rephrasings. The framework consists of "a task overview, constraints, and example test cases, guided by the selected algorithm and genre."

## Methodology
The approach uses **narrative reformulation** rather than traditional structured intermediate representations like abstract syntax trees or formal specifications. It reorganizes fragmented problem information into cohesive story-like descriptions, drawing inspiration from how humans synthesize scattered details.

## Performance Improvements
Testing across 11 models on three benchmarks (HumanEval, LiveCodeBench, CodeForces) showed "consistent improvements, with an average gain of 18.7% in zero-shot pass@10." Beyond accuracy metrics, the framework guides models toward correct algorithmic strategies, reduces implementation errors, and produces more modular code structures.

## Training Requirements
Yes, this is **training-free**. The method operates at inference time through prompt reformulation, requiring no model fine-tuning or retraining. The improvements come purely from how problems are presented to existing models.

The code is publicly available, and the work was accepted to ACL 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9cba3e8-4158-46e8-abd5-7c8f168ee215",
  "isSidechain": false,
  "promptId": "9e08ddf0-33d2-4d92-a77f-55540a5b8b2a",
  "type": "user",
  "uuid": "2c87d22f-7b7b-40fa-81a0-0a2ec60ae0eb",
  "toolUseResult": {
    "bytes": 46800,
    "code": 200,
    "codeText": "OK",
    "result": "# StoryCoder Overview\n\n## Abstract Summary\nStoryCoder transforms code generation questions into coherent natural language narratives rather than using simple rephrasings. The framework consists of \"a task overview, constraints, and example test cases, guided by the selected algorithm and genre.\"\n\n## Methodology\nThe approach uses **narrative reformulation** rather than traditional structured intermediate representations like abstract syntax trees or formal specifications. It reorganizes fragmented problem information into cohesive story-like descriptions, drawing inspiration from how humans synthesize scattered details.\n\n## Performance Improvements\nTesting across 11 models on three benchmarks (HumanEval, LiveCodeBench, CodeForces) showed \"consistent improvements, with an average gain of 18.7% in zero-shot pass@10.\" Beyond accuracy metrics, the framework guides models toward correct algorithmic strategies, reduces implementation errors, and produces more modular code structures.\n\n## Training Requirements\nYes, this is **training-free**. The method operates at inference time through prompt reformulation, requiring no model fine-tuning or retraining. The improvements come purely from how problems are presented to existing models.\n\nThe code is publicly available, and the work was accepted to ACL 2026.",
    "durationMs": 13706,
    "url": "https://arxiv.org/abs/2604.14631"
  },
  "sourceToolAssistantUUID": "a9cba3e8-4158-46e8-abd5-7c8f168ee215",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-12T01:03:28.027Z_

<details><summary>↩ Tool result · `toolu_01FCe73JC3XAazKL3PAHV1PU`</summary>

```text
Here are the answers to your three questions:

---

**1. Is there an ARR submission cycle with deadline around May 25, 2026?**

Yes, confirmed. The **May 2026 ARR cycle** has a submission deadline of **May 25, 2026**. The full timeline for that cycle is:

- Submission deadline: May 25, 2026
- Reviewer registration: May 27, 2026
- Reviews due: June 29, 2026
- Author response: July 7--13, 2026
- Meta-reviews released: July 30, 2026
- Cycle end: August 2, 2026

---

**2. When is the EMNLP 2026 commitment deadline?**

The EMNLP 2026 commitment deadline is **August 2, 2026**. This aligns exactly with the end of the May 2026 ARR cycle, meaning papers submitted to the May 2026 ARR cycle are the last ones eligible for commitment to EMNLP 2026. Other key dates:

- Notification of acceptance: August 20, 2026
- Camera-ready papers due: September 20, 2026

All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

---

**3. Is EMNLP 2026 in Budapest?**

Yes, confirmed. EMNLP 2026 will be held in **Budapest, Hungary**, from **October 24--29, 2026**.

---

Sources:
- [ACL Rolling Review -- Dates and Venues](http://aclrollingreview.org/dates)
- [EMNLP 2026 Official Website](https://2026.emnlp.org/)
- [EMNLP 2026 -- ConferenceDeadlines.com](https://www.conferencedeadlines.com/conference/emnlp)
- [EMNLP 2026 Call for Papers -- PaperPilot](https://www.getpaperpilot.com/deadlines/emnlp-2026.html)

agentId: a33fc0873e29cb96b (use SendMessage with to: 'a33fc0873e29cb96b' to continue this agent)
&lt;usage>total_tokens: 14714
tool_uses: 7
duration_ms: 37940&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ed927e3-506a-45fe-97f3-9295d652f4ca",
  "isSidechain": false,
  "promptId": "9e08ddf0-33d2-4d92-a77f-55540a5b8b2a",
  "type": "user",
  "uuid": "38bf4002-8f8d-41be-b7ea-0f4dc391f776",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the ARR (ACL Rolling Review) submission deadline for May 2026, and the EMNLP 2026 commitment deadline. I need to verify:\n1. Is there an ARR submission cycle with deadline around May 25, 2026?\n2. When is the EMNLP 2026 commitment deadline?\n3. Is EMNLP 2026 in Budapest?\n\nSearch: \"ACL Rolling Review May 2026 submission deadline\"\nSearch: \"EMNLP 2026 dates Budapest commitment deadline\"\nSearch: \"ARR 2026 submission cycles dates\"",
    "agentId": "a33fc0873e29cb96b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the answers to your three questions:\n\n---\n\n**1. Is there an ARR submission cycle with deadline around May 25, 2026?**\n\nYes, confirmed. The **May 2026 ARR cycle** has a submission deadline of **May 25, 2026**. The full timeline for that cycle is:\n\n- Submission deadline: May 25, 2026\n- Reviewer registration: May 27, 2026\n- Reviews due: June 29, 2026\n- Author response: July 7--13, 2026\n- Meta-reviews released: July 30, 2026\n- Cycle end: August 2, 2026\n\n---\n\n**2. When is the EMNLP 2026 commitment deadline?**\n\nThe EMNLP 2026 commitment deadline is **August 2, 2026**. This aligns exactly with the end of the May 2026 ARR cycle, meaning papers submitted to the May 2026 ARR cycle are the last ones eligible for commitment to EMNLP 2026. Other key dates:\n\n- Notification of acceptance: August 20, 2026\n- Camera-ready papers due: September 20, 2026\n\nAll deadlines are 11:59PM UTC-12:00 (\"anywhere on Earth\").\n\n---\n\n**3. Is EMNLP 2026 in Budapest?**\n\nYes, confirmed. EMNLP 2026 will be held in **Budapest, Hungary**, from **October 24--29, 2026**.\n\n---\n\nSources:\n- [ACL Rolling Review -- Dates and Venues](http://aclrollingreview.org/dates)\n- [EMNLP 2026 Official Website](https://2026.emnlp.org/)\n- [EMNLP 2026 -- ConferenceDeadlines.com](https://www.conferencedeadlines.com/conference/emnlp)\n- [EMNLP 2026 Call for Papers -- PaperPilot](https://www.getpaperpilot.com/deadlines/emnlp-2026.html)"
      }
    ],
    "totalDurationMs": 37940,
    "totalTokens": 14714,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 220,
      "cache_creation_input_tokens": 707,
      "cache_read_input_tokens": 13280,
      "output_tokens": 507,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 707
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 220,
          "output_tokens": 507,
          "cache_read_input_tokens": 13280,
          "cache_creation_input_tokens": 707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 707,
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
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "0ed927e3-506a-45fe-97f3-9295d652f4ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-12T01:04:13.707Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me synthesize my findings:

### Critical Finding: PGS (Property-Generated Solver)

PGS (arXiv:2506.18315, June 2025, revised May 2026) is a VERY direct competitor to ExeSpec:
- Uses high-level program properties (not test cases) as feedback
- Executes properties and provides simplest failing counterexample
- Achieves 13.4% improvement in pass@1 over TDD methods
- 1.4-1.6x higher bug fix rate than strongest debugging approaches


- Applies to both generation and debugging tasks

The core overlap is clear: both prioritize properties over tests, leverage execution for verification, and work across generation and debugging without requiring training. However, they diverge in framing—PGS emphasizes property-based testing with minimal counterexamples while ExeSpec structures specifications more comprehensively with pre/postconditions, invariants, and type constraints. ExeSpec also extends further into SWE-bench tasks and cross-file completion, plus it validates the specifications themselves through execution to prevent hallucinated specs, not just using them to test generated code.

ExeSpec's advantages are the richer spec schema and controlled ablation studies isolating each component's contribution. This is a meaningful differentiation point. I can position against PGS by highlighting the multi-task scope, the execution grounding of specs themselves, the more detailed specification structure, and the ablation methodology.

The venue timeline checks out—ARR May 2026 deadline is May 25, and EMNLP 2026 is August 2 in Budapest. On the SWE-bench contamination front, that's a legitimate concern the idea already flags, and I'll need to report held-out test results to address it.

Looking at related work I should cover: StoryCoder from ACL 2026 uses narrative reformulation as a training-free structured reasoning approach with solid zero-shot improvements, and ContractEval's 0% contract satisfaction under standard prompting suggests spec generation quality is a real problem worth solving. Both strengthen the motivation.

The novelty rating of 3 feels right—PGS has the core idea, but execution grounding plus multi-task application plus the schema depth plus ablation design do add meaningful contributions. Feasibility is also a 3 because the timeline is tight at 14-18 days and SWE-bench contamination introduces evaluation risk, though the GPU budget is manageable.

The clarity is strong at 4—the pipeline is well-articulated and the experimental design is honest. Impact lands at 3 because while the multi-task application and ablation would be valuable, the practical gains might be incremental.

This is iteration 4 of 10, so the idea has matured. The core fixes are straightforward: cite PGS and ContractEval properly, sharpen what differentiates this from PGS, address the contamination concern more rigorously, and either justify the model choice or switch to something like Qwen3-Coder. The timeline is the real constraint, but it's doable.

At 3.25, I'm below the 4.0 threshold for a pass. The missing PGS citation is a real problem—EMNLP reviewers would catch that immediately as a gap in related work. But it's fixable with a proper citation and a positioning paragraph that clarifies the distinctions.

I'm second-guessing whether my novelty score of 3 is fair. ExeSpec does have genuine contributions beyond PGS: grounding the specs themselves through execution, applying it across multiple tasks, a comprehensive schema, and the controlled ablation design. The core insight overlaps, but these extensions are substantive. That might push novelty closer to 3.5 or even 4 if I weight the multi-task framing and execution grounding more heavily.

On feasibility, the 14-18 day manual mode estimate does push against the 16-day constraint, so keeping it at 3 feels right. Clarity at 4 is solid—the paper articulates the idea very well. Impact at 3 is reasonable for a moderate but meaningful contribution.

I'm sticking with "revise" and keeping the feedback focused on the actionable items: add the PGS citation, clarify the differentiation, and maybe tighten the timeline estimates slightly.

Now I'm thinking through whether this actually meets EMNLP standards. The work fits their NLP and Code Models track well—it's a rigorous evaluation framework with controlled experiments and honest ablations, which are genuine strengths. The multi-task evaluation is comprehensive. With those fixes, this could genuinely be EMNLP-quality. But at 3.25 average, it's below the 4.0 acceptance threshold, so "revise" is the right call.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38bf4002-8f8d-41be-b7ea-0f4dc391f776",
  "isSidechain": false,
  "requestId": "req_011CawmrpBrxfn96SXCWmVag",
  "type": "assistant",
  "uuid": "99ea6aba-a923-42ff-a155-a7023ea19164",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1a2nLUJayAntZ8rzLR8D6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 291,
      "cache_creation_input_tokens": 4742,
      "cache_read_input_tokens": 46447,
      "output_tokens": 3652,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 291,
          "output_tokens": 3652,
          "cache_read_input_tokens": 46447,
          "cache_creation_input_tokens": 4742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4742
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

_source line 45 · 2026-05-12T01:05:03.136Z_

Now I have a comprehensive picture. Let me synthesize my findings into the final review.

**Key findings from my independent investigation:**

1. **All 8 verified references exist** with correct venues and claims.
2. **Venue/deadline confirmed**: ARR May 25, 2026 → EMNLP 2026 commitment Aug 2, 2026, Budapest.
3. **Critical missing competitor found**: PGS (Property-Generated Solver, arXiv:2506.18315) — uses property-based feedback instead of test cases, achieving 13.4% pass@1 improvement and 1.4-1.6x higher bug fix rate.
4. **SWE-bench Verified is contaminated**: Top score is 93.9%, SWE-bench Pro now recommended (same models score ~46% on Pro vs ~81% on Verified).
5. **ContractEval** shows 0% contract satisfaction under standard prompting — raises questions about spec generation quality.
6. **Qwen3-Coder** now exists; reviewers may question using Qwen2.5-Coder.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "The core insight (property-level specs > test cases for LLM code feedback) is directly shared with PGS (arXiv:2506.18315, June 2025), which uses high-level program properties with minimal counterexamples, achieving 13.4% pass@1 improvement and 1.4-1.6x bug fix rate. ExeSpec adds execution grounding of specs themselves, multi-task application, and comprehensive spec schema, but the fundamental contribution is partially anticipated. 'From Prompts to Properties' (FSE 2025) and 'Preconditions and Postconditions as Design Constraints' (IEEE Access 2024/2025) further erode novelty."},
    "feasibility": {"score": 3, "rationale": "GPU budget (100-150 H100-hours) fits within the 200-hour constraint. However, the manual timeline of 14-18 days exceeds the 16-day constraint at the upper end. SWE-bench Verified is now contaminated (93.9% top score; SWE-bench Pro recommended), adding evaluation risk. ContractEval shows LLMs achieve 0% contract satisfaction under standard prompting, raising concerns about spec generation quality that the paper's execution grounding must overcome."},
    "clarity": {"score": 4, "rationale": "Exceptionally well-structured. The three-stage pipeline, four controlled experimental conditions, and critical spec-component ablation are clearly articulated. The honest framing ('if I/O-only ≈ full specs, novelty collapses') and explicit acknowledgment of limitations (static grounding for cross-file tasks, SWE-bench contamination) demonstrate intellectual rigor."},
    "impact": {"score": 3, "rationale": "If specs genuinely outperform tests across diverse code tasks, this would be a meaningful contribution to inference-time code improvement. However, Self-Spec showed only +2-5pp gains on HumanEval (already saturated), and the training-free constraint limits the method's ceiling. The controlled ablation design and multi-task evaluation framework would be the most durable contribution."}
  },
  "issues": [
    "CRITICAL MISSING COMPETITOR: PGS (Property-Generated Solver, arXiv:2506.18315, June 2025, revised May 2026) uses high-level program properties instead of test cases as feedback for LLM code refinement, with execution-based property verification and minimal counterexample generation. It achieves 13.4% pass@1 improvement over TDD methods and 1.4-1.6x higher bug fix rate. This shares ExeSpec's core insight (properties > tests) and must be cited, compared against, and clearly differentiated.",
    "MISSING RELATED WORK: (1) 'From Prompts to Properties: Rethinking LLM Code Generation with Property-Based Testing' (FSE 2025) directly challenges test-based paradigm in favor of properties; (2) ContractEval/PACT (arXiv:2510.12047) benchmarks LLM contract satisfaction showing 0% under standard prompting, validating the problem but also raising spec generation quality concerns; (3) 'Preconditions and Postconditions as Design Constraints for LLM Code Generation' (IEEE Access 2024/2025) directly studies ExeSpec's premise with controlled experiments; (4) StoryCoder (arXiv:2604.14631, ACL 2026) is another training-free structured intermediate reasoning method achieving 18.7% improvement.",
    "SWE-BENCH VERIFIED CONTAMINATION: The benchmark is now severely contaminated — top score is 93.9% (Claude Mythos), while the same models score only ~46% on SWE-bench Pro. OpenAI has stopped reporting Verified scores. The paper acknowledges contamination but should more seriously consider using SWE-bench Pro as the primary evaluation or running both and comparing. Reporting only Verified results risks reviewer skepticism.",
    "MODEL CURRENCY: Qwen3-Coder has been released since the idea was designed. EMNLP reviewers may question why the paper uses Qwen2.5-Coder-7B/32B rather than the latest version. Either justify the choice (reproducibility, available at experiment time) or update.",
    "SPEC GENERATION QUALITY RISK INSUFFICIENTLY ADDRESSED: ContractEval shows 0% contract satisfaction under standard prompting and only 23-41% with explicit contracts. CodeSpecBench shows 20.2% repo-level success. The paper's execution grounding is meant to catch bad specs, but if >60% of specs fail grounding, the method effectively degrades to 'generate specs → discard most → fall back to whatever survives' — potentially no better than test-only methods with fewer but higher-quality tests. The paper should include analysis of spec survival rates and graceful degradation behavior.",
    "TIMELINE MARGINAL: The manual estimate of 14-18 days with 2 researchers overlaps but can exceed the 16-day deadline. The upper bound should be trimmed to fit. Consider dropping one supplementary benchmark (e.g., RepoBench) to ensure the primary benchmarks are completed thoroughly."
  ],
  "feedback": "This is now a well-structured idea that has improved substantially through four rounds. The controlled experimental design with honest ablations is the strongest aspect. However, one critical competitor was discovered that must be addressed before this can pass:\n\n1. **CITE AND DIFFERENTIATE FROM PGS** (most important): PGS (arXiv:2506.18315) shares ExeSpec's core insight that properties outperform tests as LLM code feedback. Differentiate on: (a) ExeSpec execution-grounds the specs themselves (catches hallucinated specs before use), while PGS assumes properties are correct; (b) ExeSpec applies across 4 task types (generation, debugging, completion, issue resolution), PGS focuses on generation/repair; (c) ExeSpec's comprehensive spec schema (5 component types) vs. PGS's single-property checking; (d) ExeSpec's controlled ablation isolates each spec component's contribution. Add PGS as a fifth baseline condition, or at minimum cite and discuss in Related Work with clear differentiation.\n\n2. **CITE FSE 2025 AND ContractEval**: 'From Prompts to Properties' (FSE 2025) validates the property-vs-test framing from a PBT perspective. ContractEval (arXiv:2510.12047) both validates your problem (LLMs fail at contracts) and raises spec quality concerns — use it to motivate your execution grounding stage.\n\n3. **ADDRESS SWE-BENCH CONTAMINATION SERIOUSLY**: Either (a) add SWE-bench Pro as the primary SE benchmark alongside Verified, or (b) follow the paper's current plan but add a contamination analysis section comparing performance on instances with/without known gold patch exposure. Option (a) is safer but adds implementation effort.\n\n4. **ADD SPEC SURVIVAL RATE ANALYSIS**: Report what fraction of generated specs survive execution grounding by task type and model. If survival is low, analyze whether the surviving specs still provide gains over test-only methods. This directly addresses the CodeSpecBench/ContractEval concern and strengthens the paper's analytical contribution.\n\n5. **JUSTIFY MODEL CHOICE**: Add a sentence noting that Qwen2.5-Coder was selected as the strongest open-source code model available at experiment design time, and that the method is model-agnostic. If time permits, add one data point with a newer model.\n\nThese are all fixable in one more revision round. The idea's core structure, experimental design, and positioning are sound — the main gap is incomplete coverage of the competitive landscape.",
  "reason": "Strong experimental design and clear positioning, but PGS (arXiv:2506.18315) shares the core insight (properties > tests for LLM code feedback) and must be cited and differentiated; SWE-bench contamination and spec quality risks need stronger mitigation."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99ea6aba-a923-42ff-a155-a7023ea19164",
  "isSidechain": false,
  "requestId": "req_011CawmrpBrxfn96SXCWmVag",
  "type": "assistant",
  "uuid": "a4f4631d-a9d4-476f-a281-aa13dfc73d87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D1a2nLUJayAntZ8rzLR8D6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 291,
      "cache_creation_input_tokens": 4742,
      "cache_read_input_tokens": 46447,
      "output_tokens": 3652,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 291,
          "output_tokens": 3652,
          "cache_read_input_tokens": 46447,
          "cache_creation_input_tokens": 4742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4742
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

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a4f4631d-a9d4-476f-a281-aa13dfc73d87",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Execution-grounded behavioral specifications for code reasoning",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a4f4631d-a9d4-476f-a281-aa13dfc73d87",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Execution-grounded behavioral specifications for code reasoning",
  "sessionId": "dfc514ab-163a-43aa-8fe2-f6ee8596621e"
}
```

---
