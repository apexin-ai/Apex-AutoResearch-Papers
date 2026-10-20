# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-09 (UTC).** Your job: indep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/d1d1e179-387b-4b03-977f-20bfd6c5f449.jsonl`
- **Structured JSON:** [`775e2b9f7684c0f15bcd.json`](../../sessions/77/775e2b9f7684c0f15bcd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-09T20:15:07.648Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-09T20:15:07.648Z",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-09 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: LLM Agents.\n\nDirection: LLM Agents — planning algorithms, memory architectures, tool use, multi-agent coordination, agent training (SFT/RL), self-correction in agentic loops, environment feedback exploitation.\n\nContribution type: METHOD ONLY. Must propose a concrete new algorithm, training procedure, or inference-time mechanism. Reject pure benchmark / dataset / analysis ideas. Method + analysis OK if analysis validates the method.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total (baselines + method + ablations). Show the math.\n2. Time: ≤16 days. Build on existing OSS agent codebases (AutoGen, LangGraph, OpenManus, etc.) — no from-scratch systems.\n3. Eval: existing benchmarks only — AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench.\n\nAvoid: generic ReAct variants, plain tool retrieval, naive memory summarization. Look for: agent training with minimal RL budget, structured planning beyond flat CoT, multi-agent communication protocols, agent self-verification mechanisms.\n\nTag: direction=agent, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-09?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 9/10)\n{\n  \"title\": \"CascadeWatch: Cascade-Onset Detection with Targeted Rollback for Long-Horizon Agent Tasks\",\n  \"core_problem\": \"In long-horizon agent tasks, individual early-step errors produce cascading downstream failures that grow exponentially more costly to correct with each additional step. The core question is whether a lightweight trained monitor can prospectively detect cascade onset—predicting failure propagation before it fully manifests—to trigger targeted rollback rather than reactive reflection or full replanning. The challenge is not simply detecting failure: the Intervention Paradox (arXiv 2602.03338) establishes that generic critics with AUROC 0.94 cause up to 26 percentage point performance degradation by triggering on non-cascade failures that the agent would have self-corrected. The disruption-recovery tradeoff (Δ Success = p·r − (1−p)·d) only favors intervention on high-failure benchmarks like ALFWorld; it degrades GAIA and HotPotQA even with accurate critics. The solution is not a better generic critic but a cascade-specific one: targeting only the recoverability-degrading prefix patterns that precede confirmed cascades—detectable via recoverability proxy signals—to achieve the high precision (low d) and focused recall (high p conditional on cascade-onset) that shifts the threshold in favor of intervention. A natural alternative early-warning signal is canonical path deviation (arXiv 2602.19008): measuring Jaccard similarity of tool invocations against the convergent set shared across successful runs. This signal is empirically validated but requires aggregating tool invocation sequences from multiple successful runs per task, making it unavailable for novel tasks or low-success-rate settings. CascadeWatch uses ERR Efficiency Score recoverability deltas (arXiv 2601.22352) approximated as running prefix statistics over the agent's tool-call/result sequence without reference to other runs, enabling cascade detection in the absence of precomputed canonical paths. The rollback mechanism varies by environment affordance: for text-game environments (ALFWorld), full environment-state rollback is achieved via command-replay from env.reset(); for tool-augmented environments (WebShop, GAIA), context-only rollback rewinds the agent's context window. Neither mechanism requires a non-existent API; both are acknowledged to have environment-specific costs and limitations.\",\n  \"opportunity\": \"The cascade failure pattern is now well-characterized and trainable. AgentErrorBench (arXiv 2509.25370) provides the first systematically annotated failure taxonomy across ALFWorld, WebShop, and GAIA, with expert root-cause step annotations (critical_failure_step field, annotated by ten graduate students at Cohen's κ = 0.55) identifying where cascades originate; the dataset contains 100 ALFWorld, 50 GAIA, and 50 WebShop trajectories, all of which are failure trajectories by design (failures are deliberately oversampled). Memory and reflection errors at steps 5–15 are the most common cascade initiators, crucially occurring mid-trajectory rather than at the earliest steps where the Intervention Paradox shows all regressions occur. The ERR paper (arXiv 2601.22352) formalizes recoverability as Expected Recovery Regret and derives a measurable Efficiency Score proxy, empirically validated across five benchmarks to within δ ≤ 0.05 of observed post-failure regret—establishing that step-level recoverability is observable from trajectory prefixes and thus learnable as a predictive signal. This signal applies directly to tool-augmented agents (WebShop, GAIA) where structured tool-call/result pairs provide natural Efficiency Score observables as running prefix estimates; for text-game environments (ALFWorld), where failures are cognitive planning errors rather than tool execution failures, a domain-adapted proxy (step-level game score delta) is used instead, acknowledged as a heuristic extension. Canonical Path Deviation (arXiv 2602.19008) provides independent corroboration of the self-reinforcing cascade mechanism in long-horizon tool-use tasks: each off-canonical tool invocation raises the probability that the next invocation is also off-canonical by 22.7 percentage points, confirming that cascade propagation is empirically measurable and compounding. CascadeWatch uses recoverability signals rather than canonical path adherence specifically because recoverability deltas are approximable from a single trajectory prefix, enabling deployment where canonical paths from multiple successful runs are unavailable. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) demonstrates that backtracking triggers improve GUI agent task completion on Mobile3M and Auto-UI benchmarks, but requires constructing a task-specific training dataset and fine-tuning the agent components—leaving a clear gap for an external, training-free cascade monitor that operates on any frozen agent in cognitive long-horizon tasks. The proactive detection landscape now includes TrajAD (arXiv 2602.06443) for general trajectory anomaly detection on TrajBench (a synthesized benchmark; rollback-and-retry is described as an intended downstream benefit but is not empirically evaluated for task success improvement), InferAct (arXiv 2407.11843, EMNLP 2025) for single-step action misalignment detection with human alerting on ALFWorld/WebArena, ProMAS (arXiv 2603.20260) for multi-agent error attribution, ProbGuard (arXiv 2508.00500) for physical safety monitoring, Trajectory Guard (arXiv 2601.00516) for general structural anomaly detection in agentic trajectories, and ErrorProbe (arXiv 2604.17658) for offline step-level cascade diagnosis in multi-agent systems, but none combines cascade-specific onset detection using recoverability signals with a step-threshold calibrated to the Intervention Paradox, empirically evaluated task success improvement on ALFWorld/GAIA/WebShop, and automated targeted rollback. The labeled failure datasets, recoverability signals, and the Intervention Paradox's threshold formula together make a specific, testable hypothesis: a cascade-specific monitor using recoverability signals and a step ≥ 5 threshold will achieve sufficiently higher precision than generic critics and general anomaly detectors to make rollback net-positive on benchmarks where generic critics fail, for the first time.\",\n  \"landscape\": \"Proactive monitoring is an active and crowded area that must be navigated carefully.\\n\\nTrajAD (arXiv 2602.06443, February 2026) is the closest methodological neighbor and must be explicitly differentiated. TrajAD fine-tunes Qwen3-4B with QLoRA (affecting 1.8% of parameters) on TrajBench, a purpose-built benchmark of 63,484 balanced samples synthesized via a 'Perturb-and-Complete' pipeline from AgentBank across five domains (reasoning, mathematics, coding, web navigation, embodied AI), covering three anomaly types: Task Failure (reasoning errors, invalid tool parameters), Process Inefficiency (redundant loops and detours), and Unwarranted Continuation (failure to stop after task completion). TrajBench labels are generated synthetically through controlled perturbation injection, not expert cascade root-cause annotation. TrajAD frames detection as a joint classification-and-localization task, outputting both a binary verdict and the predicted first-error step index (Joint Exact Match: 53.75% vs. 5.81% for the best zero-shot baseline; Macro-F1: 81.81% vs. 70.43%). The paper describes rollback-and-retry as an intended downstream benefit of precise error localization, but does not empirically evaluate whether rollback improves task success rate on any downstream benchmark; TrajAD's evaluation is exclusively on anomaly detection and localization metrics (F1, JEM) on TrajBench. TrajAD does not evaluate on ALFWorld, GAIA, or WebShop in their standard agentic task-completion form. Five distinctions separate TrajAD from CascadeWatch. (1) Training labels: TrajAD's TrajBench uses synthetic perturbations; CascadeWatch trains on AgentErrorBench expert root-cause annotations with the confirmed-cascade criterion (trajectory fails AND root-cause step before midpoint), learning from real cascade failures with verified propagation, not synthetic deviations. (2) Anomaly target and Intervention Paradox awareness: TrajAD's 'Process Inefficiency' category—loops and detours that are semantically valid but suboptimal—is precisely the class of self-correctable deviations that the Intervention Paradox (arXiv 2602.03338) shows causes performance degradation when interrupted; triggering on these raises d in the disruption-recovery tradeoff (Δ Success = p·r − (1−p)·d) and explains why generic critics with AUROC 0.94 still degrade performance. CascadeWatch targets only recoverability-degrading cascade-onset prefixes (not process inefficiencies or unwarranted continuations), and imposes a step ≥ 5 minimum threshold specifically calibrated to the Intervention Paradox's empirical finding that all observed regressions occur at steps 0–1 (on HotPotQA and GAIA; ALFWorld is the exception where early intervention yields modest gains). TrajAD has no step threshold and does not reference or address the Intervention Paradox. (3) Architecture: TrajAD fine-tunes a 4B model via QLoRA, modifying model weights and requiring backbone-level training infrastructure. CascadeWatch trains a 2-layer MLP probe on frozen Qwen/Qwen3-32B embeddings combined with ERR recoverability deltas, requiring no modification to the base agent; deploying on a different backbone requires retraining only the MLP probe (~3–5 H100-hours). (4) Recoverability signal: TrajAD introduces no ERR-motivated recoverability channel; CascadeWatch's ERR Efficiency Score running prefix estimates specifically measure the compounding cost of cascade continuation, providing a principled signal for distinguishing cascade-onset from recoverable anomalies. (5) Task success evaluation: TrajAD evaluates exclusively on anomaly detection metrics (F1, JEM) on TrajBench; CascadeWatch evaluates task success rate improvement on ALFWorld, GAIA, and WebShop, directly measuring whether cascade-specific rollback is net-positive in the Intervention Paradox regime. CascadeWatch and TrajAD address overlapping detection problems on different evaluation surfaces; direct metric comparison is not possible across evaluation surfaces. To enable direct comparison on identical data, CascadeWatch's baseline set includes a TrajAD-style general anomaly detection condition: a general anomaly detector trained on synthetic perturbation labels on the same CascadeWatch benchmarks (ALFWorld/GAIA/WebShop), without a step threshold or ERR recoverability signal, directly testing cascade-specific precision against general-purpose detection in the Intervention Paradox regime.\\n\\nInferAct (arXiv 2407.11843, EMNLP 2025 main track, pages 222–244) uses Theory-of-Mind reasoning grounded in LLM belief inference to detect single-step actions misaligned with user intent before execution on WebArena (web shopping), ALFWorld (household tasks), and HotpotQA (question answering), achieving up to 20% Marco-F1 improvement over baselines. When misalignment is detected, InferAct alerts users for timely correction. Three distinctions separate InferAct from CascadeWatch. (1) InferAct addresses the single-step mismatch between an upcoming action and user authorization—whether a specific action matches what the user intended to authorize (e.g., accidental 'buy-now' triggering); CascadeWatch addresses multi-step cascade propagation, where an early-step cognitive error (steps 5–15) compounds across subsequent trajectory steps independent of any user authorization issue. (2) InferAct's detection signal is ToM belief inference over user intent; CascadeWatch's detection signal is trajectory-prefix ERR Efficiency Score running estimates over cascade-onset patterns, a fundamentally different feature channel targeting compounding-cost propagation rather than intent alignment. (3) InferAct's intervention is human alerting, requiring a human in the loop to correct the misaligned action; CascadeWatch's intervention is automated targeted rollback with a false-positive circuit-breaker (max 2 rollbacks per episode), requiring no human involvement. Published at EMNLP 2025—the primary target venue for CascadeWatch—InferAct is a direct framing overlap that must be cited, but the single-step authorization framing vs. multi-step cascade propagation distinction is substantive.\\n\\nMASC (arXiv 2510.14319) detects cascading errors in multi-agent systems via Prototype-Guided Next-Execution Reconstruction: it forecasts subsequent step embeddings from query and interaction history (Next-Execution Reconstruction) and establishes a prototype prior over normal-step embeddings for stabilized anomaly scoring in sparse contexts (Prototype-Guided Enhancement). Anomaly scoring is unsupervised; when anomalies are flagged, a correction agent revises the acting agent's output before propagating downstream. MASC achieves up to 8.47% AUC-ROC improvement in step-level error detection on the Who&When multi-agent benchmark. Two distinctions separate MASC from CascadeWatch: (1) MASC operates on multi-agent systems where a correction agent revises another agent's output; CascadeWatch operates on single-agent long-horizon trajectories where there is no second agent to correct and the rollback must rewind the agent's own context or environment state. (2) MASC's anomaly scoring is unsupervised (reconstruction-based); CascadeWatch's cascade-onset detection is supervised using expert-annotated root-cause labels and ERR-motivated recoverability signals, enabling principled distinction between cascade-onset and recoverable anomalies.\\n\\nProMAS (arXiv 2603.20260, March 2026) uses Causal Delta Features mapped to a 30-prototype Vector Markov Space with a frozen Meta-Llama-3.1-8B extractor to predict failure onset in multi-agent collaborative reasoning systems, achieving 22.97% step-level accuracy on the Who&When benchmark (annotated multi-agent dialogues of math and logic puzzles) while processing only 27% of reasoning logs. Critically, ProMAS raises an alert but provides no corrective action—it is a detector only and evaluates exclusively on the Who&When multi-agent attribution benchmark, not on single-agent long-horizon tasks.\\n\\nErrorProbe (arXiv 2604.17658, April 2026) is a contemporaneous offline diagnostic for multi-agent systems that uses a three-stage pipeline: (1) failure taxonomy-based local anomaly detection, (2) symptom-driven backward tracing to prune irrelevant trajectory context, and (3) a specialized multi-agent verification team (Strategist, Investigator, Arbiter) that validates error hypotheses via tool-grounded execution. ErrorProbe maintains a verified episodic memory of confirmed error/patch patterns and is evaluated on TracerTraj and Who&When benchmarks. Two distinctions separate ErrorProbe from CascadeWatch: (1) ErrorProbe is a post-hoc offline diagnostic tool—its backward tracing and multi-agent verification pipeline is not compatible with real-time inference-time intervention; CascadeWatch is an online monitor that triggers rollback during episode execution. (2) ErrorProbe targets multi-agent systems; CascadeWatch targets single-agent long-horizon trajectory monitoring where no second agent is available for verification.\\n\\nProbGuard (arXiv 2508.00500) learns a Discrete-Time Markov Chain from symbolic agent-state abstractions with PAC-style guarantees and triggers prompt-injection interventions when P(unsafe state) exceeds a threshold; it predicts traffic violations up to 38.66 seconds ahead and reduces unsafe behavior by 65.37% in embodied agents, but operates on physical safety constraints using symbolic abstractions rather than frozen neural representations or recoverability signals.\\n\\nTrajectory Guard (arXiv 2601.00516, AAAI TrustAgent Workshop 2026) proposes a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss for real-time anomaly detection in agentic AI trajectories, achieving F1 0.88–0.94 on balanced sets and recall 0.86–0.92 on imbalanced external benchmarks while running 17–27× faster than LLM Judge baselines at 32ms inference. Three distinctions separate this from CascadeWatch: (1) Trajectory Guard detects general structural anomalies—contextual misalignment and sequential incoherence—via reconstruction error, not cascade-specific onset via recoverability-delta signals; (2) it evaluates on synthetic perturbations, security audit failures (RAS-Eval), and multi-agent attribution (Who&When), not on single-agent long-horizon cognitive tasks (ALFWorld, GAIA, WebShop); (3) it provides no rollback or correction mechanism—detection only.\\n\\nThe ORC auditing paper (ICLR Workshop 2026, arXiv 2603.13325) detects cascading risks in multi-agent systems via Ollivier-Ricci Curvature on completed interaction graphs—post-hoc auditing, not inference-time intervention.\\n\\nCanonical Path Deviation (arXiv 2602.19008, Feb 2026) is the closest theoretical neighbor to CascadeWatch's cascade-onset framing. Analyzing 515 model-task combinations on the Toolathlon benchmark (22 frontier models, 108 real-world tool-use tasks across 3 independent runs each), Wilson Y. Lee identifies stochastic drift from canonical solution paths—the convergent set of tool invocations shared across successful runs—as a causal mechanism of long-horizon failure. Path adherence is measured as Jaccard similarity between actual and canonical tool invocation sequences; adherence gaps are statistically indistinguishable from zero through the first half of trajectories but become significant and self-reinforcing thereafter, with each off-canonical tool call raising the probability that the next call is also off-canonical by 22.7 percentage points. An intervention restarting the bottom tercile of runs by mid-trajectory canonical adherence achieves +8.8pp success rate improvement. Three distinctions separate this from CascadeWatch: (1) Canonical path adherence requires aggregating tool invocation sequences across multiple successful runs per task—unavailable for novel tasks or low-success-rate settings; CascadeWatch's ERR Efficiency Score running prefix estimates are computable from a single trajectory without reference to other runs. (2) Canonical path deviation detects drift retrospectively via trajectory statistics that become significant only in the second half of execution; CascadeWatch proactively intervenes at steps 5–15 using a trained probe on prefix embeddings, before adherence divergence solidifies. (3) The CPD intervention is a full task restart of lowest-adherence runs; CascadeWatch performs targeted rollback to the pre-cascade checkpoint, preserving valid completed steps and avoiding full re-execution cost.\\n\\nFrom Spark to Fire (arXiv 2603.04474, March 2026) models cascade error propagation in LLM-based multi-agent collaboration using an individual-based mean-field framework over inter-agent communication graphs, and proposes a genealogy-graph governance layer that tracks atomic claim provenance via NLI-based verification (Green/Red/Yellow status using DeBERTa-v3-small) and blocks transmission of error-carrying messages; the Benign Infection Control Rate improves from 0.32 to 0.89 across Chain, Mesh, and Star multi-agent topologies. The cascade mechanism is specifically inter-agent. CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory—where there are no inter-agent message dependencies.\\n\\nThe Intervention Paradox (arXiv 2602.03338) is the most important negative result in the space: ROLLBACK and APPEND interventions triggered by a generic LLM critic (AUROC 0.94) degrade performance on HotPotQA by −2.3 to −25.5pp and on GAIA by −4.4 to −30pp; only ALFWorld (high baseline failure rate: 5.8–14.7%) shows improvement (+0.5 to +2.8pp). All observed regressions occur with early-step (steps 0–1) interventions on HotPotQA and GAIA; the paper recommends a minimum-step constraint of min_step ≥ 2. ALFWorld is the exception where early intervention yields positive returns, consistent with the disruption-recovery tradeoff favoring intervention when baseline failure rate exceeds threshold.\\n\\nBacktrackAgent (arXiv 2505.20660, EMNLP 2025) trains a verifier-judger-reflector pipeline for GUI agents (Mobile3M, Auto-UI benchmarks) to detect individual action errors and trigger backtracking. Unlike CascadeWatch, BacktrackAgent requires constructing a task-specific training dataset and fine-tuning the agent's backtracking components; it targets GUI action-level errors rather than recoverability-degrading cascade onset in cognitive long-horizon tasks.\\n\\nSelf-Backtracking (arXiv 2502.04404) trains the base LLM to internalize when and where to backtrack during training and inference, achieving over 40% performance gains over optimal-path SFT baselines in general reasoning. This approach requires model retraining and modifies the agent's internal reasoning; CascadeWatch operates as a frozen external probe on any pre-trained agent.\\n\\nPrior work probes LLM hidden states for single-step answer correctness in mathematical reasoning (arXiv 2504.05419), achieving 24% token reduction via early exit. The mechanism is structurally similar to CascadeWatch's frozen embedding + MLP probe, but targets single-step correctness rather than multi-step cascade onset; it adds no recoverability signal channel.\\n\\nReactive self-correction methods share the same fundamental limitation: ExpeL and Contextual Experience Replay distill past trajectories for future improvement; self-verification (arXiv 2602.03485) confirms rechecks rarely identify errors; T-STAR (arXiv 2604.07165) achieves training-time divergence detection via Cognitive Trees but adds no inference-time mechanism.\\n\\nNo existing system combines (1) cascade-specific onset detection using ERR recoverability signals, (2) a step ≥ 5 threshold explicitly calibrated to the Intervention Paradox and AgentErrorBench's cascade-onset distribution, (3) expert-annotated cascade labels (not synthetic perturbations), (4) empirically evaluated task success improvement on ALFWorld/GAIA/WebShop (not anomaly detection metrics alone), and (5) environment-appropriate targeted rollback with a false-positive circuit-breaker—nor validates that cascade-specific precision avoids the disruption-recovery tradeoff that defeats all general-purpose critics and general anomaly detectors.\",\n  \"approach\": \"We train CascadeWatch to address the Intervention Paradox by targeting only the recoverability-degrading mid-trajectory patterns that precede confirmed cascades. Training data: AgentErrorBench's 200 expert-annotated trajectories (davide221/agenterrorbench on HuggingFace, spanning ALFWorld, WebShop, and GAIA; all 200 are failure trajectories by design, expert-annotated by ten graduate students at Cohen's κ = 0.55) augmented with ~2,000 synthetic rollouts total from Qwen/Qwen3-32B (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization) sampled at two temperatures (T=0.7, T=1.0), yielding approximately 333 rollouts per benchmark per temperature across ALFWorld, WebShop, and GAIA, to increase failure-mode diversity.\\n\\nCascade label derivation differs between real and synthetic trajectories. For the 200 AgentErrorBench trajectories, the confirmed-cascade criterion is applied using the expert-annotated critical_failure_step field: step k is labeled cascade-onset if k equals the annotated root-cause step AND that step occurs before the trajectory midpoint (k ≤ ⌊total_steps / 2⌋). Since all 200 trajectories are failures by design, the midpoint filter is the only active criterion. Given AgentErrorBench's finding that cascade-initiating errors cluster at steps 5–15, and typical episode lengths of 20–40 steps, the majority of annotated root-cause steps fall before the midpoint. Estimated cascade-positive training examples: approximately 65–75 of 100 ALFWorld trajectories, 35–40 of 50 GAIA trajectories, and 35–40 of 50 WebShop trajectories, totaling approximately 135–155 cascade-positive examples before augmentation. For the ~2,000 synthetic rollouts, expert root-cause annotation is unavailable. Synthetic cascade labels use a trajectory-level failure proxy: a synthetic trajectory is labeled cascade-positive at step k if (1) the trajectory ultimately fails AND (2) k ≤ ⌊N/2⌋, where N is total episode length. This proxy is coarser than the confirmed-cascade criterion—it applies the cascade-positive label to all early-half steps of failed trajectories without identifying the specific root-cause step, including steps that precede any actual error. Concretely, real cascade-onset labels are maximally sparse (exactly one positive-labeled step per trajectory, at the expert-annotated root-cause step, with all other steps labeled 0) while synthetic labels are maximally dense (all steps k ≤ ⌊N/2⌋ in each failed trajectory receive cascade-positive labels); this label density mismatch means the MLP trained on the mixture must reconcile two structurally different decision boundaries—'fire only at the specific cascade-onset step' from real labels versus 'fire throughout the early phase of any failing run' from synthetic labels. The training corpus is therefore a deliberate mixture of high-precision real labels (AgentErrorBench expert root-cause annotations, ~135–155 cascade-positive examples) and lower-precision synthetic labels (trajectory-level failure proxy with label density mismatch). This methodological caveat is acknowledged explicitly; an additional ablation trains the probe on AgentErrorBench-only data to quantify the performance ceiling under expert labels alone versus the mixed corpus, and to isolate whether the probe learns cascade-specific onset patterns (from real labels) or merely learns to fire throughout early failed-run prefixes (synthetic density signal).\\n\\nA minimum intervention threshold of step ≥ 5 is imposed at inference time, grounded in two complementary findings. First, AgentErrorBench's expert annotations show cascade-initiating errors occur primarily at steps 5–15, making cascade-onset detection at k < 5 both empirically impossible (no cascade has yet begun) and mechanistically unnecessary. Second, the Intervention Paradox (arXiv 2602.03338) finds that all regression-causing interventions occur at steps 0–1 on HotPotQA and GAIA, recommending min_step ≥ 2; CascadeWatch's step ≥ 5 threshold is more conservative than this recommendation, providing additional safety margin. Note that ALFWorld is the exception in the Intervention Paradox paper: early intervention yields positive gains on ALFWorld (+0.5 to +2.8pp), consistent with its high baseline failure rate. The step ≥ 5 threshold is therefore over-conservative for ALFWorld specifically—but is retained for consistency across benchmarks and because AgentErrorBench's cascade-onset distribution at steps 5–15 independently grounds the threshold as the earliest step where cascade-positive signal exists. The 50-task pilot test per benchmark will empirically verify whether the threshold is correctly calibrated for each of the three benchmarks.\\n\\nEach trajectory prefix at step k is represented by concatenating (a) frozen Qwen/Qwen3-32B hidden-state embeddings (mean-pooled last 4 transformer layers over the action–observation sequence) with (b) recoverability delta signals. For WebShop and GAIA (tool-augmented benchmarks with structured tool-call/result pairs), these are running prefix estimates of ERR Efficiency Score deltas as defined in arXiv 2601.22352. Critically, the full ERR Efficiency Score formula (ES = RR / (1 + λC/Cmax)) requires knowing the final trajectory outcome (recovery rate RR), making it not directly computable online. CascadeWatch approximates the recoverability delta at step k using observable prefix quantities: the running cumulative cost ratio C_k/Cmax (estimated from trajectory length against the benchmark's typical maximum) and the incremental milestone completion rate, which serves as a partial recovery rate proxy. These prefix-approximated deltas are the features fed to the probe; the approximation error is bounded by the ERR paper's empirical δ ≤ 0.05 validation result, which confirms that prefix statistics are predictive of final recoverability within this tolerance. For ALFWorld (a text-based game where failures are cognitive planning errors rather than tool execution failures, and which lacks structured tool-call pairs), the domain-adapted proxy is step-level delta in the normalized ALFWorld game score (Δ(info['score'] / info['max_score']) at each step), which tracks incremental subgoal-completion rate. This is an acknowledged heuristic extension of the ERR framework; whether the recoverability motivation holds for this proxy is explicitly tested in the ablation.\\n\\nA 2-layer MLP probe (with L2 weight decay 1e-4) outputs P(cascade | prefix_k), with Platt scaling applied on a stratified held-out validation split. Training data sparsity is addressed by (i) 3-fold cross-validation stratified by benchmark (ALFWorld / WebShop / GAIA) to estimate generalization without benchmark leakage, and (ii) a parallel logistic probe baseline to assess whether MLP complexity is justified over this small labeled set. The GAIA cascade probe operates near the minimum viable supervised learning regime (~27 training samples per fold in 3-fold CV across ~35–40 GAIA cascade-positive examples); GAIA results are consequently treated as preliminary evidence, with ALFWorld (~65–75 cascade-positive examples, ~43–50 per fold) providing the primary evidence base for the main cascade-avoidance claim.\\n\\nCascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. This is a meaningful practical advantage over BacktrackAgent, which requires constructing a task-specific training dataset and fine-tuning agent components, and over TrajAD, which fine-tunes a 4B model via QLoRA and must be retrained per backbone.\\n\\nThe rollback mechanism is specified per benchmark. For ALFWorld, environment-state rollback is performed via command-replay from env.reset(): the TextWorld gym environment is reset to the initial observation, then the k−1 accepted actions from the checkpoint buffer are re-executed sequentially to reconstruct game state at step k−1. The ALFWorld game engine processes each text command in approximately 1–2ms; for typical episodes capped at 50 steps, rollback at step k incurs roughly 25–100ms wall-clock overhead—negligible relative to LLM inference time. A checkpoint buffer stores accepted action sequences at each step to enable replay without re-querying the LLM. Note that TextWorld's Python API does not expose a save/restore mechanism for Glulx-format (.ulx) games used in ALFWorld competition settings, so command-replay is the correct mechanism; the O(k) replay cost is in game-engine steps, not LLM compute. For WebShop and GAIA, context-only rollback rewinds the agent context window to step k_checkpoint, masks all subsequent actions and observations, and re-samples an alternative action with temperature +0.3. Context-only rollback does not undo irreversible WebShop web-state changes (e.g., submitted searches), which is explicitly noted as a limitation; the WebShop simulation environment resets between episodes, so irreversibility affects intra-episode recovery quality but not cross-episode evaluation validity.\\n\\nA false-positive circuit-breaker limits rollback to a maximum of 2 triggers per episode; after the second trigger, monitoring is suspended for the remainder of the episode to prevent compounding disruption. Before full evaluation, we run the Intervention Paradox's 50-task pilot test on each benchmark to empirically verify that CascadeWatch's cascade-specific intervention is net-positive (p > d/(r+d)) on that benchmark; benchmarks where the pilot test fails are reported as negative results, not omitted.\\n\\nWe include a pre-registered 4-way ablation: (a) frozen embeddings only → logistic probe, (b) recoverability-delta features only → logistic regression (no embeddings), (c) full CascadeWatch (embeddings + recoverability-delta) → 2-layer MLP, and (d) AgentErrorBench-only training (no synthetic augmentation) → 2-layer MLP, to quantify the noise contribution of the synthetic trajectory-level proxy labels (with their label density mismatch) versus high-precision expert labels. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld, GAIA, and WebShop while avoiding the performance degradation caused by generic critics observed in the Intervention Paradox—demonstrating for the first time that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation serves as an internal validation gate: if recoverability-delta provides ≥3% F1 lift over frozen embeddings alone, the ERR-motivated feature design is empirically confirmed; if the lift is <3%, the theoretical ERR motivation weakens substantially and this is reported honestly as a negative result on the recoverability signal hypothesis. We evaluate task success rate, steps saved per episode, and false-positive intervention rate against no-correction, ExpeL-style reflection, self-verification, T-STAR offline, a TrajAD-style general anomaly detection baseline (trained on synthetic perturbation labels on the same CascadeWatch benchmarks without step threshold or ERR signal, re-implementing TrajAD's training methodology on CascadeWatch's evaluation surface), and ProMAS-style detection-only baselines on ALFWorld, WebShop, and GAIA (subject to pilot test results). The TrajAD-style baseline directly tests whether cascade-specific detection (step ≥ 5 threshold + ERR signal + expert labels) outperforms general anomaly detection (no threshold + synthetic labels + process inefficiency triggering) in the Intervention Paradox regime on the identical evaluation surface.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~100-140 H100-hours total: rollout generation ~45 H100-hours (Qwen/Qwen3-32B runs in BF16 on 1× H100-80GB without quantization—32B × 2 bytes ≈ 64GB, within the 80GB VRAM budget; inference throughput roughly doubles relative to a 72B model; ~45h covers ~5K synthetic rollouts across three benchmarks at three temperatures, including environment interaction overhead and tool-call latency for GAIA tasks); probe training ~10 H100-hours (5-fold CV × 4-way ablation × logistic/MLP variants; these are small models, <1h each); evaluation runs ~45–85 H100-hours across three benchmarks + pilot tests (50 tasks × 3 benchmarks × 2 conditions per test). ALFWorld command-replay rollback adds <1 H100-hour overhead across all evaluation episodes.\",\n      \"gpu_utilization\": \"~30–40% effective utilization; high idle between human coding, debugging, and analysis cycles\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"2 researchers\",\n      \"estimated_gpu_cost\": \"~$200–$280 at ~$2/H100-hour\"\n    },\n    \"human_in_loop\": {\n      \"scope_note\": \"Compressed to satisfy the joint ≤16-day calendar / ≤200 H100-hour constraint. Primary benchmarks: ALFWorld + GAIA + WebShop (all three, matching TrajAD's intended evaluation surface). Synthetic rollouts: 2,000 total at 2 temperatures (T=0.7, T=1.0), approximately 333 rollouts per benchmark per temperature (333 ALFWorld + 333 GAIA + 333 WebShop per temperature × 2 temperatures = 2,000 total); 3-fold CV. Human gates: cascade label validation (including review of synthetic trajectory-level proxy labeling procedure and label density mismatch implications), pilot test pass/fail judgment per benchmark, ablation design review, threshold decisions. Human engagement: 2–3 hours/day.\",\n      \"compute_breakdown\": \"Rollout generation (2,000 total rollouts: ≈333 per benchmark per temperature × 2 temperatures × 3 benchmarks): ~8–12 H100-hours (ALFWorld ≈666 rollouts ~1–2h; GAIA ≈666 rollouts ~4–6h including tool-call overhead; WebShop ≈666 rollouts ~2–4h; Qwen/Qwen3-32B BF16 on 1× H100-80GB without quantization). Probe training (3-fold CV × 4-way ablation × logistic/MLP): ~4–6 H100-hours. Pilot tests (50 tasks × 3 benchmarks × 2 conditions × 2 seeds = 600 episodes): ~10–15 H100-hours. Full evaluation (post-pilot, 3 benchmarks × 5 baselines + CascadeWatch): ~35–50 H100-hours. Buffer/debugging: ~5–10 H100-hours. Total: ~62–93 H100-hours.\",\n      \"gpu_hours\": \"~62–93 H100-hours (well within ≤200 H100-hour constraint)\",\n      \"gpu_utilization\": \"~60–70% utilization; human approval gates reduce compute waste on dead-end ablations\",\n      \"timeline\": \"12–14 calendar days (rollout generation days 1–3, labeling + probe training days 2–5, pilot tests with human review days 5–9, full evaluation days 8–12 with GAIA and WebShop evaluations running in parallel, analysis and write-up days 10–14)\",\n      \"team\": \"1 researcher, ~2–3 hours/day check-in\",\n      \"claude_api_cost\": \"$150–$250\",\n      \"estimated_gpu_cost\": \"~$124–$186 at ~$2/H100-hour\",\n      \"risk_note\": \"Small labeled training set (200 trajectories, all failures) risks MLP overfitting; confirmed-cascade criterion and synthetic proxy labeling strategy are critical human-gate decisions. Synthetic trajectory-level proxy labels are coarser than expert annotations and exhibit label density mismatch (maximally dense vs. maximally sparse real labels); the AgentErrorBench-only ablation (4-way ablation arm d) will quantify this noise and determine whether the probe learns cascade-specific onset or merely fires throughout early failed-run prefixes. GAIA evaluation results should be treated as preliminary evidence (~27 cascade-positive training samples per fold in 3-fold CV) pending replication on a larger annotated set. ALFWorld ERR proxy (game score delta) is a domain adaptation—its F1 contribution must be validated in ablation before committing to full evaluation on ALFWorld. WebShop context-only rollback does not undo irreversible intra-episode web-state changes (submitted searches); this is a limitation of the intervention mechanism, not the detection mechanism, and is explicitly noted. Pilot test (50 tasks × 3 benchmarks) must be reviewed by human before committing to full evaluation on each benchmark.\"\n    },\n    \"auto_research\": {\n      \"note\": \"This mode exceeds the primary ≤200 H100-hour constraint and is presented as an extended evaluation scenario for teams with unrestricted compute, not a valid path within the joint 16-day/200 H100-hour constraint. Included for completeness only.\",\n      \"gpu_hours\": \"~300–450 H100-hours (3–5× more ablations across probe architectures, threshold strategies, feature combinations, augmentation volumes, rollback trigger policies, and minimum-step thresholds; reduced from prior estimates due to Qwen/Qwen3-32B being more compute-efficient than the previously specified 72B model)\",\n      \"gpu_utilization\": \"~85–95%; near-zero idle as agent continuously queues and launches experiments\",\n      \"timeline\": \"3–10 days with 4+ H100s in parallel\",\n      \"team\": \"0 (initial setup only)\",\n      \"claude_api_cost\": \"$350–$600\",\n      \"estimated_gpu_cost\": \"~$600–$900\",\n      \"speed_bottleneck\": \"Number of H100s available; rollout generation dominates throughput\",\n      \"risk_note\": \"Automated cascade label derivation for synthetic trajectories uses trajectory-level failure proxy (step k ≤ ⌊N/2⌋ in failed trajectories)—coarser than expert confirmed-cascade criterion, with label density mismatch (all early-half steps labeled positive) that the auto-research mode cannot self-correct without human oversight. No human oversight to detect always-predict-cascade degenerate solutions or validate that the synthetic proxy is not systematically mis-labeling self-correcting trajectories. Pilot test pass/fail judgment and Intervention Paradox threshold calculation require human review—an agent may proceed to full evaluation on benchmarks where intervention is net-negative. ALFWorld ERR proxy domain adaptation requires human judgment to validate before scaling.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR deadline May 25, 2026)\",\n    \"AAAI 2027 (abstract deadline expected ~August 2026)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Where LLM Agents Fail and How They can Learn From Failures (arXiv 2509.25370, 2025)\",\n    \"Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents (arXiv 2601.22352, 2026)\",\n    \"The Intervention Paradox: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention (arXiv 2602.03338, 2026)\",\n    \"Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2602.19008, 2026)\",\n    \"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents (arXiv 2602.06443, 2026)\",\n    \"InferAct: Inferring Safe Actions for LLM-Based Agents Through Preemptive Evaluation and Human Feedback (arXiv 2407.11843, EMNLP 2025, pages 222–244)\",\n    \"MASC: Metacognitive Self-Correction for Multi-Agent Systems via Prototype-Guided Next-Execution Reconstruction (arXiv 2510.14319, 2025)\",\n    \"Trajectory Guard: A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI (AAAI TrustAgent Workshop 2026, arXiv 2601.00516)\",\n    \"ProMAS: Proactive Error Forecasting for Multi-Agent Systems Using Markov Transition Dynamics (arXiv 2603.20260, 2026)\",\n    \"From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration (arXiv 2603.04474, 2026)\",\n    \"ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety (arXiv 2508.00500, 2025)\",\n    \"Auditing Cascading Risks in Multi-Agent Systems via Semantic–Geometric Co-evolution (ICLR Workshop 2026, arXiv 2603.13325)\",\n    \"Towards Self-Improving Error Diagnosis in Multi-Agent Systems (arXiv 2604.17658, 2026)\",\n    \"Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes (arXiv 2604.28138, 2026)\",\n    \"Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization (arXiv 2604.07165, 2026)\",\n    \"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning (arXiv 2602.03485, 2026)\",\n    \"Beyond Fluency: Toward Reliable Trajectories in Agentic IR — position paper on failure modes, not empirical cascade measurement (arXiv 2604.04269, 2026)\",\n    \"BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism (EMNLP 2025, arXiv 2505.20660)\",\n    \"Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models (arXiv 2502.04404, 2025)\",\n    \"Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv 2504.05419, 2025)\"\n  ],\n  \"description\": \"Long-horizon agent tasks suffer from cascade failures: a single early error propagates across subsequent steps, compounding recovery cost. The critical challenge is the Intervention Paradox (arXiv 2602.03338): a generic critic with AUROC 0.94 causes up to 26 percentage point degradation by disrupting self-correcting trajectories, with all observed regressions occurring at early intervention steps (steps 0–1) on HotPotQA and GAIA—ALFWorld is the exception where early intervention yields modest gains. The solution requires cascade-specific, high-precision detection rather than general failure prediction or general anomaly detection. We propose CascadeWatch, an inference-time monitor that targets cascade onset specifically using frozen Qwen/Qwen3-32B hidden-state embeddings (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization) combined with running prefix estimates of ERR Efficiency Score recoverability deltas to estimate P(cascade_failure | prefix_k) at each step, with a minimum trigger threshold of step ≥ 5. This threshold is doubly grounded: (1) AgentErrorBench shows cascade-initiating errors begin at step 5, so cascade-onset detection is mechanistically impossible before step 5; (2) the Intervention Paradox recommends min_step ≥ 2 to avoid regression-causing early interventions—step ≥ 5 is more conservative than this recommendation. For WebShop and GAIA (tool-augmented benchmarks), recoverability deltas are running prefix estimates of ERR Efficiency Score quantities (arXiv 2601.22352), approximated from observable cumulative cost ratios and incremental milestone completion rates without requiring final trajectory outcomes. For ALFWorld (text-based game with cognitive planning errors, not tool execution failures), a domain-adapted proxy is used: step-level delta in the normalized ALFWorld game score, acknowledged as a heuristic extension and isolated in the ablation.\\n\\nTraining uses AgentErrorBench's 200 expert-annotated trajectories (all failure trajectories by design; ALFWorld: 100, GAIA: 50, WebShop: 50) augmented with ~2,000 synthetic rollouts total (approximately 333 per benchmark per temperature across T=0.7 and T=1.0). Cascade label derivation differs by data source: AgentErrorBench trajectories use the confirmed-cascade criterion (root-cause step before trajectory midpoint per expert critical_failure_step annotation), yielding approximately 65–75 cascade-positive examples from ALFWorld, 35–40 from GAIA, and 35–40 from WebShop (~135–155 total). Synthetic trajectories use a trajectory-level failure proxy (cascade-positive = any step k ≤ ⌊N/2⌋ in a failed trajectory), which exhibits a label density mismatch relative to real labels: real labels are maximally sparse (one positive step per trajectory at the expert-annotated root-cause step) while synthetic labels are maximally dense (all first-half steps of each failed trajectory receive cascade-positive labels). The MLP trained on the mixture must reconcile these as structurally different decision boundaries; a 4-way ablation includes an AgentErrorBench-only arm to determine whether the probe learns cascade-specific onset or merely fires throughout early failed-run prefixes.\\n\\nCascadeWatch is positioned precisely among nine distinct neighboring systems. (1) TrajAD (arXiv 2602.06443) fine-tunes Qwen3-4B with QLoRA on TrajBench (63,484 balanced samples, five domains: reasoning, math, coding, web navigation, embodied AI) for general trajectory anomaly detection, evaluating exclusively on TrajBench anomaly detection metrics (F1, JEM); rollback-and-retry is described as an intended benefit but is not empirically evaluated for task success improvement, and TrajAD does not evaluate on ALFWorld, GAIA, or WebShop in their standard agentic form. TrajAD's three anomaly types include 'Process Inefficiency' (loops/detours) which is precisely the self-correctable deviation class that the Intervention Paradox shows causes regression when interrupted—TrajAD has no step threshold and does not address the Intervention Paradox tradeoff. CascadeWatch differs: trained on AgentErrorBench expert cascade root-cause annotations (not synthetic perturbations), targeting only recoverability-degrading cascade-onset prefixes (not process inefficiencies), imposing step ≥ 5 threshold calibrated to both the Intervention Paradox and AgentErrorBench's cascade-onset distribution, requiring no model fine-tuning (frozen external probe), and directly evaluating task success improvement on ALFWorld/GAIA/WebShop. CascadeWatch and TrajAD address overlapping detection problems on different evaluation surfaces; CascadeWatch's baseline set includes a TrajAD-style general anomaly detection condition trained on synthetic perturbation labels on the same CascadeWatch benchmarks to enable direct comparison. (2) InferAct (arXiv 2407.11843, EMNLP 2025) uses Theory-of-Mind reasoning to detect single-step actions misaligned with user intent on WebArena, ALFWorld, and HotpotQA, achieving up to 20% Marco-F1 improvement, alerting humans for correction; InferAct targets single-step authorization misalignment while CascadeWatch targets multi-step cascade propagation using ERR recoverability prefix estimates, with automated rollback rather than human alerting. (3) MASC (arXiv 2510.14319) detects cascading errors in multi-agent systems via unsupervised Prototype-Guided Next-Execution Reconstruction on Who&When; CascadeWatch targets single-agent cascade onset using supervised ERR-motivated recoverability labels on ALFWorld, GAIA, and WebShop. (4) Canonical Path Deviation (arXiv 2602.19008) identifies stochastic drift from canonical solution paths—aggregated from multiple successful runs per task—as a long-horizon failure mechanism, achieving +8.8pp improvement via restart of lowest-adherence runs; CascadeWatch uses single-trajectory recoverability prefix estimates (no canonical paths required) and performs targeted rollback rather than full restarts. (5) ErrorProbe (arXiv 2604.17658) is a contemporaneous offline diagnostic for multi-agent systems using backward tracing and multi-agent verification teams; CascadeWatch is an online single-agent monitor with automated rollback, not an offline diagnostic. (6) From Spark to Fire (arXiv 2603.04474) proposes a genealogy-graph governance layer for cascade mitigation in multi-agent collaboration; CascadeWatch addresses single-agent cognitive cascade failure where there are no inter-agent message dependencies. (7) ProMAS (arXiv 2603.20260) raises alerts in multi-agent reasoning but provides no corrective action and evaluates only on Who&When. (8) ProbGuard (arXiv 2508.00500) softly intervenes on physical safety constraints via symbolic DTMC. (9) Trajectory Guard (arXiv 2601.00516) uses a Siamese Recurrent Autoencoder for general structural anomaly detection at 32ms but targets reconstruction deviation on security audit and multi-agent benchmarks, provides no rollback.\\n\\nUnlike BacktrackAgent (arXiv 2505.20660, EMNLP 2025), which trains a verifier-judger-reflector pipeline for GUI action errors, CascadeWatch requires no modification to the base agent; unlike TrajAD, it requires no backbone fine-tuning—deploying on a different backbone requires retraining only the MLP probe (~3–5 H100-hours). Unlike Self-Backtracking (arXiv 2502.04404), which trains the LLM itself, CascadeWatch operates as a frozen external probe. Prior hidden-state probing (arXiv 2504.05419) targets single-step reasoning correctness for token reduction; CascadeWatch targets multi-step cascade onset with ERR recoverability prefix estimates as a second feature channel.\\n\\nRollback: for ALFWorld, command-replay from env.reset() (~25–100ms for 50-step episodes; TextWorld's Python API does not expose save/restore for Glulx-format .ulx games); for WebShop and GAIA, context-only rollback (does not undo irreversible intra-episode web-state changes—acknowledged as limitation; WebShop simulation resets between episodes so this affects recovery quality but not evaluation validity). Cascade-positive training examples: ~135–155 from AgentErrorBench expert annotations before synthetic augmentation. GAIA probe operates near minimum viable supervised learning regime; GAIA results are preliminary evidence. Primary empirical claim: CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld, GAIA, and WebShop while avoiding the performance degradation caused by generic critics and general anomaly detectors—demonstrating that cascade-specific precision with Intervention Paradox–calibrated thresholding is sufficient to make rollback net-positive on benchmarks where generic critics fail. A TrajAD-style baseline re-implements TrajAD's training methodology (synthetic perturbation labels, no step threshold, no ERR signal) on the same CascadeWatch evaluation surface to enable direct comparison. Recoverability-delta ablation: ≥3% F1 lift confirms ERR-motivated design; <3% is reported as a negative result. Compressed HIL mode fits within ~62–93 H100-hours and 12–14 calendar days.\",\n  \"project_name\": \"cascade_monitor\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL MISSING RELATED WORK: ProMAS (arXiv 2603.20260, March 2026) — 'Proactive Error Forecasting for Multi-Agent Systems Using Markov Transition Dynamics' — directly pre-empts the core contribution. It proactively predicts failures from trajectory prefixes using semantic displacement features + MLP Proactive Prediction Head, achieving 22.97% step-level accuracy while processing only 27% of reasoning logs. Without citing and clearly differentiating from ProMAS, reviewers will reject on novelty grounds.\", \"CRITICAL MISSING RELATED WORK: ProbGuard (arXiv 2508.00500, August 2025) — 'Probabilistic Runtime Monitoring for LLM Agent Safety' — learns a DTMC from execution traces to estimate P(reaching unsafe states) at each step and triggers intervention when risk exceeds threshold. This is structurally isomorphic to CascadeWatch (P(cascade) > threshold → intervention). Though applied to physical safety, not cognitive-task cascades, it must be discussed in related work.\", \"Training data is critically sparse: ~200 labeled trajectories total (100 ALFWorld, 50 WebShop, 50 GAIA). Even with 5K synthetic augmentation, the distribution shift between synthetic (Qwen3-72B backbone rollouts) and the human-annotated test distribution may dominate. No cross-validation strategy or regularization design is specified to guard against overfitting the 2-layer MLP to this small set.\", \"Rollback mechanism underspecified for stateful environments: ALFWorld and WebShop are simulators with action-irreversible state (e.g., picking up an object, submitting a search). 'Targeted rollback to the last low-risk checkpoint' requires either full simulator state serialization at every step (not costed, adds significant engineering overhead) or is limited to context-only rollback (which does NOT undo executed actions). This is a core mechanism that must be precisely defined.\", \"Resource estimate does not explicitly convert A100-hours to H100-hours. Qwen3-72B requires 2× A100 80GB or 1× H100 80GB for FP16 inference, so the stated '~80h A100 for rollout generation' should read '~80h × 2 GPUs = ~160 A100-GPU-hours = ~80 H100-hours.' Total revised estimate: ~145-160 H100-hours (still within 200, but needs to be shown explicitly).\", \"Cascade label derivation from root-cause annotations introduces labeling noise: not all trajectories with a root-cause error at step k actually produce cascades — some errors are contained. The label = 'any step ≥ earliest root-cause error is cascade-onset' assumption will generate false cascade labels for trajectories where the agent partially recovers, inflating cascade-positive counts and degrading classifier reliability.\", \"No ablation is planned to isolate the contribution of ERR-delta features vs. hidden-state embeddings alone. Without this ablation, the paper cannot claim that integrating ERR adds value, which is the key technical differentiator from ProMAS. If ERR adds ≤1% over embeddings-only, the theoretical motivation weakens substantially.\", \"False-positive compounding is unaddressed: if the monitor fires at step k and the re-sampled action (with elevated temperature) is worse than the original, the agent is now at step k with a potentially worse trajectory prefix. There is no circuit-breaker to prevent repeated triggers, which could lead to worse outcomes than no correction at all.\", \"The 'Snowball Effect' paper (arXiv 2604.04269) is cited as quantifying 'exponential error amplification,' but from the abstract it is a position/analysis paper about agentic IR, not an empirical measurement of cascade amplification rates that can be cited as empirical support. The claim should be qualified.\"]\nFeedback: The core idea — a lightweight probe combining frozen LLM hidden-state features with ERR-derived recoverability signals to trigger early rollback — is technically coherent and the supporting evidence (AgentErrorBench, ERR paper) is well-chosen. The revision should focus on three surgical changes that would materially strengthen the paper for EMNLP:\n\n1. **Differentiate from ProMAS and ProbGuard explicitly.** Add both to related work. The differentiating argument should be: (a) ProMAS uses Markovian transition dynamics between quantized semantic clusters but has no corrective action mechanism; CascadeWatch is the first proactive monitor that triggers hard rollback rather than only raising an alert. (b) ProbGuard operates via prompt-injection intervention on physical safety constraints using a DTMC; CascadeWatch targets cognitive-task cascade failure using frozen neural representations + recoverability signals. Frame CascadeWatch as the first system that closes the loop: ProMAS detects, ProbGuard detects and softly intervenes — CascadeWatch detects and hard-rollbacks with empirically validated cascade labels.\n\n2. **Make rollback concrete.** For stateful environments (ALFWorld, WebShop), specify whether rollback restores full simulator state (requiring explicit checkpoint saving at each step) or is context-only (rewinding the prompt/observation history while leaving environment state unchanged). Context-only rollback is implementable in 16 days and sufficient to demonstrate the method; hard state rollback requires environment-specific engineering. Pick one, specify it, and note the limitation for the other case.\n\n3. **Add the ablation that proves ERR adds value.** The only new feature CascadeWatch contributes over ProMAS is the ERR-derived Efficiency Score delta signals. Budget 20-30 A100-hours for a 3-way ablation: (a) embeddings-only probe, (b) ERR-deltas-only logistic regression, (c) full CascadeWatch. If ERR provides ≥3% F1 lift over (a), this is the central empirical result of the paper and should be foregrounded.\n\nMinor: Fix the resource estimate to show explicit H100-hour conversion. Address label noise in cascade derivation by adding a 'cascade confirmed' criterion (e.g., task fails AND root-cause step is before the midpoint). Add a false-positive circuit-breaker (max 2 rollbacks per episode).\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL — TextWorld save_game/restore_game API is factually incorrect: TextWorld core.py has no save_game or restore_game methods (confirmed via GitHub); the Glulx interpreter's text-level save/restore commands exist but are documented as disabled for ALFWorld competition games (TextWorld GitHub issue #161); the only state-copy mechanism is env.copy(), which does not support .ulx Glulx games and incurs full environment duplication cost, not 5ms. The rollback implementation must be redesigned: either use command-replay from reset (O(k) cost, not 5ms — must be costed), use Jericho's RAM-save for .z8 format games (different game engine, not ALFWorld), or acknowledge ALFWorld rollback is also context-only. The title 'Hard Rollback' is misleading if ALFWorld's claimed mechanism doesn't exist.\", \"CRITICAL — Hard constraint incompatibility: the 16-day timeline and ≤200 H100-hour compute budget cannot be jointly satisfied. Manual mode: 135–175 H100-hours (within budget) but 4–6 months (violates 16 days). HIL mode: 180–220 H100-hours (within budget) but 4–8 weeks (violates 16 days). Auto-research mode: 3–10 days (within 16 days) but 480–600 H100-hours (2.4–3× the 200-hour limit). The paper must either restructure the HIL mode to be achievable in 16 days under 200 H100-hours (e.g., 3–4 benchmarks only, no ablation sweep, 2K rollouts instead of 5K), or honestly acknowledge that a 16-day execution requires either compute overage or reduced scope.\", \"MISSING RELATED WORK — BacktrackAgent (arXiv 2505.20660, May 2025): a framework for GUI agent error detection and backtracking with verifier, judger, and reflector modules. The conceptual overlap (error detection → backtracking trigger) must be acknowledged and differentiated. CascadeWatch's differentiator is cascade-specific detection using recoverability signals, not the backtracking trigger mechanism itself.\", \"MISSING RELATED WORK — 'Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models' (arXiv 2502.04404, Feb 2025): trains LLMs to internalize when and where to backtrack during both training and inference. Must be cited to clarify that CascadeWatch is an external monitor (does not require model retraining) and targets cascade failure specifically, not general reasoning dead-ends.\", \"MISSING RELATED WORK — 'Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification' (arXiv 2504.05419, Apr 2025): uses frozen LLM hidden-state probes for correctness prediction with 24% token reduction in reasoning tasks. The mechanism is structurally similar to CascadeWatch's frozen Qwen3-72B embedding + MLP probe. Must be cited; key differentiation is that CascadeWatch targets agent cascade failure (multi-step trajectory prefixes) rather than single-step answer correctness.\", \"ERR applicability gap: the ERR paper (arXiv 2601.22352) formalizes recoverability for tool-augmented agents recovering from tool execution failures (e.g., API errors, failed web actions). ALFWorld is a text-based game where failures are cognitive planning errors, not tool execution failures. The paper must explicitly address how the Efficiency Score observable is computed for ALFWorld trajectories that lack structured tool-call/result pairs, or qualify that ERR-delta features apply only to WebShop and GAIA (which involve tool use) and use a different recoverability proxy for ALFWorld.\", \"Title inconsistency: the paper is titled 'CascadeWatch: Cascade-Onset Detection with Hard Rollback' but WebShop and GAIA receive only context-only rollback (which explicitly does not undo executed web-state changes). If ALFWorld's save_game/restore_game API doesn't exist either, then no benchmark achieves hard rollback. Either fix the rollback mechanism for at least one benchmark to be genuinely hard, or rename to 'CascadeWatch: Cascade-Onset Detection with Targeted Rollback'.\", \"Resource estimate inconsistency: the auto-research mode (480–600 H100-hours) is presented as a valid execution mode but exceeds the stated hard constraint of ≤200 H100-hours by 2.4–3×. The auto-research section should be framed as 'extended evaluation beyond constraint' or the constraint should be explicitly re-evaluated for that mode.\"]\nFeedback: The Round 2 revision successfully addresses five of nine Round 1 issues: ProMAS and ProbGuard are now explicitly differentiated, the confirmed-cascade criterion fixes label noise, the 3-way ablation is pre-registered, the H100-hour conversion is shown, and the circuit-breaker is specified. The idea remains technically sound and well-motivated. Three surgical changes are needed for Round 3:\n\n1. **Fix the ALFWorld rollback claim (highest priority).** The save_game/restore_game methods do not exist in TextWorld's Python API, and the Glulx-level save commands are disabled for ALFWorld competition games. Replace with one of: (a) command-replay rollback from env.reset() — acknowledge the O(k) replay cost and add ~5–10 H100-hours to the compute estimate; (b) restrict to context-only rollback for all three benchmarks and retitle accordingly; (c) prototype with Jericho's .z8 RAM-save API, but note this uses a different game format from standard ALFWorld. Option (b) is achievable in 16 days; option (c) risks benchmark mismatch. Whatever you choose, the 5ms claim must be removed.\n\n2. **Add three missing citations with differentiation.** For BacktrackAgent (2505.20660): 'Unlike BacktrackAgent's trained verifier-judger-reflector pipeline for GUI actions, CascadeWatch uses a cascade-specific probe targeting recoverability-degrading prefix patterns, without modifying the base agent.' For Self-Backtracking (2502.04404): 'Self-Backtracking trains the base LLM to internalize rollback decisions; CascadeWatch requires no model retraining and operates as an external monitor on any frozen agent.' For hidden-state probes (2504.05419): 'Prior work probes hidden states for single-step answer correctness in reasoning tasks; CascadeWatch probes multi-step trajectory prefixes for cascade onset in long-horizon agent tasks, adding ERR-delta recoverability signals as a second feature channel.'\n\n3. **Resolve the 16-day/200 H100-hour joint constraint.** The only execution path within both constraints is a compressed HIL mode: reduce to 2 benchmarks (ALFWorld + GAIA), 2K synthetic rollouts at 2 temperatures, 3-fold CV instead of 5-fold, and daily human engagement of 2–3 hours rather than 30 minutes. This brings estimated compute to ~120–140 H100-hours and calendar time to 12–14 days. Show this math explicitly.\n\nMinor: Qualify ERR-delta applicability — note that for ALFWorld, Efficiency Score deltas are computed from step-level reward signals (ALFWorld provides intermediate rewards) rather than from tool-call success rates, and acknowledge this is a domain adaptation of the ERR framework.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"UNACKNOWLEDGED COMPETITOR — arXiv 2602.19008 'Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks' (Feb 2026, Wilson Y. Lee) directly analyzes why long-horizon agents fail by measuring stochastic drift from canonical solution paths. The key finding—that adherence gaps become significant only at 75% trajectory completion and that drift is self-reinforcing—is structurally equivalent to cascade-onset propagation, using path adherence as the recoverability-degrading signal. CascadeWatch must cite this and explain why detecting recoverability-delta (ERR Efficiency Score) is preferable to detecting canonical path deviation as an early-warning signal.\", \"UNACKNOWLEDGED RELATED WORK — arXiv 2603.04474 'From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration' (March 2026) explicitly models cascade error propagation in LLM-based systems and proposes a governance layer with rollback via message-layer blocking, achieving defense success rate from 0.32 to 0.89. Although this is multi-agent and uses genealogy graphs rather than trajectory-prefix probes, EMNLP reviewers will find it. CascadeWatch should explicitly state: this paper targets multi-agent distributed collaboration; CascadeWatch targets single-agent long-horizon cognitive failure in text-game and tool-augmented environments. The distinction is real but must be stated.\", \"AGENT-SPECIFICITY CLAIM IS MISLEADING: The paper claims CascadeWatch is 'deployable on any frozen agent without model retraining.' This is false as stated. The probe uses frozen Qwen3-72B hidden-state embeddings as features; deploying it with a different backbone (Claude, GPT-4o, Llama-3.3-70B) changes the embedding space entirely, requiring full probe retraining on that backbone's trajectories. The correct claim is: 'CascadeWatch requires no modification to the base agent and does not require retraining the base agent; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours), not the base agent.' This is still a meaningful practical advantage over BacktrackAgent but must be stated accurately.\", \"PRIMARY EMPIRICAL CLAIM FRAMING: The central empirical claim is stated as 'recoverability-delta provides ≥3% F1 lift over embeddings alone.' This is an ablation threshold, not a headline result. EMNLP reviewers will evaluate the paper primarily on the task success rate improvement over baselines (no-correction, ExpeL, self-verification) on ALFWorld and GAIA—especially whether CascadeWatch avoids the Intervention Paradox regression observed with generic critics. The ≥3% F1 ablation claim should be repositioned as an internal validation gate; the primary empirical claim should be the task success rate delta against baselines on pilot-test-passing benchmarks.\", \"MODEL VERSION STALENESS: The paper specifies 'frozen Qwen3-72B' as the backbone, but Qwen3.5 (released February 2026) and Qwen3.6-Plus supersede Qwen3-72B as of the submission date. This does not invalidate the method but creates a reproducibility question—which checkpoint is used? The paper should specify the exact model checkpoint (Qwen/Qwen3-72B on HuggingFace or equivalent) to ensure reproducibility, or update to Qwen3.5-72B-Instruct if that provides meaningfully better cascade signal separation.\", \"MINOR — Crab (arXiv 2604.28138) is cited in key references but its role is unclear in the paper. Crab provides semantics-aware checkpoint/restore for agent sandboxes, which is architecturally relevant to the rollback mechanism. The paper should clarify whether Crab was considered for ALFWorld rollback (and why command-replay was chosen instead) or should remove the citation if it has no direct bearing on the method.\"]\nFeedback: Round 3 has cleanly resolved all three surgical changes requested in Round 2: the ALFWorld rollback mechanism is now technically correct (command-replay from env.reset(), O(k) acknowledged, no false save_game claim), the joint 16-day/200 H100-hour constraint is satisfied in the HIL mode (80–110 H100-hours, 12–14 days), and all three requested citations are present with accurate differentiation. The idea is now coherent, well-specified, and positioned at the right level of novelty for EMNLP Findings. One more focused round is needed.\n\n**Four targeted changes for Round 4:**\n\n1. **Cite and differentiate arXiv 2602.19008 (Canonical Path Deviation).** This paper (Feb 2026) is the closest theoretical neighbor—it identifies stochastic drift from canonical solution paths as the causal mechanism of long-horizon failure, using path adherence as the early-warning signal. The differentiation argument: 'Canonical Path Deviation detects drift post-hoc using trajectory-completion statistics (significance emerges only at 75% completion); CascadeWatch targets cascade onset proactively at steps 5–15 using a trained probe on prefix embeddings + recoverability-delta, enabling intervention before the 75% threshold. Moreover, canonical path adherence requires knowing the canonical path—requiring either multiple successful runs or a verifier—while CascadeWatch's recoverability proxy is computable from single trajectories.'\n\n2. **Cite arXiv 2603.04474 (From Spark to Fire) in 1–2 sentences.** 'From Spark to Fire [citation] proposes a genealogy-graph governance layer for cascade mitigation in multi-agent collaboration; CascadeWatch addresses a structurally different failure mode—cognitive cascade failure in single-agent long-horizon tasks—using trajectory-prefix probes with recoverability signals rather than message-level graph analysis.'\n\n3. **Fix the 'any frozen agent' claim.** Change to: 'CascadeWatch requires no modification to the base agent; deploying it with a new LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself.'\n\n4. **Reframe the primary empirical claim.** The headline result should be: 'CascadeWatch achieves [X]pp task success rate improvement over no-correction on ALFWorld and [Y]pp on GAIA, while avoiding the degradation caused by generic critics (Intervention Paradox) on both benchmarks.' The ≥3% F1 ablation threshold becomes the validation gate for including recoverability-delta features, not the primary claim.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MODERATE — Trajectory Guard (arXiv 2601.00516, AAAI TrustAgent Workshop 2026) is not cited despite direct framing overlap. The paper proposes a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss for real-time anomaly detection in agentic AI trajectories, achieving F1 0.88–0.94 while running 17–27× faster than LLM Judge baselines at 32ms inference. CascadeWatch must cite and differentiate: (a) Trajectory Guard detects general structural anomalies via reconstruction error, not cascade-specific onset via recoverability-delta signals; (b) it evaluates on security audit failures (RAS-Eval) and multi-agent systems (Who&When), not single-agent long-horizon tasks (ALFWorld, GAIA); (c) it provides no rollback or correction mechanism. These distinctions are clear and defensible, but leaving Trajectory Guard uncited risks a reviewer objection on related-work coverage.\", \"MODERATE — The claim 'Qwen/Qwen3-32B; the largest official open-weights model in the Qwen3 family' is factually incorrect. Qwen3-235B-A22B is an official open-weight MoE model published at Qwen/Qwen3-235B-A22B on HuggingFace under Apache 2.0 with 235B total parameters — larger than Qwen3-32B. The correct claim is 'the largest official open-weights dense model in the Qwen3 family' (the 32B is justified by fitting in 1× H100-80GB BF16 without quantization, not by being the absolute largest). Alternatively, drop the superlative entirely and state: 'We use Qwen/Qwen3-32B (32B dense model, 64GB BF16, fits in 1× H100-80GB without quantization).'\", \"MINOR — The GAIA training data regime (~27 samples per fold after 3-fold CV on 50 total trajectories) is acknowledged only in the resource_estimate risk_note, not in the methods or experiment design sections. The paper body should explicitly state that the GAIA cascade probe operates near the minimum viable supervised learning regime and frame GAIA results as preliminary evidence, with ALFWorld (100 trajectories, ~67 per fold) providing the primary evidence base for the main claim.\"]\nFeedback: Round 4 has cleanly addressed all four targeted issues from Round 3. Canonical Path Deviation is now extensively cited with technically precise differentiation (single-trajectory vs. multi-run signals, proactive vs. retrospective detection, targeted rollback vs. full restart). From Spark to Fire is differentiated on structural grounds (inter-agent vs. single-agent cascade). The 'any frozen agent' claim is corrected. The primary empirical claim is reframed as task success rate improvement. The ALFWorld rollback is technically correct (command-replay from env.reset(), Glulx API limitation acknowledged, Crab rationale clarified). Three short fixes will bring this to pass:\n\n1. **Add one Trajectory Guard sentence to §Related Work**: 'Trajectory Guard [arXiv 2601.00516] uses a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss to detect trajectory anomalies in agentic AI at 32ms, but targets general structural anomalies rather than cascade-specific onset via recoverability signals, evaluates on security audit and multi-agent benchmarks (not ALFWorld/GAIA), and provides no rollback mechanism.' This citation is necessary because its framing ('lightweight inference-time monitoring of agentic trajectories') directly overlaps with CascadeWatch's positioning.\n\n2. **Fix Qwen3-32B superlative**: Remove 'the largest official open-weights model in the Qwen3 family.' Replace with 'Qwen/Qwen3-32B (32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization).' The 235B MoE model is also official and is larger; the superlative will draw reviewer scrutiny.\n\n3. **Disclose GAIA data regime in §Experiments**: Add one sentence: 'The GAIA subset (50 trajectories, ~27 training samples per fold) operates near the minimum viable supervised regime; GAIA results are treated as preliminary evidence, with ALFWorld (100 trajectories) providing the primary evidence base for the main cascade-avoidance claim.'\n\n### Round 5 review\nVerdict: revise\nIssues: [\"MODERATE — InferAct (arXiv 2407.11843, EMNLP 2025 main track, pages 222–244) is uncited despite being published at the exact target venue and explicitly framing its contribution as 'preemptive detection and correction of misaligned actions in LLM agents.' It uses Theory-of-Mind reasoning (Task Inference Unit + Task Verification Unit) to detect misaligned agent actions before execution and achieves up to 20% Marco-F1 improvement over baselines. EMNLP 2026 reviewers will know this paper and its absence will be a red flag. The distinction from CascadeWatch is real — InferAct targets single-step action misalignment with user intent (e.g., executing a buy action without user authorization) via ToM belief reasoning and requires human-in-loop correction via user alerts; CascadeWatch targets multi-step cascade propagation onset via trajectory-prefix ERR recoverability signals and triggers automated rollback — but these distinctions must be stated explicitly in related work.\", \"MINOR — MASC (arXiv 2510.14319, October 2025, revised January 2026) — 'Metacognitive Self-Correction for Multi-Agent System via Prototype-Guided Next-Execution Reconstruction' — explicitly targets cascading errors in agent systems using history-conditioned embedding anomaly scoring (Next-Execution Reconstruction + Prototype-Guided Enhancement) to trigger step-level correction, achieving +8.47% AUC-ROC on the Who&When benchmark. Though MASC is multi-agent (not single-agent), it uses an embedding-based cascade-targeting mechanism structurally related to CascadeWatch's frozen embedding probe, and its explicit 'cascading errors' framing partially occupies CascadeWatch's conceptual space. A 1–2 sentence mention with differentiation (multi-agent vs. single-agent; unsupervised reconstruction vs. supervised ERR-motivated cascade labels; Who&When vs. ALFWorld/GAIA) is needed to complete the landscape coverage.\"]\nFeedback: All three Round 4 fixes are cleanly implemented. The paper is close to pass-ready. Two targeted additions will close the remaining reviewer exposure:\n\n1. **Add InferAct to §Related Work (required):** 'InferAct [arXiv 2407.11843, EMNLP 2025] uses Theory-of-Mind reasoning to detect actions misaligned with user intent before execution and alerts users for correction, achieving up to 20% Marco-F1 improvement. InferAct addresses single-step action misalignment — whether a specific upcoming action matches user authorization — and relies on human-in-loop correction via user alerts. CascadeWatch addresses a structurally different failure mode: multi-step cascade propagation, where an early-step error compounds across subsequent trajectory steps regardless of user intent; our detection uses trajectory-prefix ERR recoverability signals rather than ToM belief inference, and our intervention is automated rollback rather than human alerting.' This distinction is accurate and defensible; the citation is necessary.\n\n2. **Add MASC to §Related Work (recommended, 1–2 sentences):** 'MASC [arXiv 2510.14319] proposes metacognitive self-correction for multi-agent systems via Prototype-Guided Next-Execution Reconstruction, detecting cascading errors at step level via history-conditioned embedding anomaly scoring and triggering correction agents; CascadeWatch differs in targeting single-agent long-horizon cognitive cascades using supervised ERR-motivated recoverability labels (not unsupervised reconstruction) and evaluating on ALFWorld/GAIA rather than the Who&When multi-agent benchmark.'\n\n### Round 6 review\nVerdict: revise\nIssues: [\"CRITICAL — TrajAD (arXiv 2602.06443, 'Trajectory Anomaly Detection for Trustworthy LLM Agents') is an uncited competitor that evaluates on ALFWorld, GAIA, AND WebShop — the exact same benchmark set as CascadeWatch — and explicitly states rollback-and-retry is essential for error recovery, using a specialized verifier trained with fine-grained process supervision. EMNLP reviewers will recognize this paper. The differentiation argument exists (TrajAD uses synthetic TrajBench perturbation labels for general anomaly detection; CascadeWatch uses AgentErrorBench's expert-annotated cascade root-causes with ERR recoverability deltas for cascade-specific onset detection; TrajAD's approach is retrospective error localization while CascadeWatch's step ≥ 5 threshold proactively targets the cascade-propagation window that the Intervention Paradox identifies as the high-risk regime), but it must be stated explicitly in §Related Work.\", \"CRITICAL — InferAct (arXiv 2407.11843, EMNLP 2025 main track, pages 222–244) remains uncited despite being flagged as required in Round 5. It evaluates on ALFWorld (among other benchmarks), is published at the exact target venue, and is preemptive detection with correction — a direct framing overlap. The absence of this citation after two review rounds of flagging will draw immediate reviewer scrutiny.\", \"MODERATE — MASC (arXiv 2510.14319) remains uncited despite being recommended in Round 5. Its history-conditioned embedding anomaly scoring for cascading errors in multi-agent systems partially occupies CascadeWatch's conceptual space and uses Who&When (not ALFWorld/GAIA) as its benchmark, making differentiation straightforward but necessary.\"]\nFeedback: Round 6 submission has made no additions relative to Round 5's required citations — InferAct and MASC are still absent. Additionally, a new high-priority competitor (TrajAD) has been independently identified that evaluates on the same benchmark triple (ALFWorld, GAIA, WebShop) with explicit rollback-and-retry. Three targeted additions are needed:\n\n1. **Add TrajAD to §Related Work (highest priority, newly identified):** 'TrajAD [arXiv 2602.06443] proposes a specialized verifier trained with fine-grained process supervision for trajectory anomaly detection on ALFWorld, GAIA, and WebShop, explicitly enabling rollback-and-retry on error localization. TrajAD is a general-purpose anomaly detector: it uses synthetic TrajBench perturbation labels covering diverse procedural deviations, not cascade-specific annotations tied to confirmed failure propagation. CascadeWatch differs in three ways: (1) detection is cascade-onset specific rather than general-anomaly — using ERR Efficiency Score recoverability deltas as the distinguishing signal for compounding-cost prefixes, not reconstruction deviation; (2) training labels come from AgentErrorBench expert root-cause annotations with the confirmed-cascade criterion (trajectory fails AND root-cause before midpoint), not synthetic perturbations; (3) the step ≥ 5 minimum intervention threshold is specifically calibrated to the Intervention Paradox finding that all observed regressions occur at step ≤ 2, a constraint TrajAD does not impose.'\n\n2. **Add InferAct to §Related Work (required, carried from Round 5):** 'InferAct [arXiv 2407.11843, EMNLP 2025] uses Theory-of-Mind reasoning to detect single-step actions misaligned with user intent before execution on WebArena, ALFWorld, and HotpotQA, achieving up to 20% Marco-F1 improvement. InferAct addresses misalignment between the upcoming action and user authorization — whether a specific action matches user intent — and relies on human-in-loop correction via alerts. CascadeWatch addresses a structurally different failure mode: multi-step cascade propagation, where an early-step cognitive error compounds across subsequent trajectory steps independent of user intent; our detection uses trajectory-prefix ERR recoverability signals rather than ToM belief inference, and our intervention is automated targeted rollback rather than human alerting.'\n\n3. **Add MASC in 1–2 sentences (recommended, carried from Round 5):** 'MASC [arXiv 2510.14319] detects cascading errors in multi-agent systems via Prototype-Guided Next-Execution Reconstruction with unsupervised embedding anomaly scoring on Who&When; CascadeWatch targets single-agent long-horizon cognitive cascades using supervised ERR-motivated recoverability labels (not unsupervised reconstruction) on ALFWorld and GAIA.'\n\n### Round 7 review\nVerdict: revise\nIssues: [\"MODERATE — Cascade label derivation for synthetic trajectories is unspecified: the confirmed-cascade criterion requires identifying the 'earliest annotated root-cause error step' for each trajectory, but the 5K synthetic rollouts from Qwen/Qwen3-32B have no expert annotations. If the automated label proxy for synthetic trajectories is 'trajectory fails AND some heuristic for early-step failure' (e.g., any step k before midpoint in a failed trajectory), this introduces systematic label noise that differs from the expert-annotated criterion used for the 200 real trajectories. The paper must explicitly state how cascade labels are derived for synthetic data — either the same confirmed-cascade criterion (which is impossible without root-cause annotation) or a degraded proxy (which must be acknowledged and its error rate estimated).\", \"MODERATE — WebShop omission weakens TrajAD comparison: TrajAD evaluates on ALFWorld, GAIA, AND WebShop; CascadeWatch's 'optional extension' framing for WebShop means the head-to-head comparison with the closest benchmark competitor is incomplete on a full third of its evaluation surface. EMNLP reviewers familiar with TrajAD will flag this. Either (a) commit to WebShop in the primary evaluation (adding ~15–25 H100-hours, which still fits within the 200-hour HIL constraint), or (b) explicitly acknowledge in the paper that the comparison is partial and that TrajAD's WebShop performance remains uncontested by CascadeWatch.\", \"MINOR — The expected number of cascade-positive examples from the 200 AgentErrorBench trajectories after applying the confirmed-cascade filter is never stated. ALFWorld has a baseline failure rate of 5.8–14.7% (per the Intervention Paradox paper), suggesting most trajectories succeed, but AgentErrorBench likely oversamples failures. Estimating that, say, 60–80 of 100 ALFWorld trajectories are failure trajectories and perhaps 40–60 pass the confirmed-cascade criterion (root-cause before midpoint) gives ~40–60 cascade-positive training examples before augmentation — this should be stated explicitly to give readers confidence in the probe's training signal without relying solely on the 5K synthetic expansion.\", \"MINOR — The Intervention Paradox's specific finding that 'all observed regressions occur at step ≤ 2' is stated as a key empirical fact grounding the step ≥ 5 threshold, but this claim is from a paper that evaluated specific benchmarks (HotPotQA, GAIA, ALFWorld) with a specific critic type. It would strengthen the paper to note whether this step-≤-2 regression finding applies uniformly across all benchmarks evaluated in that paper, or only to specific ones, to ensure the step ≥ 5 threshold is correctly calibrated for ALFWorld and GAIA specifically.\"]\nFeedback: The Round 7 submission cleanly addresses all three Round 6 critical issues — TrajAD is now extensively differentiated across four dimensions (training labels, anomaly target with Intervention Paradox awareness, architecture, recoverability signal); InferAct is cited with three substantive distinctions; MASC is differentiated on multi-agent vs. single-agent and supervised vs. unsupervised. Independent verification found no unaddressed competitor papers: the four papers I investigated (Failure is Feedback, Agent Banana, AgentEval, WebRollback) are either in different domains (multimodal retrieval, image editing), post-hoc evaluation frameworks, or web-specific rollback without cascade detection. Two targeted changes are needed for Round 8:\n\n1. **Specify the cascade label derivation procedure for synthetic trajectories (required).** The confirmed-cascade criterion requires expert-annotated root-cause steps, which don't exist for the 5K synthetic rollouts. Add one explicit paragraph: state whether synthetic trajectories are labeled using (a) an automated root-cause approximation (e.g., step where cumulative reward delta first becomes negative), (b) trajectory-level failure labels only (cascade-positive = any step k < ⌊N/2⌋ in a failed trajectory), or (c) held to the same confirmed-cascade standard (in which case, how?). If (b), acknowledge that synthetic labels are coarser than AgentErrorBench expert labels and the probe trains on a mixture of high-precision real labels and lower-precision synthetic labels — this is an important methodological caveat.\n\n2. **Resolve the WebShop evaluation gap (required for TrajAD comparison integrity).** The simplest resolution: add WebShop to the primary HIL evaluation plan. An additional ~15–25 H100-hours brings the total to ~65–100 H100-hours, still well within the 200-hour constraint and within the 12–14 day timeline (WebShop evaluation runs in parallel with GAIA evaluation). This makes the CascadeWatch vs. TrajAD comparison complete on the exact benchmark triple TrajAD uses. If WebShop is genuinely not feasible, change the framing from 'optional extension' to 'out-of-scope negative result: CascadeWatch's context-only rollback for WebShop (which cannot undo submitted searches) makes it a poor fit for this benchmark's action-irreversibility profile, unlike TrajAD's rollback-and-retry which is evaluated there.'\n\n### Round 8 review\nVerdict: revise\nIssues: [\"MODERATE (potentially CRITICAL) — TrajAD benchmark claim is unverified: The submission states TrajAD 'evaluates on ALFWorld, GAIA, and WebShop—the same benchmark set as CascadeWatch,' enabling a 'direct head-to-head comparison.' But the actual arXiv 2602.06443 abstract and HTML indicate TrajAD introduces its own TrajBench (a dataset synthesized via Perturb-and-Complete) and does not appear to evaluate on ALFWorld, GAIA, or WebShop. If TrajAD evaluates on TrajBench only, then (1) the 'identical benchmark triple' claim is false, (2) the 'direct head-to-head' framing must be changed to 'methodology comparison on different benchmarks,' and (3) TrajAD remains a relevant related work for architectural contrast but not a head-to-head baseline. The full TrajAD paper PDF must be checked; if TrajBench-only, reframe TrajAD as 'the most similar concurrent methodology' (not same-benchmark competitor) and compare methods on their respective reported metrics rather than claiming head-to-head.\", \"MODERATE — Internal rollout count inconsistency across sections: the approach section states '~2,000 synthetic rollouts sampled at two temperatures'; the HIL scope note states '2,000 total at 2 temperatures (T=0.7, T=1.0)'; the compute breakdown states '2K rollouts × 2 temperatures = 4K trajectories; ~1K ALFWorld + 1K GAIA + 1K WebShop per temperature.' The per-temperature breakdown (1K × 3 benchmarks = 3K per temperature × 2 temperatures = 6K total) contradicts both '2K total' and '4K trajectories.' One consistent number must appear throughout: if the intent is 2K total (≈333 per benchmark per temperature), the per-temperature breakdown should read '~333 ALFWorld + ~333 GAIA + ~333 WebShop'; if the intent is 4K total (≈667 per benchmark per temperature), the approach section should say '~4,000 synthetic rollouts.' The compute estimate (~15–20 H100-hours) should also be recalculated against the correct total.\", \"MODERATE — Real-vs-synthetic label granularity mismatch is acknowledged but understated: the paper says synthetic labels are 'coarser,' but the actual structural difference is more consequential. Real cascade-onset labels from AgentErrorBench are maximally sparse: exactly ONE step per trajectory receives label 1 (the expert-annotated root-cause step), all others receive 0. Synthetic cascade labels are maximally dense: ALL steps k ≤ ⌊N/2⌋ of every failed synthetic trajectory receive label 1. Training a 2-layer MLP on this mixed distribution creates a fundamental learning inconsistency: the probe trained on real data must learn 'fire only at the specific cascade-onset step'; the probe trained on synthetic data must learn 'fire throughout the early trajectory of any failing run.' These are different decision boundaries. The paper should name this conflict explicitly ('label density mismatch') rather than just calling synthetic labels 'coarser,' and should add a sentence explaining what the probe is expected to learn from the mixture: 'the mixed corpus trains the probe to distinguish cascade-onset prefixes from successful-trajectory prefixes (from real labels) while learning failure-mode diversity from synthetic trajectories at the cost of false cascade-onset signal at non-root-cause early steps.'\"]\nFeedback: Round 8 has addressed both Round 7 required changes: synthetic cascade label derivation is now explicitly specified (trajectory-level failure proxy for synthetic data, with AgentErrorBench-only ablation arm to quantify noise), and WebShop is now included in the primary HIL evaluation. The Intervention Paradox calibration, ALFWorld command-replay rollback, and all prior related-work citations are cleanly maintained. Three targeted changes are needed for Round 9:\n\n1. **Verify and correct the TrajAD benchmark claim (highest priority).** Fetch the full TrajAD PDF and confirm whether it evaluates on ALFWorld, GAIA, and WebShop or exclusively on TrajBench. If TrajBench-only: remove 'evaluates on ALFWorld, GAIA, and WebShop' from the TrajAD description; replace 'enabling a direct head-to-head comparison' with 'enabling a methodology comparison — CascadeWatch and TrajAD address the same detection problem but on different evaluation surfaces'; retain TrajAD in the baseline set as 'a TrajAD-style general anomaly detector trained on the same CascadeWatch benchmarks using synthetic perturbation labels, ablating cascade-specific precision against general-purpose detection.' This reframing preserves the scientific comparison while being accurate about TrajAD's own evaluation scope.\n\n2. **Resolve the rollout count inconsistency.** Pick one number consistently: either 2K total (≈333/benchmark/temperature, light augmentation) or 4K total (≈667/benchmark/temperature, moderate augmentation). Update the approach section, scope note, compute breakdown, and per-benchmark per-temperature figures to match. Recompute the 15–20 H100-hour rollout estimate against the correct total.\n\n3. **Add one sentence naming the label density mismatch explicitly.** In the training data paragraph, after acknowledging the methodological caveat, add: 'Concretely, real cascade-onset labels are maximally sparse (one positive-labeled step per trajectory, at the expert-annotated root-cause step) while synthetic labels are maximally dense (all first-half steps of each failed trajectory receive cascade-positive labels); the MLP trained on the mixture must reconcile these as a label density mismatch rather than a smoothly graded precision difference. The AgentErrorBench-only ablation arm isolates whether the probe learns cascade-specific onset patterns or merely learns to fire throughout early failed-run prefixes.'\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-09T20:15:07.651Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-09T20:15:07.651Z",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-09T20:15:07.676Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-09 (UTC).**

Your job: independently verify this idea's claims via WebSearch, then issue a verdict.

## User requirements
The user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: LLM Agents.

Direction: LLM Agents — planning algorithms, memory architectures, tool use, multi-agent coordination, agent training (SFT/RL), self-correction in agentic loops, environment feedback exploitation.

Contribution type: METHOD ONLY. Must propose a concrete new algorithm, training procedure, or inference-time mechanism. Reject pure benchmark / dataset / analysis ideas. Method + analysis OK if analysis validates the method.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total (baselines + method + ablations). Show the math.
2. Time: ≤16 days. Build on existing OSS agent codebases (AutoGen, LangGraph, OpenManus, etc.) — no from-scratch systems.
3. Eval: existing benchmarks only — AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench.

Avoid: generic ReAct variants, plain tool retrieval, naive memory summarization. Look for: agent training with minimal RL budget, structured planning beyond flat CoT, multi-agent communication protocols, agent self-verification mechanisms.

Tag: direction=agent, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].**
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
4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-09?
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
  "title": "CascadeWatch: Cascade-Onset Detection with Targeted Rollback for Long-Horizon Agent Tasks",
  "core_problem": "In long-horizon agent tasks, individual early-step errors produce cascading downstream failures that grow exponentially more costly to correct with each additional step. The core question is whether a lightweight trained monitor can prospectively detect cascade onset—predicting failure propagation before it fully manifests—to trigger targeted rollback rather than reactive reflection or full replanning. The challenge is not simply detecting failure: the Intervention Paradox (arXiv 2602.03338) establishes that generic critics with AUROC 0.94 cause up to 26 percentage point performance degradation by triggering on non-cascade failures that the agent would have self-corrected. The disruption-recovery tradeoff (Δ Success = p·r − (1−p)·d) only favors intervention on high-failure benchmarks like ALFWorld; it degrades GAIA and HotPotQA even with accurate critics. The solution is not a better generic critic but a cascade-specific one: targeting only the recoverability-degrading prefix patterns that precede confirmed cascades—detectable via recoverability proxy signals—to achieve the high precision (low d) and focused recall (high p conditional on cascade-onset) that shifts the threshold in favor of intervention. A natural alternative early-warning signal is canonical path deviation (arXiv 2602.19008): measuring Jaccard similarity of tool invocations against the convergent set shared across successful runs. This signal is empirically validated but requires aggregating tool invocation sequences from multiple successful runs per task, making it unavailable for novel tasks or low-success-rate settings. CascadeWatch uses ERR Efficiency Score recoverability deltas (arXiv 2601.22352) approximated as running prefix statistics over the agent's tool-call/result sequence without reference to other runs, enabling cascade detection in the absence of precomputed canonical paths. The rollback mechanism varies by environment affordance: for text-game environments (ALFWorld), full environment-state rollback is achieved via command-replay from env.reset(); for tool-augmented environments (WebShop, GAIA), context-only rollback rewinds the agent's context window. Neither mechanism requires a non-existent API; both are acknowledged to have environment-specific costs and limitations.",
  "opportunity": "The cascade failure pattern is now well-characterized and trainable. AgentErrorBench (arXiv 2509.25370) provides the first systematically annotated failure taxonomy across ALFWorld, WebShop, and GAIA, with expert root-cause step annotations (critical_failure_step field, annotated by ten graduate students at Cohen's κ = 0.55) identifying where cascades originate; the dataset contains 100 ALFWorld, 50 GAIA, and 50 WebShop trajectories, all of which are failure trajectories by design (failures are deliberately oversampled). Memory and reflection errors at steps 5–15 are the most common cascade initiators, crucially occurring mid-trajectory rather than at the earliest steps where the Intervention Paradox shows all regressions occur. The ERR paper (arXiv 2601.22352) formalizes recoverability as Expected Recovery Regret and derives a measurable Efficiency Score proxy, empirically validated across five benchmarks to within δ ≤ 0.05 of observed post-failure regret—establishing that step-level recoverability is observable from trajectory prefixes and thus learnable as a predictive signal. This signal applies directly to tool-augmented agents (WebShop, GAIA) where structured tool-call/result pairs provide natural Efficiency Score observables as running prefix estimates; for text-game environments (ALFWorld), where failures are cognitive planning errors rather than tool execution failures, a domain-adapted proxy (step-level game score delta) is used instead, acknowledged as a heuristic extension. Canonical Path Deviation (arXiv 2602.19008) provides independent corroboration of the self-reinforcing cascade mechanism in long-horizon tool-use tasks: each off-canonical tool invocation raises the probability that the next invocation is also off-canonical by 22.7 percentage points, confirming that cascade propagation is empirically measurable and compounding. CascadeWatch uses recoverability signals rather than canonical path adherence specifically because recoverability deltas are approximable from a single trajectory prefix, enabling deployment where canonical paths from multiple successful runs are unavailable. BacktrackAgent (arXiv 2505.20660, EMNLP 2025) demonstrates that backtracking triggers improve GUI agent task completion on Mobile3M and Auto-UI benchmarks, but requires constructing a task-specific training dataset and fine-tuning the agent components—leaving a clear gap for an external, training-free cascade monitor that operates on any frozen agent in cognitive long-horizon tasks. The proactive detection landscape now includes TrajAD (arXiv 2602.06443) for general trajectory anomaly detection on TrajBench (a synthesized benchmark; rollback-and-retry is described as an intended downstream benefit but is not empirically evaluated for task success improvement), InferAct (arXiv 2407.11843, EMNLP 2025) for single-step action misalignment detection with human alerting on ALFWorld/WebArena, ProMAS (arXiv 2603.20260) for multi-agent error attribution, ProbGuard (arXiv 2508.00500) for physical safety monitoring, Trajectory Guard (arXiv 2601.00516) for general structural anomaly detection in agentic trajectories, and ErrorProbe (arXiv 2604.17658) for offline step-level cascade diagnosis in multi-agent systems, but none combines cascade-specific onset detection using recoverability signals with a step-threshold calibrated to the Intervention Paradox, empirically evaluated task success improvement on ALFWorld/GAIA/WebShop, and automated targeted rollback. The labeled failure datasets, recoverability signals, and the Intervention Paradox's threshold formula together make a specific, testable hypothesis: a cascade-specific monitor using recoverability signals and a step ≥ 5 threshold will achieve sufficiently higher precision than generic critics and general anomaly detectors to make rollback net-positive on benchmarks where generic critics fail, for the first time.",
  "landscape": "Proactive monitoring is an active and crowded area that must be navigated carefully.\n\nTrajAD (arXiv 2602.06443, February 2026) is the closest methodological neighbor and must be explicitly differentiated. TrajAD fine-tunes Qwen3-4B with QLoRA (affecting 1.8% of parameters) on TrajBench, a purpose-built benchmark of 63,484 balanced samples synthesized via a 'Perturb-and-Complete' pipeline from AgentBank across five domains (reasoning, mathematics, coding, web navigation, embodied AI), covering three anomaly types: Task Failure (reasoning errors, invalid tool parameters), Process Inefficiency (redundant loops and detours), and Unwarranted Continuation (failure to stop after task completion). TrajBench labels are generated synthetically through controlled perturbation injection, not expert cascade root-cause annotation. TrajAD frames detection as a joint classification-and-localization task, outputting both a binary verdict and the predicted first-error step index (Joint Exact Match: 53.75% vs. 5.81% for the best zero-shot baseline; Macro-F1: 81.81% vs. 70.43%). The paper describes rollback-and-retry as an intended downstream benefit of precise error localization, but does not empirically evaluate whether rollback improves task success rate on any downstream benchmark; TrajAD's evaluation is exclusively on anomaly detection and localization metrics (F1, JEM) on TrajBench. TrajAD does not evaluate on ALFWorld, GAIA, or WebShop in their standard agentic task-completion form. Five distinctions separate TrajAD from CascadeWatch. (1) Training labels: TrajAD's TrajBench uses synthetic perturbations; CascadeWatch trains on AgentErrorBench expert root-cause annotations with the confirmed-cascade criterion (trajectory fails AND root-cause step before midpoint), learning from real cascade failures with verified propagation, not synthetic deviations. (2) Anomaly target and Intervention Paradox awareness: TrajAD's 'Process Inefficiency' category—loops and detours that are semantically valid but suboptimal—is precisely the class of self-correctable deviations that the Intervention Paradox (arXiv 2602.03338) shows causes performance degradation when interrupted; triggering on these raises d in the disruption-recovery tradeoff (Δ Success = p·r − (1−p)·d) and explains why generic critics with AUROC 0.94 still degrade performance. CascadeWatch targets only recoverability-degrading cascade-onset prefixes (not process inefficiencies or unwarranted continuations), and imposes a step ≥ 5 minimum threshold specifically calibrated to the Intervention Paradox's empirical finding that all observed regressions occur at steps 0–1 (on HotPotQA and GAIA; ALFWorld is the exception where early intervention yields modest gains). TrajAD has no step threshold and does not reference or address the Intervention Paradox. (3) Architecture: TrajAD fine-tunes a 4B model via QLoRA, modifying model weights and requiring backbone-level training infrastructure. CascadeWatch trains a 2-layer MLP probe on frozen Qwen/Qwen3-32B embeddings combined with ERR recoverability deltas, requiring no modification to the base agent; deploying on a different backbone requires retraining only the MLP probe (~3–5 H100-hours). (4) Recoverability signal: TrajAD introduces no ERR-motivated recoverability channel; CascadeWatch's ERR Efficiency Score running prefix estimates specifically measure the compounding cost of cascade continuation, providing a principled signal for distinguishing cascade-onset from recoverable anomalies. (5) Task success evaluation: TrajAD evaluates exclusively on anomaly detection metrics (F1, JEM) on TrajBench; CascadeWatch evaluates task success rate improvement on ALFWorld, GAIA, and WebShop, directly measuring whether cascade-specific rollback is net-positive in the Intervention Paradox regime. CascadeWatch and TrajAD address overlapping detection problems on different evaluation surfaces; direct metric comparison is not possible across evaluation surfaces. To enable direct comparison on identical data, CascadeWatch's baseline set includes a TrajAD-style general anomaly detection condition: a general anomaly detector trained on synthetic perturbation labels on the same CascadeWatch benchmarks (ALFWorld/GAIA/WebShop), without a step threshold or ERR recoverability signal, directly testing cascade-specific precision against general-purpose detection in the Intervention Paradox regime.\n\nInferAct (arXiv 2407.11843, EMNLP 2025 main track, pages 222–244) uses Theory-of-Mind reasoning grounded in LLM belief inference to detect single-step actions misaligned with user intent before execution on WebArena (web shopping), ALFWorld (household tasks), and HotpotQA (question answering), achieving up to 20% Marco-F1 improvement over baselines. When misalignment is detected, InferAct alerts users for timely correction. Three distinctions separate InferAct from CascadeWatch. (1) InferAct addresses the single-step mismatch between an upcoming action and user authorization—whether a specific action matches what the user intended to authorize (e.g., accidental 'buy-now' triggering); CascadeWatch addresses multi-step cascade propagation, where an early-step cognitive error (steps 5–15) compounds across subsequent trajectory steps independent of any user authorization issue. (2) InferAct's detection signal is ToM belief inference over user intent; CascadeWatch's detection signal is trajectory-prefix ERR Efficiency Score running estimates over cascade-onset patterns, a fundamentally different feature channel targeting compounding-cost propagation rather than intent alignment. (3) InferAct's intervention is human alerting, requiring a human in the loop to correct the misaligned action; CascadeWatch's intervention is automated targeted rollback with a false-positive circuit-breaker (max 2 rollbacks per episode), requiring no human involvement. Published at EMNLP 2025—the primary target venue for CascadeWatch—InferAct is a direct framing overlap that must be cited, but the single-step authorization framing vs. multi-step cascade propagation distinction is substantive.\n\nMASC (arXiv 2510.14319) detects cascading errors in multi-agent systems via Prototype-Guided Next-Execution Reconstruction: it forecasts subsequent step embeddings from query and interaction history (Next-Execution Reconstruction) and establishes a prototype prior over normal-step embeddings for stabilized anomaly scoring in sparse contexts (Prototype-Guided Enhancement). Anomaly scoring is unsupervised; when anomalies are flagged, a correction agent revises the acting agent's output before propagating downstream. MASC achieves up to 8.47% AUC-ROC improvement in step-level error detection on the Who&When multi-agent benchmark. Two distinctions separate MASC from CascadeWatch: (1) MASC operates on multi-agent systems where a correction agent revises another agent's output; CascadeWatch operates on single-agent long-horizon trajectories where there is no second agent to correct and the rollback must rewind the agent's own context or environment state. (2) MASC's anomaly scoring is unsupervised (reconstruction-based); CascadeWatch's cascade-onset detection is supervised using expert-annotated root-cause labels and ERR-motivated recoverability signals, enabling principled distinction between cascade-onset and recoverable anomalies.\n\nProMAS (arXiv 2603.20260, March 2026) uses Causal Delta Features mapped to a 30-prototype Vector Markov Space with a frozen Meta-Llama-3.1-8B extractor to predict failure onset in multi-agent collaborative reasoning systems, achieving 22.97% step-level accuracy on the Who&When benchmark (annotated multi-agent dialogues of math and logic puzzles) while processing only 27% of reasoning logs. Critically, ProMAS raises an alert but provides no corrective action—it is a detector only and evaluates exclusively on the Who&When multi-agent attribution benchmark, not on single-agent long-horizon tasks.\n\nErrorProbe (arXiv 2604.17658, April 2026) is a contemporaneous offline diagnostic for multi-agent systems that uses a three-stage pipeline: (1) failure taxonomy-based local anomaly detection, (2) symptom-driven backward tracing to prune irrelevant trajectory context, and (3) a specialized multi-agent verification team (Strategist, Investigator, Arbiter) that validates error hypotheses via tool-grounded execution. ErrorProbe maintains a verified episodic memory of confirmed error/patch patterns and is evaluated on TracerTraj and Who&When benchmarks. Two distinctions separate ErrorProbe from CascadeWatch: (1) ErrorProbe is a post-hoc offline diagnostic tool—its backward tracing and multi-agent verification pipeline is not compatible with real-time inference-time intervention; CascadeWatch is an online monitor that triggers rollback during episode execution. (2) ErrorProbe targets multi-agent systems; CascadeWatch targets single-agent long-horizon trajectory monitoring where no second agent is available for verification.\n\nProbGuard (arXiv 2508.00500) learns a Discrete-Time Markov Chain from symbolic agent-state abstractions with PAC-style guarantees and triggers prompt-injection interventions when P(unsafe state) exceeds a threshold; it predicts traffic violations up to 38.66 seconds ahead and reduces unsafe behavior by 65.37% in embodied agents, but operates on physical safety constraints using symbolic abstractions rather than frozen neural representations or recoverability signals.\n\nTrajectory Guard (arXiv 2601.00516, AAAI TrustAgent Workshop 2026) proposes a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss for real-time anomaly detection in agentic AI trajectories, achieving F1 0.88–0.94 on balanced sets and recall 0.86–0.92 on imbalanced external benchmarks while running 17–27× faster than LLM Judge baselines at 32ms inference. Three distinctions separate this from CascadeWatch: (1) Trajectory Guard detects general structural anomalies—contextual misalignment and sequential incoherence—via reconstruction error, not cascade-specific onset via recoverability-delta signals; (2) it evaluates on synthetic perturbations, security audit failures (RAS-Eval), and multi-agent attribution (Who&When), not on single-agent long-horizon cognitive tasks (ALFWorld, GAIA, WebShop); (3) it provides no rollback or correction mechanism—detection only.\n\nThe ORC auditing paper (ICLR Workshop 2026, arXiv 2603.13325) detects cascading risks in multi-agent systems via Ollivier-Ricci Curvature on completed interaction graphs—post-hoc auditing, not inference-time intervention.\n\nCanonical Path Deviation (arXiv 2602.19008, Feb 2026) is the closest theoretical neighbor to CascadeWatch's cascade-onset framing. Analyzing 515 model-task combinations on the Toolathlon benchmark (22 frontier models, 108 real-world tool-use tasks across 3 independent runs each), Wilson Y. Lee identifies stochastic drift from canonical solution paths—the convergent set of tool invocations shared across successful runs—as a causal mechanism of long-horizon failure. Path adherence is measured as Jaccard similarity between actual and canonical tool invocation sequences; adherence gaps are statistically indistinguishable from zero through the first half of trajectories but become significant and self-reinforcing thereafter, with each off-canonical tool call raising the probability that the next call is also off-canonical by 22.7 percentage points. An intervention restarting the bottom tercile of runs by mid-trajectory canonical adherence achieves +8.8pp success rate improvement. Three distinctions separate this from CascadeWatch: (1) Canonical path adherence requires aggregating tool invocation sequences across multiple successful runs per task—unavailable for novel tasks or low-success-rate settings; CascadeWatch's ERR Efficiency Score running prefix estimates are computable from a single trajectory without reference to other runs. (2) Canonical path deviation detects drift retrospectively via trajectory statistics that become significant only in the second half of execution; CascadeWatch proactively intervenes at steps 5–15 using a trained probe on prefix embeddings, before adherence divergence solidifies. (3) The CPD intervention is a full task restart of lowest-adherence runs; CascadeWatch performs targeted rollback to the pre-cascade checkpoint, preserving valid completed steps and avoiding full re-execution cost.\n\nFrom Spark to Fire (arXiv 2603.04474, March 2026) models cascade error propagation in LLM-based multi-agent collaboration using an individual-based mean-field framework over inter-agent communication graphs, and proposes a genealogy-graph governance layer that tracks atomic claim provenance via NLI-based verification (Green/Red/Yellow status using DeBERTa-v3-small) and blocks transmission of error-carrying messages; the Benign Infection Control Rate improves from 0.32 to 0.89 across Chain, Mesh, and Star multi-agent topologies. The cascade mechanism is specifically inter-agent. CascadeWatch addresses a structurally different failure mode—cognitive cascade failure within a single agent's sequential trajectory—where there are no inter-agent message dependencies.\n\nThe Intervention Paradox (arXiv 2602.03338) is the most important negative result in the space: ROLLBACK and APPEND interventions triggered by a generic LLM critic (AUROC 0.94) degrade performance on HotPotQA by −2.3 to −25.5pp and on GAIA by −4.4 to −30pp; only ALFWorld (high baseline failure rate: 5.8–14.7%) shows improvement (+0.5 to +2.8pp). All observed regressions occur with early-step (steps 0–1) interventions on HotPotQA and GAIA; the paper recommends a minimum-step constraint of min_step ≥ 2. ALFWorld is the exception where early intervention yields positive returns, consistent with the disruption-recovery tradeoff favoring intervention when baseline failure rate exceeds threshold.\n\nBacktrackAgent (arXiv 2505.20660, EMNLP 2025) trains a verifier-judger-reflector pipeline for GUI agents (Mobile3M, Auto-UI benchmarks) to detect individual action errors and trigger backtracking. Unlike CascadeWatch, BacktrackAgent requires constructing a task-specific training dataset and fine-tuning the agent's backtracking components; it targets GUI action-level errors rather than recoverability-degrading cascade onset in cognitive long-horizon tasks.\n\nSelf-Backtracking (arXiv 2502.04404) trains the base LLM to internalize when and where to backtrack during training and inference, achieving over 40% performance gains over optimal-path SFT baselines in general reasoning. This approach requires model retraining and modifies the agent's internal reasoning; CascadeWatch operates as a frozen external probe on any pre-trained agent.\n\nPrior work probes LLM hidden states for single-step answer correctness in mathematical reasoning (arXiv 2504.05419), achieving 24% token reduction via early exit. The mechanism is structurally similar to CascadeWatch's frozen embedding + MLP probe, but targets single-step correctness rather than multi-step cascade onset; it adds no recoverability signal channel.\n\nReactive self-correction methods share the same fundamental limitation: ExpeL and Contextual Experience Replay distill past trajectories for future improvement; self-verification (arXiv 2602.03485) confirms rechecks rarely identify errors; T-STAR (arXiv 2604.07165) achieves training-time divergence detection via Cognitive Trees but adds no inference-time mechanism.\n\nNo existing system combines (1) cascade-specific onset detection using ERR recoverability signals, (2) a step ≥ 5 threshold explicitly calibrated to the Intervention Paradox and AgentErrorBench's cascade-onset distribution, (3) expert-annotated cascade labels (not synthetic perturbations), (4) empirically evaluated task success improvement on ALFWorld/GAIA/WebShop (not anomaly detection metrics alone), and (5) environment-appropriate targeted rollback with a false-positive circuit-breaker—nor validates that cascade-specific precision avoids the disruption-recovery tradeoff that defeats all general-purpose critics and general anomaly detectors.",
  "approach": "We train CascadeWatch to address the Intervention Paradox by targeting only the recoverability-degrading mid-trajectory patterns that precede confirmed cascades. Training data: AgentErrorBench's 200 expert-annotated trajectories (davide221/agenterrorbench on HuggingFace, spanning ALFWorld, WebShop, and GAIA; all 200 are failure trajectories by design, expert-annotated by ten graduate students at Cohen's κ = 0.55) augmented with ~2,000 synthetic rollouts total from Qwen/Qwen3-32B (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization) sampled at two temperatures (T=0.7, T=1.0), yielding approximately 333 rollouts per benchmark per temperature across ALFWorld, WebShop, and GAIA, to increase failure-mode diversity.\n\nCascade label derivation differs between real and synthetic trajectories. For the 200 AgentErrorBench trajectories, the confirmed-cascade criterion is applied using the expert-annotated critical_failure_step field: step k is labeled cascade-onset if k equals the annotated root-cause step AND that step occurs before the trajectory midpoint (k ≤ ⌊total_steps / 2⌋). Since all 200 trajectories are failures by design, the midpoint filter is the only active criterion. Given AgentErrorBench's finding that cascade-initiating errors cluster at steps 5–15, and typical episode lengths of 20–40 steps, the majority of annotated root-cause steps fall before the midpoint. Estimated cascade-positive training examples: approximately 65–75 of 100 ALFWorld trajectories, 35–40 of 50 GAIA trajectories, and 35–40 of 50 WebShop trajectories, totaling approximately 135–155 cascade-positive examples before augmentation. For the ~2,000 synthetic rollouts, expert root-cause annotation is unavailable. Synthetic cascade labels use a trajectory-level failure proxy: a synthetic trajectory is labeled cascade-positive at step k if (1) the trajectory ultimately fails AND (2) k ≤ ⌊N/2⌋, where N is total episode length. This proxy is coarser than the confirmed-cascade criterion—it applies the cascade-positive label to all early-half steps of failed trajectories without identifying the specific root-cause step, including steps that precede any actual error. Concretely, real cascade-onset labels are maximally sparse (exactly one positive-labeled step per trajectory, at the expert-annotated root-cause step, with all other steps labeled 0) while synthetic labels are maximally dense (all steps k ≤ ⌊N/2⌋ in each failed trajectory receive cascade-positive labels); this label density mismatch means the MLP trained on the mixture must reconcile two structurally different decision boundaries—'fire only at the specific cascade-onset step' from real labels versus 'fire throughout the early phase of any failing run' from synthetic labels. The training corpus is therefore a deliberate mixture of high-precision real labels (AgentErrorBench expert root-cause annotations, ~135–155 cascade-positive examples) and lower-precision synthetic labels (trajectory-level failure proxy with label density mismatch). This methodological caveat is acknowledged explicitly; an additional ablation trains the probe on AgentErrorBench-only data to quantify the performance ceiling under expert labels alone versus the mixed corpus, and to isolate whether the probe learns cascade-specific onset patterns (from real labels) or merely learns to fire throughout early failed-run prefixes (synthetic density signal).\n\nA minimum intervention threshold of step ≥ 5 is imposed at inference time, grounded in two complementary findings. First, AgentErrorBench's expert annotations show cascade-initiating errors occur primarily at steps 5–15, making cascade-onset detection at k < 5 both empirically impossible (no cascade has yet begun) and mechanistically unnecessary. Second, the Intervention Paradox (arXiv 2602.03338) finds that all regression-causing interventions occur at steps 0–1 on HotPotQA and GAIA, recommending min_step ≥ 2; CascadeWatch's step ≥ 5 threshold is more conservative than this recommendation, providing additional safety margin. Note that ALFWorld is the exception in the Intervention Paradox paper: early intervention yields positive gains on ALFWorld (+0.5 to +2.8pp), consistent with its high baseline failure rate. The step ≥ 5 threshold is therefore over-conservative for ALFWorld specifically—but is retained for consistency across benchmarks and because AgentErrorBench's cascade-onset distribution at steps 5–15 independently grounds the threshold as the earliest step where cascade-positive signal exists. The 50-task pilot test per benchmark will empirically verify whether the threshold is correctly calibrated for each of the three benchmarks.\n\nEach trajectory prefix at step k is represented by concatenating (a) frozen Qwen/Qwen3-32B hidden-state embeddings (mean-pooled last 4 transformer layers over the action–observation sequence) with (b) recoverability delta signals. For WebShop and GAIA (tool-augmented benchmarks with structured tool-call/result pairs), these are running prefix estimates of ERR Efficiency Score deltas as defined in arXiv 2601.22352. Critically, the full ERR Efficiency Score formula (ES = RR / (1 + λC/Cmax)) requires knowing the final trajectory outcome (recovery rate RR), making it not directly computable online. CascadeWatch approximates the recoverability delta at step k using observable prefix quantities: the running cumulative cost ratio C_k/Cmax (estimated from trajectory length against the benchmark's typical maximum) and the incremental milestone completion rate, which serves as a partial recovery rate proxy. These prefix-approximated deltas are the features fed to the probe; the approximation error is bounded by the ERR paper's empirical δ ≤ 0.05 validation result, which confirms that prefix statistics are predictive of final recoverability within this tolerance. For ALFWorld (a text-based game where failures are cognitive planning errors rather than tool execution failures, and which lacks structured tool-call pairs), the domain-adapted proxy is step-level delta in the normalized ALFWorld game score (Δ(info['score'] / info['max_score']) at each step), which tracks incremental subgoal-completion rate. This is an acknowledged heuristic extension of the ERR framework; whether the recoverability motivation holds for this proxy is explicitly tested in the ablation.\n\nA 2-layer MLP probe (with L2 weight decay 1e-4) outputs P(cascade | prefix_k), with Platt scaling applied on a stratified held-out validation split. Training data sparsity is addressed by (i) 3-fold cross-validation stratified by benchmark (ALFWorld / WebShop / GAIA) to estimate generalization without benchmark leakage, and (ii) a parallel logistic probe baseline to assess whether MLP complexity is justified over this small labeled set. The GAIA cascade probe operates near the minimum viable supervised learning regime (~27 training samples per fold in 3-fold CV across ~35–40 GAIA cascade-positive examples); GAIA results are consequently treated as preliminary evidence, with ALFWorld (~65–75 cascade-positive examples, ~43–50 per fold) providing the primary evidence base for the main cascade-avoidance claim.\n\nCascadeWatch requires no modification to the base agent and does not require retraining the agent backbone; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself. This is a meaningful practical advantage over BacktrackAgent, which requires constructing a task-specific training dataset and fine-tuning agent components, and over TrajAD, which fine-tunes a 4B model via QLoRA and must be retrained per backbone.\n\nThe rollback mechanism is specified per benchmark. For ALFWorld, environment-state rollback is performed via command-replay from env.reset(): the TextWorld gym environment is reset to the initial observation, then the k−1 accepted actions from the checkpoint buffer are re-executed sequentially to reconstruct game state at step k−1. The ALFWorld game engine processes each text command in approximately 1–2ms; for typical episodes capped at 50 steps, rollback at step k incurs roughly 25–100ms wall-clock overhead—negligible relative to LLM inference time. A checkpoint buffer stores accepted action sequences at each step to enable replay without re-querying the LLM. Note that TextWorld's Python API does not expose a save/restore mechanism for Glulx-format (.ulx) games used in ALFWorld competition settings, so command-replay is the correct mechanism; the O(k) replay cost is in game-engine steps, not LLM compute. For WebShop and GAIA, context-only rollback rewinds the agent context window to step k_checkpoint, masks all subsequent actions and observations, and re-samples an alternative action with temperature +0.3. Context-only rollback does not undo irreversible WebShop web-state changes (e.g., submitted searches), which is explicitly noted as a limitation; the WebShop simulation environment resets between episodes, so irreversibility affects intra-episode recovery quality but not cross-episode evaluation validity.\n\nA false-positive circuit-breaker limits rollback to a maximum of 2 triggers per episode; after the second trigger, monitoring is suspended for the remainder of the episode to prevent compounding disruption. Before full evaluation, we run the Intervention Paradox's 50-task pilot test on each benchmark to empirically verify that CascadeWatch's cascade-specific intervention is net-positive (p > d/(r+d)) on that benchmark; benchmarks where the pilot test fails are reported as negative results, not omitted.\n\nWe include a pre-registered 4-way ablation: (a) frozen embeddings only → logistic probe, (b) recoverability-delta features only → logistic regression (no embeddings), (c) full CascadeWatch (embeddings + recoverability-delta) → 2-layer MLP, and (d) AgentErrorBench-only training (no synthetic augmentation) → 2-layer MLP, to quantify the noise contribution of the synthetic trajectory-level proxy labels (with their label density mismatch) versus high-precision expert labels. The primary empirical claim is that CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld, GAIA, and WebShop while avoiding the performance degradation caused by generic critics observed in the Intervention Paradox—demonstrating for the first time that cascade-specific precision is sufficient to make rollback net-positive on benchmarks where generic critics fail. The recoverability-delta ablation serves as an internal validation gate: if recoverability-delta provides ≥3% F1 lift over frozen embeddings alone, the ERR-motivated feature design is empirically confirmed; if the lift is <3%, the theoretical ERR motivation weakens substantially and this is reported honestly as a negative result on the recoverability signal hypothesis. We evaluate task success rate, steps saved per episode, and false-positive intervention rate against no-correction, ExpeL-style reflection, self-verification, T-STAR offline, a TrajAD-style general anomaly detection baseline (trained on synthetic perturbation labels on the same CascadeWatch benchmarks without step threshold or ERR signal, re-implementing TrajAD's training methodology on CascadeWatch's evaluation surface), and ProMAS-style detection-only baselines on ALFWorld, WebShop, and GAIA (subject to pilot test results). The TrajAD-style baseline directly tests whether cascade-specific detection (step ≥ 5 threshold + ERR signal + expert labels) outperforms general anomaly detection (no threshold + synthetic labels + process inefficiency triggering) in the Intervention Paradox regime on the identical evaluation surface.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~100-140 H100-hours total: rollout generation ~45 H100-hours (Qwen/Qwen3-32B runs in BF16 on 1× H100-80GB without quantization—32B × 2 bytes ≈ 64GB, within the 80GB VRAM budget; inference throughput roughly doubles relative to a 72B model; ~45h covers ~5K synthetic rollouts across three benchmarks at three temperatures, including environment interaction overhead and tool-call latency for GAIA tasks); probe training ~10 H100-hours (5-fold CV × 4-way ablation × logistic/MLP variants; these are small models, <1h each); evaluation runs ~45–85 H100-hours across three benchmarks + pilot tests (50 tasks × 3 benchmarks × 2 conditions per test). ALFWorld command-replay rollback adds <1 H100-hour overhead across all evaluation episodes.",
      "gpu_utilization": "~30–40% effective utilization; high idle between human coding, debugging, and analysis cycles",
      "timeline": "4–6 months",
      "team": "2 researchers",
      "estimated_gpu_cost": "~$200–$280 at ~$2/H100-hour"
    },
    "human_in_loop": {
      "scope_note": "Compressed to satisfy the joint ≤16-day calendar / ≤200 H100-hour constraint. Primary benchmarks: ALFWorld + GAIA + WebShop (all three, matching TrajAD's intended evaluation surface). Synthetic rollouts: 2,000 total at 2 temperatures (T=0.7, T=1.0), approximately 333 rollouts per benchmark per temperature (333 ALFWorld + 333 GAIA + 333 WebShop per temperature × 2 temperatures = 2,000 total); 3-fold CV. Human gates: cascade label validation (including review of synthetic trajectory-level proxy labeling procedure and label density mismatch implications), pilot test pass/fail judgment per benchmark, ablation design review, threshold decisions. Human engagement: 2–3 hours/day.",
      "compute_breakdown": "Rollout generation (2,000 total rollouts: ≈333 per benchmark per temperature × 2 temperatures × 3 benchmarks): ~8–12 H100-hours (ALFWorld ≈666 rollouts ~1–2h; GAIA ≈666 rollouts ~4–6h including tool-call overhead; WebShop ≈666 rollouts ~2–4h; Qwen/Qwen3-32B BF16 on 1× H100-80GB without quantization). Probe training (3-fold CV × 4-way ablation × logistic/MLP): ~4–6 H100-hours. Pilot tests (50 tasks × 3 benchmarks × 2 conditions × 2 seeds = 600 episodes): ~10–15 H100-hours. Full evaluation (post-pilot, 3 benchmarks × 5 baselines + CascadeWatch): ~35–50 H100-hours. Buffer/debugging: ~5–10 H100-hours. Total: ~62–93 H100-hours.",
      "gpu_hours": "~62–93 H100-hours (well within ≤200 H100-hour constraint)",
      "gpu_utilization": "~60–70% utilization; human approval gates reduce compute waste on dead-end ablations",
      "timeline": "12–14 calendar days (rollout generation days 1–3, labeling + probe training days 2–5, pilot tests with human review days 5–9, full evaluation days 8–12 with GAIA and WebShop evaluations running in parallel, analysis and write-up days 10–14)",
      "team": "1 researcher, ~2–3 hours/day check-in",
      "claude_api_cost": "$150–$250",
      "estimated_gpu_cost": "~$124–$186 at ~$2/H100-hour",
      "risk_note": "Small labeled training set (200 trajectories, all failures) risks MLP overfitting; confirmed-cascade criterion and synthetic proxy labeling strategy are critical human-gate decisions. Synthetic trajectory-level proxy labels are coarser than expert annotations and exhibit label density mismatch (maximally dense vs. maximally sparse real labels); the AgentErrorBench-only ablation (4-way ablation arm d) will quantify this noise and determine whether the probe learns cascade-specific onset or merely fires throughout early failed-run prefixes. GAIA evaluation results should be treated as preliminary evidence (~27 cascade-positive training samples per fold in 3-fold CV) pending replication on a larger annotated set. ALFWorld ERR proxy (game score delta) is a domain adaptation—its F1 contribution must be validated in ablation before committing to full evaluation on ALFWorld. WebShop context-only rollback does not undo irreversible intra-episode web-state changes (submitted searches); this is a limitation of the intervention mechanism, not the detection mechanism, and is explicitly noted. Pilot test (50 tasks × 3 benchmarks) must be reviewed by human before committing to full evaluation on each benchmark."
    },
    "auto_research": {
      "note": "This mode exceeds the primary ≤200 H100-hour constraint and is presented as an extended evaluation scenario for teams with unrestricted compute, not a valid path within the joint 16-day/200 H100-hour constraint. Included for completeness only.",
      "gpu_hours": "~300–450 H100-hours (3–5× more ablations across probe architectures, threshold strategies, feature combinations, augmentation volumes, rollback trigger policies, and minimum-step thresholds; reduced from prior estimates due to Qwen/Qwen3-32B being more compute-efficient than the previously specified 72B model)",
      "gpu_utilization": "~85–95%; near-zero idle as agent continuously queues and launches experiments",
      "timeline": "3–10 days with 4+ H100s in parallel",
      "team": "0 (initial setup only)",
      "claude_api_cost": "$350–$600",
      "estimated_gpu_cost": "~$600–$900",
      "speed_bottleneck": "Number of H100s available; rollout generation dominates throughput",
      "risk_note": "Automated cascade label derivation for synthetic trajectories uses trajectory-level failure proxy (step k ≤ ⌊N/2⌋ in failed trajectories)—coarser than expert confirmed-cascade criterion, with label density mismatch (all early-half steps labeled positive) that the auto-research mode cannot self-correct without human oversight. No human oversight to detect always-predict-cascade degenerate solutions or validate that the synthetic proxy is not systematically mis-labeling self-correcting trajectories. Pilot test pass/fail judgment and Intervention Paradox threshold calculation require human review—an agent may proceed to full evaluation on benchmarks where intervention is net-negative. ALFWorld ERR proxy domain adaptation requires human judgment to validate before scaling."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR deadline May 25, 2026)",
    "AAAI 2027 (abstract deadline expected ~August 2026)"
  ],
  "level": "solid",
  "key_references": [
    "Where LLM Agents Fail and How They can Learn From Failures (arXiv 2509.25370, 2025)",
    "Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents (arXiv 2601.22352, 2026)",
    "The Intervention Paradox: Accurate Failure Prediction in Agents Does Not Imply Effective Failure Prevention (arXiv 2602.03338, 2026)",
    "Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks (arXiv 2602.19008, 2026)",
    "TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents (arXiv 2602.06443, 2026)",
    "InferAct: Inferring Safe Actions for LLM-Based Agents Through Preemptive Evaluation and Human Feedback (arXiv 2407.11843, EMNLP 2025, pages 222–244)",
    "MASC: Metacognitive Self-Correction for Multi-Agent Systems via Prototype-Guided Next-Execution Reconstruction (arXiv 2510.14319, 2025)",
    "Trajectory Guard: A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI (AAAI TrustAgent Workshop 2026, arXiv 2601.00516)",
    "ProMAS: Proactive Error Forecasting for Multi-Agent Systems Using Markov Transition Dynamics (arXiv 2603.20260, 2026)",
    "From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration (arXiv 2603.04474, 2026)",
    "ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety (arXiv 2508.00500, 2025)",
    "Auditing Cascading Risks in Multi-Agent Systems via Semantic–Geometric Co-evolution (ICLR Workshop 2026, arXiv 2603.13325)",
    "Towards Self-Improving Error Diagnosis in Multi-Agent Systems (arXiv 2604.17658, 2026)",
    "Crab: A Semantics-Aware Checkpoint/Restore Runtime for Agent Sandboxes (arXiv 2604.28138, 2026)",
    "Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization (arXiv 2604.07165, 2026)",
    "Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning (arXiv 2602.03485, 2026)",
    "Beyond Fluency: Toward Reliable Trajectories in Agentic IR — position paper on failure modes, not empirical cascade measurement (arXiv 2604.04269, 2026)",
    "BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism (EMNLP 2025, arXiv 2505.20660)",
    "Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models (arXiv 2502.04404, 2025)",
    "Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (arXiv 2504.05419, 2025)"
  ],
  "description": "Long-horizon agent tasks suffer from cascade failures: a single early error propagates across subsequent steps, compounding recovery cost. The critical challenge is the Intervention Paradox (arXiv 2602.03338): a generic critic with AUROC 0.94 causes up to 26 percentage point degradation by disrupting self-correcting trajectories, with all observed regressions occurring at early intervention steps (steps 0–1) on HotPotQA and GAIA—ALFWorld is the exception where early intervention yields modest gains. The solution requires cascade-specific, high-precision detection rather than general failure prediction or general anomaly detection. We propose CascadeWatch, an inference-time monitor that targets cascade onset specifically using frozen Qwen/Qwen3-32B hidden-state embeddings (HuggingFace: Qwen/Qwen3-32B; 32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization) combined with running prefix estimates of ERR Efficiency Score recoverability deltas to estimate P(cascade_failure | prefix_k) at each step, with a minimum trigger threshold of step ≥ 5. This threshold is doubly grounded: (1) AgentErrorBench shows cascade-initiating errors begin at step 5, so cascade-onset detection is mechanistically impossible before step 5; (2) the Intervention Paradox recommends min_step ≥ 2 to avoid regression-causing early interventions—step ≥ 5 is more conservative than this recommendation. For WebShop and GAIA (tool-augmented benchmarks), recoverability deltas are running prefix estimates of ERR Efficiency Score quantities (arXiv 2601.22352), approximated from observable cumulative cost ratios and incremental milestone completion rates without requiring final trajectory outcomes. For ALFWorld (text-based game with cognitive planning errors, not tool execution failures), a domain-adapted proxy is used: step-level delta in the normalized ALFWorld game score, acknowledged as a heuristic extension and isolated in the ablation.\n\nTraining uses AgentErrorBench's 200 expert-annotated trajectories (all failure trajectories by design; ALFWorld: 100, GAIA: 50, WebShop: 50) augmented with ~2,000 synthetic rollouts total (approximately 333 per benchmark per temperature across T=0.7 and T=1.0). Cascade label derivation differs by data source: AgentErrorBench trajectories use the confirmed-cascade criterion (root-cause step before trajectory midpoint per expert critical_failure_step annotation), yielding approximately 65–75 cascade-positive examples from ALFWorld, 35–40 from GAIA, and 35–40 from WebShop (~135–155 total). Synthetic trajectories use a trajectory-level failure proxy (cascade-positive = any step k ≤ ⌊N/2⌋ in a failed trajectory), which exhibits a label density mismatch relative to real labels: real labels are maximally sparse (one positive step per trajectory at the expert-annotated root-cause step) while synthetic labels are maximally dense (all first-half steps of each failed trajectory receive cascade-positive labels). The MLP trained on the mixture must reconcile these as structurally different decision boundaries; a 4-way ablation includes an AgentErrorBench-only arm to determine whether the probe learns cascade-specific onset or merely fires throughout early failed-run prefixes.\n\nCascadeWatch is positioned precisely among nine distinct neighboring systems. (1) TrajAD (arXiv 2602.06443) fine-tunes Qwen3-4B with QLoRA on TrajBench (63,484 balanced samples, five domains: reasoning, math, coding, web navigation, embodied AI) for general trajectory anomaly detection, evaluating exclusively on TrajBench anomaly detection metrics (F1, JEM); rollback-and-retry is described as an intended benefit but is not empirically evaluated for task success improvement, and TrajAD does not evaluate on ALFWorld, GAIA, or WebShop in their standard agentic form. TrajAD's three anomaly types include 'Process Inefficiency' (loops/detours) which is precisely the self-correctable deviation class that the Intervention Paradox shows causes regression when interrupted—TrajAD has no step threshold and does not address the Intervention Paradox tradeoff. CascadeWatch differs: trained on AgentErrorBench expert cascade root-cause annotations (not synthetic perturbations), targeting only recoverability-degrading cascade-onset prefixes (not process inefficiencies), imposing step ≥ 5 threshold calibrated to both the Intervention Paradox and AgentErrorBench's cascade-onset distribution, requiring no model fine-tuning (frozen external probe), and directly evaluating task success improvement on ALFWorld/GAIA/WebShop. CascadeWatch and TrajAD address overlapping detection problems on different evaluation surfaces; CascadeWatch's baseline set includes a TrajAD-style general anomaly detection condition trained on synthetic perturbation labels on the same CascadeWatch benchmarks to enable direct comparison. (2) InferAct (arXiv 2407.11843, EMNLP 2025) uses Theory-of-Mind reasoning to detect single-step actions misaligned with user intent on WebArena, ALFWorld, and HotpotQA, achieving up to 20% Marco-F1 improvement, alerting humans for correction; InferAct targets single-step authorization misalignment while CascadeWatch targets multi-step cascade propagation using ERR recoverability prefix estimates, with automated rollback rather than human alerting. (3) MASC (arXiv 2510.14319) detects cascading errors in multi-agent systems via unsupervised Prototype-Guided Next-Execution Reconstruction on Who&When; CascadeWatch targets single-agent cascade onset using supervised ERR-motivated recoverability labels on ALFWorld, GAIA, and WebShop. (4) Canonical Path Deviation (arXiv 2602.19008) identifies stochastic drift from canonical solution paths—aggregated from multiple successful runs per task—as a long-horizon failure mechanism, achieving +8.8pp improvement via restart of lowest-adherence runs; CascadeWatch uses single-trajectory recoverability prefix estimates (no canonical paths required) and performs targeted rollback rather than full restarts. (5) ErrorProbe (arXiv 2604.17658) is a contemporaneous offline diagnostic for multi-agent systems using backward tracing and multi-agent verification teams; CascadeWatch is an online single-agent monitor with automated rollback, not an offline diagnostic. (6) From Spark to Fire (arXiv 2603.04474) proposes a genealogy-graph governance layer for cascade mitigation in multi-agent collaboration; CascadeWatch addresses single-agent cognitive cascade failure where there are no inter-agent message dependencies. (7) ProMAS (arXiv 2603.20260) raises alerts in multi-agent reasoning but provides no corrective action and evaluates only on Who&When. (8) ProbGuard (arXiv 2508.00500) softly intervenes on physical safety constraints via symbolic DTMC. (9) Trajectory Guard (arXiv 2601.00516) uses a Siamese Recurrent Autoencoder for general structural anomaly detection at 32ms but targets reconstruction deviation on security audit and multi-agent benchmarks, provides no rollback.\n\nUnlike BacktrackAgent (arXiv 2505.20660, EMNLP 2025), which trains a verifier-judger-reflector pipeline for GUI action errors, CascadeWatch requires no modification to the base agent; unlike TrajAD, it requires no backbone fine-tuning—deploying on a different backbone requires retraining only the MLP probe (~3–5 H100-hours). Unlike Self-Backtracking (arXiv 2502.04404), which trains the LLM itself, CascadeWatch operates as a frozen external probe. Prior hidden-state probing (arXiv 2504.05419) targets single-step reasoning correctness for token reduction; CascadeWatch targets multi-step cascade onset with ERR recoverability prefix estimates as a second feature channel.\n\nRollback: for ALFWorld, command-replay from env.reset() (~25–100ms for 50-step episodes; TextWorld's Python API does not expose save/restore for Glulx-format .ulx games); for WebShop and GAIA, context-only rollback (does not undo irreversible intra-episode web-state changes—acknowledged as limitation; WebShop simulation resets between episodes so this affects recovery quality but not evaluation validity). Cascade-positive training examples: ~135–155 from AgentErrorBench expert annotations before synthetic augmentation. GAIA probe operates near minimum viable supervised learning regime; GAIA results are preliminary evidence. Primary empirical claim: CascadeWatch achieves task success rate improvement over no-correction baselines on ALFWorld, GAIA, and WebShop while avoiding the performance degradation caused by generic critics and general anomaly detectors—demonstrating that cascade-specific precision with Intervention Paradox–calibrated thresholding is sufficient to make rollback net-positive on benchmarks where generic critics fail. A TrajAD-style baseline re-implements TrajAD's training methodology (synthetic perturbation labels, no step threshold, no ERR signal) on the same CascadeWatch evaluation surface to enable direct comparison. Recoverability-delta ablation: ≥3% F1 lift confirms ERR-motivated design; <3% is reported as a negative result. Compressed HIL mode fits within ~62–93 H100-hours and 12–14 calendar days.",
  "project_name": "cascade_monitor",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL MISSING RELATED WORK: ProMAS (arXiv 2603.20260, March 2026) — 'Proactive Error Forecasting for Multi-Agent Systems Using Markov Transition Dynamics' — directly pre-empts the core contribution. It proactively predicts failures from trajectory prefixes using semantic displacement features + MLP Proactive Prediction Head, achieving 22.97% step-level accuracy while processing only 27% of reasoning logs. Without citing and clearly differentiating from ProMAS, reviewers will reject on novelty grounds.", "CRITICAL MISSING RELATED WORK: ProbGuard (arXiv 2508.00500, August 2025) — 'Probabilistic Runtime Monitoring for LLM Agent Safety' — learns a DTMC from execution traces to estimate P(reaching unsafe states) at each step and triggers intervention when risk exceeds threshold. This is structurally isomorphic to CascadeWatch (P(cascade) > threshold → intervention). Though applied to physical safety, not cognitive-task cascades, it must be discussed in related work.", "Training data is critically sparse: ~200 labeled trajectories total (100 ALFWorld, 50 WebShop, 50 GAIA). Even with 5K synthetic augmentation, the distribution shift between synthetic (Qwen3-72B backbone rollouts) and the human-annotated test distribution may dominate. No cross-validation strategy or regularization design is specified to guard against overfitting the 2-layer MLP to this small set.", "Rollback mechanism underspecified for stateful environments: ALFWorld and WebShop are simulators with action-irreversible state (e.g., picking up an object, submitting a search). 'Targeted rollback to the last low-risk checkpoint' requires either full simulator state serialization at every step (not costed, adds significant engineering overhead) or is limited to context-only rollback (which does NOT undo executed actions). This is a core mechanism that must be precisely defined.", "Resource estimate does not explicitly convert A100-hours to H100-hours. Qwen3-72B requires 2× A100 80GB or 1× H100 80GB for FP16 inference, so the stated '~80h A100 for rollout generation' should read '~80h × 2 GPUs = ~160 A100-GPU-hours = ~80 H100-hours.' Total revised estimate: ~145-160 H100-hours (still within 200, but needs to be shown explicitly).", "Cascade label derivation from root-cause annotations introduces labeling noise: not all trajectories with a root-cause error at step k actually produce cascades — some errors are contained. The label = 'any step ≥ earliest root-cause error is cascade-onset' assumption will generate false cascade labels for trajectories where the agent partially recovers, inflating cascade-positive counts and degrading classifier reliability.", "No ablation is planned to isolate the contribution of ERR-delta features vs. hidden-state embeddings alone. Without this ablation, the paper cannot claim that integrating ERR adds value, which is the key technical differentiator from ProMAS. If ERR adds ≤1% over embeddings-only, the theoretical motivation weakens substantially.", "False-positive compounding is unaddressed: if the monitor fires at step k and the re-sampled action (with elevated temperature) is worse than the original, the agent is now at step k with a potentially worse trajectory prefix. There is no circuit-breaker to prevent repeated triggers, which could lead to worse outcomes than no correction at all.", "The 'Snowball Effect' paper (arXiv 2604.04269) is cited as quantifying 'exponential error amplification,' but from the abstract it is a position/analysis paper about agentic IR, not an empirical measurement of cascade amplification rates that can be cited as empirical support. The claim should be qualified."]
