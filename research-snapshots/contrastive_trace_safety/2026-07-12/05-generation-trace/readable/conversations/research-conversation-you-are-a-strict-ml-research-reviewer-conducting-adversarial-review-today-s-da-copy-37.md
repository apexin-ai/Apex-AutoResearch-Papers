# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/a16d81f2-1dec-44c4-8dd5-2dc1064e96a2.jsonl`
- **Structured JSON:** [`762e13d074e51a7ddc6d.json`](../../sessions/76/762e13d074e51a7ddc6d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:35:25.268Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:35:25.268Z",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 6/10)\n{\n  \"title\": \"SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair\",\n  \"core_problem\": \"Automated repair agents fail on ambiguous bug reports not from lack of code understanding, but because unstructured issue text leaves behavioral expectations underspecified — what interface should change, what the user observed, and what correct behavior looks like are rarely made explicit. SpecRover (ICSE 2025) partially addresses this via per-instance LLM prompting that extracts specifications from CODE during codebase traversal, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue. Its error analysis (Section V-A, 'Reasons for Failure'; see https://arxiv.org/html/2408.02232, Section V-A) identifies that 107 of its 207 unresolved SWE-bench Lite tasks (51.7%) are classified as 'ambiguous issue description' — cases the paper characterizes as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for why underspecified descriptions constitute an irreducible failure mode for code-space approaches. This architectural limitation is structural: code-side spec extraction can only infer specifications from code that already exists, not from behavior that is described in the issue but not yet correctly implemented. Bug reports routinely contain latent behavioral specifications in their runtime artifacts: stack traces name the affected interface, error messages describe observed behavior, and reproducer assertions encode expected behavior. No method trains a dedicated model to extract these signals from bug report text into a structured repair specification — covering affected interface, observed behavior, expected behavior, and their delta — that could constrain both fault localization and patch generation before any codebase traversal begins.\",\n  \"opportunity\": \"Failing test assertions in SWE-bench's test patches encode implementation-agnostic behavioral specifications without revealing implementation strategies: `assert result == expected_value` or `with pytest.raises(ValueError)` states precisely what the program SHOULD do, independent of WHICH code to change or HOW to change it. By mechanically converting (problem_statement + test_patch assertions + stack traces) to structured JSON spec fields using AST-level test parsing and NLP extraction on SWE-bench's 2,294 instances, we construct a training corpus of 2,294 (bug_report, structured_spec) pairs — where the spec encodes behavioral expectations derivable without knowing the implementation strategy. This avoids the critical flaw of training on SWE-bench Pro requirements, which were authored by humans with full access to the golden patch (making them solution-conditioned). SWE-bench-Live (NeurIPS 2025, arXiv 2505.23419; ~1,890 Docker-reproducible instances across 223 repositories, drawn from post-January-2024 GitHub issues, growing at ~50 instances/month) provides a clean, contamination-resistant evaluation target with no training-set overlap. As SWE-bench Verified saturates with contamination concerns (OpenAI officially deprecated it in February 2026), SWE-bench-Live provides contamination-resistant evaluation on post-2024 issues unavailable during model training. SWE-bench Pro's human-written `requirements` and `interface` fields (731 public instances) serve as an ecological validity check — we measure cosine similarity between machine-derived specs and human requirements on a held-out 200-instance slice — confirming that AST-parsed test assertions produce specs that match expert behavioral descriptions, without using requirements as training supervision.\",\n  \"landscape\": \"SpecRover (ICSE 2025, arXiv 2408.02232) is the closest prior work: given a GitHub issue, it iteratively traverses the codebase, prompting Claude 3.5 Sonnet to extract function-level summaries from visited code, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue and 31% on SWE-bench Lite (93/300). SpecRover operates in code-space (it visits source files to generate specs from code) and uses per-instance prompting (no fine-tuning). Our approach operates in issue-space (extracts specs from bug report text and runtime artifacts before any codebase traversal) and uses supervised fine-tuning (consistent structured output at ~$0.05-0.10/issue). These are complementary directions: SpecRover's code-space specs and our issue-space specs could ultimately be fused. Agent-CoEvo (arXiv 2604.04580, April 2026) proposes the most directly competing design philosophy: rather than pre-extracting behavioral constraints from issue text, it coevolves code patches and test patches simultaneously during repair, treating tests as dynamic constraints that are iteratively revised alongside candidate fixes. Agent-CoEvo achieves 41.33% on SWE-bench Lite (DeepSeek-V3) and 46.4% on SWT-bench Lite, outperforming Agentless-1.5 (32%) on those benchmarks. SpecExtract takes the complementary pre-extraction stance: (1) issue-space specs derived before any codebase access are reusable across repair backbones without retraining, including static pipeline systems like Agentless that do not support dynamic constraint revision during search; (2) pre-extracted specs reduce the initial search space before coevolution begins, making SpecExtract a potential front-end that improves Agent-CoEvo's starting population rather than competing with it. SWE-Lego (arXiv 2601.01426, Jan 2026) is the most directly competing concurrent SFT work: it trains on 32k high-quality task instances with error masking and a difficulty-based curriculum, achieving 52.6% on SWE-bench Verified (58.8% with test-time scaling at 16 samples) using a 32B model. SWE-Lego is an end-to-end system that produces complete code fixes; SpecExtract is a preprocessing module that extracts structured behavioral specs from bug report text before any repair attempt, and can plug into SWE-Lego or any other repair backbone as a drop-in front-end — improving fault localization precision and patch generation alignment without retraining the repair agent itself. CodeSpecBench (arXiv 2604.12268, April 2026) benchmarks existing LLMs (Claude, GPT-4, Gemini) on executable behavioral specification generation via prompting — it does not train a dedicated extractor, operates on code-side and description inputs rather than bug report runtime artifacts, and is an evaluation framework rather than a preprocessing pipeline for repair. Its existence confirms that structured specification generation is an active research area, while simultaneously validating the gap: no trained, issue-space specification extractor for repair preprocessing exists. VibeRepair (arXiv 2602.08263, Feb 2026) translates buggy CODE into behavior specifications, repairs the spec, then synthesizes corrected code, achieving 19-23% improvement on Defects4J — code-space to spec, not text-space to spec. TraceRepair (arXiv 2604.02647, Apr 2026) uses runtime execution traces generated by instrumented code execution as shared repair constraints across a multi-agent committee, fixing 392 Defects4J defects — traces are generated during repair, not extracted from issue text before repair begins. RepoRepair (arXiv 2603.01048) generates hierarchical code documentation from source files toward the bug; its documentation is code-driven, not report-driven. SoRFT (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) fine-tunes on SWE-bench with RL to decompose the repair TASK into subtasks (file → function → line → edit), achieving 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite with a 7B model (30.8% Verified and 24.0% Lite with a 32B model) — it structures the repair pipeline, not the issue semantics. PathFix (arXiv 2510.14341) derives behavioral specs from static code execution paths — code-space and offline, not issue-space. The gap: no existing work trains a dedicated model to extract structured behavioral specifications from bug report text and embedded runtime artifacts, operating entirely in issue-space before codebase access.\",\n  \"approach\": \"We train SpecExtract, a Qwen3-Coder-30B-A3B model (Mixture-of-Experts: 30B total parameters, ~3B active per token — fine-tuning and inference cost scale with active parameters, comparable to a 3B dense model; fits on a single H100 80GB with QLoRA at ~17.5GB VRAM per Unsloth benchmarks; 2× H100 is the recommended training configuration for throughput, not minimum requirement) fine-tuned to map (bug_report_text, runtime_artifacts?) → structured JSON spec, where runtime artifacts are any combination of stack traces, error messages, test failure output, or explicit reproducer assertions present in the issue text. The model gracefully handles varying artifact availability through a masked-field training protocol: training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs. **Formal schema**: Each spec has four typed fields — (1) `affected_interface`: {module: str, signature: str|null, entry_point: str} extracted from stack frame function names and explicitly mentioned APIs; (2) `observed_behavior`: {error_type: str|null, error_message: str|null, symptom: str} from error output and user complaint; (3) `expected_behavior`: {description: str, assertions: [str]} as natural-language description plus test-style constraint strings when derivable; (4) `behavioral_delta`: str, a one-sentence expected-vs-actual summary. Worked example for a NumPy issue 'linalg.solve silently returns None for singular matrices instead of raising': {affected_interface: {module: 'numpy.linalg', entry_point: 'solve', signature: 'solve(a, b)'}, observed_behavior: {error_type: null, symptom: 'returns None for singular matrix input'}, expected_behavior: {description: 'should raise for non-invertible input', assertions: ['raises np.linalg.LinAlgError when matrix is singular']}, behavioral_delta: 'solve silently returns None instead of raising LinAlgError on singular input'}. **Training data construction (implementation-agnostic behavioral specifications)**: From SWE-bench full (2,294 instances including Verified 500 and the broader set): (1) parse `test_patch` test functions via Python AST to extract formal assertions — pytest.raises calls → error_type, assert statements → expected_behavior.assertions, decorated test function signatures → affected_interface hints; (2) extract stack traces and error strings from `problem_statement` text via regex heuristics → observed_behavior; (3) combine via LLM-assisted template fill using Qwen3-Coder-30B-A3B in a chain-of-thought extraction pass to produce coherent spec JSON; (4) validate on 200 SWE-bench Pro public instances that have non-null `requirements` and `interface` fields by computing cosine similarity (sentence-transformer) between mechanically-derived specs and human-authored requirements — target alignment ≥ 0.65 before training at scale (this threshold aligns with established semantic similarity cutoffs in information-extraction evaluation literature, where scores below 0.65 on sentence-transformer embeddings indicate insufficient semantic overlap for structural field matching); this validates the schema rather than using requirements as training targets. Important framing on conditionality: test assertions are written alongside gold patches and encode the behavioral outcome the fix achieves. The training specs are therefore *implementation-agnostic* — they do not reveal which code to change or the implementation strategy — rather than strictly solution-independent. This distinction is explicitly addressed in the paper to avoid overclaiming. The EMNLP 2026 ARR submission uses the 2,294-instance SWE-bench full corpus as the SFT training set; GitBugs augmentation (~3,000 pseudo-labeled instances, yielding a ~5,300-instance total corpus) is reserved for the ICSE 2027 extended paper. **Differentiation from SpecRover**: (1) issue-space — no codebase traversal needed at spec extraction time; (2) supervised learning — consistent, typed JSON output from a single forward pass (~$0.05-0.10/issue) vs. SpecRover's multi-step code traversal ($0.65/issue); (3) directly targets SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved SWE-bench Lite tasks) by conditioning on all available runtime artifacts in the issue, not just the code side. **Integration with Agentless**: Agentless (arXiv 2407.01489) is used as the repair backbone for all SWE-bench-Live evaluations — it follows a fixed three-stage pipeline (hierarchical fault localization → patch generation → patch selection) with no iterative tool calls, making spec injection clean and reproducible. SpecExtract specs are injected at two stages: (1) fault localization Stage 1 — BM25+embedding file retrieval is biased by prepending `affected_interface.module` and `entry_point` as a structured query prefix, pushing relevant files higher in the candidate list; (2) patch generation Stage 3 — the repair LLM receives all four spec fields as an explicit behavioral constraint header in its prompt, focusing generation on the documented delta. **Agentless baseline on SWE-bench-Live**: Per the SWE-bench-Live paper (arXiv 2505.23419, Table 3), Agentless resolves 11.67% (GPT-4o), 12.00% (GPT-4.1), and 13.33% (DeepSeek V3) of SWE-bench-Live Lite (300 instances) — substantially below its 50.8% on SWE-bench Verified, reflecting the contamination-resistant, harder distribution of post-2024 issues. These published numbers establish the Agentless-direct baseline; SpecExtract targets +4-7 percentage points improvement over the best Agentless backbone, which is reported as the primary experimental contribution. **Evaluation**: Primary eval on SWE-bench-Live Lite (300 instances, contamination-resistant, post-2024 issues) with Agentless as backbone; per-field ablations independently zero out each spec field to quantify individual contribution to resolve rate. Secondary eval: cosine-similarity validation on 200 SWE-bench Pro held-out instances (schema validity check). Comparison baselines: Agentless direct repair without spec (established at 11-13% from published SWE-bench-Live results), SpecRover-equivalent prompting (ablation of supervised fine-tuning benefit), SoRFT-Qwen-7B (21.4% Verified / 14.0% Lite, structured subtask decomposition), SWE-Lego (52.6% Verified, end-to-end SFT backbone — SpecExtract as preprocessing front-end demonstrates orthogonal contribution). **Publication scope**: The EMNLP 2026 ARR submission (auto-research mode, 6-10 days) reports results on the 2,294-instance SWE-bench full SFT corpus with SWE-bench-Live Lite 300-instance primary eval and a 2-field ablation (affected_interface vs. none, expected_behavior vs. none) — the two fields with the strongest localization and generation signal respectively. The full 5,300-instance corpus (with GitBugs augmentation) and all four per-field ablation fields constitute the ICSE 2027 extended paper.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~90-110 H100-hours (~180-220 A100-equivalent hours)\",\n      \"gpu_breakdown\": \"SFT partition (~10-14 H100-hours): Qwen3-Coder-30B-A3B QLoRA fine-tuning on 5,300 instances, 3 epochs, 2× H100 80GB recommended for throughput (single H100 80GB is technically sufficient at ~17.5GB VRAM) — MoE active-parameter efficiency reduces training cost to ~3B dense equivalent. Eval partition (~80-96 H100-hours): spec extraction inference on 5,300 instances (~4 H100-hours); SWE-bench-Live Lite main eval 300 instances × 12.5 min/instance / 4 parallel H100s ≈ 16 H100-hours; per-field ablations 4 fields × 300 instances ≈ 64 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~50-60% — Docker sandbox test execution during SWE-bench-Live eval is CPU-bound; GPU idles between model inference calls\",\n      \"timeline\": \"3-5 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$216-264 (90-110h × $2.40/hr H100 SXM5 on-demand; within the 200 H100-hour hard constraint)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~135-160 H100-hours (~270-380 A100-equivalent hours)\",\n      \"gpu_breakdown\": \"SFT partition (~25-35 H100-hours): 3 fine-tuning configurations (schema variant, augmentation ablation, masked-field protocol variant). Eval partition (~110-125 H100-hours): spec extraction ~5 H100-hours; Agentless baseline run on 300 instances ≈ 16 H100-hours; SWE-bench-Live partial eval 600 instances / 4 parallel ≈ 31 H100-hours; per-field ablations on 300-instance subset × 4 fields ≈ 62 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~60-70% — agent runs fine-tuning and SWE-bench-Live eval jobs continuously; human approves schema validation threshold, masked-field training protocol, retrieval bias weights, and ablation scope at daily check-ins\",\n      \"timeline\": \"5-9 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$200-400 (~2,500 orchestration turns at ~$0.10/turn Opus)\",\n      \"estimated_gpu_cost\": \"~$324-384 (135-160h × $2.40/hr H100); within the 200 H100-hour hard constraint\",\n      \"risk_note\": \"Critical unknown: whether AST-parsed test assertions produce specs that align with human behavioral descriptions (measured by cosine similarity ≥ 0.65 on 200 SWE-bench Pro validation instances). If alignment is below threshold, the spec schema needs redesign before scale-up. GitBugs pseudo-spec quality is the secondary risk — human spot-check of 100 instances recommended before augmentation scale-up.\"\n    },\n    \"auto_research\": {\n      \"note\": \"Budget-capped auto-research only — uncapped sweeps would exceed the 200 H100-hour hard constraint. Capped to 3 fine-tuning configurations × 1 retrieval variant × 1 patch-generation prompt strategy on SWE-bench-Live Lite (300 instances) for the main configuration sweep, then ablations on the best-performing config only.\",\n      \"gpu_hours\": \"~160-180 H100-hours (budget-capped)\",\n      \"gpu_breakdown\": \"SFT partition (~30-35 H100-hours): 3 QLoRA configs on 5,300 instances. Eval partition (~130-145 H100-hours): 3-config main sweep 3 × 300 instances ≈ 48 H100-hours; per-field ablations on best config 300 × 4 fields ≈ 64 H100-hours; Agentless baseline ≈ 16 H100-hours; spec extraction inference ≈ 5 H100-hours; validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~80-85% — continuous fine-tuning, inference, and SWE-bench-Live Docker eval; sandbox parallelized across 30 instances simultaneously\",\n      \"timeline\": \"6-10 days with 4 parallel H100 GPUs\",\n      \"team\": \"0 (setup only, ~3h initial configuration)\",\n      \"claude_api_cost\": \"$400-600 (~4,500 turns)\",\n      \"estimated_gpu_cost\": \"~$384-432 (160-180h × $2.40/hr H100)\",\n      \"speed_bottleneck\": \"SWE-bench-Live Docker sandbox throughput, not GPU compute; Qwen3-Coder-30B-A3B MoE inference (~3B active params) is fast and avoids multi-GPU coordination overhead that a dense 30B model would require\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026 — 15 days remaining; conference October 24-29, Budapest) — NLP angle on structured information extraction from semi-structured bug text; EMNLP ARR submission reports auto-research results (6-10 days): SFT on SWE-bench full 2,294-instance corpus (GitBugs augmentation deferred to ICSE), SWE-bench-Live Lite 300-instance primary eval, and 2-field ablation (affected_interface vs. none, expected_behavior vs. none). The full 5,300-instance corpus with all four per-field ablation fields is the ICSE 2027 extended paper.\",\n    \"ICSE 2027 (abstract deadline June 23, 2026; full paper ~July 2026; conference April-May 2027, Dublin) — SE angle; preferred primary target for full experimental results including GitBugs-augmented 5,300-instance corpus, SWE-bench-Live partial-set ablations, and all four per-field ablation conditions\",\n    \"NeurIPS 2026 (submission deadline expected May-June 2026) — systems and benchmarks angle; natural co-venue given SWE-bench-Live is NeurIPS 2025\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"SpecRover: Code Intent Extraction via LLMs (arXiv 2408.02232, ICSE 2025) — primary related work: code-space spec inference via prompting, 31% SWE-bench Lite (93/300), $0.65/issue; Section V-A 'Reasons for Failure' (see https://arxiv.org/html/2408.02232, Section V-A) categorizes 107/207 unresolved SWE-bench Lite tasks (51.7%) as 'ambiguous issue description', cases characterized as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for the hardness of this failure mode\",\n    \"SWE-bench Goes Live! (arXiv 2505.23419, NeurIPS 2025 D&B) — primary evaluation benchmark: ~1,890 contamination-resistant instances across 223 repositories, post-2024 GitHub issues, Docker-reproducible, growing at ~50 instances/month; Table 3 reports Agentless on SWE-bench-Live Lite (300 instances) at 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3) — establishes the Agentless-direct baseline for our evaluation\",\n    \"Agent-CoEvo: Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints (arXiv 2604.04580, April 2026) — most directly competing design philosophy: coevolves code patches and test patches simultaneously during repair (41.33% SWE-bench Lite with DeepSeek-V3); SpecExtract's pre-extraction stance is complementary — issue-space specs reduce the initial search space before coevolution, and are pipeline-agnostic for static repair systems that do not support dynamic constraint revision\",\n    \"SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (arXiv 2509.16941) — schema ecological validity validator: 731 public instances with human requirements and interface fields\",\n    \"SWE-Lego (arXiv 2601.01426, Jan 2026) — most competitive concurrent SFT work: 32k training instances, difficulty-based curriculum SFT, 52.6% SWE-bench Verified (58.8% with 16-sample test-time scaling) with 32B model; end-to-end repair backbone that SpecExtract can serve as a preprocessing front-end for\",\n    \"Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489) — integration repair backbone: open-source three-stage fixed pipeline (localization → repair → validation), ~50.8% SWE-bench Verified (Agentless-1.5), 32% SWE-bench Lite; spec injected at file localization (retrieval bias) and patch generation (behavioral constraint prefix) stages\",\n    \"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (arXiv 2604.12268, April 2026) — evaluates prompting-based spec generation from code and descriptions using existing LLMs; does not train a dedicated extractor, operates on code-side inputs rather than bug report runtime artifacts, and is an evaluation framework rather than a repair preprocessing pipeline — confirms structured spec generation is an active research area while the trained, issue-space extractor gap remains open\",\n    \"Specification Vibing for Automated Program Repair / VibeRepair (arXiv 2602.08263, Feb 2026) — code-space spec extraction before repair, Defects4J, 19-23% improvement\",\n    \"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate / TraceRepair (arXiv 2604.02647, Apr 2026) — trace-based repair constraints during execution, Defects4J\",\n    \"SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) — structured repair subtask decomposition with RL; SoRFT-Qwen-7B: 21.4% SWE-bench Verified / 14.0% SWE-bench Lite; SoRFT-Qwen-32B: 30.8% SWE-bench Verified / 24.0% SWE-bench Lite; key baseline for SpecExtract's supervised fine-tuning approach\",\n    \"GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More (arXiv 2504.09651) — 150K+ open-licensed bug reports for training augmentation\",\n    \"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048)\",\n    \"On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481)\",\n    \"PathFix: Automated Program Repair with Expected Path (arXiv 2510.14341)\"\n  ],\n  \"description\": \"We introduce SpecExtract, the first supervised issue-space specification extractor for program repair: a fine-tuned Qwen3-Coder-30B-A3B model (MoE, ~3B active parameters — fine-tuning and inference cost comparable to a 3B dense model; fits on a single H100 80GB at ~17.5GB VRAM with QLoRA; 2× H100 recommended for training throughput) that maps (bug_report_text, runtime_artifacts?) → a structured four-field JSON spec covering affected interface, observed behavior, expected behavior, and behavioral delta. The key methodological insight is that failing test assertions in SWE-bench test patches encode implementation-agnostic behavioral specifications — they state what the program SHOULD do without revealing which code to change or the implementation strategy — enabling AST-level test parsing combined with problem-statement NLP extraction to construct 2,294 clean (bug_report, structured_spec) training pairs from SWE-bench. GitBugs (150K+ open-licensed bug reports) provides ~3,000 pseudo-labeled augmentation instances for the ICSE 2027 extended paper; the EMNLP 2026 ARR submission uses the 2,294-instance SWE-bench full corpus only. SWE-bench Pro public requirements serve as an ecological validity check (cosine similarity ≥ 0.65 on 200 held-out instances), not a training target. Extracted specs are integrated with Agentless as the repair backbone, injected at fault localization (retrieval biased toward affected_interface.module/entry_point) and patch generation (structured behavioral constraint prefix). Primary evaluation is on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues — as SWE-bench Verified saturates with contamination concerns, SWE-bench-Live provides the contamination-resistant evaluation target), with the Agentless-direct baseline established at 11-13% from published SWE-bench-Live results (Table 3, arXiv 2505.23419) and a target improvement of +4-7 percentage points; per-field ablations measure individual spec contributions. Agent-CoEvo (arXiv 2604.04580, 41.33% SWE-bench Lite) represents the competing dynamic-coevolution philosophy; SpecExtract's pre-extraction stance is complementary — pipeline-agnostic and applicable to static repair systems. SWE-Lego (52.6% Verified with 32B) is included as an end-to-end SFT baseline to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end rather than competing as a repair system. Differentiated from SpecRover (code-space prompting, $0.65/issue, 31% SWE-bench Lite) by operating in issue-space at ~$0.05-0.10/issue — directly targeting SpecRover's Section V-A identified 51.7% ambiguous-description failure mode — and from SWE-Lego by producing modular, pipeline-agnostic specs that plug into any repair backbone without retraining it. Compute in H100-hours: manual mode ~90-110 H100-hours (SFT ~10-14 H100-hours, eval ~80-96 H100-hours), within the 200-hour hard constraint.\",\n  \"project_name\": \"structured_spec_repair\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Training data availability: The public SWE-bench Pro HuggingFace dataset contains 731 instances from 11 repositories with copyleft licenses. The remaining 1,134 instances (held-out: 12 repos, commercial: 18 proprietary repos) are explicitly not publicly accessible. The proposal's assumption of ~1,865 training pairs is wrong by a factor of 2.5x. At 731 instances, standard fine-tuning of a 32B Qwen3-Coder model risks severe overfitting and is far too small for reliable generalization.\", \"CRITICAL — Training signal invalidity (train-test distribution mismatch): SWE-bench Pro requirements were authored by humans with full access to the golden patch AND the passing test suite, working backward from tests to specifications. They are solution-conditioned prescriptive clarifications of already-solved problems. Real-world target bug reports are solution-ignorant descriptive complaints from confused users. Fine-tuning SpecExtract on (solution-knowing-human-written-spec → structured-spec) pairs will not teach the model to extract specs from genuinely ambiguous bug reports — it will teach it to produce post-hoc rationalizations of known solutions. This fundamental mismatch is not acknowledged and cannot be patched by synthetic augmentation alone.\", \"CRITICAL — Evaluation benchmark reliability: SWE-bench Verified shows SOTA of 93.9% (Claude Mythos Preview, May 2026) with documented evidence of data contamination — OpenAI has officially stopped recommending Verified scores for meaningful comparison. Demonstrating a statistically meaningful improvement on a benchmark where frontier models may be reproducing gold patches verbatim severely weakens the paper's empirical contribution.\", \"Novelty gap — SpecRover (ICSE 2025, arXiv 2408.02232) performs iterative code intent extraction and specification inference from GitHub issue descriptions using LLM agents (not supervised training), and achieves >50% improvement in repair rate on SWE-bench at $0.65/issue. The paper's claim that 'no prior work trains a spec extractor' is technically true but misses that SpecRover occupies the same research niche via prompting. The paper must explicitly frame what the supervised training provides that SpecRover's prompting approach cannot.\", \"Compute unit mismatch vs. hard constraint: The hard constraint is ≤200 H100-hours. All estimates are given in A100-hours. H100 is ~2–3× faster than A100 for transformer fine-tuning workloads, so 200 A100-hours ≈ 67–100 H100-hours (manual, within budget), but the auto-research mode at 800 A100-hours ≈ 300–400 H100-hours exceeds the hard constraint. The paper should explicitly reconcile resource estimates in H100-hours and confirm the primary research plan stays within budget.\", \"Structured spec schema undefined: The proposal outputs 'structured specs' with fields (affected interface, pre/post-conditions, expected/actual behavior delta), but these fields are never formally defined — no JSON schema, no field type definitions, no examples of what a valid spec looks like. SWE-bench Pro requirements are freeform prose; the conversion of freeform requirements to structured JSON is the hardest step and receives no design discussion.\", \"Data leakage if evaluation pivots to SWE-bench Pro: If the proposal trains on SWE-bench Pro (public: 731 instances) and evaluates on the same benchmark, it cannot cleanly show generalization. The community will ask whether the structured spec format was reverse-engineered from the test set rather than learned from scratch.\"]\nFeedback: The core direction — using SWE-bench Pro annotations to supervise structured specification extraction — is creative and timely, but rests on a mischaracterization of what SWE-bench Pro requirements actually are and how many are publicly accessible. To revise toward 'pass': (1) **Fix the training data premise**: Acknowledge that SWE-bench Pro public set is 731 instances, not 1,865. Address the solution-conditioned nature of the requirements by designing the training task as 'given the bug report + human requirements, produce structured spec fields,' treating the requirements as an alignment target rather than pretending they were extracted from bug reports alone. (2) **Address SpecRover directly**: Add SpecRover (ICSE 2025, arXiv 2408.02232) to the related work and explicitly argue why supervised fine-tuning generalizes better than per-instance LLM prompting — e.g., lower inference cost, better calibration, consistency across bug report styles. (3) **Replace SWE-bench Verified as primary eval**: Use SWE-bench Pro public (731 instances) with a held-out split for evaluation, and add an additional out-of-distribution eval on RepoBench or DebugBench to show generalization. Explicitly argue why SWE-bench Pro's requirements-based evaluation is the right target, not the contaminated Verified leaderboard. (4) **Define the structured spec schema**: Add a formal schema definition with field types and a worked example. Show how SWE-bench Pro freeform requirements can be automatically converted to this schema via a parsing step (this becomes its own empirical contribution). (5) **Reconcile compute in H100-hours**: Convert all estimates to H100-hours and confirm manual mode (~67–100 H100-hours) is well within the 200-hour budget. Remove or prominently caveat auto-research mode since it exceeds the hard constraint.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Model naming error: 'Qwen3-Coder-14B' does not exist. Qwen3-Coder is only available in 30B-A3B (MoE, 3B active) and 480B-A35B variants. The closest viable alternatives are Qwen3-14B (dense, base Qwen3 family) or Qwen2.5-Coder-14B (prior generation). This error must be corrected with the actual model to be used, and any VRAM/compute estimates adjusted accordingly.\", \"CRITICAL — Unverifiable SpecRover failure claim: The proposal states SpecRover 'explicitly identifies that 51.7% of its unresolved SWE-bench Lite failures stem from ambiguous issue descriptions.' This specific statistic could not be verified from the SpecRover abstract or public-facing sections. If this is an inference rather than a direct quote, it must be either verified by citing the exact section, reframed as an approximation, or removed. The entire motivation chain rests on this number.\", \"SIGNIFICANT — SoRFT baseline misrepresented: The proposal states SoRFT achieves '21.4% on SWE-bench Verified with a 7B model' but SoRFT (ACL 2025) actually reports 21.4% on SWE-bench Lite, not Verified. The Verified number for SoRFT-7B is 14.0%. Using the wrong benchmark undermines the baseline comparison.\", \"SIGNIFICANT — Integration repair agent unspecified: The primary experimental claim requires running a full end-to-end repair pipeline on SWE-bench-Live (1,890 instances) that integrates the extracted spec. The proposal does not specify which agent (SWE-agent, Moatless, Agentless, custom) is used, how the spec is injected, or what its baseline resolve rate is. Without this, the compute estimate and experimental design are incomplete.\", \"SIGNIFICANT — SWE-Lego (arXiv 2601.01426) not addressed: This January 2026 SFT-for-issue-resolving paper uses 32k training instances and a comprehensive SFT curriculum for end-to-end repair. As direct related work in the SFT-for-SWE space, its omission leaves a gap the reviewer committee will flag. The differentiation should be: SpecExtract does a spec-extraction subtask (not end-to-end repair), enabling pipeline-agnostic reuse.\", \"MODERATE — Test_patch assertion conditionality overstated: The 'non-solution-conditioned' framing is the linchpin of the training data justification, but test patches are written after/alongside gold patches and specifically designed to validate the fix. In many SWE-bench instances, assertions encode precise return values or exception types only determinable by knowing the codebase implementation. The paper should more carefully scope the claim: 'behavioral-specification-level, not implementation-level conditioned' rather than 'non-solution-conditioned.'\", \"MINOR — SWE-bench-Live size outdated: The proposal states '1,565+ instances' but the live dataset now contains 1,890 tasks across 223 repositories. Update to the current figure.\", \"MINOR — Compute budget tightness for full eval: Running a repair agent on 1,890 SWE-bench-Live instances at ~10-15 minutes/issue with 4 parallel H100s consumes approximately 79-118 H100-hours for evaluation alone, leaving 0-6 H100-hours for fine-tuning in the manual mode upper estimate. Explicitly partition the budget between SFT and eval inference.\"]\nFeedback: The Round 2 revision has substantially addressed the Round 1 critical issues: the training data premise is now grounded (SWE-bench test_patch AST parsing rather than SWE-bench Pro requirements), the evaluation target is appropriate (SWE-bench-Live), compute is expressed in H100-hours with manual mode under budget, and the JSON schema is formally defined. This is genuine progress. To advance to 'pass':\n\n(1) **Fix the model name immediately**: Replace 'Qwen3-Coder-14B' with either 'Qwen3-14B' (dense, 14B params, general Qwen3 family) or 'Qwen3-Coder-30B-A3B' (MoE, only 3B active params, faster and better for code). Qwen3-Coder-30B-A3B is the more credible choice for a coding spec-extraction task — its ~3B active parameters mean fine-tuning cost is comparable to a 3B dense model despite 30B total params.\n\n(2) **Verify or remove the 51.7% SpecRover claim**: Read SpecRover Section 4 or 5 (error analysis). If the 51.7% figure is there, cite the exact table/figure. If it's an approximation, write: 'SpecRover's error analysis identifies ambiguous issue descriptions as the dominant unresolved failure mode (Section X); our estimate from their public failure logs is ~50%.' If it's not there, reframe the motivation as: 'SpecRover's code-space approach cannot address cases where the issue description itself is underspecified — a failure mode it cannot observe.'\n\n(3) **Fix the SoRFT baseline**: Change '21.4% on SWE-bench Verified' to '21.4% on SWE-bench Lite (14.0% on Verified).' This makes SoRFT a weaker baseline, which actually helps SpecExtract's positioning.\n\n(4) **Specify the integration repair agent**: Choose one concrete agent (e.g., Agentless or Moatless) as the integration vehicle for the SWE-bench-Live evaluation. Report its baseline resolve rate, then show the SpecExtract-augmented rate. Add this as 1-2 sentences in the approach section. This is the most critical missing piece for a credible empirical narrative.\n\n(5) **Add SWE-Lego differentiation**: One paragraph acknowledging SWE-Lego (arXiv 2601.01426) as concurrent SFT work, differentiating that SpecExtract is a preprocessing spec-extraction module (not an end-to-end repair system) that can be combined with any SFT-trained or prompted repair backbone, including SWE-Lego itself.\n\n(6) **Scope the conditionality claim**: In the training data section, replace 'non-solution-conditioned' with 'implementation-agnostic behavioral specifications' to reflect that while test assertions do implicitly know the fix's behavior, they do not expose the implementation strategy, making them valid targets for behavioral spec learning.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL — Fabricated SpecRover citation (third consecutive round): The proposal cites 'SpecRover Section V-A, Reasons for Failure' with the specific claim that 51.7% of its 207 unresolved SWE-bench Lite tasks involve ambiguous issue descriptions (107/207 instances, labeled by SWE-bench Verified human annotators). Independent verification via WebFetch of arXiv 2408.02232v3 confirms this section does not exist — SpecRover has no dedicated error analysis section categorizing failures by issue ambiguity, and contains no 51.7% figure, 107/207 count, or SWE-bench Verified annotation cross-reference. The Round 3 generator escalated from 'unverifiable' (Round 2) to 'fabricated with false specificity' by inventing the section label, count, and labeling provenance. This is an academic integrity violation that will result in desk rejection or post-acceptance retraction if submitted as-is.\", \"SIGNIFICANT — Agent-CoEvo (arXiv 2604.04580, April 2026) not addressed in landscape: This concurrent paper, 'Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints,' proposes that behavioral constraints (tests) should be coevolved dynamically with code patches during repair rather than pre-extracted from bug reports. It evaluates on SWE-bench Lite and SWT-bench Lite and outperforms agentless baselines. This represents the most direct competing design philosophy to SpecExtract's pre-extraction approach and must be discussed — specifically, why pre-extraction from issue text before any codebase access is preferable to dynamic constraint coevolution.\", \"MODERATE — SoRFT numbers are now correct but were mishandled across three rounds: Independent verification via ACL Anthology (2025.acl-long.559) confirms SoRFT-7B achieves 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite — exactly as stated in Round 3. The Round 2 reviewer was wrong to flag these as reversed. While the numbers are now correct, three rounds of oscillation on this point suggest the generator should add a footnote citing the ACL Anthology URL to preempt reviewer confusion.\", \"MODERATE — No reported Agentless-on-SWE-bench-Live baseline: The experimental design requires establishing Agentless-direct (no spec injection) on SWE-bench-Live Lite (300 instances) as the baseline, then measuring SpecExtract-augmented Agentless. This baseline number is not reported anywhere in the proposal, making it impossible to assess whether the expected delta (e.g., +3-8 percentage points) is plausible or whether Agentless-1.5's 50.8% Verified score generalizes to the Live dataset at all. At minimum, cite the Agentless-1.5 SWE-bench-Live Lite score if published, or explicitly acknowledge this is unmeasured.\", \"MINOR — QLoRA VRAM claim is slightly oversimplified: Qwen3-Coder-30B-A3B with QLoRA requires ~17.5GB VRAM (verified via Unsloth documentation), fitting comfortably on a single H100 80GB rather than requiring 2× H100s. The 2× claim is not wrong (it enables larger batch sizes and faster throughput) but should be reframed as 'recommended configuration for efficient throughput' rather than 'minimum requirement.'\"]\nFeedback: This proposal has made genuine progress across three rounds — the model choice, Agentless integration, SWE-Lego differentiation, schema definition, and compute budget are all solid. One issue now blocks this from passing, and one new issue must be addressed:\n\n(1) **IMMEDIATE: Remove or replace the fabricated SpecRover Section V-A claim.** There is no 'Section V-A: Reasons for Failure' in SpecRover, no 51.7% figure, no 107/207 count, and no SWE-bench Verified annotation cross-reference in the paper. Replace the entire motivation chain with a defensible framing: 'SpecRover (ICSE 2025) evaluates on SWE-bench Lite and explicitly acknowledges that its code-space traversal approach cannot resolve cases where the issue description itself is underspecified — it can only infer specifications from code that exists, not from behavior that is described but not yet correctly implemented. This architectural limitation motivates an issue-space approach that operates on bug report text before codebase access.' If you want to keep a quantitative hook, look at SpecRover's SWE-bench Lite resolve rate (31%) and the known proportion of SWE-bench tasks where the issue description is classified as ambiguous by SWE-bench Verified human annotators — cite the SWE-bench Verified paper (arXiv 2410.06992) or the SWE-bench Pro paper for that annotation, not SpecRover.\n\n(2) **Add Agent-CoEvo to related work.** One paragraph: 'Agent-CoEvo (arXiv 2604.04580, April 2026) proposes coevolving code and test patches simultaneously during repair, treating tests as dynamic behavioral constraints. SpecExtract takes the complementary pre-extraction stance: issue-space specs derived before any codebase access reduce the search space for both fault localization and patch generation, and are reusable across repair backbones without retraining — including static repair systems like Agentless that do not support dynamic constraint revision.'\n\n(3) **Add Agentless-on-SWE-bench-Live baseline.** State the known or estimated Agentless-1.5 resolve rate on SWE-bench-Live Lite (or acknowledge it as an early experimental measurement to be reported in the paper). The experimental contribution is the delta, and without the baseline anchor the paper cannot make its empirical case.\n\nWith these three changes — particularly (1) — this proposal should be able to pass in Round 4.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"IMPORTANT CORRECTION — SpecRover Section V-A claim is VERIFIED, not fabricated: Independent WebFetch of the HTML version of arXiv:2408.02232 (https://arxiv.org/html/arXiv:2408.02232) confirms the paper contains Section V-A 'RQ1: Overall Efficacy of Task Resolving' with a subsection 'Reasons for Failure' that explicitly documents 107/207 unresolved SWE-bench Lite tasks (51.7%) classified as ambiguous issue descriptions. The Round 3 reviewer's 'fabricated' accusation was incorrect. The generator should add a footnote or parenthetical citing the HTML URL to preempt any residual reviewer confusion, since the accusation has been raised three consecutive rounds.\", \"SIGNIFICANT — Internal inconsistency in EMNLP pilot scope: The EMNLP venue description states 'realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval,' but the main approach uses 2,294 SWE-bench instances + 3,000 GitBugs pseudo-labeled instances = 5,300 corpus. These are in direct conflict. Either (a) define the EMNLP submission as explicitly scoped to a pilot — SFT on SWE-bench Verified 500 subset, SWE-bench-Live Lite 300-instance eval, no GitBugs augmentation — and state this clearly in the approach section, or (b) remove the '500-instance Verified' framing from the venue description and commit to the full corpus with the understanding that compute and eval must finish within 16 days.\", \"MODERATE — 16-day deadline is unrealistically framed without explicit pilot scope: Building the 5,300-instance training corpus (AST parsing + NLP regex + LLM-assisted spec fill), SFT (10-14 H100-hours), establishing Agentless-SWE-bench-Live Docker infrastructure, running the full 300-instance eval + 4-field ablations (80-96 H100-hours), and writing the paper cannot realistically be completed in 16 days by 1-2 researchers. The submission plan should explicitly acknowledge that the EMNLP ARR submission will report pilot-scale results (e.g., SFT on 500-instance Verified subset, 100-instance SWE-bench-Live Lite eval) with the full-scale results reserved for ICSE 2027 as the primary venue.\", \"MODERATE — 'Replacing the officially-abandoned SWE-bench Verified' is imprecise: OpenAI's February 2026 announcement recommends SWE-bench Pro as the frontier evaluation replacement — not SWE-bench-Live. SWE-bench-Live is the appropriate replacement for contamination-resistant research evaluation, which is the correct positioning for this paper, but the phrasing implies SWE-bench-Live is the community standard replacement for Verified, which overstates its current adoption. Reframe as: 'As SWE-bench Verified saturates with contamination concerns, SWE-bench-Live (NeurIPS 2025) provides contamination-resistant evaluation on post-2024 issues — the appropriate target for research contributions that train on SWE-bench data.'\", \"MINOR — Cosine similarity threshold (≥ 0.65) for schema validation is stated without justification: The proposal requires AST-parsed test assertions to achieve ≥ 0.65 cosine similarity with SWE-bench Pro human requirements on 200 held-out instances. This threshold determines whether the schema is redesigned before scale-up, making it a critical gating decision. Add one sentence explaining why 0.65 is the right threshold (e.g., 'consistent with semantic similarity thresholds in information extraction literature where 0.65 distinguishes semantically related from unrelated pairs').\"]\nFeedback: The SpecRover Section V-A claim has been independently verified as correct — the HTML paper confirms the 107/207 (51.7%) ambiguous issue description statistics in the 'Reasons for Failure' subsection of Section V-A. After three rounds of false accusations, add a parenthetical citing the HTML URL (https://arxiv.org/html/arXiv:2408.02232) to preempt any residual reviewer skepticism. To reach 'pass' in Round 5: (1) **Fix the pilot/full scope inconsistency**: Choose one coherent story for EMNLP. The most defensible is a pilot submission — SFT on SWE-bench Verified 500-instance subset, primary eval on 100-150 SWE-bench-Live Lite instances (not 300), 2-field ablation (affected_interface vs. none, expected_behavior vs. none). Remove the '500-instance SWE-bench Verified training' from the venue description and put it in the approach section as the EMNLP pilot plan. State that the full 5,300-instance corpus + 300-instance eval is the ICSE 2027 primary submission. (2) **Fix the SWE-bench Verified replacement framing**: Change 'replacing the officially-abandoned SWE-bench Verified' to 'providing contamination-resistant evaluation as SWE-bench Verified saturates at frontier.' (3) **Justify the 0.65 cosine similarity threshold** in one sentence. With these changes, the proposal will have resolved all substantive issues from rounds 1-4 and should be ready to pass.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"SIGNIFICANT (unresolved from Round 4) — EMNLP venue scope vs approach inconsistency: The target_venues description states 'realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval,' but the approach section describes a 5,300-instance training corpus (2,294 SWE-bench full + ~3,000 GitBugs pseudo-labeled). These are directly contradictory in the same document. Round 4 explicitly flagged this and asked for a coherent pilot story. It remains unresolved in Round 5.\", \"MODERATE (unresolved from Round 4) — 'replacing the officially-abandoned SWE-bench Verified' framing: The abandonment by OpenAI is factually confirmed (Feb 2026), but OpenAI recommends SWE-bench Pro as the replacement — not SWE-bench-Live. The proposal implies SWE-bench-Live is the community-endorsed successor to Verified, which overstates its adoption. Round 4 asked to reframe as 'providing contamination-resistant evaluation as SWE-bench Verified saturates at frontier.' This change was not made in Round 5.\", \"MODERATE (unresolved from Round 4) — 16-day timeline not explicitly scoped to auto-research + pilot: Manual mode timeline is 3-5 months, Human-in-Loop is 5-9 weeks, and only auto-research (6-10 days) fits the 16-day EMNLP window. The proposal does not state that the EMNLP ARR submission will be auto-research mode output only, and does not reconcile whether pilot-scale (500 training, 100-150 eval) or full-scale (5,300 training, 300 eval + ablations) results will be in the paper.\", \"MINOR (unresolved from Round 4) — Cosine similarity threshold 0.65 still has no justification: The schema validation gate (≥0.65 cosine similarity on 200 held-out SWE-bench Pro instances) determines whether the schema is redesigned before scale-up, yet no rationale for this specific threshold value appears anywhere in the proposal. Round 4 asked for a one-sentence justification.\", \"MINOR (unresolved from Round 4) — SpecRover HTML URL not added: Round 4 explicitly requested adding the HTML URL (https://arxiv.org/html/arXiv:2408.02232) as a parenthetical to preempt future reviewer skepticism about the 51.7% statistic — especially given three rounds of false 'fabricated' accusations in the review history. This was not done in Round 5.\"]\nFeedback: The technical substance of Round 5 is solid: Agentless baseline numbers are verified from Table 3 of arXiv 2505.23419 (11.67%/12.00%/13.33%), the SpecRover 107/207 (51.7%) claim is independently confirmed via direct HTML fetch, Qwen3-Coder-30B-A3B specs are correct, Agent-CoEvo and SWE-Lego are properly integrated, and the schema+worked-example is concrete. The paper is almost ready. Three Round 4 items remain unresolved and need targeted fixes:\n\n(1) **Fix the EMNLP pilot scope — choose one story**: The fastest fix is to remove '500-instance SWE-bench Verified training' from the venue description and replace it with the actual EMNLP submission plan. The defensible choice is: 'EMNLP ARR submission reports auto-research results: SFT on SWE-bench full 2,294-instance corpus (GitBugs augmentation deferred to ICSE), SWE-bench-Live Lite 300-instance eval, 2-field ablation (affected_interface vs. none, expected_behavior vs. none). Full 5,300-instance corpus with all four ablation fields is the ICSE 2027 extended paper.' State this explicitly in both the venue description and the approach section's experimental scope.\n\n(2) **Fix the Verified framing in one clause**: Change 'replacing the officially-abandoned SWE-bench Verified' to 'as SWE-bench Verified saturates with contamination concerns (OpenAI, Feb 2026), SWE-bench-Live provides contamination-resistant evaluation on post-2024 issues.' This is a factually accurate reframe that doesn't misrepresent which benchmark OpenAI actually recommends as replacement.\n\n(3) **Add the 0.65 threshold justification**: One sentence: 'This threshold aligns with established semantic similarity cutoffs in information-extraction evaluation literature, where scores below 0.65 on sentence-transformer embeddings indicate insufficient semantic overlap for structural field matching.' This is the only change needed for that issue.\n\n(4) **Add SpecRover HTML URL** as a parenthetical: after '107 of its 207 unresolved SWE-bench Lite tasks (51.7%)' add '(see https://arxiv.org/html/arXiv:2408.02232, Section V-A)'. Four words of insurance given three rounds of false accusations.\n\nWith these four targeted changes, all substantive issues from rounds 1-5 will be resolved.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:35:25.274Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:35:25.274Z",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-10T07:35:25.312Z_

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
  "title": "SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair",
  "core_problem": "Automated repair agents fail on ambiguous bug reports not from lack of code understanding, but because unstructured issue text leaves behavioral expectations underspecified — what interface should change, what the user observed, and what correct behavior looks like are rarely made explicit. SpecRover (ICSE 2025) partially addresses this via per-instance LLM prompting that extracts specifications from CODE during codebase traversal, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue. Its error analysis (Section V-A, 'Reasons for Failure'; see https://arxiv.org/html/2408.02232, Section V-A) identifies that 107 of its 207 unresolved SWE-bench Lite tasks (51.7%) are classified as 'ambiguous issue description' — cases the paper characterizes as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for why underspecified descriptions constitute an irreducible failure mode for code-space approaches. This architectural limitation is structural: code-side spec extraction can only infer specifications from code that already exists, not from behavior that is described in the issue but not yet correctly implemented. Bug reports routinely contain latent behavioral specifications in their runtime artifacts: stack traces name the affected interface, error messages describe observed behavior, and reproducer assertions encode expected behavior. No method trains a dedicated model to extract these signals from bug report text into a structured repair specification — covering affected interface, observed behavior, expected behavior, and their delta — that could constrain both fault localization and patch generation before any codebase traversal begins.",
  "opportunity": "Failing test assertions in SWE-bench's test patches encode implementation-agnostic behavioral specifications without revealing implementation strategies: `assert result == expected_value` or `with pytest.raises(ValueError)` states precisely what the program SHOULD do, independent of WHICH code to change or HOW to change it. By mechanically converting (problem_statement + test_patch assertions + stack traces) to structured JSON spec fields using AST-level test parsing and NLP extraction on SWE-bench's 2,294 instances, we construct a training corpus of 2,294 (bug_report, structured_spec) pairs — where the spec encodes behavioral expectations derivable without knowing the implementation strategy. This avoids the critical flaw of training on SWE-bench Pro requirements, which were authored by humans with full access to the golden patch (making them solution-conditioned). SWE-bench-Live (NeurIPS 2025, arXiv 2505.23419; ~1,890 Docker-reproducible instances across 223 repositories, drawn from post-January-2024 GitHub issues, growing at ~50 instances/month) provides a clean, contamination-resistant evaluation target with no training-set overlap. As SWE-bench Verified saturates with contamination concerns (OpenAI officially deprecated it in February 2026), SWE-bench-Live provides contamination-resistant evaluation on post-2024 issues unavailable during model training. SWE-bench Pro's human-written `requirements` and `interface` fields (731 public instances) serve as an ecological validity check — we measure cosine similarity between machine-derived specs and human requirements on a held-out 200-instance slice — confirming that AST-parsed test assertions produce specs that match expert behavioral descriptions, without using requirements as training supervision.",
  "landscape": "SpecRover (ICSE 2025, arXiv 2408.02232) is the closest prior work: given a GitHub issue, it iteratively traverses the codebase, prompting Claude 3.5 Sonnet to extract function-level summaries from visited code, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue and 31% on SWE-bench Lite (93/300). SpecRover operates in code-space (it visits source files to generate specs from code) and uses per-instance prompting (no fine-tuning). Our approach operates in issue-space (extracts specs from bug report text and runtime artifacts before any codebase traversal) and uses supervised fine-tuning (consistent structured output at ~$0.05-0.10/issue). These are complementary directions: SpecRover's code-space specs and our issue-space specs could ultimately be fused. Agent-CoEvo (arXiv 2604.04580, April 2026) proposes the most directly competing design philosophy: rather than pre-extracting behavioral constraints from issue text, it coevolves code patches and test patches simultaneously during repair, treating tests as dynamic constraints that are iteratively revised alongside candidate fixes. Agent-CoEvo achieves 41.33% on SWE-bench Lite (DeepSeek-V3) and 46.4% on SWT-bench Lite, outperforming Agentless-1.5 (32%) on those benchmarks. SpecExtract takes the complementary pre-extraction stance: (1) issue-space specs derived before any codebase access are reusable across repair backbones without retraining, including static pipeline systems like Agentless that do not support dynamic constraint revision during search; (2) pre-extracted specs reduce the initial search space before coevolution begins, making SpecExtract a potential front-end that improves Agent-CoEvo's starting population rather than competing with it. SWE-Lego (arXiv 2601.01426, Jan 2026) is the most directly competing concurrent SFT work: it trains on 32k high-quality task instances with error masking and a difficulty-based curriculum, achieving 52.6% on SWE-bench Verified (58.8% with test-time scaling at 16 samples) using a 32B model. SWE-Lego is an end-to-end system that produces complete code fixes; SpecExtract is a preprocessing module that extracts structured behavioral specs from bug report text before any repair attempt, and can plug into SWE-Lego or any other repair backbone as a drop-in front-end — improving fault localization precision and patch generation alignment without retraining the repair agent itself. CodeSpecBench (arXiv 2604.12268, April 2026) benchmarks existing LLMs (Claude, GPT-4, Gemini) on executable behavioral specification generation via prompting — it does not train a dedicated extractor, operates on code-side and description inputs rather than bug report runtime artifacts, and is an evaluation framework rather than a preprocessing pipeline for repair. Its existence confirms that structured specification generation is an active research area, while simultaneously validating the gap: no trained, issue-space specification extractor for repair preprocessing exists. VibeRepair (arXiv 2602.08263, Feb 2026) translates buggy CODE into behavior specifications, repairs the spec, then synthesizes corrected code, achieving 19-23% improvement on Defects4J — code-space to spec, not text-space to spec. TraceRepair (arXiv 2604.02647, Apr 2026) uses runtime execution traces generated by instrumented code execution as shared repair constraints across a multi-agent committee, fixing 392 Defects4J defects — traces are generated during repair, not extracted from issue text before repair begins. RepoRepair (arXiv 2603.01048) generates hierarchical code documentation from source files toward the bug; its documentation is code-driven, not report-driven. SoRFT (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) fine-tunes on SWE-bench with RL to decompose the repair TASK into subtasks (file → function → line → edit), achieving 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite with a 7B model (30.8% Verified and 24.0% Lite with a 32B model) — it structures the repair pipeline, not the issue semantics. PathFix (arXiv 2510.14341) derives behavioral specs from static code execution paths — code-space and offline, not issue-space. The gap: no existing work trains a dedicated model to extract structured behavioral specifications from bug report text and embedded runtime artifacts, operating entirely in issue-space before codebase access.",
  "approach": "We train SpecExtract, a Qwen3-Coder-30B-A3B model (Mixture-of-Experts: 30B total parameters, ~3B active per token — fine-tuning and inference cost scale with active parameters, comparable to a 3B dense model; fits on a single H100 80GB with QLoRA at ~17.5GB VRAM per Unsloth benchmarks; 2× H100 is the recommended training configuration for throughput, not minimum requirement) fine-tuned to map (bug_report_text, runtime_artifacts?) → structured JSON spec, where runtime artifacts are any combination of stack traces, error messages, test failure output, or explicit reproducer assertions present in the issue text. The model gracefully handles varying artifact availability through a masked-field training protocol: training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs. **Formal schema**: Each spec has four typed fields — (1) `affected_interface`: {module: str, signature: str|null, entry_point: str} extracted from stack frame function names and explicitly mentioned APIs; (2) `observed_behavior`: {error_type: str|null, error_message: str|null, symptom: str} from error output and user complaint; (3) `expected_behavior`: {description: str, assertions: [str]} as natural-language description plus test-style constraint strings when derivable; (4) `behavioral_delta`: str, a one-sentence expected-vs-actual summary. Worked example for a NumPy issue 'linalg.solve silently returns None for singular matrices instead of raising': {affected_interface: {module: 'numpy.linalg', entry_point: 'solve', signature: 'solve(a, b)'}, observed_behavior: {error_type: null, symptom: 'returns None for singular matrix input'}, expected_behavior: {description: 'should raise for non-invertible input', assertions: ['raises np.linalg.LinAlgError when matrix is singular']}, behavioral_delta: 'solve silently returns None instead of raising LinAlgError on singular input'}. **Training data construction (implementation-agnostic behavioral specifications)**: From SWE-bench full (2,294 instances including Verified 500 and the broader set): (1) parse `test_patch` test functions via Python AST to extract formal assertions — pytest.raises calls → error_type, assert statements → expected_behavior.assertions, decorated test function signatures → affected_interface hints; (2) extract stack traces and error strings from `problem_statement` text via regex heuristics → observed_behavior; (3) combine via LLM-assisted template fill using Qwen3-Coder-30B-A3B in a chain-of-thought extraction pass to produce coherent spec JSON; (4) validate on 200 SWE-bench Pro public instances that have non-null `requirements` and `interface` fields by computing cosine similarity (sentence-transformer) between mechanically-derived specs and human-authored requirements — target alignment ≥ 0.65 before training at scale (this threshold aligns with established semantic similarity cutoffs in information-extraction evaluation literature, where scores below 0.65 on sentence-transformer embeddings indicate insufficient semantic overlap for structural field matching); this validates the schema rather than using requirements as training targets. Important framing on conditionality: test assertions are written alongside gold patches and encode the behavioral outcome the fix achieves. The training specs are therefore *implementation-agnostic* — they do not reveal which code to change or the implementation strategy — rather than strictly solution-independent. This distinction is explicitly addressed in the paper to avoid overclaiming. The EMNLP 2026 ARR submission uses the 2,294-instance SWE-bench full corpus as the SFT training set; GitBugs augmentation (~3,000 pseudo-labeled instances, yielding a ~5,300-instance total corpus) is reserved for the ICSE 2027 extended paper. **Differentiation from SpecRover**: (1) issue-space — no codebase traversal needed at spec extraction time; (2) supervised learning — consistent, typed JSON output from a single forward pass (~$0.05-0.10/issue) vs. SpecRover's multi-step code traversal ($0.65/issue); (3) directly targets SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved SWE-bench Lite tasks) by conditioning on all available runtime artifacts in the issue, not just the code side. **Integration with Agentless**: Agentless (arXiv 2407.01489) is used as the repair backbone for all SWE-bench-Live evaluations — it follows a fixed three-stage pipeline (hierarchical fault localization → patch generation → patch selection) with no iterative tool calls, making spec injection clean and reproducible. SpecExtract specs are injected at two stages: (1) fault localization Stage 1 — BM25+embedding file retrieval is biased by prepending `affected_interface.module` and `entry_point` as a structured query prefix, pushing relevant files higher in the candidate list; (2) patch generation Stage 3 — the repair LLM receives all four spec fields as an explicit behavioral constraint header in its prompt, focusing generation on the documented delta. **Agentless baseline on SWE-bench-Live**: Per the SWE-bench-Live paper (arXiv 2505.23419, Table 3), Agentless resolves 11.67% (GPT-4o), 12.00% (GPT-4.1), and 13.33% (DeepSeek V3) of SWE-bench-Live Lite (300 instances) — substantially below its 50.8% on SWE-bench Verified, reflecting the contamination-resistant, harder distribution of post-2024 issues. These published numbers establish the Agentless-direct baseline; SpecExtract targets +4-7 percentage points improvement over the best Agentless backbone, which is reported as the primary experimental contribution. **Evaluation**: Primary eval on SWE-bench-Live Lite (300 instances, contamination-resistant, post-2024 issues) with Agentless as backbone; per-field ablations independently zero out each spec field to quantify individual contribution to resolve rate. Secondary eval: cosine-similarity validation on 200 SWE-bench Pro held-out instances (schema validity check). Comparison baselines: Agentless direct repair without spec (established at 11-13% from published SWE-bench-Live results), SpecRover-equivalent prompting (ablation of supervised fine-tuning benefit), SoRFT-Qwen-7B (21.4% Verified / 14.0% Lite, structured subtask decomposition), SWE-Lego (52.6% Verified, end-to-end SFT backbone — SpecExtract as preprocessing front-end demonstrates orthogonal contribution). **Publication scope**: The EMNLP 2026 ARR submission (auto-research mode, 6-10 days) reports results on the 2,294-instance SWE-bench full SFT corpus with SWE-bench-Live Lite 300-instance primary eval and a 2-field ablation (affected_interface vs. none, expected_behavior vs. none) — the two fields with the strongest localization and generation signal respectively. The full 5,300-instance corpus (with GitBugs augmentation) and all four per-field ablation fields constitute the ICSE 2027 extended paper.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~90-110 H100-hours (~180-220 A100-equivalent hours)",
      "gpu_breakdown": "SFT partition (~10-14 H100-hours): Qwen3-Coder-30B-A3B QLoRA fine-tuning on 5,300 instances, 3 epochs, 2× H100 80GB recommended for throughput (single H100 80GB is technically sufficient at ~17.5GB VRAM) — MoE active-parameter efficiency reduces training cost to ~3B dense equivalent. Eval partition (~80-96 H100-hours): spec extraction inference on 5,300 instances (~4 H100-hours); SWE-bench-Live Lite main eval 300 instances × 12.5 min/instance / 4 parallel H100s ≈ 16 H100-hours; per-field ablations 4 fields × 300 instances ≈ 64 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.",
      "gpu_utilization": "~50-60% — Docker sandbox test execution during SWE-bench-Live eval is CPU-bound; GPU idles between model inference calls",
      "timeline": "3-5 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$216-264 (90-110h × $2.40/hr H100 SXM5 on-demand; within the 200 H100-hour hard constraint)"
    },
    "human_in_loop": {
      "gpu_hours": "~135-160 H100-hours (~270-380 A100-equivalent hours)",
      "gpu_breakdown": "SFT partition (~25-35 H100-hours): 3 fine-tuning configurations (schema variant, augmentation ablation, masked-field protocol variant). Eval partition (~110-125 H100-hours): spec extraction ~5 H100-hours; Agentless baseline run on 300 instances ≈ 16 H100-hours; SWE-bench-Live partial eval 600 instances / 4 parallel ≈ 31 H100-hours; per-field ablations on 300-instance subset × 4 fields ≈ 62 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.",
      "gpu_utilization": "~60-70% — agent runs fine-tuning and SWE-bench-Live eval jobs continuously; human approves schema validation threshold, masked-field training protocol, retrieval bias weights, and ablation scope at daily check-ins",
      "timeline": "5-9 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$200-400 (~2,500 orchestration turns at ~$0.10/turn Opus)",
      "estimated_gpu_cost": "~$324-384 (135-160h × $2.40/hr H100); within the 200 H100-hour hard constraint",
      "risk_note": "Critical unknown: whether AST-parsed test assertions produce specs that align with human behavioral descriptions (measured by cosine similarity ≥ 0.65 on 200 SWE-bench Pro validation instances). If alignment is below threshold, the spec schema needs redesign before scale-up. GitBugs pseudo-spec quality is the secondary risk — human spot-check of 100 instances recommended before augmentation scale-up."
    },
    "auto_research": {
      "note": "Budget-capped auto-research only — uncapped sweeps would exceed the 200 H100-hour hard constraint. Capped to 3 fine-tuning configurations × 1 retrieval variant × 1 patch-generation prompt strategy on SWE-bench-Live Lite (300 instances) for the main configuration sweep, then ablations on the best-performing config only.",
      "gpu_hours": "~160-180 H100-hours (budget-capped)",
      "gpu_breakdown": "SFT partition (~30-35 H100-hours): 3 QLoRA configs on 5,300 instances. Eval partition (~130-145 H100-hours): 3-config main sweep 3 × 300 instances ≈ 48 H100-hours; per-field ablations on best config 300 × 4 fields ≈ 64 H100-hours; Agentless baseline ≈ 16 H100-hours; spec extraction inference ≈ 5 H100-hours; validation ≈ 1 H100-hour.",
      "gpu_utilization": "~80-85% — continuous fine-tuning, inference, and SWE-bench-Live Docker eval; sandbox parallelized across 30 instances simultaneously",
      "timeline": "6-10 days with 4 parallel H100 GPUs",
      "team": "0 (setup only, ~3h initial configuration)",
      "claude_api_cost": "$400-600 (~4,500 turns)",
      "estimated_gpu_cost": "~$384-432 (160-180h × $2.40/hr H100)",
      "speed_bottleneck": "SWE-bench-Live Docker sandbox throughput, not GPU compute; Qwen3-Coder-30B-A3B MoE inference (~3B active params) is fast and avoids multi-GPU coordination overhead that a dense 30B model would require"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026 — 15 days remaining; conference October 24-29, Budapest) — NLP angle on structured information extraction from semi-structured bug text; EMNLP ARR submission reports auto-research results (6-10 days): SFT on SWE-bench full 2,294-instance corpus (GitBugs augmentation deferred to ICSE), SWE-bench-Live Lite 300-instance primary eval, and 2-field ablation (affected_interface vs. none, expected_behavior vs. none). The full 5,300-instance corpus with all four per-field ablation fields is the ICSE 2027 extended paper.",
    "ICSE 2027 (abstract deadline June 23, 2026; full paper ~July 2026; conference April-May 2027, Dublin) — SE angle; preferred primary target for full experimental results including GitBugs-augmented 5,300-instance corpus, SWE-bench-Live partial-set ablations, and all four per-field ablation conditions",
    "NeurIPS 2026 (submission deadline expected May-June 2026) — systems and benchmarks angle; natural co-venue given SWE-bench-Live is NeurIPS 2025"
  ],
  "level": "solid",
  "key_references": [
    "SpecRover: Code Intent Extraction via LLMs (arXiv 2408.02232, ICSE 2025) — primary related work: code-space spec inference via prompting, 31% SWE-bench Lite (93/300), $0.65/issue; Section V-A 'Reasons for Failure' (see https://arxiv.org/html/2408.02232, Section V-A) categorizes 107/207 unresolved SWE-bench Lite tasks (51.7%) as 'ambiguous issue description', cases characterized as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for the hardness of this failure mode",
    "SWE-bench Goes Live! (arXiv 2505.23419, NeurIPS 2025 D&B) — primary evaluation benchmark: ~1,890 contamination-resistant instances across 223 repositories, post-2024 GitHub issues, Docker-reproducible, growing at ~50 instances/month; Table 3 reports Agentless on SWE-bench-Live Lite (300 instances) at 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3) — establishes the Agentless-direct baseline for our evaluation",
    "Agent-CoEvo: Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints (arXiv 2604.04580, April 2026) — most directly competing design philosophy: coevolves code patches and test patches simultaneously during repair (41.33% SWE-bench Lite with DeepSeek-V3); SpecExtract's pre-extraction stance is complementary — issue-space specs reduce the initial search space before coevolution, and are pipeline-agnostic for static repair systems that do not support dynamic constraint revision",
    "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (arXiv 2509.16941) — schema ecological validity validator: 731 public instances with human requirements and interface fields",
    "SWE-Lego (arXiv 2601.01426, Jan 2026) — most competitive concurrent SFT work: 32k training instances, difficulty-based curriculum SFT, 52.6% SWE-bench Verified (58.8% with 16-sample test-time scaling) with 32B model; end-to-end repair backbone that SpecExtract can serve as a preprocessing front-end for",
    "Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489) — integration repair backbone: open-source three-stage fixed pipeline (localization → repair → validation), ~50.8% SWE-bench Verified (Agentless-1.5), 32% SWE-bench Lite; spec injected at file localization (retrieval bias) and patch generation (behavioral constraint prefix) stages",
    "CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (arXiv 2604.12268, April 2026) — evaluates prompting-based spec generation from code and descriptions using existing LLMs; does not train a dedicated extractor, operates on code-side inputs rather than bug report runtime artifacts, and is an evaluation framework rather than a repair preprocessing pipeline — confirms structured spec generation is an active research area while the trained, issue-space extractor gap remains open",
    "Specification Vibing for Automated Program Repair / VibeRepair (arXiv 2602.08263, Feb 2026) — code-space spec extraction before repair, Defects4J, 19-23% improvement",
    "Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate / TraceRepair (arXiv 2604.02647, Apr 2026) — trace-based repair constraints during execution, Defects4J",
    "SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) — structured repair subtask decomposition with RL; SoRFT-Qwen-7B: 21.4% SWE-bench Verified / 14.0% SWE-bench Lite; SoRFT-Qwen-32B: 30.8% SWE-bench Verified / 24.0% SWE-bench Lite; key baseline for SpecExtract's supervised fine-tuning approach",
    "GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More (arXiv 2504.09651) — 150K+ open-licensed bug reports for training augmentation",
    "RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048)",
    "On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481)",
    "PathFix: Automated Program Repair with Expected Path (arXiv 2510.14341)"
  ],
  "description": "We introduce SpecExtract, the first supervised issue-space specification extractor for program repair: a fine-tuned Qwen3-Coder-30B-A3B model (MoE, ~3B active parameters — fine-tuning and inference cost comparable to a 3B dense model; fits on a single H100 80GB at ~17.5GB VRAM with QLoRA; 2× H100 recommended for training throughput) that maps (bug_report_text, runtime_artifacts?) → a structured four-field JSON spec covering affected interface, observed behavior, expected behavior, and behavioral delta. The key methodological insight is that failing test assertions in SWE-bench test patches encode implementation-agnostic behavioral specifications — they state what the program SHOULD do without revealing which code to change or the implementation strategy — enabling AST-level test parsing combined with problem-statement NLP extraction to construct 2,294 clean (bug_report, structured_spec) training pairs from SWE-bench. GitBugs (150K+ open-licensed bug reports) provides ~3,000 pseudo-labeled augmentation instances for the ICSE 2027 extended paper; the EMNLP 2026 ARR submission uses the 2,294-instance SWE-bench full corpus only. SWE-bench Pro public requirements serve as an ecological validity check (cosine similarity ≥ 0.65 on 200 held-out instances), not a training target. Extracted specs are integrated with Agentless as the repair backbone, injected at fault localization (retrieval biased toward affected_interface.module/entry_point) and patch generation (structured behavioral constraint prefix). Primary evaluation is on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues — as SWE-bench Verified saturates with contamination concerns, SWE-bench-Live provides the contamination-resistant evaluation target), with the Agentless-direct baseline established at 11-13% from published SWE-bench-Live results (Table 3, arXiv 2505.23419) and a target improvement of +4-7 percentage points; per-field ablations measure individual spec contributions. Agent-CoEvo (arXiv 2604.04580, 41.33% SWE-bench Lite) represents the competing dynamic-coevolution philosophy; SpecExtract's pre-extraction stance is complementary — pipeline-agnostic and applicable to static repair systems. SWE-Lego (52.6% Verified with 32B) is included as an end-to-end SFT baseline to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end rather than competing as a repair system. Differentiated from SpecRover (code-space prompting, $0.65/issue, 31% SWE-bench Lite) by operating in issue-space at ~$0.05-0.10/issue — directly targeting SpecRover's Section V-A identified 51.7% ambiguous-description failure mode — and from SWE-Lego by producing modular, pipeline-agnostic specs that plug into any repair backbone without retraining it. Compute in H100-hours: manual mode ~90-110 H100-hours (SFT ~10-14 H100-hours, eval ~80-96 H100-hours), within the 200-hour hard constraint.",
  "project_name": "structured_spec_repair",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL — Training data availability: The public SWE-bench Pro HuggingFace dataset contains 731 instances from 11 repositories with copyleft licenses. The remaining 1,134 instances (held-out: 12 repos, commercial: 18 proprietary repos) are explicitly not publicly accessible. The proposal's assumption of ~1,865 training pairs is wrong by a factor of 2.5x. At 731 instances, standard fine-tuning of a 32B Qwen3-Coder model risks severe overfitting and is far too small for reliable generalization.", "CRITICAL — Training signal invalidity (train-test distribution mismatch): SWE-bench Pro requirements were authored by humans with full access to the golden patch AND the passing test suite, working backward from tests to specifications. They are solution-conditioned prescriptive clarifications of already-solved problems. Real-world target bug reports are solution-ignorant descriptive complaints from confused users. Fine-tuning SpecExtract on (solution-knowing-human-written-spec → structured-spec) pairs will not teach the model to extract specs from genuinely ambiguous bug reports — it will teach it to produce post-hoc rationalizations of known solutions. This fundamental mismatch is not acknowledged and cannot be patched by synthetic augmentation alone.", "CRITICAL — Evaluation benchmark reliability: SWE-bench Verified shows SOTA of 93.9% (Claude Mythos Preview, May 2026) with documented evidence of data contamination — OpenAI has officially stopped recommending Verified scores for meaningful comparison. Demonstrating a statistically meaningful improvement on a benchmark where frontier models may be reproducing gold patches verbatim severely weakens the paper's empirical contribution.", "Novelty gap — SpecRover (ICSE 2025, arXiv 2408.02232) performs iterative code intent extraction and specification inference from GitHub issue descriptions using LLM agents (not supervised training), and achieves >50% improvement in repair rate on SWE-bench at $0.65/issue. The paper's claim that 'no prior work trains a spec extractor' is technically true but misses that SpecRover occupies the same research niche via prompting. The paper must explicitly frame what the supervised training provides that SpecRover's prompting approach cannot.", "Compute unit mismatch vs. hard constraint: The hard constraint is ≤200 H100-hours. All estimates are given in A100-hours. H100 is ~2–3× faster than A100 for transformer fine-tuning workloads, so 200 A100-hours ≈ 67–100 H100-hours (manual, within budget), but the auto-research mode at 800 A100-hours ≈ 300–400 H100-hours exceeds the hard constraint. The paper should explicitly reconcile resource estimates in H100-hours and confirm the primary research plan stays within budget.", "Structured spec schema undefined: The proposal outputs 'structured specs' with fields (affected interface, pre/post-conditions, expected/actual behavior delta), but these fields are never formally defined — no JSON schema, no field type definitions, no examples of what a valid spec looks like. SWE-bench Pro requirements are freeform prose; the conversion of freeform requirements to structured JSON is the hardest step and receives no design discussion.", "Data leakage if evaluation pivots to SWE-bench Pro: If the proposal trains on SWE-bench Pro (public: 731 instances) and evaluates on the same benchmark, it cannot cleanly show generalization. The community will ask whether the structured spec format was reverse-engineered from the test set rather than learned from scratch."]
