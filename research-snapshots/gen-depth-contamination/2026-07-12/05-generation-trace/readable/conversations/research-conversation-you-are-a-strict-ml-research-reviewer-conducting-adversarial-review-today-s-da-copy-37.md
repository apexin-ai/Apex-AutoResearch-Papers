# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-11 (UTC).** Your job: indep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/41899480-887b-407e-aeec-9b978a73446c.jsonl`
- **Structured JSON:** [`6bed3a34bb280e35faf2.json`](../../sessions/6b/6bed3a34bb280e35faf2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-11T23:53:51.251Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-11T23:53:51.251Z",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-11 (UTC).**\n\nYour job: independently verify this idea's claims via WebSearch, then issue a verdict.\n\n## User requirements\nThe user asked for: **Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: LLM Agents.\n\nDirection: LLM Agents — planning algorithms, memory architectures, tool use, multi-agent coordination, agent training (SFT/RL), self-correction in agentic loops, environment feedback exploitation.\n\nContribution type: METHOD ONLY. Must propose a concrete new algorithm, training procedure, or inference-time mechanism. Reject pure benchmark / dataset / analysis ideas. Method + analysis OK if analysis validates the method.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total (baselines + method + ablations). Show the math.\n2. Time: ≤16 days. Build on existing OSS agent codebases (AutoGen, LangGraph, OpenManus, etc.) — no from-scratch systems.\n3. Eval: existing benchmarks only — AgentBench, WebArena, SWE-bench Verified, GAIA, ToolBench, ALFWorld, Mind2Web, τ-bench.\n\nAvoid: generic ReAct variants, plain tool retrieval, naive memory summarization. Look for: agent training with minimal RL budget, structured planning beyond flat CoT, multi-agent communication protocols, agent self-verification mechanisms.\n\nTag: direction=agent, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].**\nYou MUST evaluate whether this idea actually meets the user's requirements. If the user asked for a top venue, assess whether the idea is truly top-venue quality. If the user asked for low resource cost, verify the resource estimate is realistic and low. An idea that doesn't match what the user asked for should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证，深入思考每个维度。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：不要只依赖搜索摘要。用 WebFetch 实际阅读相关论文的 abstract 和关键章节，形成你自己的判断。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass——真正好的 idea 经得起严格审查\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献（不是自说自话的贡献）\n\n6. **评分诚实**：\n   - 不要给\"看起来还行\"的 idea 高分——4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n充分利用你的工具——做真正的调研，不是走过场。\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} {year}` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} {year}` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} {year} site:scholar.google.com` — 或直接搜索让 Google 自动包含 Scholar 结果\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} {year}` — 按活跃作者追踪（找到领域大牛后追踪其最新工作）\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `site:paperswithcode.com {method_name}` — 查看方法是否已被实现\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} {year}` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey {year}` — 找综述论文\n   - `semanticscholar.org {paper_title}` — 查看 cited by（谁引用了这篇）和 references（它引用了谁）\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n   - `site:huggingface.co {model_name}` — 验证模型/数据集是否可获取\n\n### 搜索维度（多角度交叉，不要只按 topic 搜）\n\n对每个 idea/方向，尽量覆盖以下维度：\n\n1. **正向搜索**：直接搜索主题相关论文\n   - `{topic} {subtopic} {year}`\n   - `{method_name} for {task_name}`\n\n2. **竞争论文搜索**（最关键！）：\n   - `{core_problem} {year}` — 有没有人在解决同样的问题？\n   - `{approach_keyword} {task} {year}` — 有没有人用类似方法？\n   - `{gap_description} solution` — 你发现的 gap 是否已被解决？\n   - **搜索知名团队的最新工作**：如果你知道哪些团队在做这个方向，搜索他们最近 6 个月的论文\n\n3. **相邻领域搜索**：\n   - `{method_from_other_field} applied to {your_task}`\n   - `{your_problem} in {adjacent_domain}` — 其他领域是否已解决类似问题\n\n4. **反面搜索**（找到反对你 idea 的证据）：\n   - `{your_approach} limitations` / `{your_approach} failure`\n   - `why {assumed_gap} is not a problem`\n   - `{baseline_method} sufficient for {task}` — baseline 是否其实已经够好\n\n5. **引用链追踪**（发现遗漏工作的最有效方法）：\n   - 找到一篇核心相关论文后，用 WebFetch 阅读它的 references 部分\n   - 在 Semantic Scholar 上查看它的 \"cited by\" — 最近引用它的论文很可能是 concurrent work\n   - 对 3 个以上核心相关论文重复此步骤\n\n### 搜索数量建议（理想目标，上下文充裕时尽量达到）\n\n| 角色 | 建议搜索次数 | 说明 |\n|------|-------------|------|\n| Round 1 Generator | 10-15 次 | 每个方向争取 3 次独立搜索 |\n| Round 2 Generator | 5-8 次 | 验证 approach 可行性 + baseline |\n| Review Agent | 8-12 次 | 独立验证 + 竞争论文 + 反面证据 |\n| Revision Agent | 5-10 次 | 针对每个 issue 独立调研 |\n\n### 上下文管理\n\n你的输出 token 有限，必须在上下文耗尽之前完成 JSON 输出。\n\n- 上述搜索次数是理想目标。在上下文充裕时应尽量多搜、深搜，搜得越充分越好。\n- 但必须动态评估剩余上下文：如果已经消耗了大量上下文，应优先完成输出，不要为了凑次数而冒着无法输出的风险。\n- WebFetch 深度阅读很有价值，但每次 fetch 消耗大量 token——优先 fetch 最关键的 2-3 篇，而不是每篇都 fetch。\n- 质量 > 数量：5 次精准搜索 + 深度思考 > 15 次浅层搜索。\n\n\nAs a reviewer, your search focus should be:\n1. **验证 claim**：Generator 声称的 SOTA、gap、novelty 是否属实\n2. **找竞争论文**：是否有 Generator 遗漏的高度相关/相似的工作\n3. **找反面证据**：是否有论文表明 Generator 的 approach 行不通\n4. **引用链检查**：通过核心论文的 cited-by 发现 concurrent work\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n这是你作为 Reviewer 最重要的职责之一——发现 Generator 遗漏的竞争工作：\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n   - 同义词替换（e.g., 'efficient' → 'lightweight/fast/scalable'）\n   - 不同粒度（e.g., 'text classification' → 'sentiment analysis' → 'NLP'）\n   - 方法名 + 任务名的不同组合\n\n2. **知名团队追踪**：如果你知道哪些团队/实验室在做相关方向，\n   搜索他们最近的论文（`\"team_name\" OR \"author_name\" {topic} {year}`）\n\n3. **会议最新录用**：搜索最近一轮 ICML/NeurIPS/ICLR/AAAI/ACL 等会议的 accepted papers\n   - `site:openreview.net {topic} 2026`\n   - `{conference_name} 2026 accepted papers {topic}`\n\n4. **arXiv 近 3 个月密集搜索**：对精确相关的关键词，搜索过去 3 个月的 arXiv 论文\n   这是发现 concurrent work 最有效的窗口\n\n如果你发现了 Generator 遗漏的重要相关工作，必须在 issues 中列出论文标题和链接，\n并在 feedback 中说明这些工作如何影响 idea 的 novelty。\n\n## Review checklist\n1. **SOTA freshness**: Are the models/baselines cited actually current SOTA?\n   If outdated, specify what the current SOTA is and cite your source.\n2. **Reference verification**: Do the cited papers actually exist? (WebSearch to check)\n3. **Gap validity**: Does the claimed research gap still exist, or has recent work addressed it?\n4. **Venue validity**: Are target_venues' submission deadlines after 2026-05-11?\n5. **Feasibility**: Is the resource estimate realistic? Are there hidden dependencies?\n6. **Novelty**: Is this sufficiently different from existing work?\n   When scoring novelty < 4:\n   - You MUST identify the closest existing work(s) via WebSearch\n   - In your feedback, write: \"This idea is too similar to [Paper Title (Venue Year)]. Specifically, [what overlaps]. To differentiate, the generator should [suggestion].\"\n   - This gives the generator targeted guidance to boost novelty, not just \"be more novel\".\n7. **Cost realism across modes**: Are the three mode estimates (manual/human-in-loop/auto) internally consistent?\n   - Auto Research uses more GPU hours (2-5x manual) but GPU idle rate should be near zero\n   - Auto Research timeline should reflect resource availability as bottleneck — days with sufficient GPUs, not weeks\n   - Human-in-Loop should fall between manual and auto on most dimensions\n   - Manual and HIL must NOT include salary/wages — only GPU and API costs\n   - Auto Research must NOT include agent operational overhead\n   - If any mode estimate is clearly unrealistic, flag it\n\n## Idea under review (round 3/10)\n{\n  \"title\": \"Zero-Cost Credit Assignment via Environment-Native Potential Functions for Agentic RL\",\n  \"core_problem\": \"How to provide dense, step-level credit signals for agentic RL that are simultaneously (1) zero-cost (no extra rollouts, no learned models, no LLM judges), (2) environment-grounded (derived from actual task state), and (3) formally safe (provably preserving optimal policy ranking via PBRS)? A secondary question: does formal PBRS structure yield practical advantages (lower variance, better worst-case performance) over informal temporal shaping or naive additive shaping in LLM agent training — or is the guarantee merely theoretical?\",\n  \"opportunity\": \"The agentic RL credit assignment landscape has exploded with methods extracting dense step-level signals, but every approach either (a) adds compute cost via learned models or LLM critics, or (b) uses environment signals without formal policy-invariance guarantees. BEACON (arXiv:2605.06078, May 2026) achieves SOTA results (94.5% ALFWorld, 79.7% WebShop at 7B) using environment-native milestone signals with temporal decay shaping and dual-scale advantage estimation — but its non-potential-based formulation lacks policy-invariance guarantees. Self-Guide (arXiv:2604.03098) explicitly acknowledges the non-PBRS bias problem, citing Ng et al. (1999), and mitigates it with a hand-tuned annealing schedule — validating that the community recognizes this gap but has not solved it principally. Meanwhile, environment observations in text-based agent tasks already encode explicit progress signals (ALFWorld PDDL predicates, WebShop attribute-match scores) that map naturally to potential functions within PBRS (Ng et al., 1999), yet no method formalizes them as such. The specific gap: between BEACON's effective but theoretically ungrounded temporal shaping, Self-Guide's annealing-based bias mitigation, and TIPS's gold-answer-dependent PBRS formulation, there exists room for a simpler, zero-cost method with formal guarantees — one that uses the same environmental ingredients as BEACON but applies them through PBRS's mathematically clean framework.\",\n  \"landscape\": \"Step-level credit assignment for agentic RL is a rapidly growing area with 47+ cataloged methods (Xu et al., 2026). Key approaches: (1) **Learned credit methods**: iStar (ICLR 2026) learns implicit PRMs via multi-turn DPO, adding PRM training overhead. HCAPO (2026) uses the LLM as hindsight critic for step-level Q-values. SPA-RL decomposes final rewards via a progress evaluator. SWE-TRACE trains rubric-based PRMs with LLM judges. (2) **Structure-exploiting methods**: GiGPO (NeurIPS 2025) groups actions from identical anchor states for micro-advantage estimation — 90.8% on ALFWorld at 7B but requires repeated states across trajectories. SALT constructs trajectory graphs. RewardFlow (arXiv:2603.18859) propagates terminal rewards through state graphs via BFS/PageRank, achieving 89.8% on ALFWorld at 7B. (3) **Milestone-based methods**: BEACON (arXiv:2605.06078) partitions trajectories at environment-provided milestone boundaries, applies temporal decay shaping within segments, and uses dual-scale advantage estimation — achieving 94.5% on ALFWorld and 79.7% on WebShop at 7B, the current SOTA. ADMIRE (arXiv:2602.11524) similarly uses milestone-based asymmetric credit for GUI agents. Critically, neither BEACON nor ADMIRE frames its shaping as potential-based, foregoing policy-invariance guarantees. (4) **Naive environment reward methods**: Agent-RLVR, RLEF (ICML 2025), Planner-R1, and Corecraft use environment signals additively without formal shaping guarantees. (5) **Methods acknowledging the non-PBRS bias problem**: Self-Guide (arXiv:2604.03098) explicitly identifies that non-potential-based shaping biases converged policies away from the true objective and uses a trapezoid annealing schedule to withdraw internal rewards before convergence — an effective but heuristic mitigation requiring schedule tuning. (6) **Formal PBRS for LLMs**: TIPS (ICLR 2026) applies formal PBRS using teacher-model log-likelihood over gold answers — inapplicable to interactive environments without gold trajectories. The gap: no method combines environment-native, pre-defined potential functions with formal PBRS for zero-cost, theoretically grounded credit assignment — and BEACON's success demonstrates the power of environment signals while leaving the formal-vs-informal question unanswered empirically.\",\n  \"approach\": \"Define environment-native potential functions Φ(s) that extract scalar progress signals directly from task states with zero learning: (1) For ALFWorld, Φ(s) = fraction of PDDL goal predicates currently satisfied (e.g., isHot(egg), isIn(egg, plate)), directly queryable from the TextWorld engine's state tracker. (2) For WebShop, Φ(s) = attribute-match score of the product currently being viewed (computed by calling the environment's scoring function on the current product page state; 0 on search/results pages). This design choice — scoring the currently-viewed product rather than a terminal-only buy action — is justified because PBRS uses the difference F(s,s') = γΦ(s') − Φ(s), so temporary viewing of a high-match product that the agent navigates away from produces a positive shaping signal upon arrival and a symmetric negative signal upon departure, with the PBRS guarantee ensuring this bidirectional signal cannot alter optimal policy ranking regardless of viewing-vs-buying semantics. Apply formal PBRS via F(s,s') = γΦ(s') − Φ(s) atop sparse outcome rewards during GRPO training of Qwen2.5-7B-Instruct, inheriting policy invariance without any teacher model, learned PRM, or extra rollouts. Build on the verl-agent codebase (github.com/langfengQ/verl-agent), which natively supports ALFWorld, WebShop, and GRPO/GiGPO, adding only a lightweight PBRS reward wrapper.\\n\\n**Experimental design (3 conditions, 2 environments, 2 seeds = 12 runs):** (a) sparse-reward GRPO baseline, (b) EN-PBRS (our method), (c) naive additive shaping (r + αΦ(s'), violating PBRS form). Compare against published BEACON 7B results (94.5%/79.7% from their paper on same codebase/model) and GiGPO 7B results (~90.8%/~70% from their paper). Cite iStar/HCAPO numbers from their papers.\\n\\n**Robust contribution framing (mitigating fragile hypothesis):** We anticipate three possible outcome scenarios and design analyses for each: (Scenario A) EN-PBRS > naive shaping on aggregate — directly validates PBRS formalism's practical importance. (Scenario B) EN-PBRS ≈ naive on aggregate but differs on specific task types — we conduct per-task-type analysis across ALFWorld's 6 task categories (Pick, Clean, Heat, Cool, Examine, Pick2), hypothesizing that multi-step tasks (Pick2, Heat+Place) where naive shaping can create misleading intermediate rewards will show the largest PBRS advantage. (Scenario C) EN-PBRS ≈ naive across all metrics — we contribute: (i) EN-PBRS as a zero-cost alternative to learned methods (iStar, HCAPO, SPA-RL) achieving competitive performance with no training overhead, (ii) formal guarantees as future-proofing for harder environments where naive shaping will diverge, (iii) training stability analysis showing PBRS produces lower return variance across seeds. In all scenarios, the comparison against BEACON is valuable: EN-PBRS uses the SAME type of environmental signals as BEACON but with a dramatically simpler mathematical framework (one formula vs. temporal decay + dual-scale advantage + segment partitioning), providing evidence that formal PBRS achieves competitive performance with less engineering complexity.\\n\\n**Key analyses:** (i) Aggregate success rate vs. all baselines, (ii) per-task-type breakdown on ALFWorld's 6 categories, (iii) training variance across seeds (PBRS should produce lower variance by eliminating shaping-induced bias), (iv) convergence speed comparison, (v) qualitative failure analysis identifying cases where naive/temporal shaping creates perverse incentives but EN-PBRS does not.\\n\\n**Generalizability discussion (dedicated section):** We explicitly address EN-PBRS's scope limitation — it requires environments with queryable progress metrics. We discuss extensions along a spectrum of decreasing structure: (a) ScienceWorld provides explicit subgoal signals directly consumable as potentials (immediate extension, not implemented here due to compute constraints). (b) WebArena: DOM state features (form fields filled, navigation depth, URL similarity to target) could define approximate Φ. (c) SWE-bench: intermediate test pass rate as approximate Φ. (d) General case: LLM-based progress estimators could serve as approximate potential functions, with the PBRS framework providing principled guidance for their use — specifically, Self-Guide's annealing approach is unnecessary if the estimator is formulated as a proper potential function. This discussion frames EN-PBRS as the gold standard for structured environments and PBRS as a general design principle for reward shaping in agentic RL.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180-200h H100\",\n      \"gpu_utilization\": \"40-55%\",\n      \"timeline\": \"12-14 days\",\n      \"team\": \"1 researcher\",\n      \"estimated_gpu_cost\": \"$720-800 (at ~$4/hr spot H100)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~180-200h H100\",\n      \"gpu_utilization\": \"60-75% — agent queues sequential training runs; human designs potential functions, validates PBRS correctness, and crafts per-task-type analysis\",\n      \"timeline\": \"10-12 days\",\n      \"team\": \"1 researcher, ~30min/day check-in\",\n      \"claude_api_cost\": \"$100-200\",\n      \"estimated_gpu_cost\": \"$720-800\",\n      \"risk_note\": \"Primary risk: naive shaping may not observably degrade aggregate performance. Mitigated by pre-planned per-task-type analysis, variance analysis, and reframed contribution as zero-cost alternative to learned methods\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~250-350h H100 (extended sweeps over α, potential function variants)\",\n      \"gpu_utilization\": \"85-95%\",\n      \"timeline\": \"7-10 days with ≥4 H100s\",\n      \"team\": \"0 (initial setup only)\",\n      \"claude_api_cost\": \"$200-400\",\n      \"estimated_gpu_cost\": \"$1,000-1,400\",\n      \"speed_bottleneck\": \"ALFWorld environment CPU bottleneck during rollout collection; WebShop HTTP-based environment adds latency\",\n      \"risk_note\": \"Agent may not craft the key per-task-type analysis showing where PBRS matters most without human intuition about which task structures are vulnerable to naive shaping bias\"\n    },\n    \"compute_breakdown\": \"12 runs (3 conditions × 2 environments × 2 seeds) × ~16h/run (150 iterations × 362s/iteration for 7B GRPO) = ~192h H100. BEACON and GiGPO baselines cited from published results on identical model/environment configurations. γ sensitivity discussed theoretically rather than swept (saves ~4 additional runs). Budget includes ~8h buffer for debugging and reruns.\"\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR deadline May 25, 2026)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping (Ng et al., ICML 1999)\",\n    \"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs (ICLR 2026)\",\n    \"Group-in-Group Policy Optimization for LLM Agent Training [GiGPO] (NeurIPS 2025)\",\n    \"Agentic Reinforcement Learning with Implicit Step Rewards [iStar] (ICLR 2026)\",\n    \"BEACON: Milestone-Guided Policy Learning for Long-Horizon Language Agents (arXiv:2605.06078, May 2026)\",\n    \"Self-Guide: Co-Evolution of Policy and Internal Reward for Language Agents (arXiv:2604.03098, April 2026)\",\n    \"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL (arXiv:2603.18859, March 2026)\",\n    \"Adaptive Milestone Reward for GUI Agents [ADMIRE] (arXiv:2602.11524, February 2026)\",\n    \"Hindsight Credit Assignment for Long-Horizon LLM Agents [HCAPO] (arXiv 2026)\",\n    \"SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph (Findings of EACL 2026)\",\n    \"SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution (arXiv 2025)\",\n    \"Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards (arXiv 2025)\",\n    \"RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning (ICML 2025)\",\n    \"Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs (arXiv 2025)\",\n    \"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for LLMs (arXiv 2026)\",\n    \"SWE-TRACE: Optimizing Long-Horizon SWE Agents through Rubric Process Reward Models (arXiv 2026)\"\n  ],\n  \"description\": \"We propose Environment-Native PBRS (EN-PBRS), a method that derives dense, step-level credit signals for agentic RL directly from pre-defined environment potential functions — PDDL goal-predicate satisfaction in ALFWorld, attribute-match scores in WebShop — without learning any reward model, training any critic, or running any additional rollouts. EN-PBRS uses the same type of environment progress signals as BEACON (the current SOTA on these benchmarks) but applies them through a dramatically simpler mathematical framework: a single PBRS formula F(s,s') = γΦ(s') − Φ(s) versus BEACON's temporal decay, segment partitioning, and dual-scale advantage estimation. Unlike BEACON's informal milestone shaping and Self-Guide's annealing-based bias mitigation, EN-PBRS inherits the formal PBRS guarantee (Ng et al., 1999) that optimal policy ranking is preserved — requiring no schedule tuning and no risk of shaping-induced bias at convergence. Our contribution is designed to be robust across empirical outcomes: if EN-PBRS outperforms naive shaping, this directly validates PBRS formalism in LLM agent training; if performance is comparable on aggregate, we contribute (a) per-task-type analysis revealing where PBRS provides stability advantages, (b) training variance analysis showing PBRS's lower variance guarantees, and (c) EN-PBRS as a zero-cost, formally grounded alternative to learned credit methods (iStar, HCAPO, SPA-RL). Building on verl-agent with Qwen2.5-7B-Instruct and GRPO, we compare against sparse GRPO, naive additive shaping, and published BEACON/GiGPO results on ALFWorld and WebShop, with per-task-type and stability analyses. A dedicated generalizability section discusses how PBRS extends beyond structured environments via approximate potential functions (DOM features for WebArena, test pass rates for SWE-bench, LLM-based progress estimators), positioning EN-PBRS as the principled framework for environment-informed reward shaping in agentic RL.\",\n  \"project_name\": \"env_native_pbrs\",\n  \"source\": \"web_research\"\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL: Venue mismatch — user requires EMNLP 2026 (ARR deadline May 25, 2026) but idea targets ICLR 2027 and AAAI 2027, completely ignoring the user's specified target venue and deadline.\", \"CRITICAL: Compute budget violation — user hard constraint is ≤200 H100-hours total; idea estimates 1,000–1,500h A100 in manual mode alone (≈700–1,050 H100-equivalent hours), 5x+ over budget.\", \"CRITICAL: Timeline violation — user hard constraint is ≤16 days; idea estimates 3–5 months, an order of magnitude over budget.\", \"MAJOR: Missing critical competing work — Agent-RLVR (Scale AI, 2025) already uses environment execution rewards for SWE-bench RL training without PBRS formalization and achieves strong results. RLEF (ICML 2025) does the same for code generation. SWE-TRACE uses rubric-based environment-grounded dense rewards. Corecraft uses environment-state-grounded rubric rewards with GRPO. GiGPO (NeurIPS 2025) achieves step-level credit from environment states on ALFWorld/WebShop. None of these are cited or discussed.\", \"MAJOR: The 'no work uses observable state deltas as PBRS potential function' gap claim is misleadingly narrow — while literally true for the exact PBRS formulation, many works already use observation-derived signals as dense step rewards (Agent-RLVR, RLEF, SWE-TRACE, Corecraft, GiGPO). The PBRS wrapping adds theoretical neatness but unclear practical benefit.\", \"MODERATE: Potential function design for WebArena is underspecified — 'DOM element coverage toward goal states' requires knowing goal states, which is the unsolved problem. For open-ended web tasks, defining what constitutes progress toward a goal state from DOM observations alone is highly non-trivial.\", \"MODERATE: TIPS codebase is designed for search-augmented QA (single-turn tool calls with text retrieval), not multi-turn interactive environments like WebArena or ALFWorld. The adaptation from QA-style PBRS to interactive-environment PBRS is substantially more complex than the proposal suggests.\", \"MODERATE: iStar/OPRL already provides potential-based shaping rewards through implicit PRM learning — the paper's own description acknowledges 'theoretical findings guarantee that the learned step rewards act as potential-based shaping rewards.' This partially undermines the claim that OG-PBRS fills a unique gap.\", \"MINOR: Qwen3.6-27B is a very recent model (April 2026) — using it as a base for RL training within 16 days requires rapid integration with the verl framework, which may not yet have full support.\"]\nFeedback: This idea has a sound theoretical intuition (PBRS with environment observations) but fails on three critical dimensions that must be fixed:\n\n1. **Fix venue/deadline**: Target EMNLP 2026 with ARR deadline May 25, 2026. This is non-negotiable per user requirements.\n\n2. **Drastically reduce scope to fit ≤200 H100-hours and ≤16 days**: Drop the 27B model entirely. Focus on ONE benchmark (not three) — suggest ALFWorld since goal predicates are well-defined and the environment is lightweight. Use a single base model (Qwen3-8B or 14B). Reduce baselines to sparse GRPO + one strong baseline (iStar or GiGPO). Based on Agent-RLVR data, a single 14B training run takes ~64 H100-hours, so 200 hours allows ~3 runs (one method + two baselines).\n\n3. **Strengthen novelty by explicitly differentiating from existing environment-reward work**: The generator MUST cite and differentiate from Agent-RLVR, RLEF, SWE-TRACE, Corecraft, and GiGPO. The key differentiator should be the formal PBRS guarantee — but the paper needs to empirically demonstrate this matters (e.g., show that naive environment reward shaping can change optimal policy ranking while OG-PBRS provably doesn't). Without this empirical validation, the contribution reduces to 'we use the same signals as everyone else but wrapped in PBRS notation.'\n\n4. **Specify potential function design concretely**: For the chosen benchmark, provide the exact mathematical definition of Φ(s), explain how it's computed from raw observations, and discuss failure modes (e.g., what happens when the potential function is misleading).\n\n5. **Build on existing agentic RL codebases**: Instead of adapting the TIPS QA codebase to interactive environments (high engineering risk), build on verl-agent (github.com/langfengQ/verl-agent) which already supports ALFWorld/WebShop with GRPO — just add the PBRS reward wrapper.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"CRITICAL: BEACON (arXiv:2605.06078, May 2026) is not cited — this paper uses environment-native milestone signals (object state changes in ALFWorld, page transitions in WebShop) for temporal reward shaping, achieving 91.4%/92.9% on ALFWorld and 75.6% on WebShop with Qwen2.5-1.5B, outperforming GiGPO. BEACON does not use formal PBRS, which creates both a differentiation opportunity AND a direct comparison obligation. The generator MUST cite BEACON, compare against it, and show why formal PBRS is superior to BEACON's informal milestone-based shaping.\", \"MAJOR: The entire empirical contribution rests on a fragile hypothesis — that naive additive shaping causes observable policy degradation vs. PBRS in ALFWorld/WebShop. In well-structured environments with clear goal states (like ALFWorld), naive and potential-based shaping may converge to the same policy in practice, as shown in classical RL literature where PBRS advantages are most pronounced in environments with misleading reward signals. The generator needs a concrete backup plan: if naive ≈ PBRS in performance, what is the paper's contribution?\", \"MAJOR: Limited generalizability undermines impact — EN-PBRS requires environments with pre-defined, queryable progress metrics. This covers ALFWorld (PDDL predicates) and WebShop (attribute scores) but NOT the most impactful agent benchmarks: SWE-bench (no PDDL state), WebArena (no built-in progress metric), GAIA (open-ended), Mind2Web (no progress API). The paper should explicitly discuss this limitation and ideally propose how potential functions could be approximated in less structured environments.\", \"MODERATE: WebShop's reward API is terminal-only — the attribute-match score is computed only when the agent clicks 'buy'. Implementing step-level potential computation requires calling the scoring function on the currently-viewed product at each step, which is engineering-feasible but introduces artifacts (e.g., the agent hasn't committed to buying, so the 'potential' of viewing a product differs from the potential of selecting it). This design choice needs justification.\", \"MODERATE: Self-Guide (arXiv:2604.03098) should be cited as both motivation and partial competitor — it explicitly identifies the non-PBRS bias problem and uses annealing as a mitigation. The generator should explain why formal PBRS is preferable to Self-Guide's annealing approach (stronger theoretical guarantees, no schedule tuning needed).\", \"MINOR: The 150-200 H100-hour estimate for training + 3 baselines + ablations over 3 seeds is tight. With ~362s/iteration for 7B GRPO (from GiGPO paper), running ~200 iterations × 3 seeds × 4 conditions (sparse, EN-PBRS, naive, GiGPO) = ~12 runs, each ~20h = ~240h. This exceeds the 200h hard constraint. The generator should either reduce seeds from 3 to 2, or reduce the number of conditions.\"]\nFeedback: The revision successfully fixed the three critical issues from Round 1 (venue, compute, timeline), and the idea is now properly scoped. But three new issues need addressing:\n\n1. **Cite and compare against BEACON (arXiv:2605.06078)**: This is your most direct competitor — it uses the same type of environment-native signals in the same environments. Your key differentiation is formal PBRS guarantees vs. BEACON's informal temporal shaping. Add BEACON as a baseline and empirically demonstrate where BEACON's non-potential-based shaping fails but EN-PBRS succeeds. This would actually STRENGTHEN your paper by providing a concrete example of why PBRS formalism matters.\n\n2. **Mitigate the fragile empirical hypothesis**: Your paper's impact hinges on showing naive shaping ≠ PBRS in practice. Prepare for the scenario where they perform similarly on average: (a) analyze per-task-type performance — naive shaping may fail on specific task categories even if aggregate performance is similar, (b) analyze training stability/variance — PBRS may produce lower variance even if means are comparable, (c) frame the contribution partially as 'zero-cost alternative to learned methods (iStar, HCAPO)' rather than purely 'PBRS > naive.'\n\n3. **Address generalizability honestly**: Add a discussion section about how potential functions could be defined for less structured environments — e.g., using LLM-based progress estimators as approximate potentials, or extracting structured state from HTML in WebArena. This shows the framework extends beyond ALFWorld/WebShop even if this paper doesn't implement it.\n\n4. **Cite Self-Guide (arXiv:2604.03098)**: It explicitly validates your theoretical motivation by acknowledging the non-PBRS bias problem. Use it as evidence that the community recognizes this gap but hasn't solved it properly.\n\n5. **Tighten compute budget**: Your current plan likely exceeds 200 H100-hours. Either reduce to 2 seeds, or drop one ablation (e.g., γ sensitivity can be discussed theoretically rather than swept).\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"}\n  },\n  \"issues\": [\"specific issue 1\", \"specific issue 2\", ...],\n  \"feedback\": \"Actionable feedback for the generator (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": idea is sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold — provide specific feedback\n- \"fail\": fundamental flaw (e.g., gap doesn't exist, approach provably wrong, or scores remain low after multiple revisions)\n- Threshold is HIGH (4.0/5.0): agent scores tend to be inflated, so only truly outstanding ideas should pass. An avg of 3.5 is NOT enough.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-11T23:53:51.256Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-11T23:53:51.256Z",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-11T23:53:51.283Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-11 (UTC).**

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

