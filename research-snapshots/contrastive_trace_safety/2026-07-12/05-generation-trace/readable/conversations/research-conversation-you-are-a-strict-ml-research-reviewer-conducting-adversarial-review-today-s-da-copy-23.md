# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a.jsonl`
- **Structured JSON:** [`758ecdef1c23e10503ee.json`](../../sessions/75/758ecdef1c23e10503ee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T06:56:33.239Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T06:56:33.239Z",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 3/10)\n{\n  \"title\": \"SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair\",\n  \"core_problem\": \"Automated repair agents fail on ambiguous bug reports not from lack of code understanding, but because unstructured issue text leaves behavioral expectations underspecified — what interface should change, what the user observed, and what correct behavior looks like are rarely made explicit. SpecRover (ICSE 2025) partially addresses this via per-instance LLM prompting that extracts specifications from CODE during codebase traversal, yet its error analysis (Section V-A, 'Reasons for Failure') explicitly identifies that 51.7% of its 207 unresolved SWE-bench Lite tasks involve ambiguous issue descriptions (107/207 instances, as labeled by SWE-bench Verified human annotators) — a failure mode that code-side spec extraction cannot remedy. Bug reports routinely contain latent behavioral specifications in their runtime artifacts: stack traces name the affected interface, error messages describe observed behavior, and reproducer assertions encode expected behavior. No method trains a dedicated model to extract these signals from bug report text into a structured repair specification — covering affected interface, observed behavior, expected behavior, and their delta — that could constrain both fault localization and patch generation before any codebase traversal begins.\",\n  \"opportunity\": \"Failing test assertions in SWE-bench's test patches encode implementation-agnostic behavioral specifications without revealing implementation strategies: `assert result == expected_value` or `with pytest.raises(ValueError)` states precisely what the program SHOULD do, independent of WHICH code to change or HOW to change it. By mechanically converting (problem_statement + test_patch assertions + stack traces) to structured JSON spec fields using AST-level test parsing and NLP extraction on SWE-bench's 2,294 instances, we construct a training corpus of 2,294 (bug_report, structured_spec) pairs — where the spec encodes behavioral expectations derivable without knowing the implementation strategy. This avoids the critical flaw of training on SWE-bench Pro requirements, which were authored by humans with full access to the golden patch (making them solution-conditioned). SWE-bench-Live (NeurIPS 2025, arXiv 2505.23419; ~1,890 Docker-reproducible instances across 223 repositories, drawn from post-January-2024 GitHub issues, growing at ~50 instances/month) provides a clean, contamination-resistant evaluation target with no training-set overlap, replacing the officially-abandoned SWE-bench Verified. SWE-bench Pro's human-written `requirements` and `interface` fields (731 public instances) serve as an ecological validity check — we measure cosine similarity between machine-derived specs and human requirements on a held-out 200-instance slice — confirming that AST-parsed test assertions produce specs that match expert behavioral descriptions, without using requirements as training supervision.\",\n  \"landscape\": \"SpecRover (ICSE 2025, arXiv 2408.02232) is the closest prior work: given a GitHub issue, it iteratively traverses the codebase, prompting Claude 3.5 Sonnet to extract function-level summaries from visited code, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue and 46.2% on SWE-bench Verified (now contaminated). SpecRover operates in code-space (it visits source files to generate specs from code) and uses per-instance prompting (no fine-tuning). Our approach operates in issue-space (extracts specs from bug report text and runtime artifacts before any codebase traversal) and uses supervised fine-tuning (consistent structured output at ~$0.05-0.10/issue). These are complementary directions: SpecRover's code-space specs and our issue-space specs could ultimately be fused. SWE-Lego (arXiv 2601.01426, Jan 2026) is the most directly competing concurrent SFT work: it trains on 32k high-quality task instances with error masking and a difficulty-based curriculum, achieving 52.6% on SWE-bench Verified (58.8% with test-time scaling at 16 samples) using a 32B model. SWE-Lego is an end-to-end system that produces complete code fixes; SpecExtract is a preprocessing module that extracts structured behavioral specs from bug report text before any repair attempt, and can plug into SWE-Lego or any other repair backbone as a drop-in front-end — improving fault localization precision and patch generation alignment without retraining the repair agent itself. VibeRepair (arXiv 2602.08263, Feb 2026) translates buggy CODE into behavior specifications, repairs the spec, then synthesizes corrected code, achieving 19-23% improvement on Defects4J — code-space to spec, not text-space to spec. TraceRepair (arXiv 2604.02647, Apr 2026) uses runtime execution traces generated by instrumented code execution as shared repair constraints across a multi-agent committee, fixing 392 Defects4J defects — traces are generated during repair, not extracted from issue text before repair begins. RepoRepair (arXiv 2603.01048) generates hierarchical code documentation from source files toward the bug; its documentation is code-driven, not report-driven. SoRFT (arXiv 2502.20127, ACL 2025) fine-tunes on SWE-bench with RL to decompose the repair TASK into subtasks (file → function → line → edit), achieving 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite with a 7B model — it structures the repair pipeline, not the issue semantics. PathFix (arXiv 2510.14341) derives behavioral specs from static code execution paths — code-space and offline, not issue-space. The gap: no existing work trains a dedicated model to extract structured behavioral specifications from bug report text and embedded runtime artifacts, operating entirely in issue-space before codebase access.\",\n  \"approach\": \"We train SpecExtract, a Qwen3-Coder-30B-A3B model (Mixture-of-Experts: 30B total parameters, ~3B active per token — fine-tuning and inference cost scale with active parameters, comparable to a 3B dense model; fits on 2× H100 80GB with QLoRA) fine-tuned to map (bug_report_text, runtime_artifacts?) → structured JSON spec, where runtime artifacts are any combination of stack traces, error messages, test failure output, or explicit reproducer assertions present in the issue text. The model gracefully handles varying artifact availability through a masked-field training protocol: training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs. **Formal schema**: Each spec has four typed fields — (1) `affected_interface`: {module: str, signature: str|null, entry_point: str} extracted from stack frame function names and explicitly mentioned APIs; (2) `observed_behavior`: {error_type: str|null, error_message: str|null, symptom: str} from error output and user complaint; (3) `expected_behavior`: {description: str, assertions: [str]} as natural-language description plus test-style constraint strings when derivable; (4) `behavioral_delta`: str, a one-sentence expected-vs-actual summary. Worked example for a NumPy issue 'linalg.solve silently returns None for singular matrices instead of raising': {affected_interface: {module: 'numpy.linalg', entry_point: 'solve', signature: 'solve(a, b)'}, observed_behavior: {error_type: null, symptom: 'returns None for singular matrix input'}, expected_behavior: {description: 'should raise for non-invertible input', assertions: ['raises np.linalg.LinAlgError when matrix is singular']}, behavioral_delta: 'solve silently returns None instead of raising LinAlgError on singular input'}. **Training data construction (implementation-agnostic behavioral specifications)**: From SWE-bench full (2,294 instances including Verified 500 and the broader set): (1) parse `test_patch` test functions via Python AST to extract formal assertions — pytest.raises calls → error_type, assert statements → expected_behavior.assertions, decorated test function signatures → affected_interface hints; (2) extract stack traces and error strings from `problem_statement` text via regex heuristics → observed_behavior; (3) combine via LLM-assisted template fill using Qwen3-Coder-30B-A3B in a chain-of-thought extraction pass to produce coherent spec JSON; (4) validate on 200 SWE-bench Pro public instances that have non-null `requirements` and `interface` fields by computing cosine similarity (sentence-transformer) between mechanically-derived specs and human-authored requirements — target alignment ≥ 0.65 before training at scale; this validates the schema rather than using requirements as training targets. Important framing on conditionality: test assertions are written alongside gold patches and encode the behavioral outcome the fix achieves. The training specs are therefore *implementation-agnostic* — they do not reveal which code to change or the implementation strategy — rather than strictly solution-independent. This distinction is explicitly addressed in the paper to avoid overclaiming. Augment with ~3,000 pseudo-labeled GitBugs instances (arXiv 2504.09651; 150K+ open-licensed bug reports from Firefox, Cassandra, VS Code) selected for stack-trace richness and LLM-derived pseudo-specs, yielding a ~5,300-instance fine-tuning corpus. **Differentiation from SpecRover**: (1) issue-space — no codebase traversal needed at spec extraction time; (2) supervised learning — consistent, typed JSON output from a single forward pass (~$0.05-0.10/issue) vs. SpecRover's multi-step code traversal ($0.65/issue); (3) directly targets SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved SWE-bench Lite tasks) by conditioning on all available runtime artifacts in the issue, not just the code side. **Integration with Agentless**: Agentless (arXiv 2407.01489) is used as the repair backbone for all SWE-bench-Live evaluations — it follows a fixed three-stage pipeline (hierarchical fault localization → patch generation → patch selection) with no iterative tool calls, making spec injection clean and reproducible. SpecExtract specs are injected at two stages: (1) fault localization Stage 1 — BM25+embedding file retrieval is biased by prepending `affected_interface.module` and `entry_point` as a structured query prefix, pushing relevant files higher in the candidate list; (2) patch generation Stage 3 — the repair LLM receives all four spec fields as an explicit behavioral constraint header in its prompt, focusing generation on the documented delta. Agentless baseline (no spec) on SWE-bench-Live Lite (300 instances) is measured first to establish a clean delta. **Evaluation**: Primary eval on SWE-bench-Live Lite (300 instances, contamination-resistant, post-2024 issues) with Agentless as backbone; per-field ablations independently zero out each spec field to quantify individual contribution to resolve rate. Secondary eval: cosine-similarity validation on 200 SWE-bench Pro held-out instances (schema validity check). Comparison baselines: Agentless direct repair without spec, SpecRover-equivalent prompting (ablation of supervised fine-tuning benefit), SoRFT-Qwen-7B (21.4% Verified / 14.0% Lite, structured subtask decomposition), SWE-Lego (52.6% Verified, end-to-end SFT backbone — SpecExtract as preprocessing front-end demonstrates orthogonal contribution).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~90-110 H100-hours (~180-220 A100-equivalent hours)\",\n      \"gpu_breakdown\": \"SFT partition (~10-14 H100-hours): Qwen3-Coder-30B-A3B QLoRA fine-tuning on 5,300 instances, 3 epochs, 2× H100 80GB — MoE active-parameter efficiency reduces training cost to ~3B dense equivalent. Eval partition (~80-96 H100-hours): spec extraction inference on 5,300 instances (~4 H100-hours); SWE-bench-Live Lite main eval 300 instances × 12.5 min/instance / 4 parallel H100s ≈ 16 H100-hours; per-field ablations 4 fields × 300 instances ≈ 64 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~50-60% — Docker sandbox test execution during SWE-bench-Live eval is CPU-bound; GPU idles between model inference calls\",\n      \"timeline\": \"3-5 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$216-264 (90-110h × $2.40/hr H100 SXM5 on-demand; within the 200 H100-hour hard constraint)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~135-160 H100-hours (~270-380 A100-equivalent hours)\",\n      \"gpu_breakdown\": \"SFT partition (~25-35 H100-hours): 3 fine-tuning configurations (schema variant, augmentation ablation, masked-field protocol variant). Eval partition (~110-125 H100-hours): spec extraction ~5 H100-hours; Agentless baseline run on 300 instances ≈ 16 H100-hours; SWE-bench-Live partial eval 600 instances / 4 parallel ≈ 31 H100-hours; per-field ablations on 300-instance subset × 4 fields ≈ 62 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~60-70% — agent runs fine-tuning and SWE-bench-Live eval jobs continuously; human approves schema validation threshold, masked-field training protocol, retrieval bias weights, and ablation scope at daily check-ins\",\n      \"timeline\": \"5-9 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$200-400 (~2,500 orchestration turns at ~$0.10/turn Opus)\",\n      \"estimated_gpu_cost\": \"~$324-384 (135-160h × $2.40/hr H100); within the 200 H100-hour hard constraint\",\n      \"risk_note\": \"Critical unknown: whether AST-parsed test assertions produce specs that align with human behavioral descriptions (measured by cosine similarity ≥ 0.65 on 200 SWE-bench Pro validation instances). If alignment is below threshold, the spec schema needs redesign before scale-up. GitBugs pseudo-spec quality is the secondary risk — human spot-check of 100 instances recommended before augmentation scale-up.\"\n    },\n    \"auto_research\": {\n      \"note\": \"Budget-capped auto-research only — uncapped sweeps would exceed the 200 H100-hour hard constraint. Capped to 3 fine-tuning configurations × 1 retrieval variant × 1 patch-generation prompt strategy on SWE-bench-Live Lite (300 instances) for the main configuration sweep, then ablations on the best-performing config only.\",\n      \"gpu_hours\": \"~160-180 H100-hours (budget-capped)\",\n      \"gpu_breakdown\": \"SFT partition (~30-35 H100-hours): 3 QLoRA configs on 5,300 instances. Eval partition (~130-145 H100-hours): 3-config main sweep 3 × 300 instances ≈ 48 H100-hours; per-field ablations on best config 300 × 4 fields ≈ 64 H100-hours; Agentless baseline ≈ 16 H100-hours; spec extraction inference ≈ 5 H100-hours; validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~80-85% — continuous fine-tuning, inference, and SWE-bench-Live Docker eval; sandbox parallelized across 30 instances simultaneously\",\n      \"timeline\": \"6-10 days with 4 parallel H100 GPUs\",\n      \"team\": \"0 (setup only, ~3h initial configuration)\",\n      \"claude_api_cost\": \"$400-600 (~4,500 turns)\",\n      \"estimated_gpu_cost\": \"~$384-432 (160-180h × $2.40/hr H100)\",\n      \"speed_bottleneck\": \"SWE-bench-Live Docker sandbox throughput, not GPU compute; Qwen3-Coder-30B-A3B MoE inference (~3B active params) is fast and avoids multi-GPU coordination overhead that a dense 30B model would require\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026 — 15 days remaining; conference October 24-29, Budapest) — NLP angle on structured information extraction from semi-structured bug text; realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval\",\n    \"ICSE 2027 (abstract deadline June 23, 2026; full paper ~July 2026; conference April-May 2027, Dublin) — SE angle; preferred primary target for full experimental results including SWE-bench-Live partial-set ablations\",\n    \"NeurIPS 2026 (submission deadline expected May-June 2026) — systems and benchmarks angle; natural co-venue given SWE-bench-Live is NeurIPS 2025\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"SpecRover: Code Intent Extraction via LLMs (arXiv 2408.02232, ICSE 2025) — primary related work: code-space spec inference via prompting, 46.2% SWE-bench Verified, $0.65/issue; Section V-A 'Reasons for Failure' identifies 107/207 (51.7%) unresolved SWE-bench Lite tasks as 'ambiguous issue description' (labeled by SWE-bench Verified human annotators)\",\n    \"SWE-bench Goes Live! (arXiv 2505.23419, NeurIPS 2025 D&B) — primary evaluation benchmark: ~1,890 contamination-resistant instances across 223 repositories, post-2024 GitHub issues, Docker-reproducible, growing at ~50 instances/month\",\n    \"SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (arXiv 2509.16941) — schema ecological validity validator: 731 public instances with human requirements and interface fields\",\n    \"SWE-Lego (arXiv 2601.01426, Jan 2026) — most competitive concurrent SFT work: 32k training instances, difficulty-based curriculum SFT, 52.6% SWE-bench Verified (58.8% with 16-sample test-time scaling) with 32B model; end-to-end repair backbone that SpecExtract can serve as a preprocessing front-end for\",\n    \"Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489) — integration repair backbone: open-source three-stage fixed pipeline (localization → repair → validation), ~50.8% SWE-bench Verified (Agentless-1.5); spec injected at file localization (retrieval bias) and patch generation (behavioral constraint prefix) stages\",\n    \"Specification Vibing for Automated Program Repair / VibeRepair (arXiv 2602.08263, Feb 2026) — code-space spec extraction before repair, Defects4J, 19-23% improvement\",\n    \"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate / TraceRepair (arXiv 2604.02647, Apr 2026) — trace-based repair constraints during execution, Defects4J\",\n    \"SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv 2502.20127, ACL 2025) — structured repair subtask decomposition with RL, 21.4% SWE-bench Verified / 14.0% SWE-bench Lite with 7B model, key baseline\",\n    \"GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More (arXiv 2504.09651) — 150K+ open-licensed bug reports for training augmentation\",\n    \"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048)\",\n    \"On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481)\",\n    \"PathFix: Automated Program Repair with Expected Path (arXiv 2510.14341)\"\n  ],\n  \"description\": \"We introduce SpecExtract, the first supervised issue-space specification extractor for program repair: a fine-tuned Qwen3-Coder-30B-A3B model (MoE, ~3B active parameters — fine-tuning and inference cost comparable to a 3B dense model) that maps (bug_report_text, runtime_artifacts?) → a structured four-field JSON spec covering affected interface, observed behavior, expected behavior, and behavioral delta. The key methodological insight is that failing test assertions in SWE-bench test patches encode implementation-agnostic behavioral specifications — they state what the program SHOULD do without revealing which code to change or the implementation strategy — enabling AST-level test parsing combined with problem-statement NLP extraction to construct 2,294 clean (bug_report, structured_spec) training pairs from SWE-bench. GitBugs (150K+ open-licensed bug reports) provides 3,000 pseudo-labeled augmentation instances, yielding a 5,300-instance fine-tuning corpus. SWE-bench Pro public requirements serve as an ecological validity check (cosine similarity ≥ 0.65 on 200 held-out instances), not a training target. Extracted specs are integrated with Agentless as the repair backbone, injected at fault localization (retrieval biased toward affected_interface.module/entry_point) and patch generation (structured behavioral constraint prefix). Primary evaluation is on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues), with per-field ablations measuring individual spec contributions. SWE-Lego (52.6% Verified with 32B) is included as an end-to-end SFT baseline to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end rather than competing as a repair system. Differentiated from SpecRover (code-space prompting, $0.65/issue) by operating in issue-space at ~$0.05-0.10/issue — directly targeting SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved tasks) — and from SWE-Lego by producing modular, pipeline-agnostic specs that plug into any repair backbone without retraining it. Compute in H100-hours: manual mode ~90-110 H100-hours (SFT ~10-14 H100-hours, eval ~80-96 H100-hours), within the 200-hour hard constraint.\",\n  \"project_name\": \"structured_spec_repair\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Training data availability: The public SWE-bench Pro HuggingFace dataset contains 731 instances from 11 repositories with copyleft licenses. The remaining 1,134 instances (held-out: 12 repos, commercial: 18 proprietary repos) are explicitly not publicly accessible. The proposal's assumption of ~1,865 training pairs is wrong by a factor of 2.5x. At 731 instances, standard fine-tuning of a 32B Qwen3-Coder model risks severe overfitting and is far too small for reliable generalization.\", \"CRITICAL — Training signal invalidity (train-test distribution mismatch): SWE-bench Pro requirements were authored by humans with full access to the golden patch AND the passing test suite, working backward from tests to specifications. They are solution-conditioned prescriptive clarifications of already-solved problems. Real-world target bug reports are solution-ignorant descriptive complaints from confused users. Fine-tuning SpecExtract on (solution-knowing-human-written-spec → structured-spec) pairs will not teach the model to extract specs from genuinely ambiguous bug reports — it will teach it to produce post-hoc rationalizations of known solutions. This fundamental mismatch is not acknowledged and cannot be patched by synthetic augmentation alone.\", \"CRITICAL — Evaluation benchmark reliability: SWE-bench Verified shows SOTA of 93.9% (Claude Mythos Preview, May 2026) with documented evidence of data contamination — OpenAI has officially stopped recommending Verified scores for meaningful comparison. Demonstrating a statistically meaningful improvement on a benchmark where frontier models may be reproducing gold patches verbatim severely weakens the paper's empirical contribution.\", \"Novelty gap — SpecRover (ICSE 2025, arXiv 2408.02232) performs iterative code intent extraction and specification inference from GitHub issue descriptions using LLM agents (not supervised training), and achieves >50% improvement in repair rate on SWE-bench at $0.65/issue. The paper's claim that 'no prior work trains a spec extractor' is technically true but misses that SpecRover occupies the same research niche via prompting. The paper must explicitly frame what the supervised training provides that SpecRover's prompting approach cannot.\", \"Compute unit mismatch vs. hard constraint: The hard constraint is ≤200 H100-hours. All estimates are given in A100-hours. H100 is ~2–3× faster than A100 for transformer fine-tuning workloads, so 200 A100-hours ≈ 67–100 H100-hours (manual, within budget), but the auto-research mode at 800 A100-hours ≈ 300–400 H100-hours exceeds the hard constraint. The paper should explicitly reconcile resource estimates in H100-hours and confirm the primary research plan stays within budget.\", \"Structured spec schema undefined: The proposal outputs 'structured specs' with fields (affected interface, pre/post-conditions, expected/actual behavior delta), but these fields are never formally defined — no JSON schema, no field type definitions, no examples of what a valid spec looks like. SWE-bench Pro requirements are freeform prose; the conversion of freeform requirements to structured JSON is the hardest step and receives no design discussion.\", \"Data leakage if evaluation pivots to SWE-bench Pro: If the proposal trains on SWE-bench Pro (public: 731 instances) and evaluates on the same benchmark, it cannot cleanly show generalization. The community will ask whether the structured spec format was reverse-engineered from the test set rather than learned from scratch.\"]\nFeedback: The core direction — using SWE-bench Pro annotations to supervise structured specification extraction — is creative and timely, but rests on a mischaracterization of what SWE-bench Pro requirements actually are and how many are publicly accessible. To revise toward 'pass': (1) **Fix the training data premise**: Acknowledge that SWE-bench Pro public set is 731 instances, not 1,865. Address the solution-conditioned nature of the requirements by designing the training task as 'given the bug report + human requirements, produce structured spec fields,' treating the requirements as an alignment target rather than pretending they were extracted from bug reports alone. (2) **Address SpecRover directly**: Add SpecRover (ICSE 2025, arXiv 2408.02232) to the related work and explicitly argue why supervised fine-tuning generalizes better than per-instance LLM prompting — e.g., lower inference cost, better calibration, consistency across bug report styles. (3) **Replace SWE-bench Verified as primary eval**: Use SWE-bench Pro public (731 instances) with a held-out split for evaluation, and add an additional out-of-distribution eval on RepoBench or DebugBench to show generalization. Explicitly argue why SWE-bench Pro's requirements-based evaluation is the right target, not the contaminated Verified leaderboard. (4) **Define the structured spec schema**: Add a formal schema definition with field types and a worked example. Show how SWE-bench Pro freeform requirements can be automatically converted to this schema via a parsing step (this becomes its own empirical contribution). (5) **Reconcile compute in H100-hours**: Convert all estimates to H100-hours and confirm manual mode (~67–100 H100-hours) is well within the 200-hour budget. Remove or prominently caveat auto-research mode since it exceeds the hard constraint.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Model naming error: 'Qwen3-Coder-14B' does not exist. Qwen3-Coder is only available in 30B-A3B (MoE, 3B active) and 480B-A35B variants. The closest viable alternatives are Qwen3-14B (dense, base Qwen3 family) or Qwen2.5-Coder-14B (prior generation). This error must be corrected with the actual model to be used, and any VRAM/compute estimates adjusted accordingly.\", \"CRITICAL — Unverifiable SpecRover failure claim: The proposal states SpecRover 'explicitly identifies that 51.7% of its unresolved SWE-bench Lite failures stem from ambiguous issue descriptions.' This specific statistic could not be verified from the SpecRover abstract or public-facing sections. If this is an inference rather than a direct quote, it must be either verified by citing the exact section, reframed as an approximation, or removed. The entire motivation chain rests on this number.\", \"SIGNIFICANT — SoRFT baseline misrepresented: The proposal states SoRFT achieves '21.4% on SWE-bench Verified with a 7B model' but SoRFT (ACL 2025) actually reports 21.4% on SWE-bench Lite, not Verified. The Verified number for SoRFT-7B is 14.0%. Using the wrong benchmark undermines the baseline comparison.\", \"SIGNIFICANT — Integration repair agent unspecified: The primary experimental claim requires running a full end-to-end repair pipeline on SWE-bench-Live (1,890 instances) that integrates the extracted spec. The proposal does not specify which agent (SWE-agent, Moatless, Agentless, custom) is used, how the spec is injected, or what its baseline resolve rate is. Without this, the compute estimate and experimental design are incomplete.\", \"SIGNIFICANT — SWE-Lego (arXiv 2601.01426) not addressed: This January 2026 SFT-for-issue-resolving paper uses 32k training instances and a comprehensive SFT curriculum for end-to-end repair. As direct related work in the SFT-for-SWE space, its omission leaves a gap the reviewer committee will flag. The differentiation should be: SpecExtract does a spec-extraction subtask (not end-to-end repair), enabling pipeline-agnostic reuse.\", \"MODERATE — Test_patch assertion conditionality overstated: The 'non-solution-conditioned' framing is the linchpin of the training data justification, but test patches are written after/alongside gold patches and specifically designed to validate the fix. In many SWE-bench instances, assertions encode precise return values or exception types only determinable by knowing the codebase implementation. The paper should more carefully scope the claim: 'behavioral-specification-level, not implementation-level conditioned' rather than 'non-solution-conditioned.'\", \"MINOR — SWE-bench-Live size outdated: The proposal states '1,565+ instances' but the live dataset now contains 1,890 tasks across 223 repositories. Update to the current figure.\", \"MINOR — Compute budget tightness for full eval: Running a repair agent on 1,890 SWE-bench-Live instances at ~10-15 minutes/issue with 4 parallel H100s consumes approximately 79-118 H100-hours for evaluation alone, leaving 0-6 H100-hours for fine-tuning in the manual mode upper estimate. Explicitly partition the budget between SFT and eval inference.\"]\nFeedback: The Round 2 revision has substantially addressed the Round 1 critical issues: the training data premise is now grounded (SWE-bench test_patch AST parsing rather than SWE-bench Pro requirements), the evaluation target is appropriate (SWE-bench-Live), compute is expressed in H100-hours with manual mode under budget, and the JSON schema is formally defined. This is genuine progress. To advance to 'pass':\n\n(1) **Fix the model name immediately**: Replace 'Qwen3-Coder-14B' with either 'Qwen3-14B' (dense, 14B params, general Qwen3 family) or 'Qwen3-Coder-30B-A3B' (MoE, only 3B active params, faster and better for code). Qwen3-Coder-30B-A3B is the more credible choice for a coding spec-extraction task — its ~3B active parameters mean fine-tuning cost is comparable to a 3B dense model despite 30B total params.\n\n(2) **Verify or remove the 51.7% SpecRover claim**: Read SpecRover Section 4 or 5 (error analysis). If the 51.7% figure is there, cite the exact table/figure. If it's an approximation, write: 'SpecRover's error analysis identifies ambiguous issue descriptions as the dominant unresolved failure mode (Section X); our estimate from their public failure logs is ~50%.' If it's not there, reframe the motivation as: 'SpecRover's code-space approach cannot address cases where the issue description itself is underspecified — a failure mode it cannot observe.'\n\n(3) **Fix the SoRFT baseline**: Change '21.4% on SWE-bench Verified' to '21.4% on SWE-bench Lite (14.0% on Verified).' This makes SoRFT a weaker baseline, which actually helps SpecExtract's positioning.\n\n(4) **Specify the integration repair agent**: Choose one concrete agent (e.g., Agentless or Moatless) as the integration vehicle for the SWE-bench-Live evaluation. Report its baseline resolve rate, then show the SpecExtract-augmented rate. Add this as 1-2 sentences in the approach section. This is the most critical missing piece for a credible empirical narrative.\n\n(5) **Add SWE-Lego differentiation**: One paragraph acknowledging SWE-Lego (arXiv 2601.01426) as concurrent SFT work, differentiating that SpecExtract is a preprocessing spec-extraction module (not an end-to-end repair system) that can be combined with any SFT-trained or prompted repair backbone, including SWE-Lego itself.\n\n(6) **Scope the conditionality claim**: In the training data section, replace 'non-solution-conditioned' with 'implementation-agnostic behavioral specifications' to reflect that while test assertions do implicitly know the fix's behavior, they do not expose the implementation strategy, making them valid targets for behavioral spec learning.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T06:56:33.245Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T06:56:33.245Z",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-10T06:56:33.283Z_

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
  "title": "SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair",
  "core_problem": "Automated repair agents fail on ambiguous bug reports not from lack of code understanding, but because unstructured issue text leaves behavioral expectations underspecified — what interface should change, what the user observed, and what correct behavior looks like are rarely made explicit. SpecRover (ICSE 2025) partially addresses this via per-instance LLM prompting that extracts specifications from CODE during codebase traversal, yet its error analysis (Section V-A, 'Reasons for Failure') explicitly identifies that 51.7% of its 207 unresolved SWE-bench Lite tasks involve ambiguous issue descriptions (107/207 instances, as labeled by SWE-bench Verified human annotators) — a failure mode that code-side spec extraction cannot remedy. Bug reports routinely contain latent behavioral specifications in their runtime artifacts: stack traces name the affected interface, error messages describe observed behavior, and reproducer assertions encode expected behavior. No method trains a dedicated model to extract these signals from bug report text into a structured repair specification — covering affected interface, observed behavior, expected behavior, and their delta — that could constrain both fault localization and patch generation before any codebase traversal begins.",
  "opportunity": "Failing test assertions in SWE-bench's test patches encode implementation-agnostic behavioral specifications without revealing implementation strategies: `assert result == expected_value` or `with pytest.raises(ValueError)` states precisely what the program SHOULD do, independent of WHICH code to change or HOW to change it. By mechanically converting (problem_statement + test_patch assertions + stack traces) to structured JSON spec fields using AST-level test parsing and NLP extraction on SWE-bench's 2,294 instances, we construct a training corpus of 2,294 (bug_report, structured_spec) pairs — where the spec encodes behavioral expectations derivable without knowing the implementation strategy. This avoids the critical flaw of training on SWE-bench Pro requirements, which were authored by humans with full access to the golden patch (making them solution-conditioned). SWE-bench-Live (NeurIPS 2025, arXiv 2505.23419; ~1,890 Docker-reproducible instances across 223 repositories, drawn from post-January-2024 GitHub issues, growing at ~50 instances/month) provides a clean, contamination-resistant evaluation target with no training-set overlap, replacing the officially-abandoned SWE-bench Verified. SWE-bench Pro's human-written `requirements` and `interface` fields (731 public instances) serve as an ecological validity check — we measure cosine similarity between machine-derived specs and human requirements on a held-out 200-instance slice — confirming that AST-parsed test assertions produce specs that match expert behavioral descriptions, without using requirements as training supervision.",
  "landscape": "SpecRover (ICSE 2025, arXiv 2408.02232) is the closest prior work: given a GitHub issue, it iteratively traverses the codebase, prompting Claude 3.5 Sonnet to extract function-level summaries from visited code, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue and 46.2% on SWE-bench Verified (now contaminated). SpecRover operates in code-space (it visits source files to generate specs from code) and uses per-instance prompting (no fine-tuning). Our approach operates in issue-space (extracts specs from bug report text and runtime artifacts before any codebase traversal) and uses supervised fine-tuning (consistent structured output at ~$0.05-0.10/issue). These are complementary directions: SpecRover's code-space specs and our issue-space specs could ultimately be fused. SWE-Lego (arXiv 2601.01426, Jan 2026) is the most directly competing concurrent SFT work: it trains on 32k high-quality task instances with error masking and a difficulty-based curriculum, achieving 52.6% on SWE-bench Verified (58.8% with test-time scaling at 16 samples) using a 32B model. SWE-Lego is an end-to-end system that produces complete code fixes; SpecExtract is a preprocessing module that extracts structured behavioral specs from bug report text before any repair attempt, and can plug into SWE-Lego or any other repair backbone as a drop-in front-end — improving fault localization precision and patch generation alignment without retraining the repair agent itself. VibeRepair (arXiv 2602.08263, Feb 2026) translates buggy CODE into behavior specifications, repairs the spec, then synthesizes corrected code, achieving 19-23% improvement on Defects4J — code-space to spec, not text-space to spec. TraceRepair (arXiv 2604.02647, Apr 2026) uses runtime execution traces generated by instrumented code execution as shared repair constraints across a multi-agent committee, fixing 392 Defects4J defects — traces are generated during repair, not extracted from issue text before repair begins. RepoRepair (arXiv 2603.01048) generates hierarchical code documentation from source files toward the bug; its documentation is code-driven, not report-driven. SoRFT (arXiv 2502.20127, ACL 2025) fine-tunes on SWE-bench with RL to decompose the repair TASK into subtasks (file → function → line → edit), achieving 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite with a 7B model — it structures the repair pipeline, not the issue semantics. PathFix (arXiv 2510.14341) derives behavioral specs from static code execution paths — code-space and offline, not issue-space. The gap: no existing work trains a dedicated model to extract structured behavioral specifications from bug report text and embedded runtime artifacts, operating entirely in issue-space before codebase access.",
  "approach": "We train SpecExtract, a Qwen3-Coder-30B-A3B model (Mixture-of-Experts: 30B total parameters, ~3B active per token — fine-tuning and inference cost scale with active parameters, comparable to a 3B dense model; fits on 2× H100 80GB with QLoRA) fine-tuned to map (bug_report_text, runtime_artifacts?) → structured JSON spec, where runtime artifacts are any combination of stack traces, error messages, test failure output, or explicit reproducer assertions present in the issue text. The model gracefully handles varying artifact availability through a masked-field training protocol: training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs. **Formal schema**: Each spec has four typed fields — (1) `affected_interface`: {module: str, signature: str|null, entry_point: str} extracted from stack frame function names and explicitly mentioned APIs; (2) `observed_behavior`: {error_type: str|null, error_message: str|null, symptom: str} from error output and user complaint; (3) `expected_behavior`: {description: str, assertions: [str]} as natural-language description plus test-style constraint strings when derivable; (4) `behavioral_delta`: str, a one-sentence expected-vs-actual summary. Worked example for a NumPy issue 'linalg.solve silently returns None for singular matrices instead of raising': {affected_interface: {module: 'numpy.linalg', entry_point: 'solve', signature: 'solve(a, b)'}, observed_behavior: {error_type: null, symptom: 'returns None for singular matrix input'}, expected_behavior: {description: 'should raise for non-invertible input', assertions: ['raises np.linalg.LinAlgError when matrix is singular']}, behavioral_delta: 'solve silently returns None instead of raising LinAlgError on singular input'}. **Training data construction (implementation-agnostic behavioral specifications)**: From SWE-bench full (2,294 instances including Verified 500 and the broader set): (1) parse `test_patch` test functions via Python AST to extract formal assertions — pytest.raises calls → error_type, assert statements → expected_behavior.assertions, decorated test function signatures → affected_interface hints; (2) extract stack traces and error strings from `problem_statement` text via regex heuristics → observed_behavior; (3) combine via LLM-assisted template fill using Qwen3-Coder-30B-A3B in a chain-of-thought extraction pass to produce coherent spec JSON; (4) validate on 200 SWE-bench Pro public instances that have non-null `requirements` and `interface` fields by computing cosine similarity (sentence-transformer) between mechanically-derived specs and human-authored requirements — target alignment ≥ 0.65 before training at scale; this validates the schema rather than using requirements as training targets. Important framing on conditionality: test assertions are written alongside gold patches and encode the behavioral outcome the fix achieves. The training specs are therefore *implementation-agnostic* — they do not reveal which code to change or the implementation strategy — rather than strictly solution-independent. This distinction is explicitly addressed in the paper to avoid overclaiming. Augment with ~3,000 pseudo-labeled GitBugs instances (arXiv 2504.09651; 150K+ open-licensed bug reports from Firefox, Cassandra, VS Code) selected for stack-trace richness and LLM-derived pseudo-specs, yielding a ~5,300-instance fine-tuning corpus. **Differentiation from SpecRover**: (1) issue-space — no codebase traversal needed at spec extraction time; (2) supervised learning — consistent, typed JSON output from a single forward pass (~$0.05-0.10/issue) vs. SpecRover's multi-step code traversal ($0.65/issue); (3) directly targets SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved SWE-bench Lite tasks) by conditioning on all available runtime artifacts in the issue, not just the code side. **Integration with Agentless**: Agentless (arXiv 2407.01489) is used as the repair backbone for all SWE-bench-Live evaluations — it follows a fixed three-stage pipeline (hierarchical fault localization → patch generation → patch selection) with no iterative tool calls, making spec injection clean and reproducible. SpecExtract specs are injected at two stages: (1) fault localization Stage 1 — BM25+embedding file retrieval is biased by prepending `affected_interface.module` and `entry_point` as a structured query prefix, pushing relevant files higher in the candidate list; (2) patch generation Stage 3 — the repair LLM receives all four spec fields as an explicit behavioral constraint header in its prompt, focusing generation on the documented delta. Agentless baseline (no spec) on SWE-bench-Live Lite (300 instances) is measured first to establish a clean delta. **Evaluation**: Primary eval on SWE-bench-Live Lite (300 instances, contamination-resistant, post-2024 issues) with Agentless as backbone; per-field ablations independently zero out each spec field to quantify individual contribution to resolve rate. Secondary eval: cosine-similarity validation on 200 SWE-bench Pro held-out instances (schema validity check). Comparison baselines: Agentless direct repair without spec, SpecRover-equivalent prompting (ablation of supervised fine-tuning benefit), SoRFT-Qwen-7B (21.4% Verified / 14.0% Lite, structured subtask decomposition), SWE-Lego (52.6% Verified, end-to-end SFT backbone — SpecExtract as preprocessing front-end demonstrates orthogonal contribution).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~90-110 H100-hours (~180-220 A100-equivalent hours)",
      "gpu_breakdown": "SFT partition (~10-14 H100-hours): Qwen3-Coder-30B-A3B QLoRA fine-tuning on 5,300 instances, 3 epochs, 2× H100 80GB — MoE active-parameter efficiency reduces training cost to ~3B dense equivalent. Eval partition (~80-96 H100-hours): spec extraction inference on 5,300 instances (~4 H100-hours); SWE-bench-Live Lite main eval 300 instances × 12.5 min/instance / 4 parallel H100s ≈ 16 H100-hours; per-field ablations 4 fields × 300 instances ≈ 64 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.",
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
    "EMNLP 2026 (ARR submission deadline May 25, 2026 — 15 days remaining; conference October 24-29, Budapest) — NLP angle on structured information extraction from semi-structured bug text; realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval",
    "ICSE 2027 (abstract deadline June 23, 2026; full paper ~July 2026; conference April-May 2027, Dublin) — SE angle; preferred primary target for full experimental results including SWE-bench-Live partial-set ablations",
    "NeurIPS 2026 (submission deadline expected May-June 2026) — systems and benchmarks angle; natural co-venue given SWE-bench-Live is NeurIPS 2025"
  ],
  "level": "solid",
  "key_references": [
    "SpecRover: Code Intent Extraction via LLMs (arXiv 2408.02232, ICSE 2025) — primary related work: code-space spec inference via prompting, 46.2% SWE-bench Verified, $0.65/issue; Section V-A 'Reasons for Failure' identifies 107/207 (51.7%) unresolved SWE-bench Lite tasks as 'ambiguous issue description' (labeled by SWE-bench Verified human annotators)",
    "SWE-bench Goes Live! (arXiv 2505.23419, NeurIPS 2025 D&B) — primary evaluation benchmark: ~1,890 contamination-resistant instances across 223 repositories, post-2024 GitHub issues, Docker-reproducible, growing at ~50 instances/month",
    "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (arXiv 2509.16941) — schema ecological validity validator: 731 public instances with human requirements and interface fields",
    "SWE-Lego (arXiv 2601.01426, Jan 2026) — most competitive concurrent SFT work: 32k training instances, difficulty-based curriculum SFT, 52.6% SWE-bench Verified (58.8% with 16-sample test-time scaling) with 32B model; end-to-end repair backbone that SpecExtract can serve as a preprocessing front-end for",
    "Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489) — integration repair backbone: open-source three-stage fixed pipeline (localization → repair → validation), ~50.8% SWE-bench Verified (Agentless-1.5); spec injected at file localization (retrieval bias) and patch generation (behavioral constraint prefix) stages",
    "Specification Vibing for Automated Program Repair / VibeRepair (arXiv 2602.08263, Feb 2026) — code-space spec extraction before repair, Defects4J, 19-23% improvement",
    "Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate / TraceRepair (arXiv 2604.02647, Apr 2026) — trace-based repair constraints during execution, Defects4J",
    "SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv 2502.20127, ACL 2025) — structured repair subtask decomposition with RL, 21.4% SWE-bench Verified / 14.0% SWE-bench Lite with 7B model, key baseline",
    "GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More (arXiv 2504.09651) — 150K+ open-licensed bug reports for training augmentation",
    "RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048)",
    "On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481)",
    "PathFix: Automated Program Repair with Expected Path (arXiv 2510.14341)"
  ],
  "description": "We introduce SpecExtract, the first supervised issue-space specification extractor for program repair: a fine-tuned Qwen3-Coder-30B-A3B model (MoE, ~3B active parameters — fine-tuning and inference cost comparable to a 3B dense model) that maps (bug_report_text, runtime_artifacts?) → a structured four-field JSON spec covering affected interface, observed behavior, expected behavior, and behavioral delta. The key methodological insight is that failing test assertions in SWE-bench test patches encode implementation-agnostic behavioral specifications — they state what the program SHOULD do without revealing which code to change or the implementation strategy — enabling AST-level test parsing combined with problem-statement NLP extraction to construct 2,294 clean (bug_report, structured_spec) training pairs from SWE-bench. GitBugs (150K+ open-licensed bug reports) provides 3,000 pseudo-labeled augmentation instances, yielding a 5,300-instance fine-tuning corpus. SWE-bench Pro public requirements serve as an ecological validity check (cosine similarity ≥ 0.65 on 200 held-out instances), not a training target. Extracted specs are integrated with Agentless as the repair backbone, injected at fault localization (retrieval biased toward affected_interface.module/entry_point) and patch generation (structured behavioral constraint prefix). Primary evaluation is on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues), with per-field ablations measuring individual spec contributions. SWE-Lego (52.6% Verified with 32B) is included as an end-to-end SFT baseline to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end rather than competing as a repair system. Differentiated from SpecRover (code-space prompting, $0.65/issue) by operating in issue-space at ~$0.05-0.10/issue — directly targeting SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved tasks) — and from SWE-Lego by producing modular, pipeline-agnostic specs that plug into any repair backbone without retraining it. Compute in H100-hours: manual mode ~90-110 H100-hours (SFT ~10-14 H100-hours, eval ~80-96 H100-hours), within the 200-hour hard constraint.",
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
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "type": "user",
  "uuid": "daf02abe-1c03-4b7d-8bb9-faa8aa0833c1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T06:56:33.280Z_