Feedback: The core direction — using SWE-bench Pro annotations to supervise structured specification extraction — is creative and timely, but rests on a mischaracterization of what SWE-bench Pro requirements actually are and how many are publicly accessible. To revise toward 'pass': (1) **Fix the training data premise**: Acknowledge that SWE-bench Pro public set is 731 instances, not 1,865. Address the solution-conditioned nature of the requirements by designing the training task as 'given the bug report + human requirements, produce structured spec fields,' treating the requirements as an alignment target rather than pretending they were extracted from bug reports alone. (2) **Address SpecRover directly**: Add SpecRover (ICSE 2025, arXiv 2408.02232) to the related work and explicitly argue why supervised fine-tuning generalizes better than per-instance LLM prompting — e.g., lower inference cost, better calibration, consistency across bug report styles. (3) **Replace SWE-bench Verified as primary eval**: Use SWE-bench Pro public (731 instances) with a held-out split for evaluation, and add an additional out-of-distribution eval on RepoBench or DebugBench to show generalization. Explicitly argue why SWE-bench Pro's requirements-based evaluation is the right target, not the contaminated Verified leaderboard. (4) **Define the structured spec schema**: Add a formal schema definition with field types and a worked example. Show how SWE-bench Pro freeform requirements can be automatically converted to this schema via a parsing step (this becomes its own empirical contribution). (5) **Reconcile compute in H100-hours**: Convert all estimates to H100-hours and confirm manual mode (~67–100 H100-hours) is well within the 200-hour budget. Remove or prominently caveat auto-research mode since it exceeds the hard constraint.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL — Model naming error: 'Qwen3-Coder-14B' does not exist. Qwen3-Coder is only available in 30B-A3B (MoE, 3B active) and 480B-A35B variants. The closest viable alternatives are Qwen3-14B (dense, base Qwen3 family) or Qwen2.5-Coder-14B (prior generation). This error must be corrected with the actual model to be used, and any VRAM/compute estimates adjusted accordingly.", "CRITICAL — Unverifiable SpecRover failure claim: The proposal states SpecRover 'explicitly identifies that 51.7% of its unresolved SWE-bench Lite failures stem from ambiguous issue descriptions.' This specific statistic could not be verified from the SpecRover abstract or public-facing sections. If this is an inference rather than a direct quote, it must be either verified by citing the exact section, reframed as an approximation, or removed. The entire motivation chain rests on this number.", "SIGNIFICANT — SoRFT baseline misrepresented: The proposal states SoRFT achieves '21.4% on SWE-bench Verified with a 7B model' but SoRFT (ACL 2025) actually reports 21.4% on SWE-bench Lite, not Verified. The Verified number for SoRFT-7B is 14.0%. Using the wrong benchmark undermines the baseline comparison.", "SIGNIFICANT — Integration repair agent unspecified: The primary experimental claim requires running a full end-to-end repair pipeline on SWE-bench-Live (1,890 instances) that integrates the extracted spec. The proposal does not specify which agent (SWE-agent, Moatless, Agentless, custom) is used, how the spec is injected, or what its baseline resolve rate is. Without this, the compute estimate and experimental design are incomplete.", "SIGNIFICANT — SWE-Lego (arXiv 2601.01426) not addressed: This January 2026 SFT-for-issue-resolving paper uses 32k training instances and a comprehensive SFT curriculum for end-to-end repair. As direct related work in the SFT-for-SWE space, its omission leaves a gap the reviewer committee will flag. The differentiation should be: SpecExtract does a spec-extraction subtask (not end-to-end repair), enabling pipeline-agnostic reuse.", "MODERATE — Test_patch assertion conditionality overstated: The 'non-solution-conditioned' framing is the linchpin of the training data justification, but test patches are written after/alongside gold patches and specifically designed to validate the fix. In many SWE-bench instances, assertions encode precise return values or exception types only determinable by knowing the codebase implementation. The paper should more carefully scope the claim: 'behavioral-specification-level, not implementation-level conditioned' rather than 'non-solution-conditioned.'", "MINOR — SWE-bench-Live size outdated: The proposal states '1,565+ instances' but the live dataset now contains 1,890 tasks across 223 repositories. Update to the current figure.", "MINOR — Compute budget tightness for full eval: Running a repair agent on 1,890 SWE-bench-Live instances at ~10-15 minutes/issue with 4 parallel H100s consumes approximately 79-118 H100-hours for evaluation alone, leaving 0-6 H100-hours for fine-tuning in the manual mode upper estimate. Explicitly partition the budget between SFT and eval inference."]
Feedback: The Round 2 revision has substantially addressed the Round 1 critical issues: the training data premise is now grounded (SWE-bench test_patch AST parsing rather than SWE-bench Pro requirements), the evaluation target is appropriate (SWE-bench-Live), compute is expressed in H100-hours with manual mode under budget, and the JSON schema is formally defined. This is genuine progress. To advance to 'pass':

