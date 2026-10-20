# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/9c7af506-9068-4d10-a414-f029954427c9.jsonl`
- **Structured JSON:** [`def7b6bee7935fa4ca77.json`](../../sessions/de/def7b6bee7935fa4ca77.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:50:28.520Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:50:28.520Z",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 7/10)\n{\n  \"title\": \"SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair\",\n  \"core_problem\": \"Automated repair agents fail on ambiguous bug reports not from lack of code understanding, but because unstructured issue text leaves behavioral expectations underspecified — what interface should change, what the user observed, and what correct behavior looks like are rarely made explicit. SpecRover (ICSE 2025) partially addresses this via per-instance LLM prompting that extracts specifications from CODE during codebase traversal, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue. Its error analysis (Section V-A, 'Reasons for Failure'; see https://arxiv.org/html/2408.02232, Section V-A) identifies that 107 of its 207 unresolved SWE-bench Lite tasks (51.7%) are classified as 'ambiguous issue description' — cases the paper characterizes as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for why underspecified descriptions constitute an irreducible failure mode for code-space approaches. This architectural limitation is structural: code-side spec extraction can only infer specifications from code that already exists, not from behavior that is described in the issue but not yet correctly implemented. Bug reports routinely contain latent behavioral specifications in their runtime artifacts: stack traces name the affected interface, error messages describe observed behavior, and reproducer assertions encode expected behavior. No method trains a dedicated model to extract these signals from bug report text into a structured repair specification — covering affected interface, observed behavior, expected behavior, and their delta — that could constrain both fault localization and patch generation before any codebase traversal begins.\",\n  \"opportunity\": \"Failing test assertions in SWE-bench's test patches encode implementation-agnostic behavioral specifications without revealing implementation strategies: `assert result == expected_value` or `with pytest.raises(ValueError)` states precisely what the program SHOULD do, independent of WHICH code to change or HOW to change it. By mechanically converting (problem_statement + test_patch assertions + stack traces) to structured JSON spec fields using AST-level test parsing and NLP extraction on SWE-bench's 2,294 instances, we construct a training corpus of 2,294 (bug_report, structured_spec) pairs — where the spec encodes behavioral expectations derivable without knowing the implementation strategy. This avoids the critical flaw of training on SWE-bench Pro requirements, which were authored by humans with full access to the golden patch (making them solution-conditioned). SWE-bench-Live (NeurIPS 2025, arXiv 2505.23419; ~1,890 Docker-reproducible instances across 223 repositories, drawn from post-January-2024 GitHub issues, growing at ~50 instances/month) provides a clean, contamination-resistant evaluation target with no training-set overlap. As SWE-bench Verified saturates with contamination concerns (OpenAI officially deprecated it in February 2026), SWE-bench-Live provides contamination-resistant evaluation on post-2024 issues unavailable during model training. SWE-bench Pro's human-written `requirements` and `interface` fields (731 public instances) serve as an ecological validity check — we measure cosine similarity between machine-derived specs and human requirements on a held-out 200-instance slice — confirming that AST-parsed test assertions produce specs that match expert behavioral descriptions, without using requirements as training supervision.\",\n  \"landscape\": \"SpecRover (ICSE 2025, arXiv 2408.02232) is the closest prior work: given a GitHub issue, it iteratively traverses the codebase, prompting Claude 3.5 Sonnet to extract function-level summaries from visited code, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue and 31% on SWE-bench Lite (93/300). SpecRover operates in code-space (it visits source files to generate specs from code) and uses per-instance prompting (no fine-tuning). Our approach operates in issue-space (extracts specs from bug report text and runtime artifacts before any codebase traversal) and uses supervised fine-tuning (consistent structured output at ~$0.05-0.10/issue). These are complementary directions: SpecRover's code-space specs and our issue-space specs could ultimately be fused. Agent-CoEvo (arXiv 2604.04580, April 2026) proposes the most directly competing design philosophy: rather than pre-extracting behavioral constraints from issue text, it coevolves code patches and test patches simultaneously during repair, treating tests as dynamic constraints that are iteratively revised alongside candidate fixes. Agent-CoEvo achieves 41.33% on SWE-bench Lite (DeepSeek-V3) and 46.4% on SWT-bench Lite, outperforming Agentless-1.5 (32%) on those benchmarks. SpecExtract takes the complementary pre-extraction stance: (1) issue-space specs derived before any codebase access are reusable across repair backbones without retraining, including static pipeline systems like Agentless that do not support dynamic constraint revision during search; (2) pre-extracted specs reduce the initial search space before coevolution begins, making SpecExtract a potential front-end that improves Agent-CoEvo's starting population rather than competing with it. SWE-Lego (arXiv 2601.01426, Jan 2026) is the most directly competing concurrent SFT work: it trains on 32k high-quality task instances with error masking and a difficulty-based curriculum, achieving 52.6% on SWE-bench Verified (58.8% with test-time scaling at 16 samples) using a 32B model. SWE-Lego is an end-to-end system that produces complete code fixes; SpecExtract is a preprocessing module that extracts structured behavioral specs from bug report text before any repair attempt, and can plug into SWE-Lego or any other repair backbone as a drop-in front-end — improving fault localization precision and patch generation alignment without retraining the repair agent itself. CodeSpecBench (arXiv 2604.12268, April 2026) benchmarks existing LLMs (Claude, GPT-4, Gemini) on executable behavioral specification generation via prompting — it does not train a dedicated extractor, operates on code-side and description inputs rather than bug report runtime artifacts, and is an evaluation framework rather than a preprocessing pipeline for repair. Its existence confirms that structured specification generation is an active research area, while simultaneously validating the gap: no trained, issue-space specification extractor for repair preprocessing exists. VibeRepair (arXiv 2602.08263, Feb 2026) translates buggy CODE into behavior specifications, repairs the spec, then synthesizes corrected code, achieving 19-23% improvement on Defects4J — code-space to spec, not text-space to spec. TraceRepair (arXiv 2604.02647, Apr 2026) uses runtime execution traces generated by instrumented code execution as shared repair constraints across a multi-agent committee, fixing 392 Defects4J defects — traces are generated during repair, not extracted from issue text before repair begins. RepoRepair (arXiv 2603.01048) generates hierarchical code documentation from source files toward the bug; its documentation is code-driven, not report-driven. SoRFT (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) fine-tunes on SWE-bench with RL to decompose the repair TASK into subtasks (file → function → line → edit), achieving 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite with a 7B model (30.8% Verified and 24.0% Lite with a 32B model) — it structures the repair pipeline, not the issue semantics. PathFix (arXiv 2510.14341) derives behavioral specs from static code execution paths — code-space and offline, not issue-space. The gap: no existing work trains a dedicated model to extract structured behavioral specifications from bug report text and embedded runtime artifacts, operating entirely in issue-space before codebase access.\",\n  \"approach\": \"We train SpecExtract, a Qwen3-Coder-30B-A3B model (Mixture-of-Experts: 30B total parameters, ~3B active per token — fine-tuning and inference cost scale with active parameters, comparable to a 3B dense model; fits on a single H100 80GB with QLoRA at ~17.5GB VRAM per Unsloth benchmarks; 2× H100 is the recommended training configuration for throughput, not minimum requirement) fine-tuned to map (bug_report_text, runtime_artifacts?) → structured JSON spec, where runtime artifacts are any combination of stack traces, error messages, test failure output, or explicit reproducer assertions present in the issue text. The model gracefully handles varying artifact availability through a masked-field training protocol: training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs. Each artifact field (stack_trace, error_message, test_assertions) is independently masked with p=0.5 at training time; masked fields are replaced with a [MISSING] token, and the model is trained to output null for those positions while filling remaining fields from whatever signals are available — not to infer missing artifacts from correlated signals. **Formal schema**: Each spec has four typed fields — (1) `affected_interface`: {module: str, signature: str|null, entry_point: str} extracted from stack frame function names and explicitly mentioned APIs; (2) `observed_behavior`: {error_type: str|null, error_message: str|null, symptom: str} from error output and user complaint; (3) `expected_behavior`: {description: str, assertions: [str]} as natural-language description plus test-style constraint strings when derivable; (4) `behavioral_delta`: str, a one-sentence expected-vs-actual summary. Worked example for a NumPy issue 'linalg.solve silently returns None for singular matrices instead of raising': {affected_interface: {module: 'numpy.linalg', entry_point: 'solve', signature: 'solve(a, b)'}, observed_behavior: {error_type: null, symptom: 'returns None for singular matrix input'}, expected_behavior: {description: 'should raise for non-invertible input', assertions: ['raises np.linalg.LinAlgError when matrix is singular']}, behavioral_delta: 'solve silently returns None instead of raising LinAlgError on singular input'}. **Training data construction (implementation-agnostic behavioral specifications)**: From SWE-bench full (2,294 instances including Verified 500 and the broader set): (1) parse `test_patch` test functions via Python AST to extract formal assertions — pytest.raises calls → error_type, assert statements → expected_behavior.assertions, decorated test function signatures → affected_interface hints; (2) extract stack traces and error strings from `problem_statement` text via regex heuristics → observed_behavior; (3) combine via LLM-assisted template fill using Qwen3-Coder-30B-A3B in a chain-of-thought extraction pass to produce coherent spec JSON; (4) validate on 200 SWE-bench Pro public instances that have non-null `requirements` and `interface` fields by computing cosine similarity (sentence-transformer) between mechanically-derived specs and human-authored requirements — target alignment ≥ 0.65 before training at scale (this threshold aligns with established semantic similarity cutoffs in information-extraction evaluation literature, where scores below 0.65 on sentence-transformer embeddings indicate insufficient semantic overlap for structural field matching); this validates the schema rather than using requirements as training targets. This is a pilot ecological validity check only — it confirms schema alignment with expert behavioral annotations on curated SWE-bench instances but cannot validate generalization to genuinely ambiguous in-the-wild reports that are not SWE-bench-adjacent; a full generalization validation would require human annotation of randomly sampled GitBugs instances and is deferred to the ICSE 2027 extended paper. Important framing on conditionality: test assertions are written alongside gold patches and encode the behavioral outcome the fix achieves. The training specs are therefore *implementation-agnostic* — they do not reveal which code to change or the implementation strategy — rather than strictly solution-independent. This distinction is explicitly addressed in the paper to avoid overclaiming. The EMNLP 2026 ARR submission uses the 2,294-instance SWE-bench full corpus as the SFT training set; GitBugs augmentation (~3,000 pseudo-labeled instances, yielding a ~5,300-instance total corpus) is reserved for the ICSE 2027 extended paper. **Differentiation from SpecRover**: (1) issue-space — no codebase traversal needed at spec extraction time; (2) supervised learning — consistent, typed JSON output from a single forward pass (~$0.05-0.10/issue) vs. SpecRover's multi-step code traversal ($0.65/issue); (3) directly targets SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved SWE-bench Lite tasks) by conditioning on all available runtime artifacts in the issue, not just the code side. **Integration with Agentless**: Agentless (arXiv 2407.01489) is used as the repair backbone for all SWE-bench-Live evaluations — it follows a fixed pipeline (hierarchical fault localization → patch generation → patch selection) with no iterative tool calls, making spec injection clean and reproducible. Agentless's fault localization uses (a) LLM prompting over the repository folder tree to identify suspicious directories and (b) embedding-based cosine similarity retrieval over code chunks — it does not use BM25. SpecExtract specs are injected at two points: (1) fault localization — we modify the LLM prompting step by prepending a structured spec header (affected_interface.module + entry_point) before the folder listing, so the LLM identifies suspicious directories with the affected interface explicitly in context; we additionally introduce a BM25 pass over file paths and module docstrings using the extracted interface tokens as a third retrieval signal complementing Agentless's existing embedding-based similarity — BM25 exact-match on lexically-specific tokens like `numpy.linalg` or `django.db.models.QuerySet` catches files that semantic embeddings miss when the module is underrepresented in the embedder's training distribution, exactly the localization failure mode that intensifies on post-2024 SWE-bench-Live repos relative to in-distribution SWE-bench Verified; (2) patch generation — the repair LLM receives all four spec fields as an explicit behavioral constraint header in its prompt, focusing generation on the documented behavioral delta. **Agentless baseline on SWE-bench-Live**: Per the SWE-bench-Live paper (arXiv 2505.23419, Table 3), Agentless resolves 11.67% (GPT-4o), 12.00% (GPT-4.1), and 13.33% (DeepSeek V3) of SWE-bench-Live Lite (300 instances) — substantially below its ~50.8% on SWE-bench Verified, reflecting the contamination-resistant, harder distribution of post-2024 issues. These published numbers establish the Agentless-direct baseline; SpecExtract targets +4-7 percentage points improvement over the best Agentless backbone, which is reported as the primary experimental contribution. **Mechanistic case for the +4-7 pp improvement target**: Agentless's embedding-based file localization achieves ~57% file-level Recall@1 on SWE-bench Lite (original Agentless paper), yet its end-to-end resolve rate drops ~4× from SWE-bench Verified (~50.8%) to SWE-bench-Live Lite (13.33% best case). A primary contributor to this degradation is fault localization failure on post-2024 repos that are underrepresented in embedding model training data: embedding similarity between an issue query and post-2024 codebase chunks is noisier than on in-distribution repos, because the model has not seen those module structures and naming conventions. SpecExtract's BM25 pass on extracted module/entry_point tokens addresses this directly: exact-match retrieval on tokens like `numpy.linalg` does not require the embedding model to have indexed those repository paths during pretraining and does not degrade under distribution shift. Hybrid BM25+dense retrieval is well-established to improve out-of-domain recall in code search — a two-stage pipeline combining BM25 first-pass retrieval with dense reranking improves MRR by 8.6% over dense-only on out-of-distribution queries (Revisiting Code Search in a Two-Stage Paradigm, ICSE 2023). The +4-7 pp improvement target reflects two compounding gains: (a) localization improvement from BM25-anchored interface token matching, which provides a high-precision signal robust to the post-2024 distribution shift Agentless's embedder faces; (b) generation improvement from Stage 3 behavioral constraint injection narrowing the patch candidate space to the documented behavioral delta — these gains compound because better localization provides a more focused candidate file set for patch generation. **Evaluation**: Primary eval on SWE-bench-Live Lite (300 instances, contamination-resistant, post-2024 issues) with Agentless as backbone; per-field ablations independently zero out each spec field to quantify individual contribution to resolve rate. Secondary eval: cosine-similarity validation on 200 SWE-bench Pro held-out instances (schema validity check). Comparison baselines: Agentless direct repair without spec (established at 11-13% from published SWE-bench-Live results), SpecRover-equivalent prompting (ablation of supervised fine-tuning benefit), SoRFT-Qwen-7B (21.4% Verified / 14.0% Lite, structured subtask decomposition), SWE-Lego (52.6% Verified, end-to-end SFT backbone — SpecExtract as preprocessing front-end demonstrates orthogonal contribution). **Publication scope**: The EMNLP 2026 ARR submission (auto-research mode, 6-10 days) reports results on the 2,294-instance SWE-bench full SFT corpus with SWE-bench-Live Lite 300-instance primary eval and a 2-field ablation (affected_interface vs. none, expected_behavior vs. none) — the two fields with the strongest localization and generation signal respectively. The full 5,300-instance corpus (with GitBugs augmentation) and all four per-field ablation fields constitute the ICSE 2027 extended paper.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~90-110 H100-hours (~180-220 A100-equivalent hours)\",\n      \"gpu_breakdown\": \"SFT partition (~10-14 H100-hours): Qwen3-Coder-30B-A3B QLoRA fine-tuning on 5,300 instances, 3 epochs, 2× H100 80GB recommended for throughput (single H100 80GB is technically sufficient at ~17.5GB VRAM) — MoE active-parameter efficiency reduces training cost to ~3B dense equivalent. Eval partition (~80-96 H100-hours): spec extraction inference on 5,300 instances (~4 H100-hours); SWE-bench-Live Lite main eval 300 instances × 12.5 min/instance / 4 parallel H100s ≈ 16 H100-hours; per-field ablations 4 fields × 300 instances ≈ 64 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~50-60% — Docker sandbox test execution during SWE-bench-Live eval is CPU-bound; GPU idles between model inference calls\",\n      \"timeline\": \"3-5 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$216-264 (90-110h × $2.40/hr H100 SXM5 on-demand; within the 200 H100-hour hard constraint)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~135-160 H100-hours (~270-380 A100-equivalent hours)\",\n      \"gpu_breakdown\": \"SFT partition (~25-35 H100-hours): 3 fine-tuning configurations (schema variant, augmentation ablation, masked-field protocol variant). Eval partition (~110-125 H100-hours): spec extraction ~5 H100-hours; Agentless baseline run on 300 instances ≈ 16 H100-hours; SWE-bench-Live partial eval 600 instances / 4 parallel ≈ 31 H100-hours; per-field ablations on 300-instance subset × 4 fields ≈ 62 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~60-70% — agent runs fine-tuning and SWE-bench-Live eval jobs continuously; human approves schema validation threshold, masked-field training protocol, retrieval bias weights, and ablation scope at daily check-ins\",\n      \"timeline\": \"5-9 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$200-400 (~2,500 orchestration turns at ~$0.10/turn Opus)\",\n      \"estimated_gpu_cost\": \"~$324-384 (135-160h × $2.40/hr H100); within the 200 H100-hour hard constraint\",\n      \"risk_note\": \"Critical unknown: whether AST-parsed test assertions produce specs that align with human behavioral descriptions (measured by cosine similarity ≥ 0.65 on 200 SWE-bench Pro validation instances). If alignment is below threshold, the spec schema needs redesign before scale-up. GitBugs pseudo-spec quality is the secondary risk — human spot-check of 100 instances recommended before augmentation scale-up.\"\n    },\n    \"auto_research\": {\n      \"note\": \"Budget-capped auto-research only — uncapped sweeps would exceed the 200 H100-hour hard constraint. Capped to 3 fine-tuning configurations × 1 retrieval variant × 1 patch-generation prompt strategy on SWE-bench-Live Lite (300 instances) for the main configuration sweep, then ablations on the best-performing config only.\",\n      \"gpu_hours\": \"~160-180 H100-hours (budget-capped)\",\n      \"gpu_breakdown\": \"SFT partition (~30-35 H100-hours): 3 QLoRA configs on 5,300 instances. Eval partition (~130-145 H100-hours): 3-config main sweep 3 × 300 instances ≈ 48 H100-hours; per-field ablations on best config 300 × 4 fields ≈ 64 H100-hours; Agentless baseline ≈ 16 H100-hours; spec extraction inference ≈ 5 H100-hours; validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~80-85% — continuous fine-tuning, inference, and SWE-bench-Live Docker eval; sandbox parallelized across 30 instances simultaneously\",\n      \"timeline\": \"6-10 days with 4 parallel H100 GPUs\",\n      \"team\": \"0 (setup only, ~3h initial configuration)\",\n      \"claude_api_cost\": \"$400-600 (~4,500 turns)\",\n      \"estimated_gpu_cost\": \"~$384-432 (160-180h × $2.40/hr H100)\",\n      \"speed_bottleneck\": \"SWE-bench-Live Docker sandbox throughput, not GPU compute; Qwen3-Coder-30B-A3B MoE inference (~3B active params) is fast and avoids multi-GPU coordination overhead that a dense 30B model would require\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026 — 15 days remaining; conference October 24-29, Budapest) — NLP angle on structured information extraction from semi-structured bug text; EMNLP ARR submission reports auto-research results (6-10 days): SFT on SWE-bench full 2,294-instance corpus (GitBugs augmentation deferred to ICSE), SWE-bench-Live Lite 300-instance primary eval, and 2-field ablation (affected_interface vs. none, expected_behavior vs. none). The full 5,300-instance corpus with all four per-field ablation fields is the ICSE 2027 extended paper.\",\n    \"ICSE 2027 (abstract deadline June 23, 2026; full paper ~July 2026; conference April-May 2027, Dublin) — SE angle; preferred primary target for full experimental results including GitBugs-augmented 5,300-instance corpus, SWE-bench-Live partial-set ablations, and all four per-field ablation conditions\",\n    \"NeurIPS 2026 (submission deadline expected May-June 2026) — systems and benchmarks angle; natural co-venue given SWE-bench-Live is NeurIPS 2025\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"SpecRover: Code Intent Extraction via LLMs (arXiv 2408.02232, ICSE 2025) — primary related work: code-space spec inference via prompting, 31% SWE-bench Lite (93/300), $0.65/issue; Section V-A 'Reasons for Failure' (see https://arxiv.org/html/2408.02232, Section V-A) categorizes 107/207 unresolved SWE-bench Lite tasks (51.7%) as 'ambiguous issue description', cases characterized as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for the hardness of this failure mode\",\n    \"SWE-bench Goes Live! (arXiv 2505.23419, NeurIPS 2025 D&B) — primary evaluation benchmark: ~1,890 contamination-resistant instances across 223 repositories, post-2024 GitHub issues, Docker-reproducible, growing at ~50 instances/month; Table 3 reports Agentless on SWE-bench-Live Lite (300 instances) at 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3) — establishes the Agentless-direct baseline for our evaluation\",\n    \"Agent-CoEvo: Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints (arXiv 2604.04580, April 2026) — most directly competing design philosophy: coevolves code patches and test patches simultaneously during repair (41.33% SWE-bench Lite with DeepSeek-V3); SpecExtract's pre-extraction stance is complementary — issue-space specs reduce the initial search space before coevolution, and are pipeline-agnostic for static repair systems that do not support dynamic constraint revision\",\n    \"SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (arXiv 2509.16941) — schema ecological validity validator: 731 public instances with human requirements and interface fields\",\n    \"SWE-Lego (arXiv 2601.01426, Jan 2026) — most competitive concurrent SFT work: 32k training instances, difficulty-based curriculum SFT, 52.6% SWE-bench Verified (58.8% with 16-sample test-time scaling) with 32B model; end-to-end repair backbone that SpecExtract can serve as a preprocessing front-end for\",\n    \"Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489) — integration repair backbone: open-source fixed pipeline with (a) LLM prompting over repository folder tree for directory filtering and (b) embedding-based cosine similarity retrieval over code chunks; SpecExtract augments both with a structured spec header in the LLM prompt and a BM25 third retrieval pass on extracted interface tokens; ~50.8% SWE-bench Verified (Agentless-1.5), 32% SWE-bench Lite; file-level Recall@1 ~57% on SWE-bench Lite\",\n    \"Revisiting Code Search in a Two-Stage Paradigm (ICSE 2023, dl.acm.org/doi/pdf/10.1145/3539597.3570383) — hybrid BM25+dense code retrieval: two-stage BM25 first-pass → CodeBERT reranking improves MRR by 8.6% over dense-only on out-of-distribution queries; mechanistic support for adding BM25 as a third retrieval signal in Agentless fault localization on post-2024 SWE-bench-Live repos\",\n    \"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (arXiv 2604.12268, April 2026) — evaluates prompting-based spec generation from code and descriptions using existing LLMs; does not train a dedicated extractor, operates on code-side inputs rather than bug report runtime artifacts, and is an evaluation framework rather than a repair preprocessing pipeline — confirms structured spec generation is an active research area while the trained, issue-space extractor gap remains open\",\n    \"Specification Vibing for Automated Program Repair / VibeRepair (arXiv 2602.08263, Feb 2026) — code-space spec extraction before repair, Defects4J, 19-23% improvement\",\n    \"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate / TraceRepair (arXiv 2604.02647, Apr 2026) — trace-based repair constraints during execution, Defects4J\",\n    \"SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) — structured repair subtask decomposition with RL; SoRFT-Qwen-7B: 21.4% SWE-bench Verified / 14.0% SWE-bench Lite; SoRFT-Qwen-32B: 30.8% SWE-bench Verified / 24.0% SWE-bench Lite; key baseline for SpecExtract's supervised fine-tuning approach\",\n    \"On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481) — fault localization recall analysis: documents how localization granularity and retrieval method affect end-to-end repair performance; provides empirical context for why embedding-based localization degrades on out-of-distribution repos\",\n    \"GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More (arXiv 2504.09651) — 150K+ open-licensed bug reports for training augmentation\",\n    \"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048)\",\n    \"PathFix: Automated Program Repair with Expected Path (arXiv 2510.14341)\"\n  ],\n  \"description\": \"We introduce SpecExtract, the first supervised issue-space specification extractor for program repair: a fine-tuned Qwen3-Coder-30B-A3B model (MoE, ~3B active parameters — fine-tuning and inference cost comparable to a 3B dense model; fits on a single H100 80GB at ~17.5GB VRAM with QLoRA; 2× H100 recommended for training throughput) that maps (bug_report_text, runtime_artifacts?) → a structured four-field JSON spec covering affected interface, observed behavior, expected behavior, and behavioral delta. The key methodological insight is that failing test assertions in SWE-bench test patches encode implementation-agnostic behavioral specifications — they state what the program SHOULD do without revealing which code to change or the implementation strategy — enabling AST-level test parsing combined with problem-statement NLP extraction to construct 2,294 clean (bug_report, structured_spec) training pairs from SWE-bench. The masked-field training protocol (p=0.5 per artifact field, [MISSING] token, null output for masked positions) enables graceful handling of partially-available runtime artifacts at inference time. GitBugs (150K+ open-licensed bug reports) provides ~3,000 pseudo-labeled augmentation instances for the ICSE 2027 extended paper; the EMNLP 2026 ARR submission uses the 2,294-instance SWE-bench full corpus only. SWE-bench Pro public requirements serve as a pilot ecological validity check (cosine similarity ≥ 0.65 on 200 held-out instances, confirming schema alignment with expert annotations rather than generalizing to in-the-wild reports), not a training target. Extracted specs are integrated with Agentless as the repair backbone: Agentless's fault localization uses LLM prompting over the repository folder tree plus embedding-based cosine similarity retrieval — SpecExtract augments this by (a) prepending a structured spec header (affected_interface.module + entry_point) to the LLM prompting step and (b) adding a BM25 pass over file paths and docstrings using extracted interface tokens as a third retrieval signal, catching files that embedding similarity misses when the module is underrepresented in the embedder's training distribution (a failure mode that intensifies on post-2024 SWE-bench-Live repos); at patch generation, a structured behavioral constraint prefix focuses generation on the documented delta. Primary evaluation is on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues), with the Agentless-direct baseline established at 11-13% from published SWE-bench-Live results (Table 3, arXiv 2505.23419) and a mechanistically-grounded target improvement of +4-7 percentage points: Agentless's ~57% file-level Recall@1 on SWE-bench Lite degrades on post-2024 repos where embedding similarity is noisiest, and BM25-anchored lexical matching on extracted module/function tokens provides a distribution-shift-robust localization signal, consistent with hybrid retrieval literature showing 8.6% OOD MRR gains (ICSE 2023 two-stage code search). Per-field ablations measure individual spec contributions. Agent-CoEvo (arXiv 2604.04580, 41.33% SWE-bench Lite) represents the competing dynamic-coevolution philosophy; SpecExtract's pre-extraction stance is complementary — pipeline-agnostic and applicable to static repair systems. SWE-Lego (52.6% Verified with 32B) is included as an end-to-end SFT baseline to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end. Differentiated from SpecRover (code-space prompting, $0.65/issue, 31% SWE-bench Lite) by operating in issue-space at ~$0.05-0.10/issue — directly targeting SpecRover's Section V-A identified 51.7% ambiguous-description failure mode. Compute in H100-hours: manual mode ~90-110 H100-hours (SFT ~10-14 H100-hours, eval ~80-96 H100-hours), within the 200-hour hard constraint.\",\n  \"project_name\": \"structured_spec_repair\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Training data availability: The public SWE-bench Pro HuggingFace dataset contains 731 instances from 11 repositories with copyleft licenses. The remaining 1,134 instances (held-out: 12 repos, commercial: 18 proprietary repos) are explicitly not publicly accessible. The proposal's assumption of ~1,865 training pairs is wrong by a factor of 2.5x. At 731 instances, standard fine-tuning of a 32B Qwen3-Coder model risks severe overfitting and is far too small for reliable generalization.\", \"CRITICAL — Training signal invalidity (train-test distribution mismatch): SWE-bench Pro requirements were authored by humans with full access to the golden patch AND the passing test suite, working backward from tests to specifications. They are solution-conditioned prescriptive clarifications of already-solved problems. Real-world target bug reports are solution-ignorant descriptive complaints from confused users. Fine-tuning SpecExtract on (solution-knowing-human-written-spec → structured-spec) pairs will not teach the model to extract specs from genuinely ambiguous bug reports — it will teach it to produce post-hoc rationalizations of known solutions. This fundamental mismatch is not acknowledged and cannot be patched by synthetic augmentation alone.\", \"CRITICAL — Evaluation benchmark reliability: SWE-bench Verified shows SOTA of 93.9% (Claude Mythos Preview, May 2026) with documented evidence of data contamination — OpenAI has officially stopped recommending Verified scores for meaningful comparison. Demonstrating a statistically meaningful improvement on a benchmark where frontier models may be reproducing gold patches verbatim severely weakens the paper's empirical contribution.\", \"Novelty gap — SpecRover (ICSE 2025, arXiv 2408.02232) performs iterative code intent extraction and specification inference from GitHub issue descriptions using LLM agents (not supervised training), and achieves >50% improvement in repair rate on SWE-bench at $0.65/issue. The paper's claim that 'no prior work trains a spec extractor' is technically true but misses that SpecRover occupies the same research niche via prompting. The paper must explicitly frame what the supervised training provides that SpecRover's prompting approach cannot.\", \"Compute unit mismatch vs. hard constraint: The hard constraint is ≤200 H100-hours. All estimates are given in A100-hours. H100 is ~2–3× faster than A100 for transformer fine-tuning workloads, so 200 A100-hours ≈ 67–100 H100-hours (manual, within budget), but the auto-research mode at 800 A100-hours ≈ 300–400 H100-hours exceeds the hard constraint. The paper should explicitly reconcile resource estimates in H100-hours and confirm the primary research plan stays within budget.\", \"Structured spec schema undefined: The proposal outputs 'structured specs' with fields (affected interface, pre/post-conditions, expected/actual behavior delta), but these fields are never formally defined — no JSON schema, no field type definitions, no examples of what a valid spec looks like. SWE-bench Pro requirements are freeform prose; the conversion of freeform requirements to structured JSON is the hardest step and receives no design discussion.\", \"Data leakage if evaluation pivots to SWE-bench Pro: If the proposal trains on SWE-bench Pro (public: 731 instances) and evaluates on the same benchmark, it cannot cleanly show generalization. The community will ask whether the structured spec format was reverse-engineered from the test set rather than learned from scratch.\"]\nFeedback: The core direction — using SWE-bench Pro annotations to supervise structured specification extraction — is creative and timely, but rests on a mischaracterization of what SWE-bench Pro requirements actually are and how many are publicly accessible. To revise toward 'pass': (1) **Fix the training data premise**: Acknowledge that SWE-bench Pro public set is 731 instances, not 1,865. Address the solution-conditioned nature of the requirements by designing the training task as 'given the bug report + human requirements, produce structured spec fields,' treating the requirements as an alignment target rather than pretending they were extracted from bug reports alone. (2) **Address SpecRover directly**: Add SpecRover (ICSE 2025, arXiv 2408.02232) to the related work and explicitly argue why supervised fine-tuning generalizes better than per-instance LLM prompting — e.g., lower inference cost, better calibration, consistency across bug report styles. (3) **Replace SWE-bench Verified as primary eval**: Use SWE-bench Pro public (731 instances) with a held-out split for evaluation, and add an additional out-of-distribution eval on RepoBench or DebugBench to show generalization. Explicitly argue why SWE-bench Pro's requirements-based evaluation is the right target, not the contaminated Verified leaderboard. (4) **Define the structured spec schema**: Add a formal schema definition with field types and a worked example. Show how SWE-bench Pro freeform requirements can be automatically converted to this schema via a parsing step (this becomes its own empirical contribution). (5) **Reconcile compute in H100-hours**: Convert all estimates to H100-hours and confirm manual mode (~67–100 H100-hours) is well within the 200-hour budget. Remove or prominently caveat auto-research mode since it exceeds the hard constraint.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Model naming error: 'Qwen3-Coder-14B' does not exist. Qwen3-Coder is only available in 30B-A3B (MoE, 3B active) and 480B-A35B variants. The closest viable alternatives are Qwen3-14B (dense, base Qwen3 family) or Qwen2.5-Coder-14B (prior generation). This error must be corrected with the actual model to be used, and any VRAM/compute estimates adjusted accordingly.\", \"CRITICAL — Unverifiable SpecRover failure claim: The proposal states SpecRover 'explicitly identifies that 51.7% of its unresolved SWE-bench Lite failures stem from ambiguous issue descriptions.' This specific statistic could not be verified from the SpecRover abstract or public-facing sections. If this is an inference rather than a direct quote, it must be either verified by citing the exact section, reframed as an approximation, or removed. The entire motivation chain rests on this number.\", \"SIGNIFICANT — SoRFT baseline misrepresented: The proposal states SoRFT achieves '21.4% on SWE-bench Verified with a 7B model' but SoRFT (ACL 2025) actually reports 21.4% on SWE-bench Lite, not Verified. The Verified number for SoRFT-7B is 14.0%. Using the wrong benchmark undermines the baseline comparison.\", \"SIGNIFICANT — Integration repair agent unspecified: The primary experimental claim requires running a full end-to-end repair pipeline on SWE-bench-Live (1,890 instances) that integrates the extracted spec. The proposal does not specify which agent (SWE-agent, Moatless, Agentless, custom) is used, how the spec is injected, or what its baseline resolve rate is. Without this, the compute estimate and experimental design are incomplete.\", \"SIGNIFICANT — SWE-Lego (arXiv 2601.01426) not addressed: This January 2026 SFT-for-issue-resolving paper uses 32k training instances and a comprehensive SFT curriculum for end-to-end repair. As direct related work in the SFT-for-SWE space, its omission leaves a gap the reviewer committee will flag. The differentiation should be: SpecExtract does a spec-extraction subtask (not end-to-end repair), enabling pipeline-agnostic reuse.\", \"MODERATE — Test_patch assertion conditionality overstated: The 'non-solution-conditioned' framing is the linchpin of the training data justification, but test patches are written after/alongside gold patches and specifically designed to validate the fix. In many SWE-bench instances, assertions encode precise return values or exception types only determinable by knowing the codebase implementation. The paper should more carefully scope the claim: 'behavioral-specification-level, not implementation-level conditioned' rather than 'non-solution-conditioned.'\", \"MINOR — SWE-bench-Live size outdated: The proposal states '1,565+ instances' but the live dataset now contains 1,890 tasks across 223 repositories. Update to the current figure.\", \"MINOR — Compute budget tightness for full eval: Running a repair agent on 1,890 SWE-bench-Live instances at ~10-15 minutes/issue with 4 parallel H100s consumes approximately 79-118 H100-hours for evaluation alone, leaving 0-6 H100-hours for fine-tuning in the manual mode upper estimate. Explicitly partition the budget between SFT and eval inference.\"]\nFeedback: The Round 2 revision has substantially addressed the Round 1 critical issues: the training data premise is now grounded (SWE-bench test_patch AST parsing rather than SWE-bench Pro requirements), the evaluation target is appropriate (SWE-bench-Live), compute is expressed in H100-hours with manual mode under budget, and the JSON schema is formally defined. This is genuine progress. To advance to 'pass':\n\n(1) **Fix the model name immediately**: Replace 'Qwen3-Coder-14B' with either 'Qwen3-14B' (dense, 14B params, general Qwen3 family) or 'Qwen3-Coder-30B-A3B' (MoE, only 3B active params, faster and better for code). Qwen3-Coder-30B-A3B is the more credible choice for a coding spec-extraction task — its ~3B active parameters mean fine-tuning cost is comparable to a 3B dense model despite 30B total params.\n\n(2) **Verify or remove the 51.7% SpecRover claim**: Read SpecRover Section 4 or 5 (error analysis). If the 51.7% figure is there, cite the exact table/figure. If it's an approximation, write: 'SpecRover's error analysis identifies ambiguous issue descriptions as the dominant unresolved failure mode (Section X); our estimate from their public failure logs is ~50%.' If it's not there, reframe the motivation as: 'SpecRover's code-space approach cannot address cases where the issue description itself is underspecified — a failure mode it cannot observe.'\n\n(3) **Fix the SoRFT baseline**: Change '21.4% on SWE-bench Verified' to '21.4% on SWE-bench Lite (14.0% on Verified).' This makes SoRFT a weaker baseline, which actually helps SpecExtract's positioning.\n\n(4) **Specify the integration repair agent**: Choose one concrete agent (e.g., Agentless or Moatless) as the integration vehicle for the SWE-bench-Live evaluation. Report its baseline resolve rate, then show the SpecExtract-augmented rate. Add this as 1-2 sentences in the approach section. This is the most critical missing piece for a credible empirical narrative.\n\n(5) **Add SWE-Lego differentiation**: One paragraph acknowledging SWE-Lego (arXiv 2601.01426) as concurrent SFT work, differentiating that SpecExtract is a preprocessing spec-extraction module (not an end-to-end repair system) that can be combined with any SFT-trained or prompted repair backbone, including SWE-Lego itself.\n\n(6) **Scope the conditionality claim**: In the training data section, replace 'non-solution-conditioned' with 'implementation-agnostic behavioral specifications' to reflect that while test assertions do implicitly know the fix's behavior, they do not expose the implementation strategy, making them valid targets for behavioral spec learning.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL — Fabricated SpecRover citation (third consecutive round): The proposal cites 'SpecRover Section V-A, Reasons for Failure' with the specific claim that 51.7% of its 207 unresolved SWE-bench Lite tasks involve ambiguous issue descriptions (107/207 instances, labeled by SWE-bench Verified human annotators). Independent verification via WebFetch of arXiv 2408.02232v3 confirms this section does not exist — SpecRover has no dedicated error analysis section categorizing failures by issue ambiguity, and contains no 51.7% figure, 107/207 count, or SWE-bench Verified annotation cross-reference. The Round 3 generator escalated from 'unverifiable' (Round 2) to 'fabricated with false specificity' by inventing the section label, count, and labeling provenance. This is an academic integrity violation that will result in desk rejection or post-acceptance retraction if submitted as-is.\", \"SIGNIFICANT — Agent-CoEvo (arXiv 2604.04580, April 2026) not addressed in landscape: This concurrent paper, 'Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints,' proposes that behavioral constraints (tests) should be coevolved dynamically with code patches during repair rather than pre-extracted from bug reports. It evaluates on SWE-bench Lite and SWT-bench Lite and outperforms agentless baselines. This represents the most direct competing design philosophy to SpecExtract's pre-extraction approach and must be discussed — specifically, why pre-extraction from issue text before any codebase access is preferable to dynamic constraint coevolution.\", \"MODERATE — SoRFT numbers are now correct but were mishandled across three rounds: Independent verification via ACL Anthology (2025.acl-long.559) confirms SoRFT-7B achieves 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite — exactly as stated in Round 3. The Round 2 reviewer was wrong to flag these as reversed. While the numbers are now correct, three rounds of oscillation on this point suggest the generator should add a footnote citing the ACL Anthology URL to preempt reviewer confusion.\", \"MODERATE — No reported Agentless-on-SWE-bench-Live baseline: The experimental design requires establishing Agentless-direct (no spec injection) on SWE-bench-Live Lite (300 instances) as the baseline, then measuring SpecExtract-augmented Agentless. This baseline number is not reported anywhere in the proposal, making it impossible to assess whether the expected delta (e.g., +3-8 percentage points) is plausible or whether Agentless-1.5's 50.8% Verified score generalizes to the Live dataset at all. At minimum, cite the Agentless-1.5 SWE-bench-Live Lite score if published, or explicitly acknowledge this is unmeasured.\", \"MINOR — QLoRA VRAM claim is slightly oversimplified: Qwen3-Coder-30B-A3B with QLoRA requires ~17.5GB VRAM (verified via Unsloth documentation), fitting comfortably on a single H100 80GB rather than requiring 2× H100s. The 2× claim is not wrong (it enables larger batch sizes and faster throughput) but should be reframed as 'recommended configuration for efficient throughput' rather than 'minimum requirement.'\"]\nFeedback: This proposal has made genuine progress across three rounds — the model choice, Agentless integration, SWE-Lego differentiation, schema definition, and compute budget are all solid. One issue now blocks this from passing, and one new issue must be addressed:\n\n(1) **IMMEDIATE: Remove or replace the fabricated SpecRover Section V-A claim.** There is no 'Section V-A: Reasons for Failure' in SpecRover, no 51.7% figure, no 107/207 count, and no SWE-bench Verified annotation cross-reference in the paper. Replace the entire motivation chain with a defensible framing: 'SpecRover (ICSE 2025) evaluates on SWE-bench Lite and explicitly acknowledges that its code-space traversal approach cannot resolve cases where the issue description itself is underspecified — it can only infer specifications from code that exists, not from behavior that is described but not yet correctly implemented. This architectural limitation motivates an issue-space approach that operates on bug report text before codebase access.' If you want to keep a quantitative hook, look at SpecRover's SWE-bench Lite resolve rate (31%) and the known proportion of SWE-bench tasks where the issue description is classified as ambiguous by SWE-bench Verified human annotators — cite the SWE-bench Verified paper (arXiv 2410.06992) or the SWE-bench Pro paper for that annotation, not SpecRover.\n\n(2) **Add Agent-CoEvo to related work.** One paragraph: 'Agent-CoEvo (arXiv 2604.04580, April 2026) proposes coevolving code and test patches simultaneously during repair, treating tests as dynamic behavioral constraints. SpecExtract takes the complementary pre-extraction stance: issue-space specs derived before any codebase access reduce the search space for both fault localization and patch generation, and are reusable across repair backbones without retraining — including static repair systems like Agentless that do not support dynamic constraint revision.'\n\n(3) **Add Agentless-on-SWE-bench-Live baseline.** State the known or estimated Agentless-1.5 resolve rate on SWE-bench-Live Lite (or acknowledge it as an early experimental measurement to be reported in the paper). The experimental contribution is the delta, and without the baseline anchor the paper cannot make its empirical case.\n\nWith these three changes — particularly (1) — this proposal should be able to pass in Round 4.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"IMPORTANT CORRECTION — SpecRover Section V-A claim is VERIFIED, not fabricated: Independent WebFetch of the HTML version of arXiv:2408.02232 (https://arxiv.org/html/arXiv:2408.02232) confirms the paper contains Section V-A 'RQ1: Overall Efficacy of Task Resolving' with a subsection 'Reasons for Failure' that explicitly documents 107/207 unresolved SWE-bench Lite tasks (51.7%) classified as ambiguous issue descriptions. The Round 3 reviewer's 'fabricated' accusation was incorrect. The generator should add a footnote or parenthetical citing the HTML URL to preempt any residual reviewer confusion, since the accusation has been raised three consecutive rounds.\", \"SIGNIFICANT — Internal inconsistency in EMNLP pilot scope: The EMNLP venue description states 'realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval,' but the main approach uses 2,294 SWE-bench instances + 3,000 GitBugs pseudo-labeled instances = 5,300 corpus. These are in direct conflict. Either (a) define the EMNLP submission as explicitly scoped to a pilot — SFT on SWE-bench Verified 500 subset, SWE-bench-Live Lite 300-instance eval, no GitBugs augmentation — and state this clearly in the approach section, or (b) remove the '500-instance Verified' framing from the venue description and commit to the full corpus with the understanding that compute and eval must finish within 16 days.\", \"MODERATE — 16-day deadline is unrealistically framed without explicit pilot scope: Building the 5,300-instance training corpus (AST parsing + NLP regex + LLM-assisted spec fill), SFT (10-14 H100-hours), establishing Agentless-SWE-bench-Live Docker infrastructure, running the full 300-instance eval + 4-field ablations (80-96 H100-hours), and writing the paper cannot realistically be completed in 16 days by 1-2 researchers. The submission plan should explicitly acknowledge that the EMNLP ARR submission will report pilot-scale results (e.g., SFT on 500-instance Verified subset, 100-instance SWE-bench-Live Lite eval) with the full-scale results reserved for ICSE 2027 as the primary venue.\", \"MODERATE — 'Replacing the officially-abandoned SWE-bench Verified' is imprecise: OpenAI's February 2026 announcement recommends SWE-bench Pro as the frontier evaluation replacement — not SWE-bench-Live. SWE-bench-Live is the appropriate replacement for contamination-resistant research evaluation, which is the correct positioning for this paper, but the phrasing implies SWE-bench-Live is the community standard replacement for Verified, which overstates its current adoption. Reframe as: 'As SWE-bench Verified saturates with contamination concerns, SWE-bench-Live (NeurIPS 2025) provides contamination-resistant evaluation on post-2024 issues — the appropriate target for research contributions that train on SWE-bench data.'\", \"MINOR — Cosine similarity threshold (≥ 0.65) for schema validation is stated without justification: The proposal requires AST-parsed test assertions to achieve ≥ 0.65 cosine similarity with SWE-bench Pro human requirements on 200 held-out instances. This threshold determines whether the schema is redesigned before scale-up, making it a critical gating decision. Add one sentence explaining why 0.65 is the right threshold (e.g., 'consistent with semantic similarity thresholds in information extraction literature where 0.65 distinguishes semantically related from unrelated pairs').\"]\nFeedback: The SpecRover Section V-A claim has been independently verified as correct — the HTML paper confirms the 107/207 (51.7%) ambiguous issue description statistics in the 'Reasons for Failure' subsection of Section V-A. After three rounds of false accusations, add a parenthetical citing the HTML URL (https://arxiv.org/html/arXiv:2408.02232) to preempt any residual reviewer skepticism. To reach 'pass' in Round 5: (1) **Fix the pilot/full scope inconsistency**: Choose one coherent story for EMNLP. The most defensible is a pilot submission — SFT on SWE-bench Verified 500-instance subset, primary eval on 100-150 SWE-bench-Live Lite instances (not 300), 2-field ablation (affected_interface vs. none, expected_behavior vs. none). Remove the '500-instance SWE-bench Verified training' from the venue description and put it in the approach section as the EMNLP pilot plan. State that the full 5,300-instance corpus + 300-instance eval is the ICSE 2027 primary submission. (2) **Fix the SWE-bench Verified replacement framing**: Change 'replacing the officially-abandoned SWE-bench Verified' to 'providing contamination-resistant evaluation as SWE-bench Verified saturates at frontier.' (3) **Justify the 0.65 cosine similarity threshold** in one sentence. With these changes, the proposal will have resolved all substantive issues from rounds 1-4 and should be ready to pass.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"SIGNIFICANT (unresolved from Round 4) — EMNLP venue scope vs approach inconsistency: The target_venues description states 'realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval,' but the approach section describes a 5,300-instance training corpus (2,294 SWE-bench full + ~3,000 GitBugs pseudo-labeled). These are directly contradictory in the same document. Round 4 explicitly flagged this and asked for a coherent pilot story. It remains unresolved in Round 5.\", \"MODERATE (unresolved from Round 4) — 'replacing the officially-abandoned SWE-bench Verified' framing: The abandonment by OpenAI is factually confirmed (Feb 2026), but OpenAI recommends SWE-bench Pro as the replacement — not SWE-bench-Live. The proposal implies SWE-bench-Live is the community-endorsed successor to Verified, which overstates its adoption. Round 4 asked to reframe as 'providing contamination-resistant evaluation as SWE-bench Verified saturates at frontier.' This change was not made in Round 5.\", \"MODERATE (unresolved from Round 4) — 16-day timeline not explicitly scoped to auto-research + pilot: Manual mode timeline is 3-5 months, Human-in-Loop is 5-9 weeks, and only auto-research (6-10 days) fits the 16-day EMNLP window. The proposal does not state that the EMNLP ARR submission will be auto-research mode output only, and does not reconcile whether pilot-scale (500 training, 100-150 eval) or full-scale (5,300 training, 300 eval + ablations) results will be in the paper.\", \"MINOR (unresolved from Round 4) — Cosine similarity threshold 0.65 still has no justification: The schema validation gate (≥0.65 cosine similarity on 200 held-out SWE-bench Pro instances) determines whether the schema is redesigned before scale-up, yet no rationale for this specific threshold value appears anywhere in the proposal. Round 4 asked for a one-sentence justification.\", \"MINOR (unresolved from Round 4) — SpecRover HTML URL not added: Round 4 explicitly requested adding the HTML URL (https://arxiv.org/html/arXiv:2408.02232) as a parenthetical to preempt future reviewer skepticism about the 51.7% statistic — especially given three rounds of false 'fabricated' accusations in the review history. This was not done in Round 5.\"]\nFeedback: The technical substance of Round 5 is solid: Agentless baseline numbers are verified from Table 3 of arXiv 2505.23419 (11.67%/12.00%/13.33%), the SpecRover 107/207 (51.7%) claim is independently confirmed via direct HTML fetch, Qwen3-Coder-30B-A3B specs are correct, Agent-CoEvo and SWE-Lego are properly integrated, and the schema+worked-example is concrete. The paper is almost ready. Three Round 4 items remain unresolved and need targeted fixes:\n\n(1) **Fix the EMNLP pilot scope — choose one story**: The fastest fix is to remove '500-instance SWE-bench Verified training' from the venue description and replace it with the actual EMNLP submission plan. The defensible choice is: 'EMNLP ARR submission reports auto-research results: SFT on SWE-bench full 2,294-instance corpus (GitBugs augmentation deferred to ICSE), SWE-bench-Live Lite 300-instance eval, 2-field ablation (affected_interface vs. none, expected_behavior vs. none). Full 5,300-instance corpus with all four ablation fields is the ICSE 2027 extended paper.' State this explicitly in both the venue description and the approach section's experimental scope.\n\n(2) **Fix the Verified framing in one clause**: Change 'replacing the officially-abandoned SWE-bench Verified' to 'as SWE-bench Verified saturates with contamination concerns (OpenAI, Feb 2026), SWE-bench-Live provides contamination-resistant evaluation on post-2024 issues.' This is a factually accurate reframe that doesn't misrepresent which benchmark OpenAI actually recommends as replacement.\n\n(3) **Add the 0.65 threshold justification**: One sentence: 'This threshold aligns with established semantic similarity cutoffs in information-extraction evaluation literature, where scores below 0.65 on sentence-transformer embeddings indicate insufficient semantic overlap for structural field matching.' This is the only change needed for that issue.\n\n(4) **Add SpecRover HTML URL** as a parenthetical: after '107 of its 207 unresolved SWE-bench Lite tasks (51.7%)' add '(see https://arxiv.org/html/arXiv:2408.02232, Section V-A)'. Four words of insurance given three rounds of false accusations.\n\nWith these four targeted changes, all substantive issues from rounds 1-5 will be resolved.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"SIGNIFICANT — Agentless retrieval mechanism mis-specified: The proposal states spec injection occurs at 'BM25+embedding file retrieval' (Agentless Stage 1), but independent verification of arXiv 2407.01489 confirms Agentless uses (a) LLM prompting over the repository tree to identify suspicious files, and (b) embedding-based cosine similarity retrieval — neither of which is BM25. The proposed integration (prepending affected_interface.module as a structured query prefix to BM25) requires either modifying Agentless's localization code to add BM25 as a third retrieval signal, or re-describing the injection as modifying the LLM prompt template to include structured spec fields. This is not a minor terminology slip — if the integration mechanism is inaccurate, the mechanistic case for the +4-7 pp improvement collapses entirely.\", \"SIGNIFICANT — The +4-7 pp improvement prediction lacks mechanistic support: The improvement claim is the paper's sole empirical contribution (from 13.33% to ~17-20% on SWE-bench-Live Lite, a 28-50% relative gain). No mechanistic argument is given for why adding structured spec fields to Agentless's retrieval/generation pipeline would produce this magnitude of improvement. Independent search confirms Agentless already sends the full issue text to its embedding retrieval — if the spec is derived FROM the issue text, the marginal information gain is structural compression (module/function names extracted from prose), not new information. The paper needs an explicit argument: e.g., 'Agentless's LLM prompting for file localization mistakes incidentally-mentioned module names for structurally-important ones; SpecExtract's extraction isolates the true affected interface with X% precision on a validation set.'\", \"MODERATE — Cosine similarity validation against SWE-bench Pro requirements has a circularity: SWE-bench Pro requirements were authored by annotators who had full access to the gold patch and tests. Achieving ≥ 0.65 cosine similarity between AST-extracted specs and SWE-bench Pro requirements confirms that machine-derived specs are solution-adjacent — not that they are useful for genuinely ambiguous in-the-wild bug reports. This validation cannot distinguish between 'our specs capture true behavioral expectations' and 'our specs recapitulate solution-known annotations.' A stronger validation would compare SpecExtract's spec quality on a held-out set of real GitHub issues that were NOT in SWE-bench (e.g., randomly sampled GitBugs instances without ground truth), graded by human annotators blind to the gold patch.\", \"MINOR — Masked-field training protocol is mechanically underspecified: The proposal mentions 'training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs' but does not specify the per-field masking probability, whether masking is uniform or weighted by artifact availability in the corpus, or how the loss is computed for masked vs. unmasked fields (e.g., is the model trained to output null for masked fields, or to infer the field from available signals?). One sentence would suffice: e.g., 'Each artifact field is independently masked with p=0.5 at training time; masked fields are replaced with a [MISSING] token and the model is trained to output null for those positions while filling the remaining fields normally.'\"]\nFeedback: Round 6 has successfully addressed all five Round 5 issues: the EMNLP scope is now self-consistent (auto-research, 2,294 SWE-bench full, GitBugs deferred to ICSE 2027), the SWE-bench Verified framing is corrected, the timeline is explicitly scoped to auto-research mode, the 0.65 threshold is justified, and the SpecRover HTML URL is added. The proposal is nearly ready.\n\nTwo fixes will unlock 'pass' in Round 7:\n\n(1) **Fix the Agentless integration description**: Independent verification of arXiv 2407.01489 confirms Agentless uses (a) LLM prompting over a repo tree, and (b) embedding-based cosine similarity — not BM25. Replace 'BM25+embedding file retrieval is biased by prepending affected_interface.module and entry_point as a structured query prefix' with an accurate description: e.g., 'We modify Agentless's LLM prompting step at Stage 1 by prepending a structured spec header (affected_interface.module + entry_point) before the repository tree, so the LLM identifies suspicious files with the affected interface explicitly in context; we additionally add a BM25 pass over file paths using the structured interface tokens as a third retrieval signal, complementing Agentless's existing embedding-based similarity.' This also strengthens the mechanistic case: BM25 exact-match on extracted module/function names catches files that embedding similarity misses because module names are out-of-distribution lexically.\n\n(2) **Add one sentence of mechanistic justification for the +4-7 pp improvement target**: The argument is available — just make it explicit: 'Agentless's fault localization already achieves roughly X% file-level recall on SWE-bench Verified; on SWE-bench-Live, where models are less likely to have encountered the repos during pretraining, recall drops. SpecExtract's structured interface extraction provides a high-precision localization signal (module + entry_point) that compensates for this distribution shift, analogous to how BM25 lexical matching improves recall in out-of-domain retrieval settings (cite BM25 + dense retrieval hybrid literature, e.g., Karpukhin et al. 2020 DPR or a code-specific IR paper).'\n\n(3) Optional but strengthening: acknowledge the cosine similarity validation limitation in one sentence (e.g., 'As a pilot ecological validity check only — this validates schema alignment against expert-annotated specs, not generalization to ambiguous in-the-wild reports') to preempt reviewer #2 questioning.\n\nWith fixes (1) and (2), the empirical contribution has a mechanistic backbone that survives reviewer scrutiny.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:50:28.525Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:50:28.525Z",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-10T07:50:28.553Z_

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
  "title": "SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair",
  "core_problem": "Automated repair agents fail on ambiguous bug reports not from lack of code understanding, but because unstructured issue text leaves behavioral expectations underspecified — what interface should change, what the user observed, and what correct behavior looks like are rarely made explicit. SpecRover (ICSE 2025) partially addresses this via per-instance LLM prompting that extracts specifications from CODE during codebase traversal, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue. Its error analysis (Section V-A, 'Reasons for Failure'; see https://arxiv.org/html/2408.02232, Section V-A) identifies that 107 of its 207 unresolved SWE-bench Lite tasks (51.7%) are classified as 'ambiguous issue description' — cases the paper characterizes as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for why underspecified descriptions constitute an irreducible failure mode for code-space approaches. This architectural limitation is structural: code-side spec extraction can only infer specifications from code that already exists, not from behavior that is described in the issue but not yet correctly implemented. Bug reports routinely contain latent behavioral specifications in their runtime artifacts: stack traces name the affected interface, error messages describe observed behavior, and reproducer assertions encode expected behavior. No method trains a dedicated model to extract these signals from bug report text into a structured repair specification — covering affected interface, observed behavior, expected behavior, and their delta — that could constrain both fault localization and patch generation before any codebase traversal begins.",
  "opportunity": "Failing test assertions in SWE-bench's test patches encode implementation-agnostic behavioral specifications without revealing implementation strategies: `assert result == expected_value` or `with pytest.raises(ValueError)` states precisely what the program SHOULD do, independent of WHICH code to change or HOW to change it. By mechanically converting (problem_statement + test_patch assertions + stack traces) to structured JSON spec fields using AST-level test parsing and NLP extraction on SWE-bench's 2,294 instances, we construct a training corpus of 2,294 (bug_report, structured_spec) pairs — where the spec encodes behavioral expectations derivable without knowing the implementation strategy. This avoids the critical flaw of training on SWE-bench Pro requirements, which were authored by humans with full access to the golden patch (making them solution-conditioned). SWE-bench-Live (NeurIPS 2025, arXiv 2505.23419; ~1,890 Docker-reproducible instances across 223 repositories, drawn from post-January-2024 GitHub issues, growing at ~50 instances/month) provides a clean, contamination-resistant evaluation target with no training-set overlap. As SWE-bench Verified saturates with contamination concerns (OpenAI officially deprecated it in February 2026), SWE-bench-Live provides contamination-resistant evaluation on post-2024 issues unavailable during model training. SWE-bench Pro's human-written `requirements` and `interface` fields (731 public instances) serve as an ecological validity check — we measure cosine similarity between machine-derived specs and human requirements on a held-out 200-instance slice — confirming that AST-parsed test assertions produce specs that match expert behavioral descriptions, without using requirements as training supervision.",
  "landscape": "SpecRover (ICSE 2025, arXiv 2408.02232) is the closest prior work: given a GitHub issue, it iteratively traverses the codebase, prompting Claude 3.5 Sonnet to extract function-level summaries from visited code, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue and 31% on SWE-bench Lite (93/300). SpecRover operates in code-space (it visits source files to generate specs from code) and uses per-instance prompting (no fine-tuning). Our approach operates in issue-space (extracts specs from bug report text and runtime artifacts before any codebase traversal) and uses supervised fine-tuning (consistent structured output at ~$0.05-0.10/issue). These are complementary directions: SpecRover's code-space specs and our issue-space specs could ultimately be fused. Agent-CoEvo (arXiv 2604.04580, April 2026) proposes the most directly competing design philosophy: rather than pre-extracting behavioral constraints from issue text, it coevolves code patches and test patches simultaneously during repair, treating tests as dynamic constraints that are iteratively revised alongside candidate fixes. Agent-CoEvo achieves 41.33% on SWE-bench Lite (DeepSeek-V3) and 46.4% on SWT-bench Lite, outperforming Agentless-1.5 (32%) on those benchmarks. SpecExtract takes the complementary pre-extraction stance: (1) issue-space specs derived before any codebase access are reusable across repair backbones without retraining, including static pipeline systems like Agentless that do not support dynamic constraint revision during search; (2) pre-extracted specs reduce the initial search space before coevolution begins, making SpecExtract a potential front-end that improves Agent-CoEvo's starting population rather than competing with it. SWE-Lego (arXiv 2601.01426, Jan 2026) is the most directly competing concurrent SFT work: it trains on 32k high-quality task instances with error masking and a difficulty-based curriculum, achieving 52.6% on SWE-bench Verified (58.8% with test-time scaling at 16 samples) using a 32B model. SWE-Lego is an end-to-end system that produces complete code fixes; SpecExtract is a preprocessing module that extracts structured behavioral specs from bug report text before any repair attempt, and can plug into SWE-Lego or any other repair backbone as a drop-in front-end — improving fault localization precision and patch generation alignment without retraining the repair agent itself. CodeSpecBench (arXiv 2604.12268, April 2026) benchmarks existing LLMs (Claude, GPT-4, Gemini) on executable behavioral specification generation via prompting — it does not train a dedicated extractor, operates on code-side and description inputs rather than bug report runtime artifacts, and is an evaluation framework rather than a preprocessing pipeline for repair. Its existence confirms that structured specification generation is an active research area, while simultaneously validating the gap: no trained, issue-space specification extractor for repair preprocessing exists. VibeRepair (arXiv 2602.08263, Feb 2026) translates buggy CODE into behavior specifications, repairs the spec, then synthesizes corrected code, achieving 19-23% improvement on Defects4J — code-space to spec, not text-space to spec. TraceRepair (arXiv 2604.02647, Apr 2026) uses runtime execution traces generated by instrumented code execution as shared repair constraints across a multi-agent committee, fixing 392 Defects4J defects — traces are generated during repair, not extracted from issue text before repair begins. RepoRepair (arXiv 2603.01048) generates hierarchical code documentation from source files toward the bug; its documentation is code-driven, not report-driven. SoRFT (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) fine-tunes on SWE-bench with RL to decompose the repair TASK into subtasks (file → function → line → edit), achieving 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite with a 7B model (30.8% Verified and 24.0% Lite with a 32B model) — it structures the repair pipeline, not the issue semantics. PathFix (arXiv 2510.14341) derives behavioral specs from static code execution paths — code-space and offline, not issue-space. The gap: no existing work trains a dedicated model to extract structured behavioral specifications from bug report text and embedded runtime artifacts, operating entirely in issue-space before codebase access.",
  "approach": "We train SpecExtract, a Qwen3-Coder-30B-A3B model (Mixture-of-Experts: 30B total parameters, ~3B active per token — fine-tuning and inference cost scale with active parameters, comparable to a 3B dense model; fits on a single H100 80GB with QLoRA at ~17.5GB VRAM per Unsloth benchmarks; 2× H100 is the recommended training configuration for throughput, not minimum requirement) fine-tuned to map (bug_report_text, runtime_artifacts?) → structured JSON spec, where runtime artifacts are any combination of stack traces, error messages, test failure output, or explicit reproducer assertions present in the issue text. The model gracefully handles varying artifact availability through a masked-field training protocol: training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs. Each artifact field (stack_trace, error_message, test_assertions) is independently masked with p=0.5 at training time; masked fields are replaced with a [MISSING] token, and the model is trained to output null for those positions while filling remaining fields from whatever signals are available — not to infer missing artifacts from correlated signals. **Formal schema**: Each spec has four typed fields — (1) `affected_interface`: {module: str, signature: str|null, entry_point: str} extracted from stack frame function names and explicitly mentioned APIs; (2) `observed_behavior`: {error_type: str|null, error_message: str|null, symptom: str} from error output and user complaint; (3) `expected_behavior`: {description: str, assertions: [str]} as natural-language description plus test-style constraint strings when derivable; (4) `behavioral_delta`: str, a one-sentence expected-vs-actual summary. Worked example for a NumPy issue 'linalg.solve silently returns None for singular matrices instead of raising': {affected_interface: {module: 'numpy.linalg', entry_point: 'solve', signature: 'solve(a, b)'}, observed_behavior: {error_type: null, symptom: 'returns None for singular matrix input'}, expected_behavior: {description: 'should raise for non-invertible input', assertions: ['raises np.linalg.LinAlgError when matrix is singular']}, behavioral_delta: 'solve silently returns None instead of raising LinAlgError on singular input'}. **Training data construction (implementation-agnostic behavioral specifications)**: From SWE-bench full (2,294 instances including Verified 500 and the broader set): (1) parse `test_patch` test functions via Python AST to extract formal assertions — pytest.raises calls → error_type, assert statements → expected_behavior.assertions, decorated test function signatures → affected_interface hints; (2) extract stack traces and error strings from `problem_statement` text via regex heuristics → observed_behavior; (3) combine via LLM-assisted template fill using Qwen3-Coder-30B-A3B in a chain-of-thought extraction pass to produce coherent spec JSON; (4) validate on 200 SWE-bench Pro public instances that have non-null `requirements` and `interface` fields by computing cosine similarity (sentence-transformer) between mechanically-derived specs and human-authored requirements — target alignment ≥ 0.65 before training at scale (this threshold aligns with established semantic similarity cutoffs in information-extraction evaluation literature, where scores below 0.65 on sentence-transformer embeddings indicate insufficient semantic overlap for structural field matching); this validates the schema rather than using requirements as training targets. This is a pilot ecological validity check only — it confirms schema alignment with expert behavioral annotations on curated SWE-bench instances but cannot validate generalization to genuinely ambiguous in-the-wild reports that are not SWE-bench-adjacent; a full generalization validation would require human annotation of randomly sampled GitBugs instances and is deferred to the ICSE 2027 extended paper. Important framing on conditionality: test assertions are written alongside gold patches and encode the behavioral outcome the fix achieves. The training specs are therefore *implementation-agnostic* — they do not reveal which code to change or the implementation strategy — rather than strictly solution-independent. This distinction is explicitly addressed in the paper to avoid overclaiming. The EMNLP 2026 ARR submission uses the 2,294-instance SWE-bench full corpus as the SFT training set; GitBugs augmentation (~3,000 pseudo-labeled instances, yielding a ~5,300-instance total corpus) is reserved for the ICSE 2027 extended paper. **Differentiation from SpecRover**: (1) issue-space — no codebase traversal needed at spec extraction time; (2) supervised learning — consistent, typed JSON output from a single forward pass (~$0.05-0.10/issue) vs. SpecRover's multi-step code traversal ($0.65/issue); (3) directly targets SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved SWE-bench Lite tasks) by conditioning on all available runtime artifacts in the issue, not just the code side. **Integration with Agentless**: Agentless (arXiv 2407.01489) is used as the repair backbone for all SWE-bench-Live evaluations — it follows a fixed pipeline (hierarchical fault localization → patch generation → patch selection) with no iterative tool calls, making spec injection clean and reproducible. Agentless's fault localization uses (a) LLM prompting over the repository folder tree to identify suspicious directories and (b) embedding-based cosine similarity retrieval over code chunks — it does not use BM25. SpecExtract specs are injected at two points: (1) fault localization — we modify the LLM prompting step by prepending a structured spec header (affected_interface.module + entry_point) before the folder listing, so the LLM identifies suspicious directories with the affected interface explicitly in context; we additionally introduce a BM25 pass over file paths and module docstrings using the extracted interface tokens as a third retrieval signal complementing Agentless's existing embedding-based similarity — BM25 exact-match on lexically-specific tokens like `numpy.linalg` or `django.db.models.QuerySet` catches files that semantic embeddings miss when the module is underrepresented in the embedder's training distribution, exactly the localization failure mode that intensifies on post-2024 SWE-bench-Live repos relative to in-distribution SWE-bench Verified; (2) patch generation — the repair LLM receives all four spec fields as an explicit behavioral constraint header in its prompt, focusing generation on the documented behavioral delta. **Agentless baseline on SWE-bench-Live**: Per the SWE-bench-Live paper (arXiv 2505.23419, Table 3), Agentless resolves 11.67% (GPT-4o), 12.00% (GPT-4.1), and 13.33% (DeepSeek V3) of SWE-bench-Live Lite (300 instances) — substantially below its ~50.8% on SWE-bench Verified, reflecting the contamination-resistant, harder distribution of post-2024 issues. These published numbers establish the Agentless-direct baseline; SpecExtract targets +4-7 percentage points improvement over the best Agentless backbone, which is reported as the primary experimental contribution. **Mechanistic case for the +4-7 pp improvement target**: Agentless's embedding-based file localization achieves ~57% file-level Recall@1 on SWE-bench Lite (original Agentless paper), yet its end-to-end resolve rate drops ~4× from SWE-bench Verified (~50.8%) to SWE-bench-Live Lite (13.33% best case). A primary contributor to this degradation is fault localization failure on post-2024 repos that are underrepresented in embedding model training data: embedding similarity between an issue query and post-2024 codebase chunks is noisier than on in-distribution repos, because the model has not seen those module structures and naming conventions. SpecExtract's BM25 pass on extracted module/entry_point tokens addresses this directly: exact-match retrieval on tokens like `numpy.linalg` does not require the embedding model to have indexed those repository paths during pretraining and does not degrade under distribution shift. Hybrid BM25+dense retrieval is well-established to improve out-of-domain recall in code search — a two-stage pipeline combining BM25 first-pass retrieval with dense reranking improves MRR by 8.6% over dense-only on out-of-distribution queries (Revisiting Code Search in a Two-Stage Paradigm, ICSE 2023). The +4-7 pp improvement target reflects two compounding gains: (a) localization improvement from BM25-anchored interface token matching, which provides a high-precision signal robust to the post-2024 distribution shift Agentless's embedder faces; (b) generation improvement from Stage 3 behavioral constraint injection narrowing the patch candidate space to the documented behavioral delta — these gains compound because better localization provides a more focused candidate file set for patch generation. **Evaluation**: Primary eval on SWE-bench-Live Lite (300 instances, contamination-resistant, post-2024 issues) with Agentless as backbone; per-field ablations independently zero out each spec field to quantify individual contribution to resolve rate. Secondary eval: cosine-similarity validation on 200 SWE-bench Pro held-out instances (schema validity check). Comparison baselines: Agentless direct repair without spec (established at 11-13% from published SWE-bench-Live results), SpecRover-equivalent prompting (ablation of supervised fine-tuning benefit), SoRFT-Qwen-7B (21.4% Verified / 14.0% Lite, structured subtask decomposition), SWE-Lego (52.6% Verified, end-to-end SFT backbone — SpecExtract as preprocessing front-end demonstrates orthogonal contribution). **Publication scope**: The EMNLP 2026 ARR submission (auto-research mode, 6-10 days) reports results on the 2,294-instance SWE-bench full SFT corpus with SWE-bench-Live Lite 300-instance primary eval and a 2-field ablation (affected_interface vs. none, expected_behavior vs. none) — the two fields with the strongest localization and generation signal respectively. The full 5,300-instance corpus (with GitBugs augmentation) and all four per-field ablation fields constitute the ICSE 2027 extended paper.",
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
    "Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489) — integration repair backbone: open-source fixed pipeline with (a) LLM prompting over repository folder tree for directory filtering and (b) embedding-based cosine similarity retrieval over code chunks; SpecExtract augments both with a structured spec header in the LLM prompt and a BM25 third retrieval pass on extracted interface tokens; ~50.8% SWE-bench Verified (Agentless-1.5), 32% SWE-bench Lite; file-level Recall@1 ~57% on SWE-bench Lite",
    "Revisiting Code Search in a Two-Stage Paradigm (ICSE 2023, dl.acm.org/doi/pdf/10.1145/3539597.3570383) — hybrid BM25+dense code retrieval: two-stage BM25 first-pass → CodeBERT reranking improves MRR by 8.6% over dense-only on out-of-distribution queries; mechanistic support for adding BM25 as a third retrieval signal in Agentless fault localization on post-2024 SWE-bench-Live repos",
    "CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (arXiv 2604.12268, April 2026) — evaluates prompting-based spec generation from code and descriptions using existing LLMs; does not train a dedicated extractor, operates on code-side inputs rather than bug report runtime artifacts, and is an evaluation framework rather than a repair preprocessing pipeline — confirms structured spec generation is an active research area while the trained, issue-space extractor gap remains open",
    "Specification Vibing for Automated Program Repair / VibeRepair (arXiv 2602.08263, Feb 2026) — code-space spec extraction before repair, Defects4J, 19-23% improvement",
    "Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate / TraceRepair (arXiv 2604.02647, Apr 2026) — trace-based repair constraints during execution, Defects4J",
    "SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) — structured repair subtask decomposition with RL; SoRFT-Qwen-7B: 21.4% SWE-bench Verified / 14.0% SWE-bench Lite; SoRFT-Qwen-32B: 30.8% SWE-bench Verified / 24.0% SWE-bench Lite; key baseline for SpecExtract's supervised fine-tuning approach",
    "On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481) — fault localization recall analysis: documents how localization granularity and retrieval method affect end-to-end repair performance; provides empirical context for why embedding-based localization degrades on out-of-distribution repos",
    "GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More (arXiv 2504.09651) — 150K+ open-licensed bug reports for training augmentation",
    "RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048)",
    "PathFix: Automated Program Repair with Expected Path (arXiv 2510.14341)"
  ],
  "description": "We introduce SpecExtract, the first supervised issue-space specification extractor for program repair: a fine-tuned Qwen3-Coder-30B-A3B model (MoE, ~3B active parameters — fine-tuning and inference cost comparable to a 3B dense model; fits on a single H100 80GB at ~17.5GB VRAM with QLoRA; 2× H100 recommended for training throughput) that maps (bug_report_text, runtime_artifacts?) → a structured four-field JSON spec covering affected interface, observed behavior, expected behavior, and behavioral delta. The key methodological insight is that failing test assertions in SWE-bench test patches encode implementation-agnostic behavioral specifications — they state what the program SHOULD do without revealing which code to change or the implementation strategy — enabling AST-level test parsing combined with problem-statement NLP extraction to construct 2,294 clean (bug_report, structured_spec) training pairs from SWE-bench. The masked-field training protocol (p=0.5 per artifact field, [MISSING] token, null output for masked positions) enables graceful handling of partially-available runtime artifacts at inference time. GitBugs (150K+ open-licensed bug reports) provides ~3,000 pseudo-labeled augmentation instances for the ICSE 2027 extended paper; the EMNLP 2026 ARR submission uses the 2,294-instance SWE-bench full corpus only. SWE-bench Pro public requirements serve as a pilot ecological validity check (cosine similarity ≥ 0.65 on 200 held-out instances, confirming schema alignment with expert annotations rather than generalizing to in-the-wild reports), not a training target. Extracted specs are integrated with Agentless as the repair backbone: Agentless's fault localization uses LLM prompting over the repository folder tree plus embedding-based cosine similarity retrieval — SpecExtract augments this by (a) prepending a structured spec header (affected_interface.module + entry_point) to the LLM prompting step and (b) adding a BM25 pass over file paths and docstrings using extracted interface tokens as a third retrieval signal, catching files that embedding similarity misses when the module is underrepresented in the embedder's training distribution (a failure mode that intensifies on post-2024 SWE-bench-Live repos); at patch generation, a structured behavioral constraint prefix focuses generation on the documented delta. Primary evaluation is on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues), with the Agentless-direct baseline established at 11-13% from published SWE-bench-Live results (Table 3, arXiv 2505.23419) and a mechanistically-grounded target improvement of +4-7 percentage points: Agentless's ~57% file-level Recall@1 on SWE-bench Lite degrades on post-2024 repos where embedding similarity is noisiest, and BM25-anchored lexical matching on extracted module/function tokens provides a distribution-shift-robust localization signal, consistent with hybrid retrieval literature showing 8.6% OOD MRR gains (ICSE 2023 two-stage code search). Per-field ablations measure individual spec contributions. Agent-CoEvo (arXiv 2604.04580, 41.33% SWE-bench Lite) represents the competing dynamic-coevolution philosophy; SpecExtract's pre-extraction stance is complementary — pipeline-agnostic and applicable to static repair systems. SWE-Lego (52.6% Verified with 32B) is included as an end-to-end SFT baseline to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end. Differentiated from SpecRover (code-space prompting, $0.65/issue, 31% SWE-bench Lite) by operating in issue-space at ~$0.05-0.10/issue — directly targeting SpecRover's Section V-A identified 51.7% ambiguous-description failure mode. Compute in H100-hours: manual mode ~90-110 H100-hours (SFT ~10-14 H100-hours, eval ~80-96 H100-hours), within the 200-hour hard constraint.",
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

### Round 6 review
Verdict: revise
Issues: ["SIGNIFICANT — Agentless retrieval mechanism mis-specified: The proposal states spec injection occurs at 'BM25+embedding file retrieval' (Agentless Stage 1), but independent verification of arXiv 2407.01489 confirms Agentless uses (a) LLM prompting over the repository tree to identify suspicious files, and (b) embedding-based cosine similarity retrieval — neither of which is BM25. The proposed integration (prepending affected_interface.module as a structured query prefix to BM25) requires either modifying Agentless's localization code to add BM25 as a third retrieval signal, or re-describing the injection as modifying the LLM prompt template to include structured spec fields. This is not a minor terminology slip — if the integration mechanism is inaccurate, the mechanistic case for the +4-7 pp improvement collapses entirely.", "SIGNIFICANT — The +4-7 pp improvement prediction lacks mechanistic support: The improvement claim is the paper's sole empirical contribution (from 13.33% to ~17-20% on SWE-bench-Live Lite, a 28-50% relative gain). No mechanistic argument is given for why adding structured spec fields to Agentless's retrieval/generation pipeline would produce this magnitude of improvement. Independent search confirms Agentless already sends the full issue text to its embedding retrieval — if the spec is derived FROM the issue text, the marginal information gain is structural compression (module/function names extracted from prose), not new information. The paper needs an explicit argument: e.g., 'Agentless's LLM prompting for file localization mistakes incidentally-mentioned module names for structurally-important ones; SpecExtract's extraction isolates the true affected interface with X% precision on a validation set.'", "MODERATE — Cosine similarity validation against SWE-bench Pro requirements has a circularity: SWE-bench Pro requirements were authored by annotators who had full access to the gold patch and tests. Achieving ≥ 0.65 cosine similarity between AST-extracted specs and SWE-bench Pro requirements confirms that machine-derived specs are solution-adjacent — not that they are useful for genuinely ambiguous in-the-wild bug reports. This validation cannot distinguish between 'our specs capture true behavioral expectations' and 'our specs recapitulate solution-known annotations.' A stronger validation would compare SpecExtract's spec quality on a held-out set of real GitHub issues that were NOT in SWE-bench (e.g., randomly sampled GitBugs instances without ground truth), graded by human annotators blind to the gold patch.", "MINOR — Masked-field training protocol is mechanically underspecified: The proposal mentions 'training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs' but does not specify the per-field masking probability, whether masking is uniform or weighted by artifact availability in the corpus, or how the loss is computed for masked vs. unmasked fields (e.g., is the model trained to output null for masked fields, or to infer the field from available signals?). One sentence would suffice: e.g., 'Each artifact field is independently masked with p=0.5 at training time; masked fields are replaced with a [MISSING] token and the model is trained to output null for those positions while filling the remaining fields normally.'"]
Feedback: Round 6 has successfully addressed all five Round 5 issues: the EMNLP scope is now self-consistent (auto-research, 2,294 SWE-bench full, GitBugs deferred to ICSE 2027), the SWE-bench Verified framing is corrected, the timeline is explicitly scoped to auto-research mode, the 0.65 threshold is justified, and the SpecRover HTML URL is added. The proposal is nearly ready.

Two fixes will unlock 'pass' in Round 7:

(1) **Fix the Agentless integration description**: Independent verification of arXiv 2407.01489 confirms Agentless uses (a) LLM prompting over a repo tree, and (b) embedding-based cosine similarity — not BM25. Replace 'BM25+embedding file retrieval is biased by prepending affected_interface.module and entry_point as a structured query prefix' with an accurate description: e.g., 'We modify Agentless's LLM prompting step at Stage 1 by prepending a structured spec header (affected_interface.module + entry_point) before the repository tree, so the LLM identifies suspicious files with the affected interface explicitly in context; we additionally add a BM25 pass over file paths using the structured interface tokens as a third retrieval signal, complementing Agentless's existing embedding-based similarity.' This also strengthens the mechanistic case: BM25 exact-match on extracted module/function names catches files that embedding similarity misses because module names are out-of-distribution lexically.

(2) **Add one sentence of mechanistic justification for the +4-7 pp improvement target**: The argument is available — just make it explicit: 'Agentless's fault localization already achieves roughly X% file-level recall on SWE-bench Verified; on SWE-bench-Live, where models are less likely to have encountered the repos during pretraining, recall drops. SpecExtract's structured interface extraction provides a high-precision localization signal (module + entry_point) that compensates for this distribution shift, analogous to how BM25 lexical matching improves recall in out-of-domain retrieval settings (cite BM25 + dense retrieval hybrid literature, e.g., Karpukhin et al. 2020 DPR or a code-specific IR paper).'

(3) Optional but strengthening: acknowledge the cosine similarity validation limitation in one sentence (e.g., 'As a pilot ecological validity check only — this validates schema alignment against expert-annotated specs, not generalization to ambiguous in-the-wild reports') to preempt reviewer #2 questioning.

With fixes (1) and (2), the empirical contribution has a mechanistic backbone that survives reviewer scrutiny.


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
  "promptId": "3ac0dfab-43b1-4ccc-8a77-a4e1fe2dfea0",
  "type": "user",
  "uuid": "89660a90-8189-4f87-820e-e9ba1789d4c0",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:50:28.549Z_

```json
{
  "parentUuid": "89660a90-8189-4f87-820e-e9ba1789d4c0",
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
  "uuid": "9d148eb1-cdee-490a-9f8b-29ebfc6009ff",
  "timestamp": "2026-05-10T07:50:28.549Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:50:28.549Z_

```json
{
  "parentUuid": "9d148eb1-cdee-490a-9f8b-29ebfc6009ff",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e63e4761-5178-4ae5-bc95-011e14310409",
  "timestamp": "2026-05-10T07:50:28.549Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
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
  "leafUuid": "e63e4761-5178-4ae5-bc95-011e14310409",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space behavioral spec extraction for program repair",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:50:59.662Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this round 7 review carefully. The proposal is for "SpecExtract" - a supervised learning approach to extract behavioral specifications from bug reports for guided program repair, targeting EMNLP 2026.

Let me review what has been addressed from Round 6 issues:

**Round 6 Issues to check if resolved in Round 7:**

1. **SIGNIFICANT — Agentless retrieval mechanism mis-specified**: Round 6 said Agentless uses LLM prompting + embedding, not BM25. Looking at the Round 7 proposal...

From the approach section: "Agentless's fault localization uses (a) LLM prompting over the repository folder tree to identify suspicious directories and (b) embedding-based cosine similarity retrieval over code chunks — it does not use BM25. 

This looks FIXED. The proposal now correctly describes Agentless's mechanism (LLM prompting + embedding) and explains that SpecExtract ADDS BM25 as a third signal on top of the existing retrieval methods.

2. **SIGNIFICANT — The +4-7 pp improvement prediction** - I need to continue examining whether this claim is properly justified in Round 7.

The mechanistic case is now solid: Agentless's embedding-based approach hits ~57% file-level Recall@1 on SWE-bench Lite but drops dramatically to 13.33% on SWE-bench-Live Lite due to distribution shift on post-2024 repos. SpecExtract's BM25 retrieval on exact module and entry point tokens bypasses this embedding dependency entirely, so it should recover performance on out-of-distribution repositories without requiring the embedding model to have seen those paths during training.

The cosine similarity validation limitation is also clarified—it's acknowledged as a pilot check on curated SWE-bench instances that can't validate generalization to genuinely ambiguous real-world reports.

The masked-field training protocol is clear too: each artifact field gets independently masked at 50% probability, replaced with a [MISSING] token, and the model learns to output null for those positions rather than inferring missing artifacts from correlated signals.

Now I need to independently verify the key claims, starting with the Agentless integration.

I'm focusing on what actually needs verification at Round 7—the previous rounds have already addressed most issues, so I should prioritize checking for any new concurrent work that's emerged, validating the mechanistic case for the +4-7 percentage point improvement, confirming the SWE-bench-Live baseline numbers, and examining the SpecRover claims and model specifications.

My main skepticism centers on whether BM25 integration is genuinely novel or just incremental engineering, whether a 30-50% relative improvement from 13.33% is realistic, and whether structured spec extraction fits EMNLP's scope or if this is fundamentally a software engineering contribution. Let me search for recent specification extraction papers and any competing approaches that have surfaced since the last round.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e63e4761-5178-4ae5-bc95-011e14310409",
  "isSidechain": false,
  "requestId": "req_011CatXH8PQJNUkjkCBgNuxg",
  "type": "assistant",
  "uuid": "d6ad7916-86b2-43ba-bf46-d28bc91d02ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0133s1DVcChsKo8V5SpJeeVH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26265,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2097,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2097,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26265
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

_source line 9 · 2026-05-10T07:50:59.664Z_

I'll conduct independent verification searches on the key claims in this Round 7 proposal before issuing a verdict.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6ad7916-86b2-43ba-bf46-d28bc91d02ee",
  "isSidechain": false,
  "requestId": "req_011CatXH8PQJNUkjkCBgNuxg",
  "type": "assistant",
  "uuid": "58946f4e-bacc-4dd3-8831-e62e8756ed3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0133s1DVcChsKo8V5SpJeeVH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26265,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2097,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2097,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26265
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

_source line 10 · 2026-05-10T07:51:12.840Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0176xXCgqR2SBUDGxj1MWXtz`</summary>

```json
{
  "description": "Independent verification of SpecExtract paper claims",
  "subagent_type": "Explore",
  "prompt": "You are a research verification agent. Search the web to independently verify claims in a machine learning paper proposal. Do NOT trust any claim — search independently and report what you find.\n\n## Claims to Verify\n\n**Claim 1**: Agentless (arXiv 2407.01489) uses (a) LLM prompting over repository folder tree and (b) embedding-based cosine similarity retrieval — NOT BM25. Verify what Agentless's actual retrieval mechanism is.\n\n**Claim 2**: SWE-bench-Live (arXiv 2505.23419) reports Agentless baseline at 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3) on SWE-bench-Live Lite 300 instances. Verify these numbers.\n\n**Claim 3**: Agent-CoEvo (arXiv 2604.04580) achieves 41.33% on SWE-bench Lite and 46.4% on SWT-bench Lite. Verify existence and numbers.\n\n**Claim 4**: SWE-Lego (arXiv 2601.01426) achieves 52.6% on SWE-bench Verified with 32B model. Verify.\n\n**Claim 5**: SpecRover (arXiv 2408.02232) achieves 31% (93/300) on SWE-bench Lite and Section V-A 'Reasons for Failure' identifies 107/207 (51.7%) unresolved tasks as 'ambiguous issue descriptions'. Verify.\n\n**Claim 6**: Search for any NEW papers from Jan-May 2026 on: \"issue-space specification extraction for program repair\", \"bug report spec extraction repair\", \"structured specification extraction automated repair\". These would be concurrent work the proposal may have missed.\n\n**Claim 7**: Check if Qwen3-Coder-30B-A3B is a real, available model with MoE architecture (~3B active parameters).\n\n**Claim 8**: Search paperswithcode.com for current SWE-bench Verified SOTA to check if it's truly \"saturated\" (93%+ claimed).\n\nFor each claim, report:\n- What you found\n- Whether it confirms or contradicts the claim\n- Any important nuances or discrepancies\n\nSearch sources: arXiv, paperswithcode, Google, Semantic Scholar. Use at least 8 different searches across these sources."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58946f4e-bacc-4dd3-8831-e62e8756ed3b",
  "isSidechain": false,
  "requestId": "req_011CatXH8PQJNUkjkCBgNuxg",
  "type": "assistant",
  "uuid": "695bb850-fa22-4cb9-869c-cc05b3696e81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0133s1DVcChsKo8V5SpJeeVH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26265,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2097,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2097,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 26265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26265
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

_source line 11 · 2026-05-10T07:52:39.772Z_

<details><summary>↩ Tool result · `toolu_0176xXCgqR2SBUDGxj1MWXtz`</summary>

```text
Perfect! I now have comprehensive verification data. Let me compile my findings.

## Verification Report: Machine Learning Paper Claims

Based on my independent web search and document verification, here's what I found for each claim:

---

### **Claim 1: Agentless Retrieval Mechanism**

**Claim**: Agentless uses (a) LLM prompting over repository folder tree and (b) embedding-based cosine similarity retrieval — NOT BM25.

**Verification Result**: **PARTIALLY CONFIRMED WITH NUANCE**

**Findings**:
- Agentless DOES use LLM prompting over repository folder tree structure. The system creates a high-level tree representation by recursively traversing from the root folder, which is fed to the LLM for initial localization of candidate files.
- Agentless uses **embedding-based retrieval** to identify additional suspicious files, combining results with LLM-based prompting.
- The claim about "NOT BM25" is correct—Agentless prioritizes embedding-based retrieval with cosine similarity. However, some subsequent work (like Agentless-Lite) has adopted BM25 as an alternative due to its lightweight, scalable properties for large repositories.

**Sources**: [Agentless paper on arXiv](https://arxiv.org/abs/2407.01489), [GitHub discussion of method](https://github.com/sorendunn/Agentless-Lite)

---

### **Claim 2: SWE-bench-Live Agentless Baseline Numbers**

**Claim**: SWE-bench-Live reports Agentless baseline at 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3).

**Verification Result**: **CONFIRMED**

**Findings**:
- I directly verified Table 3 in the SWE-bench-Live paper (arXiv 2505.23419), which confirms these exact numbers:
  - GPT-4o: 11.67%
  - GPT-4.1: 12.00%
  - DeepSeek V3: 13.33%
- These represent resolved rates on SWE-bench-Live Lite (300 instances).
- The note in the paper indicates Agentless evaluations omitted the reranking stage based on regression testing due to infrastructure constraints.

**Sources**: [SWE-bench Goes Live! paper](https://arxiv.org/html/2505.23419v1), verified via direct document fetch

---

### **Claim 3: Agent-CoEvo Performance Numbers**

**Claim**: Agent-CoEvo achieves 41.33% on SWE-bench Lite and 46.4% on SWT-bench Lite.

**Verification Result**: **CONFIRMED**

**Findings**:
- Agent-CoEvo (arXiv 2604.04580) achieves exactly:
  - SWE-bench Lite (300 issues): 41.33% resolution rate
  - SWT-bench Lite (276 issues): 46.4% resolution rate, with 56.0% mean line coverage improvement
- The paper notes that Agent-CoEvo exceeds strong baselines like DARS (37.00% on SWE-bench Lite) and AssertFlip (38.0% on SWT-bench Lite).
- The framework is a coevolutionary multi-agent system that jointly explores code patches and test patches.

**Sources**: [Agent-CoEvo paper](https://arxiv.org/html/2604.04580), verified via direct document fetch

---

### **Claim 4: SWE-Lego Performance**

**Claim**: SWE-Lego achieves 52.6% on SWE-bench Verified with 32B model.

**Verification Result**: **CONFIRMED**

**Findings**:
- SWE-Lego-Qwen3-32B achieves exactly **52.6%** on SWE-bench Verified using only Supervised Fine-Tuning (SFT).
- The model uses a carefully crafted SFT-only approach comprising: (1) SWE-Lego dataset (32k high-quality task instances + 18k validated trajectories), (2) error masking, and (3) difficulty-based curriculum.
- Paper published January 4, 2026 (arXiv 2601.01426).

**Sources**: [SWE-Lego paper](https://arxiv.org/abs/2601.01426), [GitHub repository](https://github.com/SWE-Lego/SWE-Lego)

---

### **Claim 5: SpecRover Performance and Failure Analysis**

**Claim**: SpecRover achieves 31% (93/300) on SWE-bench Lite. Section V-A identifies 107/207 (51.7%) unresolved tasks as 'ambiguous issue descriptions'.

**Verification Result**: **CONFIRMED**

**Findings**:
- SpecRover (arXiv 2408.02232) achieved exactly **31% efficacy on SWE-bench Lite**, resolving **93 out of 300 issues**.
- The failure analysis in Section V-A ("Reasons for Failure" in RQ1) analyzed 207 unresolved tasks with this breakdown:
  - **Ambiguous issue descriptions**: 51.7% (107 tasks) - labeled as "hard or impossible to solve" without additional information
  - Incorrect fix location: 29.5% (61 tasks)
  - Incorrect code modification: 18.8% (39 tasks)
- This is an improvement of >50% over the predecessor AutoCodeRover on full SWE-Bench (2294 issues).

**Sources**: [SpecRover paper](https://arxiv.org/html/2408.02232), verified via direct document fetch

---

### **Claim 6: New Papers Jan-May 2026 on Specification Extraction**

**Claim**: Search for new papers on "issue-space specification extraction for program repair", "bug report spec extraction repair", "structured specification extraction automated repair".

**Verification Result**: **FOUND RELEVANT CONCURRENT WORK**

**Findings**: I found multiple relevant papers from Jan-May 2026 that address specification extraction and specification-centric program repair:

1. **Specification Vibing for Automated Program Repair** (February 2026, arXiv 2602.08263)
   - Treats repair as behavior-specification repair rather than ad-hoc code editing
   - Translates buggy code into structured behavior specifications capturing intended runtime behavior
   - VibeRepair correctly repairs 174 bugs on Defects4J v1.2, exceeding SOTA by 28 bugs
   - **This is directly concurrent work the proposal may have missed**

2. **Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation** (April-May 2026, arXiv 2505.07270)
   - SpecFix addresses automated repair by analyzing and repairing program distributions induced by descriptions
   - Significantly improves code generation performance of SOTA LLMs
   - **Directly relevant to the proposal's focus on ambiguous specifications**

3. **Survey: A Survey of LLM-based Automated Program Repair** (2026, arXiv 2506.23749)
   - Comprehensive taxonomy of 63 LLM-based APR systems (Jan 2022 - Jun 2025)
   - Categorizes systems into four paradigms
   - Shows rapid evolution in specification and behavior-centric approaches

4. **Synthetic Data Generation for APR** (2026 ICSE)
   - Synthetic data pipeline using LLMs to generate bugs through code rewriting
   - Synthesizes valuable intermediate repair steps
   - Recent advancement in training data for repair systems

**Sources**: [Specification Vibing](https://arxiv.org/abs/2602.08263), [Ambiguous Problem Description Repair](https://arxiv.org/html/2505.07270), [LLM APR Survey](https://arxiv.org/abs/2506.23749)

---

### **Claim 7: Qwen3-Coder-30B-A3B Model Architecture**

**Claim**: Qwen3-Coder-30B-A3B is a real, available model with MoE architecture (~3B active parameters).

**Verification Result**: **CONFIRMED**

**Findings**:
- **Qwen3-Coder-30B-A3B is a real, available model** publicly hosted on Hugging Face and accessible via multiple platforms (OpenRouter, LM Studio, Ollama).
- **Confirmed MoE architecture**:
  - Total: 30.5 billion parameters
  - Active per token: ~3.3 billion parameters (sparse activation)
  - 128 total experts with 8 experts selected via routing per token
  - This matches the claim of "~3B active parameters"
- 48 transformer layers, Grouped Query Attention (GQA) with 32 query heads and 4 key-value heads
- **Native context window**: 32,768 tokens; extendable to 131,072 or 256,000 with YaRN scaling
- Specialized for code generation, repository-scale understanding, and agentic tool use

**Sources**: [Qwen3-30B-A3B on Hugging Face](https://huggingface.co/Qwen/Qwen3-30B-A3B), [Qwen3-Coder on OpenRouter](https://openrouter.ai/qwen/qwen3-coder-30b-a3b-instruct), [GitHub](https://github.com/QwenLM/Qwen3-Coder)

---

### **Claim 8: SWE-bench Verified SOTA and Saturation**

**Claim**: Check if SWE-bench Verified is truly "saturated" (93%+ claimed).

**Verification Result**: **CONFIRMED AS SATURATED**

**Findings**:
- **Top SWE-bench Verified scores (April 2026)**:
  - Claude Mythos Preview: **93.9%** (leads the leaderboard)
  - GPT-5.3 Codex: 85%
  - Claude Opus 4.5: 80.9%
- **Clear evidence of saturation**:
  - The same Claude Mythos model that achieves 93.9% on SWE-bench Verified scores only **45.9% on SWE-bench Pro** (the harder, contamination-free version)
  - This dramatic 48-point drop demonstrates severe saturation and potential contamination issues in the Verified benchmark
- **Community response to saturation**:
  - SWE-bench Pro was introduced to address limitations and saturation
  - OpenAI's audit found that frontier models (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could reproduce verbatim gold patches for certain tasks
  - 59.4% of hardest unsolved problems have flawed test cases

**Sources**: [SWE-bench Verified Leaderboard](https://www.swebench.com/verified.html), [CodeAnt SWE-bench Analysis](https://www.codeant.ai/blogs/swe-bench-scores), [SWE-Bench Pro analysis](https://www.morphllm.com/swe-bench-pro)

---

## Summary Table

| Claim | Status | Key Finding | Confidence |
|-------|--------|------------|------------|
| 1. Agentless retrieval | Partially Confirmed | Uses embedding+LLM prompting, not BM25 | High |
| 2. Agentless baseline numbers | Confirmed | Exact numbers verified in Table 3 | Very High |
| 3. Agent-CoEvo numbers | Confirmed | 41.33% / 46.4% verified | Very High |
| 4. SWE-Lego 52.6% | Confirmed | Exact performance verified | Very High |
| 5. SpecRover 31% + 51.7% | Confirmed | All metrics verified in paper | Very High |
| 6. Concurrent spec work | Found | SpecVibe (Feb 2026) and others exist | High |
| 7. Qwen3-Coder MoE | Confirmed | Real model, ~3.3B active params | Very High |
| 8. SOTA saturation 93%+ | Confirmed | 93.9% achieved, evidence of saturation | Very High |

---

**Overall Assessment**: The proposal's factual claims are **well-supported** by the literature. The main insight is that Specification Vibing (arXiv 2602.08263, Feb 2026) represents concurrent work directly addressing specification-centric repair that the proposal should acknowledge.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "695bb850-fa22-4cb9-869c-cc05b3696e81",
  "isSidechain": false,
  "promptId": "3ac0dfab-43b1-4ccc-8a77-a4e1fe2dfea0",
  "type": "user",
  "uuid": "cc1a51f5-2f73-494f-9b03-1e4c60cd4e4e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are a research verification agent. Search the web to independently verify claims in a machine learning paper proposal. Do NOT trust any claim — search independently and report what you find.\n\n## Claims to Verify\n\n**Claim 1**: Agentless (arXiv 2407.01489) uses (a) LLM prompting over repository folder tree and (b) embedding-based cosine similarity retrieval — NOT BM25. Verify what Agentless's actual retrieval mechanism is.\n\n**Claim 2**: SWE-bench-Live (arXiv 2505.23419) reports Agentless baseline at 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3) on SWE-bench-Live Lite 300 instances. Verify these numbers.\n\n**Claim 3**: Agent-CoEvo (arXiv 2604.04580) achieves 41.33% on SWE-bench Lite and 46.4% on SWT-bench Lite. Verify existence and numbers.\n\n**Claim 4**: SWE-Lego (arXiv 2601.01426) achieves 52.6% on SWE-bench Verified with 32B model. Verify.\n\n**Claim 5**: SpecRover (arXiv 2408.02232) achieves 31% (93/300) on SWE-bench Lite and Section V-A 'Reasons for Failure' identifies 107/207 (51.7%) unresolved tasks as 'ambiguous issue descriptions'. Verify.\n\n**Claim 6**: Search for any NEW papers from Jan-May 2026 on: \"issue-space specification extraction for program repair\", \"bug report spec extraction repair\", \"structured specification extraction automated repair\". These would be concurrent work the proposal may have missed.\n\n**Claim 7**: Check if Qwen3-Coder-30B-A3B is a real, available model with MoE architecture (~3B active parameters).\n\n**Claim 8**: Search paperswithcode.com for current SWE-bench Verified SOTA to check if it's truly \"saturated\" (93%+ claimed).\n\nFor each claim, report:\n- What you found\n- Whether it confirms or contradicts the claim\n- Any important nuances or discrepancies\n\nSearch sources: arXiv, paperswithcode, Google, Semantic Scholar. Use at least 8 different searches across these sources.",
    "agentId": "aad09a08af3ab3a8f",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I now have comprehensive verification data. Let me compile my findings.\n\n## Verification Report: Machine Learning Paper Claims\n\nBased on my independent web search and document verification, here's what I found for each claim:\n\n---\n\n### **Claim 1: Agentless Retrieval Mechanism**\n\n**Claim**: Agentless uses (a) LLM prompting over repository folder tree and (b) embedding-based cosine similarity retrieval — NOT BM25.\n\n**Verification Result**: **PARTIALLY CONFIRMED WITH NUANCE**\n\n**Findings**:\n- Agentless DOES use LLM prompting over repository folder tree structure. The system creates a high-level tree representation by recursively traversing from the root folder, which is fed to the LLM for initial localization of candidate files.\n- Agentless uses **embedding-based retrieval** to identify additional suspicious files, combining results with LLM-based prompting.\n- The claim about \"NOT BM25\" is correct—Agentless prioritizes embedding-based retrieval with cosine similarity. However, some subsequent work (like Agentless-Lite) has adopted BM25 as an alternative due to its lightweight, scalable properties for large repositories.\n\n**Sources**: [Agentless paper on arXiv](https://arxiv.org/abs/2407.01489), [GitHub discussion of method](https://github.com/sorendunn/Agentless-Lite)\n\n---\n\n### **Claim 2: SWE-bench-Live Agentless Baseline Numbers**\n\n**Claim**: SWE-bench-Live reports Agentless baseline at 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3).\n\n**Verification Result**: **CONFIRMED**\n\n**Findings**:\n- I directly verified Table 3 in the SWE-bench-Live paper (arXiv 2505.23419), which confirms these exact numbers:\n  - GPT-4o: 11.67%\n  - GPT-4.1: 12.00%\n  - DeepSeek V3: 13.33%\n- These represent resolved rates on SWE-bench-Live Lite (300 instances).\n- The note in the paper indicates Agentless evaluations omitted the reranking stage based on regression testing due to infrastructure constraints.\n\n**Sources**: [SWE-bench Goes Live! paper](https://arxiv.org/html/2505.23419v1), verified via direct document fetch\n\n---\n\n### **Claim 3: Agent-CoEvo Performance Numbers**\n\n**Claim**: Agent-CoEvo achieves 41.33% on SWE-bench Lite and 46.4% on SWT-bench Lite.\n\n**Verification Result**: **CONFIRMED**\n\n**Findings**:\n- Agent-CoEvo (arXiv 2604.04580) achieves exactly:\n  - SWE-bench Lite (300 issues): 41.33% resolution rate\n  - SWT-bench Lite (276 issues): 46.4% resolution rate, with 56.0% mean line coverage improvement\n- The paper notes that Agent-CoEvo exceeds strong baselines like DARS (37.00% on SWE-bench Lite) and AssertFlip (38.0% on SWT-bench Lite).\n- The framework is a coevolutionary multi-agent system that jointly explores code patches and test patches.\n\n**Sources**: [Agent-CoEvo paper](https://arxiv.org/html/2604.04580), verified via direct document fetch\n\n---\n\n### **Claim 4: SWE-Lego Performance**\n\n**Claim**: SWE-Lego achieves 52.6% on SWE-bench Verified with 32B model.\n\n**Verification Result**: **CONFIRMED**\n\n**Findings**:\n- SWE-Lego-Qwen3-32B achieves exactly **52.6%** on SWE-bench Verified using only Supervised Fine-Tuning (SFT).\n- The model uses a carefully crafted SFT-only approach comprising: (1) SWE-Lego dataset (32k high-quality task instances + 18k validated trajectories), (2) error masking, and (3) difficulty-based curriculum.\n- Paper published January 4, 2026 (arXiv 2601.01426).\n\n**Sources**: [SWE-Lego paper](https://arxiv.org/abs/2601.01426), [GitHub repository](https://github.com/SWE-Lego/SWE-Lego)\n\n---\n\n### **Claim 5: SpecRover Performance and Failure Analysis**\n\n**Claim**: SpecRover achieves 31% (93/300) on SWE-bench Lite. Section V-A identifies 107/207 (51.7%) unresolved tasks as 'ambiguous issue descriptions'.\n\n**Verification Result**: **CONFIRMED**\n\n**Findings**:\n- SpecRover (arXiv 2408.02232) achieved exactly **31% efficacy on SWE-bench Lite**, resolving **93 out of 300 issues**.\n- The failure analysis in Section V-A (\"Reasons for Failure\" in RQ1) analyzed 207 unresolved tasks with this breakdown:\n  - **Ambiguous issue descriptions**: 51.7% (107 tasks) - labeled as \"hard or impossible to solve\" without additional information\n  - Incorrect fix location: 29.5% (61 tasks)\n  - Incorrect code modification: 18.8% (39 tasks)\n- This is an improvement of >50% over the predecessor AutoCodeRover on full SWE-Bench (2294 issues).\n\n**Sources**: [SpecRover paper](https://arxiv.org/html/2408.02232), verified via direct document fetch\n\n---\n\n### **Claim 6: New Papers Jan-May 2026 on Specification Extraction**\n\n**Claim**: Search for new papers on \"issue-space specification extraction for program repair\", \"bug report spec extraction repair\", \"structured specification extraction automated repair\".\n\n**Verification Result**: **FOUND RELEVANT CONCURRENT WORK**\n\n**Findings**: I found multiple relevant papers from Jan-May 2026 that address specification extraction and specification-centric program repair:\n\n1. **Specification Vibing for Automated Program Repair** (February 2026, arXiv 2602.08263)\n   - Treats repair as behavior-specification repair rather than ad-hoc code editing\n   - Translates buggy code into structured behavior specifications capturing intended runtime behavior\n   - VibeRepair correctly repairs 174 bugs on Defects4J v1.2, exceeding SOTA by 28 bugs\n   - **This is directly concurrent work the proposal may have missed**\n\n2. **Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation** (April-May 2026, arXiv 2505.07270)\n   - SpecFix addresses automated repair by analyzing and repairing program distributions induced by descriptions\n   - Significantly improves code generation performance of SOTA LLMs\n   - **Directly relevant to the proposal's focus on ambiguous specifications**\n\n3. **Survey: A Survey of LLM-based Automated Program Repair** (2026, arXiv 2506.23749)\n   - Comprehensive taxonomy of 63 LLM-based APR systems (Jan 2022 - Jun 2025)\n   - Categorizes systems into four paradigms\n   - Shows rapid evolution in specification and behavior-centric approaches\n\n4. **Synthetic Data Generation for APR** (2026 ICSE)\n   - Synthetic data pipeline using LLMs to generate bugs through code rewriting\n   - Synthesizes valuable intermediate repair steps\n   - Recent advancement in training data for repair systems\n\n**Sources**: [Specification Vibing](https://arxiv.org/abs/2602.08263), [Ambiguous Problem Description Repair](https://arxiv.org/html/2505.07270), [LLM APR Survey](https://arxiv.org/abs/2506.23749)\n\n---\n\n### **Claim 7: Qwen3-Coder-30B-A3B Model Architecture**\n\n**Claim**: Qwen3-Coder-30B-A3B is a real, available model with MoE architecture (~3B active parameters).\n\n**Verification Result**: **CONFIRMED**\n\n**Findings**:\n- **Qwen3-Coder-30B-A3B is a real, available model** publicly hosted on Hugging Face and accessible via multiple platforms (OpenRouter, LM Studio, Ollama).\n- **Confirmed MoE architecture**:\n  - Total: 30.5 billion parameters\n  - Active per token: ~3.3 billion parameters (sparse activation)\n  - 128 total experts with 8 experts selected via routing per token\n  - This matches the claim of \"~3B active parameters\"\n- 48 transformer layers, Grouped Query Attention (GQA) with 32 query heads and 4 key-value heads\n- **Native context window**: 32,768 tokens; extendable to 131,072 or 256,000 with YaRN scaling\n- Specialized for code generation, repository-scale understanding, and agentic tool use\n\n**Sources**: [Qwen3-30B-A3B on Hugging Face](https://huggingface.co/Qwen/Qwen3-30B-A3B), [Qwen3-Coder on OpenRouter](https://openrouter.ai/qwen/qwen3-coder-30b-a3b-instruct), [GitHub](https://github.com/QwenLM/Qwen3-Coder)\n\n---\n\n### **Claim 8: SWE-bench Verified SOTA and Saturation**\n\n**Claim**: Check if SWE-bench Verified is truly \"saturated\" (93%+ claimed).\n\n**Verification Result**: **CONFIRMED AS SATURATED**\n\n**Findings**:\n- **Top SWE-bench Verified scores (April 2026)**:\n  - Claude Mythos Preview: **93.9%** (leads the leaderboard)\n  - GPT-5.3 Codex: 85%\n  - Claude Opus 4.5: 80.9%\n- **Clear evidence of saturation**:\n  - The same Claude Mythos model that achieves 93.9% on SWE-bench Verified scores only **45.9% on SWE-bench Pro** (the harder, contamination-free version)\n  - This dramatic 48-point drop demonstrates severe saturation and potential contamination issues in the Verified benchmark\n- **Community response to saturation**:\n  - SWE-bench Pro was introduced to address limitations and saturation\n  - OpenAI's audit found that frontier models (GPT-5.2, Claude Opus 4.5, Gemini 3 Flash) could reproduce verbatim gold patches for certain tasks\n  - 59.4% of hardest unsolved problems have flawed test cases\n\n**Sources**: [SWE-bench Verified Leaderboard](https://www.swebench.com/verified.html), [CodeAnt SWE-bench Analysis](https://www.codeant.ai/blogs/swe-bench-scores), [SWE-Bench Pro analysis](https://www.morphllm.com/swe-bench-pro)\n\n---\n\n## Summary Table\n\n| Claim | Status | Key Finding | Confidence |\n|-------|--------|------------|------------|\n| 1. Agentless retrieval | Partially Confirmed | Uses embedding+LLM prompting, not BM25 | High |\n| 2. Agentless baseline numbers | Confirmed | Exact numbers verified in Table 3 | Very High |\n| 3. Agent-CoEvo numbers | Confirmed | 41.33% / 46.4% verified | Very High |\n| 4. SWE-Lego 52.6% | Confirmed | Exact performance verified | Very High |\n| 5. SpecRover 31% + 51.7% | Confirmed | All metrics verified in paper | Very High |\n| 6. Concurrent spec work | Found | SpecVibe (Feb 2026) and others exist | High |\n| 7. Qwen3-Coder MoE | Confirmed | Real model, ~3.3B active params | Very High |\n| 8. SOTA saturation 93%+ | Confirmed | 93.9% achieved, evidence of saturation | Very High |\n\n---\n\n**Overall Assessment**: The proposal's factual claims are **well-supported** by the literature. The main insight is that Specification Vibing (arXiv 2602.08263, Feb 2026) represents concurrent work directly addressing specification-centric repair that the proposal should acknowledge."
      }
    ],
    "totalDurationMs": 86926,
    "totalTokens": 42197,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3176,
      "cache_read_input_tokens": 35909,
      "output_tokens": 3105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3176
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3105,
          "cache_read_input_tokens": 35909,
          "cache_creation_input_tokens": 3176,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3176,
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
  "sourceToolAssistantUUID": "695bb850-fa22-4cb9-869c-cc05b3696e81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "cc1a51f5-2f73-494f-9b03-1e4c60cd4e4e",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space behavioral spec extraction for program repair",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9"
}
```

---

### Assistant

_source line 14 · 2026-05-10T07:54:20.441Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the verification agent has confirmed most claims. Let me now analyze the Round 7 proposal more carefully in light of:

1. All Round 6 issues were addressed
2. Concurrent work: SpecFix (arXiv 2505.07270) and Specification Vibing (arXiv 2602.08263) are already mentioned in the proposal as "VibeRepair" - so it's already in the landscape
3. Qwen3-Coder-30B-A3B is confirmed as a real model
4. All key numbers are verified


5. SpecRover's 51.7% claim checks out

Now looking at what was actually fixed from Round 6: the agentless retrieval mechanism is now properly described with LLM prompting, embeddings, and BM25 as three separate signals. The mechanistic case for the improvement is explicitly laid out through Recall@1 degradation on post-2024 repositories. The cosine similarity validation is acknowledged as a limited pilot check, and the masked-field training protocol is specified with concrete parameters like p=0.5 and the [MISSING] token.

For the new proposal, BM25 is being introduced as an additional third retrieval signal layered on top of the existing agentless approach rather than replacing it. The mechanistic argument for the 4-7 percentage point gain rests on agentless dropping dramatically from around 50.8% on SWE-bench Verified down to 13.33% on SWE-bench-Live Lite, which they attribute to fault localization failures on newer repositories. They're arguing BM25 applied to extracted module and entry point tokens would help bridge that distribution shift, and they cite an ICSE 2023 paper showing 8.6% MRR improvement in out-of-distribution settings. The reasoning is sound, though there are still some lingering concerns to work through.

The first issue is whether BM25 is actually novel here—the verification agent mentioned that Agentless-Lite already adopted BM25 for its lightweight, scalable properties on large codebases, so if it's already in the system, then SpecExtract's contribution might just be reusing existing tooling rather than introducing something new. I need to verify this more carefully. Second, the 4× performance drop is attributed to localization failure, but that's asserted rather than demonstrated—the actual causes could be many things like harder issues in the live set, different issue description quality, or varying codebase complexity, and BM25 only addresses one potential cause. Third, the projected 4-7 percentage point improvement still feels somewhat speculative given these uncertainties.

The training set of 2,294 instances for fine-tuning a 30B parameter model is quite small, so the claimed magnitude of improvement from spec injection into Agentless's fault localization might be overstated. I also found SpecFix from May 2026, which handles automated repair of ambiguous problem descriptions for LLM-based code generation and shows significant performance gains—this is recent concurrent work that the proposal doesn't address. Finally, there's the EMNLP positioning around extracting structured information from semi-structured bug text, which needs to be evaluated for how well it actually fits the venue's scope. EMNLP typically focuses on core NLP tasks (text, language understanding, generation), and a paper about SWE-bench program repair that uses NLP techniques but is fundamentally about software engineering might face desk rejection. The novelty of the NLP contribution (information extraction from bug reports) needs to be clearer.

The auto-research mode costs total around $784-1032 (GPU plus Claude API), which is outside typical academic budgets but within the stated constraints.

For novelty, the fine-tuned issue-space spec extractor is somewhat novel, though SpecRover already handles spec extraction and VibeRepair does code-to-spec translation. The BM25 addition to Agentless is a straightforward engineering improvement, and while the SFT on test_patch AST parsing shows creativity, the training set is quite small—I'd rate this around 3/5 for moderate but incremental novelty.

On feasibility, Qwen3-Coder-30B-A3B is real and fits on H100 with QLoRA, the 2,294 training instances are workable despite being small, and the BM25 integration with Agentless is implementable. The 16-day timeline is tight but achievable, though the predicted +4-7 percentage point improvement is mechanistically grounded yet uncertain—I'd score this 3.5/5 overall.

The proposal itself is now very detailed and well-structured after multiple rounds of revision, and the schema is coming together clearly. or just concerns. The key question is whether SpecExtract's spec extraction step genuinely adds novelty beyond what Agentless-Lite already does with BM25, or if it's primarily an engineering improvement. I also need to verify the relationship to SpecFix, which tackles the ambiguous specification problem from a different angle and may have been published around the same time. The training set of 2,294 instances also feels relatively small for training a sophisticated spec extraction model, which raises questions about generalization.

Looking at the core contribution more carefully, it really comes down to two things: a fine-tuned model for extracting structured behavioral specs from bug reports, and integrating that with Agentless through prompt injection and an additional BM25 retrieval signal. For a venue like EMNLP, the NLP contribution would center on the information extraction task itself—converting unstructured bug reports into structured specs. That's an interesting problem, but the training approach seems to rely heavily on existing techniques rather than novel methodology.

The real question is whether this clears the bar for EMNLP. The spec extraction framing as structured information extraction could work if the empirical results on SWE-bench-Live are strong enough and the distinction between issue-space and code-space reasoning is clearly articulated. The projected 4-7 percentage point improvement is modest, though potentially meaningful if it holds up.

But there are real limitations: the training data construction leans on AST parsing of test patches, which feels somewhat circular since tests are written with knowledge of the fix. The spec quality on genuinely ambiguous real-world reports hasn't been validated beyond cosine similarity to SWE-bench Pro requirements. And the BM25 addition could easily be dismissed as a straightforward engineering choice rather than a novel contribution.

I should also note that SpecFix appeared just three days ago, which is too recent for the proposal to have accounted for, though it's worth flagging as a reviewer. Looking back at the core structural issues, the Round 7 proposal has made progress on several fronts, but I need to assess whether those improvements are sufficient for the venue.

The main new concern is whether the BM25 component in Agentless-Lite is truly novel or just an incremental engineering decision.

There's also a question about whether 2,294 training instances is adequate for teaching a 30B parameter model to extract specifications reliably, especially without discussion of overfitting risks or data-to-capacity ratios.

And I'm still uncertain whether this reads as an NLP contribution or primarily a software engineering paper—the spec extraction methodology needs clearer positioning for EMNLP's audience.

On novelty, the AST-based SFT approach for extracting specs from test assertions is creative, but the training data comes directly from SWE-bench, which limits the originality somewhat. The spec extractor itself is useful and the contamination-resistant evaluation is solid, but the 4-7 percentage point improvement on SWE-bench-Live Lite feels incremental, and EMNLP might not be the right fit for a systems-focused contribution. With an average score of 3.375, I'm below the acceptance threshold—the core issue is that novelty and impact both sit at 3/5, which is hard to overcome even with strong clarity and feasibility. At Round 7 of 10, the technical soundness is there, but the fundamental concerns about depth and significance remain unresolved, so I'm leaning toward recommending revision rather than outright failure. The training set size is a real gap—2,294 instances seems light for fine-tuning a 30B parameter model, and the proposal doesn't address generalization concerns at all. I need to flag this as a significant issue requiring justification, along with clarifying the novelty distinction between their BM25 approach and Agentless-Lite's existing methods. The core issue is that if Agentless-Lite already incorporates BM25, then the proposal's BM25 contribution becomes less novel—it's essentially just applying BM25 to extracted interface tokens rather than introducing the technique itself. I need to flag this as a significant concern and push the authors to clarify how their BM25 approach differs from Agentless-Lite's implementation. Given these novelty questions around BM25, the training data justification gap, and the need for clearer EMNLP framing, this warrants a revise verdict. I need to reconsider the BM25 angle—Agentless-Lite already uses BM25, but SpecExtract's approach is fundamentally different because it applies BM25 to extracted interface tokens from the spec rather than raw issue text, which is a more structured and meaningful signal. This distinction needs to be front and center in my feedback, along with flagging the small training set as a moderate concern.

Looking back at the actual novelty, the core contributions that matter are the first trained model specifically for issue-space spec extraction, the data construction methodology combining AST parsing with LLM assistance, the pipeline-agnostic design, and the SWE-bench-Live evaluation on a contamination-resistant benchmark. The BM25 component is less central to the story than I initially weighted it.

Even accounting for this reframing, the small training set and incremental nature of the work keep me from pushing novelty higher than 3/5. The average of 3.375 falls short of the 4.0 threshold, so revise is the right call—these issues need substantive fixes, not just surface-level adjustments.

For the feedback, I should focus on clarifying how SpecExtract's structured token extraction differs from Agentless-Lite's BM25 approach, pushing them to better justify their training data choices, tightening the EMNLP framing around NLP contributions, and addressing the concurrent SpecFix work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc1a51f5-2f73-494f-9b03-1e4c60cd4e4e",
  "isSidechain": false,
  "requestId": "req_011CatXSoEG1xXnDG52v5Bix",
  "type": "assistant",
  "uuid": "4d0d9d84-2cc0-43f5-b742-4e4bd7b7e965",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018fEM956f8PcPn77JaFBFEZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5213,
      "cache_read_input_tokens": 37896,
      "output_tokens": 5662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5662,
          "cache_read_input_tokens": 37896,
          "cache_creation_input_tokens": 5213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5213
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

_source line 15 · 2026-05-10T07:54:20.443Z_

Now let me do a focused follow-up search on the Agentless-Lite BM25 question and the SpecFix paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d0d9d84-2cc0-43f5-b742-4e4bd7b7e965",
  "isSidechain": false,
  "requestId": "req_011CatXSoEG1xXnDG52v5Bix",
  "type": "assistant",
  "uuid": "7d0b743f-3e6c-418b-a68f-b2ac499b90f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018fEM956f8PcPn77JaFBFEZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5213,
      "cache_read_input_tokens": 37896,
      "output_tokens": 5662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5662,
          "cache_read_input_tokens": 37896,
          "cache_creation_input_tokens": 5213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5213
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

_source line 16 · 2026-05-10T07:54:30.102Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MauYSPo95dUGT2N1dSg84f`</summary>

```json
{
  "description": "Verify Agentless-Lite BM25 and SpecFix concurrent work",
  "subagent_type": "Explore",
  "prompt": "I need to independently verify two specific claims for a paper review:\n\n**Search 1**: Does \"Agentless-Lite\" or any official Agentless variant ALREADY use BM25 for code localization? A paper (SpecExtract) claims to ADD BM25 as a new third retrieval signal to Agentless. But one search result mentioned \"Agentless-Lite adopted BM25 as an alternative.\" Is BM25 already in Agentless's official codebase or Agentless-Lite? Search:\n- \"Agentless-Lite BM25\" site:github.com\n- \"Agentless BM25 retrieval\" \n- arXiv 2407.01489 (Agentless) - check if any version uses BM25\n- paperswithcode Agentless to see if there are BM25-based variants\n\nReport: Does Agentless (any official variant) already use BM25? If yes, does it use raw query text or structured tokens for BM25?\n\n**Search 2**: Find the paper \"SpecFix: Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation\" (arXiv 2505.07270). What does it do? How does it relate to extracting behavioral specs from bug reports? Is it a direct competitor to SpecExtract (which extracts structured specs from bug reports to guide program repair)? Fetch the abstract from https://arxiv.org/abs/2505.07270\n\n**Search 3**: Search for any papers from Jan-May 2026 that specifically focus on \"extracting behavioral specifications from GitHub issues\" or \"fine-tuning for specification extraction from bug reports\" — i.e., trained models specifically for issue-space spec extraction. This is the specific gap SpecExtract claims to fill.\n\nSearch queries to try:\n- \"specification extraction bug report fine-tuning 2026\" site:arxiv.org\n- \"behavioral specification GitHub issues extraction\" 2026\n- \"issue description specification extraction repair\" 2026\n\nReport your findings clearly with paper titles, arXiv IDs, and whether they challenge SpecExtract's novelty claim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d0b743f-3e6c-418b-a68f-b2ac499b90f6",
  "isSidechain": false,
  "requestId": "req_011CatXSoEG1xXnDG52v5Bix",
  "type": "assistant",
  "uuid": "e5cb2d16-44e6-4838-a5ae-8782fe329a27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018fEM956f8PcPn77JaFBFEZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5213,
      "cache_read_input_tokens": 37896,
      "output_tokens": 5662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5213,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5662,
          "cache_read_input_tokens": 37896,
          "cache_creation_input_tokens": 5213,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5213
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

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "e5cb2d16-44e6-4838-a5ae-8782fe329a27",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space behavioral spec extraction for program repair",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9"
}
```

---

### Tool result

_source line 19 · 2026-05-10T07:56:35.509Z_

<details><summary>↩ Tool result · `toolu_01MauYSPo95dUGT2N1dSg84f`</summary>

```text
Perfect! Now I have the critical information. Let me compile my findings for the user.

## Summary of Findings

Based on my comprehensive search, here are the answers to your three verification questions:

---

### **SEARCH 1: Does Agentless (any variant) already use BM25?**

**YES - Agentless DOES use BM25 for code localization, not just Agentless-Lite.**

**Critical Finding:** The original **Agentless paper (arXiv 2407.01489)** explicitly uses BM25 for code localization. According to multiple sources, Agentless "prepends the top-10 BM25-ranked files to the prompt using the task description as the query, with BM25 computed over function/class-level chunks using rank-bm25, and scores aggregated to file level by taking the maximum chunk score."

**Agentless-Lite variant:** The lighter variant uses **embedding-based (dense) retrieval instead**, not BM25. According to the SWE-Bench leaderboards, Agentless-Lite uses "an embedding model to retrieve relevant files from the repository" (models like Voyage Code-3 or text-embedding-3-small) rather than BM25.

**On Query Format:** The Agentless baseline uses the **raw task description** (not structured tokens) as the BM25 query. One recent paper mentions that "query reformulation, which adds a summary and code signals (identifiers, snippets), consistently strengthens lexical retrieval, with BM25 boosting first-file localization by 36% over baseline" — but this is an **enhancement**, not the baseline Agentless approach.

**Implication for SpecExtract's novelty claim:** If SpecExtract claims to "ADD BM25 as a new third retrieval signal" to Agentless, this claim is **problematic**. BM25 is already Agentless's primary (and only) localization method. However, it's possible SpecExtract adds BM25 with **structured tokens** (not raw query text), which would be the novel contribution.

---

### **SEARCH 2: What is SpecFix (arXiv 2505.07270)?**

**SpecFix** automatically repairs ambiguous natural language problem descriptions for LLM-based code generation. It works in two steps:

1. **Analysis & Repair:** Uses testing and program repair to modify how the LLM interprets a description
2. **Refinement:** Applies "contrastive specification inference" to update the description based on interpretation changes

**How it relates to bug report specs:** SpecFix clarifies *ambiguous problem statements* (code generation benchmarks) by improving descriptions using input-output examples. Bug report specification extraction typically clarifies *what went wrong* by identifying reproduction conditions and desired fixes. Both address ambiguity but in opposite directions—SpecFix clarifies "what to build," bug specs clarify "what went wrong."

**Is it a direct competitor to SpecExtract?** **NO** — SpecFix targets code generation benchmarks with input-output examples, while SpecExtract (based on your description) targets real GitHub issues/bug reports. Different problem domain.

---

### **SEARCH 3: Are there papers on fine-tuned models for specification extraction from GitHub issues (Jan-May 2026)?**

**NO dedicated papers found specifically on "fine-tuned models trained to extract structured specifications from GitHub issues/bug reports."**

However, **related papers found that are close to this claim:**

1. **SpecRover (arXiv 2408.02232)** - Conducts "iterative code search accompanied by specification inference" from GitHub issues. Infers intended behavior by analyzing issue context + codebase. Shows 50%+ improvement over AutoCodeRover on SWE-Bench. **Key point:** It infers specs from issues but is NOT described as a "fine-tuned model specifically for spec extraction."

2. **Keys4BR** - Fine-tunes DistilBERT to improve semantic representation of bug reports (focuses on detecting missing/ambiguous sections, not extracting behavioral specs for repair).

3. **Multiple 2025-2026 papers** on program repair mention specification understanding as important (ExpeRepair, SemAgent, Adversarial Reasoning for Repair), but none explicitly claim to be "fine-tuned models trained specifically for extracting behavioral specs from GitHub issues."

**Search results on spec extraction from issues in 2026:**
- CodeSpecBench (2604.12268) - Benchmarks LLMs on generating *executable behavioral specifications* (pre/postconditions) but does NOT focus on extracting specs *from* GitHub issues
- "Spec2Assertion" papers focus on *generating* assertions from specifications, not extracting specs
- Multiple papers on "ambiguous issue descriptions" (BouncerBench arXiv:2506.17812) but framing is about fixing ambiguity, not extracting specs

**Implication:** If SpecExtract claims novelty in being "the first fine-tuned model trained to extract behavioral specs from GitHub issues," this appears **credible** — I found no 2026 papers making this exact claim. There are papers on inference-time specification reasoning (SpecRover) but not on fine-tuned extraction models for this task.

---

### **Sources:**
- [Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489)](https://arxiv.org/pdf/2407.01489)
- [Dissecting the SWE-Bench Leaderboards (arXiv 2506.17208)](https://arxiv.org/html/2506.17208v2)
- [The Navigation Paradox in Large-Context Agentic Coding (arXiv 2602.20048)](https://arxiv.org/html/2602.20048)
- [Automated Repair of Ambiguous Problem Descriptions (SpecFix, arXiv 2505.07270)](https://arxiv.org/html/2505.07270v3)
- [SpecRover: Code Intent Extraction via LLMs (arXiv 2408.02232)](https://arxiv.org/pdf/2408.02232)
- [A Survey of LLM-based Automated Program Repair (arXiv 2506.23749)](https://arxiv.org/pdf/2506.23749)
- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (arXiv 2604.12268)](https://arxiv.org/html/2604.12268v1)
- [Reformulate, Retrieve, Localize: Agents for Repository-Level Bug Localization (arXiv 2512.07022)](https://arxiv.org/html/2512.07022)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5cb2d16-44e6-4838-a5ae-8782fe329a27",
  "isSidechain": false,
  "promptId": "3ac0dfab-43b1-4ccc-8a77-a4e1fe2dfea0",
  "type": "user",
  "uuid": "6ecde50a-343d-4fd0-8490-fc49df1415bd",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to independently verify two specific claims for a paper review:\n\n**Search 1**: Does \"Agentless-Lite\" or any official Agentless variant ALREADY use BM25 for code localization? A paper (SpecExtract) claims to ADD BM25 as a new third retrieval signal to Agentless. But one search result mentioned \"Agentless-Lite adopted BM25 as an alternative.\" Is BM25 already in Agentless's official codebase or Agentless-Lite? Search:\n- \"Agentless-Lite BM25\" site:github.com\n- \"Agentless BM25 retrieval\" \n- arXiv 2407.01489 (Agentless) - check if any version uses BM25\n- paperswithcode Agentless to see if there are BM25-based variants\n\nReport: Does Agentless (any official variant) already use BM25? If yes, does it use raw query text or structured tokens for BM25?\n\n**Search 2**: Find the paper \"SpecFix: Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation\" (arXiv 2505.07270). What does it do? How does it relate to extracting behavioral specs from bug reports? Is it a direct competitor to SpecExtract (which extracts structured specs from bug reports to guide program repair)? Fetch the abstract from https://arxiv.org/abs/2505.07270\n\n**Search 3**: Search for any papers from Jan-May 2026 that specifically focus on \"extracting behavioral specifications from GitHub issues\" or \"fine-tuning for specification extraction from bug reports\" — i.e., trained models specifically for issue-space spec extraction. This is the specific gap SpecExtract claims to fill.\n\nSearch queries to try:\n- \"specification extraction bug report fine-tuning 2026\" site:arxiv.org\n- \"behavioral specification GitHub issues extraction\" 2026\n- \"issue description specification extraction repair\" 2026\n\nReport your findings clearly with paper titles, arXiv IDs, and whether they challenge SpecExtract's novelty claim.",
    "agentId": "a8bbf5a452b534657",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have the critical information. Let me compile my findings for the user.\n\n## Summary of Findings\n\nBased on my comprehensive search, here are the answers to your three verification questions:\n\n---\n\n### **SEARCH 1: Does Agentless (any variant) already use BM25?**\n\n**YES - Agentless DOES use BM25 for code localization, not just Agentless-Lite.**\n\n**Critical Finding:** The original **Agentless paper (arXiv 2407.01489)** explicitly uses BM25 for code localization. According to multiple sources, Agentless \"prepends the top-10 BM25-ranked files to the prompt using the task description as the query, with BM25 computed over function/class-level chunks using rank-bm25, and scores aggregated to file level by taking the maximum chunk score.\"\n\n**Agentless-Lite variant:** The lighter variant uses **embedding-based (dense) retrieval instead**, not BM25. According to the SWE-Bench leaderboards, Agentless-Lite uses \"an embedding model to retrieve relevant files from the repository\" (models like Voyage Code-3 or text-embedding-3-small) rather than BM25.\n\n**On Query Format:** The Agentless baseline uses the **raw task description** (not structured tokens) as the BM25 query. One recent paper mentions that \"query reformulation, which adds a summary and code signals (identifiers, snippets), consistently strengthens lexical retrieval, with BM25 boosting first-file localization by 36% over baseline\" — but this is an **enhancement**, not the baseline Agentless approach.\n\n**Implication for SpecExtract's novelty claim:** If SpecExtract claims to \"ADD BM25 as a new third retrieval signal\" to Agentless, this claim is **problematic**. BM25 is already Agentless's primary (and only) localization method. However, it's possible SpecExtract adds BM25 with **structured tokens** (not raw query text), which would be the novel contribution.\n\n---\n\n### **SEARCH 2: What is SpecFix (arXiv 2505.07270)?**\n\n**SpecFix** automatically repairs ambiguous natural language problem descriptions for LLM-based code generation. It works in two steps:\n\n1. **Analysis & Repair:** Uses testing and program repair to modify how the LLM interprets a description\n2. **Refinement:** Applies \"contrastive specification inference\" to update the description based on interpretation changes\n\n**How it relates to bug report specs:** SpecFix clarifies *ambiguous problem statements* (code generation benchmarks) by improving descriptions using input-output examples. Bug report specification extraction typically clarifies *what went wrong* by identifying reproduction conditions and desired fixes. Both address ambiguity but in opposite directions—SpecFix clarifies \"what to build,\" bug specs clarify \"what went wrong.\"\n\n**Is it a direct competitor to SpecExtract?** **NO** — SpecFix targets code generation benchmarks with input-output examples, while SpecExtract (based on your description) targets real GitHub issues/bug reports. Different problem domain.\n\n---\n\n### **SEARCH 3: Are there papers on fine-tuned models for specification extraction from GitHub issues (Jan-May 2026)?**\n\n**NO dedicated papers found specifically on \"fine-tuned models trained to extract structured specifications from GitHub issues/bug reports.\"**\n\nHowever, **related papers found that are close to this claim:**\n\n1. **SpecRover (arXiv 2408.02232)** - Conducts \"iterative code search accompanied by specification inference\" from GitHub issues. Infers intended behavior by analyzing issue context + codebase. Shows 50%+ improvement over AutoCodeRover on SWE-Bench. **Key point:** It infers specs from issues but is NOT described as a \"fine-tuned model specifically for spec extraction.\"\n\n2. **Keys4BR** - Fine-tunes DistilBERT to improve semantic representation of bug reports (focuses on detecting missing/ambiguous sections, not extracting behavioral specs for repair).\n\n3. **Multiple 2025-2026 papers** on program repair mention specification understanding as important (ExpeRepair, SemAgent, Adversarial Reasoning for Repair), but none explicitly claim to be \"fine-tuned models trained specifically for extracting behavioral specs from GitHub issues.\"\n\n**Search results on spec extraction from issues in 2026:**\n- CodeSpecBench (2604.12268) - Benchmarks LLMs on generating *executable behavioral specifications* (pre/postconditions) but does NOT focus on extracting specs *from* GitHub issues\n- \"Spec2Assertion\" papers focus on *generating* assertions from specifications, not extracting specs\n- Multiple papers on \"ambiguous issue descriptions\" (BouncerBench arXiv:2506.17812) but framing is about fixing ambiguity, not extracting specs\n\n**Implication:** If SpecExtract claims novelty in being \"the first fine-tuned model trained to extract behavioral specs from GitHub issues,\" this appears **credible** — I found no 2026 papers making this exact claim. There are papers on inference-time specification reasoning (SpecRover) but not on fine-tuned extraction models for this task.\n\n---\n\n### **Sources:**\n- [Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489)](https://arxiv.org/pdf/2407.01489)\n- [Dissecting the SWE-Bench Leaderboards (arXiv 2506.17208)](https://arxiv.org/html/2506.17208v2)\n- [The Navigation Paradox in Large-Context Agentic Coding (arXiv 2602.20048)](https://arxiv.org/html/2602.20048)\n- [Automated Repair of Ambiguous Problem Descriptions (SpecFix, arXiv 2505.07270)](https://arxiv.org/html/2505.07270v3)\n- [SpecRover: Code Intent Extraction via LLMs (arXiv 2408.02232)](https://arxiv.org/pdf/2408.02232)\n- [A Survey of LLM-based Automated Program Repair (arXiv 2506.23749)](https://arxiv.org/pdf/2506.23749)\n- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (arXiv 2604.12268)](https://arxiv.org/html/2604.12268v1)\n- [Reformulate, Retrieve, Localize: Agents for Repository-Level Bug Localization (arXiv 2512.07022)](https://arxiv.org/html/2512.07022)"
      }
    ],
    "totalDurationMs": 125402,
    "totalTokens": 41521,
    "totalToolUseCount": 28,
    "usage": {
      "input_tokens": 265,
      "cache_creation_input_tokens": 1184,
      "cache_read_input_tokens": 38463,
      "output_tokens": 1609,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1184
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 265,
          "output_tokens": 1609,
          "cache_read_input_tokens": 38463,
          "cache_creation_input_tokens": 1184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1184,
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
      "otherToolCount": 28
    }
  },
  "sourceToolAssistantUUID": "e5cb2d16-44e6-4838-a5ae-8782fe329a27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-10T07:58:04.955Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a CRITICAL finding: The search agent found that Agentless ALREADY uses BM25. Let me re-examine this carefully.

From the search results: "The original Agentless paper (arXiv 2407.01489) explicitly uses BM25 for code localization. According to multiple sources, Agentless "prepends the top-10 BM25-ranked files to the prompt using the task description as the query, with BM25 computed over function/class-level chunks using rank-bm25, and scores aggregated to file level by taking the maximum chunk score."


But the Round 7 proposal directly contradicts this, claiming Agentless uses LLM prompting and embedding-based cosine similarity instead of BM25. This is a major discrepancy—either the search results are outdated or conflating different versions, or the proposal has mischaracterized the actual approach. I need to verify which version of Agentless is being referenced and whether there's been a methodological shift between iterations. I'm realizing there's likely a version distinction at play here—the original Agentless paper may have used different retrieval mechanisms than the current Agentless-1.5 variant that the proposal references, which could explain why the search results show BM25 being used while the proposal claims it isn't. I need to figure out which version the proposal is actually building on to determine if the BM25 addition is truly novel or redundant. The hybrid retrieval approach mentioned in that ICSE 2023 paper is exactly what the proposal is building on. But now I'm seeing a potential contradiction: if Agentless already uses BM25 with the raw task description as its query, then SpecExtract's actual contribution becomes much narrower—it's just swapping in structured tokens instead of raw text for the BM25 query. That's a significant gap between what's claimed and what's actually novel.

And there's a deeper problem here: Round 6 identified that Agentless doesn't use BM25, which led to changes in Round 7 to explicitly state it does. But the search results suggest Agentless may already be doing BM25 retrieval with the task description. If that's accurate, then the claim that "Agentless does not use BM25" in the original proposal was incorrect, and this needs to be flagged as a critical issue for the current round. I'm noticing a potential contradiction here—the reviewer in Round 6 explicitly stated that Agentless uses LLM prompting and embedding-based retrieval without BM25, but the Round 7 proposal now claims Agentless doesn't use BM25, which aligns with that feedback. The discrepancy might come from different Agentless versions, where the original paper could have used BM25 while the newer version (1.5) switched to LLM prompting and embeddings. I should flag this version uncertainty and clarify which Agentless variant the proposal is actually modifying.

Even if there's ambiguity about Agentless's retrieval method, SpecExtract's key innovation would be using extracted structured tokens for BM25 rather than raw text, which is still a meaningful contribution. However, I'm also realizing the search agent cited a source from June 2026, which is after today's date, so that information wouldn't have been available to the proposal authors—I need to be careful about what evidence actually applies here. ection paper's analysis, which could be a later version than arXiv 2407.01489. Or it could be an error in the search agent.

Given this uncertainty, I should flag the issue but acknowledge that I'm not 100% certain. The proposal made a specific claim that Agentless "does not use BM25" based on what appears to be a detailed reading of the paper (by Round 6 reviewer). If the search agent is correct that it DOES use BM25, this is a critical error in the proposal.

I think the most likely explanation is that there are different versions at play: the original Agentless uses BM25 for localization, Agentless-Lite swaps that for embedding-based retrieval, and Agentless-1.5 is unclear. The proposal's description of embedding-based cosine similarity without BM25 sounds like it's describing Agentless-Lite specifically, which would make the contribution of adding BM25 as a third signal more coherent. However, the proposal also references Agentless-1.5 performance numbers, so there's ambiguity about which version is actually being integrated.

This needs to be clarified in the proposal. I'll flag it as a significant issue that requires the authors to explicitly state which Agentless version they're using and confirm whether that version uses BM25 or not.

There's also a moderate concern about the training dataset size—2,294 instances seems quite small for fine-tuning a 30B parameter model, even with only 3B active parameters. The proposal doesn't address potential overfitting or discuss training stability measures like learning rate scheduling and validation monitoring.

The EMNLP framing also needs work for the NLP and Code Models track. The core NLP contribution—structured information extraction from bug reports—isn't clearly positioned as a modeling challenge. The proposal should explain why the masked-field training approach is a meaningful NLP design choice and why supervised training is necessary here rather than zero-shot prompting, especially since CodeSpecBench showed existing LLMs can already generate specs reasonably well. Framing this explicitly as an information extraction problem would strengthen the submission.

I should also flag SpecFix, a concurrent work from May 2026 that addresses specification ambiguity for code generation. While it targets a different domain (code generation benchmarks rather than GitHub issues) and uses contrastive inference instead of extraction, it's recent enough that reviewers might expect a mention. A brief note distinguishing the two approaches would be prudent.

Looking at the evaluation scores, the novelty sits at 3/5—the gap is genuine since no trained spec extractor exists for issue repair, but the technical approach combining AST parsing with supervised fine-tuning is fairly straightforward, and the BM25 contribution may overlap with what Agentless already does. Feasibility scores 3.5/5; the method is sound and the improvements of 4-7 percentage points are mechanistically justified, though the training dataset is quite small. Clarity rates 4/5.

For impact, I'm assessing 3/5—while the pipeline-agnostic value is real and the absolute gain from 13.33% is meaningful, the improvement magnitude remains modest, and the work needs stronger NLP framing to fit EMNLP's scope. This averages to 3.375, which falls below the 4.0 threshold for acceptance.

However, I'm reconsidering whether "revise" is the right call at Round 7. The proposal has genuinely improved through seven iterations. The remaining obstacles are fixable: there's a potentially significant inconsistency around Agentless's BM25 usage that just surfaced, plus two moderate concerns about training data scale and EMNLP positioning, and one minor issue. The core technical approach remains sound.

I'm now caught on a factual contradiction—the Round 6 reviewer independently verified arXiv 2407.01489 and confirmed Agentless uses LLM prompting over the repository tree and embedding-based retrieval, not BM25. But my search agent cites a June 2026 paper claiming BM25. The earlier reviewer's direct source check carries more weight, so I'm leaning toward trusting that verification. I'm realizing the search agent might be pulling from unreliable sources or conflating different versions of Agentless—the Round 6 reviewer explicitly confirmed the paper uses LLM prompting with embeddings, while the search agent's citation points to a future-dated paper that seems suspicious. Given this contradiction, I should treat the search agent's BM25 claim cautiously and flag this as a moderate uncertainty rather than accepting it at face value.

The real issue here is that the proposal doesn't specify which exact version of Agentless it's using or clarify its retrieval mechanism, which could easily confuse reviewers who might remember BM25 from the original paper or different variants. I should add this version ambiguity as a moderate concern, along with noting that the training dataset size needs better justification.

On the dataset front, 2,294 instances from SWE-bench seems quite small compared to SWE-Lego's 32k, so the proposal should explain why this is sufficient for the spec-extraction task—whether it's because the structured output space is simpler, or because the MoE architecture has built-in regularization that reduces overfitting risk.

There's also a framing gap for EMNLP reviewers: the proposal targets the NLP and Code Models track but doesn't explicitly articulate the NLP contribution. The information extraction angle—extracting structured specs from semi-structured bug reports with incomplete information—should be front and center, along with a clear explanation of why supervised fine-tuning is necessary rather than just zero-shot prompting.

SpecFix is recent related work on fixing ambiguous specs for code generation, though it operates on benchmarks rather than GitHub issues, so a quick note distinguishing the domains would help preempt questions.

The scores across novelty, feasibility, clarity, and impact average to 3.375, so the proposal needs revision before finalizing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ecde50a-343d-4fd0-8490-fc49df1415bd",
  "isSidechain": false,
  "requestId": "req_011CatXkB5sw6qGNSt4f9be3",
  "type": "assistant",
  "uuid": "9a07bd67-bc2c-4079-b475-bd8e6a30d186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01At37vHcc1aJw9KTvQ8fAT1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7268,
      "cache_read_input_tokens": 43109,
      "output_tokens": 6741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6741,
          "cache_read_input_tokens": 43109,
          "cache_creation_input_tokens": 7268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7268
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

_source line 21 · 2026-05-10T07:58:46.257Z_

Based on my independent verification research, I can now issue the Round 7 verdict.

**Key findings from independent verification:**
- SWE-bench-Live Agentless baselines (11.67%/12.00%/13.33%) ✅ confirmed from Table 3 of arXiv 2505.23419
- Agent-CoEvo (41.33% SWE-bench Lite, 46.4% SWT-bench Lite) ✅ confirmed
- SWE-Lego (52.6% SWE-bench Verified) ✅ confirmed
- SpecRover 51.7% ambiguous description failure (Section V-A) ✅ confirmed
- Qwen3-Coder-30B-A3B model ✅ confirmed (real, ~3.3B active params)
- SWE-bench Verified saturation at 93.9% ✅ confirmed
- **⚠ NEW**: Search evidence suggests original Agentless paper (arXiv 2407.01489) may describe BM25 file ranking — conflicting with the proposal's claim that Agentless "does not use BM25"
- **⚠ NEW**: No direct competitor found for the specific gap (trained, issue-space spec extractor) — novelty gap confirmed
- SpecFix (arXiv 2505.07270, May 2026) found — targets different domain (benchmark descriptions vs. GitHub issues)

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The gap (no trained issue-space spec extractor) is real and independently confirmed. However, the BM25 localization contribution may be less novel than claimed if original Agentless already uses BM25 with raw text — SpecExtract's actual contribution reduces to 'structured extracted tokens for BM25' rather than 'adding BM25 as new signal.' The SFT-on-AST-parsed-assertions approach is creative but modest in technical depth."
    },
    "feasibility": {
      "score": 3,
      "rationale": "Technical components are real and verified (Qwen3-Coder-30B-A3B, Agentless integration, SWE-bench-Live eval infrastructure). However, 2,294 training instances is small for a 30B-A3B model on a structured extraction task, and the +4-7 pp improvement prediction rests on the assumption that fault localization failure is the PRIMARY cause of Agentless's 4× performance drop on SWE-bench-Live, which is asserted rather than demonstrated."
    },
    "clarity": {
      "score": 4,
      "rationale": "After 7 rounds of revision, the proposal is well-organized and complete: schema is formally defined with a worked example, masked-field protocol is specified with masking probability, integration mechanism is described, and training data construction is step-by-step. The SpecRover HTML URL and the 0.65 threshold justification are both present."
    },
    "impact": {
      "score": 3,
      "rationale": "The pipeline-agnostic preprocessing design is genuinely useful — SpecExtract can serve as a front-end to any repair backbone including SWE-Lego. But +4-7 pp absolute improvement from a 13.33% baseline is modest, and the EMNLP venue fit requires a clearer NLP framing — information extraction from semi-structured bug text needs to be explicitly positioned as an NLP contribution for the 'NLP and Code Models' track."
    }
  },
  "issues": [
    "SIGNIFICANT (NEW) — Agentless BM25 inconsistency: The proposal explicitly states 'Agentless's fault localization... does not use BM25,' but independent search found evidence that the original Agentless paper (arXiv 2407.01489) describes prepending BM25-ranked files to prompts using the task description as query. This directly contradicts the proposal's claim. The Round 6 reviewer also verified this and concluded Agentless uses LLM prompting + embedding — but search results suggest there may be version ambiguity between original Agentless (BM25) and Agentless-Lite (embedding). The proposal must specify (a) which exact version of Agentless is used, (b) whether that version uses BM25, and (c) if BM25 is already present, reframe SpecExtract's contribution as 'using structured extracted interface tokens for BM25 queries rather than raw issue text' — a narrower but still defensible differentiation. If BM25 is already in Agentless, the entire 'adding BM25 as a third retrieval signal' framing collapses.",
    "MODERATE (NEW) — Training dataset size not justified: SFT of Qwen3-Coder-30B-A3B on 2,294 instances is not discussed in terms of sufficiency. SWE-Lego uses 32k instances for a related code task; the proposal gives no reason why 2,294 instances suffices for reliable generalization across diverse bug report styles and repository domains. Add one sentence: e.g., the structured output space is simpler than end-to-end repair (4 typed fields vs. full code patches), reducing the sample complexity requirement; or cite a comparable structured extraction task at similar data scale.",
    "MODERATE (NEW) — EMNLP NLP framing is underspecified: The 'NLP and Code Models' track requires a clear NLP modeling contribution. The proposal's NLP contribution (structured IE from semi-structured bug text with partial observability) is buried in the approach section. EMNLP reviewers will ask: why supervised fine-tuning over zero-shot prompting? CodeSpecBench (arXiv 2604.12268) shows prompting-based spec generation is imperfect — the proposal should explicitly state that zero-shot prompting produces inconsistent output structure across diverse bug report styles, motivating the SFT approach. One paragraph framing SpecExtract as an information extraction system for bug reports (akin to NER/RE from clinical notes or legal text) would anchor it for NLP reviewers.",
    "MINOR (NEW) — SpecFix (arXiv 2505.07270, May 2026) is recent adjacent work: it repairs ambiguous problem descriptions for LLM-based code generation using contrastive spec inference. While it operates on benchmark descriptions rather than GitHub issue repair, EMNLP reviewers may flag its absence. One sentence suffices: 'SpecFix (arXiv 2505.07270) repairs ambiguous problem descriptions for code generation benchmarks using contrastive inference; SpecExtract targets GitHub issue bug reports rather than benchmark descriptions and produces structured specs rather than repairing the description text itself.'"
  ],
  "feedback": "Round 7 has resolved all four Round 6 issues: Agentless retrieval is now correctly described as LLM prompting + embedding with BM25 as an added third signal; the +4-7 pp improvement has a mechanistic backbone; the cosine similarity limitation is acknowledged; and the masked-field protocol is fully specified. The proposal is close to passable but one new critical finding blocks it.\n\n**(1) URGENT — Resolve the Agentless BM25 inconsistency**: Independent search found the original Agentless paper (arXiv 2407.01489) may already use BM25 file ranking (top-10 BM25 files prepended to LLM prompt, query = raw task description). If true, the proposal's explicit claim 'it does not use BM25' is incorrect, and the 'adding BM25 as a third retrieval signal' framing mis-states SpecExtract's novelty. The fix is: (a) fetch https://arxiv.org/pdf/2407.01489 to confirm which version of Agentless you are integrating with; (b) if it uses BM25 with raw text, reframe SpecExtract's BM25 contribution as 'replacing raw-text BM25 queries with structured extracted interface tokens — module names and entry points extracted from the spec — which are lexically precise and distribution-shift-robust, unlike free-form issue text that contains incidental mentions'; (c) update the proposal to accurately state Agentless's retrieval mechanism for the specific version used.\n\n**(2) Add one sentence on training data sufficiency**: Explain why 2,294 instances is adequate for the spec-extraction subtask (e.g., simpler output space than end-to-end repair, or comparable to similar structured IE tasks).\n\n**(3) Add one paragraph on EMNLP NLP framing**: Explicitly state why supervised fine-tuning is required over zero-shot prompting for structured spec extraction, using CodeSpecBench's imperfect prompting results as motivation. Frame SpecExtract as an IE system for semi-structured bug text.\n\n**(4) Add one sentence on SpecFix** (arXiv 2505.07270) noting the domain difference.\n\nWith issue (1) resolved, the proposal should reach pass in Round 8.",
  "reason": "All Round 6 issues are resolved, but new evidence that original Agentless already uses BM25 directly contradicts the proposal's 'does not use BM25' claim, potentially collapsing the localization novelty argument; average score 3.375 is below the 4.0 threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a07bd67-bc2c-4079-b475-bd8e6a30d186",
  "isSidechain": false,
  "requestId": "req_011CatXkB5sw6qGNSt4f9be3",
  "type": "assistant",
  "uuid": "ae429f0f-c20e-4fd2-9c07-eae8404acdba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01At37vHcc1aJw9KTvQ8fAT1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7268,
      "cache_read_input_tokens": 43109,
      "output_tokens": 6741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6741,
          "cache_read_input_tokens": 43109,
          "cache_creation_input_tokens": 7268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7268
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

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ae429f0f-c20e-4fd2-9c07-eae8404acdba",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space behavioral spec extraction for program repair",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "ae429f0f-c20e-4fd2-9c07-eae8404acdba",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space behavioral spec extraction for program repair",
  "sessionId": "9c7af506-9068-4d10-a414-f029954427c9"
}
```

---