Feedback: The core idea — a lightweight probe combining frozen LLM hidden-state features with ERR-derived recoverability signals to trigger early rollback — is technically coherent and the supporting evidence (AgentErrorBench, ERR paper) is well-chosen. The revision should focus on three surgical changes that would materially strengthen the paper for EMNLP:

1. **Differentiate from ProMAS and ProbGuard explicitly.** Add both to related work. The differentiating argument should be: (a) ProMAS uses Markovian transition dynamics between quantized semantic clusters but has no corrective action mechanism; CascadeWatch is the first proactive monitor that triggers hard rollback rather than only raising an alert. (b) ProbGuard operates via prompt-injection intervention on physical safety constraints using a DTMC; CascadeWatch targets cognitive-task cascade failure using frozen neural representations + recoverability signals. Frame CascadeWatch as the first system that closes the loop: ProMAS detects, ProbGuard detects and softly intervenes — CascadeWatch detects and hard-rollbacks with empirically validated cascade labels.

2. **Make rollback concrete.** For stateful environments (ALFWorld, WebShop), specify whether rollback restores full simulator state (requiring explicit checkpoint saving at each step) or is context-only (rewinding the prompt/observation history while leaving environment state unchanged). Context-only rollback is implementable in 16 days and sufficient to demonstrate the method; hard state rollback requires environment-specific engineering. Pick one, specify it, and note the limitation for the other case.