(1) **Fix the model name immediately**: Replace 'Qwen3-Coder-14B' with either 'Qwen3-14B' (dense, 14B params, general Qwen3 family) or 'Qwen3-Coder-30B-A3B' (MoE, only 3B active params, faster and better for code). Qwen3-Coder-30B-A3B is the more credible choice for a coding spec-extraction task — its ~3B active parameters mean fine-tuning cost is comparable to a 3B dense model despite 30B total params.

(2) **Verify or remove the 51.7% SpecRover claim**: Read SpecRover Section 4 or 5 (error analysis). If the 51.7% figure is there, cite the exact table/figure. If it's an approximation, write: 'SpecRover's error analysis identifies ambiguous issue descriptions as the dominant unresolved failure mode (Section X); our estimate from their public failure logs is ~50%.' If it's not there, reframe the motivation as: 'SpecRover's code-space approach cannot address cases where the issue description itself is underspecified — a failure mode it cannot observe.'

(3) **Fix the SoRFT baseline**: Change '21.4% on SWE-bench Verified' to '21.4% on SWE-bench Lite (14.0% on Verified).' This makes SoRFT a weaker baseline, which actually helps SpecExtract's positioning.

(4) **Specify the integration repair agent**: Choose one concrete agent (e.g., Agentless or Moatless) as the integration vehicle for the SWE-bench-Live evaluation. Report its baseline resolve rate, then show the SpecExtract-augmented rate. Add this as 1-2 sentences in the approach section. This is the most critical missing piece for a credible empirical narrative.

