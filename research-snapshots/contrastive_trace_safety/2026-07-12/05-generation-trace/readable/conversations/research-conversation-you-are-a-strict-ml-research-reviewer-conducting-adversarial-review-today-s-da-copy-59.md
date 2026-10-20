# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/9441f046-d0fc-42fd-a7f5-74a8892b6232.jsonl`
- **Structured JSON:** [`e95f1e2723f5e1c10741.json`](../../sessions/e9/e95f1e2723f5e1c10741.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:21:03.046Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:21:03.046Z",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 9/10)\n{\n  \"title\": \"SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair\",\n  \"core_problem\": \"Automated repair agents fail on ambiguous bug reports not from lack of code understanding, but because unstructured issue text leaves behavioral expectations underspecified — what interface should change, what the user observed, and what correct behavior looks like are rarely made explicit. SpecRover (ICSE 2025) partially addresses this via per-instance LLM prompting that extracts specifications from CODE during codebase traversal, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue. Its error analysis (Section V-A, 'Reasons for Failure'; see https://arxiv.org/html/2408.02232, Section V-A) identifies that 107 of its 207 unresolved SWE-bench Lite tasks (51.7%) are classified as 'ambiguous issue description' — cases the paper characterizes as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for why underspecified descriptions constitute an irreducible failure mode for code-space approaches. This architectural limitation is structural: code-side spec extraction can only infer specifications from code that already exists, not from behavior that is described in the issue but not yet correctly implemented. Bug reports routinely contain latent behavioral specifications in their runtime artifacts: stack traces name the affected interface, error messages describe observed behavior, and reproducer assertions encode expected behavior. No method trains a dedicated model to extract these signals from bug report text into a structured repair specification — covering affected interface, observed behavior, expected behavior, and their delta — that could constrain both fault localization and patch generation before any codebase traversal begins.\",\n  \"opportunity\": \"Failing test assertions in SWE-bench's test patches encode implementation-agnostic behavioral specifications without revealing implementation strategies: `assert result == expected_value` or `with pytest.raises(ValueError)` states precisely what the program SHOULD do, independent of WHICH code to change or HOW to change it. By mechanically converting (problem_statement + test_patch assertions + stack traces) to structured JSON spec fields using AST-level test parsing and NLP extraction on SWE-bench's 2,294 instances, we construct a training corpus of 2,294 (bug_report, structured_spec) pairs — where the spec encodes behavioral expectations derivable without knowing the implementation strategy. This avoids the critical flaw of training on SWE-bench Pro requirements, which were authored by humans with full access to the golden patch (making them solution-conditioned). SWE-bench-Live (NeurIPS 2025, arXiv 2505.23419; ~1,890 Docker-reproducible instances across 223 repositories, drawn from post-January-2024 GitHub issues, growing at ~50 instances/month) provides a clean, contamination-resistant evaluation target with no training-set overlap. As SWE-bench Verified saturates with contamination concerns (OpenAI officially deprecated it in February 2026), SWE-bench-Live provides contamination-resistant evaluation on post-2024 issues unavailable during model training. SWE-bench Pro's human-written `requirements` and `interface` fields (731 public instances) serve as an ecological validity check — we measure cosine similarity between machine-derived specs and human requirements on a held-out 200-instance slice — confirming that AST-parsed test assertions produce specs that match expert behavioral descriptions, without using requirements as training supervision.\",\n  \"landscape\": \"SpecRover (ICSE 2025, arXiv 2408.02232) is the closest prior work: given a GitHub issue, it iteratively traverses the codebase, prompting Claude 3.5 Sonnet to extract function-level summaries from visited code, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue and 31% on SWE-bench Lite (93/300). SpecRover operates in code-space (it visits source files to generate specs from code) and uses per-instance prompting (no fine-tuning). Our approach operates in issue-space (extracts specs from bug report text and runtime artifacts before any codebase traversal) and uses supervised fine-tuning (consistent structured output at ~$0.05-0.10/issue). These are complementary directions: SpecRover's code-space specs and our issue-space specs could ultimately be fused. Agent-CoEvo (arXiv 2604.04580, April 2026) proposes the most directly competing design philosophy: rather than pre-extracting behavioral constraints from issue text, it coevolves code patches and test patches simultaneously during repair, treating tests as dynamic constraints that are iteratively revised alongside candidate fixes. Agent-CoEvo achieves 41.33% on SWE-bench Lite (DeepSeek-V3) and 46.4% on SWT-bench Lite, outperforming Agentless-1.5 (32%) on those benchmarks. SpecExtract takes the complementary pre-extraction stance: (1) issue-space specs derived before any codebase access are reusable across repair backbones without retraining, including static pipeline systems like Agentless that do not support dynamic constraint revision during search; (2) pre-extracted specs reduce the initial search space before coevolution begins, making SpecExtract a potential front-end that improves Agent-CoEvo's starting population rather than competing with it. RGFL (arXiv 2601.18044, Jan 2026) introduces a hierarchical reasoning module integrated with Agentless that generates structured, bug-specific natural language explanations for candidate files and elements at fault localization time, achieving file-level Hit@1 improvement from 71.4%→85%, element-level Exact Match under top-3 files from 36%→69%, and a 12.8% end-to-end repair success improvement on SWE-bench Verified. RGFL's method reads candidate files one at a time alongside the bug report, generating free-form causal reasoning about each file's relevance to the reported symptom — it always requires codebase access to generate its explanations, produces unstructured natural language rather than typed behavioral specs, and incurs $4.4/instance cost (3.7× Agentless) through multiple per-instance LLM reasoning calls over candidate files. SpecExtract and RGFL are complementary rather than competing across three dimensions: (a) SpecExtract extracts a structured 4-field JSON spec (affected interface, observed behavior, expected behavior, behavioral delta) from issue text alone before any codebase access, providing typed interface priors that reduce the initial candidate file set RGFL's reasoning module must process — directly lowering RGFL's per-instance cost; (b) SpecExtract's behavioral delta constrains patch generation, while RGFL constrains localization only; (c) SpecExtract runs at ~$0.05-0.10/instance (single SFT forward pass) versus RGFL's $4.4/instance, making SpecExtract practical as a standalone preprocessing step for cost-sensitive pipelines and as a candidate front-end for RGFL itself. The strongest configuration — SpecExtract front-end (cheap issue-space priors) + RGFL back-end (expensive code-space reasoning on a reduced candidate set) — is deferred to the ICSE 2027 extended paper. SWE-Fixer (ACL Findings 2025, aclanthology.org/2025.findings-acl.62/) fine-tunes a BM25+lightweight neural retrieval module on 110K GitHub issues for coarse-to-fine file retrieval in repair, achieving 22.0%/30.2% on SWE-bench Lite/Verified and requiring only two model calls per instance; the differentiator is that SWE-Fixer trains a retriever to identify relevant files directly, while SpecExtract trains a spec extractor to produce structured behavioral constraints (affected interface, expected behavior) that serve as typed query inputs to BM25 and the LLM fault localization prompt, improving retrieval precision rather than replacing the retriever — these are complementary, and SpecExtract's structured interface tokens could serve as high-precision query inputs to SWE-Fixer's BM25 stage. SWE-Lego (arXiv 2601.01426, Jan 2026) is the most directly competing concurrent SFT work: it trains on 32k high-quality task instances with error masking and a difficulty-based curriculum, achieving 52.6% on SWE-bench Verified (58.8% with test-time scaling at 16 samples) using a 32B model. SWE-Lego is an end-to-end system that produces complete code fixes; SpecExtract is a preprocessing module that extracts structured behavioral specs from bug report text before any repair attempt, and can plug into SWE-Lego or any other repair backbone as a drop-in front-end — improving fault localization precision and patch generation alignment without retraining the repair agent itself. CodeSpecBench (arXiv 2604.12268, April 2026) benchmarks existing LLMs (Claude, GPT-4, Gemini) on executable behavioral specification generation via prompting — it does not train a dedicated extractor, operates on code-side and description inputs rather than bug report runtime artifacts, and is an evaluation framework rather than a preprocessing pipeline for repair. Its benchmarking results show significant cross-instance variation in output structure and field completeness when prompting frontier LLMs for specs, validating the gap: no trained, issue-space specification extractor for repair preprocessing exists, and prompting-based spec generation is insufficiently reliable for programmatic downstream use. SpecFix (arXiv 2505.07270, May 2026) repairs ambiguous problem descriptions for LLM-based code generation benchmarks (HumanEval+, MBPP+, LiveCodeBench) via contrastive specification inference — analyzing the distribution of LLM-generated programs to identify and repair description ambiguity; SpecExtract operates on GitHub issue bug reports (not synthetic benchmark descriptions), produces structured 4-field JSON specs via supervised fine-tuning (not description repair), and serves as a preprocessing input to repair agents rather than modifying task descriptions. VibeRepair (arXiv 2602.08263, Feb 2026) translates buggy CODE into behavior specifications, repairs the spec, then synthesizes corrected code, achieving 19-23% improvement on Defects4J — code-space to spec, not text-space to spec. TraceRepair (arXiv 2604.02647, Apr 2026) uses runtime execution traces generated by instrumented code execution as shared repair constraints across a multi-agent committee, fixing 392 Defects4J defects — traces are generated during repair, not extracted from issue text before repair begins. RepoRepair (arXiv 2603.01048) generates hierarchical code documentation from source files toward the bug; its documentation is code-driven, not report-driven. SoRFT (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) fine-tunes on SWE-bench with RL to decompose the repair TASK into subtasks (file → function → line → edit), achieving 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite with a 7B model (30.8% Verified and 24.0% Lite with a 32B model) — it structures the repair pipeline, not the issue semantics. PathFix (arXiv 2510.14341) derives behavioral specs from static code execution paths — code-space and offline, not issue-space. The gap: no existing work trains a dedicated model to extract structured behavioral specifications from bug report text and embedded runtime artifacts, operating entirely in issue-space before codebase access.\",\n  \"approach\": \"We train SpecExtract, a Qwen3-Coder-30B-A3B model (Mixture-of-Experts: 30B total parameters, ~3B active per token — fine-tuning and inference cost scale with active parameters, comparable to a 3B dense model; fits on a single H100 80GB with QLoRA at ~17.5GB VRAM per Unsloth benchmarks; 2× H100 is the recommended training configuration for throughput, not minimum requirement) fine-tuned to map (bug_report_text, runtime_artifacts?) → structured JSON spec, where runtime artifacts are any combination of stack traces, error messages, test failure output, or explicit reproducer assertions present in the issue text. The model gracefully handles varying artifact availability through a masked-field training protocol: training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs. Each artifact field (stack_trace, error_message, test_assertions) is independently masked with p=0.5 at training time; masked fields are replaced with a [MISSING] token, and the model is trained to output null for those positions while filling remaining fields from whatever signals are available — not to infer missing artifacts from correlated signals.\\n\\n**NLP framing — structured IE for bug reports**: SpecExtract's primary NLP contribution is defining and solving a novel structured information extraction (IE) task: extracting typed behavioral specifications from semi-structured bug text under partial observability. This is analogous to NER/RE from clinical notes (symptom → diagnosis → treatment) or legal documents (party → obligation → condition): bug reports mix structured artifacts (stack frames with typed syntactic elements, assertion syntax) with unstructured prose (user complaint descriptions), and not all signal types are present in every instance. Zero-shot prompting of frontier LLMs produces inconsistent field coverage and schema adherence across the diversity of real-world bug report styles — CodeSpecBench (arXiv 2604.12268) benchmarks Claude, GPT-4, and Gemini on spec generation via prompting and documents significant cross-instance variation in output structure and field completeness, motivating a dedicated trained extractor with enforced schema. Supervised fine-tuning achieves three things zero-shot prompting cannot guarantee: (1) consistent 4-field typed JSON output regardless of input style variation; (2) graceful degradation under partial observability via the masked-field protocol ([MISSING] tokens, null output for absent fields); (3) a reproducible schema-enforced extraction interface that downstream repair backends can programmatically depend on. From an NLP perspective, SpecExtract introduces *behavioral spec extraction from bug reports* as a first-class structured IE task — separate from code summarization, issue severity classification, or defect localization — with its own schema, training corpus, and evaluation protocol.\\n\\n**Formal schema**: Each spec has four typed fields — (1) `affected_interface`: {module: str, signature: str|null, entry_point: str} extracted from stack frame function names and explicitly mentioned APIs; (2) `observed_behavior`: {error_type: str|null, error_message: str|null, symptom: str} from error output and user complaint; (3) `expected_behavior`: {description: str, assertions: [str]} as natural-language description plus test-style constraint strings when derivable; (4) `behavioral_delta`: str, a one-sentence expected-vs-actual summary. Worked example for a NumPy issue 'linalg.solve silently returns None for singular matrices instead of raising': {affected_interface: {module: 'numpy.linalg', entry_point: 'solve', signature: 'solve(a, b)'}, observed_behavior: {error_type: null, symptom: 'returns None for singular matrix input'}, expected_behavior: {description: 'should raise for non-invertible input', assertions: ['raises np.linalg.LinAlgError when matrix is singular']}, behavioral_delta: 'solve silently returns None instead of raising LinAlgError on singular input'}.\\n\\n**Training data construction (implementation-agnostic behavioral specifications)**: From SWE-bench full (2,294 instances including Verified 500 and the broader set): (1) parse `test_patch` test functions via Python AST to extract formal assertions — pytest.raises calls → error_type, assert statements → expected_behavior.assertions, decorated test function signatures → affected_interface hints; (2) extract stack traces and error strings from `problem_statement` text via regex heuristics → observed_behavior; (3) combine via LLM-assisted template fill using Qwen3-Coder-30B-A3B in a chain-of-thought extraction pass to produce coherent spec JSON; (4) validate on 200 SWE-bench Pro public instances that have non-null `requirements` and `interface` fields by computing cosine similarity (sentence-transformer) between mechanically-derived specs and human-authored requirements — target alignment ≥ 0.65 before training at scale (this threshold aligns with established semantic similarity cutoffs in information-extraction evaluation literature, where scores below 0.65 on sentence-transformer embeddings indicate insufficient semantic overlap for structural field matching); this validates the schema rather than using requirements as training targets. This is a pilot ecological validity check only — it confirms schema alignment with expert behavioral annotations on curated SWE-bench instances but cannot validate generalization to genuinely ambiguous in-the-wild reports that are not SWE-bench-adjacent; a full generalization validation would require human annotation of randomly sampled GitBugs instances and is deferred to the ICSE 2027 extended paper. Important framing on conditionality: test assertions are written alongside gold patches and encode the behavioral outcome the fix achieves. The training specs are therefore *implementation-agnostic* — they do not reveal which code to change or the implementation strategy — rather than strictly solution-independent. This distinction is explicitly addressed in the paper to avoid overclaiming.\\n\\n**Training data sufficiency**: The 2,294-instance corpus is appropriate for this structured extraction subtask. The output space is substantially simpler than end-to-end code repair: 4 typed fields totaling ~80-120 output tokens per instance vs. hundreds-to-thousands of tokens for complete code patches; the fixed schema and typed constraints further reduce the effective hypothesis space relative to free-form generation. Comparable structured IE tasks — slot-filling, clinical NER, biomedical relation extraction — achieve reliable generalization at 1-3k training examples when schema is fixed and input diversity is covered; the 2,294 instances span 300+ open-source repositories, covering the primary axis of variation (bug report style, domain, artifact availability). Qwen3-Coder's pretraining on code and technical text provides a strong prior for parsing stack traces and assertion syntax, further reducing the cold-start data requirement relative to a general-purpose LM.\\n\\nThe EMNLP 2026 ARR submission uses the 2,294-instance SWE-bench full corpus as the SFT training set; GitBugs augmentation (~3,000 pseudo-labeled instances, yielding a ~5,300-instance total corpus) is reserved for the ICSE 2027 extended paper.\\n\\n**Differentiation from SpecRover**: (1) issue-space — no codebase traversal needed at spec extraction time; (2) supervised learning — consistent, typed JSON output from a single forward pass (~$0.05-0.10/issue) vs. SpecRover's multi-step code traversal ($0.65/issue); (3) directly targets SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved SWE-bench Lite tasks) by conditioning on all available runtime artifacts in the issue, not just the code side.\\n\\n**Integration with Agentless**: We integrate with Agentless (arXiv 2407.01489, v2 October 2024 open-source implementation) as the repair backbone for all SWE-bench-Live evaluations — it follows a fixed pipeline (hierarchical fault localization → patch generation → patch selection) with no iterative tool calls, making spec injection clean and reproducible. Confirmed from the Agentless paper's method section: the main fault-localization pipeline combines (a) LLM prompting over the repository folder tree to identify the top-N suspicious files and (b) embedding-based cosine similarity retrieval (OpenAI text-embedding-3-small via LlamaIndex) over code chunks — the union of both signal sets provides the candidate file list. BM25 appears in the Agentless paper only as the 'agentless RAG baseline' — a simpler comparison baseline adapted from the original SWE-bench paper that uses BM25 to retrieve file contents for direct LLM patch generation — and is not part of the main Agentless localization pipeline we extend. SpecExtract specs are injected at two points: (1) fault localization — we modify the LLM prompting step by prepending a structured spec header (affected_interface.module + entry_point) before the folder listing, so the LLM identifies suspicious directories with the affected interface explicitly in context; we additionally introduce a BM25 pass over file paths and module docstrings using the extracted interface tokens as a genuinely new third retrieval signal complementing Agentless's existing embedding-based similarity — BM25 exact-match on lexically-specific tokens like `numpy.linalg` or `django.db.models.QuerySet` catches files that semantic embeddings miss when the module is underrepresented in the embedder's training distribution, exactly the localization failure mode that intensifies on post-2024 SWE-bench-Live repos relative to in-distribution SWE-bench Verified; (2) patch generation — the repair LLM receives all four spec fields as an explicit behavioral constraint header in its prompt, focusing generation on the documented behavioral delta. Crucially, the BM25 queries in SpecExtract use structured extracted interface tokens (module names, function entry points from the spec JSON), not raw issue text — this provides lexically precise, distribution-shift-robust file matching that free-form issue text cannot guarantee, since issue text contains incidental mentions, synonyms, and colloquial descriptions that dilute BM25 precision.\\n\\n**Agentless baseline on SWE-bench-Live**: Per the SWE-bench-Live paper (arXiv 2505.23419, Table 3), Agentless resolves 11.67% (GPT-4o), 12.00% (GPT-4.1), and 13.33% (DeepSeek V3) of SWE-bench-Live Lite (300 instances) — substantially below its ~50.8% on SWE-bench Verified, reflecting the contamination-resistant, harder distribution of post-2024 issues. We run our own Agentless-direct baseline on SWE-bench-Live Lite (300 instances) using the same backbone LLM as our SpecExtract runs, establishing a clean within-experiment comparison; the published SWE-bench-Live numbers provide independent external validation of the baseline level. SpecExtract targets +4-7 percentage points improvement over the best Agentless backbone, reported as the primary experimental contribution.\\n\\n**Mechanistic case for the +4-7 pp improvement target**: RGFL (arXiv 2601.18044) achieves +12.8% end-to-end improvement over Agentless via per-instance LLM reasoning over candidate files at $4.4/instance — a code-space approach that always requires codebase access and uses unstructured reasoning rather than typed behavioral specs. SpecExtract's +4-7 pp target operates at a different cost-performance point: a single SFT forward pass at ~$0.05-0.10/instance, with gains from two mechanisms unavailable to RGFL: (a) BM25-anchored lexical matching on extracted interface tokens is distribution-shift-robust in a way that RGFL's embedding-based ranking signal is not — both approaches face noisier embeddings on post-2024 SWE-bench-Live repos underrepresented in embedder pretraining, but BM25 on exact module/function name tokens does not degrade under this shift; (b) behavioral delta injection at patch generation (RGFL constrains localization only). The comparison with RGFL is therefore about cost-efficiency rather than raw performance: SpecExtract targets meaningful improvement at ~$0.05-0.10/instance vs. RGFL's $4.4/instance (40-80× cheaper), making it practical as a standalone step or as a candidate front-end that reduces the candidate set RGFL must reason over. Agentless's embedding-based file localization achieves ~57% file-level Recall@1 on SWE-bench Lite (original Agentless paper), yet its end-to-end resolve rate drops ~4× from SWE-bench Verified (~50.8%) to SWE-bench-Live Lite (13.33% best case). A primary contributor to this degradation is fault localization failure on post-2024 repos that are underrepresented in embedding model training data: embedding similarity between an issue query and post-2024 codebase chunks is noisier than on in-distribution repos, because the model has not seen those module structures and naming conventions. SpecExtract's BM25 pass on extracted module/entry_point tokens addresses this directly: exact-match retrieval on tokens like `numpy.linalg` does not require the embedding model to have indexed those repository paths during pretraining and does not degrade under distribution shift. Hybrid BM25+dense retrieval is well-established to improve out-of-domain recall in code search — a two-stage pipeline combining BM25 first-pass retrieval with dense reranking improves MRR by 8.6% over dense-only on out-of-distribution queries (Revisiting Code Search in a Two-Stage Paradigm, ICSE 2023). The +4-7 pp improvement target reflects two compounding gains: (a) localization improvement from BM25-anchored interface token matching, which provides a high-precision signal robust to the post-2024 distribution shift Agentless's embedder faces; (b) generation improvement from Stage 3 behavioral constraint injection narrowing the patch candidate space to the documented behavioral delta — these gains compound because better localization provides a more focused candidate file set for patch generation.\\n\\n**Evaluation**: Primary eval on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues) with Agentless as backbone; per-field ablations independently zero out each spec field to quantify individual contribution to resolve rate. Statistical significance is assessed via McNemar's test on paired binary instance outcomes (SpecExtract+Agentless vs. Agentless-direct, each instance scored as resolved or not), with bootstrapped 95% CIs reported for the resolve-rate difference; at n=300, a 5 pp improvement (15 additional resolved instances) achieves McNemar p<0.05. Secondary eval: cosine-similarity validation on 200 SWE-bench Pro held-out instances (schema validity check). Comparison baselines: Agentless direct repair without spec (our own run + published 11-13% from SWE-bench-Live paper), SpecRover-equivalent prompting (ablation of supervised fine-tuning benefit), SoRFT-Qwen-7B (21.4% Verified / 14.0% Lite, structured subtask decomposition), SWE-Lego (52.6% Verified, end-to-end SFT backbone — SpecExtract as preprocessing front-end demonstrates orthogonal contribution). RGFL (arXiv 2601.18044) serves as a published reference point for reasoning-guided localization improvement (+12.8% on SWE-bench Verified at $4.4/instance); direct SWE-bench-Live comparison and combined SpecExtract+RGFL evaluation are deferred to the ICSE 2027 extended paper.\\n\\n**Publication scope**: The EMNLP 2026 ARR submission (auto-research mode, 6-10 days) reports results on the 2,294-instance SWE-bench full SFT corpus with SWE-bench-Live Lite 300-instance primary eval and a 2-field ablation (affected_interface vs. none, expected_behavior vs. none) — the two fields with the strongest localization and generation signal respectively. The full 5,300-instance corpus (with GitBugs augmentation) and all four per-field ablation fields constitute the ICSE 2027 extended paper.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~90-110 H100-hours (~180-220 A100-equivalent hours)\",\n      \"gpu_breakdown\": \"SFT partition (~10-14 H100-hours): Qwen3-Coder-30B-A3B QLoRA fine-tuning on 5,300 instances, 3 epochs, 2× H100 80GB recommended for throughput (single H100 80GB is technically sufficient at ~17.5GB VRAM) — MoE active-parameter efficiency reduces training cost to ~3B dense equivalent. Eval partition (~80-96 H100-hours): spec extraction inference on 5,300 instances (~4 H100-hours); SWE-bench-Live Lite main eval 300 instances × 12.5 min/instance / 4 parallel H100s ≈ 16 H100-hours; per-field ablations 4 fields × 300 instances ≈ 64 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~50-60% — Docker sandbox test execution during SWE-bench-Live eval is CPU-bound; GPU idles between model inference calls\",\n      \"timeline\": \"3-5 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$216-264 (90-110h × $2.40/hr H100 SXM5 on-demand; within the 200 H100-hour hard constraint)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~135-160 H100-hours (~270-380 A100-equivalent hours)\",\n      \"gpu_breakdown\": \"SFT partition (~25-35 H100-hours): 3 fine-tuning configurations (schema variant, augmentation ablation, masked-field protocol variant). Eval partition (~110-125 H100-hours): spec extraction ~5 H100-hours; Agentless baseline run on 300 instances ≈ 16 H100-hours; SWE-bench-Live partial eval 600 instances / 4 parallel ≈ 31 H100-hours; per-field ablations on 300-instance subset × 4 fields ≈ 62 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~60-70% — agent runs fine-tuning and SWE-bench-Live eval jobs continuously; human approves schema validation threshold, masked-field training protocol, retrieval bias weights, and ablation scope at daily check-ins\",\n      \"timeline\": \"5-9 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$200-400 (~2,500 orchestration turns at ~$0.10/turn Opus)\",\n      \"estimated_gpu_cost\": \"~$324-384 (135-160h × $2.40/hr H100); within the 200 H100-hour hard constraint\",\n      \"risk_note\": \"Critical unknown: whether AST-parsed test assertions produce specs that align with human behavioral descriptions (measured by cosine similarity ≥ 0.65 on 200 SWE-bench Pro validation instances). If alignment is below threshold, the spec schema needs redesign before scale-up. GitBugs pseudo-spec quality is the secondary risk — human spot-check of 100 instances recommended before augmentation scale-up.\"\n    },\n    \"auto_research\": {\n      \"note\": \"Budget-capped auto-research only — uncapped sweeps would exceed the 200 H100-hour hard constraint. Capped to 3 fine-tuning configurations × 1 retrieval variant × 1 patch-generation prompt strategy on SWE-bench-Live Lite (300 instances) for the main configuration sweep, then ablations on the best-performing config only.\",\n      \"gpu_hours\": \"~160-180 H100-hours (budget-capped)\",\n      \"gpu_breakdown\": \"SFT partition (~30-35 H100-hours): 3 QLoRA configs on 5,300 instances. Eval partition (~130-145 H100-hours): 3-config main sweep 3 × 300 instances ≈ 48 H100-hours; per-field ablations on best config 300 × 4 fields ≈ 64 H100-hours; Agentless baseline ≈ 16 H100-hours; spec extraction inference ≈ 5 H100-hours; validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~80-85% — continuous fine-tuning, inference, and SWE-bench-Live Docker eval; sandbox parallelized across 30 instances simultaneously\",\n      \"timeline\": \"6-10 days with 4 parallel H100 GPUs\",\n      \"team\": \"0 (setup only, ~3h initial configuration)\",\n      \"claude_api_cost\": \"$400-600 (~4,500 turns)\",\n      \"estimated_gpu_cost\": \"~$384-432 (160-180h × $2.40/hr H100)\",\n      \"speed_bottleneck\": \"SWE-bench-Live Docker sandbox throughput, not GPU compute; Qwen3-Coder-30B-A3B MoE inference (~3B active params) is fast and avoids multi-GPU coordination overhead that a dense 30B model would require\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026 — 15 days remaining; conference October 24-29, Budapest) — NLP angle: structured information extraction from semi-structured bug text with partial observability, supervised fine-tuning motivation over zero-shot prompting, masked-field training protocol. The NLP contribution (task definition, schema, masked-field training, training corpus construction) is framed independently of the repair backbone integration; EMNLP ARR submission reports auto-research results (6-10 days): SFT on SWE-bench full 2,294-instance corpus, SWE-bench-Live Lite 300-instance primary eval, and 2-field ablation (affected_interface vs. none, expected_behavior vs. none). The full 5,300-instance corpus with all four per-field ablation fields is the ICSE 2027 extended paper.\",\n    \"ICSE 2027 (abstract deadline June 23, 2026; full paper ~July 2026; conference April-May 2027, Dublin) — SE angle; preferred primary target for full experimental results including GitBugs-augmented 5,300-instance corpus, SWE-bench-Live partial-set ablations, all four per-field ablation conditions, and combined SpecExtract+RGFL evaluation\",\n    \"NeurIPS 2026 (submission deadline expected May-June 2026) — systems and benchmarks angle; natural co-venue given SWE-bench-Live is NeurIPS 2025\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"SpecRover: Code Intent Extraction via LLMs (arXiv 2408.02232, ICSE 2025) — primary related work: code-space spec inference via prompting, 31% SWE-bench Lite (93/300), $0.65/issue; Section V-A 'Reasons for Failure' (see https://arxiv.org/html/2408.02232, Section V-A) categorizes 107/207 unresolved SWE-bench Lite tasks (51.7%) as 'ambiguous issue description', cases characterized as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for the hardness of this failure mode\",\n    \"SWE-bench Goes Live! (arXiv 2505.23419, NeurIPS 2025 D&B) — primary evaluation benchmark: ~1,890 contamination-resistant instances across 223 repositories, post-2024 GitHub issues, Docker-reproducible, growing at ~50 instances/month; Table 3 reports Agentless on SWE-bench-Live Lite (300 instances) at 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3) — establishes the Agentless-direct comparison level for our evaluation\",\n    \"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models (arXiv 2601.18044, Jan 2026) — direct competitor on localization improvement: hierarchical reasoning module integrated with Agentless, reading candidate files one at a time alongside the bug report to generate free-form causal explanations; achieves file-level Hit@1 71.4%→85%, element-level Exact Match 36%→69%, +12.8% end-to-end repair success improvement on SWE-bench Verified; costs $4.4/instance (3.7× Agentless); complementary to SpecExtract: RGFL operates in code-space (requires codebase access, produces unstructured reasoning), SpecExtract operates in issue-space (no codebase access, produces typed JSON spec that can reduce the candidate set RGFL must reason over); combined SpecExtract+RGFL evaluation deferred to ICSE 2027\",\n    \"Agent-CoEvo: Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints (arXiv 2604.04580, April 2026) — most directly competing design philosophy: coevolves code patches and test patches simultaneously during repair (41.33% SWE-bench Lite with DeepSeek-V3); SpecExtract's pre-extraction stance is complementary — issue-space specs reduce the initial search space before coevolution, and are pipeline-agnostic for static repair systems that do not support dynamic constraint revision\",\n    \"SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (arXiv 2509.16941) — schema ecological validity validator: 731 public instances with human requirements and interface fields\",\n    \"SWE-Lego (arXiv 2601.01426, Jan 2026) — most competitive concurrent SFT work: 32k training instances, difficulty-based curriculum SFT, 52.6% SWE-bench Verified (58.8% with 16-sample test-time scaling) with 32B model; end-to-end repair backbone that SpecExtract can serve as a preprocessing front-end for\",\n    \"SWE-Fixer (ACL Findings 2025, aclanthology.org/2025.findings-acl.62/) — fine-tunes BM25+lightweight neural retrieval module on 110K GitHub issues for coarse-to-fine file retrieval, achieving 22.0%/30.2% on SWE-bench Lite/Verified (24.7%/32.8% with P2P filtering) using only two model calls per instance; complementary to SpecExtract: SWE-Fixer trains a retriever to find relevant files directly, SpecExtract trains a spec extractor to produce structured behavioral constraints (typed interface tokens) that improve BM25 query precision — SpecExtract's extracted interface tokens could serve as high-precision query inputs to SWE-Fixer's BM25 stage\",\n    \"Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489, v2 October 2024) — integration repair backbone: open-source fixed pipeline; confirmed from paper method section: main fault-localization pipeline uses (a) LLM prompting over repository folder tree and (b) embedding-based cosine similarity (OpenAI text-embedding-3-small via LlamaIndex) over code chunks; BM25 appears only in the Agentless paper's comparison baseline ('agentless RAG baseline' from the original SWE-bench paper) — it is not part of the main localization pipeline that SpecExtract extends; SpecExtract introduces BM25 as a new third retrieval signal using structured extracted interface tokens; ~50.8% SWE-bench Verified (Agentless-1.5), 32% SWE-bench Lite; file-level Recall@1 ~57% on SWE-bench Lite\",\n    \"Revisiting Code Search in a Two-Stage Paradigm (ICSE 2023, dl.acm.org/doi/pdf/10.1145/3539597.3570383) — hybrid BM25+dense code retrieval: two-stage BM25 first-pass → CodeBERT reranking improves MRR by 8.6% over dense-only on out-of-distribution queries; mechanistic support for adding BM25 as a third retrieval signal in Agentless fault localization on post-2024 SWE-bench-Live repos\",\n    \"CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (arXiv 2604.12268, April 2026) — evaluates prompting-based spec generation from code and descriptions using existing LLMs; documents significant cross-instance variation in output structure and field completeness when prompting frontier LLMs, directly motivating the SFT approach (consistent schema adherence requires supervised training, not just prompting); is an evaluation framework rather than a repair preprocessing pipeline — confirms both that structured spec generation is an active research area and that the trained, issue-space extractor gap remains open\",\n    \"SpecFix: Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation (arXiv 2505.07270, May 2026) — repairs ambiguous problem descriptions for code generation benchmarks (HumanEval+, MBPP+, LiveCodeBench) via contrastive specification inference; operates on synthetic benchmark descriptions rather than GitHub issue bug reports, produces repaired descriptions rather than structured 4-field specs, and targets benchmark performance improvement rather than repair preprocessing — distinct from SpecExtract in domain, method, and purpose\",\n    \"Specification Vibing for Automated Program Repair / VibeRepair (arXiv 2602.08263, Feb 2026) — code-space spec extraction before repair, Defects4J, 19-23% improvement\",\n    \"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate / TraceRepair (arXiv 2604.02647, Apr 2026) — trace-based repair constraints during execution, Defects4J\",\n    \"SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) — structured repair subtask decomposition with RL; SoRFT-Qwen-7B: 21.4% SWE-bench Verified / 14.0% SWE-bench Lite; SoRFT-Qwen-32B: 30.8% SWE-bench Verified / 24.0% SWE-bench Lite; key baseline for SpecExtract's supervised fine-tuning approach\",\n    \"On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481) — fault localization recall analysis: documents how localization granularity and retrieval method affect end-to-end repair performance; provides empirical context for why embedding-based localization degrades on out-of-distribution repos\",\n    \"GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More (arXiv 2504.09651) — 150K+ open-licensed bug reports for training augmentation\",\n    \"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048)\",\n    \"PathFix: Automated Program Repair with Expected Path (arXiv 2510.14341)\"\n  ],\n  \"description\": \"We introduce SpecExtract, the first supervised issue-space specification extractor for program repair: a fine-tuned Qwen3-Coder-30B-A3B model (MoE, ~3B active parameters — fine-tuning and inference cost comparable to a 3B dense model; fits on a single H100 80GB at ~17.5GB VRAM with QLoRA; 2× H100 recommended for training throughput) that maps (bug_report_text, runtime_artifacts?) → a structured four-field JSON spec covering affected interface, observed behavior, expected behavior, and behavioral delta. The primary NLP contribution is defining *behavioral spec extraction from bug reports* as a novel structured information extraction (IE) task — analogous to NER/RE from clinical notes or legal documents — where heterogeneous bug text mixes structured artifacts (stack traces, assertion syntax) with unstructured prose under partial observability. Zero-shot prompting of frontier LLMs produces inconsistent field coverage across diverse bug report styles (documented by CodeSpecBench, arXiv 2604.12268), motivating supervised fine-tuning: the SFT approach delivers consistent 4-field typed JSON output regardless of input style variation, graceful degradation via masked-field training when runtime artifacts are absent, and a reproducible schema-enforced extraction interface that repair backends can programmatically depend on. The masked-field training protocol (p=0.5 per artifact field, [MISSING] token, null output for masked positions) enables graceful handling of partially-available runtime artifacts at inference time. The key methodological insight for training data construction is that failing test assertions in SWE-bench test patches encode implementation-agnostic behavioral specifications — they state what the program SHOULD do without revealing which code to change or the implementation strategy — enabling AST-level test parsing combined with problem-statement NLP extraction to construct 2,294 clean (bug_report, structured_spec) training pairs from SWE-bench. The 2,294-instance corpus is appropriate for this structured extraction subtask: the output space (4 typed fields, ~80-120 tokens/instance) is substantially simpler than end-to-end code repair, and comparable structured IE tasks achieve reliable generalization at 1-3k examples when schema is fixed and input diversity is covered by instances spanning 300+ repositories. SWE-bench Pro public requirements serve as a pilot ecological validity check (cosine similarity ≥ 0.65 on 200 held-out instances, confirming schema alignment with expert annotations), not a training target. GitBugs (150K+ open-licensed bug reports) provides ~3,000 pseudo-labeled augmentation instances for the ICSE 2027 extended paper; the EMNLP 2026 ARR submission uses the 2,294-instance SWE-bench full corpus only. Extracted specs are integrated with Agentless (arXiv 2407.01489, v2 October 2024) as the repair backbone. Confirmed from the Agentless paper's method section: the main fault-localization pipeline uses LLM prompting over the repository folder tree combined with embedding-based cosine similarity (OpenAI text-embedding-3-small via LlamaIndex) — BM25 appears in the Agentless paper only as the 'agentless RAG baseline' comparison, not the main pipeline. SpecExtract augments Agentless localization by (a) prepending a structured spec header to the LLM prompting step and (b) adding a BM25 pass over file paths and docstrings using extracted interface tokens as a genuinely new third retrieval signal — these are structured module/function tokens (e.g., `numpy.linalg`, `django.db.models.QuerySet`), not raw issue text, providing lexically precise distribution-shift-robust file matching that catches modules underrepresented in the embedder's training distribution on post-2024 SWE-bench-Live repos; at patch generation, a structured behavioral constraint prefix focuses generation on the documented delta. Primary evaluation is on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues), with a within-experiment Agentless-direct baseline (complemented by published SWE-bench-Live results at 11-13%) and a mechanistically-grounded target improvement of +4-7 percentage points at ~$0.05-0.10/instance — a different cost-performance point than RGFL (arXiv 2601.18044), which achieves +12.8% via per-instance code-space reasoning at $4.4/instance (40-80× more expensive). Statistical significance is assessed via McNemar's test on paired binary instance outcomes, with bootstrapped 95% CIs; at n=300, a 5 pp improvement achieves McNemar p<0.05. Per-field ablations measure individual spec contributions. SWE-Fixer (ACL Findings 2025) fine-tunes a retriever for file identification; SpecExtract trains a spec extractor whose typed interface tokens improve BM25 query precision — complementary approaches. Agent-CoEvo (arXiv 2604.04580, 41.33% SWE-bench Lite) represents the competing dynamic-coevolution philosophy; SpecExtract's pre-extraction stance is complementary and pipeline-agnostic. SWE-Lego (52.6% Verified with 32B) is included as an end-to-end SFT baseline to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end. Differentiated from SpecRover (code-space prompting, $0.65/issue, 31% SWE-bench Lite) by operating in issue-space at ~$0.05-0.10/issue — directly targeting SpecRover's Section V-A identified 51.7% ambiguous-description failure mode. Compute in H100-hours: manual mode ~90-110 H100-hours (SFT ~10-14 H100-hours, eval ~80-96 H100-hours), within the 200-hour hard constraint.\",\n  \"project_name\": \"structured_spec_repair\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL — Training data availability: The public SWE-bench Pro HuggingFace dataset contains 731 instances from 11 repositories with copyleft licenses. The remaining 1,134 instances (held-out: 12 repos, commercial: 18 proprietary repos) are explicitly not publicly accessible. The proposal's assumption of ~1,865 training pairs is wrong by a factor of 2.5x. At 731 instances, standard fine-tuning of a 32B Qwen3-Coder model risks severe overfitting and is far too small for reliable generalization.\", \"CRITICAL — Training signal invalidity (train-test distribution mismatch): SWE-bench Pro requirements were authored by humans with full access to the golden patch AND the passing test suite, working backward from tests to specifications. They are solution-conditioned prescriptive clarifications of already-solved problems. Real-world target bug reports are solution-ignorant descriptive complaints from confused users. Fine-tuning SpecExtract on (solution-knowing-human-written-spec → structured-spec) pairs will not teach the model to extract specs from genuinely ambiguous bug reports — it will teach it to produce post-hoc rationalizations of known solutions. This fundamental mismatch is not acknowledged and cannot be patched by synthetic augmentation alone.\", \"CRITICAL — Evaluation benchmark reliability: SWE-bench Verified shows SOTA of 93.9% (Claude Mythos Preview, May 2026) with documented evidence of data contamination — OpenAI has officially stopped recommending Verified scores for meaningful comparison. Demonstrating a statistically meaningful improvement on a benchmark where frontier models may be reproducing gold patches verbatim severely weakens the paper's empirical contribution.\", \"Novelty gap — SpecRover (ICSE 2025, arXiv 2408.02232) performs iterative code intent extraction and specification inference from GitHub issue descriptions using LLM agents (not supervised training), and achieves >50% improvement in repair rate on SWE-bench at $0.65/issue. The paper's claim that 'no prior work trains a spec extractor' is technically true but misses that SpecRover occupies the same research niche via prompting. The paper must explicitly frame what the supervised training provides that SpecRover's prompting approach cannot.\", \"Compute unit mismatch vs. hard constraint: The hard constraint is ≤200 H100-hours. All estimates are given in A100-hours. H100 is ~2–3× faster than A100 for transformer fine-tuning workloads, so 200 A100-hours ≈ 67–100 H100-hours (manual, within budget), but the auto-research mode at 800 A100-hours ≈ 300–400 H100-hours exceeds the hard constraint. The paper should explicitly reconcile resource estimates in H100-hours and confirm the primary research plan stays within budget.\", \"Structured spec schema undefined: The proposal outputs 'structured specs' with fields (affected interface, pre/post-conditions, expected/actual behavior delta), but these fields are never formally defined — no JSON schema, no field type definitions, no examples of what a valid spec looks like. SWE-bench Pro requirements are freeform prose; the conversion of freeform requirements to structured JSON is the hardest step and receives no design discussion.\", \"Data leakage if evaluation pivots to SWE-bench Pro: If the proposal trains on SWE-bench Pro (public: 731 instances) and evaluates on the same benchmark, it cannot cleanly show generalization. The community will ask whether the structured spec format was reverse-engineered from the test set rather than learned from scratch.\"]\nFeedback: The core direction — using SWE-bench Pro annotations to supervise structured specification extraction — is creative and timely, but rests on a mischaracterization of what SWE-bench Pro requirements actually are and how many are publicly accessible. To revise toward 'pass': (1) **Fix the training data premise**: Acknowledge that SWE-bench Pro public set is 731 instances, not 1,865. Address the solution-conditioned nature of the requirements by designing the training task as 'given the bug report + human requirements, produce structured spec fields,' treating the requirements as an alignment target rather than pretending they were extracted from bug reports alone. (2) **Address SpecRover directly**: Add SpecRover (ICSE 2025, arXiv 2408.02232) to the related work and explicitly argue why supervised fine-tuning generalizes better than per-instance LLM prompting — e.g., lower inference cost, better calibration, consistency across bug report styles. (3) **Replace SWE-bench Verified as primary eval**: Use SWE-bench Pro public (731 instances) with a held-out split for evaluation, and add an additional out-of-distribution eval on RepoBench or DebugBench to show generalization. Explicitly argue why SWE-bench Pro's requirements-based evaluation is the right target, not the contaminated Verified leaderboard. (4) **Define the structured spec schema**: Add a formal schema definition with field types and a worked example. Show how SWE-bench Pro freeform requirements can be automatically converted to this schema via a parsing step (this becomes its own empirical contribution). (5) **Reconcile compute in H100-hours**: Convert all estimates to H100-hours and confirm manual mode (~67–100 H100-hours) is well within the 200-hour budget. Remove or prominently caveat auto-research mode since it exceeds the hard constraint.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — Model naming error: 'Qwen3-Coder-14B' does not exist. Qwen3-Coder is only available in 30B-A3B (MoE, 3B active) and 480B-A35B variants. The closest viable alternatives are Qwen3-14B (dense, base Qwen3 family) or Qwen2.5-Coder-14B (prior generation). This error must be corrected with the actual model to be used, and any VRAM/compute estimates adjusted accordingly.\", \"CRITICAL — Unverifiable SpecRover failure claim: The proposal states SpecRover 'explicitly identifies that 51.7% of its unresolved SWE-bench Lite failures stem from ambiguous issue descriptions.' This specific statistic could not be verified from the SpecRover abstract or public-facing sections. If this is an inference rather than a direct quote, it must be either verified by citing the exact section, reframed as an approximation, or removed. The entire motivation chain rests on this number.\", \"SIGNIFICANT — SoRFT baseline misrepresented: The proposal states SoRFT achieves '21.4% on SWE-bench Verified with a 7B model' but SoRFT (ACL 2025) actually reports 21.4% on SWE-bench Lite, not Verified. The Verified number for SoRFT-7B is 14.0%. Using the wrong benchmark undermines the baseline comparison.\", \"SIGNIFICANT — Integration repair agent unspecified: The primary experimental claim requires running a full end-to-end repair pipeline on SWE-bench-Live (1,890 instances) that integrates the extracted spec. The proposal does not specify which agent (SWE-agent, Moatless, Agentless, custom) is used, how the spec is injected, or what its baseline resolve rate is. Without this, the compute estimate and experimental design are incomplete.\", \"SIGNIFICANT — SWE-Lego (arXiv 2601.01426) not addressed: This January 2026 SFT-for-issue-resolving paper uses 32k training instances and a comprehensive SFT curriculum for end-to-end repair. As direct related work in the SFT-for-SWE space, its omission leaves a gap the reviewer committee will flag. The differentiation should be: SpecExtract does a spec-extraction subtask (not end-to-end repair), enabling pipeline-agnostic reuse.\", \"MODERATE — Test_patch assertion conditionality overstated: The 'non-solution-conditioned' framing is the linchpin of the training data justification, but test patches are written after/alongside gold patches and specifically designed to validate the fix. In many SWE-bench instances, assertions encode precise return values or exception types only determinable by knowing the codebase implementation. The paper should more carefully scope the claim: 'behavioral-specification-level, not implementation-level conditioned' rather than 'non-solution-conditioned.'\", \"MINOR — SWE-bench-Live size outdated: The proposal states '1,565+ instances' but the live dataset now contains 1,890 tasks across 223 repositories. Update to the current figure.\", \"MINOR — Compute budget tightness for full eval: Running a repair agent on 1,890 SWE-bench-Live instances at ~10-15 minutes/issue with 4 parallel H100s consumes approximately 79-118 H100-hours for evaluation alone, leaving 0-6 H100-hours for fine-tuning in the manual mode upper estimate. Explicitly partition the budget between SFT and eval inference.\"]\nFeedback: The Round 2 revision has substantially addressed the Round 1 critical issues: the training data premise is now grounded (SWE-bench test_patch AST parsing rather than SWE-bench Pro requirements), the evaluation target is appropriate (SWE-bench-Live), compute is expressed in H100-hours with manual mode under budget, and the JSON schema is formally defined. This is genuine progress. To advance to 'pass':\n\n(1) **Fix the model name immediately**: Replace 'Qwen3-Coder-14B' with either 'Qwen3-14B' (dense, 14B params, general Qwen3 family) or 'Qwen3-Coder-30B-A3B' (MoE, only 3B active params, faster and better for code). Qwen3-Coder-30B-A3B is the more credible choice for a coding spec-extraction task — its ~3B active parameters mean fine-tuning cost is comparable to a 3B dense model despite 30B total params.\n\n(2) **Verify or remove the 51.7% SpecRover claim**: Read SpecRover Section 4 or 5 (error analysis). If the 51.7% figure is there, cite the exact table/figure. If it's an approximation, write: 'SpecRover's error analysis identifies ambiguous issue descriptions as the dominant unresolved failure mode (Section X); our estimate from their public failure logs is ~50%.' If it's not there, reframe the motivation as: 'SpecRover's code-space approach cannot address cases where the issue description itself is underspecified — a failure mode it cannot observe.'\n\n(3) **Fix the SoRFT baseline**: Change '21.4% on SWE-bench Verified' to '21.4% on SWE-bench Lite (14.0% on Verified).' This makes SoRFT a weaker baseline, which actually helps SpecExtract's positioning.\n\n(4) **Specify the integration repair agent**: Choose one concrete agent (e.g., Agentless or Moatless) as the integration vehicle for the SWE-bench-Live evaluation. Report its baseline resolve rate, then show the SpecExtract-augmented rate. Add this as 1-2 sentences in the approach section. This is the most critical missing piece for a credible empirical narrative.\n\n(5) **Add SWE-Lego differentiation**: One paragraph acknowledging SWE-Lego (arXiv 2601.01426) as concurrent SFT work, differentiating that SpecExtract is a preprocessing spec-extraction module (not an end-to-end repair system) that can be combined with any SFT-trained or prompted repair backbone, including SWE-Lego itself.\n\n(6) **Scope the conditionality claim**: In the training data section, replace 'non-solution-conditioned' with 'implementation-agnostic behavioral specifications' to reflect that while test assertions do implicitly know the fix's behavior, they do not expose the implementation strategy, making them valid targets for behavioral spec learning.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL — Fabricated SpecRover citation (third consecutive round): The proposal cites 'SpecRover Section V-A, Reasons for Failure' with the specific claim that 51.7% of its 207 unresolved SWE-bench Lite tasks involve ambiguous issue descriptions (107/207 instances, labeled by SWE-bench Verified human annotators). Independent verification via WebFetch of arXiv 2408.02232v3 confirms this section does not exist — SpecRover has no dedicated error analysis section categorizing failures by issue ambiguity, and contains no 51.7% figure, 107/207 count, or SWE-bench Verified annotation cross-reference. The Round 3 generator escalated from 'unverifiable' (Round 2) to 'fabricated with false specificity' by inventing the section label, count, and labeling provenance. This is an academic integrity violation that will result in desk rejection or post-acceptance retraction if submitted as-is.\", \"SIGNIFICANT — Agent-CoEvo (arXiv 2604.04580, April 2026) not addressed in landscape: This concurrent paper, 'Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints,' proposes that behavioral constraints (tests) should be coevolved dynamically with code patches during repair rather than pre-extracted from bug reports. It evaluates on SWE-bench Lite and SWT-bench Lite and outperforms agentless baselines. This represents the most direct competing design philosophy to SpecExtract's pre-extraction approach and must be discussed — specifically, why pre-extraction from issue text before any codebase access is preferable to dynamic constraint coevolution.\", \"MODERATE — SoRFT numbers are now correct but were mishandled across three rounds: Independent verification via ACL Anthology (2025.acl-long.559) confirms SoRFT-7B achieves 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite — exactly as stated in Round 3. The Round 2 reviewer was wrong to flag these as reversed. While the numbers are now correct, three rounds of oscillation on this point suggest the generator should add a footnote citing the ACL Anthology URL to preempt reviewer confusion.\", \"MODERATE — No reported Agentless-on-SWE-bench-Live baseline: The experimental design requires establishing Agentless-direct (no spec injection) on SWE-bench-Live Lite (300 instances) as the baseline, then measuring SpecExtract-augmented Agentless. This baseline number is not reported anywhere in the proposal, making it impossible to assess whether the expected delta (e.g., +3-8 percentage points) is plausible or whether Agentless-1.5's 50.8% Verified score generalizes to the Live dataset at all. At minimum, cite the Agentless-1.5 SWE-bench-Live Lite score if published, or explicitly acknowledge this is unmeasured.\", \"MINOR — QLoRA VRAM claim is slightly oversimplified: Qwen3-Coder-30B-A3B with QLoRA requires ~17.5GB VRAM (verified via Unsloth documentation), fitting comfortably on a single H100 80GB rather than requiring 2× H100s. The 2× claim is not wrong (it enables larger batch sizes and faster throughput) but should be reframed as 'recommended configuration for efficient throughput' rather than 'minimum requirement.'\"]\nFeedback: This proposal has made genuine progress across three rounds — the model choice, Agentless integration, SWE-Lego differentiation, schema definition, and compute budget are all solid. One issue now blocks this from passing, and one new issue must be addressed:\n\n(1) **IMMEDIATE: Remove or replace the fabricated SpecRover Section V-A claim.** There is no 'Section V-A: Reasons for Failure' in SpecRover, no 51.7% figure, no 107/207 count, and no SWE-bench Verified annotation cross-reference in the paper. Replace the entire motivation chain with a defensible framing: 'SpecRover (ICSE 2025) evaluates on SWE-bench Lite and explicitly acknowledges that its code-space traversal approach cannot resolve cases where the issue description itself is underspecified — it can only infer specifications from code that exists, not from behavior that is described but not yet correctly implemented. This architectural limitation motivates an issue-space approach that operates on bug report text before codebase access.' If you want to keep a quantitative hook, look at SpecRover's SWE-bench Lite resolve rate (31%) and the known proportion of SWE-bench tasks where the issue description is classified as ambiguous by SWE-bench Verified human annotators — cite the SWE-bench Verified paper (arXiv 2410.06992) or the SWE-bench Pro paper for that annotation, not SpecRover.\n\n(2) **Add Agent-CoEvo to related work.** One paragraph: 'Agent-CoEvo (arXiv 2604.04580, April 2026) proposes coevolving code and test patches simultaneously during repair, treating tests as dynamic behavioral constraints. SpecExtract takes the complementary pre-extraction stance: issue-space specs derived before any codebase access reduce the search space for both fault localization and patch generation, and are reusable across repair backbones without retraining — including static repair systems like Agentless that do not support dynamic constraint revision.'\n\n(3) **Add Agentless-on-SWE-bench-Live baseline.** State the known or estimated Agentless-1.5 resolve rate on SWE-bench-Live Lite (or acknowledge it as an early experimental measurement to be reported in the paper). The experimental contribution is the delta, and without the baseline anchor the paper cannot make its empirical case.\n\nWith these three changes — particularly (1) — this proposal should be able to pass in Round 4.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"IMPORTANT CORRECTION — SpecRover Section V-A claim is VERIFIED, not fabricated: Independent WebFetch of the HTML version of arXiv:2408.02232 (https://arxiv.org/html/arXiv:2408.02232) confirms the paper contains Section V-A 'RQ1: Overall Efficacy of Task Resolving' with a subsection 'Reasons for Failure' that explicitly documents 107/207 unresolved SWE-bench Lite tasks (51.7%) classified as ambiguous issue descriptions. The Round 3 reviewer's 'fabricated' accusation was incorrect. The generator should add a footnote or parenthetical citing the HTML URL to preempt any residual reviewer confusion, since the accusation has been raised three consecutive rounds.\", \"SIGNIFICANT — Internal inconsistency in EMNLP pilot scope: The EMNLP venue description states 'realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval,' but the main approach uses 2,294 SWE-bench instances + 3,000 GitBugs pseudo-labeled instances = 5,300 corpus. These are in direct conflict. Either (a) define the EMNLP submission as explicitly scoped to a pilot — SFT on SWE-bench Verified 500 subset, SWE-bench-Live Lite 300-instance eval, no GitBugs augmentation — and state this clearly in the approach section, or (b) remove the '500-instance Verified' framing from the venue description and commit to the full corpus with the understanding that compute and eval must finish within 16 days.\", \"MODERATE — 16-day deadline is unrealistically framed without explicit pilot scope: Building the 5,300-instance training corpus (AST parsing + NLP regex + LLM-assisted spec fill), SFT (10-14 H100-hours), establishing Agentless-SWE-bench-Live Docker infrastructure, running the full 300-instance eval + 4-field ablations (80-96 H100-hours), and writing the paper cannot realistically be completed in 16 days by 1-2 researchers. The submission plan should explicitly acknowledge that the EMNLP ARR submission will report pilot-scale results (e.g., SFT on 500-instance Verified subset, 100-instance SWE-bench-Live Lite eval) with the full-scale results reserved for ICSE 2027 as the primary venue.\", \"MODERATE — 'Replacing the officially-abandoned SWE-bench Verified' is imprecise: OpenAI's February 2026 announcement recommends SWE-bench Pro as the frontier evaluation replacement — not SWE-bench-Live. SWE-bench-Live is the appropriate replacement for contamination-resistant research evaluation, which is the correct positioning for this paper, but the phrasing implies SWE-bench-Live is the community standard replacement for Verified, which overstates its current adoption. Reframe as: 'As SWE-bench Verified saturates with contamination concerns, SWE-bench-Live (NeurIPS 2025) provides contamination-resistant evaluation on post-2024 issues — the appropriate target for research contributions that train on SWE-bench data.'\", \"MINOR — Cosine similarity threshold (≥ 0.65) for schema validation is stated without justification: The proposal requires AST-parsed test assertions to achieve ≥ 0.65 cosine similarity with SWE-bench Pro human requirements on 200 held-out instances. This threshold determines whether the schema is redesigned before scale-up, making it a critical gating decision. Add one sentence explaining why 0.65 is the right threshold (e.g., 'consistent with semantic similarity thresholds in information extraction literature where 0.65 distinguishes semantically related from unrelated pairs').\"]\nFeedback: The SpecRover Section V-A claim has been independently verified as correct — the HTML paper confirms the 107/207 (51.7%) ambiguous issue description statistics in the 'Reasons for Failure' subsection of Section V-A. After three rounds of false accusations, add a parenthetical citing the HTML URL (https://arxiv.org/html/arXiv:2408.02232) to preempt any residual reviewer skepticism. To reach 'pass' in Round 5: (1) **Fix the pilot/full scope inconsistency**: Choose one coherent story for EMNLP. The most defensible is a pilot submission — SFT on SWE-bench Verified 500-instance subset, primary eval on 100-150 SWE-bench-Live Lite instances (not 300), 2-field ablation (affected_interface vs. none, expected_behavior vs. none). Remove the '500-instance SWE-bench Verified training' from the venue description and put it in the approach section as the EMNLP pilot plan. State that the full 5,300-instance corpus + 300-instance eval is the ICSE 2027 primary submission. (2) **Fix the SWE-bench Verified replacement framing**: Change 'replacing the officially-abandoned SWE-bench Verified' to 'providing contamination-resistant evaluation as SWE-bench Verified saturates at frontier.' (3) **Justify the 0.65 cosine similarity threshold** in one sentence. With these changes, the proposal will have resolved all substantive issues from rounds 1-4 and should be ready to pass.\n\n### Round 5 review\nVerdict: revise\nIssues: [\"SIGNIFICANT (unresolved from Round 4) — EMNLP venue scope vs approach inconsistency: The target_venues description states 'realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval,' but the approach section describes a 5,300-instance training corpus (2,294 SWE-bench full + ~3,000 GitBugs pseudo-labeled). These are directly contradictory in the same document. Round 4 explicitly flagged this and asked for a coherent pilot story. It remains unresolved in Round 5.\", \"MODERATE (unresolved from Round 4) — 'replacing the officially-abandoned SWE-bench Verified' framing: The abandonment by OpenAI is factually confirmed (Feb 2026), but OpenAI recommends SWE-bench Pro as the replacement — not SWE-bench-Live. The proposal implies SWE-bench-Live is the community-endorsed successor to Verified, which overstates its adoption. Round 4 asked to reframe as 'providing contamination-resistant evaluation as SWE-bench Verified saturates at frontier.' This change was not made in Round 5.\", \"MODERATE (unresolved from Round 4) — 16-day timeline not explicitly scoped to auto-research + pilot: Manual mode timeline is 3-5 months, Human-in-Loop is 5-9 weeks, and only auto-research (6-10 days) fits the 16-day EMNLP window. The proposal does not state that the EMNLP ARR submission will be auto-research mode output only, and does not reconcile whether pilot-scale (500 training, 100-150 eval) or full-scale (5,300 training, 300 eval + ablations) results will be in the paper.\", \"MINOR (unresolved from Round 4) — Cosine similarity threshold 0.65 still has no justification: The schema validation gate (≥0.65 cosine similarity on 200 held-out SWE-bench Pro instances) determines whether the schema is redesigned before scale-up, yet no rationale for this specific threshold value appears anywhere in the proposal. Round 4 asked for a one-sentence justification.\", \"MINOR (unresolved from Round 4) — SpecRover HTML URL not added: Round 4 explicitly requested adding the HTML URL (https://arxiv.org/html/arXiv:2408.02232) as a parenthetical to preempt future reviewer skepticism about the 51.7% statistic — especially given three rounds of false 'fabricated' accusations in the review history. This was not done in Round 5.\"]\nFeedback: The technical substance of Round 5 is solid: Agentless baseline numbers are verified from Table 3 of arXiv 2505.23419 (11.67%/12.00%/13.33%), the SpecRover 107/207 (51.7%) claim is independently confirmed via direct HTML fetch, Qwen3-Coder-30B-A3B specs are correct, Agent-CoEvo and SWE-Lego are properly integrated, and the schema+worked-example is concrete. The paper is almost ready. Three Round 4 items remain unresolved and need targeted fixes:\n\n(1) **Fix the EMNLP pilot scope — choose one story**: The fastest fix is to remove '500-instance SWE-bench Verified training' from the venue description and replace it with the actual EMNLP submission plan. The defensible choice is: 'EMNLP ARR submission reports auto-research results: SFT on SWE-bench full 2,294-instance corpus (GitBugs augmentation deferred to ICSE), SWE-bench-Live Lite 300-instance eval, 2-field ablation (affected_interface vs. none, expected_behavior vs. none). Full 5,300-instance corpus with all four ablation fields is the ICSE 2027 extended paper.' State this explicitly in both the venue description and the approach section's experimental scope.\n\n(2) **Fix the Verified framing in one clause**: Change 'replacing the officially-abandoned SWE-bench Verified' to 'as SWE-bench Verified saturates with contamination concerns (OpenAI, Feb 2026), SWE-bench-Live provides contamination-resistant evaluation on post-2024 issues.' This is a factually accurate reframe that doesn't misrepresent which benchmark OpenAI actually recommends as replacement.\n\n(3) **Add the 0.65 threshold justification**: One sentence: 'This threshold aligns with established semantic similarity cutoffs in information-extraction evaluation literature, where scores below 0.65 on sentence-transformer embeddings indicate insufficient semantic overlap for structural field matching.' This is the only change needed for that issue.\n\n(4) **Add SpecRover HTML URL** as a parenthetical: after '107 of its 207 unresolved SWE-bench Lite tasks (51.7%)' add '(see https://arxiv.org/html/arXiv:2408.02232, Section V-A)'. Four words of insurance given three rounds of false accusations.\n\nWith these four targeted changes, all substantive issues from rounds 1-5 will be resolved.\n\n### Round 6 review\nVerdict: revise\nIssues: [\"SIGNIFICANT — Agentless retrieval mechanism mis-specified: The proposal states spec injection occurs at 'BM25+embedding file retrieval' (Agentless Stage 1), but independent verification of arXiv 2407.01489 confirms Agentless uses (a) LLM prompting over the repository tree to identify suspicious files, and (b) embedding-based cosine similarity retrieval — neither of which is BM25. The proposed integration (prepending affected_interface.module as a structured query prefix to BM25) requires either modifying Agentless's localization code to add BM25 as a third retrieval signal, or re-describing the injection as modifying the LLM prompt template to include structured spec fields. This is not a minor terminology slip — if the integration mechanism is inaccurate, the mechanistic case for the +4-7 pp improvement collapses entirely.\", \"SIGNIFICANT — The +4-7 pp improvement prediction lacks mechanistic support: The improvement claim is the paper's sole empirical contribution (from 13.33% to ~17-20% on SWE-bench-Live Lite, a 28-50% relative gain). No mechanistic argument is given for why adding structured spec fields to Agentless's retrieval/generation pipeline would produce this magnitude of improvement. Independent search confirms Agentless already sends the full issue text to its embedding retrieval — if the spec is derived FROM the issue text, the marginal information gain is structural compression (module/function names extracted from prose), not new information. The paper needs an explicit argument: e.g., 'Agentless's LLM prompting for file localization mistakes incidentally-mentioned module names for structurally-important ones; SpecExtract's extraction isolates the true affected interface with X% precision on a validation set.'\", \"MODERATE — Cosine similarity validation against SWE-bench Pro requirements has a circularity: SWE-bench Pro requirements were authored by annotators who had full access to the gold patch and tests. Achieving ≥ 0.65 cosine similarity between AST-extracted specs and SWE-bench Pro requirements confirms that machine-derived specs are solution-adjacent — not that they are useful for genuinely ambiguous in-the-wild bug reports. This validation cannot distinguish between 'our specs capture true behavioral expectations' and 'our specs recapitulate solution-known annotations.' A stronger validation would compare SpecExtract's spec quality on a held-out set of real GitHub issues that were NOT in SWE-bench (e.g., randomly sampled GitBugs instances without ground truth), graded by human annotators blind to the gold patch.\", \"MINOR — Masked-field training protocol is mechanically underspecified: The proposal mentions 'training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs' but does not specify the per-field masking probability, whether masking is uniform or weighted by artifact availability in the corpus, or how the loss is computed for masked vs. unmasked fields (e.g., is the model trained to output null for masked fields, or to infer the field from available signals?). One sentence would suffice: e.g., 'Each artifact field is independently masked with p=0.5 at training time; masked fields are replaced with a [MISSING] token and the model is trained to output null for those positions while filling the remaining fields normally.'\"]\nFeedback: Round 6 has successfully addressed all five Round 5 issues: the EMNLP scope is now self-consistent (auto-research, 2,294 SWE-bench full, GitBugs deferred to ICSE 2027), the SWE-bench Verified framing is corrected, the timeline is explicitly scoped to auto-research mode, the 0.65 threshold is justified, and the SpecRover HTML URL is added. The proposal is nearly ready.\n\nTwo fixes will unlock 'pass' in Round 7:\n\n(1) **Fix the Agentless integration description**: Independent verification of arXiv 2407.01489 confirms Agentless uses (a) LLM prompting over a repo tree, and (b) embedding-based cosine similarity — not BM25. Replace 'BM25+embedding file retrieval is biased by prepending affected_interface.module and entry_point as a structured query prefix' with an accurate description: e.g., 'We modify Agentless's LLM prompting step at Stage 1 by prepending a structured spec header (affected_interface.module + entry_point) before the repository tree, so the LLM identifies suspicious files with the affected interface explicitly in context; we additionally add a BM25 pass over file paths using the structured interface tokens as a third retrieval signal, complementing Agentless's existing embedding-based similarity.' This also strengthens the mechanistic case: BM25 exact-match on extracted module/function names catches files that embedding similarity misses because module names are out-of-distribution lexically.\n\n(2) **Add one sentence of mechanistic justification for the +4-7 pp improvement target**: The argument is available — just make it explicit: 'Agentless's fault localization already achieves roughly X% file-level recall on SWE-bench Verified; on SWE-bench-Live, where models are less likely to have encountered the repos during pretraining, recall drops. SpecExtract's structured interface extraction provides a high-precision localization signal (module + entry_point) that compensates for this distribution shift, analogous to how BM25 lexical matching improves recall in out-of-domain retrieval settings (cite BM25 + dense retrieval hybrid literature, e.g., Karpukhin et al. 2020 DPR or a code-specific IR paper).'\n\n(3) Optional but strengthening: acknowledge the cosine similarity validation limitation in one sentence (e.g., 'As a pilot ecological validity check only — this validates schema alignment against expert-annotated specs, not generalization to ambiguous in-the-wild reports') to preempt reviewer #2 questioning.\n\nWith fixes (1) and (2), the empirical contribution has a mechanistic backbone that survives reviewer scrutiny.\n\n### Round 7 review\nVerdict: revise\nIssues: [\"SIGNIFICANT (NEW) — Agentless BM25 inconsistency: The proposal explicitly states 'Agentless's fault localization... does not use BM25,' but independent search found evidence that the original Agentless paper (arXiv 2407.01489) describes prepending BM25-ranked files to prompts using the task description as query. This directly contradicts the proposal's claim. The Round 6 reviewer also verified this and concluded Agentless uses LLM prompting + embedding — but search results suggest there may be version ambiguity between original Agentless (BM25) and Agentless-Lite (embedding). The proposal must specify (a) which exact version of Agentless is used, (b) whether that version uses BM25, and (c) if BM25 is already present, reframe SpecExtract's contribution as 'using structured extracted interface tokens for BM25 queries rather than raw issue text' — a narrower but still defensible differentiation. If BM25 is already in Agentless, the entire 'adding BM25 as a third retrieval signal' framing collapses.\", \"MODERATE (NEW) — Training dataset size not justified: SFT of Qwen3-Coder-30B-A3B on 2,294 instances is not discussed in terms of sufficiency. SWE-Lego uses 32k instances for a related code task; the proposal gives no reason why 2,294 instances suffices for reliable generalization across diverse bug report styles and repository domains. Add one sentence: e.g., the structured output space is simpler than end-to-end repair (4 typed fields vs. full code patches), reducing the sample complexity requirement; or cite a comparable structured extraction task at similar data scale.\", \"MODERATE (NEW) — EMNLP NLP framing is underspecified: The 'NLP and Code Models' track requires a clear NLP modeling contribution. The proposal's NLP contribution (structured IE from semi-structured bug text with partial observability) is buried in the approach section. EMNLP reviewers will ask: why supervised fine-tuning over zero-shot prompting? CodeSpecBench (arXiv 2604.12268) shows prompting-based spec generation is imperfect — the proposal should explicitly state that zero-shot prompting produces inconsistent output structure across diverse bug report styles, motivating the SFT approach. One paragraph framing SpecExtract as an information extraction system for bug reports (akin to NER/RE from clinical notes or legal text) would anchor it for NLP reviewers.\", \"MINOR (NEW) — SpecFix (arXiv 2505.07270, May 2026) is recent adjacent work: it repairs ambiguous problem descriptions for LLM-based code generation using contrastive spec inference. While it operates on benchmark descriptions rather than GitHub issue repair, EMNLP reviewers may flag its absence. One sentence suffices: 'SpecFix (arXiv 2505.07270) repairs ambiguous problem descriptions for code generation benchmarks using contrastive inference; SpecExtract targets GitHub issue bug reports rather than benchmark descriptions and produces structured specs rather than repairing the description text itself.'\"]\nFeedback: Round 7 has resolved all four Round 6 issues: Agentless retrieval is now correctly described as LLM prompting + embedding with BM25 as an added third signal; the +4-7 pp improvement has a mechanistic backbone; the cosine similarity limitation is acknowledged; and the masked-field protocol is fully specified. The proposal is close to passable but one new critical finding blocks it.\n\n**(1) URGENT — Resolve the Agentless BM25 inconsistency**: Independent search found the original Agentless paper (arXiv 2407.01489) may already use BM25 file ranking (top-10 BM25 files prepended to LLM prompt, query = raw task description). If true, the proposal's explicit claim 'it does not use BM25' is incorrect, and the 'adding BM25 as a third retrieval signal' framing mis-states SpecExtract's novelty. The fix is: (a) fetch https://arxiv.org/pdf/2407.01489 to confirm which version of Agentless you are integrating with; (b) if it uses BM25 with raw text, reframe SpecExtract's BM25 contribution as 'replacing raw-text BM25 queries with structured extracted interface tokens — module names and entry points extracted from the spec — which are lexically precise and distribution-shift-robust, unlike free-form issue text that contains incidental mentions'; (c) update the proposal to accurately state Agentless's retrieval mechanism for the specific version used.\n\n**(2) Add one sentence on training data sufficiency**: Explain why 2,294 instances is adequate for the spec-extraction subtask (e.g., simpler output space than end-to-end repair, or comparable to similar structured IE tasks).\n\n**(3) Add one paragraph on EMNLP NLP framing**: Explicitly state why supervised fine-tuning is required over zero-shot prompting for structured spec extraction, using CodeSpecBench's imperfect prompting results as motivation. Frame SpecExtract as an IE system for semi-structured bug text.\n\n**(4) Add one sentence on SpecFix** (arXiv 2505.07270) noting the domain difference.\n\nWith issue (1) resolved, the proposal should reach pass in Round 8.\n\n### Round 8 review\nVerdict: revise\nIssues: [\"SIGNIFICANT (NEW) — RGFL (arXiv 2601.18044, Jan 2026) is absent from the landscape and directly competes: 'Reasoning Guided Fault Localization for Automated Program Repair Using LLMs' integrates a hierarchical reasoning module with Agentless to generate structured, bug-specific explanations for candidate files, achieving Hit@1 improvement from 71.4%→85% and 12.8% end-to-end repair success improvement on Agentless. This is a direct competitor on the core localization improvement claim and was available since January 2026 — EMNLP reviewers will flag its absence. SpecExtract must differentiate from RGFL: (1) RGFL uses per-instance LLM reasoning at localization time (high inference cost), while SpecExtract's spec extraction is a single forward pass of a fine-tuned model; (2) RGFL generates file-level explanations, not typed behavioral specs (affected interface, expected behavior, delta) that constrain patch generation; (3) RGFL does not address the 'ambiguous issue description' structural limitation that motivates issue-space extraction. These differentiations exist but must be stated explicitly.\", \"MODERATE (NEW) — SWE-Fixer (ACL Findings 2025, aclanthology.org/2025.findings-acl.62/) uses BM25 + lightweight retrieval model fine-tuning for code file retrieval in repair, achieving 22.0%/30.2% on SWE-bench Lite/Verified. As a fine-tuning-based approach using BM25 retrieval for repair (overlapping SpecExtract's BM25 contribution and SFT angle), its omission from the landscape may draw reviewer questions. The differentiator is clean: SWE-Fixer fine-tunes a retriever to find relevant files, while SpecExtract fine-tunes a spec extractor to produce structured behavioral constraints that improve retrieval precision — these are complementary, not competing.\", \"MODERATE (PERSISTENT) — The quantitative case for +4-7 pp improvement is now weakened by RGFL's published 12.8% end-to-end gain: if a reasoning-guided localization approach already achieves this improvement, the proposal must show either (a) SpecExtract achieves comparable gain via a cheaper, inference-time-efficient method (one forward pass vs. per-instance LLM reasoning), or (b) SpecExtract is additive on top of RGFL. The current mechanistic argument (ICSE 2023 hybrid retrieval → 8.6% OOD MRR gain) does not account for RGFL as a competing baseline.\", \"MINOR (NEW) — Statistical significance at 300-instance evaluation scale is unaddressed. The primary empirical claim (+4-7 pp over 13.33% baseline = +11 to +21 additional instances resolved out of 300) is small enough that statistical significance testing is non-trivial and reviewers will request it. McNemar's test on paired binary outcomes (instance i: SpecExtract resolves vs. Agentless-direct resolves) is the appropriate method and should be mentioned in the experimental design.\"]\nFeedback: Round 8 has successfully resolved all four Round 7 issues: Agentless BM25 mechanism is correctly described and verified; training data sufficiency is justified with comparable structured IE literature; EMNLP NLP framing is explicit; SpecFix is addressed. The primary blocking issue for Round 9 is a newly identified competitor.\n\n**(1) URGENT — Add RGFL to the landscape and differentiate**: RGFL (arXiv 2601.18044, January 2026) proposes reasoning-guided fault localization integrated with Agentless and achieves 12.8% end-to-end repair improvement — directly competing on SpecExtract's localization improvement claim. Add one paragraph: 'RGFL (arXiv 2601.18044, Jan 2026) generates structured, bug-specific LLM explanations for candidate files at fault localization time, achieving 12.8% end-to-end improvement when integrated with Agentless. SpecExtract complements rather than competes with RGFL: (a) spec extraction is a single forward pass of a fine-tuned model (~$0.05-0.10/issue) rather than per-instance LLM reasoning calls at localization time; (b) the structured 4-field spec constrains not only localization but also patch generation via behavioral delta injection; (c) issue-space extraction operates before any codebase access, making SpecExtract applicable as a front-end to RGFL itself — extracting the affected interface and behavioral delta that RGFL's reasoning module can then ground against codebase evidence.' This framing turns a competitor into a collaborator while protecting SpecExtract's novelty.\n\n**(2) Add SWE-Fixer** (ACL Findings 2025) in one sentence: 'SWE-Fixer fine-tunes a BM25+dense retrieval module to identify relevant files; SpecExtract instead trains a spec extractor to produce structured behavioral constraints that inform retrieval precision, complementing fine-tuned retrievers.' This is a 20-word addition that preempts a reviewer flag.\n\n**(3) Add statistical significance mention**: One sentence in the experimental design: 'Statistical significance is assessed via McNemar's test on paired binary instance outcomes (SpecExtract-Agentless vs. Agentless-direct), with bootstrapped CIs reported for the resolve-rate difference.'\n\nWith these three additions — particularly (1) — the proposal will have addressed all substantive issues from rounds 1-8 and should be ready to pass in Round 9.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:21:03.052Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:21:03.052Z",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-10T08:21:03.092Z_

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
  "title": "SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair",
  "core_problem": "Automated repair agents fail on ambiguous bug reports not from lack of code understanding, but because unstructured issue text leaves behavioral expectations underspecified — what interface should change, what the user observed, and what correct behavior looks like are rarely made explicit. SpecRover (ICSE 2025) partially addresses this via per-instance LLM prompting that extracts specifications from CODE during codebase traversal, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue. Its error analysis (Section V-A, 'Reasons for Failure'; see https://arxiv.org/html/2408.02232, Section V-A) identifies that 107 of its 207 unresolved SWE-bench Lite tasks (51.7%) are classified as 'ambiguous issue description' — cases the paper characterizes as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for why underspecified descriptions constitute an irreducible failure mode for code-space approaches. This architectural limitation is structural: code-side spec extraction can only infer specifications from code that already exists, not from behavior that is described in the issue but not yet correctly implemented. Bug reports routinely contain latent behavioral specifications in their runtime artifacts: stack traces name the affected interface, error messages describe observed behavior, and reproducer assertions encode expected behavior. No method trains a dedicated model to extract these signals from bug report text into a structured repair specification — covering affected interface, observed behavior, expected behavior, and their delta — that could constrain both fault localization and patch generation before any codebase traversal begins.",
  "opportunity": "Failing test assertions in SWE-bench's test patches encode implementation-agnostic behavioral specifications without revealing implementation strategies: `assert result == expected_value` or `with pytest.raises(ValueError)` states precisely what the program SHOULD do, independent of WHICH code to change or HOW to change it. By mechanically converting (problem_statement + test_patch assertions + stack traces) to structured JSON spec fields using AST-level test parsing and NLP extraction on SWE-bench's 2,294 instances, we construct a training corpus of 2,294 (bug_report, structured_spec) pairs — where the spec encodes behavioral expectations derivable without knowing the implementation strategy. This avoids the critical flaw of training on SWE-bench Pro requirements, which were authored by humans with full access to the golden patch (making them solution-conditioned). SWE-bench-Live (NeurIPS 2025, arXiv 2505.23419; ~1,890 Docker-reproducible instances across 223 repositories, drawn from post-January-2024 GitHub issues, growing at ~50 instances/month) provides a clean, contamination-resistant evaluation target with no training-set overlap. As SWE-bench Verified saturates with contamination concerns (OpenAI officially deprecated it in February 2026), SWE-bench-Live provides contamination-resistant evaluation on post-2024 issues unavailable during model training. SWE-bench Pro's human-written `requirements` and `interface` fields (731 public instances) serve as an ecological validity check — we measure cosine similarity between machine-derived specs and human requirements on a held-out 200-instance slice — confirming that AST-parsed test assertions produce specs that match expert behavioral descriptions, without using requirements as training supervision.",
  "landscape": "SpecRover (ICSE 2025, arXiv 2408.02232) is the closest prior work: given a GitHub issue, it iteratively traverses the codebase, prompting Claude 3.5 Sonnet to extract function-level summaries from visited code, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue and 31% on SWE-bench Lite (93/300). SpecRover operates in code-space (it visits source files to generate specs from code) and uses per-instance prompting (no fine-tuning). Our approach operates in issue-space (extracts specs from bug report text and runtime artifacts before any codebase traversal) and uses supervised fine-tuning (consistent structured output at ~$0.05-0.10/issue). These are complementary directions: SpecRover's code-space specs and our issue-space specs could ultimately be fused. Agent-CoEvo (arXiv 2604.04580, April 2026) proposes the most directly competing design philosophy: rather than pre-extracting behavioral constraints from issue text, it coevolves code patches and test patches simultaneously during repair, treating tests as dynamic constraints that are iteratively revised alongside candidate fixes. Agent-CoEvo achieves 41.33% on SWE-bench Lite (DeepSeek-V3) and 46.4% on SWT-bench Lite, outperforming Agentless-1.5 (32%) on those benchmarks. SpecExtract takes the complementary pre-extraction stance: (1) issue-space specs derived before any codebase access are reusable across repair backbones without retraining, including static pipeline systems like Agentless that do not support dynamic constraint revision during search; (2) pre-extracted specs reduce the initial search space before coevolution begins, making SpecExtract a potential front-end that improves Agent-CoEvo's starting population rather than competing with it. RGFL (arXiv 2601.18044, Jan 2026) introduces a hierarchical reasoning module integrated with Agentless that generates structured, bug-specific natural language explanations for candidate files and elements at fault localization time, achieving file-level Hit@1 improvement from 71.4%→85%, element-level Exact Match under top-3 files from 36%→69%, and a 12.8% end-to-end repair success improvement on SWE-bench Verified. RGFL's method reads candidate files one at a time alongside the bug report, generating free-form causal reasoning about each file's relevance to the reported symptom — it always requires codebase access to generate its explanations, produces unstructured natural language rather than typed behavioral specs, and incurs $4.4/instance cost (3.7× Agentless) through multiple per-instance LLM reasoning calls over candidate files. SpecExtract and RGFL are complementary rather than competing across three dimensions: (a) SpecExtract extracts a structured 4-field JSON spec (affected interface, observed behavior, expected behavior, behavioral delta) from issue text alone before any codebase access, providing typed interface priors that reduce the initial candidate file set RGFL's reasoning module must process — directly lowering RGFL's per-instance cost; (b) SpecExtract's behavioral delta constrains patch generation, while RGFL constrains localization only; (c) SpecExtract runs at ~$0.05-0.10/instance (single SFT forward pass) versus RGFL's $4.4/instance, making SpecExtract practical as a standalone preprocessing step for cost-sensitive pipelines and as a candidate front-end for RGFL itself. The strongest configuration — SpecExtract front-end (cheap issue-space priors) + RGFL back-end (expensive code-space reasoning on a reduced candidate set) — is deferred to the ICSE 2027 extended paper. SWE-Fixer (ACL Findings 2025, aclanthology.org/2025.findings-acl.62/) fine-tunes a BM25+lightweight neural retrieval module on 110K GitHub issues for coarse-to-fine file retrieval in repair, achieving 22.0%/30.2% on SWE-bench Lite/Verified and requiring only two model calls per instance; the differentiator is that SWE-Fixer trains a retriever to identify relevant files directly, while SpecExtract trains a spec extractor to produce structured behavioral constraints (affected interface, expected behavior) that serve as typed query inputs to BM25 and the LLM fault localization prompt, improving retrieval precision rather than replacing the retriever — these are complementary, and SpecExtract's structured interface tokens could serve as high-precision query inputs to SWE-Fixer's BM25 stage. SWE-Lego (arXiv 2601.01426, Jan 2026) is the most directly competing concurrent SFT work: it trains on 32k high-quality task instances with error masking and a difficulty-based curriculum, achieving 52.6% on SWE-bench Verified (58.8% with test-time scaling at 16 samples) using a 32B model. SWE-Lego is an end-to-end system that produces complete code fixes; SpecExtract is a preprocessing module that extracts structured behavioral specs from bug report text before any repair attempt, and can plug into SWE-Lego or any other repair backbone as a drop-in front-end — improving fault localization precision and patch generation alignment without retraining the repair agent itself. CodeSpecBench (arXiv 2604.12268, April 2026) benchmarks existing LLMs (Claude, GPT-4, Gemini) on executable behavioral specification generation via prompting — it does not train a dedicated extractor, operates on code-side and description inputs rather than bug report runtime artifacts, and is an evaluation framework rather than a preprocessing pipeline for repair. Its benchmarking results show significant cross-instance variation in output structure and field completeness when prompting frontier LLMs for specs, validating the gap: no trained, issue-space specification extractor for repair preprocessing exists, and prompting-based spec generation is insufficiently reliable for programmatic downstream use. SpecFix (arXiv 2505.07270, May 2026) repairs ambiguous problem descriptions for LLM-based code generation benchmarks (HumanEval+, MBPP+, LiveCodeBench) via contrastive specification inference — analyzing the distribution of LLM-generated programs to identify and repair description ambiguity; SpecExtract operates on GitHub issue bug reports (not synthetic benchmark descriptions), produces structured 4-field JSON specs via supervised fine-tuning (not description repair), and serves as a preprocessing input to repair agents rather than modifying task descriptions. VibeRepair (arXiv 2602.08263, Feb 2026) translates buggy CODE into behavior specifications, repairs the spec, then synthesizes corrected code, achieving 19-23% improvement on Defects4J — code-space to spec, not text-space to spec. TraceRepair (arXiv 2604.02647, Apr 2026) uses runtime execution traces generated by instrumented code execution as shared repair constraints across a multi-agent committee, fixing 392 Defects4J defects — traces are generated during repair, not extracted from issue text before repair begins. RepoRepair (arXiv 2603.01048) generates hierarchical code documentation from source files toward the bug; its documentation is code-driven, not report-driven. SoRFT (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) fine-tunes on SWE-bench with RL to decompose the repair TASK into subtasks (file → function → line → edit), achieving 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite with a 7B model (30.8% Verified and 24.0% Lite with a 32B model) — it structures the repair pipeline, not the issue semantics. PathFix (arXiv 2510.14341) derives behavioral specs from static code execution paths — code-space and offline, not issue-space. The gap: no existing work trains a dedicated model to extract structured behavioral specifications from bug report text and embedded runtime artifacts, operating entirely in issue-space before codebase access.",
  "approach": "We train SpecExtract, a Qwen3-Coder-30B-A3B model (Mixture-of-Experts: 30B total parameters, ~3B active per token — fine-tuning and inference cost scale with active parameters, comparable to a 3B dense model; fits on a single H100 80GB with QLoRA at ~17.5GB VRAM per Unsloth benchmarks; 2× H100 is the recommended training configuration for throughput, not minimum requirement) fine-tuned to map (bug_report_text, runtime_artifacts?) → structured JSON spec, where runtime artifacts are any combination of stack traces, error messages, test failure output, or explicit reproducer assertions present in the issue text. The model gracefully handles varying artifact availability through a masked-field training protocol: training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs. Each artifact field (stack_trace, error_message, test_assertions) is independently masked with p=0.5 at training time; masked fields are replaced with a [MISSING] token, and the model is trained to output null for those positions while filling remaining fields from whatever signals are available — not to infer missing artifacts from correlated signals.\n\n**NLP framing — structured IE for bug reports**: SpecExtract's primary NLP contribution is defining and solving a novel structured information extraction (IE) task: extracting typed behavioral specifications from semi-structured bug text under partial observability. This is analogous to NER/RE from clinical notes (symptom → diagnosis → treatment) or legal documents (party → obligation → condition): bug reports mix structured artifacts (stack frames with typed syntactic elements, assertion syntax) with unstructured prose (user complaint descriptions), and not all signal types are present in every instance. Zero-shot prompting of frontier LLMs produces inconsistent field coverage and schema adherence across the diversity of real-world bug report styles — CodeSpecBench (arXiv 2604.12268) benchmarks Claude, GPT-4, and Gemini on spec generation via prompting and documents significant cross-instance variation in output structure and field completeness, motivating a dedicated trained extractor with enforced schema. Supervised fine-tuning achieves three things zero-shot prompting cannot guarantee: (1) consistent 4-field typed JSON output regardless of input style variation; (2) graceful degradation under partial observability via the masked-field protocol ([MISSING] tokens, null output for absent fields); (3) a reproducible schema-enforced extraction interface that downstream repair backends can programmatically depend on. From an NLP perspective, SpecExtract introduces *behavioral spec extraction from bug reports* as a first-class structured IE task — separate from code summarization, issue severity classification, or defect localization — with its own schema, training corpus, and evaluation protocol.\n\n**Formal schema**: Each spec has four typed fields — (1) `affected_interface`: {module: str, signature: str|null, entry_point: str} extracted from stack frame function names and explicitly mentioned APIs; (2) `observed_behavior`: {error_type: str|null, error_message: str|null, symptom: str} from error output and user complaint; (3) `expected_behavior`: {description: str, assertions: [str]} as natural-language description plus test-style constraint strings when derivable; (4) `behavioral_delta`: str, a one-sentence expected-vs-actual summary. Worked example for a NumPy issue 'linalg.solve silently returns None for singular matrices instead of raising': {affected_interface: {module: 'numpy.linalg', entry_point: 'solve', signature: 'solve(a, b)'}, observed_behavior: {error_type: null, symptom: 'returns None for singular matrix input'}, expected_behavior: {description: 'should raise for non-invertible input', assertions: ['raises np.linalg.LinAlgError when matrix is singular']}, behavioral_delta: 'solve silently returns None instead of raising LinAlgError on singular input'}.\n\n**Training data construction (implementation-agnostic behavioral specifications)**: From SWE-bench full (2,294 instances including Verified 500 and the broader set): (1) parse `test_patch` test functions via Python AST to extract formal assertions — pytest.raises calls → error_type, assert statements → expected_behavior.assertions, decorated test function signatures → affected_interface hints; (2) extract stack traces and error strings from `problem_statement` text via regex heuristics → observed_behavior; (3) combine via LLM-assisted template fill using Qwen3-Coder-30B-A3B in a chain-of-thought extraction pass to produce coherent spec JSON; (4) validate on 200 SWE-bench Pro public instances that have non-null `requirements` and `interface` fields by computing cosine similarity (sentence-transformer) between mechanically-derived specs and human-authored requirements — target alignment ≥ 0.65 before training at scale (this threshold aligns with established semantic similarity cutoffs in information-extraction evaluation literature, where scores below 0.65 on sentence-transformer embeddings indicate insufficient semantic overlap for structural field matching); this validates the schema rather than using requirements as training targets. This is a pilot ecological validity check only — it confirms schema alignment with expert behavioral annotations on curated SWE-bench instances but cannot validate generalization to genuinely ambiguous in-the-wild reports that are not SWE-bench-adjacent; a full generalization validation would require human annotation of randomly sampled GitBugs instances and is deferred to the ICSE 2027 extended paper. Important framing on conditionality: test assertions are written alongside gold patches and encode the behavioral outcome the fix achieves. The training specs are therefore *implementation-agnostic* — they do not reveal which code to change or the implementation strategy — rather than strictly solution-independent. This distinction is explicitly addressed in the paper to avoid overclaiming.\n\n**Training data sufficiency**: The 2,294-instance corpus is appropriate for this structured extraction subtask. The output space is substantially simpler than end-to-end code repair: 4 typed fields totaling ~80-120 output tokens per instance vs. hundreds-to-thousands of tokens for complete code patches; the fixed schema and typed constraints further reduce the effective hypothesis space relative to free-form generation. Comparable structured IE tasks — slot-filling, clinical NER, biomedical relation extraction — achieve reliable generalization at 1-3k training examples when schema is fixed and input diversity is covered; the 2,294 instances span 300+ open-source repositories, covering the primary axis of variation (bug report style, domain, artifact availability). Qwen3-Coder's pretraining on code and technical text provides a strong prior for parsing stack traces and assertion syntax, further reducing the cold-start data requirement relative to a general-purpose LM.\n\nThe EMNLP 2026 ARR submission uses the 2,294-instance SWE-bench full corpus as the SFT training set; GitBugs augmentation (~3,000 pseudo-labeled instances, yielding a ~5,300-instance total corpus) is reserved for the ICSE 2027 extended paper.\n\n**Differentiation from SpecRover**: (1) issue-space — no codebase traversal needed at spec extraction time; (2) supervised learning — consistent, typed JSON output from a single forward pass (~$0.05-0.10/issue) vs. SpecRover's multi-step code traversal ($0.65/issue); (3) directly targets SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved SWE-bench Lite tasks) by conditioning on all available runtime artifacts in the issue, not just the code side.\n\n**Integration with Agentless**: We integrate with Agentless (arXiv 2407.01489, v2 October 2024 open-source implementation) as the repair backbone for all SWE-bench-Live evaluations — it follows a fixed pipeline (hierarchical fault localization → patch generation → patch selection) with no iterative tool calls, making spec injection clean and reproducible. Confirmed from the Agentless paper's method section: the main fault-localization pipeline combines (a) LLM prompting over the repository folder tree to identify the top-N suspicious files and (b) embedding-based cosine similarity retrieval (OpenAI text-embedding-3-small via LlamaIndex) over code chunks — the union of both signal sets provides the candidate file list. BM25 appears in the Agentless paper only as the 'agentless RAG baseline' — a simpler comparison baseline adapted from the original SWE-bench paper that uses BM25 to retrieve file contents for direct LLM patch generation — and is not part of the main Agentless localization pipeline we extend. SpecExtract specs are injected at two points: (1) fault localization — we modify the LLM prompting step by prepending a structured spec header (affected_interface.module + entry_point) before the folder listing, so the LLM identifies suspicious directories with the affected interface explicitly in context; we additionally introduce a BM25 pass over file paths and module docstrings using the extracted interface tokens as a genuinely new third retrieval signal complementing Agentless's existing embedding-based similarity — BM25 exact-match on lexically-specific tokens like `numpy.linalg` or `django.db.models.QuerySet` catches files that semantic embeddings miss when the module is underrepresented in the embedder's training distribution, exactly the localization failure mode that intensifies on post-2024 SWE-bench-Live repos relative to in-distribution SWE-bench Verified; (2) patch generation — the repair LLM receives all four spec fields as an explicit behavioral constraint header in its prompt, focusing generation on the documented behavioral delta. Crucially, the BM25 queries in SpecExtract use structured extracted interface tokens (module names, function entry points from the spec JSON), not raw issue text — this provides lexically precise, distribution-shift-robust file matching that free-form issue text cannot guarantee, since issue text contains incidental mentions, synonyms, and colloquial descriptions that dilute BM25 precision.\n\n**Agentless baseline on SWE-bench-Live**: Per the SWE-bench-Live paper (arXiv 2505.23419, Table 3), Agentless resolves 11.67% (GPT-4o), 12.00% (GPT-4.1), and 13.33% (DeepSeek V3) of SWE-bench-Live Lite (300 instances) — substantially below its ~50.8% on SWE-bench Verified, reflecting the contamination-resistant, harder distribution of post-2024 issues. We run our own Agentless-direct baseline on SWE-bench-Live Lite (300 instances) using the same backbone LLM as our SpecExtract runs, establishing a clean within-experiment comparison; the published SWE-bench-Live numbers provide independent external validation of the baseline level. SpecExtract targets +4-7 percentage points improvement over the best Agentless backbone, reported as the primary experimental contribution.\n\n**Mechanistic case for the +4-7 pp improvement target**: RGFL (arXiv 2601.18044) achieves +12.8% end-to-end improvement over Agentless via per-instance LLM reasoning over candidate files at $4.4/instance — a code-space approach that always requires codebase access and uses unstructured reasoning rather than typed behavioral specs. SpecExtract's +4-7 pp target operates at a different cost-performance point: a single SFT forward pass at ~$0.05-0.10/instance, with gains from two mechanisms unavailable to RGFL: (a) BM25-anchored lexical matching on extracted interface tokens is distribution-shift-robust in a way that RGFL's embedding-based ranking signal is not — both approaches face noisier embeddings on post-2024 SWE-bench-Live repos underrepresented in embedder pretraining, but BM25 on exact module/function name tokens does not degrade under this shift; (b) behavioral delta injection at patch generation (RGFL constrains localization only). The comparison with RGFL is therefore about cost-efficiency rather than raw performance: SpecExtract targets meaningful improvement at ~$0.05-0.10/instance vs. RGFL's $4.4/instance (40-80× cheaper), making it practical as a standalone step or as a candidate front-end that reduces the candidate set RGFL must reason over. Agentless's embedding-based file localization achieves ~57% file-level Recall@1 on SWE-bench Lite (original Agentless paper), yet its end-to-end resolve rate drops ~4× from SWE-bench Verified (~50.8%) to SWE-bench-Live Lite (13.33% best case). A primary contributor to this degradation is fault localization failure on post-2024 repos that are underrepresented in embedding model training data: embedding similarity between an issue query and post-2024 codebase chunks is noisier than on in-distribution repos, because the model has not seen those module structures and naming conventions. SpecExtract's BM25 pass on extracted module/entry_point tokens addresses this directly: exact-match retrieval on tokens like `numpy.linalg` does not require the embedding model to have indexed those repository paths during pretraining and does not degrade under distribution shift. Hybrid BM25+dense retrieval is well-established to improve out-of-domain recall in code search — a two-stage pipeline combining BM25 first-pass retrieval with dense reranking improves MRR by 8.6% over dense-only on out-of-distribution queries (Revisiting Code Search in a Two-Stage Paradigm, ICSE 2023). The +4-7 pp improvement target reflects two compounding gains: (a) localization improvement from BM25-anchored interface token matching, which provides a high-precision signal robust to the post-2024 distribution shift Agentless's embedder faces; (b) generation improvement from Stage 3 behavioral constraint injection narrowing the patch candidate space to the documented behavioral delta — these gains compound because better localization provides a more focused candidate file set for patch generation.\n\n**Evaluation**: Primary eval on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues) with Agentless as backbone; per-field ablations independently zero out each spec field to quantify individual contribution to resolve rate. Statistical significance is assessed via McNemar's test on paired binary instance outcomes (SpecExtract+Agentless vs. Agentless-direct, each instance scored as resolved or not), with bootstrapped 95% CIs reported for the resolve-rate difference; at n=300, a 5 pp improvement (15 additional resolved instances) achieves McNemar p<0.05. Secondary eval: cosine-similarity validation on 200 SWE-bench Pro held-out instances (schema validity check). Comparison baselines: Agentless direct repair without spec (our own run + published 11-13% from SWE-bench-Live paper), SpecRover-equivalent prompting (ablation of supervised fine-tuning benefit), SoRFT-Qwen-7B (21.4% Verified / 14.0% Lite, structured subtask decomposition), SWE-Lego (52.6% Verified, end-to-end SFT backbone — SpecExtract as preprocessing front-end demonstrates orthogonal contribution). RGFL (arXiv 2601.18044) serves as a published reference point for reasoning-guided localization improvement (+12.8% on SWE-bench Verified at $4.4/instance); direct SWE-bench-Live comparison and combined SpecExtract+RGFL evaluation are deferred to the ICSE 2027 extended paper.\n\n**Publication scope**: The EMNLP 2026 ARR submission (auto-research mode, 6-10 days) reports results on the 2,294-instance SWE-bench full SFT corpus with SWE-bench-Live Lite 300-instance primary eval and a 2-field ablation (affected_interface vs. none, expected_behavior vs. none) — the two fields with the strongest localization and generation signal respectively. The full 5,300-instance corpus (with GitBugs augmentation) and all four per-field ablation fields constitute the ICSE 2027 extended paper.",
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
    "EMNLP 2026 (ARR submission deadline May 25, 2026 — 15 days remaining; conference October 24-29, Budapest) — NLP angle: structured information extraction from semi-structured bug text with partial observability, supervised fine-tuning motivation over zero-shot prompting, masked-field training protocol. The NLP contribution (task definition, schema, masked-field training, training corpus construction) is framed independently of the repair backbone integration; EMNLP ARR submission reports auto-research results (6-10 days): SFT on SWE-bench full 2,294-instance corpus, SWE-bench-Live Lite 300-instance primary eval, and 2-field ablation (affected_interface vs. none, expected_behavior vs. none). The full 5,300-instance corpus with all four per-field ablation fields is the ICSE 2027 extended paper.",
    "ICSE 2027 (abstract deadline June 23, 2026; full paper ~July 2026; conference April-May 2027, Dublin) — SE angle; preferred primary target for full experimental results including GitBugs-augmented 5,300-instance corpus, SWE-bench-Live partial-set ablations, all four per-field ablation conditions, and combined SpecExtract+RGFL evaluation",
    "NeurIPS 2026 (submission deadline expected May-June 2026) — systems and benchmarks angle; natural co-venue given SWE-bench-Live is NeurIPS 2025"
  ],
  "level": "solid",
  "key_references": [
    "SpecRover: Code Intent Extraction via LLMs (arXiv 2408.02232, ICSE 2025) — primary related work: code-space spec inference via prompting, 31% SWE-bench Lite (93/300), $0.65/issue; Section V-A 'Reasons for Failure' (see https://arxiv.org/html/2408.02232, Section V-A) categorizes 107/207 unresolved SWE-bench Lite tasks (51.7%) as 'ambiguous issue description', cases characterized as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for the hardness of this failure mode",
    "SWE-bench Goes Live! (arXiv 2505.23419, NeurIPS 2025 D&B) — primary evaluation benchmark: ~1,890 contamination-resistant instances across 223 repositories, post-2024 GitHub issues, Docker-reproducible, growing at ~50 instances/month; Table 3 reports Agentless on SWE-bench-Live Lite (300 instances) at 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3) — establishes the Agentless-direct comparison level for our evaluation",
    "RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models (arXiv 2601.18044, Jan 2026) — direct competitor on localization improvement: hierarchical reasoning module integrated with Agentless, reading candidate files one at a time alongside the bug report to generate free-form causal explanations; achieves file-level Hit@1 71.4%→85%, element-level Exact Match 36%→69%, +12.8% end-to-end repair success improvement on SWE-bench Verified; costs $4.4/instance (3.7× Agentless); complementary to SpecExtract: RGFL operates in code-space (requires codebase access, produces unstructured reasoning), SpecExtract operates in issue-space (no codebase access, produces typed JSON spec that can reduce the candidate set RGFL must reason over); combined SpecExtract+RGFL evaluation deferred to ICSE 2027",
    "Agent-CoEvo: Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints (arXiv 2604.04580, April 2026) — most directly competing design philosophy: coevolves code patches and test patches simultaneously during repair (41.33% SWE-bench Lite with DeepSeek-V3); SpecExtract's pre-extraction stance is complementary — issue-space specs reduce the initial search space before coevolution, and are pipeline-agnostic for static repair systems that do not support dynamic constraint revision",
    "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (arXiv 2509.16941) — schema ecological validity validator: 731 public instances with human requirements and interface fields",
    "SWE-Lego (arXiv 2601.01426, Jan 2026) — most competitive concurrent SFT work: 32k training instances, difficulty-based curriculum SFT, 52.6% SWE-bench Verified (58.8% with 16-sample test-time scaling) with 32B model; end-to-end repair backbone that SpecExtract can serve as a preprocessing front-end for",
    "SWE-Fixer (ACL Findings 2025, aclanthology.org/2025.findings-acl.62/) — fine-tunes BM25+lightweight neural retrieval module on 110K GitHub issues for coarse-to-fine file retrieval, achieving 22.0%/30.2% on SWE-bench Lite/Verified (24.7%/32.8% with P2P filtering) using only two model calls per instance; complementary to SpecExtract: SWE-Fixer trains a retriever to find relevant files directly, SpecExtract trains a spec extractor to produce structured behavioral constraints (typed interface tokens) that improve BM25 query precision — SpecExtract's extracted interface tokens could serve as high-precision query inputs to SWE-Fixer's BM25 stage",
    "Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489, v2 October 2024) — integration repair backbone: open-source fixed pipeline; confirmed from paper method section: main fault-localization pipeline uses (a) LLM prompting over repository folder tree and (b) embedding-based cosine similarity (OpenAI text-embedding-3-small via LlamaIndex) over code chunks; BM25 appears only in the Agentless paper's comparison baseline ('agentless RAG baseline' from the original SWE-bench paper) — it is not part of the main localization pipeline that SpecExtract extends; SpecExtract introduces BM25 as a new third retrieval signal using structured extracted interface tokens; ~50.8% SWE-bench Verified (Agentless-1.5), 32% SWE-bench Lite; file-level Recall@1 ~57% on SWE-bench Lite",
    "Revisiting Code Search in a Two-Stage Paradigm (ICSE 2023, dl.acm.org/doi/pdf/10.1145/3539597.3570383) — hybrid BM25+dense code retrieval: two-stage BM25 first-pass → CodeBERT reranking improves MRR by 8.6% over dense-only on out-of-distribution queries; mechanistic support for adding BM25 as a third retrieval signal in Agentless fault localization on post-2024 SWE-bench-Live repos",
    "CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation (arXiv 2604.12268, April 2026) — evaluates prompting-based spec generation from code and descriptions using existing LLMs; documents significant cross-instance variation in output structure and field completeness when prompting frontier LLMs, directly motivating the SFT approach (consistent schema adherence requires supervised training, not just prompting); is an evaluation framework rather than a repair preprocessing pipeline — confirms both that structured spec generation is an active research area and that the trained, issue-space extractor gap remains open",
    "SpecFix: Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation (arXiv 2505.07270, May 2026) — repairs ambiguous problem descriptions for code generation benchmarks (HumanEval+, MBPP+, LiveCodeBench) via contrastive specification inference; operates on synthetic benchmark descriptions rather than GitHub issue bug reports, produces repaired descriptions rather than structured 4-field specs, and targets benchmark performance improvement rather than repair preprocessing — distinct from SpecExtract in domain, method, and purpose",
    "Specification Vibing for Automated Program Repair / VibeRepair (arXiv 2602.08263, Feb 2026) — code-space spec extraction before repair, Defects4J, 19-23% improvement",
    "Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate / TraceRepair (arXiv 2604.02647, Apr 2026) — trace-based repair constraints during execution, Defects4J",
    "SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) — structured repair subtask decomposition with RL; SoRFT-Qwen-7B: 21.4% SWE-bench Verified / 14.0% SWE-bench Lite; SoRFT-Qwen-32B: 30.8% SWE-bench Verified / 24.0% SWE-bench Lite; key baseline for SpecExtract's supervised fine-tuning approach",
    "On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481) — fault localization recall analysis: documents how localization granularity and retrieval method affect end-to-end repair performance; provides empirical context for why embedding-based localization degrades on out-of-distribution repos",
    "GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More (arXiv 2504.09651) — 150K+ open-licensed bug reports for training augmentation",
    "RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048)",
    "PathFix: Automated Program Repair with Expected Path (arXiv 2510.14341)"
  ],
  "description": "We introduce SpecExtract, the first supervised issue-space specification extractor for program repair: a fine-tuned Qwen3-Coder-30B-A3B model (MoE, ~3B active parameters — fine-tuning and inference cost comparable to a 3B dense model; fits on a single H100 80GB at ~17.5GB VRAM with QLoRA; 2× H100 recommended for training throughput) that maps (bug_report_text, runtime_artifacts?) → a structured four-field JSON spec covering affected interface, observed behavior, expected behavior, and behavioral delta. The primary NLP contribution is defining *behavioral spec extraction from bug reports* as a novel structured information extraction (IE) task — analogous to NER/RE from clinical notes or legal documents — where heterogeneous bug text mixes structured artifacts (stack traces, assertion syntax) with unstructured prose under partial observability. Zero-shot prompting of frontier LLMs produces inconsistent field coverage across diverse bug report styles (documented by CodeSpecBench, arXiv 2604.12268), motivating supervised fine-tuning: the SFT approach delivers consistent 4-field typed JSON output regardless of input style variation, graceful degradation via masked-field training when runtime artifacts are absent, and a reproducible schema-enforced extraction interface that repair backends can programmatically depend on. The masked-field training protocol (p=0.5 per artifact field, [MISSING] token, null output for masked positions) enables graceful handling of partially-available runtime artifacts at inference time. The key methodological insight for training data construction is that failing test assertions in SWE-bench test patches encode implementation-agnostic behavioral specifications — they state what the program SHOULD do without revealing which code to change or the implementation strategy — enabling AST-level test parsing combined with problem-statement NLP extraction to construct 2,294 clean (bug_report, structured_spec) training pairs from SWE-bench. The 2,294-instance corpus is appropriate for this structured extraction subtask: the output space (4 typed fields, ~80-120 tokens/instance) is substantially simpler than end-to-end code repair, and comparable structured IE tasks achieve reliable generalization at 1-3k examples when schema is fixed and input diversity is covered by instances spanning 300+ repositories. SWE-bench Pro public requirements serve as a pilot ecological validity check (cosine similarity ≥ 0.65 on 200 held-out instances, confirming schema alignment with expert annotations), not a training target. GitBugs (150K+ open-licensed bug reports) provides ~3,000 pseudo-labeled augmentation instances for the ICSE 2027 extended paper; the EMNLP 2026 ARR submission uses the 2,294-instance SWE-bench full corpus only. Extracted specs are integrated with Agentless (arXiv 2407.01489, v2 October 2024) as the repair backbone. Confirmed from the Agentless paper's method section: the main fault-localization pipeline uses LLM prompting over the repository folder tree combined with embedding-based cosine similarity (OpenAI text-embedding-3-small via LlamaIndex) — BM25 appears in the Agentless paper only as the 'agentless RAG baseline' comparison, not the main pipeline. SpecExtract augments Agentless localization by (a) prepending a structured spec header to the LLM prompting step and (b) adding a BM25 pass over file paths and docstrings using extracted interface tokens as a genuinely new third retrieval signal — these are structured module/function tokens (e.g., `numpy.linalg`, `django.db.models.QuerySet`), not raw issue text, providing lexically precise distribution-shift-robust file matching that catches modules underrepresented in the embedder's training distribution on post-2024 SWE-bench-Live repos; at patch generation, a structured behavioral constraint prefix focuses generation on the documented delta. Primary evaluation is on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues), with a within-experiment Agentless-direct baseline (complemented by published SWE-bench-Live results at 11-13%) and a mechanistically-grounded target improvement of +4-7 percentage points at ~$0.05-0.10/instance — a different cost-performance point than RGFL (arXiv 2601.18044), which achieves +12.8% via per-instance code-space reasoning at $4.4/instance (40-80× more expensive). Statistical significance is assessed via McNemar's test on paired binary instance outcomes, with bootstrapped 95% CIs; at n=300, a 5 pp improvement achieves McNemar p<0.05. Per-field ablations measure individual spec contributions. SWE-Fixer (ACL Findings 2025) fine-tunes a retriever for file identification; SpecExtract trains a spec extractor whose typed interface tokens improve BM25 query precision — complementary approaches. Agent-CoEvo (arXiv 2604.04580, 41.33% SWE-bench Lite) represents the competing dynamic-coevolution philosophy; SpecExtract's pre-extraction stance is complementary and pipeline-agnostic. SWE-Lego (52.6% Verified with 32B) is included as an end-to-end SFT baseline to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end. Differentiated from SpecRover (code-space prompting, $0.65/issue, 31% SWE-bench Lite) by operating in issue-space at ~$0.05-0.10/issue — directly targeting SpecRover's Section V-A identified 51.7% ambiguous-description failure mode. Compute in H100-hours: manual mode ~90-110 H100-hours (SFT ~10-14 H100-hours, eval ~80-96 H100-hours), within the 200-hour hard constraint.",
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

### Round 7 review
Verdict: revise
Issues: ["SIGNIFICANT (NEW) — Agentless BM25 inconsistency: The proposal explicitly states 'Agentless's fault localization... does not use BM25,' but independent search found evidence that the original Agentless paper (arXiv 2407.01489) describes prepending BM25-ranked files to prompts using the task description as query. This directly contradicts the proposal's claim. The Round 6 reviewer also verified this and concluded Agentless uses LLM prompting + embedding — but search results suggest there may be version ambiguity between original Agentless (BM25) and Agentless-Lite (embedding). The proposal must specify (a) which exact version of Agentless is used, (b) whether that version uses BM25, and (c) if BM25 is already present, reframe SpecExtract's contribution as 'using structured extracted interface tokens for BM25 queries rather than raw issue text' — a narrower but still defensible differentiation. If BM25 is already in Agentless, the entire 'adding BM25 as a third retrieval signal' framing collapses.", "MODERATE (NEW) — Training dataset size not justified: SFT of Qwen3-Coder-30B-A3B on 2,294 instances is not discussed in terms of sufficiency. SWE-Lego uses 32k instances for a related code task; the proposal gives no reason why 2,294 instances suffices for reliable generalization across diverse bug report styles and repository domains. Add one sentence: e.g., the structured output space is simpler than end-to-end repair (4 typed fields vs. full code patches), reducing the sample complexity requirement; or cite a comparable structured extraction task at similar data scale.", "MODERATE (NEW) — EMNLP NLP framing is underspecified: The 'NLP and Code Models' track requires a clear NLP modeling contribution. The proposal's NLP contribution (structured IE from semi-structured bug text with partial observability) is buried in the approach section. EMNLP reviewers will ask: why supervised fine-tuning over zero-shot prompting? CodeSpecBench (arXiv 2604.12268) shows prompting-based spec generation is imperfect — the proposal should explicitly state that zero-shot prompting produces inconsistent output structure across diverse bug report styles, motivating the SFT approach. One paragraph framing SpecExtract as an information extraction system for bug reports (akin to NER/RE from clinical notes or legal text) would anchor it for NLP reviewers.", "MINOR (NEW) — SpecFix (arXiv 2505.07270, May 2026) is recent adjacent work: it repairs ambiguous problem descriptions for LLM-based code generation using contrastive spec inference. While it operates on benchmark descriptions rather than GitHub issue repair, EMNLP reviewers may flag its absence. One sentence suffices: 'SpecFix (arXiv 2505.07270) repairs ambiguous problem descriptions for code generation benchmarks using contrastive inference; SpecExtract targets GitHub issue bug reports rather than benchmark descriptions and produces structured specs rather than repairing the description text itself.'"]
Feedback: Round 7 has resolved all four Round 6 issues: Agentless retrieval is now correctly described as LLM prompting + embedding with BM25 as an added third signal; the +4-7 pp improvement has a mechanistic backbone; the cosine similarity limitation is acknowledged; and the masked-field protocol is fully specified. The proposal is close to passable but one new critical finding blocks it.

**(1) URGENT — Resolve the Agentless BM25 inconsistency**: Independent search found the original Agentless paper (arXiv 2407.01489) may already use BM25 file ranking (top-10 BM25 files prepended to LLM prompt, query = raw task description). If true, the proposal's explicit claim 'it does not use BM25' is incorrect, and the 'adding BM25 as a third retrieval signal' framing mis-states SpecExtract's novelty. The fix is: (a) fetch https://arxiv.org/pdf/2407.01489 to confirm which version of Agentless you are integrating with; (b) if it uses BM25 with raw text, reframe SpecExtract's BM25 contribution as 'replacing raw-text BM25 queries with structured extracted interface tokens — module names and entry points extracted from the spec — which are lexically precise and distribution-shift-robust, unlike free-form issue text that contains incidental mentions'; (c) update the proposal to accurately state Agentless's retrieval mechanism for the specific version used.

**(2) Add one sentence on training data sufficiency**: Explain why 2,294 instances is adequate for the spec-extraction subtask (e.g., simpler output space than end-to-end repair, or comparable to similar structured IE tasks).

**(3) Add one paragraph on EMNLP NLP framing**: Explicitly state why supervised fine-tuning is required over zero-shot prompting for structured spec extraction, using CodeSpecBench's imperfect prompting results as motivation. Frame SpecExtract as an IE system for semi-structured bug text.

**(4) Add one sentence on SpecFix** (arXiv 2505.07270) noting the domain difference.

With issue (1) resolved, the proposal should reach pass in Round 8.

### Round 8 review
Verdict: revise
Issues: ["SIGNIFICANT (NEW) — RGFL (arXiv 2601.18044, Jan 2026) is absent from the landscape and directly competes: 'Reasoning Guided Fault Localization for Automated Program Repair Using LLMs' integrates a hierarchical reasoning module with Agentless to generate structured, bug-specific explanations for candidate files, achieving Hit@1 improvement from 71.4%→85% and 12.8% end-to-end repair success improvement on Agentless. This is a direct competitor on the core localization improvement claim and was available since January 2026 — EMNLP reviewers will flag its absence. SpecExtract must differentiate from RGFL: (1) RGFL uses per-instance LLM reasoning at localization time (high inference cost), while SpecExtract's spec extraction is a single forward pass of a fine-tuned model; (2) RGFL generates file-level explanations, not typed behavioral specs (affected interface, expected behavior, delta) that constrain patch generation; (3) RGFL does not address the 'ambiguous issue description' structural limitation that motivates issue-space extraction. These differentiations exist but must be stated explicitly.", "MODERATE (NEW) — SWE-Fixer (ACL Findings 2025, aclanthology.org/2025.findings-acl.62/) uses BM25 + lightweight retrieval model fine-tuning for code file retrieval in repair, achieving 22.0%/30.2% on SWE-bench Lite/Verified. As a fine-tuning-based approach using BM25 retrieval for repair (overlapping SpecExtract's BM25 contribution and SFT angle), its omission from the landscape may draw reviewer questions. The differentiator is clean: SWE-Fixer fine-tunes a retriever to find relevant files, while SpecExtract fine-tunes a spec extractor to produce structured behavioral constraints that improve retrieval precision — these are complementary, not competing.", "MODERATE (PERSISTENT) — The quantitative case for +4-7 pp improvement is now weakened by RGFL's published 12.8% end-to-end gain: if a reasoning-guided localization approach already achieves this improvement, the proposal must show either (a) SpecExtract achieves comparable gain via a cheaper, inference-time-efficient method (one forward pass vs. per-instance LLM reasoning), or (b) SpecExtract is additive on top of RGFL. The current mechanistic argument (ICSE 2023 hybrid retrieval → 8.6% OOD MRR gain) does not account for RGFL as a competing baseline.", "MINOR (NEW) — Statistical significance at 300-instance evaluation scale is unaddressed. The primary empirical claim (+4-7 pp over 13.33% baseline = +11 to +21 additional instances resolved out of 300) is small enough that statistical significance testing is non-trivial and reviewers will request it. McNemar's test on paired binary outcomes (instance i: SpecExtract resolves vs. Agentless-direct resolves) is the appropriate method and should be mentioned in the experimental design."]
Feedback: Round 8 has successfully resolved all four Round 7 issues: Agentless BM25 mechanism is correctly described and verified; training data sufficiency is justified with comparable structured IE literature; EMNLP NLP framing is explicit; SpecFix is addressed. The primary blocking issue for Round 9 is a newly identified competitor.

**(1) URGENT — Add RGFL to the landscape and differentiate**: RGFL (arXiv 2601.18044, January 2026) proposes reasoning-guided fault localization integrated with Agentless and achieves 12.8% end-to-end repair improvement — directly competing on SpecExtract's localization improvement claim. Add one paragraph: 'RGFL (arXiv 2601.18044, Jan 2026) generates structured, bug-specific LLM explanations for candidate files at fault localization time, achieving 12.8% end-to-end improvement when integrated with Agentless. SpecExtract complements rather than competes with RGFL: (a) spec extraction is a single forward pass of a fine-tuned model (~$0.05-0.10/issue) rather than per-instance LLM reasoning calls at localization time; (b) the structured 4-field spec constrains not only localization but also patch generation via behavioral delta injection; (c) issue-space extraction operates before any codebase access, making SpecExtract applicable as a front-end to RGFL itself — extracting the affected interface and behavioral delta that RGFL's reasoning module can then ground against codebase evidence.' This framing turns a competitor into a collaborator while protecting SpecExtract's novelty.

**(2) Add SWE-Fixer** (ACL Findings 2025) in one sentence: 'SWE-Fixer fine-tunes a BM25+dense retrieval module to identify relevant files; SpecExtract instead trains a spec extractor to produce structured behavioral constraints that inform retrieval precision, complementing fine-tuned retrievers.' This is a 20-word addition that preempts a reviewer flag.

**(3) Add statistical significance mention**: One sentence in the experimental design: 'Statistical significance is assessed via McNemar's test on paired binary instance outcomes (SpecExtract-Agentless vs. Agentless-direct), with bootstrapped CIs reported for the resolve-rate difference.'

With these three additions — particularly (1) — the proposal will have addressed all substantive issues from rounds 1-8 and should be ready to pass in Round 9.


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
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "type": "user",
  "uuid": "22d2a022-ba4c-4682-9591-a97a5b5ef4c2",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:21:03.087Z_

```json
{
  "parentUuid": "22d2a022-ba4c-4682-9591-a97a5b5ef4c2",
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
  "uuid": "ae63d213-42d1-4323-b2cf-701232fbefc9",
  "timestamp": "2026-05-10T08:21:03.087Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:21:03.087Z_

```json
{
  "parentUuid": "ae63d213-42d1-4323-b2cf-701232fbefc9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "25399fd6-9d67-4884-9941-358f492b213b",
  "timestamp": "2026-05-10T08:21:03.087Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
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
  "leafUuid": "25399fd6-9d67-4884-9941-358f492b213b",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Structured Specification Extraction for Guided Program Repair",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232"
}
```

---

### Assistant

_source line 8 · 2026-05-10T08:21:26.117Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this Round 9 submission of SpecExtract. I need to independently verify claims, check for competitive work, and assess whether the Round 8 issues have been properly addressed.

Let me first understand what the Round 8 issues were:
1. SIGNIFICANT — RGFL (arXiv 2601.18044) absent from landscape — **NOW ADDRESSED** in Round 9 (appears extensively in landscape section)
2. MODERATE — SWE-Fixer (ACL Findings 2025) absent — **NOW ADDRESSED** in Round 9


3. MODERATE — Quantitative case for +4-7 pp weakened by RGFL's 12.8% — need to check if addressed through cost-efficiency framing
4. MINOR — Statistical significance unaddressed — **NOW ADDRESSED** (McNemar's test mentioned)

The landscape section now properly covers RGFL with clear differentiation on cost and approach, includes SWE-Fixer, and addresses the statistical significance concern. I need to verify whether the quantitative comparison issue has been resolved and continue examining the rest of the submission.

Now I'm doing independent verification of the key papers and claims cited in Round 9 — checking if RGFL, SWE-bench-Live, CodeSpecBench, Agent-CoEvo, and SpecFix are real papers with accurate numbers, plus searching for any new competitive work that might have emerged recently. I'm in round 9 of review, so most issues have been addressed already. I should focus on verifying the new claims about RGFL and SWE-Fixer are accurate, hunting for any recent competitive work I might have missed, and confirming the previous round's fixes actually stuck. Looking at the RGFL integration specifically, the proposal claims substantial improvements—hitting 85% file-level accuracy and 69% element-level exact match, with a 12.8% end-to-end boost on SWE-bench Verified—though it does cost 3.7× more per instance than the agentless baseline.

The SWE-Fixer differentiation is now clearer, and McNemar's test provides statistical grounding. The cost argument has been sharpened too, positioning SpecExtract as 40-80× cheaper than RGFL while still delivering meaningful gains. Now I need to verify these numbers are solid and check whether any new papers have emerged that might compete with or contradict the claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25399fd6-9d67-4884-9941-358f492b213b",
  "isSidechain": false,
  "requestId": "req_011CatZcNJpXJRCUeE5ArT3k",
  "type": "assistant",
  "uuid": "2ac84875-be3a-44b2-8814-ea56e7916eba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017daaqW2ojXxaCvKCHSq2tL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32183,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32183,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2016,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 32183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32183
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

_source line 9 · 2026-05-10T08:21:26.178Z_

I'll conduct independent verification of the Round 9 submission's key claims, checking whether Round 8 issues were resolved and searching for new competitive work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ac84875-be3a-44b2-8814-ea56e7916eba",
  "isSidechain": false,
  "requestId": "req_011CatZcNJpXJRCUeE5ArT3k",
  "type": "assistant",
  "uuid": "6d96503b-2dfe-48e3-a432-fcb3e9a2d18c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017daaqW2ojXxaCvKCHSq2tL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32183,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32183,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2016,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 32183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32183
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

_source line 10 · 2026-05-10T08:21:31.242Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0178qeLZoAL5u2P5VTRNabUs`</summary>

```json
{
  "description": "Verify RGFL paper claims and search for new competitive work",
  "subagent_type": "Explore",
  "prompt": "I need to verify several paper claims for an ML research review. Please search for the following:\n\n1. RGFL paper (arXiv 2601.18044) - \"Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models\" - verify: (a) does it exist, (b) does it achieve file-level Hit@1 improvement from 71.4%→85%, element-level Exact Match 36%→69%, +12.8% end-to-end repair improvement on SWE-bench Verified, (c) $4.4/instance cost.\n\n2. Search for very recent (March-May 2026) papers on: \"issue specification extraction for program repair\", \"structured specification from bug reports\", \"behavioral specification extraction code repair\" - any new competitive work?\n\n3. SWE-bench-Live paper (arXiv 2505.23419) - does it report Agentless on SWE-bench-Live Lite at approximately 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3)?\n\n4. SWE-Lego (arXiv 2601.01426) - does it achieve 52.6% on SWE-bench Verified with 32B model?\n\n5. Agent-CoEvo (arXiv 2604.04580) - does it achieve 41.33% on SWE-bench Lite with DeepSeek-V3?\n\nUse WebSearch for these queries. I need factual verification, not summaries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d96503b-2dfe-48e3-a432-fcb3e9a2d18c",
  "isSidechain": false,
  "requestId": "req_011CatZcNJpXJRCUeE5ArT3k",
  "type": "assistant",
  "uuid": "4165843c-b2d3-4db6-9507-3b962730b26e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017daaqW2ojXxaCvKCHSq2tL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32183,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32183,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2016,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 32183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32183
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

_source line 11 · 2026-05-10T08:21:37.082Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01WcKyFdQhb1ZS4m5QRD7YfW`</summary>

```json
{
  "description": "Search for concurrent competitive work in issue-space spec extraction",
  "subagent_type": "Explore",
  "prompt": "I'm reviewing a research paper about \"SpecExtract\" - a method that trains a supervised model to extract structured behavioral specifications from bug reports (issue text, stack traces, test assertions) before running any automated program repair. The paper claims no prior work trains a dedicated model for issue-space specification extraction.\n\nPlease search for:\n\n1. \"site:arxiv.org specification extraction bug report 2026\" - any papers in 2026 doing this?\n2. \"site:arxiv.org structured information extraction program repair 2025 2026\"\n3. \"issue specification repair SWE-bench fine-tuning 2026 arxiv\"\n4. \"behavioral specification extraction supervised learning bug 2025 2026\"\n5. \"CodeSpecBench arxiv 2604.12268\" - verify this exists and what it benchmarks\n6. \"SpecFix arxiv 2505.07270\" - verify this exists and what it does (repairs benchmark descriptions via contrastive inference)\n7. Search paperswithcode.com for \"SWE-bench Verified\" current SOTA leaderboard - what's the current top score?\n\nUse WebSearch. I need to know if there are any papers that train a dedicated supervised model to extract specifications FROM BUG REPORT TEXT (not from code) for use in automated program repair. This is the core novelty claim of SpecExtract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4165843c-b2d3-4db6-9507-3b962730b26e",
  "isSidechain": false,
  "requestId": "req_011CatZcNJpXJRCUeE5ArT3k",
  "type": "assistant",
  "uuid": "0a5fed40-3622-4f63-8f80-f8b3936a88eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017daaqW2ojXxaCvKCHSq2tL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32183,
      "cache_read_input_tokens": 11631,
      "output_tokens": 2016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32183,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2016,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 32183,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32183
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

_source line 12 · 2026-05-10T08:22:00.907Z_

<details><summary>↩ Tool result · `toolu_01WcKyFdQhb1ZS4m5QRD7YfW`</summary>

```text
Based on my comprehensive search, here are my findings on the SpecExtract paper's novelty claims:

## Core Novelty Claim Assessment

**The claim that "no prior work trains a dedicated model for issue-space specification extraction" appears plausible but requires nuance:**

### Papers Found (2025-2026)

**1. CodeSpecBench (arXiv 2604.12268)** - VERIFIED & CRITICAL FINDING
- **What it does**: Benchmarks LLMs for executable behavioral specification generation
- **Key difference**: This evaluates LLMs' ability to generate specifications FROM CODE, not from bug report text
- **Specification format**: Executable Python functions (preconditions/postconditions)
- **Evaluation setup**: Function and repository-level code generation tasks
- **This does NOT train a supervised model on issue text** - it benchmarks LLMs on specification generation from code context

**2. SpecFix (arXiv 2505.07270)** - VERIFIED & RELEVANT
- **What it does**: Repairs ambiguous problem descriptions FOR LLM-BASED CODE GENERATION via contrastive specification inference
- **Process**: (1) Analyzes LLM's interpretation using testing/program repair, (2) Refines descriptions via contrastive inference
- **Key distinction**: Modifies/refines benchmark descriptions themselves (HumanEval+, MBPP+), not extracting specs from bug reports
- **This is not supervised extraction** - it's iterative description refinement

**3. SWE-Lego (arXiv 2601.01426)** - RELEVANT
- Supervised Fine-Tuning for software issue resolving with 32k task instances
- Fine-tunes models on SWE-bench instances
- **Does NOT specifically focus on specification extraction from issue text**

**4. SWE-Bench++ (arXiv 2512.17419)** - PARTIALLY RELEVANT
- Includes Hint Injection Algorithm converting model-breaking instances into trajectories
- Injects function signatures and dependency graphs
- **Not specifically specification extraction from bug report text**

### No Direct Prior Art Found

My search found **no papers that explicitly train a dedicated supervised model to extract structured specifications (behavior specifications, test requirements, assertions) FROM BUG REPORT TEXT** for use in automated program repair. This appears to be SpecExtract's core novelty.

The closest work (CodeSpecBench, SpecFix) operates in different spaces:
- CodeSpecBench: LLM evaluation on specification generation from code
- SpecFix: Iterative repair of problem descriptions, not supervised extraction from issues

### Current SOTA on SWE-Bench Verified

**Top performers (as of May 2026):**
- **GPT 5.5**: 82.60%
- **Claude Opus 4.7**: 82.00%
- Other fine-tuned models (SWE-Lego-Qwen3-32B): 52.6%

The leaderboard shows a significant gap between frontier models and fine-tuned open-source models, suggesting room for innovative approaches like specification extraction pre-processing.

Sources:
- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/abs/2604.12268)
- [Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation](https://arxiv.org/abs/2505.07270)
- [SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving](https://arxiv.org/html/2601.01426v2)
- [SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks](https://arxiv.org/html/2512.17419v1)
- [SWE-Bench Verified Benchmark](https://www.swebench.com/verified.html)
- [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a5fed40-3622-4f63-8f80-f8b3936a88eb",
  "isSidechain": false,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "type": "user",
  "uuid": "c029c217-47f0-4217-a64d-2534a3d4c49a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a research paper about \"SpecExtract\" - a method that trains a supervised model to extract structured behavioral specifications from bug reports (issue text, stack traces, test assertions) before running any automated program repair. The paper claims no prior work trains a dedicated model for issue-space specification extraction.\n\nPlease search for:\n\n1. \"site:arxiv.org specification extraction bug report 2026\" - any papers in 2026 doing this?\n2. \"site:arxiv.org structured information extraction program repair 2025 2026\"\n3. \"issue specification repair SWE-bench fine-tuning 2026 arxiv\"\n4. \"behavioral specification extraction supervised learning bug 2025 2026\"\n5. \"CodeSpecBench arxiv 2604.12268\" - verify this exists and what it benchmarks\n6. \"SpecFix arxiv 2505.07270\" - verify this exists and what it does (repairs benchmark descriptions via contrastive inference)\n7. Search paperswithcode.com for \"SWE-bench Verified\" current SOTA leaderboard - what's the current top score?\n\nUse WebSearch. I need to know if there are any papers that train a dedicated supervised model to extract specifications FROM BUG REPORT TEXT (not from code) for use in automated program repair. This is the core novelty claim of SpecExtract.",
    "agentId": "a37fbbadb2fa9cc12",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search, here are my findings on the SpecExtract paper's novelty claims:\n\n## Core Novelty Claim Assessment\n\n**The claim that \"no prior work trains a dedicated model for issue-space specification extraction\" appears plausible but requires nuance:**\n\n### Papers Found (2025-2026)\n\n**1. CodeSpecBench (arXiv 2604.12268)** - VERIFIED & CRITICAL FINDING\n- **What it does**: Benchmarks LLMs for executable behavioral specification generation\n- **Key difference**: This evaluates LLMs' ability to generate specifications FROM CODE, not from bug report text\n- **Specification format**: Executable Python functions (preconditions/postconditions)\n- **Evaluation setup**: Function and repository-level code generation tasks\n- **This does NOT train a supervised model on issue text** - it benchmarks LLMs on specification generation from code context\n\n**2. SpecFix (arXiv 2505.07270)** - VERIFIED & RELEVANT\n- **What it does**: Repairs ambiguous problem descriptions FOR LLM-BASED CODE GENERATION via contrastive specification inference\n- **Process**: (1) Analyzes LLM's interpretation using testing/program repair, (2) Refines descriptions via contrastive inference\n- **Key distinction**: Modifies/refines benchmark descriptions themselves (HumanEval+, MBPP+), not extracting specs from bug reports\n- **This is not supervised extraction** - it's iterative description refinement\n\n**3. SWE-Lego (arXiv 2601.01426)** - RELEVANT\n- Supervised Fine-Tuning for software issue resolving with 32k task instances\n- Fine-tunes models on SWE-bench instances\n- **Does NOT specifically focus on specification extraction from issue text**\n\n**4. SWE-Bench++ (arXiv 2512.17419)** - PARTIALLY RELEVANT\n- Includes Hint Injection Algorithm converting model-breaking instances into trajectories\n- Injects function signatures and dependency graphs\n- **Not specifically specification extraction from bug report text**\n\n### No Direct Prior Art Found\n\nMy search found **no papers that explicitly train a dedicated supervised model to extract structured specifications (behavior specifications, test requirements, assertions) FROM BUG REPORT TEXT** for use in automated program repair. This appears to be SpecExtract's core novelty.\n\nThe closest work (CodeSpecBench, SpecFix) operates in different spaces:\n- CodeSpecBench: LLM evaluation on specification generation from code\n- SpecFix: Iterative repair of problem descriptions, not supervised extraction from issues\n\n### Current SOTA on SWE-Bench Verified\n\n**Top performers (as of May 2026):**\n- **GPT 5.5**: 82.60%\n- **Claude Opus 4.7**: 82.00%\n- Other fine-tuned models (SWE-Lego-Qwen3-32B): 52.6%\n\nThe leaderboard shows a significant gap between frontier models and fine-tuned open-source models, suggesting room for innovative approaches like specification extraction pre-processing.\n\nSources:\n- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/abs/2604.12268)\n- [Automated Repair of Ambiguous Problem Descriptions for LLM-Based Code Generation](https://arxiv.org/abs/2505.07270)\n- [SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving](https://arxiv.org/html/2601.01426v2)\n- [SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks](https://arxiv.org/html/2512.17419v1)\n- [SWE-Bench Verified Benchmark](https://www.swebench.com/verified.html)\n- [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/)"
      }
    ],
    "totalDurationMs": 23821,
    "totalTokens": 22603,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 3160,
      "cache_creation_input_tokens": 3962,
      "cache_read_input_tokens": 14523,
      "output_tokens": 958,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3962
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3160,
          "output_tokens": 958,
          "cache_read_input_tokens": 14523,
          "cache_creation_input_tokens": 3962,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3962,
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
  "sourceToolAssistantUUID": "0a5fed40-3622-4f63-8f80-f8b3936a88eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T08:22:40.255Z_

<details><summary>↩ Tool result · `toolu_0178qeLZoAL5u2P5VTRNabUs`</summary>

```text
Perfect! Now let me compile a comprehensive verification report based on all the information I've gathered.

## Verification Report: ML Research Paper Claims

Based on my search and document analysis, here are the factual verification results for each claim:

### **1. RGFL (arXiv 2601.18044) - VERIFIED ✓**

**Paper exists:** Yes, confirmed on arXiv.

**Reported metrics - ALL VERIFIED:**
- File-level Hit@1 improvement: 71.4% → 85% ✓
- Element-level Exact Match improvement: 36% → 69% ✓
- End-to-end repair improvement on SWE-bench Verified: +12.8% ✓
- Cost per instance: $4.40 ✓

All numerical claims match the paper's reported results.

**Source:** [RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models](https://arxiv.org/abs/2601.18044)

---

### **2. Recent Papers (March-May 2026) on Specification Extraction - IDENTIFIED**

Three competitive/related works in this timeframe:

**CodeSpecBench (arXiv 2604.12268)** - April 2026
- Benchmarks LLMs on executable behavioral specification generation
- Finds sharp degradation on repo-level tasks: best model achieves only 20.2% pass rate
- Key finding: "Specification generation is substantially more challenging than code generation"
- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/abs/2604.12268)

**VibeRepair (arXiv 2602.08263)** - February 2026
- Specification-centric APR approach
- Fixes 174 bugs on Defects4J v1.2 (19% improvement over SOTA)
- Three-phase process: transform buggy code → repair specification → generate fixed code
- [Specification Vibing for Automated Program Repair](https://arxiv.org/abs/2602.08263)

**VulnResolver (arXiv 2601.13933)** - January 2026
- LLM-based hybrid agent for vulnerability repair
- Uses Safety Property Analysis Agent (SPAAgent) to generate/validate safety properties
- Achieves 75% on SEC-bench Lite
- [VulnResolver: A Hybrid Agent Framework for LLM-Based Automated Vulnerability Repair](https://arxiv.org/pdf/2601.13933)

---

### **3. SWE-bench-Live (arXiv 2505.23419) - VERIFIED ✓**

**Paper exists:** Yes, confirmed.

**Agentless results on SWE-bench-Live Lite - ALL VERIFIED:**
- GPT-4o: 11.67% ✓
- GPT-4.1: 12.00% ✓
- DeepSeek V3: 13.33% ✓

The paper specifically evaluates "Agentless" baseline approach with these exact metrics.

**Source:** [SWE-bench Goes Live!](https://arxiv.org/abs/2505.23419)

---

### **4. SWE-Lego (arXiv 2601.01426) - VERIFIED ✓**

**Paper exists:** Yes, confirmed.

**32B model performance on SWE-bench Verified: 52.6% - VERIFIED ✓**

The paper states: "SWE-Lego-Qwen3-32B model attains 52.6% on SWE-bench Verified."

Additional finding: Can reach 58.8% with test-time scaling at TTS@16.

**Source:** [SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving](https://arxiv.org/abs/2601.01426)

---

### **5. Agent-CoEvo (arXiv 2604.04580) - VERIFIED ✓**

**Paper exists:** Yes, confirmed as "Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints"

**SWE-bench Lite performance with DeepSeek-V3: 41.33% - VERIFIED ✓**

The paper reports: "On SWE-bench Lite, Agent-CoEvo achieves 41.33% resolution rate, surpassing strong baselines like DARS (37%) and KGCompass (36.67%)."

Additional finding: On SWT-bench Lite (test quality), it achieves 46.4%.

**Source:** [Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints](https://arxiv.org/html/2604.04580)

---

## Summary

**All five main paper claims are VERIFIED with accurate metrics.** No discrepancies found. All numerical values match the papers' reported results. The three specification-related papers (CodeSpecBench, VibeRepair, VulnResolver) represent active competitive work in this space from January-April 2026.

Sources:
- [RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models](https://arxiv.org/abs/2601.18044)
- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/abs/2604.12268)
- [Specification Vibing for Automated Program Repair](https://arxiv.org/abs/2602.08263)
- [VulnResolver: A Hybrid Agent Framework for LLM-Based Automated Vulnerability Repair](https://arxiv.org/pdf/2601.13933)
- [SWE-bench Goes Live!](https://arxiv.org/abs/2505.23419)
- [SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving](https://arxiv.org/abs/2601.01426)
- [Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints](https://arxiv.org/html/2604.04580)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4165843c-b2d3-4db6-9507-3b962730b26e",
  "isSidechain": false,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "type": "user",
  "uuid": "8aa2c251-da59-4ed5-a7ad-d338d78d3dd7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify several paper claims for an ML research review. Please search for the following:\n\n1. RGFL paper (arXiv 2601.18044) - \"Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models\" - verify: (a) does it exist, (b) does it achieve file-level Hit@1 improvement from 71.4%→85%, element-level Exact Match 36%→69%, +12.8% end-to-end repair improvement on SWE-bench Verified, (c) $4.4/instance cost.\n\n2. Search for very recent (March-May 2026) papers on: \"issue specification extraction for program repair\", \"structured specification from bug reports\", \"behavioral specification extraction code repair\" - any new competitive work?\n\n3. SWE-bench-Live paper (arXiv 2505.23419) - does it report Agentless on SWE-bench-Live Lite at approximately 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3)?\n\n4. SWE-Lego (arXiv 2601.01426) - does it achieve 52.6% on SWE-bench Verified with 32B model?\n\n5. Agent-CoEvo (arXiv 2604.04580) - does it achieve 41.33% on SWE-bench Lite with DeepSeek-V3?\n\nUse WebSearch for these queries. I need factual verification, not summaries.",
    "agentId": "ac873be0562f7a6e1",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me compile a comprehensive verification report based on all the information I've gathered.\n\n## Verification Report: ML Research Paper Claims\n\nBased on my search and document analysis, here are the factual verification results for each claim:\n\n### **1. RGFL (arXiv 2601.18044) - VERIFIED ✓**\n\n**Paper exists:** Yes, confirmed on arXiv.\n\n**Reported metrics - ALL VERIFIED:**\n- File-level Hit@1 improvement: 71.4% → 85% ✓\n- Element-level Exact Match improvement: 36% → 69% ✓\n- End-to-end repair improvement on SWE-bench Verified: +12.8% ✓\n- Cost per instance: $4.40 ✓\n\nAll numerical claims match the paper's reported results.\n\n**Source:** [RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models](https://arxiv.org/abs/2601.18044)\n\n---\n\n### **2. Recent Papers (March-May 2026) on Specification Extraction - IDENTIFIED**\n\nThree competitive/related works in this timeframe:\n\n**CodeSpecBench (arXiv 2604.12268)** - April 2026\n- Benchmarks LLMs on executable behavioral specification generation\n- Finds sharp degradation on repo-level tasks: best model achieves only 20.2% pass rate\n- Key finding: \"Specification generation is substantially more challenging than code generation\"\n- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/abs/2604.12268)\n\n**VibeRepair (arXiv 2602.08263)** - February 2026\n- Specification-centric APR approach\n- Fixes 174 bugs on Defects4J v1.2 (19% improvement over SOTA)\n- Three-phase process: transform buggy code → repair specification → generate fixed code\n- [Specification Vibing for Automated Program Repair](https://arxiv.org/abs/2602.08263)\n\n**VulnResolver (arXiv 2601.13933)** - January 2026\n- LLM-based hybrid agent for vulnerability repair\n- Uses Safety Property Analysis Agent (SPAAgent) to generate/validate safety properties\n- Achieves 75% on SEC-bench Lite\n- [VulnResolver: A Hybrid Agent Framework for LLM-Based Automated Vulnerability Repair](https://arxiv.org/pdf/2601.13933)\n\n---\n\n### **3. SWE-bench-Live (arXiv 2505.23419) - VERIFIED ✓**\n\n**Paper exists:** Yes, confirmed.\n\n**Agentless results on SWE-bench-Live Lite - ALL VERIFIED:**\n- GPT-4o: 11.67% ✓\n- GPT-4.1: 12.00% ✓\n- DeepSeek V3: 13.33% ✓\n\nThe paper specifically evaluates \"Agentless\" baseline approach with these exact metrics.\n\n**Source:** [SWE-bench Goes Live!](https://arxiv.org/abs/2505.23419)\n\n---\n\n### **4. SWE-Lego (arXiv 2601.01426) - VERIFIED ✓**\n\n**Paper exists:** Yes, confirmed.\n\n**32B model performance on SWE-bench Verified: 52.6% - VERIFIED ✓**\n\nThe paper states: \"SWE-Lego-Qwen3-32B model attains 52.6% on SWE-bench Verified.\"\n\nAdditional finding: Can reach 58.8% with test-time scaling at TTS@16.\n\n**Source:** [SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving](https://arxiv.org/abs/2601.01426)\n\n---\n\n### **5. Agent-CoEvo (arXiv 2604.04580) - VERIFIED ✓**\n\n**Paper exists:** Yes, confirmed as \"Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints\"\n\n**SWE-bench Lite performance with DeepSeek-V3: 41.33% - VERIFIED ✓**\n\nThe paper reports: \"On SWE-bench Lite, Agent-CoEvo achieves 41.33% resolution rate, surpassing strong baselines like DARS (37%) and KGCompass (36.67%).\"\n\nAdditional finding: On SWT-bench Lite (test quality), it achieves 46.4%.\n\n**Source:** [Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints](https://arxiv.org/html/2604.04580)\n\n---\n\n## Summary\n\n**All five main paper claims are VERIFIED with accurate metrics.** No discrepancies found. All numerical values match the papers' reported results. The three specification-related papers (CodeSpecBench, VibeRepair, VulnResolver) represent active competitive work in this space from January-April 2026.\n\nSources:\n- [RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models](https://arxiv.org/abs/2601.18044)\n- [CodeSpecBench: Benchmarking LLMs for Executable Behavioral Specification Generation](https://arxiv.org/abs/2604.12268)\n- [Specification Vibing for Automated Program Repair](https://arxiv.org/abs/2602.08263)\n- [VulnResolver: A Hybrid Agent Framework for LLM-Based Automated Vulnerability Repair](https://arxiv.org/pdf/2601.13933)\n- [SWE-bench Goes Live!](https://arxiv.org/abs/2505.23419)\n- [SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving](https://arxiv.org/abs/2601.01426)\n- [Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints](https://arxiv.org/html/2604.04580)"
      }
    ],
    "totalDurationMs": 69005,
    "totalTokens": 29978,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2895,
      "cache_read_input_tokens": 25577,
      "output_tokens": 1499,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2895
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1499,
          "cache_read_input_tokens": 25577,
          "cache_creation_input_tokens": 2895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2895,
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
  "sourceToolAssistantUUID": "4165843c-b2d3-4db6-9507-3b962730b26e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
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
  "leafUuid": "8aa2c251-da59-4ed5-a7ad-d338d78d3dd7",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Structured Specification Extraction for Guided Program Repair",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232"
}
```

---

### Assistant

_source line 16 · 2026-05-10T08:24:08.517Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me now assess the Round 9 submission based on these search results and the review history.

**Key findings from my research:**

1. **All key numerical claims verified**: RGFL (71.4%→85% Hit@1, 36%→69% element-level EM, +12.8%, $4.4/instance), SWE-bench-Live Agentless numbers, SWE-Lego 52.6%, Agent-CoEvo 41.33% - all verified.


2. **The core novelty holds up**: The supervised extraction of structured specifications directly from bug reports for repair appears genuinely novel—existing work either focuses on LLM prompting for spec generation from code or repairs based on benchmark descriptions, but nothing targets issue-space supervised extraction specifically.
3. **SWE-bench Verified shows why the proposal's focus is sound**: With GPT-5.5 at 82.6% and Claude Opus at 82%, the ceiling is too high for meaningful differentiation, making SWE-bench-Live the right choice for demonstrating improvements.

Now checking how Round 8 feedback was addressed: RGFL gets proper treatment with cost and scope differentiation ($4.4 per instance versus $0.05-0.10, plus localization-only versus localization-plus-generation), and SWE-Fixer is now included. The improvement claim gets reframed as a different cost-performance tradeoff rather than direct competition with RGFL's 12.8%, which is reasonable though reviewers might still question whether the gains justify the approach. Statistical significance testing via McNemar's test is in place.

The remaining concern is whether the +4-7 percentage point improvement claim holds up given RGFL's stronger baseline.  The mechanistic argument about BM25 on structured tokens providing distribution-shift robustness for post-2024 repositories is genuinely novel, but the comparison gets complicated since RGFL was tested on SWE-bench Verified while SpecExtract targets the harder SWE-bench-Live Lite distribution. The training data scale (2,294 instances versus SWE-Lego's 32k) is now justified by pointing to simpler output structure and comparable structured IE tasks that work at 1-3k examples. The ecological validity concern is acknowledged as a pilot check rather than a full solution.

Using SWE-bench-Live as the primary evaluation makes sense given that Verified is already saturated at 82.6%. The NLP framing around structured information extraction from semi-structured bug reports and the masked-field protocol feels appropriate for EMNLP. The remaining question is whether reviewers will find the 4-7 percentage point improvement on SWE-bench-Live Lite compelling enough, especially when that translates to just a handful of additional instances resolved out of 300.

There's also the matter of SWE-bench-Live Lite's relative newness—it's only been around for about 90 days and the community hasn't had much time to familiarize themselves with it compared to Verified. The ecological validity check using 200 instances from SWE-bench Pro is somewhat limited, though framing it as a pilot study helps. The timeline is also tight—the auto-research mode needs to complete within 6-10 days to meet the May 25 EMNLP ARR deadline, which is technically feasible but leaves little margin for error.

Looking at the overall assessment: novelty sits around 3.5 because while the core idea of using supervised issue-space spec extraction as a preprocessing step for repair is genuinely novel, it's a fairly natural extension of existing work like SpecRover and RGFL. Feasibility is also around 3.5—the compute requirements check out at 90-110 H100-hours, and the Agentless integration is well-specified, though there's uncertainty about whether the claimed 4-7 percentage point improvement will actually materialize. The proposal itself is exceptionally clear and detailed, with a concrete schema and well-articulated training approach.

For impact, I'm settling on 3.5 as well—this is a preprocessing module that would improve an existing repair system incrementally on a relatively new benchmark, and while the practical value is real (40-80× cheaper than RGFL for comparable localization), the overall repair improvement remains incremental. That puts the average around 3.75, which falls short of the 4.0 threshold.

But wait—this is round 9 out of 10, and I need to reconsider whether the arguments for passing actually hold up. All the critical issues from earlier rounds have been resolved, the technical work is sound and thoroughly specified, the core novelty around supervised spec extraction is legitimate, and every major claim has been verified. The related work is comprehensive and the compute budget is realistic.

On the other hand, the empirical gains of 4-7 percentage points are modest and depend on an unverified assumption about robustness to distribution shift. The ecological validity check using cosine similarity on 200 SWE-bench Pro instances has acknowledged limitations. The training corpus of 2,294 instances is small compared to SWE-Lego's 32k, and while the justification for this size is plausible, it hasn't been tested. And there's a question about whether a preprocessing module for a software engineering task really fits EMNLP's scope, even within the NLP and Code Models track—it's not a core NLP modeling contribution.

Let me think through the novelty and feasibility more carefully here.

The core contribution is training a supervised model to extract structured specifications from bug reports and runtime artifacts, then using those as preprocessing for repair. This approach is clearly distinct from prior work like SpecRover, which operates in code-space with per-instance prompting, or RGFL with its per-instance reasoning, or SWE-Fixer which uses a retriever rather than spec extraction, or CodeSpecBench which evaluates prompting strategies, or SpecFix which focuses on benchmark description repair. The novelty holds up—I'd rate it around 3.5 to 4.0.

On feasibility, the compute budget is reasonable, the necessary models and tools are available, and constructing the data through AST parsing, regex, and LLM assistance is straightforward. The real question mark is whether that 4-7 percentage point improvement actually shows up in practice.

The main practical constraint is the SWE-bench-Live Docker infrastructure—spinning up 300 instances is a significant undertaking, though the proposal acknowledges this as the bottleneck. That brings feasibility down to about 3.5.

Looking at this holistically, after nine rounds of refinement, all the critical blocking issues have been resolved. The novelty is genuine, the technical approach is well-specified and achievable, and I haven't uncovered any new critical problems. The remaining uncertainty is purely empirical—whether the predicted improvements will actually materialize when the experiments run.

But there's a gap in the empirical validation: the proposal frames SpecExtract as a front-end to SWE-Lego and other repair systems, yet SWE-Lego already hits 52.6% on SWE-bench Verified. To make that claim stick, you'd want to show SpecExtract improving performance on top of SWE-Lego, but that experiment is deferred. Instead, the paper only demonstrates gains over Agentless on SWE-bench-Live, which is a thinner empirical story for a venue like EMNLP. The proposal is transparent about this limitation, though. The comparison framing makes sense for a preprocessing module—you'd naturally evaluate SpecExtract+Agentless against Agentless rather than against SWE-Lego. But I'm noticing another potential issue: the proposal claims SWE-bench Verified was officially deprecated by OpenAI in February 2026, yet current SOTA scores are still being reported on it (GPT 5.5 at 82.6%, Claude Opus at 82%), which suggests the deprecation claim might be overstated—OpenAI may have discouraged it for frontier comparisons without fully discontinuing it.

Looking at how the proposal frames this in the landscape section, though, it actually works: "As SWE-bench Verified saturates with contamination concerns (OpenAI officially deprecated it in February 2026), SWE-bench-Live provides contamination-resistant evaluation on post-2024 issues unavailable during model training." The deprecation framing is reasonable even if models still report scores, since that doesn't contradict OpenAI's official stance on frontier comparisons.

Now I'm checking whether the Qwen3-Coder-30B-A3B model claim holds up—the model does exist and was verified in earlier feedback, and the VRAM estimate of around 17.5GB with QLoRA on a single GPU seems plausible.

After working through everything, the submission has addressed all the critical issues from the previous round, verified the key numerical claims, and demonstrates genuine novelty in the issue-space supervised spec extraction approach with solid experimental design and appropriate compute allocation. The main remaining uncertainties are that the +4-7 percentage point improvement is a prediction dependent on actual experimental results, the training corpus is smaller than comparable work, and the ecological validity check has acknowledged limitations—but these are typical pre-submission uncertainties rather than fundamental problems.

Looking at the scores across novelty, feasibility, clarity, and impact, I'm landing around 3.75, which falls short of the 4.0 threshold. Since this is round 9 of 10, a revise verdict means one more iteration to address things. The key issue I'd flag is that the SpecExtract and SWE-Lego combination is presented as a contribution but hasn't been empirically validated in the EMNLP submission itself—that scope needs clarification. Additionally, while the mechanistic justification for the improvement targets has gotten stronger, it still leans heavily on the distribution shift argument between BM25 and the proposed approach.

Actually, I need to think through this more carefully as a reviewer. The real question is whether to pass now or issue a final revise that forces a definitive decision at round 10. The average score is below threshold, but the issues aren't fundamental—the core claims check out and the approach is technically sound. Some of the uncertainty is just inherent to pre-publication work.

But there are two legitimate new concerns worth raising. First, the primary SWE-bench-Live evaluation only tests with Agentless as the repair backbone across 300 instances, yet the proposal claims SpecExtract is pipeline-agnostic without actually demonstrating that.  The paper should either test with another backbone like SWE-agent or Moatless to prove portability, or explicitly frame this as a SpecExtract-Agentless integration and save the broader claims for later. Second, the core improvement argument hinges on Agentless failing on post-2024 repos because the embedder hasn't seen them, but Agentless-1.5 already achieves around 50.8% on SWE-bench Verified which has repos from various time periods, so the drop to 13.33% on Live needs better explanation than just the embedding gap.

The mechanistic argument has some real gaps here, but it's not a dealbreaker. Since this is round 9, I can issue a revise with specific feedback to tighten the improvement prediction and clarify the scope around pipeline-agnosticism claims, knowing round 10 will force a final decision.

Looking at what's left to address: the pipeline-agnosticism claim versus single-backbone evaluation, whether distribution shift is really the right explanation for the BM25 advantage, and the undemonstrated assumption about SWE-Lego gains being orthogonal. These are all legitimate but fixable with targeted revisions.

For my final scores, novelty sits at 3.5—the issue-space supervised spec extraction for repair is genuinely novel and the structured IE framing helps, but it's more of an incremental methodological advance than a fundamental shift.

Feasibility is also 3.5 because while the approach is technically sound and the budget works, those 4-7 percentage point improvements depend on mechanistic assumptions I haven't fully validated empirically. Clarity is strong at 4.5 given how detailed and well-specified everything is. Impact lands at 3.5 too—it's a preprocessing module with modest claimed gains, and while the cost-efficiency angle against RGFL is compelling, I haven't actually validated it directly.

That averages to 3.75, which falls below the 4.0 threshold, so my verdict is revise. The persistent issue is whether the distribution shift explanation for the 4× degradation from Verified to Live data actually holds up, or if it's just a matter of problem difficulty instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8aa2c251-da59-4ed5-a7ad-d338d78d3dd7",
  "isSidechain": false,
  "requestId": "req_011CatZjX57ykuGQUzozAP8a",
  "type": "assistant",
  "uuid": "e7368966-1fb2-4a35-adb7-d5509a6d2b19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0124KtSAh4LrRrNvUmNhETqq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 985,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 43814,
      "output_tokens": 5016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 985,
          "output_tokens": 5016,
          "cache_read_input_tokens": 43814,
          "cache_creation_input_tokens": 3541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3541
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

_source line 17 · 2026-05-10T08:24:13.359Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013nmNf4J1y7sXovEqpNWSDK`</summary>

```json
{
  "description": "Verify Agentless degradation on SWE-bench-Live and distribution shift claims",
  "subagent_type": "Explore",
  "prompt": "I need to verify one specific claim in a research paper for adversarial review. The paper argues that Agentless degrades from ~50.8% on SWE-bench Verified to ~13.33% on SWE-bench-Live Lite primarily due to \"embedding distribution shift\" - specifically that the OpenAI text-embedding-3-small model used by Agentless hasn't indexed post-2024 repository structures.\n\nPlease search for:\n1. \"site:arxiv.org SWE-bench-Live 2505.23419\" - fetch or search for the actual paper to see if it discusses WHY Agentless degrades so dramatically (4x) from Verified to Live - is it attributed to distribution shift, harder problems, or something else?\n2. \"Agentless SWE-bench degradation distribution shift embedding\" - any papers analyzing why Agentless performs worse on harder/newer benchmarks?\n3. \"OpenAI text-embedding-3-small out of distribution code retrieval\" - any papers documenting this specific embedding model's OOD degradation on code retrieval?\n4. Also search: \"SWE-bench Verified vs Live difficulty\" - any analysis of whether the 4x gap is about problem difficulty vs embedding quality?\n\nI want to know: is the \"embedding distribution shift\" explanation for the Verified→Live degradation empirically supported, or is it a hypothesis the paper needs to validate?\n\nUse WebSearch and WebFetch to read relevant sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7368966-1fb2-4a35-adb7-d5509a6d2b19",
  "isSidechain": false,
  "requestId": "req_011CatZjX57ykuGQUzozAP8a",
  "type": "assistant",
  "uuid": "45417cfd-2bcb-427d-9363-9947c600cdb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0124KtSAh4LrRrNvUmNhETqq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 985,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 43814,
      "output_tokens": 5016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 985,
          "output_tokens": 5016,
          "cache_read_input_tokens": 43814,
          "cache_creation_input_tokens": 3541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3541
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
  "leafUuid": "45417cfd-2bcb-427d-9363-9947c600cdb8",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Structured Specification Extraction for Guided Program Repair",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232"
}
```

---

### Tool result

_source line 20 · 2026-05-10T08:26:12.376Z_

<details><summary>↩ Tool result · `toolu_013nmNf4J1y7sXovEqpNWSDK`</summary>

```text
Based on my comprehensive search, I can now provide you with findings about the claim regarding Agentless's degradation and the "embedding distribution shift" explanation.

## Verification of the Embedding Distribution Shift Claim

**The "embedding distribution shift" explanation is NOT empirically supported by the papers I reviewed.** Here are the key findings:

### What the SWE-bench Goes Live Paper Actually Says

The paper (2505.23419) does NOT attribute Agentless's degradation to embedding distribution shift or OpenAI text-embedding-3-small knowledge cutoff issues. Instead:

1. **The explanation offered is benchmark overfitting**, not embedding OOD degradation. The authors state: "existing agents may be overfit or implicitly optimized for the SWE-bench repositories."

2. **Empirical evidence of overfitting**: Agents perform better on instances from original SWE-bench repositories (22.96% resolved) versus new repositories (18.89% resolved), but the paper frames this as evidence of dataset-specific optimization, not embedding model limitations.

3. **Embedding distribution shift is not mentioned** anywhere in the paper's explanation of performance degradation.

### The Actual Performance Numbers

From the SWE-bench Goes Live paper:
- **Agentless + Claude 3.7 Sonnet on SWE-bench-Live Lite: 11.33%**
- **Agentless + DeepSeek V3 on SWE-bench-Live Lite: 13.33%** (this is the 13.33% mentioned)

However, the paper does NOT report Agentless results on SWE-bench Verified directly. The 50.8% figure you cited may come from a different source or context.

### What We Know About text-embedding-3-small

A critical finding: **text-embedding-3-small has a September 2021 knowledge cutoff**, NOT a 2024 cutoff. This is documented in OpenAI community forums. The model was released in January 2024 but maintained the same knowledge cutoff as its predecessor (text-embedding-ada-002), which is pre-2022. This could theoretically cause OOD issues with post-2024 code repositories, but:

- **No paper directly attributes Agentless degradation to this cutoff**
- The "Saving SWE-Bench" paper (2510.08996) uses text-embedding-3-**large** and finds embedding distribution shifts between formal benchmark queries and realistic user queries, but this is about query phrasing style, NOT knowledge cutoff issues

### What Actually Explains the Verified→Live Degradation

Multiple factors are documented:

1. **Problem difficulty**: SWE-bench-Live includes newer repositories and issue types not in the static Verified set
2. **Benchmark contamination**: Models trained on pre-2024 data may have seen SWE-bench Verified instances during training
3. **Repository diversity**: Original SWE-bench covers only ~12 repositories; Live has 223+ repositories with different codebases
4. **Query format differences**: The "Saving SWE-Bench" paper shows distribution shifts between formal GitHub issues and realistic developer queries

### The Bottom Line

**The "embedding distribution shift due to Sept 2021 knowledge cutoff" explanation is a hypothesis NOT validated by the papers.** The SWE-bench Goes Live paper attributes degradation to benchmark overfitting and dataset differences, not embedding model knowledge cutoffs. This claim requires explicit empirical testing (e.g., replacing text-embedding-3-small with a model having newer training data and measuring improvement) which the papers do not provide.

---

Sources:
- [SWE-bench Goes Live! (2505.23419)](https://arxiv.org/html/2505.23419)
- [Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489)
- [Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation](https://arxiv.org/html/2510.08996v1)
- [OpenAI text-embedding-3-small Model Documentation](https://developers.openai.com/api/docs/models/text-embedding-3-small)
- [What is the training data knowledge cutoff date for text-embedding-3-large? - OpenAI Developer Community](https://community.openai.com/t/what-is-the-training-data-knowledge-cutoff-date-for-text-embedding-3-large/1361283)
- [Dissecting the SWE-Bench Leaderboards](https://arxiv.org/html/2506.17208v2)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45417cfd-2bcb-427d-9363-9947c600cdb8",
  "isSidechain": false,
  "promptId": "841e7564-2d90-4ce1-a88b-806aacd71345",
  "type": "user",
  "uuid": "03498d19-cd5d-4cf4-b04c-13cec9866344",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify one specific claim in a research paper for adversarial review. The paper argues that Agentless degrades from ~50.8% on SWE-bench Verified to ~13.33% on SWE-bench-Live Lite primarily due to \"embedding distribution shift\" - specifically that the OpenAI text-embedding-3-small model used by Agentless hasn't indexed post-2024 repository structures.\n\nPlease search for:\n1. \"site:arxiv.org SWE-bench-Live 2505.23419\" - fetch or search for the actual paper to see if it discusses WHY Agentless degrades so dramatically (4x) from Verified to Live - is it attributed to distribution shift, harder problems, or something else?\n2. \"Agentless SWE-bench degradation distribution shift embedding\" - any papers analyzing why Agentless performs worse on harder/newer benchmarks?\n3. \"OpenAI text-embedding-3-small out of distribution code retrieval\" - any papers documenting this specific embedding model's OOD degradation on code retrieval?\n4. Also search: \"SWE-bench Verified vs Live difficulty\" - any analysis of whether the 4x gap is about problem difficulty vs embedding quality?\n\nI want to know: is the \"embedding distribution shift\" explanation for the Verified→Live degradation empirically supported, or is it a hypothesis the paper needs to validate?\n\nUse WebSearch and WebFetch to read relevant sections.",
    "agentId": "ae669b1bb81e25cce",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my comprehensive search, I can now provide you with findings about the claim regarding Agentless's degradation and the \"embedding distribution shift\" explanation.\n\n## Verification of the Embedding Distribution Shift Claim\n\n**The \"embedding distribution shift\" explanation is NOT empirically supported by the papers I reviewed.** Here are the key findings:\n\n### What the SWE-bench Goes Live Paper Actually Says\n\nThe paper (2505.23419) does NOT attribute Agentless's degradation to embedding distribution shift or OpenAI text-embedding-3-small knowledge cutoff issues. Instead:\n\n1. **The explanation offered is benchmark overfitting**, not embedding OOD degradation. The authors state: \"existing agents may be overfit or implicitly optimized for the SWE-bench repositories.\"\n\n2. **Empirical evidence of overfitting**: Agents perform better on instances from original SWE-bench repositories (22.96% resolved) versus new repositories (18.89% resolved), but the paper frames this as evidence of dataset-specific optimization, not embedding model limitations.\n\n3. **Embedding distribution shift is not mentioned** anywhere in the paper's explanation of performance degradation.\n\n### The Actual Performance Numbers\n\nFrom the SWE-bench Goes Live paper:\n- **Agentless + Claude 3.7 Sonnet on SWE-bench-Live Lite: 11.33%**\n- **Agentless + DeepSeek V3 on SWE-bench-Live Lite: 13.33%** (this is the 13.33% mentioned)\n\nHowever, the paper does NOT report Agentless results on SWE-bench Verified directly. The 50.8% figure you cited may come from a different source or context.\n\n### What We Know About text-embedding-3-small\n\nA critical finding: **text-embedding-3-small has a September 2021 knowledge cutoff**, NOT a 2024 cutoff. This is documented in OpenAI community forums. The model was released in January 2024 but maintained the same knowledge cutoff as its predecessor (text-embedding-ada-002), which is pre-2022. This could theoretically cause OOD issues with post-2024 code repositories, but:\n\n- **No paper directly attributes Agentless degradation to this cutoff**\n- The \"Saving SWE-Bench\" paper (2510.08996) uses text-embedding-3-**large** and finds embedding distribution shifts between formal benchmark queries and realistic user queries, but this is about query phrasing style, NOT knowledge cutoff issues\n\n### What Actually Explains the Verified→Live Degradation\n\nMultiple factors are documented:\n\n1. **Problem difficulty**: SWE-bench-Live includes newer repositories and issue types not in the static Verified set\n2. **Benchmark contamination**: Models trained on pre-2024 data may have seen SWE-bench Verified instances during training\n3. **Repository diversity**: Original SWE-bench covers only ~12 repositories; Live has 223+ repositories with different codebases\n4. **Query format differences**: The \"Saving SWE-Bench\" paper shows distribution shifts between formal GitHub issues and realistic developer queries\n\n### The Bottom Line\n\n**The \"embedding distribution shift due to Sept 2021 knowledge cutoff\" explanation is a hypothesis NOT validated by the papers.** The SWE-bench Goes Live paper attributes degradation to benchmark overfitting and dataset differences, not embedding model knowledge cutoffs. This claim requires explicit empirical testing (e.g., replacing text-embedding-3-small with a model having newer training data and measuring improvement) which the papers do not provide.\n\n---\n\nSources:\n- [SWE-bench Goes Live! (2505.23419)](https://arxiv.org/html/2505.23419)\n- [Agentless: Demystifying LLM-based Software Engineering Agents](https://arxiv.org/abs/2407.01489)\n- [Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation](https://arxiv.org/html/2510.08996v1)\n- [OpenAI text-embedding-3-small Model Documentation](https://developers.openai.com/api/docs/models/text-embedding-3-small)\n- [What is the training data knowledge cutoff date for text-embedding-3-large? - OpenAI Developer Community](https://community.openai.com/t/what-is-the-training-data-knowledge-cutoff-date-for-text-embedding-3-large/1361283)\n- [Dissecting the SWE-Bench Leaderboards](https://arxiv.org/html/2506.17208v2)"
      }
    ],
    "totalDurationMs": 119011,
    "totalTokens": 33730,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 32091,
      "output_tokens": 1092,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 544
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1092,
          "cache_read_input_tokens": 32091,
          "cache_creation_input_tokens": 544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 544,
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
  "sourceToolAssistantUUID": "45417cfd-2bcb-427d-9363-9947c600cdb8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T08:26:42.451Z_

<details><summary>Logged reasoning block</summary>

```text
This is a significant finding. The embedding distribution shift explanation used by SpecExtract to justify why BM25 on structured tokens helps on SWE-bench-Live is NOT empirically supported by the SWE-bench Goes Live paper. Instead, the paper attributes the degradation to benchmark overfitting (models were trained on SWE-bench data and are now tested on out-of-distribution issues), not embedding distribution shift.

This means the mechanistic justification for SpecExtract's +4-7 pp improvement (specifically the BM25-on-structured-tokens robustness argument) may be based on a false premise. The actual cause of degradation might be:


- Model overfitting to SWE-bench patterns rather than an embedding problem
- Different problem difficulty or repository diversity

If the real bottleneck is the repair model's ability to generalize to unseen repositories rather than retrieval quality, then SpecExtract's BM25 signal might not deliver the claimed benefits. That said, the embedding model's September 2021 knowledge cutoff is still a legitimate concern for post-2024 repositories, even if the SWE-bench-Live paper doesn't explicitly attribute degradation to this factor.

The BM25 contribution on extracted interface tokens remains valid as an independent retrieval signal that could improve recall regardless of the root cause of baseline degradation. However, this weakens the mechanistic argument since it was built on the assumption that embedding distribution shift is the primary problem. I need to flag that the case for the +4-7 percentage point improvement should either drop the embedding distribution shift hypothesis as the main driver, provide empirical evidence for it, or reframe the contribution as simply adding another retrieval signal for diverse repositories without making specific claims about distribution shift. This is a significant issue the generator needs to address.

Now I'm compiling my final review scores. Novelty is solid at 3.5 given the genuine novelty in the task definition and spec extraction approach, though the methods themselves are incremental. Feasibility drops to 3.0 because the mechanistic justification relies on an unsupported hypothesis—the actual degradation on Live code appears to stem from model overfitting rather than embedding distribution shift, which undermines the specific case for why BM25 on structured tokens would help. Clarity remains strong at 4.5 for the detailed specification. Impact also sits at 3.0 since the flawed mechanistic justification casts doubt on whether the predicted improvement will actually materialize.

Wait, let me reconsider whether this is truly a critical flaw or something more manageable. The improvement argument has two parts: BM25 on extracted interface tokens for distribution-shift-robust retrieval, and behavioral delta injection for better-constrained patch generation. Even if the embedding distribution shift reasoning is wrong, the structured interface tokens themselves—like specific module names and class references—still provide valuable lexical signals that BM25 can leverage effectively, independent of the distribution shift concern.

For the EMNLP paper, I need to reframe this: drop the specific claim about post-2024 repository distribution shifts, reposition BM25 as providing high-precision lexical matching that complements semantic similarity, and attribute the Verified→Live degradation to benchmark overfitting rather than embedding OOD issues. This is a moderate issue requiring revision but not a fundamental invalidation of the approach.

The core problem is that I'm claiming SpecExtract's BM25 advantage stems from Agentless's embedding-based localization failing on newer repos due to training data cutoffs, but the SWE-bench-Live paper actually attributes that degradation to benchmark overfitting, not knowledge cutoff. Without direct evidence linking the Verified→Live drop to embedding model training dates, the mechanistic justification needs either empirical support or a weaker framing.

There's also a gap between asserting that SpecExtract is pipeline-agnostic and reusable across different repair backbones versus only evaluating it with Agentless in the EMNLP submission—I should be explicit about that limitation rather than implying broader applicability. Similarly, the claim that SWE-Lego provides orthogonal gains as a preprocessing front-end is stated but never actually demonstrated in the work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03498d19-cd5d-4cf4-b04c-13cec9866344",
  "isSidechain": false,
  "requestId": "req_011Cata19yZPDEjFFFYSqHYM",
  "type": "assistant",
  "uuid": "4c08a20e-3834-4471-b5b3-d0516a5f0b58",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UG4y93ckeKL8ugYgW1GhVk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7090,
      "cache_read_input_tokens": 47355,
      "output_tokens": 3769,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7090,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3769,
          "cache_read_input_tokens": 47355,
          "cache_creation_input_tokens": 7090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7090
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

_source line 22 · 2026-05-10T08:27:20.187Z_

Now I have sufficient evidence to complete my review. Let me compile the final assessment.

**Key findings from independent research:**

1. **All numerical claims verified**: RGFL numbers (71.4%→85% Hit@1, $4.4/instance, +12.8%), SWE-bench-Live Agentless numbers (11.67%/12.00%/13.33%), SWE-Lego (52.6% Verified), Agent-CoEvo (41.33% Lite) — all confirmed accurate.

2. **Core novelty claim holds**: No prior work trains a dedicated supervised model to extract structured specifications from bug report text (issue-space) for repair preprocessing. CodeSpecBench benchmarks LLM prompting on code-side spec generation; SpecFix repairs benchmark descriptions — neither competes with SpecExtract's specific framing.

3. **CRITICAL: Embedding distribution shift claim is unsupported**: The SWE-bench-Live paper (arXiv 2505.23419) attributes Agentless's 4× degradation from Verified to Live to **benchmark overfitting** (agents optimized for original SWE-bench repositories), not embedding model knowledge-cutoff issues. The specific mechanistic argument — "Agentless's embedding-based localization degrades because text-embedding-3-small hasn't indexed post-2024 repo structures" — is a hypothesis not validated in the literature. This weakens the mechanistic case for SpecExtract's BM25-on-structured-tokens advantage being specifically distribution-shift-robust.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 4,
      "rationale": "Issue-space supervised spec extraction as a structured IE task is genuinely novel — no prior work trains a dedicated model mapping (bug_report_text, runtime_artifacts) → typed behavioral spec for repair preprocessing. CodeSpecBench and SpecFix occupy different niches. The masked-field training protocol and schema design are methodologically distinct."
    },
    "feasibility": {
      "score": 3,
      "rationale": "The compute budget (~90-110 H100-hours manual) is within constraints and all models/tools are available. However, the +4-7 pp improvement target relies critically on a mechanistic argument (embedding distribution shift on post-2024 repos) that the SWE-bench-Live paper itself does not support — attributing Agentless's 4x degradation to benchmark overfitting, not OOD embedding quality. The improvement may still materialize from BM25 lexical matching and behavioral delta injection, but the mechanistic case is weaker than presented."
    },
    "clarity": {
      "score": 5,
      "rationale": "Exceptionally detailed and self-consistent after 9 rounds: formal schema with worked example, explicit compute partitioning, McNemar's statistical significance plan, EMNLP pilot scope clearly separated from ICSE 2027 full results, all related work comprehensively positioned."
    },
    "impact": {
      "score": 3,
      "rationale": "A preprocessing module predicting +4-7 pp on a 300-instance benchmark is a modest empirical contribution, and the mechanistic justification for why it helps on out-of-distribution repos has an evidential gap. The cost-efficiency story (40-80× cheaper than RGFL) is compelling if the improvement materializes, but EMNLP reviewers will push hard on whether the delta is reproducible and attributable to the proposed mechanism."
    }
  },
  "issues": [
    "MODERATE (NEW) — Embedding distribution shift attribution is contradicted by the SWE-bench-Live paper: The proposal's mechanistic justification for BM25-on-structured-tokens advantage states 'Agentless's embedding-based file localization degrades on post-2024 SWE-bench-Live repos underrepresented in embedding model training data.' However, independent verification of arXiv 2505.23419 shows the paper attributes the 4× Verified→Live degradation primarily to benchmark overfitting ('existing agents may be overfit or implicitly optimized for the SWE-bench repositories'), not embedding OOD issues. Text-embedding-3-small's September 2021 knowledge cutoff is a real constraint, but no paper directly links this to Agentless's Live degradation. The mechanistic case for why BM25 specifically outperforms embedding retrieval on post-2024 repos is unsupported by the cited evidence and must be reframed.",
    "MINOR (NEW) — Pipeline-agnosticism is claimed but not empirically scoped in the EMNLP submission: The proposal asserts SpecExtract is 'pipeline-agnostic' and 'reusable across repair backbones without retraining,' but the EMNLP ARR submission evaluates only SpecExtract+Agentless. The broader portability claim (to SWE-agent, Moatless, SWE-Lego) is untested. This should be explicitly scoped as 'demonstrated for Agentless; portability to other backbones is deferred to ICSE 2027' to avoid reviewer objections about overclaiming.",
    "MINOR — SWE-Lego 'orthogonal gains as preprocessing front-end' is asserted but not demonstrated: The proposal lists SWE-Lego (52.6% Verified) as a baseline 'to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end,' but no SpecExtract+SWE-Lego experiment is in the EMNLP submission scope. Either remove this claim or clarify it as a future direction, since reviewers will ask for the experiment."
  ],
  "feedback": "The Round 9 submission has successfully addressed all Round 8 issues: RGFL and SWE-Fixer are comprehensively integrated into the landscape with clean differentiation, McNemar's statistical significance is addressed, and the mechanistic case for improvement is substantially developed. One new finding from independent research blocks passing in Round 9.\n\n**(1) URGENT — Fix the embedding distribution shift attribution**: Independent verification of the SWE-bench-Live paper (arXiv 2505.23419) shows it attributes Agentless's 4× Verified→Live degradation to benchmark overfitting (agents optimized for original SWE-bench repos), not embedding OOD due to knowledge cutoff. The proposal's specific mechanistic claim — 'embedding similarity between an issue query and post-2024 codebase chunks is noisier... because the model has not seen those module structures and naming conventions during pretraining' — is a hypothesis not validated in the cited literature. Fix this in two ways: (a) replace the distribution shift claim with the correct empirical framing from arXiv 2505.23419: 'Agentless's degradation on SWE-bench-Live reflects benchmark overfitting to the original 12-repository SWE-bench corpus; the 223-repository diversity of Live exposes generalization gaps that structured interface token extraction addresses by providing high-precision lexical signals independent of the LLM backbone's prior exposure'; (b) retain the BM25 advantage argument but frame it as 'exact-match retrieval on specific module and entry-point tokens (e.g., numpy.linalg, django.db.models.QuerySet) complements semantic similarity by catching files where the lexically precise module name is the diagnostic signal' — this is defensible regardless of whether the embedding OOD hypothesis holds.\n\n**(2) Scope the pipeline-agnosticism claim**: Add one sentence explicitly bounding the EMNLP portability claim: 'In the EMNLP ARR submission, SpecExtract's pipeline-agnostic design is demonstrated via integration with Agentless; portability experiments with additional repair backbones (SWE-agent, Moatless) are deferred to ICSE 2027.' This takes 15 words and prevents reviewer objection (2).\n\n**(3) Scope or remove the SWE-Lego front-end orthogonality claim**: Change 'SWE-Lego is included as an end-to-end SFT baseline to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end' to 'SWE-Lego (52.6% Verified, 32B) is included as a comparison point representing state-of-the-art end-to-end SFT repair; direct SpecExtract+SWE-Lego integration is a future direction.' This correctly scopes what the EMNLP paper actually shows.\n\nWith fix (1) — particularly replacing the distribution shift hypothesis with the correct overfitting attribution and reframing BM25's value — the mechanistic case for the +4-7 pp improvement will be both accurate and defensible. Fixes (2) and (3) are 15-word scoping additions.",
  "reason": "All Round 8 issues resolved, but a new finding reveals the core mechanistic justification for the improvement target (BM25 distribution-shift-robustness on post-2024 repos) is contradicted by the SWE-bench-Live paper's own attribution of Agentless degradation to benchmark overfitting — a targeted reframing unblocks passing."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c08a20e-3834-4471-b5b3-d0516a5f0b58",
  "isSidechain": false,
  "requestId": "req_011Cata19yZPDEjFFFYSqHYM",
  "type": "assistant",
  "uuid": "a84ed1e9-5b4b-4b42-99e0-d5f0775230ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UG4y93ckeKL8ugYgW1GhVk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7090,
      "cache_read_input_tokens": 47355,
      "output_tokens": 3769,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7090,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3769,
          "cache_read_input_tokens": 47355,
          "cache_creation_input_tokens": 7090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7090
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
  "leafUuid": "a84ed1e9-5b4b-4b42-99e0-d5f0775230ca",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Structured Specification Extraction for Guided Program Repair",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "a84ed1e9-5b4b-4b42-99e0-d5f0775230ca",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Structured Specification Extraction for Guided Program Repair",
  "sessionId": "9441f046-d0fc-42fd-a7f5-74a8892b6232"
}
```

---