```json
{
  "parentUuid": "daf02abe-1c03-4b7d-8bb9-faa8aa0833c1",
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
  "uuid": "928a3a2b-c9a6-47de-973c-e82b35805962",
  "timestamp": "2026-05-10T06:56:33.280Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T06:56:33.280Z_

```json
{
  "parentUuid": "928a3a2b-c9a6-47de-973c-e82b35805962",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ac4c1ab9-6d07-414c-aef6-642b4f7cdc39",
  "timestamp": "2026-05-10T06:56:33.280Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
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
  "leafUuid": "ac4c1ab9-6d07-414c-aef6-642b4f7cdc39",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify spec extraction for code repair methods",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a"
}
```

---

### Assistant

_source line 8 · 2026-05-10T06:57:02.678Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze this Round 3 review of "SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair."

The idea has gone through 2 previous revisions. Let me check what issues were raised before and what the current version addresses:

**Round 1 critical issues:**
1. Training data availability (SWE-bench Pro - 731 public instances, not 1,865)
2. Training signal invalidity (solution-conditioned requirements)
3. Evaluation benchmark reliability (SWE-bench Verified contamination)
4. SpecRover novelty gap
5. Compute unit mismatch (A100 vs H100 hours)


6. Structured spec schema undefined
7. Data leakage

**Round 2 critical issues:**
1. Model naming error ('Qwen3-Coder-14B' doesn't exist)
2. Unverifiable SpecRover failure claim (51.7%)
3. SoRFT baseline misrepresented (Lite vs Verified)
4. Integration repair agent unspecified
5. SWE-Lego not addressed
6. Test_patch assertion conditionality overstated
7. SWE-bench-Live size outdated
8. Compute budget tightness

**Round 3 fixes:**
The model naming is now corrected to "Qwen3-Coder-30B-A3B" with proper MoE specifications, and the SpecRover claim is backed up with a specific citation (107/207 instances). However, the SoRFT baseline still has the numbers flipped—it should be 21.4% on Lite and 14.0% on Verified, not the other way around.

The integration repair agent is properly attributed to Agentless, SWE-Lego has clear differentiation, and the conditionality issue is addressed with "implementation-agnostic behavioral specifications." SWE-bench-Live is now sized at ~1,890 Docker-reproducible instances, and compute partitioning is explicitly split between SFT and eval phases.

But I need to fix that SoRFT reversal immediately—the current phrasing still has it backwards. I see the issue clearly now — SoRFT's numbers are inverted in the current version, with 21.4% listed for Verified when it should be for Lite, and 14.0% for Lite when it should be for Verified. This was explicitly flagged in the previous review and somehow still wasn't corrected. Now I need to verify the actual claims in this proposal by checking the original papers and sources directly, starting with SoRFT's real performance numbers, then moving through the other key benchmarks and model availability claims like SWE-bench Pro's instance count, the status of SWE-bench Live, and whether models like Qwen3-Coder and datasets like GitBugs are actually available. I need to verify several more claims about model performance and paper details, then strategically plan my searches to cross-check everything in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac4c1ab9-6d07-414c-aef6-642b4f7cdc39",
  "isSidechain": false,
  "requestId": "req_011CatTAeErPyAmK9U6Wd5KL",
  "type": "assistant",
  "uuid": "58072222-9263-4d43-a2af-42b582fad6c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Drmv5kkUwmDqqJy8bWXvfZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17870,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3663,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3663,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17870
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

_source line 9 · 2026-05-10T06:57:02.684Z_

I'll conduct independent verification of this Round 3 proposal's claims before issuing a verdict. Let me run parallel searches across the key dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58072222-9263-4d43-a2af-42b582fad6c6",
  "isSidechain": false,
  "requestId": "req_011CatTAeErPyAmK9U6Wd5KL",
  "type": "assistant",
  "uuid": "859eef4d-ef90-459c-b733-930fb8924b3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Drmv5kkUwmDqqJy8bWXvfZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17870,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3663,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3663,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17870
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

_source line 10 · 2026-05-10T06:57:10.181Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MxMTtovJgVW33zG1BCHRbW`</summary>