## Idea under review (round 3/10)
{
  "title": "Zero-Cost Credit Assignment via Environment-Native Potential Functions for Agentic RL",
  "core_problem": "How to provide dense, step-level credit signals for agentic RL that are simultaneously (1) zero-cost (no extra rollouts, no learned models, no LLM judges), (2) environment-grounded (derived from actual task state), and (3) formally safe (provably preserving optimal policy ranking via PBRS)? A secondary question: does formal PBRS structure yield practical advantages (lower variance, better worst-case performance) over informal temporal shaping or naive additive shaping in LLM agent training — or is the guarantee merely theoretical?",
  "opportunity": "The agentic RL credit assignment landscape has exploded with methods extracting dense step-level signals, but every approach either (a) adds compute cost via learned models or LLM critics, or (b) uses environment signals without formal policy-invariance guarantees. BEACON (arXiv:2605.06078, May 2026) achieves SOTA results (94.5% ALFWorld, 79.7% WebShop at 7B) using environment-native milestone signals with temporal decay shaping and dual-scale advantage estimation — but its non-potential-based formulation lacks policy-invariance guarantees. Self-Guide (arXiv:2604.03098) explicitly acknowledges the non-PBRS bias problem, citing Ng et al. (1999), and mitigates it with a hand-tuned annealing schedule — validating that the community recognizes this gap but has not solved it principally. Meanwhile, environment observations in text-based agent tasks already encode explicit progress signals (ALFWorld PDDL predicates, WebShop attribute-match scores) that map naturally to potential functions within PBRS (Ng et al., 1999), yet no method formalizes them as such. The specific gap: between BEACON's effective but theoretically ungrounded temporal shaping, Self-Guide's annealing-based bias mitigation, and TIPS's gold-answer-dependent PBRS formulation, there exists room for a simpler, zero-cost method with formal guarantees — one that uses the same environmental ingredients as BEACON but applies them through PBRS's mathematically clean framework.",
  "landscape": "Step-level credit assignment for agentic RL is a rapidly growing area with 47+ cataloged methods (Xu et al., 2026). Key approaches: (1) **Learned credit methods**: iStar (ICLR 2026) learns implicit PRMs via multi-turn DPO, adding PRM training overhead. HCAPO (2026) uses the LLM as hindsight critic for step-level Q-values. SPA-RL decomposes final rewards via a progress evaluator. SWE-TRACE trains rubric-based PRMs with LLM judges. (2) **Structure-exploiting methods**: GiGPO (NeurIPS 2025) groups actions from identical anchor states for micro-advantage estimation — 90.8% on ALFWorld at 7B but requires repeated states across trajectories. SALT constructs trajectory graphs. RewardFlow (arXiv:2603.18859) propagates terminal rewards through state graphs via BFS/PageRank, achieving 89.8% on ALFWorld at 7B. (3) **Milestone-based methods**: BEACON (arXiv:2605.06078) partitions trajectories at environment-provided milestone boundaries, applies temporal decay shaping within segments, and uses dual-scale advantage estimation — achieving 94.5% on ALFWorld and 79.7% on WebShop at 7B, the current SOTA. ADMIRE (arXiv:2602.11524) similarly uses milestone-based asymmetric credit for GUI agents. Critically, neither BEACON nor ADMIRE frames its shaping as potential-based, foregoing policy-invariance guarantees. (4) **Naive environment reward methods**: Agent-RLVR, RLEF (ICML 2025), Planner-R1, and Corecraft use environment signals additively without formal shaping guarantees. (5) **Methods acknowledging the non-PBRS bias problem**: Self-Guide (arXiv:2604.03098) explicitly identifies that non-potential-based shaping biases converged policies away from the true objective and uses a trapezoid annealing schedule to withdraw internal rewards before convergence — an effective but heuristic mitigation requiring schedule tuning. (6) **Formal PBRS for LLMs**: TIPS (ICLR 2026) applies formal PBRS using teacher-model log-likelihood over gold answers — inapplicable to interactive environments without gold trajectories. The gap: no method combines environment-native, pre-defined potential functions with formal PBRS for zero-cost, theoretically grounded credit assignment — and BEACON's success demonstrates the power of environment signals while leaving the formal-vs-informal question unanswered empirically.",
  "approach": "Define environment-native potential functions Φ(s) that extract scalar progress signals directly from task states with zero learning: (1) For ALFWorld, Φ(s) = fraction of PDDL goal predicates currently satisfied (e.g., isHot(egg), isIn(egg, plate)), directly queryable from the TextWorld engine's state tracker. (2) For WebShop, Φ(s) = attribute-match score of the product currently being viewed (computed by calling the environment's scoring function on the current product page state; 0 on search/results pages). This design choice — scoring the currently-viewed product rather than a terminal-only buy action — is justified because PBRS uses the difference F(s,s') = γΦ(s') − Φ(s), so temporary viewing of a high-match product that the agent navigates away from produces a positive shaping signal upon arrival and a symmetric negative signal upon departure, with the PBRS guarantee ensuring this bidirectional signal cannot alter optimal policy ranking regardless of viewing-vs-buying semantics. Apply formal PBRS via F(s,s') = γΦ(s') − Φ(s) atop sparse outcome rewards during GRPO training of Qwen2.5-7B-Instruct, inheriting policy invariance without any teacher model, learned PRM, or extra rollouts. Build on the verl-agent codebase (github.com/langfengQ/verl-agent), which natively supports ALFWorld, WebShop, and GRPO/GiGPO, adding only a lightweight PBRS reward wrapper.\n\n**Experimental design (3 conditions, 2 environments, 2 seeds = 12 runs):** (a) sparse-reward GRPO baseline, (b) EN-PBRS (our method), (c) naive additive shaping (r + αΦ(s'), violating PBRS form). Compare against published BEACON 7B results (94.5%/79.7% from their paper on same codebase/model) and GiGPO 7B results (~90.8%/~70% from their paper). Cite iStar/HCAPO numbers from their papers.\n\n**Robust contribution framing (mitigating fragile hypothesis):** We anticipate three possible outcome scenarios and design analyses for each: (Scenario A) EN-PBRS > naive shaping on aggregate — directly validates PBRS formalism's practical importance. (Scenario B) EN-PBRS ≈ naive on aggregate but differs on specific task types — we conduct per-task-type analysis across ALFWorld's 6 task categories (Pick, Clean, Heat, Cool, Examine, Pick2), hypothesizing that multi-step tasks (Pick2, Heat+Place) where naive shaping can create misleading intermediate rewards will show the largest PBRS advantage. (Scenario C) EN-PBRS ≈ naive across all metrics — we contribute: (i) EN-PBRS as a zero-cost alternative to learned methods (iStar, HCAPO, SPA-RL) achieving competitive performance with no training overhead, (ii) formal guarantees as future-proofing for harder environments where naive shaping will diverge, (iii) training stability analysis showing PBRS produces lower return variance across seeds. In all scenarios, the comparison against BEACON is valuable: EN-PBRS uses the SAME type of environmental signals as BEACON but with a dramatically simpler mathematical framework (one formula vs. temporal decay + dual-scale advantage + segment partitioning), providing evidence that formal PBRS achieves competitive performance with less engineering complexity.\n\n**Key analyses:** (i) Aggregate success rate vs. all baselines, (ii) per-task-type breakdown on ALFWorld's 6 categories, (iii) training variance across seeds (PBRS should produce lower variance by eliminating shaping-induced bias), (iv) convergence speed comparison, (v) qualitative failure analysis identifying cases where naive/temporal shaping creates perverse incentives but EN-PBRS does not.\n\n**Generalizability discussion (dedicated section):** We explicitly address EN-PBRS's scope limitation — it requires environments with queryable progress metrics. We discuss extensions along a spectrum of decreasing structure: (a) ScienceWorld provides explicit subgoal signals directly consumable as potentials (immediate extension, not implemented here due to compute constraints). (b) WebArena: DOM state features (form fields filled, navigation depth, URL similarity to target) could define approximate Φ. (c) SWE-bench: intermediate test pass rate as approximate Φ. (d) General case: LLM-based progress estimators could serve as approximate potential functions, with the PBRS framework providing principled guidance for their use — specifically, Self-Guide's annealing approach is unnecessary if the estimator is formulated as a proper potential function. This discussion frames EN-PBRS as the gold standard for structured environments and PBRS as a general design principle for reward shaping in agentic RL.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180-200h H100",
      "gpu_utilization": "40-55%",
      "timeline": "12-14 days",
      "team": "1 researcher",
      "estimated_gpu_cost": "$720-800 (at ~$4/hr spot H100)"
    },
    "human_in_loop": {
      "gpu_hours": "~180-200h H100",
      "gpu_utilization": "60-75% — agent queues sequential training runs; human designs potential functions, validates PBRS correctness, and crafts per-task-type analysis",
      "timeline": "10-12 days",
      "team": "1 researcher, ~30min/day check-in",
      "claude_api_cost": "$100-200",
      "estimated_gpu_cost": "$720-800",
      "risk_note": "Primary risk: naive shaping may not observably degrade aggregate performance. Mitigated by pre-planned per-task-type analysis, variance analysis, and reframed contribution as zero-cost alternative to learned methods"
    },
    "auto_research": {
      "gpu_hours": "~250-350h H100 (extended sweeps over α, potential function variants)",
      "gpu_utilization": "85-95%",
      "timeline": "7-10 days with ≥4 H100s",
      "team": "0 (initial setup only)",
      "claude_api_cost": "$200-400",
      "estimated_gpu_cost": "$1,000-1,400",
      "speed_bottleneck": "ALFWorld environment CPU bottleneck during rollout collection; WebShop HTTP-based environment adds latency",
      "risk_note": "Agent may not craft the key per-task-type analysis showing where PBRS matters most without human intuition about which task structures are vulnerable to naive shaping bias"
    },
    "compute_breakdown": "12 runs (3 conditions × 2 environments × 2 seeds) × ~16h/run (150 iterations × 362s/iteration for 7B GRPO) = ~192h H100. BEACON and GiGPO baselines cited from published results on identical model/environment configurations. γ sensitivity discussed theoretically rather than swept (saves ~4 additional runs). Budget includes ~8h buffer for debugging and reruns."
  },
  "target_venues": [
    "EMNLP 2026 (ARR deadline May 25, 2026)"
  ],
  "level": "top-tier",
  "key_references": [
    "Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping (Ng et al., ICML 1999)",
    "TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs (ICLR 2026)",
    "Group-in-Group Policy Optimization for LLM Agent Training [GiGPO] (NeurIPS 2025)",
    "Agentic Reinforcement Learning with Implicit Step Rewards [iStar] (ICLR 2026)",
    "BEACON: Milestone-Guided Policy Learning for Long-Horizon Language Agents (arXiv:2605.06078, May 2026)",
    "Self-Guide: Co-Evolution of Policy and Internal Reward for Language Agents (arXiv:2604.03098, April 2026)",
    "RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL (arXiv:2603.18859, March 2026)",
    "Adaptive Milestone Reward for GUI Agents [ADMIRE] (arXiv:2602.11524, February 2026)",
    "Hindsight Credit Assignment for Long-Horizon LLM Agents [HCAPO] (arXiv 2026)",
    "SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph (Findings of EACL 2026)",
    "SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution (arXiv 2025)",
    "Agent-RLVR: Training Software Engineering Agents via Guidance and Environment Rewards (arXiv 2025)",
    "RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning (ICML 2025)",
    "Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs (arXiv 2025)",
    "From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for LLMs (arXiv 2026)",
    "SWE-TRACE: Optimizing Long-Horizon SWE Agents through Rubric Process Reward Models (arXiv 2026)"
  ],
  "description": "We propose Environment-Native PBRS (EN-PBRS), a method that derives dense, step-level credit signals for agentic RL directly from pre-defined environment potential functions — PDDL goal-predicate satisfaction in ALFWorld, attribute-match scores in WebShop — without learning any reward model, training any critic, or running any additional rollouts. EN-PBRS uses the same type of environment progress signals as BEACON (the current SOTA on these benchmarks) but applies them through a dramatically simpler mathematical framework: a single PBRS formula F(s,s') = γΦ(s') − Φ(s) versus BEACON's temporal decay, segment partitioning, and dual-scale advantage estimation. Unlike BEACON's informal milestone shaping and Self-Guide's annealing-based bias mitigation, EN-PBRS inherits the formal PBRS guarantee (Ng et al., 1999) that optimal policy ranking is preserved — requiring no schedule tuning and no risk of shaping-induced bias at convergence. Our contribution is designed to be robust across empirical outcomes: if EN-PBRS outperforms naive shaping, this directly validates PBRS formalism in LLM agent training; if performance is comparable on aggregate, we contribute (a) per-task-type analysis revealing where PBRS provides stability advantages, (b) training variance analysis showing PBRS's lower variance guarantees, and (c) EN-PBRS as a zero-cost, formally grounded alternative to learned credit methods (iStar, HCAPO, SPA-RL). Building on verl-agent with Qwen2.5-7B-Instruct and GRPO, we compare against sparse GRPO, naive additive shaping, and published BEACON/GiGPO results on ALFWorld and WebShop, with per-task-type and stability analyses. A dedicated generalizability section discusses how PBRS extends beyond structured environments via approximate potential functions (DOM features for WebArena, test pass rates for SWE-bench, LLM-based progress estimators), positioning EN-PBRS as the principled framework for environment-informed reward shaping in agentic RL.",
  "project_name": "env_native_pbrs",
  "source": "web_research"
}


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL: Venue mismatch — user requires EMNLP 2026 (ARR deadline May 25, 2026) but idea targets ICLR 2027 and AAAI 2027, completely ignoring the user's specified target venue and deadline.", "CRITICAL: Compute budget violation — user hard constraint is ≤200 H100-hours total; idea estimates 1,000–1,500h A100 in manual mode alone (≈700–1,050 H100-equivalent hours), 5x+ over budget.", "CRITICAL: Timeline violation — user hard constraint is ≤16 days; idea estimates 3–5 months, an order of magnitude over budget.", "MAJOR: Missing critical competing work — Agent-RLVR (Scale AI, 2025) already uses environment execution rewards for SWE-bench RL training without PBRS formalization and achieves strong results. RLEF (ICML 2025) does the same for code generation. SWE-TRACE uses rubric-based environment-grounded dense rewards. Corecraft uses environment-state-grounded rubric rewards with GRPO. GiGPO (NeurIPS 2025) achieves step-level credit from environment states on ALFWorld/WebShop. None of these are cited or discussed.", "MAJOR: The 'no work uses observable state deltas as PBRS potential function' gap claim is misleadingly narrow — while literally true for the exact PBRS formulation, many works already use observation-derived signals as dense step rewards (Agent-RLVR, RLEF, SWE-TRACE, Corecraft, GiGPO). The PBRS wrapping adds theoretical neatness but unclear practical benefit.", "MODERATE: Potential function design for WebArena is underspecified — 'DOM element coverage toward goal states' requires knowing goal states, which is the unsolved problem. For open-ended web tasks, defining what constitutes progress toward a goal state from DOM observations alone is highly non-trivial.", "MODERATE: TIPS codebase is designed for search-augmented QA (single-turn tool calls with text retrieval), not multi-turn interactive environments like WebArena or ALFWorld. The adaptation from QA-style PBRS to interactive-environment PBRS is substantially more complex than the proposal suggests.", "MODERATE: iStar/OPRL already provides potential-based shaping rewards through implicit PRM learning — the paper's own description acknowledges 'theoretical findings guarantee that the learned step rewards act as potential-based shaping rewards.' This partially undermines the claim that OG-PBRS fills a unique gap.", "MINOR: Qwen3.6-27B is a very recent model (April 2026) — using it as a base for RL training within 16 days requires rapid integration with the verl framework, which may not yet have full support."]
Feedback: This idea has a sound theoretical intuition (PBRS with environment observations) but fails on three critical dimensions that must be fixed:

1. **Fix venue/deadline**: Target EMNLP 2026 with ARR deadline May 25, 2026. This is non-negotiable per user requirements.

2. **Drastically reduce scope to fit ≤200 H100-hours and ≤16 days**: Drop the 27B model entirely. Focus on ONE benchmark (not three) — suggest ALFWorld since goal predicates are well-defined and the environment is lightweight. Use a single base model (Qwen3-8B or 14B). Reduce baselines to sparse GRPO + one strong baseline (iStar or GiGPO). Based on Agent-RLVR data, a single 14B training run takes ~64 H100-hours, so 200 hours allows ~3 runs (one method + two baselines).

3. **Strengthen novelty by explicitly differentiating from existing environment-reward work**: The generator MUST cite and differentiate from Agent-RLVR, RLEF, SWE-TRACE, Corecraft, and GiGPO. The key differentiator should be the formal PBRS guarantee — but the paper needs to empirically demonstrate this matters (e.g., show that naive environment reward shaping can change optimal policy ranking while OG-PBRS provably doesn't). Without this empirical validation, the contribution reduces to 'we use the same signals as everyone else but wrapped in PBRS notation.'

4. **Specify potential function design concretely**: For the chosen benchmark, provide the exact mathematical definition of Φ(s), explain how it's computed from raw observations, and discuss failure modes (e.g., what happens when the potential function is misleading).

5. **Build on existing agentic RL codebases**: Instead of adapting the TIPS QA codebase to interactive environments (high engineering risk), build on verl-agent (github.com/langfengQ/verl-agent) which already supports ALFWorld/WebShop with GRPO — just add the PBRS reward wrapper.

### Round 2 review
Verdict: revise
Issues: ["CRITICAL: BEACON (arXiv:2605.06078, May 2026) is not cited — this paper uses environment-native milestone signals (object state changes in ALFWorld, page transitions in WebShop) for temporal reward shaping, achieving 91.4%/92.9% on ALFWorld and 75.6% on WebShop with Qwen2.5-1.5B, outperforming GiGPO. BEACON does not use formal PBRS, which creates both a differentiation opportunity AND a direct comparison obligation. The generator MUST cite BEACON, compare against it, and show why formal PBRS is superior to BEACON's informal milestone-based shaping.", "MAJOR: The entire empirical contribution rests on a fragile hypothesis — that naive additive shaping causes observable policy degradation vs. PBRS in ALFWorld/WebShop. In well-structured environments with clear goal states (like ALFWorld), naive and potential-based shaping may converge to the same policy in practice, as shown in classical RL literature where PBRS advantages are most pronounced in environments with misleading reward signals. The generator needs a concrete backup plan: if naive ≈ PBRS in performance, what is the paper's contribution?", "MAJOR: Limited generalizability undermines impact — EN-PBRS requires environments with pre-defined, queryable progress metrics. This covers ALFWorld (PDDL predicates) and WebShop (attribute scores) but NOT the most impactful agent benchmarks: SWE-bench (no PDDL state), WebArena (no built-in progress metric), GAIA (open-ended), Mind2Web (no progress API). The paper should explicitly discuss this limitation and ideally propose how potential functions could be approximated in less structured environments.", "MODERATE: WebShop's reward API is terminal-only — the attribute-match score is computed only when the agent clicks 'buy'. Implementing step-level potential computation requires calling the scoring function on the currently-viewed product at each step, which is engineering-feasible but introduces artifacts (e.g., the agent hasn't committed to buying, so the 'potential' of viewing a product differs from the potential of selecting it). This design choice needs justification.", "MODERATE: Self-Guide (arXiv:2604.03098) should be cited as both motivation and partial competitor — it explicitly identifies the non-PBRS bias problem and uses annealing as a mitigation. The generator should explain why formal PBRS is preferable to Self-Guide's annealing approach (stronger theoretical guarantees, no schedule tuning needed).", "MINOR: The 150-200 H100-hour estimate for training + 3 baselines + ablations over 3 seeds is tight. With ~362s/iteration for 7B GRPO (from GiGPO paper), running ~200 iterations × 3 seeds × 4 conditions (sparse, EN-PBRS, naive, GiGPO) = ~12 runs, each ~20h = ~240h. This exceeds the 200h hard constraint. The generator should either reduce seeds from 3 to 2, or reduce the number of conditions."]
Feedback: The revision successfully fixed the three critical issues from Round 1 (venue, compute, timeline), and the idea is now properly scoped. But three new issues need addressing:

1. **Cite and compare against BEACON (arXiv:2605.06078)**: This is your most direct competitor — it uses the same type of environment-native signals in the same environments. Your key differentiation is formal PBRS guarantees vs. BEACON's informal temporal shaping. Add BEACON as a baseline and empirically demonstrate where BEACON's non-potential-based shaping fails but EN-PBRS succeeds. This would actually STRENGTHEN your paper by providing a concrete example of why PBRS formalism matters.

2. **Mitigate the fragile empirical hypothesis**: Your paper's impact hinges on showing naive shaping ≠ PBRS in practice. Prepare for the scenario where they perform similarly on average: (a) analyze per-task-type performance — naive shaping may fail on specific task categories even if aggregate performance is similar, (b) analyze training stability/variance — PBRS may produce lower variance even if means are comparable, (c) frame the contribution partially as 'zero-cost alternative to learned methods (iStar, HCAPO)' rather than purely 'PBRS > naive.'

3. **Address generalizability honestly**: Add a discussion section about how potential functions could be defined for less structured environments — e.g., using LLM-based progress estimators as approximate potentials, or extracting structured state from HTML in WebArena. This shows the framework extends beyond ALFWorld/WebShop even if this paper doesn't implement it.

4. **Cite Self-Guide (arXiv:2604.03098)**: It explicitly validates your theoretical motivation by acknowledging the non-PBRS bias problem. Use it as evidence that the community recognizes this gap but hasn't solved it properly.

5. **Tighten compute budget**: Your current plan likely exceeds 200 H100-hours. Either reduce to 2 seeds, or drop one ablation (e.g., γ sensitivity can be discussed theoretically rather than swept).


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
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "type": "user",
  "uuid": "3718dabd-c620-42dc-a986-d431e87e74f4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-11T23:53:51.281Z_

```json
{
  "parentUuid": "3718dabd-c620-42dc-a986-d431e87e74f4",
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
  "uuid": "9adcca6e-726d-4194-8a06-2b8936d4ee56",
  "timestamp": "2026-05-11T23:53:51.281Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-11T23:53:51.281Z_

```json
{
  "parentUuid": "9adcca6e-726d-4194-8a06-2b8936d4ee56",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "77b5d178-aa82-4910-872e-a4e95c74d20b",
  "timestamp": "2026-05-11T23:53:51.281Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
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
  "leafUuid": "77b5d178-aa82-4910-872e-a4e95c74d20b",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Environment-native PBRS for agentic RL training",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c"
}
```

---

### Assistant

_source line 8 · 2026-05-11T23:54:02.163Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully review this idea as a strict ML research reviewer. I need to independently verify the claims, check for competing work, assess feasibility, novelty, and overall quality. Let me start by searching for the key papers and claims mentioned.

Let me plan my review systematically:

1. **Verify BEACON** (arXiv:2605.06078) - the most direct competitor
2. **Verify Self-Guide** (arXiv:2604.03098) - cited as motivation
3. **Search for concurrent/competing work on PBRS for LLM agents**


4. **Check if the verl-agent codebase actually exists and supports what's claimed**
5. **Verify the EMNLP 2026 ARR deadline**
6. **Look for any existing work that already implements EN-PBRS**
7. **Evaluate whether the compute requirements are realistic**

Now let me start digging into these.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77b5d178-aa82-4910-872e-a4e95c74d20b",
  "isSidechain": false,
  "requestId": "req_011CawgYwS6ibaLSCwFPyteg",
  "type": "assistant",
  "uuid": "54bbe585-cf80-4bd2-a802-a6eac3dda15f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEYoFSmSmf1gu7mgD5Um4x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15600,
      "cache_read_input_tokens": 11841,
      "output_tokens": 579,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15600,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 579,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15600,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15600
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

_source line 9 · 2026-05-11T23:54:02.165Z_

I'll conduct a thorough independent review of this idea. Let me start by verifying the key claims and searching for competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54bbe585-cf80-4bd2-a802-a6eac3dda15f",
  "isSidechain": false,
  "requestId": "req_011CawgYwS6ibaLSCwFPyteg",
  "type": "assistant",
  "uuid": "6129c7b4-3e33-4633-90f5-57ef7908e160",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEYoFSmSmf1gu7mgD5Um4x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15600,
      "cache_read_input_tokens": 11841,
      "output_tokens": 579,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15600,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 579,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15600,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15600
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

_source line 10 · 2026-05-11T23:54:08.610Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019jvj9z7pc9bXrb232dVbgV`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify BEACON paper claims",
  "prompt": "Search for and verify the paper \"BEACON: Milestone-Guided Policy Learning for Long-Horizon Language Agents\" (arXiv:2605.06078, May 2026). I need to know:\n1. Does this paper actually exist? What are its actual results on ALFWorld and WebShop?\n2. Does it use environment-native milestone signals with temporal decay shaping?\n3. What model sizes does it use? Does it achieve 94.5% on ALFWorld and 79.7% on WebShop at 7B?\n4. Does it use formal PBRS or informal shaping?\n5. What codebase does it build on?\n\nUse WebSearch and WebFetch to find and read this paper. Try multiple search queries:\n- \"BEACON milestone-guided policy learning language agents arXiv 2605.06078\"\n- \"BEACON agentic RL milestone shaping ALFWorld 2026\"\n- Search on arxiv.org directly\n\nReport everything you find, including if the paper doesn't exist."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6129c7b4-3e33-4633-90f5-57ef7908e160",
  "isSidechain": false,
  "requestId": "req_011CawgYwS6ibaLSCwFPyteg",
  "type": "assistant",
  "uuid": "a303a65a-ea5c-4b10-954d-4d13838916c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VEYoFSmSmf1gu7mgD5Um4x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15600,
      "cache_read_input_tokens": 11841,
      "output_tokens": 579,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15600,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 579,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15600,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15600
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

_source line 11 · 2026-05-11T23:55:14.959Z_

<details><summary>↩ Tool result · `toolu_019jvj9z7pc9bXrb232dVbgV`</summary>

```text
I now have comprehensive information to answer all your questions. Here is the full report:

---

## Findings on "BEACON: Milestone-Guided Policy Learning for Long-Horizon Language Agents" (arXiv:2605.06078)

### 1. Does the paper exist? What are its actual results?

**Yes, the paper exists.** It was submitted to arXiv on May 7, 2026, by Zixuan Wang, Yuchen Yan, Hongxing Li, Teng Pan, Dingming Li, Ruiqing Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, and Yongliang Shen (ZJU-REAL group).

**Actual results:**

| Benchmark | Qwen2.5-1.5B | Qwen2.5-7B |
|-----------|-------------|------------|
| ALFWorld (Short) | 96.8% | 95.1% |
| ALFWorld (Medium) | 87.0% | 94.9% |
| ALFWorld (Long) | 92.9% | 90.0% |
| ALFWorld (Average) | 91.4% | **94.5%** |
| WebShop | 75.6% | **79.7%** |
| ScienceWorld | 45.3% | 64.3% |

The headline number often cited from the abstract (92.9%) is specifically the **long-horizon ALFWorld** result at **1.5B**, not the overall average.

### 2. Does it use environment-native milestone signals with temporal decay shaping?

**Yes to both.**

- **Environment-native milestones:** The milestone detector Phi "detects observable state changes from environment feedback" and "does not require learned models or manual annotation." In ALFWorld these are object state changes (pick-up, heating completion); in WebShop they are page transitions toward the target product; in ScienceWorld the environment provides explicit subgoal signals.
- **Temporal decay shaping:** The paper applies temporal reward shaping that "assigns higher credit to actions closer to milestone completion" with a decay factor gamma = 0.95 across all benchmarks.

### 3. Model sizes and the specific numbers 94.5% / 79.7%?

**Model sizes:** Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct.

**Yes, both numbers are confirmed at 7B:**
- **94.5% on ALFWorld** (average across short/medium/long) with Qwen2.5-7B
- **79.7% on WebShop** with Qwen2.5-7B

These are the paper's actual reported results.

### 4. Formal PBRS or informal shaping?

**Informal shaping.** The paper does NOT use formal potential-based reward shaping (PBRS). It applies an informal temporal reward decay within milestone-delimited segments. There is no mention of potential functions or the PBRS theoretical framework (Ng et al., 1999).

### 5. What codebase does it build on?

BEACON builds on **verl-agent** (https://github.com/langfengQ/verl-agent), which itself extends **veRL** (https://github.com/volcengine/verl). The technical stack includes PyTorch 2.6.0, CUDA 12.4, vLLM 0.8.5, and Flash Attention 2.7.4. BEACON's own contributions are isolated in `migpo/` (advantage and reward computation) and `agent_system/` (environment integrations), inheriting most RL training infrastructure from verl-agent.

---

Sources:
- [arXiv Abstract: 2605.06078](https://arxiv.org/abs/2605.06078)
- [Full HTML Paper: 2605.06078](https://arxiv.org/html/2605.06078)
- [GitHub: ZJU-REAL/BEACON](https://github.com/ZJU-REAL/BEACON)

agentId: aa805466eb3d6d97b (use SendMessage with to: 'aa805466eb3d6d97b' to continue this agent)
&lt;usage>total_tokens: 16424
tool_uses: 7
duration_ms: 66341&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a303a65a-ea5c-4b10-954d-4d13838916c2",
  "isSidechain": false,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "type": "user",
  "uuid": "353afd35-f9bc-4d2b-9b33-cadd6e791e56",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify the paper \"BEACON: Milestone-Guided Policy Learning for Long-Horizon Language Agents\" (arXiv:2605.06078, May 2026). I need to know:\n1. Does this paper actually exist? What are its actual results on ALFWorld and WebShop?\n2. Does it use environment-native milestone signals with temporal decay shaping?\n3. What model sizes does it use? Does it achieve 94.5% on ALFWorld and 79.7% on WebShop at 7B?\n4. Does it use formal PBRS or informal shaping?\n5. What codebase does it build on?\n\nUse WebSearch and WebFetch to find and read this paper. Try multiple search queries:\n- \"BEACON milestone-guided policy learning language agents arXiv 2605.06078\"\n- \"BEACON agentic RL milestone shaping ALFWorld 2026\"\n- Search on arxiv.org directly\n\nReport everything you find, including if the paper doesn't exist.",
    "agentId": "aa805466eb3d6d97b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information to answer all your questions. Here is the full report:\n\n---\n\n## Findings on \"BEACON: Milestone-Guided Policy Learning for Long-Horizon Language Agents\" (arXiv:2605.06078)\n\n### 1. Does the paper exist? What are its actual results?\n\n**Yes, the paper exists.** It was submitted to arXiv on May 7, 2026, by Zixuan Wang, Yuchen Yan, Hongxing Li, Teng Pan, Dingming Li, Ruiqing Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, and Yongliang Shen (ZJU-REAL group).\n\n**Actual results:**\n\n| Benchmark | Qwen2.5-1.5B | Qwen2.5-7B |\n|-----------|-------------|------------|\n| ALFWorld (Short) | 96.8% | 95.1% |\n| ALFWorld (Medium) | 87.0% | 94.9% |\n| ALFWorld (Long) | 92.9% | 90.0% |\n| ALFWorld (Average) | 91.4% | **94.5%** |\n| WebShop | 75.6% | **79.7%** |\n| ScienceWorld | 45.3% | 64.3% |\n\nThe headline number often cited from the abstract (92.9%) is specifically the **long-horizon ALFWorld** result at **1.5B**, not the overall average.\n\n### 2. Does it use environment-native milestone signals with temporal decay shaping?\n\n**Yes to both.**\n\n- **Environment-native milestones:** The milestone detector Phi \"detects observable state changes from environment feedback\" and \"does not require learned models or manual annotation.\" In ALFWorld these are object state changes (pick-up, heating completion); in WebShop they are page transitions toward the target product; in ScienceWorld the environment provides explicit subgoal signals.\n- **Temporal decay shaping:** The paper applies temporal reward shaping that \"assigns higher credit to actions closer to milestone completion\" with a decay factor gamma = 0.95 across all benchmarks.\n\n### 3. Model sizes and the specific numbers 94.5% / 79.7%?\n\n**Model sizes:** Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct.\n\n**Yes, both numbers are confirmed at 7B:**\n- **94.5% on ALFWorld** (average across short/medium/long) with Qwen2.5-7B\n- **79.7% on WebShop** with Qwen2.5-7B\n\nThese are the paper's actual reported results.\n\n### 4. Formal PBRS or informal shaping?\n\n**Informal shaping.** The paper does NOT use formal potential-based reward shaping (PBRS). It applies an informal temporal reward decay within milestone-delimited segments. There is no mention of potential functions or the PBRS theoretical framework (Ng et al., 1999).\n\n### 5. What codebase does it build on?\n\nBEACON builds on **verl-agent** (https://github.com/langfengQ/verl-agent), which itself extends **veRL** (https://github.com/volcengine/verl). The technical stack includes PyTorch 2.6.0, CUDA 12.4, vLLM 0.8.5, and Flash Attention 2.7.4. BEACON's own contributions are isolated in `migpo/` (advantage and reward computation) and `agent_system/` (environment integrations), inheriting most RL training infrastructure from verl-agent.\n\n---\n\nSources:\n- [arXiv Abstract: 2605.06078](https://arxiv.org/abs/2605.06078)\n- [Full HTML Paper: 2605.06078](https://arxiv.org/html/2605.06078)\n- [GitHub: ZJU-REAL/BEACON](https://github.com/ZJU-REAL/BEACON)"
      }
    ],
    "totalDurationMs": 66341,
    "totalTokens": 16424,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 465,
      "cache_read_input_tokens": 14979,
      "output_tokens": 979,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 465
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 979,
          "cache_read_input_tokens": 14979,
          "cache_creation_input_tokens": 465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 465,
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
  "sourceToolAssistantUUID": "a303a65a-ea5c-4b10-954d-4d13838916c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-11T23:55:30.555Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GXRv2diKnT3cnFb9pwWPbP`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify Self-Guide and TIPS papers",
  "prompt": "Search for and verify these two papers:\n\n1. \"Self-Guide: Co-Evolution of Policy and Internal Reward for Language Agents\" (arXiv:2604.03098, April 2026)\n   - Does it exist? Does it explicitly acknowledge the non-PBRS bias problem and cite Ng et al. 1999?\n   - Does it use a trapezoid annealing schedule to withdraw internal rewards?\n   - What results does it achieve?\n\n2. \"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs\" (ICLR 2026)\n   - Does it exist? Is it actually at ICLR 2026?\n   - Does it use formal PBRS with teacher-model log-likelihood over gold answers?\n   - Is it designed for QA/search tasks rather than interactive environments?\n\nUse WebSearch and WebFetch. Try multiple queries for each paper. Report everything you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "353afd35-f9bc-4d2b-9b33-cadd6e791e56",
  "isSidechain": false,
  "requestId": "req_011Cawgf6cRE6tcQ58Y6cuVT",
  "type": "assistant",
  "uuid": "fdfd1d32-c7e7-4a18-91b8-4b96bb64f81c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7icM8LRpZAf5TLRA8bDUu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1635,
      "cache_read_input_tokens": 27441,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1635,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 317,
          "cache_read_input_tokens": 27441,
          "cache_creation_input_tokens": 1635,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1635
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

_source line 13 · 2026-05-11T23:56:57.631Z_

<details><summary>↩ Tool result · `toolu_01GXRv2diKnT3cnFb9pwWPbP`</summary>

```text
Now I have all the information needed. Let me compile the full report.

---

## Paper 1: "Self-Guide: Co-Evolution of Policy and Internal Reward for Language Agents"

### Existence and Identity
**Confirmed to exist.** arXiv ID 2604.03098, submitted April 3, 2026. The method is explicitly called "Self-Guide" in the paper. Authors: Xinyu Wang, Hanwei Wu, Jingwei Song, Shuyuan Zhang, Jiayi Zhang, Fanqi Kong, Tung Sum Thomas Kwok, Xiao-Wen Chang, Yuyu Luo, Chenglin Wu, Bang Liu.

### Non-PBRS Bias Problem and Ng et al. 1999 Citation
**Yes to both.** The paper explicitly acknowledges the non-PBRS bias problem. It states: *"Because the self-guidance-derived reward is not potential-based, retaining it indefinitely would bias the converged policy away from the true environment objective."* It directly cites **Ng et al. (1999) "Policy invariance under reward transformations: theory and application to reward shaping"** in Section 3.5 as the theoretical foundation for why this bias matters.

### Trapezoid Annealing Schedule
**Yes, confirmed.** The paper proposes a four-phase "trapezoid schedule" (Equation 10) to withdraw internal rewards:
- **Phase I:** Guidance-only (lambda = 0)
- **Phase II:** Linear ramp from 0 to 1
- **Phase III:** Full strength (lambda = 1)
- **Phase IV:** Linear annealing from 1 to 0

Ablation studies (Figure 5, Section 4.4) validate this structure, showing that skipping annealing or using immediate full reward both degrade results.

### Results
Evaluated across three interactive agent benchmarks using GRPO, with Qwen3-4B:
- **ALFWorld:** 86.7% (GRPO baseline) -> 96.9% (+10.2%)
- **ScienceWorld:** 71.9% -> 78.1% (+6.2%)
- **WebShop:** 84.3% -> 87.8% (+3.5%)

Improvements are consistent across 1.7B, 4B, and 7B model scales. The overall improvement is approximately 8% over baselines trained solely with environment reward.

---

## Paper 2: "TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs"

### Existence and Venue
**Confirmed to exist and confirmed at ICLR 2026.** Accepted as an **ICLR 2026 Poster** (submission #3519). Published January 26, 2026 on OpenReview; arXiv preprint is 2603.22293. Authors: Yutao Xie, Nathaniel Thomas, Nicklas Hansen, Yang Fu, Li Erran Li, Xiaolong Wang (UCSD Wang Lab). Code available at `github.com/ucsd-wang-lab-lm/tips`.

### Formal PBRS with Teacher-Model Log-Likelihood
**Partially correct -- uses PBRS, but the "teacher model" is actually a frozen copy of the policy itself, not a separate teacher.** The potential function is formally defined as:

**Phi(S) := L(S; A) = log sum_{m=1}^{M} p_teach(A^(m) | S)**

This is the teacher's log-probability of generating any correct answer given context S. The turn-level reward is the difference in potential: **Delta_k = alpha * [Phi(S_k) - Phi(S_{k-1})]**.

The paper explicitly frames this as standard potential-based reward shaping and cites **Ng et al. (1999)** multiple times (Section 3.2 and Appendix F). However, the "teacher" is a **frozen copy of the policy model itself, periodically refreshed** -- not a separate, stronger teacher model. Ablation studies (Table 6) showed that using different/stronger teacher models actually degraded performance; the frozen policy copy worked best.

So: formal PBRS -- yes. Teacher-model log-likelihood over gold answers -- technically yes, but the "teacher" is a frozen self-copy, not an external teacher.

### Domain: QA/Search vs. Interactive Environments
**Confirmed: designed specifically for QA/search tasks, NOT interactive environments.** The framework targets "search-augmented large language models" for "open-domain question answering" where agents interleave reasoning with retrieval tool calls. This is fundamentally different from interactive environments like ALFWorld or WebShop (which Self-Guide targets).

### Results
Evaluated on seven QA benchmarks with Qwen-2.5-7B Instruct:
- **In-domain:** Natural Questions (NQ), HotpotQA
- **Out-of-domain:** TriviaQA, PopQA, 2WikiMultiHopQA, MuSiQue, Bamboogle
- **Additional:** BrowseComp-Plus

Performance: TIPS improves average Exact Match by **11.8%** and F1 by **13.6%** over PPO. It consistently outperforms both PPO and GRPO baselines and substantially improves training stability.

---

## Summary of Verification

| Claim | Verdict |
|-------|---------|
| Self-Guide exists at arXiv:2604.03098 (April 2026) | **TRUE** |
| Self-Guide acknowledges non-PBRS bias and cites Ng et al. 1999 | **TRUE** -- explicitly does both |
| Self-Guide uses trapezoid annealing schedule | **TRUE** -- four-phase trapezoid (Eq. 10) |
| TIPS exists at ICLR 2026 | **TRUE** -- accepted as poster |
| TIPS uses formal PBRS with teacher-model log-likelihood over gold answers | **MOSTLY TRUE** -- uses formal PBRS with log-likelihood of gold answers, but the "teacher" is a frozen self-copy, not a separate teacher model |
| TIPS is for QA/search rather than interactive environments | **TRUE** |

Sources:
- [Self-Guide on arXiv](https://arxiv.org/abs/2604.03098)
- [Self-Guide HTML version](https://arxiv.org/html/2604.03098)
- [TIPS on arXiv](https://arxiv.org/abs/2603.22293)
- [TIPS on OpenReview (ICLR 2026)](https://openreview.net/forum?id=eBMOr6a84z)
- [TIPS HTML version](https://arxiv.org/html/2603.22293v1)
- [TIPS GitHub repository](https://github.com/ucsd-wang-lab-lm/tips)

agentId: a41b6c49438027517 (use SendMessage with to: 'a41b6c49438027517' to continue this agent)
&lt;usage>total_tokens: 19235
tool_uses: 10
duration_ms: 87071&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdfd1d32-c7e7-4a18-91b8-4b96bb64f81c",
  "isSidechain": false,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "type": "user",
  "uuid": "d4d521d5-15d0-4f8a-b42b-ec4bf28a0afb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify these two papers:\n\n1. \"Self-Guide: Co-Evolution of Policy and Internal Reward for Language Agents\" (arXiv:2604.03098, April 2026)\n   - Does it exist? Does it explicitly acknowledge the non-PBRS bias problem and cite Ng et al. 1999?\n   - Does it use a trapezoid annealing schedule to withdraw internal rewards?\n   - What results does it achieve?\n\n2. \"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs\" (ICLR 2026)\n   - Does it exist? Is it actually at ICLR 2026?\n   - Does it use formal PBRS with teacher-model log-likelihood over gold answers?\n   - Is it designed for QA/search tasks rather than interactive environments?\n\nUse WebSearch and WebFetch. Try multiple queries for each paper. Report everything you find.",
    "agentId": "a41b6c49438027517",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Let me compile the full report.\n\n---\n\n## Paper 1: \"Self-Guide: Co-Evolution of Policy and Internal Reward for Language Agents\"\n\n### Existence and Identity\n**Confirmed to exist.** arXiv ID 2604.03098, submitted April 3, 2026. The method is explicitly called \"Self-Guide\" in the paper. Authors: Xinyu Wang, Hanwei Wu, Jingwei Song, Shuyuan Zhang, Jiayi Zhang, Fanqi Kong, Tung Sum Thomas Kwok, Xiao-Wen Chang, Yuyu Luo, Chenglin Wu, Bang Liu.\n\n### Non-PBRS Bias Problem and Ng et al. 1999 Citation\n**Yes to both.** The paper explicitly acknowledges the non-PBRS bias problem. It states: *\"Because the self-guidance-derived reward is not potential-based, retaining it indefinitely would bias the converged policy away from the true environment objective.\"* It directly cites **Ng et al. (1999) \"Policy invariance under reward transformations: theory and application to reward shaping\"** in Section 3.5 as the theoretical foundation for why this bias matters.\n\n### Trapezoid Annealing Schedule\n**Yes, confirmed.** The paper proposes a four-phase \"trapezoid schedule\" (Equation 10) to withdraw internal rewards:\n- **Phase I:** Guidance-only (lambda = 0)\n- **Phase II:** Linear ramp from 0 to 1\n- **Phase III:** Full strength (lambda = 1)\n- **Phase IV:** Linear annealing from 1 to 0\n\nAblation studies (Figure 5, Section 4.4) validate this structure, showing that skipping annealing or using immediate full reward both degrade results.\n\n### Results\nEvaluated across three interactive agent benchmarks using GRPO, with Qwen3-4B:\n- **ALFWorld:** 86.7% (GRPO baseline) -> 96.9% (+10.2%)\n- **ScienceWorld:** 71.9% -> 78.1% (+6.2%)\n- **WebShop:** 84.3% -> 87.8% (+3.5%)\n\nImprovements are consistent across 1.7B, 4B, and 7B model scales. The overall improvement is approximately 8% over baselines trained solely with environment reward.\n\n---\n\n## Paper 2: \"TIPS: Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs\"\n\n### Existence and Venue\n**Confirmed to exist and confirmed at ICLR 2026.** Accepted as an **ICLR 2026 Poster** (submission #3519). Published January 26, 2026 on OpenReview; arXiv preprint is 2603.22293. Authors: Yutao Xie, Nathaniel Thomas, Nicklas Hansen, Yang Fu, Li Erran Li, Xiaolong Wang (UCSD Wang Lab). Code available at `github.com/ucsd-wang-lab-lm/tips`.\n\n### Formal PBRS with Teacher-Model Log-Likelihood\n**Partially correct -- uses PBRS, but the \"teacher model\" is actually a frozen copy of the policy itself, not a separate teacher.** The potential function is formally defined as:\n\n**Phi(S) := L(S; A) = log sum_{m=1}^{M} p_teach(A^(m) | S)**\n\nThis is the teacher's log-probability of generating any correct answer given context S. The turn-level reward is the difference in potential: **Delta_k = alpha * [Phi(S_k) - Phi(S_{k-1})]**.\n\nThe paper explicitly frames this as standard potential-based reward shaping and cites **Ng et al. (1999)** multiple times (Section 3.2 and Appendix F). However, the \"teacher\" is a **frozen copy of the policy model itself, periodically refreshed** -- not a separate, stronger teacher model. Ablation studies (Table 6) showed that using different/stronger teacher models actually degraded performance; the frozen policy copy worked best.\n\nSo: formal PBRS -- yes. Teacher-model log-likelihood over gold answers -- technically yes, but the \"teacher\" is a frozen self-copy, not an external teacher.\n\n### Domain: QA/Search vs. Interactive Environments\n**Confirmed: designed specifically for QA/search tasks, NOT interactive environments.** The framework targets \"search-augmented large language models\" for \"open-domain question answering\" where agents interleave reasoning with retrieval tool calls. This is fundamentally different from interactive environments like ALFWorld or WebShop (which Self-Guide targets).\n\n### Results\nEvaluated on seven QA benchmarks with Qwen-2.5-7B Instruct:\n- **In-domain:** Natural Questions (NQ), HotpotQA\n- **Out-of-domain:** TriviaQA, PopQA, 2WikiMultiHopQA, MuSiQue, Bamboogle\n- **Additional:** BrowseComp-Plus\n\nPerformance: TIPS improves average Exact Match by **11.8%** and F1 by **13.6%** over PPO. It consistently outperforms both PPO and GRPO baselines and substantially improves training stability.\n\n---\n\n## Summary of Verification\n\n| Claim | Verdict |\n|-------|---------|\n| Self-Guide exists at arXiv:2604.03098 (April 2026) | **TRUE** |\n| Self-Guide acknowledges non-PBRS bias and cites Ng et al. 1999 | **TRUE** -- explicitly does both |\n| Self-Guide uses trapezoid annealing schedule | **TRUE** -- four-phase trapezoid (Eq. 10) |\n| TIPS exists at ICLR 2026 | **TRUE** -- accepted as poster |\n| TIPS uses formal PBRS with teacher-model log-likelihood over gold answers | **MOSTLY TRUE** -- uses formal PBRS with log-likelihood of gold answers, but the \"teacher\" is a frozen self-copy, not a separate teacher model |\n| TIPS is for QA/search rather than interactive environments | **TRUE** |\n\nSources:\n- [Self-Guide on arXiv](https://arxiv.org/abs/2604.03098)\n- [Self-Guide HTML version](https://arxiv.org/html/2604.03098)\n- [TIPS on arXiv](https://arxiv.org/abs/2603.22293)\n- [TIPS on OpenReview (ICLR 2026)](https://openreview.net/forum?id=eBMOr6a84z)\n- [TIPS HTML version](https://arxiv.org/html/2603.22293v1)\n- [TIPS GitHub repository](https://github.com/ucsd-wang-lab-lm/tips)"
      }
    ],
    "totalDurationMs": 87071,
    "totalTokens": 19235,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1399,
      "cache_read_input_tokens": 16174,
      "output_tokens": 1661,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1399
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1661,
          "cache_read_input_tokens": 16174,
          "cache_creation_input_tokens": 1399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1399,
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
  "sourceToolAssistantUUID": "fdfd1d32-c7e7-4a18-91b8-4b96bb64f81c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-11T23:57:09.793Z_

<details open><summary>🔧 Tool call — Agent · `toolu_014gsuqsYwC2P5h4Gq7PTBqB`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for PBRS in LLM agents",
  "prompt": "I'm reviewing a paper idea that proposes using formal potential-based reward shaping (PBRS, Ng et al. 1999) with environment-native potential functions for LLM agent RL training. I need to find if anyone has ALREADY done this — specifically applying formal PBRS with environment-derived potential functions (not learned models) in LLM agent training.\n\nSearch for:\n1. \"potential-based reward shaping\" + \"LLM agent\" or \"language agent\" 2025-2026\n2. \"PBRS\" + \"ALFWorld\" or \"WebShop\" or \"agent training\"\n3. \"reward shaping\" + \"PDDL\" + \"language model\" or \"LLM\"\n4. \"potential function\" + \"agentic RL\" or \"agent reinforcement learning\"\n5. \"environment reward shaping\" + \"policy invariance\" + \"LLM\"\n6. Check if there's any work from Jan-May 2026 that formalizes environment signals as PBRS potentials for agent RL\n\nAlso search for:\n7. \"RewardFlow\" (arXiv:2603.18859) - verify it exists and what it does\n8. \"GiGPO\" - verify NeurIPS 2025 and its results on ALFWorld/WebShop\n9. Any other recent (2026) methods for step-level credit in agentic RL that the idea might be missing\n\nBe thorough - use WebSearch with multiple query variations. Report all findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4d521d5-15d0-4f8a-b42b-ec4bf28a0afb",
  "isSidechain": false,
  "requestId": "req_011CawgnfeDQGyfkwY9o2diV",
  "type": "assistant",
  "uuid": "91855de1-ce67-4a84-ac02-d1c718c37556",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqUCBaTxUVQoEWyW2At4z9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 29076,
      "output_tokens": 448,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 448,
          "cache_read_input_tokens": 29076,
          "cache_creation_input_tokens": 2053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2053
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

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "91855de1-ce67-4a84-ac02-d1c718c37556",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Environment-native PBRS for agentic RL training",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c"
}
```

---

### Tool result

_source line 17 · 2026-05-12T00:01:44.465Z_

<details><summary>↩ Tool result · `toolu_014gsuqsYwC2P5h4Gq7PTBqB`</summary>

```text
I now have a thorough picture of the landscape. Here is my comprehensive report.

---

## Comprehensive Literature Search Report: Formal PBRS with Environment-Native Potentials for LLM Agent RL Training

### Executive Summary

**No existing work was found that does exactly what the proposed paper describes** -- applying formal potential-based reward shaping (Ng et al. 1999) with environment-derived potential functions (not learned models) specifically for LLM agent RL training. This appears to be a genuine gap. However, several closely related papers touch on overlapping pieces of this idea, and the proposed work would need to carefully position itself against them.

---

### 1. Closest Related Work (Partial Overlaps)

#### TIPS (arXiv:2603.22293, March 2026) -- MOST RELEVANT
- **What it does:** Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs. Explicitly uses formal PBRS from Ng et al. 1999, proves policy invariance, and applies the shaping formula F(s,s') = alpha * [Phi(s_k) - Phi(s_{k-1})].
- **Critical distinction from proposed idea:** The potential function Phi(S) = log sum_m p_teach(A^(m)|S) is **model-derived** (log-probability of correct answer under a frozen teacher copy of the policy), NOT environment-derived. It is applied to QA benchmarks (NQ, TriviaQA, HotpotQA, etc.), NOT to agentic environments like ALFWorld or WebShop.
- **Gap it leaves open:** Formalizing environment-native signals (inventory changes, page scores, task milestones) as potential functions.
- [Paper](https://arxiv.org/abs/2603.22293) | [Code](https://github.com/ucsd-wang-lab-lm/tips)

#### RewardFlow (arXiv:2603.18859, March 2026) -- VERIFIED EXISTS
- **What it does:** Constructs state graphs from environment states, propagates terminal outcome rewards backward through topology-aware graph propagation to estimate state-level dense rewards. Uses the reward difference R(s_{t+1}) - R(s_t) which structurally resembles PBRS.
- **Critical distinction:** Does NOT cite Ng et al. 1999, does NOT prove policy invariance, and does NOT frame its approach as formal PBRS. The state graph IS constructed from environment states (nodes = distinct environment states, edges = observed actions). Tested on ALFWorld, WebShop, Sokoban, and DeepResearch.
- **Relationship to proposed idea:** RewardFlow uses environment topology but lacks the formal PBRS framing. The proposed paper could argue that RewardFlow is an instance of informal/implicit PBRS without theoretical guarantees.
- [Paper](https://arxiv.org/abs/2603.18859)

#### BEACON (arXiv:2605.06078, May 2026) -- VERY RECENT
- **What it does:** Milestone-guided policy learning that uses environment-native milestone detection (e.g., detecting object state changes like successful pick-up or heating completion in ALFWorld). Applies temporal reward shaping within segments using exponential decay.
- **Critical distinction:** Uses environment-derived signals, but does NOT use formal PBRS. Does not cite Ng et al. 1999. No policy invariance proof. Results: 92.9% on ALFWorld (nearly doubling GRPO's 53.5%).
- **Relationship:** Closest to using environment-native signals, but lacks formal PBRS theory.
- [Paper](https://arxiv.org/abs/2605.06078) | [Code](https://github.com/ZJU-REAL/BEACON)

#### STO-RL (arXiv:2601.08107, January 2026)
- **What it does:** Explicitly uses formal PBRS (Ng et al. 1999) with LLM-generated subgoal temporal orderings as the potential function. Proves policy invariance.
- **Critical distinction:** Trains a **traditional RL agent** (IQL), NOT an LLM agent. Potential is LLM-derived (not environment-native). Tests on grid-world navigation (CliffWalking, FourRoom, PointMaze), not ALFWorld/WebShop.
- [Paper](https://arxiv.org/abs/2601.08107)

---

### 2. GiGPO -- Verified (NeurIPS 2025)

- **Confirmed:** Published at NeurIPS 2025 as a poster ([OpenReview](https://openreview.net/forum?id=QXEhBMNrCW)).
- **What it does:** Group-in-Group Policy Optimization. Two-level advantage estimation -- episode-level macro advantages + step-level anchor state grouping for fine-grained credit. Critic-free, low memory, stable convergence.
- **Results:** >12% gain on ALFWorld, >9% on WebShop over GRPO. Tested with Qwen2.5-1.5B/3B/7B.
- **Relationship:** Addresses step-level credit but does NOT use PBRS or environment-derived potentials.
- [Paper](https://arxiv.org/abs/2505.10978) | [Code](https://github.com/langfengQ/verl-agent)

---

### 3. Other Recent Methods for Step-Level Credit in Agentic RL (2025-2026)

These are methods the proposed paper should cite and differentiate from:

| Method | Year/Venue | Approach | Environment-Native? | Formal PBRS? |
|--------|-----------|----------|---------------------|---------------|
| **iStar/OPRL** | ICLR 2026 | Implicit PRM via trajectory DPO | No (learned model) | No (Bradley-Terry) |
| **SSVPO** | ICLR 2026 | Sequential Shapley Values | No (game-theoretic) | No |
| **HCAPO** | March 2026 | Hindsight credit via LLM self-critique | No (model-based) | No |
| **HiPER** | Feb 2026 | Hierarchical planner-executor with HAE | Partial (subgoals) | No |
| **GEPO** | Oct 2025 | Graph-based centrality rewards | Yes (state-transition graph) | No |
| **Planner-R1** | NeurIPS 2025 | Dense process-level reward curriculum | No | No |
| **AgentPRM** | ACM Web 2026 | Step-wise promise and progress PRM | No (learned) | No |
| **RTMC** | April 2026 | Rollout Tree Monte Carlo | No (rollout-based) | No |
| **C3** | March 2026 | Counterfactual leave-one-out credit | No (causal model) | No |
| **Progressive RS** | Dec 2025 | Curriculum-based stage-wise feedback | No | No |

Key observation: **None of these use formal PBRS with environment-native potentials.**

---

### 4. Adjacent Work Using LLMs for PBRS (But NOT for LLM Agent Training)

- **"Extracting Heuristics from LLMs for Reward Shaping"** (arXiv:2405.15194): Uses LLMs to generate PBRS heuristics for traditional RL agents (PPO, A2C, Q-learning) in BabyAI/Minecraft. Withdrawn from ICLR 2025. Trains traditional RL agents, not LLMs.
- **Text2Reward** (ICLR 2024): LLMs generate reward code for robotics RL. Not PBRS-formal, not for LLM agents.

---

### 5. The Credit Assignment Survey (arXiv:2604.09459, April 2026)

A comprehensive survey covering 47 credit assignment methods (2024-early 2026). Organizes by granularity (token/segment/step/turn) and methodology (Monte Carlo/TD/model-based/game-theoretic/information-theoretic). **Confirmed: the survey does NOT mention any work applying formal PBRS with environment-derived potentials for LLM agent training.** This corroborates that the proposed idea is novel.

---

### 6. Summary of Gap Analysis

The proposed paper sits at an intersection that no existing work occupies:

| Dimension | TIPS | RewardFlow | BEACON | STO-RL | Proposed |
|-----------|------|------------|--------|--------|----------|
| Formal PBRS (Ng 1999) | Yes | No | No | Yes | Yes |
| Policy invariance proof | Yes | No | No | Yes | Yes |
| Environment-native potential | No (model) | Yes (topology) | Yes (milestones) | No (LLM) | Yes |
| LLM agent training | Yes (QA) | Yes (agentic) | Yes (agentic) | No (trad. RL) | Yes |
| ALFWorld/WebShop | No | Yes | Yes | No | Yes |

The proposed contribution -- **formal PBRS + environment-native potentials + LLM agent RL training** -- appears genuinely novel as of May 2026. The strongest positioning would be:
- Against TIPS: "We use environment-derived potentials rather than model-derived, applying PBRS to agentic environments"
- Against RewardFlow/BEACON: "We provide formal PBRS guarantees (policy invariance) that these methods lack"
- Against STO-RL: "We train LLM agents, not traditional RL agents"

---

Sources:
- [TIPS: Turn-Level Information-Potential Reward Shaping](https://arxiv.org/abs/2603.22293)
- [RewardFlow: Topology-Aware Reward Propagation](https://arxiv.org/abs/2603.18859)
- [BEACON: Milestone-Guided Policy Learning](https://arxiv.org/abs/2605.06078)
- [GiGPO: Group-in-Group Policy Optimization (NeurIPS 2025)](https://openreview.net/forum?id=QXEhBMNrCW)
- [iStar/OPRL: Implicit Step Rewards (ICLR 2026)](https://arxiv.org/abs/2509.19199)
- [SSVPO: Sequential Shapley Value Policy Optimization (ICLR 2026)](https://openreview.net/forum?id=g33DGvnHYd)
- [STO-RL: Subgoal Temporal Order Reward Shaping](https://arxiv.org/abs/2601.08107)
- [HiPER: Hierarchical RL with Explicit Credit Assignment](https://arxiv.org/abs/2602.16165)
- [GEPO: Graph-Enhanced Policy Optimization](https://arxiv.org/abs/2510.26270)
- [HCAPO: Hindsight Credit Assignment](https://arxiv.org/abs/2603.08754)
- [Planner-R1: Reward Shaping for Agentic RL](https://arxiv.org/abs/2509.25779)
- [Credit Assignment Survey (47 papers)](https://arxiv.org/abs/2604.09459)
- [Extracting Heuristics from LLMs for Reward Shaping](https://arxiv.org/abs/2405.15194)
- [AgentPRM: Process Reward Models for LLM Agents](https://arxiv.org/abs/2511.08325)
- [C3: Contextual Counterfactual Credit Assignment](https://arxiv.org/abs/2603.06859)
- [RTMC: Step-Level Credit via Rollout Trees](https://arxiv.org/abs/2604.11037)
- [Progressive Reward Shaping](https://arxiv.org/abs/2512.07478)

agentId: a1e7add93ddd5d18f (use SendMessage with to: 'a1e7add93ddd5d18f' to continue this agent)
&lt;usage>total_tokens: 50662
tool_uses: 42
duration_ms: 274668&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91855de1-ce67-4a84-ac02-d1c718c37556",
  "isSidechain": false,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "type": "user",
  "uuid": "5288e7bf-e327-4aaa-b9a8-569336b9f9c0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper idea that proposes using formal potential-based reward shaping (PBRS, Ng et al. 1999) with environment-native potential functions for LLM agent RL training. I need to find if anyone has ALREADY done this — specifically applying formal PBRS with environment-derived potential functions (not learned models) in LLM agent training.\n\nSearch for:\n1. \"potential-based reward shaping\" + \"LLM agent\" or \"language agent\" 2025-2026\n2. \"PBRS\" + \"ALFWorld\" or \"WebShop\" or \"agent training\"\n3. \"reward shaping\" + \"PDDL\" + \"language model\" or \"LLM\"\n4. \"potential function\" + \"agentic RL\" or \"agent reinforcement learning\"\n5. \"environment reward shaping\" + \"policy invariance\" + \"LLM\"\n6. Check if there's any work from Jan-May 2026 that formalizes environment signals as PBRS potentials for agent RL\n\nAlso search for:\n7. \"RewardFlow\" (arXiv:2603.18859) - verify it exists and what it does\n8. \"GiGPO\" - verify NeurIPS 2025 and its results on ALFWorld/WebShop\n9. Any other recent (2026) methods for step-level credit in agentic RL that the idea might be missing\n\nBe thorough - use WebSearch with multiple query variations. Report all findings.",
    "agentId": "a1e7add93ddd5d18f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a thorough picture of the landscape. Here is my comprehensive report.\n\n---\n\n## Comprehensive Literature Search Report: Formal PBRS with Environment-Native Potentials for LLM Agent RL Training\n\n### Executive Summary\n\n**No existing work was found that does exactly what the proposed paper describes** -- applying formal potential-based reward shaping (Ng et al. 1999) with environment-derived potential functions (not learned models) specifically for LLM agent RL training. This appears to be a genuine gap. However, several closely related papers touch on overlapping pieces of this idea, and the proposed work would need to carefully position itself against them.\n\n---\n\n### 1. Closest Related Work (Partial Overlaps)\n\n#### TIPS (arXiv:2603.22293, March 2026) -- MOST RELEVANT\n- **What it does:** Turn-Level Information-Potential Reward Shaping for Search-Augmented LLMs. Explicitly uses formal PBRS from Ng et al. 1999, proves policy invariance, and applies the shaping formula F(s,s') = alpha * [Phi(s_k) - Phi(s_{k-1})].\n- **Critical distinction from proposed idea:** The potential function Phi(S) = log sum_m p_teach(A^(m)|S) is **model-derived** (log-probability of correct answer under a frozen teacher copy of the policy), NOT environment-derived. It is applied to QA benchmarks (NQ, TriviaQA, HotpotQA, etc.), NOT to agentic environments like ALFWorld or WebShop.\n- **Gap it leaves open:** Formalizing environment-native signals (inventory changes, page scores, task milestones) as potential functions.\n- [Paper](https://arxiv.org/abs/2603.22293) | [Code](https://github.com/ucsd-wang-lab-lm/tips)\n\n#### RewardFlow (arXiv:2603.18859, March 2026) -- VERIFIED EXISTS\n- **What it does:** Constructs state graphs from environment states, propagates terminal outcome rewards backward through topology-aware graph propagation to estimate state-level dense rewards. Uses the reward difference R(s_{t+1}) - R(s_t) which structurally resembles PBRS.\n- **Critical distinction:** Does NOT cite Ng et al. 1999, does NOT prove policy invariance, and does NOT frame its approach as formal PBRS. The state graph IS constructed from environment states (nodes = distinct environment states, edges = observed actions). Tested on ALFWorld, WebShop, Sokoban, and DeepResearch.\n- **Relationship to proposed idea:** RewardFlow uses environment topology but lacks the formal PBRS framing. The proposed paper could argue that RewardFlow is an instance of informal/implicit PBRS without theoretical guarantees.\n- [Paper](https://arxiv.org/abs/2603.18859)\n\n#### BEACON (arXiv:2605.06078, May 2026) -- VERY RECENT\n- **What it does:** Milestone-guided policy learning that uses environment-native milestone detection (e.g., detecting object state changes like successful pick-up or heating completion in ALFWorld). Applies temporal reward shaping within segments using exponential decay.\n- **Critical distinction:** Uses environment-derived signals, but does NOT use formal PBRS. Does not cite Ng et al. 1999. No policy invariance proof. Results: 92.9% on ALFWorld (nearly doubling GRPO's 53.5%).\n- **Relationship:** Closest to using environment-native signals, but lacks formal PBRS theory.\n- [Paper](https://arxiv.org/abs/2605.06078) | [Code](https://github.com/ZJU-REAL/BEACON)\n\n#### STO-RL (arXiv:2601.08107, January 2026)\n- **What it does:** Explicitly uses formal PBRS (Ng et al. 1999) with LLM-generated subgoal temporal orderings as the potential function. Proves policy invariance.\n- **Critical distinction:** Trains a **traditional RL agent** (IQL), NOT an LLM agent. Potential is LLM-derived (not environment-native). Tests on grid-world navigation (CliffWalking, FourRoom, PointMaze), not ALFWorld/WebShop.\n- [Paper](https://arxiv.org/abs/2601.08107)\n\n---\n\n### 2. GiGPO -- Verified (NeurIPS 2025)\n\n- **Confirmed:** Published at NeurIPS 2025 as a poster ([OpenReview](https://openreview.net/forum?id=QXEhBMNrCW)).\n- **What it does:** Group-in-Group Policy Optimization. Two-level advantage estimation -- episode-level macro advantages + step-level anchor state grouping for fine-grained credit. Critic-free, low memory, stable convergence.\n- **Results:** >12% gain on ALFWorld, >9% on WebShop over GRPO. Tested with Qwen2.5-1.5B/3B/7B.\n- **Relationship:** Addresses step-level credit but does NOT use PBRS or environment-derived potentials.\n- [Paper](https://arxiv.org/abs/2505.10978) | [Code](https://github.com/langfengQ/verl-agent)\n\n---\n\n### 3. Other Recent Methods for Step-Level Credit in Agentic RL (2025-2026)\n\nThese are methods the proposed paper should cite and differentiate from:\n\n| Method | Year/Venue | Approach | Environment-Native? | Formal PBRS? |\n|--------|-----------|----------|---------------------|---------------|\n| **iStar/OPRL** | ICLR 2026 | Implicit PRM via trajectory DPO | No (learned model) | No (Bradley-Terry) |\n| **SSVPO** | ICLR 2026 | Sequential Shapley Values | No (game-theoretic) | No |\n| **HCAPO** | March 2026 | Hindsight credit via LLM self-critique | No (model-based) | No |\n| **HiPER** | Feb 2026 | Hierarchical planner-executor with HAE | Partial (subgoals) | No |\n| **GEPO** | Oct 2025 | Graph-based centrality rewards | Yes (state-transition graph) | No |\n| **Planner-R1** | NeurIPS 2025 | Dense process-level reward curriculum | No | No |\n| **AgentPRM** | ACM Web 2026 | Step-wise promise and progress PRM | No (learned) | No |\n| **RTMC** | April 2026 | Rollout Tree Monte Carlo | No (rollout-based) | No |\n| **C3** | March 2026 | Counterfactual leave-one-out credit | No (causal model) | No |\n| **Progressive RS** | Dec 2025 | Curriculum-based stage-wise feedback | No | No |\n\nKey observation: **None of these use formal PBRS with environment-native potentials.**\n\n---\n\n### 4. Adjacent Work Using LLMs for PBRS (But NOT for LLM Agent Training)\n\n- **\"Extracting Heuristics from LLMs for Reward Shaping\"** (arXiv:2405.15194): Uses LLMs to generate PBRS heuristics for traditional RL agents (PPO, A2C, Q-learning) in BabyAI/Minecraft. Withdrawn from ICLR 2025. Trains traditional RL agents, not LLMs.\n- **Text2Reward** (ICLR 2024): LLMs generate reward code for robotics RL. Not PBRS-formal, not for LLM agents.\n\n---\n\n### 5. The Credit Assignment Survey (arXiv:2604.09459, April 2026)\n\nA comprehensive survey covering 47 credit assignment methods (2024-early 2026). Organizes by granularity (token/segment/step/turn) and methodology (Monte Carlo/TD/model-based/game-theoretic/information-theoretic). **Confirmed: the survey does NOT mention any work applying formal PBRS with environment-derived potentials for LLM agent training.** This corroborates that the proposed idea is novel.\n\n---\n\n### 6. Summary of Gap Analysis\n\nThe proposed paper sits at an intersection that no existing work occupies:\n\n| Dimension | TIPS | RewardFlow | BEACON | STO-RL | Proposed |\n|-----------|------|------------|--------|--------|----------|\n| Formal PBRS (Ng 1999) | Yes | No | No | Yes | Yes |\n| Policy invariance proof | Yes | No | No | Yes | Yes |\n| Environment-native potential | No (model) | Yes (topology) | Yes (milestones) | No (LLM) | Yes |\n| LLM agent training | Yes (QA) | Yes (agentic) | Yes (agentic) | No (trad. RL) | Yes |\n| ALFWorld/WebShop | No | Yes | Yes | No | Yes |\n\nThe proposed contribution -- **formal PBRS + environment-native potentials + LLM agent RL training** -- appears genuinely novel as of May 2026. The strongest positioning would be:\n- Against TIPS: \"We use environment-derived potentials rather than model-derived, applying PBRS to agentic environments\"\n- Against RewardFlow/BEACON: \"We provide formal PBRS guarantees (policy invariance) that these methods lack\"\n- Against STO-RL: \"We train LLM agents, not traditional RL agents\"\n\n---\n\nSources:\n- [TIPS: Turn-Level Information-Potential Reward Shaping](https://arxiv.org/abs/2603.22293)\n- [RewardFlow: Topology-Aware Reward Propagation](https://arxiv.org/abs/2603.18859)\n- [BEACON: Milestone-Guided Policy Learning](https://arxiv.org/abs/2605.06078)\n- [GiGPO: Group-in-Group Policy Optimization (NeurIPS 2025)](https://openreview.net/forum?id=QXEhBMNrCW)\n- [iStar/OPRL: Implicit Step Rewards (ICLR 2026)](https://arxiv.org/abs/2509.19199)\n- [SSVPO: Sequential Shapley Value Policy Optimization (ICLR 2026)](https://openreview.net/forum?id=g33DGvnHYd)\n- [STO-RL: Subgoal Temporal Order Reward Shaping](https://arxiv.org/abs/2601.08107)\n- [HiPER: Hierarchical RL with Explicit Credit Assignment](https://arxiv.org/abs/2602.16165)\n- [GEPO: Graph-Enhanced Policy Optimization](https://arxiv.org/abs/2510.26270)\n- [HCAPO: Hindsight Credit Assignment](https://arxiv.org/abs/2603.08754)\n- [Planner-R1: Reward Shaping for Agentic RL](https://arxiv.org/abs/2509.25779)\n- [Credit Assignment Survey (47 papers)](https://arxiv.org/abs/2604.09459)\n- [Extracting Heuristics from LLMs for Reward Shaping](https://arxiv.org/abs/2405.15194)\n- [AgentPRM: Process Reward Models for LLM Agents](https://arxiv.org/abs/2511.08325)\n- [C3: Contextual Counterfactual Credit Assignment](https://arxiv.org/abs/2603.06859)\n- [RTMC: Step-Level Credit via Rollout Trees](https://arxiv.org/abs/2604.11037)\n- [Progressive Reward Shaping](https://arxiv.org/abs/2512.07478)"
      }
    ],
    "totalDurationMs": 274668,
    "totalTokens": 50662,
    "totalToolUseCount": 42,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3704,
      "cache_read_input_tokens": 44018,
      "output_tokens": 2939,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3704
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2939,
          "cache_read_input_tokens": 44018,
          "cache_creation_input_tokens": 3704,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3704,
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
      "otherToolCount": 42
    }
  },
  "sourceToolAssistantUUID": "91855de1-ce67-4a84-ac02-d1c718c37556",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-12T00:02:04.476Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SyUkbx54fKjfp4Qc5hQ4VG`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify verl-agent and compute estimates",
  "prompt": "I need to verify several things for a paper review:\n\n1. **verl-agent codebase**: Search for \"github.com/langfengQ/verl-agent\" — does it exist? Does it support ALFWorld, WebShop, and GRPO training? Does it support Qwen2.5-7B-Instruct?\n\n2. **Compute estimates**: The paper claims ~362s/iteration for 7B GRPO training (citing GiGPO paper). With 150 iterations per run and 12 runs (3 conditions × 2 environments × 2 seeds), they estimate ~192h H100. Verify:\n   - Is 362s/iteration realistic for 7B GRPO on H100?\n   - ALFWorld rollout collection — how long does it typically take? Is there a CPU bottleneck?\n   - WebShop rollout collection — is there HTTP latency?\n\n3. **Self-Guide results**: The idea claims Self-Guide achieves results with annealing. But Self-Guide (arXiv:2604.03098) reports 96.9% on ALFWorld with Qwen3-4B. This is HIGHER than BEACON's 94.5% at 7B. Does this undermine BEACON's SOTA claim? Search for the latest ALFWorld leaderboard/results.\n\n4. **ARR deadline**: Verify that the ACL Rolling Review (ARR) submission deadline for EMNLP 2026 is May 25, 2026. Search for \"EMNLP 2026 ARR deadline\" or \"ACL Rolling Review May 2026 deadline\".\n\nUse WebSearch and WebFetch to verify all of the above."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5288e7bf-e327-4aaa-b9a8-569336b9f9c0",
  "isSidechain": false,
  "requestId": "req_011Cawh9ottxWDguABgHcxJJ",
  "type": "assistant",
  "uuid": "fc190550-78f8-475a-a90d-c1d4856c0e2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115CDwv5HbDYQqDhtUtLq6J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3467,
      "cache_read_input_tokens": 31129,
      "output_tokens": 493,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3467,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 493,
          "cache_read_input_tokens": 31129,
          "cache_creation_input_tokens": 3467,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3467
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

_source line 19 · 2026-05-12T00:04:28.730Z_

<details><summary>↩ Tool result · `toolu_01SyUkbx54fKjfp4Qc5hQ4VG`</summary>

```text
Now I have all the information needed. Let me compile the comprehensive findings.

---

Here are my findings for each of the four verification items:

## 1. verl-agent Codebase

**The repository exists** at [github.com/langfengQ/verl-agent](https://github.com/langfengQ/verl-agent). It is the official code for the GiGPO paper ("Group-in-Group Policy Optimization for LLM Agent Training").

- **ALFWorld**: Supported
- **WebShop**: Supported
- **GRPO training**: Supported (along with PPO, DAPO, GSPO, RLOO, REINFORCE++, and GiGPO)
- **Qwen2.5-7B-Instruct**: Explicitly supported. The README reports a 90.8% success rate on ALFWorld with this model. The framework also supports Qwen3, Qwen2.5-VL, LLaMA3.2, and others.
- **Hardware**: 7B models require 4x H100 GPUs; 1.5B models use 2x H100 GPUs. LoRA support is available to reduce compute.

**Verdict**: The codebase claim checks out fully.

## 2. Compute Estimates

**Critical finding: The ~362s/iteration figure is for the 1.5B model, NOT the 7B model.**

The GiGPO paper (Section 5.5, Figure 6) explicitly states: "we train an LLM agent in ALFWorld using **Qwen2.5-1.5B-Instruct** and record a detailed breakdown of per-iteration training time." The total time per iteration for the dominant operations (rollouts, old/ref probability computation, policy updates) is 362.83s. The paper does **not** report per-iteration timing for the 7B model.

This means:
- **The paper's claim of ~362s/iteration for 7B GRPO is misattributed.** The GiGPO paper's 362s figure applies to a 1.5B model on 2x H100s. A 7B model on 4x H100s would likely be significantly slower per iteration (roughly 3-5x, though the exact ratio depends on parallelism efficiency, batch size, and sequence lengths).
- **The ~192 H100-hour estimate is therefore likely a significant underestimate.** Recalculating: if 7B takes ~1000-1800s/iteration (a reasonable scaling estimate), 150 iterations x 12 runs = 1800 runs of iterations, totaling 500-900 H100-hours rather than 192.
- **Rollout bottleneck**: Literature confirms rollout generation consumes over 70% of total training time in synchronous RL systems. ALFWorld involves 30-50 step multi-turn interactions, which are CPU-bound when running environment simulations. WebShop involves HTTP-based web interaction, adding variable network latency. Both environments contribute to the straggler problem where a few long rollouts block entire batches.

**Verdict**: The 362s/iteration figure is cited incorrectly for 7B -- it is actually a 1.5B benchmark. The total compute estimate of ~192 H100-hours is likely a substantial underestimate.

## 3. Self-Guide Results and BEACON's SOTA Claim

**Self-Guide (arXiv:2604.03098) results on ALFWorld:**
- **Qwen3-4B with GRPO + Self-Guide + Guidance Reward: 96.9%** (confirmed from the paper's tables)
- Qwen2.5-7B-Instruct with GRPO + Self-Guide + Guidance Reward: 95.3%
- Qwen3-1.7B with full Self-Guide: 89.8%

**This does complicate BEACON's SOTA claim.** If BEACON reports 94.5% on ALFWorld with a 7B model, then:
- Self-Guide achieves 96.9% with a **smaller** Qwen3-4B model
- Self-Guide achieves 95.3% with the **same** Qwen2.5-7B-Instruct model
- Both exceed BEACON's reported 94.5%

**Furthermore, even more recent work surpasses these:**
- [Skill1](https://arxiv.org/html/2605.06130) achieves **97.5%** on ALFWorld (current SOTA)
- [RetroAgent](https://arxiv.org/html/2605.06130) achieves 94.9%
- [GiGPO](https://arxiv.org/html/2505.10978v3) achieves 90.8% (verl-agent baseline)

**Verdict**: BEACON's 94.5% on ALFWorld is not SOTA. Self-Guide (96.9% at 4B) and Skill1 (97.5%) both surpass it. The fact that a smaller 4B model outperforms BEACON's 7B result is a particularly strong counterpoint. However, there may be important caveats around evaluation protocol consistency (same test split, number of evaluation seeds, etc.) that should be examined.

## 4. ARR Deadline for EMNLP 2026

**Confirmed: The ARR submission deadline for EMNLP 2026 is May 25, 2026** (11:59 PM UTC-12:00, "anywhere on Earth").

Key dates from the [official EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/):
- ARR submission deadline: **May 25, 2026**
- Reviewer registration deadline: May 27, 2026
- Author response period: July 7-13, 2026
- Meta review released: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Acceptance notification: August 20, 2026
- Main Conference: October 24-29, 2026

**Important policy note**: For the May 2026 ARR cycle, authors must explicitly declare their target conference (EMNLP or AACL) at submission time, and the choice is **binding**.

**Verdict**: The May 25, 2026 deadline is confirmed.

---

**Summary of key findings for the review:**
1. verl-agent codebase: Fully verified, supports all claimed features.
2. Compute estimates: **Major issue** -- the 362s/iteration figure is for 1.5B, not 7B. The 192 H100-hour estimate is likely a significant underestimate.
3. SOTA claim: **Undermined** -- Self-Guide (96.9% at 4B) and Skill1 (97.5%) both surpass the claimed 94.5% at 7B.
4. ARR deadline: Confirmed as May 25, 2026.

Sources:
- [verl-agent GitHub Repository](https://github.com/langfengQ/verl-agent)
- [GiGPO Paper (arXiv:2505.10978)](https://arxiv.org/html/2505.10978v3)
- [Self-Guide Paper (arXiv:2604.03098)](https://arxiv.org/html/2604.03098)
- [Skill1 Paper (arXiv:2605.06130)](https://arxiv.org/html/2605.06130)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [EMNLP 2026 Twitter Announcement](https://x.com/emnlpmeeting/status/2029508292637061462)
- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)
- [Hugging Face open-r1 GRPO Compute Discussion](https://github.com/huggingface/open-r1/issues/100)

agentId: ae10280c20a04e6b3 (use SendMessage with to: 'ae10280c20a04e6b3' to continue this agent)
&lt;usage>total_tokens: 28965
tool_uses: 23
duration_ms: 144249&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc190550-78f8-475a-a90d-c1d4856c0e2c",
  "isSidechain": false,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "type": "user",
  "uuid": "f6d4e34d-2868-409b-af39-b4ec3beda647",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify several things for a paper review:\n\n1. **verl-agent codebase**: Search for \"github.com/langfengQ/verl-agent\" — does it exist? Does it support ALFWorld, WebShop, and GRPO training? Does it support Qwen2.5-7B-Instruct?\n\n2. **Compute estimates**: The paper claims ~362s/iteration for 7B GRPO training (citing GiGPO paper). With 150 iterations per run and 12 runs (3 conditions × 2 environments × 2 seeds), they estimate ~192h H100. Verify:\n   - Is 362s/iteration realistic for 7B GRPO on H100?\n   - ALFWorld rollout collection — how long does it typically take? Is there a CPU bottleneck?\n   - WebShop rollout collection — is there HTTP latency?\n\n3. **Self-Guide results**: The idea claims Self-Guide achieves results with annealing. But Self-Guide (arXiv:2604.03098) reports 96.9% on ALFWorld with Qwen3-4B. This is HIGHER than BEACON's 94.5% at 7B. Does this undermine BEACON's SOTA claim? Search for the latest ALFWorld leaderboard/results.\n\n4. **ARR deadline**: Verify that the ACL Rolling Review (ARR) submission deadline for EMNLP 2026 is May 25, 2026. Search for \"EMNLP 2026 ARR deadline\" or \"ACL Rolling Review May 2026 deadline\".\n\nUse WebSearch and WebFetch to verify all of the above.",
    "agentId": "ae10280c20a04e6b3",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Let me compile the comprehensive findings.\n\n---\n\nHere are my findings for each of the four verification items:\n\n## 1. verl-agent Codebase\n\n**The repository exists** at [github.com/langfengQ/verl-agent](https://github.com/langfengQ/verl-agent). It is the official code for the GiGPO paper (\"Group-in-Group Policy Optimization for LLM Agent Training\").\n\n- **ALFWorld**: Supported\n- **WebShop**: Supported\n- **GRPO training**: Supported (along with PPO, DAPO, GSPO, RLOO, REINFORCE++, and GiGPO)\n- **Qwen2.5-7B-Instruct**: Explicitly supported. The README reports a 90.8% success rate on ALFWorld with this model. The framework also supports Qwen3, Qwen2.5-VL, LLaMA3.2, and others.\n- **Hardware**: 7B models require 4x H100 GPUs; 1.5B models use 2x H100 GPUs. LoRA support is available to reduce compute.\n\n**Verdict**: The codebase claim checks out fully.\n\n## 2. Compute Estimates\n\n**Critical finding: The ~362s/iteration figure is for the 1.5B model, NOT the 7B model.**\n\nThe GiGPO paper (Section 5.5, Figure 6) explicitly states: \"we train an LLM agent in ALFWorld using **Qwen2.5-1.5B-Instruct** and record a detailed breakdown of per-iteration training time.\" The total time per iteration for the dominant operations (rollouts, old/ref probability computation, policy updates) is 362.83s. The paper does **not** report per-iteration timing for the 7B model.\n\nThis means:\n- **The paper's claim of ~362s/iteration for 7B GRPO is misattributed.** The GiGPO paper's 362s figure applies to a 1.5B model on 2x H100s. A 7B model on 4x H100s would likely be significantly slower per iteration (roughly 3-5x, though the exact ratio depends on parallelism efficiency, batch size, and sequence lengths).\n- **The ~192 H100-hour estimate is therefore likely a significant underestimate.** Recalculating: if 7B takes ~1000-1800s/iteration (a reasonable scaling estimate), 150 iterations x 12 runs = 1800 runs of iterations, totaling 500-900 H100-hours rather than 192.\n- **Rollout bottleneck**: Literature confirms rollout generation consumes over 70% of total training time in synchronous RL systems. ALFWorld involves 30-50 step multi-turn interactions, which are CPU-bound when running environment simulations. WebShop involves HTTP-based web interaction, adding variable network latency. Both environments contribute to the straggler problem where a few long rollouts block entire batches.\n\n**Verdict**: The 362s/iteration figure is cited incorrectly for 7B -- it is actually a 1.5B benchmark. The total compute estimate of ~192 H100-hours is likely a substantial underestimate.\n\n## 3. Self-Guide Results and BEACON's SOTA Claim\n\n**Self-Guide (arXiv:2604.03098) results on ALFWorld:**\n- **Qwen3-4B with GRPO + Self-Guide + Guidance Reward: 96.9%** (confirmed from the paper's tables)\n- Qwen2.5-7B-Instruct with GRPO + Self-Guide + Guidance Reward: 95.3%\n- Qwen3-1.7B with full Self-Guide: 89.8%\n\n**This does complicate BEACON's SOTA claim.** If BEACON reports 94.5% on ALFWorld with a 7B model, then:\n- Self-Guide achieves 96.9% with a **smaller** Qwen3-4B model\n- Self-Guide achieves 95.3% with the **same** Qwen2.5-7B-Instruct model\n- Both exceed BEACON's reported 94.5%\n\n**Furthermore, even more recent work surpasses these:**\n- [Skill1](https://arxiv.org/html/2605.06130) achieves **97.5%** on ALFWorld (current SOTA)\n- [RetroAgent](https://arxiv.org/html/2605.06130) achieves 94.9%\n- [GiGPO](https://arxiv.org/html/2505.10978v3) achieves 90.8% (verl-agent baseline)\n\n**Verdict**: BEACON's 94.5% on ALFWorld is not SOTA. Self-Guide (96.9% at 4B) and Skill1 (97.5%) both surpass it. The fact that a smaller 4B model outperforms BEACON's 7B result is a particularly strong counterpoint. However, there may be important caveats around evaluation protocol consistency (same test split, number of evaluation seeds, etc.) that should be examined.\n\n## 4. ARR Deadline for EMNLP 2026\n\n**Confirmed: The ARR submission deadline for EMNLP 2026 is May 25, 2026** (11:59 PM UTC-12:00, \"anywhere on Earth\").\n\nKey dates from the [official EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/):\n- ARR submission deadline: **May 25, 2026**\n- Reviewer registration deadline: May 27, 2026\n- Author response period: July 7-13, 2026\n- Meta review released: July 30, 2026\n- EMNLP commitment deadline: August 2, 2026\n- Acceptance notification: August 20, 2026\n- Main Conference: October 24-29, 2026\n\n**Important policy note**: For the May 2026 ARR cycle, authors must explicitly declare their target conference (EMNLP or AACL) at submission time, and the choice is **binding**.\n\n**Verdict**: The May 25, 2026 deadline is confirmed.\n\n---\n\n**Summary of key findings for the review:**\n1. verl-agent codebase: Fully verified, supports all claimed features.\n2. Compute estimates: **Major issue** -- the 362s/iteration figure is for 1.5B, not 7B. The 192 H100-hour estimate is likely a significant underestimate.\n3. SOTA claim: **Undermined** -- Self-Guide (96.9% at 4B) and Skill1 (97.5%) both surpass the claimed 94.5% at 7B.\n4. ARR deadline: Confirmed as May 25, 2026.\n\nSources:\n- [verl-agent GitHub Repository](https://github.com/langfengQ/verl-agent)\n- [GiGPO Paper (arXiv:2505.10978)](https://arxiv.org/html/2505.10978v3)\n- [Self-Guide Paper (arXiv:2604.03098)](https://arxiv.org/html/2604.03098)\n- [Skill1 Paper (arXiv:2605.06130)](https://arxiv.org/html/2605.06130)\n- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [EMNLP 2026 Twitter Announcement](https://x.com/emnlpmeeting/status/2029508292637061462)\n- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)\n- [Hugging Face open-r1 GRPO Compute Discussion](https://github.com/huggingface/open-r1/issues/100)"
      }
    ],
    "totalDurationMs": 144249,
    "totalTokens": 28965,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 820,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 25302,
      "output_tokens": 1939,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 904
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 820,
          "output_tokens": 1939,
          "cache_read_input_tokens": 25302,
          "cache_creation_input_tokens": 904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 904,
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
  "sourceToolAssistantUUID": "fc190550-78f8-475a-a90d-c1d4856c0e2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
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
  "leafUuid": "f6d4e34d-2868-409b-af39-b4ec3beda647",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Environment-native PBRS for agentic RL training",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c"
}
```

---

### Tool call

_source line 22 · 2026-05-12T00:04:42.106Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01RzbjqLTqZfSCJMd6gzC4Et`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for counter-evidence PBRS",
  "prompt": "I'm reviewing a paper that claims formal PBRS (potential-based reward shaping, Ng et al. 1999) provides practical advantages over informal/naive reward shaping in LLM agent training. I need to find counter-evidence and critical perspectives:\n\n1. Search for papers showing that PBRS provides NO practical benefit over naive shaping in practice:\n   - \"potential-based reward shaping not necessary\" or \"PBRS unnecessary\"\n   - \"reward shaping without potential function works\" \n   - \"informal reward shaping sufficient\"\n   - Any empirical comparisons where PBRS ≈ naive shaping\n\n2. Search for \"Skill1\" paper (arXiv:2605.06130) that reportedly achieves 97.5% on ALFWorld — verify what method it uses and if it's relevant\n\n3. Search for practical limitations of PBRS in deep RL / LLM contexts:\n   - PBRS assumes MDP structure, but LLM agent environments may be POMDPs\n   - PBRS policy invariance only holds for the optimal policy in the limit — with finite training, does the guarantee matter?\n   - Are there papers discussing PBRS limitations in function approximation settings?\n\n4. Search for \"GEPO graph-enhanced policy optimization\" and \"C3 counterfactual credit assignment\" for agentic RL — these might be additional competitors not cited\n\n5. Search for whether WebShop's scoring function can actually be called at each step (not just at buy time):\n   - \"WebShop environment step reward\" or \"WebShop intermediate reward\"\n   - \"WebShop attribute match score step\"\n\nUse WebSearch. Report all findings."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6d4e34d-2868-409b-af39-b4ec3beda647",
  "isSidechain": false,
  "requestId": "req_011CawhMvBzhPWQt4wk4rwBq",
  "type": "assistant",
  "uuid": "bac3c8e7-059e-460d-af93-1bd2c61c76ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ax31DHWV13se4czXe31eXq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2511,
      "cache_read_input_tokens": 34596,
      "output_tokens": 478,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2511,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 478,
          "cache_read_input_tokens": 34596,
          "cache_creation_input_tokens": 2511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2511
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

_source line 23 · 2026-05-12T00:11:29.203Z_

<details><summary>↩ Tool result · `toolu_01RzbjqLTqZfSCJMd6gzC4Et`</summary>

```text
Now I have enough information to compile a comprehensive report. Here is the full synthesis of findings:

---

## Comprehensive Report: Counter-Evidence and Critical Perspectives on PBRS for LLM Agent Training

### 1. Does PBRS Provide NO Practical Benefit Over Naive Shaping?

**Short answer: The evidence is mixed, not clearly in favor of "PBRS is unnecessary."**

The most relevant empirical comparison comes from **Muller & Kudenko (arXiv 2502.01307, AAMAS 2025)**. Their finding: for high-dimensional locomotion, **PBRS yields smaller speedup but is markedly more robust to scaling of shaping terms** compared to naive additive shaping (NS). This means naive shaping can sometimes give faster initial learning, but is fragile -- if you scale the shaping reward wrong, naive shaping degrades badly while PBRS remains stable. The paper also identifies a real limitation: PBRS effectiveness depends heavily on agent initialization, environment reward structure, and potential scaling. They propose exponential potential functions to fix issues with small potential differences between consecutive states.

**Counter-evidence you can cite:** There are no papers I found that flatly state "PBRS is unnecessary" or show it provides zero benefit. The strongest counter-argument is indirect: **the vast majority of successful agentic RL papers in 2025-2026 do not use formal PBRS at all** -- they use process reward models, hindsight credit assignment, graph-based reward propagation, or simple binary/ratio-based dense rewards. The practical LLM agent community has largely moved past the PBRS framework without apparently suffering for it.

The classic **Randlov & Alstrom (1998) bicycle example** remains the canonical illustration of naive shaping going wrong (the agent learned to ride in circles to accumulate shaping reward), which motivated Ng et al. (1999). However, this is a tabular RL example, not a deep RL or LLM context.

### 2. Skill1 Paper (arXiv 2605.06130)

**Verified:** Skill1 achieves **97.5% success rate on ALFWorld**, surpassing RetroAgent by 2.6 points. It also achieves leading performance on WebShop.

**Method:** Skill1 does NOT use PBRS. It uses a **unified skill-augmented RL framework** where a single policy co-evolves skill selection, utilization, and distillation. All learning derives from a single task-outcome signal, decomposed into low-frequency trend (crediting selection) and high-frequency variation (crediting distillation). It compares against GRPO, PPO, RLOO, and GiGPO. The base RL algorithm appears to be group-based (GRPO-family), not PBRS-based.

**Relevance to your review:** Skill1 is relevant as a **strong competitor that achieves SOTA without PBRS**, suggesting that skill-based augmentation + standard RL is sufficient to reach very high performance on ALFWorld.

### 3. Practical Limitations of PBRS in Deep RL / LLM Contexts

**POMDP issue:** There is a dedicated line of work on extending PBRS to POMDPs. Key paper: **"Potential-Based Reward Shaping for POMDPs" (AAMAS 2013)** and **"Potential-based reward shaping for finite horizon online POMDP planning" (JAAMAS 2015, Springer)**. These show that extending PBRS to POMDPs requires defining potentials over **belief states** rather than true states, which is non-trivial. LLM agent environments (where the agent sees partial HTML, truncated observations, etc.) are indeed POMDPs, making standard PBRS theory not directly applicable.

**Function approximation:** The literature explicitly acknowledges that **"theoretical proofs do not yet exist (and may not even be possible to obtain) when neural nets are used to approximate the value function."** Empirical results suggest policy invariance is maintained in deep RL, but this is not proven. Additionally, numeric instability can bias policies when potentials are learned online -- papers recommend bounding potential ranges and applying terminal corrections.

**Finite training / convergence:** PBRS policy invariance holds **only at convergence** (in the limit). During finite training:
- PBRS "can express nontrivial bias if finite horizons are not properly managed"
- "Practical improvements in sample efficiency are sensitive to the agent's initialization, environment reward structure, and potential scaling"
- Bounding potential ranges and applying terminal corrections is essential to ensure policy ordering is preserved during training

This is a legitimate criticism: if you only train for N steps (as in all practical LLM fine-tuning), the convergence guarantee is irrelevant. What matters is sample efficiency during those N steps, which PBRS does not formally guarantee.

### 4. GEPO and C3 as Competitors

**GEPO (Graph-Enhanced Policy Optimization, arXiv 2510.26270):**
- Constructs a dynamic state-transition graph from agent experience
- Uses graph-theoretic centrality for three signals: (1) structured intrinsic rewards guiding exploration, (2) graph-enhanced advantage for topology-aware credit assignment, (3) dynamic discount factor
- Results: **+4.1% on ALFWorld (94.9% for 7B), +5.3% on WebShop (7B), +10.9% on Workbench** over baselines
- This is directly relevant as a competitor -- it uses graph structure rather than potential functions for dense reward signals

**C3 (Contextual Counterfactual Credit Assignment, arXiv 2603.06859):**
- Uses a leave-one-out (LOO) framework to isolate causal impact of individual messages
- Freezes transcript-derived context and evaluates counterfactual alternatives via fixed-continuation replay
- Evaluated on **five mathematical and coding benchmarks** (not WebShop/ALFWorld specifically)
- Part of a broader trend: three independent hindsight/counterfactual papers (HCAPO, C3, CCPO) appeared within a single week in March 2026, signaling community convergence on retrospective counterfactual analysis as the paradigm for agentic credit assignment

**Additional competitors found:**
- **GiGPO (Group-in-Group Policy Optimization):** Fine-grained credit assignment while remaining critic-free, low memory, stable convergence
- **TIPS (Turn-Level Information-Potential Reward Shaping, arXiv 2603.22293):** Explicitly uses PBRS construction but with learned information-theoretic potentials. Improves EM by 11.8% and F1 by 13.6% over PPO on QA benchmarks. This is notable because it IS potential-based but the potential is learned, not hand-designed.
- **PSPO (Trainable Potential-Based Reward Shaping Policy Optimization):** Makes the potential function trainable, alternating between policy and potential updates. Uses an L-infinity trust region to bound potential drift. Interesting because it shows PBRS needs substantial modification (learned potentials + drift control) to be practical.
- **Planner-R1:** Shows reward shaping enables efficient agentic RL with smaller LLMs (8B), achieving 2.7x improvement over GPT-5 baseline, but uses process-level dense rewards rather than PBRS specifically.
- **RewardFlow:** Constructs state graphs from multiple rollouts and propagates terminal rewards using graph methods to produce dense rewards -- another non-PBRS approach.
- **iStar (Implicit Step Rewards):** General credit-assignment strategy without additional rollouts or explicit step labels.

### 5. WebShop Scoring Function Availability at Each Step

**Finding: WebShop provides reward ONLY at the terminal buy action.** Multiple papers confirm this:

- The **"Practitioner's Guide to Multi-turn Agentic Reinforcement Learning" (arXiv 2510.01132)** explicitly studies reward sparsity in environments including WebShop, noting that "in agentic RL settings, trajectories span 10-100+ turns with environment interactions between each turn, and the reward remains sparse and terminal."

- The **iStar / OPRL paper (arXiv 2509.19199)** addresses WebShop's sparse reward problem specifically, describing how agents receive only terminal feedback.

- The **HCAPO paper (arXiv 2603.08754)** states that environments like WebShop provide "only a scalar reward upon reaching a terminal state."

The reward itself is computed as a **matching score** (considering attributes, type, options, and price of the chosen product vs. the instruction), but this score is only evaluated **when the agent executes the buy action** -- not at intermediate navigation/search steps. During navigation, the reward is 0. This means that any paper claiming to use WebShop's built-in scoring as a per-step reward signal would need to be calling the scoring function in a modified way (e.g., computing hypothetical match scores for products currently being viewed, which is technically possible using the environment's internal API but is NOT the standard reward protocol).