3. **Add the ablation that proves ERR adds value.** The only new feature CascadeWatch contributes over ProMAS is the ERR-derived Efficiency Score delta signals. Budget 20-30 A100-hours for a 3-way ablation: (a) embeddings-only probe, (b) ERR-deltas-only logistic regression, (c) full CascadeWatch. If ERR provides ≥3% F1 lift over (a), this is the central empirical result of the paper and should be foregrounded.

Minor: Fix the resource estimate to show explicit H100-hour conversion. Address label noise in cascade derivation by adding a 'cascade confirmed' criterion (e.g., task fails AND root-cause step is before the midpoint). Add a false-positive circuit-breaker (max 2 rollbacks per episode).

### Round 2 review
Verdict: revise
Issues: ["CRITICAL — TextWorld save_game/restore_game API is factually incorrect: TextWorld core.py has no save_game or restore_game methods (confirmed via GitHub); the Glulx interpreter's text-level save/restore commands exist but are documented as disabled for ALFWorld competition games (TextWorld GitHub issue #161); the only state-copy mechanism is env.copy(), which does not support .ulx Glulx games and incurs full environment duplication cost, not 5ms. The rollback implementation must be redesigned: either use command-replay from reset (O(k) cost, not 5ms — must be costed), use Jericho's RAM-save for .z8 format games (different game engine, not ALFWorld), or acknowledge ALFWorld rollback is also context-only. The title 'Hard Rollback' is misleading if ALFWorld's claimed mechanism doesn't exist.", "CRITICAL — Hard constraint incompatibility: the 16-day timeline and ≤200 H100-hour compute budget cannot be jointly satisfied. Manual mode: 135–175 H100-hours (within budget) but 4–6 months (violates 16 days). HIL mode: 180–220 H100-hours (within budget) but 4–8 weeks (violates 16 days). Auto-research mode: 3–10 days (within 16 days) but 480–600 H100-hours (2.4–3× the 200-hour limit). The paper must either restructure the HIL mode to be achievable in 16 days under 200 H100-hours (e.g., 3–4 benchmarks only, no ablation sweep, 2K rollouts instead of 5K), or honestly acknowledge that a 16-day execution requires either compute overage or reduced scope.", "MISSING RELATED WORK — BacktrackAgent (arXiv 2505.20660, May 2025): a framework for GUI agent error detection and backtracking with verifier, judger, and reflector modules. The conceptual overlap (error detection → backtracking trigger) must be acknowledged and differentiated. CascadeWatch's differentiator is cascade-specific detection using recoverability signals, not the backtracking trigger mechanism itself.", "MISSING RELATED WORK — 'Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models' (arXiv 2502.04404, Feb 2025): trains LLMs to internalize when and where to backtrack during both training and inference. Must be cited to clarify that CascadeWatch is an external monitor (does not require model retraining) and targets cascade failure specifically, not general reasoning dead-ends.", "MISSING RELATED WORK — 'Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification' (arXiv 2504.05419, Apr 2025): uses frozen LLM hidden-state probes for correctness prediction with 24% token reduction in reasoning tasks. The mechanism is structurally similar to CascadeWatch's frozen Qwen3-72B embedding + MLP probe. Must be cited; key differentiation is that CascadeWatch targets agent cascade failure (multi-step trajectory prefixes) rather than single-step answer correctness.", "ERR applicability gap: the ERR paper (arXiv 2601.22352) formalizes recoverability for tool-augmented agents recovering from tool execution failures (e.g., API errors, failed web actions). ALFWorld is a text-based game where failures are cognitive planning errors, not tool execution failures. The paper must explicitly address how the Efficiency Score observable is computed for ALFWorld trajectories that lack structured tool-call/result pairs, or qualify that ERR-delta features apply only to WebShop and GAIA (which involve tool use) and use a different recoverability proxy for ALFWorld.", "Title inconsistency: the paper is titled 'CascadeWatch: Cascade-Onset Detection with Hard Rollback' but WebShop and GAIA receive only context-only rollback (which explicitly does not undo executed web-state changes). If ALFWorld's save_game/restore_game API doesn't exist either, then no benchmark achieves hard rollback. Either fix the rollback mechanism for at least one benchmark to be genuinely hard, or rename to 'CascadeWatch: Cascade-Onset Detection with Targeted Rollback'.", "Resource estimate inconsistency: the auto-research mode (480–600 H100-hours) is presented as a valid execution mode but exceeds the stated hard constraint of ≤200 H100-hours by 2.4–3×. The auto-research section should be framed as 'extended evaluation beyond constraint' or the constraint should be explicitly re-evaluated for that mode."]
Feedback: The Round 2 revision successfully addresses five of nine Round 1 issues: ProMAS and ProbGuard are now explicitly differentiated, the confirmed-cascade criterion fixes label noise, the 3-way ablation is pre-registered, the H100-hour conversion is shown, and the circuit-breaker is specified. The idea remains technically sound and well-motivated. Three surgical changes are needed for Round 3:

1. **Fix the ALFWorld rollback claim (highest priority).** The save_game/restore_game methods do not exist in TextWorld's Python API, and the Glulx-level save commands are disabled for ALFWorld competition games. Replace with one of: (a) command-replay rollback from env.reset() — acknowledge the O(k) replay cost and add ~5–10 H100-hours to the compute estimate; (b) restrict to context-only rollback for all three benchmarks and retitle accordingly; (c) prototype with Jericho's .z8 RAM-save API, but note this uses a different game format from standard ALFWorld. Option (b) is achievable in 16 days; option (c) risks benchmark mismatch. Whatever you choose, the 5ms claim must be removed.

2. **Add three missing citations with differentiation.** For BacktrackAgent (2505.20660): 'Unlike BacktrackAgent's trained verifier-judger-reflector pipeline for GUI actions, CascadeWatch uses a cascade-specific probe targeting recoverability-degrading prefix patterns, without modifying the base agent.' For Self-Backtracking (2502.04404): 'Self-Backtracking trains the base LLM to internalize rollback decisions; CascadeWatch requires no model retraining and operates as an external monitor on any frozen agent.' For hidden-state probes (2504.05419): 'Prior work probes hidden states for single-step answer correctness in reasoning tasks; CascadeWatch probes multi-step trajectory prefixes for cascade onset in long-horizon agent tasks, adding ERR-delta recoverability signals as a second feature channel.'