```json
{
  "description": "Verify SoRFT paper numbers and SpecRover failure analysis",
  "subagent_type": "Explore",
  "prompt": "I need to verify specific numbers from two NLP/code papers for an adversarial review. Please search for:\n\n1. **SoRFT paper** (arXiv 2502.20127, \"SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning\", ACL 2025): \n   - Search for the paper and find its actual performance numbers on SWE-bench Lite and SWE-bench Verified\n   - The question is: does SoRFT-7B achieve 21.4% on SWE-bench Lite or SWE-bench Verified? And what is the number for the other benchmark?\n   - Try: site:arxiv.org SoRFT subtask reinforced fine-tuning SWE-bench\n   - Try: \"SoRFT\" SWE-bench Lite Verified results 2025\n\n2. **SpecRover paper** (arXiv 2408.02232, ICSE 2025): \n   - Does it have a Section V-A or error analysis that identifies \"51.7%\" or \"107/207\" instances failing due to \"ambiguous issue descriptions\"?\n   - Try: site:arxiv.org SpecRover code intent extraction LLM SWE-bench 2408.02232\n   - Try: SpecRover ICSE 2025 failure analysis ambiguous issue description\n\nReport back the actual numbers found for SoRFT, and what SpecRover's error analysis actually says (verbatim if possible)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "859eef4d-ef90-459c-b733-930fb8924b3d",
  "isSidechain": false,
  "requestId": "req_011CatTAeErPyAmK9U6Wd5KL",
  "type": "assistant",
  "uuid": "34b7980f-3708-457c-880f-0abfeb1fe42e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Drmv5kkUwmDqqJy8bWXvfZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17870,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3663,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3663,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17870
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

_source line 11 · 2026-05-10T06:57:19.053Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KqLciTxt978ArrXaDsBLHc`</summary>

```json
{
  "description": "Verify SWE-bench Live, SWE-Lego, and GitBugs paper existence",
  "subagent_type": "Explore",
  "prompt": "I need to verify the existence and details of several papers cited in a research proposal for an adversarial review. Please search for each and confirm whether they exist:\n\n1. **SWE-bench Goes Live** (arXiv 2505.23419): \"SWE-bench Goes Live!\" - claimed to be NeurIPS 2025, with ~1,890 Docker-reproducible instances across 223 repositories, post-January-2024 GitHub issues\n   - Search: site:arxiv.org 2505.23419\n   - Search: \"SWE-bench Goes Live\" NeurIPS 2025 benchmark\n\n2. **SWE-Lego** (arXiv 2601.01426): January 2026 paper on SFT for issue resolving, 32k training instances, difficulty-based curriculum, claimed 52.6% SWE-bench Verified\n   - Search: site:arxiv.org SWE-Lego 2601.01426\n   - Search: \"SWE-Lego\" curriculum SFT SWE-bench 2026\n\n3. **GitBugs** (arXiv 2504.09651): \"GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More\" - 150K+ open-licensed bug reports from Firefox, Cassandra, VS Code\n   - Search: site:arxiv.org 2504.09651 GitBugs bug reports\n\n4. **VibeRepair** (arXiv 2602.08263): February 2026 paper on translating buggy code to behavior specs, then repairing spec, achieving 19-23% improvement on Defects4J\n   - Search: site:arxiv.org 2602.08263 VibeRepair\n\n5. **TraceRepair** (arXiv 2604.02647): April 2026 paper on runtime execution traces for multi-agent repair on Defects4J\n   - Search: site:arxiv.org 2604.02647 TraceRepair\n\nFor each paper, confirm: Does it exist? Are the claimed arXiv IDs correct? Are the venue claims accurate? Report exact title and abstract details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34b7980f-3708-457c-880f-0abfeb1fe42e",
  "isSidechain": false,
  "requestId": "req_011CatTAeErPyAmK9U6Wd5KL",
  "type": "assistant",
  "uuid": "9ef8e539-b6e7-4ff6-aac9-905f5e9fd022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Drmv5kkUwmDqqJy8bWXvfZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17870,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3663,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3663,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17870
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

_source line 12 · 2026-05-10T06:57:27.897Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01G1BUHczLWPipAJGzLhDsZ8`</summary>

```json
{
  "description": "Search for concurrent work on bug report specification extraction",
  "subagent_type": "Explore",
  "prompt": "I'm doing an adversarial literature review for a paper called \"SpecExtract\" which proposes: training a model to extract structured behavioral specifications from bug report text (stack traces, error messages, test assertions) to guide automated program repair. The model extracts: affected interface, observed behavior, expected behavior, and behavioral delta. It's trained on SWE-bench test patch assertions.\n\nPlease search for concurrent or competing work that the authors might have missed:\n\n1. **Bug report information extraction / specification extraction**:\n   - Search: \"bug report\" \"specification extraction\" NLP 2025 2026\n   - Search: site:arxiv.org structured information extraction bug reports program repair 2025\n\n2. **Issue-to-spec methods for code repair**:\n   - Search: site:arxiv.org \"issue description\" specification \"program repair\" 2025 2026\n   - Search: \"behavioral specification\" \"bug report\" automatic extraction 2026\n\n3. **Test assertion-based specification mining**:\n   - Search: \"test assertions\" specification mining program repair 2025 2026\n   - Search: site:arxiv.org test patch specification behavioral constraints repair\n\n4. **SWE-bench training data approaches**:\n   - Search: site:arxiv.org SWE-bench training data specification structured 2025 2026\n   - Search: SWE-bench fine-tuning specifications behavioral extraction 2026\n\n5. **Information extraction for debugging/repair**:\n   - Search: site:arxiv.org \"stack trace\" NLP information extraction repair 2025\n   - Search: site:paperswithcode.com bug report structured extraction program repair\n\nReport any papers that directly overlap with SpecExtract's approach of (a) extracting structured specs from bug report text, (b) using test assertions as training signal for spec learning, or (c) injecting specs into fault localization or patch generation pipelines."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ef8e539-b6e7-4ff6-aac9-905f5e9fd022",
  "isSidechain": false,
  "requestId": "req_011CatTAeErPyAmK9U6Wd5KL",
  "type": "assistant",
  "uuid": "49f63263-d3ad-4cec-aaf7-05b11e4fa171",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Drmv5kkUwmDqqJy8bWXvfZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17870,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3663,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3663,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17870
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

_source line 13 · 2026-05-10T06:57:36.072Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Q61n9LQb2NxVn9dtKtzexw`</summary>

```json
{
  "description": "Verify Qwen3-Coder and Agentless model capabilities",
  "subagent_type": "Explore",
  "prompt": "I need to verify details about two AI models/systems for an adversarial review:\n\n1. **Qwen3-Coder-30B-A3B**: The proposal claims this is a Mixture-of-Experts model with 30B total parameters, ~3B active per token, fits on 2× H100 80GB with QLoRA, and fine-tuning cost is comparable to a 3B dense model.\n   - Search: site:huggingface.co Qwen3-Coder-30B-A3B\n   - Search: \"Qwen3-Coder\" 30B MoE active parameters specifications\n   - Does this model exist? What are its actual specs (VRAM requirements, parameter counts)?\n   - Is \"2× H100 80GB with QLoRA\" realistic for fine-tuning a 30B MoE?\n\n2. **Agentless-1.5** (arXiv 2407.01489): The proposal claims \"~50.8% SWE-bench Verified (Agentless-1.5)\"\n   - Search: Agentless-1.5 SWE-bench Verified performance 2025\n   - Search: site:arxiv.org Agentless SWE-bench 2407.01489\n   - What is Agentless-1.5's actual SWE-bench Verified score?\n   - Is Agentless an open-source three-stage fixed pipeline as claimed?\n\n3. **SWE-bench Verified current SOTA** (as of May 2026):\n   - Search: site:paperswithcode.com SWE-bench Verified leaderboard\n   - Search: SWE-bench Verified SOTA 2026 May results\n   - What is the actual current SOTA on SWE-bench Verified? The proposal mentions \"Claude Mythos Preview\" at 93.9% somewhere.\n\nReport actual numbers and whether the model/system claims are accurate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49f63263-d3ad-4cec-aaf7-05b11e4fa171",
  "isSidechain": false,
  "requestId": "req_011CatTAeErPyAmK9U6Wd5KL",
  "type": "assistant",
  "uuid": "57945dff-d571-41e6-9514-714cc011cc7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Drmv5kkUwmDqqJy8bWXvfZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17870,
      "cache_read_input_tokens": 11631,
      "output_tokens": 3663,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3663,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17870
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

_source line 14 · 2026-05-10T06:57:39.356Z_

<details><summary>↩ Tool result · `toolu_01KqLciTxt978ArrXaDsBLHc`</summary>

```text
## Verification Results

I've searched for all five papers. Here's my findings:

### 1. **SWE-bench Goes Live** (arXiv 2505.23419) ✓ EXISTS

**Status:** VERIFIED
- **arXiv ID:** 2505.23419 - CORRECT
- **Title:** "SWE-bench Goes Live!" - CORRECT
- **Venue:** NeurIPS 2025 (Datasets and Benchmarks track) - CORRECT
- **Dataset Size:** The paper claims 1,890 Docker-reproducible instances across 223 repositories - CORRECT
- **GitHub Issues:** Post-January-2024 (specifically since 2024) - CORRECT
- **Authors:** Linghao Zhang, Shilin He, Chaoyun Zhang, and colleagues from Microsoft Research

### 2. **SWE-Lego** (arXiv 2601.01426) ✓ EXISTS

**Status:** VERIFIED
- **arXiv ID:** 2601.01426 - CORRECT
- **Title:** "SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving" - CORRECT
- **Date:** January 4, 2026 - CORRECT
- **SFT Training:** 32k task instances + 18k validated trajectories - CORRECT
- **Curriculum:** Difficulty-based curriculum with error masking - CORRECT
- **Performance:** SWE-Lego-Qwen3-32B achieves 52.6% on SWE-bench Verified - CORRECT

### 3. **GitBugs** (arXiv 2504.09651) ✓ EXISTS

**Status:** VERIFIED
- **arXiv ID:** 2504.09651 - CORRECT
- **Title:** "GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, Triage, and More" - CORRECT (slightly more complete than cited)
- **Dataset Size:** 150,000+ bug reports - CORRECT
- **Projects:** Includes Firefox, Cassandra, VS Code, plus Hadoop, HBase, Mozilla Core, Seamonkey, Spark, Thunderbird - CORRECT (open-licensed from GitHub/Bugzilla/Jira)
- **Code/Data:** Available at https://github.com/av9ash/gitbugs/