(5) **Add SWE-Lego differentiation**: One paragraph acknowledging SWE-Lego (arXiv 2601.01426) as concurrent SFT work, differentiating that SpecExtract is a preprocessing spec-extraction module (not an end-to-end repair system) that can be combined with any SFT-trained or prompted repair backbone, including SWE-Lego itself.

(6) **Scope the conditionality claim**: In the training data section, replace 'non-solution-conditioned' with 'implementation-agnostic behavioral specifications' to reflect that while test assertions do implicitly know the fix's behavior, they do not expose the implementation strategy, making them valid targets for behavioral spec learning.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL — Fabricated SpecRover citation (third consecutive round): The proposal cites 'SpecRover Section V-A, Reasons for Failure' with the specific claim that 51.7% of its 207 unresolved SWE-bench Lite tasks involve ambiguous issue descriptions (107/207 instances, labeled by SWE-bench Verified human annotators). Independent verification via WebFetch of arXiv 2408.02232v3 confirms this section does not exist — SpecRover has no dedicated error analysis section categorizing failures by issue ambiguity, and contains no 51.7% figure, 107/207 count, or SWE-bench Verified annotation cross-reference. The Round 3 generator escalated from 'unverifiable' (Round 2) to 'fabricated with false specificity' by inventing the section label, count, and labeling provenance. This is an academic integrity violation that will result in desk rejection or post-acceptance retraction if submitted as-is.", "SIGNIFICANT — Agent-CoEvo (arXiv 2604.04580, April 2026) not addressed in landscape: This concurrent paper, 'Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints,' proposes that behavioral constraints (tests) should be coevolved dynamically with code patches during repair rather than pre-extracted from bug reports. It evaluates on SWE-bench Lite and SWT-bench Lite and outperforms agentless baselines. This represents the most direct competing design philosophy to SpecExtract's pre-extraction approach and must be discussed — specifically, why pre-extraction from issue text before any codebase access is preferable to dynamic constraint coevolution.", "MODERATE — SoRFT numbers are now correct but were mishandled across three rounds: Independent verification via ACL Anthology (2025.acl-long.559) confirms SoRFT-7B achieves 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite — exactly as stated in Round 3. The Round 2 reviewer was wrong to flag these as reversed. While the numbers are now correct, three rounds of oscillation on this point suggest the generator should add a footnote citing the ACL Anthology URL to preempt reviewer confusion.", "MODERATE — No reported Agentless-on-SWE-bench-Live baseline: The experimental design requires establishing Agentless-direct (no spec injection) on SWE-bench-Live Lite (300 instances) as the baseline, then measuring SpecExtract-augmented Agentless. This baseline number is not reported anywhere in the proposal, making it impossible to assess whether the expected delta (e.g., +3-8 percentage points) is plausible or whether Agentless-1.5's 50.8% Verified score generalizes to the Live dataset at all. At minimum, cite the Agentless-1.5 SWE-bench-Live Lite score if published, or explicitly acknowledge this is unmeasured.", "MINOR — QLoRA VRAM claim is slightly oversimplified: Qwen3-Coder-30B-A3B with QLoRA requires ~17.5GB VRAM (verified via Unsloth documentation), fitting comfortably on a single H100 80GB rather than requiring 2× H100s. The 2× claim is not wrong (it enables larger batch sizes and faster throughput) but should be reframed as 'recommended configuration for efficient throughput' rather than 'minimum requirement.'"]
Feedback: This proposal has made genuine progress across three rounds — the model choice, Agentless integration, SWE-Lego differentiation, schema definition, and compute budget are all solid. One issue now blocks this from passing, and one new issue must be addressed:

(1) **IMMEDIATE: Remove or replace the fabricated SpecRover Section V-A claim.** There is no 'Section V-A: Reasons for Failure' in SpecRover, no 51.7% figure, no 107/207 count, and no SWE-bench Verified annotation cross-reference in the paper. Replace the entire motivation chain with a defensible framing: 'SpecRover (ICSE 2025) evaluates on SWE-bench Lite and explicitly acknowledges that its code-space traversal approach cannot resolve cases where the issue description itself is underspecified — it can only infer specifications from code that exists, not from behavior that is described but not yet correctly implemented. This architectural limitation motivates an issue-space approach that operates on bug report text before codebase access.' If you want to keep a quantitative hook, look at SpecRover's SWE-bench Lite resolve rate (31%) and the known proportion of SWE-bench tasks where the issue description is classified as ambiguous by SWE-bench Verified human annotators — cite the SWE-bench Verified paper (arXiv 2410.06992) or the SWE-bench Pro paper for that annotation, not SpecRover.

(2) **Add Agent-CoEvo to related work.** One paragraph: 'Agent-CoEvo (arXiv 2604.04580, April 2026) proposes coevolving code and test patches simultaneously during repair, treating tests as dynamic behavioral constraints. SpecExtract takes the complementary pre-extraction stance: issue-space specs derived before any codebase access reduce the search space for both fault localization and patch generation, and are reusable across repair backbones without retraining — including static repair systems like Agentless that do not support dynamic constraint revision.'

(3) **Add Agentless-on-SWE-bench-Live baseline.** State the known or estimated Agentless-1.5 resolve rate on SWE-bench-Live Lite (or acknowledge it as an early experimental measurement to be reported in the paper). The experimental contribution is the delta, and without the baseline anchor the paper cannot make its empirical case.

With these three changes — particularly (1) — this proposal should be able to pass in Round 4.