3. **Resolve the 16-day/200 H100-hour joint constraint.** The only execution path within both constraints is a compressed HIL mode: reduce to 2 benchmarks (ALFWorld + GAIA), 2K synthetic rollouts at 2 temperatures, 3-fold CV instead of 5-fold, and daily human engagement of 2–3 hours rather than 30 minutes. This brings estimated compute to ~120–140 H100-hours and calendar time to 12–14 days. Show this math explicitly.

Minor: Qualify ERR-delta applicability — note that for ALFWorld, Efficiency Score deltas are computed from step-level reward signals (ALFWorld provides intermediate rewards) rather than from tool-call success rates, and acknowledge this is a domain adaptation of the ERR framework.

### Round 3 review
Verdict: revise
Issues: ["UNACKNOWLEDGED COMPETITOR — arXiv 2602.19008 'Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks' (Feb 2026, Wilson Y. Lee) directly analyzes why long-horizon agents fail by measuring stochastic drift from canonical solution paths. The key finding—that adherence gaps become significant only at 75% trajectory completion and that drift is self-reinforcing—is structurally equivalent to cascade-onset propagation, using path adherence as the recoverability-degrading signal. CascadeWatch must cite this and explain why detecting recoverability-delta (ERR Efficiency Score) is preferable to detecting canonical path deviation as an early-warning signal.", "UNACKNOWLEDGED RELATED WORK — arXiv 2603.04474 'From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration' (March 2026) explicitly models cascade error propagation in LLM-based systems and proposes a governance layer with rollback via message-layer blocking, achieving defense success rate from 0.32 to 0.89. Although this is multi-agent and uses genealogy graphs rather than trajectory-prefix probes, EMNLP reviewers will find it. CascadeWatch should explicitly state: this paper targets multi-agent distributed collaboration; CascadeWatch targets single-agent long-horizon cognitive failure in text-game and tool-augmented environments. The distinction is real but must be stated.", "AGENT-SPECIFICITY CLAIM IS MISLEADING: The paper claims CascadeWatch is 'deployable on any frozen agent without model retraining.' This is false as stated. The probe uses frozen Qwen3-72B hidden-state embeddings as features; deploying it with a different backbone (Claude, GPT-4o, Llama-3.3-70B) changes the embedding space entirely, requiring full probe retraining on that backbone's trajectories. The correct claim is: 'CascadeWatch requires no modification to the base agent and does not require retraining the base agent; deploying CascadeWatch with a different LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours), not the base agent.' This is still a meaningful practical advantage over BacktrackAgent but must be stated accurately.", "PRIMARY EMPIRICAL CLAIM FRAMING: The central empirical claim is stated as 'recoverability-delta provides ≥3% F1 lift over embeddings alone.' This is an ablation threshold, not a headline result. EMNLP reviewers will evaluate the paper primarily on the task success rate improvement over baselines (no-correction, ExpeL, self-verification) on ALFWorld and GAIA—especially whether CascadeWatch avoids the Intervention Paradox regression observed with generic critics. The ≥3% F1 ablation claim should be repositioned as an internal validation gate; the primary empirical claim should be the task success rate delta against baselines on pilot-test-passing benchmarks.", "MODEL VERSION STALENESS: The paper specifies 'frozen Qwen3-72B' as the backbone, but Qwen3.5 (released February 2026) and Qwen3.6-Plus supersede Qwen3-72B as of the submission date. This does not invalidate the method but creates a reproducibility question—which checkpoint is used? The paper should specify the exact model checkpoint (Qwen/Qwen3-72B on HuggingFace or equivalent) to ensure reproducibility, or update to Qwen3.5-72B-Instruct if that provides meaningfully better cascade signal separation.", "MINOR — Crab (arXiv 2604.28138) is cited in key references but its role is unclear in the paper. Crab provides semantics-aware checkpoint/restore for agent sandboxes, which is architecturally relevant to the rollback mechanism. The paper should clarify whether Crab was considered for ALFWorld rollback (and why command-replay was chosen instead) or should remove the citation if it has no direct bearing on the method."]
Feedback: Round 3 has cleanly resolved all three surgical changes requested in Round 2: the ALFWorld rollback mechanism is now technically correct (command-replay from env.reset(), O(k) acknowledged, no false save_game claim), the joint 16-day/200 H100-hour constraint is satisfied in the HIL mode (80–110 H100-hours, 12–14 days), and all three requested citations are present with accurate differentiation. The idea is now coherent, well-specified, and positioned at the right level of novelty for EMNLP Findings. One more focused round is needed.

**Four targeted changes for Round 4:**

1. **Cite and differentiate arXiv 2602.19008 (Canonical Path Deviation).** This paper (Feb 2026) is the closest theoretical neighbor—it identifies stochastic drift from canonical solution paths as the causal mechanism of long-horizon failure, using path adherence as the early-warning signal. The differentiation argument: 'Canonical Path Deviation detects drift post-hoc using trajectory-completion statistics (significance emerges only at 75% completion); CascadeWatch targets cascade onset proactively at steps 5–15 using a trained probe on prefix embeddings + recoverability-delta, enabling intervention before the 75% threshold. Moreover, canonical path adherence requires knowing the canonical path—requiring either multiple successful runs or a verifier—while CascadeWatch's recoverability proxy is computable from single trajectories.'

2. **Cite arXiv 2603.04474 (From Spark to Fire) in 1–2 sentences.** 'From Spark to Fire [citation] proposes a genealogy-graph governance layer for cascade mitigation in multi-agent collaboration; CascadeWatch addresses a structurally different failure mode—cognitive cascade failure in single-agent long-horizon tasks—using trajectory-prefix probes with recoverability signals rather than message-level graph analysis.'

3. **Fix the 'any frozen agent' claim.** Change to: 'CascadeWatch requires no modification to the base agent; deploying it with a new LLM backbone requires retraining only the lightweight MLP probe (~3–5 H100-hours) against that backbone's embedding space, not retraining the agent itself.'

4. **Reframe the primary empirical claim.** The headline result should be: 'CascadeWatch achieves [X]pp task success rate improvement over no-correction on ALFWorld and [Y]pp on GAIA, while avoiding the degradation caused by generic critics (Intervention Paradox) on both benchmarks.' The ≥3% F1 ablation threshold becomes the validation gate for including recoverability-delta features, not the primary claim.

### Round 4 review
Verdict: revise
Issues: ["MODERATE — Trajectory Guard (arXiv 2601.00516, AAAI TrustAgent Workshop 2026) is not cited despite direct framing overlap. The paper proposes a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss for real-time anomaly detection in agentic AI trajectories, achieving F1 0.88–0.94 while running 17–27× faster than LLM Judge baselines at 32ms inference. CascadeWatch must cite and differentiate: (a) Trajectory Guard detects general structural anomalies via reconstruction error, not cascade-specific onset via recoverability-delta signals; (b) it evaluates on security audit failures (RAS-Eval) and multi-agent systems (Who&When), not single-agent long-horizon tasks (ALFWorld, GAIA); (c) it provides no rollback or correction mechanism. These distinctions are clear and defensible, but leaving Trajectory Guard uncited risks a reviewer objection on related-work coverage.", "MODERATE — The claim 'Qwen/Qwen3-32B; the largest official open-weights model in the Qwen3 family' is factually incorrect. Qwen3-235B-A22B is an official open-weight MoE model published at Qwen/Qwen3-235B-A22B on HuggingFace under Apache 2.0 with 235B total parameters — larger than Qwen3-32B. The correct claim is 'the largest official open-weights dense model in the Qwen3 family' (the 32B is justified by fitting in 1× H100-80GB BF16 without quantization, not by being the absolute largest). Alternatively, drop the superlative entirely and state: 'We use Qwen/Qwen3-32B (32B dense model, 64GB BF16, fits in 1× H100-80GB without quantization).'", "MINOR — The GAIA training data regime (~27 samples per fold after 3-fold CV on 50 total trajectories) is acknowledged only in the resource_estimate risk_note, not in the methods or experiment design sections. The paper body should explicitly state that the GAIA cascade probe operates near the minimum viable supervised learning regime and frame GAIA results as preliminary evidence, with ALFWorld (100 trajectories, ~67 per fold) providing the primary evidence base for the main claim."]
Feedback: Round 4 has cleanly addressed all four targeted issues from Round 3. Canonical Path Deviation is now extensively cited with technically precise differentiation (single-trajectory vs. multi-run signals, proactive vs. retrospective detection, targeted rollback vs. full restart). From Spark to Fire is differentiated on structural grounds (inter-agent vs. single-agent cascade). The 'any frozen agent' claim is corrected. The primary empirical claim is reframed as task success rate improvement. The ALFWorld rollback is technically correct (command-replay from env.reset(), Glulx API limitation acknowledged, Crab rationale clarified). Three short fixes will bring this to pass:

1. **Add one Trajectory Guard sentence to §Related Work**: 'Trajectory Guard [arXiv 2601.00516] uses a Siamese Recurrent Autoencoder with hybrid contrastive-reconstruction loss to detect trajectory anomalies in agentic AI at 32ms, but targets general structural anomalies rather than cascade-specific onset via recoverability signals, evaluates on security audit and multi-agent benchmarks (not ALFWorld/GAIA), and provides no rollback mechanism.' This citation is necessary because its framing ('lightweight inference-time monitoring of agentic trajectories') directly overlaps with CascadeWatch's positioning.

2. **Fix Qwen3-32B superlative**: Remove 'the largest official open-weights model in the Qwen3 family.' Replace with 'Qwen/Qwen3-32B (32B dense model; 64GB BF16; fits in 1× H100-80GB without quantization).' The 235B MoE model is also official and is larger; the superlative will draw reviewer scrutiny.

3. **Disclose GAIA data regime in §Experiments**: Add one sentence: 'The GAIA subset (50 trajectories, ~27 training samples per fold) operates near the minimum viable supervised regime; GAIA results are treated as preliminary evidence, with ALFWorld (100 trajectories) providing the primary evidence base for the main cascade-avoidance claim.'

### Round 5 review
Verdict: revise
Issues: ["MODERATE — InferAct (arXiv 2407.11843, EMNLP 2025 main track, pages 222–244) is uncited despite being published at the exact target venue and explicitly framing its contribution as 'preemptive detection and correction of misaligned actions in LLM agents.' It uses Theory-of-Mind reasoning (Task Inference Unit + Task Verification Unit) to detect misaligned agent actions before execution and achieves up to 20% Marco-F1 improvement over baselines. EMNLP 2026 reviewers will know this paper and its absence will be a red flag. The distinction from CascadeWatch is real — InferAct targets single-step action misalignment with user intent (e.g., executing a buy action without user authorization) via ToM belief reasoning and requires human-in-loop correction via user alerts; CascadeWatch targets multi-step cascade propagation onset via trajectory-prefix ERR recoverability signals and triggers automated rollback — but these distinctions must be stated explicitly in related work.", "MINOR — MASC (arXiv 2510.14319, October 2025, revised January 2026) — 'Metacognitive Self-Correction for Multi-Agent System via Prototype-Guided Next-Execution Reconstruction' — explicitly targets cascading errors in agent systems using history-conditioned embedding anomaly scoring (Next-Execution Reconstruction + Prototype-Guided Enhancement) to trigger step-level correction, achieving +8.47% AUC-ROC on the Who&When benchmark. Though MASC is multi-agent (not single-agent), it uses an embedding-based cascade-targeting mechanism structurally related to CascadeWatch's frozen embedding probe, and its explicit 'cascading errors' framing partially occupies CascadeWatch's conceptual space. A 1–2 sentence mention with differentiation (multi-agent vs. single-agent; unsupervised reconstruction vs. supervised ERR-motivated cascade labels; Who&When vs. ALFWorld/GAIA) is needed to complete the landscape coverage."]
Feedback: All three Round 4 fixes are cleanly implemented. The paper is close to pass-ready. Two targeted additions will close the remaining reviewer exposure:

1. **Add InferAct to §Related Work (required):** 'InferAct [arXiv 2407.11843, EMNLP 2025] uses Theory-of-Mind reasoning to detect actions misaligned with user intent before execution and alerts users for correction, achieving up to 20% Marco-F1 improvement. InferAct addresses single-step action misalignment — whether a specific upcoming action matches user authorization — and relies on human-in-loop correction via user alerts. CascadeWatch addresses a structurally different failure mode: multi-step cascade propagation, where an early-step error compounds across subsequent trajectory steps regardless of user intent; our detection uses trajectory-prefix ERR recoverability signals rather than ToM belief inference, and our intervention is automated rollback rather than human alerting.' This distinction is accurate and defensible; the citation is necessary.

2. **Add MASC to §Related Work (recommended, 1–2 sentences):** 'MASC [arXiv 2510.14319] proposes metacognitive self-correction for multi-agent systems via Prototype-Guided Next-Execution Reconstruction, detecting cascading errors at step level via history-conditioned embedding anomaly scoring and triggering correction agents; CascadeWatch differs in targeting single-agent long-horizon cognitive cascades using supervised ERR-motivated recoverability labels (not unsupervised reconstruction) and evaluating on ALFWorld/GAIA rather than the Who&When multi-agent benchmark.'

### Round 6 review
Verdict: revise
Issues: ["CRITICAL — TrajAD (arXiv 2602.06443, 'Trajectory Anomaly Detection for Trustworthy LLM Agents') is an uncited competitor that evaluates on ALFWorld, GAIA, AND WebShop — the exact same benchmark set as CascadeWatch — and explicitly states rollback-and-retry is essential for error recovery, using a specialized verifier trained with fine-grained process supervision. EMNLP reviewers will recognize this paper. The differentiation argument exists (TrajAD uses synthetic TrajBench perturbation labels for general anomaly detection; CascadeWatch uses AgentErrorBench's expert-annotated cascade root-causes with ERR recoverability deltas for cascade-specific onset detection; TrajAD's approach is retrospective error localization while CascadeWatch's step ≥ 5 threshold proactively targets the cascade-propagation window that the Intervention Paradox identifies as the high-risk regime), but it must be stated explicitly in §Related Work.", "CRITICAL — InferAct (arXiv 2407.11843, EMNLP 2025 main track, pages 222–244) remains uncited despite being flagged as required in Round 5. It evaluates on ALFWorld (among other benchmarks), is published at the exact target venue, and is preemptive detection with correction — a direct framing overlap. The absence of this citation after two review rounds of flagging will draw immediate reviewer scrutiny.", "MODERATE — MASC (arXiv 2510.14319) remains uncited despite being recommended in Round 5. Its history-conditioned embedding anomaly scoring for cascading errors in multi-agent systems partially occupies CascadeWatch's conceptual space and uses Who&When (not ALFWorld/GAIA) as its benchmark, making differentiation straightforward but necessary."]
Feedback: Round 6 submission has made no additions relative to Round 5's required citations — InferAct and MASC are still absent. Additionally, a new high-priority competitor (TrajAD) has been independently identified that evaluates on the same benchmark triple (ALFWorld, GAIA, WebShop) with explicit rollback-and-retry. Three targeted additions are needed:

1. **Add TrajAD to §Related Work (highest priority, newly identified):** 'TrajAD [arXiv 2602.06443] proposes a specialized verifier trained with fine-grained process supervision for trajectory anomaly detection on ALFWorld, GAIA, and WebShop, explicitly enabling rollback-and-retry on error localization. TrajAD is a general-purpose anomaly detector: it uses synthetic TrajBench perturbation labels covering diverse procedural deviations, not cascade-specific annotations tied to confirmed failure propagation. CascadeWatch differs in three ways: (1) detection is cascade-onset specific rather than general-anomaly — using ERR Efficiency Score recoverability deltas as the distinguishing signal for compounding-cost prefixes, not reconstruction deviation; (2) training labels come from AgentErrorBench expert root-cause annotations with the confirmed-cascade criterion (trajectory fails AND root-cause before midpoint), not synthetic perturbations; (3) the step ≥ 5 minimum intervention threshold is specifically calibrated to the Intervention Paradox finding that all observed regressions occur at step ≤ 2, a constraint TrajAD does not impose.'

2. **Add InferAct to §Related Work (required, carried from Round 5):** 'InferAct [arXiv 2407.11843, EMNLP 2025] uses Theory-of-Mind reasoning to detect single-step actions misaligned with user intent before execution on WebArena, ALFWorld, and HotpotQA, achieving up to 20% Marco-F1 improvement. InferAct addresses misalignment between the upcoming action and user authorization — whether a specific action matches user intent — and relies on human-in-loop correction via alerts. CascadeWatch addresses a structurally different failure mode: multi-step cascade propagation, where an early-step cognitive error compounds across subsequent trajectory steps independent of user intent; our detection uses trajectory-prefix ERR recoverability signals rather than ToM belief inference, and our intervention is automated targeted rollback rather than human alerting.'