---

### Summary of Key Arguments Against PBRS in LLM Agent Training

1. **Convergence guarantees are irrelevant in practice** -- LLM fine-tuning uses finite training budgets; PBRS guarantees hold only in the limit
2. **LLM environments are POMDPs** -- standard PBRS assumes MDP structure; extending to POMDPs requires belief-state potentials, which are impractical for LLM observation spaces
3. **No proof for function approximation** -- policy invariance under PBRS is unproven with neural network approximators
4. **The field has moved on** -- the most successful agentic RL methods (Skill1, GEPO, GiGPO, HCAPO, C3, RewardFlow, iStar) do not use PBRS; they use graph-based, counterfactual, or process reward model approaches
5. **When PBRS is used, it must be substantially modified** -- TIPS and PSPO use "potential-based" framing but with learned potentials, trust regions, and information-theoretic objectives, far from classical PBRS
6. **Naive shaping can match PBRS** -- Muller & Kudenko show PBRS is more robust but not necessarily faster; in finite training with proper hyperparameter tuning, naive shaping can achieve comparable results

Sources:
- [Improving the Effectiveness of PBRS in RL (arXiv 2502.01307)](https://arxiv.org/abs/2502.01307)
- [Skill1: Unified Evolution of Skill-Augmented Agents (arXiv 2605.06130)](https://arxiv.org/abs/2605.06130)
- [GEPO: Graph-Enhanced Policy Optimization (arXiv 2510.26270)](https://arxiv.org/abs/2510.26270)
- [C3: Contextual Counterfactual Credit Assignment (arXiv 2603.06859)](https://arxiv.org/abs/2603.06859)
- [TIPS: Turn-Level Information-Potential Reward Shaping (arXiv 2603.22293)](https://arxiv.org/abs/2603.22293)
- [PSPO: Trainable Potential-Based Reward Shaping (OpenReview)](https://openreview.net/pdf/716150ef4380523082d62402247e27eb322e5366.pdf)
- [A Practitioner's Guide to Multi-turn Agentic RL (arXiv 2510.01132)](https://arxiv.org/abs/2510.01132)
- [iStar / OPRL: Agentic RL with Implicit Step Rewards (arXiv 2509.19199)](https://arxiv.org/abs/2509.19199)
- [HCAPO: Hindsight Credit Assignment (arXiv 2603.08754)](https://arxiv.org/abs/2603.08754)
- [Potential-Based Reward Shaping for POMDPs (AAMAS 2013)](https://aamas.csc.liv.ac.uk/Proceedings/aamas2013/docs/p1123.pdf)
- [PBRS for Finite Horizon Online POMDP Planning (Springer)](https://link.springer.com/article/10.1007/s10458-015-9292-6)
- [Planner-R1: Reward Shaping for Smaller LLMs (arXiv 2509.25779)](https://arxiv.org/abs/2509.25779)
- [GiGPO: Group-in-Group Policy Optimization (arXiv 2505.10978)](https://arxiv.org/abs/2505.10978)
- [From Reasoning to Agentic: Credit Assignment Survey (arXiv 2604.09459)](https://arxiv.org/html/2604.09459)
- [Comprehensive Overview of Reward Engineering (arXiv 2408.10215)](https://arxiv.org/html/2408.10215v1)
- [WebShop: Towards Scalable Real-World Web Interaction (GitHub)](https://github.com/princeton-nlp/WebShop)
- [Potential-Based Reward Shaping in RL (EmergentMind)](https://www.emergentmind.com/topics/potential-based-reward-shaping)
- [RewardFlow: Propagating Reward in State Graphs (OpenReview)](https://openreview.net/forum?id=5oGJbM5u86)
- [Randlov & Alstrom 1998: Learning to Drive a Bicycle](https://gwern.net/doc/reinforcement-learning/model-free/1998-randlov.pdf)

agentId: a7d2ad15fde0e2e83 (use SendMessage with to: 'a7d2ad15fde0e2e83' to continue this agent)
&lt;usage>total_tokens: 43910
tool_uses: 31
duration_ms: 407092&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bac3c8e7-059e-460d-af93-1bd2c61c76ea",
  "isSidechain": false,
  "promptId": "9711bf0f-3f90-45ae-b6fb-d82a50b6fd6e",
  "type": "user",
  "uuid": "aaa6af9e-ee62-4764-9b7e-b8dacca5ee7c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper that claims formal PBRS (potential-based reward shaping, Ng et al. 1999) provides practical advantages over informal/naive reward shaping in LLM agent training. I need to find counter-evidence and critical perspectives:\n\n1. Search for papers showing that PBRS provides NO practical benefit over naive shaping in practice:\n   - \"potential-based reward shaping not necessary\" or \"PBRS unnecessary\"\n   - \"reward shaping without potential function works\" \n   - \"informal reward shaping sufficient\"\n   - Any empirical comparisons where PBRS ≈ naive shaping\n\n2. Search for \"Skill1\" paper (arXiv:2605.06130) that reportedly achieves 97.5% on ALFWorld — verify what method it uses and if it's relevant\n\n3. Search for practical limitations of PBRS in deep RL / LLM contexts:\n   - PBRS assumes MDP structure, but LLM agent environments may be POMDPs\n   - PBRS policy invariance only holds for the optimal policy in the limit — with finite training, does the guarantee matter?\n   - Are there papers discussing PBRS limitations in function approximation settings?\n\n4. Search for \"GEPO graph-enhanced policy optimization\" and \"C3 counterfactual credit assignment\" for agentic RL — these might be additional competitors not cited\n\n5. Search for whether WebShop's scoring function can actually be called at each step (not just at buy time):\n   - \"WebShop environment step reward\" or \"WebShop intermediate reward\"\n   - \"WebShop attribute match score step\"\n\nUse WebSearch. Report all findings.",
    "agentId": "a7d2ad15fde0e2e83",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to compile a comprehensive report. Here is the full synthesis of findings:\n\n---\n\n## Comprehensive Report: Counter-Evidence and Critical Perspectives on PBRS for LLM Agent Training\n\n### 1. Does PBRS Provide NO Practical Benefit Over Naive Shaping?\n\n**Short answer: The evidence is mixed, not clearly in favor of \"PBRS is unnecessary.\"**\n\nThe most relevant empirical comparison comes from **Muller & Kudenko (arXiv 2502.01307, AAMAS 2025)**. Their finding: for high-dimensional locomotion, **PBRS yields smaller speedup but is markedly more robust to scaling of shaping terms** compared to naive additive shaping (NS). This means naive shaping can sometimes give faster initial learning, but is fragile -- if you scale the shaping reward wrong, naive shaping degrades badly while PBRS remains stable. The paper also identifies a real limitation: PBRS effectiveness depends heavily on agent initialization, environment reward structure, and potential scaling. They propose exponential potential functions to fix issues with small potential differences between consecutive states.\n\n**Counter-evidence you can cite:** There are no papers I found that flatly state \"PBRS is unnecessary\" or show it provides zero benefit. The strongest counter-argument is indirect: **the vast majority of successful agentic RL papers in 2025-2026 do not use formal PBRS at all** -- they use process reward models, hindsight credit assignment, graph-based reward propagation, or simple binary/ratio-based dense rewards. The practical LLM agent community has largely moved past the PBRS framework without apparently suffering for it.\n\nThe classic **Randlov & Alstrom (1998) bicycle example** remains the canonical illustration of naive shaping going wrong (the agent learned to ride in circles to accumulate shaping reward), which motivated Ng et al. (1999). However, this is a tabular RL example, not a deep RL or LLM context.\n\n### 2. Skill1 Paper (arXiv 2605.06130)\n\n**Verified:** Skill1 achieves **97.5% success rate on ALFWorld**, surpassing RetroAgent by 2.6 points. It also achieves leading performance on WebShop.\n\n**Method:** Skill1 does NOT use PBRS. It uses a **unified skill-augmented RL framework** where a single policy co-evolves skill selection, utilization, and distillation. All learning derives from a single task-outcome signal, decomposed into low-frequency trend (crediting selection) and high-frequency variation (crediting distillation). It compares against GRPO, PPO, RLOO, and GiGPO. The base RL algorithm appears to be group-based (GRPO-family), not PBRS-based.\n\n**Relevance to your review:** Skill1 is relevant as a **strong competitor that achieves SOTA without PBRS**, suggesting that skill-based augmentation + standard RL is sufficient to reach very high performance on ALFWorld.\n\n### 3. Practical Limitations of PBRS in Deep RL / LLM Contexts\n\n**POMDP issue:** There is a dedicated line of work on extending PBRS to POMDPs. Key paper: **\"Potential-Based Reward Shaping for POMDPs\" (AAMAS 2013)** and **\"Potential-based reward shaping for finite horizon online POMDP planning\" (JAAMAS 2015, Springer)**. These show that extending PBRS to POMDPs requires defining potentials over **belief states** rather than true states, which is non-trivial. LLM agent environments (where the agent sees partial HTML, truncated observations, etc.) are indeed POMDPs, making standard PBRS theory not directly applicable.\n\n**Function approximation:** The literature explicitly acknowledges that **\"theoretical proofs do not yet exist (and may not even be possible to obtain) when neural nets are used to approximate the value function.\"** Empirical results suggest policy invariance is maintained in deep RL, but this is not proven. Additionally, numeric instability can bias policies when potentials are learned online -- papers recommend bounding potential ranges and applying terminal corrections.\n\n**Finite training / convergence:** PBRS policy invariance holds **only at convergence** (in the limit). During finite training:\n- PBRS \"can express nontrivial bias if finite horizons are not properly managed\"\n- \"Practical improvements in sample efficiency are sensitive to the agent's initialization, environment reward structure, and potential scaling\"\n- Bounding potential ranges and applying terminal corrections is essential to ensure policy ordering is preserved during training\n\nThis is a legitimate criticism: if you only train for N steps (as in all practical LLM fine-tuning), the convergence guarantee is irrelevant. What matters is sample efficiency during those N steps, which PBRS does not formally guarantee.\n\n### 4. GEPO and C3 as Competitors\n\n**GEPO (Graph-Enhanced Policy Optimization, arXiv 2510.26270):**\n- Constructs a dynamic state-transition graph from agent experience\n- Uses graph-theoretic centrality for three signals: (1) structured intrinsic rewards guiding exploration, (2) graph-enhanced advantage for topology-aware credit assignment, (3) dynamic discount factor\n- Results: **+4.1% on ALFWorld (94.9% for 7B), +5.3% on WebShop (7B), +10.9% on Workbench** over baselines\n- This is directly relevant as a competitor -- it uses graph structure rather than potential functions for dense reward signals\n\n**C3 (Contextual Counterfactual Credit Assignment, arXiv 2603.06859):**\n- Uses a leave-one-out (LOO) framework to isolate causal impact of individual messages\n- Freezes transcript-derived context and evaluates counterfactual alternatives via fixed-continuation replay\n- Evaluated on **five mathematical and coding benchmarks** (not WebShop/ALFWorld specifically)\n- Part of a broader trend: three independent hindsight/counterfactual papers (HCAPO, C3, CCPO) appeared within a single week in March 2026, signaling community convergence on retrospective counterfactual analysis as the paradigm for agentic credit assignment\n\n**Additional competitors found:**\n- **GiGPO (Group-in-Group Policy Optimization):** Fine-grained credit assignment while remaining critic-free, low memory, stable convergence\n- **TIPS (Turn-Level Information-Potential Reward Shaping, arXiv 2603.22293):** Explicitly uses PBRS construction but with learned information-theoretic potentials. Improves EM by 11.8% and F1 by 13.6% over PPO on QA benchmarks. This is notable because it IS potential-based but the potential is learned, not hand-designed.\n- **PSPO (Trainable Potential-Based Reward Shaping Policy Optimization):** Makes the potential function trainable, alternating between policy and potential updates. Uses an L-infinity trust region to bound potential drift. Interesting because it shows PBRS needs substantial modification (learned potentials + drift control) to be practical.\n- **Planner-R1:** Shows reward shaping enables efficient agentic RL with smaller LLMs (8B), achieving 2.7x improvement over GPT-5 baseline, but uses process-level dense rewards rather than PBRS specifically.\n- **RewardFlow:** Constructs state graphs from multiple rollouts and propagates terminal rewards using graph methods to produce dense rewards -- another non-PBRS approach.\n- **iStar (Implicit Step Rewards):** General credit-assignment strategy without additional rollouts or explicit step labels.\n\n### 5. WebShop Scoring Function Availability at Each Step\n\n**Finding: WebShop provides reward ONLY at the terminal buy action.** Multiple papers confirm this:\n\n- The **\"Practitioner's Guide to Multi-turn Agentic Reinforcement Learning\" (arXiv 2510.01132)** explicitly studies reward sparsity in environments including WebShop, noting that \"in agentic RL settings, trajectories span 10-100+ turns with environment interactions between each turn, and the reward remains sparse and terminal.\"\n\n- The **iStar / OPRL paper (arXiv 2509.19199)** addresses WebShop's sparse reward problem specifically, describing how agents receive only terminal feedback.\n\n- The **HCAPO paper (arXiv 2603.08754)** states that environments like WebShop provide \"only a scalar reward upon reaching a terminal state.\"\n\nThe reward itself is computed as a **matching score** (considering attributes, type, options, and price of the chosen product vs. the instruction), but this score is only evaluated **when the agent executes the buy action** -- not at intermediate navigation/search steps. During navigation, the reward is 0. This means that any paper claiming to use WebShop's built-in scoring as a per-step reward signal would need to be calling the scoring function in a modified way (e.g., computing hypothetical match scores for products currently being viewed, which is technically possible using the environment's internal API but is NOT the standard reward protocol).\n\n---\n\n### Summary of Key Arguments Against PBRS in LLM Agent Training\n\n1. **Convergence guarantees are irrelevant in practice** -- LLM fine-tuning uses finite training budgets; PBRS guarantees hold only in the limit\n2. **LLM environments are POMDPs** -- standard PBRS assumes MDP structure; extending to POMDPs requires belief-state potentials, which are impractical for LLM observation spaces\n3. **No proof for function approximation** -- policy invariance under PBRS is unproven with neural network approximators\n4. **The field has moved on** -- the most successful agentic RL methods (Skill1, GEPO, GiGPO, HCAPO, C3, RewardFlow, iStar) do not use PBRS; they use graph-based, counterfactual, or process reward model approaches\n5. **When PBRS is used, it must be substantially modified** -- TIPS and PSPO use \"potential-based\" framing but with learned potentials, trust regions, and information-theoretic objectives, far from classical PBRS\n6. **Naive shaping can match PBRS** -- Muller & Kudenko show PBRS is more robust but not necessarily faster; in finite training with proper hyperparameter tuning, naive shaping can achieve comparable results\n\nSources:\n- [Improving the Effectiveness of PBRS in RL (arXiv 2502.01307)](https://arxiv.org/abs/2502.01307)\n- [Skill1: Unified Evolution of Skill-Augmented Agents (arXiv 2605.06130)](https://arxiv.org/abs/2605.06130)\n- [GEPO: Graph-Enhanced Policy Optimization (arXiv 2510.26270)](https://arxiv.org/abs/2510.26270)\n- [C3: Contextual Counterfactual Credit Assignment (arXiv 2603.06859)](https://arxiv.org/abs/2603.06859)\n- [TIPS: Turn-Level Information-Potential Reward Shaping (arXiv 2603.22293)](https://arxiv.org/abs/2603.22293)\n- [PSPO: Trainable Potential-Based Reward Shaping (OpenReview)](https://openreview.net/pdf/716150ef4380523082d62402247e27eb322e5366.pdf)\n- [A Practitioner's Guide to Multi-turn Agentic RL (arXiv 2510.01132)](https://arxiv.org/abs/2510.01132)\n- [iStar / OPRL: Agentic RL with Implicit Step Rewards (arXiv 2509.19199)](https://arxiv.org/abs/2509.19199)\n- [HCAPO: Hindsight Credit Assignment (arXiv 2603.08754)](https://arxiv.org/abs/2603.08754)\n- [Potential-Based Reward Shaping for POMDPs (AAMAS 2013)](https://aamas.csc.liv.ac.uk/Proceedings/aamas2013/docs/p1123.pdf)\n- [PBRS for Finite Horizon Online POMDP Planning (Springer)](https://link.springer.com/article/10.1007/s10458-015-9292-6)\n- [Planner-R1: Reward Shaping for Smaller LLMs (arXiv 2509.25779)](https://arxiv.org/abs/2509.25779)\n- [GiGPO: Group-in-Group Policy Optimization (arXiv 2505.10978)](https://arxiv.org/abs/2505.10978)\n- [From Reasoning to Agentic: Credit Assignment Survey (arXiv 2604.09459)](https://arxiv.org/html/2604.09459)\n- [Comprehensive Overview of Reward Engineering (arXiv 2408.10215)](https://arxiv.org/html/2408.10215v1)\n- [WebShop: Towards Scalable Real-World Web Interaction (GitHub)](https://github.com/princeton-nlp/WebShop)\n- [Potential-Based Reward Shaping in RL (EmergentMind)](https://www.emergentmind.com/topics/potential-based-reward-shaping)\n- [RewardFlow: Propagating Reward in State Graphs (OpenReview)](https://openreview.net/forum?id=5oGJbM5u86)\n- [Randlov & Alstrom 1998: Learning to Drive a Bicycle](https://gwern.net/doc/reinforcement-learning/model-free/1998-randlov.pdf)"
      }
    ],
    "totalDurationMs": 407092,
    "totalTokens": 43910,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 39643,
      "output_tokens": 3299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 967
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3299,
          "cache_read_input_tokens": 39643,
          "cache_creation_input_tokens": 967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 967,
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
      "otherToolCount": 31
    }
  },
  "sourceToolAssistantUUID": "bac3c8e7-059e-460d-af93-1bd2c61c76ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-12T00:12:55.444Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research results. Let me synthesize my findings and produce the review.

## Key Findings:

### BEACON Verification
- **Confirmed**: BEACON exists (arXiv:2605.06078), achieves 94.5% on ALFWorld and 79.7% on WebShop at 7B. Uses informal temporal shaping, NOT formal PBRS. Builds on verl-agent.

### Self-Guide Verification
- **Confirmed**: Self-Guide exists (arXiv:2604.03098), acknowledges non-PBRS bias, uses trapezoid annealing, cites Ng et al. 

Self-Guide actually outperforms BEACON with 96.9% on ALFWorld using only a 4B model, demonstrating superior efficiency despite not using formal PBRS.

### TIPS Verification
- **Confirmed**: TIPS exists at ICLR 2026. Uses formal PBRS but with model-derived frozen potentials rather than environment-native ones, and targets QA/search tasks instead of interactive environments.

### Novelty Assessment
The specific combination of formal PBRS with environment-native potentials applied to LLM agent RL training appears genuinely novel—no existing work combines these elements. However, the individual components and their effectiveness are well-established in the literature.

### Compute Estimates
There's a critical timing discrepancy here. The proposal cites 362s per iteration for 7B GRPO, but that figure actually comes from the GiGPO paper's measurements on 1.5B models. Scaling to 7B would require substantially more compute per iteration, making the 192-hour H100 estimate potentially a significant underestimate. The proposal doesn't adequately account for this scaling difference. So if the actual iteration time is closer to 800-1000 seconds rather than 362, that pushes each run to 33-42 hours and the full 12 runs well over 400 hours, which blows past the 200-hour budget. On the SOTA front, BEACON's 94.5% on ALFWorld isn't actually state-of-the-art—Self-Guide hits 96.9% on 4B and 95.3% on 7B, while Skill1 reaches 97.5%, so claiming it as current SOTA is misleading. For WebShop, the proposal acknowledges the reward is only given at purchase time and proposes calling the scoring function on currently-viewed products as a workaround, which is feasible but deviates from standard evaluation.

There's also a theoretical issue: LLM agent environments are POMDPs rather than MDPs, but the PBRS guarantees the proposal relies on only hold for MDPs. Beyond that, even when PBRS guarantees do apply, they're only valid at convergence with infinite training, and in practice with finite LLM environments, the actual value of those guarantees becomes questionable.

Looking at the empirical evidence, Self-Guide already achieves 96.9% on ALFWorld using a simpler heuristic annealing approach, which outperforms both BEACON and what EN-PBRS appears to deliver. The paper also overlooks stronger baselines like GEPO (94.9%) and Skill1 (97.5%), both of which achieve competitive or superior results without relying on formal PBRS guarantees. The "fragile hypothesis" framing attempts to address this, but Scenario C—where EN-PBRS performs similarly to naive approaches—seems most likely given the literature, and in that case the actual contributions become quite limited.

That said, the proposal has genuinely improved through the iterations. The experimental setup is solid with clean conditions and multiple seeds, the codebase choice is well-grounded, and the three-scenario framing thoughtfully acknowledges different outcomes. The differentiation from related work like TIPS, BEACON, and Self-Guide is articulated clearly, and the authors are honest about generalizability constraints. The core idea of combining formal PBRS theory with environment-native potentials for LLM agents does represent genuine novelty, even if the practical impact remains uncertain.

But there are real limitations that temper my assessment. The theoretical guarantee around policy invariance may not translate to practical benefits, the approach only works for environments with pre-defined progress metrics, and the most plausible empirical result—EN-PBRS performing similarly to naive baselines—would yield only incremental contributions. The field is moving quickly, and EN-PBRS is unlikely to outperform existing methods like Self-Guide or Skill1. There's also a concerning gap in the compute budget: the actual runtime could hit 400-500 hours, which overshoots the stated 200-hour limit by a factor of 2-2.5x.

Looking at the scoring, novelty lands around 3/5—the specific combination is new, but PBRS itself is decades old, and applying it to LLM agents with environment signals feels like a relatively incremental extension. Feasibility also sits at 3/5, primarily because of the compute uncertainty. estimated. The 362s/iteration figure is for 1.5B, not 7B. Real compute likely exceeds 200h budget. Timeline is tight.
- **Clarity**: 4/5 — The proposal is well-structured, addresses reviewer concerns, and the experimental design is clear.
- **Impact**: 2.5/5 — Limited to environments with pre-defined progress metrics. The practical benefit of formal PBRS over informal shaping is unclear. The field is achieving excellent results without PBRS.

Average: (3 + 3 + 4 + 2.5) / 4 = 3.125

This is below the 4.0 threshold. Verdict: **revise** (or potentially fail given this is round 3 and the fundamental impact concern persists).

The proposal does have genuine strengths though — the zero-cost framing is sound, the comparison against BEACON using identical signals is a clean experimental design, and the three-scenario contribution structure shows intellectual honesty. But the compute underestimate is a hard constraint violation, and the impact problem is structural: it's difficult to make PBRS compelling in 2026 when the field has already moved beyond it. My final scores remain Novelty 3/5, Feasibility 2.5/5, Clarity 4/5, Impact 2.5/5, averaging to 3.0 — clearly below threshold, so the verdict is revise. The critical issues are the compute estimate being based on 1.5B timing rather than 7B (likely requiring 400-500h instead of the budgeted 200h) and the structural impact concern that persists. Let me recalculate the compute more carefully. The GiGPO baseline shows 362 seconds per iteration on 2 H100s, which translates to 724 H100-seconds per iteration. Scaling to 7B on 4 GPUs accounts for the 4.7x model size increase and doubled GPU count, putting each iteration around 850-1000 seconds of wallclock time. That's roughly 166.8 H100-hours per run, and across 12 runs I'm looking at around 2000 H100-hours total—well beyond what's feasible.

But I should double-check what the proposal actually means by their 192-hour estimate. They're calculating 150 iterations × 362 seconds per iteration ≈ 15 hours of wallclock per run, then 12 runs × 15 hours ≈ 181 hours with some buffer, which seems to assume the same iteration time as the baseline.

The key issue is whether "H100-hours" refers to wallclock time or total GPU compute time. If it's GPU-hours and they're using 4 GPUs, then 15 hours wallclock becomes 60 GPU-hours per run, totaling 720 GPU-hours across 12 runs—well over the 200 H100-hour budget.

But I'm realizing the convention might be ambiguous across papers. Some treat "GPU hours" as wallclock time on a GPU setup, while others mean total compute. The user's constraint of "≤200 H100-hours total" typically implies GPU-hours in ML, but I should check how similar work reports this before concluding there's a fundamental error in the proposal.

The real problem is that the 362s/iteration figure is for 1.5B, not 7B—if I correct for the larger model, the wallclock estimate would roughly double. I think "revise" is the right verdict here, with specific guidance on fixing the compute estimate and the SOTA claims. The work is novel and improving across rounds, but these issues are significant enough to warrant revision rather than acceptance. I'm hesitating on whether "fail" might be more appropriate given the structural concerns about PBRS's practical relevance, though those issues might be addressable with more work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aaa6af9e-ee62-4764-9b7e-b8dacca5ee7c",
  "isSidechain": false,
  "requestId": "req_011CawhtuxUMKEZc9LL38GrC",
  "type": "assistant",
  "uuid": "0463f6f8-b580-4fe5-b518-074df14b9dea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C4xZELmT5uvj8xupcPeLTz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3860,
      "cache_read_input_tokens": 37107,
      "output_tokens": 6291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6291,
          "cache_read_input_tokens": 37107,
          "cache_creation_input_tokens": 3860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3860
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

_source line 25 · 2026-05-12T00:13:49.246Z_

Now let me compile my findings and produce the review. Here's what I've verified:

**Key findings from independent research:**

1. **BEACON verified** — exists at arXiv:2605.06078, achieves 94.5% ALFWorld / 79.7% WebShop at 7B, uses informal temporal shaping (no PBRS). Builds on verl-agent.

2. **Self-Guide verified** — achieves **96.9% on ALFWorld with Qwen3-4B** and **95.3% with Qwen2.5-7B**, both surpassing BEACON's 94.5%. Explicitly acknowledges non-PBRS bias and cites Ng et al. 1999.

3. **Skill1 (arXiv:2605.06130) achieves 97.5% on ALFWorld** — current actual SOTA, not cited.

4. **GEPO achieves 94.9% on ALFWorld at 7B** — not cited.

5. **The 362s/iteration figure is for 1.5B, NOT 7B** (from GiGPO paper Section 5.5). Compute is significantly underestimated.

6. **No existing work does formal PBRS + environment-native potentials + LLM agent training** — the novelty claim is verified as genuine.

7. **PBRS has known limitations**: holds only for MDPs (not POMDPs), only at convergence (not finite training), no proof for neural function approximation.

8. **ARR deadline May 25, 2026 confirmed**.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 3, "rationale": "The specific combination (formal PBRS + environment-native potentials + LLM agent RL) is genuinely novel — no existing work occupies this exact intersection. However, PBRS itself is a 27-year-old technique, and applying it to LLM agents with pre-existing environment signals is a relatively straightforward extension, not a conceptual leap. The 'gap' is real but narrow."},
    "feasibility": {"score": 2, "rationale": "The compute estimate contains a critical error: the 362s/iteration figure cited from GiGPO is for Qwen2.5-1.5B on 2×H100, NOT for 7B. A 7B model on 4×H100 would take ~800-1000s/iteration, doubling wallclock per run. Furthermore, '192 H100-hours' appears to conflate wallclock time with GPU-hours (each run requires 4 GPUs, so 16h wallclock = 64 GPU-hours, not 16). Corrected estimate: ~384-500 GPU-hours, exceeding the 200h hard constraint by 2-2.5×."},
    "clarity": {"score": 4, "rationale": "The proposal is well-structured with a clean experimental design, honest three-scenario contribution framing, and explicit generalizability discussion. The PBRS formulation is precisely specified. The WebShop per-step scoring justification via bidirectional PBRS signals is thoughtful."},
    "impact": {"score": 2, "rationale": "Limited by three structural factors: (1) PBRS theoretical guarantees don't directly apply — agent environments are POMDPs, training is finite, no proof for neural function approximation; (2) restricted to environments with pre-defined progress metrics, excluding the most impactful benchmarks (SWE-bench, WebArena, GAIA); (3) Self-Guide already achieves 96.9% on ALFWorld using heuristic bias mitigation, suggesting formal PBRS provides marginal practical benefit. The most likely empirical outcome (Scenario C: EN-PBRS ≈ naive) yields contributions too modest for a top venue."}
  },
  "issues": [
    "CRITICAL: Compute estimate is based on incorrect per-iteration timing. The 362s/iteration figure from GiGPO (Section 5.5, Figure 6) is explicitly for Qwen2.5-1.5B on 2×H100, NOT 7B. For 7B on 4×H100, per-iteration time is likely ~800-1000s. Additionally, the estimate conflates wallclock hours with GPU-hours (each 7B run requires 4 H100s, so 16h wallclock = 64 GPU-hours). Corrected total: ~384-500 H100-GPU-hours for 12 runs, exceeding the 200h hard constraint by 2-2.5×.",
    "MAJOR: BEACON is NOT the current SOTA on ALFWorld. Self-Guide (arXiv:2604.03098) achieves 96.9% with Qwen3-4B and 95.3% with Qwen2.5-7B-Instruct, both exceeding BEACON's 94.5%. Skill1 (arXiv:2605.06130) achieves 97.5%. GEPO (arXiv:2510.26270) achieves 94.9% at 7B. The framing of BEACON as 'current SOTA' and primary comparison target is inaccurate. If Self-Guide's heuristic annealing approach achieves higher performance than BEACON without formal PBRS, this substantially weakens the argument that formal PBRS is necessary.",
    "MAJOR: PBRS theoretical guarantees do not directly apply to the experimental setting. Three gaps: (1) ALFWorld/WebShop are POMDPs (agent sees partial text observations, not full state), but PBRS policy invariance is proven for MDPs only — extension to POMDPs requires belief-state potentials (Devlin et al., AAMAS 2013); (2) The policy-invariance guarantee holds only at convergence with infinite training, but LLM fine-tuning uses finite training budgets (150 iterations); (3) No theoretical proof exists for PBRS policy invariance under neural network function approximation. The paper should honestly discuss these caveats rather than claiming PBRS provides 'formal guarantees' without qualification.",
    "MAJOR: Missing important competitors — GEPO (arXiv:2510.26270, 94.9% ALFWorld at 7B) uses graph-theoretic centrality for dense rewards from environment states and should be cited as a direct competitor. Skill1 (arXiv:2605.06130, 97.5% ALFWorld) achieves true SOTA. PSPO (trainable potential-based reward shaping) makes PBRS potentials learnable and should be discussed. STO-RL (arXiv:2601.08107) applies formal PBRS with LLM-generated subgoal orderings for traditional RL agents.",
    "MODERATE: The most likely empirical outcome (Scenario C: EN-PBRS ≈ naive shaping) yields contributions insufficient for a top venue. The three claimed contributions in this scenario are weak: (i) 'zero-cost alternative to learned methods' is a valid but incremental contribution that doesn't require the PBRS formalism — BEACON already demonstrates zero-cost environment-native shaping; (ii) 'future-proofing for harder environments' is speculative without empirical evidence; (iii) 'lower training variance' is an empirical claim not guaranteed by PBRS theory (PBRS guarantees policy ranking preservation, not variance reduction).",
    "MODERATE: Self-Guide's success (96.9% ALFWorld) with its trapezoid annealing schedule undermines the core argument that formal PBRS is needed to solve the non-PBRS bias problem. If a simple annealing heuristic not only mitigates the bias but also achieves higher performance than BEACON, the practical motivation for formal PBRS is weakened. The paper needs to directly address why formal PBRS is preferable to Self-Guide's approach given Self-Guide's stronger results.",
    "MINOR: The proposal correctly identifies that WebShop scoring can be called on currently-viewed products, but should note this is non-standard (the environment's reward API is terminal-only at buy time). The engineering required to hook into the scoring function at each step should be explicitly acknowledged as a modification of the standard environment protocol."
  ],
  "feedback": "The idea has improved substantially over three rounds, and the novelty claim (formal PBRS + environment-native potentials for LLM agents) is verified as genuine. However, three issues prevent a pass:\n\n**1. Fix the compute estimate (CRITICAL):** The 362s/iteration figure is for 1.5B, not 7B. You must either: (a) switch to Qwen2.5-1.5B as the primary model (BEACON shows strong 1.5B results: 91.4% ALFWorld, 75.6% WebShop), which would genuinely fit within 200 H100-hours; or (b) correctly estimate 7B compute as ~400-500 GPU-hours and reduce the number of runs (e.g., drop one condition or one environment) to fit the budget. Option (a) is recommended — 1.5B results are publishable in this field and allow more ablations within budget.\n\n**2. Update SOTA landscape and strengthen positioning against Self-Guide:** BEACON is not SOTA. Self-Guide (96.9% at 4B) and Skill1 (97.5%) surpass it. More importantly, Self-Guide's success with heuristic annealing undermines the core motivation for formal PBRS. You need to argue why formal PBRS is better than Self-Guide's approach — possible angles: (a) PBRS requires NO schedule tuning (Self-Guide requires tuning 4 annealing phases), (b) PBRS provides a principled framework that subsumes Self-Guide's approach (Self-Guide's annealing is a heuristic approximation to potential-based withdrawal), (c) Self-Guide requires training an internal reward model while EN-PBRS uses pre-defined potentials at zero cost.\n\n**3. Honestly discuss PBRS's theoretical limitations in your setting:** The policy-invariance guarantee doesn't directly apply (POMDP, finite training, function approximation). Frame the contribution more carefully: 'EN-PBRS uses the PBRS framework as a principled design guideline for reward shaping rather than claiming formal optimality guarantees, and we empirically validate that this principled design leads to more stable training.' This is more honest and still publishable.\n\n**4. Add missing competitors:** Cite GEPO, Skill1, STO-RL, and PSPO. Position EN-PBRS in the landscape table clearly.\n\n**5. Consider narrowing the contribution claim:** Rather than 'PBRS formalism matters for LLM agents,' consider 'zero-cost, environment-native reward shaping achieves competitive performance with learned methods, and PBRS provides a principled, tuning-free framework for designing such signals.' This is defensible regardless of whether EN-PBRS beats naive shaping.",
  "reason": "Compute estimate contains a critical error (362s/iteration is for 1.5B, not 7B) likely exceeding the 200h budget by 2×+; SOTA claims are inaccurate (Self-Guide 96.9% and Skill1 97.5% surpass BEACON's 94.5%); and the practical value of formal PBRS in settings where its theoretical guarantees don't strictly apply remains undemonstrated."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0463f6f8-b580-4fe5-b518-074df14b9dea",
  "isSidechain": false,
  "requestId": "req_011CawhtuxUMKEZc9LL38GrC",
  "type": "assistant",
  "uuid": "d00c3fc4-3587-4316-a8bc-48ba3007618b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C4xZELmT5uvj8xupcPeLTz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3860,
      "cache_read_input_tokens": 37107,
      "output_tokens": 6291,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6291,
          "cache_read_input_tokens": 37107,
          "cache_creation_input_tokens": 3860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3860
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d00c3fc4-3587-4316-a8bc-48ba3007618b",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Environment-native PBRS for agentic RL training",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-11 (UTC).**  Your job: independently verify this idea's claims via WebSearch, then issue a verdict.  ## Us…",
  "leafUuid": "d00c3fc4-3587-4316-a8bc-48ba3007618b",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Environment-native PBRS for agentic RL training",
  "sessionId": "41899480-887b-407e-aeec-9b978a73446c"
}
```

---