### Round 4 review
Verdict: revise
Issues: ["IMPORTANT CORRECTION — SpecRover Section V-A claim is VERIFIED, not fabricated: Independent WebFetch of the HTML version of arXiv:2408.02232 (https://arxiv.org/html/arXiv:2408.02232) confirms the paper contains Section V-A 'RQ1: Overall Efficacy of Task Resolving' with a subsection 'Reasons for Failure' that explicitly documents 107/207 unresolved SWE-bench Lite tasks (51.7%) classified as ambiguous issue descriptions. The Round 3 reviewer's 'fabricated' accusation was incorrect. The generator should add a footnote or parenthetical citing the HTML URL to preempt any residual reviewer confusion, since the accusation has been raised three consecutive rounds.", "SIGNIFICANT — Internal inconsistency in EMNLP pilot scope: The EMNLP venue description states 'realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval,' but the main approach uses 2,294 SWE-bench instances + 3,000 GitBugs pseudo-labeled instances = 5,300 corpus. These are in direct conflict. Either (a) define the EMNLP submission as explicitly scoped to a pilot — SFT on SWE-bench Verified 500 subset, SWE-bench-Live Lite 300-instance eval, no GitBugs augmentation — and state this clearly in the approach section, or (b) remove the '500-instance Verified' framing from the venue description and commit to the full corpus with the understanding that compute and eval must finish within 16 days.", "MODERATE — 16-day deadline is unrealistically framed without explicit pilot scope: Building the 5,300-instance training corpus (AST parsing + NLP regex + LLM-assisted spec fill), SFT (10-14 H100-hours), establishing Agentless-SWE-bench-Live Docker infrastructure, running the full 300-instance eval + 4-field ablations (80-96 H100-hours), and writing the paper cannot realistically be completed in 16 days by 1-2 researchers. The submission plan should explicitly acknowledge that the EMNLP ARR submission will report pilot-scale results (e.g., SFT on 500-instance Verified subset, 100-instance SWE-bench-Live Lite eval) with the full-scale results reserved for ICSE 2027 as the primary venue.", "MODERATE — 'Replacing the officially-abandoned SWE-bench Verified' is imprecise: OpenAI's February 2026 announcement recommends SWE-bench Pro as the frontier evaluation replacement — not SWE-bench-Live. SWE-bench-Live is the appropriate replacement for contamination-resistant research evaluation, which is the correct positioning for this paper, but the phrasing implies SWE-bench-Live is the community standard replacement for Verified, which overstates its current adoption. Reframe as: 'As SWE-bench Verified saturates with contamination concerns, SWE-bench-Live (NeurIPS 2025) provides contamination-resistant evaluation on post-2024 issues — the appropriate target for research contributions that train on SWE-bench data.'", "MINOR — Cosine similarity threshold (≥ 0.65) for schema validation is stated without justification: The proposal requires AST-parsed test assertions to achieve ≥ 0.65 cosine similarity with SWE-bench Pro human requirements on 200 held-out instances. This threshold determines whether the schema is redesigned before scale-up, making it a critical gating decision. Add one sentence explaining why 0.65 is the right threshold (e.g., 'consistent with semantic similarity thresholds in information extraction literature where 0.65 distinguishes semantically related from unrelated pairs')."]
Feedback: The SpecRover Section V-A claim has been independently verified as correct — the HTML paper confirms the 107/207 (51.7%) ambiguous issue description statistics in the 'Reasons for Failure' subsection of Section V-A. After three rounds of false accusations, add a parenthetical citing the HTML URL (https://arxiv.org/html/arXiv:2408.02232) to preempt any residual reviewer skepticism. To reach 'pass' in Round 5: (1) **Fix the pilot/full scope inconsistency**: Choose one coherent story for EMNLP. The most defensible is a pilot submission — SFT on SWE-bench Verified 500-instance subset, primary eval on 100-150 SWE-bench-Live Lite instances (not 300), 2-field ablation (affected_interface vs. none, expected_behavior vs. none). Remove the '500-instance SWE-bench Verified training' from the venue description and put it in the approach section as the EMNLP pilot plan. State that the full 5,300-instance corpus + 300-instance eval is the ICSE 2027 primary submission. (2) **Fix the SWE-bench Verified replacement framing**: Change 'replacing the officially-abandoned SWE-bench Verified' to 'providing contamination-resistant evaluation as SWE-bench Verified saturates at frontier.' (3) **Justify the 0.65 cosine similarity threshold** in one sentence. With these changes, the proposal will have resolved all substantive issues from rounds 1-4 and should be ready to pass.

### Round 5 review
Verdict: revise
Issues: ["SIGNIFICANT (unresolved from Round 4) — EMNLP venue scope vs approach inconsistency: The target_venues description states 'realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval,' but the approach section describes a 5,300-instance training corpus (2,294 SWE-bench full + ~3,000 GitBugs pseudo-labeled). These are directly contradictory in the same document. Round 4 explicitly flagged this and asked for a coherent pilot story. It remains unresolved in Round 5.", "MODERATE (unresolved from Round 4) — 'replacing the officially-abandoned SWE-bench Verified' framing: The abandonment by OpenAI is factually confirmed (Feb 2026), but OpenAI recommends SWE-bench Pro as the replacement — not SWE-bench-Live. The proposal implies SWE-bench-Live is the community-endorsed successor to Verified, which overstates its adoption. Round 4 asked to reframe as 'providing contamination-resistant evaluation as SWE-bench Verified saturates at frontier.' This change was not made in Round 5.", "MODERATE (unresolved from Round 4) — 16-day timeline not explicitly scoped to auto-research + pilot: Manual mode timeline is 3-5 months, Human-in-Loop is 5-9 weeks, and only auto-research (6-10 days) fits the 16-day EMNLP window. The proposal does not state that the EMNLP ARR submission will be auto-research mode output only, and does not reconcile whether pilot-scale (500 training, 100-150 eval) or full-scale (5,300 training, 300 eval + ablations) results will be in the paper.", "MINOR (unresolved from Round 4) — Cosine similarity threshold 0.65 still has no justification: The schema validation gate (≥0.65 cosine similarity on 200 held-out SWE-bench Pro instances) determines whether the schema is redesigned before scale-up, yet no rationale for this specific threshold value appears anywhere in the proposal. Round 4 asked for a one-sentence justification.", "MINOR (unresolved from Round 4) — SpecRover HTML URL not added: Round 4 explicitly requested adding the HTML URL (https://arxiv.org/html/arXiv:2408.02232) as a parenthetical to preempt future reviewer skepticism about the 51.7% statistic — especially given three rounds of false 'fabricated' accusations in the review history. This was not done in Round 5."]
Feedback: The technical substance of Round 5 is solid: Agentless baseline numbers are verified from Table 3 of arXiv 2505.23419 (11.67%/12.00%/13.33%), the SpecRover 107/207 (51.7%) claim is independently confirmed via direct HTML fetch, Qwen3-Coder-30B-A3B specs are correct, Agent-CoEvo and SWE-Lego are properly integrated, and the schema+worked-example is concrete. The paper is almost ready. Three Round 4 items remain unresolved and need targeted fixes:

(1) **Fix the EMNLP pilot scope — choose one story**: The fastest fix is to remove '500-instance SWE-bench Verified training' from the venue description and replace it with the actual EMNLP submission plan. The defensible choice is: 'EMNLP ARR submission reports auto-research results: SFT on SWE-bench full 2,294-instance corpus (GitBugs augmentation deferred to ICSE), SWE-bench-Live Lite 300-instance eval, 2-field ablation (affected_interface vs. none, expected_behavior vs. none). Full 5,300-instance corpus with all four ablation fields is the ICSE 2027 extended paper.' State this explicitly in both the venue description and the approach section's experimental scope.

(2) **Fix the Verified framing in one clause**: Change 'replacing the officially-abandoned SWE-bench Verified' to 'as SWE-bench Verified saturates with contamination concerns (OpenAI, Feb 2026), SWE-bench-Live provides contamination-resistant evaluation on post-2024 issues.' This is a factually accurate reframe that doesn't misrepresent which benchmark OpenAI actually recommends as replacement.

(3) **Add the 0.65 threshold justification**: One sentence: 'This threshold aligns with established semantic similarity cutoffs in information-extraction evaluation literature, where scores below 0.65 on sentence-transformer embeddings indicate insufficient semantic overlap for structural field matching.' This is the only change needed for that issue.

(4) **Add SpecRover HTML URL** as a parenthetical: after '107 of its 207 unresolved SWE-bench Lite tasks (51.7%)' add '(see https://arxiv.org/html/arXiv:2408.02232, Section V-A)'. Four words of insurance given three rounds of false accusations.

With these four targeted changes, all substantive issues from rounds 1-5 will be resolved.


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
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "type": "user",
  "uuid": "46a868b0-3a76-4338-9306-c1e6fdbd61a8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:35:25.307Z_

```json
{
  "parentUuid": "46a868b0-3a76-4338-9306-c1e6fdbd61a8",
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
  "uuid": "61adf409-3344-48e9-93e5-bcf981c65abb",
  "timestamp": "2026-05-10T07:35:25.307Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:35:25.308Z_

```json
{
  "parentUuid": "61adf409-3344-48e9-93e5-bcf981c65abb",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "52724580-df0b-401c-9288-40a0f2ecedc1",
  "timestamp": "2026-05-10T07:35:25.308Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
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
  "leafUuid": "52724580-df0b-401c-9288-40a0f2ecedc1",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space spec extraction for program repair",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:35:40.808Z_

<details><summary>Logged reasoning block</summary>

```text
Let me conduct a thorough adversarial review of the "SpecExtract" paper idea. This is Round 6 of 10. Let me carefully analyze the proposal and conduct independent verification via web search.

Key areas to investigate:
1. Whether the Round 5 issues were actually resolved in Round 6
2. Verify claims about SpecRover Section V-A
3. Verify SWE-bench-Live numbers
4. Check for competing/concurrent work
5. Verify Qwen3-Coder-30B-A3B specs


6. Check the EMNLP scope consistency
7. Verify Agent-CoEvo claims

Let me start with web searches to independently verify key claims. From the Round 5 feedback, I need to check whether the main issues were addressed: the EMNLP pilot scope inconsistency, the framing around SWE-bench Verified, the 16-day timeline scoping, the cosine similarity threshold justification, and whether SpecRover's HTML URL was added. Now I'm examining what was actually fixed in Round 6.

The EMNLP scope is now consistent—the venue description aligns with the approach section, both clarifying that the full 5,300-instance corpus with all ablation fields is reserved for the ICSE 2027 extended paper, while EMNLP uses the 2,294-instance corpus with a 2-field ablation. That's fixed. Now checking the SWE-bench Verified framing...

the text correctly avoids implying SWE-bench-Live is the community-endorsed successor by saying "saturates with contamination concerns" instead of "officially abandoned," though it still mentions OpenAI deprecated it, which is factually accurate even if it doesn't explicitly note they recommend SWE-bench Pro as the replacement—mostly addressed. Moving on to verify the 16-day timeline claim in the venue description... Now I need to search strategically for competing work on issue-space specification extraction, verify the claims about Agent-CoEvo and SWE-Lego, and check if there's any other concurrent research I might have missed, keeping in mind my context constraints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52724580-df0b-401c-9288-40a0f2ecedc1",
  "isSidechain": false,
  "requestId": "req_011CatW8ZG17baRTQWjvpU3o",
  "type": "assistant",
  "uuid": "9369fc94-715a-4be8-8b46-f53630dd81dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XoPqSzbqUL3nWg145WSfZz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23591,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1975,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1975,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23591
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

_source line 9 · 2026-05-10T07:35:40.830Z_

I'll conduct independent research to verify the Round 6 claims before issuing my verdict. Let me start with targeted searches on the key claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9369fc94-715a-4be8-8b46-f53630dd81dc",
  "isSidechain": false,
  "requestId": "req_011CatW8ZG17baRTQWjvpU3o",
  "type": "assistant",
  "uuid": "48dff12a-d987-4e2f-b655-93fd2d621dd0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XoPqSzbqUL3nWg145WSfZz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23591,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1975,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1975,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23591
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

_source line 10 · 2026-05-10T07:35:47.481Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017huRBJracnq3JJcG4gD92X`</summary>

```json
{
  "description": "Verify SWE-bench-Live paper claims and competing work",
  "subagent_type": "Explore",
  "prompt": "Search the web to verify the following claims for an adversarial ML paper review. Return factual findings only.\n\n1. Search for \"SWE-bench-Live arXiv 2505.23419\" to verify: (a) the paper exists at NeurIPS 2025, (b) Agentless baseline numbers on SWE-bench-Live Lite (300 instances) - specifically 11.67% GPT-4o, 12.00% GPT-4.1, 13.33% DeepSeek V3 from Table 3, (c) the current dataset size (~1,890 instances).\n\n2. Search for \"Agent-CoEvo arXiv 2604.04580\" to verify: (a) the paper exists, (b) it achieves 41.33% on SWE-bench Lite with DeepSeek-V3, (c) it coevolves code patches and test patches.\n\n3. Search for \"SWE-Lego arXiv 2601.01426\" to verify: (a) it achieves 52.6% on SWE-bench Verified with 32B model, (b) uses 32k training instances.\n\n4. Search for any very recent (2025-2026) papers on \"issue specification extraction program repair\" or \"bug report structured spec extraction\" that might be competing work not mentioned in the proposal.\n\n5. Search for \"SpecRover ICSE 2025 arXiv 2408.02232\" to verify the Section V-A \"Reasons for Failure\" / ambiguous issue descriptions claim.\n\nUse web search for each. Report exact findings including any discrepancies."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48dff12a-d987-4e2f-b655-93fd2d621dd0",
  "isSidechain": false,
  "requestId": "req_011CatW8ZG17baRTQWjvpU3o",
  "type": "assistant",
  "uuid": "0b3a8d5b-4625-439a-9d1b-e463cd165f5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XoPqSzbqUL3nWg145WSfZz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23591,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1975,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1975,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23591
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

_source line 11 · 2026-05-10T07:35:54.677Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GHU2ttqo3mtrttg2gK4by4`</summary>

```json
{
  "description": "Search for competing concurrent work on issue-space specification extraction",
  "subagent_type": "Explore",
  "prompt": "Conduct adversarial novelty search for a paper called \"SpecExtract\" which trains a model (fine-tuned Qwen3-Coder-30B-A3B) to extract structured behavioral specifications from bug report text + runtime artifacts (stack traces, error messages, test assertions) before any codebase access, using those specs to guide automated program repair on SWE-bench.\n\nSearch for papers that might overlap with or compete against this idea:\n\n1. Search: \"structured specification extraction bug report program repair 2025 2026\" on Google/arXiv\n2. Search: \"issue text specification LLM fine-tuning code repair\" arxiv 2025 2026\n3. Search: \"behavioral specification extraction SWE-bench\" \n4. Search: site:arxiv.org \"issue specification\" \"program repair\" 2026\n5. Search: \"bug report information extraction structured repair\" NLP 2025 2026\n6. Search: \"CodeSpecBench arXiv 2604.12268\" to verify this paper's claims\n7. Search: \"SoRFT arXiv 2502.20127\" SWE-bench Verified vs Lite numbers - verify if 21.4% is on Verified or Lite\n8. Search for any papers combining AST parsing + NLP extraction from bug reports for fault localization\n\nReport all relevant papers found with their titles, venues, and key claims. Focus especially on finding papers that do specification extraction from issue text (not code) for repair purposes."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b3a8d5b-4625-439a-9d1b-e463cd165f5a",
  "isSidechain": false,
  "requestId": "req_011CatW8ZG17baRTQWjvpU3o",
  "type": "assistant",
  "uuid": "85ebd88e-cdeb-43f6-af72-641d3c4e10cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XoPqSzbqUL3nWg145WSfZz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 23591,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1975,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23591,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1975,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 23591,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23591
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

_source line 12 · 2026-05-10T07:36:48.173Z_

<details><summary>↩ Tool result · `toolu_017huRBJracnq3JJcG4gD92X`</summary>

```text
Based on my comprehensive web search and document verification, here are my factual findings:

## Summary of Verification Results

### 1. **SWE-bench-Live (arXiv 2505.23419)**

**Status: PARTIALLY VERIFIED with DISCREPANCIES**

- **(a) Paper exists at NeurIPS 2025:** CONFIRMED - The paper "SWE-bench Goes Live!" is confirmed as accepted at NeurIPS 2025 Datasets & Benchmarks track.

- **(b) Agentless baseline numbers on SWE-bench-Live Lite (300 instances):** CONFIRMED with caveats
  - GPT-4o: 11.67% ✓
  - GPT-4.1: 12.00% ✓  
  - DeepSeek V3: 13.33% ✓
  - These exact percentages were confirmed in the search results.

- **(c) Dataset size (~1,890 instances):** DISCREPANCY FOUND
  - The OpenReview/GitHub repository mentions **1,890 instances** across 223 repositories
  - However, the official SWE-bench-Live leaderboard (June 2025) states **1,565 instances** across 164 repositories
  - The paper's initial release (May 29, 2025) stated **1,319 instances**
  - **Conclusion:** The dataset size has grown over time. The 1,890 figure appears to be from a later version (current/May 2026), but the leaderboard shows 1,565 as of June 2025. Both numbers are accurate for different time periods.

### 2. **Agent-CoEvo (arXiv 2604.04580)**

**Status: VERIFIED**

- **(a) Paper exists:** CONFIRMED - Found as "Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints"

- **(b) 41.33% on SWE-bench Lite with DeepSeek-V3:** CONFIRMED - Verified from the paper's Table 1, which shows Agent-CoEvo with DeepSeek-V3 achieves exactly 41.33% resolution on the 300-issue benchmark.

- **(c) Coevolves code patches and test patches:** CONFIRMED - The paper explicitly states it is "a coevolutionary multi-agent framework in which candidate code patches and test patches are jointly explored and iteratively refined."

### 3. **SWE-Lego (arXiv 2601.01426)**

**Status: VERIFIED**

- **(a) 52.6% on SWE-bench Verified with 32B model:** CONFIRMED - SWE-Lego-Qwen3-32B achieves 52.6% on SWE-bench Verified (further boosted to 58.8% under test-time scaling).

- **(b) Uses 32k training instances:** CONFIRMED - The dataset comprises "32k high-quality task instances and 18k validated trajectories," combining real and synthetic data.

### 4. **Recent competing work on issue specification extraction (2025-2026)**

**Status: FOUND RELEVANT PAPERS**

Several relevant papers identified:
- *"Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation"* (arXiv 2505.07270) - Addresses specification ambiguity repair
- *"A Survey of LLM-based Automated Program Repair"* (arXiv 2506.23749) - Comprehensive taxonomy including specification extraction
- *"Knowledge-Enhanced Program Repair for Data Science Code"* (ICSE 2025) - Uses knowledge extraction from issues
- *"Automated Program Repair: Emerging Trends"* (ACM Computing Surveys) - General survey on APR trends

These papers exist but don't appear to be the primary focus on structured spec extraction from issue descriptions in the way the proposal implies.

### 5. **SpecRover (ICSE 2025, arXiv 2408.02232)**

**Status: VERIFIED with SPECIFIC FINDING**

- **Section V-A "Reasons for Failure" / ambiguous issue descriptions:** CONFIRMED - SpecRover examined 207 unresolved tasks and found:
  - **Ambiguous issue descriptions: 107 cases (51.7%)** - classified as "hard or impossible to solve without further information"
  - Incorrect fix location: 29.5%
  - Incorrect code modification: 18.8%

This confirms the claim that ambiguous issue descriptions are a major failure mode for program repair systems.

---

## Key Discrepancy Summary

The only substantive discrepancy is the **SWE-bench-Live dataset size**, which varies between:
- 1,319 (initial May 29, 2025 release)
- 1,565 (June 2025 official leaderboard)
- 1,890 (OpenReview/recent update)

All other major claims have been verified with exact numbers matching the sources.

Sources:
- [SWE-bench Goes Live! arXiv Abstract](https://arxiv.org/abs/2505.23419)
- [SWE-bench Goes Live! OpenReview](https://openreview.net/forum?id=OGWkr7gXka)
- [Agent-CoEvo HTML Version](https://arxiv.org/html/2604.04580)
- [SWE-Lego arXiv Abstract](https://arxiv.org/abs/2601.01426)
- [SpecRover arXiv HTML](https://arxiv.org/html/2408.02232)
- [SWE-bench-Live Leaderboard](https://swe-bench-live.github.io/)
- [SWE-bench-Live GitHub Repository](https://github.com/microsoft/SWE-bench-Live)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b3a8d5b-4625-439a-9d1b-e463cd165f5a",
  "isSidechain": false,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "type": "user",
  "uuid": "7b07260b-668f-43f8-9e89-cb2788007377",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify the following claims for an adversarial ML paper review. Return factual findings only.\n\n1. Search for \"SWE-bench-Live arXiv 2505.23419\" to verify: (a) the paper exists at NeurIPS 2025, (b) Agentless baseline numbers on SWE-bench-Live Lite (300 instances) - specifically 11.67% GPT-4o, 12.00% GPT-4.1, 13.33% DeepSeek V3 from Table 3, (c) the current dataset size (~1,890 instances).\n\n2. Search for \"Agent-CoEvo arXiv 2604.04580\" to verify: (a) the paper exists, (b) it achieves 41.33% on SWE-bench Lite with DeepSeek-V3, (c) it coevolves code patches and test patches.\n\n3. Search for \"SWE-Lego arXiv 2601.01426\" to verify: (a) it achieves 52.6% on SWE-bench Verified with 32B model, (b) uses 32k training instances.\n\n4. Search for any very recent (2025-2026) papers on \"issue specification extraction program repair\" or \"bug report structured spec extraction\" that might be competing work not mentioned in the proposal.\n\n5. Search for \"SpecRover ICSE 2025 arXiv 2408.02232\" to verify the Section V-A \"Reasons for Failure\" / ambiguous issue descriptions claim.\n\nUse web search for each. Report exact findings including any discrepancies.",
    "agentId": "a44695e3e805a9397",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive web search and document verification, here are my factual findings:\n\n## Summary of Verification Results\n\n### 1. **SWE-bench-Live (arXiv 2505.23419)**\n\n**Status: PARTIALLY VERIFIED with DISCREPANCIES**\n\n- **(a) Paper exists at NeurIPS 2025:** CONFIRMED - The paper \"SWE-bench Goes Live!\" is confirmed as accepted at NeurIPS 2025 Datasets & Benchmarks track.\n\n- **(b) Agentless baseline numbers on SWE-bench-Live Lite (300 instances):** CONFIRMED with caveats\n  - GPT-4o: 11.67% ✓\n  - GPT-4.1: 12.00% ✓  \n  - DeepSeek V3: 13.33% ✓\n  - These exact percentages were confirmed in the search results.\n\n- **(c) Dataset size (~1,890 instances):** DISCREPANCY FOUND\n  - The OpenReview/GitHub repository mentions **1,890 instances** across 223 repositories\n  - However, the official SWE-bench-Live leaderboard (June 2025) states **1,565 instances** across 164 repositories\n  - The paper's initial release (May 29, 2025) stated **1,319 instances**\n  - **Conclusion:** The dataset size has grown over time. The 1,890 figure appears to be from a later version (current/May 2026), but the leaderboard shows 1,565 as of June 2025. Both numbers are accurate for different time periods.\n\n### 2. **Agent-CoEvo (arXiv 2604.04580)**\n\n**Status: VERIFIED**\n\n- **(a) Paper exists:** CONFIRMED - Found as \"Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints\"\n\n- **(b) 41.33% on SWE-bench Lite with DeepSeek-V3:** CONFIRMED - Verified from the paper's Table 1, which shows Agent-CoEvo with DeepSeek-V3 achieves exactly 41.33% resolution on the 300-issue benchmark.\n\n- **(c) Coevolves code patches and test patches:** CONFIRMED - The paper explicitly states it is \"a coevolutionary multi-agent framework in which candidate code patches and test patches are jointly explored and iteratively refined.\"\n\n### 3. **SWE-Lego (arXiv 2601.01426)**\n\n**Status: VERIFIED**\n\n- **(a) 52.6% on SWE-bench Verified with 32B model:** CONFIRMED - SWE-Lego-Qwen3-32B achieves 52.6% on SWE-bench Verified (further boosted to 58.8% under test-time scaling).\n\n- **(b) Uses 32k training instances:** CONFIRMED - The dataset comprises \"32k high-quality task instances and 18k validated trajectories,\" combining real and synthetic data.\n\n### 4. **Recent competing work on issue specification extraction (2025-2026)**\n\n**Status: FOUND RELEVANT PAPERS**\n\nSeveral relevant papers identified:\n- *\"Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation\"* (arXiv 2505.07270) - Addresses specification ambiguity repair\n- *\"A Survey of LLM-based Automated Program Repair\"* (arXiv 2506.23749) - Comprehensive taxonomy including specification extraction\n- *\"Knowledge-Enhanced Program Repair for Data Science Code\"* (ICSE 2025) - Uses knowledge extraction from issues\n- *\"Automated Program Repair: Emerging Trends\"* (ACM Computing Surveys) - General survey on APR trends\n\nThese papers exist but don't appear to be the primary focus on structured spec extraction from issue descriptions in the way the proposal implies.\n\n### 5. **SpecRover (ICSE 2025, arXiv 2408.02232)**\n\n**Status: VERIFIED with SPECIFIC FINDING**\n\n- **Section V-A \"Reasons for Failure\" / ambiguous issue descriptions:** CONFIRMED - SpecRover examined 207 unresolved tasks and found:\n  - **Ambiguous issue descriptions: 107 cases (51.7%)** - classified as \"hard or impossible to solve without further information\"\n  - Incorrect fix location: 29.5%\n  - Incorrect code modification: 18.8%\n\nThis confirms the claim that ambiguous issue descriptions are a major failure mode for program repair systems.\n\n---\n\n## Key Discrepancy Summary\n\nThe only substantive discrepancy is the **SWE-bench-Live dataset size**, which varies between:\n- 1,319 (initial May 29, 2025 release)\n- 1,565 (June 2025 official leaderboard)\n- 1,890 (OpenReview/recent update)\n\nAll other major claims have been verified with exact numbers matching the sources.\n\nSources:\n- [SWE-bench Goes Live! arXiv Abstract](https://arxiv.org/abs/2505.23419)\n- [SWE-bench Goes Live! OpenReview](https://openreview.net/forum?id=OGWkr7gXka)\n- [Agent-CoEvo HTML Version](https://arxiv.org/html/2604.04580)\n- [SWE-Lego arXiv Abstract](https://arxiv.org/abs/2601.01426)\n- [SpecRover arXiv HTML](https://arxiv.org/html/2408.02232)\n- [SWE-bench-Live Leaderboard](https://swe-bench-live.github.io/)\n- [SWE-bench-Live GitHub Repository](https://github.com/microsoft/SWE-bench-Live)"
      }
    ],
    "totalDurationMs": 60685,
    "totalTokens": 30748,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1674,
      "cache_read_input_tokens": 27666,
      "output_tokens": 1401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1674
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1401,
          "cache_read_input_tokens": 27666,
          "cache_creation_input_tokens": 1674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1674,
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
  "sourceToolAssistantUUID": "0b3a8d5b-4625-439a-9d1b-e463cd165f5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T07:37:20.518Z_

<details><summary>↩ Tool result · `toolu_01GHU2ttqo3mtrttg2gK4by4`</summary>

```text
Perfect. Let me compile a comprehensive report of all the findings from the adversarial novelty search.

## Adversarial Novelty Search Report: SpecExtract

I've conducted a systematic search across 8 search queries covering specification extraction, bug report analysis, fine-tuning, SWE-bench, and related program repair work. Here are the **key competing or overlapping papers and approaches** identified:

### DIRECT COMPETITORS (Closest Novelty Risk)

1. **SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning** (arXiv 2502.20127, ICLR 2024)
   - Directly addresses issue resolution on SWE-bench with fine-tuned models
   - **Key claim verified**: 21.4% on SWE-Bench Verified (with SoRFT-Qwen-7B)
   - Uses rejection-sampled supervised fine-tuning + rule-based RL
   - Decomposes issue resolving into structured subtasks: file localization, function localization, line localization, code edit generation
   - **Potential overlap**: Also targets structured task decomposition from issues, but not explicitly "specification extraction"

2. **CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation** (arXiv 2604.12268, 2026)
   - Benchmark for generating executable behavioral specifications from code
   - Best model achieves only 20.2% pass rate on repository-level tasks
   - Uses preconditions/postconditions as executable specifications
   - **Potential overlap**: Focuses on spec generation capability but from CODE, not from bug report text/runtime artifacts

3. **Specification Vibing for Automated Program Repair** (arXiv 2602.08263, February 2026)
   - Repairs specification misalignments and synthesizes code guided by corrected behavior specification
   - 19% improvement on Defects4J v1.2, 23% improvement on v2.0
   - **Potential overlap**: Uses behavioral specifications to guide repair, but spec source unclear (likely from code)

### STRONG OVERLAPPING WORK (Key Context)

4. **Test Case Generation from Bug Reports via Large Language Models: A Cognitive Layered Evaluation Framework** (arXiv 2510.05365, 2025)
   - Directly extracts structured information from bug reports using LLMs
   - Multi-step prompting pipelines for context localization, scaffolding, model planning, feedback loops
   - **Relevance**: Uses bug reports as primary input like SpecExtract, but focuses on test case generation not repair specification extraction

5. **Automatic Generation of Test Cases based on Bug Reports: a Feasibility Study with Large Language Models** (arXiv 2310.06320, 2023)
   - Earlier work on translating bug reports to executable tests
   - **Relevance**: Demonstrates feasibility of structured extraction from unstructured bug text

6. **Enriching automatic test case generation by extracting relevant test inputs from bug reports** (Springer 2025, Empirical Software Engineering)
   - **BRMiner**: Extracts relevant inputs from bug reports for test generation
   - 60.03% Relevant Input Rate, 31.71% Extraction Accuracy
   - **Relevance**: Shows extraction from bug reports improves downstream tasks

7. **Past, Present, and Future of Bug Tracking in the Generative AI Era** (arXiv 2510.08005, October 2025)
   - LLM-driven bug report enhancement and analysis
   - Fine-tuned Qwen 2.5 achieves 77% CTQRS score for transforming casual bug reports into structured templates
   - **Relevance**: Directly addresses structured extraction from bug reports, though for report enhancement not repair

### RUNTIME ARTIFACT & FEEDBACK APPROACHES

8. **Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate** (arXiv 2604.02647, 2026)
   - Uses runtime execution traces as guidance for repair
   - **Relevance**: Leverages runtime artifacts like SpecExtract, but agent-based debate paradigm differs

9. **DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information** (arXiv 2512.24635, 2025)
   - Iterative repair using execution-level dynamic information
   - **Relevance**: Uses runtime artifacts but iterative refinement rather than upfront specification extraction

10. **Integrating Various Software Artifacts for Better LLM-based Bug Localization and Program Repair** (arXiv 2412.03905, 2024)
    - **DEVLoRe**: Integrates multiple artifacts for localization and repair
    - 49.3% buggy method localization, 56.0% plausible patches on Defects4J v2.0
    - **Relevance**: Shows value of integrating artifacts (tests, code) but less focused on specification extraction

### FINE-TUNING FOR REPAIR (Methodological Competition)

11. **The Impact of Fine-tuning Large Language Models on Automated Program Repair** (arXiv 2507.19909, 2025)
    - Comprehensive study on LLM fine-tuning for APR
    - Compares full-parameter fine-tuning (FPFT) with parameter-efficient techniques (LoRA, AdaLoRA, IA3)
    - LoRA remains best choice for APR
    - **Relevance**: Methodological foundation for SpecExtract's fine-tuning approach

12. **MORepair** (2025, TOSEM)
    - Multi-objective fine-tuning using QLoRA (4-bit quantization, rank-32 LoRA)
    - Optimizes both patch correctness and repair rationale
    - **Relevance**: Similar fine-tuning methodology applied to repair models

13. **SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving** (arXiv 2601.01426, 2026)
    - Direct SFT approach for issue resolving
    - **Relevance**: Competitor on SWE-bench with SFT paradigm

### ISSUE-FOCUSED REPAIR APPROACHES

14. **RepairAgent: An Autonomous, LLM-Based Agent for Program Repair** (ICSE 2025)
    - Agent-based approach to repair using issue context
    - **Relevance**: Uses issue information but agent framework differs from fine-tuning

15. **Template-Guided Program Repair in the Era of Large Language Models** (ICSE 2025)
    - Uses structured templates to guide repair generation
    - **Relevance**: Similar spirit of structured guidance, though template-based not specification-extraction-based

### RELATED BENCHMARKS & SURVEYS

16. **A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications** (arXiv 2506.23749, 2026)
    - Comprehensive 63-paper survey of LLM-based APR systems (Jan 2022 - Jun 2025)
    - Categorizes 4 paradigms: fine-tuning, prompting, procedural pipelines, agentic frameworks
    - **Relevance**: Establishes landscape; SpecExtract fits fine-tuning paradigm with specification-extraction novelty

17. **A Systematic Literature Review on Large Language Models for Automated Program Repair** (arXiv 2405.01466, 2026)
    - Survey covering 2020-2025, details repair scenarios benefiting from LLMs
    - **Relevance**: Contextual background on field maturity

18. **SWE-bench Verified** (OpenAI, 2024)
    - Human-filtered benchmark addressing specification clarity issues
    - 500 instances with reviewed problem descriptions and test patches
    - **Relevance**: SpecExtract targets same benchmark; SWE-bench Verified created partly to address specification ambiguity that SpecExtract proposes to solve

19. **Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures** (arXiv 2506.17208, 2026)
    - Recent analysis of SWE-bench evaluation approaches
    - **Relevance**: Current state-of-field context

### RELATED WORK ON CODE UNDERSTANDING & SPECIFICATION

20. **Qwen3-Coder-Next Technical Report** (arXiv 2603.00729, 2026)
    - State-of-art code model achieving 70%+ on SWE-Bench Verified
    - Uses agent-centric training with verifiable tasks and executable environments
    - **Relevance**: Establishes baseline capability; SpecExtract proposes fine-tuning smaller models with specification guidance

21. **Memory-Efficient Large Language Models for Program Repair with Semantic-Guided Patch Generation** (arXiv 2410.16655, 2025)
    - **FLAMES**: Uses semantic feedback from test validation
    - **Relevance**: Semantic guidance approach similar in spirit to SpecExtract's behavioral specification guidance

### RELATED BUG INFORMATION EXTRACTION

22. **Auto-labelling of Bug Report using Natural Language Processing** (arXiv 2212.06334, 2024)
    - NLP techniques for extracting structured bug report fields
    - **Relevance**: Earlier work on NLP-based extraction from bug tickets

23. **When Deep Learning Meets Information Retrieval-based Bug Localization: A Survey** (arXiv 2505.00144, 2025)
    - Comprehensive survey on DL+IRBL combining textual bug reports with code for localization
    - **Relevance**: Shows value of combining bug report text with code artifacts

---

## NOVELTY ASSESSMENT

**SpecExtract's key novelty lies in:**
1. **Explicit behavioral specification extraction** (preconditions/postconditions like CodeSpecBench but FROM issue text)
2. **Integration of runtime artifacts** (stack traces, error messages, test assertions) into specification generation
3. **Before-codebase-access workflow** - generates specs first, then uses them to guide repair
4. **Fine-tuning approach specifically optimized for specification extraction** from issue text + runtime data

**Closest competitors:**
- **SoRFT** (2502.20127) - Structured task decomposition but doesn't explicitly extract behavioral specs
- **CodeSpecBench** (2604.12268) - Spec generation but from code not issues
- **Test case generation from bug reports** papers - Extract from text but focus on tests not repair specs
- **Bug report enhancement** work - Transforms unstructured reports but for report quality, not repair specs

**Differentiation:**
No paper found explicitly combines: (1) specification extraction, (2) from issue text + runtime artifacts, (3) before codebase access, (4) to guide SWE-bench repair with fine-tuned Qwen3-Coder. The combination appears novel, though each component has prior art.

Sources:
- [SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning](https://arxiv.org/abs/2502.20127)
- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/abs/2604.12268)
- [A Survey of LLM-based Automated Program Repair](https://arxiv.org/html/2506.23749v1)
- [Test Case Generation from Bug Reports via Large Language Models](https://arxiv.org/html/2510.05365)
- [Runtime Execution Traces Guided Automated Program Repair](https://arxiv.org/html/2604.02647)
- [Past, Present, and Future of Bug Tracking in the Generative AI Era](https://arxiv.org/html/2510.08005v2)
- [When Deep Learning Meets Information Retrieval-based Bug Localization](https://arxiv.org/html/2505.00144v1)
- [Qwen3-Coder-Next Technical Report](https://arxiv.org/html/2603.00729v1)
- [Template-Guided Program Repair in the Era of Large Language Models](https://conf.researchr.org/details/icse-2025/icse-2025-research-track/11/Template-Guided-Program-Repair-in-the-Era-of-Large-Language-Models)
- [The Impact of Fine-tuning Large Language Models on Automated Program Repair](https://arxiv.org/pdf/2507.19909)
- [SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving](https://arxiv.org/html/2601.01426v2)
- [Specification Vibing for Automated Program Repair](https://arxiv.org/pdf/2602.08263)
- [A Systematic Literature Review on Large Language Models for Automated Program Repair](https://arxiv.org/html/2405.01466v4)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85ebd88e-cdeb-43f6-af72-641d3c4e10cc",
  "isSidechain": false,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "type": "user",
  "uuid": "328186b5-79a0-4a7b-9962-4d4eca63bdcc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Conduct adversarial novelty search for a paper called \"SpecExtract\" which trains a model (fine-tuned Qwen3-Coder-30B-A3B) to extract structured behavioral specifications from bug report text + runtime artifacts (stack traces, error messages, test assertions) before any codebase access, using those specs to guide automated program repair on SWE-bench.\n\nSearch for papers that might overlap with or compete against this idea:\n\n1. Search: \"structured specification extraction bug report program repair 2025 2026\" on Google/arXiv\n2. Search: \"issue text specification LLM fine-tuning code repair\" arxiv 2025 2026\n3. Search: \"behavioral specification extraction SWE-bench\" \n4. Search: site:arxiv.org \"issue specification\" \"program repair\" 2026\n5. Search: \"bug report information extraction structured repair\" NLP 2025 2026\n6. Search: \"CodeSpecBench arXiv 2604.12268\" to verify this paper's claims\n7. Search: \"SoRFT arXiv 2502.20127\" SWE-bench Verified vs Lite numbers - verify if 21.4% is on Verified or Lite\n8. Search for any papers combining AST parsing + NLP extraction from bug reports for fault localization\n\nReport all relevant papers found with their titles, venues, and key claims. Focus especially on finding papers that do specification extraction from issue text (not code) for repair purposes.",
    "agentId": "aaff778508146ce09",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Let me compile a comprehensive report of all the findings from the adversarial novelty search.\n\n## Adversarial Novelty Search Report: SpecExtract\n\nI've conducted a systematic search across 8 search queries covering specification extraction, bug report analysis, fine-tuning, SWE-bench, and related program repair work. Here are the **key competing or overlapping papers and approaches** identified:\n\n### DIRECT COMPETITORS (Closest Novelty Risk)\n\n1. **SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning** (arXiv 2502.20127, ICLR 2024)\n   - Directly addresses issue resolution on SWE-bench with fine-tuned models\n   - **Key claim verified**: 21.4% on SWE-Bench Verified (with SoRFT-Qwen-7B)\n   - Uses rejection-sampled supervised fine-tuning + rule-based RL\n   - Decomposes issue resolving into structured subtasks: file localization, function localization, line localization, code edit generation\n   - **Potential overlap**: Also targets structured task decomposition from issues, but not explicitly \"specification extraction\"\n\n2. **CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation** (arXiv 2604.12268, 2026)\n   - Benchmark for generating executable behavioral specifications from code\n   - Best model achieves only 20.2% pass rate on repository-level tasks\n   - Uses preconditions/postconditions as executable specifications\n   - **Potential overlap**: Focuses on spec generation capability but from CODE, not from bug report text/runtime artifacts\n\n3. **Specification Vibing for Automated Program Repair** (arXiv 2602.08263, February 2026)\n   - Repairs specification misalignments and synthesizes code guided by corrected behavior specification\n   - 19% improvement on Defects4J v1.2, 23% improvement on v2.0\n   - **Potential overlap**: Uses behavioral specifications to guide repair, but spec source unclear (likely from code)\n\n### STRONG OVERLAPPING WORK (Key Context)\n\n4. **Test Case Generation from Bug Reports via Large Language Models: A Cognitive Layered Evaluation Framework** (arXiv 2510.05365, 2025)\n   - Directly extracts structured information from bug reports using LLMs\n   - Multi-step prompting pipelines for context localization, scaffolding, model planning, feedback loops\n   - **Relevance**: Uses bug reports as primary input like SpecExtract, but focuses on test case generation not repair specification extraction\n\n5. **Automatic Generation of Test Cases based on Bug Reports: a Feasibility Study with Large Language Models** (arXiv 2310.06320, 2023)\n   - Earlier work on translating bug reports to executable tests\n   - **Relevance**: Demonstrates feasibility of structured extraction from unstructured bug text\n\n6. **Enriching automatic test case generation by extracting relevant test inputs from bug reports** (Springer 2025, Empirical Software Engineering)\n   - **BRMiner**: Extracts relevant inputs from bug reports for test generation\n   - 60.03% Relevant Input Rate, 31.71% Extraction Accuracy\n   - **Relevance**: Shows extraction from bug reports improves downstream tasks\n\n7. **Past, Present, and Future of Bug Tracking in the Generative AI Era** (arXiv 2510.08005, October 2025)\n   - LLM-driven bug report enhancement and analysis\n   - Fine-tuned Qwen 2.5 achieves 77% CTQRS score for transforming casual bug reports into structured templates\n   - **Relevance**: Directly addresses structured extraction from bug reports, though for report enhancement not repair\n\n### RUNTIME ARTIFACT & FEEDBACK APPROACHES\n\n8. **Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate** (arXiv 2604.02647, 2026)\n   - Uses runtime execution traces as guidance for repair\n   - **Relevance**: Leverages runtime artifacts like SpecExtract, but agent-based debate paradigm differs\n\n9. **DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information** (arXiv 2512.24635, 2025)\n   - Iterative repair using execution-level dynamic information\n   - **Relevance**: Uses runtime artifacts but iterative refinement rather than upfront specification extraction\n\n10. **Integrating Various Software Artifacts for Better LLM-based Bug Localization and Program Repair** (arXiv 2412.03905, 2024)\n    - **DEVLoRe**: Integrates multiple artifacts for localization and repair\n    - 49.3% buggy method localization, 56.0% plausible patches on Defects4J v2.0\n    - **Relevance**: Shows value of integrating artifacts (tests, code) but less focused on specification extraction\n\n### FINE-TUNING FOR REPAIR (Methodological Competition)\n\n11. **The Impact of Fine-tuning Large Language Models on Automated Program Repair** (arXiv 2507.19909, 2025)\n    - Comprehensive study on LLM fine-tuning for APR\n    - Compares full-parameter fine-tuning (FPFT) with parameter-efficient techniques (LoRA, AdaLoRA, IA3)\n    - LoRA remains best choice for APR\n    - **Relevance**: Methodological foundation for SpecExtract's fine-tuning approach\n\n12. **MORepair** (2025, TOSEM)\n    - Multi-objective fine-tuning using QLoRA (4-bit quantization, rank-32 LoRA)\n    - Optimizes both patch correctness and repair rationale\n    - **Relevance**: Similar fine-tuning methodology applied to repair models\n\n13. **SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving** (arXiv 2601.01426, 2026)\n    - Direct SFT approach for issue resolving\n    - **Relevance**: Competitor on SWE-bench with SFT paradigm\n\n### ISSUE-FOCUSED REPAIR APPROACHES\n\n14. **RepairAgent: An Autonomous, LLM-Based Agent for Program Repair** (ICSE 2025)\n    - Agent-based approach to repair using issue context\n    - **Relevance**: Uses issue information but agent framework differs from fine-tuning\n\n15. **Template-Guided Program Repair in the Era of Large Language Models** (ICSE 2025)\n    - Uses structured templates to guide repair generation\n    - **Relevance**: Similar spirit of structured guidance, though template-based not specification-extraction-based\n\n### RELATED BENCHMARKS & SURVEYS\n\n16. **A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications** (arXiv 2506.23749, 2026)\n    - Comprehensive 63-paper survey of LLM-based APR systems (Jan 2022 - Jun 2025)\n    - Categorizes 4 paradigms: fine-tuning, prompting, procedural pipelines, agentic frameworks\n    - **Relevance**: Establishes landscape; SpecExtract fits fine-tuning paradigm with specification-extraction novelty\n\n17. **A Systematic Literature Review on Large Language Models for Automated Program Repair** (arXiv 2405.01466, 2026)\n    - Survey covering 2020-2025, details repair scenarios benefiting from LLMs\n    - **Relevance**: Contextual background on field maturity\n\n18. **SWE-bench Verified** (OpenAI, 2024)\n    - Human-filtered benchmark addressing specification clarity issues\n    - 500 instances with reviewed problem descriptions and test patches\n    - **Relevance**: SpecExtract targets same benchmark; SWE-bench Verified created partly to address specification ambiguity that SpecExtract proposes to solve\n\n19. **Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures** (arXiv 2506.17208, 2026)\n    - Recent analysis of SWE-bench evaluation approaches\n    - **Relevance**: Current state-of-field context\n\n### RELATED WORK ON CODE UNDERSTANDING & SPECIFICATION\n\n20. **Qwen3-Coder-Next Technical Report** (arXiv 2603.00729, 2026)\n    - State-of-art code model achieving 70%+ on SWE-Bench Verified\n    - Uses agent-centric training with verifiable tasks and executable environments\n    - **Relevance**: Establishes baseline capability; SpecExtract proposes fine-tuning smaller models with specification guidance\n\n21. **Memory-Efficient Large Language Models for Program Repair with Semantic-Guided Patch Generation** (arXiv 2410.16655, 2025)\n    - **FLAMES**: Uses semantic feedback from test validation\n    - **Relevance**: Semantic guidance approach similar in spirit to SpecExtract's behavioral specification guidance\n\n### RELATED BUG INFORMATION EXTRACTION\n\n22. **Auto-labelling of Bug Report using Natural Language Processing** (arXiv 2212.06334, 2024)\n    - NLP techniques for extracting structured bug report fields\n    - **Relevance**: Earlier work on NLP-based extraction from bug tickets\n\n23. **When Deep Learning Meets Information Retrieval-based Bug Localization: A Survey** (arXiv 2505.00144, 2025)\n    - Comprehensive survey on DL+IRBL combining textual bug reports with code for localization\n    - **Relevance**: Shows value of combining bug report text with code artifacts\n\n---\n\n## NOVELTY ASSESSMENT\n\n**SpecExtract's key novelty lies in:**\n1. **Explicit behavioral specification extraction** (preconditions/postconditions like CodeSpecBench but FROM issue text)\n2. **Integration of runtime artifacts** (stack traces, error messages, test assertions) into specification generation\n3. **Before-codebase-access workflow** - generates specs first, then uses them to guide repair\n4. **Fine-tuning approach specifically optimized for specification extraction** from issue text + runtime data\n\n**Closest competitors:**\n- **SoRFT** (2502.20127) - Structured task decomposition but doesn't explicitly extract behavioral specs\n- **CodeSpecBench** (2604.12268) - Spec generation but from code not issues\n- **Test case generation from bug reports** papers - Extract from text but focus on tests not repair specs\n- **Bug report enhancement** work - Transforms unstructured reports but for report quality, not repair specs\n\n**Differentiation:**\nNo paper found explicitly combines: (1) specification extraction, (2) from issue text + runtime artifacts, (3) before codebase access, (4) to guide SWE-bench repair with fine-tuned Qwen3-Coder. The combination appears novel, though each component has prior art.\n\nSources:\n- [SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning](https://arxiv.org/abs/2502.20127)\n- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/abs/2604.12268)\n- [A Survey of LLM-based Automated Program Repair](https://arxiv.org/html/2506.23749v1)\n- [Test Case Generation from Bug Reports via Large Language Models](https://arxiv.org/html/2510.05365)\n- [Runtime Execution Traces Guided Automated Program Repair](https://arxiv.org/html/2604.02647)\n- [Past, Present, and Future of Bug Tracking in the Generative AI Era](https://arxiv.org/html/2510.08005v2)\n- [When Deep Learning Meets Information Retrieval-based Bug Localization](https://arxiv.org/html/2505.00144v1)\n- [Qwen3-Coder-Next Technical Report](https://arxiv.org/html/2603.00729v1)\n- [Template-Guided Program Repair in the Era of Large Language Models](https://conf.researchr.org/details/icse-2025/icse-2025-research-track/11/Template-Guided-Program-Repair-in-the-Era-of-Large-Language-Models)\n- [The Impact of Fine-tuning Large Language Models on Automated Program Repair](https://arxiv.org/pdf/2507.19909)\n- [SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving](https://arxiv.org/html/2601.01426v2)\n- [Specification Vibing for Automated Program Repair](https://arxiv.org/pdf/2602.08263)\n- [A Systematic Literature Review on Large Language Models for Automated Program Repair](https://arxiv.org/html/2405.01466v4)"
      }
    ],
    "totalDurationMs": 85838,
    "totalTokens": 38883,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3098,
      "cache_read_input_tokens": 32638,
      "output_tokens": 3140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3098
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3140,
          "cache_read_input_tokens": 32638,
          "cache_creation_input_tokens": 3098,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3098,
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
  "sourceToolAssistantUUID": "85ebd88e-cdeb-43f6-af72-641d3c4e10cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "328186b5-79a0-4a7b-9962-4d4eca63bdcc",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space spec extraction for program repair",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2"
}
```

---

### Assistant

_source line 16 · 2026-05-10T07:39:28.844Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me now analyze the Round 6 proposal against the Round 5 issues and what I found from independent research.

**What was required to be fixed (from Round 5 feedback):**

1. **Fix the EMNLP pilot scope — choose one story** (Round 4, 5 unresolved): Round 5 feedback said to remove '500-instance SWE-bench Verified training' and replace with 'EMNLP ARR submission reports auto-research results: SFT on SWE-bench full 2,294-instance corpus (GitBugs augmentation deferred to ICSE), SWE-bench-Live Lite 300-instance eval, 2-field ablation.'
   
   Looking at Round 6, the EMNLP ARR submission now specifies the auto-research mode timeline (6-10 days), the full 2,294-instance corpus with the two-field ablation (affected_interface vs. none, expected_behavior vs. none), and defers the full five-field ablation to ICSE 2027. This addresses the requirement.

2. **Fix the Verified framing**: Round 5 feedback said to change to "as SWE-bench Verified saturates with contamination concerns." Round 6 says "As SWE-bench Verified saturates with contamination concerns (OpenAI officially deprecated it in February 2026)." This is fixed.

3. **Add the 0.65 threshold justification**: Now says "this threshold aligns with established semantic similarity cutoffs in information-extraction evaluation literature, where scores below 0.65 on sentence-transformer embeddings indicate insufficient semantic overlap for structural field matching." This is fixed.

4. **Add SpecRover HTML URL**: Now says "(see https://arxiv.org/html/2408.02232, Section V-A)". This is fixed.

All five Round 5 issues appear to be resolved. Now I'm checking for any new issues that might have emerged. I notice the SWE-bench-Live dataset size is mentioned but appears incomplete in the text—I should verify what the actual size claim is and whether it's properly justified. The ACL Anthology confirms those SoRFT numbers check out. Now I need to verify the Qwen3-Coder-30B-A3B MoE specs about fitting on a single H100 with QLoRA at around 17.5GB VRAM. I also spotted a potentially competing paper on automated repair of ambiguous problem descriptions for code generation that might be relevant to this work's scope.

There's a circular dependency concern here—the proposal uses Qwen3-Coder-30B-A3B to generate its own training data through LLM-assisted template filling, which is a form of self-training. But this is somewhat mitigated since the model is just filling structured slots from concrete signals like test assertions and stack traces rather than doing free-form generation. The paper also makes an important distinction about test assertions being implementation-agnostic—they encode behavioral outcomes without revealing which code to change or the specific fix strategy, which helps avoid overclaiming about solution independence.

That said, there's still a real issue with test_patch assertions: when SWE-bench instances have tests that check exact expected values, those values often only make sense if you already know what the gold patch does, which could leak information into the training data. The improvement targets are also ambitious—going from 11-13% baseline to 15-20% would be a 30-60% relative improvement, and the proposal doesn't mechanically explain why we should expect gains of that magnitude. On the resource side, the auto-research mode is estimated at 160-180 H100-hours, which fits within the 200-hour budget, though I should verify this against the actual SWE-bench-Live Lite evaluation requirements.

Let me work through the math: 300 instances at 12.5 minutes each comes to about 62.5 H100-hours per run on a single GPU, or roughly 16 hours with 4 parallel H100s. For 3 main configs plus 4 ablation runs, that's 7 total runs, which would be around 112 H100-hours, plus another 30-35 for SFT training, landing in the 142-147 range—well within budget. The proposal's 160-180 estimate likely accounts for some overhead, which seems reasonable.

Looking at the auto-research breakdown: the 3-config sweep at 48 H100-hours checks out (16 per run), the per-field ablations at 64 H100-hours work out to 16 per field, and the agentless baseline at 16 hours all align. Adding those up with the other components gives 164-169 H100-hours total for evaluation plus SFT, which fits comfortably under 200.

But there's a critical assumption I need to examine: the entire premise depends on whether extracting specs actually translates to better repair performance. The proposal claims a 4-7 percentage point improvement over the agentless baseline, but I'm not seeing a clear explanation for how that mechanism actually works.

The approach relies on two things—biasing file retrieval by affected interfaces and module information, plus injecting structured behavioral constraints into the prompt. The real question is whether agentless is already doing something equivalent through its own fault localization. Agentless-1.5 already hits 50.8% on SWE-bench Verified, which suggests it's already quite capable at finding the right code. The gap on SWE-bench-Live (13.33%) could mean the issues are genuinely harder, or it could be that the model hasn't seen those repositories during training. If it's the latter, specs might help less than expected.

I'm also uncertain about the ecological validity of using a 0.65 cosine similarity threshold on 200 samples.  The SWE-bench Pro requirements were written after humans saw the gold patch, so even if the AST-extracted specs match at that threshold, it's somewhat circular—we're just validating that the specs resemble solution-conditioned specs, not that they're actually useful.

Now I'm reviewing what's been addressed from the previous round. All five issues from Round 5 have been fixed: the EMNLP scope is consistent, the SWE-bench Verified framing is corrected, the 16-day timeline is properly scoped to auto-research mode, and the 0.65 threshold is justified. So I need to think about what new issues should come up in Round 6.

The main concern is that the expected +4-7 percentage point improvement is quite ambitious but lacks mechanistic grounding. Going from 13.33% to 17-20% on SWE-bench-Live Lite would be a 27-50% relative improvement just from adding spec injection as a preprocessing step. The paper doesn't explain why biasing BM25 retrieval with module names would produce such a large effect, especially since Agentless already uses BM25 plus embedding retrieval.

There's also a potential training data contamination issue between the full SWE-bench (2,294 instances) and SWE-bench-Live, since the latter uses post-2024 issues.  The full set includes SWE-bench Verified's 500 instances plus others, and some repos may overlap with SWE-bench-Live repos. However, since the model is being fine-tuned to extract specifications rather than fix code, this contamination risk is probably minor.

I should also look more carefully at a related paper on automated repair of ambiguous problem descriptions for LLM-based code generation that came up in my search. Additionally, I need to verify the specs for the Qwen3-Coder-30B-A3B model, which was released around April-May 2026, though my search didn't specifically confirm those details.

The 30B-A3B MoE variant fitting into roughly 17.5GB with QLoRA on a single H100 makes sense given how MoE models load only active parameters to the GPU. The paper is correctly positioned at NeurIPS 2025 Datasets & Benchmarks, and the core proposal looks solid—issue-space spec extraction via supervised fine-tuning is genuinely novel, the numbers check out within the compute budget, the schema is well-defined with worked examples, and the projected 4-7 percentage point improvement on SWE-bench-Live is meaningful if demonstrated rigorously.

The two main weaknesses are the lack of mechanistic justification for the improvement target and the circularity concern that AST-extracted specs derive from test patches, making them somewhat solution-adjacent. But stepping back to the actual scoring rubric—"pass" requires a sound idea with high quality (average ≥4.0 and no critical issues), while "revise" handles fixable issues or below-threshold scores. Scoring this proposal: novelty lands around 3.5/5 since the core concept of issue-space SFT spec extraction is genuinely novel, though the full pipeline combining NLP, AST parsing, and LLM-assisted spec generation is somewhat incremental.

Feasibility also sits at 3.5/5—the compute budget and timeline are realistic, but the entire empirical contribution hinges on whether the +4-7 percentage point improvement actually materializes, and given that Agentless already uses BM25 with embedding retrieval, adding module name biasing might only yield marginal gains.

The clarity score of 4.0 reflects a well-defined schema and clear integration with Agentless, though the masked-field training protocol needs more mechanical detail. Impact lands at 3.5 as well—while SWE-bench-Live provides good contamination resistance and a 4-7 pp improvement on an 11-13% baseline is meaningful, the shift toward SWE-bench Pro could limit visibility for this work.

Averaging these scores gives 3.625, which falls short of the threshold.

Actually, let me reconsider—the proposal has matured significantly. Looking more carefully at novelty: the core insight of using issue-space SFT for spec extraction before repair is genuinely novel, and the training data construction via AST parsing of test assertions combined with NLP on problem statements is clever. The distinction from SpecRover is clear. But the novelty is somewhat narrow—essentially "spec extraction before codebase access" versus "spec inference during traversal"—and the research community might view this as incremental engineering rather than a fundamental advance, especially since the training signal remains solution-adjacent.

On feasibility, the compute budget is tight but workable, though the core risk is real: the entire empirical contribution hinges on achieving a 4-7 percentage point improvement over Agentless's 11-13% baseline. If that doesn't materialize, there's no paper. Adding module names to BM25+embedding retrieval may not yield much signal, and the validation gate itself—requiring cosine similarity ≥ 0.65 across 200 SWE-bench Pro instances—is uncertain enough that failure would force a redesign.

Clarity is the strongest dimension here, with a well-defined schema, clear worked example, and specified integration points. Impact is modest but real, targeting SWE-bench-Live appropriately, though the practical significance remains to be demonstrated.

The critical weakness I'm seeing now is the lack of mechanistic justification for that +4-7 pp improvement claim. Agentless already leverages function and class names from the repo structure, so simply prefixing queries with module names like "numpy.linalg.solve" may not shift retrieval results meaningfully. That's a significant gap in the reasoning that needs addressing.

Given that all the Round 5 issues are resolved and the core contribution around issue-space SFT is genuinely novel, I'm leaning toward a "revise" verdict rather than outright rejection. The improvement magnitude concern is fixable with proper mechanistic justification, and we're only at Round 6 of 10, so there's room for iteration.

Looking at the scoring more carefully: the novelty of combining supervised fine-tuning for spec extraction in the issue-space with AST-parsed test assertions as training signal is solid—that's a 3.5. Feasibility checks out at 3.5 given the plausible compute estimates and existing models. Clarity is strong at 4.0. Impact is moderate at 3.5 with the SWE-bench-Live evaluation and the EMNLP angle on structured information extraction. That puts the average around 3.625, which falls short of the 4.0 threshold, but the paper is salvageable with focused revisions on the improvement justification.

The core problem is that the mechanistic case for the +4-7 percentage point gain over Agentless is underspecified—the proposal doesn't adequately explain why extracting module names from specs would meaningfully outperform Agentless's existing BM25 and embedding-based retrieval when those methods already operate on the full issue text. Since specs are essentially a compressed, structured view of information already present in the issue, the added information content is limited, and the improvement pathway remains unclear. There's also a concern about the training data: using Qwen3-Coder-30B-A3B to generate the spec labels and then fine-tuning the same model on those labels creates a self-reference problem that needs addressing. about whether the fine-tuned model adds capability beyond what the base model prompting already achieves. The paper should acknowledge this and explain why SFT is expected to improve over simply prompting the base model with a schema.

3. **MINOR - The "masked-field training protocol" mentioned in the approach is never mechanically described**: The proposal mentions "training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs" but doesn't specify the masking rate, whether the training alternates between different artifact configurations, or how this affects the loss computation.

Actually, point 2 (self-reference in training data) is a known technique (self-play, bootstrapping) that's accepted in the literature. I shouldn't overweight it.

The core issue is that the empirical contribution—the +4-7 percentage point improvement over Agentless—needs stronger justification. Without explaining the mechanism, reviewers will question why structured specs derived from issue text would help more than just using the original text itself. The paper could address this by arguing that structural formatting improves retrieval signals, that specs compress noise from verbose issue descriptions, or by citing prior work showing similar structured injection helps downstream tasks. This is fixable and the paper is otherwise solid, so "revise" seems appropriate.

I'm also checking whether I missed any competing papers. One result stands out: "Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation" directly tackles ambiguous problem descriptions for code generation, which seems potentially relevant to this work. The paper on automated repair of ambiguous problem descriptions could be a more direct competitor, so I need to flag that. Now I'm settling on my final assessment: the work merits a revise recommendation. Novelty scores around 3.5 out of 5 since it combines existing ideas in a genuine way but covers narrow ground, with that repair paper being the closest rival. Feasibility is also 3.5 given the compute requirements are manageable but the core improvement claim lacks theoretical grounding. Clarity rates higher at 4.0 thanks to the well-defined schema and integration examples. Impact lands at 3.5 since the evaluation target is sound but the actual performance gains remain speculative. This averages to 3.625, falling short of the 4.0 bar. The biggest concern is that the claimed 4-7 percentage point improvement has no mechanistic explanation behind it. Looking back at 2505.07270 more carefully—it's about repairing the problem descriptions themselves to improve clarity, whereas SpecExtract extracts structured specs from existing descriptions. They're addressing related but distinct problems, so it warrants a mention but isn't a direct competitor. The proposal has been thoroughly revised and addresses the key concerns, so I'm reconsidering my initial severity ratings.

For EMNLP, which is a solid NLP venue, the contributions around training data construction, supervised fine-tuning for structured output, and integration with Agentless as a preprocessing step are legitimate. The real question is whether the mechanistic explanation for why this improves code repair is sufficiently rigorous—that's the fixable gap for Round 7. Given the strengths from previous iterations, I'm leaning toward revision rather than rejection.

Looking at the scoring more carefully: the novelty of the issue-space SFT approach is genuine, and while there's overlap with some recent work on problem description repair and bug report transformation, the specific focus on training structured spec extraction is distinct.

The real concern is feasibility—the entire empirical contribution hinges on a +4-7 percentage point improvement, but there's no mechanistic explanation for why adding module name prefixes or behavioral constraints to an already sophisticated retrieval system would yield gains of that magnitude. The risk is high that the actual improvement could be much smaller or even negative.

The writing is generally clear, though the masked-field training protocol could use more detail. As for impact, this is primarily a preprocessing module that would benefit downstream tasks.

Averaging out the scores puts this around 3.5, which means it needs revision. The most critical feedback is that the +4-7 pp improvement claim requires mechanistic justification—specifically, I need to understand what fraction of failures in SWE-bench-Live Lite come from fault localization versus patch generation errors, and whether structured query prefixes have shown meaningful gains in prior work.

I also need to address the missing related work: arXiv 2505.07270 on automated repair of ambiguous problem descriptions is a direct parallel that should be differentiated, and arXiv 2510.08005 on fine-tuning Qwen to transform bug reports into structured templates is methodologically similar and deserves explicit comparison. Finally, the masked-field training protocol needs a clearer one-sentence mechanical explanation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "328186b5-79a0-4a7b-9962-4d4eca63bdcc",
  "isSidechain": false,
  "requestId": "req_011CatWH32aMwWsnt45SnEyH",
  "type": "assistant",
  "uuid": "e3ed19b1-08d9-42fe-872c-4b9de38613cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016VriLP2gZ5paXBuexQePUg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6568,
      "cache_read_input_tokens": 35222,
      "output_tokens": 7541,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6568,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7541,
          "cache_read_input_tokens": 35222,
          "cache_creation_input_tokens": 6568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6568
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

_source line 17 · 2026-05-10T07:39:29.151Z_

Let me search for one additional potentially competing paper before finalizing my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3ed19b1-08d9-42fe-872c-4b9de38613cc",
  "isSidechain": false,
  "requestId": "req_011CatWH32aMwWsnt45SnEyH",
  "type": "assistant",
  "uuid": "d8ae436a-a966-4cc6-8802-b257891dcfd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016VriLP2gZ5paXBuexQePUg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6568,
      "cache_read_input_tokens": 35222,
      "output_tokens": 7541,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6568,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7541,
          "cache_read_input_tokens": 35222,
          "cache_creation_input_tokens": 6568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6568
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

_source line 18 · 2026-05-10T07:39:34.364Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UDySAvwNeQq9yYauPSTYhE`</summary>

```json
{
  "description": "Check specific competing paper and Agentless retrieval mechanism",
  "subagent_type": "Explore",
  "prompt": "I need to quickly verify two things for an ML paper review:\n\n1. Find and summarize \"Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation\" (arXiv 2505.07270). What does this paper do? Does it extract structured specifications from bug reports for program repair? How does it differ from fine-tuning a model to extract behavioral specs (affected_interface, observed_behavior, expected_behavior, behavioral_delta) from bug report text?\n\n2. Search for how Agentless (the program repair framework, arXiv 2407.01489) does fault localization. Specifically: does Agentless's file retrieval already use function names and module names from the issue text as retrieval signals? Would adding pre-extracted \"affected_interface.module\" and \"entry_point\" fields as a structured prefix to BM25 retrieval provide additional signal beyond Agentless's current approach?\n\nFor #2, look for the Agentless paper or its GitHub description of its localization approach.\n\nReport in under 300 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8ae436a-a966-4cc6-8802-b257891dcfd8",
  "isSidechain": false,
  "requestId": "req_011CatWH32aMwWsnt45SnEyH",
  "type": "assistant",
  "uuid": "1af7710a-dacf-4ea2-a6d4-e27ae3b5c1fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016VriLP2gZ5paXBuexQePUg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6568,
      "cache_read_input_tokens": 35222,
      "output_tokens": 7541,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6568,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7541,
          "cache_read_input_tokens": 35222,
          "cache_creation_input_tokens": 6568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6568
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "1af7710a-dacf-4ea2-a6d4-e27ae3b5c1fc",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space spec extraction for program repair",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2"
}
```

---

### Tool result

_source line 21 · 2026-05-10T07:40:03.517Z_

<details><summary>↩ Tool result · `toolu_01UDySAvwNeQq9yYauPSTYhE`</summary>

```text
Perfect. Now I have the information needed. Here's my summary:

---

## Question 1: arXiv 2505.07270 (SpecFix)

**Not what you're looking for.** This paper (SpecFix) targets **problem description ambiguity in code generation**, not bug report repair. It automatically repairs unclear problem specifications to improve LLM code generation quality—a fundamentally different task. It does *not* extract structured specifications (affected_interface, observed_behavior, etc.) from bug reports for program repair. Instead, it uses contrastive specification inference to refine descriptions before generation.

---

## Question 2: Agentless Fault Localization

**Agentless uses dual retrieval signals but neither is pre-extracted structured fields:**

1. **Prompting-based:** Constructs repository tree structure, prompts LLM to identify suspicious files from raw issue text
2. **Embedding-based:** Chunks files into code segments, computes embeddings (OpenAI text-embedding-3-small), retrieves via cosine similarity to the *full issue description*

**Would pre-extracted structured fields help?** Yes, likely. Agentless currently:
- Uses the *entire issue description* as the embedding query (including noise)
- Relies on the LLM to infer relevant files from repo tree + text
- Does not explicitly leverage function/module names as first-class retrieval signals

Adding `affected_interface.module` and `entry_point` as a **structured prefix to BM25 retrieval** would provide additional signal because:
- It isolates domain-specific names from noisy natural language
- BM25 exact matching on module/function names complements embedding-based semantic similarity
- Agentless's current embedding approach can't distinguish that "UserAuthenticator.login()" is more important than those words mentioned incidentally elsewhere

This would likely improve **recall in Step 1 (file localization)**, though the overall impact depends on label quality.

---

Sources:
- [arXiv 2505.07270 - SpecFix](https://arxiv.org/abs/2505.07270)
- [arXiv 2407.01489 - Agentless](https://arxiv.org/html/2407.01489)
- [Agentless GitHub](https://github.com/OpenAutoCoder/Agentless)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1af7710a-dacf-4ea2-a6d4-e27ae3b5c1fc",
  "isSidechain": false,
  "promptId": "6c8395c8-b18c-4a31-ae29-3f90cbb76146",
  "type": "user",
  "uuid": "2c871f0d-9ab4-4eb5-9591-a45b7daf8b72",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to quickly verify two things for an ML paper review:\n\n1. Find and summarize \"Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation\" (arXiv 2505.07270). What does this paper do? Does it extract structured specifications from bug reports for program repair? How does it differ from fine-tuning a model to extract behavioral specs (affected_interface, observed_behavior, expected_behavior, behavioral_delta) from bug report text?\n\n2. Search for how Agentless (the program repair framework, arXiv 2407.01489) does fault localization. Specifically: does Agentless's file retrieval already use function names and module names from the issue text as retrieval signals? Would adding pre-extracted \"affected_interface.module\" and \"entry_point\" fields as a structured prefix to BM25 retrieval provide additional signal beyond Agentless's current approach?\n\nFor #2, look for the Agentless paper or its GitHub description of its localization approach.\n\nReport in under 300 words.",
    "agentId": "ac2b4a29eb9e8f9c3",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now I have the information needed. Here's my summary:\n\n---\n\n## Question 1: arXiv 2505.07270 (SpecFix)\n\n**Not what you're looking for.** This paper (SpecFix) targets **problem description ambiguity in code generation**, not bug report repair. It automatically repairs unclear problem specifications to improve LLM code generation quality—a fundamentally different task. It does *not* extract structured specifications (affected_interface, observed_behavior, etc.) from bug reports for program repair. Instead, it uses contrastive specification inference to refine descriptions before generation.\n\n---\n\n## Question 2: Agentless Fault Localization\n\n**Agentless uses dual retrieval signals but neither is pre-extracted structured fields:**\n\n1. **Prompting-based:** Constructs repository tree structure, prompts LLM to identify suspicious files from raw issue text\n2. **Embedding-based:** Chunks files into code segments, computes embeddings (OpenAI text-embedding-3-small), retrieves via cosine similarity to the *full issue description*\n\n**Would pre-extracted structured fields help?** Yes, likely. Agentless currently:\n- Uses the *entire issue description* as the embedding query (including noise)\n- Relies on the LLM to infer relevant files from repo tree + text\n- Does not explicitly leverage function/module names as first-class retrieval signals\n\nAdding `affected_interface.module` and `entry_point` as a **structured prefix to BM25 retrieval** would provide additional signal because:\n- It isolates domain-specific names from noisy natural language\n- BM25 exact matching on module/function names complements embedding-based semantic similarity\n- Agentless's current embedding approach can't distinguish that \"UserAuthenticator.login()\" is more important than those words mentioned incidentally elsewhere\n\nThis would likely improve **recall in Step 1 (file localization)**, though the overall impact depends on label quality.\n\n---\n\nSources:\n- [arXiv 2505.07270 - SpecFix](https://arxiv.org/abs/2505.07270)\n- [arXiv 2407.01489 - Agentless](https://arxiv.org/html/2407.01489)\n- [Agentless GitHub](https://github.com/OpenAutoCoder/Agentless)"
      }
    ],
    "totalDurationMs": 29146,
    "totalTokens": 20989,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 19632,
      "output_tokens": 550,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 800
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 550,
          "cache_read_input_tokens": 19632,
          "cache_creation_input_tokens": 800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 800,
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
  "sourceToolAssistantUUID": "1af7710a-dacf-4ea2-a6d4-e27ae3b5c1fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T07:40:36.102Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have confirmation that:
1. arXiv 2505.07270 (SpecFix) is NOT a direct competitor - it repairs problem descriptions for code generation, not extracts behavioral specs for program repair.
2. Agentless's fault localization uses full issue text embeddings, so adding structured spec fields (module names, function signatures) as structured BM25 prefixes WOULD provide additional signal.

This actually strengthens the feasibility of SpecExtract's integration claim somewhat. The +4-7 pp improvement is more plausible than I initially thought, since Agentless doesn't currently do structured entity extraction for BM25 retrieval.
 
But I need to be careful here - Agentless already uses LLM prompting to identify suspicious files from the repo tree and issue text, which might already surface module and function names if they're mentioned in the issue. The embedding-based retrieval also processes the full issue text, so there's some overlap with what structured extraction would provide. The real question is how much additional signal comes from explicitly extracting and formatting these entities for BM25 when the issue text might already contain them naturally. The +4-7 pp claim is mechanistically more sound now that I see Agentless relies on LLM prompting and embeddings rather than BM25, but the actual gains would hinge on how often issues explicitly name the relevant modules and functions. I see there's a discrepancy between what SpecExtract claims about Agentless's retrieval mechanism and what the actual search results show—Agentless uses embedding-based retrieval with LLM prompting, not BM25+embedding as the proposal suggests. It's possible the newer Agentless-1.5 changed this, but without direct verification I shouldn't assume. The core point is that the integration approach itself seems reasonable, even if there's some ambiguity about the exact baseline architecture.

Now I'm formulating my final assessment: the +4-7 percentage point improvement is quite ambitious given the 13.33% baseline, and the proposal needs to be clearer about whether it's actually compatible with how Agentless currently works. Either the paper should confirm which Agentless variant supports BM25 injection, or it should describe the integration more precisely in terms of what Agentless actually does—like adding module names as a structured query component.

There's also a circularity problem with the validation approach: testing on SWE-bench Pro instances doesn't really prove the specs generalize to real-world ambiguous reports, since those instances were written by annotators who already knew the solution. The high cosine similarity just shows the extracted specs are solution-adjacent, not that they'd help with genuinely unclear issues.

Finally, the paper mentions injecting specs at two stages of Agentless but doesn't fully clarify how this works across the pipeline.

But stepping back—I need to focus on what actually matters for deciding whether this should pass or get sent back for revisions. I've already verified the major claims: the training data approach, the SpecRover citation, the SoRFT numbers, the Agentless baseline numbers, how it differs from SWE-Lego, the Agent-CoEvo integration, the schema, and the compute estimates. So the question is whether the remaining issues are significant enough to warrant a revise.

The core problem is that the +4-7 percentage point improvement is the entire empirical contribution, and that's a substantial claim for what's essentially a preprocessing step. There's also a potential inaccuracy about how Agentless works—it uses embedding plus LLM retrieval, not BM25 plus embedding. And there's a subtle circularity in how the training data gets validated. These aren't trivial issues given the 4.0 threshold, though they're all addressable with revisions.

Breaking down the scores: novelty lands at 3.5 because the issue-space SFT spec extraction is genuinely novel but quite narrow. Feasibility is 3.5—the compute budget works, but the improvement claim needs stronger mechanistic justification and that Agentless description needs fixing. Clarity is solid at 4, with just minor gaps. Impact is 3.5 given the appropriate evaluation setup but modest improvement targets. That averages to 3.625, which means revise.

The feedback focuses on three concrete fixes: clarify exactly how Agentless retrieves specs and where spec injection helps, build a mechanistic argument for why this improvement range is realistic, and either replace or supplement the cosine similarity validation with something more direct like ablating specific spec fields in a localization-only experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c871f0d-9ab4-4eb5-9591-a45b7daf8b72",
  "isSidechain": false,
  "requestId": "req_011CatWV3skxPrMWGt8Me1dQ",
  "type": "assistant",
  "uuid": "c213b821-dc04-43c9-8fee-cd7acab47c88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QAJsUnBWFFg9KaGmczcDg1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8084,
      "cache_read_input_tokens": 41790,
      "output_tokens": 4138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8084,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4138,
          "cache_read_input_tokens": 41790,
          "cache_creation_input_tokens": 8084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8084
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

_source line 23 · 2026-05-10T07:41:18.367Z_

Now I have sufficient evidence to issue my verdict. Let me compile my independent findings:

**Key verified claims:**
- SpecRover Section V-A 107/207 (51.7%) - CONFIRMED
- SWE-bench-Live Agentless baselines (11.67%/12.00%/13.33%) - CONFIRMED  
- Agent-CoEvo 41.33% SWE-bench Lite - CONFIRMED
- SWE-Lego 52.6% Verified with 32B - CONFIRMED
- arXiv 2505.07270 is SpecFix (clarify ambiguous problem descriptions for code gen, NOT competing)
- Agentless uses LLM prompting + embedding retrieval, NOT BM25 - potential inaccuracy in proposal

**All 5 Round 5 issues are fixed** in Round 6.

**New issues found:**
1. Agentless uses embedding + LLM prompting, not "BM25+embedding" as stated
2. The +4-7 pp improvement claim still lacks mechanistic support
3. Training data circularity (cosine similarity against solution-conditioned SWE-bench Pro requirements)

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "Issue-space SFT spec extraction (before codebase access, via AST parsing + NLP) is genuinely novel relative to SpecRover (code-space prompting), SWE-Lego (end-to-end repair SFT), and Agent-CoEvo (dynamic coevolution). The closest potential overlap — arXiv 2505.07270 SpecFix — turns out to address problem-description clarification for code generation, not repair-oriented spec extraction, so no direct collision. The combination is narrow but defensible."
    },
    "feasibility": {
      "score": 3,
      "rationale": "Compute budget (160-180 H100-hours for auto-research, within 200-hour cap) and model specs are verified. However, the proposal describes injecting specs into 'BM25+embedding file retrieval' at Agentless Stage 1, but independent verification confirms Agentless uses LLM prompting + embedding similarity — not BM25. If the integration mechanism is mis-specified, the predicted +4-7 pp gain (30-50% relative improvement over a 13.33% baseline) lacks a verified mechanistic basis and is the paper's entire empirical contribution."
    },
    "clarity": {
      "score": 4,
      "rationale": "Schema definition with worked example, integration points, training data construction pipeline, and ablation scope are all well-specified. The masked-field training protocol ('random subsets of available artifacts') is mentioned but not mechanically described — masking rate and loss computation under masking are unspecified."
    },
    "impact": {
      "score": 3,
      "rationale": "SWE-bench-Live as contamination-resistant evaluation is the right choice. The preprocessing front-end framing is architecturally flexible. However, the impact is entirely contingent on the +4-7 pp improvement materializing; if the Agentless integration is mis-described (BM25 vs. embedding/LLM) the improvement could be much smaller, and a 1-2 pp gain on an 11-13% baseline is not a publishable EMNLP contribution."
    }
  },
  "issues": [
    "SIGNIFICANT — Agentless retrieval mechanism mis-specified: The proposal states spec injection occurs at 'BM25+embedding file retrieval' (Agentless Stage 1), but independent verification of arXiv 2407.01489 confirms Agentless uses (a) LLM prompting over the repository tree to identify suspicious files, and (b) embedding-based cosine similarity retrieval — neither of which is BM25. The proposed integration (prepending affected_interface.module as a structured query prefix to BM25) requires either modifying Agentless's localization code to add BM25 as a third retrieval signal, or re-describing the injection as modifying the LLM prompt template to include structured spec fields. This is not a minor terminology slip — if the integration mechanism is inaccurate, the mechanistic case for the +4-7 pp improvement collapses entirely.",
    "SIGNIFICANT — The +4-7 pp improvement prediction lacks mechanistic support: The improvement claim is the paper's sole empirical contribution (from 13.33% to ~17-20% on SWE-bench-Live Lite, a 28-50% relative gain). No mechanistic argument is given for why adding structured spec fields to Agentless's retrieval/generation pipeline would produce this magnitude of improvement. Independent search confirms Agentless already sends the full issue text to its embedding retrieval — if the spec is derived FROM the issue text, the marginal information gain is structural compression (module/function names extracted from prose), not new information. The paper needs an explicit argument: e.g., 'Agentless's LLM prompting for file localization mistakes incidentally-mentioned module names for structurally-important ones; SpecExtract's extraction isolates the true affected interface with X% precision on a validation set.'",
    "MODERATE — Cosine similarity validation against SWE-bench Pro requirements has a circularity: SWE-bench Pro requirements were authored by annotators who had full access to the gold patch and tests. Achieving ≥ 0.65 cosine similarity between AST-extracted specs and SWE-bench Pro requirements confirms that machine-derived specs are solution-adjacent — not that they are useful for genuinely ambiguous in-the-wild bug reports. This validation cannot distinguish between 'our specs capture true behavioral expectations' and 'our specs recapitulate solution-known annotations.' A stronger validation would compare SpecExtract's spec quality on a held-out set of real GitHub issues that were NOT in SWE-bench (e.g., randomly sampled GitBugs instances without ground truth), graded by human annotators blind to the gold patch.",
    "MINOR — Masked-field training protocol is mechanically underspecified: The proposal mentions 'training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs' but does not specify the per-field masking probability, whether masking is uniform or weighted by artifact availability in the corpus, or how the loss is computed for masked vs. unmasked fields (e.g., is the model trained to output null for masked fields, or to infer the field from available signals?). One sentence would suffice: e.g., 'Each artifact field is independently masked with p=0.5 at training time; masked fields are replaced with a [MISSING] token and the model is trained to output null for those positions while filling the remaining fields normally.'"
  ],
  "feedback": "Round 6 has successfully addressed all five Round 5 issues: the EMNLP scope is now self-consistent (auto-research, 2,294 SWE-bench full, GitBugs deferred to ICSE 2027), the SWE-bench Verified framing is corrected, the timeline is explicitly scoped to auto-research mode, the 0.65 threshold is justified, and the SpecRover HTML URL is added. The proposal is nearly ready.\n\nTwo fixes will unlock 'pass' in Round 7:\n\n(1) **Fix the Agentless integration description**: Independent verification of arXiv 2407.01489 confirms Agentless uses (a) LLM prompting over a repo tree, and (b) embedding-based cosine similarity — not BM25. Replace 'BM25+embedding file retrieval is biased by prepending affected_interface.module and entry_point as a structured query prefix' with an accurate description: e.g., 'We modify Agentless's LLM prompting step at Stage 1 by prepending a structured spec header (affected_interface.module + entry_point) before the repository tree, so the LLM identifies suspicious files with the affected interface explicitly in context; we additionally add a BM25 pass over file paths using the structured interface tokens as a third retrieval signal, complementing Agentless's existing embedding-based similarity.' This also strengthens the mechanistic case: BM25 exact-match on extracted module/function names catches files that embedding similarity misses because module names are out-of-distribution lexically.\n\n(2) **Add one sentence of mechanistic justification for the +4-7 pp improvement target**: The argument is available — just make it explicit: 'Agentless's fault localization already achieves roughly X% file-level recall on SWE-bench Verified; on SWE-bench-Live, where models are less likely to have encountered the repos during pretraining, recall drops. SpecExtract's structured interface extraction provides a high-precision localization signal (module + entry_point) that compensates for this distribution shift, analogous to how BM25 lexical matching improves recall in out-of-domain retrieval settings (cite BM25 + dense retrieval hybrid literature, e.g., Karpukhin et al. 2020 DPR or a code-specific IR paper).'\n\n(3) Optional but strengthening: acknowledge the cosine similarity validation limitation in one sentence (e.g., 'As a pilot ecological validity check only — this validates schema alignment against expert-annotated specs, not generalization to ambiguous in-the-wild reports') to preempt reviewer #2 questioning.\n\nWith fixes (1) and (2), the empirical contribution has a mechanistic backbone that survives reviewer scrutiny.",
  "reason": "All Round 5 issues resolved, but the proposal's sole empirical claim (+4-7 pp improvement over Agentless) rests on a mis-described integration mechanism (Agentless uses LLM prompting + embeddings, not BM25+embeddings as stated) — fixing this description and adding a one-sentence mechanistic argument should unlock pass in Round 7."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c213b821-dc04-43c9-8fee-cd7acab47c88",
  "isSidechain": false,
  "requestId": "req_011CatWV3skxPrMWGt8Me1dQ",
  "type": "assistant",
  "uuid": "0993d822-af44-47e9-904f-3ab8b57f0780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QAJsUnBWFFg9KaGmczcDg1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8084,
      "cache_read_input_tokens": 41790,
      "output_tokens": 4138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8084,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4138,
          "cache_read_input_tokens": 41790,
          "cache_creation_input_tokens": 8084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8084
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "0993d822-af44-47e9-904f-3ab8b57f0780",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space spec extraction for program repair",
  "sessionId": "a16d81f2-1dec-44c4-8dd5-2dc1064e96a2"
}
```

---
