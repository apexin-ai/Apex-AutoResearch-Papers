# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-10 (UTC).** Your job: indep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b.jsonl`
- **Structured JSON:** [`90c025fffe873f1ec3f5.json`](../../sessions/90/90c025fffe873f1ec3f5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T18:40:10.189Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T18:40:10.189Z",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-10 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.\n\nDirection: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.\n\nContribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.\n2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).\n3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.\n\nLook for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.\n\nTag: direction=code_models, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-10?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 4/10)\n{\n  \"title\": \"StructFuse: Fusing Data-Flow and Lexical Signals for Repository-Level Code Repair Context Selection\",\n  \"core_problem\": \"Repository-level bug repair requires selecting relevant context from large codebases. Existing neural context selectors (SWE-Pruner, Squeez) rely on expensive LLM-generated labels (~$50-200 per labeling run), are coupled to specific teacher models, and lack structural grounding. Retrieve-and-rerank methods like SweRank achieve strong text-based localization but miss structural dependencies. Graph-guided agents like LocAgent capture import/call/inheritance edges but omit fine-grained data-flow (def-use) edges that trace variable-level dependencies across functions. On SWE-bench Pro (where top systems score 42-59% and context selection accounts for 4-10pp swings), context quality remains a dominant differentiator. Can we build a context selector that fuses data-flow structural signals with lexical retrieval in a lightweight distilled model—one that requires no LLM teacher, is model-independent, and provides interpretable, structurally-grounded selections?\",\n  \"opportunity\": \"SWE-Pruner (arXiv:2601.16746) demonstrated a 0.6B neural skimmer can reduce tokens 23-54% with <1pp degradation on SWE-bench Verified, but its supervision comes entirely from Qwen3-Coder-30B inference. LocAgent (ACL 2025) showed graph-guided localization achieves 92.7% file-level accuracy on SWE-bench Lite, but uses only import/invocation/inheritance edges—not data-flow. SweRank (arXiv:2505.07849) achieves SOTA retrieve-and-rerank localization but is purely text-based. ARISE (arXiv:2605.03117) confirmed data-flow slicing yields 17pp localization gains on SWE-bench Lite but keeps analysis as runtime tool calls, not distilled knowledge. Sliceformer (ACL 2026) validated that data-flow knowledge transfers to neural models with 22% ExactMatch gains. The opportunity: no existing work distills data-flow structural signals into a lightweight, fast model for repair context selection. LocAgent's graph lacks def-use edges; ARISE's data-flow is runtime-only; SweRank ignores structure entirely. Fusing data-flow features with lexical retrieval in a trained model fills this gap—cheap to supervise (program analysis, not LLM inference), model-independent, and fast at inference.\",\n  \"landscape\": \"**Neural context selectors**: SWE-Pruner trains a 0.6B skimmer on 61K LLM-labeled samples, achieving <1pp degradation on SWE-bench Verified (70.6%→70.2%)—but relies on expensive Qwen3-Coder-30B labels and the Verified benchmark is known contaminated (OpenAI, Feb 2026). Squeez (arXiv:2604.04979) fine-tunes Qwen 3.5 2B for task-conditioned tool-output pruning (0.86 recall, 92% token removal) but targets tool outputs, not repository context. LongCodeZip (ASE 2025) achieves 5.6x compression via perplexity-based ranking, training-free but code-agnostic. **Retrieve-and-rerank approaches**: SweRank (arXiv:2505.07849) achieves SOTA issue localization via SweRankEmbed (bi-encoder retriever) + SweRankLLM (listwise LLM reranker), outperforming both prior models and agent-based systems. SweRank+ (arXiv:2512.20482) extends to multilingual multi-turn ranking with 155K training instances. Both are purely text-based with no structural signals. **Graph-guided approaches**: LocAgent (ACL 2025, arXiv:2503.09089) parses codebases into directed heterogeneous graphs with import/invocation/inheritance edges, achieving 92.7% file-level accuracy with fine-tuned Qwen2.5-32B—but omits data-flow (def-use) edges and requires a 32B model at inference. KGCompass (arXiv:2503.21710) constructs repository knowledge graphs (58.3% repair) but with heavy construction overhead. **Data-flow-specific approaches**: ARISE (arXiv:2605.03117) augments SWE-agent with statement-level def-use edges, gaining 17pp Function Recall@1 and 4.7pp Pass@1—but keeps analysis as runtime tool calls, adding latency at inference. LLMxCPG (USENIX Security 2025) uses Code Property Graphs for vulnerability detection (67-91% code reduction, 15-40% F1 gain) but targets security, not repair context. Sliceformer (ACL 2026) distills DFG knowledge into CodeT5+ for slicing tasks, validating structural knowledge transfer but not addressing repair. **Compression paradigms**: A recent empirical study (arXiv:2604.13725) shows continuous latent vector compression surpasses full-context by up to 28.3% BLEU at 4x compression—demonstrating that intelligent filtering outperforms naive truncation, though text-level selection remains complementary and more interpretable. **Benchmarks**: SWE-bench Pro (Scale AI, 1865 tasks) is the recommended hard benchmark; SWE-bench Lite (300 instances) remains widely used; RepoBench-R (ICLR 2024) directly evaluates cross-file context retrieval; SWE-ContextBench (arXiv:2602.08316) provides 1100+376 tasks for context evaluation. **Gap**: No existing work distills data-flow (def-use) signals into a lightweight model for repair context selection. LocAgent uses structural edges but not def-use; SweRank is text-only; ARISE uses def-use but only at runtime. The fusion of data-flow features with lexical retrieval in a fast, distilled model is unexplored.\",\n  \"approach\": \"We propose StructFuse, a multi-signal context selector that fuses data-flow structural features with lexical retrieval signals in a lightweight distilled model for repository-level code repair context selection.\\n\\n**Stage 1: Multi-Signal Feature Extraction (Days 1-3).** For 5K SWE-smith training instances across ~80-100 of the 128 available repositories, we extract three signal types: (a) *Data-flow features*: Using CodeQL for inter-procedural def-use analysis and call-graph construction on the ~128 shared repositories (each needing one database build), augmented by Beniget for intra-file def-use chains where CodeQL databases fail (~20-30% of repos). For each candidate file/function, we compute: graph distance to buggy location, number of data-flow paths, dependency type (def-use, call-graph, import). (b) *Lexical features*: BM25 similarity between issue description and candidate code, plus SweRankEmbed scores as a strong retrieval baseline. (c) *Structural metadata*: File co-change frequency from git history, import distance, directory distance. We explicitly acknowledge Python's dynamic features (eval, metaclasses, monkey-patching) limit static analysis coverage and quantify this via a validation step on 500 instances before full-scale extraction.\\n\\n**Stage 2: Fusion Model Training (Days 4-5).** We train a Qwen2.5-Coder-3B model via LoRA SFT on multi-signal fusion. The model receives structured multi-signal representations (data-flow graph features, BM25/SweRankEmbed scores, structural metadata) as input alongside the code context and learns to predict file/function-level relevance. We apply data-flow-guided loss weighting: candidates with strong structural connections receive higher loss weight, encoding the inductive bias that structurally-connected code is more reliably relevant than lexically-similar code. We are transparent that this training methodology—multi-source features as input with confidence-weighted loss—is technically standard; the contribution lies in demonstrating that data-flow signals provide effective supervision without LLM teachers and that the specific signal combination yields empirical gains. Training takes ~2-4 hours per run on a single H100; we run 5 ablation configurations (data-flow only, lexical only, full fusion, with/without loss weighting, CodeQL inter-procedural vs. Beniget intra-file only).\\n\\n**Stage 3: Evaluation (Days 6-10).** The distilled selector plugs into SWE-agent as a drop-in context retrieval component. We evaluate on: (a) SWE-bench Lite (300 instances, full), (b) SWE-bench Pro public split (500-instance stratified sample of 731 public instances), (c) RepoBench-R (cross-file retrieval evaluation, no LLM needed). Metrics: localization recall@k (file and function level), end-to-end Pass@1 repair rate, token efficiency. End-to-end evaluation uses Qwen3.6-27B exclusively (open-weight, no API costs). We compare against: (i) SweRank/SweRankEmbed (SOTA text-based retrieval), (ii) SWE-Pruner (LLM-labeled selector), (iii) BM25 baseline, (iv) LocAgent's graph-guided approach (import/call/inheritance edges, no def-use), (v) no-pruning full-context. Key ablations isolate each signal type's contribution.\\n\\n**Stage 4: Writing (Days 10-15).** The central hypothesis: on hard benchmarks, the fusion of data-flow + lexical signals outperforms either alone—and achieves comparable or better performance than LLM-labeled selectors at zero labeling cost. The paper frames StructFuse as an empirical and systems contribution: (a) first demonstration that program-analysis-derived data-flow features provide effective, free supervision for context selection, (b) empirical evidence that def-use edges complement the import/call/inheritance edges used by LocAgent and the text signals used by SweRank, (c) a practical, reproducible pipeline (CodeQL→features→3B fusion model) that is fast at inference and model-independent.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180h H100 (CodeQL database creation for ~128 repos: ~10h CPU-parallel + 5h GPU; feature extraction: ~15h; SFT training 5 ablation runs: ~20h; SWE-bench evaluation 800 instances with Qwen3.6-27B: ~120h; RepoBench-R evaluation: ~10h)\",\n      \"gpu_utilization\": \"~70-80% utilization during evaluation phase (Qwen3.6-27B inference is GPU-bound); ~30-40% during CodeQL/feature extraction\",\n      \"timeline\": \"15 days (Days 1-3: CodeQL pipeline + feature extraction; Days 4-5: SFT training + ablations; Days 6-10: evaluation; Days 10-15: writing)\",\n      \"team\": \"1-2 researchers (one with CodeQL/program analysis, one with LLM fine-tuning; can be same person)\",\n      \"estimated_gpu_cost\": \"$400-600 (180h H100 at spot ~$2.50/hr; no LLM API costs—all evaluation uses open-weight Qwen3.6-27B)\",\n      \"claude_api_cost\": \"$0 for evaluation (Qwen3.6-27B only); ~$50-100 for writing assistance\",\n      \"risk_note\": \"CodeQL database creation may fail for 20-30% of Python repos with complex dependencies; Beniget fallback covers intra-file analysis. SWE-smith repos are well-maintained open-source projects with higher-than-average build success rates.\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~150h H100 (same pipeline, agent manages CodeQL builds and queues training runs; human reviews label quality at day 2 and evaluation configs at day 5)\",\n      \"gpu_utilization\": \"~75-85% utilization; agent parallelizes independent experiments\",\n      \"timeline\": \"12-14 days\",\n      \"team\": \"1 researcher, ~45min/day check-in for label quality review and experiment approval\",\n      \"claude_api_cost\": \"$80-150 (800-1500 turns for pipeline code generation and debugging)\",\n      \"estimated_gpu_cost\": \"$350-500 (150h H100 at spot ~$2.50/hr)\",\n      \"risk_note\": \"Tight timeline requires pre-validated CodeQL setup; recommend testing on 10 repos in first 4 hours before scaling\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~200h H100 (full ablation suite, hyperparameter sweep over loss weights, multi-benchmark evaluation including RepoBench-R)\",\n      \"gpu_utilization\": \"~85-90% utilization; agent continuously launches experiments, parallelizes independent ablations\",\n      \"timeline\": \"10-12 days with 2-4 H100 GPUs available concurrently\",\n      \"team\": \"0 (initial setup: CodeQL CLI installation, SWE-smith repo cloning, SWE-bench evaluation harness)\",\n      \"claude_api_cost\": \"$200-400 (2000-4000 turns for iterative pipeline development, CodeQL query debugging, experiment scheduling)\",\n      \"estimated_gpu_cost\": \"$500-700 (200h H100 at spot ~$2.50/hr to on-demand ~$3.50/hr)\",\n      \"speed_bottleneck\": \"SWE-bench evaluation (~9min/instance × 800 instances on Qwen3.6-27B ≈ 120 H100-hours; parallelizable across GPUs)\",\n      \"risk_note\": \"Agent should validate CodeQL coverage on first 10 repos and report def-use coverage before scaling. If coverage < 50%, pivot to Beniget-only for broader but shallower analysis.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline: May 25, 2026; conference: Fall 2026; topic area: 'NLP and Code Models')\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents (arXiv:2601.16746, Jan 2026) — 0.6B skimmer, LLM-labeled, <1pp degradation on SWE-bench Verified\",\n    \"LocAgent: Graph-Guided LLM Agents for Code Localization (ACL 2025, arXiv:2503.09089) — 92.7% file-level accuracy on SWE-bench Lite using import/invocation/inheritance edges with fine-tuned Qwen2.5-32B; no def-use edges\",\n    \"SweRank: Software Issue Localization with Code Ranking (arXiv:2505.07849, May 2025) — SOTA retrieve-and-rerank, outperforms agent-based systems; text-only, no structural signals\",\n    \"SweRank+: Multilingual, Multi-Turn Code Ranking (arXiv:2512.20482, Dec 2025) — extends SweRank to multilingual multi-turn with 155K training instances\",\n    \"Sliceformer: Static Program Slicing Using Language Models With Dataflow-Aware Pretraining (ACL 2026, arXiv:2604.26961) — validates data-flow knowledge transfer to neural models\",\n    \"ARISE: Repository-level Graph Representation for Agentic Fault Localization and Repair (arXiv:2605.03117, May 2026) — def-use edges as runtime tool calls, +17pp Function Recall@1\",\n    \"LLMxCPG: Context-Aware Vulnerability Detection Through CPG-Guided LLMs (USENIX Security 2025) — CPG-guided context extraction, 67-91% code reduction\",\n    \"Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents (arXiv:2604.04979, Apr 2026) — 0.86 recall, 92% token removal on tool outputs\",\n    \"On the Effectiveness of Context Compression for Repository-Level Tasks (arXiv:2604.13725, Apr 2026) — continuous latent vectors surpass full-context by 28.3% at 4x compression\",\n    \"LongCodeZip: Compress Long Context for Code Language Models (ASE 2025, arXiv:2510.00446) — 5.6x training-free compression\",\n    \"RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems (ICLR 2024, arXiv:2306.03091) — cross-file retrieval evaluation benchmark\",\n    \"SWE-ContextBench: A Benchmark for Context Learning in Coding (arXiv:2602.08316, Feb 2026) — 1100+376 context evaluation tasks\",\n    \"On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv:2604.05481, Apr 2026) — file-level is dominant factor\",\n    \"Why SWE-bench Verified No Longer Measures Frontier Coding Capabilities (OpenAI, Feb 2026) — contamination analysis\",\n    \"SWE-bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (Scale AI, arXiv:2509.16941, 2025)\",\n    \"LLMDFA: Analyzing Dataflow in Code with Large Language Models (NeurIPS 2024)\",\n    \"SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025 D&B Spotlight)\",\n    \"SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (ICLR 2024)\"\n  ],\n  \"description\": \"We propose StructFuse, a multi-signal context selector for repository-level code repair that fuses data-flow (def-use) structural features with lexical retrieval signals in a lightweight 3B distilled model. Unlike SWE-Pruner (expensive LLM-labeled supervision), SweRank (text-only retrieval), and LocAgent (import/call/inheritance edges but no def-use), StructFuse extracts inter-procedural def-use chains via CodeQL and fuses them with BM25/SweRankEmbed retrieval scores in a Qwen2.5-Coder-3B model trained with LoRA SFT. The contribution is empirical and practical, not methodological: (1) we demonstrate that program-analysis-derived data-flow features provide effective supervision for context selection without any LLM teacher—zero labeling cost vs. ~$50-200 for LLM-supervised methods; (2) we show that def-use edges complement the coarser structural edges (import/call/inheritance) used by LocAgent and the text signals used by SweRank, with fusion outperforming either signal type alone; (3) the resulting pipeline (CodeQL→features→3B fusion model) is fast at inference, model-independent, and provides interpretable selections with traceable data-flow paths to the bug. We evaluate on SWE-bench Lite (300 instances), a 500-instance SWE-bench Pro subset, and RepoBench-R (cross-file retrieval), using only open-weight Qwen3.6-27B for end-to-end repair evaluation (no API costs). We target EMNLP 2026 under the 'NLP and Code Models' topic area, with a 15-day implementation sprint fitting within 200 H100-hours.\",\n  \"project_name\": \"structfuse_context\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING REFERENCE: Sliceformer (arXiv:2604.26961, ACL 2026, April 2026) distills data-flow knowledge into neural models using tree-sitter DFGs—conceptually very close. Must acknowledge and differentiate.\", \"CRITICAL MISSING REFERENCE: SWE-Pruner (arXiv:2601.16746, Jan 2026) uses a 0.6B neural skimmer for line-level context pruning in coding agents—same architecture concept, different training signal.\", \"16-day timeline is not credible: ARISE code is unreleased (confirmed), Tree Climber only supports intra-procedural analysis, and OPCD requires iterative generate-then-train loops that multiply wall-clock time.\", \"27B model contradicts the 'fast inference' framing: Qwen3.6-27B requires 1-3 seconds per forward pass. The '10-50x lower latency vs ARISE' claim only holds if comparing against multi-round tool-call overhead, not against the actual static analysis (tree-sitter is fast).\", \"Weak baseline concern: ARISE's 22.0% on SWE-bench Lite is far below SOTA (62.7%). If the distilled selector is only evaluated as a replacement in ARISE-level systems, absolute gains will appear modest.\", \"OPCD complexity vs. timeline: On-policy distillation requires multiple rounds of student generation + training. Standard SFT with data-flow labels would be far simpler and more feasible within constraints.\", \"Inter-procedural gap: The proposal claims repo-level context selection but Tree Climber only supports intra-procedural def-use chains. Scaling to cross-function/cross-file data-flow for SWE-bench instances is a significant unsolved engineering challenge.\"]\nFeedback: This idea has a valid core insight (distilling static analysis signals into a neural context selector is more principled than LLM-generated relevance labels), but needs significant revision to be feasible within constraints and differentiated from concurrent work:\n\n1. **Acknowledge and differentiate from Sliceformer (ACL 2026)**: This paper already distills data-flow into neural models via pretraining objectives on DFGs. Your differentiation is: (a) application to repair context selection rather than slicing, (b) on-policy distillation rather than pretraining objectives, (c) end-to-end evaluation on repair. Make this explicit.\n\n2. **Acknowledge SWE-Pruner**: Position your work as replacing SWE-Pruner's LLM-teacher signal with ground-truth data-flow signals, showing that structural program analysis provides better training signal than LLM-generated relevance.\n\n3. **Simplify the method for 16-day feasibility**: Drop OPCD. Use standard SFT with binary labels (data-flow-relevant vs. not) as supervision. This cuts training to a single pass and dramatically reduces complexity. Frame OPCD as future work.\n\n4. **Use a smaller model**: A 7B model (e.g., Qwen3-8B or Qwen2.5-Coder-7B) would genuinely achieve fast inference AND fit the compute budget better. The 'distilled fast selector' narrative is more convincing with a small model.\n\n5. **Scope down data generation**: Instead of full repo-level inter-procedural analysis (which Tree Climber can't do), use intra-procedural def-use chains + simple call-graph edges (tree-sitter can extract these). Be honest about this limitation.\n\n6. **Strengthen evaluation**: Evaluate as a plug-in context selector for a STRONG agent (not just ARISE-level), e.g., plug into SWE-agent with Qwen3.6-27B as the repair model. This would show the selector helps even with capable models.\n\n7. **Realistic timeline**: With simplified SFT + 7B model + scoped data pipeline, 16 days becomes plausible: ~5 days data pipeline, ~3 days training + iteration, ~5 days evaluation, ~3 days writing.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL: SWE-Pruner 70.2% framing is misleading. Verified via full paper: the baseline WITHOUT SWE-Pruner achieves 70.6% with Claude Sonnet 4.5. SWE-Pruner DEGRADES performance by 0.4pp (to 70.2%) while reducing tokens 23%. The idea frames 70.2% as SWE-Pruner's achievement, but LLM labels already produce near-perfect context selection. This means the improvement ceiling from better labels is extremely narrow — at best recovering 0.4pp.\", \"CRITICAL: Narrow improvement ceiling undermines motivation. If LLM-generated labels already enable <1% degradation from the unpruned baseline, the core argument ('LLM labels are noisy and can be improved with structural signals') is empirically weak. The value proposition must be reframed: data-flow labels are (a) cheaper (no LLM teacher needed), (b) model-independent, (c) more interpretable — NOT necessarily higher quality.\", \"CRITICAL: SWE-bench Verified is now considered a compromised benchmark. OpenAI stopped reporting Verified scores in Feb 2026 after finding models reproduce verbatim gold patches. Evaluating only on Verified severely weakens the paper. Must add SWE-bench Pro evaluation (top SOTA: ~46-77% depending on scaffolding, much harder and uncontaminated).\", \"MISSING REFERENCE: Squeez (arXiv:2604.04979, April 2026) — another task-conditioned context pruning approach for coding agents using fine-tuned Qwen 3.5 2B with LoRA, achieving 0.86 recall and 92% token removal. Must be discussed and compared as a concurrent context pruning method.\", \"MISSING REFERENCE: LongCodeZip (ASE 2025, arXiv:2510.00446) — code compression using conditional perplexity ranking + knapsack pruning. Achieves 5.6x compression. A relevant baseline for context compression.\", \"MISSING REFERENCE: SWE Context Bench (arXiv:2602.08316, Feb 2026) — a benchmark specifically for evaluating context learning/selection in coding tasks. Should be used for evaluation.\", \"Tree-sitter def-use extraction for Python is underspecified. Tree-sitter is a parser, not a static analysis tool. Tree Climber only supports C. The proposal says 'we run intra-procedural def-use chain analysis via tree-sitter' without specifying what existing tool or library will be used, or acknowledging that this must be built from scratch. For Python's dynamic typing, metaclasses, monkey patching, and eval, the resulting labels will be very noisy. The proposal should either: (a) specify using a proper Python type-aware tool like Pyright/Jedi for more complete analysis, (b) quantify expected label noise and demonstrate noisy labels still provide useful signal, or (c) restrict scope to statically-typed Python patterns.\", \"Method contribution is too thin for EMNLP Main. The actual method is: (1) extract def-use chains, (2) use as binary labels, (3) train standard SFT. Steps 2-3 are trivially standard. The entire contribution rests on the labeling strategy, making this an empirical study rather than a method paper. Consider reframing as an empirical contribution or adding a methodological innovation (e.g., hybrid labels combining data-flow and LLM signals, curriculum over label sources, or data-flow-aware loss weighting).\", \"MISSING REFERENCE: LLMxCPG (USENIX Security 2025) uses Code Property Graphs (including data-flow edges) to guide an LLM in extracting vulnerability-relevant code slices. Very similar paradigm (program analysis guides neural context extraction), though for vulnerability detection. Should be discussed as related work from an adjacent domain.\"]\nFeedback: The revised idea has addressed most Round 1 issues well (Sliceformer/SWE-Pruner positioning, dropping OPCD, 7B model, scoped data generation). However, critical new issues have emerged from deep verification:\n\n1. **Reframe the motivation around cost and independence, not quality**: The SWE-Pruner data shows LLM labels already produce near-optimal context selection (<1% degradation). Your story should NOT be 'data-flow labels are higher quality than LLM labels' — it should be: 'data-flow labels are (a) 100x cheaper to produce (no expensive LLM teacher inference), (b) model-independent (no coupling to a specific teacher like Qwen3-Coder-30B), (c) structurally grounded and interpretable, and (d) potentially complementary to LLM labels.' Consider a hybrid approach: data-flow labels + LLM labels combined could outperform either alone.\n\n2. **Add SWE-bench Pro to evaluation**: SWE-bench Verified is compromised. Add SWE-bench Pro (and/or SWE-bench Live) to the evaluation plan. This also addresses a harder benchmark where context selection may matter more (the unpruned baseline won't be 70%+ on Pro).\n\n3. **Specify the def-use extraction tool concretely**: Don't just say 'tree-sitter def-use analysis' — tree-sitter is a parser. You need to build a custom analysis pass on top of tree-sitter ASTs. Consider: (a) using scope_resolution + assignment patterns from tree-sitter to build intra-function def-use chains, (b) using call_expression nodes for one-hop call-graph edges. Alternatively, consider using Jedi (a Python static analysis library with type inference) for better def-use coverage. Quantify the expected noise and include a label-quality validation step.\n\n4. **Strengthen the method contribution**: The current method is essentially 'SFT with different labels,' which is too thin. Consider adding: (a) a hybrid label strategy (data-flow + BM25 + LLM confidence ensemble), (b) data-flow-aware loss weighting (higher weight for labels derived from longer def-use chains), or (c) a two-stage approach (coarse data-flow-based file selection → fine-grained function ranking). This would make it a genuine method paper rather than an ablation study.\n\n5. **Add Squeez (arXiv:2604.04979), LongCodeZip (ASE 2025), SWE Context Bench (arXiv:2602.08316), and LLMxCPG (USENIX Security 2025) to the related work**: These are direct competitors or related work that reviewers will expect to see.\n\n6. **Correct the SWE-Pruner framing**: State clearly that SWE-Pruner reduces 70.6% → 70.2% (a 0.4pp degradation with 23% token savings), not that it 'achieves 70.2%.' This honest framing actually strengthens your argument about the need for better labels if you frame it correctly.\n\n7. **Timeline reality check**: With 15 days remaining, focus on the most achievable version: use an existing Python analysis library (Jedi/Pyright) rather than building tree-sitter def-use from scratch, restrict to a subset of SWE-smith instances (10K instead of 50K), and parallelize writing with experiments.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"CRITICAL VENUE MISMATCH: User explicitly requires EMNLP 2026 (ARR deadline May 25, 2026, 15 days away), but the idea targets AAAI 2027 / ICLR 2027 / ICSE 2027. Must retarget to EMNLP 2026 or provide a justified alternative within the user's timeline.\", \"CRITICAL TIMELINE MISMATCH: Manual mode estimates 2-3 months, HIL 4-6 weeks, auto 2-3 weeks. The user's hard constraint is ≤16 days. Even auto mode exceeds this. The resource estimates must be reworked to fit a 15-day sprint to ARR submission.\", \"UNBUDGETED API COST: SWE-bench Pro end-to-end evaluation requires running 1865 instances through Claude Sonnet 4.6 at ~$3/M input + $15/M output tokens. With ~0.7M input + ~0.1M output per instance (from SWE-Pruner numbers), this costs ~$5,600-$11,200 in API fees — entirely missing from the resource estimate. Either budget this or use a cheaper evaluation model (e.g., Qwen3.6-27B only).\", \"MISSING REFERENCE: LocAgent (ACL 2025, arXiv:2503.09089) — graph-guided LLM agents for code localization using directed heterogeneous graphs (imports, invocations, inheritance). Achieves 92.7% file-level accuracy on SWE-bench Lite with fine-tuned Qwen2.5-32B. This is the closest prior work combining graph structure with neural models for code localization. Must differentiate: LocAgent uses structural edges (import/call/inheritance) but NOT data-flow edges; StructFuse's def-use chains are complementary.\", \"MISSING REFERENCE: SweRank (arXiv:2505.07849, May 2025) — SOTA retrieve-and-rerank framework for software issue localization, outperforming both prior ranking models and costly agent-based systems. Should be included as a baseline for the retrieval component comparison.\", \"MISSING REFERENCE: 'On the Effectiveness of Context Compression for Repository-Level Tasks' (arXiv:2604.13725, Apr 2026) — empirical study showing continuous latent vector methods surpass full-context by up to 28.3% at 4x compression. This challenges the assumption that text-level context selection is the best compression paradigm.\", \"EVALUATION GAP: User's requirements include CrossCodeEval and RepoBench as evaluation benchmarks, which are directly relevant for cross-file context retrieval. The current evaluation plan only covers SWE-bench variants. At minimum, RepoBench file-level retrieval evaluation should be added.\", \"METHOD CONTRIBUTION PRECISION: 'Signal-aware fusion training with data-flow-guided loss weighting' sounds novel but is technically standard: (1) extract features from multiple sources, (2) concatenate as model input, (3) apply weighted cross-entropy loss based on feature confidence. The paper should be transparent that the contribution is in the specific signal combination and empirical validation, not in the training methodology itself.\"]\nFeedback: Round 3 has significantly improved the idea — the SWE-Pruner framing is now honest, the tool choices (CodeQL/Scalpel/Beniget) are concrete, and the label-quality validation step addresses Python dynamic features. However, critical structural issues remain:\n\n1. **Retarget to EMNLP 2026**: The user requires EMNLP 2026 (ARR May 25). 'NLP and Code Models' is an explicit EMNLP 2026 topic area. Retarget the venue and rework the timeline to fit a 15-day sprint. This is aggressive but possible: Days 1-3: CodeQL pipeline on 5K SWE-smith instances (not 10K — reduce scope), Days 4-5: SFT training (3B model on 5K examples with LoRA takes ~2-4 hours per run), Days 6-10: SWE-bench Lite evaluation (300 instances, manageable) + SWE-bench Pro subset (sample 500 of 1865 instances), Days 10-15: Writing. Skip full SWE-bench Pro (too expensive in 15 days).\n\n2. **Budget API costs explicitly**: End-to-end repair evaluation requires LLM API calls. Either: (a) budget ~$3,000-6,000 for API costs, (b) use only open-weight models (Qwen3.6-27B) for evaluation to avoid API costs, or (c) evaluate on SWE-bench Lite (300 instances, ~$900-1,800) instead of full Pro.\n\n3. **Add LocAgent and SweRank to related work and baselines**: LocAgent (ACL 2025) is the most direct competitor — it also uses graph structure for code localization. Your differentiation: LocAgent uses import/call/inheritance edges at file/class/function granularity, while StructFuse adds intra-procedural data-flow (def-use) edges, which capture finer-grained variable-level dependencies. SweRank is SOTA for text-based retrieval and should be a baseline.\n\n4. **Scope down for feasibility**: With 15 days, reduce: 10K→5K training instances, full SWE-bench Pro→500-instance sample, skip CodeContests/HumanEval (irrelevant for context selection), keep RepoBench for cross-file retrieval evaluation.\n\n5. **Be precise about method contribution**: Don't overclaim 'signal-aware training' as a novel training methodology. The contribution is: (a) demonstrating that data-flow signals provide useful supervision without LLM teachers, (b) showing fusion of structural + lexical signals outperforms either alone, (c) the specific pipeline (CodeQL→features→fusion model) is practical and reproducible. This is a strong empirical contribution with practical value — frame it that way.\n\n6. **Compute budget**: The user's constraint is ≤200 H100-hours. Your manual estimate of ~250h A100 ≈ ~125-165h H100 fits. But you must account for the evaluation compute separately and ensure the total stays under 200h H100.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T18:40:10.194Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T18:40:10.194Z",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-10T18:40:10.225Z_

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

## Idea under review (round 4/10)
{
  "title": "StructFuse: Fusing Data-Flow and Lexical Signals for Repository-Level Code Repair Context Selection",
  "core_problem": "Repository-level bug repair requires selecting relevant context from large codebases. Existing neural context selectors (SWE-Pruner, Squeez) rely on expensive LLM-generated labels (~$50-200 per labeling run), are coupled to specific teacher models, and lack structural grounding. Retrieve-and-rerank methods like SweRank achieve strong text-based localization but miss structural dependencies. Graph-guided agents like LocAgent capture import/call/inheritance edges but omit fine-grained data-flow (def-use) edges that trace variable-level dependencies across functions. On SWE-bench Pro (where top systems score 42-59% and context selection accounts for 4-10pp swings), context quality remains a dominant differentiator. Can we build a context selector that fuses data-flow structural signals with lexical retrieval in a lightweight distilled model—one that requires no LLM teacher, is model-independent, and provides interpretable, structurally-grounded selections?",
  "opportunity": "SWE-Pruner (arXiv:2601.16746) demonstrated a 0.6B neural skimmer can reduce tokens 23-54% with <1pp degradation on SWE-bench Verified, but its supervision comes entirely from Qwen3-Coder-30B inference. LocAgent (ACL 2025) showed graph-guided localization achieves 92.7% file-level accuracy on SWE-bench Lite, but uses only import/invocation/inheritance edges—not data-flow. SweRank (arXiv:2505.07849) achieves SOTA retrieve-and-rerank localization but is purely text-based. ARISE (arXiv:2605.03117) confirmed data-flow slicing yields 17pp localization gains on SWE-bench Lite but keeps analysis as runtime tool calls, not distilled knowledge. Sliceformer (ACL 2026) validated that data-flow knowledge transfers to neural models with 22% ExactMatch gains. The opportunity: no existing work distills data-flow structural signals into a lightweight, fast model for repair context selection. LocAgent's graph lacks def-use edges; ARISE's data-flow is runtime-only; SweRank ignores structure entirely. Fusing data-flow features with lexical retrieval in a trained model fills this gap—cheap to supervise (program analysis, not LLM inference), model-independent, and fast at inference.",
  "landscape": "**Neural context selectors**: SWE-Pruner trains a 0.6B skimmer on 61K LLM-labeled samples, achieving <1pp degradation on SWE-bench Verified (70.6%→70.2%)—but relies on expensive Qwen3-Coder-30B labels and the Verified benchmark is known contaminated (OpenAI, Feb 2026). Squeez (arXiv:2604.04979) fine-tunes Qwen 3.5 2B for task-conditioned tool-output pruning (0.86 recall, 92% token removal) but targets tool outputs, not repository context. LongCodeZip (ASE 2025) achieves 5.6x compression via perplexity-based ranking, training-free but code-agnostic. **Retrieve-and-rerank approaches**: SweRank (arXiv:2505.07849) achieves SOTA issue localization via SweRankEmbed (bi-encoder retriever) + SweRankLLM (listwise LLM reranker), outperforming both prior models and agent-based systems. SweRank+ (arXiv:2512.20482) extends to multilingual multi-turn ranking with 155K training instances. Both are purely text-based with no structural signals. **Graph-guided approaches**: LocAgent (ACL 2025, arXiv:2503.09089) parses codebases into directed heterogeneous graphs with import/invocation/inheritance edges, achieving 92.7% file-level accuracy with fine-tuned Qwen2.5-32B—but omits data-flow (def-use) edges and requires a 32B model at inference. KGCompass (arXiv:2503.21710) constructs repository knowledge graphs (58.3% repair) but with heavy construction overhead. **Data-flow-specific approaches**: ARISE (arXiv:2605.03117) augments SWE-agent with statement-level def-use edges, gaining 17pp Function Recall@1 and 4.7pp Pass@1—but keeps analysis as runtime tool calls, adding latency at inference. LLMxCPG (USENIX Security 2025) uses Code Property Graphs for vulnerability detection (67-91% code reduction, 15-40% F1 gain) but targets security, not repair context. Sliceformer (ACL 2026) distills DFG knowledge into CodeT5+ for slicing tasks, validating structural knowledge transfer but not addressing repair. **Compression paradigms**: A recent empirical study (arXiv:2604.13725) shows continuous latent vector compression surpasses full-context by up to 28.3% BLEU at 4x compression—demonstrating that intelligent filtering outperforms naive truncation, though text-level selection remains complementary and more interpretable. **Benchmarks**: SWE-bench Pro (Scale AI, 1865 tasks) is the recommended hard benchmark; SWE-bench Lite (300 instances) remains widely used; RepoBench-R (ICLR 2024) directly evaluates cross-file context retrieval; SWE-ContextBench (arXiv:2602.08316) provides 1100+376 tasks for context evaluation. **Gap**: No existing work distills data-flow (def-use) signals into a lightweight model for repair context selection. LocAgent uses structural edges but not def-use; SweRank is text-only; ARISE uses def-use but only at runtime. The fusion of data-flow features with lexical retrieval in a fast, distilled model is unexplored.",
  "approach": "We propose StructFuse, a multi-signal context selector that fuses data-flow structural features with lexical retrieval signals in a lightweight distilled model for repository-level code repair context selection.\n\n**Stage 1: Multi-Signal Feature Extraction (Days 1-3).** For 5K SWE-smith training instances across ~80-100 of the 128 available repositories, we extract three signal types: (a) *Data-flow features*: Using CodeQL for inter-procedural def-use analysis and call-graph construction on the ~128 shared repositories (each needing one database build), augmented by Beniget for intra-file def-use chains where CodeQL databases fail (~20-30% of repos). For each candidate file/function, we compute: graph distance to buggy location, number of data-flow paths, dependency type (def-use, call-graph, import). (b) *Lexical features*: BM25 similarity between issue description and candidate code, plus SweRankEmbed scores as a strong retrieval baseline. (c) *Structural metadata*: File co-change frequency from git history, import distance, directory distance. We explicitly acknowledge Python's dynamic features (eval, metaclasses, monkey-patching) limit static analysis coverage and quantify this via a validation step on 500 instances before full-scale extraction.\n\n**Stage 2: Fusion Model Training (Days 4-5).** We train a Qwen2.5-Coder-3B model via LoRA SFT on multi-signal fusion. The model receives structured multi-signal representations (data-flow graph features, BM25/SweRankEmbed scores, structural metadata) as input alongside the code context and learns to predict file/function-level relevance. We apply data-flow-guided loss weighting: candidates with strong structural connections receive higher loss weight, encoding the inductive bias that structurally-connected code is more reliably relevant than lexically-similar code. We are transparent that this training methodology—multi-source features as input with confidence-weighted loss—is technically standard; the contribution lies in demonstrating that data-flow signals provide effective supervision without LLM teachers and that the specific signal combination yields empirical gains. Training takes ~2-4 hours per run on a single H100; we run 5 ablation configurations (data-flow only, lexical only, full fusion, with/without loss weighting, CodeQL inter-procedural vs. Beniget intra-file only).\n\n**Stage 3: Evaluation (Days 6-10).** The distilled selector plugs into SWE-agent as a drop-in context retrieval component. We evaluate on: (a) SWE-bench Lite (300 instances, full), (b) SWE-bench Pro public split (500-instance stratified sample of 731 public instances), (c) RepoBench-R (cross-file retrieval evaluation, no LLM needed). Metrics: localization recall@k (file and function level), end-to-end Pass@1 repair rate, token efficiency. End-to-end evaluation uses Qwen3.6-27B exclusively (open-weight, no API costs). We compare against: (i) SweRank/SweRankEmbed (SOTA text-based retrieval), (ii) SWE-Pruner (LLM-labeled selector), (iii) BM25 baseline, (iv) LocAgent's graph-guided approach (import/call/inheritance edges, no def-use), (v) no-pruning full-context. Key ablations isolate each signal type's contribution.\n\n**Stage 4: Writing (Days 10-15).** The central hypothesis: on hard benchmarks, the fusion of data-flow + lexical signals outperforms either alone—and achieves comparable or better performance than LLM-labeled selectors at zero labeling cost. The paper frames StructFuse as an empirical and systems contribution: (a) first demonstration that program-analysis-derived data-flow features provide effective, free supervision for context selection, (b) empirical evidence that def-use edges complement the import/call/inheritance edges used by LocAgent and the text signals used by SweRank, (c) a practical, reproducible pipeline (CodeQL→features→3B fusion model) that is fast at inference and model-independent.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180h H100 (CodeQL database creation for ~128 repos: ~10h CPU-parallel + 5h GPU; feature extraction: ~15h; SFT training 5 ablation runs: ~20h; SWE-bench evaluation 800 instances with Qwen3.6-27B: ~120h; RepoBench-R evaluation: ~10h)",
      "gpu_utilization": "~70-80% utilization during evaluation phase (Qwen3.6-27B inference is GPU-bound); ~30-40% during CodeQL/feature extraction",
      "timeline": "15 days (Days 1-3: CodeQL pipeline + feature extraction; Days 4-5: SFT training + ablations; Days 6-10: evaluation; Days 10-15: writing)",
      "team": "1-2 researchers (one with CodeQL/program analysis, one with LLM fine-tuning; can be same person)",
      "estimated_gpu_cost": "$400-600 (180h H100 at spot ~$2.50/hr; no LLM API costs—all evaluation uses open-weight Qwen3.6-27B)",
      "claude_api_cost": "$0 for evaluation (Qwen3.6-27B only); ~$50-100 for writing assistance",
      "risk_note": "CodeQL database creation may fail for 20-30% of Python repos with complex dependencies; Beniget fallback covers intra-file analysis. SWE-smith repos are well-maintained open-source projects with higher-than-average build success rates."
    },
    "human_in_loop": {
      "gpu_hours": "~150h H100 (same pipeline, agent manages CodeQL builds and queues training runs; human reviews label quality at day 2 and evaluation configs at day 5)",
      "gpu_utilization": "~75-85% utilization; agent parallelizes independent experiments",
      "timeline": "12-14 days",
      "team": "1 researcher, ~45min/day check-in for label quality review and experiment approval",
      "claude_api_cost": "$80-150 (800-1500 turns for pipeline code generation and debugging)",
      "estimated_gpu_cost": "$350-500 (150h H100 at spot ~$2.50/hr)",
      "risk_note": "Tight timeline requires pre-validated CodeQL setup; recommend testing on 10 repos in first 4 hours before scaling"
    },
    "auto_research": {
      "gpu_hours": "~200h H100 (full ablation suite, hyperparameter sweep over loss weights, multi-benchmark evaluation including RepoBench-R)",
      "gpu_utilization": "~85-90% utilization; agent continuously launches experiments, parallelizes independent ablations",
      "timeline": "10-12 days with 2-4 H100 GPUs available concurrently",
      "team": "0 (initial setup: CodeQL CLI installation, SWE-smith repo cloning, SWE-bench evaluation harness)",
      "claude_api_cost": "$200-400 (2000-4000 turns for iterative pipeline development, CodeQL query debugging, experiment scheduling)",
      "estimated_gpu_cost": "$500-700 (200h H100 at spot ~$2.50/hr to on-demand ~$3.50/hr)",
      "speed_bottleneck": "SWE-bench evaluation (~9min/instance × 800 instances on Qwen3.6-27B ≈ 120 H100-hours; parallelizable across GPUs)",
      "risk_note": "Agent should validate CodeQL coverage on first 10 repos and report def-use coverage before scaling. If coverage < 50%, pivot to Beniget-only for broader but shallower analysis."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline: May 25, 2026; conference: Fall 2026; topic area: 'NLP and Code Models')"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents (arXiv:2601.16746, Jan 2026) — 0.6B skimmer, LLM-labeled, <1pp degradation on SWE-bench Verified",
    "LocAgent: Graph-Guided LLM Agents for Code Localization (ACL 2025, arXiv:2503.09089) — 92.7% file-level accuracy on SWE-bench Lite using import/invocation/inheritance edges with fine-tuned Qwen2.5-32B; no def-use edges",
    "SweRank: Software Issue Localization with Code Ranking (arXiv:2505.07849, May 2025) — SOTA retrieve-and-rerank, outperforms agent-based systems; text-only, no structural signals",
    "SweRank+: Multilingual, Multi-Turn Code Ranking (arXiv:2512.20482, Dec 2025) — extends SweRank to multilingual multi-turn with 155K training instances",
    "Sliceformer: Static Program Slicing Using Language Models With Dataflow-Aware Pretraining (ACL 2026, arXiv:2604.26961) — validates data-flow knowledge transfer to neural models",
    "ARISE: Repository-level Graph Representation for Agentic Fault Localization and Repair (arXiv:2605.03117, May 2026) — def-use edges as runtime tool calls, +17pp Function Recall@1",
    "LLMxCPG: Context-Aware Vulnerability Detection Through CPG-Guided LLMs (USENIX Security 2025) — CPG-guided context extraction, 67-91% code reduction",
    "Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents (arXiv:2604.04979, Apr 2026) — 0.86 recall, 92% token removal on tool outputs",
    "On the Effectiveness of Context Compression for Repository-Level Tasks (arXiv:2604.13725, Apr 2026) — continuous latent vectors surpass full-context by 28.3% at 4x compression",
    "LongCodeZip: Compress Long Context for Code Language Models (ASE 2025, arXiv:2510.00446) — 5.6x training-free compression",
    "RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems (ICLR 2024, arXiv:2306.03091) — cross-file retrieval evaluation benchmark",
    "SWE-ContextBench: A Benchmark for Context Learning in Coding (arXiv:2602.08316, Feb 2026) — 1100+376 context evaluation tasks",
    "On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv:2604.05481, Apr 2026) — file-level is dominant factor",
    "Why SWE-bench Verified No Longer Measures Frontier Coding Capabilities (OpenAI, Feb 2026) — contamination analysis",
    "SWE-bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (Scale AI, arXiv:2509.16941, 2025)",
    "LLMDFA: Analyzing Dataflow in Code with Large Language Models (NeurIPS 2024)",
    "SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025 D&B Spotlight)",
    "SWE-bench: Can Language Models Resolve Real-World GitHub Issues? (ICLR 2024)"
  ],
  "description": "We propose StructFuse, a multi-signal context selector for repository-level code repair that fuses data-flow (def-use) structural features with lexical retrieval signals in a lightweight 3B distilled model. Unlike SWE-Pruner (expensive LLM-labeled supervision), SweRank (text-only retrieval), and LocAgent (import/call/inheritance edges but no def-use), StructFuse extracts inter-procedural def-use chains via CodeQL and fuses them with BM25/SweRankEmbed retrieval scores in a Qwen2.5-Coder-3B model trained with LoRA SFT. The contribution is empirical and practical, not methodological: (1) we demonstrate that program-analysis-derived data-flow features provide effective supervision for context selection without any LLM teacher—zero labeling cost vs. ~$50-200 for LLM-supervised methods; (2) we show that def-use edges complement the coarser structural edges (import/call/inheritance) used by LocAgent and the text signals used by SweRank, with fusion outperforming either signal type alone; (3) the resulting pipeline (CodeQL→features→3B fusion model) is fast at inference, model-independent, and provides interpretable selections with traceable data-flow paths to the bug. We evaluate on SWE-bench Lite (300 instances), a 500-instance SWE-bench Pro subset, and RepoBench-R (cross-file retrieval), using only open-weight Qwen3.6-27B for end-to-end repair evaluation (no API costs). We target EMNLP 2026 under the 'NLP and Code Models' topic area, with a 15-day implementation sprint fitting within 200 H100-hours.",
  "project_name": "structfuse_context",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL MISSING REFERENCE: Sliceformer (arXiv:2604.26961, ACL 2026, April 2026) distills data-flow knowledge into neural models using tree-sitter DFGs—conceptually very close. Must acknowledge and differentiate.", "CRITICAL MISSING REFERENCE: SWE-Pruner (arXiv:2601.16746, Jan 2026) uses a 0.6B neural skimmer for line-level context pruning in coding agents—same architecture concept, different training signal.", "16-day timeline is not credible: ARISE code is unreleased (confirmed), Tree Climber only supports intra-procedural analysis, and OPCD requires iterative generate-then-train loops that multiply wall-clock time.", "27B model contradicts the 'fast inference' framing: Qwen3.6-27B requires 1-3 seconds per forward pass. The '10-50x lower latency vs ARISE' claim only holds if comparing against multi-round tool-call overhead, not against the actual static analysis (tree-sitter is fast).", "Weak baseline concern: ARISE's 22.0% on SWE-bench Lite is far below SOTA (62.7%). If the distilled selector is only evaluated as a replacement in ARISE-level systems, absolute gains will appear modest.", "OPCD complexity vs. timeline: On-policy distillation requires multiple rounds of student generation + training. Standard SFT with data-flow labels would be far simpler and more feasible within constraints.", "Inter-procedural gap: The proposal claims repo-level context selection but Tree Climber only supports intra-procedural def-use chains. Scaling to cross-function/cross-file data-flow for SWE-bench instances is a significant unsolved engineering challenge."]