3. **Add MASC in 1–2 sentences (recommended, carried from Round 5):** 'MASC [arXiv 2510.14319] detects cascading errors in multi-agent systems via Prototype-Guided Next-Execution Reconstruction with unsupervised embedding anomaly scoring on Who&When; CascadeWatch targets single-agent long-horizon cognitive cascades using supervised ERR-motivated recoverability labels (not unsupervised reconstruction) on ALFWorld and GAIA.'

### Round 7 review
Verdict: revise
Issues: ["MODERATE — Cascade label derivation for synthetic trajectories is unspecified: the confirmed-cascade criterion requires identifying the 'earliest annotated root-cause error step' for each trajectory, but the 5K synthetic rollouts from Qwen/Qwen3-32B have no expert annotations. If the automated label proxy for synthetic trajectories is 'trajectory fails AND some heuristic for early-step failure' (e.g., any step k before midpoint in a failed trajectory), this introduces systematic label noise that differs from the expert-annotated criterion used for the 200 real trajectories. The paper must explicitly state how cascade labels are derived for synthetic data — either the same confirmed-cascade criterion (which is impossible without root-cause annotation) or a degraded proxy (which must be acknowledged and its error rate estimated).", "MODERATE — WebShop omission weakens TrajAD comparison: TrajAD evaluates on ALFWorld, GAIA, AND WebShop; CascadeWatch's 'optional extension' framing for WebShop means the head-to-head comparison with the closest benchmark competitor is incomplete on a full third of its evaluation surface. EMNLP reviewers familiar with TrajAD will flag this. Either (a) commit to WebShop in the primary evaluation (adding ~15–25 H100-hours, which still fits within the 200-hour HIL constraint), or (b) explicitly acknowledge in the paper that the comparison is partial and that TrajAD's WebShop performance remains uncontested by CascadeWatch.", "MINOR — The expected number of cascade-positive examples from the 200 AgentErrorBench trajectories after applying the confirmed-cascade filter is never stated. ALFWorld has a baseline failure rate of 5.8–14.7% (per the Intervention Paradox paper), suggesting most trajectories succeed, but AgentErrorBench likely oversamples failures. Estimating that, say, 60–80 of 100 ALFWorld trajectories are failure trajectories and perhaps 40–60 pass the confirmed-cascade criterion (root-cause before midpoint) gives ~40–60 cascade-positive training examples before augmentation — this should be stated explicitly to give readers confidence in the probe's training signal without relying solely on the 5K synthetic expansion.", "MINOR — The Intervention Paradox's specific finding that 'all observed regressions occur at step ≤ 2' is stated as a key empirical fact grounding the step ≥ 5 threshold, but this claim is from a paper that evaluated specific benchmarks (HotPotQA, GAIA, ALFWorld) with a specific critic type. It would strengthen the paper to note whether this step-≤-2 regression finding applies uniformly across all benchmarks evaluated in that paper, or only to specific ones, to ensure the step ≥ 5 threshold is correctly calibrated for ALFWorld and GAIA specifically."]
Feedback: The Round 7 submission cleanly addresses all three Round 6 critical issues — TrajAD is now extensively differentiated across four dimensions (training labels, anomaly target with Intervention Paradox awareness, architecture, recoverability signal); InferAct is cited with three substantive distinctions; MASC is differentiated on multi-agent vs. single-agent and supervised vs. unsupervised. Independent verification found no unaddressed competitor papers: the four papers I investigated (Failure is Feedback, Agent Banana, AgentEval, WebRollback) are either in different domains (multimodal retrieval, image editing), post-hoc evaluation frameworks, or web-specific rollback without cascade detection. Two targeted changes are needed for Round 8:

1. **Specify the cascade label derivation procedure for synthetic trajectories (required).** The confirmed-cascade criterion requires expert-annotated root-cause steps, which don't exist for the 5K synthetic rollouts. Add one explicit paragraph: state whether synthetic trajectories are labeled using (a) an automated root-cause approximation (e.g., step where cumulative reward delta first becomes negative), (b) trajectory-level failure labels only (cascade-positive = any step k < ⌊N/2⌋ in a failed trajectory), or (c) held to the same confirmed-cascade standard (in which case, how?). If (b), acknowledge that synthetic labels are coarser than AgentErrorBench expert labels and the probe trains on a mixture of high-precision real labels and lower-precision synthetic labels — this is an important methodological caveat.

2. **Resolve the WebShop evaluation gap (required for TrajAD comparison integrity).** The simplest resolution: add WebShop to the primary HIL evaluation plan. An additional ~15–25 H100-hours brings the total to ~65–100 H100-hours, still well within the 200-hour constraint and within the 12–14 day timeline (WebShop evaluation runs in parallel with GAIA evaluation). This makes the CascadeWatch vs. TrajAD comparison complete on the exact benchmark triple TrajAD uses. If WebShop is genuinely not feasible, change the framing from 'optional extension' to 'out-of-scope negative result: CascadeWatch's context-only rollback for WebShop (which cannot undo submitted searches) makes it a poor fit for this benchmark's action-irreversibility profile, unlike TrajAD's rollback-and-retry which is evaluated there.'

### Round 8 review
Verdict: revise
Issues: ["MODERATE (potentially CRITICAL) — TrajAD benchmark claim is unverified: The submission states TrajAD 'evaluates on ALFWorld, GAIA, and WebShop—the same benchmark set as CascadeWatch,' enabling a 'direct head-to-head comparison.' But the actual arXiv 2602.06443 abstract and HTML indicate TrajAD introduces its own TrajBench (a dataset synthesized via Perturb-and-Complete) and does not appear to evaluate on ALFWorld, GAIA, or WebShop. If TrajAD evaluates on TrajBench only, then (1) the 'identical benchmark triple' claim is false, (2) the 'direct head-to-head' framing must be changed to 'methodology comparison on different benchmarks,' and (3) TrajAD remains a relevant related work for architectural contrast but not a head-to-head baseline. The full TrajAD paper PDF must be checked; if TrajBench-only, reframe TrajAD as 'the most similar concurrent methodology' (not same-benchmark competitor) and compare methods on their respective reported metrics rather than claiming head-to-head.", "MODERATE — Internal rollout count inconsistency across sections: the approach section states '~2,000 synthetic rollouts sampled at two temperatures'; the HIL scope note states '2,000 total at 2 temperatures (T=0.7, T=1.0)'; the compute breakdown states '2K rollouts × 2 temperatures = 4K trajectories; ~1K ALFWorld + 1K GAIA + 1K WebShop per temperature.' The per-temperature breakdown (1K × 3 benchmarks = 3K per temperature × 2 temperatures = 6K total) contradicts both '2K total' and '4K trajectories.' One consistent number must appear throughout: if the intent is 2K total (≈333 per benchmark per temperature), the per-temperature breakdown should read '~333 ALFWorld + ~333 GAIA + ~333 WebShop'; if the intent is 4K total (≈667 per benchmark per temperature), the approach section should say '~4,000 synthetic rollouts.' The compute estimate (~15–20 H100-hours) should also be recalculated against the correct total.", "MODERATE — Real-vs-synthetic label granularity mismatch is acknowledged but understated: the paper says synthetic labels are 'coarser,' but the actual structural difference is more consequential. Real cascade-onset labels from AgentErrorBench are maximally sparse: exactly ONE step per trajectory receives label 1 (the expert-annotated root-cause step), all others receive 0. Synthetic cascade labels are maximally dense: ALL steps k ≤ ⌊N/2⌋ of every failed synthetic trajectory receive label 1. Training a 2-layer MLP on this mixed distribution creates a fundamental learning inconsistency: the probe trained on real data must learn 'fire only at the specific cascade-onset step'; the probe trained on synthetic data must learn 'fire throughout the early trajectory of any failing run.' These are different decision boundaries. The paper should name this conflict explicitly ('label density mismatch') rather than just calling synthetic labels 'coarser,' and should add a sentence explaining what the probe is expected to learn from the mixture: 'the mixed corpus trains the probe to distinguish cascade-onset prefixes from successful-trajectory prefixes (from real labels) while learning failure-mode diversity from synthetic trajectories at the cost of false cascade-onset signal at non-root-cause early steps.'"]
Feedback: Round 8 has addressed both Round 7 required changes: synthetic cascade label derivation is now explicitly specified (trajectory-level failure proxy for synthetic data, with AgentErrorBench-only ablation arm to quantify noise), and WebShop is now included in the primary HIL evaluation. The Intervention Paradox calibration, ALFWorld command-replay rollback, and all prior related-work citations are cleanly maintained. Three targeted changes are needed for Round 9:

1. **Verify and correct the TrajAD benchmark claim (highest priority).** Fetch the full TrajAD PDF and confirm whether it evaluates on ALFWorld, GAIA, and WebShop or exclusively on TrajBench. If TrajBench-only: remove 'evaluates on ALFWorld, GAIA, and WebShop' from the TrajAD description; replace 'enabling a direct head-to-head comparison' with 'enabling a methodology comparison — CascadeWatch and TrajAD address the same detection problem but on different evaluation surfaces'; retain TrajAD in the baseline set as 'a TrajAD-style general anomaly detector trained on the same CascadeWatch benchmarks using synthetic perturbation labels, ablating cascade-specific precision against general-purpose detection.' This reframing preserves the scientific comparison while being accurate about TrajAD's own evaluation scope.

2. **Resolve the rollout count inconsistency.** Pick one number consistently: either 2K total (≈333/benchmark/temperature, light augmentation) or 4K total (≈667/benchmark/temperature, moderate augmentation). Update the approach section, scope note, compute breakdown, and per-benchmark per-temperature figures to match. Recompute the 15–20 H100-hour rollout estimate against the correct total.

3. **Add one sentence naming the label density mismatch explicitly.** In the training data paragraph, after acknowledging the methodological caveat, add: 'Concretely, real cascade-onset labels are maximally sparse (one positive-labeled step per trajectory, at the expert-annotated root-cause step) while synthetic labels are maximally dense (all first-half steps of each failed trajectory receive cascade-positive labels); the MLP trained on the mixture must reconcile these as a label density mismatch rather than a smoothly graded precision difference. The AgentErrorBench-only ablation arm isolates whether the probe learns cascade-specific onset patterns or merely learns to fire throughout early failed-run prefixes.'


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
  "promptId": "85c410d9-22c4-47d9-a7b3-8ec988288332",
  "type": "user",
  "uuid": "6600e571-c452-48cb-9aef-cc1063c8e754",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-09T20:15:07.673Z_

```json
{
  "parentUuid": "6600e571-c452-48cb-9aef-cc1063c8e754",
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
  "uuid": "6d51116d-7290-4687-9fbd-ec42e20fff6f",
  "timestamp": "2026-05-09T20:15:07.673Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-09T20:15:07.673Z_

```json
{
  "parentUuid": "6d51116d-7290-4687-9fbd-ec42e20fff6f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8c86b5d5-baee-45bd-9fb9-d40912ce3c1c",
  "timestamp": "2026-05-09T20:15:07.673Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "8c86b5d5-baee-45bd-9fb9-d40912ce3c1c",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Cascade-specific onset detection via recoverability signals for agent long-horizon tasks",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449"
}
```

---

### Assistant

_source line 8 · 2026-05-09T20:15:24.338Z_

<details><summary>Logged reasoning block</summary>

```text
This is Round 9/10 of an adversarial review. Let me carefully analyze the current state of the idea and verify claims through web research before issuing my verdict.

The previous Round 8 review had three required changes:
1. Verify and correct TrajAD benchmark claim (does it evaluate on ALFWorld/GAIA/WebShop or only TrajBench?)
2. Resolve rollout count inconsistency (2K vs 4K)
3. Add explicit label density mismatch naming

Let me check the current submission to see if these are addressed:

Looking at the current submission (round 9):


The TrajAD benchmark claim now correctly specifies that it evaluates only on TrajBench with 63,484 balanced samples from the Perturb-and-Complete pipeline, and explicitly states it does not evaluate on ALFWorld, GAIA, or WebShop in their standard agentic task-completion form—so that's been fixed.

The rollout count is internally consistent: 333 rollouts per benchmark per temperature across three benchmarks and two temperatures gives roughly 2,000 total, which matches what's stated in both the approach and resource estimate sections.

Now I'm checking the label density issue—the approach section mentions that real cascade-onset labels are maximally sparse with exactly one positive-labeled step per trajectory at the expert-annotated root-cause step, but I need to see how this connects to the rest of the claim.

The label density mismatch is explicitly addressed: real labels are sparse (one positive per trajectory) while synthetic labels are dense (all steps up to ⌊N/2⌋ in failed trajectories get positive labels), forcing the MLP to reconcile two different decision boundaries.

Now I'm going to independently verify some of the key papers and claims: checking TrajAD, AgentErrorBench, the ERR paper, and the Intervention Paradox to confirm they exist and have the features described.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c86b5d5-baee-45bd-9fb9-d40912ce3c1c",
  "isSidechain": false,
  "requestId": "req_011CascFhk8W9gS7HFHSKqWL",
  "type": "assistant",
  "uuid": "72946889-7546-4d38-a7a4-06d201735300",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W9kVMHyFwbd7Tg3RinEZW8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32971,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1980,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1980,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 32971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32971
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

_source line 9 · 2026-05-09T20:15:24.583Z_

I'll conduct independent verification of the key claims in this Round 9 submission before issuing a verdict. Let me search for competitors and verify the cited papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72946889-7546-4d38-a7a4-06d201735300",
  "isSidechain": false,
  "requestId": "req_011CascFhk8W9gS7HFHSKqWL",
  "type": "assistant",
  "uuid": "cd4b0919-9ec8-4fac-bc55-94d613659cc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W9kVMHyFwbd7Tg3RinEZW8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32971,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1980,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1980,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 32971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32971
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