### 4. **VibeRepair** (arXiv 2602.08263) ✓ EXISTS

**Status:** VERIFIED
- **arXiv ID:** 2602.08263 - CORRECT
- **Title:** "Specification Vibing for Automated Program Repair" - CORRECT (actual title differs slightly from "VibeRepair")
- **Date:** February 9, 2026 - CORRECT
- **Approach:** Translates buggy code to behavior specs, repairs spec, generates repaired code - CORRECT
- **Performance on Defects4J v1.2:** 174 bugs fixed (28 bug improvement = 19% over baseline) - CORRECT
- **Performance on Defects4J v2.0:** 178 bugs fixed (33 bug improvement = 23% over baseline) - CORRECT
- **Authors:** Taohong Zhu, Lucas C. Cordeiro, Mustafa A. Mustafa, Youcheng Sun

### 5. **TraceRepair** (arXiv 2604.02647) ✓ EXISTS

**Status:** VERIFIED
- **arXiv ID:** 2604.02647 - CORRECT
- **Title:** "Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate" - CORRECT
- **Date:** April 3, 2026 - CORRECT
- **Approach:** Uses runtime execution traces for multi-agent repair with probe agent and committee agents - CORRECT
- **Performance:** Fixes 392 defects on Defects4J benchmark
- **Additional Benchmark:** Constructed Recent-Java benchmark for robustness testing

---

## Summary

**All five papers exist and are accurately cited.** The arXiv IDs, titles, venues, and claimed results are all verifiable. The proposal citations appear to be legitimate and current as of the search date (May 2026).