Feedback: This idea has a valid core insight (distilling static analysis signals into a neural context selector is more principled than LLM-generated relevance labels), but needs significant revision to be feasible within constraints and differentiated from concurrent work:

1. **Acknowledge and differentiate from Sliceformer (ACL 2026)**: This paper already distills data-flow into neural models via pretraining objectives on DFGs. Your differentiation is: (a) application to repair context selection rather than slicing, (b) on-policy distillation rather than pretraining objectives, (c) end-to-end evaluation on repair. Make this explicit.

2. **Acknowledge SWE-Pruner**: Position your work as replacing SWE-Pruner's LLM-teacher signal with ground-truth data-flow signals, showing that structural program analysis provides better training signal than LLM-generated relevance.

3. **Simplify the method for 16-day feasibility**: Drop OPCD. Use standard SFT with binary labels (data-flow-relevant vs. not) as supervision. This cuts training to a single pass and dramatically reduces complexity. Frame OPCD as future work.

4. **Use a smaller model**: A 7B model (e.g., Qwen3-8B or Qwen2.5-Coder-7B) would genuinely achieve fast inference AND fit the compute budget better. The 'distilled fast selector' narrative is more convincing with a small model.

5. **Scope down data generation**: Instead of full repo-level inter-procedural analysis (which Tree Climber can't do), use intra-procedural def-use chains + simple call-graph edges (tree-sitter can extract these). Be honest about this limitation.

6. **Strengthen evaluation**: Evaluate as a plug-in context selector for a STRONG agent (not just ARISE-level), e.g., plug into SWE-agent with Qwen3.6-27B as the repair model. This would show the selector helps even with capable models.

7. **Realistic timeline**: With simplified SFT + 7B model + scoped data pipeline, 16 days becomes plausible: ~5 days data pipeline, ~3 days training + iteration, ~5 days evaluation, ~3 days writing.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL: SWE-Pruner 70.2% framing is misleading. Verified via full paper: the baseline WITHOUT SWE-Pruner achieves 70.6% with Claude Sonnet 4.5. SWE-Pruner DEGRADES performance by 0.4pp (to 70.2%) while reducing tokens 23%. The idea frames 70.2% as SWE-Pruner's achievement, but LLM labels already produce near-perfect context selection. This means the improvement ceiling from better labels is extremely narrow — at best recovering 0.4pp.", "CRITICAL: Narrow improvement ceiling undermines motivation. If LLM-generated labels already enable <1% degradation from the unpruned baseline, the core argument ('LLM labels are noisy and can be improved with structural signals') is empirically weak. The value proposition must be reframed: data-flow labels are (a) cheaper (no LLM teacher needed), (b) model-independent, (c) more interpretable — NOT necessarily higher quality.", "CRITICAL: SWE-bench Verified is now considered a compromised benchmark. OpenAI stopped reporting Verified scores in Feb 2026 after finding models reproduce verbatim gold patches. Evaluating only on Verified severely weakens the paper. Must add SWE-bench Pro evaluation (top SOTA: ~46-77% depending on scaffolding, much harder and uncontaminated).", "MISSING REFERENCE: Squeez (arXiv:2604.04979, April 2026) — another task-conditioned context pruning approach for coding agents using fine-tuned Qwen 3.5 2B with LoRA, achieving 0.86 recall and 92% token removal. Must be discussed and compared as a concurrent context pruning method.", "MISSING REFERENCE: LongCodeZip (ASE 2025, arXiv:2510.00446) — code compression using conditional perplexity ranking + knapsack pruning. Achieves 5.6x compression. A relevant baseline for context compression.", "MISSING REFERENCE: SWE Context Bench (arXiv:2602.08316, Feb 2026) — a benchmark specifically for evaluating context learning/selection in coding tasks. Should be used for evaluation.", "Tree-sitter def-use extraction for Python is underspecified. Tree-sitter is a parser, not a static analysis tool. Tree Climber only supports C. The proposal says 'we run intra-procedural def-use chain analysis via tree-sitter' without specifying what existing tool or library will be used, or acknowledging that this must be built from scratch. For Python's dynamic typing, metaclasses, monkey patching, and eval, the resulting labels will be very noisy. The proposal should either: (a) specify using a proper Python type-aware tool like Pyright/Jedi for more complete analysis, (b) quantify expected label noise and demonstrate noisy labels still provide useful signal, or (c) restrict scope to statically-typed Python patterns.", "Method contribution is too thin for EMNLP Main. The actual method is: (1) extract def-use chains, (2) use as binary labels, (3) train standard SFT. Steps 2-3 are trivially standard. The entire contribution rests on the labeling strategy, making this an empirical study rather than a method paper. Consider reframing as an empirical contribution or adding a methodological innovation (e.g., hybrid labels combining data-flow and LLM signals, curriculum over label sources, or data-flow-aware loss weighting).", "MISSING REFERENCE: LLMxCPG (USENIX Security 2025) uses Code Property Graphs (including data-flow edges) to guide an LLM in extracting vulnerability-relevant code slices. Very similar paradigm (program analysis guides neural context extraction), though for vulnerability detection. Should be discussed as related work from an adjacent domain."]
Feedback: The revised idea has addressed most Round 1 issues well (Sliceformer/SWE-Pruner positioning, dropping OPCD, 7B model, scoped data generation). However, critical new issues have emerged from deep verification:

1. **Reframe the motivation around cost and independence, not quality**: The SWE-Pruner data shows LLM labels already produce near-optimal context selection (<1% degradation). Your story should NOT be 'data-flow labels are higher quality than LLM labels' — it should be: 'data-flow labels are (a) 100x cheaper to produce (no expensive LLM teacher inference), (b) model-independent (no coupling to a specific teacher like Qwen3-Coder-30B), (c) structurally grounded and interpretable, and (d) potentially complementary to LLM labels.' Consider a hybrid approach: data-flow labels + LLM labels combined could outperform either alone.

2. **Add SWE-bench Pro to evaluation**: SWE-bench Verified is compromised. Add SWE-bench Pro (and/or SWE-bench Live) to the evaluation plan. This also addresses a harder benchmark where context selection may matter more (the unpruned baseline won't be 70%+ on Pro).

3. **Specify the def-use extraction tool concretely**: Don't just say 'tree-sitter def-use analysis' — tree-sitter is a parser. You need to build a custom analysis pass on top of tree-sitter ASTs. Consider: (a) using scope_resolution + assignment patterns from tree-sitter to build intra-function def-use chains, (b) using call_expression nodes for one-hop call-graph edges. Alternatively, consider using Jedi (a Python static analysis library with type inference) for better def-use coverage. Quantify the expected noise and include a label-quality validation step.

4. **Strengthen the method contribution**: The current method is essentially 'SFT with different labels,' which is too thin. Consider adding: (a) a hybrid label strategy (data-flow + BM25 + LLM confidence ensemble), (b) data-flow-aware loss weighting (higher weight for labels derived from longer def-use chains), or (c) a two-stage approach (coarse data-flow-based file selection → fine-grained function ranking). This would make it a genuine method paper rather than an ablation study.

5. **Add Squeez (arXiv:2604.04979), LongCodeZip (ASE 2025), SWE Context Bench (arXiv:2602.08316), and LLMxCPG (USENIX Security 2025) to the related work**: These are direct competitors or related work that reviewers will expect to see.

6. **Correct the SWE-Pruner framing**: State clearly that SWE-Pruner reduces 70.6% → 70.2% (a 0.4pp degradation with 23% token savings), not that it 'achieves 70.2%.' This honest framing actually strengthens your argument about the need for better labels if you frame it correctly.

7. **Timeline reality check**: With 15 days remaining, focus on the most achievable version: use an existing Python analysis library (Jedi/Pyright) rather than building tree-sitter def-use from scratch, restrict to a subset of SWE-smith instances (10K instead of 50K), and parallelize writing with experiments.

### Round 3 review
Verdict: revise
Issues: ["CRITICAL VENUE MISMATCH: User explicitly requires EMNLP 2026 (ARR deadline May 25, 2026, 15 days away), but the idea targets AAAI 2027 / ICLR 2027 / ICSE 2027. Must retarget to EMNLP 2026 or provide a justified alternative within the user's timeline.", "CRITICAL TIMELINE MISMATCH: Manual mode estimates 2-3 months, HIL 4-6 weeks, auto 2-3 weeks. The user's hard constraint is ≤16 days. Even auto mode exceeds this. The resource estimates must be reworked to fit a 15-day sprint to ARR submission.", "UNBUDGETED API COST: SWE-bench Pro end-to-end evaluation requires running 1865 instances through Claude Sonnet 4.6 at ~$3/M input + $15/M output tokens. With ~0.7M input + ~0.1M output per instance (from SWE-Pruner numbers), this costs ~$5,600-$11,200 in API fees — entirely missing from the resource estimate. Either budget this or use a cheaper evaluation model (e.g., Qwen3.6-27B only).", "MISSING REFERENCE: LocAgent (ACL 2025, arXiv:2503.09089) — graph-guided LLM agents for code localization using directed heterogeneous graphs (imports, invocations, inheritance). Achieves 92.7% file-level accuracy on SWE-bench Lite with fine-tuned Qwen2.5-32B. This is the closest prior work combining graph structure with neural models for code localization. Must differentiate: LocAgent uses structural edges (import/call/inheritance) but NOT data-flow edges; StructFuse's def-use chains are complementary.", "MISSING REFERENCE: SweRank (arXiv:2505.07849, May 2025) — SOTA retrieve-and-rerank framework for software issue localization, outperforming both prior ranking models and costly agent-based systems. Should be included as a baseline for the retrieval component comparison.", "MISSING REFERENCE: 'On the Effectiveness of Context Compression for Repository-Level Tasks' (arXiv:2604.13725, Apr 2026) — empirical study showing continuous latent vector methods surpass full-context by up to 28.3% at 4x compression. This challenges the assumption that text-level context selection is the best compression paradigm.", "EVALUATION GAP: User's requirements include CrossCodeEval and RepoBench as evaluation benchmarks, which are directly relevant for cross-file context retrieval. The current evaluation plan only covers SWE-bench variants. At minimum, RepoBench file-level retrieval evaluation should be added.", "METHOD CONTRIBUTION PRECISION: 'Signal-aware fusion training with data-flow-guided loss weighting' sounds novel but is technically standard: (1) extract features from multiple sources, (2) concatenate as model input, (3) apply weighted cross-entropy loss based on feature confidence. The paper should be transparent that the contribution is in the specific signal combination and empirical validation, not in the training methodology itself."]
Feedback: Round 3 has significantly improved the idea — the SWE-Pruner framing is now honest, the tool choices (CodeQL/Scalpel/Beniget) are concrete, and the label-quality validation step addresses Python dynamic features. However, critical structural issues remain:

1. **Retarget to EMNLP 2026**: The user requires EMNLP 2026 (ARR May 25). 'NLP and Code Models' is an explicit EMNLP 2026 topic area. Retarget the venue and rework the timeline to fit a 15-day sprint. This is aggressive but possible: Days 1-3: CodeQL pipeline on 5K SWE-smith instances (not 10K — reduce scope), Days 4-5: SFT training (3B model on 5K examples with LoRA takes ~2-4 hours per run), Days 6-10: SWE-bench Lite evaluation (300 instances, manageable) + SWE-bench Pro subset (sample 500 of 1865 instances), Days 10-15: Writing. Skip full SWE-bench Pro (too expensive in 15 days).

2. **Budget API costs explicitly**: End-to-end repair evaluation requires LLM API calls. Either: (a) budget ~$3,000-6,000 for API costs, (b) use only open-weight models (Qwen3.6-27B) for evaluation to avoid API costs, or (c) evaluate on SWE-bench Lite (300 instances, ~$900-1,800) instead of full Pro.

3. **Add LocAgent and SweRank to related work and baselines**: LocAgent (ACL 2025) is the most direct competitor — it also uses graph structure for code localization. Your differentiation: LocAgent uses import/call/inheritance edges at file/class/function granularity, while StructFuse adds intra-procedural data-flow (def-use) edges, which capture finer-grained variable-level dependencies. SweRank is SOTA for text-based retrieval and should be a baseline.

4. **Scope down for feasibility**: With 15 days, reduce: 10K→5K training instances, full SWE-bench Pro→500-instance sample, skip CodeContests/HumanEval (irrelevant for context selection), keep RepoBench for cross-file retrieval evaluation.

5. **Be precise about method contribution**: Don't overclaim 'signal-aware training' as a novel training methodology. The contribution is: (a) demonstrating that data-flow signals provide useful supervision without LLM teachers, (b) showing fusion of structural + lexical signals outperforms either alone, (c) the specific pipeline (CodeQL→features→fusion model) is practical and reproducible. This is a strong empirical contribution with practical value — frame it that way.

6. **Compute budget**: The user's constraint is ≤200 H100-hours. Your manual estimate of ~250h A100 ≈ ~125-165h H100 fits. But you must account for the evaluation compute separately and ensure the total stays under 200h H100.


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
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "type": "user",
  "uuid": "753c3e95-deae-4eea-b793-b296e91e2ea4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T18:40:10.223Z_

```json
{
  "parentUuid": "753c3e95-deae-4eea-b793-b296e91e2ea4",
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
  "uuid": "12449d45-41ae-457e-bcd9-9110359df2f7",
  "timestamp": "2026-05-10T18:40:10.223Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T18:40:10.223Z_

```json
{
  "parentUuid": "12449d45-41ae-457e-bcd9-9110359df2f7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d234add5-2e2e-456e-9be7-a1858b6b4075",
  "timestamp": "2026-05-10T18:40:10.223Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
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
  "leafUuid": "d234add5-2e2e-456e-9be7-a1858b6b4075",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify StructFuse feasibility and competing work for EMNLP 2026 submission",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Assistant

_source line 8 · 2026-05-10T18:40:17.816Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this Round 4 submission of StructFuse. I need to independently verify claims, check for missing references, assess feasibility, and determine if the previous review issues have been adequately addressed.

Let me start by checking the key claims and searching for competing/missing work.

Key things to verify:
1. Has the idea addressed Round 3's critical issues (venue targeting, timeline, API costs)?
2. Are the cited references real and accurately described?
3. Are there missing competing works?
4. Is the 15-day timeline realistic?
5. Is the method contribution sufficient for EMNLP?


Now I'm looking up the references they cite and checking what other related work exists in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d234add5-2e2e-456e-9be7-a1858b6b4075",
  "isSidechain": false,
  "requestId": "req_011CauNpdk53vtehhRFvbK8m",
  "type": "assistant",
  "uuid": "ee80ee71-15dd-4bcb-911b-644a4ec84780",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183WJfQj77jkBPRLR41mTUB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18222,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1493,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 18222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18222
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

_source line 9 · 2026-05-10T18:40:18.079Z_

I'll conduct an independent adversarial review of this Round 4 submission. Let me verify key claims, check for missing references, and assess feasibility.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee80ee71-15dd-4bcb-911b-644a4ec84780",
  "isSidechain": false,
  "requestId": "req_011CauNpdk53vtehhRFvbK8m",
  "type": "assistant",
  "uuid": "ea616764-2cc4-442e-82cd-77157465d062",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183WJfQj77jkBPRLR41mTUB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18222,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1493,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 18222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18222
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

_source line 10 · 2026-05-10T18:40:23.535Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01U1PdcUCh9BN6dAHJB7XNrq`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify ARISE paper claims",
  "prompt": "Search the web for the paper \"ARISE: Repository-level Graph Representation for Agentic Fault Localization and Repair\" (arXiv:2605.03117). I need to verify:\n1. Does this paper actually exist on arXiv?\n2. Does it use def-use edges as runtime tool calls?\n3. Does it report +17pp Function Recall@1 on SWE-bench Lite?\n4. Does it report 4.7pp Pass@1 improvement?\n\nUse WebSearch to find this paper and WebFetch to read its abstract/details if possible. Report exactly what you find — do not fabricate details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea616764-2cc4-442e-82cd-77157465d062",
  "isSidechain": false,
  "requestId": "req_011CauNpdk53vtehhRFvbK8m",
  "type": "assistant",
  "uuid": "80901a79-db2d-4341-93fb-e19c20d02539",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183WJfQj77jkBPRLR41mTUB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18222,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1493,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 18222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18222
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

_source line 11 · 2026-05-10T18:40:26.742Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NXXAiwTdGvRYpmNyGoLR9X`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Sliceformer paper",
  "prompt": "Search the web for the paper \"Sliceformer: Static Program Slicing Using Language Models With Dataflow-Aware Pretraining\" (arXiv:2604.26961). I need to verify:\n1. Does this paper actually exist?\n2. Is it accepted at ACL 2026?\n3. Does it validate data-flow knowledge transfer to neural models?\n4. What are the key results (e.g., 22% ExactMatch gains)?\n\nUse WebSearch and WebFetch to find this. Report exactly what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80901a79-db2d-4341-93fb-e19c20d02539",
  "isSidechain": false,
  "requestId": "req_011CauNpdk53vtehhRFvbK8m",
  "type": "assistant",
  "uuid": "7b0823c9-9f0a-4988-b6a6-51ebca7ea9bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183WJfQj77jkBPRLR41mTUB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18222,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1493,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 18222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18222
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

_source line 12 · 2026-05-10T18:40:31.600Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011Ewss6APxYGR8ZLddgpp5t`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check LocAgent and SweRank papers",
  "prompt": "Search the web and verify these two papers:\n\n1. \"LocAgent: Graph-Guided LLM Agents for Code Localization\" (arXiv:2503.09089) — claimed ACL 2025, 92.7% file-level accuracy on SWE-bench Lite using import/invocation/inheritance edges with fine-tuned Qwen2.5-32B. Does it exist? Are the claims accurate?\n\n2. \"SweRank: Software Issue Localization with Code Ranking\" (arXiv:2505.07849) — claimed SOTA retrieve-and-rerank, outperforms agent-based systems, text-only. Does it exist? Are claims accurate?\n\nUse WebSearch and WebFetch. Report exactly what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b0823c9-9f0a-4988-b6a6-51ebca7ea9bf",
  "isSidechain": false,
  "requestId": "req_011CauNpdk53vtehhRFvbK8m",
  "type": "assistant",
  "uuid": "27d42fb3-8f00-4e2c-998a-4acc29c8c4a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183WJfQj77jkBPRLR41mTUB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18222,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1493,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 18222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18222
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

_source line 13 · 2026-05-10T18:40:38.304Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UfiKMPqkR3Ww5x73hbMXHS`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search competing work on data-flow context selection",
  "prompt": "I'm reviewing a paper idea that distills data-flow (def-use) signals into a lightweight neural model for repository-level code repair context selection. I need to find competing or closely related work that the authors may have missed.\n\nSearch for the following using WebSearch:\n1. \"data-flow context selection code repair 2025 2026 site:arxiv.org\"\n2. \"def-use analysis neural code understanding 2025 2026\"\n3. \"code property graph context pruning LLM 2025 2026\"\n4. \"repository level fault localization graph neural 2025 2026\"\n5. \"program analysis guided code generation context 2025 2026\"\n6. Search for \"CodeQL code repair\" or \"CodeQL LLM\" to see if anyone has used CodeQL for similar purposes\n7. Search for any work combining BM25/retrieval with structural code features for code tasks\n\nReport all relevant papers you find, with titles, venues, and brief descriptions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27d42fb3-8f00-4e2c-998a-4acc29c8c4a4",
  "isSidechain": false,
  "requestId": "req_011CauNpdk53vtehhRFvbK8m",
  "type": "assistant",
  "uuid": "2bca583c-2b47-4106-90f4-0d68e110037b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183WJfQj77jkBPRLR41mTUB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18222,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1493,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 18222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18222
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

_source line 14 · 2026-05-10T18:40:43.665Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016RC63Z4o7sNhSMcTzQPqya`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify SWE-bench Pro SOTA and eval costs",
  "prompt": "Search the web to verify:\n1. Current SOTA scores on SWE-bench Pro (as of May 2026). The idea claims top systems score 42-59%.\n2. Current SOTA scores on SWE-bench Lite (the idea needs strong baselines here).\n3. Whether Qwen3.6-27B exists as a model. If not, what is the correct name for Qwen's ~27B code model?\n4. How long does SWE-bench evaluation typically take per instance? The idea claims ~9min/instance.\n5. What is SWE-smith and is it publicly available with 128 repositories?\n\nUse WebSearch to verify these. Be precise about what you find vs. what you cannot confirm."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bca583c-2b47-4106-90f4-0d68e110037b",
  "isSidechain": false,
  "requestId": "req_011CauNpdk53vtehhRFvbK8m",
  "type": "assistant",
  "uuid": "eaaf424e-a7cf-47bd-995e-2404806dd195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0183WJfQj77jkBPRLR41mTUB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18222,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1493,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 18222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18222
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

_source line 15 · 2026-05-10T18:41:01.720Z_

<details><summary>↩ Tool result · `toolu_01U1PdcUCh9BN6dAHJB7XNrq`</summary>

```text
Here are my findings for each of your four questions:

**1. Does this paper actually exist on arXiv?**

Yes. The paper is real and accessible at [arXiv:2605.03117](https://arxiv.org/abs/2605.03117). Its full title is "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair," authored by Shahd Seddik and Fatemeh Fard (University of British Columbia), submitted May 4, 2026.

**2. Does it use def-use edges as runtime tool calls?**

Yes, but with a nuance worth noting. The paper builds a multi-granularity program graph that extends structural relationships down to **statement-level nodes connected by intra-procedural definition-use edges**. These def-use edges are not themselves "tool calls" in the LLM sense; rather, the graph (including the def-use edges) is **exposed to the agent through a three-tier tool API**. This makes data-flow slicing a first-class, queryable agent primitive -- the agent can issue a tool call to trace which statements define or consume a variable. So the def-use edges are the underlying graph data that the agent queries via tool calls at runtime.

**3. Does it report +17pp Function Recall@1 on SWE-bench Lite?**

Yes. The paper reports that ARISE improves **Function Recall@1 by 17.0 percentage points** over the unmodified SWE-agent baseline on SWE-bench Lite (300 real GitHub issues, 11 Python repositories). It also reports a 15.0 percentage-point improvement in Line Recall@1.

**4. Does it report 4.7pp Pass@1 improvement?**

Yes. The paper reports ARISE achieves **22.0% Pass@1 (66/300)**, which is a **4.7 percentage-point improvement** over SWE-agent. The backbone model used was Qwen2.5-Coder-32B-Instruct.

All four claims check out against the actual arXiv listing.

Sources:
- [ARISE paper on arXiv (abstract)](https://arxiv.org/abs/2605.03117)
- [ARISE paper on arXiv (HTML version)](https://arxiv.org/html/2605.03117)

agentId: a33c9ea291d6d06b2 (use SendMessage with to: 'a33c9ea291d6d06b2' to continue this agent)
&lt;usage>total_tokens: 13897
tool_uses: 4
duration_ms: 38179&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80901a79-db2d-4341-93fb-e19c20d02539",
  "isSidechain": false,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "type": "user",
  "uuid": "be2bd930-5c15-4760-9e11-303d0d47fc0c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the paper \"ARISE: Repository-level Graph Representation for Agentic Fault Localization and Repair\" (arXiv:2605.03117). I need to verify:\n1. Does this paper actually exist on arXiv?\n2. Does it use def-use edges as runtime tool calls?\n3. Does it report +17pp Function Recall@1 on SWE-bench Lite?\n4. Does it report 4.7pp Pass@1 improvement?\n\nUse WebSearch to find this paper and WebFetch to read its abstract/details if possible. Report exactly what you find — do not fabricate details.",
    "agentId": "a33c9ea291d6d06b2",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings for each of your four questions:\n\n**1. Does this paper actually exist on arXiv?**\n\nYes. The paper is real and accessible at [arXiv:2605.03117](https://arxiv.org/abs/2605.03117). Its full title is \"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair,\" authored by Shahd Seddik and Fatemeh Fard (University of British Columbia), submitted May 4, 2026.\n\n**2. Does it use def-use edges as runtime tool calls?**\n\nYes, but with a nuance worth noting. The paper builds a multi-granularity program graph that extends structural relationships down to **statement-level nodes connected by intra-procedural definition-use edges**. These def-use edges are not themselves \"tool calls\" in the LLM sense; rather, the graph (including the def-use edges) is **exposed to the agent through a three-tier tool API**. This makes data-flow slicing a first-class, queryable agent primitive -- the agent can issue a tool call to trace which statements define or consume a variable. So the def-use edges are the underlying graph data that the agent queries via tool calls at runtime.\n\n**3. Does it report +17pp Function Recall@1 on SWE-bench Lite?**\n\nYes. The paper reports that ARISE improves **Function Recall@1 by 17.0 percentage points** over the unmodified SWE-agent baseline on SWE-bench Lite (300 real GitHub issues, 11 Python repositories). It also reports a 15.0 percentage-point improvement in Line Recall@1.\n\n**4. Does it report 4.7pp Pass@1 improvement?**\n\nYes. The paper reports ARISE achieves **22.0% Pass@1 (66/300)**, which is a **4.7 percentage-point improvement** over SWE-agent. The backbone model used was Qwen2.5-Coder-32B-Instruct.\n\nAll four claims check out against the actual arXiv listing.\n\nSources:\n- [ARISE paper on arXiv (abstract)](https://arxiv.org/abs/2605.03117)\n- [ARISE paper on arXiv (HTML version)](https://arxiv.org/html/2605.03117)"
      }
    ],
    "totalDurationMs": 38179,
    "totalTokens": 13897,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1378,
      "cache_read_input_tokens": 11957,
      "output_tokens": 561,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1378
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 561,
          "cache_read_input_tokens": 11957,
          "cache_creation_input_tokens": 1378,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1378,
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
      "otherToolCount": 4
    }
  },
  "sourceToolAssistantUUID": "80901a79-db2d-4341-93fb-e19c20d02539",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T18:41:18.903Z_

<details><summary>↩ Tool result · `toolu_01NXXAiwTdGvRYpmNyGoLR9X`</summary>

```text
Here are my findings on each of your questions:

**1. Does this paper actually exist?**

Yes. The paper is real and available on arXiv at ID **2604.26961**, submitted April 9, 2026. The full title is "Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding." The authors are Pengfei He, Shaowei Wang, Tse-Hsun (Peter) Chen, and Muhammad Asaduzzaman. The system is indeed called "Sliceformer" and uses CodeT5+ as its backbone.

**2. Is it accepted at ACL 2026?**

The arXiv abstract page metadata indicates "Accepted at ACL 2026." However, the full HTML body of the paper itself does not explicitly repeat this claim in the text. The acceptance note appears on the abstract/metadata page, which is a standard place for authors to note venue acceptance on arXiv. So the evidence points to **yes, it is marked as accepted at ACL 2026** on arXiv.

**3. Does it validate data-flow knowledge transfer to neural models?**

Yes. The paper's central thesis is that dataflow-aware pretraining can transfer data-flow knowledge into neural sequence-to-sequence models. It validates this through:
- Two novel pretraining objectives that leverage Data Flow Graphs (DFGs): (a) **dataflow-preserving statement permutation** and (b) **dataflow-aware span corruption**.
- Ablation studies showing each component's contribution, with span corruption identified as the most impactful for learning data dependencies.
- Comparative results demonstrating clear superiority over models that lack dataflow pretraining.

**4. What are the key results?**

- **Java ExactMatch**: 92.20% (Sliceformer) vs. 85.77% (NS-slicer/GraphBERT baseline) -- a **6.4% gain**.
- **Python ExactMatch**: 83.15% (Sliceformer) vs. 61.25% (NS-slicer baseline) -- a **21.9% gain**.
- The "up to 22% ExactMatch gains" claim in the abstract rounds the 21.9% Python improvement. This is accurate.

In summary: the paper exists, it is marked as accepted at ACL 2026 on its arXiv page, it does validate data-flow knowledge transfer to neural models via novel pretraining objectives, and the headline result of ~22% ExactMatch gain (specifically 21.9% on Python) is substantiated by the reported numbers.

Sources:
- [arXiv Abstract: 2604.26961](https://arxiv.org/abs/2604.26961)
- [arXiv HTML: Full Paper](https://arxiv.org/html/2604.26961)

agentId: a8ce9e4db0ebbe7fc (use SendMessage with to: 'a8ce9e4db0ebbe7fc' to continue this agent)
&lt;usage>total_tokens: 14501
tool_uses: 5
duration_ms: 52158&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b0823c9-9f0a-4988-b6a6-51ebca7ea9bf",
  "isSidechain": false,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "type": "user",
  "uuid": "607962e1-d5d9-45bb-a8bc-de5260510be1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for the paper \"Sliceformer: Static Program Slicing Using Language Models With Dataflow-Aware Pretraining\" (arXiv:2604.26961). I need to verify:\n1. Does this paper actually exist?\n2. Is it accepted at ACL 2026?\n3. Does it validate data-flow knowledge transfer to neural models?\n4. What are the key results (e.g., 22% ExactMatch gains)?\n\nUse WebSearch and WebFetch to find this. Report exactly what you find.",
    "agentId": "a8ce9e4db0ebbe7fc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are my findings on each of your questions:\n\n**1. Does this paper actually exist?**\n\nYes. The paper is real and available on arXiv at ID **2604.26961**, submitted April 9, 2026. The full title is \"Static Program Slicing Using Language Models With Dataflow-Aware Pretraining and Constrained Decoding.\" The authors are Pengfei He, Shaowei Wang, Tse-Hsun (Peter) Chen, and Muhammad Asaduzzaman. The system is indeed called \"Sliceformer\" and uses CodeT5+ as its backbone.\n\n**2. Is it accepted at ACL 2026?**\n\nThe arXiv abstract page metadata indicates \"Accepted at ACL 2026.\" However, the full HTML body of the paper itself does not explicitly repeat this claim in the text. The acceptance note appears on the abstract/metadata page, which is a standard place for authors to note venue acceptance on arXiv. So the evidence points to **yes, it is marked as accepted at ACL 2026** on arXiv.\n\n**3. Does it validate data-flow knowledge transfer to neural models?**\n\nYes. The paper's central thesis is that dataflow-aware pretraining can transfer data-flow knowledge into neural sequence-to-sequence models. It validates this through:\n- Two novel pretraining objectives that leverage Data Flow Graphs (DFGs): (a) **dataflow-preserving statement permutation** and (b) **dataflow-aware span corruption**.\n- Ablation studies showing each component's contribution, with span corruption identified as the most impactful for learning data dependencies.\n- Comparative results demonstrating clear superiority over models that lack dataflow pretraining.\n\n**4. What are the key results?**\n\n- **Java ExactMatch**: 92.20% (Sliceformer) vs. 85.77% (NS-slicer/GraphBERT baseline) -- a **6.4% gain**.\n- **Python ExactMatch**: 83.15% (Sliceformer) vs. 61.25% (NS-slicer baseline) -- a **21.9% gain**.\n- The \"up to 22% ExactMatch gains\" claim in the abstract rounds the 21.9% Python improvement. This is accurate.\n\nIn summary: the paper exists, it is marked as accepted at ACL 2026 on its arXiv page, it does validate data-flow knowledge transfer to neural models via novel pretraining objectives, and the headline result of ~22% ExactMatch gain (specifically 21.9% on Python) is substantiated by the reported numbers.\n\nSources:\n- [arXiv Abstract: 2604.26961](https://arxiv.org/abs/2604.26961)\n- [arXiv HTML: Full Paper](https://arxiv.org/html/2604.26961)"
      }
    ],
    "totalDurationMs": 52158,
    "totalTokens": 14501,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 13194,
      "output_tokens": 665,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 641
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 665,
          "cache_read_input_tokens": 13194,
          "cache_creation_input_tokens": 641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 641,
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
      "otherToolCount": 5
    }
  },
  "sourceToolAssistantUUID": "7b0823c9-9f0a-4988-b6a6-51ebca7ea9bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T18:42:03.949Z_

<details><summary>↩ Tool result · `toolu_011Ewss6APxYGR8ZLddgpp5t`</summary>

```text
I now have comprehensive verified information on both papers. Here is my report.

---

## Paper 1: LocAgent (arXiv:2503.09089)

**Verdict: The paper exists. All claims are accurate.**

- **Title:** "LocAgent: Graph-Guided LLM Agents for Code Localization"
- **Authors:** Zhaoling Chen, Xiangru Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, and Xingyao Wang (Gerstein Lab / Yale)
- **arXiv ID:** 2503.09089 -- confirmed, submitted March 12, 2025, updated April 29, 2025 (v2)
- **ACL 2025:** Confirmed accepted. It appears in the ACL Anthology as `2025.acl-long.426`, published at the 63rd Annual Meeting of the Association for Computational Linguistics (Long Papers), Vienna, Austria, July 2025, pages 8697-8727, with DOI `10.18653/v1/2025.acl-long.426`.
- **92.7% file-level accuracy on SWE-bench Lite:** Confirmed. The paper reports "up to 92.7% accuracy on file-level localization."
- **Import/invocation/inheritance edges:** Confirmed. The paper parses codebases into "directed heterogeneous graphs" capturing three dependency types: imports, invocations, and inheritance relationships between code entities (files, classes, functions).
- **Fine-tuned Qwen2.5-32B:** Confirmed. The model is specifically "Qwen-2.5-Coder-Instruct-32B" (fine-tuned), achieving results comparable to proprietary models at ~86% cost reduction.
- **Additional claim:** 12% improvement in downstream GitHub issue resolution success rates (Pass@10).

All stated claims check out.

---

## Paper 2: SweRank (arXiv:2505.07849)

**Verdict: The paper exists. Claims are mostly accurate, with one important update.**

- **Title:** "SweRank: Software Issue Localization with Code Ranking"
- **Authors:** Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty (UIUC, Salesforce Research, KAIST)
- **arXiv ID:** 2505.07849 -- confirmed, submitted May 7, 2025. The latest arXiv version (as of April 22, 2026) is the camera-ready for its accepted venue.
- **SOTA retrieve-and-rerank:** Confirmed. SweRank achieves state-of-the-art performance on SWE-Bench-Lite and LocBench. Specifically:
  - SweRankEmbed-Large (7B): 82.12% function-level accuracy@10
  - SweRankEmbed-Large + SweRankLLM-Large (32B reranker): 88.69% function-level accuracy@10
- **Outperforms agent-based systems:** Confirmed. The paper explicitly claims to outperform "costly agent-based systems using closed-source LLMs like Claude-3.5," including LocAgent. It also achieves up to a 60x better accuracy-to-cost ratio ($0.011-$0.015 per example vs. $0.66 for Claude-powered agents).
- **Text-only:** Confirmed. SweRank reframes localization as a code ranking task using embedding similarity (bi-encoder retriever + listwise LLM reranker). It does not use graph structure, dependency analysis, or code graphs -- it is purely text-based retrieve-and-rerank.
- **Venue note:** The paper was not just an arXiv preprint -- it was accepted at **ICLR 2026** (not just arXiv as implied by the query). Salesforce lists it among their 21 accepted ICLR 2026 papers. There is also a follow-up paper, "SweRank+" (arXiv:2512.20482), extending the approach to multilingual and multi-turn settings.

All stated claims check out. The only nuance is that by now (May 2026) it has been accepted at ICLR 2026, making it a peer-reviewed publication rather than just a preprint.

---

Sources:
- [LocAgent on arXiv](https://arxiv.org/abs/2503.09089)
- [LocAgent at ACL Anthology](https://aclanthology.org/2025.acl-long.426/)
- [LocAgent GitHub](https://github.com/gersteinlab/LocAgent)
- [SweRank on arXiv](https://arxiv.org/abs/2505.07849)
- [SweRank on HuggingFace Papers](https://huggingface.co/papers/2505.07849)
- [SweRank GitHub](https://github.com/gangiswag/SweRank)
- [Salesforce AI Research at ICLR 2026](https://www.salesforce.com/blog/salesforce-iclr-2026/)
- [MarkTechPost coverage of SweRank](https://www.marktechpost.com/2025/05/13/agent-based-debugging-gets-a-cost-effective-alternative-salesforce-ai-presents-swerank-for-accurate-and-scalable-software-issue-localization/)

agentId: a418c5b4cf9dbb7ee (use SendMessage with to: 'a418c5b4cf9dbb7ee' to continue this agent)
&lt;usage>total_tokens: 18028
tool_uses: 10
duration_ms: 92346&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27d42fb3-8f00-4e2c-998a-4acc29c8c4a4",
  "isSidechain": false,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "type": "user",
  "uuid": "058dcd88-505e-4d1f-8326-f6696b471442",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web and verify these two papers:\n\n1. \"LocAgent: Graph-Guided LLM Agents for Code Localization\" (arXiv:2503.09089) — claimed ACL 2025, 92.7% file-level accuracy on SWE-bench Lite using import/invocation/inheritance edges with fine-tuned Qwen2.5-32B. Does it exist? Are the claims accurate?\n\n2. \"SweRank: Software Issue Localization with Code Ranking\" (arXiv:2505.07849) — claimed SOTA retrieve-and-rerank, outperforms agent-based systems, text-only. Does it exist? Are claims accurate?\n\nUse WebSearch and WebFetch. Report exactly what you find.",
    "agentId": "a418c5b4cf9dbb7ee",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive verified information on both papers. Here is my report.\n\n---\n\n## Paper 1: LocAgent (arXiv:2503.09089)\n\n**Verdict: The paper exists. All claims are accurate.**\n\n- **Title:** \"LocAgent: Graph-Guided LLM Agents for Code Localization\"\n- **Authors:** Zhaoling Chen, Xiangru Tang, Gangda Deng, Fang Wu, Jialong Wu, Zhiwei Jiang, Viktor Prasanna, Arman Cohan, and Xingyao Wang (Gerstein Lab / Yale)\n- **arXiv ID:** 2503.09089 -- confirmed, submitted March 12, 2025, updated April 29, 2025 (v2)\n- **ACL 2025:** Confirmed accepted. It appears in the ACL Anthology as `2025.acl-long.426`, published at the 63rd Annual Meeting of the Association for Computational Linguistics (Long Papers), Vienna, Austria, July 2025, pages 8697-8727, with DOI `10.18653/v1/2025.acl-long.426`.\n- **92.7% file-level accuracy on SWE-bench Lite:** Confirmed. The paper reports \"up to 92.7% accuracy on file-level localization.\"\n- **Import/invocation/inheritance edges:** Confirmed. The paper parses codebases into \"directed heterogeneous graphs\" capturing three dependency types: imports, invocations, and inheritance relationships between code entities (files, classes, functions).\n- **Fine-tuned Qwen2.5-32B:** Confirmed. The model is specifically \"Qwen-2.5-Coder-Instruct-32B\" (fine-tuned), achieving results comparable to proprietary models at ~86% cost reduction.\n- **Additional claim:** 12% improvement in downstream GitHub issue resolution success rates (Pass@10).\n\nAll stated claims check out.\n\n---\n\n## Paper 2: SweRank (arXiv:2505.07849)\n\n**Verdict: The paper exists. Claims are mostly accurate, with one important update.**\n\n- **Title:** \"SweRank: Software Issue Localization with Code Ranking\"\n- **Authors:** Revanth Gangi Reddy, Tarun Suresh, JaeHyeok Doo, Ye Liu, Xuan Phi Nguyen, Yingbo Zhou, Semih Yavuz, Caiming Xiong, Heng Ji, Shafiq Joty (UIUC, Salesforce Research, KAIST)\n- **arXiv ID:** 2505.07849 -- confirmed, submitted May 7, 2025. The latest arXiv version (as of April 22, 2026) is the camera-ready for its accepted venue.\n- **SOTA retrieve-and-rerank:** Confirmed. SweRank achieves state-of-the-art performance on SWE-Bench-Lite and LocBench. Specifically:\n  - SweRankEmbed-Large (7B): 82.12% function-level accuracy@10\n  - SweRankEmbed-Large + SweRankLLM-Large (32B reranker): 88.69% function-level accuracy@10\n- **Outperforms agent-based systems:** Confirmed. The paper explicitly claims to outperform \"costly agent-based systems using closed-source LLMs like Claude-3.5,\" including LocAgent. It also achieves up to a 60x better accuracy-to-cost ratio ($0.011-$0.015 per example vs. $0.66 for Claude-powered agents).\n- **Text-only:** Confirmed. SweRank reframes localization as a code ranking task using embedding similarity (bi-encoder retriever + listwise LLM reranker). It does not use graph structure, dependency analysis, or code graphs -- it is purely text-based retrieve-and-rerank.\n- **Venue note:** The paper was not just an arXiv preprint -- it was accepted at **ICLR 2026** (not just arXiv as implied by the query). Salesforce lists it among their 21 accepted ICLR 2026 papers. There is also a follow-up paper, \"SweRank+\" (arXiv:2512.20482), extending the approach to multilingual and multi-turn settings.\n\nAll stated claims check out. The only nuance is that by now (May 2026) it has been accepted at ICLR 2026, making it a peer-reviewed publication rather than just a preprint.\n\n---\n\nSources:\n- [LocAgent on arXiv](https://arxiv.org/abs/2503.09089)\n- [LocAgent at ACL Anthology](https://aclanthology.org/2025.acl-long.426/)\n- [LocAgent GitHub](https://github.com/gersteinlab/LocAgent)\n- [SweRank on arXiv](https://arxiv.org/abs/2505.07849)\n- [SweRank on HuggingFace Papers](https://huggingface.co/papers/2505.07849)\n- [SweRank GitHub](https://github.com/gangiswag/SweRank)\n- [Salesforce AI Research at ICLR 2026](https://www.salesforce.com/blog/salesforce-iclr-2026/)\n- [MarkTechPost coverage of SweRank](https://www.marktechpost.com/2025/05/13/agent-based-debugging-gets-a-cost-effective-alternative-salesforce-ai-presents-swerank-for-accurate-and-scalable-software-issue-localization/)"
      }
    ],
    "totalDurationMs": 92346,
    "totalTokens": 18028,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 533,
      "cache_read_input_tokens": 16109,
      "output_tokens": 1385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 533
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1385,
          "cache_read_input_tokens": 16109,
          "cache_creation_input_tokens": 533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 533,
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
  "sourceToolAssistantUUID": "27d42fb3-8f00-4e2c-998a-4acc29c8c4a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
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
  "leafUuid": "058dcd88-505e-4d1f-8326-f6696b471442",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify StructFuse feasibility and competing work for EMNLP 2026 submission",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Tool result

_source line 20 · 2026-05-10T18:42:04.217Z_

<details><summary>↩ Tool result · `toolu_016RC63Z4o7sNhSMcTzQPqya`</summary>

```text
Here are the verified findings for all five questions:

---

## 1. SWE-bench Pro SOTA Scores

The claim of "42-59%" is **partially outdated/inaccurate as of May 2026**. The current leaderboard shows scores significantly higher than that range:

- **Claude Mythos Preview**: 77.8% (top score, as of April 28, 2026)
- **Claude Opus 4.7 (Adaptive)**: 64.3%
- **GPT-5.5**: 58.6%
- Three different agent systems running the same model (Opus 4.5) scored between 50.2% and 55.4%, showing that scaffolding matters significantly.

The 42-59% range may have been accurate at an earlier point, but the frontier has moved well past 59% by May 2026. On the standardized SEAL leaderboard with constrained scaffolding, scores are lower (e.g., Claude Opus 4.5 at 45.9%), so the range depends heavily on whether custom agent scaffolding is permitted.

## 2. SWE-bench Lite SOTA Scores

The top scores on SWE-bench Lite as of May 2026:

- **Claude Opus 4.6**: 62.7% (top score)
- **MiniMax M2.5**: 56.3%
- 62 models have been evaluated; average score is 26.8% with a standard deviation of 19.9%.

For context, SWE-bench Verified (a related but different benchmark) shows much higher scores, with Claude Mythos Preview at 93.9%. This suggests SWE-bench Lite is an intermediate difficulty level -- harder than Verified but easier than Pro.

## 3. Qwen3.6-27B Existence

**Confirmed: Qwen3.6-27B does exist.** It was released on April 22, 2026 by the Qwen team (Alibaba Group). The official model name is **Qwen/Qwen3.6-27B**, and it is available on Hugging Face, Ollama, vLLM, and other platforms. It is described as a "Flagship-Level Coding in a 27B Dense Model" that uses gated delta networks hybrid attention, supports vision+text input, and has a 262K context window. The GitHub repo is at `github.com/QwenLM/Qwen3.6`.

## 4. SWE-bench Evaluation Time per Instance

The claim of "~9 min/instance" is **roughly in the right ballpark but varies widely**:

- **Agentless** averages ~209 seconds (~3.5 min) of inference time and ~728 seconds (~12 min) of CPU time per instance on SWE-bench Verified.
- The All Hands team originally reported over 10 minutes per sample for SWE-bench Lite (300 examples took "several days").
- Optimized Docker setups can run full SWE-bench Verified (500 instances) in about 62 minutes on a beefy machine (~7.4 seconds per instance for just the test execution harness, not including agent inference).
- Per-instance wall-clock timeout is typically set at 45 minutes maximum.

The ~9 min/instance figure likely refers to total agent inference + evaluation time for a mid-tier system. This is plausible but highly variable depending on the model, agent framework, and hardware. Lightweight/agentless approaches can be faster (3-4 min), while complex agent systems can take much longer.

## 5. SWE-smith: Availability and 128 Repositories

**Confirmed: SWE-smith is publicly available and uses exactly 128 repositories.**

- SWE-smith is a data generation pipeline that creates task instances from open-source repositories. It was published as a NeurIPS 2025 Datasets & Benchmarks Spotlight paper.
- It generates **50,000 task instances** from **128 Python repositories** (average of 381 instances per repo).
- All assets (collection procedure, task instances, trajectories, and trained models) are open-sourced at [swesmith.com](https://swesmith.com) and on [GitHub](https://github.com/SWE-bench/SWE-smith).
- Using SWE-smith data, they trained **SWE-agent-LM-32B**, which achieved 40.2% on SWE-bench Verified -- state of the art among open-source models at the time of publication.

---

**Summary of claim accuracy:**

| Claim | Verdict |
|---|---|
| SWE-bench Pro top systems: 42-59% | Outdated -- frontier is now up to 77.8% with custom scaffolding, though ~42-58% may hold under standardized evaluation |
| SWE-bench Lite strong baselines needed | Valid -- top score is 62.7%, many strong baselines exist |
| Qwen3.6-27B exists | Confirmed -- released April 22, 2026 |
| ~9 min/instance evaluation time | Plausible but variable (3-12 min depending on setup) |
| SWE-smith publicly available with 128 repos | Confirmed -- 128 repos, 50K instances, fully open-sourced |

Sources:
- [SWE-bench Leaderboards](https://www.swebench.com/)
- [SWE-Bench Pro Leaderboard (Scale AI)](https://labs.scale.com/leaderboard/swe_bench_pro_public)
- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81% (Morph)](https://www.morphllm.com/swe-bench-pro)
- [SWE-bench Lite Leaderboard 2026](https://pricepertoken.com/leaderboards/benchmark/swe-bench-lite)
- [Qwen3.6-27B Blog Post](https://qwen.ai/blog?id=qwen3.6-27b)
- [Qwen/Qwen3.6-27B on Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B)
- [How to run SWE-bench Verified in one hour (Epoch AI)](https://epoch.ai/blog/swebench-docker)
- [SWE-smith on GitHub](https://github.com/SWE-bench/SWE-smith)
- [SWE-smith paper (arXiv)](https://arxiv.org/abs/2504.21798)
- [SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness](https://arxiv.org/html/2509.09853v1)
- [SWE-bench Pro Benchmark 2026 (BenchLM)](https://benchlm.ai/benchmarks/swePro)

agentId: addd1852ac844ebc4 (use SendMessage with to: 'addd1852ac844ebc4' to continue this agent)
&lt;usage>total_tokens: 18736
tool_uses: 9
duration_ms: 80549&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eaaf424e-a7cf-47bd-995e-2404806dd195",
  "isSidechain": false,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "type": "user",
  "uuid": "22ac52d4-fbae-4bac-9ca9-499669f08db0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web to verify:\n1. Current SOTA scores on SWE-bench Pro (as of May 2026). The idea claims top systems score 42-59%.\n2. Current SOTA scores on SWE-bench Lite (the idea needs strong baselines here).\n3. Whether Qwen3.6-27B exists as a model. If not, what is the correct name for Qwen's ~27B code model?\n4. How long does SWE-bench evaluation typically take per instance? The idea claims ~9min/instance.\n5. What is SWE-smith and is it publicly available with 128 repositories?\n\nUse WebSearch to verify these. Be precise about what you find vs. what you cannot confirm.",
    "agentId": "addd1852ac844ebc4",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the verified findings for all five questions:\n\n---\n\n## 1. SWE-bench Pro SOTA Scores\n\nThe claim of \"42-59%\" is **partially outdated/inaccurate as of May 2026**. The current leaderboard shows scores significantly higher than that range:\n\n- **Claude Mythos Preview**: 77.8% (top score, as of April 28, 2026)\n- **Claude Opus 4.7 (Adaptive)**: 64.3%\n- **GPT-5.5**: 58.6%\n- Three different agent systems running the same model (Opus 4.5) scored between 50.2% and 55.4%, showing that scaffolding matters significantly.\n\nThe 42-59% range may have been accurate at an earlier point, but the frontier has moved well past 59% by May 2026. On the standardized SEAL leaderboard with constrained scaffolding, scores are lower (e.g., Claude Opus 4.5 at 45.9%), so the range depends heavily on whether custom agent scaffolding is permitted.\n\n## 2. SWE-bench Lite SOTA Scores\n\nThe top scores on SWE-bench Lite as of May 2026:\n\n- **Claude Opus 4.6**: 62.7% (top score)\n- **MiniMax M2.5**: 56.3%\n- 62 models have been evaluated; average score is 26.8% with a standard deviation of 19.9%.\n\nFor context, SWE-bench Verified (a related but different benchmark) shows much higher scores, with Claude Mythos Preview at 93.9%. This suggests SWE-bench Lite is an intermediate difficulty level -- harder than Verified but easier than Pro.\n\n## 3. Qwen3.6-27B Existence\n\n**Confirmed: Qwen3.6-27B does exist.** It was released on April 22, 2026 by the Qwen team (Alibaba Group). The official model name is **Qwen/Qwen3.6-27B**, and it is available on Hugging Face, Ollama, vLLM, and other platforms. It is described as a \"Flagship-Level Coding in a 27B Dense Model\" that uses gated delta networks hybrid attention, supports vision+text input, and has a 262K context window. The GitHub repo is at `github.com/QwenLM/Qwen3.6`.\n\n## 4. SWE-bench Evaluation Time per Instance\n\nThe claim of \"~9 min/instance\" is **roughly in the right ballpark but varies widely**:\n\n- **Agentless** averages ~209 seconds (~3.5 min) of inference time and ~728 seconds (~12 min) of CPU time per instance on SWE-bench Verified.\n- The All Hands team originally reported over 10 minutes per sample for SWE-bench Lite (300 examples took \"several days\").\n- Optimized Docker setups can run full SWE-bench Verified (500 instances) in about 62 minutes on a beefy machine (~7.4 seconds per instance for just the test execution harness, not including agent inference).\n- Per-instance wall-clock timeout is typically set at 45 minutes maximum.\n\nThe ~9 min/instance figure likely refers to total agent inference + evaluation time for a mid-tier system. This is plausible but highly variable depending on the model, agent framework, and hardware. Lightweight/agentless approaches can be faster (3-4 min), while complex agent systems can take much longer.\n\n## 5. SWE-smith: Availability and 128 Repositories\n\n**Confirmed: SWE-smith is publicly available and uses exactly 128 repositories.**\n\n- SWE-smith is a data generation pipeline that creates task instances from open-source repositories. It was published as a NeurIPS 2025 Datasets & Benchmarks Spotlight paper.\n- It generates **50,000 task instances** from **128 Python repositories** (average of 381 instances per repo).\n- All assets (collection procedure, task instances, trajectories, and trained models) are open-sourced at [swesmith.com](https://swesmith.com) and on [GitHub](https://github.com/SWE-bench/SWE-smith).\n- Using SWE-smith data, they trained **SWE-agent-LM-32B**, which achieved 40.2% on SWE-bench Verified -- state of the art among open-source models at the time of publication.\n\n---\n\n**Summary of claim accuracy:**\n\n| Claim | Verdict |\n|---|---|\n| SWE-bench Pro top systems: 42-59% | Outdated -- frontier is now up to 77.8% with custom scaffolding, though ~42-58% may hold under standardized evaluation |\n| SWE-bench Lite strong baselines needed | Valid -- top score is 62.7%, many strong baselines exist |\n| Qwen3.6-27B exists | Confirmed -- released April 22, 2026 |\n| ~9 min/instance evaluation time | Plausible but variable (3-12 min depending on setup) |\n| SWE-smith publicly available with 128 repos | Confirmed -- 128 repos, 50K instances, fully open-sourced |\n\nSources:\n- [SWE-bench Leaderboards](https://www.swebench.com/)\n- [SWE-Bench Pro Leaderboard (Scale AI)](https://labs.scale.com/leaderboard/swe_bench_pro_public)\n- [SWE-Bench Pro Leaderboard (2026): Why 46% Beats 81% (Morph)](https://www.morphllm.com/swe-bench-pro)\n- [SWE-bench Lite Leaderboard 2026](https://pricepertoken.com/leaderboards/benchmark/swe-bench-lite)\n- [Qwen3.6-27B Blog Post](https://qwen.ai/blog?id=qwen3.6-27b)\n- [Qwen/Qwen3.6-27B on Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B)\n- [How to run SWE-bench Verified in one hour (Epoch AI)](https://epoch.ai/blog/swebench-docker)\n- [SWE-smith on GitHub](https://github.com/SWE-bench/SWE-smith)\n- [SWE-smith paper (arXiv)](https://arxiv.org/abs/2504.21798)\n- [SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness](https://arxiv.org/html/2509.09853v1)\n- [SWE-bench Pro Benchmark 2026 (BenchLM)](https://benchlm.ai/benchmarks/swePro)"
      }
    ],
    "totalDurationMs": 80549,
    "totalTokens": 18736,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 720,
      "cache_creation_input_tokens": 2650,
      "cache_read_input_tokens": 13693,
      "output_tokens": 1673,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2650
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 720,
          "output_tokens": 1673,
          "cache_read_input_tokens": 13693,
          "cache_creation_input_tokens": 2650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2650,
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
      "otherToolCount": 9
    }
  },
  "sourceToolAssistantUUID": "eaaf424e-a7cf-47bd-995e-2404806dd195",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T18:43:14.511Z_

<details><summary>↩ Tool result · `toolu_01UfiKMPqkR3Ww5x73hbMXHS`</summary>

```text
Here is the comprehensive landscape of competing and closely related work that the authors should consider referencing or differentiating from. I have organized the papers by thematic relevance.

---

## 1. Graph-Based Repository-Level Fault Localization and Repair (Most Directly Competing)

**ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair**
- arXiv:2605.03117, May 2026
- Augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges. Exposes data-flow slicing as a first-class queryable agent primitive. Evaluated on SWE-bench Lite with Qwen2.5-Coder-32B, improving Function Recall@1 by 17 points and achieving 22.0% Pass@1.
- **Why critical:** This paper uses def-use edges in a repository-level graph for code repair context selection -- essentially the same core idea. The authors must cite and differentiate from it.
- [Paper](https://arxiv.org/abs/2605.03117)

**KGCompass: Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs**
- arXiv:2503.21710, March 2025
- Builds a repository-aware knowledge graph linking issues, PRs, files, classes, and functions. Uses path-guided repair with KG-mined entity paths to augment LLMs. Achieves 45.67% on SWE-Bench-Lite. Found that 89.7% of successful fault locations require 2+ hops in the graph.
- **Why relevant:** Uses structural code graphs for context selection in repair, though at a coarser granularity than def-use.
- [Paper](https://arxiv.org/abs/2503.21710)

**GREPO: A Benchmark for Graph Neural Networks on Repository-Level Bug Localization**
- arXiv:2602.13921, February 2026
- First GNN benchmark for repository-scale bug localization: 86 Python repos, 47,294 bug-fixing tasks. Extracts directory/file/class/function entities with contain, call, and inheritance relations. GNN architectures outperform IR baselines.
- **Why relevant:** Directly benchmarks GNNs for repo-level bug localization -- the evaluation methodology is relevant even if the task framing differs.
- [Paper](https://arxiv.org/abs/2602.13921)

---

## 2. Code Property Graphs + LLMs

**CodeBadger: Bridging Code Property Graphs and Language Models for Program Analysis**
- arXiv:2603.24837, March 2026; accepted at Software Vulnerability Management Workshop @ ICSE 2026
- An MCP server integrating Joern's Code Property Graph engine with LLMs. Provides high-level tools for program slicing, taint tracking, data flow analysis, and semantic code navigation. Demonstrated discovering a buffer overflow in libtiff and patching CVE-2025-6021 in libxml2.
- **Why relevant:** Operationalizes CPG-based data-flow analysis (including def-use) for LLM-driven code tasks, though focused on vulnerability analysis rather than distillation into a lightweight model.
- [Paper](https://arxiv.org/abs/2603.24837)

**LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided LLMs**
- USENIX Security 2025 (arXiv:2507.16585)
- Integrates CPGs with LLMs for vulnerability detection. CPG-based slice construction reduces code size by 67-91% while preserving vulnerability-relevant context. Achieves 15-40% F1 improvements over SOTA.
- **Why relevant:** Demonstrates CPG-guided context pruning for LLMs -- the pruning/selection mechanism is analogous to what a def-use distillation model would learn.
- [Paper](https://arxiv.org/abs/2507.16585)

**CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases**
- NAACL 2025 (arXiv:2408.03910)
- Integrates LLM agents with graph database interfaces. Uses static analysis to extract code graphs (MODULE, CLASS, FUNCTION nodes; CONTAINS, INHERITS, USES edges). Agents construct and execute graph queries for structure-aware context retrieval. Evaluated on CrossCodeEval, SWE-bench, and EvoCodeBench.
- **Why relevant:** Pioneering work on graph-database-mediated code context retrieval for LLMs.
- [Paper](https://arxiv.org/abs/2408.03910)

---

## 3. Fault Localization Context and Granularity for LLM Repair

**A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks**
- arXiv:2604.00167, April 2026
- Studies how fault localization granularity (file, function, line) affects repair under perfect FL assumptions on SWE-Bench. Finds function-level granularity yields the highest resolve rate overall, but optimal granularity is task-dependent.
- **Why relevant:** Directly relevant to the question of what granularity of context selection is optimal for repo-level repair.
- [Paper](https://arxiv.org/abs/2604.00167)

**On the Role of Fault Localization Context for LLM-Based Program Repair**
- arXiv:2604.05481, April 2026
- Finds that expanding file context to approximately 6-10 relevant files improves repair, but element-level and line-level expansion can degrade performance through noise amplification.
- **Why relevant:** Empirically characterizes the context selection problem that the proposed distillation approach aims to solve.
- [Paper](https://arxiv.org/abs/2604.05481)

**RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models**
- arXiv:2601.18044, January 2026
- Introduces per-candidate reasoning where the LLM explains each file/element's functionality and its causal relation to the bug symptom, then uses these explanations as ranking signals in a two-stage scheme. Evaluated on SWE-bench Verified, Lite, and Java.
- **Why relevant:** An alternative approach to context selection for repair that uses reasoning rather than data-flow signals.
- [Paper](https://arxiv.org/abs/2601.18044)

---

## 4. Semantics-Aware Slicing and Analysis-Augmented Repair

**Appatch: Automated Adaptive Prompting LLMs for Real-World Software Vulnerability Patching**
- USENIX Security 2025
- Uses semantics-aware scoping (union slicing) to narrow code to vulnerability-relevant subsets, then applies adaptive exemplar prompting. Raised F1 from 44.9% to 57.2% on 306 real vulnerabilities.
- **Why relevant:** Demonstrates that program slicing (a form of data-flow-guided context selection) significantly improves LLM repair, but uses it at inference time rather than distilling it into a model.
- [Paper](https://arxiv.org/abs/2408.13597)

**D4C: Aligning the Objective of LLM-based Program Repair**
- ICSE 2025 (arXiv:2404.08877)
- A prompting framework that replaces localize-then-repair with direct debugging. Repairs 180 bugs on Defects4J with only 10 samples per patch, surpassing SOTA by 10%.
- **Why relevant:** Challenges the standard pipeline where data-flow context is explicitly extracted, instead letting the LLM perform implicit localization.
- [Paper](https://github.com/CUHK-Shenzhen-SE/D4C)

**CodeCorrector: Context-Aware Prompting for LLM-Based Program Repair**
- Automated Software Engineering journal, 2025
- Uses Chain-of-Thought to analyze test failures, select relevant context, and build context-aware repair prompts. Fixes 38 unique defects that no baseline can handle.
- **Why relevant:** Another context-selection approach for repair, using test-failure-driven reasoning rather than data-flow analysis.
- [Paper](https://link.springer.com/article/10.1007/s10515-025-00512-w)

---

## 5. Distillation for Lightweight Code Models

**Reasoning Distillation for Lightweight Automated Program Repair**
- arXiv:2601.10987, January 2026
- Distills structured symbolic reasoning tags from a large teacher model into a CodeT5-based student for fix-type classification. Improves macro-averaged performance on rare bug categories without increasing model size.
- **Why relevant:** The most directly comparable methodological approach -- distilling program analysis signals into a lightweight model for repair. The paper under review does the same but with data-flow signals specifically.
- [Paper](https://arxiv.org/abs/2601.10987)

---

## 6. Retrieval-Augmented Code Repair (BM25 + Structural Features)

**SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution**
- ACL Findings 2025
- Uses a coarse-to-fine retrieval pipeline combining BM25 with a fine-tuned 7B retriever (initialized from GraphCodeBERT-style embeddings) for code file retrieval, followed by a fine-tuned 72B editor. Achieves 32.8% on SWE-Bench Verified.
- **Why relevant:** Combines sparse retrieval (BM25) with neural structural code features in a retrieval pipeline for repo-level repair.
- [Paper](https://aclanthology.org/2025.findings-acl.62.pdf)

---

## 7. CodeQL + LLM Integration

**CORE: Resolving Code Quality Issues using LLMs**
- ACM, 2024-2025
- Uses CodeQL to identify code quality issues, then applies LLMs to generate fixes, filtering suggestions that fail original CodeQL rules. Achieves 88.81% success on Python files passing CodeQL checks.
- **Why relevant:** Uses a static analysis tool (CodeQL) to both identify and validate repair context -- a pipeline the authors should compare against.
- [Paper](https://dl.acm.org/doi/pdf/10.1145/3643762)

**CQLLM: A Framework for Generating CodeQL Security Vulnerability Detection Code Based on LLM**
- Applied Sciences, January 2026
- Uses LLMs to generate CodeQL queries for vulnerability detection, addressing CodeQL's high barrier to entry.
- [Paper](https://www.mdpi.com/2076-3417/16/1/517)

**Guiding AI to Fix Its Own Flaws: LLM-Driven Secure Code Generation with CodeQL Feedback**
- arXiv:2506.23034, 2025
- Feeds CodeQL feedback and contextual information to GPT-4o for post-hoc vulnerability repair.
- [Paper](https://arxiv.org/abs/2506.23034)

---

## 8. Surveys

**A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications**
- arXiv:2506.23749, June 2025; published in TOSEM 2026
- Covers 63 systems across four paradigms. Categorizes analysis-augmented generation into failing-test evidence, semantics-aware slices, and execution traces.
- [Paper](https://arxiv.org/abs/2506.23749)

**Towards an Understanding of Context Utilization in Code Intelligence**
- arXiv:2504.08734, April 2025
- Studies how LLMs utilize different types of context (AST, data flow, dependency graphs) for code tasks.
- [Paper](https://arxiv.org/abs/2504.08734)

---

## Summary of Coverage Gaps the Authors Should Address

The most critical papers to cite and differentiate from are:

1. **ARISE** (May 2026) -- uses def-use edges in a repo-level graph for agentic repair; the closest competitor.
2. **Reasoning Distillation for Lightweight APR** (Jan 2026) -- distills analysis signals into a lightweight model; the closest methodological analog.
3. **LLMxCPG** (USENIX Security 2025) -- CPG-based context pruning achieving 67-91% code reduction.
4. **CodeBadger** (ICSE 2026 workshop) -- operationalizes CPG data-flow analysis for LLM code tasks.
5. **KGCompass** (March 2025) -- knowledge-graph-based context selection for repo-level repair.
6. **GREPO** (Feb 2026) -- GNN benchmark for repo-level bug localization.
7. **Appatch** (USENIX Security 2025) -- semantics-aware slicing for LLM repair.
8. **The fault localization granularity studies** (April 2026) -- empirical evidence on optimal context granularity.

agentId: a1c6187e43302749f (use SendMessage with to: 'a1c6187e43302749f' to continue this agent)
&lt;usage>total_tokens: 34727
tool_uses: 22
duration_ms: 156204&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2bca583c-2b47-4106-90f4-0d68e110037b",
  "isSidechain": false,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "type": "user",
  "uuid": "f3696073-edc5-43e8-a88d-42f236dd91ff",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper idea that distills data-flow (def-use) signals into a lightweight neural model for repository-level code repair context selection. I need to find competing or closely related work that the authors may have missed.\n\nSearch for the following using WebSearch:\n1. \"data-flow context selection code repair 2025 2026 site:arxiv.org\"\n2. \"def-use analysis neural code understanding 2025 2026\"\n3. \"code property graph context pruning LLM 2025 2026\"\n4. \"repository level fault localization graph neural 2025 2026\"\n5. \"program analysis guided code generation context 2025 2026\"\n6. Search for \"CodeQL code repair\" or \"CodeQL LLM\" to see if anyone has used CodeQL for similar purposes\n7. Search for any work combining BM25/retrieval with structural code features for code tasks\n\nReport all relevant papers you find, with titles, venues, and brief descriptions.",
    "agentId": "a1c6187e43302749f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the comprehensive landscape of competing and closely related work that the authors should consider referencing or differentiating from. I have organized the papers by thematic relevance.\n\n---\n\n## 1. Graph-Based Repository-Level Fault Localization and Repair (Most Directly Competing)\n\n**ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair**\n- arXiv:2605.03117, May 2026\n- Augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges. Exposes data-flow slicing as a first-class queryable agent primitive. Evaluated on SWE-bench Lite with Qwen2.5-Coder-32B, improving Function Recall@1 by 17 points and achieving 22.0% Pass@1.\n- **Why critical:** This paper uses def-use edges in a repository-level graph for code repair context selection -- essentially the same core idea. The authors must cite and differentiate from it.\n- [Paper](https://arxiv.org/abs/2605.03117)\n\n**KGCompass: Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs**\n- arXiv:2503.21710, March 2025\n- Builds a repository-aware knowledge graph linking issues, PRs, files, classes, and functions. Uses path-guided repair with KG-mined entity paths to augment LLMs. Achieves 45.67% on SWE-Bench-Lite. Found that 89.7% of successful fault locations require 2+ hops in the graph.\n- **Why relevant:** Uses structural code graphs for context selection in repair, though at a coarser granularity than def-use.\n- [Paper](https://arxiv.org/abs/2503.21710)\n\n**GREPO: A Benchmark for Graph Neural Networks on Repository-Level Bug Localization**\n- arXiv:2602.13921, February 2026\n- First GNN benchmark for repository-scale bug localization: 86 Python repos, 47,294 bug-fixing tasks. Extracts directory/file/class/function entities with contain, call, and inheritance relations. GNN architectures outperform IR baselines.\n- **Why relevant:** Directly benchmarks GNNs for repo-level bug localization -- the evaluation methodology is relevant even if the task framing differs.\n- [Paper](https://arxiv.org/abs/2602.13921)\n\n---\n\n## 2. Code Property Graphs + LLMs\n\n**CodeBadger: Bridging Code Property Graphs and Language Models for Program Analysis**\n- arXiv:2603.24837, March 2026; accepted at Software Vulnerability Management Workshop @ ICSE 2026\n- An MCP server integrating Joern's Code Property Graph engine with LLMs. Provides high-level tools for program slicing, taint tracking, data flow analysis, and semantic code navigation. Demonstrated discovering a buffer overflow in libtiff and patching CVE-2025-6021 in libxml2.\n- **Why relevant:** Operationalizes CPG-based data-flow analysis (including def-use) for LLM-driven code tasks, though focused on vulnerability analysis rather than distillation into a lightweight model.\n- [Paper](https://arxiv.org/abs/2603.24837)\n\n**LLMxCPG: Context-Aware Vulnerability Detection Through Code Property Graph-Guided LLMs**\n- USENIX Security 2025 (arXiv:2507.16585)\n- Integrates CPGs with LLMs for vulnerability detection. CPG-based slice construction reduces code size by 67-91% while preserving vulnerability-relevant context. Achieves 15-40% F1 improvements over SOTA.\n- **Why relevant:** Demonstrates CPG-guided context pruning for LLMs -- the pruning/selection mechanism is analogous to what a def-use distillation model would learn.\n- [Paper](https://arxiv.org/abs/2507.16585)\n\n**CodexGraph: Bridging Large Language Models and Code Repositories via Code Graph Databases**\n- NAACL 2025 (arXiv:2408.03910)\n- Integrates LLM agents with graph database interfaces. Uses static analysis to extract code graphs (MODULE, CLASS, FUNCTION nodes; CONTAINS, INHERITS, USES edges). Agents construct and execute graph queries for structure-aware context retrieval. Evaluated on CrossCodeEval, SWE-bench, and EvoCodeBench.\n- **Why relevant:** Pioneering work on graph-database-mediated code context retrieval for LLMs.\n- [Paper](https://arxiv.org/abs/2408.03910)\n\n---\n\n## 3. Fault Localization Context and Granularity for LLM Repair\n\n**A Study on the Impact of Fault Localization Granularity for Repository-Scale Code Repair Tasks**\n- arXiv:2604.00167, April 2026\n- Studies how fault localization granularity (file, function, line) affects repair under perfect FL assumptions on SWE-Bench. Finds function-level granularity yields the highest resolve rate overall, but optimal granularity is task-dependent.\n- **Why relevant:** Directly relevant to the question of what granularity of context selection is optimal for repo-level repair.\n- [Paper](https://arxiv.org/abs/2604.00167)\n\n**On the Role of Fault Localization Context for LLM-Based Program Repair**\n- arXiv:2604.05481, April 2026\n- Finds that expanding file context to approximately 6-10 relevant files improves repair, but element-level and line-level expansion can degrade performance through noise amplification.\n- **Why relevant:** Empirically characterizes the context selection problem that the proposed distillation approach aims to solve.\n- [Paper](https://arxiv.org/abs/2604.05481)\n\n**RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models**\n- arXiv:2601.18044, January 2026\n- Introduces per-candidate reasoning where the LLM explains each file/element's functionality and its causal relation to the bug symptom, then uses these explanations as ranking signals in a two-stage scheme. Evaluated on SWE-bench Verified, Lite, and Java.\n- **Why relevant:** An alternative approach to context selection for repair that uses reasoning rather than data-flow signals.\n- [Paper](https://arxiv.org/abs/2601.18044)\n\n---\n\n## 4. Semantics-Aware Slicing and Analysis-Augmented Repair\n\n**Appatch: Automated Adaptive Prompting LLMs for Real-World Software Vulnerability Patching**\n- USENIX Security 2025\n- Uses semantics-aware scoping (union slicing) to narrow code to vulnerability-relevant subsets, then applies adaptive exemplar prompting. Raised F1 from 44.9% to 57.2% on 306 real vulnerabilities.\n- **Why relevant:** Demonstrates that program slicing (a form of data-flow-guided context selection) significantly improves LLM repair, but uses it at inference time rather than distilling it into a model.\n- [Paper](https://arxiv.org/abs/2408.13597)\n\n**D4C: Aligning the Objective of LLM-based Program Repair**\n- ICSE 2025 (arXiv:2404.08877)\n- A prompting framework that replaces localize-then-repair with direct debugging. Repairs 180 bugs on Defects4J with only 10 samples per patch, surpassing SOTA by 10%.\n- **Why relevant:** Challenges the standard pipeline where data-flow context is explicitly extracted, instead letting the LLM perform implicit localization.\n- [Paper](https://github.com/CUHK-Shenzhen-SE/D4C)\n\n**CodeCorrector: Context-Aware Prompting for LLM-Based Program Repair**\n- Automated Software Engineering journal, 2025\n- Uses Chain-of-Thought to analyze test failures, select relevant context, and build context-aware repair prompts. Fixes 38 unique defects that no baseline can handle.\n- **Why relevant:** Another context-selection approach for repair, using test-failure-driven reasoning rather than data-flow analysis.\n- [Paper](https://link.springer.com/article/10.1007/s10515-025-00512-w)\n\n---\n\n## 5. Distillation for Lightweight Code Models\n\n**Reasoning Distillation for Lightweight Automated Program Repair**\n- arXiv:2601.10987, January 2026\n- Distills structured symbolic reasoning tags from a large teacher model into a CodeT5-based student for fix-type classification. Improves macro-averaged performance on rare bug categories without increasing model size.\n- **Why relevant:** The most directly comparable methodological approach -- distilling program analysis signals into a lightweight model for repair. The paper under review does the same but with data-flow signals specifically.\n- [Paper](https://arxiv.org/abs/2601.10987)\n\n---\n\n## 6. Retrieval-Augmented Code Repair (BM25 + Structural Features)\n\n**SWE-Fixer: Training Open-Source LLMs for Effective and Efficient GitHub Issue Resolution**\n- ACL Findings 2025\n- Uses a coarse-to-fine retrieval pipeline combining BM25 with a fine-tuned 7B retriever (initialized from GraphCodeBERT-style embeddings) for code file retrieval, followed by a fine-tuned 72B editor. Achieves 32.8% on SWE-Bench Verified.\n- **Why relevant:** Combines sparse retrieval (BM25) with neural structural code features in a retrieval pipeline for repo-level repair.\n- [Paper](https://aclanthology.org/2025.findings-acl.62.pdf)\n\n---\n\n## 7. CodeQL + LLM Integration\n\n**CORE: Resolving Code Quality Issues using LLMs**\n- ACM, 2024-2025\n- Uses CodeQL to identify code quality issues, then applies LLMs to generate fixes, filtering suggestions that fail original CodeQL rules. Achieves 88.81% success on Python files passing CodeQL checks.\n- **Why relevant:** Uses a static analysis tool (CodeQL) to both identify and validate repair context -- a pipeline the authors should compare against.\n- [Paper](https://dl.acm.org/doi/pdf/10.1145/3643762)\n\n**CQLLM: A Framework for Generating CodeQL Security Vulnerability Detection Code Based on LLM**\n- Applied Sciences, January 2026\n- Uses LLMs to generate CodeQL queries for vulnerability detection, addressing CodeQL's high barrier to entry.\n- [Paper](https://www.mdpi.com/2076-3417/16/1/517)\n\n**Guiding AI to Fix Its Own Flaws: LLM-Driven Secure Code Generation with CodeQL Feedback**\n- arXiv:2506.23034, 2025\n- Feeds CodeQL feedback and contextual information to GPT-4o for post-hoc vulnerability repair.\n- [Paper](https://arxiv.org/abs/2506.23034)\n\n---\n\n## 8. Surveys\n\n**A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications**\n- arXiv:2506.23749, June 2025; published in TOSEM 2026\n- Covers 63 systems across four paradigms. Categorizes analysis-augmented generation into failing-test evidence, semantics-aware slices, and execution traces.\n- [Paper](https://arxiv.org/abs/2506.23749)\n\n**Towards an Understanding of Context Utilization in Code Intelligence**\n- arXiv:2504.08734, April 2025\n- Studies how LLMs utilize different types of context (AST, data flow, dependency graphs) for code tasks.\n- [Paper](https://arxiv.org/abs/2504.08734)\n\n---\n\n## Summary of Coverage Gaps the Authors Should Address\n\nThe most critical papers to cite and differentiate from are:\n\n1. **ARISE** (May 2026) -- uses def-use edges in a repo-level graph for agentic repair; the closest competitor.\n2. **Reasoning Distillation for Lightweight APR** (Jan 2026) -- distills analysis signals into a lightweight model; the closest methodological analog.\n3. **LLMxCPG** (USENIX Security 2025) -- CPG-based context pruning achieving 67-91% code reduction.\n4. **CodeBadger** (ICSE 2026 workshop) -- operationalizes CPG data-flow analysis for LLM code tasks.\n5. **KGCompass** (March 2025) -- knowledge-graph-based context selection for repo-level repair.\n6. **GREPO** (Feb 2026) -- GNN benchmark for repo-level bug localization.\n7. **Appatch** (USENIX Security 2025) -- semantics-aware slicing for LLM repair.\n8. **The fault localization granularity studies** (April 2026) -- empirical evidence on optimal context granularity."
      }
    ],
    "totalDurationMs": 156204,
    "totalTokens": 34727,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3022,
      "cache_read_input_tokens": 28484,
      "output_tokens": 3220,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3022
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3220,
          "cache_read_input_tokens": 28484,
          "cache_creation_input_tokens": 3022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3022,
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
      "otherToolCount": 22
    }
  },
  "sourceToolAssistantUUID": "2bca583c-2b47-4106-90f4-0d68e110037b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
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
  "leafUuid": "f3696073-edc5-43e8-a88d-42f236dd91ff",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify StructFuse feasibility and competing work for EMNLP 2026 submission",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Assistant

_source line 24 · 2026-05-10T18:43:17.567Z_

Good, I've gathered substantial data. Now let me do a few more targeted searches to complete my review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3696073-edc5-43e8-a88d-42f236dd91ff",
  "isSidechain": false,
  "requestId": "req_011CauP4DVhPYpfRR7HqEYGA",
  "type": "assistant",
  "uuid": "142fede6-7be3-48f4-9ee2-15b00d840419",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ay9BUmRNybQbHf5WHnrMco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1772,
      "cache_creation_input_tokens": 7683,
      "cache_read_input_tokens": 30026,
      "output_tokens": 894,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1772,
          "output_tokens": 894,
          "cache_read_input_tokens": 30026,
          "cache_creation_input_tokens": 7683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7683
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

_source line 25 · 2026-05-10T18:43:26.410Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Jqtb9yx1ggvnQ9TvFoQcZ7`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check SWE-Pruner details and Beniget",
  "prompt": "I need to verify two things:\n\n1. **SWE-Pruner (arXiv:2601.16746)**: The idea claims SWE-Pruner's LLM-labeled supervision costs \"$50-200 per labeling run\" and uses Qwen3-Coder-30B as the teacher. Verify: does SWE-Pruner actually use Qwen3-Coder-30B? What teacher model does it use? What is the actual labeling cost?\n\n2. **Beniget**: The idea proposes using Beniget as a fallback for intra-file def-use analysis in Python. Search for \"beniget python def-use analysis\" to verify: (a) Does Beniget exist and is it maintained? (b) What does it actually provide? (c) Is it suitable for def-use chain extraction from Python code?\n\n3. **CodeQL for Python def-use analysis**: Search for \"CodeQL python dataflow analysis inter-procedural\" to verify whether CodeQL actually supports inter-procedural def-use analysis for Python projects and how reliable it is.\n\nUse WebSearch and WebFetch. Report exactly what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "142fede6-7be3-48f4-9ee2-15b00d840419",
  "isSidechain": false,
  "requestId": "req_011CauP4DVhPYpfRR7HqEYGA",
  "type": "assistant",
  "uuid": "a6d08ecd-5bd9-4c3a-bd46-53e8a6aafd2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ay9BUmRNybQbHf5WHnrMco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1772,
      "cache_creation_input_tokens": 7683,
      "cache_read_input_tokens": 30026,
      "output_tokens": 894,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1772,
          "output_tokens": 894,
          "cache_read_input_tokens": 30026,
          "cache_creation_input_tokens": 7683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7683
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

_source line 26 · 2026-05-10T18:43:29.884Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JP3gzQu4rrfkGzt45Vip8a`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check EMNLP 2026 ARR deadline",
  "prompt": "Search the web for \"EMNLP 2026 ARR submission deadline\" or \"ACL Rolling Review May 2026 deadline\" to verify:\n1. Is there an ARR submission deadline on May 25, 2026 (or close to it) that feeds into EMNLP 2026?\n2. Does EMNLP 2026 have a topic area called \"NLP and Code Models\" or similar?\n3. What is the conference date for EMNLP 2026?\n\nUse WebSearch. Report what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6d08ecd-5bd9-4c3a-bd46-53e8a6aafd2e",
  "isSidechain": false,
  "requestId": "req_011CauP4DVhPYpfRR7HqEYGA",
  "type": "assistant",
  "uuid": "dc201ec9-3540-4116-ac4f-db7b4a08e0df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ay9BUmRNybQbHf5WHnrMco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1772,
      "cache_creation_input_tokens": 7683,
      "cache_read_input_tokens": 30026,
      "output_tokens": 894,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1772,
          "output_tokens": 894,
          "cache_read_input_tokens": 30026,
          "cache_creation_input_tokens": 7683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7683
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

_source line 27 · 2026-05-10T18:43:36.601Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BEtWTT8Tp7t7KhDrfcXNzC`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for concurrent distillation work for code repair",
  "prompt": "Search the web for very recent (2025-2026) work on distilling program analysis signals or structural code knowledge into lightweight models for code repair or code understanding tasks. I need to check whether the idea of \"distilling data-flow features into a neural model for code context selection\" has been done before. Search specifically for:\n\n1. \"distill program analysis code repair 2025 2026 arxiv\"\n2. \"lightweight code localization model distillation 2026\"\n3. \"data flow distillation code model 2025 2026\"\n4. \"structural code features neural context selection\"\n5. \"fusion retrieval structural code repair 2025 2026\"\n6. Search for \"Reasoning Distillation for Lightweight Automated Program Repair\" (arXiv:2601.10987) — does it exist and what does it do?\n\nReport all papers found with titles, key details, and relevance."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc201ec9-3540-4116-ac4f-db7b4a08e0df",
  "isSidechain": false,
  "requestId": "req_011CauP4DVhPYpfRR7HqEYGA",
  "type": "assistant",
  "uuid": "05e615e1-841f-4591-a56f-357d5bc7c3cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ay9BUmRNybQbHf5WHnrMco",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1772,
      "cache_creation_input_tokens": 7683,
      "cache_read_input_tokens": 30026,
      "output_tokens": 894,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1772,
          "output_tokens": 894,
          "cache_read_input_tokens": 30026,
          "cache_creation_input_tokens": 7683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7683
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

_source line 28 · 2026-05-10T18:44:18.570Z_

<details><summary>↩ Tool result · `toolu_01JP3gzQu4rrfkGzt45Vip8a`</summary>

```text
Here are the findings from the web searches:

---

**1. ARR Submission Deadline on May 25, 2026 for EMNLP 2026 -- CONFIRMED**

Yes, the ARR submission deadline for EMNLP 2026 is **May 25, 2026**. This was confirmed by the official EMNLP 2026 Twitter/X account and the call for papers page. Additional key dates in that pipeline:
- Reviewer registration deadline: May 27, 2026
- Author response / author-reviewer discussion: July 7-13, 2026
- Meta reviews released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Notification of acceptance: August 20, 2026

One notable detail: since EMNLP 2026 and AACL share the same ARR May cycle, authors must explicitly select a target conference at submission time, and that choice is binding.

**2. "NLP and Code Models" Topic Area -- CONFIRMED**

Yes, EMNLP 2026 does have a topic area called **"NLP and Code Models"** listed among its accepted topic areas in the call for main conference papers.

**3. Conference Date for EMNLP 2026 -- CONFIRMED**

EMNLP 2026 is scheduled for **October 24-29, 2026**, in **Budapest, Hungary**. It will be a hybrid conference.

---

Sources:
- [Call for Main Conference Papers - EMNLP 2026](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 Homepage](https://2026.emnlp.org/)
- [EMNLP 2026 First Call for Papers (X/Twitter)](https://x.com/emnlpmeeting/status/2029508292637061462)
- [EMNLP 2026 Update on Shared ARR Cycle (X/Twitter)](https://x.com/emnlpmeeting/status/2047754845919031450)
- [ARR Dates and Venues](http://aclrollingreview.org/dates)
- [LINGUIST List - EMNLP 2026 (Hungary)](https://linguistlist.org/issues/37/972/)
- [EMNLP 2026 on callforpaper.org](https://callforpaper.org/call-for-papers-emnlp-2026)

agentId: a68e12d16edde6771 (use SendMessage with to: 'a68e12d16edde6771' to continue this agent)
&lt;usage>total_tokens: 16216
tool_uses: 7
duration_ms: 48683&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc201ec9-3540-4116-ac4f-db7b4a08e0df",
  "isSidechain": false,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "type": "user",
  "uuid": "3608f8f6-11f8-488e-bb88-3c44034e5204",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for \"EMNLP 2026 ARR submission deadline\" or \"ACL Rolling Review May 2026 deadline\" to verify:\n1. Is there an ARR submission deadline on May 25, 2026 (or close to it) that feeds into EMNLP 2026?\n2. Does EMNLP 2026 have a topic area called \"NLP and Code Models\" or similar?\n3. What is the conference date for EMNLP 2026?\n\nUse WebSearch. Report what you find.",
    "agentId": "a68e12d16edde6771",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings from the web searches:\n\n---\n\n**1. ARR Submission Deadline on May 25, 2026 for EMNLP 2026 -- CONFIRMED**\n\nYes, the ARR submission deadline for EMNLP 2026 is **May 25, 2026**. This was confirmed by the official EMNLP 2026 Twitter/X account and the call for papers page. Additional key dates in that pipeline:\n- Reviewer registration deadline: May 27, 2026\n- Author response / author-reviewer discussion: July 7-13, 2026\n- Meta reviews released: July 30, 2026\n- EMNLP commitment deadline: August 2, 2026\n- Notification of acceptance: August 20, 2026\n\nOne notable detail: since EMNLP 2026 and AACL share the same ARR May cycle, authors must explicitly select a target conference at submission time, and that choice is binding.\n\n**2. \"NLP and Code Models\" Topic Area -- CONFIRMED**\n\nYes, EMNLP 2026 does have a topic area called **\"NLP and Code Models\"** listed among its accepted topic areas in the call for main conference papers.\n\n**3. Conference Date for EMNLP 2026 -- CONFIRMED**\n\nEMNLP 2026 is scheduled for **October 24-29, 2026**, in **Budapest, Hungary**. It will be a hybrid conference.\n\n---\n\nSources:\n- [Call for Main Conference Papers - EMNLP 2026](https://2026.emnlp.org/calls/main_conference_papers/)\n- [EMNLP 2026 Homepage](https://2026.emnlp.org/)\n- [EMNLP 2026 First Call for Papers (X/Twitter)](https://x.com/emnlpmeeting/status/2029508292637061462)\n- [EMNLP 2026 Update on Shared ARR Cycle (X/Twitter)](https://x.com/emnlpmeeting/status/2047754845919031450)\n- [ARR Dates and Venues](http://aclrollingreview.org/dates)\n- [LINGUIST List - EMNLP 2026 (Hungary)](https://linguistlist.org/issues/37/972/)\n- [EMNLP 2026 on callforpaper.org](https://callforpaper.org/call-for-papers-emnlp-2026)"
      }
    ],
    "totalDurationMs": 48683,
    "totalTokens": 16216,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1800,
      "cache_read_input_tokens": 13806,
      "output_tokens": 609,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1800
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 609,
          "cache_read_input_tokens": 13806,
          "cache_creation_input_tokens": 1800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1800,
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
  "sourceToolAssistantUUID": "dc201ec9-3540-4116-ac4f-db7b4a08e0df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T18:45:29.313Z_

<details><summary>↩ Tool result · `toolu_01BEtWTT8Tp7t7KhDrfcXNzC`</summary>

```text
Here is my comprehensive report of all findings.

---

## Literature Search Results: Distilling Program Analysis Signals into Lightweight Models for Code Repair/Understanding

### Summary Assessment

The specific idea of **"distilling data-flow features into a neural model for code context selection"** has NOT been done exactly as described, but several closely related threads exist. The novelty gap is real but narrow -- multiple recent works touch adjacent points in this design space. Below are all relevant papers found, organized by relevance.

---

### TIER 1: Highly Relevant Papers (directly overlap with your idea)

**1. "Reasoning Distillation for Lightweight Automated Program Repair" (arXiv:2601.10987, January 2026)**
- Authors: Aanand Balasubramanian, Sashank Silwal
- **This paper exists and is confirmed.** It distills *symbolic reasoning tags* (not data-flow features specifically) from a large teacher model into a CodeT5-based student model for fix-type classification. The reasoning traces capture "high-level causal properties of bugs" -- conceptually adjacent to data-flow reasoning. Evaluated on IntroClass benchmark.
- **Key difference from your idea:** Their distillation target is symbolic *reasoning traces about bug causality*, not data-flow graph features. They address fix-type classification, not context selection/localization.
- **Relevance: HIGH** -- closest existing work to your concept, but does not use data-flow features and does not address context selection.

**2. KNOD: "Domain Knowledge Distilled Tree Decoder for Automated Program Repair" (arXiv:2302.01857, ICSE 2023)**
- Authors: Nan Jiang, Thibaud Lutellier, Yiling Lou, Lin Tan, Dan Goldwasser, Xiangyu Zhang
- Distills *syntactic and semantic domain rules* (AST structure rules, type constraints) into a tree decoder for patch generation via teacher-student distributions.
- **Key difference:** Distills structural *syntax/semantics rules* into the decoder, not data-flow features. Does not address context selection -- focuses on patch generation.
- **Relevance: HIGH** -- proves the concept of distilling structural program knowledge into a neural model for APR, but in a different part of the pipeline (generation, not localization/context selection).

**3. "An Empirical Study of Knowledge Distillation for Code Understanding Tasks" (arXiv:2508.15423, August 2025, to appear at ICSE 2026)**
- Authors: Ruiqi Wang, Zezhou Yang, Cuiyun Gao, Xin Xia, Qing Liao
- Systematic study of logit-based and feature-based KD across 8 student models and 2 teacher PLMs for code understanding tasks.
- **Key difference:** Studies generic KD (logit/feature-based) for code comprehension, NOT distillation of program-analysis signals specifically. Does not incorporate data-flow features as the distillation source.
- **Relevance: MEDIUM-HIGH** -- establishes that KD works for code understanding but does not investigate program-analysis-derived features as the knowledge source.

---

### TIER 2: Related Papers (overlap on one dimension)

**4. SODA: "Smaller but Better: Self-Paced Knowledge Distillation for Lightweight yet Effective LCMs" (FSE 2025)**
- Distills programming capabilities from large teacher LCMs to ~7B student models using self-paced curriculum. SodaCoder-DS-6.7B outperforms ChatGPT on Pass@1 across 7 languages.
- **Key difference:** Generic code-generation distillation; no program-analysis signals, no context selection.
- **Relevance: MEDIUM** -- relevant as a distillation-for-code baseline, but orthogonal to your structural/data-flow angle.

**5. DistiLRR: "Transferring Code Repair for Low-Resource Programming Languages" (arXiv:2406.14867, June 2024)**
- Authors: Kyle Wong et al.
- Transfers reasoning and code generation ability from teacher to student for code repair on low-resource languages (Perl, Go, Swift). Finds weak correlation between reasoning ability and code correction ability.
- **Key difference:** Transfers general reasoning/generation capability, not program-analysis features. Cross-language transfer focus.
- **Relevance: MEDIUM**

**6. RGFL: "Reasoning Guided Fault Localization for Automated Program Repair" (arXiv:2601.18044, January 2026)**
- Hierarchical reasoning module that generates structured bug-specific explanations for candidate files/elements, using them as ranking signals. On SWE-bench Verified: file-level Hit@1 from 71.4% to 85%.
- **Key difference:** Uses LLM reasoning for localization (not a distilled lightweight model). No data-flow distillation; the "reasoning" is generated on-the-fly by large LLMs.
- **Relevance: MEDIUM** -- addresses context selection for repair (localization), but via large-model reasoning, not distilled lightweight models.

**7. "Enhancing Neural Code Representation with Additional Context" (arXiv:2510.12082, October 2025)**
- Authors: Huy Nguyen et al.
- Studies enriching code representations with version history and structural relationships for clone detection and summarization. CodeT5 gains +15.92% F1 on clone detection with version history context.
- **Key difference:** Augments representations with contextual signals but does not distill structural features into a lightweight model.
- **Relevance: MEDIUM** -- shows structural/contextual enrichment helps code models, but no distillation step.

**8. MoEKD: "Leveraging Mixture of Experts to Improve Knowledge Distillation for Language Models of Code" (arXiv:2603.13213, March 2026)**
- Applies Mixture of Experts to KD for CodeBERT/GraphCodeBERT on vulnerability detection. Improves predictive performance by up to 13% and adversarial robustness by up to 30%.
- **Key difference:** Distills from CodeBERT/GraphCodeBERT (which use data-flow), but the distillation itself is model-to-model, not explicitly distilling data-flow *features* as a signal. Focus is vulnerability detection, not context selection or repair.
- **Relevance: MEDIUM** -- closest to "distilling from a data-flow-aware model" but does not explicitly extract/distill data-flow features themselves.

---

### TIER 3: Background/Survey Papers

**9. "A Survey of LLM-based Automated Program Repair" (arXiv:2506.23749, June 2025)** -- Covers 63 LLM-based APR systems (Jan 2022-June 2025).

**10. "A Systematic Literature Review on Large Language Models for Automated Program Repair" (TOSEM 2026)** -- 189 papers on LLM-based APR from 2020-Sept 2025.

**11. GraphCodeBERT (arXiv:2009.08366, ICLR 2021)** -- The foundational work on pre-training code representations with data flow graphs. Not about distillation but is the upstream source for "data-flow features."

---

### Gap Analysis: What Has NOT Been Done

Based on this search, the following specific combination appears novel:

1. **Extracting data-flow features via static program analysis** (e.g., def-use chains, data dependencies)
2. **Distilling those features into a lightweight neural model** (not just using them as input to a large model)
3. **Using the distilled model for context selection/localization** in a code repair pipeline

Existing work covers:
- Distilling *reasoning traces* into repair models (paper #1)
- Distilling *syntax/semantic rules* into repair decoders (KNOD)
- Using data-flow in *pre-training* large models (GraphCodeBERT)
- Generic KD for code understanding (paper #3)
- LLM-based fault localization with reasoning (RGFL)

But nobody has combined "data-flow feature extraction -> distillation -> lightweight context selector for repair." The closest threat is the arXiv:2601.10987 paper, which distills program-analysis-flavored reasoning into a small model, but it targets fix classification rather than context selection, and uses symbolic reasoning tags rather than actual data-flow graph features.

---

Sources:
- [Reasoning Distillation for Lightweight Automated Program Repair (arXiv:2601.10987)](https://arxiv.org/abs/2601.10987)
- [KNOD: Domain Knowledge Distilled Tree Decoder for APR (arXiv:2302.01857)](https://arxiv.org/abs/2302.01857)
- [An Empirical Study of Knowledge Distillation for Code Understanding Tasks (arXiv:2508.15423)](https://arxiv.org/abs/2508.15423)
- [SODA: Self-Paced Knowledge Distillation for Lightweight LCMs (FSE 2025)](https://dl.acm.org/doi/10.1145/3729405)
- [DistiLRR: Transferring Code Repair for Low-Resource Languages (arXiv:2406.14867)](https://arxiv.org/abs/2406.14867)
- [RGFL: Reasoning Guided Fault Localization (arXiv:2601.18044)](https://arxiv.org/abs/2601.18044)
- [Enhancing Neural Code Representation with Additional Context (arXiv:2510.12082)](https://arxiv.org/abs/2510.12082)
- [MoEKD: Mixture of Experts Knowledge Distillation for Code Models (arXiv:2603.13213)](https://arxiv.org/html/2603.13213)
- [A Survey of LLM-based APR (arXiv:2506.23749)](https://arxiv.org/html/2506.23749v1)
- [Systematic Literature Review on LLMs for APR (TOSEM 2026)](https://github.com/iSEngLab/AwesomeLLM4APR)
- [GraphCodeBERT (arXiv:2009.08366)](https://arxiv.org/abs/2009.08366)

agentId: ac29145168a016e57 (use SendMessage with to: 'ac29145168a016e57' to continue this agent)
&lt;usage>total_tokens: 27615
tool_uses: 16
duration_ms: 112705&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05e615e1-841f-4591-a56f-357d5bc7c3cf",
  "isSidechain": false,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "type": "user",
  "uuid": "b57ac172-df31-49b4-9d1a-31e48c7de31d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for very recent (2025-2026) work on distilling program analysis signals or structural code knowledge into lightweight models for code repair or code understanding tasks. I need to check whether the idea of \"distilling data-flow features into a neural model for code context selection\" has been done before. Search specifically for:\n\n1. \"distill program analysis code repair 2025 2026 arxiv\"\n2. \"lightweight code localization model distillation 2026\"\n3. \"data flow distillation code model 2025 2026\"\n4. \"structural code features neural context selection\"\n5. \"fusion retrieval structural code repair 2025 2026\"\n6. Search for \"Reasoning Distillation for Lightweight Automated Program Repair\" (arXiv:2601.10987) — does it exist and what does it do?\n\nReport all papers found with titles, key details, and relevance.",
    "agentId": "ac29145168a016e57",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my comprehensive report of all findings.\n\n---\n\n## Literature Search Results: Distilling Program Analysis Signals into Lightweight Models for Code Repair/Understanding\n\n### Summary Assessment\n\nThe specific idea of **\"distilling data-flow features into a neural model for code context selection\"** has NOT been done exactly as described, but several closely related threads exist. The novelty gap is real but narrow -- multiple recent works touch adjacent points in this design space. Below are all relevant papers found, organized by relevance.\n\n---\n\n### TIER 1: Highly Relevant Papers (directly overlap with your idea)\n\n**1. \"Reasoning Distillation for Lightweight Automated Program Repair\" (arXiv:2601.10987, January 2026)**\n- Authors: Aanand Balasubramanian, Sashank Silwal\n- **This paper exists and is confirmed.** It distills *symbolic reasoning tags* (not data-flow features specifically) from a large teacher model into a CodeT5-based student model for fix-type classification. The reasoning traces capture \"high-level causal properties of bugs\" -- conceptually adjacent to data-flow reasoning. Evaluated on IntroClass benchmark.\n- **Key difference from your idea:** Their distillation target is symbolic *reasoning traces about bug causality*, not data-flow graph features. They address fix-type classification, not context selection/localization.\n- **Relevance: HIGH** -- closest existing work to your concept, but does not use data-flow features and does not address context selection.\n\n**2. KNOD: \"Domain Knowledge Distilled Tree Decoder for Automated Program Repair\" (arXiv:2302.01857, ICSE 2023)**\n- Authors: Nan Jiang, Thibaud Lutellier, Yiling Lou, Lin Tan, Dan Goldwasser, Xiangyu Zhang\n- Distills *syntactic and semantic domain rules* (AST structure rules, type constraints) into a tree decoder for patch generation via teacher-student distributions.\n- **Key difference:** Distills structural *syntax/semantics rules* into the decoder, not data-flow features. Does not address context selection -- focuses on patch generation.\n- **Relevance: HIGH** -- proves the concept of distilling structural program knowledge into a neural model for APR, but in a different part of the pipeline (generation, not localization/context selection).\n\n**3. \"An Empirical Study of Knowledge Distillation for Code Understanding Tasks\" (arXiv:2508.15423, August 2025, to appear at ICSE 2026)**\n- Authors: Ruiqi Wang, Zezhou Yang, Cuiyun Gao, Xin Xia, Qing Liao\n- Systematic study of logit-based and feature-based KD across 8 student models and 2 teacher PLMs for code understanding tasks.\n- **Key difference:** Studies generic KD (logit/feature-based) for code comprehension, NOT distillation of program-analysis signals specifically. Does not incorporate data-flow features as the distillation source.\n- **Relevance: MEDIUM-HIGH** -- establishes that KD works for code understanding but does not investigate program-analysis-derived features as the knowledge source.\n\n---\n\n### TIER 2: Related Papers (overlap on one dimension)\n\n**4. SODA: \"Smaller but Better: Self-Paced Knowledge Distillation for Lightweight yet Effective LCMs\" (FSE 2025)**\n- Distills programming capabilities from large teacher LCMs to ~7B student models using self-paced curriculum. SodaCoder-DS-6.7B outperforms ChatGPT on Pass@1 across 7 languages.\n- **Key difference:** Generic code-generation distillation; no program-analysis signals, no context selection.\n- **Relevance: MEDIUM** -- relevant as a distillation-for-code baseline, but orthogonal to your structural/data-flow angle.\n\n**5. DistiLRR: \"Transferring Code Repair for Low-Resource Programming Languages\" (arXiv:2406.14867, June 2024)**\n- Authors: Kyle Wong et al.\n- Transfers reasoning and code generation ability from teacher to student for code repair on low-resource languages (Perl, Go, Swift). Finds weak correlation between reasoning ability and code correction ability.\n- **Key difference:** Transfers general reasoning/generation capability, not program-analysis features. Cross-language transfer focus.\n- **Relevance: MEDIUM**\n\n**6. RGFL: \"Reasoning Guided Fault Localization for Automated Program Repair\" (arXiv:2601.18044, January 2026)**\n- Hierarchical reasoning module that generates structured bug-specific explanations for candidate files/elements, using them as ranking signals. On SWE-bench Verified: file-level Hit@1 from 71.4% to 85%.\n- **Key difference:** Uses LLM reasoning for localization (not a distilled lightweight model). No data-flow distillation; the \"reasoning\" is generated on-the-fly by large LLMs.\n- **Relevance: MEDIUM** -- addresses context selection for repair (localization), but via large-model reasoning, not distilled lightweight models.\n\n**7. \"Enhancing Neural Code Representation with Additional Context\" (arXiv:2510.12082, October 2025)**\n- Authors: Huy Nguyen et al.\n- Studies enriching code representations with version history and structural relationships for clone detection and summarization. CodeT5 gains +15.92% F1 on clone detection with version history context.\n- **Key difference:** Augments representations with contextual signals but does not distill structural features into a lightweight model.\n- **Relevance: MEDIUM** -- shows structural/contextual enrichment helps code models, but no distillation step.\n\n**8. MoEKD: \"Leveraging Mixture of Experts to Improve Knowledge Distillation for Language Models of Code\" (arXiv:2603.13213, March 2026)**\n- Applies Mixture of Experts to KD for CodeBERT/GraphCodeBERT on vulnerability detection. Improves predictive performance by up to 13% and adversarial robustness by up to 30%.\n- **Key difference:** Distills from CodeBERT/GraphCodeBERT (which use data-flow), but the distillation itself is model-to-model, not explicitly distilling data-flow *features* as a signal. Focus is vulnerability detection, not context selection or repair.\n- **Relevance: MEDIUM** -- closest to \"distilling from a data-flow-aware model\" but does not explicitly extract/distill data-flow features themselves.\n\n---\n\n### TIER 3: Background/Survey Papers\n\n**9. \"A Survey of LLM-based Automated Program Repair\" (arXiv:2506.23749, June 2025)** -- Covers 63 LLM-based APR systems (Jan 2022-June 2025).\n\n**10. \"A Systematic Literature Review on Large Language Models for Automated Program Repair\" (TOSEM 2026)** -- 189 papers on LLM-based APR from 2020-Sept 2025.\n\n**11. GraphCodeBERT (arXiv:2009.08366, ICLR 2021)** -- The foundational work on pre-training code representations with data flow graphs. Not about distillation but is the upstream source for \"data-flow features.\"\n\n---\n\n### Gap Analysis: What Has NOT Been Done\n\nBased on this search, the following specific combination appears novel:\n\n1. **Extracting data-flow features via static program analysis** (e.g., def-use chains, data dependencies)\n2. **Distilling those features into a lightweight neural model** (not just using them as input to a large model)\n3. **Using the distilled model for context selection/localization** in a code repair pipeline\n\nExisting work covers:\n- Distilling *reasoning traces* into repair models (paper #1)\n- Distilling *syntax/semantic rules* into repair decoders (KNOD)\n- Using data-flow in *pre-training* large models (GraphCodeBERT)\n- Generic KD for code understanding (paper #3)\n- LLM-based fault localization with reasoning (RGFL)\n\nBut nobody has combined \"data-flow feature extraction -> distillation -> lightweight context selector for repair.\" The closest threat is the arXiv:2601.10987 paper, which distills program-analysis-flavored reasoning into a small model, but it targets fix classification rather than context selection, and uses symbolic reasoning tags rather than actual data-flow graph features.\n\n---\n\nSources:\n- [Reasoning Distillation for Lightweight Automated Program Repair (arXiv:2601.10987)](https://arxiv.org/abs/2601.10987)\n- [KNOD: Domain Knowledge Distilled Tree Decoder for APR (arXiv:2302.01857)](https://arxiv.org/abs/2302.01857)\n- [An Empirical Study of Knowledge Distillation for Code Understanding Tasks (arXiv:2508.15423)](https://arxiv.org/abs/2508.15423)\n- [SODA: Self-Paced Knowledge Distillation for Lightweight LCMs (FSE 2025)](https://dl.acm.org/doi/10.1145/3729405)\n- [DistiLRR: Transferring Code Repair for Low-Resource Languages (arXiv:2406.14867)](https://arxiv.org/abs/2406.14867)\n- [RGFL: Reasoning Guided Fault Localization (arXiv:2601.18044)](https://arxiv.org/abs/2601.18044)\n- [Enhancing Neural Code Representation with Additional Context (arXiv:2510.12082)](https://arxiv.org/abs/2510.12082)\n- [MoEKD: Mixture of Experts Knowledge Distillation for Code Models (arXiv:2603.13213)](https://arxiv.org/html/2603.13213)\n- [A Survey of LLM-based APR (arXiv:2506.23749)](https://arxiv.org/html/2506.23749v1)\n- [Systematic Literature Review on LLMs for APR (TOSEM 2026)](https://github.com/iSEngLab/AwesomeLLM4APR)\n- [GraphCodeBERT (arXiv:2009.08366)](https://arxiv.org/abs/2009.08366)"
      }
    ],
    "totalDurationMs": 112705,
    "totalTokens": 27615,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 968,
      "cache_creation_input_tokens": 4097,
      "cache_read_input_tokens": 20040,
      "output_tokens": 2510,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4097
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 968,
          "output_tokens": 2510,
          "cache_read_input_tokens": 20040,
          "cache_creation_input_tokens": 4097,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4097,
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
  "sourceToolAssistantUUID": "05e615e1-841f-4591-a56f-357d5bc7c3cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "b57ac172-df31-49b4-9d1a-31e48c7de31d",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify StructFuse feasibility and competing work for EMNLP 2026 submission",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Tool result

_source line 32 · 2026-05-10T18:45:46.243Z_

<details><summary>↩ Tool result · `toolu_01Jqtb9yx1ggvnQ9TvFoQcZ7`</summary>

```text
Now I have all the information needed. Let me compile the findings.

Here are my findings for all three verification tasks:

---

## 1. SWE-Pruner (arXiv:2601.16746) -- Teacher Model and Labeling Cost

**Teacher model -- CONFIRMED as Qwen3-Coder-30B (with nuance):**
The paper does use **Qwen3-Coder-30B-A3B-Instruct** as its teacher LLM. The full paper text states it is used to "synthesize task-oriented queries that target specific functional subsets of each snippet." Additionally, the paper uses **Qwen3-Next-80B-A3B-Thinking** as an LLM-as-a-Judge filter for quality control. Both are real, publicly available models from Alibaba's Qwen team (available on Hugging Face).

Note: The name "Qwen3-Coder-30B" is slightly imprecise. The actual model is **Qwen3-Coder-30B-A3B-Instruct**, which is a 30.5B-parameter Mixture-of-Experts model that only activates ~3B parameters per forward pass (hence "A3B"). This is an important distinction -- it is a much more lightweight model at inference time than a dense 30B model.

**Labeling cost -- NOT VERIFIED; likely fabricated in the idea:**
The paper contains **no mention of "$50-200 per labeling run"** or any dollar figure for the labeling process. I checked the full HTML paper on arxiv, the GitHub repository (`github.com/Ayanami1314/swe-pruner`), and multiple search queries. The paper describes generating 200,000 initial snippets from GitHub and producing 61,184 high-quality training samples, but discloses no cost figure. The "$50-200 per labeling run" claim appears to be fabricated or speculative -- it is not sourced from the paper.

**Training process:** The paper uses a teacher-student paradigm: sample code from GitHub, use the teacher LLM to synthesize task-oriented queries and generate training quadruplets `(q, C, M, S)` where `M` is a binary line-level mask, then filter with the LLM-as-a-Judge. The 0.6B-parameter neural skimmer is then trained on these 61K samples.

---

## 2. Beniget -- Python Def-Use Analysis

**(a) Does Beniget exist and is it maintained? YES.**
- It is a real, actively maintained Python package: [PyPI page](https://pypi.org/project/beniget/), [GitHub](https://github.com/serge-sans-paille/beniget)
- Latest version: **0.5.0**, released **November 29, 2025**
- Requires Python >= 3.6
- 82 GitHub stars, 22 forks, 143 commits
- Author: Serge Guelton (serge-sans-paille), who also created the Pythran Python-to-C++ compiler
- Available in Fedora packages, conda, and PyPI

**(b) What does it actually provide?**
- Beniget provides **def-use chains** (mapping each definition to its uses) and **use-def chains** (mapping each use to its possible definitions), plus an **Ancestors** analysis (mapping nodes to enclosing nodes)
- It works by analyzing Python ASTs (using either the `gast` cross-version AST library or standard library `ast`)
- It computes a static over-approximation of global and local definitions inside Python modules, classes, and functions
- Practical uses include: detecting unused imports, finding decorated functions, computing captured identifiers in closures

**(c) Is it suitable for def-use chain extraction from Python code? YES, with caveats.**
- It is purpose-built for exactly this task and is well-suited for **intra-file** analysis
- Known limitations (acknowledged by the author):
  - Dynamic Python features (`eval()`, `exec()`, `globals()` lookups) defeat the analysis
  - Star imports are handled conservatively
  - Self-attribute analysis is not an alias analysis
  - Cannot handle `self` reassignment or tuple assignments
  - It is a static over-approximation, not a precise analysis
- It does **not** do inter-file or inter-procedural analysis -- it operates at the module level

**Conclusion:** Beniget is a legitimate and suitable choice as a fallback for intra-file def-use analysis in Python.

---

## 3. CodeQL for Python Inter-Procedural Def-Use Analysis

**Does CodeQL support inter-procedural data flow for Python? YES.**
- CodeQL provides both **local (intra-procedural)** and **global (inter-procedural)** data flow analysis for Python
- The [official documentation](https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/) confirms: "Global data flow tracks data flow throughout the entire program"
- It supports taint tracking across function boundaries
- Users implement `DataFlow::ConfigSig` to define sources, sinks, and optional barriers

**Does it provide def-use chains specifically?**
- CodeQL does **not** explicitly provide traditional "def-use chains" as a named abstraction
- However, it provides **equivalent functionality** through its `Definition` class (`semmle.python.essa.Definitions`), `Variable` class hierarchy (LocalVariable, GlobalVariable), and data flow node tracking
- It tracks data "from places where data originates to places where it is used"

**How reliable is it?**
- Global analysis is explicitly noted as **"less precise than local data flow"** and requires **"significantly more time and memory"**
- The documentation recommends restricting sources to `LocalSourceNode` instances for performance
- No completeness or soundness guarantees are documented
- The modular API (replacing a deprecated legacy library) became available in CodeQL 2.13.0
- No comparative quality assessment against other languages is provided in the docs

**Practical limitations:**
- Requires CodeQL database creation for each project (heavyweight setup)
- Global analysis has performance concerns for large codebases
- Requires manual configuration of sources and sinks -- it is designed for security-oriented taint tracking, not general-purpose def-use chain extraction
- Python's dynamic nature presents fundamental challenges for any static analysis tool

**Conclusion:** CodeQL does support inter-procedural data flow analysis for Python, but it is primarily designed for security vulnerability detection (source-to-sink taint tracking), not for general-purpose def-use chain extraction. Using it for def-use analysis is possible but requires significant configuration and may be heavyweight for that purpose.

---

Sources:
- [SWE-Pruner paper (arXiv)](https://arxiv.org/abs/2601.16746)
- [SWE-Pruner full paper HTML](https://arxiv.org/html/2601.16746)
- [SWE-Pruner GitHub](https://github.com/Ayanami1314/swe-pruner)
- [Qwen3-Coder-30B-A3B-Instruct on Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
- [Qwen3-Next-80B-A3B-Thinking on Hugging Face](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking)
- [Beniget on PyPI](https://pypi.org/project/beniget/)
- [Beniget on GitHub](https://github.com/serge-sans-paille/beniget)
- [Beniget blog post: Gast, Beniget! Use-Def chains for Python Programs](https://serge-sans-paille.github.io/pythran-stories/gast-beniget-use-def-chains-for-python-programs.html)
- [Beniget documentation](https://beniget.readthedocs.io/en/latest/)
- [CodeQL: Analyzing data flow in Python](https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/)
- [CodeQL: About data flow analysis](https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/)
- [CodeQL Python Definition class](https://codeql.github.com/codeql-standard-libraries/python/Variables/Definition.qll/type.Definition$Definition.html)

agentId: a65a17dcfa6d48cd6 (use SendMessage with to: 'a65a17dcfa6d48cd6' to continue this agent)
&lt;usage>total_tokens: 24189
tool_uses: 16
duration_ms: 139829&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6d08ecd-5bd9-4c3a-bd46-53e8a6aafd2e",
  "isSidechain": false,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "type": "user",
  "uuid": "c2abdad4-709b-4977-9466-d38adae15b37",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two things:\n\n1. **SWE-Pruner (arXiv:2601.16746)**: The idea claims SWE-Pruner's LLM-labeled supervision costs \"$50-200 per labeling run\" and uses Qwen3-Coder-30B as the teacher. Verify: does SWE-Pruner actually use Qwen3-Coder-30B? What teacher model does it use? What is the actual labeling cost?\n\n2. **Beniget**: The idea proposes using Beniget as a fallback for intra-file def-use analysis in Python. Search for \"beniget python def-use analysis\" to verify: (a) Does Beniget exist and is it maintained? (b) What does it actually provide? (c) Is it suitable for def-use chain extraction from Python code?\n\n3. **CodeQL for Python def-use analysis**: Search for \"CodeQL python dataflow analysis inter-procedural\" to verify whether CodeQL actually supports inter-procedural def-use analysis for Python projects and how reliable it is.\n\nUse WebSearch and WebFetch. Report exactly what you find.",
    "agentId": "a65a17dcfa6d48cd6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Let me compile the findings.\n\nHere are my findings for all three verification tasks:\n\n---\n\n## 1. SWE-Pruner (arXiv:2601.16746) -- Teacher Model and Labeling Cost\n\n**Teacher model -- CONFIRMED as Qwen3-Coder-30B (with nuance):**\nThe paper does use **Qwen3-Coder-30B-A3B-Instruct** as its teacher LLM. The full paper text states it is used to \"synthesize task-oriented queries that target specific functional subsets of each snippet.\" Additionally, the paper uses **Qwen3-Next-80B-A3B-Thinking** as an LLM-as-a-Judge filter for quality control. Both are real, publicly available models from Alibaba's Qwen team (available on Hugging Face).\n\nNote: The name \"Qwen3-Coder-30B\" is slightly imprecise. The actual model is **Qwen3-Coder-30B-A3B-Instruct**, which is a 30.5B-parameter Mixture-of-Experts model that only activates ~3B parameters per forward pass (hence \"A3B\"). This is an important distinction -- it is a much more lightweight model at inference time than a dense 30B model.\n\n**Labeling cost -- NOT VERIFIED; likely fabricated in the idea:**\nThe paper contains **no mention of \"$50-200 per labeling run\"** or any dollar figure for the labeling process. I checked the full HTML paper on arxiv, the GitHub repository (`github.com/Ayanami1314/swe-pruner`), and multiple search queries. The paper describes generating 200,000 initial snippets from GitHub and producing 61,184 high-quality training samples, but discloses no cost figure. The \"$50-200 per labeling run\" claim appears to be fabricated or speculative -- it is not sourced from the paper.\n\n**Training process:** The paper uses a teacher-student paradigm: sample code from GitHub, use the teacher LLM to synthesize task-oriented queries and generate training quadruplets `(q, C, M, S)` where `M` is a binary line-level mask, then filter with the LLM-as-a-Judge. The 0.6B-parameter neural skimmer is then trained on these 61K samples.\n\n---\n\n## 2. Beniget -- Python Def-Use Analysis\n\n**(a) Does Beniget exist and is it maintained? YES.**\n- It is a real, actively maintained Python package: [PyPI page](https://pypi.org/project/beniget/), [GitHub](https://github.com/serge-sans-paille/beniget)\n- Latest version: **0.5.0**, released **November 29, 2025**\n- Requires Python >= 3.6\n- 82 GitHub stars, 22 forks, 143 commits\n- Author: Serge Guelton (serge-sans-paille), who also created the Pythran Python-to-C++ compiler\n- Available in Fedora packages, conda, and PyPI\n\n**(b) What does it actually provide?**\n- Beniget provides **def-use chains** (mapping each definition to its uses) and **use-def chains** (mapping each use to its possible definitions), plus an **Ancestors** analysis (mapping nodes to enclosing nodes)\n- It works by analyzing Python ASTs (using either the `gast` cross-version AST library or standard library `ast`)\n- It computes a static over-approximation of global and local definitions inside Python modules, classes, and functions\n- Practical uses include: detecting unused imports, finding decorated functions, computing captured identifiers in closures\n\n**(c) Is it suitable for def-use chain extraction from Python code? YES, with caveats.**\n- It is purpose-built for exactly this task and is well-suited for **intra-file** analysis\n- Known limitations (acknowledged by the author):\n  - Dynamic Python features (`eval()`, `exec()`, `globals()` lookups) defeat the analysis\n  - Star imports are handled conservatively\n  - Self-attribute analysis is not an alias analysis\n  - Cannot handle `self` reassignment or tuple assignments\n  - It is a static over-approximation, not a precise analysis\n- It does **not** do inter-file or inter-procedural analysis -- it operates at the module level\n\n**Conclusion:** Beniget is a legitimate and suitable choice as a fallback for intra-file def-use analysis in Python.\n\n---\n\n## 3. CodeQL for Python Inter-Procedural Def-Use Analysis\n\n**Does CodeQL support inter-procedural data flow for Python? YES.**\n- CodeQL provides both **local (intra-procedural)** and **global (inter-procedural)** data flow analysis for Python\n- The [official documentation](https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/) confirms: \"Global data flow tracks data flow throughout the entire program\"\n- It supports taint tracking across function boundaries\n- Users implement `DataFlow::ConfigSig` to define sources, sinks, and optional barriers\n\n**Does it provide def-use chains specifically?**\n- CodeQL does **not** explicitly provide traditional \"def-use chains\" as a named abstraction\n- However, it provides **equivalent functionality** through its `Definition` class (`semmle.python.essa.Definitions`), `Variable` class hierarchy (LocalVariable, GlobalVariable), and data flow node tracking\n- It tracks data \"from places where data originates to places where it is used\"\n\n**How reliable is it?**\n- Global analysis is explicitly noted as **\"less precise than local data flow\"** and requires **\"significantly more time and memory\"**\n- The documentation recommends restricting sources to `LocalSourceNode` instances for performance\n- No completeness or soundness guarantees are documented\n- The modular API (replacing a deprecated legacy library) became available in CodeQL 2.13.0\n- No comparative quality assessment against other languages is provided in the docs\n\n**Practical limitations:**\n- Requires CodeQL database creation for each project (heavyweight setup)\n- Global analysis has performance concerns for large codebases\n- Requires manual configuration of sources and sinks -- it is designed for security-oriented taint tracking, not general-purpose def-use chain extraction\n- Python's dynamic nature presents fundamental challenges for any static analysis tool\n\n**Conclusion:** CodeQL does support inter-procedural data flow analysis for Python, but it is primarily designed for security vulnerability detection (source-to-sink taint tracking), not for general-purpose def-use chain extraction. Using it for def-use analysis is possible but requires significant configuration and may be heavyweight for that purpose.\n\n---\n\nSources:\n- [SWE-Pruner paper (arXiv)](https://arxiv.org/abs/2601.16746)\n- [SWE-Pruner full paper HTML](https://arxiv.org/html/2601.16746)\n- [SWE-Pruner GitHub](https://github.com/Ayanami1314/swe-pruner)\n- [Qwen3-Coder-30B-A3B-Instruct on Hugging Face](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)\n- [Qwen3-Next-80B-A3B-Thinking on Hugging Face](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking)\n- [Beniget on PyPI](https://pypi.org/project/beniget/)\n- [Beniget on GitHub](https://github.com/serge-sans-paille/beniget)\n- [Beniget blog post: Gast, Beniget! Use-Def chains for Python Programs](https://serge-sans-paille.github.io/pythran-stories/gast-beniget-use-def-chains-for-python-programs.html)\n- [Beniget documentation](https://beniget.readthedocs.io/en/latest/)\n- [CodeQL: Analyzing data flow in Python](https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-python/)\n- [CodeQL: About data flow analysis](https://codeql.github.com/docs/writing-codeql-queries/about-data-flow-analysis/)\n- [CodeQL Python Definition class](https://codeql.github.com/codeql-standard-libraries/python/Variables/Definition.qll/type.Definition$Definition.html)"
      }
    ],
    "totalDurationMs": 139829,
    "totalTokens": 24189,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 349,
      "cache_read_input_tokens": 21772,
      "output_tokens": 2067,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 349
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2067,
          "cache_read_input_tokens": 21772,
          "cache_creation_input_tokens": 349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 349,
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
  "sourceToolAssistantUUID": "a6d08ecd-5bd9-4c3a-bd46-53e8a6aafd2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-10T18:45:46.247Z_

```json
{
  "parentUuid": "c2abdad4-709b-4977-9466-d38adae15b37",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "403c28bf-26a3-4d6c-9530-4613dbee2e1d",
  "timestamp": "2026-05-10T18:45:46.247Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 34 · 2026-05-10T18:47:20.608Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive data to conduct my review. Let me synthesize everything I've learned and assess the idea carefully.

## Key Findings from My Research

### Reference Verification
1. **ARISE (arXiv:2605.03117)** - CONFIRMED. Uses def-use edges as runtime tool calls, +17pp Function Recall@1, 4.7pp Pass@1 improvement. All claims accurate.
2. **Sliceformer (arXiv:2604.26961)** - CONFIRMED. ACL 2026, validates data-flow knowledge transfer, ~22% ExactMatch gains on Python.


3. **LocAgent (arXiv:2503.09089)** - CONFIRMED. ACL 2025, achieves 92.7% file-level accuracy using import/invocation/inheritance edges.
4. **SweRank (arXiv:2505.07849)** - CONFIRMED. Accepted at ICLR 2026, represents current state-of-the-art for text-based retrieval.
5. **SWE-Pruner (arXiv:2601.16746)** - CONFIRMED. Leverages Qwen3-Coder-30B-A3B-Instruct, a mixture-of-experts model with only 3B parameters active.
6. **Qwen3.6-27B** - CONFIRMED. Released April 22, 2026.
7. **Beniget** - CONFIRMED. Maintained tool suitable for analyzing variable definitions and uses within individual files.
8. **CodeQL Python inter-procedural** - CONFIRMED but with caveats. It does support this capability, though it's primarily designed for security taint analysis rather than general def-use tracking, and carries significant computational overhead.

The EMNLP 2026 venue details check out: ARR deadline May 25, 2026, with the "NLP and Code Models" topic area confirmed, and the conference running October 24-29 in Budapest. However, the benchmark claim about top systems scoring 42-59% on SWE-bench Pro appears outdated.

Looking at current performance metrics, Claude Mythos Preview achieves 77.8% on SWE-bench Pro, while Claude Opus 4.6 reaches 62.7% on the Lite version—both significantly higher than the cited range. I'm also noticing several recent papers on related fault localization and code analysis work that should probably be referenced: GREPO for repository-level bug detection, CodeBadger for integrating control flow graphs with language models, RGFL for reasoning-guided fault localization, and SWE-Fixer, though that last one appears to be cut off.

Now examining the novelty angle more carefully. The core contribution—combining CodeQL data-flow extraction with distillation into a 3B model for context selection during repair—does seem genuinely distinct. While prior work touches on individual pieces like ARISE's runtime def-use analysis or Sliceformer's data-flow distillation, none combines these specific techniques in this exact way for the repair task.

Checking the Round 3 issues: the venue mismatch is resolved by targeting EMNLP 2026 with the May 25 ARR deadline, timeline concerns are addressed with a 15-day manual mode, API costs are eliminated by using only open-weight Qwen, and the missing references to LocAgent, SweRank, and context compression papers have all been added and properly differentiated.

Now I'm noticing two remaining problems that need attention. The SWE-bench Pro SOTA claim citing 42-59% is significantly outdated since the frontier has moved to 77.8%. More concerning is the SWE-Pruner labeling cost claim of $50-200 per run, which doesn't appear to come from the paper itself and seems inflated—given that SWE-Pruner actually uses Qwen3-Coder-30B-A3B with only 3B active parameters, the real inference cost would be substantially lower, which undermines the argument about expensive LLM teachers.

I'm also questioning whether CodeQL can realistically handle general def-use chain extraction the way the idea assumes. CodeQL's inter-procedural analysis is really built for security taint tracking from source to sink, not arbitrary code repair contexts, so significant custom query development would likely be necessary. On the timeline front, the feasibility looks questionable—creating CodeQL databases for 128 Python repos with dependency resolution could easily take a full day even with parallelization, making the 10-hour CPU estimate seem optimistic.

The 20-30% CodeQL failure rate is acknowledged, and the total compute budget of 180 hours on H100s fits within the 200-hour limit, which is good. But the methodological contribution feels thin for a Main conference submission—the work is honest about being standard training methodology with empirical and practical contributions like showing data-flow features work without LLM teachers and that fusion outperforms either signal alone. This reads more like a solid Findings paper than Main material, since reviewers will likely want more methodological novelty beyond the data-flow-guided loss weighting. There are also some missing references to account for, like GREPO from February 2026 on GNN benchmarks for repository-level code.

I should also note that SweRank is now accepted at ICLR 2026, not just an arXiv preprint, and there's a precision issue with the teacher model—it's actually Qwen3-Coder-30B-A3B-Instruct, which is a mixture-of-experts model with only 3 billion active parameters, making the labeling cost significantly cheaper than citing the full 30B model would suggest.

For novelty, the specific combination of distilling data-flow features into a lightweight model for repair context selection is genuinely novel, though the individual components—CodeQL analysis, LoRA fine-tuning, feature fusion, BM25 retrieval—are all established techniques. The real contribution is how these signals combine and the empirical validation, which feels incremental but solid. Related work like Sliceformer and ARISE have shown data-flow can be distilled and that def-use edges help localization, so this work is connecting existing dots rather than introducing fundamentally new methodology. I'd rate this 3.5 for novelty.

On feasibility, the 15-day timeline is quite tight.  CodeQL database creation is the main bottleneck with its acknowledged 20-30% failure rate and Beniget fallback, though LoRA fine-tuning on 5K examples with a 3B model should be fast, and evaluating on SWE-bench Lite's 300 instances is manageable. The bigger concern is that CodeQL's inter-procedural analysis was designed for security, not general def-use extraction, so custom query development could easily overrun the timeline. The compute budget of 180 hours on H100s fits within the 200-hour limit, and the 500-instance SWE-bench Pro subset is doable, but CodeQL query development remains the real risk. I'm settling on 3.5 for feasibility.

The presentation is well-structured with clear stages and honest acknowledgments of limitations.

On impact though, I'm seeing a ceiling here. SWE-Pruner already demonstrates less than 1 percentage point degradation with LLM-labeled context selection, so the improvement margin is tight. The cost savings angle might not resonate with users who can already afford LLM inference, though the model-independence property is valuable. The harder benchmarks like SWE-bench Pro could show where context quality matters more, potentially lifting the impact score. Averaging across clarity, feasibility, novelty, and impact gives me 3.5, which falls short of the 4.0 threshold needed to pass. The work has progressed meaningfully but still has fundamental issues to address.

I'm leaning toward revision rather than rejection since we're only in round 4 of 10. The main problems are fixable: I need to verify or remove that unsubstantiated cost claim about SWE-Pruner labeling, update the outdated SOTA numbers for SWE-bench Pro, clarify what CodeQL query development actually entails for general def-use extraction beyond its security-focused design, and potentially reframe this toward EMNLP Findings given the empirical nature of the contribution.

After three rounds of iteration, the core idea is holding up well. The novelty sits at 3/5 — it's a solid empirical combination of existing techniques (Sliceformer's data-flow distillation, ARISE's def-use localization) applied to context selection, but the training methodology itself is standard. It's incremental but defensible for Findings, and borderline for Main.

Actually, reconsidering the novelty score — the specific fusion hasn't been done before, and using program-analysis features to replace LLM teacher labels for context selection is a meaningful insight. The approach combines CodeQL inter-procedural def-use with lexical scoring, git co-change, and import distance, then fuses them in a 3B model with data-flow-guided loss weighting. That's more than just relabeling; the loss weighting based on structural confidence adds a real methodological contribution. I'd bump this to 3.5.

Feasibility is tight at 3.5/5 but achievable.

Clarity scores well at 4/5 — the framing is honest about limitations. Impact sits at 3/5 though, since the improvement ceiling is concerning even if the cost-independence argument has some weight. That puts the average at 3.5, below the 4.0 threshold, so this needs revision.

The core fixable problems are the unverified cost claims, outdated SWE-bench numbers, the mischaracterization of SWE-Pruner's teacher as a dense 30B when it's actually a 3B MoE, vague CodeQL specifications, and a narrow impact argument that needs strengthening.

I'm also noticing some missing citations like SWE-Fixer, GREPO, and Reasoning Distillation that should be included. Now I'll draft the review with specific feedback to push this above 4.0.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "403c28bf-26a3-4d6c-9530-4613dbee2e1d",
  "isSidechain": false,
  "requestId": "req_011CauPFQEAnePdeXjsHcdCM",
  "type": "assistant",
  "uuid": "98c64307-d73e-4d3e-ae89-a104bd70c895",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1eo6iAKvvFmyD6e3SGg5c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8250,
      "cache_read_input_tokens": 37709,
      "output_tokens": 3842,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8250,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3842,
          "cache_read_input_tokens": 37709,
          "cache_creation_input_tokens": 8250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8250
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

_source line 35 · 2026-05-10T18:47:20.741Z_

Now let me do one final targeted check on a critical claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98c64307-d73e-4d3e-ae89-a104bd70c895",
  "isSidechain": false,
  "requestId": "req_011CauPFQEAnePdeXjsHcdCM",
  "type": "assistant",
  "uuid": "4b321e95-3fec-4259-9502-d15f646a653a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1eo6iAKvvFmyD6e3SGg5c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8250,
      "cache_read_input_tokens": 37709,
      "output_tokens": 3842,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8250,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3842,
          "cache_read_input_tokens": 37709,
          "cache_creation_input_tokens": 8250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8250
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

_source line 36 · 2026-05-10T18:47:22.945Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Jq34H1U3RicsRVxd5pXn4D`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify SWE-Pruner MoE teacher cost",
  "prompt": "I need to verify the actual inference cost of Qwen3-Coder-30B-A3B-Instruct, which is a Mixture-of-Experts model with 30B total parameters but only ~3B active parameters per forward pass.\n\n1. Search for \"Qwen3-Coder-30B-A3B cost inference\" or similar to find the actual cost of running this model for inference.\n2. How does the cost compare to running a dense 27B-30B model? Since only 3B params are active, it should be much cheaper.\n3. If someone uses this model to label 61K training samples (as SWE-Pruner does), what would the approximate cost be? Is it closer to $5-10 or $50-200?\n\nThe reason this matters: a paper idea claims that SWE-Pruner's LLM labeling costs \"$50-200 per labeling run,\" which would make data-flow-based supervision a significant cost saving. But if the MoE teacher is actually very cheap (since only 3B params active), the cost argument weakens.\n\nUse WebSearch. Report what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b321e95-3fec-4259-9502-d15f646a653a",
  "isSidechain": false,
  "requestId": "req_011CauPFQEAnePdeXjsHcdCM",
  "type": "assistant",
  "uuid": "5ae2a3a1-eec0-40e5-b682-d0e6990a62e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X1eo6iAKvvFmyD6e3SGg5c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8250,
      "cache_read_input_tokens": 37709,
      "output_tokens": 3842,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8250,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3842,
          "cache_read_input_tokens": 37709,
          "cache_creation_input_tokens": 8250,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8250
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

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "5ae2a3a1-eec0-40e5-b682-d0e6990a62e6",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify StructFuse feasibility and competing work for EMNLP 2026 submission",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Tool result

_source line 39 · 2026-05-10T18:49:15.964Z_

<details><summary>↩ Tool result · `toolu_01Jq34H1U3RicsRVxd5pXn4D`</summary>

```text
Here is my analysis based on the search results:

---

## Qwen3-Coder-30B-A3B-Instruct Inference Cost Analysis

### 1. Actual API Pricing

The Qwen3-Coder-30B-A3B-Instruct model is extremely cheap to run via API:

| Provider | Input (per 1M tokens) | Output (per 1M tokens) |
|---|---|---|
| OpenRouter (cheapest) | $0.07 | $0.27 |
| Nebius | $0.10 | $0.30 |
| Alibaba Cloud (official) | $0.19 | $0.84 |

These are among the lowest prices in the LLM API market.

### 2. Comparison to Dense 27B-30B Models

Dense models of comparable total parameter size are significantly more expensive:

| Model | Input (per 1M tokens) | Output (per 1M tokens) |
|---|---|---|
| Qwen3.6-27B (dense) | $0.32 | $3.20 |
| Qwen3.5-27B (dense) | $0.195 | $1.56 |
| **Qwen3-Coder-30B-A3B (MoE)** | **$0.07** | **$0.27** |

The MoE model is roughly **3-5x cheaper on input** and **6-12x cheaper on output** compared to dense 27B models. This is exactly what you'd expect: with only 3.3B active parameters per forward pass, inference compute is comparable to running a ~3B dense model, not a 30B one. The model also runs on a single consumer GPU (fits in ~18GB VRAM at Q4 quantization).

### 3. Estimated Cost of Labeling 61K Samples (SWE-Pruner)

The SWE-Pruner paper uses Qwen3-Coder-30B-A3B-Instruct as the teacher model to generate 61,184 synthetic training samples. The labeling task involves:
- Taking code snippets sampled from GitHub
- Having the teacher LLM synthesize task-oriented queries and line-level retention labels across 9 agentic task categories

**Cost estimation:**

For code labeling tasks, a reasonable estimate is ~1,000-3,000 input tokens per sample (the code snippet + prompt) and ~200-500 output tokens per sample (the query + line-level annotations). Using moderate estimates:

- **Conservative estimate** (2,000 input + 500 output tokens per sample):
  - Input: 61K x 2,000 = 122M tokens x $0.07/1M = **$8.54**
  - Output: 61K x 500 = 30.5M tokens x $0.27/1M = **$8.24**
  - **Total: ~$17**

- **Generous estimate** (4,000 input + 1,000 output tokens per sample):
  - Input: 61K x 4,000 = 244M tokens x $0.07/1M = **$17.08**
  - Output: 61K x 1,000 = 61M tokens x $0.27/1M = **$16.47**
  - **Total: ~$34**

- **Using Alibaba's own (more expensive) API** with generous token counts:
  - Input: 244M tokens x $0.19/1M = **$46.36**
  - Output: 61M tokens x $0.84/1M = **$51.24**
  - **Total: ~$98**

**The realistic cost is in the $5-35 range** using competitive API providers, and at most ~$100 even using Alibaba's own more expensive endpoint with generous token estimates. This is nowhere near "$200."

### 4. Implications for the Cost Argument

The claim that SWE-Pruner's LLM labeling costs "$50-200 per labeling run" appears to be an overestimate, likely by a factor of 3-10x. Here is why:

- **At cheapest API pricing** (OpenRouter at $0.07/$0.27): The cost is likely **$10-35** for 61K samples.
- **At Alibaba's own pricing** ($0.19/$0.84): The cost could reach **$50-100**, but only with generous assumptions about tokens per sample.
- **The MoE architecture is the key factor**: Because only 3.3B parameters are active per forward pass, the model is priced like a small model despite having 30B total parameters. This is not a "$50-200" teacher -- it is a "$10-35" teacher at market rates.

This substantially weakens the cost-saving argument for data-flow-based supervision as an alternative to LLM labeling. If the LLM labeling cost is $10-35 (a one-time cost to generate training data), the marginal savings from avoiding LLM labeling are modest, not a major advantage.

The cost argument would only hold if the paper assumed:
1. Using a much more expensive teacher model (e.g., GPT-4 or Claude at $10-15/1M output tokens), or
2. Very long code contexts (10K+ tokens per sample), or
3. Multiple labeling passes per sample

---

Sources:
- [OpenRouter - Qwen3 Coder 30B A3B Instruct Pricing](https://openrouter.ai/qwen/qwen3-coder-30b-a3b-instruct)
- [Artificial Analysis - Qwen3 Coder 30B A3B](https://artificialanalysis.ai/models/qwen3-coder-30b-a3b-instruct)
- [Price Per Token - Qwen3 30B A3B Pricing](https://pricepertoken.com/pricing-page/model/qwen-qwen3-30b-a3b)
- [OpenRouter - Qwen3.6 27B (dense) Pricing](https://openrouter.ai/qwen/qwen3.6-27b)
- [OpenRouter - Qwen3.5 27B (dense) Pricing](https://openrouter.ai/qwen/qwen3.5-27b)
- [SWE-Pruner Paper (arXiv 2601.16746)](https://arxiv.org/html/2601.16746)
- [Qwen3 Technical Report](https://arxiv.org/html/2505.09388v1)
- [VRAM Requirements - Qwen3-Coder-30B-A3B](https://oniyoon.com/models/qwen3-coder-30b-a3b-instruct/)
- [Qwen3-30B-A3B Specifications](https://apxml.com/models/qwen3-30b-a3b)

agentId: a5375a2fae36aa637 (use SendMessage with to: 'a5375a2fae36aa637' to continue this agent)
&lt;usage>total_tokens: 24259
tool_uses: 13
duration_ms: 113016&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ae2a3a1-eec0-40e5-b682-d0e6990a62e6",
  "isSidechain": false,
  "promptId": "e60a209e-5c56-4b6e-8041-a861958aa4e3",
  "type": "user",
  "uuid": "837e6e28-1a06-46ec-b58a-e89ba873765d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify the actual inference cost of Qwen3-Coder-30B-A3B-Instruct, which is a Mixture-of-Experts model with 30B total parameters but only ~3B active parameters per forward pass.\n\n1. Search for \"Qwen3-Coder-30B-A3B cost inference\" or similar to find the actual cost of running this model for inference.\n2. How does the cost compare to running a dense 27B-30B model? Since only 3B params are active, it should be much cheaper.\n3. If someone uses this model to label 61K training samples (as SWE-Pruner does), what would the approximate cost be? Is it closer to $5-10 or $50-200?\n\nThe reason this matters: a paper idea claims that SWE-Pruner's LLM labeling costs \"$50-200 per labeling run,\" which would make data-flow-based supervision a significant cost saving. But if the MoE teacher is actually very cheap (since only 3B params active), the cost argument weakens.\n\nUse WebSearch. Report what you find.",
    "agentId": "a5375a2fae36aa637",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my analysis based on the search results:\n\n---\n\n## Qwen3-Coder-30B-A3B-Instruct Inference Cost Analysis\n\n### 1. Actual API Pricing\n\nThe Qwen3-Coder-30B-A3B-Instruct model is extremely cheap to run via API:\n\n| Provider | Input (per 1M tokens) | Output (per 1M tokens) |\n|---|---|---|\n| OpenRouter (cheapest) | $0.07 | $0.27 |\n| Nebius | $0.10 | $0.30 |\n| Alibaba Cloud (official) | $0.19 | $0.84 |\n\nThese are among the lowest prices in the LLM API market.\n\n### 2. Comparison to Dense 27B-30B Models\n\nDense models of comparable total parameter size are significantly more expensive:\n\n| Model | Input (per 1M tokens) | Output (per 1M tokens) |\n|---|---|---|\n| Qwen3.6-27B (dense) | $0.32 | $3.20 |\n| Qwen3.5-27B (dense) | $0.195 | $1.56 |\n| **Qwen3-Coder-30B-A3B (MoE)** | **$0.07** | **$0.27** |\n\nThe MoE model is roughly **3-5x cheaper on input** and **6-12x cheaper on output** compared to dense 27B models. This is exactly what you'd expect: with only 3.3B active parameters per forward pass, inference compute is comparable to running a ~3B dense model, not a 30B one. The model also runs on a single consumer GPU (fits in ~18GB VRAM at Q4 quantization).\n\n### 3. Estimated Cost of Labeling 61K Samples (SWE-Pruner)\n\nThe SWE-Pruner paper uses Qwen3-Coder-30B-A3B-Instruct as the teacher model to generate 61,184 synthetic training samples. The labeling task involves:\n- Taking code snippets sampled from GitHub\n- Having the teacher LLM synthesize task-oriented queries and line-level retention labels across 9 agentic task categories\n\n**Cost estimation:**\n\nFor code labeling tasks, a reasonable estimate is ~1,000-3,000 input tokens per sample (the code snippet + prompt) and ~200-500 output tokens per sample (the query + line-level annotations). Using moderate estimates:\n\n- **Conservative estimate** (2,000 input + 500 output tokens per sample):\n  - Input: 61K x 2,000 = 122M tokens x $0.07/1M = **$8.54**\n  - Output: 61K x 500 = 30.5M tokens x $0.27/1M = **$8.24**\n  - **Total: ~$17**\n\n- **Generous estimate** (4,000 input + 1,000 output tokens per sample):\n  - Input: 61K x 4,000 = 244M tokens x $0.07/1M = **$17.08**\n  - Output: 61K x 1,000 = 61M tokens x $0.27/1M = **$16.47**\n  - **Total: ~$34**\n\n- **Using Alibaba's own (more expensive) API** with generous token counts:\n  - Input: 244M tokens x $0.19/1M = **$46.36**\n  - Output: 61M tokens x $0.84/1M = **$51.24**\n  - **Total: ~$98**\n\n**The realistic cost is in the $5-35 range** using competitive API providers, and at most ~$100 even using Alibaba's own more expensive endpoint with generous token estimates. This is nowhere near \"$200.\"\n\n### 4. Implications for the Cost Argument\n\nThe claim that SWE-Pruner's LLM labeling costs \"$50-200 per labeling run\" appears to be an overestimate, likely by a factor of 3-10x. Here is why:\n\n- **At cheapest API pricing** (OpenRouter at $0.07/$0.27): The cost is likely **$10-35** for 61K samples.\n- **At Alibaba's own pricing** ($0.19/$0.84): The cost could reach **$50-100**, but only with generous assumptions about tokens per sample.\n- **The MoE architecture is the key factor**: Because only 3.3B parameters are active per forward pass, the model is priced like a small model despite having 30B total parameters. This is not a \"$50-200\" teacher -- it is a \"$10-35\" teacher at market rates.\n\nThis substantially weakens the cost-saving argument for data-flow-based supervision as an alternative to LLM labeling. If the LLM labeling cost is $10-35 (a one-time cost to generate training data), the marginal savings from avoiding LLM labeling are modest, not a major advantage.\n\nThe cost argument would only hold if the paper assumed:\n1. Using a much more expensive teacher model (e.g., GPT-4 or Claude at $10-15/1M output tokens), or\n2. Very long code contexts (10K+ tokens per sample), or\n3. Multiple labeling passes per sample\n\n---\n\nSources:\n- [OpenRouter - Qwen3 Coder 30B A3B Instruct Pricing](https://openrouter.ai/qwen/qwen3-coder-30b-a3b-instruct)\n- [Artificial Analysis - Qwen3 Coder 30B A3B](https://artificialanalysis.ai/models/qwen3-coder-30b-a3b-instruct)\n- [Price Per Token - Qwen3 30B A3B Pricing](https://pricepertoken.com/pricing-page/model/qwen-qwen3-30b-a3b)\n- [OpenRouter - Qwen3.6 27B (dense) Pricing](https://openrouter.ai/qwen/qwen3.6-27b)\n- [OpenRouter - Qwen3.5 27B (dense) Pricing](https://openrouter.ai/qwen/qwen3.5-27b)\n- [SWE-Pruner Paper (arXiv 2601.16746)](https://arxiv.org/html/2601.16746)\n- [Qwen3 Technical Report](https://arxiv.org/html/2505.09388v1)\n- [VRAM Requirements - Qwen3-Coder-30B-A3B](https://oniyoon.com/models/qwen3-coder-30b-a3b-instruct/)\n- [Qwen3-30B-A3B Specifications](https://apxml.com/models/qwen3-30b-a3b)"
      }
    ],
    "totalDurationMs": 113016,
    "totalTokens": 24259,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1874,
      "cache_read_input_tokens": 20704,
      "output_tokens": 1680,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1680,
          "cache_read_input_tokens": 20704,
          "cache_creation_input_tokens": 1874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1874,
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
  "sourceToolAssistantUUID": "5ae2a3a1-eec0-40e5-b682-d0e6990a62e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-10T18:50:00.901Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to complete my review. Let me synthesize everything.

## Summary of All Findings

### What Round 4 Fixed from Round 3:
1. ✅ Venue: Now targets EMNLP 2026 (ARR May 25) — confirmed correct
2. ✅ Timeline: Now 15 days — aggressive but plausible
3. ✅ API Costs: Now uses Qwen3.6-27B (open-weight, no API costs)
4. ✅ LocAgent cited and differentiated


5. ✅ SweRank cited as baseline
6. ✅ RepoBench-R added to evaluation
7. ✅ Context compression paper cited
8. ✅ Method contribution honestly framed as empirical/practical

### Remaining Issues:

**1. SWE-Pruner Labeling Cost Claim is Fabricated/Misleading**
The $50-200 per labeling run figure for SWE-Pruner doesn't appear in the original paper and seems inflated by several multiples compared to realistic costs.  The teacher model uses a sparse architecture with minimal active parameters, priced accordingly, so the actual savings from avoiding LLM labeling is probably just $10-35 one-time—not a compelling differentiator.

**2. SWE-bench Pro SOTA Claims Outdated**
The 42-59% range cited for top systems is stale given that Claude Mythos Preview now achieves 77.8%. While the lower range might still be accurate under the standardized SEAL evaluation, this needs clarification.

**3. CodeQL for General Def-Use is Not Straightforward**
Examining how CodeQL handles definition-use analysis...

CodeQL's Python capabilities are built for security taint tracking rather than general def-use extraction, so custom queries would be necessary. The idea glosses over this as simple feature extraction when it actually requires substantial query development and introduces timeline risk.

**4. SWE-Pruner Teacher is MoE (3B active), Not Dense 30B**
The framing suggests an expensive 30B teacher model, but it's actually a mixture-of-experts with only 3.3B active parameters—inference costs align with a 3B model. This undermines the narrative about expensive LLM teachers.

**5. Narrow Improvement Ceiling Not Adequately Addressed**
Looking at the performance gains on SWE-bench Verified...

the unpruned baseline is already at 70.6%, leaving less than 1 percentage point of degradation from pruning. The room for improvement through better labels is quite limited, though the argument that harder benchmarks might reveal larger gaps is reasonable but unvalidated.

**6. Missing References (Minor)**
There are several relevant papers not cited: SWE-Fixer combines retrieval approaches for repo-level repair, GREPO applies GNNs to repo localization, and there's work on distilling reasoning signals into lightweight models. Also, SweRank is an ICLR 2026 paper, not just an arXiv preprint.

**7. Method Contribution for EMNLP Main**
The training approach itself is standard, which the idea acknowledges. The empirical contribution centers on demonstrating that data-flow features effectively improve performance.

The combination of CodeQL def-use extraction, feature engineering, fusion with BM25 and SweRankEmbed, and the 3B LoRA model with data-flow-guided loss weighting is novel in how these pieces fit together. No prior work has distilled data-flow information into a lightweight model specifically for repair context selection. That said, each individual component is established—Sliceformer already showed data-flow can be distilled into neural models, and ARISE demonstrated that def-use edges help with localization. The novelty lies in the specific combination and application rather than any single technique.

The 15-day timeline is tight but achievable, though CodeQL query development for general def-use extraction poses a real risk. The Beniget fallback provides good insurance, and the compute budget of 180 hours on H100s fits within the 200-hour allocation. Qwen3.6-27B and SWE-smith data are both confirmed available. The main concerns are CodeQL database creation failures (acknowledged at 20-30%) and the time needed to develop custom queries.

The proposal is well-structured and honest about its limitations, including Python's dynamic features and the reliance on standard methodology. The differentiation from prior work is clear, though there's a fabricated claim about SWE-Pruner's cost. The impact argument around cost savings is overstated—LLM labeling isn't actually as expensive as suggested.

The model-independence and interpretability benefits are real, but the improvement ceiling on easier benchmarks is narrow. Harder benchmarks might show more value, though that's speculative. The practical contribution of the CodeQL-to-features-to-3B pipeline does have genuine community value.

Averaging the scores gives 3.5, which falls short of the 4.0 threshold. The core issues holding it back are the weakened cost motivation, fabricated figures, outdated SOTA claims, thin methodological contribution, and limited improvement potential on standard benchmarks.

All of these are fixable with specific, actionable revisions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "837e6e28-1a06-46ec-b58a-e89ba873765d",
  "isSidechain": false,
  "requestId": "req_011CauPWrqjNcBo1YVj9Q9sW",
  "type": "assistant",
  "uuid": "12c8a9d8-79fb-463a-acfa-10028e17570f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156MdPBM1425xpEu9gC57fC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5592,
      "cache_read_input_tokens": 45959,
      "output_tokens": 3878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5592,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3878,
          "cache_read_input_tokens": 45959,
          "cache_creation_input_tokens": 5592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5592
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

_source line 41 · 2026-05-10T18:50:49.202Z_

I now have all the evidence I need. Let me synthesize my findings into the final review.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3.5, "rationale": "The specific combination (CodeQL def-use → feature fusion with BM25/SweRankEmbed → 3B LoRA model) is genuinely novel — no existing work distills data-flow into a lightweight model for repair context selection. However, each component is standard, the training methodology is explicitly acknowledged as standard, and Sliceformer (ACL 2026) already demonstrated data-flow distillation into neural models. Novelty is in the application and combination, not technique."},
    "feasibility": {"score": 3.5, "rationale": "The 15-day timeline is aggressive but structurally plausible: LoRA SFT on 5K examples takes 2-4 hours, SWE-bench Lite evaluation is manageable, and Qwen3.6-27B/SWE-smith are confirmed available. However, CodeQL's Python inter-procedural analysis is designed for security taint tracking, not general def-use extraction — custom query development adds significant unbudgeted time risk, and the 20-30% database creation failure rate for Python repos is a real concern."},
    "clarity": {"score": 4, "rationale": "Well-structured with clear stages, honest acknowledgment that the training methodology is standard, comprehensive landscape, concrete tool choices (CodeQL, Beniget, SweRankEmbed), and good differentiation from prior work. The honest framing of contributions as 'empirical and practical' is commendable. Minor deduction for the unverified SWE-Pruner cost claim."},
    "impact": {"score": 3, "rationale": "The cost-saving argument is significantly weaker than presented: SWE-Pruner's teacher (Qwen3-Coder-30B-A3B) is an MoE model with only 3B active params, making LLM labeling cost ~$10-35, not '$50-200.' Model-independence and interpretability are genuine advantages, but the improvement ceiling on easy benchmarks is narrow (<1pp on Verified). Impact depends on showing clear gains on harder benchmarks (Pro), which is speculative."}
  },
  "issues": [
    "CRITICAL: SWE-Pruner labeling cost claim '~$50-200 per labeling run' is NOT from the paper and appears fabricated. The SWE-Pruner paper provides no cost figures. My independent verification shows the teacher model (Qwen3-Coder-30B-A3B-Instruct) is an MoE with only 3.3B active parameters, priced at $0.07-0.19/1M input tokens. Labeling 61K samples realistically costs $10-35 (at cheapest API) or at most ~$100 (at Alibaba's own endpoint). This 3-10x overestimate significantly weakens the cost motivation — the savings from avoiding LLM labeling are modest, not transformative.",
    "SWE-bench Pro SOTA claim 'top systems score 42-59%' is outdated. Claude Mythos Preview scores 77.8% as of April 2026. The 42-59% range only holds under SEAL-standardized evaluation constraints. Must be corrected or qualified.",
    "CodeQL for general-purpose def-use extraction is underspecified. CodeQL's Python inter-procedural data flow API is designed for security source-to-sink taint tracking, not arbitrary def-use chain enumeration. Custom CodeQL queries (defining sources, sinks, and flow configurations) must be written to extract general def-use features. This is non-trivial engineering not reflected in the timeline. The idea should specify: (a) what CodeQL query patterns will be used, (b) whether existing security queries can be adapted, or (c) how much query development time is budgeted.",
    "SWE-Pruner teacher model mischaracterization: The idea repeatedly frames Qwen3-Coder-30B as an expensive teacher, but it is an MoE model with only 3.3B active parameters per forward pass — inference cost comparable to a 3B dense model, not a 30B one. This undermines the 'expensive LLM teacher' narrative throughout the paper. The cost argument must be reframed: the advantage is not primarily cost savings but model-independence, interpretability, and avoiding coupling to a specific teacher's biases.",
    "Missing reference: SWE-Fixer (ACL Findings 2025) combines BM25 with a fine-tuned 7B retriever (from GraphCodeBERT-style embeddings) for coarse-to-fine code file retrieval in repo-level repair, achieving 32.8% on SWE-bench Verified. This is architecturally similar (BM25 + neural retrieval fusion for context selection) and should be discussed.",
    "SweRank venue update: SweRank is accepted at ICLR 2026 (confirmed via Salesforce's ICLR 2026 accepted papers list), not just an arXiv preprint. Should be cited correctly.",
    "Method contribution remains thin for EMNLP Main. With the training methodology explicitly acknowledged as standard, and the contribution framed as empirical, this reads more like a strong Findings paper than a Main paper. Reviewers at Main will expect either: (a) a novel training objective beyond weighted cross-entropy, (b) a theoretical grounding for why data-flow signals should outperform lexical signals, or (c) a more surprising empirical result than 'fusion outperforms individual signals.'"
  ],
  "feedback": "Round 4 has made excellent progress — venue targeting, timeline, API cost elimination, and honest method framing are all fixed. The idea is now structurally sound. However, the cost motivation has a factual foundation problem that must be addressed before this can pass:\n\n1. **Rewrite the cost motivation entirely.** The '$50-200 per labeling run' claim is unverifiable and almost certainly a 3-10x overestimate. SWE-Pruner's teacher (Qwen3-Coder-30B-A3B) has only 3.3B active parameters and costs $0.07/1M input tokens — labeling 61K samples costs ~$10-35. Do NOT fabricate cost figures. Instead, reframe the advantage as: (a) **model-independence** — SWE-Pruner's labels are coupled to Qwen3-Coder's biases and selection patterns; data-flow labels are ground-truth from program analysis; (b) **zero marginal cost at scale** — adding more repos requires only running CodeQL, no LLM inference budget; (c) **interpretability** — each selection comes with a traceable data-flow path to the bug, not an opaque LLM judgment; (d) **reproducibility** — labels are deterministic given the same CodeQL database, unlike stochastic LLM outputs. The cost angle is a nice-to-have, not the headline.\n\n2. **Update SWE-bench Pro SOTA.** State clearly: 'Top agent systems score 50-78% on SWE-bench Pro depending on scaffolding complexity (Claude Mythos Preview: 77.8% with custom scaffolding; SEAL-standardized evaluation constrains scores to ~42-58%).' This is important because higher Pro scores narrow the improvement ceiling from context selection.\n\n3. **Specify CodeQL query strategy concretely.** State: 'We configure CodeQL's Python taint tracking API with broad source/sink definitions (all function parameters as sources, all variable reads as sinks) to approximate general def-use chains. Where this overproduces flows, we filter by graph distance. We budget 1 day specifically for CodeQL query development and validation on 10 pilot repos before scaling.' This addresses the practical risk.\n\n4. **Correct the SWE-Pruner teacher characterization.** Note that Qwen3-Coder-30B-A3B is an MoE model with 3.3B active parameters. Do not frame it as an expensive 30B teacher.\n\n5. **Add SWE-Fixer (ACL Findings 2025) to related work** — it is the most architecturally similar prior work (BM25 + neural retriever fusion for repo-level repair context selection). Differentiate: SWE-Fixer uses learned embeddings without structural program analysis features.\n\n6. **Explicitly target EMNLP Findings alongside Main.** Given the empirical contribution type, dual-targeting de-risks rejection. The paper's strength is practical value (cheap, fast, interpretable, model-independent context selector), which Findings rewards.\n\n7. **Strengthen the method contribution.** Consider adding one of: (a) a contrastive learning objective where data-flow-connected pairs are pulled together in the embedding space, distinct from standard cross-entropy; (b) a two-stage cascade (coarse file selection via BM25 + data-flow features → fine-grained function ranking via the 3B model), which adds architectural novelty; or (c) a data-flow-aware hard negative mining strategy where training negatives are selected as files that are lexically similar but structurally disconnected from the bug. Any of these would elevate the method contribution above 'SFT with different labels.'",
  "reason": "Solid idea with genuine novelty in the combination, but the cost motivation rests on fabricated/inflated figures (SWE-Pruner labeling costs $10-35, not $50-200), SOTA claims are outdated, and the method contribution remains thin for Main — needs reframed motivation and one methodological innovation to clear the 4.0 threshold."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12c8a9d8-79fb-463a-acfa-10028e17570f",
  "isSidechain": false,
  "requestId": "req_011CauPWrqjNcBo1YVj9Q9sW",
  "type": "assistant",
  "uuid": "8e52cdb1-afe1-4175-af63-40b978e2ce73",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0156MdPBM1425xpEu9gC57fC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5592,
      "cache_read_input_tokens": 45959,
      "output_tokens": 3878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5592,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3878,
          "cache_read_input_tokens": 45959,
          "cache_creation_input_tokens": 5592,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5592
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "8e52cdb1-afe1-4175-af63-40b978e2ce73",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify StructFuse feasibility and competing work for EMNLP 2026 submission",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-10 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "8e52cdb1-afe1-4175-af63-40b978e2ce73",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify StructFuse feasibility and competing work for EMNLP 2026 submission",
  "sessionId": "9fa949bb-b495-4f49-a9fb-ebb5d0f2bc3b"
}
```

---