_source line 10 · 2026-05-09T20:15:29.504Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XJ2ZqSFGaXHaxSTswempLW`</summary>

```json
{
  "description": "Verify TrajAD benchmark scope and find competitors",
  "subagent_type": "Explore",
  "prompt": "Search for the paper \"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents\" (arXiv 2602.06443). I need to verify:\n1. Whether TrajAD evaluates on ALFWorld, GAIA, and WebShop directly, or only on its own TrajBench dataset\n2. What benchmarks TrajAD actually uses for evaluation\n3. Whether TrajAD performs rollback-and-retry on any standard agent benchmark\n\nSearch strategies:\n- Search for \"TrajAD trajectory anomaly detection 2026\" \n- Search for \"arxiv 2602.06443\"\n- Try to fetch the abstract/paper from arxiv\n\nAlso search for any new competitor papers I might have missed:\n- \"cascade failure agent detection 2026\"\n- \"agent trajectory monitoring rollback 2026\"\n- \"LLM agent failure prediction intervention 2026\"\n\nReport what you find about TrajAD's actual benchmark coverage and any new related papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd4b0919-9ec8-4fac-bc55-94d613659cc2",
  "isSidechain": false,
  "requestId": "req_011CascFhk8W9gS7HFHSKqWL",
  "type": "assistant",
  "uuid": "6b171c6d-e42e-488f-aaf4-8004dc96523f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W9kVMHyFwbd7Tg3RinEZW8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32971,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1980,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1980,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 32971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32971
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

_source line 11 · 2026-05-09T20:15:37.073Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01ACC8djDYCx2FQyaQeLAvRK`</summary>

```json
{
  "description": "Verify AgentErrorBench and ERR paper existence and claims",
  "subagent_type": "Explore",
  "prompt": "Search for and verify these specific papers:\n\n1. \"Where LLM Agents Fail and How They Can Learn From Failures\" (arXiv 2509.25370) - supposedly \"AgentErrorBench\" with 200 expert-annotated trajectories across ALFWorld, WebShop, GAIA with Cohen's κ = 0.55\n   - Search: \"arxiv 2509.25370\" and \"AgentErrorBench\"\n   - Verify: Does it contain critical_failure_step field? Is it on HuggingFace as davide221/agenterrorbench?\n\n2. \"Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents\" (arXiv 2601.22352) - supposedly defines ERR Efficiency Score proxy validated within δ ≤ 0.05\n   - Search: \"arxiv 2601.22352\" and \"ERR Efficiency Score recoverability\"\n   - Verify: Does it validate across five benchmarks?\n\n3. \"The Intervention Paradox\" (arXiv 2602.03338) - supposedly shows generic critics (AUROC 0.94) cause up to 26pp degradation, all regressions at steps 0-1\n   - Search: \"arxiv 2602.03338\" and \"intervention paradox agent failure\"\n   - Verify the specific claims about step 0-1 regressions and AUROC 0.94\n\nReport what you find - specifically whether these papers exist and whether the claims match what's described."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b171c6d-e42e-488f-aaf4-8004dc96523f",
  "isSidechain": false,
  "requestId": "req_011CascFhk8W9gS7HFHSKqWL",
  "type": "assistant",
  "uuid": "7ab03e16-a3e9-4307-8fd5-b12b960af23f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W9kVMHyFwbd7Tg3RinEZW8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32971,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1980,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1980,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 32971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32971
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

_source line 12 · 2026-05-09T20:15:43.347Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KzkUkbrJk2EcbNMFFUnpVr`</summary>

```json
{
  "description": "Search for recent agent monitoring and cascade detection papers",
  "subagent_type": "Explore",
  "prompt": "Search for recent (2025-2026) papers on LLM agent monitoring, cascade failure detection, and rollback mechanisms. I need to find any papers that might be competitors to \"CascadeWatch\" - a system that detects cascade failures in long-horizon agent tasks using frozen LLM embeddings + recoverability signals to trigger rollback.\n\nSearch queries to try:\n1. \"arxiv 2025 2026 agent trajectory monitoring cascade failure rollback\"\n2. \"LLM agent self-correction backtracking cascade 2026\"\n3. \"agent failure detection probe hidden states trajectory 2026\"\n4. \"agent cascade error proactive detection intervention 2026\"\n5. site:arxiv.org \"cascade failure\" \"LLM agent\" 2026\n6. \"agent monitoring rollback recoverability 2026\"\n7. \"BacktrackAgent\" arXiv 2505.20660 - verify this exists\n8. \"Canonical path deviation\" agent failure arXiv 2602.19008 - verify this\n\nFor each paper found, note: title, venue/arXiv ID, whether it does cascade detection, whether it does rollback, what benchmarks it uses.\n\nSpecifically focus on finding any papers from the last 3 months (Feb-May 2026) that might be concurrent/competitor work not yet cited."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ab03e16-a3e9-4307-8fd5-b12b960af23f",
  "isSidechain": false,
  "requestId": "req_011CascFhk8W9gS7HFHSKqWL",
  "type": "assistant",
  "uuid": "196b257b-d119-49c6-b0cc-be511eba1082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01W9kVMHyFwbd7Tg3RinEZW8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 32971,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1980,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 32971,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1980,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 32971,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 32971
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

_source line 13 · 2026-05-09T20:16:12.355Z_

<details><summary>↩ Tool result · `toolu_01XJ2ZqSFGaXHaxSTswempLW`</summary>

```text
Perfect! Now I have comprehensive information. Let me compile the findings for you.

## Summary of Findings

### TrajAD (arxiv 2602.06443) - Verification of Benchmarks

**Critical finding:** TrajAD **does NOT** evaluate on ALFWorld, GAIA, WebShop, or any other standard agent benchmarks directly.

**What TrajAD actually evaluates on:**
- **TrajBench** only - a custom dataset created by the authors
- Constructed from 60,000+ trajectories (1:1 balanced normal/anomalous samples)
- Synthesized using a "Perturb-and-Complete" strategy
- Covers 5 domains: Reasoning, Mathematics, Programming, Web Navigation, and Embodied AI
- Includes 13 tasks across these domains
- Source data derived from AgentBank, an existing trajectory collection that authors modified

**Critical limitation:** TrajAD evaluates anomaly detection and error localization capabilities in isolation on their synthetic dataset. The paper does NOT report end-to-end results showing how rollback-and-retry functionality improves actual agent success rates on real-world benchmarks like ALFWorld, GAIA, or WebShop.

**Rollback-and-retry capability:** While TrajAD proposes rollback-and-retry conceptually (halting at step t and rolling back to t-1), there is no evidence from the paper that this is actually implemented or evaluated on standard agent benchmarks.

---

### Competitor Papers Found

**1. AgentErrorBench** - A more relevant competitor that DOES evaluate on standard benchmarks:
- First dataset of **systematically annotated failure trajectories from ALFWorld, GAIA, and WebShop**
- 200 trajectories total: 100 from ALFWorld, 50 from WebShop, 50 from GAIA
- Provides AgentErrorTaxonomy for failure classification
- Expert annotation at decision-step level
- More directly applicable to your use case than TrajAD

**2. Trajectory Guard** (arxiv 2601.00516):
- Lightweight sequence-aware anomaly detection model
- Achieves F1-scores of 0.88–0.94
- Evaluated on synthetic perturbations AND real-world failures from security audits and multi-agent systems
- More comprehensive evaluation than TrajAD

**3. ATBench** (arxiv 2604.02022):
- Diverse and realistic agent trajectory benchmark
- Designed for trajectory-level safety evaluation
- Covers long-horizon tool use

**4. The Intervention Paradox** (arxiv 2602.03338) - Critical finding on rollback-and-retry:
- Highly relevant: demonstrates that accurate failure prediction does **NOT** guarantee effective intervention
- Even critics with AUROC 0.94 fail to improve performance
- Shows disruption-recovery tradeoff: interventions can disrupt otherwise successful trajectories
- Important for understanding rollback limitations

**5. Where LLM Agents Fail and How They Can Learn From Failures** (arxiv 2509.25370):
- Comprehensive analysis using AgentErrorBench
- Documents cascading failure patterns
- Shows how errors propagate through subsequent decisions

---

### Key Insight

TrajAD is narrower in scope than you may have expected. It's a detection-focused paper on a synthetic dataset (TrajBench), not a benchmark evaluation paper. If you need evidence of rollback-and-retry performance on standard benchmarks, **AgentErrorBench and the related failure analysis papers are more directly applicable**, as they provide actual failure trajectory data from ALFWorld, GAIA, and WebShop with annotations.

---

### Sources
- [TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents](https://arxiv.org/abs/2602.06443)
- [TrajAD HTML version](https://arxiv.org/html/2602.06443)
- [Where LLM Agents Fail and How They Can Learn From Failures](https://arxiv.org/pdf/2509.25370)
- [AgentErrorBench on alphaXiv](https://www.alphaxiv.org/overview/2509.25370v1)
- [The Intervention Paradox](https://arxiv.org/html/2602.03338)
- [Trajectory Guard](https://arxiv.org/html/2601.00516v1)
- [ATBench](https://arxiv.pdf/2604.02022)
- [Enhancing Web Agents with Explicit Rollback Mechanisms](https://aclanthology.org/2026.eacl-short.12.pdf)
- [Agent Trajectory Monitors](https://www.montecarlodata.com/blog-agent-trajectory-monitors)
- [SafeAgent: A Runtime Protection Architecture for Agentic Systems](https://arxiv.org/html/2604.17562v1)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b171c6d-e42e-488f-aaf4-8004dc96523f",
  "isSidechain": false,
  "promptId": "85c410d9-22c4-47d9-a7b3-8ec988288332",
  "type": "user",
  "uuid": "88a50463-f841-4bb0-a7c2-e2827013a9b6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for the paper \"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents\" (arXiv 2602.06443). I need to verify:\n1. Whether TrajAD evaluates on ALFWorld, GAIA, and WebShop directly, or only on its own TrajBench dataset\n2. What benchmarks TrajAD actually uses for evaluation\n3. Whether TrajAD performs rollback-and-retry on any standard agent benchmark\n\nSearch strategies:\n- Search for \"TrajAD trajectory anomaly detection 2026\" \n- Search for \"arxiv 2602.06443\"\n- Try to fetch the abstract/paper from arxiv\n\nAlso search for any new competitor papers I might have missed:\n- \"cascade failure agent detection 2026\"\n- \"agent trajectory monitoring rollback 2026\"\n- \"LLM agent failure prediction intervention 2026\"\n\nReport what you find about TrajAD's actual benchmark coverage and any new related papers.",
    "agentId": "ab6bba0e778b9f88e",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information. Let me compile the findings for you.\n\n## Summary of Findings\n\n### TrajAD (arxiv 2602.06443) - Verification of Benchmarks\n\n**Critical finding:** TrajAD **does NOT** evaluate on ALFWorld, GAIA, WebShop, or any other standard agent benchmarks directly.\n\n**What TrajAD actually evaluates on:**\n- **TrajBench** only - a custom dataset created by the authors\n- Constructed from 60,000+ trajectories (1:1 balanced normal/anomalous samples)\n- Synthesized using a \"Perturb-and-Complete\" strategy\n- Covers 5 domains: Reasoning, Mathematics, Programming, Web Navigation, and Embodied AI\n- Includes 13 tasks across these domains\n- Source data derived from AgentBank, an existing trajectory collection that authors modified\n\n**Critical limitation:** TrajAD evaluates anomaly detection and error localization capabilities in isolation on their synthetic dataset. The paper does NOT report end-to-end results showing how rollback-and-retry functionality improves actual agent success rates on real-world benchmarks like ALFWorld, GAIA, or WebShop.\n\n**Rollback-and-retry capability:** While TrajAD proposes rollback-and-retry conceptually (halting at step t and rolling back to t-1), there is no evidence from the paper that this is actually implemented or evaluated on standard agent benchmarks.\n\n---\n\n### Competitor Papers Found\n\n**1. AgentErrorBench** - A more relevant competitor that DOES evaluate on standard benchmarks:\n- First dataset of **systematically annotated failure trajectories from ALFWorld, GAIA, and WebShop**\n- 200 trajectories total: 100 from ALFWorld, 50 from WebShop, 50 from GAIA\n- Provides AgentErrorTaxonomy for failure classification\n- Expert annotation at decision-step level\n- More directly applicable to your use case than TrajAD\n\n**2. Trajectory Guard** (arxiv 2601.00516):\n- Lightweight sequence-aware anomaly detection model\n- Achieves F1-scores of 0.88–0.94\n- Evaluated on synthetic perturbations AND real-world failures from security audits and multi-agent systems\n- More comprehensive evaluation than TrajAD\n\n**3. ATBench** (arxiv 2604.02022):\n- Diverse and realistic agent trajectory benchmark\n- Designed for trajectory-level safety evaluation\n- Covers long-horizon tool use\n\n**4. The Intervention Paradox** (arxiv 2602.03338) - Critical finding on rollback-and-retry:\n- Highly relevant: demonstrates that accurate failure prediction does **NOT** guarantee effective intervention\n- Even critics with AUROC 0.94 fail to improve performance\n- Shows disruption-recovery tradeoff: interventions can disrupt otherwise successful trajectories\n- Important for understanding rollback limitations\n\n**5. Where LLM Agents Fail and How They Can Learn From Failures** (arxiv 2509.25370):\n- Comprehensive analysis using AgentErrorBench\n- Documents cascading failure patterns\n- Shows how errors propagate through subsequent decisions\n\n---\n\n### Key Insight\n\nTrajAD is narrower in scope than you may have expected. It's a detection-focused paper on a synthetic dataset (TrajBench), not a benchmark evaluation paper. If you need evidence of rollback-and-retry performance on standard benchmarks, **AgentErrorBench and the related failure analysis papers are more directly applicable**, as they provide actual failure trajectory data from ALFWorld, GAIA, and WebShop with annotations.\n\n---\n\n### Sources\n- [TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents](https://arxiv.org/abs/2602.06443)\n- [TrajAD HTML version](https://arxiv.org/html/2602.06443)\n- [Where LLM Agents Fail and How They Can Learn From Failures](https://arxiv.org/pdf/2509.25370)\n- [AgentErrorBench on alphaXiv](https://www.alphaxiv.org/overview/2509.25370v1)\n- [The Intervention Paradox](https://arxiv.org/html/2602.03338)\n- [Trajectory Guard](https://arxiv.org/html/2601.00516v1)\n- [ATBench](https://arxiv.pdf/2604.02022)\n- [Enhancing Web Agents with Explicit Rollback Mechanisms](https://aclanthology.org/2026.eacl-short.12.pdf)\n- [Agent Trajectory Monitors](https://www.montecarlodata.com/blog-agent-trajectory-monitors)\n- [SafeAgent: A Runtime Protection Architecture for Agentic Systems](https://arxiv.org/html/2604.17562v1)"
      }
    ],
    "totalDurationMs": 42846,
    "totalTokens": 26348,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2096,
      "cache_read_input_tokens": 23082,
      "output_tokens": 1163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2096
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1163,
          "cache_read_input_tokens": 23082,
          "cache_creation_input_tokens": 2096,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2096,
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
  "sourceToolAssistantUUID": "6b171c6d-e42e-488f-aaf4-8004dc96523f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-09T20:16:46.611Z_

<details><summary>↩ Tool result · `toolu_01ACC8djDYCx2FQyaQeLAvRK`</summary>

```text
Perfect! Now I have all the information I need. Let me compile my findings on all three papers.

## Verification Report: Research Papers

I successfully located and verified all three papers. Here are my findings:

### Paper 1: "Where LLM Agents Fail and How They Can Learn From Failures" (arXiv 2509.25370)

**Status: VERIFIED ✓**

Key claims validated:
- **AgentErrorBench exists**: Confirmed as a dataset of systematically annotated failure trajectories
- **200 expert-annotated trajectories**: CONFIRMED - 200 trajectories total across three environments (GAIA: 50, ALFWorld: 100, WebShop: 50)
- **Cohen's κ = 0.55**: CONFIRMED - The paper reports exactly 0.55 for inter-annotator agreement
- **critical_failure_step field**: CONFIRMED - The HuggingFace dataset (davide221/agenterrorbench) contains this field with step numbers (range: 1-30)
- **HuggingFace dataset**: CONFIRMED - Available at https://huggingface.co/datasets/davide221/agenterrorbench

Additional details found: The dataset contains 18.3 MB across three splits (Train: 139, Validation: 31, Test: 30 rows) and includes fields for critical_failure_module (6 types), failure_types, and failure_reasonings alongside the full trajectories.

---

### Paper 2: "Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents" (arXiv 2601.22352)

**Status: VERIFIED ✓**

Key claims validated:
- **ERR Efficiency Score proxy**: CONFIRMED - The paper defines ERR (Expected Recovery Regret) with Efficiency Score (ES) as the observable predictor
- **Validation threshold δ ≤ 0.05**: CONFIRMED - The paper states "Predicted regret under the ERR–ES law closely matched observed post-failure regret measured from Monte Carlo rollouts, within Δnorm≤0.05"
- **Validates across five benchmarks**: CONFIRMED - The validation is explicitly stated to span "five benchmarks and multiple model scales (8B-32B parameters)"

Additional details: The paper demonstrates that recovery follows a measurable "efficiency-regret manifold" with mechanism-invariant geometry, and the framework enables recovery-aware planning without full simulation.

---

### Paper 3: "The Intervention Paradox" (arXiv 2602.03338)

**Status: VERIFIED ✓ (with partial claim clarification)**

Key claims validated:
- **Generic critics AUROC 0.94**: CONFIRMED - The paper explicitly mentions "LLM critics with strong predictive accuracy (AUROC 0.94)"
- **Up to 26pp degradation**: CONFIRMED - "Intervention caused regressions up to 26 percentage points" on high-success tasks (HotPotQA)
- **Regressions at steps 0-1**: CONFIRMED - The paper identifies "Most harm occurred when interventions disrupted correct early steps (steps 0-1), triggering cascading failures"

The paper reveals a "disruption-recovery tradeoff" where interventions help only when baseline failure rate exceeds the threshold: p > d/(r+d).

---

## Summary

All three papers **exist and are accurately described**. The specific technical claims about:
1. Cohen's κ = 0.55 with 200 expert-annotated trajectories and critical_failure_step field
2. δ ≤ 0.05 validation threshold across five benchmarks  
3. AUROC 0.94, 26pp degradation, and steps 0-1 regressions

are all **confirmed and accurate** based on the papers' published content.

Sources:
- [arXiv 2509.25370 Abstract](https://arxiv.org/abs/2509.25370)
- [AgentErrorBench on HuggingFace](https://huggingface.co/datasets/davide221/agenterrorbench)
- [arXiv 2601.22352 Full Text](https://arxiv.org/html/2601.22352)
- [arXiv 2602.03338 Full Text](https://arxiv.org/html/2602.03338)
- [AgentDebug GitHub Repository](https://github.com/ulab-uiuc/AgentDebug)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ab03e16-a3e9-4307-8fd5-b12b960af23f",
  "isSidechain": false,
  "promptId": "85c410d9-22c4-47d9-a7b3-8ec988288332",
  "type": "user",
  "uuid": "37cab258-ca9d-4bf8-ae47-36104148b12e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify these specific papers:\n\n1. \"Where LLM Agents Fail and How They Can Learn From Failures\" (arXiv 2509.25370) - supposedly \"AgentErrorBench\" with 200 expert-annotated trajectories across ALFWorld, WebShop, GAIA with Cohen's κ = 0.55\n   - Search: \"arxiv 2509.25370\" and \"AgentErrorBench\"\n   - Verify: Does it contain critical_failure_step field? Is it on HuggingFace as davide221/agenterrorbench?\n\n2. \"Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents\" (arXiv 2601.22352) - supposedly defines ERR Efficiency Score proxy validated within δ ≤ 0.05\n   - Search: \"arxiv 2601.22352\" and \"ERR Efficiency Score recoverability\"\n   - Verify: Does it validate across five benchmarks?\n\n3. \"The Intervention Paradox\" (arXiv 2602.03338) - supposedly shows generic critics (AUROC 0.94) cause up to 26pp degradation, all regressions at steps 0-1\n   - Search: \"arxiv 2602.03338\" and \"intervention paradox agent failure\"\n   - Verify the specific claims about step 0-1 regressions and AUROC 0.94\n\nReport what you find - specifically whether these papers exist and whether the claims match what's described.",
    "agentId": "a87ff885e50e603e5",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have all the information I need. Let me compile my findings on all three papers.\n\n## Verification Report: Research Papers\n\nI successfully located and verified all three papers. Here are my findings:\n\n### Paper 1: \"Where LLM Agents Fail and How They Can Learn From Failures\" (arXiv 2509.25370)\n\n**Status: VERIFIED ✓**\n\nKey claims validated:\n- **AgentErrorBench exists**: Confirmed as a dataset of systematically annotated failure trajectories\n- **200 expert-annotated trajectories**: CONFIRMED - 200 trajectories total across three environments (GAIA: 50, ALFWorld: 100, WebShop: 50)\n- **Cohen's κ = 0.55**: CONFIRMED - The paper reports exactly 0.55 for inter-annotator agreement\n- **critical_failure_step field**: CONFIRMED - The HuggingFace dataset (davide221/agenterrorbench) contains this field with step numbers (range: 1-30)\n- **HuggingFace dataset**: CONFIRMED - Available at https://huggingface.co/datasets/davide221/agenterrorbench\n\nAdditional details found: The dataset contains 18.3 MB across three splits (Train: 139, Validation: 31, Test: 30 rows) and includes fields for critical_failure_module (6 types), failure_types, and failure_reasonings alongside the full trajectories.\n\n---\n\n### Paper 2: \"Recoverability Has a Law: The ERR Measure for Tool-Augmented Agents\" (arXiv 2601.22352)\n\n**Status: VERIFIED ✓**\n\nKey claims validated:\n- **ERR Efficiency Score proxy**: CONFIRMED - The paper defines ERR (Expected Recovery Regret) with Efficiency Score (ES) as the observable predictor\n- **Validation threshold δ ≤ 0.05**: CONFIRMED - The paper states \"Predicted regret under the ERR–ES law closely matched observed post-failure regret measured from Monte Carlo rollouts, within Δnorm≤0.05\"\n- **Validates across five benchmarks**: CONFIRMED - The validation is explicitly stated to span \"five benchmarks and multiple model scales (8B-32B parameters)\"\n\nAdditional details: The paper demonstrates that recovery follows a measurable \"efficiency-regret manifold\" with mechanism-invariant geometry, and the framework enables recovery-aware planning without full simulation.\n\n---\n\n### Paper 3: \"The Intervention Paradox\" (arXiv 2602.03338)\n\n**Status: VERIFIED ✓ (with partial claim clarification)**\n\nKey claims validated:\n- **Generic critics AUROC 0.94**: CONFIRMED - The paper explicitly mentions \"LLM critics with strong predictive accuracy (AUROC 0.94)\"\n- **Up to 26pp degradation**: CONFIRMED - \"Intervention caused regressions up to 26 percentage points\" on high-success tasks (HotPotQA)\n- **Regressions at steps 0-1**: CONFIRMED - The paper identifies \"Most harm occurred when interventions disrupted correct early steps (steps 0-1), triggering cascading failures\"\n\nThe paper reveals a \"disruption-recovery tradeoff\" where interventions help only when baseline failure rate exceeds the threshold: p > d/(r+d).\n\n---\n\n## Summary\n\nAll three papers **exist and are accurately described**. The specific technical claims about:\n1. Cohen's κ = 0.55 with 200 expert-annotated trajectories and critical_failure_step field\n2. δ ≤ 0.05 validation threshold across five benchmarks  \n3. AUROC 0.94, 26pp degradation, and steps 0-1 regressions\n\nare all **confirmed and accurate** based on the papers' published content.\n\nSources:\n- [arXiv 2509.25370 Abstract](https://arxiv.org/abs/2509.25370)\n- [AgentErrorBench on HuggingFace](https://huggingface.co/datasets/davide221/agenterrorbench)\n- [arXiv 2601.22352 Full Text](https://arxiv.org/html/2601.22352)\n- [arXiv 2602.03338 Full Text](https://arxiv.org/html/2602.03338)\n- [AgentDebug GitHub Repository](https://github.com/ulab-uiuc/AgentDebug)"
      }
    ],
    "totalDurationMs": 69535,
    "totalTokens": 29048,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 514,
      "cache_read_input_tokens": 27466,
      "output_tokens": 1063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 514
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1063,
          "cache_read_input_tokens": 27466,
          "cache_creation_input_tokens": 514,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 514,
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
  "sourceToolAssistantUUID": "7ab03e16-a3e9-4307-8fd5-b12b960af23f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "37cab258-ca9d-4bf8-ae47-36104148b12e",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Cascade-specific onset detection via recoverability signals for agent long-horizon tasks",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449"
}
```

---

### Tool result

_source line 17 · 2026-05-09T20:17:13.236Z_

<details><summary>↩ Tool result · `toolu_01KzkUkbrJk2EcbNMFFUnpVr`</summary>

```text
Perfect! Now I have comprehensive information. Let me compile the final report with all the papers I found.

## Comprehensive Report: Recent Papers on LLM Agent Monitoring, Cascade Failure Detection, and Rollback (2025-2026)

Based on my search across recent arXiv papers, I've identified numerous systems that address cascade failure detection, agent failure monitoring, and rollback mechanisms. Here are the key findings organized by relevance to CascadeWatch:

### DIRECTLY RELEVANT PAPERS (Feb-May 2026 - Potential Competitors)

**1. "From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration" (arXiv:2603.04474)**
- **Date:** March 4, 2026
- **Cascade Detection:** YES - Models error propagation and amplification through message dependencies
- **Rollback:** Mentions mitigation strategies for cascade amplification
- **Key Feature:** Identifies three vulnerability classes: cascade amplification, topological sensitivity, and consensus inertia
- **Approach:** Propagation dynamics model using directed dependency graphs with early-stage risk criteria
- **Benchmarks:** Six mainstream multi-agent frameworks tested
- **Status:** COMPETITOR - directly addresses cascade failure detection in multi-agent systems

**2. "Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks" (arXiv:2602.19008)**
- **Date:** February 22, 2026
- **Cascade Detection:** YES - Identifies gradual self-reinforcing drift from canonical solution paths
- **Rollback:** Implicit (detection enables rollback to correct path)
- **Key Feature:** Natural experiment with 22 frontier models on Toolathlon benchmark (108 tasks, 3 runs each)
- **Approach:** Causal analysis of off-canonical tool calls that self-reinforce errors
- **Benchmarks:** Toolathlon (tool-use tasks)
- **Status:** COMPETITOR - targets exactly the cascade failure phenomenon (deviation amplification)

**3. "Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents" (arXiv:2603.29231)**
- **Date:** March 31, 2026
- **Cascade Detection:** YES - Studies how errors cascade across agents in multi-agent pipelines
- **Rollback:** Not primary focus but discusses reliability composition
- **Key Feature:** Distinguishes capability (pass@1) from reliability (across repeated invocations)
- **Approach:** Framework for evaluating long-horizon reliability vs. short-horizon capability
- **Benchmarks:** Custom multi-agent pipeline studies
- **Status:** COMPETITOR - addresses cascade failures in reliability framework

### AGENT TRAJECTORY MONITORING & ANOMALY DETECTION (Recent, 2026)

**4. "TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents" (arXiv:2602.06443)**
- **Date:** February 6, 2026
- **Cascade Detection:** YES - Detects anomalies that could cascade
- **Rollback:** YES - Error localization enables efficient "rollback-and-retry"
- **Key Feature:** Specialized verifier with fine-grained process supervision
- **Approach:** Fine-tuned model with TrajBench (perturb-and-complete dataset)
- **Benchmarks:** TrajBench (synthesized procedural anomalies)
- **Status:** COMPETITOR - trajectory-level anomaly detection with rollback capability

**5. "Trajectory Guard -- A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI" (arXiv:2601.00516)**
- **Date:** January 2026
- **Cascade Detection:** YES - Detects structural incoherence and contextual misalignment
- **Rollback:** Implicit (real-time detection enables intervention)
- **Key Feature:** Siamese Recurrent Autoencoder with hybrid loss (contrastive + reconstruction)
- **Approach:** Task-trajectory alignment via contrastive learning + sequential validity via reconstruction
- **Performance:** F1 0.88-0.94 on balanced sets, 17-27x faster than LLM judges
- **Benchmarks:** RAS-Eval, Who&When, synthetic perturbations
- **Status:** COMPETITOR - real-time trajectory anomaly detection, similar embedding-based approach

**6. "AgentRx: Diagnosing AI Agent Failures from Execution Trajectories" (arXiv:2602.02475)**
- **Date:** February 2, 2026
- **Cascade Detection:** YES - Identifies critical failure steps that cascade
- **Rollback:** YES - Localization enables targeted rollback/retry
- **Key Feature:** Pinpoints critical failure step in failed trajectories
- **Approach:** Normalizes heterogeneous logs, synthesizes constraints, produces validation log with evidence
- **Performance:** +23.6% absolute improvement in failure localization over LLM baselines
- **Benchmarks:** Tau-bench (APIs), Flash (incident management), Magentic-One (web/file tasks) - 115 failures annotated
- **Status:** COMPETITOR - systematic failure diagnosis with 9-category taxonomy
- **Note:** Microsoft open-sourced this framework

**7. "ATBench: A Diverse and Realistic Agent Trajectory Benchmark for Safety Evaluation and Diagnosis" (arXiv:2604.02022)**
- **Date:** April 2026
- **Cascade Detection:** YES - Taxonomy includes failure modes that cascade
- **Rollback:** Enables diagnosis for rollback decisions
- **Key Feature:** 1,000 trajectories (503 safe, 497 unsafe) with delayed-trigger protocol for long-horizon risk
- **Approach:** Three dimensions: risk source, failure mode, real-world harm
- **Benchmarks:** 1,000 trajectories, 3.95k tokens avg, 2,084 available tools
- **Status:** COMPETITOR - trajectory-level safety benchmark for cascade evaluation

### FAILURE ROOT CAUSE & DIAGNOSIS (2026)

**8. "AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems" (arXiv:2603.14688)**
- **Date:** March 2026
- **Cascade Detection:** YES - Reconstructs causal propagation paths
- **Rollback:** Enables targeted rollback through root cause identification
- **Key Feature:** Lightweight post-hoc failure diagnosis framework
- **Approach:** Reconstructs causal graphs from logs, traces backward from errors
- **Benchmarks:** Deployed multi-agent workflows
- **Status:** COMPETITOR - causal tracing for cascade root cause analysis

**9. "Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?" (arXiv:2602.09937)**
- **Date:** February 2026
- **Cascade Detection:** YES - 12 pitfall types across agent interactions
- **Rollback:** Addresses systematic failures preventing corrective action
- **Key Feature:** 1,675 agent runs across 5 LLMs, classified into 12 pitfall types
- **Approach:** Intra-agent reasoning, inter-agent communication, agent-environment interaction analysis
- **Benchmarks:** OpenRCA benchmark
- **Status:** COMPETITOR - systematic failure analysis preventing cascade

**10. "Why Do Multi-Agent LLM Systems Fail?" (arXiv:2503.13657)**
- **Date:** March 2025
- **Cascade Detection:** YES - Identifies cascading effects across failure categories
- **Rollback:** Not primary focus
- **Key Feature:** Identifies cascading failure phenomena
- **Status:** COMPETITOR - early work on cascade failure categorization

### PROACTIVE MONITORING & INTERVENTION (2026)

**11. "ProbGuard/Pro2Guard: Proactive Runtime Enforcement of LLM Agent Safety via Probabilistic Model Checking" (arXiv:2508.00500)**
- **Date:** August 2025 (updated 2026)
- **Cascade Detection:** YES - Anticipates future unsafe states probabilistically
- **Rollback:** YES - Proactive intervention before violation occurs
- **Key Feature:** Probabilistic risk prediction model
- **Approach:** Estimates probability of reaching unsafe states, triggers intervention with risk context
- **Status:** COMPETITOR - proactive failure prevention vs. reactive detection

**12. "SentinelAgent: Graph-based Anomaly Detection in LLM-based Multi-Agent Systems" (arXiv:2505.24201)**
- **Date:** May 2025
- **Cascade Detection:** YES - Detects multi-agent collusion and latent exploit paths
- **Rollback:** YES - Oversight agent can intervene in execution
- **Key Feature:** Graph-based execution modeling, semantic anomaly detection
- **Approach:** Dynamic execution graphs with rule-based + LLM-based reasoning, pluggable oversight agent
- **Benchmarks:** Email assistant, Microsoft Magentic-One
- **Status:** COMPETITOR - graph-based multi-agent cascade detection

**13. "AI Runtime Infrastructure" (arXiv:2603.00495)**
- **Date:** February/March 2026
- **Cascade Detection:** YES - Detects emerging failure modes during runtime
- **Rollback:** YES - Active recovery mechanisms, rollback to safe states
- **Key Feature:** Monitoring evolving state, detecting failure modes, applying corrective actions
- **Approach:** Active intervention through memory management, control-flow adjustment, policy enforcement
- **Status:** COMPETITOR - runtime intervention framework

### SELF-CORRECTION & BACKTRACKING

**14. "BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism" (arXiv:2505.20660)**
- **Date:** May 27, 2025
- **Cascade Detection:** YES - Error detection and prevention
- **Rollback:** YES - Explicit backtracking mechanism
- **Key Feature:** Verifier, judger, reflector components for error recovery
- **Approach:** Training dataset for backtracking with outcome-page consideration
- **Benchmarks:** Mobile3M, Auto-UI
- **Status:** COMPETITOR - explicit backtracking for GUI agents

### RELATED FOUNDATIONAL WORK (Early 2026)

**15. "Diagnosing Failure Root Causes in Platform-Orchestrated Agentic Systems: Dataset, Taxonomy, and Benchmark" (arXiv:2509.23735)**
- **Date:** September 2025 (continuing into 2026)
- **Cascade Detection:** YES - Fine-grained failure annotation with root cause linking
- **Rollback:** Enables targeted intervention
- **Benchmarks:** AgentFail dataset with 307 failure logs from 10 agentic systems
- **Status:** FOUNDATIONAL - failure root cause dataset and taxonomy

**16. "Beyond Fluency: Toward Reliable Trajectories in Agentic IR" (arXiv:2604.04269)**
- **Date:** April 2026
- **Cascade Detection:** YES - Addresses "Snowball Effect" where minor divergence cascades
- **Rollback:** YES - Recommends state externalization for "dry-run" before live API calls
- **Key Feature:** Causal attribution to pinpoint responsible failure step
- **Approach:** Trajectory analysis with state provenance tracking
- **Status:** COMPETITOR - cascade effect analysis in IR agents

**17. "Sherlock: Reliable and Efficient Agentic Workflow Execution" (arXiv:2511.00330)**
- **Date:** November 2025
- **Cascade Detection:** YES - Early mistake propagation detection
- **Rollback:** YES - Speculative execution with intelligent rollback
- **Key Feature:** Selective verification preventing downstream contamination
- **Performance:** 48.7% latency reduction, 26% cost reduction
- **Status:** COMPETITOR - speculative execution with rollback

**18. "Agent Mentor: Framing Agent Knowledge through Semantic Trajectory Analysis" (arXiv:2604.10513)**
- **Date:** April 2026
- **Cascade Detection:** Implicit - Learning from trajectories
- **Rollback:** Enables memory-based prevention
- **Approach:** Semantic trajectory analysis for agent knowledge
- **Status:** RELATED - trajectory-based learning to prevent future cascades

**19. "Trajectory-Informed Memory Generation for Self-Improving Agent Systems" (arXiv:2603.10600)**
- **Date:** March 2026
- **Cascade Detection:** Implicit - Extracting learnings from failed trajectories
- **Rollback:** Enables prevention of similar failures
- **Approach:** Automatic actionable learning extraction
- **Status:** RELATED - self-improving via trajectory analysis

### MULTI-AGENT CASCADE SYSTEMS

**20. "Cascade-Aware Multi-Agent Routing: Spatio-Temporal Sidecars and Geometry-Switching" (arXiv:2603.17112)**
- **Date:** March 2026
- **Cascade Detection:** YES - Studies how failures cascade in different topologies
- **Rollback:** Not primary focus
- **Key Feature:** Tree-like vs. cyclic graph topology analysis
- **Status:** FOUNDATIONAL - cascade topology analysis

---

## Key Findings Summary

### Papers Most Similar to CascadeWatch (Feb-May 2026)
The closest competitors addressing cascade failure detection in long-horizon agent tasks are:

1. **From Spark to Fire (2603.04474)** - Direct cascade modeling with dependency graphs
2. **Capable but Unreliable (2602.19008)** - Canonical path deviation causing cascades
3. **TrajAD (2602.06443)** - Trajectory anomaly detection with rollback capability
4. **Trajectory Guard (2601.00516)** - Embedding-based anomaly detection (similar to frozen embeddings approach)
5. **AgentRx (2602.02475)** - Systematic failure diagnosis from trajectories
6. **ATBench (2604.02022)** - Trajectory-level safety evaluation benchmark

### Distinguishing Features of CascadeWatch
Your approach using **frozen LLM embeddings + recoverability signals** appears unique because:
- Most papers use trajectory anomaly detection (TrajAD, Trajectory Guard) rather than embedding-based probing
- Most focus on root cause diagnosis rather than proactive cascade prediction
- Most don't combine embedding freezing with recoverability signals as early warning mechanism
- The emphasis on "recoverability signals" as trigger for rollback is novel vs. pure detection

### Benchmarks Being Used
- **ATBench** - Most comprehensive (1,000 trajectories)
- **OpenRCA** - Cloud root cause analysis
- **Toolathlon** - Real-world tool-use tasks
- **Mobile3M/Auto-UI** - GUI agent tasks
- **RAS-Eval/Who&When** - Multi-agent systems
- Tau-bench, Flash, Magentic-One - Domain-specific

### Research Velocity
The volume of papers (20+) in just Feb-May 2026 indicates this is an extremely hot area, with multiple concurrent approaches suggesting significant commercial/research demand.

Sources:
- [From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration](https://arxiv.org/abs/2603.04474)
- [Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks](https://arxiv.org/abs/2602.19008)
- [Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents](https://arxiv.org/html/2603.29231v1)
- [TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents](https://arxiv.org/abs/2602.06443)
- [Trajectory Guard -- A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI](https://arxiv.org/abs/2601.00516)
- [AgentRx: Diagnosing AI Agent Failures from Execution Trajectories](https://arxiv.org/abs/2602.02475)
- [ATBench: A Diverse and Realistic Agent Trajectory Benchmark for Safety Evaluation and Diagnosis](https://arxiv.org/abs/2604.02022)
- [AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems](https://arxiv.org/abs/2603.14688)
- [Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?](https://arxiv.org/abs/2602.09937)
- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/html/2503.13657v1)
- [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://arxiv.org/abs/2505.20660)
- [SentinelAgent: Graph-based Anomaly Detection in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2505.24201)
- [AI Runtime Infrastructure](https://arxiv.org/pdf/2603.00495)
- [Beyond Fluency: Toward Reliable Trajectories in Agentic IR](https://arxiv.org/html/2604.04269)
- [Sherlock: Reliable and Efficient Agentic Workflow Execution](https://arxiv.org/pdf/2511.00330)
- [Agent Mentor: Framing Agent Knowledge through Semantic Trajectory Analysis](https://arxiv.org/html/2604.10513)
- [Trajectory-Informed Memory Generation for Self-Improving Agent Systems](https://arxiv.org/abs/2603.10600)
- [Cascade-Aware Multi-Agent Routing: Spatio-Temporal Sidecars and Geometry-Switching](https://arxiv.org/abs/2603.17112)
- [Diagnosing Failure Root Causes in Platform-Orchestrated Agentic Systems](https://arxiv.org/pdf/2509.23735)
- [ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety](https://arxiv.org/html/2508.00500)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "196b257b-d119-49c6-b0cc-be511eba1082",
  "isSidechain": false,
  "promptId": "85c410d9-22c4-47d9-a7b3-8ec988288332",
  "type": "user",
  "uuid": "3b0505b6-ecf4-4dd2-86b1-053118bc9a91",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent (2025-2026) papers on LLM agent monitoring, cascade failure detection, and rollback mechanisms. I need to find any papers that might be competitors to \"CascadeWatch\" - a system that detects cascade failures in long-horizon agent tasks using frozen LLM embeddings + recoverability signals to trigger rollback.\n\nSearch queries to try:\n1. \"arxiv 2025 2026 agent trajectory monitoring cascade failure rollback\"\n2. \"LLM agent self-correction backtracking cascade 2026\"\n3. \"agent failure detection probe hidden states trajectory 2026\"\n4. \"agent cascade error proactive detection intervention 2026\"\n5. site:arxiv.org \"cascade failure\" \"LLM agent\" 2026\n6. \"agent monitoring rollback recoverability 2026\"\n7. \"BacktrackAgent\" arXiv 2505.20660 - verify this exists\n8. \"Canonical path deviation\" agent failure arXiv 2602.19008 - verify this\n\nFor each paper found, note: title, venue/arXiv ID, whether it does cascade detection, whether it does rollback, what benchmarks it uses.\n\nSpecifically focus on finding any papers from the last 3 months (Feb-May 2026) that might be concurrent/competitor work not yet cited.",
    "agentId": "a2bb7453a00484f84",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information. Let me compile the final report with all the papers I found.\n\n## Comprehensive Report: Recent Papers on LLM Agent Monitoring, Cascade Failure Detection, and Rollback (2025-2026)\n\nBased on my search across recent arXiv papers, I've identified numerous systems that address cascade failure detection, agent failure monitoring, and rollback mechanisms. Here are the key findings organized by relevance to CascadeWatch:\n\n### DIRECTLY RELEVANT PAPERS (Feb-May 2026 - Potential Competitors)\n\n**1. \"From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration\" (arXiv:2603.04474)**\n- **Date:** March 4, 2026\n- **Cascade Detection:** YES - Models error propagation and amplification through message dependencies\n- **Rollback:** Mentions mitigation strategies for cascade amplification\n- **Key Feature:** Identifies three vulnerability classes: cascade amplification, topological sensitivity, and consensus inertia\n- **Approach:** Propagation dynamics model using directed dependency graphs with early-stage risk criteria\n- **Benchmarks:** Six mainstream multi-agent frameworks tested\n- **Status:** COMPETITOR - directly addresses cascade failure detection in multi-agent systems\n\n**2. \"Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks\" (arXiv:2602.19008)**\n- **Date:** February 22, 2026\n- **Cascade Detection:** YES - Identifies gradual self-reinforcing drift from canonical solution paths\n- **Rollback:** Implicit (detection enables rollback to correct path)\n- **Key Feature:** Natural experiment with 22 frontier models on Toolathlon benchmark (108 tasks, 3 runs each)\n- **Approach:** Causal analysis of off-canonical tool calls that self-reinforce errors\n- **Benchmarks:** Toolathlon (tool-use tasks)\n- **Status:** COMPETITOR - targets exactly the cascade failure phenomenon (deviation amplification)\n\n**3. \"Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents\" (arXiv:2603.29231)**\n- **Date:** March 31, 2026\n- **Cascade Detection:** YES - Studies how errors cascade across agents in multi-agent pipelines\n- **Rollback:** Not primary focus but discusses reliability composition\n- **Key Feature:** Distinguishes capability (pass@1) from reliability (across repeated invocations)\n- **Approach:** Framework for evaluating long-horizon reliability vs. short-horizon capability\n- **Benchmarks:** Custom multi-agent pipeline studies\n- **Status:** COMPETITOR - addresses cascade failures in reliability framework\n\n### AGENT TRAJECTORY MONITORING & ANOMALY DETECTION (Recent, 2026)\n\n**4. \"TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents\" (arXiv:2602.06443)**\n- **Date:** February 6, 2026\n- **Cascade Detection:** YES - Detects anomalies that could cascade\n- **Rollback:** YES - Error localization enables efficient \"rollback-and-retry\"\n- **Key Feature:** Specialized verifier with fine-grained process supervision\n- **Approach:** Fine-tuned model with TrajBench (perturb-and-complete dataset)\n- **Benchmarks:** TrajBench (synthesized procedural anomalies)\n- **Status:** COMPETITOR - trajectory-level anomaly detection with rollback capability\n\n**5. \"Trajectory Guard -- A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI\" (arXiv:2601.00516)**\n- **Date:** January 2026\n- **Cascade Detection:** YES - Detects structural incoherence and contextual misalignment\n- **Rollback:** Implicit (real-time detection enables intervention)\n- **Key Feature:** Siamese Recurrent Autoencoder with hybrid loss (contrastive + reconstruction)\n- **Approach:** Task-trajectory alignment via contrastive learning + sequential validity via reconstruction\n- **Performance:** F1 0.88-0.94 on balanced sets, 17-27x faster than LLM judges\n- **Benchmarks:** RAS-Eval, Who&When, synthetic perturbations\n- **Status:** COMPETITOR - real-time trajectory anomaly detection, similar embedding-based approach\n\n**6. \"AgentRx: Diagnosing AI Agent Failures from Execution Trajectories\" (arXiv:2602.02475)**\n- **Date:** February 2, 2026\n- **Cascade Detection:** YES - Identifies critical failure steps that cascade\n- **Rollback:** YES - Localization enables targeted rollback/retry\n- **Key Feature:** Pinpoints critical failure step in failed trajectories\n- **Approach:** Normalizes heterogeneous logs, synthesizes constraints, produces validation log with evidence\n- **Performance:** +23.6% absolute improvement in failure localization over LLM baselines\n- **Benchmarks:** Tau-bench (APIs), Flash (incident management), Magentic-One (web/file tasks) - 115 failures annotated\n- **Status:** COMPETITOR - systematic failure diagnosis with 9-category taxonomy\n- **Note:** Microsoft open-sourced this framework\n\n**7. \"ATBench: A Diverse and Realistic Agent Trajectory Benchmark for Safety Evaluation and Diagnosis\" (arXiv:2604.02022)**\n- **Date:** April 2026\n- **Cascade Detection:** YES - Taxonomy includes failure modes that cascade\n- **Rollback:** Enables diagnosis for rollback decisions\n- **Key Feature:** 1,000 trajectories (503 safe, 497 unsafe) with delayed-trigger protocol for long-horizon risk\n- **Approach:** Three dimensions: risk source, failure mode, real-world harm\n- **Benchmarks:** 1,000 trajectories, 3.95k tokens avg, 2,084 available tools\n- **Status:** COMPETITOR - trajectory-level safety benchmark for cascade evaluation\n\n### FAILURE ROOT CAUSE & DIAGNOSIS (2026)\n\n**8. \"AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems\" (arXiv:2603.14688)**\n- **Date:** March 2026\n- **Cascade Detection:** YES - Reconstructs causal propagation paths\n- **Rollback:** Enables targeted rollback through root cause identification\n- **Key Feature:** Lightweight post-hoc failure diagnosis framework\n- **Approach:** Reconstructs causal graphs from logs, traces backward from errors\n- **Benchmarks:** Deployed multi-agent workflows\n- **Status:** COMPETITOR - causal tracing for cascade root cause analysis\n\n**9. \"Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?\" (arXiv:2602.09937)**\n- **Date:** February 2026\n- **Cascade Detection:** YES - 12 pitfall types across agent interactions\n- **Rollback:** Addresses systematic failures preventing corrective action\n- **Key Feature:** 1,675 agent runs across 5 LLMs, classified into 12 pitfall types\n- **Approach:** Intra-agent reasoning, inter-agent communication, agent-environment interaction analysis\n- **Benchmarks:** OpenRCA benchmark\n- **Status:** COMPETITOR - systematic failure analysis preventing cascade\n\n**10. \"Why Do Multi-Agent LLM Systems Fail?\" (arXiv:2503.13657)**\n- **Date:** March 2025\n- **Cascade Detection:** YES - Identifies cascading effects across failure categories\n- **Rollback:** Not primary focus\n- **Key Feature:** Identifies cascading failure phenomena\n- **Status:** COMPETITOR - early work on cascade failure categorization\n\n### PROACTIVE MONITORING & INTERVENTION (2026)\n\n**11. \"ProbGuard/Pro2Guard: Proactive Runtime Enforcement of LLM Agent Safety via Probabilistic Model Checking\" (arXiv:2508.00500)**\n- **Date:** August 2025 (updated 2026)\n- **Cascade Detection:** YES - Anticipates future unsafe states probabilistically\n- **Rollback:** YES - Proactive intervention before violation occurs\n- **Key Feature:** Probabilistic risk prediction model\n- **Approach:** Estimates probability of reaching unsafe states, triggers intervention with risk context\n- **Status:** COMPETITOR - proactive failure prevention vs. reactive detection\n\n**12. \"SentinelAgent: Graph-based Anomaly Detection in LLM-based Multi-Agent Systems\" (arXiv:2505.24201)**\n- **Date:** May 2025\n- **Cascade Detection:** YES - Detects multi-agent collusion and latent exploit paths\n- **Rollback:** YES - Oversight agent can intervene in execution\n- **Key Feature:** Graph-based execution modeling, semantic anomaly detection\n- **Approach:** Dynamic execution graphs with rule-based + LLM-based reasoning, pluggable oversight agent\n- **Benchmarks:** Email assistant, Microsoft Magentic-One\n- **Status:** COMPETITOR - graph-based multi-agent cascade detection\n\n**13. \"AI Runtime Infrastructure\" (arXiv:2603.00495)**\n- **Date:** February/March 2026\n- **Cascade Detection:** YES - Detects emerging failure modes during runtime\n- **Rollback:** YES - Active recovery mechanisms, rollback to safe states\n- **Key Feature:** Monitoring evolving state, detecting failure modes, applying corrective actions\n- **Approach:** Active intervention through memory management, control-flow adjustment, policy enforcement\n- **Status:** COMPETITOR - runtime intervention framework\n\n### SELF-CORRECTION & BACKTRACKING\n\n**14. \"BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism\" (arXiv:2505.20660)**\n- **Date:** May 27, 2025\n- **Cascade Detection:** YES - Error detection and prevention\n- **Rollback:** YES - Explicit backtracking mechanism\n- **Key Feature:** Verifier, judger, reflector components for error recovery\n- **Approach:** Training dataset for backtracking with outcome-page consideration\n- **Benchmarks:** Mobile3M, Auto-UI\n- **Status:** COMPETITOR - explicit backtracking for GUI agents\n\n### RELATED FOUNDATIONAL WORK (Early 2026)\n\n**15. \"Diagnosing Failure Root Causes in Platform-Orchestrated Agentic Systems: Dataset, Taxonomy, and Benchmark\" (arXiv:2509.23735)**\n- **Date:** September 2025 (continuing into 2026)\n- **Cascade Detection:** YES - Fine-grained failure annotation with root cause linking\n- **Rollback:** Enables targeted intervention\n- **Benchmarks:** AgentFail dataset with 307 failure logs from 10 agentic systems\n- **Status:** FOUNDATIONAL - failure root cause dataset and taxonomy\n\n**16. \"Beyond Fluency: Toward Reliable Trajectories in Agentic IR\" (arXiv:2604.04269)**\n- **Date:** April 2026\n- **Cascade Detection:** YES - Addresses \"Snowball Effect\" where minor divergence cascades\n- **Rollback:** YES - Recommends state externalization for \"dry-run\" before live API calls\n- **Key Feature:** Causal attribution to pinpoint responsible failure step\n- **Approach:** Trajectory analysis with state provenance tracking\n- **Status:** COMPETITOR - cascade effect analysis in IR agents\n\n**17. \"Sherlock: Reliable and Efficient Agentic Workflow Execution\" (arXiv:2511.00330)**\n- **Date:** November 2025\n- **Cascade Detection:** YES - Early mistake propagation detection\n- **Rollback:** YES - Speculative execution with intelligent rollback\n- **Key Feature:** Selective verification preventing downstream contamination\n- **Performance:** 48.7% latency reduction, 26% cost reduction\n- **Status:** COMPETITOR - speculative execution with rollback\n\n**18. \"Agent Mentor: Framing Agent Knowledge through Semantic Trajectory Analysis\" (arXiv:2604.10513)**\n- **Date:** April 2026\n- **Cascade Detection:** Implicit - Learning from trajectories\n- **Rollback:** Enables memory-based prevention\n- **Approach:** Semantic trajectory analysis for agent knowledge\n- **Status:** RELATED - trajectory-based learning to prevent future cascades\n\n**19. \"Trajectory-Informed Memory Generation for Self-Improving Agent Systems\" (arXiv:2603.10600)**\n- **Date:** March 2026\n- **Cascade Detection:** Implicit - Extracting learnings from failed trajectories\n- **Rollback:** Enables prevention of similar failures\n- **Approach:** Automatic actionable learning extraction\n- **Status:** RELATED - self-improving via trajectory analysis\n\n### MULTI-AGENT CASCADE SYSTEMS\n\n**20. \"Cascade-Aware Multi-Agent Routing: Spatio-Temporal Sidecars and Geometry-Switching\" (arXiv:2603.17112)**\n- **Date:** March 2026\n- **Cascade Detection:** YES - Studies how failures cascade in different topologies\n- **Rollback:** Not primary focus\n- **Key Feature:** Tree-like vs. cyclic graph topology analysis\n- **Status:** FOUNDATIONAL - cascade topology analysis\n\n---\n\n## Key Findings Summary\n\n### Papers Most Similar to CascadeWatch (Feb-May 2026)\nThe closest competitors addressing cascade failure detection in long-horizon agent tasks are:\n\n1. **From Spark to Fire (2603.04474)** - Direct cascade modeling with dependency graphs\n2. **Capable but Unreliable (2602.19008)** - Canonical path deviation causing cascades\n3. **TrajAD (2602.06443)** - Trajectory anomaly detection with rollback capability\n4. **Trajectory Guard (2601.00516)** - Embedding-based anomaly detection (similar to frozen embeddings approach)\n5. **AgentRx (2602.02475)** - Systematic failure diagnosis from trajectories\n6. **ATBench (2604.02022)** - Trajectory-level safety evaluation benchmark\n\n### Distinguishing Features of CascadeWatch\nYour approach using **frozen LLM embeddings + recoverability signals** appears unique because:\n- Most papers use trajectory anomaly detection (TrajAD, Trajectory Guard) rather than embedding-based probing\n- Most focus on root cause diagnosis rather than proactive cascade prediction\n- Most don't combine embedding freezing with recoverability signals as early warning mechanism\n- The emphasis on \"recoverability signals\" as trigger for rollback is novel vs. pure detection\n\n### Benchmarks Being Used\n- **ATBench** - Most comprehensive (1,000 trajectories)\n- **OpenRCA** - Cloud root cause analysis\n- **Toolathlon** - Real-world tool-use tasks\n- **Mobile3M/Auto-UI** - GUI agent tasks\n- **RAS-Eval/Who&When** - Multi-agent systems\n- Tau-bench, Flash, Magentic-One - Domain-specific\n\n### Research Velocity\nThe volume of papers (20+) in just Feb-May 2026 indicates this is an extremely hot area, with multiple concurrent approaches suggesting significant commercial/research demand.\n\nSources:\n- [From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration](https://arxiv.org/abs/2603.04474)\n- [Capable but Unreliable: Canonical Path Deviation as a Causal Mechanism of Agent Failure in Long-Horizon Tasks](https://arxiv.org/abs/2602.19008)\n- [Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents](https://arxiv.org/html/2603.29231v1)\n- [TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents](https://arxiv.org/abs/2602.06443)\n- [Trajectory Guard -- A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI](https://arxiv.org/abs/2601.00516)\n- [AgentRx: Diagnosing AI Agent Failures from Execution Trajectories](https://arxiv.org/abs/2602.02475)\n- [ATBench: A Diverse and Realistic Agent Trajectory Benchmark for Safety Evaluation and Diagnosis](https://arxiv.org/abs/2604.02022)\n- [AgentTrace: Causal Graph Tracing for Root Cause Analysis in Deployed Multi-Agent Systems](https://arxiv.org/abs/2603.14688)\n- [Why Do AI Agents Systematically Fail at Cloud Root Cause Analysis?](https://arxiv.org/abs/2602.09937)\n- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/html/2503.13657v1)\n- [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://arxiv.org/abs/2505.20660)\n- [SentinelAgent: Graph-based Anomaly Detection in LLM-based Multi-Agent Systems](https://arxiv.org/abs/2505.24201)\n- [AI Runtime Infrastructure](https://arxiv.org/pdf/2603.00495)\n- [Beyond Fluency: Toward Reliable Trajectories in Agentic IR](https://arxiv.org/html/2604.04269)\n- [Sherlock: Reliable and Efficient Agentic Workflow Execution](https://arxiv.org/pdf/2511.00330)\n- [Agent Mentor: Framing Agent Knowledge through Semantic Trajectory Analysis](https://arxiv.org/html/2604.10513)\n- [Trajectory-Informed Memory Generation for Self-Improving Agent Systems](https://arxiv.org/abs/2603.10600)\n- [Cascade-Aware Multi-Agent Routing: Spatio-Temporal Sidecars and Geometry-Switching](https://arxiv.org/abs/2603.17112)\n- [Diagnosing Failure Root Causes in Platform-Orchestrated Agentic Systems](https://arxiv.org/pdf/2509.23735)\n- [ProbGuard: Probabilistic Runtime Monitoring for LLM Agent Safety](https://arxiv.org/html/2508.00500)"
      }
    ],
    "totalDurationMs": 89885,
    "totalTokens": 39951,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2739,
      "cache_read_input_tokens": 32832,
      "output_tokens": 4373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2739
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 4373,
          "cache_read_input_tokens": 32832,
          "cache_creation_input_tokens": 2739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2739,
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
  "sourceToolAssistantUUID": "196b257b-d119-49c6-b0cc-be511eba1082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3b0505b6-ecf4-4dd2-86b1-053118bc9a91",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Cascade-specific onset detection via recoverability signals for agent long-horizon tasks",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449"
}
```

---

### Assistant

_source line 20 · 2026-05-09T20:19:30.861Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research results. Let me analyze what I've found:

**Key Findings:**

1. **TrajAD benchmark claim - CONFIRMED AS CORRECT**: The Round 9 submission correctly states that TrajAD "does not evaluate on ALFWorld, GAIA, or WebShop in their standard agentic task-completion form" - this was one of the Round 8 required fixes, and it appears the revision correctly addressed it by checking TrajBench.

2. **AgentErrorBench (arXiv 2509.25370) - VERIFIED**: 


The dataset contains 200 expert-annotated trajectories split across train (139), validation (31), and test (30) sets, with the critical_failure_step field and Cohen's κ = 0.55 confirmed. However, there's a constraint I'm noticing: since the training set only has 139 trajectories and they're all failure cases, the cascade-positive label distribution is limited by this smaller pool.

I've now verified the ERR paper's δ ≤ 0.05 threshold across five benchmarks and confirmed the Intervention Paradox findings showing AUROC 0.94 with up to 26pp degradation at early steps. I'm also discovering two new competitors I hadn't seen cited before: AgentRx, which achieves +23.6% improvement in failure localization by pinpointing critical failure steps, and Sherlock, which uses speculative execution with intelligent...

Now I'm reviewing the Round 9 submission against the required changes from Round 8. The TrajAD benchmark claim has been corrected to specify TrajBench-only evaluation, the rollout counts are now consistent at roughly 2,000 total across benchmarks, and the label density mismatch is explicitly acknowledged. I'm checking whether the differentiation from TrajAD is clear—the submission now properly states that TrajAD doesn't evaluate on ALFWorld, GAIA, or WebShop in their standard agentic forms, and includes a TrajAD-style general anomaly detection baseline for comparison.

The rollout math checks out: 333 per benchmark per temperature across three benchmarks and two temperatures equals approximately 2,000 total. But I'm noticing a potential issue with AgentRx (arXiv 2602.02475), which appears to do something very similar but isn't cited.

AgentRx focuses on post-hoc failure localization with a 23.6% improvement, whereas CascadeWatch's real advantage is being an online cascade detector that can actually intervene during inference with rollback capabilities. Then there's Sherlock (arXiv 2511.00330), which uses speculative execution and rollback to achieve 48.7% latency reduction—that's a more direct competitor since it also does rollback, though it seems oriented toward workflow efficiency rather than cascade-specific failure detection in long-horizon tasks.

I'm also seeing ATBench (arXiv 2604.02022) as a potential new finding—it's a trajectory-level safety benchmark with 1,000 trajectories and delayed-trigger mechanisms that might be relevant to the cascade detection problem.

Looking at what could actually hurt the submission: AgentRx isn't cited but the differentiation seems defensible since it's clearly post-hoc. Sherlock is the more concerning one because it combines speculative execution with rollback, which overlaps with CascadeWatch's core mechanism. The data regime is also tight—AgentErrorBench only has 139 training trajectories, all failures by design, and after filtering for confirmed cascades where the root cause appears before the midpoint, the usable training set gets even smaller. estimates 135-155 cascade-positive examples... but wait, the data has only 200 total trajectories including validation and test splits. If using only the train split (139 trajectories), the cascade-positive count would be lower:
   - ALFWorld in train: ~69 trajectories, ~45-52 cascade-positive
   - GAIA in train: ~34 trajectories, ~24-28 cascade-positive
   - WebShop in train: ~36 trajectories, ~24-29 cascade-positive
   
   This means the GAIA probe is in an even more challenging training regime than stated (closer to 24-28 training examples, with only ~8-9 per fold in 3-fold CV). This is a significant concern that makes the "minimum viable supervised learning regime" even more acute.

   The key question is whether they're using all 200 trajectories with their own 3-fold cross-validation stratified by benchmark, or respecting the HuggingFace train/val/test splits. The approach section mentions using 3-fold CV with Platt scaling on a held-out validation split, which suggests they might be using all 200 examples for training—making their 135-155 cascade-positive estimate plausible. But if they're properly withholding the test set, that would reduce the available training data and create ambiguity about what's actually being evaluated.

   Actually, I realize CascadeWatch isn't directly evaluating on AgentErrorBench's test set—it's measuring task success rates on fresh episodes of ALFWorld, GAIA, and WebShop. So using all 200 trajectories for training the probe is methodologically sound; there's no data contamination concern.

   On the Intervention Paradox calibration, the paper claims regressions occur only at steps 0–1 for HotPotQA and GAIA, with ALFWorld being the exception where even early interventions help. This means their step ≥ 5 threshold is overly conservative for ALFWorld specifically, and the submission acknowledges this nuance in how the threshold applies across benchmarks.

   Sherlock is another uncited paper doing speculative execution with intelligent rollback for workflow efficiency, which seems orthogonal to cascade detection via embeddings. Without the full paper, I can't assess if there's a critical overlap, but the core mechanisms appear distinct enough.

**Reviewing the Round 9 submission:**

The previous round's issues have been addressed—TrajAD benchmark claim is corrected, rollout counts are now consistent at 2,000 total, and the label density mismatch is explicitly acknowledged.

Two gaps remain: AgentRx from Microsoft detects critical failure steps post-hoc with strong empirical results (+23.6% improvement), but it's fundamentally different from online cascade detection, so the distinction should be stated clearly. Sherlock appears primarily focused on execution efficiency rather than cascade-specific detection, making it a lower priority concern.

The synthetic label density problem is now honestly framed—training on 200 real examples with maximally dense labels alongside ~2,000 synthetic examples with maximally sparse labels does create a genuine learning contradiction, but the paper addresses this through the AgentErrorBench-only ablation to quantify the noise contribution. The GAIA data regime concern has been resolved by explicitly noting the minimal supervised learning setting (~27 samples per fold across ~35–40 cascade-positive examples) and framing results as preliminary evidence. There's a potential inconsistency flagged about AgentErrorBench's 200 expert-annotated trajectories that needs clarification. 200 are failure trajectories by design (failures are deliberately oversampled)." The label distribution is entirely failure trajectories - which means the probe is trained only on failure examples from AgentErrorBench (cascade-positive vs. non-cascade-positive failure examples), with successful runs coming from synthetic rollouts. This creates an interesting class imbalance question: the real-label training examples have no true negative examples from AgentErrorBench (since all 200 are failures). True negatives come only from successful synthetic trajectories. This is now addressed by the synthetic augmentation, but it means the probe's decision boundary between "cascade-positive" and "non-cascade-positive" on real trajectories is based entirely on AgentErrorBench, while the "success vs. failure" discrimination comes from synthetic data. This is a methodological complexity that the paper now acknowledges.

The cascade-specific detection combined with ERR recoverability signals and intervention calibration feels genuinely novel compared to the crowded field of related systems, though the core probe-and-rollback mechanism itself isn't particularly groundbreaking - the real differentiation comes from the cascade-focused framing and how ERR integrates into it. The approach is technically sound and the compute requirements are realistic, but the label density mismatch and minimal GAIA probe sample size create real training challenges, and some rollback scenarios like WebShop's irreversible web state changes can't be fully undone.

The submission is remarkably thorough and well-grounded in its claims and limitations, which makes it exceptionally clear for an academic venue, though the extreme density might require significant condensation for the actual paper. The impact is meaningful if cascade-specific monitors genuinely outperform generic critics and avoid the intervention paradox degradation, but the gap is fairly specialized and improvements are likely modest across most benchmarks.

I'm settling on around 3.75 overall, which falls short of the 4.0 pass threshold. Since this is Round 9 and not the final round, I can still recommend revisions rather than forcing a binary decision. The main gaps I'm seeing are that AgentRx from Microsoft—which handles failure diagnosis and targeted recovery on several benchmarks—isn't cited as a competitor, and the core contribution still needs clearer validation that the recoverability delta actually demonstrates ERR's value beyond the specific backbone it was trained on.

There's also a real methodological tension here: the GAIA probe with only 27 samples per fold, combined with synthetic label noise and the label density mismatch, creates genuine reproducibility concerns. The paper's results could be artifacts of training toward synthetic failure patterns rather than genuine cascade-specific onset detection. The authors acknowledge this and commit to reporting negative results if the ablation shows minimal F1 lift, which is scientifically honest but also means the core claim could collapse under scrutiny. On top of that, the intervention threshold for ALFWorld appears over-conservative, which the paper recognizes but doesn't fully resolve.

Now looking at the missing citations and related work: AgentRx does something structurally similar with failure diagnosis and targeted rollback, and Sherlock's speculative execution approach should at least be mentioned. These gaps are addressable in revision, but they're meaningful enough that the paper probably needs another round to properly position itself against these competitors. I'm leaning toward revise rather than accept, though the paper has clearly gone through substantial iteration already. revision and has addressed every critical issue raised. The remaining gaps (AgentRx, Sherlock) are moderate at most. The core methodology is sound, the feasibility is demonstrated, the differentiation from existing work is comprehensive.

The average scores I'd assign:
- Novelty: 3.5 (crowded space, but genuinely differentiated approach)
- Feasibility: 3.5 (technically sound, acknowledged limitations, within compute budget)
- Clarity: 4.5 (extremely detailed and precise)
- Impact: 3.5 (useful but modest contribution, results could be mixed)

Average: 3.75 - below the 4.0 pass threshold.

Given this is Round 9, I should give "revise" with two targeted remaining issues:
1. Cite AgentRx (Microsoft, Feb 2026) - it's a legitimate uncited competitor
2. Address whether Sherlock needs citation

But I'm realizing the novelty argument hinges on whether the ERR recoverability signals actually deliver meaningful lift over embeddings alone. If the ablation shows less than 3% improvement—the paper's own threshold—then the core novelty claim collapses to just embeddings plus step thresholding plus rollback, which is far less differentiated. The whole contribution is contingent on experimental results that haven't been validated yet. The Round 9 submission has addressed all the required changes from Round 8, leaving just a couple of remaining gaps—AgentRx needs a citation for its conceptual overlap with the failure step identification approach, and Sherlock is a minor positioning issue. Given the paper's substantial improvements across eight rounds of revision, solid methodology, and real contribution, I'm leaning toward REVISE for Round 9 with AgentRx as the primary note, which should set things up for a potential acceptance in Round 10.

Actually, reconsidering AgentRx more carefully—it's fundamentally a post-hoc diagnosis tool that identifies failure points after the fact, whereas CascadeWatch operates online during execution to detect and prevent cascading failures. The differentiation is clear and substantial enough that an EMNLP reviewer wouldn't see them as directly competing, so the citation is more of a nice-to-have than a critical gap.

Now looking at the Round 9 submission more realistically: the novelty is solid with the combination of ERR signals, cascade-specific labels, and Intervention Paradox calibration—I'd rate that around 3.5. Feasibility checks out at 3.5-4 with sound mechanisms and acknowledged limitations. The clarity is strong at 4.5. The real impact would be demonstrating that cascade-specific monitors outperform generic critics in this regime, which is a meaningful contribution to agent reliability. The question is whether these scores average above the 4.0 threshold. Reconsidering my scoring more carefully: novelty deserves a 4 since the cascade-specific detection approach and Intervention Paradox framing are genuinely novel contributions, and feasibility is clearly a 4 with all mechanisms specified and timeline realistic. That puts me at exactly 4.0 average with clarity at 4.5 and impact at 3.5, which technically meets the threshold—but I'm second-guessing whether I should be this generous given how high the bar actually is. 0 meaning novelty of 4 is actually justified? In an area as crowded as agent monitoring/cascade detection, getting a novelty of 4 requires the approach to stand out meaningfully. The ERR integration + Intervention Paradox calibration is genuinely novel, but the probe-based approach to agent monitoring is well-established.

I'll give novelty 3.5, not 4.

**Final scoring:**
- Novelty: 3.5
- Feasibility: 4.0
- Clarity: 4.5
- Impact: 3.5

Average: (3.5 + 4 + 4.5 + 3.5) / 4 = 3.875 - below 4.0 threshold.

Verdict: **REVISE** for Round 9, with the note that the remaining issues are minor and the paper is close to pass-ready.

For the revision, I need to flag that AgentRx from Microsoft is uncited—it does post-hoc failure diagnosis with a 9-category taxonomy, which overlaps conceptually, though CascadeWatch's online monitoring and rollback mechanism differentiate it. There's also a foundational tension worth addressing: the GAIA probe trains on only ~27 samples per fold, which is barely viable for supervised learning, and mixing sparse real labels with dense synthetic ones could create conflicting decision boundaries that the ablation might not fully capture if the MLP just learns a compromise.

But stepping back, the paper actually acknowledges all the key limitations honestly—GAIA sample size, label density mismatch, synthetic proxy coarseness, ALFWorld game score proxy, WebShop irreversibility. These are methodological constraints handled with appropriate ablations and caveats, which is good science. The only genuinely uncited but potentially relevant work is AgentRx, which is moderate, not critical. So the verdict stands: REVISE with AgentRx citation as the primary fix.

Now I'm reconsidering whether REVISE or PASS is the right call. After eight rounds of revision, the critical issues are resolved—the methodology is sound, the resource estimate is accurate, the differentiation is comprehensive, and the paper honestly owns its limitations. The remaining gap is the AgentRx citation and a score just below 4.0, which for EMNLP Findings is reasonable. But with Round 10 being final, I need to weigh whether the contingent novelty and uncited competitor warrant another revision cycle or if the work is ready to move forward.

Given how close this is and that AgentRx is a legitimate Microsoft paper on failure diagnosis that deserves acknowledgment, I'm going with REVISE to give one final chance to address the citation gap. I'm also double-checking the Sherlock paper—it's about speculative execution with intelligent rollback for workflow efficiency, which doesn't really overlap with cascade-specific failure detection, so that's not a concern.

The main issue is that the paper's core novelty hinges on the ERR ablation threshold being ≥3% F1 improvement, which means if that threshold doesn't hold up, the contribution over embeddings-only baselines becomes questionable. The authors are transparent about this contingency, but reviewers might see it as unvalidated. Adding the AgentRx citation with clear differentiation should resolve the primary concern, and then this is ready for EMNLP 2026 Findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b0505b6-ecf4-4dd2-86b1-053118bc9a91",
  "isSidechain": false,
  "requestId": "req_011CascQxMhuwLF9DCwF6Bk8",
  "type": "assistant",
  "uuid": "87eb84ae-767f-45e6-bb9f-782a353bf605",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RjVcEWkBhbQMz1AK8zL1vK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8652,
      "cache_read_input_tokens": 44602,
      "output_tokens": 9044,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9044,
          "cache_read_input_tokens": 44602,
          "cache_creation_input_tokens": 8652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8652
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

_source line 21 · 2026-05-09T20:20:12.060Z_

Now I have the research I need. Let me synthesize my findings and issue the verdict.

**Research findings:**

1. **TrajAD (arXiv 2602.06443)** - CONFIRMED: Evaluates exclusively on its own TrajBench (63,484 synthetic samples), NOT on ALFWorld/GAIA/WebShop directly. The Round 9 submission correctly reflects this.

2. **AgentErrorBench (arXiv 2509.25370)** - VERIFIED: 200 expert-annotated trajectories, critical_failure_step field confirmed on HuggingFace (davide221/agenterrorbench), Cohen's κ = 0.55 confirmed. Dataset has Train:139/Val:31/Test:30 splits.

3. **ERR paper (arXiv 2601.22352)** - VERIFIED: δ ≤ 0.05 validated across five benchmarks, Efficiency Score proxy confirmed.

4. **Intervention Paradox (arXiv 2602.03338)** - VERIFIED: AUROC 0.94, up to 26pp degradation, regressions at steps 0-1 confirmed.

5. **NEW UNCITED COMPETITOR: AgentRx (arXiv 2602.02475)** - "Diagnosing AI Agent Failures from Execution Trajectories" — Microsoft system that pinpoints critical failure steps from agent trajectories using a 9-category failure taxonomy, achieving +23.6% absolute improvement in failure localization on Tau-bench, Flash, and Magentic-One. While post-hoc (not real-time), it is the closest uncited work in terms of critical-failure-step identification.

6. **Sherlock (arXiv 2511.00330)** - "Speculative execution with intelligent rollback" at 48.7% latency reduction. This appears focused on execution efficiency rather than cascade-specific failure detection; differentiation from CascadeWatch is substantial.

**Round 8 required changes - status:**
1. ✓ TrajAD benchmark claim corrected (now accurately states TrajBench-only)
2. ✓ Rollout count made consistent (2,000 total, ~333/benchmark/temperature, consistent across all sections)
3. ✓ Label density mismatch explicitly named and explained with "maximally sparse" vs. "maximally dense" framing

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {
      "score": 3,
      "rationale": "The crowded landscape (9+ differentiated systems cited) and contingent core novelty claim — ERR recoverability deltas must provide ≥3% F1 lift over embeddings alone for the theoretical ERR motivation to hold — means novelty is not yet empirically established. The cascade-specific framing and Intervention Paradox calibration are genuinely novel, but the probe-based approach to trajectory monitoring is well-established, and the differentiation from TrajAD rests primarily on training data quality rather than architectural innovation."
    },
    "feasibility": {
      "score": 4,
      "rationale": "HIL mode (62–93 H100-hours, 12–14 days) is well within the joint constraint; all mechanisms are technically verified (command-replay rollback, context-only for WebShop/GAIA, MLP probe training); resource math is consistent; WebShop is now included in primary evaluation. The label density mismatch and GAIA training sparsity (~27 samples/fold) are real risks but are addressed by dedicated ablation arms."
    },
    "clarity": {
      "score": 4,
      "rationale": "The submission is exceptionally precise — every mechanism is specified, every limitation acknowledged, every differentiation from competing work is stated with three or more concrete distinctions. The label density mismatch is now explicitly named and explained. This level of specification is rare and reduces reviewer ambiguity substantially."
    },
    "impact": {
      "score": 3,
      "rationale": "If the ERR ablation confirms that cascade-specific precision circumvents the Intervention Paradox on all three benchmarks, this would be a meaningful contribution to agent reliability research. However, the primary evidence base is ALFWorld (~65–75 cascade-positive training examples), GAIA results are preliminary, and the Intervention Paradox already found only +0.5 to +2.8pp improvement on ALFWorld even with generic critics — meaning the expected margin for cascade-specific gains over no-correction is modest."
    }
  },
  "issues": [
    "MODERATE — AgentRx (arXiv 2602.02475, February 2026, Microsoft) is uncited despite directly targeting critical failure step identification in agent trajectories. AgentRx normalizes heterogeneous agent logs, synthesizes validation constraints, and pinpoints the critical failure step across a 9-category taxonomy, achieving +23.6% absolute improvement in failure localization on Tau-bench, Flash, and Magentic-One. While AgentRx is post-hoc (applied after task failure is determined, not during execution), its explicit 'critical failure step' framing and trajectory-based diagnosis overlaps conceptually with CascadeWatch's cascade-onset detection. A 1–2 sentence differentiation is required: 'AgentRx diagnoses failure root causes post-hoc from completed failed trajectories, applying a 9-category taxonomy after the task has already failed; CascadeWatch monitors online during execution, triggering rollback before cascade failure compounds — requiring real-time recoverability estimation from prefix statistics rather than complete trajectory analysis.'",
    "MODERATE — The contingent novelty structure creates a self-undermining risk that reviewers will flag: the paper pre-registers that if the recoverability-delta ablation yields <3% F1 lift over embeddings alone, this will be 'reported honestly as a negative result on the recoverability signal hypothesis.' This is admirable scientific honesty, but it means the paper's primary differentiator from embeddings-only probe baselines (the ERR theoretical motivation) is explicitly unvalidated prior to submission. EMNLP reviewers will recognize this and may view the contribution as speculative pending experimental results. The paper should either (a) strengthen the theoretical case for why ERR signals should provide meaningful lift beyond embeddings in this specific setting, or (b) reframe the primary novelty claim around the cascade-specific label design and Intervention Paradox calibration (which are unconditional contributions) rather than centering ERR on the contingent ablation threshold.",
    "MINOR — The AgentErrorBench HuggingFace dataset (davide221/agenterrorbench) has pre-defined train/validation/test splits (Train: 139, Validation: 31, Test: 30). If CascadeWatch applies its own 3-fold cross-validation over all 200 trajectories ignoring these splits, the results may not be comparable to future work that uses the canonical splits. The paper should clarify whether it uses the canonical splits or re-splits the full dataset, and if the latter, explain why (e.g., the canonical test split is too small for reliable cascade-positive class stratification)."
  ],
  "feedback": "Round 9 cleanly resolves all three Round 8 required changes: TrajAD benchmark claim is now accurate (TrajBench-only, no head-to-head framing), rollout counts are consistent (2,000 total, ~333/benchmark/temperature throughout), and the label density mismatch is explicitly named with the 'maximally sparse vs. maximally dense' framing and an AgentErrorBench-only ablation arm to quantify the conflict. The submission is substantively mature after 9 rounds.\n\nTwo targeted changes for Round 10:\n\n1. **Add AgentRx (arXiv 2602.02475) with 1–2 sentence differentiation.** This is a February 2026 Microsoft system that identifies critical failure steps from completed failed trajectories using a 9-category taxonomy. The distinction is: AgentRx is post-hoc (analyzes completed failed trajectories offline); CascadeWatch is online (detects cascade onset during execution from prefix statistics and triggers rollback before failure compounds). This distinction is real and defensible, but the paper's 'critical failure step' framing creates enough conceptual overlap that EMNLP reviewers will find the omission notable.\n\n2. **Reframe the ERR novelty claim as unconditional.** Currently, the paper's most distinctive feature (ERR recoverability deltas as the cascade-specific signal) is framed as contingent: 'if <3% lift, report as negative result.' This positions ERR as a bet rather than a contribution. Strengthen by arguing from first principles why ERR recoverability deltas are the right signal for distinguishing cascade-onset from self-correctable deviations (the compounding cost structure is precisely what the Intervention Paradox's disruption-recovery tradeoff captures), and frame the ablation as an empirical confirmation of a well-motivated design choice rather than a pass/fail gate on the entire contribution. The cascade-specific label design, Intervention Paradox calibration, and expert-annotated training data are unconditional contributions that hold regardless of the ablation result.\n\n3. **Clarify the AgentErrorBench train/val/test split usage.** State explicitly whether the 200 trajectories are pooled for 3-fold CV (ignoring canonical splits) and why, or whether the canonical splits are respected and how this affects the cascade-positive counts per fold.",
  "reason": "All three Round 8 required changes are cleanly addressed, but one moderate uncited competitor (AgentRx, Microsoft, arXiv 2602.02475) and a contingent novelty framing on the ERR ablation require targeted fixes before this is EMNLP-ready."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87eb84ae-767f-45e6-bb9f-782a353bf605",
  "isSidechain": false,
  "requestId": "req_011CascQxMhuwLF9DCwF6Bk8",
  "type": "assistant",
  "uuid": "3a311e7a-0b3e-41bc-bb87-8fbc4559cf75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RjVcEWkBhbQMz1AK8zL1vK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8652,
      "cache_read_input_tokens": 44602,
      "output_tokens": 9044,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9044,
          "cache_read_input_tokens": 44602,
          "cache_creation_input_tokens": 8652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8652
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3a311e7a-0b3e-41bc-bb87-8fbc4559cf75",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Cascade-specific onset detection via recoverability signals for agent long-horizon tasks",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-09 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "3a311e7a-0b3e-41bc-bb87-8fbc4559cf75",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Cascade-specific onset detection via recoverability signals for agent long-horizon tasks",
  "sessionId": "d1d1e179-387b-4b03-977f-20bfd6c5f449"
}
```

---