Sources:
- [SWE-bench Goes Live! - arXiv:2505.23419](https://arxiv.org/abs/2505.23419)
- [SWE-Lego - arXiv:2601.01426](https://arxiv.org/abs/2601.01426)
- [GitBugs - arXiv:2504.09651](https://arxiv.org/abs/2504.09651)
- [Specification Vibing for Automated Program Repair - arXiv:2602.08263](https://arxiv.org/abs/2602.08263)
- [Runtime Execution Traces Guided Automated Program Repair - arXiv:2604.02647](https://arxiv.org/abs/2604.02647)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ef8e539-b6e7-4ff6-aac9-905f5e9fd022",
  "isSidechain": false,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "type": "user",
  "uuid": "9eeda77a-4e6d-4949-babb-8c02cdc44a1e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify the existence and details of several papers cited in a research proposal for an adversarial review. Please search for each and confirm whether they exist:\n\n1. **SWE-bench Goes Live** (arXiv 2505.23419): \"SWE-bench Goes Live!\" - claimed to be NeurIPS 2025, with ~1,890 Docker-reproducible instances across 223 repositories, post-January-2024 GitHub issues\n   - Search: site:arxiv.org 2505.23419\n   - Search: \"SWE-bench Goes Live\" NeurIPS 2025 benchmark\n\n2. **SWE-Lego** (arXiv 2601.01426): January 2026 paper on SFT for issue resolving, 32k training instances, difficulty-based curriculum, claimed 52.6% SWE-bench Verified\n   - Search: site:arxiv.org SWE-Lego 2601.01426\n   - Search: \"SWE-Lego\" curriculum SFT SWE-bench 2026\n\n3. **GitBugs** (arXiv 2504.09651): \"GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More\" - 150K+ open-licensed bug reports from Firefox, Cassandra, VS Code\n   - Search: site:arxiv.org 2504.09651 GitBugs bug reports\n\n4. **VibeRepair** (arXiv 2602.08263): February 2026 paper on translating buggy code to behavior specs, then repairing spec, achieving 19-23% improvement on Defects4J\n   - Search: site:arxiv.org 2602.08263 VibeRepair\n\n5. **TraceRepair** (arXiv 2604.02647): April 2026 paper on runtime execution traces for multi-agent repair on Defects4J\n   - Search: site:arxiv.org 2604.02647 TraceRepair\n\nFor each paper, confirm: Does it exist? Are the claimed arXiv IDs correct? Are the venue claims accurate? Report exact title and abstract details.",
    "agentId": "a1ac6ca4047c4969a",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Verification Results\n\nI've searched for all five papers. Here's my findings:\n\n### 1. **SWE-bench Goes Live** (arXiv 2505.23419) ✓ EXISTS\n\n**Status:** VERIFIED\n- **arXiv ID:** 2505.23419 - CORRECT\n- **Title:** \"SWE-bench Goes Live!\" - CORRECT\n- **Venue:** NeurIPS 2025 (Datasets and Benchmarks track) - CORRECT\n- **Dataset Size:** The paper claims 1,890 Docker-reproducible instances across 223 repositories - CORRECT\n- **GitHub Issues:** Post-January-2024 (specifically since 2024) - CORRECT\n- **Authors:** Linghao Zhang, Shilin He, Chaoyun Zhang, and colleagues from Microsoft Research\n\n### 2. **SWE-Lego** (arXiv 2601.01426) ✓ EXISTS\n\n**Status:** VERIFIED\n- **arXiv ID:** 2601.01426 - CORRECT\n- **Title:** \"SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving\" - CORRECT\n- **Date:** January 4, 2026 - CORRECT\n- **SFT Training:** 32k task instances + 18k validated trajectories - CORRECT\n- **Curriculum:** Difficulty-based curriculum with error masking - CORRECT\n- **Performance:** SWE-Lego-Qwen3-32B achieves 52.6% on SWE-bench Verified - CORRECT\n\n### 3. **GitBugs** (arXiv 2504.09651) ✓ EXISTS\n\n**Status:** VERIFIED\n- **arXiv ID:** 2504.09651 - CORRECT\n- **Title:** \"GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, Triage, and More\" - CORRECT (slightly more complete than cited)\n- **Dataset Size:** 150,000+ bug reports - CORRECT\n- **Projects:** Includes Firefox, Cassandra, VS Code, plus Hadoop, HBase, Mozilla Core, Seamonkey, Spark, Thunderbird - CORRECT (open-licensed from GitHub/Bugzilla/Jira)\n- **Code/Data:** Available at https://github.com/av9ash/gitbugs/\n\n### 4. **VibeRepair** (arXiv 2602.08263) ✓ EXISTS\n\n**Status:** VERIFIED\n- **arXiv ID:** 2602.08263 - CORRECT\n- **Title:** \"Specification Vibing for Automated Program Repair\" - CORRECT (actual title differs slightly from \"VibeRepair\")\n- **Date:** February 9, 2026 - CORRECT\n- **Approach:** Translates buggy code to behavior specs, repairs spec, generates repaired code - CORRECT\n- **Performance on Defects4J v1.2:** 174 bugs fixed (28 bug improvement = 19% over baseline) - CORRECT\n- **Performance on Defects4J v2.0:** 178 bugs fixed (33 bug improvement = 23% over baseline) - CORRECT\n- **Authors:** Taohong Zhu, Lucas C. Cordeiro, Mustafa A. Mustafa, Youcheng Sun\n\n### 5. **TraceRepair** (arXiv 2604.02647) ✓ EXISTS\n\n**Status:** VERIFIED\n- **arXiv ID:** 2604.02647 - CORRECT\n- **Title:** \"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate\" - CORRECT\n- **Date:** April 3, 2026 - CORRECT\n- **Approach:** Uses runtime execution traces for multi-agent repair with probe agent and committee agents - CORRECT\n- **Performance:** Fixes 392 defects on Defects4J benchmark\n- **Additional Benchmark:** Constructed Recent-Java benchmark for robustness testing\n\n---\n\n## Summary\n\n**All five papers exist and are accurately cited.** The arXiv IDs, titles, venues, and claimed results are all verifiable. The proposal citations appear to be legitimate and current as of the search date (May 2026).\n\nSources:\n- [SWE-bench Goes Live! - arXiv:2505.23419](https://arxiv.org/abs/2505.23419)\n- [SWE-Lego - arXiv:2601.01426](https://arxiv.org/abs/2601.01426)\n- [GitBugs - arXiv:2504.09651](https://arxiv.org/abs/2504.09651)\n- [Specification Vibing for Automated Program Repair - arXiv:2602.08263](https://arxiv.org/abs/2602.08263)\n- [Runtime Execution Traces Guided Automated Program Repair - arXiv:2604.02647](https://arxiv.org/abs/2604.02647)"
      }
    ],
    "totalDurationMs": 20299,
    "totalTokens": 24516,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 2482,
      "cache_creation_input_tokens": 3736,
      "cache_read_input_tokens": 17095,
      "output_tokens": 1203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3736
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2482,
          "output_tokens": 1203,
          "cache_read_input_tokens": 17095,
          "cache_creation_input_tokens": 3736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3736,
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
  "sourceToolAssistantUUID": "9ef8e539-b6e7-4ff6-aac9-905f5e9fd022",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T06:57:40.393Z_

<details><summary>↩ Tool result · `toolu_01MxMTtovJgVW33zG1BCHRbW`</summary>

```text
Perfect! I now have the key information. Let me report my findings:

## Verification Results

### SoRFT Paper (arXiv 2502.20127, ACL 2025)

**ANSWER TO YOUR FIRST QUESTION:** The 21.4% figure applies to **SWE-bench Verified**, not SWE-bench Lite.

**Exact Performance Numbers:**
- **SoRFT-Qwen-7B on SWE-bench Verified: 21.4%**
- **SoRFT-Qwen-7B on SWE-bench Lite: 14.0%**

For the larger model:
- SoRFT-Qwen-32B on SWE-bench Verified: 30.8%
- SoRFT-Qwen-32B on SWE-bench Lite: 24.0%

The paper notes that with RL training, the 7B model improved from 18.0% (SFT alone) to 21.4% on Verified.

### SpecRover Paper (arXiv 2408.02232, ICSE 2025)

**ANSWER TO YOUR SECOND QUESTION:** The specific numbers you mentioned (51.7% or 107/207) **do not appear** in the SpecRover paper.

**What the paper actually contains:**
The SpecRover paper reports overall success metrics (19.31% on full SWE-Bench, 31.00% on SWE-Bench Lite) and claims 50% improvement over AutoCodeRover. However, it **does not have a dedicated error analysis section** that breaks down failures by root cause, such as "ambiguous issue descriptions." While the paper discusses specification inference and patch validation, it does not provide granular failure statistics categorized by ambiguity or specific failure modes.

---

**For your adversarial review:** You should note that SoRFT's 21.4% result is on the more challenging SWE-bench Verified benchmark, not Lite. And the SpecRover paper appears not to contain the specific error analysis breakdown you're checking for—if those numbers exist, they may be in a different paper or appendix.

Sources:
- [SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv HTML)](https://arxiv.org/html/2502.20127)
- [SoRFT on arXiv](https://arxiv.org/abs/2502.20127)
- [SpecRover: Code Intent Extraction via LLMs (arXiv HTML)](https://arxiv.org/html/2408.02232v3)
- [SpecRover on arXiv](https://arxiv.org/abs/2408.02232)
- [SoRFT on ACL Anthology](https://aclanthology.org/2025.acl-long.559/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34b7980f-3708-457c-880f-0abfeb1fe42e",
  "isSidechain": false,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "type": "user",
  "uuid": "14b133c0-9236-47d7-ade1-7f75dcbb9775",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify specific numbers from two NLP/code papers for an adversarial review. Please search for:\n\n1. **SoRFT paper** (arXiv 2502.20127, \"SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning\", ACL 2025): \n   - Search for the paper and find its actual performance numbers on SWE-bench Lite and SWE-bench Verified\n   - The question is: does SoRFT-7B achieve 21.4% on SWE-bench Lite or SWE-bench Verified? And what is the number for the other benchmark?\n   - Try: site:arxiv.org SoRFT subtask reinforced fine-tuning SWE-bench\n   - Try: \"SoRFT\" SWE-bench Lite Verified results 2025\n\n2. **SpecRover paper** (arXiv 2408.02232, ICSE 2025): \n   - Does it have a Section V-A or error analysis that identifies \"51.7%\" or \"107/207\" instances failing due to \"ambiguous issue descriptions\"?\n   - Try: site:arxiv.org SpecRover code intent extraction LLM SWE-bench 2408.02232\n   - Try: SpecRover ICSE 2025 failure analysis ambiguous issue description\n\nReport back the actual numbers found for SoRFT, and what SpecRover's error analysis actually says (verbatim if possible).",
    "agentId": "ad56e0f2ccf31b19b",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I now have the key information. Let me report my findings:\n\n## Verification Results\n\n### SoRFT Paper (arXiv 2502.20127, ACL 2025)\n\n**ANSWER TO YOUR FIRST QUESTION:** The 21.4% figure applies to **SWE-bench Verified**, not SWE-bench Lite.\n\n**Exact Performance Numbers:**\n- **SoRFT-Qwen-7B on SWE-bench Verified: 21.4%**\n- **SoRFT-Qwen-7B on SWE-bench Lite: 14.0%**\n\nFor the larger model:\n- SoRFT-Qwen-32B on SWE-bench Verified: 30.8%\n- SoRFT-Qwen-32B on SWE-bench Lite: 24.0%\n\nThe paper notes that with RL training, the 7B model improved from 18.0% (SFT alone) to 21.4% on Verified.\n\n### SpecRover Paper (arXiv 2408.02232, ICSE 2025)\n\n**ANSWER TO YOUR SECOND QUESTION:** The specific numbers you mentioned (51.7% or 107/207) **do not appear** in the SpecRover paper.\n\n**What the paper actually contains:**\nThe SpecRover paper reports overall success metrics (19.31% on full SWE-Bench, 31.00% on SWE-Bench Lite) and claims 50% improvement over AutoCodeRover. However, it **does not have a dedicated error analysis section** that breaks down failures by root cause, such as \"ambiguous issue descriptions.\" While the paper discusses specification inference and patch validation, it does not provide granular failure statistics categorized by ambiguity or specific failure modes.\n\n---\n\n**For your adversarial review:** You should note that SoRFT's 21.4% result is on the more challenging SWE-bench Verified benchmark, not Lite. And the SpecRover paper appears not to contain the specific error analysis breakdown you're checking for—if those numbers exist, they may be in a different paper or appendix.\n\nSources:\n- [SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv HTML)](https://arxiv.org/html/2502.20127)\n- [SoRFT on arXiv](https://arxiv.org/abs/2502.20127)\n- [SpecRover: Code Intent Extraction via LLMs (arXiv HTML)](https://arxiv.org/html/2408.02232v3)\n- [SpecRover on arXiv](https://arxiv.org/abs/2408.02232)\n- [SoRFT on ACL Anthology](https://aclanthology.org/2025.acl-long.559/)"
      }
    ],
    "totalDurationMs": 30205,
    "totalTokens": 23615,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1067,
      "cache_read_input_tokens": 21845,
      "output_tokens": 696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1067
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 696,
          "cache_read_input_tokens": 21845,
          "cache_creation_input_tokens": 1067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1067,
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
  "sourceToolAssistantUUID": "34b7980f-3708-457c-880f-0abfeb1fe42e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
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
  "leafUuid": "14b133c0-9236-47d7-ade1-7f75dcbb9775",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify spec extraction for code repair methods",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a"
}
```

---

### Tool result

_source line 18 · 2026-05-10T06:58:32.041Z_

<details><summary>↩ Tool result · `toolu_01Q61n9LQb2NxVn9dtKtzexw`</summary>

```text
Perfect! I now have comprehensive information to verify all the claims. Let me compile my findings:

---

## Verification Report: AI Model and Benchmark Claims

### 1. **Qwen3-Coder-30B-A3B Model Specifications**

**Status: VERIFIED - Claims are accurate**

The model exists and specifications are confirmed:

- **Model Type**: Genuine Mixture-of-Experts (MoE) architecture
- **Total Parameters**: 30.5B (not approximately 30B)
- **Activated Parameters**: 3.3B per token (not exactly 3B as stated, but reasonably close)
- **MoE Architecture**: 128 total experts with 8 active per forward pass
- **Architecture**: 48 transformer layers, 32 attention heads for Q (GQA), 4 for KV
- **Context Length**: 262,144 tokens natively (256K)

**VRAM Requirements - PARTIALLY ACCURATE BUT REQUIRES CONTEXT:**

- **Fine-tuning with QLoRA**: Can fit in 17.5GB VRAM when quantized to 4-bit using QLoRA techniques (confirmed via Unsloth)
- **2× H100 80GB claim**: This is realistic but oversimplified:
  - H100 80GB can easily handle the model for inference or fine-tuning with QLoRA
  - However, you don't actually need 2× H100s for QLoRA fine-tuning (17.5GB fits on one card)
  - 2× H100 would be necessary only for full-precision (BF16) inference/training (~61GB+) or significantly larger batch sizes
  - The claim seems to conflate maximum capability with actual minimum requirements

**Fine-tuning Cost Claim**: Cannot directly verify "comparable to a 3B dense model" without specific cloud provider quotes, but the VRAM efficiency (17.5GB QLoRA) does support efficient fine-tuning costs relative to the 30.5B total parameters.

---

### 2. **Agentless-1.5 SWE-bench Performance**

**Status: VERIFIED - Claim is accurate**

- **Actual SWE-bench Verified score**: 50.8% (exactly as claimed)
- **SWE-bench Lite score**: 40.67% (slightly different from "~40.7%" but effectively the same)
- **Configuration**: Agentless-1.5 integrated with Claude 3.5 Sonnet

**Architecture Claim - VERIFIED:**

Agentless is confirmed to be a **three-stage fixed pipeline**:
1. **Localization**: Hierarchical localization (file → edit location) using IR retrieval + LLM prompting
2. **Repair**: Generation of candidate patches
3. **Validation**: Patch validation

**Open-source status**: YES - Agentless is open-source ([GitHub: OpenAutoCoder/Agentless](https://github.com/OpenAutoCoder/Agentless))

Key distinction: Unlike agent-based systems, Agentless does NOT allow LLMs to autonomously decide future actions. Each stage is treated as a single-turn problem with verifiable rewards.

---

### 3. **SWE-bench Verified Current SOTA (May 2026)**

**Status: PARTIALLY ACCURATE with important caveats**

**Current leaderboard leader**:
- **Claude Mythos Preview**: 93.9% (0.939 score) - CONFIRMED
- **Claude Opus 4.7**: 87.6%
- **Claude Opus 4.5**: 80.9%

**CRITICAL CAVEAT**: The 93.9% score is on a **contaminated benchmark**:
- OpenAI has officially stopped reporting SWE-Bench Verified scores
- OpenAI now recommends **SWE-Bench Pro** instead
- The issue: Top models score 46% on SWE-Bench Pro but 81% on Verified due to data contamination
- SWE-Bench Verified is no longer considered reliable for evaluating true software engineering capabilities

**Claude Mythos Preview context**:
- Released April 7, 2026 (unreleased, restricted access)
- Part of Project Glasswing (restricted to 12 major tech/finance companies for defensive cybersecurity only)
- Not available for general use
- Reportedly achieves unprecedented coding capabilities (93.9% represents a ~2-3x jump from 2024 models at 40-55%)

---

## Summary of Claim Accuracy

1. **Qwen3-Coder-30B-A3B specs**: 85-90% accurate (minor oversimplification on 2× H100 requirement; 3.3B ≠ 3B exactly but close)
2. **Agentless-1.5 @ 50.8%**: 100% accurate
3. **Claude Mythos Preview @ 93.9%**: Technically accurate but misleading without context about benchmark contamination and restricted access

The most significant red flag is presenting the Claude Mythos 93.9% figure without mentioning that SWE-Bench Verified is contaminated and OpenAI no longer endorses it as a reliable benchmark. The 46% SWE-Bench Pro score is the more defensible claim.

Sources:
- [Qwen/Qwen3-Coder-30B-A3B-Instruct · Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
- [Qwen3 - How to Run & Fine-tune | Unsloth Documentation](https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune)
- [Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489)
- [GitHub - OpenAutoCoder/Agentless](https://github.com/OpenAutoCoder/Agentless)
- [SWE-bench Leaderboards](https://www.swebench.com/)
- [Claude Mythos Preview Benchmarks, Pricing & Context Window](https://llm-stats.com/models/claude-mythos-preview)
- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%](https://www.morphllm.com/swe-bench-pro)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57945dff-d571-41e6-9514-714cc011cc7f",
  "isSidechain": false,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "type": "user",
  "uuid": "e8c05e62-53c2-4c87-b21f-e818e64ba4c2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify details about two AI models/systems for an adversarial review:\n\n1. **Qwen3-Coder-30B-A3B**: The proposal claims this is a Mixture-of-Experts model with 30B total parameters, ~3B active per token, fits on 2× H100 80GB with QLoRA, and fine-tuning cost is comparable to a 3B dense model.\n   - Search: site:huggingface.co Qwen3-Coder-30B-A3B\n   - Search: \"Qwen3-Coder\" 30B MoE active parameters specifications\n   - Does this model exist? What are its actual specs (VRAM requirements, parameter counts)?\n   - Is \"2× H100 80GB with QLoRA\" realistic for fine-tuning a 30B MoE?\n\n2. **Agentless-1.5** (arXiv 2407.01489): The proposal claims \"~50.8% SWE-bench Verified (Agentless-1.5)\"\n   - Search: Agentless-1.5 SWE-bench Verified performance 2025\n   - Search: site:arxiv.org Agentless SWE-bench 2407.01489\n   - What is Agentless-1.5's actual SWE-bench Verified score?\n   - Is Agentless an open-source three-stage fixed pipeline as claimed?\n\n3. **SWE-bench Verified current SOTA** (as of May 2026):\n   - Search: site:paperswithcode.com SWE-bench Verified leaderboard\n   - Search: SWE-bench Verified SOTA 2026 May results\n   - What is the actual current SOTA on SWE-bench Verified? The proposal mentions \"Claude Mythos Preview\" at 93.9% somewhere.\n\nReport actual numbers and whether the model/system claims are accurate.",
    "agentId": "a84d08e135aaf0f67",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I now have comprehensive information to verify all the claims. Let me compile my findings:\n\n---\n\n## Verification Report: AI Model and Benchmark Claims\n\n### 1. **Qwen3-Coder-30B-A3B Model Specifications**\n\n**Status: VERIFIED - Claims are accurate**\n\nThe model exists and specifications are confirmed:\n\n- **Model Type**: Genuine Mixture-of-Experts (MoE) architecture\n- **Total Parameters**: 30.5B (not approximately 30B)\n- **Activated Parameters**: 3.3B per token (not exactly 3B as stated, but reasonably close)\n- **MoE Architecture**: 128 total experts with 8 active per forward pass\n- **Architecture**: 48 transformer layers, 32 attention heads for Q (GQA), 4 for KV\n- **Context Length**: 262,144 tokens natively (256K)\n\n**VRAM Requirements - PARTIALLY ACCURATE BUT REQUIRES CONTEXT:**\n\n- **Fine-tuning with QLoRA**: Can fit in 17.5GB VRAM when quantized to 4-bit using QLoRA techniques (confirmed via Unsloth)\n- **2× H100 80GB claim**: This is realistic but oversimplified:\n  - H100 80GB can easily handle the model for inference or fine-tuning with QLoRA\n  - However, you don't actually need 2× H100s for QLoRA fine-tuning (17.5GB fits on one card)\n  - 2× H100 would be necessary only for full-precision (BF16) inference/training (~61GB+) or significantly larger batch sizes\n  - The claim seems to conflate maximum capability with actual minimum requirements\n\n**Fine-tuning Cost Claim**: Cannot directly verify \"comparable to a 3B dense model\" without specific cloud provider quotes, but the VRAM efficiency (17.5GB QLoRA) does support efficient fine-tuning costs relative to the 30.5B total parameters.\n\n---\n\n### 2. **Agentless-1.5 SWE-bench Performance**\n\n**Status: VERIFIED - Claim is accurate**\n\n- **Actual SWE-bench Verified score**: 50.8% (exactly as claimed)\n- **SWE-bench Lite score**: 40.67% (slightly different from \"~40.7%\" but effectively the same)\n- **Configuration**: Agentless-1.5 integrated with Claude 3.5 Sonnet\n\n**Architecture Claim - VERIFIED:**\n\nAgentless is confirmed to be a **three-stage fixed pipeline**:\n1. **Localization**: Hierarchical localization (file → edit location) using IR retrieval + LLM prompting\n2. **Repair**: Generation of candidate patches\n3. **Validation**: Patch validation\n\n**Open-source status**: YES - Agentless is open-source ([GitHub: OpenAutoCoder/Agentless](https://github.com/OpenAutoCoder/Agentless))\n\nKey distinction: Unlike agent-based systems, Agentless does NOT allow LLMs to autonomously decide future actions. Each stage is treated as a single-turn problem with verifiable rewards.\n\n---\n\n### 3. **SWE-bench Verified Current SOTA (May 2026)**\n\n**Status: PARTIALLY ACCURATE with important caveats**\n\n**Current leaderboard leader**:\n- **Claude Mythos Preview**: 93.9% (0.939 score) - CONFIRMED\n- **Claude Opus 4.7**: 87.6%\n- **Claude Opus 4.5**: 80.9%\n\n**CRITICAL CAVEAT**: The 93.9% score is on a **contaminated benchmark**:\n- OpenAI has officially stopped reporting SWE-Bench Verified scores\n- OpenAI now recommends **SWE-Bench Pro** instead\n- The issue: Top models score 46% on SWE-Bench Pro but 81% on Verified due to data contamination\n- SWE-Bench Verified is no longer considered reliable for evaluating true software engineering capabilities\n\n**Claude Mythos Preview context**:\n- Released April 7, 2026 (unreleased, restricted access)\n- Part of Project Glasswing (restricted to 12 major tech/finance companies for defensive cybersecurity only)\n- Not available for general use\n- Reportedly achieves unprecedented coding capabilities (93.9% represents a ~2-3x jump from 2024 models at 40-55%)\n\n---\n\n## Summary of Claim Accuracy\n\n1. **Qwen3-Coder-30B-A3B specs**: 85-90% accurate (minor oversimplification on 2× H100 requirement; 3.3B ≠ 3B exactly but close)\n2. **Agentless-1.5 @ 50.8%**: 100% accurate\n3. **Claude Mythos Preview @ 93.9%**: Technically accurate but misleading without context about benchmark contamination and restricted access\n\nThe most significant red flag is presenting the Claude Mythos 93.9% figure without mentioning that SWE-Bench Verified is contaminated and OpenAI no longer endorses it as a reliable benchmark. The 46% SWE-Bench Pro score is the more defensible claim.\n\nSources:\n- [Qwen/Qwen3-Coder-30B-A3B-Instruct · Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)\n- [Qwen3 - How to Run & Fine-tune | Unsloth Documentation](https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune)\n- [Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489)\n- [GitHub - OpenAutoCoder/Agentless](https://github.com/OpenAutoCoder/Agentless)\n- [SWE-bench Leaderboards](https://www.swebench.com/)\n- [Claude Mythos Preview Benchmarks, Pricing & Context Window](https://llm-stats.com/models/claude-mythos-preview)\n- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%](https://www.morphllm.com/swe-bench-pro)"
      }
    ],
    "totalDurationMs": 55964,
    "totalTokens": 30123,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 785,
      "cache_creation_input_tokens": 1509,
      "cache_read_input_tokens": 26282,
      "output_tokens": 1547,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1509
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 785,
          "output_tokens": 1547,
          "cache_read_input_tokens": 26282,
          "cache_creation_input_tokens": 1509,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1509,
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
  "sourceToolAssistantUUID": "57945dff-d571-41e6-9514-714cc011cc7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-10T06:59:12.088Z_

<details><summary>↩ Tool result · `toolu_01G1BUHczLWPipAJGzLhDsZ8`</summary>

```text
Perfect. Now let me compile a comprehensive report of all the relevant competing work I've found for the SpecExtract paper. This is substantial, so let me organize it by research category and direct overlap.

## Adversarial Literature Review for SpecExtract

Based on my systematic search of recent literature (2025-2026), I've identified significant competing and overlapping work across multiple research dimensions. Here are the key findings organized by research theme:

---

## **DIRECTLY OVERLAPPING WORK: Specification Generation and Extraction from Bug Reports**

### 1. **CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (2026)**
- **URL:** https://arxiv.org/html/2604.12268v1
- **Direct Overlap:** This work explicitly benchmarks specification generation (preconditions, postconditions) from code and requirements. The paper finds that specification generation is substantially more challenging than code generation (20.2% pass rate on repository-level SWE-bench Verified tasks).
- **Key Difference:** Focuses on generating specifications FROM code/requirements rather than FROM bug reports specifically, but uses same SWE-bench Verified training data.

### 2. **Specification Vibing for Automated Program Repair (February 2026)**
- **URL:** https://arxiv.org/html/2602.08263
- **Direct Overlap:** VibeRepair transforms buggy code and failing test cases into "test-based flawed behavior specification" through iterative interaction with validation feedback. This is almost directly parallel to SpecExtract's core idea of extracting behavioral specifications from test failures.
- **Key Difference:** VibeRepair focuses on iterative refinement through feedback loops rather than upfront extraction training.

### 3. **Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design (2026)**
- **URL:** https://arxiv.org/html/2601.03878v1
- **Direct Overlap:** This registered report studies LLM-driven specification engineering with the CURRANTE workflow (Specification → Tests → Function pipeline). The work demonstrates the importance of explicit specification stages in code generation.
- **Key Difference:** Studies human-in-the-loop specification engineering rather than automatic extraction from bug reports.

---

## **HIGH-OVERLAP WORK: Test-Based Specification and Behavioral Constraint Extraction**

### 4. **Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints (April 2026)**
- **URL:** https://arxiv.org/html/2604.04580
- **High Overlap:** Agent-CoEvo models tests as dynamic behavioral constraints that guide repair. The paper explicitly recognizes that "enabling repair agents to revise behavioral constraints during search is critical," directly overlapping with SpecExtract's use of test assertions to guide repair.
- **Critical Claim:** Proposes that behavioral constraints should be coevolved with patches rather than fixed, which is a competing design choice to SpecExtract's pre-trained spec extraction approach.

### 5. **Can We Enhance Bug Report Quality Using LLMs?: An Empirical Study of LLM-Based Bug Report Generation (April 2025)**
- **URL:** https://arxiv.org/abs/2504.18804
- **High Overlap:** Investigates instruction fine-tuning for automated structured bug report generation. Shows LLMs can enhance bug report quality by filling missing details and semantic analysis of descriptions.
- **Key Difference:** Focuses on improving bug report quality itself rather than extracting specifications from existing reports.

### 6. **BugMentor: Generating Answers to Follow-up Questions from Software Bug Reports using Structured Information Retrieval and Neural Text Generation (2023-2025)**
- **URL:** https://arxiv.org/abs/2304.12494
- **High Overlap:** Extracts and reasons over structured information from bug reports using neural methods.

---

## **COMPETING APPROACHES: Specification-Driven Repair Pipelines**

### 7. **Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation (SpecFix, 2025)**
- **URL:** https://arxiv.org/html/2505.07270
- **Competing Approach:** SpecFix analyzes behavioral divergence among generated solutions and produces patches to repair ambiguous problem descriptions. Modified 43.58% of descriptions, improving performance by 4.09% overall—this is a different approach to handling specification quality.
- **Key Insight:** Shows that specification quality/ambiguity directly affects code generation success (30.9% improvement when specs are fixed).

### 8. **Knowledge-Enhanced Program Repair for Data Science Code (February 2025)**
- **URL:** https://arxiv.org/html/2502.09771v1
- **Competing Approach:** Organizes problem description, incorrect code, stderr, and API knowledge into a structured prompt. This is a prompting-based approach to leverage specification information rather than learning to extract it.

### 9. **Repeton: Structured Bug Repair with ReAct-Guided Patch-and-Test Cycles (June 2025)**
- **URL:** https://arxiv.org/html/2506.08173
- **Competing Approach:** Uses structured patch-and-test cycles guided by lightweight heuristics rather than learned specifications. Tests are treated as dynamic constraints in the repair loop.

---

## **RELATED WORK: Agentic Bug Reproduction and Information Extraction**

### 10. **Agentic Bug Reproduction for Effective Automated Program Repair at Google (March 2025)**
- **URL:** https://arxiv.org/html/2502.01821v2
- **Related:** Describes automated extraction and curation of bug reproduction information from Google projects (7 languages). Shows how structured bug information improves repair.

### 11. **LLPut: Investigating Large Language Models for Bug Report-Based Input Generation (2025)**
- **URL:** https://arxiv.org/abs/2503.20578
- **Related:** Specifically investigates extracting failure-inducing inputs from bug reports using generative LLMs. Tests Qwen, LLaMA, and other models on this extraction task.

### 12. **ChatBR: Automated assessment and improvement of bug reports (2024-2025)**
- **URL:** https://dl.acm.org/doi/pdf/10.1145/3691620.3695518
- **Related:** Uses pre-trained models with attention mechanisms to assess and improve bug report quality by detecting missing fields.

### 13. **Uncovering the iceberg from the tip: Generating API Specifications for Bug (2025)**
- **URL:** https://www.ndss-symposium.org/wp-content/uploads/2025-2001-paper.pdf
- **Related:** Extracts API specifications from bug reports, specifically targeting interface-level specifications.

---

## **METHODOLOGICALLY RELEVANT: SWE-bench Training and Structured Data Approaches**

### 14. **SWE-bench Verified and SWE-Bench Pro (2025-2026)**
- **URLs:** 
  - https://arxiv.org/html/2602.04449 (What's in a Benchmark?)
  - https://openai.com/index/introducing-swe-bench-verified/
- **Relevance:** SWE-bench Pro explicitly adds structured interface specifications and behavioral requirements to reduce false negatives from naming mismatches. This is the same benchmark/training data SpecExtract uses, but with additional structured annotations.

### 15. **SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale (2025)**
- **URL:** https://arxiv.org/html/2602.23866
- **Relevance:** Automates task collection at scale and includes structured specification annotations (interface specs, behavioral requirements).

### 16. **SWE-bench Goes Live! (April 2025)**
- **URL:** https://arxiv.org/html/2505.23419v2
- **Relevance:** SWE-bench-Live provides 1,319 continuously updated benchmark instances with explicit behavioral test validation. This competing data source might have better specification annotations.

### 17. **SWE-AGI: Benchmarking Specification-Driven Software (February 2026)**
- **URL:** https://www.arxiv.org/pdf/2602.09447
- **Critical Relevance:** Each task provides explicit normative specifications (specs/), task statements (TASK.md), and test subsets. This is a direct competitor providing better structured specification annotations than raw SWE-bench.

### 18. **SWE-Bench 5G: Benchmarking AI Coding Agents on Telecom Network Engineering Tasks (2026)**
- **URL:** https://arxiv.org/html/2604.26278
- **Relevance:** Domain-specific variant showing SWE-bench can be extended with specialized specifications.

---

## **FAULT LOCALIZATION WITH SPECIFICATIONS**

### 19. **Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (2026 ICST)**
- **URL:** https://arxiv.org/html/2504.04372
- **Competing Use of Specs:** Shows that LLMs require explicit, formally stated specifications (assertion statements) to perform effective fault localization, filtering out underspecified programs. This validates SpecExtract's premise about spec importance but offers a competing approach (specs as explicit assertions in localization).

### 20. **Coverage Isn't Enough: SBFL-Driven Insights into Manually Written Tests (2025)**
- **URL:** https://arxiv.org/pdf/2512.11223
- **Related:** Investigates spectrum-based fault localization (SBFL) guided by test suite quality, showing test quality directly impacts localization effectiveness.

---

## **NEURAL PROGRAM REPAIR SURVEYS AND FRAMEWORKS**

### 21. **A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (June 2025)**
- **URL:** https://arxiv.org/html/2506.23749v1
- **Comprehensive Baseline:** Surveys 63 recent APR systems (Jan 2022 - June 2025), covering retrieval-augmented and analysis-augmented approaches. SpecExtract should position itself relative to this taxonomy (likely under "specification-augmented" repair).

### 22. **Neural Program Repair: Systems, Challenges and Solutions (2022, updated context 2025)**
- **URL:** https://arxiv.org/abs/2202.10868
- **Foundational Context:** Foundational survey on neural program repair approaches.

### 23. **A Taxonomy of Prompt Defects in LLM Systems (2025)**
- **URL:** https://arxiv.org/html/2509.14404v1
- **Relevant:** Distills prompt engineering patterns and evaluation frameworks relevant to how specifications are communicated in repair prompts.

---

## **PATCH GENERATION AND VALIDATION STRATEGIES**

### 24. **PAFT: Preservation-Aware Fine-Tuning for Minimal-Edit Program Repair (April 2026)**
- **URL:** https://arxiv.org/html/2604.03113v2
- **Competing Concern:** Notes 41.5% of LLM-generated patches require manual revision. Specification quality likely affects this overfitting problem.

### 25. **ComPass: Contrastive Learning for Automated Patch Correctness Assessment (February 2026)**
- **URL:** https://arxiv.org/html/2602.07561
- **Related:** Addresses patch overfitting due to weak test suites. Specifications could help validate patches beyond test suite passing.

### 26. **Are Benchmark Tests Strong Enough? Mutation-Guided Diagnosis and Augmentation of Regression Suites (April 2026)**
- **URL:** https://arxiv.org/html/2604.01518v1
- **Related:** STING framework uses semantic program variants to uncover test suite weaknesses. Specifications could validate behavioral correctness beyond weak test suites.

### 27. **REFINE: Enhancing Program Repair Agents through Context-Aware Patch Refinement (2025)**
- **URL:** https://arxiv.org/pdf/2510.03588
- **Related:** Context-aware refinement of patches validated against test suites.

### 28. **Root-Cause-Driven Automated Vulnerability Repair (Recent 2026)**
- **URL:** https://arxiv.org/html/2605.04251
- **Related:** Combines agentic fault localization with root-cause analysis to guide patch synthesis.

---

## **SPECIFICATION MINING AND VERIFICATION (Classical APR Context)**

### 29. **Mining Specifications for Predictive Safety Monitoring (CPS-IoT Week 2025)**
- **URL:** https://dl.acm.org/doi/10.1145/3716550.3722021
- **Historical Context:** Classical specification mining for safety properties using Signal Temporal Logic (STL). Shows specification extraction is a long-studied problem in formal methods.

---

## **TEST GENERATION AND BEHAVIORAL VALIDATION**

### 30. **Multi-Step Generation of Test Specifications using Large Language Models (2025 ACL Industry)**
- **URL:** https://aclanthology.org/2025.acl-industry.11.pdf
- **Related:** Generates test specifications using iterative refinement with LLMs.

### 31. **Large Language Models for Unit Test Generation: Achievements, Challenges, and the Road Ahead (2025)**
- **URL:** https://arxiv.org/html/2511.21382v1
- **Context:** Comprehensive study on LLM-based test generation. Shows iterative refinement approaches increase valid test generation from 24% to 70%+.

### 32. **Validating Formal Specifications with LLM-generated Test Cases (October 2025)**
- **URL:** https://arxiv.org/html/2510.23350v1
- **Reciprocal Work:** Uses LLMs to generate test cases that validate formal specifications (reverse direction from SpecExtract, but related).

### 33. **Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection (January 2026)**
- **URL:** https://arxiv.org/html/2508.06365
- **Related:** Agentless approach automatically generates reproduction tests from SWE issue descriptions and selects best patches via voting.

---

## **DELTA/DIFFERENCE LEARNING APPROACHES**

### 34. **The Delta Learning Hypothesis: Preference Tuning on Weak Data can Yield Strong Gains (2025)**
- **URL:** https://arxiv.org/html/2507.06187v1
- **Methodological Relevance:** Shows pairing responses with weaker responses (creating a delta) drives learning. SpecExtract's behavioral delta (observed vs. expected) is conceptually similar.

### 35. **Learning Program Behavioral Models from Synthesized Input-Output Pairs (2024-2025)**
- **URL:** https://arxiv.org/pdf/2407.08597
- **Related:** Learns behavioral models from I/O pairs, conceptually related to specification extraction.

---

## **ADVERSARIAL ISSUES: Claims to Address**

The authors should specifically discuss:

1. **Why train a separate spec extractor vs. end-to-end repair?** (SpecFix, VibeRepair, Repeton use different strategies)
2. **Why pre-train specs vs. coevolve them?** (Agent-CoEvo argues dynamic constraint revision is critical)
3. **Why SWE-bench test assertions as training signal vs. SWE-AGI's explicit specifications?** (SWE-AGI provides gold-standard specs, making comparison necessary)
4. **How does this compare to prompting-based approaches?** (Knowledge-Enhanced Repair shows prompting can work without explicit extraction)
5. **Patch overfitting risk:** PAFT (2026) shows 41.5% of patches still need manual revision despite test passage—do specifications help here?

---

## **SUMMARY: Key Competitive Gaps**

**Most Direct Competitors:**
- CodeSpecBench (2026) - Specification generation benchmark using same SWE-bench data
- VibeRepair (2026) - Specification refinement through test-based feedback loops
- Agent-CoEvo (2026) - Dynamic behavioral constraint coevolution during repair
- SWE-AGI (2026) - Explicit, gold-standard specification annotations on SWE-bench tasks

**Methodological Alternatives:**
- SpecFix - Specification repair via execution feedback
- Knowledge-Enhanced Repair - Prompting-based specification leverage
- SWE-Bench Pro/V2 - Structured specification annotations at benchmark level

**Critical for Positioning:** The SWE-AGI benchmark and CodeSpecBench were published in 2026 (recent/concurrent with likely SpecExtract timeline). These represent significant competing and complementary work that should be prominently addressed.

---

## **Sources:**

- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/html/2604.12268v1)
- [Specification Vibing for Automated Program Repair](https://arxiv.org/html/2602.08263)
- [Understanding Specification-Driven Code Generation with LLMs](https://arxiv.org/html/2601.03878v1)
- [Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints](https://arxiv.org/html/2604.04580)
- [Can We Enhance Bug Report Quality Using LLMs?](https://arxiv.org/abs/2504.18804)
- [Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation](https://arxiv.org/html/2505.07270)
- [Knowledge-Enhanced Program Repair for Data Science Code](https://arxiv.org/html/2502.09771v1)
- [Repeton: Structured Bug Repair with ReAct-Guided Patch-and-Test Cycles](https://arxiv.org/html/2506.08173)
- [Agentic Bug Reproduction for Effective Automated Program Repair at Google](https://arxiv.org/html/2502.01821v2)
- [LLPut: Investigating Large Language Models for Bug Report-Based Input Generation](https://arxiv.org/abs/2503.20578)
- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%](https://www.morphllm.com/swe-bench-pro)
- [SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale](https://arxiv.org/html/2602.23866)
- [SWE-bench Goes Live!](https://arxiv.org/html/2505.23419v2)
- [SWE-AGI: Benchmarking Specification-Driven Software](https://www.arxiv.org/pdf/2602.09447)
- [Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models](https://arxiv.org/html/2504.04372)
- [A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications](https://arxiv.org/html/2506.23749v1)
- [A Taxonomy of Prompt Defects in LLM Systems](https://arxiv.org/html/2509.14404v1)
- [PAFT: Preservation-Aware Fine-Tuning for Minimal-Edit Program Repair](https://arxiv.org/html/2604.03113v2)
- [ComPass: Contrastive Learning for Automated Patch Correctness Assessment](https://arxiv.org/html/2602.07561)
- [Are Benchmark Tests Strong Enough? Mutation-Guided Diagnosis and Augmentation of Regression Suites](https://arxiv.org/html/2604.01518v1)
- [REFINE: Enhancing Program Repair Agents through Context-Aware Patch Refinement](https://arxiv.org/pdf/2510.03588)
- [Root-Cause-Driven Automated Vulnerability Repair](https://arxiv.org/html/2605.04251)
- [Mining Specifications for Predictive Safety Monitoring](https://dl.acm.org/doi/10.1145/3716550.3722021)
- [Multi-Step Generation of Test Specifications using Large Language Models](https://aclanthology.org/2025.acl-industry.11.pdf)
- [Large Language Models for Unit Test Generation: Achievements, Challenges, and the Road Ahead](https://arxiv.org/html/2511.21382v1)
- [Validating Formal Specifications with LLM-generated Test Cases](https://arxiv.org/html/2510.23350v1)
- [Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection](https://arxiv.org/html/2508.06365)
- [The Delta Learning Hypothesis: Preference Tuning on Weak Data can Yield Strong Gains](https://arxiv.org/html/2507.06187v1)
- [Learning Program Behavioral Models from Synthesized Input-Output Pairs](https://arxiv.org/pdf/2407.08597)
- [iFixR: Bug Report driven Program Repair](https://cs.paperswithcode.com/paper/ifixr-bug-report-driven-program-repair)
- [ChatBR: Automated assessment and improvement of bug reports](https://dl.acm.org/doi/pdf/10.1145/3691620.3695518)
- [Uncovering the iceberg from the tip: Generating API Specifications for Bug](https://www.ndss-symposium.org/wp-content/uploads/2025-2001-paper.pdf)
- [What's in a Benchmark? The Case of SWE-Bench in Automated Program Repair](https://arxiv.org/pdf/2602.04449)
- [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49f63263-d3ad-4cec-aaf7-05b11e4fa171",
  "isSidechain": false,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "type": "user",
  "uuid": "7373a06a-319e-43a6-92e2-03ce6dd40732",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm doing an adversarial literature review for a paper called \"SpecExtract\" which proposes: training a model to extract structured behavioral specifications from bug report text (stack traces, error messages, test assertions) to guide automated program repair. The model extracts: affected interface, observed behavior, expected behavior, and behavioral delta. It's trained on SWE-bench test patch assertions.\n\nPlease search for concurrent or competing work that the authors might have missed:\n\n1. **Bug report information extraction / specification extraction**:\n   - Search: \"bug report\" \"specification extraction\" NLP 2025 2026\n   - Search: site:arxiv.org structured information extraction bug reports program repair 2025\n\n2. **Issue-to-spec methods for code repair**:\n   - Search: site:arxiv.org \"issue description\" specification \"program repair\" 2025 2026\n   - Search: \"behavioral specification\" \"bug report\" automatic extraction 2026\n\n3. **Test assertion-based specification mining**:\n   - Search: \"test assertions\" specification mining program repair 2025 2026\n   - Search: site:arxiv.org test patch specification behavioral constraints repair\n\n4. **SWE-bench training data approaches**:\n   - Search: site:arxiv.org SWE-bench training data specification structured 2025 2026\n   - Search: SWE-bench fine-tuning specifications behavioral extraction 2026\n\n5. **Information extraction for debugging/repair**:\n   - Search: site:arxiv.org \"stack trace\" NLP information extraction repair 2025\n   - Search: site:paperswithcode.com bug report structured extraction program repair\n\nReport any papers that directly overlap with SpecExtract's approach of (a) extracting structured specs from bug report text, (b) using test assertions as training signal for spec learning, or (c) injecting specs into fault localization or patch generation pipelines.",
    "agentId": "a3d6359a710b9a6ec",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect. Now let me compile a comprehensive report of all the relevant competing work I've found for the SpecExtract paper. This is substantial, so let me organize it by research category and direct overlap.\n\n## Adversarial Literature Review for SpecExtract\n\nBased on my systematic search of recent literature (2025-2026), I've identified significant competing and overlapping work across multiple research dimensions. Here are the key findings organized by research theme:\n\n---\n\n## **DIRECTLY OVERLAPPING WORK: Specification Generation and Extraction from Bug Reports**\n\n### 1. **CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (2026)**\n- **URL:** https://arxiv.org/html/2604.12268v1\n- **Direct Overlap:** This work explicitly benchmarks specification generation (preconditions, postconditions) from code and requirements. The paper finds that specification generation is substantially more challenging than code generation (20.2% pass rate on repository-level SWE-bench Verified tasks).\n- **Key Difference:** Focuses on generating specifications FROM code/requirements rather than FROM bug reports specifically, but uses same SWE-bench Verified training data.\n\n### 2. **Specification Vibing for Automated Program Repair (February 2026)**\n- **URL:** https://arxiv.org/html/2602.08263\n- **Direct Overlap:** VibeRepair transforms buggy code and failing test cases into \"test-based flawed behavior specification\" through iterative interaction with validation feedback. This is almost directly parallel to SpecExtract's core idea of extracting behavioral specifications from test failures.\n- **Key Difference:** VibeRepair focuses on iterative refinement through feedback loops rather than upfront extraction training.\n\n### 3. **Understanding Specification-Driven Code Generation with LLMs: An Empirical Study Design (2026)**\n- **URL:** https://arxiv.org/html/2601.03878v1\n- **Direct Overlap:** This registered report studies LLM-driven specification engineering with the CURRANTE workflow (Specification → Tests → Function pipeline). The work demonstrates the importance of explicit specification stages in code generation.\n- **Key Difference:** Studies human-in-the-loop specification engineering rather than automatic extraction from bug reports.\n\n---\n\n## **HIGH-OVERLAP WORK: Test-Based Specification and Behavioral Constraint Extraction**\n\n### 4. **Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints (April 2026)**\n- **URL:** https://arxiv.org/html/2604.04580\n- **High Overlap:** Agent-CoEvo models tests as dynamic behavioral constraints that guide repair. The paper explicitly recognizes that \"enabling repair agents to revise behavioral constraints during search is critical,\" directly overlapping with SpecExtract's use of test assertions to guide repair.\n- **Critical Claim:** Proposes that behavioral constraints should be coevolved with patches rather than fixed, which is a competing design choice to SpecExtract's pre-trained spec extraction approach.\n\n### 5. **Can We Enhance Bug Report Quality Using LLMs?: An Empirical Study of LLM-Based Bug Report Generation (April 2025)**\n- **URL:** https://arxiv.org/abs/2504.18804\n- **High Overlap:** Investigates instruction fine-tuning for automated structured bug report generation. Shows LLMs can enhance bug report quality by filling missing details and semantic analysis of descriptions.\n- **Key Difference:** Focuses on improving bug report quality itself rather than extracting specifications from existing reports.\n\n### 6. **BugMentor: Generating Answers to Follow-up Questions from Software Bug Reports using Structured Information Retrieval and Neural Text Generation (2023-2025)**\n- **URL:** https://arxiv.org/abs/2304.12494\n- **High Overlap:** Extracts and reasons over structured information from bug reports using neural methods.\n\n---\n\n## **COMPETING APPROACHES: Specification-Driven Repair Pipelines**\n\n### 7. **Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation (SpecFix, 2025)**\n- **URL:** https://arxiv.org/html/2505.07270\n- **Competing Approach:** SpecFix analyzes behavioral divergence among generated solutions and produces patches to repair ambiguous problem descriptions. Modified 43.58% of descriptions, improving performance by 4.09% overall—this is a different approach to handling specification quality.\n- **Key Insight:** Shows that specification quality/ambiguity directly affects code generation success (30.9% improvement when specs are fixed).\n\n### 8. **Knowledge-Enhanced Program Repair for Data Science Code (February 2025)**\n- **URL:** https://arxiv.org/html/2502.09771v1\n- **Competing Approach:** Organizes problem description, incorrect code, stderr, and API knowledge into a structured prompt. This is a prompting-based approach to leverage specification information rather than learning to extract it.\n\n### 9. **Repeton: Structured Bug Repair with ReAct-Guided Patch-and-Test Cycles (June 2025)**\n- **URL:** https://arxiv.org/html/2506.08173\n- **Competing Approach:** Uses structured patch-and-test cycles guided by lightweight heuristics rather than learned specifications. Tests are treated as dynamic constraints in the repair loop.\n\n---\n\n## **RELATED WORK: Agentic Bug Reproduction and Information Extraction**\n\n### 10. **Agentic Bug Reproduction for Effective Automated Program Repair at Google (March 2025)**\n- **URL:** https://arxiv.org/html/2502.01821v2\n- **Related:** Describes automated extraction and curation of bug reproduction information from Google projects (7 languages). Shows how structured bug information improves repair.\n\n### 11. **LLPut: Investigating Large Language Models for Bug Report-Based Input Generation (2025)**\n- **URL:** https://arxiv.org/abs/2503.20578\n- **Related:** Specifically investigates extracting failure-inducing inputs from bug reports using generative LLMs. Tests Qwen, LLaMA, and other models on this extraction task.\n\n### 12. **ChatBR: Automated assessment and improvement of bug reports (2024-2025)**\n- **URL:** https://dl.acm.org/doi/pdf/10.1145/3691620.3695518\n- **Related:** Uses pre-trained models with attention mechanisms to assess and improve bug report quality by detecting missing fields.\n\n### 13. **Uncovering the iceberg from the tip: Generating API Specifications for Bug (2025)**\n- **URL:** https://www.ndss-symposium.org/wp-content/uploads/2025-2001-paper.pdf\n- **Related:** Extracts API specifications from bug reports, specifically targeting interface-level specifications.\n\n---\n\n## **METHODOLOGICALLY RELEVANT: SWE-bench Training and Structured Data Approaches**\n\n### 14. **SWE-bench Verified and SWE-Bench Pro (2025-2026)**\n- **URLs:** \n  - https://arxiv.org/html/2602.04449 (What's in a Benchmark?)\n  - https://openai.com/index/introducing-swe-bench-verified/\n- **Relevance:** SWE-bench Pro explicitly adds structured interface specifications and behavioral requirements to reduce false negatives from naming mismatches. This is the same benchmark/training data SpecExtract uses, but with additional structured annotations.\n\n### 15. **SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale (2025)**\n- **URL:** https://arxiv.org/html/2602.23866\n- **Relevance:** Automates task collection at scale and includes structured specification annotations (interface specs, behavioral requirements).\n\n### 16. **SWE-bench Goes Live! (April 2025)**\n- **URL:** https://arxiv.org/html/2505.23419v2\n- **Relevance:** SWE-bench-Live provides 1,319 continuously updated benchmark instances with explicit behavioral test validation. This competing data source might have better specification annotations.\n\n### 17. **SWE-AGI: Benchmarking Specification-Driven Software (February 2026)**\n- **URL:** https://www.arxiv.org/pdf/2602.09447\n- **Critical Relevance:** Each task provides explicit normative specifications (specs/), task statements (TASK.md), and test subsets. This is a direct competitor providing better structured specification annotations than raw SWE-bench.\n\n### 18. **SWE-Bench 5G: Benchmarking AI Coding Agents on Telecom Network Engineering Tasks (2026)**\n- **URL:** https://arxiv.org/html/2604.26278\n- **Relevance:** Domain-specific variant showing SWE-bench can be extended with specialized specifications.\n\n---\n\n## **FAULT LOCALIZATION WITH SPECIFICATIONS**\n\n### 19. **Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (2026 ICST)**\n- **URL:** https://arxiv.org/html/2504.04372\n- **Competing Use of Specs:** Shows that LLMs require explicit, formally stated specifications (assertion statements) to perform effective fault localization, filtering out underspecified programs. This validates SpecExtract's premise about spec importance but offers a competing approach (specs as explicit assertions in localization).\n\n### 20. **Coverage Isn't Enough: SBFL-Driven Insights into Manually Written Tests (2025)**\n- **URL:** https://arxiv.org/pdf/2512.11223\n- **Related:** Investigates spectrum-based fault localization (SBFL) guided by test suite quality, showing test quality directly impacts localization effectiveness.\n\n---\n\n## **NEURAL PROGRAM REPAIR SURVEYS AND FRAMEWORKS**\n\n### 21. **A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (June 2025)**\n- **URL:** https://arxiv.org/html/2506.23749v1\n- **Comprehensive Baseline:** Surveys 63 recent APR systems (Jan 2022 - June 2025), covering retrieval-augmented and analysis-augmented approaches. SpecExtract should position itself relative to this taxonomy (likely under \"specification-augmented\" repair).\n\n### 22. **Neural Program Repair: Systems, Challenges and Solutions (2022, updated context 2025)**\n- **URL:** https://arxiv.org/abs/2202.10868\n- **Foundational Context:** Foundational survey on neural program repair approaches.\n\n### 23. **A Taxonomy of Prompt Defects in LLM Systems (2025)**\n- **URL:** https://arxiv.org/html/2509.14404v1\n- **Relevant:** Distills prompt engineering patterns and evaluation frameworks relevant to how specifications are communicated in repair prompts.\n\n---\n\n## **PATCH GENERATION AND VALIDATION STRATEGIES**\n\n### 24. **PAFT: Preservation-Aware Fine-Tuning for Minimal-Edit Program Repair (April 2026)**\n- **URL:** https://arxiv.org/html/2604.03113v2\n- **Competing Concern:** Notes 41.5% of LLM-generated patches require manual revision. Specification quality likely affects this overfitting problem.\n\n### 25. **ComPass: Contrastive Learning for Automated Patch Correctness Assessment (February 2026)**\n- **URL:** https://arxiv.org/html/2602.07561\n- **Related:** Addresses patch overfitting due to weak test suites. Specifications could help validate patches beyond test suite passing.\n\n### 26. **Are Benchmark Tests Strong Enough? Mutation-Guided Diagnosis and Augmentation of Regression Suites (April 2026)**\n- **URL:** https://arxiv.org/html/2604.01518v1\n- **Related:** STING framework uses semantic program variants to uncover test suite weaknesses. Specifications could validate behavioral correctness beyond weak test suites.\n\n### 27. **REFINE: Enhancing Program Repair Agents through Context-Aware Patch Refinement (2025)**\n- **URL:** https://arxiv.org/pdf/2510.03588\n- **Related:** Context-aware refinement of patches validated against test suites.\n\n### 28. **Root-Cause-Driven Automated Vulnerability Repair (Recent 2026)**\n- **URL:** https://arxiv.org/html/2605.04251\n- **Related:** Combines agentic fault localization with root-cause analysis to guide patch synthesis.\n\n---\n\n## **SPECIFICATION MINING AND VERIFICATION (Classical APR Context)**\n\n### 29. **Mining Specifications for Predictive Safety Monitoring (CPS-IoT Week 2025)**\n- **URL:** https://dl.acm.org/doi/10.1145/3716550.3722021\n- **Historical Context:** Classical specification mining for safety properties using Signal Temporal Logic (STL). Shows specification extraction is a long-studied problem in formal methods.\n\n---\n\n## **TEST GENERATION AND BEHAVIORAL VALIDATION**\n\n### 30. **Multi-Step Generation of Test Specifications using Large Language Models (2025 ACL Industry)**\n- **URL:** https://aclanthology.org/2025.acl-industry.11.pdf\n- **Related:** Generates test specifications using iterative refinement with LLMs.\n\n### 31. **Large Language Models for Unit Test Generation: Achievements, Challenges, and the Road Ahead (2025)**\n- **URL:** https://arxiv.org/html/2511.21382v1\n- **Context:** Comprehensive study on LLM-based test generation. Shows iterative refinement approaches increase valid test generation from 24% to 70%+.\n\n### 32. **Validating Formal Specifications with LLM-generated Test Cases (October 2025)**\n- **URL:** https://arxiv.org/html/2510.23350v1\n- **Reciprocal Work:** Uses LLMs to generate test cases that validate formal specifications (reverse direction from SpecExtract, but related).\n\n### 33. **Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection (January 2026)**\n- **URL:** https://arxiv.org/html/2508.06365\n- **Related:** Agentless approach automatically generates reproduction tests from SWE issue descriptions and selects best patches via voting.\n\n---\n\n## **DELTA/DIFFERENCE LEARNING APPROACHES**\n\n### 34. **The Delta Learning Hypothesis: Preference Tuning on Weak Data can Yield Strong Gains (2025)**\n- **URL:** https://arxiv.org/html/2507.06187v1\n- **Methodological Relevance:** Shows pairing responses with weaker responses (creating a delta) drives learning. SpecExtract's behavioral delta (observed vs. expected) is conceptually similar.\n\n### 35. **Learning Program Behavioral Models from Synthesized Input-Output Pairs (2024-2025)**\n- **URL:** https://arxiv.org/pdf/2407.08597\n- **Related:** Learns behavioral models from I/O pairs, conceptually related to specification extraction.\n\n---\n\n## **ADVERSARIAL ISSUES: Claims to Address**\n\nThe authors should specifically discuss:\n\n1. **Why train a separate spec extractor vs. end-to-end repair?** (SpecFix, VibeRepair, Repeton use different strategies)\n2. **Why pre-train specs vs. coevolve them?** (Agent-CoEvo argues dynamic constraint revision is critical)\n3. **Why SWE-bench test assertions as training signal vs. SWE-AGI's explicit specifications?** (SWE-AGI provides gold-standard specs, making comparison necessary)\n4. **How does this compare to prompting-based approaches?** (Knowledge-Enhanced Repair shows prompting can work without explicit extraction)\n5. **Patch overfitting risk:** PAFT (2026) shows 41.5% of patches still need manual revision despite test passage—do specifications help here?\n\n---\n\n## **SUMMARY: Key Competitive Gaps**\n\n**Most Direct Competitors:**\n- CodeSpecBench (2026) - Specification generation benchmark using same SWE-bench data\n- VibeRepair (2026) - Specification refinement through test-based feedback loops\n- Agent-CoEvo (2026) - Dynamic behavioral constraint coevolution during repair\n- SWE-AGI (2026) - Explicit, gold-standard specification annotations on SWE-bench tasks\n\n**Methodological Alternatives:**\n- SpecFix - Specification repair via execution feedback\n- Knowledge-Enhanced Repair - Prompting-based specification leverage\n- SWE-Bench Pro/V2 - Structured specification annotations at benchmark level\n\n**Critical for Positioning:** The SWE-AGI benchmark and CodeSpecBench were published in 2026 (recent/concurrent with likely SpecExtract timeline). These represent significant competing and complementary work that should be prominently addressed.\n\n---\n\n## **Sources:**\n\n- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/html/2604.12268v1)\n- [Specification Vibing for Automated Program Repair](https://arxiv.org/html/2602.08263)\n- [Understanding Specification-Driven Code Generation with LLMs](https://arxiv.org/html/2601.03878v1)\n- [Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints](https://arxiv.org/html/2604.04580)\n- [Can We Enhance Bug Report Quality Using LLMs?](https://arxiv.org/abs/2504.18804)\n- [Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation](https://arxiv.org/html/2505.07270)\n- [Knowledge-Enhanced Program Repair for Data Science Code](https://arxiv.org/html/2502.09771v1)\n- [Repeton: Structured Bug Repair with ReAct-Guided Patch-and-Test Cycles](https://arxiv.org/html/2506.08173)\n- [Agentic Bug Reproduction for Effective Automated Program Repair at Google](https://arxiv.org/html/2502.01821v2)\n- [LLPut: Investigating Large Language Models for Bug Report-Based Input Generation](https://arxiv.org/abs/2503.20578)\n- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81%](https://www.morphllm.com/swe-bench-pro)\n- [SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale](https://arxiv.org/html/2602.23866)\n- [SWE-bench Goes Live!](https://arxiv.org/html/2505.23419v2)\n- [SWE-AGI: Benchmarking Specification-Driven Software](https://www.arxiv.org/pdf/2602.09447)\n- [Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models](https://arxiv.org/html/2504.04372)\n- [A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications](https://arxiv.org/html/2506.23749v1)\n- [A Taxonomy of Prompt Defects in LLM Systems](https://arxiv.org/html/2509.14404v1)\n- [PAFT: Preservation-Aware Fine-Tuning for Minimal-Edit Program Repair](https://arxiv.org/html/2604.03113v2)\n- [ComPass: Contrastive Learning for Automated Patch Correctness Assessment](https://arxiv.org/html/2602.07561)\n- [Are Benchmark Tests Strong Enough? Mutation-Guided Diagnosis and Augmentation of Regression Suites](https://arxiv.org/html/2604.01518v1)\n- [REFINE: Enhancing Program Repair Agents through Context-Aware Patch Refinement](https://arxiv.org/pdf/2510.03588)\n- [Root-Cause-Driven Automated Vulnerability Repair](https://arxiv.org/html/2605.04251)\n- [Mining Specifications for Predictive Safety Monitoring](https://dl.acm.org/doi/10.1145/3716550.3722021)\n- [Multi-Step Generation of Test Specifications using Large Language Models](https://aclanthology.org/2025.acl-industry.11.pdf)\n- [Large Language Models for Unit Test Generation: Achievements, Challenges, and the Road Ahead](https://arxiv.org/html/2511.21382v1)\n- [Validating Formal Specifications with LLM-generated Test Cases](https://arxiv.org/html/2510.23350v1)\n- [Heterogeneous Prompting and Execution Feedback for SWE Issue Test Generation and Selection](https://arxiv.org/html/2508.06365)\n- [The Delta Learning Hypothesis: Preference Tuning on Weak Data can Yield Strong Gains](https://arxiv.org/html/2507.06187v1)\n- [Learning Program Behavioral Models from Synthesized Input-Output Pairs](https://arxiv.org/pdf/2407.08597)\n- [iFixR: Bug Report driven Program Repair](https://cs.paperswithcode.com/paper/ifixr-bug-report-driven-program-repair)\n- [ChatBR: Automated assessment and improvement of bug reports](https://dl.acm.org/doi/pdf/10.1145/3691620.3695518)\n- [Uncovering the iceberg from the tip: Generating API Specifications for Bug](https://www.ndss-symposium.org/wp-content/uploads/2025-2001-paper.pdf)\n- [What's in a Benchmark? The Case of SWE-Bench in Automated Program Repair](https://arxiv.org/pdf/2602.04449)\n- [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/)"
      }
    ],
    "totalDurationMs": 104187,
    "totalTokens": 42233,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3726,
      "cache_read_input_tokens": 33137,
      "output_tokens": 5363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3726
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 5363,
          "cache_read_input_tokens": 33137,
          "cache_creation_input_tokens": 3726,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3726,
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
  "sourceToolAssistantUUID": "49f63263-d3ad-4cec-aaf7-05b11e4fa171",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "7373a06a-319e-43a6-92e2-03ce6dd40732",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify spec extraction for code repair methods",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a"
}
```

---

### Assistant

_source line 22 · 2026-05-10T07:00:45.935Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent research! Now I have very detailed findings. Let me synthesize what I've found for this Round 3 review:

## Key Findings

### 1. SoRFT Numbers - CRITICAL UNRESOLVED ERROR

The most important finding: **SoRFT (arXiv 2502.20127, ACL 2025) achieves 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite**.

The Round 3 proposal says: "SoRFT-Qwen-7B (21.4% Verified / 14.0% Lite, structured subtask decomposition)"
 
Hold on—the search results confirm SoRFT-Qwen-7B gets 21.4% on Verified and 14.0% on Lite, which matches what Round 3 has. But Round 2's review claimed the opposite, saying 21.4% was on Lite and 14.0% was on Verified, with feedback to swap them. There's a direct contradiction between what Round 2 concluded and what the actual paper reports. The Round 3 proposal has the correct numbers—21.4% for Verified and 14.0% for Lite—which matches what the actual paper reports. The Round 2 reviewer appears to have made an error in claiming the numbers were flipped, since my search confirms the 21.4% figure is indeed for SWE-bench Verified, not Lite. I'm realizing the benchmark subsets work differently than I initially thought—SWE-bench Verified has clearer, human-verified issues while Lite represents harder, more representative cases, so Verified scores are typically higher. Looking at Agentless-1.5's performance confirms this pattern: 50.8% on Verified versus 40.67% on Lite. So SoRFT's 21.4% on Verified and 14.0% on Lite actually aligns with what we'd expect, meaning the Round 2 reviewer's critique about those numbers was off base. The search results indicate a critical problem: the SpecRover paper doesn't actually contain the specific 51.7% failure breakdown or the 107/207 count that SpecExtract claims motivated its approach. The paper apparently lacks a dedicated error analysis section categorizing failures by ambiguous issue descriptions, which undermines the entire foundation of SpecExtract's motivation.

But wait—I should consider that SpecRover might have different versions. The search checked the arXiv version (2408.02232), but the ICSE 2025 published version could have a different structure or additional sections that the arXiv preprint doesn't include. I need to verify whether the published conference version contains this analysis before concluding the claim is fabricated. Now I'm verifying the remaining papers and models from the comparison table. The search results confirm several key citations exist as claimed—SWE-bench Goes Live, SWE-Lego, GitBugs, VibeRepair, and TraceRepair all check out. For Qwen3-Coder-30B-A3B, the 3.3B active parameters are close enough to the stated 3B, and the 2× H100 requirement is reasonable for the described setup. Agentless-1.5 now properly specifies its integration backbone at 50.8% performance, which resolves the earlier ambiguity. I'm moving on to check the new competitor entry.

I found CoEvo, a paper from April 2026 that takes a different but related approach to SpecExtract by modeling tests as dynamic behavioral constraints and coevolving them with patches—it's in the same conceptual space but with distinct design choices. The SWE-bench Verified contamination issue is confirmed: Claude Mythos Preview achieved 93.9% on it, OpenAI has stopped reporting those numbers, and the proposal appropriately pivots to SWE-bench-Live as the primary evaluation. I'm now checking SWE-AGI, which appears to provide explicit normative specifications for SWE tasks.

Looking back through the previous rounds, I can see that most of the major issues have been addressed: the model naming is now correct with Qwen3-Coder-30B-A3B, the SoRFT baseline numbers check out, the integration repair agent is properly specified with Agentless and clear injection points, SWE-Lego differentiation is handled, the conditionality claim uses appropriate language about implementation-agnostic behavioral specifications, and the SWE-bench-Live size has been updated to ~1,890 instances.

However, there's still a critical unresolved issue with the SpecRover 51.7%/107/207 claim—the search couldn't verify this in the actual paper, so either I need exact verbatim quotes from the source or I should replace it with something defensible. Beyond that, I'm noticing a new paper that's come up: Agent-CoEvo from April 2026, which proposes dynamic behavioral constraint coevolution during repair, and this is something I should evaluate for relevance to the proposal.

The SWE-bench Pro numbers check out—731 public instances is correct, and the performance gap between Pro (46% max) and Verified (93.9%) actually supports SpecExtract's decision to avoid Verified. Now stepping back to assess the proposal's novelty more carefully: the approach is fundamentally about extracting structured specifications from bug reports using a fine-tuned model, then feeding those specs into an existing repair pipeline like Agentless, trained on SWE-bench test patch assertions.

This is a solid research direction with clear differentiation from related work—SpecRover operates in issue-space versus code-space, and SWE-Lego is a preprocessing module rather than end-to-end repair. Agent-CoEvo and VibeRepair are working in similar territory but with different angles: Agent-CoEvo focuses on dynamic constraints while VibeRepair goes code→spec→repair. The claim about no prior work training a dedicated model for extracting structured behavioral specs from bug reports appears mostly valid, though Agent-CoEvo does something adjacent.

On feasibility, the compute budget looks reasonable at 90-110 H100-hours within the 200-hour limit, but the 16-day timeline is quite aggressive.

The real concerns are empirical: whether the ecological validity check against SWE-bench Pro requirements will hold up, establishing a baseline for the agentless approach on SWE-bench-Live Lite, and whether AST-parsed test assertions actually provide meaningful training signals. There's also the integrity issue with the SpecRover claim that needs addressing.

Let me reconsider the SpecRover numbers more carefully. The search results show the paper discusses specification inference and patch validation but doesn't break down failure statistics by ambiguity type. However, the ICSE 2025 published version might contain different details than the arXiv v3 I checked. Looking at the math: if SpecRover resolved 93 out of 300 instances on SWE-bench Lite, that's a 31% resolution rate, which aligns with what the paper reports.

The claim about "107/207 instances labeled as ambiguous by SWE-bench Verified human annotators" is problematic though—this would require cross-referencing annotations between SWE-bench Verified and SWE-bench Lite instances, and if the paper doesn't explicitly provide this analysis, attributing it to "Section V-A, 'Reasons for Failure'" would be a fabrication.

For EMNLP 2026 with an ARR deadline of May 25 (15 days away), the NLP angle on structured information extraction from bug reports is defensible, but the timeline is extremely tight for writing a full paper and running all the necessary experiments.

The proposal acknowledges this constraint and suggests a pilot-scale approach using 500 instances from SWE-bench Verified for training and SWE-bench Lite for evaluation, which would actually be acceptable for EMNLP 2026 Findings.

The critical issue remains the unverifiable SpecRover claim—it's become even more problematic in this version because it's now citing a specific section, which increases the risk that this is a hallucinated reference. There's also a gap in addressing Agent-CoEvo (arXiv 2604.04580), which proposes dynamic behavioral constraint coevolution during repair and directly competes with the pre-extraction approach. The SoRFT numbers assessment was cut off but appears to be another concern worth investigating.

The 16-day timeline to run experiments and write for the May 25 EMNLP ARR deadline is extremely tight, though the computational budget of 160-180 H100-hours is technically feasible. The paper handles the conditionality of test assertions reasonably well, but the phrase "implementation-agnostic behavioral specifications" could still draw scrutiny from reviewers who understand that test assertions are inherently written after observing the gold patch's behavior. There's also a minor issue with the 2× H100 claim for QLoRA that needs clarification.

Looking at the scoring, novelty sits at 3.5 because while the specific combination of bug report NLP, test assertion AST parsing, and SFT is novel, the broader concept of spec extraction for repair is well-explored, and there's a competing approach in Agent-CoEvo that wasn't addressed. Feasibility is also 3.5—the approach is sound and the compute is within budget, but the main risks are whether AST-parsed specs actually align with real behavioral specifications, the aggressive timeline, and whether the Agentless baseline will be properly implemented.

The proposal scores well on clarity at 4.0 with its formal schema and worked examples, but impact is limited at 3.5 since even a 10-20% improvement would only be meaningful as a preprocessing module for an existing system rather than a standalone contribution. The overall average of 3.625 falls short of the 4.0 threshold needed to pass, primarily because the SpecRover claim remains unresolved and Agent-CoEvo wasn't discussed. The verdict is to revise—the work has made real progress addressing Round 2 feedback, but that critical SpecRover issue needs to be resolved before moving forward.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7373a06a-319e-43a6-92e2-03ce6dd40732",
  "isSidechain": false,
  "requestId": "req_011CatTNLys9agixsHhbHBmj",
  "type": "assistant",
  "uuid": "0d9e78c0-2fdc-43a3-8e9d-765594ba3c3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012cgXd95tiiTwTKx3TPPe3p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1573,
      "cache_creation_input_tokens": 10993,
      "cache_read_input_tokens": 29501,
      "output_tokens": 5246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10993,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1573,
          "output_tokens": 5246,
          "cache_read_input_tokens": 29501,
          "cache_creation_input_tokens": 10993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10993
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

_source line 23 · 2026-05-10T07:00:51.596Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Dnmjob7aUKS29iJeohAA44`</summary>

```json
{
  "description": "Fetch Agent-CoEvo paper and SpecRover v3 key sections",
  "subagent_type": "Explore",
  "prompt": "I need to verify two specific papers for an adversarial review. Please fetch and read key sections:\n\n1. **Agent-CoEvo** (arXiv 2604.04580): \"Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints\" (April 2026)\n   - Fetch: https://arxiv.org/abs/2604.04580\n   - Read the abstract and conclusion carefully\n   - What is the core approach? Does it extract specs from bug reports? Does it coevolve test assertions/behavioral constraints with patches?\n   - What benchmark does it evaluate on? What are its results?\n\n2. **SpecRover** (arXiv 2408.02232v3): \n   - Fetch: https://arxiv.org/html/2408.02232v3\n   - Navigate to Section V or Section 5 (Error Analysis / Reasons for Failure / Threats to Validity)\n   - Does this paper have a section called \"Reasons for Failure\" or anything in Section V that analyzes failure modes?\n   - Does it mention percentages like 51.7%, numbers like 107/207, or discuss \"ambiguous issue descriptions\" as a failure mode?\n   - Does it reference SWE-bench Verified human annotator labels on SWE-bench Lite failures?\n   - Report the EXACT text of any such error analysis sections you find\n\nBe very specific about what you actually find vs what is not there."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d9e78c0-2fdc-43a3-8e9d-765594ba3c3b",
  "isSidechain": false,
  "requestId": "req_011CatTNLys9agixsHhbHBmj",
  "type": "assistant",
  "uuid": "27d1ffd1-a972-437d-a075-80bed8371382",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012cgXd95tiiTwTKx3TPPe3p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1573,
      "cache_creation_input_tokens": 10993,
      "cache_read_input_tokens": 29501,
      "output_tokens": 5246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10993,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1573,
          "output_tokens": 5246,
          "cache_read_input_tokens": 29501,
          "cache_creation_input_tokens": 10993,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10993
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
  "leafUuid": "27d1ffd1-a972-437d-a075-80bed8371382",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify spec extraction for code repair methods",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a"
}
```

---

### Tool result

_source line 26 · 2026-05-10T07:01:07.387Z_

<details><summary>↩ Tool result · `toolu_01Dnmjob7aUKS29iJeohAA44`</summary>

```text
Based on my fetches, here's what I found:

## Agent-CoEvo (arXiv 2604.04580)

**Core Approach**: Agent-CoEvo implements a coevolutionary multi-agent framework where code patches and test patches are explored **simultaneously** rather than sequentially. This is fundamentally different from fixed-test optimization.

**Specification Extraction**: The abstract does not explicitly detail extraction of specs from bug reports. Instead, the framework treats behavioral constraints as iteratively refined during the repair process itself.

**Test/Constraint Coevolution**: YES - this is central to the approach. The paper states: "Through mutual evaluation and semantic recombination, code and test candidates progressively narrow the space of behavior consistent with the issue description." Tests function as "dynamic constraints that both guide and are revised by the repair process."

**Benchmarks & Results**:
- Evaluated on: **SWE-bench Lite** and **SWT-bench Lite**
- Result: "Agent-CoEvo consistently outperforms state-of-the-art agent-based and agentless baselines in both repair success and test reproduction quality"

---

## SpecRover (arXiv 2408.02232v3)

**Section V / Error Analysis Finding**: The paper **does NOT have a dedicated "Errors Analysis", "Reasons for Failure", or "Threats to Validity" section** as you asked for.

**What IS reported**: Section V contains failure mode analysis woven into the evaluation:

- **Reviewer agent accuracy**: 64.7% accuracy in determining patch correctness; 50.0% precision (meaning half of approved patches were actually incorrect)
- **False negatives**: 16 correct patches were rejected
- **Incomplete tests issue**: Tests can be "incomplete description of intent, i.e., a patch may pass the test without completely resolving the issue"
- **Data memorization**: Only 10% of SpecRover's solutions were syntactically identical to ground truth
- **Overall success**: Only 19.31% resolution on full SWE-Bench (443/2294 issues)

**NOT found**: The specific percentages you mentioned (51.7%), numbers like 107/207, "ambiguous issue descriptions" as explicit failure mode language, or references to SWE-bench Verified human annotator labels on SWE-bench Lite failures do not appear in the fetched content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27d1ffd1-a972-437d-a075-80bed8371382",
  "isSidechain": false,
  "promptId": "97188be6-5245-47ba-9011-c98eaa31631a",
  "type": "user",
  "uuid": "8116462c-ca96-4e6b-9a22-e519fceba637",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two specific papers for an adversarial review. Please fetch and read key sections:\n\n1. **Agent-CoEvo** (arXiv 2604.04580): \"Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints\" (April 2026)\n   - Fetch: https://arxiv.org/abs/2604.04580\n   - Read the abstract and conclusion carefully\n   - What is the core approach? Does it extract specs from bug reports? Does it coevolve test assertions/behavioral constraints with patches?\n   - What benchmark does it evaluate on? What are its results?\n\n2. **SpecRover** (arXiv 2408.02232v3): \n   - Fetch: https://arxiv.org/html/2408.02232v3\n   - Navigate to Section V or Section 5 (Error Analysis / Reasons for Failure / Threats to Validity)\n   - Does this paper have a section called \"Reasons for Failure\" or anything in Section V that analyzes failure modes?\n   - Does it mention percentages like 51.7%, numbers like 107/207, or discuss \"ambiguous issue descriptions\" as a failure mode?\n   - Does it reference SWE-bench Verified human annotator labels on SWE-bench Lite failures?\n   - Report the EXACT text of any such error analysis sections you find\n\nBe very specific about what you actually find vs what is not there.",
    "agentId": "aa685285eea0ca054",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my fetches, here's what I found:\n\n## Agent-CoEvo (arXiv 2604.04580)\n\n**Core Approach**: Agent-CoEvo implements a coevolutionary multi-agent framework where code patches and test patches are explored **simultaneously** rather than sequentially. This is fundamentally different from fixed-test optimization.\n\n**Specification Extraction**: The abstract does not explicitly detail extraction of specs from bug reports. Instead, the framework treats behavioral constraints as iteratively refined during the repair process itself.\n\n**Test/Constraint Coevolution**: YES - this is central to the approach. The paper states: \"Through mutual evaluation and semantic recombination, code and test candidates progressively narrow the space of behavior consistent with the issue description.\" Tests function as \"dynamic constraints that both guide and are revised by the repair process.\"\n\n**Benchmarks & Results**:\n- Evaluated on: **SWE-bench Lite** and **SWT-bench Lite**\n- Result: \"Agent-CoEvo consistently outperforms state-of-the-art agent-based and agentless baselines in both repair success and test reproduction quality\"\n\n---\n\n## SpecRover (arXiv 2408.02232v3)\n\n**Section V / Error Analysis Finding**: The paper **does NOT have a dedicated \"Errors Analysis\", \"Reasons for Failure\", or \"Threats to Validity\" section** as you asked for.\n\n**What IS reported**: Section V contains failure mode analysis woven into the evaluation:\n\n- **Reviewer agent accuracy**: 64.7% accuracy in determining patch correctness; 50.0% precision (meaning half of approved patches were actually incorrect)\n- **False negatives**: 16 correct patches were rejected\n- **Incomplete tests issue**: Tests can be \"incomplete description of intent, i.e., a patch may pass the test without completely resolving the issue\"\n- **Data memorization**: Only 10% of SpecRover's solutions were syntactically identical to ground truth\n- **Overall success**: Only 19.31% resolution on full SWE-Bench (443/2294 issues)\n\n**NOT found**: The specific percentages you mentioned (51.7%), numbers like 107/207, \"ambiguous issue descriptions\" as explicit failure mode language, or references to SWE-bench Verified human annotator labels on SWE-bench Lite failures do not appear in the fetched content."
      }
    ],
    "totalDurationMs": 15786,
    "totalTokens": 19275,
    "totalToolUseCount": 2,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1806,
      "cache_read_input_tokens": 16915,
      "output_tokens": 547,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1806
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 547,
          "cache_read_input_tokens": 16915,
          "cache_creation_input_tokens": 1806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1806,
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
      "otherToolCount": 2
    }
  },
  "sourceToolAssistantUUID": "27d1ffd1-a972-437d-a075-80bed8371382",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T07:01:32.356Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have very definitive confirmation:

1. **SpecRover Section V-A "Reasons for Failure" with 51.7%/107/207 claims**: DOES NOT EXIST in the paper. The paper has Section V content but it does NOT contain this specific error analysis. The claims are fabricated.

2. **Agent-CoEvo**: This IS a real competing paper that works on coevolving code and test constraints. It's different from SpecExtract (dynamic coevolution during repair vs. pre-extraction before repair) but is a direct competitor in the behavioral constraint space.
   
Agent-CoEvo evaluates on SWE-bench Lite and SWT-bench Lite rather than SWE-bench-Live, which does create some differentiation. But the core issue remains: the SpecRover citation is fundamentally fabricated—the generator invented a specific section with precise metrics that simply doesn't exist in the actual paper, which is a serious academic integrity problem that's been compounded by adding more false details across multiple review rounds.

Agent-CoEvo itself (arXiv 2604.04580, April 2026) proposes a directly competing approach using coevolutionary repair where tests are dynamically revised alongside code patches, which is meaningfully different from SpecExtract's pre-extraction strategy but addresses the same core problem of underspecified issues. The paper's failure to discuss this concurrent work leaves a significant gap in the landscape.

This brings my assessment to: Novelty at 3.5 due to the SpecRover fabrication undermining the motivation and Agent-CoEvo representing a parallel approach; Feasibility at 4.0 since the model and data exist with Agentless specified, though the ecological validity check and 16-day timeline pose real risks; and Clarity at 3.5 with the JSON schema being well-defined.

The impact score is 3.5—spec injection for repair is meaningful but depends entirely on whether the performance improvements actually materialize. Averaging these gives 3.625, which falls short of the 4.0 threshold, so this needs revision.

The SpecRover claim is the fundamental problem here. Once that's either removed or reframed honestly, the proposal could potentially reach passing territory. The underlying work is solid, but the false premise is a critical flaw.

Actually, stepping back on novelty—the core claim that no existing method trains a dedicated model to extract repair specifications from bug report text into structured form does seem defensible. SpecRover prompts code generation rather than training a model for extraction, so there's a meaningful distinction there.

So my final assessment: novelty is 3.5 due to the fabricated SpecRover comparison and the missing discussion of Agent-CoEvo, feasibility stays at 4.0, clarity drops to 3.5 because the fabricated claim undermines the entire motivation, and impact remains 3.5. That averages to 3.625—below threshold. The verdict is revise.

Now I need to focus my feedback on three concrete actions: first, I have to flag that SpecRover 51.7% claim in Section V-A as either needing verification or removal since it appears to be fabricated. Second, I should add Agent-CoEvo to the related work section to properly position this work against the coevolution baseline. Third, I need to make sure the SoRFT numbers are stated clearly and correctly this time, since they were wrong in the previous review round.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8116462c-ca96-4e6b-9a22-e519fceba637",
  "isSidechain": false,
  "requestId": "req_011CatTWqtPqggKKn2SNrSX8",
  "type": "assistant",
  "uuid": "dd99c4a1-026f-495e-a7ba-863fd26e8ce5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018Y1Ehzc7JcXBnyDc85LgFQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7369,
      "cache_read_input_tokens": 40494,
      "output_tokens": 3642,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7369,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3642,
          "cache_read_input_tokens": 40494,
          "cache_creation_input_tokens": 7369,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7369
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

_source line 28 · 2026-05-10T07:02:21.204Z_

Now I have all the evidence I need. Let me compile the verdict.

**Critical findings:**

1. **SpecRover Section V-A "Reasons for Failure" claim (51.7%/107/207)**: Independently verified by fetching arXiv 2408.02232v3 — this section **does not exist** in the SpecRover paper. The paper has Section V content but no failure-mode analysis naming "ambiguous issue descriptions," no 51.7% figure, no 107/207 count, and no reference to SWE-bench Verified human annotator labels on SWE-bench Lite failures. The Round 3 generator escalated the claim (added "Section V-A" label, "107/207," SWE-bench Verified attribution) without verifying it. This is a fabricated citation that worsens from Round 2.

2. **SoRFT numbers now correct**: Verified via ACL Anthology (2025.acl-long.559) — SoRFT-7B achieves 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite. The Round 3 proposal has these right. (The Round 2 reviewer was incorrect to flag these as wrong.)

3. **Agent-CoEvo (arXiv 2604.04580, April 2026)**: Verified to exist. It proposes coevolutionary repair where tests/behavioral constraints are revised dynamically alongside code patches. Directly competing approach not discussed in landscape.

4. **All other cited papers verified**: SWE-bench-Live, SWE-Lego, GitBugs, VibeRepair, TraceRepair — all exist with correct arXiv IDs and claimed results.

5. **Qwen3-Coder-30B-A3B**: Verified to exist with 3.3B active params (close to claimed "~3B"), fits QLoRA on 1× H100 (claimed 2×, slightly oversimplified but not problematic).

6. **Agentless-1.5 at 50.8% SWE-bench Verified**: Confirmed correct.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The issue-space SFT spec extraction framing is legitimate and meaningfully distinct from SpecRover (code-space prompting). However, the entire motivation chain rests on a fabricated SpecRover Section V-A failure analysis (51.7%/107/207) that does not exist in the paper; if that premise collapses, the gap claim weakens considerably. Agent-CoEvo (arXiv 2604.04580, April 2026) — a concurrent paper coevolving behavioral constraints dynamically during repair — is a direct competitor not discussed in the landscape, further narrowing the novelty claim."
    },
    "feasibility": {
      "score": 4,
      "rationale": "Technically sound: Qwen3-Coder-30B-A3B is confirmed to exist with 3.3B active params, QLoRA fits on 1-2× H100, SWE-bench data is accessible, Agentless integration is well-specified at the stage level, and manual mode compute (90-110 H100-hours) is within the 200-hour budget. Primary risk is the unverified ecological validity threshold (cosine ≥ 0.65 on SWE-bench Pro held-out slice) — failure would require schema redesign before scale-up."
    },
    "clarity": {
      "score": 4,
      "rationale": "The formal four-field JSON schema, worked NumPy example, explicit Agentless injection points, and per-field ablation design are well-specified improvements over earlier rounds. Clarity is undermined only by the fabricated SpecRover citation, which introduces a false narrative anchor that reviewers will likely attempt to verify."
    },
    "impact": {
      "score": 3,
      "rationale": "A modular preprocessing spec extractor that plugs into any repair backbone (including SWE-Lego) without retraining is a useful contribution to the engineering of repair pipelines. However, as a preprocessing module evaluated on 300-instance SWE-bench-Live Lite with an unknown baseline delta, the measured impact depends entirely on whether the spec injection actually improves Agentless resolve rates — empirically undemonstrated and not guaranteed."
    }
  },
  "issues": [
    "CRITICAL — Fabricated SpecRover citation (third consecutive round): The proposal cites 'SpecRover Section V-A, Reasons for Failure' with the specific claim that 51.7% of its 207 unresolved SWE-bench Lite tasks involve ambiguous issue descriptions (107/207 instances, labeled by SWE-bench Verified human annotators). Independent verification via WebFetch of arXiv 2408.02232v3 confirms this section does not exist — SpecRover has no dedicated error analysis section categorizing failures by issue ambiguity, and contains no 51.7% figure, 107/207 count, or SWE-bench Verified annotation cross-reference. The Round 3 generator escalated from 'unverifiable' (Round 2) to 'fabricated with false specificity' by inventing the section label, count, and labeling provenance. This is an academic integrity violation that will result in desk rejection or post-acceptance retraction if submitted as-is.",
    "SIGNIFICANT — Agent-CoEvo (arXiv 2604.04580, April 2026) not addressed in landscape: This concurrent paper, 'Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints,' proposes that behavioral constraints (tests) should be coevolved dynamically with code patches during repair rather than pre-extracted from bug reports. It evaluates on SWE-bench Lite and SWT-bench Lite and outperforms agentless baselines. This represents the most direct competing design philosophy to SpecExtract's pre-extraction approach and must be discussed — specifically, why pre-extraction from issue text before any codebase access is preferable to dynamic constraint coevolution.",
    "MODERATE — SoRFT numbers are now correct but were mishandled across three rounds: Independent verification via ACL Anthology (2025.acl-long.559) confirms SoRFT-7B achieves 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite — exactly as stated in Round 3. The Round 2 reviewer was wrong to flag these as reversed. While the numbers are now correct, three rounds of oscillation on this point suggest the generator should add a footnote citing the ACL Anthology URL to preempt reviewer confusion.",
    "MODERATE — No reported Agentless-on-SWE-bench-Live baseline: The experimental design requires establishing Agentless-direct (no spec injection) on SWE-bench-Live Lite (300 instances) as the baseline, then measuring SpecExtract-augmented Agentless. This baseline number is not reported anywhere in the proposal, making it impossible to assess whether the expected delta (e.g., +3-8 percentage points) is plausible or whether Agentless-1.5's 50.8% Verified score generalizes to the Live dataset at all. At minimum, cite the Agentless-1.5 SWE-bench-Live Lite score if published, or explicitly acknowledge this is unmeasured.",
    "MINOR — QLoRA VRAM claim is slightly oversimplified: Qwen3-Coder-30B-A3B with QLoRA requires ~17.5GB VRAM (verified via Unsloth documentation), fitting comfortably on a single H100 80GB rather than requiring 2× H100s. The 2× claim is not wrong (it enables larger batch sizes and faster throughput) but should be reframed as 'recommended configuration for efficient throughput' rather than 'minimum requirement.'"
  ],
  "feedback": "This proposal has made genuine progress across three rounds — the model choice, Agentless integration, SWE-Lego differentiation, schema definition, and compute budget are all solid. One issue now blocks this from passing, and one new issue must be addressed:\n\n(1) **IMMEDIATE: Remove or replace the fabricated SpecRover Section V-A claim.** There is no 'Section V-A: Reasons for Failure' in SpecRover, no 51.7% figure, no 107/207 count, and no SWE-bench Verified annotation cross-reference in the paper. Replace the entire motivation chain with a defensible framing: 'SpecRover (ICSE 2025) evaluates on SWE-bench Lite and explicitly acknowledges that its code-space traversal approach cannot resolve cases where the issue description itself is underspecified — it can only infer specifications from code that exists, not from behavior that is described but not yet correctly implemented. This architectural limitation motivates an issue-space approach that operates on bug report text before codebase access.' If you want to keep a quantitative hook, look at SpecRover's SWE-bench Lite resolve rate (31%) and the known proportion of SWE-bench tasks where the issue description is classified as ambiguous by SWE-bench Verified human annotators — cite the SWE-bench Verified paper (arXiv 2410.06992) or the SWE-bench Pro paper for that annotation, not SpecRover.\n\n(2) **Add Agent-CoEvo to related work.** One paragraph: 'Agent-CoEvo (arXiv 2604.04580, April 2026) proposes coevolving code and test patches simultaneously during repair, treating tests as dynamic behavioral constraints. SpecExtract takes the complementary pre-extraction stance: issue-space specs derived before any codebase access reduce the search space for both fault localization and patch generation, and are reusable across repair backbones without retraining — including static repair systems like Agentless that do not support dynamic constraint revision.'\n\n(3) **Add Agentless-on-SWE-bench-Live baseline.** State the known or estimated Agentless-1.5 resolve rate on SWE-bench-Live Lite (or acknowledge it as an early experimental measurement to be reported in the paper). The experimental contribution is the delta, and without the baseline anchor the paper cannot make its empirical case.\n\nWith these three changes — particularly (1) — this proposal should be able to pass in Round 4.",
  "reason": "The fabricated SpecRover Section V-A citation (51.7%/107/207, now in its third round and made more specifically false with each revision) is the sole blocker for an otherwise technically sound proposal; removing it and adding Agent-CoEvo to the landscape resolves the remaining critical gaps."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd99c4a1-026f-495e-a7ba-863fd26e8ce5",
  "isSidechain": false,
  "requestId": "req_011CatTWqtPqggKKn2SNrSX8",
  "type": "assistant",
  "uuid": "18f310c6-208a-464b-a0cf-95cd8ea487bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018Y1Ehzc7JcXBnyDc85LgFQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7369,
      "cache_read_input_tokens": 40494,
      "output_tokens": 3642,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7369,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3642,
          "cache_read_input_tokens": 40494,
          "cache_creation_input_tokens": 7369,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7369
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "18f310c6-208a-464b-a0cf-95cd8ea487bd",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify spec extraction for code repair methods",
  "sessionId": "78f395f4-5c6b-48f5-b7df-f42fdf4d4c8a"
}
```

---
